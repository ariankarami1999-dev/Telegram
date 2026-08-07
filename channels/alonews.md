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
<img src="https://cdn4.telesco.pe/file/fGpM3Wtb8_UP4XsjmRS75dQQ48LrT8duiDKIfJ6iDAuETtFfK3h3QaJFHWfVnkhrQTukCCFqS7LoiVPlg7maYb1SsWj-bv0WbC7Is8qx6jPmWGFegXpBtgAGXECi-0cpqBhHNxlW6QZLmgcti1SWRR0KBdrAJo216T4y4zYFuj6Sao1pnGNsrjUoiLn1Ujf1PTbdwgyqBPh0w-q-xzZMrpcAOsVCtKKKGFnCS0RoKXBLOZp4klKLpjG1FHj45XcZvX755183CDoFpJ6U9CzaqeW5tfNnEPbnZhJbS0kb_VaesrQiSH1E4h4oth1W5BL9pANlsOWzGUnzbOhkFtn3pg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 978K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 03:25:29</div>
<hr>

<div class="tg-post" id="msg-140501">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g69BC5B0LT3ooOy0kQwJ_4c1VsIJ99Og77rclGLyqlKX3Af-H1sJNbdJx3tzbEi2CdlO5HHBtYd_aXUh0ijq-3ZSoW5ojSDpgIjTaM6iQkgFYxDeHzXB55pRO3qXhpVQVC0kKUJwS1WnJSBtQ4TDKG3TLGHmfK5qVgcbXHNYtXDQynPnzEUuTpsZy_-oh5Hk79oNN6Ym2wtKwbkcoUSYoqjBUadtNVctl5gtwRZbTPoDIoQ8LGWBooQK31_3RgIWX0uaiwlqUIK_68f_qY_B_JwcyRcsEamX5PpLLUOIR0BVggpl5rBPVB63a3xA9kUzm9RRJmUbZCE0neR62BRJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی ان ان: ژنرال دن کین، رئیس ستاد مشترک ارتش، به طور خصوصی به مقامات ارشد دولت ترامپ روشن کرده است که ایالات متحده باید «راه فرار» از جنگ با ایران پیدا کند، زیرا معتقد است گزینه‌های نظامی موجود برای تشدید درگیری ممکن است نتیجه عکس داشته باشد.
در حالی که کین به ترامپ اطمینان داده است که ارتش ایالات متحده «قطعاً می‌تواند آن‌ها را نابود کند» اگر دستور داده شود، او همچنین بر محدودیت‌های نیروی نظامی، نگرانی‌ها درباره کاهش ذخایر مهمات ایالات متحده و خطرات یک درگیری طولانی‌مدت تأکید کرده است.
در نتیجه، مقامات به طور فزاینده‌ای درباره یافتن «راه فراری» بحث کرده‌اند که به دولت اجازه دهد تنش‌ها را کاهش دهد و در عین حال ادعای پیشرفت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/140501" target="_blank">📅 01:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140500">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
در یکی از بزرگ ترین قراداد های نظامی تاریخ خاورمیانه، ایالات متحده مجوز فروش 5250 موشک رهگیر از نوع پاتریوت و تاد به بحرین، کویت، قطر و امارات متحده عربی را صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140500" target="_blank">📅 00:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140499">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8192485a22.mp4?token=WIi_u00m9IxjSwyey2NKAXCdmwJncrL8I-stTyLNHWdYiCHMO8tok3E1bk1NbXZ4iaErLGaUWIXRsK0SdOMr-lsUVCB77gmKmTJXOTOuR6NiS9oZlDTmwy3Tde2c0lsLBp2pdYUkM5Glq1oukn3k95axM0dxpEwOzbnm2dmXdysGbO-0bNN9VLFhf_7IKio5nAtSqDvvEYAnr9PqiDymPIXsfN-LnqS9D_DlMwesZw2FFMGiEuaA8DKEHIeB6phyhKcB4mAc4J-o6MycnQbo0wYPg7mYS6IYffnfCHM_CNlZ8ppbSWA8NDELXMoc4LdzEwUWWwhgQ4EqexvxBCaSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8192485a22.mp4?token=WIi_u00m9IxjSwyey2NKAXCdmwJncrL8I-stTyLNHWdYiCHMO8tok3E1bk1NbXZ4iaErLGaUWIXRsK0SdOMr-lsUVCB77gmKmTJXOTOuR6NiS9oZlDTmwy3Tde2c0lsLBp2pdYUkM5Glq1oukn3k95axM0dxpEwOzbnm2dmXdysGbO-0bNN9VLFhf_7IKio5nAtSqDvvEYAnr9PqiDymPIXsfN-LnqS9D_DlMwesZw2FFMGiEuaA8DKEHIeB6phyhKcB4mAc4J-o6MycnQbo0wYPg7mYS6IYffnfCHM_CNlZ8ppbSWA8NDELXMoc4LdzEwUWWwhgQ4EqexvxBCaSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به خبرنگار‌ها:
ما یه جنگ بزرگ رو درپیش داریم و بنظرم بهانه‌ی خوبیه واسه اینکه اینجارو زودتر ترک کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/140499" target="_blank">📅 00:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140498">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd08a7bff2.mp4?token=KMAAD6JDsySYr9lzsxrQlr1xvwLkgfZqFC1V1ElUHDCdMRzEYuYK5-7MkQndxLeYjvJ5h1rTKWoK4VfQiivlvju6gHc58jXoI_ET1WSJJrSTQrOiZi49W3hpOezoL0qRfKRO1RTdIytxGIlJl7_jQam8dSYIWQr3mA2uHNSsMC1oaS0ASccEyqzyj4zUaiZ8ily8tK-BIaagPbF7ez6dt-_PxOQcJRVc070GbYrE39goFFqU9V68U13toa4uUcR3zO62U3668RcnpKuooVAnUOplhCAmgACOaIMm6fqTULc14HiaVOyix9W7qLEFK-3Xi130wMizIs9DmvWmEfUwBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd08a7bff2.mp4?token=KMAAD6JDsySYr9lzsxrQlr1xvwLkgfZqFC1V1ElUHDCdMRzEYuYK5-7MkQndxLeYjvJ5h1rTKWoK4VfQiivlvju6gHc58jXoI_ET1WSJJrSTQrOiZi49W3hpOezoL0qRfKRO1RTdIytxGIlJl7_jQam8dSYIWQr3mA2uHNSsMC1oaS0ASccEyqzyj4zUaiZ8ily8tK-BIaagPbF7ez6dt-_PxOQcJRVc070GbYrE39goFFqU9V68U13toa4uUcR3zO62U3668RcnpKuooVAnUOplhCAmgACOaIMm6fqTULc14HiaVOyix9W7qLEFK-3Xi130wMizIs9DmvWmEfUwBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت دونالد ترامپ با هواپیمای نیروی هوایی یک از پایگاه مشترک اندروز به مقصد فرودگاه شهری موریستاون در نیوجرسی حرکت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/140498" target="_blank">📅 00:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b422b0ac1f.mp4?token=t6hcNDN8gJzG7vgHH5S1kPmrFY2fVV2MEClmB_Y-DX4kKJh8saSc-4ew2Mtyy8N8NgAno3u2HThNPdT-V0wa1OhicRXLBtHdzxAkrEDPLDvpzFNNewiZpseh-fzZGCFJGAJrCa-6aHP6U_TmDsmFMRyzfeyK2D72UrGQqNdz6aga6rqqAQqN7n-g7A9jjrtw3siQ4o29D2gkBESQGWgXKgdKbBEh78jgmwysGnv3hJytzgkABRlf4yWtMIeufN0ufWlRYYq63JqU4jfD9odWLYC3aBDELmPRYmIzeFeOjeVQPo53ktho6SkAFbu1xox6O0loHAscz3HFornzAL9prg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b422b0ac1f.mp4?token=t6hcNDN8gJzG7vgHH5S1kPmrFY2fVV2MEClmB_Y-DX4kKJh8saSc-4ew2Mtyy8N8NgAno3u2HThNPdT-V0wa1OhicRXLBtHdzxAkrEDPLDvpzFNNewiZpseh-fzZGCFJGAJrCa-6aHP6U_TmDsmFMRyzfeyK2D72UrGQqNdz6aga6rqqAQqN7n-g7A9jjrtw3siQ4o29D2gkBESQGWgXKgdKbBEh78jgmwysGnv3hJytzgkABRlf4yWtMIeufN0ufWlRYYq63JqU4jfD9odWLYC3aBDELmPRYmIzeFeOjeVQPo53ktho6SkAFbu1xox6O0loHAscz3HFornzAL9prg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند: اوضاع مردم خوبه و تفریح و همه چی سرجاشه و همه راضین
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140497" target="_blank">📅 00:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140496">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEyTt4ib_beIvHPquV763HvxCvs31-k6fDa1y_vPo0kTlLIVj8x_PjEjkBYfzbUXHjo7IgpDOgF7vRhKQ0b3r2wHRR-GqBBlecaxxFTuyT619l1AEXedsbXPTlD8AgyAUGarpI-GS3-KCm1ObWCmyq50axtX1yRAGdedlEEBfb9BRBXljy7e7og0y3StgoURD7wZCWtzjBVpfW_OLAZ2IlTi8PZingukcGWoet-9PJS3YxWd054Jqrd9ucxawiKvRjKiRn5kNKZA7BhKRpqlkeVL6bTN-TL8DbAxZqmsDNmUqqOCtC2t6C6VG_CQvmEg3R-MreI74Q9kdP140aVFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام:
یک ملوان آمریکایی در مرکز اطلاعات رزمی ناوشکن یواس‌اس میسون (DDG 87) در حال گشت‌زنی در آب‌های منطقه‌ای است تا از محاصره بنادر و مناطق ساحلی ایران توسط ایالات متحده حمایت کند.
تا امروز، نیروهای سنتکام 51 کشتی تجاری را تغییر مسیر داده، 2 کشتی را از کار انداخته و 2 کشتی دیگر را توقیف کرده‌اند تا از رعایت مقررات اطمینان حاصل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140496" target="_blank">📅 00:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140495">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAXplt8s8dTemStZ7USvdxkUwJsfIg6pSXI0_f-s-oPIFtRcMWJlgHD0bx0De6jMZMrHOeeOZxMJvzTqSndptEyJZS_JyBn2SdyD1VcuB7Q1TWDFLaxUWp1ge0ndhY-BZuLNmI3YzY6kBM9UDbz9RabZ7Wzwli2YWGBol_Df9N7qjt_mc24BErQwLWuO2GoJUiCvN1U787GBBJdCuWr7qLBtF1GXJua37xg275E12FsPDVcemVTPcyFclHfmf5FBRZzL5ce7WX9i0HBjv6M71P7k2pzdy4dpLexTIUUM36LVrxflkQoPPmOQKYoayLri774sBu0w1XWTElpWgYEdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/140495" target="_blank">📅 00:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140494">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/140494" target="_blank">📅 00:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140493">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVVIkEFcSmriHDOpdfCCc31Y0bW9M37Cgkbn2X_-_fIrA3zLRm2Hx_yaO9bkDsEocXfqnNv_QZ7JkLc6_YnDIu7HM5K2VdOuyvIAc074G1B1B0wgYornCLYB1L9IeEES2zSX1feiAX3Z3JWQdr0WZhnbp8Qwq3SHgmkEqareUHt9xMqohLeYs-lEH887H5i2BofUSOJzqwzQQEbla0YJNWOAH9bbkZkDXji2n-UL3dbH4ofVuCVAGNIb5BQZaU9NaJc_IV41FxLYi_dgN_sz6V4-rff37mwTL1tLbnaBYBi5VTyKILpJPoO6khBiGUxiMzxXYvS8HIsTl9_sB86YlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش تعداد سوخت‌رسان‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/140493" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140492">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXCZEN8NNBPAUVoglpI90drsmydygkLwmX_TAxShnsABdIysKpGbuN5d-nvzmGfuQCMns7n1HMOBBCkXcFPFlqqNHz13kK_3fGk_j8Ynrs-8aGSVf526CQMfdIwsko1NV-lCwZ8FoMs2G1uaAaCHyLgfFMSFFl2zY5zWZJj1SPHf82QxB6i_lMN76KAfdAN8FzPjcfdQQlmWDjteiNwdES6aJQWVqbZ0iZmz57FEOh7e2FkJtV0DT65Sxc1oEJ04iznaPKnPOIFVhc5FsmmyZAKPAYyxkZx31YL9VCgMEFPVfFU7anSK1PGC4BweALVU8saKjhQc-MWxKZnOTk0J2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همزمان با برخاستن هواپیمای هشدار دهنده و کنترل زودهنگام هوابرد E-3G بین کویت و بحرین، چندین هواپیمای سوخت‌گیری از پایگاه‌های ایالات متحده برخاستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/140492" target="_blank">📅 23:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140491">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سازمان ملل: منتظر نتایج مذاکرات درباره تنگه هرمز هستیم
🔴
معاون سخنگوی سازمان ملل متحد اعلام کرد که این نهاد بین المللی در انتظار نتایج مذاکرات میان ایران و عمان درباره تنگه هرمز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140491" target="_blank">📅 23:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140490">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHHeZWEAeBTpDkfusPrrb6qCDG7ZzLXEvJvS8plX_PAxPJ3sr1UgEQZXu3dRHulGFW5BaMgkdui2soo-OkGxOpdhRAXTdOI5VbJwvYXkM9UR3xx_iJVEkoHw3WCACdE3q6LC6aNVoXst-oMtcJnepEHOuh577BkZaf02HtEcgnoRFn1L3wjzaUQ8CGKeqj3knLawtTMezHX6v1myux9BHboL_8sKUptGKfPw3SqHXV9AEV0WdW4vOPDyiXqBWr6cB4CbjeiJVnRaE0bajGy2TaUgTPIpEFaImQHsNequHJqERBBvIIhXNbEP6YQGbfZaCg_mxXEGD_OIJXUlJHs4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت هوایی قابل توجه آمریکا بر فراز تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140490" target="_blank">📅 23:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140489">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: تحریم‌هایی علیه پلتفرم‌های خرید و فروش رمزارزها که از سپاه پاسداران پشتیبانی مالی می‌کنند، اعمال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140489" target="_blank">📅 23:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140488">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOLKSxAk-va0W6-oprfYHiZphHnz9_xC_F4zSw9vKfPtDm9Kpf6K_RM_YkdTC9kzHM8JzMcK1tpvvO2dBvOZ0jLdZzN_8bwYEsZQ4YSR1z0Ao0CvKrbHPo0eXfyKuzl94SSj68evSZRhqZIk43FBuV_WTKc9O7WMI6U8-t3HD5OxyL_OvshwjSZgZzIQsNMODcIr4tpkmAEsSYJ3SFYp4rRN3W_MsX-SdNsHoskQGiU2H-bU1qo-LTHP1TLcsevtvpo9jLKKFATGF-wLtpRSbnM4Uhov6Di3m_ptdmZJKciOdh8FBcf6M7T_yfJTBGUxp_pKUm1FGrTev0i9kuFO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقایقی قبل مختار توسط صهیونیست‌ها کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/140488" target="_blank">📅 23:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140487">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
آبان تتر هم به لیست صرافی های تحریم شده امریکا اضافه شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/140487" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140486">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
دستگاه اطلاعاتی آمریکا درباره ماجرای فرودگاه لایپزیش در آلمان
سی‌ان‌ان: دستگاه اطلاعاتی آمریکا مدعی شد که پهپاد حامل مواد منفجره که چهارشنبه شب در فرودگاه لایپزیش در آلمان کشف شد، متعلق به سرویس‌های اطلاعاتی روسیه بوده است.
🔴
بنابر این ادعا، این پهپاد حامل مواد منفجره بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/140486" target="_blank">📅 23:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140485">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/78924983a9.mp4?token=sLXRBiUeXmwvHHNLVWnVg-VkywXNKdoOOE8zXQBfSTtgMR89eRLLOo4EPskXXiJSroMuS5C2ez3QgnHJmbT2YI4tNOvvCowk_Hz4ufXznSQKUFzQ-nT9D7kR2NmGDCdpAq6r95esK17KCMZGgdhmCyufHGjORofnraIK_bT3j45L3lyAXbb62DBp3cnzrDCVhwk9Y_uRnDukz6qHQrlk7Jg5HR-etGma7Bb7_TALkr6bOw5A7RHru6rLWFA6rcHLqH5d56jOhMW5AhlIIofbFKSUKHLZ736KtS_cpv5BXLPU22S-wm7lhkGMOYHjyCuQt4E7KPZWwECMhS67jhft9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/78924983a9.mp4?token=sLXRBiUeXmwvHHNLVWnVg-VkywXNKdoOOE8zXQBfSTtgMR89eRLLOo4EPskXXiJSroMuS5C2ez3QgnHJmbT2YI4tNOvvCowk_Hz4ufXznSQKUFzQ-nT9D7kR2NmGDCdpAq6r95esK17KCMZGgdhmCyufHGjORofnraIK_bT3j45L3lyAXbb62DBp3cnzrDCVhwk9Y_uRnDukz6qHQrlk7Jg5HR-etGma7Bb7_TALkr6bOw5A7RHru6rLWFA6rcHLqH5d56jOhMW5AhlIIofbFKSUKHLZ736KtS_cpv5BXLPU22S-wm7lhkGMOYHjyCuQt4E7KPZWwECMhS67jhft9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: لاولی ایسلامیک ریپابلیک آف ایران
🔴
جمهوری اسلامی ایران دوست داشتنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/140485" target="_blank">📅 23:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140484">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889f666c39.mp4?token=o7fuNb7ZU9jsW9wX8DWCUT4e4xE1nXtvMFNZkg9Wzs3O80H48jnnBdZkC_z1427oMUDYN1NfpeG5DLrwr-7c05j6aXi9GlVwaqs9L_Mvcx3lLNhQjRM8ohKkEy64DBROeDokRRrH2SDUmYeBsRpiDPK1rS3bBGx6aLfCMouo-e49LtPfoPTh5MD9nGLbtmfx0JBY5-juCXDnw77nBNwWZSjC66rMYWHGJ2AkkPi8KJxpa-ZhUOKcSa7aIUHV0eaaSq7h0X40lM40wDeYehetBGOwj6z-Vj8EkHLZvZV20-nW_7hf2D6IFPpGGwEOP_MH_CQERxTNT0IFHKaRLFx63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889f666c39.mp4?token=o7fuNb7ZU9jsW9wX8DWCUT4e4xE1nXtvMFNZkg9Wzs3O80H48jnnBdZkC_z1427oMUDYN1NfpeG5DLrwr-7c05j6aXi9GlVwaqs9L_Mvcx3lLNhQjRM8ohKkEy64DBROeDokRRrH2SDUmYeBsRpiDPK1rS3bBGx6aLfCMouo-e49LtPfoPTh5MD9nGLbtmfx0JBY5-juCXDnw77nBNwWZSjC66rMYWHGJ2AkkPi8KJxpa-ZhUOKcSa7aIUHV0eaaSq7h0X40lM40wDeYehetBGOwj6z-Vj8EkHLZvZV20-nW_7hf2D6IFPpGGwEOP_MH_CQERxTNT0IFHKaRLFx63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
برگزاری نماز جماعت وسط خیابونای لندن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140484" target="_blank">📅 23:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140483">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خرازی: باید ابتدا اروپا رو فتح کنیم بعد از راه دریا به آمریکا بریم و اونجا رو اسلامی کنیم
🔴
همزمان میتوتیم به شرق آسیا هم لشکرکشی کنیم
🔴
یک لشکر هم میتونیم به استرالیا روانه کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/140483" target="_blank">📅 23:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140482">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1qaZneA-HFhFicbOONDyeq8EIdckkvjwGNywaISv9dSOuYSIHDGS0AqoNc0fhj-ppFOO5S1MdKOeNcIZaaNhJ6FWy8UtOsHYWQXHQ8HeXRC6N-AfGmUdd1whW72fLJrsEB4yxTNQ4FaIRSHfphf0yrBd2lxWzjmF-4axYAEe-itrzpiZ09udHUEzOyqO1uAuottYxtdyJ9Br9vCwXzA6Nm4r1CTzGbRXlHo97eTCAdRBxo2zT0WvHETqUrgNXvLIG1b3eixz7-yaq2_aylfFhLzCaR2aSHvBEy7jcvH6TV0Q3LR7qbLmSkaHULnEejY2KATBIWWpPpOVe2gSrh1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خرازی: باید ابتدا اروپا رو فتح کنیم بعد از راه دریا به آمریکا بریم و اونجا رو اسلامی کنیم
🔴
همزمان میتوتیم به شرق آسیا هم لشکرکشی کنیم
🔴
یک لشکر هم میتونیم به استرالیا روانه کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/140482" target="_blank">📅 23:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140481">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ولودیمیر زلنسکی رئیس‌جمهور اوکراین در صربستان با وویچ، رئیس‌جمهور صربستان، دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/140481" target="_blank">📅 23:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140480">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca22d0550c.mp4?token=duFwZupb_AZsiagLGRIz1oJXSNhKJSM6BHfex0QGw6mIRsmdVwXE1yvd2ED1vJNpdXNF22SgLjIJDbZbITdP9ZtZzQiy7Gwuakz4_-lCTpAnjx40kaTILuINXpfko4mNHA1GeGEHFQU5RnLgtj6IDdgYsX0RS6ivXWc-SkEVSDHJre_h87SaC_li8KaGUlmKdNxb8bfStaZWOTXPzopkzpwTGZHiwIrKwlKH0zxovfk0_SMHrvApIXhuZkKtme33V3wo0ITQIxh2mOxcgMbHPkNOCFk9_m-LEs52plWlo7M-sIgOrf6ECG62LiKohjKHtSfDkIfBnoeJrVLLs250iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca22d0550c.mp4?token=duFwZupb_AZsiagLGRIz1oJXSNhKJSM6BHfex0QGw6mIRsmdVwXE1yvd2ED1vJNpdXNF22SgLjIJDbZbITdP9ZtZzQiy7Gwuakz4_-lCTpAnjx40kaTILuINXpfko4mNHA1GeGEHFQU5RnLgtj6IDdgYsX0RS6ivXWc-SkEVSDHJre_h87SaC_li8KaGUlmKdNxb8bfStaZWOTXPzopkzpwTGZHiwIrKwlKH0zxovfk0_SMHrvApIXhuZkKtme33V3wo0ITQIxh2mOxcgMbHPkNOCFk9_m-LEs52plWlo7M-sIgOrf6ECG62LiKohjKHtSfDkIfBnoeJrVLLs250iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما این‌قدر آدم داریم که من کل روز اینجا می‌مانم. اگر می‌توانید سریع بروید، ممنون می‌شوم چون ما یک جنگ برای پیگیری داریم، باشه؟ این بهانه من برای کمی زودتر از اینجا خارج شدن است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/140480" target="_blank">📅 23:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140479">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6987dc0f6.mp4?token=ESWuNF1SpTRgDBa2qpvl7w4NreKIaXYR4njJE6GxYLqzMIpWR8pW7hMbvx3o21b6akHQfdiZk4-1rXzgTazLkwqY2rUh_pFdMR-oNBnk33X1QmVpqF-A_8GYdz1Z_XXzqgDL468WI4trCe6PgrD5cnwTAXKm_L9k0smQywzUGpllyz8ZtKk0jz2sJYfJmkPTO4-Xx0HX-i4il8czrApH8VcOZ1c5ANhu1H1FWnaD1jABWwxR4Lmow1PYE8GMxT9Ey68EyunKtJagBo0i3zp4kMBQQHadgwgSRG_B2oZvOUuGqerugJiZ3uYrisvP5ecjfWWilLxSvnHpddOpFlb2jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6987dc0f6.mp4?token=ESWuNF1SpTRgDBa2qpvl7w4NreKIaXYR4njJE6GxYLqzMIpWR8pW7hMbvx3o21b6akHQfdiZk4-1rXzgTazLkwqY2rUh_pFdMR-oNBnk33X1QmVpqF-A_8GYdz1Z_XXzqgDL468WI4trCe6PgrD5cnwTAXKm_L9k0smQywzUGpllyz8ZtKk0jz2sJYfJmkPTO4-Xx0HX-i4il8czrApH8VcOZ1c5ANhu1H1FWnaD1jABWwxR4Lmow1PYE8GMxT9Ey68EyunKtJagBo0i3zp4kMBQQHadgwgSRG_B2oZvOUuGqerugJiZ3uYrisvP5ecjfWWilLxSvnHpddOpFlb2jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
ما مشکلی با اینتل داشتیم. آن‌ها ۱۰ درصد از شرکت را به ما دادند. از زمانی که شرکت را در اختیار داشتیم، سهام آن چندین و چند برابر رشد کرده است. ما ۸۲ میلیارد دلار سود کردیم. آیا من بابت این موفقیت اعتباری دریافت می‌کنم؟ خیر.
🔴
به هر حال، این برای کشور است، نه برای من.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140479" target="_blank">📅 23:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140478">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ: می خواهید باور کنید یا نکنید، اما من یک طرفدار محیط زیست هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/140478" target="_blank">📅 23:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140477">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b30c2de122.mp4?token=tASkx6JdCfx2D2YnfWgX-g6Ysc4gjNk4UNFT3Uz5UXT_-c4L1gHS2tEbbKqedgtgaWFYKzLO_eIzGbkAfbu4yYmiFlOmWtdn0MnrlM-GxauITu2YpP3tTuTyBZdTJs9fFQFzxI_1C9eOuI4ICrwyw8pMBVFVgS44ue2Lm7-m4g1yFc_bcApVJhcEAuM3--NnUS7PbkqxyRbIM3ZPs10Sr3fFsHhizA_KNTn1NU7FdJXlyw1H6mCEdwrtrwCJqphckCdrr7f6txUVIfGxHxDRT4OzKEOnMaanGrKCA7qpCAcudLvCRb37MscJYC7GmHSzQIILvtwjV-3QKVVKqJffsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b30c2de122.mp4?token=tASkx6JdCfx2D2YnfWgX-g6Ysc4gjNk4UNFT3Uz5UXT_-c4L1gHS2tEbbKqedgtgaWFYKzLO_eIzGbkAfbu4yYmiFlOmWtdn0MnrlM-GxauITu2YpP3tTuTyBZdTJs9fFQFzxI_1C9eOuI4ICrwyw8pMBVFVgS44ue2Lm7-m4g1yFc_bcApVJhcEAuM3--NnUS7PbkqxyRbIM3ZPs10Sr3fFsHhizA_KNTn1NU7FdJXlyw1H6mCEdwrtrwCJqphckCdrr7f6txUVIfGxHxDRT4OzKEOnMaanGrKCA7qpCAcudLvCRb37MscJYC7GmHSzQIILvtwjV-3QKVVKqJffsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در ایتا از مجتبی خامنه‌ای رونمایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/140477" target="_blank">📅 22:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140476">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پزشکیان : من نه تنها از شهادت نمی‌ترسم، بلکه اون برای من یک پیروزی بزرگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/140476" target="_blank">📅 22:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140475">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
آمریکا در اقدامی مبتنی بر اتمام ذخایر و ظرفیت تولید موشک های رهگیر، مجوز فروش سریع حدود ۵۰۰۰ هزار رهگیر پدافندی را به کشور های عربی صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/140475" target="_blank">📅 22:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140474">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
پزشکیان: از قالیباف خواهش کردیم که رئیس تیم مذاکره‌کننده شود/ آقای عراقچی علیرغم توهین‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ها، شبانه‌روز کار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/140474" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140473">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مقام آمریکایی به رویترز: به محض اعلام توافقی برای ازسرگیری بدون مانع کشتیرانی تجاری، محاصره بنادر ایران را لغو خواهیم کرد
🔴
مذاکرات بین عمان و ایران درباره تنگه هرمز پیشرفت داشته است و انتظار توافق زودی را داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/140473" target="_blank">📅 22:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140472">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
پزشکیان: برای اینکه بتوانیم بمانیم، باید بدانیم چه می‌کنیم؛ چه زمانی می‌خواهیم بجنگیم، چه زمانی صلح کنیم و چه زمانی هر طرف کار خودش را انجام دهد؛ نه جنگ باشد و نه صلح.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/140472" target="_blank">📅 22:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140471">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پزشکیان: ما یک بدن و یک قدرت واحد هستیم و تکه‌تکه نیستیم. کسانی که می‌خواهند بخش‌های مختلف را از یکدیگر جدا کنند، به‌دنبال ایجاد تفرقه و شکاف در جامعه‌اند.
🔴
بر همه کسانی که در این کشور زندگی می‌کنند، یک مجموعه مقررات، قوانین و یک رهبری حاکم است؛ نه اینکه هر گروهی برای خودش خانی تشکیل دهد. بااین‌حال، گاهی عده‌ای نمی‌خواهند این واقعیت را بپذیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/140471" target="_blank">📅 22:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140470">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfxH0LxbEWrUaJCHbSbwFSAlxt3Ic2V2TwTV1ho1l_Zto7AeUy2Jqri0Wvc9bzKANOQIYVKqTWQR_kJ3cCme6aViCF45xTtWv9V-uOp8F56iFGNPWLq5ozGxq2dhAA2tO6TIWlXqxTBpM8Y1zAMjiTl2nmlxqYsXl6vyk174a63oBmjEZAOeACjUK29LLEXFOIq6aMF4lm3hXXAnexICMSqh6EVnIDb_fIKh6wdRP8s2iTrFsfUr_L_2MOygWTQoC-h1GNBfNQQhflLtsdfU1LEAkMkgWcL8FFDtkbr4y7_grD3Z-1B_tOrNvnGZ4mSBakqj6rc_X934LMYSTOURog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: ایران آغازگر جنگ نبود و همراهی مردم، محاسبات دشمن برای فروپاشی کشور را برهم زد.
🔴
امروز ایران با قدرت و انسجام بیشتری مسیر خود را ادامه می‌دهد. دشمن روی فروپاشی ایران حساب کرده بود، اما ناکام ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/140470" target="_blank">📅 22:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140469">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
پزشکیان: این اروپایی‌ها بودند که موضوع اسنپ‌بک را پیش بردند و این مسئله در ابتدا به ترامپ ارتباطی نداشت.
🔴
ما با آن‌ها به توافق رسیدیم، اما ظاهراً باید از طرف دیگری اجازه می‌گرفتند و در نهایت نپذیرفتند.
🔴
این نشان می‌دهد حتی اروپایی‌ها نیز برای تصمیم‌گیری اختیار کامل ندارند؛ چون اگر اختیار داشتند، ما با آقای مکرون تفاهم کرده بودیم و میان توقعات آن‌ها و خواسته‌های ما هماهنگی به وجود آمده بود
🔴
مشکل اینجاست که آمریکا از خاک کشورهای منطقه به ما حمله کرده و پایگاه‌ها و مراکز ما را هدف قرار داده است.
🔴
سؤال این است مدرسه میناب را از کجا زدند؟ از همان کشورهای مسلمان و دوست ما.  چرا آنها باید اجازه بدهند بیایند و ما را بزنند؟ ما نمی‌خواهیم آن کشورها را هدف قرار دهیم؛ جایی را می‌زنیم که از همان‌جا به ما حمله می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/140469" target="_blank">📅 22:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140468">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
پزشکیان : با امر و نهی نمیشه جامعه رو به درستی اداره کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/140468" target="_blank">📅 22:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140467">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca37ce2571.mp4?token=lNtSn6OQV9pXArXeyVYOFfFdauV89rE4eha-CrTKiwc9We1bYdT3f_K4ND1NYI3kUlNDqbKC616ofRdK7OVPpKvDY9_GXTevUGcXearpzheXj5hwtDod3k-X3LaUymWfd3m3ey_Mnm4AXq0IsRZC6Oh7Ea-cvsAWbkNQ3oWFRUvQ9TMzsLdzFbtj_BgYNPLyLkTcWUAlDnOvsewD_LkL9h6ihF6uDPGx4gqL6Y0uKvgnvRolwFksGNraq7ZZBqgFIJzZf6nU1mFHK0fBA7uiQviRvediH8HafpZElZ7VmgQGax6Vab1UYVQE71ymPjKa1W7nmOWo2pMtZjTBYfIrzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca37ce2571.mp4?token=lNtSn6OQV9pXArXeyVYOFfFdauV89rE4eha-CrTKiwc9We1bYdT3f_K4ND1NYI3kUlNDqbKC616ofRdK7OVPpKvDY9_GXTevUGcXearpzheXj5hwtDod3k-X3LaUymWfd3m3ey_Mnm4AXq0IsRZC6Oh7Ea-cvsAWbkNQ3oWFRUvQ9TMzsLdzFbtj_BgYNPLyLkTcWUAlDnOvsewD_LkL9h6ihF6uDPGx4gqL6Y0uKvgnvRolwFksGNraq7ZZBqgFIJzZf6nU1mFHK0fBA7uiQviRvediH8HafpZElZ7VmgQGax6Vab1UYVQE71ymPjKa1W7nmOWo2pMtZjTBYfIrzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جیغ جیغ کردن یه زن چادری فضول توی ایستگاه مترو بخاطر پوشش اختیاری خانم ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/140467" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140466">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
پزشکیان: ما با کشورهای مسلمان برادریم؛ برای چه باید با آن‌ها بجنگیم؟ من واقعاً نمی‌فهمم. نه‌تنها با کشورهای مسلمان درگیر می‌شویم، بلکه در داخل کشور خودمان نیز با یکدیگر می‌جنگیم و همدیگر را قبول نداریم.
🔴
خب، تو از من بهتری؛ پاداشت را خدا می‌دهد. چرا بر من منت می‌گذاری؟ چرا برای من قیافه می‌گیری و به من امر و نهی می‌کنی؟ چه کسی گفته است که تو باید به من امر و نهی کنی؟ تو خوبی، الحمدلله؛ به من هم خوبی کن، اما بدون منت، همان‌گونه که قرآن می‌فرماید؛ برای خدا، نه اینکه بیایی به دیگران امر و نهی کنی که باید این کار را انجام دهید یا آن کار را نکنید. این رفتار موجب فرار مردم از دین و باور می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/140466" target="_blank">📅 22:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140465">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نبویان، نماینده مجلس در مورد توافق مکه: همانطور که پایگاه های آمریکا نتوانستند عربستان را نجات دهد، سعودی ها باید بدانند آویزان شدن به نوکران آمریکا هم شما را نجات نخواهد داد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/140465" target="_blank">📅 22:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140464">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
پزشکیان: چون نگاه‌های ما بسته شده و تصور کرده‌ایم کسی که ما او را مذهبی می‌دانیم، خودی است و دیگری غیرمذهبی و غیرخودی، نتوانسته‌ایم همه را جذب کنیم
🔴
در رابطه با همسایگان، بسیاری از مشکلاتمان را حل کرده‌ایم و روابط بسیار بهتر شده است.
🔴
اکنون، با جنگی که شکل گرفته، اسرائیل و آمریکا تلاش می‌کنند کشورهای خلیج فارس را علیه ما متحد کنند و ما نیز در تلاش هستیم اجازه ندهیم این اتفاق رخ دهد.
🔴
البته در داخل کشور نیز چالش‌هایی داریم؛ چون همچنان نگاه‌های متفاوتی وجود دارد و طبیعتاً آمریکا و اسرائیل از این وضعیت سوءاستفاده می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/140464" target="_blank">📅 22:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140463">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت آحرونوت: فرمانده منطقه شمال به حزب الله دستور داد پرتاب یک پهپاد انفجاری به سمت نیروهای اسرائیلی را در 24 ساعت گذشته پنهان کند و جزئیات بیشتری از فعالیت این نیروها منتشر نکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/140463" target="_blank">📅 22:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140462">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رمضان‌زاده، سخنگوی دولت اصلاحات: باید جمهوری اسلامی خودش را به پیمان‌نامه دفاعی «مکه» الحاق کند تا اولین پیمان‌نامه بدون حضور اسرائیل امضا شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/140462" target="_blank">📅 22:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140461">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2yyHxPRVYuRJcLd5LeKM7cmRI_obWiInGmTRPmwiTWpqHCgCXIIc1iG_tKCUuOe9SheShsK7enQcHTPZi67-VJPhOA0ifIFvRa_P810wx1gBFcguwwvczDO3Ng9i45WWgS4y251I1hxknPXTEQ9DMKG_rGkVh70h3Fw0SaEA6_EncyNhwFaT14a2A_CtORlTGsQE-jiHKIM7-t0u1SVnbJNXfh-vJLZF82crqBHJw8x9x4JuNzewVacz5Cp3QltiziN5mgCRfeGZ-je4KZjKlcChc1ROenobbTBqQiOoF7Buas97ugE8_LsdD38RoARMgkidvjVB_4nvY_sEgH64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر وارد کانال ۱۸۶ هزار تومان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/140461" target="_blank">📅 21:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140460">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBlRbu5xeKo7wdflnA66IDx-3uFAUPxupcgTdWaPvkKJnf55VCe8aaT4oOtw9EkDV7QyWOXasbNymHCODlkZQsf8flmBZ16smnHcRbJKGBT2cOC9Q6uXbmj-9GONobGY4-92eojeEtllx1xFKF8p5ziBe7HoOnIWT7-L_t3Zir2BCJmKxTZZ7AbT2n11mu42MFzobWThi523ityaYs0OWL7X38AkawHPAhkKt-xoWC3nMnp-mqx463Jd2k2QenObpGDXvyLJ2Fo4s4N0IaRb5goXQk0TPe4kyyRRofQvDhBkgmpIcqVPK2QDu3aQH5Glfjk3rexL6edbl0ylPnscgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی
:
نیروهای مسلح قدرتمند ایران آمادگی، توانایی و قدرت خود را در برابر گران‌ترین ارتش جهان به رخ کشیدند.
🔴
وقتی مسلمانان متحد شوند، می‌توانیم با هر چالش و تهدیدی از سوی بیگانگان کینه‌توز، رویدَررو مقابله کنیم.
🔴
زمان آن فرا رسیده که تنها به خودمان متکی باشیم و برادری واقعی را در آغوش بگیریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140460" target="_blank">📅 21:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140459">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
عربستان سعودی در طول ۳۸ روز اول درگیری، حدود ۸۶ درصد از ۲۸۰۰ موشک رهگیر PAC-3 خود را مصرف کرد و در ماه آوریل، تنها ۴۰۰ موشک باقی مانده بود.
🔴
ایالات متحده آمریکا نیز بین فوریه و جولای، حدود ۶۵ درصد از موشک‌های رهگیر پاتریوت خود را مصرف کرد و تعداد آن‌ها به کمتر از ۸۵۰ رسید، در حالی که قبل از جنگ با ایران، ۲۳۳۰ موشک رهگیر در اختیار داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/140459" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140458">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
المنار: بمباران توپخانه اسرائیل شهر المنصوری در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/140458" target="_blank">📅 21:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140457">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سازندگی : رئیس‌جمهور با استعفای "محمدباقر ذوالقدر" از دبیری شورای ‌عالی امنیت ملی موافقت نکرده است و به او گفته که کماکان به مأموریت محول‌شده با قوت و قدرت ادامه دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/140457" target="_blank">📅 21:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140456">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEjz0j8vkcOvpEK8IM9fulzaTKwVuDNW1mCImWpa4YFg_ua9bvrexdIbPKKjoJU-aUGlPG5dFsDvfBEMneFj7InVE_ryAFmjShhOuto07v0LWbEdU_MDlb64SfwI-QAAzmhX8Yxovz9rtMsRmuKFjWfxDdxl_aCHaPiAkVkscyOQlA3lBmGwBravXRcnrfeG2sMXgPR9sDuUVxKwlmNhJkzDiCFpC00SxdMbdKBoiBjRsJ5wt2h80fQFgwzA9kHNYM0L7mtiNPNj6Lz-JTlz-lQXIFQFjyvgJc_FTncgJfWgB5T1hH9WYbLiyTjr_I89Fed_3lONSW8qVFLAmWwOLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: مذاکره‌کنندگان ایرانی منتظر تایید نهایی شعام در مورد توافق با عمان و آمریکا هستند.
‏
🔴
«انتظار داریم این تایید به زودی انجام شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/140456" target="_blank">📅 21:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140455">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رسانه‌های عراق اعلام کردند که رئیس سازمان اطلاعات عربستان با علی فالح الزیدی نخست وزیر عراق دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140455" target="_blank">📅 21:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140454">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سنای آمريكا لايحه تحريم‌های گسترده انرژی روسيه را با ۸۶ رای  برابر ۱۱ رای تصويب كرد و آن را به مجلس نمايندگان فرستاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/140454" target="_blank">📅 21:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140453">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBJSKBT2kjvrcamFhKE6fWY7o2W5_D91I-NT2V_uqAvhgIHP9anBp9iyaBEkGwAksLa1wSZ3jKSU5qiq83vEfnRgmNKN5WYSz6fv5K1dZXAaik7VL8WdQhrCvynENv_t4zDck8dNxY8dIO-B9-H_qPkGxWJk_5YAWbhP509Zf5dUyuxrRE2ny5EE4S-w9Apv0rG_JwID0oGzMj2fQZTDo__Yc6fiTI3582MAfF33X0JGNawO0OxyPueaN-d4Xz3BOVkNOS0O4hGc5gd3LqWlwEyBh9stPoHgU_gGpSCCF-wYJRaS44BiMPU-XTEWNxJOqhNhGpNiD9bUTOc8_GEqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: پرونده «مرکز نظامی» واشنگتن را به دیوان عالی آمریکا می‌بریم
🔴
دونالد ترامپ اعلام کرد دو قاضی دادگاه تجدیدنظر فدرال که در دوره‌های باراک اوباما و جو بایدن منصوب شده‌اند، علیه ایجاد آنچه او «مرکز نظامی ضروری برای امنیت ملی واشنگتن و آمریکا» خواند، رأی داده‌اند.
ترامپ این حکم را «ناعادلانه» توصیف کرد و گفت دولتش فوراً به دیوان عالی ایالات متحده اعتراض خواهد کرد تا این تصمیم به‌طور کامل لغو شود. توصیف این مرکز به‌عنوان ضرورتی برای امنیت ملی و همچنین «ناعادلانه» بودن رأی دادگاه، موضع شخصی ترامپ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/140453" target="_blank">📅 21:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140452">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
یان برمر، تحلیلگر امریکایی: «توافق‌نامه دفاع مشترک مکه» مسیری کاملاً متفاوت با پروژه توافق‌های ابراهیم در خاورمیانه را نشان می‌دهد
🔴
یان برمر، تحلیلگر امریکایی نوشت: عربستان سعودی، ترکیه و پاکستان با تشکیل یک پیمان دفاعی، که عملاً می‌توان آن را هسته مرکزی یک ائتلاف اسلامی دانست، در حال پاسخ به جنگ آمریکا و ایران و این برداشت هستند که دیگر نمی‌توان برای تأمین امنیت منطقه به ایالات متحده تکیه کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/140452" target="_blank">📅 20:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140451">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
بقائی در واکنش به سخنان ترامپ: پیش از آنکه کسی بتواند ادعای «غنائم جنگی» کند، ابتدا باید در جنگ پیروز شده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/140451" target="_blank">📅 20:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140450">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
جنبش انصارالله اعلام کرد که یک حمله موشکی بالستیک و با استفاده از پهپادها علیه اردوگاه «صحن‌الجین» متعلق به نیروهای مسلح یمن وابسته به شورای انتقالی جنوب (PLC)، در شمال شرقی شهر مأرب، در یمن، انجام داده است.
🔴
این حمله به طور خاص به نیروهای یمنی و " مزدوران" (احتمالاً نیروهای سعودی) و همچنین انبارهای، خودروها و تجهیزات نظامی هدف قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/140450" target="_blank">📅 20:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140449">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27c2dba3c0.mp4?token=sWi5Tmwus1fXE96mwF-KvUvj94NwvHHJjD1fa9XD9bIMYlxL1VXxTY-22h_k89_nYo1JINlSWKXOem727OxWRzgoOgtuzOybNZhMaO6HueJgkqrAXaTAAY8yGRuNZ39tnjbE4XlRZCOboaNos9TAoVdC8mVn-J6j3Fa6-IpIxZoln3kO9y-9lhs2eVukyQL5vde6jEy4xCh8Hz8D_LLzqG57HPI4FMuvBwYgF2I5--QrEL8l7OTElzCa1pf4Bq4dK55_CS-q40_UKj19ke_Ea3iN4z7z5lyOmBN7V4vJJq2ZbBaAPRARstR0old1xSeIrDQw9elbK-t5ljYygdw7hodmSMvCKfVVlb3J4gwXAU2dpOcy_IFyq0DT-7VCW_RFJaeOHyyzi4eKEbGninCfjHobjpjraaUnqx7HtcSwwY0afk5H3luuwmqtHQk83TesRG914ONS0MVRViPjg5MQz3stbQmNTexDMrzTYALFwsQurh8AVDFxB0_E76xEgBqIoC0NfpOOlhPbgJl8D296hPdh5Y7TZLjSVy40ypoy7-PXiYZvQlla8dgiNNvV8MGPMvnHyTBBEwvoMV9lIcFTWLBAdvchJ4v3dRTd-AKGfygW8x2TdtrU6HYPRjZGz5Hdc5_410e-5t2y4z5yxVa86vs2yOJQ_XvwUNMBq7W7NTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27c2dba3c0.mp4?token=sWi5Tmwus1fXE96mwF-KvUvj94NwvHHJjD1fa9XD9bIMYlxL1VXxTY-22h_k89_nYo1JINlSWKXOem727OxWRzgoOgtuzOybNZhMaO6HueJgkqrAXaTAAY8yGRuNZ39tnjbE4XlRZCOboaNos9TAoVdC8mVn-J6j3Fa6-IpIxZoln3kO9y-9lhs2eVukyQL5vde6jEy4xCh8Hz8D_LLzqG57HPI4FMuvBwYgF2I5--QrEL8l7OTElzCa1pf4Bq4dK55_CS-q40_UKj19ke_Ea3iN4z7z5lyOmBN7V4vJJq2ZbBaAPRARstR0old1xSeIrDQw9elbK-t5ljYygdw7hodmSMvCKfVVlb3J4gwXAU2dpOcy_IFyq0DT-7VCW_RFJaeOHyyzi4eKEbGninCfjHobjpjraaUnqx7HtcSwwY0afk5H3luuwmqtHQk83TesRG914ONS0MVRViPjg5MQz3stbQmNTexDMrzTYALFwsQurh8AVDFxB0_E76xEgBqIoC0NfpOOlhPbgJl8D296hPdh5Y7TZLjSVy40ypoy7-PXiYZvQlla8dgiNNvV8MGPMvnHyTBBEwvoMV9lIcFTWLBAdvchJ4v3dRTd-AKGfygW8x2TdtrU6HYPRjZGz5Hdc5_410e-5t2y4z5yxVa86vs2yOJQ_XvwUNMBq7W7NTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آمریکا سالانه ۴۰ میلیارد دلار به سوئیس می‌دهد؛ بدون ما با مشکلات جدی روبه‌رو می‌شوند
🔴
دونالد ترامپ مدعی شد آمریکا عملاً به برخی از ثروتمندترین کشورهای جهان یارانه می‌دهد و سوئیس را یکی از این کشورها دانست. او گفت ایالات متحده سالانه حدود ۴۰ میلیارد دلار در اختیار سوئیس قرار می‌دهد و بدون این مبلغ، این کشور دیگر جایگاه فعلی خود را نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/140449" target="_blank">📅 20:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140448">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ: خیلی‌ها می‌گویند من یکی از بزرگ‌ترین رؤسای‌جمهور تاریخ هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140448" target="_blank">📅 20:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140447">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
تصاویر جدیدی از توقف کشتی‌ها در شمال تنگۀ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/140447" target="_blank">📅 20:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140446">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f48f2a3f4.mp4?token=H_rxKHCXdmwN6-GvNT7FYqVIHVJN6L2PK4FKtcBkCqnfQLq19fvkPl3TxDRR8M-7GAVq4kNeU39Y7fq45uzNyc6jYNvaL0h5nQyc7wYyK5ouoWN3xsUdLs1ZZ6fxmskmWpH-bDV07RrM_Gz5Vdx4m-D8JyhOwgn8SEKMGUFqT1zXwYo3eOLGfR7w3aejLRamI0oBmsYaNdHdKfLvS0cBOvH7PpL3jH2Hx1T0e4U28QRJkAD4_MphykatOKHIyGOh00OOgtUAG6CYhXHThKRmm4NAHbt-ZXwyTUZFTcrKzfl08MQk57g3MtZFRmGxyXW0dZMy41DBVa9mQOJCL71Mqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f48f2a3f4.mp4?token=H_rxKHCXdmwN6-GvNT7FYqVIHVJN6L2PK4FKtcBkCqnfQLq19fvkPl3TxDRR8M-7GAVq4kNeU39Y7fq45uzNyc6jYNvaL0h5nQyc7wYyK5ouoWN3xsUdLs1ZZ6fxmskmWpH-bDV07RrM_Gz5Vdx4m-D8JyhOwgn8SEKMGUFqT1zXwYo3eOLGfR7w3aejLRamI0oBmsYaNdHdKfLvS0cBOvH7PpL3jH2Hx1T0e4U28QRJkAD4_MphykatOKHIyGOh00OOgtUAG6CYhXHThKRmm4NAHbt-ZXwyTUZFTcrKzfl08MQk57g3MtZFRmGxyXW0dZMy41DBVa9mQOJCL71Mqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی برای اولین‌بار از زمان شروع جنگ، وارد صربستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/140446" target="_blank">📅 20:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140445">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وزارت ورزش و جوانان : ۱۸ میلیون زن و مرد ایرانی بدون حتی یک بار ازدواج وارد ۴۰ سالگی شدن.
🔴
بخاطر شرایط اقتصادی و کسب تجربه از زندگی مشترک دیگران و هم چنین لذت بردن از تنهایی،بسیاری از جوونای ایرانی ترجیح میدن هرگز ازدواج نکنن و تا آخر عمر تنها بمونن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/140445" target="_blank">📅 20:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140444">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d279dcf86.mp4?token=rzJRy2i-K1MgQZ09LXNLzAznZol9ihXqHZVIN7GinoFAAWwOBNjO0n5AQzjFOjTmyT_vrkQyf58AFYIES_Qq3DJlBbS53DfAH2WRUQ8gYrRO1JnGJdWxTX5fxz7ML24MuFUsvgVmnTKCxixYre--QXgUyQ-P1xAdSe1MeUquMiOxkVwKKwPYa8I3eJt_w6Eny4xFhVP32xRQMUPaSS6Vt9Hl6WRKrl7s23srhw0b74VBECSKe6nO4WNU6xmhzrV6qALU_kyF5Q01wuKfWbVOh4J34rS9AVwHmjUV4WGuzPfsTX5fzwDg10m3B72t7o44KHIgfNK3T7y1vNWgK28jUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d279dcf86.mp4?token=rzJRy2i-K1MgQZ09LXNLzAznZol9ihXqHZVIN7GinoFAAWwOBNjO0n5AQzjFOjTmyT_vrkQyf58AFYIES_Qq3DJlBbS53DfAH2WRUQ8gYrRO1JnGJdWxTX5fxz7ML24MuFUsvgVmnTKCxixYre--QXgUyQ-P1xAdSe1MeUquMiOxkVwKKwPYa8I3eJt_w6Eny4xFhVP32xRQMUPaSS6Vt9Hl6WRKrl7s23srhw0b74VBECSKe6nO4WNU6xmhzrV6qALU_kyF5Q01wuKfWbVOh4J34rS9AVwHmjUV4WGuzPfsTX5fzwDg10m3B72t7o44KHIgfNK3T7y1vNWgK28jUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان:
من اگر بخواهم استعفا بدهم رسما اعلام می‌کنم!
🔴
آنهایی که به تفاهم‌نامه می‌گویند شکست، حرف اسرائیل را می‌زنند
🔴
برای جهالت انسان همین قدر کافی است که نداند قدرتش چقدر است.
🔴
یا رهبری را نشاختند یا منطق و عقل سرشان نمی شود. ما به آمریکا چه دادیم؟! کلی دستاورد داشتیم.
🔴
آنچه به اسم تفاهم نامه نوشتیم با قدرت از آن دفاع می کنیم، آنهایی که می خواهند آن را شکست لقب بدهند من می گویم که بی انصاف هستند و این چیزی است که اسرائیل می خواهد و دانسته یا ندانسته دارند پیام منتقل می کنند.
🔴
کنار گود ایستادند و  می‌گویند این جوری است و فردا هم اگر مشکلی پیش بیاید باز هم می گویند چرا این جوری شد.
🔴
از اقتصاد نظر می دهند، از سیاست نظر می دهند، جامعه شناسی نظر می دهند. من نمی دانم این علم را از کجا آورده اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140444" target="_blank">📅 20:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140443">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
غریب آبادی: امنیت خلیج فارس باید به دست کشورهای منطقه تأمین شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/140443" target="_blank">📅 20:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140442">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت
🔴
تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت، زیرا ایرانی‌ها از آن به عنوان یک گلوگاه استفاده کرده‌اند، یا تلاش کرده‌اند از آن به همین منظور استفاده کنند.
🔴
آنچه در دو سال آینده شاهد خواهیم بود، این است که تنگه هرمز از اهمیت خود کم خواهد شد.
🔴
این تنگه به یک آبراه معمولی تبدیل خواهد شد، و من معتقدم که بیش از ۵۰ یا ۷۰ درصد از انرژی که در حال حاضر از طریق این تنگه منتقل می‌شود، از طریق خطوط لوله زیرزمینی منتقل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/140442" target="_blank">📅 20:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140441">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WZX-DWKVVdumy-5MkS9wqtYlMFtVCJg4rAF8IF5GP4pLCNipkE1H3LhtjH8nDqDx3wvnHofWSu3jmqO--YKV1Ks3jVd0a2QvMUKOpd1gHL435T22vc9gQ0H2y_xqesUWy8jOwvr9JSvCiSlp8zlqbX3dl5hg-wm31TW4MS0FgHFj8R-Zrbt6y5FwOGm1LMu855E53pHNFaGDVG8b7zHLPzPifFXDWxE9PTuuBBkFpb5BcBz3xeo0hAeITH_Cagl9cowm_1Xw3NoTWUysiTmmigNzPYKjQHXPLiPkGNxNOt56z3hSCbmxg3gsVmkxOEsd_ogwWF9fnsnu5HFzdeHBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنبش مقاومت اسلامی عراق اعلام کرد که عملیات برنامه‌ریزی‌شده علیه پایگاه‌های عربستان سعودی و آمریکا در غرب آسیا را به تعویق می‌اندازد، این اقدام در پاسخ به فراخوان قبلی مطرح‌شده توسط هادی العامری و سایر رهبران سیاسی عراقی صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/140441" target="_blank">📅 19:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140440">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وزارت خارجه آمریکا در بیانیه‌ای اعلام کرد اقدامات جدیدی برای قطع مبادلات مالی با ایران انجام داده است.
🔴
‏در بیانیۀ وزارت خارجه آمریکا آمده: اقدامات ما شبکه‌ای از شرکت‌های مبادله مالی و شرکت‌های صوری که به ایران برای نقل و انتقال میلیون‌ها دلار پول کمک کرده‌اند را هدف قرار می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/140440" target="_blank">📅 19:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140439">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8367154b7.mp4?token=ilnuMiAadNaSc0oCGPrD2ZJg8W3RYfeKwD8kkfRMwjrBZ19b8MyabVpYRgyhunXdxP8u3LQSRBTrZkVSzCDBpCF96qWZykV-Hj2iip4o-Q_ze3eU7m794WAs2AWSoNrx_UtdHZsv_lD8A2VBMWdchbjxUCc6kXL2tTcvtfERF3F3gAa1vpyK4vFtG8MrOL72JbKTRku4EPQkqZpY_6lpICgXTIcg9TqeU0hs_cQYDva61CDNF8LthU_8TQv8Ppjwys7KWj1_CddzLIXbljK02_a9bQfoWwhAhPQVkqpoZJfM1A8eF-jAhuOb_N03moH-SjB06kCUNACB2VKL5DEWiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8367154b7.mp4?token=ilnuMiAadNaSc0oCGPrD2ZJg8W3RYfeKwD8kkfRMwjrBZ19b8MyabVpYRgyhunXdxP8u3LQSRBTrZkVSzCDBpCF96qWZykV-Hj2iip4o-Q_ze3eU7m794WAs2AWSoNrx_UtdHZsv_lD8A2VBMWdchbjxUCc6kXL2tTcvtfERF3F3gAa1vpyK4vFtG8MrOL72JbKTRku4EPQkqZpY_6lpICgXTIcg9TqeU0hs_cQYDva61CDNF8LthU_8TQv8Ppjwys7KWj1_CddzLIXbljK02_a9bQfoWwhAhPQVkqpoZJfM1A8eF-jAhuOb_N03moH-SjB06kCUNACB2VKL5DEWiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عطریانفر: پوست قالیباف به اندازه‌ای کلفت است که خیلی نگران اهانت تندروها به او بابت مذاکره و توافق نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/140439" target="_blank">📅 19:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140438">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کانال ۱۴عبری: شواهدی از وخامت حال مجتبی خامنه‌ای وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/140438" target="_blank">📅 19:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140437">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
عبدالرضا داوری: ایران به توافق مکه وارد نمی شود، چون قدرت ایران ناشی از استقلال آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140437" target="_blank">📅 19:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140436">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع در وزارت خارجه پاکستان: به احتمال زیاد، عباس عراقچی، وزیر امور خارجه ایران، روز دوشنبه به پاکستان سفر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140436" target="_blank">📅 19:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140435">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
به گزارش هیل، دونالد ترامپ گفت رأی‌دهندگان حزب جمهوری‌خواه در آستانه انتخابات میان‌دوره‌ای از عملکرد جمهوری‌خواهان حاضر در کنگره ناراضی و خشمگین هستند.
🔴
ترامپ مدعی شد این نارضایتی متوجه او نیست، بلکه متوجه نمایندگان جمهوری‌خواه در کنگره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/140435" target="_blank">📅 19:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140434">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
خبرنگار ارشد کاخ سفید: سنای ایالات متحده رسماً بررسی تحریم‌های سنگین علیه روسیه و ایران را آغاز کرده است.
رأی‌گیری نهایی ممکن است امروز برگزار شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/140434" target="_blank">📅 19:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140433">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
پایگاه اینترنتی نیروی دریایی ترکیه: یک کشتی باری با پرچم ترکیه در سواحل بندر نووروسیسک روسیه هدف حمله پهپادی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140433" target="_blank">📅 19:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140432">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
معاون وزیر امور خارجه : اگر به شرایط صلح برگردیم، احتمالاً جلسات امنیتی بین کشورهای منطقه برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/140432" target="_blank">📅 19:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140431">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
المیادین: اطلاعات اولیه حاکی از آن است که نیروهای مسلح یمن یک عملیات جدید را علیه اردوگاه‌های سعودی انجام داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/140431" target="_blank">📅 19:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140430">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
اوپن سورس(رسانه نزدیک به ارتش آمریکا) : حال مجتبی خامنه ای مجددا رو به وخامت رفته و هرلحظه ممکنه از دنیا بره،اینو نزدیکان پزشکیان تایید کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/140430" target="_blank">📅 19:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140429">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
دادگاه تجدیدنظر آمریکا دستور توقف ساخت‌وساز سالن رقص کاخ سفید را صادر کرد و اعلام کرد ترامپ برای ادامه و تکمیل این پروژه باید از کنگره مجوز بگیرد.
🔴
به این ترتیب، پروژه‌ای که قرار بود با تصمیم کاخ سفید پیش برود، حالا به چراغ سبز قانون‌گذاران وابسته شده است.
👈
حتی ساخت یک سالن در کاخ سفید هم از سد تفکیک قوا عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/140429" target="_blank">📅 19:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140428">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
به گزارش بلومبرگ، دونالد ترامپ اعلام کرد اگر صلاحیت «تاد بلانش» برای تصدی سمت دادستان کل آمریکا در سنای این کشور تأیید نشود، او را همچنان به‌عنوان دادستان کل موقت حفظ خواهد کرد.
🔴
این اظهارات در حالی مطرح شده که روند بررسی صلاحیت بلانش در سنا با چالش‌هایی روبه‌رو است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/140428" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140427">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1129161947.mp4?token=mHyhncj5nn0RseK6Oz9LUNdca5EYJ2QQDiZEa2T5FDccqQh7E4VkUeQpBLuPeiB9zzCAgZlyK_083EfwfH1LRdg8wSTEo7e36mL-td39qsSZEap9gAan_WfN8y2TLnHq8l8CeiJZ-hqG-hE93KqClwifgCF_iZjjyixcIdCHtzfJpOYeclmtkYbSRn2yPGLzLGge25r-LHZwW28iio4Be1rH2-wKMlJ5HgM6QpS3-o2Dlpk7MTNsAbVRDTQRxnU6FoaqLB70N3BGrtnootuMW6W3FXYVXRF_7MWd3Ci-1eYBWGoIjrPja1KiqmBXAFNEscaTcO6k_oVOv-Dwi-IzEiLVY-TygwzZcOX2KiNz2z7pt27Jtuz-69FUEnke3TRWogCHpOHcVT8SlJYRmgAgpJA_y6wo9q10Xww2z_EXawdWjt_s9pBd-VBgeUHNPh45FOyV6ayD7tg79Sp5uvlyeldjTKEqzlYM9Egdf8Fo0O91GNVxffaQ-4kxh-qNf5X2OWKi_rRVEmJJVCBmkfrxwtaNsRXtIW_2bTflr-H6vnzcJVHVzL3dzbVXRQ5qSZSLhWVMvm2y5K1lZTkGJYD8j3sSV15Tjj0YTTPSUpORE7LlzxKWmDSg-x_VXIrJzpBm_mF0o2hLd70jy2FqvF_qJ0GmmFcGedNgxKc8EDsMQ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1129161947.mp4?token=mHyhncj5nn0RseK6Oz9LUNdca5EYJ2QQDiZEa2T5FDccqQh7E4VkUeQpBLuPeiB9zzCAgZlyK_083EfwfH1LRdg8wSTEo7e36mL-td39qsSZEap9gAan_WfN8y2TLnHq8l8CeiJZ-hqG-hE93KqClwifgCF_iZjjyixcIdCHtzfJpOYeclmtkYbSRn2yPGLzLGge25r-LHZwW28iio4Be1rH2-wKMlJ5HgM6QpS3-o2Dlpk7MTNsAbVRDTQRxnU6FoaqLB70N3BGrtnootuMW6W3FXYVXRF_7MWd3Ci-1eYBWGoIjrPja1KiqmBXAFNEscaTcO6k_oVOv-Dwi-IzEiLVY-TygwzZcOX2KiNz2z7pt27Jtuz-69FUEnke3TRWogCHpOHcVT8SlJYRmgAgpJA_y6wo9q10Xww2z_EXawdWjt_s9pBd-VBgeUHNPh45FOyV6ayD7tg79Sp5uvlyeldjTKEqzlYM9Egdf8Fo0O91GNVxffaQ-4kxh-qNf5X2OWKi_rRVEmJJVCBmkfrxwtaNsRXtIW_2bTflr-H6vnzcJVHVzL3dzbVXRQ5qSZSLhWVMvm2y5K1lZTkGJYD8j3sSV15Tjj0YTTPSUpORE7LlzxKWmDSg-x_VXIrJzpBm_mF0o2hLd70jy2FqvF_qJ0GmmFcGedNgxKc8EDsMQ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رویترز: بیش از ۱۳۰۰ مهاجر زیر سن قانونی در سئوتای اسپانیا بلاتکلیف هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/140427" target="_blank">📅 18:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140426">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
انفجار در سواحل یمن؛ احتمال هدف قرار گرفتن یک کشتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140426" target="_blank">📅 18:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140425">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ: بهای نفت تنها در صورتی افزایش می‌یابد که ناچار شویم ضربه تازه‌ای به ایران وارد کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/140425" target="_blank">📅 18:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140424">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
حوثی‌ها: توافق دفاعی عربستان، ترکیه و پاکستان معادله را تغییر نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/140424" target="_blank">📅 18:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140423">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
امارات اعلام کرده که تنها در این هفته، سه کشتی متعلق به این کشور هنگام عبور از تنگه هرمز مورد حمله قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/140423" target="_blank">📅 18:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140422">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات ارشد دولتی امریکا: پس از تماس ترامپ با معاون وزیر دفاع در مورد میزان مهمات، مقامات ارشد دفاعی برای یک جلسه لحظه‌آخری در آن شب فراخوانده شدند
🔴
این جلسه برگزار شد تا راه‌هایی برای افزایش سریع تولید مهمات حیاتی راه‌اندازی شود
🔴
معاون هگست سعی کرده با ارائه مشوق‌هایی سرعت تولیدتسلیحات را افزایش دهد
🔴
هگست و کین به‌طور خصوصی با قانونگذاران دیدار کرده‌اند تا حمایت آنها را برای درخواست هزینه‌های خود جلب کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/140422" target="_blank">📅 18:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140421">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
بر اساس داده‌های بانک سرمایه‌گذاری آمریکا، ذخیرۀ‌ استراتژیک نفت ایالات متحده به کمترین میزان از سال ۱۹۸۳ رسیده است.
🔴
این ذخیره هم‌اکنون تنها معادل ۴۳ روز مصرف نفت خام این کشور است و اگر نفت جدیدی به آمریکا نرسد این کشور با کمبود نفت مواجه خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/140421" target="_blank">📅 18:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140420">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نیویورک تایمز: بازرسان سازمان ملل ارزیابی کرده اند که ذخیره اورانیوم ایران برای ساخت ۱۰ بمب هسته‌ای کافیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/140420" target="_blank">📅 18:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140419">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد دستیابی به یک توافق، شامل آتش‌بس ۳۰ تا ۶۰ روزه، خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/140419" target="_blank">📅 18:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140418">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCEYmvp00AIGCQdIXTfzyYJz6GWmwhQ272--zJnbJbEDApvSk5wvRJV6fdThVVMQvr6lku0NFBBxvSA9O7EYhZzJlMwuc-I7iTWUjv2VCRBepBL3pDmIoIcmW-ZA29QXFErAp6O2YZlWZ2yLAsgEulaIP3OEJYANM8Th2mzNDY6zkx8EreqUHBAIg8a-uZXq7T0wt9tkG9YV5KWEW7AeJHkn_5AmROE6xGpHlPvwYzYeJDiyphQIGzu00mCeWSRPUuJRmEpkpziPeqq-eaqz-FLI0-SclJ3sPT-7X0w091_r8DgBMctMEPJa0qk7UNkkSKXd2OmdAk5pswVsDQfE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربی اعلام کردند، سرلشکر عبدالله العنزي، مسئول واحد پهپاد های سعودی در حملات نیروهای مسلح یمن کشته شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/140418" target="_blank">📅 18:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140417">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
متن توافق مکه منتشر شد
🔴
۱. توافق مکه یک همکاری متمرکز بر دفاع است که هیچ کشور خاصی را هدف قرار نمی‌دهد و هدف آن تقویت تعهدات برای حفظ صلح، ثبات و رفاه منطقه‌ای و جهانی بر اساس تقسیم بار مسئولیت و درک مشترک از امنیت است.
🔴
۲. هدف این توافق‌نامه تقویت بازدارندگی جمعی در برابر هرگونه اقدام تجاوزکارانه است و تصریح می‌کند که هرگونه حمله مسلحانه علیه هر یک از سه کشور، حمله‌ ای علیه همه آنها تلقی خواهد شد.
🔴
۳. توافق مکه نتیجه ملموس تلاش‌های دیپلماتیک بلندمدت است که مطابق با اصل مالکیت منطقه‌ای برای ایجاد زمینه مشترک برای مبارزه با تهدیدات امنیتی فزاینده منطقه‌ای و بین‌المللی انجام شده است.
🔴
۴.توافق مکه که به معنای قطع هرگونه اتحاد یا توافقی نیست، با تکمیل روابط اتحاد موجود، امنیت منطقه‌ای را تقویت می‌کند و زمینه‌ای برای همکاری با مشارکت سایر کشورهای منطقه ایجاد می‌کند.
🔴
۵. عضویت ترکیه در ناتو و مشارکت‌های منطقه‌ای جایگزین یکدیگر نیستند، بلکه ساختارهای مکملی هستند که امکان تقسیم بار امنیتی را فراهم می‌کنند.
🔴
۶. این توافق یک جبهه نظامی تهاجمی، تلاش برای مهار یا طرحی برای حمله نیست؛ بلکه گامی است که به هدف ایجاد منطقه‌ای عاری از ترور با هدف تضمین ثبات منطقه‌ای کمک خواهد کرد.
🔴
۷. توافق مکه هیچ کشوری را هدف قرار نمی‌دهد و کانال‌های موجود گفتگو را نمی‌بندد.
🔴
۸. این توافق‌نامه صرفاً ماهیت دفاعی دارد، نه تنها با تعهد سه کشور امضاکننده به حمایت از دفاع یکدیگر، بلکه با تعهد آنها به افزایش همکاری و قابلیت همکاری در صنعت دفاعی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/140417" target="_blank">📅 17:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140416">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
اردوغان، رئیس جمهور ترکیه: توافق‌نامه مکه برای دفاع مشترک «گامی تاریخی» است. توافق مکه علیه هیچ کشور مشخصی نیست. این توافق‌نامه با هدف تقویت امنیت مشترک و بازدارندگی جمعی سه‌کشور امضا‌کننده است و در صیانت از صلح و ثبات در منطقه نقش خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/140416" target="_blank">📅 17:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140415">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
آسوشیتدپرس: فشار ناشی از جنگ علیه ایران، بازار کار آمریکا را بهم ریخته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140415" target="_blank">📅 17:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140414">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEBGzyf3G2f129fftmJbkz01XMSKe0emk3pzwRr10WG6xW_hMAqkLM0tFM7pJ28sB7yysYmUcstVw9PiEd56MEetvuP10Nq_wIVkmiN4GKxZjzbBgicyPxTjJ0qYo5ppthF8EpPIPcGsUsijuZTRTvjYvoCzUeIpxyD3EsxiV-2MBXHIkQ86rCJmh-BuHN5htGzzYUZbW6y7kp-bzuP755BJjloJTBsYf0eWWSF-dUlLZw8y3kN5ZZ77SL_AqMOw20M30Z22G8ejcPlxaDr4qtAdLvnBMY9EKYgIa6tmO9fba3oCvbXP0wbHs9gLxFcr_Z5gMQJWs7yFK5424PanSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بار دیگر مقاله‌ای با عنوان «دونالد ترامپ، جنگ با ایران را برد» را منتشر کرد و آن را «مقاله ای که باید خوانده شود» نامید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/140414" target="_blank">📅 17:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140413">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
موضع وزارت بهداشت درباره ظرفیت پزشکی کنکور ۱۴۰۵: خواستار اصلاح ظرفیت‌ها هستیم، اما هنوز پاسخ مشخصی نگرفته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140413" target="_blank">📅 17:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140412">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نشریه FT : یکی از دلایل اصلی عربستان برای رفتن به سمت این ائتلاف، حملات حوثی‌هاست
🔴
ریاض نگران حملات حوثی‌ها به کشتی‌ها تو دریای سرخ و تهدید مسیرهای مهم کشتیرانیه
🔴
به همین خاطر عربستان می‌خواد با ترکیه و پاکستان همکاری نظامی و اطلاعاتی نزدیک‌تری داشته باشه تا جلوی گسترش تهدید حوثی‌ها رو بگیره
🔴
این سه کشور قصد دارن اطلاعات امنیتی رو با هم به اشتراک بذارند
🔴
رزمایش‌های مشترک برگزار کنن و برای حفاظت از دریای سرخ و باب‌المندب هماهنگی بیشتری داشته باشند
🔴
چون عربستان معتقده حملات حوثی‌ها می‌تونه امنیت منطقه و صادرات نفت رو به خطر بنداز
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/140412" target="_blank">📅 17:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140410">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نشریه FT:  به‌نظر می‌رسه محاصره دریایی آمریکا صادرات نفت خام ایران رو عملاً متوقف کرده
🔴
حدود یک هفته‌ست هیچ نفتکشی از جزیره خارگ، بارگیری نکرده
🔴
طولانی‌ترین وقفه از زمان شروع جنگ
🔴
داده‌های ماهواره‌ای و کشتیرانی هم نشون می‌ده اسکله‌های بارگیری خالیه و رفت‌وآمد نفتکش‌ها تقریباً متوقف شده
🔴
ایران فعلاً از فروش محموله‌هایی که قبل از محاصره صادر شده بود درآمد داره، اما اون محموله‌ها هم رو به اتمامه
🔴
ایران به‌جای پر کردن مخازن، تولید نفتش رو کاهش داده تا ظرفیت ذخیره‌سازی پر نشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/140410" target="_blank">📅 17:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140409">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0343b54724.mp4?token=npWb9W4nZYO981O9eX93cCdRj0RtqdK7pHNLDIKaNkysvMpVUrYCYlcSID6PdUgQ8CFuQgV4tK4yMaDv0-qe367jX6e3TLvNCPlLSfJKzP4CaSZYYXroqZKcL9h7AWMDIpz3GskJPzVAu-Qfi15_uLd7oHHq4gzoBNQKVy52y_iuqIaxxHNwUt-yxMjmMMAFa1Vb2eGcKoYwv95qnytVYHIV-eTImGaWVvCuU0BJVxU-j-SdAmxi7_aHeBAEkF0-_HqqSjTphZ6LW5JgsGvhI-rFstiMCH0Go3lsDrvlLkACFhsqLbGj0GCy52mAQ5FWijSJAZtVvVNOM5CowP4lDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0343b54724.mp4?token=npWb9W4nZYO981O9eX93cCdRj0RtqdK7pHNLDIKaNkysvMpVUrYCYlcSID6PdUgQ8CFuQgV4tK4yMaDv0-qe367jX6e3TLvNCPlLSfJKzP4CaSZYYXroqZKcL9h7AWMDIpz3GskJPzVAu-Qfi15_uLd7oHHq4gzoBNQKVy52y_iuqIaxxHNwUt-yxMjmMMAFa1Vb2eGcKoYwv95qnytVYHIV-eTImGaWVvCuU0BJVxU-j-SdAmxi7_aHeBAEkF0-_HqqSjTphZ6LW5JgsGvhI-rFstiMCH0Go3lsDrvlLkACFhsqLbGj0GCy52mAQ5FWijSJAZtVvVNOM5CowP4lDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گفتگوی بن سلمان، اردوغان و شهباز شریف پس از امضای توافق سه جانبه مشترک
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/140409" target="_blank">📅 17:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140408">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT_HsEA2yHJmt6sBMtc75ika5GkBIc8am9Nw2XjthkZegp3ZCaa2e7D-zo5--XP6-Ic3uqOts38611KViKNy2y-_6bO5z7ibAMCdyssvstuMcYmEw3mXN9vIXojoK6070VApk2y8SB6bYeQLJs_vMwvwhvOPdnUWJLQr4jGyOX3O4w-csiKbkueLhT6fMYK-31Yw_FyDWH-96T6Jkmx7V5HIs8KvLp272iSKveHokw9o6SD9yMxQ55hVk0B2xmv_H0MWBs_Hed2seNO-DaoxvKxn_uSq6-PCio7FKG3c3WDXojYrcHAIfYrH-87-H36EnaCv1b3lXUBA55SUi8l_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیت هگسث، وزیر جنگ آمریکا دقایقی پیش در حساب رسمی خود در ایکس متنی را منتشر کرد که عنوان آن “ترامپ جنگ ایران را برد” می باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/140408" target="_blank">📅 16:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140405">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266f0707c9.mp4?token=DdvTpuyI4OGHVKKrKmhJ1PwsAlJADAlycrKHhxNRPIQaVhvUar3AklkIFw-49kz_RlDrtIYvzgdEEEBWZlQcghpI7JFL4HfuWPk-4V4myN0sGC9lMEqh44aPwEKFssrYpqNVnTq-BFRki2gIuvsimN_erhsBE_JVVkZ2DPmN_Ep-BfgKGVmZjdf8UhADS-M0yhzpEXeX8Z5P3iJZqaDZRT94HqQwd-cVzAggN3YVpgluXqGz_A-SWs4OE6qS5Yo1e61ucH1FbmNiiv2BVrqcn4_SpjMD3ddlSwjMB7L1gKM8oOjGPZwHP5LEJuuo21NoE1bevDQ1-P9yAI_hdaxccg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266f0707c9.mp4?token=DdvTpuyI4OGHVKKrKmhJ1PwsAlJADAlycrKHhxNRPIQaVhvUar3AklkIFw-49kz_RlDrtIYvzgdEEEBWZlQcghpI7JFL4HfuWPk-4V4myN0sGC9lMEqh44aPwEKFssrYpqNVnTq-BFRki2gIuvsimN_erhsBE_JVVkZ2DPmN_Ep-BfgKGVmZjdf8UhADS-M0yhzpEXeX8Z5P3iJZqaDZRT94HqQwd-cVzAggN3YVpgluXqGz_A-SWs4OE6qS5Yo1e61ucH1FbmNiiv2BVrqcn4_SpjMD3ddlSwjMB7L1gKM8oOjGPZwHP5LEJuuo21NoE1bevDQ1-P9yAI_hdaxccg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت جنگ ایالات متحده، پنجمین مجموعه از اسناد مربوط به یوفو ها را منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/140405" target="_blank">📅 16:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140404">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
دولت اسپانیا ایتالیا را تهدید کرد که در صورت برنداشتن محدودیت های مرزی برای اسپانیایی ها تا یکشنبه، اسپانیا هم علیه ایتالیایی ها محدودیت مرزی وضع می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/140404" target="_blank">📅 16:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140403">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
بلومبرگ: نفتکش‌های حامل نفت عربستان برای جلوگیری از هدف قرار گرفتن، مقصد واقعی خود در دریای سرخ را پنهان کرده و بنادر مصر را به‌عنوان مقصد اعلام می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/140403" target="_blank">📅 16:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140402">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va_W2RJUm-28PW73LPqoTha_jWcQLMcrIguF5DtXPpPmXo7GJYsodspKs23-CunSuiIknzNPnlvsiJA-Fm83-HKxU1B_WQnP1bRI0DR8D1nOjLMnI9Ot2209Ia8fXch57_yYOgsOwDceCugj0IKO7mdpMT6VcuQ-JAWOqDRM6le2KlagIpfvvybn8bHFCHc1vCrysUSb6jGqpx3AUVnwTVM_VZskTsKt20utBogzkf3g6FIayMvOr76e2kgVPCEhxYFOh-NEG3GyOjmby4uX298A672IBEbUGyVTgcz-MOj8BLVjl-VFBF9aoO3wAl2agcnhcuj29evTxTcLgBbjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از انتشار آمار جدید اقتصادی آمریکا قیمت جهانی اونس طلا ۶۰ دلار افزایش یافت
🔴
همزمان شاخص دلار تضعیف شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/140402" target="_blank">📅 16:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140401">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMNy_7D9DKPKzrQaHAy46py_KaL-PRbndNhAIk3M-nvrYk4NayeqavPmWH19X3EE0ZgdTJWT8ay4w-L8aFzMc3BXxWuXZ0nLAz0vB22V_nA9InXeYQbi_UZkWGQL8eOT1V8e0lFI8P3EsiAsvJ1gRtjlkBCcskNjGVoXK4XQhwjRBxrXlaOtrlWtbjrY2eWtTLzTh6ChqpDAfQRZtqmZvvTpD2dkecmMPvTlVJXZU9t262fBO5FBu6i9gxr-0vr8TOMI57d0vvppOM9udVyKzr4CgMYyPCqRa9s9sygGFR-5-UGqeJFY4Lqx9LsKlNHcb0qqmq_KEgIORHMiZjnAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: افرادی که می‌گویند جنگ را تمام کنید، منافق هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/140401" target="_blank">📅 16:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140400">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdYVgc4thnTEhxVIWMI5DNRIRgwYeBDeF6HxPVbijgVrDUlSqhh30LE9a5EmhMZCDog98n-CWv0_tN0j4evl75KOp_UMhNXAr3ocFduNOVdQl6t9MxLCVShn9r8L3yr__441-r8MOBKI8d7AS6hjjx6cOrgYjYrdXScGUvA4uYc1dFXTppy7bjH-y3TXeK5pwzNDQP3TictKkLUZ-OwPSno-WD5xk_DDkLloS9PXUYD9ZuGOPIOvBEEmzXLpMXJnxbXDNTzEfH3OEmM6bwciKSDcaVSgpbk8aqabnfws5zu1YytvWbmWhI4nJv5V8pl2oNRRphg7DSLZY5RVn6t3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی، عضو کمیسیون امنیت ملی  در ایکس:
🔴
عربستان باید درک کند که یک توافق کاغذی با ترکیه و پاکستان امنیت را برای آن‌ها به ارمغان نخواهد آورد، درست همان‌طور که سال‌ها بهره‌کشی یک‌جانبه آمریکا امنیت را برای آن‌ها به ارمغان نیاورد. وضعیت را اصلاح کنید تا مجبور به التماس برای دریافت حمایت از دیگران نشوید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/140400" target="_blank">📅 16:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140399">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
قشقاوی، سخنگوی کمیسیون امنیت مجلس: چارچوب کلی تفاهم جمهوری اسلامی با عمان درباره تنگه هرمز مورد توافق قرار گرفته.بعد از اعلام نظر نهایی در سطوح بالاتر، بیانیه مشترک و جزئیات این تفاهم منتشر می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/140399" target="_blank">📅 16:04 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
