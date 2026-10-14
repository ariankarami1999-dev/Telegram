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
<img src="https://cdn4.telesco.pe/file/h_QsaBuBOaKsx-MfTf7vf3j3Ai7oVZpvKiVi83ZrGveukcBqM5NliAQhiyOvsWj1G_dBDxFW8yXsPbLHbJOcvSAr78RsUCUC8ZI7ct86rXWH5wO2iMxv_Frur5OTJchpcaQzjUIET_Nl5xZUHnHGAjislPfqkhR3JokgkcdjZAfbQJFtpsai3Hz22XJKfROaoId3pEk-kLN_PywjihhVoT6vI6u5YTBZle0QDWGYAasRTq96COONj-CK-05Boo7Bz0x6HlCUGDfJscCv6lirpgeZf7Kv92FEaiiC_yR3KLZQZC0Ki7vgV3SzBT0G9g8ZNRXN0s5RlZxJWphlp6clHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌بازآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 21:34:27</div>
<hr>

<div class="tg-post" id="msg-8099">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3da9b23bd0.mp4?token=RHnKxQCc4zUYLaihQxSHBqa4whUCnLYgikCVkIMOpfDeucywMPQhQHIcynBu-yBqlmVqDWn2ajcluMCvFF-Jy2y2ln26fRMhuCHmx0cvrxr0a08lVKaWHsjVFCZTU8sdhlk3wP4ziVbsGqOh0Xqmm-ZS5oPxlt2vHQkBQFshCRQHWqDBdg0KYMlSvouAXm1C1y9p1rHu24_Dh00_IB6P3QIm-j1fiNbYeNYlS89FBpBpN3DQ00IiDETdm-UAPojPqQgzgNMXZfHAJk_L7OCO7zqGCco_cJR7GIsEByNW2386r76MfM6FCQ7qgMkVmyEmgsum1WiiCe-2j4L59SI7rJ9EybZRY6ybqS2ky8L90tcJrIsRoR5v9QmOyM1w8sMZr2Evsm_oybuwcG2PFis5x7FBXFZ8EydDEF4GhVRgNjGrg-IYdBXY6lCJ4RkyUaXpTTChD2YvWrBv3RlRtAkrF5iTO7-y8dfG8xV8gMBfw8FpwyfXRA1MsIuG32s3udnBRbMcsguRvtPXnh0xfhpSvL6kBDkQgGSgF3l178pSuDvWdXqH4uFO8zGqOcWduOTFqqWdjBDJaMA8i2Xgd2kq3bmevrGF0KfWd00LGKlbj_Pe0xDmTH9RIIW1ewL7ZJ7sI-yRJgCJ82M6RvomUPhz6rFx6y2fa8n8meRtiU9lH2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3da9b23bd0.mp4?token=RHnKxQCc4zUYLaihQxSHBqa4whUCnLYgikCVkIMOpfDeucywMPQhQHIcynBu-yBqlmVqDWn2ajcluMCvFF-Jy2y2ln26fRMhuCHmx0cvrxr0a08lVKaWHsjVFCZTU8sdhlk3wP4ziVbsGqOh0Xqmm-ZS5oPxlt2vHQkBQFshCRQHWqDBdg0KYMlSvouAXm1C1y9p1rHu24_Dh00_IB6P3QIm-j1fiNbYeNYlS89FBpBpN3DQ00IiDETdm-UAPojPqQgzgNMXZfHAJk_L7OCO7zqGCco_cJR7GIsEByNW2386r76MfM6FCQ7qgMkVmyEmgsum1WiiCe-2j4L59SI7rJ9EybZRY6ybqS2ky8L90tcJrIsRoR5v9QmOyM1w8sMZr2Evsm_oybuwcG2PFis5x7FBXFZ8EydDEF4GhVRgNjGrg-IYdBXY6lCJ4RkyUaXpTTChD2YvWrBv3RlRtAkrF5iTO7-y8dfG8xV8gMBfw8FpwyfXRA1MsIuG32s3udnBRbMcsguRvtPXnh0xfhpSvL6kBDkQgGSgF3l178pSuDvWdXqH4uFO8zGqOcWduOTFqqWdjBDJaMA8i2Xgd2kq3bmevrGF0KfWd00LGKlbj_Pe0xDmTH9RIIW1ewL7ZJ7sI-yRJgCJ82M6RvomUPhz6rFx6y2fa8n8meRtiU9lH2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره Exploit با نام Relapse برای Jailbreak کردن PS5 منتشر شده که Firmware های 7.00 تا 13.60 را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/ArchiveTell/8099" target="_blank">📅 19:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8098">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgyCYr4JtPfwq4fpkmJDHdTQ-5GTRBKyPyKM_sRRnZy5qSLNuH_sUDqeGD6jHRLlZB6DbMG68To3IyrjmlQCBwLWQRGNKDRbERTockiztQ4SMtmvw8XQUlfx_VuNtD8CoNWvSxT9ZWYdGG41vx9bo3Q-mYukyuObOJ76-5Mv5A1bY5UKR6cwLhAFmDaJ78HizHzWdD9msgX3X_ZYP_vrZ1eYe-EFulCw1Mgsc4BqVRhGNrGWFkHUhkTGlE3w6pOjldy4bDOoOlPcJCzyoR8FPwv_PGFGOKhXPShOezmcoW1Ku-n6t2d4YX9OlDgzqnynjKHU0DoCzGl9Fqfo6iVIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلود منیجر اوپن‌سورس Apex برای ویندوز
‏⠀
‏هر فایل رو با ۳۲ کانکشن همزمان می‌کشه و دانلود نصفه رو دقیقاً از همون بایت ادامه می‌ده.
‏⠀
‏اپکس با موتور Rust نوشته شده و دانلودهای مرورگر رو هم شکار می‌کنه؛ بدون حساب کاربری، بدون تبلیغ و بدون تله‌متری. لایسنسش GPL نسخه ۳ـه و یه جایگزین رایگان برای IDM به حساب میاد.
‏⠀
‏
📌
ریپوی اپکس
‏
🌐
سایت رسمی
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/ArchiveTell/8098" target="_blank">📅 17:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8097">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNqbC-Xe4bOCZmSPf_d4bqiy3rTASBQDEtpOgb9aAcVmUGj8MkWvw6qO_qY4MvM5zvvjb802UQx_3cQJCGG6Rxx-76uCfWZ3Z6K9NjjaInYtFYP68to9L7ubGWgo6WGnzLhbyQ-1lK3pYUsMz3wdoG0pqqJxyF8wK3lIBxBI240s3cwQ9GY5kCZMn-mn3es5i72ZpX7sbrdZhUykQq66UEHiImyUQw0sNbJe44A3aGVmTPMZe0oBx4iUS4Rhcp2fCsFsTDsEska1Ocrw2SZLtLuiUevgkZC_pn1SO3QmhciDwxqDFDXRGG0Q5dczwRNwFlUClZd5a6r1Vj_vg4ZJkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
لینوکس داری و از GNOME استفاده می‌کنی؟ پس این افزونه رو از دست نده
🌀
Qurp یه افزونه‌ی متن‌باز برای محیط GNOME Shell هست که با کمک هسته‌ی sing-box، مدیریت پروکسی رو برات خیلی راحت‌تر می‌کنه
😎
🔥
باهاش می‌تونی
:
🔹
به سرورهای پروکسی مختلف مثل VLESS، VMess، Trojan و Shadowsocks وصل بشی
⚡
سرورها رو تست کنی و بهترین گزینه رو انتخاب کنی
🔒
از قابلیت‌های TUN و Kill Switch استفاده کنی
🔄
اشتراک‌هات رو مدیریت کنی و اتصال خودکار داشته باشی
💻
دیگه لازم نیست برای
مدیریت پروکسی
مدام بین برنامه‌های مختلف جابه‌جا بشی؛ می‌تونی مستقیماً از داخل محیط
GNOME
اتصالاتت رو کنترل کنی
🔗
لینک گیت‌هاب
📌
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/8097" target="_blank">📅 10:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8096">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERfG0wxZY5hF_HfT3ojrtRLUZAgKRy6YAAmStzw10f1gpJ3MNgge5XNRAT7VttS-BfET16ojfklad-drqAt0ZKKZ6hyDxlt0D8caWe9AZofLgIHleeAucFvuKAxjEOPi8U02WUaOVe6QbRYYrJcK7yobYKphZz8iT5mc5_v1_HBPbgd9XHYKdMnNRTNE1g6FSaU7FtIrubYdSFUXg6zvOKwv-NalmoX6Op5AyxFGLsaykuL5zFmerOGhjeBky4oR75HZ9md6YbXdFFxCG0UcJV45QpMGtkV4WWlqXxq1avUqgtzVZ_Spj-ibPrF0R41i4lsrYNXB4kMaQxt0KWyQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تست رایگان مدل Gemini 4 Argon با v0
👾
📣
با اعتبار رایگان پلتفرم v0 می‌تونید مدل
Gemini 4 Argon
رو کاملاً رایگان تست و استفاده کنید.
📌
آموزش استفاده:
☑️
وارد سایت بشید
➡️
لینک ورود
🔗
✅
با اکانت گوگل خودتون ثبت‌نام کنید
☑️
کاربرای جدید
۵ دلار
اعتبار رایگان می‌گیرن (کاربرای قدیمی هم همون ۵ دلار شارژ ماهانه رو دارن).
✅
وارد بخش انتخاب مدل (Model picker) بشید و
Add models
رو بزنید.
☑️
اسم
Gemini 4 Argon
رو سرچ و انتخاب کنید.
✅
حالا پرامپت خودتون رو بفرستید و شروع به تست کنید!
🔥
تا این فرصت رایگان از دست نرفته امتحانش کنید!
⚡️
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/8096" target="_blank">📅 06:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8095">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پروژه زدید با آرگون ؟ بفرستین تو کامنت ها بقیه هم ببینن
❤️</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/8095" target="_blank">📅 23:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8094">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9OPhX0A1KV2LCljKcf9bcezzg3aTBmmCQOQ3_V1ZuXVQkjeyKk1NRspVi_BYh0Wy0wgpd9-CkpDYEsF9auX2njlOH__g_T2M2VlZNvZDPIw51vZEB6oXfOBSs2UTJznmL_71ao-jvhu2UR3cuSl6OjjIe-mgBbkGyeQedj8lycMACbXCLv1e_deHqZrtGAvdMSCNyatnKx2k__GHRcanlC3GY7aewGRVp8numjolxj-IGfYJBWKyzJztv0l3K0_driV5qYg7x0FtzMortnFc30CCkUzNBMGru0uaIf6p4lhwyJ5R1_AYbFewJZl0I0pSi0AjOZb8xWlmiRrSXJDbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگزین متن‌باز اتوکد
⚡️
نوشته شده با زبان Rust
🖱️
پشتیبانی کامل از فایل ها و دستور های اتوکد
⏱
مصرف بهینه رم و سرعت بالای اجرا
🖱️
لینگ گیت هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/8094" target="_blank">📅 23:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8093">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پروژه زدید با آرگون ؟ بفرستین تو کامنت ها بقیه هم ببینن
❤️</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/8093" target="_blank">📅 22:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8092">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ph0aw4XX3_4pMBS30yHr8K3xWcPTM6cQM9oQHtIG_9EhR-T9o5chUkayFGE1Csowf38r3EvwJDd1pXrMrx1_2aj2aEa56ChdAr0bABvmOQBloIcZkMEEDT5i6yIQWoIURdjLwTlFxQFfTjlODDvo3KutKO75vAcdkvHmT7ri2KFVK7fS_HY0rDxUtcYv5BMa6c80qV43qGJlzWQTLeax8mX05e4rNz1FNOeEq4fMBnZ4fZelzWGNnwfYgbRCDw-w9PgBolLKvoDVQTldyn7GDkUx2EZqpFJB-VLb0q75jVKRE-aOPMVfZPEPntPxqWw7aG09gyakLZIcb-7b0qwlOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیو هم اومد</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/8092" target="_blank">📅 20:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8087">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgfZIazIw5HRvaV8b2Co4u4UnBn7kPQoLdPOR4SwZoVuTLvmaca5EIO3JTWNZnjK0v53HMY4XT0sn-yTLlu5Q28LBJWc4fZ53XfLedaI1ryVqJI2QiwM5oLQTaAlSfgYE0MCnysD9GJ5PDJPo5BU5YWmlvXAs88Q-kVHXpG830zv5ynGfM7CFOc0mMlWgIMnlv3eJwXdSKxmcqhImwwBZLiRT_EeqN3DalFFqyi5tyIt-6OLgXue8EUcjmK4w7EXpfldl6CITsYBXRbvCspcEVUmHkY7oVjd28A8KsB47wd27q0umiHJEwqgPebKJwuiLVl_OCyZKCJA8G5lyOaQZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا روی پلن اولترا منتشر شده ، معلوم نیست کی روی پلن های پرو هم منتشر شه یا اینکه اصلا منتشر میشه نسخه آرگون یا نه ...
💔
یه چند ساعت دیگه احتمالا بنچ مارک های واقعی جمنای ۴ آرگون هم در بیاد، خواهیم دید که درحد مدل های پیشتاز هستش یا خیر ...
🤝
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/8087" target="_blank">📅 19:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8086">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjXn1aD5B6d-uDoPOGTUi5Xt4Q36xmXVW95WKQT6WI9t8Snhxg_xqnPdYLR2zzG9RRyi2F7wINdfxNkUR_7eXwYGqUVi1wCP_42vtiB8dy77gsbqTwulB1WEvbSj8mgkI3oDZchw0FKkw6pTPJoUP9XL_7pDy2o6NNiTFT8Qr7ZAUBp4GKbWcMnScZbyXTopqtYLpztbE7NmEwl95TVBQR_g0GR-sJ6BoUVmfBNR551Dtsy5aa7v3JDYj6BsCTHfY63IUiXf7hlQOqmwDc5dnyRfo48mwWWU7nc6NK_IF-unHjzlW7sdiWuMy5hVLd7F6YMppDJTsHO9yKE_Iby-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📦
اپ WG Tunnel حالا روی ویندوز، لینوکس و مک
⠀
‏همون اپ رایگان اندرویدی، با بیشتر امکاناتش مثل وصل شدن خودکار، روی کامپیوتر هم نصب می‌شه.
⠀
‏
⭐️
پشتیبانی از WireGuard و AmneziaWG توی یک اپ
‏
😀
قطع کل اینترنت اگه اتصال بپره، حتی بعد از ریستارت
‏
🔥
جلوگیری از نشت ترافیک همون لحظه‌ای که روشنش می‌کنی
‏
🧦
پروکسی محلی برای مرورگر و برنامه‌های دیگه
‏
🔐
ذخیرهٔ رمزنگاری‌شدهٔ کانفیگ‌ها روی سیستم
⠀
‏این اپ خودش سرور نمی‌ده و کانفیگ رو باید از سرور شخصی یا سرویس‌دهنده‌ت بیاری؛ ترافیکت هم از همون سرور رد می‌شه. به گفتهٔ سازنده، اپ ردیاب نداره و AmneziaWG در برابر فیلترینگ مقاومت واقعی می‌ده.
⠀
‏نسخهٔ مک فعلاً از مک‌های اینتلی پشتیبانی نمی‌کنه و macOS 13 به بالا می‌خواد؛ اگه روی ویندوز نسخهٔ 1 رو داری، قبل از نصب نسخهٔ 2 پاکش کن.
⠀⠀
‏
📥
دانلود برای ویندوز، لینوکس و مک
‏
🌐
کد متن‌باز در گیت‌هاب
‏
🖱️
معرفی نسخهٔ 2 در وبلاگ سازنده
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8086" target="_blank">📅 18:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8085">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNc9vJVGktCcwrTsIkOSWpGIeKKwQZCzFJPBdfBseX8VSDVqBCW-JR5ropO8LpWY_xgC1Yt4kXVWSsipiK3iVDo_1cZe2JLrn6kZoSugvHtzJVqCjmqU-FdlFAKmOniUC1Nfxk0WsburPPB9XSw_1edFwyUfH_kHJ8TbTjaZDde1K7jeP34Fla5Vle20hTZgF74vQJ9NPwVRS6oJ5nprSt2Ql0EyridpqeVZwPR6AZY8QPk_ujzOuWOHM9TZNdk-c6LKZgErCKruzX-7W_ZW2BavPPQlXFC1x5WV3FWiUA2uDLEjrW79UQ7T1WD88Z3EoEBJR7FIfkjJtRKYJE_skQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎖
• بعضی کاربران مدعی شدن احتمالش هست روی پلن پرو هم جمنای ۴ آرگون دردسترس قرار بگیره ! ...
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/8085" target="_blank">📅 14:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8084">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr0ChdGiJt0iNSrW7JwIieedTynoZVy7ktKO_lwyl-9IiS7thklG86XmIscdmpAmcpD36SFyEY53aOaUQ4xKc-DCroEnWobp5n6HMvy4hCBroW8fLjSfyVpRF9ZPtSJ1gojAPeEuKVNidF8EzObiBPyHXsYO36v34bAH3qAQ7U9HpQxoQzAlY9nrE0X8VHJ1qyLp83iT4lroYe0cIabGeU91dWKOLrW5Y1T56K3XF-Osq0bypKST1L8WJ4SA6rtS6tRcaKEIAanKaZPmjoi0DLubA7hPrezPkFkpG0H9cqcGjuqFk57EsAaj0uQucz1tD_hk0ReVI1O6cQRdsBb15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧹
ابزار Ubuntu Cleaner برای خلوت کردن اوبونتو
⠀
‏کش و فایل‌های اضافهٔ اوبونتو رو با چند تا تیک پاک می‌کنه و جا باز می‌کنه.
⠀
‏• پاک کردن کش مرورگر، کش بسته‌ها و پیش‌نمایش‌ها
‏• حذف بسته‌های اضافی و نسخه‌های قدیمی هسته
‏• حذف نصب‌کننده‌های قدیمی
⠀
‏رایگان و متن‌بازه و روی خود دستگاهت کار می‌کنه؛ داده‌ای جایی نمی‌ره.
⠀
‏نکته: روی اوبونتو 24.04 بعضی‌ها از بسته شدن برنامه موقع انتخاب بخش‌ها و نبودن گزینهٔ پاک‌سازی هسته گفته‌ن؛ موقع حذف هستهٔ قدیمی احتیاط کن.
⠀
‏
📦
صفحهٔ ابزار در گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/8084" target="_blank">📅 23:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8081">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTYN8SK4ay5-KZTVWMUCclF6iZtUnT_UO9dWaVZrH7WdAEXQku-Bk8wOCnT5z4UZge_Jd5WyjJbdBkUDzqqQUKFRK67LHK6cWDpoHaEOSA5iB43VXNpqiWZcaNywHl6KgoMaVKnJE4QwHUynKjdhmv6QJh7uTsrSdWINAzj-IX-3gZXY2CuG_ToshNgd9CHFf8zGBeyQIoHyzZW8r2USkWPyx2WrUkDfvUF5A0bvQ9GibchTxrOSneBIDFEdFjzMwHsE569junrDZF1L2zW52qmOE6pYy2xi0Mpm3VdO_5x94d1JirP6yXVIUzfBcgTwacHjiszjBcih2xC0pLJ1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک این مدل ها در
Artificial Analysis
منتشر شد
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/8081" target="_blank">📅 21:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8077">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pa8cfLJGMsDaf_nnfyx5LS-fw8VLmnhs9_U7xWszw8-LJfHl0TFJC46jlBupCVVumLQwkeC8dwxXq5M9sZOTjefLyUfxAVMF2VLScswQJyzmSiTRyIj_7g4GXbdJ2MUUFLi6lv48BG0UTbIcpgdDx4uhbjwA66UUzlVLWxUS57-scXpDirXLc4uHzNCrrB3qQjvrCpkwSUltzQJbCSRsyzDcQ8WsmVOLsQi7LdpXAR3-XXx0bRjgJEjhlJcfMnl3lr3XHKtTt9XpekD-ZPSR7CR7wnCzYUHxSeJqS95lTSiwBk4rUTweP4FOG4erlheP4UfouEZm7f7ZCb-p_xaI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hycS3864HX5N1sZ6oQbu60e4e4RTaNLMTJy5vMUayGuJ98JWugLZGaw-ezpcJ-klrWnwWB_FVuoedOVTcP-U-FEsC2QIoPyMd-j9NGWiQswkfKCIBhUMoJCaMmZQPTmqlOBrlsQUFiu0u_D4T5KQV7nE2v913sW89n-kHZV5IxelAdqN_xqMbq5qLbSq2Yf99iCYe_8C0-dVfM_gt7phcpWuhRKkjNBZYKXItztC4_LnrxZ_GKJefIwMkkPNqTmLS9mL7-UnIrYRetFvU9MpDNsolye78vIbe0dQ1Vye-X48MGSlfNlc26I45sE6Gh6q0gZG29xo_cRLcGvGlZXVsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtQDRwEvhRsHZX3w9hCNn_aXW2mlZjHWQBxublb5UPXf35IE6rXxrOOM8hzMRCBB4bs4_jExVzchzqnC03_oah0KS-ZWUSgsm3cldeU7O7h9972apFRN2EKiArSSBivcwybinPJ4DIqB0chyPtUKHHcO4c2w10_1r9jH6RI_LwiFzl_4EQDNg--gjz3d1Mh0TDuYRfojPtNDD-PYyBxRctg3q9aDoY-zv8KcL210McDBnDX18e71Jhx5utK59HfjfJz_sp-uIcgJyOgjaN3tFGptFv-7pUFFE1zToLsEM8L_AkY3CBPPParO0nZ9a4rhmM5DKivJFHXYdTPVeMOgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jy7Y8gTM_7GgP7q1iDc9LlYEU5evHyISvAZ9946QCnQYnLVmXlUFd-sgqE7kzYEbHXohzXCjICd-skI_pAvMzBaBvjDHkV4ORU_wxezBHRiu7BJzonk46KaLZw_0hdEEaxPOMhs7EnF2caq4VlvB435hDmnwiM7GLssEHqXQiS8t1PYVTRbfczUDKsBAS9R3zYWoGpnwPe9t0GPMyJFa4_NJK4I4Bqu_u8tgqRhE-UL4hhyhnbhJ3ABh1svHAOENNN_MPlCwLj45ffhMTCcNaBR_1R3Su1Xny1QznorJVU7K44m6voUjZd3OVAWh4TTMtp0CAf8jjhibu962nabyPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🚀
معرفی مدل‌های هوش مصنوعی Muse Wonder توسط متا
‏⠀
‏متا از مدل‌های هوشمند تازه‌ش برای انجام خودکار کارهای طولانی و کدنویسی رونمایی کرد.
👀
‏⠀
‏— یادآوری خودکار پیشینه و جزئیات گفتگوی کاربر
‏— کنترل مرورگر، حل بن‌بست‌ها و تایید گرفتن قبل کارهای مهم
‏— حل بهتر مسائل پیش‌بینی‌نشده به لطف پیش‌آموزش قوی‌تر
‏⠀
‏مدل پایه تو Meta Model API و ابزار Muse Code در دسترسه، اما استفاده از Muse Wonder Full فعلاً فقط با تهیه اشتراک ممکنه. هزینه این مدل به ازای هر یک میلیون توکن، ۴ دلار ورودی و ۲۰ دلار خروجی اعلام شده.
💵
‏⠀
‏به نظرت مدل‌های جدید متا می‌تونن رقیب جدی ابزارهای کدنویسی بشن؟
👇
‏⠀
📌
بیانیه رسمی متا
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/8077" target="_blank">📅 21:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8076">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAg1eXdsJQkKImLkPEtFuSqc2gGYS-LXjqXhCtfDct2Mn6lC5CsMicHi2OITXI53Kjq58_FLJFPSA4AqaC4dv0vejp9xbwoThUV_VdlneB6ofCEGw0crcjTRCb9uKB9zVhehI4cZLz6_ID1zq912ieGQgwzV0vF9aX8YzVfiyftH7cIB4Fy006tHfpCCFRarshk2scrikubNU-H5cGd7jV40H-1fL58XA9SZ3sAqta1iccKuIopTsEO8Fd1ol7PZ7lMHhLHyNfAqvtvtytyUlCvJCylGJtO55Inij8HanF_QI59-AmhsMWLt48XiLMEWz0l__ywWuU0sc8yX85drrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعب
گیم های جدید
https://tehran.velestudio.com
GTA Farsi
https://gg405-golden-gate-racing.surge.sh
Driving</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/8076" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8075">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXs6H5pT9s0j0oxCZWBjlfwAwjFYLM6YsCPpiLtOMvihxgssDgQ0Iq30LjQbGIE9gOdCZyH_0tmmsrFfswCOnbNEmW1YlgaRU9EY3z3YxsLRtDfiBuMbKuT28wbdEorEIg6Yv7cHRtzZBkx_HQqUjJOOi_dXf4dIZCLlettiWiFF4nnF0e6LuMmp9UJJSpUylFtSlPZO5thVglx9tHkjccedR5okT1xlGomJUxttfzcobTadsnfAxxbc4Wleg7qd0L6CsbSRcYRjnUg9rZP7IR46qAafLMfTA7XLF2vwDkoZWFv9ZQIfDF_1YGBI7AVO8nyzE_D70pVNsQ1JTynAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💬
چت تیمی EdgeChat بدون نگه‌داری سرور
‏⠀
‏این سیستم چت متن‌باز کلاً روی زیرساخت کلودفلر اجرا می‌شه.
‏⠀
‏• گروه و پیام خصوصی و صدا و فایل، با مدیریت و دعوت اعضا
‏• پل دوسویه با تلگرام؛ هر طرف از ورودی همیشگی خودش استفاده می‌کنه
‏• نصب و به‌روزرسانی خودکار، بدون نگه‌داری یه سرور همیشه‌روشن
‏⠀
‏نکته‌ی حریم خصوصی: رمزنگاری پیام‌ها سمت سروره، نه سرتاسری؛ پس به محیط اجرا و صاحب کلیدها باید اعتماد داشته باشی.
‏
📌
صفحه‌ی پروژه در گیت‌هاب
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/8075" target="_blank">📅 18:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8074">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZZd8ZimsqEJt0ZV5cMKL9UL8PVA4w3Dt-KHqpDNCIpco_yw09cdjybIkwL5MEKuzSmMpkeoeYiD2oz2cdbbPJ30KX9ewJSex461UrntitcM7ouIbS9qDQ621umrO96WIcsauREFUdRd70exfV1_dxLuvyz2V5AackM2BuDllU04wxg_fvYnXZh_vct4aBgycfAsSbzQiiqhcq_Vb3a7ZbMZahsQgNYo1exOHiBytGANGja6yboN5uE7FpybmYsjNqBOf4gZ5dcICsmXvQNhC1oquGK9ZdE74jIoJKHcsSuXzNywH5Tfv5GT3i2fWARL6vRqwb01AWcMmcD3Ok0djw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اپ‌ Gander‌ برای باز کردن همهٔ فایل‌ها
⠀
‏اگه گوشیت ده تا اپ نصفه‌کاره برای باز کردن فایل داره، این یه اپ آفلاین همه‌کاره جای همشونه.
⭐️
⠀
‏• ده‌ها فرمت: ‏PDF‏، ‏Word‏، ‏Excel‏، ‏PowerPoint‏، عکس، ویدیو، صدا و زیپ
‏• بدون هیچ مجوزی کار می‌کنه؛ حتی دسترسی اینترنت هم نمی‌خواد
‏• حالت شب برای ‏PDF‏ و ‏Word‏، جست‌وجو داخل سند، ادامهٔ مطالعه از همون صفحه
‏• حجم فقط حدود ۵ مگابایت، روی اندروید ۸ به بالا
‌‏Gander‏ متن‌بازه (MIT) و همه‌چیز رو روی خود گوشی رندر می‌کنه. چون مجوز اینترنت نداره، از نظر فنی نمی‌تونه داده‌ای بفرسته بیرون؛ فایل زیپ رو هم بدون باز کردن، مثل یه پوشه نشون می‌ده.
⠀
‏
📌
ریپوی Gander در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8074" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8073">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fITlFZYKMKWEgirK7OkCb4CFNnoVlPwWKG1SVjEeYD5-gsm7Eik-hWt8OxNAcTMtJxsQTJBpsCpPvNtti4F4AEc1HNWsIX_Z3r65lTbCDw18CQvhASa_Wyvl2fDbbIWPFmnFSgkWimWWKQhxflhWoDLiIfCbHyluOaxbN5bysN9BIgyT0zN7CcDx8lnSC5oaXgEalwSdq6KDoFSXoe_TxTIK5GygKBIBKpGKZZOKu2gTbo4imEZ2b6xVTqzX4zvS9mSIiQryZHtxVG9a7XwuiL07TxAv3R9isN4f5px5jf4Ebs8mY980hskv06sP8XdGjnPLYiTgBcona2EUtXBRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🐧
خالق لینوکس از هوش مصنوعی خوشش می‌آید
‏⠀
‏لینوس توروالدز می‌گوید برای کارهایی که در آن‌ها ضعیف است از هوش مصنوعی کمک می‌گیرد و برنامه‌نویسی را برایش لذت‌بخش‌تر کرده.
👾
‏⠀
‏در گفت‌وگوی اجلاس متن‌باز اروپا تعریف کرد که رابط پروژه‌ی سرگرمی پدال گیتارش را خودش نوشته بود ولی ظاهرش شبیه دهه‌ی هشتاد شده بود. خروجی اول هوش مصنوعی افتضاح بود؛ وقتی کد خودش را نشانش داد و گفت چه می‌خواهد، نتیجه بهتر شد.
‏هشدارش هم روشن است: برای کار واقعی و مهم باید خیلی مراقب بود. با این حال سبک کدنویسی با پرامپت را برای تازه‌کارها راه خوبی می‌داند تا لذت ساختن را بچشند و وارد برنامه‌نویسی شوند. این‌ها نقل گزارش گفت‌وگوی اوست، نه توصیه‌ی رسمی پروژه‌ی لینوکس.
‏⠀
‏
📌
گزارش گفت‌وگوی توروالدز
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8073" target="_blank">📅 22:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8070">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">samsung_root_guide.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/ArchiveTell/8070" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💎
آموزش کامل روت کردن گوشی های سامسونگ
✨
فقط گوشی های سامسونگ One UI نسخه 8 به پایین قابلیت روت دارند
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/8070" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8069">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfoteYBfFn-5CWzGPv554Z06QnXPHlLUVZWT9mJTR073Z2EXcn9ZnGRHlkanIj8mvHLYYZxJNRWt5Q82GXoC0hIEaKaQkYzP3r-aPq9cE5VHXwpasgKfObphV96wuxPXpQxaEPAAjuRZsRaP1bZitwjrvphEDz8lHN5zDtrMtrlmQiTIBOTMMYEPcpNdf77i138PV1QfOcuUiADxoMH-D6KX5g2HHeVkIynO_KqBA4D1QH1HL5aUojAUItwvnKLvaeR0-TxaVucf_Qpt91lZdRyaigWJnx60cKuNUH9NgJbXqJ7iEqPuNShJoW1ZcHWbOWQkuVerx_E2iILVE7Fsrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
دستیار هوش مصنوعی شخصی‌تون، فقط روی کلود خودتون
با
Talorys
یه AI
Agent
متن‌باز و کاملاً خصوصی داشته باشید که روی اکانت
Cloudflare
خودتون اجرا می‌شه
قابلیت ها :
😀
چت هوشمند
😀
حافظه شخصی
😀
تسک و یادداشت
😀
یادآور و اتوماسیون
بدون سرور اضافه، بدون جمع‌آوری هیچ داده‌ای و کاملاً رایگان (روی پلن فری کلودفلر)
نصبش هم فقط با یه دستور سادس :
npx create-talorys@latest
😀
لینک پروژه
اگه به حریم خصوصی و سلف‌هاست اهمیت می‌دی، این پروژه ارزش امتحان کردن داره
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/8069" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoxf8wNbgFI-wlNs8Pq02XdrEzOaEm77oCRK6-gva9ci5XHG2DyV-0j5TAw-jsX63Kf4fE3O61BbFCe99ZzKlDhlipnIzU4Q4sX3BGdpUsmtHyrsGeAIfRsbobYkvST-Uy59x5HSz1bhbwKAFNcPHYAoSbBHveLexfSEjWdhXkZ5dCnVC9G07gurLTlZjZ251gOK7jhEIqgCecLQUNYhF-coVdbLqjfyAlovy6hk74dJleKXGfVt9X94m6ric6oKcv_erzrpOEcdkuRqyPbEpJ1QK3-RHAqnAr88M9D5I7AArLebVUS-1rXF3GDYzzd7vlDywGIWLm48fw0GMS1loQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8067">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAJ5rvspN1e83r-1MTcFGyZXtVlF7h4Vb4cCTB5zrqhs8iMhpEKDNJWo123MCxyyAtZSGcTxjThqoPDhLDQK0U3GxG5kgTQkevHuZx5RPJE-dVEUxuF7uvc-O43obAJGYa9dhadFjzHoLPvkShKHuYTBugCKoFGAzmz-uS0X9Rb4Y2BYHPmAUGShRi2YZE_YW_DOQUYodNn2WOoywIK2HbzP3YZfOCvz_UVnEx6RE1me-nv63UyfGm45f_5_57kk4fCAChX29epJrUdBagB2Rm7ye84Oj18ualAtY2ca7pI8FlV0LHcxEq50h4j-gYimExmGr3gHClKA2VTtxJlG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📰
پشت‌پردهٔ عرضهٔ عجله‌ای دستیار Muse متا
⠀
‏نیویورک‌تایمز می‌گه متا با این‌که از مشکل‌های امنیتی دستیارش خبر داشت، برای عقب نموندن از رقیب‌ها عجله‌ای منتشرش کرد.
⏳
⠀
‏• به گفتهٔ سه منبع آگاه، زاکربرگ تو جلسهٔ ماه اوت و با دیدن رشد استارتاپ ۱۴ نفرهٔ Instinct‏ دستور انتشار رو داده
‏• تو تست‌ها، Muse یه‌بار بدون اجازه رمز کاربر رو عوض کرده و یه‌بار پیامک‌های خصوصیش رو خونده بود
‏• از ۸ سپتامبر منتشر شده؛ بیش از ۶٫۶ میلیون دانلود و روزانه ۱٫۸ میلیون کاربر فعال داره، طبق آمار Sensor Tower‏ گزارش شده
‏سخنگوی متا ادعای عجله به‌خاطر فشار رقابتی رو رد کرده و می‌گه انتشار رو چند ماه برای اطمینان از امنیت عقب انداخته بودن. ولی این ماجرا یه یادآوریه: دستیار هوشمندی که به پیام‌ها و حساب‌هات دسترسی داره، اگه یه لحظه از کنترل خارج بشه می‌تونه دردسر بزرگی درست کنه.
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8066">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده: ⁮⁮ ⁮⁮
🆔
آیدی عددی برنده: 2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل: @ArchiveTell…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRaHGZkgfNHcqKdZhH8IvqbnKK1RLyQA7m4xAgjGteFTs0cGbHDj_IP0DyCZA5U7uj0mwp11GU2471kzepbcgD3cN4phILgUP6ApQbU2KkeXJYjuoHyZu2kCzD0Enze_-vgA8w_XTnOk38CegZAHKm-M11ZJLJK4XJ-spR1B_QJJ9IhMa_6-ecc1wOCInJXIEw9KbYK37LFF20xpav6nUgORCWpQ0CRA1c2CEbrUPL5rLyW8-z2ATiWnjKJfJfuJmtmZa4zIE3fZJ7BjlGJHSRaKH4jDYJw22cS_FZHwR3QVbELz3brHVJPNPEphMOkTyPBTyAce5-In2B-pYYulnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9iWHkGUNPxcUhnwRvg81bqy5852lRpQmbSP4RloCj8RxCsRw5idABLVF9_XpGvVXtpXXBDBmnHx9pqrxFHjD0cJPLwx6cMYUQzqGy3qKymy1jSggb-2f581jh2aDsQ9_wsOe_q3tnGPyMtCJtZw097lFDeyrGA35b-pnnUjydPM3Wj3Tlm0HYstYh8PsGnF-XPVCD_JBGC5NqoJcJX4uSgLNFc4Zidh0YcDQb8uPOXWZGxHoIW3BU9it0wYCtBtSByeWQt7Y7x9U0QS1-VwvVGvdRaoWYen7tpgQIGYFZhjjHLDd2zlVAPJC8HljScJXJEzCMDxqiThLBCrN5xZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQGs150cl7b5a9k0Djlwny7PsxdJnoK6guaELgewDPxTNAeYmePgPUiIj1d6jVYIu7ezT0tiQWtUYYXQSHYKggZsH_iaWZpNxY1djRMg8L0fboQMUF35h2ZLkvs2jjTs5ARPk0Nyp_2tLZtx9NlSljMidF8ikc4G9uei0kNjN_qTzMWKohOff7CGRSOHG9BnP752NfVWsboLGYD_FZhXR8n5-0Q0oyrKl7GOW4FYzqPH5N3gAmK57VXOwfCtk2-xh1oNW49uW1IvwPirVqd40TBSPK5TDvNxI_SCJFekWtuaq0fN_pmNq1tXMv-enDDv9Qet6LKTEMjTf_scrX0U5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
آخرین بنچمارک منتشر شده از جمنای که تونست رقبای خودش رو پشت سر بزاره
- این بنچمارک توسط خود گوگل منتشر شده و معلوم نیست چقدر راست یا دروغ هستش ولی اگر راست باشه واقعا آتیش به پا میشه رسما ( چند وقت پیش هم openai خیلی روی مدل هاش مانور میداد آخرشم چند برابر از مدل های انتروپیک ضعیف تر واقع شدند )
🤝
- توی آنتی گراویتی هم مدل های 3.7 و قدیمی تر Leaving soonخوردن و امکانش هست هرلحظه جمنای جدید منتشر بشه
🪎
- طبق آخرین اخبار جمنای 4 آرگون فقط برای پلن اولترا هستش امیدواریم نظر گوگل عوض شه
💰
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔥
مایکروسافت مدل Decision-1 را معرفی کرد — یک مدل هوش مصنوعی نوآورانه برای تصمیم‌گیری که Jev را پشت سر گذاشت!
پایه‌ی توسعه‌ی این مدل Qwen3.5-9B بود و شاخص‌های آن واقعاً شگفت‌انگیز است:
🎭
دقت به ۸۳.۵٪ در ۳۶ بنچمارک رسید که از نتایج GPT-6 Luna و تعدادی از مدل‌های دیگر پیشی گرفته است؛
🎭
سرعت عمل در وظایف تصمیم‌گیری ۳۵ برابر بیشتر از GPT-6 Sol است؛
🎭
هزینه بسیار پایین است: تنها ۰.۰۴۲ دلار برای هر میلیون توکن ورودی و توکن‌های خروجی رایگان هستند.
شرکت مایکروسافت از قبل این مدل را در فرآیندهای داخلی خود پیاده‌سازی کرده است. به عنوان مثال، بخش Xbox بیش از ۱۰ هزار بازخورد از گیمرها را تحلیل کرد: Decision-1 این حجم از کار را ۱۴ برابر سریع‌تر و ۲۰۰ برابر ارزان‌تر از GPT-6 Sol انجام داد.
این ابزار از طریق
مایکروسافت فاندری
در دسترس است و انتظار می‌رود به‌زودی در OpenRouter نیز ظاهر شود.
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UoBbgMe2CNvyH2J5YY50_TAUlpjyKUkXEuWq7Kv0X3TtcHoifjcQRtNKDjEVq8vx9IqxKG_I4241Bj-_ogJXtSl8oXu9T8ICsQeiOfk8ARq1YTsGGnQ_WIrzXPeA_-myJT8p43ElDIjOY5EV-8tFf9U0yvp5C4Gbwhdz_zB-RhIpgUs9P3GJXk8b_NRNkn7Zd9E_TxemdCitDW_rsKwAj6aZ-TPgfaGlsfaRFi6nVk2O-b5TfYWC3iW0e2jX1r957FLc765TCFdJAOdQE2g9sWaCEPpO6-wCzP5tjQQVuoDtzjDxbzf37Y0Fdhi67j2pRTfVnkz7JsCxdrYH1YQN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
استرایپ OpenRouter را ۷.۵ میلیارد دلار خرید!
‏⠀
‏استرایپ بزرگ‌ترین خرید تاریخش را انجام داد و دروازه‌ی محبوب مدل‌های هوش مصنوعی را تصاحب کرد.
🔥
‏⠀
‏به گزارش رسانه‌ها، این توافق در اوت ۲۰۲۶ اعلام شد؛ در حالی که OpenRouter فقط چند ماه قبل حدود ۱.۳ میلیارد دلار ارزش‌گذاری شده بود. طبق همین گزارش‌ها، بنیان‌گذارها حدود ۱.۵ میلیارد دلار می‌برن و بقیه به سرمایه‌گذارها می‌رسه.
‏این پلتفرم صدها مدل هوش مصنوعی و ده‌ها ارائه‌دهنده‌ی محاسبات را پشت یک API واحد جمع کرده و استرایپ گفته محصول و نقشه‌ی راهش بدون تغییر می‌مونه.
واقعاً چرا یه شرکت پرداختی باید بزرگ‌ترین خرید تاریخش رو توی زیرساخت هوش مصنوعی انجام بده؟
🫪
‏⠀
‏
📌
گزارش تک‌کرانچ
‏
🌐
تحلیل معامله
‏⠀
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کد رفرالا میوزتون رو بندازین کامنت با هم دود کنیم
یک میلیون توکن هردو طرفتون میگیرین
https://muse.ai/join
5UYP1O
50KIY3
EAWL0N
4RUYCJ
5GD9TV
8809GX
9XQLZN</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QN_8tSwD_7y6-LOFDGklWhEITOgzB3OBL7KjH75RI8w0jCLwusJRm0OIS2K-r3Pv3tunZ1s7U9JD-fyaYlt6UqkKLPd2C0owgGtl3x1VqAyBWtks67JS5PJZFRbadwcEKyAKZzEXxaM1ajWdweEez06mo-iLFMiA5Ak0kHuqqc91xk4hMJ6dLIKyEM89IAr7oN3AymOvk49GvyTt8KiM_waLcwVHBo_inJQ7AmeKvNkErF7qjcA9vxi639CYfL1b8AgvTuVw-9kI5A5v_106TMjG3ICU7gkOCu24_fHFfxYFhrE0a7DaNzMgPkis6O5D3Nu_KbZ3AD5ixBZHUREt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
ایمیل موقت رایگان با دامنهٔ شبه‌دانشجویی
‏
🔥
بدون ثبت‌نام و بدون کارت دانشجویی، یک ایمیل موقت روی دامنه‌ای شبیه دامنهٔ دانشگاهی می‌سازی.
‏• بدون ثبت‌نام؛ ایمیل‌ها مستقیم روی سایت خوانده می‌شوند
‏• صندوق مهمان ۴۸ ساعت زنده می‌ماند
‏• خود سرویس می‌گوید صندوق‌های عادی‌اش بیش از ۲ ماه فعال می‌مانند
⚠️
این ایمیل دانشگاهی واقعی نیست و وضعیت دانشجویی را تأیید نمی‌کند؛ پس روی تخفیف‌های دانشجویی حساب نکن. خود سایت Boomlify سرویس ایمیل موقت رایگان با آدرس‌های نامحدود است و ثبت‌نام لازم ندارد.
🖱️
وب‌سایت Boomlify
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lu5pyBRprqcwPtB6zH8cuSFNcVggal-AeHnaK9kPB0X2dHl5ZFP2WhpmQ_fG86i-1L07m7XWY2tDOl8PIV76x0FkVSTMa4_tbUO8ACsK_YbN5ZLGygeXzj7QL0R3ZTwopbr5AF4l8lPzNKaY0Yu-YveAQGDr7xJv8-su72y9SOb5BtWaNFx6_1Wb06nKO4kCzmst3yHQqrKHhHlVgi4SIUpwTfNA6329ScKpnyJl1htiAuJ0CgFzqYel0dUTY9R_FY2h1Q-wB11PlTkF3pZTUu6GjynDaOXhYANz5OrOPZ49y0wCQdAgrewYOvyPDWLNySgTIYsT_U6uGs0m64TuFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📰
آماده‌سازی مدیران هوش مصنوعی برای سناریوی فاجعه
‏به گفتهٔ Axios، مدیران ارشد OpenAI و Anthropic در جلسات خصوصی سناریوهای یک حادثهٔ بزرگ هوش مصنوعی را شبیه‌سازی می‌کنند.⠀
‏مدیران ارشد این شرکت‌ها از جمله داریو آمودی و سم آلتمن روی سناریوهایی مثل حملهٔ سایبری به بانک‌ها، اینترنت و زیرساخت‌های حیاتی کار می‌کنند. نگرانی اصلی‌شون موج خشم عمومی و فشار سیاسیه که بعد از اولین حادثهٔ جدی هوش مصنوعی سراغ‌شون میاد.
‏سخنگوی OpenAI گفته این مانورها «ابزار آمادگی برای نتایج محتمل» هستن، نه پیش‌بینی قطعی یک فاجعه.
⠀
‏
📌
گزارش کامل Axios
‏
🌐
خلاصهٔ فلش خبری
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=Qa3L4ZU4NzESK_PQOv87eo5panikIUkWzxTaubbr6mzPz_ENIdwBLe3zmTeLbsftn1yFNBbAl9y4E6vI_CLCk57iO82xu36ER9ycIhmMWS2aLStsK0Ng3Sj7YqLZyxMUWdK0OKni7FdeHcYTHH0vzm0ha1J_TxRdmZ558TWRMlFgcIObSfaNAKFtQr6WCMuoZWD1mng7COhw9iYh9Jv2Bc21nBahoKf1HIVdkt1DtWpMVvGn4IrNMyTNBvgp40EPrI1YBzOvIgcyii0pGRwXmh7gYoaE64cS5QcNuxC6V3xKID6BHDsmgVsTP4a8dkHcOgbaKihdOlm6q1nV1GIG9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=Qa3L4ZU4NzESK_PQOv87eo5panikIUkWzxTaubbr6mzPz_ENIdwBLe3zmTeLbsftn1yFNBbAl9y4E6vI_CLCk57iO82xu36ER9ycIhmMWS2aLStsK0Ng3Sj7YqLZyxMUWdK0OKni7FdeHcYTHH0vzm0ha1J_TxRdmZ558TWRMlFgcIObSfaNAKFtQr6WCMuoZWD1mng7COhw9iYh9Jv2Bc21nBahoKf1HIVdkt1DtWpMVvGn4IrNMyTNBvgp40EPrI1YBzOvIgcyii0pGRwXmh7gYoaE64cS5QcNuxC6V3xKID6BHDsmgVsTP4a8dkHcOgbaKihdOlm6q1nV1GIG9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
✨
ویجت‌های وب داخل پیام‌های تلگرام
⠀
‏طبق گزارش‌هایی که از نسخه بتای تلگرام منتشر شده، یه قابلیت به اسم HTMLBubbles پیدا شده؛ پیام معمولی می‌تونه به یه مینی‌سایت تعاملی تبدیل بشه.
‏پخش‌کننده موزیک، محیط اجرای کد و کارت محصول، ‏کارت پرواز تعاملی، نمودار زنده، دکمه و فرم ‏همه‌اش با HTML و CSS و جاوااسکریپت داخل خود پیام رندر می‌شه و دیگه نیازی به باز کردن پنجره جداگانه Mini App نیست.
💡
هنوز رسماً معرفی نشده و معلوم نیست کی به نسخه اصلی برسه.
⏳
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hJTx0OugK8X9h4cwy8Xrr9NI08XZ_j_0bAJ-E32qFMISGLdFadOKjC1WPGgjze3Bvozbpd-gSb8wlTWjlrzWv5sq18yq9o2SQ2Lj7uAXoZNCFiToXpBikQsK_QQ6yvX8hZW8nU2HAZXQz8qTbKafRladXKKy85WQtKBV3VnUNuQnZ3iavVc7FG8yn9m_e1-lEcxmpuLzpqAcQpVpsTbcg-DevhU7odNx3BlJeWbPvAkGDgRhzNI2HnZvnpisPwRUk_g1Uouk02UifJiNpjMQtYuP4giAmP7mCtmghuGV81O655p2VDMr5O3jjlXliHrPJrgJE1xZKzwP_1TpsVwdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎹
آهنگ‌ساز رایگان و متن‌باز Tonefold برای همه
⠀
‏بهش بگو چه آهنگی می‌خواهی، آکورد و ملودی و درام را به‌صورت میدی قابل ویرایش تحویل می‌دهد.
⠀
‏
🎼
آکورد، ملودی، بیس و درام در پیانو رول؛ نت‌به‌نت قابل ویرایش
‏
💾
خروجی MIDI و WAV و استم‌های جدا؛ افزونه‌ی VST3 و CLAP برای DAW
‏
🤖
موتور آهنگ‌سازی با Claude Agent SDK کار می‌کند؛ می‌توانی از مدل محلی Ollama هم استفاده کنی
‏خود اپ با Rust نوشته شده و برای مک و ویندوز عرضه می‌شود. قبل از هر تغییری ازت تأیید می‌گیرد؛ یعنی چیزی بدون اجازه‌ات نوشته نمی‌شود.
‏نکته‌ی حریم خصوصی: برای آهنگ‌سازی از لاگین Claude خودت استفاده می‌کند، پس متن و ایده‌ات به سرویس مدل می‌رسد.
شاهکار هاتون رو حتما برامون بفرستید ...
❤️
🤝
‏
📌
سایت رسمی Tonefold
‏
🌐
صفحه‌ی Tonefold در Product Hunt
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=XM5Mg7rFoS_5-WKuo6B0KM85r8uoNxqfnLKkVvKozEuaJC93-5mNsFWNxsdQe8XK7M7eM5LWMw4e5iK7MgpreUU6ZsY1sd7MF0fLRnTvuCUo0ygSBNVAes8KvF50nXdPkm_qZDVqy8-0KnJAP6Po8-jyzIjAF7ZV_4gtbOgOon2SLk0ifruCSUGIrSssMMV9keA00nqqkIscq1zZK-psyHBXUebkghPzFVrPf83AoEcvQxWR0AhsChcFaMrxQ5T7GuBwt0vGH3MBpLh_P8ttlsJyjjCwBQfkZnhB9Cy2Qf1Y2GqqSO0pVhCMMeK2ZjdFPFUf8w2fygpclWC6atOMHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=XM5Mg7rFoS_5-WKuo6B0KM85r8uoNxqfnLKkVvKozEuaJC93-5mNsFWNxsdQe8XK7M7eM5LWMw4e5iK7MgpreUU6ZsY1sd7MF0fLRnTvuCUo0ygSBNVAes8KvF50nXdPkm_qZDVqy8-0KnJAP6Po8-jyzIjAF7ZV_4gtbOgOon2SLk0ifruCSUGIrSssMMV9keA00nqqkIscq1zZK-psyHBXUebkghPzFVrPf83AoEcvQxWR0AhsChcFaMrxQ5T7GuBwt0vGH3MBpLh_P8ttlsJyjjCwBQfkZnhB9Cy2Qf1Y2GqqSO0pVhCMMeK2ZjdFPFUf8w2fygpclWC6atOMHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪐
سیارهٔ تازه‌ای که با کمک کلاد پیدا شد
⠀
‏یک برنامه‌نویس با کمک کلاد کد و کدکس، سیگنال یک سیارهٔ احتمالی را در داده‌های تلسکوپ ناسا پیدا کرد.
⠀
‏شعاع حدود ۱.۴ برابر زمین و سالی کمی بیشتر از سه روز،
‏دو هفته کار بی‌وقفه و بیش از هزار اسکریپت تحلیل داده،
‏و هنوز تأیید نشده؛ قرار است تلسکوپ تس دنبالش را بگیرد.
⠀
‏اولش خیلی‌ها فکر کردند توهم هوش مصنوعی است، ولی چند پژوهشگر سیاره‌های فراخورشیدی هم گفته‌اند می‌تواند واقعی باشد و داده‌ها برای بررسی بیشتر رسیده دست ناسا.
⠀
‏
📌
پست اصلی نویسنده در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCaUc-FY4c42K1cqk0RbR-lnQlv8UYFYY-z5bvNRNBdwb94t2xpsGTLas_-I3qVuPbTYkmOwbBu5egZnPDBr7wuLqPDVZjBEyVysS9-UPKOVm86UZ3k_A8KNmUsRlDelTUBSGL8cGt8TijqHQEYlbdDP1y6ar8pCeDrhRG1NABeV8AZsZ9PaNFpJYO1WHCwzBJmX4CCagA9kNkg7HMUcW9z8Bu2jx9DABqcaKMVsfs-szksguLE0lf_OuyGFE4WVw3SsORecCRUOQgxOlnXvNzN8l-3K77-qw_6Ctcj8F0uYVrEaHLy3LsZCwqrNPA2DghdPfiMGzoaUVpS0GEOnnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le1Oi0yBY3DG9xFLVbKRj61LW7JlEKXuChm5UHcRfQIQUyNdFW7jkBMmYyAeEfg-1Vxr1rFFcVCqAe7VKa9YLeB8TTbUwgzfVz5hssXVn2UHhz3Z3RfzlMD8jhJcjWBcwDWZlYIOkrQIl6Hw0FybWYlFpu7VefuAUXxvTJrHN5Cn1XHv4JZGsTkyT7VH3vWgdzMlZD-2q0efUyiyR6yya4u8_9a4UzCNTLpETnvQDYWU4sSc2Ri80JMIc7pTfIg4G2zgh-D2cJW-q1-EnyofCDh-sMi7HTCZ53YYnFmnglzJjsL_qgf9XtKbxhyMeTgWY6TYvvzgRaNT1CsK3q5RgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIt228IGn1N-8z7HKPduBD4u5XdyyD7IwwzHSQNLZfVrIi_JT-jP9zQ-dYDoXP8mwjQkgxtgUbvPWEvlK0h0VqGDK_D69D2BSRDGYpv9RFGUG67APosmVR-cNqyFzhCzG-qWf6pDFAP_LwBBo-WRAMRzGHJX3AcUNjS-JpKBqbBp7diml9jxM8sjoYSXojZjPRe6RfqnaaI2lXPqJdmVICf6pAoHKbyMJD8DJdYn3RT_EKzR3w1rpGSUT4lgKysw36k_N3JSl5pbgkLkOLb049728n95zc2ZLcFzMSJdNI-ix3yaoJahybqIlrA0h05lw1zZDOArWVL3kCVJOGpXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
متد حرفه‌ای تبدیل PDFهای طولانی به Word با Antigravity
اگه تا حالا سعی کردید یه جزوه یا کتاب رو با SI به ورد تبدیل کنید، حتماً دیدید که بعد از چند صفحه کم میارن، فرمول‌ها خراب می‌شه یا پرانتزهای فارسی به هم می‌ریزه.
ما یه ابزار
متن‌باز
و کاملاً خودکار توسعه دادیم که این مشکل رو ریشه‌ای حل کرده:
✅
فایل‌های طولانی رو بدون خطای حافظه پردازش می‌کنه.
✅
فرمول‌های ریاضی (LaTeX)، جداول و متون فارسی رو کاملاً سالم و دقیق درمیاره.
✅
خروجی نهایی، یه فایل Word مرتب با فونت‌های استاندارد دانشگاهی (مثل B Nazanin) بهتون تحویل می‌ده.
🚀
نحوه استفاده:
فقط کافیه فایل PDF رو بهش بدید تا صفر تا صد کار رو خودش انجام بده. (پرامپت‌های آماده برای مدل‌های دیگه هم داخلش هست).
🔗
لینک سورس کد، ابزارها و راهنمای کامل در گیت‌هاب:
🥹
https://github.com/faithsaly5-stack/Antigravity-PDF-to-Docx
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJhWrh6uZXDkZsNNmdS3VscBl_IdhsfHTbR-X5puQvjwAlzenbpehcgonk_gfbtLWq7FCW77vltx547rkI3POcEZAOd4MB0eoLorcggIV0z3xu2n5TF5_WLw9KXRopOkr20ciAX74QP--abUYPk8QCtpUf4Ty8kScot8Quiwa8Q2nl_HGrSUKi7Q6f2U03WtCOHxqMJO7vD0V-QgSt1UlyW-wXUGH4zruk1yucj6vJ1yUM4a-6FhD1I2O6_Ud_5NDcNzEnq_cpemVlwwJDgUENUREgZv6ofQuRQY0OhqOyr-QzFjvfA4qmtrWswioLeAPG65XcYKQazVgtYPRJRaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TL3Km-vB9z1pNvO7avJYKooxOR9hW3ls3ikaytgv09HtUbAkwRjpZRkCFDF-7Fv-iO9BEM453-bNdrvS70t3Fs1rEy_u400ogPpOKHLacyCU6oEj9CklUYnKV24edGKF9Vmc9rZq4y4ZtTxWCSndJfjccgriINytqIG9HuperbqJklckZsqxgZwoACZ6dMeY_rt1AILdmLXWN7xe34PDD7vgZ1st_75QU5LvdjGHbgvugjDjChNMVDI-OPvsDMp9fLCnC6kWdtXlfyg2Dcd1s0IOX622TRY5SATxd3WXTCIMBor2fFclBIUSu86fZcSsZ3ZtojVkhEnlVAqXvV4Omg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">#حمایتی
‏
🔐
برنامهٔ غیررسمی FoxyVPN برای ویندوز
‏به گفتهٔ سازنده، فیلترشکن فایرفاکس رو بدون اشتراک روی ویندوز بهت می‌ده.
‏
⚠️
غیررسمیه و ربطی به Mozilla نداره.
‏
📥
نسخهٔ 1.0.0+1 از بخش Releases قابل دانلوده.
‏
🔐
کل ترافیکت از این برنامه رد می‌شه؛ اول کدش رو چک کن.
دولوپر از بچه های خوب چنل
🚀
‏
📌
مخزن پروژه در گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=D1jXTXQTg0HXwAXQcIE6ILn3C8nMdMv4zFjCbQsx_n_Mi50NUrfaYt1VnJmKEqqueibcAIDltkfZz29xO00JezDNIg3znyTz1zUzyKSrdF4xREVG1ufbNgL6ufCzGrpYkrYhR2wOI45Bf7irBwBZ6PDx5S9tAQX-pCBgrYB0WP9Y3iKUtaelJgV6kaUWxrwepogqzsbV7RKpJjIB_9_W6oAN_FmLveLT9Gxh8ijmcDoRBnxaUQ-1aNNnc5ReSnp2Rr9g3_DXrO5xnRM-lf34R4iYDa2ErcB4SCoeJHEawCCWULI5PAo_jXNEcepJ1P3LARmXHiyrRwbeZPrF81GWDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=D1jXTXQTg0HXwAXQcIE6ILn3C8nMdMv4zFjCbQsx_n_Mi50NUrfaYt1VnJmKEqqueibcAIDltkfZz29xO00JezDNIg3znyTz1zUzyKSrdF4xREVG1ufbNgL6ufCzGrpYkrYhR2wOI45Bf7irBwBZ6PDx5S9tAQX-pCBgrYB0WP9Y3iKUtaelJgV6kaUWxrwepogqzsbV7RKpJjIB_9_W6oAN_FmLveLT9Gxh8ijmcDoRBnxaUQ-1aNNnc5ReSnp2Rr9g3_DXrO5xnRM-lf34R4iYDa2ErcB4SCoeJHEawCCWULI5PAo_jXNEcepJ1P3LARmXHiyrRwbeZPrF81GWDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKuMSGrYUUA7sdH4I_j7OGcloISkXQZfHXfZFYX28RCm5liY9SmUpHXyP_tXvH-6n-N-jjUGFZ-veHv5dGopVTZ8V2JO2LSSnD2aRNC9b951V9xciJ-iWLvQEk3o-EBo4Wy85FCDpgx4dDH4ht_X6ZqdmzBCW_nxMU8Tg0j_ySQIbhRxiQ3Z-9iUVS2PbQZmtIwAVLHQq0fmNTwJn63EvGtvnKMfKWxUZmzdQFoH9pyFiHZF1FE0YqLs6_ld9F9ZJdzFQqqMxjOjT4F82Dchks4MfjHzY2WJBiVkgxkExas23LECfJZrW7Nq2SEtr8jFtRr6A3z0biChUnfGIp9v8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪙
ای پی ای Tooken Club برای مدل‌های معروف هوش مصنوعی
نحوه ثبت نام توش خیلی راحته فقط کافیه ایمیلتون رو بزنید و از کپچا عبور کنید ( یا باید تصاویر مشابه انتخاب کنید یا یه شی ای که خلاف جهت بقیه حرکت میکنه رو تشخیص بدید )
‏
🤖
کلی مدل داره که میتونین استفاده کنین چند تاشو مینویسم :
claude-fable-5-1
claude-opus-5-5
gpt-6.1-sol
gpt-6-astra
glm-5.3-flash
grok-4.7
🎁
10 میلیون هم توکن میده برای استفاده اولیه که بنظر کافی هست ولی برخی مدل ها ضریب دار هستند که میتونین از بخش  instructions بررسی کنید.
Base URL :
OpenAI:
https://tooken.club/v1
Anthropic:
https://tooken.club
‏
📌
سایت اصلی سرویس
‏
🌐
کاتالوگ مدل‌ها
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9x5PqpH5G0yOO5eGS66bX61pOJlS8fBeHlLzNVGjC4twKC7JFzEybqR0Ct0N8qZ53iLgP4Ii9uk7p2CiYy7AuYpmXxdBJ0suo2sDMVZGi6SDN7avxfKCJ2tTro2fu5xW3gVWqyTAS3rcAAqnGWLSkZXqWzCCYdGaCdNuh9868nFsNYVOGiqOG5PhEIRmoMX4aMcK77-5vHZ-hfWcs8nIQmLE1CM8vTlgaUuFpapUEymKulPK6z_5nTU6i3lZ-GGzgifw9jNj8Zufe8eO5JaeMpqGYZ5Z2ALJgVIXwQCwfgaDkfXaFJFt0TIbggfgAB4cx48ppHycY_2k4LHgafrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZXDtGdbTBZuud4i_pd2ep5lh_kUR0lA-Qsss8yWdu199DI4tLQwejn0wPD78FAf291ElxkfjEq_bKnt1ARMU3GaBO5cCOJdoGbzasT8D2LUBfeVh-3uHhmdWecb4_XinLgsCNjwaajNSjqTsbYlpB8s1_wxY-ZKS8O7TW4Q03kDuyMARhrs_5D6a8eR1UtukWh7bVXx3OBGZlKJ3S6zzVYnMmbSvyvC-qiNfB6kSGkEL7nITSFelh2rMmqMHREdcq_5KCW5dAfkn78QzMKs9UgukWXrJ4vFVScV-DTAQK8kjBjO6KdrzfU0Kz4171m4X6W0FcCtZU3ESyX9UGinBrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها
⠀
‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده.
⠀
‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه
‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه
‏
⏳
اعتبار ۶ ماه بعد از تاریخ اعطا منقضی می‌شه
‏
🏷
روی اشتراک‌ها اعمال نمی‌شه
⠀
‏این اعتبار فقط روی API خود Anthropic کار می‌کنه
⠀
‏
📌
فرم دریافت اعتبار
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=lMipDAJIjEtKOPHcRJD1nO00hpxUXQTVQYIPAh7koJ-2mBbYKP4UKhL7nYD6usQdCt72wZ-9CvNdpwtO9twFwzSFa_w-KqSdUU7Cs4t4M36wLPOKX3tf53MTVvNrLMKmfWMvBaCrhRvHgk-yNgzrMxvKo0P77F9YlcJq-wO-P2mQuOId0xzzmYkPL1DBdzfOjE-7nZSC4TiQi1dHxLgMgs0yVh-cTxzrMBwhn-9hnkkSPi8EUhKsMaEygE0IYklnCl3je5C8VhfBFFzQygTPKc4EuRARE3awV8rZ_LRIjI-Vxa24kJJDEd59o5nh-ftQDyj6r3cS--dk8iF9Kk8Q6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=lMipDAJIjEtKOPHcRJD1nO00hpxUXQTVQYIPAh7koJ-2mBbYKP4UKhL7nYD6usQdCt72wZ-9CvNdpwtO9twFwzSFa_w-KqSdUU7Cs4t4M36wLPOKX3tf53MTVvNrLMKmfWMvBaCrhRvHgk-yNgzrMxvKo0P77F9YlcJq-wO-P2mQuOId0xzzmYkPL1DBdzfOjE-7nZSC4TiQi1dHxLgMgs0yVh-cTxzrMBwhn-9hnkkSPi8EUhKsMaEygE0IYklnCl3je5C8VhfBFFzQygTPKc4EuRARE3awV8rZ_LRIjI-Vxa24kJJDEd59o5nh-ftQDyj6r3cS--dk8iF9Kk8Q6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvIH0T13yVCDHTbRWqGDq3T2AwUf7PR6i7FVsFZD-eeRGOfk2EpU-AyvJCbTIPVvgOMEL8-zAPYAaUfPh2AKznRyCIBe1iG46gYUJRVU_Xq0Onp7riubAWh6HGuDSzXwMlEu_Uo8C8ZAKaCXIcPxZUQlYzx90P-gZ_Dk1TqMhcERuz56qVSZwUpi5NTL85XeBrN_6zAyQ3iBkNbT1gGtMJSuvhzEywkepTdGyB3JSwNZf4HpAgsTGkyWxhM0BZAFtt5skYgQe0itEg8RXDliLksK9ASxNJSTyeLkV3DHYsr_U81uNpAJdanJztU61FFg_efI_GyL0zajh6sJ0D7Gzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نه آقا ببین ai که حس نداره، نمیتونه عین انسان حرف بزنه بخونه
❗️
🤣
همزمان ai
⭐️
مدل جدید تولید صدای Elevenlabs V4
⠀⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EiSgiy689n1eo8MeaiojseIbzqp6D6I6GTALg6UE8dsv1DCpLPL1xMYNRtk7OSrBgBcg55K9p59W9mfJm0U-Y1bJ6If8TXZbdj5SXbII6QkwlIGkW3dEpfm5NluMLWd9zWkGB21RNBunZQkz842uPvK7tQ1czUIBzii93cRNquVaVIQZydPbYmuwoX1BKLYFUSDIr-2XMOMGbt2TcDKB_vZ36uKBRIEgIVKVZdQQzRi9ZzdG19oZDUFjGpqzpLeLk8QsHFNgG2oA7pLKTPJnZfzJclzzmoUEUcJ5QLQ5wCIO9yFl2cOP6pV2WGOZcJHFZUCtTYHsN60qPDNIXVMTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ve3aPdTLC5ZJ9E-Rwyv1uIPSgwalUY1qvG7bHkQLJmHHsiquvjItMzn2J0O-QJ4c3C4RjtPZfBA1zVsuQqC2lyTk8_WFJmlFhhHOa1zcnqT23oDCzgR_sPnK0PGX7MfpdzSmlvJpGTtdmO5rcx1jFbEiKJtrSeAN5J7b0PLCEhmwNTq3nSnHK9D8WKn_8beU4L9erQASdXC032fHL9UxsXRystALye6EbvHIvwdrQ0DKEVIYkbfWVsSsuBcyGOQV9aRJtKcdl5BsoXZO8g6VwOXsiv9w8lsxHKstLvAxWDn2II3Paf5-IgP_CKG8Pwt-YulfL_4QYDLyNJZEsYpR_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXoAqyfPNEnLEx8yzxxwA_x74RAxkqk49Wok6d-dGNG0UbF-iK-gN5ot4gvZxrfYtY3TBUBjB-U7mfP-VINAsELuf1sOHvXfn0Dn5nCVCLBWShFBaMv9fvkGqm36dcc8yBsJkdDpe5LzvjEA0STo__wwabVMT2xP0N7gJy4IulFDrnlHt43FfZH10UUWR0cgobiL7OMD5YJNzi0uMXqSF5LhIb0XRaifzUx09CFs_JJD3IINCISYl2LevUrrOgL2BkrVBNB1339ld1lgUaZOTN16HI0Y237IT68932nfMOu22lipCh3LjM9_YesrPprMtUYbPhM7rTffjyIBip1xYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNUMqTROKmT957PkO2IzbhIxSGxcbi7Sku-2gRZJR8TOSSWrejAZcw6EZjnSwUAcj8ZH73kR339_E0LY4dkuli7XA6ZB4xnv5C2kRprNXRfD-9W2nPVS3L630jZfM3LELCf_PSbtCbGrNUMoIznlrv_FGcjzrpj73UDUPfEQ3S5GVZwV_zV6yiF-mnjXeKG9b10HQqtxpfztaR_Z3VqSJC28D-gU6EfMsBTLI1xNR86reZ-MVaeG-BCGuukCbQkdQFrUjrcWozNbaU1PfO3cnip5yZlfnR53T0NukIyEfi53VSxC7ZxX4Ep20Cmo1oQjXADrYrqrhx2lp3s9hAjmLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIFoUsRKA5p4oasKLS9JORP_gKv3u3s7RPpeOtYCZ9D0u7hERGtEcv2ZmlD75WCSqV1Tq_q6I58f_cxCha1Cbziph1AETY2ylcoNb4BE2C8tsDNCWPlO85PYwy_2wT9be3c-z5eBUuuLh4lpIwOoIrpSYHZmSul6_oG3ZQsTbfKlj-rUxOAbVDrGnUOcPk0ZSqpRWE1KJl5-mqbzmR6ULuKLBWv-QN1--lQGek2D_y3ZlfK_6DFsVxIZ4AoIuadE5pXsFY2b0ulQ53ug8RJMfz-qa-3U0xji6_HxIiXaEP-BzUTM_8DROQhH0BJx7O3UCg2ZRD7X7dFddbT9tmYP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avvaYtdOrtv6k5H2guJ5G5HjEKol0KQsbrboxv4c30d28n6r62zUJxGpGmVfjdURVHcdmqIn4M0i0-BuimbRWrOP4axgJSEnEbWzLAxAi-V3lN5T1QXQl4RFLA272na10y2qxWt7fXaPeBVZbD1kRQaGHjMnMM6FDqTHsnYlNKqBNx9XBsZRIdZ3xmvfjzIrE87AN-WpCUqb48dMBlC92aCTenEqemWQKGzD_4ig_eM9t0j2TPXmdVyZ7zGLpsAM3PkU6wWqMIR1FP64f1-EC6oq49TzBXS8QSmst6Yt-wIDMUqPoBDfZNkHy00RyosJRalQTHuwtsNyqopoaIr_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pmQokj9WoAI155xjWFNRlifJ0eQtylvTkVjuzuYoA5h34N2QAmAckGkVcGDKGAxEUIstrjthDlX5nsdxyP7w-POOqUf4RPHDH768_T22dutyX0B_xKRh2IJghE8SFuDP5vJF-9HHH71xI2Duf37j2c79h6KmZd7CVgNkvAYhmWf8gKDDOu3ekX1BY5cjGdUy9yP7yOteEZSWkF7GrE7CXIvYGs7z1AGYD4GEQlkXWJo3A4FLZ3ScBAVbVoSZsxClL8dAGTBPyBsjvWrQw6tahy2xXEaHdew2BJZVDszsBkDfxPr2exap8AK_BsTCnMklDNgBPgZlhZKjeRRrHtAgAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fD04LZhS3bOx6l-3gF_s8zdJZ9QICzG5iBL4WvozBxdUyAmLbRyJHqpUTpvahqXNTuXfl8nlndf8FtpyIoDgT0QHjWqgIn7sWOwNNgVCkXW7oCEMOxqRclun_aefjViX-QtiQAx1ZLfQUGRjgaGWG8oPxb1UEIxIiygajpSIyOiCeESHJ7bw2MBHxn0ZYvJXHIr58EdwT8sL_RFnY2D6XSI1iIM9sX9EgqlH5E94mu3joa7cPYXY7yZAMvYX_aj6b-uz6lPqSHvPPeTVV7KEN0fRM9PBvbD1s_7tkwglH9GA_pE1skO6n1TxLMCRpze-_Y9aM4yFJMSvSp5za_rv6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRh4M6YPJ3CXuoZKARb-bkrS0meHnvkOQUVO1mijQvGAlKTUCbmU_b1kGyFTw0WDtBItggIB8VdN6SxWKMbVKnH5IhcX1t1I7m2ABTNgJ6D3608s8N5QW6RVBmZ7hqbJ3zDsGZkI1GkGvsmrYqZGKCUWHvOhaP7AI82CLH9HzKDVuM-i4S6X7T2oMOnWI-O5ExqBYxVIZG8jS3-9z97sufF-0raICLVu6DknUGuaZwFZqVZSLLIu8OUWdjhSkskMU4KQ6FV6WEnU3bdMc4klyvIW0h1y0moynQB4bMwVNHzwSwr5s23q3UW8iu-xEztUs6u6VCtn917twBUjU8bh3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sw3I5T8A_lqXpOhTW3uxOfgCvfGogq3zoQT4_EDs0PujxrKxFRqh7-_n4dVK9jLPr9YB1xBhnTf90N1m55vLkMo8kkKzA4CoA9w9jVXOakTcqSFfKJtpqc4thFqT2UOJFoVaHy0MnfKfGd4ZDW0YXnap-1zmZuJl0RAO1xuG8VgCvqFqyEU6lCPsz_NCgi5szmJ_XTnreY9au_MxY9__RLkouk5nd1ou_VgNXTUiSg0g18LE0t5GYXUqDZNYmSjKPjbRH9r81eGyRDrQPX8HAEOXlwXaQsCdvDmVkDLE1ebGnlOT6WcBvjpJ8Ow4P3AEiMM01F6QqOwbe7DMXGJOTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✨
بنچمارک مدل Nano Banana 2.1 برای ساخت تصویر اومد
‏به گفتهٔ منابع خبری، گوگل نسخهٔ جدید مدل ساخت تصویرش رو بی‌سروصدا منتشر کرده.
💡
به ادعای گوگل، حالت Thinking توی اینفوگرافیک دقیق و حفظ چهرهٔ چند شخصیت از Nano Banana Pro بهتره
‏
⚠️
هنوز ممکنه چپ و راست رو قاطی کنه
‏
🐞
موقع ویرایش گاهی روی ژست تصویر اصلی گیر می‌کنه
‏
🔤
متن ریز یا خیلی طولانی تار درمیاد
‏این مدل روی Gemini 3.6 Flash ساخته شده. به گفتهٔ کاربران، توی اپ Gemini‏، گوگل AI Studio و API در دسترسه و به جستجوی گوگل، Ads‏، Flow و Stitch هم اضافه شده. به گفتهٔ گوگل دانشش تا مارس ۲۰۲۶ـه، ولی منبع می‌گه عملاً از ۲۰۲۶ چیز زیادی نمی‌دونه. گوگل هنوز پست رسمی براش منتشر نکرده، پس این جزئیات رو با احتیاط بخون.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9zgHSKTUrZC9jIEAFaMYM_1LguYPSvXhXgEcf3iJ_Ho4KpdWIiQh1V7sfHHV5mj_uqBkbFSmpYXT4c1VVRviAFcxjBJrNdZ0zMz06tQdJFCADKVS9p3sNOeRFMcs3g9r8u_s9N-V0Wv5Ag2Jndz7PU703djCC9tnFhlyDTTC4eOeN2MAivVBPM77dADD8N-szxcOgHfiBlVt0jLCvq3eAjtwd2b6Im5eBToHp1ug1qMb9d1HegZjZkomond6i7fWgdt5Lw2HhqglaCZBXO_UBjPMyByqQhg_TEm-08Iitqj6SAAPVUr5nP09lE0BeEuVmPvfRJ2SwpAwcYlwcbKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TSyW1wNrMSrG4zwHU73I2hnalRzt-N4AKJ-24bhCOnwAWLvNomr4DuzFF2k6dP-3Xv11jP4R8TfPs-A7_JksDgzgem7WGLQMz9urUOJ1_px4skWZSYYJ2ZRLJw6wrdEsfVjYQzgQYNWqmumuVOGnnymRVWYA3KN0ISPUCoC1nz0YSShNksE3q2DOrPrB5JRoh6Z4p3WOhv4mphiudd8_hInJmOt77LW8xOURHrZEK3dQ8wsbpwsDU_-DIITdFYkbFynZ7YNAQ7fQq2SLRcRQLMpmZtdDqDgpqrpmjBrEoOO0LJHuGdvIhMONqfUwOfwew5L2cTv_q4KDtbnk_jGdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚖️
وقتی هوش مصنوعی خاطراتت را لو می‌دهد
‏
یه زن تو فلوریدا به Claude می‌گه می‌خواد به دفتر کلانتر حمله کنه؛ فرداش پلیس در خونه‌شه.
⠀
‏کارلی میشل هلر، ۳۰ ساله از فلوریدا، ۲۶ سپتامبر توی چت با Claude نوشته بود می‌خواد به دفتر کلانتر «حمله» کنه؛ فرداش هم نوشته یه اسلحه‌ی جدید خریده. خودش به پلیس گفته از Claude «مثل دفترچه‌ی خاطرات» استفاده می‌کرده.
‏فیلترهای امنیتی Anthropic چت رو پرچم‌دار کردن و بازبین‌های انسانی خودشون به پلیس زنگ زدن؛ زن بدون مقاومت دستگیر و به اتهام «تهدید کتبی خشونت‌آمیز» متهم شد (تو فلوریدا تا ۱۵ سال زندان داره). نکته‌ی مهم: چت‌های پرچم‌دار ممکنه توسط انسان خونده بشن و سیاست Anthropic اجازه‌ی اشتراک اطلاعات با پلیس رو توی شرایط اضطراری می‌ده.
⠀
‏
📌
گزارش Cybernews
‏
🌐
گزارش TechSpot
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi4NAdgqnp7867-6kld_fNdcHOxE7ZiKpL8g6qMV5il1rfW-HH_ysPhPZJen2eaM3G_P_lWlOes2GAb4bFKiwJYj93dA3AZ_OroyHsuYi9on9_m8Yy-QrzARUYcHEZoTkYrJsCQakg8lv6lsv8Kr71FjjPfn6GzQSkLt1bLIjUqJsou8kDjP1qHkPSIIN8xsnT20Xr4Vr1TZ9hiBoNi0WYsl9wKkIY0AOSOGR1DF9K_eSsYJ42LuLkcUmr3uu7wsD78zyHLQZvUxu3MGWnRoYZEogmmCyMnJHkN8dEOM8eLOUWa7RA369OYw2rc-vQ3SkTTXaRop-OWWCVAiti24gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🕵️
هوش مصنوعی رمزنامه‌ی ۲۱۷ ساله‌ی ناپلئون را شکست
⠀
‏یه نامه‌ی رمزی به ژنرال مارمون که ۲۱۷ سال هیچ‌کس نتونسته بود بخونه‌ش، تو ۶ ساعت باز شد.
⠀
‏این نامه مربوط به مارس ۱۸۰۹ئه؛ دستورهای ناپلئون به ژنرال مارمون، درست قبل از جنگ با اتریش. خط اولش فرانسه‌ی ساده‌ست و بعدش ۲۴ ردیف رمز: ۱۳۰۰ واحد رمز با ۱۵۵ علامت متفاوت. کلیدش هیچ‌وقت پیدا نشد.
کارتر چرچ با GPT-6 Astra اول اسکن صفحه‌ی یه مجله‌ی فرانسوی ۱۹۶۹ رو رونویسی کرد، بعد رمز هوموفونیک رو با آنیلینگ شبیه‌سازی‌شده شکست؛ کل کار حدود ۶ ساعت زمان مدل برد. حتی وقتی متن‌های تاریخی ناپلئونی رو از حافظه‌ی مدل حذف کرد، به همون جواب رسید؛ یعنی رمز واقعاً حل شده، نه حدس.
⠀
‏
📌
گزارش کامل رمزگشایی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=adZF0jOjnuZVbe0jVTulfjHePnvmrgXGHL2VQ37gVcep2fKhocNWZwqJob14w_kEE4rgyEOORWYJAYqWYHoIbF_LzFW9SQgF3EZJyngxMkguq3TVdscDAiU-CDlwCUIhw60ZQAcDBLtLDqb8N45WXl8VZw7_BDgZgJzoxvAkNyUfVL_DWFVgefpeLYFtWCI--MKjMnsb1LTdisNEuwSQ7_HK42WwJp0ScMu4_o_DPBSH-X4a7-kodqzdaIzWHm3atdMcRjSYDxDy7NKsCo2eG2sTFPNcsb23xiz1PDmJELTtEuDskNWLnqgPBbNU83eckrONQjwLasOAUJAG_08r1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=adZF0jOjnuZVbe0jVTulfjHePnvmrgXGHL2VQ37gVcep2fKhocNWZwqJob14w_kEE4rgyEOORWYJAYqWYHoIbF_LzFW9SQgF3EZJyngxMkguq3TVdscDAiU-CDlwCUIhw60ZQAcDBLtLDqb8N45WXl8VZw7_BDgZgJzoxvAkNyUfVL_DWFVgefpeLYFtWCI--MKjMnsb1LTdisNEuwSQ7_HK42WwJp0ScMu4_o_DPBSH-X4a7-kodqzdaIzWHm3atdMcRjSYDxDy7NKsCo2eG2sTFPNcsb23xiz1PDmJELTtEuDskNWLnqgPBbNU83eckrONQjwLasOAUJAG_08r1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvNXJL1ge0NrdUrGfu8WGtlwl0e1Y2WlMvJwvEvYfH5oaEEtvqyn1CRlSrdPXH_TmQD3bITxW9Z9Qm-WRgOa4utK-5Hd5YyoZT-OSBZt6FTNsZ6Jn3gQ6A-iGq7t4gmWp-uFZbUQZD5STZlkfbaPJLaLuIejjF9qK39K24hGF8Xets5uHUz87-hjsn1Eq-n4jA5GhedF8G-zZSKSNjq_pJ1lcUsgZ1wZMeRdeZIOQtT19fLiQDqOg-3hQ5ktMYvuQBuD_EOk20dqJEY3h2E2ztn9Vf5K3q1h1FxZZehxPeUptY7AdmohTo8s04J-nXRkAoySR4h37gSW0bOoIvJ28Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4ibSkes9gdQMK17bV9tJn8KhSS0_lM6dMKbFfmvF-9S6T9tfBPlEm4rXhxuFohTqB3zw58PIS3SjKZM5F68TThE9GokCB4GvV-6QevJQNcsov0sTqRaL1ZvBscHGQCC3yTq09E8PYiOliPguclQHKwTgGJuS6ILzUHvF_zz_X9Cf6Psn4YtKfFzJB9Nw_h_BUzQ-hD1ux9f1rHb7kZ6BXYvxiDEl98XNFxf99d-c47gXt3kLngG0Stn1KWlmFNjY1ZMRmWn3LVuW7KSv0uaGv3Gl-TJf_sBfBx_xxYPn0mdSwEL3ub1qmxcRTZIvZuVoIyge84da4714a18kzipTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olBt9z5qwgCMyUeKeFRB-L9gDgpXJZota-pELrobQxHsopiUjF2oMxnprj2dbyu3nXlXVGAMMIhePkTEjO9QQVeCB3V9gRrDrFtenYgr2XFX4RzxpqcxLasgmIL8UemHyT27dT6W_CDIV27gro__-10R-5jgNVlRWHfxGWk_Kzql1zZwzDuD3zSQ7WdERMqXA_YqltTSEBHVcfzuBxiN1Qhy_xbPq6LIv3JNxG0hybN3y6EbsCWqLVKxlyqVZKIMdKLBVy2ASA7vHIMjQH18ulTEsAGHC0sg8t8lHCK1mK5Zz1Kwb7ghutwQEwy30ND2YiLPYidGvmmZUYzwtzzr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GuCJWLkL7E98YwfMTFtNaO5-VcQA2l-8jt-LCp_tzMEu37Stzq_8dfrYgTE8E2NYi93PYBzTxOvJS6nSlxrvG2fvZQDL0ylzhQ2HDI6t-aLQo8mD1_KNvThE9lCYiD5tLOyyLhNSCiuM_jz0TDfvfOUYUFgA0kH64eGSqWE78wx-ebgOqpxevl_QwOIzTyuWx5hXMxlxsvGQ5i0LoyZ52VX-1H5s-P0zjivj4oVRxoocrmvItSvsJZ_UDYyN9AOeJNjIfiPxFKAA1JcFM3JzCkrZKdhL8TJX-A5A835M6CscDW3Ozhs9ZNkWW_5UgCSRLZ1TBdqNJiyEdkJxkpXtzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVv1QH3QnUHjhzuVKwDA9MSggTUmSuP7mBcl92oy2YaAwXWtVw5lgueG4OdA4Y8KJGufFPpEZkTrKRj2E6MNzsm-sDWFG12hbC6oUDW4ktEx-lAxNjpXEg2sgr7uXesD03swccS3q_FM3QNyduEpK-gUJylO9-EpgzqBZpVAk-t1zsIQD4c6XDlqKobsLOjgtkS56vQYi41ZK8lyoL1Rf9SVN7BR528Pp8kLgjqJNW7byHN59C13DB1pctCYUyDqfHol-ovlT9p8OGXajoV1lWrv_XEM3Lv6YBk_XWmqp0_yPC19GlASTrurj6lMyAsqEwSK6LU2VoWtCkni5SqlBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🎁
فهرست اعتبارهای رایگان هوش مصنوعی در یک سایت
‏این سایت پیشنهادهای رایگان، دوره‌های آزمایشی و جایگزین‌های مجانی ابزارهای هوش مصنوعی رو یه‌جا جمع کرده.
‏
🪙
اعتبار رایگان، دورهٔ آزمایشی و تخفیف دانشجویی سرویس‌ها
‏
🆚
جایگزین‌های رایگان و متن‌باز برای ابزارهای پولی
‏
⏳
مقایسهٔ سقف استفادهٔ پلن‌های رایگان
‏
🔍
مثلاً دورهٔ آزمایشی ۳۰ روزهٔ GitLab Duo که مدل‌هایی مثل Opus 5.5 و GPT-6 Astra رو داره
‏خود سایت مدل رایگان نمیده و فقط پیشنهادهای بقیهٔ سرویس‌ها رو فهرست می‌کنه. بیشترشون سقف مصرف، زمان محدود یا شرط ثبت‌نام دارن. به گفتهٔ خود سایت هم این شرایط ممکنه عوض بشه. پس قبل از ثبت‌نام، شرایط رو توی سایت اصلی هر سرویس چک کن.
‏
📌
سایت nopaywall
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy4qVuhC5RREQzxXSqJesmgSglBWKesbG1R4HUE0ypdiBYH_JEfLT3kHCcHFBDWoke_wQ5YD3a-4Yw71V3jUz9jC4-g8a8ycRW-nB8WounQWE6xcscYdndASVJjzXtPfMWkTJCGFsGhBpYfHvICNgFhmv8jW5zZW-Ss9kY--LmFBAYe8gCRbnRE2WfwDErjmmViLuDYtRe3LlUmyf4MkgobOV8qrRbm17ogIQ9BBbh9K8o9OfzpCIj_EsiwxHClZji5wthCipqQ_uEuNENeR4egz0WQev9hp_c46SX8SOsVJ6cMu84FSZ7osFqFKq48HeRcUbgX0OdHnoTlTIyj-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚀
تبدیل هر چیزی به PDF فقط در چند ثانیه!
دیگه برای ساخت فایل‌های PDF نیازی به نصب برنامه‌های سنگین و مختلف نداری!
🤩
ربات همه‌کاره ما اینجاست تا هر محتوایی رو که براش می‌‌فرستی، به یک فایل PDF تر و تمیز تبدیل کنه.
✨
این ربات با چی کار می‌کنه؟
📝
اسناد و متن‌ها: فایل‌های ورد (.docx)، اکسل (.csv)، مارک‌داون (.md)، متن (.txt) و حتی فایل‌های کدنویسی.
⚡️
عکس‌ها: یه عکس تکی بفرست یا یه آلبوم کامل؛ ربات همه رو توی یک PDF مرتب بهت تحویل میده!
🗂
فایل‌های فشرده (ZIP/RAR): آرشیو رو بفرست، ربات خودش بازش می‌کنه و محتویاتش رو توی یک PDF برات ادغام می‌کنه.
🌐
صفحات وب: لینک سایت یا مقاله رو بفرست، نسخه PDF اون صفحه رو تحویل بگیر!
👇
همین الان وارد ربات شو و رایگان تستش کن:
🤖
@Everythingtopdf_bbot
━━━━━━━━━━━━━━━━━━━━━
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/omBZ_etDCzInMc6Sahfm3rIIPRTztp9Zs2AGSBYt8U0aOW5YPKf6gj6g0kf5WFEShvIn2X79hEuoFfSB6EiY8KF0KqFwk8DCoT0hdszoxqY1fOZwmNfuOY5zx4e9dcy_MPPa3VIdWr1d5_ovFiUjqhjfOf1X6nTNOeZQcyHp5jt4p-apUDe2Zsi2MKaq3r3bimY7YA9jWC10GrbTlcvONQmRzRchqYL-R3D863syaFqkjZluWmQiegnJi-hkPcjfP6UU0Gxp6oBA28UrFzUwVk2PQvCMG5jWUpNOgkY_tD4C7n4uaupCtMa473pGS4eHhDfoAzXY2Xa79Iem_Nr2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
کلون متن‌باز فتوشاپ با Rust منتشر شد
⠀
‏استارتاپ ArtCraft نسخهٔ متن‌باز فتوشاپ رو با Rust منتشر کرد و ۶ ابزار دیگهٔ جایگزین Adobe رو هم وعده داده.
‏اسمش PhotoCraftـه و روی گیت‌هاب با لایسنس MIT منتشر شده؛ حدود ۱۸۰۰ ستاره گرفته و همین امروز نسخهٔ ۰.۲.۰ اون اومده. با Rust نوشته شده و از شتاب GPU استفاده می‌کنه. البته هنوز نسخهٔ اولیه‌ست و نباید انتظار پایداری کامل داشت.
‏نکتهٔ مهم: چند کانال نوشتن «هر ۷ ابزار منتشر شده»، ولی طبق سایت رسمی ArtCraft بقیه — VectorCraft، FilmCraft، LightCraft، PrintCraft، EffectCraft و DesignCraft — فعلاً فقط «به‌زودی» هستن و نسخه‌ای ندارن. پس فعلاً فقط PhotoCraft واقعیه و بقیه وعده‌ست.
⠀
‏
📌
ریپوی PhotoCraft در گیت‌هاب
‏
🌐
سایت رسمی ArtCraft
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dAOC_3yIxkEavT2NswwWND34_Vo6bmOqvP7jTsawBnsKkraLC-e2e3CUBJaQBMpQLlyJA9PYN5pQXk1eBfY9tmYmWJCC03_SmWmnbNZu_CSxaaJJvMA8u_p6Z5-zkUBQitY6AhXMg_ec8S-Yh04MGf-4N2lUdx6iQk9ykk1WqXOAcQbLhAbI9AGqkaVoGXuOsRxEw4i2PD0n6ZHVp6lBtDm-Hmx5zrvVe0jk1Lb1umGxqGl3Gl_B1MqF6hSllsKSw2RxD2MhkPsIBUsL_LtITmR0d7WThNIv_hLMVZ1MsMMQFV1penfcwHiizO78UG1wEAuZRT6QNDLU-iPs91Pw2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚔️
هوش مصنوعی بدون دیدن صفحه وارکرفت بازی کرد
‏⠀
‏مدل GPT-6 Astra بدون دیدن تصویر بازی، در چهل دقیقه منطقهٔ شروع وارکرفت را تمام کرد.
‏⠀
‏به‌جای تصویر، بسته‌های شبکهٔ بازی را می‌خواند
‏خودش ابزار ساخت، مسیر پیدا کرد و استراتژی چید
‏از یک باگ نقشه هم بدون اینکه بداند استفاده کرد
‏⠀
‏این کار با فریمورک متن‌باز agent-wow انجام شده که هیچ منطق بازی به مدل نمی‌دهد؛ مدل خودش سیستم ادراک ساخت، اطلاعات مرحله‌ها را از دیتابیس بازی درآورد و با برنامه‌ای که خودش به زبان C++ نوشت مسیرها را حساب کرد.
‏⠀
‏به گفتهٔ گزارش cnBeta، کل این فرایند فقط با یک پرامپت Codex شروع شد و سازنده می‌خواهد بعداً ببیند یک ایجنت می‌تواند به‌تنهایی تا لول هشتاد برود یا نه.
‏
‏
📌
گزارش کامل cnBeta
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FpvaA-A16qgDh6rlhbZZgn7x2r_CgRK7K6elWqptztwK0KokV3o65XQtOEl4AIOh-KhMB30kVbebV35sfZBGmb9VY7M1SE0qmmfwlE1R8p4PZqKuapY0ji_S9IkIklxzazSxHozqz_KevmSaEy9TbWagndQ3S9SNoT4iLZcPOopjAzSnZFVOZVRMcVOw-YDwNQKb9Ujni20hEnTZabGzdUD7bTg64uR6tMZ91pVXsOSUDtMUGR908Lw--AGFcl5FpdR-M1dnzNPuEtaJfnjT275tCqpt0cNVuXkWRSct4YaFhM4r66vYZ2NU_Mh-WsP4Nes2nuMIwDQuVdw7w-0ILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔍
اسکنر امنیتی هوشمند و رایگان برای دولوپرها
‏یه ابزار امنیتی مبتنی بر هوش مصنوعی اومده که بدون نصب ایجنت، آسیب‌پذیری‌ها رو پیدا می‌کنه و جایگزین ارزون تست‌های نفوذ گرونه.
‏⠀
‏•اسکن آسیب‌پذیری بدون نیاز به نصب ایجنت
‏• تحلیل و اولویت‌بندی یافته‌ها با هوش مصنوعی
‏• کد اصلی پروژه متن‌بازه
‏⠀
‏سازنده‌ش می‌گه چون هزینهٔ پنتست حرفه‌ای رو نداشته، خودش این ابزار رو ساخته.
‏برای دولوپرها و تیم‌های کوچیکی که بودجهٔ ابزارهای انترپرایزی رو ندارن ولی امنیت رو جدی می‌گیرن، شروع خوبیه.
‏⠀
‏
📌
ریپوی گیت‌هاب
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده: ⁮⁮ ⁮⁮
🆔
آیدی عددی برنده: 2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل: @ArchiveTell…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel | BOT</strong></div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده:
⁮⁮ ⁮⁮
🆔
آیدی عددی برنده:
2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل:
@ArchiveTell
🆔
آیدی چنل:
-1003718102196
🎊
تبریک به برنده!
🎊</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00  قرعه کشی انجام میشه و شماره مجازی تلگرام به…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EadzkoPSZBmiGBkQpTL2nQLO3hh1d0VKTQg2llCpzCwiylcUUCm3alxH6oqXjzSFPgrhpCRmX8sTIytgpiUzn1f9hzSAtEefuxAQIwmfGqBnkAR_xDQZSlw5VETwuuwbs-gJKr7PT_RgeglzuCPtQLCzkVoXLZS70HnRkZJUpSHoUbQJnmJ9GOxiZ_US6E5BZN9jHunwXCXiuN6o4hYhfsyoJNh7mTtCui7DYzYyrw-rHv69FN2OShogkTc5GooWady6qWc4I-oYNJCnzPP9pj0ChUsBWrpAApm3EYoFU7WurPKkQqmophGxO7sle6TzfPWxtP7-YX89fky8LKum1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZxZ34skkjCHa0rRt1eIeKFJ5Vt6fxsHdve2UJ4Yq9QiTEcp7We2Xecxh8W59DbjAbd3FdIXdQ4v9hvZQRE1nb17A8eSwRezR8uyyRb_Z3lB_BX9cEEkvnippUzgVuGXMTZcu3W7AGWqtQ_1AktH5soRRgEeYqYRZnhutAeFnfE0AUj8bju9pJZYIHG9d_oPriRt5BGK5kb93OthM55ZAyrI4h8FT_GrLeb9sarG-a4ruLns4JCcdX4G3LE59z1vv28pe0LAFABc8VqdUMBepY7nrFgEcvPp2FnpFG5xuFRlvrEl-OaPABCT3HV7cvGh4XztQyv0qDS37idy8NII0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📥
دانلود راحت ویدیو با Yoinks از شبکه‌های اجتماعی
⠀
‏این ابزار متن‌باز به شما اجازه می‌ده ویدیوها رو بدون تبلیغات اضافه و مستقیم از آدرس صفحه دانلود کنید.
⠀
‏
🎬
کافیه آدرس صفحه رو از یوتیوب، اینستاگرام، تیک‌تاک یا شبکه ایکس بهش بدید تا فایل اصلی بدون معطلی روی سیستمتون ذخیره بشه.
⠀
‏
✅
چون اجرای برنامه داخل ترمینال انجام می‌شه، فایل‌ها به سرور شخص ثالث نمی‌رن و خبری از تبلیغات آزاردهنده، پاپ‌آپ و تغییر مسیرهای مشکوک نیست. به گفتهٔ سازنده، بیش از ۱٬۸۰۰ وب‌سایت مختلف هم پشتیبانی می‌شن.
⠀
‏
📌
مخزن گیت‌هاب پروژه Yoinks
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnY43QpMH6yyPunvhw1-SjhobdWzQ-YabJYgaZyK4pBfq1n--Xy4x7yTLzP1kUrVPl-yzi_ZkZ5_syAvaXZnHFsofybNMDbdgNnqEpEmBPKpKpbyY43wjPDQ8TXdLieNKq-WqDe47lzZD7BvGboe8bMPaacrwlKY93mfDfygPdR-5ZxbqX278x4bQMgSdrpfCyb2F7QoQfUd5jsJNSyDt_8pXPCzQnjqGlUEQMHMg9OgOHY9eQtNcGX3JWelOk-bVKvzr9qb7Fx8ii8IACIlcIoM7azNXEQ0pX3atSywvGOXrmCU6_NN1ohilMU9pCiCnCcwXZ8tGgf9VaNIjrSs_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
ترفند فعال‌سازی Opus 5.5 روی Gemini Pro (آفر Jio)
🔥
اگه اکانت جیمینای پرو رو با طرح Jio فعال کردی ولی هنوز مدل‌های Opus 5.5 و Sonnet 5.5 توی antigravity برات باز نشده، اینو انجام بده تا بیاد:
💎
اول یه اکانت جدید رو به عنوان عضو خانواده (فمیلی) اد کن.
(دقت کن Sharing رو اکانت اصلی فعال باشه، و ریجن هر دو اکانت یکی باشه)
برای تغییر ریجن این پست رو انجام بدین
😱
بعد با همون اکانت جدیده لاگین شو.
تست کنید ببینید براتون فعال شد یا نه؛ تو کامنتا بگید
💀
👇
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJjpnVy6C-pPj6c_urRbOkv_02OBIMIThcg8T8dTU8CH-zOYFF6_X8ah7CWggMwthKak8ZcJETVs3gpl_qUlLdXtD_4tHLXQXPTW_ah34g_wBIqz0Vcl_9-uWffD02GZ8wnCUi_AVsiF6P-elykOEmXHLQ-5xWMzJBv3-vCKa7O6Yh0JZZHGdJ528FEt-rWcJmUvE85dw3JIiiBQXEYmw0iWakHb40ecJMJfh9vK2dmOLMaxHXQiDp6mpaRL9Dy2xvYdkeIteV0JSfzYEZKOsfj8ZXOFxfvkMoXfmowirt29ddZhw_u79lBZP4WcKmXMDgSA1KKS0c1AwBfVPvkT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rjTOPCQk6NVk1AZOICmIi7T-IGnXZBSO13ZWFI2ezPnl8WRTVVZnlOq523PzVLFDMkVj9BYg13N9iz2-vlCREBbPp8ZclucLsWh36RtwRJc6aOx89BpXJHkA0IzQ9jirWvV4XmrMOgXk6sN8QCfXzmQT_yCmPru6QKVa7JMjI01eg318f8YMna_t84eqnaN1rMYwnSyYntg4AUwagVwiM2O1TRdKbCYKxffWOy_LzFE4FgnwVjM7KymtWXwjZYSY8izjeCRQRWfK8tmohf9N-ZKd_3I2DNLhVd5nK75kn7qrvgmxnSPL8qSErxRPXGWyZ6Ya1_EMzBM-oHfj8laZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
☁️
اکانت تلگرامت رو تبدیل به فضای ابری کن
⠀
‏یه اپ دسکتاپ که تلگرام رو به یه فضای ذخیره‌سازی تمیز و منظم تبدیل می‌کنه.
⠀
‏• مدیریت فایل‌ها داخل Saved Messages و کانال‌ها به شکل پوشه
‏• پیش‌نمایش، پخش ویدیو، همگام‌سازی پوشه، WebDAV و REST API
‏• ویندوز، مک، لینوکس و اندروید؛ همهٔ قابلیت‌ها رایگان
⠀
‏برنامه اوپن‌سورسه و مستقیم به تلگرام وصل می‌شه، بدون سرور واسط. ولی دو نکته: برای ورود به api_id و api_hash از
my.telegram.org
نیاز داری، و فایل‌ها تابع محدودیت‌های خود تلگرام‌ان — پس «نامحدود واقعی» نیست. نسخهٔ ۵ دلاری فقط تبلیغات رو حذف می‌کنه.
⠀
نکتهٔ امنیتی: اطلاعات ورود تلگرامت رو فقط توی نسخهٔ رسمی از صفحهٔ ریلیز گیت‌هاب وارد کن.
⠀
‏تو تلگرام رو بیشتر برای فایل استفاده می‌کنی یا چت؟
👇
⠀
‏
📌
مخزن گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLtRP7mVtxO4WrNrwm16Ckv7SgMMdgq4JNITsSWDsXJuxKfNPyXDw6D3RUgOeHwfE_n2EI1u5kgFWAjmdAzVmIGkzlgk_uRsYHltqxxBVlFhe0upDhNerwOXPAdCrkVPDSzzlrPvbZSCdzY-3xel77l0EF4uTx6xpACrSqe8gyJTccWmEllX9kKwo1__RbqO5Z7xqsJjK0EzC4oWmn-F1L4babBlCQns-xBo4l234wuLN7fPLUHQWZr1c0Etd9qUfMhZlTKwhQDj8Csv59ZyvlgcvPUQvyYlonPAJkBq26lQXF_YxaWKqfc-3COxYW0nLlSo1K_8Llyf81BGPbbklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش
‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.
‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری
‏
💸
کم کردن هزینه با prompt caching و compaction‏؛ به گفتهٔ اوپن‌ای‌آی ورودی کش‌شده تا ۹۵٪ ارزون‌تره
‏
✍️
پرامپت: هدف، مخاطب، محدودیت‌ها و معیار تموم شدن کار رو روشن بگو
‏
⏳
کارهای چندساعته: عوض کردن دستور وسط کار و سپردن بخش‌هایی از کار به agentهای فرعی
‏تمرکز راهنما بیشتر روی API و Codex هست و برای کسایی که با این مدل‌ها ابزار می‌سازن مفیدتره. قابلیت multi-agent هم فعلاً آزمایشیه.
‏
📌
راهنمای رسمی اوپن‌ای‌آی
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHHlh5fNl5Y9hkvxmEDK_YErAkmu8V8EPKFbUQCN3KfRJBnZvaeG1mmb7JB3UDKOnEzYiPgPTSQ7GcQ6_nkZaqqcDm0qxxiinmFXsUgVfxvPJOWDafjQ7wmZToqD9YxaITdTNQCEiVgOs7rBBVXaNLl8Zf4B618tFcgwaqKx7OnZ8H1_OQr85N0cLrqj04ND9spkwtfkvIkRbe-50v0z-HRjocmPbrRd6jpqnv66GD7CYDrj0zq5kFUBoeNpTkkauaBp_jWwt2Xh0DoPnYlQTVDEhs3mCPZByJEKYGk-1Ob3xSQ19HQJeB_VlXKQyHPtEfLi3BWVvrdlpAr5uG9mKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚫
انتشار Grok 4.7 در اپ‌های گروک
⠀
‏مدل جدید گروک حالا توی اپ وب و موبایل هم در دسترسه و مدل پایهٔ همهٔ حالت‌ها شده
✅
⠀
‏به گفتهٔ xAI، نسخهٔ ۴.۷ روی یه مدل پایهٔ بزرگ‌تر ساخته شده و با یادگیری تقویتی طولانی‌تر، توی کارهای کدنویسی چندساعته و خود-بازبینی بهتر عمل می‌کنه. پنجرهٔ کانتکست ۵۰۰ هزار توکنه و قیمت API مثل نسخهٔ قبل مونده: ۲ دلار ورودی و ۶ دلار خروجی به‌ازای هر میلیون توکن.
⠀
‏
📌
یادداشت‌های انتشار xAI
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdOytXxTSNxqXU7OALRVflIheFY_GcUDlkVRQJeMCOlbArS1Cn1Y1rGPsr1SEjhuepSS2p9moG6tZ5Nz6HBrv3saGqiYDFRPwSnhckeK-ol0uuNtCP8JVef0C2ZOf-kOZaIPSCEbad4MPUP0asMLXjmS_0xB8n7Ac32ArN1CIpLnB9cZjIMF-zwEX0WusPIKgE2pfGex2ewnexU3n9PN4migAce6Q8YTDIH2JWcLsknJVZVVFoEks6PUflQhA6SzphIfD0mhREbmvjUdGoko-Mar-c7W6_27kSn0U6GoQY-ZOgbZ-uE84pzDkWh4K7hUoEBQxeJtykO7Fgp2Dviu1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان و ممبرهای عزیز آرشیوتل،
😍
ممنون که تا امروز با حمایت‌ها و کامنت‌های قشنگتون سرپا نگهمون داشتین. سعی کردیم به قول نیچه «با خون بنویسیم». راه سختی بود، ولی به لطف شما هنوز زنده‌ایم.
ممنون از ادمین‌ها و کانال‌هایی که با فوروارد و تبادل منصفانه حمایتمون کردن، مخصوصاً تیرکس نت. دمِ توسعه‌دهنده‌ها و همه‌ی کسایی هم گرم که تو روزهای قطعی، اینترنت رو زنده نگه داشتن.
تیم خفنمون هم که جای خودش رو داره:
احمد، که داره به مو می‌رسه ولی آفتاب شکوهش کانال رو نورانی کرده.
وگاس، که تو روزهای قهقرای من پشت کانال رو داشت.
«اس»، که با اینکه گوگل‌فنه
😁
یه متخصص واقعیه.
محمدجواد، معین، ایلیا و همه‌ی کسایی که سهمی داشتن.
خیلی‌هاتون دیگه دوستای نزدیکم شدین. امیدوارم سایه‌تون بالای سرمون بمونه و مثل همیشه با لایک و شیر پست‌ها همراهمون باشین، تا روزبه‌روز قوی‌تر ادامه بدیم
❤️</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtLz8wI3K0BZ75IjvT1jvHOFOnQ_jvp6nB5R-aJLW8YrYigQqzd9bAcGfNAHuOwt1zAEgNbhPic6iLob_DvsdYVSjyCVNABxlnYfNZspTF68wD8YbbtdKmkG6bknSCLhEpFu2GZ5XkSIsQ6chWuoyyFCAapcKBFvlANAZ5gLTX_dzMQD3BS18bNb_DyREhJngSBBgp-gV0F7sHU_yfDVnb57h-TOFt_hmvP_g-ilpyBirDuiCgGCSIn5eafT4opbfzeItw0qktxADOvcYZZp8NdYdaC_7ZBDNK_HpPw8-zPr2u6tE9OoWB1otiJcgMXnMgRg98_cpAsKZ_qbnXFALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کاربران رایگان جمینای فقط فلش‌لایت می‌گیرند
⠀
‏از ۹ اکتبر به بعد، کاربرهای رایگان جمینای فقط به مدل فلش‌لایت دسترسی دارن.
⠀
‏
🤖
کاربران رایگان: مدل‌های فلش و پرو حذف می‌شن
‏
🤖
مشترکان AI Plus: فقط فلش‌لایت و فلش می‌مونه، پرو می‌ره
‏
🤖
مشترکان پرو و اولترا هر سه مدل و قابلیت Deep Think را دارند
⠀
‏به گفتهٔ cnBeta، گوگل سیاست دسترسی حساب‌های شخصی جمینای رو چند روز بعد از معرفی مدل پرچم‌دار Gemini 4 Argon تغییر داده. خودِ Argon هم فعلاً فقط در اختیار سازمان‌های امنیتی و شرکای گوگله و به کاربر عادی نرسیده.
‏گوگل گفته زمان دقیق اجرا برای مشترکان پلاس رو با ایمیل اطلاع می‌ده.
‏این تغییر در مرکز راهنمای اپلیکیشن Gemini اعلام شده و کاربران AI Plus زمان دقیق اجرا را با ایمیل دریافت می‌کنند. سهمیهٔ مصرف از ماه مهٔ امسال بر اساس محاسبهٔ هر ۵ ساعت یک‌بار تازه‌سازی می‌شود و سقف هفتگی دارد.
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qv__SYVdu12D0-SL5MIlGQZ5CABAcI-r1RdttBLLu8rzvwEnioLPI5U7cLFNVczIR-HVOo3I6RyuVNQI7vlFdb8q-_pkMugK1CnJWvO0YWyLtuv8iX32_vT3-fjmexwkUfC7D_FskjNozYv8VM0JJONwzS6_8HjII5Kh5hJ-q8p8JST7dhmQOfCnTXXT7kQHR7OwD8hdLYGBSvvp3C0vmjRz_EcbBMVAHw_xOrMdEOwCzX7sSYQhAVc5NWXvUpoNmKpKwKvvJK4KZ9cd3LLpvCUnF9uyLbd6_qp7GTJvUQllb-dXcJUS-GSjd8blDaHNDJLtjOinJOxmBMA7ouTSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🟠
مدل‌های Claude 5.5 به Antigravity گوگل آمدند
⠀
‏در محیط کدنویسی هوش‌مصنوعی Antigravity حالا می‌شود از Opus 5.5 و Sonnet 5.5 استفاده کرد.
⠀
‏به گزارش سایت appinn، دو مدل «Opus 5.5 Medium» و «Sonnet 5.5 Medium» به فهرست مدل‌های Antigravity اضافه شده‌اند. Opus 5.5 برای کارهای پیچیده و طولانی طراحی شده و Sonnet 5.5 برای کارهای روزمره و کدنویسی است؛ Sonnet 5.5 نسبت به Sonnet 5 بیش از ۳۰٪ سریع‌تر است.
‏نکته: برای استفاده از Antigravity باید با حساب گوگل وارد شوید.
⠀
‏شما Antigravity را امتحان کرده‌اید؟ این مدل‌ها را تست می‌کنید؟
👇
⠀
‏
📌
گزارش اضافه شدن مدل‌ها
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L9ynQoQqN5YqDEjI1e0zOvzhDuh7lDojaWmni_YnNHokuWAyl72V_AclUkjicuCa0NnJ2siIp63x8Fwy-FbGVdIKuwWqzedhkjy5R5hTv82W0cH_bUd8pe4rYt3UVu_E2dkHFN5kXRTv8jRDiVIIlQmiWsszg0XRTLQDZIaFnj09WHKCU08bReuYGXcSmrzFHB3gHJgbhq2og-T8IWt6EI29-9564t6Tq_8uGn76KaQjeDv5Q5rmU5wutsTmrKXCLuG-8qMSomkqPlAXsdCKFad5FRthj3UadzL8WOrTNrMXabMkut_Pr_BUmWkARM0xx7cK5szjvGMl5QXL5v1Tbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
مدل GPT-6.1 Sol اوپن‌ای‌آی رکورد زد
⠀
‏سم آلتمن می‌گوید ۶.۱ Sol سریع‌ترین رشد تاریخ مدل‌های اوپن‌ای‌آی را داشته و مشکل کندی‌اش هم حل شده.
⠀
‏رونمایی در DevDay؛ هوشمندی نزدیک به آسترا با یک‌پنجم قیمت
‏کانتکست حدود ۱.۰۵ میلیون توکن و خروجی حداکثر ۱۲۸ هزار توکن
‏ابزارهای جست‌وجوی وب، جست‌وجوی فایل و استفاده از کامپیوتر
⠀
‏به گفتهٔ آلتمن، این مدل در ساعات شلوغی کند می‌شد ولی حالا «باید خیلی بهتر شده باشد». قیمت‌گذاری‌اش هم برای توسعه‌دهنده‌های ایجنت جذاب است: ورودی هر میلیون توکن ۲ دلار و ورودی کش‌شده فقط ۰.۱۰ دلار.
⠀
‏نسخهٔ Ultrafast هم در راه است که تا ۸ برابر سریع‌تر جواب می‌دهد، البته با قیمت بالاتر. نکتهٔ جالب: قرار بود نسخهٔ ۶.۱ آسترا هم بیاید ولی به خاطر نگرانی‌های ایمنی فعلاً متوقف شده.
⠀⠀
‏
📌
گزارش عرضه در DevDay
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iJb-rkS6WP3CiUqQJVKh9o9BsOT2yE7bGtLZp23w0RS1KSsgZr_IxnRsoeVqd3k_5VA_f0KLcG1DPucIQblIlpZ6a2TdEos1Uq0LmLzJ_6YN0leLzLZnfAQWoo8DkA5mM4VZyFGEKfh3nUBMmpQ8KmGkMUvfqMIa9SFvxmdo0nW_7l7FWr-qIlP1KVRAEuo-JR1TBGQ0nYjDJ9yoHghJkTBXVAr8cLVgKaaNZWJfSgYgk_ASle7AK_-fZMeZUZfuDHvOvOX4zVkvt1xG2ixZR9MP4hqji7zwYxrC2EWa_SRwxeOUe8PJ9cWpVFrBZbxai3pxV5dQX5xUh1ZBafTWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔢
مدل Muse Spark در حل مسائل باز ریاضی
⠀
‏متا می‌گه ریاضی‌دان‌ها با کمک مدلش شش مسئلهٔ حل‌نشده رو پیش بردن.
⠀
‏• شش مقاله در حوزه‌های احتمال، معادلهٔ موج، نظریهٔ گروه‌ها و جبر
‏• مثلاً رد یک فرضیهٔ ۲۰۲۴ با ساختن گروهی ۳۸۴ عضوی
‏• و اثبات فروریزش در زمان متناهی برای جواب‌های معادلهٔ شرودینگر
⠀
‏نکتهٔ جالب اینه که توی هر مقاله مشخص شده کدوم بخش رو انسان نوشته و کدوم رو هوش مصنوعی. البته خود متا هم پذیرفته که بعضی از همین مسئله‌ها رو گروه‌های دیگه به‌طور مستقل حل کردن؛ پس این «کشف انحصاری هوش مصنوعی» نیست، بیشتر یه نمونهٔ جدی از همکاری انسان و مدله.
⠀
‏فکر می‌کنی هوش مصنوعی کی اولین قضیهٔ مهم رو تنهایی ثابت می‌کنه؟
👇
⠀
‏
📌
گزارش RuntimeWire
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFQFL9_1Q6E3rZfbgA2pJKB1f7S2URJAvXhMxpli8_-IlJ4eAOWIIQN-vT8ErFjcbDq38P8_HwDKoc5k4XesilZkrEOEAclf3hkjL3ZEoUewbD2Z9Y3OKNFoSybjv8vAKXNgHod8Hj80rHvm1lQVo7R_10RnxgTHiOczQYnlkn93RpWMSh4TGbJdAVHCMxzA96PSf0rnLaMUhoOIlJin7mLzO36SDuPLm-SPhfb9HrspNU8ZgPouGbWspuhbw-nfJvpf7VlijDSzHyrDCGH5uR9v5C82CvRyE_MaooicvvOGPiJP7dLG9-bShdjQf37eRV7ROdg_1VVVR9hW5_38Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">📨
ایمیل موقت جیمیل و اوت‌لوک رو با temp.tf بگیر
⠀
‏یه آدرس جیمیل، اوت‌لوک یا هات‌میل برای ثبت‌نام‌های یک‌باره می‌گیری و کد تأیید رو همون‌جا توی سایت می‌خونی.
⠀
‏
✅
نه ثبت‌نام می‌خواد نه رمز؛ آدرس رو کپی می‌کنی و تمام
‏
📎
پیوست هم می‌رسه؛ عکس همون‌جا باز می‌شه و بقیهٔ فایل‌ها دانلود می‌شن
‏
🧩
یه API رایگان هم داره، بدون نیاز به کلید و با سقف ۶۰ درخواست در دقیقه
‏
این آدرس‌ها با plus alias و نقطه‌گذاری جیمیل از حساب‌های خود
temp.tf
ساخته می‌شن؛ یعنی ایمیل‌هات مستقیم می‌ره توی حساب اون‌ها و چون رمزی در کار نیست، هر کی آدرس رو داشته باشه می‌تونه ایمیل‌هاش رو بخونه.
⠀
‏
📌
سایت ایمیل موقت
‏
🌐
راهنمای برنامه‌نویس‌ها
‏
🟢
سیاست حریم خصوصی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utivilBvt88MBcf7VfB4YLvRIAonD-uaM960Z8JBUxKIyCptF4EhCLIuCxysCFCGA5E9l8t8CfW-3ycRW-Yi90cd8QnjUCxVz2QsCm-MZQVc5e3GCW66EUBSXbPHrSBHnGcbVjD2JFVvDLbJ4zdlaqWqLMWo-5SOoUvDtv97bttM4ixVN_783s67Rgrh3pYDm46lImVUFtQ7rTSJWoq-JC6fkbN9yHhUxvW98iYorzn9q5tghxOZjok3uBbVayqJqm1f-wsyLi8Xys_nZqdqkWhuE9Sf-PexCiCvCxYYw6jvutGEMV2g-p3IFgqIpuqljIGiHzayDswIQF6ypz34iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های قدرتمند هوش مصنوعی
💥
🆓
GPT 6 Astra | Opus 5.5 | GPT 6.1 Sol | Sonnet 5.5 | Gemini 3.8
✅
با این سایت میتونید 7 روز مهلت برای تست مدل های بالا رو در پلن Max دریافت کنید
🎉
🎁
⭐️
قابلیت ها :
🤖
چت با هوش مصنوعی
⚡️
تبدیل لحظه‌ای صدا به متن
📢
تشخیص و تفکیک گوینده‌ها
📖
پشتیبانی از ۱۴۰+ زبان
🗣
تبدیل فایل صوتی و ویدئویی به متن
📞
تبدیل تماس تلفنی به متن
📝
تبدیل جلسات Zoom، Google Meet و Teams به متن
⏲
ثبت دقیق زمان هر بخش از مکالمه
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saim19WkbvOED1nwjWEsAd9IUY4wAC72a4Y6KBupGSrTxtB5EquBNFJZG7TbOVdbYPP_FQTNUBg_GF-2BCgll-UQQj8iyjHZS1vLPCzfwukgK4HLHd8Xgjyinv7zlcNVlA3WqgfX6T8inheqcMftBxz_59ghdssx51QDqVqsuLMAHK7S3N-UgX-5F74OMQUu_aF7f7VoSRoHxAgJ6bfOidSbY2fDKk4sDkktvQtLDwoLJ0JV-xzH-V6_Jhrw9ELCl1cY2g6xjRim71PxfwVFSUWAqTmpULz-sTc4TAixHML1K3tBoIrTxtG1Of_sAL6_4BmiJONU9vPI-qzOyqRoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQJZnIN8alceWglSzYS7pkqpeUXfBGcFnbsMKujuOZh6MiljNitZgDn7j_DyZDNa_zvX2WceeDl-HR0L_4S1FZbkXPIFYVM2hopFotoMG8iVsDRfb5WGy-ieUSQuEXNyrxMKn711ohpJtX8xFEgWBXxTzxvvaAFdXWy2joSBVKzd0qalMsekh8DcTZmKWOIoCAPw2dlIm_3u8bpGHt0ZVuY78fYWnDlO1JCd0iMJ9XeGud_p1BnJExrTqjnXOtm5GD1S05KIE2LBOGayeFbEnunwZXP5LnfVJSmLEXNxjNYI9TF7gOpzk8kIiteOILEE-QhKkkY6JnHCZytfhpaYKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⏰
سهمیهٔ ChatGPT امشب ریست می‌شه
‏به گفتهٔ مدیر OpenAI، ساعت ۲۰:۳۰ امشب به وقت تهران سهمیهٔ همهٔ اکانت‌های پولی ChatGPT ریست می‌شه.
‏
‏این ریست ساعت ۱۰ صبح به وقت غرب آمریکاست که می‌شه ۱ بامداد فردا به وقت پکن. Tibo همچنین گفته مدل GPT-6.1 Sol اوایل عرضه به‌خاطر بار زیاد کند شده بود و الان سرعتش به حالت عادی برگشته.
‏
‏
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUQnF-uW06b3zsbijIqRVayXtIt7OoUCMLy9l9V_UsYuZvUXzy0ObjY-L5Tkstihj27o181z3fXfVmeCAG2teuRdlRCvQsrJAt2ta334P89Whv4O5eJmhrmF51EDQhfV-8O-WZ_ym87DVHFqu_VqeSqYF56We4nVOxnLnrazTG9F3WiCqUOR_EObISGFR_dUutUEt7km2I3xR8NtmJxCNSCO3XBjwMkm1C20_ePAvkeno8uVGKtLgVDz_ATDmGf7U03BQRkA-vX3XJxvoWxHHoyTZmzANtXaJ7BGuusJ43DCa5NpKHa7QJ-PBc9MaJEqpgyJrkrkhhYG9wOogRvM8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
ابزار InkGist برای خلاصهٔ صفحه‌های وب
‏لینک هر صفحهٔ وب رو بهش بدی، تو چند ثانیه نکته‌های اصلی، کاربردها و کارهایی که باید انجام بدی رو تحویل می‌ده.
‏
🤖
مدل‌های Zhipu و DeepSeek و Gemini پشتیبانی می‌شن
‏
📚
خلاصه‌ها تو بوکمارک‌های ابری چندکاربره ذخیره می‌شن
‏
🧩
افزونهٔ مرورگر بوکمارک‌ها رو با یک کلیک وارد می‌کنه
‏
📷
از صفحه‌ها نسخهٔ آفلاین هم ذخیره می‌کنه
‏
🏠
می‌شه روی سرور شخصی نصبش کرد
‏به گفتهٔ سازنده، متن صفحه اول با Defuddle به‌صورت محلی استخراج می‌شه و بعد برای خلاصه به مدل زبانی می‌ره. پس حتی تو نسخهٔ شخصی هم محتوای صفحه برای سرویس مدلی که انتخاب می‌کنی فرستاده می‌شه. نسخهٔ نمایشی آنلاین هم روزی ۱۰ بار خلاصهٔ رایگان می‌ده.
‏
📌
مخزن گیت‌هاب پروژه
‏
🟢
نسخهٔ نمایشی آنلاین
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7SGaNWPeKdJpIXHmz0mzdaFL2fJYNkae_WA44zmQSuOaEekzsWHqjP607nwPKeb8pvWtC11yEkUX-6U_xPS7wkJlbGd2_p3IJoUAAll_LGYlxMkGkroUBKziRA9_m6S9AAKmrYQWJ9xL-rIBe7hhrgVT3-mGEn4ecmrc5_OTCl8DVwGKEfwy1La-M_ADP2xKpgEFng11Jfwh2fAtTHRMY_xEAUoTayNFNV6wzUZodxVQFxb4CIOeL2lhMG-mNuKM5D_mkbQIc3U9KvgLVVCEn_tDa_lJED6QCLcrKz8THgFE6S98HftGzwVRZvF5QW9dGZui-pv7oy2Cx3Q6Hk_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFSLzb-Y7LvMcBUfO9Slu7ODBs1ee5S779qf1f9RUV7nX86e096aAatICKPm2VpY2yq4kPD_n7XbZl_9h-MFoXX_iUSCJcdHDZd_UZq4M9dXIuPognldC8L4empPAZeFPPIRt_wwmw9gAUPIj0NnFaEakmOZAtWNCqIQ40fkUlUx41THjOeXbWQ40xl1zQePLqJ1nZvxe5GIo2Dg-Vy6TWGryjAyZy9EFGtGyPdgmiicbxmuzISTUa3CnGrQolBV3Gat2-vSHoaBoYeP1WR7qCn3E6sUg7J4pEQtgwjzWz1E8YKCERn8W9gSyYNurexnq1kjHgrv9b9ipi5uu4kdmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه
‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.
‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد
‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد
‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه
‏به ادعای Anthropic‏، نسخهٔ Sonnet 5.5 بیش از ۳۰٪ از Sonnet 5 سریع‌تره و هزینهٔ هر کار باهاش تا ۳۰٪ کمتر شده. این عددها رو فقط خود شرکت اعلام کرده.
‏برای Haiku 5.5 هنوز تاریخ دقیق، قیمت و شناسهٔ مدل اعلام نشده. حرفی هم که می‌گه این مدل از Opus بهتره، فعلاً هیچ منبعی نداره.
‏به نظرتون مدل کوچیک بعدی به کارتون میاد؟
👇
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhRMsOOyDuC-ZfiJe2MVMonMeA5F3ugFci9L1G8Kc5EDRJh-gDDD4lEiPybEbPSugMl7CMyxoPNBJiI5Tq6UKIjr1dixQ_H_2F6cyBPP-YFr8Wx9bQqQcZah62Vo7PYXpM1DMGle3m8iLJzzWl36PVDUdMnSsLzAf1-bjODx4LiOdYKx6g3uWna2Q_wwUt0QYvYzdQ9OdcjJVdCzijPfebH_wFlJS_xGPPh2KSCyYREy6AVOz2OXEqC6pIuijPBpE1H_xj-3QyB6pjnI74iQONlQqLou2TVVzLrWegMDzAdpGuE_X2kRSb4D3DvuRAFuSlbg1JtxJNFY_DSK54H5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Claude Sonnet 5.5 روی اوپن‌روتر عرضه شد
⠀
‏به گفتهٔ Requesty، مدل Claude Sonnet 5.5 با قیمت ۲ دلار به‌ازای هر میلیون توکن ورودی روی OpenRouter عرضه شد.
⠀
‏بیش از ۳۰ درصد سریع‌تر از نسخهٔ قبلی
‏هزینه تا ۳۰ درصد کمتر در بیشتر کارها
‏پنجرهٔ کانتکست یک میلیون توکنی
⠀
‏این مدل دومین عضو خانوادهٔ Claude 5.5 است و به گفتهٔ Requesty در کدنویسی و کارهای ایجنتی نتیجهٔ به‌مراتب بهتری می‌دهد؛ قیمت خروجی هم ۱۰ دلار به‌ازای هر میلیون توکن است.
⠀
‏مدل هم‌زمان روی پلتفرم
B.AI
هم در دسترس قرار گرفته است.
⠀
‏
📌
اعلان B.AI در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KI8TpyemXOS5P0DCOuuRv3iX9N61nKjaian83qv9Qst_6b4L4Yy8H7GIPQIS12WnCE4-3kxIKghbMvUOXNOA5Dr34WvJyztY1VbtQgAOZ-8L9eovCEeG9nbN3HA8r2v9BUGKcMpEajKJa17bvM3ONN9Nhztgc8QddY5vB2jS_pAut-TvtqWCemrUH88ZlBgLX-5fPYOh3nD-Rb5aeCCPFgZSD8NljIweC-x_xPdLM4JfO9f-SgtjO6XsPNNq6H6UIuhb_34MlZeDTanJ9WRCHfrpiMKZIE5Pd9X2Bpq3jj_Oh9M8T-Mhe6PqAkM8leJvKk1fEllG0SulO7yQRenOGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
همهٔ دستیارهای کدنویسی توی برنامهٔ ccgui یکجا
‏اگه کار با دستیارهای کدنویسی توی ترمینال برات سخته، این برنامه همه‌شون رو توی یه پنجره میاره.
‏
🧠
موتورها: Claude Code‏، Codex‏، Gemini‏، OpenCode‏، DeepSeek Harness و چندتای دیگه
‏
🫧
یه برنامهٔ دسکتاپ که با Tauri ساخته شده
‏
📦
نسخهٔ مک، ویندوز و لینوکس طبق صفحهٔ دانلود
‏
🔄
آخرین نسخه روی گیت‌هاب: v1.1.0 در 28 سپتامبر 2026
‏کد برنامه روی گیت‌هاب بازه. ولی ccgui فقط یه رابط گرافیکیه و خودش موتور نداره. برای هر موتور معمولاً به حساب یا کلید API خود همون سرویس نیاز داری. کدت هم برای پردازش به سرور همون سرویس فرستاده می‌شه.
‏
🐱
گیت‌هاب ccgui
‏
📥
صفحهٔ دانلود برنامه
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRcRBOBnDuAxbWq-8HA58VIGAE0oLCdysdZlV6LnHlsJK0xiywSGTUoduv8D9Zsu-m8duLWvnzNCSdRo8yJl9XHzN2x1pfEwotHiA3J_K1mUNhCKr5Oa-CHZIIqoSLWmBjGrvp96Slb1xgw7UFrx7-zK91MfhWmtML8JLWBT0k4DnR0FT3c44aEwuGuMqMQVMy_L-HjQyybPNLIbDmeoQkwUDm2YzS8D60cpk7xAMvGbzghnMGB7oLyvVF0B3eL66uQ5r8-9uVQhsWztp_ajzSKUhZA-W0Ot3sz24oOfmE8F3Pr45Y5fUxrtuKarSfK2hFWhvoivASXt22YLauCSDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-14oelBsf_VGMM6Qq3qqb9o6r3CNliPqHjZzuJG_Wjs_36iEWTR9gFXrUvLIg10tX9EeD18ZdEvYhphUPCnYcfTtctlrcr37GejOk98y03e0Ew899kJkAYezPj9lzJ4PNA4LnSl1VrNtIGEECCwgxuFju-kLn_sJkF2gEF49dvg2YEGZGhTaM1PBlwJmMKaAwoNA_oyZ5XmZlwUFhjX4nTpVqNy4flSwSVYxDECFaLrEbEB4FgJ5WcMvhteeBG1AzSU4hL4nJZWVJefrVjMRQG-yJfQn4A4fCkNmcPely6lRnHYg36XK1CoBJ81CF8S2rIaC1aNzTZxfgZpvt71pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inCKH-j-qNVxoflk3Ijv4PwvePHGcgP-7jo-18_snSDlQ2XssR2mVfDcB5ZsOIdSDXt7pPANNOTsxAWIqRSzafPgNQaK0wYh1fcInQA8wJs7b89oqTo-0noziliGNtqLTlpf0LFWQ-2Tc-ZPbDaU64pzSuRf60hi0MGIq3j5m1nj4MozOP3QqoWUDI2QUpBS1X5YQ3t_14OtVxAvAKPsQFRcpm-xSS8FF2kFjtkJDMJ9yN0VwbKh4FTxFUOkK0jtY3aUkx2HuvIo8Ppz2WAY6azmQyfltkcHXXrGHbazETZRxtgZoE_jLIiwdPggv3uK2K-lMyx_ddNvY8Qk5xaACg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDwEG8MXB1cxctskoew3wTQjaXBlPS6za35IdPlsAXxcApgxLLH-9LjEYV-Hoa72iLqm6tQT1oOZTcbsypHAsFdLX8S_ZW6ZWfipmItqCYKagQt1XGkgSSWOY_qTntO-mjPpfYmXjFJakbhj324Bgu8wuF5y-SAOOoOb0vaIjHCfijAOgHfmJ4CleViwBxH9_Ghi8ZThIWkhq98ykBY5rbmTwNlQ4m-vVtlXFu_gFDaNvn4hxPxSE75mQNRO8ZTwr_0DNMj6n3pj_cVKf8xbBffAX27ggEkKKKFUpp5QZa2WkaFpp_8p0cQKuSda6zAMasWSsJ0t8nOijW0QsXNMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H65v0T2Of1gw-6atjPvHD547TOdaOwN9VJBynuLxY5g7o3ygWbDMSy4zc0zL6DasXz8G29Mm6s3RCXApKizJr7fp6p7jN8keomQcVStqAu4wG_aGhBKrazihjLhl5FjiI4_H6Fhgtij5S1bGOT5hVA0PGpRgydxNDmS-8tEuh11vSIjmCGT-AADb1uIxhJIsWLpTU62WDNGCOIWDOu63YlR2DLMmxFYNZ7AwXshblrBimgYgLTbXA5U3Nq4lZtV8hnBh07gAJAjUhGQpF2jM79tV8yvCiTIc5u5_KyPFXxw2AOcJ23AkiY1a2mKtv5qJ3BrmuLG2ttL6jjGiBcT0Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
