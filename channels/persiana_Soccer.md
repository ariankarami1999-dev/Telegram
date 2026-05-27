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
<img src="https://cdn4.telesco.pe/file/uS6TEvX0AbxU5_4YZmbrIq7ZkWqdW4qxEZ5NeWkd99gmsj0ktVpBvCR8-CLPxXIeYF3jhPtBYaNBp4Z17n5W0Pv5sDi1M0Z-MrCjfg6-tUJpxaOgxILINeygu2W5ANrANIqkKhnvfwDCwg1jOL10pfJrYhAwX_WcoF94aKARMQAH3qzizQkHbN3JBsOCRu64qV3XhN6M7zJ_jSElJh1Y7D0u4CehuOcnIh9rHLTTFeuDm2gpyvaKrG3J-4jABfx--m1klgMVTEUBz4OBm027v9mOjU8Xi5T5unHeHYwcZnl4AwcAOpSdS-IY7TMT4dr1CfIhqp9kt2fHIE9he9IczA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 186K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 21:09:14</div>
<hr>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Da5jkPAF2Ypo79_1tzGKAHdid1cW6UOYjJ5LKcJ1N0iSp7zQjg9Y0E61vAHacLn8mMwxoeIWkEp8GEA3pm7_MzNuQH9SW9gSmmS3tz2oAVlJwmfOLXG5umpwzADlqn7Vy6veouZZP73LFKwWgmVgKDDy9w6e34P8pt4YjKBe_adVELooJNRGw7aml9g6B9PuLBOITdfGbtiYrNSFoakgkzfF8g8qPOXoxHyapSnCSL65gjDrqFSmQSIGIMWjaAt8V4OC_fZOk_0oTnXwSDrLbtszFOWYCzYDe6-XrWtFwahUU5BCebG0erXT7m7Jh1V6hr08TIx2tjNvw8sKSmQNRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Da5jkPAF2Ypo79_1tzGKAHdid1cW6UOYjJ5LKcJ1N0iSp7zQjg9Y0E61vAHacLn8mMwxoeIWkEp8GEA3pm7_MzNuQH9SW9gSmmS3tz2oAVlJwmfOLXG5umpwzADlqn7Vy6veouZZP73LFKwWgmVgKDDy9w6e34P8pt4YjKBe_adVELooJNRGw7aml9g6B9PuLBOITdfGbtiYrNSFoakgkzfF8g8qPOXoxHyapSnCSL65gjDrqFSmQSIGIMWjaAt8V4OC_fZOk_0oTnXwSDrLbtszFOWYCzYDe6-XrWtFwahUU5BCebG0erXT7m7Jh1V6hr08TIx2tjNvw8sKSmQNRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 457 · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjbcRtSnIUQZCdlnmg5FhIX2uWLOX2jAvpuKLDfHphEEVkuBmk3WQgT05SUd-bcXQiAG-PbabrNuVjFRMWj6k1-jXKKpn6dq6ltL1OZrbxpVM0X0iO77c3poqjsgURssSwB_wqPuAhTu0O-s2qAGdV4FHSeeqj6RAUHu__olLCu_i6R2YJSaw9FfS_liymN0wA7vheQKA3C5AalmC4LXfTJwMmwJXljtkJjGpzoix_CBOc-0DWcQMPrOdpRaLWoeISBNtud4a3qbOjVtO8q8h4vJTdgcV-iTb1gTECuFUshzQ1xO7RhV4GDJY-k3lpLW8YsgUjLZ1XupJvR40yR3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDZ9gkrlwbN3ogcGc-h0mAJlmktl3n8s05UFkcXQzfMRVPzM1hTOqimj8jFyUsyCjLVdSrdghEwAGHr3MLBPtT-KYJ5PoXv0Gp4a8FkQU02tASDudee9QxjQ1de4gzNQp1lQM77KfJvmf04izsnJOqSlDWXRqTXR5vFnr328jfs8ZNFOeBd6IpA-QJrja_bxtibEs7CDB_Ppv4lZExrDqDEJzuIZqezTaR029z3eX9QTEOjg_t1fvEdT_8pbN7WXXW3od-o5_sFXtheyGaflry5tyjHyxKlkH0AiHKINWaVLxfkGtpUkK4cycSThTGuyH0a4m28T0wFxUYXfx4LeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwtjMsch1ufA4HetBnHAJ2I2erjg8SNet83wjyhxdvEK84F7ELr4v26mBCEZfc_oIX5HH6VsKtaSQZnNK2B-rcCZYelXrk2KOmfYmvmLRz_Zxc3qLYumXLnvo1gK0JK1iwe3NbTq9BOsWl04w471hjswLqY-bj7ELhp3iyikPBfF1HmCoxEApN-_QyTut9ZSO38uKaiDRYTkc8-L5tTgF89jiArHdr89RMtPIblrZQwWS3NWMpyh42rr_U_6i6hyzrSNGrTu4OuACl59xMD6xAUf3lTDT0_UnjI4z6vvZ1VgrBLLBCVq6dGGZS6T1r2iMlRU4xtz9X90oRLx6OzALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO48vIeDxHM1nQt_NHa9WdjnITW-IaBFNn-AqvsMH4oOjU5u5ZRIC58a7URUCoy6g_oJiLLRTznswg2I5OvgbsDUExZSDsBO4IYMU_Hv1qg1LrMAv0ojJ-EqQvNbBgjY9oPRwFBIgpx7O3UO5-14mkU4r19_RmbfEOSySeF92SjAZkppaUitdNyD1aI100i4Ubd6qECnF1vX-WKabZF7PjoRM9o6n2LjFOphXXXvQyKaDJQiSZDNBYurzBq5qHwMLRHmnE2UPejzJm48clI7a6ckHfVilHZWkuRdSMhJ-TjFuguiS0X2uAza0x3Ah9fiIKU5qWWyjY0U2WPPZV92kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGre-FFffyY6HEz8-7It02g8qwFexCv_siPvt_lK9q4g0ipVpEFrOOme9a3ShmKf7Ma05dQ9SdcI1flkK583FjIPVZgRx7rPk-N6w-EZW7M3WvRkVzB37B5qLKY6Jw83tSHiivKDR3k5w-055e22yur-be3Fpovm9OXSyzC8bJnbEh7nnnWmNHKC1em_LudEy5FPcyirtag6gglmb81sBSV8fUUi3Zbh9AKN3Got-dXPLjg9aKkUhAkY8dTj2v8ykryakNhY0kS3Uia9y2qtEYGNlqBR5xOOuhccr_nHQeIl8k6FXfDZyt-OR9dsVeGgjJuXNjoVydNYky8RQ5vNNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=LFE69C_Auaj0PSfZNzp-un3IzBXsMO4M3mzw8bF43wZ8QVs4WJlUC77xFTQ8gNPRow9MuBggICNVGmoLGpRAvlMUj1DigAytC2bwSX_NjxJCS8RtoqO90XZ10Qjatn17PybQaZxwlJvKy22rFNzmvHXHe_n8qoUqPsFgTcWGw-p9JWgqbaSUl7F1S-yPJeBl-vtHLhr5xX-xJWnqCIZjDfWvS83Csr99RtLBYqf_7yYVfLt9GoKxmWyo085iHuyvd3--tokmjqVh3gwtEpBS0CVHdfGYY4bMxHePN-1WmGJmSshiOIy8EyTowerwzlhRwlN-HNQRJ7Dx6UUQPcc8VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=LFE69C_Auaj0PSfZNzp-un3IzBXsMO4M3mzw8bF43wZ8QVs4WJlUC77xFTQ8gNPRow9MuBggICNVGmoLGpRAvlMUj1DigAytC2bwSX_NjxJCS8RtoqO90XZ10Qjatn17PybQaZxwlJvKy22rFNzmvHXHe_n8qoUqPsFgTcWGw-p9JWgqbaSUl7F1S-yPJeBl-vtHLhr5xX-xJWnqCIZjDfWvS83Csr99RtLBYqf_7yYVfLt9GoKxmWyo085iHuyvd3--tokmjqVh3gwtEpBS0CVHdfGYY4bMxHePN-1WmGJmSshiOIy8EyTowerwzlhRwlN-HNQRJ7Dx6UUQPcc8VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22351">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPDvu5rblTQyljMbo9hnGPdLD9weTvUBWoRXaEh4_xMXYecPgIIPGP5NDl3tTV6oxNl5b5TRXOBL_UWkX5Ru9TmW4NDtDzcK1QEv7A6GGpuDkzm5YuC9nqGSeOCEpi4chBXycq9QzP5sUXcBsUieTmtXFHtEEZ_OwgMMssLZdMprKEAhKR2ldYya81zLAzyGAR9Zi4B-beobs6OYmNbn7HKTscBXXdVwV7VCBE7kba0--X4z0UlEa4gIM0raTnbyfPriUhXAfOVsDMYNdEouwq6ECXUFqB5Du1B1XresofPXYmYiNIN0CYqy9QExE7jyESSao5DR8JDTgNzGh4TuGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تاحالابدون واریزی‌روی‌فوتبالها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g6
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22351" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGyuqKJyYz0W6VtwXAMhgyWJncdL3AtBLpeA95ylnc7uOb6Hmas8DlP2vjm1qidIi8VPf0uxRKInAwkSnGqlIvd_KJxwfkvGneqYvjmgfMOEMnBEPfif0k10ArjY943fidFPpHp8twjt3BXbMWXtqh0qifWipWRkaSeLxPs_Pi9SHbV_Wm4PODwKx14OBRrtfIDQcFYph5v0LML-gMH8oA4ylBWSA1YK-xI09jBQTyNsYScz2bTEnWDGSoy1unGbKyGAju3OKH3WnvPrb5AaNE_bX5aXkyfa6bMEY4XJs5A82J4lsqzIfnoBs6x6cNiYirOm5mvQ8pcS_jqyOp28VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt2JHXTTsDq61iTwnFHi43kK1g-p4jDmagEufJT7asW-Mi_qTGtHwjBl-tMKa2ERuEQQMKVvSto8lz2jAvsMwrovcTSQiiik2-1KLhEAg1XOvp271SNQ0uPMSMByiYoIaFIFQxdC2-Ba7gFbhA4blqGvw7H6boM9qEjyaplDOT3SaOieP7JODuMT88sHRBsclE9CLJTMpbmE_ez4z2yeFQWS7mfCu_Rn0ruVB0gbcMjU3LP0fVwUNwStsdXe3twLER5fHkfS_hQcOeJgfkSwd7w6YBpJEXoPOpgDeKxg-XDUw9cuTKZSC2XCkKyZ2gi9eeqg4SCa_g0hpJK-BTd7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=JoW2_AfTlFZOevBwXY_23Qhc-d_tkCYkPxrBGR7YNGSspKUmpLoaCt-YRdXi9f_jjRWzao9r1_PXYEeCt0mIj25i_r43wFRKdTkp-kGolKSlrO71-LjLjnr77vKETkdmE4jQn2tjhmZEI4PY4vB3e1dxnF4L60kEo3mWMgcVc9tYqxjNO5anB1ogG2G7ijMRIJIerksjgon85N9TYOdFK-x-tt_R_gC2XIQFydBLRuuo18OMfdiLRaZ1B80lQPq5IjRXbrEOi4RmKrrMI2RAL7OKtLRKciguQgYjGefKEUP7rQGMrDP-nGTIsRSaCx3x4bckLLKmsAg-EuXLIXhbKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=JoW2_AfTlFZOevBwXY_23Qhc-d_tkCYkPxrBGR7YNGSspKUmpLoaCt-YRdXi9f_jjRWzao9r1_PXYEeCt0mIj25i_r43wFRKdTkp-kGolKSlrO71-LjLjnr77vKETkdmE4jQn2tjhmZEI4PY4vB3e1dxnF4L60kEo3mWMgcVc9tYqxjNO5anB1ogG2G7ijMRIJIerksjgon85N9TYOdFK-x-tt_R_gC2XIQFydBLRuuo18OMfdiLRaZ1B80lQPq5IjRXbrEOi4RmKrrMI2RAL7OKtLRKciguQgYjGefKEUP7rQGMrDP-nGTIsRSaCx3x4bckLLKmsAg-EuXLIXhbKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxlhxWec4vikmYtDbIXItRHSiz_V0Z5cmEqaSJb-jaHg9UIglVJX5vUv-9eF9-PFVIBynzImyDAyespiOMyuw9czq21TCBlAvCijCoT6ATlV8GiL-NnXme0wbzS2sjQCY__7O1yD1fOG7rETUbFUic4Fe_PUHztzvEnDbVu7m6DJuWgtghAmR9y6qCFslhBU7xmAhG_GzRrhMakv7Bpi_tijKzwqqr5TdSizko7Xc6pLyTfBGHh_73-bC9ewLvkYDTyrGFBk1oBRz4hUjzfqiE5_xrgcVvkKW2DGQrrwkblCYyh8Ax6IMAvlEsg_Gx0ztwzZlP5VEvvQ4YgAQE6W9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFH1yJW0WXMeCWizC5LHbFHNVYyzYn3IZ-ED18r5lU4U10jzfAyEoIGgDnACogi72mgkNx5sV_y3_vTFQ25abGR7C-pVSfzo1RbYGlufvQHV-V1fiFM87pygqQywj2e9lgDAXUU6HpacFFxK7wcUGPH_I45h-mJWUssNNZBDVvbS1F4JEJk0Kd_o9iQFfs4Imn2Os_YGJD8vAj7leU94ZaEPleGlv5qF0Cp_ByvM6_IOh49nOCxDHqfTWpKVd1VdOCJFXGEH_oVdcZYJ4dXRE-XBY21uD7MXcLLbQT5_tyGTak1U-7M5R_agr4X3ONjYU4dLRKNX0VeNu1khcOlR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWBmPe_d4xPyR9oYyMcTBQwdqmszxRcMuoDI-ZSh_YWb7xU4KoNgdEGxBhSakNjRhtEIhqGP0ouHb8bbkQIkgMD-Pq9HVggh5FqlR8bmv4nW4gpaHb5_HiAEfQEjudEOFehknNSHm5kpFjyRa2TClxVAuLjFoHMyRWJe7JM_DwaiCfIdG-vhatD_Su7d6Ysu8L70crwCYeA3BPg7eTqi7WeimMXrxxpnmWoWHb-J9J29jFE5hMeIFicPjkw_AqV9taqfmkdM1bRiv9ym66BC7bT7pPswOxbBE6mejfS2GHokCBDJihg1mVqS3Un787Y19WcNba9BD7osdKoij7DFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXCXlT7yrbtl8LURdqvUcMzlv_cmvmFZiiyBhVbRc0LfM1NPH8LKUKyZj8KcVGxOyPGRG1CcTIwWUB7EI95Zam0rEDXqvvRimCf7bXYNVXkUFExcscncuy7A8hKfOTSAIvYju1UTcO3u7QEu8jPgGUZUiOn6HAngp-D0Q4vtT7Ssq0zN7BCKnLKFr5QhFVQfJ-iVT0-fmPHeqERD03j_-1yxahO1LK410RhXPOvpym6aq1RVYjpQ-pPBnbspE-NyyinZhv4wskO6FcUGljeSRFgY2vPSsLUCNF3AyRfwz5vg88mCoZOv4MmwYV4rd1EZqOUWELIEYHG27FU3-qMyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsFjPn8wZNPaVob0Ni1PoAaeCceN4Km00bGrGimnnFvpUFIJAMG5FknJD074vFFVBG5tdUYMVQakX6jOfmvtnHdhvpRIa6IFjppNOcArdoH6pyWn1AiO_5zL7U0ynnsJNNYwp4sq9d8Cw8bhcRnqnSwuFzL3I4xCgQKFsqu1Zbn3HKZNqYnM3dQYWcBg2wo-s3VXCQh2gFatKWKpFGhTFUZKH_naLMmF_f97Qy_5JmiKDciOkGHXSJ8RIHpt2WcPm2QBsiSJKAfqbwkIjrsFerNB7GAc0piAs6ofAxtChFZEbkJhooogiJ4gT9eL_8fLlXDoZm071zfqiqWFbg0kBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5e8FPaiqfWko3OzqohdJi6xarX1ALmKk00RoN4NUoHmd1K3tTy4CCGVP8jiRl2TFTw8e1iiRzisTs8QfSy1TPTpxYG736XekY7COaYV5fvnd1sWPvlelORDrIGb9QaFZjsmkDHejsuDSo2-18L_RuY6ZQkG4s2keY-X9ZsjG52Y07Kc2e6XDq5ze8ybJux8tUjOIvduiTNKJ1Ra16qL86QArBVF8v864yXrxMr6KDG6MBdahXy3iVcRJM3Sc8aYiTCLHF2Rc6DeU6yVCGFNEUM6_N8xxIUoGAcyQQJeVVw4TazkLR5HziKAPQZvJLwlcaJ9QKhMLtQZ3spe3K_gjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsBJEBq9kXYou_GdvGEokKh2cjeZWO14SqJ-zryTZxIDmJljE0-O1MwzTpHVe995mz_Xe4d7Il9YKW1sv8FOrEdbVN82M3S1vx6pEZyK5U2g5Isa8nQ5C-K5dXpUYbBDbC1iU6uRbuPkGuy6RYCcZqMafpBq7pPu-KE5UQyg3LZoqGLL_fmlOTgjBItpd_IXStkKfhsIFcC8UjDOWYKKjVU2FwdpzSTJR2jlCm3HQomQn7jl1_8AY1YHwmejZ2F1iOJ8ksSkPNkAK_o6qAqNbPGgubjyzhHCjFiIeA6y_oQuT6o9QiOEaKTa4G2nLa7f74ceUvAqTO3k1WMJT4EQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkT4RhI4x1O1Iq7KBrO6BJEjmqhFkPuZrRzKk5ekNGSHaJTXQ_kFgIRi92Qoma7al_RgoLVL4WfcMxE3PqUeXP4pUHDK1frNi3g-bmKiyyezyMzxrl8ulob6UDXdMXcjbxVEZe6sd_SaBC_XCCoQg22X6UQV9pn9-UVaksUjrTkatX9vecDLz5vBbRJoQY6xVX5QHwufJVJLiWanqp2caZqsRDGsvJgDPgbecDzVmRUhd1d-a2ScvXq0weLBT_MRB6eZ-FIRl4HLT_XqmX8NlbOKXH2aeJ0erejAKjPv5AvY-u_ag7WbCUmKcckYH-ab16WryjEtPwJBvMhoBP9yNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljRElpNqKVtiH3LlhNdz4M2uGz_uGQQxXz_zV_FubXynIxhQ5NTmUoERJXyzocsmoaKGDcDUWgdpZA4kupcIHhnFJpEo7_8HEFKfffB0XTo1vjE21unOHX6pkMJjs-nTl6KbcGXlcMxlEt2ydX6Vt7gb0rw4LqxHVRg7UdhK3Pt6t3GlD_z8Tfj1nc4IhxhKRRNWf7qxeI-2ParPgvAcVs-Tzlp7LIeTX0tygOiESXlp61exoUJtgU2eUTuW5NCe6ZvkhJJm_QjZcpkBLZpftuppgnadqELuvl5l1KDnTY-wCzSZkirvYSniFT_mJ7NODxJtQvRIJr_jM5TleE2nGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlvUWY96dGhwyxHUXyL7H95kmaBc8JGLjBiYm82swTjJDtk6c6l7gZWSdDd6sIHWAiKxHz7pkEGV-JF7jd75TMDAEyutRSr0xgVijKi3dSfwPTKs0sTpJ0hZnMPi-EQQiQtpNCXzF0BYanYXx7wOH6uGNj593nHC7XBQaWAyEM9TXbJ7hDvka28FeCyAVeQccd-tBE8p-NJSsUiRJpdAJegKyoEy6_yWduvsjhuSRWyxIxLdiNyAcJ6dzVdKvtTo_pEoLxEv6BN7aHIEp-QhqrTv9Ye7p3HU2pCeJb12Chk6pUfXsMuhBZf6vngy4wXZwcZP5TPXJXT1HbYQF4R_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22337">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4zedjt3e15udnZJXO4iVMyVmmTdhqiXGLF-FSmwvgCK0hGgqp3LZT-HelLjSTYB6FUd_0f_SBcWQZXInq1FCHzzM4bNw7LWzkF6kZB-tq5juYVsYaXmKeMK0f8egd-iVlAL0QA3PfPIqzuyws7J7eE7X6v7ueQi-hbO2xzB40BAJ6zqijVZHv196ltXYGPLKj0Ya3KR_P9dleu-nhhvWnubMdutQqt5vnY_m08RwDY0KnvHmYCdKfzGvQQkjFA-f6INIPbqk_gwvpZtM_kZU1gbEkQnYkEdbMsvQEi5oc6S5kVeQC_AezMgSvuyinPiQrTZx5dqXiOiutPyXA2ekg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان‌جایزه‌بده نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r6
📱
@winro_io</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/22337" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=Kbp9hojtQ3Q1FnPX-V1AYDVexIl2Mbs1pTr1ZwSqeo0FWDhnWD4diGI2ci2jDQbwzfsmxkhbMJ4iPn4en1TQqu_JwhA5tEBG_YRwBsOO9hku-9xNorHtG6WfAji8EwrAXqT2UdN9RYFxWbcpk0rWDT3_HEIGAhhMKQ49TSWqEgFm4ZdFY0f6g49n_xqbjvjMJNHJDCB5tR-E1K4TF-ZgtMf7eE5scn1BcMKI-rseR-wSzSMWa2vCfD9N8f_cM4XoC5uza7Wiplx-N5mni2V-eDLxkYW57W6r8A1keMEPH-5JqKnchzEGj7isvtC1cmL5TFXIHU_Xs0JJzJEep844pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=Kbp9hojtQ3Q1FnPX-V1AYDVexIl2Mbs1pTr1ZwSqeo0FWDhnWD4diGI2ci2jDQbwzfsmxkhbMJ4iPn4en1TQqu_JwhA5tEBG_YRwBsOO9hku-9xNorHtG6WfAji8EwrAXqT2UdN9RYFxWbcpk0rWDT3_HEIGAhhMKQ49TSWqEgFm4ZdFY0f6g49n_xqbjvjMJNHJDCB5tR-E1K4TF-ZgtMf7eE5scn1BcMKI-rseR-wSzSMWa2vCfD9N8f_cM4XoC5uza7Wiplx-N5mni2V-eDLxkYW57W6r8A1keMEPH-5JqKnchzEGj7isvtC1cmL5TFXIHU_Xs0JJzJEep844pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufRAlUGFue7NsNLryU0kFg4WbcLq_CuB0ge0KzwANkUXH_9vM4kJt5gAfKgeBNIn9Y4n7XP9wsbO20htQLGNAstSzo3jqwStORVolhWVeumjhamG3RGanqegnAnJjewIQNPtC6MKitZwmsVoMeiTvm0RRpjoF7N_tSHH4NqXSAWsrR5k26GK3bhYor6FHQuUrT-MqbQqcg0faA0T74cfoYeZGaxw9kmc2qIWrlAks9PmWbsUMTIMKvTqzW_Ysr5yB7yIsHEwuOWgQlL8ftNYq500RhLhv9FscTRoh4-R6M5R1ztObSNS9T4M7Pj3L0Bf07HLekiVDStrecbbNOVNLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNRUQb-q8lX6puiD-2b2Dff2k8CPNv7MoSrJOS_C3-fZ0KDZvEp7cSZMJog-W8phbO9VmaApSTQtFcys3wRWf6ajjG7ntJo1k1E2drbD5G_UnCPSyRPMGvY6A6W44qtuuwwo49s7ExgeTTVIxkh6n-X9Db14W9orDPYtyrSFZRd5v3zQg6qU1TONMfxmqvGophYLo-yDZJbi2K1wAfVcC4swm0r_MfiTgxUPj_y4KsfhvPP-8SacXuuOJOuj96jCSb4ysvlSCia3_05OpcB1VLDaUmTIDN5cxVeKz9zOZ0ner9fWkGJqovEwAaikWD1YZoIBrx7D_dLdwx6C_TQAFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePh49sNI9ozXd7EDAW2gy906hJDaYgLUtL72KATSAVsIbPYTZ5dIZbNmXMvwpS6XP775l70wg42nFbCOu_a9hpXUK7karyibpzBoNMNiZMhlERqke1s1rEsBfAXn50c9D6wzAlyvV7itvjDto_Ak47lQuTJz_OO__pDv42fLsmW3sFcRFvMhMT-9nE9oXIgmRCexXtGJttcmkrDgcpoj1sZh9YfbvjQJ-HRWZdKGs5yPCMVnGLbPPZ7ZD9Zh2_eqTAIZdoce4ZvpOH1ER-x_Ji80y1XGTDzAay00I-oYToZZskvprTtUHGUp6Pp44KN1EdYBdQPFgXUvinrPPqBuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt0SQUQzNkwp_i4OO_hwU137688EL4zcmpvJj_PVfvBHM9jqO-DRLdMESmFB8SCNPykj0aB141a7Oc4diejNkYQmrMBm9ZODkOBYA9S1k7kCBBvcFLdrQ3sl7VxXpM5XzSXiKHPcKk1R65QXP94KjLqOirh0kQECxedtk2aEisO703xNrjkwNNgibqqopndXT6MjDCPj6Q9Jc8VBSr0Y1d65Dx-V4uSk4w3qJkXejuW4LG_Bn4l11QIXZC3DAAQmJQeEXGElsYfEnkPaTiLFLu3NfMMXOHgIMU57jSdKjy7eKD-1_ej1D3nHkSpRPfWGWCMiYdTaUrBnNY_30mhjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNjKhLb8N6L_5mRy7XWtIEvteragylzRoA9X4Nb2xyMXpeZsy7mQQJM8irlwymxCtXcAAuKJLU0owS8NllYdpX8wjnMh_jdODKSXX0o8ejh0G_2Jnb_w7Km_T6voBDXNp_BoMGLPR9qm4Z_p_pob3QQn7sFLw3pnBTXJHjIBpR3RY9ei_wnpVfBSv8Pvk4HGfuN1CHf1sbISNcqwYftdAD0zV5NxVY4fkhum4D1NUnCEXLAQbmKrqZRYveDxVXfGJuMnyqUMYrGmjGNIcRPDaYIZ8bGVdmC1-F2dzyRnWO_AMjOkcrc3xWBvANPT5c0ho02FdLzzyxZiVOekFmGDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YA2n_blVDDYRvabsnYWeGq7_ZIC8BHqptH3sBiaNBFXMjW6Nvhj1yXAtSgeadQ2sQjihIhJvhVKDVT6G8VUKEbce1joBXGE3yH1sh8mZCjWlAbvF6ePsF3h0VAdncYjgo7ydTEb0IVs7_efZBcb8LEraBSAhGh1-RzzV6yKHX5vkBBLCZzqZyXMqtaMCZRZrx5qo25nHQqqmsPcLEwsWSI-gGfEqEVfV2RaBD7T2UnA48Zk-cpJd_iysermxIuYH2WUZSgGQxDhQ8CWj6GYkNxNiJ9C2lfMc79ut6Z-X2mgc47ebeVMSFPvBJl66fcpJJQfvaomXoq9DTU2CNU6xNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI8VO-uDfQy_cUK4b15H66327WWk3FI8_9ydFJHkYvp1T-pS0oNM3wfS6BGqOMBMxOHt5MUFIQ9nlX0ULX9HefvDI0fx74FZI0Kv7iCnzCpX_kOGB3hIjd_eSBNM7oA1WyQ9-EDPMsR5vdl0Jvkw7WoSa-Qc1PLsTP6dRq0Dfr_5jfRSrtRNhyWsW4HH-syySDBffD84dLn_vvZx8VyQVPBL0CyF_Rm6e4wxKpxTVAAvKdGabriqt2TENEZW_aGP8ul-wC937OOYNEJG6gderBhxp8f3SyRJuXY0YmpgDTwx3NrAvWfn3OMq0ht8dO9c9cPclU-lkhVotesfzrDq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=r-zgWRamN6_Rl5CEtctaZxzdg8YMYfbykVRcQIt3T6yLxs6UNEBL8QDB8qCjmhCq3SMcaDp3zWfRJF4Q2XTSe1LwZI9a74Sg2usaOk9TWEJKop7FhAw4DM8m6YCbEcLGW6jReoGnj4OGwpXwxZt4tHkc2miQ2ldGprj3iULW2GLMXu7kyQH99bnG0UL_1JrXW1ZfsJ3MNReeCOPsWY1_8egnrFsOyKA2mMlit8jFJIDUcclgIwz7SZDMd-MueEZnzLlV6gfGRtA-wpr0iEjGyoyhxGA5UbXFgD7YC5gJ4FvKHOsTV3SoGeUScllkVXJNZNuQDkEkjaYCDTtIx72PlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=r-zgWRamN6_Rl5CEtctaZxzdg8YMYfbykVRcQIt3T6yLxs6UNEBL8QDB8qCjmhCq3SMcaDp3zWfRJF4Q2XTSe1LwZI9a74Sg2usaOk9TWEJKop7FhAw4DM8m6YCbEcLGW6jReoGnj4OGwpXwxZt4tHkc2miQ2ldGprj3iULW2GLMXu7kyQH99bnG0UL_1JrXW1ZfsJ3MNReeCOPsWY1_8egnrFsOyKA2mMlit8jFJIDUcclgIwz7SZDMd-MueEZnzLlV6gfGRtA-wpr0iEjGyoyhxGA5UbXFgD7YC5gJ4FvKHOsTV3SoGeUScllkVXJNZNuQDkEkjaYCDTtIx72PlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-Lvi0oK9a9BtjOooodTp-6YrVtpuGTwFF0VYg8xoizBo_U9aeJ01l9UkC_y4LoHbzL3dMlEiRw1l_ia9D7h6HNDGSZGBU4vBYQOF-BwqwrT_vfN2YMAPlgRDOoRXOdpG6bkkwTKpntlGLFmzREzswDYJf6Rr5uF8M6ES0kFr2dQ-oeo3sOwllOF0TrB4z_cy1KMxm9CN-MYHoL9zJY46csVSIruyagtkW0qdpQoLChwgaMwGan6GGJaYdW7TMm-Ni8QvlI37cDoxJyxeVQ5KM_X-JcocmAfiEVOUsmMA_1VQjvg4C1TrpXRKVAMhkGEUsWdCX74VBdEaF-8YPzsew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFCM_bK2ilmU9upja8YSRO8nCUIpZ5g77rItH4k3Y0_Qq_M-JOocS7yqcFJDQsweUQox3WEZ48GELV4dXsIuAW79eqbIN8y-nawTAcWwU38BvBkDhW-O1QVanx5M0xxgMh74NydmCOLBVoK_dp8-4bCR3eLOAJJmM2qwxetwEUrB8UzOMDB1SkNhqWVY1wrT0Wu5PvYLl0HZy53WXc-lBLzPXgOs1RkgBqiyx08H2s1aIFX4Hz15SSOYMLGR5BmhWDS07YG7XGf5JCcUd82O7fCphJH8ej3S0TZtvUwuo2OvdQ3HgRUU4cl0OPvPNyq5D_3pm1lfWZuOViMWMKSpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=c3m0m2geUWHwYGaLdJtdX86JN6O4zxj-ANLIpMfpxuWq63gHbqYjhFpwEz4j17YClsg3n-BWBT0w0YKukhrq4Jb5tqTVECnklehj8GHcgtuWvwoFc5Tlk7Gz9wFu-lkZBSrdISGNyDlXzo4rZ4pd-aeDjSfj8TF1oAec7Sogqp67zUCEWvm2PLos3PuMiiBctwvZJ3CMBlL62wlGrht3GBT5GhdKXXZgqV0WJzZzBAMtKH76lXomxXTs7wWYta-cyiipVwhCirWm2ItFFK1fDQYysipnd0Ge1Ro7sJv0aMtV9_JKkjUjz8EK7ApPW7MXRsKvqjrtcPOTIj6qmVASrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=c3m0m2geUWHwYGaLdJtdX86JN6O4zxj-ANLIpMfpxuWq63gHbqYjhFpwEz4j17YClsg3n-BWBT0w0YKukhrq4Jb5tqTVECnklehj8GHcgtuWvwoFc5Tlk7Gz9wFu-lkZBSrdISGNyDlXzo4rZ4pd-aeDjSfj8TF1oAec7Sogqp67zUCEWvm2PLos3PuMiiBctwvZJ3CMBlL62wlGrht3GBT5GhdKXXZgqV0WJzZzBAMtKH76lXomxXTs7wWYta-cyiipVwhCirWm2ItFFK1fDQYysipnd0Ge1Ro7sJv0aMtV9_JKkjUjz8EK7ApPW7MXRsKvqjrtcPOTIj6qmVASrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIE-hu3Vwk6Irb1H8uhWSBzDiZgJxvCIIBqhgD_sbN3A-nMx1A0f-5uRwRjP4bIVHhB3Ac7WXz-oJfAt_uzIXNVyBzYj6hUxEwJbls4EiBD5IhRD4jR3HZ6ysG1NbAqbUWA19nBok3tCzMwRVUTy137RxFjxPqR34qOUKKAKmvxgXX0EGcnouzbW6zr9-JCn-3UTf5lzsOleNdOHNDKl5uAMtqH2Q7z1NkjORSaiJ-Zhykl01MuwhbCcxs3fy09vjI6I892yojpKyxANX9Okt8L7Hm_CTMdscA1k6wCrh8k5ykCSSKgEIKRR48ITDTs9XJ_andpgJJSIkLIfqfKe8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FonrUL3OplZ1Ngn2nGTY_Ssjkk6K7wFjsyPkIfY5tN1ClFJpJoqU8fEPeQmyGqhiK3f7OWfAoGoJMpxcIHIHqxO3JFvQKoORzZUTfNrKb1RxNSY8E-2HT7BGqlP-9zK4fCEh6pJUkspOQ8y8NQEyFVmyI0qrHYoCubUUYs_KcYN1h64r8O6_L1DR48e83KqI9cR0CGMtMFbTilZlIYiEPe9xXaMqBjUDaxjs9C1G1r4JrJ0aKBvL5lnAWiyaXoUxg5XGlDPhVACGLQtnnlnD66g9XXMpDl3us8kxJvw4tfpnoQvJnXdHJ8zMsCxih6--mNlJsAK92Fs2WNgLnIciyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG37jmjsiA1OeHwPI3CULWf7fStvY3ge88i7KE-AB2ccQcC3UqAZntCYH5SvC7-lr17xoTECHXRyfbSGqE0ftBLD1EGzybS-h44DSWjN6p6SenbOmmVhwKpjuA_v-yUKSSV2a6KlexRle5NQLIWkYxKyWTBxNJW_r5pqb_54DVdUGqNCcQMukbBQ2GYF4yj4NxrwpEhCkEyJS-nanj-FWkZxZRqyISvd5NQoHeDvySyTJ5NF2ExxN-EsuRGW271UlYRK5zxFpvA_a3rtxhAKbOTJpiEiMWl5Zu2RpuZDoOWUsBX1Q7LBi19c0oDf6hDz-lXBcs5DjKOLk6U9SJkBgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlPKeJ6s67JzU6TVmhFSABAZ_HWhV6_GliWIO-exeGTeaCIhEzJj53uoY_E6xZKwd5IklcH2AHiJKEm2GUUZjya5To8X11mb0-Pe7ahE5EE0cVbeHrhH8fwOc8tnFncWavYnsn2yIpL5P9WfoqH_DlNmM650h5sU80asgg4vVyfWXvc9NDS97UmN0MzjNpmUJJ-RXl008UdsUpevV-owWnNEDPxFiAP_gmmFzBXfbg914ZqtxXNipNJXhIoP7TQ7ie7reh8agFUx3sab8X9Q1gzeA4VY0LI9V0bdHv7tACZokIMRWFd14WWKmq9T_qa3THlQjhAe_gbM_V3Yqv8Wyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=hQ51KaAbcWbDEu_kwEcmNQ77SS3WSpwX7AemId1jYUTUorO5fsALCuW1nn26FaagikuDd7kuLWe0IISc47mueP2_8vJoy4NyXyiG0kbiC7Aa-hDykoam7wO6_y7KpwkmY0zttih0eTNfauHavCNycdsdx3Xd0ZI1CEStx5hiJtUbb16ZyBzvLp0En-GNlfIoY5vLkFZulHXCUkagDHhBacNMlFHTsNSAPmcpmJi6h7ZDD3ONS2BdgzWP4gJoqpGB80WAV_2PFz1DikFrIrXYwFx4oa5mRfX7edaAdOfWRupK9C0DvcID2UG_dfLHvoT5B7Q3ik6cRAAHnzpv1rZ7ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=hQ51KaAbcWbDEu_kwEcmNQ77SS3WSpwX7AemId1jYUTUorO5fsALCuW1nn26FaagikuDd7kuLWe0IISc47mueP2_8vJoy4NyXyiG0kbiC7Aa-hDykoam7wO6_y7KpwkmY0zttih0eTNfauHavCNycdsdx3Xd0ZI1CEStx5hiJtUbb16ZyBzvLp0En-GNlfIoY5vLkFZulHXCUkagDHhBacNMlFHTsNSAPmcpmJi6h7ZDD3ONS2BdgzWP4gJoqpGB80WAV_2PFz1DikFrIrXYwFx4oa5mRfX7edaAdOfWRupK9C0DvcID2UG_dfLHvoT5B7Q3ik6cRAAHnzpv1rZ7ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKe8efi-RFiEBWgaxUuZBPmOShbz8-SdBZENAirpdfaEr6nhRO3ZzJamMh7by4q7Rd_xeyANFAwyLqgtEJrW3pFPz7DUMgL77xnAzTimWR1tC8Zcx3sXG7jschIJjNVUy57ICkEisz_eh-zzobaBrNguqNuLRL0uBNYeE6jJ95sQ6JtN6y70VCmazElKZUM61HDMmLVxzcbToWN05QOxPslqWJmVhZ2gPu6CYUnBoylj-eIG7YjMviy51mttq9xQBJrugWyFLQIdXaGwonkyBvULSxbuZSwTbx6C8-D78XV-CVg3U_K_iTdQ2y5jcdg7RHvGyKN1iMW_OP0XOYKasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHhAdj8JKEU4XL42snhV5sgYQPAG4zwiAP_BPT79Zsa9UYiWpgHPiEfL_UMl6mioooOdjgGLErqkEUZrKo9faTq7glkJ01jCmP5QUheog_p4S_afuBi30cmQv542ppR30bk1G1Tht0E8Wn6TOtmObXRGvp8qH3gj4z8mABi3uMZnn263LwNJk2tJr-stRqt7YzsP2OUAYQ1wTxbvFTjmfWJGwuBEbS9aFWtZ6saSvx382dkYquKiRyQdFzgQudt4_LPEv0GvpKq1bwqa6F9gEM6-VIgRO2dmPpWk9k51WwHU_Nb0YFrxIJDZdkun6VxpGVok7_yJ7znsUwU39em8bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT9X6ueLaXxCce6vLshRBJ_8YcbfFVo_73gAMrkz6F3jlfSuNpx_yXjXAZo_jwyxD8PdEClqdEEurDb3DKu5YCgltE0i6WwXO8H1OpJoH0h4BEhFBNcomnX28enDaOdjZ7apo5FpwTG8Z7d5lgtnT3EcuLhsq9xO_FCUeYF0-jfdN5NTxEtiE3NyXglLI8M1oX75S39RR8MUiV2u9w7zwTYxcd26K1qii7qr6neOn1jfEUlU0dI7EBe95QTaBu94INImDPeE3-rBZwFuP_3drw7E6YJsvoxvs4SkSkgfXFEdGoBlci74UK1wGKOdQRusJJMmgY93mmFlnxMT8fB7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-y9QmtOFOxxEqqc8S0_V1oKgWEflMZbzz_PlldF80FPtYOsJGEBVQwT3uAEb0JiU7kIggYVAZbwNMsRzOQZ6I0ldFXIopb3e9cBcz9tJep_ofCjTprCoErAmREA9Qtuz54NayA6av4TSoXtGsPRMoKpUHmbq5Z_3Tx1ejvx9Cea7DfNYqtU5uFsjdgUDcBth-P2d9FHmOd9oWJk5U-jbokC2xCg5oFHycHim5Rq9GHduK7sOKetD31W1Kcp3A3KSTWpTQ4pokupp6b9uld0NhQaGKgt2s5r405U0YFv04MxNpkJcNWJzBXVDQGlh0-fU7lknQiQORbIX5u19MPNaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bsd9o6_KtBoCiCqoTztVmxLZg18iiK8VYQ7TxkZhVN4pm5NQLZN3DpaQGKORJZZEFd-vuK4ChfUpfMiNl5fpCw42o4GC_NDw1fcsazpBhbTuFEVxn25wAd-bVoPKVts3t893L0cXtnxZwkh80bnG95gkUD2ZNvC1PFPEjssrJesGPxeRr0u0lKYf8QE347KnnAF7yoitTEEn-1vTmM3p6qIRF-ZJfNdlzuWsP0FqyZNYc9fcTPcaG1AbFb1waj9iAuqjTlgeUJkYJICWrj9oxgHgi-pz6NoK3jEd5FVV_pebcHBmkRb3XUoGtoAQ-Vtb3I9t-YO5ZAT68oeoFbE6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiMJvPagUc68QIv0aEMXPb96Zt-NpnSchJoAbfosde7HrejR4zIjy-OSICPCQPu94SBXv9cQMiyDpplMVktf7LNP65ShzAoVsbjKwgya0pI0xQTJKyNgZ1OZr17SNmZk26EgmuwhHaVvmHdqa-DUiX0ywEt-7Dc10XkM6jnfI9lwuMo6Moq9mZ3OnE1Y30SQqYBNPjPmpD-8bkJa0iNIH-sGRPD3kafD5bRWz3vg9eeZhkxJFnKqdNELI1WinekzBbhddQGXR68XA4IxEJb6ZkYB5ngK4Sm5l2cP_d06TdZUqhpKKmJXmGnygR3QoiBpHJnriTSX2YQ7jh_tC0mB9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛نماینده‌خولیان‌آلوارز: اگه باشگاه بارسا با اتلتیکو برسررقم آزادسازی خولیان آلوارز به توافق برسد این انتقال در تابستون پیش‌رو انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/22314" target="_blank">📅 01:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC5-jVIJWsHlTfBcSQh2MxrUPjU2PG2-uwm-9FRx9ADerk6n4WNi19FLzYunLOtH8peEQ7aFkppbH_051swPK32c5Va6w6Go-Uoks2vMxac5VwckCUh5JdFiysRzn7UxlBRS8hAVYfrLj9cI4mB1Si9_d0xb6ObTrY9ThfetxxM14nGWYxejTv63euRWMSbCAkVnsTo8k1e7iVFhtcfLMI2t_7rlSa8_1dddhHIRGAnP8aHxp1gdv04wJuN893AXKpgUs4Eu6RsHcLeDhUJ6YDns_ixyyGighJNeLP_4Aed_DoflNcF_HvSjFsgeOqViycfOCRilA_4BbiaQ0NOU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ طبق گفته رسانه‌های نزدیک به حکومت؛ اینترنت بین الملل مردم ایران تا ساعات آینده وصل خواهد شد. انشالله این آخرین باری خواهد بود که اینترنت مردم عزیز ایران قطع خواهد شد.
❤️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/22313" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-CbO2dsaWuXVZhivMfaYEGRe6OpWAjcbD2FQGTafrObIor0Cg94odVg_ssYDhwP5lWZ1nFOnBfSsNU4n0cUdRFngD-Q-OvdGcuif1BPR1PZPJK_vvQi7KUpBKpUwS0kBVHFgplhnYFCBNQ86elGAVP7zIcjnFD_px6lj1TzmFpoxeZl_eWPbDhFDI_WrWw639btDF5dBqhHg-kqkgZ7BNT7Re54HTp6vehNFO33knbnWj-74iHS77cbU201LL5IMauZ0JofMd7N3nPY9JMuPxLRE2PtDZT2NoOkCuZBd8T68_cDNq0gJwmfj1tqyOXeGOfQpTaQeob7L3cY1XeFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1ukwN7wjAjMrgw44mdzXg-wFCjJVygQmP74A0E1B11WBFsn0kLrC9I5aGOqFrNUL8KCTYk6GtupoQNKtAu6XOWdplALATGUqEdg0UW4rkWEj5WY0-OmdkJbsHoL9Xobo9cCkz2_okGmly1ShRfOI1HLLIw5CN-WeLO7agCIhyAnuw0Wr0FkxJkYj2-8D0F3KN-DDrGgVaCMtStBADBMAGVeEARGmWbv2mMvZa1et0VunzuvLsWcrRjN0zfK6eaqOPJw_XAAX68FGwOomW2QB5NHV0S8U_TV57DMR5rSyrLh9l-FaFPduuXIS-xCbXqU0z9XynmDwnLyu6VFP5WTUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2dpqqpwEqrdzUG1Ee_n4lOhUBkt9SitHrIEAH_lOLO-YopWeBdFtQNptTve0x0IG_7I8sho0fW2PoDSKcwNh7g_47j48oDe3MzcDXQTe-htk7goIp80wSzM8z-fFANe2QtRDAXkGrCTUTzRTvoBjnsIobMIWREtIDByMVfJ6SOjdPFew74rytEGZO1k5DeTGP2Ux7RIJUNWDWiaPIf_vc5yoDvon-VEQNa2hrnQCy5g6kiFCwLAT0-tWJCqhxg3MYMZCYkIzoTqUMYpChI9GN-Xi3QCu-hmAgLROYKWo5VW-ILzGtjc6Y6ampHYP7CzC8paN5US5hvAn2EHhQZpkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9qAqXXTBz7725x1Yhtqh_RNv9wg7uehXY31sg-cmQe6nJZ323tlUi1NW8ZsCvlNfNwTuuwAlYXOAW7meOwp_dZFWTTj2lVTVtRLSNAU-wIPrKOrkQUPbFNM1WOdTVuswRo3pykxTemAlHQAqDJdJ-0JbM1grFHUpIE-DwcS2wA-f9PW-cSfW1fQVXwnNtZb5mmSmUg8Vv7n_UFHBnCqM9-SxBWAVpfXS9Xkk4odA5iEuOVVOd1ofWqcVEvdIBYgN_sJ5O1DJ0NohKuwHJopDhIVx2x8kOUBoKRClS4LDHRQ3SikVe9t84tC4fm4qYYxL6t9a655SSY4xO5u8SoT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJSQtGaiXt0wmVuoVw7BaO2WBssw56zRRt_BjqBS1st_ABleYF5vWaTn6u9v_rcI-SIR157rZ4-8DgFMpF2Oz6II5Cf6jIOu3S6Nco_yZsb7dFHdsA3ySH-ZOPkcFHiTx1eDt9qY0dxomYUCMaXGUh1ywdTRLLcV9F6p4nP9Uq0-MepKAAVKYQ3EFphmXjTW_BxSYv5PzR1gN9R5xfOOvAHKbKh-sEH7eky1HSkJwpkIE4qEfsliw36nbfBscwBlXbyedB65EGisQ5nAZoY-K5Tj7xOZ2l3wv761GbZxi7qdXL0k4dN75FWQ_3wB2Smrs2TUb7PL5i-qHqsk1BQasA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pl5ShM0OKtbPkhSx_AoAceLgaCLp5EKmXMdrFedh9W_m0uAFMoAvomUnaRgPCE_Kz5PtIAgxiJ27KPLRyezqPJeHlmQQF6VXcPwEKWfosfN3wAPzIX-i2i66xO5UyKcv97SBcEj19C0onyyUbzl-dUCevORdxlhj5kSxSCkR8sXAPGFzccVjiwxPLE1pAPRqLik-ocDzdlQuPrnVxOeqpIVTONsD5MtrjT0CSDd08Hezskvrmupsa8PEIBfZzh4wFhUppmCzoW6_t6kW6Z2iRfNxjnIx83Qq3cun0bjzzDPRqvY-2KCDA8wT2c0OEHn8caXUVJJm2fk0AV1Gvw6ODw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dh10pBD_flBz6rs2C_AK0J1NDr43VV9zQM-0xfzzP8VG6CjFAlj3Jteymu30l_0z7mNBjtPOF0epvekUep2o50G9yX2QjFoBYQFgUTg1hiuX4o86qHaQ-CCt1Bllq1-WwOS_Gw2w5MXO8irTctWyENu_zrgUkCngsTuzzFqrnDoOMqC9whNoKaZhB04bw4lABI4IS6ZbK0sIpZx-hOiqOrc-XgaLI-tNCuFmkLiB05yIsLCQCHwaKu1_5_372O85SQMAZVHvpFep9MP_4RQYBaIAb61mQKu65qgvR_4eo1BExfBiAFYakt_6mGi0PJndbkS5SnhiEybnEOzb-jxvvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naP7IErYJFYtJIfrQVrAvXGnT7mZceuxngXyO74XrD5NuqOorLWLoe1Mdrs9HuI5KMTkqZ1cOIOCzYaiR2dC0tcxMxIJmMTVwfvQ0mUbsfXitqYtgXkR0wumYwCQa-eUpBbjejuiSbdgKCcllEkAVjB03in9aa0VGiyiGy7Vsen_hc5GuxZysPTkQFNZU3A5Z4PJHsMUh6Vtnw07OHm_jYJAak5QxtLL5b3IVxQKveNqY9cSSIDXf1_kbioYkL0f0nkrYd7tIRO96kj9V0-xkAmlbsFekRuABzhgj_HWwZ1f6hf-9FCLYU4GX4LDyjQj2jPw2lHF6PmLcvCe4kQH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjIrZl0_D9kxN26vqGgwuysNPtuuPtICRq_rltK8wRQAE6nvpvFCwU-emCCrgPING2pJjPM5nWRgAR1lFP7e77zCCvjGTfb15jq7mbqfVbYYUwpkr1NMhEXO0p9wMMPvlznpTgu8TC6km3eVxYbLX9stS7skSDXtuaZXmp4rTPG1SlEAnx1mNkyhwmdYtUsoMVWCfLBYYn4Nl5qKvW4YInPYSvxUtLwgKKdENaAPzHzwCi51rd5W_W8qYMsAb3kvc5NJLVowI8MUBgc5ftsSrpJhAj_N-Mp94Wut8ncMeoiObMRDUEoVwWR-E-U0hOddAuSzWL7TFEaFi0dDnCN7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVALu2LRHE6EQKDz7G0dUl8NADdg2opHr_dz4uw9wIEhAZ8VaHzNI2A9DPJ02WhPxBTgaC2T83K5khAJDmhu3ZXyrAraCIvEq8vDBsZnmJE8Pdwil5AufM4uFakenmZlUSApsjlAwRpuOLZHlo5L-jtzi-yMp9_UcZZtwRBmAWSHzI5AGCoMtRTGb_FV0YAwCbCosvLSUGoXF3c9MOP74FkNUDdAPmWEYjDoOeL6bhpT75t_7FYxFzTiavHZmxe_RtSJAj26Pm9R6wXw1uSSmTpR37hUAMIcseYglYxbxNOmKH5gM3i5MH9c6nW3EhDnoRpmDOU9A_onujS9k5sO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDMlpKJc0UXVJOlhS7RX-YvUPMdpAniXJRDsqhT0Zz8rdx4Sk4Lerblmy6DNfEqaIQ5AWv0pOtjEMv-COiOKfg1iDPpGTES6bGz3b4g0ojOcMlPSmA23nvkl5Q3LVmzN9CXuczeDwT_shKZ5OJtglOXUPgryJhqqolwVponmhnUg8t5PmgDYjMAHmCOibW6Nzd95afBh2fUSmpee7DYxJGpHyZDd_LvQIh5VejjUXiIpkWmLrPboKZMpLHXG4rwf1w5tXrsQmh7kp7F-7oWWUf3x_yzY2E0YkTdKHyb2_Iv3DGaPgtQjek1sOUan-EUZO-pXVaYUUA2WB8XxyIuvBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGHo7rwu7zLXmJOIORFCrGKSEFwBrHlzV-kcezworA2YVyPpZNmVmXUzhxpSLZq3cBqMElvqhW9IZnE41TSkEkGUlRHpT6TGE0mA9LKw_0nHNOoilCJWgMZGX6E2T_iYkBbk_S5teN_KRXCWz_wfaIVsZuf22BuJNrju1PP2uSyJciRlsXcKht28iBeKsnEGVTGvthrWCk0L4Hr4nonPAznvm7Y0HdoiaBB9MJMREwqFUCH_iKvVbFPYRRc3irRHtNqTjmZCCJq7ZxuS2sAsf1SBBeExvdarTMHkcGmLCRtQ1TpxXrQAYiXoSZIZcqARRI6oxClhTqDLoPIEtKIN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGhX0DUHQqUi4OWg2gVNl_xmH9F1Ygnr-XzZOxrvWA1ZRPLs5esSqL5wkmAIxK5apN-Dj_v_RrrKC915q9vjDEjhRrPQouSS2BmH1nynMnJXwna6E46O1fuiSqJjTFDpvjaSlnWNx_bCE3l1HPGlYIedRH5AMjHRipbSjY3es-QYedLP1M0PLU7_syfVLWp2UFdRpnpxYTZy5qUi5J-tMG00WLM6ZjP7WhfxcCHx0elodLHrxeWwWqqUH_KMs9X7ckrAWzINg1Z3xFjglNRXHsIgXy00E9Fl0YFHS3hVTtoNSftw3u3gW19nuLBKJECh3_J5hjoknmULLH7ur6sDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjQtI5bsQJmjZBQB1RoUZu4l9vxJ3ClwSlnzO538ITPfiKsCAnjW_AJhzQDMmCW7MQNot0rv5VYasyOPt59LncfjS0TqCrawJl5oKBGODIIyc81qrjN32Qtk4-X-qeQPljqSGcDzYXrAJQzyvcaXexRpmtR1LERgQsGMeRy3mFjozwZCv6a7e0m-h3qp_HlAtueM-33bmu-WVPoREkfZ_pjk3VedxGxUFPrQz2PBKzrdR92MYflNqeR2VuEh_7gyz7a2rzXVeagF3ohNVafHbandhhLev5qJCNoIyuI7EnB26cPEme4cb7DXWDBGV0NnrJGF8BdG0-uEB0JuuCE7pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP3UvpwoJh4-KDghfR469xTbxxK3mY80tRP3kjDY7yVNnl3dDzmC8Go7tZdJKc0OqDKWf2wP-_BSzpEBZuRtpK05Np-VCFeNZlbha9AzwvzGVxU9Vjs-2l5A7nC9isWwoQnD5Dv2iBstpbVdi-zNnIV_D0JV875hJddaIB2jSxAQYC067vSt-A2MYDpyne9oy8u_81RrsFy_ivKF6kc7L6k7YNV9ZGCYa4xmeGEPt0mFSTpREIgcCl1JbIH7PX2OfiGxKEru5T1dd1Iz0LknzsJOUyFDXxTTT7kOEU6HoZHkqzJneGeEMAlujruojdHZdlri0rUy5wVI-sUTjIaFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQtzBEtX2vwjcrjl4MyZ0L84WEhKk2vSZHFRFzFFRmev5ro8IPUscW_BPk9iBzkB_-ayeCLrYV9yv_i7XqJknDoVABFqEI5JOhwQcA4v7qSrr-7bPqCpFL0vxDeUTuQo5otSghx1o9HGEUaGKOlm7ekuFWZPz5-XDH2RR59-zXAqyVxwYoj7EzPM-Le5bBgZcZHz_UuZpq41AX76Lt10V-QxiwBn-bSd5lcFmwerdFrqRVjoW4yFuOsUWiq1sQwitOCB7UvYH8QSkYWoIxbC0o7hQI1U1OivHPZ_1AWYTQsKjNYE2FzWRvtn7TXBW_HdfEqn62j0aC7Cb4Aq1Mn7gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYxfst02nkTDbwM7j0xvtB85Urskdqv3CQxMufsxR4LD2Q5UbigwU-E7qXOJFGUrE2if5gYS10POupznmYjinDHqDyATzti73otfXqog04FZrVZ1jd7tHJ3RPdSTNfbGhSQG4I8K_S2l5pxSLpvwR5hqwVkevAmv-eClGwNpuCxCBmNWJ-VZjdFe5KU2STK9WVUNYwrrkQ67oez_PVCOYzJpPtlU_SNcg5q-pLv_vXORgr0A8LiVdm6ssZbk3bmqoH-0xC3XZ9B6Sru0nRk8FjFNhvPM2QL9xJmHF1kcEBB_UIKLEcXQxO6rgnq3wKDi7VCNeNA1iV5SbTBoEojXsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfX79n27CnN-jj3LoVkmz_f1rd6QBJA8E-YTbthJZ7Mq9XrYnB61tLubUfSi8EXkBvrJe0eb2F08wZ1bKu2zck-eZMmBhn2nAFoKMfud_Tv1b7lUq2qF4La1xJ7WRQrD-UKjz0a7l2VXb8Nift-8fvppLx9HRTvJa4-thJ7NNGKh7vsgS0ViS0hQxbgagP6VWRnMkbJpkAz78glnfdEzmPF_lo2TAlEO11Mv9ZYFyYiOmZkdL15yy6tTDgqrYsqHd8NU45Y4m6aYaxPsWa3NyI_f55Jpw0-sJgL2yKm_RYV-gdsYBQFzMg-8yaYcaxNK6s01ATzSV3BSWpsZ90d5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1Xx_qSoGRsn1KYlpuBf8AdleOdXCuVG3pCK_YnpYyFbpwvosS3v6aO6o5P1-dVEcn3bplbzpZgHWEiOiADy8snqiw_GWuQHMde4v65mb_u2KTlEPMlRZGJxZUs149vqtDIFlwA7GJt3gEKaEdV03K0ZGzAfyNbtdky3heWVK8zzFSDulvSgVx-oB25FGARh7tOhvpFL_FucI1m2VfmQFacfs2XeDWRklh2B0LJM9LSRGHBca6aTAC81XvE2FbY6GW2TPYDKv2RYpAh3zREBpH-OR1X05jh_Pe-lQdRIO0eMxmTf7ET2WWMcZdjmwD4BTS3nu6P-yJ4LMQpN9zLRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uak2WSDcAnB9BP8hIY19PPg6Kh84JeUuZXI_iTC9MBfuph7IgX2znXATt0p9hcOkDs3ITl9fztztuOxkPSQHmUlQup4LbQ7JYAKwMFzXcVoX2M6_sTvnqwJDt367Ry_V2gKXsAexfffcCpmVVIMPbL66VQyCaaQUSojREoKW9Rv3DqGDqpYz_dqd9t_hXctlHh7C1PbabTWiJFbuLBdEO8g3S7-Mqfjh0T9wq3h_OttNlwbs9Dzzvx2oFQEbKHWYeHJWsOVBbilJNiv7G8XPnTcss1obyUI6U-CxMGuCDScwdmrkVibf6iCBhO_xtUvrSYBOMxEai25BXDcm8NxADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbbA842JQTEtGaQPKPtOYGQNy0Y2luIbL_dJK4g5WYy35MWBnu6jZk33zSSrumPkZ-rq6brRGyP7Ez3ANtghVFTA0TYMeetjbnFW9gZNn9_45swzB8pvpjgsK88-AjN6MaKBAeo_yj4q0puNt9mwD86XirukDo96sGE0aHskmQrN6In_ENLRenoTrN6nsRwWWG_RlVSKKToVhC-xojRLo-TTN5g1-6U51mNxGaI3u8gFGQeKXM41oZdl865Uxt7ON9jFUVa5D398CjBHtrHckmzVfwbgZ3-n0S2inoPVS5okDFlTlFfFL4XXme6ELWcvObUc6bAsg6KFMPheLp5rrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_PP635sI-8oV8aE1x608nG92TqnPYpPPfKOpUeLlCJn3l4nh6MlgkEM3meqBlTQASI2K8s8dbRiMDf9nlrYKssQsv7NrZWXJTeSUnqZSjATnK-XP_5YM-xIfqUPA_8771QIFu7MpbQ5XRmTazSH2diPG685ZqgtWTU2RW_IekfZTQ5WPBRfgww-vW8RGg9lKMObcMdr-AK59T0J7EzB9TbddKSYXtW3tXav-tvxV2Bxgof4oGsMUU7FnrH5HHuqxwhAqTkCedChIiztCJURRHKLDdYp2UkaaZLyBPM3L4AeLCmjten56t33AlLW3O--GuxNO2RZoLvK6gMMceHi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ken8bPypVXWgrqvyfdUcxstUBnuDvQufavc29Zyd2VfgWHoFhM4dMuH7RTtGCjwn0dMKlLVIS9XsBGuKPoxtlqi6f6gtSsdYRMDDfLymRK7mPbDO6yZ0O4ezYJQgEScKk75hGlTB_4fAGjDq5GzjFcegBWhDrkPcBoDucDJjmci1GXxKgYKTMgBk1idZ4ZqrylvOjZtaVClgTkg7tcF1zdj-66DJo1US1TZtQI4cMXbUPzDHYARQxeeGeEFS1tZSadvLwKyYc7LxAi5SbCQ0Ktz9aBL9V6BYkgThvO1RE6iDcIZSpOD-AK53estqSl0t2Y1pyoLsX_TybhCmHZIAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAoqoNavadytIoVJ-zxW-Pu72XzZNDQlmuQEnuCB3B06gbFkBZ_Kkwfri8EMmY-eTemD9nFgAC455-ncaGRgu8t0tBNzFbtHfS12Uv6UN_ZjIbEESaxDPTusOJ5bGfcOG0xs_H4P6aMi4eJIBX_PQI39NXzwi-Lgk66IsR296_-4_UbiFJ9SNbGgxBdrlGKy_B5gjSLrIhPbLLTiWLnK9DjE9iNnIhk6fythWXxTjV1AzV3QJAugX7V7Z0MI191EDE4vdt4Kl2b2wp9IK623xOrd3NK_Io5bmA_GIE8j08dWwHrDWxK7dqPXTDC8j9Nbih19OvGM7co9MLoQ8PO0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UzcR7xocdJSLl9JhMKZQyTbDLCOBYjnSiHfbLYKvyW-OSJEiRX3Y_SmMGkxC47GeenZOYOe_m9wHzLBwYCUj0e-XozdKYXF52bk2qn-qy61lJ1z5H0AMJKrDMElwJJPPah9BEfAAcLAYZULR2Sdp24IiGHQIX86H_tDUFX_zwOLn2_pqRJfIVnq43PJmuiZZhvHRtZVL7yETeixSOlYpXocCoZSVoBYBG7Wwws6OgiLwgLL-xfmXXtH3MRlQZbns9HL8EyX8taiNV49s-14XQqxcW5fhSIO5LgvvxLvVrizKUFBD_KJvy9O7Y8Y-DUoK8v8DWa5KeQ8ujYSIHFb_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfdvjhB9bfRZADh91M2nneeXAlw0Pk9BOVLB9jNxZBTIolublxq_aReK8ty5FSiy1tmNTEmlxZRiJYfrBRBEOkZMYMrMAVpxskj_lEslBTbxFvbsN7fbrr9aNFY8UqzVIL8XbS5u2-lCN1f7tT4BEyMFEsG0wmGA1a01mQtW4Q3iR7BqtfRLeq30PM1aKk3xMp1YB3nfCbEHqvojVHw-JP42Y2FlS8gF_uwgkZTaaFu14lYG9LKeJ-lsJDuKgyWZESgP1-aAEWS5hFUsc8AJCx-SvPWdpaW2D4InSS-LF5ZUJFFTq9MLVpg6UF8WLBXAUBvlCGn89m3MRLk_aRc14Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsTLmnyOYauGMG4zC37pI2BC56owRl6snm-_mY1fM9Iw6dX8yZW4GbISoTdBBGiQi0tD_mH-QSoQRQfDzEHf-B5MOXPcwdTNzcM4Qqh5hrghQPz5yf5gMmJqUheYwZrcsQKkLCMv3IV4OdnwAttBoSn3AtI_sIiUNMVgPdl7t2EXabkblJT_LTRemUBgZd2habNvdqew31Otg-gUSw3aGOy7ImYB-CbTW9b2Oae7OIrtCm_ygT-IWjK0VLpO4LqzTQqoJ2lSg0eHFMU1c2dTzq6zcZIQ3LBgwLz_-lHVdzDWW_mdiht8FWzKtGfLyIzKu2082V-l6xMa2bat5qiRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HYcYsyb-olWYVZiXDKRlWIqEvA7cGzAJt4Za4u0SKo_8LNpvfkE9wbTIE2zVSWvfOPvgx-Z8O7FPjljs99TiB7ALRqZrVaMjvaffcyXxjAvP731g34KQES1r03WBMiXXb5mq-4qCRLGzkijClk619cNFfo1qa89iSDn5ArDCJaJ6D3GUGik8LDa4ER6h8jYfIdiXDuKLC_TuBLH32Qsk-kLqhxUjipp3YpJ7PNDxAwxu1xMSwy9OSjNX8Oe_MH7MvTXO7Rd0MN2N80IvI4VieGpAJm49gTnWslbAvV8pfAAy4Ji025IrCNlSBzb7aSI_-nP2wVn-CWhLEnJ2M-GxWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKQedmT3ileW5Bdk-brNqKzWTgGy_c0RduJmfFFaKb4EhXKq8uYAE0TSLdOIjTcelEkq5x_Z6OxjCwcxAklZoovBKPEHu3dg3-ob5QIkyf0pZxldeHTk09BWu3xCtyHFT7VM9ns1_Ii2OeIIZM5GlTTfq5mCvIpla48yyXIEUB-6mR8YTpKOgduZN8Rh7SvSy68V4oU6-v5iU5gPCbkCQGgKVPlKOmbg_-xgZFurbpI5-__fliI58mrjFLP328LmQ5eK1XnKabSAOLcwxM8WcekNqUO0nI03ZTuLK0pfKTznqX8zNfM47uIuSRbtZNibpokJMvp4XXzL4nrPhVJu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6KrZUEIBf7jeRsED_J8XE97GejHZylB4TnAI8K5CwlH2KihoRpAcAgZ3GPpkFNUWW3kiJ2_pT2fsyjAnAyI4YHRgs0JtYd_qGYjA-MJmLfyNJYTe011n6elZQ7sYRUD66c3CdxxLd26Mwe4-55e46INVZ7_wh5yIB5T_BOvCOCWOqTLtAaxRtkNC69IS1NaWcOx7-A-hXniMtd2dnroXHyzK-rBGNZy2YLao-g3tG3eXyCbyu_wBuZ7EydN1RD48NY8jhl7sSWm4FNtzrxeI3Bf19aB2S-qPu8KitGnf-P5M2bJbANZ-J1ew31UHsQAR9i-HxwuyyDYMZZGDZCqKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpiMjwp2ZpOcMsVTLId0rP341OmKrE2xdpdnhieWFlbzyCe1n_XD4HkGuGzliLcfY4YbmGKRZneFe282lUVW5F0ApnqfJfivMwRmkrcrfAisoJ_dlS5IQEA5aa115y9xPtUKU4-W_DQMB8bpfvCNIohNlMFaIaunUotQCQXtPqxk6YSCwDyQ1TtN2g1PMqBx_V52NIu3NZHrx7tWAJ7qoZFCpZOkKJZYJ06Qo1uLuJFaMOp-4aFYBMaBuzn-Tm-iUNDB0qdcVHHu8T_cEnPmUwY2Cz2ixU1jzel6lTWKYWZBQS7AY7PiGWx89iA7F50D3JI2G8yj3AehkyuXiLbcGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nej73o-axysZv1oFuSxEWPsKKs_2Cv_gOagG8xXZByUxo1sC40TMO8M2V9dXUeiWTPrp03d0xsKZuVeec-9aEvQT1p5_GSQ4OJsdLW9ZoSHvhDikzab_tDOOdY4QTHvKgo8rbViGA-fDLV4RAIsaes9ml2qQvZAPOBoem5WwgiUZr5jqEZkZoM5p7fP7qIR3E-1Uj2OMhsdK87oD3dD5ZYLB8EpBur0Xt2a9kxYsLKsmdtY--Zqjgac7f-fjRizVafO9L2ZZS35tzLnRdZrKPhHOwgS2aPZ1Sae-x6briRALCBDqZKZ09VYXxw3jxkAFTkReCzd9kWVF48J15hvRAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات
|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22278" target="_blank">📅 16:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPtiFvoDUllEyjQwjxTN9sPjOMYtC_9p8Fdp4GgDhJcfu7_p_UYz3kgmdgKKii2KvQmz_qnbc-bVkl8RUXBdd5LjPL11kBywqnJh0JkOXwNo0U4HIrP88hFb0YZSKDpEy8X8tLzj2JEsw2RE2Wk1LbdXETNBPPK_Yxt1OnzGH8h33jkh6KFS6LhXBebxibeC5ZO3N1Ov5lctErOwiG-aC_zRdteTIOQTRAcE-2ruM1kbD9GwddU10ZaX3pGYmspyA-JwJcA1ffN5l453391bgCNUWF8KoS3KAIQZzOiH5FQkEAlVDubqQKyIWHsY1Iomz9uBf56l6DCM8pvogeYVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هری کین بازیکنی فراتر از یک مهاجم؛ توپ‌گیری، حمل توپ و دریبل، پاس به موقع به هم‌تیمی و گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22277" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFuK4X64YaWmxgaP9T1qeVWN_7gy83G4xYehYAipQYG1oKjXOEDQU1D42_wuw0L8_7ze7DGZ3mQ0eFk3gWlMeNPDnOLnfGgez8pG6dc5LlkZ4dBnkb15f3keXMnxb_99fP7xr9NBDH9pKAK2-vYNo_VT3M2z12n_iUQIgLhYBSjIhjN2PndGqkLkE_SfShtxMA5SkV9mYzvWDox5A1B-Z2_9_TvaFqnb7xb3SOaMOLiV7ETJPQOF-BYKkZAkDtrigsRfCFbpZhpHHHr__368I4ZHx_7ezrHeKrq450ptHIolfGBVs0KubF_kwgsuW-OVSXZGZnGetbNuiNdjyJeb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22276" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1yzNU3xR8mHzMPPn2jKiL9wjblh48DVI8oioYP3sSqWFarqyLaf4yRnT3OzfofawGZ-pnOjsRtaTVS1OezR4dVVzgKOikQ7sEeo3InJOl3AfxJFViT4Th1s4-dL1WHBsI2Cq09xtlkrSiQXZaQW6GhIk7YJw6D-JET8_AxTCGSwQTQrilrgdzv0UIyW5lhUb-AzeyfJTJ6CImeL7tU0kKF3FYvGauJ9xn1IR19rL_PJEkquNyC35-nb0FL0sPxNIhhN5Xq39kKGtDZcfEqF31xwM1dgdFKNzg-xbu0AWFQMqO9JSIP1VwAkhdfAVVb35J2uxEu6c0clWE7AuJ69YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌گفته‌‌روزنامه‌های‌ حکومتی: اینترنت بین الملل مردم ایران تااواسط خردادماه حدود 15 خرداد وصل میشه‌. حدود 2 هزار ساعته که اینترنت مردم قطعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22274" target="_blank">📅 15:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxsmzAu9YScKeZ3p6v-4K-iTSJwaX_3bzAqhG1AgaJ-hctj_ax87AZyb5UEcrQTjPjwh5S80s7XcaPyF1_HnjKupiasBR11o0ltEqsBxR9WXD5ZD_rB9PX3K--Hp4sszscQ0ESLxmTXN4jIUWuBp0P_fqXhWD8PyOFZHJ18kE488DMUdY_tOcjeJRTy-eSLbdqxCKz432O95w-rtX0erT1r970gANGRb49beohxGFtKLiyyGNgD92nOsnkpwvIZ-WmH_K7PaD7jpRVWXzIxxeahY_GeQkMlqzy73e55n9hZK2HRW7nVe5Wlh7pptbm1JxkQcotqcD2v0JQtqxJRrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22273" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8nBuPSlnJRwDzdOChpXZcoysLjNL3a852gw9tnpvvbQ_61H8yw4WIptJs5dytjfjFmqxq1UjJmrNxz1-BjYIRiYhSdeMMENsvkIGFSw8SgA2mecmvBbZve_uSg3GIeNaN08LEFkwZpSNTrd5DQ8gQ11BWYGZH1fT-VobnfQOykYxFeTMv-PBzWLdP4fSySD-ZYyxXIn7R4BVVaFjBkRUewPDoG_sbEiyh59XwZfPy_S_pVBodMLKUbwpStOPBAgw2uDw0wpeM1AIgyAuZ-U5S6Y2IoOZIK3yRsiE9hJlPDQtfQS9Doo_QgfVC-1_tSuOXebYy7C6A-vxuc-6KbrOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
درحالیکه وب سایت ویکی پدیا از تیم های حاضر در لیگ نخبگان درفصل آینده رونمایی کرده و در بالای جدول هم اعلام‌کرده این جدول غیر رسمیه اما برخی به اشتباه اعلام کرده اند که AFC اسامی باشگاه‌ها را منتشر کرده و برمبنای آن اعلام کرده اند که نمایندگان ایران از سوی فدراسیون استقلال و تراکتور هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22272" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=VpEDovWk7TjnPGi4zTI4bbKb8NVyyCp9F4UIucNIuitqvBnQtIlQoS6jPrhUrytiGyqxmAAWKslEpnJiRSC1rD8qk5DpbbrodsErVrHVhcKkElB7esA1amQIf3b67linAQjhVhCJDMIE4Jvh4z3B9x6a11E0-A7hpJTetkyY9gv5n5NPLp5czljX7mwdiL65MbolHSr_N_TdZNcKC4yHAOQsfbHOFVAQigkReCsH_7bfdmNnw8l02ZmjyEWdrad6W3KhT7wH9kaiml-JOPZlacLSPBfSA2nC_ISVC_bEAnFoqviNOgtvyA0QcfdhCpjRvKa-_st7wLjcc6cOCbveJ3DKw5hLHIoMDP4BHOLeLFVOTx-EPQR69qrQU7OsuJbKA8S6c1oBbIXzbZz5RZc5P3uG5q8OgugzbGRyM9-mFHLE5DSegchXYe33SH4eIybZe9075ilqd9DnfbsfGmWwkH_ycPCQgs7DVq37o4z3OKo71yiunh80Uvw_tHHoMEVsajAyaWGzXBtxPadhRIMWPs1dM9k5z_BtnNEtUznc3CFZIVPsDByrCdvl0F46NdkXBT22kLepQRARIbTpYsa3aXH-B2D6at79wWUipDfXdZDtecGSgn_UjTkDQIvtja9foXHPNtGSapoK2yi4pyScCGZ-SG-pL7S-3kgfrTqxyn4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=VpEDovWk7TjnPGi4zTI4bbKb8NVyyCp9F4UIucNIuitqvBnQtIlQoS6jPrhUrytiGyqxmAAWKslEpnJiRSC1rD8qk5DpbbrodsErVrHVhcKkElB7esA1amQIf3b67linAQjhVhCJDMIE4Jvh4z3B9x6a11E0-A7hpJTetkyY9gv5n5NPLp5czljX7mwdiL65MbolHSr_N_TdZNcKC4yHAOQsfbHOFVAQigkReCsH_7bfdmNnw8l02ZmjyEWdrad6W3KhT7wH9kaiml-JOPZlacLSPBfSA2nC_ISVC_bEAnFoqviNOgtvyA0QcfdhCpjRvKa-_st7wLjcc6cOCbveJ3DKw5hLHIoMDP4BHOLeLFVOTx-EPQR69qrQU7OsuJbKA8S6c1oBbIXzbZz5RZc5P3uG5q8OgugzbGRyM9-mFHLE5DSegchXYe33SH4eIybZe9075ilqd9DnfbsfGmWwkH_ycPCQgs7DVq37o4z3OKo71yiunh80Uvw_tHHoMEVsajAyaWGzXBtxPadhRIMWPs1dM9k5z_BtnNEtUznc3CFZIVPsDByrCdvl0F46NdkXBT22kLepQRARIbTpYsa3aXH-B2D6at79wWUipDfXdZDtecGSgn_UjTkDQIvtja9foXHPNtGSapoK2yi4pyScCGZ-SG-pL7S-3kgfrTqxyn4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFQ-gGknpfFSCYDMZPmH-eRonYjNYQ4shX_98fyKhNIyfXqINspjldC1C7zFwg2vQbjX0y9A3TcigyuzerfDV34RkDLmCLToGd5te6qQOYxZt4z3-06U4rZVY27RgDvZdv6f-lTazLjMMLctEFqMZWOscixxUGxmXFIOX_arTiMGP-oNRKmEkYnTZAidb2Eq1Fj6Ed2f4kcQp4kuCKnJMQ4f2w9zr2PyDTs0LrmO3b2gcUWcDLzgaKi-sA0wAhP0iu7ljZmX-8PNwSsnEVuFv67UaHq2NYbZVcs_SsGwmg5ci3lICE5b-1uC5XMsnzOmakD1Y5f0zFt1eBmrrUeYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=dQxg9tBZ_95SB-0HrFy0eSufL8PuNM58kWtKu5ITl8rLJLPghQWKXJUFd2qHmrkm0nPzgDBdvSOCv8wRyNNUyET0KYKg54HIIueWT_hvQYEgUPT_4HHJAeekd1g8deh7rzANQnrGAAcrFINNBk5XzxXvmVhuUMizcGqmQ4XiTpeacHe9BMY2Y2Fy1tt6UIkFqFDfuWpOkJkkUdBhByWYdxpaf5msSBsnpNRpBqPWoSAJjgrpwGloB3HnKkachtkhrWKAKGWyiUE2Lx4G2IJ8W0nsJO7r7Ml_yDufodirzKp5SWBFWioMjIx0tPi0DIbAc0MtxG1u_QETW5PFBRy6Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=dQxg9tBZ_95SB-0HrFy0eSufL8PuNM58kWtKu5ITl8rLJLPghQWKXJUFd2qHmrkm0nPzgDBdvSOCv8wRyNNUyET0KYKg54HIIueWT_hvQYEgUPT_4HHJAeekd1g8deh7rzANQnrGAAcrFINNBk5XzxXvmVhuUMizcGqmQ4XiTpeacHe9BMY2Y2Fy1tt6UIkFqFDfuWpOkJkkUdBhByWYdxpaf5msSBsnpNRpBqPWoSAJjgrpwGloB3HnKkachtkhrWKAKGWyiUE2Lx4G2IJ8W0nsJO7r7Ml_yDufodirzKp5SWBFWioMjIx0tPi0DIbAc0MtxG1u_QETW5PFBRy6Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=ora3lZoJLjGfVkT-nHS8g2IDBTe4WzSc1Pzrwgq1fpXqlk0INNVS9w7iF-A7IS-IYoqPAOelvE5Sx9P9QxAmvsEeYm_aWjHY-JKmGzvwjz_GfEEorfrXiC_AGEGR0T5ATWZotTzlxyMExzH72j2mhPpymAAAP-sU6L4gBfTt1nmysleZiFNjy2Jn5OElLou8_iOdzX4pUT8-Voma5TgOy6ecIk4mhN1ImbEP5wYCzp3pUB5YcUaTgNKt0cVg2eU2BdjFdkKyADxqK32TmNcmAw01APqt2LQnxM6qU1d79TbYDNsIRsz5x_MxbmdpkI91Y39ok0KvjWAvsIumCa0V_4c0lUYrfql49RfELiNJFZym9jG8Lzp4jLJ8zOr_aH58PWuhZofsnNhHQAZ8-H_Vpn5Uhf-45AN2r50eWSWWXMl88kbu4GP28SofPV-U09cj6SIunx_HXXIlziXgqwWbE8ZNZxxqGDcjnBC3HHLJMxmnsFzW054TTGfhxVe_rsbw96PdAp6wBZBfH8w_Qjf48QVkDuDd4SisSc0WFUpxkpOoHpfsyutRkcrO10g47QU3ZwDtTk_Rc6z7XK7AqS_FMkEOqC_1SXejT74eEIEa8anz9ThG9wDURBk1QpNDjlq9-7HEW0eHbk_ofrTJUefApYW_jjGz06Kf49yvAVqzPNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=ora3lZoJLjGfVkT-nHS8g2IDBTe4WzSc1Pzrwgq1fpXqlk0INNVS9w7iF-A7IS-IYoqPAOelvE5Sx9P9QxAmvsEeYm_aWjHY-JKmGzvwjz_GfEEorfrXiC_AGEGR0T5ATWZotTzlxyMExzH72j2mhPpymAAAP-sU6L4gBfTt1nmysleZiFNjy2Jn5OElLou8_iOdzX4pUT8-Voma5TgOy6ecIk4mhN1ImbEP5wYCzp3pUB5YcUaTgNKt0cVg2eU2BdjFdkKyADxqK32TmNcmAw01APqt2LQnxM6qU1d79TbYDNsIRsz5x_MxbmdpkI91Y39ok0KvjWAvsIumCa0V_4c0lUYrfql49RfELiNJFZym9jG8Lzp4jLJ8zOr_aH58PWuhZofsnNhHQAZ8-H_Vpn5Uhf-45AN2r50eWSWWXMl88kbu4GP28SofPV-U09cj6SIunx_HXXIlziXgqwWbE8ZNZxxqGDcjnBC3HHLJMxmnsFzW054TTGfhxVe_rsbw96PdAp6wBZBfH8w_Qjf48QVkDuDd4SisSc0WFUpxkpOoHpfsyutRkcrO10g47QU3ZwDtTk_Rc6z7XK7AqS_FMkEOqC_1SXejT74eEIEa8anz9ThG9wDURBk1QpNDjlq9-7HEW0eHbk_ofrTJUefApYW_jjGz06Kf49yvAVqzPNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از تکنیک‌ ناب‌ودیدنی نیمار جونیور فوق ستاره برزیلی‌تاریخ‌فوتبال در دوران حضور در PSG
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22268" target="_blank">📅 19:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ89XKOB7MesJ-s8JqpcvlUPx40XgE9YyaUEj0iB5oI52Y39LoCwV6RcD5PaZCDC57uU6droZYmsucs210KOXCy_pfPYfVBMqQ2z5pZB-5bBPrIMWwFJ-YJ1IXqpGqqyQvmawWBMhRrbZ8vwlyMnxRMc2u_AddvbPbkF8WwHH3XxPv1jgN5IpffXC_ZwjBlHlWw_cLryYh8CVXFuHjQFN2v8-M86nvuF8B_kjaMFK-Iq77iZpU9LqeKWtbRCm0QWhfrkyRYPJzvIH_BTWYOMjFfcBUcwj1kETEJRaYZS6BioXwN3AR7EvysdbN9qaKFBZLw-G5JhoNG2gLexH_nsVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22267" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOkmUS4VcKDpHmXTtZ3wZxK47n70sFCbGF9JmbpaipxHMk4V_gr3mE9oi6W2zbfmYd_RIh7Y3SHX7zy4CDNYeA8bbV0Xe3pxm5PA6KlTwfBgTQicYg5pMXAG0FbDBCP3DtTJDKv4QayN_uLiR9uial3xYjX1zp_G4zxJ7AS0Ft2Y86fVRg6J68qfodBidN0iVyousDb32sYJQT4LqjVhvfGkqG0NRCbjGRa4Fe49weJPijXNmRkfTYm9Dqgtuj0wvV0eO6GMAgI_jlQkwcjXg8cgspVZpP_xH4235EVQ7-KrzbjfdkhIghP_m8d6eDwwfU1FJIuTEwHJS4QSfg4C-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22266" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGObtI8mqVOFbaVUnSnre15OMH_ZbvoBe-sOS2qOt_R8QS97zHabLm14TO7FvUPErmDndUH9JGLvhmJ9DMoIssy_Hb_YUW6C9lOuozQ_3Kn73ey9_sHh0g9HyyPMufuOp9lvyye3U3T6D0lWIfxZ7oe7UsTPYswYkYlOuQ4WS14MJA1qCOA7Kpr5gRO7Hn8HQ_-4mx_PlwZdKudZL24ESYAKgu_7aLY4vUEylGKifP5DW8dJW00zpDP1uBBYxxe_7j1Dy7USQddk98ZQMOLP2LNJ9yKl_qHuMCwSd-eVujP3onhBMYJ5JEnnMV_2jgZGANrQVBMmZQXhYPKGBDvjlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی: پایان راه آلابا در مادرید؛ با اعلام رئال مادرید، داوید آلابا، پس‌از پنج فصل، مادرید را ترک خواهد کرد و در تابستان، بازیکن آزاد خواهد بود.
‼️
داوید آلابای ۳۳ ساله، ۱۳۱ بار برای رئال به میدان رفت، ۵ گل و ۹ پاس‌گل ثبت کرد و ۲ بار فاتح لالیگا، لیگ قهرمانان…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22265" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNiFkiNTyoFViGCYYPchS19t8z3hYTO5v1lwp9xw0PnOJIO_LWWCAQU7Ybx-Ebb20xJVYNCgO0I7m17MOJgNUfcsngOneI8dn3Kgmdo8WdlO19DkyJQZ_8JdKJBM_wfRBAFVKTVS1kfL8g1BQACQKSY78AVJuRuMfJDo70lSTazqm6hVnrgflFf4EqyMmjVVAQ9yXKZ6aJ89dkaxe5E0ZdyDONFUC5McUl5xfLX8ov0dhobtmNl_Kf3AJXUFP6FHSn4fkj88V0tGdo_xqU-IcQRoTtMF7GwtACDcm4Q7nHlu3ZoFPv9phcBcn5JTJzwBRvEVEiPgUbjzbVauM5vjKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22263" target="_blank">📅 19:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxH0Irin6foLXT9Y5PbxgLn_WaVMZnDxe_7ASn6vnOFmxeNn2kKkYXEQ1Y0E9AjJbrzIloosfHLR2Ive1nJBn3d4ROkBbI99G6gp0jWBmYASOzR9vQnq5KXeymIsCJFo83sSdxgE6TEcA3e6VV_FE6hBF9Zf1_6WVfzUYgF-sBx770CRWjG3x2yZpVvBRV4kGAtLvWYB4l5gSrMV-ZMVW2hU7H3OFZOYYGwOwVb7GWWIuCh4mbUrho7o9jRBsDS-ASUVwkzqQBwHEAiEnMGc0-o_voLC2vDY5bZgZfO59T4ncKaSEMdxKajhz-a4mHRSoov9OEos2_y_hH2PCVtkvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22262" target="_blank">📅 18:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoZtvtbyfcJp8l2XAdmK1MAN67Xs5cDNlqIT5PmlSDU0FvLqgJOLDVGnxQ6AdlyHOMZuN5wCGpId1fTtFw-gXh3OKza1fAkndzhYlKaAgCi-95bsP3rH9Tohe-vMnCfVphJx4pr9e-FFEA2UNo4qoL4i0tgwuCG9qI13hySWrdmU_N1kqGIYlq5zul2iTsJBj32BXQrvb3arXBBYJK954s6gnxMkke79BojnwooLJYrnqjH3aEdHspJ7yhEmykxVVqiKXIyxcpUH6jdyTNHOx4b109j2ku9ApCzyy7kuQC1MyzwGgjVer4AAoaZxCQYWQ7exD_4-E0j2jQ5NR-bqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22261" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTB7uKZyLNlFY7hF2_5XagIwEh0vB3adwsIdl4C1CmVaBzXjHiw95ohROVgQPWC24GpVupbMmbMQ1gSe_vf-do-H0qnLhNcTkHJEcxMQON021uus2OR-OkzfKqUazJwb1SVoEqB1kTc5DMqycdAd3_wLLe1yB_a7rP9QOM1J5iRzyvm-hRa_5ashTrkhwFzVntEFvOPdOd5J9nSUL6Io6G9zotbJ2H9RjX4OZfFPI7USfIhohpjO3a1KlfjldQjZ1LMZ7pcL84Iepevwx_CyzDbOKnmV6FLJyriykP8PnlTVA0SvBUavE6UL1ilH4CCacKXE7xP1kiZ-5TFq81g1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛
باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22260" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGiq_0oQiNhQNz4lCrDuhVtiJnIrhnSfnfXwdG0Gdf4CdbAHzO4ucSPKbL9ElCxPgMTVz3o1kHw43WGCFXYp0y0LlzczkpQA3b3iUpl1SQ00AMqoqzVsVX6TGtLDbQWFWTO3qK7QkvJ2u8nXI78LWCrV1R1nK69GxLWGMSw4gJFIbjvIecuVNPTHQKfrGYPsNGCM_-NQCRM51pfStaqTHJ840Np-sG18za5TKd0pMYRAIv9IEzG2wGlHlXcta9p9xZt3-X_aWMAN5VGeKRwmCApc9jefmz2cE19722rODctbfYl3ZuHlcDfgJb1ttZDFWSiJnBp3pa6pxefuPKRPyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22259" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcLlHNzK_sL4TV2PvJKN3VvdX31KNfTNzEAiC5EycH1JxLMQOBN1dDYTQZ5ihMymeRUCb8g8DA_MEQgAo63CD9UnlYeUpcLEnxZs_-jQ6iJGbQBqU2fyz-54g7gHfdn3Nc6O3xNDDlyZVc4VA1jEKaC86Ukmi-tytpE6fKguK6o81SDyLEQJ8Qt2BsAd2ZOO8RRS4Mq8cKNNOBpqa9AdbIhW_6GrjZltXEmIeRh4Zoj4RXJOGn9LEj-Go7Z2oAhC1ZSRmpaaMMvN4nXz05aV9exPQLZm-j-7P7f16qENpxdE7v2O19Trk7732SGKO09hwWa4i137Gkmj_0kaaDDJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برونو فرناندز ستاره تیم منچستر یونایتد به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22258" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YI0EKeI6pbduJ1uskZq4UbbO8sMW5ouhvzOu2TrCZlkw7YMcwREeJwmVADigaRB4IS14HtHj1f-Kn5eKkdP-K7x8lHul6ZLCELHrWiRdqCF3bFnWnYWLR18u25UeiVMpPrbl65uFZkzaQH9AX_UjxIgoukHcl469LOdRO5s7Hb0jC3m9AOveoBfAg70DkJXxQxtcJjH39Sc8z3NfHDBPCyln2IBQRgS1MgQDdvYCWxdN7k16PZeZMr_7JNbFzb6e22PoTSRMTXjv4hN3-Tczy7fY8ARQNARRnpQl_GG0CTmf77VYVYdJjGfPKz8R9FJw-EGLQxwUzNlyVfiO7Z7Ngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22257" target="_blank">📅 13:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZHGvSI6MoOYAcbSlpF_2TcFUTjdbgdBe6nFEPeoOfEaeTSZv53uX7LbMHcbQ0DyVsSDUl3MBA4Ws3kY8fARdBENEjuPRQ5pcgRbwxM3CYKrcJfXzbIpR-EJOotvEs6lYfFx1cQwybNwEA4QrXV2PvRIVDfQgA-SLxBx6Z6Thv5i8oki0TZXgyQjdu-WZcOuRU4LmOx_GR98W5ecQmbMvuLRbefPuaD-KhNoAjKWKuNxm7EbZKMuH8a3khHMPtHLw32lFVbGjTvUX-5ubWJuKfqEos4UsDlfWPVtco4_G3RpvXmFqIOKREwpV10Bvz1SBLAM6TF0zZlUORJ1W5nPvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسعودپزشکیان‌رئیس‌جمهور: اینترنت بخش جدا نشدنی زندگی مردم شده. دستور دادم با نظر رهبری و در جهت رفاه مردم ایران بین المللی وصل شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22256" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dw99Cm_-oI9vTxRXvoe-q_17yJhkp_tU5YEm6ZXCYg-EdJ9N0eL1pUyznRLDoO75EKjJ5O33n7cETkDbvpwh_kcFE3UBWGKW7bsjZ2nVPytOwJC7ilRQ4BqgQEh7Sp6qN71MTpoNLdrTIK9vBk1e8GchsQpTkdSCA4qBKktOsydECA95k9W1gOK_9rWJ1dXiWWxrH3_Zn2A0ucvXJ05s1CcZwKWnqcx8ZXYWXDQICHV_t6VLvmMxFQ5voxQkM2aPdgJlUsLDHsOxxJe1rPWdCtTOimkCmGDkBUiuJ7hEx95SAZH90moo_Kn8ODRgyYfeFOB95Gtyyi7-3SNsmki8sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22255" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBGsjhYmQIFfoLJjdFJLyYSJTHpPBkdHuxaFB-og1VB6B1eqzfqQ3L6Kp3I4NY8XIdf8YKNf70ZCa14RDkTc6SLC61f5JtLPLVSCPe181oUehFPH0Q0gg-5DQK7pF4vH3Un4qkWMcr0iywnUdEhtCjTr3bp06RIndBbo3uVJMTTPZGNcJUvwloBxNj1dv5ImC39hgrLdXZdCu62ai_KxmRD3M3nodtT3LoFPxJGZTFFaRgLqvI_qlQh68OmZhRAnt7Kd72yXWYVTcv8zrQfat6HNDGhkquphkuMb5kmXNaGVe8ckCfWBttOZviQN_gnnD8lZCaeO69HJ_YIl_7RnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فکت؛ کریس‌رونالدو به‌اولین‌بازیکن تاریخ فوتبال تبدیل شد که در چهار لیگ مختلف قهرمان شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22253" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjKvEthM68cVVip2qQqKuCnOEoanEhuqYOLBEQbfRRLEpHIpr8rKmQTGKcJKeXo6eSWLbB__e2UbNTrNA_InJ3YdyTiGa9WM6u7ifDVCIBBSSpp2spEG0qXjrGmpWgBtqSPCauo7iWffO46C9g6Z8LDIuD_o-kggfFSfzp0k2hG_ZS1i_8UIpfdk9WILunrB2T3jOSBoPsvQ2yo0z8CvXt2CbBqcpOLoEDrOeBlmQmWX0-zjao-Ed0VMyV0JSejSzEKhr-OBfE4AOOHvfRgLCbsv5gT6kbUS6lOs3is22AjEqLQX0PhyxTLOMAsbIvizR8eqPtz9pCqp3Zd5C7LDHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب فوق ستاره‌های توماس توخل برای جام جهانی به تیم‌ملی‌انگلیس دعوت نکرد؛ توخل در مقدماتی جام‌جهانی‌نتایج خیریه‌کننده ای با سه شیر ها گرفته بود اما درصورت عدم نتیجه گیری در جام جهانی قطعا مقصر اصلی این اتفاق خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/22252" target="_blank">📅 00:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtCOhau2h9fwi9-4Eu_xwrM1_ZlXQV95Z4GnQzFyFplynLQYN-colzDoDSehijQVxwAnt1CvDZs0hFWblS8qKof_eCQ6iNO5-EDIBvlTbeeuGZdwFEr0EJJ9NqMln6ylC6TcmAebQ-dJgJVP7eASh97Uw_mLwZe34fPmYhA7uPJK9iq1K0lQ98hfN-0PREQmuWKyl6R6VCanwX80lHrEzGXdQOmKT9sX-0rhzdIOKpmfeuzEzqXmSu01_bKC2nRmzlp6RjF6U_OzHi4yW6J18pHKxL9CuNfp-OcvznFq90b1OLSitHv8RMtrmR4eldrYdCCLZbPizsDiVUJJO7x6JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22251" target="_blank">📅 00:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfkzGcLJrij-huXBr2oAkOcAxFzVS1TsIyUjO4eHgesi7aCKOHifEYH1MR1W7LfaJ0dP63eiKODWHwk2_J5239gsF7ZZaoZSsil4fsE2EMAYYtbWbGewtpVzBBbrV7Lu2Lnmf-eMSYjECXQIxuJ2r1jMDgqCyMBcozvNHIVgS5BReX4wQGXL8EtYI87OfmS-Za6swvUnHbSpy4hRzMe3IEPNAiSkpTgHTanM6ze5XbDARTYEvFIjAI-dPEHT-mCyFNfg8so3lrB6NQDY8BviUT8uMe_wLuQ27bnP7SHgd0bgfJr2byk_DFf_T4CxbC-VSJ1b0brOlKTHQaY5WAefcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7xzYzkU018cck-d4IZT93M5_covjI-7yE5ON1Upr-XGDkpG3Nz54OdQ6bUyxp3e8CVF4id1BDpa5gPAeoyl7C_TNeK--_nTSIyOfviC0BpXffwG51DW-Y114deFKSU0sYM8i0lxY-Fem3ZXpd1KeMuZwftHL6If49V1_szpu0zUSboXMPa1Yofj0RyAexWGjdF_keLxKCT77asneJLuFJ8f3GB1QH1lHKMyiIXslJl_p6q1JQfn7zKxB6OATyc1E-SCm0Y2jT7v88Kv2aOKY70utbG93BdM8hsWilRGQEOR3D0-S24f6__hMithiuJOk7RvoU1HcXzvA7ookte4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
