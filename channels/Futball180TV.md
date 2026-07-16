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
<img src="https://cdn5.telesco.pe/file/i5kruk9pXJTOKeHAEy3brOdrH8Ko6UcvZYbY0nh2Xe4PZM17ji6NGz-NGR16jvEwAF2qFqK9fxkuYy7gFHjlN23TPdwdXckqFB-kMsl4yIZqlzuo1tn32cApPLsUK4jyCMM96UxQycpHOtmV0CI0EWHIo6ksNrfL7jrqLWgaFvuSTx0O8vqOka9bw4hB58HIKsknftNO3ph-T-rtDPzvoouKgi4gAlEoouX61kmXm-K07uZy6YBXK2CG-gKRdgOjzrMbm9Gp3J3Az1wXvafUkoUouBpJk8yaAv4U-K8N-jVy_lwD7A20K5ppOsjkX1uM-62FzTR3sPDp7i0A9VAp2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 568K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 00:59:52</div>
<hr>

<div class="tg-post" id="msg-100572">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bw1-ZdbH_yAb6wges4SHC4QtBcCexTiecU-Ox5M5u1qITdGki-0pz5_Oi8YXchEkvGB8TCRjeH_QCdA6MDD_peeJ354rRPl1e0SKJH-2LVnC4FR0GBwfMY9WyTF5SktrEXRjybQgh6NrduFsetN4nUFhlBBQ3kCsi2ayM1XIIhRcM-Xwrjca0ko0leKH2qdg44wfgApSFpi9ujxBOl5JSEUBMpNPV9dTZ4F6T8z8md2pkL90yj4X5mW-7ZLRth_y35iKEGvQ4O924DeKZBOWWV1vQyxP1OLYMnro2z5aM7MSVD-JZXAxVVZiRTphi4tCLSSOGrRlmx9ZeUNh9LrnDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/100572" target="_blank">📅 00:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100571">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrssHWxFPMPhe2vK0kjeKDs7PA7uca3UtdJ1Pc_TVV3-YKHjaBvER1YET_-48hKkb5dEkTXnmSCMQ4uDYAcj2cz__PtV4Gq_wy65GgPC-bDjzVs4wkHTHPnW7AOQLuc_rNx2Sdwhb1UlIZtnn_pt3ThrBqoE-LA_X-cIt2TJW-BZC7o2sdpxYJgYLJjBOGRPsuU__IFWtEKu1kzKmRGPAaerbsyG44Zn2YUYSXrfAtcCMrj_Ja7XCaETBqdo3-IxC8e-P1eI9ZpYKnKes2y5BGCdm-OuYBZ4djMgwPqVoqjcnvHOUkoSANtWDIFyg7QdtqaEPTno1Jq1v9eSJr9v1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رسانه‌های آمریکایی: مطابق صحبت‌های رئیس جمهور ترامپ، حملات به زیرساخت‌ها شروع شده
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/100571" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100570">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHBGfT_DzJcSsSdx5oPmw6P_zvEMsT7JJj3Hy1Xv6Pid-6x9Frb7MIkF5H8qytVu31dNa2u3hNt82YiUnFRx0x6eu5sMqaOnKkjkwyyGTcBhT5O-KqTH_MWzoVm_oOmZ9XyzzknXjuW6JkUyeTaUwrq0ughM78vBt6VbJDTvz7O9kOwAgtZ1RlAvNR3Tehmz9g_xAutLzj5aLINyy6UPhoDuvSnxjPxHKd8mKRwa7FE4KpgWl_MHWieHUZ_I1wYwC80_lXXH3gDmu404MSBPj9gmDXwyCZkPURFch5EUIGpKnVV61Kb-uXNO3aErqjgKbIZg6-D_0f8sTucPbLJSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100570" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100569">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orSRCvQqnajs81FWFIeuOVhTeVCUBABA3Dnc9AUHlbz3jBmVu-GzKXbfMgkw0e_QuCB2ndQX8B6l1MbksS_wQO0lQ9jLwJdKS-AQPwT5G1U6eqknO6Bsc95hDbgWIt5B4LLcN_RHuacvrhzimxqMCBOeVl3_6B-yBeBJtFL_imk2j1zZJwj4k2dYdCv2VAGnPTokOhH1A1ZeixOGmS8lYQwWCQl4HNkz8jrp8SaZNNJpTPE-WX9IoRTkf30K6kLE5EcB_G5hbkLJm6BBhoANkMto6DjknrDJMWg0vwEi-DZV_ypLNLxfY5b33JO5G9W-k836PDMsDHQ18IYhjH6KRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100569" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100568">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
⭕️
ایستگاه راه‌آهن بندرعباس بمباران شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100568" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100567">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Afg6oO-ovq317_tQTOo0HxO0ggUX-lRgpM0yRmrc0WM13OZuX3D6hDfRDh5LG8vuEeWCzw0OR5UaWr5x5ly4XOyUxmPSMeAT5k-o9cYHiOxpX_OAB7x60yLW3jYxbDF14ogWhScxsY-Y4sk6R18pMXL656qR6e_1Be3ipOR4PLs4BDdC3sXHuNj6wgFe2B0Wr63WzB9SAGimMCbaL5V89OOW6gMk08U6I5OxsDpdVwOh9qJCe0s8ZyULqG2_H5roQfl4d7DRqXGAwOlHL4UA3XNu8VLhst_6mW4hWAdPUQ5wVzH7QQ62uqFfo5NPRUe4idQNVoxHhWHCxCgG0GiC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، تو فینال جام جهانی 2026 حضور داره و شخصاً جام رو به کاپیتان تیم برنده اهدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100567" target="_blank">📅 00:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100566">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMLrZ9MjbmGQ5Uw12JZF48FwGQHToWaBKn8pAZmwLN7BwJ4-rJnc07jLdIdGhqrrq5cM1YScmnNz5AyMwyrZasakkH83Wq9mS-2WjZPDHU5a8uRvdhRr-QvyvV42GUAm7vwt-pSojVDKkH4RUkgnigS_4kopyP3QQ8Q-fkqfiFBZfHAHdFslOxj9RsPmAn_kdKx_ShrL7Ijie1-5vPYa4vDjK2bcRzLU5PSEn1lyN7kKXlc0VmjwHparvuMff2I6j1IxRSSDV69hLh5bDt14UVotkGOb3CACUdrbeT0PvYWax-MqMrqnn8t4s3kSCUvepLf3hUF_0Y3RhV5Asl9Vwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
محمد صلاح قصد دارد در این تابستان با باشگاه بشیکتاش‌ ترکیه  قرارداد امضا کند. صلاح درخواست دستمزد ۱۵ میلیون یورویی داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100566" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100565">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
گزارشات حمله شدید به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100565" target="_blank">📅 00:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100564">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=Be68sHZEO3kY9b4FOeraWGvrcnmW5RNGawVCp64gDXk5HX4QdJhNJbZ90X1sBlW5X6NW0qZGa54imOmoEY02Ivs8aGdid63JORSxGlglaP4aDwN_6q0iCghIwmLGoC1hjtkUGNk2GjW2mdpRpgQao-WP2t04rT41SU7Fb_8XDtBeAD66fTIXYpyhsfGH2trzpv5xwhbKvo8bqXxcQ8VrA02Lrqlw9-yCW5V9lYJPZ1hsmAJfWphvpsqoAWusfwwx_WSPS8fxwbwiQ3VSzPYANqxA0QiaWyiYzwcOqepsjScSEGlvPga7tvNpBqOL-9YwXDbbqThfEFMRX7aIvul7aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=Be68sHZEO3kY9b4FOeraWGvrcnmW5RNGawVCp64gDXk5HX4QdJhNJbZ90X1sBlW5X6NW0qZGa54imOmoEY02Ivs8aGdid63JORSxGlglaP4aDwN_6q0iCghIwmLGoC1hjtkUGNk2GjW2mdpRpgQao-WP2t04rT41SU7Fb_8XDtBeAD66fTIXYpyhsfGH2trzpv5xwhbKvo8bqXxcQ8VrA02Lrqlw9-yCW5V9lYJPZ1hsmAJfWphvpsqoAWusfwwx_WSPS8fxwbwiQ3VSzPYANqxA0QiaWyiYzwcOqepsjScSEGlvPga7tvNpBqOL-9YwXDbbqThfEFMRX7aIvul7aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صدای پرواز جنگنده‌ها در ایرانشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100564" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100563">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100563" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100561">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=s7KfgZb4ppJ6aQlCbrKRylYS8bDAX7Iw2xD_UirlHs9mGM5lU6T-O2ue9Cm9laWQoEOkmq9mlBe-1rRhCLuG9cYmQwzL8JsTYAEpzThtMc9aJuX0OkzkVd5MaSRMXz3BbTXRZV7a4JPse_JABs1KnVUPDkjw3HyBtVI5xYSixIQwvxwVtlV1d5XkS0Vv8vhNdIYKCtN8xC_Wayo0AGuWoO4js0WvMTwvuHStkJ3sKLWHe4QisVImR_lwoGaJJzOdC8x0tuGz1RMT_7CuTkHCPPKN9QhM18C2kJza1WHB8EgUYPfZgIIl70xxCJFJdejrl28H_4AyNqtnqyk2X3ERfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=s7KfgZb4ppJ6aQlCbrKRylYS8bDAX7Iw2xD_UirlHs9mGM5lU6T-O2ue9Cm9laWQoEOkmq9mlBe-1rRhCLuG9cYmQwzL8JsTYAEpzThtMc9aJuX0OkzkVd5MaSRMXz3BbTXRZV7a4JPse_JABs1KnVUPDkjw3HyBtVI5xYSixIQwvxwVtlV1d5XkS0Vv8vhNdIYKCtN8xC_Wayo0AGuWoO4js0WvMTwvuHStkJ3sKLWHe4QisVImR_lwoGaJJzOdC8x0tuGz1RMT_7CuTkHCPPKN9QhM18C2kJza1WHB8EgUYPfZgIIl70xxCJFJdejrl28H_4AyNqtnqyk2X3ERfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100561" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100560">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=kC6G5jHPdTWIAAHcomh-KClPDSdb5G0sxPZE3NawBwlFOY7PEUwIAqVYSzGa7x0NbjqxU_W5C9f6PggYomIITHz09kWZrqhJs6kMx0Fi7oAy_3eYMEd2qQT7FLJt9jpfPRIc0FQ2R6lUQSuK81fZJHwwV9dwdEUFKtLfIK7xOpNlImN8L2LfDNRXcf7eIYWuLSpg3Oh6Wv9Kfds_BHa_LSIAy_pt_uwMtKPJaZfKQWiUMGpUzgR7IePRiIimAgZ6_O72C8Jf8vyq3Q-9wuSba57KSxQysqwurGo2ZD9PJhCiSL862YfQJysoXQmxq3oNbaezzkzx9ffnugSJp0MPJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=kC6G5jHPdTWIAAHcomh-KClPDSdb5G0sxPZE3NawBwlFOY7PEUwIAqVYSzGa7x0NbjqxU_W5C9f6PggYomIITHz09kWZrqhJs6kMx0Fi7oAy_3eYMEd2qQT7FLJt9jpfPRIc0FQ2R6lUQSuK81fZJHwwV9dwdEUFKtLfIK7xOpNlImN8L2LfDNRXcf7eIYWuLSpg3Oh6Wv9Kfds_BHa_LSIAy_pt_uwMtKPJaZfKQWiUMGpUzgR7IePRiIimAgZ6_O72C8Jf8vyq3Q-9wuSba57KSxQysqwurGo2ZD9PJhCiSL862YfQJysoXQmxq3oNbaezzkzx9ffnugSJp0MPJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
پل استراتژیک که شیراز را به بندرعباس متصل میکرد و مسیر اصلی حمل و نقل مرکز کشور به بندرعباس بود، مورد حمله آمریکا قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100560" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100559">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/100559" target="_blank">📅 23:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100558">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100558" target="_blank">📅 23:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100557">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kouHaaLcN5VPMoIfu7PlsOJtCnsxhgtel3rAq30x_pnjrcuKj0tMgRJqAQ3tnerVQWH4awD5fZdr3JzjfNZhv0OJA4S53PERkp7zMsKN-SZFO05fuvo0qYJVBsvWNfep1gy_h0s-M5TFNp_ZIuiYPkpVWR_jjAmycAPRhM7aGsP8j3cveXY7x0hYCAuvpkRhGBaoJ3kcQs4fsTRI5e_f2IRWE4mGkPSVMjzMOXuarMqHMc9sCeA9KNMHVZXrA8URa3jlkLNA9z5x6PXhPw6L0y34FSGa9MKQrFtOMMyITF67B5lB3-2nx2c4e6RZdbrQnMFBwV6YOcxszaZTi8xqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گزارش برگ ریزون RMC SPORT:
ویلیام سالیبا درحالی برای فرانسه 7 بازی انجام داد که دچار شکستگی در ناحیه کمر بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100557" target="_blank">📅 23:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100556">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyfnjCviw0ZZTc9mD6mUPT1T_NIJ-Fx5MB6zYCu4CbvjlyQzTJ-okvJXrttH81ncwN9SlOFneteAYLDw6HaKc996VhrZe43wk1UBs30VFJNego9lH5ic9pppVzDtULJUsx9TNOfLpEJiypfwKP2BLpi2D3rZ5ehgdQAwcKacSsv1NsHH2mSxLwWivJB3bKNjlv2L9q-WcM5GuWK-5eWTNarDQ2uOEWCSqG2Lkfjeyp7jQM_XQy2ymmht78L19hiX2nA0AoxL5XbF1ZRantF6KymUsoqieYBT2xWHjYqXQvf-UCQEvy9n0OevQ2rlvJYeltOAbk25ZiJ7XLqnOtemCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🎙
انریکه سرایزو، رئیس باشگاه اتلتیکو مادرید:
خوان لاپورتا از قبل میداند که خولیان آلوارز در فصل آینده در کدام تیم بازی خواهد کرد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100556" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100555">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=trFcvpXnQqVvx3E4MgGNUys6SCZArV0cyeYHjhsx298jTA1s6a87SBBrZ1Cec-1lZ6V-MVxF4tHl8SZi-1EDEJr_8HdRihSJaqIQUy1jCgs4Ibs2OptkTydPd9EXb4hj5zSsmZ0t5yNT018bDkCQ8llFBLLux5aYRSGy4nzBQXUitRr9Up_YEq8S7udztOcgSxs37RrbYhvwXlgP4UfSSWAcHQWotBa34dDvCgJudyM9Ig0b6dIyE2X5k3ZpjToe_bNwWM2RfkCjBqTWfBLN5l4MoFMXNji2ImKR5SZN7ZveCYfWwgqQEAUSf3qDEXp8me8n5i1_JM5E1PS-bpvzOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=trFcvpXnQqVvx3E4MgGNUys6SCZArV0cyeYHjhsx298jTA1s6a87SBBrZ1Cec-1lZ6V-MVxF4tHl8SZi-1EDEJr_8HdRihSJaqIQUy1jCgs4Ibs2OptkTydPd9EXb4hj5zSsmZ0t5yNT018bDkCQ8llFBLLux5aYRSGy4nzBQXUitRr9Up_YEq8S7udztOcgSxs37RrbYhvwXlgP4UfSSWAcHQWotBa34dDvCgJudyM9Ig0b6dIyE2X5k3ZpjToe_bNwWM2RfkCjBqTWfBLN5l4MoFMXNji2ImKR5SZN7ZveCYfWwgqQEAUSf3qDEXp8me8n5i1_JM5E1PS-bpvzOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی و یامال تو فینال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100555" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100554">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBwJ1MEjZYhqhfcVp8PuNAHGJR1dEyEAyRZxSwFPISdROtDhYUUg4aOo_8xn_5Qjh8ub_Wsq9GqSm7S9ik2royYQsKELF2ZuXBClW2qDijDxK2kQUfqZqBkZ8MrKM2WIXRRR6zZnQXeF1YSTDO3OaL-nDCHM8XU2nyC0IC9URy4DNTFvU-fWfLGuDBQ0Skztk3tbSf4Cmg7d_SEu_FDpT8B86vGRUCSF3WIfeYvjUJQy_UNw7RyuSt7E_Rppj_P_vh7PPnwlzYrOiOAI6kQ8HTuc7I9X6Mm-PE9T9QHtw8wEThiMpAugD21FzvZ6JyCxdS00VImTmHKn4ubXA53PIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
برترین گلزنان تاریخ تیم ملی آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100554" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100552">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVjippR3xz38UbuX-HiFI2rh4NKtpKZesiaUAqyi_Mo-HpmWiAU1Py6jnM-R5D_K6_PXT789eAVHRERnPOSZ5odtLVGhMQR7DSgBT550NIcsBNcpfuf0bjw--wR4lJD2OTD17r_kw0vTrr_lBxY7dm-ZPWltl9ti6cNxwXeS5_uAlgp_-JgJ3hGKvPJzmgLZqeLNUuCzD9DeDNH26oSGXTIQPsvMAP0nCfmdw8IYiygBNXWt5L_PTuEzYM6NeXh22OFhMBVBtecFJwbs20i5zszahXqNKudkwb-MkcjVmYV6sE13pVsEspYZCdEi37tmo2D11M8GciSrSQsbEOsEUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IISK3AL1vEq_m3ynI2TJez0RAJ8GbYevJZDp1O7D1vcEuA-4vC_nAgRKdJL9EyKK7y07Qk63IJPVKEBbJrx5QQX35oR0E9b26zt6xyKNdQZaUS5KKiPxQvywuDdYEQpliWXjzQbfppBLQe0pF1hRGPrpZC6v5tzrR-b-OAGAQpy-IxulnusEiWyr7vFnMHGW68ECxijoxWyqpeUubVw6VleA4Trm1lXDsmhHdjj3vw67EBkkFnHcn3sGZNdiEgx8wFi1WxM7bOTtteWK5es6tJFLv05vvxF3R8CjLqTHMbO0opo5OTMTh0XQY6r8ayXqi8YBNFP2gvjOHkQpXkhqKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تنها 2 بازیکن در جام جهانی 2026 بیش از 20 دریبل موفق ثبت کردن:
🔺
25 : لیونل مسی
🔺
22 : لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100552" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100551">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFNHHt71RmAla-b2kc7o5AS3dpsGvuy2VD63ls3u60P0FsWcnDnjEB-C9_q_F7WcsXVx351Z8xyFiL4ceDPL2JJw9EjaNA6py0s8WGBWeYCvZdPumPA-UvmcOgCGAWFr8VxRAbMdRiUy9220fXhej84nb2Uvz4iTcJnQhQxtQHbQjbJuS5RQxL34lv1ieYZxrVPpw-mt6KKeAnSMCW3XAScq_DlmF6IGI03LCQzzp6FKkKtwk_mGXOTjTlg0E-Ok3VzGUJ2EB96YMZIAyNTp5laEg7UErr3KtdC_CwY3wPJQHmmy0L5QQnNykSikGciVwd3EnZdFRtp3qZ8pFRI-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100551" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100550">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiJtO1h75nygjkaV1UCPBgnuWJqtRrcyymghxC0xGHmD0O0lX9R-VbfnVONbj90noCStYHwi8BWQ1mhhWR-wjckiM5ZtprGk3rKxZTpXx_DVlGhCAUrkHtF1uToZ0Qr4gap4fNiOwFxobye-8b0LRHDGp8zX-_nTMjslMiS0EIjDVnT1NVsTS7RCnQBtffjE76S_stZakf97XDPKN9RTw15Bxcm7Wv18JxY2fwFNSZSQ218wSbcDmabQTpFv6pCNgHLpXk2CfrFrBTZTcfCmHkYNFTlwGjMIADEbVphSqDsSWSKyPoovFc5Qkhf1nwslXzrMSc4cWAtRAzDPR0xnUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
فابیان رویز با پاری‌سن‌ژرمن برای تمدید ۲ ساله قراردادش به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/100550" target="_blank">📅 22:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100549">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGj5895lr25rK21mjYXds9LkYOuWuF05-c9COGBllDyfLif_X4jjWj5djHXFCyWs6Py0Bk3Yw-NthZYz-_yY1BIGGXp7z08oEvw1bw3FHacKqRSuXDUvegliTiRpBzoziUOEMZF-nqxsej6t2zxe4go-Q4e2gBcIlyCucMXh31iPdvt-8zuggj9ecdvv0a988FGY93vzDT4DZbjOnxrXNsWA62eCbvtWhdS7KHeqqCQIYsF0FwqOoOvk86b_L53MpQHiT8FmwGYDrEmBdg3VehjaKOnZ0QGnMry6_-cqTcbiZg0NYkWVtrp2n-PyXelgdap9a5tRhzzUj2QOhUixzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام: حملات ما به جنوب ایران شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/100549" target="_blank">📅 21:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100544">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQTiNbsGaK1joQfnMcGhtNUMnhKyDkEnlM35PEtcRE1DmJjMaMTg3krf87S05S8bRJj0Pe82BiKMWkvUTHg3vbbyVuPqpAsI2AbyvBez3YEYFDRxN2smAjEOu02PPrMgtvhP7SkCuOBVt73BuOvQ2P4e5lTzyOJfSoZCIghJ7GZdg3nJreJkU10xPsUEEehSUC9lui9CliNhrjgSXCXousX8SxouVX0vXKX5h9yiOG8CsqImhC2W0X5J7wsgBy-ODxlK6oGRA8qtN0LLNBvjgr5omBAB77KmtDU7QXFRRNEODYq_PyMGIHqPsr3MZ1QVa_jU8YWy8PfVcmge0xJ7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SYYyOpwxqmD9XmOTvfcO8PibB_iBhR4n65Hes1ewXmry7vxvEsitZrr_Au5-h4PO1_esnJR1Tr3NE68pjj7ZU92X3F8RVg5NuvL-6Hdw6W0qEHQunkOYYWX-dfA5GcarPjFu5RG4nfz_sS8kGT5nWHtDyShYJzq7pZag2r4cpgSMHkNvI7_fZGyzBEexJ9YepXzAT362UjnHT2EpNhMk5soDn4OAUDq3PNXysq9R5wgs0fKjjKfABtqRDLSjx6hAMz0B9Ui6IfPTe4nyJLyWu3PzfqKJYuqMdkSpNk4dEPUJxWYE4CNgoctuBGIAnUrvqi8uTgGvvUeolCZha_32pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZG1GpIP5yNp1ViB_UOUca9RwUMlexvOHP3d7gv1BUmXAWAfcLnVBT5r3Y2Lzk8HnidaMmmXbt8GMaWALB9L2suZTnPw37-9j19OAAkbI4nJtkQ3uLpuc3k4zaagCR0UmabPeqFrFQ8BKVkkjzuaPW6gketIbefre_-3c11BS-sA6WwB7VNhzNQUM17mUz0TscRhyqYkLKSa6fAuSMhfbAgC9kIsyjt-CZdKPbzzSxRCZ51C0U9qGQFiRU57NbN3yNj6T7t0Su5KEmgngAfJZi4WFAjZY8RWqxaxcGnq4ByLJss7h9kvn4My8DqkQPYzpAsRgbRvVX5i5Zv0d2SNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KOgaJ9-WJHw1AlOTuvQoGMcj7YLvw3vy0fC7ectqr7xiEaDsJukNYeIjeYHdhoN3vO7K-QL_woI3DsTpjF58FbbMs-goWTB1Rto9PaiWsmpj5aHxtdAoGJw9FMZcbWXzxbquD4mvy1uYgX7vcvaiPjGBt_NJZEKljzsEREdZ6amJvCkdkAVOUk9d4j9ysl5eK6dU_9jxYPqtk21h5IBKU0p_4sJNM6BMzFvTRDj25hqR4yN66wh9NAspxgj7CiryuxvtAzjIUVRphMlOHuVMmjPMgFVRqyYdV8D8p8fmmDBNXEMHwPU2wdtk82fnDDKnCroZIwHcRtM266oWZDXtig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7z1zp3UeMxFLufHIowzoRHOKuzJsnCM91oHWC4DCUVVffPBSGx7wm-g6TP2e87roqt9ns0ZYgtLn2t_tztJXWjx08B6UP4l0k4w_T1UlgL1mCeoYXRknrVa0H45H1COEQYAK3YSAiqKjQ-cxH_2bS2QAkWjiexLlFKjN285tMElOHwhcjSqnfXopV5YBQpI7YXePJnLSWGNXb8pjeQQFDEULTPOE6B9NqJCL4NUpmvXHHBDSqJhpSiPC8xrJdTt0rcEFgcmPo6U0dQ1WzZidiwUxddehYP9vmXQ7Vhqr8vAYgDmTK4jPAnQ6qA2AF4U7pBd4H6TvjMvF3M299DCCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدر و پسران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100544" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100543">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWqP7m8JtSBTujbpXqgJxB8-r50fS364jV2jg1Al2qqjusGGFpHRhkEpK7O7B13MCRMO7f6pZz-k2vwUDxaBlZyp11MAa06y2d4EorHIi4pd5uu4cerlD5k9hKt7-bVXreaU2aCMW6-XoUmUR1tiiO6H687-NhkurbIf0axaxQS3U7-v0ANT7sQhTBIYZPbXXPxeZCASLJfDSpyXNIh-lpV6mxR2E4Z7N1l30a3rAfz2JU4bBgqFNMjSLbCtwvHK3Z7cZuzKpbOaU5JGgkJN5dqTmbrBv7D_nQo4VlmIi0QvovMZdLCGPNZLeAFIn9GFkLLkihDYxqAMmP_Q15KlNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
اولین بازی‌های زین‌الدین زیدان به عنوان سرمربی تیم ملی فرانسه:
😀
ترکیه
🆚
🇫🇷
فرانسه — ۲۵ سپتامبر ۲۰۲۶
😀
بلژیک
🆚
🇫🇷
فرانسه — ۲۸ سپتامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇮🇹
ایتالیا — ۲ اکتبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇧🇪
بلژیک — ۵ اکتبر ۲۰۲۶
🇮🇹
ایتالیا
🆚
🇫🇷
فرانسه — ۱۲ نوامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇹🇷
ترکیه — ۱۵ نوامبر ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/100543" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100542">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTVW_ptTYArGisGTfecCaCx-ZrFhwOLM84ZDabMyt0FXG40xkl7MJBIhhS5U-8icRZ0cBuDYe9lJww_ZMlIj2eyGfaMBM-1AXX83WF1LsMUPDVl8oQqFnpnAGtQLbi3rz_rYJ2awqwYl0lt5TIK0KjOEHjvbvG1bqZdOEK06eKQHy7G2WQYRqX_EwAtteei0DMA-T-lBeE-NRXrF5EHGG9xEm13BgV-S1_8zCjv0pzIk4tQ3CaqW5nek3k9xtrcr_doO7a07E1wvzawhxx5oZqtq6tdjgtoS7qck9mxHNEvQ5X3vputsQ5mowUI7Ed6-uIzOBzro4BwB8oc5uVw1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خبرنگار: چه تیمی قهرمان جام جهانی خواهد شد؟
🎙
گواردیولا: بنظرم آرژانتین قهرمان جام جهانی میشه چون حضور مسی در بالاترین سطح آمادگی، یک مزیت بزرگ برای اونا به حساب میاد؛ مسی همه چیز رو تغییر میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/100542" target="_blank">📅 21:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100541">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=DBjs-n6yIBclHkYiY1CUDbu_8Qs86q_6pl7g15lhj7Y3nobZ6qNfL6vHS4To05ykohr4Lca0npo7rmoyEbmn54YOUlGj9v0lQPXeWRL4ZhzY4m36kXXg4vWweNBveLnzY3s_uTqfYRIg8CWXfK7EVkvzr8JObLcOejoAnNcYKYHH6SDgarrnqQiKU0Yh2KW8pXuUupt4Yd9XYU6OwqyjTZlEuA0fuOItUovaIy-WtMlaSJA9hF7FYrwiWmg34Pg78asfbTdXoinRX1GqAU-gB4CCr7coxBq_TTKewfYO6mr-JX9admGsJGYAJTMroF4o7pSqGYcgUPTlT8gE_nlRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=DBjs-n6yIBclHkYiY1CUDbu_8Qs86q_6pl7g15lhj7Y3nobZ6qNfL6vHS4To05ykohr4Lca0npo7rmoyEbmn54YOUlGj9v0lQPXeWRL4ZhzY4m36kXXg4vWweNBveLnzY3s_uTqfYRIg8CWXfK7EVkvzr8JObLcOejoAnNcYKYHH6SDgarrnqQiKU0Yh2KW8pXuUupt4Yd9XYU6OwqyjTZlEuA0fuOItUovaIy-WtMlaSJA9hF7FYrwiWmg34Pg78asfbTdXoinRX1GqAU-gB4CCr7coxBq_TTKewfYO6mr-JX9admGsJGYAJTMroF4o7pSqGYcgUPTlT8gE_nlRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد شریف روزگار
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/100541" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100540">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا رایگان میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی  @FutballFuckBet…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/100540" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100539">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avc2TuMfX7i_Om908cklYHbQHZGv5ZHhHDbOjHQadZKRVNmWXIgzTYcct3-3OOykarCf-KhtYo43BkihZPGVkuyefekumrDcmIMVjSDA4iV2Ev-TOX7vuaqyJaaa2VvNbXUICSYI0DUt8Iz1h7rpvffyeveAV0uAMhQsqrZz909xpWkboqrixVKMgD0kkdZLHS8PIB-Bbhgq_mTOvenjy8d5-zo_uFdYT7HxZW2VIo3vJ8nI5ZVNkLkD4w8AWj3hC063_Fyfds5F_rpowHlP9xAJ10IN71SDy_MXPYOyBF811rqdUR4esgDmfaipysNydunhQ99h_OxWamkti26DaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا
رایگان
میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100539" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100538">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkJCsgwdyG5f-Y-ZbHn9HU9-yX0l7nF3ccSxco2jxH633mu8fiEIyh6a5LgL0JBRIhrQkVm-tHhVQzTDjNM8IiX2RGKisLoNYQEQbyhMdCG7aB8-hbgE7H1CNYVtCFJqubuwJ4qPLQDbc5ZM3e06eFHXKhgMoNSSBpey0jW8EDqGgFjAl6-aYPBDXuMvp7aIRmgCQ3YTjUxviCDlztdSZzohLuY9KwcQHHGnzkrYiCCHZn6Ww-hohssdl83dG2e0M_6vcfY-mAHer0e-R71X8-ykiHCz-Fguyrrhhd-vENDbrdMonqP6iT1iZRaJEzvYg50B0k6KZjQBNv19A6jASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇩🇪
#فوری
از اسکای‌اسپورت: اولیسه به بایرن‌مونیخ اطلاع داده که در این باشگاه قراره بمونه به رئال‌مادرید نمیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/100538" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100537">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CudcaN-6GvW1Botd5lOg7X888ZJxfL7WL2maOA9g7jrY0rUIHMS_poGOlV3Uqbamocupg_Kwez5Z2w3KbVSpOTJxoHe5rtG-Lt41hisUDh6_nNqs1O_XrWamfxx2IVtahuRqu_jHdwWXuSomXetIZ06JXaw24tjDZ38aGRsd7gx31Ko6V_GO2DBDhiAruVznnD9DawrNX1Km7KYX40ppAI_jH7eK7H6_RNDDUCPjyYx0_8cbWyk7K89G8FJS1UTAMBX0Ex1KELxAOMFmvrdYaTWe9Ko2a_pSAigax8pwjlv3teIXFGAZFvoLCD0uHPpht1T9hUUtGROhg2lxDHlvQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/100537" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100536">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🏆
🇺🇸
سخنگوی کاخ‌سفید: دونالد ترامپ در فینال جام‌جهانی حضور دارد و به تیم قهرمان کاپ را اهدا می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100536" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100535">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378abba176.mp4?token=fQTRQHmSGt7pTsLLsQuQcdClPKtHbB_lg01aG3sYk5nHVUdeoy-vi93TOuOsobrRaM3oeexCTzp7J-1Rr2CNg3JCX64JvK_jDyrYrANWouEXt6XrEFK4rD0Sz1jfvDCJ7NOjCYb9pdMMz8VSQqVp3WeYDColDieywm2B3Q3fQA_AZd-X2M81mqsjhFjF8iu9ywVmWznsoTzxeBwOgOcYIF2T33QPnpiCIOQRcJu3UnkZYLbW4tC9B2lt9YY_5uoZwmmcgMcY9N2meQY2iIL2bddwgAvGAAeRZBPPjaOz-w4wUEtAPgB90uYGpau313udsYzYHsf3b5_EvCU4AzHBYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378abba176.mp4?token=fQTRQHmSGt7pTsLLsQuQcdClPKtHbB_lg01aG3sYk5nHVUdeoy-vi93TOuOsobrRaM3oeexCTzp7J-1Rr2CNg3JCX64JvK_jDyrYrANWouEXt6XrEFK4rD0Sz1jfvDCJ7NOjCYb9pdMMz8VSQqVp3WeYDColDieywm2B3Q3fQA_AZd-X2M81mqsjhFjF8iu9ywVmWznsoTzxeBwOgOcYIF2T33QPnpiCIOQRcJu3UnkZYLbW4tC9B2lt9YY_5uoZwmmcgMcY9N2meQY2iIL2bddwgAvGAAeRZBPPjaOz-w4wUEtAPgB90uYGpau313udsYzYHsf3b5_EvCU4AzHBYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
فنونی زاده خطاب به جهانبخش: اگر تو ایران بودی یه تیم دسته چهارمی دنبالت میومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/100535" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100534">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=oKRM__4feNIwo7uJ3RLNz3QSYPy-sPJYGbzagpBU0R9-fBzp6cKqCWe8KrRL7fY6I_PNAJbCrl5_e5hVcFJwxsEN0T6MPTxGBRBxrYzlCRXaDDS07oIvrGKZl2b7CKUEeaT7B2cnY2tBSvMuWb1fvgHLYsr2pyJnFkn5_zLVn8WwgQ3O79n8kK9L4SL_F89CM486bsnX-x53RTQQbHr1xZE0Pf6F0MStvgH-gW7L-Kpwm0waHs6sfxAeLnfQMUJOQwOSvrFMJjMCaztS74YwHQwYzEoR0UwknQ2x6WRzyUHwUEjrC519pJkWPMQEfAhGiwc6cfsPI3Vyt5vhAxWceg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=oKRM__4feNIwo7uJ3RLNz3QSYPy-sPJYGbzagpBU0R9-fBzp6cKqCWe8KrRL7fY6I_PNAJbCrl5_e5hVcFJwxsEN0T6MPTxGBRBxrYzlCRXaDDS07oIvrGKZl2b7CKUEeaT7B2cnY2tBSvMuWb1fvgHLYsr2pyJnFkn5_zLVn8WwgQ3O79n8kK9L4SL_F89CM486bsnX-x53RTQQbHr1xZE0Pf6F0MStvgH-gW7L-Kpwm0waHs6sfxAeLnfQMUJOQwOSvrFMJjMCaztS74YwHQwYzEoR0UwknQ2x6WRzyUHwUEjrC519pJkWPMQEfAhGiwc6cfsPI3Vyt5vhAxWceg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
حضور تیم‌هایی از قاره‌های آمریکا جنوبی و اروپا، احتمال قضاوت علیرضا فغانی را در فینال افزایش می‌دهد؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/100534" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100533">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChVirtynu9SG24l__Ou31zwn9rKO6wmb2LEEYZzW15glAvOS-d7gl3Cs0nMRqWou84-U6uHhMpUaxBtHaepKJOljoLkaeg_Cj0D616fR7m83jPg5mD10MgtQgyxvLWDJ2P8i5si0iyjppMtP_IGzVsEpQw5yhOhCM8TwUy16gKyt0eM10Ej91QP6c_abLYuDqwys1hI0FjLSDI5kOWhISOF8kztBPNlXg2Sd6j6LTtCeTNoziKNKLsANAUPvfWxjPXZa-Vgt6_7pxn2HcDWQBfM0hXtFv8lbF-77aTzkTVx_DxT0fst-WRMYevvcUKVfmwvoUBLaQnr_7ENLmooTWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/100533" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100532">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735694936e.mp4?token=px0rgKq1lyIfm8E1_QcHlJ57_ykxWk6teAK4_GUnRjwyKYf5WXDTjqXIxpDSnBSVxQo4jRDtuYxN1JrxEoEWNHXPgQTVpZVD6Cv5nF-OioFKY6kmArZ3e3-jBk6rzQzl5DNzp06Vh8GqOhhRycwCYqfNr19gVMu1bJA8OfWiQ2d0Xx5FJXdWplCoJCb1vOv69bdHNzocdr7jq96w-Ub5KPG03xO18_qf6bC4-w0LqnQLkmFm7J4GXMWxvmh_qjg_Os9g-Xb77VoGPEJI5pMsHiUvMHqWzH9SSckCz1RC9bU9R3SyYEJXRX1xLu2azzoRjDj1iMvCiWoRtCe5v33aAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735694936e.mp4?token=px0rgKq1lyIfm8E1_QcHlJ57_ykxWk6teAK4_GUnRjwyKYf5WXDTjqXIxpDSnBSVxQo4jRDtuYxN1JrxEoEWNHXPgQTVpZVD6Cv5nF-OioFKY6kmArZ3e3-jBk6rzQzl5DNzp06Vh8GqOhhRycwCYqfNr19gVMu1bJA8OfWiQ2d0Xx5FJXdWplCoJCb1vOv69bdHNzocdr7jq96w-Ub5KPG03xO18_qf6bC4-w0LqnQLkmFm7J4GXMWxvmh_qjg_Os9g-Xb77VoGPEJI5pMsHiUvMHqWzH9SSckCz1RC9bU9R3SyYEJXRX1xLu2azzoRjDj1iMvCiWoRtCe5v33aAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی وقته دنیا یه خوشحالی از ته دل مثل این صحنه به ما ایرانیا بدهکاره..
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/100532" target="_blank">📅 21:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100531">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BKsxqecPzWq0ff2ISlxm217bMDD-N1Stu7KHDK1Ibd10PQMExUbj6opnP5CR0RNrrKxPRg3ffRhy7XVPhW4tlqCk-wqkXc0DuoJXh5hAxa5prufg11ScX59DxLUIwoOQtKH5E8KZ7AECPqL8z0vgDU4YSWi0FlLFjZBhJ5H5jPbCGsHf2KNT5x8Mzr5V_Wz-NQrDolwVN_tHZpuHfPYzT2SD1c9WjZHEAWInmPf68ECLrTsGxg3NKq4kuD3fmHxay4AeBrnXqAQYO7B2iE6Xr2rubFtlgzyQcfnBT3pEemdA-RdEptkteDQXIiMQ13H8xdEPN-hrGcH3aLbliadz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔴
کریستوس تزولیس از کلوب بروژ با مبلغ ۴۰ میلیون یورو به آرسنال پیوست.
𝙃𝙀𝙍𝙀𝙀𝙀𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100531" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100530">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6JDy3hkKY_gwM3i0OYMLca4mHZabkJJLcTNsCEzyyxyZwHXwEbAea3fZeymR40TN_Ov7mfzZxAAaFkkUp-I9vFayLLMqngBRN2gHrwM8zpo5cjehjSpaJGCDtqUTqtJRSRCPM4yYC98dm3o6gBk1dt1CZLjJ1Yx4KimNmo-0wDX_NqIzqchgZ0CQo7pM1ZF4-a84vDdzGtHcDNQSJniETUJeWJqOhHmipe-GA-hEbZV8IYAHKm2kwayHCvaKXOiDRCifDZJl0-sFJE5e9TK3OgywkMXmh3zjAY4_cb9wGAaaplb8iCWuBJzpm4ursNHJPswDMxoF5Le1UuTaUvmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
لیتان، رئیس باشگاه لیل:
🔻
ایوب بوعدی باید برای یک فصل دیگر در تیم بماند چون باشگاه لیل در لیگ قهرمانان اروپا شرکت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100530" target="_blank">📅 20:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100529">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">لیگ ملت‌های والیبال
ایران
3⃣
➖
2⃣
آلمان
🇮🇷
25|26|18|25|15
🇩🇪
22|28|25|20|12
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100529" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100528">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=pd3PeXtxeIF7g2Xaul2SfGynMMFuWx-t9OQf36PwmzW287PGZ8ktS35oFf4KR_klOSLVtmUIB_9A5U-tCWbGhjplPmCtORi53FZktUiHPRAsG2KeMV6g8s00E8tYZJuoGnw-m-q5t3zUGTN9UVsPCTDKaWRn7tQi70ZIackf_HVzhoo4g8-R0S7Ipcacf7a6iyZIzZwLQlhvaj-NPbhwFAhZV6XCESb84EDiPFq77gSCCR6zniWxttakADxh70LpzaQsEeGMlgoz-w1FIW7tXSnU9sHePgbbPgB08Ohiowi0GeieKHiCJRi_kjnKHC6vu8Z-9kC_tSvsYAvaEjqiJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=pd3PeXtxeIF7g2Xaul2SfGynMMFuWx-t9OQf36PwmzW287PGZ8ktS35oFf4KR_klOSLVtmUIB_9A5U-tCWbGhjplPmCtORi53FZktUiHPRAsG2KeMV6g8s00E8tYZJuoGnw-m-q5t3zUGTN9UVsPCTDKaWRn7tQi70ZIackf_HVzhoo4g8-R0S7Ipcacf7a6iyZIzZwLQlhvaj-NPbhwFAhZV6XCESb84EDiPFq77gSCCR6zniWxttakADxh70LpzaQsEeGMlgoz-w1FIW7tXSnU9sHePgbbPgB08Ohiowi0GeieKHiCJRi_kjnKHC6vu8Z-9kC_tSvsYAvaEjqiJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگام، درباره بحث با مسی:
هیچ مشکلی نبود فقط داشتیم درباره صحنه خطا صحبت میکردیم، خیلی شلوغش کردن! بازی کردن جلوی مسی واقعا افتخاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100528" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100527">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW0TXqvaWIK7YD1EQJhR2QNUN7eZhbkSEV9Rdj1HNyhSIrM7CYlBRI-maesoXh73Eqk4FLn5DVvTGWHMZNtHI__RTopQiRUv7egFHRY5lCRgEHMIjcn6FYvcurAtJbF6g6w5q2DpYJQ2sh1D7EIRFK1FwoaqJ7SdvxLC4YaE8EgG9n3NDgcKQMkqKf5EGke-Hd8frGMeGIKhdH1lA5LdIR4v_drEyOAJZRNsTuS9m7ur71Vq72SSvbPrgm5qjPdJBTu8tIZPRRDYpJU8drVMj0RM5tN2UrIk7ECm-LY7F_ASc5gY4GvS1I-lLSDdbNrul9X7OOWEdV_z04sAA9KurYkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW0TXqvaWIK7YD1EQJhR2QNUN7eZhbkSEV9Rdj1HNyhSIrM7CYlBRI-maesoXh73Eqk4FLn5DVvTGWHMZNtHI__RTopQiRUv7egFHRY5lCRgEHMIjcn6FYvcurAtJbF6g6w5q2DpYJQ2sh1D7EIRFK1FwoaqJ7SdvxLC4YaE8EgG9n3NDgcKQMkqKf5EGke-Hd8frGMeGIKhdH1lA5LdIR4v_drEyOAJZRNsTuS9m7ur71Vq72SSvbPrgm5qjPdJBTu8tIZPRRDYpJU8drVMj0RM5tN2UrIk7ECm-LY7F_ASc5gY4GvS1I-lLSDdbNrul9X7OOWEdV_z04sAA9KurYkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی دایی: «ما شکست خوردیم، به چیزی که می‌خواستیم نرسیدیم.»
کریم باقری: «همه طلبکارانه صحبت می‌کنند، در حالی که هیچ دستاوردی نداشتند.»
عادل فردوسی‌پور: «چرا باید برایشان مجسمه بسازند؟ چرا باید درباره استقبال از تیم ملی، واقعیت را وارونه نشان بدهیم؟ ما هیچ دستاوردی نداشتیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100527" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100526">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFQjvSx_g1kJY5aSN5MLaeHM1SvxQL7Ztwg8LLqvdMJ--hSwL4VC11kaXWrkyQHpJyOYH27nOKVfEPieaRv1FDydqqPK42qHm8sKgvRFn0X2UI8Qjr1qzaoFeUIIlzU8PNswI-S_Ho69E_Pwuflr8k6Tz-uIXkfiI1T6ijb9YK5Rq0NZsK808X5i0R9XJ4CqXGpZ76CeLzVXEsniHihBFNK5IR9kCwC9z_thrTlB7c-JW2CXjDZkV_VyJjnFqW4KHtf4Rg0-UxNPs0XY0BZibzkYMqKEgdDadMxNGAkpI8lu7MbsKRMCHvHNLObx7smbduOzb2-3ExCpaDiBSkCvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">�
جدیدترین پیش‌بینی Polymarket برای قهرمان جام جهانی ۲۰۲۶
بعد از برد ارژانتين در برابر انگلستان
🇪🇸
اسپانیا:
۵۸.۱٪
🇦🇷
آرژانتین:
۴۱.۹٪
حالا نوبت توئه؛ از داده‌های بازار ایده بگیر و پیش‌بینی خودت رو در
Betegram
ثبت کن.
🎁
۱۰۰٪ بونوس رایگان اولین واریز
⚡
واریز و برداشت سریع
🏆
بهترین ضرایب بازار
👇
همین حالا ثبت‌نام کن:
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/100526" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100525">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zetqpj2MR3DFGKyQ_rhFtzPdwvWiIs2B8e_FGOBCcZdK8qOH7BeoAarjjQk8qWCOKj2ROEix5SUxwHcSZFnQY_tiKnGxz7SYrDfWpNgbc-_nkxuh29gt_q4CziAWiiBkePDPyOzJuuhXicAxgUC4JgOR7ni0f-taUL-rJNYMxKl5qHKycWv5Ng9hF4ztmaeEcIX8FBY7lcuouOJjixh58eI47_0xSaSZy1fIZxe6RU9REWD6Svj3inSGGneXiiPYfp3K8C5uZBFjjaKeg-Lkvw-bFefy96q9jwZOA4aEAiuCsK9dGCrzAJhpJkPs79XPokWFFc0Fs3lorox8-HUjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عشقتون تو تمرین امروز تیم ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100525" target="_blank">📅 20:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100524">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=D64OC4vwH0sevomgTLlRf6y2Bi8QTrzMEzosdNdDOe3kwp3v1FJzX6ogCJnSIVSQuYXWDraQT7zbCiAmoH8V1UMMJrg2Hnvqs1n4ickiqeQ6FylqFB7NAv69_-jveOXRjGMe4DWtR_NnhRIijLIcb1_nBid1JR_10s8zumGJzmjRz-DmF-r33YjNELq1qcMUdntigz0YeOe5eXldEmCcTI-CiG_Gzhen2DvMkZxTlFzQLe6USmYqQzSIe8sxzPZERL1kfS1oxX3eZ09hCX-f5SGq6c16Yl1Kb1Uj11mb9Srz0bLrqJO47eO-AsMN0bY6d4y0LxhU1kke9zdV0acmtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=D64OC4vwH0sevomgTLlRf6y2Bi8QTrzMEzosdNdDOe3kwp3v1FJzX6ogCJnSIVSQuYXWDraQT7zbCiAmoH8V1UMMJrg2Hnvqs1n4ickiqeQ6FylqFB7NAv69_-jveOXRjGMe4DWtR_NnhRIijLIcb1_nBid1JR_10s8zumGJzmjRz-DmF-r33YjNELq1qcMUdntigz0YeOe5eXldEmCcTI-CiG_Gzhen2DvMkZxTlFzQLe6USmYqQzSIe8sxzPZERL1kfS1oxX3eZ09hCX-f5SGq6c16Yl1Kb1Uj11mb9Srz0bLrqJO47eO-AsMN0bY6d4y0LxhU1kke9zdV0acmtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
❌
لامین یامال در تمرین گروهی اسپانیا حاضر نشده و روی ران پای چپش بانداژ دیده می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100524" target="_blank">📅 20:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100523">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGA6hZxMJ4gCXPIX2Dw1YD1cxz2BauKCxbAM13joTc-ghNzNP-5nEYDVIXjH5XDq7Sq16rZwra4jtuvWuZQ2xrnjl4AKJ83uvBZm7xRkx1gWbO5FwVVECgETpQ9eeDAZ9EoOhbvdvswN0_5MWhowfJseyuLOGKh9vCzyrLDskD0HUrHh6w9KEvPOFSS-kdh_TADhTLReacJKwpOppDDZMeGC4tkybuGJax7H8qyHnLow4r3NUnmYWNU4hlMxGifR7RT9ZwfGJtHhYWEHc2XxcHdgmr4StvkY4yJjCzw97I-pwCOwWCma8ri3-XcwGLENOeQsnbd-OMDYMMaiHUVZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
#فوووووری
– گل
:
رتبه‌بندی ۵ بازیکن برتر برای توپ طلا تا به امروز:
1 - هری کین.
2 - اسطوره مسی.
3 - لامین یامال.
4 - مایکل اولیسه.
5 - کیلیان امباپه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100523" target="_blank">📅 20:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100522">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2tZE_riwWByK8TkFDsLh5cEj1j83F86eJHwg01kla4BlGucp8JECexYkoYGOK6uoW1OT6RiZUDJ7wEfRKYA-TLVzWC5nNqwoSyzOvgoY_MuGNB3p_PqYs5PRCk1pxbFw59c5MjZvAsFZ8ICuR_O2HJbYnX45Z3rH_ybmzqxqDr0v8kmPL-J_LUIqc17C9AlnqQMTuhAZleC1ldC0h-v4Mi-7tmUKHuzUBiKtCqTmwuuMDQvFModH0wJTtT8QojpaNO2zxR0NSHcAUSHzX8gaSa9eYStXFknWU_07wm8Ol-Ap3nwLBQg1yMUO1QUgUeDFfqhq_QWthjASSW1mcFaMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📊
🏆
| مقایسه آمار لیونل مسی در جام جهانی 2026 و 2022
غیرقابل توقف
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100522" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100521">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=doxBXeMA0J_JYJQBW--vrggDjle1Tw6iuDorJ6btCo1GMllyWI6_VLAu6ZjOoQoRWZU1s_X0HFLvLk2X2zoAAzSMktlWvnx66n6lFEQ9ciOk9GJFkklvklAjXyVw5CrH5jN228VrOzVLplB4cfN0s3b0GXutamao3bpXp_AL3lBD5jw_gpi24ddLWZiKw6iulZ3Hy3UFqs0O8Q_9hGdbdntH-GdXNIypMfVS3Mkjb8zgP8_3ud0vjTA988cpcj1So-90XfaZC0Sox9I96SMX-BKmb592YCW_pHpl1plswunfw6rxpW7cdrGW2ZB20X4J1xY7p9gR0QrN6d6um83vMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=doxBXeMA0J_JYJQBW--vrggDjle1Tw6iuDorJ6btCo1GMllyWI6_VLAu6ZjOoQoRWZU1s_X0HFLvLk2X2zoAAzSMktlWvnx66n6lFEQ9ciOk9GJFkklvklAjXyVw5CrH5jN228VrOzVLplB4cfN0s3b0GXutamao3bpXp_AL3lBD5jw_gpi24ddLWZiKw6iulZ3Hy3UFqs0O8Q_9hGdbdntH-GdXNIypMfVS3Mkjb8zgP8_3ud0vjTA988cpcj1So-90XfaZC0Sox9I96SMX-BKmb592YCW_pHpl1plswunfw6rxpW7cdrGW2ZB20X4J1xY7p9gR0QrN6d6um83vMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
کل‌کل بامزه دیشب عادل فردوسی‌پور و علی‌آقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100521" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100520">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtXtGya4m1eMWt0GAKhKJYQIqtTjJCdnjmuF9PAXDaXqQ_HIenKJz0RhQXBkaamdZlVIAVyI5vCHf54pZBKt9dXjq0DX27FcsSiVjJvnPFp0mHgxTnkM9jq-fx8EXAZizSYefPoar278oBxd_k-xPyJiz3yNH_MrRvYkiBSgIHYUDEGAethYv-ChfiyWc7V2ohBFy1xMYWg9J4K-pqumKZSOI4g8jham-OLXOZ5nL6y5CUDbwf68EHL09lQXs8YfXfaAXQIJqPULtoevafEP2ISScOvNoNJxIbuIyO2pKFlu_-BnaVbk1GLn2Gdse3tx5n90eVD2yL3O6_AzTZUkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابرگاس و خانواده قبل بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100520" target="_blank">📅 19:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100519">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tikfnqILYDG7_iRclgxXy_MEk2HHsyxpH-XVNPnO_l2Ui074tG0sq_o3yc5X3WCFLE0vitIW1s4uXxrnhnwm3JNJMzVNMglxKfg55MOfU7VV2rUXBS9PfXodY-hvXgXCk9RxjDvIajwTiecHHZfnJhZGSao_BklEbR4oYWgGQyteilWuqxuxhwCAnvw2nJl3jTOjJDKNBcigUS4DwfjOZiKKjFew1n4Vqu51C1fbPkCo0iRG8bOfk0301I6TjCm8BgANvK-DrA-Zik8JHkAt6iBTUtohGOIogWYlLTUfjoZuhDIsBPNvOqZyWB-2iBiNovi0TIe9FpWQHiXXc_hqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت اول آتالانتا برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100519" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100518">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcY61zCUdEp_9q9CrvIjhIsvEpNq30XUNdII92UOTnJG7iXmOQG2Pf4935clwtbvkxGyx0utwTUwpf6I5xTUFxJQZVtzZOZ2o8-tlzluogdgET1pCn6QH8orw1KRR3QfW4Yhf3L5NMoz3vPNW-Nvpe-730voD-xDtKp2F-0CEAHEoKjnDIHvrgPINDPbH8vWKQ9cJllmawoEdfSurDgv0DOYgUDwXWrV8p9A0KXmW79k0TLKvtfpa1ptJCSq0WsBMLJLl6hUW0tq_qRbZywCBijTFoWg_O6qaTjXoTkFo7PnwMEr7pp3JXS4NqGT_cn4bu9iUDk5pePhwZKLlS16Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100518" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100517">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tfxpm_m-gN3F4BXnqx4gyR1r92cZqKIeH154NwPBJcCquIUfBbKAdwd5VWeWnjep_sTQjbWxxcBKtLNKm3o1yz7iSmQ-n9cCxa1p6mU7d0ug_6IBrCahw4QgVkgGG7wAPdnIr8kFMzPSekrluXWzzNufLQ4_kwFQCP3LUapM7PtyBxebaoEaY7jElmcQPkWIkbkJ09PhhDxZRxi5yji_OAhS01CYcKkILmUSUxGW92XMGjDeonZxX84TTh06uC7XzYFBXjQ152owmqsNZRwSCD6geDNpc2JLYqeCQAyxJZPcZrKIH1hHMd3Ks-Ub6Qz-gN5UEW6Hm0NKd8GVxAs45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
استوری رامین‌رضاییان که بنظر شاهد جدایی این بازیکن از استقلال خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100517" target="_blank">📅 19:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100516">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhpMX2EmACN7MZ_wcp72EkPM2Hlz6lWjg3VS7xYGxnn4W_qXiDU23jHXMBN60VExTOIeBvpcURe6IbeAgSazTLeNrq2gEM-IrQ-PUFBwRnIo47aLdp70D5vukHahRitOHGzECOqZQDbVfqAlUmvpx9z485a_qQ6ZegTfOpFeKMMroXjLsFOmRaSHck8JGClSxYdBL_K3PNU27pTBvdhzGZKBaOqPRTH1pyI5l93xQovqIJfB05ogSeL5gQyH5YddVakpigLs_0tM-UtiTATbOC1co7t3d9pM9ZEe256vZneoerAuADg67TM89I0pRB4ODJIeryruUSyFVIZOtfb2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زین الدین زیدان برای یک انقلاب بزرگ در تیم ملی فرانسه آماده میشود.
زیدان قصد دارد یک کادر فنی بزرگ تشکیل دهد که ممکن است شامل بیش از 25 نفر باشد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100516" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100515">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=A05RuR6LYP0SXD7v1Sy3hyXCqZiH47WbS5Q8Q1mHZJUrrKwr10BAY--ZoHjsEf3PMASrL3lHCexNY8SJMy905UVnKjSEUYRPeRrDpRju55yeOVRSKUXu1e5NwwdyyZN_SvbXhU6VyODymRW18AYt-QH1gjOtHqASH488BpOMtRtkgBNeQTcU7H6K41Lvq7i6S_-UpcfkZn8mmSMqh4GtUuqJIfr-QZuZ6tj2izJsYPQe6J-LyMwm4_KfrFIMSHLPcK4a0GVLiwUT9otUh99rlhWStMFoMYWUQuveInVI78HhjmxtpEc6RQ2naRxwMstA57AoXSFJh54mwS74RCbKfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=A05RuR6LYP0SXD7v1Sy3hyXCqZiH47WbS5Q8Q1mHZJUrrKwr10BAY--ZoHjsEf3PMASrL3lHCexNY8SJMy905UVnKjSEUYRPeRrDpRju55yeOVRSKUXu1e5NwwdyyZN_SvbXhU6VyODymRW18AYt-QH1gjOtHqASH488BpOMtRtkgBNeQTcU7H6K41Lvq7i6S_-UpcfkZn8mmSMqh4GtUuqJIfr-QZuZ6tj2izJsYPQe6J-LyMwm4_KfrFIMSHLPcK4a0GVLiwUT9otUh99rlhWStMFoMYWUQuveInVI78HhjmxtpEc6RQ2naRxwMstA57AoXSFJh54mwS74RCbKfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«قاب رو ببینید... علی دایی و کریم باقری... خیلی سنگینه!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100515" target="_blank">📅 19:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100514">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6P8D88h1e_ywTuh4UbXQl0IfKxaOV3ICgNj9HZMNa6vUrtLgEvcWrA-4XKjikI95cSbIOI3UxhEo130W9H7sCxIHj1sS0nkabkVPi-XLWDYx4gwxLt6I0H_phj0YYP1w9mdgYgdy00oUeMbBg4Th1Gf6LvyQGciFGdEm1YIuFf1UcdBulm1GcMHEzv1X08i6epvFD8i7oOfIQnr0Edjony9FrCacSx0F9vMeEyKqupitevpO3xQMk_2JIjfhoFucUpiSJiqCveP4xFM5YM4TBuG5hahgVx2OGBl2SVcNRM859sg3d-0iKhXGSFWIaAL0PRMBuU65LZKgIoihoyMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمعی از هواداران فرانسوی، طوماری را برای درخواست برگزاری مجدد مسابقه بین فرانسه و اسپانیا منتشر کردند. این اقدام در اعتراض به پنالتی‌ای است که به نفع لامین یامال گرفته شد، به این دلیل که ادعا شده بود قبل از ضربه، دست او به توپ برخورد کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100514" target="_blank">📅 18:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100513">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121dde0263.mp4?token=SQ8_rWfQxEy_AK2o_Gzt9OUyZsVnQQN8-pZ2-Kj0xETT9KB_NV798nlUR5E34Zr5zx8JWlbmxX-To6I06BRkw2bpbhI0NAUfQc5QARuDbT3j1YA-ea6h_CwNmKYZuH1oZy8NOeWqyFKeEMO560HC6U_kgvHYOn1CrBPLNR3STOwndTFovDxbo6cnGdSopM3X6ZOmjs89nFpeXQpBVWsVht4asZITsUdd9HjV3nMpRUbUuHj8SuXyDbGf4HVg-omYTF2dzHTrbCOymP8dHudCzgBh6O2_gA36TxhL6UHElEO5ZMZpGg787bZT3syeYOIu1z3kEs7G-tKfqThNqxI7Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121dde0263.mp4?token=SQ8_rWfQxEy_AK2o_Gzt9OUyZsVnQQN8-pZ2-Kj0xETT9KB_NV798nlUR5E34Zr5zx8JWlbmxX-To6I06BRkw2bpbhI0NAUfQc5QARuDbT3j1YA-ea6h_CwNmKYZuH1oZy8NOeWqyFKeEMO560HC6U_kgvHYOn1CrBPLNR3STOwndTFovDxbo6cnGdSopM3X6ZOmjs89nFpeXQpBVWsVht4asZITsUdd9HjV3nMpRUbUuHj8SuXyDbGf4HVg-omYTF2dzHTrbCOymP8dHudCzgBh6O2_gA36TxhL6UHElEO5ZMZpGg787bZT3syeYOIu1z3kEs7G-tKfqThNqxI7Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
تفریحات کارگردان استادیوم‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100513" target="_blank">📅 18:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100512">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=n64Lu5fU7W98iSy5z29WnOJZLCRvJ8R_vRV52iJ6wSFgy05KOns6Mv3XCyTrxEl73F25qNCCsQE1oIuTwMtaP-EQRiIs7n69OA0FvspwZ3IBFafEMuTTWNStlhx0H89GFT7XeEx7rGrrjTxToEJ0RNripAGqpumrNezPM4rhPgJFiAoEE2uYuFWG4aoct0N3CcR_OFm7Tl5Y5y4o7YirTdo-lMdlj0bEizsv0wBnpbwaPEAwkBGyqcNp-j1x9KQqWbaBrQRQyzPYSZ2wzj2QzDA5LSdNlKMGdQSle1Fbwl3HneAGx5Fco0D-f3k4rH-_DUkcGcjL19h4sqy1JQ60DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=n64Lu5fU7W98iSy5z29WnOJZLCRvJ8R_vRV52iJ6wSFgy05KOns6Mv3XCyTrxEl73F25qNCCsQE1oIuTwMtaP-EQRiIs7n69OA0FvspwZ3IBFafEMuTTWNStlhx0H89GFT7XeEx7rGrrjTxToEJ0RNripAGqpumrNezPM4rhPgJFiAoEE2uYuFWG4aoct0N3CcR_OFm7Tl5Y5y4o7YirTdo-lMdlj0bEizsv0wBnpbwaPEAwkBGyqcNp-j1x9KQqWbaBrQRQyzPYSZ2wzj2QzDA5LSdNlKMGdQSle1Fbwl3HneAGx5Fco0D-f3k4rH-_DUkcGcjL19h4sqy1JQ60DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتخارات ایرانی‌ها تموم شدنی نیست :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100512" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100511">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f049197c85.mp4?token=dAqnQlXE0hPwDs1L-CGP2GdfmQ81lVY9bEzblqgYwIk2yT5hlqc69rbiLfmRqT4hARAwiCkHmm7cNg5pvh49BFEZIEPWHn2Cl4fz_ekc2PcpMJRwRBq2fnLjfGge457L2iM04LUWZ88oYhTkbRgpUcwPoPntYvlB_ffYoyJyAJUzpfC7Yuhk1sHlSQqYxo9ap0hjfSXyBN9zvWYNcehzzJK_Klu-fsvRBkIfeFVt7tLnG3bLRt6eOAKqsC750NTiZYmH4lcbazLQRB1fxY-jY8kf19vSkGXWxtZXPPOcrCrZVeEzBLw8TogOUjyCByGi7X_kllAfj7Ed-I_ZhYW6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f049197c85.mp4?token=dAqnQlXE0hPwDs1L-CGP2GdfmQ81lVY9bEzblqgYwIk2yT5hlqc69rbiLfmRqT4hARAwiCkHmm7cNg5pvh49BFEZIEPWHn2Cl4fz_ekc2PcpMJRwRBq2fnLjfGge457L2iM04LUWZ88oYhTkbRgpUcwPoPntYvlB_ffYoyJyAJUzpfC7Yuhk1sHlSQqYxo9ap0hjfSXyBN9zvWYNcehzzJK_Klu-fsvRBkIfeFVt7tLnG3bLRt6eOAKqsC750NTiZYmH4lcbazLQRB1fxY-jY8kf19vSkGXWxtZXPPOcrCrZVeEzBLw8TogOUjyCByGi7X_kllAfj7Ed-I_ZhYW6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتینی‌های دوست داشتنی خوشحال از پیروزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100511" target="_blank">📅 18:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100510">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4981bd9a51.mp4?token=ivLfOVrcbr81fbhXNHLsjB-qhYhiAGvmoMG9I1nqNuZf4P0_br2Zo68aPhYvk_jf16XP_H8cWOoMTIMG5NFoIV5Zg_8_Um6MCkgnqLhJpB24eDNjv2rIuPGllRqFM3fU8BGmMx8AvjoO0ZKJSFCkg6vWQ7-KlEAo5d0Zkb1adWMLt8lJLXrFJqfBDtuOH7xb7pMIq0hUOpKqhohQoiO1zt-S8QZMG-zLAjF7eMZeX-cyiWsMECjsISJ8zi879bMjH86k1D57k9X_O98lolfLHYlBVORxy7fy8pNhJ1RvMmr2x2uop4JVvj-7ggmHbwzs2av6Py_zNMNJqvhpVQGuiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4981bd9a51.mp4?token=ivLfOVrcbr81fbhXNHLsjB-qhYhiAGvmoMG9I1nqNuZf4P0_br2Zo68aPhYvk_jf16XP_H8cWOoMTIMG5NFoIV5Zg_8_Um6MCkgnqLhJpB24eDNjv2rIuPGllRqFM3fU8BGmMx8AvjoO0ZKJSFCkg6vWQ7-KlEAo5d0Zkb1adWMLt8lJLXrFJqfBDtuOH7xb7pMIq0hUOpKqhohQoiO1zt-S8QZMG-zLAjF7eMZeX-cyiWsMECjsISJ8zi879bMjH86k1D57k9X_O98lolfLHYlBVORxy7fy8pNhJ1RvMmr2x2uop4JVvj-7ggmHbwzs2av6Py_zNMNJqvhpVQGuiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از کجا به کجا رسیدیم واقعا...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100510" target="_blank">📅 18:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100509">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62564cea43.mp4?token=LFmNLIIS_elPTDB2KFC7ypwNrVoFSfGvNxxplEX_AgZAjECpLT4EjDjBrAvEhjOJ7qXj0rvRk81MoRJi7uHGIdRJ_ndQle3ROFSvD6upIrEpf0IpwQFSTcaBq73BXHEdL4S2SEhE_JfQ8uFhnlw4kaLzVExQbTWxjSVAFgvUM7WPZujQt9VwFegaw5fnZdl2_2Epo9JZtAyx_c374sWq5TrSYppGLO51Pyk1IoZ2XbzghLB3D3iHXlPA_q-6b0tbeuNxeUbEEEYmIHqjL5l6ZDWFYSi3VNmfd9__KKYziL_NAVuYwBfHIrVaY3ER6RfDn28fuJiElaY5rkrmy1O4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62564cea43.mp4?token=LFmNLIIS_elPTDB2KFC7ypwNrVoFSfGvNxxplEX_AgZAjECpLT4EjDjBrAvEhjOJ7qXj0rvRk81MoRJi7uHGIdRJ_ndQle3ROFSvD6upIrEpf0IpwQFSTcaBq73BXHEdL4S2SEhE_JfQ8uFhnlw4kaLzVExQbTWxjSVAFgvUM7WPZujQt9VwFegaw5fnZdl2_2Epo9JZtAyx_c374sWq5TrSYppGLO51Pyk1IoZ2XbzghLB3D3iHXlPA_q-6b0tbeuNxeUbEEEYmIHqjL5l6ZDWFYSi3VNmfd9__KKYziL_NAVuYwBfHIrVaY3ER6RfDn28fuJiElaY5rkrmy1O4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو چندسال پیش گفت: ما تو الکلاسیکو مسی رو خیلی عصبانی نمی‌کردیم چون در این صورت عملکردش خیلی بهتر میشد و دیگه نمیتونستیم جلوشو بگیریم! درسی که جود بلینگام یاد نگرفت و باعث درخشش مسی شد!
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100509" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100508">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2241a88830.mp4?token=I9sHxJTluC9VQ0yGqm5Ee-HPIBZDOiwEb3IfHAMj95ZLWuHRwyolXuvonv4h53haW9LkqWH0Q8O3hZCsYd7zjUK9B2ymyAhJeg33L0HtBOtrwu3nH9yp38elGTmZkmt4864VNj2xcCVh3XuBwdxNidu1EeL5MdXaGf7tr9Wbt3nLyq5B3IiJ1gjDtFtP7hkj9SprKeSP139gQWhESQz2eCE3YMplNnnErnVIBmHaZRPVQfDdKsHBMnOJXGQXlVI_8P37omegtMdMfTUi6di8w2_CFTnYTL373ebOIOEPDThD1bTOe7i7QecUonF3wSRJ6h9GQvKfgruTHzCNqGMOjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2241a88830.mp4?token=I9sHxJTluC9VQ0yGqm5Ee-HPIBZDOiwEb3IfHAMj95ZLWuHRwyolXuvonv4h53haW9LkqWH0Q8O3hZCsYd7zjUK9B2ymyAhJeg33L0HtBOtrwu3nH9yp38elGTmZkmt4864VNj2xcCVh3XuBwdxNidu1EeL5MdXaGf7tr9Wbt3nLyq5B3IiJ1gjDtFtP7hkj9SprKeSP139gQWhESQz2eCE3YMplNnnErnVIBmHaZRPVQfDdKsHBMnOJXGQXlVI_8P37omegtMdMfTUi6di8w2_CFTnYTL373ebOIOEPDThD1bTOe7i7QecUonF3wSRJ6h9GQvKfgruTHzCNqGMOjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش عادل فردوسی‌پور در تلفظ نام وریا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100508" target="_blank">📅 17:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100507">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=pxZIHZ-mNIUdC9RWnEBbhyrkeEOW3O5FWovH_uTSNB68RXPEfAcQD8YcVpWgn85ycllsGkHO2-arpa9oFo7ASvGtkRlaS5t4J7OQ1pL-V2JhY4Ma80mZ7lZuRvWwWfDk15jgmkxgensxYyCaQKd0sXvZiKbOi1Omq87vrrfpmaFaA9NVqYayUYrufZXX8kRCfB8HmiZb68dzzAwuZALyNr25XqccQKOXf901aTYQ6_8c55qydoctW5AT5sisV_TJDrpOjDtNgF6MoRBGADDnvdU0eTYI070tdhWG9DN7gfwvDRJOQbY6uXhWoNHBqCoO4YmCB_YRBX6CgMhlMuIb95PVNI_piIiW9VkD8SRxgds02jxH3weCaumr9s8aE5x3NDS0IyuY1JNeVjmYAUPHjPRGo2mUa59gdR7_Set7TDgYIYaJuTVtynf6Kv4Bcx5C3CyMe2Ceh4AVtmBpvMSi2oL90u49k8X6v9ZzceT-1tpq1PUcMMj83xlDyXYCK84syTz5_Lz3fZ_z8g765RMFmLwksDhrsqNBTRnkG4Me3AJCuH1fK4-5gj-P1rd-98yoxUZovLZyRshDbGFAK9NrpXnH-3Nr3k7HG9AWDl0iJ6FQ6Fy-TN_hZkb2hbuaRy7VF5ruzI0jN2TiKxwn3vK4JSDxN9C8Yu-zuJcps_mK9vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=pxZIHZ-mNIUdC9RWnEBbhyrkeEOW3O5FWovH_uTSNB68RXPEfAcQD8YcVpWgn85ycllsGkHO2-arpa9oFo7ASvGtkRlaS5t4J7OQ1pL-V2JhY4Ma80mZ7lZuRvWwWfDk15jgmkxgensxYyCaQKd0sXvZiKbOi1Omq87vrrfpmaFaA9NVqYayUYrufZXX8kRCfB8HmiZb68dzzAwuZALyNr25XqccQKOXf901aTYQ6_8c55qydoctW5AT5sisV_TJDrpOjDtNgF6MoRBGADDnvdU0eTYI070tdhWG9DN7gfwvDRJOQbY6uXhWoNHBqCoO4YmCB_YRBX6CgMhlMuIb95PVNI_piIiW9VkD8SRxgds02jxH3weCaumr9s8aE5x3NDS0IyuY1JNeVjmYAUPHjPRGo2mUa59gdR7_Set7TDgYIYaJuTVtynf6Kv4Bcx5C3CyMe2Ceh4AVtmBpvMSi2oL90u49k8X6v9ZzceT-1tpq1PUcMMj83xlDyXYCK84syTz5_Lz3fZ_z8g765RMFmLwksDhrsqNBTRnkG4Me3AJCuH1fK4-5gj-P1rd-98yoxUZovLZyRshDbGFAK9NrpXnH-3Nr3k7HG9AWDl0iJ6FQ6Fy-TN_hZkb2hbuaRy7VF5ruzI0jN2TiKxwn3vK4JSDxN9C8Yu-zuJcps_mK9vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپید:
دستم به دامنت یامال، تو رو به هرچی قبول داری قسمت میدم آرژانتین رو ببر و نذار مسی دوباره قهرمان جام جهانی بشه! اگه اون دوباره قهرمان بشه ما هوادارای رونالدو دیگه اصن چی داریم که بگیم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100507" target="_blank">📅 17:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100506">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I66BdoEzW2YZ8RXjTCZ1O8LIhTJ9cPlqcvIN49gv8ldUBDhWA4ZMe71jvzEBj3GJuBnZ-6W1dsrjFofNFvOsTgBW4a6vzCAfkkU0N5TKjbpbDjWeUJCq5lEw7zRhgyBsIr9qrqEFDwfWMNrasPat4AhpRm_ZO077Sfw-NuBgnc0FVxeJ17QzwxjNcD-m-VPMQzS6XNUkZVWbvj0fEtMc59_JSJBXId1bE_sRLaBpkNsk6i8V0qB5iQ2__XXQ_AnbQWxF5A5OtaVO9Dl5TkauTgA84GtXZGC968V4yfXAKhkI6Mi5-0GVfihxxjQNr-sZkwppIr0BPgQcjPbC_hhjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رامون آلواز:
رئال مادرید واسه فروش کاماوینگا مبلغ 80 میلیون یورو تعیین کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100506" target="_blank">📅 17:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100505">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=TM8xcd59G0l0GRF3ZvklTaWQJrNlCAh89WFcTdAGslMys9OCnULhrNYW6317PwbhgHu2VBf6dU2p4a75lIl_ZBQkDZovCXFrgssPKHOQbVxNtM7y54j9eK4njHch9Z-_jV39gNiKzN4wG4R9AU_B7PkNjo-xxeTctOtDkqc8nQkSWjX91K8Aw5vVxIGblKNPO57bzQmT1BjdHZS44ZBIOyWEFSBKaG44mKD76P3z4HswBxCRz_7AZaPWf-svPAyyPpcHjl62eIoNOAP0f8aTTh4oaJkrMFy2EkrpMGUkGaRLqHAD8oPiOYHYrvGCJGP3Z6SRCXhxiGSl0jCWRguPRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=TM8xcd59G0l0GRF3ZvklTaWQJrNlCAh89WFcTdAGslMys9OCnULhrNYW6317PwbhgHu2VBf6dU2p4a75lIl_ZBQkDZovCXFrgssPKHOQbVxNtM7y54j9eK4njHch9Z-_jV39gNiKzN4wG4R9AU_B7PkNjo-xxeTctOtDkqc8nQkSWjX91K8Aw5vVxIGblKNPO57bzQmT1BjdHZS44ZBIOyWEFSBKaG44mKD76P3z4HswBxCRz_7AZaPWf-svPAyyPpcHjl62eIoNOAP0f8aTTh4oaJkrMFy2EkrpMGUkGaRLqHAD8oPiOYHYrvGCJGP3Z6SRCXhxiGSl0jCWRguPRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
تصور کنید توی اوج هیجان و استرس فینال جام جهانی بین آرژانتین و اسپانیا؛ نتیجه بازی 2-2 مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه، همون لحظه بیژن مرتضوی وسط زمین:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100505" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100504">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=jV2zgK2wwcTK42g4a5U3wW6CQipQwVlDLykM1I7yWRPhL8emvHFDS2vui00IPWgZbetvf4VORWKt51CcjV4mujL_0gjs7hUNm68QWO_7n4EkozlyBffrDvzXNyMgTKgRu0dOg3ndjCz3ram7H-GTiHnejGtbAiBgSpYEwsppft32p8LeyKgDyemxl_8cEX7DFqtQa04fX-AoNEQFrg1O6W5YS9aIRITLFImgR4-9_KDsiYgOUwgCdo7Fr60ZFwzy-rsZDVqQQFh1Y0Vd0nHbYE6GSCXEII_PHk2PMG8u1GlbAzVVibyvOtmLKbTu6MWxeKiRQ-a3L9vM-1uQJf-0pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=jV2zgK2wwcTK42g4a5U3wW6CQipQwVlDLykM1I7yWRPhL8emvHFDS2vui00IPWgZbetvf4VORWKt51CcjV4mujL_0gjs7hUNm68QWO_7n4EkozlyBffrDvzXNyMgTKgRu0dOg3ndjCz3ram7H-GTiHnejGtbAiBgSpYEwsppft32p8LeyKgDyemxl_8cEX7DFqtQa04fX-AoNEQFrg1O6W5YS9aIRITLFImgR4-9_KDsiYgOUwgCdo7Fr60ZFwzy-rsZDVqQQFh1Y0Vd0nHbYE6GSCXEII_PHk2PMG8u1GlbAzVVibyvOtmLKbTu6MWxeKiRQ-a3L9vM-1uQJf-0pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه مخ‌زدن در استادیوم‌های جام‌جهانی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100504" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100502">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=GPZbvyZAmuHH-FVaZCgABhjgsZwwPbCJ0F7-HQMai7ZxlcW9u7Bwsv4fqOcvLljES5SdO47BRJ7D5erGfFWVPf_YSMOi82pIQlJCtt_xmMa-eZWZmt3z6TBawQxCctDm-Dav0zvo0QY5PZv4k10FT0o0ze-K5UDND0Xe7qK4hDEsqVwGYrxnSsVyrILGfvuvVGw_ymQM7Tm0ECUv5t4QE2oUyt0oWBjzKBZiSdpJ4zgv1dWP39yChaz3TFc_WQ2zn3Hs3iExxSulwfEby-raicH6KBrbpowKDmE91u7PHwlIdD1gSfupQIE4PmlQINvnYL8FE4qvzXCHhnsllJ1cWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=GPZbvyZAmuHH-FVaZCgABhjgsZwwPbCJ0F7-HQMai7ZxlcW9u7Bwsv4fqOcvLljES5SdO47BRJ7D5erGfFWVPf_YSMOi82pIQlJCtt_xmMa-eZWZmt3z6TBawQxCctDm-Dav0zvo0QY5PZv4k10FT0o0ze-K5UDND0Xe7qK4hDEsqVwGYrxnSsVyrILGfvuvVGw_ymQM7Tm0ECUv5t4QE2oUyt0oWBjzKBZiSdpJ4zgv1dWP39yChaz3TFc_WQ2zn3Hs3iExxSulwfEby-raicH6KBrbpowKDmE91u7PHwlIdD1gSfupQIE4PmlQINvnYL8FE4qvzXCHhnsllJ1cWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
قیاسی: رگ گردن میذارم که هالند لره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100502" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100500">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlPUFoZLOGzXhPfEgL911uGYR2kTNrz72fM2LrXh1HjUuwYawbya9Zy3cwu3TqU4yQyw1hrrD_Vb6fIYhy0NgQSo92nw5G3tOImIVKzgTL1q8d9YibYKZ7iyd1VVrkN-FEquz9KHcLBhhFCLFwWajM2vIRCRMEfFB3H8Z3rfYZ_yVHwlxbvf2ypDWD-E2jqr9FBTW6auJcQKGGqLPep1mpQoUq35Qv6bMJuHP4IDkiAb-zqJCnYRb3pIm3TStVE5NBng40ATBrMtTL4Qh8fWIngqcroZdAY0P3F9N7jg974sCkcoPU1IcdutWk4MQPuD50L_kk683B-3lr8DvpfIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjdxMLENzI4O0fhRmfxr1yqc55TiNIuofMXYUMRYGUg5eDyr4sosI5587Nioitl8XayOeZ87y62bul-64byDT_M_Xnwjk2pFgwwEpKUFAVTuxbgOS1F3jjhGEahObx1EtDe8cKiP1bGpCzKsHrrITBunDwvEythFLXbDZbFHTbnmJzaILCCePEPV5ui2Y5HnnVvewMyX60mad5h_BRRrKmsJBSWCVITSEfEP2dogG1yzc8pjOXv_V6TkWAO0nOw5prK4xwB3FU8-X6ANV7QtcCe3hKEJPBtgqL-6UFDR65WDIS9KE5A85kK0YHOnFRXLgXfXcL1CXLVTnvSDUaGQEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مینی تقابلی که قراره روی سکوها بین داداش یامال و پسر انزو فرناندز داشته باشیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100500" target="_blank">📅 16:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100499">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvD1o_L6-OC_3pt6tiNxH32dSMxcW83AjIz9HFTn1qeu1bxq6B3qDxy_4pa2WQ2-GlaYtrWhCMF47Xn_7ZklF4OAIXIt8rCA1Xb7DcGlIoHobzrGTpP546ufW9Q2TUoKz9hMogq23I4UxwrXX7PNBBkzd9dWqf-XZDr43e1lLbmre45fAD3JEfkxA-Gx5wsHUDjXKgQvM12ZsZ8B9sKnaTKhQYnGgSrbCeMaamuW43an8l3yfTtGUDynDidX0Y5-s0ELsVnIAYEe1bC5asW7tbciavaq1-OeZBrOIqVQk5XB37UEgSCQcBaPRaGGGCfu-RxQOR2jfQQk7yXN8mZzXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
الکسیس مک آلیستر بازیکنی است که بیشترین بازی را در تاریخ جام جهانی بدون باخت انجام داده است
11 برد، 2 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100499" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100498">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp_uc4FKUrtVfYdkD_FErVUhq9k2ZwAp-3aquxdoqtoOTIvyB6La0IBjPG1nAyK5Pe384mpHluK_yBbpRo1ZYNiP6H5TIabDs_-D6_ts2zUN_4shWQF1VFeyu5d1kbHueGutR77sVwLCXyPoUn9bBu21aAhzgBEpg0cFOmEahYWzWpmWVF-TMwSKyOvz-vH7Cyp-m0DZD8Kp_FV4Kk9qm3dRCIZjWZSUq3ZEo44ZzfE2kQy0K09NT4I2RsbWAua0XoUgmBM6wPwutJ1GBVn_7LDixHJtSsp0zpkaVOC6AIY3CrcXRLQ5VChNGmNtfVdQ5nfr_O0_RIYyo0eYv4RNsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: سوبوسلای مجارستانی با لیورپول برای تمدید قرارداد تا ۲۰۳۱ به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100498" target="_blank">📅 16:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100497">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=rpyqOBkqBbZQUyhuKr6x61ajl6L8yOM4e_0-URpd9zKOKF7c3w2yzfp-Fa3GLwER1UGxKdiv8zt_BnlsiM4tHy-OhGDYpvwwA586Nxh2dXPa1E8pvIF4D6p5t0Yj6PrLTyHr5-ioNkSc7XToNFLl0fHw1NliK6Jyi7SsKoiBX7yZN3klHbNNwS6jfRC9EI0M_epsCpIJNibkvOymqnTcPC47RFaOLTFNu0FiXpMSxlo0_eCCAS3A_7muFZwj8oyiA6jOmWg6xxmRRzYHXNHuhFOQ-fQSqJX7E_x9zOmyycU2FGttNdKtxzhJB9aNzXgHMuOcTf83DEuRtU16BAC3HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=rpyqOBkqBbZQUyhuKr6x61ajl6L8yOM4e_0-URpd9zKOKF7c3w2yzfp-Fa3GLwER1UGxKdiv8zt_BnlsiM4tHy-OhGDYpvwwA586Nxh2dXPa1E8pvIF4D6p5t0Yj6PrLTyHr5-ioNkSc7XToNFLl0fHw1NliK6Jyi7SsKoiBX7yZN3klHbNNwS6jfRC9EI0M_epsCpIJNibkvOymqnTcPC47RFaOLTFNu0FiXpMSxlo0_eCCAS3A_7muFZwj8oyiA6jOmWg6xxmRRzYHXNHuhFOQ-fQSqJX7E_x9zOmyycU2FGttNdKtxzhJB9aNzXgHMuOcTf83DEuRtU16BAC3HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جام که نشد ایشالا جام‌جهانی بعدی بانو
🎈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100497" target="_blank">📅 16:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100496">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=ohHhGpLhRd1kUMi8nrUc_e5srOkKHqV8K7HPoFFXBwMEcmgiL4JclB8pX-cbOsvjAv92cnvOz-kKu4Immga0kzaUjh6PsBWo6V-CGuS6qgNmozcgvXi9A2lDtbN5FV5v6n6dGhZqyJchgWdn0Pnb6QlhzqkD9fuPj-ORrw_aRHkDwJ_tr2jLT76XKy6vCbsIfn-G5qpKYlhf-N_j2QQT9MJ7L1I1YbFBzcTLUcWxkY2P5gSxBjbkRfITAZX0KKAJkPUU9TNnkYfEXz0W_MoSHPjThsSWv2Qk20OAOpmhVwdJcjP19eS39A2LpqUjSzppRKXJm6JUfkE-d9baiEIr5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=ohHhGpLhRd1kUMi8nrUc_e5srOkKHqV8K7HPoFFXBwMEcmgiL4JclB8pX-cbOsvjAv92cnvOz-kKu4Immga0kzaUjh6PsBWo6V-CGuS6qgNmozcgvXi9A2lDtbN5FV5v6n6dGhZqyJchgWdn0Pnb6QlhzqkD9fuPj-ORrw_aRHkDwJ_tr2jLT76XKy6vCbsIfn-G5qpKYlhf-N_j2QQT9MJ7L1I1YbFBzcTLUcWxkY2P5gSxBjbkRfITAZX0KKAJkPUU9TNnkYfEXz0W_MoSHPjThsSWv2Qk20OAOpmhVwdJcjP19eS39A2LpqUjSzppRKXJm6JUfkE-d9baiEIr5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
علی‌آقا دایی که میگه بخاطر مسی آرژانتینی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100496" target="_blank">📅 16:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100495">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N92zQns_P9Ro-c8n1xGcyRTq7k6Eb6uxJ7jb9vdhnSaT8RrlgCAiFS36u0K3y1fkysM-evd5pj3MOGamQBZsP76g0AHdv3KP9laorkQ-HZZLLad-97O05RLl3dlZ0RseN72nEMHi0iCOxG9HE2TQte93FYYR2fSkllK96CYyaXXoQ2K3fBgd31ayntmwZs31fAEB3ojQA5g3tfUquFnW0M1YW3UJ1-ks8gFNUBvUTPUlS6H9GGVc8VHkjP5A6QvYE_uxI7Unpt167u5rqje3p8ylPDK6xwRlWa7-rVOU_qJSbdPY0RFLVNgsAn2ot_iJVVAc1PHzaNBYB4EPG4hTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دی پائول کنار مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100495" target="_blank">📅 16:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100494">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=eQ57VXgit-wRvLAm2YMwwnMJ14D4iKZSijWn--eO4rRQCeivBJh-_Y-Tkg6YdVhtPJq3rMiYk-Q2MfvRLUAhxa5h012W92JLaIWwektiS5uZJBNEFf3GJJbUdYkD7zh1EmqLYaaTotn_SJMllpv2WcfSGovWUa-EIAqnflUKhHx_y-EZ0DlIBgPiSOnH7apobCxz7sy3TivP2PAP082ZzJpqaJ0RguuycZYnkfFTNPGEi5iL051-_yS2EeMxcEj-2xKT5g4J_7uLNmlTB0k1DAf0NODnHGTxpxg2_LQ6_jbVqwm6X8UPCSe5Istxt-0zJEJ2sGfksTDS5QoMQBGARALOkjK3NQr2qpCHsWxU93cALvj8lQFKiHMImNagc2zgSk68gqHDrRbpOgBfAnu0XpkcKPFR2N2G7Mpt7TfVElDbUFmJhDdJl02_78PjadR4L2yirfKrx0Wxb98h0c23MN_Z2NsGHzYYN3k8CSEp5Gz6iQO2UhBRqk4mYvHKwUPOBrNPON5uvu4UqovDabZtSKRtfhdHEDiqmnwZhEZ3bxK_DayCVFvGueSOLf4QXkdA7nV78RdHTi_Sj_exBERPEiqvUaF_1EVCrtlD-4J-eNAgwjMV_bqlHkCcse97_lf2gcPUGP6qQxGQFUGCD0Id30nG0Xuhp5sFYBg7RmPD9Uk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=eQ57VXgit-wRvLAm2YMwwnMJ14D4iKZSijWn--eO4rRQCeivBJh-_Y-Tkg6YdVhtPJq3rMiYk-Q2MfvRLUAhxa5h012W92JLaIWwektiS5uZJBNEFf3GJJbUdYkD7zh1EmqLYaaTotn_SJMllpv2WcfSGovWUa-EIAqnflUKhHx_y-EZ0DlIBgPiSOnH7apobCxz7sy3TivP2PAP082ZzJpqaJ0RguuycZYnkfFTNPGEi5iL051-_yS2EeMxcEj-2xKT5g4J_7uLNmlTB0k1DAf0NODnHGTxpxg2_LQ6_jbVqwm6X8UPCSe5Istxt-0zJEJ2sGfksTDS5QoMQBGARALOkjK3NQr2qpCHsWxU93cALvj8lQFKiHMImNagc2zgSk68gqHDrRbpOgBfAnu0XpkcKPFR2N2G7Mpt7TfVElDbUFmJhDdJl02_78PjadR4L2yirfKrx0Wxb98h0c23MN_Z2NsGHzYYN3k8CSEp5Gz6iQO2UhBRqk4mYvHKwUPOBrNPON5uvu4UqovDabZtSKRtfhdHEDiqmnwZhEZ3bxK_DayCVFvGueSOLf4QXkdA7nV78RdHTi_Sj_exBERPEiqvUaF_1EVCrtlD-4J-eNAgwjMV_bqlHkCcse97_lf2gcPUGP6qQxGQFUGCD0Id30nG0Xuhp5sFYBg7RmPD9Uk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
تسلط کامل فیروز کریمی روی زبان انگلیسی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100494" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100493">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=t1FWbJIRMNIKXmvQWJHbL3ahZi2oULHrt-Xc859d8NVpuzFfq57ezIdp19ccSEbpSqDkQhFfQv_LzGqVyjZcXnTY71RAeGlspiqW9rVfGOvYWqIDm7unrXFazwfVJYlXhoAhGXq0SC-HMngM5XB7CCEdX83Bxs0B9iZ9nw9Qn4fiEV8oN4TyTcoQhETa3MCcs9TwW246chIQha9Al4NQalwEsPA3bjonlt9wNgicJTVIq1F5CNOHjJMGGnRnkLrMCJwoEzDeq9GfN5z5yybQ8ch6iYVMrYmccEtZB1XS460k2iqbAmI261zqQXQlgPymSkxQJSC25NFinbT8Oy6edA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=t1FWbJIRMNIKXmvQWJHbL3ahZi2oULHrt-Xc859d8NVpuzFfq57ezIdp19ccSEbpSqDkQhFfQv_LzGqVyjZcXnTY71RAeGlspiqW9rVfGOvYWqIDm7unrXFazwfVJYlXhoAhGXq0SC-HMngM5XB7CCEdX83Bxs0B9iZ9nw9Qn4fiEV8oN4TyTcoQhETa3MCcs9TwW246chIQha9Al4NQalwEsPA3bjonlt9wNgicJTVIq1F5CNOHjJMGGnRnkLrMCJwoEzDeq9GfN5z5yybQ8ch6iYVMrYmccEtZB1XS460k2iqbAmI261zqQXQlgPymSkxQJSC25NFinbT8Oy6edA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
آخر عاقبت گنده‌گوزی یه بچه‌سال برا اسطوره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100493" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100492">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=GHDFHtez44xda717vv1mT53nT_-umsRT3_nPQMff8uQEf0s1vCSAtOgo3LgijmGL2M8BD-B1Bk63teC64ml_TSjgN4zu4dXGObAtWvM-FBYEd6gfDzLjb9qNN4-Zl9mcgSLypwYdxPS3H-L8QL5zNmr0leiWfKxZPIJgYEbVG_sTZZaRI-9GRRtoXN1sDa2OWSURMIu9gBQwFcFjxCPn-jZ6DjJykbrhDfautQqt3K8_UylTbOycXINdNl7vZj37fIkaYdKxlK3MOiKbtZkOHl9ALt8UbGqS26niSHuEFP-7HJ7W66JIm2imXj0BDO97RonWhGxKv0m0eB61v88Sbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=GHDFHtez44xda717vv1mT53nT_-umsRT3_nPQMff8uQEf0s1vCSAtOgo3LgijmGL2M8BD-B1Bk63teC64ml_TSjgN4zu4dXGObAtWvM-FBYEd6gfDzLjb9qNN4-Zl9mcgSLypwYdxPS3H-L8QL5zNmr0leiWfKxZPIJgYEbVG_sTZZaRI-9GRRtoXN1sDa2OWSURMIu9gBQwFcFjxCPn-jZ6DjJykbrhDfautQqt3K8_UylTbOycXINdNl7vZj37fIkaYdKxlK3MOiKbtZkOHl9ALt8UbGqS26niSHuEFP-7HJ7W66JIm2imXj0BDO97RonWhGxKv0m0eB61v88Sbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای عمو ها اووعو اووعوو رو بخونید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100492" target="_blank">📅 15:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100491">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd1G_fIKc3AuegYTEV5r8-mWnNaXj7LF459qAWhs4Gf28UVTpjwMM3FjFNeN51CjTv_INvYJ1dDy2qmi1D8C_QCrxZziPdBSJarxhLwMdMzAJMom42rxKWRnzDM63RUauuZhpq5ENc7oonyKNsURU0tv_z49fp11sPqEC-KWZx0xsa02xnp7uYAthHJ9C4FXYB2OoKL_UbCPkEpA0uReqZbqAgiw8rveDRN65WS3z60B0mTPRFzCA_Rm8GEuzKh3a1MDrisu_zrWtx5sgHn4Kb2eXG3cNM7bS_XiGVMegNSzFbMQe_GxiIkEsdIaxUtbngvTUL_kXL-xW1SSSPW0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
🇦🇷
آرژانتین در مراحل حذفی جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100491" target="_blank">📅 15:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100490">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZdyhRScUn2A513_RPvtabk8iZmhrNZJJwOjrfu5r4qhJ3eZhZh7bP9tNYQF5sDBstCiDcN_1aN4Ho3CddsOi1vo_3ZNCuE1c55YWzlb1XRLbLHJMPxZ7e2amdLkNwgTpI5TUqxrPAiRWIis2P9q4AZv_q7N4XTkFArZstx6h8yodhnyj6pjbnkAoFy0NzhOOtbaKXviuFS10E5hRWUenwwaZi3iupICNavDcxaDx7mSxiVIRZXcKuIMqHevRcqk0mOZbKW8YyUw7nYlOxVuRBw13OxtamgbxxVRRc0CohqihkB867IUnm6yRm0lCVGkFxOxaHgqa8R_MeJOo_ldZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🏆
با صعود به فینال جام‌جهانی، آرژانتین با عبور از اسپانیا صدرنشین رنکینگ فیفا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100490" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100489">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYN5nsVCu8LBNJCHW5FzG-8cXpIVWAJEHtX20C7uGm3XsAqTodJiCkdzDqS3clvo7OQKqfMPGSblskCZ5xNyKgbygPlClEztDlNG39dndHLNPzDmaOO3X5f_mtRBAAB8ImyrNlgnXpBagU2ayVXhqKLs0VDleTH7hPl0qZFcFLmzHv435MS-xNbWaAf5RziRk8VUhZZLfWXeca9V3Yhw_BCXHRUOVSQRnjwtPYmfvHM-p9ya8JLtLKSlnYRrw21L6MhOMw0Pflh3e9Pta-P1UV31T3lzK4F_6_liDlVtdMUOZnykYaSg9A-PnPLQ8xPSiwU5eZ0OkQpIl6D-QQBPBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏆
مالکیت توپ دو تیم آرژانتین و انگلیس بعد گلی که گوردون زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100489" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100488">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/100488" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100488" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100487">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100487" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100486">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9b7cbb4f.mp4?token=HAzjOStv01Xhv9yaamfZnxJqXvj0K_DIXQc758jSAq26mAezYgszGMVtAdS3sPsHRaTM79rY-tIQfxe952m5Te9HDcXNxQT3Num25HEPeFrth8YDdx8JLJiBiBaf_ZeC2qK8xYlD3sfpBQT_CuGAuXRRxMx2tgIpbFNGXoPQhSTiihrNiDovJJbTygNIncu35QEmZWHwjRYvlLg3ZOO55whWKUWYW_uZEZQXcxXYIM6K2hkph3p-X8X6vmOwCF58vt7fVSiJTRv3g563xJrzHMNhkT4qGLKYRKW-L5u0_OLgQda82YvRwbpao8qxW-JW3PukNcYZFX6zfJKeWsFdvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9b7cbb4f.mp4?token=HAzjOStv01Xhv9yaamfZnxJqXvj0K_DIXQc758jSAq26mAezYgszGMVtAdS3sPsHRaTM79rY-tIQfxe952m5Te9HDcXNxQT3Num25HEPeFrth8YDdx8JLJiBiBaf_ZeC2qK8xYlD3sfpBQT_CuGAuXRRxMx2tgIpbFNGXoPQhSTiihrNiDovJJbTygNIncu35QEmZWHwjRYvlLg3ZOO55whWKUWYW_uZEZQXcxXYIM6K2hkph3p-X8X6vmOwCF58vt7fVSiJTRv3g563xJrzHMNhkT4qGLKYRKW-L5u0_OLgQda82YvRwbpao8qxW-JW3PukNcYZFX6zfJKeWsFdvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لیونل‌مسی به فینال جام‌جهانی بازگشته‌است...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100486" target="_blank">📅 15:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100485">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6732c2de4.mp4?token=SAqBBCWhn1Vx-CTQraAup8p22k_DtViis0bTFMp2gSJ5ja_0dX9hlA1-tPW_vW9TiMfuHXRkqZ3C5ES8eY2Z8buxV9GgS-FflJi9vQ_3pfyoBfHZrQ8WKGZHj62NDmEhGL9AhjyTTGCBbne25RZDLXYELrVfQrSbD4FzJvdNbVTY4GCZjED1A4dHgMHq_zgzrbI9ihwse71l2n8yFpMA_R7WBh9oVDzWtSr4w2p1nvfgBij__jPgHIUVddfWaBUz-FZuK3GH2DFigFmDixsZ67ScPuyQ65r7tPbTABFcvmmm0TX3AUe6GcYq-QnDBv26XBWhWtNBMey4RiePk71Hug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6732c2de4.mp4?token=SAqBBCWhn1Vx-CTQraAup8p22k_DtViis0bTFMp2gSJ5ja_0dX9hlA1-tPW_vW9TiMfuHXRkqZ3C5ES8eY2Z8buxV9GgS-FflJi9vQ_3pfyoBfHZrQ8WKGZHj62NDmEhGL9AhjyTTGCBbne25RZDLXYELrVfQrSbD4FzJvdNbVTY4GCZjED1A4dHgMHq_zgzrbI9ihwse71l2n8yFpMA_R7WBh9oVDzWtSr4w2p1nvfgBij__jPgHIUVddfWaBUz-FZuK3GH2DFigFmDixsZ67ScPuyQ65r7tPbTABFcvmmm0TX3AUe6GcYq-QnDBv26XBWhWtNBMey4RiePk71Hug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مردم لندن درحال تماشای حذف انگلیس از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100485" target="_blank">📅 15:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100484">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0519f41eb2.mp4?token=g4bFkcfp_UmfKPLEff_D1e97afYLfiQKnPQl-Xt0HhMPzAH6wdDdW3UFBzECVn3L9-6tm09Phj4LmAiAZgL2fAR4zEYCvH5mTQLjOpNGZ3XaOxPbKrIyL1Ob3U75wtHxEwDRlVmqUFkQHoenfh0-5d74xpuD4nlxGzA0FYdGH0nGjv-yF73EsVsqH0ujbzxxXTWaBnubxrdalatYHQtT4_xh5UtQLxPK4Pt9rHb_GOrIHEQXwg9pIc59zx4a5DAK7Umrr2Ff7qHqlUsxLG4U61Uo1TpEWY0azT3y053Ecre0ppH1gt-lgSPecfrLsr0rhiCCIjtnT5yCLgeIK-YR7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0519f41eb2.mp4?token=g4bFkcfp_UmfKPLEff_D1e97afYLfiQKnPQl-Xt0HhMPzAH6wdDdW3UFBzECVn3L9-6tm09Phj4LmAiAZgL2fAR4zEYCvH5mTQLjOpNGZ3XaOxPbKrIyL1Ob3U75wtHxEwDRlVmqUFkQHoenfh0-5d74xpuD4nlxGzA0FYdGH0nGjv-yF73EsVsqH0ujbzxxXTWaBnubxrdalatYHQtT4_xh5UtQLxPK4Pt9rHb_GOrIHEQXwg9pIc59zx4a5DAK7Umrr2Ff7qHqlUsxLG4U61Uo1TpEWY0azT3y053Ecre0ppH1gt-lgSPecfrLsr0rhiCCIjtnT5yCLgeIK-YR7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
جمعیت پشم‌ریزون در بوئنوس آیرس آرژانتین هنگام صعود این کشور به فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100484" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100483">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b87eecf2d.mp4?token=PDsdpI33x70R9aY-Iy5T9iRXWt38zwUW9tR5ni_neNc2GiUU6O79v6iStkAvVcwXd8HAysTHCpAO0dqN2F-B5XHXAjxHAqPZngfyBNGqR3EScOBn3itpbuUR9yFD0--Tydm810GueldVVpWz8sofNUlsghx4-ac6fzdjshdoFac2JGRXvvCzn8C4JMut2QdWBpEA-qBRLmAkOCA_3IVaSrYkuyDeB7Ic1SacCMV-LkXm0QA0j1QyLbdRKNPmLS0_GYNb0_-2yqly9sazZS59TgkTtlQH2c0Hw84p3hiM7n5F96reot3g-tF6ngCKI7ngWUJijsoTPRvXWkjOcBGZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b87eecf2d.mp4?token=PDsdpI33x70R9aY-Iy5T9iRXWt38zwUW9tR5ni_neNc2GiUU6O79v6iStkAvVcwXd8HAysTHCpAO0dqN2F-B5XHXAjxHAqPZngfyBNGqR3EScOBn3itpbuUR9yFD0--Tydm810GueldVVpWz8sofNUlsghx4-ac6fzdjshdoFac2JGRXvvCzn8C4JMut2QdWBpEA-qBRLmAkOCA_3IVaSrYkuyDeB7Ic1SacCMV-LkXm0QA0j1QyLbdRKNPmLS0_GYNb0_-2yqly9sazZS59TgkTtlQH2c0Hw84p3hiM7n5F96reot3g-tF6ngCKI7ngWUJijsoTPRvXWkjOcBGZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
فریادهای رومرو بر سر بلینگهام بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100483" target="_blank">📅 14:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100482">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f72bbd0a4.mp4?token=dYZOoP-05gDdZcIUeoewLBr2UT-5_02qb6_TbGQO0xWhvf_z5GumjYcjTnP5ZQqY5IjXjrQh18_YvLMm26H4MYNqJa8kZiw_ehI4RTOKpQXVvpLGJ4qqlkDQAM9zFGFiwBO0_Mprp5mneKu-pDao8hFyS6rV2YcrSKxLRAdWbKD6_q8O8aubL6oG1yEAF7McJew0dUJmoyI3V_ZIuYg99xV2FCrV_2-uNLW91FNzwGe_nKGINNXHfEVkML5cNC1BFgAOh7rFnW0fqvpUZ4VU6zHHx42qJfFSMo2EGrp88JqbwA5kDl86Gh64oQQp1cqh5iRVHd8LVUYSANIcS5ZNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f72bbd0a4.mp4?token=dYZOoP-05gDdZcIUeoewLBr2UT-5_02qb6_TbGQO0xWhvf_z5GumjYcjTnP5ZQqY5IjXjrQh18_YvLMm26H4MYNqJa8kZiw_ehI4RTOKpQXVvpLGJ4qqlkDQAM9zFGFiwBO0_Mprp5mneKu-pDao8hFyS6rV2YcrSKxLRAdWbKD6_q8O8aubL6oG1yEAF7McJew0dUJmoyI3V_ZIuYg99xV2FCrV_2-uNLW91FNzwGe_nKGINNXHfEVkML5cNC1BFgAOh7rFnW0fqvpUZ4VU6zHHx42qJfFSMo2EGrp88JqbwA5kDl86Gh64oQQp1cqh5iRVHd8LVUYSANIcS5ZNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇦🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنچه در بازی دیشب اتفاق افتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100482" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100481">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq-nQno1gJp2NuBSHZWrjDKMuRvEl97MEPhdPm4XeLds6v2xsLyqtwYy88wXFIEq1VC3Ifrad63JH91kHTkYezDa5UgPpymuAa0VQo688s7P1wgGv68ujCrQLSDDFIMU1nzBh2KsoZ_5Tjn9vCGGTL4pqNb7TSHWagZGamSKenA9C6sldZf8wcNC7b2aWYNPERPbtvbn-DXob-A9bBUZcG4kpbHlflwofSYDli58ZqH0o2ZWk43g8bAL6KrvsU2PK2ue9LuFPyVKgT8xwLr2g8K1ZDP24gPXndfyGnfCCWsAfdkRmyI1LynZiktTLfZI1xo7r5ledNGnEzd2DGFRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محمد مهدی زارع، مدافع میانی ۲۳ ساله احمدگروژنی روسیه، با قراردادی چهار ساله به پرسپولیس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100481" target="_blank">📅 14:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100480">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇦🇷
سوپرگل انزو فرناندز مقابل انگلیس از از نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100480" target="_blank">📅 13:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100479">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d71841ee.mp4?token=csknAfXpbgyizyY0aqG9zcsiKCwcBZY6GAlLspjIvsqt5Uj2_8OMjQR5YU3jS4gtgPNCz75jaNjn2yTiGLgxH3Qi4PRE63dK_YqsH2CHxWHE5cylDAyIl_Eb1MId24UxDMANB5mLkZ4T_qEX5LWqqQYJcDkNmJC1RxRRf-lWMgIqNjk3UrrlOtOAFyXFfoGTAdHt8SkiT-se14rufTegG3xZQAM6zY1m15xHmEAWGr5pntlQTd4QPel90TovVRmyfF5Do_xne8oG9oHgI_4oHlqVMiJlQ9l-FrRGYm-fR3d8qaC8xVs3nEgIVO7GkPg2KXpUrLIcdTkrZnM8Rm6UTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d71841ee.mp4?token=csknAfXpbgyizyY0aqG9zcsiKCwcBZY6GAlLspjIvsqt5Uj2_8OMjQR5YU3jS4gtgPNCz75jaNjn2yTiGLgxH3Qi4PRE63dK_YqsH2CHxWHE5cylDAyIl_Eb1MId24UxDMANB5mLkZ4T_qEX5LWqqQYJcDkNmJC1RxRRf-lWMgIqNjk3UrrlOtOAFyXFfoGTAdHt8SkiT-se14rufTegG3xZQAM6zY1m15xHmEAWGr5pntlQTd4QPel90TovVRmyfF5Do_xne8oG9oHgI_4oHlqVMiJlQ9l-FrRGYm-fR3d8qaC8xVs3nEgIVO7GkPg2KXpUrLIcdTkrZnM8Rm6UTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران جذاب تیم‌ملی آرژانتین
🔥
👀
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100479" target="_blank">📅 13:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100478">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کریستین رومرو: امیدوارم وقتی بازنشسته میشوم مثل گری نویل احمق نباشم و از بازیکنان انتقاد نکنم
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100478" target="_blank">📅 13:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100477">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJWAzEHa_6-UsX3rIpZd2Hc7_amQY_DN-uXONd6cGzGaiTyg3nFBD6NZwz-8-sYjl-Fh6ZlOCS5vWrr0nVY3-MMmXz4qZy0VZzPJVd0tnKICAk3_DHddb1fWOwthHU4r30gd3evtEvHHIHtZMg3dk9Uz95Zipz0KCzZoINLJ3EYxsVISJRacCH6un1xv3LF9P09RvL-Vx8O4ANeMARsFeo_8NTHORZ8nAP3afaWdZIDQg_yHJNupMcIRswNmc9gQjzYWK3sgll-VJ94oyimXEv_nLliEnTXLgOtauNzEV95Df3z8jYyEX7EKNdJqAnHC_Lw3amYxZzksyYwKneN_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
دو سال پیش در چنین روزی کیلیان امباپه به عنوان بازیکن جدید رئال مادرید معرفی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100477" target="_blank">📅 13:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100476">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3896b54423.mp4?token=kJXKbDh_mmPzJt5KwZJR89Gyfs7sWCWrRQ1rwQc-tfL8HnrTt2ThM9Y-l-F4XuHtjs6y3bqSaZRFqAUAN78hIHA-MpAUgdN2mpoIhBN9N78JwT_5OmyQ8ZqwWjQYYOzxmB9j0i7jZi29_MPy1Bqso2rpRBtLa8ydjJZdjX9HwGSpWs7CXHxSaHDa2zLHFpTG7bVmhgDWMaHSx1nOLXpcNFRxIyWe5KjKOf_ZxcDDW1kSQZc5DSwR6jMd2pDUOXplLfa79cmq0-vUaom4Y3RR224j6H7fToVFxG4PrGK67oyr4zUQdFOUWhfK1MFzymSKS9wchyCv2eNtezUuhf9VRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3896b54423.mp4?token=kJXKbDh_mmPzJt5KwZJR89Gyfs7sWCWrRQ1rwQc-tfL8HnrTt2ThM9Y-l-F4XuHtjs6y3bqSaZRFqAUAN78hIHA-MpAUgdN2mpoIhBN9N78JwT_5OmyQ8ZqwWjQYYOzxmB9j0i7jZi29_MPy1Bqso2rpRBtLa8ydjJZdjX9HwGSpWs7CXHxSaHDa2zLHFpTG7bVmhgDWMaHSx1nOLXpcNFRxIyWe5KjKOf_ZxcDDW1kSQZc5DSwR6jMd2pDUOXplLfa79cmq0-vUaom4Y3RR224j6H7fToVFxG4PrGK67oyr4zUQdFOUWhfK1MFzymSKS9wchyCv2eNtezUuhf9VRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
توصیف عادل فردوسی‌پور از کامبک آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/100476" target="_blank">📅 13:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100475">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876233c65c.mp4?token=mYK_TNPG7yHFa50OUfWoUASWpMNFLPbYYPEkwf9wL6ssTXxERy8yQIVYBaMI_lDuHGWYp8OjXKNauOFKV7bAUC6MJkvsmPQV1LvK_ugf-NdTBDqaylDAlsj3EmRgDn9WwT47VcziycYtj4CRLL5f4H2avLtorbvkUG2XHRgiIawR4G7dYKFcoDz8wxhp4DpqoFLcv-dHmSggSPM6313L8zky_o-RCzkTUhGqNZGOGNa-EqXCtj5YTTSSEb86vvBELGgCWxpF1wwxjrMDZOclWz14Emc5MgLNLBO7hs3JTPMBPpI5u1SRRBLnwzro7W3gGfyQozb-D6ZPjMmYklOgOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876233c65c.mp4?token=mYK_TNPG7yHFa50OUfWoUASWpMNFLPbYYPEkwf9wL6ssTXxERy8yQIVYBaMI_lDuHGWYp8OjXKNauOFKV7bAUC6MJkvsmPQV1LvK_ugf-NdTBDqaylDAlsj3EmRgDn9WwT47VcziycYtj4CRLL5f4H2avLtorbvkUG2XHRgiIawR4G7dYKFcoDz8wxhp4DpqoFLcv-dHmSggSPM6313L8zky_o-RCzkTUhGqNZGOGNa-EqXCtj5YTTSSEb86vvBELGgCWxpF1wwxjrMDZOclWz14Emc5MgLNLBO7hs3JTPMBPpI5u1SRRBLnwzro7W3gGfyQozb-D6ZPjMmYklOgOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
گل‌دوم آرژانتینی‌ها از این زاویه جذاب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100475" target="_blank">📅 12:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100474">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ade47d4d3.mp4?token=HnJbvXMCi5fJK1ub8Dw7Zd3ql7eA5OIgJFaf_dtaV9JxFlbEMHCq3R7_O-_J6On1NfGbpzjSzpP2yaq9yxknuSW5UlH4XIARinYbWLN-zU-kZly703HuSRad1QsJSKzAsuV0CD9Xe2i5a1MLRMX4Eld-aA_J9Qpgnj8kv1kVJDPfhygiMvDsUFxsfnymfYrqrewip5yehnG4tzTDsMpeyqp4E97v-X8VkCkjABw3iKba9jiO5YunJWhGO3vWOqeLtUC0HFZemmPC7AFLgHDzvDreAunfjtT72oYhdm8zkNqnMXpLLzPsetZNrGW2mJ3zICO0LWUrdB6jBX-Sbit3GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ade47d4d3.mp4?token=HnJbvXMCi5fJK1ub8Dw7Zd3ql7eA5OIgJFaf_dtaV9JxFlbEMHCq3R7_O-_J6On1NfGbpzjSzpP2yaq9yxknuSW5UlH4XIARinYbWLN-zU-kZly703HuSRad1QsJSKzAsuV0CD9Xe2i5a1MLRMX4Eld-aA_J9Qpgnj8kv1kVJDPfhygiMvDsUFxsfnymfYrqrewip5yehnG4tzTDsMpeyqp4E97v-X8VkCkjABw3iKba9jiO5YunJWhGO3vWOqeLtUC0HFZemmPC7AFLgHDzvDreAunfjtT72oYhdm8zkNqnMXpLLzPsetZNrGW2mJ3zICO0LWUrdB6jBX-Sbit3GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
پست جالب باشگاه اینتر برای لائوتارو
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100474" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100473">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv_idBrnPV3lp1KRvYDF8rSxvLWg6z684XcWYAjssB7fLVyDRcz4A-xxelO3czpgIM-aqnaxYTaVLLeujFpVV3fWz2xSOG8-lKlBIj8wyrSv8iS01SoSyxI6Uth1gtYGPQkxamLUNHiv0zY7DZgLuozy5a3k1HpTPO_mcQT5U6O24O4FYcQGHQkKry9gankcvWiUHg7k-LKe7aHdDphQ3P0ZcFotjhaEEmRJqHdZuFq7Mj74xPBrOTGP9KXVa6IwyAvRgL8mUG6RkINBUKmS5elC0H1WywKvq5V5tbpB5oaIB-3D6M_B88yfGIstRzIWN9eyHDfQtGEfvprNdOZwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب نیمه‌نهایی جام‌جهانی؛ خط دفاع کاملا اسپانیایی و حمله آرژانتینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100473" target="_blank">📅 12:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100470">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tCFnBSN0fkv-36Zt1Qx2RRoO60E6sgwgcWMcKKbRFbViBoCh-pz-7fwLuZTELu8o4bShb3FsXWI7m65NXEasM1Ixvi8J97UPxv69ynAMmFIh-poMYuIR69DDyZnbz-aqJc1kRRszfCPzVnpmvX6qVCLt0VSXvDPSByU93KIsTHW_y4LUZqX9N8C1FDr1N9ERfMXGIRI2DkPPsXk2wuVjWM68B3k8ReQmsoMroA-eRbMPdoAksTf3JPfjhjYfuy9uPaNoJEahS_KWSF7noPhEiU2FL54SgjmLVEMEkws-ccgLZP7z03CRN3uyKAZjXCAYMgfECqexkqEW9i0-9dRHig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fcku8vNIQlJx_dln20ecu2a3g5eOMhQ1zSofnYA-DK2h3e8Dmx6xnLFxhx06pw4-YK13KXzyl10RNKrjS2HOllx-DSrqYgltihPXdmT7W1QFlHN4VLaLDU4Jvw4r4hO7QR1Y0_XxVrsZeAlpDR3hdbhBHgnaOJilUyPQ8BRbRc9kkTjUDZajYzxc8OLfd-R7kSziyBdv6d-FNkmX1879jwEaIBFRwZdjAptBFTsYcIbkdsHY6MFeg5XBBa-FM2LC39tJm6cSt3a7FxtAw-nBubQaTwyjCpRvwx3URv3H1VivxgQoztKxCsePeefmCvAD_ulbGDjqqLmG3v_0QEx2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvYMWH1mNXOS64QMigpmTYPZp4cJYIH5FfAi3NUZ6_AXPT_Q3twFZZP_5rEsB6t0BXVf0xcFCzHpIYcOWrIJFa0ceTvDZsNzvaA0qEiBucZ2Zz_G_ts8cZ1c02g98-0K5ez7X1MFFIRDF96K-tO1d4HXasnV9jSUe0xR4yThDb-GUd9e3_2P1ReTa6iIglHzmU4TRUbUncR8DuneEsqL5oQH2RuahFQksKdm0HJx8_iyZTj0A56rUDWE0dGY6TOytmKI46k5QojXZ7k2DgcyMvWmzyBBoR9LYvYAzGvvwHWau80Bx1PnFvL29ujYLgiXrvXpLXAQRHYcVf1hkDDgCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
⚠️
📊
مقایسه قدی سه‌بازیکن مدافع انگلیس در دقایق پایانی بازی‌دیشب با لائوتارو مارتینز که نشون میده قد دراز همیشه ملاک موفقیت در نبرد هوایی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100470" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100465">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pt-Ybj748mT26RIytsRf1bD4cDawiGps6AcSC-3RQys6xhaLxpUKl-3WQJ4PaMvTCBF4jMakNmUqB435rFIaX12s_0L6pYDwZfIexj859YTMQpKOZIUKelw2HScEnpVWMtoA9bW09gfcQSsrIVrFuUntXzucXGT_NpJmKbs2XSI1Ce4expwC6mxQDvLHuEDXEHRrpDK50sep0nTxHNhrjOue8jU47dy6Sysu_zlCzFSX4PQaMko0KyZc4Fr4VcJKxSKXosB1-OATsSQ7kSiRM2FiMSq8OS2VNfhcP_hzbn3XVBQmis-uKgquSySEhg5EdpG-qtbtMxocEJ_ch3ipcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rEtRkJ-OH8yQV1uO9FrnoVY8ybp8R3Lr1jrTuGvE6Pe-xQXv1-ljD5RvNq2Zi4jmmM3X2xYQt7MAWpbrc-4gp1pVwKU62jcYeq28Bq3HgqLF__m7BiEZhw-rNv6kqWA7mdrO64z8CuHYArsrntl54BloLkMtWSGIfcem-dsS-PHco_PjjLdPanFJr60lD8q7aAqXDFbe4KOPVTwQwdavFLro9d6n7tu43aFwcQCLvdJ1MSPx2Tuv9b74rpTTVsBhZvpba7DPD4ZoJoBMy3Db34FxfB3hfeW4b7_zv4anMBgx9bIrW7xK_EBroBe5nnjXN0svLIl3BQ0xmP2W8stLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_Uzy-YnJiP9dR8BaU-0ienlXvlcxC0mr7dFKDOsva8w6uKDp6fDQWQBn-sy1XR8eTD4i2X6zPiy_PD2EJcg8U6wa5tcZc-sEbpAXkbydzcRh6AahV5mC4E6Pe-yPnfivCE6t7zV0XIPRGsGEi8tL8YZXpvPjd6qiqOSVemCnhjgTK_17aydv1P9bBb0UPREMnnRO2ZeuhCvfMlw3fV_HyGQyiVqbAuYZW-UMgLOdSEx7cNLCyOO4nHfC_K4VfQE47CbOoIwsJzjEVn9waksAbT7lnqyClNN77zOT8eKXdUPHBVAMX2wj6qiPXZiuV9oHHVclW7PtdOwz4PAo_mfDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MavE2C9cGGT16XkAbjlijwaoICPxFpVkrkAM7roCmIHxOuRYQ5bO-FZwWcTnH5MNIKwlXlnrCGlHlHgY7bgPdPCo2lY2hXRAezPofl7gV1KBPgVe1VTYFjntsUzlLs5SKj9HlYGqDAlwupeNUOAip1I3hPFd5wfJh8NgsOCljc5M5bImOouJV3S1NKiRfuo-CBsBRnvDWnsYbUgjBvj3zEwqWLj_ou24rY9C73uMRbT_WXSOqdmJgpXQMmCHb7dVmPCGf1qpD4npT1ZLGK4dXDPxWW6dTy9gnbU64-Y6rybs46A_PEzM9CFTlupYwnJ-PFJGayY2S3QAlWHJbCeB4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJOafa5Jk72kbgnup2ggubH3e08g304HRbgU-Nmb7nIeoxih67eHXcLp2LP3TQGDOahrITOnDQxNPAhZgrqkRCYjGYlF4MT0Ejfwviyf98Ucjffx9vEF_mb7dmbEmE8tQ5upImaEVVcEjXSd3feFZ12wwtX9MdniuF-MnGnOoQkKF0zDzWinX4-6tHJekkfn-FzwnWqTZbU8-hTryl_Lim_2ioK7zxVQRlce1t8L7QmaUTyXDax06wICv3mjjp7jnFy25HbDiMEL0bBQwWH3E5bHUPsXe8yqgO5i0zwtNhcWcrWODbXZqbjbsXupTPQWRg34kg8g1hG-lpD6SThRuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🙂
اگه یه روزی بعد دیدن این عکسا میگفتیم مسی قراره با همین بچهاا فینال جام‌جهانی بازی کنه بهمون میگفتن کسخل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100465" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100464">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cca92eed.mp4?token=p6KSHyQBL778Ry_ZD3xdoMgit2o5Y44hH28JT1A_V2hcwEdYnmGylBbEZjHrQda-khJTg72_KKPnhNoR7m08yg5jf_gn_3aWktc6wGLLGItj_uc6vn6tCO1m_nydbeBft3TUVbCK9moarUmrqOrOiiDi7kV6pR6AjKOanFkNUbEBJ5F2nr8TAL_-m0UqVCP7yQmIaQhp5uVRHZkcWpywoj7g6-etZ7m_7-F0eiZfHhTiaZEuPMgQbQFUpTZC8Tt5H1rX0535bqBjM5Tew3BPmjNIZLJW_lGAOeR0U_ZnSzKQM9w0hmcIoVtD7Kr2zGXCbKXUZJ1whgx1Aj8PmYNEdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cca92eed.mp4?token=p6KSHyQBL778Ry_ZD3xdoMgit2o5Y44hH28JT1A_V2hcwEdYnmGylBbEZjHrQda-khJTg72_KKPnhNoR7m08yg5jf_gn_3aWktc6wGLLGItj_uc6vn6tCO1m_nydbeBft3TUVbCK9moarUmrqOrOiiDi7kV6pR6AjKOanFkNUbEBJ5F2nr8TAL_-m0UqVCP7yQmIaQhp5uVRHZkcWpywoj7g6-etZ7m_7-F0eiZfHhTiaZEuPMgQbQFUpTZC8Tt5H1rX0535bqBjM5Tew3BPmjNIZLJW_lGAOeR0U_ZnSzKQM9w0hmcIoVtD7Kr2zGXCbKXUZJ1whgx1Aj8PmYNEdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه‌های فیروز کریمی به قلعه‌نویی: تا الان سه تا تیم تو جام‌جهانی نباختن که دوتاشون فینالیست شدن و یکیش ایران بود. این برای ما افتخار بزرگیه و باید جشن بگیریم
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100464" target="_blank">📅 11:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100463">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ba5270ee.mp4?token=rb7Nte0MBJ2oqoG6JFihoeDlwBXp0BYZuRIi0a9Hw3YS9D-jQUuHZYf_3ja2tnMQcn2Dndk_KCgzDdLXGkD_D8Wky-SUDgjnS838XOS0O5bRckGuAO4bEFy2LJfPRVLiWWI1ojzQ8vlMYYiUSaN5JCJzyvsCEdO3TE73dG7IvrCWO06yWWgL8k-Krc_jasMFBB1yQSBak3wzX4twhJQ2MfqOypk-96ub5rvVHdHI_nS2rYkB1HPcmcwvpP8N5ImykKTKlrCNRQgLpMydPL4E3i72LkxbrxptXwevgOupQ0R7TWuKJdOKt7P7gWSNpjG4lMnK_TOh6-5uJs5_kklElQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ba5270ee.mp4?token=rb7Nte0MBJ2oqoG6JFihoeDlwBXp0BYZuRIi0a9Hw3YS9D-jQUuHZYf_3ja2tnMQcn2Dndk_KCgzDdLXGkD_D8Wky-SUDgjnS838XOS0O5bRckGuAO4bEFy2LJfPRVLiWWI1ojzQ8vlMYYiUSaN5JCJzyvsCEdO3TE73dG7IvrCWO06yWWgL8k-Krc_jasMFBB1yQSBak3wzX4twhJQ2MfqOypk-96ub5rvVHdHI_nS2rYkB1HPcmcwvpP8N5ImykKTKlrCNRQgLpMydPL4E3i72LkxbrxptXwevgOupQ0R7TWuKJdOKt7P7gWSNpjG4lMnK_TOh6-5uJs5_kklElQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇦🇷
😍
بغض و اشک‌های جولیانو سیمئونه‌ وقتی دیشب راجب لیونل‌مسی صحبت می‌کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100463" target="_blank">📅 11:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100462">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d647b8c993.mp4?token=vQUWkUj9LnGeyTJ_i96dQJlegNmuENnQXnMEu0itbCPBpkfBVPVkPlvwII9L9qwZkuRaST1mlYXcpb2UXjFNJOK37rKaIEBdjprm1Pc_P1vGGGqLDRPF9FiBMLUD7ZJKQPSuth2PWniy9GjhkKYcXwUhbYPiu_aQGiWEAeyi7oXnCuLuiiAOnDvzXYfpOXQaP-BfcLALc1hp9VPiGFesgJrn1hqWJIY6Wp9q_TnORKGRepRPMvn6oIpQLJzbvY71MSQdPdOYp3WglLe2u0xPCYUdaaiseRW8lr1Lk94lflrRpH96jFK2P_jO1TMr59zXvtc9mE4glLsNnpVcupMfLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d647b8c993.mp4?token=vQUWkUj9LnGeyTJ_i96dQJlegNmuENnQXnMEu0itbCPBpkfBVPVkPlvwII9L9qwZkuRaST1mlYXcpb2UXjFNJOK37rKaIEBdjprm1Pc_P1vGGGqLDRPF9FiBMLUD7ZJKQPSuth2PWniy9GjhkKYcXwUhbYPiu_aQGiWEAeyi7oXnCuLuiiAOnDvzXYfpOXQaP-BfcLALc1hp9VPiGFesgJrn1hqWJIY6Wp9q_TnORKGRepRPMvn6oIpQLJzbvY71MSQdPdOYp3WglLe2u0xPCYUdaaiseRW8lr1Lk94lflrRpH96jFK2P_jO1TMr59zXvtc9mE4glLsNnpVcupMfLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
لیونل اسکالونی در تمجید از مسی: "اون دیگه چیکار باید می‌کرد تا ثابت کنه بهترین فوتبالیست تاریخه؟ واقعاً دیگه هیچ شک و تردیدی وجود نداره."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100462" target="_blank">📅 11:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100461">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45e92fe93.mp4?token=dIRGQw_h_6tRtjyjmB0lm0cXTlbUcYv0srWaDVEiABr3AIUMxRj2CcqpV5WN19lZG2PkZ37phdeWn56Jx8JrINBEyAi1Wo3w4s5VWY5DPO_Z_8l9bC_rjqHhVP2jFTyZqoQpfSl6KQjFvjeqG1GnsAJXIodx-jcIH31xerbR8uBJRCgtVTFRkAF_3v4WxnJYr2tZuJ-VLRhFm_SyM3t7Rflk06R5YtfSyp6Q24etoJ01-czUOommSDbBkh-ZOQd8PVY_TlHt9qZXutpCwX8kA3UDGar_D1WcBkC6mbIz-YRLCPTVVKtjd38f77-1np1usagoY3WDwO9b3Z7zlwTl7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45e92fe93.mp4?token=dIRGQw_h_6tRtjyjmB0lm0cXTlbUcYv0srWaDVEiABr3AIUMxRj2CcqpV5WN19lZG2PkZ37phdeWn56Jx8JrINBEyAi1Wo3w4s5VWY5DPO_Z_8l9bC_rjqHhVP2jFTyZqoQpfSl6KQjFvjeqG1GnsAJXIodx-jcIH31xerbR8uBJRCgtVTFRkAF_3v4WxnJYr2tZuJ-VLRhFm_SyM3t7Rflk06R5YtfSyp6Q24etoJ01-czUOommSDbBkh-ZOQd8PVY_TlHt9qZXutpCwX8kA3UDGar_D1WcBkC6mbIz-YRLCPTVVKtjd38f77-1np1usagoY3WDwO9b3Z7zlwTl7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
بطری تقلب پیکفورد که دیشب دست بازیکنای آرژانتین افتاد و حسابی سوژه خنده شد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100461" target="_blank">📅 11:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100460">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔥
🇦🇷
جو فوق‌العاده رختکن آرژانتین که نشون میده با نهایت اتحاد و شایستگی فینالیست شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/100460" target="_blank">📅 11:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100459">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
‼️
⚠️
زد و خورد طرفداران انگلیس و آرژانتین بعد از بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100459" target="_blank">📅 10:40 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
