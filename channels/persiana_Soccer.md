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
<img src="https://cdn4.telesco.pe/file/Sj_AD5fqWsUfV7kg6KEA1B7cVyu8TYJ1u2kzHAU9h8ok4dRLkLTBW05a0r5ogGRzP_aZpEpDGK74TpFvjoHxrUHwUulemIxpci3uQ-b7uIX_1VerRCoaeCw1C-m0FSby-sld5P8ugtBMSRygfovWr8oqNGcx2DGL66u_P0rUSUxN2CrK3Hu9OcYxocAeXVNXQiwpEP0b060Ri6RGLCDXFyKy-FZAufaGhygqcaJA7cbOGEjYFxzx3uJveC40SuqLctIiCsepB7CqKHOdPykp_-4ebG3QV6kaxr4PFQ0bKdj8DsWvpjF3IA5N1DW-2CRd5bKkyKQZ-q6OrIXKkdhEJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 517K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 22:20:19</div>
<hr>

<div class="tg-post" id="msg-26013">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/persiana_Soccer/26013" target="_blank">📅 22:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26012">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNa-DZyhdu0zjaloaIhJVHNEkXK089UATrl5XA7xTLejZeLdB2lvpN6EH--EMB5_0sk4FVzLS1Qh2pUZfsUzlyEYe9yQrYiwpMWvcxXjyFLM4GxwtMOmkBY3YpE5D0limTeUYWQyQ7g3icPYJ-24CmRq4BhDyx3DIa11fy_C1S1n_1fvHtEOkZ638SnNvVScPjeDDvg88xL6H-zcP1WoRKdX8oOTsxcGz4TuYDFgwNf2M7alF59XRMz0Z2xTDcreMwS1qGviw1r_efgPaQVp7bkXjavT5gUp-6aZNSDhgbPV_xvLc-Bxj-usoEfO7WIT-P49yOA_TSYAQOLCesww3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/26012" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26011">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUsD5BhORhVAWqemHOgNJOxVnSpnQ8fsQ9Yca_leShzJx5elYMoY6_0W-s7WJdRnuXdDLPpK4NcGEwgd8oDYzZnlQt-4ohgLMj9-kcwbnYeGMKeRHxr3MlDbO3Tl8BNDoMRfGjnm5YWNDdmCvEb1FruhQjaf4BSWZLcFLcxL5i8RWn80TJG6x7YTRnp5En25DEesoRiH4kg1DnKHvdqqyy86rvyy09KfjXpebyDAaY8yUXs4Q0bNCWTKAgY03_cKJK4-K5NmQ-Kjy6dmWi7Wd6FoFbpMinaVAiSqoRAGHxZSJycNsTC14R4XL5ehGG4yH62Ur47I6EDh9zz-0aoC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/26011" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26010">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrbU4ft2RZkqOcAxqy64WMqvXMp77LOZ6hZRiOvhJLOwZYpdS5olLAZjXP2IAhYKoT6dDx5MNNyNQTKtSlJOReOvzzSGMuiVuctXawNqM82RfrZbfNt-WU5m-26laUgo1IOcNjPbi7gKseMTSCB3VlxrSg-UBmiD2QEzOZfGEPRLTCeoI2Z5uYE1Fblsl943QRf3PPHrgM3u-rwU8VeXYI0ElC1kkrqjjXth0-ccA6TN7OvV63DTC4Sk37NxhazSrXaNMuLy-m0YfdI7OuV6oZJz5W7cbFEv5ukwFg2qx1MbNPQuye1axSdzgNHly5ZHulk3hrEKELtzXTmtwpZxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتاین: آرسنال هایجک خورد؛ تیم چلسی با ارائه پیشنهادی 137 میلیون یورویی به آستون ویلا درآستانه عقدقرارداد پنج ساله با مورگان راجرز ستاره ملی پوش این باشگاه قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/26010" target="_blank">📅 21:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26009">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy4Ae5fCdtjH0GR8iW-pi_VD8T_DJ2jCW0xRvcXEWxHvu5th5YJCaemBRccr_rdLLwJ4S-Z05YyPMrsaQAhaftnBIikzx4wLezJ_LwrFpyeKWB-AuIoR50ADyegC6unuomJiGxh08vU9Bpqtk_eNxoYey12sAi__PVRU3HwWM-VkUJxt8aJUKVr1WMeCiZhOdEnJ5pYUh6IFR2PFFbMW9mUAWUCJqZOpsTfkgfuKwF2amNN83BjkiJjyBTBhYKigZQCzClwDqne8ZnHIfOoGFpIFx38arFFkLxURFNzUwZjVM8XuTFWJ5vblTdMsX2u8BKltDmOt0QnwRuvLPJtxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/26009" target="_blank">📅 21:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26008">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=nuFIf8QsmjePisUFiPJ0f5o8nyF2SRxhVc8jqSi33vTDJsNZ3-vGF5KNjmF8BoWXGEuzpHL38ud8OiLEf5zsMGp9r3Ve3GLEVXa5TrKtoFKMD4xXixX2qmmSftiIkfnFCQlyQH4vaiJDMihPcvhnCyFbF2xXHT9EXrcTGbqbByyprNXm3YKa6nEq5enBQorx6k0OiGxwSGiji3B6ge3kiZ2rg1S7dCSz_-F670SIzWs-j45Cg8ZVFdlcpYtMyZ7GLgWm6DOmW_ApuTUfJNNvvD96YRv2nlWEjEQRnr2wGc1rhvu1dGBeYEtG6_rhhCYyQFYAgydUxkNgNQGNPlHx_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=nuFIf8QsmjePisUFiPJ0f5o8nyF2SRxhVc8jqSi33vTDJsNZ3-vGF5KNjmF8BoWXGEuzpHL38ud8OiLEf5zsMGp9r3Ve3GLEVXa5TrKtoFKMD4xXixX2qmmSftiIkfnFCQlyQH4vaiJDMihPcvhnCyFbF2xXHT9EXrcTGbqbByyprNXm3YKa6nEq5enBQorx6k0OiGxwSGiji3B6ge3kiZ2rg1S7dCSz_-F670SIzWs-j45Cg8ZVFdlcpYtMyZ7GLgWm6DOmW_ApuTUfJNNvvD96YRv2nlWEjEQRnr2wGc1rhvu1dGBeYEtG6_rhhCYyQFYAgydUxkNgNQGNPlHx_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تو زندگی همه باید مثل علیرضا فغانی باشیم که حتی اگه داور فینال جام جهانی هم نشدیم از تلاش کردن تو زندگی ناامید نشیم. امید کلید پیروزیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/26008" target="_blank">📅 20:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26007">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV0bykgMIPge3TPs7ONxHCNsEW59pgU_WnGTk7UpVkf8LGoCPA6au6rQmB5prYXsjzXgREeAgLa3_mlTA18GXPkNwIlriN6JH5A572Id4MRzOSVSxqcIRgmj5BVY5HKvsiGRZ06g1bKEind6h6gyT4scIQjOX5Ux3nB8QPG0SQjr32ALXbEFbrmLfF1NkkwTo0J2-ftr8JeIA1W09zzyj6CoHdihdNDVDUBIxk9BJrWumIJrI-kdwHV6IM1SIyLtCJoyMfT4XYAKvd9CamaOAD7DQ04F4gd4cEq6qkp_m2z-iMxiYtBxUUJm7NAWvckL5FiB7MTzO1mZ-tFt4pu5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/26007" target="_blank">📅 20:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26006">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcMnVf1hDV7EOw8hBpUleVHFmZbYGh77HpPxXTOIjLGSuBNxf_EqQINrmiRsWV9HGwzytAkg3hnV1xCIoEJAnqFHRw6sDQ_AnE_QgZtbB30XzifOXCqh-qvpIavSweUrGhvP-c0_mlmL_pyR399BQlOUzoU0oO602fZoTfM9dIGuWr3OUpRGIXkNd711X5DpSW_BtR-6t47_vIjfi97AYL7IIi2FbJ9dHhT1l_rAYzgyu_wLLJx_4sp37mp3DryTQ1V5ih1UPuBwfzucejMJnsdYjCb5LGTFjiuFSNQz5eu0nOIbw_risM5dMFx1YAXXeCQgetr7QTfJxvZq7XnnnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راجب خبر حسین نژاد هم‌پرسیدیم گفتن تا شب بهتون خبر میدیم که توافق استقلال با روسا صحت داره یا که خیر. وضعیت جلسه باشگاه پرسپولیس با نساجی برای جذب ایری و طاهری هم مشخص بشه قطعا تو کانال میزنیم. خبر رو بی سر و ته نمیزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/26006" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26005">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntVQhJnay-t_biNhDj-9PaycKdk6F8D7zLA9_xr529YRYZ6yf5M6hb3v8BRTyEGwYnMt2onqI3V1vGAUBM-egE-uRctI5iOm3r2TzrTWcLZL8fLvnlbWeDbnL05immLhCjHSjhyVfqcetQdBOhRZp8FUNfNNd_S7XQzyVVWn-5h30SzsfVjbHHcWzAXwbGpKkESl0A1aV2EDTQD6T54HQ9htSEn7__cxaLL498i-BpVxD_YozJCgl3FW4bpPhebUjM6lX88oLPNXwcJFmENf-kqFfRH8XHat5wPD-oquruKR9JqpYKBbBxR87mi1ZhDmtT2nlfLCRMH9SrTSJn1gcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وزارت‌ارتباطات‌شایعه‌قطع‌اینترنت پس از جام جهانی را تکذیب کرد.
علیرضا عبداللهی‌نژاد»، رئیس مرکز روابط‌عمومی و اطلاع‌رسانی وزارت ارتباطات و فناوری اطلاعات، شایعات مطرح شده در شبکه‌های اجتماعی مبنی بر قطع اینترنت پس از مسابقات جام جهانی را کاملاًبی‌اساس‌دانست. واقعا اونایی همچین شایعاتی پخش میکنن مریضن. سه ماه مردم ما نت نداشتن بسه دیگه کم دهن مردم رو سرویس کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/26005" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26003">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNbS6FrDAXcvTuzmu8Tydtn4j5FiEyU7nLZUx-KYYNwcbxSJa0UboVHiBk8HnlINK-wBkJY5I8RdRMHrK2H2Vx14EAwCJyirJqU__9yzE4EEzWd7QK9QCLbyLFEbxCAFS7myOTbY6B0DonK2vq4mFF5TiV4HLh5Bg80lbmdsd7bgCTzQPYESo03QzbMshCt_FHHO_QMxLMuheVqfzeeSDY8HDl2jSama5-WTJGPOMG1VClPXlQxWmmEromiyrGOy2OZPPlrmOR0_9FAbyMzIVlzyJTTFpxZFNGGzido_yO973z5ck_hd-7EiICGXB7WvcGY08MQu-neTkqREr-gbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
آدیداس‌ازاستوک‌های مسی برای فینال جام جهانی رونمایی کرد که روش‌عبارت "آخرین رقص" حک شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/26003" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26002">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=EAMbJqf3oQ8sMyud_PqagSI86atBqirxrWb-vuKuQ_yIxNyg-0X4x6mYsc6q-Rsf2Epy3HaYzEhJJA-wXZwDTO2BDG4tAEpHBqSkEuxf9NAoJhnEjq3TA7UF00wf6OWKylyZsKjaSKkkZ046L7a-tBnqmi2JehZPm4OGNtelnPyYHl5iwjOPAP_qwcS0Yw0VPOLBDzwu0lz0hHT6HayVO-_VsPfmYBV3AkXtJYTvS5MGAXJBgDNXDDiVlwUm2tw9pq7onUERMX5GHlEVhu4Xi5s18_T4t0n6RXKduLa6_eS8k3NhAE77mzhxF_E0wX4Dnd0RG07qQiDjPW5E3P1bqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=EAMbJqf3oQ8sMyud_PqagSI86atBqirxrWb-vuKuQ_yIxNyg-0X4x6mYsc6q-Rsf2Epy3HaYzEhJJA-wXZwDTO2BDG4tAEpHBqSkEuxf9NAoJhnEjq3TA7UF00wf6OWKylyZsKjaSKkkZ046L7a-tBnqmi2JehZPm4OGNtelnPyYHl5iwjOPAP_qwcS0Yw0VPOLBDzwu0lz0hHT6HayVO-_VsPfmYBV3AkXtJYTvS5MGAXJBgDNXDDiVlwUm2tw9pq7onUERMX5GHlEVhu4Xi5s18_T4t0n6RXKduLa6_eS8k3NhAE77mzhxF_E0wX4Dnd0RG07qQiDjPW5E3P1bqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ درباره مسی: من‌از ورزش‌سر درمیارم، یه چیزایی هم از فوتبال می‌دونم. داشتم بازی مسی رو نگاه می‌کردم، دیدم مدافع‌ها حسابی چسبیده بودن بهش. ولی یهو دیدم غیبش زد و سر از سمت راست زمین درآورد. میفهمید‌ من چی میگم؟ همین خودش توجهم رو جلب کرد. هیچ‌کس هم درباره‌اش حرف نزد، ولی من خودم متوجهش شدم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/26002" target="_blank">📅 18:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26001">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuAfZjPtzJExFzxg-B2ntzgvj7NJcA82yPuQvYgroIb2VtPOPWirRdyIxlrvcl0z0Ye2rCc0E7t_pGlR3W10L0nbJZ4EbfIoFHZXbeve1e5ft8ragpB-e9hBn0uY7t7rFadV-0_0uJp9p0SX8Xl3rJ03bxpfJmZ-1THWfCs6fkExgxSMSTkynLD9_sRQBCPfWK1XxOZ7FiolPyrB9pUtAVMhAmk6UpS7tBH2W7n7MWzRrkzMwLqm1IpQhHIXvI7j8191WZ2ftM6z1JvZeZxDw3N_3Ufs-co0QKWmGDWmtuHB276qBy4kkzGxkNenXMSeQvvBYTP5JfX07sRMZcn0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوان‌کاپدویلا دفاع‌سابق‌اسپانیا باسابقه قهرمانی جهان دست‌زن و بچه رو گرفته و بره آمریکا فینال رو تماشا کنه بهش ویزا ندادند. حالا چرا؟ چون 10 سال پیش برای بازی خیریه به ایران سفر کرده بود .
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/26001" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26000">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqrzsWDt9uj5HDBnY0vh3EscernLFnmaN4rFkoC2E95QffbV91hqnJ6bZ_CtpiAzlmggcX7UWS4-mP-Kh9BrkXCW9tWU_e5iB2RcWZ7rPBLLx1PwXpP18PwaILzSeYIUNvbzj35URkbxm1rmktqfBVVFTS6Ehuo1jU2zybCwhRIQyvhPnOFgaJuTdgObEaqpbB9mFsFR6-DaUfczBX4gCigJ09pPCE-gPuibftwIro5UiLQScJZ1rDH1ihxOJORkpabCe5KVY4Z7oMrXRLZaMC2OzkxsIftjHKXiT4ui89M3V-YZGkkprJBfZgZM2nQXeymLvG6y1BH5F2A7GmDlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/26000" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25999">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKGOy63wrzxyddIIfto0pi3i8cSOWhlqXvtyowgROtNKG5DyUp0WnHVP__8xCYjP2j4HK_s4y68Q4uGvnA8buT7xMm7S9FGwBwRjUxyBwXOf4ih7oyb5HoBC9l5RibfyOCfoq-Bue8Rw-xobR6ww4iddJkXjxEiC9Kg1Mr5c-KSGWXyTO1_ZP75pa12SkR0jaGb1BbT8SmwB3UeuqR-BdeVDvEX4L3uGA3iLJ9HfHUgmdO0zWm9oPmzxc4R0TT56EIWUhhJwB0bESIUFCIXYva2y-9DVBer3Cw_QrZZE6kSRmaA1N8atQwwewucLc-z0oPmlYUJFuKy6j8CfKAVWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1_برد مساوی فرانسه
🇫🇷
2_قهرمانی اسپانیا
🇪🇸
🔥
💵
ضریب:
2.18
‼️
سایت های شرط بندی به دنبال صاحب کانال ARON_TIP میگردن
◀️
https://t.me/+6L9plEThEMk5YTJk
آمار روزانه 90 درصد برد
🔥
✅
با آنالیز حرفه‌ای و تخصصی که روی ، فرم ها انجام میدیم میتونید به سود مد نظرتون برسید.
🆔
@ARON_TIP
@ARON_TIP
🆔
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/25999" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25998">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K76ITIPye2q7Zd2O3zdTKd8-lXKjBaEEy7jKT3kxn162JPHvy13snh-os-4eoDv3vUXyJ71soY2FkqWhJZjmuGFqW5lY1agvxMp4DblpCWYzFPruoefe5Q11ap0puxZ46UUDe93XGR8jgmArDmnJnwh9BtlPOgYKjadMT6C3sPmpN0CDHYTp_pYaHXO4O9yWtskhIs158coVy6WOMgXmhzAMANSnGigPQ8BrGxh1eVT-KaT_yS8gVvpXnqAMiRjyloTzpiByyds3CZvqQLYs_L3pkcYYZyLvOK3RKRm-t6KvYnSLa4Li6IcqjPmzcy4UifW0QbbarAwzOt0qxsOpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم اومده با استفاده از تکنولوژی آفساید درجام‌جهانی2026 باسنشو مورد بررسی قرار داده؛ افساید مهدی طارمی هم تقریبا همچین چیزی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/25998" target="_blank">📅 18:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25997">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQQwEkJlv71g1BV-WSIfFaGABErZ17w0RJnSYkqM3HzLf8FNmlNLipSRHRRPrlUr3p6gl75Gdpkm6R8ShYpBaHM9_1QJ1a3DhdGZQpuQbLBKgFtZEYJ3_JaECUgOGH1I96sYTdtRxYUM-GXmYKHePfjx2_yh8BFciYWRGIgZSNjZ5VsrbQOfY4qgLI_YL82FE7ye1PfxK71_22kg6x4k3EYn5L8h04b1zIGDwUyARkG3qc9RQfzAgAJ6pYdesoPElh-MQlqcD-WkhCO3Uip7xHdiKHKl1xGUzy1dTIm5K8yDFRxEG_uVI3Lj_NgbSSyB7v60rLnHuZ4IK-bCHy9uAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25997" target="_blank">📅 18:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25996">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyDZUAa_VtdKW_bNSgMy6PxNeoPM4ESVmIWGTAAGGaxzQpq3m3a2IICX2Qwcifa1Y_BpT6zvZ72D3yQV5p3VuOwIKLD0JI_vlcwjN5acyem4mHmVtdIE2r6wPLdvACxvcnU8C_zcn3qh9Dr7oaM2sZtKNUBQxhooGJXStDWW82tvin42d9-Xcci6eesyTwqrq2N0_k5G-5yoCB11hOVxwDldmeNfLVWjEQ96kXeM99FkWm4nfSYUuyTXDhCaBLynJ7gfSQ8nm1xgez-2nM37gIPgZOlof_8WB6lTU9NegOkoPLgPuFexJvv7ou2z5xH7mQ3zra23Sixm_mLJFtCnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25996" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25995">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt3xXJ_Vl725FJVZ1IiKicgwsxF9yA7p0LvZQNPPQSzogXFMmY208G2vf9PreMO7msF8gfoI6vN379cSCx8lY94UhT4rHPKfwXfFquRg6PB2EkNejPM8-_iq-WhtDwD_gtFNWq_xxnM1gKXLHZnQAp93pRWaP9fdaeyzaX_elX1qleEi-BOmhIouUurrRWAWIXtOw93ry7laMmHp-9SAQ9w0ZjZK3CeJVQxAuqK3GV3qJQBN4uI8SR7ZTv4w9rRRPGnMH0rpujiENVYlgqzW9pU7cQ2ckSeDLNL3A2nLmgBNTRb8vtCKFGZU8eX5cCs2UsnvHHn8nwFuwifKWLJOzw5c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt3xXJ_Vl725FJVZ1IiKicgwsxF9yA7p0LvZQNPPQSzogXFMmY208G2vf9PreMO7msF8gfoI6vN379cSCx8lY94UhT4rHPKfwXfFquRg6PB2EkNejPM8-_iq-WhtDwD_gtFNWq_xxnM1gKXLHZnQAp93pRWaP9fdaeyzaX_elX1qleEi-BOmhIouUurrRWAWIXtOw93ry7laMmHp-9SAQ9w0ZjZK3CeJVQxAuqK3GV3qJQBN4uI8SR7ZTv4w9rRRPGnMH0rpujiENVYlgqzW9pU7cQ2ckSeDLNL3A2nLmgBNTRb8vtCKFGZU8eX5cCs2UsnvHHn8nwFuwifKWLJOzw5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیو ساخته‌شده با هوش‌مصنوعیه که خود کریس هم لایکش کرده، انقدر قشنگ ساخته شده که قطعاًاحساسی‌ترین‌ویدیوییه‌که میتونید امروز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25995" target="_blank">📅 17:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25994">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=uGRACek6CZzol1z6-MBSxSr8vgFv2fEgGLsVKvdzEiO2WSZPnHjB4XXTpkNOqwjJkup3zEg-ZWI68a1VUq9Ni5_34py1a2bHsLhT7crB8BEevc_Xi5nKtrhEWB5aKRSGsK1XkD4vjIngII28qKxQXtnaK18LS4XlErJcgzAxcGxpJNQck0pgGjkMIu9CaigAGDVYiTFbfi2p75WHNpePT8jLsUmuG9rmQ3Mb_CPGm0baVHGVsCZMHGMWR_-6X8MuhrTKHzNZbcgZn-dc7o9oDRO-IVpDlDA1aNXgtsFEDn8Qjqw7D1xic7ver1hmQ4qDz_FBwwtoZ6noWhE0bPvL6mLqebpD1ztGv7_fXRrOSGQJrfirUguBfPk3t0xmy2BuONzfkye2WEzs5tT1AMIrkaiLS7k1pWbLahRjT_T4hZVPePXVt4xiVzjIBgKP-w1YAKhFWY226eUSMWoN608-Vwiw6tn52HUrJgYjgCyXtb2tWMTMecPMh2AJbhN8M0HAl3jHO2zt5nP0o4XLDlnKTdW4h-_TdQShIhH_UwGW4Sv5SOV-nJFBf_PO23phwan-JERBb1sn17iM_G1HE27Xi7sxT40p04CvWPH4pb48Ua9AZOYPpDIJ5DmY_EW35pIUROTCuDTJKTNbxzTxo6U4XBR97JThl4r3gyuROltR15U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=uGRACek6CZzol1z6-MBSxSr8vgFv2fEgGLsVKvdzEiO2WSZPnHjB4XXTpkNOqwjJkup3zEg-ZWI68a1VUq9Ni5_34py1a2bHsLhT7crB8BEevc_Xi5nKtrhEWB5aKRSGsK1XkD4vjIngII28qKxQXtnaK18LS4XlErJcgzAxcGxpJNQck0pgGjkMIu9CaigAGDVYiTFbfi2p75WHNpePT8jLsUmuG9rmQ3Mb_CPGm0baVHGVsCZMHGMWR_-6X8MuhrTKHzNZbcgZn-dc7o9oDRO-IVpDlDA1aNXgtsFEDn8Qjqw7D1xic7ver1hmQ4qDz_FBwwtoZ6noWhE0bPvL6mLqebpD1ztGv7_fXRrOSGQJrfirUguBfPk3t0xmy2BuONzfkye2WEzs5tT1AMIrkaiLS7k1pWbLahRjT_T4hZVPePXVt4xiVzjIBgKP-w1YAKhFWY226eUSMWoN608-Vwiw6tn52HUrJgYjgCyXtb2tWMTMecPMh2AJbhN8M0HAl3jHO2zt5nP0o4XLDlnKTdW4h-_TdQShIhH_UwGW4Sv5SOV-nJFBf_PO23phwan-JERBb1sn17iM_G1HE27Xi7sxT40p04CvWPH4pb48Ua9AZOYPpDIJ5DmY_EW35pIUROTCuDTJKTNbxzTxo6U4XBR97JThl4r3gyuROltR15U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌بدونید فدراسیون‌فوتبال‌اسپانیا به سر آشپز ایرانیه یک میلیون‌دلار داده که در آستانه دیدار فینال جام‌جهانی‌بهترین غذاها رو برای بازیکنان درست کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25994" target="_blank">📅 17:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25993">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfHEcZQIiHq-oYa48qM3xYnESBnUbmYyWpqq_xsbxjdIlHqLcBVkiUSrGlH4qC-ZYDhVCC5bi6-oDo4TPYMu6oqse_s5krLEKW_wuZk0rj5vPGTfmwfTyLeXPy_F1JDrf4KOdI1S6bR2uXjen__bxsAjkDk4BO0xKCUfzEVZv1vYB5xQu39hKJn1hBC-9nn68jOtoXyrcQMdtuGZseeMPwr449jqwhTZcyU6YUhTkjJiilMQy2K1ogzGSxczPaceCvS4JVRNAGCz683pYKjAmBY-RRhTLgl3jsQbtNrHKhfS0aheo3ABCQkSnil0h3gPZ0Q-WkldlpGKHsbabNc02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز محمدامین کاظمیان؛ یاسین سلمانی وینگرجوان پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و از پرسپولیس جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25993" target="_blank">📅 16:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25992">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpxbr9jJmtSjs2SJEE5zULTliOoEc9PvRUDRvZmAFUr9Un_JUkB6NMRyysxbVYUW6VYT6hFXujwfKsXhUAdY97womn3kFOd3S0HB6HghFrsKdVf1TRcy1jHtko6ZoZHa5dvEA7zhzCU5BFslYOJwoateakkZF8wZHCkC9a4uchplIRyZR1N-myDUr2pmyr1hdM3J1SpGwRnXI1AbRB8ynoQWbSDx9_pb-Ui0h1sVSqdfx1UYR0yBegSU1KjrndqLQlX9A9iXK7o0Nm4aDJRtVrPKO2Ytp-6-1AGuP5mbSjc3mNl7OiETXB9ASpOAqmOv5DmNXOP5ScUAsanaQwYVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25992" target="_blank">📅 16:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25991">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWjLMQ_B1ubGfPIwrha36UKWIPdIut6OSwVMb9abrtfY3DjPcVZIrbO0bE4gf_t2FDkfRecLd6Nhh1vbPdNiWjIVasr66Od9EdjW9K-FXBmN-E1IWMVJqyEKeP8aWYAvaocGpl_sRG5xjNXWRdvneUa-jxumwH2k4GzbYZgyLC2Xbdo1Vzcw6UKB9YibCc-fF3oGhO45umxskuBufGSF9xCcwsiauJk6OBTaF2ZnOa3gQxk3HWjLfuuU8mwjv4-purr70K-ifhLho-B3d0CTxRwd3OSrLk-KwYXweChLLVgrrtWDUhReyVujJAhQBYHbma5YmY2Yna8ODR8vRVKQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ از طریق نزدیکان خودِ محمد جواد حسین نژاد درحال‌پیگیری‌هستیم‌که ببینیم طبق گفته علی‌تاجرنیا باشگاه‌استقلال‌باباشگاه ماخاچ قلعه برای گرفتن‌رضایت‌نامه به توافق کامل رسیده یا که خیر!
🔵
تااینجاش روخبرداریم‌که استقلال با حسین نژاد به توافق شخصی رسیده…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25991" target="_blank">📅 16:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25990">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMC7lz8zOjEcu1YjVKXHR2lv4foUP8Zt0CtaT4clyPetU3TNbz7fRkJ5eDmfIfG7gUzcKePRmQ2DsT7NcQuNNTPWmuNd7R03UlKCRQUiOsFM6dLYbezcqQXXVlgKN_b52ydeMF_cZ2SMhbtKmVmvINmBbZlwwPGXR0zE4ssFM-hZOp_XGO1EQ81B_6V3CMPuq3oacC5dkPGZgrpXCGbgTdVQRszIbfrgLlJ87-dJGnb8iALsuW-v25H_5TaqlhJjkBJxHvUmfZ2qCBg8uKCtHZHQBH7Noo-JrHj3KrsB_Ht5rUBUg6L6I5PG5Ubl2aPCcbbiPAIQPQn-K_YTrIcUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25990" target="_blank">📅 15:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25989">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi4gzXHJN_1j3cw4gMCwolOiZaP8N4-9eqQp7wb3eIuWsQAcL_zTK8QlDoyNh2OG9qXqCj3tjv-6j46eWiTWZGWwSKiibJE3d1074ZqIKsiCXfJRyWv0LFhnxJIsPRayLRXvcL0Sp4QKK1q4Ep9bZfOxk29VvH-RXL2NoduTMA5F97_ipwbN1_nKbKioD-ahA7PAGouwLRwkyKtfqgqUXaFc0rc6jSuvkGeNlznrI8M7FchweHLSFe0E9YBWvw2RkmPkO8OVViJ7YphJDsl79oz0KA2T76Rw7wsbhRuidqFpTgdS_bwT7BvrNurd1E-una63FS85I5aj-6f3jyFptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25989" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25988">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPPlSrofad9kEmVu1ucNgvjcclnAmyvlehcCDl66S76O1kHWXwg4U_DT6w3fac_1MGf3RSwere2cbzSX3JPTWP5iQJUA1kaWho3bZ-9UoQDCKcCTWKfymBA9k3q5ie1dBaat5OHvQsiQbBR6XU3HQfstykE0-jQhQtUipUJQ1KVgBOIqFJLQbD-CEWExeftai4Et-V36ZPEmwAorOG6qKHXeFrmYDnGfYCRN8s5PrUSnIbGknnO7PDjGuIlVZOwiiZXs9SoayRv6uTj2tbg77uQ3mug7Jao-FuwZqbbd1_K2AjCITFPvGnjEQ7Bqciy9V1nkcCTOmaXsaFS5PFfPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ یاسر آسانی برای فصل آینده حضور در استقلال 1.5 میلیون دلار خواسته و ازطریق‌مدیربرنامه‌خود به باشگاه استقلال گفته درصورتیکه بادرخواستش موافقت کنند حاضره قراردادش رو باآبی‌ها به‌مدت‌سه فصل تمدید کند اما در غیر این صورت ظرف 24…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25988" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25987">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/letSSacSNE1zBj5x7PYPzZgL9qAVbMr9fyqNKmZRiNTz_1K4tLThRojlrULGNDr7PukkhsStCsIrI69N51g2FcmMiNcYfot0937WID_NIfi4AqzAStXQNQ6SVH_ZWFJ-As3nxPvtPgTEmnopdtCYMEegmXBaOWBLXrNm4YSE0QmrcHxmyvpOcr6cf53R6AVRv8YS4h-ooPBZpuCjW3xM7nlwaK6PuBzRyQ6LGwF9J0O80nQ_ep15LJlpScEX8XjyZ6rYPtWOGCrBDPOINl7YU-BuyWa3bxjoWdavVD9sw-FEtbGwOaZqH-PqZ3cCK8veEk_LYJ7zilc82wTQR5vqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق جدید ترین شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ظرف همین‌هفته‌از تمدیدی‌های خود یعنی روزبه چشمی، علیرضا کوشکی و محمد حسین اسلامی رونمایی‌خواهدکرد. همانطور پیش‌ترنیز خبر دادیم تمام توافقات با این 3 نفر انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25987" target="_blank">📅 15:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25986">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYxb19mj_Ive4DUdSsZfjcOaqOoIhSO98PrqLsM471ECXC8uXehtSzBMamuQtTRRAc3F86isAV3skG6ZvAmEytcsqdqAt8Ru8GwVFZpk5XcQ6kpaBz6d8yfiMOmXesrNDa9iQ0dy23ByGOHOS-0BMfDwI3aEIRKOT-SYQtyF_uinaPppNFalge2tMizF1aWBatYjSlGZhDO47G1d5u2lVscpbBQ6utl_BKDSAZ-3rqUjnFWxcqmMnNaUdCweDTs32T9-qLXaDuIOhYWhg7fG3oFiPK6ivcCcPYAcaBWCtUoDqt-d3QIflfuLJagDa0YDWAuFsB0Sc7w-HsUMl-fTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی؛ امروز حوالی ساعت پنج عصر جلسه مهم‌سرنوشت‌سازی‌بین‌مدیران دوتیم نساجی و پرسپولیس‌برای‌انتقال دانیال ایری و کسری طاهری به این تیم دارند. طبق شنیده‌های پرشیانا احتمال اینکه این دو انتقال انجام شود بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25986" target="_blank">📅 14:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25985">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp5DHZdLk7b4hnn7zRpL51RkFFyo0i-gIHOUe4Bo8Q6x5BXtcjf_rC7jye-an5jTVpFT4zMUeL2SaV-sC9wpd3B2fRFZ8WoqGcyi-lOFoDbVKeu76fXNGhlLFqLAciGlbY1FqHPUndGx4mNNtK1jsULa2HUeBgz0UChvaf_7pUudT9LTICcKu076gRIcI7jMDcfpTRCOR212NVqbrGUY3jP-yxyE5SCGdtaPxFAOpy834JT5B-fyXT1hL9sXTLkRek20IxrhKLtcbLO8nFtJ4QWj70R4HS1i9OtupS630qIpV0wY1Qks1ePBO-RlWwr8-AW2_ThTK5Fpd82CWCYLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25985" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25984">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFab79s20IHbcdme0YcNP1wzFTGcQ3-4SNVFoxCovKDm8jDv04a1Z7Y9UsWUIBJ0Fw8Rih5JTyn53lS4Wja2vipheLNIPtkpE6nx2I4xz00xv-Dl53ieqoKWT5wXpjQwKr-4BVCz-vbLOsKd010gjpsC1OD_CP3LBGYKFlw2k9ifOtP806sAaZn3XsRbcvsoepMdolLD1VTxCRMbHgTr2pHhWsFD31Ie6Uffc3SiXFnsakl7QvhJjfTN7Ur0_EAgfalBYCnyOA0IY0QMPd-gqBb4qjEDS9u977g3KWmuJvK5Tc-83j2wDU4dwR7wIF_BjsYJXdnDMVZYMuorGQq9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
👤
طبق اخبار دریافتی پرسپولیس؛ کسری طاهری از مدیران‌تیم‌نساجی‌خواسته‌ که کمک کنند در همین پنجره‌باقراردادی‌قرضی همراه بابند خرید دائمی به پرسپولیس بپیوندد. زندی مدیرعامل نساجی قول داده که همکاری کند این انتقال بزودی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25984" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25983">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl5rvXXabkvRgJvwWLmDlR5RYgqu9jGToSKDh_JJdmgWf1KabqdLdRb3L387T9P3sRZEXBKJrgdDeYu-QLY4kjystEOjpusoF8ePC_auteCFhJlrstGo5QlP-IJQgUylTkg4uA8N1SEStMVV8h78uY4VnReYAMf1zxkPmoRoSuG0Nk8sDe7AxhDcDc5fawknYSEwBhZzPOZdCrrz1iW22sAdt-fQFe8mSPOyFxrBFve-e-kwGogYo7-sL9-9lWPxDcAA8A2eXxf4JvpARkUjz_NIg6EaHDECQ6dTUPjPHvNafHTSSyFMIUogrklOVF8Qyuvm0xsSa_SMwtwGdrGBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25983" target="_blank">📅 13:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25982">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB5SqCnaWBlgH3PVcuI5iI8Xx1Bq8AKtjA42bXQfGZmrvKwXHl0oRn_1IUosPN5r_kAR5qitf_LakcfZ40JNleQ1758u13JZ0fhrDVPUxgXqQQ517z4byUy5RCPSKcm6DdZAP52YP52iGSYqDWvVTc1l2tYp-y4-WJ9D9kJP7THPxCLh7to-uoSGzzOw8s5ioWt9RJu0U8RsBxtlNVXB22PrA7y06Wim5sksj5ru4Ylzi9Zo9kOaaKkoAdoJwuid500XZvG-oTUkqYD-H3gTBlF6n5kDFybSpnju97FNzLmwcYFwPqPP95D6Mk6WIcgS_NeIJBWRxnN52S7dd7NjBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ تاجرنیا رئیس‌هیات‌مدیره استقلال: مابامحمدجواد حسین نژاد و باشگاه ماخاچ قلعه برای جذب این‌بازیکن به توافق کامل رسیده‌ایم و بزودی با حسین نژاد قراردادی چهار ساله امضا خواهیم کرد.
🔵
علی تاجرنیا نیز اعلام کرد که تکلیف نهایی پنجره نقل‌وانتقالاتی دوشنبه‌رسمامشخص…</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25982" target="_blank">📅 13:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25981">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byooo9WLllUMShqtDCUyHpl13gdFhkqvwnGqGMQRBBDwsQfnJIQMnBadcSzuLgmlgelrs2enIB-VBFKBE_nnZ7qeLFdhcu_uov-GpDNgmoDUHOmkbfdGPEoqmkEIMxXdLdEgeFyNuU4wqAqljGQ6JHWQFCLOkV92m3mq343I9hJ6fgFqz9qhHx70z8PWD5KNkS-9aNHcR9Xy33PWo0pguHSZps5Q8CiAJOov1CToU-K9xGDJBytl7LrWMtAtv9_3ovdofsmLmMibpbhBkzDrdnneVLW1Ga6neuMHIq6SBbaOR8l2iY5gmRXVQv3wZNipKvLh0kxp6vN8ik649LmQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/25981" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25980">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce_57n8xP8fj6w8xEnnhaD8iWEYuRCp0E-WCZ3XidBPWcYE9A4KO5DzTj2kMp3RmlRGVhdLWOg69kaRJaFC9E2MlY2lntAJUWOnr04Y5OKRFQo5H8_43XzCaDT_ZK1GJLb6UBShOxp_tRxWlg_O0zWSrOEo1p7RV4qmwXepkfaRI6Lka-9g66qdRK0q5aIdlqCS8p1MU9aNAeXa6IlQlvDqMAjOHVFGw6vu7RDnvSnna9SqSqZpWHvpvYgDCQkbyZT5GIYWsxukJvxDZlhabWmQQG9HV-vjeTIlO4RG2KOwpv03xlULwUYhRbNTx1lyKwLTdZMTQWJazerOHBTjhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/persiana_Soccer/25980" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25979">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIPfZ-4_YgjAumi9rYQ19hCSJ0NnRQSrOCPOrNPCep_t2FggqLUSFDyorZm3dvcB5jP3ZOjkm-gqUgg_o21Ohl9dh8Iw_3NuRmcRe5EHs-_7MzGYBDrwD9Xyc9REerbMdS357OPlVMtEedMRTUyUMfvYo48HIRyGq5szyEvyvgLZoM_Bqfd-Q_qk2Fjc1dohk54c7xqqlnu9QQudcHdV-zMsFLtqbHQuyh19Z8jcMu31FgqQBRVFUXP8K4LOuy_ULpkzUJ5LsDBGuAkZBNXxi5dA1lmmMByLF6Yz39JGEKxiwp1zC12gahQpPbUjNdBQbgtRD1fcrH2j-t9UuAO1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه تراکتور امروز پیشنهاد تمدید قرارداد سه ساله به مهدی هاشم نژاد ستاره جوان این‌تیم داده که رقم بسیار بالایی هم به او پیشنهادشده‌است. حالا دیگه‌باید صبر کرد و دید هاشم نژاد تمایل به ماندن دارد یا رفتن از تبریز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/persiana_Soccer/25979" target="_blank">📅 12:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25978">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVc5TroZW3eTXjs9abQ-L1EszDL47znjY3hazgu2Pj_z30GcXB52lX8OrSydC9LVVXtq2XILvlKp5vsAz-VM-wWG76DF0l2STcbuA5AAx3_6xvQJSoloroHnaamyNDKb-KeTtbZJTErDcDyD8IYi6m8sqwEW8CLz-tdqgZsv8fnJJCsYxEa6xBVCC-qURAvMyqdyXvxk4IZo86KZ1fj_Fc1_O6YQ4cFaIp4aoLyirG44qUP-TSuq2DudbXM72_5n3dpzHKRCTJG-7g3jegWB_kXkc03WAw_3bZtZ-V-9O7lqE9lhEpVMAujUlPwPYu-GHBi2wp59gZ-fpPhI7YtVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#اختصاصی‌_پرشیانا #فوری؛ مدیریت اتحاد کلبا ساعتی قبل پاسخ‌ نامه باشگاه پرسپولیس روداد. این باشگاه‌اماراتی طی ایمیلی به سرخپوشان رقم‌ رضایت‌ نامه سامان قدوس هافبک‌ بازی ساز 32 ساله خود را تنها 500 هزار دلار تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/persiana_Soccer/25978" target="_blank">📅 12:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25977">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnN1IQg1SXn8tC4h0MKvxcb0qkmzXNtqLFeHQ2333Wtz71zUz1m36Ohjjlovv3kWqIPaAcXogjaQAcxM9ghUxIIRy0ah6sL_RU09I3SdcddhLwOSD5YJz-y0W86zOqQq8MqXyS53DwzUUIHNpec9DvMt-M-OUIoSSUtNCYE9WXoSXoMuUosiFiG8XKBL9MMcA3XRg388hQBRHnXNkR7e9YrZHxsY3_EHujxxgmliu4AjtehlY33RRFuElrZPqzSnjElJcnmXbTBNRJIhfcpxv_UvxmIrYAC00IZf9tZOKi9-2pVeceLFuAkvntWYIYXc7-lNyWCWnaQh4BTPPGuRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های…</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/persiana_Soccer/25977" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25976">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e239GC4BC3IjqDOipMysJQt39GxZ-wY5LVRx195e2iGyp30O7C_eOVEv5D3GmSR69GAkvIcDTeTYmEJaFu-nZ8bXRiO-E33Ka-3X9ZF2EzNYUFRIXi8V7rq-WvufrJltm8mQlilCDPz805TI-R40qNhzh6y7VJ_wP5UBLBdb3_TjMRT9fCwlQQDpoT4aNBODPwhfeY6Chtye9o-V-vi0rxsfQKunRba5kPnNXIXuB9BFVdQtM4D08BkQU3zp2M1DuQRkzaXafHAGovApQGuVZPs-yzRn5kEMJ-6H0h06sc7NPITJ-sXtQR1a9IKorBLnZUmwRKTGkU4esl0PvWChqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیربرنامه‌های یاسر آسانی ستاره فصل قبل استقلال برای جلسه با علی تاجرنیا دقایقی قبل وارد باشگاه استقلال شد. هلدینگ خلیج فارس به مدیران استقلال اعلام‌کرده‌اندکه به هر شکلی که شده آسانی رو برای فصل بعد نگه دارند. ایجنت آسانی نیز اعلام کرده آسانی هنوز نامه…</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/25976" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25975">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3gx_QqqqWiIoBaIP9zlW63Q9KgWxOuOGG1zbo5EtuQabaaH0OfLoZsKx_VcMuloMQs963GLRXOADYMF8cM1wAcxoqeq8StHw61i-fgg8mrZH8SWRYShZJIDLF5gMDscx5FqYzXnjkHguWNdEdqfGAIrHUHtQ6T7S7gNyUoN8oxqkWJU7nIH2PZvpAOt_KCzJN-vpY2j_VP548W8PaG3Hw5u0IYEkjXwTsW4HFQcDs4uSXv2WVYWGh7JwSaR_GHXgCVE0VnX2BuwWDST_9JKoCKduAbf7K9EuqZfiLJzBtt3-K4LpSQalwg_17JdMS3R6cimS_hSGCunrht75ghaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/25975" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25974">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKNdW_F3KqkzTcIo3C1-WM7f62OUNVKjmMFindwGwMRXG_Da2cm2o6Xm7q5-9aXiIUlqRbcFMxTTo1lSDmSjo_EQ_6aqMJ7zWbHqHKOAiZCcT68d7kPiax5ZEAWqtJeDfIoHyuDHppusckEktaT64odi59vDw4oHwpq6JZfqHJWS_zh7O2ffi9JvoKI5tdEXkoM5W06yHdREtu0gW0zwdBt-kpqYL48VigAypLAXsB-SQ9KbfTCDwMJpe-Ntauoh3aC0thbiuJ4gBPwQzhj8MrMR4UIjyMIK7x98aua1-EAXSFar9H-ROS29WKTN0gs7tUyWUE5tdRM65qEVR0PnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ آفر مالی‌سران‌پرسپولیس به آسانی برای فصل اول1.5میلیون‌دلار بوده و برای فصل دوم 1.8 میلیون دلار بوده. آسانی فعلا هییییچ پاسخ سر راستی به مدیران باشگاه پرسپولیس نداده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25974" target="_blank">📅 11:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25973">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=NQbxTB5aP2hMHtyPeCGBN5YeqipB6x8ReCmzGaWu-gSoOCKAZotf5o-w_mLkcStMo1321THyeQZxu0WnLksZsRz1KSU8n9WllNbLSPELgCxRiIojJpChgqpxnFsd6by_kD4lQuzZPnswuOSymMd4v38MCao6oSU1tVikoQkqVDutD2mA4p8QCBsEgF4wW21oqqmel7sRS99BNEyamlj0TKYmTGFGzrcfp6zIuxPuOaWP4hlxRs-u424eYArNToC3vomETbiXfXEyFyFgqBYBx5Ao2IOflYq4cDImmxbdVaf3PXyPKT2B-mi0FCyRObHi1r86IhnVB6ND4sWj5MbVjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=NQbxTB5aP2hMHtyPeCGBN5YeqipB6x8ReCmzGaWu-gSoOCKAZotf5o-w_mLkcStMo1321THyeQZxu0WnLksZsRz1KSU8n9WllNbLSPELgCxRiIojJpChgqpxnFsd6by_kD4lQuzZPnswuOSymMd4v38MCao6oSU1tVikoQkqVDutD2mA4p8QCBsEgF4wW21oqqmel7sRS99BNEyamlj0TKYmTGFGzrcfp6zIuxPuOaWP4hlxRs-u424eYArNToC3vomETbiXfXEyFyFgqBYBx5Ao2IOflYq4cDImmxbdVaf3PXyPKT2B-mi0FCyRObHi1r86IhnVB6ND4sWj5MbVjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین:
بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25973" target="_blank">📅 11:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25971">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NSC7O6H3ZPbAwtKI538ttRGqpnFSAz1mSfsckRv4A1CUh4-dqnycFVricus-mkwI-QjNXYVQusq_Es4jRxknfTpMX99UM7qDoEROUofm49Vw87n56QbMachAEeSRf7HjzLPgjUtRlwPGT_Hz1REwfwHt340I7c53PPvFqhbQJwT_H71j8jas7Eu8X14uWblsnUUZu3ogpRSUgeQVRuisuVzug-E0xXvuYOfHUHtqlBZUnYoj06s531IpI3KuloChtQk_6ujPPO1FqgKwGkZw2v0u6F66g5LDv7uKwlPuZk1z2mZoM3YUxUT-qT6JL8_IN_NfOt0tlNfY6h0lse6WBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwI6XqoeL7xi0vk-ZAW687-dWSIRw-2WWjV__ft3hg7anvDhz02JHZQirZsVDV2CgAL47iNU3OTYFodOuyjo7QLju5CjvxffpmXHwkBK7w754dB0yBuzwxfAnATRjUr4qSjHRzgdh_EwjIl5kFiPKZQfG7_RGZpywJS6FB8HRzdtjjY8rBAGUFVJLkLOpdZfH6TM2GqGklTfi1mh7Zq_R5NPYIjsauQj9vxOk8X7nQb0nCpSUBg0nbQcG7HCeP_VgG-7LSbGNb9o2e1KTLnmm1YUNGn2iTu6tZlTey-Nentpdvl96RKuF3nKm5B0qmzuQKNhKjfJ7BjNVdS4JCLamQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پیش‌بینی جدید پارتنر لامین یامال از نتیجه بازی نیمه‌نهایی: اسپانیا بانتیجه 3 بر 2 فرانسه رو شکست خواهدداد و راهی‌فینال‌جام‌جهانی 2026 خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25971" target="_blank">📅 11:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25970">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk7Wg_2SbOwTuBqzaNRagWIcOHYI8mmCmq0SjdBpjHMmKb96PiUqzT3l8NZOWhbx6VLFpJEQrKVUqmSzwQ3ONeclMXpZlMzCJMAZk3ynS74IpzlZgC0re9om9rgE_ReF04HWyARGb8bIt0pbq_KRkwodNlbH_josMwis3BHNx91T048NonL3PL-aV6879nUSQu3DYmR2KoxFv0MzO54Zx-ZSp0r88HZW0Zq8MVJNy9C0NTiG0gtPfWzxsZtPd-V1B9UnOfKHSNL-qkpZtEY4n_gM5-vPEVUIvu_hzsfbigR45FdgvROmKlpTObiYjYrOoW-c3ew_JSzZSBcp4UDNQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/25970" target="_blank">📅 11:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25969">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrWEqnf16GrP3-gRisdf-YThIYdoTIDhFPTsEZfo0aolJU5jdOWKcCk27zVvCOdyIAcwDJUfWcV9Z5TC6Zz-R5gmgdmASJ1WyJGhHYix1RrJyM0-Phyfjc-UrrFrl1wGCiIYoqWH4zP93Xld2D-0T5quwYbNs5XBZYCpztkdsexyKLTnrmh_9k7AyleHvgyXTZTA_MZrea74RafO4WTDr3GAL8S8de7LGQkbVLVByJSGqHLpiFdYVhgLLD9HgXv3sPjBHQLkUSXBQXXrODHG4GlsbgN9_YpYgQHtBBTxoq5ea_-Jmvsa3O2QGftgfzXp-cdfEYLVvY0JaNB3OV0XAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25969" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25968">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQLzrtWiw_Fllx-haSvJ2Vx8d4IhRDdBa1Lk0TVGCgtkLOa1ZD8alvnR-nenunLaQJa8wULUwr2BMZSdCu__T_-YVVLD4PWSVJIlD4i6fWMy3Z376CeYIk-1E8xqYlqM6RYgpyDXAstyxGWgyIPm0Xg_ap_EvmOpqzN8zq15_gWBuk_V92uOnjcWp7dweXydKL8oHqfl3dwwRBXXeuJxym_M3tFxmpBoVDeuU4cOsPFOb9K6OYrE4lRrJpKgNKNjV9F3588ryE601ueSs-aXy8tjF7OrzsoFYpmNSGelkoB-NlCspA2RfoB44Qk3NGbYvb9UFq_Olk76lOJn-b4Yqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25968" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25967">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=JCFAQ3dPcydpdwZpiO2PveiGjt4W946WY5fUlx1MTVeVP5zMkgtox8NNlC8j5hS6Z22_N9lzAo3XuqTe7SPwOCL5SSw8tduVwodzKd5FSXbR5Fc6p5geSVDcK5E8TJME7XofdaUdt9ISyWpwLrhDJrrbW2pdIay06COASTX6yVKREsaerkOSY71lNZ6HWcbJwEL97EVn1nm01h16SZz_ZEmG82q4HPJImJRN-Phzx43xSwLwpVtkOrYFAst4lX0nX6O5FVQqGlNGLwrxjJwkw-ikEdaDom2IVgmkSq3mCQk0sdpZy1xzES_UFOloTrQ2D-K9JPmsKJvj8oJWU8l1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=JCFAQ3dPcydpdwZpiO2PveiGjt4W946WY5fUlx1MTVeVP5zMkgtox8NNlC8j5hS6Z22_N9lzAo3XuqTe7SPwOCL5SSw8tduVwodzKd5FSXbR5Fc6p5geSVDcK5E8TJME7XofdaUdt9ISyWpwLrhDJrrbW2pdIay06COASTX6yVKREsaerkOSY71lNZ6HWcbJwEL97EVn1nm01h16SZz_ZEmG82q4HPJImJRN-Phzx43xSwLwpVtkOrYFAst4lX0nX6O5FVQqGlNGLwrxjJwkw-ikEdaDom2IVgmkSq3mCQk0sdpZy1xzES_UFOloTrQ2D-K9JPmsKJvj8oJWU8l1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25967" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25966">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p190H2OyRt8qTQIzbWvWjKLn49izLRuiUrtYbId-pEA_616y9QGYU9QgKZ-JH4d9_KgTL2clZI5et8s0IYvv-lI8FbFhKUSNpsBIUL7PiFIPOIVhZX9OTf6rruyO6S4xAaKYzXMJFEiRodm59kJKet_AMpHswiBUHJ8Is5U1MsKVbKtN0_Dcj9mdKO5MHBgFP0YdcPvozZic-5gfIX-7CeKf67tUs_8TbJv1Py37gO0OE1mGNAZCkG6LSFPfD3AteHtTgJKCKTTF3XXeNX35bsiecO6hAfRI_iTRdbrYTij_Cc0MGv-gAVST5wyU9yhNMdtR0tivrYXdRz9rCyPCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
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
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr27
📩
@winro_io</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25966" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25965">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEvkHzJPU_xD5fncaS0RHPCmefYieGDqx7jCPhgFmnFHoJ7aU90i5Df_IOh0akNxjqShE-VUffa6Rtpj5Hnz3C-FA_XsRF9-Lvp7cWXum7OAFPtRhqyNmAA8Z9vbg2aLjx6XVRETCwmhV0vk3E6AxzKI6l4teANeVeXxbpMiwEyrUt8aGyQx2al5-gQ6o038DYjT58cXIyG5zBZR1oEf6_FyLS3IcrQ6GRDFy86QeL_EJpB2kwrzAEDrLP1k2GNT18u3eVYabrSoAVrS_CXI01ziAy7oY8tlQCOX1yGPmSdyANujPssBuEeWhLAR23_pgrfpBvSWjDCM4kYiZRGVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25965" target="_blank">📅 10:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25964">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSeT2USR-tjMBy9BtKxVJIh_gvGE3qoc0EsUfrcjV97tndyaA7wksXXOGBrDtZaymUunFqrj47hkFN8Z6Core8ybgvNkw0K2VoD9K9aMg0As4FTgVWqFOCy_bOxLi7C7PfGmL9FYaI0GNzMHZPP1q5isbxIwCnqFzurCCNG2H6hME2AwvftTpDUX4awOFfwXslEcEuhsFO_L2EkpJ81cFSOMBN5x5UGp_0X54ZG2ZO3mu54EcJyrSuCtBZ3u1Y5VqYSM1pqq3mdIYzD2xNcJIU2pRqYSrsWrrNI39LmMy9UvGkotioOlN6eg41Xlt1efqlTvxPQguTa9ZpYO9npkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظات کل‌کل پریشب وینیسیوس و اوتامندی و به رخ کشیدن قهرمانی جهان توسط مدافع آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25964" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25963">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=q4UV0Q5ZuptC_oitGr9GmSt7z8MYsOKpclNNM5c2XbHAhigqgefmMZW6L1A__v6FftpVRzb05q76N65DAq6uP-388HlgwTX578XXPydbS6t5LR94pTYuDR0WB2Yer2Sk7yawqRNmTtKLxkkQuf3iv70y7pOMc4KdLP3l59W7hA3egOaJyAOCuu_Ltyrn9_cKX4uFvka5_X2Fs8rAyxIFlQ-BKhwq6rrKk16uQ_l3meBliJzh1-j1iX_rGh0EiHfqmiKs-5_lZo71EC6LPno1vY9Qt3ipD2BQPowpzaYaxfX1XsCzt84AHDiocQPxxTQzcKGx9JkCtj_e9dauChTQGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=q4UV0Q5ZuptC_oitGr9GmSt7z8MYsOKpclNNM5c2XbHAhigqgefmMZW6L1A__v6FftpVRzb05q76N65DAq6uP-388HlgwTX578XXPydbS6t5LR94pTYuDR0WB2Yer2Sk7yawqRNmTtKLxkkQuf3iv70y7pOMc4KdLP3l59W7hA3egOaJyAOCuu_Ltyrn9_cKX4uFvka5_X2Fs8rAyxIFlQ-BKhwq6rrKk16uQ_l3meBliJzh1-j1iX_rGh0EiHfqmiKs-5_lZo71EC6LPno1vY9Qt3ipD2BQPowpzaYaxfX1XsCzt84AHDiocQPxxTQzcKGx9JkCtj_e9dauChTQGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25963" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25962">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zmn-vZ3Hh2X_4Gjdb-3IDY36hzYi9Gr5AnVVmhuflrW4bqzR1h4peZqRoWAqBPW9CQCiGYawKJ331t5PAw3J0uv2OsTM6syExZnPLHn6Csg3eK9GbqPAlbPvPjoZu39_DTcjeFoTirAyQjhj1lnkhb5QuxLuBnrS5aKpUE9ajlc1t66uudOR99JDk4hWSbUJQviw1cPKqDaDyRYI-6V3rk7YQZbgpGqozr6tpvsB5jEdCdn2vj8qA-v2nCUkQKF3zpCiw2E5HoBG4orNkHLbaQXeLITOCD9ZwjAO9-6YNaTD5_Ox5D7EsWVgIvSXkaM3oP3eecNHU5A9_Ur078n5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ همانطور که در روزهای اخیر خبر داده بودیم؛ محمد جواد کاظمیان وینگر پرسپولیس در لیست مازاد سرخپوشان پایتخت قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25962" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25961">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnaGoTXz5BGXyRW7sa-hiYhMj-Y8LUcGH8HdlKdw2nrcFl_IO8cCxdR64EVVjRV5A9KRXC-_QFkE938_-lYE1PXxgXOLquoDsK2GhbhlVlUXwEMehZacZcjaBhAyZcegUDAqYnXdqxZyFRiSQed6jhR0dyyDOfI2thoZk9ZiBFvZBHpce_K7EFsh2_cGQT3JVbIO5su5L8VWVGsFzZ1DE0yXKh6off9cSvppX-oPUm10mbAeqvNcJFQv2lkOtdcQZX3GRKT0UP7juSS_nFNsUY9RVd5gAuCLlSW66L8RcKJj79XZcy-Q410LQN1q1f4ncgvizh7ew1QwUqM44F15-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
با اعلام مدیرعامل باشگاه نساجی؛ باشگاه پرسپولیس درصورتیکه رقم‌مدنظر باشگاه نساجی رو پرداخت کنه این باشگاه دانیال ایری و کسری طاهری رو به سرخپوشان خواهدفروخت. زندی اعلام کرد که طاهری میتونه با قراردادی قرضی همراه با بند خرید دائمی راهی پرسپولیس شود. تنها…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25961" target="_blank">📅 09:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25959">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeC5RYswVDnwg8egxJyHqqeIc_RgVnx3twe3PA5SJWq0SWAemYnjtd4UKQY6vZ2RizhYJBSdF75w5uR1N9T0i4EPHEaQ0PmF-tM-KfYpYoMmivvF2CmDuQ2d4b9nOxvIIYVI5eydWH_WJ1pc1F-dFioKVLl6c_vWifxhTZkg746F72u1F8G9Yprkp6zM3Kf4bWjiB-nKxMhLwIgb2m9lYrznMBPfSeHsiccf7bZI9BnRiiDevmRrWUWftnG1n69O9esdUgUYnL_204U5GVNsGj9P5KCnDGToVYsJY3u-ytlZw65F4pJAC4wmY0fAPW6bkQbdvuu81aB-DCuwcLRrrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تنها مسابقه مهم بامداد فردا؛
رقابت فرانسه و انگلیس برای کسب مقام سومی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25959" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25958">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxJ7fpzvG8CnEXg0G6iYF7Lf2w6RHA4N6WsNUIeCPxhKPx604PqOMBXvGyBG8khJl0eWNnvslsCnBWFFAZSn-pjVkJSp-mq2jlmXmIqXpOrmZKI06HYr1qXD6vFkaXuTI79MNk5ToDu9_SHX3pQgEFz8lA9v5_zF9R0jkz_-4UjrRfZFrdPRKhrTBqUpxdm7D9VS5OybLiG6nPChoIBohbaqKMOpIFyLFflab-FB2Fzw0M7R5wMkv2jMG-Ajiedu9-8fLk2ZftDPfPupo_fJfItjABpZIWD3j5oh4V8Gse_fTw4RKEIGMQfrsUDcJw3s7BZvO3EN6034-aefA3t1dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغذیه بدنسازی‌ویژه قبل و بعدِتمرین؛ چهار گزینه پیشنهادی عضله‌سازی عالی برای قبل و بعد از تمرین
‼️
بهترین‌تایم تغذیه قبلِ‌تمرین‌بین ۳۰ الی ۶۰ دقیقه قبل از شروع تمرین؛ بهترین تایم تغذیه بعد از تمرین بین ۲۰ تا ۱۲۰ دقیقه بعد از اتمام تمرین
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25958" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25957">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=bxSrdfL2lhd7JrawxCg5q_ymeq4GNUDvoKfZDabkRht-_SiGlICIzaSl6NTBCgybJn-FWUi6exdC84LFVnaL3DE3jX5stbtVJ5Kaea7Nb99XcISj-pKzGWz5_h_rIi9ThsTf2Sx2HnEx4bpTYJc4k2Xrnzochmi-yFt81BOKhLHV-kxDHz2yB3ln6lR2S5kPsdDETxgxilVj53nCJ3fUWTo56WbxBLFJ4hOEh9OrHXdfVc3j2_149-xs9LIXuxUuNzyqj-kUQDcqHQCuQUj0F20KpnTyrFzbtnaOS6uNPxrrpia5IW1lSRYM8xa8GyutsmIiZdDNjr7rELssTcXzFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=bxSrdfL2lhd7JrawxCg5q_ymeq4GNUDvoKfZDabkRht-_SiGlICIzaSl6NTBCgybJn-FWUi6exdC84LFVnaL3DE3jX5stbtVJ5Kaea7Nb99XcISj-pKzGWz5_h_rIi9ThsTf2Sx2HnEx4bpTYJc4k2Xrnzochmi-yFt81BOKhLHV-kxDHz2yB3ln6lR2S5kPsdDETxgxilVj53nCJ3fUWTo56WbxBLFJ4hOEh9OrHXdfVc3j2_149-xs9LIXuxUuNzyqj-kUQDcqHQCuQUj0F20KpnTyrFzbtnaOS6uNPxrrpia5IW1lSRYM8xa8GyutsmIiZdDNjr7rELssTcXzFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌علیرضافغانی از علی آقا دایی: طبق قانون سه بارپنالتی علی آقا دایی رو تکرار دادم چون ابراهیم‌شکوری زودتر میومد تو محوطه جریمه من‌هم‌مجبورمیشدم تکرار بدم. علی اومد گفت بجون داداش تا صبم تکرار میدادی من باز گلش میکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25957" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25956">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baIOoEeDOhetGv9jSzkBZUk2iTdhmbuVueVQCQQQZ6moV-BLIVAKvg6Da0ZbQ1f9M-lcRg8LNTm0-gNezQhYyiU1ag_53RuehbSsXUr1EO35VJZmHnc-vHkblBC7xEPazjxoSqnj_MNaF_-n2qdSC8tAC0HtbuSgZFaAVdQqdrhbMYAakw1qvWasn3uMaxGWJctPfkn2SnVPoBpPC4k2mM7Stw5Aqm3E0EtoGH0cqYA2R0XViqdMi-JTMHD37vA08ewySkbc0mWlFJ2UJQKhXy2mv3G9exY7n4d_kwb6N3ctcsPGDk3tYEdeXQLTWqLjHKYSaWT6rtEaiSG0kNoHug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25956" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25955">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gki1NtmWo0lZZ_7sZmNQMmdjegBLPCSS1Hr5lROu6rVh9P5GF3z--ZXvEwt-_Wa_-lov47g9ghaT6IiKIO5XyJgQdd3K2UjT-KGcngeo3ZUZ-rnCMnpfmoH4fHuw6-ukbyvPYdgLEWswVM3kdmqFFoldgVU28BolKGjRpASDtV_FEy-MMVKwYpsoPZkbg1PC4hQxA3XWNg3nvhBu382bL-m2rlSAb2TlDpsh5A2OYs4pjSxyCPJPP0560aOccAftD6G8POtzYqSEVn51bAt4PPCnUUXjtoXeHoVMgH949Tryg8IcdvKmIC4iNTqv2VXyf-UOvfxk_aDzwt8cGVYMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
👤
علی آقا دایی اسطوره بی بدلیل و تاریخی نه فوتبال ایران بلکه‌فوتبال‌دنیاست. اعتباری که علی آقا نزد مدیران‌ باشگاه‌های‌ بزرگ‌ اروپایی‌ نظیر بایرن داره بازیکنان پرادعای‌این دوره‌فوتبال‌ایران حتی از نزدیک هم استادیوم بایرن‌مونیخ رو به چشم ندیدند. زیاد به اون…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25955" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25954">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3aBtZYVgr6eYld5jLcHwjitiGhTA8z1IJT3sEsVkIqI3lKUgKPIl9rx5fkjkqON6A2g3Nx8-LdoiacU0zVlKIex2KADVChmesYVjedZMBvrgNqA8CdYf31O52n6V_-jA1eleT-9X5WQlPFYrVu9t5yYjx7i34H8nEnx0HhHbfY_M4anwuzbcUvV7xI_er-8Lxjs8gDJ9GUZWdQt901rN11kkGrwR8uhawOB6JMIrbk0kbj8WQ_HYpRU-DON9CVXQQe9LDmBsHdklKdWjaaVCaqA7IJ7bG0T2wealrX-JfPkwidSzOoNvdhSa1LmcOnwU43_egyRMXdxKbJlmXcFzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25954" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25953">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLH-XADCRe0AgMBd3gWihahb9IW2QFyc5CsmgyYWzblRuDwDkiKImuYEHKnvNLjp3AtEeHO38yV0GrRen4x_Iqg-8cmNnnZ8FXttQ0QDQ9VPCt8oi-fBezOBL4Z5xY9i7QiFYHAKrIn7clAMANY_4vkP4iT3nEWb3fj28dS44FMMmDE7X-RK2FldfhwjHbyg_RbAGOym2sGjVPtTR8HPofKQDhBSm0J_yBId4ZgP5hr8GAfVYZBXJYTZVluJK7NaM-6JSStBdI7MVQb9etR5CKlpvunWHmktBu52Jfk3Tcz7ysWhya_24UgrHCXlwNCDf-Y5MIHrW5-Wpfjw8252hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کانیه وست پیشنهاد ۲۰ میلیون دلاری سران فیفا برای یک اجرای ۵ دقیقه‌ای‌‌بین‌‌نیمه‌‌فینال‌ جام‌ جهانی رارد کرد. کانیه گفته آنقدر بزرگ است که اصلا نباید استیج را با افرادی چون شکیرا یا مدونا تقسیم کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25953" target="_blank">📅 00:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25952">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnkWg_xW4COSKErgx42hk6a8I8oYsNIZHgjUiJQ86t7Je27hRLcMfpmj9Y0tlfWSpQ6RYKUitJTl2CtWupjO8rYbjbx2OusPXEPiKPhuoZLMMkrCYS803Of2t1omDemm6ybh5jI_TRJnT-JWoQkim-uyRy2ZbOeph3tAZwKm9XwSGVX3MRgVaqWPIee5gO-Qlygys47Vu-FgB_NkC6QCTGvsMsv_rTVeUXf2eEXGK6dNzXivAdrtPFnL809aWsVlNLIpSY9qEWms3WSh3zCEfjx8ZoW0RL6kaefDENKG-kSX6eJKj4vR4Ng_dvmz8Vp59gWQi8wnTwRXFFLVrrfg6qFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnkWg_xW4COSKErgx42hk6a8I8oYsNIZHgjUiJQ86t7Je27hRLcMfpmj9Y0tlfWSpQ6RYKUitJTl2CtWupjO8rYbjbx2OusPXEPiKPhuoZLMMkrCYS803Of2t1omDemm6ybh5jI_TRJnT-JWoQkim-uyRy2ZbOeph3tAZwKm9XwSGVX3MRgVaqWPIee5gO-Qlygys47Vu-FgB_NkC6QCTGvsMsv_rTVeUXf2eEXGK6dNzXivAdrtPFnL809aWsVlNLIpSY9qEWms3WSh3zCEfjx8ZoW0RL6kaefDENKG-kSX6eJKj4vR4Ng_dvmz8Vp59gWQi8wnTwRXFFLVrrfg6qFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25952" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25951">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=IZi4E3JPTYStTEbepAXcvEP4lfrZmEZA8zfUcbJ4qadPvdbmmLsZn5ZrM9FeIE2gEBuuld6dXnYhLVSID4I-3ERQ22rsGuzokUdsBO5vqXz1ZqGGSF3hNBA7DUElTdBB5FT_Cy3xwaYgP3nTjeqoC2EfC4QySqsn2hIgKbxtHvpNN3o5nWUzGLCDs4YmNvl0M0XqwC2X8-xWP8HCcx3eugYTQwA8F73fDBxEqcwY7AGuuhe-k-ic1CEZiLq-6Pr83wLoQrFbvGmJQv1b58-hJnvBHIOL16DrO9DWYdfFHJahRk5tQjUnge0gTq5oIL_v71r-mqgh3Hu5F3Jq0EyVL4sZQgYZc9x0eyjXOctev3n-VdzNkHBAYTkgwtrc4jCSi02etOfM0jHllicRPOwD4MoVbtMS8_5yW9MDFHQkmhfuL9Pa2JzjrdcsERJZmFsS8qHmSGuKyn11WyJfFAUdaWK5FwHFiywPFDov0U0TMfR8ecgkioF8X6R47QxbTCNQ5EmYQZiOL0iRW2sUK2EgY8Z4Y7N6rhXVr4ILIaprjTbdi6DFJmtOQ0UVs4WgpsQDGXpAAxA_do4-xF7a_PnmNhXCYB5eixU1tiOMJjd3qBAkPesPXwo6Nf7qCPj0DFPlyQLkC-x_T0EuKM0vM650yl-AHEHlNukMSyqzbwquCuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=IZi4E3JPTYStTEbepAXcvEP4lfrZmEZA8zfUcbJ4qadPvdbmmLsZn5ZrM9FeIE2gEBuuld6dXnYhLVSID4I-3ERQ22rsGuzokUdsBO5vqXz1ZqGGSF3hNBA7DUElTdBB5FT_Cy3xwaYgP3nTjeqoC2EfC4QySqsn2hIgKbxtHvpNN3o5nWUzGLCDs4YmNvl0M0XqwC2X8-xWP8HCcx3eugYTQwA8F73fDBxEqcwY7AGuuhe-k-ic1CEZiLq-6Pr83wLoQrFbvGmJQv1b58-hJnvBHIOL16DrO9DWYdfFHJahRk5tQjUnge0gTq5oIL_v71r-mqgh3Hu5F3Jq0EyVL4sZQgYZc9x0eyjXOctev3n-VdzNkHBAYTkgwtrc4jCSi02etOfM0jHllicRPOwD4MoVbtMS8_5yW9MDFHQkmhfuL9Pa2JzjrdcsERJZmFsS8qHmSGuKyn11WyJfFAUdaWK5FwHFiywPFDov0U0TMfR8ecgkioF8X6R47QxbTCNQ5EmYQZiOL0iRW2sUK2EgY8Z4Y7N6rhXVr4ILIaprjTbdi6DFJmtOQ0UVs4WgpsQDGXpAAxA_do4-xF7a_PnmNhXCYB5eixU1tiOMJjd3qBAkPesPXwo6Nf7qCPj0DFPlyQLkC-x_T0EuKM0vM650yl-AHEHlNukMSyqzbwquCuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب حسینی تو برنامه امشب میلاد کریمی بلاگر معروف‌ و معروف ایلامی رو دعوت کرده این بخش ازگفتگوشون جالب و شنیدنیه ببینید. میگه  قبل از بلاگری نمیدونستم ده تومن چند تا صفر داره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25951" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25950">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTzBINvXeKBt9CXxrfpiwM9FL_vliWMJpLaEJUHHZeNol7kinQymdz7wfDIDtMD6ZKcECYJ_GksDqODkElTiMzdo8YYHHRxBcc_vHCnjhIJORusszcmkbIKu53vrgK46pH25OFDVOK1JE575OqfbRHSdMgVyf8kaDR5Od7Pg_KNt-rlr6xn7QslhLZs9-p4c1lQolwmnJSYnqFeYWPmHyvlHnfVfwU8G-c2uMDxk16RlOuxoC1QY_60jiwy8k6BOzujP3F1f6L5SlR-QB7ivrvF265nd2Yijhw1NBCbw67z5Orr3YVJ0Ih2dXGr8uK3HDLGMcCMG7u5B7cPpJAoj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های خود را در تمرینات نشون بدهد گلر اول تیم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25950" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25949">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=OzLnqqtm8r9AxnUVIVMoj5frAIGoGt3DEkmtTkMIzBVOAfVntyZXAldVzsjGuOyo91PV2CtkNiZZfxb9ONCUfjRhCTKz33MeXZed4z4hErcrSNkGxv_xQ30tyqs5b-j4X4aigvZkHrNBWUm7BrSGWhic3hy5HU2k4Lwcn-JJv6KvLjLl6EHheLsMj5Fy3YatIfgnUWdw0ubRyydZGpgJ9_0ZZMliltXDJJjprFxE6w_0ovY37dKfFA82orNTOtC6hyhgbWk9hUltBwWj9bHVp1s5fIWrF0V1Qn2nF1Hh9vrpp-ggxzm_F-pntgQEzcm7ZY5ZpRk9ZXV94cOH5Zgfyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=OzLnqqtm8r9AxnUVIVMoj5frAIGoGt3DEkmtTkMIzBVOAfVntyZXAldVzsjGuOyo91PV2CtkNiZZfxb9ONCUfjRhCTKz33MeXZed4z4hErcrSNkGxv_xQ30tyqs5b-j4X4aigvZkHrNBWUm7BrSGWhic3hy5HU2k4Lwcn-JJv6KvLjLl6EHheLsMj5Fy3YatIfgnUWdw0ubRyydZGpgJ9_0ZZMliltXDJJjprFxE6w_0ovY37dKfFA82orNTOtC6hyhgbWk9hUltBwWj9bHVp1s5fIWrF0V1Qn2nF1Hh9vrpp-ggxzm_F-pntgQEzcm7ZY5ZpRk9ZXV94cOH5Zgfyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علیرضافغانی داور 4 دوره جام‌جهانی: اگه توانی باشه در‌جام‌جهانی2030 نیز حضور پیدا خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25949" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25948">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUHRkgltTTiJVGXLD7IRNG_8ANDiRP3mU7nq00woWYz1HdcApik_5ynodTlv9b631URWBXwBeyKHc6RHCatZc9M_n-tlrON9xWwPwoxOzGf6jzslN5Jb-coSF9BG7yWCjNiDqssV-P3xPlwotMSts9Da79lPTmh8M4Tx_d1azP0ghBLX2MT3KdZj8EZkqr2HUFxYAiD14yH5EToYJkeuyZubG4o74FU2wf5XPrdDDR8FizcIWqw3ss8F_ki6X7ljOjru50JLbgyaEbQtj-GMe4XDsth6O0WiZqNyEcI0mW4uu9ZKVRRIS7cFSvQtkETfjxINodvwNHrswoRg55d_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25948" target="_blank">📅 22:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25947">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=aPsrFa0TKJyON5yJTimsCbMQL1wXpZYHWON-zRVb73fYfyh73UhfVZMGZL3OlLWh6puP8_Vhb13hhfGJuJ_RgnvXs6EwNRZUCqnacBgpCM5EOe_TbPUSkVNxRliI3PbFSwOYdZxLnXThTUEGDjS-qBjEVQNRXiOmsBm7n7HktEk7ONns1BMNRVRetY51gLvJ15s9ql8JrGb9UafLOxX3xEjGMUK8e-iFu0m86UxMwDcPU-9ZcEbDtu0Wt3gEdoIhAlVavHmk1QjP3vuZ7m6ZIwH6bMXH13vbofAdSUqRb5AMcLDaXfspBwHPg8RmWTTnGSwpbpI126T9g2jj7RBi1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=aPsrFa0TKJyON5yJTimsCbMQL1wXpZYHWON-zRVb73fYfyh73UhfVZMGZL3OlLWh6puP8_Vhb13hhfGJuJ_RgnvXs6EwNRZUCqnacBgpCM5EOe_TbPUSkVNxRliI3PbFSwOYdZxLnXThTUEGDjS-qBjEVQNRXiOmsBm7n7HktEk7ONns1BMNRVRetY51gLvJ15s9ql8JrGb9UafLOxX3xEjGMUK8e-iFu0m86UxMwDcPU-9ZcEbDtu0Wt3gEdoIhAlVavHmk1QjP3vuZ7m6ZIwH6bMXH13vbofAdSUqRb5AMcLDaXfspBwHPg8RmWTTnGSwpbpI126T9g2jj7RBi1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ رسانه‌های برزیلی: علیرضا فغانی داور استرالیایی علی رغم داشتن کفایت لازم، به به دلیل داشتن ریشه ایرانی از قضاوت در فینال جام جهانی محروم شد. گفته میشه دونالد ترامپ در این موضوع به دلیل درگیری با ایران نقش داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25947" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25946">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuSqi0XJS97jfvzrfSIYoDutEq2gB5Lr8ixaiePxO17P8KcZNEcyHoXzX417LxupFsxPTRnfthfPy3wbl57tbnBCZ3-9dEbzEj9ZgW_tv9YDHrtjBV8f-kbrTvAldbxSHlyV5oCNwKebqMAeQ0nj35U2n80Aq9bBqEQkR947n31hC-qbaKaWVcbiNcIx81WGoiaVG9ts4wUZX5xToUU2lODfpahAxQN-OfKnCJ1Kl6Lqw5T5zdheQLrgMqseJ6ZOuXIahzOccqUdNZ9m49M-Ym5xAGVZMuSzRbBYy5K7l03ww-hKxoKyMo35lwhstyl5Nrs0hphMgcaXhu3uWPD0hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25946" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25945">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5e64BvrQpfrGGVhGfj5uwztY1czUojs6bMvaUgLwLzV7q0d_D-6nTR2yfTXh_7lLkdxp02WTm6s7J-FrXDqzIb_Q6_pexAVLmoJwSl34XPf0RyaEbXQBMVil_3XaqHeTHGQRRIHyZCd8SJFeh5uBUmRJWlvTIT2yK1mNDAKTsDwoUNf8bsPbSMKn23_DlCl1xI2DoJ0uArsZ6pPW59AOVzyLcSMBOBJHOx5RNwd-CFpDuxcz76x6-3pCLD8UT-gr1EM-g6vnIDqxSOBDjzjjveSzovifP599b8x4zHHiE1LcCuw1HbamY2JIO0tusZWS5izi6dWV1oVsHhiqs_rqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌جدید پرتغال: من هرگز کریس رونالدو رو ازتیم‌ملی کنار نخواهم گذاشت و تا هر زمانی که خودش بخواهد در این تیم خواهد ماند. قطعا تجربه او در یورو 2028 بکارمون خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25945" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25943">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=px9llfB15-Ja9IK4W1C1y8z_F2DGGBUz3CNHjzbECOo4AkaaNZ_Z7e33ZYKoZWWRKEJifOTQzVvIzQmuU0MlAGlnrHUFVhq7DPWnOtVo0zYYEtKpFDlQSusZs97iFj6QUA68Oez9ZNOLYia1Zpb4-2nw8RhDutG2smZDOwF6h1a6eMGHSj-GZ6j7yneH1H4SrSrLqJFz5gF4dJOFkPvqQ6lwCGMUFeTQP-RKZxgT7qukPx6div7df72MgNJD4z_mn1zzSyNnstZJWzgMbLY0LlDcrPJkNmvDYWAGbBp9TMjoVhfA9kK8kOwqx-30PLvq6zVECcK38eDuQ4iJWRy7qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=px9llfB15-Ja9IK4W1C1y8z_F2DGGBUz3CNHjzbECOo4AkaaNZ_Z7e33ZYKoZWWRKEJifOTQzVvIzQmuU0MlAGlnrHUFVhq7DPWnOtVo0zYYEtKpFDlQSusZs97iFj6QUA68Oez9ZNOLYia1Zpb4-2nw8RhDutG2smZDOwF6h1a6eMGHSj-GZ6j7yneH1H4SrSrLqJFz5gF4dJOFkPvqQ6lwCGMUFeTQP-RKZxgT7qukPx6div7df72MgNJD4z_mn1zzSyNnstZJWzgMbLY0LlDcrPJkNmvDYWAGbBp9TMjoVhfA9kK8kOwqx-30PLvq6zVECcK38eDuQ4iJWRy7qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لئو مسی وقتی قبل شروع بازی آرژانتین - اسپانیا در فینال جام‌جهانی 2026 لامین یامال رو میبینه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25943" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25942">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=WxREPWm2ggzJGED21l35jNYleci1hV6Vk1jaPk06A5reqdm71kECu676NHERFWnX9amL7PFGyeLx4DZOCHN0lo4hWhworD-kBOm_W8EuaCnsBqkoIki2MJHam7W0w5AC_mHPXzbXYFx4hIcWbF4OZ3DzGvBcjQYn_YeArNUO9fKgp4ooZv0gUDtyB5_Q9wzwqnIP0KwCXPi5FicPAfte29Muuq0MziG3Xl6CQY4UFFcmnV_qfuoJEvn4w2vGonfFT5noLkCQjQpNaZZpDmr2zbgJjHKZ7Ty03eS9FVGt0dhf4HaOFW1x-fv34WI3L_ElheokQWcK0oy2T5bSDihadw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=WxREPWm2ggzJGED21l35jNYleci1hV6Vk1jaPk06A5reqdm71kECu676NHERFWnX9amL7PFGyeLx4DZOCHN0lo4hWhworD-kBOm_W8EuaCnsBqkoIki2MJHam7W0w5AC_mHPXzbXYFx4hIcWbF4OZ3DzGvBcjQYn_YeArNUO9fKgp4ooZv0gUDtyB5_Q9wzwqnIP0KwCXPi5FicPAfte29Muuq0MziG3Xl6CQY4UFFcmnV_qfuoJEvn4w2vGonfFT5noLkCQjQpNaZZpDmr2zbgJjHKZ7Ty03eS9FVGt0dhf4HaOFW1x-fv34WI3L_ElheokQWcK0oy2T5bSDihadw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌وشنیدنی خداداد عزیزی و جواد نکونام از اهمیت‌نماز درامارات درویژه برنامه امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25942" target="_blank">📅 21:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25941">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODV7wP6-4TJhW8yFbJ8LtGwR4UnM_AuyqvsURPl69kAqOt9cEqiceiOUlU79LekaEfjTr7I8iwJD-CjXRBrPiwSjjqnp95DPVHw85lyXb3eV7mUODsq-YyDOngnmj79lxpxZkgCxixLhU6ERyWAe11v1QVaxX-37A89MDrAFy3y2dXoKu-6vCIjuoIzVSrvG-J5qpi39WWO00q6_oDQJ5q8GhxvVnfatRUFalvDYF0G-WWUuHKNyoch4o61TbT626ew8yR1zZTlMPVvZRLlCDmwvI_UyTfq-v_uMDME2I2yFKX9mw1ZqV4yS4gw9zhFoVQBKPGAQwnOfYShfXter6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛باشگاه‌پرسپولیس خطاب به مشتریان قطری اوستون اورونوف: چهار میلیون دلار بدهید رضایت نامه اوستون اورونوف رو صادر میکنیم.
‼️
این اخرین خبر دقیقی بود که ما درباره فروش احتمالی‌اورونوف‌ازباشگاه‌دریافت کردیم. با این پول به‌احتمال فراوان محمد قربانی جذب…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25941" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25940">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=gX_KfQCwiIMZTFDoxeS27fQEUk9Ymt3cr4onqTshiMaLGIK0SGoBksi1_4z1emgpvJPvqDa0ZJSUIBkDNGSG5bwTqZsH5WwVOXRUStNIqywW34E9iI7WD5OMXwx8Z3EHAPQC27AIkhTC2wKaRV0Kj37M-vstXXUGvfT21ZsXkf_xaHNaaMUuwi0Dg7Bo6aJZ4S62vW7kLE2ArscOfLGMuS1UMpTG42_v_DSO7f1Rjlg_KHcVS4yUO5RG8HsAWmZk0W0a4FWC4LXwtgr7nZNixgrLKTkSY__MUwji5UhYN9NhYjDChWXeOr-ToXilrrJEHNeCn_Z4afZvSBAEdZCzcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=gX_KfQCwiIMZTFDoxeS27fQEUk9Ymt3cr4onqTshiMaLGIK0SGoBksi1_4z1emgpvJPvqDa0ZJSUIBkDNGSG5bwTqZsH5WwVOXRUStNIqywW34E9iI7WD5OMXwx8Z3EHAPQC27AIkhTC2wKaRV0Kj37M-vstXXUGvfT21ZsXkf_xaHNaaMUuwi0Dg7Bo6aJZ4S62vW7kLE2ArscOfLGMuS1UMpTG42_v_DSO7f1Rjlg_KHcVS4yUO5RG8HsAWmZk0W0a4FWC4LXwtgr7nZNixgrLKTkSY__MUwji5UhYN9NhYjDChWXeOr-ToXilrrJEHNeCn_Z4afZvSBAEdZCzcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
علاقه‌ شدید پوریا پورسرخ به رئال مادرید
: رونالدو هرتیمی‌بره دنبالش‌میکنم و کلکسیون پیراهن رئال مادرید رو دارم. عجیب رونالدو رو دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25940" target="_blank">📅 21:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25939">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjmQCDHzfY4UFiOpNP0qTRZI5OMOkBcSBtc-p3Q3yFmXksPOYoH8cP4PI8PFhu8IQH5jlCrZdfHZOezsgGwYsvnzZPJGBemlztKxpYPh4xCCPpPOFnNVtbC6KZffZR_Msvd4pp4VSJL3Kg0sGrL8HImsGT_kg94VpGFnJZiqv19WdIahEvdYOIPDgEyZCu3rwJaAWmNUY4tPOC8cLj71vMHsOmIhPhLl5v5Rpa-nVne_GaxOJFw3oIrIvwuqc6lPnCoUEKcPAnhsGxhpMRBR2__OlPdzO3qP9rLuhRlXVJ8iTUR47KNlHO8lWr_XeARoG3ndUvJv5zwlH87HM93LzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایکر کاسیاس اسطوره‌فوتبال اسپانیا:
ما اجازه نمی‌دیم آرژانتین‌چهارمین‌ ستاره‌ش‌رو روی پیراهنش بذاره ،اسپانیا ستاره دوم رو روی پیراهنش میذاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25939" target="_blank">📅 21:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25938">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQOHisHb5dccTKt3fngYU77qvwJNayWFnqyy_IbTOVlf4fOBPp2gbrfEe-8ZU77wpWLDMXouaUrN9Sf1-fTkz-I0NTuxkAB_6FkIEplZ1jZ6C3NE1qzAhzpj3PjTAyRCSP9Q26Yl0M57GLt7gKcF2lWEvk7glQ_bhHSQ1Oxb04JxtzHelqO2-mgqHzFlGyaOhgIRkT-Aid7OaCGmvwoAanpgZnHSbLosnJqGNlBaHsGnLfPi0pvPLOwu3YfKhuOejkVA9Az5YkCxWSVh1RlNf8nfhhGOtbknXMPgaRv0ejl01T1oc8lu7CF2xijtHX1h_eeayNzpGuz3Ecjqr1pojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا:
محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25938" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25936">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1m-0nbOY7jMjzjOE5BRCn74kWMQihzG-UeaR41g7J9mxbTX39pY0eA58YBjdgrFbVo5Ykixla05-hx3p5jPJHkdLlA66g-kJUTLz8l4gcQbULAPTSLyqXpny4EdjQ-at-H-DL-X4k8gKHl6y3CyCvve-u34sziqdh3DSTY7XQD-0j2h5Am7q_w8AeaqMAvfz6GT8EA0KkcNF9l_tXYHQJrkjIFTqubuLonzf8kxmB_AfGaYOggLn1bSnNFofPbqPX8lvYDEA6RnEA2Re7KkUGpkR69u_r0vGT320QnFBtNPof3B0yUrgPoI19IFgwHqjK9WyMxWrsaLZDuAtFJiCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25936" target="_blank">📅 19:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25935">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPw2agyYR-qzC3Py1-rLf4FEYD8o5OqnfP9CD5osziMu9bifUDcLP9vFgFJj4l38ULEKLWbNurmpYocPGERFEvUg4_CeqOR3IP4vnBLt8PoQxcbibJsLTfAGybDrA1mh44VGJxhR7fy8XJaCq6PMA6TBX9p-c-Mo9pCIprDJOG3WyflhZSw_DmlYicnAC4fcCrKuPfX-NkgUhWNT9ixY7EhOWLPNBoy387l8ag-BXZ7_g9Fyrwhsq2W8vh8NFWy4M7vUCpRpiPkXEdHGvuimbgY34bcuJ_iHOqTxRWo6RqsyG6BHAo0Nsq93hUNJG51lXZZiDeHn0ugLQyV-NZPMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسلاوکو وینچیچ همون‌داوریه‌که امسال در بازی رئال - بایرن یه کارت زرد سخت‌ گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25935" target="_blank">📅 19:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25934">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utYDwzK5KSYv8Er5hxJJLffzU1JdH4RDDLRYerrVqxonZ-6C-i7WW1NHlf-eYPP2MT4F3XhAWPhOqLlFueD5Hy5JvsjmKKVcpoYzK3vBk06bqQLfl3G6JkiRR4mYQv3mZ-B5UFt5JKuvU7gZ61Mceme9n_-o_epVryAaLqqzFP7TwtzCr4l8Xs52wWAv9ZHBn2ed3zqxPPwBEADjPUcD9tNyuV_5JD9QVWk5_tTPw5J2p_eR1gBoHGrMGmXJVymj2BHd49OisyJfeUL4ga1mekRyVh7BghL14w9gYJXmBXC7Yno84OJhbYgs13fL-eJ2sm7ecuDmI2f6oHb_oYto0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
7نفر از11بازیکنی که درفینال‌ جام‌‌جهانی 2022 برای آرژانتین از ابتدا بازی کردند در دیدار نیمه‌نهایی جام جهانی با انگلیس هم در ترکیب حضور داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25934" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25933">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8_Bh-CiLqLVluryY-Tx1tfxGhRKCA1lGLV2mwk5E0RnZpJRtbjK6oOiNwWBmbkMllDQ5wLv2cgi_9koSTHa9mVh25Tk75BUyW5LjN_lAtieAkicO_nsXf9vsneIfRFMepeAhSBj5OrrQrjELGzPQTIwg1K-c0FEV1RepqV804g7NlwbCbES7bUkP96g-MNCHw40LL5JgKkq3Cf5ztoIfkc1iGK6YFt0t4PDtR2ikjDmsmEXQMaGfI1CZ6C62XatEhqFqVk-Dj4hJFGKcMzK2RLhqRaV_MY37WFaubTtQyDQwJe5l3quafVLAYI7j5LuaMeHrGjo_M4rJExFT-9FqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25933" target="_blank">📅 19:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25932">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">📹
اسحاق نیوتن درسال ۱۶۷۶
: «اگر توانسته‌ام دور ترها را ببینم، به این‌دلیل بوده که بر شانه‌های غول‌ها ایستاده‌ام.» اگر مسی هم دورتر از همه رو دید، یکی ازغول‌هایی که بر شانه‌هایش ایستاد، رونالدینیو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25932" target="_blank">📅 15:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25931">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=nuhvnHOhw18_GOE25_i-dX6JQDbbkQZ-SgFPvcWMfcTlSpV85w4wISeau-5v2MIpZkPx8OOniXcGiP5p54SGpnZWGpRWZyJyMgQT_3l1j05IhR7o3o2M6FevSs6pftP0AaIdkzhLsnMGWaa-OAM3SNTvXmTjCGYnqRX3D-u1XYWVQnuDfR2cyPZuHtHMF_LiCpDr65iFZguMiYK0GWsHvg_sqUY0ZW8saiPq2cqmJ9POQ9oBYhOB3DFLidXPWQZCjmeLHIX8AanZDKXp2z1MHzWP7hGY59rlXxv2toqbxWIiZ0ypHgdwdQ90gYVd-R6Qw27erqHCVWnCpWJzcOWZSF8uVgme_gdIm5FJ7Vkyv3ru4lV04r90ifgk8HqytHnDjTj-YWtnIyginXj1eYZ7J9JssHSyv2AnxpeYOzeattC1wKhyFI0EYneugz_4E8gypVWbpG5ILmvzX4i8t_H4jYXxL_TB4mRgIwuLlSdNiJ-9MhhoG0Shl59jpfYsu5rjvfDxSEgAqpxbFYqaaS5JQYHtv-m1aEZ6aVfH-ZUHk7caKnBX7J-71KsP6PyIeiUlkc8sZbJfDZu832fKO398I4pKgJi1Ser1yrtzRhx1Vhi5wt91jYIqaaC_Xviww5HJpeOW_1yVpTlSGzAtsVS0_wj32lrSceBL5dtejkjQaJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=nuhvnHOhw18_GOE25_i-dX6JQDbbkQZ-SgFPvcWMfcTlSpV85w4wISeau-5v2MIpZkPx8OOniXcGiP5p54SGpnZWGpRWZyJyMgQT_3l1j05IhR7o3o2M6FevSs6pftP0AaIdkzhLsnMGWaa-OAM3SNTvXmTjCGYnqRX3D-u1XYWVQnuDfR2cyPZuHtHMF_LiCpDr65iFZguMiYK0GWsHvg_sqUY0ZW8saiPq2cqmJ9POQ9oBYhOB3DFLidXPWQZCjmeLHIX8AanZDKXp2z1MHzWP7hGY59rlXxv2toqbxWIiZ0ypHgdwdQ90gYVd-R6Qw27erqHCVWnCpWJzcOWZSF8uVgme_gdIm5FJ7Vkyv3ru4lV04r90ifgk8HqytHnDjTj-YWtnIyginXj1eYZ7J9JssHSyv2AnxpeYOzeattC1wKhyFI0EYneugz_4E8gypVWbpG5ILmvzX4i8t_H4jYXxL_TB4mRgIwuLlSdNiJ-9MhhoG0Shl59jpfYsu5rjvfDxSEgAqpxbFYqaaS5JQYHtv-m1aEZ6aVfH-ZUHk7caKnBX7J-71KsP6PyIeiUlkc8sZbJfDZu832fKO398I4pKgJi1Ser1yrtzRhx1Vhi5wt91jYIqaaC_Xviww5HJpeOW_1yVpTlSGzAtsVS0_wj32lrSceBL5dtejkjQaJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25931" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25930">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOfWRoKT-RTGGldIOjUXNlCcFHB1gqmCcXwCRBU3ssYSTCYxQWITf-T1pv-2nlV4FcCVA5qudu-lNLJW9ziyY97LClh2xM59DIPo7z1BjnbLPGf1MVf6zQqVw0e5rhFTZe7YuTp_4z49svd2OvU4RpODe09ugvdatS3PVUItk8VtMiilcwnuXuc86KWmfcutCIToK9CezzNg-Uv5jqfMzo5HpFBZcwLjtw5kxep5IiUs-LWyPWlP5jOEbsqqDkEOAfm9gLVDT0GnmYgxFrPTPAImTmreAiJIokeTMiBJ8Z1mYvieAiZhB7svy0l-qlhBn5fzuTG2MgfoJoZep05QxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25930" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25929">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abJxS4IueO-qis-fBdIGfvMyn1LcT7Dy6mHa-3XDCOgP8vgwa7esCcshJ-6Iskg4rAnGGGRtuD3ZfJpNm310fXwPjqLTFTv1BvBy4B1VUNtpClSIffZ3rsPGErz6cVhB4C2oubF33t1BoFAfAum3xngpZK9j1AUiaWBehfHWjfBNSpEpdn-SOQ-Ap0NRF8I8KnfWnJX4Vh6jXABn2I0zwVoeFBIX1n7VffI_dwmava4iDwUdwEj14uL0tlpGHFxUTUsEgEo8lz9Xu2eqJHtWqVtHgb8PTU8blFAj9f65jF0lbkvlxuY9h1ULtYRLcx5kx1uxYHYupgIP69_2n0re_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
نشریه‌اسپورت: بعد از جام جهانی؛ بارسلونا مبلغی بین 120تا150 میلیون‌یورو به سران اتلتیکو مادرید پرداخت میکنه و آلوارز بعد از کش و قوس‌ های فراوان به جمع شاگردان فلیک اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25929" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25928">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3dEUG_S0LksH-WRriCVpc2DOoxMP_qH5O59paWg-53HfZlvGHlFbzDGcH_eyuRy9dDUEXrpcPFF0s5D2Ti5r-8ozI9MqFbwp5o-DoB9eTjj_kCodOy9aP5baCg_SGbuCMt0BknJwmZFsM4lRyIYf7t9AZx2V3Uw820wkomdJ3aC_K654r5KxhDS4bskY3EAPdu_85oLmTp1O4JJ97pZ6twBRhoBfFlOcDH7M-xA6HcnGLNoq-8mX1dIMs1oun2_6tcS0KU3eCPhNaiwhjWdDeLRWfUwrjIPwJ2tobMziVGDycqBof4PFFDqWy5NYTj8kLNamBxE0qetYYiXxTiHSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25928" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25927">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iieS01NDxqqrgwXxGKxbrFBGFKfmIAH8msz5sgnvrq6Xna5bw9wGHX6xZE_AbJ2CvRjVplRFu4wjPxZ8HB2ufsN4-lKBAuaRoLP5zaxJGJIcnhFL-t1CkHTPySbl3qFvyl5vQkRkr03kUdgyMm0jFX51vllXoWoa4GAO-rryNu_N0xz6O_sCtkmxeZB6rrP81WcUSc1KE6ykECFvvI3oxVWlGaaEkuLfJEMCGwWIim6EiPJOjiAMd5l5g6KWksouqpUsgKpaBLsSt7CTt5CFl-lnUhHDiCbinQL8RIxdbWYyzyCI6Ftzumc_G3O71JEl5RNwn3IM5A07B4Rs_K7UrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💰
ثروتمندترین کشورهای جهان درسال ۲۰۲۶
؛ این‌گزارش‌بابررسی بیش‌از ۵۰ کشور، میزان رفاه کلی را بر اساس معیارهایی مانند قدرت اقتصادی، برابری درآمدی و کیفیت زندگی ارزیابی کرده. منبع: فهرست ثروتمندترین کشورای‌جهان شاخص‌رفاه HelloSafe
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25927" target="_blank">📅 13:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25926">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_drG8s3R4cknZPTv1SymrQehG9UEoVDU4n7FfsRLYXJTCIOG_c7fiUeR1SQRQuXukEtY_Elk801YFTZg6NORVb1vNutX7upvbJ--1_oaxhg59hBgRnS6FnhvUKDKDFlRNFkJ43OLQKCw4vFhK-K6PoyeSPyXa3UnhCFOgdYnbsPZij9imQ_-_NoaoUnLitXQjh9aHv-UCTipYaekqD91ektAQtB_URRj8ZFdeEhHMklVMgcd1VNH_zxuVMQYuINvzObBVMKpWbNgSwMX_lQCBFyvfOz2g6V5ZwwEZfmItZTaqBa_h2-YQj7W3J9SY720J54FDmVNfa_tGpDvRLMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
شرط اصلی ورود به تیم ملی اسپانیا: عکس یادگاری با لیونل مسی تو بچگی؛ لئو مسی هرکیو تو بچگی مالیده الان اومدن قهرمانی رو ازش بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25926" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25925">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3N1ZcF8VtpeuR_KDQJ3S0KAK8Af7DhuLm9lk6G6H-p3TSLaM29QJriNAONpLd281UbTPGoDXKnu3b-JLmnuI3m-pKVUdI2BXFBWyjeS4cHkgDgjYpTv3T70ZDetCYmHh1icpdzkubWSHiWqqSn_SMkc3yhKb9LWZlB1cmI3lAs_1l9s48TksEp5S0HSMa2vlmQl6eKdYqZWpzvndmVFEVvb74elMsuhooSeyPF_IAvZhphYot74ZLd07sFVPbgpIxb-ZEzXymGaykBqbSFBJ20YznAjqBMO9OMeX9ywLcVaMHVxXwr8SPcXrP8-W24IvS8GLbbIGQNBwTpOA5-KOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
تیم‌ملی‌والیبال نشسته ایران با شکست سه بر یک بوسنی، برای نهمین بار با افتخار قهرمان جهان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25925" target="_blank">📅 13:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25924">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVq3GPad9W0LqU3BsZxd3DyWftdzF85JT06qutDkp0v208xHwCpPZdVXik_sfTi5wFTMvuI30c_1pobGb2LhHY6289DYWmR5xxj7drmbqZj4fDLVWcBEYaHx2uEKqJQnBUx-OUurQJ_3X9XHcc-ALrTHSvP1H-gXXfromij-j_BxqkdaoojgaiP2Q69LajavNNL9Jt5nGFyYlU9EzHBRItgOfzyoUHAMXW8Yiea-wzmwb9H5Bo6EntkrLjAMPlhTE-OBj9AGxJUL6e3fHyz0z_jqTvYZ-ij64fi23LiXQlw-qOLQiyfZBPsw8rqitrFollZ4sAGg6pt7rFJfZaGorQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇮🇷
#فوری؛جواد خیابانی: از نزدیکان رامین رضاییان شنیدم که این‌بازیکن باباشگاه لگانس اسپانیا به‌توافق نهایی رسیده و فصل آینده به لالیگا میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25924" target="_blank">📅 12:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25923">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=UHF6egqMAj0_LqWauDUXfqoBBukIssPp9CZhSgx1f59vqDdqkL6SaZhreVF9urHwGCWhSLlk2nxRjDfe7H9KBsreFMRWtWJRi6-F9jcaxBqPv4k9f99PAqURh7IDhu2UcWteEnSXTqnLE_btXQzic8aUOQPYDV0RFl9jLGiXHdQiejFnwoe_GQ1EzZlmmdyGpVHE-X79ObJHPQj-G2cWBTKMsCgpVnZtpyxYZUjqu_F2RooHH-cwZPrNJXg3WQiNwA2jpoz851mhHgsyf87zLcRrvR-RWKK62BFkMFu9y_kPLw6Fl2SEaLJEvqcqwXsO9WoJW7N7ygIFkNDT1ORf3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=UHF6egqMAj0_LqWauDUXfqoBBukIssPp9CZhSgx1f59vqDdqkL6SaZhreVF9urHwGCWhSLlk2nxRjDfe7H9KBsreFMRWtWJRi6-F9jcaxBqPv4k9f99PAqURh7IDhu2UcWteEnSXTqnLE_btXQzic8aUOQPYDV0RFl9jLGiXHdQiejFnwoe_GQ1EzZlmmdyGpVHE-X79ObJHPQj-G2cWBTKMsCgpVnZtpyxYZUjqu_F2RooHH-cwZPrNJXg3WQiNwA2jpoz851mhHgsyf87zLcRrvR-RWKK62BFkMFu9y_kPLw6Fl2SEaLJEvqcqwXsO9WoJW7N7ygIFkNDT1ORf3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آداب صحیح نشستن از زبان پدر تشریفات ایران درگفتگو اخیرش‌ باابوطالب‌حسینی؛ چجوری بشینیم روی صندلی که به کسی بی احترامی نشود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25923" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25922">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rId3cxFD0WufYy2ZjlG-Vx_joFd1wai8iESPC7vTq_x6v9S_qAwn5XDi8JDUA-UQq9pf_Gq2fSiZZxJSKHXcfL-LAXmaKI0NRMs5rYZJ4Gs3p-n7Mg6ph8z4sxmuxJopEr3c405FLG3IFMO0DlTeChKSwSdMirdx4VMgwS6XdI0Shb1VGwTo-klC8oxulBMcTDIosqzo7UWwuRUycrn74G5QfxZ3s88de2lxaBFXS_OtYooQMjlFTdAe-CI2I8dn667tXHtCoTgqahbOZ0f8SG9zj3eXnFGExzqxllpbZ-IsPbK4pdlu3Ni63nmrfK5Ydgc0uSu3RlEFJD-JVdFcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25922" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25921">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879626611d.mp4?token=E38R2qCkDMu67jdsHCimNpzww060zCyPwCzQOcXMBHr7NJK4Dt34_jIbgl3BRf6NirTcq1c0NN0Ag4hhxeQ1VS420JLKw6w2qCESx74BJln0UD_dXN3fkUUmOT2btIgTlLwPUXC-WgSDMddnA6_b_FuOrpAIZJKgfukgixlO9Rz02M4soAbOA5Yxr-bod4UDOpZL7oywVa51bLEBmQZOH3V-qTV9rS_nvnVFlrjMAADYgmj56-3B6Xv5DlrTMyjSrRNpM_qHU9UXR32FIiqq9tVF05hlBcURqlVEXJbKp3mlvKn2hqaF-tFdLrqdqdgyXr5zh8b_UmAUAIQ-10TbbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879626611d.mp4?token=E38R2qCkDMu67jdsHCimNpzww060zCyPwCzQOcXMBHr7NJK4Dt34_jIbgl3BRf6NirTcq1c0NN0Ag4hhxeQ1VS420JLKw6w2qCESx74BJln0UD_dXN3fkUUmOT2btIgTlLwPUXC-WgSDMddnA6_b_FuOrpAIZJKgfukgixlO9Rz02M4soAbOA5Yxr-bod4UDOpZL7oywVa51bLEBmQZOH3V-qTV9rS_nvnVFlrjMAADYgmj56-3B6Xv5DlrTMyjSrRNpM_qHU9UXR32FIiqq9tVF05hlBcURqlVEXJbKp3mlvKn2hqaF-tFdLrqdqdgyXr5zh8b_UmAUAIQ-10TbbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدئویی‌از پدر ایرانی‌ که داره برای پسر نابیناش بازی آرژانتین و انگلیس رو روی تخته تصویر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25921" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25920">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEtMzC7-qgVijWDuH5wtVE5tyQ6X2v2H5s8H6K0kFu0YV6JeQC53Dad3uwPwwFC4k4V8phIrYntql1U_rUr_149nr6q7SvG_tSWwlT43YvFG2OMejVaJ49Y3iNc8xPu2CD5t3G54knnKW9sleEYfZkYQIC5CcmO2-lCiP3nEaGuB4_lh2r2eq_6lmo2mRTSQsUbsFASbjyKMqvsbXPyoLz2Q_d582V9_tWx7ytifzDqni8sqNNNB-U8NxLXy0-boUGqOxs7FaH9a7VBjWbTnZDjbmXbyWZV14x2dMGOzaBOU4Bv0MCLxCcpqXebD08YJpjRbGIATJ26yw0w-zM4Eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25920" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25919">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
جلسه اول برنامه تمرینی حرفه ای در خانه برای ساختن یک‌بدن‌خوب؛ این تمرینات برای دوستانیه که بنا به هر دلایل دسترسی به باشگاه ندارند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/25919" target="_blank">📅 11:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25918">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WA7eNLeVzk14QQZ690IZNy0cL8A0QBYzh-cX6XCFLqMCypgZ3d2tw4Jo36Kyr09UqpbsytXzOM6OLK7cKcXiMdgsBH6OHNEbXiFRYoiSVU8y3Y9RfBQA0_EK99II8D0VzEzZige29OnlrwXGFDwklOz3doDKhCKkjM6b7MnMjvu_adscFBTIy6ma_GYNeZYcZEUAphDOsIq5rO8oIssbFtEf6vQwmvh16220xSSWbKZO2_ab9pwvf5p4ssa1dpDA0EghfJVAKFEMbTojp1skTEjpyw9aJC0_tD0nuomb7_nH3zH4HRiamJFlDuWSjjmqFqwgQAuLFTVOc0eYFEg1lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در۲۴ساعت‌اخیرسرچِ‌جمله «لغو عضویتِ جانفدا» بیش از ۵۰۰۰ درصدافزایش‌داشته‌و به سرچ اول گوگل تبدیل شده! چی شد اوزگل؟ ترسیدی خجسته؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/25918" target="_blank">📅 11:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25917">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeoPZN6E9sm44s0ivyh0N8254H4nH5vWkZyfYRrRyqUPeyd0z2MeDDq-ovppQ4l5mHx-2NShYnBO3X0q7mT-avphYmh_TyFZ9Cz1EK6jE1dfLIMlgiXJ4m8rhPEd5vpC8LeF_2j7vjPHlSbIpuYNwVEbSJyte4Hkgka9gaKl_-RdhfZGvtxky41HhEKf3Aekz4GtqDSdniT_65mBZ-6h4g94VzXpXuWIspplauQrS627yFYFg4L5BEvFmc3LUPlTVC8k5tvn1afBah2tn1gziagUvMTDQTXmF5qXKaF8Mut6qcMvFJhB6VPKpvbFNT8fPuSlgupuI3xOM4z4bXh_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25917" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25916">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFPARltoS812biFcm7CnkeIDdjq3YUITcNINdaKuZq_MWiK2kJsAR4SdCUiW3hOFa3jyy3vPdSccL9V9ShxLOojhMSF6YwyD1kKRkhDhjOKFRFxsR_x1xdE280jL7_9ZrTMEgrsa4dRy3i4cNtkSpLSwuLghxh0c2klT6CTwS8jmrQykSlKOeUX8KjRKnHcKd1jOCLRSkzytqmYyAHve5phV_Wcm4iUwqzSsA_jop088up5zK49F5DUu8FtbhdiMYqZmaCl-UzKH0N01osqZeUmO9vYILVG9_IUNFCK6EzqaCf8cyCR2DtkSh9qbo2JwPSmWd-XRd6vrdgkPYd-iQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
عملکرد خیره‌کننده لیونل مسی 39 ساله در هفت مسابقه‌جام‌جهانی2026؛ بجز یه بازی که نمره 7.7 گرفت بقیه بازی‌ها نمرشم بالای 8.0 بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25916" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25915">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcWLEafNjqyaLJ9jxJrKV6cDD9s-agRwixn9U4PZ0iEOjpwOoaTwFwKhDWM84npZOEkaC2eGMGynfXAAfAP1CO6evhTxXlRNKotgdBVnVxpI_pbLzlWKbTmQQMIJ_8lvqIrDI8_LyKWF0diMQaPF88rPKsnJAki_ktMxf-eVOR7rMBDtqc26G1ArGs3nA7yDvM2Z-_eVzT5B1PhUbjN9tHK3lsoBiOUZ_9IywhLiYudSPDlyvAylE-GKWfXj6lBEfl54ahLmR-0Ls5-fhXYE4ViSR3g6X4jRLADdie_Cf-vdOMZD1O6-3ZrBjj6_AcL1MIo-W7k1P8S6_DUPdKQyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25915" target="_blank">📅 10:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25914">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25924a633.mp4?token=PfKGewSeNVmhQ6KtuafSAy7i_ob_cCfG8edIr0BfUuJ4JZPa5ERDPlxuhDsCOT3SfVvmblet1JvKazlIZlqO3-tmjqPBTVRBSSEJ26us4SgQjYQQ3DzpAYJoKD_aUX_uA_1r4_cwbsmfLLLUOtohEYu8HA4teWyctG3GpYIVN6WrB-aXMkPV85ZAkIkBEZte4AYLYnFj1xMdue6Jd94S8m45iEacAARaR7hwgMC8kyTKThgU0BOTEeBuF5MegTy-vOQsThir5sJSTHWgPD4NKCiKl-Qc9nUGTNgB5qgqMHwz7N_QaySeh4CUMIUNE4bPEOUqCPym0nodIw76ZhkNFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25924a633.mp4?token=PfKGewSeNVmhQ6KtuafSAy7i_ob_cCfG8edIr0BfUuJ4JZPa5ERDPlxuhDsCOT3SfVvmblet1JvKazlIZlqO3-tmjqPBTVRBSSEJ26us4SgQjYQQ3DzpAYJoKD_aUX_uA_1r4_cwbsmfLLLUOtohEYu8HA4teWyctG3GpYIVN6WrB-aXMkPV85ZAkIkBEZte4AYLYnFj1xMdue6Jd94S8m45iEacAARaR7hwgMC8kyTKThgU0BOTEeBuF5MegTy-vOQsThir5sJSTHWgPD4NKCiKl-Qc9nUGTNgB5qgqMHwz7N_QaySeh4CUMIUNE4bPEOUqCPym0nodIw76ZhkNFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضا بیرانوند خودش‌دست‌به‌کار شد و به این شکل مجسمه ژنرال رو در تهران پایه گذاری کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25914" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25913">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=YdrMBDm6GRGG6QtA5GxPKcwdPdK7vSxwEExcj-HD6u8IBiyYdaeg3K_Wn-Q9dJBsXUvuni8clZu7UYGjVGCo1eAF4G-cLE2K769ppTK9waNneZ-w4Nh7qV20rzXIyhtd0YxQpzCxEqaBtouIfQxVWmxW7ISH29FZyalTXtikLLkjopdqzBEg8anrTrvM1b6LlDSlhtuDYCEFZ9l9m8mKoS41BY4-elx1Sslgv4nNJMkAvB0NgrsPtVNLwpGG7hIDmVgV_gq_gJKj3_kQvPe2LK24FJGSC6lQznenT0eZNPydt9TKYxVjPeAusFjCuoi6wk8USPZmjg1MnzvHyjd7wa1wY9HDwhBdcTiD2I51kLHUFwSX9-88fN2TgMIc9dYEcMXCCS64hZ7rL7RFEXwb7gOYpUHC072Wxws3zP2u-2JEwEZXXdMs6p2TqIrLHBjbY8D1pYI23q-p3-fy5N99Iyfydvrj5irVGHMXh3CmyODVegrlPA9tdghhkLGFKeTD7jf_QSFW1J4CNOzQ9U2dtpghhvYraKGBMUMY4C-lY7I7bGK40KeWwNqT-dmiRCuRi2Ugv3Q1QNIQc9hu0PC1cqolq5CGPgSBspRbvz5ZzsCAAthPMD12SjS1x3b4hoeEDz5K_EvVVTNNzAVLI3MFiQwb6jpcPpTGc7VJE_xdTKc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=YdrMBDm6GRGG6QtA5GxPKcwdPdK7vSxwEExcj-HD6u8IBiyYdaeg3K_Wn-Q9dJBsXUvuni8clZu7UYGjVGCo1eAF4G-cLE2K769ppTK9waNneZ-w4Nh7qV20rzXIyhtd0YxQpzCxEqaBtouIfQxVWmxW7ISH29FZyalTXtikLLkjopdqzBEg8anrTrvM1b6LlDSlhtuDYCEFZ9l9m8mKoS41BY4-elx1Sslgv4nNJMkAvB0NgrsPtVNLwpGG7hIDmVgV_gq_gJKj3_kQvPe2LK24FJGSC6lQznenT0eZNPydt9TKYxVjPeAusFjCuoi6wk8USPZmjg1MnzvHyjd7wa1wY9HDwhBdcTiD2I51kLHUFwSX9-88fN2TgMIc9dYEcMXCCS64hZ7rL7RFEXwb7gOYpUHC072Wxws3zP2u-2JEwEZXXdMs6p2TqIrLHBjbY8D1pYI23q-p3-fy5N99Iyfydvrj5irVGHMXh3CmyODVegrlPA9tdghhkLGFKeTD7jf_QSFW1J4CNOzQ9U2dtpghhvYraKGBMUMY4C-lY7I7bGK40KeWwNqT-dmiRCuRi2Ugv3Q1QNIQc9hu0PC1cqolq5CGPgSBspRbvz5ZzsCAAthPMD12SjS1x3b4hoeEDz5K_EvVVTNNzAVLI3MFiQwb6jpcPpTGc7VJE_xdTKc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تعداد گل و پاس گل‌های کریس رونالدو، لیونل مسی و نیمار جونیور در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25913" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25911">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkEiY1xG3Rs6BEqXOU02mVcmL_9kPYYlZrgPcXZ9yT721_Iz9GMtkwxDOrQjX6fGZYodTj2pPsjMuq4IHXS3gslALgKfUg5l9e8vi7UHcRFHS0ot1ud04vlN6OoITZZz7ZPeMVpmBPKnZLkhcZnR74pLf2E27fBgJ1t8kEVa_M6LjgvqKRxP-a_pa1eM33esR9o9mecOXCDv-L7yJibPgI550NfV8Ejp-PQqSEEzk5Txez6Rv1pyBV3GSCTynHq_qHhfSaJCTSs3Vx6-AhVJo5uSKGUb5ecx1GTajNFW25bbpuYhupyQO4GBOozz6bFukSLoVsR6yA9UBstGY1TfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25911" target="_blank">📅 10:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25910">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=DG1kluhycqFDlkpSr92fDv1pi_GqxUJJJoMHckt-uW-mfJBXpZbUl8QpZAvWtA1t43OlMjLd66VBePMCzW0udWA1voQp44ztXOT-XhN9bsfOx7j1G5gD0Hl3LIkRZ8khAAXjp7xgWUYkUec0cAZAcUxzDMyZgwaF_z_JHnOc-WEMUyqJ6M9QnW-j2hE8NEecLf2lyQAHO5sFuCSjRuTKABD-FiikAk2kohrj7weVbdPB7NPh__JIwB_YLqmL1MztNoVTQT4YbABGycvIg9jRb6K7hHBhNMnT01oQE77dV7POVQcu1A4QDZU5zSgddQSsTAN9-SN5kuMb00rMKjDy_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=DG1kluhycqFDlkpSr92fDv1pi_GqxUJJJoMHckt-uW-mfJBXpZbUl8QpZAvWtA1t43OlMjLd66VBePMCzW0udWA1voQp44ztXOT-XhN9bsfOx7j1G5gD0Hl3LIkRZ8khAAXjp7xgWUYkUec0cAZAcUxzDMyZgwaF_z_JHnOc-WEMUyqJ6M9QnW-j2hE8NEecLf2lyQAHO5sFuCSjRuTKABD-FiikAk2kohrj7weVbdPB7NPh__JIwB_YLqmL1MztNoVTQT4YbABGycvIg9jRb6K7hHBhNMnT01oQE77dV7POVQcu1A4QDZU5zSgddQSsTAN9-SN5kuMb00rMKjDy_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجریه به عمو رشید میگه از فوتبالیست میبودی و‌گل میزدی شادی‌بعدگلت به چه صورت بود؟ ببینید چه حرکتی زد. جمعش‌کردگفت منظورم قلب بوده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25910" target="_blank">📅 10:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25909">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=HdHMnYagCBJgb68_6xv7w-N7Q3C2czbqY9xZhDjJGj2wirxkYi-LaQWgRd3AFEbHnydjycUvIHKsTpfMuWNz7-XL9Tkpa6jA9Nj1AZwjis9GZC4GBHh_RD-x3CgaebLzTjY-ZuNBPJHGZIkWk6x5FBCGFjwrj1hMMg-63Y8HY8jv1FZ_erx9Fk6sqDIQJ9CEeBEu1TxtxZxxIRf3I9Gy0bjf_b53GYXQO8dxsllrgetfglayIYABWP1PGRlT54IAS9wrgOgQPq87WSkWM7RDkSzrvIH5KSj3dtXh3fx-Ve_r8sv2ZrS9cEgH92eZMf7Co-pDg5H7t3RC3k7Thhvqf4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=HdHMnYagCBJgb68_6xv7w-N7Q3C2czbqY9xZhDjJGj2wirxkYi-LaQWgRd3AFEbHnydjycUvIHKsTpfMuWNz7-XL9Tkpa6jA9Nj1AZwjis9GZC4GBHh_RD-x3CgaebLzTjY-ZuNBPJHGZIkWk6x5FBCGFjwrj1hMMg-63Y8HY8jv1FZ_erx9Fk6sqDIQJ9CEeBEu1TxtxZxxIRf3I9Gy0bjf_b53GYXQO8dxsllrgetfglayIYABWP1PGRlT54IAS9wrgOgQPq87WSkWM7RDkSzrvIH5KSj3dtXh3fx-Ve_r8sv2ZrS9cEgH92eZMf7Co-pDg5H7t3RC3k7Thhvqf4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25909" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25908">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=PIZRsr7d2ob_XrkaWRmlB_JzTYYgmYChPwasx__Wbp3ElrrOvLPVM_NqPOsBWoh0dK0sl6TJImFHhjV1n8koJaZAfoZZxL5X4A1ZTLPNvVQc0aJQJh0RGMmxma0Ts2RIRuxDebNv2QmQGM5FQyOXOboKxLwaOYc80q2ZaDomVzX0bzSEyDvnZXeg21MY4OXCAyOQKi1XXWIZbc3vmr9tQ39rSH_Cj443s2Lw6vDPgVMxWosGmAUECQDu9p8oz9supZ-s0OR1_fCcvxo8ZRX4MlLAxZMig3ORSfDD-iMs8GTWEO3xAG-msrT1QDsV6488-WMh9w15XcjnCS6LPE9StLgqrHQg3QbsbuebMDx6bCc4UQWf4IMnJhocXAU0uRtApdvy87XrAiQONqf1fEMp5jBWbd4eXrtATn5TS0D4JL3nDqqksLjCgwu9WzvRlAUbzeoVm1F_xbaCisivtJgEAte2H2uvgvl8K1WmOojLrkqb9veBIDEfK0gIs253CTYEm_DxD8_bvXSIco02XnFVA3G8eFOf1AzZs_AGl0DufU6tkaVUmDRv50SsdeBYZkRIzidrLnPRExEamG4-7juPnF5puDviiZ6Pn3mKWryOAeCqcx6sgBiafMkgwno65lQydeC2gKGwrYbHpDEIBDCAcBJtusubX1I8h-H_6gCBvJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=PIZRsr7d2ob_XrkaWRmlB_JzTYYgmYChPwasx__Wbp3ElrrOvLPVM_NqPOsBWoh0dK0sl6TJImFHhjV1n8koJaZAfoZZxL5X4A1ZTLPNvVQc0aJQJh0RGMmxma0Ts2RIRuxDebNv2QmQGM5FQyOXOboKxLwaOYc80q2ZaDomVzX0bzSEyDvnZXeg21MY4OXCAyOQKi1XXWIZbc3vmr9tQ39rSH_Cj443s2Lw6vDPgVMxWosGmAUECQDu9p8oz9supZ-s0OR1_fCcvxo8ZRX4MlLAxZMig3ORSfDD-iMs8GTWEO3xAG-msrT1QDsV6488-WMh9w15XcjnCS6LPE9StLgqrHQg3QbsbuebMDx6bCc4UQWf4IMnJhocXAU0uRtApdvy87XrAiQONqf1fEMp5jBWbd4eXrtATn5TS0D4JL3nDqqksLjCgwu9WzvRlAUbzeoVm1F_xbaCisivtJgEAte2H2uvgvl8K1WmOojLrkqb9veBIDEfK0gIs253CTYEm_DxD8_bvXSIco02XnFVA3G8eFOf1AzZs_AGl0DufU6tkaVUmDRv50SsdeBYZkRIzidrLnPRExEamG4-7juPnF5puDviiZ6Pn3mKWryOAeCqcx6sgBiafMkgwno65lQydeC2gKGwrYbHpDEIBDCAcBJtusubX1I8h-H_6gCBvJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25908" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
