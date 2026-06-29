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
<img src="https://cdn4.telesco.pe/file/KQYllhrq5fquFtHCl-q3zQgK6mHyFRITxhPfTjZAVFfEZxjL5smCcAsz8EuTtYbMnZoqBTW9beNEJdLakE6fiB2sox75YXmlda737VXHmtfPUH1khrPvscjX6W5fIxMnXHtaszLHO_QSeMSxyPpnaA7ThK6IdDznx9KKY3E87D3kIbWk2dhgeDXuo1Dd6qWtUjqfXa_Fj9O2vHHdraHj7EKGhZRLgCKNQLvMAJNJDK1g8YOIrVCjTXVph6WRw0BVEoA4CHwCvtKlT6F-UQwbJe2BG1Bg18qrPDNY3gGYWeWmiNT9Sje-6VnaYHNd2t7tZBzDg6iTNDj8aEN2Lh3-Kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 345K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 13:34:21</div>
<hr>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=ajffm4VdZssihP7gUVfxYmISQyX--02MrPAWemTGS3eO4KzcZDCNop5oBNLzZ0OQmKzOFRlxdLDbM_yUihF5zH0OpK5L5wDXHzo7zDkZP6iX4tmRE8wUhYUAEng9_K6aNaLuD9mpyffNIWTlMi-P9jvc7JytTjlHO0JqaObyADDwuVV0jGH6OvfPFZ8gWH9lI3YN7Ns4KiT80bEqZrXTtwKVXgnrfoRatFz_F3OT2HHMmAzxtG_d7FlSb4gAtHjb39Ginxso0pkcQNDIekSiTD0bY8LdEl3HYhxkXyP3Fy0A6AKGe00xNaepqCJj3FzEmAvq9dQrHP3UzkRcXoAHbB2xX39BxN8Kw6ruFed-Sn0RfRbzUEo__aXXKl2ETK4UAjP9XLr5zwN2e9JYoHjn3mwTtz_ywtnRHtW8Oa3w_R3XBLQ9m564LQiKRVhMIs9pfRpD94lRki-zBt3ytzBU_q2PI5b8pdS4F78YPg4492WDPCiVKrpNJWSf7xg1pwe5-AeU9P6mcj3ewWZryuedKUW8ImdLRSC6_WH2S5bGY4VeyJq1zbeahDPtKf2vbYEBEAFbJLjzvU3Rj5sU7dPNNajIfjRkOD-6F1tU_B1VfQ3bS2zwG6ZfrcAX4377h7BbmFz8EDDpJCMUJZXEiKLWUQKAAygHEBb5FBEKJqCmKc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=ajffm4VdZssihP7gUVfxYmISQyX--02MrPAWemTGS3eO4KzcZDCNop5oBNLzZ0OQmKzOFRlxdLDbM_yUihF5zH0OpK5L5wDXHzo7zDkZP6iX4tmRE8wUhYUAEng9_K6aNaLuD9mpyffNIWTlMi-P9jvc7JytTjlHO0JqaObyADDwuVV0jGH6OvfPFZ8gWH9lI3YN7Ns4KiT80bEqZrXTtwKVXgnrfoRatFz_F3OT2HHMmAzxtG_d7FlSb4gAtHjb39Ginxso0pkcQNDIekSiTD0bY8LdEl3HYhxkXyP3Fy0A6AKGe00xNaepqCJj3FzEmAvq9dQrHP3UzkRcXoAHbB2xX39BxN8Kw6ruFed-Sn0RfRbzUEo__aXXKl2ETK4UAjP9XLr5zwN2e9JYoHjn3mwTtz_ywtnRHtW8Oa3w_R3XBLQ9m564LQiKRVhMIs9pfRpD94lRki-zBt3ytzBU_q2PI5b8pdS4F78YPg4492WDPCiVKrpNJWSf7xg1pwe5-AeU9P6mcj3ewWZryuedKUW8ImdLRSC6_WH2S5bGY4VeyJq1zbeahDPtKf2vbYEBEAFbJLjzvU3Rj5sU7dPNNajIfjRkOD-6F1tU_B1VfQ3bS2zwG6ZfrcAX4377h7BbmFz8EDDpJCMUJZXEiKLWUQKAAygHEBb5FBEKJqCmKc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/persiana_Soccer/24602" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24601">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB20u6QVJbVe94RuDRVGbosyI03CIttM6flA36ejQlFiRw8kdY9TEOsMuPB-OX263c2-civ7U25TkpeFLp81xwbCr7P6jvzvGkkyPGsXlmM54_t-z83B4O1_efQA3gppfHOs-vgmk13IKg8JA0r-5d5FUq2mzRW4QYod99oo1UlSeJrnDYcIfQbwsNt2cRGajL_xyGVxOrJ8OhxE8QhCw9ZrW9XzJok7lvpbfsy46KfCXYQofu-fG9ctjWBrZ4yf-77M8vkJfrOCS_0tJ8PLBlEQv0-IAegJ_Vl4lSCqXLqt-H8D4cHYIhXzbAyPhA1kWP8CgVWZ6rDZE-VlXzMDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/24601" target="_blank">📅 13:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24600">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=INcHkPvSgXrybGzl2xs0ufg9XPJ7s0jmITlvwIeEZ6xzkTzisyjq3_jd0j6hh9C-Wb73vv_HYrC7AHKvLtc8oECUNSKIqU6qTTiRt6K0Ro6-UEwTsDc1kiSGmaUXkXe6_eKjxlIEoShWEWo1c7JXKkvPANoTtU_EEweZehwYuYpah6V1GUodkFDVZTvfZmtoq7IAI2m0kRXIX6wFA7vxIIezlrvUJ_Jqy9OAC3vYcL2CPc06DW68q8psDky8PPlEiDW2MkPue13j4rY6JA8mJJdZwS1a0IyUu_Dk4UKgrBDWLPAw0pcmCqT0wWm7whXrwnumNvJPzaAup02xctXuRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=INcHkPvSgXrybGzl2xs0ufg9XPJ7s0jmITlvwIeEZ6xzkTzisyjq3_jd0j6hh9C-Wb73vv_HYrC7AHKvLtc8oECUNSKIqU6qTTiRt6K0Ro6-UEwTsDc1kiSGmaUXkXe6_eKjxlIEoShWEWo1c7JXKkvPANoTtU_EEweZehwYuYpah6V1GUodkFDVZTvfZmtoq7IAI2m0kRXIX6wFA7vxIIezlrvUJ_Jqy9OAC3vYcL2CPc06DW68q8psDky8PPlEiDW2MkPue13j4rY6JA8mJJdZwS1a0IyUu_Dk4UKgrBDWLPAw0pcmCqT0wWm7whXrwnumNvJPzaAup02xctXuRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌مناسبت‌دیدارحساس امشب؛
24 سال پیش، فوتبالیست‌ها رؤیایی را به‌تصویرکشید که میلیون‌ها نفر باآن‌بزرگ‌شدند؛ نبرد دو تیم ژاپن و برزیل، جایی که هیچ چیزی غیرممکن نبود. «رویای ژاپنی» فقط یک مسابقه نبود؛ یادآوری این بود که با باور، حتی بزرگ‌ترین غول‌های فوتبال هم شکست‌دادنی‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/24600" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24599">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATdGWwg_yMwVuKwSWuoiGvmNvJcLjjpEkMvPF7PfXt8huXxyfW5bqKsMhyEZ1MapHShOx-XUlcfM5W73HtE8wJr_O0uTfqQQ8vFasLY1Gb3fyyXhJlLquNZCYBs9nn-xkyg2zDY-N0cLHKuEcZvSf5LkqR2bAvkniJPOyoEYf-I_OrsGJp1XVpv6otACyBUvWgDvglcKST-SHOaR2GfdoXQW7RJ7OCwMc4AoXS6sjNu58-k9o3b2YVp5K3xgMWIFO8YNCvZHNBuBA8tMlvzQeUVRw_vvyPaR_1ee3oi2Xo_otL-0gdqg9czGL1HGCeDoqNN8Al-Th9YuGMBq0Tct1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/24599" target="_blank">📅 12:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24598">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMTYZZdQgaurSEknHtllWBjMizYTJD9rEReN3Db95CGfiVWrWgfMm-74da8ChKu2E4qAps7GWL_Od4UPKwMUyzJ0oz5HLovRsraljYs9DkyujMNMTrERkEuZic44gtdsoD_FNLLYd8Zh3pre2-kQwbGuDzV1-4KyLoIOqnHea3HjQpNI8l0M4kItbIVa1V5Iv-J6cLVOBDH2tvzKLMt9ItF0_vyYKZTG7xnig_kXPgz_AiPEZe14bYzGo0u6nB0alOUj5dES1-HspzR-HMZ07uKm76jKlra1PffA4n-1-dhpWQZjBfERGX_fulGkpPYUP9r2SvBe8SmpJcWvVnh0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛
پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24598" target="_blank">📅 12:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24597">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDKHmGShm8GGzCk0aBco3NUKTMPQQ3S5GVLMQ7xCyiCzgSOI3UDd7KuNKRqFfPV_42SFzL_eOry0QV990bmjv9N_G614dJtSXz1LXFBdesWSWdMr2bEmc7DGfIReOTQeIrnzLyJkq7aCDsc9xDtXIc4aaEGRfcieYG4YzVKhiIY8AUi_Sj0wKJ10Lh1RD0Ln7lptehAsp48yuYS-yjupTtlhX2aR7MFwZaisCQ6_iD6TJbZVdPQxFh6lzNP4F3YdXsZsviqCl0Y7HV45nkH3tEPLL7jTVyW3rAleYYk54ei3QAH1Cs4VKWm2_PtzQJT64J2Mw_P23t7RDcXb3wejHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا
#فوری
؛
طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/24597" target="_blank">📅 11:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBpf5t5Zlgm1YMNNNiZCKuK3oNgA7cwZlE23T0U1NE6v3MBCtEsc1SXPhvRHJ6JuLBL-S6QazgUJ0Q95CzgYnpDIsNd0geXeiA7zJAkmq-W86yrP1fkE86KF3cSsxk6e8ikmDneuCV-rm1lu-4Fb9PT2UtKP6vSTKlzHI72wP4QVq2o2plNEAbfd4uU2LgynD7j6w_QTH_gRWvnDYRnSqztG194OxhzjzJepdYmTOLyZha4WiC3gUMHqPg2rOKynfO4pJV91B8kD4KrStOBpJbztUZL0Rl9Oq1x0f7NtQylSsEVAD-scESAPG2QQwD8hCVRkBaKsRqp809HYJF1-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛ تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/24595" target="_blank">📅 11:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1mtemeEhpUiNxUXsIXMC_22TE6oj-G22zGVKa5zRUd_yGrgyj84CG5L-7hyaL5r82uMpGMPwp1DcMFdsi1vqj2YpGhmqQxpk79BiVNfoi4dPbtOmYo48AZP2NDgK89u_mEL8-w6zlz0hyDnfPeWLaBeEg__cvWLt1CmK8qs4_mWP4XdEFSYj7tR_AeERTY9dGh19HjxcNmDyTaphXq_rMc0rRPhnKWkr0RmXwHphdG2BPwpbik-NJzkj0__9qd4AtbCAbYBMQkQqKDLa_gxIhokqVUl6xzVzhHO0fKhIom6Y3KL6Ejg4Ui_E69HwzrX7hJ3Lq6pLwDHfkCeV9fRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/24594" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5AKVURPYaXFuwYqaWgKSGKt3yTzj-JjTvCyYE6Sc4u-kSeSVyfW4N4xe4pIUi2DksG81LwzuoVAsFJDqAd0jkE1Gh8k3LamrdPojordU94QeVzCKO-SuS1zXIf9iUO8qkCSVOO-b8QidFdgfhnBW2G7WtXMo5flxhni0dfHbj57GYln1XxuAuwCMEfFIoHy8t9MIMGJXpGGzr95LRvq6F_BO5-6uhq5BlV1_YYkpOku1nl0Ndk7z8Ss1mRa7b4SNfUIjtLwlLs2oPRYfBFY5GisQAfqltT37mcsqqaS3K-ZZRnsV4712p04G923_1kKh_g_2oi4-DucvIG1hAtpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال در تماس با مدیریت فولاد خوزستان آمادگی‌ خود را برای‌پرداخت‌رضایت نامه یوسف مزرعه وینگر چپ تکنیکی‌این‌تیم اعلام کرده و این بازیکن بزودی با عقد قراردادی چهار ساله به استقلال خواهد پیوست.
🔵
باشگاه‌استقلال پیش‌تر باخود…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24593" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=BLI_Rlb0sD6-GVjVvAnN4WcQA08KEYho31bV7Jd5xm3UPg_F0WVylAVC123PbKpYn7PNi-djts-HnghPFm9dY6EhMK1tMr3Uq6uHB0ZeTiYg0SFOUDQgPKuxXoFVDhEKZ7JN9pjMOhQQT-wmeO9fHhZcLZPImLlnYzlfLHDI9jE2rhBDjSvymwgjFhK8NoscuB4E8eSzsYZ4Sah4NtuP4zIxY3WfE5xYw7FxlON4vvIZf_vd6TOSsNsrGxIQZqND1e3COMjgiZonIBbUg-vaHVKcAWYj5GK1gpvIaS2Wkq1IQwKaOJXd2Pkx9UBSFd-r_ERjFLN0vjDcKouHI3l1VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=BLI_Rlb0sD6-GVjVvAnN4WcQA08KEYho31bV7Jd5xm3UPg_F0WVylAVC123PbKpYn7PNi-djts-HnghPFm9dY6EhMK1tMr3Uq6uHB0ZeTiYg0SFOUDQgPKuxXoFVDhEKZ7JN9pjMOhQQT-wmeO9fHhZcLZPImLlnYzlfLHDI9jE2rhBDjSvymwgjFhK8NoscuB4E8eSzsYZ4Sah4NtuP4zIxY3WfE5xYw7FxlON4vvIZf_vd6TOSsNsrGxIQZqND1e3COMjgiZonIBbUg-vaHVKcAWYj5GK1gpvIaS2Wkq1IQwKaOJXd2Pkx9UBSFd-r_ERjFLN0vjDcKouHI3l1VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/24592" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24591">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fB5DBmWlCQSbNAAiFuoc-fDwidYnna_FIBVmBcbwtsckSrtiNhTOiX4_4DOaCb8ovLrWhVYIpvQ--BuBRRa_KNi3iOwKCSBg8Em76T3uwKeH8HVrNzUaq20_KgaFcta7_f7T1J2ZLWw4mKF2dEDygRcxLg79joAFMOEnlF2BgTtYBtL65yBLvaJ4zTvuPHtzisUxQ9X8fcvkDuLesyQPDCorSIU9kRSqbkRINQnMuRZJ-15TfO0m74V8jJf3Ke7Mt9AbJyqjczzYTkrfHrzAxtjN-g_MVkv50TxGUa2dAUuaPLAE3stWIdBwzr5VMcQYHD4HMFIJSCPgNGh6CHlf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🛍
ازاین‌لحظه‌به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r8
@betinjabet</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/24591" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qApvYo5zBJwaCnbrw2hXMEztWii_Zv05DSJYac84Vy3DU1dOppdBfIkzeH5bh8-6-WgmOihcyCPxPRXwdq0tr988Hyu1624Ro0gTxfosGr3Rw0vJ4yrzWg8yckMgbmVwWxkwWocYu62-MgE_9UBYE5Oa0gWoNnzLerzyKb2Dh1HAMhqhaUGbWf2mu5PQZuTaF1Ii2hu7ESvzw5TD1dw9ncLjvItJ3RTSgS-eRq8C-EInueiGqwUkC6t_BVTXJZAQBRxv5LCzgjEefT4e5NXFrTFdIYLBjwlP29F255A1G1lXoVpcJuAmgP23_EuK8xdYs9zQJiNlXx9nfk211Se_dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24590" target="_blank">📅 10:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWfqPz--IVgWvr-nkCo93XHAHJMvwlc1T2BYTRztA4Rqu2i4kexDC5-0VKw-hYFpO7S26pq9A3FoUcZ6OGTYrRMUFy4JP6DOQmYv8Do_MEskGKxIOutPSbGlcFGCAGigr0y24fZQEuo6h2R8nOH8JWHiJSbk3b9Sz7E0qQ6Nj1UvVZj3wpzsNtJ4Sy1EW4jipC3t3fFzXUj6ofwgZDNz4gZkm8nT14ZEYwwUfG9Z3ReNHNNT-M6enxt6Nm36wifRQnIEMr2VfuQeXBruvg9FS3fIedWduasbG5nmlIGp5QbwR66M8kURM-o1QV_3r3CYsxwNAFBC-4n48dHG7oeM-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24589" target="_blank">📅 10:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=GtMwwW5qWBIx8ahsay3JypllbaZwiHimlhOAF9h9kMfWo0oOv-TegtvbHKLhfKizJLmfDizLrva8zr_IsOpvZVKM-LFFTcGxG0jfcQGr78w3V0VkW2k-0up211Ik5V5PkoUOQgmvWYW1-ZM-hTYGQUBm5Az5etzk1U9JNm1tKJIy7q_YUsLIys-G--cXLsEmc6OgCxxSoSVPhKJ7JreRKx8nUpMyxxG_TquhvOfXeoSL8OgYnPByCEz6i1jSC9gGW4z_OZeWB-dizvD82sBbJ6T8q9gAfjlT5uO1KSwV1ye2iEH7XeobDELSdo8xjg55s55tWz6UYHappbHknkQenw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=GtMwwW5qWBIx8ahsay3JypllbaZwiHimlhOAF9h9kMfWo0oOv-TegtvbHKLhfKizJLmfDizLrva8zr_IsOpvZVKM-LFFTcGxG0jfcQGr78w3V0VkW2k-0up211Ik5V5PkoUOQgmvWYW1-ZM-hTYGQUBm5Az5etzk1U9JNm1tKJIy7q_YUsLIys-G--cXLsEmc6OgCxxSoSVPhKJ7JreRKx8nUpMyxxG_TquhvOfXeoSL8OgYnPByCEz6i1jSC9gGW4z_OZeWB-dizvD82sBbJ6T8q9gAfjlT5uO1KSwV1ye2iEH7XeobDELSdo8xjg55s55tWz6UYHappbHknkQenw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
صحبت‌های‌رامین‌رضاییان ستاره استقلال در دوره از رقابت‌های جام ملت‌های آسیا و جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24588" target="_blank">📅 10:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=KB4Z62vsvaTtwEXZcgsdtPgidAiB9Zd71ZBz4FaV8YoI-qKWOTGydlLHKZsTu1sS0yDJQMsaK6omg_igkgcQFwx0kcPTeaQbrPx3rsBNMA-NmZZF9mp98Co3-ZAqytSR7qsMfaMKFJTWCpqzBf7-d9jG_SgxFQ4Czo1KBLsr1t_Wr7ds3EPUinnK3IDXh4LnGlj-EaThAvo63VS-f-yQ8qTt0JSlk45Q4OYlurjAdgpkWwHyaw6cr1z5sPjtJt0siaV7m_ve6beo0_teoHZkrXNnU8IO9pxmwo_RehVgRt5lTjHbtDZz6DrXTY21UeFhA02QlDQtIr_An1NvkjZe9Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=KB4Z62vsvaTtwEXZcgsdtPgidAiB9Zd71ZBz4FaV8YoI-qKWOTGydlLHKZsTu1sS0yDJQMsaK6omg_igkgcQFwx0kcPTeaQbrPx3rsBNMA-NmZZF9mp98Co3-ZAqytSR7qsMfaMKFJTWCpqzBf7-d9jG_SgxFQ4Czo1KBLsr1t_Wr7ds3EPUinnK3IDXh4LnGlj-EaThAvo63VS-f-yQ8qTt0JSlk45Q4OYlurjAdgpkWwHyaw6cr1z5sPjtJt0siaV7m_ve6beo0_teoHZkrXNnU8IO9pxmwo_RehVgRt5lTjHbtDZz6DrXTY21UeFhA02QlDQtIr_An1NvkjZe9Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ابوطالب‌حسینی درباره بیانیه اخیر جواد خیابانی با زبان عربی برای الجرایری  ها؛ که گفته‌بود تلاس کنید که اتریش رو شکست بدید‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/24587" target="_blank">📅 09:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24586">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=U0eXY25dcFTMPc_rZ7JHq7QCVmhzYR4mYDXZRMvBWjjFALUfsQwVKxcloi-pt_KWOKVUjVdWNjSTJZDN6h2ojmr019JCoF3XciMyNp6XOd4BSKLxVPZrc7skDTW8EZyQSsEZRDKEoz-6Zrs3z-Xq-TKQMMDWYW5XbldLfWPBhRwUx817QYu5u5kES2NxPWqmtnScXZfObDrOliv05SMGV_5157VxIyurzU-rddqNbmF0qOgM3P_QbTfwcJ1jbQFustP8Ms3ve3bBynhCx7yN6iXN3qS9TyAU-M-TyGFF54IBhYnVZ3ZAO_XV8iyqzqj7M0MQH95vZukXftp1cj7rhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=U0eXY25dcFTMPc_rZ7JHq7QCVmhzYR4mYDXZRMvBWjjFALUfsQwVKxcloi-pt_KWOKVUjVdWNjSTJZDN6h2ojmr019JCoF3XciMyNp6XOd4BSKLxVPZrc7skDTW8EZyQSsEZRDKEoz-6Zrs3z-Xq-TKQMMDWYW5XbldLfWPBhRwUx817QYu5u5kES2NxPWqmtnScXZfObDrOliv05SMGV_5157VxIyurzU-rddqNbmF0qOgM3P_QbTfwcJ1jbQFustP8Ms3ve3bBynhCx7yN6iXN3qS9TyAU-M-TyGFF54IBhYnVZ3ZAO_XV8iyqzqj7M0MQH95vZukXftp1cj7rhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
فوت پسرتازه متولدشده کودی گاگپو ستاره تیم هلند و باشگاه‌لیورپول درکوران‌مسابقات جام جهانی میتونه بدترین‌خبرممکن‌برای این ستاره هلندی باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/24586" target="_blank">📅 09:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24585">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👤
واکنش عادل در ویژه برنامه امشب جام جهانی به حذف شاگردان امیر قلعه نویی از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/24585" target="_blank">📅 09:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvdSzkqcFxa5oTK5eGqwgnY3XkReJi-wQxp9Uv-GM9QaSHgqR99rOUJlzUFBvLYXLwan3eFrbVwXtSf_zel7lpzSNlTJd5mQgwSuK2QEnGjzW1S0FhKTZsOfwsMkNSSbhasLndi70kmkdQGVFFQyC6X2QXLWYiW6F9qKxxtHuy_8KpNf-JbWl5wabhrHifBBpA8ee6tk9w_M-5xx_Xbs8po4lKeHl3sa44bmaMR5pTBlfq99spSu9i9oTnA-0xLMd61r7xuuSgW6ZWgYzbRhH6l7uQWReoWtFMGgq2vC_ROtGAr1esOE6QYX12k46nxS90zhNx3LKWZsJYfSSsl8Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24584" target="_blank">📅 02:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTGH4XTwx1E2GMrkKUs5NOIgzmheehTujEPjTO4Eg0zIGeyRoeGBGmLYk1__4rZprBBf8gePJBn3W_11gcKR-BFd1BA5S7mNoP5-HDk5Uvr3DqaiZogSTMKCmp96uuZhTqEeXyqR8o1rAyVglPJBUZOuRlfhOo0TFVtrWY_wq1kTQZqOK3mL0-C02TUPAYWbvb-mp6IRsOClKaTHiBOfx3YKNZoLJ64KX5lBa7xReto9Lav9iR_-Dq4KmrHLInMd7VvYb-Tg_zO1UCtq8sKWvxv-ozRxRpqVklk5Vk5LXtpuBGdqreAobvvsnXR2jwJAwvHp9YWc4MX5AexyoFXonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان با گلزنی در دیدار امروز با مصر، شمار گل‌های خود درجام‌جهانی را به عدد ۳ رساند و درکنار اسطوره‌فوتبال‌برزیل کافو، به صورت مشترک درصدر گلزن‌ترین مدافعان راست تاریخ جام جهانی قرار گرفت. رامین رضاییان: ۳ گل؛ کافو: ۳ گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24583" target="_blank">📅 02:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPtCsuVASscOh3LZFRRmKiDi3h17xgf_Oc51QZAhMQxAic5XVYGr-OW8akLIhp5rnSH2Nt8aOvUidTFvRtMRhMxBgCl2ZddFbVLlzVA0IaK4SYUQUKpVdpDApf7XO1fFJIWav9IO0kklTWrk4Z5PSLxmayO9qfxYLwEByXGqEtUku_1Ij3T-nUfk1usrJzqyrRPimqo2T8fACJyibndHjZovGBF8jGhvp6sNX4mHrVMlag8g6xqPFIcJaeaF9ksE4Iz0DZ4iEPpv7lXxSUQP_TZVhSiDmYOr95RaiR-zmtxZ5jppwAG017qf02WADjxNxc57GLlzTPOhGCCWLTyjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دو بازی، 36 سال فاصله، یک اتفاق مشترک!
‼️
سال ۱۹۹۰ دیدار برزیل و اسکاتلند درجام جهانی باوقوع زلزله رودبار و منجیل در همان شب هم‌زمان شد. و حالا، تکرار همان تقابل در دیشب، هم‌زمان با زلزله‌ای بالای ۷ ریشتر در ونزوئلا.  اتفاقی که بیشتر از آن‌که نتیجه‌گیری…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24580" target="_blank">📅 02:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24579">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJMEmWd_0MNmVoe0I-A9wd3HEoZOUe1iodZelPnleHaXrZ71dols9KLrGW7h3cgw2z8zZHaqhD1Z_l5KdskbuKb2jBYzbumXeg2WkfuyXQJ8ajahWI50rBUvJCcHrppGpbfq_suYlBkNYdmeKDq5gWuqo6TCjMTKtyU1SXqKtp0c-HWbFxS4fnHv_6mM1VcbTdUCxePAVz9TgxzUqIXfCyyyYaAkHbt9yC4C-0gNmzv_0fRnPrb7Xn4UIbWjVK_yo_jr4mKiueje7ZzbLdpMkfEX6tdlqYay1o48jR_ej-0XBgu5QEj09G2GcBbZNbpCfIEhqcKxpIdyWy5VjQtzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24579" target="_blank">📅 01:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUP5WlqJxBfmVY4UAJ7YHYPH4d9fJTErYq0SyPTig79rCxsNI0YO5Scrd-N7niejkeeF0ZbIauTKQ-Izd181elrqko0awR4BIzaKjY3y_XQI1c2ofQQxs5_UIJzSn00d7AMuscAYspoSBwlUTNwmCuQ1q0Uale7us6zmH68FVAhhpMs4-jzXxbkBQSxjuh4aPmjIZXM5Sgc6VczzTKl-82mG1X94DhWMdzNdUnlL26e7uBePxEWaG9wV9PgotQgnek7s7DGcBKgcQ_OZx1UkOO0xx8IhFnTsOIqoiTv1LC9BvW1yW7n45cWl8yJbEobjCO9RZDmqTctf6D90PeWNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛
تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24578" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9isMOTg_n4wJOYPodo3om7IN8ST-3s9qP29ZrFXHuSk42Jyr15vjYgJE1iBl_m0Zwlz9uguEMLip0kUsIbH0fVYL-F1zGFgzpEnzJnqJ-QuDa5AbDoPuHyZ1idl343VLxDofs8V7WhDyZYOeJIe5waN3DdbYqv9AcAZROR4OOu7QHdeJTA5INIVhh86xC7mzkieSSfMI80_AQ-_n1HyLQT6PpzgEUOvwNK399j_8Tm6UosQUiEYGMc7soLJqqOm9ffpsXQV7FWCFD7i98HDztgvWOSP-78Ttw1Zx59Ptlo1ICumS7FX6Fnl9YtlWFVX5yktlUufrU5PSn3C61zklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف بدون گل در جدال کلمبیا - پرتغال تابردآرژانتینی‌ها درشب گلزنی مسی و راهیابی کانادای میزبان بجمع 16 تیم برتر جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24577" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXUZlpTkOujeCB1YS2cKceX9q7ngb4wG_pawhxf0UM-QAjhFd8xnepSejnbUOI3Ml1dnqo52oU_b_R_75JkOJcsaLycwG3Qw_BnJZePBAjvyh85-9RU3WwPmbzc45nByCclvUGNBrEnWEgAeBTlprwdqju-PjAjMqSVrXcaDIzCB4dG785x7WZXV3M59DFL0m5NPMTgrHIpYMCkOgaZOTf81jWCJ67wC1fCJi9xfhfHVIsyYIP5Up7EUm9TV_uitlZlz4KZY2FYoe8KqZEAGlvDJCVTY16TBigJ5uzNVALnwrM9UtkyKXtLmZp9B34jlbrktb7ewokFGZiHo9kOU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24575" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=HlMqw2apWoGTghO1SNmSf71X1b33VA2RBaPBBoprtrjW9tnvqEcsfx85EvXcZ2wQz_1FO7AUoXYNd4eshp8z2tNYgHpiqynfOXTT-C7KKRZ-VlVzJkyC7TKoCW1v2tQbOeWfpLQfgA_4skB8vu5WNs6Q8pXD4QNfKgNf8R_X5t0k70ysSrrEFZgi057EG3glx_OKAKERZBdLk6QKChC41HXyFKr-4SE2bVEaM8dQ62ARlvSmhCX1scfkpgSMNFebaKfHNaO8QQNby1mGyHUipOVlUaE4w9Oe2swp3WpJWS7uM11Vc4I8Tr_jFRGKo-r_gQlSsq-OWWLELIr_k19jAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=HlMqw2apWoGTghO1SNmSf71X1b33VA2RBaPBBoprtrjW9tnvqEcsfx85EvXcZ2wQz_1FO7AUoXYNd4eshp8z2tNYgHpiqynfOXTT-C7KKRZ-VlVzJkyC7TKoCW1v2tQbOeWfpLQfgA_4skB8vu5WNs6Q8pXD4QNfKgNf8R_X5t0k70ysSrrEFZgi057EG3glx_OKAKERZBdLk6QKChC41HXyFKr-4SE2bVEaM8dQ62ARlvSmhCX1scfkpgSMNFebaKfHNaO8QQNby1mGyHUipOVlUaE4w9Oe2swp3WpJWS7uM11Vc4I8Tr_jFRGKo-r_gQlSsq-OWWLELIr_k19jAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیابانی‌این‌بارگیرداد به تتو روی‌دست امید نورافکن میگه حالا که‌اسم بابات‌علی اسم مامانت چیه
🗿
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24574" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR2jCwhuKCkvOfZeqhyY7MM_hDZhhMV8_lF6SOifbUlfbFbQYpIr-2NyLP-PEJOYfSrMDt3pZMGzdpygm_cYcv2oi6qxUFz1HQ9xRRPBPRMYLGxvKqj-yfYHMEkyYWKeUhCfIjBaPo-s9hBlKGXzT7An7szQhC00Z2-XWw8t8K9Oai-Gc-p8tXr3ltM3qlKcW-b-Hk4Q-gsilCNduLAuLh1i-oWVMDO-MPVoumAu7skOvHoahLqf6loLLmgnwG1hXrhtSxfxYVrkaucGYQ5KuLh3BXqqyNnlhsWewXd9ELdRwA1VNtgVOYDn6opQ6IxQxZ3yqr5Q_V6T8NF8Lttjkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
👤
#اختصاصی_پرشیانا #فوری؛ مشاور محمدرضا زنوزی مالک باشگاه تراکتور که در نقل و انتقالات اختیار تام گرفته با باشگاه اتحاد کلبا وارد مذاکره شده تابرای‌گرفتن رضایت نامه محمد مهدی محبی ستاره ملی‌پوش‌کلبایی‌هابه‌توافق برسد و این وینگر 26 ساله‌باقراردادی 3 ساله…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24573" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24572">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq1YQWv29tw-U_AS_H6HCSbQHA1CblLyRVsO9FuhNmGihYQibSIX_D7UOE5w48dw81rC6M56ZTw-ax2bAJm9l6dbp-WroUXhwtTS11u2g66fYxfZQZiE8EOanxSJLy92smR28eQ_RYRQ87wWHzCIitZZ4mlNJvQcUDtL9Zfz6AqcgCz5lz92C5KNNFZpDnEkB_A0PimLO0uWRmi5RpWEyZ9uQn7oDlvnJoZZXObJGn7TXp0M6esk5ZYzE_LIn1rVk9ljdmDCfQN6KvihFovOvNakMslSnXGSJBm3WSxuDZPhgwae3MpQbxWvHs4fJADC_xZeu2Yn-XN0peR5yS9Urg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جواد نکونام در کنایه به امیر قلعه نویی: شرایط جنگی نباید بهانه شود، عراق سال 2007 در شرایط جنگی قهرمان آسیا شد. پ.ن: این رو کسی میگه که خودش بعدِمساوی‌تیمش باد و هوا رو بهونه میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24572" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24571">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=Dzm3CUwBDLxdKyS_94traXQlfDlILLsYNE7-1IAxfaVEl-GKf7Q8-WadjdvbZ4RimhBcv8FVIT_Px5U3aFKQaVq02kgGbuHGUtlnJUJWm_v8iGpAJKdI3cAk5ml2zlEW7M5UGtXqYA-vTPUCgOPFk5IMWCmTxcQ1LJIf09GJNltmK2v97Qlpg0eEJcl7Wu-YmNvwM_f1hiw_4ASlFpP17Tsb-pydASnGAwWVvFnCiDB22AHS6kho8a_q65sn0ofwPQ1r4T_4w4j-yKOwU7_fRHRT6PxYd5udtG4GTZp1onM2PPovYupQg_-Xxr6KAR_12SQjOUenuNFBmwMKycDI7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=Dzm3CUwBDLxdKyS_94traXQlfDlILLsYNE7-1IAxfaVEl-GKf7Q8-WadjdvbZ4RimhBcv8FVIT_Px5U3aFKQaVq02kgGbuHGUtlnJUJWm_v8iGpAJKdI3cAk5ml2zlEW7M5UGtXqYA-vTPUCgOPFk5IMWCmTxcQ1LJIf09GJNltmK2v97Qlpg0eEJcl7Wu-YmNvwM_f1hiw_4ASlFpP17Tsb-pydASnGAwWVvFnCiDB22AHS6kho8a_q65sn0ofwPQ1r4T_4w4j-yKOwU7_fRHRT6PxYd5udtG4GTZp1onM2PPovYupQg_-Xxr6KAR_12SQjOUenuNFBmwMKycDI7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب ابوطالب حسینی درباره حذف شاگردان امیر قلعه نویی از جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24571" target="_blank">📅 23:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24569">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxKux6YJMIc7GDnttJvAeQlf6IrFBLu3C3pHtJrXgTLWzBwaO-1BTG4SmJ7Bq1RHXm3p6f7idCrRWtAE2NsQMna6pl4v-7t_3o3fW6WKlpGecKVKNLr29inaZVus3uLAX0xU1Y673lvEl20gmgQ7opVrdjcHqX7IHoAxQv7Cev8jjO9Qke0kEFD3S0i05TNFIZW6JUn0PEupIam4G5Y8ea8ZMuEfRNdjBZbCFWcFpQ8ZB8Gp6jB0bg79fq51_oyASMnfPw467QcBeam3fgObUp6DP04BvukFTaAZ7h1w_COob6PD8C1x7rbrBi2Sm_4GZpndHXmdL-YetOzwubIsBmJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxKux6YJMIc7GDnttJvAeQlf6IrFBLu3C3pHtJrXgTLWzBwaO-1BTG4SmJ7Bq1RHXm3p6f7idCrRWtAE2NsQMna6pl4v-7t_3o3fW6WKlpGecKVKNLr29inaZVus3uLAX0xU1Y673lvEl20gmgQ7opVrdjcHqX7IHoAxQv7Cev8jjO9Qke0kEFD3S0i05TNFIZW6JUn0PEupIam4G5Y8ea8ZMuEfRNdjBZbCFWcFpQ8ZB8Gp6jB0bg79fq51_oyASMnfPw467QcBeam3fgObUp6DP04BvukFTaAZ7h1w_COob6PD8C1x7rbrBi2Sm_4GZpndHXmdL-YetOzwubIsBmJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24569" target="_blank">📅 23:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olNXwHyGQ34SO7EQw-Ns8TqBvD51LA5csBTpNnl8q2CCf03Z16fNC4yb17cDVUE0XHfV4La1jRh3vQXuToOk_55NojRhP2luY6KgCJ10XfxQIefDWy5mxr7KBibeSt4S4QhseQM8UxxzIqvYczbDXmEVlYd0mSzIhm-cg_Sxm_DpNTmymTb3E2GnLRhA8GnQFFVqlcpc0MoV3c7qRRsJhaEtjT_QoDSpUzzzLxPLJtC4R7p6k9pmVlksPJbAlZSgMJ7VXl9Y8sOPDS2XhNAaUmdvpqtNYsNs0hSBHFEhPBbN7Maa8qwCMp692sRe8SAkuvXCt74PUKbLugfjHabfOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24568" target="_blank">📅 23:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=fb3Hn_TjYC5osEdUI1jFtg3fOk6wa_QQzqmZAnXyYheVLMkOrCBivMhSE9JUev0jBZL1WNDBpbCgULx6YaL6EYe1-t7OA7rbDLA9bx_akNHKohFLPMtvdu578VCj5ycncQWpoPdWJu-veE7oCAMTH9Obu8PzLGDWUGYUAXtoBTM1nDZtPtC1X92LiJq-ifWnatgLNAXeGiZmGKk5bU_CcJ39dWCD9WVkYO0rmqVC6A-Eo-6sFP9dCWvuZduCWXgiV_x1_U1AkS3e29EJBPh8hz2vX3u3yI5c0_Tns6T5S4m2KndzaDNbmucZeQ32twWE4bc1-gJGPAJSPCkE7jAZlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=fb3Hn_TjYC5osEdUI1jFtg3fOk6wa_QQzqmZAnXyYheVLMkOrCBivMhSE9JUev0jBZL1WNDBpbCgULx6YaL6EYe1-t7OA7rbDLA9bx_akNHKohFLPMtvdu578VCj5ycncQWpoPdWJu-veE7oCAMTH9Obu8PzLGDWUGYUAXtoBTM1nDZtPtC1X92LiJq-ifWnatgLNAXeGiZmGKk5bU_CcJ39dWCD9WVkYO0rmqVC6A-Eo-6sFP9dCWvuZduCWXgiV_x1_U1AkS3e29EJBPh8hz2vX3u3yI5c0_Tns6T5S4m2KndzaDNbmucZeQ32twWE4bc1-gJGPAJSPCkE7jAZlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24567" target="_blank">📅 22:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏐
دربازی‌امشب‌آرژانتین - لهستان در لیگ ملت‌های والیبال ست اول این بازی به شکل برگ ریزونی 50 بر 48 به سود هموطنان لیونل مسی به پایان رسید. قشنگ به اندازه دو ست تو یه ست بازی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24566" target="_blank">📅 22:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24565">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9cA1E7sn-nNCA9jf-hLytv5HD03V7PbdSlO2Uhz5y-Wlk6fkg491sdlpWncPeoQ5QgdXgbv6xTE_BOPj6Qe9469gc8b0HKxBGj4GMBsD08p362v6IwMmRUTWP0bo0MpSl_4UuTttcn8PKKeoM5ccHghX4T3LKyyLZMUIp3YDl7s6Bp0NS4i2U1VugZoWpjBa-ueopZIlviWjf_m48ubPUQPNRB1SyUvPt5xwTzS5JU5EEDRopVd5wv-HSLCjORNQLnf25N_1l2GAMs9LHZIrFwi_XdBDAHnU3_vh4uLhez6IE3xdiUbnjXj-SLLf_-KBwqRYxns-9NqzCLpHrcSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24565" target="_blank">📅 22:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24564">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=ehmSv33yzP2DgB3amIm0pVakAt_dVo9-mYoa7FkmPjGNJPw6A1MlRzyrQkMGrjoIF445kVovvYY-TBe7W4qx5Sj9CsoYkjbUjX7Wi_FtjBarbO7aAdu4kHy9F16UC89O06YpHTnlefNHjg5biZ-cmBXtUDBwenY4sJjg0i7pGwKnO1LPkZWPibURf-4PWkBpsTGtljN3OR1J6masKPPreVN56mEWmvWVsOa7L-8n4p1iq0mBbGHrOoRJIPQUQuIWpfPd1QsLQ3qA2BpSQEWaN5S2xOpxDtjBr1ItNrv3I47H_U2FfM1__d6PG2smvMZf-0JF9rlmwBjjDvhVgY7TFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=ehmSv33yzP2DgB3amIm0pVakAt_dVo9-mYoa7FkmPjGNJPw6A1MlRzyrQkMGrjoIF445kVovvYY-TBe7W4qx5Sj9CsoYkjbUjX7Wi_FtjBarbO7aAdu4kHy9F16UC89O06YpHTnlefNHjg5biZ-cmBXtUDBwenY4sJjg0i7pGwKnO1LPkZWPibURf-4PWkBpsTGtljN3OR1J6masKPPreVN56mEWmvWVsOa7L-8n4p1iq0mBbGHrOoRJIPQUQuIWpfPd1QsLQ3qA2BpSQEWaN5S2xOpxDtjBr1ItNrv3I47H_U2FfM1__d6PG2smvMZf-0JF9rlmwBjjDvhVgY7TFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
دلداری‌دادن‌کریس رونالدو به رودریگو ستاره جوان رئال مادرید که به‌دلیل مصدومیت جام جهانی رو از دست داد: باید صبور باشی تا موفق شوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24564" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24563">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=DchEIsKzvBJ7F-K3TlU4laAcR82PD9Az556gFnYhN3NpVcr1j9LDy6KFUGewn7XVuF3nHNAsXJTSjyrc4IbnnvdEUzTwc3UUKK1ZE9SAeQCqP3XLzkVnNbQZTlCnnQvM0LtE6zEcyhCxjvegFxTmfcXVs0dCr74KUBFuoG6v4harEQVz8Q6C4j-Dk-zlzr2Ck9T5E0UHRK_YSr2RqLtwF9E4qThc5AA0NtFOvHE_2uhna8tGSzKfUP_ikX60DeUshAH-4QXnPrQDm859EqpGQXgFANdHNeJVt0VEY_F1limtSznxiilD4goHP0aM4UlWKVz0pLksbv_dEntArXYR2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=DchEIsKzvBJ7F-K3TlU4laAcR82PD9Az556gFnYhN3NpVcr1j9LDy6KFUGewn7XVuF3nHNAsXJTSjyrc4IbnnvdEUzTwc3UUKK1ZE9SAeQCqP3XLzkVnNbQZTlCnnQvM0LtE6zEcyhCxjvegFxTmfcXVs0dCr74KUBFuoG6v4harEQVz8Q6C4j-Dk-zlzr2Ck9T5E0UHRK_YSr2RqLtwF9E4qThc5AA0NtFOvHE_2uhna8tGSzKfUP_ikX60DeUshAH-4QXnPrQDm859EqpGQXgFANdHNeJVt0VEY_F1limtSznxiilD4goHP0aM4UlWKVz0pLksbv_dEntArXYR2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24563" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24562">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7ZopXmkbb23LkNoUlZHHH3Ii2CIFQKd0vO5wyZcEEnNGAtASVSQs4Zzl-aW8BEi-yPap6f1UU7BQSmBq7aCWetDzGiRq1rXuJSOMvcsRYdUIaj6ukqs-s8LyjtBA1Ba9kgP1hDEHJaKpwAYmd9bMyWjRTVFioPz1_g8qQgD4eF3NKvd-6fS_Aq_fE04BPZIlhcnaHtQixsIgkjWNaePedYkP7Uq2jbLONKQc3p0ACKTfmdbRXEN8o4jVjrY7d9OZ8ryOIRk9q-4lGpSiF4-LXQKcia-Xjnfp25aQ3dDi0PiiiNdG625C3LN3kgZPhwKh4AlKYptTpCevalmoWC9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودار کامل مرحله حذفی
🏆
⚽️
در بتگرام پیش بینی کن کدوم تیم قهرمان این رقابتها میشه
⚽️
🔝
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
🚀
پوشش کامل بازی را در بتگرام دنبال کنید.
👉
🌐
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24562" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24561">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=ruaUNgxP6iVhOTut6flMGRVYDZAQu5hylq5WW53FhgE19-7zta-Fw_NXqT8lxDkJuUWilCskD9Z64raFQywiwqp7ctd3p3zpTpeI1yVYxkG0MDWXKfRZPcx3FW_YL6NqhTZUvazG21n0OtaSCAlymFhJXQU-GefrY1UO59cjaWpoyAOgnryRpkSBPhZ8inMvKIdllURMlUUt15B9wEMomZ-1hStz0AJF257C-UCBFjn2mBu7XLvI5ElOybSnhyPvE3v8UxINWoxHLkSZ1tsZN4aDehfypVL3H9hYpAXGREP_763U391Op44AT_K0bugTNSTJtoH0DI2Jap_qtjni-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=ruaUNgxP6iVhOTut6flMGRVYDZAQu5hylq5WW53FhgE19-7zta-Fw_NXqT8lxDkJuUWilCskD9Z64raFQywiwqp7ctd3p3zpTpeI1yVYxkG0MDWXKfRZPcx3FW_YL6NqhTZUvazG21n0OtaSCAlymFhJXQU-GefrY1UO59cjaWpoyAOgnryRpkSBPhZ8inMvKIdllURMlUUt15B9wEMomZ-1hStz0AJF257C-UCBFjn2mBu7XLvI5ElOybSnhyPvE3v8UxINWoxHLkSZ1tsZN4aDehfypVL3H9hYpAXGREP_763U391Op44AT_K0bugTNSTJtoH0DI2Jap_qtjni-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌ های تامل برانگیز آیسان اسلامی درباره باخت شاگردان امیرقلعه‌نویی از جام جهانی 2026
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24561" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24560">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=PMrtD38i5tcLb_YXdOf1nD_rTc77Ja4dIEy7vBokjbZdJKTpRRhW2jMjhozyadKIH9OTEgE34V-UMSEFiPz_Yit5m4sytx3Zgmm3RCl3Jf--G6KrWYzQD41Gtxx18e4GYUT-BTcDl62ISK__MRCoVGaOPy-_Hsr9D3ORd-KuFCY56f6DZPm2bFZQO3PqiN8p78Z_EYIn4R4lNcAvgBawIeX7wX7oxLPZX78S7VB8422nxuXiUlnz9NCpbO6u6TRrGbJ_kkZnq-i7vJTEmEs0hFo6p5lNfRkVjVuVjUK7TzcwUMrHi3f9wAry-WFe13n8PQOaKXigjbau08aU-DtcCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=PMrtD38i5tcLb_YXdOf1nD_rTc77Ja4dIEy7vBokjbZdJKTpRRhW2jMjhozyadKIH9OTEgE34V-UMSEFiPz_Yit5m4sytx3Zgmm3RCl3Jf--G6KrWYzQD41Gtxx18e4GYUT-BTcDl62ISK__MRCoVGaOPy-_Hsr9D3ORd-KuFCY56f6DZPm2bFZQO3PqiN8p78Z_EYIn4R4lNcAvgBawIeX7wX7oxLPZX78S7VB8422nxuXiUlnz9NCpbO6u6TRrGbJ_kkZnq-i7vJTEmEs0hFo6p5lNfRkVjVuVjUK7TzcwUMrHi3f9wAry-WFe13n8PQOaKXigjbau08aU-DtcCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یادی کنیم از این ناگفته های عادل فردوسی پور بعد از تعطیلی برنامه دوست داشتنی و محبوب نود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24560" target="_blank">📅 21:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24559">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fR2p_Wga-49HI0vb3qbSbf9_7MiiOPJRYa-q1IGwqXKBwSEhjj8nNqUIxF3-O1NEioMeJ_tdyqUvmilQZ0EyZpZNHZeD0Vf1EK_6ngY-tvq5Z-6QAw5mvy_pWCNVec2BuBMz7v2KgOOCuetK6FrVKfArboirNyICs5eXVNEFW_cEFvbyittZ_ZWyjMFr-U_6etfHBVG2QKbqxVfccOw5mjAcz0QsHqDxmUf6C_O1cfchpLM2FvnFEa18GfzN7QXwg7rjPVACdeyxUwGZrW1xnImqv5E2aa5anwgMW6QCFvLSWwOcNRzcNwQsjhgRN2LhVqMH_G5XoLaOp4l7KJTPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ باشگاه اتحاد کلبا به ایجنت محمد مهدی محبی اعلام کرده که‌حاضراست با دریافت یک میلیون دلار رضایت‌نامه‌این‌بازیکن رو صادر کنه. مبلغ قبلی که باشگاه اعلام کرده بود 1.2 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24559" target="_blank">📅 21:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24558">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGzJn2NF2FAADOrs-IRjrCNptPDVjhK-DJ64xNJ2BKOZ7I2eRWMCdGjBtHPuHvwFtbOSNMrozvdTxrN6vLU28ZLOS1I-rFr3XgIGWBmTwZvujI9cBLUOIA6vHf_3xbquKNkPxspGs3zFM8gMDyt5RjfrEva7z8pgnRDWvLhDimP8uTFIle_An7N5wk17_c_Hz7tKcDqBPfHDRvyq9xY6b8yKk8hyyp5TZENpKAGE_jsSlVeO6zKgu1nhSTH0hv6qdL_vJa40RcIilgGIJBzIsSsLxdOECBfbfA88p6A_k2eJ-AIIWKc81JCY5Zd0fbVFAfonJq_zS6fUJwTDIyiEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه سپاهان 72 ساعت به سید حسین حسینی دروازه‌بان 33 ساله‌فصل‌گذشته خود فرصت داده تاتصمیم نهایی‌اش‌رو برای موندن یا رفتن از این تیم بگیره. مدیریت سپاهان همچون بقیه بازیکنان از حسینی خواسته رقم قرارداش رو کاهش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24558" target="_blank">📅 21:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24557">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTsEKx_omK7QRzdzED3yCnfGcmUzxjgXLTbO_huRrzOjLEpfc4W2IajkGuAP2p8zGtwdYacsLv0rhVn5gtyu31v3wv5TxbyTe6vqSDC1iGrYL_xNaPPquV2z8yQB2AH_t36w-qTVRrxbzc-wrv6FWVDj8skPkif2RRVYnnpIYkjQ059EM4OJA0wYNuHLehY4n_SestmwftXDPqi_3E-TE0UuOc4Sp5vhlVk-uV507_CDO-t5ULk1-s_wpGL_6gkIKZKrjJjZ5l66L-9zUXcJDJoYH1Zh45XX2NAbryspABtY00DhgWP_Opjz25CioruSuh4DRPPwosdV4P80j5221w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|رابرت لواندوفسکی با ایجنتش راهی‌آمریکا شده تا با باشگاه شیکاگو فایر مذاکراتی انجام بده و درصورت توافق نهایی با این باشگاه قراردادی دو ساله به ارزش 6M€ امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24557" target="_blank">📅 21:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24556">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_52zAoaptBA2uZisKsrNOWGUqakKxq8ArBM8561dKC8MXJwhhuZHH1F4gLpJikvdR7T1J3nUTFLB1QB-iSbMR-e5O1kD4ZRaW-Iq6hfZvd8wubuNlclVyPBaJbEXgVsiE-cwn9rJ04YMZmjRQkwpQ7t3NYBdm0iOX4Kbx13YbastcG3_EmmnjGpDn5IrV4zm8c53KdT4K7KvNSOQJhsiBDz5CAYtEb6gVVpLXC1UF8tDGUfcOmq9inRk5nDQikr1nBDgIKnIkOFBF8PiLNoK5fXkeiAp5hxnaBbRAa9G9bN2-X3pe7KME4jC_Hvapkdu_yh7GKJR2AiV8e_K-EuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
🏆
#تکمیلی؛ سرمربی تیم‌ملی‌کره‌جنوبی بعد از حذف در مرحله‌گروهی‌جام‌جهانی ضمن عذرخواهی از مردم کشورش از سمت خود کناره‌گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24556" target="_blank">📅 20:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24555">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=FxkQuneNuJ4mMnsBLQK0h6PlemWEpGB3yG6Lg0XmopeUlCKntSVeH4VFShv3gjZ_m0FszspF8O1gV7DGOYHa16vkCCgyI_HAZwT9yTe2dppxRat-Q1tOePv39_S6FGwsrlyQMqqYcF8EUiH9LvJX8gWvkmXKxt4DdkinMsN9HJ1PEuULDgOLApHlCcnwNn8rtCNMqjjbxqXUb3zWxnOtPd83yrx53PHzeEuSk4xyZVQjYP2K_63F_WcuZHNGCBlvE4G5vdRiKWwmrgYme9zuy3fvqHUfZQnws70jQ6W6LJIAEb3JXzMT-CjSV8CXNg5VSyd_ZmTjzvFZGXYH_zmWYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=FxkQuneNuJ4mMnsBLQK0h6PlemWEpGB3yG6Lg0XmopeUlCKntSVeH4VFShv3gjZ_m0FszspF8O1gV7DGOYHa16vkCCgyI_HAZwT9yTe2dppxRat-Q1tOePv39_S6FGwsrlyQMqqYcF8EUiH9LvJX8gWvkmXKxt4DdkinMsN9HJ1PEuULDgOLApHlCcnwNn8rtCNMqjjbxqXUb3zWxnOtPd83yrx53PHzeEuSk4xyZVQjYP2K_63F_WcuZHNGCBlvE4G5vdRiKWwmrgYme9zuy3fvqHUfZQnws70jQ6W6LJIAEb3JXzMT-CjSV8CXNg5VSyd_ZmTjzvFZGXYH_zmWYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌ازتاریخی‌ترین گزارشای صداوسیما از رقابت های جام جهانی که تا ابد ماندگار شد. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24555" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24554">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=ahwkn9U0LRspXF8Uwd7RHj7NSzOIEbIDy5m35JDLN3gY8jDj4VeUPpJgFt1UUpXUysuWeN2JJtWjk0HuZKQ_2n5-PhstWIRnWzH1cmyoJPi3FETiFQxVsdz0OaiEtPchBm-LGVb1yv0lRKn6gnkK8iCq8_CsyfTn8PZrs41o5CPzVg24_2UexFpTpjag0yVq0z97CYEvyIEfuhclhnYUhrjyrJTX3X8TckMJD04wtJniXmQAJH6iHvCCJhUEMUIMZp24FIIuzMIL_5PL7EznTZXwDH2z6uO0TMgr4zeA6KEOYlbVrlGGCOYIF6X8Ha42ueKsNdAbASneJdBpaQJ7hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=ahwkn9U0LRspXF8Uwd7RHj7NSzOIEbIDy5m35JDLN3gY8jDj4VeUPpJgFt1UUpXUysuWeN2JJtWjk0HuZKQ_2n5-PhstWIRnWzH1cmyoJPi3FETiFQxVsdz0OaiEtPchBm-LGVb1yv0lRKn6gnkK8iCq8_CsyfTn8PZrs41o5CPzVg24_2UexFpTpjag0yVq0z97CYEvyIEfuhclhnYUhrjyrJTX3X8TckMJD04wtJniXmQAJH6iHvCCJhUEMUIMZp24FIIuzMIL_5PL7EznTZXwDH2z6uO0TMgr4zeA6KEOYlbVrlGGCOYIF6X8Ha42ueKsNdAbASneJdBpaQJ7hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24554" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24553">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0tS0vkBmPozCfugNW3tXPpc1rEOBqsX3WnIWBOe6gXPYG-mN0OGg1as7QqUBLSHgEpILEzkr3g5kFwoU1-Wli6WlNxPVgHmdXdfTJ1KNmlOrpYykML1NiHCF9efP01P7CHR6JS5hEevDTZV2ZwR0Fbti4BFYCESwbWnqpLVCfaAAnAQ5vqv_OIRwBRrrvhWBbGO-FbtODMkb19TW5KAA9R0ZesLT_QHYblTM3O5gCbifguiMhkPOTCU9jGyO4EGnBRTQLQJ37gBl92vT_4NNEDk7hw5-4fUkvhlmP3PkvCcfMpkzDau2v-mDxzEmtdVMVGH2QgzUb4FiNUnxOjC9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ دراگان اسکوچیچ سرمربی فصل گذشته‌تراکتور؛ بادوماگوی دروژدک ستاره گلزن فصل قبل تراکتور صحبت های مفصلی داشته است و درصورتیکه فردا بعنوان سرمربی پرسپولیس انتخاب شود به مدیریت باشگاه خواهد گفت اقدامات لازم رو برای جذب این ستاره کروات 30 ساله انجام…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24553" target="_blank">📅 19:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030de140d.mp4?token=sv-zVu1QxSdR7-Yy-FW0hXP05FJamXpZFaL_Wo3TevtT8LgN7N_GXU65_mj5nbLmYSMTKhWplbmX1ncU3W2MYpeVJnwCpWKNHgfYm3tCI_t7Gg0LJe_bkwfDQi2x2FTRRdcaTf0ArHyeqkutYxYxAmXTwgNtCq9ICzSCEp9UHRaFJdOHECxle5fBGOW6ZvsAR5sAvbp_jqh7fWwrJNmb4t0_oFdyNFi25l-Kb8c63xUwoSNMYPbiK4zWKtS5LyjMPNug25n36n1LJCHGWMACvgMVOFbNW551rfvMnKoG9zMA3RpSoa5ANMiL7fyFIBlMMt-vGXTu6lC-Jv3u0o22Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030de140d.mp4?token=sv-zVu1QxSdR7-Yy-FW0hXP05FJamXpZFaL_Wo3TevtT8LgN7N_GXU65_mj5nbLmYSMTKhWplbmX1ncU3W2MYpeVJnwCpWKNHgfYm3tCI_t7Gg0LJe_bkwfDQi2x2FTRRdcaTf0ArHyeqkutYxYxAmXTwgNtCq9ICzSCEp9UHRaFJdOHECxle5fBGOW6ZvsAR5sAvbp_jqh7fWwrJNmb4t0_oFdyNFi25l-Kb8c63xUwoSNMYPbiK4zWKtS5LyjMPNug25n36n1LJCHGWMACvgMVOFbNW551rfvMnKoG9zMA3RpSoa5ANMiL7fyFIBlMMt-vGXTu6lC-Jv3u0o22Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24552" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24551">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=o0PDx1syGn5Lj_IFQH23Mc1bnOy4JjoeFDfRUmZ5dO5FHnnojGj8O-pbZ5DVOEe1BBcbIs5vamsCQtmEvUBwz5tGZbkEhdXUlNBIWagW4WBDWRMDqz50P7PnHuPwVCTaZ0ck1g7CK1jE4qLDwo9nZjJmx7wT0zbfnWERrqD81N7rCXXfpaeCiba9KN7duUGBvL5O-FCgSIrCP4-H3r6lNVa-3nZItkdPGeuDP92VXyveeCyBgTL-E8KmdcuHdEftKc_o4UNc8Ae3pJgU4PdKookfcPdY6M_lxDKHwL6GDAOd2Hq0h_4NmCA4AI-qO5OoyjXWFq0khIbUcK1GrnYCzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=o0PDx1syGn5Lj_IFQH23Mc1bnOy4JjoeFDfRUmZ5dO5FHnnojGj8O-pbZ5DVOEe1BBcbIs5vamsCQtmEvUBwz5tGZbkEhdXUlNBIWagW4WBDWRMDqz50P7PnHuPwVCTaZ0ck1g7CK1jE4qLDwo9nZjJmx7wT0zbfnWERrqD81N7rCXXfpaeCiba9KN7duUGBvL5O-FCgSIrCP4-H3r6lNVa-3nZItkdPGeuDP92VXyveeCyBgTL-E8KmdcuHdEftKc_o4UNc8Ae3pJgU4PdKookfcPdY6M_lxDKHwL6GDAOd2Hq0h_4NmCA4AI-qO5OoyjXWFq0khIbUcK1GrnYCzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24551" target="_blank">📅 18:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24550">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLOnSD2YSKkxkVP9Aglk66lhA4lYYbpPrH4OumNLCsLmEf96X-VYPz1uSo-jJii_j6OR62xDeDli3slJvSM6dDDt2XPOGmrmQuM4DeC4KSEdQ1KxOamUfUInNujuItLjlrKHxyDLTuMGUvZD_N4JxkNT7elSNow9tLhonWLgC-fuGmxG4FAxkx0Hd4Y7SKE_DRfwQfaCDcEsQo55PLNumnWdGsTqO0ljsJVOKXJUAaAzxhB9nZdyZBbIxPSFaBb9E4PG_ARtS8WclGvwDdf3-8BEpaPO5t-gYy5hyjX_IvY1Hoom7hGQl8TN8yJAVxYPHNimLvGCiL627Ac9EeqeHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه پرسپولیس 5 روز پیش پیش نویس قرارداد این باشگاه رو برای دراگان اسکوچیچ فرستاد و مربی‌کروات باامضای‌آن رسما سرمربی این باشگاه‌شد. حالایکی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده که چرابدون هماهنگی با ما پیش نویس رسمی قرارداد باشگاه…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24550" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24549">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcVxnK-RyYwR8yIeQtEJ2FAybIklz7xYHryT_NaGHBNYeqsapM6-mN9qhO3BaJArR0HG0qGo1sBqMfOkiHT8gitpWjRY0Lk22vvrT7m48huDcZ1VIymYX89XIhbUHA1-19O7o45P0iINO14h9Amxwma2AkHlxZEm3Vz6zoa7XxNsXbn45uU6W6k_LXUaGTufPT-tj-FB8NjkD9neGGIjGzdB9kmClVG7cZBASoXhDSQoRn1RHQjBCCL1IVsFfr0kzIdw4qdDcOMG-A2RNDi-gjd-kFdmM2SgqferJtdILLvE8zMq0cnaL2Fte1u63mm9q4KhhRMuH2v37r78TOpnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24549" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24548">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxCT4C-tqUYqJUbXkc43jBbwzEnmm_mPSm4ICE2lpCxh9we37FCqOrDwQuP5py8ZffzYBENu0ob7vdbJPduR52kL9nGh4qCCHSdGlFopCGQAX8twGD8folCQBOK7gAY-6yqqKV00vGDRvHzEJGOQM4STkkbDtlG5VFE1xoSnLgZ4jfiMmmjeY-raJ_elIOv6F5Ne_qgGEAKOeHrr0Oz-YKj-HquhdCQhVX2hrVY9fcbv-XKmLA66YKDmKpGoiCs78ij4LeoIp9H1Bc68mM9bU0r1m9qvSvjjPoxPD8kXTPUaUbOsv6amVvfo99SougyrjIM7hdWor1BeZaSp5aHSpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌والیبال؛ پیروزی ارزشمند و شیرین تیم‌جوان و بی ادعای پیاتزا مقابل کوبایی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24548" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24546">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=tSzAXg-T8bxf-5QQnkJ99yc3W19aGahX2ohxiQtrUdpsbEzqWpm0mvvk2BC3tM3TDhOiUxkNrS5AIEFohdhQbB0MwoTz5xfWkI2DWrPVO4cGLH_pbHfSGn5zb5s7z3eg5NRJ4vat0BYRg494jkRpehVw_JxTZ1zj1nf5u8lLmJtuP1OGBi08OPXYfFR1cx2RIBh4QDrt-1IMiglNPuIB7cmr0Hb9qof-OL0RMd4RY9x4hEqPl2hV6Z54aBn_Mnk-9gcXwVquaIqe5pXhcQutFhJHM0VeDb-21jvsPImOe7Lo9AIX3a6WBgRsGIgzor3RE1YT_kcvP0uxnvxfyAPJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=tSzAXg-T8bxf-5QQnkJ99yc3W19aGahX2ohxiQtrUdpsbEzqWpm0mvvk2BC3tM3TDhOiUxkNrS5AIEFohdhQbB0MwoTz5xfWkI2DWrPVO4cGLH_pbHfSGn5zb5s7z3eg5NRJ4vat0BYRg494jkRpehVw_JxTZ1zj1nf5u8lLmJtuP1OGBi08OPXYfFR1cx2RIBh4QDrt-1IMiglNPuIB7cmr0Hb9qof-OL0RMd4RY9x4hEqPl2hV6Z54aBn_Mnk-9gcXwVquaIqe5pXhcQutFhJHM0VeDb-21jvsPImOe7Lo9AIX3a6WBgRsGIgzor3RE1YT_kcvP0uxnvxfyAPJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24546" target="_blank">📅 18:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24545">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY-oJvfUP-RrMPr5vPZcZnat2eG-IXDw22NWuJ6LCZLwAZGuAB663Npw0BKnKnwEA3rNUp8rIvmXehW2AmncDAGuLaeeL5GkcglnYXKxsS4PWOEeGlJ6elYmVET1b9PR_ld4opaC2Bcf66xd6Dfb1LNJ62eaJyCUHBs4lWtsKFCsppPgSYVToE6flGXnBR2UU8nKtT9lfVXQ06b34rHgj2U_jPUSrDIScUsV02rPilRse8a1qZYUPxnTHkfWAXDILeseQB4jTQkmakCcH_ZuGeKDsgBx8ZIwl0Cxjq2rzLnLyTYTmnqMW35Mfja6D8mvVzlK8wZnPaSxbPwEWDi30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
جادوگرغنایی: کریس‌رونالدو میتونه راجب من هر حرفی بزنه اما بازهم تاکید میکنم این تیم به دراماتیک‌ترین‌شکل‌ممکنه قهرمان جام جهانی میشه. کیپ ورو مقابل آرژانتین همه رو شوکه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24545" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24544">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTs6FfDcauqSoJXSkNZNmf69cqOctLO-UonGn64JJ035aLxCeYygIElYbp8HeQ2lA74TfURpE6Jz2Kj4WIXq4keYJWdZTZuHgIp-YxHTLaXXy1PQTL_2jdhGESoZ0MZNqg4MHoDFwxLA0c2qPBBLM03Nma8TLRs4EkH3_wjFCPMO-Nm1OYerbWKewlaRI5ToYOgJ-Vw1bI4Lq6deBY5VJPpnLtMKvJ9KEzNSbhqKP7lL4K7FLK5P8Wr1ZsvbFNbYtKCCnVxy5UFBwj8UXrd_Tl0PEBPXonxptHIohVS74pXDOiOlAxCNu-nla7PBtBy9L4gUx9B4QeVOrKAxyXQz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇴
صحبت‌های خامس رودریگز ستاره تیم ملی کلمبیا درپایان دیدار با پرتغال و تقابل با رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24544" target="_blank">📅 17:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHAFmmyTxjYP9UnBr2Bt4lmB1sUPxwDQCEgc5hGAobUxi9hpPo7_hzZnY9YmuGRQ6y4Mor5bXHj0J6Wz3g-N7myyxUrUKg1Mm18JfhQ4UP-sapTC4zKh_4BpRDP4L-kJRpdvHRTsH04Ef9Vo2nTjwK1p69YteBfoFdMdP8SVfcWXOFZz3sPq_Qd87hl2CJVVKESErfS3U8rfDN_XtoKQpqORMxDBFefzo5Yxuft9lXjHWzwuqrp9UMP6RRgFzEOqDeh_R5iMpqKh2vRV34qMn_wjnkqoKgKD6dXOjzQ6sqySP09Rgx-YznXWRX7SbCPWC4IWqLRJT7zAyI5IryMlpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت دردناک و شدید خاویر کونسپسیون بازیکن تیم والیبال کوبا در جریان بازی با ایران؛ چه زجری داره میکشه بنده خدا. مچ پاش خُرد شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24543" target="_blank">📅 17:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umKrBAj2zhap971H2OcRyPTvI1HQ2zMMYRuOr1G_qfVM9asErf2n9Uhqqa_CgRLosiYSB9zaIuLuK7CE0jtXtQhjZH8noUZcHyLBlW-wPBqHVis42DCtjibb3CfSX5PQj2dz-2zjuFTQDymNJ0HvfPnvI0l_BF4LsoJu_Lsn2YeVsJ9bftbgL9NW3mv3tAxZVrrkZU5QQcXQp7KDv-3bfB2RDNHZALuOvKFDutGHi5QeAzIDbSHJDNluNpzD9SEcp8XraDXLuKkvmJqeLS-uts8QyXfF_ipzK3eRMwmPMnqSEC1v_q_31SJz94349u136sFHOMoQIf3xHSKmJilqaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24542" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24541">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zl6siVjewLW5zwy2EjSAv_vHBzs3lbV1afRtHg4hWVW57F9L0r8JP2Rlbp4q2WcqTEP9eTGc8y3BWvB_Wsf_0ahyxBpzMyRfUl7jkeaKeYL979qECBxeqbV0r6jQCLPfYwDRZVxZ769np3_PfHkB-8mQA59KV13ULRcF7nN6FJ2QEKogHUpN_UXa3XnhVxCKR5qUt4puRFVtLHtvrhbR_k0LoPSp_1OvqLQqzRTIwTWKUMaCOV92IQM1Du5xmS3c5K4V-6oBKHHfw3_vUe0xOtyr93FBww3B0AjCEciAfxLDyLL-XFtD_21SseaSR1V3UC5n_pB63p5daeVOzFiGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24541" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jjr94G8seKTR-bXGvaBQDAsD4v5EKsXY7EQFFXccjd6jaXYfkXdXxHwxLioyok2oQKnwxH8jhqQ9eXVzMnqYmzxP-d_-8ob5EGUIX48r5qRkuravsrHhHWvKpPZKAca8S3lbNyNRyngC9wrCbWgA10ELXOBveXjFvymNR1O7s5VWQm0FUmoEVWGBZhnCSUxW_PZoP1pzouIZX6o1mg2P5WHIkcvpTE3C0Rg7SPuksr0tMbBMKLWSE8BhIdANCUXFadMYKKC9P4RUiaeONSYeEy-E8MiEQ5IOlYvZO2LBOccz56LghOrlj0N_7Fo8meeGZ1FVeKglvBN7TzsjPHxiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24540" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSneR_BTPvXBjbzzmDEaE7la7YRVLvAxiNrdMukzR9m9wfX4PPp1OoiMFJaPtN8lKrqBjA6hvXBhfqPiW_E0taZoEhDeHN0F3GFZBPeygN9pSuFG0EkilgsjiUnKCAYbQJ7HPoP6Dw7gNcrPvbpWwVNeTR6alvob7ZNDtIF6GX63sOMadsqaazjQjq92_SI6OgloTgjQ05HxUTvkF1gopA4gHERMGJhHyxp3VbOqEwa3vaTIegu99VV0xyvc3532Y_E8SktJqGjD6ZxNgHiYqlnU3qBPbzDgVLX3Zn-1Lu9LIm3LzOSkdSz5PncCMUhKxwSy4IPLIkWq6XjRUlfojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
سوپرگل دیدنی لیونل مسی در بازی بامداد امروز مقابل اردن؛ این ششمین گل لئو مسی 39 ساله در جام جهانی 2026 بود و 19 امین گل او در تاریخ رقابت های جام جهانی بود و با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24539" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1MJe56FnfZ-vfpQwYcaQW_ynWi188lmhCP2FWHr0iWiymUn9raqkbE43x5B2wsWzND5ehaajaWcVIKgsJp2gSewQ-cfEXejNm8Jj4gJ4v3RQiDY5eRroSObFPuJTI7cOLqSOkrts5oUrlQDuUFOOQX32qOg_xqsG5WFfttC4PaxbkzOc_u2HkvuqBJfRzEFEvcnfiXeiyPPHAs6e4oslVO5bIQbFm8nQXkTj2EvLgxMJYpFkuaeCr2wSLv_Kl7UmaHeOq_advipjYiVF_21HNQGBGaeUORcW8KAbMqKjqyTWUMescuboGIihbgHGlqID3OQBBT9fB1iZ0htV-LaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24538" target="_blank">📅 16:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=J8vnjyN5ThkTfCixowsy3YvboWQK-dq07rLmMTFLTAEy309NSTCAshTp2JFMZQr96tUUJKK_vl9Y5eRZ1y9mNuvN3kfUwiGxWy8CpSUWSjCdICZsVa-8xElFYrmF8D8NW5aN6be3Wd39fhf1C_JkCO-m254aKDevi31S0-TOPme0-bh_N2easv3xxvhYrfwEnlEeiS2rBoQ3jshspRXSc6P4BbRDoK-MXHHu1lgrukn1R0fi9BpnHmb0Gb4-sgF7_x2ErsZc6mDVtYVrlJhf62Ynssc7EtSkpXMKGL03p-mAsgLZ5SNzPz14UsJNFUw5mUsHm0jFFPXa6vTJwIjv2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=J8vnjyN5ThkTfCixowsy3YvboWQK-dq07rLmMTFLTAEy309NSTCAshTp2JFMZQr96tUUJKK_vl9Y5eRZ1y9mNuvN3kfUwiGxWy8CpSUWSjCdICZsVa-8xElFYrmF8D8NW5aN6be3Wd39fhf1C_JkCO-m254aKDevi31S0-TOPme0-bh_N2easv3xxvhYrfwEnlEeiS2rBoQ3jshspRXSc6P4BbRDoK-MXHHu1lgrukn1R0fi9BpnHmb0Gb4-sgF7_x2ErsZc6mDVtYVrlJhf62Ynssc7EtSkpXMKGL03p-mAsgLZ5SNzPz14UsJNFUw5mUsHm0jFFPXa6vTJwIjv2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌ لیگ‌ملت‌های‌ والیبال؛ باز هم ثبت یک شکست نزدیک و میلیمتری برابر شاگردان پیاتزا این بارمقابل سامورائی‌ها در پایان پنج ست مسابقه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24537" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YI0VrmL10E2ncRrLgWI-pPVVyxXzLqiHLOEQQsw_nsAwuPHbIoLbeSRULYe34R-WUMAb4hBsmnpEwZNMugWN_i9EHyariyizXVjQ3bx4bh5C9RppDbKq9iPSKqcXBZcjr_yEKh-frCXPpQ6lXvW0RhWgY6oghs4Tado2wS8FkTeqj9Le19yN0tmdysmneDmSdEwPuUsVsfymsPnRLDUhEKRux785VNLF84KIoEiuQHZikUNaFHNU-WJd4NE_VhFjTlln3o-7Mw2naHE4ynANti3O3vkm6b-GBHYrh5cV-58bMAa0Qw8R7awl5KP-X0jKUX3UwwAfMq6kvwsEJQmy3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا
#فوری
؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر درفصل جدید متقاعد کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24536" target="_blank">📅 16:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz0UdfhdmdI3LtIO2QhM1oyOWbCwVV-ABC-zdvbmdN-RxKEKsriA9EJaSik-8S7C5AalYO8ETP4MrArO78dvk2flc0SEpNGHSOPn5jODckgKBAjqgiwvPhdoMD18boNtCBkD-cpvhWP2ewAeCCOBoCDmdatBxbV4A-OPFDcruXDSiddlsr2ph0SpNXXvBh2X6myzeQoMf7hRV6JrI6qDf5Hb6udbFlceUVABaJTaiVFB3FociXa7Tya69GGf0zfg0_GpMD_874LQGkkoJDk-Ri4QtjBZo0SshtLvzATInKCYOwwxIS8LnJAxAsG-mpAqOsKdK5zymAdrrFuj_FqIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24535" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PL6gMycKzHueMz1xta9laHWqGGWS95HTdODdw73omdjTAUVeIbzggyBDUVB9LuhQy5dVcE5Q73xfmO0cw-3UDEMQM4RjvBnhI8pEHDfBTuUOI0g69pJHFDF_9HsOdALdrtQ4mLQ56Yyu4L3AZPEhgkEFd9MbEuhJM5k_Q4kfYzX_qiCOghOmUVr83m8LcxkERw7IaMw5NaL56ct7ZW9ecqAB0KdPSE9TxTNNRFx8Glau7HmcuWhe7E2VzMwZJDe0FoNoomaAPX17khI2pZIsApcWOzxTOKHvJvNmFQKJMB6VmQSpg7cgeBt2JWjF7UTJUwPp5ks80jZjziesVuEMOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌شایعات‌مطرح‌شده؛ پیوستن دراگان اسکوچیچ به پرسپولیس منتفی نشده است اما یکی از مدیران بانک شهر گفته چرا باید این دو شروط اسکوچیچ رو بپذیریم. ولی چیزی منتفی نشده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24534" target="_blank">📅 15:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏆
ویدیو کامل گل های روز گذشته رقابت های جام جهانی در روزاخرمرحله‌گروهی این‌رقابت‌های جذاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24533" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC__-QJjpnaWRcWm0bxjsHfdO-u0A1az1LD_ntBgZhQSddJQdrKELXVYx3T2y5T70cuCMjwdG95kOjeY2pgC3YLjye_Kk76ex6pdcspninEZ2kL0oe9sNSniAh0itknhJUIL2G68epkp_zObgHBZM9duENZg-fy7d_uvDWux6yH2xvzynPblfvEleGI0ZcQVFqA3B7yFpoKemPwpnH-q76o0S4RDHtA9YI1zNxU0eQDXvyhxnQ9LAsK33cOwIbgRpsYiJ3k_5sOnqd5ZIwDWownE1geHAJXrw3rOZPjj3yv-zGAaa_ZeyalhXvg3bs58GLNExrKPDoLimS5C30s3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=g2PdC29joLj-R78bOn4dyJZVbKwO9A-cOTDfJNNoJAPcZIJmIoebcue1LPFcO7ouJmZj-SPRWgTm8HuWbSwWxab0Xpoce6bsP9GF0tHZMqWY197pwMjT1hEBieiuGBJdutItq7iqddCcRxHTQcO7cZsEnnjZ6eRjqOjDbPl6AB8xPQnID6VHitK2F1WPuBZ56kAD41L9COZnAZcXJfjRRNJpJYs3rp-AS9OfAdJD8VHZZOprdiIEP-5VadXlkiCPCLLzrrRMSJ1GqlHbjdzknaTZdvGtBWac_B91zXCjoUv2iyIOh65vD5UR6mT0rqYMuavbSlU1QTP6FmpMr2uM1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=g2PdC29joLj-R78bOn4dyJZVbKwO9A-cOTDfJNNoJAPcZIJmIoebcue1LPFcO7ouJmZj-SPRWgTm8HuWbSwWxab0Xpoce6bsP9GF0tHZMqWY197pwMjT1hEBieiuGBJdutItq7iqddCcRxHTQcO7cZsEnnjZ6eRjqOjDbPl6AB8xPQnID6VHitK2F1WPuBZ56kAD41L9COZnAZcXJfjRRNJpJYs3rp-AS9OfAdJD8VHZZOprdiIEP-5VadXlkiCPCLLzrrRMSJ1GqlHbjdzknaTZdvGtBWac_B91zXCjoUv2iyIOh65vD5UR6mT0rqYMuavbSlU1QTP6FmpMr2uM1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایعاتی پخش شده که آقای هنکاپیه بازیکن تیم ملی اکوادور با سابرینا کارپنتر خواننده و بازیگر معروف آمریکایی وارد رابطه شده؛ سابرینا در بازی اکوادور مقابل المان هم حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24531" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mg0issjGjOcjbtkHvmwigONfqFlcSPeVgZGzotIqUHX59sUVnm834_MC9VK4JC9G--5KT_POZApIPxaeB6GUi1j_hi5Vgnfs066gFFt4o0WPuou2mdFujYtAOwWv_NKgpMqfZ17sGyhkFCX51x2yKW98tp9UOR43WKVZwvAd6BdM-Jh8kzRIMCKdv60KqJ716lJ2XMO4Iimdo1OPgZnd7hvBSWNbiot8kIgrw5YzNqIctij9N3g7OggxUCSJ6Zh6OILCVH_Ar3vU4rrJ4xPYczEQ7xc9_VRbM2n3B87VKH87FvDSpvIGH3QpfbfAD3UgO9ZQoN1oRuV6JJFwGrDWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24530" target="_blank">📅 14:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4vYQd3o11RzLwJK3KuWSJT9EnLVAIn_70sRA-OGLXLRsCK_mz4WWNbRFf1GHM5TLuvh3U1Pq49IQ7cG6i5a7w_CrTJCei07PnVQUE7n72EQakOlMszq3ZxEkFjoB4G7VsHh5W7FSiSyDTiuJP0KGJ36VouHmtL4iCOo8C1ME2c1wo2gUMCGKIS8-h_0yDYe5ommBnhMPaMvSk3lCqnntQRpbTAhzbMbFdamMWwcLZgwd0esQ2RmWcqlxWHe8psLs9NBbeLt9InVUi2PnOqDpaq_lyNEMGhMZXEeFhVjPl_UdiI68-NNmby6zVYe-zg5EojW9T8zmU3h_pYqbtxSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24529" target="_blank">📅 13:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=HQ43i20tPCZTQVgoD9T5uSBkxVl1y27X8MZdkUF_ke7z_kscWWcdSHMrW55F5z9gUZB1BixyJ8grM-NmcEw93hdZyjoXYcrFLQQY5poxNIJiblOs7k1D-D4_aOkHYHlaVCNAluCaTdwfbdfRvhv0rQWID7jyLf00NgihIAzv8N4tIdcAztiNlP33ZKbn_x4MiTcLcZU0rPCulzTG0WAB0F0l2HKe_E4q11ZiR4iicC51UlfsJRnDiLvIoy66umd27gBGq5vzj1zDzg9OLR_tep-xKsfRxRtuLbb02FzTFYe9280NbX8KzTjwazV_6zBUoM9YRuXMI5TTmhnNKXepjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=HQ43i20tPCZTQVgoD9T5uSBkxVl1y27X8MZdkUF_ke7z_kscWWcdSHMrW55F5z9gUZB1BixyJ8grM-NmcEw93hdZyjoXYcrFLQQY5poxNIJiblOs7k1D-D4_aOkHYHlaVCNAluCaTdwfbdfRvhv0rQWID7jyLf00NgihIAzv8N4tIdcAztiNlP33ZKbn_x4MiTcLcZU0rPCulzTG0WAB0F0l2HKe_E4q11ZiR4iicC51UlfsJRnDiLvIoy66umd27gBGq5vzj1zDzg9OLR_tep-xKsfRxRtuLbb02FzTFYe9280NbX8KzTjwazV_6zBUoM9YRuXMI5TTmhnNKXepjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24528" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=grGbcqRKOQ4TV0-UrZdqLOO5jFi3OYyQ5cIBGfrRr83_i9yCkUOWoB8kP7wczC1iGfYsph3dAYejsjn756iaKGqu1F28-wEbfd0-VjOAagvFxBNL2izpxVcpvCMtgr5Mjps24bZLve1PngEvePX4nl_HrNWuqPO5FcwgxHafn3mTok6j800M6Gao3tH1cWIEO67wa5vU439pSGLuyQcPNl_T-_hBgDmVwHbnEFsz59Xp6AWtErD20_3Bmm3AdrprS3G0yN-hy9oeuiBPlwlna3z-l0n7XjSV-_EKbCUH0HBcCAjoR7UjXmWY-n-ABLpIbSF5CILNlDXOYmeON2tAUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=grGbcqRKOQ4TV0-UrZdqLOO5jFi3OYyQ5cIBGfrRr83_i9yCkUOWoB8kP7wczC1iGfYsph3dAYejsjn756iaKGqu1F28-wEbfd0-VjOAagvFxBNL2izpxVcpvCMtgr5Mjps24bZLve1PngEvePX4nl_HrNWuqPO5FcwgxHafn3mTok6j800M6Gao3tH1cWIEO67wa5vU439pSGLuyQcPNl_T-_hBgDmVwHbnEFsz59Xp6AWtErD20_3Bmm3AdrprS3G0yN-hy9oeuiBPlwlna3z-l0n7XjSV-_EKbCUH0HBcCAjoR7UjXmWY-n-ABLpIbSF5CILNlDXOYmeON2tAUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛
ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر ۳ الجزایر و اتریش حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24527" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGjLHgxZ9pBxHTHF6T7QiWOLq7yYz9RS0VcwMv5rbHGYcXKiNJeaD0XfK07iR9rPCOQUdMiik5cJ8Ff5kCzYbWbz_tKE4g6xa2gfgfn84QoCXs6VinaOH27q1pGFPKU_L_05g_1WjgkGSC_JIzKwABXuZVfunoQShOlAbAqv43egq4FXoTHN5D15Vgb2vVjRyJdtfc7ef6Ht2drcJAO9xyK-cJOiTz-gKrY4dVJjYabO7GRdmZ-Q03dKrChL4m9BIcE6Y77S24ulvANUDz8716OQxCy_FJSk-RyWZasF4Mx5t_eHUXPlUlbrR7RYyO7wFMg42KobTSD6PI-ffxYxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏که‌مردم‌ایران نفهمن و بی عقل آره؟ خدا هم یجور گذاشت تو کاست که ده سال ترند سوژه های جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24525" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=h7O-AiNSwkXNCr-dkY872uIpvvNndKuwp113Syxs-ApNVTjDt8eg-c3HGk8Rd437UpU6dX7pX_9Q7fv6mF7cCeJ3GNj7Uu3ZRXxmxwMzr9zHZVgKTFLEQJeWoVyTFP08e1TP7cLbquDjGBwFBSezKYOUrRtuhbtlejljdw2xo4r-zzIBAjUXrVRGVRJakiIg9iM1-H2mx2a7VoLNuE517ZCut6pNiEgeOIhZIiGrU2SWQGfHVS7ieB8S4ObD5yT92nJakqQLI6p0lDPA-wo3yrPhUh73nGnty6HvoZzZEPX6l82TrqAIrMxMxifBfv6jIjXQB7CSQjfQXmIF0mYouA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=h7O-AiNSwkXNCr-dkY872uIpvvNndKuwp113Syxs-ApNVTjDt8eg-c3HGk8Rd437UpU6dX7pX_9Q7fv6mF7cCeJ3GNj7Uu3ZRXxmxwMzr9zHZVgKTFLEQJeWoVyTFP08e1TP7cLbquDjGBwFBSezKYOUrRtuhbtlejljdw2xo4r-zzIBAjUXrVRGVRJakiIg9iM1-H2mx2a7VoLNuE517ZCut6pNiEgeOIhZIiGrU2SWQGfHVS7ieB8S4ObD5yT92nJakqQLI6p0lDPA-wo3yrPhUh73nGnty6HvoZzZEPX6l82TrqAIrMxMxifBfv6jIjXQB7CSQjfQXmIF0mYouA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
وضعیت نهایی گروه های دوازده گانه جام جهانی بعد از اتمام دور گروهی+ جدول تیم‌های برتر سوم جام جهانی 2026 در پایان بازی های مرحله گروهی این‌مسابقات‌فوق‌العاده جذاب
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24524" target="_blank">📅 12:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNBUxJy2H7z8cTvFXmsW2YqBcNR1Z9KzWD5UK84D5ZaB9rDBypHJXW6oBkv74waFpH_b98J-hnrCQSV70NgcFx-13HgmuwsG8eJExr1YavM3dEtTfw8wIVwjPrCUwfzyfR9g3Gu25PorVgsL30nIZz8hv_D9b-2tHJD4ECgt-8b_caeeIF9oVWxovxy-qzuUU3cR0M8jZIKZPP-P1WZwOBW82BkuXgS9PuPPS83TV7fBJtfkhbKZQuaaRLxfCtuaw8_baeP0d5kRQVolJrtUy4GdpnASzyHRg13zOYNfepb2ssGa7gGxQ58eL2bWqu5RqiM4-GsMWnTs0DcMsKsJ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛علیرضا بیرانوند به‌مدیران‌دوباشگاه تراکتور و استقلال اعلام کرده دو هفته‌به‌او فرصت بدهند تاتصمیم نهایی خود را برای فصل بعد بگیرد. بیرو هم از تراکتور پیشنهاد تمدید گرفته هم از استقلال پیشنهاد سه ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24523" target="_blank">📅 12:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24522">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h88lHYn7SSzRaHhQJki5YiFDxL3rLDoLsvcNgQJKuMG1Pnp-bq9SnlUqlmooixeCaIjcPNuLyfFKz5fQTH68lgITIqp6-AYD6eF2EyjIQwk38qmOeKUaWn2Sf0PdNsFJJqMaCddowt8JJGWUA4TfR50hfQZVfHWItUPnyaHCvVtet9dnDdGnUAqAAQxk4M8I0OkWCu9xyXH3i04Etuo7yqj2Cjq0oMKbAesg_5O6zTbl7a9LK_EfhVbzAQwQAs-3S6DxVnQNu0Gz4ZKhPK6AU3xAWsGeaovRToT_ePCOZVkN2vtpQnMVW3sEs6t2bJbQFNv9s6Vi2bSeOn33SNptFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خود درگیری‌مدافع‌مسن تیم‌ملی بعدِ بازی با کیپ ورد؛ خلیل‌زاده بعد از اون صحبت‌های گوهربارش در تمرین تیم ملی خطاب به پزشکیان حالا بعد از برد دیشب انواع اقسام توهین‌هارو به مردم کرده.
‼️
حالا این‌کیپ‌وردبود که بزور بردین. فکر کنم اگه تو جام جهانی یه برد بیارن…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24522" target="_blank">📅 11:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOmn1WBUjmWZY2K3dc6Xf4zDa_Yeaeou3Rb4st4OTbpSLfyRDZ3Zntfbw_uRS2BCAhCZ7samNyxk-ieV0B5n6RcYcSrRHd7A8EMKns2B1BjgYyFML4GJWkJsB5Zzt8oS_04vRfF5HjRUFFVh9_d5jerdusy5z0bW3G-DasTuY_pERRb6C7_IPoebG4kS4npAvMXsl3gLzBMy9oPbretrX5Pkd5ZcasphHROY7T6QMWQBsMn2xgDhWGroNq2ZlssvGPUqFpZdZE8DHMG2tvecyVYwZI9MmrhcKGW_X1fOAdBnqsIanwKiTmS-cknkLgU3Fp1uhV2GITH7OcHXQdjF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#فوری #اختصاصی_پرشیانا؛قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24521" target="_blank">📅 11:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
خوشحالی بازیکنان تیم ایران ازگل دقیقه 90+3 الجزایز به اتریش قبل از گل مساوی اتریشی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24520" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVWKdpnWkRD5jidI_ttxL6ouON75sNl8gGSM3lplwgzBjFoy_cHQ_4Bf2U0RbuA8QfXXlc4bQMf31JFSg7Z9CnGJZEQLhYA_jF8M3rOEQ7_SAoNYDJji2fZZlwfSFU7L8lRgVz80xVReQ4kSYwn3UwrjAslTEpf0yfhN66X85P52hvgkKkibIs4YSIzkh1EBBFMo0ZT77lul4shK5NFbbMf5aVlsbcEKm4SkXeUxqReM32gG7Ye0hmVMT3j0L72PEbhLd6uenyp6mtMnCLMykHAx6--96sOpSOojyAoNaAC7HNubYdimSuefbo8RbRum-yiVITlpT0JisfsXHu6nlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
‏3 قهرمانی‌پیاپی‌جام ملت‌های آسیا؛ ‏صعود بعنوان تنها نماینده‌آسیا و اقیانوسیه به‌جمع 16 تیم برتر جام جهانی؛ ‏صعود به‌جمع‌هشت تیم المپیک؛ ‏صعود به سه المپیک پیاپی؛ ‏بهترین نسل تاریخ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24519" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=aCJ6ZQaqYs6-SfFFU2ci3Pm-cH4ZJlbC5fbLt-rQUgzqWuPpaItbCyh-eUWhcYYMjVcfD-b9tFnC-fEOEOV_Lqijk_GygtNSLJJ6DMo99HWYG8C-AL0fg7gsJmhGa5ynVsSdlxxhOmCx7MTXI6UGbeikVLp37elhSikxvqE-UWTCXqA6h4NBXVW6QTnk4OYFrjNFH3KopXtm1uj5vrB9oMpHYoYKvPVCxuAIMbvL_vsuCZTgFGVSUH2JxXTm-3FVrwnTX8oN-YTG5XmodgxLYWOxtdVSi0taalqjTfZHJEToQPFVUAnQoBro_jwPnNMpHgngd8k6A-EqSTly8HBrSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=aCJ6ZQaqYs6-SfFFU2ci3Pm-cH4ZJlbC5fbLt-rQUgzqWuPpaItbCyh-eUWhcYYMjVcfD-b9tFnC-fEOEOV_Lqijk_GygtNSLJJ6DMo99HWYG8C-AL0fg7gsJmhGa5ynVsSdlxxhOmCx7MTXI6UGbeikVLp37elhSikxvqE-UWTCXqA6h4NBXVW6QTnk4OYFrjNFH3KopXtm1uj5vrB9oMpHYoYKvPVCxuAIMbvL_vsuCZTgFGVSUH2JxXTm-3FVrwnTX8oN-YTG5XmodgxLYWOxtdVSi0taalqjTfZHJEToQPFVUAnQoBro_jwPnNMpHgngd8k6A-EqSTly8HBrSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌میم‌از بازی و تساوی پرگل تیم‌های الجزایر - اتریش که توسط پیج‌های خارجی ساخته شده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24518" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=V8-VbPgHkLNa0VQ0AWaFgBwrZKaLUM9_mUKwdoYpVuiKh7EV0b-CTBqicYhetTUOE291E5bWSAYYte74sWm1mPHkPJZBNsOtABQei3lDeiWnkMjxtKAzq5ewkIYLoyWkohui8VLPTcZ-qsfxLK-d6qMQS9uO90MgivDJQUUrU5L580eYSI1StgxzdRbY_GzCVyuTcdxpUgftpBeIgnD3C14-QbXdBF59Vukqd5WeSjJTc80QnORwUQmLlyv5Tb7zdRqZ6eSm8QxtyDomOMvpW5BgjQ39Ptoe3iU8T0qYzYaQmkOkXJxzmodS-1nR1uiGnCyCYegvciCCQB82YrdwHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=V8-VbPgHkLNa0VQ0AWaFgBwrZKaLUM9_mUKwdoYpVuiKh7EV0b-CTBqicYhetTUOE291E5bWSAYYte74sWm1mPHkPJZBNsOtABQei3lDeiWnkMjxtKAzq5ewkIYLoyWkohui8VLPTcZ-qsfxLK-d6qMQS9uO90MgivDJQUUrU5L580eYSI1StgxzdRbY_GzCVyuTcdxpUgftpBeIgnD3C14-QbXdBF59Vukqd5WeSjJTc80QnORwUQmLlyv5Tb7zdRqZ6eSm8QxtyDomOMvpW5BgjQ39Ptoe3iU8T0qYzYaQmkOkXJxzmodS-1nR1uiGnCyCYegvciCCQB82YrdwHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ژنرال به زودی بعد برگشتن به ایران راجب بازی‌هاشون و حذف زودهنگام از جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24516" target="_blank">📅 10:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=SUdPGz18KLNMzI78CaTtbOE-6EUrNPlKbEsnRIJo1xqXv4xI_HjrRljZVG08bmsG3FNoLQ4NU2jNDJiywZ1Gb-_vqUH5ERlJxAUiYLN4HBieAS19IhF_Tl4lAGktkq_QLV_l7PULfw9er9r-NjVY2jaMEQMhYvjiqdAhmX8z3n4yUQ-JhCC_J1xKbpWZAbkedoq847e0XCltoPWFLjKCwFW3svNFXrRBgs2Vqwpd0DPuQf-oY6ieOR1L_-9yjYZ-LzQirNzgdUmhi6OipdFY4rvnLMjJlr4H3-uMrT2sdtLzjEAwUKUO10T1RUvXCJ4kZQeL0RmLRvMQcd7TGcpwGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=SUdPGz18KLNMzI78CaTtbOE-6EUrNPlKbEsnRIJo1xqXv4xI_HjrRljZVG08bmsG3FNoLQ4NU2jNDJiywZ1Gb-_vqUH5ERlJxAUiYLN4HBieAS19IhF_Tl4lAGktkq_QLV_l7PULfw9er9r-NjVY2jaMEQMhYvjiqdAhmX8z3n4yUQ-JhCC_J1xKbpWZAbkedoq847e0XCltoPWFLjKCwFW3svNFXrRBgs2Vqwpd0DPuQf-oY6ieOR1L_-9yjYZ-LzQirNzgdUmhi6OipdFY4rvnLMjJlr4H3-uMrT2sdtLzjEAwUKUO10T1RUvXCJ4kZQeL0RmLRvMQcd7TGcpwGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
باحذف‌قطعی‌ایران از جام جهانی و بازگشت آن‌ها ظرف 24 ساعت آینده به کشور منتظر اخبار جذاب لحظه‌ای پرشیانا درباره نقل و انتقالات باشید.
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24515" target="_blank">📅 10:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGAiNwq7X8EdfE1dczyGW65ie9vX-eshJRvVSl3MG-u25v7OWPN6kLCi4jtaeDT2Du_Y0BNauUOoj6aenDCkZGyJZBE1I8YMznfykUZWu8iRyo_9m2FyM35f452IXrcuNBKmsY-UzobcogRVujGgLvXIGz2cTUiCiDIB-eo2vvtTgaa2DtQE4bl3h4yTnIzmRflm9D3zdyyKhRzAslU5N9afeOT6spgdsE0XfCB3VEVYQGzhD2RWp9SiyH__RfZpqkEeuT3lodZhHjw-kCDmCW7Dgztn1ax-h0ApSJU65-zafI2nkvSn7qUDzqVOVoUnuw4vVLaHBTiMQtxunkS1sdGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGAiNwq7X8EdfE1dczyGW65ie9vX-eshJRvVSl3MG-u25v7OWPN6kLCi4jtaeDT2Du_Y0BNauUOoj6aenDCkZGyJZBE1I8YMznfykUZWu8iRyo_9m2FyM35f452IXrcuNBKmsY-UzobcogRVujGgLvXIGz2cTUiCiDIB-eo2vvtTgaa2DtQE4bl3h4yTnIzmRflm9D3zdyyKhRzAslU5N9afeOT6spgdsE0XfCB3VEVYQGzhD2RWp9SiyH__RfZpqkEeuT3lodZhHjw-kCDmCW7Dgztn1ax-h0ApSJU65-zafI2nkvSn7qUDzqVOVoUnuw4vVLaHBTiMQtxunkS1sdGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ مجری بی‌ریخت و مفت‌خور صداوسیما که بیس چارساعته خدا گوه‌خوری میکرد اینجوری روی آنتن‌زنده‌شبکه‌دو صداوسیما ضایع شد. می‌ثاقی هم که کلا فشاری شده بود گفته بود دو تیم بت زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24514" target="_blank">📅 10:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAq1JHTBjCG6byfeizsencfF3KM3S5uaizD8i66Bh3G_hqZq93gGVzOb9-w-z0tm9NcH2RNc43or3HVAAzM5lALbY3YsmBz9apSvpz5yvWLqcu-ARyDANO6CBSzcjXNXTLjYWhLAjgz65PPrN9Fcj35HLDqZTMYolt5mIgchKtqeYl8_Hbmu-i5DpNNx7xyjHEgMrb28ytBVir9yPiGkT49B4-ev5d3Z5mdljs6yVzNIOTIKIGnW0CRAXor1yDYc4Q-7-BVG2gYfaOnxEfS8euCo54xU5Cd4WemdvOu7EejiFZqBjM88R7G7qOKTG0wiG8XTnebQtS9KwOhThYa1tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24512" target="_blank">📅 09:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjoXnvts_dugyFuksJehFPA9OF05PMfIcNgPlS4UhC6sH9uX8q41BXNmEPpLEyPkLAVwPhh_7I0XlvTOHx4DFAZKDFRGwrauMRhba4Aj_1IavEJJ6hk4GAE-BiFGdbmLphTIX9mCotOsS59Z6873OnC5Le4sUtCt7rSR1-JfYbjCnu4AUImozTYVidzFI7imIFO3yRNasi1ZDA03--nXXCxLufKsGCawcVK6tc6AwzXXalW9rI21VVFuXMWgSR9f22b_0DcGaKftbmXTjwU6RlOhS8AXm4q8sUHiHra6CyKuuDBMp3afllpF8JoZiGY3-HQ-91wmv54y4KyqFCqlhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛
این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24511" target="_blank">📅 09:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNDevaB8YCC_A9vZwVyjTXrpPI_fzRYIzAwb54iNBhK6TY-cNnHhOMfU28yeE1oCDnmP25-zv3kEPtYtshvdsruNmiPzGdsyo6uZK1K_vSxjp9x5Qm5xHK0Li3_aqLuX9cZGGKUsM3n_PE4qmkJSxcv7222UVpa3Tray-0Mp8by_hmjG86Cve0Pji9SxqtKWcM3jaHB-H_6Z6V896GRUx0EHWJql17DvyLj_Bj-Aaye78lxuONQRfSTvPTju8ByDiWuL26jSbFDvib8XTvGruvZ5N_Nh84tAsWK7vm054GryfRQKM8HIgsFsFUgiRR74LvBtH0QiXCMFh4lOu-hH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ft634pXzyTrPUgwfxMhG4vCGB8XDEI5MVAp7rDQofAFM0lzch_Il9tVhgQnKVxPqD0xkQEuo939uCDZDglusMGgGhPHGBllYLjKhBnJbfXIAMajpK-TpJQnzmLkYnhvKoKOqVjbN0m0TejhLyvYhg41hnjuz6Ra5Wxa89kYjft3x74dJWYEcoYLexaSCpQKZ16mwc5Vkv_pVm1kc-P3VN0okabjda_K3NoSUtGybWRrORIOiBOsj23jcpkbsAXA6DIvGEjFte4QrkRxsnR8iBkPTyYNGg6CYXD4GsBc-G-T5aqKq7Z9PoxjnOf8I6g-qu7XBjL-9pnpuxhrVybRSjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24509" target="_blank">📅 09:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24508">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛
گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24508" target="_blank">📅 09:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24507">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24507" target="_blank">📅 09:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24506">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=O1Am62hqAIhifU48sEveDednlu73WXWfU15RNTULPvU93AtKKrOrtptcMYRGKm4o62CdMuiP86Tlcezdhfs7JOuNDdKJW9swAw5KFxb4FOYgq3Q9Jgd05rpvMnhZIqccJfDTRRsWZFAT-p_Oue48x2Vl2pi_Hz-7rvVND4o2SJT86GaY7Sr9T-SJrRHDz5DQ_16YL4xzU1BDnRfLdwYrCxEeUj2mvnjDjUV3AvAg87kZHMyoNdgsiqPV9w5Uau5kicI8oPf57X1nIFx3mdUBYG1nDvQVN_hLpSWR-oOlfCx0AHchqvKKeUYrvvEbaDwwbdAsedK2Eo8b7anbSNiUYwgmh6dM64CykxDXqRHGUOCj-k3xpKv4Rs84tc-hJqFhB1l1h6xqBACAFmLA9vrJvlccq8ExTGE4nTxr9QAp1jNscqklHutJVp2Q1vhSJ4pjgr6v5tF3qUPEbiZ4UjSGKuVLwn1UJemDtW_oAFCjPjdDjzyZNxAxUWy439OaAG9qW-3PVYNsHuHNpCK7aRaSdmGe5gzEGh_EAtTmR5rDAh2DymXaujI4BSqfRe3-nK_WuJP1bGulju1j16MWd6KYgFvgRB_BKqNY2HCulDMwPS2nDf6uSLRrjRW3jGwqp8NC_qhu09ZymK6swWISuWIwO_7p_Nxyi7UJ3kR7sUiaQ_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=O1Am62hqAIhifU48sEveDednlu73WXWfU15RNTULPvU93AtKKrOrtptcMYRGKm4o62CdMuiP86Tlcezdhfs7JOuNDdKJW9swAw5KFxb4FOYgq3Q9Jgd05rpvMnhZIqccJfDTRRsWZFAT-p_Oue48x2Vl2pi_Hz-7rvVND4o2SJT86GaY7Sr9T-SJrRHDz5DQ_16YL4xzU1BDnRfLdwYrCxEeUj2mvnjDjUV3AvAg87kZHMyoNdgsiqPV9w5Uau5kicI8oPf57X1nIFx3mdUBYG1nDvQVN_hLpSWR-oOlfCx0AHchqvKKeUYrvvEbaDwwbdAsedK2Eo8b7anbSNiUYwgmh6dM64CykxDXqRHGUOCj-k3xpKv4Rs84tc-hJqFhB1l1h6xqBACAFmLA9vrJvlccq8ExTGE4nTxr9QAp1jNscqklHutJVp2Q1vhSJ4pjgr6v5tF3qUPEbiZ4UjSGKuVLwn1UJemDtW_oAFCjPjdDjzyZNxAxUWy439OaAG9qW-3PVYNsHuHNpCK7aRaSdmGe5gzEGh_EAtTmR5rDAh2DymXaujI4BSqfRe3-nK_WuJP1bGulju1j16MWd6KYgFvgRB_BKqNY2HCulDMwPS2nDf6uSLRrjRW3jGwqp8NC_qhu09ZymK6swWISuWIwO_7p_Nxyi7UJ3kR7sUiaQ_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24506" target="_blank">📅 09:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24505">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhEKx8fLceSmNjpeehN500YxndYd0FWs1m42peeu3E16e4OQw9UDz9WjhymXID3Vpfc4wXij1Q7al4yumwLCwWq-uZIS0fdhJ5eKqvLA-_58u7oCYm4DjwKZKeF5uybHb5sAqdwd1jPhVSNKpQXV6KzP8fTDU8YegUoejGAyqKAp_P3HMepKRtNZHL8yGS4u067NmVE7wZiHW3oNq4_h2COFLBC0-mH9kIIy_qkhBnQItA1eeDaeMQpQ4ur1xAmUFyjdg7suv8bcm_KcBqqwofWKaRX7P0TL2ojBJ5n2CrACZCjWuwESq6DP1g64YmlbQJMtwlyh2h3sh-Hlu55H6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24505" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=tnuKwQnYCQttpWR1qZjZmEm2CtZTITaZflvYH9W-th0zOKkRGNurb2_eTnEmq_Q3jmlOBHYUhljWY4mR5WXf2qmsBeqyihPyBJc8V911C5sXDxribkwSE5KGhVPCSIuU9wGVb_6qZ1RHHoozV2pQiwzj6O14bQ7j_XAi4Txu_KFrr7ujtHUyq8GPgt06UATSl4nawjwJlG6ICx33W-GcfmNTRcFpOYi_Qv6lfBlmNBQIhoBjyHbJ2ngCaphsZklxq2Z_7xbcg5NI2-_bd24yudgOfQGiqqjCXon1PYIZOQ-fknFKddQt0VB_WEOR8_HYkjxHRQAAgejGFu0pmiMR4CgTS70aP2Qmzer-FmDsSelsFrg2177oW8Z56JgT41Lym-KdcYprPZ7iT4702jQuAKXgcc-umyeqk1IaXk0KjrBNYg591o8mdFGdIlsbhp0cf61A-E-qCJ3RV7txW6ArJjWphEIk1Lo_bnx5dqvOYPB5r44TUzN8VX5MVjmwKD_ahGhkq0fXg75xIf-3oTwBlh9VTXPEtaNlPtUb6XqPq9AZvX022lTZxCswjZLbn3FbON5NODr1Y9tQWdW7AEMb3p1gDBx_HuHM4jgDLh6U0PuZSaeb4yMHAWzV8smAelJOB8MjZhmobTnVh1f7Hp4hIJGPokalrnSyUv553OMV1qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=tnuKwQnYCQttpWR1qZjZmEm2CtZTITaZflvYH9W-th0zOKkRGNurb2_eTnEmq_Q3jmlOBHYUhljWY4mR5WXf2qmsBeqyihPyBJc8V911C5sXDxribkwSE5KGhVPCSIuU9wGVb_6qZ1RHHoozV2pQiwzj6O14bQ7j_XAi4Txu_KFrr7ujtHUyq8GPgt06UATSl4nawjwJlG6ICx33W-GcfmNTRcFpOYi_Qv6lfBlmNBQIhoBjyHbJ2ngCaphsZklxq2Z_7xbcg5NI2-_bd24yudgOfQGiqqjCXon1PYIZOQ-fknFKddQt0VB_WEOR8_HYkjxHRQAAgejGFu0pmiMR4CgTS70aP2Qmzer-FmDsSelsFrg2177oW8Z56JgT41Lym-KdcYprPZ7iT4702jQuAKXgcc-umyeqk1IaXk0KjrBNYg591o8mdFGdIlsbhp0cf61A-E-qCJ3RV7txW6ArJjWphEIk1Lo_bnx5dqvOYPB5r44TUzN8VX5MVjmwKD_ahGhkq0fXg75xIf-3oTwBlh9VTXPEtaNlPtUb6XqPq9AZvX022lTZxCswjZLbn3FbON5NODr1Y9tQWdW7AEMb3p1gDBx_HuHM4jgDLh6U0PuZSaeb4yMHAWzV8smAelJOB8MjZhmobTnVh1f7Hp4hIJGPokalrnSyUv553OMV1qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24504" target="_blank">📅 06:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HblJRsz3TR4yK1KHVA50H7FQTZ8vetwxlV-C7v9yQHtBtVv0XbpUTrcEZwx1_3fpBU6LURhlkhAgAa9RxJjVn3-fmmPGNj3Ke5qXutap_LEt61ircVAmdnycE7mkHo4BtELKnFLBYknUA4AAEjp4tPwS9zcAOhrEGEPxI4VTgEuU38M4HE6MU7Z3vMjYaS72MvsnEvWY78tDppfcIK3nr6V3kUymn2lSzvniSq51OXwx038rUITwa-WqdfXOcvru9IhBPPCiAd0mIxGylLl2sWJI39BODWYREic65aptKabgjrQ2HK_uBDN4De8PkknCuYrs8OKZE5V3q7DgxOzIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24503" target="_blank">📅 05:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzHOE-1SXcsyG4IpozRwcz7NdejzwP0qYYedCtjKkn5W2b17sLwJKD2zQW-6xKtXFJScEGiURtQYdU0bqmsfy6PLfk_RQpNGNYZUZl6wjxBry_i3Gcg79Qa3PXgRo3hw34Ytjonf80UVuwt4UD6PVEHh0GWMP1Co7gQS0y07UMdukkmW7iF7HoFcrUBQ6UYEVBlVA_uOVLs4B9n4rf3x7_m2RUaWQtaIZc97ijzcEoopuC32G-LIDMUcQz4C51ZMRdR5Po--HxmU_wLyDhoZ8loV5EQG2_kYS8kbbeU9cxaVWQFtGzbA9RW_n6yjz5DqeEz5gGH94Hr9QI7SKd8pjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_GNfu3WKeZHoxouK7gin5W7eR_LP9nXF8gXw0prKU-FU9oYjtgvxR3Ay9Ls-hRnufp_dN8rwpMogmT_DXblLTGTaWhw9oJ5RMjb0nawFjwJRvXPPsFZNNawao7Y_R9APcGryz2mcvdx956F2MLBZmSB_phh9P34kow1Nk5y_OzKeIJtrVqAEwVQm5eecIax1B4hJ-U8ZS4d46Ahr0bhXouATsuxGhEAfAgTILn3Aivx2n4Cf_oHwGNIxJuzavXJxjUnZHEkXVhInQhUZy3NvP1wHmx-1yilKyC6IH_xYlGVfk_ITtq9fGE-uct45IcWr2yJ8EwR0fvbxnk3nWXGug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی کنسله. این دو تیم دیگه تا فینال به هم نمیخورن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24500" target="_blank">📅 05:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24499">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN1hjmROlnGhMnjAIi3YQyOZJcmkBxpFht-KKNaswIGGJ5FcasqiCE82YjLUf-sPF-ehCyuCV5v_uGQYFDAmI0_Na6rOe1o3tqsKR4tNTWUEv2rUlHs3eNmI3NGi-VZCqHqQAfwHBATSZ_MLO1T-cXqB6IMRDB8_BfvebBGTNWHgUwyh8vDqlWa29V4Dzfrkon-G1Tcp5wEPW3KWDA1NXPNJac0gksb-KOoQgTPuwBbKn0WN_8sFJkZym7VjYJ_ST8x46oCyWwC3yJV2VMgft93zMSXAGfjq_7czVjqcnc436rZ5mxOS7n0_vwu6Kc9f6raiZwmFVu-NR6ZPBd5P5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ دراگان اسکوچیچ سرمربی جدید پرسپولیس قراره تا آخر هفته جاری لیست ورودی و خروجی سرخپوشان پایتخت برای فصل جدید رو به مدیریت بدهد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/24499" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24496">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24496" target="_blank">📅 00:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24495">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KktMTaCO0uzpy5lGWNRlukDpQpqJ7gm7ssOvOZa5mdA0oCMocOBRfd8_b0NxaTDhJRM-twIgju9Py7DdGC1t_JfkPqUw1iNE438LG62PECO4AfwPI0YEqO8qYCg5lnepihuQ4xcHhJDs0byZbNx-2bLEFG1ljosD9j542_IWTmqGlGmIi5FQbgYBz_OzsslhCc2YqhN459e8C0BGS4xD5Dfrml0x7Eud6xynzjlztPoG3sCP2a7_YUthKjWDB_EqsHE777VCIxxN8rtYR8800kkNuRX5_mesPfH0kzUSGfL0IB38HSOvToGt2OXCtV_ljM7RqfNalfhstP61i-Et7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24495" target="_blank">📅 00:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24494">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSZ9BffBBTGbAi_w5fI-t5RqqeWIvANqrRwjZ7gYZWa2ItWTKWYaIxN1ufYQ8dXCX2_oC4TAr2BRoOAj_pArSDugWkQI_4I5ihL3bqYfm0gfPePDnpLpks-GiY4vleTTtY55zyXlrLLmnk-4iuQNyhKj5-HMPulw8V3Bn00v1uoS3FBlA7aI8-f1HDbkcgwaz8n0uo1z6yhZdxlqPzZvDBSv3iexEuYMJ39lJ92gScxnTFzh7md-SsORAnUY4I3F9IHfO1m6pOgjEarumTB1O-b0-qwv4QDzBeC5ngGvhIPtnj3FWc5_KvMJRx-jqV1SJ5DfKjFik3TFORK5JwGiow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24494" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24493">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGMGcarcSCeTDvRF92MlkhlW0BHcWCdj8-0fGk_DLYfuDtDOFwMIIzDp6TCbUochs1s5bmDx1NZnBqkeNrxi5_HE29_jq2ItI2Xkls-dP2WTb5Y_HAk0KzQ-iVXYDGOWJbUzBJI2S__JV5w328SL7nS5b_niR9CHwZGgFwzDR3yMmAYqIhEKNyA99LV-ax87pS1yRZujsGTm8hvxr28dNTFP1aWRkCeXb4zQ0jjvXgXsibY1ghiXYYQQkz2CElz3gSmLQUpZ2ltu-1TlrdFkF7sodRCyF5HdW8mga5-ejHhy8YlpEunjN6OZ2CPsyJlvMYqWLcyDI-iDW2wuIHVTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت‌نزدیک‌به‌مدیریت‌استقلال به‌ما خبر داد که ظرف 72 ساعت‌آینده گابریل پین قرار داد خود را با باشگاه استقلال امضا خواهد کرد. همچنین به محض باز شدن‌پنجره‌تیم، چهار ستاره ایرانی رو به استقلال خواهد اورد و ممکنه که یه مهاجم خارجی نیز بیاره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24493" target="_blank">📅 00:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24492">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f250d91879.mp4?token=Sew96AwXJWAJq3LqhNdxHvFwrUhyRyqwrkmm54TrNYwhYx5cAbEdBsVCGrKD5QgGIkhnQO0zS0XeGasw9ek6XpvkAHdnMFxxbATrr8cXq8Yp67_wgmWLAZm0nYbJLAKdigL6-8Fv04qSMDh1OJWXM_m60Z8_nk-OMHVOAoUR7DCCN-NHA1pn64Cc1PiAvLNZLvtb9gwkMOw8eoUHYIFFUCoGR2dOivY6WktWLfiaGEEwWq17Y-u59WqN4sYerjQ6fUASof2oPY0YZAiYVKGNCtpuUGOHx816KNKfsV2PcrPvy6a3Ff7-ba0Lc7T48W6AT9JBRdOcy1mZapOgnBqyVyDRMeTaesOytekAmZMlgFJ3cYKfEKGA2jMrEvTugnrj9tOPG48kz-BCCenoSnRJ0Uznd81Gn6TGNethD8zjsuZzisSz1VGYvDcTyh42QzBACmdy0GbhcLen4WI38z8UnXB0fh5XNoQQllNkU7n0qG9BVRp6Zx1aj8q2Qj1RcqXwDZIGLVbgjJDYk7Qj4fVKIMNIKd5fsnpnnaHLZkQuNSMhUeQO0Gk9cO_3YW_e3JweFnIzGIGsd_TRk1mllrhn2uzsh1ko4nS3IdGduOXmIX9ktYAU_N4RSOf7YUk1e4oVZ05BS4uWcp578iObTtmlK4Q3lthIKyQx0oI3ph0i09U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f250d91879.mp4?token=Sew96AwXJWAJq3LqhNdxHvFwrUhyRyqwrkmm54TrNYwhYx5cAbEdBsVCGrKD5QgGIkhnQO0zS0XeGasw9ek6XpvkAHdnMFxxbATrr8cXq8Yp67_wgmWLAZm0nYbJLAKdigL6-8Fv04qSMDh1OJWXM_m60Z8_nk-OMHVOAoUR7DCCN-NHA1pn64Cc1PiAvLNZLvtb9gwkMOw8eoUHYIFFUCoGR2dOivY6WktWLfiaGEEwWq17Y-u59WqN4sYerjQ6fUASof2oPY0YZAiYVKGNCtpuUGOHx816KNKfsV2PcrPvy6a3Ff7-ba0Lc7T48W6AT9JBRdOcy1mZapOgnBqyVyDRMeTaesOytekAmZMlgFJ3cYKfEKGA2jMrEvTugnrj9tOPG48kz-BCCenoSnRJ0Uznd81Gn6TGNethD8zjsuZzisSz1VGYvDcTyh42QzBACmdy0GbhcLen4WI38z8UnXB0fh5XNoQQllNkU7n0qG9BVRp6Zx1aj8q2Qj1RcqXwDZIGLVbgjJDYk7Qj4fVKIMNIKd5fsnpnnaHLZkQuNSMhUeQO0Gk9cO_3YW_e3JweFnIzGIGsd_TRk1mllrhn2uzsh1ko4nS3IdGduOXmIX9ktYAU_N4RSOf7YUk1e4oVZ05BS4uWcp578iObTtmlK4Q3lthIKyQx0oI3ph0i09U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24492" target="_blank">📅 23:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se3yBcc9jYRSbnV5_6qboCtDYn7iuVcotoNBxiDwqEApAmORyMnzpvEOePABSm0hA7dVz3vIsgzZlsZuTiIL1nQzmgOXfLerFlYsF6v994hhlq9ds3hBpG7rIbXPhP2J5V-fKF61M_WMgQBIgRgHcSQ6daVZzXn4aZXCdu0IPpxKFdONTTQbuTylKxtEePtwYP_ZXJCPRq2Chu0PCSlFG9jZonMT5i6IU8Q9bH4iS6Yu5CqFaepZyUqgO7_r1wd-g5jeghGTfFx4WFlRfY6rK_115TRSQCiAAQZEddjunSIncZYC64OTUeOXnWuNFY7mPaaXH4qaTO3nvn6ZGIby3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
دوئل فوق‌العاده حساس دو تیم پرتغال و کلمبیا با قضاوت علیرضا فغانی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24491" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jH6J5IOh8gcG7N8Ks-K6_c4jNcQCBhyqQ871fRVdyhkwZZsN3Nm-7drxJ7jok4DtkZJX5coGOd5hYBuVFCgFzxThRAhcGQUfEPvQC5N9rMEnN6z5UdFQAtwyYnbeCXbbp-sGLF84A-jqhpp9wkWzMrS_0rwMvmgAWKtJN8hqqSGAMEIWH9Zy55wwMgK--xTJHOQ6z_nfa9QfZCwpASCn8VBtx2rr_49HTm8-OW9TaKnMegc7GxjQrsP2fyss5XlWr_4UwwjiyLetDvrfwWlxd7c5qnjtqZ4XpY7MApy6kjEu6cHiPPxacgUb591i20z8hoOZzMuBbDE9-adc_Jg_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
ازنمایش ناامیدکننده یاران والورده تا تقسیم امتیازات در جدال ایران و مصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24490" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5TccOtONd3JZicOEleEocbw_T_slWkZgK_G7WSxeUy6jeOfnUdzLKpKQlxwjkmb6hamzTYgVOwU-3a1X2W8DLZm9YQi1BmESFVZUueZmGzskn6o8USaJ8v7KcrsuspIpVFFmJbKisYweDjnZMyu7NPTPbpIuKSVWhhbymQ3FC0wqMo0eTv2nB4m7ztS24RrLeqmifsAvGbNOZwfXa2iVbeOUIqwJDFUtpkq0uXGYTjbbUBusgPFUQsWudU29vLjbdNsNTih5jtlT3U0n86dywY_mCtA6qhp-i2aybY5OavW3GZbd72VujI7duwgjNrxS-Hmfw-Nf6LsiaXIIOw-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
هنوز چند ساعت نفس‌گیر دیگر تا مشخص شدن سرنوشت صعود ایران باقی مانده…
‏
🇮🇷
ایران برای صعود به مرحله حذفی تنها به یکی از این نتایج نیاز دارد:
‏
✅
🇬🇭
غنا،
🇭🇷
کرواسی را شکست دهد.
‏
✅
🇦🇹
اتریش و
🇩🇿
الجزایر مساوی نکنند.
‏
✅
🇨🇩
کنگو نتواند
🇺🇿
ازبکستان را شکست دهد.
‏
🔥
🇮🇷
شانس صعود ایران: بیش از ۸۰٪
‏
📅
تمام این مسابقات روز ۷ تیر برگزار خواهد شد.
‏
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
‏با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽
👉
betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24489" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=Nv6uJwRcLuOM3uQ2TlZvDJIct7hsNtKYx_JWptJNGSFieOwV9L0VKmOKE26pzkC4qPB50DZY6T864Hgk6XuLsm5T9mHtCVFajcNEstxYvJO3__E3BRWOvkb0lUL69xN_7kM6HvuXnGZSCV9GfutUnk2UJ4w-Zr5Z8eq8HsJGSeFolvXRZjQWMYEGJEF8vRBKm9XKaSBpURdAm3Xgd_Tj_BZEBULxrkwfOP7I4ZomXQaqkqcVMaHvU0BkCbIDwKmOG__69Tyx-2FYSc2WO1NF4G-VuzLInjxew_QAlIlGyYjhR0dhFqGyVFI0mpjwMPN1_VlN-WCL0nKXzb9ztFivAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=Nv6uJwRcLuOM3uQ2TlZvDJIct7hsNtKYx_JWptJNGSFieOwV9L0VKmOKE26pzkC4qPB50DZY6T864Hgk6XuLsm5T9mHtCVFajcNEstxYvJO3__E3BRWOvkb0lUL69xN_7kM6HvuXnGZSCV9GfutUnk2UJ4w-Zr5Z8eq8HsJGSeFolvXRZjQWMYEGJEF8vRBKm9XKaSBpURdAm3Xgd_Tj_BZEBULxrkwfOP7I4ZomXQaqkqcVMaHvU0BkCbIDwKmOG__69Tyx-2FYSc2WO1NF4G-VuzLInjxew_QAlIlGyYjhR0dhFqGyVFI0mpjwMPN1_VlN-WCL0nKXzb9ztFivAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیویی‌متفاوت‌ازگل رامین‌رضاییان به مصر؛
جدا از ضربه دیدنی و زاویه بسته رضاییان به شوت زاویه دار میلاد محمدی با پای راست توجه کنید که دروازه‌بان آماده مصری ها رو مجبور به دفع آن کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24488" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
