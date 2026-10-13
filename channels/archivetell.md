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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 22:53:43</div>
<hr>

<div class="tg-post" id="msg-8093">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پروژه زدید با آرگون ؟ بفرستین تو کامنت ها بقیه هم ببینن
❤️</div>
<div class="tg-footer">👁️ 284 · <a href="https://t.me/ArchiveTell/8093" target="_blank">📅 22:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8092">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbSCZvrm82W_LODDwdVtWUv6PkCpViZQIYhF4ifD3Qt5-SSiPD0J_8Q044JdTuYjG8baIFcMAql_F8hkkZN9JL3AdHukzFgdHZ6SaVkq36CjHj1kLelXmx_XRogJo6V-HB9gTio7gG91rg9BDrIBCW-IM-aaHxRlrbLfjmYdKrXh-F7Yvro3tqzZtne0MISGBPyOeQ4yx9NSogQbEElMUCJy8RRiXFYeEiATWUXXZKn78FUG7FwyDD2Pr5uoCEzIpQFspKvsHSf0svbh5hQIvhG5eHbQHapbCl_lLzES2DNhNAlhZfesStYcFGl1r20TLqxHxzNj7-1S6IrKXB2uYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق چیزی که فهمیدم جمنای 4 آرگون برای اکانت پرو هم داره به تدریج فعال میشه فعلا مثل اینکه برای ایپی های آمریکا تا جایی که فهمیدم و روی اپ خود جمنای
❤️
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/ArchiveTell/8092" target="_blank">📅 20:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8091">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">طبق چیزی که فهمیدم جمنای 4 آرگون برای اکانت پرو هم داره به تدریج فعال میشه فعلا مثل اینکه برای ایپی های آمریکا تا جایی که فهمیدم و روی اپ خود جمنای
❤️
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/ArchiveTell/8091" target="_blank">📅 20:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8087">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTbFZtK_YN2I8GJjx6g3EHZPiNxYPBG82FM9QiTZQxtSB1tRuAE4GFsxr5b-FjbQYWSMCkKHs9Dg8BSUCbB8I64e7PkBpgAn7euSErbwgH9vhT-E59Dl62rH82iAMGpa0-d7dU05VBrbO6l_SWEFzW6A0ANyYYVWfgUg2SnM7Tc0y8TG6jMMsE0DNdwadrURfmh36SPivqagfJGP0LaA45dle8AfwrXxqNWAbpI5K7cemXtbe5wA3fx0YbvKh-SRjRo-upgjkCGwlv2xA89PQT-hBAa7VzMLJjdWffUZLEUeZsT_mKd_cwFDjQiSL4TnSrcun9Mwuzn_TUUM26iJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا روی پلن اولترا منتشر شده ، معلوم نیست کی روی پلن های پرو هم منتشر شه یا اینکه اصلا منتشر میشه نسخه آرگون یا نه ...
💔
یه چند ساعت دیگه احتمالا بنچ مارک های واقعی جمنای ۴ آرگون هم در بیاد، خواهیم دید که درحد مدل های پیشتاز هستش یا خیر ...
🤝
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/8087" target="_blank">📅 19:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8086">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/8086" target="_blank">📅 18:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8085">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O64ny_XRRTzS5AF0fYN9HzLQPyEN565SFRStzqfBzy56Yb09h9EmPhoGAQPPwJrYiw-1aFCJ48p85-2DT0bLXibi90yQZ_8_gPFwQY94s8zLWkLglogL5D53zVHbbyUH0ImY2aqanP0KauaVfbxG5Ts8_iIhlJjQJvsYnNYTpQ90QcsfpLCynO7mWJN2MfpN3WhpIlJtpI5aUA0q3oYOPAnE9GjmjaRLiYPh3YE0m4vi7jiT51FhYnvRruhIl5UtiRLzoODW3KGVogeeKTqGZCohVxxDcIJHHKulitofdyNx6w53L3jpWPwxZb65iqrMxTZrtG9K0nq1VkSFhuMI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎖
• بعضی کاربران مدعی شدن احتمالش هست روی پلن پرو هم جمنای ۴ آرگون دردسترس قرار بگیره ! ...
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8085" target="_blank">📅 14:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8084">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/8084" target="_blank">📅 23:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8081">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAw9Fo40WG0a8AAVjCI-BZjRDEFHolfm7w75h-IL3bzVCVpN7whT87nZNWmU3SFtGBT5a-2I2RD8V743oO1RLzkYzD_ASvvBE1lg5bXPGbQIrZjIAckzDUAHMDBcXd-ad_PZcCd8XjwN_gfH42Yj4WGPDEYBQlJmj4HA98fCbxFwC_wQ3YvQeApqw7VTypZ6PxRUtetdf6EnIFDji2bJd3as5Dv5aVk-9lNE0c27OkJCaLNZxSWNj93YNy-w3cIIDi0dMfWCaHFyUi0ebTtiSl3d2fQUU-VpbSsNoxpoMNkYt_0xodkA8GFEVzyD2TciEYjxH0fXz1yArk_LK5OZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک این مدل ها در
Artificial Analysis
منتشر شد
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/8081" target="_blank">📅 21:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8077">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/8077" target="_blank">📅 21:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8076">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLInbInw9uiZyhp72d2C1hGGG9tK4yYhr7uph_IfZZM-jv81fuC_a2_2qtNLKfoBeo138Aolj0Drysh3SauLJsXsnbHWMEOvNJmbDVugkh2zLpSMd6DCOAhDLqYamHR1di2WLJXOMm1pGSZd1zQ1hf62FYiAO3H6oR0T8JWSsJqrloYH6Hu_gYd4Q6PvAUs3tJi9JLOhaXyXbM1pGx2BIHkzsyUtuMB61uxiJGcpBHsWo4hbzwwVDRp3kE_t9rJtOkm5vB3wYRY5VwW3kPipTox0fKgy_tHxEEixNhFpijQNe72ARSMLqdcf5CZYcaObwrcXHxQgGVbqze9rjEt8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعب
گیم های جدید
https://tehran.velestudio.com
GTA Farsi
https://gg405-golden-gate-racing.surge.sh
Driving</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/8076" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8075">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/8075" target="_blank">📅 18:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8074">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRDiMlxMNFugli02ImZaXc3yuNmEgJTQsVxLLbAvLoObi2hzlX07bDsFzxzpneWaZboNl7rwYt6T7s_gZ7AVQfd-8ag_j1pfSNwIJwrWbFvX5ALhkOB7biRTmj-ZNY9OWKm_A7eKjSY8ctAAKHm81Y37vdAvzmM5Vm55vMiKfiz3hiARfQhvHQEAdHPOj7huZKBa1pkIxqdy6IYvqB62YqfSGk0FJsV3A26lhXwORY9pIoqJaPNkO9D4PdoCPp9kDJ2xoPNqW-V3mshWFFo0Swv5lIScet6YfeMof856HZ8eD3glRPt8UyzbDZdGetvL24FYylJpSRdHPoQl0xMH-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/8074" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8073">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8073" target="_blank">📅 22:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8070">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/8070" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8069">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/8069" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjbAVe_Xl23aBaiaaNngBow3MY-SyJoe3GpyfcPa2fytipS-Shqceb17X3xlGonZPZhNwH731rkbzhHHAn1TyvT7ZdTNYCeUdNRTsHDP5rMHhIpXgPoc_C_Su_pIcktPRUeUgjePNyavS97_p_UJ8psbG9xlwjWaKIsZDnIHNPQP-6QzD8BcG5VK8MlzpHPCx_Sgh8bi4eLQY86HlodpVln0arLZ7YeNZ68XUT-ls4pyOufpIA0P8u_BcPs0uLTZVme9627-i2WK7SPzAHoqibPYlSy0tGLizrPdsuGPErzfayvnRCTVHNgTuhzQcbHvwMnaG-ZcFvLYlO9vg2DPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8067">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGGHyYeOinSqsJunlUu07N62jwzmID3PK-VCtqmKPOJMsZWpDYTxfZg2YXvzPywgDAGytWLJQZKZ4MPGuUxFh2BHm3FBetvwRH6US3wPoA9SOvkvOl99VzZfVFofcE1rj6I8x0LTUQ7rVdDSzwq77qkXtnsxUAHU7FrqE8hFfeamYCUaOsn_kV1ECgG-3_qQVhlccKES9Y_9IH7xjfGaTWZWT6Tko4E6f3CjYzPYALx1Y3sojwodFFClBCaYF8FQhc5CGrviodYw5RIbdHzPSDMzatHr9T3043AcztFVmQr6M_ez1gcaZNxuqRan_nOdHJRNJoOH5UBvnMI99w9viQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8066">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2fkpbVAKrGi2Mk8I0kVAEErIBAahBJStEhZU5ayEthhdbY3PLGw7O67jaT9uiVvkQ0GEX95w6b7tGowTt15hIKgjwwQYbTstgVwydNbi8Ld87Ul8c0K-7Yjp4Z5Dc1skBck0e9mMO1mduRYVt4kzMvIJ42htudtVJYw1NXUPCjhUDKxfgxPakt8U6l1dAdl9UKwWFPwrUeicgdf-EMlal5LiTQybARZHzoYdz0A0dt09QzemK-VDO2ThTTZNHtu8LynGmYttt2lwSfJragQJ-VYPJRvQCMo3w6L1q5DF7QDtMMttiYDwp4GscKVMi_tVeDjfq27UNtymNcNCfZpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQV7e9B4BCTgZyUL4P7yFC4HgbeZ_vm1cY0-jvRizz6ArE1WmduEX8DfUHKo78HD_FQAu8lNhiLUZ0uQYUT0JQx3nwnIK_6sT5KLGCB07E9efRJaMuovULZHDVtaMZY9d2_wSkDUWqWPp6h-6_wrNRTKcoSr59qtBDCMQpdabsZvQgMzwKUK8hu6F3kTXEB8gZWrj1xUKGBr8eO35TaFzeUzpx-8-j8BXROF1zD8FMj5pgjZSpu4jDj5JKdmmPKpGLkSF7mBJFqcFNhVrNLz0401OqlpYDzXmZA9oSOBM1mbRbS5TW7e8UDMXnmgRA_kj7IbybrlMmuof_hzCa5YyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u69HIpU7JI9s04zWedwb0pEpHBd20yel_brKPViv-Uv5ozkpWj1LKiI9YhSGJgKppQGyhpFznfoH0m3Rx7ZI5nW97w7FhBA6-aMczWLZXs0L1MsZZYhXD2-b4dZCulL1VXY3pBHkSW0jdHe6T2sp1BB6VmYLYLRQswFFdiW1HvQDL4flTxDBrMhak1yJ__aWmmVMpS8DR6Vhvy3qIJTirqyXIH1Farf_fQHILZZpiwgls7r-O56cfcIQ8dQEOw-T94O70mqLdR4906t2ypg11P-AH3MLqF_Mk0WtyAul5AS0dBnVvq56_1Pm9RE792XfEYZ584x15hqPotPQdT--zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uJ9Z1fKOUinNyn2hE6xRGOXM0Nysm1auCUSuTgqU20t99A67wa2bFOYNuwqk8q4yUQKUIud9uDTJRD5FGawo_Kd42iDpKcMvMrq_PacoT9FiJ-0nQAJG7TwSfhnowhPijktnc6Il5aokowHh4mfQWwV_LcyDW0Mjj_euvXo7csXoePmKGqSOtGvPrYz4Qcry-V2n00De6SchRGpgIfOMBfD4RDFjNBEiCnKtUD03tFcyD-_34IMXYDJgjJWzG2RTiRm8zXYtkMLbl4PE-HdD6gSnZKuyKk529LeNpPBavaoSusKx9byz1dFBq0ERTIqzK6GPAgnNgM5fVtKiTriFKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dACanF7X5PuX4PN_NjAbRE9dD33JC8wujpAol0Ve5S2vm_cRY9YH8JZXn3oMoWTVd4hVy6YwTLvbXyNRRtVbaEYGpHsMv8DIzigLq5kAD7nv3N69UjJNZOQOseymtOHpGmhMCdeGrMvLsNTKabNGJ3yTzojChM8Da3qWAIgRDgZ7RSStX4wKWIeCTd9mni4aEzO5LFkH9pyaJiQcvBhWQmtKfn4OMrcSrYbuGxxI3o5hb2T4nhMm7uy_u5EYUC1ReQXP5eAhVxNFuctHlt7ek1Q9mxdT7H9ERmVJuq6Ztb7mYciBSpX-jS_ccqgATV-UwuB_LhZKE4I3mbELuIRDxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uqb6G0XRJxXEfjXFXiDKemmFtIpVIcVktczRKO_6HivTbF1ChG4BLbvEADmok3CnJ1Kc08tB5fGrAl9JhDznQP8onuiDq67kdG-jYpbf0hcMrFS8xG721-QdlE7EaBXrxuQMX09xnj-opCBu1gw0w3EsnBiVz3FuUutn2bf7ILD8aVWWeXP_etoM07uJxUG4Dk0xNQIMHn6n69CuYkQjCIeOPEipVCy9TQKrmMNTck4vGcEBB2dl7p9KSQEZOzqz96Goer_BdiFs3F3dYHWBHZlibrRmhN4OVWWR8d6ZQw_UWayD9vm78YwYTIKRXIp6hleVw3jkxODx5q3j9s8rFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=gyPrJ3Kqzpt3y2pR8DDqylOm1fl0rYjK95iX0xdCxBP4hI8oyo6MXfffB4s125DIjarez1q_SdDXOXPZXBLD4zikojTwA73iIUrzlgEYguSFim2UjjlTa3-ae17Gou7Xn7MTrCErPJ8TXFybc_LyMJmN3Te3ngTVJSZ74IzIDGDCuYdoLVAHFjcE_WBXPzA-2RxgD6s1SofRZT2uIu7eNAkjV5vHBNjbbfWcQUXvotJlUIwFuAHyKW1VNbm_DUwE58MggftMo3pfLEwCWj64IDhOfcz9unb-kVaVHT9uhVP19nhAjDfNQigMq4hSXMPSFVbW5zX54jSTGoj4FxiNjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=gyPrJ3Kqzpt3y2pR8DDqylOm1fl0rYjK95iX0xdCxBP4hI8oyo6MXfffB4s125DIjarez1q_SdDXOXPZXBLD4zikojTwA73iIUrzlgEYguSFim2UjjlTa3-ae17Gou7Xn7MTrCErPJ8TXFybc_LyMJmN3Te3ngTVJSZ74IzIDGDCuYdoLVAHFjcE_WBXPzA-2RxgD6s1SofRZT2uIu7eNAkjV5vHBNjbbfWcQUXvotJlUIwFuAHyKW1VNbm_DUwE58MggftMo3pfLEwCWj64IDhOfcz9unb-kVaVHT9uhVP19nhAjDfNQigMq4hSXMPSFVbW5zX54jSTGoj4FxiNjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qn9_UoTxgxIid8jcpvWtMgVvqH83frqN4XVUtQ_9lNGP2B-Nr2d2nraUUR7sjRiZ6YJIeY1mXaRIDAns-mCKBoTJlwaNx6A2oDogNDlH_Rnq_q5cJDi1sreHsuKZdghz_ZJwCFeFX0SsNpZYNkMNYlofO2BLfUlAOgbK_N0LNtf_jdJPVwScnNkRfhjWN7j13BrnCb3ziFoyXnFwJVzHjlnHYKBf4Nl1GNG5PjY2aEdgyTavdCeYoLS9dA3uyKnAbI4MljxHamAvAiTemJLWUuJYoFOG9NVyW5NGZiOxAO3gi0fWJFfTrxNm1Fz4KpiPdwMB_wG7T2V9Z_kF3FHf5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=M5eW0eR7K6kx7wPO17unnb8ePjUxVWiZFIFBmQJ014iJ4k2HAhxGLYH7rLritu2YieX0stiBqoJTz4Osnj7eebH4U9DPYwRuY86cEnx6zOmifSKEUNfGG0zyb_0pt-xDZy0LeGP8jKLO_s_VymCIxdOq8U_xBcVjYDwx_6OM50zsI_YqLq7ewOGzu5HDEFA_OPK0onjdr47LaZekwVm-mMU2MvtGwED0jvBEDkM01wLPpRnAV2oXaFEcdp5h740LSCbXzUYaQVIqcROGj_WfseVOb56xvf3cJFCUpfg5v9PKQwQL0La2n93sZJQkowS3fFaidcL77sZoUrgm_bLxJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=M5eW0eR7K6kx7wPO17unnb8ePjUxVWiZFIFBmQJ014iJ4k2HAhxGLYH7rLritu2YieX0stiBqoJTz4Osnj7eebH4U9DPYwRuY86cEnx6zOmifSKEUNfGG0zyb_0pt-xDZy0LeGP8jKLO_s_VymCIxdOq8U_xBcVjYDwx_6OM50zsI_YqLq7ewOGzu5HDEFA_OPK0onjdr47LaZekwVm-mMU2MvtGwED0jvBEDkM01wLPpRnAV2oXaFEcdp5h740LSCbXzUYaQVIqcROGj_WfseVOb56xvf3cJFCUpfg5v9PKQwQL0La2n93sZJQkowS3fFaidcL77sZoUrgm_bLxJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzVoSiETRBjzUTvLkrs8GN0HO6oFina8EZquhR-sgwD9rcWNW8mJlAcK1nQMarQsr4yioKfwvaatsATAvAkViL-pPii7p5Ap1LKywSTsJzUlyBW5vYBfRkfJnYMKABM5A5fU7xaSVX_Dd4onWoDUJXD-cwZuFFtGZ_eMn8mDE5NEg2VVRNAIZ5odNBilrKv7QwX62X7zl05-15w-vArMlnAEpphuHVN6ddG9okJX5QJIQgShp9sCluPDn4Q39_jR7UqGkXUMDj8TBs2oOWlsMiV4g_xuDGPt6xEpPoMeBohpi7WdzSo5UU-iF-oho60W04MLRNl_IhB1gI7VCQSGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4edC5DBZZvegG7iYYUXo5j4k6EpeaHzK6Mby94NMzkUHVac89Zqy6Hc7T_vONy4WHtaUEjLTiHo0MVOfK_VeElwX9_ugUmR-l46siyLeyj8nMU7Fwu6PgHRCbIH-2Xpdr4_7TImqUwhcmgaMbcb5EmRaEnZue8PTDM6E-LOhG-r341XG9dlscCPiwubTSsVxxMvnQFQJ4qZ1A_kGfq5ptnaPN03yW6tKOSWHrrw6VXqHCRnQYINj4JPEuZ6jhWcge1mUDDBMARpkKCw4_GFvetCeWfr5AvderMsM2j-arJnSu6GRlG8vF3QX4dfSfCiV3p7bSap285NgX41kpf6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx77V0TaQOM42v9Qh1H2N97lIS9OiwURLO4gmDj-PjGQHmCqBXAb9YC5x_HdaqG2eA6koHqgTX42-COUJVII4VxyehYbxaQSUd0TUs1e-G3LYbzPEr9bPCkuN-h2i8vmfPMIe36aidvJKztHIaHLdYxpu5ugIKf9txmic8H9aEeLVOI8U4Os36KRh3b-lbBo0gd0wBWkA0ICinIN5p_t5tvT2DR2Uk8Af3WMEmWqFwBai3H-CWIMLOIzv9ndYmyQOO2eBr3jjrS-2xATe7gfEi-0kZsyc6Xk0LOaePixvKN2oaKBhD5OlL_hylYZmRwphp8UdWhEPP5OixRtOEe08g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR3qi-x0ZFMieamrnzv9kCJuszoxPp8REHm_0P7qMGibqcJ2zz0aYM7fHZuRkOzP-dqNaQiD8Pi5DNpPepmzBWXRXTKZ8yXTNY-gjMUcEpp_Mm_V8BZdrRT-lOEE9oltJd7lZjIUrR6dSkUIkqm-svvBCJpUv-jZ3gRKm3AfcxGkeFhVhlWTG9Fb8O-8PpdlQJyn-f9RZlvVPWcg2Fl3DpXswjj6kor-Azii4nO_zlrkPMqBWV01DokcE2-JlezTRQOi69DbWOlOTJnS8Kj6WUPvGBy_cVurscJ7bvwTHwnOfdnvB6hTcd9vNwmcexHfC6VIUM-Mr_ez7P-6KFjlwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOrGUEvT5N7ODvA2bwj6srYgji0NkXbBLSK7jXOkYY7ialR0lzSBwoGnREzzDMAUsK-8QMdhYPHkf1WZOyvkBt8cXx4317k8RxwmV2Jl_Tud1SopCqBfn3zk654gsL3_T4YXZPAtHSPNWDAN17Mr6ns2MqC1Qztrt5Iw4wdYxvFH7PEyLPob-awp9h-cEDLDF3_Gdy-HrkAlf172i5OD8BBntJooqy6jcTjdKn9K6dDQyhmeQJA4N6JdPOlAXjllSbDfRpl7a2roERtcGZ5TxHJoKMf3LlQR5fsk4KAl3x1V_2wd1Cf6tQlTvpCvVnn3kSLgbtx9zmqIMH57_sHJKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=K7-AwBW8EyBoKjrV_nm2c4BFZwsZLo5ec-oDHCQMy5tXTJGeP36TbJvEYVD8lEo-9vrlTHCKGVcqvPlYjmkfE-8f7BYlDaQwkkNHox2IHlDvSBB-JoGa9nNRQBLOcqWSpYcd4g2iCjkS4Bp0vJ1tPJNljn-BaZsFhMSzghm2f6NvSiJTiEUpf44fjtTo7uYBhqo0DNNzgBCCkZTj42jjoCijpexpNDaC7HfwtEe_83nnawV-UIpBYjsaANBAemMamrIFE1IGBhobeyTF7p0PZxa0pYiEj_hFYThKL3lJ5KTLnichL_fIKTlACzI_BnPJJYRFqheBtaSBtVpdDJc07Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=K7-AwBW8EyBoKjrV_nm2c4BFZwsZLo5ec-oDHCQMy5tXTJGeP36TbJvEYVD8lEo-9vrlTHCKGVcqvPlYjmkfE-8f7BYlDaQwkkNHox2IHlDvSBB-JoGa9nNRQBLOcqWSpYcd4g2iCjkS4Bp0vJ1tPJNljn-BaZsFhMSzghm2f6NvSiJTiEUpf44fjtTo7uYBhqo0DNNzgBCCkZTj42jjoCijpexpNDaC7HfwtEe_83nnawV-UIpBYjsaANBAemMamrIFE1IGBhobeyTF7p0PZxa0pYiEj_hFYThKL3lJ5KTLnichL_fIKTlACzI_BnPJJYRFqheBtaSBtVpdDJc07Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqeYXJ2tXDMwleguAxOWlNPk7CLcmN88kRD-NCUpT2m9uDdsQHk33coc7lX13abpTfLO-jCvn53IlC7KZmPaxzdNIspINfOSsCKmMkEHZYOZvXZN4YqK3SSVxFw-IyqusCkk9Gt3YNMa1Tz87x5QNqh_fR2QcW5UOCobsRAPyMPcOHDh7HpZijIAqYGCxnruYR-uc3SVN7WocEHZvvo2zVi5wV7C6PptRWzQTVHW3tmFD6iOzKkAVn8KQ-8GMh5dxN11L-o5VOXkVzqdnSeWW4XJn4ikI7wcOzbNzHbicQQ5RdUz4YJPuZpJZCtkYNfU0uq1xfXLdxAJ3gXo9lHyMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbUTCwW8Y0waIHL_Cq-2S2Q0R_PI-fAPCyC8MQs1CpJTIzuxSW7xY8scnDtDIaIVgqFwEUNhIf-krmRqSxs0Hin3WWkAMapVdo8KTtlz79qxFXts2U2eZwiy2Z-Uf1oMJJh9jrkxx-iqEKyzCJJsrhn0eYln8tWtlprzLyCSoGG3OunchISD1rY7FcYWN2BGeAf0kpCfgBd-zGKKJbbx5uGL4n_nMUtr4ggxN0fQN3g2XjPKaIycqiSCk_IDJ4_jrDDGH0TgrWi8kV1KKWhTNXg4Vnd6NAo-TSJUx-PHC7japufNpC632OdhEaIj7nJJJSgjsmrz3LwC4B7FjG3XSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bdosnRVk-MT5hQmHGmfjm-Kt9nAZgVPm-jrQoCJA4Jq6YHXKnLl30iln_dO5W8yrBuB79IIhY0YrnUTElZwlXkMy5N8TCGB1qY4Jw82_JtzFU_MjXOqsnTV_q9od2qDeR20LAKnLayNeSF4O9ouk00_I8Pv1ZvxIR4VCBHmoSRxkovCf77ef3N37PvJRld7r9ORJY8IWNNRwvuKZGL1gLofCuVPdF3TOA5_Wh4DBcQkAnCNYlHGmG8ZvgzE3iatlVrDewuUHDvuUzcHZwbpoXfuPGehEOxzntVquYWbaRjF928zQrwn1G_nw-VRBZI1xDbaFnJztRBNfkkF7Vy31TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=r2JU4sj1EUAKRVluhCWs3mmEFfONSregpvbJCmiRUHZpjcQTDlfpQzdGB884KquF1qm6vaG63uNEHuU6vp-zmu8JRsNcsQuBZjVvQwuSYFoIrmkXxdAvVufP33gE5uo3g2j9IHmmCh47LEC2-56GH7rRHyB3HsI6ElgJtS6fekIEi8bdXvcg-Lj0Xtq401cFPGrELGR9xS78Npgp6IeLADAY03CpQonuM745AD-HhZws1c4N18ehx9oF8Ynd9F60KYzU1mfCGCvnd-g22Ifp5mbIdCZZD2UwBhMX49kPRe7qV7nI-nlxmYWs457YTmMC2bsESWRITkjiycSXsZusqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=r2JU4sj1EUAKRVluhCWs3mmEFfONSregpvbJCmiRUHZpjcQTDlfpQzdGB884KquF1qm6vaG63uNEHuU6vp-zmu8JRsNcsQuBZjVvQwuSYFoIrmkXxdAvVufP33gE5uo3g2j9IHmmCh47LEC2-56GH7rRHyB3HsI6ElgJtS6fekIEi8bdXvcg-Lj0Xtq401cFPGrELGR9xS78Npgp6IeLADAY03CpQonuM745AD-HhZws1c4N18ehx9oF8Ynd9F60KYzU1mfCGCvnd-g22Ifp5mbIdCZZD2UwBhMX49kPRe7qV7nI-nlxmYWs457YTmMC2bsESWRITkjiycSXsZusqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDaezXLli4Phn46RgR2ZqCqGcr9O8c69CtL72w7FnUBGXJVlKTV0FRBvzCN5PS0PUv6S_emEKsvaspmHaSCQdAUk49fmJ1MiQZcOqSF6pb1RrEhNDLF9HQZEwS-3r-UuIamHF8DHgJIc9qYPBM2HIUWnJSPBzKp9U-Fae8QyWX4Tm0NzW12crhmTZpuysN1HUds7SVjOVsm_NDTfbYtnQgayDqrkwZcf8_6kRMXwfHXrlsC9dPPezz_yL074skKBjrZ_DdOpeFiSLH-84dfdXs7vWOKim_s9e4tOBm80Va4zffUryZYMdVQROp_L50jbOgVbO6IACnHu_lbYAqx1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uCyL_cPeiVpj-uf2mJ1efjtwn0iGm7U3k6vqafdXAG_hczQ-wfGJgM2tI2OoMVyIBpqL7_vwij5gslWIneV93Jkw7wwS_6Sd3walpjRKNceu6c1MNlGM8-7ycjJgCuURgF1GFSbNGrZ5Qa5UecL52DUondkpPMG4I8WIKjc1NMTBAaE4wmXi_bS-xqBvjI8pFcnmkS3_F91pOQV2xnS1fkmgC6EQb8vvvUqshdBzJERIJx8aYKWMWNsU9AsIsi_Uhfp8-4mB5p3Me3RFdEiuI1m8LXShDHMm0PZhHpnsDGpG8HcRYsok52W8SJSwaVBxyIx4Z3bBtu9E6MKXLl34ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PWtvzOcQJsv2_0Hixq1rmpr5llqPCxSXj04g-dOgsc06Ge4Vi988arc1u4Hh7gLNEObMWqJgNv6jKJOuLWSaHhWHribxJZDc4P8_sNq7NJc4Ln-soJUXhy-LocquQ3Z2QcX8XtjJB-pdiwDmOckW1_8_j5C5kWWhp9sVVD7C1wRp4MZhKWW5nO6uLZPDu2tqvx7JGGlZDu_Lh5Yd3Utqxwn_GSYutC-3dGeTJXxZIksK_1tC0FLcM95muEEyyaKBgL87rk6U8KBmpRvsrhJ4GaY2Vv-BN8CSG7RN0RKJYQ7pdT2NqRDXjazwvds_f1KT3v8IRHErbsH3HkLV35w8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cj9CTA9UStD1LJNlzyy1IvXkAx8FfmJD7jr-od28L7W56zLMr99UF3gozVjhGFavhBoylhdrpR--h2WFPsmijSZBBzA-GqapN0Cq5rsD_HjV82Ybsv0769jEsFFBSa1wWfIjZS_ZZpYQGx07J9woDnhXM3zCMfZJOMyaUfF-ZFFZadjtMNp2HcVTYiyg7eMxXVQia9p9kwfBhyRbA5xhul3x75tObUgzj0JawSvTgFq0uV3L0kCebxHEjW2eUEhLZbaOy9BdzzrMRmOYDMRaq-Vm7DuG6dv7WHN38g2tD8CIpbved6Sg1M8GGp9mjPfXZMeLVGvaRcvkgE5SuMTI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwK7cwwvw9PEqfYvd26lcxtwFq76lo3A7qNKBcQcveQp5CkSiz5a_Vh8tsaxVF7yA0s_8jUBVQ_ZJqEXTTohjbDkKrBNIsHT2epwcnUPVrpX8y7cYaGi3KgvjNTRdIPv_rEazThMJoId3g3NgyyHsjahrPcI9L65foZcKiM9Lh0rajlZAMmxhobRm0Ae1wQ-ooj467eYqkF9M3ATeKWxXCV93rGnqmkJ0hezE7XUb2yN7FFoHxWhUDUAD6ARj6T93z6D-qw3y2pQKEfX1cqLGLy3WniAVDtH3DmdgiHei6EJbBzaqRYEsCJOICjUPlrVGCxbL7_woAgF39MdZjj9OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hx3RT4iuJgoOOyK25XaDyGAFQrjLdzs9jyYAMT4_u2nrDLzkAavb0YnDwadLnsBaXiahSSVxFoMdtpWPz4Mb82uYgh-ZD-2DZ5X1_gWJe2yAP5MpCoj9hvRmNf78dE0JiVBrB8h-tR5CAGFtQKCui9knMPPEuGEsnsttVzAvuI1QFhbcJuY9MgAZ5ODXQ5nI943n0nFaALdxfA9UDjK2PSWbpNjjXxFcCQXJocg2_LEm4SF-Zxp_vqd78qN2V5fweS6z6WCRK6HkaQg7K0WELtvyAfJsRXfVTR5pI4O_JsYC-SVYDNzdXjsdYqtwqgV4cTUQdVvc8MVdR0pDtpACMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4HRPBZ3f-MU_MTFxlSNSOmv91jhH3_uSAqHNkNsLr2qLDwIUMFJGIE0sHUMaNFYmTLKcO8QcMBWWIrLw3BZfny9rCzk7BB6uXLBiSHbqTmjW3hwcNNw-qt-whQU65RcYYiZKcXgW2f3AUASDndjiJIvLEdD0pQUd5ffxEGHCHrcHWY6yWHjKJLbrBmPVOsAUEjt9R5fXtCl5j7d8gdoAWxhXkZhHq6SgVjJRnfoOX5HQk5TViACtB5vgia-4uuJUoYKLCrpi6-dqcveFfYMp7mSW3TwYJX0pbYa5JQPtY_lkiNHSy3WBZL7_OLtTuMUxBH5zE2TxFd_mIZ9l8LwZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrgphBSi9AKp5VCvK6TugFi2mob9NcykTV2FUuonCtEd609d8DqbhLjv812INRuka2dZnksg5r_rx_xcSPpNxUvGP9T-h9e4CoD5Y_6wOVHkn9-JmbnBzPsb7TkuV5tOw245-6SvRfkB2rXfQNLbQqxa_J1V5f1-ixG8_1piKknSg6M6pL_vjg1nNlJToQL5rk7CKuJuw2c3knsf90RyC7vFOUG6JRpBuDixiUclnH5FzokylaYswexL7PE_IppsytFyhlp7YgQ_yOK4AasvJLkC_LILGbWvFnObJKWEQ8sj91jm_A2-wC9QAwzPedKWvwUipOQiRok9e-3ZqSBtBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UM2BybxYEIsXQE4GUqZRvqJNNjvPpCA3tNE6IlYgpMK1mQxiMGFydMOOY2PUoNrGJne8AsIY5gYlOWjpbbEWEFPsO47ng0o6KxTWWlZ-aS7Iof63FegPwqckKx4mitPgLH6WBsFqrNGe9ZaLLPkT-cv3UCoGtqiarWhrLkKsy6pJPw2a2Conn-ATZ6BHurUqXd3-t2O3yI56XoKYT17K1S2Q5CGpBwlvFq6gBMmEuTRHTk4ADci8cImA7pU6iG0_1p8eg7gLaj6LP3SBElWNIDJhHeVchkoEZKJ1ekrtIFheYrukc89Lzwc-sCKEXElgZCqAU94Iu9i-RSVjPoov4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ua6ajS-hQYl2m4n3TcRx9OOyMsLP-iPx_FIDqDfR-nL-wW1ueEeKUiP73cGbDSb5QZvGSol6jbWJd1E64boFHamPN_kwZTc7FSM9sSdK7rFQsyrqThvW7oG4OGA_5J6V_5O5Z9rYsNb1PYm1Zm3OtL4Y7ESzQtva1kZRU2ael5V1dyKKsU38FoWICyR-tBa54pPAO6QFprPLxKfjX2Eew_n8ELeukzYLuxFhKiMhAelRrXklc-JID2Y194DO34T1WjY9wJRYzESimsRGtQHw-fuzWv7u14ZmTV5TlbYG9-aDew9jleO8oSY3bxQkvwdt_2jt0xqHNccQPfGYJO7XJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXrPFWlm1h6l_vP3qXGmHeCXtkijp2G6M0BIIALSWxNUz8UXoX4T2BQLa-UjuphHmkg_MwdqJsljt8RZ-lvARdsixXS6_ZRqBgByafk3MV9Xi-JUdvOea-TGVOJB-BfV5jN7YOvElOLW6rPxIuyYtraSsdwkLyDWBHqMys7GquurVz-m34V0PXVw-c9eSXBDGdJnP4hk60UJ2hl0H7oOIi34dB-WZRbftChU_5L2PEFuTITVwYOPe_TR2l-FltV1HjyBa2c-JkpINv8iUc33bxzhoqOFPWCYffaIZXtWveicOUeL_YOu1zl_ogEzPZxFTVOVUhNMv_mYfK8Hgx5gwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9bbC888XqVwQonGDM3AuhSFJSC_KW4KC9GiVPl1KvqixTzoHmPkfGIwbSnygq41CYdFb04H8ctF2Tlf8LHwFkK-usyJH7TLeQvbtGgHInOvVyYrWq7INxIXe6okmhTEaud5WdH_hlcol8Y8f0BBw4XaBtokbs2melZcjXcJN_ySasx3ImwMjshNHi8h7YMUGCNY_-o3zJ9zUpdDfadtQBG8UBvYHajFENDAyHXYOzPs9Llf5b3I2Edog1r6SqgsLkpYiEnDWF5fuLNonsuTG0agB4N2K-_wtYi2RcnZNrZ2SjBg12PVYq4U3UsmKms8831pPEsoUaTi7M93aU9Mdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NwTuFrymOUR6tq1AXumwqkiipBeYNi3i6NYTh9o2CyoQO1DwojDm6DoQ1ZsoS4aHlUw_RsnJ3vAYmRHOUeGJh5ephovIcyyEePaKkHL0wZZKWQYcTxg8I-3WkR1dvNqj3OKctSoSnv_5oLRGhvIzHbtDgmU7IUewQBTeA5L_AICj21vB8zCU42b8aEHJBWW_ieuaBD7h2mlTjne-6uvvZ6GTwlDjTmwEi_MiquLaPv2-9_gYBT_oLgov3ihOFVvXXDK4xkoZo8kfT7i9aIt5-ShYtRc27b4G391VsB6GlUGYa7-Ak-n2bdVY6TAM97Ubb7kYROJaYccu2JkgnWoa7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUIN_Go9ue-8iUnzZIeEAM6A1jGFMwm_D9csQBaRA88lDFHkBYmzmnv7g7-bJzY1MKnNdhDyZgEw2W380dpNt_GHNH5qBPCi2eGUHREAYwMLP5gBwUf891iiB5HlJc5LUP_Bl4L0dpU3usFp2pJBFBuFjBh0sclfD5362uNE2DmsemXzFRC3G6H440oK-hQPvb2NkKPNMedlKCYu4oR96LNxbvy768h8U4hpabGktIf2nckAbdQruq3ob127iobdA9EsO-dUdSrgKWr_2rsXSze5Sir7Wq91MWFdQtMyNfhpSrmKpDtxKng1012XhFwZcG2XGoJ3XW8NfZwX4sJs4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=k159YGfk9AL9Wh8HqEY5nd_bF_rX9MZSMO1Qq0p7Qx9yhY-7KtIxdBAT8k9zeMdcfZPYL7AqiMFLfOZILgxJArZVpq67fL4rxhhUcTD35njB-XFrFGqAX2YFy8GvGCkg5byPde8m3RIvGsDKLQUHcR6hIZTh6KVmPsIE9YPdni_7sCOlZH5tRyBRv_KsqXT_zVYxwU7J1j-cv1qaSwhyuEU8se1BOElYYQNz0VVlaj0x0An8wDzo9A9q6muOBgWdKOAV6j3q1sHDEfo_XM88uw_sh8CGWqiOmT-jtphM-rOpVo5vZZzyRAOEvxMUxeimtdOJ1dZg5S7A00OGWK8TIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=k159YGfk9AL9Wh8HqEY5nd_bF_rX9MZSMO1Qq0p7Qx9yhY-7KtIxdBAT8k9zeMdcfZPYL7AqiMFLfOZILgxJArZVpq67fL4rxhhUcTD35njB-XFrFGqAX2YFy8GvGCkg5byPde8m3RIvGsDKLQUHcR6hIZTh6KVmPsIE9YPdni_7sCOlZH5tRyBRv_KsqXT_zVYxwU7J1j-cv1qaSwhyuEU8se1BOElYYQNz0VVlaj0x0An8wDzo9A9q6muOBgWdKOAV6j3q1sHDEfo_XM88uw_sh8CGWqiOmT-jtphM-rOpVo5vZZzyRAOEvxMUxeimtdOJ1dZg5S7A00OGWK8TIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9xCab-SSIt27VJY7iDwDZ0Pv1W8qcvKu2Ua_fBAOljd_IkkPgfG3ikacZ25K_zoFebYHpbMAJcF039LjpEukLze1_sNIcrVLwbc8TRKFIsb4J06hT_hQ-n9vkqNH8eXzdz1d5FGEA7c5tjfBp5IpBm70Co-K6jiHNeXVauO9Ez1Y3y1pHrqu_-q8Y9RIucbS8p6tZ5mQiiQDyTh8_sviwAqVBuQ5UIVn0o7wCfQKyw9XC0vQle0p7b2EXr45QNe0XWPvsCTRTtRgKa194unOOnPcqqzU-EG63FxwLCY-T9Xsw5qdSMaHvha5_2oy4QXifGAvMeI-mrUtmMBWxpvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lw3vlcgQl_EZK-I3Vwa5OLcZVjZo-E2o6aoJiHerob4SGe0BNr8xWBNcEkh-wfyPDpfIdvyWFOvQqBj3pJ2XqMfRV1FhDSYBsiFjbVKiKGoKvbyty1OMuNkX6i3fR--QmnW3OrZAR4MP4VUrpAcSUgh72wLNoh4nCTSAjUnNcnL-wsfSL7opNPGBp2Bb2txloHBquFWrRJDfzL-s3Uy1izkFSYWdN5suW0O3XFjUY0o7UopNWr_kv71gJCt0JpSp-a8hXySfzEihBAT8VHPGLsm4q7TkGRUQNPJMoAPUVqyaJrhkXPNwb4QLdQ_FgrUOyXRYuf37BVKDxrq9EYO8dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUXD35_zblK-y9ZNtpWqN5czEMkG3C2tnUZHrnr0pJ4QF5eYcTbgRMRvGfD2EC_r2t2wkmvMvlzQyK7l2Ec5psaaL3QRCtwYz87YC3kOFS3AXET5OCkacjKaqnQQaACP7TXX_JPDBiFUroCYJba5rCK1j_dCdFf2Wb2QM6ckyZ6Ygnpg26MjeGUIZernfFXVGThPc3lP7irMsIXZz_XkdlWy-cN9QDijwB5oU5n7fpE3sHRYoNnbmEYjOpkzJSvr0kk00OsnVPV-6Heelp8EG3NH3ScxUGl1zu_1vJF82EAkKLX6vPUtcVDUCt0oW2VA_RtJvZo-ebVxGbl_OqttWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0qLuduGKd2a-UF_OmDGS9Xr7KtUCqeqm49CkSEcWgw3h3e7IycUofUnIAx0yXwSJy1FDs4wDaJR9REEJPTjkw9F6-PstUSnUxXlocIcUkp3b6A7mM7oPw_pj3KfmFtkTF4lL6l80z5mIcbpDHJIFQ2w6fKlYoYjGCSArNJRRy34EMuKbD6e6GBtaX9Cq7Wn6Pd0LMGUNp5bbkkrtXfoHPKzINid7I2AkFFGGRTFYVaqmD1jbJSm3RV1dgTB2q-gNrPlamEbuZ1_sgP27EkF8FMiAdJWjm-KeUp2i6xp7-ChMebGajtd2Wl2SdSaLg5Y6Mxe2Ntq8sPs5gu5hnUFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksweeEGxl0e1Vj_KmnqZgzkA_4tG9D_k_9EU9vv4KQj4GM2ZjJSOajJz6nTg9t7VZ5a1Udt9DRCl5ep04Sz1GkMHRjfjrKFQxnTyxfwmdgrHSAnxtcgZbkdVoVsLgG2EMdILyHVQcqiOTnNiFlLDsn54M-u8MOZx6Eb8OyP5dQU3zmy8sGcqZGbSiRsgTTSQa03fdaIG-XDSZFrHjpVcDAj4IMkobbH5hZOjk89lRT9f9R9Jg5ciWUG2ARicq4b4hQbXv-4DjBDzvTPLa6x3UEvlPt2wx4nfPryDzXZ_nFiU1OMtQhUtTUrnUBesjhI9JZC9Xbz1ZAGU1GpLBCbVig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNfbFqorm_FTL5AyjI4JGf9TVo01JzqTgIcvCs4ATSohFAGRfHaWRuXZWwRKkE9cQA8KiEZGINoYh8FprmV7Xv55lgF4l3h8PkpMz9FyknXQZvgyIXAE1g-jXei9Z3q_UHnqnifxzRVKGbXO4qRlXdRboBGT8eNn4fW4SWrRzYpYpowOIRf4cYHwGGkKrPJymtXURRoRvf3UijAMqOtUctg8EQyWmorz0mYHr0f0mLdO8D7rmq1xc14GN_WbRJyvyeHVtmHx6UsPRUo0Vm6LbNhTIuF6Z7Z4kHUm7Zf4pYkoLlkbtvoOMTaC-s1ypZQVBkzTj6L-EK0-SOrS2akQfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nKl_xYdR_6Kp52mTqtVNsKhXTJS-KTFdZvxIFKm-UEdYnERSWTI4805b8J7-XPZ4WBCJ02ncPNv3xhJ6k11Ogo4peE5aaao0ZO-rPTo8mhiEAlHg_iqKUze291253pwEL9zhk7dd_Y3doTI7Qf1RJ7-iTdpARMMjyFh0efITruiCwfq-yvE080FXAHLtdtwtdpEcYe8q_OJW9kh195Y0j0FYuCMN_90-PdqbTiGdRpkC0UPmDrA0yivvrpbqrpZ7sCenYpBckLivrfd8A_aQpYGPBCdYLs7wuj0g5DQOVS0lRmAHJUggB-b57NZWEJ9s8risAqAQySkuKb7dm5CbJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hS48XQGJE9_WjoaDTJuDVm_zzNiOXSCyhiUAzrmNfLDNFf_irW19t5Pq4fihV0-AvBPVKEzk6ZXNj12Lnfeue4EkV026dRaYMxUcryu0OE-y0ur_aQX_28ZHwiRPmurIMgFH79x86ID-ZVz4_SOh8t1VkKsAGhIKVxXXmRtm0PvBQFxNaxElGxmcIa8iKibH2ixlF4Gv5_ZLRC_HcYvRj7BfOHl1QYrmwqUt-XP5fpmtuaNTeVvSO9rsWKIItc-heR_KL9Qgt9NwRivULwWXgzhyjKpyN0q7T2AkDLkpJOaRtYaPHIclVC6J0FPyODGR9xzcUtHL9HfcBnzehxryIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OztER832tkLIppbxxyt2bDuGoTqoF70cWp1ZQdpOk2fCXD7DdTKuKATlgYZjMeQGmM9iptMJde9tFNnsdt025A-kO9tvrwaBovJZ8lpfg1XbQ2XAWheZQKXcxIOpk8pUSbS82UbhI6GEzPYQxNsoE4qjyY9mewugYiFdw1wZDm6mAFLQNj6ehWmghdBp10nZNQjwFisFKzPgc9DGnNnEJuzF-6Q1JhpVW2jSiT-fN5kX_Nf8q0VByphCOo_8lYSdGxgehy54fzBxGjxX6stsUBlJeZzeI4cZQrp5psIlVHVVdPNKfzzXo3FhfiRZS6RuZWIwKKc6Y8_J_fHhyv1JAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #40</div>
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
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZawin2aOopwRQJX0CyNRoktKW3fD2-AUaQ3lsvk-a6G7GCKEaI1lG3nOizK3MbIgJUxKKMHFHgXUlaXgXHrgYVMNCh8ZcEEeWRVEvkC6dxwOyRbLIq5kiQwSZkBxVjBc5CZpe5OQdwKckG01KKDguq_PidKaDKycJkm-fWhfBWqzxfhH5iBncKyVJUiWKsr5kSzguo07rXPVgugAFYD3mx50wFo-tzQstyaJvaJtjk1buIy_6YVy6X-a-pYbNJ7Cis5kFDDSdgHs5_8pX18KYsmeejthuiwHoBaIplhO7WHyNKG-NVkymYJe5nQ0KFb3raA0qUp9crYBFHKuwkwTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrldDFLqxnJZ-kwC6N4LPnTCRr24zAdbNFUTh65VHJErPmP9Kfg2uO6DpMYVArwCmJX3YMJeutlz1qoZ-FwqDlZxIpxEP2XmvEM1Yb8zZFHNpK_caERKwMUHHw5juxJg494EES8XrfrbvSoxrGkSx-m1XedXTXUGIceSiBa-Wc3ywmvz07gypbQPbP9M_qnBjZM9e-U5pDhFSQSyp5h3TDLaGjDqf0h7SOVlj6kkcdpFtQK4cros3QXvoa5So75WXB_LCBUslYYAY_cnokesAtKPY33I20gq1-dYv0IPSWROJqelo6FjMczeXCY-Uuo4JZkDdKMucf2YKqkftV59cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfqizP3It10R6MORhOXGDjJNNfvk0lMJYhPpNBLBcVGFqbQDNcmCv4o1LhS1dH153E0pDpWR6e54A5pugPDYBRg0VgjtTxzVcNrLy95_wVtouZccQaoHOVA0E905tM0imtK1bdCoRQlZmDQ-4sndMmIgbLCT6drQqeL8Az-7_h15upcD9_sk-f5zYbhQa_uL2jNnjhamtTgrCmXj1lNH0BautPxKGKMV95LkH3jwhzXqMwe3zZui-DSOuzU2VeHJ3iq-YWG1nc7jjaq_HYxNKoDzR5efhzZiHFrnwl_c1iBzGLFV-YGQZXTTuK9Ti9gtsygpWtzadRjqy0dlGJySmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st218zFykM2BLPFjtTOFUO5ohvmaZ7tbOpBVb2_Yu9hf5gdtppdClhwTs5gIdxTPVRPHCl6YK4SFZ4MOq7x6MKHBsgqdTXD9iyehPeK694CG2otn6CoSFIw3bctfbFywSB-fv0OKkvDHNqL4jXLi8BDcxJmth6Ye-mveJ_O-ubKA2KIaoFz1JwRe5ManQs5EkIQDXnvyL9wYl79X7SY2ez-qgV9f32ASRumx7unGOJ1ZjuS8RPtCC7lKSZhjng8RV7CMy5vyYEQVIMgMehI4WCmj1VicoJs5eBhzRqkB0WXWaYZG3xpeOiH0qOFLOPkvgHSCFq9Z-nZs7_PHSws4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OFezsReutWHnb_xLbKay6lwEOe6guoHPyPHN0e2h3RPLjEL2rCwjWynwNSuuPextnlTQOfmYzBq4Zq63yMRyKZI-Qfuwy42oELPV2fq2NAqSJVPTGTi80SNKinwIxeO04D-Lsjae9zDAuThYt-4GwOAuCF01qohD5aHVnxM0j3VT-oS8kfo5jhBo2piKxOSUyiuO9060nZdHY6m7HotvG_xeOjVxv0iTjP8C3SCUuWKh17DPvJ2F860jPGnI9BTXDE-471Go9x2gBOMIWJSYWMS_9owVfEZE5AnoT2pKsw3VmeWj2Zs2Fd-olk6UbWQAUQ1HCqiA5PbQZewKzbzbdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdFBVxhtFut4ZDQMqw2NiV1QlJDLkL2TuzbQyCvbJfaZLivjtVa4qKC1qRi-fZVWTDUy03Q90H8ZDCQnU7146Bg28XRRZcuJyr1TgnNgH_8K46ZFLOvn-WV14h4h6IZN7k0qZ4om9UbUiAQM-tUhMJBPT_sCB_AG5KXpHaZqNVUqhUOG6eiixVYSY5U7awtsBt9ECZ0xA7lLBvZBgpousaN0fHobae11YPRhzQ-HosrE9PL0YKvtNJ7or2P8xB6TJE20MT0QMRDpNuH2Uu8ZrNzwdbS2uU-DytnHWQUATTvVq1UYHqsg__PoUJZYDCsCr3yg3Z3tRmVVrBoPQqCODQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyPk3hSAF6-_H5sEY4UFEj1VHiEZRk5pfEloI6pyTDFcCNkUqLdhC9IPNRSJiEZOS8LFEb09_-G2lpS_5wyV2zvtNiWd5j62MgoN0kA7Amj5bO5jN6fYs3oFmTnKWAdJtrEiMGXRx0_9ZHYTP3yxdJbMVItgBYMhrF79kl1O7DCa5BorU621Jk6qm6zJWVlNFyZWblx8LYQIHiU_S7EMstFR1box8YC7kQift6UVhlEECe2XY4pCyPFlTUfGchRyRKFtLuR0MWVsflK-WQeQLcLiZbTnr0dV9JqMVL57gD9vX3Y1yBfzfZFDeGna7fr4HohyzJLxJFCPhXnxp1gaRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCxJjs6B9Ww3Vi3K3N5Xhi0dyS5FYqcFX4THAUV9_rFycs4qZF3aL1mXEuWXKrvNnZy3Ne5GiPZ7GcndEk6F-gIrymzY3sB7_039Oe3AyBLjpm1wyZxEXmevHJWj4lmnR8hJW_JisHJ05nBor7Y54-10W_OmOLd9WWhK77YOaoF4U9Y3bLnlAGDt0K_wt2luF-w5RnJXXo_Fj3GyjI3wxgBW34jpx5nbgPlFVuA8PS40g2W4pUEe8UfBpTFnU5RHanrQDbXbXuovtJ621ktid8rPXJKHuS7FpZkeGEKeVqfB23YFYpkVan6tDmsVA-erIP58SCmKD0B39ewB_yo0GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DveGsYktlGfF9XSkJ4r_PXx7DyeoPdlyQRqauxXZ92jDTla_hzMSQAjYa4qxy4wSxeTCDhbXAwS838MUnTNM-PXX6wMvm1j2Hw6-wdwHFDUQfND9lWFCP_DyjrdXmJqTal10TE4n9xTvft-HpDfZwK-78SQimdjrDnx_LyUK4dlUVzq17tSN7BctyNm1W5tQEYv2u3M1OEGlmPqBaKeuavRIRMpUwSPHK335Sym2OoiF4cJii-_ub4RxXwpWiAv3X-CurbRhDuCojGcO9Dhar-bBXxveABR9YbUODw7ns8sNKBq0hg1HG1h2tyR2whdRJhVUzcXHKuySI3BNPmPsQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soe_Y0I9y2WXcKlC66OyF7HK7Ul2tO6QETC9UisNVsdGP7d92Od5VwEQHLXgjWi40la2Wh6DQSKhs8lVyKGmF7ozDQTET-aWGu_U0YXyzPrrAlM2AoXAqH7cmf9c18vG3h5mc91YaTh-r79qbuFu-1HTWr_-WVAkpG-7RerMk4SgqI71lLnoF1AXmqbAKukTrvQcLgtEjvye_w1_BTnsJ35bu3i4-euVa-btgix7yPOHslJxkiOv8krQRSkLWrSo2CawNpGr2DX5-0FgFcjEfFdb4IABmbLm3KTzRxezkyD9e7gZnbI5uHdlax_XSCTfTwVnXJhmPfnauEL2aqsd4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/INfm1ySyVb2qwl__CwLnXWvvx76OhT0Bfld1fnp_EfyxA6Hcpl2R4osxS0xJ_P6KEVelPH_Ik_ITvRPJfJmPYfmNzzxhNgsJiUdVFJpGgFm49ekRiiVoM7Hr5IvGLFgxCkIyxz4p1di8HY5jyrvaKkSYrWN6cadxpu0VdlhKz5VcCHezSncpMAyobpw7ckmGXZ8tla1e1-DdkrOV8nhvm7M27a7TfhGB9dQNRXFFAYaIn7fH2Z5gYIsBDpYuWJd85KuEhhm-d1kTkkid5krCeJENAK5vuj2n0v0RkaatmO_iWMA7J9_nQ9L32HQOWFRoGwstrKalPwCDEWe5yCMBCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sUR_719Q8jXn4INPTqya0Ef-fOvngpBk-z5wJTFI5SOqBvXmo9Z8blpgUasjDM91m2KQjQTNMh7ZIRvP0e0VYcMp2JOCzrUHy0WkwoJZI9oMGEPkSOdWArSxM5i11ar7OrwLbE35OfY0P2In9xmmjOJZr2ilrtjpQ26wG-HjD8zzWge8LCUtdddk5Rh9HgQRhImGXvRiDiGE18Yr1K0hZajVIi1_05snKxbgpcuSmwVwo1kHpKUtabMUPZKBPiDPX-akYCTsku5ppY-CcO9YIUVIGsoytPBPbseFKTPNeW4dn4MwJkZnl1G8Km3vX8q9cAcRDp-8zIbpIE8Kxj3ZeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c66fIcpHpVU_x05m3fYUYr39W8k0QbRFCg_Q6WLRxSG-nFxnnNjIFdSKH1gGoi9BS4nI9n0s_nJxmmNY7So-o--GPgZaciOF_j32eDlLwiq0dD5to6Yn_fkr1emgELn12rVsdVuDI2L3nzempHBPyZuQLOHYz-w2M5rggC7_BB2mOUpNzRlnm3RXA1XsM5DYn8zaLCaKrVfAHg1rC5LATeOOtJjnmoTOJSwWJ4SlzDCxi0XJX_XRljodwfyTNf-6oMWqJz3DCaOmserFeAHGpfOrwTTX6MYGv531nZcDohkqLphZzM2giXL6KZK3oW4kvKx5sxh9MTAquTkn0nZayQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghTh0PLxlFUIrjJUWR5kEW_jWTw5HNy1xbMWl8IcYFSLkNmiRvVjjOs-cKrkwNWS2wDEpr19Gn9e00q9ATfaKPAw6Fr4JMTd_KWlFTWJxCttrVXQSiXdRZRr5X0_yyimFTMDxo-LfDym_0CSOoXnO7KL1WiO9TiF1ni2WuxX9EtBPXyCVCKjYmNpw1erlgHbz6X7ovm1CYb3U2zaP9aePjdCJD4PU0fCyVNLKj1sDHMTaU2LobCJbweBQBcb0E75eV1KoKPnU_YSC_PSUFWHcpG8P7XeiAtjzrNh6wYU3PhnnVGnBB8g2Roe834i3G22CJqgrIFTRuqjUnHG509s0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYbZGj8p2dZBZovuJUsr7-am7a1YKBcUq4pywj4bv0ucbJzAKZ4_fLr3FAQXcnr6doLQmti4QcKZErBc8BJYhxsESGVhHjFu6VbINsY-6ukwzcUHPQ4ia4u3tKuHS0rOIY3KYEPI8wUJ4P3sGGoufE0aDhXULmQ3yShCEhqEe8pO9OlYyk5bobXDkEY3J4Jsge6BE37TZ7rjqA64laXnAY8Rw5jsHMTuR4mSeeQ9nmvYaSCFCq45920EY-LY8KA6wDpejyDLZJd-HCNnc57IMqX9LJPsz5I_IDIxvCSf27OPD9z2TLqqmwM1oIxmXTOg3ODGk7XqcJ0R-i4Armymig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwqDWpiRN9tVYeZv563WDAzw7AOyP4HYKfv6NS-mFmMtXNGW3YgG8qIMTtHBWBT5D3ANDV8BZH12_ZQ_G8GQfyzf6btP3StrX9KUpGa7Ru4WBuA8zevoqyGpmQp8EgAMzyLv3IhsYqFR2ttBfScrU2vWjwX2UGN0CPuFyoCzZ_tgVLOEoCe_a_-WRaU4D2DaXEzfL0u-KsSDvgQUqQdQYO3wPV2QFD2AK9YW6Np5i7stNEeoMi3YZ_vrYsitbeF4lmvZaP3p7NAFlGKqb9MZOfXGpQKFrDVAxZwd9QTLIlnUw8v6tRJP1lidgG5y-QD3TL0nHxD_iCbbNbkcmcsTVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3V9LY0eyoR3hGYBA-fTBliVMS3-LCf9pGQmrveuvtHbw7e12fhHkNGPVjGpdg2s7D2Cjq_zr8TkSFc6PB0Gz2B-iJFTBbfPvMNLuSvY2fxK6q1QGdhWjIr0i_7G9KY-Q68jSnHi7F0lWP6uj3c1zug9qOAcgOngwsY3pTmcJX0xZu2UgDOijRZ2cukkMB0_fuZjv9uuycRXJUN141PPmlyhW4tobzOxtyLd_heGSCJKVBBj75Ypu9_z8VnFJHKfp1E7y74geHltW19FE7ymMGK2WGNR-Yfnwz5tllAkVmjri2xyKZFhSqVTcQ7iM9px3gYuqSeejIfoJt1tyQKtGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXd70imkTgtuyaAG58i6MUuo8l2C01zITJmkWiTbYyjVo1z9tEq_Ch6ekD_8jKodA12MBRtFonKsykGb3DokD69FvVoHIWdKlMtYPmUgqfdqOEACj1DwTcIPnkhQJuFeRyH5oicdrvFBnAHx8uzx55IHm7O4S98CL9iIP4yL06qp_krjTMdOR2JFAbURzDSg-jFmqC_IzWX66ypuZ9J9GmQgpwVV1vyWMlZluBTVuh28Bf2H7m1nuxD4iRRsFyihCHJO5IeafgBt1X6vEeCHB8ggK1tNWuOmiP_rDyDyl_a0Lbm4s9EiGbTnS62c0w3z09XtWcRCs71YJakWC8yRLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lA837HN0HeWHF8nXpRHJ1p_8Pq1oTwLG4Ywat_ijro0nz61M8hKb-BX9j-14PbUFt-d9izI6N9EtRuR_Ftl5V46eaPp1Wuqvt2Qjo7gEz9B2L8urDjtoYrYHoVC9DOVen0QzqiGkA4NgMB7ICJnJJ3NlmGs-JR3oFE0vH0W-8f7mRZIJzLvC5epzA9ob2lBQzE4fyxLjAbp92d1GDiOMFEwfhXZPAqMVE1nJ72p53pIco1Xw_PNhzVzWFfMRVPVSrTJBfo4rNpBxvhvksTtMs76F7bFxkTBX5V-uFaf5xxXwt5GP8J_xkRBasG8N98kYhN-jToNxuWg6Nyc5RnP5GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1bbhEll3NRKqLfgbIGSe47uy2OiAAVHS_CPhfDgkJGomYvkJ_rbJTV96QmDI6lHooxxPU03TjVk3XLn4s5FbuYjbSF4_IVm_A5jeAHQu8A7P5n3L59FtllBTKCNBnB9GR27W4xQ5o70OoNt0agfPDONmk_az4gwV4m0-GBGsFB1YMGJpFhB7SNmHwEJgMnor3S9GX-vmsawYTJ73OJHXUAuVbRKfIgKcXCgAwxYaGzk9e_voNIszAlUuAu3j96Q17kGlp-LrYjo6ujs8zKP2Imip1f0E6rzC8D_j3Gmx6ATu-JWgVdcUL8Ec94T86BDzpfYj1PsuyAE-xhwBFYwuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0qI4NAwqTb876LGekBNqQjZXu5GPvDE2Qm0M2P31JNmL0l06njlwDYIA46rbfSX0LyGKA10YOgEFquDgFsETv7tOrbwX5GtCanpNiFJbAyEqgCakEACGKGZdGhY4YbQoiLE3jsPFPN04Qwt2aBzNODRQ2VbtvgF6TV_v320AULecE3_G0n6M7w3LoRHM3CJY8VBiXbyrerpl7u7X0hbK3Eme4ImFYGer895o_nr4YPcCpeSIe8SwqkW1IP5JaanGcxYCQlNW1LNDrJXqPLeeHsHVg1O7OMcawPRevrQZyUMMUPKAoS-RgRf3ofqpVNFKrZ1TenTk7T7EeeoRORytQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrB1wcrURyTGa1XvkyH1-OkNcQOOupUnIvNtM2uPrhjW3BMhpdDSVCZmAksRj0Nr-3JiJv5ungHkgwYQw23prqT_g1vhQumKk4WbgMueyUmFpb7nd7Kzl8AKpdXSojrul30xfwd5ezLHGXVoTVu0xpxJjCuJFUlufiANOe4cDu9h1FBrvE6wv4JAwJHII3LoKw7NR7uJwWw2-gaHyeZf_Xt3cJ7fYRBIByjnPCu7UjPwDQ00eon1GwnspwEDjCbX1n9axIhirhOQof6aArkhx-BQGwvG_QM1w8qZQNjkKPkHOz6LKgqvgZil2J2V0SdPQIczP5zQ39jEFYN-HF5BjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxKRne6IB_qFlgP_WSmGrbAa_j1P_vOcbPdzfUqjrujhkAr3Aa-_zG6Sz_ev7caB-khaIsatwxSLt1IpuS5KYl51u5JmH9vg8gVRiQs3X8Yd5tgC7IsrijIBVzwjpLBzo9WWiZxs42PCB-70MwSA__dkM34lFHoYMecJvfyGtcyowgSWH2cZndaNFSivJEQGU-pVRq7o_4rs76pT0UqoYkiR46j-iy1KkeH1GbJpadMNRFVlE9WcW5NK6ugM3_COGs78bPYcbaN7Q9ybGFvPtBD50IFi8zi3ATXqHHeh-dS6eDepm0PkloJHWMAaU35fvWb84SDYu-gBlPRn71G8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ho_0a7QWXkQpFEprUSWi_w2nAu6aCtMNEVEhZWAPv0q5d3QfQoDKdidq9MBDa_3oy-3NMKk-Wbf36R6l-LNB98uXrm92Jw7XXwldKUTaVGRh-Te06ekvKp1OsXzu2lxcv4Ea65CmKQEV_hSpqt6NsZpqJlflLYn2FrwmtkwElzzfYK6j-EfcLhyYFLAMG8jgwWu0M0HJOwvoKyDxc2StiFnthWI7Uq9fEyMzdQTW-sVtQamx_SmQXR9qMDXTT3tKdbwqEjJB2Q999laH8EUcf3gX4uipuqpSI3SzOOT-Wh0AsK6kPlzlOgv4MWnbxbhy_SvdRxa20G2cU_zKu5dIsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn-PaHIrTVY7BV2_RXRVFauWhnLKUtzA-AFydcXtve46rzhjEweArYe_PPJRy_38mVbBIZJ3k7xwdgFNRMduazREMbLVNbanlDTWxaI1Gwaj02Utb34QMfIFcSb7tsuyW53u49ECRwJXpBbnbqWvFGs05uuEKxnBtzRDU7hW31sdmGYEbKlr1xJ_V7pu7zfL-QorU_AnczK1STOJS6wULAyoTdq2Bu8ASI0mG6nwnCL2pxzCZEYxcOHeXnBZWyoiBQATtEV4EPwGPinJgQKazx1n9J7zmb5covIjxTZtt-9Yxko13y4CUbdGhdz7xgTrrGY-foNim36BxpvJ-AZx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNhLeoWcHohdr3571Z1y-GcNPkifaQ4P3enSZb1aB7EYNMTLSt27w_y_TkL_elupI5mECI2jymBBln9un0ux6fvhTMAp9hMpeTB5SJ5odYqh-ks1iwJ3lSoQEArpcTmFDaeRsY89Jw7E3a0qc1a_xuP4YDqQFOJFwO_c0GOk4a6lLFq5dPuJ8Rr6dKZgiS9cimLJlx02un9gfCWwzKIboWS2dnovj7dLd_D_c7LCnN2IPRE4RQEf6ZBgGeR0PHmshT9sm2dWimkCjgmHdnwuuFEMWv3d2rXDnLfnvaSR3JsdZfsXZU8mKnFv5b49UCrbGxXJ5IzBrxeGaQPvZa6nSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LVx4zWJcOnNdRXyh_CZvX0Zc6WhVyY-v9wI9f7tRCC3IPda0VSulaBETFzzhkRCwrt2GtR3xzYgWzhArlfU0m23Jw61nct0RMFEuJROqrOPOC7YoR-QpmjhkiYrH5YXCMtlxr9CoXgq4UBEb-9oVdvvUy9DOpZWhvzIG1pjchifqzQfCIJZZf68FtpvsSsJYqgAyJbVIjyqzoIKtik3ekyf5GoqqMiaRx_oURM_PnceYij3P7eYufWoFaNwroeo4nfu1M7sl-XCuUQFwoudfgO_cUgsMk6hTTUBniqrcczkPQVQDLh00sZktps9rfClBDJhIeqfzFsmvzbEIMwvM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvzhiLaFVikEAVDOO8mF6_rztcHyev6E8u7Tn-hRAah92RjGu3PctkTANHp9eZnC74hbGhIpaz2-M6PHBP-NScrwetW4tcMhu926YzSrT9ZnjgqYIw12dNKxahKNgRvgfjYjmBs5RExyDnOweb7QyJs43MK4G0YyJQmHitDVmIjOJJU8XCf7ehYFghNadPKFe-TvdESoCd8gBFo-aVIySv9HBaanX2QA0CgxKBBVJpXc91MDTj9J8bAsVR8VX-60c23kcbdD2CkAqVYtyztdMo21m2cbJdhAoVAXsVZENsw9YcM7brhKUOFKG4uw53gqmLbYGZrEkfpwVF63oPfsZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lro0VIloQiUg95dwuQwQFkSEIWCsJkx9JNqozmrz94ACllzj6LuxCTwNZyjBeWPgKNUcK3Xsqini6hb8ti3A6MlTf6w9SegSBuUlsftqdxx5QnvLvIoyTRgG5N_ocurgTfWUT9omPDJMj-djVtseAIL7DB3bEj_t0xEQZn8DsK4IxZ7efABu_By6ixRj7RpctuvRXf3vQ9IDW_rSaGNVEi0xiESjU54xDYKt6TmYvXidyUR5Ble6rjwtsd_cucg8EZzLLRZuCCU0HaFlnkipqrXosryPODZ1uJHWbnstFqI6ZOKrboFc0k8rGsjtvaQ8HwTihRJkwlsOQPQlQhHZeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnNNCYtq3QZrMCRIpyNXqOagPCIRyY6pzYUJ5HModIGzW4foH8hW6eSepmDGqnhNLElSNK4tQkBLLpqGDHvRC4TX7eLy-E4iBTPvn5lHxT5oiNo6uqMdcJawoQ5coDaqQpUd5_lt1DAUsSuS7Aq84wziT2OQjbD_H6wsnEIt5ubUw2rjpnTjmeYbW6I1HVgA_ViRDGBy5bWqoiDgUSGupntaoMmar3KUq3IQ1O5c6azhzM0hBg3qDHq9koWp2rZ3UKsFSNc9Wd2zpGoecF2h7IvzfcrItL8Ql-seBAVM052ecyBtAT7hfIIYo2XvnAozX7PGeDbcbc0OgWmyYpdfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ic0ktPn1Wzkf5T1nDrFTaB-AqEzdEfa6KZ2qJsnmX1ZilGPEbgYDnkaBy43Ij1-0jry0oVG5zEW_x6iHqUbuQ4xfkyz3cGHbLIgaXylVFnpiskStDrON3HbPArPNhrxbETQFZAx7geVIYuUVoFWy3fi7On0MTzO43nsvY5N487FVyOsu9juMQ0nEkEba7GLgc7BLDoh-ro2kZOfD3uIHfR1A3rGCmE1yxa1anZDdWHGtZ5YT_6yBcIcTs1vhM4NANU-fk0kzVOK0nv7ZOpp3NX4v-vieZrelvzzUUktJG_MimH8AMGqFMR5ALNBpsL3flnmWlnnakVhlYRQ4iWvVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GDUdS40C577nBaQ05YDw9bHJZpvo9rXLyqfdyWP6SS6ZSxbQVE52Gw9IyWCzjiacGCvEUQ0qvMp0VVS1_ddQJBmP2SP-ssGsSoNsFW3tWw7zferHGXFMM_hmSMVPBY9mCqLXmmx_1SjS2wP6uu8nt00ir11MLmPgjMb7IwUbLHmpVhA60V4Z-YVA72yAGu4gWGWd2ExoA8YZZH7PsSgcFr3Zj4DC8PjUsm9FU_x7QhqE1YSw4aD9IDSVtukQL5-KqxVVVHCAoDa-XBrnLNMOyU74WTKBJ-H5FOaCPp66xZMh4OWdAR8ra_VPNBzUSXa5cHR1ogxb581lOIFrRYarfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cw7H5FPP87A33Et5oodVZhTFyeUf2loi3xgCmCxuRysYgJv_1v-E_dTY4deiEQ5Inoh8AoiWeETmrVNcTtLs_nMgTvc8tiUMa5tiD2vWEeqWz0CjMYEA7Thy9Vm2xaqYHg_Sf5qR8bj9gq6S3ftjjz-Sd4jaYz5kygV6Us77Ncp3x6168TaEb_b2jsq9CSJsalfEOr4QxHMFDcsJpIldBwzzAqs9ZdpzeTpo91to8CHVwvay2VAH5cyr0Ah5rCSt8r-O3TEvkUqBFBmQRaaDA0S7462TtpGYXBOKq5zFhw0_foRcn0MUD_A1REyu7LgihS9LyNJuuVYytYuWz-yejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOvrMZLZYpUWd0GQixs50wXNTXDDpvwSvDblK7EzP0vYjCxagdH7uqKvaevtWnSwp6aDPPDkuoONSmCqN1FhIHyFh-ZvH47tZS7zaDovJeVzUZzhfPz0LTLFe1eOrkGTy62CzgB8qJ6C6a0of8JwwxhQSO94X3S0kE1MqJbAImW4wdyC-Gq9dZYMnidk91Rcyayf9lvU-sUPswo3Rq_jZqu1hn2k28RDHGNE6tMevbnlqHvov5zlIgYRmMildOWqKz-Hfyydlb0CpbbkKzwI_NnRFRbTQnRnrf-Nt0Ky_TM-tk3MUq9czxpkUlFg22wBFzR4rgdtIE7oCjTGga4v2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
