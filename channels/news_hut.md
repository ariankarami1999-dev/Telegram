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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 22:28:39</div>
<hr>

<div class="tg-post" id="msg-68818">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4En4EPSGK8G67LtxQRuTXETtxndrFLs0MIRQSi9zaq_qyF1-Hq0M6Tw0iGiTaHbvAUlzv0Oxx3qy1qIyXkSn6k5ivo7BkxcIaQXkJ_keiKJ-aTjI6VH5Rxnc5D6b94UQD1DTyKEAoS1rOfGe9kfAGFRcz38XuKAq6wo03WUq4TeeTQQxpZylvPuc4EQqq9MzfVUMWIA4cN5-fVKJgZ4yE2PTrXgPDoot3nWBhGHgjrrDVikkqYEqS7GQDEJZffhKqJMqqfOp_CDxYhrWbmHSB_Np-_DcWW7KWH39ZffS0p1g43dppe1OZm5YpmVUlTJjJSXt4gTsGAb3F9MXEzsBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مجید موسوی فرمانده هوافضای سپاه:
اگر به پل‌ها و نیروگاه‌های ما حمله بشه
خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعیه.
@News_Hut</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/news_hut/68818" target="_blank">📅 22:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68817">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=mbZprnl3NE43ceJNMgQJzNEz86w2XxMXNpWQ-ij6_wmQQxQIJtsweZ9OkI1Fe1HKblTSm6Y7YtsIxGH8HYq_Z4ckeh5bDgG85ECeAtvsHupK0pm_2ktDR-1wrMBbycOZvLn0Qwvj9HkvNWPt2Dp_8E75q4RLK_0LZwBN-N1-6OHajq3t3xr-gq8NX2Pigr90QTKJgoWDMajjYP6Db1zbpee0C0Nt-A92YZxlfMYqepPU1mTUoMFEc44P5v8TDY5cJxAOQfB3UGWqowAWZZhkYBZj68zc5KHlWk5pXjMSDF1SAIuri0BzhHGkP8MM6_r3L9Er6q92sZdo89DdHY43qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=mbZprnl3NE43ceJNMgQJzNEz86w2XxMXNpWQ-ij6_wmQQxQIJtsweZ9OkI1Fe1HKblTSm6Y7YtsIxGH8HYq_Z4ckeh5bDgG85ECeAtvsHupK0pm_2ktDR-1wrMBbycOZvLn0Qwvj9HkvNWPt2Dp_8E75q4RLK_0LZwBN-N1-6OHajq3t3xr-gq8NX2Pigr90QTKJgoWDMajjYP6Db1zbpee0C0Nt-A92YZxlfMYqepPU1mTUoMFEc44P5v8TDY5cJxAOQfB3UGWqowAWZZhkYBZj68zc5KHlWk5pXjMSDF1SAIuri0BzhHGkP8MM6_r3L9Er6q92sZdo89DdHY43qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ظهر چهارشنبه؛ لانچر مستقر در تپه‌های پشت اسکله طاهرویی (سیریک) که روز گذشته مسئولیت شلیک به سمت کشتی‌ها در تنگه هرمز را برعهده داشت، خود هدف اصابت موشک قرار گرفت و یک ستون دود از محل برخورد دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/news_hut/68817" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68816">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhh2P1g2To555iChL4dtdwa72oF9Vvq1NuhAJ5hu7ZjkcWc-mnLXR6szuRJhTHHk0HNgiroxvsrJZ7DslUW6GiqP6Acc7zAY8-NYmg8V1qM9vBPh5Vobfm_Ap4_SCK-bWnSymxvEPUytFwKLwnjp6u5h2nOBouGABJ8IHZNRP-VsRNHo1VEFQyYZdoMsL9Hz0rQ41DCfhEeWUN0SPgqUrRp5xJazhIKVMJPOg1RbiwkWvl7sKZvEGpq-cHwanAZeNjyN74dDkrwfynQLTkbAWsKlelj1mRy9o1uB5De-JaHTQJbfZVty4dpQDPcofoEOQYYow--bLXaAJzkwxWn-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت.
اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است.
بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68816" target="_blank">📅 21:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68815">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA01D8uzQ1YgbxtZ5cTj5gDULEM555B0oi4gxYYPtMzL4xVXDeyyxbl8Z5J8BvQecElmuFY-m9iNm8Kfv0r9MzHj4BnqEwsdpbW2WieS6N8xFI_tEbVmpy0wrTZuEguCMED2gtoeKPjPsIhZCrH8eY1PCmMIqQj4-0MGgFvV3EL06JnH_3YPvLbKUTMW94AYWRK1qmEG7cq5ZWhy1kjZt6azvBMjEwHalShPtMnfKLBZxgpkSdAW1SPcM9dnBbSNVMinRORsbP5c1igZv-hzotUfuH7iUrmI_04Xr4op6oJReZZCudMWnbOiWcvEUQcrFBVP6kjEc6ezw_rF5mNFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال:
رئیس‌جمهور ترامپ به‌تازگی اعلام کرد که پس از کشته شدن نیروهای آمریکایی، به «سنتکام» (فرماندهی مرکزی ایالات متحده) دستور داده است تا «درهای جهنم» را به روی ایران بگشاید.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/68815" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68814">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/68814" target="_blank">📅 20:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68813">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7YwCvMmYmxmt_NDTvOkfT3KeiazKoeZs2xlolK45G6-c5-iE-LqUgxXcAlkpUDJibtI-qR8pUh0nPrBWsG3Tn2oJocveCm6cLt5DsufgAm-6tb4AjbVLj5Xd6wImob-8BL8TE0Gdi9VZvBzVbnAJF-k4tiKs0K-pCAgca4Z6Mvsg1pY1ZMYSUzBoSZ2uVM62YkKdSnD-7kPS6YWoJ8bWVDOph9FGaA30Wd2MN5KGl8OAuWrU7pJQXqjtOV-iI0AnbvX0KY8pYhkSV0mlsVHH0NFoMk3JiWmxYPmAhdnjUc5v8ZgumCinnVyZIvNZfZPfC565g9jFY_93Uj7ceO6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/68813" target="_blank">📅 20:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68812">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJJuU-s11crr5TX7rTUMtihwPFy5sB0d6UOaTn9cn4SAZDKgXTeP6byiWSTHBk-sW6Ex7iakTBh_g1he4-lKr9y7bMkrAP5op96T6Czk_yTLVPOscuZIhZ_N-L3h6XLoqZ048wTQM6Cg6u3DWNR-QmwDCgSpkcwhDIUwj1jUcY3BM1W9HZqHgHRSFWmbpYA7UfYp-oH6eeMtKnOxN4X_V_kAYCP0LKx7PfFbYUA2ScND1d3EynIa0dlQcR2PJUwpTWEvHymL5qlm3X4mEJnWZvxa2gPjXIOzStbDbBx3JEb9AVQ3luiC-ma3gfa0X4AejJ-YnLeOlpLCEq8ZW4yD5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یکی از حملاتی که شب گذشته توسط سنتکام در جریان یازدهمین شب متوالی عملیات علیه ایران اعلام شد، بخش نظامی فرودگاه بوشهر را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/68812" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68811">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGNczzS8NpQb1ezGozI1BCdJlbvvkAVYdIhr_v7jBNU-3NZJm2nIpeLDPUq4OjlXkGCcvQ97v0cs6SvkVFyOhs-HFoMSWCjrbprk4wLaqZvNTzUIFauqx1uHtFLFscicOKl3hmftYoi_fj2H4iMHexmlPBg0k-6k89o-wB2bm9iP7p6axl3M7xGZJ56woEYaNk13MzjbSPHRXSl5KcAyI4sHnyZz7UobSmMr1sMB0O0LYNAvalCL_Acm6yFQR4lgHAyGbp_XMW0YBfjALOmQdLJDYfiOiJwL-_i18j7lfB4gVxZU8ffPWDw5yklebD6ybrh-ekH7qZ6knFVi9pFM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
قیمت نفت خام برنت به 93.14 دلار به ازای هر بشکه افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/68811" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68810">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68810" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68809">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68809" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68808">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68808" target="_blank">📅 18:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68807">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
یک منبع نظامی به تسنیم:
هر پل و نیروگاهی از ایران هدف قرار بگیرد چندین زیرساخت و تاسیسات انرژی منطقه را می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68807" target="_blank">📅 18:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68806">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:  بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.  @News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68806" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68805">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68805" target="_blank">📅 17:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68804">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRKDgQG7yrNvq8T61GwBwB1PXd8qJOO3WF0LFMvDLDIp9rfEHt2JL16p_h-nagSWYbyVNnkhDLUt2oSRfQRKFI-8hG3UaUQCmnR4X1A0S3BVzoP9MsYxrZhtjwXFLk8WP8QfHob-sbRxAafKtjRmHBg4VPMrSxp5_l5Zy3MUDZsdt_-07NbJhEimXZ5VTnQoD_jMEI9DkTD3_9owLDf5wxg0cgmS0-28vCxzZ9PtKy9CjjWE8-isBOV5vtLJFzrOop0EsydEkxdnWfzuoPvhBF_nk7MyVGC6uzB8A9YSYdAQ3rJroIra0gsNHd6kUUk44uVp9pu5_LNoat0ZIlAQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68804" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68803">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSyYem9zgZQJE0NwiXY__CFPfgyn17MvcolECKZJQrwXxl-bV6BEBARPhMJUJ-_Ie_lR11U9B0nn4UdqrdnlV3kUwJDGUwe7NDIewDEgX7lEqwWO5FIaqz9YeHiSfS2wHBB-AvIpsH0D1I9mlTdwf_yYNxaEWTjjYiCTlvghdmZfVlFL4OHUaYPH3rxR0la6RmGf5xni2DN_em0PNkgVD0zCVa7fupkN53n3MAiquTrGvJmqZYffC08wfMsgBjouCD_1i-enE3ODY-xyvjKCt8qtoMSTBANHAlFo2B_lsEbla_Z45LSISK7BsQorQIXecdBSnSqT7ADqAauynpoTJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه
حتی اگه نزدیک تهران یا داخل خود تهران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68803" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68802">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68802" target="_blank">📅 16:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68801">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⏸
ویدیو وایرال شده از گریه های یک دختره بخاطر مردن سگش
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68801" target="_blank">📅 16:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68800">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏
🇮🇷
سپاه پاسداران:
«اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68800" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68799">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfPi8-2vHXL_Hy1Rx8B2gR4Annc3Q9geBA1CONXFF1eakcGpp4sXfnLgQpMCH58MtrH1J8clR752c7WTIS7IgjzSTvqWaWr3XOWdB8RiH8EYaTUq9uL54rrVgKnuAYn8R_x0WO4ID0JA6Q7vm7MFB3eSmVBTcBJ7y1TkTSikt2N1QcermAs9usLRntcibi7QAMQh459uiF1mfiDi4yLDZzhmK4dLc6N2BZj16LvEoIfyldPpe5xaYZPt43uMprIlChBSTV6GZDFazg3NGLAQmJwUNY7AvKCmyjqjuAIZF8sraiSxRyd-ubamCVe-OFXdwXGP8WHqlGI_pEo3xBLOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آژیر خطر در عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68799" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68798">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران به بحرین و عربستان سعودی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68798" target="_blank">📅 15:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68797">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68797" target="_blank">📅 14:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68796">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=A-Lh_FqrNGSRr7Rq24lZZwIZ4fQ2X7j3SOG0idBUMatlzOdek8xCofKntSZIVGY9w1w_mm9azqgWqVxs1KcBrUiqkkSzD_j0mc7THHggnNoFeeeoui_REJndowFZbe5aywpLkjff03bJPp-xYIn66lhWzoGPUYPCXMDphYvxmXHCnjKqrKu199H4fkNX45UAJQqQfI7TkvnfkXi7BV5MyGN6EDHvqueeNa1zTlVfBIctq3qyYVYYof2rIMlKuQ6c8GjwXS-CQ03AwFl5VEuRogzWCFN5z077-gkSzvyH2u2PR6ENhDeRyy04yTotfuMPESy6jtkjIPMF2IP2mcTvhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=A-Lh_FqrNGSRr7Rq24lZZwIZ4fQ2X7j3SOG0idBUMatlzOdek8xCofKntSZIVGY9w1w_mm9azqgWqVxs1KcBrUiqkkSzD_j0mc7THHggnNoFeeeoui_REJndowFZbe5aywpLkjff03bJPp-xYIn66lhWzoGPUYPCXMDphYvxmXHCnjKqrKu199H4fkNX45UAJQqQfI7TkvnfkXi7BV5MyGN6EDHvqueeNa1zTlVfBIctq3qyYVYYof2rIMlKuQ6c8GjwXS-CQ03AwFl5VEuRogzWCFN5z077-gkSzvyH2u2PR6ENhDeRyy04yTotfuMPESy6jtkjIPMF2IP2mcTvhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68796" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68795">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68795" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68794">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
فارس:
دقایقی قبل صدای سه انفجار حوالی سیریک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68794" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68789">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68789" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68788">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68788" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68787">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68787" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68786">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68786" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68785">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68785" target="_blank">📅 12:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68784">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olXk5llOKYXS9LY50Aoe_rVgmnSfn40GndUiHhRILP0DVb2LMTa3FVB37QjzgMTqRPthJq9K8HBtot-LncEm0njKXdaH_e3B3qH8EwRQYmTAI9PMwoani_An_Bm4Yg5JmPpw4UEnPeyvZAvvq8LcX76P_nVEaeOrke9OWSFfkipUMu-10iR6Q3CMKXrgXTMh4lswjf8t7SqvXMIUD67IcRtWf2j2_jvvFw4F-lgH4wbflzyUvRKP2yHH3ZTBU3wZIRjKggS594RPxznz9tiTFMEjA03Y91JgSL2W8lQisOwqovslkSSE4vUDpIppCBJRgSO8JuMPYrRGFj7rKZE5_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
شلیک موشک از کرمانشاه به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68784" target="_blank">📅 11:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68783">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=Q_5FnYezcedZTe-qZGw5KJXSuJwNqUQGWw8hjP6NLAz9Ea6JaMxU8VAHs5dBDnOhUw1T4OzszftSRBC4qg-kG16Enld2_YPwlCV3EvdS0Vt-O1luoXn2cyC56wq2DQaUE0WWQoeZd6xaLGa7QD5NYQ0ZTMFCU_k4HXiYVz4wPd5jpZMG1LzPOW6D1-JTe0cAcdhjUdN0tWUol_8hgPtlxOpShsrAVouapb1fbrRoBwRc3aDCMmdWP_QhsgNufs6WPxbLaJXHIIF31ZwLGRrsjBvkP0A3oRBbERZr_lLlHaWTm3GDSAiHYNYxMLtvxO0xkXjdQvpoVFQPIw9sut5DTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=Q_5FnYezcedZTe-qZGw5KJXSuJwNqUQGWw8hjP6NLAz9Ea6JaMxU8VAHs5dBDnOhUw1T4OzszftSRBC4qg-kG16Enld2_YPwlCV3EvdS0Vt-O1luoXn2cyC56wq2DQaUE0WWQoeZd6xaLGa7QD5NYQ0ZTMFCU_k4HXiYVz4wPd5jpZMG1LzPOW6D1-JTe0cAcdhjUdN0tWUol_8hgPtlxOpShsrAVouapb1fbrRoBwRc3aDCMmdWP_QhsgNufs6WPxbLaJXHIIF31ZwLGRrsjBvkP0A3oRBbERZr_lLlHaWTm3GDSAiHYNYxMLtvxO0xkXjdQvpoVFQPIw9sut5DTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
‌علی‌اکبر رائفی‌پور، ازحامیان جمهوری اسلامی:
با شناختی که از سپاه دارم اگر نظام سقوط کند، سپاه پاسداران موشک‌های خود را بر سر شهرهایی خالی خواهد کرد که به کنترل طرف مقابل درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68783" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68782">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=ZhJO2tfi0iULlFVDCrkb7UJYaBdizXLTCj4Q9B4wLo6EGkbsLlHld-hkuKvqG2Wd7f1SPBg6lL72EYbw8V3B7blee3aMRdgVpdQPx0SYk7Bh-Un0oWCm-7obgL4lxG0DEFIaUhmj3Uy0etjCnEOWVGt7l6qsei35q8OAUqJhS0pMHQaBTqCiR8pOSFZ9xfyKRylFyb_-gj8hvOxdp477cqAUm8IeG_fJ2RiIrYPV1IhxRFw4nm2fefoE-C1d65imJAWk6tvnqNhsHp9AONhsKVjnBmjt0gqgKQMso0_yxrlgww3Z-cW2RCKgFPQdx9MH6ApAA6PSB86xRLaqxmDNNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=ZhJO2tfi0iULlFVDCrkb7UJYaBdizXLTCj4Q9B4wLo6EGkbsLlHld-hkuKvqG2Wd7f1SPBg6lL72EYbw8V3B7blee3aMRdgVpdQPx0SYk7Bh-Un0oWCm-7obgL4lxG0DEFIaUhmj3Uy0etjCnEOWVGt7l6qsei35q8OAUqJhS0pMHQaBTqCiR8pOSFZ9xfyKRylFyb_-gj8hvOxdp477cqAUm8IeG_fJ2RiIrYPV1IhxRFw4nm2fefoE-C1d65imJAWk6tvnqNhsHp9AONhsKVjnBmjt0gqgKQMso0_yxrlgww3Z-cW2RCKgFPQdx9MH6ApAA6PSB86xRLaqxmDNNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⭕️
گفته میشه دیشب با وجود اینکه پدافندا توی تهران خیلی فعال بودن اما انفجاری گزارش نشده.
احتمالا دیشب بیشتر پهپادهای شناسایی آمریکا، مثل MQ-1C Gray Eagle و... تو آسمون تهران بودن و پدافندا هم سعی می‌کردن اونا رو بزنن.
احتمالاً مأموریت اصلی این پهپادا دیشب شناسایی بعضی مکان‌ها، مراکز نظامی، محل استقرار پدافندا، و... بوده و ممکنه که آمریکا درحال آماده کردن خودش برای دور جدیدی از جنگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68782" target="_blank">📅 10:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68781">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68781" target="_blank">📅 10:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68780">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68780" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68779">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68779" target="_blank">📅 09:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68778">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
سنتکام: حملات امشب به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68778" target="_blank">📅 04:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68777">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68777" target="_blank">📅 03:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68775">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=Lf5cEg_YXYM_-zMl2oa12RbXqS3Whq6S1aT5YVsE4KEcVyV6k6k4G20xB4WKb7GjZPeMpddxx0EKSlvvPmBpoTMC1AwHDoFTIgXzkQyu9euwtGLK-8jlsEUGWfd1RdMAn5XDAwvEim7EX7iH4-T_8JNoo6vyef7QYG7g5uhPlvRvzSRaOHpS2x9rNqqMZJy1Al7Z4_buKGHiLMopN1SGtt_z3YSf2sj6LZqPsIT0d8VyRLVMSZiCPxAWgRva3Z9tRYREMv94A2MHBrtVNOb5U0koGu9pmVuIQMIiVtMWvRVLv6SQoKBeS4ZSfJ9AO74iSnJmOLEuxa8OHBsCgD48Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=Lf5cEg_YXYM_-zMl2oa12RbXqS3Whq6S1aT5YVsE4KEcVyV6k6k4G20xB4WKb7GjZPeMpddxx0EKSlvvPmBpoTMC1AwHDoFTIgXzkQyu9euwtGLK-8jlsEUGWfd1RdMAn5XDAwvEim7EX7iH4-T_8JNoo6vyef7QYG7g5uhPlvRvzSRaOHpS2x9rNqqMZJy1Al7Z4_buKGHiLMopN1SGtt_z3YSf2sj6LZqPsIT0d8VyRLVMSZiCPxAWgRva3Z9tRYREMv94A2MHBrtVNOb5U0koGu9pmVuIQMIiVtMWvRVLv6SQoKBeS4ZSfJ9AO74iSnJmOLEuxa8OHBsCgD48Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68775" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68774">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
❌
🌐
امشب ریزپرنده ها در تهران فعالیت داشتند، احتمال اختلالِ بیشتر در اینترنت وجود داره؛ پروکسی های پرسرعت زیر رو داشته باشید
https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68774" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68773">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در زنجان!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68773" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68772">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXy8IwZZUdSoLPC4FrqwfS4kE0i3pjbqsJc6M8PHfl4etlszJG_gECy-TwAPS_Q-9r3YWnfizWo2VQ9P8vfEFXfHEkhGo2VQdxDzGabuK96C3-i2cE1KvOwc_8rz8MI-oX6sH6MO2nsYmGQdjvtcaani4QfVa4lH_iwx1qXVunuyQrNB345tN2R5XoP0G8dUBr8uYjN0f-ZZm3wnlSnRiC7CF7tY5cCHhxFMQpjZbJebBo9Ar4WZbgxJOgmZu-kQnhxEwbNFdLFAncCekJ121KovOzouQLhx3B6ekeqNUQqp5DHJ06K2pLlf4tChn4QKs1GJ50FC7n6HAA1RoW7iJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68772" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68771">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت پدافند شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68771" target="_blank">📅 03:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68770">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون حملات شدید آمریکا به</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68770" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68769">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68769" target="_blank">📅 02:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68768">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تا این لحظه سنتکام هیچ خبری مبنی بر آغاز حملات رو اعلام نکرده! #hjAly‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68768" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68767">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بابت گزارش های لحظه‌ایتون عمیقاً سپاسگزارم، ولی حتما سعی کنید بعدش چنین گزارش هایی رو پاک کنید خدای‌نکرده جایی تو بازرسی گوشی توسط مزدوران ج.ا، مشکلی پیش نیاد
❤️
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68767" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68766">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
هشت انفجار در تبریز  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68766" target="_blank">📅 02:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68765">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68765" target="_blank">📅 02:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68764">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه #hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68764" target="_blank">📅 02:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68763">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68763" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68762">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68762" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68761">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68761" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68760">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان  @News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68760" target="_blank">📅 02:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68759">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68759" target="_blank">📅 02:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68758">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در نارمک!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68758" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68757">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68757" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68756">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwtXaNMnKiyYi4oeFPyjIoLlBiEBvYoiAQ0T2XuNLKG10TJgRojK9hrgiYfWeRZpjLxdM4IXyquurV_Af1VeYBSsoW_9n6QBeSZQEknykoANW-KLhY2HmYsIxivl7f-zE_tdk8oepmsH2V0jMSVujB7RQ5ztiAMrvoe4j9YR7RFUNL0NHz4L1XZby7IshUMmohpM3m9byTkhp9wx6--TriWMoP0CiwynlgJFeV44Bl2njiZ3NID2V4OzJYz0jLacXU85IkMzwctSAoUS5tNleT_zZc5diVOpayS1-JnPyi203kfBeG8CEfu9mW8G742-VKq3NTc8JojQbpvL7zdBTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68756" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68755">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=HGssENKtL2UdSJyKA2csmh-DwIQp4J_EuHQR-_127fgfivU0iwfVxRzp9NKcDgJUhEP9tBvhtUmAD_tjtcdJhrwWYZ2nj4zBgYiBhVDO-XTwk1bzoLnp8H_lMLoJBuaSE42Mdu7ngAVDnH55JFA7ht1vw75EO9SrShmoZtEfraP6dj2UQuESq3SSpVYvt1cSzMcnXg22mKMlZ7wIJgNeWN_tbWieGQd2g8Thhw7so1hhkyWfqLxYlwpvKf_05iwaoLD1WCjYK1cTMi3PAJvZWEJjdz6KpCgr239Jv11QMIZKo8BMn76bqDFTlXoDpGnEtMl4aM8uCTcIhJ0VwnIB4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=HGssENKtL2UdSJyKA2csmh-DwIQp4J_EuHQR-_127fgfivU0iwfVxRzp9NKcDgJUhEP9tBvhtUmAD_tjtcdJhrwWYZ2nj4zBgYiBhVDO-XTwk1bzoLnp8H_lMLoJBuaSE42Mdu7ngAVDnH55JFA7ht1vw75EO9SrShmoZtEfraP6dj2UQuESq3SSpVYvt1cSzMcnXg22mKMlZ7wIJgNeWN_tbWieGQd2g8Thhw7so1hhkyWfqLxYlwpvKf_05iwaoLD1WCjYK1cTMi3PAJvZWEJjdz6KpCgr239Jv11QMIZKo8BMn76bqDFTlXoDpGnEtMl4aM8uCTcIhJ0VwnIB4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
پهباد‌های انتحاری در آسمان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68755" target="_blank">📅 01:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68754">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
جمهوری اسلامی به کویت حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68754" target="_blank">📅 01:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68753">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=rtXvz9uA6hdI2fTGuLwFKauKtHB_Q6F60KOW-koJY4NPO_nbmgmRMYTcNzntqNVbhIqmrGyh2Z3-Z2pQOBA7eC4AV8E2T8z3K2lPyELhbRLsgkNHfj1pFSQ0mnQ6NF8jQZAPtaMyjD8sw8SGruEqnvrMB7CF_wylW0k5iDEPw-X2xVS873-xdDYE3JSlXcjUYDvhPUS1niU9KdlZ8kChPAaXQ-KS_hVCzwQPXCCmxZTS8-pMaLthUd3ohQxByNcWuvl5EYRacu84InJU0bIXWAaCM7c_aA9jF8VXusHFjY8xGF266Y_L8gCn7DA4dG2KqM22BzgQaSXPpjnHt_FvHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=rtXvz9uA6hdI2fTGuLwFKauKtHB_Q6F60KOW-koJY4NPO_nbmgmRMYTcNzntqNVbhIqmrGyh2Z3-Z2pQOBA7eC4AV8E2T8z3K2lPyELhbRLsgkNHfj1pFSQ0mnQ6NF8jQZAPtaMyjD8sw8SGruEqnvrMB7CF_wylW0k5iDEPw-X2xVS873-xdDYE3JSlXcjUYDvhPUS1niU9KdlZ8kChPAaXQ-KS_hVCzwQPXCCmxZTS8-pMaLthUd3ohQxByNcWuvl5EYRacu84InJU0bIXWAaCM7c_aA9jF8VXusHFjY8xGF266Y_L8gCn7DA4dG2KqM22BzgQaSXPpjnHt_FvHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست وزیر جنگ آمریکا:
«رئیس‌جمهور ترامپ گفت که ما دوباره درگیر جنگ‌های احمقانه‌ای مانند [عراق و افغانستان] نمی‌شویم، و او این کار را نکرده است.
به همین دلیل است که ما سعی نکرده‌ایم جامعه ایران را از نو بسازیم، بلکه صرفاً، به شیوه‌ای واقع‌گرایانه و با شعار «اول آمریکا»، اطمینان حاصل کنیم که آنها هرگز به بمب هسته‌ای راه پیدا نمی‌کنند - کاملاً متوقف می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68753" target="_blank">📅 01:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68752">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=F4qW_TZdaphUxWp0JA0QyWdg75t9JwJ2Nfl1ZFYTb66F0efqm1SX-8ofHha4OGRNsYPVGdpzqeX4g-lRQQlToRLscWiOg1HGtsyAwMfMAxIc_oRq5f7JZi9zX6GTeTE72hsvjWKdnUZHTkvV0KasMJpWCHC5B94Tb79-yKfnsKuGGZWZ3fkQ3UsnfnrDWCJekiE43M6bc19Jmk_o7DI2NyaI_Z1fSOCYUqk04GeiV3D8Cdp_l-VRoKF1zTt4jgTO4SZbDxj7deQl-GQDe7xRzfwq7lpSwS4IcKS8dZP3VmgSjhrsJKk_eu9k4naipW95Ej5TDTXXiQR0yDV3-sJh0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=F4qW_TZdaphUxWp0JA0QyWdg75t9JwJ2Nfl1ZFYTb66F0efqm1SX-8ofHha4OGRNsYPVGdpzqeX4g-lRQQlToRLscWiOg1HGtsyAwMfMAxIc_oRq5f7JZi9zX6GTeTE72hsvjWKdnUZHTkvV0KasMJpWCHC5B94Tb79-yKfnsKuGGZWZ3fkQ3UsnfnrDWCJekiE43M6bc19Jmk_o7DI2NyaI_Z1fSOCYUqk04GeiV3D8Cdp_l-VRoKF1zTt4jgTO4SZbDxj7deQl-GQDe7xRzfwq7lpSwS4IcKS8dZP3VmgSjhrsJKk_eu9k4naipW95Ej5TDTXXiQR0yDV3-sJh0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاورمیانه هرشب
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68752" target="_blank">📅 00:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68751">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5071O0WNNbaum4XWHf6-n1KEhpY0bhkGSC8rUHddjtijcjTyVUbWkZeOgxzSLqRxLXzqFv55fagprKIKotBbThH4lGq0NmPOaVM8A7HME6jHfM-rjJqkwgO-ajodhL3HWSD89YSpiqsmdKTc1EzZqClvy0YN7cNrjXpYOSWqU5yaPok75L2p3Z_DDT-jAD6wzfVaZC0CWguMWVmyrCuLV9-Dc_6DCVwZxLY5OBKJZOEfrYoUH_GXG8MpalUruCq_YrCkfaaP2LgniVvUO7N17FDyE-suWGf6qOPnzFXYyCMgOQsqcZAOkVXUQfNukhimfYHCmMrlcMQj2QHmesijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قرارگاه مرکزی خاتم‌الانبیا:
آمریکای جنایتکار مراکز هسته‌ای و تأسیسات حساس ایران رو تهدید کرده که ممکنه بهشون حمله کنه.
اعلام می‌کنیم اگه ارتش متجاوز و تروریست آمریکا چنین اقدامی انجام بده، این کار رو به‌عنوان گسترش جنگ در منطقه تلقی می‌کنیم و همه منافع آمریکا، همچنین منافع متحدها و حامیان این کشور یاغی و شرور، هدف حملات قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68751" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68750">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=XvWzcUJY76XinBtbNsODI-g5Y_6pdAJv2uLbDtpu62YWgVMLpxyhEyysXntDzS1CBNlDoVJOYDQJr7ENX7qpl6E8RFxwNqW2MQtLatc59WPpRWNv4i7re1nEm2hy-JptdFOJFs3ITLUSqFQjxrbVIgZeValTHcZpxl3cfttiAPriB_KIcuQRKXpo-ktZrkt53CvUHtjwqpg3bc3B90zQ3HKE9eHDzSl3KQ2faKyXAfWaNKdq6ZOFzQphAdeDW4njQ1VZWWFx_xsg3YZdGpRvqzyblTf2U35GDt7XdV3phKVRFdBdCyDWrqaZjrz04KJfdI-tCnf_msZuL_mOskucrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=XvWzcUJY76XinBtbNsODI-g5Y_6pdAJv2uLbDtpu62YWgVMLpxyhEyysXntDzS1CBNlDoVJOYDQJr7ENX7qpl6E8RFxwNqW2MQtLatc59WPpRWNv4i7re1nEm2hy-JptdFOJFs3ITLUSqFQjxrbVIgZeValTHcZpxl3cfttiAPriB_KIcuQRKXpo-ktZrkt53CvUHtjwqpg3bc3B90zQ3HKE9eHDzSl3KQ2faKyXAfWaNKdq6ZOFzQphAdeDW4njQ1VZWWFx_xsg3YZdGpRvqzyblTf2U35GDt7XdV3phKVRFdBdCyDWrqaZjrz04KJfdI-tCnf_msZuL_mOskucrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68750" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68749">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=slNW1K6rwmQWmGWvVcUv3PU6YCK--hOfWH8yFKUilBrauOosrIk2fWViHizmGfOiu63G4X5IXqaARue84sD64-PhwmwtrNsyvEpGse7tYu9y4EyHU-srl8bAs_2clYvXd7p38GliSnJ1L2Sxi9mshq-MVeeSb1rFmHW1dOB2bjzyon0unwNLX16SiA3r-jwstUFKnoPifbq-UXD3D-PAmLdn9h4yuzsyA0YYwc2r1jwVREEL5MGOOjzhA49tprriKleIF-IIfx_C610JJsNNmX-0DN4DQGCl-v6Yoz47-BFGGGdL1Hxu3oOe7amtaP91ZttPGCfCpWa8vTBx3DITtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=slNW1K6rwmQWmGWvVcUv3PU6YCK--hOfWH8yFKUilBrauOosrIk2fWViHizmGfOiu63G4X5IXqaARue84sD64-PhwmwtrNsyvEpGse7tYu9y4EyHU-srl8bAs_2clYvXd7p38GliSnJ1L2Sxi9mshq-MVeeSb1rFmHW1dOB2bjzyon0unwNLX16SiA3r-jwstUFKnoPifbq-UXD3D-PAmLdn9h4yuzsyA0YYwc2r1jwVREEL5MGOOjzhA49tprriKleIF-IIfx_C610JJsNNmX-0DN4DQGCl-v6Yoz47-BFGGGdL1Hxu3oOe7amtaP91ZttPGCfCpWa8vTBx3DITtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست:
محاصره ما دوباره اعمال شده و عملاً غیرقابل‌نفوذ است...
بسیاری از حملاتی که دریاسالار کوپر و سنتکام (CENTCOM) انجام می‌دهند، توانایی ایران برای رصد و پایش در تنگه هرمز را از بین می‌برد.
سناتور جان هوون: « هدف از این بودجه‌گذاری همین است... اطمینان از اینکه ما و متحدانمان می‌توانیم در تنگه هرمز عملیات انجام دهیم... و اینکه ایران را وادار کنیم تا در راستای اهداف ما عمل کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68749" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68748">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=D1PEJIyROSwRrO1twnSClA6zkEoJbvAq67VF9L0eY_rRnJtOH2qdpFCLJ7Brqgto3ixH4Er8WQyZQdOScav5HY5pOH-s-Hh5XfJI_anPtOps4LquziFTiFdv8gRRCREeAPHTMA7-LcyLESZeEwbw8HsspmByyn0vfqX7zdf5CqUGf92BazRasjs6_7jOlm_L32ryyTfy-QfdBc9JmDNBnt0jMtoF9IuVTUQEH5pNedcQNOIIwhsUa0TuuxzWkVEMqyoGUn-C3A7mhzhjMKRpYWMdoXwGx3yPi6WnyZwknRxWnOO9fBp1pcrhJiAo-hBm7WvbVk2j4gf4w45VBMMmig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=D1PEJIyROSwRrO1twnSClA6zkEoJbvAq67VF9L0eY_rRnJtOH2qdpFCLJ7Brqgto3ixH4Er8WQyZQdOScav5HY5pOH-s-Hh5XfJI_anPtOps4LquziFTiFdv8gRRCREeAPHTMA7-LcyLESZeEwbw8HsspmByyn0vfqX7zdf5CqUGf92BazRasjs6_7jOlm_L32ryyTfy-QfdBc9JmDNBnt0jMtoF9IuVTUQEH5pNedcQNOIIwhsUa0TuuxzWkVEMqyoGUn-C3A7mhzhjMKRpYWMdoXwGx3yPi6WnyZwknRxWnOO9fBp1pcrhJiAo-hBm7WvbVk2j4gf4w45VBMMmig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
من در مقابل یک کمیته نشسته‌ام که می‌خواهد درباره پیروزی در جنگی صحبت کند که چهار سال است ادامه دارد، و درباره شکست استراتژیک درگیری‌ای صحبت می‌کند که چهار ماه است ادامه دارد، تا از دستیابی ایران به بمب هسته‌ای جلوگیری شود.
امیدوارم که در این شهر، دیدگاهی وجود داشته باشد نسبت به اهمیت تاریخی اقداماتی که رئیس‌جمهور ترامپ در حال انجام آن‌ها است.
آیا شما می‌خواهید که گروه‌های افراطی اسلامی به بمب هسته‌ای دست پیدا کنند...؟"
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68748" target="_blank">📅 00:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68747">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=aTG1dFWL4YIAWYrzlALI4n7Dzay0Y6blz3dHFFchdOBcWCnbexXNS1VT3oNrKSfYv51DtQPaxNN5y1Wl88ULye8bQJ7mlkrtgjS0mIJ-ZKfmg7ZNyKsHvfO--oj2gjdmcaRtieXASdve5ZPiHCn_WH6h7XZCoWxdB0MwBVx60_xN874Zj7wJW7Jpxd8McvWPOf0Enj5KvSejpnZWp1a4Aj5PAue8Sr_w1Owko2WV105b0PqA9CFrkeOS6s6fz04ChEie7x1XLWEUok_Gsj3hMye95rCHUtN7ejppak1syPC02iBnJJhoHSZ6sjHQTeiB_wDpYEQEQwJRB8LkHOtigQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=aTG1dFWL4YIAWYrzlALI4n7Dzay0Y6blz3dHFFchdOBcWCnbexXNS1VT3oNrKSfYv51DtQPaxNN5y1Wl88ULye8bQJ7mlkrtgjS0mIJ-ZKfmg7ZNyKsHvfO--oj2gjdmcaRtieXASdve5ZPiHCn_WH6h7XZCoWxdB0MwBVx60_xN874Zj7wJW7Jpxd8McvWPOf0Enj5KvSejpnZWp1a4Aj5PAue8Sr_w1Owko2WV105b0PqA9CFrkeOS6s6fz04ChEie7x1XLWEUok_Gsj3hMye95rCHUtN7ejppak1syPC02iBnJJhoHSZ6sjHQTeiB_wDpYEQEQwJRB8LkHOtigQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=qPfAeSrNBSi_105xKrYcnwOukFiBrkAfr6aRVsfj2kxS17wWkR8ynsCqZaDeDMn0_E73_4KZRhbS1xHXpNWGBJWAvYuEmYlTx6brfdMGXsDUoCmJ60FdjPrqAOdzj6ZAQXeXbsIbGuqLVDjmazJAprUmkLUifDi17cQqWKHySeWWE2jKP2DKKAmeJnHOlL6eyBk08gDOcDq4Kqv8UoTA4YqEQml6ul2Aj2pJqPVL5wk4ruPE3nbf-W00u133XRtxlqMvyNt8Z9pHYblVjGz6eUK7o53nOSt1n9gD5vbXmKopk1a0aMMsTQp8rZG-ZK_oiqkjMxJIrFvKec4c1GO52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=qPfAeSrNBSi_105xKrYcnwOukFiBrkAfr6aRVsfj2kxS17wWkR8ynsCqZaDeDMn0_E73_4KZRhbS1xHXpNWGBJWAvYuEmYlTx6brfdMGXsDUoCmJ60FdjPrqAOdzj6ZAQXeXbsIbGuqLVDjmazJAprUmkLUifDi17cQqWKHySeWWE2jKP2DKKAmeJnHOlL6eyBk08gDOcDq4Kqv8UoTA4YqEQml6ul2Aj2pJqPVL5wk4ruPE3nbf-W00u133XRtxlqMvyNt8Z9pHYblVjGz6eUK7o53nOSt1n9gD5vbXmKopk1a0aMMsTQp8rZG-ZK_oiqkjMxJIrFvKec4c1GO52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=UZewa2KvwXZh70mJ5StQY9i5Zwg_aXTMvq12c4jHB9l-alcUgS0s-5jDkTjE6seln0cTMuG0YwZnSXDhCNpK7wJwrqpAHP-SReskRZVZGc93yZHpcFS4FEwtN8sX_VPxkuNfIB4TJ9FyzseMCOHQPnnMtZ7n04QaxHEn_8fB9pjjDviMdcMZFh9N-K1tVY-u6WqEyzyzKBTd3kVDp9msQIKjn39xhpmZ_1LWGWobPkLeKixIwC_vy0mfxsWGB-eISTTDBQ49issiHlaMYbnmolzL5zXINKumtYHq2S_q1upqOBurX1Q0-aP6jdGzfk5yenc-6ThP4Gq4nbAc6uM--g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=UZewa2KvwXZh70mJ5StQY9i5Zwg_aXTMvq12c4jHB9l-alcUgS0s-5jDkTjE6seln0cTMuG0YwZnSXDhCNpK7wJwrqpAHP-SReskRZVZGc93yZHpcFS4FEwtN8sX_VPxkuNfIB4TJ9FyzseMCOHQPnnMtZ7n04QaxHEn_8fB9pjjDviMdcMZFh9N-K1tVY-u6WqEyzyzKBTd3kVDp9msQIKjn39xhpmZ_1LWGWobPkLeKixIwC_vy0mfxsWGB-eISTTDBQ49issiHlaMYbnmolzL5zXINKumtYHq2S_q1upqOBurX1Q0-aP6jdGzfk5yenc-6ThP4Gq4nbAc6uM--g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeFfHj__EN-RfPvxOr7WreSUyEW0FGnfkf-pG6G8cFJVsAoqIeCOtkqH4eVZ9L8DMZS4wPB4APUXfqwoJm3yWGbI60vz8VbtZketV8BLoKFpdxpofeoIbGVi7xSi40aDa6sDE9XXdqV3lls9s90TI9lNIB0QaLugRtoNRozs3rVQkMi2aQyXLkHu9nu9T41z_5exFgyqymyKhTVXbhAgI21xDw3rKU-46FnWSmVfCxCYBPSd9UzqSKVRTMlIhVWBOBEWmrtYIBL_E5sOVxTNEKGkd4foWPhYg-rEAyJSf5_E1kEZEH4iwGsCcl42c1iOGiF9gfR5x9bEhbqVMjQ8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
چند سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل بلند شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68744" target="_blank">📅 23:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68743">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تاسیسات جدید هسته‌ای ج.ا: ۲۰۰ متر زیر کوه کلنگ
پرنفوذ ترین بمب غیرهسته‌ای آمریکا: GBU-57 با ۶۰ متر نفوذ
#hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68743" target="_blank">📅 23:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68742">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSpvUDOISsFgAhmt3o9V6VhL4qeBNL71M76TcqhujJKcbm05wkKcyQ7gY26sPW_l2-Cr_xrICBLC_IqGtvnfDWEvrCjQfWLhjj1rKD9LGJdXNUP7cUioIQttDmfnq852N9z8-IM4i2u0L085n3ZnrbmqqWSo3Zv1YzljEt29aFfiKW884zyUxx8H4kncjGwigNyAaHae9yCPFh5x9iFWGIwslD8YpSc4MpB1GhDPQ_ozEdN2VKChRMWRitHYasEL9VHh82cvDZ17jYA9Mf_WIrETZXupfNt5M5Lal8TtmLcnon-WdsrQ1cbmd73GRiQtxlV6KIPn9LNZlh2v_wwhoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=eeeOXqSOvcN-d2LhtCpBF6O8CgZb5KRium9nzHCcwU1BvodN-j7zjDFKpRucpxMMKw3HvUIl09tyJWhEbLkPcbylPLQmoTufpUe6PKrz_Xxh46ysWDibD577SYFhUhEmvjY2fiS_qe4Fdcdv95BZKuoox1rJSasmh2cC19G2lA7Zz3U8-A4y29VoemzxXQeRK252dJ0esk-SYCqXIGReO9tBIhSoXwG25aPNPAALeNV2qp8N1e9pxtS3GiLT_tcU4ti4uHGcnOwi3PtqxyvhIhFCVUz5TIoAHAEQ8iK9cUMKPSMGXFR4TzD34dg-ao_8LEJnPOBpGUJ2E0aSAxFONoW-P_X5HtERRGqDzjHIWHQXbsEKU2TT0SWULjHvJitEg6JcYq6sogjLBB76PlqBSer-4PahwjIe7dffyBReIaLNOI2Zc2IdAsLna13nski4gGXwMsYWG_1GW1E8ExZfjzwbJzRjN0sDMyqkAlSG5mLDmb8GPoncwgJpwWk9U4sTRgw408dTR1X9MMPr3A8VudAwOTKqUIzUm6ItEj16mbajuGGPT0Cx-eTchHmTiKDdA_vzI_ibxRhbJboS-bqJR0pBs-pOieutsz0ez21XJENVT5G0Olku1ISe4Qbkj1abOqB49ePFdxu92LjQ8SDjkqwK5KKiQ_SfVWKJC7hQQnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=eeeOXqSOvcN-d2LhtCpBF6O8CgZb5KRium9nzHCcwU1BvodN-j7zjDFKpRucpxMMKw3HvUIl09tyJWhEbLkPcbylPLQmoTufpUe6PKrz_Xxh46ysWDibD577SYFhUhEmvjY2fiS_qe4Fdcdv95BZKuoox1rJSasmh2cC19G2lA7Zz3U8-A4y29VoemzxXQeRK252dJ0esk-SYCqXIGReO9tBIhSoXwG25aPNPAALeNV2qp8N1e9pxtS3GiLT_tcU4ti4uHGcnOwi3PtqxyvhIhFCVUz5TIoAHAEQ8iK9cUMKPSMGXFR4TzD34dg-ao_8LEJnPOBpGUJ2E0aSAxFONoW-P_X5HtERRGqDzjHIWHQXbsEKU2TT0SWULjHvJitEg6JcYq6sogjLBB76PlqBSer-4PahwjIe7dffyBReIaLNOI2Zc2IdAsLna13nski4gGXwMsYWG_1GW1E8ExZfjzwbJzRjN0sDMyqkAlSG5mLDmb8GPoncwgJpwWk9U4sTRgw408dTR1X9MMPr3A8VudAwOTKqUIzUm6ItEj16mbajuGGPT0Cx-eTchHmTiKDdA_vzI_ibxRhbJboS-bqJR0pBs-pOieutsz0ez21XJENVT5G0Olku1ISe4Qbkj1abOqB49ePFdxu92LjQ8SDjkqwK5KKiQ_SfVWKJC7hQQnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
هرگونه موفقیت عملیاتی در خاورمیانه، از جمله در زمینه محاصره ایران توسط ایالات متحده، با عملکرد نیروهای نظامی متمرکز بر مأموریت‌هایشان آغاز و تکمیل می‌شود. تا تاریخ ۲۱ ژوئیه، نیروهای آمریکایی برای اجرای کامل این محاصره، مسیر ۸ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68741" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68740">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=FS9eyDyNMmvTtDefqieYKuSzx7m3Uf3qLwrPFbUKrra2wB1mxq7clEaM81cb8xUcgbbQip-YMpUR90bKOZZKw_dGETQWQuXx8dhFpU8qY3hnR23oWYFvUzoQgueOmbxrKUPh4mC4LXipoyuNfCDYFXtkuhguN02pYJEkaxh0U97-VYRq0AWUtObVReYHTZ8P5sYK805hM4dB-BKe3dZycWqbsygNCvXtKid5TPXz0IeLhrFuJaYPAJ3BPElmk5dLggDJKwOF-A5N1RUwRqOwQahWPcxBCuWHaSuCbGS0aa2cuedgDzDK66XjpJSE-O7gCRKrzpRMnTmFIM61ovNHOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=FS9eyDyNMmvTtDefqieYKuSzx7m3Uf3qLwrPFbUKrra2wB1mxq7clEaM81cb8xUcgbbQip-YMpUR90bKOZZKw_dGETQWQuXx8dhFpU8qY3hnR23oWYFvUzoQgueOmbxrKUPh4mC4LXipoyuNfCDYFXtkuhguN02pYJEkaxh0U97-VYRq0AWUtObVReYHTZ8P5sYK805hM4dB-BKe3dZycWqbsygNCvXtKid5TPXz0IeLhrFuJaYPAJ3BPElmk5dLggDJKwOF-A5N1RUwRqOwQahWPcxBCuWHaSuCbGS0aa2cuedgDzDK66XjpJSE-O7gCRKrzpRMnTmFIM61ovNHOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇮🇱
کانال 14 اسرائیل:
سپاه سفارت اسرائیل رو تو بحرین زده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68739" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68738">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=f2BDYTDhjvGMbo-VPgvBob2zSi5FS5x121IujCI1G13nB7yRB-EhNR99qcyBjuNX4lFWWu454O4umMHx8LXltyyb920fXUTo0-gS-poTDYoqzgjyWOO_RvOrgbPus_KoJE-ZuaakXNLLmGGiP94ZkQaiWb4DMdAS0X9weN5txJXrX49Zbu8C8ipeb6dIWsNZhVy1Cz0d9CWKt6rUnewf9OB-IOoOvlfsUrBZ5booNSek_QnBS6Ou8UBOpYZeEzSXA2t0uXS2JNbn7qecEVsd7ibNnpdZakCV0TEZ3jUOdeIJQ-l54XZxZD2hTOsiBBwlS-8AbnIqkWIo03u3LDip8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=f2BDYTDhjvGMbo-VPgvBob2zSi5FS5x121IujCI1G13nB7yRB-EhNR99qcyBjuNX4lFWWu454O4umMHx8LXltyyb920fXUTo0-gS-poTDYoqzgjyWOO_RvOrgbPus_KoJE-ZuaakXNLLmGGiP94ZkQaiWb4DMdAS0X9weN5txJXrX49Zbu8C8ipeb6dIWsNZhVy1Cz0d9CWKt6rUnewf9OB-IOoOvlfsUrBZ5booNSek_QnBS6Ou8UBOpYZeEzSXA2t0uXS2JNbn7qecEVsd7ibNnpdZakCV0TEZ3jUOdeIJQ-l54XZxZD2hTOsiBBwlS-8AbnIqkWIo03u3LDip8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
انهدام پهپاد جمهوری اسلامی توسط سامانه آمریکایی برفراز اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68738" target="_blank">📅 22:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68737">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=JZHEUBtEhQOHIDaVBhZkjokHP41Xx-tm0w4JW52vNbO1ccIiCaLVBkNtIRj61_hY1SEAJnWacc0JZFot6e9A69Hdew_iwXytYeZB9IsHxXvVXeS5OS-HiWe7kUXyg8-VfHPEEyKHDtTgUvHfO0BWqhxCi7FhC1J02MbtGZzf_Sz0hlmcSCKXS9hk5VX8QdXMQNYQ9yn28z-r-5HNxlj1Yg0-VrUQ6Zik5S2bHHCPiyfcYEfBBbT7La1D9hmqP_P4LpaeL4I2iPmTzSmNVzc49ghoPPHpLmWX_a7ccBkMYXYiozJ9RXcKQuNNTm0nT4f9iaOirNXP0VeHzzzsEbXHrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=JZHEUBtEhQOHIDaVBhZkjokHP41Xx-tm0w4JW52vNbO1ccIiCaLVBkNtIRj61_hY1SEAJnWacc0JZFot6e9A69Hdew_iwXytYeZB9IsHxXvVXeS5OS-HiWe7kUXyg8-VfHPEEyKHDtTgUvHfO0BWqhxCi7FhC1J02MbtGZzf_Sz0hlmcSCKXS9hk5VX8QdXMQNYQ9yn28z-r-5HNxlj1Yg0-VrUQ6Zik5S2bHHCPiyfcYEfBBbT7La1D9hmqP_P4LpaeL4I2iPmTzSmNVzc49ghoPPHpLmWX_a7ccBkMYXYiozJ9RXcKQuNNTm0nT4f9iaOirNXP0VeHzzzsEbXHrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته دانش آموزی که ۰/۷۵ گرفته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68737" target="_blank">📅 22:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68736">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNwTkXB8tgueBtT4mJAaP1a6dbR7znJYPyMmP_-Mt5QIIDuzzxTEKI8BCcCZE7p83my-1sque_2TEML4bxf_eOvxr2ClQZt78MgwD8EIbTJKw98UyZfRbidkFOc2yD-tx-RO-Uwk3SHeBbYllHdUSCQJTWDNMK5lMvL1ZgMFXfC1skTWLXl7_IxKqw8zNjNY39Vd55GfPnyZ5iDwqJ0Y_4j640me-k4WGmydlA-yNoAZzlbDsS1wI3oXYR7XXiZ3G53kWSmC6de6bN0rCUCR4i8BTLyiKXPM6X1LViEinvp0k9jiTgBPM7YWlyYZI3mSyVggb73srKOwpGptesZNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به گفته بعضی از کاربران شیرازی، این اولین بار نیست که چنین اتفاقی می‌افته. ظاهراً چند بار هم دیده شده یه نفر میاد اینجا آتیش روشن می‌کنه و بعد میره؛ اما هنوز معلوم نیست هدفش از این کار چیه...
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68736" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68734">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NaqtHkF_St1B-2LkX-g6MshkGHX7AbTk8PRb5eRohkAscinARVjzWsUFcT1McQEEauX1ip9lJZx0FOouskZg0g7sWkEuIxwAE74bjCVxdg4m8cRMr3FYDeXl_1ErsVdREn-WXWYKVeku_8jXOcyPKHl4_EHCxfkXQiTWqKr7B95w4FZ4xIWmc8UV2yFm7365VrM-e_gZEFR2Ze9NiNnEgH6ZUDNhLvbtAH47wqXChgSioUKPSvaFlaFssX0Yv3fUNYsfYundhKWBi8pZHelmBw66Vv_YC3xeCuJlZtVTnh81x5FfYMOPMnLCCvsfyd4_u0wq7f4PjAQtJ2tMDCyCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxHWseofex7ziu56QEsGei81zVdhBpMJ_RhqoPgiFDLhZytWAHrO5ONPD_lzaSK4UQPO9JegdoMgn9Ti33RL7JTwJQgeyXIeWmeziZn6XjkzGYFerLj01gVQGogRbMvqBxXIaLqR-uCgAX86v-vFLjPX-QbZ8f0ZLwFuR5kagga8PbnUUlweGce5aELa-DUjK6fasdn-Vydf_bMO448pJncVzbux0UU-ZG8LbtlklLJ0y2dtYjJDRFs1KmEsD9Y_rlj4c6T0qagJa1Le5aiUGQyW6UJ3v1Gmaxyx4dancYSFGTFFK8nhRQMkbkGDcU6zy6hug0uiAXDp_YHBqiKWWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز در حال آتش‌سوزی به دلایل نامعلوم
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68734" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68733">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q_iUme08bS7gonw898yEfjxMtR9CfsA__m0GfTXD3Mk9wm6xpmHUp2djolntp8NPCfkwoI1EQBsnv27ggtzOUycaW3NaGrc9_r-sbHp7040a3pV4XdB21qlBppomQ02tVrC5p0gF9wS8dHjO7gPEkPAhE0tVClza9hZxaLXpeoomK50FVJLP5hpJtvoTsJ3Pxa2lpYI_LWz2tn1U6M1CRfnTqQfJWf5OCjSqVJMX5cLpY7f2FyvE5xC5s9r3fLA38ON7Uz-uLsPG0qW2Yq8vWwzz1BXirOYP0gLKh9rvbosHA7JafiEgusr9khfPF5bJnTF3yDkH3Q1TfTZAwk7JCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گزارش های تایید نشده از آتش‌سوزی در کوه دراک شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68733" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68732">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=Glt8fZgtlqodPbiKocohhk6U6SrHuoCF70aGUvzW3jX-nFgVzq6W55LeOyIXen55yYj9LkBnA2ULHgq77PpD53W4hbFXO36sIjl2ReuoVMKD1bf7bIshUD3T85wo3kx3NjEkG3D4q-2N0CmummVQZ9Z_fk9I-suG-fZ3SWOZ0kV_4QfOSIJ-fDF0ku0r8sPgLcCRi3HY9m3bA9RqFg9viN_8xXQFcXY61236RlX4a5ZoTmVIeMeOZp8dsoe3_dEp6KWmTeDg7Z-IAn8DpCQAKsj9u0OCrGr5IZjgZmkCH-afLAnHxkrob5aAShHuY0VegMlp9uDgJnVpcj9X6QrL2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=Glt8fZgtlqodPbiKocohhk6U6SrHuoCF70aGUvzW3jX-nFgVzq6W55LeOyIXen55yYj9LkBnA2ULHgq77PpD53W4hbFXO36sIjl2ReuoVMKD1bf7bIshUD3T85wo3kx3NjEkG3D4q-2N0CmummVQZ9Z_fk9I-suG-fZ3SWOZ0kV_4QfOSIJ-fDF0ku0r8sPgLcCRi3HY9m3bA9RqFg9viN_8xXQFcXY61236RlX4a5ZoTmVIeMeOZp8dsoe3_dEp6KWmTeDg7Z-IAn8DpCQAKsj9u0OCrGr5IZjgZmkCH-afLAnHxkrob5aAShHuY0VegMlp9uDgJnVpcj9X6QrL2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چندی پیش، همزمان با تهدید رئیس جمهور ترامپ به حمله به «کوه کلنگ» مستحکم ایران، چندین بمب‌افکن سنگین B-1 Lancer نیروی هوایی ایالات متحده، خاک بریتانیا را ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68732" target="_blank">📅 20:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68731">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=U6CPRPpGcXaEaxhx61zQCC8u6UMT9NoE0ksfF9l6EPAA616YdvGd5LIpGTKo8ofQqWVAXUZllj8QJqC0JmBdclcX6lSiWcIJMW7hQmbB58nH73VVbJjsyLKcAot6xesRk4VhBzSBAC1ntZyhp3-5r571oNScExj8DdPidIZx6q50ijD0zPpgZBhFo_SLKoRKHvPfLWPddItqiQUGkwB0jQ_bJ73KiFFJMXKqdcq4zMwJp1SNkM4ByQ2GIkBMoz-C49alscjVL6BOcBQ0_9f8Mg99nCGsXAMl_GMVCFDNYc5lPAgXW0O9_Mv2ZAezWF0zcGvZDxFKIo-CDp_p_dyDZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=U6CPRPpGcXaEaxhx61zQCC8u6UMT9NoE0ksfF9l6EPAA616YdvGd5LIpGTKo8ofQqWVAXUZllj8QJqC0JmBdclcX6lSiWcIJMW7hQmbB58nH73VVbJjsyLKcAot6xesRk4VhBzSBAC1ntZyhp3-5r571oNScExj8DdPidIZx6q50ijD0zPpgZBhFo_SLKoRKHvPfLWPddItqiQUGkwB0jQ_bJ73KiFFJMXKqdcq4zMwJp1SNkM4ByQ2GIkBMoz-C49alscjVL6BOcBQ0_9f8Mg99nCGsXAMl_GMVCFDNYc5lPAgXW0O9_Mv2ZAezWF0zcGvZDxFKIo-CDp_p_dyDZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ:
به ایران فرصت‌های فراوانی داده شده است تا مذاکره کند و نشان دهد که در قبال تنگه هرمز رفتاری معقول دارد. اما اگر آن‌ها بخواهند به کشتی‌های تجاری شلیک کنند، آن‌گاه ما — همان‌طور که رئیس‌جمهور گفته است — ضربه‌ای ده برابر سنگین‌تر به آن‌ها وارد خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68731" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68730">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=vKK4JRq_IroYFx2HaYQnQ186iDKpzUEkAth2pWWiA9gWopZ_71Z6bJ9rlEDNxTC1ka0C74AyXKFOt2g0_A5yJDZOhf6OTX0BggCJc3UU4OuKUoLmQBRZPFtBE3ePg3u8TcK2GjQkc6h5L0-JKWpGZAoeJfFDt-MTTUj5JFVuBKWv0FKq--L0sk4XTUlu68fXo70XXIgSzeTWh0tlp5Eo9XxOfmKcAO38Vq5AmUqnrXYn63TRzO1sYCHKLchd0UjdEXgsuPigU5Pv7tSkP8By0S6fmvpCEMvPYoIrpSqSD4F5CL4wxZtcHXRO5NXwNMX8igaj3zxaOczjm91b8gV-mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=vKK4JRq_IroYFx2HaYQnQ186iDKpzUEkAth2pWWiA9gWopZ_71Z6bJ9rlEDNxTC1ka0C74AyXKFOt2g0_A5yJDZOhf6OTX0BggCJc3UU4OuKUoLmQBRZPFtBE3ePg3u8TcK2GjQkc6h5L0-JKWpGZAoeJfFDt-MTTUj5JFVuBKWv0FKq--L0sk4XTUlu68fXo70XXIgSzeTWh0tlp5Eo9XxOfmKcAO38Vq5AmUqnrXYn63TRzO1sYCHKLchd0UjdEXgsuPigU5Pv7tSkP8By0S6fmvpCEMvPYoIrpSqSD4F5CL4wxZtcHXRO5NXwNMX8igaj3zxaOczjm91b8gV-mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-JRyQgANZjZ1eUNtG3IHTPZQ5yoitgw14BF1JZh-3uc6nrJiuhRQ0Cnr5-wg8ldj_cXu866SkynzNfMCF24XCpnT_Zt1ZlQhkq0p-VEfm0KWjypGsOw6EPHTTbdW3upcY3k4HxBMEUx68vWrLgH6tMLeZNIifLA6t0Ljd2ywuvx3AXFN8CUqNqsD__FKD_ZFyv9uGEUVH5AB1r64c3Q-A2snPIO8rEkAlTRkqSAUfFMdPY_-5RPwkPwipySpOYGWkr4pTddAlwDSp5q1vyQ3dmxJ6Lur73cACpQnzaJtm_Pyn9hW3d0epASRXppTomEX8w0JHYFhzR62LhBGMu735s0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-JRyQgANZjZ1eUNtG3IHTPZQ5yoitgw14BF1JZh-3uc6nrJiuhRQ0Cnr5-wg8ldj_cXu866SkynzNfMCF24XCpnT_Zt1ZlQhkq0p-VEfm0KWjypGsOw6EPHTTbdW3upcY3k4HxBMEUx68vWrLgH6tMLeZNIifLA6t0Ljd2ywuvx3AXFN8CUqNqsD__FKD_ZFyv9uGEUVH5AB1r64c3Q-A2snPIO8rEkAlTRkqSAUfFMdPY_-5RPwkPwipySpOYGWkr4pTddAlwDSp5q1vyQ3dmxJ6Lur73cACpQnzaJtm_Pyn9hW3d0epASRXppTomEX8w0JHYFhzR62LhBGMu735s0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=I-TOg5BpMdHmUOGuC0P1g7u8eiyte72IqJYcOUbCo6QwUhxuA3GxCW3z2gYubMtjKq0S_YLmQU7pXhVQwp9BJlNpbPNIzDkdJpF69-LUiYBhB2DHdIhDNiLqd5u8SSlcADIw64DJJ_kczM29nJ-QgbOIDfa-rbbJY77SfI_z2cmuMtHpPHRR1wigqTJcaU-nPCUizzjvWnElejJGnCidYLdTHy_G7_zBVJ-TSuFMILvqxEQKBdekxd_aqLPh6K9i1Rx1_0brwcKvKmAUcnJLhhUaNvWPjiFEgFCfYj-aYGMpCv0RBAZa515ErsuYCxE8sNuj6yMhjqFN48TqFncYBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=I-TOg5BpMdHmUOGuC0P1g7u8eiyte72IqJYcOUbCo6QwUhxuA3GxCW3z2gYubMtjKq0S_YLmQU7pXhVQwp9BJlNpbPNIzDkdJpF69-LUiYBhB2DHdIhDNiLqd5u8SSlcADIw64DJJ_kczM29nJ-QgbOIDfa-rbbJY77SfI_z2cmuMtHpPHRR1wigqTJcaU-nPCUizzjvWnElejJGnCidYLdTHy_G7_zBVJ-TSuFMILvqxEQKBdekxd_aqLPh6K9i1Rx1_0brwcKvKmAUcnJLhhUaNvWPjiFEgFCfYj-aYGMpCv0RBAZa515ErsuYCxE8sNuj6yMhjqFN48TqFncYBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=AnSM-Thc4stvc8osAEksQdmj2MK2bHEMD9d-K3P8C6sXh_QNmOKaQH_WsFuNPUsRL3jVqoPzZsBsfW31hGcMVfSYIpiDPL8uKhUW-GEsr_Kqp08W2dnuZYKtk574Ti8O-5qQMpXFBKEnpq6MolNJoJAHfVoMuzrjB7TDtcrln-h3M5KUwkvJ47GuBVKlRpiY2JtF_q8mLzjSAjJan7KWtpZoQGXFlJiQhtfiVIdUJxcBXJ1oxQarFmG3LDEQnNiF3JKiwpLLhYIpCBVnmjpowzSepEtRWGc7DGNACjTctloZLe1VKV_D6dvC-cB0-p3MY9d8mAnAWYmEoj3bIDvzGXdtvulANr1hhzWfstDng8nIKXrT8VNDhx2YnmlpSTtAnVyncFmbWeqpwu6KfPRWQXtTNq-oKXmwGJXUhgQ59JH62BJqy6vofvAXCG3nLR99bgREr_HmraKUjEjutSGxmqx3QOFoOFrLcUHfmT_XS9iDuhXHNE9oqA71-dcp84XcOIhJFMSrl5BSXmkwc4t8ULu7pu_2r6CiIrayN4XW70twHAt34vKQiHx8F1evgi0GXdau1Xf9pZzgd1S_cFdxZns6XIYpRMwD4bV5ng2ZFAhvlmJ6i5cS5qgP5mnHCX3ZUOk6ZSf8DWTFzkAC4d5tIGRwqLMlAYHhkD1aL-UFjao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=AnSM-Thc4stvc8osAEksQdmj2MK2bHEMD9d-K3P8C6sXh_QNmOKaQH_WsFuNPUsRL3jVqoPzZsBsfW31hGcMVfSYIpiDPL8uKhUW-GEsr_Kqp08W2dnuZYKtk574Ti8O-5qQMpXFBKEnpq6MolNJoJAHfVoMuzrjB7TDtcrln-h3M5KUwkvJ47GuBVKlRpiY2JtF_q8mLzjSAjJan7KWtpZoQGXFlJiQhtfiVIdUJxcBXJ1oxQarFmG3LDEQnNiF3JKiwpLLhYIpCBVnmjpowzSepEtRWGc7DGNACjTctloZLe1VKV_D6dvC-cB0-p3MY9d8mAnAWYmEoj3bIDvzGXdtvulANr1hhzWfstDng8nIKXrT8VNDhx2YnmlpSTtAnVyncFmbWeqpwu6KfPRWQXtTNq-oKXmwGJXUhgQ59JH62BJqy6vofvAXCG3nLR99bgREr_HmraKUjEjutSGxmqx3QOFoOFrLcUHfmT_XS9iDuhXHNE9oqA71-dcp84XcOIhJFMSrl5BSXmkwc4t8ULu7pu_2r6CiIrayN4XW70twHAt34vKQiHx8F1evgi0GXdau1Xf9pZzgd1S_cFdxZns6XIYpRMwD4bV5ng2ZFAhvlmJ6i5cS5qgP5mnHCX3ZUOk6ZSf8DWTFzkAC4d5tIGRwqLMlAYHhkD1aL-UFjao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOYqKr3GsIFrimyJ075PYmAjIadOcCpNjg3Uaq32bBXJ0e3BwA_u0GtzjGwzr3_59bqAgxssj3Q26Mr0S83ASPcHdWudAe_U3iSo7il0xA_T5FiEb7ZEdpg8VmWSGLAzaIcD6bBSwG-dbO2kUYADJOT-pP1VCCGfrVzmuKMnOg4M5BXcXAZUnkZMVx2PqKtVO82tdrdaKbcaEdIjFEEgnkQOgqEEp2vaiIMn226apIkqdpeNS-goC0zOmoKOI-VcIgv8owpwjpnUSuZaPTbc-tmgNP4tjt7H_UrGiJREESUDzRbYVy8oM1HO8nRbous6WyHdxC5I9we7cf_f9VuylQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=No9D8tPOyxEDhygXj-GlIt1QxTAE4vr8xue1OkqE5gYS-MmJdaEPHjQXui3-0g_WhFTCFQKTJks_5C25NDWIb0lPAFeqMZWoBMjJ3tw-luLw2jMS-v9f5xUvLKCWK8tu6ZnkHn6gVPuUx7ruInJac20E-zFayyS1fze0nE8XjJszCxtO2DVT6h_1AUHJJ_fXPLgxHLy1nE8x6-W7mhCW7X6E6-dkNlxreJq8KY1NOnNtgZL7aEP-gfz4jnWHpn8yr-F40956_xheW1e_ul_jl1HO16Oj4hfsW_xXINbmrMh8Lg_GcZFfm1Wyy1UWgyHo7P9hKBdeNZBm2Ns6U06DFzsdgls_PFz0vfig9Xq2RTsg4R1pEk3kDDIGXj9S9HApdUgr3K79Fg1F3MQEw2xfuAQbvLq1k7DpWpMRkFO7iOnReqshDB7h1lF7EkdpOzktY68PXmgEdDIHipLUulk_ztdu2rEjd1O3a66FeLQaF2OSfRnBoGbJpqniyjqOBiq9ofQjNfm80jsLFLwcuRMuHo_dbdQ1V7ZwODbYNuq0ZK3bZ9tzxq5HCLmUH-8iF2XpVq2Vxqqdn2-niXD9KVPNlcBO9bXDR9Q5LFV0TS94O9Tj1KbiEIE1JCEIfWwMya3Y4_tzfLC8t1rG_W6g_FDfGH4t2kdnqivAriyoUDy9rvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=No9D8tPOyxEDhygXj-GlIt1QxTAE4vr8xue1OkqE5gYS-MmJdaEPHjQXui3-0g_WhFTCFQKTJks_5C25NDWIb0lPAFeqMZWoBMjJ3tw-luLw2jMS-v9f5xUvLKCWK8tu6ZnkHn6gVPuUx7ruInJac20E-zFayyS1fze0nE8XjJszCxtO2DVT6h_1AUHJJ_fXPLgxHLy1nE8x6-W7mhCW7X6E6-dkNlxreJq8KY1NOnNtgZL7aEP-gfz4jnWHpn8yr-F40956_xheW1e_ul_jl1HO16Oj4hfsW_xXINbmrMh8Lg_GcZFfm1Wyy1UWgyHo7P9hKBdeNZBm2Ns6U06DFzsdgls_PFz0vfig9Xq2RTsg4R1pEk3kDDIGXj9S9HApdUgr3K79Fg1F3MQEw2xfuAQbvLq1k7DpWpMRkFO7iOnReqshDB7h1lF7EkdpOzktY68PXmgEdDIHipLUulk_ztdu2rEjd1O3a66FeLQaF2OSfRnBoGbJpqniyjqOBiq9ofQjNfm80jsLFLwcuRMuHo_dbdQ1V7ZwODbYNuq0ZK3bZ9tzxq5HCLmUH-8iF2XpVq2Vxqqdn2-niXD9KVPNlcBO9bXDR9Q5LFV0TS94O9Tj1KbiEIE1JCEIfWwMya3Y4_tzfLC8t1rG_W6g_FDfGH4t2kdnqivAriyoUDy9rvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای، (خرداد1384):
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68724" target="_blank">📅 19:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68723">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-4ysiTv422aM7LtwXWBV1bVSmb9J9Itk63EuiW9kXUNM4oc_vj4Vn_9rQqBXOMMGmkDsKPThfX1YtZWYyPWypAF9MOHNq_4YHzjEaVh7jzwSCZw1MP9Pb2f02AZjO0HnNUfbDtPOtCFsvaoGG3IqOfpzhn74mafEr27rc8tat55DCq2UBzc-s-C7DrFRRck_QXgtdCes_-awFxfxPtRSofhVYjWdMoh98LmMUTXJ8j8Iw5WNwR-gvwGWrj1G-cPwHhbUL3lSOsd539QZAiJS2aolUgRwrYlvHtaG0Sh7F30ci8QryukGORThlMdO2SEDziDcUqSAUq4rTIm3aeOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:  این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟ این گل‌محمد محمدی، 23 ساله هس. امروز صبح توسط حکومت جمهوری اسلامی اعدام شد. تنها. بی‌گناه.  @News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68722" target="_blank">📅 17:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68720">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/mzjqsD74qW2SrnJW14cubYOG-LpXVXfPHivsDSSLJ-TxhtLB_s5p4CgNrdEBUljQjRJZeP_pLDvQIOmehhTX-ep4TkL1IShGKzYeyXu9gpRQKs33fK4ZLErs9GjH-wP3vtUWMM-7Go6Idc2k4BwO-0pJIumnRa_gByTZGfw2hV2A7Bxf1MXW5k5jNGtHBLKIFs9SgSOpWZm9wGOjII7KPNdgUdewVUJAZJcY8iEx9MtZBYzdumx4rdJKzaEu5J7bvJBMVe0CBrp27GMrl0XATr2pmxJtlBluaeTtHjFOdD0qTopWepnxgCodsIeXRrLaWt4wlVqKVCwxLAwHqL5ong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/vFczr__XIsQJyxeD6R54k18mLTVPJOfKqrrnlFzhBTgynO1zBZIMUAvps7YBN_VILdq2LSsVxv9NiuSN81bLf3o_JqmUdKgjuLSXmXWYgVMmJ3Jwd9B1fs0KIvAOjhXgDhQ46Hbuvd0fuQjKsGTnrJBVYNkCMtk9HkAVs86D7IXoMbH2KhnF0ZQK8zjhnzT4Ebe0ToaZKomE3FSKbX68SF1G8TWhDoYfX2vCQ73hdeaTDnMfWGhrRbc-guB9MF7o88tKu3--4ea5kqXSUGUNFGAzNe0Ok_IgBsYKFXVWPDjjWxxNW0c_XD0BewooUddC1k0XWv11qu2inHnauzLY9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=aAp0Ap5ptwCtaEtru4kCVQNeAmDez7dqIjsxIQa06EpY_D9dekxKoUR3T_4di7mzxdbtU1CFii1Xw_nNnIvv0-2QJ5ZUwVgWB59tHMVNhqEhuaIMlIMCuLQGabQxcZ-9bkyJsi70AcYjLunxEwdWdZSPIXZOC9N2PTu7aIfyixNMPzGTPHxAbUy72ZK6hXmkOTt3zDnYcbJg7vK_m8GruEXx8FI6_WVtQnNrjFFiLHByl1QK0PBAHxuXth5GCnPklFE9WF8RG_HJM8uCFkIeqta7ugfyhXXs64_Pe5ApJ1CwK7IB3WFQboDUzrBgB9YPefKOAPlDV87um4R7Gl6-Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=aAp0Ap5ptwCtaEtru4kCVQNeAmDez7dqIjsxIQa06EpY_D9dekxKoUR3T_4di7mzxdbtU1CFii1Xw_nNnIvv0-2QJ5ZUwVgWB59tHMVNhqEhuaIMlIMCuLQGabQxcZ-9bkyJsi70AcYjLunxEwdWdZSPIXZOC9N2PTu7aIfyixNMPzGTPHxAbUy72ZK6hXmkOTt3zDnYcbJg7vK_m8GruEXx8FI6_WVtQnNrjFFiLHByl1QK0PBAHxuXth5GCnPklFE9WF8RG_HJM8uCFkIeqta7ugfyhXXs64_Pe5ApJ1CwK7IB3WFQboDUzrBgB9YPefKOAPlDV87um4R7Gl6-Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمعات شبانه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68719" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68718">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1fnC6oxZtlmjkcwZ3CbmXv85GmugzR7-MSNx1Jb0TTjqlX0MMAmMEjFgzDteE-yPi-2d8Nq_xyM3SbTZtNRZujMzJkMzsxGkoJpsgaTLd1gFrtcloH_ekCSYI8Dz8pf5St1naNupKVzNnd-X21hvJhKjasFr0v_FxveFDnYS_w-sqB0vzPuk8htGWA9qdeopuCGWBxXF8fawUX9Rx2TxZEC08_Fz3M13u1ylUGW5CPAmsdZzpiEO5R5F2W8Pq4ZVz8DkTCsd-eV5mRB6uuPn5fuLVNKn7dq3sh0X6BvvteH_k2XLkVNh1pKgh51UOApPJt1-tfQ56Wbu4Ze2I9lNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هویت نظامی آمریکایی که در جریان انهدام کنترل‌شدۀ یک پهپاد تهاجمی ایرانی در پایگاه هوایی اربیل در تاریخ ۱۹ ژوئیه کشته شد، گروهبان «مایکل سوینتون»، ۳۰ ساله و اهل فایت‌ویل در ایالت کارولینای شمالی، اعلام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68718" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68717">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da37587eed.mp4?token=SHn7-XABlTaMfkZz-Qa5galQa0V4XirKgr00d_Y-6WZzekzj20WxXGKlG1GOEtLW2JJDC3snQ56lvKeGwBf8NFdI2ZoPq6BuTR9WCd4XHYCIQqAwIWy8-LkwE2cFReBNfnlIrJ6yQkE-rNz3m5L58BwdMApuWTZCqiFr2M_y-MmA4PSB6L1MAG06IQVVTIZDCgSO7ttp6gcZ-9Vu0zSpKT1e3_SeRbixgf_4kpbPDnh6CQ0KU6YwYGXc5ai08JmArVkR9iBDYZ9Dy0pkfnLy_Q4ojD4tagkObQhLRTLLUPOiEanUubJKQ1RdqZFGtJGv4xpxQy4hm4hDqixUYCxJ-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da37587eed.mp4?token=SHn7-XABlTaMfkZz-Qa5galQa0V4XirKgr00d_Y-6WZzekzj20WxXGKlG1GOEtLW2JJDC3snQ56lvKeGwBf8NFdI2ZoPq6BuTR9WCd4XHYCIQqAwIWy8-LkwE2cFReBNfnlIrJ6yQkE-rNz3m5L58BwdMApuWTZCqiFr2M_y-MmA4PSB6L1MAG06IQVVTIZDCgSO7ttp6gcZ-9Vu0zSpKT1e3_SeRbixgf_4kpbPDnh6CQ0KU6YwYGXc5ai08JmArVkR9iBDYZ9Dy0pkfnLy_Q4ojD4tagkObQhLRTLLUPOiEanUubJKQ1RdqZFGtJGv4xpxQy4hm4hDqixUYCxJ-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbxNlCfsAYyan4htJHjRD2P-YUk9ZHjC-C1Qn8R4-pyudvQumLmQs9EOp2vmsVl2HPxZLqcD0ERfhq_pDRKHdj4A1K5GAiVtJ57-jKZFTtMBQ84WyO-xq5XUjgsVhZapQf0a_iqRBIELeXks-GGzBKIyiiBTWRVOCcCARh7bk5jnw9rpq2annvCP3VNpD5cODo1WiCQIwrQ2GrEYoXifHWvJJfiX30Qv5xqlpsL7_4xv7SobDE3hUUJQfmb3wHgB5hV0yK3OfynUIutG39CfuYHxNLHC0gL31gfUWuML3rOhlZFfFDV3Fw6RRtbN4B84zEvgVv-mCsMR4b0WwRJN-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBNzBe1JXE_lUnY_q-f41WWq7awKYNdoiWCUw1ayxWPKETzbFD0f2x7eBH4kudRL4RiR5S6RfmtEQoeD-7OK_RcHG0H0ShQLXmlcGwx-eUMFJnregBiLR-JIniWJ7KdxAlaY01MjPYVSD8RXxIm6-inUOLKpzvBl9YPzn3wRbl90HUfiw9p_4Fi3-O9_iViI4svzj9ev5j5ADjDQX1jZquLHvrpL6FpG2-zeRXnjFt35LmFroCaIelPoheXzj1X_Z2gk6oUadRRn9NfwuZNafSIeH3ARN1KtFhPY602fqFKn_TX30DtzAJJS1hJ5zLH78AeWx0eSj71wR2yKsoNASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مراد ویسی، عباس عراقچی رو فالو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68714" target="_blank">📅 15:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=dCj0dR9OkqaFqkiRyQBNLXNbumxn_ToiGR3PiOQMZi8OJlYCaUnNX6zERPg9IGZUpnzSEvKv8d089RjigS3X2NDYpb6pqClCwHN00oE_GxTiYfTsOqupmS3v-94L14pKfhXEOZ2UYk8bn86OoRZBiiHC97dHL9O3DmGcnVG0FCbhRSIAjcTFBQZBheWX5gvHv3Cty_v4Qj_2f9krXO48qm_J2gmz_g7Ca67Yt_F9vgpsoiM5HMNxRGYhFwOPX7ZUHepBzplPkJSPqvzOr0oDkf65bxPzmemkXHel74N_ZeIbsP-w-QuI7n3Vq_0xSD4rgns4BaVbWg_J9n-SsNpFUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=dCj0dR9OkqaFqkiRyQBNLXNbumxn_ToiGR3PiOQMZi8OJlYCaUnNX6zERPg9IGZUpnzSEvKv8d089RjigS3X2NDYpb6pqClCwHN00oE_GxTiYfTsOqupmS3v-94L14pKfhXEOZ2UYk8bn86OoRZBiiHC97dHL9O3DmGcnVG0FCbhRSIAjcTFBQZBheWX5gvHv3Cty_v4Qj_2f9krXO48qm_J2gmz_g7Ca67Yt_F9vgpsoiM5HMNxRGYhFwOPX7ZUHepBzplPkJSPqvzOr0oDkf65bxPzmemkXHel74N_ZeIbsP-w-QuI7n3Vq_0xSD4rgns4BaVbWg_J9n-SsNpFUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
