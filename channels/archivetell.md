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
<img src="https://cdn4.telesco.pe/file/SAXMoVtsV5vR8Mog_ilzAdmm--ujVL-CFGa14rQ3HeKF_xndggELlVFR2poMfLXUaQwW-KXF4Pj5nozdcBGlPcmbHltWBzYyjZ0ntuwc0lO6gw9Ro2CyBUehzORSYrpgO-BAKYKoNKYFtZv59lHR-d5xjs51a15wGQs_GEixklfEikEyc4HkaWJ5_hqbL5oF4OZQO7N-aB8Y1GEot1NVP2ZRuyOgVAsCrSLPzayCxckdBELFjoh2C3E8Jji13afu1T-p3l-cGXapQueKwZldNz40cHDtfKwAdx0ZegYeDLDmOjMVs0n3xX3wyQx3oXos9utSefgOyfKezXRsR7b3QA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.6K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 10:53:40</div>
<hr>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3JZIRE1RLVNckL6I-n5IL6alp26IFY-954mTQtCRQVd54Bil_vddMkNUggHrSX3PL71GuWo66xgYagjovoPmgAh5tiSmbJmZkSJJFiD05CWBy8tpWoKeJbKUYhMD0kvd6M6Nvh3M9K-0CfNuxr6CMPgkf68w9XTnhUTrwEMgjOJTEe_edYCHbDMcBF8nqC_ItDoNyEcqsrYPquJ0a78Rvwlu8BWm2FP3_nvp0v6wTIPj9wVw3Z9F8jc22MtXDyfOrA4liKyweszCsss_OFV41NXsBwDQjteNxhjBJ1TI_smhgFEGHyf1iKsKh6fXfZr6ZWotfjyKYkCT913AwJabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
BrowseryTools
مرورگر خود را به یک جعبه‌ابزار قدرتمند تبدیل کنید! 136 ابزار رایگان برای فایل، رسانه و هوش مصنوعی، همه در سمت کلاینت.
✨
قابلیت‌ها:
•
🔹
ویرایش تصویر و ویدئو بدون نصب
•
⚡
مبدل‌های فایل سریع و آنلاین
•
🛠️
ابزارهای توسعه‌دهنده با Next.js + TypeScript
•
📦
هوش مصنوعی محلی: رونویسی، ترجمه، حذف پس‌زمینه با Transformers.js
•
🌐
متن‌باز و قابل میزبانی مستقل
🔗
لینک:
https://github.com/aghyad97/browserytools
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 260 · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=rsnFdIbQ7EdUW4SriP8UxysERPj82vv61oCmIWG49QZiZLpzKYH9PphtVFC9gImmtZQ_gjg5YtNQrDid1Gno8e9SaN68DCjw-qt2u1IDRxDxRDD3CX_KwqIhw42iANtE5QyuQNZ7xGsfKw9npQaRwjXG9blSkeoUg_X3o23-SvY8xe4suXf2fohJ9vPZY0f25nuwWZDYclSG1x1Dp8qyxm26ckyrxf40eiDBGbRvrn88POlIr9jPoPB5jDMS7OUuZCCfqErO2AwAAtKLA42vgwqjpTJ8Jls-Qnpgk21Ib5pNLxEdwrTZtuiQg4BSm_Z6l39KMA6aUerd2h48NgKV0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=rsnFdIbQ7EdUW4SriP8UxysERPj82vv61oCmIWG49QZiZLpzKYH9PphtVFC9gImmtZQ_gjg5YtNQrDid1Gno8e9SaN68DCjw-qt2u1IDRxDxRDD3CX_KwqIhw42iANtE5QyuQNZ7xGsfKw9npQaRwjXG9blSkeoUg_X3o23-SvY8xe4suXf2fohJ9vPZY0f25nuwWZDYclSG1x1Dp8qyxm26ckyrxf40eiDBGbRvrn88POlIr9jPoPB5jDMS7OUuZCCfqErO2AwAAtKLA42vgwqjpTJ8Jls-Qnpgk21Ib5pNLxEdwrTZtuiQg4BSm_Z6l39KMA6aUerd2h48NgKV0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه ImageToPrompt تصویر شما را در چند ثانیه تحلیل می‌کنه و یک پرامپت آماده برای مدل‌های تولید تصویر می‌سازه.
✨
قابلیت‌ها:
•
🔹
تشخیص سبک، اشیاء، نورپردازی و ترکیب‌بندی
•
⚡
تولید پرامپت دقیق برای Stable Diffusion، DALL‑E و …
•
🛠️
بدون نیاز به ثبت‌نام یا حساب کاربری
🔗
لینک:
https://chromewebstore.google.com/detail/ImageToPrompt/pgabcjhpgdcgbflabemecpficpknnpfn
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 559 · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt-H7owtya1EUVM7_UiAaPX2d2OqGoT4UhBE5bHw5A14XnuKlIdtORwtiZfGK8Vt2k-tQac_N1Wd_rtFAY2TyKM1UfDPc6mB7F5Tnu2X3Sv5zVYFpDalkc36WPujM5OIrCQIcdVhlLaLuQW8skDuFzdWlZoGFFU6LuxshLN8v-se8MdTl4cm3IbXVNaSb2I51wHJVbvshxZpk0La5ihWJvIRkrFoSmcIsG8pjP1UeosjYz3Xr0eO8aBuAbvJlQ3XMLiXMR8nVH8tLjK_Roc4jnWxFALvClVXyJ8bxVxbmvo5MCLqg0dVvFE4SVjB9VrL5UwAH3QnphBBwQCzqKgErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتقال فایل سریع و پایدار بین دستگاه‌ها با قابلیت ادامه‌دادن پس از قطع
✨
قابلیت‌ها:
•
🔹
انتقال همزمان بین چند دستگاه
•
⚡
ادامه‌دادن خودکار پس از قطع ارتباط
•
🛠️
سازگاری با شبکه‌های پیچیده و متغیر
•
📦
انتقال تطبیقی برای بهینه‌سازی سرعت
🔗
https://shrimpsend.com
دانلود فایل مخصوص ویندوز ، مک و اندروید :
https://github.com/shrimpsend/shrimpsend/releases
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zj1RpKtqk7sKEcEi0Y1GtATFdk2JNaoXaDHJkGN6-yj7ogeqR1UKa8pRxzxqgtsmhc_4V3NmmA48eCzpd3HIDyrOYZutbXFJg4-gMbbLMIgIPQUrpNcjPvHk8islQlqn6vAN9Hlw_-Hw3ehfY3GcmQ2ftRtTcPe9aP9BzdN3QZ3FrFIG4sJ6wUJc4ggKrMZ9NamUZWsOxqakiH-YFgbgoRmyqczvr1AueMG_FMUzKKRGXqzgrniUlzX_mrTWA3bx1JfRxU9JA1dyIn6VEQnavL9YUkFgtxNcnHqRi7xFFxQmOSjmIwYX44C_nJLsUtgof_ol_d4VD8vYVwO01RyXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=M7joD3iLYAe3PIyECkM94VFXkC4YiqpSn57lp64O1tXz-Hu-ieTnCGvGh0FW6ZAGqFxxNKPN5jU3GY79CgNH9JnykNfhFG1Ch6kyuNTRfB5rp5505z5EC3peRacLNDdtGhWbijfxipI3Oh9K2E5iUaoqeHgNeg9QCAVWGRP73_BF6i_dYEOilJLH06oPGalqbXZ86C651u9_IuLDbKR-jCber0_jxMRmwEbe5E57rqurj0-nBWStpJ-CYOFvAi07Oxwl396GQ9XadLfu5S0BTEH0bkr8CAzQ-0vRMfwhIdHTHmtfrMsFWLYwmyR4yzJGd_yBQBvui1emGymHNnjfKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=M7joD3iLYAe3PIyECkM94VFXkC4YiqpSn57lp64O1tXz-Hu-ieTnCGvGh0FW6ZAGqFxxNKPN5jU3GY79CgNH9JnykNfhFG1Ch6kyuNTRfB5rp5505z5EC3peRacLNDdtGhWbijfxipI3Oh9K2E5iUaoqeHgNeg9QCAVWGRP73_BF6i_dYEOilJLH06oPGalqbXZ86C651u9_IuLDbKR-jCber0_jxMRmwEbe5E57rqurj0-nBWStpJ-CYOFvAi07Oxwl396GQ9XadLfu5S0BTEH0bkr8CAzQ-0vRMfwhIdHTHmtfrMsFWLYwmyR4yzJGd_yBQBvui1emGymHNnjfKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=vjbR-2-tOp4Evu3Dk2w0q0_961WyAAaikaR7_FADGd-L4REhmtNCWhynKFsDYO7Q6TTLpy0nAieg-av4xJI3JgCNj1MFE_uBO8-wq8MdSvHullpOSn55r-nR0HXqRW5JjiTOwo08K8xgQQI0kpyT_eu5591NMR8mYyJkZgW-znM__FaLZ7wJ_PqVyJvvcJdeDI5ifdnoxu1sUizZxAboylB_OS3_TT8SqH5-PO5Ss6_cugZGqjebeMFxDeQL_tNL8bbUSq8xi6CAMZcq0AFIaKhzAFsBeRgyRPf0Z21qmio4GTSh0fbiIZL3O-0PvAinJnyXQXMk_hQVnZ6c_8Kg_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=vjbR-2-tOp4Evu3Dk2w0q0_961WyAAaikaR7_FADGd-L4REhmtNCWhynKFsDYO7Q6TTLpy0nAieg-av4xJI3JgCNj1MFE_uBO8-wq8MdSvHullpOSn55r-nR0HXqRW5JjiTOwo08K8xgQQI0kpyT_eu5591NMR8mYyJkZgW-znM__FaLZ7wJ_PqVyJvvcJdeDI5ifdnoxu1sUizZxAboylB_OS3_TT8SqH5-PO5Ss6_cugZGqjebeMFxDeQL_tNL8bbUSq8xi6CAMZcq0AFIaKhzAFsBeRgyRPf0Z21qmio4GTSh0fbiIZL3O-0PvAinJnyXQXMk_hQVnZ6c_8Kg_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=vH9mjPR-TF2xhBSOMOxTJNKSlXB-4CAklw-c18gQ0Dims--dy8-mD03ekDzbDBDacHMl-PdndFrY8Nj01Ts9odYPWMxhLBemxMHj202WUGNQNMhoKD8PTtVwR34rzzfVLilUgVTXGFZmEg0bZsRoyPAWm2kmWN5b9e0W18xjDl2_epw-lcjGUtw94UrhBXqjmhAXpqO7QxM44MivOJ9pDpBWi3NYq0vfsNSjtt-tNgR1NsX8PW0ajUdiEIZKDQLhzW2P9KfO3ym5rxMN4YfWpcRA6-nXLoGQdnIn4JLG5_iGznJdZZB8b5F2SE65OyS5SoPbT-jUZjDxlfQ2GYKJMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=vH9mjPR-TF2xhBSOMOxTJNKSlXB-4CAklw-c18gQ0Dims--dy8-mD03ekDzbDBDacHMl-PdndFrY8Nj01Ts9odYPWMxhLBemxMHj202WUGNQNMhoKD8PTtVwR34rzzfVLilUgVTXGFZmEg0bZsRoyPAWm2kmWN5b9e0W18xjDl2_epw-lcjGUtw94UrhBXqjmhAXpqO7QxM44MivOJ9pDpBWi3NYq0vfsNSjtt-tNgR1NsX8PW0ajUdiEIZKDQLhzW2P9KfO3ym5rxMN4YfWpcRA6-nXLoGQdnIn4JLG5_iGznJdZZB8b5F2SE65OyS5SoPbT-jUZjDxlfQ2GYKJMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📝
جنجال جدید در دنیای آفیس‌های متن‌باز
پروژه
Euro-Office
نسخه 1.0 خودش رو به‌عنوان یک جایگزین اروپایی و متن‌باز برای Microsoft Office منتشر کرده، اما این ادعا با واکنش تند تیم
LibreOffice
روبه‌رو شده است
😬
🔹
بنیاد LibreOffice می‌گوید Euro-Office خودش را «اولین مجموعه آفیس متن‌باز اروپایی» معرفی کرده، در حالی که LibreOffice سال‌هاست چنین جایگاهی دارد.
🔹
همچنین توسعه‌دهندگان LibreOffice معتقدند تمرکز Euro-Office روی سازگاری کامل با فرمت‌های مایکروسافت، عملاً آن را به یک «هم‌پیمان غیرمستقیم مایکروسافت» تبدیل کرده است.
⚡️
به نظر می‌رسد رقابت بین پروژه‌های متن‌باز برای جذب کاربران و سازمان‌های اروپایی وارد مرحله جدیدی شده است.
#OpenSource
#LibreOffice
#MicrosoftOffice
#EuroOffice
🐧
📄
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vd3Q-rfJ1nF9r576pgTVYoC5FHApl9FZ4RNrNC3mSplLfB3leQNGUy4W_f4pYhRMguY00501K3ypEJ7a399vyLuwcjUSqkh9TZ5KstcwgDWkvec0LFYlzYKHv1u00qwbWUvPm3w6AVws-FXRaNooWW47ozW6tK9R9jZF1Kd0QIAhx7kwWAXwzcZKfrUqJjyNSrMbcBabTI3sEzlKIR0VSHW3JreCClRXWVP6x9sSaauSNQ2revQjoLK-PppMTRhjvTiSojF27l18GaMt9hPwtFV69uuT7DsMfmMZTba6pnV7uYkzNEcH_nu0-e7ixz6ZdxbwabpU3DJgTOuQi2_fQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ZOOOP: همه ابزارهای خلاقیت هوش مصنوعی در یک پلتفرم!
🎨
🤖
✨
قابلیت‌ها:
•
🔹
تولید تصویر، ویدئو و صدا با یک کلیک
•
⚡
کلون حرکتی برای انیمیشن‌های دقیق
•
🛠️
قالب‌ها و مدل‌های محبوب پیش‌ساخته
•
📦
یکپارچه‌سازی ساده و سریع
🔗
لینک:
https://zooop.ai
#OpenSource
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6266" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti3L8onMtqznfhME7Ut5wv_465syR7o0kyXgSmA506xCGaKdRRMLdI0nBz5PWLByeMBoiT12fSb9q2DO1tuHKhRNhyqiOUowWHjYL36xzy3vte2x05ZktCR8SaLJBvI5ANVLpLVL97gBPQih7gs4cmPxi6y3zQoWQG5HsXCNpt4wkQPjayAP3SUwBfXpvqNiC6Wth9n0UW_Z6fr4Ms9MOwlbQTs4sHFyL_BiPesB7iNP4T-9ZtnUGPER58PMsFVhd-hRvdlIvYt8GeQPjs3PQY8ut81CZZjQcZflg7ciRNclXm3tRFzE0Ya6V9YL6FO1QtmB1DiWedm9SocLjuFaLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵🏻‍♂️
با این ابزار می‌تونید فقط با وارد کردن یک نام کاربری، حضور احتمالی اون رو در سایت‌ها و پلتفرم‌های مختلف بررسی کنید.
✨
قابلیت‌ها:
• جست‌وجوی خودکار در صدها سایت
• بررسی شبکه‌های اجتماعی، انجمن‌ها، پلتفرم‌های بازی و سرویس‌های دیگر
• نمایش تطابق‌های پیدا شده در یک فهرست
• اجرا مستقیم داخل مرورگر، بدون نصب برنامه
• امکانات پایه رایگان
🔗
لینک:
https://whatsmynameapp.net/
#AI
#OSINT
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
😳
⏳
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 46 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/6264" target="_blank">📅 18:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6263">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=aAsErgm01zKu-5MV1JQGtwTYx4WT5spG-nbp69rf6qdSIeArb8lrNHrJoVXkmVQ5QWpnIgZ_yDkqegKK8uiKvSVlT3xZExrCPMx1eQetWfdnhDFV1mCPx_EmZGPPrV63ZVzqTdu_3jJn4uVHJe-xWO_HYe6fAJNzV3zYEMDF4kUsmnPX0LJV4Dk0FxflQowp7yNdfTkcKXiEoqDbWutjk0M75kXKKjsBQvnMqc8g8pxz0n7T2P1It2TUzh_L6Ts-Gba4-9pwsht542dhpcuzKVg8ve0wkN5BK1_YqzZJNR62Uv6_wqAiPsKpxU32mN7s5BDJ8u-QcRNsxk6mPFlacoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=aAsErgm01zKu-5MV1JQGtwTYx4WT5spG-nbp69rf6qdSIeArb8lrNHrJoVXkmVQ5QWpnIgZ_yDkqegKK8uiKvSVlT3xZExrCPMx1eQetWfdnhDFV1mCPx_EmZGPPrV63ZVzqTdu_3jJn4uVHJe-xWO_HYe6fAJNzV3zYEMDF4kUsmnPX0LJV4Dk0FxflQowp7yNdfTkcKXiEoqDbWutjk0M75kXKKjsBQvnMqc8g8pxz0n7T2P1It2TUzh_L6Ts-Gba4-9pwsht542dhpcuzKVg8ve0wkN5BK1_YqzZJNR62Uv6_wqAiPsKpxU32mN7s5BDJ8u-QcRNsxk6mPFlacoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تست رایگان Battlefield 6 در استیم شروع شد؛ تا ۱۵ ژوئن می‌توانید این شوتر را بدون پرداخت هزینه تجربه کنید.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان محدود تا ۱۵ ژوئن
•
⚡
شامل ۵ حالت بازی مختلف
•
🛠️
تجربه ۴ نقشه چندنفره
•
🗺️
بازگشت نقشه‌های کلاسیک مثل بازار قاهره از BF3 و جاده گولماد از BF4
🔗
لینک:
https://store.steampowered.com/app/3028330/Battlefield_REDSEC/
#Battlefield
#Gaming
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6263" target="_blank">📅 18:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سیستم جدیدی به
ربات
افزوده شد.
✨
از این پس، در بخش
سرویس‌های هوشمند >> آخرین اخبار
، امکان دریافت اخبار روز ایران و جهان فراهم شده است
📰
🌍
هر دو ساعت اخبار بروزرسانی خواهد شد
✅</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🦀
Asterinas 0.18 منتشر شد
پروژه Asterinas یکی از جاه‌طلبانه‌ترین پروژه‌های متن‌باز دنیای سیستم‌عامل‌هاست؛ یک جایگزین مدرن برای لینوکس که تقریباً به‌طور کامل با Rust نوشته شده و روی امنیت حافظه، کارایی بالا و سازگاری با اکوسیستم لینوکس تمرکز دارد.
در نسخه 0.18 تمرکز ویژه‌ای روی اجرای Asterinas در محیط‌های کانتینری و مجازی‌سازی بوده و قابلیت‌هایی مانند Namespaces، cgroups و بهبودهای مختلف VirtIO به آن اضافه شده‌اند.
از دیگر تغییرات مهم:
🔹
درایور جدید NVMe
🔹
بازنویسی درایور فایل‌سیستم EXT2
🔹
پشتیبانی بهتر از نرم‌افزارهای لینوکسی
🔹
اجرای برنامه‌هایی مانند Firefox، QEMU و Codex
اگرچه Asterinas هنوز فاصله زیادی تا جایگزینی کامل لینوکس دارد، اما یکی از جدی‌ترین تلاش‌ها برای ساخت یک سیستم‌عامل مدرن، امن و سازگار با لینوکس بر پایه Rust محسوب می‌شود.
#Linux
#Rust
#OpenSource
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کانفیگ ناب
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORuBXwe-J16xa7HCazeuE0Gb0DkvgxABWBbAIVOrY_KVgD4EmgTdTjRcRuCuLHNHBaFOLQ9dl1zYCy1w9kXR4dq_zMDWPM5xxBXqivTbjHHiEhyDvg6khGKn9Ekr9IgKsw_i7whKzx1PoYeku0qomvmtl7wRLdESbPPQZB_QIVb5XfUbhYCaof5tD8RxnOCP6sAMVlnhW9cjL7I5aGNKI9CuH2VjS6tn4vTaqlSS7C-Orc8yFxY58Ip7Wh3Go-yb5Qe_6HY6zxnanvohPvpwpzFczVROPK99Gg-i-y7_OHF7C2CxQnFJuYq2FnycF7tx-El_g4TawfPa24Ri9FTfmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
یک ویرایشگر ویدیوی رایگان که مستقیم داخل مرورگر اجرا می‌شود و فایل‌هایتان را روی کامپیوتر خودتان پردازش می‌کند؛ بدون آپلود در فضای ابری.
✨
قابلیت‌ها:
•
🔹
ویرایش چندمسیره ویدیو
•
📝
انیمیشن متن برای ساخت محتوای حرفه‌ای
•
🎧
افکت‌های صوتی کاربردی
•
🎨
تصحیح رنگ و بهبود تصویر
•
📦
خروجی با کیفیت 4K
•
🌐
اجرا در Chrome و Edge بدون نصب نرم‌افزار سنگین
🔗
لینک:
https://github.com/Augani/openreel-video
#VideoEditing
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6259" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=vhDR2xLiIAyQeZvmKRzPa7UDK2CKWj8Aib_NhXnN0o3qVE4EocXfGYGVvM4TXZ0mvGpP6Xgw4ojJQq74-RMKrtfEsAnX-qybzgBWINtKgIpPGvlHZiqPUY3Ijx7Sfh4L_1fgSSb3LHypXwVlFIrEhIMMjL2Z2OZzdSevDFwUlE75DySu84Aw83EsMlMBafgKO3JRHvcLaIKnDcnx3T2lhuDWJQVqotteIbkT8EqqCM6YdC9fntvkRJhY3hy_4HFfR9Q8Jc1M0dmy7OL01UyhuATftHx5q8nW7NjJD8seepm-Uy1r_5RocXB2s5hSWgdMrQ5uwrLRBH3fZV2QXRLOD6MJEipYUm-a3LmKponQtMz8sNVoyKMZ0rXa_mP00dT_tyXWrpnBgQUiWgg6u6ablNS1mmXRQ2miZqpcHRTmMiAU1FPpVocNovXcKx5W9Sk4wP_R_QbiA9oCuixf-l0bs-eEYjFETC66Z7wBCRy_4wT5HYlLYVWo_fc-r3Wd1c0GsRCqucNua_q3OgA_BSH_Y9Omcm3DZI2z7TZKh4NLtzfmjtjWvZHp05Bm93puix5UrT6vg9WoDWA6Jwsw8oTLKtG59WdeSdvyDv50n26rS_-J9UJG0drexGJ3EY3koJzSpzq_spKxAKQBG2_22CKxwgeC8pM5gzorwQytPlkJYAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=vhDR2xLiIAyQeZvmKRzPa7UDK2CKWj8Aib_NhXnN0o3qVE4EocXfGYGVvM4TXZ0mvGpP6Xgw4ojJQq74-RMKrtfEsAnX-qybzgBWINtKgIpPGvlHZiqPUY3Ijx7Sfh4L_1fgSSb3LHypXwVlFIrEhIMMjL2Z2OZzdSevDFwUlE75DySu84Aw83EsMlMBafgKO3JRHvcLaIKnDcnx3T2lhuDWJQVqotteIbkT8EqqCM6YdC9fntvkRJhY3hy_4HFfR9Q8Jc1M0dmy7OL01UyhuATftHx5q8nW7NjJD8seepm-Uy1r_5RocXB2s5hSWgdMrQ5uwrLRBH3fZV2QXRLOD6MJEipYUm-a3LmKponQtMz8sNVoyKMZ0rXa_mP00dT_tyXWrpnBgQUiWgg6u6ablNS1mmXRQ2miZqpcHRTmMiAU1FPpVocNovXcKx5W9Sk4wP_R_QbiA9oCuixf-l0bs-eEYjFETC66Z7wBCRy_4wT5HYlLYVWo_fc-r3Wd1c0GsRCqucNua_q3OgA_BSH_Y9Omcm3DZI2z7TZKh4NLtzfmjtjWvZHp05Bm93puix5UrT6vg9WoDWA6Jwsw8oTLKtG59WdeSdvyDv50n26rS_-J9UJG0drexGJ3EY3koJzSpzq_spKxAKQBG2_22CKxwgeC8pM5gzorwQytPlkJYAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
نسخه ۳.۲ مدل Ray از Luma منتشر شد؛ اما طبق تست‌های اولیه، هنوز با رقبایی مثل Seedance فاصله قابل‌توجهی دارد.
✨
نکات مهم:
•
🔹
پشتیبانی احتمالی از خروجی HDR با فرمت EXR 16-bit
•
⚡
تولید ویدیو تا ۱۰ ثانیه
•
🛠️
ساخت ویدیو بدون صدا
•
📦
ضعف در بافت‌ها، انسجام تصویر، دینامیک حرکت و درک پرامپت
🔗
لینک:
https://lumalabs.ai/ray3-2
#AI
#VideoGeneration
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6258" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXtKQhnxRD8XVMu8l_voWIe9zwAxDyqzTHNyzWwxCHhLVmFycZ6q5lmh5odFKSTih30pwaVMLbr62JEXxtkHGNzCid0X9YtTlz4w36rBUJ2CamEK86KMVZvzJhO4WcX6JFPfMwD-BAF4PmBL0ZUoH0ngTVDmTSjjuLWkxgOaurgpkttjBpXY-Y6YiUrtdICVKjoz-fAV3IJsQ2DHdbzsA0AIGR9h4CXgNfbzYKLULQGf9-jdiA7zuGkmQ_7capR8E0siKhXoIwRo99aqrX_l8KNtj2j5XqiUzokSz0dOo90_T7wpl-cM_XI1AIVUFT1Cuume8_OL79LfAsxd3-lPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qw-6QvIwCSddFZxxS1CKgRjxrpGKMd6o1JNQwsUiI0xpBmthzd1NeqwqHK7uPfri2PxP_badByrocjJJUOd8i_AdeFMEU1sXvBG1Uqm3f7LBGS_4cCxJem6PM_MXUrZqiBmBdokMd-5E09kgWcV8lX03xJvUbi50RdnnmMWO-AcCKMb4eHgdWLCuVpAUnrE_sJZy_HBndxoWEZNf_lUO9fgdNlIgXYmIxwDT-3w9r-rh0ZBCxStVIVJsac42Lk0XJr7bOMLAQH0_yAYpAMm8J9QAqTM0AL72VSnKXy-UYzQcNBE97vFiRQuCi4ygEEl8kJm_fLFSRSfVhvZbm0FTcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
CodeWhale
یک عامل ترمینال رایگان و متن‌باز برای کدنویسی با DeepSeek و مدل‌های محلی است.
✨
قابلیت‌ها:
•
🔹
خواندن و ویرایش فایل‌ها داخل ترمینال
•
⚡
اجرای دستورها و کار مستقیم با Git
•
🧠
حفظ زمینه بین جلسات کاری
•
🛠️
پشتیبانی از MCP، مهارت‌ها و ابزارهای اضافه
•
📦
اجرا با DeepSeek، OpenRouter یا Ollama
نصب سریع:
npm install -g codewhale
🔗
لینک:
https://github.com/Hmbown/CodeWhale
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6256" target="_blank">📅 15:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آپدیت جدید
ربات وگا
انجام شد
✨
- اضافه شدن GPT-5.4
🚀
- اضافه شدن Gemini 2.5
⚡️
- اضافه شدن Flux 2 Kelvin
🌡️
- جایگزینی Lucid Origin با Flux 2 در گروه ها
🔄
- حل مشکل هنگ کردن Gemini 3
✅
- رفع سایر مشکلات
🔧
>
آموزش گرفتن API رایگان GPT-5.5
<
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6255" target="_blank">📅 13:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">💵
گوگل اشتراک AI Plus را ارزان‌تر کرد؛ حالا فقط ۴.۹۹ دلار در ماه با ۴۰۰ گیگابایت فضای ابری.
✨
قابلیت‌ها:
•
🔹
دسترسی پیشرفته به Gemini 3.1 Pro
•
🧠
Deep Research برای موضوعات حجیم
•
📒
NotebookLM برای تحلیل و ساخت پادکست
•
🎬
تولید ویدئو با Gemini و Flow
•
☁️
۴۰۰ گیگابایت برای Gmail، Drive و Photos
🔗
لینک:
https://gemini.google.com/app
#AI
#Google
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6254" target="_blank">📅 13:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📱
اگه حافظه آیفونت زود پر میشه، iMole می‌تونه حسابی به کارت بیاد.
🔍
این ابزار فضای ذخیره‌سازی آیفون رو بررسی می‌کنه و دقیقاً نشون میده کدوم برنامه‌ها و فایل‌ها بیشترین فضا رو اشغال کرده‌اند.
☁️
از بکاپ‌گیری افزایشی هم پشتیبانی می‌کنه و می‌تونه داده‌ها رو با بیش از ۷۰ سرویس ابری مختلف همگام‌سازی کنه. بعد از اطمینان از سلامت بکاپ، فایل‌های اضافی رو هم پاک می‌کنه.
💻
روی ویندوز، لینوکس و مک اجرا میشه و خروجی JSON هم داره که برای ابزارهای هوش مصنوعی و اتوماسیون کاربردیه.
🛠️
پروژه کاملاً متن‌باز و مناسب کاربرهای حرفه‌ای و علاقه‌مندان به CLI است.
https://github.com/chenhg5/imole
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6253" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید  اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6252" target="_blank">📅 10:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRlQTJCDzKoA8vvA-lqT_MCRZOy8GCcCYPiWZammT8R2Wf1d2LC5zVD8UsrU6h0h4aSrjILUVQtd7PobaGM0WaBy9hUS-IEhJE4HBKd8-nB8R39BVLp_4PKN450aKwvIrIWzsVh0hXt9zM5Q_uOd8B12i2iFVIVGPb94qiUgcitaOhzpXdIwaYFgDP1cX17FQGn0iO7_xoQjIHQc8xNhZzB5wzetz6TgnAio12fkHKBUf7klfKlTW1XH6UjDVIgy8bqA54g0q_0t5LQ41kXopIU9Q3YEznhYJ26JmslOpNELljzle-x22yzbhTc7IDXwoTm7HR95oSvQ6sN0VBeGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Unlimited hotspot shield vpn method! |  7 days trial
/gen 415464440062
trail→
https://get.hotspotshield.com/trial
zip → 1216
Browser any
Ip usa
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6251" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC55KiMytWwyDVfL23Axh5yE26vav6b6oFjR-GXf1qw3YoEkx1M5ju1fSkAOQczPv3Gv90nvPWg4DR_9hGd7IZEgDn8WQB2xySqfV467vrhEL_CrMy6G6N0fwUKZK4qJEbFXhG_W_lVQT-4Av91prFg3SYwoqdkvEY-We0QRBVAKEOz_H1nMc_z6d0BsNowgW4_I8XBx6AtOSSsVziZfjQ8z37i-DVurBBwKlqN9RCaw0E9Z5cm3Z-OxbHRiGiHGOAakGsYRsinak9OLPSuKvCOd4wYfuj4SbM1mKvjUGjHw_mrOQAh1GlVuUcmP9ON50NhzAIEKBsLAJ6kq_XAJ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با «تحقیقات عمیق محلی» می‌توانید پژوهش‌های محرمانه را روی سیستم خودتان انجام دهید؛ رایگان و متن‌باز.
✨
قابلیت‌ها:
•
🔹
جستجوی خودکار در وب و منابع علمی
•
⚡
پشتیبانی از arXiv و PubMed
•
🛠️
کار با مدل‌های زبانی مثل Ollama و GPT
•
📄
بررسی اسناد شخصی و محلی شما
•
📚
تولید گزارش نهایی همراه با ارجاعات
🔗
لینک:
https://github.com/LearningCircuit/local-deep-research
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/6250" target="_blank">📅 10:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYwUESMbdwm9uPDamhLlPVF-y74TwY18J0X5B-WB5pMkV-y219pty-_59Sf6hVZu15Ra-3Uco0IuqgcPwiGH9XwZt4roY-inrNa-ZKXxIDNpDpXG6mV0gl8H0qc7Mj0xiCZei519k-qOEsxcqi_vqQTavFn9vscxA5gJl25BxfTbxis7CNv0pMN0XBdCuKEAmo55hN8-hS8eT3tduRdBxCOGfKKL_PSNsCy4GLIPLBp6qRRLwct1Vv8fvXnycpXDQVmlEOlQNq4NRh4yyN_LCj1_nfefbpFTlhd6sOnHjr8uu7BHuCQ3qgnZGrDRrWkwEhiOZcivcZkTsuw-CuiwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید
اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت Split Tunnel برای انتخاب برنامه‌هایی که از VPN استفاده می‌کنن
🔹
پشتیبانی از پروفایل‌ها و سابسکریپشن‌ها
🔹
متن‌باز و رایگان
جذاب‌ترین بخشش اینه که از روش‌های پیشرفته عبور از فیلترینگ مثل Hysteria2، AmneziaWG و حتی olcRTC پشتیبانی می‌کنه؛ روشی که ترافیک رو شبیه تماس ویدیویی نشون می‌ده. همچنین توسعه‌دهنده‌ها اعلام کرده‌اند نسخه ویندوز و لینوکس هم در راهه.
⭐
برای کسایی که دنبال جایگزینی متفاوت برای v2rayNG، Exclave یا Hiddify هستن، ارزش یه تست رو داره.
🐱
GitHub:
https://github.com/yanisplugg/olcvpn-client
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6249" target="_blank">📅 10:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c54422014d.mp4?token=RUNdqZ6epEesWQMveLBzKFUUZx0NnPvzUPM67WzGp9ouAHTCNbZdaEzLalE3PuvGxcvlX7rbki9vUNvuWR03OYYzoxC2auuoPYMVrkIDHG_U6GSm2yBUDuLRK8o4GlziQgipY8Z5I3POjBymBuCYvI5t5qUQUed6_PMtdA0vfBDMVS9oHL-Upv304l0Hsj4oYfD0hr10jc6EZwG3wqFQ7t9mHM1HaDV6a6nNpcBvYWLtq7BGrpQDOPqJ2mGfYWNI895tsYiyy9BAnlCBRHucGyX8V-1Nu3-JD8UvdKZXvWlvvn835iziBQ5HskiWf2n6KMfUj3YS69ZK8AnAbzRJ0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c54422014d.mp4?token=RUNdqZ6epEesWQMveLBzKFUUZx0NnPvzUPM67WzGp9ouAHTCNbZdaEzLalE3PuvGxcvlX7rbki9vUNvuWR03OYYzoxC2auuoPYMVrkIDHG_U6GSm2yBUDuLRK8o4GlziQgipY8Z5I3POjBymBuCYvI5t5qUQUed6_PMtdA0vfBDMVS9oHL-Upv304l0Hsj4oYfD0hr10jc6EZwG3wqFQ7t9mHM1HaDV6a6nNpcBvYWLtq7BGrpQDOPqJ2mGfYWNI895tsYiyy9BAnlCBRHucGyX8V-1Nu3-JD8UvdKZXvWlvvn835iziBQ5HskiWf2n6KMfUj3YS69ZK8AnAbzRJ0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
تلگرام برای اپل واچ
تلگرام به طور رسمی اپلیکیشن خود را برای اپل واچ بازگرداند.
#Telegram
#AppleWatch
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6248" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkMhJU8IEiV9FEOt7hkhZbYVZzWBG-b6rn0uPctNvuybvvXUoJYrOkGdfxSUKLHyUTCAO_VzUZ0Ocje3Cr-bw0kaIeH37YyU_sOlViGEn_UiUZkcenGcmINO3MPKl23JzFrqLJuM_a7DJYZlpaSh_mJ09S32PsfzfgyLf7h9wFkrxN1FCbRdPQJ4wWX2HmxK90TJSgnZEc1hoMRatGwaUJSmE8cARtZJ-V9HH9pxdkKlQkl6SLf_ft-JQ8C0vUViNVvXXHO1w99Vw1L2RHyV64Tj6iK2slvHVkSAyw0G2QxtJNoC-aLgCWIX3g2_D-7Sv7h-S7D56ArAM8OMtvkvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک فهرست بزرگ از ابزارهای رایگان هوش مصنوعی برای تست، توسعه و اجرای مدل‌ها
🤖
✨
قابلیت‌ها:
•
🔹
مدل‌های متن‌باز؛ از مدل‌های سبک خانگی تا گزینه‌های قدرتمند
•
⚡
ارائه APIهای رایگان برای توسعه و آزمایش
•
🛠️
اجرای محلی مدل‌ها با تمرکز روی حریم خصوصی
•
💻
دستیارهای کدنویسی رایگان جایگزین Cursor و GitHub Copilot
•
📦
فریم‌ورک‌ها و دیتابیس‌های کاربردی برای ساخت سیستم‌های چندعامله
🔗
لینک:
https://github.com/12britz/awesome-free-models
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6247" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">💻
NekoBox 5.11.18 برای ویندوز، لینوکس و مک منتشر شد
🔹
یک کلاینت متن‌باز و قدرتمند مبتنی بر Sing-box برای اتصال به انواع پروتکل‌های ضد فیلترینگ.
🔹
پشتیبانی از VLESS، VMess، Trojan، Shadowsocks، Hysteria، TUIC، WireGuard، SSH، Tor و...
⚡️
🔹
دارای حالت TUN برای هدایت کل ترافیک سیستم.
🔹
سبک، سریع، رایگان و بدون تبلیغات.
🔹
گزینه‌ای مناسب برای کاربران Clash Verge، Hiddify Desktop و v2rayN.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6246" target="_blank">📅 08:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">vless://5dcf2dbf-3e82-4456-8961-287cc732bb0f@85.198.20.217:12817?type=ws&encryption=none&path=%2F&host=Play.google.com&security=none#Germany%20Hetzner-.
10 گیگابایت تانل المان</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6245" target="_blank">📅 03:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2vUt7jMnSEUt_8OKUQqr9mCrYZn9DgaNAZjm0vSFy_W5di5vcTi15npNZ-qiqThWBF1gJivH265S5avLWtmFVTFIzwq-fwKvJp4Lo0UStu1wO0R8b5sCZEajZoYwnvlMtn6sz2wKRMTNEnELzrJ9GlHAOuLpzVw-8SavHg1jJBOL42fKDaEvTjRa0j54QLbiKQpjOK7WXlFTCHBAcwn6WGN-o8HfPzGjpEl_i4HNC15lDK0N3WWd96Q7dew2OQ6-jBQDW_YGPK7OoAUzD9KIy_AJVTSU63iLgr8in27BNGM95ZtnMwXt19wuCOHjBXckpMv223Si8Fzv6r6GVpr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله
😱
💻
اگه با 3X-UI کار می‌کنید، یه پروژه جالب به اسم X-UI-PRO منتشر شده که کلی از تنظیمات REALITY و WebSocket رو خودش انجام میده و دردسر راه‌اندازی رو کمتر می‌کنه.
🚀
🔐
این نسخه Nginx رو هم کنار 3X-UI میاره، SSL رو خودکار تمدید می‌کنه، روی پورت 443 کار می‌کنه و حتی برای مخفی‌تر شدن ترافیک از بیش از ۱۵۰ قالب فیک استفاده می‌کنه.
👀
⚡
از Sing-box، Clash Meta و Cloudflare هم پشتیبانی می‌کنه و برای Ubuntu 24 و Debian 12 آماده شده.
🛠️
اگه دنبال یه پنل کم‌دردسرتر برای REALITY هستید، بد نیست یه نگاه بهش بندازید.
https://github.com/mozaroc/x-ui-pro
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6244" target="_blank">📅 03:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hala Hey _ Live In Concert</div>
  <div class="tg-doc-extra">Armin Zareei _2AFM_</div>
