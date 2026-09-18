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
<img src="https://cdn4.telesco.pe/file/I_6TyvfvTYFRLjeO_IAeJD6kmXInTEaLYe3gWzxJNfjeypcHlgEuszMclycf9z6FXpW5aDsll8OUUXAcvqAGNpS6ushpfhkOeKBEHMiK-0Ma86eQXDmtF3W-Dw0ZI0ZnSw6S4JR9jJkrjcEQvA9mB0cZLif1TcFF5Z2lAXI-KzfVqz7UBrmLersLyhRrsT7AlYrtdgKRBeQklk5On_Q6plgtXDaoX9CjhBkgvIpXK4yjabyBkHLvgjcMQ54Vkx8xvwFLvDVelLJCF_pzYpV6sYFPvkyQwJGTS8_Z-0BTXkG0quF8qmfrnFE_AurGYbGAhpByc-gamQ_pSy1n5mZb-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 491K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 11:00:35</div>
<hr>

<div class="tg-post" id="msg-29989">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RosLnKfcyKB1Kl3yckG_RZMGGWHZfQt_95v0NRw3N3JW9F2oVomcIASPgsIHkUv_hl6rpJm0tz4spc3uYeYZEsRv-w6ciprcsKDB8zyhvzgM_4KBPcyIjzNQczABSsaQ5NntiZnsz03-89K14DXLvFrXaK-QWHYz_OEFDt9k-8AQVFUlB-9_UHTzCP6mgqd3dkj3GnB5NpmjWy55b4dEQyZuM_atKXfec0o1Mt3JNeuZcQ2WF_F9If1F8J7h91GTYkS_5bNLie0Nul7HkG4VYe5kBrWWW2U_aMTucgeHSVcJpvyu7Idiu08eogiWHqvmliw_I2YCjGO6v0pV_AwiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
برترین‌گلزنان‌ پنج‌ لیگ معتبر اروپایی تا پایان رقابت‌های این‌هفته؛ رافینیا دیاز با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/29989" target="_blank">📅 10:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29988">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKbls051N-w8up2YsRU7NGg0PN48LLhQe6RDAorDaInMBDKMb0AHI-d9JuztPf8O1KCPdba2wTZS4MEwJ7sN9uwQ8VnH7tbvg6vi3cBCmNGmnO3ddr6VkrPU3VSOu5iyUEdn9avfJX6c-8mwOlUvvVX2fq5BEuvityeAKs5Dv0lOMKk9_2ioEmwVoF8maFxC2XlqNrVlmkU0mzvrz15DuvzJOw-S9JjQCuVwS0_0p9-wlZ97rjSNhWmyJtLstH7yWGTCdoLouG-16_Jf04Yrlo6WW56RaowOh8lE8Wdxm1FCl4YftEZHD1d_ngqc8mUwa9lRlhRiOCNwmg2EKq30Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/persiana_Soccer/29988" target="_blank">📅 10:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29987">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=rHVTBu55SiamxdJjhZzGSGqEwxr7mvPN10gJXFdItGyBX_5XrnmwieDvlbFxr9AvjDQj1owqYOXeHKEGd4ullyhzV1Yl3NaSNFw3mayCYLjOXsbW6Ed9PlBJC-pyT9mhQ3EXDx0STCo5aPTi_cxE-RgPbReiHnGDls1GpG_G2wxmNPrvdxt3iy7vVXeLjDkV4MA67GYGibtco5hl8qinYk-Z8QGHgAuBlKCXFlWNfKMiHbfJSSvz2sB_hAgw22VfGEPGPYQG2RnVphmzO0XzkziLwDmZIsSacmIcAqrXmKDdsy2OfPVHP_B1SxN8ZRGRTh_zQVhV_tZfQlKyY9GDCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=rHVTBu55SiamxdJjhZzGSGqEwxr7mvPN10gJXFdItGyBX_5XrnmwieDvlbFxr9AvjDQj1owqYOXeHKEGd4ullyhzV1Yl3NaSNFw3mayCYLjOXsbW6Ed9PlBJC-pyT9mhQ3EXDx0STCo5aPTi_cxE-RgPbReiHnGDls1GpG_G2wxmNPrvdxt3iy7vVXeLjDkV4MA67GYGibtco5hl8qinYk-Z8QGHgAuBlKCXFlWNfKMiHbfJSSvz2sB_hAgw22VfGEPGPYQG2RnVphmzO0XzkziLwDmZIsSacmIcAqrXmKDdsy2OfPVHP_B1SxN8ZRGRTh_zQVhV_tZfQlKyY9GDCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی مثبت 18 مجری‌صداسیما روی آنتن زنده؛ طبق آماربببنده‌های‌صداوسیما از سال گذشته تا کنون به یک دهم‌تبدیل‌شده. مثلا یه برنامه تلویزیونی زنده شاید روی هم50هزار ببننده‌داشته‌باشه تو ‌کل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/29987" target="_blank">📅 10:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29985">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a52708609.mp4?token=NCjdTpQXMGE5nr24SL3mbisuaFBVkA49pOjeuEzifxOu2csALJgILIS38pJoMC4o37ho4zR1HUhhr69AaV6YsiNRF9Sy9b1rFWJEeRdVzIzTRI3H8tnDLupNfr5DVWm3i7819SgoAbeGpqH6I9sc-8l7GE5UNQTQLq2t9IACjck6VnBPmJDDJ-11DrbZdV4ijm7D5cWZQZ3KoDm8XDO_jjmDzdVa5PZUSbHarBsQyc7iPc9flRW0t0ljmAzmOgRbdzqwG3KkDh5_dIfuK2Ny9EtEIFU-J8GsWkqATkNSXyvcTvEKZoffxK0zBQbKvSWD4vfewZ5vF1fVQgttOUWP-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a52708609.mp4?token=NCjdTpQXMGE5nr24SL3mbisuaFBVkA49pOjeuEzifxOu2csALJgILIS38pJoMC4o37ho4zR1HUhhr69AaV6YsiNRF9Sy9b1rFWJEeRdVzIzTRI3H8tnDLupNfr5DVWm3i7819SgoAbeGpqH6I9sc-8l7GE5UNQTQLq2t9IACjck6VnBPmJDDJ-11DrbZdV4ijm7D5cWZQZ3KoDm8XDO_jjmDzdVa5PZUSbHarBsQyc7iPc9flRW0t0ljmAzmOgRbdzqwG3KkDh5_dIfuK2Ny9EtEIFU-J8GsWkqATkNSXyvcTvEKZoffxK0zBQbKvSWD4vfewZ5vF1fVQgttOUWP-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
محمدجوادحسین‌نژاد که جدایی‌اش از ماخاچ قلعه در نیم‌فصل قطعی شده امشب از نیمه دوم برای تیمش به میدان رفت و با اینکه بازی رو سه بر یک واگذار کردند نمره خوب 7.0 دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/29985" target="_blank">📅 09:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29984">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxSFqyW3FpK2kNjPMH1KpopUQtC_YOXIDGKdlWEDAn9qQWmVsNXILvM6LcHPSwZA2PC4w3r3qrSJi0nmr2HWifqO2sGHJHF7DVn9TTUwtYkzwbrkOTXC6wHDJyiNUfZMLU9iwMmPn-wTx7S8hNqV-50D2vQmlA33N7xgdZezeJ3ZpHzH59sHB8gOl989RCGBxuc1SL9gTT6YXQ5PXvX6QowZccFXmwv4bnCSsN8a8202R3xcJfsAYuDoIJdXe8lQRa1owOdHprmoi5GkGX1Z4BUsu8QnWupAGK5vaFB9wQl94auX7qg81BQe0OezZMhoM-kz2XIBqJtcTUgXScVbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امباپه‌ستاره‌رئال:
اگه‌میتونستم یه بازیکن رو به رئال مادرید بیارم کریس رونالدو رو میاوردم. او در این سن هم میتونه موثر بازی کنه. اگه به رئال مادرید برگرده قطعا میتونیم یه زوج خطرناک تشکیل بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/29984" target="_blank">📅 01:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29983">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzmfOV8bY5vW40rqrjO-5I_Gos8FEcVL9uKs_tjFGRRllp-31QhfKuAgV7GA0RFteWsN0bc2UZ2HLtRkL5j2c12cqtqyWLCBKVCFXQ6M69eT21MfQ6odTGJrDNmgHhLtNINKSf5h8NAneB0njjEHrf-TSvC_98mj9u0yLGq5W6pfSRYlY1grbRulwnrj6ENtmtyqcmGUQwoRfHFvsycTpE07vHoWdOj21D_H_Q8HMxb9TDFyyonEpbztWJs74VcFCc6ZzJAxm2hXIDLqCDXK9GkLftvIP8buu7I0ZkcQv0vWwLK36R3gK3WQ-1KsbfInWKdiGqNXycQ9d5X2imSRIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/29983" target="_blank">📅 01:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29981">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXBL_IUrCDnx10h2Y5JlyKyU9D8kd8HBAsq5lUSyRAzBkrmZnJ3t3oKvQKpcIP2U3oCYNZ90IcrjfPTC7UO2Q9sySHftX_SiAv1gJsvZryoP0maQontbn-oH49_lE91vd23lOMqDexJgIpmhDqknszvhx--vJRZDPphqS77IxBKSKBEmto0P-vMu0ulr62ZATaokIu7l0bx0Hk2dwY0DxrHmzgRkZSiwK5-osx5jRgL4m1pv1hAFwtc6opWZib_zW3qS1TzYgS1NjEZdqs7upTegSBWVdofb-dgw9S8SXYvG85nsAM9-4HqZaZweSHCCRmx5A907tynALMm0sk768Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛جدال آلونسو و شاگردانش با برنتفورد برای بازگشت به کورس صدرنشینی لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/29981" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29980">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw3LnjSjexzwVG1GQTVslvDCtLsmLLVHMWo5K2v3ktk38CGPIqs4vwRXFXiEgxShVRpEF4O_2CGMcmkdymY8ZIXcVBfNHKa7GppvUKA6an2xuyDrCayfhZ04R91wvpj9T6X_jsvkTs9gCnSYMQsscpIekkC2DZ_sh1Q0pb1Cdo0Kl8o3ZJb3CGpucB8hK13QkKDBISWk20KfZXvxSgVKCRrfK-xcUV-N-R-lRndJcfzMiUu_bThrvb5gDmbfn6rPuFPSkXXwBny_oILV_XL2XV21z0sS0V_au9VEGf66h9yyxunT_hzpssIQfAMMxrdo9UoUCdH1vH7KIcxZ_xUKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازچهل‌‌نهمین‌قهرمانی مسی افسانه‌ای تا برد پرگل یاران اسپالتی در آغاز لیگ‌اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/29980" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29978">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">📊
عملکرد بازیکنان رئال‌مادرید درفصل‌جدید؛ امباپه با 8 گل‌زده و 2 پاس گل برترین بازبکن کهکشانی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/29978" target="_blank">📅 00:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29977">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8GIaB2KtyKqb5EKp2h5_GvplbkBLR7_RNY76XyjItYHotYlH71KSCy6UMK9qmwpLbmqW-hSYjgXfJ9VS9uilsCRBlh71Ammj_EGuu449xV69_RT563vFBuJ5MCKr6tevc4-vJy2PSR1pwFc4b1EfqzAVExIpsF7dFwZXX7cVvX6JRQz_E-MZ4ZhrfFV_hk9-6AQFrnxfvxVyBSsqr38WBqBblW5AyrkuF7bWXKDQNRtb8kCmrkKJuwe6DKuRAQfpgoaBJ-vlMRLkyuC10Gc6lfwXJ8alb3ZkIKdg6HBBjckKgH2VDE-bdYYtBLrqXn2oT_1_8JUmMhvyTE8mB4juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/29977" target="_blank">📅 00:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29976">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVjX750q9KeLL7PfDnn4GCRNL7MhcSobmFmxo-ITFMutZZvFVF-PPhAEvBjeOu10jH65OzwAXfMqEB6xI7PRzX6dvqFBaweKI5spItSFJykZ5oyazLlDROTFE4eDwsvQ_J3-oCEMy2r8A1LzjBC96hvbpWy6ElcM4w0fgQ-1oHMZZ-V34Krum49XePfqpg7kTq_0czjPcZHYHqPcr2ZYggAp2Do8nvsg1tJBT9ED2qyy3E6-mSKRZXOE0FHFUeN-wDX5eQdLnCIQLF4RWFQDo06xlP93UzdxFHDEm-ovWqXDzSGTBS_RPwgpHwWYJkKPZwFzYQq1xVAnPrWNBG4oKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌ امروز؛ رویارویی صیادمنش و لخ‌پوزنان با کریستال پالاس در هفته اول لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/29976" target="_blank">📅 00:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29975">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGTkeCqEYVML6Es8klr-6asAnJc5snq_IrQJQNvqTxSZB-xIfnbL2MdTYwiHfJQI_VxGKL_8E9sYJ_8YU4rVPOmf22cpIkXhsD7lUx-R4OvmME4y8UjF2sSZY3-nHtrn-CFUtHzOruTF3f44hWKpPfOmLSAJxqGBbMyb4ndYFG-KEvUbSsHktQF0us5sPKtmF0_f0xRhOz6KiD58aSN4-ULpdBhuXjOT1mMW0-esV8e-nRs0nopuBc5xXB-TTs_ICrlZYukrxR6l_oY2U4UOxQTSr1mst53WXTvzQr_PPFIoZAWNHRLAsrgcDgaS9FNLOabL4kSseV5VkJAIxLvspQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این پست برای رفقایی که بدنسازی کار میکنند؛
ویتامین‌ها و مکمل‌های‌مهم برای وررزشکاران در کنار یک تمرین خوب برای ساختن یک بدن حرفه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/29975" target="_blank">📅 00:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29974">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPubMdc2m7P3qNULK0jN9-HuagsNko8tbQi3aT98TUS2LYumkjiHP9dlu5SrK6-p_d-ivPc6f8YO0AbWC1MEUKq4XXP-gi0w06vBKpylxziFjyQXAFHT6_ObXdGEt3LbqOaSO3ATYEXdtOsk7eN5Po1gbrq5VstTnVWxh_obczQUz8Go5flI_HvZ4d34btLsfhr-jiuPGV1AV69Xt8Tn6H3Fh7frQXBxpT7JyzEB-eD6PtaoJRZtLnr7j72M8qwDFpa365JBvwE1WtzdFg7TnEH2_lSnG9uauBZ6wf74VTYW5UnDgaI8uX-rF1qVF7TBd9_ESwbhStOM2z3wk6bPUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/29974" target="_blank">📅 23:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29973">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ala6qJNumOgm7BvrXgwRyRr4pAX-qOC2iOAYBf2d9vk7YICpN9cz7sDfSZery9ShJubi881WGcqUY561kt3sreJRsP5utv8ApLUTFUf3wRB3VwQ38pwoKw21l8ev3wpBZ8ciPR0_JHJJSij0Z0rjHcqxEjin8NnhHqL1spSZ8Nn7ePn51e6WyAOyNY3K8dCK5GF4ENrVKD_gRZ1MS2DnvCt3nvbImTs7SEJbTi6vI-lmO0PgPP3AjCi1CdqHYfh1YXGx7qD0r1D5JY-jPwzVXb3i4umL8XYyEkPhAObZuIul_JnA-yPj8EeRU5yKBcctnNJSQzh8N8VWF7wbkNpC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN
: درصورتیکه‌هانسی‌فلیک امسال تیم بارسلونا رو به‌قهرمانی لیگ قهرمانان اروپا برسونه لاپورتا قراردادش رو سه ساله دیگر تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/29973" target="_blank">📅 23:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29972">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8Zd2aKCp6HtWRs_Gj0JaEhzsftX2ev5A0N-UHEZRis5cyJ7McAozkFRWT8juvGHwhB5xr8We4CdEPHsRb72XA8etEIlJeUTu-lVsp8uzaGlI3L3wBMN1r2i9U4l1Nvhoc7t8RsnkRXJMFfmY9TiF7r2uegvjVCud4PK1YlDLTkt8OvmpAQTkedN3vuPsBQy5uxFG5WQ3ocKI1qS2uy0N7DM0BzBKcjuuRaBQrPGwO8_2EHPIaZDPsKS7WCSs8G9HwvpaTh5Gnt8CTCJrx4285GVf2ecOKgiWH7gpYFp7B8D_MA-bkeSkMq1pVxug0A2aawmZM9fygQ0AWVDJ_QDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نوزدهمین‌دوره‌لیگ‌برتر فوتبال زنان از فردا رسما آغاز می‌شود. رقاب‌هایی که به‌نظر می‌رسد با حضور تیم‌های اسم‌و‌رسم‌دار زیباتر از همیشه دنبال شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/29972" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29971">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QB4Afa2ED13-pue830vGAX40wBga6z8us0GtWlz1yj00hz19lomv5Pyu3mx6xjL7UzifdMvkcxeUcSbX-BgBzTvT2rHbtf3cy0QgBHaNum8dTjYdwjptICIGdgfHvDmMi1YQbrNzVxAhoEuQaDuOnhDEFj6GpTscMLK-WzKoN5wN3oH9J5rY6TnUbejChq7n69E4kyTFJHyWrt8WnTZ02gf1RTct85teOQOYjLv8KjphJrYSDc2jQs25qDa1L6e-Rk6jddN8YqulKj1mDAMwdmUUBwedBAJNmc3KZoDj7OH9ucUyG4l1wZ8Ta8u6s-JwsBgAuyOGikufyIhW5YF-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29971" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29970">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPH9wkPP6OPuXqLdeYB3fuWS3-qx_VLjbFUktcrOyuSJMwKbzNi3b1s8NOiKyXcJnPtOr_nf9Sgfvg0QqgiSraHOR7FIt800FcIzq5tH_g_NzNi_DoLvUkLUv9Mj9CfpJ5ZRu8nm2xrMKDYOW1hRuD595wdhBNukVUI_kXtHy6OWMPCOTemiaZ88deXYYf_MtaGimpUWfFesGjRNzjpMmjEDF9ER-LaINAGP1c_RBLxi3b9pUedKpnivzeScwq1OZUHGo1K4M2p6PhadPl8tKtV5Iuq1aFUGLTCWF2FekkkWReVffGzNJn5HdfCpRjzp_nf_qJlqh2eCnt3cVw89IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
بعد از پایان مسابقه اینترمیامی مقابل کروز آزول که باقهرمانی‌یاران لئو مسی همراه بود "چیرو" فرزند سوم لئو مسی درحالیکه بعد بازی لئو رو بغل کرده بود،به پدرش لئو گفت: بابا بوی بدی میدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/29970" target="_blank">📅 22:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29969">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372ce8a577.mp4?token=OPMqhgXKFz-l5_p1MmsK-FjEFfk6HhekFl4NS-bI8V37pLTV_DJYB4atTI3VZwvrpX2YXSBMGGZOW0t1-tmCDLS8NQCdRmUwJfd5nXnfzi1RwiVyXhXG4wA92_7Fxn8iprELaZJGMB3hJucinxAp4I0JUsUjC3eEWXTGEkFY24gCPs5ZhWoqRKjC7ynWK78-SCPmbcRdp9cTFM8SCfn-YHO-vXQtkGQ9731sFixkJbmw8wFDmbJsef3jzCbKhkEBPQz0F4BSR7b0_FIi0JpzuhhIvhB3BCTAEjF0uYR2wWqd1jFTYzeUPz3LH6HEKI-t7xqqkQPjh-eXFrwZEzK_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372ce8a577.mp4?token=OPMqhgXKFz-l5_p1MmsK-FjEFfk6HhekFl4NS-bI8V37pLTV_DJYB4atTI3VZwvrpX2YXSBMGGZOW0t1-tmCDLS8NQCdRmUwJfd5nXnfzi1RwiVyXhXG4wA92_7Fxn8iprELaZJGMB3hJucinxAp4I0JUsUjC3eEWXTGEkFY24gCPs5ZhWoqRKjC7ynWK78-SCPmbcRdp9cTFM8SCfn-YHO-vXQtkGQ9731sFixkJbmw8wFDmbJsef3jzCbKhkEBPQz0F4BSR7b0_FIi0JpzuhhIvhB3BCTAEjF0uYR2wWqd1jFTYzeUPz3LH6HEKI-t7xqqkQPjh-eXFrwZEzK_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
بعد از پایان مسابقه اینترمیامی مقابل کروز آزول که باقهرمانی‌یاران لئو مسی همراه بود "چیرو" فرزند سوم لئو مسی درحالیکه بعد بازی لئو رو بغل کرده بود،به پدرش لئو گفت: بابا بوی بدی میدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/29969" target="_blank">📅 22:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29968">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f4c8fa49.mp4?token=ozEdJVPpnepuYghHzUIvHyGB7pfMJtbnG8rKQQ7NWmx3YRPh4FGi4E8vfcAesfU6uRldAWzJvTRY3H499NGBO8L_b8ogOOA1OvXky3zYG6_th7jwb2G2tzJgeAdGcI9bpOJIS8HyNNiFTdabCICN5hyoruANpjkWObZ8bU5dwsju2SDgL_Oe0usWyfv9bdTczyKQIg5-OOihgzAsTnJO5BSEj88-CYMF1JWair2oRJfTlJDMAv97iRCtet5Sx4GGlMQxo2jBXQ8lVA-vqL-rhP7LjQnimX1OLk8cnkX2lrf0rbGJSMu98TLVQBathiRjLP142Pz_zCTw_QKrpN0SiYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f4c8fa49.mp4?token=ozEdJVPpnepuYghHzUIvHyGB7pfMJtbnG8rKQQ7NWmx3YRPh4FGi4E8vfcAesfU6uRldAWzJvTRY3H499NGBO8L_b8ogOOA1OvXky3zYG6_th7jwb2G2tzJgeAdGcI9bpOJIS8HyNNiFTdabCICN5hyoruANpjkWObZ8bU5dwsju2SDgL_Oe0usWyfv9bdTczyKQIg5-OOihgzAsTnJO5BSEj88-CYMF1JWair2oRJfTlJDMAv97iRCtet5Sx4GGlMQxo2jBXQ8lVA-vqL-rhP7LjQnimX1OLk8cnkX2lrf0rbGJSMu98TLVQBathiRjLP142Pz_zCTw_QKrpN0SiYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌انگیز و نوستالژی از تکنیک برگ ریزون نیمارجونیور در دوران حضورش در بارسلونا. اونقدر خفن بود این پسر ویدیوهاش تموم نمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29968" target="_blank">📅 22:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29967">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromver2 vpn</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB-EaVknY2Mh3lZQKME7bRTtCebQX1kVx0d_6iXX28h-ZCckSDLOmMdoi50RI8kFhZCyD3cVZvsCiGXDpd4xMMEDmQEBrOmBVz-dAvll7IHImvSqJW6i2bT8t53PssQ9qQRYDyjeZu9I-It9DGsTNu3Vl0Y0MlDfmjlCreLLssN25w2C7AoBmx34lrK6WpTOG7DHXNJ-Bgv413XfJ0Weak6sQ_yYclhT1M7jgo_nyVMK66J1hGV0-xnx-hucv6mCnLVSmpsYH7Cfj6Yl7Z91qNBWk2wN3ptWMefmja9wrP37Y5vl8SeTHrWlugdxZG0pJSLQage1FC-z7RoXC6MSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط دو هزار تومان!!
🚀
--------------------
همه کانفیگ ها با ضمانت برگشت وجه و پشتیبانی۲۴/۷ تقدیمتون میشن
❤️
💥
دارای IP ثابت
💥
سرعت بالا و اتصال پایدار
💬
تعرفه ها
🔸
سرویس ver2
▫️
30 گیگ — 60,000 تومان
▫️
50 گیگ — 100,000 تومان
▫️
100 گیگ — 200,000 تومان
🔹
نامحدود ver2
▫️
تک کاربر — 180,000 تومان
▫️
دو کاربر — 230,000 تومان
🔸
سرویس ver2 ویژه
▫️
10 گیگ — 30,000 تومان
▫️
20 گیگ — 60,000 تومان
▫️
30 گیگ — 90,000 تومان
▫️
50 گیگ — 125,000 تومان
▫️
100 گیگ — 250,000 تومان
🔹
نامحدود ver2 ویژه
هفتگی:
▫️
تک کاربر — 129,000 تومان
▫️
دو کاربر — 149,000 تومان
▫️
سه کاربر — 169,000 تومان
ماهانه:
▫️
تک کاربر — 240,000 تومان
▫️
دو کاربر — 360,000 تومان
▫️
سه کاربر — 450,000 تومان
🔸
سرویس اختصاصی
▫
5 گیگ — 35,000 تومان
▫️
10 گیگ — 70,000 تومان
▫️
20 گیگ — 120,000 تومان
▫️
30 گیگ — 180,000 تومان
▫️
50 گیگ — 300,000 تومان
▫
100 گیگ — 600,000 تومان
▫
200 گیگ — 1,000,000 تومان
﻿</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/29967" target="_blank">📅 22:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29966">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX3xfYtVFI_VIdEOxjIJw8qsJgi5mzYq-5HrYLmjjLLRS6PcX8HWRT63XdQphlcyoCr5qL_OTj4YTZuQ_tf9KVvhjZcrFVkGQFNVnKxxK_ubA6UMQwJnHGvEOiDMI6uPwCcBr9DImkChgFY9QKbmyCtmOCxKhMEA4bVFg3bGBfe2s4bBS2SyV23eC1KLxTHfuv3bra9BzVW1xu-OScbzVkc7wuuY_lpjOc1VCxnEbrh-r2ugAsu-a1JwWzoX3Ep9pIAcJJo0-n4ihq_bcZBKtzmcEHu4x1JbjM5fbVUVy1aHBjJWavo2qN-8LEUV2l8V03ySMN3PDSDCobVgp5aOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/29966" target="_blank">📅 22:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29965">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKmd0x3SvhpvfZU3XMArG8DLcRXaon2CeJ3RqmUkhbdr-yFsOdvtFpW8iZkZmth6haPrZM2DE5VJx4SUvn7zKEP5VlN17Nc7Wkaa3G6Zl60BewoWFfqiPnORNurGkGPCZDZST_aRJAs2pC6cKH5v7i0Zw_yrRe7b_y7MJ2irlBRxAYXZCStxahVniGpgQ3fS-haWacd7gYc9fc3s9gBaooHlSByg1A53OlSegiBP6S7l4N-yxW4K3JO56zA8sVepX2oqTgp0fpsp53Qt6B6C-UvkGVWUm97sdcMbCPwbeNFHZ4HaBDjacCt6ESySgw82PT27OyIVfb5KsCRPSsrAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک‌تعدادقهرمانی‌ستاره‌هایی‌که‌بیشترین تعداد جام رو در کل دوران حرفه‌ایشون بدست آورده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29965" target="_blank">📅 21:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29964">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojt9KO6jkgZXp1S-wlQCBPALBXr5ayh4Zjztbl-A0E6KJnY19ML3w96KQhbp5UZ4oq3h-ymdkeMSZPUgteLOQRHxYXJhBFNCQY2dk0vjt5he6y7b_2Y7BVK8YboCJ8Vu2krOZbHC_ujex10iVlc7bdECP31IdFmXwOMCDGRDsO7hv0TDmGIVoRY8rMC02lEXvRvwXWhehcGxL50lAS9SBC_fgli6DZ5har__NQTZMlOpx-rLuNv6rlMw2AzuGDK7Foamap7SG9p8pIBp-BFqceCEsqAGue24rrFFp-WDZ7eRyy9nJuExrjm3N3PZu-mjc8xcZGr37zOtV5IMD3w81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29964" target="_blank">📅 21:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29963">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_QerDCJn-JNhONgvGs4AS0Y3JaB9zsr62aTqNSwp3OEZJJKauB_05hZeqiOZqfWMJxUs3cT6ui1TCxmbpmPG7R79qO-nm_gXWKhIAvCR62dnsQa5kiG-KTDTd3CPRp3WKRVU5Rp0KUH2KY2twedJ89bXYe__fRExVaBNt-QXLIwuX92D8dw18SPCNTAVrgtXLIAgrq0DLrHG_--0nrSl22NFBgRgm72IypjHlcbbI2X_xq-O62AtyMe6iN0xCFeG711_-SskGGI2RSEoCnzw6ExIykIsMRNpPNuMMiX1huonJDV8-4a6waIhGiVV268wCYxDMWUCzKEJEOYpfajyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علیرضا بیرانوند دروازه‌بان ملی‌پوش تراکتور قبل از اعزام به خدمت از تیم تراکتور آفر تمدید قرار داد سه ساله‌دریافتی‌کرده. درصورتیکه بیرو به‌این آفر پاسخ منفی بدهد بعداز خدمت بازیکن آزاد به حساب خواهد آمد و به هر تیمی که بخواهد میتواند برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29963" target="_blank">📅 21:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29962">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbMknA5fmDlBuIWZYfbN1S-nDR2ijNZEVv_Qc0G4nKbjdeulIUilWx7g225bxKl5EMZb2KB_NYY8rcUOv3-1PJGu7ofv49q2LW4AIE1hgSIcoYGCMtz5obRtxxGnJLtNUFM2ys1Y3PO8LpIgrv1AFleD9qhTpBqqL3DYu2sdKwUPBc5QwiGDlaB4KfTc_2Rwy6fk8Hdj7RggeRNWH4jkHumy5QI3DQyMGEV2a5ydbs7Ayu12zS0UTc83y0DczTwG8PAlu29AhPVsOMqPdVYRja07E9MUyECHsszlRDgOuNJ-9ILyOc_nXC7dh4PGVkOqIIdbtsl68kLFezkg57Alfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه میلان بعد انکونکو؛ ساموئل ریچی ستاره جوان خود را با قراردادی قرضی تا پایان فصل به کومو داد. ایجنت ریچی پارتنرشه که خبرنگار شبکه ایتالیایی DAZN نیز هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29962" target="_blank">📅 20:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29961">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2ioLJxJkeYuCdbAMwV23D0qG-SaOHdn3dhAzehkRdPqxYmsjWGCn91K8Mhz-bFSRrSaFWVv24nQay2goO_Jn6toFoxcEXWcCBy7gocv4krK8meGdqLkBVUd9GgmFAUHjPd8Gd33L9bbg7s1eA48jRKdN2Y8DZyk_KmBAnV4wdtTyvQLUC0jlIbI23jIJ2oljzSLFdTUHZZfpv0BlGdWHtrhOJh8h1SuvJmBkHGmsM_MQ85dXgcx5cG-JUFNNEBEkShEXy9PyMQ8mHM1bfEVRljYdrmVseCNeShJNebhmzYzc59hpasT-mLHqZC6E2TjpfforY6qqX60vVUUhTNjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگهداری درست از کنسول بازی، عمرش رو بیشتر می‌کنه! اگه داری این‌نکات رو رعایت کن و قدرش رو بدون. الان‌شده‌حدود 300 تومن. دوهفته‌دیگه 400.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29961" target="_blank">📅 20:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29960">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE8pGjYjoRoyxRF5dwouWCHZodhHU2rzXXp9DFWzWyOVLLMxCtIukKjKwWBjYcKbgHf7hIKJtVxrSsLHFpLsbSHCU6PcJFusghswtWBMwTf0VY6LrdjV65IfVsILlFigXYkAecUJbnoMweYYuVaAEKmXpyMoiSCY6xwX5C-MG-O4PlUbLCU3aq6E76f1fAPSBu8P9S5zvZLTH9JTYYCR-v5nk7ZTMRLCrXHUWeD998PeB4bmpBSIfUpYcZiUMGQBUttCQS6tLgQyZrvHMF4oE3b4pd77NdfkiPsD2xJeRP8QWnNXRrBx3Fsw8vtYGbNQCe0ync34gkQwrTLnoAyR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه‌اتلتیک: جی‌جی گابریل ستاره 15 ساله منچستریونایتد تصمیم‌نهایی‌خود را گرفته و بزودی با عقدقراردادی 10 ساله به رئال‌مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29960" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29959">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef9E8x8eO3sMToBkoANjo-aROECWV6C2XqDWUnHfdF3b2WvtHjUnbEekoZIq4BpbBLcGXbFm0WoAgH-8gbmUrbCf2D3o3oDC1hPvh-1iAoiVvWvZSirU01lAwEFP_WnsiAiRqk2HMVexKHblms7JtqmHoZvYdxzcHAH0IhL3ltpZNvdnQFK1HAIbWklB7kmYKBEG6SV1ukH14XUwRz-siEhy0kY7K2Gh2Fy9MLd-60nnGwqwk0F-rr290hKgvKvEpczVi1iBt5NEgRnspOz1M-sReVJxb2fUN2cAkgyOPiSu1ktRISLBRWcvRQ3fZFR9tf69BGXwSx-BgOwEY5Qazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بازیکنان رکوردار بیشترین تعداد جام در کل دوران‌حرفه‌ایشون؛ لیونل مسی با 49 جام بااختلاف پر افتخار ترین بازیکنان تاریخ مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29959" target="_blank">📅 19:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29958">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAemwGuvWj_CXVzEEWBrVqRHshD8vHgniOQ3Ohf8l8YgLYUJZgGE7uuv-zgOrSMxb0CSPoPVvSgxlSMNTQAY4_MrMVKENLL5w6GsLDo-O5bETK-Z68yjP91T_3bNuN3rnGgfoyT5ran6EHd7fZAHSWa9XB2ySaWyFjdI9kG0oqCuXJZkE7ySDXK1jtfmyATBa_pW4OXs93AofBM58cUipT5mgYVC1ibim2CZQKRAC1CvB-wCplb_LWa3oDRb3NljSPVUEFqISk5RKy-sXr5TVd1IWGUH_uAJTBcn3bFQTpI_ohkfPE9soNsUCqXsMbmCknq-ZCK92ObzmJcqqygEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه استقلال قصد داره در پنجره نقل و انتقالات نیم فصل قراردادی‌ جدید به‌مدت سه فصل دیگر با یاسر آسانی فوق ستاره آلبانیایی خود امضا کند. آسانی از طریق مدیربرنامه های خود موافقت خود را برای بستن قرارداد جدید با آبی پوشان…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29958" target="_blank">📅 19:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29957">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMVY2ds2o6kh87PoV1OFCer8eyx8onQaAnpFYsBT5sYOFnXsGkwwN879q9cangozSh_0d2oPIlFGpIELxLboUcagbjz5LDiRGMYHCYXQCGh-SMGTUouEJnmRFr8aPbUAY_hd5C7a-MF0ePXSNx4pGj5-9q-NrASdgZiSAf263YlHPHaLZqhBRjtjx5ySF8Gn3Lk-WuWWoBwR4r5SPBlengeJI_p6Wa3V4xR1-Bx3ThI7ll_Y4uFYb8yPNolucVhi2iNv_UVr-VhPCylLOnhC0SSHSdqEMGqTmhkMpn-Qk0oLbV5DWYoQlfvjGxf9qcEYuwR-h1ynkvW3rkTa1rnQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه پرسپولیس میخواد درپایان جام ملت‌های آسیا برانکو ایوانکوویچ‌سرمربی‌سابق سرخپوشان روبعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29957" target="_blank">📅 19:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29956">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4vfa0Fk2gjRD464R_eZI4Fc6MUp8wBN4iHqmTK7LDZ6560ikkmmQSXDFgz3Hd3Gcl5YVkxPlmaT7F3aX0a73tNyIwa8wdCs22eJKvl1y0czDgVL6Hg-V2QKQCZyT5Ly7mbRsnU_CKn7tOf3R_bEOlNcOCxfvPtD1iASaWZr_mbd-ry9rLFaopQJvINgrTYJx2aHb4usjKMYdWqKUZWi9KITkhgjUa_k_Z89399DlHyWbUokCLKj2rXxg2rpVWrHTuhdp5XjjsW-2KuUmI-Fe7c86E0Wc6ovl4AZ_jMqPjjMuN1vqxjtFNIaOE6ANFDNUpksUH1wCBJ_ACAkjQVeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرد پرافتخار کروات روی نیمکت امارات؛ زلاتکو دالیچ سرمربی‌سابق تیم ملی کرواسی با قراردادی سه ساله هدایت تیم ملی امارات را بر عهده گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29956" target="_blank">📅 18:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29955">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M51WCf6yGIu-qvS_sdXCZEzLv-etimQTrcW-kmpVKf00j093XC-zRqLZAqnvGXFyoyxfnfPCaazuO5ntIF6mYcC-hTD9JE3ZciaDJoHw2kXNrd2Nnp6wH-MJOOHvgHqtX3BC1xQxkc3oW6UVvqbEWdhhq6cVRJxe9pomgaMoAP4rjQ0f81aDhHJUi-8DuZDzLjfIH6KIn4WHAXU2sYq_9C2Hw8Q9iHUB_GYiCpT0VkYRtFGdf1ADyRXIHRHNoOPaENgrXVgix-cpNZmgEmuUrlu47M84jOnReSR4_TXSNEg9OPa6z3enbTWLv5jSUpVYAQ2Piri80wSUs3oMJn1_Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ارزش باشگاه‌های لیگ برتر ایران براساس آخرین اپدیت سایت ترانسفر مارکت؛ پرسپولیس ارزشمند ترین تیم این فصل لیگ برتر ایران لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29955" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29954">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c4dede4f.mp4?token=l4LQvCHEPi-UtytybufBTczHEQfgm6XXmgfzImSulX3e-tBBQ8kuVh07O4T3PBgl3kA_vrRir07QNfYx-S6l5oknHFQDtQFWJoT1xYpXmGDq93CRpZgQOdGYVMLiIFvF2L8LYkb9mco6W2gp6-4CORxjMSjpaUFjhN4oTAjOXzHswPQVT361t3dftEuWUyCWSQdOUw195EhYdNJ6dp_EvDnYDTXfl9WX6-JAmXvKQtfS9vzueIs20IFUwbeL6pGmP7r3M_vxr10BVkaKKR3WSM2BuQ0LU5p4sba7_72H-9rAM3U_3JhEtRUkSOuB7Th1xuUacxfp7v7augWWDwSOCDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c4dede4f.mp4?token=l4LQvCHEPi-UtytybufBTczHEQfgm6XXmgfzImSulX3e-tBBQ8kuVh07O4T3PBgl3kA_vrRir07QNfYx-S6l5oknHFQDtQFWJoT1xYpXmGDq93CRpZgQOdGYVMLiIFvF2L8LYkb9mco6W2gp6-4CORxjMSjpaUFjhN4oTAjOXzHswPQVT361t3dftEuWUyCWSQdOUw195EhYdNJ6dp_EvDnYDTXfl9WX6-JAmXvKQtfS9vzueIs20IFUwbeL6pGmP7r3M_vxr10BVkaKKR3WSM2BuQ0LU5p4sba7_72H-9rAM3U_3JhEtRUkSOuB7Th1xuUacxfp7v7augWWDwSOCDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری عجیب‌وغریب علی فروتن از سکانسی که باعث توقیف کامل برنامه فیتیله‌‌ای‌ ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29954" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29953">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTxtxuZHLtjACiDXqOuHZoicg8mIUaOzRc66oOsjoNAfeIYbJBBrIwfy1sdFFpEoSjzYKKV09bNQiNJl7qJrEK0VXsh_8pLz8yQrQTtlD9GPAlHQZrtZzJ1Gh14GDge_BeQ7weGH3KwbD4uUxdBpGjIBn8vZa-9Du7ht-9XNYuTW1cmvXpuzJYWYK-ajbUE2Kv0XSs_tbcXtKCU3d-4N3043Znft-eoFyvQBfGFaor4ONaXzW_AaXY1_yq3BZ7EhmZ1Aw-hNz5DsA3FTdX8Xro0lcqvHlcCaG19YpFWaenCeeut08rYXJeQthvu4CtyfMa0wqLduutNLBURmtaJ6dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
❗️
❗️
💥
چالش بزرگ پیش بینی
🤩
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🌟
از
🤩
🤩
تا
🤩
🤩
🤩
میلیون ریال جایزه برای پیش بینی های درست
📌
فقط کافیه در طول هفته 500هزارتومن واریزی داشته باشین وقبل از شروع مسابقات به
🤩
🤩
سوال پاسخ بدی با حداقل
🤩
پیش بینی درست شانس برنده شدن داری
🙂
🔜
نتایج برندگان حداکثر تا 48ساعت بعد از پایان مسابقات اعلام میشود.
👀
آماده ای شانس خودتو امتخان کنی
❓
🌐
لینک ورود به پین توتو
🤩
🔗
https://pintoto.xyz
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g25
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29953" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29952">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fItsuduR5kNv2AG_4MK-o62XLyRabhk0HIpkIJV7vzY1393KEBlHBq3RYSSarhqC22UufBCbD1nluWcDKcorxG8X1SvHDik7DWLGCFNZhFopKYJyN0uT9B_zNDdQ437OvOEE8yhVG4iXc3zKXk1e_yIcWcNG7dWMeVnnhtuqRDDyb841Wt_VmvRB7EHjzvtTq5IQdYhvAjk7hw5aVvXWnTFt_nNqTN76PiZUFXz1_WPjE6XKqSwk2NZ-0fZ5oLl1WihOxVm4l9oKBuD2Iu3Cc_vVAWTxjoZie_RMmbwuqG6PmPlFRCc8aAYy4Z1mTS44Rog_Y77Ps6to-v2OWFIQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29952" target="_blank">📅 18:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29951">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8_l9xF2APDNEfU5S8AnTboGA8tqPyZsWxxX5UW9vCXb36oJpZ2sjbQStsNZFof7PdfI5bhKUBHKbKh5FnJmaPXdBtx-qQCIrfgEaXIP6jR44lLW4ImvIh_uwdyG4yiA04Fw1uoYNfbqCVviQrC39sIdzzZ5dY6gO_ubcJxm-zesscG0_ApmB2ic-RRo0c6VJ0hhrqv-Br1X7i74x5_yjj6YRrRMR6essX45UkxRJTNmZ6ONjFOkzLbUFeKTGb36Uwy8rXUkMSVUSQQZWOgmsO6yDcxHFbmYNKUU3oWi27ybqcytmY49zUlU2rrizHMG_vZKy-wbdvfVgf2uR3okAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌سوپرجام اسپانیا
؛ بارسلونا و اتلتیکو روز 13 بهمن‌ساعت 23:30 به مصاف هم میرند. روز بعد همون ساعت رئال باسوسیداد بازی میکنه. برنده این دوبازی مسابقه فینال سوپرکاپ رو برگزار میکنن که روز 17 بهمن ماه ساعت 23:30 برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29951" target="_blank">📅 18:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29950">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZM6h7Cjsdmn1Q0mGSRn0v1auGUfEzA0TSRxuAjBQ-davnbruCpqVwAb879rmO0TZ8Dk6YEXbXuO0cw49EhmTmv_9F9vcVeKR8x7PlY_mE0WXjvRN83YWHQlHrsDgOq4jcX8fD4lpXnqUlqmqdi89_Bszlrb8lr9_HCA5oQzha7cmQqtdvHDvIDdEwAMwVa1vcUVyUu8IsWR_S0hDV6-GywGv3htPwVLF5jg1UdS9ncl9ROhSYZxo7IUooS0watWfGf-1Rts5xc1L-5rkOSJIEyFEOY2fw7uo-36RtAaPYIiP76pszdlveSjV-jZe0dfmPdF4MtqgKJbFCZDtZqHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌پیگیری‌های‌خودراانجام داده و در تلاشه تا علیرضاجهانبخش رو نیم فصل به این تیم ببره. جهانبخش از اول دی ماه سرباز خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29950" target="_blank">📅 17:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29949">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfN7zp2TstFfYhN2B_qZlaT1r2mPOaRQxV7tC_xPXrpgQ1WHWrvBW6yM5kfZr6D4FHgV-UuqdN3U_eYBQv-GZZlCI5QUeLWqBBS3c_ppAgxDZ5PNZ89TYcLMM3qk-TWolDcuEiL3obq5qdUlX27WpZ0kOaMPquuYHcFeOjGt6RezwZk4k4x9ETZWPSC09tQHGzPfQmdtaNHByUdPokmqZV0oz7aom3rFHpmXY30hYtKkHZLebuAnxcbrNyhZVi01FcUBs071rbnhZo9lpur-ZnhEIZnW9eGfYw_hofvZ3SC5-TPv3EbEXgWCUUNU73_B5YE-9p2oYp3sR2OPjPV-hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29949" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29948">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjQH2w6UqlvXWXAaQbrg0zSYS9mb8D47du1FaTGaJnlgxwT7IirPON_r4t_wgLeLC6q26m_GUlxBrU0076Yvz_QVId0R5bUMzzanTcogCVCr1L9oWvPF0Fd4_btLaLQxvfKrnplEwBjDqDeRP1MG_J_MXV8CaG4ykb_AVQU8yI8GVBQPYADZhIV4ZGWg2ncL566W9a6DZLNk3aCdMDbhaEVlQABjPrx2zjRcZ8nwYY4YmN0p2hJlt1QCPGDpEm3m3aoFTc-diTyydfWrQ5KuZ6j775WV1C1Y6HQA9vmDSSYj73XA77lQuNrqXmDhrEtCqy7zv-eVX2KzvXPBYWtDUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29948" target="_blank">📅 16:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29947">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moC9FlXrP6C7oasnBWxInr_zG30hLqB9Ji1_9xm2JC1avbuw-c9-r9V4k2m8o9DDNQ13-uwABxztNqqIjAs6n3LkiVeMytZSxSaPZNnPMGvaZYbnJAuRh_Eb5rUr7ilaEEjGAYbvSr4ZpmUsMTgGQERcOPj9ae-Vbb9Ym7dB2LnfcqV0c_54hMKN8hhuLsNEKNLlovKq3UiK8TVfh3Tk1XLuX8vZEYRElKAXdTpkHyYneKjxYJzC76ClfQT-K5lw0dwoOyX8AvTF5MrnW6t1r3s3IcgFOrO9rEbEPNNY3tRo4ccWr_NA1UU8jltpNsZW6MolxPEkxa0gYamy4L14DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یک‌ایرانی‌مالک‌چلسی‌شد؛ بااعلام‌باشگاه چلسی، شرکت‌های‌گروه سرمایه‌گذاری Clearlake Capital رسما 87درصدسهام چلسی‌راخریداری‌کردند و به‌این ترتیب بهداد اقبالی تاجر ایرانی مرد اول چلسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29947" target="_blank">📅 16:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29946">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5e07abed.mp4?token=B_kevBLot8SdC0c_iDyIutFB6W7G14bvTswa7RhdOgNMPcSDCMJ_0YJvxfqpucK2F32zVjZxplb5ITIjUfUaoyfvRtGRrpGebus7cEI-ISfABzDbiThWDZdsGrvH9UJKM4Oz48A9Pp93TvIPKt8C6wn6hG2hGZiLD1iyetXldqJc4XfJXRpyfyTRh8Nw_cz-Y3jio1erVptsec8YWh6Rk6ylGay9CaKN0yPuYL-Hjtom4sDg0Z96wGj9cBGUWZf6qdXQ0a6pbXIvsbImVUfeRJJULgnjg9g4R9Ip8B-d2OQ-GYIb3aDm3eIiK4HUKq1k7UJr4lFBPBKru_n2sxIinqHPx2W8qPzZQrcLHhDnjjh48js6cWqboLf_NuHq7vL32llZGRWezwLRvwoExxf4NAvinJHpei1Z1rZENmpwO0wIODx4GFGRo6geEhP7a2R9YINl9sPwMuGsp4fPBPRdkvmNEZAkQyq6YLMqjZ8zFy1VQm-CPRVlhTyJutvuIAUxslE5-q7LX1yi1JbEsoZW93E8pcyLgMDSqFbSa0OxMKoPm4iME4g5HRMMnTVWD3S59baRA9__zqq3H4VK8puIVM1P5rOvZu1VFw2iRLFUKVlJDUAMK9CbnbJlRRRt_lHsDRj_orAlJMQ_PU2MgN2GkpDJRfRek-4i5mu49uZ-H2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5e07abed.mp4?token=B_kevBLot8SdC0c_iDyIutFB6W7G14bvTswa7RhdOgNMPcSDCMJ_0YJvxfqpucK2F32zVjZxplb5ITIjUfUaoyfvRtGRrpGebus7cEI-ISfABzDbiThWDZdsGrvH9UJKM4Oz48A9Pp93TvIPKt8C6wn6hG2hGZiLD1iyetXldqJc4XfJXRpyfyTRh8Nw_cz-Y3jio1erVptsec8YWh6Rk6ylGay9CaKN0yPuYL-Hjtom4sDg0Z96wGj9cBGUWZf6qdXQ0a6pbXIvsbImVUfeRJJULgnjg9g4R9Ip8B-d2OQ-GYIb3aDm3eIiK4HUKq1k7UJr4lFBPBKru_n2sxIinqHPx2W8qPzZQrcLHhDnjjh48js6cWqboLf_NuHq7vL32llZGRWezwLRvwoExxf4NAvinJHpei1Z1rZENmpwO0wIODx4GFGRo6geEhP7a2R9YINl9sPwMuGsp4fPBPRdkvmNEZAkQyq6YLMqjZ8zFy1VQm-CPRVlhTyJutvuIAUxslE5-q7LX1yi1JbEsoZW93E8pcyLgMDSqFbSa0OxMKoPm4iME4g5HRMMnTVWD3S59baRA9__zqq3H4VK8puIVM1P5rOvZu1VFw2iRLFUKVlJDUAMK9CbnbJlRRRt_lHsDRj_orAlJMQ_PU2MgN2GkpDJRfRek-4i5mu49uZ-H2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🔴
#تقویم؛ 8 سال پیش در چنین روزی؛ شبی که پرسپولیس، الدحیل را در آزادی شکست داد. 26 شهریور 1397، پرسپولیس‌پس‌از باخت 1-0 در بازی رفت و شکست 1-0 در نیمه اول جدال برگشت، در نیمه دوم سه بار دروازه الدحیل را گشود. سرخ‌ها در مجموع 3-2 پیروزشدند و جشن‌صعود به نیمه‌نهایی…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29946" target="_blank">📅 16:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29945">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABSjwSZKJAjkQsi1JLObxcz5DNtrodKS4LLp09DWbrZatyohwtaqh3DTqjmlDo3rg-BRGcQ7-1VJ_mqMymf3ZMHmtrZfVxg0jPh8jlJe-A-EaiyoP9O0rs6pnuyguTPo2t38KoZPs2vyrR-yw6Tu67SPb263DuBDKWcN8nJouEebguJAgfkyzIXtkCiCzzpjHdYFB8fQ3_dnSVRFq6_IMgfDj2iSvD7OgdQrLVcPWi9ZergFyYgyvOkaV_w9RzeCo2ibaSPVsClHo-Dw5BkQeGxyZBYgUXL_YcO9ZBEez0ljl9dtuQXGMKwe-CrWqRdTNjQl6nXGaThXehbv5r3NVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🔴
#تقویم
؛
8 سال پیش در چنین روزی؛
شبی که پرسپولیس، الدحیل را در آزادی شکست داد. 26 شهریور 1397، پرسپولیس‌پس‌از باخت 1-0 در بازی رفت و شکست 1-0 در نیمه اول جدال برگشت، در نیمه دوم سه بار دروازه الدحیل را گشود. سرخ‌ها در مجموع 3-2 پیروزشدند و جشن‌صعود به نیمه‌نهایی لیگ قهرمانان را در آزادی پر از تماشاگر برپا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29945" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29944">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27095c80f9.mp4?token=pTDAYzCNb29I6aDfEyg5IgX9KhxoqpqS2Y4_nKLvQyh93Mb80SVQGrJpmq3_AgAXMsDqIifKRc5LUREz0sj39uvu58F4uIyFsP4HVmN3gmGqjLXZViLtSByCGmT1GliUdmxdEZ5qvrXD1VZSa9POGhvgCLoNWYUWUjyhEgSVyw_KRY4N6ne-FFLpWykc2sacf1-cgCwVld4v0kHGNeAoASBIqkSFGiu9Dh1f5FMBmxDVj_geMwhTb4AHuebTI1FxciiCNx1KZVgG30IYwkFjxn4eiDe_odlXMEX74hobOGOV4wkcEFDLnsGuiC2uruqVdDbkGEbHjh-Vrs4YXYahJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27095c80f9.mp4?token=pTDAYzCNb29I6aDfEyg5IgX9KhxoqpqS2Y4_nKLvQyh93Mb80SVQGrJpmq3_AgAXMsDqIifKRc5LUREz0sj39uvu58F4uIyFsP4HVmN3gmGqjLXZViLtSByCGmT1GliUdmxdEZ5qvrXD1VZSa9POGhvgCLoNWYUWUjyhEgSVyw_KRY4N6ne-FFLpWykc2sacf1-cgCwVld4v0kHGNeAoASBIqkSFGiu9Dh1f5FMBmxDVj_geMwhTb4AHuebTI1FxciiCNx1KZVgG30IYwkFjxn4eiDe_odlXMEX74hobOGOV4wkcEFDLnsGuiC2uruqVdDbkGEbHjh-Vrs4YXYahJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ خاطره‌‌انگیز و نوستالژی از سوپرگل‌های تماشایی و برگ‌ریزون کریس رونالدو در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29944" target="_blank">📅 15:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29943">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRz8RR-Kv_17rbbpYAXVPNQBqXD15-q8BD8GYM4iiiPrjRDW_1wnH-w8RZRKkvy1GswZk_l5QHOflplCfyeZC186CwjE0x4eQIgsus5vRjTi0k4vPx6JEqlgwlgnS5sRfeG05eBGnqu5xpyluYZcoDB56i8IS31U8J6Hx2DoLpnsEWOeHmse-D1hc3lWNZpnahMLNv2R58YrCWoY9SSj0qT3re45BbZhHbvmaJnKotKDjH8NiF_nEunTmfqzCTZel7wjHev8Pvi5RUGvKhfnjD1tm3lDlc58JneePxGvRg9F0v10unX80X8JocXJg66w9LmvdavYMaPuQ9vzb0C25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29943" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29942">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtesPsw7wncsIl5ZXFQuQGy9XwrbxIgOyxybxFMMPukdVsscm35hLwM-BxP0BNhHxBuuJDkV8_5fMgD4L_CevY8uEmUU3f1NeVhdqgyJ8K5iefg3M2b-QSEIdsuX7ygAFP-gsblZBCvQ5Y5KbgD3N40q1cTE3791SRTOW1R7OrEw4pQJuuH8LBuUWprLMlbJNHjGmoCQHjhzCnNh7b5tj-OTUaNGTkFsFhC8-_tRmJdn-CHcwRkfYvnujRzUI9cYSXR-kXRWLOSTjY1JCXogADmsq63_azPX-7FNe-xhGjL453alJv7OhjB8QyA-TqNOYMahfWgagSn8Ggm72KUP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
از 368 بازیکنی که در یورو 2004 بازی کرده اند 367 نفر بازنشست‌شده‌اند و تنها بازیکنی که هنوز هم پرقدرت ادامه میدهد، کریستیانو رونالدو است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29942" target="_blank">📅 14:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29941">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anA7SZgU6UGk3szxPbgaxJ0rZ8Y_FDmn7IcM-PkIIKFkV-HZCH36vp2jHYBMwikxiCoFNlkL3NMXS7J61KpbBL39Khg10IfOyV_-zUlF55d3jFyJV8y8X5z8kHf3dtLod_ugM6HzLgJSM2dfC5IIt9bgo4ckk2J-w4Pt8bz1s5Bo95SCAKac3O5khLAzFe2UsJ0MF67tHURyR47NITWQLdlgzfXlzLyR6cnmGY7mss9bC8da9ugFbLgliDaEDL9A3eOa_YBA0rGgWSwfoYZJcC1d0v8ivXF9GFShvsrrevWNJ3d2Wr_MK7tccRx0doyPXbhaYlfCPWZQo-IBoyPidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
باشگاه‌پرسپولیس‌بزودی هزینه حق دادرسی که حدود 150 هزار دلاره به CAS پرداخت میکنه و پرونده یاسر آسانی رو به دادگاه عالی ورزش میبره!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29941" target="_blank">📅 13:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29940">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUxexSxL6K_DZB_IbhIQESJKoaobQJzOprAHJuhgzgQr00tPwEfzhqWHxZ36DiugcnJ6Ag153KJaqrphMNz-C9iheUSkfUnQwRtLMfzk0xkwf-n5wNJ-OZIUeh8isd2Js_GCfkcnr-5IvJp9trjhHT4IQPTQ4qrHgJfGjeXh7K2fxAF0Gp9ma4LOnStWfvwdGGeSla2ZXGQKIDCtW-XCrmy3TtbiGwIhWpFe1_Q-QZEQQcgFRJA8EVzqo_LZT3nahG7K1jzzp4q40VjalxzODPQ8lBq9m_g1iP2uhUYvAG4j7cHlyZfo56knaOK2yDjT-qSswLEfrW_DZxWqQNrZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29940" target="_blank">📅 13:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29939">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ab4eVEUGklVeCmLa0ajGfVxMNpnYuQQGpbyI6fHmclUVOBvCXh6VNH3OApwohL9V35pnqDwoFEnax-GzTPuBe2IVIVTh8xVJruQSZyMW_od8KIU4xdyZ6KofmxV5LKSiqWxNWAWItXDjpiUsRT_CPF0nGg7Hfe62a_8HywTEddK2-CuoMIrApNhl7sAmhpkyKS-J6XXx3pqruy_-sYbqD_dyECHiWpn4Vpiuj7ObcgqpFAIn7EEO0LG5MYO2Yv60V1AmUYY43QQwxq0UpB9mlzBU8lss5eXzIdUl2NW9CeAIDuL3zrdoJeoXp8WIshDGIvUbOOSu2PLWkYGivPsByg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29939" target="_blank">📅 13:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29938">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzw-UJTiqM23CxT6bZ-eZGdbHTVbeNwK96NPomA8Nlu0EAiPJyHtP24Kk9z71D_F_blesLq5ZtZX5X0tMQGMrTMEyT9TZGhIVZ25v4okJRdZG-jO_tjOcu6nMl7XrhJPtBNIRbOG8XssYOe9ZX9jxubHZ4500H25N03zSGBh625NmINKxRmC5zgivTJ7wTUMrLloRFs08sHphU6LSnN0DGOW-qUaMuZyLhgurRUQf38MSRW9BmxefBW9J2QPPzKjmzVtUGqrpoH_q1-3VocXl2J-Mg0u2GCYRKyP1YTcXRHFtKQzZC2Oo-OdqYvb3d28DPIy8hsJ2FIqSpj2l8lY_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29938" target="_blank">📅 13:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29937">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTSxklE7fdWCLAQhor72WUJbTXFpCerDZ9GpFKa5aaG3SX9_Sfo0tKIynn_hQep6b4FkStCD2L1oe-XjKJvDsNeKa4Tnp1og7XwDdJ_z4niJ9aMSajGJyMU-kHTuqeoM2IJgwiXryfGWm6gmSebp4azj4XD9Mm4HpJuMKK1D7XRFxfqS27enUiKelfAJP3UmHZlWUNh2DEi2YgxmEua6MvB3OkwsI_qHcDJCrF_jho5rTkyzIUb7ZB1G5x9BI9lY09kc8psEDMIrL08WhYT9X9zLVmqJZ3kGeDHDHnuNld_qRpFdq4lMchIUJ5o7wKRF9R8hdaQbABG0CIHnYhEvUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کمیته انضباطی سازمان لیگ خطاب به مدیران‌باشگاه‌پرسپولیس: قرارداد یاسر آسانی با باشگاه استقلال قانونی ثبت شده. شکایت خود را به دادگاه عالی ورزش ببرید و در آنجا پیگیری کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29937" target="_blank">📅 12:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29936">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0fc3a9a3a.mp4?token=s44SDMYD9kHx1qBGNXNpKNldB5sBmbyZVA4Mv0k2tLpI6xcPRCnp1nY78hoFU7_yxreiyt1tIPBgeyALGaaBt_l0AU0aZtx4_EkZY6wowBZIemhYwSuQzUyyj8mpsePvilJUMilWz3Fg4CnYL2S8C02k6mpIh22cW_O2GtXuiezkJfVAoKZ-BRZZXxpVeAn94e94UhxFmf9gYKATGQJ6-c8vCxRi0ivnQ-wi6HsqXGnjj-GEqLn4cDOdjnugNWuQ5ZqLQnDUFu9W0uYIWN6USELor8HcbsY0ZMtOncyxRKfIbEnxutTHjL2Tm_NEXxR0JVcBVKYCsLeIj62ftBOupoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0fc3a9a3a.mp4?token=s44SDMYD9kHx1qBGNXNpKNldB5sBmbyZVA4Mv0k2tLpI6xcPRCnp1nY78hoFU7_yxreiyt1tIPBgeyALGaaBt_l0AU0aZtx4_EkZY6wowBZIemhYwSuQzUyyj8mpsePvilJUMilWz3Fg4CnYL2S8C02k6mpIh22cW_O2GtXuiezkJfVAoKZ-BRZZXxpVeAn94e94UhxFmf9gYKATGQJ6-c8vCxRi0ivnQ-wi6HsqXGnjj-GEqLn4cDOdjnugNWuQ5ZqLQnDUFu9W0uYIWN6USELor8HcbsY0ZMtOncyxRKfIbEnxutTHjL2Tm_NEXxR0JVcBVKYCsLeIj62ftBOupoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
صحبت‌های دیوید بکهام مالک باشگاه اینتر میامی درباره لیونل مسی بعد از قهرمانی دیشب: ما هنوز باورمون نمیشه که لیونل مسی رو داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29936" target="_blank">📅 12:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29935">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJ57LXQAeRCn02co1i4Udvp3hWStqvJUcxdovPiNaHJULsV8HQyrUrHY2GT-13A508UiwXvqImPf90IFZnmNoEg-DxfVJL_1y7UTEe43-HQCvTJgQC382lk5-vjMJO_cYYmmOlDWxdzO81NYeEDOWgFn22XQ0ZVp2Vum32_8DGjEgpBCo-CqQMTmcua2IRX3o4OwJ8hNxpECPtVH-0PPa9biw7i-ilxn3zcbvKbsSSB4jlUBwRTkEhmU9W3iDI7y_c-PvVxkz9JQWN8jK9-xdk1FG55wwwma5shwO_cV0tCZAgmarEj2gqqRO_TMxcneX_h_HE-hi8kfBMxQBbPJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روبن نوس ستاره‌تیم‌الهلال: کار زشته هواداران التعاون رو هرگزفراموش نمیکنم. اونا ادعای مسلمان بودن میکنند درحالیکه‌به‌کسی که دستش از این دنیا کوتاس رحم نکردند. توصیه‌ من به اونا اینه که دیگر نماز نخونند چون اصلا مورد قبول الله نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29935" target="_blank">📅 12:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29934">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW8X4ZvK4zOpQSHq7zgYvdP8BQW4MGbE4JIV71ceWbF6OIj3rJ-Cm1pBQG4OyspKGlfS117e76RvP1bOzaBV2X7e0HLoQRzjX5XINCOl2xSkIuBfrveGeEuRYl4I9HrrXkHIMvOc4QhjGqaW5d_ClAJ7ntj6-mtZIG672sEsY72IIMO0btj0Xx-CkS3ELT3S7vQAP-kn2C4i3cObu-7LmjQWrt4DHvxcbBwgO6BGloUhpk0KjBomefjK7axK95h6yIgofD5xnTDKcLkWh08s4uzmzsNdpAJgwi7ia1Xi9dSo_FkjzTBDtKOHFv-YlzmFVkXCVBY73xtVNWz3BUXXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29934" target="_blank">📅 11:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29933">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGJryP5bh4B5mQoIyGH_88O43jdRIWx44v9oGs1QNA3iG5ybiNP0yncyOaPGx1N4pWh2JuknJt3dWMTjZj7inJ9X1P40pUqJwIcjX5cvdzBhBx-GmkHTsrfC0jXZy9cNtmYqZuJaKDL6OOofk2kJ0WHNSKQ4lbDLDKSUP0dJ5UP9BvV3dFxYjmUlS35PpKCl9IsG_2cFALbcWbaW5GpJbAs8kmExl3Wb8cGP747s3Ky0oIbwIkRF4O-iQ3x4PKLQWglrgjmq2z4p7xn5ISBOxYcYPZXb8h4cHMpLe1PLQZijuvfGs2-RmDzxgHXZ1NgKGMjnlF5pYs34JVD6nTrWZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29933" target="_blank">📅 11:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29932">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3-6R8QVEVQJUYj3buTDpzEhXGYigmbK88IU94poistC_jxP_ZHy870N5aSw3BP1a1wPSjo4B3VJMQz8KCiloxI7wChbDAgfR1uMYEP1IaaHjlKt6RNFRJOLJJIdi9n5SETS1b3ywIOGjEDymw6-d7gLMW9StATTfsQ6zhHhtY9hZQNi7w5qiaxF1--BR1Gf8dZcoRp0LcJcHiTiJ7rkI86vsP5tU0UKKxYx34OXZ-V5DTa_e_5trZsPcND2X679SdNQE7ZRjK1bLuHhPUaTgLIQxvRUHvSLrYDduURfUOoI3dHey5o2pI2cFwk619oDmzh1FGp0LhKPL9i7qX1CQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29932" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29931">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8zlBlCEnSIxM54bSOsKj26W5HB6tHGKRN-cvonl_BAKzZEeUOYkdSbLPAxLGooNijOYhbbhTTgi6GHWhrrfLljTyWHdkXQwgGqyox-i4RBzqOIOn7xkQ-StdZx38pvhAzLi1k3hUelCOj6-gznqKAYDADVdG5zCROMWV8nu57qcS8518xj19BU7h7emYPq6xA9XZa2mU7C98lGJE6M-0JuL9i4IM0KfLkcpaeryHDek6ugZvxFwMApzuAc6Jx150ndTEvLWyYrGHXajj9h5X9YyIqC2KxTavpl74eLHwMxWmb5GZtnIwuOEB3w6DJFURb9iJow5ca9wov_EOc_gNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جی جی گابریل پدیده 15 ساله منچستریونایتد که در دو راهی رئال مادرید و بارسا قرار گرفته تموم بازیکنان تیم‌رئال‌مادرید رو در اینستاگرام فالو کرد تا نشان بدهد علاقمند به پیوستن به باشگاه‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29931" target="_blank">📅 11:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29930">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8NhW6uZ6JuA-kzRbQbwwkMschEsbwlLVUwov5gQ7wyfra2ruwWTL2QRv82F_vpbACjJuD8DOmH2EDObwpCc4fuoJxD0IcMG3uC8FG_HGVSw8I-BW-X4eRTbPnH0gxB83w2-6C6O4ywLXO9IuTra-ny7mN2yXvW0S0KzStr4_3iQ51Agq8dSI4ABWahNnbsO1QlN9eleLDEVJItym77FIXkvT0OZOpTR8dTDxUamG5q-QzaCU0t-cNvcTZutAf0YGpX5NGfvYsMn1FpCqrBx0xhP3rYSwvSs4Cp5KKmp2qToDjuwhyiN6InutArUY-JoHrSrb6sDV1QUwKtMVZwIHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌لئومسی دربازی‌بامدادامروز اینترمیامی روی پاس گل دیدنی لوئیز سوارز؛ این 929 امین گل کل‌دوران‌حرفه‌‌ای لیونل مسی در مستطیل سبز بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29930" target="_blank">📅 10:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29929">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nwo0pUsnyq5PcrdjnJRMelZ3EAa6F-BbA8nHdf9Rb4AK72SWSoXgM18jOpG66wxh5C7idUKxl1UPPgenlFIkcRvG5aM3tlP5cjtkAt4PWRSjrV_HrphYvdrdklMelQvayMPItjfG84jVWuSmd1PeBm9yF6gmt1ecc2b1krxblUxqnya7QWdCJN5Zl1K604WB38p_UQY93pSzQs1WoemozEfLOgeE_S5xCvbLUgVPkuY37bEt5ZGpTSjqu7SSQ4EGLmumZ2ze9jGbWPu5OirJuW28lGjXWTSOPegF1dZRoio1jiC1EW7pZCPzYPCtZvdOJ-l6I7ZYL7eqy9Os4SFGgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیونل مسی بامداد امروز 49 امین جام خود در کل دوران حرفه‌ایش رو با اینترمیامی بدست آورد. لحظه بالا بردن کاپ قهرمانی توسط لئو مسی همراه با آمار کلی او در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29929" target="_blank">📅 10:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29928">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92dd5a0020.mp4?token=MrzAYJgGJHfMCU7j3vjxsjEP1-AvMY9f6HrZ2ST9OnRv7PJvZO9pq_5feucgwmbYM1lZlGtp-OpptKJNl2pJnvJwbC5AmTNO6WbpF3qAEVTH8hUwMe4HxmfVStJGZhwEfFRdT4ioIh37zl2NTBRffdtMOm422sC3EZ0gVhx3O_oU6x9HsR_O4O8VL2hujN96ZvUqmY4vCzofSYLDgUidbl5FTZ8y6O2tmWiE1z6x5E3Lbm-ylNGO0PobtmIWgHJVnGPt3cwbC5CGkw5mW5Y-F_EJ9u5iU7P2Ds7gPJOJsCaSEac8uhBdrsO0dD0Ss0FlCs7QLY84512XiLtY1stC_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92dd5a0020.mp4?token=MrzAYJgGJHfMCU7j3vjxsjEP1-AvMY9f6HrZ2ST9OnRv7PJvZO9pq_5feucgwmbYM1lZlGtp-OpptKJNl2pJnvJwbC5AmTNO6WbpF3qAEVTH8hUwMe4HxmfVStJGZhwEfFRdT4ioIh37zl2NTBRffdtMOm422sC3EZ0gVhx3O_oU6x9HsR_O4O8VL2hujN96ZvUqmY4vCzofSYLDgUidbl5FTZ8y6O2tmWiE1z6x5E3Lbm-ylNGO0PobtmIWgHJVnGPt3cwbC5CGkw5mW5Y-F_EJ9u5iU7P2Ds7gPJOJsCaSEac8uhBdrsO0dD0Ss0FlCs7QLY84512XiLtY1stC_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇹🇷
کاشته‌دیدنی آردا گولر دربازی این هفته رئال مادرید و شباهت‌آن به‌سوپرگل‌اوزیل درفصل 2012
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29928" target="_blank">📅 10:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29925">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P14w-xlutqkNXsAK1Od-hkNK41tFJ7bcsNif_084waiUxACNJzsIrqBUQPj5y5gXrogT6-uM45XDwUU7xySgevSA7zuAC8o_v_uC3pwkM_fXfmOUE6gkWlJKT-oePczD70M1rV25rl1fco3456UyMaiSpGLt7EaxutGIqYaPlzXhGIXbdmW5cwsUaGYrEe8oQvCrpJ7snN4_Ntx6uMGU-Dm9jxb-tcm_6zEhezvIbmS8KmYFkaoZaIl0khWWgaOQIR5dKgOMaOXmoM-AR4R1dgLPbUneCzfbH0luyNwjNZdyHU1Klz4kzy7oogSsa8n_vfXKBhGuYDmwegtyGnCeng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d0f762e7.mp4?token=pIjPCikpR3XH96b266_cpiYN2V_2sUiBceQ4rH_zBEOudPVJyV3ye8YDruo97oW6kyjJZ9MOu4feQF042TF4wAS0puAns6jQpoNeOjj0UFIOgRKcThwG2MBQMqJDImTYfmDEpMrmv5Bzm1oSbcOC1P8qLIORDOxXZM6mLioY5H-Vm8X_1K8ikGWpVobkcFkx597X090i-F-OfNyq6RQhTCaQWr0Wf1nSjcTyMqvSRVgcPPdkWTTGm6JgLFsqZDEoWOXh1qzMv1oQJ5XhmXZmwpN8NLBr04NKMMDf6de6th1m9x-o5aWlAtuE1HrZHjJdOvN0SQGfehuBlWR2amQ7Zq_2kUMMRZ2PGEtqlbUpawZBMGMvJtLvA_8I1EP5m4-8GFo0vOIA7peLaf-LlNcfr3vFcqmYWO-sM-JkphqxwNX_ZhEp6X_rfuOiSFhUcFAUTBikSjOfawyHhPWjusX-StyNlGcFhLb1E2ihPa-QpoEfVEMyiXn6qlLJX_q5LcdbLGBOpKtE2_IO7hPb5UOiDvuYnqNin9nbQHhWpXFrLCHPJJads-ZOuXElfp1a9VP2_yDWzoOl-ZscONLpUsRyaB_e3cAV3trR_oRABp6mn3pguMXsgipDuz9NVgBLW6NkGRdPeMuFt8efVf8zTkolsTNJkW5qN83EpriqDlcp0us" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d0f762e7.mp4?token=pIjPCikpR3XH96b266_cpiYN2V_2sUiBceQ4rH_zBEOudPVJyV3ye8YDruo97oW6kyjJZ9MOu4feQF042TF4wAS0puAns6jQpoNeOjj0UFIOgRKcThwG2MBQMqJDImTYfmDEpMrmv5Bzm1oSbcOC1P8qLIORDOxXZM6mLioY5H-Vm8X_1K8ikGWpVobkcFkx597X090i-F-OfNyq6RQhTCaQWr0Wf1nSjcTyMqvSRVgcPPdkWTTGm6JgLFsqZDEoWOXh1qzMv1oQJ5XhmXZmwpN8NLBr04NKMMDf6de6th1m9x-o5aWlAtuE1HrZHjJdOvN0SQGfehuBlWR2amQ7Zq_2kUMMRZ2PGEtqlbUpawZBMGMvJtLvA_8I1EP5m4-8GFo0vOIA7peLaf-LlNcfr3vFcqmYWO-sM-JkphqxwNX_ZhEp6X_rfuOiSFhUcFAUTBikSjOfawyHhPWjusX-StyNlGcFhLb1E2ihPa-QpoEfVEMyiXn6qlLJX_q5LcdbLGBOpKtE2_IO7hPb5UOiDvuYnqNin9nbQHhWpXFrLCHPJJads-ZOuXElfp1a9VP2_yDWzoOl-ZscONLpUsRyaB_e3cAV3trR_oRABp6mn3pguMXsgipDuz9NVgBLW6NkGRdPeMuFt8efVf8zTkolsTNJkW5qN83EpriqDlcp0us" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌لئومسی دربازی‌بامدادامروز اینترمیامی روی پاس گل دیدنی لوئیز سوارز؛ این 929 امین گل کل‌دوران‌حرفه‌‌ای لیونل مسی در مستطیل سبز بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29925" target="_blank">📅 10:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29924">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njA_bIh9kOv4QnWstLXRnGlM-Ltz2xSr_wJahXsxsiE6JyKNWFsAD777zR-wNQCyJjKuZyx4yvmROyXt-eT2sW4MDqjnK8n23hBWC3Rns_1UWwVx8Fhs9KiIprUqmkFeuJuRysVmah1RmeAQfux6JTFROwACwdxquZ-MZSyaMyoaYY13sF7IUHbvctfI9R_LEI-qojpE_rQuRrabR-AAiCCmp_R9ldcBxB9WteZs35Jh8TykjeYuW5iR1OxoD9U_eqyJB-XbQjzn0Jy8PaecwIgKzmIeh1UInjkX7Cm-GOlqNnpsX2S86hL3mBM6g-ySKbLCL2eQrCU_oNSK1F-n_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یک‌ایرانی‌مالک‌چلسی‌شد
؛ بااعلام‌باشگاه چلسی، شرکت‌های‌گروه سرمایه‌گذاری Clearlake Capital رسما 87درصدسهام چلسی‌راخریداری‌کردند و به‌این ترتیب بهداد اقبالی تاجر ایرانی مرد اول چلسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29924" target="_blank">📅 09:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29922">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📊
یازده گلزن برتر تاریخ فوتبال؛ 21 گل تا رکورد تاریخی‌کریس‌رونالدو برای‌رسیدن‌به 1000 گل‌زده در کل دوران حرفه‌ایش؛ لیونل مسی هم این هفته 928 امین گل کل دوران حرفه‌ایش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29922" target="_blank">📅 09:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29921">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
کریم آدیمی ستاره‌جوان بارسا دیروز سومین گل خود را برای آبی‌اناری‌ها به ثمر رساند او در این شش مسابقه‌برای بارسا 3 گل و یک‌پاس‌گل به ثبت رسانده حالا پارتنر آدیمی با یه کامنت به یان دیومانده خرید 140 میلیون یورویی رئال که این فصل اکثرا نیمکت نشین بوده تیکه‌انداخته.…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29921" target="_blank">📅 09:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29920">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇪🇸
👤
در هفته‌ششم‌ لالیگا؛ بارسلوناِ فلیک با نتیجه درخشان و پرگل هفت بر دو راسینگ سانتاندر در هم کوبید؛ 6 مسابقه، 6 پیروزی، 34 گل زده، 7 گل زده؛ عملکرد استثنایی شاگردان فلیک در این فصل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29920" target="_blank">📅 01:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29918">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn-KUsYfQWKrp856V0vq0eKa64zIACESQZcA6-m1xVMMw1HucTP03Z1Id-b7R6IfpuQExaSVliPfpFPQh9KAvUBbF9iqITw0Ycii8USFYy-BQbv6vGAZl1ey0itY5fE04oY2RrZBUBAJare7dJk5w7HQ0CrKKICSR7FXfzICg04dYAHwqBCFcwkycv2uJ01qHLtpfrHhGOq6Jx3ybBZg7-GA7Uc3IQ3dZgMFgScP0lZ6RorBiijTcvgC7-Gpp3zk3GQJhYKmjDNT0X0q9eoLzpul2TSnr-6nPMyshxXjc_7Y9nJTBeSGzoH9NB3ZAwWZx-7FvgPbtu-MSv80h01DyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌ امروز
؛ رویارویی صیادمنش و لخ‌پوزنان با کریستال پالاس در هفته اول لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/29918" target="_blank">📅 01:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29917">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1thfHlv7FzPt_KH0QPQFfG7AxeWMWLHHywuDiOBRnDS_RqrkBm34UPiCnrSRkCPx67b6E5BJonTLR8cehVq1g6-S4JYYFE09I8hhVu9gQ17nm1t4ED8LEkty4jc27rizDWMwFICtTw8IdqgUS4YTqIVb7mRlCN0ScFmOzv-SqoBC-2NZJBS8DIkT4OW1g0olYuKDEwY0DIx2gi0whw5jI2j-FGLaQbMWhZcUYuj9H6024cZe1SIjNr7Vnyspj0y3EDuEKXRggxkViPw8cxppbYTSVGnEDO3-Nkr1BrFHkbUG-nIXoSctuRoIJEpYceji4EOnXQ4roDB5VY-GykV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازکامبک‌برایتون برابر یاران کریک تا برد هفت‌گله بارسایی‌ها و تثبیت صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29917" target="_blank">📅 01:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29915">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mB96AG9TsA1qFYhBnPkv7ax-qcxMDCsoejJS59j0apqqnvr4M1OB_cKWLspzHP9WisBuLKtRNJclmD43iYIOStM9qNNYPfXAz0mJ164zctoxAC0oyU7mfKFWh96H_mSx3SowKus2DzdxPHj7p-_4GdPRCYR65etWMZyJFQcA_r4Dd3Scaa2-q5oNt4oN9a0dl9AQei5yVXXJ52leqacnG1aQn8jLgLougss1Ja7aC2dlY9z3nOMBasTXibfbFzzYhXda_9jZwKK-X_by6Rpu9_V72mlkoWhwO8wry0bJZMFGWXab1UfEhOMtGmZf7B_g75BG61s2VTbYALDnbPigqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPSV5agb3w67nL4klFBc6lHPfZiNkdW5AGMb90yOFTHknSPznQ6YPP5WFrRQwx9W-PUH73DhbPBM0eJ_7uaNvSzazUTdgSmD5ck1xAERM0byNLFDm7XnLvjjcyMuBD70kP_atO1sDfy77zyGaBm6AzlF4Ns2RBtGnRL5crUeODXKqhHTOzgCtezH59BXpg6UVaH4qH_cGuszGRwFdsYTl5KMnoDPA0HjhZ-AplX3wZe8B8-gIGb2uPEJM5dljBYixPEQzlGc3oEWMEDF3sNhUynLpsfTgebadb2CvR9Y4AaH0OyGxi_kqsIcKx9ToW4cZf3db6Rhjx7kmGUa_AU5dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29915" target="_blank">📅 01:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29914">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyURtnYLhuWacHN2GCXp4-1J2mlUS_ZiSe1XDuSzpbl934o501NnQXtmImMIynH0iGcXjQueVPWcCcW74-dxPV9pBGHur1soOkFuvjwFmA_2VpyGDvBoWYifvVBgPh1V8MEGpoxccb8B99fRpaTJNEe6r6Qu9gyS0DFVo7LBDt1usMPTt8uaTDUIWz4YMSHHJefwzc5pyzrZi0MnDVymH-qJ1mEAYzTs6txatKz6OcdYlsqZm2QRIz0azIfZlEC8Dcd25_jMWUdCWFioAbmvCLhmbWFVaRlm0_qJ_jmZVJduFIQVXWvrWYjtFueZLXq2NRM1KcU8me8Rj7DPnStwrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
در هفته‌ششم‌ لالیگا؛ بارسلوناِ فلیک با نتیجه درخشان و پرگل هفت بر دو راسینگ سانتاندر در هم کوبید؛ 6 مسابقه، 6 پیروزی، 34 گل زده، 7 گل زده؛ عملکرد استثنایی شاگردان فلیک در این فصل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/29914" target="_blank">📅 01:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29913">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHZS5dOBJnMNFC01NdAmWOj3pg6l5iMY9l3fZ2UmYfF24qYUs7-im9IoDoNpdEEsJJh1qNAVAyMXeETVjPQxPpu6loOMOWgDjF-d1VWANqjHN3Tx1V2Rq4_4x_hOLMCoe1CbXT1u1aKduoZYiCqQ5SNq_e_5is922FDCIxKK4ICINRNX1C-K-vFVnFoyCtTQq7XM0TV1VbGDAzLSPVe0XaQ0HEYUiyAYSBm3NOi6dI-37qMRpspD0ApMLBZqTEWMxy9RlQsW-Cho_jRUwGZ21EIlfs4y5CDGq7ONDoCGuNb9O69vLQICwZfVxdhIOgnFYjyxhp3hPskZBqeE6Dy1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
دبل تماشایی ژائو کانسلو در زدن سوپرگل در مسابقه امشب بارسلونا با راسینگ سانتاندر در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/29913" target="_blank">📅 01:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29912">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7n65PnJSF6az-7_12Ymmqc3tfUYc1zniGIVTzomgL6J5nNd0MlzlWQPuunifljYISbaTOl3aLVrSJRBXGdTJjjTzuW5T-ZlN--qxsKOT5_ErE5yEX9rKZAL3gpTz7mVI8N_9hAGeJhPGnoLfyoc-9trytPqRXVemLAizvGtGvzA27ooF832z9MHKgAcYhfs--flXSRkVZov-cSD-zSSatEfpIPyoCXVyLJDCtWVJ8aKbgBOsd7Pi_4xzy344GpCH7qvy62c0RM9kXLoxCiwfY9QhQ0LgFUg1wl-pNM11gSTBYG6lIPzDJ_YiQR10hRnsTzvHOH0Q1Slnw0OygT3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
دبل تماشایی ژائو کانسلو در زدن سوپرگل در مسابقه امشب بارسلونا با راسینگ سانتاندر در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29912" target="_blank">📅 01:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29909">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jE5xltzFrn2y_0yV29EuSdjZp3c0ze7_C2b2-rSqRPWEB7d06fsyH8gxpxTQCqPM6rrsSfPf9ZQ0aOTzCuXRfNupGr0TIwfp4DKvse7i_zmTJpCR_ejoCpi7nLCxYWHtW7Drlju8RflArC2bI6Iw0IJlSEh2HmlcAjJSOJMU0xCGpW3QsclO-EcimiQH6RuXjTjzfuASSF5J2hBuQTTcUdLAIPxxf3_iXNazfvBeiFZjIGMoinL2GuTKzxP1drRJbuXueh7amSb7JQIBDELIcpzd-RxC1NuPO4Qhe6qW_AOc-_2oKcoHVOJcBK15lr5JY2x7Z_tvoXhC4twcyCbiMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ic7u1WeboYalO1yI0VGki59LPr48WZkI-__2Y3xxXALdia6YMYyLA5Juix3dPFZeghUhme21oBcr9u5DMm5W0H1EH3wnsubMaRVS9XwIeHRZq5iEDk-Tn4K517FTFtKnUkXIv6Qw5PlFAgPdkpPL-qcYAoukUcgJqOYySIoofD6Lbi8D1qGJfFN_OyqwefSLPQ9VJAvq4AgWH4q5heCumOtPEffXsvpnjRurUXmO-C0NuoFRHkDEjgF98ZMXpArmjAQLZOxf75O3fHd7VF7s9lIG-y1CKmRNuziKBFofpR2-liBnshWi80fz__f0UMLrQQ8GMaC-RnVhXnh7QtgSjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دو دیدارمهم‌امشب؛
حذف عجیب و دور از انتظار شیاطین سرخ از جام اتحادیه با طعم کامبک خوردن و شکست میلانِ روبن اموریم‌مقابل‌بنفیکا درفصل‌جدید لیگ اروپا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/29909" target="_blank">📅 00:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29908">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAypyp5g8-tQ_y1WjWpbBW2RhXxZ9_LerraZO3NoRf9cWL0f5CI39i6u6bEBqStIqMCW9LNcEIkUEEphcZKenIv-HPFtqqiq_v-Hn98RXJyySm_Mkha16h8tLYkFDDBGOWptMEyEp7jN81QLo5uZMf1BLruLuR2qg_cTDfBTDPgF7Qjd2x6iYe-Yk8J04Yjyi3x95zCz6bbg6yb9Trfr-nFIZaWVlA8nKWWBtpyBLvo2oZIGSeu5IbD8xoUKwHUqDituijhoGDW4d-Ub1xsXVgmU9D2K9QliSzYvnbCF8epsPVocDDrEkxVLwJ73bpRtkDWDL9kr5MChlt8WBWqiyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/29908" target="_blank">📅 00:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29907">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk7C2kF9JJrMQBwikTedv8TcQTtimggkSgAr5_jFUSfCd357tuIRUzBh1_R27LxewB4lgGw11R6lziWV-gmr7L9a_u-U8EhhqUQYeb-uj__TiJXgV_f3pVAAMR4fPikA0HHrIWu6tgAM9V7PfssPqg8CiFgTaMeE9Cthz5XpTbqxsJbFhHrFwGOud6UQSDDkSLz5o5KaOutj9qxiTg6PbhFZg70rFnnJzWZDdrYXn8WeA5iiioKnca1qLF-7WPi1sCpb53PS1NOuqxNrYZZEhXO3cgcrDcXzk2RHF4TO4clNLKW7VjWu5-cglAfvVwhIVCF8gHzaTt4os0n1qRRGEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص مهدی‌طارمی و سردار آزمون چیزی که ازنزدیکان این دو شنیدیم درنیم‌فصل به لیگ‌برتر برنمیگردند اما این فصل‌قطعا آخرین فصل‌حضور این دو در لیگ امارات خواهند بود و درپنجره نقل و انتقالات تابستانی سال بعد به لیگ برتر خلیج فارس باز…</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/29907" target="_blank">📅 00:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29906">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP-W8p3wSW2_D3kt-lytuIQ3q8uHWZjNS6akQDmaRyCAFP39PTqqBrbQ6JNIuAh_ZwwDUuDSC2KtPW4HnBOzZRJlCTnwBqyhCpY2APtJsvcSdrATyJ-XzVBP-9WlqZiAiiKOIOxhsB5LYzwaxXnBL8oHiwk3-_SpDAxIonraIdeQTpE_XK7DGTz_cMZaZcPBdLUyK742fZF1Spvn2CuJrvmFNDujFfEboRv9wVWPDVksiZUP5Gd_G5VJa3bTnXoPKaZ_lWCBzSypJRxc9crbRTWKdoN4GT2EjJgyay1XEf0xmC9Aq_UiA-IkvPYdFcJQfNkRwDpmk7PJRTE_gNGaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/29906" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29905">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b56fabc8.mp4?token=pYJfIiIYwi5bLzdNv0C1karQqhMFcD2zzGSgWi0pGhOf1v84akn_6Z0JaGg9xYk3r0P4dqRcQuVBJEzStNttDWga7WT1xtdb3lJwc1ylpE0aZ2LGvOPgzmJQntwFBCANzPVz3ErkdeZ-1XtLJlBmAzBCn4Yd7XFW3aPCxXzBOOlEwuM_YGlF4HQ3Ibceyze2U0kOH0GXCjfP6LFPZ9FhVcqgo2Kz-57fLsbilAocX8oUMaR8YQHA4kR0AZHxhXqkX99MEgG-MIBwLVISuwl-8OIWFbJcXME7L7koRnt5Szn1HBSLeLsNBT96Xf47iO0H_T8B_R4TO8dT9gN_rnxUOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b56fabc8.mp4?token=pYJfIiIYwi5bLzdNv0C1karQqhMFcD2zzGSgWi0pGhOf1v84akn_6Z0JaGg9xYk3r0P4dqRcQuVBJEzStNttDWga7WT1xtdb3lJwc1ylpE0aZ2LGvOPgzmJQntwFBCANzPVz3ErkdeZ-1XtLJlBmAzBCn4Yd7XFW3aPCxXzBOOlEwuM_YGlF4HQ3Ibceyze2U0kOH0GXCjfP6LFPZ9FhVcqgo2Kz-57fLsbilAocX8oUMaR8YQHA4kR0AZHxhXqkX99MEgG-MIBwLVISuwl-8OIWFbJcXME7L7koRnt5Szn1HBSLeLsNBT96Xf47iO0H_T8B_R4TO8dT9gN_rnxUOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
گل‌فوق‌العاده‌دیدنی ژائو کانسلو مدافع راست بارسلونا در بازی امشب آبی اناری ها برابر سانتاندر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/29905" target="_blank">📅 23:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29904">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7cbf3081.mp4?token=aFFlfstS8dQNqdsSe2gqAyfQKIrJXxPT7ESgccoecB4ibMBjEOH8yZizYtJm7SnIuZvwdRiIb0EteOWxH3NpoDnCwBrsia6puSmrP2bgWlL7LjrLYTwva2t90sT9qfj_C8YoqnBcgMG6tdy1BfB6gCIiBtNh4Yo0A-QtC-cWB9TH4T75Ee4tSyMkm6BkAmhohUkd525x8fpR3xtPWW9kXD7aP2mRLyTnzFwGlA-RrwM1Ml_ZwZTji4qmaSN7NJK0HnNpQZKzOYkRXGzbBqvktnaofLF-jPUeZyIYcOX0_lVbJZxjxU5Eo6sD5c1XZQMYi3abokebwJNfIIRERSbsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7cbf3081.mp4?token=aFFlfstS8dQNqdsSe2gqAyfQKIrJXxPT7ESgccoecB4ibMBjEOH8yZizYtJm7SnIuZvwdRiIb0EteOWxH3NpoDnCwBrsia6puSmrP2bgWlL7LjrLYTwva2t90sT9qfj_C8YoqnBcgMG6tdy1BfB6gCIiBtNh4Yo0A-QtC-cWB9TH4T75Ee4tSyMkm6BkAmhohUkd525x8fpR3xtPWW9kXD7aP2mRLyTnzFwGlA-RrwM1Ml_ZwZTji4qmaSN7NJK0HnNpQZKzOYkRXGzbBqvktnaofLF-jPUeZyIYcOX0_lVbJZxjxU5Eo6sD5c1XZQMYi3abokebwJNfIIRERSbsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته ششم لالیگا|شماتیک ترکیب تیم بارسلونا برای دیدار مقابل راسینگ سانتاندر؛ ساعت 23:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/29904" target="_blank">📅 23:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29903">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1JsAjar-6C7C1ps8Q1sQ3YlSAzFQ-lEVaX0mDrPvDJQxA9EXI1Csdfl8HA3kay-bq4tWAXWKCaoJSsTosvkH_on7gkdsukMEFCbx6SyetM0iJR5o1cyKHHy0Jpy-YhPUINe9Qy2jpNBxOFgqTWa45oxND4yZtJEuzDEEiIq-0LVRDhw7jNTBFX_dCS5MKZbps0nkZz5XUwKUI9hB6w_3Wpcg9oFLH9zz6H6PDTSjcYmgb77l-pObVJlRqAQMt9EmJugdGSmdleQEHpsoCcst1Mw9PE3gdQgLPdX84v5jW68HzTJ7f636PUg8NQc36pgVUeA-r9IlJJQJaiueg4x0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/29903" target="_blank">📅 23:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29902">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkdqSYbhgdVWWj-Hg0Y7Zy0sX79ZCIH5FaWswfDKA4ho04R8xmj7KrDp54bw0wEREDPu1PHue7N5IchiIwOoUKZAtJdaKNsYlqOcB0evbo78GbvUBCvZKz2R21_kn791UrYIHq5OhqU4LHFIOWDVPlZ5H1vclQQ_ztVYrxhYaD8sg2H5cY3L5oNUXqk5I_hXSm0gXc0DT8ci6gyNfhZO22kf0ADkjaBHHEc9o0055YTCAwvPM4hKqn6MiZJXNAGen_4EiV82C4D5rX8KDZwAY57Hd1GLlmOzh14wNUWEr2-0ANWK2EGB1tFc0F-O8onmInxe3U4m4cN7085CHAFJDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ مهدی زارع به دلیل مصدومیتی که امروز براش رخ داد2الی4هفته دور از میادین خواهد بود و دیدار با خیبر خرم آباد رو رسما از دست داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29902" target="_blank">📅 22:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29901">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2PYTirp0N1L238vSqRcY5UxDvtO_SeywpLBH6tdA05RJJhhhL5ueJip0AvVGb-qDYyDYaizOK9GD6LUhwxu-Wc0A68yANn6Hv5EsDJfIpS1cl-nEgOYkpyjR8hyuivTjiswaPVG0eTiFA4THMAzyKapODJYZIYr956JiwWGtm4lruo_koQx_aHN5sgDOfzTmNEEdFz-eqE8VBN2wPhovoRvAou-pidnAoEbmNFV4IBYw72aIKzAKZEkncNkQAOgldx3bSoyoN9p1hVRnoxz5pIKOewIYrabMDUjMnBv6BpHSy99u_0TJU7wvYVGmcAUrJcO-iGEaogvrhaclRMeFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇫🇷
فلش‌بک‌بزنیم به UCL فصل 2017
؛ که تیم موناکو بادرخشش‌ودبل‌کیلیان‌امباپه 17 ساله بورسیا دورتموند روشکست داد. تک گل دورتموند هم عثمان دمبله ستاره18ساله و فرانسوی زنبورها بثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29901" target="_blank">📅 22:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29900">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCgmA4eiLvIsxEpeyzdp3AvaebnMChEOd2JQXW4tp6VDFToNvwrkSiAIyfuGvGMjv5vkHoR9mxo0H9OOWlrXWm8eGXApUVLIChHYOZX8cxEpguh7QN34CGrZAQVJCdAwI50uE19nB-gXWVOqB1lvT-fFngM61X9tChU4UXh_GOQwxz9GHbKfMeYCx4lnvtMbV1KZEycuAG9OolSZF5W2u9OhGhcPsTzHqSgYTysE1jxT8Iepqu2FXOyozoVwAox4DH2xEuZY9j4dnTrN1e-d8AHWJd_netIv_WWNLzcUUvEgC704FPi7BanE1yuvD9hFPHQ0lvjYyVKtaKJtE2Zwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش یان دیومانده خرید جدید رئال مادرید به شعار هواداران الچه که دیشب شعار سر میدادند که رئال کثیف ترین تیمه. اینم از حرکت دیومانده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29900" target="_blank">📅 22:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29899">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0h_RyoG2RzdZrPsZvLzfXnTmThYc2zMfiJhzMoWG-FeO1ljGqSxQi_zOwqwJlLoBaojOJ0NxTWmqSioE0kBcuQ-cmY-043jmLBWfAfWDoZgG8T2weXZvrSR0MtE0YdAWXFttDP_nUul5jh4hj1mo55ENSLePEpIkWEOrn4n9gJCczbFul_ci3mrLWLUbHoqfA2xkw1X6GrxKYe2Z0KAPkKOgIVAF2WLZwhhmkOWp-aTs4NJh5srS9RhDEoB4Njqgg-o2c8YZhO8CGHXp-ErPeiqsREn8ujlfU6ZAn7mt5CSPHqZkhCukGM4yLRbhRNWokPWSon3Gx6B_4li-ini_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته ششم لالیگا
|شماتیک ترکیب تیم بارسلونا برای دیدار مقابل راسینگ سانتاندر؛ ساعت 23:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/29899" target="_blank">📅 21:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29898">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1Xh37i0rgBWv7j9Brhx4_KgtYm4HiwXE0hvDpEQ0BHmRheGbHksPftvZCJNT8oig1T3fz1Nhf_IvX9TintoCo7Lam0o_S6BnUqhPRcbqM-jZb16pSSmQCSSY26-FLlxyQYK4ekvOue6bdFZqn5r_k4H1AxTnnRCNveSZBhnQb849905sh6Ug1wpd3IqeTinQDhK1k642qHzVwLMbhuwnNe_ybxU5dq7uKCt1dSWLU3YOyfdwyAijj5IDt0iz6AKCtSDJpUqoGG78OlnpLDZYqSArA9ujkKHLrrJtQi3a3xBbjCG5dfVgzZ2ulyacaNEhe-xSF-C1UP8SmUvy5IR1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/29898" target="_blank">📅 21:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29897">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrVFiKoFt35jk8Xp0Y9EPzPv7RKm08ol4h3AP0rHXxAJM6kJIJVKxgIjxaZmRo4CLXldZBhDe4kY5kpChlKH4Ux7n_BhMcscANXLEtNw-gnBuHGbf6_QL--A9HAED9lsho-QwpeHgWseao7rjosGh4u9g1Mmyhcm0I8KUtfYttKbYXMx5d77tv5192amw5CRUolfMt05xeyhBt7BqCVAYEFfJJMKqDQIseWpJG6wFb9oRV7sLbxZS6MbqwZsWtgnsW2OavI3-LPvQklQLdui1jFhNK39RRoR24eLKhCYPXoawMFB-T9tsi5J_y5oQCYv4fY2E2FUi4uv2T-WNTPgXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ رونمایی باشگاه پرسپولیس از فرشته کریمی خرید جدید خود؛ کریمی از 18 سالگی تاکنون درتیم‌ملی فوتسال حضور داشت و بعد از خدافظی از این رشته به تیم بانوان فوتبال پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29897" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29895">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwzR3Ct_FXW9tlUz97owIXZ_hKflF8Kt4rVWVzej_NwpWo_vQODNqLHsk57MgCi5kQt1pLxvNyMDair2yDZSUSTUYXeoYmWwN__XsA0B_bGZuL_vgrEAJdv7Ja_1_DqwEN_ot3jIuPxhOoPszdMdjZN2z_8wFSxc2Jl2YqZw2u-Jf0v_k4r9mv-iJWpT9WFjwTD4YFxRhGEggsCReSOe2tRpTLPcUfswP6KPmTu6SSwHaRb-1aNSnlxJE8CZpA5mVwKy1kgWChcWCkHoiiPVbibKEkHOK50TbEAHrlxxY7zw-OKwJ44555M9lHSYTryyscZmCOui86CZEFsj5RXPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ یکی‌از مسئولان سازمان لیگ امروز صبح به‌مدیریت‌تراکتور اخطارداده درصورت استفاده ازعلیرضا بیرانوند در بازی با استقلال در هفته هشتم لیگ برتر که روز پنجشنبه 16 مهر ماه برگزار میشود بازی سه‌برصفر به سود آبی‌پوشان میشود. اتفاقی که سال قبل برای سینا خادمپور…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29895" target="_blank">📅 20:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29894">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgmkjNjT3jM7ZUQz7OJvoBKuGK4SZ4IUC8G9FgLj-7kvEEpDj_gZS-tk-2XgZyyZeJcXphFlIBHLtYlOMvBWs5uY2qEZpO7g24ir-9CDJcQ-x1arHyhalU40Zmth915V2LzTEFvCu5dCR75d_tGy2mr9ceWAo-I9BnXYCyqamGHUP3nxYBPlOT0LsJDQNVYnvz2BOYNkx5Dg1hA9YzxyPJmsaaJ_Awiygd0qKELxOnL1MKllzrrTaxE48dSgrWnpUWtBfo2vBlasAcs_vHewS6OOXav1xYvRtqRnpeN6wijFE61qD1V_zcPn5QoqE99LOnPYBLmRKRdTt5lKtjDNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیسی‌هایی‌که درپایان‌فصل قراردادشون به‌پایان‌میرسه: پیام‌نیازمند، امیررضا رفیعی، حسین کنعانی،دنیل‌گرا، مارکوباکیچ،یاسین‌سلمانی، ارونوف، تیوی بیفوما، ایگور سرگیف، علی علیپور؛ در این بین گرا و باکیچ قطعی نیم‌فصل رفتنی‌اند. اورونوف هم احتمالا تموید میکنه.…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29894" target="_blank">📅 20:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29893">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOBHX0Iotuvv7E6I66eH95s1JLA9U6hn-U48dtts-lJAkQAjhG8-U0cqWCdCVtSeaBhk5oS6UJFROjum-UYHBxzCaY3IfjtQ9uBSUxkxesci0srojc97D2-RgYmDUd5s4uE1RPUrKr_fVABOCVW6RoMo6QPmhVNUcP315GHh6mbuCkQ4H5CwiAXX9Ab2xTtLuzq0qZFj3SvYA9s6XP3mpSAOT7rKDR7j1zH3qNShhgU0P0nNA_UJqFIDWqZlCjaAw4kuNtc1QeySr4TgKfvkgJtRwnN5ULiW2DApD6wRnRy2p9-KUhf3YkIZURO89uRwtjuFKM7xw45g6VSbAYvmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
رئیس‌سابق‌اینترمیلان:
سال2012 خواستم به هرشکلی‌که‌شده لیونل‌مسی رو به این تیم بیارم. به او پیشنهادسالانه 500 میلیون یورو دادم و حتی معاون باشگاه رو هم به اسپانیافرستادم‌که او رو راضی کنه که از بارسا به اینتر بیاد اما لئو حتی نامه‌ای که من براش فرستاده بودم رو باز نکرد و آفر رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29893" target="_blank">📅 20:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29892">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ld_EFhn99GeX4R3bFigcKEJ64npwLxVGpHci-DohPyg7Waht2YgdqodZ7jol_faZIL7KZ5VqJWwIetKzueWhr_jSDRcUVikyDedK2F2Avich28aSHQHHqFpOrICVlLXzV2Gf1JG1ZAFuujT-XFaBQroHbaQL9auAi53UeYNzFMNvmqzK8tqV00Ty2Kf6WGsRrl_ZiVWSNeLICKmUN62VeCJ0siB58nXZcyTxZCxf4vcIZPZeb-GAl5-s57_pOejPOLqaWyKDOjU54bUWOBVYyZ7GurKimja5rVQLgRKGKgf0TkthmWSVFVihvUfEw1qRxkl4dz9wZVAfNNd3idCbaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29892" target="_blank">📅 20:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29891">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKwdbMqJDjP5e4Rvqgt3rj6RL9yng118eCg8Lkb2cBVb2TSMLoofuDZ-iIT2Bf0POfVnRQVQkBIugfI25oJ1-SddwozF7_uufl7Io1hUBo2urartGD0fA_6UfYvWVJ21XVSMC9klZ7jGDKSP5Kc8cPbS3smxYaqAY-zxR1nEIht_aV4da04r72ZgGXg9E0fQ1-dcgEd6YH5hrNhOURoHAWDWF4p2EIEgbMMrcMOLbl4ZWZf_DNG1tUNKN-1csuwEPYy0ynMdHov7qOKOQeejvCMLvD4PqkQ227OXGKnUZ5ZRtxQZQ6K8IaliHVawhk8MmkWJarISBT9pm-oLjqP4HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره سوئدی میلان: یه روزی معلم کلاس‌بهمون‌گفت سیگار 15 دقیقه از عمر آدم روکم میکنه منم بهش گفتم کلاس شما 45 دقیقه ازعمر آدم رو کم میکنه اون‌هم‌عصبی‌شد فورا من رو ازکلاس درس اخراج کرد و گفت تو هیچی نمیشی. داشتم میرفتم بیرون که‌بهش‌گفتم…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29891" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29890">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTwy47ovOMtjPP9_sw1Fr0jlPl8EiL_AUclXrDegOb3psGIXj3YlsQNBSkduYvhk8hGyQStg8GJYwx4gxymvAhvg965tx_8shjEp63I9td3ggFPq9RVBSPEi7CeSIM4dULA-5JBhZ27rEO3oJzYPhGY4ahOvlOELV4tJZRJnzn_0KrPVx1Ovs-HsUUuwTztPRUj9AFVVTwsybP_3TyuuJ1V0UCQRCUF28I5bd3dfdexh6hvrMdwFF4kDfE77NIKU9oV1cCZxFWKyaMbnWMH2akbLM50jYc63LPtAR3_XbvdXZcs888y1ec1iNT5MJF3I-0avL_nKwkASRkZIEa2bmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
یوونتوس در نقل‌ و انتقالات پیش فصل؛
سه‌مهاجم‌فصل‌گذشته خود را فروخت و سه مهاجم جدید گرفت. مهاجمان سابق‌یووه این فصل روی هم هفت‌گل‌زده‌اند درحالی مهاجمان جدید بیانکونری در این فصل هنوز موفق به گلزنی در سری‌آ نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29890" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29887">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6txTeDWOtUh_XU8ihMSBAXy08oEG6kYe0yaj_9FG9EP-yYUG49LOEdMscwXvLsHMFrY4fx5KcUmsymclKHW3Uw_-BpabkDYK31QInGhd0b0QnvAsk0t1tDdR3n5jOHXRukStAWWdhsOoGMW5aYN7EUSbl9ErfoqBum7qOOj4IolY_kIRYSHZF1uqcdLLb_rB9xmA0ybVgkRu0NIoO28qIV6QRpxDJNoFqdS3UPW7Q4TkYy0iXYVq3G2s-s3_NMUOfW6iVYIgS2ovj4RdCp3JW6-vhJxxWbeUV-4KYfNAHmhy4z2gXxK5--TLQTwGeUdO05f41gB-RuQOmaNbcp1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
وزیر نیرو در72 ساعت اخیر دوبار با رسانه‌‌ها مصاحبه کرد و گفت دیگر به هیچ عنوان برق خونه‌ها اصلا قطع‌نمیشه. همین‌الان برق‌شمال‌تهران رفت تا دو ساعت دیگه! با خودتونم نمیدونید دقیقا چندچندین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29887" target="_blank">📅 19:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29886">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnXQGtseEVcyWWO1vlPryMUTM89FVqpZTnS5FPl94DR5gu5vD8LOfEe8CqE4kmMP8qDh9_MQMkRaEukHdpLZFXgO-WQkcDtO2mtn52MVKlgpIG000ieXb5jpwgoKXSptv_WMLavmpM7T6ls7HHm1XLV9NxnqgNk3PVvwXp8TUCnUV3HfjG_VYMPYbDvjxPDgt0uZ_3vWoH8k32ixFyGz003yiO1DzLQQc9heOf9E73B1FlUiu5eIKsCJR5q0Azu_f815lYL2jN5_99cVhqWAsdho80VxMcJmpFnAOK1xTuZIbAvpu0sHR3dCSl1EMDzIVXmRj7osWWIZex4NHUVhVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29886" target="_blank">📅 18:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29885">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGAf-yWYoy8b5kkccMB9R_SNNPwRXAPaG2Qkb6LnuHOpC_ho40gMp2Lh31iFnbBuG5VlUn_ljIQSFSb7vN_G86kTSfYDAxyq-uNTizVQEOAkmGGDjj4wWe_ilxesGnw3u1Eqh_bb8gfLj3h_dL1UKcO842ICD8xr3KcF-uLHqER8J4bmldLqDFBMOsCjMYxkCo9plq2EcFa8xYqZ5bh3iYG9ulAz1N5ePwyau2GVYOLYvf9dxQuPUDiOM2xdxYgC4Vj-foNE08t6wrY-adTfYhmbtLYfHkpkp_d5we7s7f4bWqf70uhyZqz0VDEE5B1mQOZEl3y-Iq_Do8OOW1aVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس رونالدو: این زمستون رو نبین ما هم بهاری داشتیم. افسوس که نامه جوانی‌ام طی شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29885" target="_blank">📅 18:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29884">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdnzNV24W8ywtwGRYQxEUYmxjNcnI_VbbgoSonmnloiWCreOwRifQSN6YT2118t5zoyVjm7ngECZNPUJAAh5_LXsXs8TUw7h4Vjp9afOadatrcdAonQPwQiAMU6lEJJiaTLh5ysAlIKTPDTOZQkROevBeJK6IHA04ba0rPfGeQ1ksw1nWVro_EWfxVusRwpLhrXL6HRRfRiyONmVDQM-K_O-wkAfuKrh54KOsjF515yZfNIK36FYubNyGooeE6tcCK-yK6BelKdFwQKArvUgwYBl0P1HtETv-NUj4bN2Fy7w30agYjmARLGvSzFonAPCMtv3rxwZ0_fqeJdSqQHTkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور ازابتدای‌این‌فصل تا کنون 17 موقعیت‌گل‌صدرصدی رو در بازی‌های رئال مادرید از دست داده‌که باعث‌شاکی‌شدن هواداران رئال شده. پرز هفتگی داره 600 هزار دلار به وینی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29884" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29883">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6de055e3c.mp4?token=MnuQmXuuu7A13hkweaIbBUpHAU3s_8dwfiubGyHx6mDnIX9A99d7FjXXdTNyo16uidSMEMaWSrgte3TCaSYTx6g36cj1Ks55CHnUZhQqkDWe6VjdL6HbJqZ_iBIf2aHujA8xESf9rZp3t3SFKa353bvhM2qHX4xKYFAOW9HkDgHhBCruwc5azIAvjdf8weWshNg2azIODj2uGi4LZlpWKwUJw9N0wOpujIVnBJpqAt2N3-PzlHhSYdINMe_k4rhEW68ebB8SEjDyEBg_DdYeqh1hWVCXDF2sGzhaAALuXmObYkVqO4-oQjTmFv0hpHgz911g10RV81TuR4-qNboe1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6de055e3c.mp4?token=MnuQmXuuu7A13hkweaIbBUpHAU3s_8dwfiubGyHx6mDnIX9A99d7FjXXdTNyo16uidSMEMaWSrgte3TCaSYTx6g36cj1Ks55CHnUZhQqkDWe6VjdL6HbJqZ_iBIf2aHujA8xESf9rZp3t3SFKa353bvhM2qHX4xKYFAOW9HkDgHhBCruwc5azIAvjdf8weWshNg2azIODj2uGi4LZlpWKwUJw9N0wOpujIVnBJpqAt2N3-PzlHhSYdINMe_k4rhEW68ebB8SEjDyEBg_DdYeqh1hWVCXDF2sGzhaAALuXmObYkVqO4-oQjTmFv0hpHgz911g10RV81TuR4-qNboe1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق ستاره برزیلی بارسلونا از تو این هایلایت وینیسیوس‌برابرالچه‌حداقل یه هت‌تریک درمیاره. دیگه خیلی داره به "یه‌ورم‌طور" بازی میکنه. دیشب داشتن سه امتیاز بازی رو از دست میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29883" target="_blank">📅 18:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29882">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a7515755.mp4?token=FBEVNONrbOuNBmkZIftHLG6j0KGKCpxO6kQFtzqEuIeu1kvUB9X_8i6SWhNmE2d_VLgtvq39-cAiV4oeuQwTE4izA4bJrTH4v4_nReboY4LDGiVhcYjkPG_nXIZxe2hVPveVkDmAGlqT3yFCxL3DMxi5H-d90wVez-mjxAglTGmc6tax0UYjx-6_tOCaODoRuTH7I0ftirn8NChlQGdFxgIkcnyBxRpG4V97FoV8uTw3xgqkQzhR7gbdzyKIi66GdxVKA2JzRQ9s50JQmjM4_TOotZUu9IhZ1b-hYMqJNX-EUY2xxR4QJKU-M3VdsL0ywr8V2JhpSXmklxSXNtxlNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a7515755.mp4?token=FBEVNONrbOuNBmkZIftHLG6j0KGKCpxO6kQFtzqEuIeu1kvUB9X_8i6SWhNmE2d_VLgtvq39-cAiV4oeuQwTE4izA4bJrTH4v4_nReboY4LDGiVhcYjkPG_nXIZxe2hVPveVkDmAGlqT3yFCxL3DMxi5H-d90wVez-mjxAglTGmc6tax0UYjx-6_tOCaODoRuTH7I0ftirn8NChlQGdFxgIkcnyBxRpG4V97FoV8uTw3xgqkQzhR7gbdzyKIi66GdxVKA2JzRQ9s50JQmjM4_TOotZUu9IhZ1b-hYMqJNX-EUY2xxR4QJKU-M3VdsL0ywr8V2JhpSXmklxSXNtxlNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29882" target="_blank">📅 17:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29881">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14d489d5c.mp4?token=ApH9Mt-dvUt1l-lj-EvgrSMyMPatMFZ2TW77bPJxfTtWu3ogJdCysoEXveniuv_bD7D2NcJFVfbErbdhjNT2uj_kHrDhyxhB2iUOs0Le1-CahqOYwfcQS1l6yFTUiquUdvb0U9_PRdEE-Kt5dpEwKhYVk-LxtOMP7jsK8YnWMgBHdpuY6z6skmlCDcGFrg7YC85kXadTTmEs3aevuEhHyMsreoEfhlrcyRibkmmDQEmAEaLfQnxOcnGClHZbMuY0dTAc-uR86MN2cW328IfQ-oUkKBAZA80Qc2NWMFiUWT_KBbPuVHY2h3h0NEGx45Bmi-0QQS69_6R_MgHeMoAWM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14d489d5c.mp4?token=ApH9Mt-dvUt1l-lj-EvgrSMyMPatMFZ2TW77bPJxfTtWu3ogJdCysoEXveniuv_bD7D2NcJFVfbErbdhjNT2uj_kHrDhyxhB2iUOs0Le1-CahqOYwfcQS1l6yFTUiquUdvb0U9_PRdEE-Kt5dpEwKhYVk-LxtOMP7jsK8YnWMgBHdpuY6z6skmlCDcGFrg7YC85kXadTTmEs3aevuEhHyMsreoEfhlrcyRibkmmDQEmAEaLfQnxOcnGClHZbMuY0dTAc-uR86MN2cW328IfQ-oUkKBAZA80Qc2NWMFiUWT_KBbPuVHY2h3h0NEGx45Bmi-0QQS69_6R_MgHeMoAWM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت
؛ علیرضا بیرانوند، داوود نوشی صوفیانی و فرزین گروسیان سه دروازه‌بانی هستند که تا پایان هفته هفتم لیگ برتر موفق به ثبت پاس گل شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29881" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcLZl1a7I_R8NyyuilP0wlP2omvld5bW-4IjjBfNiWS9wEkXtC2EApm0NHCOopfjRHiBm4RR7NeFwem_AGN-Txa30KoxStSxmW4PJp6LHwXAqpt6dZ9qkcFnjYhWKldDbk2lZxvUmD1Vpl2A_IZqTL-Mf899Or83t96ZNQXyLNkKG6IK-Y_5J9XkjyYh3_wJG2gCa1KfLfAoKHv_KCOF_nwpjsTpQpTCqfIQK-ragrpapSx4yAHlxbZ7FActxSsDimYyNhA8gg1Oq1pTmMqO56gPSOqr6HNI2rkj_2lqy9NfWRyMUPSgJMhXuaSawIAvd6N-EUdf3X5XGbPfjqRJOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره سوئدی میلان:
یه روزی معلم کلاس‌بهمون‌گفت سیگار 15 دقیقه از عمر آدم روکم میکنه منم بهش گفتم کلاس شما 45 دقیقه ازعمر آدم رو کم میکنه اون‌هم‌عصبی‌شد فورا من رو ازکلاس درس اخراج کرد و گفت تو هیچی نمیشی. داشتم میرفتم بیرون که‌بهش‌گفتم روزی کاری میکنم هرجا رفتی با افتخار بگی زلاتان شاگرد من بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29879" target="_blank">📅 16:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29878">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTUvD6ey7hZu_WEIa579x8WkaDVkvJfRbw2IUlyyP6boo9-atKC8uxRNdWv1EyUiN_qFYQnrrgsjAPqLkthXff-ctPEb4MTkjmXN4TY15w8j9PuBAkaNOzT-omUdbR3c-hwKNfAUjqXWCsVqW5gEmDhCM6Z9rhSNxoNR26igX-Gixyk2WOukQuuUmQEWZhlJTd_h-tOP5u01NGOo20Tbm8v5jfU5VKFzq-Uj4QdEwGmc5VuK9GRsUsSD1Pq50_wW7o5uR-ndmABmBL1oUj_XLmohIVdjYX8hLTkZwPj9ctifU0me9vvIiLWIG6BKdGS-1GNqrBAcCzVkVxfAPddOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌معاون‌سازمان‌نظام‌وظیفه؛ از بین قایدی، حسینی، قلی زاده و جهانبخش تنها کاپیتان تیم ملی علیرضت جهانبخش معافیت تحصیلی اش به پایان رسیده و باید تکلیف سربازی‌اش رو روشن کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29878" target="_blank">📅 16:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29877">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La5kOlmDWqYw68GrtT_ttGZNitPhIkGGVYF7eMjmXQfGV6pyDbRW1VHd3Amp3SVI3XLMNVSjBDcgze3go0qIsX4SoO9WpOp92r3XM_w_Le0vErytB7haVRS2_L31z5FMrI15wTEOjye0172bh7bFcMjtnOGUEC54Gmd_85fTRBHb_vcRCIH01658qqAq76eHtZQLvOolB635-EpqkR6bz3p36rGOIz-QH_pfX6BorYQBFMNsUH6e7DT40Or09t3_SdTBVbyCAa7UXZ-uEIQQwX8F59Q6AYtX8eLM2tZNbUwErB0MJPGT1Va9hQsOKaqI88S4NyyFpOTK_f2IW1Qo3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ اگر یک ستاره هر فصل به مدت 19 سال متوالی 50 گل بثمر برساند درمجموع 950 گل خواهدداشت. ولی‌کریستیانو رونالدو: 979 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29877" target="_blank">📅 16:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29876">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9OFNPDvalDWgaBuOfRkooSMBdJ3I6VoWew9XaAFO46olRCkE3xsAtKeP1TruxjOJbIajw1iHkpIgWM_wQrBGNYh_ATjsWf37-YW54BwMBzANdJ6dUN_h1MCoyAxQ7YUQJ4Q-YZHNMhMSa9KjxqAeCQ015tdt_eIk7F9XjLiRInDS8MFR7uGBPhQ4QnVV5i79M3OOG6x1WA17DBd1a3dFT9mfHHvv-36X5ShJpFtyBvcLc-DhHMlgTCE3icJ_mfMvT8Gt_cUu0pj9_p8ysNP7cQZx-TA6pEvWkoAfeJs1vfaplweiSTJPdUrOWL-pR74EIJ-XtMxE-_8-wwkGfXTaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لیونل مسی
🆚
کریس رونالدو با پیراهن دوتیم‌آرژانتین و پرتغال به مناسبت خدافطی فوق ستاره آرژانتینی تاریخ از دنیای مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29876" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
