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
<img src="https://cdn4.telesco.pe/file/dI0sFeQixN0T3tl4qaWRCb-kFWlrlvgfrqGKS2j6RHshOR0xWfJ1awNhmTw_8SQ8B95usK9CQSsENZYCU-_j-jB49Qa5zZfxyFZ5uEsVoXLrsb-kREdLkxQfUclp2CmaiLuSYl8BRMWQga9VtddBP4wbQbh9d59LU1IVAkzVFTtDYZX9jx4MPfzAlzcgbN2PiGlkBBv7KoovrbsJx7ic_156_59iF2hL8_kymKXYPsjPSRvw-YMLprmGbYKNyyJUgCmLkXF9wPElYdA5D8Jva1jYodiWPF1E06u5OfjtH1GU0REWSWUeJvHxm5JML7UYulUU0_Vy-5NxsgGJeQsG6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌بازآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 11:20:30</div>
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
<div class="tg-footer">👁️ 357 · <a href="https://t.me/ArchiveTell/8097" target="_blank">📅 10:31 · 22 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 843 · <a href="https://t.me/ArchiveTell/8096" target="_blank">📅 06:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8095">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پروژه زدید با آرگون ؟ بفرستین تو کامنت ها بقیه هم ببینن
❤️</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/8095" target="_blank">📅 23:40 · 21 Mehr 1405</a></div>
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
🏷️
لینگ گیت هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/8094" target="_blank">📅 23:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8093">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پروژه زدید با آرگون ؟ بفرستین تو کامنت ها بقیه هم ببینن
❤️</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/8093" target="_blank">📅 22:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8092">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbSCZvrm82W_LODDwdVtWUv6PkCpViZQIYhF4ifD3Qt5-SSiPD0J_8Q044JdTuYjG8baIFcMAql_F8hkkZN9JL3AdHukzFgdHZ6SaVkq36CjHj1kLelXmx_XRogJo6V-HB9gTio7gG91rg9BDrIBCW-IM-aaHxRlrbLfjmYdKrXh-F7Yvro3tqzZtne0MISGBPyOeQ4yx9NSogQbEElMUCJy8RRiXFYeEiATWUXXZKn78FUG7FwyDD2Pr5uoCEzIpQFspKvsHSf0svbh5hQIvhG5eHbQHapbCl_lLzES2DNhNAlhZfesStYcFGl1r20TLqxHxzNj7-1S6IrKXB2uYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیو هم اومد</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/8092" target="_blank">📅 20:37 · 21 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/8087" target="_blank">📅 19:26 · 21 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/8086" target="_blank">📅 18:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8085">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O64ny_XRRTzS5AF0fYN9HzLQPyEN565SFRStzqfBzy56Yb09h9EmPhoGAQPPwJrYiw-1aFCJ48p85-2DT0bLXibi90yQZ_8_gPFwQY94s8zLWkLglogL5D53zVHbbyUH0ImY2aqanP0KauaVfbxG5Ts8_iIhlJjQJvsYnNYTpQ90QcsfpLCynO7mWJN2MfpN3WhpIlJtpI5aUA0q3oYOPAnE9GjmjaRLiYPh3YE0m4vi7jiT51FhYnvRruhIl5UtiRLzoODW3KGVogeeKTqGZCohVxxDcIJHHKulitofdyNx6w53L3jpWPwxZb65iqrMxTZrtG9K0nq1VkSFhuMI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎖
• بعضی کاربران مدعی شدن احتمالش هست روی پلن پرو هم جمنای ۴ آرگون دردسترس قرار بگیره ! ...
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/8085" target="_blank">📅 14:25 · 21 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/8084" target="_blank">📅 23:07 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/8081" target="_blank">📅 21:29 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/8077" target="_blank">📅 21:17 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/8076" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/8075" target="_blank">📅 18:58 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/8074" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8073" target="_blank">📅 22:50 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/8070" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8069">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAD2RpR6tEJukyw8EWCR_sVe2yLmUAkcA4MebagFauqebObRKpbsw7_uvSkI4e0ekkB6a_etG6mZvoNUIbfnZL3hsxeZaKTZz8mtn2PnSMlP7PFQ1D4DZUeDbjmhObLLm55zDFHV4wd0e64MfRWCpPgZE1wIG9_PWfZkRSoSm19mxBsvD_uTGqdQyZm7pdNI3Up8p6IHWApYRlfY5EpuPcLpyboANDZ5bCaLjVeS3FEEMoxB8CIWkibx9Ofk3biqeEOqlnEyVxg1Rxx9x9YEEEvwOtWz5xa-BuFdL0X2vSxV2LPx1TyndJAbKl38ZFULxxnZA4SksDF5FLxJkLRRVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/8069" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvpQLGVF_Pzau8x-CEWMFbdRqqXM3SyiEsQujD4wqnxw8ARuWKyGGfvDqgIFT-9fwmOrFA0qQnGVRmBokjHguUzWBuqNRe1eZ8Dv1jjCVZoEcDWFAXdtKDxVH6lVIiRkyLbZvvyK0-wgd4Kmm7dS_l3ps5G0b6PcRq-MGfRfMN-qJcAQaCxn-RwU9HD6uH-yn54NN2RXeT4nrgSv-zLPQl3iaQredYUTLyqRIecGK6k_NqGt3w8kV6ihlykW6vPVYLd-Zgf9gpmovARPqPxhztaEU2lpAg-Xw3lM0mazt-ZySufy95m5w1GYYCMg7yEzFI4N3WfMnaLkSxrxAexNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8067">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5LAptkfROvRUFlV75j7wJXyBbs6BvCbJAQI7fA9wF-o0Z6CNPkvGD_CR5wEUUlzHxIZ3xnFB824RlhuOyEMNlGVm0I0vKpRR9tmgQV76QmZUFqAw83IXZ9vRWPalmUM1GjjK_R4rSEeIf6X5DahS5s_4eKLJyWg3qfjusbnzMstS2GqKLugxfFHvsP035_R_dOyD_RBXBt8R-GzYdyR4MageQtbcZCq4WbqW-FQGc3bnRxDbSA57fVkLBToen91bG1bUV4UF4yYnSNxxlrf8_XQ-tKfy8i0vhewH7hC4GUgXURlN0lHqoNrF1r_5Iyafr59nQmElJOVwe5N5kMMgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG9ltl9gwUzvoXPWhES1vc-iIdxQLUS9C3Pyb3izP7D8ZFZMxABE7oilrzf5PeXB_B6PGgcWU0ijTgjFw7CDWteFNib34bY9Qj5COFXOzUmaqsYR_9xUmGnHRYTeh6WPmkjsnnbY3798zIkx4OVznAk1cYfDn7Hx6mfJDt3_-9NcJIMrxvZyZGvetg3X9y4QfRzax44rOYitlg_xP65PodtrNu1ByPK_jae1owobaKeseNeymM4YsluALB8lgDtaZ2D8aDypGahlGhd0NMTYpXrSdkCvai9WHw3PShfaX_VJFO65yXNk-Bu1tqkScf29J4iyiShTHaVzxYvhdQKuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KuBqmnPlW8KhCEfH6E--5VfmBcIHqeNRaoy5Fm9BlAyhSPC9NOSKRLV1ElN9tAUvoePsp51X3uyXJXgjG9iB8TKGiG01lYJ96QadedVaehrhwzcXRjqty5GI0T7_5x7tQ3hbfOOpS1S3BZWe4-V_M0Cbqz2Cm0Y2MzFuBSNVKipatyg4121lyAakny6PShtAW5kgwmoy6wQaCWN0xXmk_lEUgC7RY2iSi9rjqvziztIbWdBYEQPsoUbzpf3Fk7FoIMgFdPbcHIsGNJM6z_SRKsTvT3nqL5hV3WSnE45RpgVaHuNl0AJLX-r5C8dGonkBujXE2Zw7b1H9sX0ksiqFbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8_7Mob_Pv4dlvsUxYAiQ-SIDjeN0kznt6bLbFCPzOmUXS_EhkWJA-MnfV1aTnRmXkBZGhLwz20Zxzj4LxmcIoe32T7Kn32vtoBINqOJDMgSTmLbt4VnycIJxUzkzS6Vhfd6l775p9-h1rtseS4VlpmPIbrtJFMTLUCz0R4JHTW_iNbTj_I5W7XsNPkBIDu236gCF7ct5J4JVjFtsOXiHzQq-gGDdIBwNSoRD7xEylPnl3C9H2qoF4EE3UXNx-eMRol8QWRvKDj0r3YysEw3QpApqVYvMvJ3POXlYq-eCwN4UWNDKYbWpyToSBx6CzRJthVIEMZAeG_Tc3fEjasi3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NvxVNGFrVtzHLsvR2ojoauD4YCiWDuIUJoTI4CxBe-u-FQ1JD0Xkz2QhmDB8sYHiOKLPX6s4cLcH1-cJ54w5wrFIGz7lX_qjZHlQgAK87T9xKBkMrpN48t_IGhnRpac829ZO-ReFcEVcxEiqr0XoT7WYaFzazJ-EwvN55Kd7tFgV5ov_fsT2q-Zlut39WALiGL_OS_q8gPznna6yQMHS7VlxsMfx-NMTl4b699sTw5swLktP5uHmDzNi59MD6EHr_uckZSc30Cagz-XrUBQG7VYCuKrwWx2YsIlGq3-1WIF978c1585q1BJBbmFuiiFJPt5-gFozx24q-0Vm2_iLiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDXJzTxie6Zf4ZZGo4c6kiMp1C-nND97F5ZKr0NI4YzUSKjMSwfC43r_-ogL0NDOVUhfyV95xh-hPLr96dR5QVzWP-sizCNeegsudQvrow3cb3NaSUnuNszxfwfUMfrBNXcEaWHAn0M3XEJu5feGOWydBKqmdPAuvETyOEokdwxJbNXwRLYAAW7q1D0WV9PyKDadBI53u26W7T_J2zOV1QPyhMWleC_4dXViN0O_8C12Ccr4fhT1n_08EXb3p9tnbqKzTeRMvuR_aq5emkwCEWjRu7H31GaxKrQaMEboS9U2KyVQTLzQr3Wut0ClQzl-CESqfuo4Bpir-7n0inE5Ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a303lcLcRyiAijhK2QXPKGgQq7RiqyBlTtID60B_LxmgVGmaXyU2MEjN_AVlC2343J3EUbTA5geaAgOUvU6RcYbMWrvxorQXku_HnM_GZF-M3E-0Tm2GVz29S_yu2nDeslslbqJa6pAtVM7k7rV8qitYDxpyt5irG7hrKhmsbDqdKELvv50uTlP-j2cxed_pdhjiK5rV1OAoiwPZHeNeDz-s91vYIwypygEugVr5z8t5LX7CN-A_2oYWj1NQxF5flXa9Ph5es0J0E9UYWaUNA9CmhUUtfyxf6RWZfy14k3yTWhf2IeT0vNGtUFh-CwNkKdYTtOLozRWXKP1SDz0TqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=F9Lumh3yZ4gTir7LBgwitfgAFKhOzlOWriaD2bBY2f_Pzw5iaaeZ72fQnduUSWNVXAQMAnOXjVAUWwyjqvn8s8h3ixEoJU3oBhgLhvnRdtXmSFexY_crLwXMKxyDsyLDmSIte1_kykgOt1Prjw7THXx3Jbx6mGcFcRSGx2zZ4K_VDHJWwgKHWN3B53VNSVQ9-GIx-GjB5AqZH22Mdg6IuWFgXw2K2rFCOxxIWzamjD7Jl6OsMA8u4QaO4u6HQ9iG2Uu9yJwy3disCFP_0mCY9cGHMkXH3aDVDWl0Roo1a7o_eqAjXLB5kyKr73LLNInBcSD1dwJreDQRY_-fdiB63w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=F9Lumh3yZ4gTir7LBgwitfgAFKhOzlOWriaD2bBY2f_Pzw5iaaeZ72fQnduUSWNVXAQMAnOXjVAUWwyjqvn8s8h3ixEoJU3oBhgLhvnRdtXmSFexY_crLwXMKxyDsyLDmSIte1_kykgOt1Prjw7THXx3Jbx6mGcFcRSGx2zZ4K_VDHJWwgKHWN3B53VNSVQ9-GIx-GjB5AqZH22Mdg6IuWFgXw2K2rFCOxxIWzamjD7Jl6OsMA8u4QaO4u6HQ9iG2Uu9yJwy3disCFP_0mCY9cGHMkXH3aDVDWl0Roo1a7o_eqAjXLB5kyKr73LLNInBcSD1dwJreDQRY_-fdiB63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pjbMYpBidVA-qyVXMYuAMT-BVQH9Hlph6ctouvNM2jYHH-pN7rG5EhiYq4uGe7whIz2MAkM2_JMMuMET7UFdTHT7Vjst2B0XoiYkHv4Hta7bF_tI2hSqyvjpnsoYIPGRajrwwAZ7Lozx-FnT19PWO0VM-GJxnXEj5KH886CEXp0A7AXawhlLOAc9Wt3J3AnFzLCG8n3ZfEGMjvS2LEHMqcACNCqxP0PPjJ1WTXb2TGTQwJPGSa_Ul7dULlslVzZ-T4QEOWpeVhTpq9Hph2Is_BjI9GYnDXa7MO341dBIAiARzKcHp0zHrV-JH_2Rd7IycLcbCNhdw7pOpwJrDn0iZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=SK2hd8pZL6DwxQ3jp13f6b8opcHubzE3nFNw2fJLOkWj3H-scxSKnuUJA2alCEBGXY05UlBDDCZXKSpR692upUsSq9nOHUHx6h4amSIm6emk3tBoMygrPMg-lhIEFGXt8w6vBbjYWml4M5rnWKi0flZTr-89mN5vdYd4JKmlFfEHL4MzqV_5LZxks5t0d07YG58a3xAp_JvBK1LamDRUDP12LfuIqq8kNws8s7b060_Z0Xh369AqjyQSU1uoYAFQJ2_Z3G9eNMO6BZZGVgDnhDZDZKsgXzhmrT6v9vPb804aYs9-mqct8kxDqL7X8uz40vh9erRqEEW-Pb-FkMQUjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=SK2hd8pZL6DwxQ3jp13f6b8opcHubzE3nFNw2fJLOkWj3H-scxSKnuUJA2alCEBGXY05UlBDDCZXKSpR692upUsSq9nOHUHx6h4amSIm6emk3tBoMygrPMg-lhIEFGXt8w6vBbjYWml4M5rnWKi0flZTr-89mN5vdYd4JKmlFfEHL4MzqV_5LZxks5t0d07YG58a3xAp_JvBK1LamDRUDP12LfuIqq8kNws8s7b060_Z0Xh369AqjyQSU1uoYAFQJ2_Z3G9eNMO6BZZGVgDnhDZDZKsgXzhmrT6v9vPb804aYs9-mqct8kxDqL7X8uz40vh9erRqEEW-Pb-FkMQUjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1p47NMrEDkgLi8QSLk1WI2A9VNWlgIwIHhhOCqM9EXqKhgsVHUG853SCdFxey0gH0HNQmaUcgT21TgsRLC9lAi0pGzyf29Jv0E00u4oin0xw4QuSwQX-tLvYm_0ViBURIHFE1ctNMSVdPT5g0wOGYucqCvMv5LrbBh7SXpFRBvh_hz9BBFA7YQGQNRG_5b_sELoFFsjJ7asxOintYWHeVSRVBlxw7m3L1cd63YGdYGrssLdS8FYbwkjTivYlv2E3fAoFctkXg3xmzxjFKu7KoPFgzqxxnDGD2iGW0XC12cICBMpSdGOEc3PX28UqgqURY0UwaDM5RlmTInYpC57Tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WScCdT_uod_yOPud7bnaff6r99MWcSRhWISjY3mkQEKkIhZ_vk-KebzqIG-h-rtRkcPjxZJlIoZLvqjJKt5ginim7O2v6BplT51Q2-bzIgrHw1040FkQnZ25u3VhdZqcch5x3QffVym2eWF9iBNz90aB9sHzVMZNnKCuOOQTEL_s3xzA5u6gKWJQWpYH4Dq8T56FC9BumCKfarsCv7zxKb8sAHqvV_rlKXEFwcQwDo8jJ1OuDLMjhc5HaFKFvp9TMot9e2WTSZ563MwmKQpeDtgdCYYemlGVwliM_NzO62bEptwP0DmoIzuS8HO3-_2AU6SSAojlx6ZztI9MVcX70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7AGqMQl8bRm3p8KIPv6JKB3VeSVMxPELwc7zFWxL_XZLFgtf1Pc3KcKenCdKK8-l3NKTK17LsFLeB1n_dHQEMwIpLUS8hLbjveGwgGCfeAmK6_6ZQdakeHGt36_u9NxKZh-77CM72CHTVMO3UEUNsVqXv91zH-CNLbrSuTXsc6PlCFfwM0Qi0huCfvrMrSxuUloBPg2ngLnPOuNbXB2gZVvT52EXZPpmKoK-VZnPdAYVI89_sitELLYTCzbgwhu4CqgoaulfK7VqJeMIBJb2LzY4zqlPMYa-JGLugqKxsjISfd90t13jGEUOF-QwW366A2xvd2zG3xdDqLQmzxaFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdiz8rrsver3vWWr_4qNx0dGT2oKu6cSt7KYsYAJRRXvPNvGzbK0gHLjFW51dZVSyNhT8_nLc3d1VMpiFUZCMxs7CBO3aKWS6DFR-8_lmqvWS5_IJgb0nTMYkcbogG2dRBf_BD0JOuQ4YjzXOxNQUbhqqWYFJo_QL7MkoyQ1dv0Ju5FUg1PXy8NKGxDuIbPofM6t4M6HpMexeHTBW6jS3CQVwLtBJVbZ9PZ1aUXfBjoOC07vM_Chz26pPJ5NjeTkU3PvBreOYVcsDkqgcOThzMaDAFcMzSao1nYciHt6ojH6Pgakg-WjBiZOkwwLQVn79pjIuEXYiO1mF69vdRoNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPvcHnkhf--ypqYAOuGS1kp8QeGDe40eubDiu7E-GsKltNjKPLh-7GghpDk4cj3rLHbpiTlNaka5PILghpsI41Lc2wJlySHxt9LHWTn5fh4FmI8Dsz2Kw0sUBPIAcvpdXM3UXlkU9RqBSKnx324Qs3-B3UxsswxkmkxyXmzp3eA4HeMmPlCN0mkevAt2TmTLIuDE7YXhSrjaCUgZ9yChU3gqzh2Sv8oK9BgUbCVJ7vsdnoVM6zu00ltpoJD-eqr5VWU_Zjqxc9_htquPD-sCVg4IEWXr1fVuKy6jWCnnHB9885Czh-1ITsDFU5QKIMWQjNh35bCjBY8nvalYvbtdhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=vrvqD1PwyCxo-VGfJeY4Kx7lK_AkECsAmFTgPoFOh0LK4SRXv5Q6pc6Geebevk2qW1saXfgfLgUNMHt5clG2GGj7lVTK8tBzA9T9ShlJ83rY6Vc2DFoQRFG4Ug9ELqj1JsBzgrKWSFr2LHIiX_GtN8k9oYO9Z4zTvPjqagzPQVZ7kBBAV1rXIvamKBCCcnMrNrh8PijbZynjTfkyqn6OjPpmbcV2CrwRBqRlwVx5YAlXdOuCTYvnT6kmcRByzScCurfilsd47bSmDXNExAXzcVrvBEt4GJ9plEbFfjT3oAftucbDC_DJDUGKMafpZ3Szj5fl4l02r0yf958we_vEtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=vrvqD1PwyCxo-VGfJeY4Kx7lK_AkECsAmFTgPoFOh0LK4SRXv5Q6pc6Geebevk2qW1saXfgfLgUNMHt5clG2GGj7lVTK8tBzA9T9ShlJ83rY6Vc2DFoQRFG4Ug9ELqj1JsBzgrKWSFr2LHIiX_GtN8k9oYO9Z4zTvPjqagzPQVZ7kBBAV1rXIvamKBCCcnMrNrh8PijbZynjTfkyqn6OjPpmbcV2CrwRBqRlwVx5YAlXdOuCTYvnT6kmcRByzScCurfilsd47bSmDXNExAXzcVrvBEt4GJ9plEbFfjT3oAftucbDC_DJDUGKMafpZ3Szj5fl4l02r0yf958we_vEtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vat0SwDQT03SjIlp7TsGd5GBi6PJDtCy8QPSQ3mG8YfqzpOMHFm1dQb13lhXyt7YL69-AuSd0dzGfbkeMTlTQwnuJ5kzDQOBnxhoM2KWJFhV6Fu97oHzoaUqL2XXenyc9Wcw5d3Ltg1cUDseTwbdK4komI60LvVxCzCekDcUCmUXDqAnS3dhy7yS-IfVIuhEM9ewhHPLyYtq_2TPZZwZucrIXdt8R36VWWRk5g1BHucZ-k2eead3tDrBbqZi14PXJA2T-OrCvIJAO2oB3MJUeRyvP4YnSduPmcfuOlqE1I44YYjFTCBJK_CayTC8Kp0ZMrYxoEPbVqr0bmmWxtr0Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYqEe758n0E1KRLArdTOspL6_d_yEyl_v3jwQRKWKLShCaH6de0hfk4Ov8lGGSRMWSPs-4-9y1GaDaRYHoHjPhFYaeCFdXOR8dplgN5e6YmPE9BCB4v7bW5ZXFjc-lC1Jcd4MpLUUBHWBOmW5qPlKvP0rM7vR1WtIgWm6xoaISlweeZmQvTSN1kCf4WDeZUxM_Ax-ja5rbcojYRmsfgu7Zy-ffEM8LImyX50IbBCRSEz6XLfEebe3VjJBtkaq_gX6fvJVOUFbqPdq_YzyqVrWlRlbsF3R6HvlH0XCMJUm2NBe8JCvGql7pMXvkV6t75hWldfaQJmikpyMjMwxoe7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDkJrGNsjIH9MGQXP7YF3ADA2aN4sxU7gCyKO8pBHDWLNwOL4ngVC7diHyxdIzUzaYvWy2Nk7wv37gBV3E9OBw3m6B9GhyQ2Ol4MmQGooJ_YGUCXrDaPC3UCU1ylKYdlq77OQVyUcIqqHRJgYVtkEkWXiPQ420JaJfNAyTrYo5iWFhKhi3G5qtszlX9NgTYxLl9je-HHJrNUUMndR4YqgS1gcq4rsWc7oqMFpndcZDEISWP2RW0Qbvox0f5P2P47PFGETzyPIdK71DF6uy61KnYilkhdsSLc8ID3fFmPtTijK9iYeqh1toRhq_UMmG6YUJC2y5ssTbqnHQfb9ahyhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=g7OJy30hVZ3SPfKSrFgDdLMIOorQ7i_mygWfRpFh8q5qvyarewBEViXZRe2VWKF_9jqoH_hD5SVUcsB0297uzdDHLCEFo8J1c_gSZFzdmiHPDLfkRbKWTk1WU7WvYGtnlh3IFjSwrDemCiYOWMMNuZWFTb4Pc3rXzq_qq1b_4VLgayH8aZjgyJBEnrNBMo0XLkBatBnWeA8SSyoOgzqssGZKlkzubdmFj8UhNZWVHugfrRrVXL2KxNHGsOAcQVvnc2SXLS1Fxu7vVU1EYPrxVj4Gt_I3sbJj9bHU7uj4_F6JmxRUSmrV3mQmFzEfdVQFpAjYdM7YuzdQZTqiKDmTQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=g7OJy30hVZ3SPfKSrFgDdLMIOorQ7i_mygWfRpFh8q5qvyarewBEViXZRe2VWKF_9jqoH_hD5SVUcsB0297uzdDHLCEFo8J1c_gSZFzdmiHPDLfkRbKWTk1WU7WvYGtnlh3IFjSwrDemCiYOWMMNuZWFTb4Pc3rXzq_qq1b_4VLgayH8aZjgyJBEnrNBMo0XLkBatBnWeA8SSyoOgzqssGZKlkzubdmFj8UhNZWVHugfrRrVXL2KxNHGsOAcQVvnc2SXLS1Fxu7vVU1EYPrxVj4Gt_I3sbJj9bHU7uj4_F6JmxRUSmrV3mQmFzEfdVQFpAjYdM7YuzdQZTqiKDmTQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVRXbBe0LBfa9WP4ApXVSX0aaJGNrJ_ajSXxjH0tOwixLySC2EoOZJNLzVss2Lk-wvBXZUFjTyZUWN_jUg6j9A0vaGon2UrOUJPq--T-rhpnZAQTBi_2qxRG9UQkikrQGjDKgnkFwLiaBORkwGOYgwNyWPewPYkcLeWJQ4gS6IHpEJiBEjF8PixbXkXPKych5FTIBy4pni5Pxw2qNRKBNzL05BAJTxe4HVy58LuGfHKTYkfFHE-wlkgjTQXi_S0lE4Am3gPRazqc1EjYE8ZlU48zAQaBhGEZyc7e6PbWxuF0Zj4pXUEVhzCUMBPu9t8nO4Aczsom6UxFhc3lhm4VCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWBl_oQqL7cU7VGf65YhS0CwzlUth9TmEl9bcWNpvD2cImAHaMYjZEF3F4GMtAgCOKYKtWrmwMTgQ6PoH4-pHXWafiGeUxraARBU7vV8TvpkpXRvcj5Znszbrm_9TzDShTI0WSVcuwukBgse2sW3mk2L8ieV-pLF7rfyA5FhAzIHGj-d3WJF3nM1J8CtoeNUkh1vn82z0xEDrXnuswBjC8M-sk47k35hS-HhtQk5CiBQgSYg7CE94lxjyxF56ylfMW1Rx8f7K6WLcljGvel6rZvFYKQosiZYOoINGHYALucDIEw9vVV8mnmFj7_0nPthQjZh_eg8y3SeQ6dwH8uYjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giPga-CT1UstCsSUpeCphqgdioTRLytxhBnRRKMsnvZAmXKBuV4ZOeXN3491SzL4236-nfSTL-p4Jo6oF4r23TKikRb1dF09w_nPDuUqBSq5_YKiyeqqNzmz3Vf25ulRyD3MSQaWyZ9BDglKyrGxlV_UwsmEIjLFwYH2rnDPGd_GYL0ObSGeq4H6hSdM4Y3ZN2CCvdH-stesWIBDV4qeq28MEo_ae5Sih21pOjQVVd48AALWyel6Ccs_ZolSAJ82F9RmjDoTUJ7dC-b0mGrKmTj-zoYB_Hs9FO4eZsdulGrJ0DqsG4j4SWjqlC0Dq5mptpW-NI6zlQfx2J_AXgwf0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhM87rVkX_HldsYqS59OlREbD7fcMW0X5az3DZYhGKCFM8GpMhCqnfOvmVHplVZmWcBiumQPk_0mi7M5z5Yo9sjUwyA6R_NWiN6jeFDdV_y6R1eu0kvSq8Pzm2ZohJIu6jvuYQcOpKdRk7qNf-yTTe9jUFOoldSbytCLvIXIdGeh0iY_Piy0QJpCutpLBPSUaV5nA8sjQ8vJRSM3MAnOe3b_o4Azze3nNCxVk48SKz1h_pvXBjbSN76h8uYc09BoGbFpLefHvKb7s90wuVs3YBX95T0FBNxWtK_vG8q23V4gmMKzVZQUamM7UosEHZ1PnPMqmaWMEd6mPw_Ctgfkow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3FH6V92DIsy38PmYjRQhJGA33LGUScQdZFWc7mpY-S2lXjyB72Wk6lT15UTsvG2oOA81KRnT7JzcETNmQHln9IjSplJjyRvErp7VsmeJR5osf2C1aJDOaEzMWSD1IOFsNoLC0Q_VC4mkLe_2irETinic3QZk4I10JFBobz8wT15m5PiwRCrNINjgqgF5c4A_PD5u1WZUlShtRd8wZyhOOc4CcPEBpAJFFsRyMr4gDCm9jyWpSdNsaxesD6Udqz48TZGV8mvykCp20FJdlbW9QbTRnjcPyyAXZP3ONZJ2iaaY5PuUYV90kpeNBd9qp1oIXkAokLyT4XxIP0BX4NCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBJIPcCrdU2kCTcqh_-qq8lDf0qPwKe7aHM954j-_GJ5gGuIDi32lXCFRucpRhsLFe3V5L54T3B5RzmCttFIhp6IBhYFFtSPiNk3XrCG8aJgbGoM4Tg53WNfbFod4GWZjKssXZeKgE-RPt3TtG3t1b9fb5z6z5jZc1hDttu_WfyHJbp_Qa_AR90hWR0NjK4ZzYOrDOqQGSrW132vBzMP70n4Z4eVI8-ur87lnatrQSV6PiaguhNHipsgbwCBgoRi98wyGGNIqt-uzeOhiIJeU6_2AQucyxbdoURKNJHq23aSY34IB8vbEiS0EVYzYDOPSH0b99v32maFp72-Nsn4Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAUfXQz7RwzR9edcpWeyWrDlb88qojAb_d5hOsmWdltbCFZ6EFxsxTN0jZyS9fdVQsO1WuvQ9IYWlFdImtpcPdTmdgOoceNbnOoQikiy-hrIiivTjA81tBW6kimOfGPrm9YyMJU4tf283xEu39AVTJd71JrJdfTcktV6OcGzsbEz5QhMxrFApLXLGZ6y0vpg9UD986HRxwme7_Jn4gWdTLeNboJHd4GSYnX6v5wRtbCV3Ri7vZcVP4JV6CBQ6UMNvN3dpmQj5i-S3j4ufdhnLHBlVHw2_P7jkyKuLkI94Cx0HhouT7F4DpY3VgOJcPgcrf9bZR9U0mGMU1XZcOYoOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtzCEi7vWJOBILU_CuRYxNST4LU9ZLmlJGSvnGVyz5dBniL-k5fRZUEvNCJ_GIBZR4QiAfPZ3iZHQOI1MHGnvahvhLzbWVK4BAJHHfP7oHVcyXX4Bq19e4qqFqwnzBIm92FnZ4czcsKgAFQvfywKbaLX7xMcXUcFXvEVMD1jqXJQDm5bSm-ykOUWTPR5EHbc9HPtBAUQP8VSWt5BzcADL7VkIfoPNMjThNpgfDZxZBQ3_Ti_BikurZowxyBd3pmmhfaTn2I0qVk9lVzTQT2CvBC87fI1mKOlmcx_y4iedd12oSct9Bz0htLnovXA2gG_FaFyC_xXUaPBRyGm1ETTjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFLwhIGxP5f-5-tJjAUGn6PCTLae544VEofKARjKOz_KhL47jQ2k2cKCojmL14Ap0jjEDkhvWleXetxBfAPNhSWtTVyDp8y3rr2CsywlnHfU5IrKpNNQ7P4HiVL4Pya3BvoZZzy2XiTGkJVxi3_R4lzKecfDJ60-IBiXxwm0KF5tWN7mX9PyqKoupu7yU3Qot3G8iT7pcWyoY7cwvao434Bwa3zLDJDS3t0f3TZT0kkeDiijY9t7RQje4GcIl0Adca38gwNbQSpmZca4ip0TA3Iuq4YopPNP68x3NHiXpTXaGqrKhBVAfyEsVFSKqkFjQ1w3Xf6SsT-LXgpWvTrQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eN5kcXBZITQ4gVpg0PYMaNm28I8eRddWBFWoMwTqRcogsIMdrJFdm52Eeuj9geRa4vpNCxV0Gri-Cv3e31zc-0zVWo2VRfXrs0VBaaXYJ9zGDVruz9JIoJjKBwARwHP8lijr1X6JDwN828oBAsosukLi7Hw5lk9Opxiv_hRQTInjqK_h442I13_ofqEFKso4yob_vL7K1BAukzAJkZeCdUbnq9Ucp_OAKxXKhWx5UFTab33hu5y2NHPizp3gJUVob1qebzuEcz31HGPOTZQqXzK9_E-ocsFx_py9-AEuMF0bWVFpsQ0VXNr1ZBmZ0sTHgqBk8N8v0c2edRne33gEfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-mEnrDf5SxkbNP_GNxNToMboNWKnRU7f6-JG_kiObaTOIVP1WvStfiOpmaf5o8hl8gQU5MIYOd2UIIq8A77sEU9GfCcUf8MWPfRr7y74cwWBygtW3KYw3bqcwQAxch7sVEqe05faRngrFyOpeiX4rBHyQE-UFc8yd6xChNH4yF9MNOA4dBexOPv9LCeB9QwOevVVet5FPy5qTHWmQDWEt5FrDp3Ixh9EWfyqXtrM5oULyb1EPs_flVmjc-pjyiCWJWiQkk6RppF0UcPPj0QbrkDaEaJkuE9tyfwepoyxHz5BTs3imgdEVGcaEx4qgbX6ryGjHikNI9l7zbEJ2ujVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJqVOnoUkljG57K98F7z60vGYdJ_jiccmFpKR0vhxuyspeARDBMXfZzbfbhpzxwwSk8M7zYd9-PBlmGxRFZBuE92FKP-ZXK_eCFvSMHpnRZQ8VROomKSuwqiBKxpto28yeS-BZQFUdFX3V6dFHDRxT7MWO7i6EAfp0-l9eAXPqsE0CbZvBh-INZbQgLrKDOt9nwzoGVzhDfWV_dRsc-5GxFd339SsH1tT8Z0cTiclRqj78MWh8PSNOynqZvjwtjlhcy7n9q1BSOg8XtqqH91zW-5VDaMrWZAPyiUDVhnwbYWQYCcH4Qmdm_ysWUxMnZkqL-tq1h13ZFtnlJvXNZ3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Afa8cgA3hwb0OibnLgRuoa81I6JE93V1-PVF8QWds1NiT2QKA-_2eaVnI3tgcC-u1kdv4MIHB4BchqFyN5T0sb4BZe_E95nQn1Fb4VBgGOCfKFHZemPavCLZDaIumkh9zURJarANcsytvqdcczL9erowse98vFUHbCRUU8hSvNOAYe0GP4HyS93Eoj_hGI6FXd0_kie1DoZZ2uDjxEbuAs1or2xnKpMC_5U4MpK2G_7bhEeLhFrlT54KpiPOd0yd-y09Axg6NUdf9hB8DEOekCOWFJ3CACQkefF1Dl-Qb_upwnpIpgO0RfoECSW-tE9aAJ62ZkUKvRAS1Rp1EmFWRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVU4haRywq8xQPHPMfuquTJCHThMkDQDJSZ6g_Kl9HTuTaibjwl3b66U437LpOb9TsGe_GN7FpZfyr-7ZAPPjuTzSzMDPdCpu5OIln1cMfHs3nVaeBGossd-KLNwnpqnUjLqxTO7UxWOyiz2pTcbtmNL2tLCebTVqH2dXoKMjsombEGf3Kv1GKOe3esRwTH-5MteNRztpMFmGniV-QPkRAe-oWT1iu8U_iw4vZtfRrHRIFsBfqB-NNm5AVB6X2QPhPhGN0W8ERyol0oZkzVkheo5lRaWGZy6JzgmqMDK-0gyk9g4lMCEtxvr7ocVHjcNxV3MfWfxrsHbY3hbSvDHfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=LXmc0Zu3GfqVTeGr1xQI5jHpJTlgIjo36Y3GRQznI36D2Fz9sexZpGiPaPTQ-lTZt5-acnuTPjntznTY3COZ5iBb8rtozi-xKaj9UWEwG6kORbXjmrJPMRdJU4VxAqYiMK7W4SElB8_bYlTZGbr37b7v3TWhnjWqK6cSxGhnEeqhG1Bzd0oarQaHfubnIkmyIPeYhPbzPV-ywsK2FR_NSW6Ab0ynGO2RqJ5hUx7nP_k-g2WOLODXlpcpm_XgnwSvJ7pFLRjgHdKqN14XaOpIXGNYtjozo7Yfj4PIP6ZIG_snSQX49R2Sr-ddxqTtVYEPyppc67JniqMCaZYuLfJDGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=LXmc0Zu3GfqVTeGr1xQI5jHpJTlgIjo36Y3GRQznI36D2Fz9sexZpGiPaPTQ-lTZt5-acnuTPjntznTY3COZ5iBb8rtozi-xKaj9UWEwG6kORbXjmrJPMRdJU4VxAqYiMK7W4SElB8_bYlTZGbr37b7v3TWhnjWqK6cSxGhnEeqhG1Bzd0oarQaHfubnIkmyIPeYhPbzPV-ywsK2FR_NSW6Ab0ynGO2RqJ5hUx7nP_k-g2WOLODXlpcpm_XgnwSvJ7pFLRjgHdKqN14XaOpIXGNYtjozo7Yfj4PIP6ZIG_snSQX49R2Sr-ddxqTtVYEPyppc67JniqMCaZYuLfJDGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDFCke64Emtt9Fiboo37-bmPghDK-wTO8PJFxsmNYBBDwuXkkLgIucT_39NXVoa2hsqMU05oOmLC7IAGyl-B-XIpQKdYskYTvFALh5HDkjgOm5SV6HIAh1Repc79dIM9yvGe1aZuu9My5P_Aof_h3skP7gPWEukWvDUYj2D0TTmWAPc2TqdzE_my6PAbVGuycZ0nN6KC-IH5quFUschyXWrcMW6zBDZGZMgZMjSsXSv85q701omsazQeH5cZEOzsGzJCxUl2pqVkH2PbxM_1d9dJg0C7UjQ6fysHlV626yqazDgsRLGazjDjsmRX-mlvaiCJ0f81Xegm89Ne3c8Ndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NUE1JPjYt3ZsjImCkOMoWXo6h8-C0EDphBkulZgeeNPRUPBY7cTjorXzw9Bn0hrxbmKWAoXimfm0tjEjii14pI319rgLIjB_NFyPMwABtPZ3NhJC48qPydrToOjyFUhAPltQAa9r_O1OSNALVXsNywFE4-yPtsg2A1eoOUwO_tJ3bV2qByAT2WfyRqKYUw1sT8p1MOeHGjhrMX_hAaYXSUKlDmQHhJ9QOVQ9zIMrjcdvpBwgMFizBrv4FI9uWGNJuDbtx4tpal0WN85ccd1k8Ia5cznASu3Yl1E6qK0ltupsve8rULrvPVfhxRVaTPTJYGBVif2bJ6coGdEk2N0GhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6cOroConFXTSuwcooHJAOKrxL9SgDVHU0zh5xmDD9ww4aBOriieAyAv1JkT-dTMG9i0Akg8ozsGkjwM1S1cX6i7vlLfJnmWMHbiVm20qfT356JDfeRh0fIy8opFmi-2cpNL9uC5fzIFFjRrPvi3JIt9AR5zfpwhjeHvGA3QIJ-frMN6kXGKmLoC0oX7zv_3t726VIpdDG-LBlVnXqXVweWKRs5N1I5xyTuvV-NK2RLlHjfHvQmkAerFgXdJVyuTqI-KEtDoZj3KzSoyR4asP_OZorKIbL8qDppqN_pDQgWx4ihK52XKbiBCnpb73VEw0zeD0oEEp0Ca4Itv0fAi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNhvKt2vYLFCDBogkN62EMSGTqDgO-vlNZ86GY9eljyuDhwRKekXI3xb41HssoYhIz75wHpSMWziUJEuaQopp-Q6WFEXrw-xYn6OIQ4kazLzSr4dlJfm6LnDbHrGsSJPveWBqEst7pQ3ee_ZYFS73rnOyeplJAgC0dq7XfN_RFkRnPOobTdF8gONWVYNA-NAjKnwzhSmY5htsrNqbKZ8FNeS65Sbu026lHum7FwSpxMLQAqzmv_L4WSxaamAPnkkpV9DFUuZGfN4vq9LlmuFrR2G2-czfcuYzLw1gRZmh0R6JjlQTvVTUUGpvh0k0DmBdYMR9tzVqN-VQu1oJigtUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diu0i9a1Uvd39y_jmztxWdHMC7dSLwc4LGkHGz2gM2xNjCjnmPa7Bz-5QmsgK3o-7YuWgfhI5GY3XRMv7m_gQka5_SxnCETffHItwMkTSACegYNsZF20HGziSz6eGriKgdAlzyY1FiAj5IJFSipH_KcMyQgJmiKkXmQMUdvS31Z8kw9SRhOeVTPJ4iPaFT980QRDUn8D-OzT604KDe3cAyK3ew3H1LfFSLEp_IuHhbgjU7Qixtqy204Z3fg3Y5-fy2iOCaItIM1nUgUJ-J_H_69n21xFK7aof5t_t2rSKlRvVYko8yEMtgA1f8W2OFNeuXz77wQNym9OyBVpXD0Uew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj5dkUGiUz938hsVn0AVE1NkPel8C3FQ6Uxyn54g1d7c0-hviOwd9kUWVIfpnQKRX0lgUhUlybcAiOrAEooHV45MkNAZ4NJuEABzw46mxl4i_lErPQsaEPFceJp1gq0vscRdeXUD-TqiPGhMcsTKUa8n8hIT31RkR5l68JiCUGnb_m7ht28iNyN1r3kk_kY0IC7hsafcPMgPksMM8l4jsW7vEtC4BSMz4QYDKqtueJkDhlMJrAouo8u7uE0ssi5JJ9_Jn4Jd1qMvRAIxDsuAUTKlvzwcMRnB4cQ3cqXpqvkM_7X_CeC-g5Xax4TyqLNpJsoA6JWyvZBWaLDv1MHs3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vyBz_3kSu7-Vt2SR8idf4HpjNqckTRtTPShUe2KQzMOzgxvkq1NhEbUAlWjgP2DVNeJXZ96xZUUD74mU6AQjLVOfhDbhp2Gj8Z-uU3H4nQqU9QWAOA6EzI2nOoR6tPzyviTmb0ujaYw-MY2lasV96hcfVIDmuVLjQxfw3OildgZMtO-2iZN_SdAMBMm5TLsGT7iB2UqrCq61Oy-2LaeB0EUW2Tu6A0L6zyynRP78OipKL0HoZdUY56xyYeu-WkQ34oVQe8ZYtOZhg9jSVpqWE0An-LsDmxEd0lJR4mguxyEqEbd3vnZxInq9jsXfjyU2UZjxgptrFS1ZbOT5Zz1neQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rGtv0lJ4NzqgW3uxzUs1vJFZZyaJY6CoR0eLyh3ODJzHujFekngwBvbfSMIctjxFNzYSamaIuIucPjMphR5JmjfMs4L2QRv1B6LRrXYjYV6_p-PO5-0b_hcyUirZzVkcl-EgI3KOrZlkuy1mzOa9OPf1nztYb3IxZMEO4iPTr-49VlFKclns-tp2MQ_7E5rtgVUaKDPKuZncgD-fOfKnMFGy6Xq-areV6ML0N1nmiXzgJyGXNdfr6UzZAPl8G36XfJzcvtcm7LBX1MuyH96m4z4yltqbtkRoTYl-0IVsJyKdmjw8K3L1Inef6RCyCOR3r9u1kzR-ompB2QtUy0h4aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oV4xjLe0IRGYndmn5pTh66TZq8B49_3i-2wlHqQMO5F2V8ldSMCOxdmFe_A-JwO3vJ_Ms_bxnH4pkhNlrD0FIgpimtA5FVaLDR2K3-cNitoIzmH_gSyuQ9HAm0NEv1eJz2e9ldssoChoqnQxpHQV1rYwEGz8ekG4i5aDSwscd0bVeAtNjHXZyYKKvVaIK6TVV8WxMDLHK8P9ywn3LnSUUsP3T9Ff-58Th63Ff6dqfWZPa-GxI5auR1zRRjWrjXpuzc-iJ4EvxTHY9UyBsJ5PsOo9UTNeAp-vmLzbC3hN52YQSYKpZnPk899fdUNI5waPUmVr4j59CnABKzYrzXg5BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPGcZgVFMfj6PmwKO3EnS-FvtTw9ADy6j3fQg4UO9kMAKJBUQs5ITU0EPMC1QuoVgcKqwqQ43A8CBQVtpRiQStVVtjOuqQ0Y-zq7uIay_glocJhDOs_942Q1cinIjZT2O_UXDDoz9XQIr2AVL5lhyDqEpzpw73y_n-KI3-MC1QNXOkRr9p3bxeABVl4rV0OCp_twUy68Emf4N-QxTF82IVSiv0gEQm_xiPTS1fW-lx1x6eiPlYWJ0L4Qdy5qpThU0l2u3TpoHHa74RWxhAGJfLE8M8f6jRbgtGGAojm6FLtkskdxIhH3yX9QCrV9USxwZ356O7MVAnkT5gVB0Vkkhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf6AKHY1Lb33JOvcm3qNh7nanaRJg5ihaioOTSzukvix35Qg1HkefxCUIcmMVzcp_nOx0yZUegy_JDXdOJb1m-iD53BbK67NFN5pCqsm5rGYhNKx6Vl5RE791_BF3Z-iSjn6TErganu1mFLTBTBY0d9K7oEFgP76Zegpsfg1u6sQeLFUzSgzY-72rH8mpAMmO2Sz9dmz_LJL5J3juxuZHn7f02PM83Bs2mJ_upJCoti3wNxiECTa6cUkIMZqc1SwUU36MwfqEPG-rL4APq9LGAef9vukVD8Pj3FQRGx3MCQ9yoR18H1VCSYoghc7_6MA4xGwXQzYMvYldI1NzD7woA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQhgDKyNnbnt13ySWXEQRDz6Oh6xP9z7ZOxM9Pa7sGX2VUOKLpBN9-FMTNvxhFsEY_YpO3Plz6_rFMImuzZUXNmis0gt82XlljK462eTiNSOrBuxCyFDC0ZUe0ancA5UR3WMSORp-hRsRdDLhrj0yaGNYvHsjtq_Xr7cDAyRKZ9VIhQO0RTjyWq6iVKNdQorTMCAC4RP7SZ2rTGy0fDEpGjsk8fg5Fd1xng3xgbmhuMrQJOUhA8gZ6h7Q6_7UpR82xRDyTxlTDDpvebjPEI5Bt2LXLeYbL8pXPuIrRI7K_a_12RSmd1LldVZe-Yc5UCqraULlDtDIen6JxULIS7tow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZOkrNaWoFOQdWXCw8ojIe_erNW7ZuqySbtQ9ALA82XbOxs-pQov04uxK9iUv8MFkl-5HJn8FwfspI2hvzmbcpW2oTDn1ZMxTG6uRaAH8IpGZSPY8gJya1RSX1xML-845AXJDHD7SCI4DNNhP9CLyAyIjMCTUjONmSYoj76zRH6PU6GWEGCW5GxT0VWDIvnKw4bNzTCTxr0FNOm2Ktxswu3tF9StXC8_1rI5Nedo2HZcQ0v842hzMftuRDJoVyCO61v2LFpM6hjm4qzglTiApt16-Opmi6vbBiU4qwQDkVHjjPhf_LwU0Vj5A6CfMXxnWOEY-eNW18pGOeFudtHDEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vDmaj_oKeTx9ZcLgBTpWcXcQQWg1DFq92CPYVyGdbqhVGjo5HUVTEbltvR0WB1sWqzMKUB5yTsUUL2F3hdCxY_bsjBFLUZnkOpc07Q8LmYdkuVEMIP4BHR6Us7jiJ3nUmbagk5kkubVM6D6rNnbwZUGiJYlT-vF2XV-C090knvfj5xd32GzMNDVHlHF8tVjH6Vgy5DGBH6DhsdObzbSh34FpNn-bsW07vJHmudTUjx5318E7YL4QKkMr35HA1MVjLub7SwXCfz2GVxnW6JUCMm5py2X_ttk3OhG7XDaJZWJQLbuFXollDbPWU_fBAID1Hglq-SGl9-9b-6GZKUrGug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C207Zwq0qzCRvdN3UaEsvVqSy0hyMkDaZ_P7LHqtBeQx9IiJdR_Azbovm4lUfe5ZSoZ-LiCXKgay-OGxuJz32TYZKkLkdaIzpg8OiIO00a4Hlmg8m1WLNmU01JyWWG7Ml117ZV2pzYCuRfu1kn26Aitp5faENOnNzjMFOzFuxOYcsiRcfNVI52ZGqE4Q8dhS1cgwtZuX00SfbVPshiMU-1zJyj44NPTM3b7o26Hhmbfddk4dywPpcpiYdflP9UZ7Q-rdOIwbLtJHfKakfmIZ8satNO8QyTfMVPxczppks9zsnRIze7aobBCzRA9aeAkH3xmUwflZ0zDK7bTQB5dNqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S29SXMI8Nk-sXikoLvaoAj7hNwIZAlSgL5oIxwyt1t4TqH0nsLsx_0gVRUlO7Ucm_XI37u-mthCRcdgN3cdXSM-9x4FzQACwicJs-FKTz1oXk1LSMiU_IjbAE18X_0fiTlcQ9kBAyzHOfZCalOZr_jICv8noJnOrD-sqxwUQg69haEJbkSmpCFOQYpIUYX3J5lcb9vK3RGvPIwOBCOQvHZUSPuO0uNLN8aH8zLb7KjR-Gxw4dPb2uvdvtDM9NfidGsWbEG7rviu1L2jQ5H5QO2QXPj9b-FH57igeD9NTa_LARkZvZl6LNp7K9lB7gQmfuVWRi34lzirN1wc5S66ASw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS5qmjv9Bc3c1456fEhMWwBsy18E852Uv34OlRa1rrkxHhVhWzlfVTvSWBt5TyxgmEs_dVxoMZkoxjCQ3xYEpKkPaP80eGSwfxEc_d4XL4M41iLe8d6XMLlQ7BPvr_N8lz-6ekwXDxQ31I-qpmViPeElbs4LbNOV07-x_XutElvPNSb1yjc9-hXS-7Q1E6w4_Sb-PpUmm0dvp74xQ4HSTP8RaR948Oda1EwL-8Fa__BuPUJ1O7bXy0YWKrKcSqHhFd25ewnFhx2E9yM-EnchEU_W8oQQzkXhkbf0IWxbrDtVEKk-GoWSWVo7iKRZQQ8K2JxjfoNeGI0_K9D3OpETOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve5LJlVNP5ajnkQ3jCdZlVXSlC7NTg8JP4O5g3EdqWo8ccIVTioNc55eD-hncoDSo-aGo2mLMRM7Q6KQ1D52JjDDLAD2tzZvp7YrF4AOjL3iUFSxz86sGC7bHPMOxH2D-M2Bk5jbTqaG4WIkQ7xpAikmdeB33g77me5ds8OZ-FqEWrslf3j-vqY2tKqZdEpwudU_qM3KH_Ud_rgD5ZDSiP85jcOipNtUYYRPcwHMej4_gx_SvwBNOccbpkPHKw1kpCmhJAR6dAZt2ALCqYrqkf6g1iB5ZUxHLMaHIldoB_yBxfXP6pcHBmzl64NrxHL_d-0hZVZopb-0D_n-4ad6vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ync-5jYAehX28TaXDQahnuiPmCr7Jw_FuRBLzNMIboWmWc2VIAE53lGKBWkg_ZGce4i-kNfzhzTEoe0aU5va98PMO-DRbcUNCs28vZb6z7OjPTjVb2ffyxSSq-CBH_sqZP5H_c_sZPmKHRmfNGQyYt35zJOtiZRCALf0EC5GCu8geVjTvGKQCLsROf6cRyc8x7i73hMvSjwFFVjj8y8JI_-8JMJ9ruDqFfmhy-fMfpScH0nB_vzbhJqvBZNTDDgsInGdHoJMgDAkor1PEnnK4iiBjeGfJ7CB6Did-9AKmKyXRqKRJw2-4Pzt_xRA2I-8oMlFX4cwKFzpStzQmPqB-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iAYfPqKxhNYPoVOUuOFO1J5tx0RJL_OmcdZddEFrpXJECIfC4QJAREO_7hngktuQQ2jeH1BLOjDuzlJqWzGZAb_n-AzudQFgR2m8zT4Dyga7Nwe6cPQKS5FATA5aDpPmun8wNnOVerkicZUNCDP9mUWI4WKdVo7Kf811S706x1SEvaDeQVViyjHUnD-mT0xy2V22N7wvmk9nrU_vgFe9bZq6Ak15mkWvEqkd75rkjU1iJ_A9rB8lY2-nDQ6DzIWUtICqupwTtwTlEFjklLXgnvXrDhVe09jRVPHoz2t63LydqopX6vluxrZ-j-85Qu9r9tISU8W5XsXrF0DlTbvoJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GYHggmjrFOgDt5MhQvH_p60nngs33eE1HvnuumPRNnfk1H3fvGGhL2j6WBQ9KOMn__2ROmHruHwiac4U9QenkfnpLZIuJXFW8o2UwtxmSDejypgrc8D_2xMfF0syXrTYOBNBXcZ_xy-DsQ8qoJW0VPAjKSbwmZRV-6RB8w01cJ7M2x7G4RzYoJSbDieCqFTGXrZ9FZ0aIlszdagjBD-znbIbe6Wq7HeqxyUQb0IE7Y9SAI5eQqMQSI1lhx0eoSmuUFACqS5OkrlkzGQvyjPXYKIO-VR6JKDz7vT8WvLP6Uqltv12UlU99-0Nez9IHeZbJNV1O710xRsvsrvxU0_V4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP1Bf_sqWwPAAh1UdIipLN_M0MHM3IJnKkdiZebMsrNvTxxaBC97PzH1kOy3FSfgmGe5mhdCzeqWq-tmU0e8JFoHth6P5JqA_9xbMBMrG8o-7P7KP3a2FI0vBOccUCWb6WarVxWP07K09-9OrySukj0QHirM8WB_17fKwyB4FNtxnGQDn_NDlcXV0O5R4E8RTiYrT0AkPsQvgw9NHiQd5szlzCEaxdBa2t5OHo3RgrohEk9g5APB5QTemip8kdXp18mmOfKzShOUBP5R_DDiMkIcyl7teKUbN-MzKyj0sovVheTqV79iLs99GAWJ6TEzFnw-fiHEcb5jZwnjaiBVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-8RyuezwP7C2vW6cywCSckzBFUjEniGRHHG1fw99mOyxIcps1aPjK3Ir2G8PvDc4f-0BwwB-O2tpK9xzQp4MC1LdPm3cuH8bw96qDVVGYT3-p-SxtSRo-jsDuLhXPMxMafyX-NqlCwqC9EojCmEZ6dxW-M6Xg4gsdpXDbaRK6u_awXp7DOtAPnV-a67DrSx2vicTQST-AirgP1qq8UJGUspKRkESFw6-L-4BX5CAh-5c5QRtSm_p7a-i2nQbqbZYD4k8PA_O32WMAHdQ7b_eSX0OEB8Bk-8FIIrIg9CO7XV24chNB2HaU2EKsBS5G-W0b1-sjmFVhJhlpZvuzgXnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8uadjhVq-CbAZySIDpGQH3OYAHwoMeQ86a2HZ-eLTd2WZQzlyVNHythL_JLT0e2hMxHNzBGsdQkhOSS5qAKmvOyjokgNoGdN8RxA3ON_6naWeD_Dmg8bN9-_0vchj_Y-YafI1LJ_z46HMVs1qhp0xDetRBbDRqUi_0NKIVYm3JnACe5HpvhRZmrcctor_SuL1dPI0KovvpGXSQO933-NfcflL5t1rbV2qg_8uB0xSbH6b-7VxKQ7MqojtnLHfX3F-U48VH4xuSGqoDjposrEug8HKn7ODxVtxKkTSlaXibR9Dv56BJDYCSVeLYNGLv262t4HrYlxCkfC8K79SQBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4FcEHbTBy-LnnVzZXjAoMl8VYz3E4Y2jG8qFc4EVZbJzt5dDxSDhle16XONHbkay16l1hD_0NW0unS5svqE8rpNEJH4y8aT9uCpNzJWKxPM6EY9CfVPkFEQUtc7VIbyuQuDOCW3j30qngIs0S0bzaYjJMAtiNvFTfr2bFtGOPBGt6RHWQ65nG5OsJDY3i5okP-UACCBKazHyfs79D2UyGE9mUg-U8qkgwZlz2M-W-gdqyCDDaPX4TYVHFY-fI92KAnAyZcJYAhNnNcdfscETFt1J4j6FCNNIY27JriNBH_gFKbadJpah2olWtmGBJf3nzXYXbJ1BTZRShNNxZkKGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioH0sV9DHhcVcTlGVyiw9B-WOj7p3UwQ-Wh-bKOXhMp2rVqAYxZgBzYxSu7uENcIqsYBNTbiobUeep9mudL5KI0fY6E81TanDKgUYz2phU1a5eaF1vsiv6I8det5QOZY9D_MMEzl4lGOKYAuYuIORv1GrNK4sz-UD2nRKh0JpuHxgjP34zAiLXjjkDIL_t_shL1ls5pCCEjJ06d_68uwHhHyfIgbKYUJPrlggXfr48x5FmVZgYQ4_W1cScZbXOCLp2-9fI-mV4mWsG1JFtYiifOBTzTtFzJ0xOw2zzfofnKFTwt8Zpf9tiuUDrobsIYf-Ll29mtNyUTXLLD0uS2uYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxqMbEvDW2Na9GvgWzl4CfJ-yhJaW5YrgleGZ6UszwxwaTLjZS8wm_1jPy5HawcDiiGcSKS-LSDRjjWS3Y973waEM9i1HaYhQ-O8XEAyQrSKsomvzXUcnJQ71bLL2x3HOAr_hv-QZCqv54rJBoq4LZLCK72w1fMRFVKlzWV_gsQcONkOQ9WugqTvMWgKLVQQycAtFNXFguXKuEVzIQeFOZO5iu-ygaRHv7tZRend0rNr6cJnp_bGle1mmPTUH6PnuZDqt6MVbPYbJdsEOfkAhemcIQcDzPnpMX3hAyiYTISF8acLXAcsUJPgmqzUZOsoztinpwFbloOOryykmuVDZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dir6dLxBksa8yI_jLMdZpVKt9MUsi348IbAsqPfwot9k1fo3A8BBZ3Ro8g_hCoP4W7udrqzNlK8iQNkIN9LxtYHuEWgLkfOyv-PqqZm3c08EqRg0RSdIawJETV9tSOB47ZDe0IV8Ev0RoZhPXSwrQSn_twlasvirkW__2uUSvttgEnM8zjgXbPzQEXwgFb7jHv-mNiFlZK7rAGiqhz08DmeZfmNGvI8b1_ryAnYXKE0b5X57PhLhEjiOCiBpwwTUkVi-yPpWcwB3-Cpm53_maQ1_PLH3-gkaEpwrTsiiPXSRONzq5-gPGbU0qJ8dkdskStzlePISgteem8dVJxNWEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhnlTXGXICrTrLHKU2XOQMTIua2wE-RfPafgmL7Yz6Mz4Fki3zInE2Yb5-Wg_L1jQPOTgn6R2hl3_3W2sDNGsFxpW9nF3xzECr67IF-b6-yOvwF_mAmgm-1CbdKz6PasxkQyzWGSZ-XAVvLgnzyf2PVjJbQ-jGDt4gBoqKovQYEUfXXgu2RjDd8BahYVc9gEodn5OpmP82atDupf02UyVB-hvzqGjBrIFywR0ghiD-oe7BCuVil-CoQXkYS_eZg0ITdWyRoB1wWqIbYJ77N-YpmgIeS-X30O7_yYgGj_YHdGiuYlnDOg-y7MuNjBnwuFhibR6AkATAaGDu7X9fZbMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-qyHs4vSqOpU5rmleNNcQAUWEs_IPH8KbTYzkJxj-NdcWzTLFy-JjBV27yG1el2ai2MT7jyF8m0UOhT_tz4aImpz3zWETRigkHb9ff5gb8naApIUZ9zVUyawVC3BMLC9Q4gc_z6sH5uxrD6nXeZ_FYHFPHoFRuMMD8kgTPpR8GTr8zUz62A3BhoudYnNJ6QqJi02kmHyyVTBomq3QJ8aB--3h1F0TB3946LHKY5-j598SxWqIW-oU31PrdwLt6a2m3H8tdW4CKvQ8q4Yvd8z0w6vdWYYS_5DzQif_DGSc3tHDD9hdT44NgLbg53CZiGkMX9hVlU_a96IiVsFdGYzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoZYio6Vzm4puVbXMhsyeCj5NJxMi1S4vz9fWMMHYhhyUB45hosf81RwSBhynMcQ9EcEHdQEYJG7XeAT54pQJCf2poyuUb1f3BPUcQOBo-1nvUle3hr8cLOx4w8NXBcqOkqPEVU3SIURxyZfKahtdQJdD8msKy4USRmV9vQRSxEupDqm1TWBdULDrji1r0-6WTCsWUIccMwZCOaY6uZltndNSrb8DUPmTIcOik_nYRPylSwX1vPM94AxZk8nppPu-w3RuOBPj0UEObs-eB4wbux5Ts2xZLdjFAWlUAnEUXVvnpIqkTOrZf2-7LEAcic1xuPAcRGzk3M75_VKf5mwHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkK3YjPAnv6puNXUEyxYFqhBH71MeWHlFcQmhnvq74CbuXB6Ntbkj9FuBUO8dGwQNS0tvgVs8WSDhD4BP6FjHmJDgoFym3RECGvM_v0TBUeI-ny2O4pTOahupsaFlpihXqCSz1lh-9rPiaAv2ccUA89armKlIQguUqnnKhuXnEgnLMnCxXmHmFrVggFKaiTtg9ujc7ey3QmgzXW5-MWpxxFr28YKXzZQa5_hBi2yUjfucY0sBAjPV6ps7403P4NnJ0Oi8LMOMohnPNABRh50TIGlTCSVcCMGCUoQRMrftjmplp36sjXgjBnzcM8BubfF6Lynh2y26yeBVOwp8ZuyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rL3_MNgRPZL45GRTxpUkaLX6-hGeeb35jS_BQIrWe_SMRP5tZMhuSUzruBV9jsqOwKqIJcgZvU2nU09PTxLqYItI3oK90_U-0VNDbjcUtVHCBh8tC7fG8V2xZkbltspM-0EG72dfnP6QfE0n9_uT8xwH4pepuoVpLhLXitvB5BTbrUcSOq2s22vdbujjJNmtTX4b9f3oneXGOOFTsjHdS6nTBp0kfCf40KDvbvbzkX8WiDE_nsTp4wzXSsY6YRV3aUP2TYNrvz8jlIBg4kzbrUHX9y3FIDrA3i0oLe5lrxFeaIDcTlwkO7eM7PbIs0zV6WqM5VLx5Nn65LGOINgoGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSmj1I7VjOZIOpGyTybKJcBLENr00Hly9AY54F0BKnmtNKMkHvpqplZ0cYQjfTyDDe-_OfDPxySN82m82BDK9FhrdLzJ7OisBaDHWwz5ssPwqEIZOPFduEMa_aPPFHhKo--USG-lCpNgf3M7lTXMpEf-6nrFzkooPJFSSdXxaHS3VOcSINTHx0uGO6FRBqyibFBHZAkBCSS9oELbvkCOrt1fB9q1n2532I-nDB33LpXLEH0h5BjZWhx84oPYSdphOaXcuhNle8MeuZEBhkmsSq8wNxaPMu-y0QRRWgvF1K5k6GLBPI7Kj-EQZRZzCZLQQDHxzCLAbfTPTFtfMyPk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7fif2pNdi4TolTHN8mxU623BLi4E6L7r2Ti8TE3bTM9SZg_k8TZgQilxgoouduUuCe7rhoXrA2OWdNndcr7pqudo-NCu95y37l6nZAyErAxCG-raBtLwwn36-zVctRylG5ZqAiKJuwsF2Ioln3JU6WH0Ar6IdYfqcXFIgZBx4M1LYBhq_R7LWf90P4NX8xGVuH54AVOUEl92RMU_gLfL_zO96Ya6vS6Q6xHs5CN4id6OFKf9VXwEvaGheisnA6H26a0jacg8h5nGJUHJinCgUnF9WVSPkSZtRvtV8s69phxOtblaVhEiySZJ532i3B_BhDKCM3Q0DCdfNfS_i-eLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EXhFyv5jl1hJ0UD9iVbXLCNYzFosSZEN_M5SNivRhYIgA0ykhOqhbX2j-0x0SYUxx_-BnDGIY3v6ew3Qlsv4cJTW4m-2I-F59eMxXc9i6V19cBAZB3-gtKjSqcHSNwv0vYl9NYM8PqKpHhi3ayS7vqPbk2Gr4AW_hO8zkN_7l4fmBNkkXD9yJHG8TDeVppKB41VklJG9w23bsbZPNP1df43ik5zqi9vtbewUXk8k_xEvNMGw3lElFQWzrdS70GFbCgR7giQaVhoDkp25NtbXal-KOKJ70MlKbKtUyAqgNJyaxCikQZ2YFL5wk6piBticDX6BqA1QSM2fK-NUexAxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAlgE0RagB8vfZpuLIvdMLN9ywmhvwt2U5UTfe45zH_NqWs_6BW479azQGDmfUBnhtxwR9-_iLdnxQGHCSPZMftmoKHC0Ta_IuGl6ntHlYhn_IzqXkUtZD6arzIggz2x4eTFgi2N8ftJuqGogh3PnUUB3WWFJUvtGlsyFR2jLcQ1fm88mPNs21fRwqqs6dlcgdKrzuWHtMMACN3ehHai0a2eqs0B96VafjmtNk1zeo98KNfrY7poOqzroUNrduEI1Z_-fK3F6_lccso_oX3vZBcjBoL2UVhe1Fq3-gP7huMKALosFNL9xlPrv6JRorPHtmvt3olmh0J-cd6B-YRvCw.jpg" alt="photo" loading="lazy"/></div>
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