</div>
<a href="https://t.me/archivetell/6243" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">امشب رو با این معما بخوابین
شرکت در کنسرت این شخص، از نظر اخلاقی، غیراخلاقی هست؟
#Moral_Dillema</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6243" target="_blank">📅 02:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🫠</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6242" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku_aRKDCBZAHw3MuF5f8bBvordpkXy1AuBDbvcq282zZEpnJpOYvnrfRbidwFLQtFloLCqghwlmSc27_HPBIQpQEnNjzjOXvRlgcuIyMbhaHbqNeU70_3sVdupgS9R2hr4SWNxRwpZL9PFkVrLkGkIq85w-w_WXGxLSrc59SOEZvUqwb4px00phzvV_7ziZW1HYOnxVkecykLD1SfGDY5WbN9MiCvH0-xEzlIF4p1dgj8pBVvC6v2EkwcTp6gu2F7IdZFV4V8VieggNgoLYc8t1JGEBb-4ILEMy3Go5b6kWetZ5qkP69nDj6RWsVGOvtjDuyqYosjp0nKG676y4nkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Gemma 4 بدون سانسور منتشر شد!
🔹
یه نسخه دستکاری‌شده از Gemma 4 اومده که تقریباً هیچ درخواستی رو رد نمی‌کنه.
🔹
روی سیستم‌های معمولی و حتی آیفون هم اجرا میشه.
📱
💻
🔹
حجمش کمه و با Ollama و LM Studio هم سازگاره.
🔹
جالب اینجاست که با وجود حذف محدودیت‌ها، کیفیت مدل تقریباً مثل نسخه اصلی مونده.
⚠️
طبیعتاً دیگه خبری از فیلترها و محدودیت‌های امنیتی نسخه اصلی نیست.
👀
🫠
..
#Gemma
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6241" target="_blank">📅 01:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
بی رفرال
🤐
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 140 / 140
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6240" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">https://t.me/ArchiveTellNews/212
🤨
🤔</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6239" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6238" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app
بخونید نظرتونو بگید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6237" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">StormDNS
a.cyntarix.com
25ffbc77bcfb23b2d4ee225eedcd2466
داشته باشید اگه نت قطع شد</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6236" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این پروژه پایتونی جالب هم برای تشخیص اشیاء توی ناحیه مشخص شده کاربرد داره مثلا طبق مثال خودش که با QWEN ادغامش کرده یه نفر با هودی اومده توی ناحیه مشخص شده تشخیصش داده و به گوشیش نوتیف فرستاده و گفته چه چیزی با چه اطلاعاتی اومده توی ناحیه.
برای دوربین مداربسته خوبه یه ناحیه رو مشخص میکنی هر چیزی اومد توش بهتون خبر میده،کد اصلیش با پایتون نوشته شده و از ابزارهایی مث ffmpeg برای مدیریت استریم‌های ویدیویی استفاده می‌‌کنه.
github.com/roryclear/clearcam
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6233" target="_blank">📅 00:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6232" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هر کی 99 تا رفرال داشته باشه ی کانفیگ نپستر میدیم بش
😌
🔥</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6231" target="_blank">📅 00:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6230" target="_blank">📅 00:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6229" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4tIXsD76eEuGwIdMs7OZ5Vd4LQYJihdukW_1ziSRSHpx0kgr-iBZYUTbrPo5LnAebwRfl29XGqh1wV451iKVKIIUvKm8-D3kxT7cn86tAMszPWOfa-CH24B-3pHscTkLdvvp3Ta_rMEOEs4a1c9r2SaTg2Ht1UwBDJ4qXCEesCfeVV2tfusSw06V1OY6RVfnthbdBhshWJ5zRGaKXJrASbEB3soKizIt6_gxe1yfEg7wTDwbBVXlqmIkwAROuHngqo9JbBRQgEhlPj7Xjqd_ysCp6QGc5CzOaC2X9gh-g7fw9TdCo_014eYCLL7CLASzGBnYSDrsI9bsuEXvMdmbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Gitdot؛ رقیب متن‌باز GitHub که با Rust ساخته شده
🔹
پروژه Gitdot توجه زیادی جلب کرده و به‌عنوان یک جایگزین مدرن برای GitHub معرفی شده است.
🔹
این پلتفرم از ساخت مخزن، Push/Pull، ریپوهای خصوصی و عمومی و مهاجرت از GitHub پشتیبانی می‌کند.
🔹
رابط کاربری آن با الهام از ابزارهای CLI مانند Vim و fzf طراحی شده و روی سرعت و ناوبری با کیبورد تمرکز دارد.
⚡️
🔹
قابلیت‌هایی مانند Pull Request، Issues و CI هنوز در دست توسعه هستند.
⚠️
با وجود استقبال کاربران، Gitdot هنوز در مراحل اولیه توسعه قرار دارد و فاصله زیادی تا رقابت کامل با GitHub دارد.
🔵
@ArchiveTell
| Bachelor
⚡️
https://gitdot.io/</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6227" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🛑
پایان uBlock Origin در Chrome نزدیک است
🔹
گوگل آخرین راه‌های دور زدن محدودیت‌های uBlock Origin را مسدود کرد.
🔹
پشتیبانی از افزونه‌های Manifest V2 به‌طور کامل در حال حذف شدن است.
🔹
فلگ kExtensionManifestV2Disabled نیز از Chromium حذف شده است.
🔹
مرورگر‌ های Edge، Opera و سایر مرورگرهای مبتنی بر Chromium هم این مسیر را دنبال خواهند کرد.
⚠️
نتیجه: نسخه اصلی uBlock Origin به‌تدریج از دسترس کاربران خارج می‌شود و کاربران باید به uBlock Origin Lite مهاجرت کنند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6226" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=LDpWSx08gHCB5itwLUeaH0zTovTJYEuU7RgJldFvivctL01iByt2jnXHlYJph0DnxXLJxrpL3u9RzzbC90QzpicTuoMXk6vByiUoxT9wgcxepr6sP9Fy7FlHHkfF0DjQF_fSi6RTSVlJKFAx_AUWBltrg33axGtfUoXop-VwHStpqYIKLWyfq_P91YG1XBjAEAqaGtN67h6tXxUy2GdcxPZefsvbzVJbHwTwxOQOLed7UtuoNFiEqsDNjgM4YwZ2L_pW6Dv9eEAaMALsl8OGs7YSvS5LXGw2ma5GRZgVirWu9RINFynPmdLX1a2ctbdAEPrQL4NlRqFrXw4mDAXTLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=LDpWSx08gHCB5itwLUeaH0zTovTJYEuU7RgJldFvivctL01iByt2jnXHlYJph0DnxXLJxrpL3u9RzzbC90QzpicTuoMXk6vByiUoxT9wgcxepr6sP9Fy7FlHHkfF0DjQF_fSi6RTSVlJKFAx_AUWBltrg33axGtfUoXop-VwHStpqYIKLWyfq_P91YG1XBjAEAqaGtN67h6tXxUy2GdcxPZefsvbzVJbHwTwxOQOLed7UtuoNFiEqsDNjgM4YwZ2L_pW6Dv9eEAaMALsl8OGs7YSvS5LXGw2ma5GRZgVirWu9RINFynPmdLX1a2ctbdAEPrQL4NlRqFrXw4mDAXTLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6225" target="_blank">📅 22:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfLt4kWMDr3x43obTkn4e1IL_XVW00b5j971Vp1gURXiCDrIXCNCBqOLH8Tc7SdiY9Wql2Lnn_Z6iYlk4bDW1hlfCbRP1B9zRQOVYJGXkvFblNqt9WYLbOl30z_asVtY0lbSHNq8asQnqipcPm-j4oAuurKlIQIzyrHXNs36W6vVQSeCALwS07z2O1yr4EmUiBWA4ACHVG4CeNG7nS7o7Ij1pMWCFqnt3D-nWzFboSV8Ht8DP48r2tH9H_J3xLQ0DStbU5StUcvkNGFuMAeNJtTUPajpBhI6QXLxc4qLZN1gHeZPdZ15u_5BlyJMBYSxC6dCCsuaYo-xWl__u7nHTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک ویرایشگر ویدیوی کامل که مستقیم داخل مرورگر اجرا می‌شود؛ بدون نیاز به Premiere Pro یا CapCut
🎥
✨
قابلیت‌ها:
•
🔹
پشتیبانی از چندین ترک ویدیو و صدا
•
⚡
رندر سریع با شتاب سخت‌افزاری GPU
•
🛠️
افکت‌ها، ترنزیشن‌ها و ابزارهای تدوین
•
📱
قابل استفاده روی کامپیوتر، تبلت و گوشی
•
🎬
عملکرد پایدار حتی در مرورگر معمولی
🔗
لینک:
https://tooscut.app/
#VideoEditing
#Tools
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6224" target="_blank">📅 22:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">طبق درخواست شما عزیزان
تمامی سرویس هایی که API رایگان هوش مصنوعی در اختیارتون میزارن رو مجدد قرار میدیم
✨
Freemodel.dev
🥇
developers.cloudflare.com
🥈
console.groq.com
🥉
aistudio.google.com
build.nvidia.com
cloud.cerebras.ai
openrouter.ai
console.mistral.ai
llm7.io</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6223" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ramNIBhm4DQULRqXRXoIg8ilNlYvAC9-WbeC6DQVpMNLriPdEx6PrFZ122gv1lS7FZBW8QxKIIt6JuzbM6SEJNrlkJhSUyJzrAjxewbA4fiFhMLY17OvcRkmc5UHhdmOVI9XgbAyUupNXenU8Fa80mVMG7yU-a-gpsftzWwiZMEMYbOJvxmq9g1q2IeYd61opTp9qXMPXcCVraABz0tRcJUkq-VuvbW7R4o4Uc4NS1IIzAZ4FiwuVspeVskI4_QCX1bLtvHN6ED5Wakp9rBCeyXLXjMMQrxJLNgz07L6gfww-IZSCQQ7nr4CYMoBZ_g_Ap6vQBhT2f7h9R71KxmEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
کاهش بار اضافی روی حافظه در ویندوز ۱۱ — غیرفعال کردن فعالیت پس‌زمینه Edge
😎
این کار از طریق ویرایشگر رجیستری انجام می‌شود:
1️⃣
کلیدهای Win + R را فشار دهید → regedit. را وارد کنید.
2️⃣
به مسیر زیر بروید:
HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Edge
3️⃣
روی فضای خالی کلیک راست کنید → «ایجاد» → پارامتر DWORD → نام آن را «StartupBoostEnabled» بگذارید و مقدار آن را 0 انتخاب کنید.
4️⃣
کامپیوتر را ریستارت کنید.
پس از این کار، Edge دیگر در پس‌زمینه اجرا نمی‌شود و منابع را مصرف نمی‌کند.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6222" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">walf.zip</div>
  <div class="tg-doc-extra">12.9 MB</div>
