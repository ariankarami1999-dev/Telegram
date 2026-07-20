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
<img src="https://cdn4.telesco.pe/file/VodC7mPs4FrQXNI7816SdJh8oz1GJxa1vr6Qo63Hy4sSZ0Drh5plf5xmY9lEj6aY4UCtQLNcQzbxB99TAXB2qf2Wa1ra4Ka5NdmZi5S6dAwKE6OjMOiWkJgtyi7UHglsutJ2uc3YQZRLQbM4yD6hI63HLxwO1Afrrm5VVrhxh0LqRU9O7NY4_v03619P7ozwcAzfz01Az9MuhN_dZ5Q3BLgOEgxCoPYwdBY9XP4zztZDBLTL5dLe7NaGjg4H6t5sZSKnkQ6BsSYVUgOSv0hUZoPwVKE_6JlW7nICtdbQh-Eg6NocZEycvj09DYEJl0MYoHN-p_qHIro2Rf1FQ1hAnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 520K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 04:30:39</div>
<hr>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=U0gT-FYfVP-g7HvgE6h0x71uBanInd8pxhRc0USPSGM01U7-cbGPf_sWykPJEHHVExhvXuUuKWyuOoclzF_BrXCwwFgx_GXNREFw54KdFIOtSBLSUuzHDvemZFJJSwVdHwvAv9o87DHz68aeYmFQfFxAhvJJ-oTNh7Zp-NGb6LCnfpr1BDRLDLMy34NF-q7k1Zq0lSbSeUw-N7Q94jT32zBPEPguAVf1_Xk2L4uTV0Qrxkgpy5nySFEf8U41DYu_5SnvgnIPp_tLmaQnn7fWvBbbM7i32XU0Edf9grz0aBKVvBV_aCOKSLywQkwXanEV4GnOF5WqM9UUfdFO2QhPWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=U0gT-FYfVP-g7HvgE6h0x71uBanInd8pxhRc0USPSGM01U7-cbGPf_sWykPJEHHVExhvXuUuKWyuOoclzF_BrXCwwFgx_GXNREFw54KdFIOtSBLSUuzHDvemZFJJSwVdHwvAv9o87DHz68aeYmFQfFxAhvJJ-oTNh7Zp-NGb6LCnfpr1BDRLDLMy34NF-q7k1Zq0lSbSeUw-N7Q94jT32zBPEPguAVf1_Xk2L4uTV0Qrxkgpy5nySFEf8U41DYu_5SnvgnIPp_tLmaQnn7fWvBbbM7i32XU0Edf9grz0aBKVvBV_aCOKSLywQkwXanEV4GnOF5WqM9UUfdFO2QhPWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=MA8WmKcC1iba_rYFI2ZHwTiiSHspXibMSpJJnn0-m3woBx4pMyvW0jzYZRz-G2-su0F6s8gd3HfWUEH1IzWMWTVg44U0f5I9TrETsurBsvU70UzYHlCY5QTnKmm922svqD4qmaGO_fLvodtKAZSZpD6NIh8vttrqAJ5xn56lqk_83cYHyDx0B4N0vtiY83jiNulGVzKpXdH4sFrRN2H8Nrku-gz3xXYJw6PoVtkftqTXo0bjVJrZgV3ce4AuUoOwfyDyLylHut8NJQ-WDBWlzwH2Sev505NGo2JxPZKeSavAzKzT6KXLaK0GDxWKfjFhWegFj9kT4TppconbECCoFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=MA8WmKcC1iba_rYFI2ZHwTiiSHspXibMSpJJnn0-m3woBx4pMyvW0jzYZRz-G2-su0F6s8gd3HfWUEH1IzWMWTVg44U0f5I9TrETsurBsvU70UzYHlCY5QTnKmm922svqD4qmaGO_fLvodtKAZSZpD6NIh8vttrqAJ5xn56lqk_83cYHyDx0B4N0vtiY83jiNulGVzKpXdH4sFrRN2H8Nrku-gz3xXYJw6PoVtkftqTXo0bjVJrZgV3ce4AuUoOwfyDyLylHut8NJQ-WDBWlzwH2Sev505NGo2JxPZKeSavAzKzT6KXLaK0GDxWKfjFhWegFj9kT4TppconbECCoFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=BtEM1AvtgX8wwaRje-tFdXEEg2OlhxgkEYweG7en48h8gUYbHLtydvEoD_cfxzp4G3zkg1fhjzdbDgZAzEMlWpF1bnko59IKKAZCv0ZXtsppV7-8mZJqcWd-Oz8x8Ycqd78XJX6RNv2ITuch0PXHy6Ns41hMXrYcCbbglqMqNgQwx5Txlwfj8UlOYeYEAVI_7sldUriOXgkA0ZB1iGC-AbEjj5N3sEvQUeEPUR-msZcKJSRynWMhlOMr5nHZck1Zl1faWullMr5wPExCIQ3L_mZRml5-b4fN_eXVxuj-prLvaYlOWClJXbEnKlL9AWP9KWUyQbANOIewMWS5eNQGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=BtEM1AvtgX8wwaRje-tFdXEEg2OlhxgkEYweG7en48h8gUYbHLtydvEoD_cfxzp4G3zkg1fhjzdbDgZAzEMlWpF1bnko59IKKAZCv0ZXtsppV7-8mZJqcWd-Oz8x8Ycqd78XJX6RNv2ITuch0PXHy6Ns41hMXrYcCbbglqMqNgQwx5Txlwfj8UlOYeYEAVI_7sldUriOXgkA0ZB1iGC-AbEjj5N3sEvQUeEPUR-msZcKJSRynWMhlOMr5nHZck1Zl1faWullMr5wPExCIQ3L_mZRml5-b4fN_eXVxuj-prLvaYlOWClJXbEnKlL9AWP9KWUyQbANOIewMWS5eNQGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26117">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=iUgniqkKsoqAs9DZ0JUgHCPTdDeDr3uJhiBaFd1BlIOKsXKLh9UoTl5xZMD-APD6Qzr-H5Y4YSNcPN_1zEuOjO7XCiGXLimPqlbukMPrkWCnO2x66eYgA1nTZFTKaci_lMPGoNyrQd-3hlmtNQxYUtqozFP7jjhK-nyPFVXno4OqSoImILJHMixg3jJ32KRlZUtOv_FCBP335AU95CdtQsB4zHOay-oRaxOTMMn8vEbezv6WfpU3-jui66LJAoBcAUZNm3Mt3b5VBH_T7O5CSymmrZDJd7H74vwWkG_W1qe44njkY6CSQ288LbXexd2s1Gv5ZrqYzhzBP9sSXzIKLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=iUgniqkKsoqAs9DZ0JUgHCPTdDeDr3uJhiBaFd1BlIOKsXKLh9UoTl5xZMD-APD6Qzr-H5Y4YSNcPN_1zEuOjO7XCiGXLimPqlbukMPrkWCnO2x66eYgA1nTZFTKaci_lMPGoNyrQd-3hlmtNQxYUtqozFP7jjhK-nyPFVXno4OqSoImILJHMixg3jJ32KRlZUtOv_FCBP335AU95CdtQsB4zHOay-oRaxOTMMn8vEbezv6WfpU3-jui66LJAoBcAUZNm3Mt3b5VBH_T7O5CSymmrZDJd7H74vwWkG_W1qe44njkY6CSQ288LbXexd2s1Gv5ZrqYzhzBP9sSXzIKLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/26117" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26116">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=Ye2-H6nvxnxTC0D5ralhSTYowkO3X9NVtfxL7qSTC3UGSfzAOcxahylEguuYiM4cLNkX-SF9aBpxMatJg8PforC4dVUJueZ0uIY0s3Vglocxk0MERyjdF_tCSMQDJki9Q_NhE8i4MD8Wy3a9GFlQ5b1lBNjuHdbyskJH9sglbi85fBTzjeHhtOsL4X93WedPRGpm13USUIEXaPwra_i_Yhe5bE_md31_GohMFx2S2GXocyJm-NalQmWKvUmQQSb3-Fr3OPbPFoSAV8TAzYutij1F0ZFZuMZ06Fk_tmLjwkKKnDWxmUjdzJ0txFCGzI22nQlp5oDtelvQHdkkr-UKFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=Ye2-H6nvxnxTC0D5ralhSTYowkO3X9NVtfxL7qSTC3UGSfzAOcxahylEguuYiM4cLNkX-SF9aBpxMatJg8PforC4dVUJueZ0uIY0s3Vglocxk0MERyjdF_tCSMQDJki9Q_NhE8i4MD8Wy3a9GFlQ5b1lBNjuHdbyskJH9sglbi85fBTzjeHhtOsL4X93WedPRGpm13USUIEXaPwra_i_Yhe5bE_md31_GohMFx2S2GXocyJm-NalQmWKvUmQQSb3-Fr3OPbPFoSAV8TAzYutij1F0ZFZuMZ06Fk_tmLjwkKKnDWxmUjdzJ0txFCGzI22nQlp5oDtelvQHdkkr-UKFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:
اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/persiana_Soccer/26116" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26114">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI9LFeqmAO-K0sPt0_EArkNZffobjr2m4qg3gfYkTCwjC09lqgPVhpuYuXiELwFIOUKE-vlQ1DqilzGB3shvTkSMy2vkSHbGCCyycCSoHTqpoLn5tRQkrvkHrcEC1pGWHc_s7wS164CQicC0bAr8nZv72PNm7NSvAEJ27hrp0wOCoMs1LiTCYBqUleSZbzbE5wnbEfRpXUKmtaPgzveVZTBvitC2AobRH3WFOfWnsFJhoih3o_N97IV35jgydIp4B2EXbQUfIf79itcpKKGZ66wbGI_UbIacCzDCcdDhWygctVh8B2mOMfq09cVBIHcBQjZjCsAb-zgrplX1wu_sRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/26114" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26113">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4tRFLishIuQCSb36yaFcM5i-aQgWKs1ChbZVlv5n8f17x3W9vxfo3J6631WiG_b8UXTDtRb57fye2A_qPJ9OqmFUgOYn95Oaapr2VZ-e37jUid1Zfiu97iFrQeQp9B9wd0nIG1n81R4H6fDnOHT5HHKbJpAqAaLhHe6VMwfjfg7hGCOBmXBl4u8D0eEkDKb6zOG9PWBHO6rtTGSOZPAgId5I4Eg9WL9m0bz0pI5iCIU5bXHn9TAlvpXU_WByhCwtA1eHUf2uQWZWwK8KUYsFls21ZNDlwfF9LgNRMN0hFJ1wM9HkkWz5nkyAMFU9LgRY1RXq-kXJ51xOTTgZFes3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/26113" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26112">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWH3_iVTgsbfizoB6iYvplR1P1X6guFSGqIpyxm2jnctb1ZbkeHTWhxJ0bVY7DeJKsSEWkirJSigSb1XX-tHVT4sn02DU3pUOftW0ngM5Iixa1UiMv_zl0g30IyciZUoLNvKi70h-m0-7Nsxr_scyAjyjEtCjkLySUvUBVUjFgtLFlJErCYbgzdpd-sCy7KOc3_ipYmqDNgZrIFOurAAzxDYqvJjE3uHv_gTqN1ecYmH5IxzzqzE-ZwFa_tNRHmgV4-SqqzrOueCp2PI3RtWiCsOkJVKiQwQiQqCf5nRvU1KutHx3FAMZenvgpo5dLm5USGSCLQ9k9uHUYRPKHCLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/26112" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26111">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUBnvGjDUZy0SRLj4tTdG3iCXN7EkFGsoL31S-uuZFrNmd8GkZG1NKkfl0lq3gFUsaYH40WeZJQ1t-KKmrSvqQAxo3BJJgRAP5yTKwwX5BWPBHjFYtBMwZmhm-Ha3guTGge1a_1WIKNqkTZLBbGTvUXnsUnvr9bJc0Xkr93bdx4GSYQD82aaM6MFhizaTtdBQUHHGox0VrVUAb6a19v3OME-XhoSI0w2AnLgz2kIqSuvyTat6_0Uzc7ea2In9K3rE3nS3Uqwd41Wmj0eBr3FMw_P2F3QiAWtuEy63j40YKTmj6bNXPxAwWrlHr9ipEq-ltQJEqtTg8XDWinY0J2d9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با عدم گلزنی لیونل مسی در فینال؛ کیلیان امباپه با 10 گل‌زده آقای گل‌ جام‌جهانی 2026 شد. همچنین امباپه با 22 گل‌زده‌لقب‌بهترین گلزن‌تاریخ رقابت های جام جهانی رو دوره بعدی مسابقات از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/26111" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26110">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c41lE0S-130wzwnO0G_R8j0vPBrcmBh4wzQScf8K0ypfJ_KU-AeKbxlcgF9xn-SdlOvh4icDMZEkoy-NEB5NgR4lUdBJjSgzubtqWRncRoQpuoI_KcTGjQZOGmt5iSxqCvOnaCNzMRNVc9TUGM_-bEGj33C-ina5KgvbbzjaKR1alFzrzhxYybEh4aii0jTzfFifyb09mMeDq079K5tdO0FMFo0BRJFnCHZwdDs3Iv9DIk2_SwOtzvQHN-nmCTA4tzx141KVVI3V2ZuBx6ALORytYTUQTXeluc6zEQ7Cl-yWgtvxFNxOvQEXx8LGNgQa-WJR9p-8lRZ30lvDYnc-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
پایان جام‌جهانی 2026 باقهرمانی اسپانیایی‌ها و گل نجات‌بخش فران تورس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/26110" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26109">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im6AqAbk57LE4YnyOsrA0rhUSKS6Q68yW8OQOCGC8Sa6hNu61Rm7GLeVq3-6fflcBYpABQ9ifTeSPwUmunEUGLj5Y1QOE01mZkGjUy24R4eAT0kNTwmymoT6x6quv1U0eM_futSdjWqW6n12-ysoZMBHj4412SWH5DtuQjit1ocFSUbuQY-2m5WPnijfZvV-1I5CdlLcOww79eFUM9fb3DG8xozfqykmrJm5Ox5mD8QPBJ7bLqwSQyfwW4dpdLsK2DWFp1jtnoX3ZcWjoo7bLN__dEWZDMrMY5ZF8GMdSRY6QWFVVFXwmzlRWyF5otMd1ufhJ3niAL8WQqibA08HqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرژانتین وقتی فینال رو به‌اسپانیایی‌ها باخت که دریک رپر کانادایی روبرد آرژانتین شرط بسته بود. او در این جام جهانی روی هم 10 میلیون دلار باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/26109" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26108">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_ZEe2x3-X1xiNBsEfUd7UkxOKqBTVlNDjog5uvLGki2vlGfPp9ZhzPWY-wAcBG-NTevFpCRUMVi3o72K9JoE2WEj4tp4CpE6zlufV7P26FEzMQURMeqYimmjWmv3zF2k8H8nSieqGtFNYSSXy9IMs8c07cqLTCdar0CL9qWNlj9su7VWIw6Oywj0AzPXl6maNKqM7igqvnawSTsQ9Q6po_JRvnwRS6Qw_xHKWC-gMvypeRKFJ1x9mf1dgb30VVOXXugwPxzhX32cmUImg18ZLHSH7PYs1HFJQ9PPN440sOuMUN57s1X8oKRWGGMBSat7L5kQaMYtqXjTP_06lqPLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید بلینگهام هم اومد:) فینال هم یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/26108" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrhJ5-y2OvPAdtWM8s16q3qPm2_291WqGmebs82no7WaHBXyPNt9qIgXVuvQq9p0XzeEfIYVChIE94Wmzl9t7qaqX3fq8iAQf2GiyVtg8g7ZdhbAAKo1J89p28CowDh7l-4ziNeJLhlZmmoAT-u8I8HU2Ber4-Pev4QnsB6Ar88MvTlIkVSczUepoKI44b1xaIiKV3JGB_aCbqejIAVf0dQCyCGH5KAILqY-x1Vs4W_cHkhTrPYTImQxZ_tSnZRz2a0y63RzKCbALtBaq5VHTpkBtG9dlR6XCSRCFosshIhIZBBu6h-qRr67_-5UTe9oig6kxtamwLzqtmAJ5MSQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrBnz7Pbv3eKw0u7chpHY8yPzmsKvVMbwS2ecA4kFTki2JnNAdddSs_vvpC1Yf6JNmRbFDDpwDJLOF2o_VIXdJh_sXG5uly3iOjFb1OYN9d7KHA3XoPmPl58K930N_-UNHHwU-sJBmQkFFFU8zCQ-SReyusaxC18sqQQC4h5-6gqVvmPaYpueygmlTeBxsvMfPSSVFbvp78PPGTbSQFvesrsxfBSCsFcn89pjjNgZlyrTJNecLUapgaaeIWnwGrfdAFdTxm4CbYEt8H0Vl6oknNuAv_UVKZsweZ7WmHV_udUmaOYBS3zRv0te4NH5OHiiOUSVhZuKlBwyqpng95nWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuHMt4U9y2RKoxbC05HfRrf0_bIBgtL4mEybkSnW7x2jZR5k6NqlUhN9FyH1_qI2K_O_9Dpeey5SDG7Vn4PpdJUdH0Qku41RZFZ47V5nUNRl3Zqk96bzWRXGYU77mSO2rN1ZC9yK2fmpo-hbPaltrepgRy4_2PyDcr-B1Me6xkb59zA6qAkBlJZzk5JINwsAdzRJ1Gg49bc1n2gL2JG4NXH_O5GGFjjqi6OPOsLl0H-RNNW2YBw9xzgCBfleBzftmF4-kiHCpqzyPJ2uVeid7x49wAtom9tlOihEB4Ca7JMiuERahNNPN9LbeXV9YjQ4pwA_QcagPGnYsr7jTl3XFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بعداز 12 سیو بالاخره‌مارتینز تسلیم‌شد؛ گل اول اسپانیا به آرژانتین توسط فران تورس در دقیقه 108
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/26104" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26103">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=c1g49SJsgipNbHKZUJAfIh2AxZVbwhiAZPrppyuZ9qjtJQrWHPIULc6xPoDMooPJJAMPOeHEabL6m-ceEV8H1mDqHdrWzGS0g84RwawHjLJzuuHHF_78ertufH_UAHLxBjsVy97-UpqUPHaDfMGyKX9Q5CjiuCDwvWFgb92r6Pa2wrmMKLWT6RZTDPzB3IpwWAqZRPOBpI20wbsdHzsXjHaXNJ9bLuouMr5tVTJOFXeAHYnLScePNgHKHARpA3e_-j-9tWsxXTt1GgB0YXnXdIPjPRYWMIZSZi9a2JtvjjjoAoOW-HvR5gPLG6GIr2D322-DYl0wnuOfbufPlmovQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=c1g49SJsgipNbHKZUJAfIh2AxZVbwhiAZPrppyuZ9qjtJQrWHPIULc6xPoDMooPJJAMPOeHEabL6m-ceEV8H1mDqHdrWzGS0g84RwawHjLJzuuHHF_78ertufH_UAHLxBjsVy97-UpqUPHaDfMGyKX9Q5CjiuCDwvWFgb92r6Pa2wrmMKLWT6RZTDPzB3IpwWAqZRPOBpI20wbsdHzsXjHaXNJ9bLuouMr5tVTJOFXeAHYnLScePNgHKHARpA3e_-j-9tWsxXTt1GgB0YXnXdIPjPRYWMIZSZi9a2JtvjjjoAoOW-HvR5gPLG6GIr2D322-DYl0wnuOfbufPlmovQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/26103" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlrHjr9DTZ8KlkRuk6JU3-Njfua6UQvDJHZ8a0zP4cbNZkomR6_0F3lkvoz2YGLYuYySoiPyCzhwXtYnpPIXBZkTLhErovFGGMmvkgo_usEnyV3btTrxzFcE6VUxk0N9-7t_YVReqUwXmgeyMBdKdySRvI8SO5l2a36g2IrJ-g5a8ypN78M23kCyVcD2bh1mvgy3rG2y3q3Cy4Z2VyorUOYEoa6mRQGMZArlHi2IxCFeNg6vZj-IW6e8zDkEQbALPCwp-z7G7k-Z_ClL7_IRk31cH-K_RXaLma3nvvwqbR8pk9-TxL_zRVItDU0OxvUrROld1whN-p-CP-fqwcfNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxegBBMuFxmnc4yaHLJgbFi2Az4EuLpZlQLgt3U7yCWtNZpde6sQOMozeVl02VlYuvSSdqDOZne9xwjeEeZaajBj58sMsMJfrBE2fI8LE9i1J22s1KaiTY9sK1z49Eu64ZTyBoT5pIzTwrpnR_8RXRwFGPX8YqPjWRFZf_AeH2FybeJ_LD92ERzG4PgEHbNk0FUxbJ5dZ8LSfMnOjB_AGWF6Vuw1eXDp4cL7_arfvP9d0Y2FChG-O3Is8wU_OPfitXZy3-DayMRM316htlpbPMkWtNdcgETuKBCW2ue8tSvqXYg1dwqVi4NkDlYjT_iE5ya_pEkvoyHGKKBDSS_oQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qaqd0ggb5bnqYE6HEVE5oWfsAtF-C7oD49gTvHt_lmxvDTSmdid39VNH1eUef4JRNqbVZzyAyrPDXDZ-t6oMrP3D3NfKqqN_zMJN7XCl-UhVNGGfyo6m_8vSZKBfDldAcihlxo1YYaAmkdVjw2swrT6og6gcDBIOSgSpGeYKahoD11BoUmPPUt7co3DBqJNxQ570JYLqiSGIFLyW0i3WJhaxGSjMiWOeNwAzgq6PBOs98uGBHLnnAPZH-jPVwGNtPpy-3wJtk0vE7SPkqenw4XtTgAwR0Ximwl4P3o8n4rKQkZZ1-riIs948Sj7PvlHeBZjm-Npnugic2xTQIFdLmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fqp78ikRzeorITIwnCNmkSzAy2tv1mI7lV-FkfTpBwTlN7PEutStUv-eDWF9r_U5DYIWLvYFE8KxH8igtvSQnsvnFhcZjZyFIfvnGkz5Y1jfiXb0920jxsyeio8h_vrUKgVXjeYXlgfvC0pXoVk4MMcIlaAjiXl9LaKrhkpbji6z8qxrTsa1Xr7rmEBW241c7OwFgwhyRM2leIBJT8N4n2DzEQ0i2MOgRWkQMzqhSJ7eupDdNFxBb_J0FH4CyVE-b4_8KDd8T0rjL6681rpbzXsFFc1TPD241fsfzsdQlWsuozakXX1_PAZQwtijY9etYY95ShwulPsix7XBvLNrog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0hKJ33PYq6JW0iHjPCb9qy-Y0BRjF-6Pv9hinZYhX2Gw9G08iqqHBYGNJRsdhvSHsT7yShfxW8aO8GDyQAVc0Ts36ZYqL5pzICeucB1Jllg5CG4-bEebW-tTPes20GF98htj2jgk7biVknz2C3QjrQBfwuTRv-72UYUiG2Oj7NDmhFhGWMiGVSvDZ1tZk9uTH35Y6J8M_ue382e89JmTD9AxIjYH_4s2xBWhUdeSwsBXVias_W59Z0pYJwLv0fEXdyuNIgF00bpCJOPCwf9FqEdaaTNQSxRQWrdZ59Oq3eMRwy6JMSI5Ff1vjxe7Twf1r3VnaSevjmxaUMIfVCxcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26096">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeA0dQRinmbwkE1nH2dhB28ITr_FS9KCfuxjXFtMr4UDJkRIhQobCMnfHcYqW_8N3h754rCZmXtDqALhp6lOLnuckvpzhGQh3OfmEwL12JsnA1Woh5WbLLzE_ekL7wQhixBa4Ks6mQshkdLwEE5wq9OIQYOv2HrLLl9wr9QysqsvAi7PI4wlghIrB6rTw59jloqrTIApw6cJ_1raJZKeijH9g2-1qEFCdNRCLVxPj5YBA7FJDkQjp7HegOazyrRa38RaE2LmTDGuhHAilnfpbhYKkay0bTgXWj6TIhfM6ax4bwq_Wmqc7BUnH0EDJz-BLfh273bE9W-iYXfnJ-BJPbYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeA0dQRinmbwkE1nH2dhB28ITr_FS9KCfuxjXFtMr4UDJkRIhQobCMnfHcYqW_8N3h754rCZmXtDqALhp6lOLnuckvpzhGQh3OfmEwL12JsnA1Woh5WbLLzE_ekL7wQhixBa4Ks6mQshkdLwEE5wq9OIQYOv2HrLLl9wr9QysqsvAi7PI4wlghIrB6rTw59jloqrTIApw6cJ_1raJZKeijH9g2-1qEFCdNRCLVxPj5YBA7FJDkQjp7HegOazyrRa38RaE2LmTDGuhHAilnfpbhYKkay0bTgXWj6TIhfM6ax4bwq_Wmqc7BUnH0EDJz-BLfh273bE9W-iYXfnJ-BJPbYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/26096" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26095">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=TLAbjhs7f9R3CKy_4sAtquvrqH4KxBPo2g4zJqZ0KnFz-NoIjEH6LwwjVzO8loCpbzkjAsjBvnG81UcUIibM1oG7qv9E7dND5ir7r4-Vx2qKRMZkyR_OjftjOAqhJvJK4P9pXutkU42uVPi6i4bHTxgx7WJSfPc3yaoXMd5Ives-rBa7BS2TnuMZfNngNpQSGRXO6B6AzlB89C9xzQ2E7ff3XegVyzvibJ7zk0AiY8s07n1MdgMgvuip-X5auFGdNDLI7LrI0634Q-N7HHmHo6jrWBURWK6HVNWGDQf3NJpQk1J12PAJnhKkTLYOtxfbEmC9FmETzoU7S9gXt-LfuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=TLAbjhs7f9R3CKy_4sAtquvrqH4KxBPo2g4zJqZ0KnFz-NoIjEH6LwwjVzO8loCpbzkjAsjBvnG81UcUIibM1oG7qv9E7dND5ir7r4-Vx2qKRMZkyR_OjftjOAqhJvJK4P9pXutkU42uVPi6i4bHTxgx7WJSfPc3yaoXMd5Ives-rBa7BS2TnuMZfNngNpQSGRXO6B6AzlB89C9xzQ2E7ff3XegVyzvibJ7zk0AiY8s07n1MdgMgvuip-X5auFGdNDLI7LrI0634Q-N7HHmHo6jrWBURWK6HVNWGDQf3NJpQk1J12PAJnhKkTLYOtxfbEmC9FmETzoU7S9gXt-LfuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اجرای شکیرا همین الان شروع شد؛ بزنید شبکه پرشیانا اسپورت نگاه کنید. ویدیو کامل مراسم براتون میزاریم که ببینید. نمیزاریم چیزی از دستتون بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/26095" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26094">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwz038Tj-Rbn-aJYkzYvfuhY1rkps1K9EW_uDTecphzHafEWap3iEthHNgSsG2WfNm93CNGgvh9P6EdcMRzB2FQh84bzQBGtQz0S9AnIgFDKiKy7-chwA-HsdLb7g3A8AGq2ycb_TSRXEWdmpdpo2GTGVfo6uqXyJ7yUSipTsr2VQFypCpW4Q0lCSV8Cgwx5DiTiRErknG252_VIVx_wGbpVG382ygbryHnSLcrH6i3f0eleN9y8beiaoZMN4Xx661YUDAZIYgPasl1_Mq8I5fFmymMuV2x424b1LaGeu0o0BGLFnivx8bcW6ycXP1KuRLsa8BL8dlEOfI-AmRVPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/26094" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=ozcduTiBMS4Cxf9SEy6V1GtVcrNgGjwndbr6uSc2apOTaUnNSd2PxVRQKTuXgJbhWsyb7T4cV5Q7Qfine7dwutwNJ4Xn8pIPnw86XShb-b6q04lYl2KFVz8G4e4ewoQgtetlCvFT9jaGRdn-H7cYmOkhttZd72hIdsX8NvN_rjMb-dapcHZTVSIl5YGYooFIhL8SQLR3Wa52DkSWAAn2HcOFzkNxpjrYeAt3ub2TfdwRvfynhD_bXiZUS0bu3Zm26EnMbla_UVK-eImZVY7Bz8QIsD-3WY7STW_G8Gaxu3qeuzu-wuN4TmrHrHybNTBVZFDZRX19aD9SbkD7eCxCbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=ozcduTiBMS4Cxf9SEy6V1GtVcrNgGjwndbr6uSc2apOTaUnNSd2PxVRQKTuXgJbhWsyb7T4cV5Q7Qfine7dwutwNJ4Xn8pIPnw86XShb-b6q04lYl2KFVz8G4e4ewoQgtetlCvFT9jaGRdn-H7cYmOkhttZd72hIdsX8NvN_rjMb-dapcHZTVSIl5YGYooFIhL8SQLR3Wa52DkSWAAn2HcOFzkNxpjrYeAt3ub2TfdwRvfynhD_bXiZUS0bu3Zm26EnMbla_UVK-eImZVY7Bz8QIsD-3WY7STW_G8Gaxu3qeuzu-wuN4TmrHrHybNTBVZFDZRX19aD9SbkD7eCxCbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛
عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDDE6CiP9JTujxKJivbsLM7Zg8PA005yKapFfSloRGnBn7OW5r4qywsUas4tEtJE-18aCbSU2z5U6YBvyczP36XjN9NW8XSgFWBxxQmlbmnJGyJzxwcRih3SbKe_WU3B0dekbQqaQp5CS42rE15vWD7MCjQ-zm4Rap1cbUvJkYXF2JlccQqQ6t86MymqPaI7ooHSgVQfNAWlhLl40bX9n1JnJCCbf-tuEVv0De-b2vN3fB61qciyRsh_t-6AOlx0wOFkB3t_oGLPOGmaE97Fwd9LiESoVtWI4nEfMAu85b2AGX5awAawj8iyyk7qvM_pu82FB2NzavnTlc6ub-QTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVKZHTsvPcJbVSAOUZduvsX8-aqHqsC_zVggOQzcTofnJR5qoUeuZRYGL7UioeSsfQZkDTOAihXV3gTFzs8YicZxNliC9eIXoXk9crhKO0XRjRj0f09uP_myltklu41G3bQ0tzl-4s-L6qM4TCUayKWQEEVJNQJBX9W7z-BOHhZnQKFiNhM4K5M69YJoUC5oNVtB0CG1P6Rl8Q_j28MbU143YbvvcPyU4B0lw3U6n2Z1BpIyvLR5zpKFdSJdhGCLJzN-Qt6D0o8t63qY5pZwtN9OMYnNm9hNQ4XKPBFm5_mesbTzNOm8XLlp9VZdwV0yz1O-Efe69JOAKgvL0VN9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26089">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=puGFCwoxgcptT7vSd-HQffCyBqZYfjbczoyntti9WfufV41xhIzjfp6Q8QhKkcXNIbsHixDWdUCE0uRlERDf77GyzLsPVlbmADCA_Vkod6AFMxLEc-q4O3Crcg53K9Kwm2KK-klgntfnrxcRTPHiRfHJDb8mvaYfRsgBCZf7EyEtR27CAK8_j4GSszyz6s58QE_4lc3A-22w2c4jl-iH99VruXCq1MToEqpNa4DiAVrOq1eSigtkCcKZ9769c5JNCF3oI1fNBlukBsArsCInuBvQZzFMNwl4Zh54TJDZHStPbENAwUnY4LXzZsTjYK8mo5oSNM2dhU3NOyoQomaklw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=puGFCwoxgcptT7vSd-HQffCyBqZYfjbczoyntti9WfufV41xhIzjfp6Q8QhKkcXNIbsHixDWdUCE0uRlERDf77GyzLsPVlbmADCA_Vkod6AFMxLEc-q4O3Crcg53K9Kwm2KK-klgntfnrxcRTPHiRfHJDb8mvaYfRsgBCZf7EyEtR27CAK8_j4GSszyz6s58QE_4lc3A-22w2c4jl-iH99VruXCq1MToEqpNa4DiAVrOq1eSigtkCcKZ9769c5JNCF3oI1fNBlukBsArsCInuBvQZzFMNwl4Zh54TJDZHStPbENAwUnY4LXzZsTjYK8mo5oSNM2dhU3NOyoQomaklw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/26089" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26088">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVCuPFe0zPQgy8VRFbnrNX2lMrdIMQQ9OlcHE5yegvoCigNhED482OT3g6S62KtQZBQlnNJtAk3GXhs-GRrigmAsX76ovd1hSkCTg8OZ1o3Oq0GqpgjY_lh22Echict0NyF6QvBD77Sa8PJ6qRiKxRW3Aci2Q0cJ-4Z0lKmPl98snGlGBHkFvJ_GXieZaeSp9qCkvR0lNMQ3j1Thk_JUA2kl90eL_u53nEOzBlcTxlHCSBon9V0DzurNHK6iV1X_0mVV8dLNPzRzozrxWcTWuotTaDZV6dU4CxYVwhtrbr2FOI_lGWev19FLimAvEYqmh3Kcms9V6kqL9Ni0q5vUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26088" target="_blank">📅 22:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26086">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68101d4663.mp4?token=TF1TUtCqoJMsPsvoONmayMNmfzF4A3OPHP03I8xuUqrW4eDXvktXWiOVtim-RWlQfS49i4LKqtrU3Z6bWakIw879Hs43RRRw3tZJB8-T8I_IspGRMoGkmkdhLM9WMAM3emKjYL3YjhmJ5kigdFLP-sw8W7EdK7E7jRT7ZMlpg81xg2k29fYB8Nt-RQ28zgJOc0snCIFo4Ng5XQ9bPTI-T2_cZ-AOmf3MmpJEt03ng6OYdLi6cxP_MfXohwQL_rPZxwGq-4DxD5L2TbHZgu3Ava2ZmzK0lA51003Igql8qtkKLYGao5dqiKB_IXov0yeSxq3Qn-zpLYeD7EG0eu86XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68101d4663.mp4?token=TF1TUtCqoJMsPsvoONmayMNmfzF4A3OPHP03I8xuUqrW4eDXvktXWiOVtim-RWlQfS49i4LKqtrU3Z6bWakIw879Hs43RRRw3tZJB8-T8I_IspGRMoGkmkdhLM9WMAM3emKjYL3YjhmJ5kigdFLP-sw8W7EdK7E7jRT7ZMlpg81xg2k29fYB8Nt-RQ28zgJOc0snCIFo4Ng5XQ9bPTI-T2_cZ-AOmf3MmpJEt03ng6OYdLi6cxP_MfXohwQL_rPZxwGq-4DxD5L2TbHZgu3Ava2ZmzK0lA51003Igql8qtkKLYGao5dqiKB_IXov0yeSxq3Qn-zpLYeD7EG0eu86XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل‌فردوسی‌پور: سعی کردم تیم ملی رو خیلی منصفانه نقد کنم امااین‌حرف‌که هر کی نقد کنه وطن فروشه نمیره تو کتم هر کاری میخواین بکنید. وقتی اینترنت بین الملل نیست من چجوری میتونم برنامه بسازم. عادل از اوردن اسم قلعه نویی خوداری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26086" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26085">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df505731d.mp4?token=LQYCf03pAMARLl1Ay9gxKFTw-QO34qstMIjQCXqndHKxdLg5uWh-VEKy6TdSfo7oJf6pcOENjZ-s4C7Ftrsuo5P1Qrevsfs1271ZPQ4mA9p76Dkaphe4_d5WNBfc6O6DTjtTqao5_F9NuKUT6G2L8oYGZ2liHtyQkd1iGQiI_1i5Sayrycad7clfPdU8O-QIBtPx3tv1D-lfE9iiWPMPBxUQPh5FGp2u5AX74SsT5NzFlIDxH63sTQG8aqPmSpfNEZL_uSBEyJOMKU_TgBPRQQ_nZQVjLGbAjM-AlLgbKmh8iknDMaEmyp_FA39cCArL6AeqraqNjM7ymocWKW-X_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df505731d.mp4?token=LQYCf03pAMARLl1Ay9gxKFTw-QO34qstMIjQCXqndHKxdLg5uWh-VEKy6TdSfo7oJf6pcOENjZ-s4C7Ftrsuo5P1Qrevsfs1271ZPQ4mA9p76Dkaphe4_d5WNBfc6O6DTjtTqao5_F9NuKUT6G2L8oYGZ2liHtyQkd1iGQiI_1i5Sayrycad7clfPdU8O-QIBtPx3tv1D-lfE9iiWPMPBxUQPh5FGp2u5AX74SsT5NzFlIDxH63sTQG8aqPmSpfNEZL_uSBEyJOMKU_TgBPRQQ_nZQVjLGbAjM-AlLgbKmh8iknDMaEmyp_FA39cCArL6AeqraqNjM7ymocWKW-X_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی تو این دو ویدیو به بد ترین شکل ممکن‌جواب‌صحبت‌های‌قلعه‌نویی رو داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26085" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDGoEOhUoJSpSME0D2rdedMVqW87dMz7QwoFdsNUMY2U56RXVwkJMnXupD4dD1FvNx7RSGhqAVUzegooSl6r9FBW7p6H3UDR5cxbfsAndEelwvJPmSZxsD29NRqJvCh_QDOz2QhwMfR3LfN1kvnM8uc6iQ4b0N-vrzPZdzkPLXdoy9mvkFDLtxnDcjcFar3kwmynMTGTmQETBhOyTr8USH_MOunqwNTDSZsihooMkSTlGBNQClj7tFR2tG13zYE-h8UiLIUODi2Jw32ctYAbVh_KMLrD5B6PgDsCGGBStXm_NgHi6lkS5N1JczqSD4Aa1KsHP1LQMJNc31W5SAslYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=aYhi3Jr4-Ih6txcTRNPnMyv5koIprarESbuZ1ARiFaJjCLWwIw5zf8kjnFK_b37zZ2VgXASWt1UbXGaY2LetXdTZeboI6xM2za1IkmLSAm1cNA_LuYJtnvgYP9r0bhUHtGjkvhQJLHGPXXKjjHIOVFcWyVvuTl3x_4vcGluM6Tm80f1lIAN_LZM4k7gxBG__tWhQEP0F3Ebis0LSW0lvmctIFnSnWvV5RpFCt4p1hzOZC1LtrwJ8Hp919y06mbWw2M3jSPk-wi-H7LaQP8s8_410Aco4tyOwn3tWL7TxHgI4-WQ-KvprYeNr_7n-AF2Ps7n6sVadMpNgaJ-pRCtM6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=aYhi3Jr4-Ih6txcTRNPnMyv5koIprarESbuZ1ARiFaJjCLWwIw5zf8kjnFK_b37zZ2VgXASWt1UbXGaY2LetXdTZeboI6xM2za1IkmLSAm1cNA_LuYJtnvgYP9r0bhUHtGjkvhQJLHGPXXKjjHIOVFcWyVvuTl3x_4vcGluM6Tm80f1lIAN_LZM4k7gxBG__tWhQEP0F3Ebis0LSW0lvmctIFnSnWvV5RpFCt4p1hzOZC1LtrwJ8Hp919y06mbWw2M3jSPk-wi-H7LaQP8s8_410Aco4tyOwn3tWL7TxHgI4-WQ-KvprYeNr_7n-AF2Ps7n6sVadMpNgaJ-pRCtM6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h49jT9xuB8DGKMNioELL0JJSOt9xIBnDbv1NBh9YhJCY9eudPXDRcW3asszJDHhsrlPN-H5xyk_v_akiFDrFCSvBR5fm1XrJ9bJgmzSArdyTIcn40IPdP2ylecsWlCjrrTYDHSdZc_DFlfR06944ZWAJ9dsYA84GVIjvLfL0WwuXUeaNerehLHsZlQxkv81qWePjliRnGNNjoOQz3_B9yeSMzcAwJdNAmZHfWOd45h38D5cSR-abP-kFr_BMukXlhiHtnAslKy4fWxRYvHAR7OmBXfeENG747eENVqPy2SLFutd1myhOB6Utgakgs7zeGFFKw3DcJAiAl2vQ2pg7dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnAzAcYqJqAh7rRTYAQ9_rmRo-zUxyAjLtZLlhhcOA63kuqTFAl3_kgYovx5jzIZMusG1l_11VkLVp0wRTGd0jnIWVmfYofKBB48R2z20_W7_AEz4iCY9Alf1c4xyUKR72x0Xa0XHolYpcSxl_1ZUzhYQTC6ILrbTudwHQHhenlw36tVdbR5ORzBG7zIhawctAZPpIt8YBN5waxpmwj6QlAyb_RqPBzXLKrUdikgZEcRBRgXXJVc7v-yVRBDQuDnu5lYbgNphGRzs7LToD-FqEwdqyNbcpWrRn4jpZ3YRqd2diok57PsGFYYKUJE5-Nd9KGNHtasyCen9IcrRQ0Zsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2vHndmCWqC9J8nZxlV1p5piHbH42SZ6paXRXwjp4yF2D_KYDBu-qol1Bi-MeWIWCJMseYqcvmztmwpb_IS3XPyZHJCh_087xNLDi8YusuWw7zbvwsLyX3ryHa7hHNVWOwmixludoJ48Nqq6lY18lXu8AQn1cQqdkVh_G3mbK5ttTyMp7lNmfEwl2Z0o7z_0owFnVgHYPFDm19eAy2g7fWq2qoVNr4lTPwvOCYGSd58YzZhgUbGeuslNRcu__00PD9Dfh4PBYOcMrUqzoJnINM1pPfxe-JraeEa3sf_QaKPf1StKXOqjp2Uoca4ncZ3iNF6fczckV8gu6Qa5jpvnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cfk_4hOWaN1U68Hc2lJla3KoddooD_uARivMRiM0Qg2RaqOtrtWezZ1D6I4uMzO7gW3Q2TCLS2r7tal6vTIUrkvnV8oNpkbHfSWqBrbDkFwxvWc0ttq4mN35U7_yspchhUojkwZ5jv7INhQHMH7TgE2gYgZxbdpxN3Ay_W3JuZVZXPPEs7qhnx6snUrP9R5f5lFlNjMrHxiHL1Xz4IJwvJ1bLlI95lu5tTEP5Q8ledz5B8Ssq6Zkk_tQb6nqX0EJwVhLdtQqX91GNQ4024Uc3YBvm7341uCOcvDHCIWhyQgqwpsjZxD7C0vN6ACfznROAHuuy0uGXZywRHQHW-eN4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1eaJD_dpYKdZfobp6j6jxBPko8M1DUXMXtDoNqozfMDEldojDphW8CJbZ2JrTlSpMrLi56GM1wBG2ib2es9gRA_0FYlgdZBG5MSNHkLA_CxlUV2DrVgDsBsgY7m_-IevQ8CXtcZ406YpDyyEG7yFLQgbkahPoT0IuOr_UD5L6SlfdeVBkm2yIEgMIJvGrTQNtN4Fmmq6MJ2hHU6aqOlwaDaYmUpHLTOggue8YM-G9MDV8ZGgGiy7phMwqxXQSDQJgWllrzcrKIXn4OBtKxbimSIhoSSN1ZYDzzoElG9subAXXodVfiD0ekQH3_4CAC_25G0OKXskWZ5xtxZmFwCiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26075">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5EpI843qQlY1RJA7oQFViJ2K49wDTjyBBmfoEVGSJ9cDAzPuwZxOgpXrjG0_xGf7b2PWlroppMxaZPPMr6sjgURkwR1xLWNbYutx8MmmAAhk7Ntd5VK_dAJGqXueucW7TAb7ES-ob0HyW9gJyVi4yHCxw6jQjCOwtbeuXm3DRfoZkgqsSstHJxPA-PCdMtnZJrt3we8RCvevLs1jH-zkj_WipXHxPbyTENNlB8v35j6wdVJiRTEYYGQ7feN9--ndK7CfcPtuNh0JRObNCg9wE1wUcm4khQsSWh01BAh1vkOnUs_hRUoCohFoe_HqWWvxV9uEXVnMJ4ymf7A0InMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26075" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26074">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6qqLk61_JrH69W72nFz_dDHsHNzqdPpW2kkB7i0GHWT1K0sG3azEklcVXYNu0xA-nf03WK7kj3h3Uk1TX-CJRq5eg1K8cCQDlFLh0XHR4-h87754XCrmWWGxIMO1AmKThFaJ9CUWYTWXNisa4ZiFE74nMZk_AsADxgU6CVB-0AG-_Au2QIRfkXrQtUWhIRM_7Q34CQ7jXaqMgq7qx-5YJtbSgCgSKlKC12cNrPPN29gNPnVNM01l2R3mLs80ocF9BjAG3arpmMJOg6kODYnWo9F8l1eTDzk4Y5NHAA1Dmlx7pRWxir__YBRb_ie5zdYQfzmjssDYAfJxhEJpC-qmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
علی دایی بهترین میانگین گل ملی در مقایسه با کریس‌رونالدو و لیونل‌مسی دو اسطوره فوتبال دنیا؛ بعضی رکوردها شکسته میشوند، اما بعضی از نام‌ها برای همیشه در تاریخ بشر به نیکی می‌مانند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/26074" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26073">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS1BbBNQq0_K6jfTbtvY-c7ZvBjTaVMvX0S-eZ9Jzz8l6KV1S0x2hbwNbxV5MZ9bKT9pn93hxtInkfIRqXr95mEQhOKTFDBpFq0qtmplKcLLytyuhGHuWlY7OzIfMBFDMRZYwltcmSrqr13hLEGqS6hXgIL1Sh0WNaRt06BF_bS5t7asrxoIpKX8gfI4ZLhGVxzXu7AUMhqCheRfBJucCAoI_paC3KlXslzGNddRggDbKRZa9G_vhbBGf72Zc1QtaUWBWZ_WEeU52N4f3vjFdz5XkeV8jRoA2IJfRz0I4Lx1zkA-XZ3UaajC_LMPDONBSoj_-Z0bfpRPkfRYsOD65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین
🆚
🇪🇸
اسپانیا
📅
یکشنبه ۲۸ تیر ۱۴۰۵
🕥
ساعت ۲۲:۳۰
🎁
۷۰۰ دلار جایزه
به صورت
FreeBet
بین برندگان واجد شرایط تقسیم می‌شود.
📶
علاوه بر آن،
۱ گیگ اینترنت یک‌ماهه
نیز به برندگان واجد شرایط تعلق می‌گیرد.
✨
همین حالا پیش‌بینی خودت را ثبت کن و شانس خودت را برای کسب جایزه امتحان کن
https://t.me/betegram_bot?start=p10_r4EF37DCE</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/26073" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26072">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHw2FdZg68nlZmhQ1ihFoXY0mPK941ilfzTXqI-gbrRokZ6NrYzcnMTA1mQzX5Siwr76Mc3ZhZqjom389lD6N49u429E-c3NLE8CXuoyMN6IBv2Qd-TvrapHj1CIEIEuoaxRouhZ4bTFjxztsu508XDsFgi_6b5s1gQyt2pQ5d5md8XjupkteE3esaPku3rk6BeNnciZJjw2_7CtWCKyhjr9EmWhB3d_dN0ISLRfK6sC40IsVzJBGKbdjjms7GRLOzVL6Cnv1MNjykSry7RZtOg4Ty7x8Ftp71ZVNDneRpTB-Dn-1QUqwBE1IBoLRrp_LRS1zMCFvk7UNAl040bwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:
عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26072" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26071">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCiShKAuVHvPnloWd7Qbc8XTLgt5qONMWoX_az4N44VTXOe4N5Y4el3OUf5kcSmE_w9BEMQ0-t8tcsDjj-7kVUiFU0mJ-aH_F29xnqYUlw4cjIcpFS3TqNqCJKjGMdnMM-X8Nk7-Z7t7HO37FOXt9k4dl4wAVGOQV96CS-fMhMq5LQBSTUP96hsSix7eu-iN8abErO4Zy1mhHzDkLcLt_qdgbkwfZuoX8p9PvNbXUk8jXyrkj4Q8ek6l_cIy6rt2naXlWPBE26LO8l9kCvIAW5U5mLh4HeT76IjaD3XSI9FaBotKv_nDIRgoESl4Q7vkzVH5RR6Zxa71U3S4VNws4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26071" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26069">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=rcoFTCLakiWNsmlgbIRJz05AkMLCFg4zjvgqMW1uAztLV-df3g-VNw2QlEnCan9z9zGkL-h6R2O9aNREu8zxzHa0KliXJDhkNIgNLDxC2AZaP9t60CoFVbRrgiar-hGEsahjaQbRaLEvsezn4BZXfngt1wDp3prXZ4cv0napvZeA2iVX3315pQAl2hxWT0a7stPm96bh94olgCnIWuJzLe1CYPXbOPnDOwzOhAPuZLF69ZLNsT3yE3mSydH5D4Ol0IF7CsAeP43rGSHrCx7mVfmdbxNK_1P9130indGdMmUuuTyhzcikChkUrlMfBkAfJT5tGjnHNFZXcwZiv5gRRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=rcoFTCLakiWNsmlgbIRJz05AkMLCFg4zjvgqMW1uAztLV-df3g-VNw2QlEnCan9z9zGkL-h6R2O9aNREu8zxzHa0KliXJDhkNIgNLDxC2AZaP9t60CoFVbRrgiar-hGEsahjaQbRaLEvsezn4BZXfngt1wDp3prXZ4cv0napvZeA2iVX3315pQAl2hxWT0a7stPm96bh94olgCnIWuJzLe1CYPXbOPnDOwzOhAPuZLF69ZLNsT3yE3mSydH5D4Ol0IF7CsAeP43rGSHrCx7mVfmdbxNK_1P9130indGdMmUuuTyhzcikChkUrlMfBkAfJT5tGjnHNFZXcwZiv5gRRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26069" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26068">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bX4ewok8PZeIWBpi68LjMDGgFyAtR8JiDfT-JcDTcgTWOhKQhoQKnwKn9XzoqPFvWJbmIHUZ1PRgnj9-WxHbwyo1k9226ql1-eDRPWFASrGaeDacW46NFcBEWl0NbAG3V8I-t66TTkdeCfM1Sghbs5M5SW-8G_I5ptU-ubWqdbrUounW0SkZx44likMvQ-GwALWbaGRls0NkHs_dpzkl3Zir6Ie0RMiaEH_ZW66BaxuUgXZONfTEdFW6j_mWzAARbCitc4GRrEVXkEu7qGC1Ek12XIeNSJAc8KLgR6nlJQFY8j_A0JHrCXZeIn3O-rJBDOpTBjLbRwP7sDyvpl1JOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در دو جام جهانی گذشته؛ تیمی که در مرحله حذفی با نتیجه ۲ - ۱ انگلیسی‌ها رو شکست داده در نهایت درفینال‌باخته. این اتفاق برای کرواسی ۲۰۱۸ و فرانسه (۲۰۲۲) افتاد. در این جام جهانی، آرژانتین در نیمه‌نهایی انگلیس رو با نتیجه ۲-۱ شکست داد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26068" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26067">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQcAzmlFtUvCkNg0mz3eDd3ZYrB9QFxzZfo9JWSeFW2JDUAaOoJBeNztxq9zkNywaQZmoSFzo4p5s5hBaV2ydIfBm2qk6H3Hp4df2jHM76IuGx9kfHU0UB2eF2W6aY7sJ-_l9dP0v-IvJXBAbEbZpqFwyQKJkGg1DDozsqkGigdFBXCWc9tapIyyt_li6cZc4gDQOq96KGB0D_I_Bt1CV7d9ktx9nXkjsFO6aDsteHPfYNI2Dhn-jruYdRmU6oUSeJ0R1refnsbhOyvZk1SppI27JiQo2G8A_jcOzbH74JnqoC3n742y-N_O8kHyu3K0Nqjuf21Cd4NC0iakmEgAMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26067" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26066">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlhrT3SPLBPlhjFPQ-Uc1hLskqduaoSUUa9aIZEkQ62RGGJARHdLKbwMLAaQpZWU_cXaDmlWBTRJIET1lcf9BlFFOHzbZgOgy_BtaXEy5OLTdy_z45PDUVyGnMGnC-j1KWvbz9Af1uat03SvZKftGNqdBHsu3RDOEm00PKg27wLhs3-4vhN2JDRkxGNQhyjiXRWJ7etp9ZLPaHfLGFNG-RNUPqb8iZhdLch_fRtyrgaVfhdYJkjKoZDU3JFKNJpjUWjg8uDI9s8i4Jl1aZYDLf9dHNSlUyzuWHGIALDx10eHZtVg2laH_ezybyPmgsnKB1L3Czk2g-p--F3VQ3dxRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
طبق‌شنیده‌های‌پرشیانا؛ مهدی‌تارتار سرمربی تیم پرسپولیس از وضعیت فنی سیدابوالفضل جلالی مدافع‌چپ‌جدیدسرخ‌ها راضی نیست و به او گفته اگه عملکرد فنی‌اش بهتر نشود مجبور به فسخ قراردادش خواهند شد. تارتار نیم نگاهی به جذب مدافع چپ نیز داره. جلالی سه‌فصل قبل آقای…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26066" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26065">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=mRyBN10dhfB_c9LKzNurJ4Rb80lD6MUMM0MBrLSNYrIkI_B5G6zTzOwRwfL1F8OfHM1hJJKcnCct_M86h03MCVnhCxcTQAZQuadNIHTFqLorsYg-iQTvbqH7tAFif8e4vaaq5uskbB7NdvG8NELjJqeeFA8-1uiyDU5IC9zbE0C4U6Me2qpx9GAVH1Ac_SgRuABbcz66Sz-lQdX9BUM7PWHDrrMqH_4Jcq7gywxUbYkMMQJv2tPLAzRTScSKn5AzCbRmT41-0t8LLZnVIfgO2Ix7APTXS0MxD-R-64tHjtvv-FBbuvWO8e2f-69E7j2ywbSikWsfqEtd0RzDFOp6Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=mRyBN10dhfB_c9LKzNurJ4Rb80lD6MUMM0MBrLSNYrIkI_B5G6zTzOwRwfL1F8OfHM1hJJKcnCct_M86h03MCVnhCxcTQAZQuadNIHTFqLorsYg-iQTvbqH7tAFif8e4vaaq5uskbB7NdvG8NELjJqeeFA8-1uiyDU5IC9zbE0C4U6Me2qpx9GAVH1Ac_SgRuABbcz66Sz-lQdX9BUM7PWHDrrMqH_4Jcq7gywxUbYkMMQJv2tPLAzRTScSKn5AzCbRmT41-0t8LLZnVIfgO2Ix7APTXS0MxD-R-64tHjtvv-FBbuvWO8e2f-69E7j2ywbSikWsfqEtd0RzDFOp6Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26065" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26064">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZOYdOwlYVXZ5NV6lb00k09NM3tXXF_svKxyXbQ0JfuOGhT5Et9CpSKGpV-HTOyVWbOnHn1rYGgTOKuTA3pLfK9gtl2AeCQpNiHhkNyG-CP2kkcuKvRqSxXVmjJDd4nh9SR511UYrIumvQHIxD3gBHPvhE1UTmBn8UGzXd3dIYSIEexQRVYpdGoTkRTqOPA4UolNcbmnLSEN3Myh9pwl2FlQ0D3_2Sl7WxbWnZoJRw94O-ukaocTdMVmBARXFN_fwXDSnaTotr2QLIMaQ66jT1PfqzhgLlqoN7Igz9zNaDEo2xJXsQ9EqdkJgTbYNBvz7gfG0l3l9d196PoQ_SsOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26064" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26063">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=GgYX328VjNcyNHlso10Jrh2K5p_vNcqLHr9rQZkM2KpvKx1taGF8xouLHa7Q1vY3fU4urfL4inDhXdniVkO98EQysSmQzumvHf469RdwEmtJmVzFMB_yLf2ReeuuaQrj-q598mxyGcuj5wUtWzMUGND2qa1COA-HAtnlzCU8OiW_fj9bJD7Ra8VELIeHx0DvR3hPL64GNlqojdhG9UC_89xEMoMIGO-NtR3BL2h7jQJw0ER9QHDMoSVlBHNU9a0G3qCJ_Ano6P3MwbvT90Xex0KoELueO1q_J9ZCzltDIVWMkEZcraxvhd2gDzmR9YR7a25Ldt3yudIV12gjzJ833Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=GgYX328VjNcyNHlso10Jrh2K5p_vNcqLHr9rQZkM2KpvKx1taGF8xouLHa7Q1vY3fU4urfL4inDhXdniVkO98EQysSmQzumvHf469RdwEmtJmVzFMB_yLf2ReeuuaQrj-q598mxyGcuj5wUtWzMUGND2qa1COA-HAtnlzCU8OiW_fj9bJD7Ra8VELIeHx0DvR3hPL64GNlqojdhG9UC_89xEMoMIGO-NtR3BL2h7jQJw0ER9QHDMoSVlBHNU9a0G3qCJ_Ano6P3MwbvT90Xex0KoELueO1q_J9ZCzltDIVWMkEZcraxvhd2gDzmR9YR7a25Ldt3yudIV12gjzJ833Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه دنیای فوتبال را رقم زده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26063" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26062">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltSBajRbrcv1y7QApbqV6qpmXjsR6r1Wq6QdWmPdGhf2l0ICPR2xbqrxDtggEjTAcsqonIpSE82kJTIKMGuZrlxfLwCMIW7dsdHRGGr_fYtGiQFhtxIa0p5P5To7k_fP_OHCs3_UAX5S16WWv51Mb3zBONyY_6EaEWtZLonW4ejaTmJ7Y89SgCNGvHU8FgDuGbkjYHAEy7e03-v5dzkWSC9RhMl29jUMpwXfR6x6Y-BR21pZIWXeQuSn2z7LUmB5tcgGHET0ExXGUkfXSKWgr8MmBo4-QV6sygdyi2UzzkEUktSsfEN9WSaiJbAyoPukhkkDQSbHzyZpL-xJT5Y97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026
؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26062" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26061">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIxMh8FOkd2Uw0U6LjRnFChNyXmdHfKFC9sjrWfMUA5gT-Fq4TJX7Ct0S1WY95G7lCEEthkmg2P5JGnijPd6GB3ytlWb-TOptJyG2d0SXT57qyhMxNupZI1HIgbo-5J298DuEab5E2JM8xC0yTR7HgWOdN-OhJ3224wtloFQ2NHe6XNfpkflHPFsAm1LvAvqW8bnYXwyx_IYnk3aaHFymLNtBIv94DeHS48_-yxD_sH7Dr_xtxhOq6LuCm5XGQmINJ-GQ5uJ3TkB0_83uyXhL7GflO4ilKJ9um1T6_TqVFoRKSMRtHi-l2rRHeUj9n7jPNqWE97Dv9_T5gGrur8EBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق‌ اخبار دریافتی رسانه پرشیانا؛
به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26061" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26060">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZUpWesZPo6oMAvzFREGClSP2LhwxXsh-9WiTD0KY9RWwC76GMtTykX2quvBtzcde8hx5mo_GUCZnes9vhd5mL4Nly-xbdGHVgr-0yGkbeovi8-1_L5_AuV6JI2sRUAEaSOrI907X9Kz_oPFynWa8YrjunZGzghd9_93L2_4oUFglliNZpD27YX76TDbFJSYKS1XnFqqhcahN3Jc_tgMdM9zSPWl4dvfwFeDsX8Vl-F-tHdBAZGHLEsJ2vSPGhyLYltlM_FbAdI8FoJjibqePXdU59eoTkwKJYmzwFMMjmWQnegwLQL0XyjtHq7wp-eVOpdMuPWFIjrkX4Zn05s9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26060" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26059">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=OQ5_BO_ta6g_F4WSEsJW8yV8GqVeirJFzPF_lHU6hLSmxMOPOQY-oJFg8_QuJ6i2-QHGViiRc2Wr7GWg3yqyDhvZYvDtoeLizqYKDNr2zbYDqXhdyG5W-VJKvoyfXukqE-PF3i8srJ9-HAI0y46qTkBeUBi2v_B-kBE6GX3Q2V6kXem5cGJc96D2S8Gs4LmHG3IP3kOsin0CucXJ0kvrRh135GyR7cIpDBsi03TXU8GxpFJ1D6hStxvxJpwzH4rxIrsY9DgpF8pxiw1uVC4AYpOXeRXMQoRi_vCN0XhnX0sPdm2hBlQm4OReFkrZsjrqfNbx7buclj7EQ31ruBai4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=OQ5_BO_ta6g_F4WSEsJW8yV8GqVeirJFzPF_lHU6hLSmxMOPOQY-oJFg8_QuJ6i2-QHGViiRc2Wr7GWg3yqyDhvZYvDtoeLizqYKDNr2zbYDqXhdyG5W-VJKvoyfXukqE-PF3i8srJ9-HAI0y46qTkBeUBi2v_B-kBE6GX3Q2V6kXem5cGJc96D2S8Gs4LmHG3IP3kOsin0CucXJ0kvrRh135GyR7cIpDBsi03TXU8GxpFJ1D6hStxvxJpwzH4rxIrsY9DgpF8pxiw1uVC4AYpOXeRXMQoRi_vCN0XhnX0sPdm2hBlQm4OReFkrZsjrqfNbx7buclj7EQ31ruBai4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26059" target="_blank">📅 15:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26058">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzeR8ijwNXGv5RucEXGFz2UIQT0iYwP29XS0cZjSz5bLABbNPVuQIGc8ttCnrzZgoPWIVY4EE0b0FeOugTQ-2Kjkf3v9XpiJs2zcRxd6fsAIJwRnlYNMOqsu8VDYwSUIiTQbpYtKwqmh_jnBu45oLqs3Y_5kbnzkqTPpwpGZNxqFDDAoJW9XNAuLG4wYZtF0neaQDwzOKBNq1zjQiLFlXTDK0xCFcDRDP0LUTLq53NtwuERrvgoqTzwFQLs7Rkg_VhYJ_wJUwZmDAdaAJwj7Ts8XnLylIh10lP5aTM8T5gv7E2m65r4ZtMJCsAVbzIIGyr5MsvNBzKY7rfjf5Ba2PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26058" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26057">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8HJ6X3TWUUkJlvOeCOdI4xvdzWTbv27KPHSoLOAAZtaj-cN9YGahl4Y4hv9ocBw0tkgvhZtX9Uf3Exhr1Ofb0_Dqtqt2w0Y4vF46ZGfhOVGok_5kz5O8Y8FpteIvmsXOCexqbnezDoIH2gLOVH6X-rWUcyWETxGly2_pwPwGmBb26MS_zKdlhr5R3Tt7vBRzXxF4Xhnoey63GVvoBjRenx80GYtGTCY_NBWty8TQiEN37mm7we-YcoOgAj4bUbFfP8xbnx6aRQxcqvStGuCkE8253HWnRbKKneVTDkjHVH4viDWfZMpM60SNRLfUhKIy8uyooPygKlk_z0SSWO4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26057" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26056">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=ag1IVV2pSTZD9cjU0znuxb8XqiuWKIFxFWmc7dXuFGC74TacCGiXB_AtxS62QJjR9vb-oG1nTLE08gUxFKWcYjUAEqBs45JW3m6Pa14_L_XAWNLMzgixwBmiF5J69icjC7gRNpLasptjv_yQcR0yP_jN6kGqcnVjSXcHudLmWXq_permaAG2S7dz99Q9l0XNAiGPP776eL9TtOVPyzJKLIzrdhP8p5Le-xKNo8bEMlTjMdJ3TtWSixB90e4SR2LMU6tRvrxLpQ5qhSbDJ9-0DmoVI0ePU6NJry_jky0XHMDk0y5pQ3gZ6QrMUywk92J4KQNegHeHdo1ujkuVOjrreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=ag1IVV2pSTZD9cjU0znuxb8XqiuWKIFxFWmc7dXuFGC74TacCGiXB_AtxS62QJjR9vb-oG1nTLE08gUxFKWcYjUAEqBs45JW3m6Pa14_L_XAWNLMzgixwBmiF5J69icjC7gRNpLasptjv_yQcR0yP_jN6kGqcnVjSXcHudLmWXq_permaAG2S7dz99Q9l0XNAiGPP776eL9TtOVPyzJKLIzrdhP8p5Le-xKNo8bEMlTjMdJ3TtWSixB90e4SR2LMU6tRvrxLpQ5qhSbDJ9-0DmoVI0ePU6NJry_jky0XHMDk0y5pQ3gZ6QrMUywk92J4KQNegHeHdo1ujkuVOjrreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
از تاثیرات جام جهانی فوتبال بر والیبالیست ها در لیگ‌ملت‌ها؛ دریافت‌جالب بازیکن‌تیم‌ملی آرژانیتن با پا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26056" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26055">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=jkESbsKxu-bPdUNJjo1Y6JiexXnfC_w8z1qd86asSrUuL0kWWGlcqMoUb67qtXwqdcVGcZU4eXGB5o-DLqeH8RxHDvE-ZmDASfXqgZoPj9TcoElsLz24hk_XWyV7rUDZzFPDFPn_FoTvLKvf44TZrRlhuCV2yO5NpW3YHpiLM_lkN3yrCSiP1OrVQVOJxf9A7E1CL-iq1xCNAh9f-kAS7WibRiKuditoz1nFzgdPGJ6xvK4_houQIL2DTB4Biuo5KfUgTbDlOLZhyCxsYSZQtiSh9rUq8n7NjuEcr3NcYiUah1qbPxGII4AnXmWGWrILuS9-nGgq6TAIlSyCCnlS9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=jkESbsKxu-bPdUNJjo1Y6JiexXnfC_w8z1qd86asSrUuL0kWWGlcqMoUb67qtXwqdcVGcZU4eXGB5o-DLqeH8RxHDvE-ZmDASfXqgZoPj9TcoElsLz24hk_XWyV7rUDZzFPDFPn_FoTvLKvf44TZrRlhuCV2yO5NpW3YHpiLM_lkN3yrCSiP1OrVQVOJxf9A7E1CL-iq1xCNAh9f-kAS7WibRiKuditoz1nFzgdPGJ6xvK4_houQIL2DTB4Biuo5KfUgTbDlOLZhyCxsYSZQtiSh9rUq8n7NjuEcr3NcYiUah1qbPxGII4AnXmWGWrILuS9-nGgq6TAIlSyCCnlS9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پله همیشه می‌گفت زیباترین گل زندگیش رو در ۲ اوت ۱۹۵۹ مقابل تیم‌یوونتوس زده! اما از اون مسابقه هیچ گونه فیلمی وجود نداشت. حالا گوگل با همکاری خانواده پله و با استفاده از Google DeepMind، فیلم این گل رو ساخته. این ویدئو، فیلم واقعی اون گل‌نیست؛ بلکه‌بازسازی‌مبتنی برAI و اسناد تاریخیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26055" target="_blank">📅 14:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26054">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRPPAwxqK6XVSn35TrVTBKreDxRu09AgrmmDuHA9vtjFvy2nlktqj9wDW3CJfAvypP1DGyreBWMKlBE7CQ02BC650x9jntSqCETDWCJcZsd9wMWnnS6WIj2oIaqloW9U8NktXFQ1DO7SYzgLyv_6QYa7voed-iMlxSwZBUSztsu2n08Cm-fi-0P30EVm2KabnicITC3bE7yMwmRR9vWGVtn5NAvm0OKtXnA0rlNHk7JUNkdmQCvxB23GfUKjWKxxcm94FEoe7Sr5ZkF50rncFPtB-e3hsxZzEFm8vDqqtXQFnxskBMUOOCIaesWLX_HlJ3eBPzbfuSPgQ7-Ed_9zpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26054" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26053">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8HD6KNh06pGnR7Vd6UAiWE0HvbwiJzGWYHDeHAeKHA92NyK8PUCEmjxIvLqH0ynABcn6K1ha05P01yRHMS8i_2wfJrthm6jsjgNuMyEtJSs1juUR2Gebw0y5n4Amye5r-_Dx2ae7gQD5fL01zgmzbNLtcoYdfg_Rsg8rlWVqo2Aesu5qQd-iuPx1fV-ZWkO2WDpB51AKARLWbvTxXlYjxDGfDZWZOYgblsUlIKBL_PZJ_W3LBXJLCO6XofUahO6qji-PgK8BNqVdfe-1IIEzKfm1f3qYSwYQqHorTEgRlZcJ0wfUBuvBbREGSwfZ_lXQIGTbG9PzZ9FPh18EJJigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26053" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26052">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFyFhaBGxuVv9wI7K_3vD6H6XP4xUxfi7kfaY56-7iPnCeY2ZhrA88ssEmFf4Aqre12dvreiy8UaRAGcV09TyUn0wH67WQSAg9Fhzm5kkZLPs1UUxMRrzv2Ph2SI0k-QZaa9cpy5nHh2fbI_oQ7aZIqA9atfnkK-_lGNDN8Ce12h8ixoVulAqzZixXmRKO9xEAwEHalPHsum70v6jRVK9Ky-xpZE6zyYfUKM-VrhVzZsgLoDg22gYEbzdBgUbjkE2GAoG5wyQOB04IGB71kfRLswNxIFJ5C5mWdA1lRhvmMTOZzZxD_LFHRYR2uHIWF8FfQK3IvdV8YOVERqx6vaAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26052" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26051">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWBFjjmGRlZ404ZBiqKgbbRaOpo335Z-piCb9woZu8PlNDarvJIDzOWfyOwGh3_Xm8obhBB82CW0JSL9KbldQV-SaHFive_iNLTYM8IgMXYu-wphPz7b8Zhh61z1UUKKsqtfkrwnn2c7mFdvZ-ZagvvGABwOBX4qEJzE-7j6UramARp3bkiEuCNot0nCrHhpyWd8Bl7On044gEzM2vi8AbphxYFp1bKajD03mj7zHIiA4JLJ3BdtIfp8ENjVPtuzv46CJRV6G9WHC3cCuZmtbJzWmaAkVSbCnmhyZnxF-x956MLixF7Y076hT2Q2PDbW7vpmPwZn6jWFLN1Bd1MNfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26051" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26050">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcHzZjUqWxhej5MUZOoJYCbS_Hbw8mGp_-d1EXZ2ch5JUsgiHRrM4pyttLjqjleYBzvZoII8RShGyUZ8M1PTkQ8l8OvI1rSBiHfYJpOLijMhv_o65cVNMPHs1nqxeS58G1CV67xrN-xlUdXzMG5-qZWY3d68fTAn4oGhXwDPOzShC2Ojfwga7O3wybJVaxQqRec2jRnUpCikxiPtB17mKM-uwCIoG7ifpxhrL6bsgSfL7dLv4liNMIC5TLb1kW3Y9_zEuP-mD6XLlGLGAlJ0JIdHE1b-bEvh5ukTPzC-lkKrW1Ac29x4krg0pseJz-pdFtsTk46XuBxXe9taYy_KZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26050" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26049">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpIqu4iTE17rTXNVkvvN4HsiF9b-Fevy32U_uVZ-9uni6RYYFqUmSC8ySdT9dxrBtf7JJ7RrbRnNL4IBivxKuLIFG9-2NQ-3KBOvWylpcagEmmvM5zwJhAaPSzg1gaiu84DIb92fqrhiQfk_HZafLYxHda8cHyhCfMlROAxdNiN1WHZOoexFolyRWuu1_EHPSFMJllGhWAL6F4eRhnZL58VHvK1DyY4PcqDAFvfR3uOjOhj9edTbh8u95BDfK10wKtxPnjNqErNUkqOXcM5I8RAxQLz8dYAxTEeBDEbFYkTNWyscJpgLf9uRAM4DYF_hL7Qh8X9FqSyBzu8wXQGrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کلارنس سیدورف اسطوره‌باشگاه‌آث‌میلان و رئال مادرید درکنار همسر ایرانی خود؛ سیدورف فصل قبل بعنوان مشاورمدیرعامل آبی‌ها 250 هزار دلار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26049" target="_blank">📅 11:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26048">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgBAZH_SUCFiVMWBZwzROl-LhvEC7na7_rQgoqYco2_FNGM8YUaDHKaN5htl3aKKzW4GgvVMNXGQViF7CcLM0g_Ey-V6x9je4CShZbTwGk0vaSb_S2FZyq1VE1T0kJ7LZ2QXhTx5HD5NhYY7-jy55yQBrkw6abtNddOdoPDX5TIk9s2aUYVczXwB0c5Sc6uDgnkZnP0ikvMEGKrbUFkSwrGYzSEgoKAtSnHdJkv4z3PnZXhXs5_u7o4TTiTQ0MVUBXd4YNRomFc5zPXeNHehhWLenOyFbnNm5A7RjrelEF4km_CMIG7aGrNuI4Iv0Pf-U5jy_wPicKIsuVJpA05t0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26048" target="_blank">📅 11:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26047">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8LJTfH4StyXYcqClhcJcnL8A4JCMG0MAZHwN-8M6VHo0cdjdHTFpweoJ2VWRr82T4YqMtyeEqExjpUW5l7mO33WtFMB3DG093nYQFVLq4CvG1SDLllyhO_PqCovMQtx0q37CUjDIEwhurvZ6ZvT3qT7XR2eh-5mPBjyEfj3au0FITKaLis5Dfci3b_023BkyRgCl5vjk5RlnTorkkkXAEANmBNBQXyHb224UNTv05Z-WoX99ECaGJF9EKteZhIpSUGDixKG-k-RPmCYKUdQ2Zs3efGlTYhq94Qhjxiy0ASElNZr8ElrpQCBU4v0KM6U5M5TZs1VBdi2yrDWVhksig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26047" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26046">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhTQCWfk0qGEbzTmTj25sC15u7La-qFEJ1n-OE8pGFqqSJJwXL0sFh2rcOd73cWRnc1BtKH6C9jpjVoo-ex0tz3XbzvZqnuKNJwi4pnz637F0JhbWFHCiKE12QE6pzAK6IOkF0Cbw2fpiXQ8dXwyrqipKstFpBHtHRWB3jCaI5U2g-Y2fVqWg66KpNdvf_QiNzelXGMdh3_4dRwmqsm8fpVLwY7mhEPwG3eAh8GS7NySGqgvMSbapUREb8Hc-999uTLSROKOEnUJBFjVwUzZ56ojeCdT44YoxgQmBK6ngFll-NdtD09PFu0PxuBH15c3QBrtL9wxcbRxLfiC2kJwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26046" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26045">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odL9_6eL81Bp4NSi-Vk4ZVf4vFu-JXfHPjlO_ykJyp8j86D-usjc71muOe-Mqo0djWMv8xTRcLiUEtIlL-_S-pUMEBflFQaO3HJXhztEVPGHONGd4eyaYgEgP_chFNN16SSWerXyHc86H1Mu2lUxGAeM_Rl_h_maSpZ3KM14u0OcjsEUrUirRW_Mo5MgJ4NVeWQZGOxe4KHiclY2ILE9zJZOCqK8myK-NT44-iGtX5l3OcB7UM-UfrHHCVsWHNwUOGPW27Weqnoy0YCge_TstrcxHp4kmfAlMLyG7WBkrYMsBu2D2sC10tOQXMoOI0CLk9hqZ1P_Y36icR9CypaQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26045" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">📹
ویدیوجدیدوبرگ‌ریزون‌میلادکرمی بلاگر معروف و محبوب ایلامی و ببینید. رفته رو پل B1 کرج!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26044" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2k6inj52MHQE0E4qqpkQyDFXLTIMtc4Nb3AfM6YA2q1ztjgeLRQRcJ454zA7un74k_jAMULHpwDun6x-xmyVJg_4tMRl7EtWICnLF1vQxmmWwyAF7rESatGVIhI4vHBt5IX8Vu0uqKa2xX11faQSjbiAdxB_nCdoy2w8_0q-S7m0m8UXuLs8vwfQzOQjRogOJPI2ImILH61ni6Sx7Pr_A8pzZigaYdgRQHRzaP-eQt7OuUR5rRvd1omKp_iZ1Kjjb6ReowN9cgEul6k9gcP3DFy9gxRU0_NWruY7YlDb9lX7JcWkYIQUa47OnfjsKu91-ty1a5nw6ggKOLRAWs5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
برای اولین بار در ایران ، فری بت
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎁
💰
سوپر بونوس
وینرو
، پیشبینی بازی فینال جام جهانی با بیمه ی
200
درصدی
☄️
⚽️
اسپانیا
🇪🇸
✖️
🇦🇷
آرژانیتن
⏰
امشب ساعت 22:30
🚨
ورزشگاه مت لایف
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr28
📩
@winro_io</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26043" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=iZpPqjFvFEnGVnZtEiLklT7UgXJWcjjFbRsepfzJraB96JVBhoqIfEHKqnqEuJ9oZaQ9G2HZ-nzM_6GlF6X0qBciE27e5QXlL2S4rSV8P8oESQ9yBvJ6CvXM3SV5VmN8Vp5TRwmIJ4NZGI_gGouoda7aI3lCl1zQbmY7pMwz4fqtG4m_ZndatPs8zsCFsSAVPK_ZtlIT5Q1T7J_JoTGlc7HBAoYr_TPqpwvCeASj7XUO2cZujibgGkoI7HiRCPlqWQw-hv0OHD3ydgIN4-d4NoGTVZf3kPHnnVs0_XlB0l9hnsbFHdjiPyYmgQ-TjXfLsyp5yH1horpaKRDczVCtKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=iZpPqjFvFEnGVnZtEiLklT7UgXJWcjjFbRsepfzJraB96JVBhoqIfEHKqnqEuJ9oZaQ9G2HZ-nzM_6GlF6X0qBciE27e5QXlL2S4rSV8P8oESQ9yBvJ6CvXM3SV5VmN8Vp5TRwmIJ4NZGI_gGouoda7aI3lCl1zQbmY7pMwz4fqtG4m_ZndatPs8zsCFsSAVPK_ZtlIT5Q1T7J_JoTGlc7HBAoYr_TPqpwvCeASj7XUO2cZujibgGkoI7HiRCPlqWQw-hv0OHD3ydgIN4-d4NoGTVZf3kPHnnVs0_XlB0l9hnsbFHdjiPyYmgQ-TjXfLsyp5yH1horpaKRDczVCtKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26042" target="_blank">📅 09:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=s_tLXF0d5zG4ZTmZBM022xHGgMVtIDg0nGFqbLCztf0NvmZr7KTGm_BYXwCUpMRnZPBlO2SptmDFdAGegyDjZiSAAmLArpz6DQumLigMBesd-LgKXqbYVRQ8DE5KrWo7pX49RQ3C8lR1Be2Juqi8ucfObPMvXO-qbD4e_rP2YF91J00qasLZ7F8_M1R6QX5G10P4nfFv6tJA8jXiZ5pMzES_ErWfdgBAqZfDQVkUdh2x92kEDPKuvkB6jlaFsokJmcEsZaPySHJxRyWH53WNHE1_0x1CpEHBNjMHCNjK6Vi011AYVdi8Ia8j7yfO0cK1RZGH02HZOYW0U9lWxMU_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=s_tLXF0d5zG4ZTmZBM022xHGgMVtIDg0nGFqbLCztf0NvmZr7KTGm_BYXwCUpMRnZPBlO2SptmDFdAGegyDjZiSAAmLArpz6DQumLigMBesd-LgKXqbYVRQ8DE5KrWo7pX49RQ3C8lR1Be2Juqi8ucfObPMvXO-qbD4e_rP2YF91J00qasLZ7F8_M1R6QX5G10P4nfFv6tJA8jXiZ5pMzES_ErWfdgBAqZfDQVkUdh2x92kEDPKuvkB6jlaFsokJmcEsZaPySHJxRyWH53WNHE1_0x1CpEHBNjMHCNjK6Vi011AYVdi8Ia8j7yfO0cK1RZGH02HZOYW0U9lWxMU_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین و پی‌درپی عادل فردوسی پور به امیر قلعه‌نویی سرمربی ایران در برنامه شب گذشته
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26041" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده و مهیج شب گذشته دو تیم انگلیس - فرانسه در رده‌بندی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26040" target="_blank">📅 08:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26038">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bbAGmDDd674oKg00uHItg5GQPiP72B_0_dD0sHwNIrPREwi2S2L5PJEBJMktrgmNrSgn9_fUVvE_HopDFlD9QwMera-1wDWFx5UcFEp8xuAbQ6BRC7C10OCzr0aUgzhZq_rXpxaAvPerned_MhNbG37deOJtgrRKpBsuLjxCt0avI_eTsPiaM-Jtjt_a_RU_yIzU6uImhrAl5ph1qzqKbr5YGxJNTxbX_HFHiujzW116eDmxnSrArTSJK3uphlgL3TxaJUjnHRMDdUoxHDn4d-u2bAB-T5obsPO5RbMZrvN6CuU9wSDn08YCPhnaulnrf1f_x7vlCDF_JXYAbPMXDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHJ52IpG4lDHxDVztVkB2tjShp-zw6VU8N3NmhWfmcHbDJFjksi6lIdYZBC_Xv0Ji_8bbyZ1ndRZCXyYtaE5JQ_WcQLN_RUy3BHMKrwfDzi2b_Vgyq0HVAMqKPiLFjmw8ah15gQiWvSyiK5dTq-Sav1VRPQYTT6sDnNa5JmJ3OCED6lflwcESewxWlFwmLpADf3Mp2VWJUXDTnZmI7cBqWPJ7caeIPf4WTcAFpNZ9PFVqBNXNf0qcCpbTTivSixaTbj5MCOzP9wB4xTHwSz1jHOXSfz6w-HafUN5EMDAQdoJPyJG5VrEvKFAaY_kM4STDwX7OFfjJWH9t0xl8R548g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم‌ملی‌انگلیس شب گذشته در دیدار فوق العاده تماشایی بانتیجه6بر4 از سد تیم ملی فرانسه گذشت و رتبه سوم رقابت‌های جام رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26038" target="_blank">📅 08:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26037">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoMD0hzMNRZ8Hn3rIgoI3BZoad_CUJsCKD7WMrf4Q8s69twv8jmHZQsUgY22DD9KQSTG37vSYoEecEb6GJ2_s19OztkdtQMumITlWJb58MPdjfWKPXiP7FZ0WWKCBx-O0T67Hp0VROayOOv74oeaBAaYMnGvZ_QmZLkG0fVbTy_Gu70XH5-lbGzHZfW_8RVNbqqkALcRzzn6rRz9uDDw9qAFqXS4BrPbZOtS5gU0THHReTE8wl_XvafR_XAPRNcUg5z5TcTBQtLLnykNJhsywRd1WtAZvnP_5QMgaif1bUSkmyff3kzmuybYZbXWEnCMJ8R6ZCYfXAV65fa5ZjsA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26037" target="_blank">📅 07:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26036">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=OcBqDc1G2je8xzhBuJSsP75nvdIzthL-_SD7xrSHSSyg_nxY52oh4dYze7mzZARmj0Yqmj11vRTAVih1cM8gsCF69BIuQT9eBF94sHEYCBeSIDXgkf03JIkQZGgYoh0FpZXAOV819FGMB8lyQxdnmA_ALZlBFaBgyg2HfUAi6YI38PpTsYy8x8YRLqxpJ82PfgvTMSQ6MNga8yK3JjW66nnELMbJKEv4Zea1B2xUVV88LhRmcrrQNBX_WseIRD6j8BsTe5PePwnkMqh5wvQs8kjqdRiRB4uHKJaJ_RTHa7QO0A6Y067U7K0FdED8joOXe44gBZ4jIVybrbG6fmf-DIMGrtENYQ4uSrI46twZYsumTpzhYL-3c-rQl5NSsXpNSQMo5aB8OySGjGoQMtZoj3-gHebVA3DtrFt_I0F9M_dWhJJK7rPzOjnpQfOQE4T4Lif-bO-q7_9B6HvyE4NIMAg6MPqP5eASxuqdJ_1mxk-oay6-_sJTW4rgxlUX7XFA9xdr4UDoGGl4AogH2OuZW7Hs2BYwWx0S4CqNWJjsD0K8_X6zHgB6GmxvucR_mv3f39pVw9zWQo1YAOoNvRPDQXjrW66uEbf0BRJ73COs4yy7vhDtC6uncUgDNW_AxxSo8QLCCPmGnYw4-OntgojqlLqoW8iLMRFJJoRd9WlcV3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=OcBqDc1G2je8xzhBuJSsP75nvdIzthL-_SD7xrSHSSyg_nxY52oh4dYze7mzZARmj0Yqmj11vRTAVih1cM8gsCF69BIuQT9eBF94sHEYCBeSIDXgkf03JIkQZGgYoh0FpZXAOV819FGMB8lyQxdnmA_ALZlBFaBgyg2HfUAi6YI38PpTsYy8x8YRLqxpJ82PfgvTMSQ6MNga8yK3JjW66nnELMbJKEv4Zea1B2xUVV88LhRmcrrQNBX_WseIRD6j8BsTe5PePwnkMqh5wvQs8kjqdRiRB4uHKJaJ_RTHa7QO0A6Y067U7K0FdED8joOXe44gBZ4jIVybrbG6fmf-DIMGrtENYQ4uSrI46twZYsumTpzhYL-3c-rQl5NSsXpNSQMo5aB8OySGjGoQMtZoj3-gHebVA3DtrFt_I0F9M_dWhJJK7rPzOjnpQfOQE4T4Lif-bO-q7_9B6HvyE4NIMAg6MPqP5eASxuqdJ_1mxk-oay6-_sJTW4rgxlUX7XFA9xdr4UDoGGl4AogH2OuZW7Hs2BYwWx0S4CqNWJjsD0K8_X6zHgB6GmxvucR_mv3f39pVw9zWQo1YAOoNvRPDQXjrW66uEbf0BRJ73COs4yy7vhDtC6uncUgDNW_AxxSo8QLCCPmGnYw4-OntgojqlLqoW8iLMRFJJoRd9WlcV3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب‌وغریب میلاد کردمی بلاگر ایلامی از افتادنش از روی صخره بخاطر یک تبلیغ کلینیک.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26036" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26034">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=IWUKBxNXLCkM-p_niJPXv50DiNTEaJ6ctahlU43PUsn6cPSz38XkEDxHUi4JluzG3ctFVnYLrWk2RrT9WJPLOH6KkKGEZSkOA13e2jxVhRPgNSvoL34TNC9xtkjl_zP-VPiStiFaquLNqVJUzV7wN9j-kotj5r0BbOx6vuwQKHSed3a6sUwxoCyjSw5fmi0FKhsEIBDD7m36k9disZnPkTmG3G0Tb5tk7eTOgkYPzpv2X4jGXShT9X1ijXopUFiJDwlR9NGgMNKzsxuMpHtlgWsSOC4wxQWJ4s9L1JDCVKZ3SaqR-GFKJe2vD6DJLiqqcjXXeT1DSe7D2Fw4IX0WCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=IWUKBxNXLCkM-p_niJPXv50DiNTEaJ6ctahlU43PUsn6cPSz38XkEDxHUi4JluzG3ctFVnYLrWk2RrT9WJPLOH6KkKGEZSkOA13e2jxVhRPgNSvoL34TNC9xtkjl_zP-VPiStiFaquLNqVJUzV7wN9j-kotj5r0BbOx6vuwQKHSed3a6sUwxoCyjSw5fmi0FKhsEIBDD7m36k9disZnPkTmG3G0Tb5tk7eTOgkYPzpv2X4jGXShT9X1ijXopUFiJDwlR9NGgMNKzsxuMpHtlgWsSOC4wxQWJ4s9L1JDCVKZ3SaqR-GFKJe2vD6DJLiqqcjXXeT1DSe7D2Fw4IX0WCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🎙
علاقه‌ شدید‌ جواد کاظمیان به مونیکا بلوچی ایتالیایی در گفتگو با ابوطالب: خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26034" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26033">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=ZL4mGg2glJ0hkoBpmdAtQQ8uDA95mgA6uAwy4LrcYohyRHKPxcmN8tZVy-nkREu_hirquDu17YPWNs4dHFfqmNRo_j5qbpbR3SlO1_j-WdLBnUn4ey0s27QL-TPTF4RBX08E71crztRJqQkitdVdKLQURWFcTWKefq-WBDE_KeZTQAmAmSb82LTAzVAHVIn7TYO6lvuCoZQciYos0tDRqzZTfB_TaIUQmyEViHqUU0h-KKYI63RFMW67Jyi2U2SNSRERoM-PwgtbemjTz0vVVgGpnB0AvQo8hM7gmj_3DmVSX4iPeEC4X9fTkdgnoBgUm6xgydJxpY1Yyep-Pr7zCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=ZL4mGg2glJ0hkoBpmdAtQQ8uDA95mgA6uAwy4LrcYohyRHKPxcmN8tZVy-nkREu_hirquDu17YPWNs4dHFfqmNRo_j5qbpbR3SlO1_j-WdLBnUn4ey0s27QL-TPTF4RBX08E71crztRJqQkitdVdKLQURWFcTWKefq-WBDE_KeZTQAmAmSb82LTAzVAHVIn7TYO6lvuCoZQciYos0tDRqzZTfB_TaIUQmyEViHqUU0h-KKYI63RFMW67Jyi2U2SNSRERoM-PwgtbemjTz0vVVgGpnB0AvQo8hM7gmj_3DmVSX4iPeEC4X9fTkdgnoBgUm6xgydJxpY1Yyep-Pr7zCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛
سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد اما گاوی در کمال تعجب قبول نکرد و گفت تنها عشق فعلی من بازی فوتباله!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26031">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kix654jJlIPJh4kXKOEAPOYacdlaUO9SoD_SS9q5kz07nMpFCUB149ClmWOgTaAVVw8TiHoh9SfQ5gU2uqa5pH0qLZU6v63JkxtXNIjwjhdj4X1J-zhqQvEa5rWgz_rfgQsw3szahdYIxfx0IPXqMqQhVsAA4z5HPP9J9NtEye-wFtJ99ZsR5UFDjOypMtfCY1MCSLmZJYMr4d7mpvlwJGWpDJxxF3YLZM5wZ7hNLBcxEvXBODDqRCCfvvRhvw--IEK7TPQUHe7R5TKEbFFbg8BcocRjeDU_JtwcqOff4nGm8ZtZHu_m6WiVTrGg0rlo2x-9UArFTRqmv8tpe5m7xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26031" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26029">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=cZTUrwZjCe1vkiUDdXgb18-6yZ_eV8PADzvDJJSVetSmkVxXPy8XZliwN8isg-DdwfQyTaxFGHNHpVy_G8RNMGpDoeLiI1_NzO4ofpHBKs8uWCbgEDRlqhQegZ8HyGI3R6OQgP6jQpnimOIbAgoB6w93GIcMxDL-fUQJJkRuRw7QzIlbg-2ggcnbRtKQj2VqIJTGg71Zus4X4SyIM9v056hMMpv1vLMeMzzux6JIBKWT_Ys_-RcY3ck14u2tBSbhLIakijYJroZRKhKqj92yAWdWnmhMfNiyAOYXWHg5B5rIPOxquVuDThYSxXBG4XSf_fZHn219anKi-o7ke2FpZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=cZTUrwZjCe1vkiUDdXgb18-6yZ_eV8PADzvDJJSVetSmkVxXPy8XZliwN8isg-DdwfQyTaxFGHNHpVy_G8RNMGpDoeLiI1_NzO4ofpHBKs8uWCbgEDRlqhQegZ8HyGI3R6OQgP6jQpnimOIbAgoB6w93GIcMxDL-fUQJJkRuRw7QzIlbg-2ggcnbRtKQj2VqIJTGg71Zus4X4SyIM9v056hMMpv1vLMeMzzux6JIBKWT_Ys_-RcY3ck14u2tBSbhLIakijYJroZRKhKqj92yAWdWnmhMfNiyAOYXWHg5B5rIPOxquVuDThYSxXBG4XSf_fZHn219anKi-o7ke2FpZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26029" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26028">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soPirOMbp0t6KFp5nOF7l3_-ooqOn7IaQnSMFSMJcS7uVS8UfdW5lpeDQk_xWGijWYxkuBj8anNjtXtBjt6738oSy3cG4fmQ-_9z0hneEP6lAB2r5DciFY3kBJ7RoJcS1w9_K-yuRcRfjfy36eGdYPvMmh88h0mMbfQErdD968T4LgqZJ9hu9ZlxxAYgOT8214fgqo62oQyAI9EhnABRfDz-JqgrW37jNRicgINSBqUij1_PX6qPErprdIFF__B_NOLRYw3Wv1094NReOik544fgumpA0ouvRDf0eme0M2v0m55cb7SjuVkJ5Jfvzq1OwLcJDakcxC33P0huL2THMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌دیدارهای‌امروز؛
کمتر از 22 ساعت تا نبرد تمام‌ عیار آرژانیتن
🆚
اسپانیا در فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26028" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26026">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIRpEx9p0unHhxvVcXRAtufEEgzU7BLmSmv3y_jW-2AwCF8VbOyahMzTe05C2HRKjeeOm7oqmK81q_s93rJvvcj8ZEQFIHuyqeDOk7H5NCyhMLWY_9JDEwNaqTGx2OiXfY1acpOh1HxM_WupwSy5ORAT-yOgf2Nv2oVI0eVHwaGqUxWPJrZlys3Ixnou9loxTMfJtffMHBIOrynkFA_Lv1p-JIfDo6a0_B48F7zDTdX7g0hyWQZ2i5KbJZ_7h3060P58D_m7ZvGfW1E4vz5AUR8So4r4dJyukJ9k110rPIU6M0ljREf8QPCGiVdOpabglGqtSC27wdK3vRQgck0EJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26026" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26025">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrBNSD8skm2RbB14axnhlOC56ESMS6UaG_NSloQQo9lnj_FtPobI-OPjv5w1ObbGOYteeQ_UC0Xb2mP2nIxs31E-FVMJSQ0Cg20VRj2-Y1950jkaWajlkW8i0ATJK4QVWTDEHv0gb36VKE_HM1NW7G1oxQuExWbcUJ4nC5pHzkMiU_To6vbwQ_SC77DIkC5hzo4XPsAYgRsrPE0Qx8X4k81hojof7SBeVeTW0KZTBFqWFPAPYwTaMubyi_5AIbr2OaMLkE-x4SJSAeFI7F-Sq-hT62-m7WRDB_JLcpwQvt2eH_EJ3MvFl-1lcpyI6nNjlpq1CYV5vnEPK4bOTUaLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26025" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26024">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=p2DmPlIR2cqt47EVqYoGW6IJUBxb5zcRTpGzFMPVJays0l8J80RuGMxRur5Es3-Kuw1erdJRGFEPAOXGHknuRubswo5GzfMBlLHkvHjAIWI93WVj2PCmLVGSyYnqhU7LPSBoQruRxAU2RmT-rlg1xbBUG3sSs604ADyySiBOgPc6mRErsGtTwR5hm-bd803_fqb5MQ_TXxxkb3gPHJykENzvwAjO70f6TmVjnSQB1RRagEqVkDJu9izXtwn9A41A218ElnD0A8aYcsJoU9V3FQjO67QI7ulJi1-NSWrXIlU3EfkXIJv3neEOprUjqDHAzZEmlyTqehERMws6BCKDGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=p2DmPlIR2cqt47EVqYoGW6IJUBxb5zcRTpGzFMPVJays0l8J80RuGMxRur5Es3-Kuw1erdJRGFEPAOXGHknuRubswo5GzfMBlLHkvHjAIWI93WVj2PCmLVGSyYnqhU7LPSBoQruRxAU2RmT-rlg1xbBUG3sSs604ADyySiBOgPc6mRErsGtTwR5hm-bd803_fqb5MQ_TXxxkb3gPHJykENzvwAjO70f6TmVjnSQB1RRagEqVkDJu9izXtwn9A41A218ElnD0A8aYcsJoU9V3FQjO67QI7ulJi1-NSWrXIlU3EfkXIJv3neEOprUjqDHAzZEmlyTqehERMws6BCKDGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26024" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26023">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=HrSFnVETDHluDzRIaWPi8nu4u_CqIQ22OxZ2GkJI0rc2lVcm4b8JXfT-BpotkDAWq1OGPbiL47e_3hC0oUhecBD4QL9gzxT-bVSKmXyGiVQE-kr1rID0ADxacSFEoqVumyd3jMqnhIaCrP9x5ymyToFRduVgmwYlhRjO5e2mAZ_ahann3ZXX5LEd1-zZXcwrcPyruzcPAYa8Vh96u1_3WaQaGE4M4xtBZbPlQIpGZDtGLxRcrhLfDqF3zUUP55PVKIvsnnPwH0qk37FPShnId25-hU5syYPtyP58wTeDsrzrdVUMbb6747UEccAkix_-K7s-qzGoUGDkxzsi7nJ5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=HrSFnVETDHluDzRIaWPi8nu4u_CqIQ22OxZ2GkJI0rc2lVcm4b8JXfT-BpotkDAWq1OGPbiL47e_3hC0oUhecBD4QL9gzxT-bVSKmXyGiVQE-kr1rID0ADxacSFEoqVumyd3jMqnhIaCrP9x5ymyToFRduVgmwYlhRjO5e2mAZ_ahann3ZXX5LEd1-zZXcwrcPyruzcPAYa8Vh96u1_3WaQaGE4M4xtBZbPlQIpGZDtGLxRcrhLfDqF3zUUP55PVKIvsnnPwH0qk37FPShnId25-hU5syYPtyP58wTeDsrzrdVUMbb6747UEccAkix_-K7s-qzGoUGDkxzsi7nJ5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب‌شروع‌شد؛ جواد کاظمیان با انتشار این استوری و تگ کردن مونیکا بلوچی تولد او رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26023" target="_blank">📅 23:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26022">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvtB26scQXIMKO1JgGOEB611NdvHb7DK7_tJEdj6sXToa8RfmgFXCAvnBmCqTh59VrRDD19v7SdTDOWTptb7cpQJMQkbhhnIm8us1xa0lHz1Ie6Wu9uIexykUG2he14KxRY-1fCP0d9DeM1Zzpk4RWgKH7aeeZbiZMTbycyuvLoWHCcP27Y_l3U77bsELOv3eWS7EZPBEzgaetyFxydsLwO86K8b2pIm87WtM3v7TpMKDstLl2vQxUw6fcopvqXrM_4Lu7o3fr__8YRNr0VxDLG1KgoY8C1nFPYpJUxNNOdb2Av7HQJY6zEJrZKcze2_fjjVxBP5O3pK81HSCA5SUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26022" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26020">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWa1mu5VSlH2_oR5LBs1OPP8boZKhZ3TDJ89S9rsEYnNjFCpJA7hniH1sJtT-pdLVQvPRE-6BmO7hV6D3-Bc1PKk7xKONgOukXafJP3jGPkrPKD1OT33fpF2Hr6fFhXPrc62Gyl_UO3Ur6Rr3oQkeKL_2a4RvyjE7LtYTS3nP3aJm5lkLMzI1Pxf_tX_ceTDd6wnYH6q1V8lbGBshcfCxiJnCdPqn_L7nHdEUEcErWf3ZSl_HJ0yXf85crgUo3cLrgE3aa3EpJu3BudBczSq_f5ARg9qmUauxMbn-1H4sw3_CrfIaiuJ-HMsw8X8wrvCLvOJTsq9BnN6Xt0XxZLA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNZUmre8qhyjD3cAAwHTANMq3rX-Gh3EQt7RjlyONshZXS-J5cHAkRtnKTK5MDyJDZkhci89xFfcrvxcFZeZaTSZbvQDZGk6jqv_QKWp6SyXNXtVQfdMbGA0MzlbHuovjrx6gXmMvWEL8wbvZ2IjcW1uyiSc8tKeBjHl9I7QFuMOizLdJJXPoSv4qQbesIr84kcWs4hCuPz7aLJW_JDJ9mOsT2MyB1zr4JsDMLLrCQtefHtOPgG1sDAcCuKnNPpxXxzRyJvjko1561vk0SotLDnvVJCUtQsDKlWM2ay_Spppsn_LPn2uNDFn3WpXQG_FpqusQlXkUEFrfaaWZvJsJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26020" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26019">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5sYHLJ6QM4nKl1g50K5PiVizo18r-fHm1MhuHoekXMpO-ZyC6Orp8GjHwqZB8dX9lZVBIRxtUqvS2A6gqC5YpkgIQN4K8FnRTTqZQKReLXpGPSGqyjCMCkNImN3LOM3uBWfJLp7h_1ukEpUZZ6zO2cVoEHIHQZt8mgWAyQo8hW2AeDnVjY1CDpM6vw-aRasxqCFPO-shAFI_5ZOQtTuVjmk8BeC22FloxhZdPEXHDu_AGopId7Z51XS3nl4AO9bAP7sE3rtZqIO7NAjDtWqrrydQkZCeBJeITWPdE3V6pffMQHMh3tJEl3cGSUgMQPSCDLT6p-YaraTbcklMI3q3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26019" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26018">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC-W-87A262YzfjRS41ktyjQUS9hFKeWA6bTvGHDoJi0-DnboMa9YryEfdTzSbLzZcLHSxwXnZo4ZsieFsj4dsSxdVP4lvEm4fLO923VX7k9uaTQdfeM_MMGmCgzPfW-t6nbqEFZe-O2ufSXQDlUe4Wiq64wD366Hhr_nqWr8MvhlaMvqz24hbNa1HjtRoNUbBCwFNgudVQnlseUv4wlvCRGAb28e5dSpSmUdFhR3y0cdLkO3T0i8CZAi5iZUZOkMYgi8XmNK44GZOrbcS8FguO79C68fAVdeXAJYBlqNkNEaObZU9OJXIN_4QWXw5aneVMlujJFRpRCvXsFYxGjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26018" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26016">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇪🇸
🔴
هایلایتی‌از عمکرد آلن‌هلیلوویچ ستاره سابق بارسلونا که در آستانه عقد قرار داد با پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26016" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26015">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YssXBim6sLB5FWIAxvfRgHfd05ULaMGg6F-MfQcuQZGkrCqCBJta-3ZhwXzp_-mDW3YCt9QzlFRRkXVwMKUhBp1qS7sOvHIbYxWK92chSoV8e3ID1PMbvg3Rs_OArCo-ocCCB6NYoWTJ3joFkGbDbFBPvxJsnhlXLrtT4W-T2sKjQSCFjOV369WEPWhcLkg8E4RjvsMAy82lsiGCNBgOLbgUOplw79IXOrrWLy7ScAeIN1OI8MdQtcfrC-0WndJ8Ssm2viStlsD8qM3UN4MHZkLtD-lzA_ZaRu9EpzHaNBsRhhKIVlnL4c6fmauF5KCQsrl1GgqIXEDADGAtxraFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه‌پرسپولیس به‌درخواست شخص مهدی تارتار با یک‌مهاجم‌کرواسی که سابقه بازی در تیم‌های ملی پایه این کشور درکارنامه‌خود داره وارد مذاکره شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26015" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26014">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIDt60DePFpruU2HQ4FxrgI6m0k2N9klCHOKoZE5aExMylBhSgJ7YdhDQF84lopGuJ_F0FDWsNPcHFpuBY_li0LTNaO4FJxvguVsxJp3Ptpv6_e7aupaojQliAEOStCaUlFK46NglKgLwY7M7cc7oh-BtY0SgMhBnNsctpQNXUeqpS40vmleD1i2xclW7UW7X8rMNsfIPiNgQz2kDyBGw8q1HLaqmU8IeAiCij0OjDrtify02jws-8-knbvvvR-HvGownjpd2_RLtxAfX2J90yUGwF6Pr_wTOu8cxctOUBaAjhhpktYDzLZwNIWeK1j3PQsMSTghr7k3rru4CImX_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری اسطوره باشگاه چلسی انگلیس:
این سوال رو از من می‌پرسن که چطور می‌شه مسی رو متوقف‌کرد؟جوابش‌اینه:هیچجوره نمی‌شه! حتی اگه بخوای با بازی فیزیکی جلوش رو بگیری، فقط باعث بهتر شدن اون می‌شی. مسی فوق‌العاده قدرتمنده، از جنگیدن لذت می‌بره و واقعاً هر چی که فکرشو کنید داره. به نظر من که اون بهترین بازیکن تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26014" target="_blank">📅 22:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26013">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=Ub4uaKu8LROnrxnAtaRNGEk7rBoBd7ZRk3V4Qm83DveB5YkWQ-ToQWE2jXRRhiD1AzwiJottml00e867G8x7SW7HFpd11_wY_ucPpAaLix7ws_3B1fOJGIChP0Xve_JD-_jbVhhuiVSvIJNfL9hynBwCRTUQZC-IbWzoxQCKgSPD2JMjDIARVlKWj-dzMxQ4wmpf4gAge8T4p34viL37opNAOXK8geJFOVsxPN18zZrRCa_mnchWHYAL2TRNIN6D1_-SLI4T575qMhai7FCseY1EedPM-OVcmuTQ2CHVYnSJC_EJNcC7u0w0mDo_7LlZAJXQ-rfAEA1yLEg3tsl_WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=Ub4uaKu8LROnrxnAtaRNGEk7rBoBd7ZRk3V4Qm83DveB5YkWQ-ToQWE2jXRRhiD1AzwiJottml00e867G8x7SW7HFpd11_wY_ucPpAaLix7ws_3B1fOJGIChP0Xve_JD-_jbVhhuiVSvIJNfL9hynBwCRTUQZC-IbWzoxQCKgSPD2JMjDIARVlKWj-dzMxQ4wmpf4gAge8T4p34viL37opNAOXK8geJFOVsxPN18zZrRCa_mnchWHYAL2TRNIN6D1_-SLI4T575qMhai7FCseY1EedPM-OVcmuTQ2CHVYnSJC_EJNcC7u0w0mDo_7LlZAJXQ-rfAEA1yLEg3tsl_WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26013" target="_blank">📅 22:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26012">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECuerQ4x-pXtIsW4j-69Dx8erO7eK8mQLJ2rYlYBk-SbfYrpzqpIsEHkstWux2J8TTgGK7QZBdPWU7scvqN66XZcyKomZ8v9zC6PNQMlWakVGcy_Ft1FobJZsyc9UZDAfDTYCEZiouyQH-evE4ibeEXZDEICG2XME_XnWkUInQphl53frbrVYMOuUVgtRLlaOWWpzlM3DkjFcSJhv9kWewOrQsEnsWoay_WB9qNyybX3COGTyKTLmVbBiDo3Ff4XXHqgp_XnjmOP9aVaYyzAtvEHwiNqfn69esKCwz3bzpU0OimnJ-ICASZzzt0I-n9nBAlvEZP_9l15Gmri8UMb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26012" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26011">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrdyoaQXwi733OHPtQg_4x6nJ_rnKMb14Z79wJDIVjQUKa7qkgbk66AQktwran1F4rXSPJPQrvO6bIpVWitqVgr0eDZu1h99bLhOPIzu9ZyzZb5wB91nKHwLOLx5pPFuLWKDH1IJt8xKeBUoBvOMe-ZxWrT_vmcjVGX8h26Y930G32D_P_iymbvoPImsmTdACShqpj4hxfjwYNkmbhZIedXv2sz1rxKOrjHUByHAzRT5d5r5rP5sbWqoYelMd7GEPqaYxiBbjJUin5OHCmrpziwi9eByPbC3rPHFlNu3d5ve5or6Seh1DThG9RCYEnSctV1ytwf_bANMpgsiLoxMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26011" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26010">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtDokFdAiYfnykNQu2Y8jG0VGrWNbe-xTzvUuC7YrZJiv7QopSeDAh8YrYQ5xEQyBcbzt4WgTZ3qRAm3IXey5Cl-tL4qWsbCQO9vWZsFjEc6EhdojfbiaP4btDvNsjodsVm3sPgD-d8OigK9ZkdJR4GvQ0QJRNk_lLDDsYqKBrDrl57RrnDZiydKYjzNP48BjvNyUIBgVXS0ge6GgC46J9pHy0KxFcEGOl57f4KV3wC4Ardw4sqRkZ_-4EPLPjl4ohbD6PtRqwGI5YNlOz88fUMVq8qnIOa5dhLjKs0mDHbk7hsJ3mntVdfyzG2ur-UMwmZNC7K9bwf52DUvSwcD9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتاین: آرسنال هایجک خورد؛ تیم چلسی با ارائه پیشنهادی 137 میلیون یورویی به آستون ویلا درآستانه عقدقرارداد پنج ساله با مورگان راجرز ستاره ملی پوش این باشگاه قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26010" target="_blank">📅 21:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26009">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O92PjgF-HxWgUbmKdiD3iMv7NeiCTOlqbQq14Ja_JRVToN0O0ghKxuIt1NuNDjngfahtLr7SCuCWFwGKyNCt9iepMko4D0paAHG1wQUsyrUuFXHJN6PIJ6DDXa20UNyP0uC3Sd9GnNDKH8vJzgl_O85eI7PjV40B2W2VMzYg4GGGQ4r9jie5vyjKcTRaBqxBWOMmJDYp-Ug8yvLKcWbtkS5Cur0YkQsWjtRb_L7_vTJfK4F3kq1hvdl4PCFDypWUpZ6Fe-m1BG_0_RGcymziOQlyU7oOQkSlyGKhelIEOGNk34KZfzbTIYYXx0yxM6x3ovMRgJ6ADy1UVAPvx8MssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26009" target="_blank">📅 21:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26008">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=oJXR8Fv9FckKb-R01KJK_59UpikD3uxcckcCfRdCVTSEC4ljM_ZYVxLoAJ0lZSme1MYqLd_QqBwZmWGWaWgjedbwygLMNyOgSoAoZ42UONKjkXbO3Q6hQtHiMIWgb-DMQKxkfHd-G6G_WghwJZmfp60mO6SoP7YoBqKU0KH1gWZgC43TEDg2GupI4mn7HLYPSUr0J6z6CjIr6VyPsX0JCpRGDIM6joLWwz_J7UBxPVBfNJUaWAJtApFJUK-bQuv7hz-oZgxcMTZEnxz0VAuzeW9oRfHWzq9vVM-gv1Pzzp3okSvu7eiaD-9Y208t1a_pyV4VT2hlDltWEHXK6FAcbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=oJXR8Fv9FckKb-R01KJK_59UpikD3uxcckcCfRdCVTSEC4ljM_ZYVxLoAJ0lZSme1MYqLd_QqBwZmWGWaWgjedbwygLMNyOgSoAoZ42UONKjkXbO3Q6hQtHiMIWgb-DMQKxkfHd-G6G_WghwJZmfp60mO6SoP7YoBqKU0KH1gWZgC43TEDg2GupI4mn7HLYPSUr0J6z6CjIr6VyPsX0JCpRGDIM6joLWwz_J7UBxPVBfNJUaWAJtApFJUK-bQuv7hz-oZgxcMTZEnxz0VAuzeW9oRfHWzq9vVM-gv1Pzzp3okSvu7eiaD-9Y208t1a_pyV4VT2hlDltWEHXK6FAcbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تو زندگی همه باید مثل علیرضا فغانی باشیم که حتی اگه داور فینال جام جهانی هم نشدیم از تلاش کردن تو زندگی ناامید نشیم. امید کلید پیروزیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26008" target="_blank">📅 20:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26007">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiNkqg6h1VUCxXlGrTStXEkN_XTE-Orxyap8nffukMDjIEuQlGv5FaH-3zKK5r3gAge-tCaGiz12FPO-50bV0kQyOhmeBSvVJ_UwnuiuxTKpDwtobVAetdkepEXrS9N1RL5utDWtc1pmaEpoJHwNocM_87IrELYOdGoRCxSs70gZf-JHgLLp22wMuH_c8wKnoqSKGajxNH_P-0vuuPUCx1i0epIpivYY7Hnh6sx0vaqowFzKi8v3O3a0-TIRcOsx6Hvk7QxViyu2qWXQEGqluuJACnXrf4sXQPqJT7xOWV4ET_LtplwiBH63D-UP-IzlT53SaiNX1GEgAOUfoDeU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26007" target="_blank">📅 20:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26006">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_RPCVsWyakU1FGobYeNSFTFLuZK0mrbm4Qf9zsN0fG5MizGPMEAirIWYkSMSqAQr1bcZcEgMDt161_NxJPAssK_MdZbI8fuiY1UbkIjvxJSgzdjiwznN94ynDZKMe-NqD6Ank8J-W8GvqevuxgToaKznomwAehtzZeYEG1k2tHFTM1JFUd89qxnMy90OY_cMPj3s2oaBw_m8HWHxO0OpFW5rWQaQz7Mo8wo6g7fg8ITIXHFnXNLBAhBlZ0J9p-sO9D5cE2J_eIKctcCRM5cM8-pZF8X8H-yvCZPs5kY24R1gkq2DbIku7MJfJXi20WKWo_b5Ot9sDZ5trMnkrOOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راجب خبر حسین نژاد هم‌پرسیدیم گفتن تا شب بهتون خبر میدیم که توافق استقلال با روسا صحت داره یا که خیر. وضعیت جلسه باشگاه پرسپولیس با نساجی برای جذب ایری و طاهری هم مشخص بشه قطعا تو کانال میزنیم. خبر رو بی سر و ته نمیزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26006" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
