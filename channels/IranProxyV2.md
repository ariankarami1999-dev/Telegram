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
<img src="https://cdn4.telesco.pe/file/bIxvR_Ldr-GnFhlKeRWWWbhtUoHLAHylvHpDJONiCn2uXm6lHfUzY3RhHIzazWUy3rbpDj9f6xhEYVbYotBULEhOqASMc1gbTnOdfvzTrgOXEhYBmalfagDvySPORsu42ZyAvwuQrj2dS0x_uVv3V-vujp5CTlQwZclo1lGnvn8IbmcI991N0gG0GGzjkPE9FtkYS98Le6fkw0MUpZ2nX5wUvkXIZR1M8ikJuRBvhUdZGpXNeSB-Bv2-uGP-RA4787nkVHY7xbg1tH02AGX1Nye346tbeCm-88oHCJVJnzmo5SnaZil6n0d9eT0LR6DVuwGHw61jhKpqcFhzVb4ZDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 38.6K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 17:22:08</div>
<hr>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 595 · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMvCN4tYaF4tBkn6IqtM8V9K8yPwWPE9OhweWFHQvZuR6yOS7gUGU1LOZr9PbDYL_h3eSfFeCXcP6FaGv697LzX523KmuCNxDEZoEOiUNDziZ8xRoUyq-XDI9ML4_slVg36POruvVnDXVBF5-WA58NgADFe_yU7H_gbgA5r2eqikPdkWUapuMR-mhdpIV8VuDk8NzgcN7MoIdnyumQwa_1Lr29008-Kl_ZTFpFdYqHIIRcI_KH8WnN4PgVh4pcvaX5mB-e8jtn8qGrSposX3MBVkKAvqC9AH8KyXyGNTXpRSypf3Oi6DyIGR-HeBjrDkaNjZYhYZwzhkDXhETpMXvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 899 · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRuN34C1OAZXd4Grt49NvU6fdIfIwDLHkPbXHwKXcTZW3PXE7N775PI07dzL-YCZniT690mypVdTv6ppmGrbdyU3hAw-gCERkR4a7T2vE-p5yzG7ko9kzWSFvntmP8-tT8OKTQhx6Soh-Y3cG0K5TZ7b44_T2LMPOj5TRKASVuVF0Png7G-_j6IezVHbtZjvd9ZsPwFFGfs4Yx_lAPTYKdYJEP7puwxWytFikEqovyB5vqEMg7g4jTsuvWog5npFh3IjUm2fEC6b17SHzUb_ODDEoivNV6J4LXyQe0GUqFV-VpiYyguvD-Zk8D1dhukwOHv8UgQLIUM4BRPFk0jvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS9hCTIBfORE5lG0phRhdxxHgRO6QySbrgBfFz70qJaRtGnce1D2D-MaK-636C6MQKll_6uTb-ppTjMihl_iUhjZC64cxtIRwzdlpBrlEhNNL9T6-0UEBkt2qgrpdO5K9IGroWKefdRuqGoY6z38iNwZoKem_4bwwT602p9Zn4t60d37gtrkTL3h4Pb1qPWAGA2wc0OnFbmDA09ZI2zaYuSLzfTuoLI-S_fX1RZcS8-TnlQBvKoyvGdh73PQKpm_xqk9_01cXe86Qe0gR8kLq9zL-faKfq2-7Q_KB7aLPYSTwVc67w630fbXKGcrTuPR_Vk_QP29cgfrghvJWCM-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=p1K5_6D9_dZulsQIC1Pq8KdYqSA1h3qu1tz_zzAiLJA5Sfb-US62m8pgplssil61Ie08wFV559ON4hp7bbDW4ekdiZ_07_8AEnV_YX85zyxMPGu7AK4-S1T7UFFGheEo5DjIbWISYd2AtWeEtAFECxG-GslUc4LuuKeAkW7q5VgX47ZBylUayYj3GoReoeVb7hodPUJwLqSyAdEIEFz3Wl-v-CtiZAjNgSkKmC7oGytch-a9sEV5UmapqCP6mX5BKcG15UnVVbd7bqVDEUOP46EdXJT5QIBMOHWwsctyQkalz8ZOeaFgxexi77dOUBcbPLRP_BGUP4XJQJv2fjG-Y0YQzEVa0pJ79aoqaSwynCI569kDwv29HqvT2ftxBdd5fi_g95VDLcU0isu7vOrNjl_ePjNdZFkiJA9XmhkqnOFJpEXovSbbP36umk3tDu9QRw323R8JB-UNVEbOf519ecF7kaDPGmPYNT5-333_ARPwnFMHrXNWx02BOvOuKuUX1jNRLufX5ABhZrM9ZtCSPwN6uUoW6Gc8VtZjIcuG7zh0dpjOygFITbCseFhC5bnypkqCmskHS6zgXfiVOUT7fYnzPwsBLlJckNZ27XQ9h0Uu7pVQN0MOZWt8-9E77ruRwCnY7p5zVf7o0XO5iyPqESqYwsuIlXKqtq4-oKLD10I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=p1K5_6D9_dZulsQIC1Pq8KdYqSA1h3qu1tz_zzAiLJA5Sfb-US62m8pgplssil61Ie08wFV559ON4hp7bbDW4ekdiZ_07_8AEnV_YX85zyxMPGu7AK4-S1T7UFFGheEo5DjIbWISYd2AtWeEtAFECxG-GslUc4LuuKeAkW7q5VgX47ZBylUayYj3GoReoeVb7hodPUJwLqSyAdEIEFz3Wl-v-CtiZAjNgSkKmC7oGytch-a9sEV5UmapqCP6mX5BKcG15UnVVbd7bqVDEUOP46EdXJT5QIBMOHWwsctyQkalz8ZOeaFgxexi77dOUBcbPLRP_BGUP4XJQJv2fjG-Y0YQzEVa0pJ79aoqaSwynCI569kDwv29HqvT2ftxBdd5fi_g95VDLcU0isu7vOrNjl_ePjNdZFkiJA9XmhkqnOFJpEXovSbbP36umk3tDu9QRw323R8JB-UNVEbOf519ecF7kaDPGmPYNT5-333_ARPwnFMHrXNWx02BOvOuKuUX1jNRLufX5ABhZrM9ZtCSPwN6uUoW6Gc8VtZjIcuG7zh0dpjOygFITbCseFhC5bnypkqCmskHS6zgXfiVOUT7fYnzPwsBLlJckNZ27XQ9h0Uu7pVQN0MOZWt8-9E77ruRwCnY7p5zVf7o0XO5iyPqESqYwsuIlXKqtq4-oKLD10I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=HwVkJrMjs2qPV98jd_6fo4uebuQDFnrBQuTPFovEnkUVz2FQtrccQWahZwj-7eo0B-_dtKYLrSATK8ePIhbWEdMXBz6Qiv-z0wnACZ9HRljvLxmlpW5kQwzrFF97zEuTvgtjMie9bZVN-ANENbG4YnRRpqpffSPVShD-mCW6G44pyt5_LDeq6hbx5PO1M7IY7EgzwgIJ1eZb5vN82c2h9Gtl4Xzn4afd_3UaUa_Bwqf5yDMaFyvAc0utHJ77pxyFwHEB_Al7AMvILFn7V0PdErC0TAXd0y24o8FWsZimTY64ebTTa_kq5TldK-KqqG44bGuiorR68ar9JCyjy3aWzhxo6Q_vKRg5VfrgjCvy7L-37bc4B4MbNqI__MGVQto9vZN_qfX3j4WsnD1PjQ5HPWTcwM5i8TZbvY-A9H62-MHAEuCFdfvNIEfEtkjWsvdCLebKgIdEDb60wbKuIjsOjBdPxp9PrsLAdxzf1MHuFfnmc0GBpmjdFN5ByY6C3u5trsYx0LrN1oFR5JRge9RstwyGRTUGfaap4yneVw7e2f837t94Ov9kVw36d5SkEpse9R2IFnTds_l7uWPi0UZZA5wc_bxpeoKGIEgmRa_qykrkFE7ze_gBlWLpSCe-yLqe2T9QUnhkYQSz96ql7-4dhnh8dM19LkLeiZ5Oq_2eg6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=HwVkJrMjs2qPV98jd_6fo4uebuQDFnrBQuTPFovEnkUVz2FQtrccQWahZwj-7eo0B-_dtKYLrSATK8ePIhbWEdMXBz6Qiv-z0wnACZ9HRljvLxmlpW5kQwzrFF97zEuTvgtjMie9bZVN-ANENbG4YnRRpqpffSPVShD-mCW6G44pyt5_LDeq6hbx5PO1M7IY7EgzwgIJ1eZb5vN82c2h9Gtl4Xzn4afd_3UaUa_Bwqf5yDMaFyvAc0utHJ77pxyFwHEB_Al7AMvILFn7V0PdErC0TAXd0y24o8FWsZimTY64ebTTa_kq5TldK-KqqG44bGuiorR68ar9JCyjy3aWzhxo6Q_vKRg5VfrgjCvy7L-37bc4B4MbNqI__MGVQto9vZN_qfX3j4WsnD1PjQ5HPWTcwM5i8TZbvY-A9H62-MHAEuCFdfvNIEfEtkjWsvdCLebKgIdEDb60wbKuIjsOjBdPxp9PrsLAdxzf1MHuFfnmc0GBpmjdFN5ByY6C3u5trsYx0LrN1oFR5JRge9RstwyGRTUGfaap4yneVw7e2f837t94Ov9kVw36d5SkEpse9R2IFnTds_l7uWPi0UZZA5wc_bxpeoKGIEgmRa_qykrkFE7ze_gBlWLpSCe-yLqe2T9QUnhkYQSz96ql7-4dhnh8dM19LkLeiZ5Oq_2eg6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpSISVgveqRXYjiC0GuQVgjHVll8Vo9MnmgTDgTVY5erSc8lTJhUuSj_Gbv16BYIzz7bJHUVfzUVkqqC4omve_pM89_VnrNsCuTI1VBQP_4oJinwaB0U65gY60QeQ-MVwxwkDlwaT8F0AiFsW3UE720XKU2wU_9875jWkGsuZaP2TnbZyyAs6fmnarmW_gs4JFTysZyiv-ihIdWnVPfF0H3in3kBMd6lEvg1m1aMkb3qgN9BKzB-DzTFZKmAEx-BidUH9h-EPwscuZUJO3XVUzgudKdfp-3ZGUeUiHEqhuy3U-ecIf9ZU7lpGiUMq1bt--p3WRi9oBZTMTGp15qzLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=mcWvvn9JnfL7ZEnweFn3rpnPsQalPBgoR9_blpBk9rQWWdc4Cr5UL_x7ZxGrjVTCg_VcOXnfUz1UUi6OZTrgia7UYAxD_lvg0c52eoay4Hp9MS6WFsvZkdX5rDg78mkzD_8__-MNeE1x2uM2SYEydxo4NrxLOm0TS1LuUsMq8jC0dlEu8QeTQGdLHTKqTZoTyrnGvRQwzMXKxVXjJ68dnXtY4QxKVppF2QbTWwOVKD-3hAdff2BHyFGVKB0OrWfMwcLzYlgVGbfxJDOadD663G1CwOa0L_6Mwa55vC2D3KowLSpxronln7yUKcJLqP8tD3mbAUra--AYcyQ1Q2DWZh-rrLUJBC_Hc8Z4P4eY1RgrhDGFAEwPK_SoTOYetr_ZskdyETp762btSsYdMMxMvKPffL9tt2nWkd99z5uisjviTBpfVrTapEr2sVinWN8SN18aUBAw2ZiDpr0uyrmencFMF1N9IGX1w605zfHebsotJToS_BjY4PxPUEZr9ZQE1aCJtsgD5NpYin6q57bxa4x6wnWOXxfdywDsymzhJnv31VGJcfQzqGFvo6NWIw17PP8FQZPZ2JgCPQQiAXqfhXk6G2WsKFtLsq1HKnKJdlt3cWjWjBY82v3GkxtbxyHHWgOVj3_McjhIgpNeXyHLNUOyPTrCe0eVWBqjuRs6CTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=mcWvvn9JnfL7ZEnweFn3rpnPsQalPBgoR9_blpBk9rQWWdc4Cr5UL_x7ZxGrjVTCg_VcOXnfUz1UUi6OZTrgia7UYAxD_lvg0c52eoay4Hp9MS6WFsvZkdX5rDg78mkzD_8__-MNeE1x2uM2SYEydxo4NrxLOm0TS1LuUsMq8jC0dlEu8QeTQGdLHTKqTZoTyrnGvRQwzMXKxVXjJ68dnXtY4QxKVppF2QbTWwOVKD-3hAdff2BHyFGVKB0OrWfMwcLzYlgVGbfxJDOadD663G1CwOa0L_6Mwa55vC2D3KowLSpxronln7yUKcJLqP8tD3mbAUra--AYcyQ1Q2DWZh-rrLUJBC_Hc8Z4P4eY1RgrhDGFAEwPK_SoTOYetr_ZskdyETp762btSsYdMMxMvKPffL9tt2nWkd99z5uisjviTBpfVrTapEr2sVinWN8SN18aUBAw2ZiDpr0uyrmencFMF1N9IGX1w605zfHebsotJToS_BjY4PxPUEZr9ZQE1aCJtsgD5NpYin6q57bxa4x6wnWOXxfdywDsymzhJnv31VGJcfQzqGFvo6NWIw17PP8FQZPZ2JgCPQQiAXqfhXk6G2WsKFtLsq1HKnKJdlt3cWjWjBY82v3GkxtbxyHHWgOVj3_McjhIgpNeXyHLNUOyPTrCe0eVWBqjuRs6CTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEJqAkCGIQMuY92ZzpQYqxFa3zwe34lX1R7aqiYw2rOO9l_ypIICXPEQyo5A5aLyMEQQoyxbCLBAQJtz-7BTb7VV0K7rDliyByLuVVmKM9QUl0mlWBTjAKeMQ7Rdxi2d6a1qqIJWH35zMCVfy-hhTr3fc0Sici9PqgF4HGlSBzREIxy7dCdZmKNRDj08mfpAw3Mc-gs0aeU1oUBGJqSxdTy2R5kSd20LYWd_iFHOcJfk-gRaGzZNwaTFwu6IP0hTAzqfxvRa58zpwyFSsqtAFSwLc1ebyGhWdNAZ8a5il5UgcElHWnpXlQoIpiffyDvuub9867SS-jQq1sbY1ym77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ight9uZIq71NPwFP3kad8iq-mbOru8PQ3eOYx_ziQACN-5suZxWXJSs3HQbox6BstoqiER68yrIlFiO6Ysa9XLO4hr3Wn8SkX4L38Nsa4ohrzcNXx4F_VmmzAwVrMJbabCo1d-HsZQLCU1eS15nm1-JWiyIW2Ki7reWL0jSh-uZgSfbAodzzmPRdWvukyBTX3sWVKyCpDt4bgdzeJtFiXfLRVhrhOMV1qhZJNTRg9d5h-kLIdL3XMoqDg4eMKw3CpHZkcamayWsIVUN8c5NdgWLQ2tWuAUudo8S488PVSGO-psuW7J4zs1bwgWIlEjO7GO-BZ6X68aptk6iXEEr5oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=vI_PgpM3id_3aZrsquQAPNcS2yHUQiM6iKqgZqpbz24f20FwdmiyBVVCRjvsWvLUH3_E4TwYi96OKIZsPqegjaJDgdGyG6KyYn46f9MioyE6y3tRaeEGjIKuWaygoH4pDkiLdOU8Dz2hqvy5O6k4wyiOQM4JG2_9GG7UFGxr3P9jksTU5txYMrDm3PIANhWfoygNHCGoQ7bTM0OdW8YgwC0iKnte2V9LjyF4RDx_O9jyTS_Z_rU3C5bOpmhw7tr3g62exWK60_P43t2Py3NrcKmGFmstN1UPlyh8mIgyzWszBuZbAiP-01fa9gaesDlOl5AF-IPcArEY9G4-ilGZMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=vI_PgpM3id_3aZrsquQAPNcS2yHUQiM6iKqgZqpbz24f20FwdmiyBVVCRjvsWvLUH3_E4TwYi96OKIZsPqegjaJDgdGyG6KyYn46f9MioyE6y3tRaeEGjIKuWaygoH4pDkiLdOU8Dz2hqvy5O6k4wyiOQM4JG2_9GG7UFGxr3P9jksTU5txYMrDm3PIANhWfoygNHCGoQ7bTM0OdW8YgwC0iKnte2V9LjyF4RDx_O9jyTS_Z_rU3C5bOpmhw7tr3g62exWK60_P43t2Py3NrcKmGFmstN1UPlyh8mIgyzWszBuZbAiP-01fa9gaesDlOl5AF-IPcArEY9G4-ilGZMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqt8seoX-kv0UTwFFb5rfmp3pZFvYypBruIJ_HIGfkuq7KmMqhSDYsTX5iawzN-F4fSXrLqLGxBetgjKbyt8KOxtAK0bStg2lNFsDUM-7BQPDlW7JciyscTv1OdNIwehWRqSl8RhJvTBQoqGgzW-lNLxDisUa_4cM0IapCjI-joe24iuXc_ljnzjkAwE8QPrXbB8iOiQHmZEKg3bwJo8q4onyXTj3f2tiQSx8I8vhntduZHRxw5F3jvEjTS6L6ixWSEE11r8IHjAxBPYRU486sBpj9DJxR9w1YkdEcIHeh_O4eTfW7qww821hXQcEPGfvb0vxBjBdvro_NxgpICNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQbXCaYaDuuV_E8P7_wgR_xgyUt1khBjOvJH80c1ie9ddBSsg6X9X1Dt85l3LA53piiqMQvIAFpclg7MzSZN5lo6UDZk1yFjB8RIlTbKv4TOpf6_TohGi6AP1z6HEfYucQ7DoGm9fNRWVUjyhPRE67HJhoVYC4sZVC9bMIVOFBsO-xyseng_LF70QRs8wLdReNVyjh0qo6p_xEThqK0Ys4pXsgihon6osxnf2urny1oM7o7GffIZQ8GI2wuoPf--IH0POFHGaTFavNpUr3OV3Atz2BaiSG7YtHMBlbUmzkmEqkB5Y5yPQ3SN14wv1Nq-cLriczsctCdwzA5xcBaDQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)  ‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)  ‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)  ‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)  ‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)  ‏
✅
…</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)
‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)
‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)
‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)
‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)
‏
✅
✅
❌
❌
✅
✅
❌
❌
❌
✅
❌
✅
❌
✅
❌
❌
❌
✅
✅
✅
‏۶ )
🥷
𝐑𝐚𝐝𝐢𝐧.𝐳𝟐𝟎𝟎𝟕: ‏(۱۲۳
❣
)
‏
✅
❌
✅
❌
❌
⚪
✅
✅
❌
❌
❌
✅
✅
✅
✅
✅
❌
⚪
✅
⚪
‏۷ )
🥷
Matin: ‏(۱۱۸
❣
)
‏
⚪
❌
⚪
✅
⚪
✅
⚪
✅
❌
✅
✅
✅
✅
✅
✅
❌
✅
❌
❌
❌
‏۸ )
🥷
𝘿 𝙀 𝙑 𝙄 𝙇: ‏(۱۱۵
❣
)
‏
⚪
❌
❌
❌
❌
❌
❌
✅
❌
✅
✅
✅
✅
❌
✅
✅
✅
⚪
✅
❌
‏۹ )
🥷
Paranoid: ‏(۱۰۸
❣
)
‏
✅
✅
✅
⚪
✅
⚪
❌
❌
❌
✅
❌
⚪
✅
❌
✅
✅
⚪
⚪
✅
⚪
‏۱۰ )
🥷
Robert: ‏(۱۰۲
❣
)
‏
⚪
⚪
✅
✅
⚪
✅
✅
⚪
❌
⚪
❌
❌
❌
❌
✅
✅
⚪
✅
❌
✅
‏۱۱ )
🥷
♧: ‏(۹۹
❣
)
‏
⚪
⚪
❌
✅
❌
⚪
❌
✅
✅
✅
❌
⚪
✅
✅
❌
❌
❌
❌
❌
✅
‏۱۲ )
🥷
Zaker: ‏(۹۷
❣
)
‏
✅
✅
✅
❌
⚪
✅
⚪
✅
⚪
✅
✅
❌
⚪
✅
⚪
❌
⚪
✅
⚪
❌
‏۱۳ )
🥷
✗ᏦℕiႺℍᎢ✗: ‏(۹۵
❣
)
‏
⚪
❌
✅
❌
⚪
✅
❌
❌
⚪
✅
❌
✅
✅
✅
✅
✅
❌
❌
❌
❌
‏۱۴ )
🥷
❥sheyda☙: ‏(۹۴
❣
)
‏
✅
⚪
❌
⚪
❌
⚪
❌
✅
⚪
⚪
✅
✅
⚪
✅
❌
✅
⚪
✅
⚪
✅
‏۱۵ )
🥷
Ахмед: ‏(۹۰
❣
)
‏
⚪
✅
❌
⚪
❌
✅
⚪
✅
❌
⚪
⚪
⚪
❌
✅
✅
✅
⚪
✅
✅
⚪
‏۱۶ )
🥷
Ali Moheb: ‏(۸۹
❣
)
‏
⚪
⚪
❌
✅
✅
❌
⚪
❌
❌
✅
✅
❌
❌
❌
❌
✅
✅
✅
⚪
❌
‏۱۷ )
🥷
Vista: ‏(۸۴
❣
)
‏
⚪
⚪
⚪
✅
⚪
⚪
✅
❌
⚪
❌
❌
✅
✅
❌
⚪
✅
⚪
✅
⚪
⚪
‏۱۸ )
🥷
ㅤ: ‏(۷۵
❣
)
‏
✅
⚪
✅
❌
❌
✅
❌
⚪
❌
⚪
✅
❌
⚪
❌
❌
❌
✅
❌
✅
⚪
‏۱۹ )
🥷
Mohammad: ‏(۷۴
❣
)
‏
⚪
⚪
⚪
❌
✅
⚪
✅
✅
⚪
✅
⚪
✅
⚪
✅
⚪
⚪
❌
⚪
✅
⚪
‏۲۰ )
🥷
✨
𝒫𝒶𝓇𝓂𝒾𝓈
✨
: ‏(۷۲
❣
)
‏
⚪
⚪
⚪
❌
⚪
✅
⚪
❌
❌
❌
⚪
❌
✅
⚪
✅
✅
⚪
✅
❌
⚪
‏
👥
و ۶۳ بازیکن دیگر با امتیاز (
❣
) کمتر از ۷۲
❤
خسته نباشید
❤
‏</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvAXUleiaaE9uV4-NI42Cu6jTvW0r-u40lOC7QwHoFnSrgBv6A_efqpk9PJz0OfY6HFHtQLp_vMvaIzm7GpGJ_ef87g202pogp4pKLvSlWZDoI-ORSbyw12xcNr0zdJP9YgJWzjsHnU2ztnkpEDqHQlQXhYoGS9Dft63W44D5a78JBQpL5rKSbR-7X_Xao_GZtXIZ6TtV9YfiY2r8-8cup-o-k7WOkdF5a7UIsVHS_5ed9P_P9wkaGA4Ak9G6oMG-LlBoXu7pehjAi05RV64hqbxEvirerZ2u0pkB2zMg14Dv2vrhGJ3_Pews3nxlED0aGNgiGwGeZKf-oMyUpxdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=KaJfYn1oWpbx_NjrajDGQ76MdYchVX3in43lOyoKvYu8co0xeGLWsEZinbqM0_ZaTAXAnk6YDFJRcVQ3-_V1nidaw40ShCy2_6gSQTFeD1zxfoArXJ-nsD0rhOiIv9Oy3R7oKmmNbwJPSEZhQ5MT3YSBM8BcVu8oQSHONCBTqxTdw4U3FNCWgvfizsVuxyNlkb1AUaRyt7gvVk5bbfTmc02rSmq4P7c0xk23nWFHPadAjCh2ed0Xaa1u0SRGZgMfnvzmVF0V_04mnS0Iz09k9XjxC_8sLT55AdjBUYHP5BqV2Js83Zwv4slvmxm5uQOr0208KRW4kVfxevPxos9S7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=KaJfYn1oWpbx_NjrajDGQ76MdYchVX3in43lOyoKvYu8co0xeGLWsEZinbqM0_ZaTAXAnk6YDFJRcVQ3-_V1nidaw40ShCy2_6gSQTFeD1zxfoArXJ-nsD0rhOiIv9Oy3R7oKmmNbwJPSEZhQ5MT3YSBM8BcVu8oQSHONCBTqxTdw4U3FNCWgvfizsVuxyNlkb1AUaRyt7gvVk5bbfTmc02rSmq4P7c0xk23nWFHPadAjCh2ed0Xaa1u0SRGZgMfnvzmVF0V_04mnS0Iz09k9XjxC_8sLT55AdjBUYHP5BqV2Js83Zwv4slvmxm5uQOr0208KRW4kVfxevPxos9S7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=N9RQftCeIE3Blce4bkUgt3Phi1r-092M-xQxEMskaPg58sUSrH95xqpNpQ4FcVuIUZHK75MWH6lpbBG0LAYs-9us0sFZ3yE2sSEuKe5LepvqQHQFXzPW45rztrLCplKRNY_ncnMpHyWSMtuVQfeVfCDfb8pYhq-gRZDzg78W9nlJkkVLIoNlYie8mVs1L74OIXKFbyJWLmKo0obHIwck6dA33egVeHKc0_LjBcLlVVEryTwj6eMCs-lyJbxYTUWhTeNQY5eLwrbe_Eui5WZdYYrb_so471ZtXLaQyDSNQ7h-oByQMJLwVurGLIR_pXC81GZ9F-PRYRVHb_JHpCGRHaO5GnSTKHc887VYPzeZeSbgVD2c0OfIdw5z_ZvGr91y4NEfGfxyFsjI6d_07017A-esQotBbhB3rG5hvLv4jjatynf46TXXdh1NFBxiiv3GnCeqjaAPwzfbhnT9-5xobjafoOXNPHY1rWnoxGzMbRlma_CkzbSE8b2c9jDHYBRP317priFzYv1sJmMZ0brL0NrvzGbzdO3SyvFXSPwPX2CBMgFs-x-X5wEwX5WVGg85z_iWJR487se43huhAqA-T8R379RssF9go2WxRNMpIKh-WDj9rkobV8xs5UuivbOWcce7Q8MBxqn37Ag_3LM0xPn6xNOs5KcP4j8BgHoyXSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=N9RQftCeIE3Blce4bkUgt3Phi1r-092M-xQxEMskaPg58sUSrH95xqpNpQ4FcVuIUZHK75MWH6lpbBG0LAYs-9us0sFZ3yE2sSEuKe5LepvqQHQFXzPW45rztrLCplKRNY_ncnMpHyWSMtuVQfeVfCDfb8pYhq-gRZDzg78W9nlJkkVLIoNlYie8mVs1L74OIXKFbyJWLmKo0obHIwck6dA33egVeHKc0_LjBcLlVVEryTwj6eMCs-lyJbxYTUWhTeNQY5eLwrbe_Eui5WZdYYrb_so471ZtXLaQyDSNQ7h-oByQMJLwVurGLIR_pXC81GZ9F-PRYRVHb_JHpCGRHaO5GnSTKHc887VYPzeZeSbgVD2c0OfIdw5z_ZvGr91y4NEfGfxyFsjI6d_07017A-esQotBbhB3rG5hvLv4jjatynf46TXXdh1NFBxiiv3GnCeqjaAPwzfbhnT9-5xobjafoOXNPHY1rWnoxGzMbRlma_CkzbSE8b2c9jDHYBRP317priFzYv1sJmMZ0brL0NrvzGbzdO3SyvFXSPwPX2CBMgFs-x-X5wEwX5WVGg85z_iWJR487se43huhAqA-T8R379RssF9go2WxRNMpIKh-WDj9rkobV8xs5UuivbOWcce7Q8MBxqn37Ag_3LM0xPn6xNOs5KcP4j8BgHoyXSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otuDwwvlxJ-pKJEVT3JueJ-kO5hhJaY0ZK5BMUTQkh6AD_8CBoeRjKXQ1lTEJyGeokyTOPA1AZCkrrrBw997miRGNr6vo1U1yTjXMLi8M4mMJS1tpdoxy01vv896sRheLUG9T8ltqdZZEiApBgj89OJ9CH0YcjqitoRj6VPT6HdzqE9e46Rg0wQNTarzFdfnRWFQ932I0vI8opsvX2e5sIy9eFOpy3uOq82q_eIn7372DRTIWWC9_CILy0Bo6RXeUFynJorBxJRZBEx6C9nL-Umr-xKETnx1W3WTfgxM9ICtZFG0b0f7nZQ9CCRYlx_0RjJsUY2MeIXNse8iFek9ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LorY7nT_m91HrDH1tjr2U36PczSgs0wUpMAkagGykX9UmXCzf5QU7kZqsJAGFoElg06LwbWqARDsLQW5E5Yl0yR3vcaffw-fHH5cJ2CxbpWEnmy-Yuj6LWicxZPAARFPag0A_1OHjP3DRS6E_pCLzguK7PWhltHIBJ5LLiwzxzezHn9c8HyvrV6fr5TtaiYfhAKXVHxedHfDCECkjIMP7xd9hpMPz3d7r4a6lLebK_RJDplnYYiucIBC2YNsWOFcUdIyLpfs9pSi0dErlgmmZHtAw9YnFl2-N6Tz9N3vxqJVUJpUKty_N9TpasrCQhtBQNDj_TLteqVEXkTDiMkCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
کد تخفیف حذف شد برای راحتی قیمت هارو آوردم پایین راحتر بتونید خرید بزنید
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e4IlP9ayMbYHA3-jDylqgUSWUfIn8ErFFp9auxN5X-lhAolAq4gXnPv8iUXpxQevefVtBCaopbwGL-xDpOgVYb2NTKyQOztj-AK5QWWTMCAAuzbVytY9yRLxTy53JutjY4oWe2tWXfDdL4cNIPrxXRI21Wt2deWGPcBd7ncTz3rjz3h-4x8uovVAqASDmvAp25I2Ty2Y3tj-vlBFROHpUH4HdQm6J0GJl4CgspjYhuD1vXlzjJOnU3siy1noG8iN25LAX6paSI0XTFqFi7q2n4D2tQ3FisslP5revI14QldR4LqFNy65zrVMN_if-tULd9XEFDYlvYjgjVYAIVNF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=L6o0xiX0XNi0w2tIYMTDJIbyDBUjvetoLzRWFKXVLEORFTcssdvm2uMMy_JHb19Vru709aZJ6EZWOcXQuamT_J7rfveRXGqgIawRCpeOAwWjB282yncqTOgpoCYgNIIiLZNTAOK8J1bnxq_fQneidCIfZCIwYqUpjbB3PcNg4M5ALkyCIAJptqsP-0pLdK1VcPaxbdmhhurUgjmnyXAaHBnbDIAgeQwClOl9wrdlKT6prRS9EWmWRF5Dr8DGAch2ErFUtHXmtYgIJqfjK8jE6N2skbLu02lJT3j6wDhiTgHQLftzXEeReHOFt13wnMm1SFQ9-Sz_ZpyPPgkMHQ97UnfjVNnVgRGPJGoZ0QWsa5GPlhvudNZ4kTo3b2v_UAn1wRZedCaHg9ZAMk9Gb6T3KYovGMK-WjFDQ8Pk70qDlTBOR3fgoDhHExVw4zGjGEATfnoVlVxPRWMoHKAxg9bYl41WEAygILylWjxb9JDMV731I0-Y9Z4PVRkt6uaEqwlCLmA5jN1C1VEMJODNnZst24ohHOI2UEI8OdzKGaF5w7nMBOr1NtbTwQouzsfgHklqxhcdU8H2opIBM_yFjgU9jpNXgfBy78oHlR4AqeRELt-5jia0i4HP3qJkc-UfFVsjXZqGlBFBHB7DCMFkb8x2lyt8MGYmbX0yDEgeyVKmSm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=L6o0xiX0XNi0w2tIYMTDJIbyDBUjvetoLzRWFKXVLEORFTcssdvm2uMMy_JHb19Vru709aZJ6EZWOcXQuamT_J7rfveRXGqgIawRCpeOAwWjB282yncqTOgpoCYgNIIiLZNTAOK8J1bnxq_fQneidCIfZCIwYqUpjbB3PcNg4M5ALkyCIAJptqsP-0pLdK1VcPaxbdmhhurUgjmnyXAaHBnbDIAgeQwClOl9wrdlKT6prRS9EWmWRF5Dr8DGAch2ErFUtHXmtYgIJqfjK8jE6N2skbLu02lJT3j6wDhiTgHQLftzXEeReHOFt13wnMm1SFQ9-Sz_ZpyPPgkMHQ97UnfjVNnVgRGPJGoZ0QWsa5GPlhvudNZ4kTo3b2v_UAn1wRZedCaHg9ZAMk9Gb6T3KYovGMK-WjFDQ8Pk70qDlTBOR3fgoDhHExVw4zGjGEATfnoVlVxPRWMoHKAxg9bYl41WEAygILylWjxb9JDMV731I0-Y9Z4PVRkt6uaEqwlCLmA5jN1C1VEMJODNnZst24ohHOI2UEI8OdzKGaF5w7nMBOr1NtbTwQouzsfgHklqxhcdU8H2opIBM_yFjgU9jpNXgfBy78oHlR4AqeRELt-5jia0i4HP3qJkc-UfFVsjXZqGlBFBHB7DCMFkb8x2lyt8MGYmbX0yDEgeyVKmSm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBlyuc58yfuR_dJmvy9dBBICJu5m9TeP8qgaFQF7PafY1y6dGCLUrc0KDY3bzsu62DFgElwuKYRtz8EBf71duLO4-HsglVP2dZUA-Qdjq0am3b8axhIxdjxIX4KKkT7C0_jordU8kTX7hGx4MGqqauTTP4gn9SdZLraoMwVfHmlIra3XKvVgqpzqlgbZ-_SA4v1Zw_Z5N9SyFxT54KRmevKk_Gk8eI_ZGnIgmle5dV9iMw6pWuNQghBarvTw-TCTFOzD-Agi4sErm2JB7FL125ndbuaE3zvTPePh8RMFgGfWxeuiJbri6dcir6cDuGle75e9VAFvOxxDH_spCrc6CUGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBlyuc58yfuR_dJmvy9dBBICJu5m9TeP8qgaFQF7PafY1y6dGCLUrc0KDY3bzsu62DFgElwuKYRtz8EBf71duLO4-HsglVP2dZUA-Qdjq0am3b8axhIxdjxIX4KKkT7C0_jordU8kTX7hGx4MGqqauTTP4gn9SdZLraoMwVfHmlIra3XKvVgqpzqlgbZ-_SA4v1Zw_Z5N9SyFxT54KRmevKk_Gk8eI_ZGnIgmle5dV9iMw6pWuNQghBarvTw-TCTFOzD-Agi4sErm2JB7FL125ndbuaE3zvTPePh8RMFgGfWxeuiJbri6dcir6cDuGle75e9VAFvOxxDH_spCrc6CUGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
وضعیت سرعت سرورها
@RUSSIAPROXYY
🇷🇺
📌
آیدی ربات جهت ثبت سفارش
👇🏻
✉
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J64qOLc7-JDZzshc06ZqVygjV0U17cQu461hrpmNzUA-4tB80fKnmjQOTtlIxyTfNyWO6m7YXvNMEpiVgWbzqYfYAVWTpNRVEYhP3BC3ayD3-ktyNPQe9i8-3NJxfH7bD5S8vBq30sSWnx5pPdpaUbtesamGouvFXbSz9UQvoPHf7bboV46a16bZ2_UeTXEW4QXic6zKKPYkrqsA-W2YAWI2iKpW14fTlb3Ga0qGwpON_QYci3xQYeCWerH3ACBEWB_QEkM-l3oZEWm7e4hAT0SQJM5eCT8gFvfC7YUqByQTBvcHWAGvTl30AMRl6K1PmHPmjdGHCWtWLSINc4SV6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsmgmMw1CjpgDHHbi7W5kIyOzpHTE93duU1unZCiMhXsD1elSUWZZiYOfysSQIuHqdumncnCz6Zc0W1l4oyUXB18Xf1brnY4vDS_WVt2gy5f6qrPzzixb3hZ_Cn90DItATFLmeM25CkB0QEKgVrTq7SMtfStHQ7dK9OeC3yW3qPTNgYFv_PNEyRZ7BRaJEJRjn4kWC4w7Y-Ul3OPYP_WpoW1pO3e4T5KoUGnDK6OCscrLBnI_rdMGqHiK1weJwmuLvwGSBFm49YQGUyAVIzlkmxcH3Kw731CScuoUxF_FdX61v_SHk25b4l251_Aotx7ArsT84Z8DeIrQZXN6EogFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=fj_OaNYCix3ZMw-9JpxEbtQAsnx2wbTfTgmzdoCbaR0_wlK1LGUXtfHF8h_M-Pn3H0rd5fXthxy5uzMQPX7FawbnrXxY0PFk5zIw7M-t7vubo-lhtY_FVJTIjbEGGnygtCMYxplR877MA-Ypdikhsg3frAO1V3792z2Xk0InAqgB7AUT6aNNJqe5E6TQdJqQ3Rj9MsMfs6pXAaoqj0XOzlGQPzDvxsuYCgQ-jtczt4AXTh24blbadRHD5vSGkufBsvOlJtXJkSynkj0wyiiJoqymXvNYHzUyCpKTNWf4GYUrzDiaaAtzygwEwsh0HQf0eb-8yySQ9yBabjKLsq1lOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=fj_OaNYCix3ZMw-9JpxEbtQAsnx2wbTfTgmzdoCbaR0_wlK1LGUXtfHF8h_M-Pn3H0rd5fXthxy5uzMQPX7FawbnrXxY0PFk5zIw7M-t7vubo-lhtY_FVJTIjbEGGnygtCMYxplR877MA-Ypdikhsg3frAO1V3792z2Xk0InAqgB7AUT6aNNJqe5E6TQdJqQ3Rj9MsMfs6pXAaoqj0XOzlGQPzDvxsuYCgQ-jtczt4AXTh24blbadRHD5vSGkufBsvOlJtXJkSynkj0wyiiJoqymXvNYHzUyCpKTNWf4GYUrzDiaaAtzygwEwsh0HQf0eb-8yySQ9yBabjKLsq1lOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DuocupEbYcBd9pk3wTPt59cha5aNU30gLkWaAXYgYNkVfVDj_mm5VJKToETS5HjVKLYLSGFGR2botQSHZpXht_aofoztRdr8lgGd2LTPnGF0Bu3hJgzeF8pU1hC8ZMmx-o3GGeZ3QuYyqGpl5accVpU4VWE5XAdJLHpS1Xr8JwgDwFsgXGqCl6uxhIJA2pIOdoFJczxpJ2L5VZmP1G6tKjgpEjXNRuO4KolskmjKS3p4-TMj2QBd3AqT_khhkcgqnT_ZTgc806pDs0foXJSFYA0pTghOrqY2hq94sgANqn0upyRSOd7vFN7DEYkemTujyA3wX3clwgpYKzEcNPHjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2EOPHE65A8lRJ--txxRtgWewKEttONVubQaQNhX5Ongw8iowqcZOEuxKp0QbJQUvigXlPLDnHDi1PE5sOtEGqy0dhd1Ki7wKn-sVNywRON1iE8cOz5b1eQWXHvvIPLDh0BtUjVV1lcJ_Y045Fte-CQlFP2L3v9ZvgnkOGU0SdGVOP0JrOTB709O1ljBCZ5UepKNRwJrMY3pWGUpaAvx72NZ_WE2eOlFyUv0f-mLLIW1rjuB1xnIJsRrkN-2HJfd625_CXZY9SdlC3XLPOuXxNrX1h69FjOJwqi23zS3GX45d7DxeUp9r4QflsLMM3nXZP6eeygaA2Rvh-5zCi2X0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bEHnxq9XDIBCdNB4iF8t_rAXzPPGP3tgEqrtJ9oTaQOye3OfT9tMW8Gwuv5dNrjZgqlKorqbJnU6jiYZ3nPpQCpxb6EFbOgpKJe5hAzJH-gKi0_qcH_CeDkU9jLujU212ax1tFOapOeIykuQ_uWGYwx0N_BxJ5bP4AjYfQhHl2hIIaXK6-rHWCjNoPASGLmfrLD4yr81twtPuYP-OyPtPOaT9bk-LFHLl87uuXU-Ti9qAWceFJr_Ucy8EyF9D-JSs-YdvJV1uGlpInJrQ2czSj1KbscFcel1aYdc6Gg07g4MrLTME0V3YV7IDXDJp9GKvu-ZOF_zGZb743K2aAe67g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قیمت‌ «سیمکارت سفید» و «اینترنت پرو» در بازار سیاه چقدر است؟
🔹
اینترنت پرو و دسترسی بدون فیلتر از طریق کانال‌های غیررسمی و بازار سیاه فروخته می‌شود.
🔹
قیمت ۵۰ گیگ اینترنت پرو در بازار سیاه تا حدود ۱۲ میلیون تومان اعلام شده است.
🔹
سیمکارت‌های سفید با وعده اینترنت بدون فیلتر با قیمت‌هایی بین ۴۴ تا ۱۲۰ میلیون تومان فروخته می‌شوند.
🔹
فقط اقشار مرفه توان دسترسی به اینترنت بدون محدودیت را دارند و این مسئله شکاف دیجیتالی را تشدید کرده است.
🔹
کسب‌و کارهای آنلاین و دیجیتال از محدودیت اینترنت و هزینه‌های دسترسی آسیب جدی دیده‌اند /اقتصادنیوز
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://45cd71df-7b23-4568-8677-fdc4a0daa76e@protectnet.cloudinohost.com:443?security=tls&sni=protectnet.cloudinohost.com&alpn=h2,http/1.1&fp=chrome&type=ws&path=/&host=protectnet.cloudinohost.com&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/IranProxyV2/8332" target="_blank">📅 03:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8331">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💎
𝗩𝟮𝗿𝗮𝘆𝗡𝗚 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻 or MahsaNG ( Psiphon)
vless://799f939b-964b-4416-84ac-18a6ace7fe70@camp.nahidapp.com:443?path=%2FIF_VPN_Bot&security=tls&encryption=none&insecure=0&host=camp.nahidapp.com&type=ws&allowInsecure=0&sni=camp.nahidapp.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8325" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8322">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvGonB6smB1lEhqQ4xVUqt7HbqJf8em8IHoSAosGN6vdvELKSdXF6x8DguOcjF9Evhe6ieo7ZOYtCWMz0W9HTtI1wNMIhQZzPDS-CjIgxw7MvwhxQvJRFWGUgpR1hpYL2kJcScclNjpNLmxpXnMWIfkLOHoVc43fnecLgouadQdBUrI8R_fvzlFrApxaBrlQclrNWUoSXM6tUePBeOCODPgD5g7rk14qGZwrhNyOxjjuVEZ_d1iCY2S036cpkA6YB_9skzwzOw54DMaEsg6a-6HMhMvp9CWfbyUKxstubn-zMfiteQME8rpw6z2nLXzknnTyqzWVHfFFaNbuyh7ETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وعده پزشکیان بالاخره درباره اینترنت :
◀️
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
‼️
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8322" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8321">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره،
دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول بدین صورته که شما کانفیگتون رو برای پشتیبانی ارسال میکنید و همون حجم باقی مانده براتون با ضریب دیگ چنج میشه به سرور ثابت البته با سرعت کمتری
2⃣
- روش دوم سرورتون تبدیل میشه به سرور تانل با سرعت بالا مث سرویس هایی که درحال حاضر در ربات هستند ولی، ما به تفاوتی باید پرداخت کنید بلا عوض
3⃣
- روش سومم اینه که کانفیگ هاتونو نگه دارین بعد از این شرایط نت از حالت ملی به حالت بین المللی تغییر کرد به ازای هرگیگ، ده برابر اضافه تر حجم دریافت خواهد کرد
🔻
@RUSSIAPROXYY_Admin
📌
به این آیدی جهت رفع مشکل پیام بدین
👆🏻</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/IranProxyV2/8321" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8320">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPidR83zV40t2_-h8YoOq7VfcdcEV88SesrZuV-RFD99mup5duWns7wwCYEGu90m0wg33xpLQ5n_hIKYE0P36MexuthQ75ErmeCwugVeE4k2DRkhekjuxLTpW-fOmUu9I5HZCIlYcDhQRGY9D6JcllK63c-t3L1IDIYY2tcrCS_CO5BjiB1RSlvq_csPm0IA4mZJJxiZIO1WS8Teu8Jw_0duoP9JbBALz66TtQyyFg4tO87WdKbdhRQZtBTClpO4cGkh3S2QO67vtQJpDVbnrXZCnt9TI5Sgvod-eCOl9dc-YAF6Ax-K7BmSJPkgtPwudi_lyrziM1EuysXZzmVrCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت اینترنت پرو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8320" target="_blank">📅 20:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8319">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✈️
دوستان نهایت تا امشب سعی میکنیم سرویس سرور تلگرامو اوکی کنیم، هواتونو داریم همونطور که وقتی هیچکس وصل نبود تو دوران جنگ با کمترین قیمت ممکن و کمترین سود ممکن بهتون بهترین سرویس ارائه میدادیم، سعی میکنم از جیب خودم هزینه کنم تا مشکلتونو برطرف کنم نگران نباشید
✈️
سرورای ثابت برای نت بین المللی و کلیه اپلیکیشن ها و سایت ها و... براتون تو ربات با کمترین قیمت ممکنه قرار دادم بازم امروز
قیمت هارو کاهش
دادم که دوستانی که شرایط مالی مناسبی ندارن هم بتونن کانفیگ تهیه کنند.
✈️
🎥
📸
💬
👾
📞
🤖
🔍
🕹
📱
⚡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8319" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8318">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de826422e1.mp4?token=Zao7JQR0x09Vhhf-M8RP-8d_RKAe6Q9jRaXwdfh0_DEPo9zcFMVmRe-neVkjOrL2p9JW00E9btHG7xnl4k4KesuRuzXDQazx8CWKoiWUt4eKP-oQ8jkMUSIM9ly3703NEs5nClIjxt_vhd0BrNKlTRd5jGdcGlHK5rWJ3s5Yo7lpU7gLBHVB2RuslBYFk7qRxRPwP5sUlPJ34QUCh0Wmw90XFFV4YSEWk4UBuFY6B8fTtD4hzrsbCS4atdH_66CyN4erTs4E7Nr5SzH4dD8B0NSYEQXilFoqr7n1IWq72h5_74uT7IgK217Dz2-OAocwT9WAlAhpFMTV3sz9eFnDDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de826422e1.mp4?token=Zao7JQR0x09Vhhf-M8RP-8d_RKAe6Q9jRaXwdfh0_DEPo9zcFMVmRe-neVkjOrL2p9JW00E9btHG7xnl4k4KesuRuzXDQazx8CWKoiWUt4eKP-oQ8jkMUSIM9ly3703NEs5nClIjxt_vhd0BrNKlTRd5jGdcGlHK5rWJ3s5Yo7lpU7gLBHVB2RuslBYFk7qRxRPwP5sUlPJ34QUCh0Wmw90XFFV4YSEWk4UBuFY6B8fTtD4hzrsbCS4atdH_66CyN4erTs4E7Nr5SzH4dD8B0NSYEQXilFoqr7n1IWq72h5_74uT7IgK217Dz2-OAocwT9WAlAhpFMTV3sz9eFnDDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شهبازی مجری صداوسیما خطاب به مردم ایران:
اگه اینترنت 5G که افغانستان داره و مسترکارت که سوریه داره اینقد براتون مهمه؛ خب برین همون افغانستان و سوریه زندگی کنین!
﻿
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/IranProxyV2/8318" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8317">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ایران اینترنت ندارد، روز هفتاد و چهارم …
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8317" target="_blank">📅 13:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8316">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⭕️
اطلاعیه:
وزیر ارتباطات گفت در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم.
همچنین طی پیگیری‌ از ISP اعلام کردند که اینترنت بین المللی شبکه خانگی متصل شده است اما هنوز زمان مشخصی در مورد اتصال دیتاسنترها به اینترنت بین المللی وجود ندارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8316" target="_blank">📅 12:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8315">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=R9GAQhkQt0D-drrwymlGCXtXFd1pmIxXeXNwjOf0s0rVyaKi846yuP3HqGvBcuzNsRgz01HjjWM9vpzx6VukhExTtgeHrSMaXu4i6vwZuPBVaNJvkxySi-rq42jmghBRJMRkNRDL_L2uaLLlbRg8WeJyhXvkWgBuveeuPJOCHw_emSd_XW2zmYE_J-5TuG7KM0E0GhGCetIYtJxBwGiLw7RAGDKh8DwlymPCCP_Z-iOrJyLXxPgSDIc6jCp_pfEbOJdoxOlJVecFmbpHUYVRJBdjbYW2ZP-hkR-fBV1ktwCOZpH9WET5XJxSgYRPpYdzqBA-ryJ3sjbSikirvGVTzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=R9GAQhkQt0D-drrwymlGCXtXFd1pmIxXeXNwjOf0s0rVyaKi846yuP3HqGvBcuzNsRgz01HjjWM9vpzx6VukhExTtgeHrSMaXu4i6vwZuPBVaNJvkxySi-rq42jmghBRJMRkNRDL_L2uaLLlbRg8WeJyhXvkWgBuveeuPJOCHw_emSd_XW2zmYE_J-5TuG7KM0E0GhGCetIYtJxBwGiLw7RAGDKh8DwlymPCCP_Z-iOrJyLXxPgSDIc6jCp_pfEbOJdoxOlJVecFmbpHUYVRJBdjbYW2ZP-hkR-fBV1ktwCOZpH9WET5XJxSgYRPpYdzqBA-ryJ3sjbSikirvGVTzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی:
اینترنت حق مردم است؛ عصبانیت مردم کاملا درست است/ عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8315" target="_blank">📅 11:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8314">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اژه‌ای: اینترنت پرو و سفید مثل پتک در ذهن مردم شده است
🔹
رئیس قوه قضاییه در جلسه با وزیر ارتباطات: مسئله‌ اینترنت پرو و سفید مثل پتک در ذهن مردم شده و باید با موارد خلاف قانون در این موضوع برخورد شود.
🔹
در این جلسه دادستان کل کشور و وزیر ارتباطات به رئیس قوه‌قضائیه گفتند با بررسی‌های صورت‌گرفته، احراز تخلف در قضیهٔ موسوم به «خط‌های سفید و اینترنت‌پرو»، قطعی و حتمی است./جماران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8314" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8313">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">vless://8b7dbddf-fe0a-4405-b8e9-bfac4d9439ef@185.143.233.235:8080?path=%2F&security=none&encryption=none&host=MHI.ARTARONA.IR&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8313" target="_blank">📅 11:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8312">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">V2ray + Psiphon:
vless://3728fc28-910c-4a9c-888c-c08c3e2f4a06@snapp.ir:2052?encryption=none&type=ws&path=%2Freq2&host=snapp1.gptpersian.ir#musiclovers85
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8312" target="_blank">📅 10:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8311">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">احتمالا اکه پروکسیا درست نشه با کانفیگ های ثابت جاشو براتون عوض کنیم اطلاع میدیم خدمتتون بابت صبوریتون متشکریم</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8311" target="_blank">📅 00:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8310">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حجم سفارشات ربات بسیار بالاست موجودیش تموم شده بود مجدد شارژ شد، صبور باشین، دارم یکی یکی رسیدارو صحت سنجی و تایید میکنم با تشکر
❤️
💲
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8310" target="_blank">📅 23:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8309">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4OHZvg4gkMgzisyRJfACVdWMoZyUspXI2vHXdV_FJ9oYN0mLeVINEuIxqt9pfCpYIb3vcr01BOLLu6VJWBA0cdElg1owXzsWBDa_ATemGOy_6LK7lt5D9s9kXj9CPW2NtpcCJc8zvSagzNBfSvOCoyHhfTonbWBxWykHGjaBuv_N1yBdu6t71_DhNNw3QEm2vWUMtNizAaV9V70eEj-hWBqnIHKjejib8pwRHrf2ToIUZRBbB-UZtpwLPZpHUlZo6RCyaSM7B6DnwI7uWMJh7Aie-1im1pjq3QaRA4ah0xBACB7-pdurCtLjoYgdUi4BEaDLCR7-8I7F3KpcYz-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزه چالش دیشب، برد 2-0 بارسا درست پیش بینی کرده بود
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8309" target="_blank">📅 23:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8308">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
معاون علمی پزشکیان:
حتی در شرایط جنگی هم بستن اینترنت راهکار نیست، زیرا وقتی کامل بسته بود هم ترورها ادامه داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8308" target="_blank">📅 21:00 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
