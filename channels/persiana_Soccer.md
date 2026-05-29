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
<img src="https://cdn4.telesco.pe/file/G_wCbs8BWU0C2nl5NuCqMlHG9PdTL_uDYsRduZM8alQ550Xe-kUonwghcU2-eh6UDipHFBZsRDKFXeBk0ye8RkW3ArGnSFQ31GAs8anRvJSxRCUYyQsq8y0a3Pf-v12WxXoxur0yveGZ2xUUe4pXy93JfWm-HhSqlCXdRHC5lxLikLLn8jvxcWcRAKtfHeKdN-U3FG1LhTmR0uDRgZ5kXhb7aaIT03Tg1HtY7bigW8hg5tZ34cJgZaqcSvO3WTIFqKOk62w5ZCtDiKU_a_8w1XGJ90N7TK3XKWZZuhs5sXBJ4L7nS5FK9kbVi6dPcheD_wFk-zHroE1V7ftG8pmN7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 182K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 10:08:38</div>
<hr>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=XFp6X7peeTiSe1i7gSOwDbJJ5pVEB0Uwl41M5XohaW47pYFcmwy1jaav2zsvz9acWFTgkoBvc-IWrBMWLxXP0-vZje4yRs7GBm2gEdsyOlCuaIfSXxGZmx7HwOp8VtuatToNjIf2Mk6Ap5fwpXc6QH6Qp9BsvhrP2TzoFhy9ySv9B5Sw7EcIL01oN8T53mWU_lqI4nW4JEDJY0NzGzwnJJo5PW1F_7sz7bqXj2cf7pxvnC78p4oFysnLNaHc4FgtYz_QrESHDpLqci5j4akfklo0JiXGAZo9XNq9rL7uaHPHqkH0Y_M-SDYh6WHcICrN563jTS-9QKHsKhbFeSBpm1eJ62zQngb1StfZ-51Xl8sIxJxjYdqDwmLw2IDnQB-3HZNZM6FTu70_ElJ_lABwN6hHazePuCiMdsUp5IrSKw_FSNYLNXrCjvDB332WQ9_UAlSsq6ZcOarRQ7W_-ljdhc0lwhc8HFE307aYliS2v_lo4CJIgv2Q0Cp01xLpaItoUGDg8IAYftM0mQ6cGtVXuLlH2RIbLcx9whCzjgftP0dZU0Z2-5pWjw965KWFdKAXCxFbhS-hK5BOyTtFfDnsmmTDx6JXadubJuJ_B2Mc5Q11pZulANN2gNAuEeqApp-MWUjAK2zVUIHQ_4E91q5SV_jWqAxcG-4PZ-MMcWBscZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=XFp6X7peeTiSe1i7gSOwDbJJ5pVEB0Uwl41M5XohaW47pYFcmwy1jaav2zsvz9acWFTgkoBvc-IWrBMWLxXP0-vZje4yRs7GBm2gEdsyOlCuaIfSXxGZmx7HwOp8VtuatToNjIf2Mk6Ap5fwpXc6QH6Qp9BsvhrP2TzoFhy9ySv9B5Sw7EcIL01oN8T53mWU_lqI4nW4JEDJY0NzGzwnJJo5PW1F_7sz7bqXj2cf7pxvnC78p4oFysnLNaHc4FgtYz_QrESHDpLqci5j4akfklo0JiXGAZo9XNq9rL7uaHPHqkH0Y_M-SDYh6WHcICrN563jTS-9QKHsKhbFeSBpm1eJ62zQngb1StfZ-51Xl8sIxJxjYdqDwmLw2IDnQB-3HZNZM6FTu70_ElJ_lABwN6hHazePuCiMdsUp5IrSKw_FSNYLNXrCjvDB332WQ9_UAlSsq6ZcOarRQ7W_-ljdhc0lwhc8HFE307aYliS2v_lo4CJIgv2Q0Cp01xLpaItoUGDg8IAYftM0mQ6cGtVXuLlH2RIbLcx9whCzjgftP0dZU0Z2-5pWjw965KWFdKAXCxFbhS-hK5BOyTtFfDnsmmTDx6JXadubJuJ_B2Mc5Q11pZulANN2gNAuEeqApp-MWUjAK2zVUIHQ_4E91q5SV_jWqAxcG-4PZ-MMcWBscZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی از مهم ترین دلایل‌موفقیت انریکه و PSG
: اون برای بازیکن‌هاش‌بجای یک پاداش بزرگ در پایان بازی، پاداش‌روبه‌بخش‌های کوچک تقسیم کرده: مثلا هر پرس = هر موفقیت = یک پاداش عصبی کوچک (دوپامین). نتیجه: انگیزه پایدار در طول بازی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/persiana_Soccer/22408" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=aqLImRWNSvZnqAcWIp3qrb_Fv4JNYTaubxoAUvE_y_wbN-afhYSuXvnuVPTmmHZsZiX5AHsF42i36m15_yMRk3OGULtqMEzU4vE8G_xGf8be-Khnt8lhM6Pb_KB1qhXf0TU6f5fPJURjrbtIGNHpV28UR0zVfcsLI2v7AJAa4Jtduqf5zU-28NNbEXoLNk9FnunIjRN99tCTkz79fYzBXIFK4Rsu9RIFV40xZM_p032wPf9xogjybiAaz2QHUFbShJoP7XctTJcng8w5JcVv-yF_f_fnS4Cr4A8tdRpzqQuQmDPhRng2JaQv04CSdHqRQhVQXwVvUfLbSOg7xsAz1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=aqLImRWNSvZnqAcWIp3qrb_Fv4JNYTaubxoAUvE_y_wbN-afhYSuXvnuVPTmmHZsZiX5AHsF42i36m15_yMRk3OGULtqMEzU4vE8G_xGf8be-Khnt8lhM6Pb_KB1qhXf0TU6f5fPJURjrbtIGNHpV28UR0zVfcsLI2v7AJAa4Jtduqf5zU-28NNbEXoLNk9FnunIjRN99tCTkz79fYzBXIFK4Rsu9RIFV40xZM_p032wPf9xogjybiAaz2QHUFbShJoP7XctTJcng8w5JcVv-yF_f_fnS4Cr4A8tdRpzqQuQmDPhRng2JaQv04CSdHqRQhVQXwVvUfLbSOg7xsAz1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وضعیت شنبه:
آرسنال با یک گل مقابل پاری‌ سن ژرمن پیش میفته؛ داوید رایا گلر ارسنال  دقیقه 34:
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/persiana_Soccer/22407" target="_blank">📅 09:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyP72RC_c90Tqm93TJ0pTuMpbpt0gZcI8iACfQJa7UJS8LEoTFES_Qh9eDzly_LYo4oLWTZM0xyVULy5JmXnp7DyPG7Jg44RfpurcQjUkL-2qVfHv7nbpEAOZ3-Ign3xKVGNGjqR0qQa9v28We3m4g1-37lVtw0sHIPNiGZZ4WaY1jong5xRujhgFHx4lRwH-aIy6MsMPrH2zSoD0j_uc_LqzZuBVk2PXozONBivvFzKFY86EnFx5bt7I9Svz5q6eJl_bCooCNncgyY5SymYZQatkvOzFznonaLIkN8kVO8HsCnmEewD0GuXqfCpW-ucKuCaSLpnu1KixEPX41Appg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/persiana_Soccer/22406" target="_blank">📅 09:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRPaxrshZG3NsQqqBi6oX_8-Con_8bTkV5Tpo_BawT5opN9xnEEkADPNhtiWF-bO0U_hWApYStgVebi5SMTOsoMDCWTFcw2aP6fUYFSo2Cw1bn-OJ85xuyADgV8tXV4-TGWBy2ihHPFwfEBE9UX1lQmtkFpD-XhImlCODUa3XkdHWF0doU6wdIh-NLRFgXFwrUhTY0w2X2Ck2Yso2DBNyYVd4STUhskdJsDdStOtGPPiYNlBQyiEb5f0CL-6shPdSXQO2IHU6rjKnn-ajSLxwlHTiUn1Kjthf2gn--KRYpp6DcreGvg-1Jngk5eEd28I20DbrxjLBuUqUkaVqb8kqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/persiana_Soccer/22405" target="_blank">📅 09:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DegpXKVFUJR0RGLocKI0KLL9i32iTERupG6lm2wt933tJ2uRY21-gzkx57SRTfsi9BO58IdqRG--ACUKsf8P0fBeiY9Q-0VGR1jtBpWNYR2qArcOceuU-UUi5ktdjkLTxxCp5cUsvMW7GFWKhk_Y8gJ1aOEhqHQ1JC2RD7zRokx4XtX1ro7wm_cYZGOQZJ-u0DDY6yg2jvJrDADwZPjn0AlV9eWJC5jUZ0d4L5j6X7PzU7GufFGNZcsntpGLjAOr_P0gWn5J1n5XULAQrKuFKBKrO15yjpalQ3qLq-jLzq4EkwkQcVpJ7ZhIbox5sdS5XFhm_2UTAk312O2R1RAfqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ الهیار صیادمنش مهاجم 24 ساله سابق استقلال و فعلی اوئسترلو بلژیک رسما از این باشگاه جدا شد و در حال حاضر بازیکن آزاد بشمار می‌آید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22404" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ2ESnQvbbLZDbezUGSrUHMYAp5zT6I2RtILOIWwQ0FrmB7T-13zLHHMkyMQ5RG_Ub21Z-_p8Ocy_X7uMoAL08TOUQj9xyzDZR7Y5aIs_9TrbPwRggv4CiEa0TVed3246E6_bmyark3sIFctEYkMn1SNevBNlwijOmvWFh0NEghPDE7eYWMH5ZDo45P8DshQOMAzj6yClmaUmYlQgNJisJ-XmHfXN0BxskEba8ahNxiRRLCVQxmGKvJRJJAtKEr4FkFGbce66Ezq0UmsCtaUcmlCNzIGK8h9j3fDHroMOY9QaW4iI04hzTxAgzPt-xSQXfvocGyzEeDX30hzW0CHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیست بازیکنان تیم ملی آرژانتین برای رقابت های جام جهانی 2026 با حضور لیونل مسی 39 ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/22403" target="_blank">📅 03:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKFlxHNOKvVwVN5P7YpSoxzPcyjBpe3EtTT-OlG8kWAuW9z-2QV1Y8DrK9V2HJSO145sK58WATa3ZsZiHRZKxtuotMtv1eBBzNdLDuDfSujYTWgGWBYoK_BBxrebmz-uQf_RHubhF5xnS43pjwRxjYQnFqaPzNhPZ-XuUTuni0Ybtw9jiuPkZlOGVM67RDdiLwSE_kBEWqHYaO3BS_dUalDLdSjvX5_yywB3XyiupFT8yTe6D9KTwBXrlAqn3PS8V1TWtFLLnNFmeldlV94knkeGgXDh28soNqnKdsalBCWmmL4ZcnqlmsmjOXdDReVNH_5_7viqQ7Trz2H6YnfJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های‌ امروز؛
دیدار تدارکاتی تیم قلعه‌نویی مقابل گامبیا تیم رده 116 رنکینگ فیفا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/22402" target="_blank">📅 01:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlQg3qP8cr8DJ6npHK9KVzLkoDHnygABJ6CHjpe7EeYVOsCw61Lugf0gK_mTdDsKd_k3iKFVNKUg0g36vEmTqnMUBMeJmNd84nmsWe2tk-DMRMfgKrIHrzLERc9YRLhUg05lgb52slng4df4TLYsf26LNbuE3dIqiLxr-S91xAVb9UNjie1TuVlEaUYGGM-fjdLmQS9SAtvNtKIHiWj-t1p_Y6vaQGQol3tCMK80zla4QbD7__sebDpQO6leiA6EMSB8pxpi7wr2ASc0FqIjwT22QI2Aw1W6gqmlo-swEMSHu3PI4D9xj2jTov6foOWPo6m-9F-aVtlZZikRvmmdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
برتری مصری‌ها مقابل روسیه و شکست یاران لوپتگی در جدال با ایرلند
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/22401" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmmkXSpVTQNtIU29tC-p6klsnuVFxKvuNrrCreeFnGN1ipfeurS14pE7zhl1iDbUzb947ZjRWmU37MiOLhwHK4UCWO3Mxnk_fpk1LIHYS8gQdW9AUKA4VIWWCn0gWUNmdRcJB4rBq1_7yoDbYpx3fmbX3jKWOQ4D8223f_XgLdSV4sVeXZtbvP1QR8fBhkhi0XC8jiAnMNEWZtR_uFUqZCh1Cu2ZH5gLPfl64RLqKjDdHnXlnvRu0TatHLRdEhgPBhINgAqJTVwZ4FidykspQ4Fc4j3mqnsKElrJNAF5XOY-c6AZiv3m2r3WKP5aS4y27Pvn7nIFauICxI88eR8x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/22400" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aK4GqUTmHaOUCxxDZzwzCB_bttSs1CzYx-9hplGXUDumQb-JOznivvNlVyLehh_k2JU1vI5DmpeE7X8nblKSOctiepwfwc5z9Byrh1AOxH-BZDNOjnnPdAjEamCFriktQTF7Les6AjP7Yda9nNX0IRn0fjPAfnJTDGh0edndCeGrA4-YN6B1bEperPv7L9xsGgMx7dNuBgqd-UGFs2IBUx6Ff6a3hsj13QNrcdi2AwwVz9yF4oX2vu3TCpoYH5IncrS1RQzf5zOPcIDEtBSWLJfrrTwNqeds7BRuYLwPhmrT3SB83T0QFOf3ZJDdkfoDXxziXtMVDNCIJErm4yFtcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برای دومین فصل متوالی، کیلین امباپه فرانسوی بعنوان بهترین بازیکن فصل رئال مادرید معرفی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22399" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTbviV7AarefffcD50gVZ7cf3QklBiBa3KkKQ5nC5pyT585Roelsakf5v1IesWZ_nt6ZbfUXrO_FiZfGu50s8smpz_pVX5xqm3PZQcGk_V-NHx6y1gOERFBelbHOm3wlnDgxT_OFZ3iS8WaKZwDOEy4_Nbi3XfCjpiCbwWN3X5HIwsDKQsAgaF-hm9c-PbPcWcljL6-3EWxbf2IbuvcB5fAITjfcXeLFUa2KzNkoTZdap7IYjIMrPzp8LtturD97IhJq9F5suNvcxJ4PkT5qC6kofZ7zh_tm8FtDium5HLAbOoN6sQKXaxZCMdYuhAQ3W7DzPRSI703vDwApkx9DYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی #فوری #اختصاصی_پرشیانا   دو باشگاه تراکتور تبریز و استقلال تهران از طریق ایجنت مونیر الحدادی به دنبال جذب حکیم زیاش هافبک تهاجمی و بازیساز سابق تیم چلسی هستند. دستمزد فعلی زیاش 750 هزار دلار در سال است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22398" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=udwH7wIYCyPoj-z30Lw0YAQXmPHR5vJeSQVCl4dWS2Imyb1C6EiUs4cWUtdifPA85vTzY_412xkngbEP-Gv_URPVeQdOQZIU4mbsQqD2iobFK4y92Exy0Rza7rMEpdfkG0zKcWyF6Wa7hspLA_SwroJ73tfzVKsdAho3I4AHG1GvKJ3o_xhyxd4iznhe5sc4l0NhUAz1Uzb1KMoPMuMpacEqvPJlU6paVI1IXue6lnffoNpfs2r9_vmZj5a9tb9NNiD_l-bXNPprbZIjbs19_CZkdMODyubLR8UP0JPqTppLQgT99uvAuOUqWNYFlUFS6LCH1lvBOHqwqYxJf0h8Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=udwH7wIYCyPoj-z30Lw0YAQXmPHR5vJeSQVCl4dWS2Imyb1C6EiUs4cWUtdifPA85vTzY_412xkngbEP-Gv_URPVeQdOQZIU4mbsQqD2iobFK4y92Exy0Rza7rMEpdfkG0zKcWyF6Wa7hspLA_SwroJ73tfzVKsdAho3I4AHG1GvKJ3o_xhyxd4iznhe5sc4l0NhUAz1Uzb1KMoPMuMpacEqvPJlU6paVI1IXue6lnffoNpfs2r9_vmZj5a9tb9NNiD_l-bXNPprbZIjbs19_CZkdMODyubLR8UP0JPqTppLQgT99uvAuOUqWNYFlUFS6LCH1lvBOHqwqYxJf0h8Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نت بلاکس: این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22397" target="_blank">📅 21:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQXZsHiwe9pq_OdrHkmoCTm6KBc61CBqEtV5MB0twlW31XHo115f0QGugNl9I1rhrlBuM34X0HkkqaKhhjsbjFrwzEHTE7cvRXBygzQdKQRZctLv3oW1Bj9k4Y8-F0ri3JmWKkdXq0a4VlB9lfXYDYGCLXbtGjXrQ0l-qB9nqnSIAm2jslH3kO2FyhQDrcAOa0xxkPxpc4Zw5KDiccyL0RSvB1JWlutEdwxDKvLGKcAbjRxb69Q7feXaTQBZE6Hnja0x3Vx7qlVc2C6ssgpSp_puM4NkI_6kLWUHN_FRA54MINj3xP7tPrVZC1ImLE_FK1oPxmcUaTIYwdnFFO1kPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22396" target="_blank">📅 19:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629a35090.mp4?token=EOdAg3FlGfUIq_iG299lTb-sg6zJkPyZWdgPDT9MI5cp2Fhdr4lBlt2ZFaVNjnvcnKvQ6QPUJI8I3ZDpaKyVDZBKNKrNrmr3wk-ZlZ7mRsDegaS83jsXgjlYbatmbJ6xP1QcJmt6tjL8I0M5ThxRuUEQ4_wtUnyCElGRRq83SLccOpU6aTOyvRMqeqZDoFoHodRggdsvXnRFcV8E1K5qx7egJ7uKrcY9y-SjZSFXG2SQUtnaj37RGGgeWEZlOlqwPhhTPUu4lXp66kDNXAzW-YaR2N9B1Lx6G6K7r8sGq8tZc7GKXP097C1-IBCmReJ3N2Pxuiz0qLphfAUI8YAu8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629a35090.mp4?token=EOdAg3FlGfUIq_iG299lTb-sg6zJkPyZWdgPDT9MI5cp2Fhdr4lBlt2ZFaVNjnvcnKvQ6QPUJI8I3ZDpaKyVDZBKNKrNrmr3wk-ZlZ7mRsDegaS83jsXgjlYbatmbJ6xP1QcJmt6tjL8I0M5ThxRuUEQ4_wtUnyCElGRRq83SLccOpU6aTOyvRMqeqZDoFoHodRggdsvXnRFcV8E1K5qx7egJ7uKrcY9y-SjZSFXG2SQUtnaj37RGGgeWEZlOlqwPhhTPUu4lXp66kDNXAzW-YaR2N9B1Lx6G6K7r8sGq8tZc7GKXP097C1-IBCmReJ3N2Pxuiz0qLphfAUI8YAu8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22395" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vEVciEyW1Xo4-E8IWD_s2B9K_Pf8LdnYvbnFq0oKRhXPMgqTFkO8OxLnMnFZoUJMUtIzQwW_WxhcPAsi26uUt4HiNQkcOOr0L1HwXZYy5sNy6o_o5NXkxabFUahVjr4qK2uzwYJIDp7397_foRYOfAPijuSH8FjR80stGSqreM0cflXbXpKLU8MeZEW_LMVSrnJF-sf8qfodcjk87VZW6vo9SxUKGQKUnq4dqRb3Xi1A6AoxjPlicg5IVlCqu9YHh4tkAZEzabpsEnAcAFqcAvrpx5GWfk2Oid5SlWlPS4NSQGy_7gz7rd7AcSTyw1idbXMIlCDFZWJYV4xXAKVEg3RY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vEVciEyW1Xo4-E8IWD_s2B9K_Pf8LdnYvbnFq0oKRhXPMgqTFkO8OxLnMnFZoUJMUtIzQwW_WxhcPAsi26uUt4HiNQkcOOr0L1HwXZYy5sNy6o_o5NXkxabFUahVjr4qK2uzwYJIDp7397_foRYOfAPijuSH8FjR80stGSqreM0cflXbXpKLU8MeZEW_LMVSrnJF-sf8qfodcjk87VZW6vo9SxUKGQKUnq4dqRb3Xi1A6AoxjPlicg5IVlCqu9YHh4tkAZEzabpsEnAcAFqcAvrpx5GWfk2Oid5SlWlPS4NSQGy_7gz7rd7AcSTyw1idbXMIlCDFZWJYV4xXAKVEg3RY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ببینید از تکنیک‌ناب نیمار جونیور؛ فقط ببینید چه بلایی سر بازیکنان حریف میاره‌. خدایی حیف شد همچین بازیکنی توپ طلا نگرفت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22394" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd0qm-qZZPV-ETQUO27BTwHj9f5GxM4gGSPk01LnnnzlNZY24eJndCPVCEWFlB0fE5A0aIhQZh82pozomJDaXI1P5EV2AWKVd0sFjjoE76N15Wy9Lufq44fI227V3KvFUG4UhQe55LFrEuCGsHgntI4Q-_q9rdWvfxvD0OHWGbqRL7y-MKsYdpOwLhc01iTUQS9kbzzt3Uu91gBn21Ke7icyQPlHcBX8wkx0zxJDhm2NLYjCZu408NqTFprE5UP_rEVKZWfmvhMTyzDUx8jsofLJSw4_fCeZ1Ken865l9n5Nmq2PwOUipALUikvt0BDza8McdMaAc9qPXl1WWz5zZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22393" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_hFD7oZzEj7rpz9wsR-BEvOpvrzShMR3YIG4WPiE23Sw4kx-5StIAm11_bU2nSYhdbuQ8PpP0jDY4CHEFwlDxSB3TXK1qaTo6Y8WhH-7cGNlCREElQCvdC7YpZBjs9p7Q7SZwBdIifOjQgwz9b3P7PiiZh0Ob530-xBdUgD0OtJ6F0WEAotbXI4VPOhQ4KzxYkMNhCjBJHYXY85s6mJjVHCcwgHTzPzGMmNT6tK-_EKILuODbRQklWEDCpAh5llGgqCIxGh3p5vYkh3Q4rWOQRsg6A-Ywtxcb6_dex5JzHm4an-8yt8gCkP9WVfjLNUXiRbzcLkS6oqsqt_B-1sUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22391" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YafPWvLQQkHhYyJOnS0N9LkQzkYydtXwjq9T4ZKXJvjoO9KQrmZtRYSiAbuRm8cRzJqB7X0juwNAuXWW5tR68aHcgpwNk_aQUL8mcqJSy2CEFyOtyCfxSZV8u-qNmqhAOT7aEJ4AToWos-p7Q1NYTlG9OWIDOPATqus34VHHhk8Hr85DjimWwRZOJVTDEP4LFjBSVGxglxpJP05FpXVqh-XzRbvwQnefOP-w0-74OlQDLZDzEknrB_nUfmGtVRGY60vxB4eASD764Pgc88bQv4IFP-DlMwrgZU3aE1jF1Z_xYLeUzys3Z2Gd3J590by1BUhiuBHR3tv3ITUgAVcMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22390" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skdqExMqG85JDy7UowC9Z7jyEKY0XpfLJBsHSnSXPW4CSKsMauwcDkUQ9u9MvNXeCzwheHnMA-U9Egw6xoqxRYCAIvi2oeXj_RNfcUEnRitsU4B9h6tmocIcbRNpnDLS6QAUZtkqWv7hY4zBC8af71Wph_AW5MMkn00QlDhI8tcluvVojOZ4AubuKf0qrfeVrPuQ6_Q7y5ny10lCFI6-eVYwyL7cp9kPv7IwQmAFsU-HtfdJOvkGjt9qsyjFrRJL9jl3qq2TmWYiUGsHaltYuOZP4pfNEZ2vzuUthNwu94B5u576tL3NO0Mmd6hDbhIwxFP_1TdNewUBJeOMr2yRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22389" target="_blank">📅 17:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyyrXZdDUPTxikXX-bF56HUVjtpTLv_aGuOESmm8NGpDyK1f4xQd1lapEnPQX_9aoKbqqF6ycB6aWgoWZZNC4KtQ7fgvWkDu7gd0QUOn_XEXCafh0dFvTe_tGuxEnd-BIo-SN1HUNrgLvaazHGdJkzBmHisaNumIHpCApG4nk7QzJlQXR62BCNJ00z84fqW1jDQQUr87EOzdvfkakliamHWwIhAozDEGC6-J4WVWkBKBjyX6H9PVIPG-3KK_4CCO4mBnH_3YAVswVx2gjFueyfy2o7BqsCNPAYD90ObD8dSMTRwzxYSFoVdWYGrgz7y25hGPtPMfXljXk4bSJLQ4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعدازجذب آنتونی گوردون؛ هدف بعدی سران تیم بارسلونا به خدمت گرفتن خولیان آلوارز آرژانتینیه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22388" target="_blank">📅 17:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRapht_DQXRs1wQ06i065QIltxaSOnFFA0oUjX1rzDTXZ9lzUNciIFzSGGjrqu-wzlVBe6U6p0bPoS9TzU2ZAqo5Zjttqscoksxz6SbtuwC0mTKxa4fg2F0wNJcCSjw9Xk86T-DtmLl_UQHzPa0BkeFWxMJc6qeUBJktMIBrPbgatnuRfnl3ZIolrNrpSCge-FKThvgTFFRVNrpP_ZCfq1fHA1aJR_n98hn5b-j63hYF5hHn7pe7aNhMhewz2IzCnonSDWd3H0aUdApqetBnbkQlFWQe42ShSGOfBDepSkEMP7bxnuvWUUUPKuDrYOCT3vhO_GMfQ-mFQPs4RA8V1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22387" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=wBF5tJdVf0cOv9j5lU58fk_57Xp-OUMYeLAVjueyDP8BAlFhHKXTXqqQ9GcVM78AIOGCLzu9-f3Xkho7xHHpCfu89CrohT4PklW5id8sul7wIEwriWSYdIpocsCpkD0UnChF_WxGs8tSvofPGl_ZzQ_I7IS2fXMCyHi-Tj0R--QAc88BNPYcAwca0zR5tX8DN-ZM4evb32fwEYWyFywozsEx6Qm00eLgp2JyWZh3W7rRXpWlJ-As_Ue6ul7rHuGBYIQGtMuJrF0h1tL7TjpP-paVqcV5ZaN4Hs-eO4mAeTXVsv25Q0kiNKeRJtcJ8bOJEvm1MJP_zEQSdr06Zrq0uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=wBF5tJdVf0cOv9j5lU58fk_57Xp-OUMYeLAVjueyDP8BAlFhHKXTXqqQ9GcVM78AIOGCLzu9-f3Xkho7xHHpCfu89CrohT4PklW5id8sul7wIEwriWSYdIpocsCpkD0UnChF_WxGs8tSvofPGl_ZzQ_I7IS2fXMCyHi-Tj0R--QAc88BNPYcAwca0zR5tX8DN-ZM4evb32fwEYWyFywozsEx6Qm00eLgp2JyWZh3W7rRXpWlJ-As_Ue6ul7rHuGBYIQGtMuJrF0h1tL7TjpP-paVqcV5ZaN4Hs-eO4mAeTXVsv25Q0kiNKeRJtcJ8bOJEvm1MJP_zEQSdr06Zrq0uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگه‌چشتون‌خیلی‌ضعیفه‌هیچوقت عینک رو از رو چشاتون برندارید که نتیجش میشه همچین چیزی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22386" target="_blank">📅 16:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=CnIqAPJeYjE1jf29xUHlA4bjdMB5d2GNSwU4zpDaqk4qi88OmaWVHi2zEjtyTTeB0zRhEzY9zkQKslUp3WFut9oKMVa2imjzZoSJ3Z0Y5acNI3ZE9LcFpJf83wwm5ROaWjgNjvO2TpF-usvryRwqG_hVqqiAb3V4cJ-aywmOhKJjbDX1YWaK0nIjDocq8Lkyyo3iI5jgHTEaleAHKce2H3-oMob-DmA9XjM1ac6QzzOJ5wpYpsaYduFFpQVxbbVoU_q3PSK6zRk-bv7ZjFdnL0PHPGMdwJyGRzGHevX6i5hVPb0P0mVUfPjwkNHBVbIWrszHuysHckI8-FSaNmLkHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=CnIqAPJeYjE1jf29xUHlA4bjdMB5d2GNSwU4zpDaqk4qi88OmaWVHi2zEjtyTTeB0zRhEzY9zkQKslUp3WFut9oKMVa2imjzZoSJ3Z0Y5acNI3ZE9LcFpJf83wwm5ROaWjgNjvO2TpF-usvryRwqG_hVqqiAb3V4cJ-aywmOhKJjbDX1YWaK0nIjDocq8Lkyyo3iI5jgHTEaleAHKce2H3-oMob-DmA9XjM1ac6QzzOJ5wpYpsaYduFFpQVxbbVoU_q3PSK6zRk-bv7ZjFdnL0PHPGMdwJyGRzGHevX6i5hVPb0P0mVUfPjwkNHBVbIWrszHuysHckI8-FSaNmLkHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/22385" target="_blank">📅 16:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qygIZNdq3sYN73f19X5NsftNMfHhYSU3PUYHjYTdRAk6vacMNxzwR4KxPns-6-vRzYlbjptAaze6rr5ZmzymfyV7-Ww2XYTQN2szqFh_IAfABSAaTAGXWoYZax4NUfmJxheE4jZyqptSXcPWbI2LwEABF_boMXk9Ztp0qm39q_2UkzmeGbpb9RI6Ri-Lhyux4SX_RHTyVHA0LMJXv5qTnSfEp3y-JmfwLMEmztiec6gZY7PmwyW7XUQ8ZKFht7T8SDSBx4Ua4NP7CXZQxx90B_YsrUC9j2hGam63yEJFZ0AsmKkAKE5GF--Iw_PsGhFUsFKKLr8x8MR2RvIDb8pWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22384" target="_blank">📅 16:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22383">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC3IP1eMveuH-L4FkdaPjI_EO4XV1NpW0RBC-JlvLPukfXccsJSCiMi2lNcC_jrfShNXhqqrJrk6kH1hkXLjWZwy5H02191hABd-8LB6kdW9t9OwugV4IAB64sqVVGaH7eSjiOAfrl6FjMRmu5pTpRl8z2_a6lZusS7VB2BRc42imwQ5-9QBpoLHhH8RzLQY4ZBtnuNNLdMzytTbM98h_0m2cj5PbyQ7-OiLC_f__l1li1tn9Vj8kCEcpI9HEJs-owbIP4jMdxIxIbp5iDr8u8IY8BUhPntcEF2iDHWb24n_7CjcVkASc08odwtEcs1Ccdh4r7Uq2BYT5qtcwRrTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق شنیده‌های پرشیانا از مدیران باشگاه استقلال و طبق آخرین‌پیگیری‌های علی‌تاجرنیا مدیر عامل آبی‌ها پنجره نقل و انتقالاتی تیم در تابستان باز خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22383" target="_blank">📅 15:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtWnV6AIKzVpJv6n2TDy77jwvB-Qem1rJYFjdGVesKNi42wFuBJJfYdk3r1yTfYdP49IKsarjTpUMjAfXfUqg3gsrnAceQ3zAFVt-hn9chiehzXT6sI-RzuAGDGha5pvMVYrziGsveNGX5mUv7uw96EfCpaW9cWRFwH99WHzcs8lutd5_J9VfQFuU_3brnnNsdw7E6VUedCrNDLjo4S5AOqAY8oj5Tgj4DYaGhYlnvSNJKF6e5BdzIC71GmCkNGEs4oL1uRuT7tTsIWR2fw1R1nuYVUhzxrM-yyelEa2CZOzaTQEfPauxjP-HtGcUnmJUd_5dhz3-QtBOSD3Gn6SCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که پیش‌تر گفتیم؛ اللهیار صیادمنش و علی قلی‌زاده درپایان‌ فصل قراردادشون با باشگاه‌هاشون به پایان میرسه و درصورت توافق با خودِبازیکن‌سرخابی‌ها میتونن درهمین پنجره با آن‌ها قرارداد امضاکنند و باعث‌میشه‌تیم‌هاشون با دریافتی مبلغی موافقتشون…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22382" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBTqIzJAcFn76Vq_CabmqpyY81yEOXjJ0bGxdfbgb8ddmm_iZJqDOtQaqpEbPVC-67ukX1ApINcb-iQIVZsyfbnt94iielA3IxZkmgU1PUk38AZuVQAmRUXDKhKgXi-VHmkZqwMjHrbL_PjxcINxwqbmFMF7UyIX0QHiHMbxXdX7uIP7tn7PGOpzrz2XwxV9M3-2Vc3SZ7LFRX0VvMQCsp4sGXqp4NG0sDU2y7qTUOWHOddbEC1V27vYGDZFAsBlOJU9qH3yI3yqOC_RA6tejS6lp6DQohznkWykpYkWGpmTwUUNrKsYVky0RJQTY2mVp_1lRBwDyU6UJyO_PmZ6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جلال‌الدین ماشاریپوف کاپیتان 31 ساله تیم ملی ازبکستان در گفتگو با رسانه‌های ازبکستانی اعلام کرد که با تیم استقلال قرارداد داره و در این تیم میمونه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22381" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">▶️
#تقویم
؛ 15 سال قبل در چنین روزی
؛ بارسلونا با پیروزی مقابل منچستر یونایتد در فینال لیگ قهرمانان اروپا برای چهارمین‌بار قهرمان این مسابقات شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22380" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6RX8UX6IxD1ff59FuCrABd1M_6gfBcYRiHLH3StzkpY6CGDsDyk1AFoTHiPVkvi4WN3neD6_SO7zquo5J-Ut-41biMcvon1qZDhWsRtTWh1S5bui7UmBA85aint_tA11xLxtn0-0hKuSpg4tLvmylSUldYQV4Yqr298bRjMOzkI78RbogS885Wu1dRlwkSz4N0TxiQ7H6XI4FxC1eUo42WQXPCnDHYO5dYn5YIaAbyBFpgesS3HTfN2D7zd1WgGD7ulUCtLNAzvYq1d8dNtsGO1GVXtFeM1r02j-JeRUsCmY4aMDP749EfmwCJNB0DkBt02S48mjGO8kcGhFL8Rpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ محمد امین‌ حزباوی 25 میلیارد تومان از باشگاه فولادمبارکه سپاهان طلب داره که از طریق ایجنت او اعلام‌کرده حاضره در قبال دریافت رضایت نامه‌اش ازطلایی‌پوشان اصفهانی طلبش رو ببخشد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22379" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=jLGqC_S3X-ja0tEQQ_IEXRM7yVEolcwBrCfMHePVsov2zWqW0TisBo6XTgs3JnnkznVvXK7pZQ_GQWMBxSjcArnrtE0JafhxWnQE-009-LozyEn8PZG-XwCKMe24yNQ_1T_Qt0kCSKNLdmxGLx1U9uHBTgc-G0UVAGPFR4TgY47pFaPEQzlWtTcQi6BoHYyApNW1Zbtd095QuTYvItuLh8Q5zQOufbtAmde0I7jPqVVpuVMNXPZ7i0qjnCOMYXuByK_G8_sFIKNnIXb8HS6ARxvfyuo4Lsyc-DYA8uG7Nhjq9lHmFFlDQKLgEX5NSN2c18KeFyKdv11FZjhRLjnRMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=jLGqC_S3X-ja0tEQQ_IEXRM7yVEolcwBrCfMHePVsov2zWqW0TisBo6XTgs3JnnkznVvXK7pZQ_GQWMBxSjcArnrtE0JafhxWnQE-009-LozyEn8PZG-XwCKMe24yNQ_1T_Qt0kCSKNLdmxGLx1U9uHBTgc-G0UVAGPFR4TgY47pFaPEQzlWtTcQi6BoHYyApNW1Zbtd095QuTYvItuLh8Q5zQOufbtAmde0I7jPqVVpuVMNXPZ7i0qjnCOMYXuByK_G8_sFIKNnIXb8HS6ARxvfyuo4Lsyc-DYA8uG7Nhjq9lHmFFlDQKLgEX5NSN2c18KeFyKdv11FZjhRLjnRMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
نروژ ویدیویی از لحظات پایانی رقابت علیرضا فیروز جا، استاد بزرگ ایرانی‌ تبار شطرنج فرانسه با حریف هندی را منتشر کرده. به گفته فدراسیون شطرنج نروژ، پس از تساوی دو حریف در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی و با چند حرکت حریف صاحب‌نام هندی را شکست داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22377" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qujpee2BTT0paG-YbFPH9M7mPpjPLy2ER-bsUn6UWtVglPCa3vMYcgnletWqvhbV9u9MaGsfSG8NOztxR6ukYHdRUOyZ28CnHBIT9Pb8MI4WnAj9YG6NYUXaTY-4smiueZLkx6CUwwds7yR9nCIG_VtbAM6IneCZH1jHe-zredlW0wa95GRSPsHmLZ1_asxKRq3DMXuGlCYPpgiHuj5sFJE0rFqsOCF1-B2K5X2ueQyvd99JxUJYJXnHhtFZUq1_7P7uNWbalncP3W6PxTvPCo3KQHkbzvfduDh8cSQnFXQWG_5yWJ_X2gp4bgyvM5_FnmnCm6exPDKNPydDpj9inA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فعلی مهاجمان خط‌حمله بارسلونا که ممکن است آلوارز نیز به این فهرست اضافه شود
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22376" target="_blank">📅 11:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxZauQ5taDCHT55uC5LYSH4ipchCH76RpVobtioqtDoK5KZOa8wjWhm-mETGMP0YXEuSp_fS0fKIHQUygELk9rl39UWQe1lwxLfux1OSf-1s9ImyPQ4Os4mMNQ6ZYJqQ0Zqx_4z-j_lrGDdf6r-pH220XmrFxm6VfUXF3wbmKwz1-4qxBkkvkH_JdJ_3l1OZDE-lDIXJ2X_TCtyL465mLQ6pn2DEZd9fnYm6EXGwv3OsDY5NXqvr-0ORYMELLqOvpsJGWBqOqvV_qndvDFaEoGOWrfkLsIDfKPgkhjzkJB93n_YQ_i_bQJiLukPHAKhGASnPqDEA2XX5tF9SZx0tAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22375" target="_blank">📅 10:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW9rcCUVVtMuLcbxYKWo2W4HCT3XSrQXoP3fg2U9K5xTr0qYUS49xr55BOTlvRoS1s4A2iMt-3Fd2gf1QX8SYT0G38BJaffrDJvIYWcb8TLWH0gkTLF437QX26ziDX3G4q8YcbKzQrNF4UJoGM9FErCfDoW0sm8lTT0GBym6ICtlIZ07Jjr4apwMVFoF3AkfqFPB9X_T6wvDW0V0RxayZKt8K02rKvC-1381fT_xIBf7JKS566OKyr_-FpfNMoWjP1Hn7KumJwyl4v-1LzCab1k6rfvoFRbxk30RyGsLJzGfxVR8NGj8aJYVcZMH7tyhjXlR_Ba3z9dFVFGEorkfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ کاسمیرو هافبک برزیلی تیم مچستر یونایتد، آخرین بازی خودش با پیراهن این باشگاه را انجام داد و پس‌از بازی‌از هواداران خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22374" target="_blank">📅 09:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PODm4P_hyTPAjv-AeU9d0ZEP4kmdk1-UgHVimX19GmiWcIdaA9clPG1UFz2s0cDRJitjze3RIrsXo0hcDBr4pdq0Qg8E7FMMLe9qSMmH1hsB5hcRcVL8b8lep7Bb5uAuKUJUo0BrmMR2OPcvGAAz-sexlTw568m6j5hU5_oYhrF2zCzzwW_bpnFv9nQBedOePOOV3gDmVADVgvI1znor1Fqw5hmreFtlsBYAKPfkcS3xutIqQf9qU4ZyJ2_pns1p5mN3Cs3xs-GFr-Df3iKdYyIxnJ6OZ6iEdSZaPBReEw46NLEvihfndLaVtpW9sb23ypRAHCWjqaX3gQajQvJeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کافو تنهابازیکن‌تاریخ‌فوتباله‌که‌ توانسته 3 دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22373" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=jF_5-ejSWh_aXW1czFBvh7TWjhHiHAc-cEehbhq63LXfdpA4z7yHyuwmFsU5ry6jaXRkQk7LkkM2BOKModnToSGWFGc-fmxt8v0msR4Y0pNBS18MLL8C-OxhiTtlmsNSRmJ-wERSNVkqonokjRcXKC0DPkdGZKmC2VtLkZHT51FvglZ99ZfeDPbkDjYQQjFcVPwZzBL7P3irW1bZESXOXujIQikzrZvnPl4VexjOY8B_TMUiJ1uBkXqJFuAPL926nrv3nKyJjvN3zvvlfh9YXRhQrd7J4drGMUbj2VKMvHVMvegT_rTHkj67HSczbBVRDH8DSg-HD7UKU6udJs6olg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=jF_5-ejSWh_aXW1czFBvh7TWjhHiHAc-cEehbhq63LXfdpA4z7yHyuwmFsU5ry6jaXRkQk7LkkM2BOKModnToSGWFGc-fmxt8v0msR4Y0pNBS18MLL8C-OxhiTtlmsNSRmJ-wERSNVkqonokjRcXKC0DPkdGZKmC2VtLkZHT51FvglZ99ZfeDPbkDjYQQjFcVPwZzBL7P3irW1bZESXOXujIQikzrZvnPl4VexjOY8B_TMUiJ1uBkXqJFuAPL926nrv3nKyJjvN3zvvlfh9YXRhQrd7J4drGMUbj2VKMvHVMvegT_rTHkj67HSczbBVRDH8DSg-HD7UKU6udJs6olg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های طعنه دار ابوطالب حسینی به وصل شدن اینترنت برخی از کابران بعد از حدود 90 روز. خیلیا هنوز نتونستن وصل شن. از 70 هزار نفری که همیشه پستارو میدیدن 30 هزارتا آنلاین شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22372" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtoilFKyJ_Qjv6tWgO50Wc1a0ZJp_81-gNA2spoxWOKLdstLRuntOlGw1gjinX41SjKgaR7A4uZuEHMCLE6YpJ79Yj_H664KqS2N_izs_5gtANSnYNX_8fInfJwoM5RIpNgsUx5InQMXE3l3pjYxpfP6oJSj-X4-VJD7GP-OtVfCvnS6k91FeGoHzc3hFlrB0UA6LMYR8TBVyhWkTDH1n6aqMC_02LV92QV5wF9vdnhjTzCbIvZ_JRWece_Ea8wlIhoZXYW27-8z7dXpXReP3-YbhVOyqsxSqyzoaxfkAs3LCWbnR0xiQc0RR4kFavGHbtqhwrzKW0cx6nko-rUVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmrhzxMwC-pM-jctc0ToRfjJbYfS88CKsNSDWsJW9BS9-0XFtPnmGu7mOGsd2ISovNFKpQPh_yzuklh3sHtn0tK7nMsRAZxr6kGLQcY79yeKD4c4Qqh-id4ncsEeoN5R3-rEvh0iE755vaF3WN5K32vBhK-wK6QJQrpG_SaCFEcPfrUyAMGL2_hI7GlxfhYN_z2xblglGYrji8OjPPv1HyGWPpGtIj5EFAv9Gf-YvlEyIw8FoMVqjHASb9olcfBL82HoKU_15XCu9nKME184ltjq9cY0MTA6Fg_bsxNorqusKnUbwm0V_bkSY7Gu82j9MKCPs_4J-FUfIT0Jd6_3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlANFjxiNY7_N8OSc_pyjn_QF52OZT4D2BtBtvc1BL7NoGJzv1klMMlt8m3I7VNblSmrvgTjTIq2RAlb6_dfBM4OLs5POnuO1JzG6wQBTLUpAASMsM5riH2CS9mFvfBM5fgrWFAKrAl96GBX1bEw5VRd0BQpolrVaJo-9oup4KGFIUtxWhBDlSjrvz1UbUX0DN0nN5ROlrCnsEuZfVc6GIFPf9n4xAa-3gbEBrgkTmR2tlL9sHSURcSqoz0_rwHrQzDZLtmsWFMtaKxtmTDtPBE_ruFH4Ch5ts3MZhgBix7jvzkeKFUX1nCJ0l9H68L-Gp6uysvckDBLH9XaTEmDHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=XENyB2asHMGdsuCUJwZsUDov3rmwRJipHUAG0lKwv-zMijhIQ-MrRpbdtF_nXAJpIGemA9UWS78XH_VzOm8ZjZmr2z6ovXRN2x9hsLa5qJzobYWJEH-BU5G3-joifg4hWsEJiKQDSxumcwpW5uk_At1bJrTLHuWI8BIFlOP-7gbHA9bl8XvgJtGtwq6pfBrXFlBgIz9CXCrVeNStG3zXgiZ-SdlGRJbiO_PdSJFAso_DVM4fw__hkbhvPVQtfgOUrEUcLfx0mU9l9JoUd0g5mkYvG3cj43tTxPMb0dULeJ6F2jw0MTniEH9jfMdSGj7mKwgaozy1C6ME4rW6nV4K4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=XENyB2asHMGdsuCUJwZsUDov3rmwRJipHUAG0lKwv-zMijhIQ-MrRpbdtF_nXAJpIGemA9UWS78XH_VzOm8ZjZmr2z6ovXRN2x9hsLa5qJzobYWJEH-BU5G3-joifg4hWsEJiKQDSxumcwpW5uk_At1bJrTLHuWI8BIFlOP-7gbHA9bl8XvgJtGtwq6pfBrXFlBgIz9CXCrVeNStG3zXgiZ-SdlGRJbiO_PdSJFAso_DVM4fw__hkbhvPVQtfgOUrEUcLfx0mU9l9JoUd0g5mkYvG3cj43tTxPMb0dULeJ6F2jw0MTniEH9jfMdSGj7mKwgaozy1C6ME4rW6nV4K4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تعدادی‌از فوق ستاره‌هایی که جام جهانی 2026 آمریکا آخرین‌جام‌جهانی‌خواهدبود که در آن بوده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um0o9jzw8eOYO4XtLLb_rK6Gj2Ds2pwrlBWB6TNohaKN0GSj7hmjFI1NNQ7RehTzNn42fn_hrej8s7fl3iSEnUqyCD4JnjKpYBIH8L5fbVeS3yxss1LbXLNgnX65VKtxPjMHcgVJk7ouZB0ZreyVMdI-2ezuKwZHxKifg0Ym-wFMn2mYWgBuP02kHbaqVdhmwHj_nfQx2g8J1fgj_N2YUgy9HUGX5jmj3_frhEQpZxNcnJaRaF2VSbkkn_k0xMerwqJZDieb-DPLedr1yoLkO9rmeObkyvi8QvllvI-pxt5ALkDvt1aoKb1kdxsXCJIWCYQrzSpjTEyz9LQlMEo37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه هتریک متفاوت و قابل تامل کریس رونالدو، لیونل مسی و لامین‌یامال ستاره 18 ساله بارسلونا!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22366" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJxR_sgxCPNpnrSuCqpIqVcdngrunTwAvmq7t_B5A2VA7JcEYx5JNsWAyAqkHh4rAltVIpyYTaUaTZgGvuV9rcziKIE_lxFIefE6-to3WRrnXZ2lZnbeu2E5dYNI01lba-9q-drMdnvGnaZyDFODCd9umqL0gjNs1-H2njPCrmNLDeJG_Rl3RSyJ9z4bcDnHJWMbXuEWcK7RLVCmWsMjo3dBxZbpDM2LhHa14lY3xkp8jrQLgFJU8GRlxsDhOBz8qgqbdxf9BAPuCyqFfGQPkCi9Uq7gUfXHpjcd7dKn8Wb--kE6yT5Z3EWurmK4ylo-SZT1dhaGvV63RyuK3YrDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق‌شنیده‌های‌رسانه‌پرشیانا؛ نماینده محمد امین حزباوی بزودی یک جلسه با مدیران تیم سپاهان برگزار خواهد کرد تا توافقی از جمع طلایی پوشان زاینده‌رودجداشود و راهی پرسپولیس شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22364" target="_blank">📅 00:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2vXxGmzNhBCSb0TOnVjtPXTftsCnXsrrXUT9x-QS6dShB1V5YxKQfvHhW4gUKEMuJkBXmPwPSf2uVIVLqKALbt5zwCX64ozXX8hyNmD5lVp8P-zP6TILcjAdMKHrGdhpfPjEXvS_xLJJm75sTfPUpQu9EK31sCh-bevdsA4O86zAkFlPhSzbK5Dj9_9bAaP-l_r5T4eQaJN4on_sNArYiHmSaZI8HXqW9obkO6ESqsdLC_Y-YhfjnTPvALoaBoxODjsF7jjMEt7DsnR0b1hKB615Ob1mZVMwLRlc7mbjAMkyo2G3h1Z_JH8Ons9ZZQbXAsVkw3OMMU47qXC3A-Aug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بااعلام فابریزیو رومانو؛ آنتونی گوردون ستاره نیوکاسل با عقد قراردادی رسما به بارسلونا پیوست. هزینه این انتقال 80 میلیون یورو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22363" target="_blank">📅 00:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UslMx1E-4_28bwmTKogVp2JX6VAoXg8OviNWsCm11Pie2trz7A6Dcps18sRNRadTj7Vy7T2wZXWMUshuNmoxZWlzTrNFMkKhbTmCyYiMrWdOc2mq4ur_92X5EPOeZe_QFJoR64nBRZ9mMTc1uhvvZewMuVB-o-LrUZct_QaB-sCHk3bHPFAaXXhF4CncnFi1iHGFSCSUjHEx3_9RMDf_WCCNEMw11W1IeFpBJNV9BQeaRZAnpDU8GONg9_6OfE-HWpOOAcGbvMFL-7htpBlWyCs6YhL-5cfdd8LFzhbXu95hwHbzCtSyWZIRaqIg0cwd-u-93SDvl7twsy7LXBtfVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=GnXukwa1zfMeBi2oNkYnLb76v2SFgQYLKzS7T7H1k54LEkXsklxaSEaDctKRXj7toLqF5ujlfvJIyTMlomWvzK49ywXnNTsBYgnGtOeIbBYrP6GynWs6asNeUakROzZraKVVJpMvx0L03QW35ShRlrgYTOyXnWL_seHWtBw6oKXy9iETkpr9l4WmgEakc5gb4fKG-h0ltLZSgkT0Qmm8CLrlZXjnGDZXNWHJS06nd_QgUu1HAnSfaTWjpwwT42v9_gOAkjAOKf5jNMzDr8EY4Hla5ff9Y7OyQ0cI2eD4GhuQFaNWA0R93iFsnRFH_XQHjZF3OoIlz-xR1i7p2GP1WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=GnXukwa1zfMeBi2oNkYnLb76v2SFgQYLKzS7T7H1k54LEkXsklxaSEaDctKRXj7toLqF5ujlfvJIyTMlomWvzK49ywXnNTsBYgnGtOeIbBYrP6GynWs6asNeUakROzZraKVVJpMvx0L03QW35ShRlrgYTOyXnWL_seHWtBw6oKXy9iETkpr9l4WmgEakc5gb4fKG-h0ltLZSgkT0Qmm8CLrlZXjnGDZXNWHJS06nd_QgUu1HAnSfaTWjpwwT42v9_gOAkjAOKf5jNMzDr8EY4Hla5ff9Y7OyQ0cI2eD4GhuQFaNWA0R93iFsnRFH_XQHjZF3OoIlz-xR1i7p2GP1WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از عجایب فوتبال بانوان در لیگ MLS
؛ بازیکنی باردار درحال انجام بازی در یک مسابقه کاملا رسمی!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE73I94mkKUAEquFB7QZSmiJi1v_tF_5IZ6Zn8Zhosy8ECrp3O93VfmeNTZ3NT0DJ-pK9_S0XbK3D1ImZ7cj5R_9CzAECk8AdtzrbyK8Uy1GZkEfPvaKOTKK2GYovfFD9pw0NqDm11bFPQB9ljQ6N9tshRH7RTwHZEb9Tg0ZShJ4TY4PLep2Aqlp6p8Fv_DQom4PGBHaBEd81LqohcdlutgRuU7bj34dMlBVkiYo6e6EL6NImOUQpojQuzMAKfQQ-xbscqE-GV_I_tqK5PRww-fACV1R7pazHnF_YPuoJ7JVpNxAyKPLQ4a8P2FBnKlno5DbHSLDFa4SajB98hRjlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Y5xzP2ClQAWVK5PbDoVu1kCW92rKTZLeIXPxkiPbSvBhRJog6yqHkq_A7k8no5sSWLh7GaRkcCiFKD6gdMp-yVNlzhftatC0NqLWN8QM-mv_NjQAkmmnKqBEEnK2UbnF0QtzjcJsMpBQVNav1BgMrwS-WLG6U9LXhf8tbvesGDLWXKAjh06_yuPuNAj3lJhOU_g7eT2G4ypJ4meIRbZy3K7Z1AdZ-SZeLyoQev8ro2UYrxieObTfRaWToND8v32NPUEn9TR1OOGQUjkmHFU9p5N0tAwbp76X775_O5DlA8kZjjCjtEiuIAjaAiAwOkl6q8mOeRbQwBYXlvZX0RYNXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Y5xzP2ClQAWVK5PbDoVu1kCW92rKTZLeIXPxkiPbSvBhRJog6yqHkq_A7k8no5sSWLh7GaRkcCiFKD6gdMp-yVNlzhftatC0NqLWN8QM-mv_NjQAkmmnKqBEEnK2UbnF0QtzjcJsMpBQVNav1BgMrwS-WLG6U9LXhf8tbvesGDLWXKAjh06_yuPuNAj3lJhOU_g7eT2G4ypJ4meIRbZy3K7Z1AdZ-SZeLyoQev8ro2UYrxieObTfRaWToND8v32NPUEn9TR1OOGQUjkmHFU9p5N0tAwbp76X775_O5DlA8kZjjCjtEiuIAjaAiAwOkl6q8mOeRbQwBYXlvZX0RYNXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoQuNtyDuEX7n9X_BEObYtB6rplXNVnpSCP0faSXeSZx7w3iilj8oZ2-nST4LNyKVjtOQ_sSlS9fthJWzC-p0pFOvjmF_6Z4xHhfpqj9BFXRhB1wjbAZ7OKss6jGm-eAzXtuJGUfs1Iyk16jpvN20pc6ItlRTFqgJRH6v1S8n9QaKQ7YRRVZ6mgREPqsJRik5Thd1BckOnp11FpF96bIUOBxrE8Zh5p9YU3C8TWsuIYl-1emTfunG0sAGKPnhslrZa8aJUYQcgDR0dEIZ5zXETYtXYqcs0aN5G69vEzj3l2qrRlAdd3wlbOcp2tyEI3GJPhFNUXAclsYvsYdEURbCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRcW1NrL-wgC7-hzNisBqKSIFUheEEMlhFI9_GG8CuotCEyCZemT_DEBk01chocIYTOlZArRr3d-WPZJptPbVsHb1PUaLtzLydQZf6SGOiuHuQ_SYhbKSH8o1YBgdazoo_XGqwrRzPTEv3RkXCgPj3DZ-Mdd23-eW0YzFs_kR2BtkqdkzGZv29FgVy8Pt8bjKQ3ueyCs7gSgNXRI_DzqR9akNfnqGt-g4TYiOiTsAT9HvTGpLrlwPNUfOmyyfTy3EH3cZlcQ4VJ_QCMddv8mxAY30TrwIxvz_9EoXvlN2PKQ-OkaTUcNIE6moBB5uQmKc2HgI4FXykcI0xQwmXIhZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cxnduy5ZFerzr4Ib23C7Ax20JpH3PAIIsQBvDLFuMj_zD4CHdooPSlQWFuxNAOifp19aFM7VJenSA_fUHY3wDrF2fpuGyUY1gFWRFVf8lo4M1Udu9D-4-m8x8v2M53UTVTUu8ThaieEHCrR9TOQh3xqjgozaHIke8MiFmn2aC4jlhFwwyLs4kh6Ibbdqe9T30VVKBDScoXr0ZzqP6kaLDVwX1n_kcPkxRsdnp05d_qLyW4XvXChLDoAszS_FXJ79lyOsPiZnoDTj-C4vuAR5Lg6jBI5Wqq7AHDttCXFwriHT_cKUtCF3FB_T2ve9-z4xU0bc3hJwNHLiXqJ7QdnBIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2p0kB2yo6MdkAN-SR0IbojxxwUoHLYa91KifQE6ei4eavH6SELxqmU3mjXz9afYSmjzeXYO8HjUsCRJuAStbilv2Q3mPZV9v_2nxekzuEwAriXcsqmsWgdAwGkCyaBc344xHsR1Y80DcNpY1L5pZwhrO4J00mVXJ8bzt1MnYzYnWmWGoSfQWAzAGttZjflBuxk0ji3FSmehlK3iL7ixoMnr4Ao1pjALiWgLvh9RZHa6RsAiNp3qDAjcmIaj0TobD7ga5lB3OTZjeX61vGvBGMXWB-6Iz74V2Y8F6eyDG9CCYG_6-FRea4RYAJJ-JuW2eBy3cbC5nvWKEq_9a5SRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_9QRQp11zZpLwNbO0vYVt1l8sZ2WdL8M8stuzTKTseT8zQhM-KjXHPdQ58HoTWTM_mApcrVdlRA7-Cdtjld89m8CeMVpktXCbUIBdJi6ZxgNnsxf_wCdXx9qQY_kb5j0Isuns0PZKFz5uVCIYiPpqgk0C_pJ-ZaOUL1Rr8YLkoZ2VnA6Dm6zK0luy8ArZ5ceVeEdKezxVxVIA9-Ru161AYOrkHFt3R2QheXxogT5ikpCr5zOv0qKp9d9XevPJ04CuhUCIfSNoQySJAm9a68zcSY9dOggp0Zj4mFRQEWZDV9TdMLL6AGPM_X8AJFrHiw-59_z2bWleKyvv3r_Sdwkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=UOQDwiCHGnYwVZD69Wyyiz0JEGzdde4VRs97wzok67J-2Brrz1XbB68Hv_5-oG4TXUghnmiQxoycvQjjodiXm8rwOf0zpd9AHngOBXEoQi-Afx4CMMjbwFxwlSkqLmfJDGBfcUeMqmivNkxATVEzhhl2e01aGeS0-EvJkBMco44TW4aVRr9kgaPk6Bs76B5Ior83rgLEMv8vDMSmqsh58Yv2DBfT36xWuDktcn_ZSsv17QMQFS-3sWNyY_QzahXhe3UNflWGNu5rsOI-HVT-3NccnloOZTFnD_IkuW7j3UH15O_dYPPDlQsMGt_b1nVSJ5hgFcBJfNvb7z8eUeuw_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=UOQDwiCHGnYwVZD69Wyyiz0JEGzdde4VRs97wzok67J-2Brrz1XbB68Hv_5-oG4TXUghnmiQxoycvQjjodiXm8rwOf0zpd9AHngOBXEoQi-Afx4CMMjbwFxwlSkqLmfJDGBfcUeMqmivNkxATVEzhhl2e01aGeS0-EvJkBMco44TW4aVRr9kgaPk6Bs76B5Ior83rgLEMv8vDMSmqsh58Yv2DBfT36xWuDktcn_ZSsv17QMQFS-3sWNyY_QzahXhe3UNflWGNu5rsOI-HVT-3NccnloOZTFnD_IkuW7j3UH15O_dYPPDlQsMGt_b1nVSJ5hgFcBJfNvb7z8eUeuw_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3oNyr7hGb99apL0JEY7zitNAGwV8XnT5hlZZiZ7dIxygPjKFH6Hsrh6F-wDVAGl_1Vc-SPfLFlWP9OKYS-nWPWx8bxq-HYN3zvRIp18P8kBuSPPyZH8lTs21OeVlqQNv_23YAp4ygiDIByE28o5lX8HiCzK2vTxvNjdfnvZ84mmYKxvxgo42mmp29_h-VT8FOjX9idhfWq8bg7kbdouW27nl0qkPRYlNbtjf_28AO-lHIpVCA0To1E3VTgBT-RnMzMtl6nRtxefz1KQiVG023UA0hxmh77wwofY6uFnxK9iOUrUeuzHZx9BQbjITslik21_fzDKudmlPFl12d7GJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBzJsJHUywi7RDwQmGQuC_pXBhgOV7gzledumxnJ2EgBhU77JN0qtchHknE6gjAAk6fj0jisvlxryKJDfpSbpi5evZdPbszAQROnlo2LptleD6ozcSfXSagp-kjC0aN5VQg2XBMC6iztzYa1Ju1Tn04RGhLLFKvJ7ac6eP1ht6e7ozEAvhPrklmMCigvABx-aWFh1DZAQk22_ktu31hAqOtyCGGX3q8MkhUgyhIYdZKwHZsj_8Ue6GohglAafRCOH4FOlvLUAZf8QiIM8xFS8pGdZ897Dq6c1ULVharkSXD85PQ-F8FRtGpcb0gGVWfehZHwsyOfDslW4LFgjQDQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=r8pel-7PsqSaoBKN23FQXwDQ0n9gVrYe4NR4P_U3HY7jbj-WGJEkH3s7tdG3sAKI9ltWIDGPxHO2enr8sJ1Q7qPIucFgRjkX7mJWMT1u7ziluMs9LsAgnaJGjf8HzyqQVSoV8jZ3Ozw3OntGXbs_QaE4Cus53gBpE5XW7Foy6E4ucOGYd7ybCuLdMoODDZ7cKr1YfjUXQqK1s153qturF5nl_0nXn7a3sFLSlxxeyWSYWnZBPQzQRgUrylxkuPofN9oQA7fJOYIIYnhJgwQoIbswVVniY1QntV2Np2xHwOSO4MtMyrbVQr-7XOCymiqvV4TCeeBdlqezyoG9u-TBPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=r8pel-7PsqSaoBKN23FQXwDQ0n9gVrYe4NR4P_U3HY7jbj-WGJEkH3s7tdG3sAKI9ltWIDGPxHO2enr8sJ1Q7qPIucFgRjkX7mJWMT1u7ziluMs9LsAgnaJGjf8HzyqQVSoV8jZ3Ozw3OntGXbs_QaE4Cus53gBpE5XW7Foy6E4ucOGYd7ybCuLdMoODDZ7cKr1YfjUXQqK1s153qturF5nl_0nXn7a3sFLSlxxeyWSYWnZBPQzQRgUrylxkuPofN9oQA7fJOYIIYnhJgwQoIbswVVniY1QntV2Np2xHwOSO4MtMyrbVQr-7XOCymiqvV4TCeeBdlqezyoG9u-TBPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwotTzfqJy6UX_f0Spao7bSHXxf3g6ZtI4TkYU-6TaLXIdnqBhnuUhLS-XIbILJ1La1Tl-hhzrsVcEGqt65oeAP2pPOAGoZ1ryb-zvKKHEMkwdWz7cVeuphFpdLB_lHIenrEPx27xlq-Q_GSEAunlubajNzYrkKZRAZqTgsWdZukeHuRhWXyd7ldl5QmTDZaJnZHbQWn6rL4qvUO23HEnmqKvMBqu8sGuTxTYn1YMjTGZ5DawFvU78fJsbPtHGUIiC-5lMk-GKdUhOVkhJWU1Hfu0f5oWjxl78dCzrGa59bhmY-C3UAThNwikwQ-AknIRSy5h8MzJlknnCeosJ2HDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm3Qut-Kzsq-u1CviDr-k68b5EAmskVxbdxu0rj9HQZvZoJTStBd_5YBysS-McLMjLsjDrEwBd7V_fB2CQbdvWlP2nG_sXL0Is54HohsZt2uKNBrzjaXPpQxXQdzYoTCJPUxQ03MmKGS2goXtgnDIb2UPwV9zzPOYiA1_Kt9D0XCtcjLScDQWeF8tF10YcEVLQTbnTtgjvuzCfQaGkpSOCeywURpnZk3YD_EkcN2vWH7qfWec7JRkfOldD6A52a9yoA3qr5SAEBGjnz2G3qfKZ3Qvjd0Ie8oSIEBIL0BUOhCFW6s0TLmDACOD9kZHryieuDPby435z66TPD43PbmOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q--hpyKSOCkTzICnv-NcO0Z_ljO2fBR8F0q1Wzcsby73EJB5xEh-9XL7h8YnJUZwfr54pbHCe8_AHafVl07FppEAidk00ekEbgW5_Ct5zC93G1qQutMviHSXlKV893L149JocYQGXN4fsxMUA1W8TFzuPBM3EzrwP_o_Y7ZBMGf-C7E8Ofd0-LCWn2SrHV8WNd94J0F-nXpdJnYWRL2wJtmQvYApW3hF_eSjs-lKCTVumzpgJ628zWF-5tzEOOg5MZIRsC-3ZpqsH2yFRhO_LmhEJc3zp2xG1gwzXr2rUHBCphaffhLm-tkc9FwBF1iLGOhcZmyN32aU-p7xJl82Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTf650O6ulZVDTLynNhmp3GzpauyxSNp2Pt1ofIHW8Vwhsxt3uQZrVKAGPHIU1I9n2MrBHJTKwAHgfvz5wkh_mzMvwke2hJKUvWdE8ueSKpNalr7nCdahQf8NGQ59S6CTYQG6Kmzj2y4I-e8uaE6dv04ABpxC0RG7Pp4woP5V9ncmcUoxBFYiOgoZYXx6_QLjp2qYISpbM5V39zaInmRuZ14LHOfBW9oGFVhJPtoL8ungzvf89qFlVJMi0fj-xeN_IsMjgxRocEyaAFyVnxJSr-2CTd6r9jydGZ0Ez9ClyUnz4_6rObXbj3Albg0BCutp9lvJRnn713zjL-L7ykWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qet4tIMU_tsnAfmDvqHMe8zZKe9mBbYKmLMjXn-jfCyjSqdjQLiHrxy7Si573k-fBX12YWtNl-1Mto6hO8hmbSBzZqwTVt7STzcoiXwIfOglevHo5u1GwXlcP6a_C4BGlZXMAy7RaR-Q-g6mTHMCEfTlwAkc53GUoDqXTezeB0BOxEmQYgg5aWmGIN1Js2sc_MuyvBb8EBShX1Tacz9enX9vewla1D3e7TgWgVMoM6ZzZRyWymiB_Qfr5KG9pAPTOWEomA6CFI10Jc_GlVBzfVUzFuDSQzCRbT1exBSU4BiSJsBEWkxO03g2mBgC880dIOz2G8Y8z1P1Lbci8aDgKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mr8LIbB3A2AWDcA4vbDUQwCW0a23dhC7ND49GoXUgTXttpILNGbOQYY1RWNVZ6tuzETj9Fq4s5Tc8yf1slbIhQbqAVFKT29shrF772nal8qkipSp3f1M3P7PFwaXTznkfmHKa9Um19N6cvZ_8L9ZOryy9jaXXx0YY0ZN6Hbm2f6dZeoBeYKJ--UErnw1t92VMw62bIZxR1dDrT1HpL-4kutegi7xdI5S7sfA6kuh3vIPRBlgpZ4NH8OMzBcbn6XJ0zlC8sdpczxSuBpO5TBBMFBm1fzABAvtHoy04owrO1Mjsbhd8WnmXjFxZ8kp0iXD7NEXoOhBXXS2UqX4dCmefA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3MmQOMraQ-M-TM_uBG5okR-W5tPymS57Ofq1HdJozsXTimwsAqhjEPH996XjseUBFoMBhwiwNvzur4rQ2W33glrwHcyVs69T62Fwfs7rem1JGXKzzA1NKaz8Cdqxo1f3zfPYulxFD0o9u3DVzb9USYVreG04kQw421S5qeqag-WCyTeuDmDa_7j9emcF_cUSf1RQ91T8kEt-bZE0ZvVccNPnR1_R8g-EInnNWqG-TfGdgoL6plZYfkbiMG6-SgDbv0h6t1ggaIv8f59a7s3W24THEgpdbZde0MwyLGbrs4zplmPSvtF8Sg3acqL4uO1xDt3W6EDj5ZRklOthBpZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jl5g7qNhfoU6aH5wyLkY5yhwoeubUMiu1LUfIz8LR0TvmRvk2fQyOOwEcq2et0Fjb9UJE-biVf0NpGo27x-S6NSYq4wRIyOVdgQX33dW865R-jLY6TGik4KhjoknDIVGA7Mkf2IwvaE9MFswWSSsPROwWPV_DhsA19k8sQvp8Aht3YD0TrxxzyzN4B1gTUHmfOSlhbcnlqBess1IHw4yfsvXXYaaphf6qZ7EwC8mP9QV86cVNUFh-js8kwxtAxyttTQyQTtN24EKPrp8fwBpvYuPkPDjR0Y3DCDcaWt6mdl8DiX1p_wFSfFuC0g0DgPBQt6yhQF7nHZgmIIIAhGRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db2r-kVYn37rWaEh8J4S9Kexwsp8ryn-bkl5W8q3kXeIGfk1lXSvD_kFrx1uSKeFh_VZQRx7AFikXkvFkwQWzxuI3hYvGZ7eV3pzcI0FfsGSCle8yliJSTgHCPMULz1YaE6JL-i1Ncm2Ei2IgflI6r2PB8yJfeX9jWacqaqOn8JuGCvXjDKcTBOdKsqZ7pVvWfrz4TSK_WfmG2B5dhnfyRcrnSDLcmGkOj_hCUdxANFBSOE5p-GTppY_Kz2a3gTq31-mtqKP4uzKTeTeMDNgKV7bg3cDbyY12wXpSt69w1W_XmNVV0bE2wiLVMkNijAsRu7ybNatfU6VstWIR-duzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DktP5WHUsWMyqIBq2wmPQMYSHr1X71YdfZuT_O5j8UfUoPdxYrJXMsIQznHtU4k3Zrf1wG6TL-Z5G6r4dCnndIxA7lS_E4yoEzl4YRLqy7qpEByUdKfZRJGGwAtdSTmK82S_3pKX9hu9R_T86rAeDyDEJBl8igmzITBCI7V7lh8EgKqTneaDUNXKFUzBdYyNWd6fTzZnNtlw-u1UxHpiQf1EFZl_fBnrvk-wReJMY_Kyo-pH4OprIBVesG0daHJD2sbzPyEplLTwF625oaMSVx7-S3FsOfwz_FCpBH65HWvpv2nmd1UjLfwVQSw9EQh_3CJ2ZMMYd6i9T4iP_isqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=etVijmI9YT-_e0D6NXLb8CSr2BkiRqijiMS93KPpBRANjFaoICFnz9qZIFrMUhABUA2V8QkuUJGFrSroNKfdqRsjMcjs97WVEPB3-bnKhZXRTOAn5Pnxp9-5vld23gZ1v6lU6r5KfvawlO-E6a7FbGOv9SmJRdCEV-Vhdb2jRxeeCQ1bxfKyFu4xYRUIjNM0trGG9nA2LgUXxJu1Wv3wX-CfzuQG2mAj2Tvs-ACO95kJwuje_Hrsn2KaIZtP2oBfGeGnB-tP6rXa8gKi8nwhqgOMfBORKeM1CTut41F5v_U01fLjrOru-X-8oqHNfykUQe3ofiKUlxmQ24IBR37gGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=etVijmI9YT-_e0D6NXLb8CSr2BkiRqijiMS93KPpBRANjFaoICFnz9qZIFrMUhABUA2V8QkuUJGFrSroNKfdqRsjMcjs97WVEPB3-bnKhZXRTOAn5Pnxp9-5vld23gZ1v6lU6r5KfvawlO-E6a7FbGOv9SmJRdCEV-Vhdb2jRxeeCQ1bxfKyFu4xYRUIjNM0trGG9nA2LgUXxJu1Wv3wX-CfzuQG2mAj2Tvs-ACO95kJwuje_Hrsn2KaIZtP2oBfGeGnB-tP6rXa8gKi8nwhqgOMfBORKeM1CTut41F5v_U01fLjrOru-X-8oqHNfykUQe3ofiKUlxmQ24IBR37gGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdcs8IIJJHYwZEImBwGbugkuXuPTdWYwhGIX4UIql0HezZQh8zcBZTtqn3sr6SJZlueEoi8nPlbXG79DjQAu0Ow5lheooXo2cD6L9QQkQIWyXoewi6Lc6FIPW5uVkkXx4iqL5YOzN7IbiZzWIJu3ejQkChq_rwm4bl2-LG3zjoA8NhQAj7Ugij7_YCC-ThhxRT0Yba6mOAl-hCzmDFAolAFyoL03G3HrR01Bd-8eBFTWTCk6MgqHfF9c_wQ0gsh6HeaknJv3eJ-Zz1BkCWwxY3Xrrdb1ROPUT2wK2SO6vPZLOIRfD1aCbxpFG96SrsrXcDDoI_Hjxxi__-NZZdB39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwmhzVqpSg02A912XoZFpMsvJRpqyDtUcLlzC2-qJnUmvwQxhtrOcSBUX3QeaomSKQAyX9rS_d234cuXw6vpIlffZiBpqGZsUqeG_PbUp0nsYNxQHRyFcmeu2RAVam8JcRjPRIEFrk3t74sIdPMdMOIyTMFMKXRcmJDkk91kp78Ch9zmy0LnvYCwSiDIU56OCjc8X_QnTAmgJlNjPmB2GdJeAWCYwImL4o8YKVKzAaAc8LmE-Kylqwr1Jb8ywnkKnaJCHo-Coo4CwuqTCPC8v734Qa-kw2W59CPA_12z5k_CRg0tJtPUjb0AvzAJsB2Mwe_dhpk3GgumCOSGk4_c5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwhAaaMsI9gx5JhOyncNSKJ2UhKzDNUmgpFADLFE6NLo1dyEhWM39tt0IjbyOz6iqZTGJrAC9-g1dmWYmG9kGIzGmDGS85E5dZuffI9oPX9xgjl2OiBvqdpZMgLn2-h3FNebBg3aEyB928_e_P2Yj0adD4Dp4B5YORzgtfUHwtGr3g3rUd6SuXzKCTYyHsPA6laEPa9sj_y5eMO6QwUu5DBG-pY9cB_--D9SoPYkSHDllzXu-k0YglXzKabUFQOjVcggiARsfc5Xtliez7sutR-F6Pu_FeKRNUFpiTnH7FeSsrEj1zUQYYl7G3NSiW1tTq8VtLcwhIVIBuw1j3OjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sbf-bzEzUxtls4Str8Hxfmk1VzHC_YCS2msNZSxINBAtFf6mDD5oWHTTYicpoG_HzLA0DyiGv5jvrbu2Hyk8UIvvAakUJcz9voNQDVnMoTPqJ9JUJuMyOruXSriIeySoIXAfPqq8QOu0CLpJ1IACtfjvajNoCphcPvbP3nX77l_Fs4cYeTJihKecPkiMymeyH-H07mW3fawvl2SuG-7xcjGL7UM3hHIKzEr-6wnAzLhKKUR0RudNbbBC-SQsRE400qTcvSMoViv3UPth0A8uA3oXIe_EUIpN_xf2yubWO3Tu3m10KDfRIJ5Ju0w16xOenEwfJX9Mz_eVnMYQC8C_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlEO9Pk8HEBVvVIZe49lXu5DKwdrKA2AGxRCqQq66H6jRCDNWqalbSTdD1HZM1zFyMrLOVUlVIfeCqG4MItC_RDUrHbZ0q2W87CEqXKzV-Tsvw_Nv-d0jPT9YnJr8PwRiDpVre5zEf3o8zoH4JRyTbR3B6P6u-UrXIb_qwYHIL_F1EopRPnOj23srvJDPaLpSbZUoO4CC3DTCzSzrfVDGsCY6gvqeM0zWqVfXw8F6kmiNf7Lfuzl0joSqQ6rmPn5XY2unpTZk4JniSOy9FBq5wf9oleDT-uh0AQbsTnHmyaO7VRi4rx5jro8pQ7y1ak9s2LhD47O4dkbrxdobE3GTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIIay431bmvo7oZvhTNA5hudUU5imlYWtjNjhxrKBTqom_lVB0vHfIIXtxV_YBSygjpQe_-hq2t0diFvdJs1oDJssL1JMHkHobtOpC7Yi2WBF4tXRql3FHHvfil5O4dTl3ejwZy9-duFTKSraLwmVAOsWqOY73KmLxzuHptZKzNH9CAcQzAxdX8z_6Po2ZGO0VAD3P5mhcrXzZEzC9lEOnU69DcPgS98fT2LieZaihJEpTXWBx0mKAb-NfsPF84fOUC4j2byGIa38fx5XHhuEcaAEcc__dxbYiCvhs4EL2CnLXk64KzwH1LnL2ap3D8xsN4xAinpXc8HdWBg-glEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8BfhK_atWMemQZkfJpAdI5U--X5IwXrE585wj3SyBvOMTOyYx8xCXcXvUiv6iXGYEOxPNOQPUDYqrf2_FmvecUN4hPVsi63mkSvQ-APipPeOW4ykKjXIPMTF0yVrt0tG9IXUvjQFw8GTzAlSsWIYKH1Af01FEfhccA0ZzMBtw0a4q9mxeWMBYPm6Hg1cE9m-RpEQSn7Xy9YYr7X5ouKfm56gA7XiYyfOWlpaHEskOEn1_H58jRxsOD6i05AAI4rdTbiJvnOSlHUu58umsdZIqTJ6BQ7jgKuH-vXbbu9STb_5GR5tc6VB1OlgTE6hIFIHamjm7DQwSaS57S1Dm02pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=uOZ7h_17e9GuYuqVNzcp2O5BkVDEtH3NhbsEXaD7Uq_oGtXLN2y5n8p-QpaKJ3teZYhH2F8s5Z_Yu-5QRpYrgQhgPFeJ1R5QHkNKH_iwpkNb_gYyqsnxmZqnFUuU72tSUlnVbn_ezXJV1bbjEiJYuw1IPrZXoU-blmXWIBr4tF_irwBK_FsrrxhUb7_orvmJSzRtxr-R2J-tgjaoMPEu_MpoREgnMhS7d2hb3-3u289BgljfkxuJm1ge6P_me75zotHLZhJr2gvNovSIAIBUFShXAiGqx7QK_Y1EIL8BlUuOBtB113APBXxruMV2O3Md6dgGmEas4jN8LxfJhlEZqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=uOZ7h_17e9GuYuqVNzcp2O5BkVDEtH3NhbsEXaD7Uq_oGtXLN2y5n8p-QpaKJ3teZYhH2F8s5Z_Yu-5QRpYrgQhgPFeJ1R5QHkNKH_iwpkNb_gYyqsnxmZqnFUuU72tSUlnVbn_ezXJV1bbjEiJYuw1IPrZXoU-blmXWIBr4tF_irwBK_FsrrxhUb7_orvmJSzRtxr-R2J-tgjaoMPEu_MpoREgnMhS7d2hb3-3u289BgljfkxuJm1ge6P_me75zotHLZhJr2gvNovSIAIBUFShXAiGqx7QK_Y1EIL8BlUuOBtB113APBXxruMV2O3Md6dgGmEas4jN8LxfJhlEZqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiHFdQjJQ-0HuKYp0Pc-VPzzO237yREG0td-Ue_LO3vPJr_t0LeUdhnntnh8N5cZ2iFfuprRjt00V4zGR0OUYdrS1vKSqs9RM3Ds4k2AzOjHaZL4rfoyZrYSLuaPI3h8NdfEROMV3cjVthGF8yGXwD7xO9wgV71J-ImVUGIPs8g8pk-9hcK4ujXBWgrwxgVoANikVQBlxeXVDwJxr-_Z5cEpaJ7GALnASM3hPuaDg0v1_qJr39ncoyuf5-QdASAWmZB_2Koh9fH9MK3hV3T2Q9RP3jS4agLs8cqI4BnkiRMCMkxtdkrxtA99v2RYXwbesg_e6xRHkIyDMMNR45QJ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgBlIfwJAEWdbRxOzVvpPj2c9U2QBRSo-Arss-H7pKoQcdBP7VQksDDvnfHcnlEq5Bvl88katCPQVeDqS-6EbcSaV00ZvWMdnmJwfY6qEcYrIFDbnNqhuqpxkTiR78B9EOdTrNnhdYhuOFA887YLA3RHkKZ2KnniJ7E_9ylu7E9A2drlFN78jYz4Dj4MtKvciBOPRwGeFyk8HxdzsTCfj8JE3yU36U5KJMClDTI6QFYMV0VZ3BTc6ANwkQ4G48OPeQlozvmoA76dpdQs1qVASC08JtpkI_MfuKTCalroPUB9y8HFUF5Qfs6b1QrdfPGsOlMlWRykiMUDGQCSX8zklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=TT_CEV0F118TrmvMComiA4WI8-k_SHOww23a7pIX_cJ_SNhLyqEZnKKid7Fp-U46ckkTyAEw4_dQMp4xy-ECItLWzUltJU1QY9Ghge38yynOwdCUAiBxZEpJRBb7XaTgTfLShIO51Lpm4LTZxIRJw9QbU5Vm6vf1shWgcOlCJxjDx37ltFQ-D2DC46zAVAueiUty1kB9tHauyxOcU7Rv12oRbn8scipCPgKCh-AXtBKmmD5KHB2CjHvCu1X1kjQUcVi0JAS_B1r2bGrsA624pHqAncTP014nZB1yC6uS0duU78ziaCMSPsYSsjH3zFlmXsdFGYW6OwIi_cZgrkL5zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=TT_CEV0F118TrmvMComiA4WI8-k_SHOww23a7pIX_cJ_SNhLyqEZnKKid7Fp-U46ckkTyAEw4_dQMp4xy-ECItLWzUltJU1QY9Ghge38yynOwdCUAiBxZEpJRBb7XaTgTfLShIO51Lpm4LTZxIRJw9QbU5Vm6vf1shWgcOlCJxjDx37ltFQ-D2DC46zAVAueiUty1kB9tHauyxOcU7Rv12oRbn8scipCPgKCh-AXtBKmmD5KHB2CjHvCu1X1kjQUcVi0JAS_B1r2bGrsA624pHqAncTP014nZB1yC6uS0duU78ziaCMSPsYSsjH3zFlmXsdFGYW6OwIi_cZgrkL5zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2bg_D7yqs3NkFsl0zmf2SZfTMG34LXNoB3-8kAzwPdnNbPOjDDQxPsRss8OOAkw1xV2DA5l9DMuEAyL1eHjo4XZPVv0Ycnz9fDDU0il2ukqQiU70xrqE2SlFTJP6nKOHnPWapWiyHWX-pinPyzYyeY3PMgO4lM2-DV0obNC8JeyG-8cM4MDOr6_5MoGlmcQLuV7PE4LNxnmWttRtqbjxUykKwQn9_r4JqK_racsp1bi_GtwYk2b23sQNUkAGkxknlCOmsJJeI5q84cXWMie29E5FBRsuQAGKJ8mn100fENYYThM8FJxfQ3T3Rc524szXGtBsSijcXaxSc02NID39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig_DKkYapjhe5nLGhQ8jUTYeHjpD7ljkJzNfKVvEVqasZnJ234ul1j9tOySaf32-XHwnsJiaX87nYZogehMKeThxZYycVwvwabnOKD8kgaJ5K8Q1MWWzsf7UbbL3_6sINTa7waS-uM2Y-npaZ8_QjSE-jUCqEQdRfdmpfXKp7BuHPMhsDG4QtLW0tnyP1uUQmnTpwACNgsnNfHXxHjXu1PCkAvHNcdoFzPvmdEnaFDS1EIyVoyA2KpKV-PAxLjU-gOt8H8FzKbWZo-IhWIdgxnS-dQtPpIX-cLRxShbjgrP4EIHR1vsvmhDKIplxnrc4iMP6CXnCcpaq5pkD5Dxozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhwAcvNji6c7dQ7jN0ErfS-v2JpwQknhJIQ0SRLP8as7uPDTyfprH-pXJGIL2Vrv0zZ7V0nqnYhNFHIDYp6v_Awy74aCyV3sTqXjOjhTBv7aVgE_M9EF9YqHjnGSvhUekRHFAwnWz3X4CGucKXyn8WUHJVidHXIJ-LEatRRPm0WboXTgXZSzyaJ11A1DwOO9csS0gRJygN94Bg9wYQiHXnEEpW3jtgOKJpA_Uu0xi7WNVO_NZv-EosCMz91YzBGyCapJA0WRCXa-LOL6p2iUNEYGJ5AiAc-e0-B1tqkEpEuprMR7XBD5ahZZ7JcZkywhCjQXH7bC8P42-rXIbCMc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOesrr5PoVKKtQokYvb-6KRxbP3r5UC53wjz3xVYYRr1mpRIc2pI6XbUIHbC6eMMdOdHmv2kCsC-Tn81TJs87AFqTozrLMpkqS_FHIP_77ozSO283agL555_CPudZzby2Gd_bKbKRzxdN0dEf4aoeCtKQui3a9Hnh-ljvQhmSg7WjYUHu2HddvcnE_7nkWMPR5h5THti0yyP63OX1XGQljB1hFTVnC2MGRdQ06g_5_DodsNc5Lxa3pJ2sn2qUIDSUcN8aGJyiHUefxEVBeEKH-ZG36Cgtri13qfhonLmzT5jnzZHV247_Nc85gZY5NzUM_GJps6xveE3nvwOw8yCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=B0sp7vgupttgTPscT3KyW083TiwY47aV-T4NF9kLhLORdNyUlSAb_juAe4HNeC2ucpIi1-GcGyem6XMnKhlKLDBAtLGlpmGjB6Oj-92dYWT6PwAB4yws7rHG4Rd87AxbL01WM00qd34LRS0hYM8837TcV-hlOP-h3dCKZVo5VUF24n8nsc08KkEKL_ob2eXg-qkO7b-huLXrjwmjtfVssusR-R-efrfNiMlkB_rPMIwcg3LabE8kUf9LtoydzejSBgEnkF4ivFoCUTpdx4CQyBpvKzSMpORMoOs5LJLjP17zrD0NCFq7RoUwKX4vhnWRAKgwmAH-Ze1XpAeuiA1lrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=B0sp7vgupttgTPscT3KyW083TiwY47aV-T4NF9kLhLORdNyUlSAb_juAe4HNeC2ucpIi1-GcGyem6XMnKhlKLDBAtLGlpmGjB6Oj-92dYWT6PwAB4yws7rHG4Rd87AxbL01WM00qd34LRS0hYM8837TcV-hlOP-h3dCKZVo5VUF24n8nsc08KkEKL_ob2eXg-qkO7b-huLXrjwmjtfVssusR-R-efrfNiMlkB_rPMIwcg3LabE8kUf9LtoydzejSBgEnkF4ivFoCUTpdx4CQyBpvKzSMpORMoOs5LJLjP17zrD0NCFq7RoUwKX4vhnWRAKgwmAH-Ze1XpAeuiA1lrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNxGh5xaD5-7ANm936UqY2bhFaFpZXJ4pF4w7dMRG4bh2ocsPkLuBNSAgbkUij_kFprqmNl4FDhrG1hfvN6nNkqi1HYaeM75FoO8Dr70N4wR3fZ_72duX5XzuNHm5cYDIBMN9WtXEscw9dlqvpB7Wmrvw4TGNPZNI3sfWqOLjXgsTcJq7Kg1bkyQk7lgHWXDyGI7wYWIeNoKW2ubJdDS1IgombqGziEN5w78IHpafscjR35iaFWva4bsNbNiQPx9dAf463z_EfNimqqri3vim3Sd5y_fBEGtfY-LQiolJA6n-wPv0nS_41Qwuu6Lq1u0jK1YgF1Qhw__lUtyEZVhWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7r4Do7U10gju_8h5_4NxE288hI2zmWhX_E213FneXNslAZjF8G7Ys_7HN_ie9RqaW0VUWq7FgG46Ns-lXHPJLZziIalsmQQ5TUvPbj81fF-oXFGYI8rCX5ZgYcG9Uz2OHZ8VhdQDaXpsxgByQXyaExso2a3VCP4iL-_AtT6jW5WaKLHSaEycE5qej14k4s13KaRfBecbSkBEUY8UPoyzhqv7QkAWvjLQ-aqVyDvVGPh6FHeTJYWuTYBzQ1nX5io0Gh187jlpaKpj4lwdCuc6pco3aP3Qr3MTgP7Lwpy-VmVb-dwqV4N8PLXg9waQ7aFb3si2QXi8mdHDnpnb1WX3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhicW9oSb6emInqbsDhUvF_l9Oa8p2admP_Xx7B5KZtZ9eGrKDmG1VS5GxmynDx9PyUl_td1DVjWlykzt2tgYE3gWUdggWJl_u3Q0q1pzQYPsk3dtmkKvtaEMCN7U5Mg70pX3AT3KlsUITuKw3qKttXJR_rJI2fc1onOEIUW-VC8DuQ1W0KFa1rOjS1rhq-Rgk7WIPktM80LMsPn-b_UrUqulqkGcHepRc1oBKOVGVxzh2F_HViWd1fEg1WnY09vixsZtaBvzVvXV4ZCRX8aKcYLxFa930KxAxXNUkI0CzDCu8VcZn2JNLxr6I7WmSiutm1VD2ovfFmHvukouH-9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbvUlvCfymHuVTQYOzbZ3hYW5MmbeBb6vl9_yLkazc4rtHLx0h4tUl-DVhx-bkohcGbYYOhCtegDmMHHgTGJg2asHOTf_3Cp6YOMk2rNLNFzoag88ICi9M9sjT5ZV7Iw9-SJ-OuqLTETpxI4vXDSraUiUApXk2lAPsraqbukQPhFWTj3U_62f8V9smiqF3dxGfLrwFlzPu1fULBLLfQakAV2uZFdvN9UL8DszkPhizAcMsN6VrDO1pt7ROWzWUpYiaOMXpxoBiLidFci14-rq9ZCqNLW_DUk3Xw026XyelTAbg_ljFH9ejqNpHUOdPXqddt4WS0QzXSIaH7QtLd4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2johcFlqdYNu0jGNCyJoHrDl3WPcDQzqUOlAE5T7PP3kMVRlDk0KxhccX-0TkrHVBf86dsAoXQW_PDC1t7wFv90WhLJ7FcgOXKPC-JuHD0OqTrmRU1RSPaIDoCGwGO5ON-owmbAP7kHObFyL2eAbwiHLCYVzq32SHAxuAo7CXrB6j22LT-lannC_OeY75XznOj7MrKELliWpZSnQk3yMYztpqP0fiQnLsi2DElz7cJiSim745VMSOghdc_CKk9HUQSY5eOK7r4hmyPXYqsz9i1IxEiEGCZ58Y4OB9fuzYsvvDi8EdUNbDigHdCdRTaWCj96OJnHYaKNtRhT5Hvazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyFgs7GIzeKDp5j7YLJnAtBkP0I2baR_HsHzTkrRxpSCqUBRjzv0OI64Z85J4UPwc7cr4Kt9xUu0oPkMLUh8gAFInNe0J2ZW5FXWQtRzeyFV_dQMTaCSw55jd3Z4AmN7HOx2afywIeM6W-h7go5Fu5GLQEEhYzFGGliD5JraeZj8pYg3pye2ZsBTtRqgr0VYiPQMnNI2zMo66mQCRk3h27HK_S_aPIzfUkWvAmpa9bt_3rbzflFsdp6YNH0yxGTdZphdMhx5RsXzFrPclbTeOFsj_s9EIDsOg5gGLeFKMIGhp_fW9FXk38UEfJfy3KfZRvNTr-p6LXwLU9Cv3yit0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛نماینده‌خولیان‌آلوارز: اگه باشگاه بارسا با اتلتیکو برسررقم آزادسازی خولیان آلوارز به توافق برسد این انتقال در تابستون پیش‌رو انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/22314" target="_blank">📅 01:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6CT9bt4O_LY7Pe0RmhR2wzaO_rLxP1VXEKXnLubpNdldk8u0Cv6D0HhGxEh5K_b3lqWw76lw83Pn6sQbC8q4IDaWvJIZgEevQyUN_wyvKeTQHBrk9pIyyY-q-sI14D7bit4J_V9rcDs4mt_n8UwbvTmwgme7aG5CkwvDFd-N16Z9IFc3Mf5y8hkslHl601SF5X2vmHVG366cvl5Zr7W4JTA26etRiMAi1VOEGU3UsVJIA39MxGXGJgZPjn505gQ3bD_qS-xbtcrvNxASHc6fO5AW3Y8Sj0hN51qCC00MDSB6EqT02jd0vkq-VtUbUD4vIP19QXDJT4MaRXm83T5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ طبق گفته رسانه‌های نزدیک به حکومت؛ اینترنت بین الملل مردم ایران تا ساعات آینده وصل خواهد شد. انشالله این آخرین باری خواهد بود که اینترنت مردم عزیز ایران قطع خواهد شد.
❤️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/22313" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auO07LLhlfAEsuNBdFCRJfFsbomBZwtGQtkD870weQYMoYxlerx4_XPXqI9UPpzwEvigYE5nAu7XFPxQUSuqs6wLUtNhIVSyP1eZrgM3bk7TRjPfLpK3TzGrl10icZeYva51qQfld4z3f3TIJsB9lFLzMiFDg0ucDA1E0EnE7Uj-Kj3X60TVygyXPPfGQTQLHeiuCiwzuWo2rVNPOjX474jE3ei8MgzZoeaW9OKYJtpddnbeN-7QqjVjkLkMiSwDgL9KUniJQYOxZ4KigUegqAxFNqu4TA9KXu40iVkQxKP8kJ1DLp1Lf01zCsHfKHvgMW0fZAlsRqlkos2eqPTPxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5-477S-jG14nFTZDSk-H9SNHY-zihDp8H4hx6Htnz7vZI4mUQfV5I93fNJg9A5hW2FGP8U0hd-9v2kTx0zy5K9pWMoVuMDD_jSYbPQtXFaHwyDuk3TmMgUH0dj2J3gX_8OAvn-JCnJOrWF3ePzo2C-Qu6qFBrbeRLWFgB27bwewMTcSlSFIMXhWlnJhQwULldJSiW5bGl1fCTzrJWgo6HUoLmdzr9aK2itdSwpGLk0oJqZxtQfoXj93ZaMr4wqe2Cu30NpRSZ3qplxtSeQ-s7lB7TJlPJAQYLI9ADU9HsI_UGCQs3fefZBZroWZHTta9zKNGPSesxmpZ8M2tEk5_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNAfYnn11jDWja6YrwRglfwJYa761EojTy12_QkBOpgcf1m2efSOHm-bihtlM4drjjxHp0f78IhiQvb2qflt_oLwIBgDckLShh7SmuEKRERRhbhGcqlpnB9Bg2pDsGY46463YX7c10Ptc_4NRpuw8xTqTtAIt2CNwK7umtrT5B0JksJ_Ttbzpw7YTF54nE7GaSTtDiIxrpe80VdemuJAom-Mvg5WFWvvlwNbpU2DfWJpm_ao5kdqFoW6d4FgB4dR_QdpHO_3lKxeTYXwVu75eIBbYgBm20PqG-OJWQk0uRS8nojCse7IninfoqcvBEDssEQaB9ycC5TUM5AOQj5Osw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzMMlAFRkHkwTmkv9j7jXEJPa0vpyNGKsp72m1-xtZYOG1O-LVWP6VyVjWsQ2SP6nwvYbvu4Y3VuIN3JDEuIm0r-xYGA24jaCgCetzfY0KhNq65KJetqwpDgZ-4VdliHmY_-2qDxeNBOj8tWkqO0ZSxjbyhgMBREs4AsJpGtRngusum7I2Am4VlmMeOljRWv7v3XccjviXncpDErWLTlbDJXxfD6OlaVd1KHkFNW-n2oKqllAxuoMHd2WsC7nNMBafPMcWud1P2oD38xmzz9iUvwBgvjFOY-tOJsEHujjP9fuoWDhCH4fdMF31x2u3DNwdFjQX7jJFlyoX1apu3fYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0LoSMWFxkzYrplhWXUldQSmUSrVTgmNfhi7IG-W5pmZEz6bBEeuxR1Zbk2-cA1EgBm0p0-ddCyWBe7m4EvASKd3XtI0vZ0fGe2hcwLBqfFa-JK870Kvuw1Xqqq8plISaJ7TbJsjn2lycr---MmxmzwxDWx7ExMu4hzGXhz2ef2eMVj6Y1ZqcO0qWtrT9UR14MTkmVI61-gJhfx66PI-dHQSyIH9ttt2-7FqYfXQSd8SRpFLpYLnGXDvODk_nW0bQVfwZKxJfUlbqgPKgJqa5J8TsdnlO-ecLgaFXQQaEcjKUAsJ-mudgjL5Z6GTQlImAbEHwCa1VTXhvJIbZcuNww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHhmaIytThwO66mMLj1Aa0_LPCxH1UaboHUUNXVou37r2cZ4mVef67TDsb0J_Ti1gt4rRRqJbs0eT5EErCSUPO2RxGJRD9HBWOLIo5uW-HAtLY9P61DUuK3M0fo11EbA00a8ZbGKaJbrXulfYmOovRzyqLC6keuRqso7J2VZPAffmnjcU_swV9NXiv_6B8nI_OwIFE9EYof4hlulTcHlbXKnQCT1eF7n4Kp_oNiHcertcY-fo42ek51zAfZQeAmkbezOaNlRONg3gQaaus283cVZDM7Co5mjj_K40fI0dBo5ofQHLnlxUU4i9Cv9xIoBh_9OdksOV6qyMKLKOow08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8NU88g47V_1AOGrgzJOtHNAXIO3xA-zxwD2Mu8WAGap29U-JYqP1e_9vZmJVGlRHx1EFw6Hsfezhlwdg1b5pV6x9RkPUINhlH2rk7dJ4yIhYj6xFX8En51qiST6OEOS03luwwbGsuW2KEyeojJAc_TOJ2BVKQAp0s_6W9OKyEZGBxTwOGtkxOsm4RUOLjqKTbLsmkfZmpkC-XKEdrcceBqccfe4Uo5yMdL79O0shvJ5q9qR5F4VIXXzGym3hNycqRhn1CSJ77w588Ei88DMd3zjA7HqI5h9o7SMBgkK58QtmOYy6LhNa1dyBLgNP0wUlPrEm82lri2B_ltDs2PY_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6steHTEtQjZMly0TTZ4vwr9DzUxv64Opdd__hiHjq3SmsR5grmu6SG9sm1x0D4K8Z75TS1SmYlgA77NVM6bCnkN7jwJZ2KPJ9-e-P3NGuuIINGqZJOzWP88sCkJT0gtx4oCmGRVT_kb9Owlq-pJS8K4ROPdFng6-07iOU6MwxjSnzbX8FmcxMlQEcXwuJ3ZoAHKoApxLOU-xY3J5kS8wQ2SwzN7RQdpmKMC97meARK3dpbVAFGA1cWvaiLN42flJJOwlbOc5r2Hpav0CmkA6vhNM5iVFduut76SR9KzDyNWc3ZH1ULo6VpP4Dk8S26kylZSOJ_WyLPRGyjlhWRGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjncBG3rn2b8sDgEK_x4_jPVID_7bEvfVfQAEQT0kS81XwbZ5HwHUr-kLNGSjOArEXht70XpbrcnJNyG4zux3TbXEGL88T8jqt_aSyuIJJu2JouCsyYXsmIQp0_PUlVoGYmxC9VxizxhjpHrqnVV5MWmqVj3ko6-0oBaYEnrUdr1RT74WmLkm4C3oLEjlvA1sBdFKxB3S-8DT9hemoM6V4nBCXDf_qXpsdmf4C8-iJJzk9x6-xJolllTTtCCWWWcYfj2ysaBA9UHr-Uhw-orIawzjNaj3rsFdmEzl0R9C6TeCRp_C8MO4uYkJZgawSQd2jcFZjnEa_DBnW8IsuHK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZZJm6-edwZZZF0eMtMZ4QpMnz0OW04630RM4VD0Nws93DXliwSlaPoItgnbaQOS2E54lSDb9td1dc_LEJQP8XyrrJkmlKhnHJ9gHbppdguMnFSFLlL-oKc5KmnEcPy4jIA3TL0uIZCBd7yj5c2tRsiUmuRAn2coLtU7fSPvKF8jOAgm_I6baHEJEwcwg9NvEfRt_XCzWuoJ4XdiGk72PYtcHsIiEJBMcPCddZc-hgD4R2SwDjmewE-AxiFkcnRFpGCKCBVRs6QNxzY-QrCjb1T2XmLgh2w1INkh24nYWZu3vUnruQkYK82ucFRXv1gRSRq_Z8QQpi271KiDRwSrLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RML0s2evkXIZt_kOb4qb3Eh02dgSkUoE33UCB9LVfwzBGaWg-L16vxns5r6dqFuXanUYGIuRFC7Jy8T5RdBICU61Ko4ZdxqyP79fG3wjtt9Gwq4pQYnM2AWA3zhotmw20XUMeW-DglZsSQXzoe1CYfV1mKUaCoIJuM_t6Jk-9Q3q4TzA6w-vLBuR-j9_8JmsTyK2jPwv4mokgLpg5RTZ22v_t0ki5LkIJTZlIB7LBQi201OMHZ1bceU8k-e-bTNZFvPwKXo7MtCF4FK4X4lEVt3qG_ntjpkw1mGVhvQ6sQ2_lJeDDMoLQkX69pGzp8fegKCIBTW-avIf8gNNhev2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwF31r8M4oBjgB3knArsVvVTMngyaYf3KeSwhrG9XWkkIBa3O_tf9uiBO4v8wRQI6qe25RHPwH1bCoOmoKkv50W34gUAB81KTc6YePdv38c7CD8-BBbNLMpj4jB8rCrN-CdmiHK4oWV8L3t_v484GQieYtikngpFhiDLYTMBsLyzCan9JGeMv1cVMmjr70QeWud3HYGnP6ujyHoITY_IoxMWn42liyIXiowujBOTEbECYZTyJtLZj7TgT-7RALNd2rOECNY5u_Hafh-lmna4wIDEwuegAbyY4dTUtXMWeU8g75-WcWjabfzhYaite_ZCz9ECQ-J_XkNL40YBOznCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxU9wt0g191eMcaK4bAjv1Trh9YZ5pouL4lKFTKpwmmU_tyd7FAJoQvWHgDlU1nvPYyHBjLOxLkZuEQcPrEsSg4M5Q9rIzttEyLxtfCl0ww98BfE4_LFBKoXBlQ7FWy02wM4bzBiTQzkgeGPRz19Mdy9nx74tU_BzrI9aWLHQac4RKxCzzcVJlE1x5Cga3aAg0__pswpFoAia1BdJIhfbh93PkF434xAIMcX0aPhxvVsIZMkQDh26ibg-JrnodpfJIwTQdrl9KryYdLP745Qvdtcl2F7s1513xvl2lO9ySjBuaewfeWl3eMMVvwP1Y6xeAjnuOXlJcLWKnZxbiXLrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
