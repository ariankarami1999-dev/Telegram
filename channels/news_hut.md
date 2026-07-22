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
<img src="https://cdn4.telesco.pe/file/L_VAiYb43UDuISIPCzrI39F4AVys2QzoZm7apbs3tVBm7C1w3qk4KlDmbgWgIsJpJof5Aljf1UaxjvloHUg_ew5xB44OFqkVYohS65317mPuyu1phmVb_510ke6iCVLBfdtQmuTKPIexfW4uERORtp7lXUPi1M29njeiqt7YWt_DR4DhLPui4hhAFRpCUlihEImOCZrr8leDR4udRBdkSZGGMOBxwRNRR7I1eKr_3_WvrMyvzt5mVRQDxJmE3meG9_RkLC-Y6KlVi2f_CW15Jm3tlVsKnA720RntwIi9CYB5JH5CYh8w38rj98NwXredkKBmaL_TPC6IdeTbr6BZ-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 154K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 21:16:59</div>
<hr>

<div class="tg-post" id="msg-68816">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhh2P1g2To555iChL4dtdwa72oF9Vvq1NuhAJ5hu7ZjkcWc-mnLXR6szuRJhTHHk0HNgiroxvsrJZ7DslUW6GiqP6Acc7zAY8-NYmg8V1qM9vBPh5Vobfm_Ap4_SCK-bWnSymxvEPUytFwKLwnjp6u5h2nOBouGABJ8IHZNRP-VsRNHo1VEFQyYZdoMsL9Hz0rQ41DCfhEeWUN0SPgqUrRp5xJazhIKVMJPOg1RbiwkWvl7sKZvEGpq-cHwanAZeNjyN74dDkrwfynQLTkbAWsKlelj1mRy9o1uB5De-JaHTQJbfZVty4dpQDPcofoEOQYYow--bLXaAJzkwxWn-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت.
اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است.
بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/news_hut/68816" target="_blank">📅 21:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68815">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA01D8uzQ1YgbxtZ5cTj5gDULEM555B0oi4gxYYPtMzL4xVXDeyyxbl8Z5J8BvQecElmuFY-m9iNm8Kfv0r9MzHj4BnqEwsdpbW2WieS6N8xFI_tEbVmpy0wrTZuEguCMED2gtoeKPjPsIhZCrH8eY1PCmMIqQj4-0MGgFvV3EL06JnH_3YPvLbKUTMW94AYWRK1qmEG7cq5ZWhy1kjZt6azvBMjEwHalShPtMnfKLBZxgpkSdAW1SPcM9dnBbSNVMinRORsbP5c1igZv-hzotUfuH7iUrmI_04Xr4op6oJReZZCudMWnbOiWcvEUQcrFBVP6kjEc6ezw_rF5mNFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال:
رئیس‌جمهور ترامپ به‌تازگی اعلام کرد که پس از کشته شدن نیروهای آمریکایی، به «سنتکام» (فرماندهی مرکزی ایالات متحده) دستور داده است تا «درهای جهنم» را به روی ایران بگشاید.
@News_Hut</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/news_hut/68815" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68814">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/news_hut/68814" target="_blank">📅 20:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68813">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7YwCvMmYmxmt_NDTvOkfT3KeiazKoeZs2xlolK45G6-c5-iE-LqUgxXcAlkpUDJibtI-qR8pUh0nPrBWsG3Tn2oJocveCm6cLt5DsufgAm-6tb4AjbVLj5Xd6wImob-8BL8TE0Gdi9VZvBzVbnAJF-k4tiKs0K-pCAgca4Z6Mvsg1pY1ZMYSUzBoSZ2uVM62YkKdSnD-7kPS6YWoJ8bWVDOph9FGaA30Wd2MN5KGl8OAuWrU7pJQXqjtOV-iI0AnbvX0KY8pYhkSV0mlsVHH0NFoMk3JiWmxYPmAhdnjUc5v8ZgumCinnVyZIvNZfZPfC565g9jFY_93Uj7ceO6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/68813" target="_blank">📅 20:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68812">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJJuU-s11crr5TX7rTUMtihwPFy5sB0d6UOaTn9cn4SAZDKgXTeP6byiWSTHBk-sW6Ex7iakTBh_g1he4-lKr9y7bMkrAP5op96T6Czk_yTLVPOscuZIhZ_N-L3h6XLoqZ048wTQM6Cg6u3DWNR-QmwDCgSpkcwhDIUwj1jUcY3BM1W9HZqHgHRSFWmbpYA7UfYp-oH6eeMtKnOxN4X_V_kAYCP0LKx7PfFbYUA2ScND1d3EynIa0dlQcR2PJUwpTWEvHymL5qlm3X4mEJnWZvxa2gPjXIOzStbDbBx3JEb9AVQ3luiC-ma3gfa0X4AejJ-YnLeOlpLCEq8ZW4yD5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یکی از حملاتی که شب گذشته توسط سنتکام در جریان یازدهمین شب متوالی عملیات علیه ایران اعلام شد، بخش نظامی فرودگاه بوشهر را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/68812" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68811">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGNczzS8NpQb1ezGozI1BCdJlbvvkAVYdIhr_v7jBNU-3NZJm2nIpeLDPUq4OjlXkGCcvQ97v0cs6SvkVFyOhs-HFoMSWCjrbprk4wLaqZvNTzUIFauqx1uHtFLFscicOKl3hmftYoi_fj2H4iMHexmlPBg0k-6k89o-wB2bm9iP7p6axl3M7xGZJ56woEYaNk13MzjbSPHRXSl5KcAyI4sHnyZz7UobSmMr1sMB0O0LYNAvalCL_Acm6yFQR4lgHAyGbp_XMW0YBfjALOmQdLJDYfiOiJwL-_i18j7lfB4gVxZU8ffPWDw5yklebD6ybrh-ekH7qZ6knFVi9pFM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
قیمت نفت خام برنت به 93.14 دلار به ازای هر بشکه افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/68811" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68810">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuhNN_BoqmZBqOVQ1BxPPGVXlIBEATFcJtDxNJNYJvV2zjpYFv_EWxU3W7S3UI34BYJnEUD8TlpVDmbgGIesmSiKqDMiONBQCUbi3HHMqUL4SLRN_SH_wz3dKbQ90vPpFwLaskQemnlFmrT5L4sesT5T7ldrWmRMdBuZSew8comSY8mfLEyQRFV0e-Fsg0_DXrZo0FXs701apynJtly0DWzLgflo0MG5rrqpgER4GAs4tiUmSVJlrZ7qcaIlzz3PF2qN0NW3kjk4OSaDZnW9b4zP9aRpAOxfJ9DJWU3Vuf08wSqTiNBw9hWRyYiNN0IZOcaEp3MxB7BQfe20z0Ui4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/68810" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68809">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=fW0FmXWiycKFTyVJCE_LA8IgXwECJ_BuHNGLtDO0uMFz1EWdqOm-7R5w4sa8TQe2tpYHnbEcqGe6HE6T2JzDCzPDMjmihVNXDpifsBKp0fnIRDihkRN8zn9V67VcpnhZINpNQ91EYrH8vx9wsZ_kjtGQYTLIjSNdZlkDA01Ml6MOubwq_36-4DRUQSyvaBydmTnhDvhK6dgPPKTQ0cEyDNc2rtvAbqpDCWTuVcEVLWbxOpqgby2obTeKZ4r5kCtHNxxXe4ND_7I03v5lPdg0gj9kF1EqW4PTPVfJeI2Z9GQ26jVth1D50Q7eB4uEJT0cJ76es7N1eJUWYhGoC3gTaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=fW0FmXWiycKFTyVJCE_LA8IgXwECJ_BuHNGLtDO0uMFz1EWdqOm-7R5w4sa8TQe2tpYHnbEcqGe6HE6T2JzDCzPDMjmihVNXDpifsBKp0fnIRDihkRN8zn9V67VcpnhZINpNQ91EYrH8vx9wsZ_kjtGQYTLIjSNdZlkDA01Ml6MOubwq_36-4DRUQSyvaBydmTnhDvhK6dgPPKTQ0cEyDNc2rtvAbqpDCWTuVcEVLWbxOpqgby2obTeKZ4r5kCtHNxxXe4ND_7I03v5lPdg0gj9kF1EqW4PTPVfJeI2Z9GQ26jVth1D50Q7eB4uEJT0cJ76es7N1eJUWYhGoC3gTaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس انقد کد کد کرد که
کص
از دهنش پرید بیرون
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/68809" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68808">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=qNDcztIAI0CSCQViRZCVu_wpWTQYPq2ij78Pw5IISCs9eU7rhPxgjQ8zD46rZeYZfeFq8nTx9ebTnXXeMOX7aqUtpemtQ-NHgOvy-rPfO4g3SnTJmZc2QCpGRhHt_Q3wzNUpYfh1oJvi_gwPsRT7lDVj8sjMBtqOMxHtKKBYbNi3WuctYPp3Z1uzAd4AU5wzppfvyXRImDaZPDvyzTZ_KGpsAtdsXpB_BV8X122Ausz1QCSdTS4M66YLoM5ho7dndoOIesvFW6TJCEhfsGSsToJcTIBCDYo0wt-XH8GSWPlt-uDia0Jt5xoo_bU4tGXMxo72I87GNEKqLwi6ZM5Jbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=qNDcztIAI0CSCQViRZCVu_wpWTQYPq2ij78Pw5IISCs9eU7rhPxgjQ8zD46rZeYZfeFq8nTx9ebTnXXeMOX7aqUtpemtQ-NHgOvy-rPfO4g3SnTJmZc2QCpGRhHt_Q3wzNUpYfh1oJvi_gwPsRT7lDVj8sjMBtqOMxHtKKBYbNi3WuctYPp3Z1uzAd4AU5wzppfvyXRImDaZPDvyzTZ_KGpsAtdsXpB_BV8X122Ausz1QCSdTS4M66YLoM5ho7dndoOIesvFW6TJCEhfsGSsToJcTIBCDYo0wt-XH8GSWPlt-uDia0Jt5xoo_bU4tGXMxo72I87GNEKqLwi6ZM5Jbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
عراقچی: ما به هیچ عنوان غافلگیر نشدیم!
واسه همه سناریوها برنامه داشتیم و کد بندی شده بودن.
سناریو آخر این بود که رهبری (علی خامنه‌ای) رو بزنن که کدش 110 بود.
تو جلسات کسی دلش نمیومد درباره این کد صحبت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68808" target="_blank">📅 18:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68807">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
یک منبع نظامی به تسنیم:
هر پل و نیروگاهی از ایران هدف قرار بگیرد چندین زیرساخت و تاسیسات انرژی منطقه را می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/68807" target="_blank">📅 18:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68806">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:  بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.  @News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/68806" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68805">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=IdlMMBKdVgbyOG8BbHlQibnJ7BnsdJIHaVJYhNsBQLbDLNf1Cq3ED70U9r_u-TQhaZLv09WWCZRtWsDqqOiZukbqkGSLPwbY6gsc9-_iYQ9PP3pf3HtWTXT6V6nHgQnGMKW4SmVfFVx_hv2K6IJ98vsLL9OYnq0PuZsBxtgpgKnAvlXUi67r35BiY0NxlvKgGzUIeLa2CH8Bl5QOZ_qxjxoxiNEgpdH27mtSVPWM3nnNdo4mq2ZhFdQrCH186d0Fhnqq6fOrwUrk3kIGpTlnWCaiuMSIpoHweGnFKnihEksGyaKSOcRv2w91fI2of3m0b146KQYju_euPuOW8Ct1lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=IdlMMBKdVgbyOG8BbHlQibnJ7BnsdJIHaVJYhNsBQLbDLNf1Cq3ED70U9r_u-TQhaZLv09WWCZRtWsDqqOiZukbqkGSLPwbY6gsc9-_iYQ9PP3pf3HtWTXT6V6nHgQnGMKW4SmVfFVx_hv2K6IJ98vsLL9OYnq0PuZsBxtgpgKnAvlXUi67r35BiY0NxlvKgGzUIeLa2CH8Bl5QOZ_qxjxoxiNEgpdH27mtSVPWM3nnNdo4mq2ZhFdQrCH186d0Fhnqq6fOrwUrk3kIGpTlnWCaiuMSIpoHweGnFKnihEksGyaKSOcRv2w91fI2of3m0b146KQYju_euPuOW8Ct1lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
دونالد ترامپ درباره ایران:
«آن‌ها بهای سنگینی خواهند پرداخت. آن‌ها در حال نابود شدن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/68805" target="_blank">📅 17:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68804">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRKDgQG7yrNvq8T61GwBwB1PXd8qJOO3WF0LFMvDLDIp9rfEHt2JL16p_h-nagSWYbyVNnkhDLUt2oSRfQRKFI-8hG3UaUQCmnR4X1A0S3BVzoP9MsYxrZhtjwXFLk8WP8QfHob-sbRxAafKtjRmHBg4VPMrSxp5_l5Zy3MUDZsdt_-07NbJhEimXZ5VTnQoD_jMEI9DkTD3_9owLDf5wxg0cgmS0-28vCxzZ9PtKy9CjjWE8-isBOV5vtLJFzrOop0EsydEkxdnWfzuoPvhBF_nk7MyVGC6uzB8A9YSYdAQ3rJroIra0gsNHd6kUUk44uVp9pu5_LNoat0ZIlAQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68804" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68803">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSyYem9zgZQJE0NwiXY__CFPfgyn17MvcolECKZJQrwXxl-bV6BEBARPhMJUJ-_Ie_lR11U9B0nn4UdqrdnlV3kUwJDGUwe7NDIewDEgX7lEqwWO5FIaqz9YeHiSfS2wHBB-AvIpsH0D1I9mlTdwf_yYNxaEWTjjYiCTlvghdmZfVlFL4OHUaYPH3rxR0la6RmGf5xni2DN_em0PNkgVD0zCVa7fupkN53n3MAiquTrGvJmqZYffC08wfMsgBjouCD_1i-enE3ODY-xyvjKCt8qtoMSTBANHAlFo2B_lsEbla_Z45LSISK7BsQorQIXecdBSnSqT7ADqAauynpoTJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه
حتی اگه نزدیک تهران یا داخل خود تهران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68803" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68802">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=bM6YgE60k6qbm-kDBRM6wgaqiyn6xv2pWrniGGI2UfDb4Jkl-1dDul_1rZyTVYeOMtgfI41lOKxfQV3RYQhE90MFn93k88Mp04sPK77YXurm5uHDS3OmPIAJTie7Oio_oR_xI9Pt5UCXWtjPOXJqP0MjIHSPD-1a0wQ-6gUaq_kVbpDDkBD44FJXZg4-OM11hFXaSnfOvm_9KUrdKKbORYx0Gga3VLXPV1k2UXr8DTMm2wqdx2L9wL-yffXWxsWd4LJoJYZkzCGfNmmhpedB2fUDId6byHyYZjHBXHvhOKd0HiOcUYsyycm5LFVbQOpLqjKs91nGUYffYNxv1zFFNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=bM6YgE60k6qbm-kDBRM6wgaqiyn6xv2pWrniGGI2UfDb4Jkl-1dDul_1rZyTVYeOMtgfI41lOKxfQV3RYQhE90MFn93k88Mp04sPK77YXurm5uHDS3OmPIAJTie7Oio_oR_xI9Pt5UCXWtjPOXJqP0MjIHSPD-1a0wQ-6gUaq_kVbpDDkBD44FJXZg4-OM11hFXaSnfOvm_9KUrdKKbORYx0Gga3VLXPV1k2UXr8DTMm2wqdx2L9wL-yffXWxsWd4LJoJYZkzCGfNmmhpedB2fUDId6byHyYZjHBXHvhOKd0HiOcUYsyycm5LFVbQOpLqjKs91nGUYffYNxv1zFFNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مقایسه جمعیت ۷۲ هزار نفری در کنسرت فردی مرکوری در ومبلی لندن (تیر 1364)
و جمعیت مراسم نماز و تشییع علی خامنه‌ای در مصلی تهران (تیر 1405)
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68802" target="_blank">📅 16:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68801">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⏸
ویدیو وایرال شده از گریه های یک دختره بخاطر مردن سگش
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68801" target="_blank">📅 16:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68800">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏
🇮🇷
سپاه پاسداران:
«اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68800" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68799">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfPi8-2vHXL_Hy1Rx8B2gR4Annc3Q9geBA1CONXFF1eakcGpp4sXfnLgQpMCH58MtrH1J8clR752c7WTIS7IgjzSTvqWaWr3XOWdB8RiH8EYaTUq9uL54rrVgKnuAYn8R_x0WO4ID0JA6Q7vm7MFB3eSmVBTcBJ7y1TkTSikt2N1QcermAs9usLRntcibi7QAMQh459uiF1mfiDi4yLDZzhmK4dLc6N2BZj16LvEoIfyldPpe5xaYZPt43uMprIlChBSTV6GZDFazg3NGLAQmJwUNY7AvKCmyjqjuAIZF8sraiSxRyd-ubamCVe-OFXdwXGP8WHqlGI_pEo3xBLOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آژیر خطر در عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68799" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68798">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران به بحرین و عربستان سعودی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68798" target="_blank">📅 15:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68797">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=Cyc13MIDvUdrH7BgynyC9X13UgbEDAxHPV9Z6JGvuvnpqA-GnXKzNzrOOkxatU5dGtvKxY_GVMGQSbRFsvRyKrP1_jfkat58tY32niTw7l60SJDpjBsmpcfHuSfHJJxsckAlm9URTQB2AqJROOejCFdZQ55sAnCqE6oLpY_1fl1Y1OcPDw3R0uHMuqlLuLrZK0AUZ-XnxAhr-MNPIGhPz_mTKYD6iRbisoP-_bZunK0v6DYMKgVKrEM0t2_Se36y4krAeea0W2nmvWPdfDCnPtla--cUtqQ-xRaLb_4c-FqQGsdt0_cQXM3C2GsmLgTVpnUEPDVygFdngUp-rP1QSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=Cyc13MIDvUdrH7BgynyC9X13UgbEDAxHPV9Z6JGvuvnpqA-GnXKzNzrOOkxatU5dGtvKxY_GVMGQSbRFsvRyKrP1_jfkat58tY32niTw7l60SJDpjBsmpcfHuSfHJJxsckAlm9URTQB2AqJROOejCFdZQ55sAnCqE6oLpY_1fl1Y1OcPDw3R0uHMuqlLuLrZK0AUZ-XnxAhr-MNPIGhPz_mTKYD6iRbisoP-_bZunK0v6DYMKgVKrEM0t2_Se36y4krAeea0W2nmvWPdfDCnPtla--cUtqQ-xRaLb_4c-FqQGsdt0_cQXM3C2GsmLgTVpnUEPDVygFdngUp-rP1QSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68797" target="_blank">📅 14:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68796">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=Hk7s9KNwWOro9L9ShzDgUw1SBdrd4tTiewDf0-S55_JJnQDAT9CPJ_FkXUi50ZwqK5zaWI_Kwm8ZtWs3JA0IT-9Kt1vmpVjwoJpKvj5cvuHlYiH5A8j2Nc5Mdujg2vYRl7Wxk-BKvyxjXRrDoldUFnRv-oQkyAs5nVgmSYyQVVLeHIo_ojI_MUyl_LnfCvxWO-u6DpQ___rdBCCijAkf9EhxXhq3m6o5T4h4V5Kj_eQeBWdhscS9CAE2eRioociBw3JBNaaD81kZElbZti9rto6bMEWXdcMDVYwx0Ew7pRP2RRwVCkcvg6BDA_MucS5Xk-mklpDKr44_-FrEfxJaSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=Hk7s9KNwWOro9L9ShzDgUw1SBdrd4tTiewDf0-S55_JJnQDAT9CPJ_FkXUi50ZwqK5zaWI_Kwm8ZtWs3JA0IT-9Kt1vmpVjwoJpKvj5cvuHlYiH5A8j2Nc5Mdujg2vYRl7Wxk-BKvyxjXRrDoldUFnRv-oQkyAs5nVgmSYyQVVLeHIo_ojI_MUyl_LnfCvxWO-u6DpQ___rdBCCijAkf9EhxXhq3m6o5T4h4V5Kj_eQeBWdhscS9CAE2eRioociBw3JBNaaD81kZElbZti9rto6bMEWXdcMDVYwx0Ew7pRP2RRwVCkcvg6BDA_MucS5Xk-mklpDKr44_-FrEfxJaSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68796" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68795">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=OjPUPP9WJpYLzmhs8jZhrTf7hB2LMFWPY8ckJtqCgfMDdm99eObJ5zRwfEX_F0E7PBetDSKyfurJL3LPXZbGxS2LDfB4ZIv5UFzj965MSxhKVuBa-xCsrnm3QQvCkhr85eRcOgKT9RXis17-ai_99waVxxNz-rO7C6SeMV4KrBa3UiqzJhElTXAVwpcFKJKnANI6JWDkvFaBGjzfLvUqWJwAaPgIiKrP1G2V6p6jNhr-pheyYSGC0xTTBzzyG2MktvwMGbrp2kQX_e70AEFwgVeMAfoVwm1ZAq1CKoCbQ_MXWUBt65djZhDh0nTWvedbzGp-EmZZd2SPt6DJ7HbtJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=OjPUPP9WJpYLzmhs8jZhrTf7hB2LMFWPY8ckJtqCgfMDdm99eObJ5zRwfEX_F0E7PBetDSKyfurJL3LPXZbGxS2LDfB4ZIv5UFzj965MSxhKVuBa-xCsrnm3QQvCkhr85eRcOgKT9RXis17-ai_99waVxxNz-rO7C6SeMV4KrBa3UiqzJhElTXAVwpcFKJKnANI6JWDkvFaBGjzfLvUqWJwAaPgIiKrP1G2V6p6jNhr-pheyYSGC0xTTBzzyG2MktvwMGbrp2kQX_e70AEFwgVeMAfoVwm1ZAq1CKoCbQ_MXWUBt65djZhDh0nTWvedbzGp-EmZZd2SPt6DJ7HbtJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مراد ویسی:
دیدم مردم به من گفتن عراقچی رو فالو کردی رفتم توییتر نگاه کنم ، دیدم نه تو توییتر ندارمش و رفتم تو اینستا دیدم اره عراقچی رو فالو دارم که احتمالا دستم خورده بود و انفالو کردم.
مرسی که بهم تذکر دادید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68795" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68794">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
فارس:
دقایقی قبل صدای سه انفجار حوالی سیریک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68794" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68789">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=kH8Rjewd4tqZeOPqUhEzYsIeOH67hnZl246a0WIMT72IQb3vMPqBv0yTM4FWly4x3vXZ1Qkb1ULUuJKzCRXFEq1dI26pFTbw3BiWg-CKz9lRTO8HZi1YoWqCLBtzCEYa0bwEJ5u_UP7nymHYuTtkvJQLstcGnDcKqYhj2-3mfGURyzic7K2ld1CWGcoen6r-bj4O55DEFDNDyNs4720PGy_AH7E6GV6uQoxNIOFsbn28NgkdpQCb1uI3oUMfMoTTZsb58fLauQ-4eWqD8VSfA8_DbNXDtEluJbalpOBUsoCj_BPGUPxr79wmATk_AyXmFw6vFxaShcoBH4jqUA5VVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=kH8Rjewd4tqZeOPqUhEzYsIeOH67hnZl246a0WIMT72IQb3vMPqBv0yTM4FWly4x3vXZ1Qkb1ULUuJKzCRXFEq1dI26pFTbw3BiWg-CKz9lRTO8HZi1YoWqCLBtzCEYa0bwEJ5u_UP7nymHYuTtkvJQLstcGnDcKqYhj2-3mfGURyzic7K2ld1CWGcoen6r-bj4O55DEFDNDyNs4720PGy_AH7E6GV6uQoxNIOFsbn28NgkdpQCb1uI3oUMfMoTTZsb58fLauQ-4eWqD8VSfA8_DbNXDtEluJbalpOBUsoCj_BPGUPxr79wmATk_AyXmFw6vFxaShcoBH4jqUA5VVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🚀
حملات شدید پهبادی اوکراین به روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68789" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68788">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=eXjqUei-hLGh9cPnf7xmY68DBdStjWyANIY7OKx0rfNDCAHP90viQsiKgWhsGI2yxSXSe5n6psSbfE_QexhRob4zxI3B_ueECbmBEt7a59MBb9Ur7veuRhIe2GzwegEITpbSmu2qJuPCg09tsKJEEERGP_5WME3gvCoAFNled_BkotUUDuBruCVK30LUVqcGZUKK1Cn1NqpHZt8ZtbpI-xXP6ONldCI6mhyuUM5xCiE144Mwf4jaX1HNaQNwbDhBHeFe_3e5LAz92Bn9q2C5MwqQk8S3m7qu12m_l5wbCK0aifFydp8R1uX4L7dThAJc-5qhvrdknIE3mkqsS4FJ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=eXjqUei-hLGh9cPnf7xmY68DBdStjWyANIY7OKx0rfNDCAHP90viQsiKgWhsGI2yxSXSe5n6psSbfE_QexhRob4zxI3B_ueECbmBEt7a59MBb9Ur7veuRhIe2GzwegEITpbSmu2qJuPCg09tsKJEEERGP_5WME3gvCoAFNled_BkotUUDuBruCVK30LUVqcGZUKK1Cn1NqpHZt8ZtbpI-xXP6ONldCI6mhyuUM5xCiE144Mwf4jaX1HNaQNwbDhBHeFe_3e5LAz92Bn9q2C5MwqQk8S3m7qu12m_l5wbCK0aifFydp8R1uX4L7dThAJc-5qhvrdknIE3mkqsS4FJ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی وزارت کشور :
عباس چرت میگه مشهد سقوط کرده بود، تو دی ماه من خودم مشهد بودم خبری نبود اون شب.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68788" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68787">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68787" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68786">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRCfsObK1c1pcnN18bNa_Q_Ol16UizDitDvNEcljbdVT2zHqW9MQhIo7RbH8sbeAVW4qEM4aR9c_WJORzf-rVRBTd9qamxX07QjImG84d6YZKAZuaXQvu_TpUIWOLTzE6JpizC_i94A-WJ3nQA7MllmDs6m93rw2OQENLDo5IAX_CcpWZoiJ8hWkJNM2ZVcZcFn78cqYRxPxb6TYsl2n6xTfTQrjBs8-6x46F0co2gTZeGZxfbaDkVN1yd3CvMRBYtV0Hp7cqOp-8eOS4B50hJTLjq2PTb6y8PtqXI20TfHgGSlnNxC2E--OwIOcWPxdEdqGm8X-yTwJOfbaNPl-Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68786" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68785">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=bniOvy6aBrYVIdsfXiVkOPJjGyMpfDiwicMhvZw9LeisyaIz6isqobL8RM5LBIIeF_iTny-hQbDbVwUm5Af5iGVjEvqMbIC25nQqzxw1DgDBxEzOZuZsOrpWX9Wp5dHSAgpSz4TGOby4Nr-PzjMIlyWsTz5gJEOCJxvjfh1HgkUe8MTRilDuV-DOmirsGPf50QnyMXsjldqZpVSoF5TUmQbWNj_j3PFbaDivOinPGhv6Jf-zjnaDA6splUq8FdKXjHu2OYfQGf3GRWfLQCNcP_UvdSIIIsJpGAgO2-roH2dtcjAYpCjSBHAH9-zv2XqQqfN1_1V2wa7KP0r-ZGAoig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=bniOvy6aBrYVIdsfXiVkOPJjGyMpfDiwicMhvZw9LeisyaIz6isqobL8RM5LBIIeF_iTny-hQbDbVwUm5Af5iGVjEvqMbIC25nQqzxw1DgDBxEzOZuZsOrpWX9Wp5dHSAgpSz4TGOby4Nr-PzjMIlyWsTz5gJEOCJxvjfh1HgkUe8MTRilDuV-DOmirsGPf50QnyMXsjldqZpVSoF5TUmQbWNj_j3PFbaDivOinPGhv6Jf-zjnaDA6splUq8FdKXjHu2OYfQGf3GRWfLQCNcP_UvdSIIIsJpGAgO2-roH2dtcjAYpCjSBHAH9-zv2XqQqfN1_1V2wa7KP0r-ZGAoig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این ویدیو از اینکه نشونه آدم پولدار چیه، اخیرا خیلی وایرال شده!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68785" target="_blank">📅 12:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68784">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olXk5llOKYXS9LY50Aoe_rVgmnSfn40GndUiHhRILP0DVb2LMTa3FVB37QjzgMTqRPthJq9K8HBtot-LncEm0njKXdaH_e3B3qH8EwRQYmTAI9PMwoani_An_Bm4Yg5JmPpw4UEnPeyvZAvvq8LcX76P_nVEaeOrke9OWSFfkipUMu-10iR6Q3CMKXrgXTMh4lswjf8t7SqvXMIUD67IcRtWf2j2_jvvFw4F-lgH4wbflzyUvRKP2yHH3ZTBU3wZIRjKggS594RPxznz9tiTFMEjA03Y91JgSL2W8lQisOwqovslkSSE4vUDpIppCBJRgSO8JuMPYrRGFj7rKZE5_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
شلیک موشک از کرمانشاه به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68784" target="_blank">📅 11:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68783">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=C8ethywor7bYehWmmIxtkkrbj_AXavUU2uM811jg_i0AmwWuUNnDyaV__JudOXLGQggeWtTBa0bqk4P1B4VFPSmALCDEfz3AaO93lcMo5fFoJRDR4Kyj_RyES7erayeemThZns0TAgeyPAvuc0g09vQL7c7U94xnlnsfqqn9EIeinEb67fyRRovqpQANcdQqpYs8Ee6ZMFQc9SItdgxUZ0ZhmHreVHkm8Rzm4OLASnACddbzakTLBDcCIVhICHkvUMpUTV5l5lcMH47oiTUsCRuiqGmJuTK1DvmEyBFM8_GII6Z85VaQb7Kx_aa15yeNGaCUdE9fdrA9m88Qro2xEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=C8ethywor7bYehWmmIxtkkrbj_AXavUU2uM811jg_i0AmwWuUNnDyaV__JudOXLGQggeWtTBa0bqk4P1B4VFPSmALCDEfz3AaO93lcMo5fFoJRDR4Kyj_RyES7erayeemThZns0TAgeyPAvuc0g09vQL7c7U94xnlnsfqqn9EIeinEb67fyRRovqpQANcdQqpYs8Ee6ZMFQc9SItdgxUZ0ZhmHreVHkm8Rzm4OLASnACddbzakTLBDcCIVhICHkvUMpUTV5l5lcMH47oiTUsCRuiqGmJuTK1DvmEyBFM8_GII6Z85VaQb7Kx_aa15yeNGaCUdE9fdrA9m88Qro2xEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
‌علی‌اکبر رائفی‌پور، ازحامیان جمهوری اسلامی:
با شناختی که از سپاه دارم اگر نظام سقوط کند، سپاه پاسداران موشک‌های خود را بر سر شهرهایی خالی خواهد کرد که به کنترل طرف مقابل درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68783" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68782">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=L09zq3kPStSGpTBp68FVzrpcNGIOeTWARfF0rx1MpXXCg-BMdbHBi9VyfRf2cvy5v99nz0u-CjMARusmajtCNKpW3QRuPT59qshTcsvNPXrMqi0WmIpvcEowDw3h2pLt13DVRi-hqlJFxxlHI_yznAYcwLEMaRRuOmRji-JErXWAQCA6sS1mspV7Lr-abJym8vfvsxpwhlBztJ-NUZdf-CFEKlx3OtY3dPVjgZq8h-dXs3jmgimxan9eTOyK4jB8se1QQjfj-fVgX8OzP79fZMM-dDNZ_M8mTDnUdMs8n9tlDzjOxB8QFc1eExtcd8EIdphtKr-sBSXJmOqyoyRKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=L09zq3kPStSGpTBp68FVzrpcNGIOeTWARfF0rx1MpXXCg-BMdbHBi9VyfRf2cvy5v99nz0u-CjMARusmajtCNKpW3QRuPT59qshTcsvNPXrMqi0WmIpvcEowDw3h2pLt13DVRi-hqlJFxxlHI_yznAYcwLEMaRRuOmRji-JErXWAQCA6sS1mspV7Lr-abJym8vfvsxpwhlBztJ-NUZdf-CFEKlx3OtY3dPVjgZq8h-dXs3jmgimxan9eTOyK4jB8se1QQjfj-fVgX8OzP79fZMM-dDNZ_M8mTDnUdMs8n9tlDzjOxB8QFc1eExtcd8EIdphtKr-sBSXJmOqyoyRKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⭕️
گفته میشه دیشب با وجود اینکه پدافندا توی تهران خیلی فعال بودن اما انفجاری گزارش نشده.
احتمالا دیشب بیشتر پهپادهای شناسایی آمریکا، مثل MQ-1C Gray Eagle و... تو آسمون تهران بودن و پدافندا هم سعی می‌کردن اونا رو بزنن.
احتمالاً مأموریت اصلی این پهپادا دیشب شناسایی بعضی مکان‌ها، مراکز نظامی، محل استقرار پدافندا، و... بوده و ممکنه که آمریکا درحال آماده کردن خودش برای دور جدیدی از جنگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68782" target="_blank">📅 10:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68781">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=HN5C17GJ_MmqR3bmxt8H77S47LWu57QP6sjS2lHmTrl-c-h-U_CX2QeZY-2-52ktNbejihuyaJCoWNEpV-FZqFIB3DDv4867liHtwwZaHiqwPKXQ0fjniB26Z8V-yFROhVdzDqx5k_l6xmNipHWbaDAFkpX22tLtBi5qijCD0caxGnYgXpdKUmKr3m0JilsqcVSrZBUf9uElJn3rnG6rLYDEKFDSOOdyKV-tqEYSeZ14CIX3SlzhEzWQ-z9lmCyjHs7WQCdZZq3ysG906c_U7hMcQVzZSJuSg_R1IupHWepvcesW0jRY878bcHnqzph8eh5LAI0XcoqoDzxb3GWkRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=HN5C17GJ_MmqR3bmxt8H77S47LWu57QP6sjS2lHmTrl-c-h-U_CX2QeZY-2-52ktNbejihuyaJCoWNEpV-FZqFIB3DDv4867liHtwwZaHiqwPKXQ0fjniB26Z8V-yFROhVdzDqx5k_l6xmNipHWbaDAFkpX22tLtBi5qijCD0caxGnYgXpdKUmKr3m0JilsqcVSrZBUf9uElJn3rnG6rLYDEKFDSOOdyKV-tqEYSeZ14CIX3SlzhEzWQ-z9lmCyjHs7WQCdZZq3ysG906c_U7hMcQVzZSJuSg_R1IupHWepvcesW0jRY878bcHnqzph8eh5LAI0XcoqoDzxb3GWkRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو روز قبل یه گونی آدم از مجری‌های صداوسیما ، اعضای پایداری و بعضی ورزشکارها در واکنش به کارزاری که راه افتاده بود، پا شدن رفتن جنوب که بگن ما از جنگ ترسی نداریم و این حرف‌ها؛
حالا کجا رفته باشن خوبه؟
بهمنشیر که تو نزدیکی کویته و 14 ساعت [1125 کیلومتر] با بندرعباس فاصله داره
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68781" target="_blank">📅 10:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68780">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=VhdwMTFQHVuonVvYbVU0m9coxDi45eoxIEx1KaTBQOFqEd1ANNoxWslfKuX9i_k6D3hKhLxzhOt3spVEkhLbRYBABl1ZYDniLRA1Kn2lVD_e_0d_rDgrv7d4kkCVjD93iUB0E2VrwtyUaLyGTEX4SU_Vg-Y8v6t6HCLlp36qqgbM6Uf8cK8vt_totIZxsMjhS20xqry2zmbPehnIdWqBtYG36MZD_IRtWaj1cZVw8c92Kc-EDnQzj7LBBr-_reGns9P1K_keN1ZqG8lBPlU0vCPOaz8DJ4cv5YRK9wgle8NH1b2pIqdvHoheHIgZf3gw4b1wbfLwQcGsZ-Ilpl_5jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=VhdwMTFQHVuonVvYbVU0m9coxDi45eoxIEx1KaTBQOFqEd1ANNoxWslfKuX9i_k6D3hKhLxzhOt3spVEkhLbRYBABl1ZYDniLRA1Kn2lVD_e_0d_rDgrv7d4kkCVjD93iUB0E2VrwtyUaLyGTEX4SU_Vg-Y8v6t6HCLlp36qqgbM6Uf8cK8vt_totIZxsMjhS20xqry2zmbPehnIdWqBtYG36MZD_IRtWaj1cZVw8c92Kc-EDnQzj7LBBr-_reGns9P1K_keN1ZqG8lBPlU0vCPOaz8DJ4cv5YRK9wgle8NH1b2pIqdvHoheHIgZf3gw4b1wbfLwQcGsZ-Ilpl_5jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
لحظه‌ای که عادل فردوسی‌پور تو لایو فوتبال 360 بغض و گریه کرد...
اپلیکیشن‌ و سایت فوتبال 360 به علت اینکه عادل و مهمون‌هاش از تیم ملی انتقاد کرده بودن، به درخواست قلعه نویی و باندش فیلتر و از دسترس خارج شده و مجبور شدن برنامه رو تو لایو اینستاگرام و یوتیوب اجرا کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68780" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68779">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=bI8ramhew36ZyQkudEsa8AzJ0IORK-qguXqseAaSArdy9VLoBNBxssoYFrVr8vM0Qt0SvwcVbeqv-mJ8E4Fu37OuJDUwT_n5QxTqgkCYAYPvu4J_RlzsSJw3Sjfa3xNL5KYV3RcDaFblq2K7VezMPDvfQFiQLPkA5X0C5wk80IjfqqFiMxuEeLkj-XC7LvWze7H-RRsFtDUG3mplX37gmYdWN-PMLRQTVdcN2zKqpa1M1tcf5n23TOwcJQK2iYtrh6QfbMKL35MQd9agOi5LDoZYWdh2StV-zzNQm03t0HXYk5jAG1vSkUxLqoOJS3OlWQ-ZZuSEI-rNCgMUofxtGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=bI8ramhew36ZyQkudEsa8AzJ0IORK-qguXqseAaSArdy9VLoBNBxssoYFrVr8vM0Qt0SvwcVbeqv-mJ8E4Fu37OuJDUwT_n5QxTqgkCYAYPvu4J_RlzsSJw3Sjfa3xNL5KYV3RcDaFblq2K7VezMPDvfQFiQLPkA5X0C5wk80IjfqqFiMxuEeLkj-XC7LvWze7H-RRsFtDUG3mplX37gmYdWN-PMLRQTVdcN2zKqpa1M1tcf5n23TOwcJQK2iYtrh6QfbMKL35MQd9agOi5LDoZYWdh2StV-zzNQm03t0HXYk5jAG1vSkUxLqoOJS3OlWQ-ZZuSEI-rNCgMUofxtGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
نظر مارکو روبیو درباره برجام (سپتامبر 2015)
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68779" target="_blank">📅 09:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68778">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
سنتکام: حملات امشب به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68778" target="_blank">📅 04:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68777">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68777" target="_blank">📅 03:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68775">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=tQcQoRACFt0VkaQPsXOmA4tEe-zXJo7p0z-EYUFGRMqoyqPJHR3m7zLFTRZ9VPxNyoNFVxVvYJQLcqx-X9zz_vXL6Aygqnprj7XU4XcO4juJPXpKQO9HR0-CCYKSdIp6Dw1ImRj-mojzl-qf4w-7hAXCPzKLZlXUJBy5UEKZ1HsIFAInOpOCgwcYsr-kougKkdZU1ERLGcnyCNmzQ9kNZbkb7F41MHXYBcThZb8mRT3ksKliJWDn9QGBrM3NKbw5tiOhQ6ceCnL0KLjQDgrohmujcFwCKYV_QF17OemLd3PwF0koyYbgN7VAGNeBgbN6VJ0HC0NM6RVnZZ6IQhwn3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=tQcQoRACFt0VkaQPsXOmA4tEe-zXJo7p0z-EYUFGRMqoyqPJHR3m7zLFTRZ9VPxNyoNFVxVvYJQLcqx-X9zz_vXL6Aygqnprj7XU4XcO4juJPXpKQO9HR0-CCYKSdIp6Dw1ImRj-mojzl-qf4w-7hAXCPzKLZlXUJBy5UEKZ1HsIFAInOpOCgwcYsr-kougKkdZU1ERLGcnyCNmzQ9kNZbkb7F41MHXYBcThZb8mRT3ksKliJWDn9QGBrM3NKbw5tiOhQ6ceCnL0KLjQDgrohmujcFwCKYV_QF17OemLd3PwF0koyYbgN7VAGNeBgbN6VJ0HC0NM6RVnZZ6IQhwn3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68775" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68774">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
❌
🌐
امشب ریزپرنده ها در تهران فعالیت داشتند، احتمال اختلالِ بیشتر در اینترنت وجود داره؛ پروکسی های پرسرعت زیر رو داشته باشید
https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68774" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68773">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در زنجان!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68773" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68772">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zih7D05qi-Bj7WX7xE4B9pvhkr8Z6HHKyDAOS75aiRAQN0Pbv__-JXcfVvp65gyV4Gw0WfeZKo7j5AOvopRbrVwdtx8fQdceGzpZWvpFCmT_ipGIyJ8lLDy0lmvXoMRo7C8B_zuVMkLRflcGXfUNr5ruz0pHbsK4GnAppfDF5ofk9tATBdoblBrvqPZEUuFpGRWda59vu4Rg2ztt9JSAV9zkMcMMMoPKAQHhafJwHoQI4Vq0sDoZ1DUkHCo-VMoJFD-jwM-wH9HEfsBLDFm3WYdvvnzDE4KK1O6Wi21q20BGqtMjtfknCwqIWc0cN_9KtlfUkuHMpkUxb4WM4NjEiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68772" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68771">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت پدافند شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68771" target="_blank">📅 03:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68770">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون حملات شدید آمریکا به</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68770" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68769">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68769" target="_blank">📅 02:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68768">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تا این لحظه سنتکام هیچ خبری مبنی بر آغاز حملات رو اعلام نکرده! #hjAly‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68768" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68767">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بابت گزارش های لحظه‌ایتون عمیقاً سپاسگزارم، ولی حتما سعی کنید بعدش چنین گزارش هایی رو پاک کنید خدای‌نکرده جایی تو بازرسی گوشی توسط مزدوران ج.ا، مشکلی پیش نیاد
❤️
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68767" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68766">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
هشت انفجار در تبریز  @News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68766" target="_blank">📅 02:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68765">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68765" target="_blank">📅 02:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68764">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه #hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68764" target="_blank">📅 02:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68763">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه
#hjAly‌</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68763" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68762">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68762" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68761">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68761" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68760">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان  @News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68760" target="_blank">📅 02:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68759">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68759" target="_blank">📅 02:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68758">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در نارمک!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68758" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68757">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68757" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68756">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzU3qUlqw9FSInQVlHPE-B3JXnkgy5L3EHQIXG-_yQ8ZhfeesA7_3B-13MXMef4Ej03Pag3ZQrSaY0S659Nu2gsa_AJ6uplXF0WeXOu6zaVZNBRknRWYWF3_iOOjTpCRG4IO89HRzaE46x-uwnbUNI293VQQHDLEkrX5NCksMfom_9h38bdOz1PeXt-a7B83tZA2g7zji5UW8B75t73axzV9VNBCFGKnM2c5ygpFuecjtFR9vhEADSsh0SYwIcK-981POwGnZ8M4lPddRCXTCWlGjH8JPqdyrbxMHeYVXfP3q0f66MNmoVo2q6-h5P62p8RlwnfHUl9bbaQJMqz7NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68756" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68755">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=tCXpZp7g8mkmABxoWYqD50VXoJh5OPZOQvaKkXsNYATl78RVcdEJZfVeCBwvdvj46kgEKfd1Q3pXuCVXuiF0_4UcrChpHEWSKvk_eaxZ2cvBjItFqPLnGOrTFtkwAWX8xO69t5pdWN9V9nlnYPy5Na-Da9p4p8dN3mvVLPGcOTb1VMaxGCjUnHzDDu7dquPn4dnQI1u6Sbt0Lr-KrZNbh7S9wwB7QCXc0zl6vuSm3eGB-DLZpi7xdqccef91JabAlTWmlu8S3DXsZouoFfcHjOe9UZ6iVCV4JVDrQ-vzoFiUqAPieI2kv8D7361QiNZrIh10mfLtvGAkErL0bzGk9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=tCXpZp7g8mkmABxoWYqD50VXoJh5OPZOQvaKkXsNYATl78RVcdEJZfVeCBwvdvj46kgEKfd1Q3pXuCVXuiF0_4UcrChpHEWSKvk_eaxZ2cvBjItFqPLnGOrTFtkwAWX8xO69t5pdWN9V9nlnYPy5Na-Da9p4p8dN3mvVLPGcOTb1VMaxGCjUnHzDDu7dquPn4dnQI1u6Sbt0Lr-KrZNbh7S9wwB7QCXc0zl6vuSm3eGB-DLZpi7xdqccef91JabAlTWmlu8S3DXsZouoFfcHjOe9UZ6iVCV4JVDrQ-vzoFiUqAPieI2kv8D7361QiNZrIh10mfLtvGAkErL0bzGk9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
پهباد‌های انتحاری در آسمان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68755" target="_blank">📅 01:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68754">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
جمهوری اسلامی به کویت حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68754" target="_blank">📅 01:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68753">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=uAd1OdZv8eMi--SNrpfXImF8RMC7NP4u0DD3d-QCBNcGzz_yDvBwRZeF53mH-WiKJGqeU-QnjBlH1wTxv1APvgVDM2Fqa2x8dLPvZXs6ycXvx9pu2T9YH8XnEw8EgZbMSUkAD7_wuxiHRNmsIJJ05yeWXhRjoCIorNCichj26rr1BB01D5Ki5VUjLJcinu9rFFp7xidvZsf8uzE_HfWK8siyVnztH-MqBMkkO3rhXeWPoY_lpEgxwhMS6WOTuauEntZ6UTGHLz_9gOuxLLVkJ5aafMuuruSX8FoLVe6rAtehfTjZagAOSyrlcK1yXz9oo9ax7bUPNOOKvaFldxlOag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=uAd1OdZv8eMi--SNrpfXImF8RMC7NP4u0DD3d-QCBNcGzz_yDvBwRZeF53mH-WiKJGqeU-QnjBlH1wTxv1APvgVDM2Fqa2x8dLPvZXs6ycXvx9pu2T9YH8XnEw8EgZbMSUkAD7_wuxiHRNmsIJJ05yeWXhRjoCIorNCichj26rr1BB01D5Ki5VUjLJcinu9rFFp7xidvZsf8uzE_HfWK8siyVnztH-MqBMkkO3rhXeWPoY_lpEgxwhMS6WOTuauEntZ6UTGHLz_9gOuxLLVkJ5aafMuuruSX8FoLVe6rAtehfTjZagAOSyrlcK1yXz9oo9ax7bUPNOOKvaFldxlOag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست وزیر جنگ آمریکا:
«رئیس‌جمهور ترامپ گفت که ما دوباره درگیر جنگ‌های احمقانه‌ای مانند [عراق و افغانستان] نمی‌شویم، و او این کار را نکرده است.
به همین دلیل است که ما سعی نکرده‌ایم جامعه ایران را از نو بسازیم، بلکه صرفاً، به شیوه‌ای واقع‌گرایانه و با شعار «اول آمریکا»، اطمینان حاصل کنیم که آنها هرگز به بمب هسته‌ای راه پیدا نمی‌کنند - کاملاً متوقف می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68753" target="_blank">📅 01:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68752">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=rbAWgqnGg8T7yhnMLUtEFvlW-kztwoFT60dB6q60khcxuDYtlDF7FRYuLn_luLOxlHlB_H7pnbnD0h7WEqOStm5qLaSaN9F0Wj7ZRSklb_w5D6UP3mIUnLYywkPCPwKwG9tOnlNABduL2ao9D0s7tN2OZO6zaT-Ev4qUM7G1s0FAXzc_79oka4HryRFchseADHIP5EGiVcJpIu2Fi4adIxVu0Tzi1upuKWvn4Kr704BfecHecIyXIg-CuamTGHx1zdgcEYx8B6bkgevGjar0-u6QMrakbHGHEywoUaefbdvAfFGZ5K3yemTGTFQZf2VxivaDin2uC0GV2L5jbr_Vpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=rbAWgqnGg8T7yhnMLUtEFvlW-kztwoFT60dB6q60khcxuDYtlDF7FRYuLn_luLOxlHlB_H7pnbnD0h7WEqOStm5qLaSaN9F0Wj7ZRSklb_w5D6UP3mIUnLYywkPCPwKwG9tOnlNABduL2ao9D0s7tN2OZO6zaT-Ev4qUM7G1s0FAXzc_79oka4HryRFchseADHIP5EGiVcJpIu2Fi4adIxVu0Tzi1upuKWvn4Kr704BfecHecIyXIg-CuamTGHx1zdgcEYx8B6bkgevGjar0-u6QMrakbHGHEywoUaefbdvAfFGZ5K3yemTGTFQZf2VxivaDin2uC0GV2L5jbr_Vpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاورمیانه هرشب
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68752" target="_blank">📅 00:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68751">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iho1_fLZivzDiaeqTH8rmKjMePwTGp2u6ikd789aKKX59mZiu4nfGLuIzbGPCkIW-mDS7b99Qs_y6GQ1UN__NK4XFyjNQm3VCYwUGEPwbqae-tWWcLyyzMjkCiAdtyiu1_F-ospo54M2FFiI-JmjrEUQTcJj2zYZM4BJvxDtSBX8MWVg9AbJY1ud1BnSaiN-T6GZO_3GHOZFpwDyCgC_g7_zGsd38gB_byij3ughNM4bpDJm4jzEZWl8trHjOlQlC0hRyX7veYsZu-kOnNh-hZiU52I719tx12NqGcFImIhhFtLv0xgrXbfLhDv4uOJirb74a_bubI45bxq5DI5EYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قرارگاه مرکزی خاتم‌الانبیا:
آمریکای جنایتکار مراکز هسته‌ای و تأسیسات حساس ایران رو تهدید کرده که ممکنه بهشون حمله کنه.
اعلام می‌کنیم اگه ارتش متجاوز و تروریست آمریکا چنین اقدامی انجام بده، این کار رو به‌عنوان گسترش جنگ در منطقه تلقی می‌کنیم و همه منافع آمریکا، همچنین منافع متحدها و حامیان این کشور یاغی و شرور، هدف حملات قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68751" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68750">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=c07U7H_RvwYWHh6uhNInU25kpc9uJ9DrI8oCC-44OedRIVfkFYc0Sf37Hj9jg09Lu0IUoEdvBqbcAGpTUlGuWsrWMSof8jbnnVDNJqmVIqbSa0Zbi6UcwaRk55VQzLgIwXNLD6xdRd62k7i-2CTq02oyaykFiY0k8wEEvXjQkDbEs2quvjK0hqVdHET5aNzwz9iIeEhzFq_ErM_4ov5JLRSyhvXEyQaGMlBleqC5TPdraRoujz1fGafjW6gRjbr_7M0sWuJKNQYvqz-IlKtG0WlIXndGuHO4zRAIee0AQprOkrRRWdc4f0kpWrZoPFjSGq6NHY04Q1oyVzl6mFkBDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=c07U7H_RvwYWHh6uhNInU25kpc9uJ9DrI8oCC-44OedRIVfkFYc0Sf37Hj9jg09Lu0IUoEdvBqbcAGpTUlGuWsrWMSof8jbnnVDNJqmVIqbSa0Zbi6UcwaRk55VQzLgIwXNLD6xdRd62k7i-2CTq02oyaykFiY0k8wEEvXjQkDbEs2quvjK0hqVdHET5aNzwz9iIeEhzFq_ErM_4ov5JLRSyhvXEyQaGMlBleqC5TPdraRoujz1fGafjW6gRjbr_7M0sWuJKNQYvqz-IlKtG0WlIXndGuHO4zRAIee0AQprOkrRRWdc4f0kpWrZoPFjSGq6NHY04Q1oyVzl6mFkBDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68750" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68749">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=VnXqRmo8aaX7hHEUsaQyE8Za_jw4EJk8h-Ad_b_ZjQB17YGTgsn1Oa5w-yUi6552ll2DPUBpQWBy3VXDB7dDDlo5oJLV389YU_PZAWL6kKdnMBlUEYegFG7d-PueZ09xjzhBD6Vm5uTAVchmT0KkiO7aIdB3CcKVIIdz1ANXGbzUFpD1XRlI7cs-oQD5mBMiNZ5bS5j7mGUvos9OXp9XGG64GSCkJHiHett7Xlj5-gJiq7TMcENNlqDaR4xUj_qvbvQFH7vE6WVE6I_BnQ7xQdFzgjb5wcA2VpIx9R0MZFCFp9jlBgF9mIV-ShDFF0AaABtZSUzUSFdY2q9N-mOcUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=VnXqRmo8aaX7hHEUsaQyE8Za_jw4EJk8h-Ad_b_ZjQB17YGTgsn1Oa5w-yUi6552ll2DPUBpQWBy3VXDB7dDDlo5oJLV389YU_PZAWL6kKdnMBlUEYegFG7d-PueZ09xjzhBD6Vm5uTAVchmT0KkiO7aIdB3CcKVIIdz1ANXGbzUFpD1XRlI7cs-oQD5mBMiNZ5bS5j7mGUvos9OXp9XGG64GSCkJHiHett7Xlj5-gJiq7TMcENNlqDaR4xUj_qvbvQFH7vE6WVE6I_BnQ7xQdFzgjb5wcA2VpIx9R0MZFCFp9jlBgF9mIV-ShDFF0AaABtZSUzUSFdY2q9N-mOcUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست:
محاصره ما دوباره اعمال شده و عملاً غیرقابل‌نفوذ است...
بسیاری از حملاتی که دریاسالار کوپر و سنتکام (CENTCOM) انجام می‌دهند، توانایی ایران برای رصد و پایش در تنگه هرمز را از بین می‌برد.
سناتور جان هوون: « هدف از این بودجه‌گذاری همین است... اطمینان از اینکه ما و متحدانمان می‌توانیم در تنگه هرمز عملیات انجام دهیم... و اینکه ایران را وادار کنیم تا در راستای اهداف ما عمل کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68749" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68748">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=JZZpirOlgNbBvfEletfFPOB20vRVBxq_PEspiWD-4pc7qffh57E1TvEGr7iUfAgPQCVfPYbWqCtfAQxc9Ia5RFcGgXDYp3PjZ5TEPByagchK9EFTPU4raPcUOxtEDpXc-Qg2h30rW4naeTDfjv5Jmsw3eDAYbrCs7sF6plLXjeeP33MdsFxQuZxGDFkb3wmiZ-_kUKAlWFoQH0vDu46R1kwyjwpp-CqDhoruzs0c5704o3qMusTW2oHltBiXJ33FtphizYNFNXTUBhk8V7-zMJv6JLy6RPxihCeXlxeX3HPNkhycwvswlAUfxQOYX0yWlhyn9Gbh5TiWGiYgVyGh4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=JZZpirOlgNbBvfEletfFPOB20vRVBxq_PEspiWD-4pc7qffh57E1TvEGr7iUfAgPQCVfPYbWqCtfAQxc9Ia5RFcGgXDYp3PjZ5TEPByagchK9EFTPU4raPcUOxtEDpXc-Qg2h30rW4naeTDfjv5Jmsw3eDAYbrCs7sF6plLXjeeP33MdsFxQuZxGDFkb3wmiZ-_kUKAlWFoQH0vDu46R1kwyjwpp-CqDhoruzs0c5704o3qMusTW2oHltBiXJ33FtphizYNFNXTUBhk8V7-zMJv6JLy6RPxihCeXlxeX3HPNkhycwvswlAUfxQOYX0yWlhyn9Gbh5TiWGiYgVyGh4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
من در مقابل یک کمیته نشسته‌ام که می‌خواهد درباره پیروزی در جنگی صحبت کند که چهار سال است ادامه دارد، و درباره شکست استراتژیک درگیری‌ای صحبت می‌کند که چهار ماه است ادامه دارد، تا از دستیابی ایران به بمب هسته‌ای جلوگیری شود.
امیدوارم که در این شهر، دیدگاهی وجود داشته باشد نسبت به اهمیت تاریخی اقداماتی که رئیس‌جمهور ترامپ در حال انجام آن‌ها است.
آیا شما می‌خواهید که گروه‌های افراطی اسلامی به بمب هسته‌ای دست پیدا کنند...؟"
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68748" target="_blank">📅 00:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68747">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=MuY-4vZMnmSIwadBLlOt5UALhxnx5_bX9H9zaWLCnJexvBC7DwE9jloRZh7uMUMd7o2gwX-cRnuK7WcmeBuNakLwMNMuvc6XQjqRRaFVSPAzbZ5aUnOhVpwXeOWmN6-d7OwW1Omd7pNCXOFArTIT6kc0Qc7LgOW-qtXZ8dJSD-VJ8hFvoq5RXn4u8IXB-SlocbhGJYgg6clma1Yee5sRFkLKN_z_LigRLx0G4bjxuKBxnhXbrOwy3Dr_pZSHsWMz7aionvom4g0Sh-36UpxImyajMECKgNwjSZz9XT1tAamJ_aMAb32FliZSMWDQlOsgaCs89NWeLX757eTs_Q0l0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=MuY-4vZMnmSIwadBLlOt5UALhxnx5_bX9H9zaWLCnJexvBC7DwE9jloRZh7uMUMd7o2gwX-cRnuK7WcmeBuNakLwMNMuvc6XQjqRRaFVSPAzbZ5aUnOhVpwXeOWmN6-d7OwW1Omd7pNCXOFArTIT6kc0Qc7LgOW-qtXZ8dJSD-VJ8hFvoq5RXn4u8IXB-SlocbhGJYgg6clma1Yee5sRFkLKN_z_LigRLx0G4bjxuKBxnhXbrOwy3Dr_pZSHsWMz7aionvom4g0Sh-36UpxImyajMECKgNwjSZz9XT1tAamJ_aMAb32FliZSMWDQlOsgaCs89NWeLX757eTs_Q0l0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست درباره ایران:
ایران از نظر نظامی در ضعیف‌ترین وضعیت تاریخ خود قرار دارد...
بی‌شک اذعان می‌کنم که آن‌ها همچنان از توانمندی‌هایی برخوردارند، اما حجم خساراتی که ما طی این رشته عملیات به آن‌ها وارد کرده‌ایم، آن‌ها را در بدترین موقعیت تاریخشان قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68747" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68746">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=SUZSqVTaDUfZmu-EU0IacJyhfJzjE9bQWl-rCeG7zDhLvKN21sAWr-nqO45kKYiYNmDq4ImmIjZ_DJSVFIh_ZkeA2jJpeei2U4vd3u898h9_uFFKNAf6VEyETH6Lc51EXjHyG29J8SI_JKj_tazcj-mKnI4tyDFERdkW-3Flx4Qv1DIjb4iCfdxsBcCfRc3mxeAbUpTieFDR7FgV24VlMCsp-hjbN1gzzfW-QLNCW2_PKT3nCk7fauxjiI5oNW38c-E5K2FD6HtQCet1BA1r4X86h0Be8ODfylu8iLVld7gA2QbD6zWmLuQHSDAJhIwBtSdxXBFEptt0T965HKD3CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=SUZSqVTaDUfZmu-EU0IacJyhfJzjE9bQWl-rCeG7zDhLvKN21sAWr-nqO45kKYiYNmDq4ImmIjZ_DJSVFIh_ZkeA2jJpeei2U4vd3u898h9_uFFKNAf6VEyETH6Lc51EXjHyG29J8SI_JKj_tazcj-mKnI4tyDFERdkW-3Flx4Qv1DIjb4iCfdxsBcCfRc3mxeAbUpTieFDR7FgV24VlMCsp-hjbN1gzzfW-QLNCW2_PKT3nCk7fauxjiI5oNW38c-E5K2FD6HtQCet1BA1r4X86h0Be8ODfylu8iLVld7gA2QbD6zWmLuQHSDAJhIwBtSdxXBFEptt0T965HKD3CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت
هگست:
این درخواست تکمیلی دو هدف را دنبال می‌کند: حفظ آمادگی نظامی ما برای پاسخگویی به نیازهای جدید امسال؛ و تسریع قابلیت‌های حیاتی برای جایگزینی و تقویت قابلیت‌هایی که در شرایط اضطراری استفاده کرده‌ایم...
در حوزه آمادگی، ما ۲۱ میلیارد دلار درخواست کردیم. این مبلغ برای تأمین حقوق نظامیان، جایگزینی تجهیزات مورد استفاده در عملیات‌های اخیر، حفظ نیروهای مستقر در خط مقدم و افزایش قدرت نهایی پرسنل در عین تثبیت کمبود سوخت حیاتی ماموریت و پشتیبانی از گارد ملی هزینه خواهد شد.
در حوزه قابلیت‌ها، ما ۴۶ میلیارد دلار درخواست کردیم. این بودجه خطوط تولید را گسترش داده و تحویل مهمات مورد نیاز را تسریع می‌کند. ما در مورد موتورهای موشک سوخت جامد، JADM، موشک‌های مافوق صوت و قابلیت‌های ضد پهپاد صحبت می‌کنیم. علاوه بر این، ما از این سرمایه‌گذاری برای تضمین تسلط دیجیتال و فضایی، از جمله شبکه‌های ماهواره‌ای انعطاف‌پذیر، استفاده خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68746" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68745">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=Gnh0TEPPS64x6uSue5jgQ5EgKqcxE5E9OlZA1_5l0jZHRyHcY0FXj7GLlX1gQUxiKFLJbQlh79kXXv4KTUaK9qhctZcYLc6vTa6K840BitS_QW8rYQVgLLf9AiG2Tqc2c6Jjkj8czf-y7wGpDicfkUvph7i9rciAexK7zc9InU_FvTr9DPm0CiZLKweDn4LrUwb2FqC4ViJ6h8P_EFFBA_Nq4y_qb40bfJ-qk-u8-FQ_7q0F9W0Wvw2JY5KF0n-2KorstkAZT2ge9yP7kp17AIyuNcpo0fiXSWE956Dk_VIn7WmX2bp3scL-ewZ82hA5QlqACkFQawp8C05HXzfnIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=Gnh0TEPPS64x6uSue5jgQ5EgKqcxE5E9OlZA1_5l0jZHRyHcY0FXj7GLlX1gQUxiKFLJbQlh79kXXv4KTUaK9qhctZcYLc6vTa6K840BitS_QW8rYQVgLLf9AiG2Tqc2c6Jjkj8czf-y7wGpDicfkUvph7i9rciAexK7zc9InU_FvTr9DPm0CiZLKweDn4LrUwb2FqC4ViJ6h8P_EFFBA_Nq4y_qb40bfJ-qk-u8-FQ_7q0F9W0Wvw2JY5KF0n-2KorstkAZT2ge9yP7kp17AIyuNcpo0fiXSWE956Dk_VIn7WmX2bp3scL-ewZ82hA5QlqACkFQawp8C05HXzfnIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست وزیر جنگ آمریکا:
«رئیس جمهور ترامپ از یک منطق ساده پیروی می‌کند - ارتش برای تحقق صلح از طریق قدرت به یک سرمایه‌گذاری نسلی نیاز دارد.
ما می‌دانیم که بهترین راه برای ایجاد صلح، آماده شدن برای جنگ است - برای جلوگیری از آن و این دقیقاً همان کاری است که وزارت جنگ انجام می‌دهد - ایجاد نیرویی چنان توانمند که به چالش کشیدن آن برای هر کسی پوچ و بی‌معنی باشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68745" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68744">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AV0F9r4AnRNbm1eW21jzkKcQSvX_Wf2s4jE9484pX7wbkcMKChs476FEr9W_nggUhjovYYSG8_TE5fMPazDVgDb-HrctAiaBbwtpVQ_Dw4lef43HwxFLXjR9b9kSfuetOCQoStxbTu8DjI3Umq56tM1br9RyoL_GoPYxIR6d42qafkYKIugnnSfaOysFbCYaz2pX4uES9WKNewifAaRyp27cyF6NCgGgGzpLuL-kRK3Jxs_u_JdyoW6Dxd49v1OylNSqp1SlCPInc5ruiCE2L7XoHNuQleyFnpwaJJk67rGAB9GDzScD88UVQEjy5NOx5mmShBzyd2r_LHTRN-RWIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
چند سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل بلند شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68744" target="_blank">📅 23:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68743">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تاسیسات جدید هسته‌ای ج.ا: ۲۰۰ متر زیر کوه کلنگ
پرنفوذ ترین بمب غیرهسته‌ای آمریکا: GBU-57 با ۶۰ متر نفوذ
#hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68743" target="_blank">📅 23:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68742">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6e32w6eW7y0zJpsSNFU9aWzBgEUUfS5zeZrb_bvsr3JOT1qQVpeS3yDD6A6HUfvJx8j7dIMoG9Zpo1MGlfUHFQ1Ij5obBTdwxgVseYNkykAF_3gww9BUdxwKCN8NehG1IOu4KxPS1jQCzVgY4SwYpEB46jsn-yqsIAOgl3cR-NIZ74tvXF4ToyfFvZrgC7_zeQuiMnIOaYrgspv3uoU-1NtsHjQ-0pPvITTNcBIvz-eAON_OBoDlFORBAffZ5r8AMGlhfW_P0h0or15yjDFPVvLqey86x4WVz5huYhwNC6RiycGguNxL1ygU3L34xX2bBWLwyrVKZ7z4zjosNLSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
جنگ افغانستان: ۲۰ سال، ۲ هزار کشته.
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
درگیری‌ها در ونزوئلا: ۱ روز، ۰ کشته.
درگیری‌های نظامی با ایران: ۴ ماه، ۱۸ کشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68742" target="_blank">📅 23:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68741">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=sZoviATdMLponBlDmOSfsIrBxxbHqfdA5mkQ4Fik2XF3oBSQBPOkgRf898yV1XOqPTIZcNHJUPdpx9iK-FjvovBIoC9FCK-M7F9GGHaM6l8FHqAcfSZ41Hw2ZfAepdC7XO9VIlTxaSSPSPhJNmpfy24ynP4X8oQ45b0HbnrdeGotFw3En1NqleS6kW1QYpBadZ8SZV--cg43F4VRK3z-f73HsigpCpeyDCzouLLdmmexCHFQk3m_M9yiKSpXrC9ZNHf8sJ_uPd3NrlyTGvcJbxWTdfH0VoxTZaxYh2VU5oW1sVJ8Z70QzdV7Uus3Z3OSLbuK8IHAZc0mNJyJ0Pi6-jl8Z5v-rVBoowMRp1yHd6RJglyYYEizp5udYfxOH4LVe4gGAwyc8m8BWY1Uq-MW5YGEhpkvqaZiFp-8ini9nQx14o8fL54LIcw8B2PzWID0AsfGqHb7iRlAYkwd4jXHg-Oz5-GIgaI4LyjTMX15VqkAsBXnJf2iwnAlWOWHpSCRFJDnAVH8gmFClrhUlkd2IAEabZMqKzXj0qveiaW0Y8idDp4_7X0-BP35xSGb0qGtMySc3FMyxb8aPKchLySNa5YkOeKdkFJ9Owf_lMehDCWZ0lguKoZlZsvPbmLEJPAxIPeG6gAuUC_401Rai8Y5Z0bGBHUbQf6NattTQdM582w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=sZoviATdMLponBlDmOSfsIrBxxbHqfdA5mkQ4Fik2XF3oBSQBPOkgRf898yV1XOqPTIZcNHJUPdpx9iK-FjvovBIoC9FCK-M7F9GGHaM6l8FHqAcfSZ41Hw2ZfAepdC7XO9VIlTxaSSPSPhJNmpfy24ynP4X8oQ45b0HbnrdeGotFw3En1NqleS6kW1QYpBadZ8SZV--cg43F4VRK3z-f73HsigpCpeyDCzouLLdmmexCHFQk3m_M9yiKSpXrC9ZNHf8sJ_uPd3NrlyTGvcJbxWTdfH0VoxTZaxYh2VU5oW1sVJ8Z70QzdV7Uus3Z3OSLbuK8IHAZc0mNJyJ0Pi6-jl8Z5v-rVBoowMRp1yHd6RJglyYYEizp5udYfxOH4LVe4gGAwyc8m8BWY1Uq-MW5YGEhpkvqaZiFp-8ini9nQx14o8fL54LIcw8B2PzWID0AsfGqHb7iRlAYkwd4jXHg-Oz5-GIgaI4LyjTMX15VqkAsBXnJf2iwnAlWOWHpSCRFJDnAVH8gmFClrhUlkd2IAEabZMqKzXj0qveiaW0Y8idDp4_7X0-BP35xSGb0qGtMySc3FMyxb8aPKchLySNa5YkOeKdkFJ9Owf_lMehDCWZ0lguKoZlZsvPbmLEJPAxIPeG6gAuUC_401Rai8Y5Z0bGBHUbQf6NattTQdM582w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
هرگونه موفقیت عملیاتی در خاورمیانه، از جمله در زمینه محاصره ایران توسط ایالات متحده، با عملکرد نیروهای نظامی متمرکز بر مأموریت‌هایشان آغاز و تکمیل می‌شود. تا تاریخ ۲۱ ژوئیه، نیروهای آمریکایی برای اجرای کامل این محاصره، مسیر ۸ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68741" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68740">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=GmWGmiyTOM4ERP_VC7X_q5n75uTWgwBtEyGd3Kw_Umg7y01kTk4Bo3Cec1jxaLwfyuskpt89sucxcBUGNQMSsE4kXZ3PqZ3oKf8AX_NggFylcWQkazhKI4uUjdSaVyLVSBlpGyQtl4mZIfQa_e8FgvvLAyZ-zLr27mEwNd8CTTwBxs15Pp1WnIqhtaWZvE2XcW_LUxkq2Y7LtlxT1Gupnlx_inNPYbbGVHq4P0DLSuDm8FqSIXXfThT2QMQXVf6ZTRdJyWfytjgOca3FCtN5y2lHyxa_orKlMqzDlGd6AUVT-cP1UccQmxUnWB8O1KOZYLlVBNKu8S88RH4svEW27Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=GmWGmiyTOM4ERP_VC7X_q5n75uTWgwBtEyGd3Kw_Umg7y01kTk4Bo3Cec1jxaLwfyuskpt89sucxcBUGNQMSsE4kXZ3PqZ3oKf8AX_NggFylcWQkazhKI4uUjdSaVyLVSBlpGyQtl4mZIfQa_e8FgvvLAyZ-zLr27mEwNd8CTTwBxs15Pp1WnIqhtaWZvE2XcW_LUxkq2Y7LtlxT1Gupnlx_inNPYbbGVHq4P0DLSuDm8FqSIXXfThT2QMQXVf6ZTRdJyWfytjgOca3FCtN5y2lHyxa_orKlMqzDlGd6AUVT-cP1UccQmxUnWB8O1KOZYLlVBNKu8S88RH4svEW27Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
جوزف، رئیس جمهور لبنان:
شما رئیس جمهور بزرگی هستید.
🇺🇸
ترامپ:
ببینید این خیلی خوب بلده خایمالی کنه، الان منم هر چی بخواد بهش میدم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68740" target="_blank">📅 23:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68739">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇮🇱
کانال 14 اسرائیل:
سپاه سفارت اسرائیل رو تو بحرین زده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68739" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68738">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=CdQu7ectJDGnznSagtc4wMu3IT_y6S5f3K8WQB6WlhPJfvqAvsEvBA1HbHEO1ukvHCMEZebxHse4awiRDFvKYKMSLAHtQngEAgLjKhP-Fo2UU-FN_KY4XrQ3VdVrEbvcRRPtIwTATlMNOiY_R8o-fgS25_1__q04ukjkFAw36_RIfjAtmig6qkVVSv4_TzS6H4cnYW8MNN9m7zUNSiPBO6SSoCwbOD81cBzhExETd4sB8XFNcTNQnwasH7pSkh90tp9OwhPMuNJAYTz2soeBuMUr7vBeUeguI-s6-hW4eKeDR752KWCB7CCejBT8byeE9y9eJPuzwrzYNk66MDc2EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=CdQu7ectJDGnznSagtc4wMu3IT_y6S5f3K8WQB6WlhPJfvqAvsEvBA1HbHEO1ukvHCMEZebxHse4awiRDFvKYKMSLAHtQngEAgLjKhP-Fo2UU-FN_KY4XrQ3VdVrEbvcRRPtIwTATlMNOiY_R8o-fgS25_1__q04ukjkFAw36_RIfjAtmig6qkVVSv4_TzS6H4cnYW8MNN9m7zUNSiPBO6SSoCwbOD81cBzhExETd4sB8XFNcTNQnwasH7pSkh90tp9OwhPMuNJAYTz2soeBuMUr7vBeUeguI-s6-hW4eKeDR752KWCB7CCejBT8byeE9y9eJPuzwrzYNk66MDc2EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
انهدام پهپاد جمهوری اسلامی توسط سامانه آمریکایی برفراز اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68738" target="_blank">📅 22:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68737">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=EdXgxy1yK1aXBcEfRB13flvH_pYiAJCG-6wUDcREbqKch-w9AQG_yPXI3RmGGu2ZwLpjzERemT7Z_768-_Kat8Q5rdrOyfa7TtQrt4MhjfhPhdN5LhgVRf7BfXkZdmkMYM3v008LzeOR2YliCGNdSKmJ9TKP2FugWdXmCq4DJbjkwKBkvubn6lT-MgHhiRczrV8G7SnjuGwIEx9cO74duniglI2rCxWbRLAV1g2qIfJWi8DQ9olrnFgqpAgCvQ-0DpddXVpe9YE4ALujusLLLndzIpl7c4aQX1HuajQQHew2yNHRP0F97LwyHD-Hvu3EausFKX8te6_speby6KdSOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=EdXgxy1yK1aXBcEfRB13flvH_pYiAJCG-6wUDcREbqKch-w9AQG_yPXI3RmGGu2ZwLpjzERemT7Z_768-_Kat8Q5rdrOyfa7TtQrt4MhjfhPhdN5LhgVRf7BfXkZdmkMYM3v008LzeOR2YliCGNdSKmJ9TKP2FugWdXmCq4DJbjkwKBkvubn6lT-MgHhiRczrV8G7SnjuGwIEx9cO74duniglI2rCxWbRLAV1g2qIfJWi8DQ9olrnFgqpAgCvQ-0DpddXVpe9YE4ALujusLLLndzIpl7c4aQX1HuajQQHew2yNHRP0F97LwyHD-Hvu3EausFKX8te6_speby6KdSOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته دانش آموزی که ۰/۷۵ گرفته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68737" target="_blank">📅 22:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68736">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFVxei1iaBrSHBbkorCMVjAJvUJg56vYeEEoyOvqWasco_Hi5FcFVPaMQ3SURtxT4g-PMoZ-jhzVVwewajWlq47BdD8aVE-l8-UcLizFkc4mNWpVYUDzQ6xeQZ5EYB3_P7ckWWiUnMJltdeGbKGctfef7u4MHU3CWQH4Ob5_3Y75EbfEkSWk4sR1k9flgu0mkzRyUNn1MCBGvnvXrW-rhJPWCofp5l4UTezFGWYUY6dpwFlcIrtiPrw-nod8t393kF9C3rCnE8lt_GYTa-YI0plg0zVO5flBkeLTfci8wCY79T_jUfVKzbDrpPW0i76alzDZin2EEZiSrMeBa6-ETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به گفته بعضی از کاربران شیرازی، این اولین بار نیست که چنین اتفاقی می‌افته. ظاهراً چند بار هم دیده شده یه نفر میاد اینجا آتیش روشن می‌کنه و بعد میره؛ اما هنوز معلوم نیست هدفش از این کار چیه...
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68736" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68734">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8LtvgG1aGH54-r4RGAefydjMPzuQeOecpjuUwPg6iqIhYUO5FOACtFdAo_TAFzYF8HApCBCNtHh5Z2bYXtTJdIQWmHMKqEk6s0TCetLqZo81M2WyzFXMEbZR6oUYT1N7hn-2WksoM_PFzTQqiQOBmqMj8bURxNyfGc8NPv-fX2rO8ChQi6060nKLIUwSqmPSzcjoddPODUndfVaHzbzNktVTuZm6dlu3SjWA-KeJ9WyzW_1uIwqw_6PCdbmdw3ekaiY6b4xbJsfU8oGwnzRYwFGyHkHIIJ-u3YIWMjoVB3bX4jwCoHcS5w7u_EcQA_KhUuZuQl1i8SkMZZJhtPopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XOMVLLpvLNg53fSIvYLOoY1ki95Ud3uc2_ZChwZnzMEAccIcAIh0GaTBc6ayS82Ql-WG1zogTOy488roKoeIwh-uPzlEWRS3VSYvaxLrpRFiLufv-8sBNRSB5PCvj9lq8SaBWp3ulg954ckvIgYGyqnQ_US_YxIggToE5ji8KqCjGBFsye8-gVpBuDuEWSq7GJG3pRrTmfMPHVg2l2AE1NXeBAwBUfL-8lhtLfUXaFzqxniMmlqoGg830sE0s1zziSdsktLlU5LAjf2US04TElEh2dhSRRECkzL0g5_MbJxOjn0myrtc0FRnE2HYjk97YfKCW3AHhlzTGXwL6SY9Dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز در حال آتش‌سوزی به دلایل نامعلوم
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68734" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68733">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/upiEQZDgi2djulR2z4RVo4tVwoFDD7nb0bkzK5E-tN6OVu3RDmGaIlkOakvGuO91gWLMWe92WKEukiGiHqWcM56WN4afelrOAqK3_uVoTZdpTl69RBwF-AbkIyuLeOv5iid3Wi2qFp-oxrx0Fq37BMvGg7gxnrPwEPaLHmaTXydlYWeV7qNDoboMtrQtXXmkPgt4hsC4vEb-jCW5zVXav4ofYR03iTgOpvSVoAFO41ziNPJlkIWqC9V2uiAtsyHZjMRW0JGX7cmzcMyGO2tN9c2mZdEDfNwr856Bmq8lEtjUm8filO3CbIKCpCpAwewhke5w8A6my5vWSyZC7NOWXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گزارش های تایید نشده از آتش‌سوزی در کوه دراک شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68733" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68732">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=JpnIMRJj0kubNs3e-lBG4j7elwp7fEozrp-dS60Fb6Z-8IBQIBc2YZGmVubt9igD_3F5t1kAcbxd0nXJlri3fRPw23lW9lbqLGfTINqmnTHIw5yTlA_lpsB1xknbBoJDwaC72Yf6DtWY9qQfc9auk9-6pWBSoTe9BLzfS2urZ1UiWHtfMb5rtlyif2JGfqI6bMgO1URHoSuttOhk0Us-DYuWKgxg-yuTIQv382UbKUU6zy24JNhcA7ngEDXxdj2TvaktuspBhPMl78mAcro34rrUvS-FrxnM6UtFc26ArWSPHcXHyPvfbOh-7s8FHrwDnMvzOPJyDmfTJcJQ-wh2Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=JpnIMRJj0kubNs3e-lBG4j7elwp7fEozrp-dS60Fb6Z-8IBQIBc2YZGmVubt9igD_3F5t1kAcbxd0nXJlri3fRPw23lW9lbqLGfTINqmnTHIw5yTlA_lpsB1xknbBoJDwaC72Yf6DtWY9qQfc9auk9-6pWBSoTe9BLzfS2urZ1UiWHtfMb5rtlyif2JGfqI6bMgO1URHoSuttOhk0Us-DYuWKgxg-yuTIQv382UbKUU6zy24JNhcA7ngEDXxdj2TvaktuspBhPMl78mAcro34rrUvS-FrxnM6UtFc26ArWSPHcXHyPvfbOh-7s8FHrwDnMvzOPJyDmfTJcJQ-wh2Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چندی پیش، همزمان با تهدید رئیس جمهور ترامپ به حمله به «کوه کلنگ» مستحکم ایران، چندین بمب‌افکن سنگین B-1 Lancer نیروی هوایی ایالات متحده، خاک بریتانیا را ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68732" target="_blank">📅 20:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68731">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=SPTUBoZqzjiTaLoFreJqMMxtqeneGnO1CO2hPi2RGM1X94hKTokAlTfX32wPYhcnTW005ddQ7HjFSNbYIsw6FOXeRMak0xv4c2ZK91HdfF1y1kcuY9MZfKN3ToitKQakaI4DxsPid9DuoHBTwKqlZhbEpWDCo_T-GykGT2EZn5pPEnP0aBbLDWwHHUEx-HImMwjsvk_IQ5BQmURq8WbXFltTnorcY87mq9m9eUu2iQpc9vOYvbmoABdL3daxD8esbR8SA-SuDb8p0HmLPjKMvqlrn8TVKihtPU-dZBVFLk7mntTrNMreoeaJ8fIHIXe1IY-c2Ch2oRzWCtRVyJabJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=SPTUBoZqzjiTaLoFreJqMMxtqeneGnO1CO2hPi2RGM1X94hKTokAlTfX32wPYhcnTW005ddQ7HjFSNbYIsw6FOXeRMak0xv4c2ZK91HdfF1y1kcuY9MZfKN3ToitKQakaI4DxsPid9DuoHBTwKqlZhbEpWDCo_T-GykGT2EZn5pPEnP0aBbLDWwHHUEx-HImMwjsvk_IQ5BQmURq8WbXFltTnorcY87mq9m9eUu2iQpc9vOYvbmoABdL3daxD8esbR8SA-SuDb8p0HmLPjKMvqlrn8TVKihtPU-dZBVFLk7mntTrNMreoeaJ8fIHIXe1IY-c2Ch2oRzWCtRVyJabJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ:
به ایران فرصت‌های فراوانی داده شده است تا مذاکره کند و نشان دهد که در قبال تنگه هرمز رفتاری معقول دارد. اما اگر آن‌ها بخواهند به کشتی‌های تجاری شلیک کنند، آن‌گاه ما — همان‌طور که رئیس‌جمهور گفته است — ضربه‌ای ده برابر سنگین‌تر به آن‌ها وارد خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68731" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68730">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=OnNtaCgZ2P9rq9QcmhUgnARHQMLZiMWiJAFfIGR9AKIMO2fV4ZWGPdY3uAPQbw0eL-hW_mmz9Q22lyRg6_A_f1ibXU5aXoOT0NqJ1GmzZLl-OuEixuWBY0SkDcVfVKwJTN4Xg_Tc_4G4d3uoCm2k-Zh3dqQTio6ValUdse-RG_KwuoGgBm_FnNM8lZA19TpkqJvCnHxd-wZXEXI63Nnvlf_JL-41TK6A0AaB_RUGHKHWxE6va-eIvkkvzyjH5WqkH4JQqr_BaLq3-3LtdzghxomJzwtE5ezie_mCkGTmlsv-5z1LdaTHLKQi5DgVp1-S_D1fua9CAEjpCss_WOPkkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=OnNtaCgZ2P9rq9QcmhUgnARHQMLZiMWiJAFfIGR9AKIMO2fV4ZWGPdY3uAPQbw0eL-hW_mmz9Q22lyRg6_A_f1ibXU5aXoOT0NqJ1GmzZLl-OuEixuWBY0SkDcVfVKwJTN4Xg_Tc_4G4d3uoCm2k-Zh3dqQTio6ValUdse-RG_KwuoGgBm_FnNM8lZA19TpkqJvCnHxd-wZXEXI63Nnvlf_JL-41TK6A0AaB_RUGHKHWxE6va-eIvkkvzyjH5WqkH4JQqr_BaLq3-3LtdzghxomJzwtE5ezie_mCkGTmlsv-5z1LdaTHLKQi5DgVp1-S_D1fua9CAEjpCss_WOPkkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله سپاه که باعث کشته شدن دوتا امریکایی شد:
«داریم توانشون رو در حدی از بین می‌بریم که هیچ‌کس فکرش رو هم نمی‌کرد ممکن باشه. واقعاً ضربات سنگینی خوردن.
البته تونستن یک مورد رو از اردن رد کنن و اگر افراد دیگه‌ای مسئول عملیات بودن، چنین اتفاقی نمی‌افتاد؛ چون ما بهترین تجهیزات دنیا رو داریم.
ما تقریباً جلوی همه‌چیز رو گرفتیم. اما وقتی کار آمریکا رو می‌سپری به آدم‌های دیگه، بعضی وقت‌ها اون‌طور که باید پیش نمیره.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68730" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68729">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-LHfbKatFablR_Mpmy_h_qz7MMcfzgvRHQL6CUzdr5dVb0ZTmMsDVpdrWR0kBXzIX6kdRECLui-HVAN_hqdI31pAHspXe5BUaaVGH-mKkmjfAZQ8aiA5AIykkdGuNkET0z99u5OqQf6D8ABL83QTR8CmafdOTA7bcyaWLhXTaW528CzYhC_svHMboF0Rd8_4nn5VslkG9fo9dnXeN4wXPaioPl1EnX4C11zFV6rqCQirvB5aOEonuO9R0tO6vMSY-QSSj7vovIxHfnlJU87yCsz4DLraczYsbu5ZdtXE42usFb1cJiRgPSAtrGIHuGMMqqcuz9OQuWBYwwEHALAhE3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-LHfbKatFablR_Mpmy_h_qz7MMcfzgvRHQL6CUzdr5dVb0ZTmMsDVpdrWR0kBXzIX6kdRECLui-HVAN_hqdI31pAHspXe5BUaaVGH-mKkmjfAZQ8aiA5AIykkdGuNkET0z99u5OqQf6D8ABL83QTR8CmafdOTA7bcyaWLhXTaW528CzYhC_svHMboF0Rd8_4nn5VslkG9fo9dnXeN4wXPaioPl1EnX4C11zFV6rqCQirvB5aOEonuO9R0tO6vMSY-QSSj7vovIxHfnlJU87yCsz4DLraczYsbu5ZdtXE42usFb1cJiRgPSAtrGIHuGMMqqcuz9OQuWBYwwEHALAhE3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ:
«قطعاً به سایت جدیدی که درباره‌اش حرف می‌زنن حمله می‌کنیم. کل این ماجرا به خاطر سلاح هسته‌ایه و اون‌ها دارن تلاش می‌کنن دوباره یک سایت هسته‌ای راه بندازن.
ما اون سایت رو هدف قرار می‌دیم. هر جایی که حتی فکر ساخت سلاح هسته‌ای توش باشه، با قدرت خیلی خیلی زیادی بهش حمله می‌کنیم.
هیچ‌کس، جز خود ایرانی‌ها، نمی‌دونه چه میزان خسارت بهشون وارد کردیم.
اگر همین فردا هم از اونجا خارج بشیم، باز هم یک موفقیت بزرگ به دست آوردیم. ولی ما فردا نمیریم.
راستش رو بخواید، هنوز هیچی ندیدن. ما تا الان باهاشون مدارا کردیم.
من اصلاً باور ندارم که بتونن دوباره خودشون رو بازسازی کنن.»
🎙
خبرنگار: «فکر می‌کنید ایران سانتریفیوژهای هسته‌ای رو جابه‌جا کرده؟»
🇺🇸
ترامپ: «ما مواد هسته‌ای رو ردیابی می‌کنیم. اصل ماجرا هم همونجاست و به احتمال خیلی زیاد، خیلی زود اون منطقه رو هدف قرار میدیم.
کار زیادی هم از دستشون برنمیاد. معمولاً همچین چیزی رو علنی نمیگم.
اگر فکر می‌کردم می‌تونن کاری انجام بدن، هیچ‌وقت این حرف رو نمی‌زدم. ولی خیلی زود اون منطقه رو هدف قرار میدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68729" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68728">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=tJkYmCuVy3zXmdL7xBdDKDjyG40wfgrr-8e5wv39H9sy96ospfl3sDdXEqYsdyPEzV75q-8tJ2ToWZ-vLtdki0SggjNki84GqrhmnBXuPDOfKt2X7r6TGF7TRAY9f_uYSvuYi06NyqWZQJawgBFBThV9GQXsB0QCLOAFzyacKefqfl2QQa6YDn68WB_JozhS1BU97sps8w3Amlzgt5AvXpRGayXk9o8img9Y8nlCLk02Oud1MfPiP3Aw-CW4UGVVfRKNbpS9leNxBzhlMziFrIO6UjwjlRxfsmcN0b9yK7dSUWn0iszAg6xP1ZY1BN3MCsMf4OIwOrZGjTJiB222_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=tJkYmCuVy3zXmdL7xBdDKDjyG40wfgrr-8e5wv39H9sy96ospfl3sDdXEqYsdyPEzV75q-8tJ2ToWZ-vLtdki0SggjNki84GqrhmnBXuPDOfKt2X7r6TGF7TRAY9f_uYSvuYi06NyqWZQJawgBFBThV9GQXsB0QCLOAFzyacKefqfl2QQa6YDn68WB_JozhS1BU97sps8w3Amlzgt5AvXpRGayXk9o8img9Y8nlCLk02Oud1MfPiP3Aw-CW4UGVVfRKNbpS9leNxBzhlMziFrIO6UjwjlRxfsmcN0b9yK7dSUWn0iszAg6xP1ZY1BN3MCsMf4OIwOrZGjTJiB222_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ :
«جوون‌ها رو می‌کشن؛ انگار هیچ ارزشی ندارن، انگار آب‌نباتن. واقعاً آدم از کاراشون شوکه می‌شه.
همین‌جوری الکی مردم رو می‌کشن؛ بیش از
52 هزار نفر
کشته شدن و هیچ‌کس هم درباره‌ش حرفی نمی‌زنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68728" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68727">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=PeR6-0RQr2Y-PL21zTbEffcl3CbnRJr8pVpqfDOtjCVuaTR3KsX8MP0qU_nlsfroTVjQ_bIOH4iOazmtSr_xGpTtr6RSmqeLsSWCNAWz-1pA3gatr-5LmlUQZRJLukoFD3dwnGPoNQJVSIzoJj90dVBVNGNyQBmqxsXRmvW9bSVLsDRh4lELDxLopH3Gb9cHZcHvQN92Isd4bBH2R1YmURdo4eukol2yBuaOjOkXGJvNOkaCw5y0-3QPYeW1eGusoxShp9tzNrj8rfRrXyP5vOMEe6uHitP3fZLqrjFe4VORnGDfLffj8trLmqPOXrZffuIhbRhsPSCjDYRB1UMGtTJCbQQvtkQA5exxWk-_NItKIZXuCWv0plFmZwBH0Et2LvKGqV0_huGvdwUAYWlWc63DzgHvIBp2gEyjIqf6xvXbKCEOT_JMCBQtzk-K_x14rCBV-g99SDYQO4b0gMCepMwfjd06sTCS6C_KZJE8sSIKFFOAU2XSPp2suYkvLIa7zwI8xYLbqKattHhZLgFjztq7tCiXrMcbKSATVyGpSXVKThYBs2IaSGs1Dy0J-MwZHI3f_0479Pn0DXj4QvuKmRTf91T0D3AeghXctVdOPQ7-Vw1GBDuS1OtChru_jj4hZGRv45TsKFoDeqNNZPEN-EoqEzFGhZQplw7eiNA-M_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=PeR6-0RQr2Y-PL21zTbEffcl3CbnRJr8pVpqfDOtjCVuaTR3KsX8MP0qU_nlsfroTVjQ_bIOH4iOazmtSr_xGpTtr6RSmqeLsSWCNAWz-1pA3gatr-5LmlUQZRJLukoFD3dwnGPoNQJVSIzoJj90dVBVNGNyQBmqxsXRmvW9bSVLsDRh4lELDxLopH3Gb9cHZcHvQN92Isd4bBH2R1YmURdo4eukol2yBuaOjOkXGJvNOkaCw5y0-3QPYeW1eGusoxShp9tzNrj8rfRrXyP5vOMEe6uHitP3fZLqrjFe4VORnGDfLffj8trLmqPOXrZffuIhbRhsPSCjDYRB1UMGtTJCbQQvtkQA5exxWk-_NItKIZXuCWv0plFmZwBH0Et2LvKGqV0_huGvdwUAYWlWc63DzgHvIBp2gEyjIqf6xvXbKCEOT_JMCBQtzk-K_x14rCBV-g99SDYQO4b0gMCepMwfjd06sTCS6C_KZJE8sSIKFFOAU2XSPp2suYkvLIa7zwI8xYLbqKattHhZLgFjztq7tCiXrMcbKSATVyGpSXVKThYBs2IaSGs1Dy0J-MwZHI3f_0479Pn0DXj4QvuKmRTf91T0D3AeghXctVdOPQ7-Vw1GBDuS1OtChru_jj4hZGRv45TsKFoDeqNNZPEN-EoqEzFGhZQplw7eiNA-M_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: هیچ نشونه‌ای نیست که ایران بخواد جنگ رو تموم کنه. پس برنامه‌تون چیه؟
🇺🇸
ترامپ: تو از کجا می‌دونی؟ چطوری می‌دونی که نشونه‌ای وجود نداره؟
چرا تو چیزی رو می‌دونی که من نمی‌دونم؟
تو نمی‌دونی چه گفت‌وگوهایی پشت صحنه در حال انجامه. اون‌ها به شدت می‌خوان ملاقات کنن تا بتونن این قضیه رو تموم کنن.
اون‌ها به شدت می‌خوان ملاقات کنن.
تا وقتی که آماده نباشن به شکل معناداری ملاقات کنن، ما هیچ علاقه‌ای به ملاقات نداریم.
ما دارم اون‌ها رو به سطحی پایین میاریم که هیچ‌کس فکرش رو هم نمی‌کرد. واقعاً دارن به شدت ضعیف می‌شن.
البته یه چیزی رو تو اردن رد کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68727" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68726">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68726" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68725">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjUfPCcFPFIZ7mSMQDkd54v_zZc_OA75UArk_im47s4m49LfEvi3nmffNcML0X3LNn4W_iwuFAkEI1IN6CSqNh_kgsi_kaxY_gZOBQdTNz9vXC8Mee5ztvWOXfuu4HWiZ2sbTR-aMeZ8EU147-hOYQxcLPAsOspSut9M3j_TD9_e7fVP0I984AJi1AHEv3dkBv_2O3wdxuJj0_jMick6flFXOd6li088pUR15XwDr8qGPJuwzzRg3nhFdykS_2qc455CFfXBaVd66jqeROJApvTVHhF8s6uwO_Cge78HzEYH047KaiAbGyo7U_A_nAC0YK6T2BaEyvUpn1Nh_f8K6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68725" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68724">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=XYVKmm3hZKs4rNcYF-0LaW9tEYJTkJAPnPRtQm2qUfOkhXIrWwaaA3mO5oefabVkYnHc3oOuJxUnV-L4Eh02jo6dUH8SDkbX031NEJo4IT_yxMDq_bEzDi-1KD3H_e_gmlCvYAksDUYBBkqjvCnHOLKDtSmovxifxHylfklMTSyMke7VZvNl1mo7aT0HfilQpwl62hhZq2_NQPfsV1MV7wnvgUxfi1_HSQMWrxxisZB94p0z969XRk6v9y_NgaDiEWjR9MnIpxrccuHvMYPpH2W6OiEDwXyRLmdeIns7-rdSyCisyHWxcRfH9TIkdxWZwD1E13zp57HH324ngqaRpJBseV4ZDZlJU2MwaUsXS0SqYP5Ei4oczYkXB4BnKRbtrcs0yzPjMXmP5e8X-z_7UVT34QXfwTsfNh_bmsNCdRacG9ur-8G5TGPKvbh-r3rK7NSRxjDyxEdieXeWpVfAk9sQi0XgglDAzZDXI8ZkjkJMfgQKlKsjnBr_r_OxP48p7DURWPAt4eWAmGqmrGKH-jvvyJmuPY0rjVq9TTp9ST3rG62R4fm2smRiRSmqZWkZ0Oc9zv1LppNTKJR8OgKRaUcXiz9TUUKiklRWGEGk7ufBKrVx7hcBZyB9rWKJQX54SUGGJYjeKC8wd2FYgS4BqXp3nG2kEuFPaxsrHkSkEBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=XYVKmm3hZKs4rNcYF-0LaW9tEYJTkJAPnPRtQm2qUfOkhXIrWwaaA3mO5oefabVkYnHc3oOuJxUnV-L4Eh02jo6dUH8SDkbX031NEJo4IT_yxMDq_bEzDi-1KD3H_e_gmlCvYAksDUYBBkqjvCnHOLKDtSmovxifxHylfklMTSyMke7VZvNl1mo7aT0HfilQpwl62hhZq2_NQPfsV1MV7wnvgUxfi1_HSQMWrxxisZB94p0z969XRk6v9y_NgaDiEWjR9MnIpxrccuHvMYPpH2W6OiEDwXyRLmdeIns7-rdSyCisyHWxcRfH9TIkdxWZwD1E13zp57HH324ngqaRpJBseV4ZDZlJU2MwaUsXS0SqYP5Ei4oczYkXB4BnKRbtrcs0yzPjMXmP5e8X-z_7UVT34QXfwTsfNh_bmsNCdRacG9ur-8G5TGPKvbh-r3rK7NSRxjDyxEdieXeWpVfAk9sQi0XgglDAzZDXI8ZkjkJMfgQKlKsjnBr_r_OxP48p7DURWPAt4eWAmGqmrGKH-jvvyJmuPY0rjVq9TTp9ST3rG62R4fm2smRiRSmqZWkZ0Oc9zv1LppNTKJR8OgKRaUcXiz9TUUKiklRWGEGk7ufBKrVx7hcBZyB9rWKJQX54SUGGJYjeKC8wd2FYgS4BqXp3nG2kEuFPaxsrHkSkEBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای، (خرداد1384):
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68724" target="_blank">📅 19:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68723">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
ابوالفضل بازرگان تحلیلگر سیاسی وابسته به حکومت :
⏺
بی تعارف نشستن منتظرن جزیره بوموسی و خارک و لاوان بگیرن
دارن ماه ها روش تمرین میکنن برای اشغال این جزایر
برای اینکه یک هفته دو هفته نگهش دارن و یک کارت جدید بزارن رو میز دیگه برای گرفتن ذخایر هیچ مشکلی ندارن
🎙
مجری : یعنی پی تلفات انسانی به خودشون میمالن؟
🔵
بازرگان : اره!
اولن که تو جزایر ما هلی بورن بشن ما متاسفانه باید از خاک خودمون جزایر خودمونو بزنیم
به ویژه بوموسی که فاصلش دوره
اگر صبر کنیم اونقدر که برسیم به جایی که یکی از جزایر گرفته بشه ، بگن حالا اگه میخوایی جزیره پس بگیری باید تنگه باز بشه ، تنگه هم باید تحت مدیریت من باشه یعنی مثلا من باید بیام تو بندرعباس پایگاه نظامی بزنم و ذخایر اورانیوم هم باید بدی
الان میگن تنگه نگهدار ، ذخایر بده حالا اون موقع فک کنید میگن خارک یا ذخایر ؛ دیگه اون موقع مگه میشه ذخایر ندی ؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68723" target="_blank">📅 18:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68722">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4T6yPziLlLv7i86MZIsU2W1hJ5qBLn6aBe0tR5cKv-TRlJNni6xsI0g5J0MqF0O3Si7e_1Thrq9GMKdev7h6O6PMa3FVdpl_TvtWW-i1tuVeWaDvLmBTXX6K6KzNZY1Ha13ZTaHvXPKFTv9CSTNkMqS9OwCNaIzwVE3zZwjTkC_AG_q7mb-1YaQqjIgZ1l6sFj1kWmZQd0CZlAeBGDMl3V-t5p1v_DmY82JEYgdBmtj2ZryvoKtpYX8DxDBTZaiIqHTb_Wks23OABpTd5aHswHq_N9sP0DoKkQLtFyxnfd8GYT9fidtTwlBQVvc8VITQ4jGAhXvYMsgOQP4nx2loA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:  این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟ این گل‌محمد محمدی، 23 ساله هس. امروز صبح توسط حکومت جمهوری اسلامی اعدام شد. تنها. بی‌گناه.  @News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68722" target="_blank">📅 17:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68720">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/KlgZLescYQjZffM_km-Nyo_HoPadYKEq5v_SRD9xxpR64RmmC9Ge65idyUePdky9vBBtCdLJRXRDryyvGy0J8XP3YSyuErtFTyn0pG9IW5GyN0Zs65NZ0wKiUvCaV2dD1EpiQPOstAlcWG0o35dFXFsemOUx0bCoar7rTiomT4sOWexPLVspSAD3JXM62IkYp7Ikp6JY_xoHU3J6EnBMvFLerq8sR5fRmcEXVMwLhPhozm2QfYOO5aWhaOuz7JXFLseNPMHq8ECLV1rDRvRBrmyAjRze-zyWt-InniH_4NwJsPjFlFfTmcx0sav1tS_BaIqy-BzfYFsgZxivt0zmAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/HjzEcyFUUrMyDikMljKNB7s-gDTgIZdRYFvppC54iNfMa8vLJlQaQY_3YN7JPRIBDsS-YIz7cugX-JggMb0NVBNLhCd34yilA_bc3sB9MKt6RMO3ZZWme3NWQ7Wosk3nn1Qw9M02YHBnPYoq0xVfTC272lNqwvbye-fkSJ4gt4Jy0TgVABHcAVplwweuNEiATrbxL5YRvB_OO_eFghRycNZb8x5ljtknOa0sIF50wGr8bmKI8ho6A9udZyUqVinE-NvAHWg3fGpV47ZhhDwnGGNCyb-1630sBXiLaiaUWfVUVgYE5QogDXDR4kInpnGPtpbA8K3EKUP2nhe_6OUECA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:
این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟
این گل‌محمد محمدی، 23 ساله هس.
امروز صبح توسط حکومت جمهوری اسلامی اعدام شد.
تنها. بی‌گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68720" target="_blank">📅 17:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68719">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=qJDVUN6xBQA_K9Q5_wV3eMs7MZWb68H9I846u6pfwy3HjqBG8E775dTkjl1UPZzYgb_OVsjmSxfSn1HcTyrWl6fOrnXxX1h_HhjdsTksE8VMiXexIgwIPl9yJD6zZQKcFkipQ-hNVkvj1qG4gFt3zHJJ8L7vLKgWLR_MV41bqlTSsbOTRZNdwI868LQ8d6ZYF7OouNJH07If9k4AkK5eZSin6TyUa4-HoqDZ50I0jlU9wvUwTCeKdpCVoaxnnPjFdrJVpn41e9xot1xQpufwYRhObrKGx4PgQKCtP59gVAWj1bsO1TNeQTOXqs26lWSiV7MARbxK7eLe1wzUvZc1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=qJDVUN6xBQA_K9Q5_wV3eMs7MZWb68H9I846u6pfwy3HjqBG8E775dTkjl1UPZzYgb_OVsjmSxfSn1HcTyrWl6fOrnXxX1h_HhjdsTksE8VMiXexIgwIPl9yJD6zZQKcFkipQ-hNVkvj1qG4gFt3zHJJ8L7vLKgWLR_MV41bqlTSsbOTRZNdwI868LQ8d6ZYF7OouNJH07If9k4AkK5eZSin6TyUa4-HoqDZ50I0jlU9wvUwTCeKdpCVoaxnnPjFdrJVpn41e9xot1xQpufwYRhObrKGx4PgQKCtP59gVAWj1bsO1TNeQTOXqs26lWSiV7MARbxK7eLe1wzUvZc1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمعات شبانه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68719" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68718">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ5zXotleyNnr-mGYgkCrlU_M-EcHSZCfk_8yfw9Q2xVpnfVbW0I7IPX5RzGDf-mhJkTCQ-JmMPIamyf71W0oHvazL3t1J30QtSYhAa7CttwNXCga46bINMvNHiAaiOwa9gmgc6TJwl6pss_pigXiOmhvTIxr7VbVH-fEuDyVyXdo5e2S-YN0QJfI91OgyLZH3uLd9ba4PLTnbS7E2cFjV1LmxClnv1N__C3uDrqTK59zh8VawCfbC4Ku-QCZequQc4pz3baFxLuAccQjipdiQkynXZVyXt1ZFIjvJHuK4WKT4lm1_p6MbrWnnRRretx9EPfR4HgjQQHaKDchf3czg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هویت نظامی آمریکایی که در جریان انهدام کنترل‌شدۀ یک پهپاد تهاجمی ایرانی در پایگاه هوایی اربیل در تاریخ ۱۹ ژوئیه کشته شد، گروهبان «مایکل سوینتون»، ۳۰ ساله و اهل فایت‌ویل در ایالت کارولینای شمالی، اعلام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68718" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68717">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da37587eed.mp4?token=Vp2eRre7uIqwaR_D9J0cQX2HdyCLXiSo1YWpLLevEdML_btUqezxSmFKU7R6fubOjDjROUwLGzIgLc8vFzTDl3OjcFrSo8_WQtcICFeq80gY-WFL2A3PQL3z66TUtXrljLVt0Jh8j1LIHupexhGvMVIl5Plwg3A0abP0BcM_EgB_g6-LG1KSq1jQbnYTfbmF-bV3fTTtRRX1NGEulPN5ih1bOj346yttdVJe_FHMAzv8hs46PJeNbUUyHaEaiOvKoWArZHHg_5G3MqzOgTx9PHZAnaB7Op4W0U8V4UaIqAlZUaZLonmHaW7Q7kVCR-wt1iFNC60UqGQC_58ezt3g7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da37587eed.mp4?token=Vp2eRre7uIqwaR_D9J0cQX2HdyCLXiSo1YWpLLevEdML_btUqezxSmFKU7R6fubOjDjROUwLGzIgLc8vFzTDl3OjcFrSo8_WQtcICFeq80gY-WFL2A3PQL3z66TUtXrljLVt0Jh8j1LIHupexhGvMVIl5Plwg3A0abP0BcM_EgB_g6-LG1KSq1jQbnYTfbmF-bV3fTTtRRX1NGEulPN5ih1bOj346yttdVJe_FHMAzv8hs46PJeNbUUyHaEaiOvKoWArZHHg_5G3MqzOgTx9PHZAnaB7Op4W0U8V4UaIqAlZUaZLonmHaW7Q7kVCR-wt1iFNC60UqGQC_58ezt3g7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شاهزاده رضا پهلوی در گفتگو با رویترز:
«دخالت خارجی در ایران لازمه. این مداخله در واقع می‌تونه باعث بشه جان آدم‌های بیشتری نجات پیدا کنه؛ آدم‌هایی که در غیر این صورت ممکنه کشته بشن.
جایگاه من به‌عنوان رهبر دوره انتقال اینه که مقصد نهایی نیستم؛ من فقط پلی هستم برای رسیدن به اون مقصد.
برای اینکه بتونم نقش یه داور بی‌طرف رو داشته باشم، خودم رو وارد هیچ جناحی نمی‌کنم. نه طرفدار پادشاهی هستم، نه جمهوری.
وظیفه من اینه که مطمئن بشم یه بحث سالم شکل می‌گیره و در نهایت، این مردم هستن که تصمیم می‌گیرن چه نوع حکومتی رو برای آینده‌شون می‌خوان.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68717" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68716">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68716" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68715">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rydvMsXOunC6LHXzHR_B_vOg7OHCJXkQH6sXIvkBwAXqYNjD0oDTwYyDs6QUOU2Gaig1UfM8J_F70quQRooq2o-p2EqoAQx6bHhOqX3gfYfyr3-Dl8xUE5H6cJrafHyaxy1GjtKcpcltYRcPw3p5ti5Jo2mx13SG86TqU7_05dT-x8_otLEVW80-JLLO_N-hsaKWUqsiuYA6Gl5_rsLVjnj9a9AwMh62HBnJXqCBsfNOepRdWwcbD6vuZ9YK5-L4NZyzPD8ZjOZlr8wRk8Z78OGvNutm0A9pUYOH8SG-RIKJ-PgjOqyLOJP52DBJ8wMpA2SWgHH5FA1RVmIraNmDqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68715" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68714">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhkGUpdUu4gt91Dg7RqQix4Vm51V8lcIKR1PEQFljJzepn6MAFaEwxKa4UEbrdyX-9uUrE_nS4vNh4kM7Lt-zQmxq6I9btZIcYbC7EIYB9fbJ0Kv-SVqa_NFp_LAvlKQyacMN04oD0fk2nJV0mzozFtZw_YzZCmSXdx4BH74aUFTZOT1N_S7T4DzcyGK2TFIoJAGdSum7IC3cMtlG8OVnkbjJmLCvdnzTzN4OB79fYnApV5pRMj2M9PD_5DfVOoKFP2LQUzSE3GSLW86fd-Y9w7yJl-pLr4VTqdLCIriSdWEbvyIj2U9K4CTAWcrms9ZOjbC_S2_Hl3jBXTO3IJLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مراد ویسی، عباس عراقچی رو فالو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68714" target="_blank">📅 15:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=mC_fFE9fhxFeOWXvi5i5682HkKFp7miiHQuHI3pkJQyNCyQ8zcqv5Exx6_NL91sViofjoJh7p9WQS9QFxzD41ticZ-GMq7eWVrTq51eJq4BZqZnpv5pBLh6xRiUadv5dzF8KWVFRL_ZtpTZEAlAX3fBjiYJM7CvkEJ7B5f5EYXYZgv5B5ydqtnAe4Oua32XAxA8t61O3Dma-wiUrtithb5dZKiXh4oFH_-OK9-JweVPqqXEeH_Oa7m-RaQwjtfxdap-p7SlEP0KZsbtNlM9u4uWCr_sRqETJd860A_75mEyXxqEAPEwY54Y0KFH5Pf1fhyZnpvxmcIYOXXFEpF2d-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=mC_fFE9fhxFeOWXvi5i5682HkKFp7miiHQuHI3pkJQyNCyQ8zcqv5Exx6_NL91sViofjoJh7p9WQS9QFxzD41ticZ-GMq7eWVrTq51eJq4BZqZnpv5pBLh6xRiUadv5dzF8KWVFRL_ZtpTZEAlAX3fBjiYJM7CvkEJ7B5f5EYXYZgv5B5ydqtnAe4Oua32XAxA8t61O3Dma-wiUrtithb5dZKiXh4oFH_-OK9-JweVPqqXEeH_Oa7m-RaQwjtfxdap-p7SlEP0KZsbtNlM9u4uWCr_sRqETJd860A_75mEyXxqEAPEwY54Y0KFH5Pf1fhyZnpvxmcIYOXXFEpF2d-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68711">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMipHRbDhz5T8uooQdlo9m-4N5tEb2DqvtCOaXP0rwKQFIifRfLmdodYMHsTIhnyMTspaoY9nmdH4V0T9HOKbTU68m3N3_VD-NBGo3awm9nOKzdNGRFbyNiBSoOdYtLLYjKVz20mCFMmwbFq1ALr_eZRlJVHDtGMfOBupw1D8MNci12Qse_0TeWAIp5jT8POux1r5lut1MmHWV9ckXwwgiFe_2uG_n53zb80WK1-5HuKRizgC65KxJfKbjG1dLVbPOt-QQ0BosnhHdALqo4c4uD4LqJ2uTUAG8BvH-ChucnD_b9lhx7aHUMaCg-HAZCpBme-KaWbKALlzmNq6d2bUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
با اعلام مقام‌های کویتی ،  چندین نیروگاه برق و تأسیسات آب‌شیرین‌کن این کشور در جریان حملات روز دوشنبه جمهوری اسلامی هدف قرار گرفته‌اند و دچار خسارات عمده‌ایی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68711" target="_blank">📅 15:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68710">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=DaL3V8ZZFBW4mrNjtHuG4KUyn1karZW96BpgLlBDayFi8BRmkJ9OI55BaoZsIrJqUMP8KRKvE7od2Sd_2IihMcXtD8_RWSJEHaQOvJ-9csAs4zWMY4xRdLR4QV_NpDvit3ObX1Z76_VUP9YALeFdFvzOKqfnRyFH3-sUQqLZMqTruQ9KihFstWUtoJZvcIFsBZhopFt4LwCG_5rIAEhdfE-dZR7NomPzedqFnVAUplJsXvlH1L0p8neCFmacgutouxy7V_WTiMC1MF2kzXQkUyudncCBRWeIZV7IcDwxjY2GSxvIz2atVcV-k4E8RBdzIA-nTB_K7BdL-xNyDceYMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=DaL3V8ZZFBW4mrNjtHuG4KUyn1karZW96BpgLlBDayFi8BRmkJ9OI55BaoZsIrJqUMP8KRKvE7od2Sd_2IihMcXtD8_RWSJEHaQOvJ-9csAs4zWMY4xRdLR4QV_NpDvit3ObX1Z76_VUP9YALeFdFvzOKqfnRyFH3-sUQqLZMqTruQ9KihFstWUtoJZvcIFsBZhopFt4LwCG_5rIAEhdfE-dZR7NomPzedqFnVAUplJsXvlH1L0p8neCFmacgutouxy7V_WTiMC1MF2kzXQkUyudncCBRWeIZV7IcDwxjY2GSxvIz2atVcV-k4E8RBdzIA-nTB_K7BdL-xNyDceYMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ها؟
درست شنیدم؟
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68710" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
