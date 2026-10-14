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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-23 01:19:55</div>
<hr>

<div class="tg-post" id="msg-8102">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doh4qA3U1LJNjNJFyWqajG2eY8cSV14z7CF7AzbZNlZhiBmtrriu2KWx5BdbfxgWvivyImqHgBNsAEO96DgZ9_H4A88z-nReg9b8xBPmDzxO7D9MvqPrjzcAymL6TGDYzhwIEi3lZ0MZzPlkWsQtKGHkKFXhZfTUNX9b7J72fUmJ0hPh8x6zbvMfJmChc-92QJJzIgehMTPAJ4W_tFugC8zfEJnUiUXz4DKbj8-vcORQ0QoMltcRFGe33VV_varujwVNtdKydNmnigxZd5IBz-ZzN7CzlEGGByMTeIOoJeSzwyp0zgSIYptjBIyjsTkXYZI6PC0EHJrATGZKpMsysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💬
کامنت‌های گیف‌دار به یوتیوب رسید
⠀
‏یوتیوب بالاخره
کامنت‌های گیف‌دار
رو اضافه می‌کنه؛ از این پاییز در اپ موبایل همه‌جا در دسترسه.
✈️
ArchiveTell</div>
<div class="tg-footer">👁️ 423 · <a href="https://t.me/ArchiveTell/8102" target="_blank">📅 00:36 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8101">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
تو این وضعیت اقتصادی یه چیزی رو برادرانه بهتون بگم:
رفیق گلم تو کشوری هستیم که بدون درآمد دلاری نمیتونی امور زندگیت رو بگذرونی.
🔵
با حقوق کارگری چند سال کار باید بکنی تا یه پراید یک میلیاردی بخری یا یه خونه 10 میلیاردی؟ تا کی میخوای شرمنده زن و بچت و آرزو و هدفت هات بشی؟ میخوای زندگیت تغییر بدی ماهی 500 میلیون در بیاری تو این کانال عضو شو ، نیاز نیست هزینه ای بپردازی
💰
:
https://t.me/+jGXs1X2rLwg2Yjg0
https://t.me/+jGXs1X2rLwg2Yjg0</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/8101" target="_blank">📅 22:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8099">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/8099" target="_blank">📅 19:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8098">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/8098" target="_blank">📅 17:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8097">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/8097" target="_blank">📅 10:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8096">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/8096" target="_blank">📅 06:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8095">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پروژه زدید با آرگون ؟ بفرستین تو کامنت ها بقیه هم ببینن
❤️</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/8095" target="_blank">📅 23:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8094">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOiHWWTGeMP1WTqh7xeelbggmrZ7YCYQwiGnwnKQ8p_7VXCkSfCJS3CfnHaUxP7ItzsLHEA_uE3hWVrOndbXjmlB3TthBRAMJGSBch6LAKvGLVn3m_ao1m_6OCe2M0xevnlO0kOC-BEzs-vuYsMu99U-omTGTAcbHgz3JFWWBapBafq51JB-TiePV6ABNGq1vXu31s085lekct-VjLeiDLHNUxL-UEjIb8BqpK1eE2Wa8VjsWoDFq5tafJhNVyx6YSQYybqEIdN9PYJ7-kiIxUkw7f4rz5yC9rD1SNVD9wvGYBQJUE5fmGeoi2MetOb1C1cPewLpzL2PQX8m1R1GKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/8094" target="_blank">📅 23:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8093">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پروژه زدید با آرگون ؟ بفرستین تو کامنت ها بقیه هم ببینن
❤️</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8093" target="_blank">📅 22:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8092">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ph0aw4XX3_4pMBS30yHr8K3xWcPTM6cQM9oQHtIG_9EhR-T9o5chUkayFGE1Csowf38r3EvwJDd1pXrMrx1_2aj2aEa56ChdAr0bABvmOQBloIcZkMEEDT5i6yIQWoIURdjLwTlFxQFfTjlODDvo3KutKO75vAcdkvHmT7ri2KFVK7fS_HY0rDxUtcYv5BMa6c80qV43qGJlzWQTLeax8mX05e4rNz1FNOeEq4fMBnZ4fZelzWGNnwfYgbRCDw-w9PgBolLKvoDVQTldyn7GDkUx2EZqpFJB-VLb0q75jVKRE-aOPMVfZPEPntPxqWw7aG09gyakLZIcb-7b0qwlOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیو هم اومد</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8092" target="_blank">📅 20:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8087">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgfZIazIw5HRvaV8b2Co4u4UnBn7kPQoLdPOR4SwZoVuTLvmaca5EIO3JTWNZnjK0v53HMY4XT0sn-yTLlu5Q28LBJWc4fZ53XfLedaI1ryVqJI2QiwM5oLQTaAlSfgYE0MCnysD9GJ5PDJPo5BU5YWmlvXAs88Q-kVHXpG830zv5ynGfM7CFOc0mMlWgIMnlv3eJwXdSKxmcqhImwwBZLiRT_EeqN3DalFFqyi5tyIt-6OLgXue8EUcjmK4w7EXpfldl6CITsYBXRbvCspcEVUmHkY7oVjd28A8KsB47wd27q0umiHJEwqgPebKJwuiLVl_OCyZKCJA8G5lyOaQZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا روی پلن اولترا منتشر شده ، معلوم نیست کی روی پلن های پرو هم منتشر شه یا اینکه اصلا منتشر میشه نسخه آرگون یا نه ...
💔
یه چند ساعت دیگه احتمالا بنچ مارک های واقعی جمنای ۴ آرگون هم در بیاد، خواهیم دید که درحد مدل های پیشتاز هستش یا خیر ...
🤝
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/8087" target="_blank">📅 19:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8086">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8086" target="_blank">📅 18:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8085">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNc9vJVGktCcwrTsIkOSWpGIeKKwQZCzFJPBdfBseX8VSDVqBCW-JR5ropO8LpWY_xgC1Yt4kXVWSsipiK3iVDo_1cZe2JLrn6kZoSugvHtzJVqCjmqU-FdlFAKmOniUC1Nfxk0WsburPPB9XSw_1edFwyUfH_kHJ8TbTjaZDde1K7jeP34Fla5Vle20hTZgF74vQJ9NPwVRS6oJ5nprSt2Ql0EyridpqeVZwPR6AZY8QPk_ujzOuWOHM9TZNdk-c6LKZgErCKruzX-7W_ZW2BavPPQlXFC1x5WV3FWiUA2uDLEjrW79UQ7T1WD88Z3EoEBJR7FIfkjJtRKYJE_skQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎖
• بعضی کاربران مدعی شدن احتمالش هست روی پلن پرو هم جمنای ۴ آرگون دردسترس قرار بگیره ! ...
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/8085" target="_blank">📅 14:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8084">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4tNRWgnI1tijWhAIh1o7Sx_thRDZrLF-lFaGmZ9_-G_0ASNMXAQj2gemFuCZOFCGOv6wqKJRsRrTtehRN3x_yaWUmunBPutC5RunNnDCHE_VtzoL84Ihhcr2PDz6S3DYD19iluy4TIHSDV8muvTm03BnAKtyBYDGm6gYf0X0SfSzC5nLotz9we7sXnkGrsVivSrIw10nb8FAwxE6MhaQtwpyzZNCl509azcXm67-R8FC85J98te030tPEKK2rzg7DcySwYDm957dJhxHEbfxdwgO3_utLo0ok512Jz6P6raBljdvVSGvDX6XB2H7qwmlsP3hemueiC1GX_cNvuWrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8084" target="_blank">📅 23:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8081">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTYN8SK4ay5-KZTVWMUCclF6iZtUnT_UO9dWaVZrH7WdAEXQku-Bk8wOCnT5z4UZge_Jd5WyjJbdBkUDzqqQUKFRK67LHK6cWDpoHaEOSA5iB43VXNpqiWZcaNywHl6KgoMaVKnJE4QwHUynKjdhmv6QJh7uTsrSdWINAzj-IX-3gZXY2CuG_ToshNgd9CHFf8zGBeyQIoHyzZW8r2USkWPyx2WrUkDfvUF5A0bvQ9GibchTxrOSneBIDFEdFjzMwHsE569junrDZF1L2zW52qmOE6pYy2xi0Mpm3VdO_5x94d1JirP6yXVIUzfBcgTwacHjiszjBcih2xC0pLJ1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک این مدل ها در
Artificial Analysis
منتشر شد
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8081" target="_blank">📅 21:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8077">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/8077" target="_blank">📅 21:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8076">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAg1eXdsJQkKImLkPEtFuSqc2gGYS-LXjqXhCtfDct2Mn6lC5CsMicHi2OITXI53Kjq58_FLJFPSA4AqaC4dv0vejp9xbwoThUV_VdlneB6ofCEGw0crcjTRCb9uKB9zVhehI4cZLz6_ID1zq912ieGQgwzV0vF9aX8YzVfiyftH7cIB4Fy006tHfpCCFRarshk2scrikubNU-H5cGd7jV40H-1fL58XA9SZ3sAqta1iccKuIopTsEO8Fd1ol7PZ7lMHhLHyNfAqvtvtytyUlCvJCylGJtO55Inij8HanF_QI59-AmhsMWLt48XiLMEWz0l__ywWuU0sc8yX85drrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعب
گیم های جدید
https://tehran.velestudio.com
GTA Farsi
https://gg405-golden-gate-racing.surge.sh
Driving</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/8076" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8075">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG3HMPHWjdpaWuV70mYjP_7SlE4H5kJaxClO00Hl_UCVwNocbOBulJ4pE69bRk_EUn6FFiQ43VKsouCB-CpXzGk0ZNUBqvVuNo_99LSIREFugBljKRcBdHjDkFnUcPBRznZIx8NGA19LHDQL5MD5X0chOODMuA_u-yzxsHytBZTdpjHn8TcxP7jmKHGr9TQQrESnStiH3R_YmMsoxs0-8b_LUFsYYrDdLrctMsAVrkw8WMoH5psEFI1q9xPZUpVRLKX9M9c-XrGCkqHDQZlNhod4lQtv-LK5TQLPePtYNMStUba_ehUzVdZY-kfY78XXSgsyCh2rOipu7sV-5c0A9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8075" target="_blank">📅 18:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8074">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1pAl67W7iIQr__i11kjSuWzVv0Syon-tA-wVZQn86wJ9gRoJ2ewXQmS2YyhGw6rVDg1e3V-Ku8qjREocEa2NBUx0uXAwxtDzoW87Z8rGDdzeboWG7g-RTYS5pQq4CijE7SqQzNzYjf9A1vw2Xmq5viweDFN8T_oJzuRvIzQawJbWnFLwQp9bYnXcuFGYlBZL--UQLpGUxmT4PpvYtxTaxsgW9wk_WSoG1g1gfdyRhKdJTngq2z5HEgKRYoYbjKdvB7XzyCySVCXZA_bffgCkylsN5ebcbhzSqEm6YCjwg1chCnFv2A8L4gmPq-oI6EqrYsBf-8Ss2viLY0WLgr2IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/8074" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8073">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/8073" target="_blank">📅 22:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8070">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/8070" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8069">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/8069" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWWgVAv4gQ2ML7K4IAtC1OjIeVPlBl7FuTQIFM29pyQExFGAmJb1Xcpf4JC2xJnpvhgDQ7-T5c_MXsYjh5jgWaZ1603r1xjWo2JNNAZSSEONoRxTiBYK8xrQOEa0VJoWJSBPbfU0wVGe3LIb-W0wLAf8Z5jUHuMkcMDD5EgEmewt0d3X5GZPl70aHmk07u6cU4CHjbcjxWnpn6Yz7JrKNUwGAiyWIzoX0Hytmf67DWMHroCBrq6EkSveViJJbDXEMps457CggrAX3FX8fDImU3yBMVjb5j_5B8nIwDhGeITat1ovD_G3LlbaCnrB6V5KqiKhteUAha_Iu1-StwKcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8067">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8066">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRaHGZkgfNHcqKdZhH8IvqbnKK1RLyQA7m4xAgjGteFTs0cGbHDj_IP0DyCZA5U7uj0mwp11GU2471kzepbcgD3cN4phILgUP6ApQbU2KkeXJYjuoHyZu2kCzD0Enze_-vgA8w_XTnOk38CegZAHKm-M11ZJLJK4XJ-spR1B_QJJ9IhMa_6-ecc1wOCInJXIEw9KbYK37LFF20xpav6nUgORCWpQ0CRA1c2CEbrUPL5rLyW8-z2ATiWnjKJfJfuJmtmZa4zIE3fZJ7BjlGJHSRaKH4jDYJw22cS_FZHwR3QVbELz3brHVJPNPEphMOkTyPBTyAce5-In2B-pYYulnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9iWHkGUNPxcUhnwRvg81bqy5852lRpQmbSP4RloCj8RxCsRw5idABLVF9_XpGvVXtpXXBDBmnHx9pqrxFHjD0cJPLwx6cMYUQzqGy3qKymy1jSggb-2f581jh2aDsQ9_wsOe_q3tnGPyMtCJtZw097lFDeyrGA35b-pnnUjydPM3Wj3Tlm0HYstYh8PsGnF-XPVCD_JBGC5NqoJcJX4uSgLNFc4Zidh0YcDQb8uPOXWZGxHoIW3BU9it0wYCtBtSByeWQt7Y7x9U0QS1-VwvVGvdRaoWYen7tpgQIGYFZhjjHLDd2zlVAPJC8HljScJXJEzCMDxqiThLBCrN5xZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWz0Wgk250PzVxyQ1siZhHb6V8RZwrSnLtVR852-3L5-MiVh2l0xY52lnD5U7zMudirgJeVwS3ucn5WPVcBy7sB4YKlP9uiYgu5x8VghKzJsYpRagk2z2KILpwJ9dOfB9jWS4McCgMMe-LNz4lnod-bVB4-rdUAq8Gyp9h7160oXP8Wv7dOAhAu-dvzX3oFpYx_dV2r29mBFL66OIAZDXCeda0nchHBT_jRv0vCJEocESHiPkR2VmoTXJP8HMcwQuCzZgA8yEVrps7_qd8ZsqqHVML09Z0QijnNixBPVmkK4YAMaWDHIT3GGtI-C-GR_Z6G6tyiRcd8QyowSUzp0cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kh0lyHfin5I0EvPVu6eydiljdyOut5INroqWgHaKHBoCcaJJMrp7XN9D7Cjs8LfkH5oUCiX-IIWRAAqXZ47aq-rx_Y0lF9WQTLbkRBCXm9shEwP-M6tq1Uxeh89cj8fvt1-5-EZI54hVxHAgDat5k4bzlCSDpNe7TyFeWJhqMNitML7YcuIs5RkZXNjcCMXTytytMFt0afmfjNpLDg4pC3_75bbhPpSusrRaZSvsnGSbOoqB8s9OBMOlS2lqCYo1RV7ZGvB0GPiuWLx_iSfSTXgfHNm2Ozp0FykRJD_3QL-cFfimAFOI6fil3Mwrc9B9_QW2TSxOmvJUI_Tuo-esCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VuOcbJ4bFnBoEpnHfIiqC4rYOIVk25QiIRDlcVonmkdyl9DCqJBHJHDEbHJqAdagw_zFWmS7mKAY8bDKqFCBw_4pPdOkjeGtxunSoVcGh0ujlVTlDMueO-V-6HqGr6GXiZmbdQkkSvekuCk7q0PH5d_E2WOL9ALtRkTj43J5L6L5VXsRLqS2bBByO0_S6vvQ5sG2Pefz57GaQ9je96QlERGg5sggx8UU3hlSJdlgvzZb-qB_oIbYKp3Vn9dmpAj0AjCFTMUaev3qesYlAiKLZjbJyV1Blkhi8WSo9O1ymx1LkO6TULVX9EZV8jD2pAd2JXZy8n1HhNClDxZx0O9L3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGqbcRVKbzwzVk7hFzzmeePRzbjuAev9eqEAIEDGuNaExq_CwsYjSQlJ4rdBcfB5jCdfiejMCmBUR2Gkxln8dQTdbYB1sT6H1qQlUifi8abN9ataDj-DlwdBlTIFp7X6QD-CRr_gzlGkW3H6aZppNjZ-jLA6fjqNe15ySBqidmpRsWKGkRbN6aP8AXqXULciAO3SWytAK0zHWcFmCKT9Ia76CHdmJMSNrD6c1QSE62d7ztFvYKr0sNVv-ZHlpa1gSs0ZrPoMzjcRIip7ts17hqJE1u9OLvS4jj9W26AFkLUQVDUjhSGRsWJwwc84l93mAPgt7_7ykuhuEMWY9S_PPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIncECZDNiPQ878L4qBvqjWY1_GQmBLPFUWovReUsPslq2Aa5Qsl6ZnYyly7Uaquvb8Z6kLLa4e5iClWliaAZC9FG2AQiCEqk8Q-_ees5N0ipD747O0cc2Snbz4G0gqHmolsS94h3JaAd-_jz_Xvw3IIQ97yu-QNoW4HFh3GE995h2vj7I3rHjEnjwtWjdUtEYkDdTfWJgcgPLvkFSkqevA-pcBhPHt6njHaJ7C7RWRXH41oZfhG27JFwKSxf5c2hid1qIX9VW3rpg6TVpDsUtdwvzTqyE8g6WVjva_D63bx4HSMIg0jAxttlhtbMg1vXNmfr5ATQgZkpUKeSEfECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVrLzm_Xg9fQdXFyKaYdprCBp6B8OORaFvP6GG23mKQN5_ptX07hAbWMae_b4iToAHfQP6moK77wLT76SJgXTi1ceeeu2ChuW3QdnSvdnhyBTVfvIzA2N__rMO_fieivC8Z0zAMr5haD1o-sXnln3VAvfyoqCqgLVSXLGL5KV9wh8Aff90pJjjGnwS0NH7Q36Ts6WK76WYlTHvYYektp0Wmp30N0XntnLjSGjDtvbrIY8dt4mo2BSpcwFFxRlzi0miQbMkX2dlWncB-MSOPeCyZVfpYS8KezG9qncQ3-kxNxuil7PodBNF4WHkJCSq3PIRwgWYx7tJV-SlKkPx4MRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KghrzVCxwNDFe2FLbUiupEqFqFR1IBOed5YsksbtfnnR5EPL7-IlNY_NdsceFMVj-Uz3XV6UHUFvU5Ic3nkAF-0y_mzx3Z_ktSmKSbQx5ah5cJ8DxhfRsZdEGLBrnUKYN3rr_iP1kKB4XflxEs1CwedBsLNwa4c5sHQuAqgKo1Ecv7w4zPsoYLAMdTl0NZ1JkCK_jSWJ1mPZF4ljHm4fxw44A2Uol0iMVz2a7QH6Dhg-utBPQ34LYnF-E-SM4NAfpgXLgXDo36KnZcjqubb_ofq0s46CJKEUV6pWdqrMlrJLaOmZu-FpJkllKR31WleYpSgkZXFf2boIaD-YhnFrCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoUMpBOL4aQ9-5ZDG854d1nsDN1zWLez3a1PjZiEv2_jsTr7EkVCxk--OkjB-P76WT0gqXxMi_OOYv6WGy-6wtdI_Oh0rz9uQUAwiOXBzjXR_YLVMwRVN4I2XlOeRZJrmZmVnh_JNzaLrXUoMPCvYhT_f6BDBgvLJ-W75yjaYb7gKq-kzFjnRKcA2pqxzw_-aNaYzggH9UWO_-J1wveVpm7u3GcyVGpOMY2b0idb7HRY4LbD8u2-QsE-L1tRIKNC5595h539YdtXy48xk7pgPzCusZdB-hDMXSPf9kKRH790oJG2JZBXLcJD5VHasuwG82gG9IYpebAgimAew-tKuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=Er2YCMOYdIyKviPmywWIhR883xAbtETNVrvRdgAtik6c1oqwM1PS1areUs0fUL2ttY_LgZMN0EBxQf5d7OyXW3vDl9b61LbvOY73NOGXCazYvdMyvVbnnsnlfEgO5uScfILABsvbpPBOh8rFdTFQa7FZ5ba8_P3-mkDlzzU7qgRIH_mL-b9jYoLmqbv6VRjEGmU5sK0UUa3-ezw3O_QbyXeZj1Y2JH4F7G_f4k7BJXo8j7-6VUX0lazPugRvONX60nQLC8PGnVUq6AFoRMzG_Rom93qEhzuHQmqKGz611UCSC45tTCNT_xdbG3KicUrU6F5ocZ9wBM4DE-ltv_8oOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=Er2YCMOYdIyKviPmywWIhR883xAbtETNVrvRdgAtik6c1oqwM1PS1areUs0fUL2ttY_LgZMN0EBxQf5d7OyXW3vDl9b61LbvOY73NOGXCazYvdMyvVbnnsnlfEgO5uScfILABsvbpPBOh8rFdTFQa7FZ5ba8_P3-mkDlzzU7qgRIH_mL-b9jYoLmqbv6VRjEGmU5sK0UUa3-ezw3O_QbyXeZj1Y2JH4F7G_f4k7BJXo8j7-6VUX0lazPugRvONX60nQLC8PGnVUq6AFoRMzG_Rom93qEhzuHQmqKGz611UCSC45tTCNT_xdbG3KicUrU6F5ocZ9wBM4DE-ltv_8oOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DO3ixq30N6LJP7LJ8bq7j1sHCAEEOjYpUOZV1MXFMQx_E7fgh_igsDF_Kx8-Z1ekmOAhcGh4HL32HET7VxOdojWqcUpY-1ina8sw-UrxtUk82t9gF_e65bGoXyQB4H0UvFWE41hd4z-U05z_7HDXiE987I4GScGWGgesaRzQ83g2LrdIVB6RoB_rxKkn4nGNuy23VSH0AeYyRNbWqvpvUGeebr_sgw1NbuybYf0YAD2H145tuUg2lJyRaqlCE2x6zyxVo16wsjtjRCD3nAA-hL8MXZ-UUf3y1j4tuuBM8oE1J687QqyEtXwp2hNzAd3YGXyEu4rxjBn5-t_HMW52vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-zf1-HUMv7L-_YvTnH08Ad87U_cZZHbLEXsXOCpus49fn_Opw1qLMwXKbazv_fxk04w8s3Mr2qNbxyW4rrv4XaDsDP8CDee8yntei_oWJI1FXwbIZ-2G5MMP-DAHOBfUETov4krGXvKBqWUuAqyyCfLHqHGRgYpTw6Dw5lbF8oymYCxq1wzJa6UbgUgytQ4BB1paoVZUUUur7SsiyI18p421URKiliPixV67Y2tF74ipNDf2RVrLscdyUecQrxBaqkFmofqgqjUWfFqyDsKxoWgDHwKO-b2mFCV6Yh7yv92zUR1TdHJFD0ilSpkYMgpKD0NYCsIg43JYMJlPOnd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nvGunTL22pwugkGA5vBK84lFxH_lzn0WBtUl8vS2jWZeWGKYDM1FWOp4-2xIB8IuyNgh27v4Ec4J1lUnWiEs5BbhXMDe2o6cJqwnN334tigHDrE3l28WUuTxOuWmg-eQc1z8CBk6ThF3hJax2bhzOYgOd4W7STLFPLHJLnS8BMXLZWeHqRCvRMk3Npv0KuUThAWWheHwkxEFTJjyO-1eW1WK4mjdCmxXeqHVVSVO2Gds2wZPfvjFTKlGLfqbgaSW-ky7HZew4WObbbxGKEXyQ0MEs1aD6X3STO93Y8ksF_Ik6t7gaDmVV7HvIOMFq9VrZaAyGrrDCl8IOf1kBqWfCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=YqV-sJ3qAapCtgMK6xkq8WMZo8qfcifsV3L-XJ5oljj0ZSi6Ho9D7pCz5a1FIJ-R55z2_eH09j0q3SxtBspmVw3QrjxiA7DgbywLtbZkLJHsr6rvEYsCHMZIyOp1Zzg7XRsl5WHldfpYHvkJHmoLdHpc-2mZvr1_3NxXsoP8prh1mnb20Uz8_4NRP7zuWn_Y7cM3caTgUDPTnGNrGHPshpf2T9RN9TnL1tzZDsejujo45J30B94WnTs6qoogY6ke3b5XRtfhC8Kc_3oSzCnA35heg7fjvLYtCghEjsnBa7p0IB3a_bDuBJHkfj5ii0J3H0byntsQxXktdU96Oh-HcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=YqV-sJ3qAapCtgMK6xkq8WMZo8qfcifsV3L-XJ5oljj0ZSi6Ho9D7pCz5a1FIJ-R55z2_eH09j0q3SxtBspmVw3QrjxiA7DgbywLtbZkLJHsr6rvEYsCHMZIyOp1Zzg7XRsl5WHldfpYHvkJHmoLdHpc-2mZvr1_3NxXsoP8prh1mnb20Uz8_4NRP7zuWn_Y7cM3caTgUDPTnGNrGHPshpf2T9RN9TnL1tzZDsejujo45J30B94WnTs6qoogY6ke3b5XRtfhC8Kc_3oSzCnA35heg7fjvLYtCghEjsnBa7p0IB3a_bDuBJHkfj5ii0J3H0byntsQxXktdU96Oh-HcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsI1bm6O7FasJpor7OwNykyXd6u5c9_PAthJWtlGwDhg-VTgE85i5CoIUwvjNWsdKW2RdOMxnhFUsjpWY6w75UEnRlF3IpRQvyN2sLNCvIcxxFe6RHATtm91lmouZWaId8-B2nnkwJBMP-jRQXrCPjzlIH7P6uSEFgWQ4adAMw54t9xH69LzqCY_7e2jimJOH3zmyZDA5fy1ZNGNPTAe5D6xVE7d0GFOSSgYwUlVj8g_bC-sACxHpoLGTZwfcXp2McOe0DmMypSEOGmu225gjvxfDLC4aWotfVU140e9MZeiDPTaIkDNw0bzYRlHu5OkjT1-frdbTgU_mrwS7kucVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWu_5i1QbVzCmfvvLCWyRuwYNgS46WJ-ZJRxSNI7J8kUnRqIuz70FP81i9WlMnsZTvPBUfhEqhpAMrezHNpp4U42MnHxnHSnhhjB4lJCDrAmWF3kQ2Z7paXMV4HJJlx4zVvcM_bMutT2BOnah0a41699ClV8MuZAXQyEi2SEhhMCwpaBbAx7APxkV2tQb4_lVt2FCDlDV1I8tKXPcZlsGkhqw84zV6ihf-Q25O6hbvsu4cAUIE-kFOkVLWbiuPBhuRcbm1U1BE3LDm_k-pe2_cW3HXomeQ7Af_0EKXCZ3RCpePt6O6ORWCMdipgVf9z84KTODg66jL55Rann56FRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3gqLgTcaTs5lN7AHZ4EmwN7f5rWPe8AYqDtXnozlfEzlnmPzRsoiNhYz-f0O5knrgQHAq8Y-9rQekv5sv1_ZKrcEW4GQ0Cg08Cgdgd4TO6vQUDv9345xHBBRyasCkmOyO3882_NAI49eyPVSyJAk8eVgFZXL4O80hWocJRMptZEV1thowE34l2d5WnF2t1FmQVYQs9Qqet_A1RGEYQc0X9XtH6V7C1Woj5VTVQwydCZ5OlT8aN39PpoK4TPXpuGlT1e5D3q6vehdLvv7vLgD1axwjWjuJTFCf6mVBx-_2VbPm4fpORCfOaghbTF7ZU8lTmJ2C4ocmFiwAO5a0KBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbAv6zHUSAmCaU-JRxboWaod7ojJ0B_ybZzm0AVnbujYRuOKnQB5BfIzzEfRy2QVk9TU-OZXRY6aCNG41TvMGCxH3kMlXcb1GN5JVPSUdLCoUWBysT5jbVfOkxEHtPNP-3nzahS-n_joQg4ETcM0vC2JVBoMGnQQsTx6U8YnhYDjXWiKXtxhwkhEfxi0URJ-xif2r9nYRX0NWjSKflUdRKyI_1H33u3wnc2B5ElGRujjxuu4joQ5TDYWEUzQwy1mMU6DohWsCNdpgEeemj42L09bhizNfwa-z1J_U0PwwQ2k3FrUwKxKJDfyrp_vS21Sn7wMoqqKBLx1pOtzsll6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8ykYjqMD9h6GnEJtofx7waxJasO9Vht9sGiJyhF29DLWDNJhmhrJ2bzzb7HfT4C5ttBmuWtmPC-wOmrx9QzKA0WmG3ySIi14x93GOqfX5A44AJA4AH_qpAO-OQVNAmOtPBhwi86TdJTlc3BgX_pxzrwGlF4DsNLiikO3q6wUZVR6geURJ0MJLXphuVgqlIA7Gtx--mZR3sCkCzZVY38-FIyeB2FYmNG7rNgBBvQJ1vC5WZ3juXFOf9Lx0ddVP5eQuYECQv4kqtMD_WF6RbebXffz4kJlVswgd9yKdlD83gLaHvSc6sA0h77OoE16hqWw6FZ3kFd0ccSqalXJAfVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENNmmkKC0Q4R3slmmk46-Q9_6mfgHKQZWrM_cPPLC660-OYkhKN4ZZSjfTOTgbD_QU05DhE827bJzy6fUUHN1LH28067wBy2lPM9LnuE8CJ85ttl-9jHd0pAEGneNBr57vGmtPa2K7p5hPG5IKGqBJRT_8OSiQk7tqyJQb5j6lq4aI8dlfn7PkoyXSTJGH-8weEZBSpJyK3ZUpI5zxF7T05MIcf2Vp_TpnH7Eybt0ybt-wiexrftmyOIHaLAk2-kgqxkNwF6f-CuN1NK2FG5RcPiSpatnSt80djAFVretl87KiJfhBC8by4_wNGpBpC2keXNH1e5mSC5ZBSwL98INA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZmfd5UTJis4KZDYs993QvFRHQg2nGwAfL7rOHfuCCA8F9UvvBNd3sH5COcaCPTj9jwINi9LBZoEJRQrEBTBbM9W1i3wF24Bq9Axtz0FRzEJgvy73W2O99kAmYm8zqDWDAjyhSyoAqFqEnwoMZbH6j00klQH0tzsGDBdBK76Is9EbFiKgVfsbFdIN1H1hCdOWIPgUEZmDyS1AXUxMe-5EsnerAZDO087bO-2dIOHzIrXPf_4TbfnsMxAuGxCBwni_ozPwqbw5Jg2e7HjdrRX2_Wssk9zp6AjOsQLSI6JwCkQv6VZ3CLxUqbxvwE42NuuRwUF1mJFARBbiAxgpEbIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXLB8DXTA6FQhj5BvdufFa1rdZ3B-XMHqNfSSGMAHwk0tsSSqHlUKobJ0fBmzEVerY7c8EItgtPjoo0aCb9i6e3lwuX99GHPLQ5OCHgjr2gQoIlqLI3vaEwiLumQh3-a9y5Zk9B2rLxL-5ompfDRZOugBSTacqLUbTLBi52rNaFvdzVeeKoUmHbYisQPrsfx0jFc1jOAKFaloN1SApsk1M7VSyyGlGzSDMD8Omj7CkcxIvAkLCfs5VrbEFiPuOC4lyCEL2qq4l1zJqfhmhxceMyYzyCQtkgjBZxN2iQhc89cmYnG8t8yfZPq22g7rswrPNfAG6dgKuKoGS5bQzLABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBgd7_OdpwDu-92BmW5Sbstq4hocJzCQM1kjZd40PMwiqQfa33HHt7qRMEMHK1B9qJI6JZm2uHALU4vzJLI34c3RSo7bhGPQDUt5GiXM413wzFBps-tvwj83DRXRUnM-74Ajt0vGX0GZtZBKUcrXujtqqaDktxP2jWGhVzfZsTZqrvVfucJFmAOO7-X4KtIS4Kc-86scY7E7Eq-1057oLVhxZNRVd3e1nKiLXNz6kybGa2uV_BbW_hbxeebo_VRzjtH3SGi5CAv3zO-sNSSZ3Jn4u8kkxTjRqq-l-jOBBq2yEjxeeIPP1sUlvGzBYQJWQ8uXyTJITEu6W948cSkZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vN-P9mvM8oNppz_uvIyV2v-kD9GtA53dFeMIclPNZfCjhDYD1YRJPGSAM9u2u1gAkXGP3KtbEJjT-1xdyKVQUIUL6fO_9mZJC1J387EyLK1G9qN-nsVqJqFKn11nKPYLASobV2-PPPLZZCIBf4ab8AWahPKkjEKvYFBLlzqTtSHI3FJ5KBhH7cN0NegVwoAwfaOjkdV_GyQyZMiR8aCVgyP95gXGIQh0ToLh8-uQdWdIRhQFjQqfgY-pTJ-SUqzscWxWNi_i2d4kYrZWCGkEg97nuB9_TPaIApGXdYBTR5T5TUw6GA8gvNxXzmeFeSmUhaJmrnbprBcA2hU3GorIyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_VzYvv6V1MEcRX7UB7xc4IZeTMfleM0hLTqmpWF0yhCijXCuh4fuDOyvp6v8RDdLPC78vOXpAf8EtPpx_azq6UdSSfoBmuQGlSw7fCht2pMIQItTBWavpJIhia25WlF0FQQmfEZl--FaGRya9q6cJQaK-4sNltPAd9mqkKfmtMpXuxsOfRKvrURqNyUQemAV2uceDjyldxShxjBfCK_NgVjcQoiQ-GK2YM8n3XdAb8Eb6xbWsisybbXWUlOcfxQeS538tmRgoINGcKU1XLVDxBUy7WzS-IFdnDmAMPw-RgK-2zW4Jg5bvueZYVK45n38P7W0JIJ7ZP0_fWca6n_5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXOPa-c_VbYSqR3mEUpVr55uhq106kXHJwyCpBxgogRszbffETMtBa_DojKx8qKQy2YMyoIIha2fZMst-JveACv5zcGzx4FsTuYgl5WbmhLk-4lFy-SKB0fo9A77l6DIwyH4TMD0Dvg5vVWN5ytk7nOn1E2aCktUclsLBmqV3GpT9F18jNJXvTOS3DZpRqVLgDD5I17tZvtwmNliLVIJZfcFPLd6wHhonrcmpcv4rKJCycracPvdU68xJ2ZC2r19FJ5E97PwF4GPsvN2O25H_5eWH3TNgj1jR59OEnh_QjuyU91-bR2k55JdRmIT8mHJbgVDf8aWbye66ES6Ego6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cYm8oeqYQUim7nzwwNA5N37tT350iacgMQnYH8NwIvVxlJm8yYm36nNbvmOg8pGj0qT8JJ7-hQ49jD1AuEgk3t9DneP_dDXgQHl-VaxVEg9impUSpOf_Tl8Fi8GfKP9XlLxQV1dGa1pabJa_Up7jOLTy6HTCUjFOpwaeBnQtvCQPh6JHdV1QUHUX7Ml36n5VyHL66BulFken_BloRjky0zIWZvnbmDVTf_0EyXWyRmTvUgTNdoppkKnJIB7JdJbFFpqd1ERqhC51kVMGuZEXuA4eym4Cq2sSrpvs-vYklupu0k6kRheZlVdiKuFsCcgZFT0I9hagb08bhCkMwxJsGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSR-xtmmszzNVC8HBY3uI7O3-iA3tAbbZPtopfmrKGot04kRPKcEWjobttsnv3EuT7x2i0dS5IJ7s5z-W7DqjgvuPuolwTHPz_RHj-UZZvjf_fmPsNBb8wgWWrG0QkDVjHd5mFF_Kl-Ti7mfw5g-ROeO76qHyCEJvmRNn6ESf9_1eT2d7vJ824-fSSqPJGuBLa-o4qXFIlw9SmaJprOv6HNh0mHHjpcOebw-yRgjF8ygSw6kBpfHADLl5wqTyo3Pfu6mfPFruZzWUOa89TL8XCbiTgKVElMbUoAvj4eCXRuSbrtzJaapYDZgmDHNn6tiBfsuA1Fidx7oFAhQe9X_HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=EWokLxjcThZiLNUDkJYIoul3KXsninr3nrfcxQ20GA_koZJTe21OQrPjFYShRUeZ6VRO0dnrTgCUpmiyW5hgrtnpS_r0o4JVNtbzv8zXT-9dR46wG-EJ2lodTVaaMdhRyWXh7hI8jK-cDCnSEZBi5uNPFEiGNNL1o4FFRBi7C_6Q_BRc84qN0M4XGGCJq2AQEEPxoVpnoHBSz9Ubsl6j1qLf6FpZCGMMy3SwiL5s881SUyxWMpIsLCvpNXSRnCAAnMKqFzu5TjGesM9g9VwYBBfeIeZDTrsq_gKPqu224YkFbvrhMM7YukeyNu9CEZ9hyUsUwIhaxlnY2a-9YddmAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=EWokLxjcThZiLNUDkJYIoul3KXsninr3nrfcxQ20GA_koZJTe21OQrPjFYShRUeZ6VRO0dnrTgCUpmiyW5hgrtnpS_r0o4JVNtbzv8zXT-9dR46wG-EJ2lodTVaaMdhRyWXh7hI8jK-cDCnSEZBi5uNPFEiGNNL1o4FFRBi7C_6Q_BRc84qN0M4XGGCJq2AQEEPxoVpnoHBSz9Ubsl6j1qLf6FpZCGMMy3SwiL5s881SUyxWMpIsLCvpNXSRnCAAnMKqFzu5TjGesM9g9VwYBBfeIeZDTrsq_gKPqu224YkFbvrhMM7YukeyNu9CEZ9hyUsUwIhaxlnY2a-9YddmAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTjtGNpADkM_Sg-JsoHyE5dH2XrGFeHuklkn0WK6132wPrsUQIsn04gtDmzKczRaJUb_bJaqSXFAO8V_qaj5-uFrTO2y4Yxr89OefcjKBEsjEjapOF01xPZqtabJphtlK-fxf344dTH4dXm9Q8N0nx-IFHvEcVohIJ2YSG4w_Zt0Z-JbLvpZU9SKZxiUnHMSXSRe65WEDC4L8tiwTYtGY7aFcIrQyQlSpWyUTsOWhUkmeMxF8u9E1717thA0pBQ58sFu5pvW3IEcu7sNsOH8YUg2vKN88NyALf6IzqzKauXAWtm_HKiRCq1oIEX_gbUFo4w0bhHBFbJ8fsgfgFZ9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RyLUElAO77TWRAGUDa_y-WJ7rDKEqk5k1P2FTf2xYcQ3nYruBNjBE2wT1WLXuhBUMVc_7IyQJzhcBfTVkrS6VVaP5Tvyuum5-YYLShC2daSeQhbiZjjoJVIu1KfPSlYoFwxNJIYJTw3_Rn6V-Im8YJlwL7RPLpOxYFQ4mFniUpSoSjEJ0dVyb4QjLoxmEOJU3HemxWzmYgYlE_qDahldNgOBha4IvrBsztqfOxOUBiDwcX1XaoWBijT50OB4reTdJLgxqVsrjhVrjnEhzTgRERua9bEzTDiJLwWwzl4LUI-k18bNCZVdL2Rrl3sMm4NnduSX-GaVJEkSzVOsevoESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuxaRCrVOZYzJ2UwuY5E1K_9rIDDKmAM0CDiZGw-ay6oVaqOMBPInZUy4zMWbQKPEUfnT5PzIFoFQTypo_sxnRYOqBJ-kP40MXKPDQVs_lH6q06ZUsrQGLaBMcQpdGfbChSD0vhhCUgGfHD0AMHpMk376Kg81rHY75PdOMFHABlkgKtlpKX0RfXtRfzkRrP4_A_5m7lmp1dtitfS447YlRpuNpSQPummnzAEoPpmqUjf9fn2DQ2nNMVhjXiVoWMqUHvDg_4cyWZxxqRZFxKICilJL0LgIpuq-G5vI16tighe07PZkPhDDUk9-YW7kSd9zbcEqRctvch5uBjd0T6tCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2wZ-4Rn-vy-DAhFQJENNujLtLJ5zhG-HJbpdsXP1RdooQWZtuDnN1uA1-jUDdXUDjiYabuLWrscxfuj729h-eO4swxmc1D_nMXpmBiNrH9eAcqMJk1vtHtpQlnZOxWA_LVUZdfvvnPCpa1CEkVTNnDKzDJakxhPk2-xmVwbNlKqgjuFrxQPDCfY2bI5n7_9h5XN3sEeczwTIo1DjILm3NblG7RdTq47TIEn2RA0NPnhgdUf8mDxBohE9cO3GuxW1_3Kg-_Q6wuDbKgcsXv-M0gqiCZzGMgDLEpFvZJ8BeBNmFCtvBG50eblhXUcZna2aWHJjk1f5xRx7dXQuwzyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IVFOTxMc7ZLCTl6pMVowrSuL2dGKo_2VreMn1IcQTsGzz8CN9kigWPXU2s8ya1OEp928r0R5QxTxz8zW6ShmhT2-F5ZaA4b04XWLPjl7v1HkefDAsan8oy_5PI6QOhBVNXk1o73JD42a4aWUzqwSMdp6NgQ3GH7uMt5LnEWUnlTxk-KwTNF_ja-8aZsUp_3NQQrTDoILBUwkI_20mdJ3OMtCG5qn3nYFyFPhb6lraC4_QtVWt1jGY7R4tp_aGyU0GNJXEzz8VaV33F7LEVv_Te8x1D8ZHdPLRlY1XXHYfKGQeR-QrhH-95A8ZAFAHgwivWxRoPvWrQ_w6pUKCxi6TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esIf9XOMfzDNiSHpd-vz4LvR_yZvxjuqD74bBi-Xf8EiE0PXPVW1Beq7Aw82jDNm9vD--hWA8isRaVHHeGnlQjChGO267hKeAWx_duKBoGgOlfDu_MsANk5g8jwcCNnEzef2TUHWLoxnhJePwfJ5X1kSAT8zDqfEh-yS5aAY5G2GMrQWxH_PjVY_c_yF3Ye_Cw3_z1U_z5rKHW5bRQ3ZKp8i_cAquhbmSQhIo_4Z-OZ7z4PeCgAb4zG_5yNvK3t_ppfuh6ZxNLoDGjfBblnENzLbpd1HY-7j6UoXSZqZzokv1ur_LbURLkUtFW35xWoHy86ILNhPleJn8k379HNpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qTMfFoaBja3VZir6O8Iddq2k_6SULf_fKf_FwKKC4eOFJpkIx1Bh7hI2urDkC97xL9rDIw5Cuq9HcBTC7D9Xg4XP3QBf_VWXe4K9VFZIyYZZ41zrAyGEbz7D2mfs5LOzJY2zc5KdUh-kOy3_LAb2o91a947mVCroda_AtSJlmny9vk44OXnr-k-tfgn3g6DKH-F0HbBFBT1dNK9_2YvybF0N8PIVQWGYMFdivQPsEFCmojSnCMqFUDKMMJDAsDIAs1D6dJID077DBqSR7Ru-0VQ59x-64hy_-wGeqy3_FGO1BtKDPiRpsFGjTg5o1QDwR7lUh-BU7HFlgmMDgoR7pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dcSxiNE77YbQ_wYrmhr4-sTSuHzHL2rfnQfr8DH5jbQpt_QsK5gA1ye-DUZBLeTwgwNNGcES_F4TBHe9wVGujjG1caFwU_VQDgAgpErYns6SXKB-hZAgbe3TpQeeavZJgrQKpZ1jZsx6hlvGPIw_U1kh-FnKBZIvI2dbR_li5b9q8z2XDfAVjb-TMlsY5OER6KI04E-CPYU4R9ICzkvTKgEdpN8WKRKGHa_b9xDbnW3QlS05-WZfsnLNRTZJZDg_SPJCtAWQa1KoAJEVLqLnyjQhg9T57h4Pj61UxugghqXBWVzalewI-JV5Gm900Od43Ut48rRmLGIsq9MFYhAtBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bD_EVAccvUNMaaqWtX8NDMdzWO39eXX80ucZVb6zOpPa7Ceb0OLwelm4qPjGAoRWo5aTvBRRSEkLVhMnmtIer0dmKSOyhgw6_r8PIBohl2aQ7Uw-g02UteGc8D3SlMLivmSfBzk48h-qRSMRh-ogMb5RjJl7EfVkT3jLLmOHupAaumAeIlB9cf6xjFS3EWO_fNebt_Pwj_VYRoO4obzMRRn0cCnqTkD5JLvRI73hrNRQN0C7cHnemrzF1Wb9aa5-xdXp7UmR9tpovj9xF2QRS6NnKiRPVL6q6P2z-OH9j1HOzoLX0TCzPCFBSnrjaUKKAoF28UrS-D3PhMD8qmp8Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMTZIM8tfzmVzBHgd-8i8nQKM3S1QrrPYSkfTwACIE96pF8l7zO54ujlgU5hNf9EOOsRlD0oXAI79eyHUXFRZdvxuCmivu__hkMxtXNsDhbM7tcHSaE1gXkyn4CeegrsEBb73csE6g4UKPhA58YvwISe8NEdWH1m_uGaHSzsh0so8oW2znsxdPjNOZXgg7mekFaDp8lt7PUu9y1f4JSAlpttkIVMI3IBIng-vex1hCReZ7GhsopwW6TZB30iusI5PRFR3hEQY8cV7I_1CaHRcxlof-rFPCaXjiYzl3GGQYBdXE1i6CokDDSEMvUhE6faIQqGM_-RYpVeVG7n6b-ilw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF7W7gnAsW482wbDg5vGsOtjROnPDu13YrVSJyCU3eD81r3tWrmJ72ECuY62NJkik64Tl4PFQ0t5rxGApXlkxA7wVc9A9o_BkJvCMajGQzq1-tRKA4pE9IIzulcUFWp8gpdYvNw-tT7PWD92vXpO2BLG9HI0GipTPbldpMnV50BZ8xPnaeAxaX47F1v2NMYEAsesbaev1G1oKTjioqlDhfunC53fVB2x8IYefJM9VTS4OA-eNoME5gVuhuD00anuZBYZ2893m6NDqDaDiSnuCySXFkQN6ifNszdWV3v_sBUC7gmFfZ9KXB0rBiqRHjcggCpBOO1l_aLjwhz5C4T-OA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0wqlMkECkv15WX9T2F-ob5kFkIxb4Evx5-OipgNi6TOue7_e3ZmqSvO7sEPfomRuBR-GR4VwRUkfoAMStwhhG-Iz9it7ryRKIsaCJVMdD07G56tzJoPKccC3iI1I467m-pPTYdg49CzaHjoAXgex98QoLZOvzosZuPbvuaxd1tLr2zCw_YANmj242lD8UxQXMmkbLuMpJoz9v9c6Czh5b-y-c45dy-N1yrrLZXD2fdNlkFzuPquFhMwiKV1pOZmJWWlko_-jgEz8c9TlGSCg_m63xwMTSvU7kBdfN9cPC_hJZ66FXhy0KzoR_tyHiBsxPIMv4ck2E0ooGtt8TO5BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3XLtgXK3v1oETD4K1rZucX1HTqW2oHNe4A8tlaq1kRh82Nr_Z5Ph-HeZPuwOuT1zfq4ZV0bwxspre8ntZfhlx8Mu5Z6w3cxpl-fQ4vdcWY-Zyy1ngkvwOg_fq3NfNSYPYnEy7B1C3tHAnF3TdgLnE8CvLnYCSrU0raYwjgWNJaNrROkhSjHmDDlQ7PSlvLsT7gzlAxQl_gKg1wMikP9iFLdqEPZLD6ez-4GmiPvdsRCXHmw7IXabSw6QBp-2au951aV9savdhTRyKwJFDuxg9dd8p-HDd5-kKmjuciquWomVf3Uy74XwXkrx0Ex-3bCpCawA8zNu_YKt23UAGwYIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z1JL5CyR8KGZsa_3G_50wS0RUKlMKwD_CMJaLFEj_CYZhsD3rkQInYPQTKimf-G3FkqaP16xUXrHfXx-ICgksbAs2ye2CVkxjQ_IQYWZgrgevxmBx57tCgaUVWZ4JpA5h4bSWn5UKtABlr6A1GqbvmSa-qgpkTozxUi1oh01rHL9elQ6lkGUMZfv59imnqINjBOzLM8Y_rMOb3nlr7bPf5tzq6EYQuc-bt9LuPtvlD8Sf115EhcZ9UoiiYykkKUad9Ptk_3xe_Lu-nLrniWRf6UiyN3ZJ-ZrCBDqJy7xyThspcr5-rgJ2eEWnu8eHcq1OkVz1a1L8-PzEfR3y3eQHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIY_vKxTv_UYHaHNm3TxHSosWstxYBZAph7s6Uj-VwvpDDx2cYg5AaY3hz2-_gxcde4v_L9-ko-hTvCB_6eVh-c3RpCPuJVl2ybA_MYlJdAA_sHKmjcLuf4cFAwFSyrAqiAZa10G3iy6A3uLtWUMhCMMHDaGJu2aohcKvOJru-WLh4oxwxHx9dUyIElC57lRhWibpGx_NdkM-5J69x_G9zT6irgd2mTFk17co2cROznmaDF2tZ4-jgB3xSHS71cMGX9lrIj8Ka0OuG6oUywVNS2v_JKVc97PY7ysS_-0nPG4vHcdJCbVpON1QaTsnuMU6Hdetmo_ZlV_KeCVOVEOZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWGWUCLdEwQT84RPNpJFoaYds17GsAChrSP0pwrRPIdzp4C99TxZVX_OZmHOYkdwiAuxnZH-KyEtK-AHbCM48f5tDiSFh8loxIVj-vxx_FB5mOmTu1C80qsI9Q5z_8ViYOLSSEfplvjr5v9zGa0gCv7z9NlPxN5PTPELs8uQ0wlGohwvONqW3YRuEDqQFPbTU9lvMjR-GguTupk1zm2P88kXi-1S3NHmA3TjycfLu4iud6rbXOITjNiJFzHNSf_cFqk-mwEF71FhVxJzZfC_I1Ti-2MqyPdNf6-zRuwz5n-mM8un0236EmQe8bcWZ0ueiWM6-KDqqkBaRIxx-dmXlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krGZdsJjgsX0B9rPUenlwcGvIWJfH2Bcin_1RAqYji8WqfV5y0dxznltgUDomkpt6EP0I9Rh402laV-Bnc32Vr3uUXqgS36QbBYZoYUUI05Edfp2mOzKrtSQfrH9q18V4odu3yyJJR6kK17vAnqQpu_yT4ifPfy3b2WQuGX-HuqfbAAiATGNPT9-__wExA6Pcz9EcGbs32iGLfZ1ShERcwKAM1VlaTXb41XCUKLWn7J-L7Iwt0DeRz7jYYrc826S_kNAFRii9Kf-_AT9FPAqR7aR7HSTae4P5zEZJ4MWt8DonN-zzWgPqi_maJDeQ39WkyJNa_yZbgY3ckrEqx4DkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcamzizJ7S9ZLvoEKhd6hh604QVHP-ofxZMcb8J44LnGmuWQt8uGUuJ30HgKV5K44u3UFo-RqI6cDya_LX9R0Qb_X9ILygT7B-FgGhKhjS3_j9IOhqmlZRqEvaC9ZnwBjOOzsWAIjpC8qo8luEDmCopnvNHFfb6EeFlfWWCc3gtGTbqKKJBDAquhMPNv6vrRCNuwzJ4M84bg9rPMwZnbPg-WHqMfiW3ju5HgYY3-UeTypWenXn0qg2IOFpDkSryDQPkXjXpuGjMPnWc3pfDyqUrSeUi2GDpODGCxKXnFm9O22ukYgjImyOpuQUUDdfsrWmixs3j-tGWGAWi36Ai7nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngDrwHIuA92p9YgW-UcTs8MEByEN-1-cHyXYaD9as6PL9GdhDTZGE7mHiN5j1eO-XQvVWkW-UfUZIoJiYvhKU5tuCYfhgmKC_I4mxB0PunctuWKIxQTCBNrJUusjBDNy0mpnpIEnfF_5uGWY17aIuxpqDUMvCG1hDK3viSVI9Pn5bGIQp9eKrOmc1RKKiHzkNO6NrL3rOVW84NK3X4AAwcK-yxz8V__evcp0aOowR6aqHmElXLa52dK7lIas7n-3dxyvUu2dgC7PE7zulHfxzaDjFSuAX322Mw-GaFI8c6T3wqIqFx0tHEuDgw-wxQjDSH6NU0hDilKrzBzGECWBzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lv1Ithp9mQfTSwGgADp3xZDr8LfNWggaajuy0IY9kp7XrFw4aXoucMJx5iYtTcn4R1dDFgoHqvomAWVGrp9aXtCbbV3dBLPokP1jNMq0Gkx5Lz9seOtbD5SZz2RL2DCHaxW0eBuIvc2A1Rua01HSG1gB8Kj0hXsUnrRjP-Ux8pbXpSxawAd3J8WC8_zliMGp76h33PU0LW5AH9SWXsChOKJsnOrfoS9w_gP8WAsnZI_GFJjOQnTZ-8EIHZp-NR31yRs3QunhlJeHjFMxSdZm6oSJfYTyLMHVYKtFxafzDLiQo5puzmRHHhbUFotoYWboV-J03--iRtK8AkEZ8KScYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sCjjWIM_HHJ6pHwv6o-T8KTRo_Jtg2OxiCvOo1YOP3j3CTaSwXGK2RRLVEv0xTJr-kumAhiGJgCyGnGQ6plD9WUux__DraWFzZyOWJ2CBq4h0jnjqATSDA_BibxNXBggUTDZ86uDmeNMoAe79xWQkcDsfX9Ap0YNIvWzJIV-dSoWvqe1YHpO09ZIwH-gpRFY2PCdi1EX3cHH6QcWAoKClDugJCOs_rLikU_QKZfXc_k8klUmNXPDcXonNGMAKr_pHIzWgc2ri6FzNOc_I51mNOEdXiX-9TW73mUpXFuHR0wk8zp9w6UdZogVjtdu-4pMYaghqutmfR5brXk3qmd-Zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpSdN-ywbs6ucHYxbDUrFkf1fZSFL-HjZINCXG2Yv2X1_fmKFMRnlMjGqPA6kjs5jiiwYRItIng4GhVgGoMEkX-9uxW6WKUzz8O2volEOLD4Tm92l-JgepsmliXoAMUgWDsXgpi6aeZ3mgZYll1FpzLt5nxlDKZpXttUl3yEtRzGxfWVbQSGkF6Dmz9V0SqAPlN7i5vM2ivxUczNKnp2RDXF15B_hfslTBvWbXb4x2vEt2dbiig6xiUmoLchS5celH5V6SJmzM4yiaYLd3Ksx8Fza468iWSH7cvT8A_0U4zhbKS2iTVVQL3kLASg2Ev7M67f1XIehoMbx58qW5xXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giDF2PXosgbPBMWbTptjS5RdKMtfSt4Tvt8FAq9GR_wS2MaqGIsQBT4I5gURe0mn7z_R0ZdPeV9JIdL6sjLxU5VYtRoYo5suFeUgosX0C5qxQmg4suYhZMUvtafze8Yx_V0L_08tJgfXYMGRwMmdEoYwbyt4opV0wYOUXtdXabCUUHugoDcWm8GT4Ebhtadaq6J43diV8LxxBD8RFZPa6dAFht2JDOS1H0-uKJoWKMnyCS_84baeLYlW8NsaFYJLu0Frc4Yp1LvTfJWf1w4tj8rSVokr2wuBi6Ci2vvam6oGCh0ENJxKPOBUxzwFn1mlAgd3ETqNY-vIE555SwcUJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAsWr-9MHbfPw8PkN2qu7Z-bZ7AilZOZ_FXILhpE5Utpr5RCgIB1Y1NdgI-ilbSA-QooIcRenHVK6LuTYscUyBORldhrzpYEgiW2vco74SbotmiWjprnuRipQw2_0wHjb51VAb3LpyU7HUslTcp2P808TPSTHjxfROsF7yO4_wA6km_Y0KhNERTJv1u28Tk_GUBSQvkIqzT0VFHCCGnDrfyojhuRepLV8CdSa3asMIr1A_K49x8MrJIgVPhQ0XwU8olsGNk-W4xmjTCpI5cTs3co3HD7tDpmsGfKuhiJlKTH7ESjIgTDw06PUJvDwP5b_oUJxmiqPXuCPhRZBRNoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGG_8jRWP6eYwCKdVhWhjtxxwF54dRmDMU_Ua2ys_ZLVXG-smuM4xkpCRZW8dBl0k1BaumEeYZdJkZASWoSYUAiJVNkkaBruW8I40E2V8Kj6KAwPK9WMYbe87vwET-akPJoxd8dCgny-aFnM1KQtCxB5ogeEJhpwm8j4Jw7EMS_ncHKeV2bs886BOl_vqFMF4baBZto6aSQqGTDOFDnlDSSYBr20pKQ6optVsBiaxET67UL98Zt1XBK9A9YwvXBWvL0nuQk84uk5WsEPQuw3Hw8BpiZyhIOJgTc8zZGNqAPBKv6i7St5gTYZ0VLiI_9BKAc36eiR4auqiHfK1JZxMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqM_pmHykPkQnj499Keg0r9YQt2iRmuRH8h5_6YFmiae-J3DNcTv8ayKdLzKUghe1erN5Vc4TuGXvF8AKbbZp9ADcHMHGcjWS7vvsBxzxlhK_bhSB262FDBU16UbEwrrpF4nMhm6jScMvWQvT1P1zjW33Zqy4tQMD2RwT4tsuy8U2pui1GM59NySszfXqtrnfdKMXYq0XGyCGLgvb1yfYR7G9glN-lbWE0Nv4teGz7DhIah6zfEafxupOUb3yMgdQozKA5na6_d0fjgV_GcY-Gmq0W4p42tPMCMbDxXc5SkX7ccX0X7YyFrKImpI66e11KOWWvI2ezclLlwqlssXmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhfGAFBctIuh1DCYe91_blU_RgIYGN7LWj9X2nUWR81QlhGEs9-0Ux3l01-9F2J2lLgNYJo18YJVAkr3kTe96a_uf8hnLP5--t5JC-TNmG6xvDqKqMVfi3etLMoVtVaEmzbV-DfFBc2Z54eAypC_Zx_vog3Beh4_5aZjBMEGQNK7esDDYSR42SDZ1oArmaEQE0PV8oLhPAa89r8lhKTfzyDhVQOdQjz6rZYL5zp60W_PTxXtwY8w8HFJflrhx8SshCObqJ2m7-pIcOPsGrJ8_oP6XF2IdY4k2DTdaNDOCveRzeDcLr_jd46FuV5dpmUpBBMVJXVXdhoCI_tNtZRcXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCV5KnA0Im6Jjd-n0IOOquZttcW4Lgr5yXXfJTObPacn3x5roirrfFKgG7wo1kAs2sEbTK6CA2yYP29-9AyqyB775VFtW2oC8m3BOeXNEmPpCownBIZaIzJLYzAewmy7kF-DZr6JjPXxtPkgL3FmoxVBqDhZbiOXSu3OVR9cixa8GB5ZZOlsprO4rZ6ZhXwUc9svR4HSPs6fCUHvwpGJnf5vZ3_L7WkOjxghCuAyUDJeSgGhX0OmMElcxgmudtlHRz0qPVncpFbRFlVgi_nhQdXjcdxjzUfc0x-eWUFomnEA-3jSrhLDN9Lbb1JbvUJOhSNXnKz0pOStiPs8AIHxpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdDXrHsspcGh6H9xs6CVdy3KLw1o-4k788xzaggLNwJSQ9A06X_jltHOcM5RSlGMXNaA8MpmBMDeYgLW1WfipWRYWlR5T-gDE9CvJBX-pWxWnpsQtWFffxJ-zBS8R_hZDoD9GT8F6SooY2NIJWsfGajce0s4V34AFPNmBLaxY9Ucd3kGU9gir2cjvRU4JzVkXifUSDl1iP4KIOap1q0RAh1-MYNX6dQyjiBDeIfX_Du3rAGoLXgxec1rze_DhWD-Q-7HnBzZ_1FjptT5e30epqwLVX5utsAm6yngN5VnuowQ3V2mGZDxJu57cMSbiJ691FMtuyjlWe52jLJo5vz6fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyfeSvWYOuNfL406v2iCLUeGU27v4PuhwCQ_LZWB6coXaMkob1EJkszoPEEaPPM19UFoZ5FavFzutxElUMj7W9QpryQ4fksyC1LcBsrvoRrB_eYVKWS-AGuG6T4oaydGKG6N-CKwdV7iSBOh1yAfVKwnpK2GsXeU-uQISR1YNRRnE4ytWYlScVeceN1rj-1cpRpuUuK2keaowTItusqqwsbw6xRYh_7LUh8aVP9lJOi9wq_KXxl3MBtMcCF15rEOd4d15QtaqlGD0JTxpj3De3v7cT_sWlkTL4zI1zMMxZRj_s8x7EBx9q2eEFEiqV-M7ClpVmiFiDNgHp-n2ymo3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kF3iKhYI0hB0H4GnWHKPtdWlrpySnGbbsXypD2GDxTJXNO9BoQoai8-B86lFIUlh9MYDWQNY89yHwOr9Dto0ZvVnSij-DUS8RHz1_w0ZHQ466lppJ4-GA1Cm0931m373TRlAM3iHlR8Otzt2OUDgfaYAtb-fjzbuUGaeaddDryNPDIpZi1Aba4SzOHQd6EX8EZ9nNG73X3TQBtxZauo7_afM-g0gVYcPzeVmXWG2T9BYY2Gd85JfvpHfOGmy5IqBkEJKAd9YvGs9uUy6Jm9I0gVP8sQNErOLiUYLYdKwxVh2ti2MsB5BpunsWzdQYa3nx1rTY1KYx8lp4MDJ5vg1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxJaeXw5ybYnLq-pAd-AXvADKLARCZs5L2RjcDUhVKkxQGL8p3G2rqXZscNvlSURrHIbcv2UBaAk4p4h9zPuzIPTGY6FTotmO8Qyn4vHfZ12eUk8iL8TkZJO5nJ0Mx0n48ZdmL5YBHgTveMpPL7fTT7MStFD94EuZFYEbQqgL5DN-RlN9sDUk5eXPXHXzI9cPRqJzVARTdFOlEmFAKxXKUjc0_4mSMvnMaRk0HsG8BySnXMOv89nPZwsPRClFfcww_lRTVfLRP5r223qxL4r6N9w7gTR1HKTIsLUEX7j-T3JTRR-QKJKczzbsWYafgWLvogMYehEXuJHETcSUW8cEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jXOoyx5zH4BbFTS3FqElzHobCsQDCyRjNPbMqD1-w0yrueQa67Par4lI6TABWiqZsrISEgkrQVIwDOXjJ2KH70Px8TWk78O6PYeorz-DWGNezBtjAotr_fIeoRXyCSVNd_4qepX7bbmm6xDCNdm9krdofEIPiGliTLnORuElPoLjsFUK3kHEtE6iNFqLJ69OVipNkxXzx59TmqMJVQOOXcFa8H2chbQqWOwFE3yQzqrAfrtsg4pw7i6yMlZnJyj3QptMbt01c6OA4GXsJQL4DOdvv1B8j6CAMWdxx6scKrg1N6gJf_GZjkoTBavDO6dS8mK4MOhubL5GrHoueKwWSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
