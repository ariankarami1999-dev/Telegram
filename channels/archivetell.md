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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 02:50:38</div>
<hr>

<div class="tg-post" id="msg-8095">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پروژه زدید با آرگون ؟ بفرستین تو کامنت ها بقیه هم ببینن
❤️</div>
<div class="tg-footer">👁️ 886 · <a href="https://t.me/ArchiveTell/8095" target="_blank">📅 23:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8094">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/ArchiveTell/8094" target="_blank">📅 23:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8093">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پروژه زدید با آرگون ؟ بفرستین تو کامنت ها بقیه هم ببینن
❤️</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/8093" target="_blank">📅 22:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8092">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbSCZvrm82W_LODDwdVtWUv6PkCpViZQIYhF4ifD3Qt5-SSiPD0J_8Q044JdTuYjG8baIFcMAql_F8hkkZN9JL3AdHukzFgdHZ6SaVkq36CjHj1kLelXmx_XRogJo6V-HB9gTio7gG91rg9BDrIBCW-IM-aaHxRlrbLfjmYdKrXh-F7Yvro3tqzZtne0MISGBPyOeQ4yx9NSogQbEElMUCJy8RRiXFYeEiATWUXXZKn78FUG7FwyDD2Pr5uoCEzIpQFspKvsHSf0svbh5hQIvhG5eHbQHapbCl_lLzES2DNhNAlhZfesStYcFGl1r20TLqxHxzNj7-1S6IrKXB2uYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیو هم اومد</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/8092" target="_blank">📅 20:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8087">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTbFZtK_YN2I8GJjx6g3EHZPiNxYPBG82FM9QiTZQxtSB1tRuAE4GFsxr5b-FjbQYWSMCkKHs9Dg8BSUCbB8I64e7PkBpgAn7euSErbwgH9vhT-E59Dl62rH82iAMGpa0-d7dU05VBrbO6l_SWEFzW6A0ANyYYVWfgUg2SnM7Tc0y8TG6jMMsE0DNdwadrURfmh36SPivqagfJGP0LaA45dle8AfwrXxqNWAbpI5K7cemXtbe5wA3fx0YbvKh-SRjRo-upgjkCGwlv2xA89PQT-hBAa7VzMLJjdWffUZLEUeZsT_mKd_cwFDjQiSL4TnSrcun9Mwuzn_TUUM26iJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا روی پلن اولترا منتشر شده ، معلوم نیست کی روی پلن های پرو هم منتشر شه یا اینکه اصلا منتشر میشه نسخه آرگون یا نه ...
💔
یه چند ساعت دیگه احتمالا بنچ مارک های واقعی جمنای ۴ آرگون هم در بیاد، خواهیم دید که درحد مدل های پیشتاز هستش یا خیر ...
🤝
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/8087" target="_blank">📅 19:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8086">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/8086" target="_blank">📅 18:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8085">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O64ny_XRRTzS5AF0fYN9HzLQPyEN565SFRStzqfBzy56Yb09h9EmPhoGAQPPwJrYiw-1aFCJ48p85-2DT0bLXibi90yQZ_8_gPFwQY94s8zLWkLglogL5D53zVHbbyUH0ImY2aqanP0KauaVfbxG5Ts8_iIhlJjQJvsYnNYTpQ90QcsfpLCynO7mWJN2MfpN3WhpIlJtpI5aUA0q3oYOPAnE9GjmjaRLiYPh3YE0m4vi7jiT51FhYnvRruhIl5UtiRLzoODW3KGVogeeKTqGZCohVxxDcIJHHKulitofdyNx6w53L3jpWPwxZb65iqrMxTZrtG9K0nq1VkSFhuMI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎖
• بعضی کاربران مدعی شدن احتمالش هست روی پلن پرو هم جمنای ۴ آرگون دردسترس قرار بگیره ! ...
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/8085" target="_blank">📅 14:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8084">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/8084" target="_blank">📅 23:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8081">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAw9Fo40WG0a8AAVjCI-BZjRDEFHolfm7w75h-IL3bzVCVpN7whT87nZNWmU3SFtGBT5a-2I2RD8V743oO1RLzkYzD_ASvvBE1lg5bXPGbQIrZjIAckzDUAHMDBcXd-ad_PZcCd8XjwN_gfH42Yj4WGPDEYBQlJmj4HA98fCbxFwC_wQ3YvQeApqw7VTypZ6PxRUtetdf6EnIFDji2bJd3as5Dv5aVk-9lNE0c27OkJCaLNZxSWNj93YNy-w3cIIDi0dMfWCaHFyUi0ebTtiSl3d2fQUU-VpbSsNoxpoMNkYt_0xodkA8GFEVzyD2TciEYjxH0fXz1yArk_LK5OZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک این مدل ها در
Artificial Analysis
منتشر شد
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/8081" target="_blank">📅 21:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8077">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/8077" target="_blank">📅 21:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8076">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLInbInw9uiZyhp72d2C1hGGG9tK4yYhr7uph_IfZZM-jv81fuC_a2_2qtNLKfoBeo138Aolj0Drysh3SauLJsXsnbHWMEOvNJmbDVugkh2zLpSMd6DCOAhDLqYamHR1di2WLJXOMm1pGSZd1zQ1hf62FYiAO3H6oR0T8JWSsJqrloYH6Hu_gYd4Q6PvAUs3tJi9JLOhaXyXbM1pGx2BIHkzsyUtuMB61uxiJGcpBHsWo4hbzwwVDRp3kE_t9rJtOkm5vB3wYRY5VwW3kPipTox0fKgy_tHxEEixNhFpijQNe72ARSMLqdcf5CZYcaObwrcXHxQgGVbqze9rjEt8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعب
گیم های جدید
https://tehran.velestudio.com
GTA Farsi
https://gg405-golden-gate-racing.surge.sh
Driving</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/8076" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8075">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/8075" target="_blank">📅 18:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8074">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/8074" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8073">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/8073" target="_blank">📅 22:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8070">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/8070" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8069">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/8069" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjbAVe_Xl23aBaiaaNngBow3MY-SyJoe3GpyfcPa2fytipS-Shqceb17X3xlGonZPZhNwH731rkbzhHHAn1TyvT7ZdTNYCeUdNRTsHDP5rMHhIpXgPoc_C_Su_pIcktPRUeUgjePNyavS97_p_UJ8psbG9xlwjWaKIsZDnIHNPQP-6QzD8BcG5VK8MlzpHPCx_Sgh8bi4eLQY86HlodpVln0arLZ7YeNZ68XUT-ls4pyOufpIA0P8u_BcPs0uLTZVme9627-i2WK7SPzAHoqibPYlSy0tGLizrPdsuGPErzfayvnRCTVHNgTuhzQcbHvwMnaG-ZcFvLYlO9vg2DPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8067">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn7SXPfs_AOvWaZZLbXoOSZAf2yDppvBJTKcAO7_Z53O8ijmk2R_zV4c03FIOWfJJfVxofkQ8MBneaOE5XRzbPoA__Hl7b8sBxiHIS1Pn__8hRgBu-2dS7vlgX_42JYs3oDBjhAZDRkr12HPNhk9VyP9fBOmQv4B3z56XFuNYhdPD41msCHY7lOl3hIeuqnuz4NymbzBIjeG_-a-mGGJdFED3QIHD48J_cTHJ323OZofYcZJz3UAcxB-AeIIq4ACAzc6KPZmk1Hip8r5GP_-sjoL0OnX3MxtszDvozd7q_1efRF_kPf9uzkXdZhFTgiKBt_rntwSWOjhaxAcH3hHvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8066">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orUqCto7NUyRwGXw5FvtRoSTQdvevXb51H7JpALfJjEIhI1bAKlovEWhI6y0zYY_XUiEfz71Qxp3PX_Dn5J2Y-Toq_gjLoRhfXNwVCNOX_5MjgFIYRUnHM4Cj9OD4NgiCCjL2EezJHAK8EbITTteUAmMFP0sBDgwHEApICqSFjEWxCN6iyKsThwbutmu_CMWsL4aBww-rbLCvGN58_8IZOE--uebFH_b39S7UfpoosbxnjcCulfpsmtlZ-wv3RnvJhyGA1Y3QODYk-gsA2FMT9NqP1v4cd4E37vRa9NuBn7yC9g_drgV_za_iHDTjzZYtNG6C-OdDiXFIblIRU3J5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvOqTtZ1t-SYeJNH1mnQ9ir-dJ-ie1XyZBSI9CDn9MBhR6ypLlKM-CnRpXVwCPi8etTVg-vxhDY1RYLs9kunqedYqsE1BkCwSFahxbE_pGxdfGJBo5theMvatytF6Sa_f_punPXUOEmSopdLjT3SpaAsOSe53jIIqL0xLQt9DJnc73E1bIodbpgS2TAzJLT34P1u5mwYo9n-d6LzQZZbkpUGERFDU5uN6rmoP9uOtkaMweXHD3zKLQDQGE_cdYHYS4PLPATokiEAooB5fWQZMTZMUxB9oSexBYBHSlvIylUr2sVE2VP1ht5j8vkRjE2dcahP9UD5qVOIb1x1i6s9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksl4kzb_08OsdW4_Tc_fBo0Yf6_-OJDtjoeBA4u-aYHLLsqlqN2yZtTu5zIprMjSNK59fPvfB-QYSZlWQPy4H25HFGu0n-_j6bW3mGxogzYHhsmNo0YeeAqngT14wRYc313jwQoXZ9LxACueOS3VnW4GbWehe5CbpLccbfyyThBTavZ5PLHLxiyTEQ-yixtMjsm-YwUOkpks3p0ycPVniBUcHbkB1l5XrqjwdZ7rN4ir36-Kz_34u_BqvY7I88C3gLx3PJBIaOFC3daTyQh3ai9wg1o2XcKhIKohpW36GWCh4OUnQmkDmqI80w6r0bHHjTFV4X-9_VA29WBI83FMwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rKhdD9i5KGDSHSCv35a1hAeYOCL6hBALZ7Rwa8yiZisdQOu8-I7T-f7Z-yrvR6v0XYlV3mRaPMf63qsSN8iU7qyEXdXrISsK6m5RB24_bTHEN1ogMbSk3lrtGjWnT9F0Qu8fZbyIcoaLdiNU97SafwdhSy7gH9rceKqSUUI7sZLcsNozSNre1TyzmLyOduzKoFixQu8pkdGMFHd20KIrevAS3JAQzSGvd3GsU2NlFjfJN1gb_NmoyapCaDY0Gs-y3zVEB-A9Bak3Ph9CS_zOBrEKls1-fM4r82Vv9xQqsQ-Gd3USDWbFaTq1PuXOqWrmSax-G0ILALPu1gX9gi9sgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iXZYnU8zTSA3B4JbAM30jIIYic-L0A4rXt2n37Mpwsk4pGujeKaePpd2Nr44-WqVLGRbdxufHc5mMa5Ukx5LUA4bO66SmCY4wxr1TIxPaJl42TafSjEQ3x53W9cSLN3EDLspW_q-P4UhPros0bMRU6VdPNgfDGaqhcWCSA_Tl-CLbZ1_N3VuTSTJMviw_P2TVZCI_fVQqhiRYxZjiBrEfd05eGB1M7AvDesuJzzOY7cvc_KAN3TBPQd5FK4EMxQWnbcj274WsrptHMivmOrLtn0PtrikhxHlCuqPjXJI3GkKURbfiJNKJqquNeI9cMaP6-EYgfq91xqjf99pADMEUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=Rn63YZe2-AuZM_v7Gsi76auhFa6AHOmZb2c6eSqSQkpDbL6TRAIYE8zP7z2Q8Uc2CKpeUV3RlXEAEZeBMrw2Ba8sA5YYAAP6wR9WbStXh1MgvqbvHw2YzSDgq8Dqa9Fz0OOEi2GbpxOoEfaoh_YN2SmPKGucHEyZchCD5QWwMdijRmFbI8yI9DFV_e42SJ0f2niXjCN9Bxa_ZG724f5VIIe5PIfIVuFJ8W44_QyWz5emOpajOf3pJMTbvWgMXPGs6-n9eXaGEcrIY_A32gaORtniNPHu5XYEleuhAjnPfqGqOh5eTtL5y1ytPF-N5-9hPYe5NNwqAFiDXd060x_pEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=Rn63YZe2-AuZM_v7Gsi76auhFa6AHOmZb2c6eSqSQkpDbL6TRAIYE8zP7z2Q8Uc2CKpeUV3RlXEAEZeBMrw2Ba8sA5YYAAP6wR9WbStXh1MgvqbvHw2YzSDgq8Dqa9Fz0OOEi2GbpxOoEfaoh_YN2SmPKGucHEyZchCD5QWwMdijRmFbI8yI9DFV_e42SJ0f2niXjCN9Bxa_ZG724f5VIIe5PIfIVuFJ8W44_QyWz5emOpajOf3pJMTbvWgMXPGs6-n9eXaGEcrIY_A32gaORtniNPHu5XYEleuhAjnPfqGqOh5eTtL5y1ytPF-N5-9hPYe5NNwqAFiDXd060x_pEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I9aoJWy66lngHTzP6vV033CXp26TMxbzniB93XHKB6WoS4umqIfXR_EJ7Hj9VVZ1kN_avemXhnXUBfgiUDuds8ap15aJEBwlFSdd90t89DlMKji9Zxo8IkRxRjxFUsu-e0g8qruMVK4LCfQDNiKycyL_-i-utInKesIZt9sm8UhKGAXPPaytfdtBc38NuRTj-GadZXDimsbdrvbRfOK83AebQgIr6c8VqfPHIo6nbqTEYfyZJoErPgGWslyl1mikrP3Gc1aw8IezB_cTIYCot0xhspRmW-J3_aQ43TUXj-p5A_4nvoJ6XKj452y6TJ_9cCodTy2EPl3bMJdOgN1yMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=qLEzN7IV72cgTj7tJ8B9ujX3HhCqlillumFgwNIMtp2H9sTU3J1y-B-FndezRR_J2CixEwc9E0ifbcvHWncff4qaLCXwUIsWZwSLN-5og-8RGvDWq7qF7zp7yO4nOxhId6WimyxfDpSVz91yH1ufqVPJ06IPFH5JwYqkoXpfaRZTv0ykFQVTtBa5JgDvMh9t5qddUa1cyII06QUd75JPHaLk-xigdZPCOEvxqp7vMMjaqnDrvgOUgYBEs9Sjq9cfpTLjIWBfEnrskPvuqJs5WbFYMpWz9UhzzFruvMMOsolPQQ96i9Tdmj8HsrN4xDMC-67urXrpvujkIlwIw6PHuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=qLEzN7IV72cgTj7tJ8B9ujX3HhCqlillumFgwNIMtp2H9sTU3J1y-B-FndezRR_J2CixEwc9E0ifbcvHWncff4qaLCXwUIsWZwSLN-5og-8RGvDWq7qF7zp7yO4nOxhId6WimyxfDpSVz91yH1ufqVPJ06IPFH5JwYqkoXpfaRZTv0ykFQVTtBa5JgDvMh9t5qddUa1cyII06QUd75JPHaLk-xigdZPCOEvxqp7vMMjaqnDrvgOUgYBEs9Sjq9cfpTLjIWBfEnrskPvuqJs5WbFYMpWz9UhzzFruvMMOsolPQQ96i9Tdmj8HsrN4xDMC-67urXrpvujkIlwIw6PHuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCYqETtRLcnSdotQwI62bXc2LOg_FsT9XZW4xqSVkv1lhd7hMX4ApBJWKy1mtqVyiV3wz5PQc7iVC0HZG7KyIFLh7vX2rMJRIY7dumX98y6C-dT-JBVUD0r5Ct8lsd4JjWoWMneYcgIByxnw27rMIXnfRdNauJMGjn_xvcb862_Txd4VV9_iQD3kzkW1tmjOudJQGuLiIQ4wGNMX9PgWJ9hJf_rkDwM-n65mYzbffpSwA21ke0AeLKR2Ak0xYJHAqwh8BVZdeaP3akcpn_4XaeRJdsF7Kd13O4I6NnDWcN8aFFVhty2oXH-Pwh9hlFenzBEK-MIo7XNO3HH4wW1_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obquMdyhxYsyBrjIGJVYu6fg8ZSYaRVEA2bTvxVpGz2I-zH4Nk48s4Mnxe6WrFfBPJaeYRGkJAg8UiIlYlFUleoRZ61jJGwRU6os0IQleHOGu5FeAG5HHSWEELW0FwmaH0XF3ZCuYA0o-kdAsTtBZvg-koGZ9MaD_p5T1TPnJGfqGO5ihxNtFt6fsDfhIiHHg96T-fAkMvNjlNu2liaat5nwyfqN25svzICXlN3VBZZGAviR3CHfNfRzGn1tHxXSDMREgeh1-f8M-L1eisMeImyuqQYVe8rrij7-I6lhrzpxieQp9zYmdH5UBnsgOfA3LygEOWsHFYx8cdP8jI138A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFHmjRtg_ZumzgOGnIDZYHXk4s43Ly5rRJDGiwcPSWnrAL0svkcususdytgSFZvAoWb4ro7_3QHAcE7vtwt-biMlPEjvi3AHSMaGYJbgxjF8YVs9lmzK2c7glNF0lLqWCGYLGNEZpDiXmrAT7GaIXotIuyzOUis9OIRrNXgRe_w1kbO29d2SKDxxuI0xF8qZ7vuBAsSMY6JFW4g3Bngi1PhNhDF8CjFZXuAoK0MxZY2u-vTsKFR2slRm2lwdSSRCW3JS3rPLgeSg_g_GIMZ8NDynZCJ2H8RlxN7TuxTmYzOyfk3a42xCAa8d2qDeN6x05TKXk3VFNusE-fyIQHmCuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktt-rhSd2UTR3U_QzebOB0-2tj90zAh9U-DV364tM5peY29YpU3zYWB-a_-t4tOhCl-kmi-yJThxOYSY72XlmYA2DtUz3B1SZAO0j2_YoCiMYSOHPVFz54agT_IrSo9LxS3Ixcq1MeFR008h98Od49o83YWPuwploT0QkK_Wknwa6Q6zvImkR_54qBXsBS4W-SSC2GLZA_fnd-Qi8NE61ky4HLqyFhz3NVa6C-gv-y42FX3nQYtTBW1wSKxJwB3L6S17SniR_t-Q73aYwZVkLe4NvBZR6IteMBfsA457R46RSsDH_AVrXIJU3jenPqshRHRu7Qg6jXAvIAdXwisVEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO_dRSFah35lp0jXvhC3TfJXa1cH7pdQAqzLwFVJ_diPmf_S7VN-HvaIIbYbktJ0ZrGc66-htfzQOLn0oLNQ9fmLmjjTKNS99j-n5ae-4Q5yxXZomPH1oTCfGtpdAXnehBn1CgIaiWPoUBoWYxy6EFOAHH6tFbDKrMmKfDV8MwRfURZtp-DW2mN-XMDxRpeacOocg0uQ4k6dAj6d4maZOB_i-hLeN7TT8xrzzUQIm55sLl_67-yHx4f6hsg-KYVqX11XT1PmG8CL7m6_aMYQ4dkwaRnyj5JKcCRK4UYhJc23gYIC_2P1o7nrDpTHSOhhT3G8tXMoO1UBkipRA0oF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_DT5DQHKXCzjCM98NZ3iTYCixqU48mjhaVLzzY67CVemCq1EBP2ecrIz9PzGGHAZIf71cnzpHilrdA2mmJwgW_3t0oeUEERj--uUJtB1Bj9s2XM1dDkPtt8MFHcaVrFD68h7_RJAezu1-1PtCJr1fNGiGqY2xe5ubhBhhExkqMDbw3RK3dVy43O2dz1I_uSqpRaKoF8SJcpcxOChyIBA7joDJ4eV4ognFofWZ-C_YLZjwr2tkO0pMkdpg9du3--r2T02zaK5co9FYDxDUQYbPGdTMryRPn1D3b6laVi-fqHCbTUZcbYYn3XZf1YrBw3ito-uZMXaj3wZVMVG9_uVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuAsrrciav_RwARsO9v2aXVS0E_DDrsJpIx_KYHe6Wr0hR_LJ4HRaQZrakeRYy00k-sQ8DMsAbza-JnT7mWVhDfqE9ESkYrxypQ0KrF59UUOadCCJF330XYADuKkAMmUjth67ic6VtqjWqK7mZsySVwybpxujfotRoY4ljOLvoYDZvRLDQIW2kjKLK35N31AoV3lNVu27rGmtO91TdXIBavnACR3Hvf3CXFCeSP6CX6Qaxtod62F06oy84rsh15OzrhHzg4D9OjwEvj-YKCo-4huAVLxSlDGILqQ-PBVDjNQRKouMBoJT8DbPLU6dA5PccL5azjJx0JCUp4LyxgIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fb70IDFCA8UpvJ10GJuEJ9y-VzrZqapDoEvlU-HAqSVGWfG6q7CMtq1HeTgR6RcO-o0MFEZ7_qa0AN5F3rOn-oWyaKGDD9C5UxQO8_qiEB-206L4DSm78zxG_WvgCVV2xuowUPf7r-iMunkX3QcjZI8SWhrkwtT61mfD_f4QOFBWffqu_1O5HV56jZUVzLlN_9P2mIbjd0_xHQCRFUPmwVBOXuGNsgAf-rKqdzvcxRMqUTeYOZRVOwBmbeBk1esUS6H2orAbCdmRs1u5xDXyXnT4SYESRN8iISCez67Ei-dLUhyVy5AwCVGyaIfBtLkd4_WlTueCBo52jgypimVgEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx32OBD-NRJT-Ti47rcft0RkFboVpbH7BF_nxL96i2YswEHZPXsw1jJMpEe1-CCrolfufKuPrtpkk1dGvN0JwV3O2WfFzjbYCbX76E95pOcNSXlm8PymvGmuss7GiOCWQwEm44niU9n6fCc5sfvwjU15RpmqV0SZNHYAYrWUFK2EmdzpGpd84aoK5riWPlAttRpnLKVSrbz78ZO9R9U5AR_HPhHlYMSdKQd0c-xU9GYwuwgDasZuoWpgiG5Ga8WE9ybHwMLXSQL_GJQHPhPVqzaKtM7NTRB-W9Drjo-yz50zXWLMXH6hv1PRW4p1zDhh5NWCVyIqOqsCMG-iYk_C1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJMiJp-hsqM-PbiuKfBsvUJfTGArQvl_To_rK787cuuWqe88_lX3MbtyxAGm8V-aWBvLBhzh-r13czdbXGPzOuwx5cmXjUff4TF7b_ur0wN89CKmJb9eazfqL-sDH6hGbnm5HVogvguBjWCrVUYiL0Lu3gFV81Tu4KBxBPFz2luqkLtByR04bzXTOgmH96dyaoPMzzjTMMGLgLKr4JIjs4ljO2TBX79WqW4wtyQTAcMSTuuuHedYsfybpMNRqJI4yfXMtCZ8jkG0Rt1JP-Lb34n4x9IF6B1vc4a7vjMjeCLj2q1hXFUbEGqgMNnrFbO4c6Oe_OmznQAIDAC54XKbww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KoNNtOnB_FMUuO5auNStop_P3UhHcm6NmRPKXQYDdWi8ijFjQFnyShWfoNk95Tm16kppobnTzMZ6zJci8RdH90JxmgCq1GzlAWtBRrKDlO9f6GljvPxaCRT4Icp9ybLul7EI0rbvVnhSy37n9Fud7-W7TnGmeCi60Na0RU7MCGWWF8XCaYdwJfTKLbHhfyA3Ckdy-9JaRdfjnZJ_5cdI4Ph-i_AzeOKxIJVHD68LfDP2VJ5gHyWGakznL3TsFNlhicgJ17Ye7kLGyHUih4WrytphT1iwg1QKKrIt-KQVt8rN4aUZmUXqMQ76Mr3Uj2WFDVtk8wzjaktFIECH7K7RZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UV_NWLVX1wrzIRhiyU-xGber3KwMhAqBiA_0M6I6OAPeeRw3A24xa9as6pbt1rV1Q9LJLI1MVN9_P871knppk3Ju37eh_7ORk9E3CKdYYsCS8Y4dNGeR_YWS_Kjkr79Rxo7SQEeOqZ_jJtHO5dD9ENyJD0cURsgAU8KsbK97dmQ8-Ncjeeem38hBTcT97X2bP8q_LgAWqSLPS8Oa9u2c8ievlUAExcd1wzV6hc8PM25uwoGMhqL1cHUbKAepmnjJvf4QsmturenzN-8Wr8l5N4aB6EBptwGzd1oF40SlKueR3k0I5RMrJBAXYGk4NCx04jCobVr1o3z25bWXPs2xlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kR-uhs6dMNjFzkYsM38tckYgQT6znPMU6LyGN54VG1SrCS6h4ZUPtjPbTU9GoD7c_Wei9KyXCf6UA-Y6-RxWjYCc7e5PxO9sGCBs_4Z8AqKByoIDmsx1GyYpZhDdf7kosE52PYQnaPSzq85PBfn8HmUSs50RZk3v829_CqPxX0qSMZWxRcoXnJH_Nlnl_pdTTeFtUDVXH3O0NWg92FlUJCFXr2mIVq4i264WJtxbNuXoF2iYkS33r9SaKMpOA7ijAxhGmnn3sPxPXU8RQw9r2QwHt1cmX5oq7OrLicZHMURdzg-nVfzll9Zgz6p-E3d7hiktvgl2z6E9psRawJKzYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6WOOz5dDLq12VPP_LgP2ouRzJjQHcnCvX4PrnybCZVW6HWZ0cZLi8eHjhqbRXTH5k723E06LetWKnUaienHppBFLWyTAO2HPs7OLtzdpjcQbKXvH38hvYOy4UOKmjEAUJ_dgKTWwFeOW-zXdhF0oQKuuCH0_CTSUX-i-vDtqZ38tcZkcbmO07uYsqRaKxbPqNTH8hi-GoJg2Vj1Uwlt7hC4YtT4oHVT_fD6l3t__lBIgyN6RclfCMxFsGE3uOXivwqGjmaEzQRnPz4L4lUnsx_f4k_rqTa4emPxW-kxKuUFqcsfkackXl7ebBhGfyrcmQTOrIEQ_VgLakuj93HyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-U3dymfKY8bU-cG0H-XqpcsIo3fdQjalcyd2qD6oYa0LYDiUtYNK11xwT_oio4703ve-UJUNbKAOyYW0YxjD818jQxf_NYVIcJgkTwnJfsGnv3kgm188Bx_tpan43OIxxr6HcwD5IxzQ6Y-qFpMAMVMKH3_H9J027WduxjahYR4gZ1M5co7ArX8d1qacx7Gp5GXOwDZOtzMmVm-VfBSaPOISgxiP9wMv7OQgS4q4xnE7GJaJm2le90pnzQTMqAD_0hdnUVUcIMT6dFDum6Wu9AIKpyNUBAWtctmov_r-uAxmRg7Qw3IpYPvPgcJq2CQSPZW88fUBfbPZ_MJzTzECg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iglncg5Odcb8GoMKm5NB-X8VvVluuvUaOu9OO4yt8WHjA1scJxwWCGuRnRRKWZCmJ6hPT40TUA5ZNJ4BlA9BBBnZzIpD_imbeQymeDJak0bNr9MQ8sCgsAekaN2aySJ1sKWfZA7_GyWHSqFDYzWTcbnByhp-nRt_UowW1WoOWVd1QtNZCxRczzu3cucowTD8zLd3WF1AVriamU5tP6KNXSZg3ziogJegfm2AP1ZhzgOeKB23esepbVym0a5xwday0qXaL2omOLIwr8jltwu4dsScYDWLh7gaSGI7eUNMA72HgGWomUy2Zp6sjB30Pokl69a4WHtw-4q61N3rMOJmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHh-liSJ41U5AdX459vJ4jshNU1XoWHu537LUFa82ukjOzW-PygYI_5yGJRLL-oRr7hWqpemQ-hbmcsXGbpLf5SBJSOEw4Fe_9P-ubmGTQmkGH_z45gtD9_DqWOb0DTREKVjh8Om-pismPTR4AahOcm0Ynn_YErg0zQGiPPCMYEP9_R6Qf-x3W049oWCSvKN3McjoTHkvP_Ft1LDlbzWRHFl0Gcd3Tb43Amr82D_rszpKBVZM84u9NSLRUcLfrCMzVNHwdTt6PqpnPthSzgN5zrHyOaebzdUpJP5DVFJUaNEWQAjVJtSl8Pw2ygBDnpNQ8aCYsLKQn2cHdt--4zy5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzsPWEKOhXNpz_hZloJTAttEMKXnjElE7WYepE0a-oVll0G1A85a5o_tueAwT-oxdjLIk0apbifvGyqW5Sz36PKqMKPsYRnfYd0cK3mXOt-0pfER2H1X4fLqrX_1t2061P2jTFphWS7is_JYr2p-xx0VuJflSWU5OU1-p0HMLsawNH3JZFKVyyagOlH8EaYqpWOHRsozgwXoE4DNuaELbxFdV2NH9C65aLyyEU0d9YL1uzBgKtzkEPohmS5QFkEU1Kif8E3yzFe02LDV5cLaYvcwKt3M88SAz4mmHkF6EFM5ra37NBK7Q_AsBW1KhKuU0NpHLfU8Amz2EWQOECZNcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGpE_9mIcexqzqWsRVN4nkitINU2fowP0oplTTbVJg38UyeQ02EHDv7kryiZBV6FqPLPCBslmB3kv40P3LHL21nNzp3chPtS3LkaUW-NJQoIqUvcsggis8SCpHX5nvUmSq5ntoYd3g-VovHmRPxbbPpToZiPD1YivlLrBURcol3pDV5RV43cmLl4LKvKP0UWz4Swk_oCbJEy79bxoVC26O-tO_TkMzsl3-4RB1ZyHyJ5F22nNuEV6fydR83zesb__Gox6szlfdLV6ZegLEvo61nOO113EElZRHep3DSsRzj5ap9jZvGbttP2R4cCl9YtUFvGv57fjD1NVjJW0veYRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O__vKwx4TYf6btAGSsGjv7phYLGBZzG25c0lAZDcz1w2UOAxmDCvBpRARk2ypy-e1GOC39rpRDqtTy_LUhhSdsfr6djnVkeCMegk5isVVDHmSGUuvCg1hgpFvQ16C-yISYNtMQ1QLwlz24TpnKuQFny_OTfwEa970qyWdMhjpoJILbHdLwqTWweC92PE42IDywVr8pojqnxwvwJTRMCaiMbCQVe28PVuW4M1qWwHTF6VpmFlC5P1qDAGJTjX0oJNOaLjFzeKgcr4rBNeZ8Kuewc8yOETw4bakIKUZUJKaEmb5n0Y7mJaBVRTRlAF2t6DkNUoRwXgaE7p10J4b2TY4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X70iGMKc_PUCNdQlg5cNW8rj3wqVGMOpeavVSfjz2f8iOw6QaFaJrKpHrQLMdEYtdS8QpJtWRt0GIs_IQzHQK1V4N2FshmZdtgHgkQMe5kdHPzixXh8T1kfZEdcxQ1jg6LBz2sRGhTzCSH47li6jEfCDAqOz2L5OTfjqhZcZfqFTgGYGtXYHJSxUJOYjWJcSky2Skl0kUufcyYGt1CBAH2wx0qN-y_Amn1dis2KielWjaXdRGWciWAUKpWpi6Gz8gM5Co6cdAJw6Q-UZGhI2mIpyVU6PeY_F_OA8-r0tliWLNw3OcqjQcOw5_YMR60adogl9gP7XsmBHytqXrinElQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmiCWLp6cJjOeAZR9pHMS5LhzmreWPWun8LM2Ma6g2Bza3fOr9jPM6e8KvC1pjvQJuel2kalBZpUIIfLkfSAHzmKp4uHTJm4QuDp6UHAIEVQiXBGDDsDYQurfRaes6kUoTRxY4b5amFgOE9lyfumyiCzcGU1Du6iGt4ZBUMCP88tehyEIF_dTTEh0mQGVrh--hIxh72_eSW849M4wrSOhBqDgHwVL1Tvos6Hdp4jQETUCUeFYjmkX-KlnuQI6DWR2-ujba5NA6VNezlEjmpf4r3To_oXCa9qkxRu-_JFkSECft6yfh1i_AOk-WoTptlZuWEgk1wOOVzUztoht91RIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=G8hF3uqB6LkrchcJfpmaVufE-3B27_l7cJPE5vygaPvw4b904oTfOzZw1JZfwfxTDFbk8FoNyRG1L6EB71qJil5o35Cg9j5-UKXAVk8KaU05_uwIIyRNzS83RCr96-Sy0_QBOvg9b24MzWCNVbedxcLFykvT-o1HwQawoKWQ3UTgcs9W7HGQsGhUWy_nASDHnZn4qEx9vABn2gJHeYqqpvzwgiusnYV66OiwedsOs1-exPPnwbux8vInt_cJdUDRT1VMnwWQsrz09Mo_BAi6ri40J_wjzgTYgecWK8eHcH_M_l8cBVZ2iCH521Nb1e9TFRt7F6cwugVkTbSwzdCneg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=G8hF3uqB6LkrchcJfpmaVufE-3B27_l7cJPE5vygaPvw4b904oTfOzZw1JZfwfxTDFbk8FoNyRG1L6EB71qJil5o35Cg9j5-UKXAVk8KaU05_uwIIyRNzS83RCr96-Sy0_QBOvg9b24MzWCNVbedxcLFykvT-o1HwQawoKWQ3UTgcs9W7HGQsGhUWy_nASDHnZn4qEx9vABn2gJHeYqqpvzwgiusnYV66OiwedsOs1-exPPnwbux8vInt_cJdUDRT1VMnwWQsrz09Mo_BAi6ri40J_wjzgTYgecWK8eHcH_M_l8cBVZ2iCH521Nb1e9TFRt7F6cwugVkTbSwzdCneg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKHIka_pLOI1oQjbuKNX8_bi4KbvSFUnWWM322GZbHlHCa8keewd4LAgmPU3AMJf6iMm_K7v26BT_0Fp5y42uQpe5AqgFwwYEpHCmbPtvsqbYgcbtMVxDkklEnlWxV7dcC13cyCE5NoUyobnma-Pk9OPG3h_RClW9vPG4x18ih7Ahp8_etjqKuydVdd7i9g6fsKDQstrKqDj_2squ1rgYJNyWCoY6_SyjIIrrNoioSX4oHnzUN6RfUwu8SBq6SUe3N0XvUZQukwPVxj7IxW6bGzFV6NWKvLFa7jpJK3BVlAkevIJ5cSb717NhZiNrQ4I492svpzrJ6ma5MqcOuyIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwNtdmLGTA4naNqmuzd1X5DMzEshgmD_J97PJ6rk3hlWbTapQCR3XEUew6HpzQmPm4TikWsjk1Bvd4FU9gc9zr5CYzRFJKgf9uRxUwRP1Db-f3Yk0jVZebTcRtFrmuYw6vU1RE7HtF0kxE9LvkCxqrdQp-wucem4cO18Fn5ciPMxmLjzG1Q0FeG0a0cVJRTlYWzG8AHkdvt8BciyGxkEy_Nbg9jS0apfmKu_1pYLbVg7Tf7eLwk-RVMFTiJplWRGTN6_QK8nsYoZ8GJwLShsZyqTniu32DLn_hupEq62dRpwg3vvWrHRZi5cFgwG0vYbu7Ma_I2XFHNiBBF8-4G7qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdkI_SfE3gNCNGM7nHZXhx_XGxuwy6mZZQLcW7RW1EowwLlAmKIVE013g-eLzBJSPQeYvf6NPMd0t5d8TG0pVOqBJTe5TzBi7kyH7G9SXdFT39Ts33NhBRwGYyDjyu1rt_R0e0ySjLHxYvY4eukcOV-y0ILCHgt3j6rofI_h0yPAy1uJOodd1HOjGnd-LGPPyD58VhY8DXOMfl3m2LQvzfffyO3O2o2Myt1lB_fI5sYTH7z-OU60vo1Z0jeIQlC_ZR2Aue7dXck5XJ6NVUdzrpAtkELYCrze1ez5FKEI8llt-4fvaYaG9LXxB9LrcXPPrqmZ0C-lsHbpz_RAVAV1cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPVkQEzL8R1Bh9eUrt271FiEE5yacFO_IZo97PlJb7V8o6R_YdUQQw80T0ma2L0W8zd61aeOSCmBxo5VeEgdU3O-_j3XFaXgUTyYfKdruiBUZhxFOaFW_awwYPEqRRiWVNdUUpGqGFJgH3Oof14y8am-45F_ps2dfOJL1UN02CiICeQlZNQgJjv8mwFI13U3c0QA08s0t_hWADII1nsmsFQXh5qBqtnUMmt9I_1bY1Oxx5QJej_Iv_-jxUb-BlyXS85vF0KjGImWlzVJF_dYpOUARQgIlkwQib9rGDH5tN-bHFpgROEv650zWDakFFtvdCKWjj4U7zxfEydXzoK3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ua2YgEuN45TTLSlMAuRdSX6NEiu28EhIAwrQkTIhecyiiWWfdmcVdG4I0BM-u8IF80XAconvAcIKrUAIpAuHme__yoBDRutCNZkOsH4vv-PFWNyUE_X4zYC1y5oVGtXe94iXn4RuVcxMbRKjgRoECcg5iyej1DHvCyUR2sS-cJbWRq9Q7UbIZfZ6BDsHULqQoq8DQXyRam1Eiil84j1mRcwdyvCmLNtl-8jwC5MZLRHm3-bpgXlDtlU2czBp9xPX5CKY8Ka0Usx5BFzdjeOZRvZuj1jsC-qOnvtFVxHQVSlQLAfk5GR660xBySNQTg0O9d_bEIy0zkt4Hd1BPLizUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOXDFcB-4kGZcyivrRnpVgWzWq8tHdtlSPRlJm4V4L8Y-6a802--Cjq-fdWApD9_4hTlwpBauoXfVFyDvWjz1eSBh7K2CYZ3GXJZvlZPTnYeU2fhxZslLJaNDpBbbI4lC6mcVC9O2pOh1sWXkvS3LfuQOTCwShhJ4hrnA3YG0xWDpC9Rz5nHGX_YPidu9kIJ9PYk5KEtuaf6Uc-a7grMuI72EsdypGotWOcI_dgUP3vfPOj3t-0BskDGz_Tyu-OhhS7-3nUg3PWLqLhqJFxuqy5WgdMcGVgbiSKtxGzwQI8Z9hrf0j_agYqAs86LySjHtx3Nv3LMwutzF1DsCunYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kNFVRniL_yfalsWa7k6ZJLvyVgj4SBCpMQCmnEnz9gxk7jXi5OsmXgrxx73psc456DHVY9t5kbz_YTLHbxAoFMCBd3kTyxNzjmCDSzi5bafviUwyaIdTxyzsD930YD-_ejSkuNz4Bsanm7789P_MW2H3w-GwSzIMPQk48-91chll1REvXwmKhHoaXmKEX1O5MtSaPtbh-FH1IHfoZRlOrPxGsBGIx2GJSbEUrG1BNb_z2v3fglvkzL94_nyauKwJtXEhYABMaH3usF1gMqrrclgKd-gMy18PxvPUhc44vZFrDCexJFEFqhLKBO_5alZjmr26StxpKj9JFnDzCcusoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kj3fTiyEzpKhpsKlO1SY9po2FrnAH1kmsutiFLS2j7gWkfaWiBEPdXRXbARUrZIVWwaGZibS2AjoaWt1gO4GG2M9mVPsESHRueWPSPMZsEt28kOBngxzyPn2rGZmHT7LqcG6Mw_zq_6P4MohuHlFlsvGC8RF3OJCLAw8Hh0wVMBWIxYPlCng7tX8tXTa4tjEULVC5dnxV5iXujQpmKdfl6T6-hbyRmYvl_Ho5Yal9HALzqM7ZB5HleKPKX87nQWv7MO1HpjM3uGvcNa3eA0-s92Vixdw-Fo9a281fGwbeS0j-Z1QCwvbAt7QMY0peV48vDjtwF1T35Shs3PD0ZbLNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y-tPQwH7wZLC2Y4kApEbRMSolmjQRmnC507JJgcobUs2vqCsURYDgLriEWpG8j-QCLN2Pn3wNSxArwbgycN0CMtDc3b2BZztSOjKmimKyc7VkhB_7Bw2h12_IhnsoUcFALnER9aZGHpL43SOP_ao9vlXX5ANP8SHR-Xag0NRqTzUJWIlZq2ACg7WTRUfYOA863u_o-svIwFkrnbSe4IOYeSlohnLYtE4OEqf5XPZaEQpe2gJ8dmDY35xwvfmSF_wleuNhYbqCADME3x9QbbKntPM5iJbO19oJKQhv3fuoWbVliLSW8QpuMBzgyNDJ93eEbhehabU8U9PCxIwSoVrAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olzKnmxLuuqIBdji_oXoSqsKpqiKBJrnT4oz7Wlk0KfKn3ZBAsFthpAY4NFam4eat7mElmI952QVZdevRk-CXtAj8ObSVR3gQCBxZh1FEzXHYF4MjkMXmndNYjaGGgkGkWo4YB86s_OADwubkD65H7f4tQDgnOhbdm06jN8lTrmPFDSsq6EDznBUskVAFywypCD2XW5FoaoEv2zh57n3Ut-MBVPGQ7GDxRZf_V2Y-pyfO7C2SAVa_CogGGaXr4G9slA_gQ1e3Q1vCPhWNy_phwOaPFRIokph9LU0BQJvzQ9EG6EuPFU_nz5w8l5q8d1MhfymAhnKI9JfDECTPdXb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSJAmVFUwoDlr6o2FujIg0W8pYTJOXh_u-0_1gBmfGjci0lAA5yA5KcLOqaHJnBuwuZnpL7uzQKdf-CbBL6XaE_mD0Vktp9Jj1dS1wvNdIaf2MMcsTuStNbJVT_oM8aXB_SrqXOEnfW5rXVPzK2LqyqppKwehnsJeEjTLRXNHx8eFmKmIIVlDtE7SDapHJRaT0OAkKCJmkb-hGiVisXH7XodImMeaM7zpOQ9xIsjj3TUWNOQk4ILhIPudTVLC9oUMPReeo-h8DOQdaxzYeIeoweOROJdSxnQKpTsva1Yydwp5oQKUsmpXsZR-hRoQGBQi_RnuXP3UJdtHDOeNsCTog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUmxGv3cJRsSwdtjL-5UhIDS5Z3XTZT_IaqwQNU78S9o0G6GgchHmBV79YOnHiQPWq5uCsXeEOwn8oriwjErsWFufwkjHi8_QtRMs9gg-lMEXYAliUU1ts0dTY2vp5mRmMM9TxlTbwUoIpO4DNFCBweBQPJlNezJSjYH-3u863IZ7nCNC3_Jt8Xv8WhX-U_sN8ITCC_SLMb5D8RsXm5pTRKE3OkQh5mUEtXOQyWdSO0AlQpivwt45nfdHyfgFWhkL8TtgHH8qn4s515_5GDNuGyvU47Kp1xsWc0TmJNIjyR-n7Km6KfUxVp7bqkjyu3ELziP-b-phk5USc3J3aJE5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpXoPoHqwBHqaGUO1Vsx-BaEue1DOSeP6igTw13g-IoOc2nG9VP2EQhMtwEZ3fRRfzN3G44B-FdjC78FZUOt_iZxMqKUZ_ws2IF4xiuuhM78eUnEt4Hrf_wLQ0_unS4MU6PH5S-XIxKwl2GtlgUzbWE_T37rj-yKCcB2qVlO49ddOlYYzdoDBTMdoAsaGTdEtrxPG86bfa7f1KzcrHeazrraAhUl1kzdaU7sXzBrAXnrUHIw0oGyqhKlVT4MNtkKOC3h8vVTdlM-3HrtxVHXt9UNkfTffm_U_HP5IxECxDi6MMmaMTxytifgIuV7WpAwXXG3TK2BPPNEVGwvg7y25A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sn_QT8kKRxsL9nbuYm97DZJ5RpbvhXH14yvGSlXjggXZ58JTu5zpyQnKJKywTW8FwZPbnrxRAd821DDhctsgPlb4onjEbMHzKvoDxvhA4gzQkTMWwEIOhEDgzj_9usn8FPRD_WR-g0-5jSbdSnMkHAAuNIToC76OOw5er74BbyvgF_sfi_a1hR3ZrQ4SAmSgJQ9s1jG6UpatQYYEExmOWIAXIUzmuRLKfRapHT_lfB_WAy701QSdXBatbVJN11TIKqjSJt60xD8iojFgN-axG2xiAFB9v8l0go4iJfPQ0po0XDdxoPo4AX-uu0wLoj3m6gJdJDkq8m2SIYH5DPLHcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPmzch3DUKd9AOUexlezFb187s_0nFIo3g-06T1Tge9s7rWzZsm9XIvH7pverY7xWiTg4a-APdv4Tr3AvuKrcswHwY-_Ek6DDp96ncxqF3m9ncEkj0nDY0tCSxDC-DdNAorCl9onoStzYQXR2HRcPA93bfVkkwXIddO6eURwaWamnGxM3WhkAhhPwRZHWwWVkSaXm5X1kKRq9Aux7WJbFI724nNxkTK_z-HjH4BYJQp3IWR8KJumLdgBqkV9t69q-l-4hP7xwlYzYVH7vCR8Fj2o4KtipByDiUL-zPJuiuS2P3wqtw3BHtmlmmRpVB-NcDbkbhpsecrqfoBJsCr1aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFLn7eR6bejDZqnWTt2Jjn_NDzVaPFAzBZ2wD6ph-CcPpDI-7Jikj3e_c7ZD9J29eDzUS7QqU5fU58cfc5Xx3Ak50MIjOkNB-r6oJPEyFZMxXsnRfN939YgtD8Kt_TBkFvSoPw0ZgOAP-duiHr9GvsPoh2FpzJz8WvKNFHB2KZqAEpScvjnVbm_IwLa9wx4n5DvMKUuR-z8NUf9ZlpgmwtUziNwEq4Ziy5gWwDlUPAP9eUGyI0jd3g8vc34QZeUiMuoj2YqgGu7W5Q73wYX_GHPQVyHUH0IWVWKeEetzL6XTCpFhi3vqo_5DqpmCtVHpTklRs5hOmkF5rZRPyht9Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Unmc5GhWVtoQcNwVbKGwjKp7ggORlnpYNzLEQgj2nmiNPoOfBsNinnTP86uEUfrFY6Hh-KMntrdY2HsFddNIXD3jcVKG1pkH5H7G63bKtfTPyhqMGql-0rFpyRMHbAgv58Z75fTnF_7Z3H0nLoAbVX1f8zSGS9A5lNGHu0uBoSthjhUXFc2A6Ra2ASFSnTwo-LDCVyOAVJ2j_HAjJTJ2NkE8xPaJBroISynQgwBV0Fib9Z8W8hQg_MOEBu3o1nj3YIw0xkRPDKjm3URiDSdoQPaCM-L63YlA_ONNnMhh8ppecIMKIjTXks4XnSR1OvOxy0m5uK2fQHg21YdORJZMFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dc92E5qZnkLb5Tt2thNvIM5VHIln6wv20qWl4yFa4VBbli0G8-gHDyi8mIcaOrEWtORleaXcYLY48ZFcBaylsEwua_1wsH7YUJszEkXsyZJFNoiiE7GzIoMpHVZAW_EYGcYTRuMiBBs0mVtvoADYIk5c7S-WdBsqi5d5XwHSTlN51qOCmuZbwhk4jGddHdHiOBxw2wC2xmNekS67MWTtX6KEKBUqmiey4S0MRR-woj0ifeR3cd6xQI5IZxnIiRJWKetNMyCyumMHzRSb4PnFfa9dR9PbebLIrgDhs5mGRZXX_SJ9LmcaJ2viIGh43APZj2_0gwi_nlSlLFp6zlquQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig5fCNd69Tt7T5IjuldXBwgD_-IMIxRF42K_kIMkuaJMyUfjQXTQP5mFOqCKBT1enQf72OjkBGni9qX8AIXDiAevzyqrF7lVxw7gSgEhb1HDAp9gb0Ai6twdYe7_YiRugpLrkc0bsyLnHFRzS17nflNhtRaMnOdhV-C_Wi41wtHN2o5Xhe3MD0GxN2vushhEMV8VIs3AIEB2D6fCq97al-HOCQV_wISZT-0sm3PPCaIH55z2XqzuhjRtnKQGtK9eESYmP-imwJulaSiEXjjJdJBPF2gy3seZ6E1JnHM86hGH8x-3D9pu3StpkeMJOIMHyf8oR__DX7bRbAC33gMsDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XQZKM3qPrnIR9o0kLm_UqRGhqBALQsF1OOWq33zR3SGpUh8S4-5soqsczviQoJPxUcJ2beTKeMnsqEG7PoghTkxI89vB5Q98ftilmF9p1-EC3tjDsLAzBOcAFeY0mZnWcNW7yJilpWPCNQ-8Op0uhDBE_erwSVQEylOZs0PTIlQJRbpNrl2Q53UPzUajYfthbf0RBL43jZHDbzVfufnk-0_Iga7HL6p8wX1LhghyDUSXffC51vIkdtbJ3KDy_wC-TNb8yHFkMMhspx-7bTnK9fWUhMS27McV3K52XQQXA1_qnAilWm5zbBvS8jj2ag1zubkD8cgjhrNTeQdx_ELWOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CYrF5HlZ110LOOjnab6WdWJHGAKMKsMUuDK09SfQ3_xlLEC5yZrrEbJvqOr-vShMUgFNN0HHbJFQWZOXffQsvwRiUVJfgRyQMcsnotr0IzqJ_ZrlZvOEuMDHcDGhZJa3N6ZBzCYxaXePlPiifVXyzQX63gTdgRUrCVFPpmJ3KUU_rWLI-jbDq2wfJv3o8jaottgrDqTFTs6EQCgk_PJfrhSJFwPQ2oP-caf1fywjnlBQMqrYfn9q7117j-H1wkv958o8q07SwCRyYKW1FOLjqerHCYxthkACiOr_1L0PUEJcdOaeN-MPtgt99INFt2bfp5vAqU6RaHbI0HFj3ZHVfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIumbSNS1mg6S5fEwYjC93SappvYzVxyqGxsxFlmBastuiD_nTJcQr8qK5LvcIJMlzRvAYdypNUa3wMq1L5j4rPOpTDJTImD9SXpFP-RbEeFUoD7UtOX952Ue8-QWkVDhYkOVWBwvYCVCpF_iTHjbBbZMR5lSQvNdvrEwt61pcashhZ2mVL7PXfSfMQczcdWZOU4-5HMmjnfdyuWI0GypwK9X8TypssowU_vQ-NaGta03MsMAvOLSCOLxOVHzs3AEqNH5NEBjmdnOqwFA3gOEbFBz6CGNVb-O2N8_21Yv34JdUgVpUfongsmvoXZBU1JmUl721bv4s-_oFGGd-KCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRF6ZBoXd6E8bT8_ssibsg3yPOoMubtIggNyGihjQn20RTpRi717EDrqHyEjkUO0bD-MJP4wgibmBMj-jh5PK6Kg0KbgV0ToQ2v2y0LUvOJY1X-k7SPhl48L1KUxYG05eHJ6oXKpnY5HY5v5Shl-SFEeUT_SHmSnG1pqt6bDJD_A65h1TiM7krV6xisGOtORJSEN8oF2jwf9W-RgEBv_B86reTy1UTIX6MfVhavLrxVNli8r3pIw4ZEG-SRLmzx1afZlGoTN6I0wIPUbZe6eBU1KvKDb1a3VUxyAvq2i_-BGc6MozqKhO7qo-DfcgNdkpN16KoOmcNRF0E4OehdMpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjlfiRX4f5i4WxSL_VKFcV3R9GqEqW1D9ijLcS61Uc4aNHOvMKhmB63y2iVoZG300lCLpXipMMYaIZmTP5ssS5gYnDQuh_CaN5DCB5lo9xdwn5cgKJoOUU5AwavhUbFTMYhpkNX6tGgpLoEE9xyKcVM-QzswRtzYypoTOMig3rRtd-M-jl9_c5hcodfijCeiWEUvLcnOV0BiHNnHtaKf4M4byG9CDA2YCuHzRA02iM3Q9bTf_o5ALdqHsRxkOY8CbFdAJjjFF0utPzxXm8MXyML1_buFt-fyYAt_J8Lp_9TuG2b9ynon1pQeNbhdgo7h0zpovSPVZS-TKZjeF5738Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nU70cmBxhAMWVHE693OdHWFOp5kSmC2f6re5-sqnZdIMuff2lgIgk4kb9WB1vm0A1ge6QWgJpObonH8Lmue03zJH0CGJEukfDUOhjHUANG2I8iVsD_ovTy87vLA96-EsoF_2m1SWHMCk4xiQPmDus08MjcaInc7kX5GQaPQOMF9mPrulQc9AIH3rVP7b83OefGoTDhPuXxD-MFxXppGeqIQRpnc8Z5ovyuZtZVrNY5QJrYEqdOK7racwTIVT3B_V5xPmdM08uS0R3DOdQWX7pL2ctUigUtxXJ0qHZn_Y5stXO9e8kf-XQGmv4MQJz-aiorqy6_ZiMLCUcAHInqYsWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emDgZgGe1ddCkf6YEjguiCzlyNqMagdknW_TampUSpinba_LV3e1y0LSVciMhTQwRXEhVBFFrqt2IEviGNrkQ3_H3eG2iVKUgfHmP7s705Yw7ey8yjOGj2MsR6V3wLhPDRwIWCH67FzyrdhI9K39j8-YQifn_tVMfeG2wiGvUFw9_T3gn73ZT-hdnuDXjaQlQ5KvYIJh0suYi-2MhAa4_I5AC3U5EGpNXl7WjAYlrj7bjCwpVg6KSlo3wHJbHhxqQiWckfGMuBi9IItjfQhcRlh6LyKzoGIMu5QFM2V79ixVEEyVGmVAkzFZbVoUl6XbBMoulPwZ-H9zWgQs0XGwbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEOumx045fmF2QciuNeoDs1KIns9fLQRmbYHjilj-M5PbEP8CUFIk5CquZpKWxdjYDZ_Qh9MjfUiXsTVr-fEMHjuwTa7p63urC_5YnhlWXLA1wKFYf3ZCNtv5F7O_TZfYBrg2z_bVvf4TOEKTnEdWJ2vpRg4FMfkWmMGUSAO80Tr6qZonLZjaLIoyCVsrtwGUA7qmfeW4I3oklWen4P9soh7bFjKyiWmcuDmAjwqhK_nPBAQ_9KMb6XwpMD7KveMCAlW0jcoup_gvltQogkZaFlx6scmxtLlqmP3PWpCxsslgpxpPMjOyzD7dQAA72Cw0ssTUHTkMSkgPkDWW_9-wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICbuzvYnoD7mFgQT119KvUMEMDrklZxxsOqSgugJ9WUU9ebSORKfIEvhlB5c9wfNxrj-sBOhrd0LiX2mZGNERE282LNlC0Hbu_33wKtSuxp2KaBT4N9cDVV9P-IV7SadraWStcZ4hHhK4nmsW50xAnpXNYy1aF21cPXRy17NZdc1qqBfU_cXir891kEDGP-FNbjjlNUW5CnrmsUrg19j5JKNKqGcBs-pNB5dLftRsZ7-TBo5wnbpKZkDjjW7vbuQCnWlOgVciDAw8JAiK645w-b_FErTrHLjQPoA0JJe5zW2TjvfgKf_jxHgcPUdLZGXh6_Xx3ltGNfVD_wqqvCZmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXNEVzFlKzkeLu4eiADzB6KwEOfcAzV94f79GsvtspEL7voo6w71T0vFHc_nY0k1J1vDz2ZxD8bPpbSDcZqKqlz1Z0B31KKi1rBYZ9pkj3dVSvHBxO04NcLHd2tc-ccNmMU-yKF8ngqoZXWUnYFpGzERqjH9Q4nAZp59YsLSoK4cBqKWQEwWQ4ZmPh5d_3oXjBGt2b0210JlBozH7fttqIWW4FvLVKx3i-lNd5lwZUxL9wPFgVa8aMDZjKEYHOkCm0ekHq6va32Qhf0toMzwMvDvlA-YhTelR7qdRrHraR2721CD19uHIBgP0HpBYYQTSfmawA9sD3g9r_-VeFUaNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buxbJ7yCGUvpBQLOpvBVHlvM8B6PSVM9uIs340mI_1UnsZAfnhEdvuO6PJx8kCva0AIOdfQ-r9dW_pZuOxiJzkoRpf7Zz41vQ585y5fN6NKK8Hk09ljULaJeMJSoz_-l2TUPqOG_pjhsuK4w1dJzu_ECxNgvanV69qhKN_aHD_nPS3KYA6h_rkZuA-e6wkuZ6Uzof-7y0sxIqtx0-qt5Xk0d7_K_4KeqdJXgB93vglFbxwjnoa9Oh75cnfArSAH0YK_cbuhORwSq91S1z2psW_Vn0OHH86w5HOKXhVnaO8mQNxy-_FgHwoWwUrhcMPo6d8zHOnOpw_kSYXHRZnI5bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEB5vsAuTPRYT87ASySCbjL7pIO2H91MyP-ftsah14jlYd9sjcikrk8mpxjiC9OlN-BPYBczP_TCAAjWZ7FwILAJz3D3PQVaQOMJ6n6kSsKcNRe_a5w-h775EBxDamFqOEzdnXeFUDnURQ_L1auuBIZ1Vc0oGhwwn0fpdnSq5K42eBIzQcHihKiUgDgpQju5u3JGN8hJdnIGArZGmlFPn2HaSpAP0BVhQMTR1gN4krHh9gCQkr1Kc-S6vZehA3WySRF5N_WSfAr3042Mj7iQjB-TDJaGnz5-r5xS2u7sX4iJEUcwW5xk4cQVsEWEy0ghzk9c1yTHH4reXUZwq7SA7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CvjR84omQaGP12bY_Wzl0qp-i4W0uOK3DGff-kKhJ5hJ78o48NbhHuxBw7APzOl_XRkZfHYqCpAB88MS7ur4zhJDeMt--FNb2NjWgNEJ18M_Yr0eDFqlPLTir8E3CJUAoNUDyvl-5fTdFviu6pZymGl9BC2fTt0V1VJ1r4QuaDL6oT-jpwe2y_Ur_hGREGA4aFgFhS2xY96U6ZnKfQUByamKM6Kyp8nrSEhVP3jJkldAinn4uSWQXxVmBxxCcTUwwRRuL6vMmj85jYtbmVDakgSY2_Y-IyAvPTDxJMz3sLi_9ehxW9xDPYHM8hN0dlwrTPMNZqTsgffzpk5-ifAUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uxO9Z6_ruhw2GayTVcVHsbyhKUN6TxQJqtVFnzgtcNeLT1TtVEqKgu2wgkTnb6vTJwMsyvk06xd1LaKM0iFrqcf99vEFJwNOYJuHhw6FnI9xh2TAfAZYFMlWaoZUMD4tGBJvN3EB7_JkZkNvihdqzhSy-UzLxuuEeC6IaJt2mV0KqoAsFKPxlOe2rUNtQD9AQn94JjZd98XoUOWChHWy9oizJsWbPLg9oba9PNlzyvPPYMZlEAsbLQFkcuXOdpFPGGcnVVcKIiYCPMop7PLjRUVOTmGQlpsc-VF6I9KlqDDOUlc3XoZbl64bIKDnKccwKYScDGe-WvTQwi5GHlOpRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTrT28CY0k1LpSwORrV6GFAD1-5GXN84n47Qz0s2Foa-eXQhF4pN4VlyxmkdW8s6i8R5FSqyQ-AR30nEiktUBwCTwxOR7EeH7gehXC0WMF3vLPda-6aYHeMy_JQbTrIu_5g_xelpWO4bIXYrVeEe2ZwsYfJb5cT1aoVibUn6crWKQPlDi4_kh_ed0x1QFQduYOxWAWFvtWJGk8asyXFuQTdPD-Xh0vEau1O5uu7TKWNLfouQdm22X4acSiBK7JgDYl3vQ7PTMFQvVfrMXYOQwYiVqayJ6pyuJeMotYi5OvzTtpEe_F8EpgFc1m5sOAqbqv_GEAcsAdr2ZXp1CHb_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7fif2pNdi4TolTHN8mxU623BLi4E6L7r2Ti8TE3bTM9SZg_k8TZgQilxgoouduUuCe7rhoXrA2OWdNndcr7pqudo-NCu95y37l6nZAyErAxCG-raBtLwwn36-zVctRylG5ZqAiKJuwsF2Ioln3JU6WH0Ar6IdYfqcXFIgZBx4M1LYBhq_R7LWf90P4NX8xGVuH54AVOUEl92RMU_gLfL_zO96Ya6vS6Q6xHs5CN4id6OFKf9VXwEvaGheisnA6H26a0jacg8h5nGJUHJinCgUnF9WVSPkSZtRvtV8s69phxOtblaVhEiySZJ532i3B_BhDKCM3Q0DCdfNfS_i-eLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a5DtQZs8ZGRA7FDccB-tkHsBu06GN5o_vtWlOiD9cx-t0Jn4RYl55EtUdaJpk3wjbbRVSLPLB0n1NcACVhMLGVlJCTTlW6QE9SSgSfKJGHV7b2hZBL_QTjEyk8L5ub_2kOR9SIMnYT50EDk4zvgnj-GL1leBy35SJo5npN09sVuATOMbvoKLZyWBxvSGguyboEy_8wUvzE03fSSTZRxdVhZVB2I651vNvGyvyCadArJSIwLqs69nNYaRKwvWDq0EKB1DsdpOcDHpUwmsjC3-YbhR4IYiO4Wxf5eidVnL6oK433B1OP-WtN9O5HWjOyKRlqxne-3klZjCGn1M7pIP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcf9LwdzgiTExWTNIbPF5uAuselOfuugVgAeILa7HVmHQ9FQ0w1S2N2dpkj_0HeCg0wDGnpHtc-C00rtASh4IBL7hljSsBfbUqGcaWzr39kW0sTHdSjW5VVfx7o21hD0VFA4KOsAM9Uuhyd0qbePE6Wj64SLTKCi9kzoQj9oDFRA1JAcdsNA1yE27Da3pVDZHZvdJ1UIdYTggDxwQ2gCkU1sJUhYX58FOZqmX0MAFDqg2bTLLhZK88B0HI0JuyBACbIl06slLwEKxqE6MrFFFYfeg9HVEDK1Vywu04r4Er2n-xRQJDSkj1r7G5nQh5brqpFqWOh-fIva-DVh3E-Mgw.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5xDh1enL2Fyh6Jj5ZmACrZDceXQrnfZFNZd2H1oe6lDbXCrumQwQbT_eiL1wOE2LOHBqNv84reS7V7-8blCr8wkfiFr4cuE2j-DEiA6CQoBVGZgieHXc7255VYFhRVUpUbHagVKCTj_mgfP5lHAsgpp8oDF9x2HvadYU3uDA70BV-FaNFiRxjUfffo4T19GDbXZlLIGfWrBvXDaZjc8yhfquUh7SUzfjbA0FUKmXTiUZmghwiVZXln-HTDGzgHmlTZN22hWJZzCS--VI9suMxMRWzlDhsN0Q1inzzOfJx6uNDPrnJogzha6g6w6fNlOVRLbeynTF7Dnqmq95_cqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
