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
<img src="https://cdn4.telesco.pe/file/DGuTU-AmW67wLSqyIDJBbm3N1Yt4345HJCPahSokEtGFL2nxz_nFxcuQXC-snOYwJGdCjrU_2dX7F7EJQn2RrftnuCmwwQcY6MwdD2d5mekoj-XLSw2oUVVxpteKCXj5HPLVI2inDzVXggJ0RFHHTS5jEaZkimS5TUxizHP1AQ6Pvza9kXKvJSN601ICXyzY6JsJ2I_GYDRbRxm2cqARdVcKb4W61OmWgBfWavYEb6RZ7J8adOIjw--tY6MAyBW3fuKS_9LokFTky5YjEQ2sg6poWWpaHrjql-ctA1DARqhB_kmloUNF1pYWTtDky2rErLtEZh-zqB0qT5ptF0b3dg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 935K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 13:46:19</div>
<hr>

<div class="tg-post" id="msg-136623">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سؤال : بعض‌ها گفته بودن تا آخر امسال شاهد تغییرات بزرگ سیاسی و اقتصادی یا حتی تغییر حکومت در کوبا خواهیم بود، چیشد؟
🔴
روبیو : ببینید؛ روابط بین‌الملل مثل یک مینی‌سریال نیست که توی سه قسمت تموم بشه، مسائل جهانی پیچیده‌ان و تغییرات بزرگ زمان می‌برن
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/136623" target="_blank">📅 13:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136622">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
روبیو : ما اوضاع دریای سرخ رو از نزدیک زیر نظر داریم
🔴
تهدید حوثی‌ها چیز جدیدی نیست و ایران پشت بخش بزرگی از این مشکلاته
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/alonews/136622" target="_blank">📅 13:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136621">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN9s59U5JfR2Z-BPTPckegT6RrkkiGEUZ1uzwHvbd_tCSLHorvW-LgJ8GZhQXakCn1XBF-4V8IILp1evHNstoAmAQjHQ1WhZQT7T4wtwOOPgP03-PR_1FpEGFdYDjBRSUUGVDJ_R9ck8DvdWFc5Is2mIfsKzh3dm8sgdDxU7o9FRYdjMZJBsd_DTyLraV1Xc3Nqkp4vpUeesP-NKpF9ohQqOf2JU4PxPUxUUPseVl2XyM5GwPxr4S3DGecFdj3o7zayoYlEYANlKhCDTtA7IjLDBbxAiE_PHmaEcctDabV1ZEnx4ejB3PPFq545Rr2viWcdpEUGpL40YR_VbnrGxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در جریان معاملات امروز شاخص کل بورس با کاهش ۳ هزار و ۵۷۴ واحد در سطح ۴ میلیون و ۸۸۳ واحدی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/136621" target="_blank">📅 13:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136620">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری / پاکستان هشدار داده است که در صورت تهدید کشتی‌های پاکستانی یا منافع دریایی این کشور توسط حملات حوثی‌ها، حق استفاده از زور را برای خود محفوظ می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/136620" target="_blank">📅 13:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136619">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
روبیو : ما به یک تفاهم‌نامه رسیدیم، اما ایران ظرف دو هفته اون رو نقض کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/136619" target="_blank">📅 13:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136618">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
روبیو: ما به تلاش خود برای از بین بردن توانمندی‌های نظامی ایران که تهدیدی برای کشتیرانی در دریا محسوب می‌شود، ادامه می‌دهیم.
🔴
چین هیچ اقدامی برای تغییر مسیر جنگ با ایران انجام نداده است و گاهی اوقات نیز همکاری داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/136618" target="_blank">📅 13:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136617">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
روبیو : ایران می‌تونست ظرف دو سال به سمت ساخت سلاح هسته‌ای بره
🔴
یا با ده‌ها هزار پهپاد و موشک ما رو تهدید کنه؛ اما دیگه نمی‌تونه این کار رو انجام بده و به‌شدت تضعیف شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/136617" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136616">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
روبیو :  ما معتقدیم ایران نباید به سلاح هسته‌ای دست پیدا کنه و این اتفاق غیرقابل قبوله
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/136616" target="_blank">📅 13:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136615">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceca6b68cc.mp4?token=KchB9IYEfRBjYgsYnhJWisXquunSobDy27om7wccd0QPFJuDwOUbBJGDnMKavBbXEgqaCJhpXZiuynsoDJ4D-JC73YJYsdYA-3kfWE2ceiQqoxq6jJCm3RQ0igDYxydLRPC9cplt_8HaNyoOua7G-zBhWAiaaTElKmJkzYBDFYkJFqfCEcJ1tVZ9jAZ5wrPetf_6Luv7-yARa9XIJ7bNq9xoZLRzysY01OaESIRv6jG9hIbDthnpGm1OCaYINH56qn97sksNLiKuZM-msRgl6cOKkzTlfleNIGiPrLugrj2y1IDrvwL0qjd0F-hcgm7IaJmgvjJwIRHWjr4TIuspUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceca6b68cc.mp4?token=KchB9IYEfRBjYgsYnhJWisXquunSobDy27om7wccd0QPFJuDwOUbBJGDnMKavBbXEgqaCJhpXZiuynsoDJ4D-JC73YJYsdYA-3kfWE2ceiQqoxq6jJCm3RQ0igDYxydLRPC9cplt_8HaNyoOua7G-zBhWAiaaTElKmJkzYBDFYkJFqfCEcJ1tVZ9jAZ5wrPetf_6Luv7-yARa9XIJ7bNq9xoZLRzysY01OaESIRv6jG9hIbDthnpGm1OCaYINH56qn97sksNLiKuZM-msRgl6cOKkzTlfleNIGiPrLugrj2y1IDrvwL0qjd0F-hcgm7IaJmgvjJwIRHWjr4TIuspUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منوچهر متکی: به محض حمله زمینی آمریکا، حمله زمینی ایران هم به بحرین و کویت آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/136615" target="_blank">📅 13:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136614">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری / ارم نیوز: آمریکا به پاکستان اطلاع داده که برای ایجاد آتش‌بس و میانجی شدن بین ما و ایران اقدامی نکنه. آمریکا میخواد تمام توانمندی‌های تهاجمی سپاه رو از بین ببره
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/136614" target="_blank">📅 13:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136613">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری / فارس: صدای سه انفجار در نزدیکی سیریک شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/136613" target="_blank">📅 13:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136612">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPVtS7HhFMoxm_lzj68b9SKdZ0qbgjsBxe7HqPJ-_uv3Ys6cQIt_9hVPcMuprD2cZwuj4HQsAXpPb3Cu2tfGMfSWGctdhNjPKwVa51cMfaUBWrr9loWfY5hXnwm9swQOZjttPjho8QFhYWNQZS7Mp4KMBq31UYd-Kp3r0ip0KtYzTeIYpdkSRJS4DhJrOGldfpSc2aIO0HOkBJp-Vl7rSDYwtQYNRyGBA_WqP3OjmYdWdzNPO88XJMWbvTEnf-DeMN1maY4wgFfxjWn3HbB__uSVMKuI-_xZb6xjlPshgnV6nKx0iK1CsY_AXtyXZ3XLa-9f2KrKI4KT379rEbWw9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بانک ملی خیلی یهویی و رندوم اومد به هر کارمندش 20 میلیون پاداش ایام اختلال داده .
+ یعنی چی ؟ یعنی اینکه برای اینکه دوماهه سیستمشون قطع بوده و تو بانک کارمندا بیکار بودن و کاری نداشتن بهشون پاداش داده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/136612" target="_blank">📅 13:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136611">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f581a6f97c.mp4?token=h2w7WBf4Pmkj_qif_jDL95dtEg2U1GSLD5qe5TbANMUglTTBnOmuP_pKtIr9pufePE4ptZP-JXW_gAS3rdQm8s8vjGmpjKZCayWwNn5biL37W-SSrWCgAJ6a-16UI-Eolslvr0qDKuS_Bd71StokvAHYY5T1eAvEM1Xf8hdJpORX0ckd7HB_L67kIMZqU2eCKlVBeWreP78z-mQxePhWYucfXlS1ExgJEIUups215u82elePoCzNbvUwsgT6LsWBMD0_19uZ1aAQTRYxHI2NUWsBWm11FnLS8u9lrr7JCcI_BQiHdTGQYDFFyReXU5MgA5bMDFWtg6jQiK2WsPycWoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f581a6f97c.mp4?token=h2w7WBf4Pmkj_qif_jDL95dtEg2U1GSLD5qe5TbANMUglTTBnOmuP_pKtIr9pufePE4ptZP-JXW_gAS3rdQm8s8vjGmpjKZCayWwNn5biL37W-SSrWCgAJ6a-16UI-Eolslvr0qDKuS_Bd71StokvAHYY5T1eAvEM1Xf8hdJpORX0ckd7HB_L67kIMZqU2eCKlVBeWreP78z-mQxePhWYucfXlS1ExgJEIUups215u82elePoCzNbvUwsgT6LsWBMD0_19uZ1aAQTRYxHI2NUWsBWm11FnLS8u9lrr7JCcI_BQiHdTGQYDFFyReXU5MgA5bMDFWtg6jQiK2WsPycWoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمو قناد: منو از تلوزیون بیرون کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/136611" target="_blank">📅 12:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136610">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
شبکه کان: جولانی اماده حمله به حزب الله می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/136610" target="_blank">📅 12:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136609">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فارس : دیشب تو تهران پهپاد زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/136609" target="_blank">📅 12:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136608">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
بلومبرگ به نقل از مرکز مشترک اطلاعات دریایی: انصارالله در حالت آماده‌باش کامل برای حمله به کشتی‌ها از مواضعی در نزدیکی تنگه باب‌المندب، در بخش جنوبی دریای سرخ، قرار دارند.
🔴
منابع نزدیک به این گروه گزارش داده‌اند که انصارالله آماده‌سازی‌های خود را برای حمله به کشتی‌ها، از جمله استقرار موشک‌ها و پهپادها، کامل کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/136608" target="_blank">📅 12:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136607">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48145b816f.mp4?token=Fwlk-HJU66pv0-3vmPACDu-xLZ-PlGNPB5FizzK9xhPnu2RpyV7AUylPMEHekqvFYs8vjQ-_Zcgq1AkMYabsthLpxJyhg3TAE0wXf3R3P_JwfGOUjHsX3Bye49S4bj-oQE6bWWI3ooAY8Xg82mQbqxj33jBQBtEl0DTXh9wBFjBBEiZtPvWu9U6nrLhqdXrlGbl-G5051EJOCbQqNsg4UFBpVl0JYIBKHVicNpr7ehHZb6tMkhtvs-ARWXikogZod4t4A-nI12WZPo93grTV3B1C4H7jDHrRiUYgInBz62aEhVMpd9cvpVXW5sxIRjGL2bdWfC-0ffNyFtg0SFu-tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48145b816f.mp4?token=Fwlk-HJU66pv0-3vmPACDu-xLZ-PlGNPB5FizzK9xhPnu2RpyV7AUylPMEHekqvFYs8vjQ-_Zcgq1AkMYabsthLpxJyhg3TAE0wXf3R3P_JwfGOUjHsX3Bye49S4bj-oQE6bWWI3ooAY8Xg82mQbqxj33jBQBtEl0DTXh9wBFjBBEiZtPvWu9U6nrLhqdXrlGbl-G5051EJOCbQqNsg4UFBpVl0JYIBKHVicNpr7ehHZb6tMkhtvs-ARWXikogZod4t4A-nI12WZPo93grTV3B1C4H7jDHrRiUYgInBz62aEhVMpd9cvpVXW5sxIRjGL2bdWfC-0ffNyFtg0SFu-tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیرمرد افغانی که دختر گرفته: خوب کردم باهاش عروسی کردم، تو همه جا دخترا رو گرفتم حتی تو
ایران
، به کسی هم ربطی نداره
🔴
وی عضو جبهه پایداری افغانستانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/136607" target="_blank">📅 12:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136606">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc7550845e.mp4?token=CRA_BGnCXZ_jfzigD20Xd2x0wsMY-lm982jV0lkaZAahobRYGm_o3NMFPQ0ekamN_jUOfSfdMUW7DYi5xl2BVHb-HA02f4SBNfCjuLiuU4Qb3EEdBj73Ie8WvelBHFgrSNSjCuXKf2S-FBuiJX5G1f0fNUWxx4OQ7i6c6pbC5VseOZITEn4Q9PZnVqAQQYh28lzIfLxLbAIbQmKzVArsYovn7cgaKjnsdvmgKVmPZtKXOkfqmJQGPZz3vw2KjSLVHgSWvE0VJq-TAHBB2eok2O25pfGCmLnFnYInfeq-Pe7IE_SrFM9KPqkiEkz7tznFeWOmtSXCbAQLkCg4Mt8uYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc7550845e.mp4?token=CRA_BGnCXZ_jfzigD20Xd2x0wsMY-lm982jV0lkaZAahobRYGm_o3NMFPQ0ekamN_jUOfSfdMUW7DYi5xl2BVHb-HA02f4SBNfCjuLiuU4Qb3EEdBj73Ie8WvelBHFgrSNSjCuXKf2S-FBuiJX5G1f0fNUWxx4OQ7i6c6pbC5VseOZITEn4Q9PZnVqAQQYh28lzIfLxLbAIbQmKzVArsYovn7cgaKjnsdvmgKVmPZtKXOkfqmJQGPZz3vw2KjSLVHgSWvE0VJq-TAHBB2eok2O25pfGCmLnFnYInfeq-Pe7IE_SrFM9KPqkiEkz7tznFeWOmtSXCbAQLkCg4Mt8uYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه از خنثی‌سازی یک حمله تروریستی در سن پترزبورگ خبر داد
🔴
یک شهروند روسی که به منظور کسب درآمد با سرویس‌های اطلاعاتی اوکراین تماس گرفته بود، اطلاعاتی درباره شرکت‌های نظامی سنت پترزبورگ و منطقه لنینگراد به آنها منتقل می‌کرد و همچنین از سوی سرپرست خود مأموریت یافته بود تا خودروی یکی از کارکنان صنایع دفاعی را منفجر کند.
🔴
به همین منظور، بمبی را که در یک دستگاه ردیاب GPS جاسازی شده بود، از یک مخفیگاه برداشت. متهم تصمیم گرفت با این بمب سوار مترو شود، اما در حین بازرسی بدنی، بمب کشف شد و پلیس او را دستگیر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136606" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136605">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2978f1e3e.mp4?token=bzMzx6rVpnmJGjYwCvTO2C7qDCBvbMU0cfs8TsNlY6TBmOz6WKb1HtEbnASQUybpWVByopaNNUJu13E8aT6d4C4fiTlaQ0MQclphkmjophBduVEXshAY7Rf9Goa80J1WP_f58K8lg980ivCuA-P6Pyde9LfakajXIKlUgZ3ivXyIoGzZxyp2CQ2mWR_utM_Dnr1x7L-W6oT1SFjQqpC3U-dqxtc4xQfDL1__c0XEQDMEN7WqTs8nGaSmBMElbtGdrPJylQPmuS_3JbcMMmKlOG0KdvBW3TaWJZaOpFRE85cAqFNDsQs4Qanve8GYrrUIdD0PTL_LBIWLJfFgwZUYO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2978f1e3e.mp4?token=bzMzx6rVpnmJGjYwCvTO2C7qDCBvbMU0cfs8TsNlY6TBmOz6WKb1HtEbnASQUybpWVByopaNNUJu13E8aT6d4C4fiTlaQ0MQclphkmjophBduVEXshAY7Rf9Goa80J1WP_f58K8lg980ivCuA-P6Pyde9LfakajXIKlUgZ3ivXyIoGzZxyp2CQ2mWR_utM_Dnr1x7L-W6oT1SFjQqpC3U-dqxtc4xQfDL1__c0XEQDMEN7WqTs8nGaSmBMElbtGdrPJylQPmuS_3JbcMMmKlOG0KdvBW3TaWJZaOpFRE85cAqFNDsQs4Qanve8GYrrUIdD0PTL_LBIWLJfFgwZUYO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمریکایی‌ها وقتی تو پادگان موفق السلطی اژیر میزنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136605" target="_blank">📅 12:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136604">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
کابینه اسرائیل روز یکشنبه شب، جلسه اضطراری برگزار میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136604" target="_blank">📅 12:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136603">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ارتش اردن: موشک های ایرانی در بیابان سقوط کردند جای هیچ نگرانی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/136603" target="_blank">📅 12:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136602">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2tInCsGj0eJPsK10XNTwUU9hCgDdK7l0DzSGOhhEW84sgttzmS1TgG1lwqAGPIy6EcqF_9BsdTBGHUncLf5GbDOupQZm7lxyhi6t0PUqVUiVWk8t3KhS8tOBfwZggjSOloLQmi6jHFI3558yy-Xk6dAp0QXduSmIRA99VszMPLHw94rwERlbUZaKAYKaRZaHKKF3c1FNAUhyMcolOuR36uITdAE9d5zub40m2Jx2FndZO7dQWwhcQmPpGbWg3JNE3Zu9GkYAO_4Moxy4my7Ep9oVMmz8k8mQRCtwaP94mAQrwR8xF4Vshs8Ix1exrWKbq6Mk7V77s3S5NKCL418tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت طلا و سکه هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/136602" target="_blank">📅 12:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136601">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پزشکیان در آستانه سال سوم دولت: دغدغه من ایران است
🔴
دو سال از آغاز ریاست‌جمهوری مسعود پزشکیان می‌گذرد؛ دولتی که کار خود را در سایه ترور و بحران آغاز کرد و در ادامه با دو جنگ پرهزینه و ویرانگر با آمریکا و اسرائیل روبه‌رو شد. اکنون، در آستانه ورود به سومین سال فعالیت دولت، پزشکیان بیش از هر زمان دیگری بر اولویت اصلی خود تأکید می‌کند و با صراحت می‌گوید: «دغدغه من، ایران است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136601" target="_blank">📅 12:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136600">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqi1aK3kxkB0MLcChNUnYNEdyIGQd1QOGhSUKUU_xX1dNBydkrByA0F0oAZCMK0ih5-85kSO6tmhrmtY-a4c4zH9IWgIgDHlSHlhu6Ql-Erh5qq7SnQAeiq0lRrwbbfPWeyJrEUfOGNPMW-87bx8jUMsbZDt_4ltN-gO8RM83oAUC_SO2391rspBqDOy9bATMoPHk9DqcYMT-Qj-5BWw8FwKFc9dFR9AuExeGCb-xLYivui7m_nPgvmQB9iENR6U5FivwF5hGPvXNx_IS282P7oQt-PS4uxL8VHG6aZQc3WpQ_Z6uoB-63R5UHD88znD7A6F9hi1SnkbfOIEgqaReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخی منابع از بلندشدن ستون‌های دود از فرودگاه ملک حسین در اردن خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/136600" target="_blank">📅 11:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136599">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فرمانده کل ارتش: پای آمریکا به ایران برسد با هرآنچه داریم با آن‌ها می‌جنگیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/136599" target="_blank">📅 11:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136598">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c042ac37e3.mp4?token=vD213YYiJvo3omAigYUbUln6CQtXCo0wPgPgF8Dx4YgkDVKICRdhyLU0swj9uouiTWat2LmtJcnqvF13mT8w_mGYQATB-fZSP7db67WZJh9U4Rp_EI0d55tyFK56UFyMQ0eeNHU5Yw3cxRP4Dc3RQocmvmO3JCOlAXL0WMBc5qWQhbbQnFPXzEuH19dmzCBCp4f22kidBZm1d-VyCau89O1NGAHzbPm6Yk2OFW-BsQfqJgX_CkVq7CPOITUY7w3aLdlDW2aQNy5cFS8PcGrDGI9GGV2YxjCnm00skMb1-7w3QnBKv_PCqyK2DOBWpRzDT2A4xjpVtdSMFN50B208kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c042ac37e3.mp4?token=vD213YYiJvo3omAigYUbUln6CQtXCo0wPgPgF8Dx4YgkDVKICRdhyLU0swj9uouiTWat2LmtJcnqvF13mT8w_mGYQATB-fZSP7db67WZJh9U4Rp_EI0d55tyFK56UFyMQ0eeNHU5Yw3cxRP4Dc3RQocmvmO3JCOlAXL0WMBc5qWQhbbQnFPXzEuH19dmzCBCp4f22kidBZm1d-VyCau89O1NGAHzbPm6Yk2OFW-BsQfqJgX_CkVq7CPOITUY7w3aLdlDW2aQNy5cFS8PcGrDGI9GGV2YxjCnm00skMb1-7w3QnBKv_PCqyK2DOBWpRzDT2A4xjpVtdSMFN50B208kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: تصمیم جدیدی برای تردد خودروهای پلاک مناطق آزاد در تهران اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136598" target="_blank">📅 11:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136597">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df721fcedd.mp4?token=asYv5ffaBYyThUr6CeUzdjabV0AVnuCCfvPTThALuwIIGRh1fZh7c5q_Ig8J8IaAd4HFjQ2wkn1VohB8JTRa7m4IQ8guDg_2weiOFOhTnOrPdXL2ORFRevYSix4g6bH7Rb889iDb5gKjA5b_Slyev2IAISpfLHuAXyxz-QSYwuFzZAFxsY4tMu9oSeUOK1L10R-fGkD20Glr7X-rLikArbeMrDMZfySJyQsJnruzf2s4EudyWudhmcSym7VYYAEBeE7vqKB2JUfyhDk6C410IzyvK0fI6sJwjHMTIVzygcugPls8KtYvArR6S_NrUqaxvx33wegfJMgVs6O_JcNgkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df721fcedd.mp4?token=asYv5ffaBYyThUr6CeUzdjabV0AVnuCCfvPTThALuwIIGRh1fZh7c5q_Ig8J8IaAd4HFjQ2wkn1VohB8JTRa7m4IQ8guDg_2weiOFOhTnOrPdXL2ORFRevYSix4g6bH7Rb889iDb5gKjA5b_Slyev2IAISpfLHuAXyxz-QSYwuFzZAFxsY4tMu9oSeUOK1L10R-fGkD20Glr7X-rLikArbeMrDMZfySJyQsJnruzf2s4EudyWudhmcSym7VYYAEBeE7vqKB2JUfyhDk6C410IzyvK0fI6sJwjHMTIVzygcugPls8KtYvArR6S_NrUqaxvx33wegfJMgVs6O_JcNgkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکاونیو، یه ویدئو جدید از بمب‌افکن B-52 با فلر منتشر کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/136597" target="_blank">📅 11:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136596">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: پاکستان میانجی اصلی ما در مذاکرات با آمریکاست
🔴
در سفر وزیر کشور به پاکستان و در لابه‌لای گفت‌وگوها اگر مسئله‌ای در این زمینه باشد هم منتقل می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136596" target="_blank">📅 11:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136595">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a635d04da1.mp4?token=VnkDQnrK5J5c9e4lGw6UTgtzHr2muPtv-ILi0vuP6yFpRnGKOwCkFaZAob0RJFkQDJTqw5bFXTP6iRGjrFi4jgbwr0ig0TQiTg2GiXfBQzNMukESvpXsK1MooiWI_uqkJ7W9P2NmkfkyHk7zavyXwsTvytL0RN5bQmCEvWJ4m7iorWMX79K6nQaYR9Yk1JA_AK-R2Vx7eKY18pF21Qyjt4l38_3yj8OvXA40i8cKSH8NtH1_3IsstLMM2VHgyQYO15uOp4o4cvFJy9Wwk1j4voNB5qQAmh9BALvF4RwhQO1h-ErlX9dCQ94AUAk0VeZGRrWuSG44zVLVUdMAHy1VgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a635d04da1.mp4?token=VnkDQnrK5J5c9e4lGw6UTgtzHr2muPtv-ILi0vuP6yFpRnGKOwCkFaZAob0RJFkQDJTqw5bFXTP6iRGjrFi4jgbwr0ig0TQiTg2GiXfBQzNMukESvpXsK1MooiWI_uqkJ7W9P2NmkfkyHk7zavyXwsTvytL0RN5bQmCEvWJ4m7iorWMX79K6nQaYR9Yk1JA_AK-R2Vx7eKY18pF21Qyjt4l38_3yj8OvXA40i8cKSH8NtH1_3IsstLMM2VHgyQYO15uOp4o4cvFJy9Wwk1j4voNB5qQAmh9BALvF4RwhQO1h-ErlX9dCQ94AUAk0VeZGRrWuSG44zVLVUdMAHy1VgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از شلیک موشک
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136595" target="_blank">📅 11:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136594">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/977d37d3e6.mp4?token=BxvgaqmLw6Zl51oil5lqL7orVl3SpQFHSibTCByGgr6KIgWiJRxRwPVkO6qYTyMA98eq6jWV1A5FTwhuz4biN-NJ4lwd_Rf0rBTjBa8YdM57bhgUTAgU1ek-zqNv5Iw3zfXVOXMyGTahKTgk4Y_P81IS53tVYvYqQkcNs-L1RXDyg_RlKeyqDhzkp2bicpIEnbbhZ0jAwJLy5gSD9z6YaW9ryuY96p59SNwpz06uT1T_xbLfIYP9aMhxVOu5ZdOE2xBhdlavnBh8Dl4kWs2f6jga-JnKa4hmHj9o_TpW_o3a3R0yCtv58Oi2Q_CPS8oiSYyGFa9_YHb4n41rAIQdKzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/977d37d3e6.mp4?token=BxvgaqmLw6Zl51oil5lqL7orVl3SpQFHSibTCByGgr6KIgWiJRxRwPVkO6qYTyMA98eq6jWV1A5FTwhuz4biN-NJ4lwd_Rf0rBTjBa8YdM57bhgUTAgU1ek-zqNv5Iw3zfXVOXMyGTahKTgk4Y_P81IS53tVYvYqQkcNs-L1RXDyg_RlKeyqDhzkp2bicpIEnbbhZ0jAwJLy5gSD9z6YaW9ryuY96p59SNwpz06uT1T_xbLfIYP9aMhxVOu5ZdOE2xBhdlavnBh8Dl4kWs2f6jga-JnKa4hmHj9o_TpW_o3a3R0yCtv58Oi2Q_CPS8oiSYyGFa9_YHb4n41rAIQdKzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
از بازداشت تا شکنجه و قتل جاویدنام امیر جوادی‌فر؛
🔴
مستند «کهریزک؛ فراموش‌شدگان تابستان ۸۸» با روایت مسعود علیزاده، از جان‌به‌دربردگان بازداشتگاه کهریزک، و ارائه مستندات، به جزئیات بازداشت، شکنجه و جان‌باختن معترضان بازداشت‌شده و مقامات حکومتی درگیر در پرونده کهریزک می‌پردازد.
🔴
امیر جوادی‌فر، یکی از قربانیان بازداشتگاه کهریزک بود که بر اثر شکنجه شدید، عفونت و تخلیه چشم، شکستگی فک و ضعف شدید زیر آفتاب سوزان تابستان ۸۸، جان خود را از دست داد.
🔴
گفتنی است در نامه مسئولان بازداشتگاه درباره علت فوت جوادی‌فر به دادستان وقت تهران، علت مرگ «مشکل تنفسی و مننژیت و همچنین ایست قلبی» اعلام شده بود!
🤔
سگ سرباز آمریکایی شرف داره به سرتاپای این حکومت و طرفدارهای حرام زاده اش.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136594" target="_blank">📅 11:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136593">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_VNqFwYYeYhPcSWtJ8C8A9V_Kn3cMD61QBVen2VLpY5szs0fvh6clYoc7iJWAiGF1eZEzBkvECChVJRUS4q6IM3Shtqo68gsG5O3Oieq0FQkCsjBP9lDaGvkGhdRdUZ2EIEg3cIT_AlcC25lClavB8ZhdWy0-BO__jo1M1F07rF2GnjkJCrYABUai3UKciyIJxcnLqViiqlUk1uZiBqNz-hG2CJSBVdilzq_KlqTes7vxs8mqJpkVyDC2sW9Rcz5WNoEyN3mCIqHPwTGl0Lnzt5CqvDve584f9x9rolSy4wxTWoOmI3_DsnbaXNigpht9wFECa64us87qFChiXEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی نفت در پی حملات ایران به پایگاه‌های نظامی آمریکا در منطقه و تشدید نگرانی‌ها درباره امنیت عرضه انرژی، به روند صعودی خود ادامه داد و بهای هر بشکه نفت به حدود ۹۵ دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136593" target="_blank">📅 11:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136592">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ارتش اسرائیل در بیانیه‌ای اعلام کرد چند موشک بالستیک از سوی سپاه به سوی عقبه اردن شلیک شده بود که توسط پدافند این کشور رهگیری شد و برخی از ترکش‌های آن در کوه‌های اطراف بندر ایلات اسرائیل سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136592" target="_blank">📅 11:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136591">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg85XPDmhmo8doq-eKzAO2OzwnAj65utm4aFKCExX3pkOdUrfFCPBzTagVOSD2PwX9NXgsX9ZL1TCAJ7Set5B-ClMF8T-2QApbiPE1opD9JMt7BaFIePyAEz1Qra6GUDdMpJyEO1doIv5UqsGNW7RzIAOSuVCYoybV4Mwosu-cG4k_s4KCZfiITq-TTPltvfClbA4TldhLOv0-Togc3S_41j39F8wgvuZTOghDEZ_pmqG7DZ-r-JR9kxIhUeZ2XsTVWWIP-s4rzULqaSqkN9wpP9DIv9zTehTqyTK1A7CjRLltrsCke7S02rrQHKZAiA8OMg1XKxtHYYeHCMcrhFAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از اعلام دستگیری نتانیاهو در صورت ورود به نیویورک توسط زهران ممدانی، شهردار نیویورک، حالا رندی فاین، عضو کنگره آمریکا ، خطاب به ممدانی گفته تو یک مسلمان تروریستی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136591" target="_blank">📅 11:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136590">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDDre8cGgn6zc-f1I4uUcySEdLv_gFAwkFBk2qQ8FL3Wx2nfCt-pCMlU42ubcdX3vM1_VCoZW6XSBmjKdxlX6MN9b5ckH17s4Gf7z2MR3uLljv8zzUeujzC9fmMPM8OpmY4BoA6unTnORykXujc03pc_vAyP8h9ywU73Tg0q_S5A7sqN96qY2DoOVYTrSxXgzFTx72d4l9ydJFyHqww8DM2MQKnWCPMV13D1GSaojh7QF5zXsh_d5UpCp8qk3swNObhtSD4vsux60qPA0QCyB0P22nvJXdNYJG6yMtkgKE3HTQc1Y93IoAPORft8HuvUFJmxxxtODdxBLg8cdQeWpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۴.۲۵ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136590" target="_blank">📅 11:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136589">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ارتش اسرائیل در بیانیه‌ای اعلام کرد چند موشک بالستیک از سوی سپاه به سوی عقبه اردن شلیک شده بود که توسط پدافند این کشور رهگیری شد و برخی از ترکش‌های آن در کوه‌های اطراف بندر ایلات اسرائیل سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136589" target="_blank">📅 11:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136588">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c29387014.mp4?token=udlhEJixE9yvA3FmTX90UbUUxv03ja_xk-dXox6L6oVVr7mXv0DqOVgX5-3z3jvSRIFMBMz6Bki89dg8txiYA62YcV2bBT2kBWcVXslDbMDSjSjbyDrjrV_pNSDv5vCjtP1e_QBKVz8GZa9qsGDmqYQdVitffpudcL4Rw1IxOGRkPZy8uDl35Xtw4QpNkATGo9OhLVzWaDhPFv2zffapENRxdB4Oq1PSDOMUn_9OdSEkzKcxhve9lD-EM7_78PkEkOsr2N4PeeLdiuqHGISurWGa9eh94ITez8qupyANyYd7UwLn2Pl0Qwuli53mf9zZve7d4NzQmlYfF62J3XhmjI6YsrZooQY67c-txJYJA65w6JJMPwpJNyXa6QiRGsX7AZT888taSD0eUFQbo7V20cc2a3MqirxZ0hLD1JaGUX2zNmnz7jB9L44swkY9iC_sMYck2SyiuTw9NbzP5jQKeTR1Cp7AUHM2d-AO45IZQC5jaPoMSkJhB6Q_JxrlRLkUckW_P4Zl55nO80d-FboKhMItA7ykbVB8eVVUniWTw_ii3dHt4RDf4wx_yzQRwUsV6Fqi1XObGwsTn0ipG6Y-kP-vaq6tqQ09i8sMygc6qryl5sy9EuE1cMURc9u9kJ7JNbdU_yy3jcL9q7CS-oleVliXQ0z5iiA-4cBSH4eSEuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c29387014.mp4?token=udlhEJixE9yvA3FmTX90UbUUxv03ja_xk-dXox6L6oVVr7mXv0DqOVgX5-3z3jvSRIFMBMz6Bki89dg8txiYA62YcV2bBT2kBWcVXslDbMDSjSjbyDrjrV_pNSDv5vCjtP1e_QBKVz8GZa9qsGDmqYQdVitffpudcL4Rw1IxOGRkPZy8uDl35Xtw4QpNkATGo9OhLVzWaDhPFv2zffapENRxdB4Oq1PSDOMUn_9OdSEkzKcxhve9lD-EM7_78PkEkOsr2N4PeeLdiuqHGISurWGa9eh94ITez8qupyANyYd7UwLn2Pl0Qwuli53mf9zZve7d4NzQmlYfF62J3XhmjI6YsrZooQY67c-txJYJA65w6JJMPwpJNyXa6QiRGsX7AZT888taSD0eUFQbo7V20cc2a3MqirxZ0hLD1JaGUX2zNmnz7jB9L44swkY9iC_sMYck2SyiuTw9NbzP5jQKeTR1Cp7AUHM2d-AO45IZQC5jaPoMSkJhB6Q_JxrlRLkUckW_P4Zl55nO80d-FboKhMItA7ykbVB8eVVUniWTw_ii3dHt4RDf4wx_yzQRwUsV6Fqi1XObGwsTn0ipG6Y-kP-vaq6tqQ09i8sMygc6qryl5sy9EuE1cMURc9u9kJ7JNbdU_yy3jcL9q7CS-oleVliXQ0z5iiA-4cBSH4eSEuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون سیاسی رئیس جمهور: در مذاکرات بعدی ایران-آمریکا، مبنا همین تفاهم‌نامه‌ای است که با سختی بدست آمده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136588" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136587">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ارتش اردن: شنیده شدن صدای انفجار در العقبه بخاطر رهگیری موفقیت آمیز موشک ها بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136587" target="_blank">📅 11:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136586">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
ادعای ترامپ درباره درخواست ایران برای مذاکره درست نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136586" target="_blank">📅 11:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136585">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5_4yFvj9c9rxgOit-vEyvRwT78s8N7jhfpbew5iAZ962IhugPfhBVwmYgdycbyNjXRCOuxSPfUfhGHh9qe9Pk1srx1fLJ5jcB_OrXBjBoXUHhOFYSYu-RziVTq2JU6KTh8DAvgQh53u3eu2ujO5nMQPXninfwj6liXd9ZzVxFljtk8pa47oJAD-hCtoQiHh5ZtwIps5_qaAZ4qN4veMjuPkKwaNUjv1qvm_pYivugoP08u-V-4O1FAwYpViMGga4F0xY6bdfnJu8x_xUj8Cyq5AUxcGgFbGByOiWe-4mtRJ7LJfc_C7xA8libDyg-ZvUimjFvb19tqHPWDBq1PS2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر گرفته شده از ایلات اسرائیل از بلند شدن دود در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136585" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136582">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/g2IUammRRddUetbJWd3mP--bbbhVVE5gNYKvTI-gK_2VTfkL7qwDbyBlOMi-z_obPOSuP6Aus4g9Q4clCsGm6pqcP8STzn15aw8f5Y1uTu6dZsEC9OgQmfq5ewbXPrbce41cWALCSi7ogdHDxW0UcL95OFzYYh12oalVrm8Kd9yPOhlD08wKNC96dBZ7MrIXi2KFpqSl5O69JvMKuGdDHfJ9fgK8dTz6uSBx9Llj4K6UzcpIqKWDLewFNgmfi50PUJ-DmNomZNoQa9_9tUOjdHKEwqXAEIR-XPCO2OCERw5fVMUQO0IvCAi0u39yu4B5O2rMY0mZCTkDeS2rDIFeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/p9zmBRSZcluOh3l5I6JbTmlSK_ZyZwOagbmFkK0bxe0KKGfKUzQb9_9pxTYDUnZEVtXxqcxYp2259t-Kdn6DYGD7DiMmZT8Q4GgWnUtAgi8rNlx9l9Flsk1QrJb0Ilt_HpWzqU8H7KVhW3f7YeKpDqDfiplH788LLsXrBjRdqRImoDKgnij5rYp-pF7uBvTbZSKNSfyylTqQuDCtRgYCgdyfbYjpyB-HexwZdVFcotDXZHhzRKBEAvrxga4802MLQZ7U5XH_RdB9oThTz7QWImCReZPi0ERJiVsBnt8pyX_7D6RxWEpx7mTF8LkK1kLXNC5CugOwavtmOyalat7Geg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/8cc3569bc8.mp4?token=l2Pes_Odz6NkxU2QZJbsPyNvs0VXzJodUgGchp8IW1VslHkbqK9aEoNWJu9bM5iDw2nwT_wPUq3-cIE8hMa8o6iB-4l4eQvs-izBHmPg0g55GRRPYRfy9QkXLiOfRVoEPV65KAiyk-PCRc89lpDfgyHawlETrwVW29Il_CV-4H6BN0vjbTUbbcao9sYfiTvzQatL4W7TpmKitTexJkDhlNcQwV2yfK3NVpHDsiezWVNsw4dhdm1WUF_G0n3Snrja6fLTy-l9nexcJbJdkrZFN4kUtPRD8y9xagGW2rGI_K-nqLdArHFBu3RfyD8kLbhNRGm0aBgJuAtsHkDDOwawDw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/8cc3569bc8.mp4?token=l2Pes_Odz6NkxU2QZJbsPyNvs0VXzJodUgGchp8IW1VslHkbqK9aEoNWJu9bM5iDw2nwT_wPUq3-cIE8hMa8o6iB-4l4eQvs-izBHmPg0g55GRRPYRfy9QkXLiOfRVoEPV65KAiyk-PCRc89lpDfgyHawlETrwVW29Il_CV-4H6BN0vjbTUbbcao9sYfiTvzQatL4W7TpmKitTexJkDhlNcQwV2yfK3NVpHDsiezWVNsw4dhdm1WUF_G0n3Snrja6fLTy-l9nexcJbJdkrZFN4kUtPRD8y9xagGW2rGI_K-nqLdArHFBu3RfyD8kLbhNRGm0aBgJuAtsHkDDOwawDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات به عقبه اردن در مرز اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136582" target="_blank">📅 11:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136581">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnMIYZREHvdTd7IT0yLu8VNpr4cPDIgMLSUZMf6CcFgkXKF3iZPGQSDsl2Dy962IIT3GMYApvQBm6Iwd4RICX8emAHOa4971UjL9fbWQEqwR-259OvcoUufjAdmhlXQjNQZBkvP_AHlNv-l_GUlEQpcdJ5m45wSShU0MBiZph-8qCMjkRuaMRJT10r-16eu_LWrfitghwWuvBjeGiW7WS5Ty6WWOOUKj1ayXOaP-GhjZ0itFlqfnWnvLi1htMkEiHFCPDv4mqzm_FaUXGaIhHT16Be1MEP-RMXsVhtrcPdjYL85TVesD4h0ecHAssWkTyaNPUjxaCgqtABN8NvMAeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارسالی از آسمان کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/136581" target="_blank">📅 11:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136580">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b2d9cceb.mp4?token=eqO1jO7NQP1-FbE8sjx6IOl9ZVAF1aJ4sQceVrDYTfbbgLLGppaEb9qpxMFWXMiXBRvW_zgSDNmvnMbPX6aYa7XAP1aCG6O8xpmIn_klTThKZCWOh4RFES0EcASK78Aix7qyEFMzdbnkBAoJtqHsoLOht1-8zRoVtChZemNJHjjkNQRCpg6JX14JAO2sNnS50KbMHFDiSADzavALnaYhIr9-SG8H_EA-ekEfGvHD6pCqnSrAG7xY-7Dhuprw2dbfmCf2gSAmfT_cptI8nmFkxJugx6KU7WKLFLrTiLmUDf63M1OFtpAo1Ax4Mt_llnsqpr975b28Cs_wc34rbV_Bog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b2d9cceb.mp4?token=eqO1jO7NQP1-FbE8sjx6IOl9ZVAF1aJ4sQceVrDYTfbbgLLGppaEb9qpxMFWXMiXBRvW_zgSDNmvnMbPX6aYa7XAP1aCG6O8xpmIn_klTThKZCWOh4RFES0EcASK78Aix7qyEFMzdbnkBAoJtqHsoLOht1-8zRoVtChZemNJHjjkNQRCpg6JX14JAO2sNnS50KbMHFDiSADzavALnaYhIr9-SG8H_EA-ekEfGvHD6pCqnSrAG7xY-7Dhuprw2dbfmCf2gSAmfT_cptI8nmFkxJugx6KU7WKLFLrTiLmUDf63M1OFtpAo1Ax4Mt_llnsqpr975b28Cs_wc34rbV_Bog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جان کندی: «آیا ما توانایی نابود کردن هر آنچه را که در زیر کوه کلنگ (Pickaxe Mountain) قرار دارد، داریم؟»
🔴
پیت هگست: «سناتور، بخش زیادی از توانمندی‌های ما محرمانه است. اما اگر در این دنیا کسی بتواند به هر نقطه‌ای روی این کره خاکی که خدا آفریده دسترسی پیدا کند، آن نیرو، ارتش ایالات متحده است؛ قدرتمندترین ارتش جهان. همه‌چیز به گزینه‌ها و موازنه میان هزینه‌ها و منافع بستگی دارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136580" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136579">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
انفجارهایی شهر العقبه در اردن را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/136579" target="_blank">📅 11:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136578">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqnUb5bC0p2Gae4aHuBSpJM90Odj0Sgg1qz1j-vMQz_bbRP-fUTHEUv7C4HihJSiS9Szp_vToyRLsv022gsOlP25IBdiSwiSWRKbU8nWc4yokwnz_LLTmwqzUzwFxvfDZrW1cHGLycVxSjhnGNz0mG4qRblridwy0w0c941Oq_Pr0EW_qyibhNvJMFCWy7ROKScfpXC9h_mdeq4Vju3u55WMuXVqcw9rPz9HDCJ3MMi6tySOCRXBn9VHcAUEHfEOsbCFbDhMLRKK_6RU83b6mw6I77Q7g11lw_eR8WMB7M6mPlhPIxY25-v3vwyp9PzanpDiL9Bb9lcnb9TqPc_uzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رد دو موشک بالستیک در آسمان تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136578" target="_blank">📅 11:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136577">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رئیس پلیس راه استان قزوین: مأموران پلیس راه استان قزوین یک دستگاه تریلی حامل ۴۰ تن بار که توسط نوجوانی ۱۵ ساله هدایت می‌شد، شناسایی و توقیف کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136577" target="_blank">📅 11:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136576">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
کرمانشاه رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/136576" target="_blank">📅 11:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136575">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کرمانشاه رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136575" target="_blank">📅 11:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136574">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: مسائل قانونی و شرعی گواهینامه بانوان حل شده است؛ مقدمات آن در حال انجام است و به زودی شاهد اجرای این قانون خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136574" target="_blank">📅 10:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136573">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ستاد عالی آزمون‌های وزارت آموزش و پرورش: امتحانات نهایی پایه‌های یازدهم و دوازدهم از فردا طبق برنامه برگزار میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136573" target="_blank">📅 10:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136572">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">طلا بخریم؟ نخریم؟</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136572" target="_blank">📅 10:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136571">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ارتش: ساختمان‌های اسکان و رفاهی و انبار تجهیزات ارتش آمریکا در پایگاه الازرق اردن را هدف حملات پهپادی قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136571" target="_blank">📅 10:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136570">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZGhyNs8uKG5WfW0njiAA_2fIvtB6dD509NqBChgid3E0p7UkBdVQx_E-TuMnF3LLnD_RLYt8HDN6jqwJ2Fu7S366rhgyVnrRRFx7QlwWOZfuTCtiaAY8eHJOTPTPbgWP9SRNZftbUHuZIKv9xN8bm8VrszLfeHFbl-pfjYIdNXwb1ybSBTH0tqNfq2agGwDj9mPUGQh4gbKpk5q__bqVzjDsagPUrtrXspBG0umjA5Q3CwKJj9pRoNQv_v142l3evE-_Wo-bMZlE9q-5wwfEdme-V2N3mhmO4rMPXIt3lCOebNl5V4ITOXs_ureHBAYcW6vt3raPiJoP8QPsY3j5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری یحیی گل‌محمدی در حمایت از عادل فردوسی‌پور
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136570" target="_blank">📅 10:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136569">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c927f960c7.mp4?token=K4iOFilGEio_lhccpp_ZN6NDlG4zWJJ9KTHAwHWJ81-yadqrvlBXWWWreeUQagIHyFmboOv9jm-zw6MoYp47LQyay-Imp8SSlzzeo94Vjfq7gYEdsBxZb55TSEXksiD0FL_jleshdtEx59UGPvo99dcELAdCS5o3stJpxfBhaAAXXmefjaCVfzkMVABXnYS7H0Q0BcLjacmvwgPZU9MZ86YWzPJOZ9heMVUjb8OcnM1FEQdOdKk2H3nNzCh3TkpVEyuv_rwztepR-VrnlmORr9wdlGb0c_wEbHCWziUEhJK3d4BwCTMdmZClCXwn6zDPAQWdosGSMN-LonwyhJflCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c927f960c7.mp4?token=K4iOFilGEio_lhccpp_ZN6NDlG4zWJJ9KTHAwHWJ81-yadqrvlBXWWWreeUQagIHyFmboOv9jm-zw6MoYp47LQyay-Imp8SSlzzeo94Vjfq7gYEdsBxZb55TSEXksiD0FL_jleshdtEx59UGPvo99dcELAdCS5o3stJpxfBhaAAXXmefjaCVfzkMVABXnYS7H0Q0BcLjacmvwgPZU9MZ86YWzPJOZ9heMVUjb8OcnM1FEQdOdKk2H3nNzCh3TkpVEyuv_rwztepR-VrnlmORr9wdlGb0c_wEbHCWziUEhJK3d4BwCTMdmZClCXwn6zDPAQWdosGSMN-LonwyhJflCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای تهاجمی اوکراین صبح امروز دومین مرکز توزیع و انبار شرکت بزرگ تجارت الکترونیک روسیه، wildberries، را در شهر نِوینومیسک هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136569" target="_blank">📅 10:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136568">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
صدای انفجار در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136568" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136567">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3yG0gIr1Yr-Y7NNi5pbZE7tCcXCQwhE9t3lAA-35AjrB8bYj3zMkI9HvTVkG6E-77Db-bgurLLK4te_z1DPv10e7YY5wfJ-zivUMH96U3DUDFbGDsn21eKmaqlfQc0PBhJxDhKomkQ8ysLmCmboONDZAkySjgiggp80y9FbkNP_9J9KJfnw6A5KfnEEA2ZeodLhjC7W2vdu9zl-Du7lpUZOmVmqu1zO2WkFNgtYUJfi1BJ0jW_kM5RS2tFAbqG60-cEgXlT9kymoDZjK1umPRHcZRb5ifXPrf6u2dr7wf5pDZrFYPjZZDs7ZWO6bSD27WAp-ifFnre7QE8iM9FE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت به ۹۳ دلار رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136567" target="_blank">📅 10:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136566">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
شرکت هواپیمایی هند بار دیگر آغاز مجدد پروازهای مستقیم خود میان تل‌آویو و دهلی نو را به تعویق انداخت و تاریخ جدید آن را تا اول اکتبر ۲۰۲۶ (۱۰ مهر ۱۴۰۵) اعلام کرد.
🔴
این شرکت دلیل اصلی این تأخیر را «ادامهٔ نااطمینانی‌های امنیتی» در منطقه عنوان کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136566" target="_blank">📅 10:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136565">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rqw49vlzUwBQAIwF053D_xt5A8WkwmowRkAn3X6lGsTQAo-SNo5ieoENWlO100lW51ykrjutCvvycRW1iHLlQT0JsbOtqipthCZ1dAsW8vIIWngvEcVpL_ZZ9gVH9WoNOY_47M9cRRNpHLtOJHf-TACfkz3y-pUS_9MdFG9xZnetSm22A_SVhRgRicFuLSQ9mNKQY1RbKpwoiYkEnq_q75e2jjDwd_VvI9zS9_EVl2C2sjJnIvfnWYDzopr3QvvvoOZXv4MHAuEC92_ngfftztR_Wn_mFraJyIKFbKMKRvKYu7_zqGbdjuWip18bkL9RRfNOZX_GJTRMIdip_tEqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنتاگون اعلام کرد که سروان آنجل ایس رامبرساد، یک سرباز آمریکایی، کشته شده است. این سرباز پیش از این به عنوان مفقود شده گزارش شده بود، پس از حمله‌ای که نیروهای ایرانی به یک پایگاه نظامی در اردن انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136565" target="_blank">📅 10:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136560">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBCZiaCLiGjsMku8rEksSEUXox5LIThMu2rMdGF7dEAQn0AAszulTZgVjXDUVWBPmxmY52t1H_Uj8RYAvLNEFDNGsvf1EQ6DSdWGUtpJ37GlTvd73nD5_BQAOeIddguC_rEDAbEU90cRRQh0AJrMbkWnxVfWxHYtppx6blXxpXZjoqkHmeXe8lJy9AEFTCbCFzCCZY2GTrEPnvMYrwutPsmUq-pfPXjBG1eePGdF5ZDJFrkojRp8E5EiSyccOJzVcq6Ie2RLdzk7-ywUBiOe6FAAE3tIgJiVESbJgbkuuN9nifcD3GMK7dqwHLlU8pS5lH9uw5fgWUPIIscogKuXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnLHE2HC1Lv2Y-M7s5rGwum9apt9DgPEEBSCljd2mmpSMXPqARRtE6cSAmjPMmK3a9zYSAaQ8ZQOtpJtU985TQVfqqcMLc39JgVnyj5xiWH9D8qtncOEUh8PR-ilCN0STP78zfHonJBnpUskj__MyhQIJI-Hm0uneLVM5YfldRXHZmXGonQxNxCHWv_T6DbD8klzLbZIKDIBHXPVPVuA1mz6hAV36T5xJG80DFGE2JBhgE6ghGV0QrM3jTarog3rQi8g_nhTL3T94HR9gMltVL7xid81OZLV15iiyGF70c3l3zKOuhwtZM6Y18gtfjD59WBN96dqX9Ut9zCwym9ZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgegl2ChGkbI4NCCoe1Kk076I4Bsel7Pg0TyWieyuzF1jiIXzysfPpuuVUEloy80Y9W3YdmyT9VQ5QsWeL5zFNTDFFuRQGRmfAZINXpC0TJWlEKLXohb05tGejaXaHavVZW3c6rmKS7bmCKQL0aBjRx3rNdAHDojVRxsDJzbHJNQvp3V-fMGXT8ZWPZf3_jznmwpLnl_pRcafkbW1g2rM3xBHWy_dWPdS5g1RtOGHB5K4bSlAItmTEYPS71yCGzwhqHh6ROFj3Wr3WYh3RGIy7mTzyKRg2NnJ3DiC0c5MSZ-eSadf6lenyDz0xsSM929vSy41kO6yg33852_3tXlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKAghcrYdLZqWp-ZdaCDLpGo4fhv-JPS6K964_nvjTKoIwnnaSfq9FvqAbhzyGipwaagCZgS3zsqNpCORODTXb-FlJG7_9GZ-y-Gs3itPxu4ys0ZSaVr6EFUe-GTMDyOu-XapmS-6pkbgyNLeATIPvkJwUb-CFCEldLvPSf_2_IzHLLoyKR0i2-AtAEEMSyc17K6FZljHww7m31XjQbnmwJRxzb8SmHru_bW_v18MC4gtTktF8PXWJiU7Ufx7xQX7rbBlYNmMTzAUSrpIGWYjHbVq4LvL3oMWePeXSrLTJgAP3bP0hPTSD6v6Y0bSyX8qciXPuIG50-qY_SSPfshwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwDJCu9XZ9LrvqN5WIw4NIfu9hSS_GbLd1sbovM6_BRoXts6XejFUEw0peNSSwyVcPZxv293t1dl4pYxYB0VjSKtC5wPCWWdiMwMfFTLiHTQDJ9hl4GVxncirsRtlQQHzkyszgbq6kPc8sSZREgxXT0Rkxb2mfLH6KFVfV4PWVmFj0n3LSgwkfL9E3Olof55dXamjdJC4MTAVj80KQ4du-USt-TLcf9rmwdB7-wNOeq9TgBOPIWNw0qzJmrAy8XC5BRKSQr_v8hkreIXYHIH9vuaewV06Ma4nUOh56_te2DxccIH6zmURYM2uVf9uLWQViDYpI-Bw_eL3Gbl2LPIxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از دیدار دیروز ژوزف عون رئیس‌جمهور لبنان و دونالد ترامپ که نشان میدهد این دیدار خیلی دوستانه بود و دوطرف از این ملاقات رضایت کامل را داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136560" target="_blank">📅 10:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136559">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ebb0efc2d.mp4?token=NQAC1zzjGwDmE_SbdK2qUEATGmFD4aVYcLg7D9sXV0IzF6qaVeRWDuJGK8nbiybz2vsJC5U5JPDyXg9tbRedZon8XCAtmGg-w-V0dwxBsqVXqFQlvwjEUC8jtWuy7NadywRKckJkdVELkpM5FMmGTsBEpUo7svF7SViQuyPa9oOif4Qf4RdTbhDD-wSRowLc-ob9_6Uy-pjMuayojxr9-rNMhn398bxJvFX8T_Vrm-KFVTKoHfXkMr9bEReo9B7uM04CZOarHjOYlOtJixoI88aziYLHy-d3QDzW35mX6pbrYYjNK6-aSKGK0lND5JcNLd1yGGi-1uGyaSiaemPz9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ebb0efc2d.mp4?token=NQAC1zzjGwDmE_SbdK2qUEATGmFD4aVYcLg7D9sXV0IzF6qaVeRWDuJGK8nbiybz2vsJC5U5JPDyXg9tbRedZon8XCAtmGg-w-V0dwxBsqVXqFQlvwjEUC8jtWuy7NadywRKckJkdVELkpM5FMmGTsBEpUo7svF7SViQuyPa9oOif4Qf4RdTbhDD-wSRowLc-ob9_6Uy-pjMuayojxr9-rNMhn398bxJvFX8T_Vrm-KFVTKoHfXkMr9bEReo9B7uM04CZOarHjOYlOtJixoI88aziYLHy-d3QDzW35mX6pbrYYjNK6-aSKGK0lND5JcNLd1yGGi-1uGyaSiaemPz9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم سنتکام از حمله ارتش آمریکا به چند قایق در سواحل ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136559" target="_blank">📅 09:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136558">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
شبکه CNN گزارش داد که لاشه هواپیمای «پن‌ام ۵۲۶A» (Clipper Endeavor) پس از ۷۴ سال در بستر اقیانوس اطلس، در نزدیکی سواحل پورتوریکو، کشف شده است. این هواپیما در سال ۱۹۵۲ سقوط کرد و تمامی ۵۲ سرنشین آن جان باختند. این سانحه به‌عنوان یکی از نقاط عطف صنعت هوانوردی شناخته می‌شود و زمینه‌ساز اجباری شدن آموزش‌های ایمنی پیش از پرواز و بهبود دستورالعمل‌های اضطراری در پروازهای تجاری شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/136558" target="_blank">📅 09:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136557">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZJCKGdp6hiUhyM3EhfcMGLgbX6BzjuNdtIkopYXyeLM90mt7YLJQsaCkSDngO-YQKOtnInPS7s5L5oeC1vdob_6m2Kx6HApWojRAZBdz2DTumqMG_9SbLbNSElbSBzeQlxm-r2J2_KlnB0J7SHeees-OUgnv_hGsoxMiqII9SoFNREjtvFou4-g5ZtZKOZdxnaTLr9z2n5avLydBAEbUu71wI5xUKnh3s-1Y3xx6HErF0UQvRnx1d22A-sdRosnPLBz2w-hv3etS739yyLs5i0k0iZD66ISuyexM_VdXS6BT6bcdH3SGRaMu6RMRnljGv_Hc7FjvsfXqnf_cxGs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برآوردهای گلدمن ساکس نشان می‌دهد صادرات نفت منطقه به‌تدریج در حال کاهش وابستگی به تنگه هرمز است.
🔴
بر اساس این برآورد، در مقایسه با آغاز جنگ، روزانه حدود ۵ میلیون بشکه نفت بیشتر از طریق خطوط لوله و مسیرهای جایگزین منتقل می‌شود؛ روندی که نشان می‌دهد بخشی از صادرات نفت، تنگه هرمز را دور زده و از مسیرهای زمینی به بازارهای جهانی می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136557" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136556">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پست جدید دفتر شهرداری نیویورک: زهران ممدانی، شهردار نیویورک در این ویدیو تاکید میکند که نتانیاهو جنایتکار جنگیه و بمب های اسراییلی با پول های امریکایی ساخته می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/136556" target="_blank">📅 09:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136555">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ادارات هامون، زابل و نیمروز امروز ۲ ساعت زودتر تعطیل می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/136555" target="_blank">📅 09:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136554">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
روزنامه اصولگرا:  برای مقابله با جنگ زمینی احتمالی با امریکا، آموزش نظامی را شروع کنید.
🔴
لشکر جانفدایان را سازماندهی کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/136554" target="_blank">📅 09:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136553">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma0YLkfbtUpKya5q0cwN_vdgH6rlfX1Ll2Oa9aU9uwOnzmUYPSfT5njEnTVw1z7r5KIZarHH-xSJ8C1lE-YK-3swah5s670BWCOlATobvjl5nrjksxkNMnkluWhVlLthkBZrng4AXxVrTfM03zY1m7TCvmiwg9A5_p9t_iEeNMD_eg2jsZF0X91w2NzWGOeiK1T9d1Gok6t8LWLYJlGgeDR2rbx5v3NykLTePIqYH8klKQJQP3Zo9DqNNmUED8aBzvXScY8WsIkL8upNI8W-3T8HebdBsaWjEx04jB9K319bK3kCFfnE_Il9tWxf4hynIArNORrht6vJICvWjDHJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه حملات دیشب آمریکا به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/136553" target="_blank">📅 09:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136552">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29c9d9b51a.mp4?token=UF99OPSG6UegS4ZGKPC-s66u2buRsAwbQGuYODRC2AFgj_dscJO5v-UcApFC7UOEk1o0zscSmWv2_Ix5L6bH13XwQp01noInRPP5SiNPp8WEIJWtTicWZeBs6IqtnPVeZZVdZUi7SapDhI_JZqUD4m1b9Od4gzqjBbLMzSzx8J1vfbOxXRWf_ftZ5O3i_g2bssaLbOGS1SyBmX9FdDZDUZE0geB1vggqwwLi5n2H_LD3vDGzbPGjLXVxmM97zBgjdmKhpsyQCSlpH_-cuQPy6VPLyNyzOy1N-L_5S-TqaiC5GE4v5jwy9vHuuclk9gwyUs0ufvds7ZeNGNM5R_pEkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29c9d9b51a.mp4?token=UF99OPSG6UegS4ZGKPC-s66u2buRsAwbQGuYODRC2AFgj_dscJO5v-UcApFC7UOEk1o0zscSmWv2_Ix5L6bH13XwQp01noInRPP5SiNPp8WEIJWtTicWZeBs6IqtnPVeZZVdZUi7SapDhI_JZqUD4m1b9Od4gzqjBbLMzSzx8J1vfbOxXRWf_ftZ5O3i_g2bssaLbOGS1SyBmX9FdDZDUZE0geB1vggqwwLi5n2H_LD3vDGzbPGjLXVxmM97zBgjdmKhpsyQCSlpH_-cuQPy6VPLyNyzOy1N-L_5S-TqaiC5GE4v5jwy9vHuuclk9gwyUs0ufvds7ZeNGNM5R_pEkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید دفتر شهرداری نیویورک: زهران ممدانی، شهردار نیویورک در این ویدیو تاکید میکند که نتانیاهو جنایتکار جنگیه و بمب های اسراییلی با پول های امریکایی ساخته می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/136552" target="_blank">📅 09:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136551">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
خبرگزاری سی‌بی‌اس: هزینه واقعی جنگ در ایران بسیار بیشتر از مبلغی است که وزیر جنگ، بیت هیگز، اعلام کرده بود، یعنی 37.5 میلیارد دلار. این تخمین، هزینه‌هایی مانند ساخت و سازهای نظامی و تعمیرات پایگاه‌های آمریکایی که در اثر حملات ایران در طول جنگ آسیب دیده‌اند را شامل نمی‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/136551" target="_blank">📅 08:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136550">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835169113c.mp4?token=EWYy8s4Y86THTG7uYkE3z70t4Ygi8iq01k-8NWcJ9A6qOXOE0-6SvosQ5yayW8JaCEOZ--6AWZp6qJEhsb0VI5OcqjurjNQ45YZm5GJRaEHlfueN067Dgfrlg2Cd6KcdVVsZg6uZH8TbLyTEvHy0Q86Bxw4WBfaM8qUgGp16EwP9TPVYhc2DBhEEekRzBEPX5EeYqLSEMzFToe7DHAtrSopova6JX_E3NoFdf6q5xe7oMkgrWPnHBO6U7zYnbixEEuLXetUAYHO8wNOtPhlCiAht0yzYZuAz-OQpThLUlGd1Ey2VssB-f6f6R9FDu1xYXU_WPW2WpXsCmKXS8KRS9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835169113c.mp4?token=EWYy8s4Y86THTG7uYkE3z70t4Ygi8iq01k-8NWcJ9A6qOXOE0-6SvosQ5yayW8JaCEOZ--6AWZp6qJEhsb0VI5OcqjurjNQ45YZm5GJRaEHlfueN067Dgfrlg2Cd6KcdVVsZg6uZH8TbLyTEvHy0Q86Bxw4WBfaM8qUgGp16EwP9TPVYhc2DBhEEekRzBEPX5EeYqLSEMzFToe7DHAtrSopova6JX_E3NoFdf6q5xe7oMkgrWPnHBO6U7zYnbixEEuLXetUAYHO8wNOtPhlCiAht0yzYZuAz-OQpThLUlGd1Ey2VssB-f6f6R9FDu1xYXU_WPW2WpXsCmKXS8KRS9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور دموکرات، جان فتِرمن، درمورد قصد ممدانی شهردار نیویورک برای بازداشت نتانیاهو: او یک جوک تمام‌عیار است، هیچ اختیاری برای بازداشت نتانیاهو ندارد.
شما شهردار هستید، آقای [ممدانی].
زباله جمع کنید، چند گودال در جاده را تعمیر کنید، راه حلی برای مشکل مسکن در شهر خود پیدا کنید.
🔴
شما اصلاً در جایگاهی که فکر می‌کنید نیستید
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/136550" target="_blank">📅 08:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136549">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نشریه «وال استریت ژورنال» بامداد چهارشنبه به نقل از مقام‌های آمریکایی نوشت که ترامپ توافقنامه همکاری هسته‌ای غیرنظامی با عربستان سعودی به مدت ۳۰ سال و ارزش ده‌ها میلیارد دلار را امضا کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/136549" target="_blank">📅 08:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136548">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpSKUusXqLax1h6ImI221GKwBrGz-PrTmuX_NSuf2HdBLKrp-Mtjg6VQhXm1zq88CuQPu5R9l1J1BwRqcC-WYG6rlj8Kx0puT3lN_Rbq-cnFB87OFy8rXmoD8k5JZCOcskU_eiLBQo2A5gOAykQ7B34GRWMwiqmbda63QcB3dc59mk1BwIH7fQz06kr_iLibZmsGbfx-n8ex5tzPKoDLJ1XiFoXBcDrwULQ3TDzn2-3DEKA8so1mvnPqFxDHx0HeNI1eISTzL0UJSDmJUxgurgWS8sk6Vfhv7WrCneNKwkkXpGEG7nMBpwcljfhCU5sDE4MPAG1ULjgRWrlnzOqd4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد بیشتری از هواپیماهای آمریکایی مدل KC-135R/T که وظیفه سوخت‌رسانی هوایی را دارند، به سمت پایگاه‌های اسرائیلی در حال حرکت هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/136548" target="_blank">📅 08:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136547">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
انفجار در نهاوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/136547" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136546">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
انفجار در آبدانان
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/136546" target="_blank">📅 03:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136545">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
انفجار در ابهر زنجان
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/136545" target="_blank">📅 03:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136544">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
انفجار در الیگودرز لرستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/136544" target="_blank">📅 03:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136543">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سایت اتمی طالقان ۲ زو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/136543" target="_blank">📅 03:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136542">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
پدافند تاسیسات نظامی پارچین در شرق تهران شدیدا درحال فعالیته
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/136542" target="_blank">📅 03:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136541">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پدافند تاسیسات نظامی پارچین در شرق تهران شدیدا درحال فعالیته
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/136541" target="_blank">📅 03:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136538">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
جنگنده از آسمان قزوین رد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/136538" target="_blank">📅 03:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136537">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd3f23e865.mp4?token=N61KQxWuptSCRHqYtViNXT_KnCF5rGJirMm9xqzyAlxD7ihMhxTG5o5DqqoqpiP1F87bbInHn_jsTU-M4zX29Y0zyMxtocAzMQnol-SD_F1H9ttXvkH89k93PV2i9Rb0FQdB5dQsYnu70G9M6pu3YiNpMZLElEZRB2hlrgX3UulsvLUtWg9c75N09GTrIZYxTnBqAAhUHXs6IiaYI3jRvHTuN910ImQ-3fRZJJPUgPW00AUa1IUB8jyOM17FYDqZwu-C4RItqcbGTmQHUYhXT-Z_f_JkWT6mwBzg0Pg0ALkpdGcScRhj0sePijC5zQFlq6zrWYO7u7CrkAhKtJii2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd3f23e865.mp4?token=N61KQxWuptSCRHqYtViNXT_KnCF5rGJirMm9xqzyAlxD7ihMhxTG5o5DqqoqpiP1F87bbInHn_jsTU-M4zX29Y0zyMxtocAzMQnol-SD_F1H9ttXvkH89k93PV2i9Rb0FQdB5dQsYnu70G9M6pu3YiNpMZLElEZRB2hlrgX3UulsvLUtWg9c75N09GTrIZYxTnBqAAhUHXs6IiaYI3jRvHTuN910ImQ-3fRZJJPUgPW00AUa1IUB8jyOM17FYDqZwu-C4RItqcbGTmQHUYhXT-Z_f_JkWT6mwBzg0Pg0ALkpdGcScRhj0sePijC5zQFlq6zrWYO7u7CrkAhKtJii2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منتسب به ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/136537" target="_blank">📅 03:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136536">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
خوش چشم: آمریکا توان حمله به تهران رو نداره برای همین داره جنوب رو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/136536" target="_blank">📅 03:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136535">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
دقایقی قبل آمریکا نقطه‌ای در شهرستان کنگاور استان کرمانشاه را مورد حمله موشکی خود قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/136535" target="_blank">📅 03:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136534">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
پدافند کرج هم فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/136534" target="_blank">📅 03:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136533">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b55cc12d69.mp4?token=gviYY_gK99dzwuGMBQj3Cxq7My2xuDZP1aGJbz946cOlgCdcGKBM-NAOKuzuDcoHnWAy89XKlFsWGPIgyB-2Ii_lSZlYFuFtJ289QFCE_wvmxP7c8h-DlJhxjzp2X0eMPdYnp6jr8Ekzzl3FDoavLoau3uq8hB2pdRrdLd9jA3pH1-eQgXJwGvKDbiR3exDLcDZ36KhP0AtiS3BUfcDKKg3e3lU_ddNhdVIlaeK651gxHAXIy1Rn3WcGvxzpH3pZI9cJ1ElWfUTAvavSVzO-nqT61UNfGS1otctHOpnXIxPi-BJMWTOG-7jCH8by9g5AtkVxefJnWd2kSJaVObZMyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b55cc12d69.mp4?token=gviYY_gK99dzwuGMBQj3Cxq7My2xuDZP1aGJbz946cOlgCdcGKBM-NAOKuzuDcoHnWAy89XKlFsWGPIgyB-2Ii_lSZlYFuFtJ289QFCE_wvmxP7c8h-DlJhxjzp2X0eMPdYnp6jr8Ekzzl3FDoavLoau3uq8hB2pdRrdLd9jA3pH1-eQgXJwGvKDbiR3exDLcDZ36KhP0AtiS3BUfcDKKg3e3lU_ddNhdVIlaeK651gxHAXIy1Rn3WcGvxzpH3pZI9cJ1ElWfUTAvavSVzO-nqT61UNfGS1otctHOpnXIxPi-BJMWTOG-7jCH8by9g5AtkVxefJnWd2kSJaVObZMyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت شدید پدافند در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/136533" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136532">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
انفجار مجدد در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/alonews/136532" target="_blank">📅 03:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136530">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فووووری/پدافند تهران فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/alonews/136530" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136529">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b2530c00.mp4?token=MxbrCXxInQsF7cYi3Gu9fWEs127ikYOBZjFpHht4wli8Yr7JQQb6sv-R0Sjg23529sbf8uQVJEVVhOL5jDk5kqOLj-emB6UjZo6fC4FdDhj1BHGjYvYA4nT-htFIr3MZ6tmAiUtIomezPug4p_LWvFQfTyrc9ED_KHPNFir3201nYtvlhtSWY-MViiSPukr_m05qYKx4CSqXa3BmpM135yeFlIJJmbKU3pjPkucmtKhhfgdq018cP1AeE81vHOL7c_0iNV_iE0Pu3lYxsm4166-XUkH1mz6YYmT6G_ZnyAO0i8leDTXe5l5MoY3hKgLlvfQRHZ2T9T-TccDE39gnNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b2530c00.mp4?token=MxbrCXxInQsF7cYi3Gu9fWEs127ikYOBZjFpHht4wli8Yr7JQQb6sv-R0Sjg23529sbf8uQVJEVVhOL5jDk5kqOLj-emB6UjZo6fC4FdDhj1BHGjYvYA4nT-htFIr3MZ6tmAiUtIomezPug4p_LWvFQfTyrc9ED_KHPNFir3201nYtvlhtSWY-MViiSPukr_m05qYKx4CSqXa3BmpM135yeFlIJJmbKU3pjPkucmtKhhfgdq018cP1AeE81vHOL7c_0iNV_iE0Pu3lYxsm4166-XUkH1mz6YYmT6G_ZnyAO0i8leDTXe5l5MoY3hKgLlvfQRHZ2T9T-TccDE39gnNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حملات امشب تبریز :
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/alonews/136529" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136528">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
بوشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/136528" target="_blank">📅 02:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136527">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
همزمان جنوب و شمال غرب زیر حملات سنگینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/136527" target="_blank">📅 02:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136526">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
چندین انفجار سنگین در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/alonews/136526" target="_blank">📅 02:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136525">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری/انفجار در نارمک تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/alonews/136525" target="_blank">📅 02:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136524">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
انفجار در امیدیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/alonews/136524" target="_blank">📅 02:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136523">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/alonews/136523" target="_blank">📅 02:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136522">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/alonews/136522" target="_blank">📅 02:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136520">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری/انفجار در نارمک تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/alonews/136520" target="_blank">📅 02:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136519">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تهرانیا تایید؟
👍
👎</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/alonews/136519" target="_blank">📅 02:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136518">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری/انفجار در نارمک تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/136518" target="_blank">📅 02:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136517">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWsBvTtqe2iQn3VWCqhZqOut74Yhz4wH_MWsOsmJRnu7NM_GZquu5JgDOc_VRCKIea_uY7p_07vk5-6fdr6K0a7theLGZWuqxgca6EYyPhHsihkvqyPwA4XckHfQn1bHi3ykA5fhQnljnKhwEvQS9GOzH4r13mGPV7FujspSUiffrO_W22uNzMoI7IWPd_nPHNpuRSzGU8jS4mbVxPzQcrI50l29MTBcfVi948s8hjnIM65GAfwT2P-XVKXgx2gC-VSKfkYsvjwDC8PA5xt8dnzik5MYhUgA-c7HEqL5OgUnINwRLQnX1eDwwFdHshmlWgWtwbHTWMP1J2TVL6jOoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست:
ترامپ، می‌خواهد اینفانتینو (رئیس فیفا)، دبیرکل بعدی سازمان‌ملل متحد شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/136517" target="_blank">📅 02:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136516">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
خبرنگار:
آیا فکر می‌کنید ایران با تهدید به بستن یا تحت تأثیر قرار دادن تنگه هرمز، تلاش دارد بر انتخابات میان‌دوره‌ای آمریکا تأثیر بگذارد؟
🔴
ترامپ: «
احتمالاً
. اما آنها هیچ تأثیری بر من نخواهند داشت. من فقط کاری را انجام خواهم داد که درست است. من به این موضوع با این دید نگاه نمی‌کنم که "اوه، ما در آستانه انتخابات هستیم." فکر می‌کنم مردم بسیار تحت تأثیر قرار گرفته‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/alonews/136516" target="_blank">📅 01:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136515">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">استوری دنیا جهانبخت از حضور در مراسم عزاداری.  وقتش شد یادی کنیم از ..... زدن دنیا خانوم جهانبخت برای تتلو
😂
😂
😂
◀️
◀️
مشاهده فیلم</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/136515" target="_blank">📅 01:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136514">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/136514" target="_blank">📅 01:30 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
