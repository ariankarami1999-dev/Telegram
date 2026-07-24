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
<img src="https://cdn4.telesco.pe/file/iAxVfNDfbUhAPEbjiIMNtdLkwvqpQHsCe0S8vEat5uo-iijOSsuWHSiq4GvpfneEbRlmUFO7yGEftEiNAO_iR2XgfkdYB9ZPThUSwqJCEVLY4h0tXkvca3AuUU6J9hzoWvrayX6hDOZeeoilcw31Tw7I_m4h9k0FIJ8nGOZOdZFOjDaRv6QsdaW_ClIl_cBpinRveKR5B09GvVcGSIDljUzHuGwdGOQL-VSkwL5d-ilgxI3FgaAf-yVYQgLmynJySXAk6pAygGxPLEFHUqtJcWoyCCkAmBaKKvxU9CL0RILHTv8vowh2fo-XsHUcEMFF3x2vq84yxCI4ZbJZEdb3KA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 931K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 03:26:29</div>
<hr>

<div class="tg-post" id="msg-137366">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTgGkRDBuLyxetuq5laD1XaEL4bTFh7eCI1cB1_0POez7meckMqzeOe_gZg9c6iDNgHxG755DPVfRG5hyuBkjjKaA1mfrHi2e5H5Zqlb1piQSgnAHkwB37Embt7sPMawC7BLqq6xItzt_4LLeSH_hoDDZ1542Z7aCGfhyF883AGQzVVyWiDycV0atZD8UwXo3qW25BV-VzQVTz2qFeFvT6m9pUVQXqMx0c5-asqLRXZaIJpeq7gRZNOeY9Exu-8q87-1Fh4s5Hi_DMBWH0lzCFUqcVCkJy6vmdj_Y4dE7RoD1feooOYJ4syuRWdlLNKBYpdI_MdpEqwS_-VU_4Tf5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا معتقدن مجتبی خامنه‌ای، رهبر جدید ایران، نسبت به علی خامنه‌ای تمایل بیشتری به دنبال کردن برنامه ساخت سلاح هسته‌ای داره.
🔴
با این حال، مقام‌های آمریکایی میگن ایران هنوز برنامه هسته‌ایش رو از سر نگرفته، اما به گفته اون‌ها، رهبری جدید ظاهراً آمادگی و تمایل بیشتری برای توسعه توانمندی‌های پیشرفته هسته‌ای نشون میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/137366" target="_blank">📅 03:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137365">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66640af45a.mp4?token=kSgNNsm87byclsghNccbgH3T5ZkqF7EIbwb5_H4ICVJ2pvJ-OdcpTeH7z0Ysme6jZ24ocxxke2CY_HIFtaSfLviNF6Ygg0sHTQmWCyEmbBdWxfoUkgRKj0GCYjwuTyMlMS5YEhpnTWzSCesUAKed8J65Qmkd7BdpxjfHCLmt0gGKxDA5xRQjv06cf3D4G4bRVdTrOhb6ehCSYRgIiIe5f6uFRxQZj2UkmYMQ1V4vg-AViYLD-ar5la6LtVXWFGza9dlf5d4BWw-Pb1fxZrRQUT0d69kLWFZmxlPlS4tqYTLEQUzurBaZSkYM17cD3wptFKUJJ9RiuO--zQ-zq7-yqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66640af45a.mp4?token=kSgNNsm87byclsghNccbgH3T5ZkqF7EIbwb5_H4ICVJ2pvJ-OdcpTeH7z0Ysme6jZ24ocxxke2CY_HIFtaSfLviNF6Ygg0sHTQmWCyEmbBdWxfoUkgRKj0GCYjwuTyMlMS5YEhpnTWzSCesUAKed8J65Qmkd7BdpxjfHCLmt0gGKxDA5xRQjv06cf3D4G4bRVdTrOhb6ehCSYRgIiIe5f6uFRxQZj2UkmYMQ1V4vg-AViYLD-ar5la6LtVXWFGza9dlf5d4BWw-Pb1fxZrRQUT0d69kLWFZmxlPlS4tqYTLEQUzurBaZSkYM17cD3wptFKUJJ9RiuO--zQ-zq7-yqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لشکرکشی شبانه در عراق
‼️
🔴
گویا ساعاتی قبل نیروهای وابسته به جمهوری اسلامی به سمت پایگاه آمریکا پهپاد شلیک کردن و ارتش عراق یه ستون زرهی سنگین را راهی پایگاه‌های حشدالشعبی کرده تا پهپادها رو جمع کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/137365" target="_blank">📅 02:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137364">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
فعالیت شدید جنگنده ها در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/137364" target="_blank">📅 02:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137363">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
چهار سوخت‌رسان از اسرائیل برخواستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/137363" target="_blank">📅 02:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137362">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید  زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/137362" target="_blank">📅 02:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137361">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری/ هاآرتص:
تل آویو می‌خواهد تهران را به حمله پیش‌دستانه علیه اسرائیل سوق دهند و در نتیجه برای پاسخ اسرائیل، مشروعیت بین‌المللی فراهم شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/137361" target="_blank">📅 02:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137360">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
شرکت هواپیمایی اتریش، تمام پروازهای خود به تل‌آویو را لغو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/137360" target="_blank">📅 02:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137359">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
عوستاد: تا فتح قدس یه یاعلی مونده
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/137359" target="_blank">📅 02:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137358">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEK_1yWkKkGMeTX5WuFiAQ6_iVfuahFw7WJmn3IZ25ckH94VTew2A0lI0llZSeXCbFcndm2GmKsRENeBCpD8uM8hhrZjYbLugWsJuLWvbE3BXOZ6lrDa5vbW1HqXlWetljQcRfOmN6qwBzmQ6lQ0vTgHFO5XzMf2nDr-wvGAlEIvevqGp0a3GZKp3zddgOW8lqRAFFMBpbr3cm1zqHtGcQvwyhbDz1TDPbkec-Vy414VNdaWv8oX-Q9CCl_w4P4AVo5RVlmUaj77JBzwNk6S53hEvf-N9YkqTnSPDY2I0Q_QUbrxPZlfbFJmxRySZk4aPgBC-q46w4ofag5TEfiHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد: تا فتح قدس یه یاعلی مونده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/137358" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137357">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
شلیک موشک از خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/137357" target="_blank">📅 01:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137356">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فووووووری/هم اکنون برخی کشور های اروپایی در حال لغو ناگهانی پرواز های خود به اسرائیل برای فردا می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/137356" target="_blank">📅 01:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137355">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hect9TDCNky-HB2rXYcqOA1TlFhpRZXY_pdL4fUGDiQM8600ZmmJ7S7LmtqNt1BeAOGxuhc0_1SxmXVf8RrlwkQzM-ToBcwRSZ-pNU-mKWBLbW9wUVemBQfFIUCW4IwE-27h3FP3hRZQsoePYe9vr9ZcMEwDCYhZVDlhPrhV8zo3xBXpzQWUoXONZAQ49LxxqGlt-WaN42Exl8p4hPAe82EKgSIVqVTSSDTuwclnnNUjVzDZDItq7glK2J6VyaSy6nyzZ9buXGWLFO_zhYJ3JKSnWMDfOrexOVv3_GWdD-09D3ug_gB1DGWgRTHj33flj3BuzsK1UgCJa0TdcGsoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای ارتباطی E-11A BACN نیروی هوایی آمریکا در حال آماده شدن برای برخاستن از پایگاه هوایی شاهزاده سلطان در عربستان سعودی است تا ارتباطات را برای تیم‌های حمله آمریکا تجمیع و هماهنگ کند؛ این تیم‌ها در حال آماده‌سازی برای انجام حملات احتمالی گسترده علیه ایران هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/137355" target="_blank">📅 01:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137354">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e29cb2148.mp4?token=eIBTus2mcGQku30IvVl0KunvXKIf3dmecgUVboOx_HY557N9YQgx7FisUfR7n24jkM8BfxHKePQmjKHRr1yPlo0T1StSR0lBdIUNdK4MMR3WrMqmR_W3CwBkfgaZ9paznjSCLSA6U33p7Xru3kV5rreanydGdEx1g5xY-Eik_uTziHxKgb0tEdstlMsZklT2aeV-KvAx_yXqNDyhz5wiUzX-4yUxDajmekYF9b5C4fCJ4sv-O1VvJdIh0DACMsztjx7JwmhHb3gOjhGNXzzCxuis6mfQr4Ml-yfWebHOTdVz67uId5WnFo3f1RJULWCHd3fSNGQm3uzw9reP5ohTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e29cb2148.mp4?token=eIBTus2mcGQku30IvVl0KunvXKIf3dmecgUVboOx_HY557N9YQgx7FisUfR7n24jkM8BfxHKePQmjKHRr1yPlo0T1StSR0lBdIUNdK4MMR3WrMqmR_W3CwBkfgaZ9paznjSCLSA6U33p7Xru3kV5rreanydGdEx1g5xY-Eik_uTziHxKgb0tEdstlMsZklT2aeV-KvAx_yXqNDyhz5wiUzX-4yUxDajmekYF9b5C4fCJ4sv-O1VvJdIh0DACMsztjx7JwmhHb3gOjhGNXzzCxuis6mfQr4Ml-yfWebHOTdVz67uId5WnFo3f1RJULWCHd3fSNGQm3uzw9reP5ohTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این شخص ارزشی این ویدیو فرستاده برامون و میگه حرفم به مخالفین حق هست بزار تو کانال تا ببینی
🔴
جوابش با شما:
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/137354" target="_blank">📅 01:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137353">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
خبرنگار کاخ سفید: سنتکام گزارش داده بود بعضی اوقات ما به ایران حمله نمی‌کردیم ولی میدیدیم که کلی موشک در آسمان به طرف ایران میره، بعد می‌فهمیدیم که کویت و امارات و بحرین و عربستان در حال حمله به ایران بودن ولی به طور رسمی اعلام نمی‌کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137353" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137352">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری/سیریک رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/137352" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137351">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd-ANm1gW3vuWm0NHuVjv4JiY-FDqPLelKbNMGCeumXx4g2FX6Sg3qVcWasvo8B9dhZhkIp2tz6rC1LgQ-xu7Q8JveUNX5J6k8re1GdinT48G_cm2YU0ibTmkRK3w2H-Omz0HBjDWdmUO-dJPx6vYz6noc_iO1cvg094lV_F3onYhCuOqGiebr1cz7nU-Hu4Nawl7rm0wVLZbdeC_WQmbyCbBf8KE7MmbMK7couKgO-cSqy_yPKfCDo3xAdaPIT3FuEv_-7l5qQGnrgw0u-GOJ_mnvgnYkwJ_yDyyr-DgjbxgbsaH-DI34gIxmpxOvTsrg9by6vvokGeabrHEJdgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همراه اول قیمت بسته های شبانه خودشو 3 برابر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/137351" target="_blank">📅 01:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137350">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
به نظرم یه جنگ سنگین و فشرده و حداکثر ۱۴ روزه در راهه، از لحاظ شدت حدود ۲برابر قبلیه و ترور هم زیاده. خداکنه به زیرساخت نرسه اما احتمالا میرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137350" target="_blank">📅 01:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137349">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: هواپیمایی اتریش و شرکت آی‌تی‌اِی در میان نگرانی‌ها از تشدید تنش‌ها، پروازهای خود به مقصد اسرائیل را لغو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137349" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137348">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq7Pit73x2P6yJVTgbJ_VvXLpcTBZ_yXJ1qt9V6vl6mvUz0cFgsov_zANxVxUHy5GK1RXY0vDsB0di_XXzsYTqD_ytDJvsmmF5fPl9G9HQtwClsebDvx0h-A9eOT2dpSuQs2I7kbg_DdZyknTc5yJ_69QwDvgKQ1kWdjWfYKM-vVrjW0fVlAGMaOXzZXJ0I45G3ZOJbW_tIw_Do9sx9wcdXXTuQBgD4FfA_spQAClTrDH7CtWWn-kQuS8x078ghejMiRR2Su83Nnvf7RXastN7EbGATpowu_-7A1NgLmP8FnEaPOgEz_bnbzRnufaZKJT7ELN7WLcBct_SKnSnOtIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرویز پرستویی: لعنت به پهلوی و همه طرفداراش
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/137348" target="_blank">📅 00:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137347">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
دقایقی قبل یک موشک به پایگاه آمریکا در بحرین اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/137347" target="_blank">📅 00:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137346">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKR0mHZWXvlSZljtq_-yHMWPpVRr26UYttbTSNFlECOPu1ssNNGPVoItSBiusdCt672oDSy9z8m7k1ovjJmHeE1SqlykuPKXt7lz9cnDRg4RvqrkmzNeinr6NdrJ4BsOG6oVa0UBii8kj7QVLk6PbZsOyHWJtBSgAWvrsdu8xjJuHJGwN8rF1WNfUlX4bDOs_IhRwvdgoY8oFmC1Pv-Kl1OG0y1VpTrKYyf08bdpc_Sko_JyD9F0XhDb8CtTjEMuexyeL93IrSilKGsVclBW1HK68EwnB_bmZFnbeMTEEE6CdvtwTN1MDs6t4ooisN5FlnydGP0E7ngxXuA5tIWaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: یا مرگ یا ارث بابام
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/137346" target="_blank">📅 00:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137345">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2479a179bf.mp4?token=K0XnH7_0cPdaXCJZsguT8G6OgRY8JtvX1zzDykymvifm9Zp9AfvL51nM3QahQQInWuyNQLV_-1pvD6zIVo-hdzIzrfSDJDBoU_HIxn1BbZkJ1NxIQw-EA4X8CTji_r8nEfyMjkKizTE4rmALDO2MlgK3HAt4ipM0pStzmy83q518CxT20vNWyKl63AJic-SMwoEpMCKdsUuJPeTNQVizeQpFuIBuzL0ugTUz4pfLi8GT3tM_Q4m9G8nhgrxNALLvXODk-H85cU15TE4k2KuPTQxA3MtgmbvsERw1exbpuupjdYtorTS41EvhbDQwTPTociRFD2Il_VioL1ak2AQ6Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2479a179bf.mp4?token=K0XnH7_0cPdaXCJZsguT8G6OgRY8JtvX1zzDykymvifm9Zp9AfvL51nM3QahQQInWuyNQLV_-1pvD6zIVo-hdzIzrfSDJDBoU_HIxn1BbZkJ1NxIQw-EA4X8CTji_r8nEfyMjkKizTE4rmALDO2MlgK3HAt4ipM0pStzmy83q518CxT20vNWyKl63AJic-SMwoEpMCKdsUuJPeTNQVizeQpFuIBuzL0ugTUz4pfLi8GT3tM_Q4m9G8nhgrxNALLvXODk-H85cU15TE4k2KuPTQxA3MtgmbvsERw1exbpuupjdYtorTS41EvhbDQwTPTociRFD2Il_VioL1ak2AQ6Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی قبل یک موشک به پایگاه آمریکا در بحرین اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/137345" target="_blank">📅 00:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137344">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
گویا سفارت خانه هند هم در تهران تخلیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/137344" target="_blank">📅 00:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137343">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مراد ویسی؛ تحلیلگر اینترنشنال :
🔴
تا جایی که من آمار دارم تعداد جاویدنام ها ۳۲۲۲ نفر هست. اگه آمار بیشتر هم باشه اسمی ازشون نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/137343" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137342">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4lD6V2jPrwPlpHtAZkYbQBF46HJNv7ehAMpKh_HUZYrearxxQsMbdOUpzQpmF7U42nq4km7bsgmIbKK8Ufind-IAONumJtAcbu-nudDJBgTJDVkifF9vHdb0AxJJKEYa8Ay5_mpDv6JZ0jWh0MgsHDpu4TQlprzVMOvL8lG72Fo2VUShzUgeq1DQ5t4PVbyIxOtUuXQdHcaA_s38gn-VLBNcqKlMC3Z7-9_PYLcR4z7O8HaD86IUN2LLTnucWEBvJBO-hGjorGprO46FoYM2LhcKYzz_XpnqrhHB-068oXc4zwHlLoVZpDi4i0Zq_BV3vQ1Hlxy6rbKmo-vX6hALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرویز پرستویی:
لعنت به پهلوی و همه طرفداراش
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/137342" target="_blank">📅 00:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137341">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ائتلاف از حمله به مواضع نظامی انصارالله در استان الحدیده خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/137341" target="_blank">📅 00:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137340">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=u_i3QOy7C41AjOdAx8uubkmLbiXWeVSGnnEhSE9zQ1JnfkHSSswYFcJWPwq69yuEpFlft6JJbwmRpMooAkR7Nlc9FkPmHSPrJVEPEB0hgCuUcyG6vKozLWElAqP8FSRmEA9xEQsxZeOX4RDLI0dGmFETBfT2iIWUT4fS1nNZ-SrrCBldgy450rWk4YxkEZOSMUR6xB_S6YQe0Ycrf05zK4q9KaU5tN-NHO5HjhGFU_c9IIkXwmf4tL9wz-SOUChQcwDoQxz2fqzk2o10YfTPgKS0mXt8_3tkSVmZjUELCRyJHMJzUnWpa5bg3DRw5M7GAC-RiNV0uJG2ivUR9M5dJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=u_i3QOy7C41AjOdAx8uubkmLbiXWeVSGnnEhSE9zQ1JnfkHSSswYFcJWPwq69yuEpFlft6JJbwmRpMooAkR7Nlc9FkPmHSPrJVEPEB0hgCuUcyG6vKozLWElAqP8FSRmEA9xEQsxZeOX4RDLI0dGmFETBfT2iIWUT4fS1nNZ-SrrCBldgy450rWk4YxkEZOSMUR6xB_S6YQe0Ycrf05zK4q9KaU5tN-NHO5HjhGFU_c9IIkXwmf4tL9wz-SOUChQcwDoQxz2fqzk2o10YfTPgKS0mXt8_3tkSVmZjUELCRyJHMJzUnWpa5bg3DRw5M7GAC-RiNV0uJG2ivUR9M5dJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آژیر حمله موشکی در بحرین به صدا دراومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/137340" target="_blank">📅 00:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137339">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8mLzRo_iYaF-17W7AtfyPoNP7BiQso5FhGSEQnWjf1GSCHEw8X38Cw-YVV7TTMb2DBXD-AWQiT6hKQz7zxiyuxCDtH9xkkrEaeYBC-TRZg57HprN1hlWvQazvaByvuLRMfp7KVyqykyLgvtRP1sprUO7yLfiJLzperH9ohjnjn39dcJzcfwM5EWLVlX6pl_Sn0G8d6wp1suif5KvGZI31CE2RBobBTiXjUkm9RoAXc3IfJXc8LuDpxLbgX-sThOpwYKL405Yo2TFL535FDfZhlS7VqeNrLOWv8R1UeX6P2njBpU8WNXoCISw2Vcb4CCzNm092h6LpM5VLwGKm7L4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید
زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/137339" target="_blank">📅 00:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137338">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499b17bb9a.mp4?token=EqpkphaNHS37P61bMFCCcF9JCq7EbNiQclFHg8FAr29YfGH0JQy_qDrpyeM5w63QFRfKxq8XS_46f54xdc_F-JCAiUUUw0Ciw8xGneSTrAdI7RbO6Jv3NPjUS2_4Ssg2c-DrNzXuYgE_Ly9BzVi5D45zr_e3GZRfLKGPnAVdphhFz_SYTZx-wJ6fG1sXTmFMb6amheEefxjCy2BQxKBKocQ6YzC4MggVyxj9WBkxkOKwXn2KPgXQWhBYmxkUPMDd1_4dopdemukIzQA1k3QGzJVocAAQQqZ8Dv5raTWLKOz1AeHRZtmJdg1W1DyQ0I9y3-eEyw4Oq-QPDmeqTncxvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499b17bb9a.mp4?token=EqpkphaNHS37P61bMFCCcF9JCq7EbNiQclFHg8FAr29YfGH0JQy_qDrpyeM5w63QFRfKxq8XS_46f54xdc_F-JCAiUUUw0Ciw8xGneSTrAdI7RbO6Jv3NPjUS2_4Ssg2c-DrNzXuYgE_Ly9BzVi5D45zr_e3GZRfLKGPnAVdphhFz_SYTZx-wJ6fG1sXTmFMb6amheEefxjCy2BQxKBKocQ6YzC4MggVyxj9WBkxkOKwXn2KPgXQWhBYmxkUPMDd1_4dopdemukIzQA1k3QGzJVocAAQQqZ8Dv5raTWLKOz1AeHRZtmJdg1W1DyQ0I9y3-eEyw4Oq-QPDmeqTncxvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیروزمند، کارشناس صداوسیما: تا کی قراره مجتبی خامنه‌ای بیرون نیاد؟
🔴
مجری: تا نابودی کامل عوامل جنگ.
🔴
پیروزمند: خب اینطوری شاید ۱۰ سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/137338" target="_blank">📅 00:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137337">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری/هم اکنون وزارت خارجه آمریکا در هشداری جدید اعلام کرد:
تمام شهروندان آمریکایی باید در برنامه‌های خود برای سفر به خاورمیانه تجدیدنظر کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/137337" target="_blank">📅 00:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137336">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Djcxnx2FT4FeDY3xbWMmecG6DI2zp5R8amD4nxE-IPNx95sA1ekG-DOLqIjP8bY1xkLWEZng_JUrwLOHaATG-yzkUQkGYMssi16d1lMSYt6wO8_7Lhx091odx_0Ll7FzEYIbhgiB49eN4dpkGA-HXERDuvvbIX5FkhvBcUbiQB2o7Ri5aOnrR_e2kAw77pOBTcQgVc6Y2crrKDYzeu74hJsoMQv56KlwyjjPwJlqJRJQ8dzH0xolDGat8gUBSyd942LgIXOc93HmY8gHPZNKo01SXHxpb3chV_-hGwmHPUdS4K1oDlvsGnV9FEZZ2AcB2_Wz354Gk0CB39B6jZx8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارشات بمب افکن b21 raider که جدیدترین بمب افکن آمریکا است جهت عملیات در تهران به اروپا منتقل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/137336" target="_blank">📅 00:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137334">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نیویورک تایمز:
مقامات نظامی می‌گویند بمب‌افکن‌های دوربرد B-2 و B-52 در ایالات متحده در حالت آماده‌باش کامل هستند و هواپیماهای سوخت‌رسانی هوایی بیشتری برای پشتیبانی از آنها به خاورمیانه نزدیک‌تر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/137334" target="_blank">📅 00:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137333">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری/انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/137333" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137332">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bd99063.mp4?token=vMXSxnmJ8MriR33WclsGAr0JZmb5Ff1D2lv91ZQJ3BqvPLKqVTkSeb_ZaUXPDYx4hnWVaOX1_aT7UluzOdQU-Mc7E2rTW7lQ-EHVwwfTDNECCxgdwBicrrbMdB-B_rbQvUdqH2aPLe2Me5drXGNfE0F5G6E4RHMQygqUPhZ847ZfgYfKNXeMsnl6sFtR2RAUmNNQViRft6NAAhJ58gAXyxY8_g050TNSzTL3ZRLK_pLv8Wm7cSFt1rrUuhDayMkGu38Q0yq3vwwomSfEmaKEqDViplZC728bbArbBl6ie0EFgeoI3Gh-5-cVT4GGhwEIdXhPSBg4eTm7thgaxadhZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bd99063.mp4?token=vMXSxnmJ8MriR33WclsGAr0JZmb5Ff1D2lv91ZQJ3BqvPLKqVTkSeb_ZaUXPDYx4hnWVaOX1_aT7UluzOdQU-Mc7E2rTW7lQ-EHVwwfTDNECCxgdwBicrrbMdB-B_rbQvUdqH2aPLe2Me5drXGNfE0F5G6E4RHMQygqUPhZ847ZfgYfKNXeMsnl6sFtR2RAUmNNQViRft6NAAhJ58gAXyxY8_g050TNSzTL3ZRLK_pLv8Wm7cSFt1rrUuhDayMkGu38Q0yq3vwwomSfEmaKEqDViplZC728bbArbBl6ie0EFgeoI3Gh-5-cVT4GGhwEIdXhPSBg4eTm7thgaxadhZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی؛ تحلیلگر اینترنشنال :
🔴
تا جایی که من آمار دارم تعداد جاویدنام ها ۳۲۲۲ نفر هست. اگه آمار بیشتر هم باشه اسمی ازشون نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/137332" target="_blank">📅 00:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137331">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
خبرفوری/جنگنده‌های F22 آمریکا به عربستان رسیدن</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/137331" target="_blank">📅 23:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137328">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34fd806b7.mp4?token=OUSTERarqDk0hG8W4421y9kGdAKnN7aknSyMJYwun82jhn9EaA44hWMhytbmK6qe3ChARjvECEjMPQFjzWp5Ro0SVHcd2IvhYuCYCA2qXNyU3bP8Ew-Lv_nMvnPDOgZ7Bem3unxqjZLo2XSs5qYk_2frX7rrJPXMIhrtzMxdtOVtoXDrdAmlesdKjUX4VG9JOAEx3UCkvv5NFhrTABGtzeUbwH4NVvLJsNHhfgZIa8Cn00Rmhf3XivzxWfDn2EoVCTMA7KO-oz6k5YmCrzJh2PZBH_goiE-2BpWYvRda9n3_yGPar5fOBMWIPAnKj81ILoAxU4zRnGjhTMexJ4bcVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34fd806b7.mp4?token=OUSTERarqDk0hG8W4421y9kGdAKnN7aknSyMJYwun82jhn9EaA44hWMhytbmK6qe3ChARjvECEjMPQFjzWp5Ro0SVHcd2IvhYuCYCA2qXNyU3bP8Ew-Lv_nMvnPDOgZ7Bem3unxqjZLo2XSs5qYk_2frX7rrJPXMIhrtzMxdtOVtoXDrdAmlesdKjUX4VG9JOAEx3UCkvv5NFhrTABGtzeUbwH4NVvLJsNHhfgZIa8Cn00Rmhf3XivzxWfDn2EoVCTMA7KO-oz6k5YmCrzJh2PZBH_goiE-2BpWYvRda9n3_yGPar5fOBMWIPAnKj81ILoAxU4zRnGjhTMexJ4bcVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران گفت: اگر من رئیس‌جمهور نبودم، اسرائیلی وجود نداشت.
🔴
ایران، به شکل شوکه‌کننده‌ای، شروع کرد به شلیک کردن به همه در سراسر خاورمیانه.
اگر آن‌ها یک سلاح هسته‌ای داشتند، از آن استفاده می‌کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/137328" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137327">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ظهر امروز نفتکش عربستانی NCC MASA مورد حمله حوثی‌ها قرار گرفته بود.
🔴
خبرگزاری دولتی عربستان سعودی اعلام کرد اسیب وارده به این نفتکش جزئی بوده و آن به ادامه مسیر خود ادامه داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/137327" target="_blank">📅 23:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137326">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
خبرنگار: شما می‌گویید که با ایران مذاکره می‌کنید. چه کسانی در این قضیه دخیل هستند؟ ویتکاف؟
🔴
ترامپ: تقریباً همه. جی‌دی، مارکو، خیلی از افراد مشغول گفت‌وگو هستند. این موضوع خیلی مهمی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/137326" target="_blank">📅 23:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137325">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_hDO-vWutDEOx2hCi3HqYIs3sBbBo-JHWI1R4MAqwtyKmuTArLBs3xIqefAJKmrEZ_Im6-P8XHpTkuJgQRRSWLIrIKjDpu4rdUg9HOINLvm8UkdoCw6rKXoIr3zUMIWfn18WPtIFUJlXs4nUTQ1t3CD0CDSnFvjh1g4IhjUhd_zDHbTEVlf27qn9p-7gml6RgWXMxA2w4efsT4TfXu_KOegyKRv3zmmBFUUwmCTny73YbcLD3NPo7he8_4hnRodPOlRxNzIDCgUTg0iCtqNI9NduwJb5ngqepZXvMCjKRP2CJqqKNO8bDiKoORTS86r0XLvJtn1ek6etaFvUiCgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون بندر الحدیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/137325" target="_blank">📅 23:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137324">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ : ایران، باورنکردنیه، شروع کرد به شلیک کردن به همه‌جای خاورمیانه.
🔴
اگه سلاح هسته‌ای داشت، حتما ازش استفاده میکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/137324" target="_blank">📅 23:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137323">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea64c7c35f.mp4?token=fu9WV0lpyqSuhX7shlmY2TPuMlyjqSJd3ORf5_xQnLhZ5FoATdMWBgv4xkgVg8reuxfqiqT7wJTNHxIaPWsOZ4hRN5ZXPA0xyMznu02vCO8bRMOAUZLJT3qTJdWnzHughN7pXQejM5XIo4PX5XF1gPzsWAZbXYT356U19rj4JOXQgU3p8tJuuPk8I36dQejxCQsGbD-efsihnbRgFVVi57BilrWnrEHHWqLIFrCoWF-HHAlvh35HhIN8oMwUHaZqqk6phY9JcLzCZzo_tI60MPpQncQKlDfmyDCb1Al2crV1XrJYfroVIGaQG0WY1wNr-XsSelr3r9bF9BQVP8XRFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea64c7c35f.mp4?token=fu9WV0lpyqSuhX7shlmY2TPuMlyjqSJd3ORf5_xQnLhZ5FoATdMWBgv4xkgVg8reuxfqiqT7wJTNHxIaPWsOZ4hRN5ZXPA0xyMznu02vCO8bRMOAUZLJT3qTJdWnzHughN7pXQejM5XIo4PX5XF1gPzsWAZbXYT356U19rj4JOXQgU3p8tJuuPk8I36dQejxCQsGbD-efsihnbRgFVVi57BilrWnrEHHWqLIFrCoWF-HHAlvh35HhIN8oMwUHaZqqk6phY9JcLzCZzo_tI60MPpQncQKlDfmyDCb1Al2crV1XrJYfroVIGaQG0WY1wNr-XsSelr3r9bF9BQVP8XRFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : باراک حسین اوباما خبرنگاران را تحت پیگرد قرار داد، اما هیچ‌کس چیزی درباره‌اش نگفت.
🔴
وقتی اوباما این کار را می‌کند، اشکالی ندارد؛ اما وقتی من این کار را می‌کنم، می‌گویند اشکال دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/137323" target="_blank">📅 23:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137322">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
گزارشگر: چه زمانی ایران تسلیم خواهد شد و واقعاً پای میز مذاکره خواهد آمد؟
🔴
ترامپ: شاید آن‌ها تسلیم شوند، یا شاید فقط به یک غار بروند و مخفی شوند.
🔴
آن‌ها غارهای بسیار عمیقی دارند که می‌توانند در آنجا پنهان شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/137322" target="_blank">📅 23:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137321">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رویترز: چندین انفجار در مناطق الحدیده در غرب یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/137321" target="_blank">📅 23:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137320">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری / حملات هوایی نیروی هوایی سلطنتی عربستان سعودی علیه بندر حدیده، در یمن که تحت کنترل جنبش انصارالله قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/137320" target="_blank">📅 23:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137319">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ : وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند.
🔴
اما دو روز بعد، آن‌ها گفتند: "وای، این فوق‌العاده است.
🔴
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند. بازسازی ایران ۲۵ سال طول خواهد کشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/137319" target="_blank">📅 23:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137318">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQPTuQ98b3WpOJMUkFqQVywYtduy8xCFKStgKTKM1LfV4U6v0FlQF337HCbG0VCvyYKtaOCdniR8i9pQeqhv3l3t5kPPVjc0Iwexwr8PPp3FPJhTCBL3AjklFA_YqG-B20arrH3OKR_rD5uJRoutcWIDa76yOWlf8s7Pg85RRI_xtvITmixyFCVE3lhkLXinCrygCc67xTwDs77Qr8vBbfIPPpXMHO2S9E1XyLhHjxLNhBvyt7dNuSpxB57SIgvv9yTJNSc_fu3fLCFhFjjiL7N81UOsTZf_uLiJLXTxxVamIxVVGFYtfHloKlKuR1jObOoggz25QgmB-myRL4-_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون کاهش قیمت تتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/137318" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137317">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ: هنوز درباره اجرای حملات بزرگ آمریکا علیه ایران تصمیمی اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/137317" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137316">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ :  من صاحب مسابقات "دختر شایسته جهان" بودم، و همیشه نماینده ونزوئلا در این مسابقات عملکرد بسیار خوبی داشت.
🔴
بنابراین، من اطلاعاتی در مورد این کشور دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/137316" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137315">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5decfc4f.mp4?token=hApwYK4TTdDaa5Kz2hcdXQCeCCyNldDePnAkaGmNNJkQv9iuJppzRzzVFQTaCGWfkvo5iX_Gk1JN5TPkK9zZ3-c8-WL-CM8ASw-XnJRBL61O4Cf8Z68kbLo3QTN1H9UvKZrFKWeluKR8NAzkHAkyRhNnpfHb4liTL8Enh25j4tnMFEB7nNWcQ8f8XGYYu6JeY5CvXXtooHzyRDv4KSdnBMjgfP_aFIJrOiK6S49ex_rrHJy2DoU4fy14NgWlxsGydC7RI3hWSQD5JkuqapJyw-fZFJiYtao_qqXEe5OGRuu_raoirvHWKstDlGsEL-nEMGxhStwD-Zy-7q6VfNG37w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5decfc4f.mp4?token=hApwYK4TTdDaa5Kz2hcdXQCeCCyNldDePnAkaGmNNJkQv9iuJppzRzzVFQTaCGWfkvo5iX_Gk1JN5TPkK9zZ3-c8-WL-CM8ASw-XnJRBL61O4Cf8Z68kbLo3QTN1H9UvKZrFKWeluKR8NAzkHAkyRhNnpfHb4liTL8Enh25j4tnMFEB7nNWcQ8f8XGYYu6JeY5CvXXtooHzyRDv4KSdnBMjgfP_aFIJrOiK6S49ex_rrHJy2DoU4fy14NgWlxsGydC7RI3hWSQD5JkuqapJyw-fZFJiYtao_qqXEe5OGRuu_raoirvHWKstDlGsEL-nEMGxhStwD-Zy-7q6VfNG37w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ونزوئلا: ونزوئلا هنوز برای برگزاری انتخابات آماده نیست.
🔴
خانم دلسی کار بسیار خوبی انجام داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/137315" target="_blank">📅 23:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137314">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در حال حاضر با آنها در گفتگو هستیم. به نظر من، با گذشت روزها، آنها جدی‌تر و جدی‌تر می‌شوند.
🔴
من معتقدم که توافق، راه هوشمندانه‌تری است، اما کاری که ما انجام می‌دهیم، راه آسان‌تری است. ما آماده ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/137314" target="_blank">📅 23:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137313">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خبرنگار: وزیر جنگ گفت که چین و روسیه از ایران حمایت می‌کنند.
🔴
ترامپ: هم شی و هم پوتین به من گفتند که در این کار مشارکت نخواهند کرد.
🔴
ترامپ: من به آنها اعتماد دارم. فکر نمیکنم که آنها بخواهند من ناامید شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/137313" target="_blank">📅 23:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137312">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: همین الان که داریم حرف میزنیم داریم با ایرانیا مذاکره هم میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/137312" target="_blank">📅 23:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137311">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ درباره توافق هسته‌ای با عربستان سعودی: در یک مقطعی، عربستان سعودی به پیمان ابراهیم خواهد پیوست و برنامه هسته‌ای غیرنظامی خود را دنبال خواهد کرد. هیچ گونه غنی‌سازی انجام نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/137311" target="_blank">📅 23:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137310">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری / ترامپ: مهمات برای یک حمله بزرگ علیه ایران آماده است. ایرانی‌ها باید این موضوع را جدی‌تر بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/137310" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137309">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ درباره ایران: «آنها میخواهند توافق کنند. گاهی می‌گویند نمی‌خواهند توافق کنند
🔴
دو راه وجود دارد: یا می.توانیم به آن‌ها حمله کنیم، یا می‌توانیم با آنها مذاکره کنیم، که همین الان هم داریم انجامش می‌دهیم.
🔴
همین الان که داریم حرف می‌زنیم، داریم با آنها صحبت می‌کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/137309" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137308">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=nvnFM8VX9y-JEvePwAWV_sV_UpcO2gi1tSQC4YOGliHCsz0WjosV3qF3ILIS4JUtGq71l-4UIxnkZeU35BGEV_O8s8rNaJPpMaJR4L-RqwQ6CXXFgHCpo-IWc82JhDHdENr0V8rRkxjL_OfkOfH56p8vyh3h7nw6q7Yu8WEyhL8Q1zN4KIrrxQu1KaO3heuIk5t0bQDEyTRM-_7eCggAPpYJqd8iBri3W5bZA22KX8oVKaqeenUXbbK_LROF6xBWCvUGaYfUQw5UafiCMeTZR6kR2fEMEx6-lsQ3tVx5GzOx2sJXE0gvuTrrfOCO0HzvczU5thYDUFmTbZ7ouRWqmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=nvnFM8VX9y-JEvePwAWV_sV_UpcO2gi1tSQC4YOGliHCsz0WjosV3qF3ILIS4JUtGq71l-4UIxnkZeU35BGEV_O8s8rNaJPpMaJR4L-RqwQ6CXXFgHCpo-IWc82JhDHdENr0V8rRkxjL_OfkOfH56p8vyh3h7nw6q7Yu8WEyhL8Q1zN4KIrrxQu1KaO3heuIk5t0bQDEyTRM-_7eCggAPpYJqd8iBri3W5bZA22KX8oVKaqeenUXbbK_LROF6xBWCvUGaYfUQw5UafiCMeTZR6kR2fEMEx6-lsQ3tVx5GzOx2sJXE0gvuTrrfOCO0HzvczU5thYDUFmTbZ7ouRWqmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شما دارید درباره‌ی منفجر کردن نیروگاه‌های غیرنظامی و پل‌ها صحبت می‌کنید. بسیاری از جهان متمدن این را یک جنایت جنگی می‌دانند. نظر شما چیست؟
🔴
ترامپ: من به آن سؤال پاسخ نمی‌دهم. شما از کدام رسانه هستید؟
🔴
خبرنگار: نیویورک تایمز.
🔴
ترامپ: حدس زدم. همان نیویورک تایمزِ ورشکست
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/137308" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137307">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهوری آمریکا جمعه دوم مرداد به چین و روسیه درباره فروش سلاح به ایران هشدار داد و گفت که او اظهارات شی جین ‌پینگ و ولادیمیر پوتین مبنی بر اینکه تاکنون چنین اقدامی انجام نداده‌اند را باور دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/137307" target="_blank">📅 23:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137306">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ : اگه عربستان توافق هسته‌ای می‌خواد، باید به توافق ابراهیم هم بپیونده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/137306" target="_blank">📅 23:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137305">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ae6c6862.mp4?token=WwW70Cp4eVGB1CwKenWyrOM5d6td7ajyoIJ5wggTV_rj7ntSRn5xm_36LJ4bPaotxKhfj2vPwqkfGxlWVMS1AWNK8owPLg-spfbNoVAemeAvAM1GSZHDx2vJU7nbB-uFjIy2ymeGPluSzOSJQG8X2ITi8uwucuWwZi-xGK2JUUEQFoWNs_3r9m0pGVEEDnDlo3Y3gftCOIQ-2pSJ_ZTfhH6D9l8vyeSEKCDVmu6CEX9mHO-KQ-K4f3Kl-WhDCX5PQ231qs4khUdPRFm7gT4cjaRdTUj-oj7_I3qo3uhrOHrMb_NKnnPvp2AiXTFD5H4sqEvQELaY11S7SgRE-UMU1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ae6c6862.mp4?token=WwW70Cp4eVGB1CwKenWyrOM5d6td7ajyoIJ5wggTV_rj7ntSRn5xm_36LJ4bPaotxKhfj2vPwqkfGxlWVMS1AWNK8owPLg-spfbNoVAemeAvAM1GSZHDx2vJU7nbB-uFjIy2ymeGPluSzOSJQG8X2ITi8uwucuWwZi-xGK2JUUEQFoWNs_3r9m0pGVEEDnDlo3Y3gftCOIQ-2pSJ_ZTfhH6D9l8vyeSEKCDVmu6CEX9mHO-KQ-K4f3Kl-WhDCX5PQ231qs4khUdPRFm7gT4cjaRdTUj-oj7_I3qo3uhrOHrMb_NKnnPvp2AiXTFD5H4sqEvQELaY11S7SgRE-UMU1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صلاح یکتا که کار آچر کشی و فیزیوتراپی در ایران و دبی انجام میداد رو گرفتن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/137305" target="_blank">📅 22:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137304">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
فارس:  آمریکا با موشک، یه تانکر حامل گاز مایع رو مورد حمله قرار داد، چون به اشتباه تصور میکرد که این تانکر حامل گاز ایرانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/137304" target="_blank">📅 22:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137303">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
روایت «المیادین» از فشار ترامپ به کردستان عراق برای جنگ علیه ایران
🔴
خبرنگار المیادین که در سلیمانیه حضور دارد،‌ خبر داد واشنگتن بر رهبران منطقه کردستان عراق فشار می‌آورد تا مستقیماً وارد جنگ علیه جمهوری اسلامی ایران شوند.
🔴
المیادین همچنین گزارش داد که دولت آمریکا به مسئولان کردستان عراق هشدار داده اگر با ایران وارد جنگ نشوند، نوع حکومت کنونی آنان (خودمختاری) را لغو کرده و تغییر خواهد داد.
🔴
ایران هم به سران کردستان درباره آغاز چنین جنگی هشدار داده و تأکید کرده اربیل باید عواقب حمایت از تجزیه‌طلبان ضد ایرانی را مد نظر قرار دهد.
🔴
خبرنگار المیادین همچنین خبر داد، ایران به سران کردستان هشدار داده هر گونه دست داشتن در جنگ، با پاسخ مستقیم ایران و حتی عملیات زمینی در این منطقه مواجه خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/137303" target="_blank">📅 22:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137302">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
بلومبرگ: ترامپ به طور فزاینده‌ای از روند جنگ ناامید شده و می‌خواهد هزینه آن را برای ایران افزایش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/137302" target="_blank">📅 22:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137301">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
طبق گزارشات سفارت هلند هم در تهران تخلیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/137301" target="_blank">📅 22:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137300">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
هشدار سفارتخانه‌های آمریکا در عراق، اردن و اسرائیل به شهروندان خود: در سفر به منطقه یا عبور از آن تجدید نظر کنید
🔴
برای لغو پرواز‌ها و بسته شدن حریم هوایی آمادگی داشته باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/137300" target="_blank">📅 22:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137299">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
عراقچی به وزیر خارجه پاکستان:
حملات آمریکا به زیرساخت‌های ایران را محکوم می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/137299" target="_blank">📅 22:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137298">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3crbVK2DXR0TXaiF9SR7LFB9ROueMVbFhcyDE2ioYoooI8EAaEvUfxopDg5a_9ChNveyjsiFuzcTuzx3MuShrizrW2njNM2QHfeNdVOq4KbYF0pJVA-pqtCq4FMJp6QQI1vyaxx5EljxG-fL186YYF4nhW8uvLUC4pbgBlQckmKlRUjp59S_c6PBlu8unngE42LZ6zXbk15ZdTA4FXuxVkJxLqcb5BB2M2PrxvzetQ6FJRNzXx76f3WMktGSJBijkNanNAA7OBnrNDYXv6wS7sNqJcuNNEUDLyuD-0VwGfdUpoP_DnTM7J4H2P1_IB0VKr_al8xRdIUXkWkim6FbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از نتایج اصابت موشک FP-5 به کارخانه "اویتک
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/137298" target="_blank">📅 22:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137297">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بلومبرگ به نقل از منابع:
ترامپ به طور فزاینده‌ای از روند جنگ ناامید شده و می‌خواهد هزینه آن را برای ایران افزایش دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/137297" target="_blank">📅 22:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137296">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3dORvbZ-UPqHP_hsGc5kk4lDWVW-8vcI9dtECuebvYS3S9HkpifuD8xIPDssaSv_XAe3g7RDTQ_aWOnZOhXDap1CHeuOGrAQeCXpt63TuBH1KlhoHSSK3zAvuGCOmnL42e3gZ8quqU83t5Mfb8kDcryVPNir87TKmvI0JgS1_1zSLJuf9VVX_zPhXdujHh5ZHE73ie2X8ZPGMKz0UlsYay9z6AcvcyVrRjKRhXyceomrgSw1HSI7SS1lxKCLFz9BlirAXAPQDSyR1Pv-e3VZw3Dcxk6-X5mtRjv6o0ZndkwM2umLRLdVa6BCL1dju_6NnfSiLXsW7V8PU-ktjShpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه جدید برای قتل ترامپ/ کانال ۱۴ اسرائیل فاش کرد:
🔴
بر اساس یک گزارش جدید، چند تن از مشاوران ارشد رئیس‌جمهور هشدارهای اطلاعاتی مبنی بر تلاش ایران برای هدف قرار دادن آن‌ها دریافت کرده‌اند.
🔴
در نتیجه، به برخی از آن‌ها دستور داده شده که از خدمات تاکسی‌های اینترنتی و خودروهای کرایه‌ای به دلیل نگرانی از یک حمله برنامه‌ریزی‌شده استفاده نکنند.
🔴
هم‌زمان، خود ترامپ نیز گزارش‌های اطلاعاتی از سوی اسرائیل دریافت کرده که نشان می‌دهد تهران در حال بررسی طرح جدیدی برای هدف قرار دادن اوست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/137296" target="_blank">📅 22:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137295">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER_hzgUphm-tXubkRLOK8ZVxmRot4EayGTK0tO6Skkqz8u43fJFG6In1Yp3L8PKYz2mI8zB32pwbDjy2eWJH7PGfiwLzc0heX0AhSVP5NjTg3KvCVAi38Zgace8koC4bUPA7ccJ5ZLypOPu5ZAmKHHf4ueP2MGTM2t7h3Qw7_PwJLqimTXT4y7i8oo5UwMDZkHqglAMoW2SNovo9k190WbRVNiUHOY-7RZp-Bd7uFaeDJdlY1uLkAVsTIvIAlkGPN425IUsJBgsLREAlE4hLp2F3dCNjQ00kKDHMvv18mkkShrSiMkxeLRloszcN3cXIrRuyB3Mv8ORdfs-vo5kogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: مسیر دیپلماتیک بین تهران و واشنگتن ممکن است دشوار و پیچیده باشد، اما علیرغم لفاظی‌ها در مورد تشدید درگیری نظامی، دستیابی به موفقیت در هر لحظه قابل انتظار است و بعید نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/137295" target="_blank">📅 22:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137294">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c80ce599.mp4?token=c7F6_O8_OlMcunwJ0MmDTi_R_VUD8z8pnbLsPYFQ08Ojg5s8d0skQyP9cnUrz2mddmjBUaGqI3UC7TtDCOLl2RL6PAoL5kbsG_Jqu0PUY3vBJ8c-dC72hEFuqkNhF9EtLdbZzXotSouN-9DNOY4g_halosZhPdhsBl3BXySRvRHLQP58-4MEvlQ8JuWwndu7DhCN0cr5RxO6KjcBr77Ugd8KN7GJ0fRvtfKStpqw8DrHGN3-sa15xxf1jd0w2JwKkmBD0FsYvRt01nrpP6UnOmC9xODMsnF5mlPLI-UiKCmjlAnwFxtyBIgUsYSN9LB3xWXD_F7tiEWG6hTTD3IJqGGgpP1g57h5Cpzr7DuW2ynUfuQ1w8ZhZY5C3ud9Ynf1InbxKE0VdCAezE3Mj9FOBe0Qc7q3pvk0VQspqfabdHjVW9JJGrkmH-9eGqlG-enUP5iyoD9ecvd9K4XMcr4DDk8Xa-_SUe9a6pegyoJohurI6IaNHfBDwmQNkQUv5OyeF5MT_7SVKORFnwrQ06lf5i_3qCQm3GEMqQSY4Pzj8YEDgptD-jIIyoXdpr_iAyS8Fz8jBeANNXtT-NCT3Y9vGEzbRsGJ_tULc8Eltkwy6izwvNyi2t0MmA7ynnkRs31pwnoB21Fd8akCiF0mmdrwljse3-C9iLVKEFXR8bmHRRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c80ce599.mp4?token=c7F6_O8_OlMcunwJ0MmDTi_R_VUD8z8pnbLsPYFQ08Ojg5s8d0skQyP9cnUrz2mddmjBUaGqI3UC7TtDCOLl2RL6PAoL5kbsG_Jqu0PUY3vBJ8c-dC72hEFuqkNhF9EtLdbZzXotSouN-9DNOY4g_halosZhPdhsBl3BXySRvRHLQP58-4MEvlQ8JuWwndu7DhCN0cr5RxO6KjcBr77Ugd8KN7GJ0fRvtfKStpqw8DrHGN3-sa15xxf1jd0w2JwKkmBD0FsYvRt01nrpP6UnOmC9xODMsnF5mlPLI-UiKCmjlAnwFxtyBIgUsYSN9LB3xWXD_F7tiEWG6hTTD3IJqGGgpP1g57h5Cpzr7DuW2ynUfuQ1w8ZhZY5C3ud9Ynf1InbxKE0VdCAezE3Mj9FOBe0Qc7q3pvk0VQspqfabdHjVW9JJGrkmH-9eGqlG-enUP5iyoD9ecvd9K4XMcr4DDk8Xa-_SUe9a6pegyoJohurI6IaNHfBDwmQNkQUv5OyeF5MT_7SVKORFnwrQ06lf5i_3qCQm3GEMqQSY4Pzj8YEDgptD-jIIyoXdpr_iAyS8Fz8jBeANNXtT-NCT3Y9vGEzbRsGJ_tULc8Eltkwy6izwvNyi2t0MmA7ynnkRs31pwnoB21Fd8akCiF0mmdrwljse3-C9iLVKEFXR8bmHRRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
درود بر روانشاد
#نوید_افکاری
🔴
#رشید_مظاهری
به سلامت باد
🤔
ننگ ابدی بر عليرضا دبیر و تمامی حرام زاده های طرفدار حکومت جمهوری اسلامی
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/137294" target="_blank">📅 22:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137293">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نیویورک تایمز: نهادهای اطلاعاتی آمریکا معتقدند که رهبر جدید جمهوری اسلامی، نسبت به پدر و رهبر پیشین خود، علاقه و تمایل بسیار بیشتری به دنبال کردن برنامه دستیابی به سلاح هسته‌ای دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/137293" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137292">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217970b0cb.mp4?token=iSLhazXaXjPsXnWpEDszd2u_-Sh2_58c5gI5_b0An0oygo_5uRx5RvaApVkk477bw7OuJw7wMAUtC6xoytBAUjACwOrseYwbGieCFfsnFH8r7WWqCFCqcaMFUhx-tQWWy66a_zDIkriFvG-rO8T4X7N0T1YKoX3OiKHU5cJfG0m94qz_2Vc07DEFF5pZ0T_uCMB7VV3Qt7M2Qr9okqxOzFzRAcprzpUSeDCaF3LA9g1EEiD0IZJYihldsAF66pG9aiYZ84dsCZfJ1ha_HWjIcnN-fqRgYECKvSGW08waaC2L_duqkuIujeGJy9CIKSjpKxzeeuqP4_xsIBGZW0JEpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217970b0cb.mp4?token=iSLhazXaXjPsXnWpEDszd2u_-Sh2_58c5gI5_b0An0oygo_5uRx5RvaApVkk477bw7OuJw7wMAUtC6xoytBAUjACwOrseYwbGieCFfsnFH8r7WWqCFCqcaMFUhx-tQWWy66a_zDIkriFvG-rO8T4X7N0T1YKoX3OiKHU5cJfG0m94qz_2Vc07DEFF5pZ0T_uCMB7VV3Qt7M2Qr9okqxOzFzRAcprzpUSeDCaF3LA9g1EEiD0IZJYihldsAF66pG9aiYZ84dsCZfJ1ha_HWjIcnN-fqRgYECKvSGW08waaC2L_duqkuIujeGJy9CIKSjpKxzeeuqP4_xsIBGZW0JEpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک زن عصرحجری معترض به توافقنانه: مردم اگه گرسنه هستن یونجه بخورن، ما انتقام میخوایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/137292" target="_blank">📅 22:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137291">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
المیادین: واشنگتن از رهبران کردستان عراق خواسته در جنگ علیه ایران وارد شوند و ایران هم به اربیل درباره پیامدهای هرگونه همراهی با این جنگ هشدار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/137291" target="_blank">📅 22:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137290">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
پدافند کویت مجدد فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/137290" target="_blank">📅 22:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137289">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ایرنا : آمریکا امروز بعدازظهر دو موشک به سمت یه نفتکش گاز مایع که از خلیج عمان نزدیک منطقه می‌شد، شلیک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137289" target="_blank">📅 22:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137288">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409d06d604.mp4?token=Hy88GxpUcAZpVUvL63Cc9c0ohJji2H48vrmvg4frtrgSi5KylCuWfJnUwO968ujavJV-LK_07QIV5QSqzxZvEIW7FEXyDmcD2Cb2kmoQaN8XE9fa_1hX4Iu4OaZLKNWNVXu4GqPRhKP41Cjdm7JQ5XYinsEQsOrE-thy5FkUcMUwuh_ADvt-xR_o4MI0QrMoiNOGTEA8LxNfKEx4VCp6oZ3rn2CFcv5BsElrXe0Fr43g5q1Q606N7F2kGS2zpVJO-KZBwqQCkLGY_qcNVDJGolkv2FfJKOdHACK9oQtSI-5u1ylqDQBPn6MsVmBOuT8lX0AEFyQyM8u64x4xCGcy4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409d06d604.mp4?token=Hy88GxpUcAZpVUvL63Cc9c0ohJji2H48vrmvg4frtrgSi5KylCuWfJnUwO968ujavJV-LK_07QIV5QSqzxZvEIW7FEXyDmcD2Cb2kmoQaN8XE9fa_1hX4Iu4OaZLKNWNVXu4GqPRhKP41Cjdm7JQ5XYinsEQsOrE-thy5FkUcMUwuh_ADvt-xR_o4MI0QrMoiNOGTEA8LxNfKEx4VCp6oZ3rn2CFcv5BsElrXe0Fr43g5q1Q606N7F2kGS2zpVJO-KZBwqQCkLGY_qcNVDJGolkv2FfJKOdHACK9oQtSI-5u1ylqDQBPn6MsVmBOuT8lX0AEFyQyM8u64x4xCGcy4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راز شلوغی کافه‌های شمال تهران
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137288" target="_blank">📅 22:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137287">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
چندین انفجار شمال کویت را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137287" target="_blank">📅 22:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137286">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
قوه قضاییه: شعبات ساعدی‌نیا همچنان پلمب هستند
🔴
ساعدی‌نیا هیچ امکانی برای فعالیت ندارد
🔴
موضوع مصادره اموال در حال رسیدگی قضایی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137286" target="_blank">📅 22:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137285">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdN-xr1YiKohgGensCHCDbCON_ZGe6BhF94HzGmTrILaDDgKVNVdlP8STH3FMlMYdTp8gqxgYY8IpNI1UVndxM6yXNz4CRamj8f8kxgXj-9H_sv6SrqXDlUFIOjdX75Ghux9ZT9344JGcfOJjmA_cnrbXcbSGej_OPggVgsAAVhD1L7n6X-rUorGwNXzAB6MuI2oJfDNQqfOdB7J-Ko2xhX3CD_LZC4vNSBKyN7fkQ8qLTrSigqgZDsibsu3uUStmoW860KWik6_1NCRRKJsGKiks0ZMcL3N9Q5CNO93a6GsEi1_80P2peM3nl01fgOiqPP3A6iSzzEfqvUVQeyjQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با سرویس های نامحدود ⅓ بهای مخصوص نت ملی هایپرلینک از شر اختلال ها و قطعی های اینترنت خلاص شو
🌟
با ۱۴۷ هزار تومن سرویس های نامحدود و ایپی ثابت هایپرلینک همیشه انلاین باش
✔️
همین الان تست بگیر
کد تخفیف ۳۳ درصدی فقط به مدت ۲۴ ساعت:
Code
:
w
ar33
⭐️
🤖
@hlink_robot
📢
@hyperlink_ch
💬
@HyperLinkSupport</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/137285" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137284">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ روز جمعه با مشاوران ارشد خود درباره تشدید حملات علیه ایران دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137284" target="_blank">📅 21:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137283">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مقام آمریکایی : ما یه سایت امنیتی ایران رو تو نزدیکی یک گذرگاه مرزی بمبارون کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/137283" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137282">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_lc1V2eOSgE3rzUgAp4wJzBxYBeVZByvZQ0y_gqi-QzFbc2deNOBjF6oWKo7dpbGzmTQ2SqdbKiQ68kd1CDteZGfUET_-ih5oE3QJsi5cYFC6LFRs-cXYkpB1h97O67y7Gv9ECZ4X7tH_97Bqxxt2anB3MT0_y0vybeRkOnWXy2oKAp5TkHrfTI49LbgYn6YjLjBVHcBXwhUKxIXz8E1Pr8pwsclY0BS9V-xEwr6gJcLsiWMkSQA3bXkf6DwRH5fwg6sFBhCqCfQyPPN8Do2yJWfcIzoJAp5SDnTK445aHm3EPNSmRXFomrGG4TlpxJ8SRWhhhqs9n1G_x7M9x4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین پست اکبر عبدی در کنار علی دایی، نوشته بود: حالم خوبه نگران نباشین
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/137282" target="_blank">📅 21:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137281">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فرماندار جاسک: ۱۰۰ شناور در حملات اخیر آمریکا آسیب دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/137281" target="_blank">📅 21:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137280">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ: انتظار داریم به‌زودی تعرفه‌های گمرکی سنگینی علیه اتحادیه اروپا اعمال کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/137280" target="_blank">📅 21:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137279">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
العربیه: اسلام‌آباد از تهران خواست تا بر حوثی‌ها فشار وارد کند تا از حملات خود در دریای سرخ دست بردارند.
🔴
پاکستان به ایران هشدار داده است که بستن تنگه "باب المندب" وضعیت را پیچیده‌تر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/137279" target="_blank">📅 21:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137278">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYqNJJK-yLmJLtwnOCT-a5r62ec65R9FWOi7hvVKW8Ry_l_7fJyf06ZIT_FAog32XzWX8eYp3RSO9djoEshjSu196yzOfH9Vd8d-UV5DrRZNyes323ge5FOEEJWIFJp-6YGQIgrTKg5nD2tgkfNNod3DdS4yaRFd-bamfa010kpn3yBpUdkHBPnckNJA9ZGGhjRNrkq0sYajkz4vKNQYhAgxlV1Suuf4Oa3rtwfitr37o1lcE-btP-oEcxw6O7z4ikjQVSXRF5lWxKJbm4grri7IKTcuZ3uw5H1m2OG7e4UD8Sk4rKE1_l-7ikQrD7nXqmZFBsh0FyfKa6Fsa254Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، از طریق شبکه Truth Social:
از تمام سناتورهایی که با تلاش مجدد دموکرات‌ها برای تضعیف امنیت ملی ما مخالفت کردند، سپاسگزارم. تبریک می‌گویم به آقای مایک جانسون، رئیس مجلس نمایندگان، و نمایندگان جمهوری‌خواه به خاطر موفقیت بزرگشان در برداشتن اولین قدم به سمت تصویب طرح بودجه.
🔴
از آقای جودی آرتینگتون، رئیس کمیته، چِپ روی، میشل فیشباخ، ویرجینیا فاکس، جیسون اسمیت، مایک راجرز، جی‌تی تامپسون، برایان استیل، و همچنین از آقای تام امر، رئیس گروه اکثریت، استیو اسکالیزه، و همه کسانی که برای برداشتن این گام مهم همکاری کردند، سپاسگزارم.
🔴
این طرح، یکی از مهم‌ترین طرح‌های قانونی در تاریخ آمریکا خواهد بود. این طرح، به تقویت ارتش قدرتمند ما، ارائه کمک به کشاورزان و، مهم‌تر از همه، اجرای بخش‌های قابل توجهی از طرح "نجات آمریکا" کمک خواهد کرد.
🔴
مردم ما بسیار خوشحال و حتی تحت تاثیر قرار خواهند گرفت! از سنا می‌خواهم که قبل از شروع تعطیلات تابستانی، یک مصوبه بودجه را تصویب کند، که می‌توان آن را با اکثریت ساده به تصویب رساند. ما آماده‌ایم که در کنار سنا برای انجام این کار به نفع مردم آمریکا همکاری کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/137278" target="_blank">📅 21:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137277">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7XtOx5nIsqfax0ICETaFzU3vci2qxj4Fp_ZRL8qIWUAorCrgdb7pdzb8P_ZJeTZQlVd9gen6T26gbrR-dT7mBSu_NJx4psAgdWcBlAzWnxVVz_uRIKBA5Ghachlh-Nda90Miv36_fcYRBoNvJ-0xOg2tT-YTWdz99YO3wgQZKzJixekCB6bluhJCCIulEQpr0-40BgZcsi5JbQS3EpRMLd8tuFtynPUIcs-6SRCAhJoOcRpijY_xRy0roPfdEAs7h2EMEF4ORKYu-4NfUzbGE_LXbmORJ4SwWieceVWC-X4EIh2-uzOMbuYXof8hXIetxYe1Nw41NXasxIPR0Kbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/137277" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137276">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJwjNJeJk5GHe9EAzCw7ZME_L4NJmOHga93HbDWjfsL7GlJ1Mm95Lz9AJYrMwrgeuixkixZmGj7NffX5Pb3I75iDgTMnhZ37aZn_1K-ogCR9IPTxxOEZyP65Vb7rwcGSXAHTPRGVCcNYfVcHzTTFQp1GW9DC8eKXi31jQJTOXM-TgtKSX2QXOYHcaa14HRLmCuUs6voNbKssGOvxF0i3PxrAyMb6MkxcPs6O7HuHEWSFC_j7J5LU5PWFBWz-ubwHGe04JmTI1LZVTcGRj-yfQrBnBvcoo5zDxUFK4awlVZqzIGGTGxTh6tnmkJQR8rvlpA5PptqxyMW9A56a1Tsxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: تشکر از نخست‌وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/137276" target="_blank">📅 20:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137275">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp3MvUbfv3Fik1wU21LW1PjeshpaQdfj46-Hx70Keypcs4Zwtrx0lLFYB3e4mj-Dsn-t0CaeIZ9hxqB-ho52xnpAOuap5ppMSvARAF8uNZzDjfitXiqvY6BUjmjoQ-z4eTxZqZiyeojt7cCSTMaiYasAt_Gd9rWCHfW6-CZ2O6BFhE-Vp0K72ZWUMXgeA3QXsAiGlmN8eS_To_W71YNvGFBt6TRDxZkQMD5rv2C69a_awk_Q7e1xt2vtTi5lf0lHcL0YH3QLQnSjy1mvQwx35RHclbeKgnm-Fwc3ButWrrYDwa4gTahNy6mQ0NBTTquEqyioWRVei0-JebnougLWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همراه اول قیمت بسته های شبانه خودشو یهویی ۳ برابر کرد و اعلام کرد با مجوز گرون کردیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/137275" target="_blank">📅 20:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137274">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afacd735eb.mp4?token=YTuUdk3efqx1sr9gTdgmW4OnBb9ze5usmpqHOArVb5ZtSME98otv_0GVcB8Y5viKpc95udjcc7f30BWrX3S25d7kg4oaTJxSxj7C0uDGjwWEo8jp1m1qU_rHRATzU9-DGqh714z-FE7tlPKymR1A9lf9iLeCheT8uup9PwVOSLn7DzaXpI3WNsXC55DuTSKEIDXINiUnLUM6fhKVNAUcURMIjx1IWDwlBsK5kFHvpGaUBvuXdXG1YJh9nLXSCRdavZcVGuaHFT9-1kjZOiURcQZORVXc5giOaD7Sn2EFwZw-a7DnVOiW7nlfIyTnwyfUySlUs2nCnDkOz3q812KQ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afacd735eb.mp4?token=YTuUdk3efqx1sr9gTdgmW4OnBb9ze5usmpqHOArVb5ZtSME98otv_0GVcB8Y5viKpc95udjcc7f30BWrX3S25d7kg4oaTJxSxj7C0uDGjwWEo8jp1m1qU_rHRATzU9-DGqh714z-FE7tlPKymR1A9lf9iLeCheT8uup9PwVOSLn7DzaXpI3WNsXC55DuTSKEIDXINiUnLUM6fhKVNAUcURMIjx1IWDwlBsK5kFHvpGaUBvuXdXG1YJh9nLXSCRdavZcVGuaHFT9-1kjZOiURcQZORVXc5giOaD7Sn2EFwZw-a7DnVOiW7nlfIyTnwyfUySlUs2nCnDkOz3q812KQ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از انهدام سیستم دفاع هوایی پاتریوت در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/137274" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137273">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: بحرین و کویت در حمله به ایران مشارکت مستقیم داشته‌اند
🔴
وال‌استریت‌ژورنال به‌نقل از منابع آگاه نوشت: کشورهای بحرین و کویت در اقدامی مخفیانه، جنگنده‌های خود را برای حمله به اهدافی در داخل خاک ایران اعزام کرده‌اند.
🔴
امارات نیز با ارائه اطلاعاتی از اهداف و تأمین پوشش هوایی، در این عملیات مشارکت داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/137273" target="_blank">📅 20:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137272">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpVmnPuGrFPV0WokRDr9FCzrrDXOusGbeSa1XeGPFjJNa88MyP4Pffpj8tKYvGwVPWkCL5fB81pCALYJ3qcpHynhwtH0R_IVWBFvHV_AuUtD3RLSDer3GdcFkZDTWmvkq7y3L6CH32fOU3do1YMhFjlkskJ5AsOKRru3x8qeTwtlnlEtRfz4u2sT82ikzq1IwXQvVo-UBvhD4ubq8W9UgVsRPTutZd6JKnWMFhTfXGh0duJWKrh3Fz6wYFsUqPcS6JvGcrLP8DsCpyP0vhL7ypR96f1V3w9zl_ayjVyjbyyAuUdWH3SSCrenr_BTrq2X3JbwhbM6oD469WpJOHXVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخورد پهپادهای انتحاری سپاه به مواضع گروهک های کرد  در شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/137272" target="_blank">📅 20:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137271">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDtztLxgB1cMWWb2NRT0bWsGQoYt1FM7AUYmYsl8Jxh_khmSk5OEYbNTOG-IW84p9hn48rQ8MWwS83BycwCddNNZpzzM3v5tDmFXtj_NiH3X5exgH9pOBszSWqAG00iUxkYXK8yeyBiq8dRl1IWD6EEItoESGuDUcMYyZtLVBvigBHZseOZTBymVJ1Q_vcn-FTaJLzWGnYl3WGgs4dhBf35pycD0LZ1zcJPNdAb4PltSkBhVJZhvj_bEj2LZbMnnj6xDZr3Y6LZYASedwyscE-9ZupXhfe9uIDzMp10__bBrvipOW452DYyyDB7g-nG-OVQdob_WAqQZ98qO6YIoGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخورد دیشب پهپاد سپاه به پنت هوس یک برج معروف در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/137271" target="_blank">📅 20:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137270">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWuTf1S3YFZKViPjfCsZQ1ELluPb3s84o4H9zuTqGVXp8DLfI2ZStvVYlS-y-Kcd2k1J7DLW5Q0o1vbDu6XMbefnTQzbqSl6ppuFkwX5j0-6dTXN7GctptqF3yyb3DYcsbAHDNQbSqEbT2t3mClTZXn2s62pdjcGJnU4x-K8NpoEpnOakHWX-ufmuObpghsCCmnAYyFlZ3rbMRSqZ96x7k3fVA-RHq5T7xsyi9MwCqdhLP_9-pAhecRUSskvm5iacGBolLQFCDaPxbssQ5NiKnOIcgmdsLrUgbWHlPtvH2eCVC69_qFVFR4AzpOPWw3Su3aJrhk6jJjAtjPB34VLLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social: کانادا دعوت آمریکا را برای افتتاح پل گوردِی هاو لغو کرد، که البته جای تعجب ندارد، با توجه به اینکه آنها مبالغ قابل توجهی به عنوان تعرفه به ایالات متحده پرداخت می‌کنند.
🔴
توافق اولیه، که توسط دولت قبلی به طرز فجیعی مذاکره شده بود، دیگر اعتبار ندارد.
🔴
ما شرایط را تغییر دادیم، به طوری که اکنون ایالات متحده 50 درصد از سود را دریافت می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/137270" target="_blank">📅 20:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137269">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
حمله پهپاد های شاهد به اربیل، هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/137269" target="_blank">📅 20:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137268">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
منابع عربی: صدای چند انفجار شدید در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/137268" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137267">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای خارجه ایران و عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/137267" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137266">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
آکسیوس: ایالات متحده و بریتانیا در حال برنامه‌ریزی برای برگزاری یک کنفرانس بین‌المللی درباره تنگه هرمز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/137266" target="_blank">📅 19:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137265">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فرمانده مقر خاتم الانبیاء مرکزی: به ازای هر شهروند ایرانی که شهید شود، یک سرباز آمریکایی کشته خواهد شد. ما بلیط‌های رفت و برگشت مستقیم به جهنم را برای شما آماده کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/137265" target="_blank">📅 19:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137264">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
منابع عربی: صدای چند انفجار شدید در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/137264" target="_blank">📅 19:44 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
