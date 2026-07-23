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
<img src="https://cdn4.telesco.pe/file/AKt9Hvo8xGK6wy-8PY0z4DYAr7AuOietYKPee0Aq3adwUfx2SvnK_Ga9pn94wE2I-iNvAXWnKNIcWXrTiwHUafeRSbt8e11Xtf7AMOdULoKGLXMmu7IPTHyBwCkNvYDHB8T0ttuUGxOrGvCxHR9B_Uptim6a_DUSvZjz9sL0VDm5QbznyvdXpFc2MLslpamI2t1X6BzZiVS1t9FJuuJBZ3DrGGggDQziwf4uyLosCLZefObMC7x1NA2dtFUM6r8BJ6ishbBX1mFw0mHDA0wwU-5Ziy3Stvh-y1D0_DrwsCjRm_yvfq633S_dF91Utyd4gBUck2fqxZn4I-v8LiWB3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 152K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 15:38:44</div>
<hr>

<div class="tg-post" id="msg-68852">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n08hvWNXbQH5YYz8XqV0iaLbryDnWUYm9ir1-OyrGUSUMevIWHd8o86fSiHOAAGNisaSsQ1bfxZxNqkiRIcvPbdw5N2Pw-3Yr8N-XmnVg62n7YBvNxzRkHE3Ql-errUwuSZdebZWuYNkz03hRL7O6Njfmkwdu1jITs8uvecoFIg8rQ2veSWqnVlJR8spnuHedcnHIvhXmC0x64H50jaCvN9jLwXSPq-VpM05fZLTWrxsc6MZt3WzXyHg97GRlGsaIqNZakj-s5wF5bCKGfTw0-yVtZyTGq-atRzn4P-1r4WbamfVPGht_vDRrbK7zoj5YSNO3PXDXl3R5AAqseHofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توافق هسته‌ای غیرنظامی (که شامل هیچ‌گونه غنی‌سازی مواد نخواهد بود!) میان وزارت انرژی ایالات متحده و عربستان سعودی — که صرفاً به مصارف غیرنظامی، مشابه آنچه ایران و امارات (و دیگران) در اختیار دارند، مربوط می‌شود — تصویب خواهد شد؛
اما این امر کاملاً مشروط به پیوستن عربستان سعودی به «پیمان‌های ابراهیم» است که بسیار محترم و موفق هستند.
ایالات متحده با تأسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) مخالف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/news_hut/68852" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68851">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=PsqgkhKq0Opxnc_VRTrIb4U_H6uOXKt5icyj2XBCx-fcQ2PzUAIc0pT_YK2VfWAIV4EILY0G25I9yo5B7Pd1EKO1Kan15tKvBvNy44GJD7XBIAAdYlTGmk61bBg1lQQeK83FVnD3eE-iHm7hMMdnyOkj5fLYORrY2srQejfM_OeAn8UUvwGZC1CImOU59ua46rznuK0Ih46QkSRE5lQHKB-DDzAg0pIjpfzxLpik9oU1tqqAReBiZxMaL5LMf3zwX8Ql3UvJuPq3ddmIQrKZw6IZ9kejZTVNHcC_m-dc4DTOQks2-RXBrCq5Dr3AIDA4BSk1Cr83--Fk85NUv8TaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=PsqgkhKq0Opxnc_VRTrIb4U_H6uOXKt5icyj2XBCx-fcQ2PzUAIc0pT_YK2VfWAIV4EILY0G25I9yo5B7Pd1EKO1Kan15tKvBvNy44GJD7XBIAAdYlTGmk61bBg1lQQeK83FVnD3eE-iHm7hMMdnyOkj5fLYORrY2srQejfM_OeAn8UUvwGZC1CImOU59ua46rznuK0Ih46QkSRE5lQHKB-DDzAg0pIjpfzxLpik9oU1tqqAReBiZxMaL5LMf3zwX8Ql3UvJuPq3ddmIQrKZw6IZ9kejZTVNHcC_m-dc4DTOQks2-RXBrCq5Dr3AIDA4BSk1Cr83--Fk85NUv8TaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو فروند هواپیمای «EA-37B Compass Call» صبح امروز وارد پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) شدند.
این هواپیماها که بر پایه بدنه «گلف‌استریم G550» ساخته شده‌اند، جدیدترین هواپیماهای جنگ الکترونیک نیروی هوایی ایالات متحده محسوب می‌شوند و مأموریت اصلی آن‌ها مختل کردن شبکه‌ها، رادارها و سامانه‌های فرماندهی و کنترل دشمن است.
در حال حاضر تنها
پنج فروند
از این هواپیماها در خدمت عملیاتی قرار دارند و قیمت هر یک از آن‌ها بیش از ۳۰۰ میلیون دلار است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/news_hut/68851" target="_blank">📅 15:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68849">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlJZWBiESMbE_vFnWeXPCkymoNJgXHUvaLC-fJP_KPKztuzskIgaDCna3qBars49gShT0tV5NKewT3RTJvJqkDGdAhFnNLfqjqjCpjVbxSinAkfaFxq_xkmDbxQao1cHYYFnIJ5rHd12yZsjiEaCxz58qgS-WcD-S-OWLh4TLjDY7E68s0MUrO2c1cjotrNQ5-jXoBQzZ7zFgO1T8xeR-rL_LbrGkrG6Z7Vonq6mw7fSWVEo9bn1EEVCvfvzYaFFw-vUJ96SDiaj_McbHMcWi7kvayKP4jm865ITse4YWCPgjkf56indwhYOQXNnj4Bty48_-Er_O-aUZCyl7t03WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=HZlWrPiePeA1o5hmlCakb-fif45Yz50l8xzO81VMv5p0MuVePoMwwlwcQfXLzEl4NLNcVPeA3YP33DBhsRjtmWKwhRUCoV_wlizfnBhfiesS4_ufZAom9E2Bi_Eprq9k_FCFfyFmrJvvTGdnRu3vWDbem2Y2RbaA_jrYgXAsMclAgmsJYK3soa_GbvYdhJi0q03RdOUUkgaen5U5fMWaemfLsgkNstx8fyzUC7zg7QtOXlTLfY_NiRQpiAurFfGr7qV_DaBrsPezvfEueCsYtT8pvQPSfEz5wrWWMHyJU2yeea40IWxhlwC4i5W7qt0oLYvBgyj2q9GO5RZfzJkySVaN5sbB5f75WiHaJKgbnHIHEnA_ha54xd4GtPixCwhGB9olHzuH4wDYgZtLdhYP5h8UPrWp4KnbYxLZ9YXHSfg38CoZDdIJbHLUwKPOertt9MVRjVWu16lx1OwLVbzbwnmn4KMrjljR5ledlA8oOe_EiLE-oVuyRdxfiwrwU0wxKhuf07mgnPejv4m4RqQyCyNV2QAfKSu7VGO_3FCWbSoMTQNGHlWz2CgblYap-ctS0Sp1HckXrYKxw5z4DWk17jYGUz7c9Ou5Q4DZqU80bls_LJn7haiMjh86UCqJmwhF_-gwYsNwX-iuES4RCvOSJqG5hGEqvLo584bI3yyCwUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=HZlWrPiePeA1o5hmlCakb-fif45Yz50l8xzO81VMv5p0MuVePoMwwlwcQfXLzEl4NLNcVPeA3YP33DBhsRjtmWKwhRUCoV_wlizfnBhfiesS4_ufZAom9E2Bi_Eprq9k_FCFfyFmrJvvTGdnRu3vWDbem2Y2RbaA_jrYgXAsMclAgmsJYK3soa_GbvYdhJi0q03RdOUUkgaen5U5fMWaemfLsgkNstx8fyzUC7zg7QtOXlTLfY_NiRQpiAurFfGr7qV_DaBrsPezvfEueCsYtT8pvQPSfEz5wrWWMHyJU2yeea40IWxhlwC4i5W7qt0oLYvBgyj2q9GO5RZfzJkySVaN5sbB5f75WiHaJKgbnHIHEnA_ha54xd4GtPixCwhGB9olHzuH4wDYgZtLdhYP5h8UPrWp4KnbYxLZ9YXHSfg38CoZDdIJbHLUwKPOertt9MVRjVWu16lx1OwLVbzbwnmn4KMrjljR5ledlA8oOe_EiLE-oVuyRdxfiwrwU0wxKhuf07mgnPejv4m4RqQyCyNV2QAfKSu7VGO_3FCWbSoMTQNGHlWz2CgblYap-ctS0Sp1HckXrYKxw5z4DWk17jYGUz7c9Ou5Q4DZqU80bls_LJn7haiMjh86UCqJmwhF_-gwYsNwX-iuES4RCvOSJqG5hGEqvLo584bI3yyCwUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقوع انفجارها در گذرگاه مرزی «عبدلی» میان عراق و کویت، در سمتِ بصره (عراق)
@News_Hut</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/news_hut/68849" target="_blank">📅 14:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68848">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUP5Bp8xcogTptLlrXlfoCYDkVAbYUFJxju5j1cp5gPUSD6URgNT4MmtBT4dl7h-TrL3bJvMIoIbhSnFzC73PNLLfIk9rxSsBCkchgZAF-CAFaa7EM9ikQ-Hjvf4N4QXCm3W_JgiphWNAPBXbMvzjCISi02RePrOK7gjzvVIlfcoCO95y1nAUFgcAJNMKcBg_uqcliCG2v7iKD0MfyXgfwW_vHKFKRZs73aj6y0u-DOR6Wjy1OhCQjwIomPDxzf8Lwsx_DIr_xMGwIaL2V3nHVOB2A-FYjeyI8Yzc3t3G4tugx1EXFpqs-N87dOMPAWaq0rCvggLuTdV5Sa4aEDqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابوالفضل ابوترابی، نماینده مجلس:
دولت مسعود پزشکیان با ارسال ۲۸ نامه به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، برای مذاکره اصرار کرده و او را «تهدید» کرده است.
قالیباف و پزشکیان در «تله مذاکره» افتادند و «باید به عقل هر کسی که الان حرف از مذاکره می‌زند، شک کرد.»
اگر جمهوری اسلامی «دو هفته دیگر جنگ را تحمل می‌کرد»، آمریکا و دونالد ترامپ، رییس‌جمهوری آمریکا، پیش از آغاز مذاکرات «همه خواسته‌های» جمهوری اسلامی را می‌پذیرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/68848" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68847">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=jVXC7mjqIfu0h8Au4swnQ55mWwRVtCZ5Bbgca7zmCt47gQzamjyYLWdF1QyNHlRKY-pzTv5KjwVvkgEaHELUgweYEoQwmsxfebLo4dVidQB7rpACYaOGqYPdZ_gGi2e_opPQKPV4K6BYht1rNxExqTfVOCmtMN8su6OGvtD-UXuPbK7g15btpQMosCuCddwxyYv9Dqpa8y2zXNlD62bH1fxXYfFjLxAT6OPX9azFWXc2qLo9Jbclzp6kfO5aeSMFIsmQEqjScDm4b71S2iQKCNXtdfpqJxF6Tytx1M_yYWtGpI0huqJqyYPKq5mFA9qj33XCi8GWaSygI6aWrn_scA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=jVXC7mjqIfu0h8Au4swnQ55mWwRVtCZ5Bbgca7zmCt47gQzamjyYLWdF1QyNHlRKY-pzTv5KjwVvkgEaHELUgweYEoQwmsxfebLo4dVidQB7rpACYaOGqYPdZ_gGi2e_opPQKPV4K6BYht1rNxExqTfVOCmtMN8su6OGvtD-UXuPbK7g15btpQMosCuCddwxyYv9Dqpa8y2zXNlD62bH1fxXYfFjLxAT6OPX9azFWXc2qLo9Jbclzp6kfO5aeSMFIsmQEqjScDm4b71S2iQKCNXtdfpqJxF6Tytx1M_yYWtGpI0huqJqyYPKq5mFA9qj33XCi8GWaSygI6aWrn_scA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه حمله آمریکا به حوالی بهبهان
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/68847" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68846">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc1jr4YIYsZI4REzId3J4WjZsQbpYewBA1q3I8FMvcGtsUic05GTnoTd-35R34IaC-yW2EBZYQGCDYOc6JVqrH7xaRngohTVXzLoxHmkjvLuliBBLwfVY0CaopdbGnsb3N1u_9kBjbKyqMVnESrdb9wVi8tc4mW_1BTRwZUE9ipuv-cGFSyq49yzPm_7z6P8jIA3qCwE0S-0NuwvDhqUYo0XiAaX6I8s8vyDg-ZTo44b4D2lVQoN5Z8U4toYPjMayg9b4CO_2Uygs9F3U8UZbs6WpsgZoWcq7i_nqzu9L1Tmgml1puGlwHsrSM8HYCJAX2PAOAI_dohDy1Yd4Is7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/68846" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68845">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇱
شهردار «رامات گان» در اسرائیل:
«ما تصمیم گرفته‌ایم تمام پناهگاه‌های شهر را باز کنیم. ارزیابی وضعیت نشان می‌دهد که خطر حملات موشکی از سوی ایران در تعطیلات آخر هفته افزایش یافته و دیگر ناچیز نیست؛
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/68845" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68844">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=EIDnlQmKwk1xPO5sMStcXWKdiI2ieroIWEAL01veQD6JmEjnmtT1HzqQVqbiiCPy2gf_1KIA2ywQwPKFJa9pUlLUjkF-EnBLXiyPfnmYYF3_ZZe2da-4vRjzDCZY5naF9PMFoCC_uAbqG53sb56jQCV-n4X0zHtPlhE8zH1-ctlOHOij6ShKPDHdLB3E6mBalME5c5MNzt3ss0O9__WqXpDxcqt4SSjZQ5OWGJQn4iJz7j5RZk9L_e1ibz5Mk_wVCTkk74OBpa86_BaitEmHPIAp5yhxTaV91iK-e65HxcWUNHyhaCOyNQc2vtzHx5XokOjeZjF946uqUxBVA0fj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=EIDnlQmKwk1xPO5sMStcXWKdiI2ieroIWEAL01veQD6JmEjnmtT1HzqQVqbiiCPy2gf_1KIA2ywQwPKFJa9pUlLUjkF-EnBLXiyPfnmYYF3_ZZe2da-4vRjzDCZY5naF9PMFoCC_uAbqG53sb56jQCV-n4X0zHtPlhE8zH1-ctlOHOij6ShKPDHdLB3E6mBalME5c5MNzt3ss0O9__WqXpDxcqt4SSjZQ5OWGJQn4iJz7j5RZk9L_e1ibz5Mk_wVCTkk74OBpa86_BaitEmHPIAp5yhxTaV91iK-e65HxcWUNHyhaCOyNQc2vtzHx5XokOjeZjF946uqUxBVA0fj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
عراقچی می‌گوید سیاست آن‌ها "چشم در برابر چشم" است.
سیاست ترامپ "سر در برابر چشم" است.
آن‌ها بهای بسیار سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/68844" target="_blank">📅 12:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68843">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzaQu3zoy15SukZGy8R50deJP7Jg7X6b2ZXL0NJNg4G12WRzdFrNch1cbzKKDTs7CTKtaE93cqtczEa39t6JzwsuM7oumJ7wJsdlzGq6U3A8bW6DZhTQdeyfOXfoggIJ6AKWPjofhvv1JfsmQ2i4umGQL8ny3uUzjxn_gdAp3xxvSN-95GndkwQbl3ZmZR3EVj0liyl2KTSLK3RF9_6-HpTpFRhzVHCjcLf4AreT9T6ZgG6J3279XHVudeZ0In5POMcqBvEwUELDW39Qk3i54T6lECYIquv8fE36cN8NVVmyY3a7AXZ-1-1rJry6GtOy_JSt02jq6W5wxVdnM9RCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پایگاه دریایی ارتش جاسک که صبح امروز مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/68843" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68842">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=pj9Fh6QgpeaziedWtui6weQorZEYwvTfx49Gdu3WM7i_6o9Ks3eOPdEs0iS8m-ZlQjbAokWVDdrR8paaz-tq6_ku17Fs_4WEf2gq9fCmhmy226V-pHGqZ94jrEp6Q2XZJPPKbh82u2t13WBj3x2zqOWUnC5wx-UEZaJASWg9QpzXfIqCisAz1AwclfzszTUAaNOgNImnf9c9p69gfyRY1PmKs83bZVQoCxqhORFsoOba1lrcLZgqS3HCOVM_v_Y5CqPWMKkF7Qeq61HqRdbtQcXqeKSgIzwpEuU5UaEL7YLHGTxhDocrKr9xoyoyXITsHaWeeIiNOUNEy44aETBk8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=pj9Fh6QgpeaziedWtui6weQorZEYwvTfx49Gdu3WM7i_6o9Ks3eOPdEs0iS8m-ZlQjbAokWVDdrR8paaz-tq6_ku17Fs_4WEf2gq9fCmhmy226V-pHGqZ94jrEp6Q2XZJPPKbh82u2t13WBj3x2zqOWUnC5wx-UEZaJASWg9QpzXfIqCisAz1AwclfzszTUAaNOgNImnf9c9p69gfyRY1PmKs83bZVQoCxqhORFsoOba1lrcLZgqS3HCOVM_v_Y5CqPWMKkF7Qeq61HqRdbtQcXqeKSgIzwpEuU5UaEL7YLHGTxhDocrKr9xoyoyXITsHaWeeIiNOUNEy44aETBk8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای ناموسی در پخش زنده
😃
⏺
امیرحسین ثابتی:
نباید تنگه رو از دست بدیم، نباید تنگه رو بدیم بره. شما می‌ گید تنگه رو باز کنیم، مفت بدیم بره.
⏺
شهریاری، عضو کمیسیون امنیت ملی مجلس وسط پخش زنده :
بدید برررره، تنگه مال ننت بوده که بدید بره؟
مال عمه‌تونه؟ مال کیه؟ ارث باباته؟
⏺
امیرحسین ثابتی :
آقای شهریاری ادب داشته باش چرا وارد بحث ناموسی میشی تو پخش زنده...
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68842" target="_blank">📅 11:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68841">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=VMxV5jTxRrnnd0xWJu6hYhn29pfLwhfu2Sabv3RkJbPYgNJ2bkiCJGV0H5HBR4oLzzHhI9F-IoXO9NISMwGzcIHHEF1j9HXQCeQLygq9vne52-KXMRrRsf-H80GkHNMjywIIRPhXHNrBet59MNzvNGEPqOctACgXTlxmQcv-5IEft1Plzq79XgQJLvV11NjJ_CtkVSkQLMUwc-4QgStR3kgpB_wtRZC-jXCsTiuwYWRzWmfexQej9CXFHe3DPQF7nP39TwLq0MRNX06GtS8CwIkLKb7Dyx3U4EEObm3-HseaITt8VtkIrulrE524xCUuQeH727xXo-jHsaay1cvgjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=VMxV5jTxRrnnd0xWJu6hYhn29pfLwhfu2Sabv3RkJbPYgNJ2bkiCJGV0H5HBR4oLzzHhI9F-IoXO9NISMwGzcIHHEF1j9HXQCeQLygq9vne52-KXMRrRsf-H80GkHNMjywIIRPhXHNrBet59MNzvNGEPqOctACgXTlxmQcv-5IEft1Plzq79XgQJLvV11NjJ_CtkVSkQLMUwc-4QgStR3kgpB_wtRZC-jXCsTiuwYWRzWmfexQej9CXFHe3DPQF7nP39TwLq0MRNX06GtS8CwIkLKb7Dyx3U4EEObm3-HseaITt8VtkIrulrE524xCUuQeH727xXo-jHsaay1cvgjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دعوا بالا گرفته بین قالیباف و افراد افراطی!
🟡
الله کرم رئیس گروه فشار:
بهتون اصلا اجازه نمیدیم به هیچ وجه اورانیوم بدید بره.
🇮🇷
مشاور قالیباف:
به عنوان کی داری اینو میگی؟ نماینده مردمی؟ اندازه حزبت حرفت بزن زیادی نگو.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68841" target="_blank">📅 10:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68839">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=oujL-tBepBqIoJ2fAJHSRXc2m_rcilLaFUuIslYEoAK6LtdVMDcu5vdEbWejJSUEYCV6XZtp5g-CqUTWmB6M25ysDQw7kbi7LFtDpqU5eJMh8Ya7OdXVddy-xcCpfDgJZwJBLd9Vj1QtN4a8DE3eaQQpQELJm5jzLevhtyqDmtc6btu37dpu6BBZAzyK_umjlVRtSLFh11BPWTUbQ3_Qg6VRmZ9uphigVz0k4HKd4HW84M0LrJp5wWaQEF-4NBzJbvQvhRwIWafDtbOeCCvyHmJ5ImILvQGu_mydviscvKwsPlYjac664U8GMJgeAOGyLyW3CrdmYswPmxCQww9Bdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=oujL-tBepBqIoJ2fAJHSRXc2m_rcilLaFUuIslYEoAK6LtdVMDcu5vdEbWejJSUEYCV6XZtp5g-CqUTWmB6M25ysDQw7kbi7LFtDpqU5eJMh8Ya7OdXVddy-xcCpfDgJZwJBLd9Vj1QtN4a8DE3eaQQpQELJm5jzLevhtyqDmtc6btu37dpu6BBZAzyK_umjlVRtSLFh11BPWTUbQ3_Qg6VRmZ9uphigVz0k4HKd4HW84M0LrJp5wWaQEF-4NBzJbvQvhRwIWafDtbOeCCvyHmJ5ImILvQGu_mydviscvKwsPlYjac664U8GMJgeAOGyLyW3CrdmYswPmxCQww9Bdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حمله دیشب آمریکا به پاسگاه مرزی شلمچه
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68839" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68838">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jENsILgCH3es4VynhgkbxIr0GWENXEoSW2xDC500Onnucpy8IYycSAGB-vdb5v-HJdb4nP-Z0kSkSKM4_zrBIyrIQYc5vVomgYIOc66DqJd_IZ5xkV_XQbVbS8TuVu2rZi_UmAdObuY0clFzMgtbk8t6m8eFw-2eQqh9ayP5ypczfm2527H_h-0duXDZ1NzFMNC0wunVVZ3o5_yKO-7QZ2_snAda_G6lzs9hCKXfHOoHe1Kk_TUBj-NCrDCJ2HsFNTAUSI6qRsoLAVRv1xYXDL1qvFsP5cZBmnnP0PYU9CV6MQbrWkE7k_98cO74vNTR9uxnpR6Hy5uoWJDHVwtOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته:
با این مملکت درس خوندن جواب نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68838" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68837">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQQ0mVdacPstSJl5xyjsAdRDEOGKZLiMkPy8uotTKSOLo3NWWNfINfXITAQnGLAAIUYMK1RqJEA4UtVp6yJ9YT6Fte9NxmiyvKiKh7jbWErmTxcM-UVntmHluqGuPXotRhhi9_Z9jseckevs22Hq7jGwh20Tu4BaGOTD8k-xkW2k_cxX-8KlA3b3IoX72iNGRsLOrF0ZeXVhs-5bFmTwTtg_vfpxev1Oq87hSMJlb-GtNT45iyq9ME1yl0_1y2xpcohUMGZBXrF3ritGnyI4poICouVv3AyqhdEvX1G1WNP5cjs0qb8qpuTvHSizLAVTapTKsYel_KPmwi-NRNaOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👌
وال‌استریت ژورنال: ایالات متحده در حال اعزام گسترده نیروها، کادر درمانی و تسلیحات به خاورمیانه است تا در شرایطی که رئیس‌جمهور ترامپ احتمال گسترش درگیری با ایران را بررسی می‌کند، گزینه‌های نظامی قدرتمندتری در اختیار داشته باشد.
به گفته مقامات، ایالات متحده طی روزهای اخیر پروازهای باری را از پایگاه‌های محل استقرار نیروهای عملیات ویژه به مقصد خاورمیانه انجام داده است. نیروهای عملیات ویژه در مرحله نخست جنگ موسوم به «خشم حماسی» (Epic Fury) در عملیات‌های رزمی جست‌وجو و نجات به کار گرفته شدند، هرچند توانایی اجرای طیف وسیعی از مأموریت‌های دیگر را نیز دارند.
به گفته برخی از این مقامات، بمب‌افکن‌های دوربرد نیز در حال آماده‌سازی برای انجام عملیات‌های رزمی بزرگ هستند؛ از جمله بمب‌افکن‌های «بی-۱» (B-1) که هم‌اکنون در بریتانیا مستقرند.
وال‌استریت ژورنال پیش‌تر گزارش داده بود که ارتش همچنین هواپیماهای سوخت‌رسان، جنگنده‌های «اف-۱۶» (F-16) از پایگاه هوایی «اسپانگ‌دالِم» در آلمان و جنگنده‌های رادارگریز «اف-۳۵» (F-35) از پایگاه هوایی «لیکنهیث» در انگلستان را به منطقه اعزام کرده است. اردن و اسرائیل به عنوان میزبانان احتمالی این هواپیماها در نظر گرفته می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68837" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68836">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⏺
فرماندار بوشهر:
روز چهارشنبه، یک نیروگاه در مجاورت نیروگاه هسته‌ای بوشهر در جنوب ایران هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68836" target="_blank">📅 02:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68835">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=XKD75xp8apOeMsSmQ3lXsP6cBE7c7w6p0O9m7Vo2y1Tni6JSgKOXMu1DVl7zXQhpCaUpCiJa3udamItfw0vaKEzTpiSoOhaZdWrSYMOkOYUsX-zQS8y3DtbVZHU58vsvXe722hgWBzB2QDDL2qsPf-KLvQS37rcaMMIeHt2tWUOQDNM0DlPWwXYB8pDLmswSScH7ObBsjTuVc6lTSuNxiyYhfMG441jFU6LSFSbDm-7x490Nea2udE5P_dNcH729WheVH--cD5W7LwnzpLs0og3yR0j33icN1slngN691EXVd-dwpPZt-Jaj-xWkWObViU_xjqUNrz9TUypPbqCWjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=XKD75xp8apOeMsSmQ3lXsP6cBE7c7w6p0O9m7Vo2y1Tni6JSgKOXMu1DVl7zXQhpCaUpCiJa3udamItfw0vaKEzTpiSoOhaZdWrSYMOkOYUsX-zQS8y3DtbVZHU58vsvXe722hgWBzB2QDDL2qsPf-KLvQS37rcaMMIeHt2tWUOQDNM0DlPWwXYB8pDLmswSScH7ObBsjTuVc6lTSuNxiyYhfMG441jFU6LSFSbDm-7x490Nea2udE5P_dNcH729WheVH--cD5W7LwnzpLs0og3yR0j33icN1slngN691EXVd-dwpPZt-Jaj-xWkWObViU_xjqUNrz9TUypPbqCWjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛مجلس نمایندگان آمریکا لایحه سیاست دفاعی ۱.۱۵ تریلیون دلاری را با اختلاف آرای اندک (۲۱۶ رأی موافق در برابر ۲۱۲ رأی مخالف) تصویب کرد.
این طرح شامل 95 میلیارد دلار بودجه نظامی اضافی است که عمدتاً برای تأمین هزینه‌های مرتبط با جنگ علیه ایران در نظر گرفته شده است.
این لایحه اکنون برای بررسی به مجلس سنا ارجاع خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68835" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68834">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0hru1Lr04gM0V5ROdAvYjMji1PHq3SUktopY-J4ywK7ejwlqqXkgwJDgWnMZCBOcutvv1smFexIRz6MDw4cCV_wJyQMGyV_VbdoAXib_8Pj73mjrCJJAD068N2kAmesxSXxWJHQjT0lGTQe8FwSFJp9yiiH-huzGmhShQdzZ1EOrDEKlCnNjyhvP5nle0DfXRI7iRBftgvAGAGFygV3AvfCeiGxvJ886P3SZmfwRj4Qz3X-0hZIwQcVUBJMO_zSiCQRHVu62bxDistTUt_gKWABijX77-H3u-HgK8yamQdJ45e4atW1ZSnbdQs82a3ab4wHoeEV7Is4azi3RRF3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ستاد فرماندهی مرکزی ایالات متحده (سنتکام): امروز ساعت ۵:۳۰ بعدازظهر به وقت شرقی، نیروهای آمریکایی به دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند.
این مأموریت با هدف تضعیف هرچه بیشتر توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاریِ در حال تردد در آب‌های منطقه، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68834" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68833">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدید حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68833" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68832">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇮🇷
هم‌اکنون حملات سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68832" target="_blank">📅 01:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68831">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPYzyLotDAn_M200zMnhbYsfWfySmt_6ZHx0uCz8jDl9dABGNjFXr-HWabeHc3NUnPtzqglMIm6rxl5XO61S8TH33vt84GanG5BhsjziD5QdxJZLPgmjJgYbLo9YBQG9-oFiIo1qYFXJl2_PF9MO6G34HY9woz3fn4ecfU1t1tRSrDSc_Tgr0mHemganqwNNWyT-ecvE7EXWK5aGsxF6C8AHzXr3vbpgN26WQhTBsmd8zF-0BhTisTizmdSoo-9lEQ3SG6LHFGK7B5iJVysytGzV_V1KpjcgDNAx7vzH6TOc1b8RCfDmWFLMBVCaEi89qvQN9jYmapA0C41jYOByhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب تا این لحظه هدف حمله قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68831" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68830">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyq1GloXi7oBbl9KWvY6ivhvTxedHBQ-f6RIIgjreZZHTDQhTnBl9XMNRkhKtL73-m7V6juaGh0qhVaKvK-mZl5wQkzBkCAHrCGwJZYV0JgGSU4bk4nc_XxB3q0cH3VgNbxkmTpXoqVOS2IwPQwCMYW5KSPmgRt8xLNjQ6R2Ew0N8J27rpIz2aAFEISTQQr8tftmCtmmQFqVWffKI7xHN4tPVu_Xwjc0MJRvSXm2oqMcuyZ5XY9IbIuwnujy8HzuLfLA-dl_O4u_F9GgaFDZPLcDB4c2YtxGI-ldtGXITSgZFbDzy1bjwWCYmyRs9K3POMsFeLVzj3VwklUObYp9GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.  @News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68830" target="_blank">📅 01:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68829">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30afc95033.mp4?token=MKgS6NHw9XNzkjRph3DsCZeUUJ4W77X9HWcgvt6Hkr6aCUDDoaU--3w9F6KGX5Ps4rfVjsDMdAXs9z3hdm7hbx4iyV-0QaZ_A8zxJcFVkFdoFgWEUzF8kUecIv68IIRTcoln9jLDiYQS6DzAQB_LgrxQ2kpBjmB7fp_aL7fl3UCfjihust1rOZkQk1HcyXF2V-ZK12UjjPAiHyB_zFwTNSVvgw3HdQ0NODex9Gfn1rskaHljVW3abjlCwFeSQysU9U_b9FZNG0eceS0WNI6ppdoEFZPkWYrkQZdA4rh1W-G9rj-lJv1ZjzmuNaE7cdevmCx0lRsM7T9qGjOTILDFkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30afc95033.mp4?token=MKgS6NHw9XNzkjRph3DsCZeUUJ4W77X9HWcgvt6Hkr6aCUDDoaU--3w9F6KGX5Ps4rfVjsDMdAXs9z3hdm7hbx4iyV-0QaZ_A8zxJcFVkFdoFgWEUzF8kUecIv68IIRTcoln9jLDiYQS6DzAQB_LgrxQ2kpBjmB7fp_aL7fl3UCfjihust1rOZkQk1HcyXF2V-ZK12UjjPAiHyB_zFwTNSVvgw3HdQ0NODex9Gfn1rskaHljVW3abjlCwFeSQysU9U_b9FZNG0eceS0WNI6ppdoEFZPkWYrkQZdA4rh1W-G9rj-lJv1ZjzmuNaE7cdevmCx0lRsM7T9qGjOTILDFkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68829" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68828">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
صدای دو انفجار در بوشهر شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68828" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68827">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
فارس:
حملۀ موشکی دشمن آمریکایی به یک سولۀ انبار آسفالت در اطراف رامشیر استان خوزستان.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68827" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68826">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJRHLqeX_EfNnRxoNWMr0_qakiUjzsN_zj3HuxiO2jeUsJUG9rU0PQSdYHBAfEGB1J0a8jh1euW4VNOwWfjvG3wvDV_76EeSCek25dmXhsRvpO5fgzi5JjrpF0FPBruDllEJxWeOEQHvDClWo4uXRO2l7xOuHgVxLBQJu8xNHCO1W1_isIMycMlrXBu_t1w0kpaogFbvfijduy0MdpGnYzJikbfi9M_OL9fvo99tVkX1Hf4V-c6RUcsaQNUDK5kyS5QhsBo3fVMeAM_97lA_iMpMGNGDM-pTlGGpzbwHg5LFVjx7_3RDpiGdz4PQy17bGljgmd9yBBxOkJVQmAd3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یک جریان مداوم از تجهیزات هوایی آمریکایی به سمت خاورمیانه در حال انجام است، که احتمالاً شامل هواپیماهای تانکر سوخت‌رسان نیز می‌شود، در چارچوب آمادگی‌ها برای تشدید عملیات نظامی علیه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68826" target="_blank">📅 00:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68825">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
پاسگاه دریایی زیارت در سیریک هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68825" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68824">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
دقایقی قبل صدای چندین انفجار در اهواز و ماهشهر نیز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68824" target="_blank">📅 00:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68823">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
صداوسیما:
چند دقیقه پیش، صدای انفجاری در منطقه بمانی، واقع در شهرستان سیریک، شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68823" target="_blank">📅 00:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68822">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/030860acf9.mp4?token=pBkeqNEUZfj_VL87QH5zKIWSnn2znzVAo8K0nJ8H7PHqF_2S8Utoi_40JzlnF6VtrVrxYZ72ux8N2nr-mpFQQnxZVHqIdDLPQle6OLWfREdmybZyOvIkAtUD8SFPllOpE6OWueNuQaXYbMEOJXw_lPDtaxm_vBCd0Z7ErW54SEs11yCsm4-UZHxD5QMp2Zqq8hfWpN0TuozsL-31Nska6gi6Mo36WfEc7PL7Bi2Y54v2b1XIbvakz-PstVMCviFe1yW0NKuOKvDnlMMCIw37ge2qqSHfP5JY5r5CaXdRRioP4KHIBTWwMAkSixZbiy5NTS_ArRSP3hCs1CS6BwXD5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/030860acf9.mp4?token=pBkeqNEUZfj_VL87QH5zKIWSnn2znzVAo8K0nJ8H7PHqF_2S8Utoi_40JzlnF6VtrVrxYZ72ux8N2nr-mpFQQnxZVHqIdDLPQle6OLWfREdmybZyOvIkAtUD8SFPllOpE6OWueNuQaXYbMEOJXw_lPDtaxm_vBCd0Z7ErW54SEs11yCsm4-UZHxD5QMp2Zqq8hfWpN0TuozsL-31Nska6gi6Mo36WfEc7PL7Bi2Y54v2b1XIbvakz-PstVMCviFe1yW0NKuOKvDnlMMCIw37ge2qqSHfP5JY5r5CaXdRRioP4KHIBTWwMAkSixZbiy5NTS_ArRSP3hCs1CS6BwXD5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه روز پیش که پل کهورستان رو زدن ، سریع اومدن یه جاده آسفالت از رودخونه خشک شده اونجا کشیدن که رفت‌وآمد متوقف نشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68822" target="_blank">📅 23:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68821">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=isPqFfvWqPMkRadFgnCAs4JJR9-7w2GyQK0lWWCnIdU5XN4YgXqwvzlvOSXS8dyJyUPYU9sI9o14LVZ_u_dgEV-PL5CDXgwLeTenGp0W89DxMWEw2RHzr7YtD9DPP645psiysSu8Sit6Yj0Xn7Vsf9HajBJMnAqSJKf3BwcROnE_0Y62phYrf1QTnpSjLSOAqGJBkW7PHaaYvI-7-ELlbzolZYtzInaddn0jF4hwBmB8L-UZaxnEEL13_4KaP17uy_1_tqF4xFBPMUuP8UnUPyckXo1PJ54dbnK5qxtpA98XeqmRfSEQurKyaU0Pzk-7GVrxqx6RMHtx2NI_CjPOHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=isPqFfvWqPMkRadFgnCAs4JJR9-7w2GyQK0lWWCnIdU5XN4YgXqwvzlvOSXS8dyJyUPYU9sI9o14LVZ_u_dgEV-PL5CDXgwLeTenGp0W89DxMWEw2RHzr7YtD9DPP645psiysSu8Sit6Yj0Xn7Vsf9HajBJMnAqSJKf3BwcROnE_0Y62phYrf1QTnpSjLSOAqGJBkW7PHaaYvI-7-ELlbzolZYtzInaddn0jF4hwBmB8L-UZaxnEEL13_4KaP17uy_1_tqF4xFBPMUuP8UnUPyckXo1PJ54dbnK5qxtpA98XeqmRfSEQurKyaU0Pzk-7GVrxqx6RMHtx2NI_CjPOHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به تنگه‌ها احتیاجی نداریم؛ اصلاً به هیچ‌کدومشون نیاز نداریم.
ما نیازی به تنگه هرمز نداریم، اما مجبوریم این کار رو انجام بدیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.
من اسمش رو جنگ نمی‌ذارم؛ یه درگیری محدود بین ما و جمهوری اسلامی ایران.
اون‌ها اون‌قدر تحت فشار و ضربه هستن که می‌خوان توافق کنن، ولی به نظر من هنوز آماده توافق نیستن.
الان هنوز آماده توافق نیستن.
ولی خیلی زود آماده می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68821" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68820">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🇮🇷
ستاد مرکزی خاتم‌الأنبیا:
رئیس‌جمهور ایالات متحده، که رفتاری بی‌منطق و جنایتکارانه دارد و به قتل کودکان متهم است، بار دیگر تهدید کرده است که به زیرساخت‌های این کشور حمله خواهد کرد.
اگر این تهدیدات آمریکا عملی شوند، نیروهای مسلح جمهوری اسلامی ایران اجازه نخواهند داد حتی یک قطره نفت از کشورهای منطقه صادر شود، و زیرساخت‌های نفت، گاز، برق و اقتصادی منطقه هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68820" target="_blank">📅 23:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68819">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=Neu9iAbUa2jBDXBKYtL6_G4GDdh3dyim_lHZNHsQP6951jITx2oOfEfpL8udyqPtGxckHCIs9rd8IqTwilsjYIhIAIqRV62GC8KJm2X8M1vxcyLSVBzjqeoTVnkB1GYcXm8twA6tdajbAg61p24JbviAJCEcYUIMXPSqY57sUClKLIw9NJm0vJZ2R3RztQsuqqj5dSnvXDtOB9pz5mvRBDoCc9bhbS2XDX5YY_z0Pii4UWklu_W1SuYbFiJ-0CQiLXrFLkIEPHqinCGB6jjTuqvP7jWC7_T6VDWMLRnxcR2FgemZShIfMXUhciQ0brbEsb64Yb01FKBb3LZht5vBJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=Neu9iAbUa2jBDXBKYtL6_G4GDdh3dyim_lHZNHsQP6951jITx2oOfEfpL8udyqPtGxckHCIs9rd8IqTwilsjYIhIAIqRV62GC8KJm2X8M1vxcyLSVBzjqeoTVnkB1GYcXm8twA6tdajbAg61p24JbviAJCEcYUIMXPSqY57sUClKLIw9NJm0vJZ2R3RztQsuqqj5dSnvXDtOB9pz5mvRBDoCc9bhbS2XDX5YY_z0Pii4UWklu_W1SuYbFiJ-0CQiLXrFLkIEPHqinCGB6jjTuqvP7jWC7_T6VDWMLRnxcR2FgemZShIfMXUhciQ0brbEsb64Yb01FKBb3LZht5vBJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو این اوضاع ویدیو های سمی هم وایرال میشه
😔
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68819" target="_blank">📅 22:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68818">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVRSvGMzQK_4w7kwMvp4jXTmnThoT5OPeSQHaMmkoq2pVm0zTfaAZwnmm2kqVfhUVW9NHoTGuVKnDfqq9NWRnL0qNvyUlBY6l4RjKGJOaJXC1aJjV76XZK8nSllfduRYct3_jF_rBBlbw1uGdW3ZZdVM47OQMdLX42wF0z04GHnNQyO9aMZUh-pyA5ZPTXhSf0OlaHMo2s1_nvLJWtAWoP5MGHs4M-6RpOJFE9c8HGtIgEY_OI9sJXnc3-iFK1j2yXD6-RmZ73yZrqK7jN9q7VoaEvO7ZH6PM4KizIZqbCLy-3Rs5KjxFtEKdO9ucrL5TVY5TsrgkUe2fgu78vBFzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مجید موسوی فرمانده هوافضای سپاه:
اگر به پل‌ها و نیروگاه‌های ما حمله بشه
خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعیه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68818" target="_blank">📅 22:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68817">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=mOmqWiFiuxy3-ES01qpgeYwFzGFQ4IgRhu2-p0b9PHyUsMpMBlnCelJ0-7Ex9COzWhVMr5z43Z337GbQOkqtSnknJnfKd4Gx-4CyhWcKAzKK13rYfxHq0R_huTkGhoCWTReucToLXlGJPvx1UqSKF5FB02pCDaPOJn1g-8npE1KBs1w3JDo7gpvDQOzu8ZMw13dQl6pPHB1UVbjkw6FGeY1S6GEFNCQeFCZ3Xo9emeTHnjcPY80ilBE9hDd7XB0Us52DzVV1ijvk7crO8C2y39kYO7nc7ScAIiGKMGqbs-hAVIysps1NM-ZgaKUHSG0tN51ZS7lQ3m0gBuE3YJUreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=mOmqWiFiuxy3-ES01qpgeYwFzGFQ4IgRhu2-p0b9PHyUsMpMBlnCelJ0-7Ex9COzWhVMr5z43Z337GbQOkqtSnknJnfKd4Gx-4CyhWcKAzKK13rYfxHq0R_huTkGhoCWTReucToLXlGJPvx1UqSKF5FB02pCDaPOJn1g-8npE1KBs1w3JDo7gpvDQOzu8ZMw13dQl6pPHB1UVbjkw6FGeY1S6GEFNCQeFCZ3Xo9emeTHnjcPY80ilBE9hDd7XB0Us52DzVV1ijvk7crO8C2y39kYO7nc7ScAIiGKMGqbs-hAVIysps1NM-ZgaKUHSG0tN51ZS7lQ3m0gBuE3YJUreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ظهر چهارشنبه؛ لانچر مستقر در تپه‌های پشت اسکله طاهرویی (سیریک) که روز گذشته مسئولیت شلیک به سمت کشتی‌ها در تنگه هرمز را برعهده داشت، خود هدف اصابت موشک قرار گرفت و یک ستون دود از محل برخورد دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68817" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68816">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzkmQQ-MU4CrrnwaEy0utDaNjBaQ0uD3RA5d4KpIoPPBHjrpi7mXe8x-JXIZYi7Ke_QixiaFfsRMAKkm2C4eD_07YPkR64-6TiSbt47fKvxEHQQ_Z9zSo4qesExx37IMdm4PdnmOTKFMcQsvpksk7-rHqPnRH1p4fiIQvLBZ04_GBVSvfh-oaSzWBO_kca_yaGMBl2F1i5QoLvoVlP2T5uF87yNtdot7su0f_mWA_6s7pnguBc5hnz_gUDemoq2epe7erZKIZ9BbOWThPH8H_MJCgrHsPYzWC5g7hAxBbtthBnDVccm0kPrBmmW3ZxIDFKfsGe6nWXQrD17CVb8C8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت.
اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است.
بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68816" target="_blank">📅 21:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68815">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0XPgJcAsad32SfyDkYOzn2w8QDchVpCj0cgAhRqXEaWLewcAELJpWZ-QKy5CDzBo4Hx0DwAwWVcEarP9Of4rtJpY4NAKM6aKTLITVHlDYqm6OWrG5-gH4IVARySq5IhtPv5Q5bzYv6dhwrubsMY80_H7WaFu2EZFLkoHk9Qazlmx87Uw2QarnCX1Tu4xql3fM5VX_xl0lJYbRcH8xlmy5orkBn4c6fIWSBUHLaoaprvte_bKjJlhYAvHlP2O7FhSJyKwgq0lF-O-SflnYBZv5T5Sh_RDeLYMyczYJdVSaoS1w-hG4eERLNVxkcu45B-0qQPp2703Aw9pvKti8fsdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال:
رئیس‌جمهور ترامپ به‌تازگی اعلام کرد که پس از کشته شدن نیروهای آمریکایی، به «سنتکام» (فرماندهی مرکزی ایالات متحده) دستور داده است تا «درهای جهنم» را به روی ایران بگشاید.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68815" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68814">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68814" target="_blank">📅 20:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68813">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta7LwFqww_9djzCmGOb-8CIVmgWbxCbnUvUAJp5uv3chq_EkM5AsfTmEUseGSlEJS2IFcQwwEhpGyebsJptfwqMYM6b8_00AD3in7wu9uwbIFSqYxRZzgdDOPei_URwbE7WX-UzlpweLUd4E0XlBu4vWkgpZfSGdGcfjhSmuF7eqHSBvZzVwEVUuBzFj51WsCx4n5utZ9o7hKQuHOBdBsTnOxbbc1Ox8tpv7nRr71Y9WYxQUp-UJQ-vXelBFYB6rNKQsFAfssbv9tof2__2mrWVoZlkXJYVYUv58SG6hJaPKK285jrlCLMXHb3x-L476V4jJZPLxJT9JO9L0oXeSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68813" target="_blank">📅 20:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68812">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYMh9608T42jit2vuj9hcSbjRAA-1plGpiKAupk_XVxSiSpWRRT3Xx550YH55EcUwkAj6EDmcItjP9wFhyu0UPk1Gq3NGse0DxXwGdR1SrhisNCo13Ync6_QCjIt6obgJHDCFbmSzkYjivx03-vD4M35flz5uxk35xOwlexOkd5G1HzVkLQK_yuBVczdksvREyB2i1WVUO-NdmateJCJszWDlWGMz7f-YqyPS1EdABXo0fqaiCFZp08bw8l5fZgornH_ADq_6V9GVj1yVUH7lSF6FUkbKR3J_buhgsmXz5Q8BC0riSrRcIoFm7Io9_yJ5oyPrwJ-KoD9asiazzq_Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یکی از حملاتی که شب گذشته توسط سنتکام در جریان یازدهمین شب متوالی عملیات علیه ایران اعلام شد، بخش نظامی فرودگاه بوشهر را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68812" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68811">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl3dihz_WhJiIhzRR812K1OX4iONOxCBFyK46GqTTmx-IE4mWf3BqLTRvVesFoAR6G0_rQuUdahoGi3GHe1v1LTHeWyLrR6bzIki-LXZDJdQ08YCYx-7qH54q2iYnDnnu1y48rQ_Mt-NraihZ9ZPYVts8uHXTCqvMfdAhuPz5PvWxgYGVJux4DP_ablVbZC4XIuSSKoa3KKrVo92rKN_MOow6vqBmdnylhMmSorIyAFAAu7es6S0mRIKi1TvT_461j-6YXbAHUqpDWb9TigcD92vJ0aeY0VvRzgcocXf5arx9Ft1LVUfaPwcbVFY8waJ1uMej1ua2aV0pbDLM_t5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
قیمت نفت خام برنت به 93.14 دلار به ازای هر بشکه افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68811" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68810">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVCrBnFPoeJIcy9duk1eceetx3cj5BD_vsWCytPexm74UVIgGYlMPbRAltgRaedseAMZ1EaPMn9-A2siRrIZrM2uLcV6m3jhUYLBJvj8F9STQJ1QGPM2kIWWipKZYQW1nLdpniMfTwhE4Zj5hZPf5F0FHAiIZ2gyQ5nAsZKzAUywTS53KtN58gmuo9b1E0H0qRgvGKoI45E_VvhGfzJ_Mw-PfdhxnoCbZgW7Rg4SPHpG4wctHJWQC6ny3aYs1C0AsZJI3Xsk7v4PpE--8jNtpvcREArtg5T82ibFtys23ro_dpe_nyQY1yQ-5CNJ0akKp-fJE6uXLVBcXoUBocwvVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68810" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68809">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=DwF3MKuYkVAbI6CzMEVY_18yIsZSNCMbkUdZ356fq3Qu9Qe4Xa5_ymUlztv-ANCGMYcbVYPmKG6wV5IpNI1ZHSYsmhWQLFdEIBlymIoIu_24kdtxGiW4XoPH2pGW0R02jAXm9VFpGOr-kgNnFlgzIOoDfOYsJASTk9C5dxGO2_MyO_qo2ha_BA3onhRauTRVaIFiXRvY5OG8X0O2qVn059LGabvyOamE3kKOo8ZiDh5aWt0ceaFyhu1XM1e7oxYDZXkbHIHFiqYeeEca9Dv33EnJaB_3LViUdc2UowCePoRA_jqv54DMzm8C_YmdeHKfndgCKZpyK08d5UtymysiUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=DwF3MKuYkVAbI6CzMEVY_18yIsZSNCMbkUdZ356fq3Qu9Qe4Xa5_ymUlztv-ANCGMYcbVYPmKG6wV5IpNI1ZHSYsmhWQLFdEIBlymIoIu_24kdtxGiW4XoPH2pGW0R02jAXm9VFpGOr-kgNnFlgzIOoDfOYsJASTk9C5dxGO2_MyO_qo2ha_BA3onhRauTRVaIFiXRvY5OG8X0O2qVn059LGabvyOamE3kKOo8ZiDh5aWt0ceaFyhu1XM1e7oxYDZXkbHIHFiqYeeEca9Dv33EnJaB_3LViUdc2UowCePoRA_jqv54DMzm8C_YmdeHKfndgCKZpyK08d5UtymysiUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس انقد کد کد کرد که
کص
از دهنش پرید بیرون
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68809" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68808">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=dBKYhKLc600wo5O-B2MT0Kfan8oL-TZMSV-p30dCZmoeQ0ENExicTil3ZKbbTfsEFbf-_MkNPCC9QKrb_wMTqm37sdSQq1-M1RVtNSWvcEs0jORbqeUKBqoC7TQxW5wgWS-L_xmjxHfjaZuQOWmRvhZ55E3IkiZxyvwTk_s45kC3KcoQ9UXszCLzJdhtzvkBjNu4I97Om0AargUmkd7ioCvrDczhHAx9zD0IQWlfdm0OLTwaoTEYwIUu1QCYOhigc--1-IwYcOWkKqvv-lwcj8KZk7PzAo1PiII5su3g_CwsBzjh_8zASQn9u5PyA_6C3zwgYbcPFZ47_sjijmHT-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=dBKYhKLc600wo5O-B2MT0Kfan8oL-TZMSV-p30dCZmoeQ0ENExicTil3ZKbbTfsEFbf-_MkNPCC9QKrb_wMTqm37sdSQq1-M1RVtNSWvcEs0jORbqeUKBqoC7TQxW5wgWS-L_xmjxHfjaZuQOWmRvhZ55E3IkiZxyvwTk_s45kC3KcoQ9UXszCLzJdhtzvkBjNu4I97Om0AargUmkd7ioCvrDczhHAx9zD0IQWlfdm0OLTwaoTEYwIUu1QCYOhigc--1-IwYcOWkKqvv-lwcj8KZk7PzAo1PiII5su3g_CwsBzjh_8zASQn9u5PyA_6C3zwgYbcPFZ47_sjijmHT-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
عراقچی: ما به هیچ عنوان غافلگیر نشدیم!
واسه همه سناریوها برنامه داشتیم و کد بندی شده بودن.
سناریو آخر این بود که رهبری (علی خامنه‌ای) رو بزنن که کدش 110 بود.
تو جلسات کسی دلش نمیومد درباره این کد صحبت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68808" target="_blank">📅 18:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68807">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
یک منبع نظامی به تسنیم:
هر پل و نیروگاهی از ایران هدف قرار بگیرد چندین زیرساخت و تاسیسات انرژی منطقه را می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68807" target="_blank">📅 18:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68806">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:  بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.  @News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68806" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68805">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=ePiZPcRNaoplOUigj92mDCKhKP4hnYk7KmpyJr0i12oLT9fkjQxjrGoRBPL16L4uIKXhow7YIqsrDtDU_N_KaFKCXibcElea4W43eTvfNiNd2CfcL5ru2uMdu2oBaqJ7k_uWRqNXEkga-hrTwrX-giS4IOdi4QzODp9oqRM2YpnEyioVPto3LlMwLd5evF9DQD_HlbaOw6fb28eJnJpMIT5YwP1Xw-l6wmYlmuMvFSgk_Z2iRt8jap0MuCBzc15sI-RpKnoLmrFMhjZrimIfeD1VWk9LUTJknPr-DEipUZaInMa9uuhxFJSKGBdGFx6Yv5Hnj_oo8qjJPd2mh0DkcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=ePiZPcRNaoplOUigj92mDCKhKP4hnYk7KmpyJr0i12oLT9fkjQxjrGoRBPL16L4uIKXhow7YIqsrDtDU_N_KaFKCXibcElea4W43eTvfNiNd2CfcL5ru2uMdu2oBaqJ7k_uWRqNXEkga-hrTwrX-giS4IOdi4QzODp9oqRM2YpnEyioVPto3LlMwLd5evF9DQD_HlbaOw6fb28eJnJpMIT5YwP1Xw-l6wmYlmuMvFSgk_Z2iRt8jap0MuCBzc15sI-RpKnoLmrFMhjZrimIfeD1VWk9LUTJknPr-DEipUZaInMa9uuhxFJSKGBdGFx6Yv5Hnj_oo8qjJPd2mh0DkcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
دونالد ترامپ درباره ایران:
«آن‌ها بهای سنگینی خواهند پرداخت. آن‌ها در حال نابود شدن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68805" target="_blank">📅 17:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68804">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rm20L7Y52xljfD8cFSZQFswFvjsVdv5yMhp4jyHxnESbq5dz6C4djzHAgybEcZwf6UMolZeZKsKxYQR7qv-qg7-9KHvSWwy4iQAsg297uwcmh_Jj-zYnz9AW0C-6GpyrJFA4oSCfeI2Gd6VK0UfZCk5k_fmkXnj8dIuJmt_k8objpmBKA-fmezqtqlJ39XoQiiaB5VyOypYf176GNO0z_8BBW7o73Lf3J6zM83N-enhRBfP3pO-sBrWtiB8x5IEIcOIoNxDHV6HIJ6VAE6h1mXs8OC-kX4C6Dd5Uo-N5P-8lZmuOWGMKME-R_9aLkywtHH9ixtzQ1LMAtr3DpfvY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68804" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68803">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfzezRz1RF5ls_7iX22E4PYvwdwejXW3lnp86DDfQCF5-shipjAzABBw_vJNF-Pa84yr1PvrdoD2wHmrXDK6l7N9rJcuUUOkYTcu8w3aolkYhSs35b0VICVl2s9n44pweRIy77y4I4Ov-P1dcB6RHvkWq6C2RvbRF0GTFsucoceVFt40fTnVY-u85Wxcn6NqTKxUt74DR4hY9exN5IuHfOVbGNN8crUdfqfWygpSxEqYG2eHZ3DWGiwuw8-BLfELpEsJcvLC1DcQH09LYeKWqXGb-pJ9gTAwpL_8fK7VQs_PX12PsoCgvKa1WII4zkOG4vWttlCcdBtYS-9cAp2s1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه
حتی اگه نزدیک تهران یا داخل خود تهران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68803" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68802">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=JkjJ8AeVK1bpwm5O2tk_gPc2K9wfFzZNSOwEi9Q9sijmo4tzt5T7wMzTRQIy-DND85ECeYqHTqF2ugyvqZ4VbiSyb1Ya8oR6n6dhwphxYJeL2u-soF_ghkRis3FW11P_OI3O54Pl-jQJWmw0fv_6olKr0l_Gc1xPZZw71SK_2baeWq6iZ5b5pDwdKe4cIXc86NwLvO7ZPETQ7siC9IYIQ6FN8bbwR1nh1fTHoWOUU-LEwx7U-g-yh6wAtEDDrPtLD4gvtgFMiUlp7T7cYCV6EAY21Zd4JxUXvN_dATHcYiCo8-c0nlj5XmUr2q6nK6vqpjkUSQymMI7cWotJvzONgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=JkjJ8AeVK1bpwm5O2tk_gPc2K9wfFzZNSOwEi9Q9sijmo4tzt5T7wMzTRQIy-DND85ECeYqHTqF2ugyvqZ4VbiSyb1Ya8oR6n6dhwphxYJeL2u-soF_ghkRis3FW11P_OI3O54Pl-jQJWmw0fv_6olKr0l_Gc1xPZZw71SK_2baeWq6iZ5b5pDwdKe4cIXc86NwLvO7ZPETQ7siC9IYIQ6FN8bbwR1nh1fTHoWOUU-LEwx7U-g-yh6wAtEDDrPtLD4gvtgFMiUlp7T7cYCV6EAY21Zd4JxUXvN_dATHcYiCo8-c0nlj5XmUr2q6nK6vqpjkUSQymMI7cWotJvzONgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مقایسه جمعیت ۷۲ هزار نفری در کنسرت فردی مرکوری در ومبلی لندن (تیر 1364)
و جمعیت مراسم نماز و تشییع علی خامنه‌ای در مصلی تهران (تیر 1405)
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68802" target="_blank">📅 16:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68801">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⏸
ویدیو وایرال شده از گریه های یک دختره بخاطر مردن سگش
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68801" target="_blank">📅 16:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68800">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏
🇮🇷
سپاه پاسداران:
«اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت»
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68800" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68799">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoSW1jS4Uve5A_gqNCuSlTPoYcz4gN-8ZB25T6mwaQhf4-T50o-Q5_LBjShDxKYbTBxsDyJnEoq_DKHRW0m6uoYFrwHQy5ONF2XTzP6grq81GwNrvGFZzq4CrmsV7sxZKci2bcX0xaUgK2BphkYLvoE-f1req3dqs3S8P5wyIN3lOgfv5bImMIeJa7oBCQkPG9yMob1bhT0OJbFuwPaOotAKeMiINWvvb2sBgoi7XSQu2zymeE08sDxog6_0tsz5xhq7AxG1_pXHHEaRRyTXIrt8UgT17fEWKxS0lkJhllfVXsjDKB3MOofISWFBFMGwth_0AiMy92n8GLL3eberSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آژیر خطر در عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68799" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68798">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران به بحرین و عربستان سعودی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68798" target="_blank">📅 15:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68797">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=WZ14Jm9fmv56klG0DX6jGwGxlP2Z3e3p-g7flJG6L0Zgt3judp1WPVWRZgrn7xIQmRKb7nqMm6kLWEUpgbwjSpW_xSBgGLbxnTnTXB1enJQFdnf7J0THsjqFbK_KT8TbvC37z3c5uHFPZyhU_5gHQD7FOyfHJSqWcEg7vihMKJF6EcMXJluWYzDRyBTCqLGSirE7uqiwj5hsnW8-6Cv9vmgxTGS5wunVvz3wYbSf38ttjPMBohQ9yRN9j6FaRAAz96r7uTcSq1-OFVqEFbQA8q0KVe7cwqr_wqI6yQ59JUHQ5IUWiPPtvKPzs41kpUZYbjv18LjX7uwvditQymKGzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=WZ14Jm9fmv56klG0DX6jGwGxlP2Z3e3p-g7flJG6L0Zgt3judp1WPVWRZgrn7xIQmRKb7nqMm6kLWEUpgbwjSpW_xSBgGLbxnTnTXB1enJQFdnf7J0THsjqFbK_KT8TbvC37z3c5uHFPZyhU_5gHQD7FOyfHJSqWcEg7vihMKJF6EcMXJluWYzDRyBTCqLGSirE7uqiwj5hsnW8-6Cv9vmgxTGS5wunVvz3wYbSf38ttjPMBohQ9yRN9j6FaRAAz96r7uTcSq1-OFVqEFbQA8q0KVe7cwqr_wqI6yQ59JUHQ5IUWiPPtvKPzs41kpUZYbjv18LjX7uwvditQymKGzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی:
هم‌وطنای عزیزم، مردم بزرگ و شجاع ایران،
با توجه به اینکه تنش‌ها داره بیشتر می‌شه و احتمال داره حمله‌ها، مخصوصاً تو جنوب کشور، گسترده‌تر بشه، می‌خوام چند دقیقه باهاتون حرف بزنم؛ به‌خصوص با مردم عزیز سیستان‌ و بلوچستان، هرمزگان، بوشهر، خوزستان و همه کسایی که کنار خلیج فارس و دریای مکران زندگی می‌کنن.
🇮🇷
جنگ و بحرانی که الان کشورمون گرفتارش شده، از نگاه من یه مقصر بیشتر نداره؛ جمهوری اسلامی.
ولی جنگ واقعی، یعنی جنگ جمهوری اسلامی علیه مردم ایران، از 47 سال پیش شروع شده و هنوز هم ادامه داره.
همه مردم ایران یه جورایی از این حکومت آسیب دیدن. نذاریم کسی طوری حرف بزنه که انگار جنوب ایران تازه وارد جنگ شده.
جنوب ایران از همون روزی وارد جنگ شد که بچه‌های بلوچ به خاطر نبود آب آشامیدنی و امکانات اولیه، قربانی گاندوها شدن؛ از همون روزی که جوون‌های سیستان و بلوچستان، سرزمین رستم، مجبور شدن برای یه لقمه نون سوخت‌بری کنن؛ از همون روزی که هرمزگان و بندرعباس، با اینکه بزرگ‌ترین بندر ایرانن، تو فقر و محرومیت رها شدن؛ از همون روزی که بوشهر با اون همه منابع گاز، و خوزستان که قلب صنعت نفت ایرانه، خودشون از ثروتی که تولید می‌کنن سهمی نبردن.
👑
اما ایران آزاد یه کشور کاملاً متفاوت خواهد بود.
با روی کار اومدن یه دولت ملی، کاربلد و توسعه‌محور، سیستان و بلوچستان می‌تونه با تکیه به موقعیت راهبردیش، جوون‌های توانمندش و دسترسی به آب‌های آزاد، به یکی از مهم‌ترین موتورهای رشد و پیشرفت ایران تبدیل بشه.
چابهار هم می‌تونه دوباره به قلب تجارت ایران و دروازه اتصال به اقیانوس هند، آسیای مرکزی و بازارهای جهانی تبدیل بشه؛ با احیای همون برنامه‌ای که قبل از انقلاب 57 قرار بود اجرا بشه.
هرمزگان، بوشهر، خوزستان و جزایر خلیج فارس هم با توسعه تجارت، گردشگری، صنعت و جذب سرمایه‌گذاری، می‌تونن به ثروتمندترین و پیشرفته‌ترین مناطق ایران تبدیل بشن.
✊
هم‌وطنای عزیز،
🇮🇷
این حکومت نه برای مردم پناهگاه درست کرده و نه حتی توان دفاع درست از آسمون کشور رو داره. در حالی که خودشون تو پناهگاه‌های زیرزمینی قایم شدن، از مدرسه‌ها، بیمارستان‌ها و مراکز غیرنظامی استفاده نظامی می‌کنن و مردم ایران، حتی سربازای وظیفه، رو به سپر انسانی تبدیل کردن.
توی جنگی که جمهوری اسلامی به کشور تحمیل کرده، اولین و مهم‌ترین وظیفه شما اینه که مراقب جون، امنیت و سلامت خودتون و خانواده‌هاتون باشید. چون شما سرمایه واقعی ایران و نیروهای اصلی برای پس گرفتن کشور هستید.
دفتر ارتباطات و رسانه من هم به‌زودی توصیه‌ها و راهنمایی‌های لازم رو منتشر می‌کنه تا مردم بتونن امنیت خودشون رو بیشتر حفظ کنن.
آماده بودن و ادامه دادن این مسیر، یه مسئولیت همیشگیه. هرچقدر مردم قوی‌تر باشن و جمهوری اسلامی ضعیف‌تر، رسیدن به پیروزی نهایی سریع‌تر و با هزینه کمتری انجام می‌شه.
👑
پاینده ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68797" target="_blank">📅 14:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68796">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=TR2w63M2OakjMe4-VfJE6bjhIIPFGl1jIGzsIml-Lk-UjKI-f3G9825NsEXfsEsWwjK3QWw4jBISDIevzWn7TMSK06UHi9ApB9qp-AnECRt6NC-eivjj_mEcyJgPwB180J2CvSo2QXxl63_mDtxI5RPRxCvDf736aYUBRYfhBEsJGTSefADcmySE4P4UZWCXs-GzsHDV7TU-0iXy18FzWsc6b7HJJZjWgqxKrz_BHDobPU62z-77VNBCHfdNJlOltcaSq-Fo0ZocH1RzRYFL_IWmvhyhcwqYpjUkZrJ_sYouHghRJXEMQMRt1M_NTHclOHca2JAHJVAQiZuigXOHUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=TR2w63M2OakjMe4-VfJE6bjhIIPFGl1jIGzsIml-Lk-UjKI-f3G9825NsEXfsEsWwjK3QWw4jBISDIevzWn7TMSK06UHi9ApB9qp-AnECRt6NC-eivjj_mEcyJgPwB180J2CvSo2QXxl63_mDtxI5RPRxCvDf736aYUBRYfhBEsJGTSefADcmySE4P4UZWCXs-GzsHDV7TU-0iXy18FzWsc6b7HJJZjWgqxKrz_BHDobPU62z-77VNBCHfdNJlOltcaSq-Fo0ZocH1RzRYFL_IWmvhyhcwqYpjUkZrJ_sYouHghRJXEMQMRt1M_NTHclOHca2JAHJVAQiZuigXOHUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تفاهم‌نامه هیچ حقی برای حمله ایران به کشتی‌های تجاری قائل نشده است
.
🎙
خبرنگار:
آیا این تفاهم‌نامه (MoU) ذاتاً دچار اشکال نیست؟ چون در بند ۵، به نوعی به ایران نقش و اختیار در تنگه هرمز را به رسمیت می‌شناسد.
🇺🇸
مارکو روبیو:
فکر نمی‌کنم متن تفاهم‌نامه چنین چیزی را بیان کند. این تفاهم‌نامه به ایران حق نمی‌دهد که پهپاد و موشک به سمت کشتی‌های تجاری شلیک کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68796" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68795">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=QC8g3O7jRa51otYbq5LJ1_RD2q463lWaQcBCRnuGigvjTvfAjZgRWjPJEtylswFtSXPYlTidrh5SFY3mrIs4Ebuo_BS8edLJSmO5bVPJVkdrIXjEj4f-a3hXSGVgoLFeQnoj_fPhn83r4x81W27EtXtSKYVc3b2IJAa0v8z9EhNfQSqn-oFCyfJxZ7nbo-OoUWc4Q4JMB4rlaHiCzxa-cBtn9r4Y9Mu0XpVIl0yI-5WI0OjtZC5_JKBsm0Lw0qNXs-JosuOoKlTexoW3QcEwdzuHI9pO-dyuah6rX9XTLvHg6UFVsUGS8W7MZ4qVTAs6g5mJW70Lnj_-78AuNo2nJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=QC8g3O7jRa51otYbq5LJ1_RD2q463lWaQcBCRnuGigvjTvfAjZgRWjPJEtylswFtSXPYlTidrh5SFY3mrIs4Ebuo_BS8edLJSmO5bVPJVkdrIXjEj4f-a3hXSGVgoLFeQnoj_fPhn83r4x81W27EtXtSKYVc3b2IJAa0v8z9EhNfQSqn-oFCyfJxZ7nbo-OoUWc4Q4JMB4rlaHiCzxa-cBtn9r4Y9Mu0XpVIl0yI-5WI0OjtZC5_JKBsm0Lw0qNXs-JosuOoKlTexoW3QcEwdzuHI9pO-dyuah6rX9XTLvHg6UFVsUGS8W7MZ4qVTAs6g5mJW70Lnj_-78AuNo2nJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مراد ویسی:
دیدم مردم به من گفتن عراقچی رو فالو کردی رفتم توییتر نگاه کنم ، دیدم نه تو توییتر ندارمش و رفتم تو اینستا دیدم اره عراقچی رو فالو دارم که احتمالا دستم خورده بود و انفالو کردم.
مرسی که بهم تذکر دادید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68795" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68794">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
فارس:
دقایقی قبل صدای سه انفجار حوالی سیریک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68794" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68789">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=lkK0Hdbdar_sQadGCjr3bnfjQevO9z_aI54JJbnhxqqizb1vMntRzKOfSob5l_te7xMhuzRddN-s_oPs5nKTMfgp99IUnzNB7tRqGiN7urxacVLTpAgFdpVW5GPoQFyId2WZQ6T1uzdFtjV8pN1dWho4fte-BwgWK1GnErYNQleyKZV7UaQjcdxnGy5DpzkH0FgIDhG3iL6k2feS0o0YjV920RnYP74fHPKghOEMv0rOYxcbUZ5vXxgjUTL1p1MOBT8LEsdC-aDYa5tHHRFNImA4yRwehFzi-sAYUj0tuEG3VomG7RAZbhdNDV_w6qoWK9NB8_3eUsMBpW3MgqVgRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=lkK0Hdbdar_sQadGCjr3bnfjQevO9z_aI54JJbnhxqqizb1vMntRzKOfSob5l_te7xMhuzRddN-s_oPs5nKTMfgp99IUnzNB7tRqGiN7urxacVLTpAgFdpVW5GPoQFyId2WZQ6T1uzdFtjV8pN1dWho4fte-BwgWK1GnErYNQleyKZV7UaQjcdxnGy5DpzkH0FgIDhG3iL6k2feS0o0YjV920RnYP74fHPKghOEMv0rOYxcbUZ5vXxgjUTL1p1MOBT8LEsdC-aDYa5tHHRFNImA4yRwehFzi-sAYUj0tuEG3VomG7RAZbhdNDV_w6qoWK9NB8_3eUsMBpW3MgqVgRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🚀
حملات شدید پهبادی اوکراین به روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68789" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68788">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=SKJ6SRMubJxzC3OiKc5lOb4tpmJbofrXxt79zu5cSf58pq9kQiJ05D7lBsPmm6h-Bvz2GQK9bQ3MTicqOBT35hSm8DcUxKu2iFQ21fsAK7B1Ak3MtRbtw_CfpeTDA-0AJZBMLWPisnIteLrZxxXhpRzAmCrR_J9Ns0EQMVuMkXDXKQDGD-emWgjU_p2OLFxovZX2YbI0W4zDOCjJomfVZNCTr9fYcF0XLlg8sCl8ADdEH2XEkLXi81hFBVPY40h7IwEAHXiNdQnkW6x0QkFwwHvFOEQ_FFzSbg5w_3ay2Ui2lyUBghb7Id71k7rbjLJc8gQeNIuRwEEuC3OmxMaXAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=SKJ6SRMubJxzC3OiKc5lOb4tpmJbofrXxt79zu5cSf58pq9kQiJ05D7lBsPmm6h-Bvz2GQK9bQ3MTicqOBT35hSm8DcUxKu2iFQ21fsAK7B1Ak3MtRbtw_CfpeTDA-0AJZBMLWPisnIteLrZxxXhpRzAmCrR_J9Ns0EQMVuMkXDXKQDGD-emWgjU_p2OLFxovZX2YbI0W4zDOCjJomfVZNCTr9fYcF0XLlg8sCl8ADdEH2XEkLXi81hFBVPY40h7IwEAHXiNdQnkW6x0QkFwwHvFOEQ_FFzSbg5w_3ay2Ui2lyUBghb7Id71k7rbjLJc8gQeNIuRwEEuC3OmxMaXAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی وزارت کشور :
عباس چرت میگه مشهد سقوط کرده بود، تو دی ماه من خودم مشهد بودم خبری نبود اون شب.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68788" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68787">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68787" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68786">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIKvsD4QRmlja5aQ47r36drmEyXpCwJT-7dy4XLfSWZc64y6Ox9IE0NMoKcsArKatpe5VAzhgZ2O7xFD-L_g2xwLFYRU36pIjdH9CPaAZ9yu0DdYz23V3eBcLbVEpqjySRixiZQqcoTgsoyNV5sqX8G-8Iy52_3geFnEHmicz7hq9ZuxmdgTINZJbxt8LnVcEGmBqgUr5RE-A_2vLGtBHZUea64HURtEfA2XutbZXipp_pPRwmrU0JfbDMZiw2bt6zOWF3qFnux1pZfCOzfQ_MTN9N5XCX3ehjVLejFdp4BtwWFrGZFLEUenmZYQVL1JBZsuH5l_p5nxONkI0hqx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68786" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68785">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=iRM2j2w2JYrjZDDXeNQOV5NGb0o1tvKQAKXZLwuMxretWWzItj35y6HFoTEJCjcZRkNsBy1ou3I2D9CT82PS3vfApdi7M8qvaemrlN8Xk4XgkK-_9IYtFpkfdS46xuVj6GQQHo-rS_9X2OxhILfrQJw-DU-vaE4j-07QFtnvRjSqC9vPYAYHmmpeoI-huhH66D0Y_-Y9GKrPIIqhix2LxKsybHuXTyE9oYxdEIuznfBCFa8f8bsVMW8R63erSUsdqk1kc9oUKi6ckzcGNCNVRDZIf2IAzhJC_dGoZpW4r8pd35TBqsVme6UZz4rWCSANFD4LCzDnV3TJYip57SqIwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=iRM2j2w2JYrjZDDXeNQOV5NGb0o1tvKQAKXZLwuMxretWWzItj35y6HFoTEJCjcZRkNsBy1ou3I2D9CT82PS3vfApdi7M8qvaemrlN8Xk4XgkK-_9IYtFpkfdS46xuVj6GQQHo-rS_9X2OxhILfrQJw-DU-vaE4j-07QFtnvRjSqC9vPYAYHmmpeoI-huhH66D0Y_-Y9GKrPIIqhix2LxKsybHuXTyE9oYxdEIuznfBCFa8f8bsVMW8R63erSUsdqk1kc9oUKi6ckzcGNCNVRDZIf2IAzhJC_dGoZpW4r8pd35TBqsVme6UZz4rWCSANFD4LCzDnV3TJYip57SqIwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این ویدیو از اینکه نشونه آدم پولدار چیه، اخیرا خیلی وایرال شده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68785" target="_blank">📅 12:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68784">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lajKP6hE0tcvxuBeY75Y9_KD43_zOP7ykZMe-Qmtxy2MowgEXmOKIZE0tn2YYC9d3dwMfNp_BAeUxMxzZW1u7uhxBIcA08ACrJ5H9wUnmHf5Z2DMCMsC2vQAxI3IBAbv9QeAjgTctfGZIG2oE-CeRXn6OjCf5yHf_6pOZj2pZHxwBZ6HBUUlKs12iJofbSmjjqOKbEVLKM4NVgjzd3bAPD4ZwegP2y8nQEV98Rvao4_aRDvWeM1QKcHN0m0ks5-k2N4J48fpH37hU8oKy3DybNtZUPStBwEurM4AzGJLmrgKCpDMbSaFagUDyjeNUYQsU03zojnhamSHgQa1gXnzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
شلیک موشک از کرمانشاه به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68784" target="_blank">📅 11:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68783">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=O-xJ1O4SadHfcQbq2C0e2ormrabQ9aYLxdLqBx7-SCqtwSYHyuY1PZzWfBJC96Fv8Jx00lImV4FXOmF2YGluhJ_5gRUMrk_ZVCfASv1L44pn4F53P1FojA8j9PO0G8sppjuedN_EoKPoF9oDq2U_PLSop2ct-HdROM_eX8exg_l1SufgqsKaFdkagL1m4Y-cSh4s5Yft_98VzL5GxDywD0yHlDcK_2AAHXm9YwZ49IdMaPUh1_N8QzC5RiTT20SelbcLq8m5oErvoP9oAXN5k_frqqJgm0--hteq_NqFBtvnD_Br-UTiDuwgoUxD7R0K7aEaHTq9mmiW0rea0Ciorw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=O-xJ1O4SadHfcQbq2C0e2ormrabQ9aYLxdLqBx7-SCqtwSYHyuY1PZzWfBJC96Fv8Jx00lImV4FXOmF2YGluhJ_5gRUMrk_ZVCfASv1L44pn4F53P1FojA8j9PO0G8sppjuedN_EoKPoF9oDq2U_PLSop2ct-HdROM_eX8exg_l1SufgqsKaFdkagL1m4Y-cSh4s5Yft_98VzL5GxDywD0yHlDcK_2AAHXm9YwZ49IdMaPUh1_N8QzC5RiTT20SelbcLq8m5oErvoP9oAXN5k_frqqJgm0--hteq_NqFBtvnD_Br-UTiDuwgoUxD7R0K7aEaHTq9mmiW0rea0Ciorw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
‌علی‌اکبر رائفی‌پور، ازحامیان جمهوری اسلامی:
با شناختی که از سپاه دارم اگر نظام سقوط کند، سپاه پاسداران موشک‌های خود را بر سر شهرهایی خالی خواهد کرد که به کنترل طرف مقابل درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68783" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68782">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=gMvu7i79ezNafiIe4GiuNumsUGdXlObR-ytbGhn324OyjQUkY5M3pWXKAvVQ8aEzdUWMMdzQmxSzjEvnj_371QKM-skyRO1Ctg2xogH5KMgvZI_v7qZn5yD0G0KX2OfWnIz2hVtHML3FoRrpRIzE2rJkAvF3GlWcYjgAE-1aYy7vkb7wQTrP1KOsuXp5UCJFi49oborAxR-AW6yh3D4hyXU8z7jw3RAWHG7PCQ-NUmdACAp29wV3Lk1_jDM780Ubl87Z1qRsz69UD23b9IfBemSetgQK8HGy0P4LM_SEbKWS_Ud0abO4QhdDaGEX9L5wzTsFh2qJAh6gG0qIW_zZWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=gMvu7i79ezNafiIe4GiuNumsUGdXlObR-ytbGhn324OyjQUkY5M3pWXKAvVQ8aEzdUWMMdzQmxSzjEvnj_371QKM-skyRO1Ctg2xogH5KMgvZI_v7qZn5yD0G0KX2OfWnIz2hVtHML3FoRrpRIzE2rJkAvF3GlWcYjgAE-1aYy7vkb7wQTrP1KOsuXp5UCJFi49oborAxR-AW6yh3D4hyXU8z7jw3RAWHG7PCQ-NUmdACAp29wV3Lk1_jDM780Ubl87Z1qRsz69UD23b9IfBemSetgQK8HGy0P4LM_SEbKWS_Ud0abO4QhdDaGEX9L5wzTsFh2qJAh6gG0qIW_zZWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⭕️
گفته میشه دیشب با وجود اینکه پدافندا توی تهران خیلی فعال بودن اما انفجاری گزارش نشده.
احتمالا دیشب بیشتر پهپادهای شناسایی آمریکا، مثل MQ-1C Gray Eagle و... تو آسمون تهران بودن و پدافندا هم سعی می‌کردن اونا رو بزنن.
احتمالاً مأموریت اصلی این پهپادا دیشب شناسایی بعضی مکان‌ها، مراکز نظامی، محل استقرار پدافندا، و... بوده و ممکنه که آمریکا درحال آماده کردن خودش برای دور جدیدی از جنگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68782" target="_blank">📅 10:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68781">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=DQdd9x66QxdJSwwbqoz4EdkvPb8NmNQIv0-BlQpxJ1JKc_lPsvD8SJP4w_D9BxoF6-KP1PzIfbaX6kyuuDA1XDOUZRWHXpwIjSDOHCTs9Jj6EuSYmhENaLQnzsL86R9KrmIyut1yEEtG3Bs2298Dp4a2RZKRoVeY7eopKAW-qfrmIdi-vbSAKlHjbUfFLsAA-Ye5LdOPvmlIJVpsDZuUC-ECO66e-SxVWCdxia4AkJN_2MVZBsYpaxjXKs2jmq8coAcLkUmB_6kzEv-0pxLT58MTnFCIdwc24NtxKPvoKkmB5Xz7cBkqV4zVe293PRSRFjBGct28T7bdVvNZgFgUkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=DQdd9x66QxdJSwwbqoz4EdkvPb8NmNQIv0-BlQpxJ1JKc_lPsvD8SJP4w_D9BxoF6-KP1PzIfbaX6kyuuDA1XDOUZRWHXpwIjSDOHCTs9Jj6EuSYmhENaLQnzsL86R9KrmIyut1yEEtG3Bs2298Dp4a2RZKRoVeY7eopKAW-qfrmIdi-vbSAKlHjbUfFLsAA-Ye5LdOPvmlIJVpsDZuUC-ECO66e-SxVWCdxia4AkJN_2MVZBsYpaxjXKs2jmq8coAcLkUmB_6kzEv-0pxLT58MTnFCIdwc24NtxKPvoKkmB5Xz7cBkqV4zVe293PRSRFjBGct28T7bdVvNZgFgUkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو روز قبل یه گونی آدم از مجری‌های صداوسیما ، اعضای پایداری و بعضی ورزشکارها در واکنش به کارزاری که راه افتاده بود، پا شدن رفتن جنوب که بگن ما از جنگ ترسی نداریم و این حرف‌ها؛
حالا کجا رفته باشن خوبه؟
بهمنشیر که تو نزدیکی کویته و 14 ساعت [1125 کیلومتر] با بندرعباس فاصله داره
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68781" target="_blank">📅 10:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68780">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=nKfGlM3l0iVN8eaMl7uxDkvDGg90sypCKeiGeKRohIetmgI4Z8EhMU7FELNpXfrIJOK1asICfKlqg9UgYwHjDmtzI4ZdXfcbtRDpttYi2FrgzttHasBOuJexf_JDnllEUJBeGstUxVqlG1ovnK45p6cs2IgjM3ZNTEvyShF0LrcZEwT30TYmcrgiETeHp6zgFyDoTWX8DiooZQy7-_3BM3U9phKCJslyklWLUWlTjL-YSY9ybAtvyIrRKGTDbJm0WGf9OZXzgQjWc8u9xJjcWrTBrhnGcROWnFM8izO60EKBdbBF0WDZ-sGKiQQutqsAPuZqNyU8p0cfaNBYiK4Xzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=nKfGlM3l0iVN8eaMl7uxDkvDGg90sypCKeiGeKRohIetmgI4Z8EhMU7FELNpXfrIJOK1asICfKlqg9UgYwHjDmtzI4ZdXfcbtRDpttYi2FrgzttHasBOuJexf_JDnllEUJBeGstUxVqlG1ovnK45p6cs2IgjM3ZNTEvyShF0LrcZEwT30TYmcrgiETeHp6zgFyDoTWX8DiooZQy7-_3BM3U9phKCJslyklWLUWlTjL-YSY9ybAtvyIrRKGTDbJm0WGf9OZXzgQjWc8u9xJjcWrTBrhnGcROWnFM8izO60EKBdbBF0WDZ-sGKiQQutqsAPuZqNyU8p0cfaNBYiK4Xzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
لحظه‌ای که عادل فردوسی‌پور تو لایو فوتبال 360 بغض و گریه کرد...
اپلیکیشن‌ و سایت فوتبال 360 به علت اینکه عادل و مهمون‌هاش از تیم ملی انتقاد کرده بودن، به درخواست قلعه نویی و باندش فیلتر و از دسترس خارج شده و مجبور شدن برنامه رو تو لایو اینستاگرام و یوتیوب اجرا کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68780" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68779">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=oEektPOnSPzP2nmMHYBJdsb7D3s7uAaO0Elae6eX-CcgW23oUoL7XXA1uSf1f_velZ496z7T8q8XH234yKGdnSv4IXkKqedmC4DDLLSFqqjaytuGbaflnhwJorsm-QAfqhhI-PKP8MIxPTmW7KJ987zaWZ6A7wtmv2H7rI97HscGd4DJMwwqJt-rdmfsI5BJlwDq7byhlK3AhCjkf18cj0owJILTgf2UG22Nsb1c2FDkSVVWID-3T5pJlldz4jwOpWjoqDFLJX1A8LWU2mii0Gk-Fcnc4vLVkb0zLdawlbyP3ixVzfWMlHJadq6b2tvBnaqpgC1Gl2iekuGVccVAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=oEektPOnSPzP2nmMHYBJdsb7D3s7uAaO0Elae6eX-CcgW23oUoL7XXA1uSf1f_velZ496z7T8q8XH234yKGdnSv4IXkKqedmC4DDLLSFqqjaytuGbaflnhwJorsm-QAfqhhI-PKP8MIxPTmW7KJ987zaWZ6A7wtmv2H7rI97HscGd4DJMwwqJt-rdmfsI5BJlwDq7byhlK3AhCjkf18cj0owJILTgf2UG22Nsb1c2FDkSVVWID-3T5pJlldz4jwOpWjoqDFLJX1A8LWU2mii0Gk-Fcnc4vLVkb0zLdawlbyP3ixVzfWMlHJadq6b2tvBnaqpgC1Gl2iekuGVccVAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
نظر مارکو روبیو درباره برجام (سپتامبر 2015)
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68779" target="_blank">📅 09:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68778">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
سنتکام: حملات امشب به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68778" target="_blank">📅 04:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68777">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68777" target="_blank">📅 03:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68775">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=h42A76HHoBq0xkvniSCECW9Rf-Jr1oHDYDBdmRqMaojON7IRHWHyuWF5-T2FgvrQHHQKKt51bwEtL_Gi6qpo-nMK5A57bjsAkG8dKcTxS8IMyUa-DRueuy3k56Sl_mtUZJK16RiYlqfcXv8_WKuUVqGc6MCcb5nRKKBeywLSNBHWusOsFLILwCi-69SCIKzYl23erPkjlyJ4QrUT5kYBZOphFveqXHe_zPJ-HsX3t28MUgjGk5hADH5fXubhlLj0wyFPGFkxwtPNdNgQ8JsqjPXbP3MllpvDZ9ThIHNSU3SiT7HV5zEUgh6LDFEWjWn_KyTPZFbTyUWRRbTtJ5Lq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=h42A76HHoBq0xkvniSCECW9Rf-Jr1oHDYDBdmRqMaojON7IRHWHyuWF5-T2FgvrQHHQKKt51bwEtL_Gi6qpo-nMK5A57bjsAkG8dKcTxS8IMyUa-DRueuy3k56Sl_mtUZJK16RiYlqfcXv8_WKuUVqGc6MCcb5nRKKBeywLSNBHWusOsFLILwCi-69SCIKzYl23erPkjlyJ4QrUT5kYBZOphFveqXHe_zPJ-HsX3t28MUgjGk5hADH5fXubhlLj0wyFPGFkxwtPNdNgQ8JsqjPXbP3MllpvDZ9ThIHNSU3SiT7HV5zEUgh6LDFEWjWn_KyTPZFbTyUWRRbTtJ5Lq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68775" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68774">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
❌
🌐
امشب ریزپرنده ها در تهران فعالیت داشتند، احتمال اختلالِ بیشتر در اینترنت وجود داره؛ پروکسی های پرسرعت زیر رو داشته باشید
https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68774" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68773">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در زنجان!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68773" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68772">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umNtMSwlVEViaQDk0B7-sd6RiVN9v9oWNb43DXyJySb8poZuC-E9th4GOJZRcvkRdnteDXCWAtf6t_on3AQp2-cMyHMiydXw2t-zPRccOQLFlSNwGVU-MOdOxQ1tTXvj6EMbYUNnCAhXj3qWgKQ-mzPgN4Q1Dss4zIJ-AXxsCt-jqWSv9UFDlBLzcXb-jDgSTkloyP4zDKRVNrfo1Ddsffv0JLf0KNaxAm8lNKw4uKEeEQfq_z7gv5NO1AqGoR_zrIWkfLEIaV3nsJ4j5dqCDutvFyuoyr6y2q3RdMq5NAmn4zJfPbArFKN4UfZvNV6EHmRJ696EoRU7BhF108ViZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68772" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68771">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت پدافند شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68771" target="_blank">📅 03:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68770">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون حملات شدید آمریکا به</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68770" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68769">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68769" target="_blank">📅 02:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68768">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تا این لحظه سنتکام هیچ خبری مبنی بر آغاز حملات رو اعلام نکرده! #hjAly‌</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68768" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68767">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بابت گزارش های لحظه‌ایتون عمیقاً سپاسگزارم، ولی حتما سعی کنید بعدش چنین گزارش هایی رو پاک کنید خدای‌نکرده جایی تو بازرسی گوشی توسط مزدوران ج.ا، مشکلی پیش نیاد
❤️
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68767" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68766">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
هشت انفجار در تبریز  @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68766" target="_blank">📅 02:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68765">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68765" target="_blank">📅 02:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68764">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه #hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68764" target="_blank">📅 02:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68763">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68763" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68762">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68762" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68761">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68761" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68760">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان  @News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68760" target="_blank">📅 02:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68759">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68759" target="_blank">📅 02:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68758">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در نارمک!!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68758" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68757">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68757" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68756">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ML9s1Cu0GoTreZKWiXTRGqFJOAnUFV1SJk3RLrRlFRQV9TbS_nG_NA5XHU9LOb5Z9G0dZDiSvcxpwS67-36cLpgdjT3rH0W7GUyW96sOYR5gKFXdu4cxMv49MvYz5N2aAhusmrWJIn1sdIilSQvf8zE4rMFd60VJPg_DQwoupJPYmrAIXmpCqmbnIf-jL0WsiMI8nHt5xfKwNfFcLcfhk8qoPIvR7hVsTLZ1NMsG-hVHEIROvGR-SToyXYV481o6UQTHnBosoJzK5Kqd-z66EyqLtzgXPIKHpQYZzm9KkLxnmlmgM0F0jgfSXTKEHj0YaiiLMkkPvdvxMzq-qH8bVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68756" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68755">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=hz3zx4SyucqTduMFs8exVYlBTWqYn6Ni8pGdYqyHWrCTSdtavzkgr9wJvkTzoadSE-b8scJmHr2l4yr26d7pTIj3Cs7fo8nIXaMCWcG_g0GsR0U2b060WCu0WWP1tIrvwBw-O2E6jNA68nfM-WB42tmKuOH7x5xq2mgUsGh69DKFD3zurGiTXATznD36Wy7J9UbB4FpfEugXEcPkeJFLde7PIYcbZ4h7f5NjfylmaFlauaYnSWffz5WNoEHqCIFrtXGmOHavFAJ0Eb32T9N5ZKz7xX29bwY-R69hm83enZJpApUzh3hPKu9JNYz8RGyohTLT6E5iTUG3qKFIBHZYZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=hz3zx4SyucqTduMFs8exVYlBTWqYn6Ni8pGdYqyHWrCTSdtavzkgr9wJvkTzoadSE-b8scJmHr2l4yr26d7pTIj3Cs7fo8nIXaMCWcG_g0GsR0U2b060WCu0WWP1tIrvwBw-O2E6jNA68nfM-WB42tmKuOH7x5xq2mgUsGh69DKFD3zurGiTXATznD36Wy7J9UbB4FpfEugXEcPkeJFLde7PIYcbZ4h7f5NjfylmaFlauaYnSWffz5WNoEHqCIFrtXGmOHavFAJ0Eb32T9N5ZKz7xX29bwY-R69hm83enZJpApUzh3hPKu9JNYz8RGyohTLT6E5iTUG3qKFIBHZYZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
پهباد‌های انتحاری در آسمان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68755" target="_blank">📅 01:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68754">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
جمهوری اسلامی به کویت حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68754" target="_blank">📅 01:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68753">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=gHVJjRChjuVudXkip9R32MpXg_NDL6LQjtpmcrvLsOTKy-lg8NWz8lHbvL0ypUqbB9Nqpo3-TIGu-pwW3-Jlko2IZRIVKwBjBzFv2ObqN_oCU8d9vpppSgQNbsiH7hCA-AWRHU8OtqPTNVgdevYEsBNEh3SaW0qlOqkctc7RvVN1kAFWWkAw0wh8o2PGJ67QGW1xqk9iY_b0nlngN-rbsHzbs7CyAevE-Tyk4W3oQQJshlcQQ4MkigmQ1au_nu2F4D7tCU3dP8-ykSlmKZnRrJBoeuBNY0iQx-xwP8yySalSA4-PTOfJDw4MvJNbaCmP49ZiMK4DcPsgrW89HQn4gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=gHVJjRChjuVudXkip9R32MpXg_NDL6LQjtpmcrvLsOTKy-lg8NWz8lHbvL0ypUqbB9Nqpo3-TIGu-pwW3-Jlko2IZRIVKwBjBzFv2ObqN_oCU8d9vpppSgQNbsiH7hCA-AWRHU8OtqPTNVgdevYEsBNEh3SaW0qlOqkctc7RvVN1kAFWWkAw0wh8o2PGJ67QGW1xqk9iY_b0nlngN-rbsHzbs7CyAevE-Tyk4W3oQQJshlcQQ4MkigmQ1au_nu2F4D7tCU3dP8-ykSlmKZnRrJBoeuBNY0iQx-xwP8yySalSA4-PTOfJDw4MvJNbaCmP49ZiMK4DcPsgrW89HQn4gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست وزیر جنگ آمریکا:
«رئیس‌جمهور ترامپ گفت که ما دوباره درگیر جنگ‌های احمقانه‌ای مانند [عراق و افغانستان] نمی‌شویم، و او این کار را نکرده است.
به همین دلیل است که ما سعی نکرده‌ایم جامعه ایران را از نو بسازیم، بلکه صرفاً، به شیوه‌ای واقع‌گرایانه و با شعار «اول آمریکا»، اطمینان حاصل کنیم که آنها هرگز به بمب هسته‌ای راه پیدا نمی‌کنند - کاملاً متوقف می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68753" target="_blank">📅 01:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68752">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=Q2RaAvwUtdTYhUTi6EllQ8z8Ad1rsrtayKVjV-qGcLBfEuhyBu-A0ZnxUgvAsWNgcx3kBm-AGI7vzhJVsu1NQHRAu_YP_POXj98ONvOtI-7fVPWn9zPP3i1hu4TOcvZPfHM16t31vsrw7lyVurBuqiwHjBslApPqioE0ArityZV7dv6V6Erce1XG_y14BcCabQZ_JOU1EvyfKTevVpy2VGo5pEklt9RRl_-rO51hKdRNkXab8oBTG8SIiQzgGi8wq7iD91NDEW3miuKqY7yet99QC-NaaspyflAMGBt38em04b6k5HYzLQlLUBhwnhPs04QT16zV4eRy9pU4cQXJ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=Q2RaAvwUtdTYhUTi6EllQ8z8Ad1rsrtayKVjV-qGcLBfEuhyBu-A0ZnxUgvAsWNgcx3kBm-AGI7vzhJVsu1NQHRAu_YP_POXj98ONvOtI-7fVPWn9zPP3i1hu4TOcvZPfHM16t31vsrw7lyVurBuqiwHjBslApPqioE0ArityZV7dv6V6Erce1XG_y14BcCabQZ_JOU1EvyfKTevVpy2VGo5pEklt9RRl_-rO51hKdRNkXab8oBTG8SIiQzgGi8wq7iD91NDEW3miuKqY7yet99QC-NaaspyflAMGBt38em04b6k5HYzLQlLUBhwnhPs04QT16zV4eRy9pU4cQXJ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاورمیانه هرشب
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68752" target="_blank">📅 00:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68751">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFd0QhOvPWFEiiTvV4M-fzfogu0Z4YsPuzB9X3JnMGZ7Vd2oLoU0w6Ir5sGzSpTsjjkUIJAXsT8pCBEXRJ1SVrb-sZ66Sx3LWdEhml7v0Uog28cXxGcuuRx2FiqmsNSp1ijmZLhGHZZQoP9CbF0HeNLiAcAqhwqJh-sLVfh6VnSue0GJmInv_iIKQMS0LsRggiNAlH03cBmreWHPICK2fuqQV8ylQoe07OLVZp0j52UgAYG1xuRtv-xg0DG_vIEcnnFvXXIk9Cs4QCAumb2ads1B8u24UZpPYdLuEo-AwvcQfe-r0ZcOz45mwRwniQXNSASTh5VDT1XjpSfIEV4jEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قرارگاه مرکزی خاتم‌الانبیا:
آمریکای جنایتکار مراکز هسته‌ای و تأسیسات حساس ایران رو تهدید کرده که ممکنه بهشون حمله کنه.
اعلام می‌کنیم اگه ارتش متجاوز و تروریست آمریکا چنین اقدامی انجام بده، این کار رو به‌عنوان گسترش جنگ در منطقه تلقی می‌کنیم و همه منافع آمریکا، همچنین منافع متحدها و حامیان این کشور یاغی و شرور، هدف حملات قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68751" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68750">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=hMqN-1I11jqq7JcaD7sPlA6m6yOu6Ow8GfE8Hoty8iuKkeHowdOUtwhB9YbMP57WSJ7kxEjCjbY6gWEcKEXzK8B5MrPBnwbnxFmUBu0PbU5-AxTsPuXTBCZSSzDXD-Z_xfsM5EinXI_PHrWKVJ4SkrrcPf6gOvqfQunCeUhqsxG3ReSwRQvIM1EioEYbV_0Mn-NZAcNGIZiQ0XDFKrxxfLVuTfuoUSu623LO3zs_BLttquiXKG18HrfMvPHKaXMM3KjMDQMd4IWNnBEX2Qy66CCRyOyo0Etg98J2dQlYyhemAExDUsvYI-XpbPBGNlWyeccO5Tya_x_SB77LMYmMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=hMqN-1I11jqq7JcaD7sPlA6m6yOu6Ow8GfE8Hoty8iuKkeHowdOUtwhB9YbMP57WSJ7kxEjCjbY6gWEcKEXzK8B5MrPBnwbnxFmUBu0PbU5-AxTsPuXTBCZSSzDXD-Z_xfsM5EinXI_PHrWKVJ4SkrrcPf6gOvqfQunCeUhqsxG3ReSwRQvIM1EioEYbV_0Mn-NZAcNGIZiQ0XDFKrxxfLVuTfuoUSu623LO3zs_BLttquiXKG18HrfMvPHKaXMM3KjMDQMd4IWNnBEX2Qy66CCRyOyo0Etg98J2dQlYyhemAExDUsvYI-XpbPBGNlWyeccO5Tya_x_SB77LMYmMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🎙
سناتور:
آیا ما توانایی نابود کردن هر آنچه را که در زیر «کوه پیک‌اکس» (Pickaxe Mountain) ایران قرار دارد، داریم؟
⏺
🇺🇸
هگست:
بسیاری از توانمندی‌های ما طبقه‌بندی‌شده (محرمانه) هستند، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای از این کره خاکی دسترسی پیدا کند، آن ارتش ایالات متحده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68750" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68749">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=MvlL5mGNzQdF4irrOJMved7dwrsofMescp9dA7DJbURyc8NuhDl7lRJlnyR6UUko67KfTpvLS0FZChP1Utf8kb--GBuoTzc-UTUR1vvnFzvJmG0f2Y86sh4eOEzAKAuzMJkylFb2OhiHbgu7pv4VdA7prTUv7IRk1HpZ-Qhx6sE64pJkBs3z04EGCDoUEF0msMgqlY42cGngsCoP8sRhYjj0OP0RadI3j1b8k4J4mAEOiN-mLjzuSlyTvrcvsYWQWUN3fLw2GsRR98QFva0IC1lr2vBJGEoEKgi6AwZYpLzZO8W0pZTIs2shcVRAU536jxwLLwwBtZCrJlfrTvbq6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=MvlL5mGNzQdF4irrOJMved7dwrsofMescp9dA7DJbURyc8NuhDl7lRJlnyR6UUko67KfTpvLS0FZChP1Utf8kb--GBuoTzc-UTUR1vvnFzvJmG0f2Y86sh4eOEzAKAuzMJkylFb2OhiHbgu7pv4VdA7prTUv7IRk1HpZ-Qhx6sE64pJkBs3z04EGCDoUEF0msMgqlY42cGngsCoP8sRhYjj0OP0RadI3j1b8k4J4mAEOiN-mLjzuSlyTvrcvsYWQWUN3fLw2GsRR98QFva0IC1lr2vBJGEoEKgi6AwZYpLzZO8W0pZTIs2shcVRAU536jxwLLwwBtZCrJlfrTvbq6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست:
محاصره ما دوباره اعمال شده و عملاً غیرقابل‌نفوذ است...
بسیاری از حملاتی که دریاسالار کوپر و سنتکام (CENTCOM) انجام می‌دهند، توانایی ایران برای رصد و پایش در تنگه هرمز را از بین می‌برد.
سناتور جان هوون: « هدف از این بودجه‌گذاری همین است... اطمینان از اینکه ما و متحدانمان می‌توانیم در تنگه هرمز عملیات انجام دهیم... و اینکه ایران را وادار کنیم تا در راستای اهداف ما عمل کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68749" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68748">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=g-W_aDj93n9P63t5-7bq5DpcxQJ1DfSGv4BphQZxoriwPoJbytEifcdaB1wUDQuKSVBmZ9UZO7UK2RBAWCkPrYQm_5SlfFRXDHU1E73KyKAvPF_r-7sKQlQ0Gy2Z5JoFqUof2MK5Rr-tHJ4TQ6iGs3kCPMaDoMh4gHGPnRNqHt_If3mXPhZic2IiVMzxBnwRBg04wma3Jsc7tseDPk_gmSHwtPD-_X1lvoRy_iZS9ip3W0Zk2PI3SGlpi9QzgQRz1DHJKXs3PTL6RAVkJUzScYeTJeWIeel9mq-pHsGQvk5YJUxKAQmXCGsFgk0TJo0QRCt8mZzY3WGlG2n365SYCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=g-W_aDj93n9P63t5-7bq5DpcxQJ1DfSGv4BphQZxoriwPoJbytEifcdaB1wUDQuKSVBmZ9UZO7UK2RBAWCkPrYQm_5SlfFRXDHU1E73KyKAvPF_r-7sKQlQ0Gy2Z5JoFqUof2MK5Rr-tHJ4TQ6iGs3kCPMaDoMh4gHGPnRNqHt_If3mXPhZic2IiVMzxBnwRBg04wma3Jsc7tseDPk_gmSHwtPD-_X1lvoRy_iZS9ip3W0Zk2PI3SGlpi9QzgQRz1DHJKXs3PTL6RAVkJUzScYeTJeWIeel9mq-pHsGQvk5YJUxKAQmXCGsFgk0TJo0QRCt8mZzY3WGlG2n365SYCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
من در مقابل یک کمیته نشسته‌ام که می‌خواهد درباره پیروزی در جنگی صحبت کند که چهار سال است ادامه دارد، و درباره شکست استراتژیک درگیری‌ای صحبت می‌کند که چهار ماه است ادامه دارد، تا از دستیابی ایران به بمب هسته‌ای جلوگیری شود.
امیدوارم که در این شهر، دیدگاهی وجود داشته باشد نسبت به اهمیت تاریخی اقداماتی که رئیس‌جمهور ترامپ در حال انجام آن‌ها است.
آیا شما می‌خواهید که گروه‌های افراطی اسلامی به بمب هسته‌ای دست پیدا کنند...؟"
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68748" target="_blank">📅 00:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68747">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=K5e0y095I35QUfmfMZR0IP-p09q7iSrllzaRAQkJgJVJhrFedm0Z1ZvOe0OVpGdvNM1UUaVh0ZT4ts79-otxL6rzHR-YA2g-MNLumLM5FYpAPBySQ0AQhot-aSCmDrfLWOMgTjZNi4QIPHabU0b3M-rIHLdW4RcZxU7jGZ4OKhVwX6kkTO8Ko3E1zqYRj0fisKvvNs3MFYEyGC9Y8OzVxvmKkplKtjcm8JO475Q2N2yMZ9nokxAqfjQkwNGeW25xZYkdAs6UhNt-RB8R_IVSWD8kU4izuGFa9yaXJTLPEF1cq8TIFi9jsdbJgAFXsJrt2CEZN-oOJekNA6jorE89wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=K5e0y095I35QUfmfMZR0IP-p09q7iSrllzaRAQkJgJVJhrFedm0Z1ZvOe0OVpGdvNM1UUaVh0ZT4ts79-otxL6rzHR-YA2g-MNLumLM5FYpAPBySQ0AQhot-aSCmDrfLWOMgTjZNi4QIPHabU0b3M-rIHLdW4RcZxU7jGZ4OKhVwX6kkTO8Ko3E1zqYRj0fisKvvNs3MFYEyGC9Y8OzVxvmKkplKtjcm8JO475Q2N2yMZ9nokxAqfjQkwNGeW25xZYkdAs6UhNt-RB8R_IVSWD8kU4izuGFa9yaXJTLPEF1cq8TIFi9jsdbJgAFXsJrt2CEZN-oOJekNA6jorE89wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست درباره ایران:
ایران از نظر نظامی در ضعیف‌ترین وضعیت تاریخ خود قرار دارد...
بی‌شک اذعان می‌کنم که آن‌ها همچنان از توانمندی‌هایی برخوردارند، اما حجم خساراتی که ما طی این رشته عملیات به آن‌ها وارد کرده‌ایم، آن‌ها را در بدترین موقعیت تاریخشان قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68747" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68746">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=fRiyJqswvmeHaj2ixuGweYXdQjeL9DNjZDAm8Pah8NG_bZ3SNyhluad5Jfj72o1auzTTBoZygrU_SkWlwM5AaGvD1c95yorbKZ8eP5eqmov5LbBJAq0e6-IaRRWkwrw_U99gMWlPaL0-iuMx0RoKOe-IuAXGwDXUXIdaoStFbFMjyd5w1e6UEC2zTjtqLGRYcx_6-u-2yvYISjtn3_BUKaTrb8ISeIT_dRtOPALlR71e8ZXM09SbZF_XNa5XGsNeNsmJFSh5pEVQxk58fw-7_Z0616PKZtUSyIZRzJshFoGVm18GmZzugpcoM098rBf3HYw3CAB_oaw0JN896uhhrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=fRiyJqswvmeHaj2ixuGweYXdQjeL9DNjZDAm8Pah8NG_bZ3SNyhluad5Jfj72o1auzTTBoZygrU_SkWlwM5AaGvD1c95yorbKZ8eP5eqmov5LbBJAq0e6-IaRRWkwrw_U99gMWlPaL0-iuMx0RoKOe-IuAXGwDXUXIdaoStFbFMjyd5w1e6UEC2zTjtqLGRYcx_6-u-2yvYISjtn3_BUKaTrb8ISeIT_dRtOPALlR71e8ZXM09SbZF_XNa5XGsNeNsmJFSh5pEVQxk58fw-7_Z0616PKZtUSyIZRzJshFoGVm18GmZzugpcoM098rBf3HYw3CAB_oaw0JN896uhhrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت
هگست:
این درخواست تکمیلی دو هدف را دنبال می‌کند: حفظ آمادگی نظامی ما برای پاسخگویی به نیازهای جدید امسال؛ و تسریع قابلیت‌های حیاتی برای جایگزینی و تقویت قابلیت‌هایی که در شرایط اضطراری استفاده کرده‌ایم...
در حوزه آمادگی، ما ۲۱ میلیارد دلار درخواست کردیم. این مبلغ برای تأمین حقوق نظامیان، جایگزینی تجهیزات مورد استفاده در عملیات‌های اخیر، حفظ نیروهای مستقر در خط مقدم و افزایش قدرت نهایی پرسنل در عین تثبیت کمبود سوخت حیاتی ماموریت و پشتیبانی از گارد ملی هزینه خواهد شد.
در حوزه قابلیت‌ها، ما ۴۶ میلیارد دلار درخواست کردیم. این بودجه خطوط تولید را گسترش داده و تحویل مهمات مورد نیاز را تسریع می‌کند. ما در مورد موتورهای موشک سوخت جامد، JADM، موشک‌های مافوق صوت و قابلیت‌های ضد پهپاد صحبت می‌کنیم. علاوه بر این، ما از این سرمایه‌گذاری برای تضمین تسلط دیجیتال و فضایی، از جمله شبکه‌های ماهواره‌ای انعطاف‌پذیر، استفاده خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68746" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