</div>
<a href="https://t.me/archivetell/6221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ℹ️
فایل سرچ پروتکل و سرور ویندسکرایب
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6221" target="_blank">📅 19:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚀
برنامه WALF منتشر شد!
اسکنر خودکار سرورهای ویندسکرایب نسخه PC
اگر از عوض کردن دستی سرورها خسته شدی یا دنبال یه راه سریع برای دور زدن فیلترینگ میگردی، این برنامه دقیقا همون چیزیه که نیاز داری.
کار برنامه چیه؟
برنامه WALF کاملا خودکار و بدون اینکه نیاز باشه کاری کنی، تک تک سرورها، شهرها و لوکیشن های ویندسکرایب رو روی پروتکل ها و پورت های مختلف تست میکنه تا بهترین و سریع ترین اتصال رو برات پیدا کنه.
👇
چطور کار میکنه؟ خیلی ساده:
۱. فایل برنامه رو از لینک زیر دانلود کن و از حالت فشرده درش بیار.
۲. فایل walf.exe رو اجرا کن و دکمه Start رو بزن.
۳. تمام! خود برنامه اگر ویندسکرایب بسته باشه بازش میکنه و شروع میکنه به اسکن کردن کل شبکه تا بهترین اتصال رو برات ردیف کنه. (فقط مطمئن باش که قبلا توی ویندسکرایب اکانتت لاگین شده باشه).
لینک دانلود برنامه سرچ خودکار پروتکل پورت و سرور های ویندسکرایب در پست بعدی
⬇️
با تشکر از چنل
@CubicDreams
که زحمت کشیدن ساختن
🙌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6220" target="_blank">📅 19:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خب یه پست اختصاصی دیگه داریم این فایل رو خیلی جاها میلیونی میفروختن در حالی که رایگان بودش یکم دیگه پابلیک میکنم
🔥</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6219" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWFNXeDF1wHFSa0DIJI1mBGnTxpyGpDXKFOAPSpFiKT6AIv0XVChjlWOk5CDNXB6MvEgf9OO_pzl1RBLdZrT0iNMm3XkgeJ9Bp8HuVqcWIM4AY30MwQ3EV360S_hgexh_vKxk-494hAwdD-pUDImzbm4aHL2Y0xDtI7p5F1i8_dniH5PaP6j9Gvame4chN2YkTwFB-R1o0gkxpTzjOk7lyEsN2CWR5GZEoAvUo8bHoDqKd5uWr0s1XwjuWLNtDoPuWOyHXsLgg1mOuNs9Ue9PfxxLKiEFuRGEIZFbs0ULG6iYZGjI6FlNHR-_mtKZesBHfs1HsL9NERU2lEyMnreiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel  اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت Freemodel شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6218" target="_blank">📅 18:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚠️
اطلاع رسانی برای افرادی که اشتراک ویندسکرایب پرو خریداری کرده‌اند:
پروتکل
ikev2
روی تمام لوکیشن ها (تقریبا) متصل میشه
✅️
با تست هایی که گرفته شده با فیبرنوری مخابرات  سرعت همه سرور ها دانلود ۲۰۰ مگابیت و اپلود حدود ۵ مگ فعلا قفل هست
(پیش‌بینی میشه پهنای باند ikev2 کم کم محدودیتش برداشته بشه و به قبل شرایط ۱۸ و ۱۹ دی ماه محدودیت شبکه برگرده)
سرعت کانکت شدن به سرور ها و امنیت ، این پروتکل خیلی بهتر از tcp هست حتما استفاده کنید
👌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6216" target="_blank">📅 18:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ArchiveTel
pinned «
ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6215" target="_blank">📅 17:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel
اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت
Freemodel
شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
بخش اول: احراز هویت با شماره تلفن
🔹
بخش دوم: احراز هویت با تلگرام
✅
گزینه احراز هویت با تلگرام را انتخاب کنید.  لینک ربات تلگرام برای شما نمایش داده می‌شود. وارد ربات شوید و استارت را بزنید
🎉
پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار  هر هفته: ۶۶ دلار اعتبار
💰
4️⃣
از منوی سایت وارد بخش API Keys
شوید و یک API Key جدید بسازید.
5️⃣
در بخش Docs می‌توانید مستندات کامل استفاده از API را مطالعه کنید.
🛠
تنظیمات نمونه:
model_provider = "freemodel" model = "gpt-5.5" model_reasoning_effort = "xhigh" disable_response_storage = true preferred_auth_method = "apikey" [model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses"
🤖
حالا API Key و مشخصات بالا را به هوش مصنوعی موردنظر خود بدهید و از آن بخواهید برایتان کد تولید کند:
✅
JavaScript
✅
HTML
✅
Python
✅
PHP
✅
Node.js
✅
و بسیاری زبان‌های دیگر...
💡
می‌توانید با آن:
🔹
ربات تلگرام بسازید
🔹
وب‌سایت طراحی کنید
🔹
ابزارهای اتوماسیون ایجاد کنید
🔹
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت خوبی برای تست GPT-5.5 بدون پرداخت هزینه است.
@Archivetell
✨</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6214" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6213" target="_blank">📅 17:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
hysteria2://5z15av99psrlhdqp@32.195.51.20:39150?alpn=h3%2Chttp%2F1.1%2Ch2&fm=%7B%22udp%22%3A%5B%7B%22settings%22%3A%7B%22password%22%3A%22dlxmzvxvcp3i6v0e%22%7D%2C%22type%22%3A%22salamander%22%7D%5D%7D&fp=chrome&obfs=salamander&obfs-password=dlxmzvxvcp3i6v0e&security=tls&sni=32.195.51.20#usa_hesteria-%40u2vpn-100.00GB%F0%9F%93%8A
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6212" target="_blank">📅 15:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پروکسی‌های اختصاصی آرشیوتل
😎
⚡️
پروکسی ۱
🚀
پروکسی ۲
💥
پروکسی۳
💡
روی لینک بزنید و گزینه Connect را انتخاب کنید.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6211" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4CeROI1ljVH2suWWgMAF-vg4W2DFeGdDk_U62EOK1XH402fqGzSSftnJ1xXPU6JcLapJxxjh20l2ttiSwhytKYnt2uwHPPYVAIAWOm_g7YzpuQVmU3LwybyR-gs9xftYWm2ZXDaxBl0PIZvGGI0nT9hL2oCRZ5-CoYdMuLtCTezfcJaPlCRCVahq317xccFyv_cISoF09ElD4-Hfr0mWhWUHDsUYn9gguFtfFR0ThSicmKOFT5C8TmTuXUf1EpLEl0OazFTRPZgXg17oYmQhnsqHbnNrOmv1w-pftNmucdtsPYCPK3yjFh8GkrdR0FtvWWm6YnUMEjAG69J1EYtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب یه روش مخصوص ایرانی‌ها اضافه کرده، رو همه اپراتورها عالی کانکت میشه:
Settings → Connection → Anti-Censorship
گزینه Protocol Tweaks رو روی Enable بذارید، بعد وارد Configuration بشید و یکی از دو گزینه آخر که ایران هست رو انتخاب کنید. گزینه Large TLS رو هم روشن کنید.
پروتکل های udp و tcp رو تست کنید
ایرانسل tcp 587 france
مخابرات همراه اول udp 80
با فیک میل اکانت بسازید
https://windscribe.com/signup
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6210" target="_blank">📅 13:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY2sWa5neF8gex6UvK32hqTy-XAGQ09OFeChoyKuEKeceLHDiqJMDGtBMj1vYmrqHT5fbUACmJXn0FmQ-q8PiktvzsuP8H04c94ox4xEj77oDylq8UNKTwyVP1h3J1rR-h-9IBgFQX-RZfRox7j_AyTrpatdMlTH4efT6jpRFWCnI5wBWkeUVBLGoamDVrtp51hUAYRKzJ-RKj4s_w51icMqOFzOoTA5i2-oz3VMcYadWgNBxn2IHQdIFW4zOFfBiNsBAnu79mYFTRpyrTiKCTahQwRwkjZQ3kGm6mEC_pr1wsKSyikwxlRT0Se0zWC7SplYXmsAPPydqY2t31lZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
Impeccable
‏این ابزار به عامل های هوش مصنوعی کمک می‌کند تا وب‌سایت‌های منحصربفرد و بدون الگوهای استاندارد ایجاد کند
🔥
‏
✨
قابلیت‌ها:
‏•
🔹
آموزش عامل‌های هوش مصنوعی برای ایجاد طراحی‌های منحصربفرد
‏•
⚡
کار به عنوان منتقد، توسعه‌دهنده front-end و نویسنده UX
‏•
📊
آزمایش ماکت‌ها، برطرف کردن خطاها و بهبود طراحی
‏
‏
🔗
لینک:
https://github.com/pbakaus/impeccable
‏
#هوش_مصنوعی
#طراحی
#OpenSource
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6209" target="_blank">📅 13:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ec__y6u_8nYDfw5-D7OVCJoEDxPgU9neZX7gaZQvr1znq87GUwF-yNaMBod1DJuD7kVZJCkxKymqhOInnL3zcybyWrKglclSWwaO2wO2zqCZacx0Qe5tfGXAV75vEGf4ukBkVWp23dCHLuvrxrwE7JkfzWMX23gSREmG6rEpKY8qSD_ee0P9fnP6Sq7cvzGUFdsNrzTo3yA-RYOAge2BeItKP9AbynmDxHU6cze_YhufAmHxuYjn2wgyZkp7TjXRe3UbwUnyCPLwnsPxNyWT0UElGRQIJHpvaWHHOTb4KSNS1sb45sitDg-ttSiUOoeh6NugsyMtbCjiICCUsFYMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEEJ2mFRCKtMZsAbSjcbRo0PGGiFS5hUwaC_Y3jnO1ehgitvdMxZYY5tpeKhJp9-ZYVvKENLpgBcU7UUYqxweBFU776X21mhbLisdFhbvkqWx9pOiEuNGaRKqoUKrR_b2qSXoPdGMimzMLaZhqe91fGF3jh9cm4tFq_BQjHlIjrwdQkKVx8xM_MrzuoqCQXHFIS26Qr5hEJj0v3zhpvO_Yi-ilQSpqj5aL3kBFONezdMseEoPVlmpXjXzKSJFwBgq1qWrD8CHlKAGUvTvvFaAdCcLPrOnBZPwHpVDdSypTwtZ1Ziei8-z2CItc9sKfkLLQb6GCfd3PlQsgIo3oD7fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UGnzqHm953mSqyKbDB07xwPd05E1_F2Nq1yjWt4zkK8UHN1ykXherrxvcFjMalszP5nEF3dDJqmnJAjfn-MyFxD_fcPWrgPAJDpshMGypqStoHDcr069kubjyA5qbj6ccAjPQkUSHunTwDsOtSyk0Gc2fQukKNIwN8fv7hMuQzTZsM72Ts8oFn3hPln14RWRpZeeIeUIvTpNwBmaqqHaC7Vn6FkyDDr9clpqdgqFkAgK994ZYSy_ZZK8NWR6w29POJCE6lo9TtrB1arGcttD_e1T5VJ-3GDIQneANap45HzTlZ9Vqw9vD4PqMItzHAwHOV2w1RDMp-iXRfoHm952Ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=AIrZ8mO2TAPW3YhT5oY3Lv2UjoL_wf2dQm2sURmB-Ov5HEiouSodz2PNjCfXHg9u5YCkzTmPSK2Pog1CmKkW_I4cTfqY5968hL-RAn30y8C6uzDOrSy7Imnfy7h6MzlG83YxNoTscSPJGiy2wgUW6M-ZZ48jL9bvrcHycCW_GYVrWaLZ7zguN3oh6Qi0oZ5SHzbmFwWVZh8RnAQNiWwz6Fem5Rh5pUOeYAEdf9rqJInun8rTCiiKiUBQ5VrvNaaI51lmg7mGs5Rr-Ziy_iCLFP1p6wwqJi4HBTaVYxSLxxto1haEaNSOiHPJeyLnekXRH6Ek0AgdpjOTp2tIE8iB2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=AIrZ8mO2TAPW3YhT5oY3Lv2UjoL_wf2dQm2sURmB-Ov5HEiouSodz2PNjCfXHg9u5YCkzTmPSK2Pog1CmKkW_I4cTfqY5968hL-RAn30y8C6uzDOrSy7Imnfy7h6MzlG83YxNoTscSPJGiy2wgUW6M-ZZ48jL9bvrcHycCW_GYVrWaLZ7zguN3oh6Qi0oZ5SHzbmFwWVZh8RnAQNiWwz6Fem5Rh5pUOeYAEdf9rqJInun8rTCiiKiUBQ5VrvNaaI51lmg7mGs5Rr-Ziy_iCLFP1p6wwqJi4HBTaVYxSLxxto1haEaNSOiHPJeyLnekXRH6Ek0AgdpjOTp2tIE8iB2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
هوش مصنوعی Siri یاد گرفته است که عکس‌ها را مانند Nano Banana Pro ویرایش کند.
✨
قابلیت‌ها:
‏•
🔹
«بازآفرینی فضایی» برای تغییر ترکیب، زاویه و پرسپکتیو عکس‌ها
‏•
📸
ویرایش پیشرفته برای ایجاد عکس‌های خلاقانه
#Apple
#Siri
#Ai
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6205" target="_blank">📅 12:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWpOlr9etk9xPPkPv9HRmmxm6FPubvjk9yBEI41K4Q7R68EDGNFWkbLzRkAXWe4CYGnEG4OL8FZ1gWz4o_ywgK_6doYZxyYS_aXQMbQP2IWgBVSW21S3etdOb_rM267SNyoVhGMAldbKrW4n8qYcdlGEgFmA6n2XqO6dTVVsCGfwL8IpIIN5tcqwiPPjWJLXsHvji_pylzJN7dDh3u3CMkMvrTiVGFbilNIGSxIkJdxTP2IrsLeHlp0w9X4EN48a7Xrs7HN7thLgAvfrAQnLF-64oE05H74Ya4gi-CSoMhIr60rCz8cp6g3OND8sHM6N5KplHakAGQc2x9WMXba-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
.FrameCoach معرفی شد!
‏این ابزار هوشمند تنظیمات گرافیکی ایده‌آل را برای هر سخت‌افزاری انتخاب می‌کند و حداکثر FPS را استخراج می‌کند
🎮
‏
‏
✨
قابلیت‌ها:
‏•
🔹
انتخاب کارت گرافیک و پردازنده
‏•
⚡
انتخاب بازی از کاتالوگ
‏•
🛠️
دریافت تنظیمات بهینه برای حداکثر FPS یا بهترین گرافیک
‏•
📊
مشاهده تأثیر هر پارامتر بر عملکرد
‏•
📈
تست تنظیمات و پیش‌بینی فریم بر ثانیه
‏
‏
🔗
لینک:
https://theframecoach.com/
‏
#گیمینگ
#بهینه‌سازی
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6204" target="_blank">📅 12:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">با پلتفرم Cerebras به مدل‌های قدرتمند gpt-oss-120b و glm-4.7 با محدودیت بی‌نظیر ۱ میلیون توکن و ۲۴۰۰ درخواست در روز دسترسی پیدا کنید
🚀
شما می‌توانید کلید API خود را دریافت کرده و پروژه‌های هوش مصنوعی‌تان را با سرعت و دقتی فوق‌العاده پیاده‌سازی کنید
🛠️
. این یک موقعیت عالی برای استفاده از مدل‌های سنگین بدون پرداخت هزینه است
💸
، پس آن را از دست ندهید!
✨
cloud.cerebras.ai
🔗</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6203" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=CqGZezncRcSItzpQOwzXUGGfdwMkCNuKxnn9HixWuvbhCUcVTfFjUuQdVCw7ZnjmwR8rXTTM0-hu_V9M8jL6r-iqnncI3M6NeYlOQiMmMzWl60IPP-rNHI24gtw6tcSi7RJCfZCTtL-xx4jjr-vUIFN1pT3oskwYxvEg1ystYoyIYB4k70W6VaBISkZRD1vl-kaYK9Wa562rMNy_VN3l5rshqu9W1YHun6yQjGNgd705jcYtT9IX992jmx9O3sPlUj1DCj9FTS9RDErOdAEmKTZj1IYEDFnuYAFMqdwS0SwKhXYAOqa2SIrgnup_TGIa_e6Iw6_lpxm37GyG0Z5W7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=CqGZezncRcSItzpQOwzXUGGfdwMkCNuKxnn9HixWuvbhCUcVTfFjUuQdVCw7ZnjmwR8rXTTM0-hu_V9M8jL6r-iqnncI3M6NeYlOQiMmMzWl60IPP-rNHI24gtw6tcSi7RJCfZCTtL-xx4jjr-vUIFN1pT3oskwYxvEg1ystYoyIYB4k70W6VaBISkZRD1vl-kaYK9Wa562rMNy_VN3l5rshqu9W1YHun6yQjGNgd705jcYtT9IX992jmx9O3sPlUj1DCj9FTS9RDErOdAEmKTZj1IYEDFnuYAFMqdwS0SwKhXYAOqa2SIrgnup_TGIa_e6Iw6_lpxm37GyG0Z5W7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🤖
چینی‌ها یک هیولای هوش مصنوعی با ارتشی از عوامل عرضه کردند — Kimi Work می‌تواند تا صد دستیار را به طور همزمان روی یک دستگاه اجرا کند.
‏
‏
✨
قابلیت‌ها:
‏* تا ۳۰۰ عامل می‌توانند به طور موازی روی وظایف مختلف کار کنند
‏* مرورگر را تقریباً مانند یک انسان کنترل می‌کند
‏* دسترسی به داده‌های مالی را بدون پیچیدگی در تنظیم API فراهم می‌کند
‏* عادت‌ها، زمینه و اقدامات قبلی را به خاطر می‌سپارد
‏* با فایل‌ها و اسناد محلی کار می‌کند
‏* کد پایتون را اجرا می‌کند و فرآیندهای روتین را خودکار می‌کند
‏* کمک می‌کند برنامه‌ریزی کنید و وظایف بزرگ را تقسیم کنید
‏
🔗
https://www.kimi.com/products/kimi-work
#kimi
#ai
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6202" target="_blank">📅 11:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">78.2 MB</div>
</div>
<a href="https://t.me/archivetell/6201" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">12.8.0 (6913)
Directly downloadable from
telegram.org/android
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6201" target="_blank">📅 11:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyCpPDhK_q8N3CrE8T_RHEmr0awM1qdeVzR0DejjWJse9qbTUa0OWaF6PegbRIGE6YnNO2xOcqAqgimedweBWkK2BlFXLx8RNx5fD1IkwKNwFmiS8AL0scCQ0WSAb45SqdfDdS4_LNNIcIJ1MllhjIyXEDQ6B1IyzHXwgFSGEn1dCO6z8ZpjEcotvjtMqgCO38zz2cUcuYXmf0PCn_G0Uu6f3k-IKFFcztoiMXP9I_E4hHHFcwkyk2C5xAG20Wm7yUa3h4kIWhCMP5kSB28B4e4MbSQtxYqu66-kLEGGD6V8FlTzOQhPB1lpVc_GWaJ6Usznv2L6Kwlhy9AhQw1zOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
گوگل NotebookLM را با قابلیت‌های جدید هوش مصنوعی ارتقا داد.
حالا این ابزار از مدل جدید Gemini استفاده می‌کند و می‌تواند فراتر از یادداشت‌برداری عمل کند.
🚀
✨
قابلیت‌ها:
•
🤖
پردازش و تحلیل بهتر اطلاعات با Gemini
•
📊
ساخت نمودار و تحلیل داده‌ها
•
💻
اجرای کد مستقیماً داخل نوت‌بوک
•
📝
تولید اسناد و گزارش‌های مختلف
•
☁️
محیط پردازش ابری اختصاصی برای هر پروژه
🎯
ابزار NotebookLM کم‌کم از یک ابزار یادداشت‌برداری به یک دستیار تحقیق و تحلیل کامل تبدیل می‌شود.
🔗
لینک:
https://notebooklm.google.com
#Google
#Gemini
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6200" target="_blank">📅 10:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee5737315.mp4?token=onoCnNQaHdLQESiyVS2SvkT8Ojb0iS7ABs0y8j7m9l5SY1bGjx-6Ab3SE4O-R-hJTNeQC21T0L4OKlNXDF4SKSuGqfXTAjmtR2k0VpBwlkuoa1kGFovMnUzG-92-mpJl1d2_qM94exgJtYcq0ujgQVb15W09f8uzC7RUKhRSR4q1LqlbBDGx85k5mthK9Y-K1ut6Uf0pMTHmJKQwn-rXnm-wmty_uoy2lqYq4jFtLxY1k8IGBfg8xAwiCS0NGSyPJWofmG1SiCodrfVQDwBlAhTgtZ-mdJQJd45P-52fHUC_swhtMxWL039nZcOwYTsxBKrr6vU5t11cXqJGx7xRJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee5737315.mp4?token=onoCnNQaHdLQESiyVS2SvkT8Ojb0iS7ABs0y8j7m9l5SY1bGjx-6Ab3SE4O-R-hJTNeQC21T0L4OKlNXDF4SKSuGqfXTAjmtR2k0VpBwlkuoa1kGFovMnUzG-92-mpJl1d2_qM94exgJtYcq0ujgQVb15W09f8uzC7RUKhRSR4q1LqlbBDGx85k5mthK9Y-K1ut6Uf0pMTHmJKQwn-rXnm-wmty_uoy2lqYq4jFtLxY1k8IGBfg8xAwiCS0NGSyPJWofmG1SiCodrfVQDwBlAhTgtZ-mdJQJd45P-52fHUC_swhtMxWL039nZcOwYTsxBKrr6vU5t11cXqJGx7xRJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔤
پیدا کردن فونت هر سایتی در چند ثانیه
ابزار
Font Stealer
یک ابزار رایگان برای طراحان است که فونت‌های استفاده‌شده در هر وب‌سایت را شناسایی می‌کند.
✨
قابلیت‌ها:
• نمایش فونت‌های به‌کاررفته در صفحه
• دانلود فونت‌ها در فرمت‌های مختلف
• پیشنهاد جایگزین‌های رایگان از Google Fonts برای فونت‌های پولی
🎨
ابزاری کاربردی برای طراحان UI/UX و توسعه‌دهندگان وب.
#Design
#Fonts
#WebDesign
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6198" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🌐
اختلال VPNها در روسیه وارد مرحله جدیدی شده است.
گزارش‌ها حاکی از آن است که فیلترینگ در روسیه نیز دیگر فقط بر اساس IP نیست و اکنون الگوی ترافیک و TLS Fingerprint نیز بررسی می‌شود. همین موضوع باعث ناپایداری VPNها، MTProto و پروتکل‌هایی مانند WireGuard و VLESS شده است.
#VPN
#Telegram
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6197" target="_blank">📅 10:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚀
پروکسی محلی برای تلگرام دسکتاپ
TG WS Proxy یک ابزار متن‌باز است که ترافیک Telegram Desktop را از طریق WebSocket عبور می‌دهد تا اتصال پایدارتر و سریع‌تری داشته باشید؛ بدون نیاز به سرور واسط اختصاصی.
✨
قابلیت‌ها:
• اجرای MTProto Proxy به‌صورت محلی روی سیستم
• انتقال ترافیک از طریق WebSocket و TLS
• پشتیبانی از Windows، Linux و macOS
• رابط گرافیکی ساده برای مدیریت تنظیمات
• متن‌باز و رایگان
📥
دانلود و مشاهده سورس:
https://github.com/Flowseal/tg-ws-proxy
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6196" target="_blank">📅 03:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">قابلیت جستجو در وب در ربات هوش مصنوعی وگا اضافه شد.
🔍
همین حالا بیاید و اون رو در پیویتون و گروهاتون تجربه  کنید.
😉
@T_Vegabot</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6190" target="_blank">📅 01:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">موتور جستجوی ربات
Vega
چگونه کار می‌کند؟
🤔
بخش جستجو در وب در Vega از مدل gpt-oss-120b پشتیبانی می‌کند که API آن توسط Groq ارائه شده است.
🌐
همچنین در این سایت انواع مدل‌ها وجود دارند که سرویس‌های جستجوی وب مختلفی را ارائه می‌دهند.
🛠
سایت برای دریافت کلید و تست انواع مدل‌ها
✨
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6188" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=NqjQQQ1VyonfOfKeocSvQMkkNXWC5QeP3nPsuQfQXtGZhc5IPsvivsNrEVX69sKSlC-ko0CBbBRh-vOz3Pq7y4IszYgtURJih7UIsMJdDtz3TdJj7hY_PYhqOJt-lwBWmEThnt_RxFuGEGGkpS032lGrMNQidFPz_WMabjzIhFAV0V4MDzpS-NQtATMJriGWQ88WHkVFeZTi6wZQGbuk0Rrp6mgonLhPvuxdD22UdukTR6yoWUzoB4OY3_zB3Q2ZPN5klpljwzHgK3Q2NFinfpKFGI53wFWygNo22jxovxbPkYuZl9FGIR7XJ5d5FMB7c_F5Q9gelmyvEr0LVzE-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=NqjQQQ1VyonfOfKeocSvQMkkNXWC5QeP3nPsuQfQXtGZhc5IPsvivsNrEVX69sKSlC-ko0CBbBRh-vOz3Pq7y4IszYgtURJih7UIsMJdDtz3TdJj7hY_PYhqOJt-lwBWmEThnt_RxFuGEGGkpS032lGrMNQidFPz_WMabjzIhFAV0V4MDzpS-NQtATMJriGWQ88WHkVFeZTi6wZQGbuk0Rrp6mgonLhPvuxdD22UdukTR6yoWUzoB4OY3_zB3Q2ZPN5klpljwzHgK3Q2NFinfpKFGI53wFWygNo22jxovxbPkYuZl9FGIR7XJ5d5FMB7c_F5Q9gelmyvEr0LVzE-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍎
Siri AI: تحولی در WWDC 2026!
در آخرین حضور تیم کوک، سیری با قدرت گرفتن از Google Gemini به یک چت‌بات هوشمند با اپلیکیشن مستقل و دسترسی کامل به اکوسیستم اپل تبدیل شد.
🤖
این دستیار حالا با دسترسی عمیق به ایمیل‌ها، عکس‌ها و تقویم، می‌تواند کارهای پیچیده و چندمرحله‌ای را به‌صورت کاملاً بومی مدیریت کند.
✨
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6187" target="_blank">📅 21:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=tiTz1FDazWoGKOtLiw7tnV3iZZKws7lti53oIWwQPg1hpZAizJ9DctK_XgpwmIjFzlufjEmLHiB_X6HonEFlv6jfMp_5SAprxBq02kmtpvxCK9W9Wd-QDG8H_fHT6L4UvUaG9uA0q7aGTtYjHVq4Qphv1QXtkSCZm8Np7MK6ahrf-VXbnLdGOmdaCQ9NUr6TLcEIxxKtgVXWp_xRJ7jLFu3_7i32oHIHibdSXT9Eb-eeVyZLxGbYxQgGYEpcSeDpBxbbkRZiua_BrUCFooIXhLgX3s58s_9pXfAYKh1Mn6Sn9XsWUwwWwEZsvFvy8acHvhI3pXS9RkkEz5C7AD-59Q" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=tiTz1FDazWoGKOtLiw7tnV3iZZKws7lti53oIWwQPg1hpZAizJ9DctK_XgpwmIjFzlufjEmLHiB_X6HonEFlv6jfMp_5SAprxBq02kmtpvxCK9W9Wd-QDG8H_fHT6L4UvUaG9uA0q7aGTtYjHVq4Qphv1QXtkSCZm8Np7MK6ahrf-VXbnLdGOmdaCQ9NUr6TLcEIxxKtgVXWp_xRJ7jLFu3_7i32oHIHibdSXT9Eb-eeVyZLxGbYxQgGYEpcSeDpBxbbkRZiua_BrUCFooIXhLgX3s58s_9pXfAYKh1Mn6Sn9XsWUwwWwEZsvFvy8acHvhI3pXS9RkkEz5C7AD-59Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Apple
#WWDC26
has started
Watch live:
https://www.youtube.com/watch?v=hF8swzNR1-o
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6186" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/em-qAE-GxyjHBqPBFN7cH5TEsdb8fQZ7Y9qSx0_p59SMkedq8Jn_tmOVWuAuxuEtdUhstbl58JeI4mDpiYdU9jTbUwHSWW472GgSYAsjNjfNgnFAr4nNMMYe1wImtdKWs1GekwikBSk32246jLNqnMszIZMZEHr_uWI9hMuaAya_X6B8PBG1MgV5iEKvhtLxb8HB3-srocQm6v-XRWBr1Yqz5jjtbS8CpQ1qP9zAFMYHcaDwqUmHOUN9bJT7pY0ofRGOh08At-hIuBW5YqdN6auiXGbrLNcIZNy3PHmtdaHlFzJads7TDk3aLyjBnBX7x82KcTrW-YbjgIgSTXAGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت ارائه APIهای هوش مصنوعی رایگان
🔥
از مدل‌های چندوجهی شامل متن، تصویر و ویدیو پشتیبانی می‌کند و یک راه‌حل توکن مقرون‌به‌صرفه برای توسعه‌دهندگان ارائه می‌دهد.
🔗
https://agnes-ai.com/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6185" target="_blank">📅 20:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🤖
Kimi Work
دستیار هوش مصنوعی که کارها را خودش انجام می‌دهد
نسخه دسکتاپ Kimi Work منتشر شد؛ یک AI Agent محلی که می‌تواند بخشی از کارهای روزمره را به‌صورت خودکار انجام دهد.
✨
قابلیت‌ها:
• اجرای همزمان تا ۳۰۰ ایجنت هوش مصنوعی روی سیستم
• کنترل مرورگر برای جستجو، کلیک، تایپ و انجام وظایف مختلف
• دسترسی مستقیم به داده‌های مالی از Yahoo Finance و World Bank
• سیستم حافظه برای یادآوری ترجیحات و سابقه کارهای شما
💻
قابل استفاده روی Windows و macOS (Apple Silicon)
🔗
اطلاعات بیشتر
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6184" target="_blank">📅 19:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frmCr72N1yOopuH9Z-y-oYZEQhUO8jpA0WMNqCJDs-6yoDXGfMego6B3Mw2en5_a1W7kpE9W_UfKVey10baIIoGkqGKkl_nRp-YMumxYHlVGrrdgN635_8nMV-quA8Tr06RUvXj5w592XwfBao9kxMieDLUisguBd5Z3S9bjK8WycQrliHPrpbkICbw8YMS9N39ejV5kvGRrM2WgZLbTwQaucW7GGsOIXQaV4mwZo3YTvHEh2AkmGvgDTcuFO9OgVPJkWSlfTXSdxRySTuNRdR4m_0n_s7pAIZp-amUBghxJ7brBeoytW4x6qRdYcJOSkgZ2A6SbvRDpIEaSaKckhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
جعبه ابزار رایگان ویدئو
🔸
فشرده‌سازی ویدئو برای صرفه‌جویی در فضا.
🔸
برش سریع.
🔸
حذف کامل صدا.
🔸
ایجاد GIF از هر ویدئویی.
🔸
تبدیل بین فرمت‌های محبوب.
🔸
کنترل سرعت پخش.
🔸
افزودن واترمارک‌ها.
🔸
ادغام چندین ویدئو در یک فایل.
🔸
همه چیز به صورت محلی روی دستگاه شما انجام می‌شود.
https://www.zipvid.online/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6181" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
هکرها با سوءاستفاده از ابزار هوش مصنوعی متا، بیش از ۲۰ هزار حساب اینستاگرام را هک کردند
شرکت Meta اعلام کرد حدود
۲۰٬۲۲۵ حساب اینستاگرام
در جریان سوءاستفاده از ابزار هوش مصنوعی پشتیبانی این شرکت، در معرض تصاحب قرار گرفته‌اند. مهاجمان با فریب چت‌بات پشتیبانی مبتنی بر AI، موفق می‌شدند ایمیل حساب قربانی را تغییر داده و سپس رمز عبور را بازنشانی کنند.
🎯
در میان حساب‌های هدف قرارگرفته، نام حساب‌های مرتبط با
کاخ سفید دوران اوباما، برند Sephora و جان بنتیوگنا (Chief Master Sergeant نیروی فضایی آمریکا)
نیز دیده می‌شود.
🔒
متا می‌گوید این آسیب‌پذیری برطرف شده، لینک‌های بازنشانی رمز عبور نامعتبر شده‌اند و حساب‌های آسیب‌دیده تحت اقدامات امنیتی اضافی قرار گرفته‌اند. این حمله عمدتاً حساب‌هایی را هدف قرار می‌داد که
احراز هویت دومرحله‌ای (2FA)
نداشتند.
💡
این اتفاق بار دیگر نشان می‌دهد که واگذاری فرآیندهای حساس امنیتی به سیستم‌های هوش مصنوعی بدون کنترل‌های کافی می‌تواند پیامدهای جدی داشته باشد.
#Instagram
#Meta
#CyberSecurity
#AI
#Hacking
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6180" target="_blank">📅 18:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_hS5wtDxwnNzjrr34kTVtNHd9zRIjk3DL-5h1Gj_O0eIcB2s7GLacSenAeZAK2XAMoNpkBUkn5i79kt21sJeac0v612ODgFx-OVl8c9na9lNU3m5dpV-MeK70Q3qMf5c44XiRtxo3XZ2E_rdGGuLCoDAIKfcKHCj0Sy2-uLSawwixdCZc2PCfJJhh9WZL5mIfy7SDQWp0WMuHSeb1z3j8SytM0G2vzF2nPDmZsFJFIaBu0-e2CiqwH3DL5xUEXZEPIM0L2_wU5oGWmpXwZtx7tFrxfrXKyEe7asmQCDj3wTaHg-4ttBRp97bEJJbl1_wFK_-BIAvvaWxOO2xu8Yow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦾
شبکه‌های عصبی اکنون شبکه‌های عصبی دیگری می‌سازند — با عامل هوش مصنوعی خودکار ML Intern آشنا شوید.
⚡️
دیگر نیازی به یادگیری کد ندارید — عامل هوش مصنوعی مقالات علمی را می‌خواند و مدل را برای نیازهای شما می‌سازد
💎
مستندات Hugging Face را مطالعه می‌کند، مجموعه داده ها را جستجو می‌کند، کد می‌نویسد و آموزش را اجرا می‌کند
💥
خطاها را پیدا می‌کند، کد را اشکال‌زدایی می‌کند و شبکه عصبی آماده را مستقر می‌کند
🔗
https://github.com/huggingface/ml-intern
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6179" target="_blank">📅 18:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
کمپانی
OpenAI حالت Lockdown Mode را برای ChatGPT معرفی کرد
🔒
شرکت
OpenAI
قابلیت جدیدی با نام
Lockdown Mode
را برای ChatGPT معرفی کرده که با غیرفعال کردن دسترسی به اینترنت، Deep Research و Agent Mode، خطر نشت اطلاعات محرمانه از طریق حملات Prompt Injection را کاهش می‌دهد.
⚡
این حالت به‌طور کامل جلوی این حملات را نمی‌گیرد، اما آخرین مرحله استخراج داده‌ها را مسدود می‌کند و امنیت بیشتری هنگام کار با اطلاعات حساس فراهم می‌سازد.
💡
با وجود این قابلیت، OpenAI تأکید می‌کند که Prompt Injection همچنان یک چالش حل‌نشده در مدل‌های زبانی است و کاربران باید در استفاده از داده‌های محرمانه احتیاط کنند.
#OpenAI
#ChatGPT
#AI
#CyberSecurity
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6178" target="_blank">📅 17:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
ss://2022-blake3-aes-256-gcm:dxzSnG5le2y16bNqdyL2Hj2b9Qjptq2Ust7li7mLR6Q=%3AGZs23OkRjsO4i11hMhke9I48yENOx6VVuL23GKRXTi0=@37.32.8.201:8080#%D8%A2%D8%B1%D8%B4%DB%8C%D9%88%20%D8%AA%D9%84%20%D8%A7%D9%88%D8%B4%D8%A7%D8%AE%D9%84%D8%A7%D8%B1%DB%8C
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6177" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L29ZSiw17eoB3QC8iUOKvh8rJbIe5ux3UdWXi6UENkDyJXSqUJxh5aZJv-OE3ppqld2c26-KAJsFQMDtfWygVL_IKlsSJaHsLCbLhGo11ZxOshxxERn_oDzuKBjiNO8cw5Fbujlc3R4axGEApgxRpleOZcUfP3SVjfIAKJwiWiH8r2yN7si0Nbgan73PHQsTV6WAEuc3Uiq4lGP7XszFIqAbJPgvLSpi-Rg8832_URUB0BxAeuSO7MkfONHlvVLPXIpcpg5oSXe9hORPSH_362H7qgODUMjGeiQCiaVKw2KfFrKuq5zELSilE2-EwCtd43Nm9S1dfIVJfRsk5rETuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار تازه و ناب
🔥
@ArchiveTellNews</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6175" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی  وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6173" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=vvMptJSR_ggBuk51_0gW-qBgaMwr5JkJjglaBplQ7RXcqbH-Td5vI0ah73xQKz1FHp96C8HY85wSxXuTUmYWfF2vQrSq2kp__7IB2gqgupA5DI8fXkNJKbEQiW5p5r47a69hjb2ylDd8iGYwzj_DN1cz9fmPan_J460IWaFWCr8CPm5KNcovEqAoFEKu23OeFpsYNcZaDJZ92I8Tk_VzdjCBjXGZtd1AAy9ZVbaErY5EqGZhakHTrcZb6oinYnGZh6NHOEWWjbXwjF6eObZ5mKSeGZRPrcZmoQE47arPOHyS_LDxRXFfB1ZfWaItbYItw5S0rYm7etquSRgYmPVyXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=vvMptJSR_ggBuk51_0gW-qBgaMwr5JkJjglaBplQ7RXcqbH-Td5vI0ah73xQKz1FHp96C8HY85wSxXuTUmYWfF2vQrSq2kp__7IB2gqgupA5DI8fXkNJKbEQiW5p5r47a69hjb2ylDd8iGYwzj_DN1cz9fmPan_J460IWaFWCr8CPm5KNcovEqAoFEKu23OeFpsYNcZaDJZ92I8Tk_VzdjCBjXGZtd1AAy9ZVbaErY5EqGZhakHTrcZb6oinYnGZh6NHOEWWjbXwjF6eObZ5mKSeGZRPrcZmoQE47arPOHyS_LDxRXFfB1ZfWaItbYItw5S0rYm7etquSRgYmPVyXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
AlicentAI — هوش مصنوعی برای ایجاد محتوای متنی
💎
این سرویس پست‌ها، توضیحات محصولات و مقالات را بر اساس درخواست‌های متنی تولید می‌کند.
⚡️
از طریق وب کار می‌کند که در آن می‌توانید بلافاصله نتیجه را برای نیازهای خود ویرایش کنید.
🔗
https://alicent.ai/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6172" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">برای مدت کوتاهی اخبار مهم رو منتشر می کنیم
🙏
❤️
کنسل شد نمی کنیم
😂</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6170" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
تهران پارکینگ‌های زیرزمینی را به پناهگاه تبدیل می‌کند
بر اساس اعلام شهرداری تهران، در پی افزایش تنش‌ها و حملات اخیر، پارکینگ‌های زیرزمینی در سطح شهر به‌تدریج برای استفاده عمومی به‌عنوان پناهگاه آماده‌سازی و تجهیز خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6169" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
ارتش اسرائیل: برای چند روز درگیری با ایران آماده می‌شویم  بر اساس گزارش رسانه‌های اسرائیلی، منابع ارتش این کشور اعلام کرده‌اند که خود را برای چند روز درگیری و عملیات نظامی علیه ایران آماده می‌کنند.
📌
به گفته این منابع، از نگاه ارتش اسرائیل، تحولات فعلی…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6168" target="_blank">📅 12:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
ارتش اسرائیل: برای چند روز درگیری با ایران آماده می‌شویم
بر اساس گزارش رسانه‌های اسرائیلی، منابع ارتش این کشور اعلام کرده‌اند که خود را برای چند روز درگیری و عملیات نظامی علیه ایران آماده می‌کنند.
📌
به گفته این منابع، از نگاه ارتش اسرائیل، تحولات فعلی یک عملیات جدید محسوب نمی‌شود، بلکه ادامه عملیات Operation Rising Lion (شیر خیزان) است.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6167" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نت رو قراره بزنن
ای‌ک</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6166" target="_blank">📅 12:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
منابع ارتش اسرائیل: آماده سناریوی حملات گسترده حزب‌الله هستیم
بر اساس گزارش رسانه‌های اسرائیلی، منابع نظامی این کشور اعلام کرده‌اند که هماهنگی کاملی با آمریکا برقرار است و هم‌زمان برای احتمال حملات موشکی یا پهپادی گسترده از سوی حزب‌الله به مناطق مختلف اسرائیل آماده می‌شوند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6165" target="_blank">📅 12:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی
💎
vless://1b5607ba-c295-43f8-923a-dc633a099276@82.47.63.98:8443?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=farsroid.com&mode=auto&path=%2Flokayb&pbk=US5uDp2cCip8cEuQUWEf4o7VbASXg45EeVia_Kz2QTI&security=reality&sid=fc0f43e6354ef57b&sni=www.qq.com&type=xhttp#%F0%9F%94%B5@ArchiveTell%20%7C%2050GB
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6164" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شرکت Wizz Air اعلام کرد تمامی پروازهای خود به اسرائیل را حداقل تا فردا لغو کرده است. برخی پروازها نیز در مسیر فرود به تل‌آویو به مقصدهای جایگزین مانند لارناکا هدایت شدند.
در همین حال، سازمان فرودگاه‌های اسرائیل اعلام کرد که فرودگاه بن‌گوریون همچنان به‌صورت عادی فعالیت می‌کند و پروازها طبق برنامه در حال انجام هستند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6163" target="_blank">📅 12:24 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
