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
<img src="https://cdn5.telesco.pe/file/KdZubS7lfsRTbfAjkIXcZWNpnTocd6t8JsdiL96uR7uYqpQB40aC0vIDKoYCcMT_D9FIt7TuLRe1Wxo0P0E-VyYJJxQA1tGomU8q9Fs-jkyC6Leg3Uz3zQrTZ6Y_MZYwlxKsUfafeN7UChnCQH1CO7Ec59rUoVqX3uLJAKzeMcy9z9uuM2MqlGgzFm_SDWbdkATNrB0fCQJbJlI5rbnV4iSw_vIZM-l2lc6hQ8-o-qHYfhtYQzR6c1wtk-6Iz0Fmds9UkzRFaHgdVW8bJixRFyNE7C0_KwQPqBVo_Pbet7Ilealv2VU-YvSrqL64jQt558ffRFy3KmgGir8VMK1v6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 406K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 15:01:28</div>
<hr>

<div class="tg-post" id="msg-107004">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxbgHsiuAOqCBjUkWec-nMkxIhSRAxH_R_fn6AHWirJD-fPAPsLeld__Ja4ti3-2eoYiE7j56JcoFShcY3HfWwk__ed0a7yxmxKpFHGwxKDoyuyrcaPE8IFrvL1rjI6h912VBbaVsjUst_p8olsUrvGFzQLMvk2qotdJjGcwEhSbv4E7TAGNeTEzoCQ0R62X3HhTu1Pst0OPVu5fHsYqoSf5EnhJHzbwW39C1wVoReZwVA-JLkkNmdwu0y575FKijvWpDrS3fZKJsFFQDryJQdYSSmLiPbF01wv_8kBie84XEfkFnE_7SoqGZIV9I-jgsrrYsFxZdXlFulwxq0TqIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/Futball180TV/107004" target="_blank">📅 14:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107003">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBJ8fP96VsY-JupBNKMAEiDfFZ_B477T6B84z6k1x0vqirSCpAvynT5PMXixPGSjCjBigChpJtN1JmKuWmcBsqpNgF7bymwA57P35U10Q1ce6nvhJ3dwAc-rFmFMmwx6OlMf8wZz2FMyIekNxCx432pcrvACeu2vxWxVVlfnskUArGjYW3aAE4hEyaNGInxx9usaoQQpk2F3za6RULnv58a2acpYNHL0fSUip84SkNxkfOISTygT3M3pyJ9iwWz40TIa1iTqTfULGB_Bxd2zRXNcRjDHHL9mxPd4CV_kSFYoP7jpqJjQlGD0HLZd71Cr4aL5dQanzb2lLGQ_OMM7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد تیم‌ملی اسپانیا با دلافوئنته تا سال ۲۰۳۲ میلادی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/Futball180TV/107003" target="_blank">📅 14:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107002">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=Iw0LMjvC3jA4RJN6xd37YEcjW5fEO9qUlODOeOT2uh0-xeRF4PtRlhTnfXTP0s3mBGPRbgvX2mkchcFvksViKJ58BZ3mqhUnXGqyos7PblCm5FQrIo7aSMBkh4RcQVL21CkwN7QT6KNniMIAfYZsvvrOKnnNLqGHC9gWKQlxzT2OrCqcyFoj7Xq7oG73BBFmpD_3w2jcHKoRyN_fAcOhDtyFpMk_WNuP22BaT6w6jAD_AfYFG4b6v_6_ZuqbuHJgbWc6U6T3pg66cYNoqMRgyclAL7rXROG1MXDcqGz5PIwpz8Dg4gfXPjByr24nQrSztDaAYDkHqwbKc5xR3TISKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=Iw0LMjvC3jA4RJN6xd37YEcjW5fEO9qUlODOeOT2uh0-xeRF4PtRlhTnfXTP0s3mBGPRbgvX2mkchcFvksViKJ58BZ3mqhUnXGqyos7PblCm5FQrIo7aSMBkh4RcQVL21CkwN7QT6KNniMIAfYZsvvrOKnnNLqGHC9gWKQlxzT2OrCqcyFoj7Xq7oG73BBFmpD_3w2jcHKoRyN_fAcOhDtyFpMk_WNuP22BaT6w6jAD_AfYFG4b6v_6_ZuqbuHJgbWc6U6T3pg66cYNoqMRgyclAL7rXROG1MXDcqGz5PIwpz8Dg4gfXPjByr24nQrSztDaAYDkHqwbKc5xR3TISKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
🇪🇸
بازیکنان رئال‌مادرید و زیدی‌هاشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/107002" target="_blank">📅 14:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107001">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH1oGu_fQOVg9jEyg3G5JCgJA076OxqakPr6Ogm504Au5QisNegppNzG23kNbTinAyf2bRgT98-sr1nbG7FvOs8LZVFISdPKgY_DlZ5yCRsLwI34RTTLpRIa5iIiVaZFp3nlje7ruKKddE19zgFx9EQz8Fbt7XG6ws30tKyO99sk6YCIH70Qg6U-SxvmDA5lUTmNGJBDmQ5hZd3zwYWybREIF7dnHbJnmuYc5yVlNYmbRSnYInlJAUF3pAAmOIuZZUYZ5Zhm6L73z_d-b6_339tzcTrAZFya5cOE5ejmhi4zQhxutRGo653NADICcC86gC_q1kk7gnoSRStWhyOaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین تعداد گل رافینیا، مسی و کریستیانو پس از گذشت ۷ هفته نخست لیگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/Futball180TV/107001" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7xn5MIsg5xrIPljYykE1Buxx0THJORm7V092mqEsSZRxiB5Jy1SMz3ltlNbmSWnpVuGitvpqg-eayacJ7WAHhGwB7Ds3dXtfdvV1x2UvOdM3exU7yTBGA0GhkYyXtWmjS_r51BgRKhBL0lHDcSpaSpbiZ-i1-09GeDcHPuqJsW7yInC1gL-6ECWOhfBdu6dgp57IH1fqTIM_ED0uHjaN88WER6-2ia0ef6sT6RswIHdPd3UzcMTJQyonIpRAQIL6gW-YIgFUTQ0kSmYtABUfMkuJfCG33YG8aqnapuE5LuBRX8-fZxx6_ml2q1uTsg2qI8XkSWwcENaREFDfLB7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/Futball180TV/107000" target="_blank">📅 13:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=mrTBX2PJOegaBx4-Ssql8Ul4usmfyMcr79iww_6KWzDVkHFej0DG5ewyQbPDmAASUkxjCPEsyiV7JfhhQHrMwOjlhzMJg7bZoZKuYtFRYBvoKjBvwXbWrYARgmJ6-YxzcjERGqw49EYpoYNAVK6N5sZbkfsAu7V-Zt3U-7bSKQ4rbuzteYq9feilDFiAnpSFJmu1WSuR229vLe-L4gtMMV7dsUEBkzDfMiDl5n8QrxXvFEKxGtqHRacP5eQA_3NSePfGbmyrXauku_8GnX1Of9-jQil132C2Ih0WIeu5DK_2v95DIHDjg6uef3V9SsnhB4LIVl_FNwwjCmQBXHZqdIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=mrTBX2PJOegaBx4-Ssql8Ul4usmfyMcr79iww_6KWzDVkHFej0DG5ewyQbPDmAASUkxjCPEsyiV7JfhhQHrMwOjlhzMJg7bZoZKuYtFRYBvoKjBvwXbWrYARgmJ6-YxzcjERGqw49EYpoYNAVK6N5sZbkfsAu7V-Zt3U-7bSKQ4rbuzteYq9feilDFiAnpSFJmu1WSuR229vLe-L4gtMMV7dsUEBkzDfMiDl5n8QrxXvFEKxGtqHRacP5eQA_3NSePfGbmyrXauku_8GnX1Of9-jQil132C2Ih0WIeu5DK_2v95DIHDjg6uef3V9SsnhB4LIVl_FNwwjCmQBXHZqdIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
اولین گزارش سعید زلفی در پلتفرم اینترنتی پس از جدایی از صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/106999" target="_blank">📅 13:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXaqbuidWjrBmfcRe7DKwsTgJCrfLeYeY44XWQJKjYqh5SYZAPJbuuA5JYal6plTbNJ-kaPCeBTetVpAXeopCIv6BYz58KwT0jLJB3UCw1B5ZnPFoEbmof7sCT1d-ccjBGxrDn4GjjB5JDAjSCi3OxJI-mNz7WUoDnAKP50ogzoyQ0rZkL7qBagXoOwUxaw448iKs01oQCHUxvD2lT6sEhsKB9d_To8fpVkDz64E8ywcyU6vTmiLk1qtKYF2hEPg11_nnrY4b_6uB2CxHRFxG_tuIJgj063RfItS67hm7TWpPU7gUERcbPLwacZHC2SRbCC3NK2OnIjb3SfraO1-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔴
اینو حتماً تو اینستاگرامتون فعال کنید!
برید:
Settings → Data usage and media quality → Data Saver
با فعال کردنش، اینستاگرام مصرف اینترنت کمتری برای لود عکس و ویدیو داره یه تنظیم کوچیکه، ولی اگه زیاد اینستا می‌رید، تو مصرف حجمتون حسابی اثر می‌ذاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/Futball180TV/106998" target="_blank">📅 13:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-QO6j4Rzp0HvTi6MDZ9T_Sva_tQaeA88wbmOJeLrf4TzfTSeCfpH-dZlCTEmwJ3xUQdMHOqpm0B48zbeL64QphJOmcrOFMsM5u50mbibuMEdQd7G85_mQjF0RG4XIVngF3xHUGt7hwWb5hA6j343bcXHGKGFqoEoQTFVNk_EP9SGlAp6Q7lsB6ZPaehSgrmxJKtDIPA6tG7PcFc3o8bWu8B-dK0c6ld4FRbvg6Sc9KUVwcsS7ZkC4iMuXUO0GFO9aw7RQ1hpeaogeYOqTAEoxzkXjuXBo0-rdTsIxVLdGqTjIlIMm4fGoR2Ui6Wz1Iw-lcttf8oEGEuFZ9OWrdaRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🙂
استاد گودرزی
: متاسفانه پارسال نزاشتن پیاده تا آرامگاه کوروش بزرگ برم؛ اما امسال دیگه میرم
هموطن راه در جهان یکیست و آن راه راستیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/106997" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=BNj3i2d6mbkhAztd2nsbtYJO4qP4bK6LGTeHWPnTuB_hLAI0djw6AZpheySWGPIXFGlV7AJ67U2MLcYILIxCdrZZeaS0J--bT-RY2PpBqZ3Pp9ccREDi4zWvgAZgInUny1Job9VuCCH6DbiW6zAI3ReFOr3egW3cMdt2eDZqesUOxt3kxEfO_4KCJNYN319iQmwxLHtOFOMSytQlyIs32gKlMYANehYkTgKB6lhlwqLR1DqwXHy2rdMXfvfsuhn_bKV-vcNZTzDvhUy4Kj2zlnX8tR2QwJv4w681xFmC3FVndv_8pI8lhymcCK3JNLAVluoRprw3h4VR2Sn64_F9qIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=BNj3i2d6mbkhAztd2nsbtYJO4qP4bK6LGTeHWPnTuB_hLAI0djw6AZpheySWGPIXFGlV7AJ67U2MLcYILIxCdrZZeaS0J--bT-RY2PpBqZ3Pp9ccREDi4zWvgAZgInUny1Job9VuCCH6DbiW6zAI3ReFOr3egW3cMdt2eDZqesUOxt3kxEfO_4KCJNYN319iQmwxLHtOFOMSytQlyIs32gKlMYANehYkTgKB6lhlwqLR1DqwXHy2rdMXfvfsuhn_bKV-vcNZTzDvhUy4Kj2zlnX8tR2QwJv4w681xFmC3FVndv_8pI8lhymcCK3JNLAVluoRprw3h4VR2Sn64_F9qIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
لامین‌یامال از مدعیان اصلی توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/106996" target="_blank">📅 12:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zmq5H4My4Fg5S0cJi--DeCiRQxVTDZL71GuHlYB2TQYjX2GQzcE5bzogUDeRQizfg7L-BYc71nAueBHM3GWbbX5NYJ8ZU4Y2HWbt4ohz7dWJZPIsV2qH3uwhCP466l1LrzXS5ofytmznD5XK09GamWN_f4js8YJjeFmavZbArjiPyjBafwswam0I6ibtt72-xE9pPCnTVlzAbmCdlwFoHNoL9AlXHbmqjVScXXjYlVuk2iV6Wn8EG96FDaL-ursugdC3GJ2qtJTi_e-UXgyzKWszivRaWRIvALfGySGu9DRYNo0__yJetNrEiccwkAlbP7VKA6Ic9Bopxfgaqy3cDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/106995" target="_blank">📅 12:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106994">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THGD2oQjSw0uSgRcmEwLJ02C_2dfGUY0PJ971mz0UTadobtdX9CBNZBRztTa-dJM7PH__ThZUSJvpY_ePBSMnXC6PTJbzlu9wI1lDr3iPNvV9V3ito70vGht_3xVi-1pI3Pbkb9ULJJN4UMjiGfWp8Xq-GG06nHwzPhOlzWB2nMvALrmCo1NgB4GXFC_yn-LA3B2WnQMt-skYS0svwROBfajxiHKNi04DdTJ1aaxRpoTOAyUjGN0Vqkuz-NkWF35JVXxyQEyVPNOpfYybS2qDVjw4WrowcybCCgE_gNyklR0gxZev7M2tak8ex8PrneQqk_aG2Uayp3UH9fzHJpx4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫡
🔥
بهترین بازیکن فعلی فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/106994" target="_blank">📅 12:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106993">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1dd2f2cd.mp4?token=CGR4ISDnI5Y2k7w00CgLK7viZ34PL2PHcn6nzF8jaU3bm9UP_lkP1ZD-1RSRJtKFM7EOduXde2OwNw4IQm2hzMQn2i1vNK6nR0R1IIni0rLkYSAHh3jPssaKpOj2bxuX5ZR8dxz_hNkUzgo2lfZE40WVVebOuZKxpYkC8dCNV1XG5WUPHU21PrFnDx8sqIvmRVqE8vJRtju74tNjYFEDOjs4rbTjU6r92xqMBvHemS21Z6lKUONGS2voJEhEZMdt2cIzVjtZSjCIIW5WgGUM7BY-PSFo-hVYAbR3l-F0n0U47d5E5l-moTozDUj2xAz-qCXhnhhsoDDS6ykhJXeNxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1dd2f2cd.mp4?token=CGR4ISDnI5Y2k7w00CgLK7viZ34PL2PHcn6nzF8jaU3bm9UP_lkP1ZD-1RSRJtKFM7EOduXde2OwNw4IQm2hzMQn2i1vNK6nR0R1IIni0rLkYSAHh3jPssaKpOj2bxuX5ZR8dxz_hNkUzgo2lfZE40WVVebOuZKxpYkC8dCNV1XG5WUPHU21PrFnDx8sqIvmRVqE8vJRtju74tNjYFEDOjs4rbTjU6r92xqMBvHemS21Z6lKUONGS2voJEhEZMdt2cIzVjtZSjCIIW5WgGUM7BY-PSFo-hVYAbR3l-F0n0U47d5E5l-moTozDUj2xAz-qCXhnhhsoDDS6ykhJXeNxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند ویدیو معروفش که با هوش مصنوعی درست شده بود را بازسازی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/106993" target="_blank">📅 11:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106992">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETmKAlVE74prLjXPC9W84fPtaIcaXv1_ForWWJj8meFA2lN8eFnkI3pNJZsrKRlmSr14CpSftMPUjTjQXyh40dQy_4v6Anz6aOU5nvS9dnxBQTVwJPJ8vwWzcgT5EC_35IxGL3qeEZRkifE8Cw84t3aeAepzNglwTgs5MNiaXJTCOFuQ_DG-diWtSkaLcj7jZ46G_kj6AFywx9qFTZpCFpZnSPq3VfQU-PALkxJ5rc-9-m1AOP0sz5_BMu0mXOriSowz5ol-aym9gYaj_mnfNapDDG-4pSGA-8m0lnyd0kVOSLbM-9gsdZv8lMBc7gW8Duc3o3bJBYF65ifGH1HDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
‼️
اعلام رأی کمیته استیناف:‌ اعتراض تراکتور رد و محرومیت 4 ماهه خداداد عزیزی تأیید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106992" target="_blank">📅 11:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106991">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0476c7864.mp4?token=qn4FiJTO7lgqflGrFzHGydsumFRkMo11o5N3o3TbgE12L2TE-YKM_haNEJoHoA0qr9Yv6CJ-8-8QlGkLmk6YYMqua3qJepoW2nlA6roySzBuHVeqbvjdBdXFXSfkgSB5GQ4-ZrO1PvW6p3HoWP_IYXxgQToGfg27EiyqvVKZLzOr3N0dZjZRUkTS_tDL7cttxeMpMw5w9JTUVXUrkVCcoI4zKnimFRxvNXWUmk83RtHoqrhUIpxdQFEeLvSeDCFV_HwUybOSFQL3P1pEwnV8_bSwWYY5XOD8BuEq2G9du4wijhK8xdjRefr9B5T4Z-sdBJk_VhEOIDum34CQfzYHRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0476c7864.mp4?token=qn4FiJTO7lgqflGrFzHGydsumFRkMo11o5N3o3TbgE12L2TE-YKM_haNEJoHoA0qr9Yv6CJ-8-8QlGkLmk6YYMqua3qJepoW2nlA6roySzBuHVeqbvjdBdXFXSfkgSB5GQ4-ZrO1PvW6p3HoWP_IYXxgQToGfg27EiyqvVKZLzOr3N0dZjZRUkTS_tDL7cttxeMpMw5w9JTUVXUrkVCcoI4zKnimFRxvNXWUmk83RtHoqrhUIpxdQFEeLvSeDCFV_HwUybOSFQL3P1pEwnV8_bSwWYY5XOD8BuEq2G9du4wijhK8xdjRefr9B5T4Z-sdBJk_VhEOIDum34CQfzYHRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
‼️
🇪🇸
ویدیو سال ۲۰۲۳ بارسلونا وقتی که یامال ۱۵ سالش بود و شماره ۱۰ بارسلونا به آنسو فاتی رسید و براش جشن گرفتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/106991" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106990">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106990" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106990" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106989">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTCM-t2YLytlPFuXaAwgWi8V5wFgCfIj_sktEpf0MW-i9yFDrv3qPfuv3CSCoGQuGZh_xI2IkPrzRwE4VAOSaQWMezdu_AFCkR8ofk6gMKuP3yc8bjMLpdC99WJyG1rE2vJRUwGDYGnotyvwME5qCqu8S7RNj9QGz5W0pp45D07qG-xCNaKFaDQrfp87KoyYxjopJrVQsD2obb3zVoB54-D0ReC4wg8VAG0w1ZQHv0J3saJZ_ud6f4QznNmCJbX2CSqJa29LTHQgOgdIXq8-y-HxvwetS9P3NllG7SmP5Wg2nPYbO5KuJQjXSbUFhUwzo4YeCphuyg8R1oNYHaBmNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/106989" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106988">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ee4811fc.mp4?token=MWkMjr0j9TsXtoQtBkNfWYnIlFKkjPipWzS-IyQz4JEdJqZjG30rS7qt1KoFMHy0LHiBRBslf5Xb2p80ZB5Nx6yLlSB7MPcourp7oAl1BtHvEr_deVBQdKMJTtBZqaDg1bCvqv3zTma2JPU_l6OGkIojQWDA5_Ub2CT3niFfXcx0Gr9mYJKKHxSeUuc5DScbEoyYe07GPNTYPZZMhFZ5hnRE6HEidK4z50ysfPnsJ1tLj1V8E16JDHAwo4p2q-fYJzogvIzE3GnDDdYKmYVBGkNVsXT0YB0jCUf_nLKsRJr7d1ZVedgjJ0NPi1c772yPWX-rirsw8tZMIoveg5fqhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ee4811fc.mp4?token=MWkMjr0j9TsXtoQtBkNfWYnIlFKkjPipWzS-IyQz4JEdJqZjG30rS7qt1KoFMHy0LHiBRBslf5Xb2p80ZB5Nx6yLlSB7MPcourp7oAl1BtHvEr_deVBQdKMJTtBZqaDg1bCvqv3zTma2JPU_l6OGkIojQWDA5_Ub2CT3niFfXcx0Gr9mYJKKHxSeUuc5DScbEoyYe07GPNTYPZZMhFZ5hnRE6HEidK4z50ysfPnsJ1tLj1V8E16JDHAwo4p2q-fYJzogvIzE3GnDDdYKmYVBGkNVsXT0YB0jCUf_nLKsRJr7d1ZVedgjJ0NPi1c772yPWX-rirsw8tZMIoveg5fqhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدای کم‌گوش بدید
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106988" target="_blank">📅 11:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106987">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9186ccb478.mp4?token=UTI-wqX-x2XtVgiELbUv6cjrynVla_CVZA3PPZ7bN-ebYTJns63uZNztn7pLQ7TenDbvQk5Xwsz0pjmwLUfdkAUcw9Yw7ZuIw3K52fBcQxLqKhFfL8dZC51gedSkkhXD4EDknOiOpac4MXNB4yUGW68OgML8yk1R5eUVdNLeZy-YQo_fVxwDPEHWqabhSY-oWNifyYWgkz7paPsytXUIZHXpL6zp1Yp9uzfLWLCEHDzoN7bDLtiU0y-YV7Xo_FQwCHVIwkAptM59l5U1jmrsR07NjVoZGwd9hyrel6Dyom0sVhBQklA01TJrx2qbSJC5LfgYDX6d-b0S1nVpXMnjXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9186ccb478.mp4?token=UTI-wqX-x2XtVgiELbUv6cjrynVla_CVZA3PPZ7bN-ebYTJns63uZNztn7pLQ7TenDbvQk5Xwsz0pjmwLUfdkAUcw9Yw7ZuIw3K52fBcQxLqKhFfL8dZC51gedSkkhXD4EDknOiOpac4MXNB4yUGW68OgML8yk1R5eUVdNLeZy-YQo_fVxwDPEHWqabhSY-oWNifyYWgkz7paPsytXUIZHXpL6zp1Yp9uzfLWLCEHDzoN7bDLtiU0y-YV7Xo_FQwCHVIwkAptM59l5U1jmrsR07NjVoZGwd9hyrel6Dyom0sVhBQklA01TJrx2qbSJC5LfgYDX6d-b0S1nVpXMnjXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
تعداد‌گل‌های این فصل رافینیا در مقایسه با چند تیم مطرح اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106987" target="_blank">📅 10:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106986">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxMx0wJkst91TrYqx7v5UQ7DTzwZnbLEgrO0uUNOQe52MdOiQMtCK1WP6uCAp6yEaDDB_d_Ft-hFCPYVcpnsTnopzBJ4kwu88b8JHgECWTGhuXTgH1AtdLkl2QMCkCSAR_HOT3cr7ArcnUgXqSo1V71OS30F27A4FIKPdPusEHT6yxYJwlZ9V-eyOIYlIWPOJB232w6kmZQk-JNzpcC8djGw_do08twpMMjUf3qYapcQXfeh4BqpMTX-jsN41i5Xw-Sfz-lPTjnfArX8n4TqS-Xt8zp4pmd5E7rHmHI3mOXp903PUmKrAiV2ebla6PTNMRSZfkDDMQjBk-PDjzorFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
احمد ایراندوست از بازگشت شادمهر عقیلی به ایران در آبان امسال خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106986" target="_blank">📅 10:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106985">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a7263425c.mp4?token=o7ojyut6bm4Ur0GDCnc9bcpgskqmLhta3Eym10ybzkUj6SVSGK7ToBgOB7KF7tGE-PAn6yMBEGfv5EWcKIuwV7sZSgNtrAZ5aYelqlW9_DZRbTBovdKXUwwOPsOnKTsX4rIVB-n8CQSfEAnd6q-lOEDlWT0dPOm74GhFqvQ_EIcOQyw6CGJIEOFvc8HsQLdxy8tg7klz1PgwSKtZ00WpBlHBm8H-eMi33jVDWEsaw37dZEb194jwh-8O8JqzTILR_fL84WcHqMBM39OWUlYOhWfNFvAUb1o9ZBwjyGN_SBvjAj-WqflreteswO7xgd0faA9Hju1zS1_uRNcbsgwRTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a7263425c.mp4?token=o7ojyut6bm4Ur0GDCnc9bcpgskqmLhta3Eym10ybzkUj6SVSGK7ToBgOB7KF7tGE-PAn6yMBEGfv5EWcKIuwV7sZSgNtrAZ5aYelqlW9_DZRbTBovdKXUwwOPsOnKTsX4rIVB-n8CQSfEAnd6q-lOEDlWT0dPOm74GhFqvQ_EIcOQyw6CGJIEOFvc8HsQLdxy8tg7klz1PgwSKtZ00WpBlHBm8H-eMi33jVDWEsaw37dZEb194jwh-8O8JqzTILR_fL84WcHqMBM39OWUlYOhWfNFvAUb1o9ZBwjyGN_SBvjAj-WqflreteswO7xgd0faA9Hju1zS1_uRNcbsgwRTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🟣
گل‌تماشایی لیونل‌مسی از روی ضربه کاشته در بازی بامداد امروز اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106985" target="_blank">📅 10:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106984">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a81f86f53.mp4?token=ClK-W-Br7Epn5d9xacxnlZY1kvii9FQwWjzp06L-r2LYHboxG2x9W5shdS0-BolLgIdfP70uGm2bhlc6fc6Ah0DyFu2A-8naTDxabznFKoaGrZeC50hw7OC-UekTn4xCOOZHTgOWF1XHLoDj4VjA1g37F_REIR0rrhbdqMUeoGLVNT_2BX43QK3b42fasYToS-IHPR38zg7z2X60jcP6aoCJSaGwyjNnscj5E-ZInOS8Crd0q4FyqIadRFUh7O5jEDfjrPne_F8PTWu-59vdJfobYCZFbEQhVes70TCKGeN8UK2b31qauKgXwqmRmDIkF8cLI5iJ-wLsK3CfatJtYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a81f86f53.mp4?token=ClK-W-Br7Epn5d9xacxnlZY1kvii9FQwWjzp06L-r2LYHboxG2x9W5shdS0-BolLgIdfP70uGm2bhlc6fc6Ah0DyFu2A-8naTDxabznFKoaGrZeC50hw7OC-UekTn4xCOOZHTgOWF1XHLoDj4VjA1g37F_REIR0rrhbdqMUeoGLVNT_2BX43QK3b42fasYToS-IHPR38zg7z2X60jcP6aoCJSaGwyjNnscj5E-ZInOS8Crd0q4FyqIadRFUh7O5jEDfjrPne_F8PTWu-59vdJfobYCZFbEQhVes70TCKGeN8UK2b31qauKgXwqmRmDIkF8cLI5iJ-wLsK3CfatJtYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لوئیس گارسیا پلازا، سرمربی سویا، پس از شکست ۳–۱ مقابل بارسلونا:⁣
اونا خیلی، خیلی، خیلی، خیلی خوبن. همین که تونستیم باهاشون رقابت کنیم، کار بزرگی کردیم؛ چون بقیه تیما رو جارو کرده بودن.⁣
توی فوتبال یه‌سری اتفاقات هست که نمی‌تونم درکشون کنم؛ اینکه رافینیا جزو نامزدهای توپ طلا نیست هم یکی از همون اتفاقاته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106984" target="_blank">📅 09:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106983">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5061d27e31.mp4?token=E9yxrpTaZdtCu2aVkHMCI-X5CSyWjdJ4KrayZd5OktDYrvpA-jFFkliaMwMHviaYsFY1NhajmWEVkSIDPxPyGgJjhBlmaWBsBQ4drF82T06wjlH9-iHoB1RuNzyr0rHo6C9tc1R5PslvFTAGXjm8YfXtHq7V6x3Xmw4H6XkgnQW6d_cqydlLE2sRn6s2MvtDWOb71VHceLkLq1b1WWBy1kKwNTWcQF-dAhJMhL7Ko3R3ovgQiVsxCJsPo8740aNYJskzDNwlQKTql3Jqf51OlQnb58pP_O2o6MDkwTHhkOUY8gxa0b_bpkmGd_xuSDg_pZPltUqwSWHnWjEbT2iIgDW3Af5NNtp2GQXVi5PzuANbECNZbsCtC3r9M_aPdb0I5lBozOLlqBy3hn344Ns9a2S-p01Y8R6fFiFEKVEuh9Qg3BhedLlLzc0md52zvFdyhCImjzBuOCRsozYdOZW4SkKATvF5-zjIXGZm8MqPdbEA0knBIbCmmxbKlrEHbCZVpqoJHnhbvcxRTRzn-DRetla9Ey3OQtoo59bew_qZnOgrAcCuVItHJHnX_KMUJq2LF2UGaVNw_bj34Bnu_C5Ig0X7aT2XFk9IlfLfAZ9IJkRQJx_sNFuc8EoZdvLbN6K1cBiasqW_4_emZCUoBhmiiOidhBeg0N-f8OE1e5vRYcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5061d27e31.mp4?token=E9yxrpTaZdtCu2aVkHMCI-X5CSyWjdJ4KrayZd5OktDYrvpA-jFFkliaMwMHviaYsFY1NhajmWEVkSIDPxPyGgJjhBlmaWBsBQ4drF82T06wjlH9-iHoB1RuNzyr0rHo6C9tc1R5PslvFTAGXjm8YfXtHq7V6x3Xmw4H6XkgnQW6d_cqydlLE2sRn6s2MvtDWOb71VHceLkLq1b1WWBy1kKwNTWcQF-dAhJMhL7Ko3R3ovgQiVsxCJsPo8740aNYJskzDNwlQKTql3Jqf51OlQnb58pP_O2o6MDkwTHhkOUY8gxa0b_bpkmGd_xuSDg_pZPltUqwSWHnWjEbT2iIgDW3Af5NNtp2GQXVi5PzuANbECNZbsCtC3r9M_aPdb0I5lBozOLlqBy3hn344Ns9a2S-p01Y8R6fFiFEKVEuh9Qg3BhedLlLzc0md52zvFdyhCImjzBuOCRsozYdOZW4SkKATvF5-zjIXGZm8MqPdbEA0knBIbCmmxbKlrEHbCZVpqoJHnhbvcxRTRzn-DRetla9Ey3OQtoo59bew_qZnOgrAcCuVItHJHnX_KMUJq2LF2UGaVNw_bj34Bnu_C5Ig0X7aT2XFk9IlfLfAZ9IJkRQJx_sNFuc8EoZdvLbN6K1cBiasqW_4_emZCUoBhmiiOidhBeg0N-f8OE1e5vRYcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
✔️
سوپرگل فوق‌العاده در لیگ‌کشور مکزیک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106983" target="_blank">📅 09:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106982">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9b6fbcb00.mp4?token=jXQ_OrQlYtGGJAkoB9STqYdY7eOQUqAwTrABV3KbJ8aVWJOrP_Hu6OzDhWJccwrNr1YPO3xyNiDY98Mn08BWP-jdzkVglILiUT5gdn3G_C2jxiU_dNSlh1YRlhZq-F_g8Nf6tvB6PiUxSo4gNDGNM9oFWwPGzlgo3f5zfovt0cmjVqb-p1ryBUIC5VjDYPgG64fBJhU4xp_G6veanZ2-g0ZEvZHk5SY7LVj4nn6qhO5cfHYsylPJuluCJmzfA9oqs6ZJoVWZEt_rahc4TykJvOXEhloDb2sY9T_No9N42VPGFvBxWOtl0Pa5aiffFq74MnlqrZcIDHfXZxvXc9_RKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9b6fbcb00.mp4?token=jXQ_OrQlYtGGJAkoB9STqYdY7eOQUqAwTrABV3KbJ8aVWJOrP_Hu6OzDhWJccwrNr1YPO3xyNiDY98Mn08BWP-jdzkVglILiUT5gdn3G_C2jxiU_dNSlh1YRlhZq-F_g8Nf6tvB6PiUxSo4gNDGNM9oFWwPGzlgo3f5zfovt0cmjVqb-p1ryBUIC5VjDYPgG64fBJhU4xp_G6veanZ2-g0ZEvZHk5SY7LVj4nn6qhO5cfHYsylPJuluCJmzfA9oqs6ZJoVWZEt_rahc4TykJvOXEhloDb2sY9T_No9N42VPGFvBxWOtl0Pa5aiffFq74MnlqrZcIDHfXZxvXc9_RKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فاصله بارسا و رئال به شش امتیاز رسید.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106982" target="_blank">📅 08:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106981">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106981" target="_blank">📅 01:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106980">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/Futball180TV/106980" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106979">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4uMo4tb-2L-ALE9eU0EylZ2xDkvKWt6vZ5LH7cj22weoOsdtwZW9QfA35Qxah9ivOmHdBsCw0DQtwuUgWsSO6UZs7vSvMW6zdgQmycViF7AJhVi_c393cXQ9BfeSo6yDyZ9PWfnlreZs67agTVcSrXNeufGa-TRK2JbCGAohx6JACpyRQW-GsopfCjCNAp8SshnheDALn1Enmnap2tdiYp5KjSFdZ-AptXdvjLpXzwnEmBG3Z3UEoYWQ_G3bSw7dnFbk2XbdsGXBqCqVmQOuivGl856bySnVZU5WbS-ItgJQ3uMqLajhZ9_uJYqhNB-pL6qC-Q47UeFZpPQ_Kqs5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
سیمئونه درباره بارسلونا:
🔻
انگار اونا دارن یه ورزش دیگه‌ای رو بازی می‌کنن، نه همونی که ما بازی می‌کنیم. مهاجم شماره ۹ نداشتن، ولی یهو رافینیا از راه رسید و ۱۲ گل زد. یامال هم اگه اشتباه نکنم ۷ گل زده.
🔻
توی زمین خودت بهت فشار میارن، زمان رو ازت می‌گیرن و از ریسک کردن و گل خوردن هم نمی‌ترسن. حتی انگار گل خوردن باعث میشه بهتر بازی کنن. اونا الان بهترین تیم هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106979" target="_blank">📅 00:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106978">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIgtIRJXDCx6qbq553ToDfhCwdIQmI3amIvZuicm3yJNekfytM7yiFwyMjxC-pODayaJOU0koL_buv1_SXLxeLLqGVGTfFxTtKH_2LKlGrqjEXtzCvvdWAilmhDNmUKCT8rF14LTcpA0lxeDfAfhTNeVPXVXv83p30LfaVpoMXocimGOQn7QB82n0kPQ8xfMZbR3b_gSkKCEaciPuwcSBWGuDri9WHRzFKxXT5oSnrbsMPEp4puUlSq32_77BI8H74VI-1IvL2BcWoCbH_7TZxjFOk_gLBQe0EKvuCDnJTIIarfakqbUU9Ucin5mgCTY0rKTH_GOKbrHUieepUQkeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⭕️
شبیری‌زنجانی از مراجع تقلید شیعیان دقایقی پیش در بستر بیماری درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106978" target="_blank">📅 00:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106977">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGaAxhkUyzvaoyb9M42flK71rGtLrZPFuAQlgj5oB6OosnM300-qQDL0Eq8lNwTzveiZfvGNuMPAgCy6AKZb2HHcSnnihWa2hqjDPlBD3PKFsDi_OcQtsYnqOFTVwBUDouDFThRv37bW66X0EBLvrcwvXaJwW1kzVU9kyP-X81LzS0hW9dLH0c2MH4Vlz26wQQAj98ab8K5udmMSQeHWMdgKDObctNlwRq3TzaPJI3cAVvf-bAnPbP8PEMDZlLbxt9LPCmK5qFJJa9vd4KBZlGwzzaYvgfJSXxUHJ6c8yava4Mf9agHoJfp9IEa-qbU7EWSE5ojBf3zRPd7FeJrYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
خوزه مورینیو: به کمیته داوران تبریک می‌گویم. آن‌ها باید از این نتیجه بسیار راضی باشند. همه‌چیز بسیار عجیب بود. بازی باید ۱۱ در برابر ۹ دنبال می‌شد؛ چرا که اتلتیکو از دریافت دو کارت قرمزِ مسلم قسر در رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106977" target="_blank">📅 00:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106976">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OugSCzrof76BH6yOMrGLPSrbBwber0U2R01wxs-Eb7AKF9CukIy8zNlKy7giDmpY6DXqCXUCJXvte1-Q0NSqdIjvsbvdUNwLuZQ2I07PTWMg_ciqA7hbxaE_2q8quDiFcAFJSByH2N2R2Dt-8Xd-nlAdhgra5dicmKQut1Bpk0xPey6k9o12cgebQXxELe02X77Kuvr0t2lJBt9AKjTgWgVBuipSR74hsJrclBd-KXLsKuq-R1DP3OL2NJ8YtRTW0gKznTNN4vleyB64wuUVbQy5B6KcGhEQW-52q3LSdyT0Cufy6nJ7kP0froKhekyNDOcg16-XHK8u8T6cxTyVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بارسلونا در فصل ۲۰۲۶/۲۷ تا اینجا :
⚽️
۸ بازی: ۸ برد، ۰ مساوی، ۰ باخت
⚽️
۳۶ گل زده
🥅
۸ گل خورده
🇧🇷
رافینیا: ۱۷ (
⚽️
۱۴ گل،
🅰️
۳ پاس گل)
🇪🇸
لامین: ۱۴ (
⚽️
۸ گل،
🅰️
۶ پاس گل)
🇪🇸
فرمین: ۶ (
⚽️
۴ گل،
🅰️
۲ پاس گل)
🇩🇪
آدیمی: ۵ (
⚽️
۳ گل،
🅰️
۲ پاس گل)
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گوردون: ۴ (
⚽️
۰ گل،
🅰️
۴ پاس گل)
🇪🇸
پدری: ۳ (
⚽️
۱ گل،
🅰️
۲ پاس گل)
🇪🇸
اسپارت: ۳ (
⚽️
۱ گل،
🅰️
۲ پاس گل)
🇪🇸
اولمو: ۳ (
⚽️
۰ گل،
🅰️
۳ پاس گل)
🇧🇷
ژسوس: ۲ (
⚽️
۲ گل،
🅰️
۰ پاس گل)
🇵🇹
کانسلو: ۲ (
⚽️
۱ گل،
🅰️
۱ پاس گل)
🇪🇸
برنال: ۲ (
⚽️
۰ گل،
🅰️
۲ پاس گل)
🇩🇰
کریستنسن: ۱ (
⚽️
۰ گل،
🅰️
۱ پاس گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106976" target="_blank">📅 00:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106975">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773fad15d7.mp4?token=lb09KJVnFfusSJXKotce0Z4ikhuXgsbn86kAqdFz8s0yzBEUIPZMi75qkbZdXIy6SiFECJZGumc16-tqXy175urLb_Fe3SgSNVJVAXYlNFfO--IOr8c6M31WsD1YlEThqkjKcu1P1c75HPFmBmC-9adl8slIKZApvIUtHIzcimdSO_vqoI2dwkk-Irn4fTjKwK91r0DboK8A1moDb2tgBysvDHZYMu_WpzEP99XnOe9dhGovzx-YS7UR0tUCwhrnD2SpR694cMRF6fJ7ovq0KvyCkwTSi6W1Xr7W70gYUN9zh7DmIsgLKuw6R6dVBqQ-Hd4MTJSxeZnLgH64XyrpQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773fad15d7.mp4?token=lb09KJVnFfusSJXKotce0Z4ikhuXgsbn86kAqdFz8s0yzBEUIPZMi75qkbZdXIy6SiFECJZGumc16-tqXy175urLb_Fe3SgSNVJVAXYlNFfO--IOr8c6M31WsD1YlEThqkjKcu1P1c75HPFmBmC-9adl8slIKZApvIUtHIzcimdSO_vqoI2dwkk-Irn4fTjKwK91r0DboK8A1moDb2tgBysvDHZYMu_WpzEP99XnOe9dhGovzx-YS7UR0tUCwhrnD2SpR694cMRF6fJ7ovq0KvyCkwTSi6W1Xr7W70gYUN9zh7DmIsgLKuw6R6dVBqQ-Hd4MTJSxeZnLgH64XyrpQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم پاری‌سن‌ژرمن به مارسی توسط مارکینیوش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106975" target="_blank">📅 23:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106974">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f22d5f48d9.mp4?token=iqIu7XO2I7kkmj9iIL0GHSRpvQsVkhGf5WYjAmQyAx8NJ8rpFLPqSojLSNj2gIkoyvGyzqBifF9MzaEeP4sqBV-6aopyiKxPInrWGaTXswtFYAEZGjYNZeUUzWa_UlZGeJ7NDFYm3ymFiAqrNwVouvIwmW3cytI2E0-kOWTEVS7bXlDcPaOOA3GfdqzAqgk-rp_Pid4byrk9daS6e6Lf8qbGZ55shKpQuU_fRhNrQ8VRdMCwvVqWY9vKIcrkkiOXI9-qW6HuLbymR5V_NEq89sF6N27KiAFZqXI4JO70EQDmAU3z2s_1PqkwN1e1vD5Y9kwM6uCkSGpAU2FvsRw2AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f22d5f48d9.mp4?token=iqIu7XO2I7kkmj9iIL0GHSRpvQsVkhGf5WYjAmQyAx8NJ8rpFLPqSojLSNj2gIkoyvGyzqBifF9MzaEeP4sqBV-6aopyiKxPInrWGaTXswtFYAEZGjYNZeUUzWa_UlZGeJ7NDFYm3ymFiAqrNwVouvIwmW3cytI2E0-kOWTEVS7bXlDcPaOOA3GfdqzAqgk-rp_Pid4byrk9daS6e6Lf8qbGZ55shKpQuU_fRhNrQ8VRdMCwvVqWY9vKIcrkkiOXI9-qW6HuLbymR5V_NEq89sF6N27KiAFZqXI4JO70EQDmAU3z2s_1PqkwN1e1vD5Y9kwM6uCkSGpAU2FvsRw2AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی مارسی به پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106974" target="_blank">📅 23:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106973">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed04c10225.mp4?token=FDpRpyylpF4z3ykz9BHLw221OzuArYdOdIR_NMv38i-u9WdpcfxEG0Igyph1OzewGL-X95nEzDyosIAYcPzEFBFP1CW-awzgZHhQe0-tB0jR7vDk0Yny1c6Is1ont-FpIobsfeLxyNQuMcCWeaR9WrKtCBPcD_YU_Gdz3VKL8GRAgNu0MVPRNNpUaF6Q04VbOTutMPrbSI9G5W8_oRqc1X19FtsbVpCE9nSdhWX6aGQPCPXOpdf8FAA1OFc4it3-E6CBoRcpb9LPJgyjyB8219wnVOTqeuNOyIzq6jMnTtAaL1TnHDXhh_YFUEFZskYPKx--fZzRhGYDQzCMzfacahQJoaf4-x0VK_7I8q8g_7Jj-itHdwaRTqRwjqbldeOTwT05U9rCAtfBivXZL9B52UfnYVUUGdTWh_HQU_dK6FcXpJktiQI3u0WrHOeaNDVUBFu3CAMhJoXCZg12SYXSuvtB0crP7tzCr5yb40MQ3OxvFZ6eqmBCOASoOnluEiYeKbx0AAkBNR4z14eMamvK1dpOUf2c6Wc6BJIkE5QP776jmieBv4GLXnNfUZ_MNtvhefsDZNMr13oKzAhwXlfEU9C73bSNbAuU7EYXNB0PorLJAQ_GqlVeZU5atuirIg_mlk9s2JVF0DqwDebrhyDvmXujEYEcUpoaGzuHdgF0iQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed04c10225.mp4?token=FDpRpyylpF4z3ykz9BHLw221OzuArYdOdIR_NMv38i-u9WdpcfxEG0Igyph1OzewGL-X95nEzDyosIAYcPzEFBFP1CW-awzgZHhQe0-tB0jR7vDk0Yny1c6Is1ont-FpIobsfeLxyNQuMcCWeaR9WrKtCBPcD_YU_Gdz3VKL8GRAgNu0MVPRNNpUaF6Q04VbOTutMPrbSI9G5W8_oRqc1X19FtsbVpCE9nSdhWX6aGQPCPXOpdf8FAA1OFc4it3-E6CBoRcpb9LPJgyjyB8219wnVOTqeuNOyIzq6jMnTtAaL1TnHDXhh_YFUEFZskYPKx--fZzRhGYDQzCMzfacahQJoaf4-x0VK_7I8q8g_7Jj-itHdwaRTqRwjqbldeOTwT05U9rCAtfBivXZL9B52UfnYVUUGdTWh_HQU_dK6FcXpJktiQI3u0WrHOeaNDVUBFu3CAMhJoXCZg12SYXSuvtB0crP7tzCr5yb40MQ3OxvFZ6eqmBCOASoOnluEiYeKbx0AAkBNR4z14eMamvK1dpOUf2c6Wc6BJIkE5QP776jmieBv4GLXnNfUZ_MNtvhefsDZNMr13oKzAhwXlfEU9C73bSNbAuU7EYXNB0PorLJAQ_GqlVeZU5atuirIg_mlk9s2JVF0DqwDebrhyDvmXujEYEcUpoaGzuHdgF0iQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول پاری‌سن‌ژرمن به مارسی توسط فران تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106973" target="_blank">📅 23:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106972">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2832d49487.mp4?token=DedIFiqIfsupke_ESTfy9C3SzxL1krd_GdEZ970Yh80tJ9Vm5uzWYG5NQ4dJZo2E7TB8tr6Isvq9DZbptc_ieX10ATGqK6FlxiN3uulxjObrIMDUmg4teTgZT_slJNzdweKhZAFUhqpn7ALtapZNTHQPA0Zi20ifGDF8OJT0_5HO3rzjWqMbALdPcZI_s1l6aq6Mt_RhI-fcagTFdfYv4cgM8w6iyQ1hxXlCF6rxnLqVj1WHdScLji8QxNi3cGrfydQLeZdiLtxN3ra6ZiTTK2nPTH3PzA9A0YwZzgkK3vxmwrCupBTJ8oPklKHCyuWpDOuGXTDa5ml5IBX7weI-6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2832d49487.mp4?token=DedIFiqIfsupke_ESTfy9C3SzxL1krd_GdEZ970Yh80tJ9Vm5uzWYG5NQ4dJZo2E7TB8tr6Isvq9DZbptc_ieX10ATGqK6FlxiN3uulxjObrIMDUmg4teTgZT_slJNzdweKhZAFUhqpn7ALtapZNTHQPA0Zi20ifGDF8OJT0_5HO3rzjWqMbALdPcZI_s1l6aq6Mt_RhI-fcagTFdfYv4cgM8w6iyQ1hxXlCF6rxnLqVj1WHdScLji8QxNi3cGrfydQLeZdiLtxN3ra6ZiTTK2nPTH3PzA9A0YwZzgkK3vxmwrCupBTJ8oPklKHCyuWpDOuGXTDa5ml5IBX7weI-6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم لخ پوزنان به رادومیاک توسط اللهیار صیادمنش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106972" target="_blank">📅 23:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106971">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwgMFPUZHL7O8j2-TT0lV-o6VohhHOW0P617mEGNtCyS9QrvEcjCO_i0FFucKems7i8ZWJJvCv6BKr2nRk2PZXHRBHPmmK6FnwkPMJcNgQ4ZMwbGCUOSDKt40uM52X4BmPtK-Y8yPaJ7Qsw078hHY5_4FVJdE935jU7oOJYTSVLB6pff_B-f7H3lBOHLH0spVoujEtlQdlyxjRbuASMu95v2DKL-Dvhy4yTu4JP5memOLMLSYyFtOvm_5rK9kw1pUa7J7sK4LzF67f5E2t01g0cpmlxrfx2unqYcSsTFXd1UvJknsggXDgHhfY-Dk01bOVmSIuP_qyA6E8ohbsDP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ترکیب پاری‌سن‌ژرمن مقابل مارسی؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106971" target="_blank">📅 21:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106970">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=InCcFscUl-Gnr0uK58jvxPuurowsZ7Wait5Uh_fueqVkH1gtNAWl_psDZ9qaEmiZSy5-v9Lcf6dwbQVaetXrLz9CqhvG8ciLO-3RpU427T8vZ2sIqmLZezyP_8MoRVCJNDJKAqJ-KZP5iyDxDLoDB4Z_jcz3JlBqvCgNQXz9EuzuPyEiuVQ6mV5me6nldn1XzPmXCf08PKHFA9Ih43lP_-5byUwWCJpnsMzFaB5I9tBvai94ItV7qAi-8gGoeQOp78eM-KICNsmeddP8Plzw1ihOnUqih7Sc7I2jz5c3nWrPRmEyL5STqqQV3WMPJkENCtH3pLLTxc3F-7-N9Aeu1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=InCcFscUl-Gnr0uK58jvxPuurowsZ7Wait5Uh_fueqVkH1gtNAWl_psDZ9qaEmiZSy5-v9Lcf6dwbQVaetXrLz9CqhvG8ciLO-3RpU427T8vZ2sIqmLZezyP_8MoRVCJNDJKAqJ-KZP5iyDxDLoDB4Z_jcz3JlBqvCgNQXz9EuzuPyEiuVQ6mV5me6nldn1XzPmXCf08PKHFA9Ih43lP_-5byUwWCJpnsMzFaB5I9tBvai94ItV7qAi-8gGoeQOp78eM-KICNsmeddP8Plzw1ihOnUqih7Sc7I2jz5c3nWrPRmEyL5STqqQV3WMPJkENCtH3pLLTxc3F-7-N9Aeu1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
توی آلمان یه دختر تریان (انسان‌های که فکر می‌کنن حیوانن) به یه خانم حمله می‌کنه و گازش می‌گیره، به پلیس اطلاع داده شد، هر چقدر از دختر اسم و فامیل پرسیدن فقط پارس کرد، پلیس هم اون رو برد مرکز نگهداری از حیوانات
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106970" target="_blank">📅 21:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106969">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVN7ZFOY60XYLppjqR8jBSqD45bIiwxoicYSPP7P7nf-G6p8d9YmMZ7dUfT9RxzqyldgBQcGDMpThxVrh_HhnSENO82vl5CpFDQPDivY-5PmpO8iW7DzE4q1L19dfPXk0mLO-zPHF889qLLdUPFnrLevrikvPNdsearaoUqhFUpMubt-nOAzfpTWZ0gajqbZa-7VbGXFeNvxBqpZKx1JAnPtSyNp2EeDU_4K8L9UKLfYSzkS8yAnniXwj1rQLFMCySQR308OG1afuyTkcTieU3uZ14U90dQm9KQXlyA7DvvGv7OPhgeecictrgaqUxlN5YFw08Rif0w-uqs7V35-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مورینیو در ۱۶ فوریه ۲۰۲۶ که مربی بنفیکا بود:
تو یادداشت داور نوشته شده بود که شوامنی، کارراس و هویسن نباید کارت زرد بگیرن، چون بازی برگشت رو از دست می‌دادن! من خودم سرمربی رئال مادرید بودم، واسه همین خوب می‌دونم اونجا اوضاع چطوری پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106969" target="_blank">📅 21:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106968">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh32ypLj425u0cgrpaMUtV5og-XS4Gd1u0xe2mw_sM984d1xICHCtyLTh85WtLbNB4nRuBYkowvHXa7vDgVRJddy0UNh_nE1wm6PwvYHfGjpqy6z1JBpHV2xQdWqJThPwOgcd5hviEQniT70xWcN5HxUdVDC9pRvLZ8BAemRzLwGvYs8DGNAvGDvFAKPtVTvkYT5FwCQqCVsxFwoAsQ80g_d-wa1vR7W350rZaKRo6le7BBPk71x1YcDajJ11BjBJJK_wnYS2BZudz5AVcB8YkoEKqWcoc3Ll95VpGcxSZ2sD3ldKftl7jrX3xwra3K7UDmCFbr4rn_Lok5oT4lC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نتایج درخشان منچستریونایتد در پریمیرلیگ؛ عجب کسشری شدن بعد فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106968" target="_blank">📅 20:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106967">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=OWSgxmKYVCguHvfApVI9QfPXy7K0ZdCwfa9V6UY-IrKou2OdnliF8lELe18GGU5iVhBGKYcOMZPipJsO01S_C43dpvEeT1CSiQOE91m4fA1UtyeN89SkeBsStzZgZe97L6lwX0zsInRsDTiFAnWjIe9viA8SsA8fglOg1h7vnZC1qAIZutlaLjA_eQ7OT2x4H2qInvPPVWAKB9VrQZAZWvE4U4sgi401tL1A_UflLl_GE304UY8RMaNxFfkE_PiSbueljB4_GxMPHrcyBiMIQ2GpSuJZUAiX8D8TFJUjwQ56vrPFvU-9wVR3ryKWjqMdqw7LedYXWW1lD4mruaGtww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=OWSgxmKYVCguHvfApVI9QfPXy7K0ZdCwfa9V6UY-IrKou2OdnliF8lELe18GGU5iVhBGKYcOMZPipJsO01S_C43dpvEeT1CSiQOE91m4fA1UtyeN89SkeBsStzZgZe97L6lwX0zsInRsDTiFAnWjIe9viA8SsA8fglOg1h7vnZC1qAIZutlaLjA_eQ7OT2x4H2qInvPPVWAKB9VrQZAZWvE4U4sgi401tL1A_UflLl_GE304UY8RMaNxFfkE_PiSbueljB4_GxMPHrcyBiMIQ2GpSuJZUAiX8D8TFJUjwQ56vrPFvU-9wVR3ryKWjqMdqw7LedYXWW1lD4mruaGtww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول منچستریونایتد به فولام توسط متئوس کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106967" target="_blank">📅 20:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106966">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kghxmY5iStH4jZjkWZWl8pZiNmtHEjgcqreSOxbdy3jT4vMKnA3SENDBWmh1YZAgIBzGSkWR2tbH7zS8W5rFXHEpYILd6PGqa4vU7uuURHjXpcTVzrxxGeteK59L0JPf4LqfKzDKjtp9wIcUwuYpVa-OygyKfqFQ1xotDa8kOSTM3qLSQITwhfB7EPsztxKOvpH_HA_su_lzwG6RE4WJeEFZ6GMDTqOeCW54J6yT3WTfgVR-1N9pVctd_f7MOvlnHZ31FKMCpYhTE_MVwiwScLRbEt061E3JPDwk5v2yjnCrf6siALw2hkwBZuEwu8i1qgjjb18ohiDYJovG4Rpmfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇸
رئال مادرید Tv:
🔹
وقتی پای رئال مادرید وسط میاد، برخوردها کاملاً متفاوته.
🔹
لالیگا و فدراسیون فوتبال اسپانیا اجازه نمی‌دن رئال مادرید رقابت کنه... اون‌ها یه نقشه و برنامه از قبل طراحی‌شده دارن.
🔹
دیدن همه این جریان‌ها حالت تهوع به آدم میده... اصلاً براتون مهم نیست که کثافت و مزخرفات تمام لالیگای خاویر تباس رو برداشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106966" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106965">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34da8be998.mp4?token=dj3tIGBvB7kbjatfIbYEgbu6euQDgvMKrbfmbO1BMckjN7lzY9HWaA0ICNHCaPjZlzZNI4hefsWRrPqdTfD15ttjCQCZGN1WF5sHknuwY573xnMR4dIzGmWFPzRljB3pH8bJBotyGmP6G_n887c9C54xX1Z-EFqOtr2NJLInfXe63zeTGPPIIgOgZKJvRlPXCQ2CSoDyVZInb8ZVLHkRuT7p8boYVFMfCsbooBeWGElINzFK-ivw0MHUF9MA6T8i6fP0fH662L1bsrWjkkkrco2967X0nSqOtLxUIJwZ4rkx1u35Lzel028QDXUzulhZQy_vgDmL8cHEZP8azICptQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34da8be998.mp4?token=dj3tIGBvB7kbjatfIbYEgbu6euQDgvMKrbfmbO1BMckjN7lzY9HWaA0ICNHCaPjZlzZNI4hefsWRrPqdTfD15ttjCQCZGN1WF5sHknuwY573xnMR4dIzGmWFPzRljB3pH8bJBotyGmP6G_n887c9C54xX1Z-EFqOtr2NJLInfXe63zeTGPPIIgOgZKJvRlPXCQ2CSoDyVZInb8ZVLHkRuT7p8boYVFMfCsbooBeWGElINzFK-ivw0MHUF9MA6T8i6fP0fH662L1bsrWjkkkrco2967X0nSqOtLxUIJwZ4rkx1u35Lzel028QDXUzulhZQy_vgDmL8cHEZP8azICptQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
حالا که بحث جنگ دوباره داغ شده؛
اگه تو آسمون یه جنگنده دیدید، سعی نکنید بهش شلیک کنید یا سمتش سنگ پرت کنید، فقط این فن استاد رو بزنید تا خود به خود به آشیانه‌ش برگرده :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106965" target="_blank">📅 20:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106964">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=XCUXIn-GfadiEghx7XBIK_r8WByJN1TcIxB4fS0K-9PPeH9BWopPU3jUnQMiPfYJWond6HTeqrSYczJDvC3Rrji8zoj3jrRECCVl6-pK-RwAHfqNMX7tAeES0y6QJGqqtmUrXMLVCVHgOZ5a5ajyyc5wPgPPr5epm6wAKVY4TatxtkqLqKjNFMIuwt92lsTgQ4NswP6bn7oIvuxi-aqqPrTS8EKlP_vhhUt0PEyT7JK7U5659OlEHKy0RhUNWUXMz1AGn5NGT2RcktGb9YiKECLPmkgw7xutrt7yuBmrqi4QcuPXz90VTaFzUP94m0pF85qtxmz43wCNjI7qPTJdnoKeKQwNG-wP96oYSHjdeLIdpiMNgqsTimFdlcsKcrd2EyYjtXB9klQ59wFTGu6vNdKUulXcG_3qr4nCj6UvJoaoFws4_ABmaBivM5tf3pvoRw28nfw8EKBuz8SzI4UjlVIHcU-HvQE9yWVeeqzxzfqv4gcqgMW_uZdsK5KOPHRvTtMrvCGa39KK0opXDMyX7mPheM7uTy-d7DObkW4wlNVrHE_9bnTANC996Mh1wP7UMRB9pB0L9_oknlmeVhewqGgVyRmY7jwNOBXlWs5K9LfOLJMgVmAfLQ95fDUMzW9FCugxDVLAQYXCL8HQB1DYe02OK3i686Fu9mHKNc-PKF0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=XCUXIn-GfadiEghx7XBIK_r8WByJN1TcIxB4fS0K-9PPeH9BWopPU3jUnQMiPfYJWond6HTeqrSYczJDvC3Rrji8zoj3jrRECCVl6-pK-RwAHfqNMX7tAeES0y6QJGqqtmUrXMLVCVHgOZ5a5ajyyc5wPgPPr5epm6wAKVY4TatxtkqLqKjNFMIuwt92lsTgQ4NswP6bn7oIvuxi-aqqPrTS8EKlP_vhhUt0PEyT7JK7U5659OlEHKy0RhUNWUXMz1AGn5NGT2RcktGb9YiKECLPmkgw7xutrt7yuBmrqi4QcuPXz90VTaFzUP94m0pF85qtxmz43wCNjI7qPTJdnoKeKQwNG-wP96oYSHjdeLIdpiMNgqsTimFdlcsKcrd2EyYjtXB9klQ59wFTGu6vNdKUulXcG_3qr4nCj6UvJoaoFws4_ABmaBivM5tf3pvoRw28nfw8EKBuz8SzI4UjlVIHcU-HvQE9yWVeeqzxzfqv4gcqgMW_uZdsK5KOPHRvTtMrvCGa39KK0opXDMyX7mPheM7uTy-d7DObkW4wlNVrHE_9bnTANC996Mh1wP7UMRB9pB0L9_oknlmeVhewqGgVyRmY7jwNOBXlWs5K9LfOLJMgVmAfLQ95fDUMzW9FCugxDVLAQYXCL8HQB1DYe02OK3i686Fu9mHKNc-PKF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول فولام به منچستریونایتد با گل‌بخودی لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106964" target="_blank">📅 20:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106963">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyjIsSWkrT8MEemGwQtXUPgiMsDvlJCbpg8LJ5-BAr-6PvAp9hhgLOUoSQDmwS72x-2WjFibeT5TnXWLYzWpyIp1x8_umqc9FW58Ay3owzbIb5CfvV-GOvCGkwLAyMWogNJdnw7qajNArEbHDmnryJ3Ew_-I-hhk5eEuU7U6CT4YAyK9P-Z-qJzmqdq5dQhyWE3MdRoJ31ZmuEsKFtV8twgxh7BeMxtCxqqcKU6nYhZBxNRv8thxNAlpSKyguXIvBAk6y_ZwriUQnUGTvqjG5hKAQbRcZgFhkGZ9zrPgcGSuTLvfjbVsMiGFyQlR6P-obSeUNsWWg8jN8OF811w_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
خوزه مورینیو
: به کمیته داوران تبریک می‌گویم. آن‌ها باید از این نتیجه بسیار راضی باشند. همه‌چیز بسیار عجیب بود. بازی باید ۱۱ در برابر ۹ دنبال می‌شد؛ چرا که اتلتیکو از دریافت دو کارت قرمزِ مسلم قسر در رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106963" target="_blank">📅 20:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106962">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeiA08BApLFfCxvd1FVQHJy-JAGfG_gg_dX4us2P5Qizl7BYPD-ppquwuXhFKio--_hYj3yYWCXhafFfCD1CD1GPVVBX1q8480-UaaLO_AW0dgRkwyGUk3vRcyG8sZSP4avJeJrHOxgfkT3cYKqDy5XfSsgh4lDa742HVcpriBBXHklZeu0JylJGRprgA-3oLXFwc5ynWmqyG5fH3ChMuflVegKgBldob7kfx1U9TdZsucdnfUXDUm8Qh1EazfMuUjvIB7uBSjFzZJHLckdBaw-cOzGoMKmppM5fqpWt1BCGcK9e3dUuKY8wh-fV5DwJi7shAL-o4M6XF_7rC2dq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
کانال رسمی رئال مادرید:
اورتیز آریاس داور بازی، رفیقِ لامین یاماله…
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106962" target="_blank">📅 19:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106961">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwVCCdm6FEfo2CWgLHCOqt8J6WvqEa0sXtA6lLKRC7Fk1BmHVzDyObOTAsAekx0SgbKyr-3jNlvqvoMHa1QOzf2AdAEV11_mxBJrlBBco5aQ11HwZm3Y-aPd0x_HdiCEDchTctpLZUdKwbD0badq5shUK19RZD9EF_PyO7uoomJ0sxRq2ScanNEX-Xm9XDltH_KCo_nkmwJdFMtZT8S5A9IG_lYVZFncAEjvpdCehAfZ5Jey8Nq2Td1zdE8zxl3pV17JXdxOw4D8vXC2egzGXo_yrlAWQrCkfy9iRcXCKkeesdSD_TPxQgWlR3kvwzfRZTZa0HO_yTNjX5kXjCLTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106961" target="_blank">📅 19:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106960">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3b_VN5d_ii3YEkXqhCOtjtwdk4Yvu2A4H_HX1aPIgW1Rjj0W_-A0knz7gdkLGaTi928fEU42-MmyZXx_oM7dAVdv96qmzz0Psv2dVIqnuQXVRzIRci-MuMqyu0mfLAjMxwiR77OuUZV9xTNhKwSekX6ybZRhrnSvLdj8ePmvdxs_CvjRKng7ibg28vjDOtoPhZTum2N4WcgecwRQ3bb8Oc7EvtWBkOJlwsgGadC-ucIQA2DjFE5hpn-ZQGde81uc2ui8aBF6ZJQAXN6xtpoE8yXPMOXwPX6z0MrryETDi6elqTXT_TSDP2CidI1JXUto6QDFdp23pp4n6x0Fmi_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106960" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106959">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqWRLZTpiJilE28AJYo8TWYwWjY9_SeLKaiwUEX-p9wCkztAaxOl9Yjo9LtwQTVNdpbQjr6uv2OgrdT_DJGvfSlfIzIrEeLlR23yO-zJDtRTsA7vyWau1UyIJPyCt1lCQTJhaTkw8FdbvKbVs6fIenpgnMSLrm4pqx5CciGuBpKr2uirwfyzngzj0mV4rRPXKrZvvNeUX5a14eUwK2Bo0xoHI2zcdQ8dGMth9i_qHWt4WH69rZAj2LuwgHKz1NR_UF90T_58GNkNhgaB40FEjzwOONX3ML_dKb3YvOk1vY0WRUdvdaD1QC0VFjpSzGxd72VV-mNtBkBZ87yoyWxmPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106959" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106958">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">۶ دقیقه وقت اضافهههههه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106958" target="_blank">📅 19:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106957">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دقیقه ۸۹</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106957" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106956">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رودیگررررررر</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106956" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106955">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رئال یکی زددددد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106955" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106954">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106954" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106953">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یا حضرت عبااااااس چه توپی گرفت کورتوااااا</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106953" target="_blank">📅 19:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106952">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اتلتیکو دومییییییییی زددددد
🚨
🚨
🚨
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106952" target="_blank">📅 19:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106951">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106951" target="_blank">📅 19:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106950">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7be2074ac.mp4?token=tp4aT-J5rl9ag9MP8W9jGqenVlWrhxI-5nL5jA2yBslipXSTlOZQKy03_UR6BjhqOHzo4ny7myFgC42POEJ_qlaRoBIlEtKsJ-eiP8Hzcm9Z2NNfo_7CXWZQ4bTqdxuLtOuSMZXg17GetqGczkRDiYHSsoNbOUZqKrgqFqREFJ6bU_tUlzVhwBtqhzRA3Jv7I2Sbhh6gSkTgttZGuSsyZVnV9kmLv_GV7_c8p_OH8Qdkg1X6Sfz9k-dRTgRIkCW7JMMU8EgkVbVnODcwjoDKrguUnsZJ4SGCG_7v6tIEOIfTlYrQ3Yg1JtpUXiLW8fEpNmWsfI3pnlBjOlwApCJ73A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7be2074ac.mp4?token=tp4aT-J5rl9ag9MP8W9jGqenVlWrhxI-5nL5jA2yBslipXSTlOZQKy03_UR6BjhqOHzo4ny7myFgC42POEJ_qlaRoBIlEtKsJ-eiP8Hzcm9Z2NNfo_7CXWZQ4bTqdxuLtOuSMZXg17GetqGczkRDiYHSsoNbOUZqKrgqFqREFJ6bU_tUlzVhwBtqhzRA3Jv7I2Sbhh6gSkTgttZGuSsyZVnV9kmLv_GV7_c8p_OH8Qdkg1X6Sfz9k-dRTgRIkCW7JMMU8EgkVbVnODcwjoDKrguUnsZJ4SGCG_7v6tIEOIfTlYrQ3Yg1JtpUXiLW8fEpNmWsfI3pnlBjOlwApCJ73A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌اول اتلتیکومادرید توسط گریمالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106950" target="_blank">📅 19:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106949">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اتلتیکومادرید زدددددددددد
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106949" target="_blank">📅 19:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106948">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلگلگگلگلگلگلگگاگلگاگاگاگگاگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106948" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106947">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دین هویسن اخراججججججج شدددددد
🚨
🚨
🚨
🚨
🟥
🟥
🟥
🟥
🟥
🟥
🟥</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106947" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106946">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پنالتی برای اتلتیکومادرید
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106946" target="_blank">📅 18:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106945">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
کانال رئال‌مادرید: وقتی داور طرفدار بارسلونا باشد، چنین اشتباهات خنده داری کاملا عمدی بوده و پرونده نگریرا رو بیش از قبل بزرگنمایی می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106945" target="_blank">📅 18:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106944">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106944" target="_blank">📅 18:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106943">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ_gC00DATSIzjuue2UpsCGZcPGLVosRu3yZ2uKpIKsUO-7dzcL9t461CK-11ci_o8UoR46TaOhatuxclWvnihjLLFQKc6C-NeNbD1lttYPnPVUy6X9vZYeJP8hRaUtpNubZuDlIzC3WLCZlxpBmwqgP0-PMAisZqCQUOcPnHHvjpTtGqpWJ5CnT_aMHUaRhPJU4hkQ9HStONple_Sb49AuQO2VopiThiCVvpTqFbE9tiNubEUDHe-xEaMjDzWWgeYNkG8Bc66PnrSnIeudaADIS6i7bIb6QezLphcOVckoQto3pkmrV86uSTQwZ5qW_lbIpNKsLbJ7U65ZN5DEAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106943" target="_blank">📅 18:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106942">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JV71cQYXwXjXfbms3096YhIfW0lSzWRJrJGhbOGJmHw8y9G1lUOxIxGQSGae8vO5M4VeuXzq8szkmHbcZyRfaFxX6OlkkK2bptcyWlwrDueTaSktTzPABYeeMK9vyTML989HWIfDAMp7prVcwnaEnN4RTRsZF3AGb6Nmrxa8cDdQBv0FXhFmdCISipXzxkwOm1IbF3-dNosVfq_MJTvVh5yCsS7XHDctQdBxgvJ86qDnHb63oUnTA0V-ynrra0d3EMu-EhRE8ncr3luIDCC6f9eIiNUtlBNaws81FdvOCn5wiAwunRIxlOciaklGguoZ6Q9wa3zRlSZQ59CPzN9Rtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
با گلزنی به ساندرلند؛ ارلینگ هالند اکنون مقابل تمام تیم‌های پریمیرلیگ که تا به حال با آن‌ها رو به رو شده، گلزنی کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106942" target="_blank">📅 18:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106941">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106941" target="_blank">📅 18:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106940">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeVMRy80UifQinib6-YRLDYpLq2qAt4zLw-tKtqh7i2QR0AVUkTYRtHscIREERstpZkT-KrC06TWvefULSEZd3G6_kB47d273dgWtBMVYrKy2JxO8XhsVzG-E_dPgqI7HhMqL6jLHK3AvZynXNpvX8YDDf4PbJOY3RuMPDzI_1Dlov6LeqWfNGpfDfqaegApULcOaaS7qsDkleYlJKmustfyDacifJNm22qOF8VsmexlywY75SjTAc7FqJ8KC5JqEs0cJOtvzzvA_q35wRBVk3UQnm9o9SltfM523tosSNbMAk3rHZ7M0e25r9IzV7LEXip0_sWJVyNgZyKI8tMnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106940" target="_blank">📅 18:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106939">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اتلتیکومادرید دقایقی هست رئالو لوله کرده
😐</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106939" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106938">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbT8g5VGjy8-bMC2kVDp_j4nW-ao7MhUSZpbWpcnnnuBShBc9FAFRtcf8b4iNU7C86mNR23mQMeQOhoP4Qo9D_Hl6EOiA26SSdJ5YuhTGDV9VLPIXx_A0FJS11Aa6xDai41rXGmcXbtyFYUMDj9Yzos0soaxc0ZCJjCY18yDiYzfRXYj_iRNLjbsh83_jyCGVPMsE8rQmR5aLGv5u6sBgUwMBjyP1T6J5pnpEPNqXcm1DwnrXKU695Vls1OUvA5OXHJKF76cUfXncjmPt7saMv0il_PBtVXK2r8kTd5_EiBRdRwULKR10KvxwPj_BYHcMj-xk59hei47DWGDqpyu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
براساس معاینات اولیه، کریستنسن به مدت حداقل ۴ هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106938" target="_blank">📅 17:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106937">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787e254f6d.mp4?token=kqYAl9LEEIGpLzlQC41narFSDyrVr6l_vG7ql82ULr2mBM31B6Jjl5M6s95pikW85EvJQwnokwg4yHKrm3xmId3dOUoooQAHwZEaLi0djWV1efah4pXAzSWBpwbDURi_QKFf_OQY8xTGIEI0nvazfF_TCm-L-J5txDtS6XPkWjkOSAoOLLZy9Jkl3Xxxd0nj1wzuLYaeIdb89866Qel_DCAmqQhVGquM0VSZ75SWlh-L9rg-l7pHM9X35fXe7kLFi4ZJQkz89iI2i2aBdi8TagbsBIhFAnFTL_R6O1nAHw_ct9BxoxcxJLj7J-O-FFy7wy0VadRkLjEjNxRzA_maiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787e254f6d.mp4?token=kqYAl9LEEIGpLzlQC41narFSDyrVr6l_vG7ql82ULr2mBM31B6Jjl5M6s95pikW85EvJQwnokwg4yHKrm3xmId3dOUoooQAHwZEaLi0djWV1efah4pXAzSWBpwbDURi_QKFf_OQY8xTGIEI0nvazfF_TCm-L-J5txDtS6XPkWjkOSAoOLLZy9Jkl3Xxxd0nj1wzuLYaeIdb89866Qel_DCAmqQhVGquM0VSZ75SWlh-L9rg-l7pHM9X35fXe7kLFi4ZJQkz89iI2i2aBdi8TagbsBIhFAnFTL_R6O1nAHw_ct9BxoxcxJLj7J-O-FFy7wy0VadRkLjEjNxRzA_maiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🏆
پیک‌زدن هری‌کین به سلامتی توپ‌طلا احتمالی‌ش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106937" target="_blank">📅 17:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106936">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106936" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106936" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106935">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RomlBPLApvEfngw95qzAL8M6BB2jtg6rJFQdTLaoyvyMslqAzgH7tPv8_3PK4kCZ6q_Vw962_2X3v88a1GGBmIOASS4zlfbyYx3VQ-MSrmj9Bamu0-MqdLsFzfH9dtvRMx0C1hn9Pj8LK0N_bPiPLavHJ8D7erqqe5ghIPCFjtF31_p0HpmGsI_1KF-bQvDmZYaTHTuHdG7nQX65Dp6LFTh79_V4otTPDKTlHBZVNF-3yzxQRJt3TZKV97vraYz8gDf9P8tng6uyovDbCmZk6_5MV3tEkGjecbjF4dcqWoF_RjFDI-9SRxyhfJtqKhFGK_QS7AU4sDJOKoR4AQJ7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106935" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106934">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">برررررریم سراغ دربی حساس مادریددددد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106934" target="_blank">📅 17:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106932">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iK8XoEv_c2y7DPJKiBqQfMFIayN3klP5aMNmnAulWwpKg9snYx_C4RqBxKWoHUo8SKEpZWDCHSaBsXV1tG6XoWTminBbInHfILcIW66MfYJdAo01YN8OuompXB44GGcJmI8vbA_v9L0zvRqMLXkC65SzrVX9_QVUJvPWRc_Hk31vMsZa2wN84tmzTRhdawK4PcOvu7K1CU7gECvLmjBnAsabRl8AfoGcQja0z8L1vNm2GyG5a_8sEgJMlKfqlHz9ddcWXEHkhSN61lGODScSp9aGEDoIHJ80SypDRp91VcjYlXy9Zdx7NjVxZkOF_3jqV7WOuNIUNgd3rZIw6Qhg3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpBY0cZ46SLLhqUkdSXBzNAa69OWXcaCtWBbyKN4nWc18G0uEg0dsenFjVA6s2LQKdJP1UMRot6gqQiyoJ3GeTdpodrM_8YNTYXH9gsXdrlwXlIx4I1GihUWwso6fH1YNh1gD2aOY1rLMd7R7e6I3HucW4XwEHevkN3gUQmwq2G_6WYxcqn-nIPgkXOkeKbFsVRvnITFgP2qr9yZ-zR6tfj-zHGJ8v9L_x8MMqvb8wO43W7KsYXvd-1e3zUwHH8M1qhC20dGHN-li_wKV3dki9O1C35DbdzmJLu--Z6C2ccruSFGOx8UgOq2NrIEHqn13i_rsDbp8pfCCtOg9Z-x1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
ترکیب دو تیم رئال مادرید و اتلتیکو مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106932" target="_blank">📅 16:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106931">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c42dce9e.mp4?token=fZaSs0GoahiUdKUfBBhWGsWDX3hAA8z3n7nlUq4nFLgGcruvlf4xJNDhwmEkiQPr5l82059uzJAQitSb5TLY25A0DsMxvH5aU4J2ejsf2w3CvFF9R3naWdRwG5XC4PzKIwNcyGQAfGMEiqY_oKH8_50BTcmc5zEVyTOL51gtGC9G_3_ZZEMuQLO0iZiiINJJXHCiUCMVOoDbueIgny_MEl7rXMU58LAdhJuCs3qDkpJ6zXw2J1JCq01eI0maR1uq-J8PXLR1kXnuC9dDxPzR3WIFp43wWldtPzGABEYHwC7XdNFzhYVHHFvgUULDTzUp4-_rr84qERc2fdAKiYbP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c42dce9e.mp4?token=fZaSs0GoahiUdKUfBBhWGsWDX3hAA8z3n7nlUq4nFLgGcruvlf4xJNDhwmEkiQPr5l82059uzJAQitSb5TLY25A0DsMxvH5aU4J2ejsf2w3CvFF9R3naWdRwG5XC4PzKIwNcyGQAfGMEiqY_oKH8_50BTcmc5zEVyTOL51gtGC9G_3_ZZEMuQLO0iZiiINJJXHCiUCMVOoDbueIgny_MEl7rXMU58LAdhJuCs3qDkpJ6zXw2J1JCq01eI0maR1uq-J8PXLR1kXnuC9dDxPzR3WIFp43wWldtPzGABEYHwC7XdNFzhYVHHFvgUULDTzUp4-_rr84qERc2fdAKiYbP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
دوباره از ایتالیا صدای گرگ میاد.
🔥
🐺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106931" target="_blank">📅 16:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106930">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b89b6e77.mp4?token=LejEJY8kjiiWSvWvIHISjoxtuP12mHFuFsdZB7LKgwkXY3Oaq3Kj6tqIXWIldSaFDfzNGOfaUdgOGetsMhRQazY8wV49iQXyGUX3KNCQ9o5LfDquVtHAkVwtF9GbHvdPvdkMS6bKwiFiXQ1vD70KkOXJvMOoSmiYcQl_WH3jCe1P_429lRWw7L4tsrHHv8qCIv7CMQ-TuMgzX3omWcw3mb47mSF7oU398wZqgyoeLajynOiFA7fxSJujJEaF-zMzaw3grjYXP1OBkVZ6NBxsGIqtlbz0mLpnmqFJ-AvyqWGGGf0YowrGHmDJOen8SFGNIYMhatFZgWAGC3n7RSxEmIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b89b6e77.mp4?token=LejEJY8kjiiWSvWvIHISjoxtuP12mHFuFsdZB7LKgwkXY3Oaq3Kj6tqIXWIldSaFDfzNGOfaUdgOGetsMhRQazY8wV49iQXyGUX3KNCQ9o5LfDquVtHAkVwtF9GbHvdPvdkMS6bKwiFiXQ1vD70KkOXJvMOoSmiYcQl_WH3jCe1P_429lRWw7L4tsrHHv8qCIv7CMQ-TuMgzX3omWcw3mb47mSF7oU398wZqgyoeLajynOiFA7fxSJujJEaF-zMzaw3grjYXP1OBkVZ6NBxsGIqtlbz0mLpnmqFJ-AvyqWGGGf0YowrGHmDJOen8SFGNIYMhatFZgWAGC3n7RSxEmIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
بغض ایراندوست از طلسمی که شکست
پدر و خواهران مریم ایراندوست در ورزشگاه، برای اولین‌بار؛ خانواده‌ای که بالاخره برای یک بازی زنان دور هم جمع شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106930" target="_blank">📅 15:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106929">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e67d6e531.mp4?token=l5bHq7SLhtOr39auIMrhoSSdYpvjtCjDwAOwolsqdYC0pJS-g7i2kP3JPue28qtG5_LjjkguiZHoq2MgQRv2Gk2EFBGksYv1YA50YWo5Ep1nNutyvnrxSBj2LxMRtWdxAwnu4IIEj5e2XkJ-mRjVjdU8ugdDmZlR6AaqoS1xvlvxYgOXCRxXOxS9yY7Hm_A_jkCAAEHUsmilVl4O9jVGEqrNY_ZMG9WJZkB7QixL21dZYt1xHMADJJnvol0-b4pcffjnkBD7zqnKHmp6g65H575eTymvLTssGEq5zGNzo_-6r4TF5mRLTqQEMLL8hATjA-JmRbvjhDnpsr7cfmuhDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e67d6e531.mp4?token=l5bHq7SLhtOr39auIMrhoSSdYpvjtCjDwAOwolsqdYC0pJS-g7i2kP3JPue28qtG5_LjjkguiZHoq2MgQRv2Gk2EFBGksYv1YA50YWo5Ep1nNutyvnrxSBj2LxMRtWdxAwnu4IIEj5e2XkJ-mRjVjdU8ugdDmZlR6AaqoS1xvlvxYgOXCRxXOxS9yY7Hm_A_jkCAAEHUsmilVl4O9jVGEqrNY_ZMG9WJZkB7QixL21dZYt1xHMADJJnvol0-b4pcffjnkBD7zqnKHmp6g65H575eTymvLTssGEq5zGNzo_-6r4TF5mRLTqQEMLL8hATjA-JmRbvjhDnpsr7cfmuhDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
🇮🇷
فرشید اسماعیلی: یک‌زمانی در زمان رویانیان در آستانه حضور در پرسپولیس بودم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106929" target="_blank">📅 14:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106928">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shSp_wlhCU7pctJDFDIM17Gqz2xmXkuxk-rMqP0UUFPlel2RvXUxB_mMuNMAHNX1SUunF9qIfGAOHVNSmZn04Ii1sTzOasVxYikZvo31_Xy0dXM97wqLAJkPYfwJYKBpkS6-kUSmraWBCbLNdFG569ZRqTena4yuiXkSbyGA9G-REspukLmWYDcwvLLYn3zd_DsOySI1MIo5bsKZbCvP2IuPseEkj-gVF1CQXBWmjs-shzDfM14Zlp2qHXhqqP34xCy_Q9cq2ZmBEWXY631szPXOkCOBR1imcN-WWjQaIQPJI5jLm3pmaWZQIGc5NR6XPKVCk7-DD_7l0srh8tIG3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشون زید دیومانده هستن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106928" target="_blank">📅 13:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106927">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=ju1wm5T4w1oOw85-X_eP8XpB-JukrGll7AWxmwXeEGihPNT3dBW4NqT5tk5nQKq-96ZZdIJJPetot3hoKJ3eJ7k2jCmV6CZLAci54UioLcVHmH6mG52OSSdwpo0yFmu_nwutmOG3j7FJtSP1ML7DtRKeloXGvJQDpQPhN-JZ6JOWI56MGbMJG3U5eHwXFPaWbxRIx4ln507UtU3zhr5Mb6R-Uf_yG5T8F8YJ-PcMCCzW5w8omPQiGGNhFIu3CR07sqC4uU74dGGUoUFJA9KBbs531pTDO9Dnj3U7Vn2VOPvDEJSyja6QQUhDTE6z6p1vzvyQB-D24jfnE8XOTY4C9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=ju1wm5T4w1oOw85-X_eP8XpB-JukrGll7AWxmwXeEGihPNT3dBW4NqT5tk5nQKq-96ZZdIJJPetot3hoKJ3eJ7k2jCmV6CZLAci54UioLcVHmH6mG52OSSdwpo0yFmu_nwutmOG3j7FJtSP1ML7DtRKeloXGvJQDpQPhN-JZ6JOWI56MGbMJG3U5eHwXFPaWbxRIx4ln507UtU3zhr5Mb6R-Uf_yG5T8F8YJ-PcMCCzW5w8omPQiGGNhFIu3CR07sqC4uU74dGGUoUFJA9KBbs531pTDO9Dnj3U7Vn2VOPvDEJSyja6QQUhDTE6z6p1vzvyQB-D24jfnE8XOTY4C9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رختکن چلسی بعد باخت جلو برنتفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106927" target="_blank">📅 12:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106926">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=m6y_n-KXJByIP_88XItEQlsFHzHWMNcOS9OGETrkBHvrOSIHyTPw3-dLft37NgKmXv0bNGe0ARHYesxNBYAA7Oj6zANpPguiiONltEA6dbvgBfLEtf2SLn7SmNc5w-R58ky42_jetlJLzwKY9qtJjL3hMlQoAkF65Qq_m3r1M5GwOIh3NS52g7LOy8ReZjmV2AATbZNiEiaG75uB8MzkAdmpLD4Qibs5g8zWPBXMCm8dJRPZEW5ouFbfDYCAQLYSEfXfNALxrz8YlRSt1K5V1NAa2p8Gk57g7xnr7a7MlFFKuPnGaBaVi2gmPT7nwDMXEOXxaB5OgcA5E0KhRiZJdgUK59alO2JJjF2io9jjJwwNgUDQ1tjv_AQoHOHs8iEYDAYXFbXB89qPXVS79z1Zacvhrre-Fhq56I8z18egMgjglSsIZifwHl3TIlSdsxhA-AMX_Ts60Riaq8gdd7uMyIXhBAKbNPKiC2N3HWYFo_7mRnwxKIz3PDYPyqv6pUeMBLreW_RHcSe12joSCn99SKqdSPH32MphSKvjGS6wDZlLPoiFtZ7onLOcGSzujDUE78OEbx6p888W_Axwu307_ycaJrdyDJ_hXKrZtCM9ddDrO0LKQxWglP0oxSObAAKU5oV6Nn1IqiStslLacd34sAbGG5aYhLfLF7nN02qJmPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=m6y_n-KXJByIP_88XItEQlsFHzHWMNcOS9OGETrkBHvrOSIHyTPw3-dLft37NgKmXv0bNGe0ARHYesxNBYAA7Oj6zANpPguiiONltEA6dbvgBfLEtf2SLn7SmNc5w-R58ky42_jetlJLzwKY9qtJjL3hMlQoAkF65Qq_m3r1M5GwOIh3NS52g7LOy8ReZjmV2AATbZNiEiaG75uB8MzkAdmpLD4Qibs5g8zWPBXMCm8dJRPZEW5ouFbfDYCAQLYSEfXfNALxrz8YlRSt1K5V1NAa2p8Gk57g7xnr7a7MlFFKuPnGaBaVi2gmPT7nwDMXEOXxaB5OgcA5E0KhRiZJdgUK59alO2JJjF2io9jjJwwNgUDQ1tjv_AQoHOHs8iEYDAYXFbXB89qPXVS79z1Zacvhrre-Fhq56I8z18egMgjglSsIZifwHl3TIlSdsxhA-AMX_Ts60Riaq8gdd7uMyIXhBAKbNPKiC2N3HWYFo_7mRnwxKIz3PDYPyqv6pUeMBLreW_RHcSe12joSCn99SKqdSPH32MphSKvjGS6wDZlLPoiFtZ7onLOcGSzujDUE78OEbx6p888W_Axwu307_ycaJrdyDJ_hXKrZtCM9ddDrO0LKQxWglP0oxSObAAKU5oV6Nn1IqiStslLacd34sAbGG5aYhLfLF7nN02qJmPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
اقدام عجیب و جنجالی سیگار کشیدن مجید واشقانی با اردشیر رستمی در برنامه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106926" target="_blank">📅 11:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106925">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3BgKA7JCTAS9Mb6c2u3VONClZT6jvkG9OHzCc9v74YCEU84wDAfXtcBfSeQ4synDVpJl5FzNZ4EbiSPYYriIhJdhKBNIxAYoRdZ_xJzX9_Dn8XVkpPapj4qSSqupAaVX4FOg2lCp69bW1fwweMeHNG8GMq1UdI44eMYILS5QUAmWJOQxVyLGPP7UozLDKmjTyi1ujeyvkVPdIiz6gb_Vr48w9h7MkR9s3hgAkaajwotPXk-qrOwaDgIzcg3VjhgsO7NIklDLHhiy21hjkWxI1Es3kFV-tbIIOjRxZvhm9oAb1UCjH661UlHs8iO_TQi4FLf-ZRp_5rzlCxWxUq30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106925" target="_blank">📅 10:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106924">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنالیز متفاوت و جذاب از تاتنهام که برخلاف نتایجش، فوتبال نسبتا خوبی ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106924" target="_blank">📅 09:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106923">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=Knhx4OmS6O1u7OnLSme3ECEuyGKj6XxTuSG_i10ugDUEMWlWNEAEVAe4rQooqbuJeczjZ0LIVA2T4TfvmXnQcSO2loUP1y4wXs3TSSqB_0Oi30L83qRaxUG_l8Ux7GzerxLriq6C2FTHmzro-rRYBdHcbyupTrf2pQlUE8BdlaRv_NzFcYNzn0cXl1XGPdfdcEthfLRSum61oty3u0peq9xbf8Hy73oUguQSCTarHYYRJGI49K5MVtsKUgG0H0PrZ-IEeaINR9IMtR1zUP0l7-on8ZP7vJN_59fiGFeUyX6gVu3qzZXgCVMHyOire-Qec5LMOo03NzcOZsaf3SkxijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=Knhx4OmS6O1u7OnLSme3ECEuyGKj6XxTuSG_i10ugDUEMWlWNEAEVAe4rQooqbuJeczjZ0LIVA2T4TfvmXnQcSO2loUP1y4wXs3TSSqB_0Oi30L83qRaxUG_l8Ux7GzerxLriq6C2FTHmzro-rRYBdHcbyupTrf2pQlUE8BdlaRv_NzFcYNzn0cXl1XGPdfdcEthfLRSum61oty3u0peq9xbf8Hy73oUguQSCTarHYYRJGI49K5MVtsKUgG0H0PrZ-IEeaINR9IMtR1zUP0l7-on8ZP7vJN_59fiGFeUyX6gVu3qzZXgCVMHyOire-Qec5LMOo03NzcOZsaf3SkxijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
😢
جوآنا ویتژیک ورزشکار ایتالیایی در مسابقات چین یهو وسط کار اسهال میشه و بی‌اختیار ازش خارج میشه اما با این وجود مسابقه رو ادامه میده و قهرمان میشه. در نهایت از مردم عذرخواهی کرده و گفته امتیازاتی که گرفته رو ازش صرف نظر میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106923" target="_blank">📅 09:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571388041d.mp4?token=TL102K9Ne_jY632V16Tt8N1n5X0i_-14CuOtwrs8HPA6I-N-LbeCYozTeH5zEFcfMZdP4Ds19xLiEVPLm9zcuFQ03X3Ybs2W_BgthxOXSu5sXbFzc13HDU-z5aTb5AfaCAK3WmIFI0l4qOIw92xoAVp8JgVih1J2ByUbfn7z7RyXZ1ROSLX9ZGvo45_HVTZN4FssPCur5fyNwaliNMk1EU6vXCHa6-dwU584XAXyMOx5n28JcYj3v91ClIpTCkYRakbp94btoI2kqK5ALIWUGbFz89hB7uNgK9wUpbIm3Odg1HmB4Au875SOypRd9e3DeDruQ4Iip4mRQfO24gq_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571388041d.mp4?token=TL102K9Ne_jY632V16Tt8N1n5X0i_-14CuOtwrs8HPA6I-N-LbeCYozTeH5zEFcfMZdP4Ds19xLiEVPLm9zcuFQ03X3Ybs2W_BgthxOXSu5sXbFzc13HDU-z5aTb5AfaCAK3WmIFI0l4qOIw92xoAVp8JgVih1J2ByUbfn7z7RyXZ1ROSLX9ZGvo45_HVTZN4FssPCur5fyNwaliNMk1EU6vXCHa6-dwU584XAXyMOx5n28JcYj3v91ClIpTCkYRakbp94btoI2kqK5ALIWUGbFz89hB7uNgK9wUpbIm3Odg1HmB4Au875SOypRd9e3DeDruQ4Iip4mRQfO24gq_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇪🇸
کار جدید حمید سحری از برد امشب بارسا: واقعا کی میخواد جلوی این بارسا رو بگیره؟
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106920" target="_blank">📅 01:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dL22XMCgCfRSvCMLdk0PnWOScp8UN1VXDjBGjUmcNHE2hgeynZGpedHOQnvARUHP8MGNBqMlpuUd5Ga1GKEyTP1v54rrLb2HKHe0feX1xjBjjCNNL06K5qosg5q6qq7yVoun-WXjCxGviGc3ZmpH6ff0xO9i46QIOi7v0hQ_VYmzxQcDQkHkPIj15iC1LMhwE5IqiAS4rz_wdS-iSS26WS1SO20iYjMLi0xDq2DKNBS7OPIyzkznDQxlSAKFDZJt0d4mMQWr4ulffD2NX5aoLf29ILWdx_w6_-yTMCPOmZcWMrSrELiD4MZVgmYiJZIyG1MFLnYxGyJA_jfSfBC32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
براساس معاینات اولیه، کریستنسن به مدت حداقل ۴ هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106919" target="_blank">📅 01:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106918">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIHdhtkIgpTUCCiO8r3h-xj0PNWFOV6I_qq0CvpUnpVS_3OmR0RLbKE5kx2xJQDDgWUc0H953iWoXAjb_n0q2_xS5__Kqg5rggYMSe6ew0KUZi2lPCZWGo_jpcuUVMtnH65clw43JJ14-lRycvKb2v1zev5so1refb9673KAc1Qs32K5lKQXQCngcVuRNIUOacecznPFQY9I6v9VlvgrbfJS_9WXYN-MLGwQH0YM_CNdjOIFgvIT--wkh8IcdANfMcnvTGKSALE83DnBDdLIWq47pB32wbAyAg-beSmqMQcFDV5341c1u_XvNAgrx1ncyWJScwMPS8yaKv0QZNXwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇪🇸
هانسی‌فلیک: شگفت‌زدگی بابت عملکرد رافینیا؟ بله من شگفت‌زده شدم اما نه امروز بلکه دو سال پیش و هنگام اولین تمرین با این بازیکن. او و لامین دو عنصر فوق‌العاده تیم ما هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106918" target="_blank">📅 00:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106917">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDw7o3SB3D5zaK3mnyQlCrWyIaOfoB8S9PQnNcr4aM_PvJ8iafQg8zH1HtanqR9suR70y9L5pCLlcPV53HOpdKnQ0aq0yXFp8SPPDgvnnLiLQJTv7_FWmOam09cYvgPbEWpqTy0ZhLcD9FSsTCqn2ERaMkN0r2V56ZdzRIB8WoaPSTa3wnoslzgz0a6z6VcazjURcNvbCUQ_fqq75nOnXpuj15bSI6qG0v1w5PZr5hu3Xwi8luH6U8LXICYDBT67oCGQ7gL14iL-WasZN5ibkYQpw_EoZvP5InpWXh6NBL6JlKdg-OmkKrVF_LqdxblmDqis5rjZvDU0gELYk-4ZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد بارسلونا از شروع‌فصل تا امروز؛ بازی بعدی تیم وحشی فلیک ۲۰ روز دیگه مقابل ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106917" target="_blank">📅 00:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106916">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_s0m3dmK6WP6CZ-fTjCgHwfpdHB75hT_GaMwDNS00xeam0IsK5QyUQPCHKfTzjDCLbNBb655mrKvAKwoU5MNB7ogxiGypp8MGp5g2-XQz8QabRodfRR2lkXfg6aDiE_SjQ83ThcKq1K9R9Q0AyLd6LxSgPOuG1XfuplHPaB1ax2tK0z2rGa0LbdT1AH7TOf4qD7suDcKd2QzkfuvRROc6quiT4Q4go5kzyqMwWaBJrPql4yqo8ARIGBrMBnkSZAsVmCy5Jv8pzs4pcRE_QWVPljLRhKbVnpjara_v-meFyI7zfYaSm6n7Ms29RfcB4zxZNwqDzGMsWFkgUAARCM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
هفته‌هفتم لالیگا اسپانیا|یکه‌تازی غایب بزرگ بالندور در این‌فصل اروپا؛ بارسلونا با هتریک کاپیتان رافینیا در جهنم خانگی سویا برنده شد
🇪🇸
بارسلونا
😆
-
😃
سویا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106916" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106915">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1I3_nFMBFomW3M_jfcECrtNoVY5iE96K2i8UbzU-kVBIcnalvYTGfAfQaoXmsiXIUW8tSPp6dpMx13nzi_1-g9oh-_bbLXqYhmpQ-x-tiWm77TFM0kfdVUINqkUuOtcruDOcgxLRwTJEA_JXhnT_GqfgsD9ASk2cS8E-YgB56DAsTgzeMwcYi7z52Ms5r_AqZij4-NS2MdzQFTglgdGee9XMWVWMg4-HFko9KY_RBCn70U_3qVBrvdc29olgtk8xvI47PwxfWJVKHa5J5q2ZzhxArPw_jZHeOfpjFwIUyw1Cdrl0o3ojMxoKNnTNYx3Fso9uAFoZDlcVLbXsTvsFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
😳
😳
😳
🔥
🔥
🔥
🔥
🥶
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106915" target="_blank">📅 00:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106914">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkRPffW0ghEsZFgcr7v_Q5R8WFA3K_ZC1p55lxcdBu1j9BxOCDdJPHiH-qF0oZ59ofUaXlO_Ak-YPPVbYK1yO4Ksm7W12spU_PYoeiNZl8jRJ6nHgtB67rKGpSqnl5Svi1_eIVlaASu3r1Wl3aw3lE6js-Jp7qv6-zswGyrYztmASQsZDCJzTjlIACUDOpxJzHCVzcJv5lDQfFM8sMKFjEfS7aerndx4wFuqR7r0s7Lv-MKO2xer9Z5qAb3autqcCxrwDV6tLw9a-jG53dGgOl6p2YWMHKBhPh1jLWXtPcpoSva0kF6MrWtBDUf8YMTIvWOy-cOdbx9XHjJv37R94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
🇪🇸
رافینیا اولین بازیکن تاریخ بارسلونا شد که در ۸ بازی ابتدایی فصل موفق به ثبت ۱۴ گل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106914" target="_blank">📅 00:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106913">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB-Bs0k6RDbU_P_YgOkNDHmrGCzS4MTIV6dVj8qH_qZuB7_s0uIjTA4xyKY2yEEonvhtKeDe2FDX9SZTOoLN0OvqRku_094Fcxrgo0XUQ4T96owicLY6kKsoqnX9kzdTzivH07psFAMTEiv4HIRealKU8T_amNCJiG55-f4s0VFnsWmbuagXGqHTBDu3apgIX-wu64LN_KELgPHwKH40a1-nKorU03meZD02jU1nk1zYCZZTE4Ugejb_a5fluWdKYX3xsKmY1tK-mzrchkTlFMXuaVxrpMiQ1PL6QTldJQS_oLV6xwazMbNcdPOWtobxvBIj1NYmVJ10CTyw-_eLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
🇪🇸
رافینیا اولین بازیکن تاریخ بارسلونا شد که در ۸ بازی ابتدایی فصل موفق به ثبت ۱۴ گل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106913" target="_blank">📅 00:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106912">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چه پاس گلی یامال داد
😐
😐
😐
😐
😳
😳</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106912" target="_blank">📅 00:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106911">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چه چیپ سکسی زدددددددد
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106911" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106910">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هتریک رافینیااااااااا
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106910" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106909">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106909" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106908">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c2fc4a5c5.mp4?token=IlrAUCC3D3PNCKzjxirQcSl3HEDc-_mcUE9Z01rJnufPUTABqmuehEmX2mMxudxNbH0IDXPIPdlxNnBdfjuBOg7Fc9uQqSB0XCyHS5BL8LplPKxkcIAa3082cwZZUMKkRgHD6dIA1cnlL94sSPWmk_jgkOXXA2Wktz4AJVmFunbisCAldxfTybzM1jN3Dff14e_KEE-eB71qeDZ8T8woBMwAZGfXeB0E9-gZvPsML6P2SwyQXfYsoSw2Dn5UXdVJo0eGqSDyjzmLsd6KeDkgA1r3egF_bpF8rUphvc1RTA9jWCKsOOucB62QrEt2QTlgLLmOy4CjBqdXG9-sB3C8CjCnJwMm-w7oQ1C1VWEC_acGkJ0QksbmTtTTcSBALMtW7KenzBrWI2p1pgfytqLtdoey94jbWiyt5uiwzn1wkjc7FcO9oDeASDWYQYpwDUOMXe6QHRLIO10JHLR447Zol3YhoZ8Nhs7P5BqtHP8vUn5xakNF5ZaQKZLSgWBgN-z77o4qklpsmSZmyt_fjPGPnEQWpwuSWlBzrAa0Jd-9xFibq9ke_WXsetVU7QMflHVUoSc4wagsFlXF-tHGMeJqOw_sjjEwezX7SK5nv1TV21PGuLQBKCBn6wpwzlWtJRiYI7vUf2nYTdSQ1-z9_qnQ5yad8W8X7GeOyuT5t8Qg1qo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c2fc4a5c5.mp4?token=IlrAUCC3D3PNCKzjxirQcSl3HEDc-_mcUE9Z01rJnufPUTABqmuehEmX2mMxudxNbH0IDXPIPdlxNnBdfjuBOg7Fc9uQqSB0XCyHS5BL8LplPKxkcIAa3082cwZZUMKkRgHD6dIA1cnlL94sSPWmk_jgkOXXA2Wktz4AJVmFunbisCAldxfTybzM1jN3Dff14e_KEE-eB71qeDZ8T8woBMwAZGfXeB0E9-gZvPsML6P2SwyQXfYsoSw2Dn5UXdVJo0eGqSDyjzmLsd6KeDkgA1r3egF_bpF8rUphvc1RTA9jWCKsOOucB62QrEt2QTlgLLmOy4CjBqdXG9-sB3C8CjCnJwMm-w7oQ1C1VWEC_acGkJ0QksbmTtTTcSBALMtW7KenzBrWI2p1pgfytqLtdoey94jbWiyt5uiwzn1wkjc7FcO9oDeASDWYQYpwDUOMXe6QHRLIO10JHLR447Zol3YhoZ8Nhs7P5BqtHP8vUn5xakNF5ZaQKZLSgWBgN-z77o4qklpsmSZmyt_fjPGPnEQWpwuSWlBzrAa0Jd-9xFibq9ke_WXsetVU7QMflHVUoSc4wagsFlXF-tHGMeJqOw_sjjEwezX7SK5nv1TV21PGuLQBKCBn6wpwzlWtJRiYI7vUf2nYTdSQ1-z9_qnQ5yad8W8X7GeOyuT5t8Qg1qo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا توسط رافینیا با پاس یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106908" target="_blank">📅 23:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106907">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رافینیاااااا دبل کرددددددددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106907" target="_blank">📅 23:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106906">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گلگلگگلگلگگلگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106906" target="_blank">📅 23:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106905">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSRkN8Xe3mvlv2oI4DQJy0aMHoFlEn0_2rC6zjbLftRkcamz7azWntdt-c180rGI7AJUIL8p9y38DcJYtoZ4Q-a5kfI_o9y8gIqGYzfqFbIRL8GHAlCdrppusKPy0680pwIxHB4HeIoaCxSpSwpRM55RLjUQqV6co03VWTkQ3fsJ29EvEPXOSodTH6Vg-HqZZjYG9xrMCweOwDzETOFsw9YElTJHJaazPI0fXQl5lk_BkxdlthXaDfOc8DOvU-mfZ0sfum4w2fRVQMmnRU1WA2mJp3b-NyhKaf0PMZYI7LDGJuFcy3CKpevkabUMurfzs_z_O6vBSYIMnufG4eGFRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
سعید زلفی و نیما تاجیک ۲ گزارشگر مطرح و باسابقه تلویزیون به پلتفرم اینترنتی نماوا اسپورت پیوستند و از تلویزیون کناره گیری کردند. پیش تر محمدرضا احمدی هم از تلوزیون کناره گیری کرده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/106905" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106904">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9e51312166.mp4?token=knRCjBniicrcJzGzGduRUpQpVOBhht-igiQ2FZcXFM8hzttR0aKx79aBFwCZbPJaCOl4pAEeR7YG5J5tbXsUVy3XZff-8ouHSGQBs5qFs56jj4mYraWYX5VnzHTlGv_aki51EvgDELhcNV7OvIc3Ckbo-FokAX7-0b4mlDAutcKfAdZJxq7zgai-r5Aoe1IJYMv_1N_-WfsM52xh2wmGKL0tjmN0Im_00GQhYPfTD-2RFR5q8Ht4L0Axsrzpg_6H9VAnYizyg91OzcWKe3qY8YyH46zcvs2sZX24CR1BHjriFjUXC-A1Chx3SeD6Q-dbWS3GVi000VYt7CL2sPB06C_WXzyU699QKrBqCaBtw0vtF94a-MKffy9vmhrp5v7jszdlMJroofzlnbKmKwA296ThYeCe0MgRxcRu7g4oVqHQW5NQM8G-IEAeqqvRpvBqs2GWt7B6zeJ3beeWGSlehNeKuT94G1PQXYzs-Xm0vmrFVBim_y58ikfeIANhJCzOME1wpPAzcJfSsT0-224TtT6HSJ8qr4nOSvCj3hh7jQlFO55S87NWwXSys54xqeqew_D5fVhmENECRBv-kw8ClQsLPE4askccDytdjs8ncyVR0RwrikMGxXnhuQT4NmPnZ597Y9e5Q_mZTxCw33xT91OMuTyNlairbVduQHOiRbc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9e51312166.mp4?token=knRCjBniicrcJzGzGduRUpQpVOBhht-igiQ2FZcXFM8hzttR0aKx79aBFwCZbPJaCOl4pAEeR7YG5J5tbXsUVy3XZff-8ouHSGQBs5qFs56jj4mYraWYX5VnzHTlGv_aki51EvgDELhcNV7OvIc3Ckbo-FokAX7-0b4mlDAutcKfAdZJxq7zgai-r5Aoe1IJYMv_1N_-WfsM52xh2wmGKL0tjmN0Im_00GQhYPfTD-2RFR5q8Ht4L0Axsrzpg_6H9VAnYizyg91OzcWKe3qY8YyH46zcvs2sZX24CR1BHjriFjUXC-A1Chx3SeD6Q-dbWS3GVi000VYt7CL2sPB06C_WXzyU699QKrBqCaBtw0vtF94a-MKffy9vmhrp5v7jszdlMJroofzlnbKmKwA296ThYeCe0MgRxcRu7g4oVqHQW5NQM8G-IEAeqqvRpvBqs2GWt7B6zeJ3beeWGSlehNeKuT94G1PQXYzs-Xm0vmrFVBim_y58ikfeIANhJCzOME1wpPAzcJfSsT0-224TtT6HSJ8qr4nOSvCj3hh7jQlFO55S87NWwXSys54xqeqew_D5fVhmENECRBv-kw8ClQsLPE4askccDytdjs8ncyVR0RwrikMGxXnhuQT4NmPnZ597Y9e5Q_mZTxCw33xT91OMuTyNlairbVduQHOiRbc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇪🇸
گل‌اول بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106904" target="_blank">📅 22:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106903">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چه گلیییییی زدددددد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106903" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106902">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رافینیاااااااااااا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106902" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
