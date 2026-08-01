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
<img src="https://cdn5.telesco.pe/file/FcIsEUqwHUiJMiI4h-c4KPWeEfQJidd04r6LyLlTyPFUmqCVNeNjl2O2piStDSqQ7s7Clk8rn6EE509w8Kh-LXW8ZZ9N7ezY4wzSN4B6X-kSBf3zKWZl0UsIH63SjdFuhq77asCF-0qhMSlwFrM44cL3QATVLz7hUFdrnvMrxUhjePK2khVGYq7x4jPPAfwGmedZ84uM4YquNKN0jbNuyUVmZg3CkvhjVdtfQRlLuKfa-mp6mL63x9PpEyMss0Eniy2EUhBSnv1SaLNrAR_KKziS_16b5QOXnXhhHaL8JZxSrI2gilfogjPKoEDcaWEz0jQrdkgei4HBlRV2TVk3Ug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 504K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 02:55:44</div>
<hr>

<div class="tg-post" id="msg-102541">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=K8IznZSWnVgNFFhHNSYcQ50euXnqmlg7CeMIUtCfsHl1n9ctJAVlkW78O27fQmFOMeTOa1lrVBUWgFTB-sKCn0YKKSD75LKcqcaAw75gWB2VWLbyeG6lcq4iPRexAU5wqr_b2BjzHZpThfaVg1aXLxesWpSGhun7WEK5DxNAm7BX0vhYPBLCKkAR6iM0rP9EYvZ6ioP5a5ejdECjNLfv8dAoCaU8-UNlY9c_ecrzAeR9prxQOi2R2qhidRWg7-dX5daaOA2JBTCdkJGfZ6Z8OrA5WPoujQHAqe5smA7cDdmk_s5VqE7MvNQD8BAHXvhssRAYk7R3nJyI_Vt92WShEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=K8IznZSWnVgNFFhHNSYcQ50euXnqmlg7CeMIUtCfsHl1n9ctJAVlkW78O27fQmFOMeTOa1lrVBUWgFTB-sKCn0YKKSD75LKcqcaAw75gWB2VWLbyeG6lcq4iPRexAU5wqr_b2BjzHZpThfaVg1aXLxesWpSGhun7WEK5DxNAm7BX0vhYPBLCKkAR6iM0rP9EYvZ6ioP5a5ejdECjNLfv8dAoCaU8-UNlY9c_ecrzAeR9prxQOi2R2qhidRWg7-dX5daaOA2JBTCdkJGfZ6Z8OrA5WPoujQHAqe5smA7cDdmk_s5VqE7MvNQD8BAHXvhssRAYk7R3nJyI_Vt92WShEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این تعویض کارلتو که خودشم پشماش ریخت و خندش گرفت؛ بازیکن ۱۸ ساله ۱۸ ثانیه بعد از ورود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/102541" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102540">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4mqedJitNRF6rkZPo1zftI--9rDYWGAMGlm3EsVq6-1hFepkx7C46JgcqGr7bqlIziJk2NTM3rt3U1zxBXMrsfSh_zkVkcwLbdoEklnNQcKiApsok3XZ2N7BvAknU-S4HNp3ZkGvLtSg-dE4yFzsGCXB5A6BD7Edl5znpR1AtIRd7Dk98KXtve3jARVDSoyIz_102Ny3IsHvSgeDLKSlRSUT_wUXGEO-ZLYmXfUe_LiK6f160s0p7e46HnqGt1Y_s3A5ia3P4wL1OSQYmhfDJGWbY4EHGlGdymRAu4RXR8bKqPVyJLs5_dkI3QOsY2-NkpudajEDKUCFEUlrxSobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم پورتو پرتغال برای بار ۲۵‌ام قهرمان سوپرکاپ فوتبال این کشور شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/Futball180TV/102540" target="_blank">📅 01:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102539">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=T3Y7ldJ_JObOz7PCt2gVaM3qIw5QanJvLftxYBCP0xWxM_vv1eFHitbkL7nnCJ4bSB0bJelo2B4QvGHO500mDoLvKd7N04-UaCTlHCnlcpqZBoQS5_9H-GA0Gtw11megndRAy6fxBOVRSRGpzf0l3WbEDZcuhkIlyHkovxD4Ra3XFIAWCmDXG9mEXF4PNKPQucJHaLG3rJEOvX_U4FQf82QDyHWfAMpQDs9kYvC4mRp84ZkP_bxN8jgVs6Vi3KkAN5afOm3y6RqrDmIHlkJTwxd8Z70qt9V3_TdByOqAd59eliSjhXNT2zbmtVRJenFhBtzfEG6AUU423DR_gGvuyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=T3Y7ldJ_JObOz7PCt2gVaM3qIw5QanJvLftxYBCP0xWxM_vv1eFHitbkL7nnCJ4bSB0bJelo2B4QvGHO500mDoLvKd7N04-UaCTlHCnlcpqZBoQS5_9H-GA0Gtw11megndRAy6fxBOVRSRGpzf0l3WbEDZcuhkIlyHkovxD4Ra3XFIAWCmDXG9mEXF4PNKPQucJHaLG3rJEOvX_U4FQf82QDyHWfAMpQDs9kYvC4mRp84ZkP_bxN8jgVs6Vi3KkAN5afOm3y6RqrDmIHlkJTwxd8Z70qt9V3_TdByOqAd59eliSjhXNT2zbmtVRJenFhBtzfEG6AUU423DR_gGvuyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح برگزاری فینال مسابقات زارم کلایه استان گیلان رو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102539" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102538">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqEqd7gdZbi1dUe9g6DC57gOecC17l_jXlF3Tn4mq3iIJjY-K4X6Gp0BEqBBSK3oNco7cR9l8w5THXER7_lJyKXmm7Gljl8x0k2vzVjDl8EbVeHslPns2ZS4VlhZ8-Rg6SfL4xfjxzGKv4LEBxJ6genSDPaeVqCk4VE7e-BQ28Plqr0Dlwpi2MHDictaYOXUYGH_mO_osDRK8JWdRWoumpi0MPtHuhYd5YYJIa0tTeC4Njj2tD7vyZa8EwhQ3NwPAaTkCStO5vGsb8VjR29BmGmZVkJ_if58CXDUzitmKWDZuWz5vmh9cARg8wDOO12J2A5JSb55VqPDlsR7-NObDUZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqEqd7gdZbi1dUe9g6DC57gOecC17l_jXlF3Tn4mq3iIJjY-K4X6Gp0BEqBBSK3oNco7cR9l8w5THXER7_lJyKXmm7Gljl8x0k2vzVjDl8EbVeHslPns2ZS4VlhZ8-Rg6SfL4xfjxzGKv4LEBxJ6genSDPaeVqCk4VE7e-BQ28Plqr0Dlwpi2MHDictaYOXUYGH_mO_osDRK8JWdRWoumpi0MPtHuhYd5YYJIa0tTeC4Njj2tD7vyZa8EwhQ3NwPAaTkCStO5vGsb8VjR29BmGmZVkJ_if58CXDUzitmKWDZuWz5vmh9cARg8wDOO12J2A5JSb55VqPDlsR7-NObDUZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های جنجالی قالیباف درباره لحظات حساس اولین‌روز جنگ با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/102538" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102537">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/102537" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102536">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FhRVZ1p3vUA9mSnKobfgjgPwwWy0A-BZ2HeLO5bandlWkyr9dwa66RGFgvz2e9fXFa2A5xvQn74nV2pgMr5gByA6vhB9aloXZwxMg7-jpQ5WbGRp81crj35kaldrCKXCBgUdSBt0XTFAHD79BACmJSRW8FzJbV_UZr0j4x2n3c9kHfhgwMTuCTa4pQSnH31OGr9ng1Yh4F-2U_9S5g1CHppXsaYIONcFsaSwLGXDh5M9PCK6CRcGEvOf4JqyFdI1SuHsJgy7cqHxhxz1K-zEdn71-eRPo8y1c7F9PVjTM4nIoMswAnvOcHkJqw2AtQpr7fk8AHu9cMHYRVNLj7hsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی
#فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/102536" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102535">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=jXgD_uzKAljLQxdVNlMfnMzQlARduqxP2e0tJYzKOOGFzNeycYkVoljzhArrDBr9J0_50glsWKrUysH_bQ5jJJl7NUyoGMfjdVncPEU7_DBQra759fLbO4wn-kKDX-iAtfxaC5tnpCRYjoczGGqGkKl6gYC_qLr-j3cDPPZGEEj809FUpf1cN9H8Da0rLwU3dzk1bDdZhskoXUtAi8BpSfDv4ChIuSvAk0TG0yz21AmykPhgyftHK5Kqy4ejmWavCjGZHN8WwtplBIgTnk9UUWclB1SEhpXqp-KvVUXi0rY_bY8wiK_D8_CNPflZnIaBybmMYlZw24zUUpPxf_Yr0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=jXgD_uzKAljLQxdVNlMfnMzQlARduqxP2e0tJYzKOOGFzNeycYkVoljzhArrDBr9J0_50glsWKrUysH_bQ5jJJl7NUyoGMfjdVncPEU7_DBQra759fLbO4wn-kKDX-iAtfxaC5tnpCRYjoczGGqGkKl6gYC_qLr-j3cDPPZGEEj809FUpf1cN9H8Da0rLwU3dzk1bDdZhskoXUtAi8BpSfDv4ChIuSvAk0TG0yz21AmykPhgyftHK5Kqy4ejmWavCjGZHN8WwtplBIgTnk9UUWclB1SEhpXqp-KvVUXi0rY_bY8wiK_D8_CNPflZnIaBybmMYlZw24zUUpPxf_Yr0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاخدااااا از این سوپر پاس کاماوینگا به توپ جمع کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102535" target="_blank">📅 00:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102531">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JknzRKYM4_5KGm2KXs9a-a2LV_dApPxOCOrkSdKK8mw9DzaynicoxDSTO-EaeD_EJYUx5moPOdy5Zx87RZ9SYXcQbovq1sA9g14siNPaoTJl_trB2xMw3PyJr5Lns77eTXst5BqVauaVl4sWeuVYn5Va8Fs6c-Urd5iSM7uF1RppQ4rnV-gU7GIP-gQoiWZ2j_fDxNkfliM8DkYsrLw0tpdWv0HdKFwoR1TzuwbV_TZdIr1Pnk_eRllfIFMnLeZ3h5OfBu4Hw_y2cxDYu7mJPwxVKlR6hWgrxPD2i5uA0cuwgHfzzjCbkh61XWIny1V7z_k6qqebUiqwryxcgAEOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH4fCfzuLFS1Dxaok1vh5ogWnRSjxamZUbuNaLdIT0bvgr9OTV6hwl8z9tJK8aPgpILePZNGbfiSE-dvMnWIIdQptnnFD40jk7NQbEpJ0Vmyn7JfZESFs8JsGhABX7IxOx3w6K7NeB9PO_mnsiCn03zwFW1YZ6O7cUV4cNf9F3c9HdWEX5HGc76MGZPU4GZaj1lIeBW0cYBcvzQgEn8gskWYkZIM3B2AftbLe1wx-mqbkU018gyB1p2L1TDjfPVHRREvp809ZrIWF4J4nxgMeRprgy2RTxiQAyIz-PpNszp2M7qQSkUJIGpx_2FeuMdeBaOlAEbZ1Wl3N7r9aQ1CJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYzDJktUan2Nrwzp4tB9NQ8mT05rUxh1ZdExUzWIhRijwyp7Zp6etjZjmPbT0rtPrUQcLxQYA_DP1AQBEbrbngtfCjUfWRcBj8iNdYqNPmXlmWec5XuQXa0TSXfESfNA8deC4FIQpWKHx7t1YaIq0XJcxt0YACbkweF9Y4kMrVgm2kVB-3zqItkDPGWag4umywRn5my65UyXATlZrAqgG9Zc6RBX8RUvk_cH93qFBlmidsCJb9f_3Fc3-Mb4x5YJkG7s1csTZajPcP2WaOT5g3FNSu2xbF-4hKs1a8Suum-s65qHxmBZYBEqa9ErToWK0i0ZiF7jwMmN4yL-IALgRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQL8tpikhzUyf3yu1vuyPD_6M85a5LZ-hmoUkVbw1dy-D_DD95WwpYPtotTkXh6lwOdL8cDtRJIVnIDtWjIZQSBsq7rA6xrOJgtCB3u_VljwLqwbQTeAE9MS76VDhSTvYVMplmjooaRuWvhXvp8YQXrtG9bjP5CPIlXjZF9SvGje1WMQVqWMbUkJzFnbhjrOxoe8nSBHeMPFG2BjZ_1cnFYoSlS8wCr4gXxau9Lo08ELtWNYgrrwzxd3E9VhptVOKiXJpBTFbcHVtd40p5_3oecO-r9P5Y5WkFf2gwtoOprGT37NG4zyUgajkGcpOCIjib4W2oS0AA-sG1kfM7cxRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال وینی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102531" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102530">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twqWlLkXVmKF1HQFMYrOnd2M8-fpmV9WSGyrIMl6hGwsBLTrn6zG70Djl1EQrcNolES4wCcRvXg2eGr657y1dtBtL3nxVtTOr0tsD5Es95fg2BvsMDrnImOIkHNARe6vD2uLjtk6nvQij2YXZuzawRhLXXf3u07Dc4vsbozYmDT_o1tmmlYpIe3SZRCC51MA1frdZhX7BhBGOgxe8fa6ECoBSzc28x7cPwhUrM6koOO-Y0wedvytFict-PAFR-LjWItuCJtWz-1awPJB8U2jOAtj9vcf843JWQi982sSWLNMrYaNrGw1z-voNym3zt6Y19A8mY0N6zz8mV15s9CfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مورینیو بعد از مساوی امروز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102530" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102529">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kox515Y72BUGgFGGtEmFNSzZbDrjvWxSK5rX-YSopoZD5N7Fh5amIHuZ2BjRJVyP-1d_yFQVx6Eh9QNed4JXq7T_ax_kUNB3nz7OjhpxXyhsLkBXSOvXIKGrkR6fS2Gs52MCh0G9UC_KO4soAmzkDGW50VSMPr9uB8T03MQBYHlUgRjIlkMhq8rN5ulvDPQTPmwEoH7ralFi23CdWORQ8nU9aSw-tU7JAYj4oPEYFjJXs8NJ3zOFs0sthtkUfOxb_iS1JghscVbGoeMRLswbcEErsZJfv0l5QHAqRkjcH7P1NPWOUuaSP1xTkm_I5DWAzDeblw4QBKzu-PgENQF_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیمایی که ولبک در اون بازی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102529" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102528">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRVqbnNpHD82jytaMXYvPdEMMyjlnOVqez-NFRFrtKB8REuqGqT8D6_xeAfJfnqaXx3egKW-iVpUBE08_Jb0MvhG6AtPbZ96Z5DKSBA4ohfWfzbsGCBgQ9UeL5b2_Xsg15m9dxWheU-na4FyGCa4lW6gj5CqF_hQLOmlt09KZW6OU7BXB1A73SD8DakWUUOCHnolDco79YxN_Znj2ThJMz0tJRBkEvFhpjWybHzukctKwcP0FlswGoQZRDC0VgHPaxZskxVWyOYFO5qxQkXlBt5vF5-lrgHEAjrx6Jv7tsNpCMzCMCrOiH2mjMJGcwShdcNvPGAG3l7RQ73Qh_dPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال هم تو بازی دوستانه از فیورنتینا کامبک خورد و بازی مساوی تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102528" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102527">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRE_f7iurJeg7UcLCDWdQl7HyCsig1KRk13BAUCRiiuXU7mJpdnR-dmJej0olDVOYd3e1WtcUkt3K0DR_vV77uma7jBKwxF9fYp8bINTyPaf-3w2Q7DAOItV0LRuJXeBrJ3qa3qoaGzZTbkQAiGU1LJUHlnYqbn_6BU7NoXaQPSzMLgKB8o9pz_LpWou605CaQEtKRhwaFLtyE4kEY9ggevURgkCWXu1LK6GtrK99RsDEah54TIzLK-1D1C8aQNrJ6tJYZDrSS5bk2ZcW7TKAG79ZqfZMeEPXToWf0Fc7ZI21CqKa-jLS1qXl6KBLGRwzPHBI1IMqDIlRsJ10iMJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کارلوس اسپی:
🔺
پنجشنبه: بستن قرارداد.
🔺
جمعه: اولین تمرین.
🔺
شنبه: اولین حضور در بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102527" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102526">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEnPaJgz3m16Vbtf754c1LGe-_CKH2KRjk4YV6Yh5NeSBqt30gkRPkVC2ugjVE1EyfVqNumHcYXRs5-cuqNIDAgw0vK8wl01VcxXNBRked29UAh-7g821rTliAGZlXWD-Pmg3pfAE7gxdcq7LvxNoM1i8_DlfNJAzmftmv7ZgetaGZSG0aM1-6Y7suXwkuVbcf_c9ooI26gMy33jD6Rxy3GfFzDD1RDfT95_FCMaB_eoGDIXD79dfJ1cm6C5YhOqDAMMP_prxIYEDnMpxLPa0PGi11MJKn_mKX-O-nYchJQg8jctIUENMkPBAqNPim-IgZdLduqU0xyhJfNW0UAmrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی‌دوستانه|ترکیب آرسنال مقابل ژیرونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102526" target="_blank">📅 20:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102525">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpLdDLned7CzrS_MMladjmqit0-LdwOVRcp0KaHAFWW8qRDsCG0D4Uq6DjNFGmekvc1OtKiMIx7EpQFW0r35JmUkRQPYELwztUec6OBhtYh5rcMDrjHgVy4nNEM2Md-8taupAe7kLeE3bbzC_KbHVDpYUZqE31QeMsliqOPvU1_uNmR-Gr4YJGc-AkPJDO0UUY-gRUKcK6WWYWcLPhqe_r4HjHYdjk7Z8lCxSSzNucj3vYyvith0EmrvWo8O8S-nlXT9tyO6jnMLnBUM3z7tupRNfD77kl59HaPLx2DrRr5I7q3KPOV0GzFJx3Py799fmoiRgMEUS1OPgqDZGHMVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامبد جوان با زنش چیکار میکنه اینجوری شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102525" target="_blank">📅 20:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102524">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jl1uYlRzxyT4LaYjkNF-c-hYYGHo9f3n4JhvqGFg1KOsvwfg2mYvs0yv26GE0LcxtPIqvO_5wRxXDG6YQxh32rf61vgbBNDI9I8gW3Z5mrrl3Lw-U-Tp0M3LomiQGg4BOqYnhiSWmsDlCYDDz0y1Aeh76Gje9h0wb0UgGGax2w8qvLJ-HnEX_6bbUv-huz-SmoHSuBP8AT4xztaeATtu2VqiKJjWfCCpVzL5452sufIVJve3zC3yi7DUELxqtiKesNjwtCaccyIlsH7Fq8GnU14QlNhiGkKYDMMRzZxGB_SOBqtk3ZEhXizzTAjwHlC8Q8oayL-qrc67UVw4BKE9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دنی ولبک رسما به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102524" target="_blank">📅 19:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102523">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glkDk1TpHpEH_xI-sRKyRRbYSdVAPGvp5uZhuaUjCA0Ni01uV68MJFhU96aInrStqNoKPKOhhFq0eQK7i2l9sK-yhHg0aUMNSyUs-slpmY4HeTUJrXvyDG1fBcg5tPXmrI6oeZmO2OQZB7haBDMKmDGtkPNXSP_mnusiyfxLVdB_zMc0ZMwAeGRj_j_bawtAAnkXc1u60CDQ25WKO2KsIGimlXNFBRNoPAzQDX6cF4BdC9a7jeJzqk6vvfzVh1fkWy7a5l98Kj9NlTx7nseurKkXooGPjghwKdNZqfKEUWPJwYtAKm3M5GnTDL8CRSq2AuojX481gmm3LNeb0WHCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جاکوبز:
جایگاه اینفانتینو در فیفا بشدت در خطره و احتمالش زیاده که برکنار بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102523" target="_blank">📅 19:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102522">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFzJwqHhULAWRh4mjkvDg-mSh8MZ5CBQVM4ZuC7ZXAqMM4waIbq5heXz4ZCS5_yxzy1tjmqb8Hji9lM9yOVadbYZAltbD84z_7CeV--3EUDQ-jVUsiWGJXfxBVnnYVqtamQro03-r8ZAagzCRSxn2VAo91E1Kp-AedJlOkm5JsjWXtH4FJE1jPZayj5eWUESHEKEpmPQvvq-pDTMy4KI_ojeRtnDSchjZjRly9AU2vvfIWODFWF59xcHFufHFetmj7sg1lvmo7hdc8JUJNuaglaT1lGd0H3p0WWdiSoBbNdvcSMwk6OLt32Ll8HawAbMmmXuGZ1MWPOHiarodDleBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
🔺
انتقال های رئال مادرید به آرسنال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102522" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102521">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aK3mt4c64I8ukYlsSRD0ghwoS5vi2dQtRPTmeoA1x1sVuJHDbqezeR0bYsq72FXhMiIYcIqo4wJrzLg70ibny0xXo-QKdOntZHQzTuXKzvOPKecHn9q9WaJHva1DcMQc4VDHwctheG7s1tIKSjsSCuGZxHqJskIcZWi-ys_3__B750lS5k-l-a8z_HjpEScw6h7OByq40zVac8VH8EgMDh9yLiIGIcXCsmZTJUzSvIeGg46r8WWAB-bnGkjzMk9PvzWfW9YHWTKIh1IRzetJSaW-AeboA4no0Q-LeAVrKNxlAV99gUkh5E03CuS8AGpOIP7xrgjyqz2PWXdDFOWAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مقابل فیورنتینا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102521" target="_blank">📅 18:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102520">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHbGciny2o4HtLespz4FhB8Y5pJIrPAV9O2yhc5IF2YCe9oEobjcNcyiycmtPjAnjC9PQrRoTz8F88rT8EYdYCRpW_nu_0Fk2g9CwFLTOTcWrcz3Z6zYCyi9WqzeQRV0LGEedEZf1R7ikJ45bm9P1PR4_tFEWWlGGltMTGM24lN9vRvf3qjtUXxAKmeGdW_4HDYpCGaU83Vv2eGo5ssP-fZA0FkcdS2nSIB9t5YDzP-7dQP39ga2CzWJtRy3XvRSiyhVbwzFcm5MKMrTQwHt1O3WPIeIw_mYIGpn5dqDxHy3rdoPkAbO600l9fpTywF-I_rBFT081gOrY-Zyin3FfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوکاسل رسما لخت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102520" target="_blank">📅 17:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102519">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDLtTZskk0arUtgRSQDD3Ged5rlHNDTgTowXMFpA_sdJuyhuEY0GYYXScMfnZitTqytHGpp5KHMjdtdKEOZJQFNAVaif4EzJjESvqy4yHGP72tLNQtrQmkXIuo62rF058KoATdrOyxsM429SkQfSwDfGDGyIvp_RzfLgspb3Y9phW9mTBuisehbLhUDMVGMhFC9xEO9JSHmsSxv94kyc3IB7V-hBLEA5P4S9Xc8_DrUnHHkzNAgftil8ta3UiTz4_LGAuizfAnx8BRMII6F3sp0Z9GMODKFrGDGi-yprhalo2c_h-S9h-5yxpeytpZsDi76yQQEvXDaymM-vFMajaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
چلسی پیشنهاد سه باشگاه اروپایی برای جذب ژائو پدرو را رد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102519" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102518">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSTe5GUpPpf36_5jQhP8745vJLVaF57zuojfzGkbXRmgI5YzLacmSCxsiR16b2PW3lLkVLvm6RgxL5s36Tqzk1lqEnRvlUo1eUwidvhMmSnEpanPd4diDL0Rx3Og6OdaJqabekdc2_rU7cb52qIUaT1ZeYHOXuC8aD0oB5NGoMvxusU8ofM-iIstOq6Hibxbi7WblZv810pSaCYGIMiVzmDf3-kIIoK1C0j4d0K2B37EM2BTZ233VmewSsXLIZQYswrENwwbDAdPh6ILJ5wiA3YRz5uUFatoI-qlEa4m6QIO08HPyN5dAJaIYjwh9ox1Yxg5XHR0OmTn-NxxIbx8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس طاقچه بالا میزاره و ممکنه بره آرسنال؟!
من یک ایده دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102518" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102517">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7VgyjT91wW6SSiC9v2PfrKyo7t2ywUe29hWjEfUCchfHhRkSna2gQhdLKZacEZOPu-qICnV_8ziebjPW89r6zzKJMXDm3BLqXW7f5sJ-O9Dp37dKrnJZNxUoSTzo2H1ZZsf_wryuitA8kQcP1e2Dt90C5eP1NAdXecDipDzZ2Nab-b4_lPU4Ic9gTVSwrA_mt0WnEnjCrUhwVklFUGMaVIIVZLfvSLazbtiO8fpRIQc_MXT91ZMs3KJZp_3BVWVyYlXjUBy0W8gliKhaBCGcTXSxCHyHPNSA6T1SUlpAlSwPHmKwz02eXL1bF5V38CfaRf8Q1jaDlsIB6B6McIcM7JmDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7VgyjT91wW6SSiC9v2PfrKyo7t2ywUe29hWjEfUCchfHhRkSna2gQhdLKZacEZOPu-qICnV_8ziebjPW89r6zzKJMXDm3BLqXW7f5sJ-O9Dp37dKrnJZNxUoSTzo2H1ZZsf_wryuitA8kQcP1e2Dt90C5eP1NAdXecDipDzZ2Nab-b4_lPU4Ic9gTVSwrA_mt0WnEnjCrUhwVklFUGMaVIIVZLfvSLazbtiO8fpRIQc_MXT91ZMs3KJZp_3BVWVyYlXjUBy0W8gliKhaBCGcTXSxCHyHPNSA6T1SUlpAlSwPHmKwz02eXL1bF5V38CfaRf8Q1jaDlsIB6B6McIcM7JmDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چرخ تو اکسپلور میزنی میبینی پر شده از کلیپای عروسی ورژن ایرانی رونالدو و جورجینا
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102517" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102513">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9mPog6CqJWD24_nDW0t33EgqaNDkRe-MvIEKqSIqiOc0IFz8L1Z9zG1tLSwds4igbXmL33RpwsBm-d6iaR3J5id3QbsBmBeHartAqaZX5s_MlX0brRsCPadrmmPTW0CK5R7s4wfKDZqcFv3rV3jiifiTTE0Pjtau7SlgyX28w83iTRVW8OP5I54aHHPmHC7ghlHBCA9TBuHQDL5ezlUnfxCm411HBTvpKYl_QTPtbVtXwzH8Xgeq-bJV_ZoOkrARc9LhB4fyomXuvso7JxN2jUi5dFS7JTvgxWlMTk397Vc_GhyKba0TAWWqTian2by4uXew5LQpS3OfloyUFaI9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/et96n4ctRLLvGR_7CTPF97BW5lp2ZDUzRG-KaQANdhDWICDuvSrQJdW5bIE--bBD4wsU4iPKlkhtnT_155WvQXd-RQESbam2hvs2tAAfA00H4Cv1NDbAoT6U9HnMbyAK0aQkx7PYszDQSBu_K_ayFG1WVqhL5q-Wt9AV3gueQyHcGltHjeFAJTCvCLG_BPpjO-NBNktrlHQmDgUw6rpec3BlyHxvNQwEG3vqj7Mc06bNsQPREQLCUUOo88q64VylLKNooMBSULqxdkrF6UEEIVzsw0hb3tZn7aCqH117gAjx0abtWb24MibNYGjk_RKgW96DX5eRKFgY7ZDsK4XmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2zxW45bJ-6YE8gVkIj46lJZSheQOEY0WA3VtNyw2fDfTtrnI0QIEHZwTcDcndeLIVBLzcg8jL3ZdyDvgMjjZmEBXSyGgmku0_X2boZlqdIn0BPjdZI0i__Su42zsbb6IM-bjD0s_nWpxJHRCZ2ezEYfUJIjgVBPLn9ZsSz7lntTZNv-HtUljoT3YXouU5yEBzAzuYpPVDuV3dlVK46avhvMHOY_GwSBOgkcwtI476nqwbINrTB1CrOxvyqnV_syBjbTg9UhH0f09G56D3lA5BLxoi0wJKLnBsYwTbimDzt_gN8R-PkWEiYYyo_VJOLsYnWqWbZK-OiUXX-Jfw44Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l61Lkd8Uz-GcPmg-QHGLj23gRPH0XPKsYSTpMCe5_JK3nnMDswdc-3eRYccL_ibp2IQwkKIp0h5XbW1a1MN2jUH5vDm8OhHPPgJzYcVVLGka2MmDEYXeXLuq1RsDlOfPLxK8wPrfz6ob5BEq9g4DFyy1LFvQENqktkzyih8a78G5hEUI-4GTQ5wE7wyhJQUOdAwRpzMbULwO-ciW18rNy-UMGmCaQm_sfOjdAgVlRWN4uVOWfo8m3gd0AwHigP7QM1xC4J5i4ialRb71d9GXxWB6Kd2oGOLSYSbwyHxwukEDg_vca4odq5a1M_YjvcH4eEa9GMDa0Ornn6s5gotQDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پستای جدید جورجی جون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102513" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102512">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF0ozzzbzSoPRX8D-DFhceHe4U158gTJNqe1q0gEP8nimrbzEua6XoFu7kC1uBf-_5cjsyYwXrHJH5b9y7pZR2ZgaEdBRzwTNZaa8zWEDz1hOOxT0LVjfPQZgH4Xyc1mucCkI0TIuL3eugFV9lBOWvT43nuQKmBBsdXhhCUCexmEqhSxCVCd1VpOfcbCza6OlEMBNBRUN6_uAclh1IpHV7NBwa9IcshcNsliLBWTmWZdZWQHLpmoF-dsc-H6wpEiTq7OssVi9rCitF3AJvs6XTr9wtsZKrT0QdZ3HhJqcyi1PBjtMYuV8DDEZPQlGmtxgk_nDyHice2sEaH17BAijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔵
اینتر با نتیجه [3-1] در ضربات پنالتی مقابل منچسترسیتی پیروز شد. بازیکنای منچسترسیتی سه پنالتی رو خراب کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102512" target="_blank">📅 17:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102511">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=vKrMMnb0bUQgs82qoy-dIzJU35G2R4gW1OSGZXfCKgbD8uJhZDVmTXWXLOpaHD_YnIXKDHSN5mRz_qpZe8w3I9Ed0UC3vx-fzQhIPNbdefh8jSYKRFAS91rIPDWyM8V2PPNxipxNhf1HylcXdgAbMqEqg_oXtRYelVYGgL497yGmVQJDqM59fMOQq5OltA6J4QfAWiM0SPCdnU1jgPq7pGT-cX1M0sJMD7pN1Gp3AKC2e7iNP_j9RCtIeWRmC4j8uM3p5ZoA3m35rOTbYBa8LOZ1PnXIkErffK_l7gvARV3yHK9lCx5jX19hw6mw0lhiXNAxz2vqz-IbPuLuXTZFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=vKrMMnb0bUQgs82qoy-dIzJU35G2R4gW1OSGZXfCKgbD8uJhZDVmTXWXLOpaHD_YnIXKDHSN5mRz_qpZe8w3I9Ed0UC3vx-fzQhIPNbdefh8jSYKRFAS91rIPDWyM8V2PPNxipxNhf1HylcXdgAbMqEqg_oXtRYelVYGgL497yGmVQJDqM59fMOQq5OltA6J4QfAWiM0SPCdnU1jgPq7pGT-cX1M0sJMD7pN1Gp3AKC2e7iNP_j9RCtIeWRmC4j8uM3p5ZoA3m35rOTbYBa8LOZ1PnXIkErffK_l7gvARV3yHK9lCx5jX19hw6mw0lhiXNAxz2vqz-IbPuLuXTZFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اگر پاس گل پوشکاش داشت، اوزیل بیشترین رو توی افتخارات‌ش میداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102511" target="_blank">📅 17:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102510">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK8fXXuEYGP_r2-UEq176jm0BFwcZ8ygKyjH3YK07C4UdzdXXZYsaNCK8_AvPJmOP8d1BRRRJTpcnl2DqqDcasD4z4_bs3yy1vlHu9D-9_e9ltwYxuCwJBhWbxVRXOyCr48sM_pfr4NyzC1R3C5oIanTcbuV4TWHbFddGPOY45DY_L-D39AgyYpuRam43CHW-HDbEutFkxMq1eY7M5yhRmiCEmFzHxhwEQ2oMoCv5Nc3YJn3oa6Cv2guthKF0-6sntIxShL4q7A9847JtVyb7nGOocEgp5V2NrQFArmaWMAvb2oT_bgKwclN7dpL2OlOUHX8SK7XClsnI0-EhbJAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورنشتین | اگر وینیسیوس با رئال مادرید به توافق نرسه حاضره همین فصل به آرسنال بره.
ماریو کورتگانا: آرسنال ماه‌هاست که برای جذب وینیسیوس به طور مخفیانه حرکت می‌کند. آندریا برتا، مدیر ورزشی، با اطرافیان وینیسیوس گفتگوهایی داشته است. چهره‌های کلیدی آرسنال نیز به نمایندگان او اعلام کرده‌اند که او مهره کلیدی یک پروژه مستحکم خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102510" target="_blank">📅 16:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102509">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzcNNldFcRO37RtUz2tcIwp3nSSb9hLmeez-FoGIMHSEkWnDSm00A6LTb9kWagrmPvN8VHRUataONxhwZF2RXETRRQgyzBtNJ7Fs6Lz0ON9EIbReQfID1w3c84_Ix3vcxiecx0DW7N1s0OXE_auB1icgfP314sxuRgwpLikKNbmPd0gfyb4g4jUlFjDiS17fkUJtchKZSNKZoZawFX3dqZAycmIVqXmR-6Ucx5US4WaRoqSCCeM6RUokzWiBkOaXP2FJOLgBZzQ3mmv2f6r2Y4HmTLg_HoZfbOqG-ErmJG7BwWF-UAKXrORN96qi2jRTreEc0PGsBKutmNpFJZa-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا - ESPN:
طبق اطلاعاتی که به من رسیده، انتقال یان دیومانده به رئال مادرید با مبلغ ۱۲۲ میلیون یورو + ۱۰ میلیون یورو بند پاداش نهایی خواهد شد. همچنین انتقال رودری حدود ۶۵ میلیون یورو هزینه خواهد داشت و باشگاه در حال حاضر منتظر نهایی شدن انتقال بوعدی است.
⚽️
@Futball180TV
‌</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102509" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102508">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDK3XyaCOYOh_Nki8LUYkP-O_Tsa1meXZRuVmd-3dGDNztCiJrpJ1zDBGnauhPFySh1eey4UZKOEcyZqRLZXTL2nQ0fXQGDPxlG-86z3VXjzByz9zT6_TSNwlhQ0QBU-IzRACZ6eYA8xRNeDVVZ-Xclse_8mp-_gDO70FE6bu6pcDqimSMcFqlmuJvdrOHbPUrtRrIdWHT0HPv4sa6E35nAgGS7F8yJ7aTAfA7o1VaP3q_WlgjCmaKfgyBWGlYZHmPO2qLGSEXYxOCf5O1aBCzoVlOOpfLC-52cbrFqwMuXPwgDnbVdoN0wg67emi950zvK7q9tQhQhnWj9O02GpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین شات از عشقتون وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102508" target="_blank">📅 16:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102507">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC3NNI4nfvTJ3ScMGpePfWP_Slvtaj-3lwdfl-llb7agLlRBLfvh9q1xxhrTwcnpHT8ERkwqhEptynD598-_KzveJUjw0dRwLWPB36ROzQHr1KwSJZXZLtI-hbAi5cBLOdHbf2DLhFI23bhzDOu0U7iyybMiHgjRbtwtnlzt1BKy5LtNDGOzFBTcLvwkwemssK54ydRsz3ijCgjsm4Ca-OAklRSo9zfMGtO7VshmSeVUyhhdoTMZ66Mjm13S4VW5iOeRe-FF0ENWLhs6S8AMyxiJ08aijYarJz2_7Z1AX6xqf0AdUcHhfomRnZxNcpgs2z5TX2FGlkGg3ceQAHvNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
چلسی در یک دیدار تماشایی موفق شد به تاتنهام 10 نفره 2-1 ببازه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102507" target="_blank">📅 15:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102506">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO9vUjGapsWCIWXRupkCvy5Rt35EAvfvxudd6BAZGz60IRsT7vqwTwW8Gpe4pnzlyfjkrcU1flB_wRLH3hpg5axaj0BklTZwj6KzWyQVKFLOkQvfmafGke4oyCe318rgKa3Ji70aM8SYnsRfyEosvJq4pzFipL6GpGB-RAATR74zgbe6W-avZzB7zAemf7wdIgNwmAuPULlNFZ67QEEdyGfT2f5niFd1Z9B6OPJ_GliooaUAYu2532BB7-GsIeH7RqCzMQ0ZvlyXMWJAlqT6Gm8estDgglMpPLcj3Q8V19XD2sbNIlBz5eqbv1eXMoN4GYijzF5NfuC3cLKHm2zevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
تام هالند:
بدترین تصمیم عمرم که خیلی ازش پشیمون هستم اینه که طرفدار تاتنهام شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102506" target="_blank">📅 15:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102504">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1fTku8wXouns6Mo_HDXaJEzmQaxqI_1vWgkHxiITZRzBISgpPmErvuYolpHQlAJCaZvY18XE8btor6ZtH2ZjoB1NQOJAYy01m73cxXnO6qZmiiQGtWQi-CKtByFUKS60mARMXdJVog6Xjh5haUcBa8_oOL2Uu26rklt2AnL3rUYrhTQT1o6OtNHLHZMyyu3ZGvxt1Jj7zM1g1bIzq9rdZfqFEk0XRORq3fqLAvrYqSISJE3fIy-l73rZjUXnhpQQv5_tFU_WBHbwewvwloTsGh2oSYaNlxliFW2G-cCfESsSbUZEfYQP_cZ20918UAPey1VGDv97kzU9QdDPFloag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8hRvbnrxQ6JicqOV-REYPrUXFHeTGCbT6aOGmaFD5abVYlSqRZreCk981cRB6GRBcg3EXrhGgMJzoBhiJAbaU-uIO7sMM-tFQNlVOKM9gDb1u5HZC3sKd3C2IrEwwxK_EWSluI2vf0JytYTJfkh02SQpKelu_mFiXcs8lDg3QQ9EKTsNrVkKlb-uz7Otvu1e18Arj-SEYfzB1c3TulZPtk1XaaB_Ha7qESiipxTnnRx6PeCSX3t0PebIrjIv_yDOzP68IeP_C1vyUvypl9xqaIk9kiq_kSoh7krSHKt5rADd3mBbksFCVYLiW5zpsK5gfMD68Cdbh5P3CAJAC8Wkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
یه پستچی رفته بسته‌ کوکوریارو تحویل بده که کوکوریا نه تنها باهاش عکس گرفته بلکه بدین شکل یه عکس هم با مدال جام جهانی ازش گرفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102504" target="_blank">📅 14:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102502">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rySRZayF4adT-0-oh0JNzBjdI-FfAX0BlTBHthvJp9cQ-gFIqmwEKXX9hgkBKRMmZB4HIPTKGFBx_Li_95ZGmEaFg1u-EfuhpLnjDWq3LubQDz-KSyfKFnwa4Z_EiVs1FhbwT7m9IE6nKit8MkEIwpSM9QYzY5O-s2DJXD-x6vW2yTbfNmd2y5aGQ8JnmiLBO7_hCKZCorkIhXBnHddkhteMmB2lxvg5o0V8MJFE_OripxdOY6eNmAVqPxibxuanS1oTt-taDukTl7LvyQ1lRUdie_Y-EI6R7V12LGLJNtU4RArqb2YUFAlbJI3d2B8Q5_BoPDanFrzdSESHK6ol_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Du80yLNkx_Q7p_wgn-PwHpOhnBWTopFUGhaKxi59HValggMwMhz1eIu5cEcm5Jjr9ziGAjx_hUemx1_mpphuRMxtpbZ02bMdJKaQIcUC7Rr_xnNvDqu43f3UJC7lxfuNzIrBQaN6yaqPTTDW_AJ0rRiNfjvfFFvmaUHstColpHQFz6FXjmK1vAz9_St8DsC7eXEE8nRbtuJGyTU1H7lXXL20z_sruyifNWcQ5rBUH2x6fsPqlihW_dwUWXuKSf9VxTdzrhzuYWRIs_hY2ZYtfOAFfkBC7SzUJahtX0gAOrRsE99og_DuSI46v9f7N-jHBXHU-Vf0I1f_EwSIDnuINA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
نقل و انتقالات بارسا و رئال تا به اینجا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102502" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102501">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5_UNSbE9Qu_pK2H1HNcqfmW2R2dCCRogR-IZFVCOAfymIzGPfs1GPv_HXK1eP7nzMZvtinc82IvbFDKYWAQETBrgu-RYhIqjLirTEpNcC_71Vkb1hA-Ers9yE9BeH9fwZCG2TI8IWLIaYsxT0axQrkUp9BCDfPITOQGIEvn-B65wAA4MOXJhR8DochNeg0AcYZzxcavyAa_FwmrLR1lLeVWXGZ7L7M63zqjQuje5biHYelo_5fR13lg1fiCgFjQcYjgR7yYkZiF7XQtqA1JDRPk3XPZ13ne5UohziO1lG9cUr__qeb7jXn37BpNuyUL_ifgjGmZvxkjGNhZXLqLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
اطرافیان وینی هرگونه توافق بین این بازیکن و آرسنال رو تکذیب کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102501" target="_blank">📅 13:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102500">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sf8w7pDq2_8_iBSSw5wv16uoA9yT5S6kXwFj3SzB9CIKis46zEBUWTe0Rjd2EM2lGWbuNV1RKl50NYMWH11UtJtshaLIZ719Wvtm6Rfi6C_y0Tf0eSu6qntsHQtS-2gpHVTLRFEremGlfyxKKTk7SUaHgNdQSaMH5AtOXR5GurqiezDJPR3RewaCCIZ_5YIxYlZTY4nvs90m_6-UIIRAXHpPeS1VbnhiDk7VzS5gcwFdoV3sRAol70mTciHq9nhsadnENZeFxGptaY6lZW9k8RqxTIP7c874gwhif5ZxbxRgQvahv_d_fq6BT8U0h8-cG08pChTizNuQUzwg7avobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
• کریستیانو رونالدو به یک ویدیوی کوتاه در اینستاگرام که او را به عنوان مشهورترین ورزشکار تاریخ معرفی می‌کند، پاسخ داد:
"خیلی ساده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102500" target="_blank">📅 12:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102499">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=EPU1o5fERphSWmF_tivMYhXKcppVtdQ1eLpFmfdbXJX2wExCLcwnQMchsOy4SvvvTSMwA-780dtZIlYPumG0ns-GlVZaESXYdYaZ5DE0q6YMzUUhNYadKxZwH3cm4u5J5KQ2HiDF450FXU_cpVe_kmBGjZRFSNCef5fc47Z4hTTZyNeU_ASHfsg5TTT2YP7NDjDVdXSzXa7uk0vbX1iMiSUBb2OtWkyCaX2mjDJslw8D8Iiq1mYFo_nLYDTO3kq5g1dmx6uQYOkfL_n2Uu_uFGTbhDrFzqgK1No9p6n6p6Dc9kO-IzcoRgpwBbpy86dEhdhW2OOt75SgMa_F2jpYq4JPRCJo5URfRwdCNT0QisLzn_EVknaQz3gU_uMsOsdtfUPSmn1Ocivzl7NacTSJORdyE3w8gqX-Xb3C5C4o7GO3GAFOEm1R5ATCWF2V6rMsld4MQzamYTGDbqxdvg1n8B47mvB3khayPe4rPRfmY4w7-cZyOpFLoZXwYAZY52_5WSiMc8YCCQWtQ8r9_sTkvIk50AIjngdKLdZv1mQat8rwZ8c9VEqt_uUh5jDK28HBwOxjZr29GTZI-_jhLLt-YCYocHtX7peTYREUJfHDewWhSRLO-A5oXFHv1OyBK7Fv0i17hRi9WPZ4vneJ5zquSX0VfMRDVrfZ24jLT1bW1G0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=EPU1o5fERphSWmF_tivMYhXKcppVtdQ1eLpFmfdbXJX2wExCLcwnQMchsOy4SvvvTSMwA-780dtZIlYPumG0ns-GlVZaESXYdYaZ5DE0q6YMzUUhNYadKxZwH3cm4u5J5KQ2HiDF450FXU_cpVe_kmBGjZRFSNCef5fc47Z4hTTZyNeU_ASHfsg5TTT2YP7NDjDVdXSzXa7uk0vbX1iMiSUBb2OtWkyCaX2mjDJslw8D8Iiq1mYFo_nLYDTO3kq5g1dmx6uQYOkfL_n2Uu_uFGTbhDrFzqgK1No9p6n6p6Dc9kO-IzcoRgpwBbpy86dEhdhW2OOt75SgMa_F2jpYq4JPRCJo5URfRwdCNT0QisLzn_EVknaQz3gU_uMsOsdtfUPSmn1Ocivzl7NacTSJORdyE3w8gqX-Xb3C5C4o7GO3GAFOEm1R5ATCWF2V6rMsld4MQzamYTGDbqxdvg1n8B47mvB3khayPe4rPRfmY4w7-cZyOpFLoZXwYAZY52_5WSiMc8YCCQWtQ8r9_sTkvIk50AIjngdKLdZv1mQat8rwZ8c9VEqt_uUh5jDK28HBwOxjZr29GTZI-_jhLLt-YCYocHtX7peTYREUJfHDewWhSRLO-A5oXFHv1OyBK7Fv0i17hRi9WPZ4vneJ5zquSX0VfMRDVrfZ24jLT1bW1G0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ویدیو جالب و وایرال شده از رقص امین‌حیایی بازیگر محبوب سینمای مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102499" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102498">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=XdwSfD6dNBMR2_OxBaDXyzAcNumdMAIsJPQ6LJmlqzslHWUSt6gK_fPCjZQ-PUNKg2NirMCcjyXvKucbcuXVhvwaNbjNda-uW-lc4o-aD_si8vtO1Ri23ahk8rRzVo5kXXu0OpMfgzNRkIH9LCks4UzhzXDJ2qCUb4hOqRYGEib_m9gfgViDX_t30cDFj1AQzI6I7n9Hv0mX7fkQCLKo3eTkYK2dBt9rrJGrXD5TYyAMD2mIKQOMRbz7K0_rfrGhjdkZUNjd3llAKWvkNC37W7VuP_fhl39Bo9WypeM8fkC0UOfPKusehcL-IGLYqL1hL02GZbSmK8E7Jt5z8kEysRVmFT_E6XL1YZHi3znjOvpAaGqR1qNjOKkjrtmUNIb7InRGmkXWvQVIatwqRE_lH_wEBuTCLGLO8u9TdTBBW49k74PryfJBNeGcOJxmXZhXZkd18lN7DmQaqL6u6pT2R3nZFyfRmUQ_pQZ0e4nZPMLWuh5vruPikwt4ExiLUfotNE85iwDLKUGu_DLExAZHubpFILbK43RSh-9R6GJnEmbKzHJ8rcOM_eZ-RYZbLcnniRJoPqmDuYiCc8Hz6tSzMHo5qMTVXrrUdipa0vI3bas7Dq7HCWZFgUEBp4Z5Jd0Vlbv6WQMmYKFWETMXASPVXt7DLwujtMR2BiPOszW6Jmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=XdwSfD6dNBMR2_OxBaDXyzAcNumdMAIsJPQ6LJmlqzslHWUSt6gK_fPCjZQ-PUNKg2NirMCcjyXvKucbcuXVhvwaNbjNda-uW-lc4o-aD_si8vtO1Ri23ahk8rRzVo5kXXu0OpMfgzNRkIH9LCks4UzhzXDJ2qCUb4hOqRYGEib_m9gfgViDX_t30cDFj1AQzI6I7n9Hv0mX7fkQCLKo3eTkYK2dBt9rrJGrXD5TYyAMD2mIKQOMRbz7K0_rfrGhjdkZUNjd3llAKWvkNC37W7VuP_fhl39Bo9WypeM8fkC0UOfPKusehcL-IGLYqL1hL02GZbSmK8E7Jt5z8kEysRVmFT_E6XL1YZHi3znjOvpAaGqR1qNjOKkjrtmUNIb7InRGmkXWvQVIatwqRE_lH_wEBuTCLGLO8u9TdTBBW49k74PryfJBNeGcOJxmXZhXZkd18lN7DmQaqL6u6pT2R3nZFyfRmUQ_pQZ0e4nZPMLWuh5vruPikwt4ExiLUfotNE85iwDLKUGu_DLExAZHubpFILbK43RSh-9R6GJnEmbKzHJ8rcOM_eZ-RYZbLcnniRJoPqmDuYiCc8Hz6tSzMHo5qMTVXrrUdipa0vI3bas7Dq7HCWZFgUEBp4Z5Jd0Vlbv6WQMmYKFWETMXASPVXt7DLwujtMR2BiPOszW6Jmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پنج گل برتر فصل‌گذشته لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102498" target="_blank">📅 11:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102497">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwRvnMfsoc2UOnS7sJYlnX2akiSBMBc0dyqn0aG4vBr4tAfdpH5zs_nYESkqgn23gWdC9cqQrA3q76StUgtE7RU-kdrEYzIP7ebH-UyKCnae8IYOrxnU9oZyb-UglwpFLq7KcuccWIn4PpVBQgc1Y4Za-X4L6s47B0xN84AWaqzCyJDTtsPrmWheJ09Mcxuc9fMh31KqKfayqpPWcvvK9rQZRHMJzjZW74zO8YW7U6ewewxNtx4UqYrUj5NU5GJOVRRoxRYHFR4GqLgidM7lJyiggDTsvTSIDgnMsfvnkyuNZx_2g-oGcPIm4kp1Tj9vzF7ONQTPm0C4wFGjcYjvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
اینفانتینو با انتشار بیانیه‌ای اعلام کرد که طرح فروش بخشی از سود جام جهانی به شرکت‌های سرمایه‌گذاری خصوصی، به طور کامل لغو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102497" target="_blank">📅 11:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102496">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e324940235.mp4?token=Bl5voWHdlRCMsZ-ZFpE1PTscJ5x4F9yWPvOCfx1on-oS829a8DktxJlcrOpFwlhvNrstCmVqipJ1HUlxMG35vrI0ulaIl00_GF1kS2lTlLuyF6AVyB-0o1J5rW-V-12L0-GwM-jUecW49JbAIwQVWOYrg9NdzraEtbue6c8C_ptAn5l0KOl3X4gNitRYw5DiVaJrWvIZCgdCH7AhqELVSSXsyLzPl9YpfvCU6XE3Nh1obV8NVd7fWu7s7xUAR5zDwXbAr-K-Naedt_-y3irYBeGRTNWMzRjJ2csrQ5nSFGOcjNb5WELPXNrkPuwWaAi33dy2gyNh9mu0P3JLyw39nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e324940235.mp4?token=Bl5voWHdlRCMsZ-ZFpE1PTscJ5x4F9yWPvOCfx1on-oS829a8DktxJlcrOpFwlhvNrstCmVqipJ1HUlxMG35vrI0ulaIl00_GF1kS2lTlLuyF6AVyB-0o1J5rW-V-12L0-GwM-jUecW49JbAIwQVWOYrg9NdzraEtbue6c8C_ptAn5l0KOl3X4gNitRYw5DiVaJrWvIZCgdCH7AhqELVSSXsyLzPl9YpfvCU6XE3Nh1obV8NVd7fWu7s7xUAR5zDwXbAr-K-Naedt_-y3irYBeGRTNWMzRjJ2csrQ5nSFGOcjNb5WELPXNrkPuwWaAi33dy2gyNh9mu0P3JLyw39nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
و بالاخره تحقق رویای دوران فوتبالی کاسمیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102496" target="_blank">📅 11:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102495">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👀
🔥
هشت سوپرپاس‌گل ثبت‌شده فصول اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102495" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102494">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuDUKzJs5mE5KePnwIeMi_1iQ9AbhKM0KCULlVIXto517-6VTVbIIQ7QUsAJe9EMj5aQXrvlYEePC0PCAU1_GhBElQfz9LrfibsU1vw6y8s19JnUW_5BjUJg2Fy366aKzrkTfVRJ5Fn5rW0RkBpLt8IKGJRurQEF_bhjpxmHbxksR23HjTxhQvb9lQ6o9PBYyuPc2lWnbmbhHONDBxCAl6C3bCwHHAxtNTmPr3aSLQG1GstnubTJwqVy-FloBtnD5En1_N59tbJwAiU-hPBubG5H5cW0rL2kT56CKIB6BxF0Ss-p19ygQSPCyUm8HH98GIYLZRlPxdqf5Jg_KzsQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار مسی و هالند زیر نظر پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102494" target="_blank">📅 10:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102493">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvfujV1Z40npbDQYKOnmQyKyWhpoGRO_5YZ6ts1LZuQCHpVjwCfDi2YFbhq-HSrVhFhiet9LKjwQo6Qijo19cCBF42ohyO-IRJ54e1qbSeoWyfQf_EKTHU7Logz87Nx7HaM1KA9_s6GWfpmvzYHy_Ga4IsYa1aCY5KoSSjciSvpHLaDnO_s2eUK7KBd_bkc0PwQDSn6r7LieHLPO7zmqs5La6bXPpah40y0-8_yXAkpbwWoOhKKLECW8IXxpBtoyRn4eXtyybgAEpqK_xvzmbdwaaHGb6CGAvbCmFu98pWeaipP1De8y2c1Dk74d_mBR4kv1PJKf38pcfIO0S6tAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان ادوار مختلف پریمیرلیگ ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102493" target="_blank">📅 10:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102492">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBunBdXNXRojB0gaIfOTwYOI3alXNeX7sh3dnTrF0jZ4cEvPpubAyAS7tDj0D2OaxOfgZC-Um99Ql09OVG9Np3qG0YSlazTTcCwK3RCKR8NS5g9_qurQjkdBRVcxhwL_Hohp8fyyDWt-rp1UJ3VpZ1qPJM4fxV57JCzXlvWl2IwutaJ21SwX67242sz7kfAvDKhtjvmgazeAdmrnYwQ8ZYOLYTQh_azq4kkNqG21P-K8R0DTWm3BSbNDY3UXOsG84DogSxrTdcN4jtErrQa6Q6h_ifE_pDNPsiB7C9z3W43Z_EShS4RyPOyKrb5sEO0km0Nudro0NGnCevKAqzLgwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
باورنکردنی است که برخی از زنان چه توانایی‌هایی دارند!
💪
ژوستین وانهائورمات، هافبک بلژیکی تیم زنان کریستال پالاس، در سه‌ماهه سوم بارداری خود همچنان در حال تمرین کردن است
❤️
او ۷ ماهه باردار است و همچنان با تمام توان به تلاش و فعالیت ادامه می‌دهد
👏
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102492" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102491">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5RQ4eI3U8Fm-COxxW8lK1aodHNFLoJsLSt-zgbKJ9NA5SVkfnQJKSv0MthjWxovUGeEbjZZqEULNyV6719LQzuVPli2ZhCXyJzChLHuUVeSjhKF0jnippBB0D48ALHSyhJ8QbTl2CiGIHRK5Nib5vG7ZRRQkzKQHyQW96CtHBlBeNZMCcyIk0q_n3pXEbCxBH7r74iZo9b92z0RT_0eDMyTn5zSEw_KCRr9VcC22t2uTNbMC2eKfLMgHKszWErD9xKlKzti6_MF9ZxpL6sUcX_ObiFtI5-5ic-ijmtKfmQdYqXb1kHYOXcpoG0IfadL2vmVbd4KjeYskQUgdbnOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇫🇷
فوریییییی از فابریزیو رومانو: پاریس بازم وینگر خرید! مگنس آکلیوش، وینگر راست ۲۴ ساله موناکو به پاریسن ژرمن پیوست. مبلغ انتقال ۵۰ میلیون‌یورو و تا سال ۲۰۳۱؛
هیر وی گو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102491" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102490">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=bzBR6DKt9lRKeumx9HAdkUIxhjQg70eXGvLLwmJU6X-5JFMCTlECl9-c1TWTJYbjV5c1GQHOz0D2oD-1l0VTbHsWrKAqt1WqtoIX2kR62kcxFWp1x1S316KOY3Do-DpRBTOzqwIoCrzZ1sD9L3mgww5V4w9h-PtTL3uHDyFeccWSvOl9cy8nC5mepI2XgvDiK8hD2qmO3J8GAd7EGxMVT8j908AGnS0KyV0Mi5pdgBbR8Yo1J_7g4juMjlJqQPB7rv7IOM-SLGPzyLzIAj-rfwiLbWRdsFNKSJSQJs08__VPwTBBngwlbaS1fhx2byuIhYO1uXELzZtFZA63iSJnXpssTbXQOMTAcpziOsyDRr3kNIITDfoRXgLLMob9wK8ZE5fEUHS7M6zAzYTWoR4_0Eot5f37jGyj_rFElGcI4DmdN1Xfae__KFC1Jcwhbm8QOg0yMp7iUkWPpgvXVoaxxCcW2CCQ9y93ZGWBM8vForzuMb-YX1IJ5iKgL_B75mJi6e-frpvoUs614nlZ36DSOowM7zXmueHCvpKnbE4zvKCELYFgoXyLYwmFib-Th-FPR8RR1SfELHgsIl7axPSysI89HJ5YVHL8B_CVrIMQ-Foq25Ejn0Tagu-_VR470Nnn2ehMs5rJk-8VdQiQNAym1E8wvufJok9-vbDkj_50WVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=bzBR6DKt9lRKeumx9HAdkUIxhjQg70eXGvLLwmJU6X-5JFMCTlECl9-c1TWTJYbjV5c1GQHOz0D2oD-1l0VTbHsWrKAqt1WqtoIX2kR62kcxFWp1x1S316KOY3Do-DpRBTOzqwIoCrzZ1sD9L3mgww5V4w9h-PtTL3uHDyFeccWSvOl9cy8nC5mepI2XgvDiK8hD2qmO3J8GAd7EGxMVT8j908AGnS0KyV0Mi5pdgBbR8Yo1J_7g4juMjlJqQPB7rv7IOM-SLGPzyLzIAj-rfwiLbWRdsFNKSJSQJs08__VPwTBBngwlbaS1fhx2byuIhYO1uXELzZtFZA63iSJnXpssTbXQOMTAcpziOsyDRr3kNIITDfoRXgLLMob9wK8ZE5fEUHS7M6zAzYTWoR4_0Eot5f37jGyj_rFElGcI4DmdN1Xfae__KFC1Jcwhbm8QOg0yMp7iUkWPpgvXVoaxxCcW2CCQ9y93ZGWBM8vForzuMb-YX1IJ5iKgL_B75mJi6e-frpvoUs614nlZ36DSOowM7zXmueHCvpKnbE4zvKCELYFgoXyLYwmFib-Th-FPR8RR1SfELHgsIl7axPSysI89HJ5YVHL8B_CVrIMQ-Foq25Ejn0Tagu-_VR470Nnn2ehMs5rJk-8VdQiQNAym1E8wvufJok9-vbDkj_50WVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بازی‌خاطره‌انگیزمیلان و یونایتد در UCL 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102490" target="_blank">📅 09:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102489">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هایلایتی‌از بازی‌جذاب الکلاسیکو در فصل ۲۰۱۲/۱۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102489" target="_blank">📅 09:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102488">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7q3yDIgOI6aD9ghFxhJoTVh4n0mdf0EeF7cgAIfUN5UaLBoPodJQ7fABvyAn0A2_IgWzidZd3yq5DiHSmahw9bcm1nB38TQqsMUkKNQNcA_0MuuDDfNha7Knt32VAYGrrEZvbmKYsxg6MYEwnMuARJij9-XoaotDAR0ExOgGsUY5Rm6vwpUbbpXfu8NP-tLVuY5MYgB8Ihzi5rs2f4-K4q-49zAwKwT8Bt4a8htqvVmlWMMK2OvNvvPZt6ZuNJsZwb5iMZDPRK7Q1JLYmS4wbrzCgG-d21RNsksDExh0clfkcjk5TlfLY4LJWfazfydvawqu-mfCFJNPie0lGxpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای اون ترکیب لجندری بارسا چی میخوردن؟
مسی عالیه :)))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102488" target="_blank">📅 05:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102486">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVTBcPfyetQUBD6bmidKfiIGhua_y-HyODdsogg8bwbag2vRIeeZJRuQzkrgyGEfkAQpFgk1bSOmqnQjgfH4z9b_I_9zeth6ozBsJbs9QkOZd74oB00iiQ5NzqBhgQSx2op4YXyRb_mCrAe-OU_L_hVchom41b9RRb-jjRBocZUgD5fBB_8tlATHvT-V_pw1uxRBRTtQz48e7YezwnUyxuSHZyu7x7nmR6n56SNv4kSSYoy6s5y1fFIJPAG7QSs8tXo_c7wIQ62RPdGA0u--d4rCXyQu1W_taEFAgySqY1cKmJr7rHgaixHu0fssGM_tCTyQuYU1jWx976Ek61tFpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گوئدس ستاره باشگاه آژاکس با رقم ۵۰ میلیون یورو بزودی به psg ملحق خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102486" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102485">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇱
کانال ۱۲ اسرائیل: نتانیاهو در دیدار اخیر با ترامپ موفق به راضی کردن رئیس جمهور آمریکا برای بمباران زیرساخت‌های انرژی ایران کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102485" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102484">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlwPvRK2Gkq24qHVXG6APOnqdv3I48iN1_ZBjwmjDGn8GpnI0qPMoz-m6S-bonv8YmmeR8klzwXJd5VQMFfFE7dyPUmx0zQNUv0Sv4YnKiFpQhB93vP4gXQr1OHHED44xIR8pzH-t-82foFBz6Andp7hXFG5BgigQnUR3LbgRtL2ScepAgAtftJSN4WAZHBagLiEkWkV4v4UghQ-kEZAb5I7xRPYjhTrHYP3feuE2s630JpBlNMjuP51rngPGctvIHx5ZOsTCl800cDd1bgH55XHg7D7axXDOniuMmYkTlBmqf6bd1ShnBLpibHWCIL0akU2PqjHSt1aMt56YEx0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بروبچ محله تامی شلبی حسابی واسه جود سنگ تموم گذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/102484" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102483">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/102483" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5nRoXVTIN6bR-qMindDYUw6hRfR5LTBOApMWNdvTkKsEdI7BWEFh9cyVF8O9z8K3feCTrjHhiL76xspoAnygaUQBvFJ3tBDh5B3aj3y67kaFYdFDOcQ1Qq6yUrwnBgEQCOf90fdy0HxB5uKK-znYAVkzLnHORB0mqr9I3uVW4yT96YSGMI6ymapJ70DR81j55Zdm8jndEcnb3RvIeYrgQpfCncnjR8fJ-rm6AKzfXthTJsWOrDzT_CJa6K9XdbP9pXXoUxk3KMlMzaadWwtmxRXSJzxux27XGKbYgH-usXzfZgblSc-_96AIjuKtBSJOyVAXMs-qI0zH0i4rdbctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102479">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6gBtpb7gGo9WvsLz8gTGyaRJXgIBbL4oSb05m8FoIVnL0NhKulZ89nMn_LzYHKy9BK7nt4_iJg4FLTWG_qoUZadJgievVnkzRHxVTZD7uCAnizR8JDvTogavN-DN2eahq1c_uvNza_sPmAjb5nVxGXeo4cmXXs4QywwfWlbxJYOU-FGFqJqzqcoKIcNCJQbB8IRF_5bAlFtAlALCsqWGqgB9TxtN00GVPTYYuePq3wUamCxpJBJsR3biWrnrHz-IWr67kahrOrBcrklz9amsSPUi1R0lrCPG0UR133-J0IwOFabTYZhLno3pnfaXP2JVLSPeyhX5tMRzeCMx4nv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iim-C1yAFr6WptGSNUeEHDpMVnWjUe6A2XkpuaCVcsHBghnaoRT75hraA6xfJFJC0WguiuboBvmJafGwUE1GSKWsWMupVtj0k_QdEsBlgeRs_hW5uEfpBP_fFo5eFUlvqVN4OyYZN5iquAs-M1my36BYPES06dXTavWyTcwH-QY2WQXeF93covsRROnyAdJmRc7NJtqQCbmKAym2JEcQScUKxiONui8VKARdF5En7b-AYtAU4V06l801c5gWpZWWuwTDsgxILc0Ax3ZgjYr9KcW3G13L6ZfeblyDUUjA2tC7XeHN-iYQ23AdDcnvLvRtmIaeJEUk55iNVRrs5tdxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icwhTKRpwY1OKQQHJT-Falia1idhKbSZUGdj2MDh3SoWymVNZjO7FYpirIsXNxrs_OWEED13LYyJFp4axkv3vZs5XkHv_hLrOFFItiDxjS60rUXmgEQdQT1-8LHQR-wlhTISkmPEqZuy5LL6gbE_q9fyxHhGN6k4pEQ393pBf1uS6rt0H8zF258m2d4Y0YNDxgTZWwrcZ3zs7VDihMnMWcGM--9Krf6LH7i_8aecnrO9Pv9CqrVBZE2S-nKPUGouHz9cVpaKZtkTUnNjrqcUe66TVBP_JjzBRlVxAWVjovCwsk8hcPSMF5OUxS12DNG7foV5I6zByhmNNIwjubTzrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
باشگاه فوق العاده محبوب آگزبورگ از کیت خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102479" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102478">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORxG4ePnC2f14ycSlisvMjtjeO0mL2rDq4GadFcJ3G3c6SZnbFsHruA1zcE5hBLkNJMmh5s_ov1GhW3cFoGs0dgco-prQKZR9Dy7Xr52IKxdM7ZQjPIfFMobSdAJORxjppRanAHSF5TNPc3dbw7wpCPtsXxSXgU3N4egUrCCILZCLURtCK5wyMuug1eQK-MS5kqqoPpLq2WncjJc90z094PDHsOy4hLHTdUBvXOW8VDdHsNqS7JIMuz_JhSwv2eJd8UJW8B6w2kOEpYZ6rruTjXAaF1kqIwRYfakUhzMfqPn4eFtOXSsyVlL7z4hQY6yX4QfnUZ-zT9EPfqaSjdUew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هندآف آرسنال رسانه نزدیک به آرسنال:
وینیسیوس شخصا با آرسنال به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102478" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102477">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102477" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102476">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Nw8BYplLo8vMnxdF7dL47NJGD2m6hzoEiySd5Ny6ZIaWPaPJo_LvwFLVUCRH4jaoZsJGzAqj2ekPHy22ezzCnKy8G8LzyXsegWeoqgn2_VdAnB-f3MQEBVEPbBl8hvvY_GIunabrEdQVoYowsxYeBgUzDUWseSzjDXQKbNWqNM0fpeyFMGVerPKqFIg-kGHxWv-mJuieLxn6awRENxB7io0nT5K1bhgJ-jiaRIVd7H3cPe-NtRZAEZhIpkSpzidXHNJfFQA6wPJTHA821UzfCJlZrObm5qVP8tpiCpoGcBGpcL4Jkhy98S-8ygbPkmj2Dy7BDAXq3rJ3aadGkm8R5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Nw8BYplLo8vMnxdF7dL47NJGD2m6hzoEiySd5Ny6ZIaWPaPJo_LvwFLVUCRH4jaoZsJGzAqj2ekPHy22ezzCnKy8G8LzyXsegWeoqgn2_VdAnB-f3MQEBVEPbBl8hvvY_GIunabrEdQVoYowsxYeBgUzDUWseSzjDXQKbNWqNM0fpeyFMGVerPKqFIg-kGHxWv-mJuieLxn6awRENxB7io0nT5K1bhgJ-jiaRIVd7H3cPe-NtRZAEZhIpkSpzidXHNJfFQA6wPJTHA821UzfCJlZrObm5qVP8tpiCpoGcBGpcL4Jkhy98S-8ygbPkmj2Dy7BDAXq3rJ3aadGkm8R5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102476" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102475">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC599jkIGJX1-QzQ0iP293sqGM9ZPI2S3b799DCbIlm7Foj-P0d_uB5GzO8nfKE_hYut2-k0mwT38Mo7z7BKwn07afE02Y6bLz6GdiVozzTnwb5NubcY_d82yBlhNk3fN8aAdNrfYNRcH60gIYyJbaR-FaJ1EVlwErLiyturZpYQG_4R-3wxt0V6sV-Rz-6HEo8lqKFGaf3h-CePim62NBQqfalxpLGXVt7UaxiLIx-tOWmCxpJgnlPJIVXv1VZyLQTB1_rZRIWxPg5Y-3oNBrTCW3MGDDNOBIr5MUSrcGfGzdolQ7P4W6mKQ9ReGfYSuDPNM7DtntLyVNeUrI5n9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بارسلونا در یک بازی دوستانه مقابل بیرمینگام شکست خورد. بیرمینگام با نتیجه 3 بر 2 در ضربات پنالتی به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102475" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102474">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGSB6jsgZbxmLoo2jVazduTqwC2YXfd7HiXiaz7APBqTgq4LoPrpUCJfh45MW2XBVA_Q7SK6qc-xpd-qll1FrSOQjNe_Y8AnKZ4-jzDiJvK2AalUsWtNAjn9N1EMVq7Kf92N2P02HHaNdU9Kh_axZz02JdrvfjMZbdShbciRDq6cTygMN-0hyUdQkhJlTMY4ODsKCx1M9q025cGUT-jvAwSBdla1eRR6GwnHrYDEo0_OfGyVTfrr6sxP6vy01fjGoydjYmOmG6HEoLww1B-vxagAUNvOhENUV9nyPjlwj5YZxP0btavephIrElbBKt0tyZ0YS0GWWz1Z5ijq4rYCQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دوست دختر یامال
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102474" target="_blank">📅 00:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102473">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDvcY2P7FCfLBUWcV9DpYOe8qcelfJ77TP1pRx1Jk-1D30ded8zcZHZm1-TdcXzXeERfDaDT_KKfAkjJXA5LIgSkkvNC6IcPZM_GD0tybTuuOhzHYjW3NULOITG-TjNeEG3qo8N0a2J1B_wW9mY39LB01zXimnnNDK2OpggJBQeakYcQ4zxNnWAgAAFaDACPyZythGgQBl9hn9wiP1T3w0A2NYpvcSqR2KOzqdS13-RGxGKqZHp_iIiwHaz1LAp5HVBt1mPuaeSbsQF6_j4J37B4M_TJyTeK5zCTwTe_f6YUbcWTB8x6w65h7yRpdvo5w84bJpBxP-FJUw5rkeACaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤩
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102473" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102472">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTSOSo9Osw1s6cCDFdHqcskSv01i4uW5X1G1n5TNf4KdZTKaY84_DJGyTSX6_6j_1l0Wr-GPL1bKrelnS2sjnmLniz-27ohuxawV4w6Y57PRvi8TLaZCN6t1xy66Sfy6vv0fabSavQl2bgydet7rqj7nBDNm_D-IH16gpM9ob6oz_ssu7Mwx5iteVJoe7A_1C-4disKC3xHvsUCMVixfxXyIROhHSCczwwrR2AnlMavxoxrnBXooPIo8VtrpIdalPPwUL587u0J7IR1tRPlUBVg5Uq8M2iEi6xl5_waZ0w7DdbAWwxYqd6_ZSkCmRrwo2ysjT5DCRlNYCnVf7LMB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
مسی و کاسمیرو تو تمرینات اینترمیامی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102472" target="_blank">📅 23:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102471">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c665525c.mp4?token=emlA_8UBQn-dioXa2gCueytfFpv0o0ltK5s9mf56Yx1JxuAM2ZbsISaZqjjvRaq-ToYUWW4dZ29CNVC417EYEzQPYyWHqaTduXYgZyhDeETuGs0MTYkz7cWYuK4249QS2TV747417CNMajpcVQB6B4Pwf4tyUVMSqqMLrrzApnoHO3T_1P6tjeCUmOAigIAv8seury_Xm9izM3MKhRmhT1om_DCICiRqYdue7ZoBUp3CnzPfuEMunL9FchOPkI_YfUP7uF3rUhF35tE99EPSCIFFM5NVFvQAUptijQEFk9SOAhgUGNjOJ4vrPqnAsoIssHn7YEGDnLt6x2CP48nziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c665525c.mp4?token=emlA_8UBQn-dioXa2gCueytfFpv0o0ltK5s9mf56Yx1JxuAM2ZbsISaZqjjvRaq-ToYUWW4dZ29CNVC417EYEzQPYyWHqaTduXYgZyhDeETuGs0MTYkz7cWYuK4249QS2TV747417CNMajpcVQB6B4Pwf4tyUVMSqqMLrrzApnoHO3T_1P6tjeCUmOAigIAv8seury_Xm9izM3MKhRmhT1om_DCICiRqYdue7ZoBUp3CnzPfuEMunL9FchOPkI_YfUP7uF3rUhF35tE99EPSCIFFM5NVFvQAUptijQEFk9SOAhgUGNjOJ4vrPqnAsoIssHn7YEGDnLt6x2CP48nziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین ووزینیا که تو جام‌جهانی تک تک تیما رو سرویس کرده بود، جلوی علی علیپور اینجوری فحش خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102471" target="_blank">📅 22:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102470">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpeGs3nx96bvmOx8f9GFjcFC8y1JtVXkjfRmXIvWA56bPTPjYTJRBOslQf-VdoBrlY2WseCUIVNPh7Ius80WwyWihwimB2izgJX9K0hjw_jROPrrcaDinLMRFU5zIRnCNpUaoobyvOSP93OHEBn9FpHLwj35NjKqud2s14RWqgjqVGokH4pDSP0nN6jdsOzkWxRSqPubqGa8x6q6c9vce716axmT-UJ-MZp0cuUy0u6Wfx1ueX1qtu52FDiHDtBW-9xjMoteUt6LWs5RDwig_ysxxBphjYZJWI-2x9XurK4dZQ01Qj3ZZY8iIzkZoaInVmdBXSrxc8HBE3FYJEP_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ار‌ام‌سی:
مندی تو وضعیت مالی بدی قرار گرفته در حدی‌ که مدال و کاپ جام جهانی خودشو 54 هزار یورو فروخته.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102470" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=DfqT5Ly_XxlFiNqpWGz83y3QHwaG1U1XlA-X3MwzJsTSP8N5TtYLsw2I5vhAFDscEVFCtQeFbK69RPh85c9Bp9ttif6Vq1zip3OnjDO0zFtpxzwB6PIGXjuxFNh-MgSLSQCt5J539PwIfaZ9_B3xgX8ce9zunzYKx7OnNKTi24fRf6qE3t2TnTuGnf2Hvcka_NBnKqxsHCQWYSkD2j7Hdb3hEwOtILyWnDUGXeUoGpnQQE1XV4gsc-VkpVLrp1DAfIcMHiyRn1uU7L6KEf2QsI5yNibHcnBGwJTo7rMGdZsqxAUEwZPb3S6UNwY3kEnmbzn1ownJIgwjiK7pLCVbXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=DfqT5Ly_XxlFiNqpWGz83y3QHwaG1U1XlA-X3MwzJsTSP8N5TtYLsw2I5vhAFDscEVFCtQeFbK69RPh85c9Bp9ttif6Vq1zip3OnjDO0zFtpxzwB6PIGXjuxFNh-MgSLSQCt5J539PwIfaZ9_B3xgX8ce9zunzYKx7OnNKTi24fRf6qE3t2TnTuGnf2Hvcka_NBnKqxsHCQWYSkD2j7Hdb3hEwOtILyWnDUGXeUoGpnQQE1XV4gsc-VkpVLrp1DAfIcMHiyRn1uU7L6KEf2QsI5yNibHcnBGwJTo7rMGdZsqxAUEwZPb3S6UNwY3kEnmbzn1ownJIgwjiK7pLCVbXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
تام هالند یک‌بار به ارلینگ هالند دایرکت داد و از او خواست به تاتنهام بیاید، اما ارلینگ اصلاً متوجه نشد فرستنده، بازیگر اسپایدرمن است. بعد از اینکه ماجرا جنجالی شد، هالند برای تام پیام فرستاد و توضیح داد هیچ قصدی برای بی‌احترامی نداشته و فقط او را نشناخته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102468">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssdmCRwsum6A7FZnIY22vXn4A_v884UA25b5PrzfyBs6x-XRtbnPrnBjYBbRyqYREXZ9LGKUFRIrnfHkv3ydJy7jKgfODZKLErW5gB6bDWUWyzuuDhHLBjUv_uczo6P2qOB-BcZ5M1A9nXQDAhrCuV8a8rLmMXPHGT7HxltUXT6BtmPHEV_nTeRVvQ-ahmTMwTQ5S5Q-eljxOxsmgtE_8pRq9pGPhVKN9xkwlqU7eBcPNWbyzyL2XFlioA2TXIk00JhHumcRGnd8SD9YB2CK3tmwk5Z04_HCwm7Y-1Aji-3oniaA_NUU0iOggalDhClqQf_v0DajphRFURlS4NNHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
بمب لاپورتا ترکید:
جسی بیسیوو، وینگر بلژیکی کلوب بروژ،
به بارسلونا پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102468" target="_blank">📅 21:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102467">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7w-DtUtItDpibEFSrHQZxM9UgB9Pq3Iyq0YnzdqyAlu9tOiMQhN2_ZTlJUNI8P3YVK2xk8wNX7nvCHofeRamX2EwlJnh3wDLpwhzJF8Nr1yTE5PRt11b0dWh5GYvvvoUsFSNl6230ttyy0bMaMLUqRPo3W40hcJjS-w6g7D9CilaJbBLVX4lfZKOIIrKmJ48nKhs9OSH_tC_1p9uVA5-LZTJxnbpZMEajf0ar4hyC3dngAzHEtwEdVVgkDJju7lEJteCup4z9fh6rHdl2Z1YY7_64bltJzgBDHGlHIxIYlP7l6IauGhqsja1YtVlHucGAix16YuquJee7kOzwyrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه مقابل بیرمنگام‌سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102467" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102466">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=vYN0ocTrGwCltJdOyJKSb5CTJ6uKXJrbaGBTpcJ8WzNKVX5qDtEvtXQk0lJTPnZ2ZY-SyJEHaK7GDgZsKAFzFlhEPJB43ipCMzmCkB8yvL0mqi3rgCOkj4zWkwf34hfQHpRuTlKmk9fXVGbzm_NOGIZf2kyg0tL3lXMB4OUc3nNXFR9q1_oyEVUGvjcScHK4iN4Def__gE0fE_VfMncQPKzxorDWHMGLEDMssZmyp2WrTuMjYuB7Kt1Z4IKjxDlk23RMYPrGR60NY9wtlmlrKgzBzTjQAiqajynNjCGYFQQcffEK4tIlVv6uCyHctMilE8boG2t5G88WDaXw_aMkgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=vYN0ocTrGwCltJdOyJKSb5CTJ6uKXJrbaGBTpcJ8WzNKVX5qDtEvtXQk0lJTPnZ2ZY-SyJEHaK7GDgZsKAFzFlhEPJB43ipCMzmCkB8yvL0mqi3rgCOkj4zWkwf34hfQHpRuTlKmk9fXVGbzm_NOGIZf2kyg0tL3lXMB4OUc3nNXFR9q1_oyEVUGvjcScHK4iN4Def__gE0fE_VfMncQPKzxorDWHMGLEDMssZmyp2WrTuMjYuB7Kt1Z4IKjxDlk23RMYPrGR60NY9wtlmlrKgzBzTjQAiqajynNjCGYFQQcffEK4tIlVv6uCyHctMilE8boG2t5G88WDaXw_aMkgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔹
وقتی منچسترسیتی حریف پیکان نشد! سال ۲۰۰۲ پیکان با سرمربی‌گری ذوالفقارنسب برای آمادگی در رقابت‌های لیگ برتر، یک اردو در انگلیس برگزار کرد که در بازی دوستانه مقابل منچسترسیتی موفق به توقف این تیم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102466" target="_blank">📅 21:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102465">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=t5114GCUElnN_aOpr3LU_sPIrwzhz1Wn3po6B-OH83C4ZDGkHi-qQyK6MPFMu1Qd7Hqgg6MfCXVGCwJuVK2wFBq9QO50YrdaC8dxSi1Xbt9xpZsWQdbSJuYOVprn5bWlts6avC4JPGhw2eYd-3LCZXM0ZnTwTiryjSodn46JMvPpB3mtXY6kCIKcsiMi54rXL6NO6QkoLmkyGqULO2_b1PMQiukHtXKLcxFlJhD8UkJwxKMqkhkQdGYi3026yfG6U_ezTRY-coQeuuT9E9TUA7cvW5krz2bnllHd5Vrpe9k6_fHjXtbRuS3-PRFvQZbZYuIEv3rs74eE7kp_LA3UBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=t5114GCUElnN_aOpr3LU_sPIrwzhz1Wn3po6B-OH83C4ZDGkHi-qQyK6MPFMu1Qd7Hqgg6MfCXVGCwJuVK2wFBq9QO50YrdaC8dxSi1Xbt9xpZsWQdbSJuYOVprn5bWlts6avC4JPGhw2eYd-3LCZXM0ZnTwTiryjSodn46JMvPpB3mtXY6kCIKcsiMi54rXL6NO6QkoLmkyGqULO2_b1PMQiukHtXKLcxFlJhD8UkJwxKMqkhkQdGYi3026yfG6U_ezTRY-coQeuuT9E9TUA7cvW5krz2bnllHd5Vrpe9k6_fHjXtbRuS3-PRFvQZbZYuIEv3rs74eE7kp_LA3UBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚪️
رونالدو چرا رئال رو ترک کرد؟ شرح ماجرای جدایی اسطوره فوتبال از زبان خودش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102465" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102464">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=KsfFxyXmiKqrdaXMfWCssGBhfVMXXzTAIkVkvvkc66uJcwGXD9Y_u3TpSKkYo4G3ifrnj8Go89NNcBymecvRTchbBL6521IIV1hZosekHeNe5Mox0ovjowChaPC3sgvi9rnanUSuiR0WchhA5so_wZKfCYEjpWAcJH4VAIs0MmrtVDilEYR4zysrqLW-UqdzQOd9x_YntSbi_IGBgvXi-wbQ1Ue02Ptvt135ovRJ7aHn690yMBj5uRSjI5ZXBGoLiJ_GrgY77O7InBNqN6AEObQY_t61MoCUrqI8c-CC34nPJm_95aHgjGz6JWlA1gZNoRI_gyTZXJVfTEA7f_CN9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=KsfFxyXmiKqrdaXMfWCssGBhfVMXXzTAIkVkvvkc66uJcwGXD9Y_u3TpSKkYo4G3ifrnj8Go89NNcBymecvRTchbBL6521IIV1hZosekHeNe5Mox0ovjowChaPC3sgvi9rnanUSuiR0WchhA5so_wZKfCYEjpWAcJH4VAIs0MmrtVDilEYR4zysrqLW-UqdzQOd9x_YntSbi_IGBgvXi-wbQ1Ue02Ptvt135ovRJ7aHn690yMBj5uRSjI5ZXBGoLiJ_GrgY77O7InBNqN6AEObQY_t61MoCUrqI8c-CC34nPJm_95aHgjGz6JWlA1gZNoRI_gyTZXJVfTEA7f_CN9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک تازه داماد پرسپولیس را حذف کرد!
از ماه عسل برگشته بود و چهار ماه حتی توپ به پاهاش نخورده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102464" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102462">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102462" target="_blank">📅 20:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=WoSzwj54o4GAK6WP9JlbYd1W1jsH4WoRWbuSJ5PXJJMXPz-5e-YAcDDCCcgF2z3dL3LDcIQoBQNzoMPG9jnWcjhjZdIRDqZPG3tjQOLza8of7J0fICAUDv_5fxnJNqMO_7_Dlma8UD7i52JE-rx-oz_aHhRPw_RFvyNCVFZrcZWPHKZlyOFhWOC022qE2k1EKeDIovSC6sYeP0yomdhgbYFb34xXysArpY3G39BGnZ9uxH4j-7gIvwV-sdsU-Xk6WaADmzGQY4ouQlyQeYI-t33AcuqgvD-CqDWyrM7Br2BD3JkVBCEiWqY1IBg-fdvIHi6GKQcg6CwA2vj6Ldgz4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=WoSzwj54o4GAK6WP9JlbYd1W1jsH4WoRWbuSJ5PXJJMXPz-5e-YAcDDCCcgF2z3dL3LDcIQoBQNzoMPG9jnWcjhjZdIRDqZPG3tjQOLza8of7J0fICAUDv_5fxnJNqMO_7_Dlma8UD7i52JE-rx-oz_aHhRPw_RFvyNCVFZrcZWPHKZlyOFhWOC022qE2k1EKeDIovSC6sYeP0yomdhgbYFb34xXysArpY3G39BGnZ9uxH4j-7gIvwV-sdsU-Xk6WaADmzGQY4ouQlyQeYI-t33AcuqgvD-CqDWyrM7Br2BD3JkVBCEiWqY1IBg-fdvIHi6GKQcg6CwA2vj6Ldgz4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شزنی جنس رسیده بهش و مشغول دلقک‌بازی تو تمرین بارساست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=EXzOx6DMFDQq7KI42tPImcPLtWn2EI86ZZJV2cP31a8w6vO61huomMnmjdNA_a6Oa1ZpVJfWeKavqxf_cA5Drrn4YVXzd9Qwns-soe-_RdvA-3vhHxXa_Dc_MguC6ecpq6nqyrx08glnQUhkh97gTVBtvcrVa4URgONjdxV94Vg9vdzMc9N6QAwe7DzVk_bfUaz-C2gBwPpFnhDxKDudUxKP2g7tyfE3JkY4zp4-7Ak35M4Zs69mbg4ky1i3LJg5MFrqivXIIjxCHFao2XFaez90z6DqJ8KeW6wGHqIWL6AdtdJxienK07oN9Ymi70JfZv4fjsMVwaCRq53WUKGyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=EXzOx6DMFDQq7KI42tPImcPLtWn2EI86ZZJV2cP31a8w6vO61huomMnmjdNA_a6Oa1ZpVJfWeKavqxf_cA5Drrn4YVXzd9Qwns-soe-_RdvA-3vhHxXa_Dc_MguC6ecpq6nqyrx08glnQUhkh97gTVBtvcrVa4URgONjdxV94Vg9vdzMc9N6QAwe7DzVk_bfUaz-C2gBwPpFnhDxKDudUxKP2g7tyfE3JkY4zp4-7Ak35M4Zs69mbg4ky1i3LJg5MFrqivXIIjxCHFao2XFaez90z6DqJ8KeW6wGHqIWL6AdtdJxienK07oN9Ymi70JfZv4fjsMVwaCRq53WUKGyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کول پالمر:
برای بازی مکزیک - انگلیس بیدار موندم، ولی بین دو نیمه خوابم برد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTqMTOzopBlQMz85EYvAAc_b_9h8P95TTcPeWD538--706ahQ17L1POuRhHWA3u67HRdSPu8GKB5kvkGYXi011Kiol-jVY7K-o0thafRJYEi3CBxwTVBokeDo7AkWjNrvy6ssCradF13R15Dx80LIijlCXDOUtj5p_4hx8RK4zOV6ykvlFk1IJFHxcHafeFpDm-o9Gl38BboK4UbdGdMwaxrmXyW4KjwwqaiD0K0AKjEpe0JFfrAIvi6NN0qgJQATjZOKf5uM27dG_T9SKdCStyw1aCckqZ2xlsNmzTMLoYfEtVDKHRHZJep-qBwzrnw-IuCf_zO2TtZr4dKTXq9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHaNC-FOUgeyoWod3hEaH-6o6zhgahvq-Nj1glbcv7P8Z7oyLWqHJQegNLTPW8alsSMUOFH0_Rw3wn1dQDecWJP0TtO12wtdHzXzB5rJ7909BoEZHY7bQO89bDpgQ6TkmM-LM_05pcEx981cm_QaVQJf5HdCSyHWKpyUjvv4nmhqMFA5bDQ-7Te5bpQoeRQWO9Z-6_aeDgaHLHz5lw6ayz4vdli6geeYZ4SU07QCqvtxlRmxrOqJSwAfyfqr8PKtR2UQKqnkIExSX9tfLGe74rU0HpsRHM-AY3Z4g2sfYUcZ2cVCrhDxMcYfEf9nhaf9215DqfC6lHdEpgY7g950Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
فقط سه بازیکن توی ۱۰ فصل اخیر تونستن در ۵ لیگ معتبر اروپا هم بیش از ۲۰۰ گل بزنن و هم حداقل ۵۰ پاس گل ثبت کنن:
😀
محمد صلاح
🇫🇷
کیلیان امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQVbEFI3_nl7tX3aTP7UrPHX83nVHfwgB5f4i_Meehb_fKpfe3vdKruchwr9ZTSHKNkMXjYdJIxbRbFKweos692yWbVTQdcyqY6FiSOd9HNp7bruOnV7iN28n7h2A7f64_7WNnf9Bqvda4Eqi2OdEJmMfYdcy8R8m-fORG-wq0l2-1MuYtxTGpMSOIG6vWGhQ8FwgUUsxxcSHYs1t53ImbM8RsviLf6NEjOcVl0mgwhEel6zSpt-8aXpNFBBAU0B6T-WbiUi7hvfwwAZXP9oSxs8xTfUd1o_9ltDtE6fRoDVMpzKhI0g9hQlGsxfZ-QQ3pDiw6Co6ucH4jIO7LPODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg5xSe7fZIL7MnUbmiuaKnDWbPh182K9C80WvrVVFrSC4-SW8_m4K-ED7uVNG5VBLutpOhiniG0Hci0G68mw1x_8OJVcmeUdQ5TTZq1VzR9rTfJd0WZC-zh_XfBCH2by1MjKxMDbRNHcmV_6xF-UKyX9TsTSxMTd5yrfouRQS8fjsGmp0k3ih6UlxiwmliHEr_22_Ym35B_JGYUzCrcMx_UEKCLYL2szhwZ6GddVY6y9HX57d6VPvh8wo-A77Y0Ttx1wWxjWhhpJFyBwdB989o2af-0RC7nGaec1R6wUNAd3D0ZBSYHCjtMzi9BC8O9lgvD8dbahyCeDovYJ6tmDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqVK2D03pqqGWZ2c4_ycJmEqZkjiYnEJMbawVTKLeNr5BuuqZR1-8NXtAE7HQcPxwpy-px_HtKGLyhPPUR2j9Eh-is_-VraGkTanrBZTY8m8cHBgT3YGFBIzYToW6Brk1VA1uZVyFF1NM7A-8Nu-kwF8HKYWydSPvMTv8GDLn1dFiq6ascHpsz9eALfhtoS_dv6SjwoyLly9s9NXQOfH9EQFOrAxDU8ptqcnzP2vN4Ldx6ThQ6EZCgCixK_u9hsJpF_m_wY9il6-7z9bt548tqgoPVItxdrAg2DK2IbuUBE3g-0lKxVjvyAcfewTfwY8RAxXayRSwcFSLbY3-8qpEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102451">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A72nYCc9qOR_GJlg0TO7RnXarQcPpIHQFdsozH5CLcYg50Xegir8CbSwCcHb8GNVZ3GAOsrNrwkuFGcpMXZmTml-pm5fIBM8jeY-NKYf24jGvR7sF0wxz6Bgwo6x1Usibjv3GtWR-vSh_tfhEkT8POzO4I8dMQXIBA3q5UFXRt2G_c4DoxWd8_-jNrax58RAf8ovXqMtyFo-h4U3lrGMyJspPlxtouoHFX8q2es9LzV_WRvJvebXFiEVP7Lwx2RfjnLPmgM1P99Lj_3L-K46KCqZZCakIA_C67m4Yg-xfk3kHCqTtTVnDclyEBD17A2mowhS9pobqtojjKmXQDLILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN برزیل: رئال‌مادرید هیچگونه افزایش مبلغی در پیشنهاد تمدید قرارداد به وینیسیوس ارائه نمی‌دهد و پیشنهاد فعلی همان آخرین پیشنهاد تمدید قرارداد است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102451" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102450">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tggUg8x3jXMxuhVCVnHBLjW89AbD91DPEXxxdcn26yMahSqx3hQtklp-D4JGSAK2N9Pv9jSR7-9INGUMqR94Uu9YA2mPU9X1g7eMeiQK4Fh39Z-OtLSfV0al4FHHvWRhJjyBq2Pg3_Yxyoa_C0NSX1rdvJRoS-ZIpIqF8ft7g1PrH2tqSXLGgKwv1XyWu-O09x-5akg0jNGnAiJdcffRDtS8eVHScKxs32Sw7CbySy6BRRTVA2WA98Gb0g3XLNR1VjrGheRcYE16eEZbhAniuiAJuWagcpRsqBxi5RRozLUxekSemm5WQwVg__Ponek3137ZEi3Oo5GMEM3sHn8DNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
اینفانتینو: جام‌جهانی ۲۰۳۰ بهترین دوره از تاریخ این مسابقات خواهد بود چون در کشور زیبای مراکش برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102450" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102449">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jq984OOIdN0TeAY3t8y_4kp_fJtenORdwzT2KBpZcxCqQcONkdzXdiB56MTPnNCMN2mq15fa7-yp8p7pqYKAXccV6mBntkr6UR6FRebw9ky-aI6R92aCBku8eXUBCSqhOhfDYkIoCzOFJdacYYPFxpVh0y9H1acM06N2R5SFjKvRS-eVVPUKZyAsJ5nuuU9x9DAbe_HoFP7L2YAOe8DNrpPvXjRCzNCxRP-O4mk9FgsXbhtlruF7hZepruIGDPOcy1VgxiAGsR3MhhhD0eRS6ogZDiC6KxK6yFzHnkH8-bzMO1SN1HYp4mLsYqRdI57_EdT4CWAsFPSLxJ1Yg-PPxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس تعدادی از بازیکنای فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102449" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102448">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF7mHXJMDPn6pj1D7bO2cn0sk-4PaCyj5ucabMUfiJontnf9KZE6gxVd8AdPYvAqcRzZjCHOMrSA4Th8gaLUeFxHjxWjb3ACvIh-oJPcop0iQnQdiDRy0OQczo9zli10oYewbVIsgORVkKGT24wjHUT5WeLU1dLI9XxurH-Nsr4JYJyCmI9weJcqCSL4gulEBCjot3GGuO17aScmNuoitIvgxPAAdEeiLhzVt66gF_ikBR9u0Rd_7VZ4jQEY4_vL0M-3ME7sVQVIUdt827aH_3sJohN9Iovsgzs9dBZo0Q-JJGXClpL82qAh83vYhvd4T2w_MnzjqHG1LT8DrLbXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
اسپی:
انتقالم به مادرید خیلی یهویی اتفاق افتاد و همه چیز خیلی سریع انجام شد، رویایی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102448" target="_blank">📅 19:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRmqtRXhw3FWo5SJXdj3iz0oU3AIMrjt-MqizQ9L9P4DF2Xzn21l9X8fn0aA3SXMwFYoMphtFRpe3KMInQ8vJYlvq1JBZz6Odm589Mty1gAaUD357my-4xB3UO7ybb78DUH3m4vNd4d6_VFEkOo0CfIU-xsWsHE8PuClefZtrdIRyH_L3LhN_5BYMLu9xam4zLfLhi7odfGFJYc3AuU0K5BF66xao4zbJQrUS3hVC4L_FHNGmP_hSdlGO-kja6sHxoqMa0_yqIF83F8HMj1I1kqa9fkdKSFzdCwn8nev1BThVvkogkCWaWwqTSPV9o6GHWreNaRq9yyaZc7tR3E34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0l7SgMDHzAC4EPYoYnSa_1Xo6iiuizjGpH-28La7BAhOQwDtO3lLTrrQpzWT5IdUy5YP4XkwxevFGViSattOO75Y8-wzUvnITAHBHfZnazGGDi1tjxXXPYLKbHxHCVZUAwLLJY55vOXQinXybKMEvkjPYWmS7n5IFECDCv21YkW_bKtyqhVoXMTSbEy6dotYOZkFlQyvFWv_JDQih2FGlY4C_bi5BakpLC5R1crMYzhkjV4aNur2l_nYxmBH_EaRK7vh7sDsqlx36hckyGrNJSbBivGJvqm3c7aMzxT9P7cF1ScwtUnsBZLgl29IriNu9qD1eaD38UonYjpoS74BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzbVM0bpaZ3epshDwHXyGH5u8tQlhPlo1CYi_IdEJClde5v5h_NNIOe7qWxpZLwmVSbjzHwxFnopZ1P2g5J_60bzAoMa1UwhFjQJpD-688Yvq90ib5KEMa0L1dFScnxevvYltGG-kI47s9ebph1t2JOiP7I82t8JwqHXuTniruqWOW96K-PVE6AcRPtGEp41VrhmrnfxnZwDjnR4SViibgx0oN9wWtGG_FfGFTl-RQdtcME9Fz5x5ddqXcFhCIJcK0bIfRa9jsh7aA9GzPbrKi6zdx2MJMJoS6PzeCCbaCEZ014WdcXDwElLO4iLmBwdNdSvgmInfuxo5P2L7Y-S5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5XJjcRte4T84H8NRzsYIafSCfCz60dhxqLNMIhTr1TES3grBqIgr-t3Rg5XOHr0luuL9NGIiV0i9vJz3HkhyeOyZa3Lys-k8q4wOYJsckWo-BkmT_EBX_bhUlw1xszpCHaxk3h_AdFSvSRs1_4I7QMMayxANwPQmHBsZcV-TjnRBKUJ6NDYoJ-XRrDymaGyGwUEnk7tp7bRNC7i_xx-OAsZUOOFTbX8eFsQIVxffY6w9Ij-Qoth_ibLimk3W3M_-NbIInXz2GlnaJOy9m9uvmMHjP_eNzF_PiYd5eki9KfPVT1FCuUT9g2WsQ1lPiNDSiFYay7VndNFNwcx_hVw5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال لامین یامال با دوست دخترش اینس گارسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4mJw-sSkRFS8Me-W2wFP7ujpAHv0ko0c3vLjDjP_o_4yGtrDARtFc89R3q0rnXE9NcN0vDlIRQpTQQgHYqsO2OZ-Zik8TSjTt2-82bpV5Ny4LLbQhe4Q3-ezuwe0c1-Obh9e6YHqYh1PNRn4vDAiw7ZFFu4ye-fZHUUrDHCwKV3afN0RVaFD3NxqActq4KcjQe2CBpNkqTt-pdWUOfxFt_VFWpccNPqSH9wZa4CGCvz8s3XH-us1f2OUNLHrsgaoNMe4JxXVSQXkTr_w9EmdwXIG999wXEM81JCGZyoPhzjTD5rMWuSzB8s_lj1gYrUH5m5OAhOEen0krGTOmxyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhXzIw6-_Nf27oBMIG29Mm_iuQ1IFqGKUKxltC4NPwZPdTlVjXvbuLANQ9Lg-TP7Z7iJfWYGCetK6QSecWUspm8V_uMXcVwGYldEl_j1YWMT5bCxPybdzBars40Il_XZ4eYwlWtjtdUSi8v9ObL0gG8Me8HfCfk9R06q7KqIFGYTZklLBfZmpTXWD1mxHPkXAs99Jgw-EwrIGbKs1S9rldSK3ggN94icg6eypVOc8lF3j_0uZDuyPxJkRbvkV6QSv_YtMjHn5MIFDBaxYaAsSKjs-dC77vUAqWU-t_BHpD1oHql1NVy2cbXPBHKLjcjDzsJpFB9T-QUIw2NsmFFgEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHLDzC1J3KhbZBQ-PkXRWrsFUdkZ9qQ8nyNvNYI_AY8gqRQjKXlrxCnt-Y_xb4HZDENZgajhNX1ktQ1OHQRX9G3JInmjh2thsWQxlcjS2oJhN0Id_DrIGMl1AvEikiklgZVX34ZTZgBAe6yoBq5qN3_DYVmMehshPxFR2OT5LvnZQM47LOSAbDQNiIomY8uUzdF3iD3uahf_8nKO1TegfpgqqMcfw1dSveYsroVlXAQv_EJUQQLl_CaD7jvSESNhi3JXUQH5JnwWKvp5Wb_2PUda_28GDcno_3fMLBcjJ9wzrgoqF2LL_wgUEvTaP2C04_vO-QCU1Jj8MCcl748Wkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcKEOtehChuBKsuaRz-NrQbw-EaJ-WqEKbrA1AQU6c00iHW50457BWk3OKB2aiBx9L04P-3TZFLXH1I2d2F4CyPOGm1rMLG9RYCvCAZUMRHGIAqwH_5N03ApfdDhX3r1QNroBVRNFHDR8n2VRAsKOKbRa03w6cnsUYQxWot2uQab19uUQ35uG-koWi35HzJdTAV5PbkPNOO_TySQuiLlgQ4HE0NBI6RLGXLFXc5QoZMXxd4AZYvj2_CTFaT9kJMu52lsxkhsluJ8tstrT8WLHyxsoivmspWNV1fHO1CkcugjJ_c1VYPb9szj_E2sJxA5hR3oaPEzd4j6MB1p-GDXkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPoxTHIq_7w1_jy4dVw42qWLhtnppkfjD72UTbrXRAOc01Dpaij189TD3WWS-pXaOoYoyxDsqkymFanvNPSFRCshViqFvtM02T9dCrtqUpg8CyFXGYKWwNB8_0nEFEicUP4wpnLlWPiR7cC5almaiPZZF2ajYSklkW3nurUStYTFZ4cMQ_c3IkTLzGbcU7yyTYQJjgjJduHhp_qBfIEplaVkRcyAXiVS1hOpMYmNozRdRRrQWHa3APKahY4aaOkpMefR1jWH3MlRJawt1QKBxdxdo8cDc_ucO4uKJIDDI-LStu-fM30iFumBFRKEcFARwo0RahitzZNKnJ6-Mg3TvryE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPoxTHIq_7w1_jy4dVw42qWLhtnppkfjD72UTbrXRAOc01Dpaij189TD3WWS-pXaOoYoyxDsqkymFanvNPSFRCshViqFvtM02T9dCrtqUpg8CyFXGYKWwNB8_0nEFEicUP4wpnLlWPiR7cC5almaiPZZF2ajYSklkW3nurUStYTFZ4cMQ_c3IkTLzGbcU7yyTYQJjgjJduHhp_qBfIEplaVkRcyAXiVS1hOpMYmNozRdRRrQWHa3APKahY4aaOkpMefR1jWH3MlRJawt1QKBxdxdo8cDc_ucO4uKJIDDI-LStu-fM30iFumBFRKEcFARwo0RahitzZNKnJ6-Mg3TvryE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=TMku10MMu9u1SrluTejV7rvqV3OY7-sOI2RDkgUWdmubEMGo1UtNlE43uVpzsuJcqyzSk5F4ucq8FwJyx5Rv73MjqPYYPayTchJF0oRJDEnb7ymKbFbrIOkkjDomGG3eFiLvO6VxJeUQv3fCSACq97gkFEVwCiU61FgxgQI84hp2wIQc4-BdXjjXogEBgc3G-kPe0mnvIlPUAxSz9SpB1fEw2gAPqu-z2b7cFg9n5GHyDrNmnDpXIVZ5jNraVMmHsS6XBp8KPisRWWDOkcXADNiRpN0TEuokU1FKm1smfLUBJxMFCUt2GQ4Uc_-DkTPIU5MAReji5nJyo8aVxlTssg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=TMku10MMu9u1SrluTejV7rvqV3OY7-sOI2RDkgUWdmubEMGo1UtNlE43uVpzsuJcqyzSk5F4ucq8FwJyx5Rv73MjqPYYPayTchJF0oRJDEnb7ymKbFbrIOkkjDomGG3eFiLvO6VxJeUQv3fCSACq97gkFEVwCiU61FgxgQI84hp2wIQc4-BdXjjXogEBgc3G-kPe0mnvIlPUAxSz9SpB1fEw2gAPqu-z2b7cFg9n5GHyDrNmnDpXIVZ5jNraVMmHsS6XBp8KPisRWWDOkcXADNiRpN0TEuokU1FKm1smfLUBJxMFCUt2GQ4Uc_-DkTPIU5MAReji5nJyo8aVxlTssg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NzuyrCkkInyDl9lr3-ZecPwgh02HJpWAjeLJLFKiAZKyxrPMHoYPBdnGqBmD6l-9tMlTsg3ZMI2c299teywoFHbsUfcsTXByZCYdeNseuLvHTs07BifLdh4J6b4NzKfkuA_j_g96q5nrzCLJ-NieONw8fEdZXj4SlfNNrWF92q7-MCN2VaVbNc43qU-DfjJ1Xss7qurhY1W8axt1bp13YNEZYjX1XfN2E671FRd2TD3IlgnIAsDShGYtWrUbYi8258Y6rHYUt5wYeCHpsrE0Sxs8i0iXPCIVqnRi6h9NJzmZGnaK-XSn1f1LjmHzUn5sRmHei7q1UhYIbFLKiTjoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_COpxUffL6r2H-yi7yMfjP_BRdXQloGvFH1oRXMZnEUNhXeIhaA-IeBRuH85mdorkFdio7cTV_C1q0KoazEehHhG82rpyOYuAU1WW1H41246eFUvAIqSRZEsgm2ZbSgod4k7E2Ep5NBaKMLTp4ABo_h4we1Gcq5JqFeaGPez2ZeixsJSfBhdeIoYTage1fW8HNSDvIahRpw0Tzp54DnOeN2zrfU7SPex2N5JY9PAoYttBISr6d5T4VD1xD78iFyp-8zamcpOkiEwobuU3rG38WsFTovdXLkeNfqoHqKKge_5vqBIgDOynazrhwU8pTD8r8nvRoHodE2rfODWWQkWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
فوری، محرومیت سنگین چلسی:
🗣
باشگاه چلسی به مبلغ 10 میلیون پوند جریمه شد.
🗣
همچنین، به طور تعلیقی از ثبت بازیکن جدید در دو دوره نقل و انتقال محروم خواهد شد. به این معنی که اگر بار دیگر خطایی انجام دهد این بار پنجره قطعی بسته خواهد شد.
🗣
در ابتدا 6 امتیاز از مجموع امتیازات چلسی در فصل آینده کسر شد، اما باشگاه درخواست تجدیدنظر داد و این رأی باطل شد.
🗣
این رای بخاطر تخلفات نقل و انتقالاتی در دوره آبراموویچ مالک قبلی باشگاه صادر شده است. مالکان جدید این باشگاه خود این تخلفات را گزارش دادند که باعث تخفیف در حکم نهایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102435">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=JbBlOe56VZrWdjuQDbg7y4Y8ucT95k_yA2wR1fQAELI594XyQr0DSBPgq9Ih0IhgaR54qj2siwc8s1jPXfCZjySX2i09axLf02iefJkzjI1ad1D4DsLriXIVrCpmmXg-AubLju-dXVI5Anroz6phh6IfQoBhXIp5Tvawb4ccz8UJ_ptFq-CkkhmEW0rtPSm_klWv5Ak_rpWjWafG4OmzsmIJxrUlCyh5NVyoQ-ikqCIr0k8cKXzT27DCyxTWVlPlYQfiGVHGZ7-vy4J72BikAyTKNGAEr-SWc8SCqYMVXEGbwxuF8I_4tEx6XoxLXv-X4mjqHi4zt5elDHXyDZmv0YU8gIHGMXSDRzcB6g0clia-8hGlmIMlFv8kkbhSRfBiT3VJLlzLD8hU4f78LgUYwh2q9zRj1f1lXgnWRcW1qqyHwXnMcmOA0U_FG3i_sGaiH8C62A7TCYWM9pTCSxO_EvCZrIPDKMB7q2JgIFLijXYkeXOxIJJU8S4cmc3thJFIX11ZD_M1SNXmdG83DjnX63bAtplxRbE2fN5ZJErY3bUWAehTiXRxR7BEVH-d1TdjBm3oNjs6STjwwDjdkkUOMkJfMmm75BnBaF6Gx7-TG7Go5GrTktomjJj2AI8vdu5sF_6quD7JCfbKjncMNNPq76UQ06YFFJftCyUMC8zojdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=JbBlOe56VZrWdjuQDbg7y4Y8ucT95k_yA2wR1fQAELI594XyQr0DSBPgq9Ih0IhgaR54qj2siwc8s1jPXfCZjySX2i09axLf02iefJkzjI1ad1D4DsLriXIVrCpmmXg-AubLju-dXVI5Anroz6phh6IfQoBhXIp5Tvawb4ccz8UJ_ptFq-CkkhmEW0rtPSm_klWv5Ak_rpWjWafG4OmzsmIJxrUlCyh5NVyoQ-ikqCIr0k8cKXzT27DCyxTWVlPlYQfiGVHGZ7-vy4J72BikAyTKNGAEr-SWc8SCqYMVXEGbwxuF8I_4tEx6XoxLXv-X4mjqHi4zt5elDHXyDZmv0YU8gIHGMXSDRzcB6g0clia-8hGlmIMlFv8kkbhSRfBiT3VJLlzLD8hU4f78LgUYwh2q9zRj1f1lXgnWRcW1qqyHwXnMcmOA0U_FG3i_sGaiH8C62A7TCYWM9pTCSxO_EvCZrIPDKMB7q2JgIFLijXYkeXOxIJJU8S4cmc3thJFIX11ZD_M1SNXmdG83DjnX63bAtplxRbE2fN5ZJErY3bUWAehTiXRxR7BEVH-d1TdjBm3oNjs6STjwwDjdkkUOMkJfMmm75BnBaF6Gx7-TG7Go5GrTktomjJj2AI8vdu5sF_6quD7JCfbKjncMNNPq76UQ06YFFJftCyUMC8zojdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری کورتیس‌جونز، سیمیکاس و سوبوسلای بر سر بازوبند کاپیتانی لیورپول در بازی دوستانه اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102435" target="_blank">📅 17:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102433">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hN1Fho1bSJyAo8xlUADVnsAoTUcCzDHl_-_yawGrbqEEYk6CwENmTYN9VJSszOkBJ10QhYKPeUGbmEIYm4qI-_udwVUgdr0-GMvXS0sxCbstiHz8raHjDLYw3lYUw4vUDJ7cSqftRMEHwPpmVQbNG010-NMQCLz78KEtjPQC8tzAsrDgjmatI5toDUD1mGyvmJjGSNFaaUinKLv85cMmTGCTVf4Msz7sJPREqB6El1-bXdLrFWWfyRD2OgWhSjM0WYHyMMvSxZK9rIhllfq5xjmsLubcHwH3pcUfOwOkwoc9oecUV4AHCFmPEaAYhj_5CZ_BMUY8cJEQlGlBfFfLHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeUvXR58uywhPZ7Id9t6lSs-d_EseFCycR1XPBgnysDXkqhm41X3AxShoTwxeveX0lVnscfN6p1shRD7LjCjixL-iL9CSzPNqu5mo1sdqmBr9Zc-fskYIWZ_dqdST4FgODVwYtAp4cmJRDxMbz65OiEH53QDMfArHfas7il5Wj-YExurE76TYS359luLgimbzZhvE07CIaGXBy3T5M3WlCeVtTSEN9Qe7uMdft_kJRmwPF2kRvGpLZT9dDhW0kQ-f3_nX7r6DQbv1RRDO8b3x7wDCNotf72asaSc0ukq8rEBXQtzq6ibcXCe1DlBsyg6NZFHHko29kR8o6gYqLj02Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ال اسپانیول:
پرتغال و اسپانیا اعلام کردن اگه اینفانتینو پیشنهاد خصوصی سازی جام جهانی رو پس نگیره از میزبانی جام جهانی 2030 کناره گیری خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102433" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102432">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96363baca3.mp4?token=vMsU_AOlraaiMkZ4rMvrSeojLw206PdaQ0eVT1_1_peBX46tUz2HRkz1pa0G1YZV1nenD_DU-G7rpeyhEM7mc26MLzaaOmo5nG15pPir-x2wGQQ53_wBO7cwXcsXcTZw1quh454PaJiB5tKIkLXqmQpxPcA4xY7XysMK9eJ6l5tyNI4kVv5er-iZIlpcjzrmYtffM0_005G8nQj3p_0ckyM2YDqsE9tQglufnWRdL4ODIlDGMJn5CBf4EkIRYMmkKEJKyTdw9qA0Re-CYW2VL3DDS9JgDRPx_QTp5LyAmPJl0Ov_hvt3soiKLtwiXCCXBWKdmv6t3HyN6dt4hpOZiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96363baca3.mp4?token=vMsU_AOlraaiMkZ4rMvrSeojLw206PdaQ0eVT1_1_peBX46tUz2HRkz1pa0G1YZV1nenD_DU-G7rpeyhEM7mc26MLzaaOmo5nG15pPir-x2wGQQ53_wBO7cwXcsXcTZw1quh454PaJiB5tKIkLXqmQpxPcA4xY7XysMK9eJ6l5tyNI4kVv5er-iZIlpcjzrmYtffM0_005G8nQj3p_0ckyM2YDqsE9tQglufnWRdL4ODIlDGMJn5CBf4EkIRYMmkKEJKyTdw9qA0Re-CYW2VL3DDS9JgDRPx_QTp5LyAmPJl0Ov_hvt3soiKLtwiXCCXBWKdmv6t3HyN6dt4hpOZiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مرزها برای میزبانی از زائران اربعین آماده‌تر از همیشه
🔹
در آستانه اربعین حسینی، پروژه‌های عمرانی و زیرساختی در پایانه‌های مرزی کشور با هدف تسهیل تردد زائران اجرا شده است.
🔹
در مهران ظرفیت خدمات و زیرساخت‌های برق، آب و روشنایی تقویت شده، در شلمچه بازسازی و نوسازی بخش‌های مختلف پایانه انجام گرفته، چذابه با توسعه امکانات رفاهی تجهیز شده، باشماق به سامانه‌های هوشمند مدیریت تردد مجهز شده، تمرچین توسعه زیرساخت‌های خدماتی و ساماندهی محوطه را پشت سر گذاشته و در خسروی نیز سالن‌های مسافری، پارکینگ‌ها و فضاهای خدمت‌رسانی توسعه یافته‌اند.
🔹
همه این اقدامات با یک هدف انجام شده است؛ سفری ایمن‌تر، روان‌تر و آرام‌تر برای زائران اربعین
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102432" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102431">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">💥
🧐
رونالدو، پسرش و جورجینا درحال عشق و حال در گرمای تابستونی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102431" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102430">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=NvPn2PQKD4EUb719A-_0dAXuN2Wco7zhWepGT2gVTKpj37Dlu7HyUTE5ekGtK01zcY44U-cSe8yeEwAuRzLc7-xAysJZEuwX9lal2MV5zgqzemwa72O6EiSdqS8jVMsJrkvwbR6yZETUSDlLjLvJfwpGP2OBWlNFvqV2HWZ056j9Lhr4dsWsd9ClODCsvW7gjdeNEUwHqCjQAL-N1FQL3qRWZ2hV7lQBTrDuYsUIlsKv7rBUqKknUuVtt7qQ3Y-gnFm5ZhkmAIjPLb_6XHnwARdB-XetbaSyzJGtYb3o_EJ_h61rsXfBY0qlryY7safFcIgB_KZ9pXUvqTmGPBIQ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=NvPn2PQKD4EUb719A-_0dAXuN2Wco7zhWepGT2gVTKpj37Dlu7HyUTE5ekGtK01zcY44U-cSe8yeEwAuRzLc7-xAysJZEuwX9lal2MV5zgqzemwa72O6EiSdqS8jVMsJrkvwbR6yZETUSDlLjLvJfwpGP2OBWlNFvqV2HWZ056j9Lhr4dsWsd9ClODCsvW7gjdeNEUwHqCjQAL-N1FQL3qRWZ2hV7lQBTrDuYsUIlsKv7rBUqKknUuVtt7qQ3Y-gnFm5ZhkmAIjPLb_6XHnwARdB-XetbaSyzJGtYb3o_EJ_h61rsXfBY0qlryY7safFcIgB_KZ9pXUvqTmGPBIQ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تمجید جالب کاسمیرو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102430" target="_blank">📅 17:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102429">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=ocC96I5aY8gsnqiUO0KQCJ0USWqrMvIgZcpN0X9k_Bp01LVentvUIPlYPRipX6FakF_DadaNwyKgfAeaSCF3MrwDdiE9rkYcXJpKqeylmBNDvHs9YhKLN6vxSPJNC9a9bpZxczJxG1IAng5TST2xUESJu6_F0x4m8fCvfhGyjojnfzaEeuqCY9iq_ts7xkFzKbSiGYx_7gSTLGEKLwnsnjjYpmqIPEmxp_2w4vklmMmUgFzxTnxhnGhOVlEl0e6QaMWwPE9FcHacNbco8i0Ix71XZ2RA733sqBtWTDwMF1MKwhSfSSQEVgapNzICU47xd1dg0eF2E98mYVJkIRL6bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=ocC96I5aY8gsnqiUO0KQCJ0USWqrMvIgZcpN0X9k_Bp01LVentvUIPlYPRipX6FakF_DadaNwyKgfAeaSCF3MrwDdiE9rkYcXJpKqeylmBNDvHs9YhKLN6vxSPJNC9a9bpZxczJxG1IAng5TST2xUESJu6_F0x4m8fCvfhGyjojnfzaEeuqCY9iq_ts7xkFzKbSiGYx_7gSTLGEKLwnsnjjYpmqIPEmxp_2w4vklmMmUgFzxTnxhnGhOVlEl0e6QaMWwPE9FcHacNbco8i0Ix71XZ2RA733sqBtWTDwMF1MKwhSfSSQEVgapNzICU47xd1dg0eF2E98mYVJkIRL6bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102428">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=F5umTzEMoKp61Hgy9kdrpyPRZHhwDnzNephlffNFHJ-j0TiQlhHBKOYWYkGiQM9DsdL6fgvzhhigWOBDCB4HXNG2FF0IPVaTbIRdcs6BIcZBR7tbFbMJcFdwb5JmigWwK_HKt8RFhDeRnji8sJmAvinDT3g7Xx-ugtY7KG2XXWrTwCUbiofa3cpYT4BgPaKDzwc1C7my2-NV91VKOAbpvSAnBPu6R5YG4gjyvrjyEju05aaLuwwIxgnGBXdx681a4mUT4Mqig9RxQhxWi9Qh8S2GZ0kDUq5dOsVsqwYLKjrtkih9sEL7YQYuJQXWp-E3oyhOvKTeDxqPO7edmcACGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=F5umTzEMoKp61Hgy9kdrpyPRZHhwDnzNephlffNFHJ-j0TiQlhHBKOYWYkGiQM9DsdL6fgvzhhigWOBDCB4HXNG2FF0IPVaTbIRdcs6BIcZBR7tbFbMJcFdwb5JmigWwK_HKt8RFhDeRnji8sJmAvinDT3g7Xx-ugtY7KG2XXWrTwCUbiofa3cpYT4BgPaKDzwc1C7my2-NV91VKOAbpvSAnBPu6R5YG4gjyvrjyEju05aaLuwwIxgnGBXdx681a4mUT4Mqig9RxQhxWi9Qh8S2GZ0kDUq5dOsVsqwYLKjrtkih9sEL7YQYuJQXWp-E3oyhOvKTeDxqPO7edmcACGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیاز بود یه آیتم جدا برا لحظات تاریخی فیروز خان کریمی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102428" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102427">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=g1ANX80bFjLD6qTsXEAD6OY-upxth2W7GxrangKiiQZ6-0UrlUUAQIKoW7RO0OFJZflalrSoJ3uNgPhQiTpZT0L0WflBMir9oe4sB2iLapBjALFVlSVlbbzEPpT8u_k8sw5NMreusocrer8cFBXpp0_CEdzumbWtXcEqeTJr-3Zvt4zcOV348zFfQVcVSnBshk5bbhk3czd48fTqPc6da44cjxSE8mlpxjfJGHsybpnLVYcNtYuvlUBzr753i43Bfr_wHKeszmayQIPjTgO85JjzRFiz8wmxRnP8ZSYfC4Tewo85BQ2cDZVnM5WlpBStcjfbpsFxiTt11APWqSyEMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=g1ANX80bFjLD6qTsXEAD6OY-upxth2W7GxrangKiiQZ6-0UrlUUAQIKoW7RO0OFJZflalrSoJ3uNgPhQiTpZT0L0WflBMir9oe4sB2iLapBjALFVlSVlbbzEPpT8u_k8sw5NMreusocrer8cFBXpp0_CEdzumbWtXcEqeTJr-3Zvt4zcOV348zFfQVcVSnBshk5bbhk3czd48fTqPc6da44cjxSE8mlpxjfJGHsybpnLVYcNtYuvlUBzr753i43Bfr_wHKeszmayQIPjTgO85JjzRFiz8wmxRnP8ZSYfC4Tewo85BQ2cDZVnM5WlpBStcjfbpsFxiTt11APWqSyEMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
▶️
رکورد پرش سه گام جاناتان ادواردز (۱۹۹۵) با ۱۸.۲۹ متر ثبت شد و ۳۰ سال پابرجاست. این دستاورد استثنایی در دو و میدانی تحسین شده است. ادواردز در مصاحبه اخیر بر تکنیک منحصر به فرد و هماهنگی قدرت و تکنیک تأکید کرد. او پیشرفت رشته را با شکستن رکورد توسط نسل جدید ورزشکاران مفید می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102427" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102426">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=paayGEfUCrFqFpLJB1JH_evdJQjuRsO19z-GQr4Wks5-RbZAxVxr0BLG4ePesQHoK664zrtk0gSGwJs0TnjYqCF-P5vnvHg26_18SU6Je1KI8rkL0avib_k8srhjZYJea8sOypxlP0bTraRHbPDZm998J-A_70wxln1yuE7ehyAU9oISUf4dyQy-SVCxcv5NoV56Slb4mOIB7dcdF1PxlwqIAgW75yi_ULg5qY5ifyIH6OPtdjv70AjC74fQqlBmTLbn6Ueu86ZFUx11EZuZE-M_ZoKqMU7Ukcofy6QgfT1YEVFENmzsO6V7ju-y2q8JRDTmUx7gNbPsCj0lolWyMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=paayGEfUCrFqFpLJB1JH_evdJQjuRsO19z-GQr4Wks5-RbZAxVxr0BLG4ePesQHoK664zrtk0gSGwJs0TnjYqCF-P5vnvHg26_18SU6Je1KI8rkL0avib_k8srhjZYJea8sOypxlP0bTraRHbPDZm998J-A_70wxln1yuE7ehyAU9oISUf4dyQy-SVCxcv5NoV56Slb4mOIB7dcdF1PxlwqIAgW75yi_ULg5qY5ifyIH6OPtdjv70AjC74fQqlBmTLbn6Ueu86ZFUx11EZuZE-M_ZoKqMU7Ukcofy6QgfT1YEVFENmzsO6V7ju-y2q8JRDTmUx7gNbPsCj0lolWyMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو کمتر دیده شده از مارادونا و فن‌پرسی
💘
💘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102426" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102425">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43f315425.mp4?token=QTHROFqpgFJ1OmJNWgGIJguKdIWMMNXwCprye4C3ZWJOI5xNnC1BaQiRbqErUHGLVCf_zx4JMnH-jKbM1aq09XQMlqGTrobAx2glmcXJfIlSUlq5C-VOG1Psgg3YxRbMbkbsisJSllHTqY4oOzsQyt1g5JpettsIFcQM-lEUy2VzsN1U792Bb-RatETUyowMWZ9TWEjX0QHCydXC7obJG2RLGtadusTVt9uo6oLGRJEbmiAl3iDtTKBIr49jRgJiV-qGsSXXR6CYEg8BFps9045JFwNrYaQG0KtFiq20xD6UNU5exARVifYgMJQdfdpDK4Q4p4luVQGKX6ce7P0CSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43f315425.mp4?token=QTHROFqpgFJ1OmJNWgGIJguKdIWMMNXwCprye4C3ZWJOI5xNnC1BaQiRbqErUHGLVCf_zx4JMnH-jKbM1aq09XQMlqGTrobAx2glmcXJfIlSUlq5C-VOG1Psgg3YxRbMbkbsisJSllHTqY4oOzsQyt1g5JpettsIFcQM-lEUy2VzsN1U792Bb-RatETUyowMWZ9TWEjX0QHCydXC7obJG2RLGtadusTVt9uo6oLGRJEbmiAl3iDtTKBIr49jRgJiV-qGsSXXR6CYEg8BFps9045JFwNrYaQG0KtFiq20xD6UNU5exARVifYgMJQdfdpDK4Q4p4luVQGKX6ce7P0CSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚠️
تجسمی از المپیک اگر تهران برگذار میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102425" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102424">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGiBI77AfWOSDW2J_qdja4ch8NtLl9BORtIfcySLgOrW-vFNAjQ-M0kLuM4OSPfWdDyOf0J_jqpSSm6C_qGL929_VpwYNmEZgh8xgpyLsqHBG5RWgtEYwqlQkNdJrXR5JLuvkvAfBxGZBYc_C2ygXsUkWlaIgYsNenCYvbiKlBxy-jtNoiUrPY2wVFOqeM-7b31cKl4S9x0sfYQT3CeWXS7NBkHumYKKtMnS3XjeyuiTnmqMknxHVyry1NnYCm3u52XU4RO-0ZUEcp3IGiL8WX5zF9WUm0j7NKJGc_ab2fyGyflDNL-v3mw6zs7EtqN44dJ5M3nPgrgo3LakyI5q_c7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGiBI77AfWOSDW2J_qdja4ch8NtLl9BORtIfcySLgOrW-vFNAjQ-M0kLuM4OSPfWdDyOf0J_jqpSSm6C_qGL929_VpwYNmEZgh8xgpyLsqHBG5RWgtEYwqlQkNdJrXR5JLuvkvAfBxGZBYc_C2ygXsUkWlaIgYsNenCYvbiKlBxy-jtNoiUrPY2wVFOqeM-7b31cKl4S9x0sfYQT3CeWXS7NBkHumYKKtMnS3XjeyuiTnmqMknxHVyry1NnYCm3u52XU4RO-0ZUEcp3IGiL8WX5zF9WUm0j7NKJGc_ab2fyGyflDNL-v3mw6zs7EtqN44dJ5M3nPgrgo3LakyI5q_c7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🔥
👀
۵ گل زیبا و برتر اولیویر ژیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102424" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
