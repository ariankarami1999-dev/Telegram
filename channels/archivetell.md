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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 16:41:30</div>
<hr>

<div class="tg-post" id="msg-8097">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 858 · <a href="https://t.me/ArchiveTell/8097" target="_blank">📅 10:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8096">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/8096" target="_blank">📅 06:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8095">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پروژه زدید با آرگون ؟ بفرستین تو کامنت ها بقیه هم ببینن
❤️</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/8095" target="_blank">📅 23:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8094">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/8094" target="_blank">📅 23:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8093">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پروژه زدید با آرگون ؟ بفرستین تو کامنت ها بقیه هم ببینن
❤️</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/8093" target="_blank">📅 22:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8092">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbSCZvrm82W_LODDwdVtWUv6PkCpViZQIYhF4ifD3Qt5-SSiPD0J_8Q044JdTuYjG8baIFcMAql_F8hkkZN9JL3AdHukzFgdHZ6SaVkq36CjHj1kLelXmx_XRogJo6V-HB9gTio7gG91rg9BDrIBCW-IM-aaHxRlrbLfjmYdKrXh-F7Yvro3tqzZtne0MISGBPyOeQ4yx9NSogQbEElMUCJy8RRiXFYeEiATWUXXZKn78FUG7FwyDD2Pr5uoCEzIpQFspKvsHSf0svbh5hQIvhG5eHbQHapbCl_lLzES2DNhNAlhZfesStYcFGl1r20TLqxHxzNj7-1S6IrKXB2uYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیو هم اومد</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/8092" target="_blank">📅 20:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8087">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTbFZtK_YN2I8GJjx6g3EHZPiNxYPBG82FM9QiTZQxtSB1tRuAE4GFsxr5b-FjbQYWSMCkKHs9Dg8BSUCbB8I64e7PkBpgAn7euSErbwgH9vhT-E59Dl62rH82iAMGpa0-d7dU05VBrbO6l_SWEFzW6A0ANyYYVWfgUg2SnM7Tc0y8TG6jMMsE0DNdwadrURfmh36SPivqagfJGP0LaA45dle8AfwrXxqNWAbpI5K7cemXtbe5wA3fx0YbvKh-SRjRo-upgjkCGwlv2xA89PQT-hBAa7VzMLJjdWffUZLEUeZsT_mKd_cwFDjQiSL4TnSrcun9Mwuzn_TUUM26iJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا روی پلن اولترا منتشر شده ، معلوم نیست کی روی پلن های پرو هم منتشر شه یا اینکه اصلا منتشر میشه نسخه آرگون یا نه ...
💔
یه چند ساعت دیگه احتمالا بنچ مارک های واقعی جمنای ۴ آرگون هم در بیاد، خواهیم دید که درحد مدل های پیشتاز هستش یا خیر ...
🤝
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/8087" target="_blank">📅 19:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8086">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPfvmykAG2lbF1lhi-btkyPD7GUKkucYXWqSclEAyDQZ96099S_WhE0ztvfl_6vOVSTvZ5PJ94Z2DcOacPAnuPqV3EmutZCkceLW2-cE7maHiSx9p094j2CP06TKrdMgrpjZFk__HVf44uIfN2rkJmBCBvwI2wTb2ArNyskBHX6gn5XnCRiyTotXn3RZXcFdBAJ-x9WKpcaBbqGVoPQRVOyT_-XL99vG5wpYMu7wKTsc8X_CwPsAmtsiyKZD0HMWDs5RO_-Gc_IuL7cx3P5w5SA3hgGyZeFmDr6JIwKSamJ_mrU0v0gGgzTUTLZmnlY4LkI6ndqE_9t0BwMzPl0PPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/8086" target="_blank">📅 18:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8085">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNc9vJVGktCcwrTsIkOSWpGIeKKwQZCzFJPBdfBseX8VSDVqBCW-JR5ropO8LpWY_xgC1Yt4kXVWSsipiK3iVDo_1cZe2JLrn6kZoSugvHtzJVqCjmqU-FdlFAKmOniUC1Nfxk0WsburPPB9XSw_1edFwyUfH_kHJ8TbTjaZDde1K7jeP34Fla5Vle20hTZgF74vQJ9NPwVRS6oJ5nprSt2Ql0EyridpqeVZwPR6AZY8QPk_ujzOuWOHM9TZNdk-c6LKZgErCKruzX-7W_ZW2BavPPQlXFC1x5WV3FWiUA2uDLEjrW79UQ7T1WD88Z3EoEBJR7FIfkjJtRKYJE_skQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎖
• بعضی کاربران مدعی شدن احتمالش هست روی پلن پرو هم جمنای ۴ آرگون دردسترس قرار بگیره ! ...
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/8085" target="_blank">📅 14:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8084">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/8084" target="_blank">📅 23:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8081">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAw9Fo40WG0a8AAVjCI-BZjRDEFHolfm7w75h-IL3bzVCVpN7whT87nZNWmU3SFtGBT5a-2I2RD8V743oO1RLzkYzD_ASvvBE1lg5bXPGbQIrZjIAckzDUAHMDBcXd-ad_PZcCd8XjwN_gfH42Yj4WGPDEYBQlJmj4HA98fCbxFwC_wQ3YvQeApqw7VTypZ6PxRUtetdf6EnIFDji2bJd3as5Dv5aVk-9lNE0c27OkJCaLNZxSWNj93YNy-w3cIIDi0dMfWCaHFyUi0ebTtiSl3d2fQUU-VpbSsNoxpoMNkYt_0xodkA8GFEVzyD2TciEYjxH0fXz1yArk_LK5OZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک این مدل ها در
Artificial Analysis
منتشر شد
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/8081" target="_blank">📅 21:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8077">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPAXrR4_5M1fSE7YFykpur60FuhfOI3V2_QFC0XutNPAnqzG8M6HE7lE3TbI_OwERriwOxhSZEdq2rV6AVVaVdg1fnui4_osYskSr_aU8v_k2ZRxYqqVASX6sPd2dVhVUOumTk5Xv5YadyqEHEELjFCDCRlNLiXLTpKbPP8kaiSO3CIAU8LpLppiOQWWqQrP1Gl-zzpKUumyE56uT57jnmCc0Oybt9MT7Pcp24v8clAeIMmYHhySWFM3GHC6ZP1i2gwUiTynP4o2pHkNReohzX4WLQL-auu6NxX6zIMJBlpmHNnoHCd44vQSWVyM6o9KMF525UYIAaYrRJqoKcp8tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxxQOOlAxfi61psGN32tG2wWpQ5UzS-jJtXbZ-y9gi70OTslyD9h2WRharkg70T-sVCtvuOY0Xc3qddckunfhxIes35NvqtYl-nOZMC0Vc855cCL-GNgCWi_YEf6jOgzfCTAw7-PLdh_BOf6t7DpVyDr5lNYXJjalHJolk2-jCWOqTUROfMMufDXAS4XG61gIzBaH4v-dFIO4IFX3CbC3ah1T2_8_Zbwf6zJaOKeJPUVYLDhiUB3jZdvbgq52aQQm8haO7R5HMKYC3n4aYjyspb9_c6h6O-up6dtvwnkSiz8pVCck705DQ_KdEW_V5EuVTFJxQLtmOPjiFCvoNYwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKgtXK252bRhE9rmfdBvE3x4nOWRpKGdw_TlXsiWpCvhZshMM_TuHnl_xC2FXKTt-VnDQRzo0wB1hmQQOSeVgkGTu0G47eay7vLDv_DCWFc56TbNSnVWFI6qnsfSd4wWt7fd_M6F4mAj_Bo_tqXI-bffHpf_2Iu_S9H9aS2tIwfmUh0-BkQECp-hGWOY4fbWnpBv6rGO3_XKlldCKBvI4YzqFI4B2dLNAxnb1w9xpOibNRuxGalTv8LJ3lvD_7hKV64_p-C3ZUB6oogEzRhuK1sP0hHENgVixe2HnmuRKDwYT1J4D7N-1lw8L-EzcII5gkPbb1n1q33Sh7vz_TO3bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGlDidx9yCIZph34aPIbj5Fkj6LJJGmiIa1uocIt8JBXmSszgRXsV89m8kdYXnssXkdDqOo4ZH6V1M6WVXbsdegDxFhhVetwWgC3BkqoPY4RMVcHawMLB1-e5b8-nW3pp0wFFQQgVnaaixOYS70jId-oeO5gWCdTcuJAiDqRR_mssegGql1tAXb4ouvywQbrxTHoJ_B-j3JUXJ6OHp3KYw7sIrCwAK4mEw95JwoXQSU5xuIrN2xQORZyyFSXgm5YnuwBaVQK4pflkPg-l8rJpQaQb1B1MPA21G1OYwOhstv-YjrvJiczHkBTk8k1rQiWiMyAvVBpPS_SkAZFV1kXgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/8077" target="_blank">📅 21:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8076">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLInbInw9uiZyhp72d2C1hGGG9tK4yYhr7uph_IfZZM-jv81fuC_a2_2qtNLKfoBeo138Aolj0Drysh3SauLJsXsnbHWMEOvNJmbDVugkh2zLpSMd6DCOAhDLqYamHR1di2WLJXOMm1pGSZd1zQ1hf62FYiAO3H6oR0T8JWSsJqrloYH6Hu_gYd4Q6PvAUs3tJi9JLOhaXyXbM1pGx2BIHkzsyUtuMB61uxiJGcpBHsWo4hbzwwVDRp3kE_t9rJtOkm5vB3wYRY5VwW3kPipTox0fKgy_tHxEEixNhFpijQNe72ARSMLqdcf5CZYcaObwrcXHxQgGVbqze9rjEt8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعب
گیم های جدید
https://tehran.velestudio.com
GTA Farsi
https://gg405-golden-gate-racing.surge.sh
Driving</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/8076" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8075">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pshAgxWPygYlrAnwqja0P-G-PZlyXyq4DBXA1lFFzabR0GpjEfqs4V1W2iFQyoTLcomxqqxcEHSbyjWzbwUvDXB-f-DVrV6KcyGTzcljzjlTJNWVYS55oO7THwKB_7sPxNyruewgrLPXNVTx8d0RSOPLPfxso0V3DD2RrMKGGyTBrEz5bQ1oijNfUPAkFDxIi5oNSrQIPA2WnZck7dhvVgZexDD9ZV2vFAPg521-9hNij81ebqZXZ9lhK6Rur0ftQ6lmk6gPe9cRoum6s8BpekTIljdNp4Uyfy7WchDBG5WOLBoheYMmNCniMuZXQS273dDhy2HW32ANnw4hsuSG8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/8075" target="_blank">📅 18:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8074">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXbR5ocV-I3upaOeyRC9ZvhK0HcUeM2Ao8o0C8lbu5zA6E1jNRNT0FKwtIzzB4OnUFVF3dYO9_01uWdWEUhi8ali3J7TtK45ZU5gM_6QqE-0TP3wXyuWSMjqUQoPB6w32rHtD-w4tnZu26VyIRvug_p6g1ZpKzmwlNMLy42Ycwtu_hVWZ78ghg8MuuX0LkhcYxP2ZbSkaHIdUGo_ai1s1-oeG-KxINUWl6hDhbdNWUGH0jXg2Iqa5wU6nogpfaV301N7NWXX_ZhVNBaLam6MP9SPuYertw3MFyIGFdcXVRcrP0_rP22iiGlynghbKsPYSaD6Hy8v9yzGkb0D5SfYwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8074" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8073">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fq29-t-zs0wXwO3PVivwhIeRcsEl25u23yrTjx7CqhpBoIjzqeRk_gcEI174_5RVHWJgyEBZABJdh4rhCpPwhyJRIGSpsQ-8fHIv1NNlSeIF0DDyO6BMeNLtIv9ISNq0sLZQjUlSFjcmj0IQeB5bdCEzODTM-XVXKwjbx-fBYDqrAS7wLXubrLPZjjShlzcwJNlxve5_Q7JzHBF_i0pWfhv6MC3ENbdqjHAM1VIKFJC1aHmvcvQtEN2fwpMvIe7cgXE3lEAIhl7kWcobzAn6NA-fs2smOgzWVqj1Io3_-ZXveuHR-QCUavhcD19WCeehVvnQ2gkO71ZLgGsJWRQ3ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8073" target="_blank">📅 22:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8070">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8070" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8069">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWkbQvS-uTzNYJV7gF1jG6RdLZmIX7PsHcexxT-7XZgc9IlCP5IRoK4RIEdQHl46FImIlUuBzzNOfwUuToRyqO98ynNOmQ8H5UzPb44OGe2yMZffci27IlulkhjDxIPp9mCWnZJBSL3oQUbZ61Zo87HIN4X0Q7BvS2sUF0OdNAQTnMTdHmfX1NP3NW4jcYMMi0880BJCXLz5S__IBKkgbS3C-JrPI1-oBTVEqqH3xJECvguSO1u_qFP-jBjMHFTT9VmcqbclYZ_mPuG_AY1DbO9QqTjJ1hzrbzhRSuCVaBhXquGpDLndjwX8Xvwaw8-i6Y8OjTErNwRd8BXHErM3ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8069" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyu7qMvhoW0eFtc_IJeY2qluvxwbY9Msf9X_NC5KI_AzrgO1XflBOqvQt9-VjdhBcZAt0OR_RZmGk6XUd4KUaCDinOZZkPqUIIBngc9Bl-P_W77a-ckls4cYiWbJFCPLTJ6PO9IoN908-LMrLPoRMTlok2WEGTH1chyMERyrsqnhUwnW78U6qFRoGbuUWPRtvlgwJQ7VkPaiF9MeKn8o2WZ8v3Icjw0lky6t2t5TmOWZAMdRus1eUKZcCE7W081nMkOHd6aXe2QPx7qzU2X6IFmYUNtjrH0jTEuTTwODrJZ4TzPrd9HN2vpg9nO5NQPVY2-BB9_CKNcAb4UZEE6b_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8067">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuQaLsZCsj95WpY89B4rvVht-1-L1Sh52uBNQccIe2md1dVrGDg1Vg-F0gbjRWw3gFUOZc3avCA3yxLEyLDOqf-ed97jbA4xAJYx1ubLnmhFOvz2c7cJAgK3orjF98WWp5RgZzlp2zDGo_rmzvIKdUjxyqpjLj3nA51KItgdAidWfKBTgjN3J27Ux1UFwZfUQ6sVAqOxk8cmI3LH3_e3cL1lSS-UUKTu7fwjTPUReXoZDXM1rm9FFBxrdjyVCB_HsrD-lJGmMprzRBzOpuVB1h2mHOo8iRmPrQlunoyroD45npcTjhDkXrYUrwix7qvKmxP6wZ2B4lgnrMxV3fvwvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8066">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE2etZSrJ8i2CxiREJyF4T9KUsKEEu7AsTC5-_81abDA_URdz_ZbYSJglXLlodHn2mMVtWLN7EJsRRhkY96NV4vdh_8_CRA_Cfjdo1_a81YhZzX1sOeWvVJUIZqVQYd1Ron-haR2sLShJHJCTlht0odaFYaGGJWWvaZmRwA012PrESIoKvCmqOqn11mUGN6isbd0o5N8eI-Zgz-bPq_Kh32RmjtidttIcWOp-EpABCRcoyT7kpj0sorpO0G99gLe29b1QE_1Kau2TJCeurw-QmLWrXfhZSAWxFb0yNu28ZgA4kpRaTjpb46bXusmtFIOdQsnpQC79QPh2JqBPFk2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7a3qPV47p_yX_5I56Djf64D12LocPPLdmymwmkLw67H4TRAUy9fBr8Dr-DCvKlsQGZ8FB2GMzllpTiIFGMEJt1w_ZHoafld7DCgOp9LpG5DlrVd9tXoznOIUS3TMY0Z4q8Aru7n8TNuwRkpPLhq5vd1RY09tAJDvGJH_QkmD6WgRJ3MCKqSJLBy-yL8YI0sZSgbXocFcw8s8l7GdIxNONtswK-YG2Whi4Tmd4XrH6fUPSyCQhh3UiKUqC-g1thXnK16rtSp2qK3Llf_WZvbc8txaPZyoTNbwR8KZDOarWNN58sPKTkwkOpVhoyGXpO6R3C7H1grR8UC9WSYcXaPgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPxeC5PTD-lKCsDcrxo33JDZvhc92koxuInDiWKa-C4IACI4puIoO3cdWf1JdzIcmOn903b8eg4LSwSD-jOWmFs7U7NuR4L5KP4__eMlvBVSL-sCteXwsfYIjYRux9IQxNEg4lDQI2f6H0yVz_O-je6p5PLgpO9KFKShG6jrijaXvaQVw55ZB2KxklMCflD0MbDbS_mkSspCDlc9FRpNv2cazh-VSWpUYIuVASOa2Kz07BOjYi3X0tYockD_wY10dO03XxJ0OCyZy_MVy4niapH6FNA5pRK05ZFFi2TqZPQxdeLj64EKSTgzABuPGtHtw25wDEuVCigbQzp5l8BeaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S3eIdA6o-VTZV_ZX2QrsCd1V1tuR31iVCJ9XEEJ5FnSt-uTDdRwYFNKP6eb_23C9m0bnzCOAzGNbyjgh0L-W-GDZPlfz5ooPSer-9WClT555j5bUq6vH1f-P7UwM7MOIewruZZip5Xk_sdWqQHTMeeJNNbkHZV5UK-J0q9uWulsPxs7xMsaL_PyqugC8KLSaSKnF94sxDaSWtyI_qdEOlcOq2ZW8i5QHRaDRLuc3pP_gAmqVJten1a7pTg5PH0sJcGaJ7wnL9gHY451A3ezaTaVlMsUuAIrP6FATsZ8qVMgILbBgU6GQePIrePG9XLn0RiDccpeh5oPjKFvBpPzh-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDA4pG8oO3sKIJJqcK1tueroMCErqa8O7cq5iEjK8PN_xcWOpGLqi9bbZernmcDIrgt9Umb5YycrK0SixWa_YKehsu04imCl0b8aSqWnnxlHaYt6VcKrUWG9t732XaJ6igfN15lHCz1G1p1YSHyyB1vr8cy9GGEChjnv1nkxgGfidRsv1X2cepPZNbxOgFGQxvjO9B09iZ6xKw9uMZeI5fLo0Xt-Ee-P3bjVMtMkMWgc_gIidxUpZ76CmrsobgtM8x9Oq0SmusJ0Jzl669QazeiHXQkrQuhmwZE_uooYmxa58YGlaLx_g1cK9LSsDfUZ8WRxVJOHLlhS7Z6Naow-wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j20UfvoXXmpQTizo6DFKcEC4DKX8Fp33Szq1G_beLKJ1yWQwwpKxuEVW4HwlsaZQ828BcflOH6PzCu9bBb3sKWHcciXvdI84Vr-fPElqC94w58DCK-kUR9OjUrRMjwYLs4kgu5lbL6k0FmY8SoN2EUwYfrRX_MuFihMVos5198h-OQ-MxDQFImtJkxKvNlQeyPLN6J7CM2sUiogLWIn-pBqDPnEIlKnEizXIqpcUXoFJPwN5JRrO7r-gEvBWLAyn_mycj2JvUx_sVST5HPnsijbV_jS5C7VUpXrUAbSwxPzOPsX1ORHd822XnhkJn8pXEJloYCZI_t89ugtt0iSX5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=Q-b4q-UAeCum1qaTroym8ExK9dhlSEZaqHMgbAKSjMOk3KHlVN41YTcnmLUNrcz0y6DpBrVelTaydl5hOPlpIh6NAVuOanU4AY8P6Lv8XfIlmyyJQYxzXxCAd0vNCHqIIkgYP32OKjBOdmKd5N_cQW3VY-VqqP3hhbo5qEz5sjeGXDX-lBmlSsfj7pD6GzGN6amjAtNbvBLUuzxkJJVUnMZaobPVpOCFjNX1UFUgorV9vup7budo4qfeWVIxH9EKC2pO5PTaeOA2caZFSrZNHjiM1PkwJ_weI0rtiO52AjUZEUMMQ8Ef2a06J4aV_uq0Dfi3z8az8VfmCGYnILfRvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=Q-b4q-UAeCum1qaTroym8ExK9dhlSEZaqHMgbAKSjMOk3KHlVN41YTcnmLUNrcz0y6DpBrVelTaydl5hOPlpIh6NAVuOanU4AY8P6Lv8XfIlmyyJQYxzXxCAd0vNCHqIIkgYP32OKjBOdmKd5N_cQW3VY-VqqP3hhbo5qEz5sjeGXDX-lBmlSsfj7pD6GzGN6amjAtNbvBLUuzxkJJVUnMZaobPVpOCFjNX1UFUgorV9vup7budo4qfeWVIxH9EKC2pO5PTaeOA2caZFSrZNHjiM1PkwJ_weI0rtiO52AjUZEUMMQ8Ef2a06J4aV_uq0Dfi3z8az8VfmCGYnILfRvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gZ1fqgdsOYvCQft1hDnlC1UKHnm5Dh9dJD1ehrIHJSajX4TOoduJAFImhvUZquVRKTi5kztW7E1ZBOyfncb6iPkhCx3vI9P3P-wxZITdBEk9UE6YABTXkb3qb1S7FJDo060aYi1t-FTaXhdmbbyXCkR7JwVmn96x0lK8v0HoZM5eXtUZdCTUevdMMrv0E0yJqFTwp-c1ILRDMBK-Os-HdX5sVrcUX7GIz_30MiGyl5fhcFhfVWbl0Q5gdp9oV3BhCoQuVfsKnrhxiKBq7pgLKF-QdNY_hXjMbtzjYb4mPzNT2pRJl-r3G6Tb0LXa4Cb0DmTI1HnbVh92ORSJQOTD6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=cc2J3G68tHKsD-0wp-5Ntq-OCva3DRa0t6y6Pv-R5bUwqt3UO4iEbGJxsPFbqPFZ9gzdTixnKJr7d67fWkczsnwv6QDGAY5c65ENdf188Vdw_cPBr1gY-q34hoiHBmFRahI59c3Stciv_mIlVvxAgI7YEd5cu3GVKIvw3VZ1ipML_G2VXgC1J50NxN8J5uJw8W_5Xy1B_tt1n1Fhc9u2fV8aix8aaF6M2I-obZh6nkbVySQr9PcnlzwxBZftZSs_4DxkdU7E6DohvIssMKkOlJWB3e3MOunA7cOcZEzw3C8rV5sCHjYMEmR2JnR7SfdkCa6X6yLQ_0m95DHvpUHEOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=cc2J3G68tHKsD-0wp-5Ntq-OCva3DRa0t6y6Pv-R5bUwqt3UO4iEbGJxsPFbqPFZ9gzdTixnKJr7d67fWkczsnwv6QDGAY5c65ENdf188Vdw_cPBr1gY-q34hoiHBmFRahI59c3Stciv_mIlVvxAgI7YEd5cu3GVKIvw3VZ1ipML_G2VXgC1J50NxN8J5uJw8W_5Xy1B_tt1n1Fhc9u2fV8aix8aaF6M2I-obZh6nkbVySQr9PcnlzwxBZftZSs_4DxkdU7E6DohvIssMKkOlJWB3e3MOunA7cOcZEzw3C8rV5sCHjYMEmR2JnR7SfdkCa6X6yLQ_0m95DHvpUHEOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9MQ7qNFE-Kra385HK_fJ19_MUkJOtfBxtNEjaqiRzGsgslACzCv2BKd-frtlsQGMEF6Kv3IBYAbfiuRQ-THHjDrqZzSUVjJXMpIa4qZHkjzSm9BxTFy_11pKO8GNnTM-f-H1QT5kXS5CDSzS9oNY5wLtHkOj1ldciCwEIW1sErgI-OnzO0rTe-iaycYHUbFatFad35Nl_-XNhrg_rNz3y7WMCCPhGTw7yEK7wulu4Aodm7rNa-ZMTT3aTvIOW6z6UAsRHqnlGQsKMiZz5iUE26KwqmMA_Jd4zou-0KJatjYbu0xEI-a0EzJARtlwLN-jXIA8EbXFqidK7SNn1m86Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2X2gK2GE7mmEk8bInzwRJ8mL1yjy9Qg_ESY962I23jFeHLzOlhaGMkyXFz3EmP5D6t4WvbYpopQdZhww_AnX7OGjnKsVVCov2GJmONSkmWgZyzwfw3gu2dk6g9vPI-0aC5lmroB0X54ZXZ4mzGXJVqj8tbV_CXUKVNT0mkobx3n2Mrq4CT62BWih22rn6CgYjhV7YLvOTT4t7zNVPOyKhW9OEjsbd0vy0XmC_Gl7SLP1SMdjXB3-LwzsJq6tI1pLXQgpGeXHagILCNVbvXJtoyBMP8dm8T8PMs_tZyJwoFK1FqDi-YxEuRB5Qc96Z_dP0O2TK4jU1rhQZxpCM0MTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX-BVNFBDswj0ibx9nLZrq-4g8LyK7N-QC4xXFTZ0LSl8Nn9YZ8tLE-XrZjYoud0A1T32LFZfthLy7WwahfmgSXOCOfbxD9k4IdZz60ejOZPKsr30RRBjkklF3LgVwlZDzG1c48WHYEV_mlsil0XHaHCbPO7e43hTntsBBp4TbkHo655X8jBvOaxgysGwFkkEsElOe4t6A1VF7V084sIbLt_jFHfrn-N-MIUzsrGCnRftUW1LSZ6-Mgcwr4Z_HuyD3BkskEyRO_WXzIKgUcDHolH5s5D-JnbX3IPKW2trgMiwQkKnlS1l3bAmYrV3YLCMQuac_LnMkYrMy7kRIiX9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDSs7moriQMLbu8JGhyZR06EuxoyyXQfPkXgeSswySOarv_ndWt_NCVheqmAcTfkeujUSQxTCQIks6y27tCypaxbDovGFyNxIC31YHDckgEQdcB743uBjqNPCHzGoUIOqP7yJLkPhseM1BCzSueIErzvqqnp_-G7ipPbR_1vvB5ABgWbPON5lDWT0oD-nFHXhWqXTljI36r7nTC0G-lQ4vmQxMZWX6208oS9yT_r_4sn58qknTSpo3skawENaF59ql9SKYrZZyOfW8iLbijvWeYop5CINtpdHdtbDFAA7zbAmR3l2qwk3wAoWadg8VsUUUfFzJU3fCjbpeGzI5kjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/or3folF0wFNVKt36H_zX1ZMZuJ41_9b9o971XTF9-q3augr4nvn86kuhXw3P5ZE8BbdHmcmTPWF4PyZDYoj82BDr9KKgBeW02NKdip4wA_tr6x9bjJDnRaH2icdkj2uwXZdzfYgWGI1I5VIj7GKq93eG5f5pgF6Zn5hYp1zL1XQjWhh3dlW3-lAh0GI8zyzKXbXBqdYo7kvKlFPJmWs7OQeIekWZvu9wbcL3g52SqmQv-Cq21JYPfP-Qok6yFv3ISX2vRqYcRLsXIuY_E5IMOVMpHFLjRl3rMp04EMCO7A5MDwQDnWehadrjHDwGdM2SL2qnf6pxqYeB2Q_1QZ409Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=jVLPelBWBq3F6nbFVwq7yFkQcrpP3xJtSp9mvpwxPxGkqpHYPnCfBMhr0ZuOC49QxAlYrKl7XwD5y3xLl7Th5_77DD3wJsUrqGmrfkqqtc0zWNjjPbFPYHSRHDrXA7a2zDCKZjlYv_GO9mcF0FvZ7cucKj0UuEpbjJJUHqXh25rK7Q1PAknvJF8NMMqIFJxBOXfID_psHF30vD0rv0ecpKKsGXRsENOmIdNfoglmg6WHGnoiXanAQPJZcdgGqy4F-YLlvqm-Ynl5h5FndPSUD01Vk5VkCPOIbLnRTUB-s4J4c4yUTRJ4fsuJ9MqAu_amLxTGK7NAiR9SnZJW-OVKDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=jVLPelBWBq3F6nbFVwq7yFkQcrpP3xJtSp9mvpwxPxGkqpHYPnCfBMhr0ZuOC49QxAlYrKl7XwD5y3xLl7Th5_77DD3wJsUrqGmrfkqqtc0zWNjjPbFPYHSRHDrXA7a2zDCKZjlYv_GO9mcF0FvZ7cucKj0UuEpbjJJUHqXh25rK7Q1PAknvJF8NMMqIFJxBOXfID_psHF30vD0rv0ecpKKsGXRsENOmIdNfoglmg6WHGnoiXanAQPJZcdgGqy4F-YLlvqm-Ynl5h5FndPSUD01Vk5VkCPOIbLnRTUB-s4J4c4yUTRJ4fsuJ9MqAu_amLxTGK7NAiR9SnZJW-OVKDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoaWG7iDFSAt_p67mfXJzW52IVX6D7VsiFbQUWcZOpce45NRwMCN1qiGZzSao3MJCejriRmBQQjELR8QOsSxQM_hUrF3bGcQtB18XSX6lhkEAXcqdHrLOFTV8RPIszj7RnczHXKRB6EnTscxlg3PzCmPOzfHHtY1pMTaQ912AwnBWTs62Yjbnd0o8FbjrhZ8pfUe_jRFO78PRtX0CJrrxOxDMVrHsCTiSan5xg6p96plDeFYnQptk7AqXIKKfsTDcekA-Vomo9pKtPSN1RwR7HhYryYVmHQqw58gnGPQhoyW9C7nXjlRVFI9r608oCM1DmsU8uMQ62TcH4fsQ9wreA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iJtNPJQxIdTC_FB-8YKCNAFaYWH080plyhiHPXTGUGnmy5j0a79wS9NJVTNNRILbOJdjekCjuM49t_yTSfJuJMGbPrl55LIpjO3uEEwUp73To0NrVC7uQQ4LJBT_fGqB0uAxayxRLxlWgeSKXr7yp2fl_teJJI00S6-KQQzEEFVVPhRYFI2nK7fN37Zl-MCWeL5gUGytI8Fvn12QwovDWCEi1qPbF_wOwS1LlxTf943IGn-W8fsdnWn9j49GMZipLCBQmNF9nyUlhfrft96czWwKK-rw2aD3rYmGpJ1mnt5jJ1SG10ChDUS-Z7qU5trb4Bf7OWCikp-jw9JVh6c38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXl_0kZinwz9OliR5gjeHtehU_xG2Ky5XlGnYbd-g2etZ0v7rTo5l2Ua5zDdnKvInJVFY3l8x5XkJdEXJA7PDFlqX1IUXk4rWQpISAGxhJmyGaYs1bs8bk4mmKZlzyuBehofIh_7A_DHY57RIS-ywC1KCI_DLu1ET8LGxfjcBidSWwuxlHzJeEA-n5ndPB5qohxXPTu0N7sqxJ6K7vYGqIswA6SmGyMNFoR_jhsHnONT4lGrAT5wvjw7kThKiEFrqc0kVyfgFrbrfXpQE4WDIw3s1UeFkw8MOexGDEobhqj5gdRK_FJ_qa0gcrMXA3ffsslciBJWUGKoKjT3fPWUMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=ckfehdBiu3Jo58aY9AIzB0YIYecvaYiu4-H9UqqCOw3A5YvRqQQB8bCCXsh5QEy6uoXvhlegRVY0SvhAK0Fc6DACYufbutmIi-tUF07Mg3PlCW-JFNhDuLb7FuwwPB1zMQMbtZOxS3yrYEsQ9QHCMLqUesMylw98h_JbLZGMc8dtBFB-FaCjMdcLJsF0Drm-lmzKQ621XebT280CRtgQWEEyosPXUBOhXv5WiLWNkhx8a_sjfPshLXf9hg6u0zRtVERmT6qVstqDlNYL7ojIo7mmxy5G7BBnB6SSnEw3uF4JC1R3LlXqSE1XM1IBJf5giI--Jylp4J4sk7KUZ_jxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=ckfehdBiu3Jo58aY9AIzB0YIYecvaYiu4-H9UqqCOw3A5YvRqQQB8bCCXsh5QEy6uoXvhlegRVY0SvhAK0Fc6DACYufbutmIi-tUF07Mg3PlCW-JFNhDuLb7FuwwPB1zMQMbtZOxS3yrYEsQ9QHCMLqUesMylw98h_JbLZGMc8dtBFB-FaCjMdcLJsF0Drm-lmzKQ621XebT280CRtgQWEEyosPXUBOhXv5WiLWNkhx8a_sjfPshLXf9hg6u0zRtVERmT6qVstqDlNYL7ojIo7mmxy5G7BBnB6SSnEw3uF4JC1R3LlXqSE1XM1IBJf5giI--Jylp4J4sk7KUZ_jxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdc4jLNZknGCedEJ4z-VVLPJ4THxV9-dwt5I5HQmsIpHqYltDzaG27LR____phWuFmNmAPdw4M1ZIxOO0Ys-16NwSEQFr7wjh1xq_1UiwlqJzd4gDoFcLp340uISdmnE89xlQLeOdk-ugLrWBpQlmake47LSEEWIzuwoBrgtUbtVl0SJhLr11czb1Tvx7ugFPypfh2-MsgrDW6wNiTyT2WsVC8PsPNbTnmvLsUpXPxYwKI_8eDXVzNfEFQZX4EN8xmkJHJ5Spygkl-CR9X8ve1YE-7QCUaZPpTiO1kQ4p8asiStMG3m3hMn5EeIrT8VHvCvMIpXAAgrxnIHb9Ub_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1gu4coMTzNvw1ZG9zT4S0RWMz4A0SauRCzQsaPSVPqZWpEC8pU9dFduQV6gG4BtV7OrHMBfUGL6AkRMoj4GPGfY1RgaFN2TmZcBuFGU8UZWeIP49GchJke3j-tqZXtEkwztySeg0zupU6SfM6k-oqzKSZ7lnZlh-Sl9TRU3eCIdjQ5VAQvpjO7hO3bulQQTcgue_LwHZCfTqjZnl1tzgsPk7jJrvBvla1oGT0ezFvXtmFwXNLJMHcz4h16_i5zcACdyPf7oK-VZSPgMRDO32gcfjsjvv2EOuhmp_FBYa0rYJkHjQrOw81OW1fa_Aecvc6blRXM3JquZYWeF7R45sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ciN06498z5o3zV_CEPEz2IbnyxAt2mHWtDoeKkd_WbNN_Rr9OPDgChU2BJTTA9uGTELPI0SyhmoE8n6b6uRuJCtpzMnR-AUxH6Ogt_JNvYQIYgd3GT3m1qACGc9QXBVqet_PO9A3hRt7Vz0Kk8AmT8LGJb1hMN_jnzsXVKxahnXBPH_Vsi15rI20eBi-SLdTIA8jPigocDz_zHeyTg0C8wJ3CGb5BTNCbId2Za3Z8o44yivOAkEheT6WwAQofj4hy9yWxhFaKy6McuIWPO1Kt955elb8TdL64KyGwmqi7RfWdalLR4KWrefUYi67oCdvo-gqnmFzM-b7ENhT39cLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RD60I8J1w0U9QwAXe18-OLRZ6KizQr6g682dABxPoT_H7VX8zI_PR3mbo1yLkcq7U6i-I6AvrFS-eLBumv32s-9R17OHB_-lmt8B6pBxm6KN1f-20GDbddLyv_r7ciTL_L2aQKCkDr5GUdGzIkKqcPHhKepIDl5QK2xmRhiFfcyiwHS6s0g9yuRtOdarfkBE5_YiT2OrZFJD5Bfx2Q501VJEqvR2PJZwbKVJuBGhLckKyyG3HLJVamcHXYbSR53ePqWgSf6ur5FD6iw94E7LWHjKOlolwaP2ASbz1akrYT_H8NRHTzUixrdb5rXOBd33-UgzYDumnkWOjv9ju5WXAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gPGEoSw4SSffmNnP4nW89NTZ8shzB_pC7dMJzxjLMK8xRTps9SstN_Umyj7nVyjKT-3WC0ADkXy_QQy2Tc8qNou_KWw6aE0jpTJp7nfnJcjQrt_b1KgWWWoTUAw4S1mdE_2G-7j_qeeGqDLEHkzf0EFN65pZTpaDPdxcFpxivkdURIUe48EmFSQWgFOA0A-arTuNwDXmTcOVW_FHAQIeEl-9mf2tsNqds_X-AXzIurhV7LluUDcINJcj76_ivLyYjfscxevH66ZQyODJfFRCGKvmVJAoN0czjecEv4FgU7wFE9-Wkyqvpak-wn6e_1vdIOeodIX5DKTKcg_Z9qonEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jk5hbZsvJL1drKKdJM8P-_5SzZOI_PzkDoCvOxrc2fWD3-12V-hr3Fv6Gmg5vthIGa987neWieDCiQalJKothX_hS8ebiR2AyLhhLLjpRwU65HRt3JgJy3UcFRXwRJnkoESXZg5SmOifTdELL39pWgMo6MuamVdCSj3siP0vcMQJcBi8ogAXdNiCwWppYAC8bRxHOoGlYKBzlywiO-rKh7ATTnn46Geuvt6HQX_tXll6F0kD5uI9YepiaxyiMvK6YoDNAemQblUSL5079_cEXp-B7FTAJMBZngrbjtiN0KTz7Lk-1dBuMciqL12sUBdcVkg6h_M7eN1LYvSOV5ZFRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sm_p9AdoqDfXmX-6Upg09Ur-XeLnNQCk8A0oQyScftmVEhg_WBWmxl33bLYpX-wPgb436YxzTTMjg27lC5WCt0DKIzgBXlJJekGQjv-TPnzucUSqnEQ1nH_vWThb6eq1_OjCm6GMqnlUb5zElqCVbOFdd1VqQsvXiiUZ3Kl7szbgRhbqfUYS3XJId--kOmSCLRSXB4TqVq6aQKxpd6zn_eY2LlHVec5UsrjRz_LugOde-U4OEPAlocSnpA_fV89qPdXqP8gE8ca_ZBUcwL1D99tAOneGWcBkav9gaYK1bkOPvKR_uYEcovWSVZNWCw5QtuNIiEhhWruR3xHMiPNdpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbUPKZokSW6yQ8HhpbhIyZwxubsRg4hoOKMXNvvYqy3-07NB7Cwo-nVsK-8IxMdGtlBQ4YKGCtRRQ2xz1p6agthsaofzWtnGO7vhkvqcqQN7bMRIe9BLhCIHM3u-xRT-ORfEW1flIpGz6kqNdQnBqZAEizD0hNIWtJH6TtE_i2Hsd_z8pq2hCmgVkzpVJy_0jut9hBbvc9sUbzRl2jmQ9knwDvH74tFND3-f1F1wPeKPouXTLyP8aybB7_6nKcgPVKGarVwIRJaGikXrBMBsPFAuBZ64MFlRJkwLJqJN0VWYU7Wuqz6TnP71Pht4iAnk0RCzJ5usGONDtmnisndNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rx_4_ati2mXEjPpysxVu-w_29YJRdEianw85wQcxltKDZz-bGUQ_NQ-9xkcdbNPrMV9HjlFo31VO68ZT3xvekay8g9Aa8sEnWK2lmszKjAuliBD3_I3cSaRWN2Yg_LJLRCHLNJjG9sIw-Oq29-gvFslGXTwIZM5P0I9LqsXJs9OGXOhBq4mR8eocGZizGcGOp1q0aYg7fJLh0GdTFZE3xVVoxH06cGIEAvZah-47DKDiQcsNf_mKIGNpB08YkTRtXFBiTujc9OK6iQLa4WO4VApcafLs5IH3jGYUp-lLjkfizmqlnmm3uyIyC4bmeqBlv52DxuVoWpgPb8jYa1ukHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbRwBB3Z6byz7k-fHz8XK6jS8gNCdQjAwnrQqqWGqCvq2fhtk5k3Rh3PofCNQWbThfIcdj2bbp7sHWiTVfJLbOXs7ZAzkg7X0wKOd7v_Tsj5rENH4OIMnQ0HaMBcDBgczCsqxo4Ajtvv5unrkaRgwslW8l7HoFNpRKmCiwe3W6TkQo2rXEGYWUlZZybBbyjMMXEi9VYGy6fdF4_-vaGoQb4y2QCUCXlabdaWmJLXNQzT8pEQE63yhtUiypg1eCmpKIQBrqPerZ0QJM6JV0s7YJs_-0LduOuBuA32MPIs1a9RHNyNO3Cwli5ZtbgXRI7uSl1Cg2xjCWdvQVzCOUIitA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcpwBKSqurnHQSTdbebmerKYiu6PoSYyIlCha7IJUAIOweS6FuUuY7DbwQgVgU-o87B2_sPn56ReiOyef-Hna_M-3JnqCg5TZIZ1mTuRUrwTUOSByp4sJ6TjTt4haHdNQInVmvIsvvA6-idkK8KGjVUnM81mEoZtFzDq2GnbkA7Xv86IqAlbRV201MrYBzPLSGVM4ztTkdrf0aS_q-3_1iasfxhVIRs4ckGROc9o5JoXaDkz5MuWCqDurk4rVadFOpf5rsITd5Ho4dDN5XIvXiNhu8kPAfg7MqM7r4iRdY5tMlQds_5H7ICAjrKEUbDYf2ZDDmpoHbGLGCamim8nbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePPmP5D3GISwmB4ZFD4ryMgVcO3RvfMdXtA5_LyXw9DVsVWh92DQwSR06yFfGcVjy4I7ehyknHOChGVoed18Vv4Dw3e1CCOlHnehQNg4GAct0GcoTnOvlpAZcIGty3gKWhXuSVJghoXiSirnonXm2mTffj2oPBjcNleuNB0obJApcpfyu5CbwmPDzfELHl6DSL083kD3-DOx-aGgRuPFEry-aR7yr6DLLSvhDKiCEY4rg0Fltq48EwyS14MX3GnMGlTRRU5y8NgHLb_2VjsXrVRksfDyFSyeM3zQB4djNFjihPbHOuR7QC1zvLhZ14zHa5AuPpfF3A9GATMXRPF4Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fyhAckcFhwopKQnDTG4OPB30PNadguYJTA8x7FI7AnUqMYDwpMdWolYW0YUpEV7n_t1xe-rPSEJE_yvaSUUJ4RDKLe94hHTI_6WV113K3gNKcYwadv50miOB4AAt6MgZMLNzRgtolOBAve13WdWJ4hG4rrzoSFqMT16mcPGLl8i1xhWbsZEPFnMqPCBh5q6HaZ_NRY1CAx4yTGU8bJMo4G8rdVVw_-j2eA7Zpjnl1ny6wrcsoN4lLaWxXCs4qfiHvpT9eKOJbFF-is82RS92WDJ8t0VedZMHkXRLrpniaiHXh6X97Bkvo_VDcDAUatTYhWAOr7rn8vCI1IRd21EMIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXHxY-CPq64YqmcBgW4AnIKNWw--kutC8Jhc-sEgTg0fC0Q3BrXAJha6S-as1oUdx5LY4_--ewxJQiRDoapmI_YOlvUwtfiBDVNLHg9X4RjjKYitTLO8_g14mUSVi5n_PyUfXKehpXkSySbB3cgg43NEPkBAmkAgpcXtFIvr1Zv3ySiCr5Fn3vxoRQRueVTP61hQj304aif0jmwBAup3DkvYG9-3jaLT32ErONYhVM3aKY_Nqxyu4GVrPbA69dJikqJFbhA71T49eO53GgY4cNYVCMJSehp1UjBkR3qvt0aznJArDB9OOwKfcnJ2f-UUqpy7RAF9eL4aMEWC5-PLgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=Mhfdjc7DyNDep4sIaGmLMpRvWbRnSmmJPVbP9u4270juDtdfZQK7KtyY2CwqtyD-KQr1PVv_ogZtilZrXGVw3rFpYk08D-XIFCjmYOZ1eSfs7ivcWAm1xjSnYThumXflVLFzSuouQt64f_q_j3aAkEcY58XMPO1936oIIbbeRWEXI5lweuXxR1RCQBxE5XfP11xQei1VejjxLMk2TSFCjoMOgKXXl5U2RCzYp_ZmdzcXwlndMuZnTQrA-PO-rCu019Q7GmBEdFnN7c4YKENvIOLSDRSyp6uMNsxQ34Bs0fef-BihjGp-RNb-p0-Xp664AlqUjhTVWlRaBi_XoJauvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=Mhfdjc7DyNDep4sIaGmLMpRvWbRnSmmJPVbP9u4270juDtdfZQK7KtyY2CwqtyD-KQr1PVv_ogZtilZrXGVw3rFpYk08D-XIFCjmYOZ1eSfs7ivcWAm1xjSnYThumXflVLFzSuouQt64f_q_j3aAkEcY58XMPO1936oIIbbeRWEXI5lweuXxR1RCQBxE5XfP11xQei1VejjxLMk2TSFCjoMOgKXXl5U2RCzYp_ZmdzcXwlndMuZnTQrA-PO-rCu019Q7GmBEdFnN7c4YKENvIOLSDRSyp6uMNsxQ34Bs0fef-BihjGp-RNb-p0-Xp664AlqUjhTVWlRaBi_XoJauvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8W00EHC8VEbnJrikk1x3A2-pZKv1ADp6Z5MXvt0yje530HPGu28jBdFtneKZKwd2Hpn-7UrIJi5c0wOUFw1nYxtjGVT0oKLTxLo8B62E9leGvwWKl1w-5TnNOSIKEZGkEg4vX5xpCpIl8nAkA60fPFn5aSKFEzzPPgt7J_5izsT9S3v2HKyfZtSWEDiJNE1_MAu_Icn4k4i-mq-fb7ruABX822ufPAQEemT8db35yJNDNKPw-K0dTRGeu6_wRfdE0YAhWeZK9LYnPNavOI-6Btbo7UuQXs__meChZm5Ch5uKbSmeT_HmUwBcn5n9yzHhCfzO817ggkx81k_GNTSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lg9wLkcVWgiU4zbzko9TUnOyYNYVl86vRJXRdHsPtWxNKAr-lCmIYI8sQFsen474ezYTO4vhGdTN8K16OuxCxsE4-eJLGGegx4Ji_IVxgMmNnVy8PPmzMeo1H3nVyCq_L-eDqx3m22tFivL2HwdgNexKjrhfT7-Iegi-TXKARPTRGsoGgdFjHKoljmSV79a11kQzy_ZkQnM_VwMTTgliL34UxH-fbv73xKzP0QnweCThJZyvKGK-epbAPa0nOKHgGFli_pA8ij8ZqmDbAGF4cGNWpmbp1xp6COYrvaWgFfAcEUqbsxVVBx7I__gtX8hTFnqFdOHNWm6CsSUrikmd-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8cF5o8uLQvbSwuXG7561hTQuPA4OuSJfbshc13RDoDLElbkMGThMtHCreYDLLPM2AFQtYETngfdX_rD609nSP6vcs6Lnv_PI6XAdATXsMu_7d7qG0AF1ja-4Yeo10gw9aVSRav7ONzjROCV7OxhFGZVhm8hRMTa6YzsiX02yVGuID0jOG7fUP9m-9Yr5-oVz4eTDQgeSTf_7Zp-bg3ymEeyAbAAvRsRXA8wDTOkVyp69-kwI8q2v1-iuKR31GM2UQ9ZPX704RMvUyekHPATzZbF4Nsu_NzxUeNIBUUP8u1YBKBoAOd6sa5p2VL0ESvUal-7TCWNGemvW6EUh4ShxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXq4ig_RMvDsg8LOPGKHxHatSyqnp2X5TMISFdO8ICieXQt_C1sVxFeL__ObSWPQdjafFNzouGxuRgHjARbVO64N0anN91hPPsim8wI3YOJzPJlG0s7oSN44Z_AxJtxSpporsAy2_Vwh0HcMFw6k0QdFSpPcGwEo_iC9xQ3bZyFeRXTght-H74p48jvhWBUPYN3nj9BDvnQe8HNMGuqCWl_IO7iyMPSCMNSpBiTqLS-wXFrmli7WHdcNFqjTsYyVYIMJB2OTNGzlCQ4DfIn7rx8pfwe77-bnqVikZjOsjg1G47Jm6XciloRTC-yzrZC3JcNPerIJVZ28Ysqw1yaotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1_UJuEBmYnfkITBqg7G09zOatXYdl1Hsk2cztqWSmdutsM6AEVcjUPz9wk3lCojpxHEZX_xoBO4Qz3kOaH4dSK2K8cojTZsONfSqXQ14dw-w4EgcMl4GQSYP1tzrYAy3JoprkeBLoiL-gwGHD-9F-tICV6n_ZuMSboXt7dlVGMjRXu9p48GlvhKoXwn1NZNt2WECASiRGhjuT4Hu2RoOZSQXIPkPVdi0mYauvsWGkB0ftNF2c5E8pNJPhcJ3oIgF2rt9ClLN7iG1-0wf6TzolyVBx7yVhjMhzsY1ZzZMN7tvmw3qIsANXlOtSGMn-loGTOuRrvQrU7vVsJU78oPjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xppo3b2fDGY3NMwNAFDmCtkX_F74dCYpnZm7wCW62Jq7ASf38jvfjU6ibGSwrl4XW0rGV4xI9QKAuRX2BTaUu6dlW7kzuy1OdBJHfGAXOUKDdWRO3QQNAKUxg351VKbVIawBcPR8UIS-EtwrLNCWsuPVfhJCL2I_H45RstvfTodOMO5AY9p9X6Y7lrTGqMDx7cBQGUhRZCENsjhmMM9t11x5u2A09eqpTKu77o3Crw-qZZ5uGJG0TTON0YpXXMm-b5Hb97xKgkKntEhZnxrsJye6iQq5zipnJYuvAyMUg3omMcHQg7Np-LwRuF_-QPY8NWDcoVWf5mhcHJKDUM7siQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iColBxTbVInOOTQLff_i1Bz0AwlelAWxxENDM3MLLuEA2mY0wmGP9jzNGYvG3RyoTzU0mEbo_iG-XVKH0ypr-3iyNlDIXiBaDAmZas-3Fq2iEyIAT5dhGupNy2dDXeFN8aTKDFIroKOmgoCUx_54r2YWqz2O65D24_METAGE8pCApvwNIES7VHIvgLIsBCkdSS2LTHEd4DAS50VDaB-Vtel94c6S4HvmtudJOtCYHuvI6vR4l-dHZBBMq1prrx4r2Wj6gkT0GB1YOLU5XotZE6CkbGZp-Pybpy9pgHwYdnKm22zF0vq2xpQpJTVYjPh1lYfTRJ1KO1Vs19iYmNkLWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VFZKM8UNOl6nhQDcUO6nJoVX2fO9gquB_u2_JcrIE6MzNRkgZLmvfdBnkMlyM1S12ovrAQJ11u04brV06FwG4i3wuJF1Tuxfxm_G2VYY22sgqtYR-xbT39cfINMVQNBdTqbLJiyAGQBPRSH-mqOlhCMdZXLEiO3oMUJNbEnWk81KdiTsmSe2iddeEXo8A6dPtAseu0TvZbzdGiFGRxIK1FOx2ogurXV3meQ3i5WrQUv9-4D7bQObp1nDezXqoMkGLB5Tj9H2V3pLeYXEXnYSCi-E1-zJWC36SAFl8Lk2qRvic4_2tjTKVKVEVxL4Lm8AO8cV5Gd9LvOxgiuY1Fb2RA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wbhy6yX-ZYBNXBuYZcKjVCn7NNhapfed_ehkN5T9OUCynDcuY8kMHS66Buj9JVIXJxGDCXT-Moql2TECA-zsIzgjCnMLrsvHiEdZy5Tg5itGual4DGkDkhbZ8SoNxkPncY3JJtBmQxLWuE9X4gsYeAOEpUMqQZeAu8MnxQEx-xMrQM0fb6PQ_oGtiWX2APeMlGfXYYM4qlkuYyXtJ_k3jfUcV-A-9ZVWcKLLtdnkGZozOu7Ppe-8S0IpBCotPpGLvrbnBYCBH-Upu86zxsOR13BmiROEX363Rswa1UtFPrO1dLIzopwDH-aXoIUc3A3Co5CFDWQsudQc25inl8Et3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAVAV-TaL9mlUh5_D-OtX35JamETJGeyfacmZpzeP3O4WEb6P9YBk2iAQp_JRnNFO8wl4Pu2r6aZYnygOhH4XvAxh9-vRXjKTp0ux0SFakTM2WVuO0H_YC2U_8IUvJ-M8zIGh_T8D8bDbV-UI9TkbWGaqvd8ZsCvMG5bs-iKXpWGT6ptxCfsxpTfpCVFatC-fQDMWgZkfMoL9ntH30tCatnY6gmy4q6tfzxKdyaFo-0p4-P7zQYPYXDrW5Yam-J0BLLboxQ-qxaKNy0bRBooVO65_GwyegmsoyxoquqrIHeqoC-wQVZJ3EJBQnhY65DZ0RI4EXRAIbKTZuNoFXSepQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KI8WBObl-NZkmaIiLBSEYfGL2m5GSoYqfce7aTMmvZgqePEeiOHgDPoNT7-Rtqyp5-qU_e2yHyEsQq4vs_nnLMmH2DmCWv7k8uR2AWF8KD54ljLCJ0LMGPwDzPC-vjj3enTdcNvyGniYBBe0-KDW17AozDjK3_YIMvVhrYysm4V-fG8HS-clWk9y0rdlzE1EyXxqxDXbB7AKfELQgE1XXQtyh-BB0XpwM-dYNefzE_lKe1ec1DN6d56K5Il0klZGhcNvKOBwBE5ZpVBFK85GB3Pyy3yVhxF2B7iPQNXxEHnPG8qz5Fb0tsZMdYSFVvicPmevv-CH91e60RV7I6jBjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvlenrwHbVZ1RCWaC85kLlU57vVgf29oxKYfdTaICOLRET8RhUci4CA41BBiXmn1bfwpphy1ULfWOrT8eL53hbqUMTGhzQB-_3-m63HelUrgioqtaM3bQ5kzqx0fXIDOj--AKLkOE4dcMQqvJYxL1Iz3lbRUrK431itIfZbkUO1bMBwBp1ynBH4dnlVz_qZbYIvieb74UHyLAt-TGcyRFy80LERnXATbCkzsssiQhPKmmbkt74vAViL1vtGJNrvJZW2s8Aeo4lL2yvyKJDdq1SNmRqYJbpWW10u4olHxl1j4CAlqMCUH87LCJ2fXbi4FrPclwanExAH7SwR3qbKA7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NU5BD0ILfd8HyNAPhSItcmNd4U3OESyTmASo8bHCttNLSGmtkdoSqNALUhlKpuuTlmi0i2UoR1c-CfBESHE05vPktxfYlgYQqq33iH0MLUVpA3vRO2mKmHw-RSai-TYXWTDii38TTj7c-qlF1bHJcK7RgIY4F8Hxqug42uFN2XXaDQI_EjL5cLBvn2e-rySHZxCo088mUN4vktDlZNQ-qr9WbIik-ajkj9Pn9mj6t41AWtmKhSr8W4I9NDCXJpPEjUpSRSwY8hmSA03ppPssbk0Xb8pRz49aTYI2DpZ0dW2XPdJIRO0rtwj0c1I-4jxK-hnCgpSat0iQSfUHjWgT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b3GV7y2qTzqn9sCus1HBTlNzHARO9kW9iKP3JwE-7tf6YkllOygC9tu4hE8fhD1XqgzeShiyM8Ov42I5Zek-ceh__3-MxmjU62nUsviIu30XIhP9mL7CEckUwOwUlDEUUQipLCuHkntODv5AInp2CVq8JT7_QGYp232O062bdWgBfL40z45SwgooRLRcqjQHXJoydPSy3nImjDA09vLEIjKL65Xyz8BapeS2UL6_rtnIMS8mT_2rZF2Bgr5fryDTie8XHbrN5AZd7mB7qsdff1TJrcBLzUBPvYhibgGQNC-0Xak9hxq0tL-P6-OuEQcqIsr1tcj1UARDi6uRqJ639w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF0PgnJ0PENdy7YEs-Ud12vcn_ALwghZcLXR1GiYbv_GFp7LCAZWS8oMYqu2IasCGNEpcnJN2bir7SsBg1baW56Il8NyqWgfATn8hekH3pRdKvNwuGKiG_AV66G0QFqE20xpuKbZHB53UduBSUknypgCm6zuZq9WgUvqLEMYBDFqZ3xejyzEVnIGN0aH7nwKnCO3F5f5huKsrt05ARXbxX8K5zqpQRo-cCo4aJ_xN0Dro0ZLW0urq1cm0T8bjjlohsaIy4xYx_4s1fNHs8gfPkMr7h98xg-IhLcjqd3fL6B-ZOGhkvckEH8JKfmiu7VWbmktT1o2X6UnmK4KoBpVcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikPMY-7w60MWLmpotaYFjpjFv5_T8zWsB7gp6OaifO8twY64_tJ7R2d53qS7WSa657V7TYOwquvpx4yhVgwaF5aYtLXJPzuPGXZCesWtwojvK9h5mZhHbA43Of2DzXTcay3xdLxNUNWKFAMbTokJDX2wQpOGQh6xLQfHEEW3bO5CDk7O4Sdfvb2NGUFNXAlDdE4GlUVmRNp_2lVHWtBugdc46vP1CA46_JxTJVF4icVEBjgWMA0qOMobExJ-WXRRDmyFG7no1BG_zgVm4OSm8arYHKsnUQhu2vl6iLxeTS0C42IqTnUMXnOguJ05OzVapIDJtRzoYBXCxqZTdfuDZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_gstM6LgIRabEr2LqawwpFf_TZRHGb8CZFwuHNbTIergPO-taQNJ09SA9UHAatWhTB0PN0Bhbodk_WQigGi_cWatiBGj4E32kXHrsgXUpj_mRFH3IL1SSqabWwXzQyTCQ6ARMUHvPUHY1OF1m7EKOYL0BW4DbDOSbcPU6ujojsPMbDyb6Dwd56luZ6fAXa-b7BHZEpO6JTi0zbh5_XJFV3SrdRe1xEH78EWaSaYBx7n-4ZzfFY3z2NWRsmnUza7GBMDH1ma0BDjQ0PkErL_kBtZ80Kj6y93x0GoD1UXoCXlD6T151cCUz7yofgJiiuMBWYI1bO0F2fss7MHxjsIdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubxhL1yqsvD4RDNLQ1hnNuU6gkRbliPIG6xT0fFeCAtwTFsj-dv6y4-8qFMozmcwdEPqLymft8niQtCqo1CbB21jvUKm1Dd5UcO-x8my7SCePvZRRuakDzj9GKeriW6jcwKuaXwtVIIGlcwrYlQEh8kVPDDJYIxYn2JZm4O2o0BVfW1NktV3-JTo6HIZcfUlr4sR384mEFylWxOKOfWpCP5LA1XHJrBJUM2e4d29ep-PnusfAR2qaIsDEftAxV2DIv2vntIr6fXglmPunrIOEesSii_gdlbienxxUT3E0n2VN6-RfXleBJC4sqU5Vrm-3fL5IonGCBZBHDNbZAV-qA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnWkxXYoqKBCuMHu-Y2pMWpq3PGW9Kyh-H_XA0-i4DOLKt-eYSyH3R-motGb8Juc-TGPQO8cMqPUNflwBB3TvJRG8UXA_IrWR1L1Js_j52FDVXqiOUqJEbIdmdr-JNHPSAvlQJY3FUhlIeMt_lOv7CCbHIIsb4tsi9Z2eN8y1nij61l6GJkOTwTPYzTU4odLm_maFJbVfRIJzKPAPiTknqXJae2pqB72oPvWHkCgaiTfakPunnOoRUYxhuHUBbRqWgwCGY6qIvtu8YF75TBsUTtaqTrUeolYMPcsyPY7zM3o_GuJZoCaePmonWlpKC6HKmY7xtvLMqbniqmc9iWhAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f_6T1RWh6CA9bTqeikXG6pR1_RhJN5M6DSMwpeUzVB45XdEhRmoI7Kf9J7sXx3SXqmNELUf6dLa1GPGZJSOPt4lz4m-2nDPHNQjtBnz_KreOPC_MAKZT9_pQZzH23m751iawIhDDmAyJ-3YKDsG2CnSn5igrXOEYf2itLfOLLtTVOUrMyw9vDhi6T4UdiPp_tMKO-7CYZqTGvnTb1JQV824VSTEwpSPqgeVXB6Fw6uN3BRlR_9UBwqTdDZ5pO2KKkTCBCNB3617I6BHr3MqCxaEoohxgCvtEVwYSRvVsxsU0SldJz35b685RLrwAJCM-ygSFgNizICJOgs2acMSZhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P9HmCyMjR0PTWJGARq0mikqkOyTfZjNDAbihG5rrL5k3-otIUaNqsaLV1Vuyk7tm-R-3XrKOC6mnI2jPopu_BXEwQOji1N2pqMenMejwZ-cRCdTVlZHqYZM5rLmN5NP5PuiwgeTflksPWz9Eb4uD_GBhPPGVisHFG8WoKb_ZrGjxekUef9ECCQG_OW4DVX8dz4Mkoi4Tn4Wy1ZIcN1e0MYJfRrdnz2plSTjf3zleFG4uUFqw_guNeolHI9LHtpppWS2FLkPVl8aJl2uHpwF2Bjm4_qTk4D4qnmWLfS2u2I-s5SESFEQpPw0OSMhCw_2bKDoId5Ir09DboQGZ93gtIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Rzge-CwplXXe9W8j8I_9_3XWtKmSj1jD3d4PrXaJyke6ldR1rsyM96H_4zG_CziAdRmw2zoakS54qZWGlNsbb04dpAbF88AWr3N5LoJfuqL7Dc1WjqYlQVmivO2ziIlMBazzPmhvRB7MYhS9TSYazl-CCd2goEErsijNJ-CR7B4RXOYmKkOl3wYQxTQESkft-1RUE4t3G9v1Sc8kdeBx_WNDMSVtLOwrMACGgUEhqMbbULjm4-h6ASyHalqLPR16fI_3sRQB-x-fN0xFg_20O14iaGeUTfAmF6ode6ggVmZYckQYw7odympEO_qaJD0mS8_grTCCe_hM8-hLe4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgzmqDzit99jRSBdMsKJ6Qv9Fxx2xD2Y_aJC5w5h86wpxupFE9Z04jVXQZnpv_XTepd7GL9j1z9f_jBpBSny1b_xXlUMx79x9u4b1YmNBIrC4CIV-hcH04NaBUavkQ-ewfJ9lYAOgSHGTYxuIgGe58QWGcwcR6SZmQPDNOvqQzbQMHGHeNgufFkzRVV9lCL4svviKu1T-qcYvyF5bk5zp87cjZztHDBBpvaD7RBGUZYGEuzsaCsDfrH8wUew9QJDb5EYdshrBaMX-NlvufOXLt3IAa7Rv8yfWMUBoGV4211-fkDltK1DokmPmQB5AhRJFl5XD8ObjIydZwQDfqh8Vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktjbhRFYw-MY7npnqnXeMiXeH6zoTdjjypxJUuDEFdwRkQBkD6wpr9SDXJWereVaQx5aNupnwQG6d8iCM3I245pTDPuR3g1hR4VkqOlq4SRu7fscRe8I2H05RBIlGg9zCFrrdfyTWv9CIyvF4AKOL8rYzQbnMGxa2Yn-EX3ef4IMAVp_HkVcZs56S2sPxXt6BcZf4wHQJHUVgnd4Bt5arGniGxj3RR200Rq_J8Hdik2bWJbzLT0f25dO12mEJzrigJnM4b1TFJqg1_lTnB7VWn4U-0DSH_Ax6iKY9ddlzZRXIbv83CQNSNcQ0elnJi76yMcL82HgoltN4Rc71g3uXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjUKipYIpb1MxOIFwWoFrrSBXKNU41Yo_nR0bdUCr8bH-t64O64wNiPn-bc9DBPy6set_RtxJewvbBOrpOe-ojmsGi5bHea7-3NF7a19Pmj3KwN93QiJJFAZCw6BTRBEsBTZazGXdrAjKgoADNMarHBUmcYh8ic0jy1_CdTBxnlx7xHMXbY_rogIe7UBozQ669yg7Fzqqe-02yyEN7JRV6PkMELzq4BLSY-7r_c9aYQKcHTVXmaCQINcgNdjp_TmdNrFWzMMZ4ZbeFM1wQ5I3LTtfJzuRfve6vc7rxoCZXhgk5wwuz7T4NL0F_HU7Ih-l1KRq2Ds56XzMH3nxf6dAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxbWBWkNe32ggrKhMp-mtZMTDgRSulJn-l2JrhUYy8th72jQzCQxzL3qQMXMCxVFzVIRk4k75pQhP-Mqo09so1LA-N5D-HLVh9V-NpngIGhUOmTkQhnumPilaMCHbxLgd2HTL5KfSp_tQqMCbDrjuMvvXZsHHaiok670Tdp-iX1wgjJcI1v_C5jk2lzQqa9mwPo1KxbP9XkVS59UOzxP_n31qbPDyxQlmOb57qzxVkgCNaCD1rVtLeYH_S2niPF9W2jOq4PezseZr9rE98oyMjQx3dMN8cZMbm4IZPKoKqU0PNAg-u0ByYOheH6okSkxO58vHfr6WbrYz6fa1ttA5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU2_JtaKPjlDv4B5UToDn3eio_t1V5fc1d5pi_gcM6VUcatiw7Xit-VzZ3H2P02rn8KZixwA7i5fTswGz_cxVuSh5NlvT0FWX1C4njgmCgOTBBTvLG2l6ie7JE6wlvN8r5z1WMcWhQoklRMoMTRb39NScjobB3phfxPq1yNrfMyaMWrLg-k37yDEm9jTMxHhQVoC42kMZSytEhoJJWd7iSYt7UcS4l7AxpSN4DIkdrZ5FZqIh5yarz3KGS1V3jVnSdOUrECr9RdV3i28gQ68jiGYe8UuKopvIb3zCmc7xYyadGzH2ZY0wZiMw1dbhsTnMsLSn-dbQfrd4F0SsvD2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI2idfzLgi1e37kWC7JIpftkoCy6TZlNm3Qzi17Hp_MvZwKpOZY7TI_027_HmI3G2Mt_qyYCOd1cH13JO3XyEoAC_FyakPfuhlTH7R2gb_Djiok-ruwWXMrR64NAY8nlzDU3EGVqCrE4PVUKLyIT9D5M_StbuI-rMfuTfARZFS3SzbZdeZ3AoEb8VRDUdMSSWRAcuC02idrVgd5cVcfP-4KAOrPD6vjoKsZT77zCWz6JaSZBUAdo6heMbInr-MNFk7UTvjaIERPq7JLsXpLS0Q7X_lm4XqT7934ddrjBjQgrQnwRqtCtfmeizln0oDsB4e2IrPCtSX3m7A83hilEfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKK1i9I4DAUxLyuKIbzoXhlN4-VOSbzRRbNpW9lyP_gYxRZi990otIu57A2IXjr9L5uFuRibFRW0QQ7kWNLJJrVdnhayoCANXtREyMEcpZzUmyOjrw3RNnKDMqGQS2nN0qeybWPeIptidigIzwOvb89THDj4yq6-pLNpt81gZRyCKNJCTwOpGpVkzx7OpabGrjuxD8NEt4UrS0oeKw3YmvpEuhwGcrBs3lfcLKhCrkBfXFkI2sTsIgfX2UZMuAevjvwqKGYlzSM-rnszeQ_jIWrUXFeXxNSbudAwXXC7UAp-Pfk9CxNrvvkUG4ZVeMzaMokfuzNmQBT_dxvYRDHy1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwKzMBOpU9BYmjsQ4KsFgPnXiwODR3AKC-HRB39zJsJR03b-Db9MjGHySJCHS9hymHCccBQFYYgJRgXSuk8rlyk_dIsbbQf1d28GpsF5UOg148ZnmBT5D_MVVCm8V_8vQ2btCJ93K-YjElhBlv0UzEG5sFC3iBI5cMNA70KbubDn6ybe0ne1MtvtnAZKqgZaVPOlVzAkKhg4XXnsHkP9qaoqEKb9zzS6EwE9hQY6MKsQWlC2Ou400yNu-Xv-4oXALntpOjPaJr2rD7hoQQoBvLHWyF0wFJNf4LBS3Vd2obs-F0KSG6UXgOjeQ3rBIebGH2WHawS2_PrzzTTxoLwyiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsrPyjTMN0C7KIOxyWQGgNJp0GmQGgj8L0r76oUItiNm0iHaPnjlovKBIZ1ztMgOHy0Xh6llcOGqAkTBgPib5y_aiswl-MpzHgHW8oYgTzYyWT1zoXq-1vBVY4BFq6xJTc6ZW_JllpdfqrHkZGJe_uWCd3r2L2voN9T5hJoy2mAGTdnvxHphXc5ZQ5btF8COdtz4I8Wo128aSwYcC-rftwYK9oiMa9rI1J8r0Ji3QfiYImHvprVSRdkmFCUyumlXIjvOSw_94Rxe_o7ypPisTxYs0u40zxBQbyONRXcp6Bue0sAlMtJ5HogS_90_63CtPUS13wBmdwlfoiHUcYmtMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hl29ciX98Vc6PAy_h6Ni7CO7_aEZoEljG_fOO0HT4yXZCVtdJcsgjnFqMq41HoYZnTigvGOFlmTZLjUppjsjPMn-vHssvg-OD_lCkEOpHDb1qdnWQjlItVdnKGuHIDaR9MGJHiBN91OIRmwHsZGy6_mDea8a01gOJ95T4vLU_LaiK3xuu7lea6Eec8or7Shbu4i6ImJQbM3NVK-o_6O-XxHZTyzaKldHJpUyszSA9jk5hByUKBhJP9ErNZHj6rTbajoPoz-Yp5P5-h1D4B95B7KasLmWhf-aQG4qzYuYZzNaSh2UvPT6g0eS-I1CFPHXq8NLe_ygdqsJLHi_oBnvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNv5kTNDuGHLV-QruXUfX0FPcI3GkhCZnoeWhcnRdXcfwmWRVcBPelQZ7gMHPFsVDmIwYd2IDri7oa29DPdKvc4AnJPhWMiB08bd7PbC2BBOFDOh7N7_N94G2Nl0GkJZgDdFrS8tG-Bz5FtmH8-Jw5S0RrrUJsGZgMgEMhYKDGnQ72_No6OlI43aJwMk65DAN2WjEEcDHPqcjGfFYB9ptUf4-T8Fh2IFGxbs6iL1zEzwMavGZTYUiRbxZZ1M4BcwcpCyz34i0hE0ExThl1uejzXdI6TxuwDUNDthSB9sFnkpNAS8MJtf_AukPLrMWOx4apt-EyEFr7mhl6aj-p3ltA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iF2JkMPGnfwe8TH5CQ0y5m38xM5XKmSbtRMPyuQsgG4WBqPmslt3Cl_MWAElSJbdZ-SmKUjhhB-tdG1nbL8DcAC0iEPf4pyD2Ik6NYc_YG2W9bIRnYnmm0jXFzhOsxrt6lIrTTBac_K03pwR9TazihDM13FdDkUprsIypHm-VKFpAF8P2VJM9tpGG5I_tOVI8r-d0LZLzxnU77ndcZEMYN1LBZPzmXrd7WsCPCw_oUzOgTbqLMYdTJ8TK_T2Eo3pIAXt98tYMCE3ncpANxXksDCeI9352x0794bxdHwg8idJTxkxXjwi4dSERRbxUwgrp_753CSR4q4g0BdXOj1r_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMvBbVyOD05d0cevL2FjEY3x04NNhSdkg7lO5PkKzzaX7TjglqccZ07U4vymhMJRQtuoES2K_wEV7umh_2W1bnMn3QuWAHOoGFXNMRbyX7XqytYGtBeGUPrXresMzWF6RLPtlZ52nVj8gjUUgPiSghO3P1BMSogEOnmakL6nw_aOl1aBSq5aCbfVTbO104OVZdFtPGrRGkp329sGwdBKv6s7SNeX65AfAATwUi3ggpRM_2ivAAut2D253Do98lZyeYUPMtDiIw5X-AblmrAioCLUDgqhIOmec3crijS7ny5n8g2CLnqwWngsvNYt6metHCXBj2y2BOSTwpwp1YBRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rXDZeDn4N8e7lO7ZeBBei2mU4WHvh-BhvFV0s30iBb82__bIC5wYe4GtAkJ4d68LwRbUc6S1eHZ4BmE4dzIIAHj7VnEVx7lzWzOzpb1HJDGTUEh-A2KhsFpbmsZPsqReCXTuW-FMdOCUdFNus0XEpVtgEAELNANX2yZevrLPSKaQ-gddJm5VTc0SRB_lKnc4m1C2Fy6kYQCfmR4qcIP0yoIQaeQ6QSRPklPE3UfROai8VcFj8l3RCwUleEUGl-5qOlrGYVGQbWikUeZoBJkMcFAlONf9BDVIDEpgMxWZkNPUpkzjfAXuvH0zmj-LGnCK46jXDokrM5dzkTYO9SE_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlqcEF_tBN4ilkVLXwbT25FDcV2eG9bZUWfQvWkE3iZvinQJfxlaqVrdvU5NlVzM8Rw0MCNEeYu8tARNBrZ0gwA3-20mR18qD1eyR_twEJSbDm5RKPwhEqX4rBe6eL3QCCeSlYQiuDzzd7_B64YFZ9_zwFSL4oxaIbN35oqkUUna5I8WLyXq5Qpb1qkX6GgRRiG-HTtDPxsxmDOj23th5Ns23Mxp_nWAIVEys0726oRLJBXFAu73CtJ3xXT1f7ogzKxhW3NDSv3Wp3yr8qp0TKEst6vFMHk1EHKlPIPo27poNAKXeUw9zJ9-rLUTB2MjE4MgoRk31Tz4yJxd3J3bMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
اسکیل‌های Gemini برای همه رایگان شد
‏⠀
‏گوگل قابلیت اسکیل‌ها را که قبلاً فقط برای کاربران پولی بود برای حساب‌های رایگان هم باز کرد.
‏⠀
‏
🫧
با اسلش در کادر چت، دستورهای سفارشی‌ات را سریع صدا بزن
‏
🫧
جم‌هایی که ساخته‌ای حفظ می‌مانند و از ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند
‏
🫧
فعلاً برای حساب‌های شخصی بالای ۱۸ سال است و انتشارش تدریجی پیش می‌رود
‏⠀
‏اسکیل‌ها نسخهٔ ارتقایافتهٔ جم‌ها هستند؛ به‌جای گشتن در فهرست بلند، کافی است در کادر چت اسلش بزنی و دستور دلخواه را انتخاب کنی. گوگل می‌گوید جم‌های قدیمی‌ات هم در مهاجرت ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند.
‏انتشار هنوز برای همه کامل نشده و ممکن است دکمهٔ ساخت اسکیل را نبینی؛ چند روز دیگر دوباره سر بزن. ساخت اسکیل به حساب گوگل وصل است و حواست به داده‌هایی که وارد چت می‌کنی باشد.
‏⠀
‏برای چه کاری اولین اسکیلت را می‌سازی؟
👇
‏⠀
‏
📌
صفحهٔ ساخت اسکیل
‏
🌐
گزارش نئووین
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
