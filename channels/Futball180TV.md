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
<img src="https://cdn5.telesco.pe/file/nsTl0sBdmqKtcYk2XxsvZzO3MDGr_0MmKNM2vPW6cUdNGivhTgOpC3D2O9WdMpTfXkxdy_X_3YHCtxsg9MGjBc_AITRIpG0fpJeWJ7mJa80CHfXAosuk4tpgCaSW7YKyE2NIkkcL-37f-ZrqH_ROAk3NZfOmFsd-8ZR9MiVuRYefRGDilIMXPobAyyzMr7v_s4K9Kee1rYPETDpAyThQnwZwL1tr3HwJky8Ha9xBUCaCRkSux18tdJ5eD-sgN8wDLjdy913hrksyJkDjR3PoHvJ-fy1cy65iog5x31JFVW67Udi9RmYhYdAGnOB6Ga3IiNbPV0NyLyF4p0XI5j3AVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 572K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 22:33:11</div>
<hr>

<div class="tg-post" id="msg-93324">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjhUKudnQ-uiwq43cf2yQbURvWMtYDa2CKaQcRA-n8kEyYX-_Oq4kiglEVE_WZIrx6ThM4hLdNaXnN7XE7j-6zNpmk9973pntK2OHs_LHvaYhocEMFih9AGWzjdty-s6xWM4w3ey6sTaBdTqQXtLvdkFXsSODVcWEjLQMx_CJ4-aGgFC6kzwmp72z5z_YNUXi3nuUjo0OowabWo468P9N2kICWpVc6BZnavF9gSqdOMontfHbz2JBmwbUofvjCsGqdZZp1gQyvHaaSp6tMsIkOGd_gx3lhLmgHOzAqwPQFJvpT4buT39TR47mJWSAuI0OJNIHWXQ0EF7axhfmTcPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
اسپانیا در اولین دیدار از پنج جام جهانی اخیر تنها یک بازی را برده است.
‼️
❌
۲۰۱۰: شکست ۱-۰ مقابل سوئیس
❌
۲۰۱۴: شکست ۵-۱ مقابل هلند
➖
۲۰۱۸: تساوی ۳-۳ مقابل پرتغال
✅
۲۰۲۲: پیروزی ۷-۰ مقابل کاستاریکا
➖
۲۰۲۶: تساوی ۰-۰ مقابل کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/93324" target="_blank">📅 22:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93323">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بریم سراغ بازی مصر و بلژیک
🔥</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/93323" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93322">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9bSQRBpXCXwS1D--MWimaetKlaCgHQrGwNMpcSoHQw8oKSfNWKCWqmcazplAVVCSmlLnUNp6T_pmMSv2XcS-eO10P_3lD8wQn8nZoZQf-ezunrq62vAnZoxvTVKvizmNwbz80JlskMJn5BSSz0nLqZtzDX428N4QaYYFB1f5KjCyceJZGr_9d4EQ7TzjxdeS5l1y6apoqDnbzpHXErsPu-ST2d67IKdDr3BSE-y1WJZlvlvMG6LL7KXTbhEdUfVt8Ny3Sl89C5B0Jhr-baxlegPKU6otV-E3jX48y0Wj4JCjtdWmfK3asOEUDHz_J-ClY62-4C96lhVsrQL9pnBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
پشماتون بریزه ووزینیا بعد از درخشش امشبش جلوی اسپانیا تعداد فالووراش از 50 هزار تا به 1.6 میلیون نفر رسیده و همینجور داره میره بالا.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/93322" target="_blank">📅 22:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93321">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6DziTL09Hy31QykbtMdWwVcRxU0CDcAV34wVxrZsezyS1xG6L3NWWI9ZqVmOU3Vbj3ZXs827eOHWTJg11VAPOT59kdLis7Z7EITqW6k5Y69To_RLmrtDhPL0UGf76yJxmwujyYUZFX1GDOQorck8Viaf-e5aK3x8mOgBSSNoe7yWPS6EBJZC4NV6ERgOyMPq_5Utphqy99ZrzvAtW-2JnpeE_mZuFY7U5Y2mHUM-XKxpLNPm9hiQBNlk89Nsybv-Wp1M_UBd9HmMzcT4c5mf48_n6kaCWHI25KtEEoVfJAUVRliBKWwQb8nkmJjDEzyfb_lNa-CGtg6PcjKUa_DTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا بدون وینگر تفاوتی با یه تیم معمولی نداره.
۷۰ دقیقه بدون یامال، کل پلن این بود که توپ بدید پدری یه کاری کنه!
با یامال و ویلیامز اسپانیا میرسه به ورژن یورو ۲۰۲۴، ولی بدون اونا حتی توان بردن کیپ ورد هم نداشتن…
البته گلر کیپ ورد هم کار بزرگی کرد و یه امتیاز برای تیمش گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/93321" target="_blank">📅 22:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93320">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZhQSsnugrByJYgyrZeE5DNisQMlB8hbDdVWtUeRLRaeZOGVVRJnM3zGJ37eyc1LGaUUZ73VuW9fvcNJgJWssGq04OLVDuP_uESDNfSe-y9kSOxz0SELlMYQ41sAraCITHzMAgDwhCuqZuFXqy2UA4SHkWZtlTPUAZidODmJqn7TKRqOYYSC8qXlor_HdRkN8UMTkjOLmZo4HRKOSX3i56gSmWonUzh7Pr4fZvwcmAinjrRcfQFldevpJHTGRipnBML8D7wXGadSu8oJDhosm1D1f76jFWr9qhke-rkEaejKo9X-vbHrOnnpmOJaJtYb974WT2sXwM_zrD9HwEqk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم برای دلت مَرد، ضربه ای که تو با شرط بستن روی اسپانیا خوردی هیچکس نخورد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/93320" target="_blank">📅 22:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93319">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b27f7be0b.mp4?token=roqwQsAN6aRS0iN6crT3LHx5dekpnMVrR2AB4vXjij94VlMWtR2Ku1NnoKzCJyIX5KV2L5kyb8ZOJpKnamx38gViBZF_rptxBi3kwF5XnS2Hmg97oBHysV96Dk8sMokM4jAU_jHYEAquuXj6M2TorRhFI5IN7sIgFeE-4zrsyXxG3YPpBUxjWH2oUeZdH06bBzMH5f_tdQAxe3Lr5pw87icLJMu8V2N-EC0WCTodDAr-hxE8Ntz_HdBZf7VEmIppgSe59PaJRO-XoR2cuqz_vXOuOZhhqRM8Yn-DATlIM_VqbloKeL-Ce3yYbW2JNp1Ep60qUXaiYZK_UxkYjvXkKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b27f7be0b.mp4?token=roqwQsAN6aRS0iN6crT3LHx5dekpnMVrR2AB4vXjij94VlMWtR2Ku1NnoKzCJyIX5KV2L5kyb8ZOJpKnamx38gViBZF_rptxBi3kwF5XnS2Hmg97oBHysV96Dk8sMokM4jAU_jHYEAquuXj6M2TorRhFI5IN7sIgFeE-4zrsyXxG3YPpBUxjWH2oUeZdH06bBzMH5f_tdQAxe3Lr5pw87icLJMu8V2N-EC0WCTodDAr-hxE8Ntz_HdBZf7VEmIppgSe59PaJRO-XoR2cuqz_vXOuOZhhqRM8Yn-DATlIM_VqbloKeL-Ce3yYbW2JNp1Ep60qUXaiYZK_UxkYjvXkKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
ایرانیا لس‌آنجلس سازشون کوکه انگار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93319" target="_blank">📅 21:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93318">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/678ca94f4f.mp4?token=asHUbM1meWxQlFuUKbF-0O9L_rWoSCrAPUjT8qozYOdLBSOs9USJ7tBSspgnaY1ETn32KaUn0ZILqljgpph5YNTItj5BVhdX04jb9C1bBswT5POpwnUJcR46PegHPoTQyRzb7-0NGN-1-pXa7DZcKA5zpZVmnzX1k2r8BLSIebbAha9V0Djs360lIZad2aWN9L7oGekB0M32Pc6lFEhLqopiUDVwgMqHRBm0hYBvVwfFjLkOGLhsw5UYkuFem5XsVzdj-0I4OKGCwMbOwTz4JYUctRH0edjqrY7GUizzpgZhAP1x0na9S4xxB_oI5jeqlag3GC3Rs7PgpbAWk9L9NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/678ca94f4f.mp4?token=asHUbM1meWxQlFuUKbF-0O9L_rWoSCrAPUjT8qozYOdLBSOs9USJ7tBSspgnaY1ETn32KaUn0ZILqljgpph5YNTItj5BVhdX04jb9C1bBswT5POpwnUJcR46PegHPoTQyRzb7-0NGN-1-pXa7DZcKA5zpZVmnzX1k2r8BLSIebbAha9V0Djs360lIZad2aWN9L7oGekB0M32Pc6lFEhLqopiUDVwgMqHRBm0hYBvVwfFjLkOGLhsw5UYkuFem5XsVzdj-0I4OKGCwMbOwTz4JYUctRH0edjqrY7GUizzpgZhAP1x0na9S4xxB_oI5jeqlag3GC3Rs7PgpbAWk9L9NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🏆
انتقاد ویرجیل فن‌دایک کاپیتان هلند از هایدریشن بریک در بازی های جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93318" target="_blank">📅 21:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93317">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffi3Y6t6mUG3N_mk_5Y9ChOe4a_4JMunvq6QIF-Xye6ElN8k0SepHmqOWF_e6lx1PcUTe3BR9AoEuyRVcIb-GadFGH3pZ5gRZ6CuEKmDIQ7R5T3UpwPMntDfKcISyWycKxyRt-h3obcLW6w68C2mPf6446X9hyVo2WsgEHXDOea_3LPNjqQ1v7pIXaempoYfGqT09aLNWo7uGb62zuN3q4BdD4LCOz-anENFDgGsYs2XnUDwPJUolViUgoWffk-dx5w94S7qTdNybCmqz3NLOhJX-lPS0xHoKN4WtLZT5UMH_-eweYG7exPVLbgacLzZsDi7bL6VC_O43SqZpUa2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🆚
🇳🇿
ایران
🆚
نیوزلند
🔥
نبردی که برای ایران فقط یک بازی نیست؛
شروع مسیر اثبات قدرت در جام جهانی 2026 است.
تیم ملی ایران با میلیون‌ها هوادار پرشور،
با انگیزه‌ای بزرگ وارد میدان می‌شود تا اولین قدم را محکم بردارد
⚽️
🇮🇷
اما نیوزلند…
تیمی جنگنده، منظم و خطرناک در ضدحمله‌ها که آمده تا معادلات را به‌هم بزند
👀
⚡️
🏆
آیا ایران می‌تواند با یک شروع قدرتمند، پیامش را به تمام مدعیان جام ارسال کند؟
یا نیوزلند یکی از غافلگیری‌های بزرگ تورنمنت را رقم خواهد زد؟
🕟
ساعت ۴:۳۰ صبح
📅
سه‌شنبه ۲۶ خرداد
📺
پخش آنلاین بازی منتخب داخل کانال زنده
🎁
شرط رایگان ورزشی ویژه کاربران جدید
⚡️
هیجان لحظه‌به‌لحظه جام جهانی 2026
🚀
امشب فقط تماشا نکن… هیجان را زندگی کن
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/93317" target="_blank">📅 21:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93316">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
#فوووری
؛ نتانیاهو: بلایی که سر غزه آمد را بر سر جنوب لبنان خواهیم آورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93316" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93315">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBEhQzUmerzqgBzPHPUKUPy7UtH9IUEiy_SL3KRXmiBP_3MkQ8aK1b0EUFYs3zum-5eL9GpAUQcKuLzvRn83n_ulng_yGybERnWKi5Lu7qdVfvH-qbFri7k4CBkgYcNck6bWMgoVZ2uy1H456oAx8oYPAawB7bjFFUG38eChbTQUPgee_wLsJaHUEPiQV8R2uxopzy8Iblbz7nRtpPxVhE-VlT2SiT_uvNJN8Hrx152RwX9Q8YZreE0UNiobS7Qy8YN7Y7YCVXw52PUkNSTRfFeAadjlQfx3IvXRLBU_H6EBJrTY9DhhPAU9IjTy-MfvpFML_RHuW0FneTpUOwJexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
ووزینیا گلر کیپ ورد بعد از درخشش مقابل اسپانیا اینجوری احساساتی شد و حسابی گریه کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93315" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93314">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9Kp6a8w64bXf8aMymC7aG_-IF4rmusdGST8auVi-WadGiz_oqPewZuajYxj8-A6E9-tDix8ZKLXJy5TBjda1lbfLCLLlQ6t8sseMF6LHnczXcyfWQjWDp-8VygW1osLji9aF1to939nu27uSIYX5wchWI7-SfY7TG3GkSYbA5S4_KJHbt4UrvbFKGEbKkDJhrpD1PLCnXc54sFMX0_NeO9KYpNsgln06HGoX8m1kUwHqbJA7pCDGk6dOUTeov-ssoM1YZJ1M--bj9RB7HBVUh1nwBGkw7sJZNu2N0p-1ZlTxWr39BV-vSAiBoduwDe7rXwQOognwnxxX324CarhZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رودری:
سبک بازی حریف بد بود، اون‌ها اینجوری بازی میکنن، حتی از خط میانی عبور نکردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93314" target="_blank">📅 21:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93313">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0IO-eTRo8VkEpLCbuZUjWneGCHBhpmGgBMcqThoJREoyGHQkeqg1UiTLpc6xZB5_H5MmdEZZWMBdMXugaT-_UU_p7D3PVaK_KsQtM8Oe3Airb70N7xrSYHzQhmo92PJAhr5QxwZ5AC-X7n9UjW7slYZaKtrSs1KR_iXM8_v2r_w66wLTbMBdtWOCHOkQfLcKFp5F0CahpmAptiCSRx-tz-uRS1b-BuwmMNWKzT8aTPcOB_1DpgPjTHShzBFaacquauZWXyNIl6lbjyQS03whbsOpu_STbYssRcm-7NUFIwHMt7cmti8s9ITSuT5AGbSvQKo6PRfregBFGuQiaLl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا برای اولین بار از جام جهانی ۲۰۱۰ نتونست در بازی افتتاحیه خودش در جام جهانی گلزنی کنه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93313" target="_blank">📅 21:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93312">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
اسپانیا در 4 بازی اخیر جام جهانی:
تساوی مقابل آلمان
شکست مقابل ژاپن
تساوی مقابل مراکش و ترک مسابقات در ضربات پنالتی
تساوی امروز مقابل کیپ ورد‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/93312" target="_blank">📅 21:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93311">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtOGMwXqmwP-yDQfv9tnIkJggoIfGkX50QUGLmh08w7Bu59KuHxE1i4VEOqfVA_F3YjGyWe9c5w3IC1fY5UY-sg3vfgMBLcq_OzkytdDEvmKleM4BvGLsCuH2tX65H5VKPnBXrLkvy5vfpMeH-2ywfF_boarhoRXPEDr8U2I1tgyIlt17H1W1WApBpvI-vTXv_F9FOo7crZDNR88344j-NGNhE9MP6mc47J6PU9HTWVxbKJ1vWGx0EFUhgdq85HRN10vZvKM9wuh_z4bzh6Sy2RQAF-116LqZLbM2zdcnR61iwgKjY8LEN1mxAXGtX9Dj77v4FGiR1m3ybtE6j2StA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروازه بان 40 ساله کیپ ورد امروز 7 سیو داشت
وژینا تو لیگ دسته 2 پرتغال بازی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93311" target="_blank">📅 21:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93310">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2308e52e5.mp4?token=GCl2a-quA2bVmat9Go3Bm-R9KCWx8-9OZDT9g29IJYVH7cVvSx1n_9LxNiMEp7I5nLOZUKBlj3wSFCnxseqHCDU9WF9IXuHy_AZTsbsE_Xj5CR436ggKGauUgtBHTcM_eZgBXkxM1g9az8nuujBb4SIqmD6hDX_FjQiCnD-I9PRAteFEbI7v8lTdQiup_Y2xdy5dQsUd6GlH446-jNKyzsrQVKrLuPq40v2l1BmQh7f3ec1U7KuHN-AnP4G_gFWtRwxg9iXuQgGmMo4pGqrzqVLiO-eE87ZPmPraK8AmkY4SJZY0EdunDyjhetkF_3mKRvx9HzjpTjqcbzNC6YfZ06f55b-NSXB-oGPgl4RLji8X6Glj13nLeNsr30PU4FkwPK7fCCv5BK2LPPJ42i5dNOyeKj9OcSCLMVHrH9fqYlfwZSsSebWOK7x7W7cJnQoMHX8abQSSO_D0OYBHgM2iZ_wcCRUIN8u4C_dCzfy1YEM70t1WsYram_O7AxVu9GmPXxoPeShiqILxauly5TVvlsUSGx8-e0ZVfGECMNaMi1-at_corlp1rlvnQFFZkYPeWP-3e54Kv73Ub0KBN0W_YqPcvu8c58J6IlR3iWpe0Za35m4nyBULN8nQF31NqzpCy_JwFrFkvgMuv5USlH5SjLgPC2L4v6Y1Zk0BoexZxQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2308e52e5.mp4?token=GCl2a-quA2bVmat9Go3Bm-R9KCWx8-9OZDT9g29IJYVH7cVvSx1n_9LxNiMEp7I5nLOZUKBlj3wSFCnxseqHCDU9WF9IXuHy_AZTsbsE_Xj5CR436ggKGauUgtBHTcM_eZgBXkxM1g9az8nuujBb4SIqmD6hDX_FjQiCnD-I9PRAteFEbI7v8lTdQiup_Y2xdy5dQsUd6GlH446-jNKyzsrQVKrLuPq40v2l1BmQh7f3ec1U7KuHN-AnP4G_gFWtRwxg9iXuQgGmMo4pGqrzqVLiO-eE87ZPmPraK8AmkY4SJZY0EdunDyjhetkF_3mKRvx9HzjpTjqcbzNC6YfZ06f55b-NSXB-oGPgl4RLji8X6Glj13nLeNsr30PU4FkwPK7fCCv5BK2LPPJ42i5dNOyeKj9OcSCLMVHrH9fqYlfwZSsSebWOK7x7W7cJnQoMHX8abQSSO_D0OYBHgM2iZ_wcCRUIN8u4C_dCzfy1YEM70t1WsYram_O7AxVu9GmPXxoPeShiqILxauly5TVvlsUSGx8-e0ZVfGECMNaMi1-at_corlp1rlvnQFFZkYPeWP-3e54Kv73Ub0KBN0W_YqPcvu8c58J6IlR3iWpe0Za35m4nyBULN8nQF31NqzpCy_JwFrFkvgMuv5USlH5SjLgPC2L4v6Y1Zk0BoexZxQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شادی مردم کیپ‌ورد از تساوی مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93310" target="_blank">📅 21:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93309">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVJ9eIIRqACq6pTCfRGiIAK_iur_h9lV8WzDrlj0q0He5KJuY8Fg1txczPT2STx0ZbQrCtltRGAkZgjI0at_WK96JVXUs_6M3B_VAA7hXSyvuLA9U3t3Df2K8nNVk4xxhgLdcqEzRQtvcwUtL78P6HquRbvuXLkisMnVD0sTf0IDCdRMNPcMYRWgeInLvmcLNtC5OHriLQIX4AxcJUze-58YpR9HuFGkNDh_Bvwze0jNBt0s3WBh6S81gLj7JcU_JhBBdnlQ7SVxOTWk8GdyqTsyYKF61e46rod-29Ktwyly0BmaGfQ5V5bndCErhvFO38nCfMxRPBwjBXfkORA85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
پایان بازی | اولین تساوی بدون گل جام رقم خورد
🇪🇸
اسپانیا 0 -
🇨🇻
کیپ ورد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/93309" target="_blank">📅 21:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93308">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کیپ ورد نزدیک بود گل بزنه
😐
😂</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/93308" target="_blank">📅 21:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93307">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چه دفاعی میکنه کیپ ورد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93307" target="_blank">📅 21:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93306">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3MmkpP2P9zkDtSsrPnZYI3fYDr7rZv7l_ohEAXKLDXYL9LATK6kZCUXtB-fjmqws7P-AwWaljZN6rorRAbpHQ7xwOZ8rEQLcYI75lX6MhZU0i-DqKAq2ArIsFR3D3_oArRpE-5nPUWLxcMvZV7h6MJ9eU-0B1Pl4kd-ua0kTkBCwv-ena_hm6BB5zzge5NbrDi1gJgN06tTi6v2uuFm57UzjeV-qCPhyR30x4zHS75iXt9GtrBzTUSnWuomXzBK1vuN8i0G3d2TkCiBRHLnnAvsTnUVb3zBxEnF4-7XzzbYAE0XYZhT_5QIlA5s0Slruybos7U2bgvGc6uhNtRTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
ترکیب مصر مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93306" target="_blank">📅 21:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93305">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اگه این تیم اسپانیا با این بازي قهرمان جام بشه سردر جام باید شاشید</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93305" target="_blank">📅 21:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93304">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6f49769b.mp4?token=P6ywHbS60OGV5LvyOQhjvXuRRXJj8xsdA2aGkE55V-Cf0006QFA7vjZS657G62s9vQ5Bwa9eULIc6CAIH3O-fqRnrN_UjlIH4_Qw-ar28PPbeT7ieV2xAGWY2m_J7jXthxGepi6n0Ryjgv5gpGRx-GwbVTRcPyifU_t7jC9euIB_tvGN7SNTC6yEwfATexpmOtbSfMxxb0sU6m4dSOhIY6A5AFx5G7YHUHsUqCwujzKOtXeVqYC6WJS6sYVWMRscqt8_1E2_yNObNbsE_QSyKLRrss_U5et6quNFrSaKAvAl5P9Mx3TToCUR_h2IGioI0_yqPzjYEBhAZbEBAZjNHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6f49769b.mp4?token=P6ywHbS60OGV5LvyOQhjvXuRRXJj8xsdA2aGkE55V-Cf0006QFA7vjZS657G62s9vQ5Bwa9eULIc6CAIH3O-fqRnrN_UjlIH4_Qw-ar28PPbeT7ieV2xAGWY2m_J7jXthxGepi6n0Ryjgv5gpGRx-GwbVTRcPyifU_t7jC9euIB_tvGN7SNTC6yEwfATexpmOtbSfMxxb0sU6m4dSOhIY6A5AFx5G7YHUHsUqCwujzKOtXeVqYC6WJS6sYVWMRscqt8_1E2_yNObNbsE_QSyKLRrss_U5et6quNFrSaKAvAl5P9Mx3TToCUR_h2IGioI0_yqPzjYEBhAZbEBAZjNHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🇮🇷
🇳🇿
پیش‌بینی جغد معروف از بازی امشب ایران‌ و نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93304" target="_blank">📅 21:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93303">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
‼️
درگیری شدید طرفداران تیم ایران با مخالفان تیم قلعه‌نویی در لس‌آنجلس ساعاتی قبل بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93303" target="_blank">📅 21:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93301">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a429dbfe1a.mp4?token=oyQNufY6p0FjqAAlvJ7fPRHbPy11N3BUWlkA3S7ToztN31OHitIU614i46Lzz5evQrtEIPUjt9_JEjvwqQPkyphCJU7xehEPyN71eXtioaG-9fxayDEX8PEMDlMfRPojgP_0hd_rJlSs20tKa4pAwazw5Zs624x8KEjyeC3th4EGlTyRC5HWtdIeOEXxMb3hgG2mwY69ZQ2n-rhYOKaLuLCZtp0mwfPCt1aTYW5J5lpGdRtWJI24WuBDoziNIfxmgNyFLzHBR_Rc8aAez-2K9TbIR-IOVZvXTW9a5QitDqw9dwlCcoOf_8ujqp4Sx4fSObn6dDuSZvGoS61VPfm9bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a429dbfe1a.mp4?token=oyQNufY6p0FjqAAlvJ7fPRHbPy11N3BUWlkA3S7ToztN31OHitIU614i46Lzz5evQrtEIPUjt9_JEjvwqQPkyphCJU7xehEPyN71eXtioaG-9fxayDEX8PEMDlMfRPojgP_0hd_rJlSs20tKa4pAwazw5Zs624x8KEjyeC3th4EGlTyRC5HWtdIeOEXxMb3hgG2mwY69ZQ2n-rhYOKaLuLCZtp0mwfPCt1aTYW5J5lpGdRtWJI24WuBDoziNIfxmgNyFLzHBR_Rc8aAez-2K9TbIR-IOVZvXTW9a5QitDqw9dwlCcoOf_8ujqp4Sx4fSObn6dDuSZvGoS61VPfm9bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
هواداران ژاپنی برای جشن گرفتن تساوی خود مقابل هلند به تقاطع معروف شیبویا در توکیو دویدند.
✔️
آنها فقط به مدت ۴۰ ثانیه در حالی که چراغ عابر پیاده سبز بود جشن گرفتند.
آنها هیچ قانونی از قوانین ترافیکی را نشکستند!
😭
😂
به محض اینکه چراغ قرمز شد، همه جشن را متوقف کردند و به پیاده‌رو بازگشتند.
😂
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93301" target="_blank">📅 21:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93299">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X70YGpxLOAXHbI5tvgPWfkHHravo9pCfegb0izpO_DhLuZKJAljMrSICESGzPA_Qp_7tOS4kRI8CCQPBTTUTHoax2aa9gn_mSSPkBa7fJqLwjVV-xAUe8X02GXDGAJupaRuA8IRyGstedOcTeySxWXBWk7lOr0xIdP0LUKUd54uEoqxM7QhV4n1xdTKVUnjbdOdSpGlkQ5X9pLPDNL5_ehstI6N0ze6AJm2c2XnQkM1ycv8D5Zz2O3Map0KrIqO-ZZcVuXOiNdGiEZvHsMUZ8K4pgh-Fk9QaIC87HWWkZSRNDGoVvm3GHXwLgjuzxjDrW95gOYtPHzgYrscCsDBumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد از تلگرام بدون نیاز به ممبر و تولید محتوا؟
سیستمی به اسم MTP وجود داره که باهاش میتونی وارد پروژه‌های واقعی بشی و درآمد کسب کنی.
✅
بدون نیاز به ممبر
✅
بدون نیاز به فالوور
✅
بدون نیاز به تولید محتوا
✅
شروع سریع
✅
آموزش کامل و پشتیبانی
🎁
فقط برای ۳۰ نفر اول:
سه پروژه اولیه بهت داده میشه
مبلغ هر پروژه ۲۵ میلیون تومنه
یعنی از همون ابتدا امکان رسیدن به درآمدهای بالا برات فراهمه
اگر میخوای جزو ۳۰ نفر اول باشی، وارد کانال شو و شمارت رو ارسال کن:
👇
👇
👇
https://t.me/+QpsFnjSfC382MGQ0</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93299" target="_blank">📅 21:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93298">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dy71FOsLbl6t3buuz27jPw15K6jgeQ_IDwz4NdESTbBma8wq-kYV1zWfkU9s-UgwPlCFAKTFFY-ubGecRWio7A9vtC6615lzlYuSAvuZLuQjJ-6tKTGfWrJ6Jsw1rdp3VP1WCTiKuBRPtbWYXWVj3K58ckaIbYYpAfcn_uqOww_rs19BSAj4GukwLpDXnU9_qixXMcHn5dxPVZ7719as7zyeB4CB14syWhJu8MNDIg8V6SdGFg2AmPnzjl7UL_RmYnttL_C6xYN-zkKEISn5pWM8e3OH9EwWc-3QzWbDxwxrCMTLlNLOpjmXmgIKQa_MjaIZkUDjb_TQ8IrLuzH_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیگر کشتی کج دیشب تو ورزشگاه برای بازی ژاپن و هلند حضور داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93298" target="_blank">📅 21:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93297">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evjGjmYEFRz-xX3hEy1TMvKKr-AWaJsekf-0nlj5aA-Hpxo-br4OoMy42ImnFUjFPMdNV0089IoUjy7NB1UjMMEvKjFMlAj7DznCaL9ZX_upQDoMbeQVk7uRlfkp8230LCOKln61BMGUfQUuhDnObrQbxuUVSreSIvmVtKbugVmdWBo9qjv9ewdl02JLAd6WgAsTHL281pz2SyBZObbxR_o_1_GG7hnQlZWMXKSUJNSK9kj5ZBWanvphl--bDpx8GGAbgM3ygJG5lw-EIxA88Tmi5TO2p1heaNWDx6_FyXqq-7IwUk2WmiVWGIKi0e__hLQNsQ0Z5ihib23tlRMtHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇾
👀
🔞
ایشون یکی از که مدل های معروف اونلی فنز؛ برای بازی امشب رو برد اروگوئه بت زده و قول داده این سری به جای عکس؛ فیلم خودشو بزاره
✔️
⚠️
🔖
🤤
عکس قبلی که سر برد قبلی گذاشته بود رو داخل ربات پایین گذاشتم
💥
🆕
🖥
🔞
https://t.me/FoootyHub_Bot?start=v4ujXYFM
💦
⚠️</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/93297" target="_blank">📅 21:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93296">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یامال بالاخره وارد زمین شد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93296" target="_blank">📅 20:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93295">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دوای درد این بازی یاماله</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93295" target="_blank">📅 20:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93294">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کیپ ورد عجب اتوبوسی چیده</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/93294" target="_blank">📅 20:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93293">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اسپانیا از موقعیت هاش استفاده نمیکنه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93293" target="_blank">📅 20:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93292">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شروع نیمه دوم</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93292" target="_blank">📅 20:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93291">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOLD0sKW1vhyn5GUsazVhmQdGiQWdYo8jhVOuFMmplqMgy3ciwyHq71XZWWT6K2CxWMC9iIfibmEgPO8W0iXYng2faOJd8yJMDZcAtx7vBigZH3HDiDGfMMDr7PUG5dWZtWDZ2gohiEHmBEy2Z1t3ytASM-QswoOa-COQKKsfa4b06UmKxBIC31Pj0e2a9NLfb4YM6UEZS96r-XPYqcrrKvkq3Uhp3WCT7jpyp8XjG1eoWDnnB2feV5icZ6OpkfD-cOQvmP0q4UH--V1qVzCLVT1PThpei0bn0DnN0WOQdouWv0P9Xk-Q2NY7ZIICn3c9mYHlkCgGYZko7Tx5ZQZmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تام‌هالند(مرد عنکبوتی) راجب خولیان آلوارز:
🗣️
تو یک مرد عنکبوتی فوق‌العاده خواهی بود، دوست دارم روزی با تو ملاقات کنم، من از طرفداران پروپاقرص تو هستم و امیدوارم جام جهانی فوق‌العاده‌ای داشته باشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/93291" target="_blank">📅 20:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93290">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/510d539031.mp4?token=BD6rEE6P3-RX4sZrrdoyI4gW2xeUBwDBe8fdiLhJLNz0dRcMQXPtank0pXthVdnUqkxjmDn_k2l-LHx-oU7Z0b3MvvrnfW9WWFhTHpOb-oBf47y54pvqr6Tx-9Imq-jadzES34OoEdzvtatrNqPNv7eouyUAXZa1B42UoBBDOnYwRFhZdeimeaZM48UukAPbwNbU0W03WXkdlt-pF3dabAuPRcvUJCfTMuhbcyS8yhuxbxB5IipH-0clOFCBP0qWjg9RNV3k-oC_KEt3rr06v4lGPbcaSFbO2wbg3wu5jGYkx0NpLk1XJ2rYhFBOb7_l6m218Uu3218xUWRsEeSebQExQN_ugfBy729xwZ293R1_9Zl3aDOySK3RplR68BSr6f8b5Wij8wKZJ8IcJvG9yyFapXmIScA_NyUYHZUKmmfXhp9JVlx-kIiG7nD7ZTjf_aZ3KKq4f2Ql9mh8YukSYjVFoOXeTAojHneszfqRh7XT0puAHK6t9qlmRwqHG2yBbs7VxgpYsdzHwItKy6QIHBUJsg8A2wXKrRlWq7kFWNAPEDuvaU9GbaFMH0UHespbNvUFAz2OB3IWc013oxR_5TmzAkP1p7RKozBk3DI7X97kA4FgtnGfHgLCXPb5yCe98LNQLsJXen7AuuDwIdKlrcxv6y67mS11qoimfE-MhXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/510d539031.mp4?token=BD6rEE6P3-RX4sZrrdoyI4gW2xeUBwDBe8fdiLhJLNz0dRcMQXPtank0pXthVdnUqkxjmDn_k2l-LHx-oU7Z0b3MvvrnfW9WWFhTHpOb-oBf47y54pvqr6Tx-9Imq-jadzES34OoEdzvtatrNqPNv7eouyUAXZa1B42UoBBDOnYwRFhZdeimeaZM48UukAPbwNbU0W03WXkdlt-pF3dabAuPRcvUJCfTMuhbcyS8yhuxbxB5IipH-0clOFCBP0qWjg9RNV3k-oC_KEt3rr06v4lGPbcaSFbO2wbg3wu5jGYkx0NpLk1XJ2rYhFBOb7_l6m218Uu3218xUWRsEeSebQExQN_ugfBy729xwZ293R1_9Zl3aDOySK3RplR68BSr6f8b5Wij8wKZJ8IcJvG9yyFapXmIScA_NyUYHZUKmmfXhp9JVlx-kIiG7nD7ZTjf_aZ3KKq4f2Ql9mh8YukSYjVFoOXeTAojHneszfqRh7XT0puAHK6t9qlmRwqHG2yBbs7VxgpYsdzHwItKy6QIHBUJsg8A2wXKrRlWq7kFWNAPEDuvaU9GbaFMH0UHespbNvUFAz2OB3IWc013oxR_5TmzAkP1p7RKozBk3DI7X97kA4FgtnGfHgLCXPb5yCe98LNQLsJXen7AuuDwIdKlrcxv6y67mS11qoimfE-MhXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
هاجیمه موریاسو سرمربی ژاپن بعد بازی هلند:
چون هدف گرفتن ۳ امتیازه در نتیجه تساوی برای ژاپن ناامید کننده است.⁣ فوتبال ژاپن قویتر شده، چون هم رشد بازیکنای جوان در جی-لیگ بهتر شده و هم تعداد بازیکنای ژاپنی شاغل در خارج از کشور که در سطح بین‌المللی فعالیت میکنن بیشتر شده
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93290" target="_blank">📅 20:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93289">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bs06Np4_mCOh55z-bHbwcaAUYw2RC1SYrQWKf48EGn-KfW7sM6Z8xwlviXY_ad_6320VVzrxZTXRCU87nbalmxGI6ahhyO6DqSK-jnrJ-DfFhCR9OSuWCiSgDuWK3_sAhM4KasoQrV36_9LZeJT8ZRcnUCSJ3wIpKVLvMwVQpGVzF8DBvpD3Mcbj5EToJ6xb5WD-mRAmzsZ9iOuaheerz6ZiBZEVy2aWv4QwY-EmyLjXBIiOWRJf0MHJD6RwRnhmm3NGOJt0j_R17njcBZ7aYwC7Xkz19ow93sq0-hGE5aFPQ4KCLVkePtPXT_tFz2yvK3P0jN-8hwY90vBS6-ZkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادار کیپ ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93289" target="_blank">📅 20:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93288">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/93288" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93288" target="_blank">📅 20:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93287">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRfyYw6FgxUwZ_kVcNn-mhvTJ0tWVresThMhM1GAyP-6COXbGkh8X5-9proXdMpxisLJoHF8j2dI8XbbZnKNV9-NfxE82CkGX3WPQ_OEJRYh8rjxTHBbQwp6H1x2ztJcN8X7w4EsZW8D4qQfULSGH0Wmc0Iq-zmZo47CME_HaQftC8d5ndkFpWdlTL7MGdlN2za8peUdkARTF7iQFSGdjEcT4TLDi9MeQ2YIxFaWMAEkRBU9IBPI9ZjxkgJzcnjI1up5r6EIqyH2VpWN5KwPNZPxFc4-sFUw1xqX7KFgTU10qM7wZLv-W3S_W-BODH2mSbehdrWSatAUNm2GsvnokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93287" target="_blank">📅 20:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93286">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ih1GkZssBy2MCNuj01z7xvbCOTLe9_GTAyaqTuEwvR9eWHoBsx5PHZ4Wn4pdTJ433yTsmSFA8vAPdRD_I99979vyOpGMP25Z-fznNqZ0yIodZOk31jgGqSUzhQwJGHUTCsuGMEsljkJH8z63opRi0eC-BC31nFUxj72EFA3wVBNJazaEdchWvC7zvVgkFtCrIKjwdvErLHZ_R3WU31VMuAAw5zEvV4sIlaAXrjcbIjW0v6wjJTgHVhtizpAQ-jEVvuguHEEUP-Gl6yHy0wAXXUjs3wf9veYbxMtRvELYdrRPjUPPcfsGuwFF6UO3u6CkuCn9PGGEVGfbvpshZNDNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر چهل ساله کیپ ورد که نیمه اول ترکوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93286" target="_blank">📅 20:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93285">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6cm7hjWOd9SFW7iRjGzv-boCXmqkdsVs8X_0AlMtiY4hOOaFpgYS12MpLXr77c2kEmDKNC3UdMGjTxzhfwjGCZWOGROBX4fn2hquObuiTs2TcAjs4pbOMqpGaeez71KEog8x-RsIrz-9M7hYafjWr09bfKiE5ChrHlcj32b44_OKGAW9V9Lvpu-Q93QE5U7rc3Uc0FeaiSEW5wpwwkwf1cTboXOwC0GDFaGOumxLiB59R2-RqpnIcqWkc1PaSS5lB_I0ZumO3Lbog78sdKMRTcwm_-ju0Jzu8ck1k9uwZxqpvfo66eni1IMVz03mSsSRmSOQaLmdTOyoUazlbjnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🏆
🇪🇸
#فکت
؛ پشمامممممممم!!! میکیل اویارزابال اولین بازیکن در تاریخ از سال ۱۹۶۶ است که در ۳۰ دقیقه اول یک بازی در جام جهانی فوتبال حتی یک بار هم توپ را لمس نکرده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93285" target="_blank">📅 20:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93284">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پایان نیمه اول
🇪🇸
اسپانیا 0 -
🇨🇻
کیپ ورد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93284" target="_blank">📅 20:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93282">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کوکوریا چقدر خوبه رئال واقعا سود کرد بابت خریدش</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93282" target="_blank">📅 20:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93281">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عجب گلری داره این کیپ ورد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93281" target="_blank">📅 20:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93280">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">عجب گلری داره این کیپ ورد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93280" target="_blank">📅 20:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93279">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmvpuzMbG4IBHzmo6B0uiB_5nPItbcnfKoFCfk65n1q9jOlUOjoQh_ETmiFuoqZPC-OcCEY4kcjurCj2tVtK9rvx8a6qKLItQIwxuXazu0HthM8ofnpVWxqfSIRZJ_qG-jwVE8TEpWlyVcOK3UkwpK-daeW5YHZXHcT4VViC6z0blf0TQ-He9T-gElzmRzSG7CA0WLSN1Ixae7VYuo0PKHPGX9jc-Lkg2h7ssjkenBSH1PrLyBF_KR-P9VEBhZCHiD2Rnn40qeL4Mkton8j_P0ZNRZxKbo5MjfkItKnsnWIYyBjJQ88CcLkeqf-bqZ8luo8ZdpPhlTJrkygj7wwwLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تصویر منتخب امروز جام‌جهانی؛ پیراهن زیدان در دستان بازیکنان بزرگ سابق و فعلی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93279" target="_blank">📅 20:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93278">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz-bUVlpzEkqc0uqEgWTvHYBr6UmgD1_TQDVgdefgfxmHRNvwyK6sWVwAckiPRHraKtwHVl07guPcRifEifZh7WsF8XnYSKnjVtWUmI7MowYoygstP4U4fUkVX6ZNx6YF83OkID8Za2USViJcE9CckwS8J4e_vw86LpsCya4nXlGfzVrSC4Bi-z3BbRfgLvqGxtvDPYYJjg_RFAvVSvRAK0y9QGivNWIzVhTJmM0YbN55CSfZ4sB6il821eLnwOn6dD39K7EA0vJbj4r6KhJ_DtL-sHsKgRQxdCy-7QapBpuoIuRnSA-_1EZHpBVn4d_8VUElUrFhLf3Rb_yp5rmfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو حالت عادی همه فکر میکنن این توپ گل شده‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93278" target="_blank">📅 20:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93277">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فران کوسه چجوری گل نکردی</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93277" target="_blank">📅 20:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93276">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پشمام اسپانیا تو شیش قدمی زد تو تیر</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93276" target="_blank">📅 20:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93275">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسپانیا یه موقعیت عالی داشت اونم آفساید اعلام شد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93275" target="_blank">📅 20:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93274">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خوابمون گرفت از این بازی</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93274" target="_blank">📅 20:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93273">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM6c-OiytaAiWiAVHlfh_TUYdnItiQRLiZE37d0QtwkdYcd2-Pkmcetfjshnc5W5HRsiH12tF61ZWtKM1LNvbacweffkRFkaCaL9Rco2BS4oMQ3tCDSWqhJVMgm43Ob2fKth9KNo6PFmws6a9RLZAzkfm35tVJv59P2lUMQv65DG_coJZ-r4-WvSm2kpU9h5BXoFO3YlLThE92g-xnA43MXY_cOUuliWWJW2CEVaP8tLBOOq3llGYiYFMje4RcRAp9NAZ5j7lmmTBiHPm1_Iknf9UgIE9QnW7XwLaBwRyUdMXtPwLWqOWC0vq3O-gdA43GdzPgM2dVaT4ddTbTbaug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
ترکیب مصر مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/93273" target="_blank">📅 19:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93272">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جای خالی ویلیامز و یامال کامل حس میشه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93272" target="_blank">📅 19:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93269">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ch-qOEUXXH1SOgAJh2lSoaqrZfzIkzEmQA-z9vXxPFsx9Yzi7zk3wSX9wrEDUjkmW0q4_7BeP131Azl3mXPCvg30efJjyMl59VjBGtKqWrZEtGAzRoeaAvOFxXUc-wQ4i_ekRDLZP7pCHCKGNpighR2737R-_Zi-S2Ysm-bsludrf1AMczGz9NuuPlOoaK2ZRW20UzVakyc1LbW-oYJ3p7F5pcl9Gp0xPdRO_rkACxF4FnSRVt2MJ_mp222MqWN-63mHz9c5VQgga1Ismdf6OHpLwVF-3nVnoLhbx9hwtKzYxuw3b9TiipqlDL6qGQGUQMngMWGPXe2Tf79y7YbA-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FORqbU-88y7nUVpvhGjoXMH_WmSsNUe83s-tX6-k-v9YcRVnMjd-UO0TYwyP88ErqA8HMjgAVNw-oWfg19zr3qnARQgD8TzxtFmoijbG3f5NduA1DzvviDypcgo_6Bja1MqztemVbUqUW3Ks-PtMVSIU-gKQX0OXpdNX_KOi4AVuf5Vwk7zffkz0w4CgoamBmsgp8gcEdcxweLHmB_PHYf-4k5ADq7UJFllJDJfGS-ES5LOEW6Ub1HxPjw6Np99QKfrQu10yOAc-ILXHDSTyAyrUEcW6fCW-gS9TqfFc2jBMqmOU44XkgqdI2AbFPpoAqTNu3Y0_Ov5wyRg35WE3Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r6cPukQu7-zuf6O7qLRMzWDWnugpOsPRAzEF5vcb63QAFxT5XxViXRmSarIIZZa-hyGEPrtXKwbILz4xzZO5f2VwJ6Y8-HePAmrMcy57M0dyJyNXumEzcUGVxdGRPHeBQPVpc8IFQ0_HQxWktbQydJAFlgyI9BgJn4Co8Zz2k8ruMNigz_XOIzTcOaHmH_ojGvIv9oKSAnzHhapLDxtunGCDWi61B9Ey8dk5XjbVbn6iGOQ6rwbHq0TmCF7a3-l1Qj7BOlF9rSXFzuxlqalI7tNkpJTYxP34sGH9wcF1IFDwfNFDK0BNgGDY5fsDUz6GjJSLhvat1Kt1cItMUKjvYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دزدی که از دزد بزنه شاه دزده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93269" target="_blank">📅 19:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93268">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
ترامپ: ما خواهان روابط خوب با ایران هستیم و اگر این اتفاق نیفتد، به جنگ باز خواهیم گشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93268" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93267">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اسپانیا توپ و میدون رو در اختیار داره اما موقعیتی نداشته</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93267" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93266">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSU1SrRip_H8LSBGJvwItOa90nh05TVkP_KuuV1sVavBb5e7ducYQaVz8EJMC-XwHTIWKW7KK1T0dN3xJNu4tNbHNJWZyBagDDKSx8u79DU5gzj6d9krbDCDHQyQbiH8gF3wLIO66MXMw57_Fg5q-CLddoaPcx9dMQ6j5u5C8kTYubBECpxLYGrvAGh--ZAwo-Pd9FLOV7ObgokpSyk16nCwraPE9iEyimh-frZguHTOt4D0Rv5MLEfsRjUMthznSl7dMDTzYejXpYjK_aiR3122g_1FB5PROblATz41JE-diN1mdWaufbdUYf9A1R1wl90RUSFnO4GPde9ZiqG5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تام هالند رفته بازی رو ببینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93266" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93265">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بریم واسه بازی اسپانیا و کیپ ورد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93265" target="_blank">📅 19:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93263">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Omhx2z16zeVQco_g0aNQt0tdJyqJ35hJmY12HaCSJS_pQSimD53UdoyPQ7pzCxt98lfN0HgRpImVDHyt5rX88GK5Zlp-T5np5mx2y6oNxtymfOFdu-_807lSSdXcDN9ztXcgx3GuItCxnGUi_265u2-8oQp7OgjW1MtoSnR9H6vVso_tPIttzJ_egkgAQddiUOTAQ6nkiQWQpsAOj_8JdvQ4rAqybG3V7XrIG2vDZCVDowZ0PyntLACwtKjWFSQCJ7QJMH6b4Xds_1KVeJ-VG0Sw3PkuO9LupaihuBSWwICSpXC4diLSEWtxbpoSjWbfynhpahRhJUxJa_fHMRFAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BWUFVed_F-1ecRyIV-KSov1ESquViMGbTeJGaGFuEEk5lTEYl9siOLES8--_OeyxE7NRipIXIy1J8JKIMjRVZefAyfvS0czmlZ9yJFeF2AQLD_wPWEww-gdX5mnX0RB5b2Xk0xLS51R7xV9k8ninjsMGcLLGs0hP_uj-m-lPD0fPZd_fL4XMJYMQIYZQaOphAhFo6B2GYmDHyJTQrgW5nMBt7ooc7bcquxBKxkKQlUqmDTa-SVfceHdrmyE_Ohwo86Um-7PSxAwWwyRWwmYG-uSUVqrJ-2OkSNRAnm2eDiRWMZAD82qMMHMMFp33_qbLjx5QegAdTnFWy67XDp9c-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
یک فیلتر میتونه همه چیز رو تغییر بده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93263" target="_blank">📅 19:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93262">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5039f86f30.mp4?token=N-XO0dLR_iADcrMnUcA88H8I6bhoH2ur1XvsL82NBfMEfxLmF8pgzCU213hImN6zcn8YfxmahNyWthaNjRUClgPuldd5yHE-8ARtthMKgbkUyf8P6b42xm54ldbToF_okE-nxxRrX0n6Qf8Z0J6l7DaVcMdcM3leabQF8yufGc5uPV0ZS4QM8nBoMCzhLNqOpsAmYLs3N-WQamIjCsBbW3HhReMBFXXKjY695sySV7qDi6Pepm5nPiHD1B8cM-YbI3slCYX9a6dDGkNv_7Z6_WbDEUjE5jjBgT5iPLWnqyJ7VnpBIgM_wHo7BKdj4BTPICY3jtFk7HlIanc9BjVVLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5039f86f30.mp4?token=N-XO0dLR_iADcrMnUcA88H8I6bhoH2ur1XvsL82NBfMEfxLmF8pgzCU213hImN6zcn8YfxmahNyWthaNjRUClgPuldd5yHE-8ARtthMKgbkUyf8P6b42xm54ldbToF_okE-nxxRrX0n6Qf8Z0J6l7DaVcMdcM3leabQF8yufGc5uPV0ZS4QM8nBoMCzhLNqOpsAmYLs3N-WQamIjCsBbW3HhReMBFXXKjY695sySV7qDi6Pepm5nPiHD1B8cM-YbI3slCYX9a6dDGkNv_7Z6_WbDEUjE5jjBgT5iPLWnqyJ7VnpBIgM_wHo7BKdj4BTPICY3jtFk7HlIanc9BjVVLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مملکت از وقتی به فنا رفت که مردها میل و کباده باستانی رو گذاشتن کنار این شکلی ورزش کردند.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93262" target="_blank">📅 19:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93261">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
😈
همراه با تست رایگان
💵
تعرفه‌ها 10 گیگ — 170 تومان 20 گیگ — 340 تومان نامحدود — 450 تومان (ترکیه)  برای خرید بهشون پیام بدین
⬇️
…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93261" target="_blank">📅 19:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93259">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
😈
همراه با تست رایگان
💵
تعرفه‌ها
10 گیگ — 170 تومان
20 گیگ — 340 تومان
نامحدود — 450 تومان (ترکیه)
برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93259" target="_blank">📅 19:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93258">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPGEwZaDXYtUU4Qgiqh3S39Moa6abAEd77o9CNsGajRKctIIvKkapShSdd3r0sF3_98TjsUNdDv0ZNkA26y26nvDH4NQG9nfan9h3M18tVR6PKNngflrylnREDMaFFP3kAzzdkTrFp-GPIe3XjWH-A1uhbRbxGM9IjihnyURPAgag4Dz8CpxftkDAvT-IY4_5bB9-u0GjFdQSpqiT-U7iXm1FVssXJsWTW5yNwCdM9_ABXT2R2yxgo80PTDq_RkZmXJqzjovRGaf7DVZI3PmYknkda5_6sTp8zGIuLkT5nu2cPutVHmmG6AsFoVu2pgTR_TCQ5lcIJkpx0YRZyTDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
عمق اسکواد پشم‌ریزون رئال مادرید برای فصل آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93258" target="_blank">📅 19:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93255">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lgiHoVw430oN9mB9GTAtfj6fX1KxPG5PwBEvBQnr-ZcofVNKMaSh0PH228ZQ1BFO3Z-0aLsnSI4VMjx02nvRULcS344InGhxOnozLoTDtZ8JpsbJazyRv_KptMlFgir6TMMFjO1Ve9EKlLFUIKnDndREn-mSTmFfaQ887yI4GtEDwmPv3nuutBEcWwRkHk0ad3VmM2F0E4Tkoqc3LRUG3lpKqX2u9rBs_tx78IdEmPF0Id5uwVy2UU4Zvv9zL6SWnDcsNpfm181qLplXDjARqT84y0OKmZwM8amSR5NrHV9xnYsBVjWCXmZGSnuJSVQ4KgjrEJz5EOY3Er3PbEtSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRwVFAgBxsRNyHtOz6kctYpAn5J1wTIQLU7NNB3dkKvBb2BrZRUqahYpLNC59pUtkqNL0UuFF4ipK3GVkR9NO-e2iUzPjIa-GHVseztDMPBsJnSSo16z7g9c_hvPTzCJlkgMBHlBB_3Hh9gIUDTl2C-uyXI-EEOH_HQPihuclsb1K7tMtVwCSEClC7ll5C6iIbTU_pQ8KTOgZdQcX473vLxFFlQWq_eIvkG3z_2xsSEmNTd1hkwv3xelXyr7lmw6Dp0VkPFfYTCALc2mJcXx0HK8T2Wlf0LSbp_K_AW69DsgSFsn7ArZGuIWHnQZlWo4F5m_NfNkifvfeMDRezVPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jcKWrjXz-eW8kQX0FB4bKtfERMDE_qA9yOTdBJKzW7UbUKsdA1Wbpi5nYcKrfQeMfprAHfJHfbiy-5xVqMrXyHrGK0hwrwQefGKeN15nOU7kkhAs0KbeWp-RUgi_jQBknBDG1FtniyMzkOAHjUfq7ubn7dScdU6mBzqdbiw96BqI6FWxPhX4ZLNvsB8zRBJNMhUQMIbJ25h9y6kCd-VD7E30l_7CpPRJvvY-iJ-GQ29I41OumgMwia6-UOMhP4zQxERymhhuc-SVWxrSRNhpNUdouPPwbAdnuvyLBR40KRtv16Nbcwp6smcetRSUPeNDBNw116GZ2nB48pcFT2X7XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وندا: یه مدت شدیدا از آسنسیو خوشم اومده بود
👀
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/93255" target="_blank">📅 19:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93252">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fF7es01VhddGdO8GAhQM2pFubtbGKKJIDiEgp7HlQWbwfEFgTN5B7BycqNssWSkWBLVSN98bNQiyYF94dlS65Nk9mHjpW2oQYW3pUDxwLSGfLHu1gUyHA3Igm6XhqB3SJYUoFHj6ulh46npEET13dE0c27tkm9kJ16l6r6RHKNju9klYqaarzLuVqP1FnHVbq64pEpMimlT_QyK_0hUxXXn3v9wtI9T3opcQxfyX1a15y0k6vleiSOoa2H5OdCeD7rTteOobJF9pKAJ9OqOyEYSmLZallN56PAPxyOw5sg9V7y5s6AVDoqVltE1jzlxxysqpaxitq_WIZD8ABGC_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cCXQEgAObLJQ8pwsF9o9wgEC8ejijnwSKbD0VhgchA9QOXh4grV_ZINM7yEmAGpC0AY-lBSTi3CH1zIjpo0e9bhiniIalMYKbQ58z6XfiCnYMSznULCD-Kb49ksy4pD2qkMiAjrrNg0tvfW6mP476w4jrP7BwFLa71znqIWP8sECzbE3s_HkNtRzm3GmkK7P0oNylqtoywaXkF3_zbIrtLXsFQBhLC-_5HBBpKs3bqs3v6NsY3PDKNrtq5pYhKoNzZgvCPiezliW7YHDUuvA01dr-dHM3HjVnTDb71K3LtANdEK9e3Hhx87BxFUw5PpZqNejGgZwdlthJrdDlGnJXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NR9qYT-bU6hDON5sajxRD1JUYx6IMHko1YhasmIdTpGAlfyAfRuoFYljZch3iFy_RdSvCwaI1H5UmT5fudrTobTqzQMtFLty45mSPxGF6kmig_pjYoDrZDXEnqpmYoBhMsZP5gMsM6c5KEhVYWQ-HX-GEGDZ1Pjooed-F1mtcZB-kKt9u9002w2nXfOUc6s7bW08LUdW6y48rm6vciWbCdknOzEb11fJi0Ungvc_jDEEve9KRUrHXdwM8OkehR8Az6vhv7Zvj8sco8X7deFoxzb5_SGbLU6cSoQpATt6NM4GlIyRDbtui4xUhuiqjmK8l0t3BJ7IQVesrt9ZmDE3Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ما درگیر خبرای جام‌جهانی هستیم بعد بن‌وایت اینجوری با دافی رفته دم دریا عشق و حال
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93252" target="_blank">📅 19:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93251">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1929949e0.mp4?token=cKta2Toa3m6rwRZ9RDFpJEV0hrRBBdVzBMW7NOVshONq5mjjtxaWdtWKZKo-TXzubd5VmMMhJbpgamT2GP8HCz-WWVLIOVJp-sUutD1X9oq6xo7OaZof16CBKCe3yu804zUjIPsXUlOWB5oUfKu_EDR8iDU_4iPleinCoGViPaOyukagX2oESZb9YckA8Krfi9-ONTdvH0tFibxVU5DbhKvRM2m4WwepbkCtv3NzwL303SChyro5AmwEfV3TBQW-E0i0e0gteIEzziQv0znEHlImhvuv6HZTbYEouDD3jelzQj5FWuozp90pOlfekCOLuhh3ZfySp62nVQ_5P3HJPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1929949e0.mp4?token=cKta2Toa3m6rwRZ9RDFpJEV0hrRBBdVzBMW7NOVshONq5mjjtxaWdtWKZKo-TXzubd5VmMMhJbpgamT2GP8HCz-WWVLIOVJp-sUutD1X9oq6xo7OaZof16CBKCe3yu804zUjIPsXUlOWB5oUfKu_EDR8iDU_4iPleinCoGViPaOyukagX2oESZb9YckA8Krfi9-ONTdvH0tFibxVU5DbhKvRM2m4WwepbkCtv3NzwL303SChyro5AmwEfV3TBQW-E0i0e0gteIEzziQv0znEHlImhvuv6HZTbYEouDD3jelzQj5FWuozp90pOlfekCOLuhh3ZfySp62nVQ_5P3HJPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محل‌بازی امروز اسپانیا که شاهکار معماریه
🤌🏻
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93251" target="_blank">📅 18:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93250">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87cd6dfe2c.mp4?token=oHSka-zDdh8lLz4OH61EfNV916DH2Pt3JtPZFm4SHU4gKMrMjygi-WG9k2QnYbVIW0c7YUKDp3DnlAFIKCVPyceJLWpYvkAfwQUpLeRlg8pBI0uf6rKWFKvoFwXHAvaOYZumcUULEjXeOVGCXm0dgsnKuEwxDj-ApxLm3rtwKS2u2GH85Ka-VyMS_znEuLNLWT4P6Kju0k2aXAaQO0FebVP4P0K2Sv2b3xuIOhdU9VuCyeQdR_1MqjzhYsTidApFe3s9qkozOznIPUYj-AUia-Z4ChP3238ST1j0D0aP2uq1sVg5JW3t9rvgXlvxBG6t4t5Kz97uvDPNIFlhxg6ZyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87cd6dfe2c.mp4?token=oHSka-zDdh8lLz4OH61EfNV916DH2Pt3JtPZFm4SHU4gKMrMjygi-WG9k2QnYbVIW0c7YUKDp3DnlAFIKCVPyceJLWpYvkAfwQUpLeRlg8pBI0uf6rKWFKvoFwXHAvaOYZumcUULEjXeOVGCXm0dgsnKuEwxDj-ApxLm3rtwKS2u2GH85Ka-VyMS_znEuLNLWT4P6Kju0k2aXAaQO0FebVP4P0K2Sv2b3xuIOhdU9VuCyeQdR_1MqjzhYsTidApFe3s9qkozOznIPUYj-AUia-Z4ChP3238ST1j0D0aP2uq1sVg5JW3t9rvgXlvxBG6t4t5Kz97uvDPNIFlhxg6ZyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی طارمی: وقتی مردم زیر موشک بودند فوتبال دیگر هیچ اهمیتی برایم نداشت. ترجیح می‌دادم در زمان جنگ در ایران می‌بودم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/93250" target="_blank">📅 18:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93248">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c36eec65de.mp4?token=pP5RCnASO0w9Euy0lRvA1nvo3JBJEjZtBd_doAuz3j0QauzNBlVwk-OlB_lT4y5m8uPUchzoNaDNUmx5RCOqkKiG7PBmcEnCQDWPYHQ2JuJ_bznRcIQC2Dp__ppc26U6-usZeXx0ndf6JfkDruf9Hcydq-eFMUGpxoFVuP4xxorJle1kO0kWYR0Zvs7mlerzCotUbJ5r2oJKw91AQRFQastrHoGzIDUJJhWazyE02vhfS8PLdhttSRBWeqOjvckzaF0LiwZe02vBgyomJwP-a5oLASOSw7k6vXan3nySTFr-462b4JVtnWkoUjKOogywJw6NMHVYFAcqk_L9Hjm1MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c36eec65de.mp4?token=pP5RCnASO0w9Euy0lRvA1nvo3JBJEjZtBd_doAuz3j0QauzNBlVwk-OlB_lT4y5m8uPUchzoNaDNUmx5RCOqkKiG7PBmcEnCQDWPYHQ2JuJ_bznRcIQC2Dp__ppc26U6-usZeXx0ndf6JfkDruf9Hcydq-eFMUGpxoFVuP4xxorJle1kO0kWYR0Zvs7mlerzCotUbJ5r2oJKw91AQRFQastrHoGzIDUJJhWazyE02vhfS8PLdhttSRBWeqOjvckzaF0LiwZe02vBgyomJwP-a5oLASOSw7k6vXan3nySTFr-462b4JVtnWkoUjKOogywJw6NMHVYFAcqk_L9Hjm1MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زودتر بازی اسپانیای جذاب رو شروع کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/93248" target="_blank">📅 18:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93247">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEEa-KFHZ_wOD4qCYa_d2xh_b_hbZFXwxGLpCuq-36k-MdT8hfXupCKcnQ9LF6s7ywkgJAfHTq5Q0HRmng5oREbZndW0QQYMXYj90uXLCEejRFjZ2c1EmORhksRbGi_Efu-4DwpDLGb_ggvA6OEB9SlUag-6YP8Yl1OUmTwpymVcb6c_anCCf7-SZKTen7EJJN4gg7crq29DKXxpnn3Luji7SsDxE-tR8Sj-Pyp4pjI0i-2s1XnfkYzeeE66nfyZP5utC1gNyOguljKdHo90cvqFaV_cnw6oD2dQO1xKbmgCV0paIjSfRHzebviGl0J9xdpvhvXaokEGCLQozBQcBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇩🇪
آلمانی‌های جذاب در روز گلباران کوراسائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93247" target="_blank">📅 18:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93246">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b474c596.mp4?token=gx2NlruGHc3rZmmeboRH_3DVUo4bBC5c37HJme-Gldyg6VFBzWGhZb1xYCd7wZZP7bcGen4Fx0hRZB04_N5KJydP-2PNWN1-EUCY7q7eIq3nRrwCOvnzPxNMy2XzxgE59AKlUBp8UoI3R2UOuWoAisddhDzbCC4WZ13LDnVbW6cyE6KeFfsM6rrDUUa0bjA-Z0QXjWSKVdAvrcI84BNsaGn9eA9R74k9Tqj8dUaEt7OHPH0IyspA127mr3y2j-MdWBpB2kPTgRuGg9AtKtJx1Z9bxBF0XqdAv3njf4bEHBuqsKflMn5ETWBqnxONQL02WKPHua3Fc2bfrmRftmvrew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b474c596.mp4?token=gx2NlruGHc3rZmmeboRH_3DVUo4bBC5c37HJme-Gldyg6VFBzWGhZb1xYCd7wZZP7bcGen4Fx0hRZB04_N5KJydP-2PNWN1-EUCY7q7eIq3nRrwCOvnzPxNMy2XzxgE59AKlUBp8UoI3R2UOuWoAisddhDzbCC4WZ13LDnVbW6cyE6KeFfsM6rrDUUa0bjA-Z0QXjWSKVdAvrcI84BNsaGn9eA9R74k9Tqj8dUaEt7OHPH0IyspA127mr3y2j-MdWBpB2kPTgRuGg9AtKtJx1Z9bxBF0XqdAv3njf4bEHBuqsKflMn5ETWBqnxONQL02WKPHua3Fc2bfrmRftmvrew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇶🇦
داف‌های قطری در کشور آمریکا سرمست از اولین امتیازشون در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/93246" target="_blank">📅 18:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93245">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هویسن:  اسم این بازیکنتون که تو اینتر بازی میکرد رو یادم رفته اسمش چی بود؟
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/93245" target="_blank">📅 18:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93244">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هویسن:  الگوم راموسه و میخوام مثلش بشم شاید هم بهتر از بشم
😳
کورتوا هم بهترین دروازبان جهانه شاید هم تاریخ
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93244" target="_blank">📅 18:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93243">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دین هویسن:  وقتی تو رم بودم سردار آزمون هم تیمیم بود منو ساییده بود هی میگفت بیا ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/93243" target="_blank">📅 18:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93242">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6178cd4640.mp4?token=XUXJMhILtsr32G1p7i2lZkIbcjANyYj2vixjAg7g69FFVBlDU3vU8_QcjFnRoJo7lrDhE-DczD69iI24O1skjwZe9W_SQw92rUI2UF4gH9HNcK4dRXg3gOvDq_q2S5yd8RVYFMnlv3BnjJP0iQj8d8HfNeZwghmTqR3_y1xqw_NccA2bve-nz2RD_rWC9u0ow4RTCtnPxDHubE1MU2cFBc1AEUFk35O7kkct-KYw3Z1_6pblgzF1WgjqkQCrNST_V-X2E-s3-l3gBmO6cvBHf4r1j49o_Wsn-sxoq0ebhU7wZFs_xvEP1xGCJzJLZ2nl7zSpopk8lOERqiL9oMg97A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6178cd4640.mp4?token=XUXJMhILtsr32G1p7i2lZkIbcjANyYj2vixjAg7g69FFVBlDU3vU8_QcjFnRoJo7lrDhE-DczD69iI24O1skjwZe9W_SQw92rUI2UF4gH9HNcK4dRXg3gOvDq_q2S5yd8RVYFMnlv3BnjJP0iQj8d8HfNeZwghmTqR3_y1xqw_NccA2bve-nz2RD_rWC9u0ow4RTCtnPxDHubE1MU2cFBc1AEUFk35O7kkct-KYw3Z1_6pblgzF1WgjqkQCrNST_V-X2E-s3-l3gBmO6cvBHf4r1j49o_Wsn-sxoq0ebhU7wZFs_xvEP1xGCJzJLZ2nl7zSpopk8lOERqiL9oMg97A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇸🇦
هوادار جذاب و مشتی عربستانی در انتظار بازی امشب تیمش مقابل اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/93242" target="_blank">📅 18:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93241">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
فوورییی  بعد از دیبالا حالا فردوسی پور با هویسن مدافع رئال مصاحبه میکند!!
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/93241" target="_blank">📅 18:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93240">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2YARgmmC2RL7BcOpZ4Q72YGlRcgg9C_zEAPTvBA1FfiqD9KEiXUtXpwywjQw1woRbDTANbPlPulbwu3jjeU8TCbBWcF2uCeQsKHtIk8YPtzmHYNkWLyGz5cbxSZzIXd3KwPt3AEL4RNoIow6Ayq6ZgBt5z49_9d-6ul7G4CvCM9eDn0mM-155hgXoJgYPv_n7ey-mr6SocMd4-8QUn6ZA3vQE_M7it_EzdNZM57ANK9q-u9r6QGGiCpPJslfQUpLxFr25h3hnWYGisFdbFvE2_rcPfqCaY8JsCUqDXyjMkx71GiHIdBaTx7NJ1DJWCINJcoESeG7c8KAPI5kSUhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آقای گل جام جهانی
6️⃣
2️⃣
0️⃣
2️⃣
رسید
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/93240" target="_blank">📅 18:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93239">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
فوورییی  بعد از دیبالا حالا فردوسی پور با هویسن مدافع رئال مصاحبه میکند!!
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/93239" target="_blank">📅 18:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93238">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
فوورییی  بعد از دیبالا حالا فردوسی پور با هویسن مدافع رئال مصاحبه میکند!!
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/93238" target="_blank">📅 18:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93237">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcaPwyi8eK_ebUgnLnGEDfEJCgZVuPi20swcsN9mQrN1J5nriJCeA6AoVLwqTbR8rCMb0t-6fy8zlrf1kGXZYa8CK2YQj6dneglXaSfkq8jZVLqMA_mxIPP1vGT5xEa5Og7WYwW0t9NFICstxQ_BFrB1BDy8QFbE83u7fj_vXegnXlSJvbHm3CcHe_2NtFbSqXX_K90QD66_jPMe0JziD1eFRfzn8jjQvCJzEfnQ6v8ogrrIuVwNRXzdLBda4Rc1-yphOrW7xSZVIIcal1ryYINAcIBmkD7mkVuX_oGmJyIH9zz8jpnoYCLpJ4o5jlZ5M6fTuG4ouPUPz1xWKDtXpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوورییی
بعد از دیبالا حالا فردوسی پور با هویسن مدافع رئال مصاحبه میکند!!
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/93237" target="_blank">📅 18:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93236">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کلیپ سوپر آدیداس از مسی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/93236" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93235">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTmKCB6iMso06LBqcpsrAPISWXWR2ipL1OfWCqyW2K2IW7YsfMGApO_x8deshL5dcxvTHQz_c9FffELtv9EEjSLNr1HBD8tkdCPTQ7ITZsn_Mt3w6g8759pCwJKq8UgJ3wELgPlmoeH_rkK4-d_KRL3zJuY9RXOTlUm2D0YbTxhonlqQtgQ6HkdrC0DywwSiGuF6Ubp24GJAACO3khNeGgeSCKm7QlVsQSBgOnMovvnEqJmpH1cmmkZqJ9-gTCwofCx1oNpNbC5QfoejtnJDF1Uf6-UQWhHtbwYW71e1CI4P6UHgAi9nvjZ7bSW3tlQd7ESHrsWK7vPKCMy5KWdX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست دختر کش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/93235" target="_blank">📅 18:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93234">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
ونس: امیدواریم متن توافق با ایران این هفته منتشر شود.  خواهیم دید که آیا تهران حاضر به امتیازدهی است یا خیر!  🄷
🆔
@EsteghlalPage</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/93234" target="_blank">📅 18:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93233">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f00a8073.mp4?token=Fpyy8psaCgHOqNrsuYH8N6Jrzfh02NZCrQwnjd-bKmQCYA9M0N-7oe-LGe8tyc1IaIff1th_HPel_O_VPx7sKlrOqhWx48M2DbUPKGqVGELCGE627OY_rrsG45ZiwV5AFKe-jIcr2ugCxZRkwr0RjIVHhMsOG_AUnyNT4ToX4F0JnFTPiCztuqjjLYvercBTQRUuxh7xT38cIgeIZqOKqLE3tzIj-VBS5H85N3oPRskq_cVh8t7unqYugW2E0fKN4Zhj3qurQsgvVr0HNiJGeXpxx3dqAt-kEEqOeQr2d87MPTDP_gEOlBrd4lZhY9VTZuSI4UufbbiSWk6tfxCuFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f00a8073.mp4?token=Fpyy8psaCgHOqNrsuYH8N6Jrzfh02NZCrQwnjd-bKmQCYA9M0N-7oe-LGe8tyc1IaIff1th_HPel_O_VPx7sKlrOqhWx48M2DbUPKGqVGELCGE627OY_rrsG45ZiwV5AFKe-jIcr2ugCxZRkwr0RjIVHhMsOG_AUnyNT4ToX4F0JnFTPiCztuqjjLYvercBTQRUuxh7xT38cIgeIZqOKqLE3tzIj-VBS5H85N3oPRskq_cVh8t7unqYugW2E0fKN4Zhj3qurQsgvVr0HNiJGeXpxx3dqAt-kEEqOeQr2d87MPTDP_gEOlBrd4lZhY9VTZuSI4UufbbiSWk6tfxCuFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای بیرانوند ببین کاراتو مرد مومن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/93233" target="_blank">📅 17:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93232">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTecgQxwStG9oeNE2zydJIBQhCjMJKJrkLhuhBtw-3oYgJQHHbIQpe28QYHglr-cWmGracR4f93k96Iw-dMPmH4_ggksYXONxbmy31kJZFEqUv8QBiM8Oflm9ToSIcczoHJ8nynlxyWYCjp4Mj8LDAUfwDqWakbsMBVrik9JTS7OX5AbQqVkxNPPmZEtXlylY_Sr7w9eRwUQ4YWFCzdDocfEnx4txQNsdizuvCFW8ciSd7FoDVUVQgYa3AeAnyilBlZgbSwkxiuhYRTXb7uOWLy_nnJI6b8Cldf9_OvH40pZEMDgDUM-ctUEBSCzAc5sZ089P6wZyo85shdQ8RnCnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل کیپ‌ورد؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/93232" target="_blank">📅 17:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93231">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk3Q3xh4vqSBl5nKKp_zZRRiL8yysej9s_GoyfoOL-tQEA6UGSEtoonH4vB6Ow-nL0F7-md1gGQkGg981DsbcKosPBOYT4_144ls8rsS1gRzzvxh8WNtGed8TBiPp9qBylvAKHVzjS5SUjMVuqT2BFfbkhr34VTTS_So1C70z_01AdIxResBU-LEt-BlrVRbsYd4dTMCY6-6vFQv49aSaJitSLnnFb9F6jWi74AjFr2KdfIodxcKazo2ezhyBrF-uKfsMBe_qN_TX2vjosSnBnbZ93whQ8jnEb1ygMSLoANhZ9Ie41EjIP37RwtfAZl9uukKr9lN9XTGHBSxn0VlKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران - نیوزلند
نمونده.
🇮🇷
⚽️
🇳🇿
⭐️
با پیش‌بینی این بازی، هم
۲ برابر امتیاز
می‌گیری و هم وارد قرعه‌کشی
Apple Watch 11
می‌شی.
⌚️
‌
🔥
با جمع کردن امتیاز این بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
‌
فرصت رو از دست نده و همین حالا پیش‌بینیت رو ثبت کن
👇
🔗
روی
«
لینک
»
بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/93231" target="_blank">📅 17:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93230">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc8gM53bvRWUvzrZ8eGnRpiBEAvhSMUTdf4qk5v9YqyU_F1lRKGjnw-eMN_JYQgZeE6BXVpFunO1fA69dn6F4aXGSLhigcHKskSzdFjL2ZpKgLbO7AVaAQfHc1juCV7kULlhvDruksujaD2FyQlHgs9Ca95jet75JfhSWQj1kxiGJqw5tYJY4nXH2WE39SLCTlxuCt0m8BBe-nZMjKX5Tg0tCvPqgReMSk-VW_7TmxjaCzm8HYuEtCxAsAg8urV2TqvSOstXuThf3upwTT69UOFn2HlqBAPG7o5cwnHqtDKTLUkmFq9BCIKlOIof9BR0uPGIQQHyyX-fOQo2R6iQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔹
آرائوخو:
«در بارسلونا احساس راحتی زیادی دارم. از هیچ رقابتی برای حضور در ترکیب اصلی نمی‌ترسم، چون اعتماد بسیار زیادی به خودم و آینده‌ای که در انتظارم است دارم.»
«باور دارم که بهترین سال‌های فوتبالم هنوز از راه نرسیده‌اند. وارد آن دوران خواهم شد؛ اما این بار با ذهنیتی پخته‌تر و بالغ‌تر.»
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/93230" target="_blank">📅 17:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93229">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_W2V329D5OU3ce3s7-XKcwiV1CSpkKYOP58-z-HMUdZSUVKdDYC6LIhluBDlbOr1MjUygc08QT-az4jZ68vo9XyDkCjZ2VBkIljqhHakvFZnsz6j7tfvQ8qgMUwjO9p8o5Zz3qQTpihyK3GC5e1wre9m8v3SAIzhXEzC4RbJwU9CIw26bW5gFsJlGxbvmAgigNZgejKWJUrsa4HNZp_h8mI_XGPbf028tmTRv0R98sZaR-EpVePxzijauyL8-MDQOn2mOQahN-ifEWMuK2Eq9d7e_eJ7PQh1YnWD3EJ6rXW1XxZJsJSu8ZSVpZ_Su0PDy7IIhdsiWCAWxQ6mW8PRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فدراسیون بین المللی فوتبال (فیفا) به دنبال برگزاری یک مسابقه نمادین بین تیم های ملی فلسطین و اسرائیل است
هدف از این مسابقه استفاده از فوتبال به عنوان وسیله ای برای ترویج صلح و وحدت جهانی است، ایده ای که جیانی اینفانتینو، رئیس فیفا به شدت از آن استقبال کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/93229" target="_blank">📅 17:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93228">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
ریدمان عجیب میثاقی هنگام شروع برنامش
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/93228" target="_blank">📅 17:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93227">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd99b8a0b.mp4?token=ZvrzH0vF7jzkQgKMNGDpQCZBctzkZUucYNsikcTrjZ01w9vJ4YVtf0YVVllmPEtnx0AEVxOg85eh9saK0kDb7GlK76PNlHeyna7iYxGqkmHbFppBKX5PoZz9ivbkw7XCMFBN9kyDdT_Ig6ZV_WIz_VrFYpV32tpIgjH5fU6qfk1h-DdJdVyF0c7brNr62LZVu4dT0dyp6XYg53kVMnePaUZo41lK9xqTvPBaBPqE9Qg0GFMlr5NDDjwHd_M0WAnmumlWwg8y2M5lQR5EU-nbUYLlT590wjcAUsxe5jiWtSdKV2UaNseQ0ZggWxzfKyIdJqXU3KM6RNd4kUjmatEXog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd99b8a0b.mp4?token=ZvrzH0vF7jzkQgKMNGDpQCZBctzkZUucYNsikcTrjZ01w9vJ4YVtf0YVVllmPEtnx0AEVxOg85eh9saK0kDb7GlK76PNlHeyna7iYxGqkmHbFppBKX5PoZz9ivbkw7XCMFBN9kyDdT_Ig6ZV_WIz_VrFYpV32tpIgjH5fU6qfk1h-DdJdVyF0c7brNr62LZVu4dT0dyp6XYg53kVMnePaUZo41lK9xqTvPBaBPqE9Qg0GFMlr5NDDjwHd_M0WAnmumlWwg8y2M5lQR5EU-nbUYLlT590wjcAUsxe5jiWtSdKV2UaNseQ0ZggWxzfKyIdJqXU3KM6RNd4kUjmatEXog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ریدمان عجیب میثاقی هنگام شروع برنامش
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93227" target="_blank">📅 17:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93226">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZxTyfdcekpJcU36Q9ibsJVcTrkSO_OotUhLYjV5ivpAwg68S30Wco2hA_IOdyUBt7inSlu1_Ixdkw_fHsuW2rnbvikRj6HCEDpDZPxOTKb1wPCjpiyNxhmghhlAxWXd1Z4u7s4UeD_lHiDBijeqyYbbPS_I4a_XQgg2eJWakb7nCVWQmTkMYxZ-3YldINVdQ-aFM0Xr26UVozuz6P0vQQO6dLmJ3q2CVuxdgzVwPeKToUACqjQhr15K33EcYqqiZ7jlvF4JaoRisLnKrZ7CNCa4vYYRMQ-_3r0o4YzCjDoaKeHbpT5orsILGwylL7OdJepQeAWts6NUOkk5tWLNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
۵ بازیکن با بالاترین نمره در جام جهانی ۲۰۲۶ تا اینجای کار:
🇸🇪
• الکساندر ایساک — 8.61
🇩🇪
• فلیکس انمچا — 8.51
🇩🇪
• جمال موسیالا — 8.46
🇨🇮
• آماد دیالو — 8.45
🇦🇺
• پاتریک بیچ — 8.45
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/93226" target="_blank">📅 17:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93225">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nTRrwnrInOc05cYJATBUg-RrFBSqAWZbmmac630s_U-u9OpFt8azTPtH0lwWzmyqa_jl8ElcTyOPZg8yhM7B2n-iwFehg-nBw5cZ-UNcJa8idpv7hoy8ekNvVvD59Nbp61-R3tiwa7fMFboJuvgsIB05XeTA7NdFUoSBMxslabj_x6kbUi96oth-fpcDBtOpqVxdaeVfJg3g61d4MnULmO6MevWBhfATJDLoUMuhmhkjd22KeSS8nKEteYhc7-KtUsbv19gEjp8Qp8YhltUX7gAs9tXXD-1oD4KbSO-_AeAuQhItdhHanCBsGLf65AA_-qH-IhXs_DGf3EbNar6wXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
مورینیو به نیکوپاز ستاره جوان و آرژانتینی رئال‌مادرید اعلام کرده که در ترکیب اصلی ممکنه قرار نگیره و به همین خاطر این بازیکن میخواد به حضورش در تیم فوتبال کومو ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93225" target="_blank">📅 17:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93224">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9xzggaoONJJ722UTA7hnhYnxUAxKdCqqzj5YogJU3Ou35Q6mMe3EpiAjBSbNeBGE8CTvI-RiUOtDx7EcHeE_xZEEdclEIyiAFVDAhFz44ybZSBoTUyIFckx9PcP3l5kPjF3pcx9vikljqmT42rLu1WCzrBXQ7QD-RcyldUFMAfMaqQE-_eMpQQOodjRRcU-xa6UWN8lm3TePV085MKLDsfFIYOx3W2CqZyLo_yHQTrfaOw2N4d2fEIDTK-H1DtntmiIlNPooR0YtGQWCDTd2Fl_HmOiHbTvAAz-0RSAFb9Jv1T6HA3y4QxzMGgRRMpZStg7ylH34FmV8gEejXeq2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل کیپ‌ورد؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/93224" target="_blank">📅 17:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93223">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQ3h2T27b2zdDQhkE68Cg2CdiHqAzBChvtRT_MtHj-VEjblbD95S20eruEjkPmtjted9h8w_fx2PtlTaAtO_HHKztc4PfUYvOXOeX4L7nEp1-glnnq1o1LiSxtMO0Z7o0mSs_9eM2PQw1fvr7dcQGnAVFCih7NunL38wNo1kj5N127-Lp82VTQoX3uWHCZm1AZCEEUN0k3u1Ou-Plsc_Jk9g9mbSzeTldVpkyNF04PE03_Q-G6dN5WZAadrNa594-KwUbjQw8t1od5gmXaOIqt6SKeWLdus7aOksjkcLwy9d_ZSIF5pO_DwdZ_Mx9amFBoEukwd6aoLIp9N5Z9QRUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
آرزوی موفقیت سردار آزمون برای تیم قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/93223" target="_blank">📅 17:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93222">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🏅
🏅
کسری طاهری رفته دو باشگاه استقلال و پرسپولیس ببینه کی بیشتر پول میده بره همون باشگاه
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/93222" target="_blank">📅 17:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93221">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cae9858e70.mp4?token=kPxrPrioPva2xOyaDNgrlFcmWLj12LiSxb8Mf4GcriqgajebyooZxN8-S7KxSajQvEokFvMBJItP6m-LiNtHQUCYbQyIAOtT1n9tRk8Sp4aB3I2bKS9zo0hksB2Le_4BbeRH6HfzEpFScenlaO5YBaPofVDHAAAdCQWJ7ZzRogn4sQ4woVmzxE0Re6-O-HSK4DTSk0OOd1XwD811OO9cYoA8PC9Keee9i3SZndnaEAwqpnSpXZ-7e4sJxkf0kp-hAIli9vAFXOzUPMX1eESLQDgBu-IqAS7oqxLxc_ne5Oa2SrMhG8PG1iJYHm8NRcJIUiy4xe0OkTN1fs7fUH1beA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cae9858e70.mp4?token=kPxrPrioPva2xOyaDNgrlFcmWLj12LiSxb8Mf4GcriqgajebyooZxN8-S7KxSajQvEokFvMBJItP6m-LiNtHQUCYbQyIAOtT1n9tRk8Sp4aB3I2bKS9zo0hksB2Le_4BbeRH6HfzEpFScenlaO5YBaPofVDHAAAdCQWJ7ZzRogn4sQ4woVmzxE0Re6-O-HSK4DTSk0OOd1XwD811OO9cYoA8PC9Keee9i3SZndnaEAwqpnSpXZ-7e4sJxkf0kp-hAIli9vAFXOzUPMX1eESLQDgBu-IqAS7oqxLxc_ne5Oa2SrMhG8PG1iJYHm8NRcJIUiy4xe0OkTN1fs7fUH1beA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
اتحاد و همدلی در فوتبال و جام‌جهانی؛ بعد بازی و شکست دیشب، درحالی که بازیکنان کوراسائو درحال عبادت بودن، دوتا از بازیکنان آلمان هم در کنارشون اومدن و با تشکیل حلقه به انجام اینکار پرداختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/93221" target="_blank">📅 17:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93220">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trY9_tWbZaARdKvrP0DIwZi4n8dkBnI_pFwZ3ptRJHl-WgzDZ5FN1-ozMMK_le9BUsFZY9nTOxuEQ7pF0kqEv9Mn7qMfGn9RjlgRi45XpAhvKtsEsyuSP-Pyi1TKKeJ__zbDg32k3QImaDXApa6cszn3vtW7uJjX-tXabPzcQ_IVtojH5DQ6wUkBUeSLHbMAlEE0VQcujhat309XOG3yzqma3K_5wTCiD8wDWvycuWnQmbmCUxZXISVi83yKVFt8mDkHh-Ekq-wdjPQr4n8rph8DooLBse2TMjptYQR9g57E8T3tkPoFKlpYexf7ZQGJ0F49qyb79ng3Kmuu6805ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فووووووری
؛ مائوریتسیو ساری سرمربی تیم فوتبال آتلانتا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/93220" target="_blank">📅 17:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93219">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikCmLa7V6RGGJGq6mUBu_jeKdhJQDImUKr3z4cRg0cWqi_Iix7x68B8gSOM-qRhGONBfiah2H2YN3KnY0uNstrKDJPeouUHyocg95EcSA9R2Fe3EeRyM6dyUWZyGS34bbFeTGdb7Y0HapaO3ZtlmOKnZ0sOqRHrkGXqB32dcQLqmTX6JxZQziOE7o5e_Dqurflc6oDbbonMNwtDCikBdluMifI7oUJQGl78Us4WIJyRuJfkiZw5ptkmwg3p8dhS2w1UGddbG_JKRIPcT-OjB-uE4H_vOTwqGrRUBAFuG2PtBpzIuDWtkIYylM0Edt0ucKBZLp-4ljPYyY9xz-oJ_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه هفته نیست جام جهانی شروع شده ۱۹ هزار زن حامله شدن تو کشورای میزبان
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/93219" target="_blank">📅 17:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93218">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e61bc4f6.mp4?token=NFp9xku6ZZdCQA7kadHvWDEsOzbt6QQ-Dq5kNaOgi7t5gBlnxq9W27NA9ArS4usFYeRXzGJcYNqAAdUJQj-hMVO1RBXrEYggHS98BuH3EDe_uH-brWhAjLSisFvGGNo7nHlsQrxWMYpCaEtGhl00uarvmDQY8v4RR0s0JnGNbVKewEfasC41BlMvXgnnFWUYnyUMF7IwvWE4CA1WX4lQxK7q4C4Gk96_Ka7EeZCumdI59n8YcWKELGgMtB935XLoXZIUCST6zjnX0JDwfv9FWybT6cd3DzmJo1dLTX5IflsaXNrKKqb6n9JtLwU2TL_8KGAhuLvTwRxBxKstGuvW0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e61bc4f6.mp4?token=NFp9xku6ZZdCQA7kadHvWDEsOzbt6QQ-Dq5kNaOgi7t5gBlnxq9W27NA9ArS4usFYeRXzGJcYNqAAdUJQj-hMVO1RBXrEYggHS98BuH3EDe_uH-brWhAjLSisFvGGNo7nHlsQrxWMYpCaEtGhl00uarvmDQY8v4RR0s0JnGNbVKewEfasC41BlMvXgnnFWUYnyUMF7IwvWE4CA1WX4lQxK7q4C4Gk96_Ka7EeZCumdI59n8YcWKELGgMtB935XLoXZIUCST6zjnX0JDwfv9FWybT6cd3DzmJo1dLTX5IflsaXNrKKqb6n9JtLwU2TL_8KGAhuLvTwRxBxKstGuvW0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
🇨🇭
تحلیل بازی سوئیس و قطر با هادی‌عقیلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/93218" target="_blank">📅 17:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93214">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_dxXNiGvjW03V18Xk_EhN2uJdWMQx8QXkOJWgKi3dLYsZbL5QMaImG6ZPDaIw9q7_mbK3z0KR6BJVGTwLNyaBGU6uBfWxOd5bpqvay6bCO3TasPLI85od4fnE0TGQPQKpJNqi2X9F5BjGOnh6Zex1DLiNChTjrPXBceVeHSp770Vy1jQyUO5qRxv2kAe2FXjb-JZdT7jD8oT4YtAYuJAGhCbK55sSQQJvlKFS9dVGTxgNANbMOkatMJewh9w0l4JAPLj5zrYaHKFGfKzAIvi1iKWau_RBG2GYhN5LFFy76q82r3IFEe7R_HpmmvqT-KbdCuRJbeULnUrp-DqohT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XKNvOB_xM_TPhVW7Is4Uam6XxAJA2gt8-K0_VjmxCPuqY_S8Jho5X_nrLVZBH-J_P-Axn079xtTay-t75Q0ObG1QLNx11VaPkHmY7bAiRLNY6W9m2HXsJb0-5hNSI48FUJ40ebMQdAG_kKgxIVxTVSF-3NOvI3VQyalyewFuuRWGTaUF3Aah9UmQfWZCJAFGeUJvZp3PCB2csEeYBDJZ2AsPc2BCvKH6iOxde574qZuoyzM9-Xiu9jdRSO8K8wEeXPgK9gyKNnAS1Z-W8A8tcWUHvDyHcjaha0GwJSb1gAUj2LPtVLRfVJYjqa8hP3tCUBU5JKTjLvS7EhrSCTMpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdgaIkuCFzneY_6fE9RaR2Xn53wCp7VlxUfNlOCSLjodDtPV35Dts4f4T5ezUJcCF8YhFtkhElvKQdrKQ4kd1M9RX94cYePYZ9mXYLj4sSTlLe_eJlSYszW_m4PktovqNdPO9JuVk4IvWPzbXzG2idQN1JC8KFgF2bPiWwY6Ln5j5u9-jh-9YsuK5s5zi0HccxeEA_O0n_-HcQ816Mtj5gTbaz1qd2jLJbGpR0RLCk5jQqCOt-Cd1Dsid1eUcimYHxh2VlIoL-_9j4-o1B6cljWPAIy4XmbyqXLfkaaQhyh-t8cmAsf6gLaWhjY-8O97l9U73l4-XFIMbN0GDz2HxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLk5EznPz674zzIJgm3sIZtwyG6t3bVZQNlDnYpE6tgx6BXMJGWc5mpFqC4KlVF-sBcA5aadwQCtKk9z2xpcXj-j4SQh8PiTt3dqrQpkkjFxLOG-sZXSQJQVBd5OjxfLcxvHNR_MAUylBHUq5HHJQuxHp3tu2DcDVR7WgE3uN0D4qgcrc47cXYvlLv-35W48LlRS0TeZjmUgJbpMx0dQgIUQqRTvM0RYM3ppVPXLSb0E9iz9Tu2UdPOYRfJ3LnYvgUuin5oohDnNh98VE34s8lstFI1MG_Hy1hRve4QUPFjqmHAGLk0g7fXSkiZcnI9M21DVrCAESOqi_ScPnxecvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
🏆
۲۰ سال حضور کریستیانو رونالدو در جام جهانی
۲۰۰۶
➡️
۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/93214" target="_blank">📅 16:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93213">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ماسیس
❌
قرومساق
✅
@sammfoott</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/93213" target="_blank">📅 16:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93212">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOGXCJ6sfgd75cxr5AE-4cTaVvf0d39-VEubxF7bj16C43ECOzYLoa9DlrzS7uFVfdw8DYp-ph8icvKXvGNnEBO9Nki2kjiAo-SM13f2bRYNJ8KU357iOoI1QO6rOklJ1ipYTTvEGQNkaWBH8DQt2EKHrPSreUHZ5zDrwOMG0pS5LRz9U25U1sO_FQfmHig0SbTFuaKZLJd1-LK3XxMZRkXUGSy7HQwOABYDSJIqjpdQq5pN4jeHhz7mAH8M2XGZobp1pOVjgncKEWe7ZlUDk_HVVZSRznwYk_coN4p2d-yR0Sn2iXeT4ttyvSHN384Qc5VSVrQDedZChOTYp88YxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
زیون سوزوکی گلر ژاپن؛
🇺🇸
در آمریکا به دنیا اومده
🇯🇵
مادرش ژاپنی است
🇬🇭
پدرش غنایی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/93212" target="_blank">📅 16:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93211">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Io7NGRE-r9pKjCGrb6KDw17sbV7Vgr0EdYKY3dTB9a69I1MdtxENZ5pmoZ7H6LAIZ83WRdRpl5rnv1sGie1p4LiXcehm9BoVG8uaB5weNxZ_Nj79rDghCucgj-6TLElHTEYYe5juGN7kznUJQ8Ny35PQiQ2d3i_dY3Wq1axACCaCEABndWS7mBoRJQDOGEjoRyBdJ4Mg9a_IPd_r6lqUdA2UbNzU275Y8osSGZ4r1T0jA7i-_4E1XluDVgZZpkK7AbhSuDbl7iWg5YpvQjMl4uclJRnzjhiXZoEeUTajIJtPP-Wl3FCZiy1LgEY0QVJi157HXvxLkODREj8kRDmjUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شزنی : رختکن بارسا پر از جوونه، وقتی وارد رختکن میشم حس میکنم عموی اونا هستم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/93211" target="_blank">📅 16:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93210">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn_pzP_di1Cr0MQ_dd-o5rShmgjtfeHpoZUWl77BRVt9sameJ2Cy6Bn3Sv8plVF4FaA7CniVTjzNBESn4rTU_T0HNfSEjj9G8KxYIgMuCq4KSvhl1XIAV0ryp28-Kv5yhcnWxd8JTHjw2XjYiBSgoHo8Wme0A-Myy5goutxobTILCU_ratOOb5tdThOAN-Nx-TTlefvD58HbI_dFfQRizaIRPr72lYD4CXKayF70HKYVw0KWoyWfZrIth3zvy-a_MRaz4ISkWkKU0sTqmOdSTc1F4tV7sca0MCOPC1WhPZlnyAD7UIKd39mLMrnyFmdOM8tKDIaKC3KY3hCW6ry43w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رافا میر بازیکن والنسیا، بدلیل تجاوز دستگیر و به 9 سال حبس محکوم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/93210" target="_blank">📅 16:26 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
