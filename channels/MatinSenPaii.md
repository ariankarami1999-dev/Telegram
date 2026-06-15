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
<img src="https://cdn1.telesco.pe/file/jlsdadSqdgx_P5c3gqgU5NyDPbWO3CebcM44mW7gAAxlN9yp20D0cfsDiPg-m97TTNDT8XrfYEo81dZEWg8Y4uGGMwMHBbJ0kqAtQe7ahc6FQ74VZ5BWzcECbm4yIDfTIQ7Z6wntPgzOO700myW8tiR85-gXn9_xMNJ-PNmoZBqG6BzXur5ZTaAEx79KUG6JZ09EcP-vXSP-vHEbWAbvaHzIPmkd-UeE9VjH1vqvsZE1p4rXRG9c9RhAkSOA5LCoNvk1nqYwkDYYEJ74fkCEgHFHu3PjERAX13fn4Gr977ij_NDfEQPrlrrDujKbYqh4NbpCHDZAb1L1lUHmK-UKPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 162K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 12:20:57</div>
<hr>

<div class="tg-post" id="msg-3890">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CP7X6_gT4OA828-wpuad6K06had9bEvkYOrJUkLN69pDjYi-Uzm4vp-s46UFW-d1BOGnihtjK9-jLOyF7Hy2b6XfJBoPgZWIITlco28Z-sCBjwNKTtTKwTDdjVgTEHE6YURha9x8D6KizqPshLIWIc55Lntqx7bNVnf32v6UpR8JnB3oakOPpELApVAAbhLdepDoL1XwofPWO6UC8dAQV3BMHZK-Qz5-Kc1rrsXvN2Ef4S5Kx9BUVb1EJJG_THMa__Rq4vTzalHLiu0sahVVh0gNqnZq_Z4PzwNTkMmAuP66wqfsviGu36Fd_HQJ6KXuuLXsda9AlHVmedLgw6AQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اول که ممنون از لطفتون و بازخورداتون، دوم اینکه اسکنر حجم زیادی میخوره حواستون به این نکته باشه
🧐</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/MatinSenPaii/3890" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3888">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k2jSugTFpL3ccgZXpd6Cz75BFMyp_uCBbBIGIarq5gFFcKoHGUP7g5peZUCG4FN6Qp0zS2AmJRsqdqroGhBD_rgbbyPKi9YvhLCW6k6IcGAW7cpUA2sBkySnCyDLQDOHO65VkzecFbO3t1ZwawtxCmOkxuiqFsBh1IVY1nN8HDq8Xc0TBGqWubQ2TrC8kJxLG6dY4Btragmnn1DJyLN7JLaSqfyBY3AlE1_GJrc4msaCo0j7eFsauP6mY7-L1vg4SHujHpH9DD9H_VP0fDCIK26K-qW1vNMrtd2QG_Ng1jexLlMCngWKdcO1Jk4Npa5PvT62lv6lArjyAsaOYn4VKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dc1-koR5Gar8lSPFzJXVHj6iw_kzV5U5ZvfNk0unlH9DeHlOXy0Y3CMyhvDeG-6JMbvRXaZmdvhS5C63rntOU7j6Yq9uXaWkXlSjpqvMjgyOaXh1M8wpC27Bp4-f_oMqBO-aabUk7C4kVvY_PPD9pIsKp5qTiSGnR0K8kjwoWLk0-nWFgf4YHNuA7_SNj92s2FsezqfNu-fTTc20Tn73oup6idgaKTWgeBgbAgsoX4KEn-q197La-RvrP77ezANM_DmKfQUqg_wQcWeuauF8uS8QKtpN9cwSR9SmS6IAEhesZxW-Y0Pg-1JmXm_1sueM2UuSECs-SC5qMbnyrTYISg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور: @nahanproxyipbot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/MatinSenPaii/3888" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3887">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V7wJg0SWNnIt82pdDA1puz0a69_HXoAmpUd0dasbs40qlkEPSKcKY5qUT2sX0Vv5moCQq1I-75siURajV8dEcbddS3TQfiCI0Xi8-GCAFtCviUmNGhECK2aHr2rPAYXhRzBJH8aYSMAOxCsoUYKb7Svh38D-mUicxoPJWyrnjS0xXCV18ZNfyqSz3UzK3o2sB7CfQPE7ppOvbpsP1c7tGDrDiyyZIDtZx6oMsU5olxszqAsNeiBEkYVNkW76hYGDbaxw4FUIrJxPRPDEhr_nK_8SZ51beG0GMtxcuStdexslIddQM9hGol3jBCioR5xllUhU0EGaSiltkf8gZzLVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور:
@nahanproxyipbot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/MatinSenPaii/3887" target="_blank">📅 10:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3886">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خب قیمت دلار اومده 165
انگار جدی جدی توافق(که نه، تفاهم) شده</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/3886" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3885">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GdUuMzjB6H5hb1dn3BcUfkfaVgbS3AJux9mmRjoli52c8-g4DuTjUpu92BqcaH0Oi4oze9-5w-GqQE1F0-68-W7fIrrp8WMmmIKlFKez4Ujeftp5xH3Nh6B3lfqHpgHCIjgR7T7IDZ89oc73Yda5rsZI9tirNO-iB20V82dC7R9EsAsKv7dJ7ws9H872cUsjttWSD5Y3JWvvSmBQIuK3MnnINy56KbCtG2hO3soh6uBhXl0IhsTAx1KytBeWdty612ZVLK9H3nizJhmjaPtBzLCMMZlC6AtTbZp9J4RjEmNCIdvP3sEcbp_8MiG1g7WjYtX-NlUXl9nbGSBqLTQGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پروژه‌ی جالب دیدم به اسم SurfSense، که بهش می‌گن جایگزین اوپن سورس NotebookLM
📞
اگه از NotebookLM میاید، باید بگم که SurfSense همون کارو می‌کنه؛ صرفا با کنترل کامل دست خودتون. خلاصه بخوام بگم، یه agent تحقیقاتی اوپن‌سورس و با تمرکز روی حریم خصوصیه که شبیه به کار NotebookLM رو انجام میده.
👍
مزایا نسبت به NotebookLM:
• اتصال به ۲۵+ منبع: گوگل درایو، Notion، Slack، YouTube، GitHub و افزونه‌ی مرورگر برای ذخیره‌ی هر صفحه‌ای (حتی پشت لاگین)
• آزادی انتخاب مدل: ۱۰۰+ مدل از طریق LiteLLM، یا اجرای کاملاً لوکال با Ollama و vLLM
• بدون محدودیت داده: هیچ سقفی روی تعداد منبع و نوت‌بوک نیست، و دیتا روی سرور(یا سیستم) خودت می‌مونه
• جستجوی بهتر: RAG دومرحله‌ای در برابر سرچ تک‌مرحله‌ای NotebookLM
• قابلیت‌های تیمی جالب: به شما رول‌های Owner/Admin/Editor/Viewer میده + چت و کامنت و...
• تولید پادکستا بدون محدودیته
😭
معایب:
• نصبش هلو برو توی گلو نیست واقعا. رو اعصابه — باید با dependency، API key و فایل‌های Env کلنجار برید
• هنوز کاملاً production-ready نیست و در حال توسعه‌ی فعاله
• باید خودت میزبانی و نگهداری کنی؛ طبیعتا که راحتی NotebookLM رو نداره
#️⃣
جمع‌بندی:
صادقانه بگم، NotebookLM همچنان ساده‌تر و آماده‌تره ولی کاملاً بسته‌ست. SurfSense سخت‌تر راه میفته ولی دیتا و انتخاب مدل کاملاً دست خودته. اگه با self-hosting و سرور هم بخواید پیش برید، به درد بخورترینه.
🔗
ریپوی اصلی:
github.com/MODSetter/SurfSense
آدرس خود وبسایتش برای دانلود مستقیم نرم‌افزار:
https://www.surfsense.com/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/3885" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3884">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/3884" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3883">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/3883" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3882">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LV2It6PnjfR3H0q6UB2r1Us-C3JhVrwxAELKkV-mVVk9fqLzqGcWy7EHPpRecKV4-_b7zy2qmgMsfeR-dlUEVvr7OFSYMVK0LMHmlCKapXJZosWtS4tPe66vJgMSQx5sHBLRQRB5oW7naxYhpU-7we85N5h804jurvb-s79-_URHorbNtRFIVz6RU-HOFi1nwlZa0Zpg-MYXcQfSbtAuaslPxZK-vfUE1u5EJ_oJhiMBtdZO6_Asbbz_J3U0H3qsHp3s-du3Yji1ZsLLINZOyUcHQwUiZGqkCfsax_9Jbu-II8_2bt_ZP6xcGvWY2bY5vEWTjN5FRWIEytAV6pIWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو برای اسکنر یا هر پروژه‌ی دیگه‌ای می‌گیرید، ترموکس رو از گیتهاب نصب کنید؛ درست میشه
https://github.com/termux/termux-app/releases</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/3882" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3881">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWRksh3smWzgmmGeKk2ToJ0_Ukfk641lhgUM4aKv2A5ueeCg6v1aJCQY3anX-goIQI0x-7F4owzKFwTDVbQh4K_YFAWEMkXo1E3_SkQfntf16fqHg1KpuGOzm9QRpL1c9NDHtOfY8-dVKmKCPW6dy3S4eHUjWFX-7KdOXk2SxKDIW04KUgzKhLQs7zC_rf38grL2E_Z8t6bWOdEIMtdYcBwPzJopPi9QuMFFVR3MJVWcHkEZ2b50xUmKtV-JG-PY2T_jDGwXaPwragJxNxtnUAF3enUoPSdmmPLNYrgaGHxgEM68Bd-8PmRY_71WRl2Ou5Sv6hz23GOFvBnt8ZdVKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان خودم با سرعت عالی وصلم روی ایرانسل. ۲۰ ثانیه طول کشید حدودا، منتها ممکنه تا چند دقیقه طول بکشه. ولی وقتی وصل بشه دیگه کانکت می‌مونه و قطعی نداره</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/3881" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3876">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3876" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید اپ WhiteDNS VPN آماده شده.
در این نسخه
• سرعت اتصال بهتر شده
• مشکل داغ شدن گوشی رفع شده
• اپ همانقدر ساده مانده و فقط شما باید دکمه اتصال رو بزنید
متاسفانه باید نسخه قدیم رو پاک کنید و این ورژن رو از اول نصب کنید. این مشکل از ورژن بعدی نخواهد بود.
ممنون
🔥
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/3876" target="_blank">📅 15:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3875">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TmWcyj223ZVIg6g7kOOgTF1buHkQmTcUZB1RZg9mpK2APryWCRHjrmlEZdqqlMnR2FMviR8i3n7s1lViJBpe5pUhqfQDkVykXdTgcFiu7fr_29WzGuSSWyc68pse_H-kwM0uldJyI2ovZDGPVb2ISNhVMzsd1QVbFnXQpFqVcXZsnP5s4hI1LOxIaYgwsoMjsMgSNlc1i1o6ZS6PEgQmlm74rFTPDBkikvVw5w-IldVL-RqXbu-z3c4lo-gd3Lj5sP80vGSb0rK-qcnUmKLn_jhyB2zmzKxJchVeqhmmD9lzDD9iNmGEgtAcWqUVxKYnr_8ZHcUSTG90fc4TLrGgFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو نمی‌کردم یه روزی قالب وردپرس رو هم بگن بیاید اقساطی بخرید</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/3875" target="_blank">📅 13:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3874">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خب دوستان به نظر من اشتباه کردم و فونت وزیر متن هستش. مسئله اینجا بود که از من پرسید، گفتش چه ترکیبی بزنم؟ چندتا داشت، یکیش فونت مربع+یکان‌بخ بود. منم زدم همین و بعد دیدم اصلا پولیه. اما الان انگار وزیر متن انتخاب کرده
نکته اینجاست که چرا اصلا فونت‌های پولی و غیررایگان باید بهشون اشاره کنه یا دروغ بگه
🤔</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/3874" target="_blank">📅 12:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3872">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ilMlBLKR7MITtC7JcPAu3g2h7bWAPG-x-7UXhwSBvH4OTxcYN66ruMRa5tdljvUGRqbdl3GF9QdKRxHHgNMKkghp-o4FLtMj5hiX61kh9RI_bCYb_cn51zM-5QycYWa63G30P2RodXc2VlGChwengiElsrRbme5WKKYGwzi90QfJTS5rq3L-TUoRot5ldecXEFWmZLx99lWXwMRw_dhKw-lL8kSbBGpiECn7lPD1jv1j12o7kyODaypcnctiqV9t8nPzAdd3itbHRFkoapR1r7KK-q9kAXsQUMD1yOHtfoXf_NQWaGt5a0JvMRpA5FjJwU2s9uXUuglTgJy6xwZDqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/paJPKp7DIVkNETQeIEpv8dPVFE_cJUxTozIVcfAKevM__worbHQnScumSEzD-9gKqJgP7Ui5_ypn3IMXTwDH0pWMTlMO6MLigTjPrq3v24Y_FqD-u665xDPUZM2N6x3HOaFnsSCcmNnYaP-zyoxnN4yjWHTEIBBI7RnJMKv0IJMn5H9bnBD4jEkydt-MRis5tZS-TnXmjoEyJ561sru2umVBMqC9UvmjDJz9dCQymew_5QCI2zBDZXunrOAY6zXj4hMaf89rytclKf0fTJWnmuPS71F8WkH7jV32cly3OBa1fEZq2ruQr9RC7fRobw4x2Y-qwj504ljxJspZZAfkXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم کپی‌رایت برای کلاد شوخی‌ای بیش نیست. اون از قابلیت اکستنشنش که کل UI و المنت‌های صفحه وب رو درجا کپی میکرد، اینم از این</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/3872" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3871">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NfUJGj-EXqvvROuhquIYVxMsiaIYSdy5aUVVP5LDfh2nlajewCnmt1TknAmHhKDzlu4cAmHOZqdIXh6HDlEFMxJ1S138NTe3oHjfQYtvu9jopiu7oEFnDiGjyghOFN18Eiu-V3aSY23VbTzz1rFHn3EnIBW2bBUBieYViXQUdkJNMhLWfkPDlvJzzifcbn5RNcNUGRMwggFygPQHOzca1v_2PdTQ0TNKN0K-GsqciOYEhvztSRRS2XjqfB9cdW4pLJGilR3gktzFAhstQidCQuQvSHTv9X09Zm6KC6G2U_p0bRhtO4DpvdZO-hv2mgxuFQtj_nFYiwxih8ZeYxMUpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/3871" target="_blank">📅 10:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3870">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/3870" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3869">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/3869" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3868">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/3868" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3867">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏
بدافزارهایی که با ترساندن هوش مصنوعی پنهان می‌مانند!
تصور کنید یک سارق بعد از دزدی، یادداشتی آنقدر وحشتناک جلوی در خانه بگذارد که مامور پلیس بعد از خواندنش، با خود بگوید «بیخیال…» و اصلاً بازرسی را ادامه ندهد! پژوهشگران متوجه شده‌اند در موج تازه‌ای از حملات نرم‌افزاری، هکرها از ترفندی مشابه برای فریب دادن هوش مصنوعی استفاده می‌کنند؛ آن‌ها بدافزارهایی می‌سازند که بخشی از متن‌شان طوری نوشته شده که هوش مصنوعی از بررسی هرچه بیشتر صرف نظر می‌کند!
ابزارهای هوش مصنوعی کنونی، ترمزهایی از پیش تعریف‌شده دارند. برای مثال اگر از آن‌ها راجع به نحوه‌ی ساخت «بدافزار»، «تسلیحات شیمیایی» یا «تسلیحات اتمی» سوال کنید، فوراً ترمزشان کشیده می‌شود و از پاسخ دادن طفره می‌روند. حالا هکرها متوجه شده‌اند که با افزودن این نوع از متون ممنوعه به بدافزارها یا نرم‌افزارهای معتبری که آلوده شده‌اند، می‌توان فرایند بررسی امنیتی کدها از سوی هوش مصنوعی را هم مختل کرد.
به زبان ساده، مهاجم سعی دارد کاری کند که ابزار امنیتی وقتی به بدافزار می‌رسد، به‌جای بررسی دقیق کدها با خود بگوید: «من اصلاً اجازه ندارم این را تحلیل کنم» و از آن رد شود.
﻿
این نوع حمله نشانه‌ای است از ورود به مرحله تازه‌ای در امنیت سایبری؛ مهاجمان دیگر فقط انسان‌ها را فریب نمی‌دهند، بلکه رفتار هوش مصنوعی هم هدف قرار می‌گیرد و ترفندها در گذر زمان فقط پیچیده‌تر و خلاقانه‌تر خواهند شد.
✍️
NooshDaroo</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/3867" target="_blank">📅 08:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3866">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOfI0HoTxapwcu432cuX3_WzlSo3Aep_vDSS978f9f93PpW9XcENQcWgIE2WeTQ17er8H-12oJU7x63nDBSIAj9WLnQy6e0koAPL2H1CS0LKdvX9S_REf0XT-CvPbsslYnH2LzmuhP077kij9nQz41DKI_Z43heGaYyv5NLIaGWfH6ZRTwLMEnwG8G9aqk_rbUTjklWJp3AIau0-lHpcelqZTSZZTNdktYLpKMWmmRiBRIi-N8fHvqPXmTYA8wx7uRm39d1TUoYgsi_F3RekabBIL_-CZh9RyBFLxD0pcbkNrv5bVxeeWARLYVlAe5kXjQC9ILMQZ_7X7gkoTWc7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید دفید قراره قابلیت چت با رمزنگاری e2e داشته باشه؛
باهاش میشه ارتباط امن با خارج و داخل ایران داشت.
کل این قابلیت با ریزالور ها کار‌ میکنه تا توی فیلترینگ و قطعی شدید هم وصل بمونه.
طبق تست های من یک‌ سرور متوسط با ۸ گیگ رم و ۴ کور سی‌پی‌یو میتونه تا ۵ هزار کاربر انلاین رو هندل کنه!
اینجوری کار میکنه که هر کاربر یک اکانت رندم واسش ساخته میشه که توی سرور های مختلف ادرس اکانتش ثابت هست؛
ادرس اکانت شامل ۲۰ حرف انگلیسیه که هرکی این رو داشه باشه میتونه بهتون پیام بده.
(سیستم اکانتینگش تقریبا شکل شبکه اتریوم هست، یعنی‌یک seed دارید که با اون یک اکانت ساخته میشه)
کلاینت هر ۱۵ ثانیه به سرور هایی که بهش وصل هست درخواست میده و پیام های جدید رو میگیره و تقریبا برای ارسال یک پیام چند کلمه ای باید حدود ۴‌ کوئری دی ان اس کوچیک‌به سرور بفرسته!
واسه اینکه به سرور ها فشار نیاد محدودیت های سختگیرانه گذاشتم، ولی همه این محدودیت ها توی سرور قابل تنظیم هست و اگر سرور شخصی راه بندازید میتونید محدودیت هارو کمتر کنید.
https://x.com/i/status/2065531715041239193</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/3866" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3865">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJ32wbhzWwLpsw5U_apNxCeh1_-EUyn1E0uPiMQiAEb3dRjwaroEuJMTcu92ySVlIZQ1GklXx1UY8d4dobpPA_uS2h43ZsXxieq0wPgDGU-Ua8GFmZp5YcGmZmXPgYw9R7LPeYFu-11mVmgQoKIvZelgnxKNDeUq0TrVEcB-4nIxjilDofhCTkRu6_kVDqJ6kOP-N1rjK0vbmRtVeq52pO4S13aHKQ64WRd7nbHf808OGfQwzxxiQYnegYH08awF4mqZ4kPBOAm5ugS0Q2h7bJdLoAuoKqCXvPSrVTRkrtYrNbr_PgDJL4Syl-s_0Ghv5FoycE4Ik0uaC1s1k1hAAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا به هیچ وجه روی کانفیگ Websocket معمولی سرور شخصیتون نباید اسکنر ران کنید. فقط روی Workerهاتون انجام بدید که ارزشی ندارن و ابیوز هم نمی‌خورن</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/3865" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3864">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">برای اندروید و ترموکس، کسایی که مشکل دارن طبق این آموزش دوستمون برن</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/3864" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3863">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">برقا باز شروع کردن به رفتن؟ خیلی دیدم امروز توییتر وسط کد و گیم و ادیت و... برقشون رفته بود</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/3863" target="_blank">📅 17:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3862">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مرحله اول  همه بخش مرحله یک  رو کپی و توی ترموکس بذار
pkg update && pkg upgrade -y
pkg install golang git -y</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3862" target="_blank">📅 15:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3861">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/3861" target="_blank">📅 14:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3860">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نمیدونم این کانالای تلگرامی چه گیری روی ری‌اکشن دارن
میگن ری‌اکشن بزنین انرژی بگیریم. انگار از ری‌اکشن برق تولید می‌کنن
عقل ندارن راحتن به خدا</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/MatinSenPaii/3860" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3859">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم
پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/MatinSenPaii/3859" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3856">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ml8C2yGiB3n9Rconl0E-aDJaFQCBwAb8zokNVAeOiM13fGFU1gmlD15oirM4WdgVIfKbybbqfW5TLveH332Izyr7rTTQYtRu6ZPuvkrNyLNw-DP154TgNBavnFZuEoBvOIjPE9koamHTSoDGWR6XM7L4l3rfU4pauO-P9Eh2bGd0Wl871mGQos_Rzwz9enNmzmet0ORbcdwT1mEGiHpfnJGpHH_wkWn1KAkq9DKv8AK5W04hQW6J_aRmWho3o7WyS6z3RZ3Oj-yjZ-JcjKOQFSaYfoMwxvqLpV2yo_szQHkKoxv8chiMQTItHzFtOSCRzAokdXzGsbbFqcpHe9tJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oVm2eyq8-quIY224joUEDLHTXS-0lpub2MlDsC4Pv8732MoC1IIXKojr-4vTzgqsXa5m59QlPi5p-bnxr1Nd4Yghe_vjUWBo9kK7RL5N7yy_Y5ThOvi_azXRy64iVHuXKS7cfs5HYHWabxGrm1RVXyFvUX86vsar1ZemeHfQ1RaciEgT4RlG4-CkcgYX4s_qFmFpUnDA9ne-sjPSZPaK5H5RkhtvurgOegitoAVLETfC7SLRlUFBOvg3omPCaEXaaFlhYN1PDTAfgxTVhMfK7svfELmIuCAk8aF6c-8lbfrFzuGcwVaXBz9vccEmb13T1eXDyKnxeMl6bRZk3v8cKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OPFIMg8cdeRMzEvL2O0-r19KrS_4FpdFxjA1uDEC-set_dbLn1-4mgeVCnT69WycY1di9UKXIFD7hf6XTmz1lWnrF2XNAn2I98IovuN4sOZ7rERvHstWDztkQejaDAuvFzPFGIUoHhwRh1Vz7ySYL-gYiGHelGyCrfEDQVCp9Wb8Jk9dVjOKRHmoXQ3Tf0myh0jXppZrxzKysjnViV64Vkw0INxmC-NlnVrrn3ufxaU_6lzwpKhOmKg2U-aQE1pOl6GBj56rkFiDe4K2Xo4PulQsBTdcjKdyl_sEkxbzD5opWj61zLSFAx7UJrqtVibnS3wp3sQiSulJIW5CrAIzmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن 0.7.1 از SenPaiScanner منتشر شد
✉️
😏
پروتکل‌های جدید
: پشتیبانی از
Shadowsocks
و
VMess
اضافه شد — هر دو از فاز ۱ اسکن تا فاز ۲ xray کاملا کار می‌کنن.
🧮
خروجی چندفرمتی
: با زدن
e
بعد از فاز ۲ می‌تونید نتایج رو به سه فرمت صادر کنید:
1- لیست Subscription
2- Sing-Box JSON
3- Clash YAML
🔥
تنظیمات سرعت
: فیلتر حداقل سرعت، تست سرعت آپلود، آدرس سرعت‌سنج دلخواه، و سایز sample قابل تنظیم.
🤖
ذخیره تنظیمات
: تنظیمات اسکن ذخیره می‌شن و گزینه «retry last scan» هم اضافه شد.
📚
پشتیبانی از CIDR
: حالا می‌تونید توی
ips.txt
، مستقیم رنج‌های
/13
و... بنویسید.
📱
اولین نسخه پیش‌نمایش
اپ اندروید
با Kotlin و Jetpack Compose اضافه شد. معماری MVVM، تم‌بندی کامل، و ساخت خودکار APK از طریق CI/CD(هرچند CI/CD باید روش کار بشه هنوز).
لینک دانلود آخرین نسخه:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.7.1</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3856" target="_blank">📅 13:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3855">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دوستان، این شکلی میتونید به من پیام بدید:
https://t.me/MatinSenPaii?direct
اما از اونجایی که دایرکت به شدت شلوغه، و من پیامها رو اسکرول می‌کنم پایین، ممکنه گاهی اوقات زده باشه سین شده، اما من نخوندم در واقع</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3855" target="_blank">📅 12:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3854">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حقیقتا MiMo اگر پلن پولی بده، خودم اولین مشتریش هستم. توی تسک‌های متوسط Backend شاهکار کرد امروز
هم توی سرعت
هم توی دقت</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/3854" target="_blank">📅 12:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3853">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هم پشتیبانی از Trojan و Vmess و Shadowsocks اضافه شده
هم تشخیص ISP
هم تست آپلود و شخصی‌سازی تست دانلود
هم WebSocket(که بهتره On بذارید)
هم هسته رو به کلی بازنویسی کردم
و این به کوشش دوستان عزیز برنامه‌نویس دیگه هم بودش که اسمشون توی Release note میاد و contributer پروژه هستن. من شاید 20 درصد از این 10 هزار خط کد که اضافه شد توی این ورژن رو نوشته بودم</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/3853" target="_blank">📅 12:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3851">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rinqtTFzk5Iqui3_HcHhinEGzUmPIT-8iBfGyxLmL0OuASr-nH6SkO6xc16jy65_TXXRKr5CJILP1bV3YlmOue7YyzdclprluEg2cacsFYdRtjDhEYv_4QmuiagNYeH2W5UH8jy8IV21de-RuuT8yT5YEgMA-obNSj6VtgiW3MnYRomtFd6smcTXKgeYCYUonNCEw8Wv_RR5_jtFhb1sfIUyscN9BWKdq_7fih6p6myjF5LlXxhATz_Zv_nA7jaKZg29LLkiLyU1IAyzR3SWVNoxNTCpVJA1RImt7GFb00kXPptqbCHCKAwcJuf5RBO7BTXwF8CMYrXAEBV12uD5mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ncsQYAiEqeoJA8kprEvmAtCzrYcBoigjkyLlOyEH_DG9U9Dya5Vm9dypj320Ib3qqaHIXxiQKiJURhB7wVfBFcxkzC7N5asBfKi0x4U4GKwIP6Zt7LFX5oaE1hxg0hQv5X8IABTYFf_zjVj4Q2qavEoYuaNeImyIexuMSZFHUBZbRv3wqEGYpasdjv_SEwqtDSEwQ859Q_jQ9xS-IM7UB5PbNrHXQtNZA2pg0HI7se-OA0HSrCwZSIuU2bZP7psrHvR5_hi5sF3Nk0xfeqVw1a50n8txE0abk3X-2ZIu-jKHgiMTi9cmrY9i-8sdHSIs6seiMe2-40_agJn_arXnnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/3851" target="_blank">📅 11:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3850">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KpQA3ren5ID0C45unLV9lKERAhCWL1eD2FwWiaHK_cN9cBlbUZvOAAEpMUClgvEktRu-VyIrSdVEYrTfIu-WDXEOSTzSgI6OGRVLVCAFgVkcVVNRZtRiRtRhUel5Vav3m3VlEizz4FcKmBbDUf5vIy0UaCd0oXsKRXINbZ09JFJZnVpPRqv7lK-044xgVlSOjuMWLeUGK6JGlFcNZUWpRwkNKNl9wYqv2v_n8cfUI7YxCEL9ETvN2IrP-CWLzfkWEYdlwy_4aQAj_rCGKnTKm7hhtbZ5xbCUMXsADkOwIMRBaniv7wjHOea663qswiRVNyGJRTWu5AfApoRz5x_-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/3850" target="_blank">📅 11:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3849">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/3849" target="_blank">📅 11:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3848">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/okfpIO1-Ts9XJIlBnfOP08qdQMuOYEDOJBP3XNrZ8C9U2aUUQrCI3nNfZbILZow3TEph4enSEEvAtS4IS7G62h8NjP9Hzy5TfKk3Wrlnd8k0RjsCjJ8U12Fl1fM88JZ1fibwnB5lLpffEpRDknfjjyZXhdMGlrizNDjcy0m6nmUbvmt8KwfyMeBmfPKA79drN1j-zt4WKnaYnVm50pgY2b45f7LMxFa1djYDWxHepqcYm7hKQ7OXvKOnSANQaZ76eKQaK5L7GQNqRDRpjMPjgp9GmuWS9ZFrADJMo1f5i4NnIVYU55t19zeEUzjqKG3t0OR9wV3vKL0Hk1iD-_f3Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان خوب، لطف کرد و هسته‌ی اندروید و تمام چیزی که برای ورژن اندروید نیاز داریم اد کرده، صرفا منتظرم که خود اسکنر عملکردش به بهترین سطح برسه، اون موقع نسخه‌ی اندروید هم بیلد میگیرم</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/3848" target="_blank">📅 11:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3847">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نکته‌ی خنده‌دار اینجاست که دولت آمریکا دستور داده دسترسی به این مدل‌ها برای هر فرد غیرآمریکایی (foreign national) — حتی داخل آمریکا و حتی کارکنان غیرآمریکایی آنتروپیک — مسدود بشه!!  آنتروپیک اعلام کرده که چک کردن ملیت کاربران به صورت عملی ممکن نیست، بنابراین…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/3847" target="_blank">📅 11:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3846">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/3846" target="_blank">📅 11:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3845">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/3845" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3838">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">32 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خب، دوستای من هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/3838" target="_blank">📅 11:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3837">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خب، دوستای من
هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/3837" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3836">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VRctQWe72vrun2gENooOJTMeYvsVJm703jH_r8X-wH8SUn_FVI5UT975iXLFf2ZBaZVXJlx7F1kJaz2f6eAsCWMum2V_rMrDfEjaG6t4O5g7sb4ks3fmyRCtIw4_PeUH6OTXvXJltOBsZeAYFIGl93EjxPl2GGHgL9Sec8IO6lOGnC96yKMsGYDWE2TJkuypg_kTSBr_TfCcZUC6X8zXtuA628-JRR2t-3uvW4Ybu5-lb11y8__toa4B9KLaR6YCVUjCY8Cu2tIxovzr3zJRJzlOTS73Y3NVvtifq2UMcsLVmJCZAfFbWJuv_inrcddIGzm6kC0yt-Yl4NyOun8VIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لپ تاپ اوکی شده الان اومدم تست کردم MiMo رو و خوشگله یه تست پرفورمنسی بریم باهاش روی SenPaiScanner</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/3836" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3835">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xj7twe-WIp9kOc2-jiPY5rinSX2iuFYL8FWFOTfCmb5i45l8obJ7CbrhnA-U3UI-2SciASxDkWaLET27m0eDQcnTyKxT2hbDYyk8-AiGtAXIprnH2ugDpLlUM8uVOr9irUXYNKKh-ANpt6TzWtzROUnIrER8WkCxu42GD0-R_tbP9GGndIZBVA7JbXbitxKV6EAkXxPnyuME5jAFc8GY-R8qPmufva6otXAtfSzT1nYiGVRZUfOWxgjmd2B3rTnu-69QbOcOz4cmUH06RQcLhgy99v4eaOiM3lgdrrB3BDBDxMyncoYUgHLg76aPLuxtKk9gxs53kfo3jkd2uvqXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/3835" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3834">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/3834" target="_blank">📅 09:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3833">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UWWIJIxzeurgtYPEIIjvYAIH97v2uzhVgJpAzoAzfcTWVFRcDQqpkSzu3eRiqwR6Y4AF0053MSd_Anq-tns1mHRQmSoMYGNmz2nLu5tNDoAcL9soA3pUWfEqjTV79s9keYVEPYv5m-mVdNQFs1-JoLsGbVp4un_qZt0d4-_JKlbUnhJsG8UveWpxHjQxzB9G1smtPLxiffuT0A-Gk4exI_K5frOKjlzS3HCvdgFpgMBIA_i6lC7mvqL67-VqMwYpZYT21dJKOYmXHBy9RHkQS11MX7NQYJIajFMdgNXMVCO8eHB_SBCSQoHo8_QWYkQjY5yaIDMB9KZH_8uQqAoqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/3833" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3832">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید http://l53.net/</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/3832" target="_blank">📅 02:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3831">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DpwOFgL-aHRzshZ47rlkaCWEHwZ5APJvkkCk4CTmcDQGLkClGjUqEUPZK-I2EF9aRbKlsenyQ-DcI29-DJwvfhMaBGhg0SWImlMX97pqXp-1vRH2IxuByt2jQYOGnYLHpMXcspAtYGsPayhvddVs-Uwb4KkJLTxe5W9zaSjEG6BQ0mFrXEhNWVUByKU21LxvqpUJ6n3wLqKIx-iAhRIG6vAfWUH9VwmB8tmKolbHdVfhbNcW1q8mULOWZbRW84tf8DGKDGOZJGahtWYscrMNMgf3A_bxG_PayCf_JLywWO-1oDeCKu8SkatuyT2A9c9YDPQWsU3iLmXFKSHthnG3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید
http://l53.net/</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3831" target="_blank">📅 01:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3830">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">من شرایط ضبط نداشتم دوستان. یه مشکلی هم برای لپ تاپم پیش اومده که باید بدم تعمیر و ممکنه کلا مادربوردش بسوزه اگه روشن کنم ترجیح میدم ریسک نکنم چون دیگه پول ندارم بخرم
😂
تعمیر شد، آموزش‌هایی که قول داده بودم رو ضبط می‌کنم</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/3830" target="_blank">📅 01:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3829">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWireguard Configᵛᵖⁿ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=cUHH6aMY5d4Dh8VUnwCqU5qLGGKjchCXOzwiZCEy_Jcw8E6dX5dTWdzU6-ghM_PZ8oPlabYXHnVjN07Ne2g7FJpAqvZYoYVvHoXVqxiS8BjJ9nh1-AVKDcnbY1HBw-gb95RAtErugDcicCwJapKPs3iUUwQKaMVsKiY_jsSgvr66nr1XVbO4Z-ln_djNxRwX8lotmSBrcoXInb23Rj3DO50sjqOi0bXhYujqLfLr_hjJXzLUW_3TBVbkDGsH3q67bcuGhXhWj3FJiJEq4AKGCLtwaXvLPIdRwzxOhYnl9gTiLVhcUJm2_7jkMcwTh0XbVLPFxQ_3c-w6R6o-jkUQNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=cUHH6aMY5d4Dh8VUnwCqU5qLGGKjchCXOzwiZCEy_Jcw8E6dX5dTWdzU6-ghM_PZ8oPlabYXHnVjN07Ne2g7FJpAqvZYoYVvHoXVqxiS8BjJ9nh1-AVKDcnbY1HBw-gb95RAtErugDcicCwJapKPs3iUUwQKaMVsKiY_jsSgvr66nr1XVbO4Z-ln_djNxRwX8lotmSBrcoXInb23Rj3DO50sjqOi0bXhYujqLfLr_hjJXzLUW_3TBVbkDGsH3q67bcuGhXhWj3FJiJEq4AKGCLtwaXvLPIdRwzxOhYnl9gTiLVhcUJm2_7jkMcwTh0XbVLPFxQ_3c-w6R6o-jkUQNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سا
خت کانفیگ Amnezia VPN
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
🟡
فعلا روی ایرانسل
💯
جوابه(همراه اول ،مخابرات،سامانعلی)
📍
ای پی جدید هم اضافه می‌کنم
https://darknessshade.github.io/Amnezia-VPN-Config/
@ConfigWireguard</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/3829" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3828">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کلا فکر کنم ساعت از ۱۲ میگذره دکمه‌ی بمبارونشون روی سیریک گیر می‌کنه</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/3828" target="_blank">📅 00:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3827">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QxtME0qh_8wxuBFAbueZ1HvhiFA75dhgUqXUkiIQw6bqQl_v0c1g7nt65IYQLNjeUXLmxJ3_i-Y1omX1fFVfX_ai2gaSXdAFnwwjaCI3kE4l0r22gDYBzlYDL0ih4-ac6taZAWItyDMnfbeUWDIyXQxN9lVnoQ3Z1hfb0i-GLojIM1ZVdW-uIDpYtJ-HgMHLP046HAGRhSe7_axNEzg9-iKf9lXINYl6F2OfYubmJl22909HSdm0rFyniGC1M6u7Ort_K4VlxSuSQAViiIBd_Bd23RfPyPhuTEQAuH5OtN0IvZWud7t_qi_NsGxxZjcVzDyvq5X8BYNISCK5xG8ing.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3827" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3825">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اگر مشکل باز نشدن توییتر با پنل BPB دارید، همونطور که توی
ویدئوی تنظیماتش
یاد دادم، NAT64 یا ProxyIP ست کنید. اگر باز هم نشد، صرفا کانفیگتون رو عوض کنید با چندتا کانفیگ تست کنید، درست میشه.
proxy chain هم صد درصد درستش می‌کنه.</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3825" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3824">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CflnGrM9wkL_znh2e5ejgwutoTrbA1scKVGxBwR_AAOXK1EvHBPXqsOnDJG6ISdxw5Bagqol8OSJvJnz5PhwVKlI5EnLNI9C0E8RfDvv2l9cTzR5rQ3bO5qaJQYxCqCr1LInQ0RNvw1zCOe4AobLzWXvmPirWPh2otbsJ7LtAq9DxAxx-nzbAQK4L2BcU5hBszqudQZlw_BE8VOttJdAA0HLfequZiIdF6AAz-ylcrOaFIEBaraFzyBMV_13o5uzuS4vjqAsvTBEUNA4WjgRxWTBYfuUo9RbE5tN_HRE7_dXnQEDvZhE7cmB3ftdBziFrynadx4HsSrON7rU-28B1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد
توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش
فورک OpenCode
هست!).
خلاصه‌ی ماجرا: تیم MiMo شیائومی به‌تازگی، دو روز پیش (۱۰ ژوئن ۲۰۲۶) نسخه‌ی
v0.1.0
از یه
AI coding agent اوپن‌سورس
با لایسنس MIT منتشر کرده که توی ترمینال کار می‌کنه و برای پروژه‌های پیچیده و
long-horizon
(بیش از ۲۰۰ مرحله) ساخته شده. این ابزار فقط کد نمی‌نویسه؛ می‌تونه دستور اجرا کنه، با Git کار کنه و در طول جلسات مختلف، درک عمیقی از پروژه‌ت رو حفظ کنه.
از اون‌جا که نسخه v0.1.0 هست، طبیعتاً یه پروژه‌ی اولیه و اکتشافیه — ولی معماری‌ش جدی و قابل‌بررسیه.
ویژگی‌های جذابش:
۱. حافظه ماندگار (Persistent Memory):
برخلاف ابزارهای فعلی که فقط به context window مدل تکیه می‌کنن، اینجا یه subagent جداگانه (به اسم checkpoint-writer) توی پس‌زمینه کار می‌کنه و تصمیم‌ها و پیشرفت رو لحظه‌به‌لحظه ثبت می‌کنه. حافظه روی
SQLite FTS5
(جست‌وجوی full-text) ذخیره می‌شه و توی فایل‌هایی مثل
MEMORY.md
،
checkpoint.md
و
tasks/<id>/progress.md
نگه‌داری می‌شه. وقتی context پر می‌شه، خودش از روی آخرین checkpoint بازسازیش می‌کنه؛ یعنی دیگه نیازی نیست پروژه رو از اول یاد بگیره.
۲. ویژگی Dream و Distill (خودتکاملی):
دستور
/dream
به راحتی جلسات اخیر رو اسکن می‌کنه، دانش مهم رو به حافظه پروژه منتقل می‌کنه و موارد قدیمی رو حذف می‌کنه. دستور
/distill
هم کارهای تکراری رو پیدا می‌کنه و تبدیلشون می‌کنه به skill یا command قابل‌استفاده مجدد. هر چی بیشتر کار کنی، بهتر «پروژه‌ی شما رو می‌شناسه».
۳. قابلیت Max Mode (آزمایشی):
چند راه‌حل موازی تولید می‌کنه (best-of-N) و با یه مدل داور بهترین رو انتخاب می‌کنه. که با
experimental.maxMode
توی فایل کانفیگ می‌تونید فعالش کنید.
۴. قابلیت Goal Mode:
با دستور
/goal
یه شرط توقف تعیین می‌کنی؛ وقتی agent می‌خواد متوقف بشه، یه
مدل داور مستقل
چک می‌کنه که واقعاً شرط برآورده شده یا نه — در نتیجه جلوی توقف زودهنگام و خوش‌بینانه رو می‌گیره.
۵. ویژگی Compose Mode:
با زدن کلید Tab فعال می‌شه و یه workflow ساختاریافته برای توسعه مبتنی بر spec ارائه می‌ده — با skillهای داخلی برای planning، اجرا، code review، TDD، دیباگ و merge. کل چرخه از spec تا کد نهایی.
۶. ورودی صوتی، Git و Multimodal:
ورودی صوتی real-time با
/voice
(بر پایه MiMo ASR و TenVAD، مخصوص کاربران لاگین‌شده)؛ مستقیم با Git پروژه‌ت کار می‌کنه و multimodal هم هست.
۷. سازگار با Claude Code:
authentication، skillها، MCP serverها و دستورهای قبلی رو توی یه مرحله import می‌کنه از پروژه‌ای که داشتید با Claude می‌زدید.
۸. انعطاف‌پذیری مدل:
MiMo Auto به‌صورت
رایگان(1 میلیون توکن اگز اشتباه نکنم) برای مدت محدود
و بدون کانفیگ در دسترسه، ولی خودش هم از هر API سازگار با OpenAI و prov/erهایی مثل Anthropic، DeepSeek، Kimi و GLM هم پشتیبانی می‌کنه — یعنی vendor lock-in نداریم.
نتیجه؟
طبق ادعای شیائومی، توی بنچمارک‌های SWE-Bench Pro و Terminal Bench 2 (به‌ترتیب ۶۲٪ و ۷۳٪)، با همون مدل پایه حدوداً
۵ درصد
از Claude Code جلوتره(که هنوز بعید میدونم. به چینی‌ها اعتماد ندارم). اما می‌گن تفاوت واقعی‌ش جایی خودش رو نشون می‌ده که کار طولانی و چندمرحله‌ای باشه — نه «له کردن»، ولی برتری معناداری توی long-horizon.
نحوه استفاده (خیلی ساده):
۱. نصب یک‌خطی (Mac/Linux):
curl -fsSL https://mimo.xiaomi.com/install | bash
(بهترین تجربه با iTerm یا ترمینال VSCode)
ویندوز:
npm install -g @mimo-ai/cli
۲. اولین اجرا:
خودش راهنمایی می‌کنه — MiMo Auto (رایگان) رو انتخاب می‌کنیم، با حساب شیائومی لاگین می‌کنیم، از Claude Code Import می‌کنیم تنظیمات و... رو، یا خودمون می‌سازیم.
۳.
می‌ریم تو پروژه و کار رو بهش می‌سپریم (با زدن Tab بین agentهای build / plan / compose سوییچ می‌کنیم).
لینک‌ها:
- گیت‌هاب:
github.com/XiaomiMiMo/MiMo-Code
- سایت:
mimo.xiaomi.com/en/mimocode
- بلاگ فنی (درباره long-horizon):
mimo.xiaomi.com/en/blog/mimo-code-long-horizon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3824" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3819">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CYEuFwmaO2qXJoMwjkeQ_GBOw3hVD6EIaqopit3uFU1-Yy4Ohllm9kKwTtMjeuPqxfgTIszYmbSqBHDTwS_X06wHOaGsrdzHlw9GBfybpAotF8gMLRiir3eYcTcPkY6rERkxtSgtlMeLSWlfwwDuZY2MmGKbZg-aCHlbdAUkuFg8L7Y8A_Q7aH2DALLjK4Rkj-DxEyw069JuhMa7usQiwzPLaEnpe8DEMqr_59MwQHXiJtyT_ETLvGNkTtwUylYclWyfxVJJIetZ3IwPCMtrdZ13dQpayYg3WXchpWCMfBspB79OFE3tvIP-1coOAmEcGP0TqBWxR4Jj1l92057UsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از ChatGPT بپرسید که
یه عدد بین ۱ تا ۱۰۰ انتخاب کن
بهتون به احتمال زیاد میگه 73! علتش رو هم از خودش پرسیدم:
وقتی کسی می‌گوید «یه عدد بین ۱ تا ۱۰۰ انتخاب کن»، من واقعاً عدد تصادفی تولید نمی‌کنم؛ بیشتر یک عدد دلخواه را انتخاب می‌کنم. بعضی عددها مثل ۷۳، ۳۷، ۴۲ یا ۶۹ به خاطر الگوهای آماری و داده‌های آموزشی بیشتر از بقیه به ذهن مدل می‌آیند.
جالب اینجاست که در آزمایش‌ها، وقتی از انسان‌ها می‌خواهند یک عدد «تصادفی» بین ۱ تا ۱۰۰ بگویند، عدد ۳۷ بیش از حد انتظار انتخاب می‌شود. مغز آدم‌ها از اعداد خیلی گرد (مثل ۵۰) فرار می‌کند و به سمت اعدادی می‌رود که «تصادفی‌تر به نظر می‌رسند». من هم تا حدی همین سوگیری را دارم.
پس اگر چند نفر قبلاً همین سؤال را پرسیده باشند، کاملاً ممکن است من دوباره ۷۳ را گفته باشم
امروز توی توییتر اینو دیده بودم و واسم جالب بود علتش</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3819" target="_blank">📅 15:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3818">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NLZUe0ODhDCHS0dgfujTDj7WFpyk_GgP_WIa7WZ_VWgaGm7BIKE069zAw2mEYG8ZJxlyaK9WFhiF57t6AwVCt0ZsiUWz8bC0WgwNAXuGpWOcaigHzIXNYyDduYwrG8Ib1lK2WaaMz9ocOKyRW0aAVd7xOcahJTJD1Inwn6bqtv8AMTANLohRt1sdb7-4vOnoTEVbOR1nGrLGXtFrsmxeoR1rwXSnUSWHWeor-e2GMPMAu9RELHgqGWUJANaogdTWnkgmOVhlYg-W-ZnCPxmxpJ4hcVfBW4ZasRIu0scf1Y5NnQ-tXRK4GfN3OZcYnaa-WFjy_xgRtJ27J0LZLVdoKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار باحال آنلاین پیدا کردم: یه عکس می‌دی بهش، بهت گرادینت میده با کلی تنظیمات.
برای وقتایی که دنبال یه بک‌گراند یا پلت رنگی هماهنگ با یه تصویری، عالیه.
تو مرورگر کار می‌کنه و رایگانه
👇
photogradient.com
‎
✍️
Reza</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3818" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3817">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا
ابزاری که امروز معرفی میکنم...
داخل این سایت میتونید تمام ip های مربوط و بنا بر نت خودتون چه برای ورکر و کلودفلر یا شیر و خورشید اسکن کنید
❗️
ویژگی ها:
💡
اسکن راحت و سریع و دقیق
رابطه کاربری خوب برا همه سیستم ها
داشتن ip بیشتر cdn ها
لینک سایت:
✅
https://cdn-scanner-pro.vercel.app/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/3817" target="_blank">📅 12:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3816">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2658a29175.mp4?token=bR4y0NcUKyZR0QFM_4pbsJkxGdEj9Q5CJdjlwi3eOtg7lrBd4q6yJvxgaHGzv9eBr32A2wmC2qjMembHtTElXqS1IYHDuGEnQVM_mCq8gwiMHfGFev1Mh4Q5wu5M9ovNwzTELRqPtBq-fs3WwQ8YwnWcD1I4axFD-ieR5kenUBI5djAIgE7hLYowoTRrkQ3Yt3ahET5_HvsrKq8ygmIczRTNjjtCfPHtv35tcuIFdeqzzwi_6ROJA7lTddTBdhg09ww6JzHm3EkLfvGKaQI1SPZXgNtNmFqHl6Chvot2NS8Kd8ADeYsp-RpNpoT2qluGsMF8H_7wNjRwQKvFef2Krg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2658a29175.mp4?token=bR4y0NcUKyZR0QFM_4pbsJkxGdEj9Q5CJdjlwi3eOtg7lrBd4q6yJvxgaHGzv9eBr32A2wmC2qjMembHtTElXqS1IYHDuGEnQVM_mCq8gwiMHfGFev1Mh4Q5wu5M9ovNwzTELRqPtBq-fs3WwQ8YwnWcD1I4axFD-ieR5kenUBI5djAIgE7hLYowoTRrkQ3Yt3ahET5_HvsrKq8ygmIczRTNjjtCfPHtv35tcuIFdeqzzwi_6ROJA7lTddTBdhg09ww6JzHm3EkLfvGKaQI1SPZXgNtNmFqHl6Chvot2NS8Kd8ADeYsp-RpNpoT2qluGsMF8H_7wNjRwQKvFef2Krg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیگما یه اکستنشن کروم منتشر کرده(فعلا برای کاربرای پلن پرو) که با رفتن توی اکثر وبسایت‌ها، می‌تونید با یه کلیک، تمام اون صفحه‌ی وبسایت رو به شکل فایل قابل ادیت فیگما دریافت کنید.
برام جالبه که سر بحث کپی‌رایت و اینا کسی بهش چیزی نگفته هنوز
😁
اما خب گویا هنوز با چنگ و دندون قصد دارن نگه دارن اکوسیستم فیگما رو بعد از اون سقوط سنگین سر Claude Design
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3816" target="_blank">📅 11:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3815">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!  همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.  بعد…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3815" target="_blank">📅 10:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3814">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uRsEjqM1MAVM7t0VmtJIf-e3Z9P-x5SHHv10amWvlQByvgwvDO7KrI692tenk8CyLjyNX87PzP3PPpXG8J3e7kBOmemLjGob2s3O_siw2ulL8S8PQ1ZJDr4-S_k0rMPmmvPfDaIQ5e1Br4KpzCRYw-cY47NWvBAA1M89DJlVTdwNIL9oDHoPt_acBO_lcD3saS4GLYxltcCrpVoEYb1hkbkocyyiae7iKJ1Jd2bNfGxJVOw22wDqxcjTz9exF7tOPG4bXcQ6c4MVPe-8Ovzl38VfRL9LhMe6L-8he7OMIXnm-AO56jbmEOYcfdHZGbUc7DqqGnDpRfqqixABeiwhKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!
همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.
بعد از چند دور summarize کردن، نهایتا بخشی از دیتای مهم از بین میره و تسک به صورت کامل انجام نمیشه! پس اومدیم یک سری تکنیک پیاده کردیم مثل تقسیم کار بین sub-agentها تا از پر شدن سریع کانتکس اصلی جلوگیری کنیم.
بعد این ایده مطرح شد که بیایم هدف نهایی (PRD) رو تعریف کنیم و اون رو به تعداد زیادی sub-task تقسیم کنیم، بعد مدل رو در یک loop بندازیم که با هر بار اجرا، یک context و یک prompt جدید داشته باشه و بعد از هر iteration چک کنیم که تسک به صورت کامل انجام شده، و در غیر اینصورت چرخه رو دوباره تکرار کنیم!
در واقع به جای اینکه برای اتمام تسک به مدل اعتماد کنیم، ما در یک لایه بالاتر این رو validate میکنیم و اجینتِ تنبل رو harness می‌کنیم :))
✍️
Amir</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/MatinSenPaii/3814" target="_blank">📅 09:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3813">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SeFSS6sNVKaUj9faDJxuCI96ccVlSDCtGRLoIeqSsG2ffHUd2uXY7zABYB_4DY-gVnI9cgSt6jtY0pg-_bCpfJl_7_cOI74zw-HoEZdVjOs8e0gVSuoEWWxfl5cN7xayGFtfPeLOss48auEfpLieqPZZOmGmo3dG3MJGllo6jQGptHMc3r5ZWKBaLLP__Xu1LMXOE0Js6-AdA5kfIJLxbKx7oOWKV6x3wAOaEG2hTbM17E-UwypRnfGvy2q2jbya63r7cfWUct1TdSCxheHpQKRk-mF8BgDQqy_tLzAfEuB2wXjKMzGRLNDpxs2_JKYd063UGg-goEhrGbjZz2_IMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله شما می‌تونید دامنه و سرور خارج رو از سایت‌های ایرانی هم بخرید، اما چندتا نکته وجود داره:
۱- احراز هویت سایت‌های ایرانی کلا جالب نیست و خب این ریسک رو باید در نظر داشته باشید
۲- توی شرایط قطعی، فروش دامنه و سرور همه‌ی این سایت‌ها میره روی هوا
۳- شاید عجیب باشه شما اگر از سایت‌هایی مثل netlen و با کریپتو خرید کنی دامین+سرور رو، شاید ۸۰۰ هزار تومن(با کارمزد و همه‌چیش) پات بیفته. اما همین دوتا رو از سایت ایرانی بخری زیر 1 تومن نیست</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3813" target="_blank">📅 07:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3811">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نکات استفاده</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3811" target="_blank">📅 01:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3809">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o1qSDkK53YCTXOZrR97lYViwbxdGGNpxDsRRQteLSk7J2ozIrTUUkKABLDoUVaNTLvF5Qa5aM8UMB2n5T4kANDOjsQvo_OI6oz5lVmwXCg2oKgJqgw31CFzJDS40WIuHI71VWsV275vKIMwvOkKDatqxKSQWLIdkL0XJEvYkXK3x45K2KpDoE2N2ainKjchy3rQbDuDqggLzS43nWhsV7FD1s1ryAJoIoc4AwLydTB1ImKYbdo9xvVhSi4Eye7eNqQyedloOW9vczrhdjP8uLUreI3XTgKPDjlKF_L-_MM4RF4hIJBjU0dKSVl_NcBCswl8LXV2--0J4tFXJJcD0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran  * دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)  ///  * حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)  * کافی است لینک subscription را وارد…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/3809" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3808">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/3808" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3807">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B6Wj8vK5-vKztjKk7ciPl2j5_cBBJO6TN7pT2-B4sWuAaGi4sgslwtT_84f1IQDBVkwNPnpg8MGh4r6SfVH9gFMMDJ9JFSEUjgmSOWQwLuEwMt3wso5j5pwUqSGhYkiaUYMcymrK8dWuMHjx5bNt5mc4Abi9tKYX_ZnafAlHbcxTAmYwrBzm-BCsD9lzauyfDkZ6wpIRBsIOq7lx6kE_OD3p-ThnRJy81Vek5f4Vd0T027BZyS_IFVRZF8JcpTkAIA5-hoZ9qQ2HKWZDguRUt1jEvcLpkQtHahLc565uUbimLHCNnHlV46tf0LSqyGNwOXAGyPZipSPugDaDUs0sAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از http://Netlen.com.tr بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰ باز هم خود دانید</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3807" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3806">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">درود به همه رفقا
🍷
اگر از پنل bpb و... استفاده میکنید میخواید ip ثابت باشه ولی جز لوکیشن آلمان
🇩🇪
میتونید از ابزار زیر استفاده کنید برای ip های مختلف برای مثال:
میتونید از ip چین استفاده کنید برای دور زدن تبلیغات یا از ip آمریکا برای بیشتر هوش مصنوعی ها خلاصه این ابزار مشابه واسه خود bpb برای ثابت کردن ip هست ولی با لوکیشن بیشتر
❗️
لینک پروژه:
✅
https://smart-ip-scanner.10-354.workers.dev/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/3806" target="_blank">📅 22:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید  محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان»…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/3805" target="_blank">📅 22:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1AvyDrGZFkA8a-XHszgTTR_Ovq6o3CMvBTW77gI1lKopuRNDjZoEH-UC-Wz-_E7lm5dWSbUv2V95ejYYQTIbeL3EDO22O97YsC5pW5NuAEdvG4qbKAw7cBSiizbh3nuMoH_zsermGK7dHJD3vZYge3awSMBgZR6LyK59QPty8KXS49aVaIdSgFJTAsKaUG5Vn4CNBVefej7VgeeyEfxankwJqqXgaTFoRBVJGDXfY6_Ki8UcpuMzDGPOxV9gXNM7myTYYuKdv1gMe9_EXIiTDxhz3J_RBmsYurQjWdNSsdiFRGrb1BkfRILBWXDqJ2FpHrDAvtUUKYO_K28EVJRfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید
محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان» (X-VPN) است که برای نصب بدافزاری به نام STX RAT روی سیستم قربانیان استفاده شده است. این بدافزار می‌تواند رمزهای ذخیره‌شده، نشست‌های فعال و اطلاعات سیستم را سرقت کند و به مهاجم امکان اجرای دستور از راه دور بدهد.
در این حمله سرویس ایکس وی‌پی‌ان هک نشده و کانال‌های رسمی دانلود این برنامه سالم هستند. خطر اصلی متوجه کاربرانی است که نسخه آلوده را از منابع غیررسمی (در این مورد، یک مخزن ناشناس در سرویس Bitbucket) دانلود کرده‌اند. در پاسخ به این تهدید، ایکس وی‌پی‌ان به‌سرعت آپدیت نسخه ۷۷.۵.۳ ویندوز را با کنترل‌های سخت‌گیرانه‌تر منتشر کرد.
➕
نوشدارو پلاس: این هشدار مشخصاً به نسخه ویندوز X-VPN مربوط است، آن هم زمانی که کاربر نسخه جعلی و دست‌کاری‌شده را از منابع غیررسمی دانلود کرده باشد. طبق اعلام X-VPN، نسخه‌های رسمی دریافت‌شده از وب‌سایت X-VPN یا Microsoft Store تحت تأثیر این سناریو نیستند.
▪️
روش زیرکانه هکرها برای اجرای حمله
این کمپین ابتدا با نسخه‌های جعلی برنامه‌هایی مانند «بایننس» (Binance)، «بای‌بیت» (Bybit)، متاتریدر ۵ (MetaTrader 5) و کیف پول اکسودوس (Exodus)، معامله‌گران را هدف قرار داد. آن‌ها حتی به سراغ پلتفرم بازی استیم نیز رفتند و در نهایت تمرکز خود را روی کاربرانی گذاشتند که از ابزار تغییر آی‌پی ایکس وی‌پی‌ان برای حفظ حریم خصوصی بهره می‌برند.
💡
نکته: بد نیست بدانید شرکت Kaspersky (کسپرسکی) پیش‌تر متوجه شده بود که همین بدافزار با نفوذ به سایت CPUID، بیش از ۱۵۰ قربانی را در صنایع و کشورهای مختلف آلوده کرده بود.
بر اساس یافته‌های شرکت سایدرز، مهاجمان در فایل نصبی اپ‌های معتبر یک فایل مخرب به نام CRYPTBASE.dll جاسازی می‌کنند؛ تکنیکی که به آن «بارگذاری جانبی» (DLL Sideloading) می‌گویند.
به دلیل ساختار سیستم‌عامل ویندوز، فرایند نصب برنامه در ظاهر کاملاً عادی پیش می‌رود، اما فایل پنهان‌شده، بدافزار را مستقیماً به حافظه دستگاه تزریق می‌کند تا آنتی‌ویروس‌ها متوجه ردپای آن نشوند. پس از فعال‌سازی، بدافزار می‌تواند ارتباطات خود را در قالب ترافیک عادی و قفل‌گذاری‌شده وب پنهان سازد.
▪️
چطور قربانی برنامه‌های جعلی نشویم؟
دفاع در برابر این نوع حملات بسیار ساده است و نیازی به دانش فنی ندارد:
• دانلود از منابع رسمی: برنامه‌ها را فقط از وب‌سایت اصلی شرکت یا فروشگاه‌های رسمی دانلود کنید. این هشدار برای ما کاربران ایرانی که اغلب ناچار به دانلود از منابع واسطه هستیم، اهمیتی دوچندان دارد.
• تایپ مستقیم آدرس: برای جلوگیری از ورود به سایت‌های مشابه و جعلی، آدرس را مستقیم تایپ کنید و روی تبلیغات کلیک نکنید.
• استفاده از نرم‌افزارهای امنیتی: داشتن یک آنتی‌ویروس قدرتمند و به‌روز در کنار رعایت اصول دانلود امن، لایه محافظتی محکمی ایجاد می‌کند.
اگر گمان می‌کنید نسخه جعلی را نصب کرده‌اید، فرض را بر لو رفتن اطلاعاتتان بگذارید. فوراً رمزهای عبور خود را از یک دستگاه امن تغییر دهید، از حساب‌ها خارج شده و احراز هویت دومرحله‌ای را فعال کنید.
✍️
یونس مرادی(نوشدارو)</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/3804" target="_blank">📅 21:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3803">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HEzjT0EAyCT4HFJaZGWGq9g1sBiJ4kyA_KW-61ujKOfsckSZd2cXUouodOTPXNMT0P6RmmdGbu6BfLHTqqGkqwVDZ3TWMjC6gQNjfStql4H4NT3GzoGzspSMuuoVpXen9vuVG2YDSuoqmAHLphS2IoNNXkgB9IAgZ3V_Hf2N_k2bCbN9TzA-shXkrpjJdrgQqcwyoioLQ22dL3-X8CvSXm5rae8lXlNJHY-J-F8R6f6wSvVUuLlrc1zCpyIq-bpylmeMyWyUcj0aMxkJQBcgv3RABkYtP4_SFpAM4awWEBEVwcZLtMMY2uNLqzw8b9dUrgOytqhxE7IoMyzc702cGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏یه نکته‌ی جالب از کنفرانس WWDC اپل!
توی ویدیو هر بار که کلمه سیری گفته می‌شد فرکانس‌های ۳، ۴، ۵ و ۶ کیلوهرتز صدا رو کات می‌کردن. چرا؟
برای اینکه وقتی دارید ویدیو رو می‌بینید، سیری توی دیوایس‌های اطراف شما بی‌دلیل بیدار نشه.
✍️
Behrad Javed
منبع</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/3803" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3802">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگر از
http://Netlen.com.tr
بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار
یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰
باز هم خود دانید</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3802" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3801">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ببینید واقعا درک می‌کنم که ۶ دلار هزینه سرور و دامنه براتون زیاده، اما اگر سه چهار نفر با هم بگیرید بهتون فشار نمیاد. همه هم می‌تونید استفاده کنید
برای من سود و ضرری نداره صرفا می‌خوام بدونید که با نفری ۱۵۰-۲۰۰ میتونید راهش بندازید</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3801" target="_blank">📅 19:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3800">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-poll">
<h4>📊 میتونم بپرسم چرا هنوز راه ننداختین؟</h4>
<ul>
<li>✓ هزینش زیاد بود واسم</li>
<li>✓ آموزش پیچیده بود واسم</li>
<li>✓ حوصله‌ام نشد و بعد از قطعی مغزم نیاز به استراحت داشت</li>
</ul>
</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/3800" target="_blank">📅 18:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3799">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/3799" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3798">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تمام آموزش‌های مبنی بر اینترنت آزاد که من توی کانال یوتوبم منتشر کردم به علاوه‌ی توضیحات و اینکه توی چه شرایطی به چه دردی می‌خورن. از بالا به پایین، برای شرایط سخت‌تر معرفی می‌شن تا شرایط خاموشی کامل:  1- متد Paqet، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/3798" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3797">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3797" target="_blank">📅 17:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3796">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-poll">
<h4>📊 آیا سرور MasterDNS راه انداختید برای خودتون و خانوادتون؟</h4>
<ul>
<li>✓ آری👍</li>
<li>✓ خیر👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3796" target="_blank">📅 17:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3794">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">هرچی کانفیگ مرده بود با این تنظیمات واسم زنده شد. توضیحاتش رو هم میدم خدمتتون که هر کدوم چیه و Mux رو خاموش بذارید</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3794" target="_blank">📅 16:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3793">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U0rJCj7BV3H3nCyPh5wvbYOf9E1bY4h4isfythSw7yz98WebHBp0GUEyUxWqEgV0yB8WQ0PN2FOFsu6KeVxvuQdUnJ4FqV3JfDp6Muanloxz52kSUB2Be5CQwSfr-3jZXrGNpewL0TfAZh5vHQ-RHMzGQ7mQcm1QZk145g7urk9yR5B9wOoF97BUw8X0h2jcHvI9U-lbZztsy1_5kzPhq0g1ivBLnr0s1u3o8oYz0GcuXg1Ani_KTCz16U71r84RvxmoRLi5Iz39i-9fYUaB5jOpiVEisg_-LZQ1AInqkk6qbD_wHIYL3ssrgDVt6IS8mpItjZzxjgTDTQ6kHlxBuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی کانفیگ مرده بود با این تنظیمات واسم زنده شد.
توضیحاتش رو هم میدم خدمتتون که هر کدوم چیه
و Mux رو خاموش بذارید</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3793" target="_blank">📅 15:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3789">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nakgKMlfXT1uVqHRaXhIVF-sl5Ks1l7DQq4vooVJhtfwezAe0giC_9M_Yb9UINqbGdf2_3JS7mU5BeovTD1q6NvV8mLhi-Ho6G8d43wzlvvwvEuhKAGCvt6rIC7cGk4cz8ATnkihKuDM0KC_nA-ALE2c8vrtpNfVTsHvI_VOgSfOu6m-u11YSeD0XJk3bdxnsyS-YpWrJqm0UJ7xQpdVaBUvDbLKM1VoQMUCy-CLSe1Qqedr6633NoFU5y6dwvmusQBF43GYyyB8YPXflIqF41PWziJ2FplxVfkLDbUkSOxHqHB767JSWtVR0jpW-O7qkkt144VZTzQorWi7U2v3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t-2XFhT6S8zySBfnC2-SMuJMmiUJvAxvY7SXo0XsEpVYkwLZMW4LKoQ-uumLAvgfsd0p3XMCpvAXvrYsPqEItahydkkXAOQkXHu99xFOpTQdnS4OBRhlKO5_PlLa1iUis3xyUE_jlTqKPY9zXURA66Yt3WKyHFRxJLzfp-5cDWqCpqTtu7ZjgpJkZWaULKLLz_sQKsTZ6GUAcBuxZM3VgRds1_ofSb9cQnTRh3uo66kE5-lwnNs83QGlXNgy9WLeAWH-C-dj7gPxeI86qgZrEAJOLsjsYnGUVYqCJlaMtmwTT3XX4GieIVRaQ6F7Gb3VQ8IsvNl_vqYNzMs1tec2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kfdU7lvNZEAHl-KnjZuAQisnE6fAK9RemfMkjAWcSBC0lj8sExozhaZh0mjyI7I3Ej5TDrkCOtaGJ5xl3H_9UlrTUC27ih2SYBPp52coa_P_OoRgdP9C2VbVZhPqJxGzLDOBUZVqeXHm7N-BXzhuKuQy5Mau_Ti6DRtiqKk3ZbYCnf2Mk_FQEoNQe2K0Uri8s7Qzo4MJfxQdSem4cVeN0Q5gjieL5OwZArNIh63VMUDPUmD118ngV1ZxSf7jRq3hNX1HOBPMhuCVKw8fE2PowZfhAFyhFLY_wxmhBUprUPMTx7WlokMw4KwQg6n_vlhV4FIU9FCQPmPTEY5q1oVaag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NjTmmZ_qUszdkE1qaD-4s3tFqbZNdJJY6CAVnBts99drufq6JxRQB1dJssL47Iy_gBst7K1FoFE79zu2lqaj7HQN8pLI6Xb86648Uve_uu3YlyVKywFo1HH4FsoyxmhKV6h9FrR2T7jxcvyrwTiHyq-31GANTODCHGSF7VnQUqKo1WLDnVtRoOli1RVnjSMzCccAmJTtN9JF-cAsgr2hF95K8wmKFM3bRjW5PnKzNJMIwcray54o16slxf77a5GnRlLXIGx1mqs7DxuUlrflKiD5pdOZk6iQV0HyZurfaFY5VBjN1i6AsWbktcF-xwD3ZNzaLM-A-RwnYgUKJEQQaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش فعالسازی Fragment توی اپلیکیشن MahsaNG برای رفع مشکل سرعت آپلود و محدودیت اتصال توی برخی نقاط
روی Auto بذارید فعلا، من در ادامه واستون یه سری تنظیمات پیش‌فرض می‌ذارم که تست کنید روی اینترنتتون
اگر الان کانفیگ واستون با سرعت خوبی وصله، نیازی به فعال کردن Fragment ندارید. چون سرعت کلی رو پایین میاره</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/3789" target="_blank">📅 13:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3788">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ما آخر نفهمیدیم جنگ شد یا نشد</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/MatinSenPaii/3788" target="_blank">📅 09:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3784">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امیدوارم
WhiteDNS
ستاپ کرده باشید. برای اتصال توی شرایط جنگ
دیگه حوصله‌ی اصرار نیست</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/MatinSenPaii/3784" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3782">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اگر خواستید مفهوم فیلترینگ منطقه‌ای رو بفهمید، سوار اتوبوس بشید و از تهران برید خوزستان. به هر شهری می‌رسید آیپی تمیزهاتون از کار میفتن و باید دوباره اسکن کنید. به استان خوزستان که می‌رسید، گوشی تبدیل به یه پاره آجر بی‌مصرف میشه و فقط می‌تونید باهاش زنگ بزنید
😂</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/MatinSenPaii/3782" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3781">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HuFHxJlRANsmMMds-joait_84pzT05APabdvdzLSX23L_gMvJ3GnIuoq_Cl28rcOMmn5zqnhcZDQ_vu-eSP1AXfIlagp0ZXU9YOTal1pZLmgMwavAUt9Zq2Em28smRHncUCfV1YXBxSJTaDuhzQU2Awdv66SiE_lkNddAgZ3sX8rzeO4VyA4WX5I0EmNeBtXuwI6C6R2MiAjjqoijPRS1fr89QkAOAreqhUtqhiOttFxPX4WIFXGP6GjaNJLWzw979vGzODs_rFS7Rtw0QfH-bpQSVrS2isKZlmgL-d3dE9IKGVOYOTl4UiSM0w9KZAqvdX8Fbc6t3peIvR-ydRLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وقتشه یه سری حقایق راجب بورسیه MEXT ژاپن بگم.
حالم از این پوسترا مخصوصا راجب بورسیه‌ی ژاپن به هم می‌خوره.
واقعیت:
۱- از چندین هزار متقاضی، سالانه زیر ۵۰ نفر(متغیر) مجموعا از تمام مقاطع برگزیده میشن که اونم کاملا شانسیه.
۲- انتخاب شدن شما تماما به نیاز ژاپن بستگی داره و اصلا هم اعلام نمی‌کنن که ما به فلان رشته نیاز داریم. ممکنه شما تمام شرایط عالی رو داشته باشی با بالاترین نمره، اما «امسال ژاپن به رشته شما نیاز نداشته باشه»(مقطع ارشد و دکتری) و این رو به صورت مبهم فقط بهتون میگن که شما رد شدید! یعنی هیچ دلیلی برای رد شدنتون بهتون نمیدن توی هیچ مقطعی. شخص A با دانش نزدیک به صفر بدون بلد بودن انگلیسی یا ژاپنی قبول میشه چون ژاپن این رشته رو نیاز داره، شخص B بدون توضیح رد میشه با اینکه دانش و علم خیلی بالایی داره یا حتی مدرک زبان ژاپنی داره، چون به رشته‌اش نیاز ندارن. و فقط میگن رد شدی بدون توضیح.
۳- روند غربالگری به شدت غیراستاندارد، و رد شدن توی هر مرحله بدون توضیح هست(سه مرحله داره شامل ارسال مدارک و آزمون کتبی و مصاحبه که هرجا رد شدید، علتی نمیگن)
۴- ثبت نام برخلاف به روز بودن خود کشور ژاپن، به صورت کاملا سنتی و با پست کردن مدرک کاغذی برای سفارت توی یه فرآیند بسیار زمان‌بر و استرس‌زا(نکنه فلان چیز رو یادم رفته باشه) و هزارتا دنگ و فنگ انجام میشه. همه چیز کاغذی. همه‌چیز. یعنی حتی زحمت نمی‌دن به خودشون کد ملی شما رو وارد کنن اطلاعاتتون رو بگیرن. و توی همه‌ی ۱۵-۲۰ تا مدرکی هم که می‌خوان، یه نقطه اگر اشتباه باشه رد می‌شید توی مرحله‌ی اول. که باز هم توضیحی نمی‌دن بهتون که چرا رد شدید. صرفا میگن نقص مدارک
۵- شما ممکنه تمام تلاشتون رو بکنید، همه‌ی مراحل رو قبول بشید، اما در نهایت ژاپن توی اون سال Mext رو برای ایران کنسل کنه!! بله درست شنیدید. پارسال به خاطر جنگ ۱۲ روزه، ژاپن بورسیه‌اش رو برای ایران لغو کرد(
🤣
🤣
🤣
) صرفا چون تایم آزمونش جنگ شد. به تعویق هم ننداخت. لغو کرد. امسال هم همین شد دقیقا و به دلیل وضعیت کشور، لغو کرد. و تمام کسایی که پارسال و امسال هدفشون رو گذاشته بودن Mext، گند خورد به زندگیشون.
خلاصه‌ی کلام اینکه برای بورسیه تمرکزتون رو روی ژاپن به تنهایی نذارید و چندین تا کشور زیر نظرتون باشه</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3781" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3780">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nXtx21T9RvIkXTc7flVlGnDGSRPl1R-ai-5GMrv7yV3XhqmZK_m0gj1Mg44xib84aa9eX4rxAbeFcBsFnxKbFr0pnH3_Vrkgn89Yc6_gDAe0lXOEFhpQ7P3kdc5H9bTbhv0V-AlnpeyG5u1xIilBb7tc2wlG4J9EUor_HYBWiE2EW6YCtJ4-DGPTG_cC4XAady7i-m6s3DEittHOvKa4AgPi-zBiGodErelTIFOSNYApqf4aOTFPMWzTZZtP4RsAu5nvJFUUOSK4QGhB7VeGIYJheuADhYw3ofcFzUatFXvQdZ6_eKn8O0ii4JhxZZ28TT8PApwMU1plZvjgionkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
پروژه‌ی FreeLLMAPI — یه پروکسی OpenAI-compatible فوق‌العاده‌ست که ۱۶ تا از بهترین ارائه‌دهنده‌های LLM(مدل‌های زبانی بزرگ. همون هوش مصنوعی خودمون) رایگان رو روی هم جمع کرده!
تقریباً ۱٫۷ میلیارد توکن توی هر ماه ظرفیت inference (از Google Gemini، Groq، Mistral، Cerebras، OpenRouter، GitHub Models، Cloudflare، NVIDIA، HuggingFace و ... + هر endpoint سفارشی مثل Ollama، vLLM، LM Studio و غیره) می‌ده.
ویژگی‌های اصلی:
🔤
یه endpoint واحد (/v1/chat/completions) برای همه‌چی
🔤
روتینگ هوشمند + failover خودکار (اگر یه کلید به rate limit خورد، سریع میره سراغ بعدی)
🔤
مدیریت دقیق quota هر api key تا زیر حد استفاده‌ی رایگان بمونیم
🔤
کلیدها به صورت رمزنگاری‌شده ذخیره میشن
🔤
داشبورد باحال برای مدیریت api key
🔤
نصب خیلی راحت با Docker
در واقع همه free tierهای پراکنده رو تبدیل کرده به یه LLM قدرتمند و همیشه در دسترس، بدون اینکه مجبور بشی با کلی SDK و rate limit جداگانه کلنجار بری.
بهترین‌ها برای کدنویسی (بر اساس این پروژه و لیست هوش مصنوعی‌ها) عمدتاً DeepSeek V4 Pro، Qwen3-Coder سری (مخصوصاً Qwen3-Coder Next و 480B) و Codestral/Devstral هستن.
⚡️
لینک پروژه:
https://github.com/tashfeenahmed/freellmapi
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3780" target="_blank">📅 23:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3779">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">من خودم با Hiddify راحتترم برای ساب، از اون استفاده میکنم کلا(با نت H+ الان دارم این پست رو می‌ذارم با همین ساب) اگر پینگ نداد، توی تنظیمات Tls Fragment رو روشن کنید</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3779" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3777">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ri6YUEmAmo6YhMzBy99HGrMr93x9uHO7TmWhHkbe-hfrwbyWQ-0_JeCDY9AamLyjhZPp6hP6HtuUxWP0yZn6j80skQ-R-ZXOnmOIrn-lrS4t1lis-sm2XCsOvxSv4EwqMAOFoT6kQsbW-uU_v6ax9M6LjSF1SKLkGyA-HR4FI0LHwCapMCwWezIGADGamoT06oAOfp3IE6ZsSakj3EY7FFoUsYCdJl0uMFK6iQUAfZF6jMscnqOixUAJoDSj9bnwafNbnHJsnyAH5zk1r4C8RdRBRxjq_UwdAXiLskV6c44mPb__1gd_LA5upuyKF2RtPiiHJZKjZmY3QcRbVOlQlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n-psWxmTkA9BWUZFlN7yALrnmauQc4z4peRvG5KhI1ZOxGTSAslfXEiE-Kjt6e0ZivWPdZuSWDCJoE6DufKnJrRgLEmqf5XKOpMAmGUcHP8ISuiVOV4ESbBOYWsGRavXp63WTvY7WHEZC-PCO2dTo756rk6-PJsMfx_BXHu2Q8WYAhZGfIq1Xl6d9DlOi1ZmBh6lNRtG56o3FP3O7GDfQE63ir4tp4tH1AJpzghc1f5JyVIOaHGujh-V3f-DEuxo3HapigfIBzIZYqjqsmEdYXPFVFXSJjsKwK9uoVIXa9-_8CJdcxQoSBdAjB_UqzAchoMNB9IADWYgeUy8eMW--Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بچه‌های WhiteDNS دارن رو یه چیزی کار می‌کنن که شاهکاره ایده‌اش
(عاشق UI اولیه‌ی اپلیکیشنم
😂
)</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/3777" target="_blank">📅 21:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3776">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MENpQ4aups_0piNwg9vqgQS5pZNTp0pcUhAYxOUhdV6Sz8Moi39i5wUb9kxHDD2Hw7tz9M1RBTU0ui9fwjNeqXFhggd5XMBU_LIl6EL3YMVpZqJEERdN5MrRWF8qjuuEnaYsz99-7maAo2B2ByRqeaec7gROYOMTeQmqqKLEr5ZXSDN7K3EyZCU3LaUaHLWKuIozz37kTuRy5QrWPDmqrwXLyMUyoCP9HFLoGfPxSzdcuiGxpChmObYfarlzIeyvcetAogmiQ0-A_9HlTjB8XfLo0a54UZ6yfPQj63BYxCTgqt5yt5cE0ZQEZnadjOv8CPUdYMCb3jVmMr0eai2w8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!  این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3776" target="_blank">📅 19:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3775">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=KOmLh3dVQXm9AIiybRDmGdYhVS8YN9MDsO9S3EUo1CjrGXOA6Ql6vIDzi06mLt0EFqUNGAotvHIcPbo7qsEkD2QJSienmIujrc5_zdc27wB7On1sAcsoRKWf6HRbY6E3gxJcF_QNy4Qt2awNSN9Fl7SDPyq5xbzvzVc53uOiJABUzEuC5O2tpGCijUXT_gJTM1puKzY_29fw7ldcpjtKYeKCp4G1rehaR75s8KdQu2x3MZZ1akLrst_97QG8GOyKvbzi0CpHtYbGffFM27WDlRusohmCfwDSrcetlilsbN-cKTbCLpLuiB9kVhPUnefJBw4xpsQYeJV7hx4cBlMlyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=KOmLh3dVQXm9AIiybRDmGdYhVS8YN9MDsO9S3EUo1CjrGXOA6Ql6vIDzi06mLt0EFqUNGAotvHIcPbo7qsEkD2QJSienmIujrc5_zdc27wB7On1sAcsoRKWf6HRbY6E3gxJcF_QNy4Qt2awNSN9Fl7SDPyq5xbzvzVc53uOiJABUzEuC5O2tpGCijUXT_gJTM1puKzY_29fw7ldcpjtKYeKCp4G1rehaR75s8KdQu2x3MZZ1akLrst_97QG8GOyKvbzi0CpHtYbGffFM27WDlRusohmCfwDSrcetlilsbN-cKTbCLpLuiB9kVhPUnefJBw4xpsQYeJV7hx4cBlMlyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!
این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.
همینطور به دلیل توانایی‌های بالاش، برای موضوعات حساس مثل امنیت سایبری(هک و امنیت)، زیست‌شناسی(شاید تولید سلاح‌های زیستی)، شیمی(شاید تولید مواد مخدر
😂
) و مطالب مشابه، از مدل ضعیف‌تر Opus 4.8 استفاده می‌شه.
همینطور همزمان مدل Mythos 5 هم معرفی شده که یه نسخه از Fable 5 با محدودیت‌های امنیتی کمتره.
فعلاً Mythos 5 فقط در اختیار تیم‌های امنیت سایبری خود آمریکا و زیرساخت‌های حیاتیش هست و ممکنه بعداً برای پژوهش‌های پزشکی و امنیتی به افراد مورد اعتماد بیشتری داده بشه. طبق جدول منتشر شده، Mythos 5 و Fable 5 در بنچمارک‌ها امتیاز بالاتری نسبت به GPT 5.5 و Gemini 3.1 Pro و خود Claude Opus 4.8 کسب کردن</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3775" target="_blank">📅 18:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3774">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W8YFFbHFHKsrkLciL5xhRrCoBmuCGdn2hl3kgDYG4jmB4WnsR21ZG6z4RRDqPk6NABW1H2vxtlIaRR3siPNjmNuX5qlkCAG-AB4QQhuHH2qx46ku4i0NOyMBM-3AltsJmRXnSftmnGfRvcNSarWfA7YXK-nn9Q33AhqiFqLCrjwKtCizDZ00iXjtZ0j4dd1O79VgvPZ8IO1aPmhmk59C2xFiJ5OV-Fb1W_TjSbffTGHEhgxAsYDFez5eCFtIMdqUxlkwxiw7_wjFag2JP_ctWQk6OC4N2BiIgXKiy4buqmyklxPe30KCkT8Zgf6Rj-zYuS2JlTK_D3XYf8-YgGuBEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من خودم با Hiddify راحتترم برای ساب، از اون استفاده میکنم کلا(با نت H+ الان دارم این پست رو می‌ذارم با همین ساب) اگر پینگ نداد، توی تنظیمات Tls Fragment رو روشن کنید</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/3774" target="_blank">📅 16:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3773">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X-iBnGqBEsFCrCa_z05YUQu9kP2aShAYxOqfUDUnjV22paQRv-UNs7sbiR1zJ1UADTx0Vd4_YDG1SBUcDGi3XEY_v_j_r4ilDKNhu0RAPhPxGUQBTnI7HQNExaRLP7lBDCItSPgdYD5Hdn2qBP9xFULuuU9_reCcwpkz1tFFPGI8vSGF7aa00t8qKy0tjSh5rZVs37OeMJCjkM6TtF3ZTIzimgNKknwB9269mlAenZuefCSxgemzoZYoNP-c0n0Nb-Dnw4Kx0b3fmOdQReZDmgAvqpFpOIpfMX6Xxf-EEj4xUkPUpwUDROHz2fUpqIQ1rQ7xpnSjfJ0X9dpWfvklZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ساب‌ها رو می‌تونید توی هر کلاینت V2rayای که دارید وارد کنید و استفاده کنید ازشون</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3773" target="_blank">📅 14:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3772">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ساب لینک مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها: https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/3772" target="_blank">📅 13:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3771">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">ساب لینک
مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها
:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
⚡️
توی تمامی کلاینت ها به جز npv میتونین استفاده کنین پینگ نگیرین وصله
🟢
نحوه ی اضافه کردن ساب لینک با اپدیت خودکار
⭐️
پروکسی 1
⭐️
دونیت برای کمک به ادامه دادن این مسیر
❤️
🪐
Channel |
@Masir_Sefid
| کانال
🪐</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/MatinSenPaii/3771" target="_blank">📅 13:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3770">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⏯️
ویدیو آموزش استفاده از WhiteDNS Wizard و نصب و راه‌اندازی کامل و اتوماتیک پنل ثنایی
https://youtu.be/rxxlNXLcaqU</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/3770" target="_blank">📅 11:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3769">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🛡️𝔽𝕣𝕖𝕖 𝕋𝕣𝕚𝕒𝕝 𝕂𝕖𝕪𝕤🗝️(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2b536338.mp4?token=uYc54GmmhbN0i1n3XAWAla2jiOAk7kZ2bl_giNsPSUp3-0bL8mFRKz-65xgqCch6jOhvrqNXyOLpZxsQW7hGyonBmW1JByZbXg0ubTvyQFDf3TO73CrYOqlfZWSM6cbWDRtZGJfrCe6AKZXvCt_A-FGeCiSOhImFMC6s4fhP2Fh30EUxIEy15WxtMWnKsN8yv3WmeInCqkPujI7oFhD0KU_MZ_QBiq6hB78V7wYTaARtEtkjMx8yciswARcAWTdQO-9LH-aNjY7OoxARdgTqdhotljsyw9oP_DUXhYm3No2UoJU3DgOaBTflynEs0N-X24RFufXFMB1MoO1XiDQUSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2b536338.mp4?token=uYc54GmmhbN0i1n3XAWAla2jiOAk7kZ2bl_giNsPSUp3-0bL8mFRKz-65xgqCch6jOhvrqNXyOLpZxsQW7hGyonBmW1JByZbXg0ubTvyQFDf3TO73CrYOqlfZWSM6cbWDRtZGJfrCe6AKZXvCt_A-FGeCiSOhImFMC6s4fhP2Fh30EUxIEy15WxtMWnKsN8yv3WmeInCqkPujI7oFhD0KU_MZ_QBiq6hB78V7wYTaARtEtkjMx8yciswARcAWTdQO-9LH-aNjY7OoxARdgTqdhotljsyw9oP_DUXhYm3No2UoJU3DgOaBTflynEs0N-X24RFufXFMB1MoO1XiDQUSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روش وارد کردن کلید avast secureline
هر کلید برای صد کاربر هستش
اگه به لوکیشن گیر داد داخل نرفت یبار کلیر کش کنید دوباره کلید رو وارد کنید یا به نت دیگه و vpn دیگه</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/3769" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3768">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🛡️𝔽𝕣𝕖𝕖 𝕋𝕣𝕚𝕒𝕝 𝕂𝕖𝕪𝕤🗝️(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b056aeeb9d.mp4?token=SEnDh7o9mwk2a3tiE03rczNkNlnMVc5TF2ZTcc5OzZJIyjriNkZANVx-cErV4rgrYNnZMrbNBQIBvbwnO4rAe5kvwWE1FqGe8SSQhVtp7zkcDvOmOr-1Yl5kYhEbsdyKo0EwsfH5TDv06NF3xRp5uc8YdVys0tLuEjxOAOK8exGEREGTfESQmajI2TKj0he9yI1joXQRcz01Jdbkw-Re0yutsW_xNSqoA2QTQNdv7LZjLmI9a8IHgg10bq2nw6ZWiSq6oML_3-MQTSgzWYbf8SdpNw5ajsT2dUKv1-6cW6TCrtHmIPWyQbj-eawRDKewcPplvY3tk260tufAZ-1KWzkiGp_lKN3xoDxT0zM1Ox3ohsHPDMEy9VGtPvo5rymw1QBAI_WZjI0ltKqRnFQnGs9mpgnqvwUNqI_La1KJkc_u3uh_2L9Z42eqek-5RKmwD83IiZiQfa7H8zGROWHIv90CSvpkiCs6TDi75f-4AUkbSyTWH6bp3XHRzEyuyo4poeilorRp9-qmfff2OgFf7p0eKsdm5CJX72m6qA_Cchy7PGFF6JCB3lNcQ2m5-8X2NtP5u69ntQWP6nR53OhOiAbl8rgkIfJJM6Rf83ijbQJAWRJ-sV3_JPM_2r5nnifWvxMIsQlsWNndvDt2E2uQCIXOfySBSjoaq1Mo1WsLuHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b056aeeb9d.mp4?token=SEnDh7o9mwk2a3tiE03rczNkNlnMVc5TF2ZTcc5OzZJIyjriNkZANVx-cErV4rgrYNnZMrbNBQIBvbwnO4rAe5kvwWE1FqGe8SSQhVtp7zkcDvOmOr-1Yl5kYhEbsdyKo0EwsfH5TDv06NF3xRp5uc8YdVys0tLuEjxOAOK8exGEREGTfESQmajI2TKj0he9yI1joXQRcz01Jdbkw-Re0yutsW_xNSqoA2QTQNdv7LZjLmI9a8IHgg10bq2nw6ZWiSq6oML_3-MQTSgzWYbf8SdpNw5ajsT2dUKv1-6cW6TCrtHmIPWyQbj-eawRDKewcPplvY3tk260tufAZ-1KWzkiGp_lKN3xoDxT0zM1Ox3ohsHPDMEy9VGtPvo5rymw1QBAI_WZjI0ltKqRnFQnGs9mpgnqvwUNqI_La1KJkc_u3uh_2L9Z42eqek-5RKmwD83IiZiQfa7H8zGROWHIv90CSvpkiCs6TDi75f-4AUkbSyTWH6bp3XHRzEyuyo4poeilorRp9-qmfff2OgFf7p0eKsdm5CJX72m6qA_Cchy7PGFF6JCB3lNcQ2m5-8X2NtP5u69ntQWP6nR53OhOiAbl8rgkIfJJM6Rf83ijbQJAWRJ-sV3_JPM_2r5nnifWvxMIsQlsWNndvDt2E2uQCIXOfySBSjoaq1Mo1WsLuHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Avast
Secureline
آموزش دریافت لایسنس‌کی یکماهه
لینک سایت
https://businesshub.avast.com/dashboard
فیک میل
https://temp-mail.org/en/
https://internxt.com/temporary-email
https://mail.tm/en/
https://temp-mail.io/en
لینک دانلود
•
Android
•
iOS
برای کانکت شدن از ی vpn کمکی حتما استفاده کنید
از پروتکل mimic و openvpn استفاده کنید
ÐΛɌ₭ᑎΞ𐒡𐒡</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/3768" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3767">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QzIkp-5-X4xCjIcq89TqbxQUyax7-tdSMhdh7_6wzJjc0w8CKzjTYMgLsmt2rggXsEB3cNDzTsSk1hmKA8Gk9hzEEE8Mizf94KJ3tGAAFqsRSXBLme2WJjcgaRD38Hwh_y3tq8l6U5Y2zFd8vhP6g7VxaRc-y9tOnEiccl3aEyX1paar3Tgg4mmD50JBKzZp-BCpX0jW63WWsZW4c0LZyNMEegwg_7WTgsklpA95pnqa59VVxmYHbS3g2f9loUUY_2e7xZBytv9LfWXttMLFNjGRDk4atT5RWXK_HRJoP8dRK4fpth99jsfRvAAb8REOxhbrw8y4WSy0eRYW58v_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد وایب کده. اسم دیگه روش گذاشتن قرار نیست ماهیتش رو عوض کنه
و نه خوبه نه بد. بحثش به شدت مفصله</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3767" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3766">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">برای WhiteDNS از
http://Netlen.com.tr
هم میتونید سرور بگیرید. فقط قبلا یه تایمی درگاه ترونش خراب بود نمیدونم درست شده یا نه
اینجا میتونید با شماره ایرانتون هم رجیستر کنید</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3766" target="_blank">📅 17:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3765">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qCVBLWHb2NCRxCmVKPqgnonCmTNe_fUT8nC4PXsCGWwTOZ2Q-ZbFYPumbQeucV2DBOxSH_QdJy5erQLmS5f45E4Psx-TbLy7QfZP87rlWezb3Wxl9xpN1HCImbLhoNcytV9QbIbWuKqQQhQpkcq-LEfgc17vQdvsxx4jyCvmBNa9TxGwMiJb8acaRuJDPqpdimx1SximJguDmS9Nno1lXcptRRyIVEqs6BAEFld-VGcAfSa3vOJvSTRw2CMARjXNfKbtMvqgxOpCnOeuCxrly62FbCXI2uSKMWmBr1Wrg9MvXBYdlLHvPErif0rwWaeNgestQqtj3zVKVRt0-TVtFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام بچه‌ها:
متین جان لطفا تو کانال اعلام کن که از namecheap دامنه نگیرن. من گرفتم و بعد دو روز به علت تحریمات اکانتمو بست.</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/MatinSenPaii/3765" target="_blank">📅 13:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3764">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اگر توی ساخت پنل bpb یا edge یا nova یا نهان ارور 1101 گرفتید، کلا از اون اکانت Log out کنید و با یه اکانت جدید شروع کنید</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/3764" target="_blank">📅 10:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3763">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اگر توی ساخت پنل bpb یا edge یا nova یا نهان ارور 1101 گرفتید، کلا از اون اکانت Log out کنید و با یه اکانت جدید شروع کنید</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/MatinSenPaii/3763" target="_blank">📅 09:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3762">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دوستان اگر خواستید از سایت yotta سرور و دامنه بگیرید، می‌تونید آدرس فیک از
fakexy.com
بگیرید و استفاده کنید</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/MatinSenPaii/3762" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3761">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Valid-08-June-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/MatinSenPaii/3761" target="_blank">📅 16:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3760">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67cf13d855.webm?token=ivOUMmMYqxG9LML8rX1RcYfmaM5M7nVr8wSzolUj8GtDCJmxgv2MbwzgelDMWTz3FBiV9MHLTXz92-c32yn8ltx7A613ZBRhn6j-lZnaA59FG7b7eYdMzT6nTDA0rPnUkVWJckOT-8sYIYtqn7UvJHiFOryrYzwd5DPxUFMID-Bqtc5RBPHtwHn6pJOoAzFY6_R3M2VFRybTZE5kFjOWEZNClO17lRDrdNe-0mVR3CvFyZeLoNF3nx-B7yflPIpysaagbJ6aLzxP57EnMXriyZyXEHtYAijZgnlaW_VZKXJAH2PKIoPOZKBBg0QgNXnBogWVvYIZMDGiM-MHRWsvAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67cf13d855.webm?token=ivOUMmMYqxG9LML8rX1RcYfmaM5M7nVr8wSzolUj8GtDCJmxgv2MbwzgelDMWTz3FBiV9MHLTXz92-c32yn8ltx7A613ZBRhn6j-lZnaA59FG7b7eYdMzT6nTDA0rPnUkVWJckOT-8sYIYtqn7UvJHiFOryrYzwd5DPxUFMID-Bqtc5RBPHtwHn6pJOoAzFY6_R3M2VFRybTZE5kFjOWEZNClO17lRDrdNe-0mVR3CvFyZeLoNF3nx-B7yflPIpysaagbJ6aLzxP57EnMXriyZyXEHtYAijZgnlaW_VZKXJAH2PKIoPOZKBBg0QgNXnBogWVvYIZMDGiM-MHRWsvAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/MatinSenPaii/3760" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
