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
<img src="https://cdn4.telesco.pe/file/QaD8XCH7rpu4vnOa94wSLMWcZGQvoe_2txXQqSRTP1KMLalMuYX73ll74_JUEiY4R-NrgzPMKQgpR_fHMGvKdDsgvRI6QMeSYH_Sp0r0bxqGlsBlaadN6wHimC6p5_iy0g9tUjMU6B7Tl3QcJvjo88iOSgUpki7qGf0YVlseGJkN3zl7M0IbrjiIbkDdc0DhEolpgAfJjKaTnd4T-H4qMXR7cmL3rR_9BqXBBi1T8f0j-X7AuwKx5n-Nh76rHLRN_EqPdvs6jnheirgQxb_DC8Jt9yRSPDdEwdZ_D0QPnaHenj5xnErEEb_oPiGYxuNlsb70Tl0OSMbLtoK6bnTz1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 118K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 09:26:04</div>
<hr>

<div class="tg-post" id="msg-70442">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78b2128551.mp4?token=KOTXWOPMoJCwNBocAw7nb6CDtoq20SV8chod8AwkR-_m2603wHMDxXFrDA9LublXdZDlkjRxMUw8ZlgsSukTBZhxm164H4Q5PLF65-GoxlYX35_KT71a6fKmcwdUi4YXYyEfkamxjYGAXfu_Z9Na-j6nfg3A8EK9lOd40JibEL7Rin5iRZl-nLyh7sqvKKNwLR5enE21Pf_BIj8x3YwEVd14TllkPlx4VDmJ8iIEgb2eA7p4AuQKDlMwtOoB5ECzblk5W8brACUEfcVbSwiT9cjUG_A8lUVdwBOZt-DomAjqNO2IMU9-t6jPyhA7MlnUxnC90B-AgzvgEZqpYIqJ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78b2128551.mp4?token=KOTXWOPMoJCwNBocAw7nb6CDtoq20SV8chod8AwkR-_m2603wHMDxXFrDA9LublXdZDlkjRxMUw8ZlgsSukTBZhxm164H4Q5PLF65-GoxlYX35_KT71a6fKmcwdUi4YXYyEfkamxjYGAXfu_Z9Na-j6nfg3A8EK9lOd40JibEL7Rin5iRZl-nLyh7sqvKKNwLR5enE21Pf_BIj8x3YwEVd14TllkPlx4VDmJ8iIEgb2eA7p4AuQKDlMwtOoB5ECzblk5W8brACUEfcVbSwiT9cjUG_A8lUVdwBOZt-DomAjqNO2IMU9-t6jPyhA7MlnUxnC90B-AgzvgEZqpYIqJ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
مراد ویسی، تحلیل‌گر ارشد ایران‌اینترنشنال:
🔴
جمهوری اسلامی با سه‌راهی مرگباری روبه‌روست:
تسلیم شروط آمریکا شود
وارد جنگ شود
بدون توافق و جنگ، با فروپاشی شتابان اقتصادی مواجه شود.
🔴
این وضعیت اختلافات در راس نظام را تشدید کرده؛
احمد وحیدی، محسن رضایی و حسین طائب خواهان ادامه تقابل‌اند...
پزشکیان و قالیباف با اشاره به محاصره بنادر، قطع صادرات نفت و کمبود بنزین، توافق با آمریکا را ضروری می‌دانند.»
@News_Hut</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/news_hut/70442" target="_blank">📅 09:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70441">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">💎
میدونستین تو دربی بت
✅
با شارژ بالاتر از ۱۰۰ دلار ۱۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/news_hut/70441" target="_blank">📅 01:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70440">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70440" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر D
erby Bet
✅
✅
✅
✅
واریز و برداشت ارزی و ریالی
‼️
✅
بونوس 120% اولین واریز
‼️
✅
بونوس برای 4 واریز اول
‼️
🎁
بونوس ورزشی هر شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🎁
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a31
✔
@DerbyBetOfficial</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/news_hut/70440" target="_blank">📅 01:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70439">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8QyTbDVFlNc-uSpKJTdXz9kZeLacGOH0O9oXLNU9bReSGwvoJA1ZcwD_QXVKYN_qUe7yh68O8ut9cGbz8OPbXJmOmTBDL-jtmFQYfKwqlx490gPGzcT7wtCdyzj6s0nzDCR0w9Z282ecA7jyGDt58RhbssNw6OWxuYFdjLYdiSMNYW8GlIcqN4PViGdysxZCa5rFZtLn66WzZoWqovtS9JuyNM1FZ7_sEDm66LlHXb4UXqX-jVqdChdO4DU53sVXxtBTwOrcqcvXe4nougEXXrL3f-dDb3MT55pWPTwLiXxT74PdxaldiXVT0rFG_ogaDCmvrre_aekq_wV-QZhRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ با انتشار این پست ادعای مارک تیسن مبنی بر اینکه بیش از ۱۰۰۰ کشتی با اسکورت از تنگه هرمز عبور داده شدند را تقویت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/70439" target="_blank">📅 01:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70438">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J75e18vPc6u7xsUuc7xMYkbdIZmTmh6DxaTL9Dycb8KmeNA8Uk8L7BxCgHIfe6-tQB4Xu72bxqtVbLmI0wGCLJ0s1TGsLpuz2oyImxTNeQvm6bbU9dibS9p1DME9ycg4O2alU5G35pRwOIPAUhvsUa6HIxMqVEXgh3j8JBv0wDwzsq2mSxKla0UsllA8GGCO7gskhwNM9k2VBUiqnAFg6xL_qdoHXIBz45qQaoq6uJipY5m3UthTomxJ8vjHx-WlrjtD8K-dhu7-s9C_NmuOOqUS1l1nqKDIz6D8883S40txxcDcaHOvaclCQz8DTP9hU480BEq1InH-L-iVUpmPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
املاکی مجدد این تصویرو با عنوان تنگه هرمز قلمرو جدید ایالات متحده منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/70438" target="_blank">📅 00:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70437">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39665a7cce.mp4?token=Wk5zDvVLPRukXAPT9IKcmG3z43VYnFzk6Vw9_Tw-Tt9s-o3sXeiXWyJSfqXHXtPOr-kgwmbIWBuufJdAThsfqCF6-_Ri4WbMjaSLn3AVMK6ugl6yFa8dfEAr2Er5w-3j1SNWqfljEkGPGaBbXGq9aujR5OS00l-cULaCDn4wNBo2Ep-zIUtHWbeMHsIbklt48QQT2wWyD0c84zuw_nCJpcdjMlj8hfQd-MjUQuPqmPhjUhjVh9MvnshIGFx9ms2HbnJRcFcAT3ZEiObBMyeHEhodxL-AiQ314tnoF1e7jfdn_pw-d32RNGL2S9tMzH7_R9DzUHPCuUyAb5g6vBkvMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39665a7cce.mp4?token=Wk5zDvVLPRukXAPT9IKcmG3z43VYnFzk6Vw9_Tw-Tt9s-o3sXeiXWyJSfqXHXtPOr-kgwmbIWBuufJdAThsfqCF6-_Ri4WbMjaSLn3AVMK6ugl6yFa8dfEAr2Er5w-3j1SNWqfljEkGPGaBbXGq9aujR5OS00l-cULaCDn4wNBo2Ep-zIUtHWbeMHsIbklt48QQT2wWyD0c84zuw_nCJpcdjMlj8hfQd-MjUQuPqmPhjUhjVh9MvnshIGFx9ms2HbnJRcFcAT3ZEiObBMyeHEhodxL-AiQ314tnoF1e7jfdn_pw-d32RNGL2S9tMzH7_R9DzUHPCuUyAb5g6vBkvMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
توصیه‌ام به مردم اینه که کم کم از تو همون خونه و محلات، شروع به تولید چیزهایی کنن که نیاز دارن
😐
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/70437" target="_blank">📅 00:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70436">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927919a024.mp4?token=jGFYAL9UC5gmxd5Mp6jumPBgQtOJRRLdibnUymluBnyyoohtngP6IbC4aqFRboi_G--ZEkjCTXRxLiRaZm9hGlZx9sfhR6aEfyATKqf-SOupg2drHG5oTRrOjg8GYXtQsTNTzdHD3bqvLxprdtUpkkDNd9qNAX-M0OtelPeri-rQcpTFD4rG4N5C0Ps5YLfou3BzvYyybBZF821O9zbSnr1_7GogANPX6Jjz5CktWGvsFKfaONLjlljAKZbaD8uWObqX93eZrw9PB9XlHadFT6N28AXHeKpPOY8Q4mzfjfuI1WyPVs1psRxGIcXr56IfnjLzJQ5sv0pRovwcoREG7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927919a024.mp4?token=jGFYAL9UC5gmxd5Mp6jumPBgQtOJRRLdibnUymluBnyyoohtngP6IbC4aqFRboi_G--ZEkjCTXRxLiRaZm9hGlZx9sfhR6aEfyATKqf-SOupg2drHG5oTRrOjg8GYXtQsTNTzdHD3bqvLxprdtUpkkDNd9qNAX-M0OtelPeri-rQcpTFD4rG4N5C0Ps5YLfou3BzvYyybBZF821O9zbSnr1_7GogANPX6Jjz5CktWGvsFKfaONLjlljAKZbaD8uWObqX93eZrw9PB9XlHadFT6N28AXHeKpPOY8Q4mzfjfuI1WyPVs1psRxGIcXr56IfnjLzJQ5sv0pRovwcoREG7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محسن رضایی، دبیر شورای عالی امنیت ملی:
🇺🇸
🇮🇱
نتانیاهو به ترامپ گفته ایران رو 6 ماه محاصره کن، تسلیم میشن!
ترامپ بهش گفته اشتباه میکنیا، نتانیاهو هم گفته آقا تو 2-3 ماه تست کن، می‌گیره.
آمریکا به طور کامل از حمله نظامی ناامید شده و محاصره اقتصادی راه انداخته.
هدفشون هم اینه که یه عده معترض رو بریزن وسط خیابون تا اونا به F35های آمریکا کمک کنن.
محاصره و تحریم‌ اقتصادی آمریکا ادامه پیدا کنه، شرکت‌های آمریکایی منطقه رو می‌زنیم!
تا الان هیچ کاری با شرکت‌های آمریکایی نداشتیم و فقط پایگاه زدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70436" target="_blank">📅 23:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70435">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35614b49f.mp4?token=s2U_zMRiClT_XiKVwWrH7pEU6NgWd-oLxPmI-yWG6OCZT9Id0Ql6AWa4JQfjtx0CIkEyYoeHzznxVYGa6TBv3F6FKdmogNUUpxbq3Jw1tIDvHbhttQjCSFr5Op5xsEENcPoDGwvZYvoIA0zY7_MawpBsg7jzYDC55cAgwk_YLJiC6osSCqrKEVbKFOerr4e1kSYEHRQmHp2ZhI4GNhzjSIhDjeNaLoymEiAcKf5h9bk_W6KM6grom_Csc4M9hN_fGZjsUmzg6LUKti4CzbtUrbALEf32KUsHaaWbDXZkFHtSOaea46XxKHQ--QadXWFGMgk3FvyrUW4jPZ_vPbIq6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35614b49f.mp4?token=s2U_zMRiClT_XiKVwWrH7pEU6NgWd-oLxPmI-yWG6OCZT9Id0Ql6AWa4JQfjtx0CIkEyYoeHzznxVYGa6TBv3F6FKdmogNUUpxbq3Jw1tIDvHbhttQjCSFr5Op5xsEENcPoDGwvZYvoIA0zY7_MawpBsg7jzYDC55cAgwk_YLJiC6osSCqrKEVbKFOerr4e1kSYEHRQmHp2ZhI4GNhzjSIhDjeNaLoymEiAcKf5h9bk_W6KM6grom_Csc4M9hN_fGZjsUmzg6LUKti4CzbtUrbALEf32KUsHaaWbDXZkFHtSOaea46XxKHQ--QadXWFGMgk3FvyrUW4jPZ_vPbIq6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
فیلد مارشال محسن رضایی:
در رفتار دیپلماسی ایران قطعا اصلاحاتی انجام میشه و تکامل ها پشت سر هم صورت میگیره
تصور جهانیان از آمریکا به کشوری خوار و ذلیل تغییر کرده و ایران قدرتمند تر شده
ملت ۵ هزار ساله ایران با دولت ۲۵۰ ساله آمریکا داره رقابت میکنه
تصمیم رهبر انقلاب برای آمدن فرماندهان جدید نشونه جنگ متفاوت و غیرقابل پیش بینی از سوی ما هس
حتما شیوه جنگ رو تغییر خواهیم داد
دشمن روی تفرقه و اختلاف حساب باز کرده ولی وحدت ما کمتر از لانچر ها نیست
حماقت ترامپ باعث شده کل جهان خواستار دستیابی به سلاح هسته‌ای بشه
در جنگ جدید اقتصادی نیز به حساب اونا خواهیم رسید
ترامپ خالی بند است چندماهی هست اصلا حرفاشو گوش نمیدیم
وحدت بدون اطاعت از رهبر انقلاب ممکن نیست
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70435" target="_blank">📅 23:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70432">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0dsfEjcvcWFVMXw4vCQK2DJcdnjNvvXUP7Ts8wytIdfVL8qgWsQXUn2NLUfhUPFTxaQGRYLN4sU7HzhkyUeNQ_114FekN6ayzLbeIMOki_WD5VcW3qJw4SHRxhJKEZZZbTV37A261IMoceAHiOYavDUKyhUqotFoDG5G0e8rKFQS1Xkx92twCp5uNfgRCKm5avKbanVfBdJrhDH583t_i8YtqEYQqHFt0Mg8DjnUKfV8gv2xFvW9N1R8v-JshTIST-ti0Q5knp76ER7dfbhReVw9ciOxb8x3c82D0UlCWNOuucZAQqp2qwHoqOHVZAyJnInKRY90kOWVVAOg47pow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dI4oZqN0p0XZ4jl8UNc9qTiN_ohHZhm0LOgLYfFhYd4Ip3u5JFcZqSJpk4ztDs3znI6qsQ1phCWs9dmUuFFgGQOLjIAO6qE4bfn9W2nahYaZJC-2hXO-izMLQv-r7CxnMvSLPlB2NS_FYdSuzS1TkOrPaZYgdRz5NN92QznXs7VkzHbwJiRamuhO9V3vldxADdHr01MaJzi5YbJVGCq8rTmhbNtpLX4pR6bGt27nN7Z9Z6gbsSksCdaQDevcgVInAU7qg9Hihz6I5qAk73WZ6NzZ1MC1mg8jvrVNsqAi0C0i0SUxieSHqTLQ6WvUeFYmzkfDl3CKVmmG6nqi5ESkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KJ8rViFAzHTR3EvtVez1CP8DnUtRuWwOTzMLuL09e4NVhAGG_hNdxxTNaZlrYeemqza37am2QyMyEobOoft3BxAiXWW4q-ZhXIlhL1pSSiSC9rl3d-UULP5PG5dlk6uo3-xDUnixiq6zIQKmO_5iOaXw3fILe5e9LimIXZrArKScuYQs5HNOTn96I6sXztFT5Y82jMDq7CnH0dmE2aAoMd1CSNZfQKKOd-sdjNeQEQbvKXDOhOKKA0JV2gYIzqd4rfmwRKJ-6fqZhUTFuMHc-ZUQyP9Pejet75w3o5Ce3aCy58V0YHkpZAe2Aqc-NY4b_zE94X0H8GL7zj7MVVE3zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
جفت کنین؛ یه دختر به اسم نگین، سه بار به دوس پسرش خیانت کرده و پسره بخشیدتش.
اما بخاطر اینکه پسره با خاله و دختر خاله‌اش رفته بیرون تهدیدش کرده رو صورتت اسید می‌ریزم!
چند ساعت بعد دختره پیام داده که حتی اگه صورتت با اسید نابود بشه، بازم مال منی!
من پنج بار تریسام زدم اما تو وظیفته منو دوست داشته باشی!
فرداش رفیق دختره پیام داده که نگین مسته و با یه پسر به اسم امیر سکس کرده، اما خدا شاهده قلبش پیش توعه!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70432" target="_blank">📅 23:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70431">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
گروهی موسیقی در جنوب ایران همراه با جمعیت، آهنگی سنتی به سبک بندری می‌خوانند و با افتخار نام رضا شاه را فریاد می‌زنند
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70431" target="_blank">📅 22:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70430">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toxu3Rm1WRzv0uv3H7R59q65tYiltbCbv8k7CUroEP6OSnuTkMoHlMKOPvi0FfaSfe94sdJyiexPrAzwr6FAycBBxXjkFwC9UW_sPrY7-_rZ-u9oGNZaf8GenPTTynXlEDj5y9227Y_J5QYEsO0ByZV6pUT7G8iVRgfaxwFbe8QTcV8umAe_7E8he8hvhnvarjf2TNUelfbFCCSx3dmMHraxQL057AuS_jDDAIDe-NUedNzhL8VPNHIhvR3nPdw5v2IWak3YkTrS4W3_GnvA93spRMtCJB_mQ8S1asPgrUoTqqrMrPTZEmKRLq1z8RuwR0S2t5mQzcWkI3XMKL1Qtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اینترنت یکی از استان‌های یمن رو قطع کرده
حالا خبرگزاری تسنیم اومده نوشته اقدام ضد انسانی :))))
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70430" target="_blank">📅 22:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70429">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b6fb2242.mp4?token=tMYR_AmH_-jkcmMwqlhUcep7_zXxOvzQaYShBoDlDjbFvnZ3v9fAMhtzbZY3RvLh_SfV20HKjFqhEzBwQHb07Rrym0Knse7c7Yeo2RyBxq_Mwf0VXFSyoGJKQbrT8GlqPz49qA9h28Fkd45xkGv4nEmK6kXZx_9Ygog_gxntkCeJGZjxE4KACQ_QHVJOuE6kNHb38jfH8CwuAy6HqGwB9lKCUTB7nqALgDiVo8Ou--hDfJ6XbDwvh6d9D2WJEhiHOcE2_otmn5ErCbn8W91e8lUp54KpQtVR8LY9LjpStbDaorTfFymkzTcj9_2jYm_W-Z614btdcuDYvK9mG2B85Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b6fb2242.mp4?token=tMYR_AmH_-jkcmMwqlhUcep7_zXxOvzQaYShBoDlDjbFvnZ3v9fAMhtzbZY3RvLh_SfV20HKjFqhEzBwQHb07Rrym0Knse7c7Yeo2RyBxq_Mwf0VXFSyoGJKQbrT8GlqPz49qA9h28Fkd45xkGv4nEmK6kXZx_9Ygog_gxntkCeJGZjxE4KACQ_QHVJOuE6kNHb38jfH8CwuAy6HqGwB9lKCUTB7nqALgDiVo8Ou--hDfJ6XbDwvh6d9D2WJEhiHOcE2_otmn5ErCbn8W91e8lUp54KpQtVR8LY9LjpStbDaorTfFymkzTcj9_2jYm_W-Z614btdcuDYvK9mG2B85Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه عده از مخالفای بی‌حجابی تو محمودآبادِ مازندران رفتن فرمانداری و علیه آدمای بی‌حجاب شکایت کردن؛
حالا فرمانده نیروی انتظامی محمودآباد هم با این سیس و خنده‌های ریز اومده بهشون قول داده که با بی‌حجابی تو محمودآباد برخورد می‌کنن تا یکم آرومشون کنه:
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70429" target="_blank">📅 21:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70428">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48faea4858.mp4?token=id4wu-5LDbgc9P4IshfyYmjv_95B6uipuCSlKh6mLaMnMk1Sg2FPWSxFSMeXQT-Qt-nPG-znJhSeW91orJW4TBklUVT_vjwjD-0Zt6b0KaOjJUzbo_htqSzAGvuTn-zO3WkspYiLyb5wdmVdzn9XjUKnWwyLeeWiuUzUoAY4lJcRCT-9hyaZMy2IVknHJtuQ7DNGz0LZ6OqBElbjalO7lXdvq69RJUYAC5mkTq21s0Bo6LoGEVofz3b_ZRWYeMdwz67TzzzFdyWs-QF3T5lGh8Gl3zcufNYsnvoGRcCQXot_t1z3vSQz7qKfxCmIPcvPsYAQqKwpFPb55prOjEoaGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48faea4858.mp4?token=id4wu-5LDbgc9P4IshfyYmjv_95B6uipuCSlKh6mLaMnMk1Sg2FPWSxFSMeXQT-Qt-nPG-znJhSeW91orJW4TBklUVT_vjwjD-0Zt6b0KaOjJUzbo_htqSzAGvuTn-zO3WkspYiLyb5wdmVdzn9XjUKnWwyLeeWiuUzUoAY4lJcRCT-9hyaZMy2IVknHJtuQ7DNGz0LZ6OqBElbjalO7lXdvq69RJUYAC5mkTq21s0Bo6LoGEVofz3b_ZRWYeMdwz67TzzzFdyWs-QF3T5lGh8Gl3zcufNYsnvoGRcCQXot_t1z3vSQz7qKfxCmIPcvPsYAQqKwpFPb55prOjEoaGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید ماساژ هپی اندینگ به گوشتون خورده باشه، حالا چی هست؟
بعد از اینکه ماساژ صورت گرفت، آخر کار نواحی جنسی مشتری رو لمس میکنن و ماساژ میدن، تا ارضا بشه.
حالا با یکی از خانمایی که ماساژ هپی اندینگ انجام میده مصاحبه کردن!
میگه هفته‌ای ۵ نفرو ماساژ میدم و از هر نفر ۵ میلیون میگیرم!
یعنی با روزی ۱ ساعت کار در هفته به غیر از پنجشنبه و جمعه، ایشون ماهی ۱۰۰ میلیون درآمد داره!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70428" target="_blank">📅 20:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70427">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
اخوندی که بی دلیل و بی اجازه از یک زن ایرانی عکس گرفت!
زن ایرانی شجاع بهش حمله کرد و چند تا مرد دیگه هم رفتن بزننش.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70427" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70426">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70426" target="_blank">📅 20:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70425">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivUBTYQDZ88LcQFP1-6NF458VkX65B7J-p_rG2sFS-6SUzrYWAQjaWQ1NkQ4Yna1As-WnlvNHNLyD22hODVVC-fIidpxp5ggh83hke-9dC-DiRMGegJl-5_YMlvdpCwnnHm_9qmjviE2W3oqCXSNR2ilromoFCaGneTeKNfdcPueBpmze-9SzT7KDDAw7dNZGZYA8WJjrCYG7niBilvyAunXdvBnOx6u_Kn-v-NOfaHB9XPx49-PHK9d6O-xO4LEeZOKUgW5ez4Z1I71440q3DLfRr-TwSZdr_5H6CbTgTldhQrDkFX5ZKWABncpjtjRnKAYgdxxXuyyEczqrz51Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70425" target="_blank">📅 20:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70424">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89c9ecf73f.mp4?token=AH5EoFuGs5wixE9_D3K98sXOERVmOlXbyOMudwR1GdSo0Fbfsr1owBj4gQpmYpZoQe-VyAyIMppsUhK9-tniTSXEfww0huCW5L3sPx-rCrds2Wi3cQfcmVA8d4hvuoNUrcN0yWTs7amz0QOqMy3wWKLVS0-G8XTGndoKIB4BOUj6glnDPkVJaaYSr4Vbnr9tUEav-4uGubscfgCPG6SMUdYR82JngRgCOX8gZHuf3aGjs1qa7aZWFu2UKi2FD7yx8gE4BXnaSty8STOUhlFzoRzmY0R7h0pERkPziqXPDQew1u0BUnJ9fp1u2_fNHcv1pA4npE8ILAZMAxFfhjE-jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89c9ecf73f.mp4?token=AH5EoFuGs5wixE9_D3K98sXOERVmOlXbyOMudwR1GdSo0Fbfsr1owBj4gQpmYpZoQe-VyAyIMppsUhK9-tniTSXEfww0huCW5L3sPx-rCrds2Wi3cQfcmVA8d4hvuoNUrcN0yWTs7amz0QOqMy3wWKLVS0-G8XTGndoKIB4BOUj6glnDPkVJaaYSr4Vbnr9tUEav-4uGubscfgCPG6SMUdYR82JngRgCOX8gZHuf3aGjs1qa7aZWFu2UKi2FD7yx8gE4BXnaSty8STOUhlFzoRzmY0R7h0pERkPziqXPDQew1u0BUnJ9fp1u2_fNHcv1pA4npE8ILAZMAxFfhjE-jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
۴ سال پیش گفتید تحصیل تا کلاس ۸  مجانی میشه، به کجا رسید؟
❤️
محمدرضاشاه:
اون که مجانی شد هیچ، دبیرستان و دانشگاه هم مجانی کردیم
🎙
خبرنگار:
گفته بودید سال آینده درآمد سرانه به ۱۸۰۰ دلار میرسه..
❤️
محمدرضاشاه:
۲ ماه پیش رسید به ۲۲۰۰ دلار
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70424" target="_blank">📅 19:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70423">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tddO0U_-BeKKuALUFuchRUbZwKEdegwOrHHHFPBmL_RBxu7fTFvEgLRlMVYJ4MxG8wWBVi6Ali5SefsMX4ykBzMJ7_d0omu2tp7IgHJRIwm23tfGwX2v62VFnUKtyAj4uTG4Ot0uBmrLJHnayY77pHatD-ET0jU4mRF9GGXlcyivAgItmV_asG5nESn_ETjiM6nG29xoBwtR6f2AFVQnpDr9pEqqQbNjW_Z6ykTE3sVlx5vTCmuOdf8hnWzu6qWBvTCyyPL8dptfyxmvLljPCncupDEZs7oCi4rhVzYApSvqNl5t2gTPhEqkMQof_K8j5b97UB9U2lL8_J9cpKdqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
📰
اکسیوس به نقل از سه مقام آمریکایی:
شامگاه جمعه حدود ۴۰ نفتکش در هر دو جهت از طریق کانال آب‌عمیق جنوبی از تنگه هرمز عبور کردند.
در طول شب، حدود ۱۶ میلیون بشکه نفت از طریق این مسیر جنوبی از تنگه خارج شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70423" target="_blank">📅 19:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70422">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193d1b1501.mp4?token=TeCDx1c7TDZaRbaPgVNFHVBGsAHip_vo9UdhqvThxfGEBPYYOe1Qe1CRpwrlDhtZAsi-vQ3TDDB7UuRcqZQV_yZYyzdxMOi80QJ9Tcn-T0D__It7KZIjHNxbX7aBe7wveDSaRzYH5oMDtdUbi4SWGb_Z-EIpaPIRYb8QqOjRCFSiMsmpJduMDhhAiS2f-xZyD5w81XQXumt1Rd3xzH8V26Odi2HXT-3_i0bFGkCZ823rqU8fYzH1J0qnDr8qfiIHvB5mOdVFDupCdtgqinUk_TwG6va5wz_8fzG3pPcbxzV6ateJVDlJA1PP_POPDoq9jcLgWFvnK445s4_EXVdABIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193d1b1501.mp4?token=TeCDx1c7TDZaRbaPgVNFHVBGsAHip_vo9UdhqvThxfGEBPYYOe1Qe1CRpwrlDhtZAsi-vQ3TDDB7UuRcqZQV_yZYyzdxMOi80QJ9Tcn-T0D__It7KZIjHNxbX7aBe7wveDSaRzYH5oMDtdUbi4SWGb_Z-EIpaPIRYb8QqOjRCFSiMsmpJduMDhhAiS2f-xZyD5w81XQXumt1Rd3xzH8V26Odi2HXT-3_i0bFGkCZ823rqU8fYzH1J0qnDr8qfiIHvB5mOdVFDupCdtgqinUk_TwG6va5wz_8fzG3pPcbxzV6ateJVDlJA1PP_POPDoq9jcLgWFvnK445s4_EXVdABIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
علی عبداللهی، از یک کارخانه تولید موشک‌های بالستیک زیرزمینی بازدید کرد تا از آخرین پیشرفت‌های مربوط به تسلیحات بومی مطلع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70422" target="_blank">📅 18:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70421">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e0051dae.mp4?token=Di0hOOzwrNSY23FuKILoj_nielQiFjCitTkuI1T0hJ9DdnXdAC6eiIwsFX6n075WjS82nCBqr5ROMfrckh82afvtnK8pGcsEqfihEUwhC8Jbqjl9HvGadBfv2dqzZraVdBywPWgCcbUbbTdGLtNqdhlLiMBGaQg6rswAY2Wwct93EjWjmiNxbfeYDf0lwMvm8OGxlnX3RUICpXonQXZBRzhamJKGwHMVR-mLjm_X45FhBOyM_UZ0r6vIT_72VKJujzfEvi8zmlcaJzf_Dbmv7zJyKH9AQS12OYcyPzv813xcMXBxTqRjXnR-l8TSlNBKM_1wyvP8cFYpjPPydJE--g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e0051dae.mp4?token=Di0hOOzwrNSY23FuKILoj_nielQiFjCitTkuI1T0hJ9DdnXdAC6eiIwsFX6n075WjS82nCBqr5ROMfrckh82afvtnK8pGcsEqfihEUwhC8Jbqjl9HvGadBfv2dqzZraVdBywPWgCcbUbbTdGLtNqdhlLiMBGaQg6rswAY2Wwct93EjWjmiNxbfeYDf0lwMvm8OGxlnX3RUICpXonQXZBRzhamJKGwHMVR-mLjm_X45FhBOyM_UZ0r6vIT_72VKJujzfEvi8zmlcaJzf_Dbmv7zJyKH9AQS12OYcyPzv813xcMXBxTqRjXnR-l8TSlNBKM_1wyvP8cFYpjPPydJE--g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
📰
فاکس‌نیوز:در حالی که دولت ترامپ آماده می‌شود تا موج جدیدی از فشارهای اقتصادی را بر تهران اعمال کند، او می‌گوید که ایران در حال تغییر موضع و نرم شدن است.
ترامپ می‌گوید: «آن‌ها اکنون دارند کوتاه می‌آیند، چرا که وقتی کشوری دیگر نیروی دریایی و نیروی هوایی ندارد، حرف زیادی برای گفتن باقی نمی‌ماند.» او می‌افزاید که بسیاری از رهبران ایران کنار رفته‌اند و «اصلاً نمی‌دانم باید با چه کسی سروکار داشته باشم.»
این اظهارات در حالی بیان می‌شود که ایران سیگنال‌های متناقضی ارسال می‌کند: رئیس‌جمهور مسعود پزشکیان می‌گوید شاید زمان آن رسیده باشد که «همین امروز به جنگ پایان دهیم»، در حالی که رئیس مجلس ایران لحنی بسیار سرسختانه‌تر و تقابلی در قبال ایالات متحده در پیش گرفته است.
اکنون فشارها شدت می‌گیرد: انتظار می‌رود اسکات بسنت، وزیر خزانه‌داری، روز دوشنبه تحریم‌های جدیدی را با هدف انزوای بیشتر ایران اعلام کند؛ تحریم‌هایی که روابط ایران با روسیه و چین، چالش عمده‌ای در مسیر آن‌ها محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70421" target="_blank">📅 17:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70420">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d3e5c370.mp4?token=QLE6E3RBuNrBgvVhh1hgYzDKFRg4Kin4uCXgJiu1OPt4lHU8CmM6YHbPydG94QO0MBR-r1_zFfMa77qiuviYbfk_yJeElGXLtdugi4Pyk5546QEmLrjaMO7gZKC7VQEHXRovg38qcUAEtwWdduA56m6mQyyfsMxpxylZgqWC4FJrHqXMfisk5cSZtinn8dP7-9WJVJzGep7meX8bqeCR08HTIeN104CKwXfNSivKX_-N1TNd2OVV88-vY3297b9eab6061-uUwrLmxKqCLwt3i7ThDlGVnTCwmBeUJbALFpD6ta7TVqqx4TTqx6u_0rqBb_Es9vSURCD9oK32FVbL35t5QPV3gKKsJuxdrn35Q2XMx855qTEq6TbXFiixQaGLHuqIZLXZrNxzubg6Me2mdStfNuI99ihJs7GyQ_6VJC7X2XkpX2xQkp41-tpzxl2IfhFtU351nqKRVKImIn76teHq_vESdb_N2fh8RHrZUXOW4k5INqrXW8fmCwzbgB1BGHxXqww9C9bMOYeU4U7nhcvnVLMwfy_he_jCshHLX1PLF5hWaf9W-KSo6sMqtp28LGx-29a0nYy4DYazy_aSOJcydzcvESQhiUOg76QLaP6FW8qVlcpSUsec05MQQVb5J4P9JpC1tgz47lzo-EarOyIAaSq3QRbDRcUkgPVB8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d3e5c370.mp4?token=QLE6E3RBuNrBgvVhh1hgYzDKFRg4Kin4uCXgJiu1OPt4lHU8CmM6YHbPydG94QO0MBR-r1_zFfMa77qiuviYbfk_yJeElGXLtdugi4Pyk5546QEmLrjaMO7gZKC7VQEHXRovg38qcUAEtwWdduA56m6mQyyfsMxpxylZgqWC4FJrHqXMfisk5cSZtinn8dP7-9WJVJzGep7meX8bqeCR08HTIeN104CKwXfNSivKX_-N1TNd2OVV88-vY3297b9eab6061-uUwrLmxKqCLwt3i7ThDlGVnTCwmBeUJbALFpD6ta7TVqqx4TTqx6u_0rqBb_Es9vSURCD9oK32FVbL35t5QPV3gKKsJuxdrn35Q2XMx855qTEq6TbXFiixQaGLHuqIZLXZrNxzubg6Me2mdStfNuI99ihJs7GyQ_6VJC7X2XkpX2xQkp41-tpzxl2IfhFtU351nqKRVKImIn76teHq_vESdb_N2fh8RHrZUXOW4k5INqrXW8fmCwzbgB1BGHxXqww9C9bMOYeU4U7nhcvnVLMwfy_he_jCshHLX1PLF5hWaf9W-KSo6sMqtp28LGx-29a0nYy4DYazy_aSOJcydzcvESQhiUOg76QLaP6FW8qVlcpSUsec05MQQVb5J4P9JpC1tgz47lzo-EarOyIAaSq3QRbDRcUkgPVB8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این مرد ۴۱ ساله درحالتی که مشروب خورده بود درحال رانندگی بود که پلیس گرفتش
:
از ماشین پیادش کردن میبینن دکمه های شلوارش بازه و یه دختر بچه روی صندلی شاگرد نشسته
۵ تا دختربچه خیلی کم سن و سال هم روی صندلی عقب نشستن ، پلیس بهش میگه اینا کین ، میگه اینا دوستامن
درضمن یکی از اون بچه ها هم حامله بوده
در نهایت این شخص به دلیل سواستفاده جنسی از کودکان ۳۶ سال حبس میگیره.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70420" target="_blank">📅 17:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70419">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/357928b911.mp4?token=M-2c8Bcb_tzF3ylFkoMXxOLR5VTwmnUEE_oNy4Q4Fwbg645Om8JufdMKoeyEUzELgG7uQHd5azdJA6YLHUcZiIdKUeWPAlingKRnx79jdbeNSendpj_HGZTPrKzfVJl0EVE5T006Lp_0UqTqAP_WWkml7YNsEIT4UbdB_K39HZrZjr-jdGNHbOzEiQ9mQUNMw6u8ObT_WjUE5hZDWypILHfDIu01FE1jsYu9mhpRU-xnPWqOO8cDHKmYoHPNZcSZ6haPzFIseVNnBcqXKxLOdXJ3m4gXR0Qqy5nrZSV0j23HZJXRen9nWBFNmJqg-z7j3P3aibnf3unyEVeQ-ZnqSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/357928b911.mp4?token=M-2c8Bcb_tzF3ylFkoMXxOLR5VTwmnUEE_oNy4Q4Fwbg645Om8JufdMKoeyEUzELgG7uQHd5azdJA6YLHUcZiIdKUeWPAlingKRnx79jdbeNSendpj_HGZTPrKzfVJl0EVE5T006Lp_0UqTqAP_WWkml7YNsEIT4UbdB_K39HZrZjr-jdGNHbOzEiQ9mQUNMw6u8ObT_WjUE5hZDWypILHfDIu01FE1jsYu9mhpRU-xnPWqOO8cDHKmYoHPNZcSZ6haPzFIseVNnBcqXKxLOdXJ3m4gXR0Qqy5nrZSV0j23HZJXRen9nWBFNmJqg-z7j3P3aibnf3unyEVeQ-ZnqSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دخترا :
خیلی برای کنکور استرس دارم کل بدنم داره میلرزه .
پسرا به روایت تصویر :
خیلی استرس داشتم که چجوری کیکم رو بخورم که تا آخر امتحان کیکه تموم نشه ، که نفر جلوییم بهم کیکشو داد و کل استرسم رفع شد ، دمش گرم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70419" target="_blank">📅 17:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70418">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c46390cc4.mp4?token=IMbhWxkZW0-EZ1lyQp5l6WKwdramoTfA9GsbbrVPnVu_F8K22ewTEm0uEiUbx6NC2gR-kz41g0eX2QgmXO1JsyWOB80r3j3zUl7f59moFQhd0Guu1urNYJJFsESVWU9mxvj3G-6v30bCtw2NJ3lZi2rHWui869hPphbrR-mDJ7cdOxVBGYoKBHjXibegFXHeY2cjhISILhgXqTIO6Tmr3nwzf5KW4y5bzQlGO_7-QIQ2EyEAWKEBZX3i5UeB2LYmBOBvg2ZuSfu1tDYDX1dST_wJ5Ih8YJkX1-y3tiCANlj7kHq5mBRQ6UbUNYrzkVMZ93mQHmlxe8OUYMOCJrqMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c46390cc4.mp4?token=IMbhWxkZW0-EZ1lyQp5l6WKwdramoTfA9GsbbrVPnVu_F8K22ewTEm0uEiUbx6NC2gR-kz41g0eX2QgmXO1JsyWOB80r3j3zUl7f59moFQhd0Guu1urNYJJFsESVWU9mxvj3G-6v30bCtw2NJ3lZi2rHWui869hPphbrR-mDJ7cdOxVBGYoKBHjXibegFXHeY2cjhISILhgXqTIO6Tmr3nwzf5KW4y5bzQlGO_7-QIQ2EyEAWKEBZX3i5UeB2LYmBOBvg2ZuSfu1tDYDX1dST_wJ5Ih8YJkX1-y3tiCANlj7kHq5mBRQ6UbUNYrzkVMZ93mQHmlxe8OUYMOCJrqMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به رسایی:
حضورت اینجا خلاف پروتکل هاست
ولی بخاطر عمامه ات ایرادی نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70418" target="_blank">📅 16:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70417">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e1045a89.mp4?token=PG9TA6f0gVjzzoxkSvN17RmNc1eqtILkJ4Wp7TR-KzPuO2rmG9x069oDeI0ZmD04LGCiGDTlTHcxCHxV4x8wlEkh4-r16B-kR6vQTy940CpCSdvaH0vaL80AjYiZ3aflYKCIwtbqObtOeXjwr3qsnBiXQa4N_6XwboG9Yu7C16qP2v85nyWfktodmaRdtseUmESUHMf4UwzPEPvqEPWm75RX1c4577H26B_WHAmDBxnE4eN7cfJXka7BgI42g0mFw9bn6b-ha1fz_uS2MQY9SeHW74BVV0173cQMIRRt3np-A6aM2au6IX2WM0qa_tKHcAo59IZP2GA2JmlI5XWvrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e1045a89.mp4?token=PG9TA6f0gVjzzoxkSvN17RmNc1eqtILkJ4Wp7TR-KzPuO2rmG9x069oDeI0ZmD04LGCiGDTlTHcxCHxV4x8wlEkh4-r16B-kR6vQTy940CpCSdvaH0vaL80AjYiZ3aflYKCIwtbqObtOeXjwr3qsnBiXQa4N_6XwboG9Yu7C16qP2v85nyWfktodmaRdtseUmESUHMf4UwzPEPvqEPWm75RX1c4577H26B_WHAmDBxnE4eN7cfJXka7BgI42g0mFw9bn6b-ha1fz_uS2MQY9SeHW74BVV0173cQMIRRt3np-A6aM2au6IX2WM0qa_tKHcAo59IZP2GA2JmlI5XWvrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
#تاریخی
؛در این ویدیو، به بررسی نبرد حرّان میان امپراتوری اشکانی ایران و روم به فرماندهی کراسوس می‌پردازد.
کراسوس که برای کسب ثروت و شهرت به ایران حمله کرده بود، با ۴۰ هزار سرباز رومی در برابر ۸ هزار سوارکار و ۱۰۰۰ سواره‌نظام ایرانی قرار گرفت.
ایرانیان با استفاده از تاکتیک تیراندازی از روی اسب به سمت عقب، پشتیبانی بی‌نظیر ۱۰۰۰ شتر حامل تیر برای تامین مهمات و ورود سواره‌نظام که ۱۴۰۰ سال از تکنولوژی نظامی اروپا جلوتر بودند، توانستند ارتش روم را به‌طور کامل در هم بکوبند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70417" target="_blank">📅 16:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70416">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpnE_mcfw3WXUdAfVrvFaTKr2dc1iLrfgtlQEZywvSnPSXYCHS2fHF_vyb2c14kp2hxRtTHSA9f_dHdn_4UyTwQd0Sgjx4lvimMjBI2jPxytJI9Lue84JK4BJqhznUI8nP2-JbFNkpyayK7zkV8CE9ftPsXNDMt8tvLLQh2SkAeCE1rghcKxtdrd1-0TXzbXVGtSSnPZ8o5LaqGWzmagfoEudP_B5isz4rJULVeqtdPxh4H6h9BFy4QlNIh-kxe3GxmvUry6JGEWXIG2rpB7Ua372MV5cX4f5aTIbqksf-x38aH75PyPdU_Pw6dOeqr6hhFKtLVLUuY6pMvMd91sfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یه خانم رفته لیزر و خجالت می‌کشیده که اپراتور زن باشه، گفته یه اپراتور مرد بیارید صیغه بخونیم‌بعدش منو لیزر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70416" target="_blank">📅 15:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70415">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
قالیباف:
ما پیام‌های متعددی از کشورهای همسایه درباره
شکل‌دهی به ترتیبات امنیتی و همکاری‌های اقتصادی جدید در منطقه
دریافت کرده‌ایم.
ایالات متحده امنیت تک‌تک متحدانش را با قلدری و بی‌اعتنایی مطلق به منافع آن‌ها به‌خاطر منافع اسرائیل چنان به خطر انداخت که آن‌ها برای لحظه‌ای، تمام هستی خود را در خطر دیدند.
یک نظم بومی و مستقل که واقعاً صلح و امنیت را در منطقه به ارمغان خواهد آورد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70415" target="_blank">📅 14:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70414">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szRvBYYbVhzvqY-bsGuLvzPw_94QlNmwVrB5ng-FHy9xEkOxKdTRt96nAlury8IiQl3b2-jYuvx9IZ85FMP2IXgldYxFAUk3QgLxrHT60gTrt4L5Qpoy8cQDdYxHDT03zo3utIEWZ3S7iOAsDJFgcL5ubQNG-xNPM3TqZqNnHXnbE0AVYDTKTRQD-SOzD5Umbu-wbrZkFDth1sil-f2C2ylVrr-LuIQrYKsJK1CX1_ICL59Vcy5vzqq2YyhaAmG7uybfEHzOsdkEgUicqcd4kC6HfFSTmHsU3NmiQO7Y9z9gGp6rBP894YQI3CkHZ7ONIYcLPIAguquD849_RKKEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تصویری وایرال شده از پزشکیان:
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70414" target="_blank">📅 14:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70413">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1159d44f.mp4?token=Ec8bQw4FciZkcEp1Tjtfjz-ietUEgTJZEvY_NGloqx9RsRnHyOE1E-04k9zAFiZeEhvvSws0NIwQRYqdtCGdZnc8verJ9A-yRYh4Cg-a_KlGX3lpWiwZwHmZqx1zgc4W1lIRtlaoRYYFicx6Cvavyi5Fc_LaUmoxujfFd5GP8lI77Yg99VGBlN8bdKZpEzUmz5T9Bga4rBfOFknceoi6W1c1Fo-VPp6he1-7kt7Ju643eCUwXpdKF5_FsYLfF9ls3-ZJIvH4IvUr5cPzDiVeevm7IFEqJW_Vex1xC6_60C7JQaOLzR6Xkq6zKTZCFDt8RS_jLQgl4f2gNs0vGEhxiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1159d44f.mp4?token=Ec8bQw4FciZkcEp1Tjtfjz-ietUEgTJZEvY_NGloqx9RsRnHyOE1E-04k9zAFiZeEhvvSws0NIwQRYqdtCGdZnc8verJ9A-yRYh4Cg-a_KlGX3lpWiwZwHmZqx1zgc4W1lIRtlaoRYYFicx6Cvavyi5Fc_LaUmoxujfFd5GP8lI77Yg99VGBlN8bdKZpEzUmz5T9Bga4rBfOFknceoi6W1c1Fo-VPp6he1-7kt7Ju643eCUwXpdKF5_FsYLfF9ls3-ZJIvH4IvUr5cPzDiVeevm7IFEqJW_Vex1xC6_60C7JQaOLzR6Xkq6zKTZCFDt8RS_jLQgl4f2gNs0vGEhxiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:وقتم خیلی خالیه باید چیکار کنم؟
خب الان من چیکار کنم؟ نظرتون چیه برگردم و دوباره ایران رو بیشتر بمباران کنم؟
جمعیت حاضر: آرررررررره!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70413" target="_blank">📅 13:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70412">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWt8YiSOXXt57JKlJsQxprotwNblQzTG1XJHc_GH73R0AeTs2QP8TQU6McJ93w7PfFpIGvv19yU739lgl3ErxA1pcfBJdTgYEPV4uvF9expubzasWzU3NtYFC0wo7d3dk-rDljmM86qL2SMFLQte8H9ilnh8inFG1Q62mg_k6Ixx92L0TJ2I5uMq8-cGm5vsflA2PivAb1wgkcf_KLprrNKDLXJq95vpaPv5pwPeBd8X0v2IKwaq9vQSPhUErmxhzeFMIEFne9UFY3QvvZOgsIxclRYP1Y9VJP6JjYLCmMCAvgps1DandoGDQzqIfhLvMHMDNguSAOqXfxPUk6h8Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
باقرزاده: اوضاع جسمی خلبانان ایرانی در قطر خوب نیست
فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح با اشاره به وضعیت جسمانی نامناسب برخی اسرای ایرانی در قطر، خواستار اعزام یک دستگاه آمبولانس هوایی از سوی کمیته بین‌المللی صلیب سرخ برای انتقال هرچه سریع‌تر اسرای مجروح و بیمار به ایران شد.
وی با بیان اینکه محل نگهداری اسرا بر روی آب، شرایط مناسبی برای حفظ سلامت آنان ندارد، از دولت قطر خواست اسرای ایرانی را دراسرع‌وقت به خشکی و یک بیمارستان مجهز منتقل کند.
باقرزاده از دولت کویت نیز خواست با استناد به کنوانسیون‌های چهارگانه ژنو، حقوق اسرای جنگی را رعایت کرده و زمینه برقراری ارتباط اولیه آنان با خانواده‌هایشان را فراهم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70412" target="_blank">📅 13:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70411">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7PwHAJQ-V9h0wrBoL_smNnMSmn2DljO8kReed-UKU9xSYQCRtEjCWY2D4qWBusUVe6GQWjwLjBGdute47xd97LFE5i44Y8qtw-_PgozPKJckDRYWwh2hA5fqb1ZTDwVo7DZ3dzJU1DpxMBnD0WToofdrlRp6kaIrSeEq3z5gOaFRgrlQ6HK_jCqADJS0emqN5bcYeU2bbkNE-SpVlJayngfybOWkKBeJ-UQbX-tnIZgnnmsUrgyeTnbZPfPriEyWcd6R9InZXAt--kdLinsaeSZadYLppuYk7CRJdasRxYPBa12w4chpiU63K37L6Vzynn5JxnRg4ZBQvbh-BKDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇪
یک تانکر نفتی متعلق به شرکت "ادنوک" امارات، با موفقیت از تنگه هرمز عبور کرد. این تانکر، شب گذشته، از مسیر تعیین‌شده توسط آمریکا عبور کرد و توسط جنگنده‌های آمریکایی اسکورت می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70411" target="_blank">📅 12:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70402">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmczIs0A1WBCqnocM9W7Ydt69-Z06ZMHSSdKOVxpgi4rgX87jPlRoAaszQU-JO-qrnUS7yIjIf7bwrzQjQJ6rj-WpMFJ23XeyPu4Po0Fa5C-kLXj1usf2BPjpSNSiLSfbM5ZcBxMhhT_PXrpACvCERtT5wJcI0R3YadY_GK71JX5Wr4vA_09a-v9RkcJ2cB6yhRlaG0Xk2BJ7UvgjQ55fJEM3esBKvGpa2lICult5aXblzox8KecMLTCk8rUDc4fsMgDy421QjUHpdxz9o5pOj-QtPauo8n2TgYyJAezchX2TP4ylVXZka5cdC3LqLhF1uYLEif0c-MT3TDjmTAXIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJNfmcICqgIpCfvhl3asfB9A-UytEV_imbj8jK4ZVE_o5oQVSYUPj6SmsNldClfI9X6JC_7Mhmj_ap9VxzZjLC99o-V3qH3v67IArJVgWiDss7CAeOiuQJ2fKcPXa2VpHdFdtI-WBfWz6cfp2sv3SM6lOV05MiCLMimj6699OrNXgaMADUggF3reIpyEK4bQ4VU8l_C9PCMtAnbtnM8vE9RjBB2kmapElyeHSul4WWqudP-WfM308JTohNZ0kvRs-IbKX54Dx57bqHrVu7mzY_63qHueQCw90htG9LxoMnsEOkLiu2zDRWxBTDi41mtLocWI1zbxBVSzXC_vcnVICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWZpa2C3i0DQRl5p7ef7uCLKOQQmSQEGdX-w-AobZUGAGu_oLvLQIGic69F1HnM8ootUpwimGdYMfCeto3ZWIIQIhm6iKsIRuP8NbUFjDzxnanQ98LJEZFZXwDOBPuwAyIZI20KxmzpeFJZJfTiC3T7ADb8PltfJsVYQ9Qht1xSVNiAA0mRPE9efyzWGfOmMvwTzYvrwWBTrCtl_TjM2X9cPefBjeO1ESagO6X07XYcVTD5B_cl0ZOZHrd8z508XVQo-2HWWW0i_ijyt1FGEbt5snK3aGlQYT9bjYDi9u6B97PeiJESokjIBh9Ud97jQAuAIu7mMWGxwnryHdbsUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VOYE1aOSEtxhRHw7gR8m8RxcksghJSigsxca0OPA3S1VKGqGXmEGdNLlMtJXRwnKVKG6tHvWk5s4pP98Ti4R_nNw3G4cD1VueVNY9bQk3FyfQE92JGDAN2LHzRYLEFlZY-e3OeqPn9Jc0JSIVXNnIMPKpiwlm49tdXLfeIH5tfW2yjRbn1lLgVQ7WRGV30CS8D1ulCKTkLCQZVDZ-xxr-PwEw49ezzxWF_AklkxBk97GNRMDcKxgQwrTUqkJX0Tx0VTx-92Up2fmmsWs-9wGtcGl49l3mlqnMRLbANmwGKqZ4gjkDB834N6QvfheLmZrqmcG9ixvjOuT7n-3UViluw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9Pr8eRNUQ_SFpdxByd9DVNYm_Vz41cqewraZmb3uDEZJhlr9XT7U6U72jYXwgJOjeD3fFf5pnU5ePHzoMdMLD-fWpOAZp5iwRpB_BUcvhJbDpdlQwEdv_LHpfodBKVoQz6O3to_orh5OfeAK7Verklyc52A1OAfUrj_BYIahmCjRxjVfpl2gEef6_XBQfrpNUa5ES3VLctHT7Ht6GkKqOPRIvUy6Ty9iYRMxT_4BNhuWYrAqIGS8ukeSfrIZPFdcjiTgMd3IcpjCPR9TRdoEz2JFuAAgiZo8wdh-70VESpRtclyeTvJHKfR4aBUcBFDVuLZcC-cPzlHSjs5Q28iQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrcJNbzcb-E_sI2Jjgx-tD7LV1rgAuiVKeXIGahvD7Sr4kpBnE-733FonahxHMqd5JbdfgNvP9BbHGLVqv3iSbNFWc_vXWD72ZS9Usfibnk--5oGtYJ-BGI2y9YI2pDkVAkEkiKUwsc7lWoQDIXp_CaWRvHLtdhvTQ3UxbVN-VpF8tCIUIC2bdAYsMMP63FzGqlQjjalS1c2LO1vg8eCQRhOr8J7601LiXhNe5PqHWsh1_HokjCbEIC-CGkzUK_gABjrK8OxtlpaY20blcYYeS9XLTAQ-_8L8-nczImbvyQ420x-REKrb2OZxkSSzmwTNGER31yK98aE8qtoOBdohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XM2obwwDu2m1a6MJKPK3H5aE2T8yPGbOYaOS75I7BYiv5shTMxPaLZThdrWiT_gKTT5PIpArxKfHr_9hOslmboKrLBWidDo0_uAvhhoZTyyWM9_IobodxL9NlDL1-YcRKMuyJdTzIBvr7iYVXfdGRX6aM_7gijPm89lMk1lfe6I14eqwhpr2qvrxwksNUZadS0L2KbWME48yvwoNAuqWUwnSvQedhb7LIesClq3GfNXPxMhXYh7Z5FSVl_lGlp1NzZ0IfDnQVqpIhn5cXFHZLdRbpbAvhwJu5IDXByu9vD0I7jp8IzFx-tTaw_7xDDRN6UwUjZQqwMSJEsE4tw6LOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eer59SSZIk-bU9sjOV2U-H4L51znVRGGsPdi8EnK-PqZVNvy4rfxYZT-hzLNYMv2oXhESV8GfXB0OPsKNh0R8OSuMvDzGOPxx3WHwJHEAva__kL3KVxUNEOSie72i54KMB4K3-wnJ8_rEIiDBPOvvhV8tK5JITbXetJKicAhBS6gQ943r6ZAA3Iw3Limns_iSH2rgXFlbLgM0c9KX7AMATZjlCF5gIBZoP_qPZhEi-zVv_Wwn-nbKm-goWlDMOQEF-v0f11T4pWH6wG335K8vjLijFLbONSb5FCJBO10mP5gCicg5t3IWmd2-N0bpsa6kjWGITK_t8QamfnAr47ueA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTdZLmKzqPmzbseku6qnzaiFvrudsBhHWnlqfh1gMPMtwGzAYDx7DrK0yd5PVCFWXvI25Qoy-9thN3a4FqVJUDVOqbcOQGe7uJt0AFcl-jeYj1a6rbmwr4NQfExJ7F0G9FaqcYtGylV3yBD73qIfvrIVlTUS297dukT1ogArxQ-Ex2inqmX-S_NZ5IHXda5JwrCqyFYPhMVaUPHP0_XFV1craaem9IYgcDGXzs1LzBP13yjSYpiufl-pbaL_6DWE93FNrjZBlQF4GghH06YF_t8ubjQ53b5XHa0bXGUW5xT7rDt399LoRX9X9KzeFu_3ShJG5eqUnQAHNI3dH8uzrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حملات سنگین اوکراین به پالایشگاه‌های نفت چاپایفسک و نووکویبیشفسک روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70402" target="_blank">📅 12:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70401">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70401" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/70401" target="_blank">📅 12:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70400">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIiqjzX1CI1nMVQGQrufNxxw8NZrfWsuv1R0n-__2rJsPW7RKkaMfnJTNexL4sr1snbWQTtaOeU7MZnnIaRUtE7eJmVFbiFFiCx8QrZjZn3vCz8VIuQ09Er80UQ1dyvO3ahlvQDItArcRBXGC_l5od0p-E-lDMh-GQ_S7Y6hgDssoo61xkFwpcFOx5YM6KPE73tkyPEyyEouu_JNEb4qL0iz78uI9yjrFn7lUXDW0ZTUSoJt8L4Con1u3Rj5K1jpOpiFCvHWK8kUfpwNR5ZqnHiTcrtcS-V0lLPE999PUmM0cyTkOvbMNX54cbaxLnuXBkeisyI1DhIySvyvQKpz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a31
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/70400" target="_blank">📅 12:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163f624c09.mp4?token=lgc9OFdye7VaKn0PKv31KOmBhohhDlLkWVEbVI8I5C4UrG62PW5pbapPbmq-dz8VxlmnWbzyoCmqz2Qj8Lx4y5-pP3tGgqyBqqeF7BN0IrQr4Pajtm6KuNr7Up_cOzuoQ22uSYHHzc5fvSJSOjkyYRL9_5W-XEJjaYTx6g5zGRcPr0VxxKHkVd2ZeEs2Er_Wo0DiuXY6R8s53xxCmlu8A0cPKDAZaMC3D2U3YjhwtDkaa6OpnaIUh62TrOBo9DsuAwaG5_nigGnlpk3bnEE8uWBIm2YgBAxjVw9s7REd3DrU9smkM0m7vD559TRKBANEbOwxUP5dRHPL2HXcq3n5-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163f624c09.mp4?token=lgc9OFdye7VaKn0PKv31KOmBhohhDlLkWVEbVI8I5C4UrG62PW5pbapPbmq-dz8VxlmnWbzyoCmqz2Qj8Lx4y5-pP3tGgqyBqqeF7BN0IrQr4Pajtm6KuNr7Up_cOzuoQ22uSYHHzc5fvSJSOjkyYRL9_5W-XEJjaYTx6g5zGRcPr0VxxKHkVd2ZeEs2Er_Wo0DiuXY6R8s53xxCmlu8A0cPKDAZaMC3D2U3YjhwtDkaa6OpnaIUh62TrOBo9DsuAwaG5_nigGnlpk3bnEE8uWBIm2YgBAxjVw9s7REd3DrU9smkM0m7vD559TRKBANEbOwxUP5dRHPL2HXcq3n5-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
توی فرشته تهران، یه مازراتی بجای اینکه ترمز بگیره، گاز داد و این شکلی خودشو ده‌ها میلیارد پولو بگا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70399" target="_blank">📅 12:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70397">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucKNbIzu8EH1J66QtrJ1BSM8MHLpJqsz04F6tuTFUWD-PXs7vPQ6k-fC0UdQi1hY1G-5hQvRtmwXxEMycWamKAYUt9KnRRwJDuKUUXMXyAoQnbsCPG2kDytMwvgZZIOFb9SiwqZEV6TX130Aesb7YvPh3f8xT3D4rWhoE-_cnUt-no3CzzyGz3B_YFdJJ6aH7SS_2kI9qN7j-xHWQxIxXroaGQ_kvSlY2kOHD7FZ2j25wyiuVft1nfh-her6JoHoDKrtgl5RDybI4RugwD_B5z4ybx24wD-EaFX9izb1VRoK4GnbThze8UWAe41Mzby6PXVHu91c_vykcs5AcWA_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d025747579.mp4?token=QSp4DiIHQcX9N_VpoQwleteHtlKQ1SaoMOj4cdmMbt7S_--DreT6YO1i9jVXlRDSv32i8x4-0OpT9GFyOdVmie-tTGjc_t_ocBB-3vlYolg_wkug3_b5mE9WPGvbhxIrqokmkivDkJMUcEKAgRj_f7VavScXPNk4fWFcvEaINu1pWDlze1tQh2gIQgJ3pLMT6g24JrKYRi3hRa_d2SfBUDf9lkmLlIYAJMbJ6RvNiEoapsdet-BlQquw0iZh9NtuohdalBc4o-1khEm41Sc5Mn8aYfHvQmdzKf7lB0SyrsAFufX927k3XFteM67UD1wjWUhmx1hnYLZ78EDqtHamXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d025747579.mp4?token=QSp4DiIHQcX9N_VpoQwleteHtlKQ1SaoMOj4cdmMbt7S_--DreT6YO1i9jVXlRDSv32i8x4-0OpT9GFyOdVmie-tTGjc_t_ocBB-3vlYolg_wkug3_b5mE9WPGvbhxIrqokmkivDkJMUcEKAgRj_f7VavScXPNk4fWFcvEaINu1pWDlze1tQh2gIQgJ3pLMT6g24JrKYRi3hRa_d2SfBUDf9lkmLlIYAJMbJ6RvNiEoapsdet-BlQquw0iZh9NtuohdalBc4o-1khEm41Sc5Mn8aYfHvQmdzKf7lB0SyrsAFufX927k3XFteM67UD1wjWUhmx1hnYLZ78EDqtHamXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خواهر پژمان جمشیدی :
برادرِ من امام‌زاده نیست!
مثل بقیه جوون‌ها، عشق و حال کرده و همه‌کار میکنه، نوش جونش چون شهرت و ثروت داره.
ولی وصله تجاوز به داداشم نمی‌چسبه چون اصلا نیازی نداره‌
ترانه علیدوستی؟
یه بار با یه کارگران بوده که زنِ طرف فهمیده.
یه بار با یه بازیگره بوده که دوست‌دخترِ ده ساله طرف فهمیده.
یه بار با یه بازیگر که دوتا بچه هم داشت بود که همین باعث شد هم اون بازیگره طلاق بگیره، هم شوهرِ ترانه طلاقش رو بده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70397" target="_blank">📅 11:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70396">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di4D-Az0xCzPe8MZNuQPGqDktHBEqy4qeCQpVfkQwrScT2bTe9xzkjc-MLHYv1wBLY9FDP-PBA5quokzCgby9y-kwWqtSqkoP5Hwr7sYKgG4b5Lb9SDVHRl9BlUCeWzNOn0te8VTP9sPIB5RHPULckeIpzqSHAEranUk96ziOU26WrW6jmaCSHgF2RW_y-E1vE_uq4qtCatv5gRf06N5ZMyxzkS6G39ie3eeheJ-2FZRjBc1pI-mB6FuHKDn58D92vF5Ws3dH3h5Z-JrUvZXf2xYNegiaigqUFzZUh5m8izPyTfvnUzm3XxqPcZmxNsIiWSAjYZVOU60nEwub3iX_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شاهزاده رضا پهلوی:هم‌میهنان عزیز،
تلاش جمهوری اسلامی برای افزایش قیمت بنزین، بار دیگر بی‌کفایتی و نابسامانی ساختاری بازار انرژی ایران تحت سلطه این رژیم را آشکار کرده است.
در شرایطی که جمهوری اسلامی منابع کشور را صرف تروریست‌های خارجی و سرکوبگران داخلی می‌کند، مقامات نظام و نزدیکانشان در غارت اموال ملی با یکدیگر رقابت می‌کنند و بی‌کفایتی رژیم در اداره کشور کمر خانوارها را شکسته و ایرانیان را فقیر کرده است. تحمیل افزایش قیمت سوخت به مردم، اشتباهی نابخشودنی و خیانتی بزرگ است. نمی‌توان بهای سوخت را با کشورهای دیگر مقایسه کرد، در حالی که درآمد ایرانیان به ریال و زیر خط فقر است.
مسئله سوخت و انرژی در تقریباً همه کشورهای جهان، حتی بسیاری از کشورهایی که منابعی بسیار کمتر از ایران دارند، به‌طور روزمره و بدون بحران مدیریت می‌شود.
از یک سو، مافیای قاچاق سپاه روزانه ده‌ها میلیون لیتر سرمایه ایران را از طریق تانکر، خط لوله و اسکله قاچاق می‌کند و از سوی دیگر، مافیای خودرو، خودروهای بی‌کیفیت و پرمصرف را به ملت تحمیل می‌کند. این فرقه تبهکار که قادر به حل مشکل نیست، از طریق دستگاه پروپاگاندای خود بار کمبود سوخت را بر دوش مردم می‌گذرد و آنها را عامل افزایش مصرف و قاچاق سوخت معرفی می‌کند.
جمهوری اسلامی، رژیمی بی‌کفایت، فاسد و ضدایرانی است که خود ریشه این نابسامانی‌هاست و هرگز قادر به حل آنها نخواهد بود.
تنها راه نجات ایران و پایان این چرخه ویرانگر، برانداختن کامل این رژیم و استقرار دولتی ملی و کارآمد است. «پروژه شکوفایی ایران» برنامه‌های روشنی برای ایجاد توازن میان تولید و مصرف سوخت تدوین کرده است. این برنامه‌ها بر پایه بهترین شیوه‌های آزموده‌شده جهانی و تجربه ملی ایران در مدیریت منابع انرژی استوارند و پس از سقوط این رژیم، در دوران گذار، اجرایی خواهند شد.
👑
پاینده ایران،
رضا پهلوی
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70396" target="_blank">📅 11:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70395">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56910ac654.mp4?token=pVDyjiuU5WUjSg3x8AWw1J5sIouktqw9boWLcXyR0wkdmyOsKR8hRY7jgszjrJpiiPU6bAFFCgMDxPMr7QUP1UrYJYJWIO7YdfLgekmfXEeXWPyCJ8AqaHAL6N2jhTVv37dGeqJ2S-779Y8c8AkXV-yYsH-Cu1C4EXrJ-y2De7vzu-HE7V9BMNAswDHtuXlwmE2Q4nUS4QZ9ag4Xo6ehTsIGuern9L12IJggWDgnQwTMHJFj4ECO2fNPm6aaFjIA9Embyau41VXdFswmRG-ODlgKeU1HT9HnxH4hWW3rdrM1WwcDFRQw_1_ryuPl9qapJj7knW4jdsP0REQ6-PuexQZqlEBfZ7zw9PMIHIzHinQ7SAdf-YvewieSP-HiiUAiTmFf4b3Mc1lVxvHu-W8Ggxm1lbub766jOj6YaBNXV7r7d61xfiSfLLYFjT0q-Gg_LePbJNCB8iwnyOdL8DlkBq34H0s7NU90VnWrpOveAoA0ezUs7C-2Y6NaXtFWAL47CYcXA1Fz8P7C8L3ojWd3hTNimoVbW3YcK0rE__-VArQNqPN0Aq1YVYUyMw9lZj8f_CkcoRUXhvZmlyp7NUKdeuHhIP5YSFrnZfB3oat8EiDhzJSdEvUdO05mZHNRlWjW7CJH_X7JfRrB4RTNKAxLlZwj3FRvwiEBlFzglqaXtMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56910ac654.mp4?token=pVDyjiuU5WUjSg3x8AWw1J5sIouktqw9boWLcXyR0wkdmyOsKR8hRY7jgszjrJpiiPU6bAFFCgMDxPMr7QUP1UrYJYJWIO7YdfLgekmfXEeXWPyCJ8AqaHAL6N2jhTVv37dGeqJ2S-779Y8c8AkXV-yYsH-Cu1C4EXrJ-y2De7vzu-HE7V9BMNAswDHtuXlwmE2Q4nUS4QZ9ag4Xo6ehTsIGuern9L12IJggWDgnQwTMHJFj4ECO2fNPm6aaFjIA9Embyau41VXdFswmRG-ODlgKeU1HT9HnxH4hWW3rdrM1WwcDFRQw_1_ryuPl9qapJj7knW4jdsP0REQ6-PuexQZqlEBfZ7zw9PMIHIzHinQ7SAdf-YvewieSP-HiiUAiTmFf4b3Mc1lVxvHu-W8Ggxm1lbub766jOj6YaBNXV7r7d61xfiSfLLYFjT0q-Gg_LePbJNCB8iwnyOdL8DlkBq34H0s7NU90VnWrpOveAoA0ezUs7C-2Y6NaXtFWAL47CYcXA1Fz8P7C8L3ojWd3hTNimoVbW3YcK0rE__-VArQNqPN0Aq1YVYUyMw9lZj8f_CkcoRUXhvZmlyp7NUKdeuHhIP5YSFrnZfB3oat8EiDhzJSdEvUdO05mZHNRlWjW7CJH_X7JfRrB4RTNKAxLlZwj3FRvwiEBlFzglqaXtMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کجا بفهمیم طرف قوای جنسی قوی‌ و کمر پر ملاتی داره؟
این 4 نشونه‌ رو تو هرکی دیدید یا فرار کنید یا سفت بهش بچسبید:
صورت رو به سه قسمت تقسیم کنید، قسمت پایینی از دو قسمت دیگه بزرگ‌تر باشه.
فاصله‌ی بین لب بالایی تا بینی هرچقد ارتفاع، عرض و عمق‌ش بیشتر باشه.
لب پایینی گوشتی باشه.
سوراخ بینی گرد و بزرگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70395" target="_blank">📅 10:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70394">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxRphIgX-JA0g6x_XiUjRpDi3JsM3bBQRypgh2VBM3-KKcJbuoT6eFE-J4QsN9s0kGnzpf_hmb1YP9wPTF20L0zI5nU-_yAql0M_ERF9WZXZtHiZTeZx9hIG--gCFLVfTfzW7G1MYw6s2pxW1bQRHXAqARH4Fk9Fb--hBxJs-hkqDnCD34_ySrQ5oj5qhB9_t8nMHfojbyip-I_i46Uf-gbmO57CooMMZT2vqzo329UNwVlgrn1YAaWVwALGrDlgSAR78HRzaLGnrRSyoCELVBRvQ9qpGjTS-D1N6XoP5mb4YXCdJ5InWhuaidVpMN5XcNlX2MpxHbDT6uLO6QAe3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
〰️
سنتکام:
نیروهای آمریکایی مسیر ۶۸ فروند کشتی تجاری را تغییر داده‌اند، ۳ فروند را غیرفعال کرده‌اند و سوار شدن به ۲ فروند دیگر را انجام داده‌اند تا از رعایت مقررات مربوط به بن‌بست اعمال‌شده بر بنادر ایران اطمینان حاصل کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70394" target="_blank">📅 10:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70393">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49fa266ff.mp4?token=DDhuCyDCcZlOCWHa29EIdItEiCUr2b5dLbXzHYu62jaj9ksbZSDa_Aqxyovv1A8nDwqaaaxmb3e1BQ84-ARX-X6n0E4H7UX6L7rSaHveP5tOQoAfaLqg52EBr7Rif5o-t0bOzjn4RYCCr4RkhfAWgAa4_7EU0lTj31-fvpajkE9fIpHrmj94fuCK7V-eyACQLY34DHo-7MprXFyVcAiKHnoaM1XWvryOcn5xi_MWEfwJKledxe4j-gYIc48NYXelu-_HJfziSlilNvmuI8riy7DXWIJjIcrVqY0evUbl3GVjJBorLyBMOxaJroZNRfz_U_Kyk9NKIb0F9TTw9ak2Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49fa266ff.mp4?token=DDhuCyDCcZlOCWHa29EIdItEiCUr2b5dLbXzHYu62jaj9ksbZSDa_Aqxyovv1A8nDwqaaaxmb3e1BQ84-ARX-X6n0E4H7UX6L7rSaHveP5tOQoAfaLqg52EBr7Rif5o-t0bOzjn4RYCCr4RkhfAWgAa4_7EU0lTj31-fvpajkE9fIpHrmj94fuCK7V-eyACQLY34DHo-7MprXFyVcAiKHnoaM1XWvryOcn5xi_MWEfwJKledxe4j-gYIc48NYXelu-_HJfziSlilNvmuI8riy7DXWIJjIcrVqY0evUbl3GVjJBorLyBMOxaJroZNRfz_U_Kyk9NKIb0F9TTw9ak2Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Ai
❌
IR
✔️
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70393" target="_blank">📅 09:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70392">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15aadac163.mp4?token=PiKmngOoLoJHuiEUNZzE5HTsqGoEQwGWvbfuAn07OYZyLU2plwVLqf6Z5_qJUDREe8L9JErskDgpI0aEDiCpczaDsmRCvYKcZ3PE1vGxoOVpS-bQXr4DH1gW7wl0w8bgZm1JlyN62wVpHBjIVm16uxeQOgViEa4iCLFRbqmpKTdWazEEXCzlnBLXJroPtpFAc-ckJObJqO0cLwTpEaAShB5W_Lc7EtoX5OpI71lGW4zTs9Jee9jlcJ8GnF0UYEheP4fEKFvjLvynRRPpDCxYa5rI01n4f_drfQylGlo7af73i2pmih7EwoXMOwBQ7CuJ0hLVQOZVCnRtoeH8SHoCVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15aadac163.mp4?token=PiKmngOoLoJHuiEUNZzE5HTsqGoEQwGWvbfuAn07OYZyLU2plwVLqf6Z5_qJUDREe8L9JErskDgpI0aEDiCpczaDsmRCvYKcZ3PE1vGxoOVpS-bQXr4DH1gW7wl0w8bgZm1JlyN62wVpHBjIVm16uxeQOgViEa4iCLFRbqmpKTdWazEEXCzlnBLXJroPtpFAc-ckJObJqO0cLwTpEaAShB5W_Lc7EtoX5OpI71lGW4zTs9Jee9jlcJ8GnF0UYEheP4fEKFvjLvynRRPpDCxYa5rI01n4f_drfQylGlo7af73i2pmih7EwoXMOwBQ7CuJ0hLVQOZVCnRtoeH8SHoCVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصطفی خوش‌چشم تحلیل‌گر صداوسیما:
ما همه کاری رو در دنیا میتونیم انجام بدیم.
بریم چندتا مین کار بزاریم توی خلیج فلوریدا.
خنثی کردن این مین‌ها هم کار آسونی نیست و کار سختیه.
شما برو چندتا مین پیشرفته کار بزار اونجا تا یکی دوماه مصیبت بکشن.
بحث من الان تنگه هرمز نیستا من کاملا جدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70392" target="_blank">📅 09:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70391">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70391" target="_blank">📅 03:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70390">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=mGy-CqXCks3cNIMtWakB1Jy4laDdKuFUiip7IdVBQSHC8eu209ULa-DuYRT7YDVBc25NbcadPSpxoaXJXAqnNVs3V47WQoOoUXFGNjio3aTP19StWOesaVz1IePbAmW5B3WQgg36iUF4c3TNyN5BqsxUa9R-YN2i8CNfJWFkYfHBzlJr6aGQdfh5WiOkPq9LBfvAr76rBsL77F3-Xjci3CcgsA_3RGtNucmP2p4MxlDnEOOmBzhFhqqZR6kcGQLEhS09CgmM5AaQssMrY_pJdOwkpNGhliE4Ye01dAPCgiPU0SHesyO_GBKh2I2V0420gnxDdKawZo29cDumdgaO5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=mGy-CqXCks3cNIMtWakB1Jy4laDdKuFUiip7IdVBQSHC8eu209ULa-DuYRT7YDVBc25NbcadPSpxoaXJXAqnNVs3V47WQoOoUXFGNjio3aTP19StWOesaVz1IePbAmW5B3WQgg36iUF4c3TNyN5BqsxUa9R-YN2i8CNfJWFkYfHBzlJr6aGQdfh5WiOkPq9LBfvAr76rBsL77F3-Xjci3CcgsA_3RGtNucmP2p4MxlDnEOOmBzhFhqqZR6kcGQLEhS09CgmM5AaQssMrY_pJdOwkpNGhliE4Ye01dAPCgiPU0SHesyO_GBKh2I2V0420gnxDdKawZo29cDumdgaO5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+UfR2NG4GjAMwNTQ0</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70390" target="_blank">📅 03:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70389">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWenBj5TEMiBRpEA8oFpGiGYXl3HV1IM90IX4t-UQtxg41FxXnywy1BN1eU9BPyi5MTEjFCiq6COluoVEG6q5wZA7iG-XvfINJ9BgJ8eQ0deykIwLg0pNHxsrj1QVrKmWkb6YIsoxtene3hO1MpDaHDhbiORmQeVxtfURhpHDMO0H8KW2Aw6TrsgeWphd7T_5EXeAbxrGLo-SXozrU4askOT5WFHoYoFfiXP4VEhXD0JFBk97koe32g4V0rld21jt_aYcS7P9J3x-ScCYtepV2xzyquWyTQESa_TldKh6I3NPe14hDmaL75oajun_Vuq2-1l_GSUpx6iSZMUh10UxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فعالیت پنج سوخت‌رسان و یک هواپیمای هشدار اولیه در اطراف تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70389" target="_blank">📅 02:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70388">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c253cab7c2.mp4?token=cI9H0olHvPqD9gv_qIDEPm7ZgrX3Qvo9GujdAFEcHT8UNstda2tboJ3XZF5NZNjig_nwG3wbrr5yDAwsvNQP7QGURjKcvfVxyI8bE_y8uDCIx7wfI7nXWJ4Ml4MMuVjVUBjzUHyHgpZLhJbLkhMnNbvao5Is_C2zZCU-b3qgo1AChGXxiUOilgSBYe9uhz7KZQqJk-29s17il00a7Z6Y0PNUkpLynhYhy8IpflTIIcx_MuDb-BO720fwqdxzX-H_lZUtdkQzBEfMqpmXU2iecLtAGCTCHB8kOLKx21DzM-AYLRIUAsBpytKqJpJazrmoyaznffPQ_AbMbn9DTiN4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c253cab7c2.mp4?token=cI9H0olHvPqD9gv_qIDEPm7ZgrX3Qvo9GujdAFEcHT8UNstda2tboJ3XZF5NZNjig_nwG3wbrr5yDAwsvNQP7QGURjKcvfVxyI8bE_y8uDCIx7wfI7nXWJ4Ml4MMuVjVUBjzUHyHgpZLhJbLkhMnNbvao5Is_C2zZCU-b3qgo1AChGXxiUOilgSBYe9uhz7KZQqJk-29s17il00a7Z6Y0PNUkpLynhYhy8IpflTIIcx_MuDb-BO720fwqdxzX-H_lZUtdkQzBEfMqpmXU2iecLtAGCTCHB8kOLKx21DzM-AYLRIUAsBpytKqJpJazrmoyaznffPQ_AbMbn9DTiN4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
〰️
سنتکام:
ملوانان نیروی دریایی ایالات متحده در حالی که ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» (CVN 73) در دریای عرب در حال حرکت است، عملیات پروازی شبانه را بر عرشه آن انجام می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70388" target="_blank">📅 00:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70387">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4291f4458.mp4?token=SZ77NYsnHExALRVBcbDq22xWdTqgOq4p1NY-2gp4GorGOcANUWMZ1zZulkgb_qJ0_p5sSGhgRd8iQaxX325KIWMWGsX76y2szjCKwHlckhMFSt1eFi56cu2UrVaYE0d0r4kqivwVfUI7d4P13geb0YmQ2v_yInf60xrEyXCb47qy3wz3Js39guKI45VULS5M3rZL9ej5LiiOuP8vn-4uzAbydxPF6T2k8ZUE4rHNC2X_2uD3qZnNV25respIaWDxfPFbQ5h3FUY8cKHFyRZ8R-TsR-OPpB7qrI6kgbClqVRcB3oI7vgyuQMSnKAKgpd6JWc4tWwjVq_Jbe0hot3B3ILm05pL_iHfpjrQrVZcUAbN3t3SPY6IGkD2OkIIFN8Vr0RXTI-iyxCUsr1IasvxSFVHxz2ZOrs0Y4QWueRbNv4HwXQQBQlTEIrY7TvQMllW2wjMsuVs2pIk8A6cRbdkkP14pbM2hZwyA_EbNewywruG7YXqNarM4alktsP1X47DPQDm0SmKu9HzWx6yfdoeMta6p_xqYy98z0bCzSUl-nbpgSUiioA5qyzQQapYhNGRPnfhxZTwKSZNey7Mc-MZvijYQmG5WncUCo-qrZTN2GMBvYnfI7yeQqDTQn2tOvh3_kXtNNuV0IUF1hLmJ380x8SrjcouPfhjlcAmwd_B11M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4291f4458.mp4?token=SZ77NYsnHExALRVBcbDq22xWdTqgOq4p1NY-2gp4GorGOcANUWMZ1zZulkgb_qJ0_p5sSGhgRd8iQaxX325KIWMWGsX76y2szjCKwHlckhMFSt1eFi56cu2UrVaYE0d0r4kqivwVfUI7d4P13geb0YmQ2v_yInf60xrEyXCb47qy3wz3Js39guKI45VULS5M3rZL9ej5LiiOuP8vn-4uzAbydxPF6T2k8ZUE4rHNC2X_2uD3qZnNV25respIaWDxfPFbQ5h3FUY8cKHFyRZ8R-TsR-OPpB7qrI6kgbClqVRcB3oI7vgyuQMSnKAKgpd6JWc4tWwjVq_Jbe0hot3B3ILm05pL_iHfpjrQrVZcUAbN3t3SPY6IGkD2OkIIFN8Vr0RXTI-iyxCUsr1IasvxSFVHxz2ZOrs0Y4QWueRbNv4HwXQQBQlTEIrY7TvQMllW2wjMsuVs2pIk8A6cRbdkkP14pbM2hZwyA_EbNewywruG7YXqNarM4alktsP1X47DPQDm0SmKu9HzWx6yfdoeMta6p_xqYy98z0bCzSUl-nbpgSUiioA5qyzQQapYhNGRPnfhxZTwKSZNey7Mc-MZvijYQmG5WncUCo-qrZTN2GMBvYnfI7yeQqDTQn2tOvh3_kXtNNuV0IUF1hLmJ380x8SrjcouPfhjlcAmwd_B11M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی پشم‌ریزون از زلزله شدید چند روز قبل در کلمبیا که باعث شد ساختمونا برن رو ویبره:
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70387" target="_blank">📅 00:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70386">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
⁉️
دقایقی پیش حوالی یوسف‌آباد و امیرآباد و فاطمی و... در تهران صدای فعالیت پدافند شنیده شده.
عده هم میگن صدای تیراندازی بوده و همه چی آرومه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70386" target="_blank">📅 23:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70385">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc11d1c4b.mp4?token=mfVNAOQxDfo84-hysut8J1dJnhJnJ-N28sd93S_YjJipT_a0TDumK9XjBIXvSmGXzxFL3ZJ0nyb0dI4MGsDXX7beVho1yhz6on-F-lzL6D9qER2sg64lGrFgWQvPSmaEeCBp9CbOw5qw9FUc624vqXPi20rIXuv5T9V2Vgh86_rTSpLQLp1pbLf6whE_XPg5D-5gj0reKNPm4Oapr8reYNr-KmgEDisGUGE34WGqoMDlSpqld4Qtk203YX_AndH_7ZHyvvoLDm1zGkbXNPhJcYcqV535kmXSHwrIge_GlGL3NNrLD-4pp-4nDFR8t3azsGa_PLOKBYYIM3wahyIwkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc11d1c4b.mp4?token=mfVNAOQxDfo84-hysut8J1dJnhJnJ-N28sd93S_YjJipT_a0TDumK9XjBIXvSmGXzxFL3ZJ0nyb0dI4MGsDXX7beVho1yhz6on-F-lzL6D9qER2sg64lGrFgWQvPSmaEeCBp9CbOw5qw9FUc624vqXPi20rIXuv5T9V2Vgh86_rTSpLQLp1pbLf6whE_XPg5D-5gj0reKNPm4Oapr8reYNr-KmgEDisGUGE34WGqoMDlSpqld4Qtk203YX_AndH_7ZHyvvoLDm1zGkbXNPhJcYcqV535kmXSHwrIge_GlGL3NNrLD-4pp-4nDFR8t3azsGa_PLOKBYYIM3wahyIwkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ظهوریان، نائب رئیس‌کمیسیون اقتصادی مجلس:
افزایش قیمت بنزین مثل چیپس و پفک نیست که راحت بتوان قیمت آن را تغییر داد
هیچ‌کدام از ۳ طرح مطرح شده، برای بنزین مناسب نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/70385" target="_blank">📅 23:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70384">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9209031f2e.mp4?token=KDntkEoJzBEO8lwo3ktLIImabKbiKfCNgpUf6ID79fRKptUmQUhWhlerY8k1yvKict-DFRiCfhMbNIKHHQ8vZqPDfbK7a5hDPi3aNEkqkBMW4WMrhXJ7ePhBNb4gY3VxrR0oA_GDvqPGZRuCsZF8QW_ObV3gCI4_-9FRH46Kcgz8Cpn2y8whKWlP_kSwlGpF2zRpnieHjW2LeFHMt2B0WzqzsZMp4HeXFzlhaTqPiPQEDtNoCl9npuAVTkPnKMYICprGzcl-lmExpVVh9BS6QXb-fEu_OVw69anZEnF8TM5-uOEIigW5EHRSJ_XmTxGe6v70AzAQg9jXuVIgpHBEqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9209031f2e.mp4?token=KDntkEoJzBEO8lwo3ktLIImabKbiKfCNgpUf6ID79fRKptUmQUhWhlerY8k1yvKict-DFRiCfhMbNIKHHQ8vZqPDfbK7a5hDPi3aNEkqkBMW4WMrhXJ7ePhBNb4gY3VxrR0oA_GDvqPGZRuCsZF8QW_ObV3gCI4_-9FRH46Kcgz8Cpn2y8whKWlP_kSwlGpF2zRpnieHjW2LeFHMt2B0WzqzsZMp4HeXFzlhaTqPiPQEDtNoCl9npuAVTkPnKMYICprGzcl-lmExpVVh9BS6QXb-fEu_OVw69anZEnF8TM5-uOEIigW5EHRSJ_XmTxGe6v70AzAQg9jXuVIgpHBEqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
❌
🇮🇱
فرمانده سابق نیروهای ویژه ترکیه، زکای آکساکالی:
اسرائیل نمی‌تواند با ما رقابت کند، ما مانند سایر کشورها نیستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70384" target="_blank">📅 22:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70383">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXDsWuqk_8yte0oSMnnYgEpQaFtJMI5OBK2OkWZXEMyTv7a4sn-mxWMChk3Qix630Gs_oxnrzJVhqbwBMao3hTlwyK1E3umS-oMixyH00SjQ0Qs2r3Pd5kVQfq8pX2lNDZ9u9BAjAr5luXCHYwmhJY2VIQ_oyx6BdPiLEAQHwe78m6fN9gWK69rqvPOAYCZPaWMAuiwePRRqxRpvOPalk0-ISHYUphSIkCR5I9NAcmpvo-omi-zIxIZ4x98458jq064vDUBnBuzOsVt6VWMzvalflxqujtmHU3OPJAvsJ4bJuuz6L0mxg0r7c3jwHmj530KzWEsUMlOhrTw1dUzkZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ بازنشر کرد:
رئیس‌جمهور ما به ایران هر فرصت ممکنی را داد تا سرانجام رفتار خود را اصلاح کند، از نقش خود به‌عنوان بزرگ‌ترین حامی تروریسم در جهان دست بکشد و به کشورهای تولیدکننده بپیوندد. او درباره پیامدهای ادامه مسیر غیرقانونی و وحشیانه‌شان به آنها هشدار داد. اما «رهبران» آنها چیزی جز رفتار تروریستی و قانون‌شکنانه نمی‌دانند و اکنون رئیس‌جمهور ما به وعده‌های هشدارآمیز خود عمل می‌کند. این‌گونه است که رهبری واقعی عمل می‌کند!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70383" target="_blank">📅 21:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70382">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7188f3aad0.mp4?token=Z5JQo5Upln1a1c-qMX5AIxJ9wikY8p3DxsBxitMuUilPYESsShwI31lqkMWUk7FPUZl2TZJ3Da_Cx8ju_xcvpy_zZb1ok1Ya2tCvZUTxH1LU13CZqJZqPvg-4lifmiufvyTUlcizZDqnaHLQH1PbUgZAA9UbqB5dzvpWK-AJ7j0_VuCpjhoWbQt4zItYFenqOU-Hp61Rr1WlFduSvMqbm28uvj84PAPm9-ejtMk-c2PNYrhx1jUUDdNxfPyAD1giCbHLAo6ASCtZfJ2867_CoPlKT-V-XIAEaoK8Mpj1U4mCigxuQbwRn9l-ZGaDDfqGYe6GLGt1CxDY9LerZbp1Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7188f3aad0.mp4?token=Z5JQo5Upln1a1c-qMX5AIxJ9wikY8p3DxsBxitMuUilPYESsShwI31lqkMWUk7FPUZl2TZJ3Da_Cx8ju_xcvpy_zZb1ok1Ya2tCvZUTxH1LU13CZqJZqPvg-4lifmiufvyTUlcizZDqnaHLQH1PbUgZAA9UbqB5dzvpWK-AJ7j0_VuCpjhoWbQt4zItYFenqOU-Hp61Rr1WlFduSvMqbm28uvj84PAPm9-ejtMk-c2PNYrhx1jUUDdNxfPyAD1giCbHLAo6ASCtZfJ2867_CoPlKT-V-XIAEaoK8Mpj1U4mCigxuQbwRn9l-ZGaDDfqGYe6GLGt1CxDY9LerZbp1Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
در شهر برن سوئیس در تابستان، خیلی از مردم، در مسیرهای مشخص بعد از پایان کار وارد رودخانه آره (Aare) می‌شوند و همراه جریان آب تا نزدیکی خانه‌شان شناور می‌شوند.
لباس و وسایلشان را داخل کیسه‌های ضدآب می‌گذارند و در نقطه مشخصی از آب خارج می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70382" target="_blank">📅 21:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70381">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNtpSnCjGfBRfdCZxJ8PwCDQnbTzzHksPo0eG0-NlBXpsYWxqJRrc4NtQBG236gJ2KMMQTc-C1a5WNH-zK5BBMwN9_Q5GQxm72vUuW9nIibxI0sJlx7lC0l6npcgf0PHHmns7RSiZ5HsKLT1Bo38cSq7kwj4dk888RcdqWrTWVaHCChAc-_PZozofPIHNGxHmdpzr0TypMmYp4FmCZscD2pR-UKsOe1_LQL8lW8UFnTP3hfBKi9jfZfP5wZYLgKRDT3CajVjF64UkiKgtHCE29wtTF8E0c8gvFH9XYTgF3e4OkUsQnkmNVrGCskNciwFxe-idimKM7OzBJBujOvkvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ایالات متحده ثابت کرده است که زبان دیپلماسی را نمی‌فهمد. آن‌ها نه تحریم‌ها را لغو می‌کنند، نه منابع ایران را آزاد می‌سازند و نه به دزدی دریایی پایان می‌دهند.
با این حال، تاریخ نشان خواهد داد که زبان قدرت، آن‌ها را وادار خواهد کرد تا نه‌تنها این اقدامات را انجام دهند، بلکه از ملت بزرگ ایران نیز عذرخواهی کرده و برای همیشه منطقه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70381" target="_blank">📅 20:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70380">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTpk-yMZNpyJ5oToMGXWoTGfx-arnLk58h30bdkOB1mvl9yWRwwcSVTR0kWd-dkgBxEoZI324vKWrLbtk193i7KMu7IkS_C_7YDnX8YdzU-SKCMvv6QCsfjhTNkNLf-XPh0u9WxhC198lIzyYFLc4tgtTBUSrO4JRzU3dKHmTttmsbivypuA90XzvuvwuEO1I4YgmbtI4r8TSBN0XMdLRveVFFSbixwDCn5BCNaMSZ3hui9_KqjdrOr0HDtgsDbunDwVVAoSLS8ZWMDDC3lrOTZZCkyBbj8JykM87Y_6C-xzthsS4MXSQwgNGUqxazOP0eZEG9eUYlFRpHPgsLmE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی:
۱۴ سال پیش: «فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
۸ سال پیش: «فشار حداکثری.» شکست خورد.
۵ ماه پیش: «تسلیم بی‌قید و شرط.» شکست خورد.
امروز: «ویرانگرترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
ما این فیلم را قبلاً دیده‌ایم. همان حرف‌های پوچ؛ همان قلدرها، اما با چهره‌هایی متفاوت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70380" target="_blank">📅 20:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70379">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781f58184f.mp4?token=XaIAmjl4kFWZU5AXXdHj4arRAbzf70XmghybqR1SWuNPzzJ08mj5CkqQe8IauuknQ_8_1HLdhPeK_18b9zH_VCI783uskMFTiI20xAoP8N88vn-JLJ7bKqISUXE7XVGBmeWEO1sf36-BfIGm-2WSyBkqnJbtiPI48o9lQfWEZZnUTr9YamwBVTFqBGWk9QpIt4hHKPbx7CfVMnhoh7iC8Dujs1QcvHCqmhdYiMyM97PkvPnZvn0QU7XLU9K1G6eyzvCEWrF1nQ7HjBynuGlSFNctc1KdDWckUeTIZhyAClw0vMffM026cETr4zyA3uI5VMHejyZPItuYR-7BdhbwnrmFS-NFKMGLiyODsqLVGSg6Xhb66gU2OhqemWyWcJJPXXipvHHMkR6-cA8lspzdnLXhgdtPX5UQm_7W08iTh5ML9UlDN--t95Zb34P36rsdnaEaeNxtPQN6GPR3THOwLT6024t8OUn1OZ_6_764u2u0LFEL-QjIJUn2l2wn-AuwEfJDBSfna3XCuxsgtQHtpsG8EkBEuB0EVwWS9MGgKnfZaxiC6Cv3jj5a0PlsUD_-sg_d0UGkqJT3ThqheCL9-7gO--TCl8gh_h1LtKVbArEEY_CAE2IW-gCT0QvFBzvKjlEY-eDjp2soWI31_dBCezlbzfkngPYzqCrAOMt4gI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781f58184f.mp4?token=XaIAmjl4kFWZU5AXXdHj4arRAbzf70XmghybqR1SWuNPzzJ08mj5CkqQe8IauuknQ_8_1HLdhPeK_18b9zH_VCI783uskMFTiI20xAoP8N88vn-JLJ7bKqISUXE7XVGBmeWEO1sf36-BfIGm-2WSyBkqnJbtiPI48o9lQfWEZZnUTr9YamwBVTFqBGWk9QpIt4hHKPbx7CfVMnhoh7iC8Dujs1QcvHCqmhdYiMyM97PkvPnZvn0QU7XLU9K1G6eyzvCEWrF1nQ7HjBynuGlSFNctc1KdDWckUeTIZhyAClw0vMffM026cETr4zyA3uI5VMHejyZPItuYR-7BdhbwnrmFS-NFKMGLiyODsqLVGSg6Xhb66gU2OhqemWyWcJJPXXipvHHMkR6-cA8lspzdnLXhgdtPX5UQm_7W08iTh5ML9UlDN--t95Zb34P36rsdnaEaeNxtPQN6GPR3THOwLT6024t8OUn1OZ_6_764u2u0LFEL-QjIJUn2l2wn-AuwEfJDBSfna3XCuxsgtQHtpsG8EkBEuB0EVwWS9MGgKnfZaxiC6Cv3jj5a0PlsUD_-sg_d0UGkqJT3ThqheCL9-7gO--TCl8gh_h1LtKVbArEEY_CAE2IW-gCT0QvFBzvKjlEY-eDjp2soWI31_dBCezlbzfkngPYzqCrAOMt4gI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یک آخوند در تجمعات شبانه:هنوزم از کنار بیت رد میشم بوی گوشت سوخته آقا میاد
🤣
🤣
یه روز یکی بهم‌گفت بیا بریم بیت هنوزم بوی گوشت سوخته حضرت آقا میاد
گفتم اغراق میکنی چنین چیزی ممکن نیست
خدا سر شاهده رفتم بیت دیدم هنوزم بوی گوشت سوخته آقا میاد
نامردا ۱۱۰ موشک سنگین به بیت آقا زدن
حضرت آقا بدن لطیفی داشت اصلا ایشون آرزوی کربلا داشتن هروقت میرفتیم‌کربلا میگفتن به نیت ایشون قدم بزنید
الان رهبر شهید شب جمعه ای کنار امام حسین نشسته و داره ما رو تماشا میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70379" target="_blank">📅 19:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70378">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyalegEEyv1HBVhneW72rVeQwg4hVvYKwq38Hp5zTQDsB0G-z8YR_Td1F61-hQStVHs5uq6Lb7tT4Zna7vrz7JWOBbsZ_GN71rOd3ReGAiU66EEgZ59gBCnelUeLOk9C_9WfdJEP0hqGg4nD4y58-9VKTAABPvxWLxgmoVA70aFMHAM1PIV8zuhXgnTSMgoprumbpLl5UmJsqtvi4QiuV7oQUoIMUKp9xnENqrlzWTqXlnsRxBcPhGy-Q5VC4RgE9bfA4rqu1A0MnwxrpXpJAS5kFezX3Vndf85dErk9lmDvqaTEkG9WAD1Fr04w3DUI1hPyNRpYv9dhlIkcCRjBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
〰️
سنتکام:
تا تاریخ ۲۰ اوت، نیروهای آمریکایی مسیر ۶۷ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70378" target="_blank">📅 18:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70377">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb50540ec1.mp4?token=UuyZoT_ZJ6vmzFHhgh9pjEvNDOiQ1bOK5JvEtti8XJcurnembMxl6eJ21duYxbQgsoIq-hRp7l6WbtNL-JUprvGVV_hdSKgl2Jx24DaTZnSnVK2NsgA5UjLhAvoLTLc1NIgn9qoCN0jtc9ILhKnZYpA1P1RGD01E4Ycl5GViZzfiW24VZjWWrBsUteLnqyEZrM_9AJHTvfuQGXNCse3Dvf5L4K4GmpaZtE6Xlx-KdJLehSLutMbM1MCk94xsrCFK-z7aQEhf8L-UAF6Nbd9TRhYt5dyvr-q_qs3P-MNC7s9IrJZqzZKys-bqISBFXc4p9xPL7-xgutHaPbVisXGvZF3bM2oLIFnZemFZJl-YzDAGsPvFjJxRxr-hG245e3V7_6EFziWPf-1vdeOyzYic97r5oj8gXXFzqZdhoME6Q7Zw4fGDUT1IfH0MrJeF4lEwpV9867B2j-vegPVrlgBcdSO_mkQjp3mQI4UTSXjGdscerp5NUftnkCGESSpNvXCwZd8dnjiX729EkNSMpahNnZ3Rmv1h9B421y-h8GUdZE1BBSxgIMyVawKft1o5LnQlGFNY3q9iQ6UsRc5ElPryY7skC6wkkfAJEv9fgo4kC0-lZDlUeHWERBc5WYhrDzE8kNGvYFLYvoVqSWpPeT4P7V05kOYW6R2B5wDvoAcbc9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb50540ec1.mp4?token=UuyZoT_ZJ6vmzFHhgh9pjEvNDOiQ1bOK5JvEtti8XJcurnembMxl6eJ21duYxbQgsoIq-hRp7l6WbtNL-JUprvGVV_hdSKgl2Jx24DaTZnSnVK2NsgA5UjLhAvoLTLc1NIgn9qoCN0jtc9ILhKnZYpA1P1RGD01E4Ycl5GViZzfiW24VZjWWrBsUteLnqyEZrM_9AJHTvfuQGXNCse3Dvf5L4K4GmpaZtE6Xlx-KdJLehSLutMbM1MCk94xsrCFK-z7aQEhf8L-UAF6Nbd9TRhYt5dyvr-q_qs3P-MNC7s9IrJZqzZKys-bqISBFXc4p9xPL7-xgutHaPbVisXGvZF3bM2oLIFnZemFZJl-YzDAGsPvFjJxRxr-hG245e3V7_6EFziWPf-1vdeOyzYic97r5oj8gXXFzqZdhoME6Q7Zw4fGDUT1IfH0MrJeF4lEwpV9867B2j-vegPVrlgBcdSO_mkQjp3mQI4UTSXjGdscerp5NUftnkCGESSpNvXCwZd8dnjiX729EkNSMpahNnZ3Rmv1h9B421y-h8GUdZE1BBSxgIMyVawKft1o5LnQlGFNY3q9iQ6UsRc5ElPryY7skC6wkkfAJEv9fgo4kC0-lZDlUeHWERBc5WYhrDzE8kNGvYFLYvoVqSWpPeT4P7V05kOYW6R2B5wDvoAcbc9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این هواپیما پس از گرفتار شدن در تلاطم (توربولانس) شدید، ناگهان وارد یک وضعیت کاهش ارتفاع تند می‌شود؛ وضعیتی که با پر شدن فضای کابین از صدای جیغ مسافران، موجب وحشت آن‌ها می‌گردد.
تلاطم هوا می‌تواند باعث تغییرات ناگهانی و شدید در ارتفاع و سرعت عمودی شود. اگرچه این وضعیت از داخل کابین ممکن است بسیار هولناک به نظر برسد، اما هواپیما به گونه‌ای طراحی شده است که در برابر فشارهای ناشی از تلاطم‌های شدید مقاومت کند.
بزرگ‌ترین خطر معمولاً متوجه مسافران یا خدمه‌ای است که کمربند ایمنی خود را به درستی نبسته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70377" target="_blank">📅 18:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70374">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3QLlfQwKKzb_zdP5oI4YNBWE_59CSXWP_5_HbZfhiG8Tpot1QXhnCWe4r2y4djfUAB7aGh4RHgx3fV65YqnGQG1iHh55Yz1xlwGrT8FVZMYPne_U4z2nnzK3-BWCtQEwK7qt78YdP94IjIAEJvF5L3FIjeLfbfEyOPDmWvAzNAjfjV4YJhP5nbHiSZ2-peCNrQGWd8570T94XDCrqztg60vAUFcyK5lFCFazs91BK8dQ9F2S3L1gCQ50F_QQD34XcSPW8R-WvnYaWieRzBsB5RpFszk4sSbq2NJyAUr0pIQGc8HKmI-6tJQnPp60cnZFwgCaVhOIOF2ew-dp4hRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjZ5Ftn5-O72vsBgeie0rfQSboJB5Cm3stliGY1mgx7YbRHLhSQ0IQ2J0K2S8kKlS8eDeyV5Onq3b5PILmCRR83v1mKOU_KUaiK5IJDLdDhdRpdOecBvl8msVcq1gMYSMvOxvX4KhOq5sl4SwV6ziTV4PLtxfmuSB1ad0E3w_r9xKqQBuepeX4wsM1QhgAaHvGdiV272Nu_LEl7vfCtz9m46cLJCSPH-lTLKo07yOWVvpsmGOkPkqCE0kAVd7ta_MCYuG1sFvLlOhnIf4HcdeRfuJHWkTbm4vWQIlotvv6ARHkcvntK9BVQrDPQMQ7qHP67pZ1RG69Yw5wdsoc_Z0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee703d2eeb.mp4?token=i4YKNNgTFJJ-h80-7ramYxyJmtS1Z-P77FTzqMp7THMJumVNjzirohr7C00nmxLnyJz3WpCdOYaizTYqIiWBXI8H8mDNT-63HkzIPNRia3db4bPQM-3g2mk-d4Nvxd37-w_qmMjWaQwH483_8Wr9Texw99swQRZ7ZBL6rP0Sh01RX1tMC_Usm--xHaTQOORQZPl1uvqZVUsMOjz1XUQM8D4UOa1UAlsHXff8T0fakbx4sHtwNw5IAiBEt1zd8YvU--vDKQb-58CF7MSPGzyc35rBL-k1NaT194ZP49o3gop62CTOXBi65GSewYJNrrdPsAMBYb6fJs9zNNcfEMwUkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee703d2eeb.mp4?token=i4YKNNgTFJJ-h80-7ramYxyJmtS1Z-P77FTzqMp7THMJumVNjzirohr7C00nmxLnyJz3WpCdOYaizTYqIiWBXI8H8mDNT-63HkzIPNRia3db4bPQM-3g2mk-d4Nvxd37-w_qmMjWaQwH483_8Wr9Texw99swQRZ7ZBL6rP0Sh01RX1tMC_Usm--xHaTQOORQZPl1uvqZVUsMOjz1XUQM8D4UOa1UAlsHXff8T0fakbx4sHtwNw5IAiBEt1zd8YvU--vDKQb-58CF7MSPGzyc35rBL-k1NaT194ZP49o3gop62CTOXBi65GSewYJNrrdPsAMBYb6fJs9zNNcfEMwUkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر لب ساحل ، با این پوشش ساعت ۷ صبح رفته و از اون ور یه مرد با شرت هفتی اومده بهش گیر داده که تو چرا اینجایی پاشو برو تو قسمت زنونه...
دختر هم میگه داری بهم استرس وارد میکنی، مرد میگه استرست بیاد بره تو کونم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70374" target="_blank">📅 18:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70373">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">امروز تو ویپاری رو برد آرسنال
⚽️
100 دلار بزارید 245 دلار (25.000.000تومان‌بونوس میده)  سود کنید.
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70373" target="_blank">📅 18:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70372">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/70372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g39
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70372" target="_blank">📅 18:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70371">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea7209957.mp4?token=CocG6vxFx-k1ZjM1KfasxZMwCV-y7Owz4SCIN1GNNXsEFvQZIfx21rd_KohpP6zMtzOYHkh5DZDAW9FftNkmHk2oQmb7PmYq78BcGcwCzUuDyQfJkal6VjPHvz60WZfLB_il9Bb2vGmUfbp0S3N5tCwrCJNzgfLY0FT2jWVby2rO9CaDbuVLGWXU1T-x7twAwNZdnaAfhZ3a2LaL-yzjX4ES5Sf0rNxX-Sck_0zZw1wpbn4tVT_kcMenf-VMW7e4_vWJHz4jvNa2ZkGRNSC56oD9rSVGfEaUIVkE9UQfr3sDzcMzL9Ts9EDoxBizVqx8n85Tseu1d9LDd_gc3HFcvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea7209957.mp4?token=CocG6vxFx-k1ZjM1KfasxZMwCV-y7Owz4SCIN1GNNXsEFvQZIfx21rd_KohpP6zMtzOYHkh5DZDAW9FftNkmHk2oQmb7PmYq78BcGcwCzUuDyQfJkal6VjPHvz60WZfLB_il9Bb2vGmUfbp0S3N5tCwrCJNzgfLY0FT2jWVby2rO9CaDbuVLGWXU1T-x7twAwNZdnaAfhZ3a2LaL-yzjX4ES5Sf0rNxX-Sck_0zZw1wpbn4tVT_kcMenf-VMW7e4_vWJHz4jvNa2ZkGRNSC56oD9rSVGfEaUIVkE9UQfr3sDzcMzL9Ts9EDoxBizVqx8n85Tseu1d9LDd_gc3HFcvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سری دخترا بخاطر اینکه امروز کنکور دادن، این شکلی از پدر، پارتنر و... کادو گرفتن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70371" target="_blank">📅 18:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70370">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8650fb289.mp4?token=Gc4igRFDe-mWRfuQtD9ribksqR4oFhDvpyls2088XSKzAviKr8So7QPxFi5uSMD9VEl1W3TibD2JmbUhNXPd1IbqLSqDpHk0TCabmwUymnecwjAU6jhI0U4B7M-HVgQfds3uhfWgoOhannCzhjarm0-4-1aGGyt8psg_tkrHJHKGkPGrvmnTAHOfdDgy4-EhXb_4wAOLmI2ts2w7mGPemcmRhHGCyJnyuOnY3lUMZbYY02APXQqm3p_B5ZA02AhGnzI43uoKzcIcagX4A6cMcf7oQeT_CZKU473CzXjLSL4PCkg0wNlPzMclpN4CtCG5XCzswLead9XQP2_Khbn8xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8650fb289.mp4?token=Gc4igRFDe-mWRfuQtD9ribksqR4oFhDvpyls2088XSKzAviKr8So7QPxFi5uSMD9VEl1W3TibD2JmbUhNXPd1IbqLSqDpHk0TCabmwUymnecwjAU6jhI0U4B7M-HVgQfds3uhfWgoOhannCzhjarm0-4-1aGGyt8psg_tkrHJHKGkPGrvmnTAHOfdDgy4-EhXb_4wAOLmI2ts2w7mGPemcmRhHGCyJnyuOnY3lUMZbYY02APXQqm3p_B5ZA02AhGnzI43uoKzcIcagX4A6cMcf7oQeT_CZKU473CzXjLSL4PCkg0wNlPzMclpN4CtCG5XCzswLead9XQP2_Khbn8xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر به اسم امیر 850 میلیون برای دوس دخترش طلا خریده! حالا برا چی؟ دوس دخترش Pms بوده و میخواسته حالشو خوب کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70370" target="_blank">📅 17:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70368">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/600be60d87.mp4?token=SyeRZBMHuyZBWtRQmj-ZD-CCAhdiOTmJaf0wwGwPgk_iTR5yOd2bP68uF5xEQq7D0yJEKbwN6lK0OQPbTw_lJqbGKzF02m07ajzZWAVjGwufNEpUfjNCLRdSPHq08uGgCTa6DMTDqM60koPcPp2aHAmV9ZpukzkUXYEnDjqlGcXQWi5yIgNeqBo_jcKpiPQYK0mtpdxXigfo7gkTDZNRk5XdsV9vVCZh3jBCVWgnYf_rjvx1aUvlLnziOQBCOFrsn1S0QhT6qvPKnk-ujrfzzXEptmL_iGCJhzOm84z7ODKoz_WVUiXerHqhlUyybXnvSnSFy2jAmgVrykixkZrMkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/600be60d87.mp4?token=SyeRZBMHuyZBWtRQmj-ZD-CCAhdiOTmJaf0wwGwPgk_iTR5yOd2bP68uF5xEQq7D0yJEKbwN6lK0OQPbTw_lJqbGKzF02m07ajzZWAVjGwufNEpUfjNCLRdSPHq08uGgCTa6DMTDqM60koPcPp2aHAmV9ZpukzkUXYEnDjqlGcXQWi5yIgNeqBo_jcKpiPQYK0mtpdxXigfo7gkTDZNRk5XdsV9vVCZh3jBCVWgnYf_rjvx1aUvlLnziOQBCOFrsn1S0QhT6qvPKnk-ujrfzzXEptmL_iGCJhzOm84z7ODKoz_WVUiXerHqhlUyybXnvSnSFy2jAmgVrykixkZrMkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود پسرای مجرد به سیتی سنتر خلیج فارس اهواز ممنوع شد!
بخاطر اینکه پسرای مجرد دختر بازی و دور دور نکنن، ورودشون به سیتی سنتر خلیج فارس ممنوع شد!
ورود دخترای مجرد هیچ مانعی نداره و میتونن وارد بشن، بزودی قراره در سیتی سنتر و مراکز خرید سراسر کشور طرحی اجرا بشه که؛
ورود پسرای مجرد ممنوع بشه که جلوی بساط دختر بازی گرفته بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70368" target="_blank">📅 17:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70367">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a5f935a3.mp4?token=vnja9ZFjHtHSwQb4nA1IsYPKs08F95vxblVMY9fgyaBm09IoefJfR8fORIdqM6_hVEKQmAJkuHUpZx6NcFdNJlV3Ln5tTBoP9lD4eCakyYpxFAdXKdAKS8N0lR8nKcz2osPcJgdCXYpckmnVsbDfiPItbsNYiDNfm6JSxvTHg9xprhDKyxSt5F4M1ZorN_ls4R6X-4g7KU0qEE2cnTOjKLd-zqLANyKcvTUKxK_ILs5s1uQ_cXH8sNUtRoTu2ujTOdjr-XLCt9ro4-ypqY9iSQ_ZhjV2epnHXaz3-hsiNK1et-TSA5HWjgXvslf2Qh4nAQZP0fMcnnATcVUT3VCnOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a5f935a3.mp4?token=vnja9ZFjHtHSwQb4nA1IsYPKs08F95vxblVMY9fgyaBm09IoefJfR8fORIdqM6_hVEKQmAJkuHUpZx6NcFdNJlV3Ln5tTBoP9lD4eCakyYpxFAdXKdAKS8N0lR8nKcz2osPcJgdCXYpckmnVsbDfiPItbsNYiDNfm6JSxvTHg9xprhDKyxSt5F4M1ZorN_ls4R6X-4g7KU0qEE2cnTOjKLd-zqLANyKcvTUKxK_ILs5s1uQ_cXH8sNUtRoTu2ujTOdjr-XLCt9ro4-ypqY9iSQ_ZhjV2epnHXaz3-hsiNK1et-TSA5HWjgXvslf2Qh4nAQZP0fMcnnATcVUT3VCnOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداوسیما درباره نتانیاهو: نتانیاهو خیلی مرده؛
همین الان آماده ترین عنصر برای حمله‌ به ایران اسرائیل هس نه آتش بس میفهمه نه خستگی
نتانیاهو مرده واقعی هس نه پشیمونه نه خسته این همه زدیم سرش دوباره فکر حمله داره
با خودش میگه تا وقتی کله زرد توی قدرته باید ایران صد در صدی رو به زیر صفر برسونم
به هیچ قراردادی پایبند نیستن و چون ما براشون تهدید موجودیتی هستیم قطعا اقدام میکنه مجدد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70367" target="_blank">📅 16:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70366">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpXfFA3hkuEKMiDAdGamNxrs-Kb33zKPkugAHLw2NzYykycL4-vNqNTjt5IOE_KbsqUUs39L46Y5l_9I-pYKim1-JkRjy-z_GYDSY2pMyOmLvnvowJn-PFhHgAVL4A30mUr6ilEmbLhy9QitkwTr3m9uBODEC4XOkh_a-sBY75W9vo-HUjnmOtyIrXdL7UIPQ3zomRKzrK_a8sKhIhHO-KCcbjkI2fAHRd4ncmjJ3oi69X4bjusMHigZVy-bVcGQatfJujFWtRfQj6I2CAG0srxLNAB9XremB2wFlJRl9fYHD35ZX7V9foLmwp-gQyvh1SEi1rEYPW5-trt8gHS6yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
پزشکیان:   درباره هزینه تأمین سوخت، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومانی بخرد و بعد آن را ۱۵۰۰ تومان بفروشد؟ ادامه این روند، منابع دولت برای افزایش اعتبار کالابرگ و پرداخت تعهدات مربوط به گندم‌کاران، بیمه‌ها و معیشت کارگران، بازنشستگان و کارمندان…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70366" target="_blank">📅 15:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70365">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⏺
🇮🇷
پزشکیان:
درباره هزینه تأمین سوخت، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومانی بخرد و بعد آن را ۱۵۰۰ تومان بفروشد؟
ادامه این روند، منابع دولت برای افزایش اعتبار کالابرگ و پرداخت تعهدات مربوط به گندم‌کاران، بیمه‌ها و معیشت کارگران، بازنشستگان و کارمندان را محدود می‌کند
.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70365" target="_blank">📅 15:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70364">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzrVObMDfoZv3GQyJYNhm3RRqxOYHFNjQs5InRbpQRdsWCG2fP1Ubjl8MmPk3ASk98ZlKkb7jILbTAVckPIkUv9B8VSGuAqNVLkdVLfHxk5Ap9uZfP8mkXlxX7vzaNYqYDP9e4EbQ6hDGmpP-8JjLwNvF4OkQeJfhAs4Plc1Oj-ze-fzdV6YeSXMJgrAzDoa2gSuZ8q6XYJ5Kli2R6RLsN-BTtbSD27G_fgajzRU_Knl8jn5KcD9l1OQwuYIWnyJMDfNY82_LpEOjMK8PP0-2-2x9T-0Dwd7GLD5eqEpiqVCxWyvY6fCW94lvI8VocgLkcI5eryZJVQgHGAkuvWI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
مسعود پزشکیان:
بهتر است جنگ را امروز، در حالی که در موضع قدرت و عزت هستیم، پایان دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70364" target="_blank">📅 15:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70363">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356ce94a67.mp4?token=DaF0Sj-Gf811gX5sGtZYT-ELDr-YTBvSRJmL05_BryjgRSTRXNib0-l5MvcAB2FygyP5yqNveuVIYKbsCxBEfwAqwoJ8vygdL-phahlWBd2UNoGoRGXAMnZH00sE3n7BADnwbdAWC4ReBxtrSz575mrATz1HEeEuxIPrrIcdr8vFfKXayxZTYwYkJWpVgMDPVlkOZb9JA36QAWVaAOB1lY4xYEbrxPt5OKaeOnsQ_4YaBtiJjAyYTnAUkTCqHAzYTKT_7MzEDZ9Ceg1uSRHWyyGHu_2m8MuiKiCWAl3FQN0Vx7hPfiIsmUmf6Xpt_p9o4PmtTmbYH43zSc8l8j__gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356ce94a67.mp4?token=DaF0Sj-Gf811gX5sGtZYT-ELDr-YTBvSRJmL05_BryjgRSTRXNib0-l5MvcAB2FygyP5yqNveuVIYKbsCxBEfwAqwoJ8vygdL-phahlWBd2UNoGoRGXAMnZH00sE3n7BADnwbdAWC4ReBxtrSz575mrATz1HEeEuxIPrrIcdr8vFfKXayxZTYwYkJWpVgMDPVlkOZb9JA36QAWVaAOB1lY4xYEbrxPt5OKaeOnsQ_4YaBtiJjAyYTnAUkTCqHAzYTKT_7MzEDZ9Ceg1uSRHWyyGHu_2m8MuiKiCWAl3FQN0Vx7hPfiIsmUmf6Xpt_p9o4PmtTmbYH43zSc8l8j__gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وایرال شده از زنی که با اسپری عکس زنای بدحجاب تو لندن رو رنگی میکنه مردا تحریک نشن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70363" target="_blank">📅 14:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70360">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dz5FQN0g6UMPLNSvZ2ebQZzGF_hAxqqidoS_W092EGLgGSg6YewtXOhnSKzROtbNtPopmv1xnqUPmZeVg1mWAQU59Owz7SYKBRqRUfxjPqz0iGHbfqrzkGX5jXXbEIhDZBvwpprCdhLMZt5u1b5itRrYVrHEXd4VoM3_n9mt8kxq0G6BLjTc6S0YmNqrFry_tHTw21pCT_UNjMWv9IFRmVbjXDBNVy0H_ti9PsbqZE1McaZC794n9rSaN__D8fsGBCoiYh2bNJV3Cn2ujaUrfY6fqhX_IYAYnhVVJywM-uRadtG_xJ5WsT2z98IsA8f4sQAvJsIle9oAvgIDSHbTaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smqwouhKG0ffZrZUyYWO-gygO9AxBrAgv_sLIXYIUqbLXc2qT-pStaxwbYsngWvc_qXneYaZ6uue81xuHLt9MSfa8OsVCSW0iuT7ObPm8JF1Pt74WwOXpsg49EBqFx2_o3MVQQnzEMWlpbUlGivtaDZ7YLE3zIjjOZZUhVPLfMrwvK3S6pQvJWxNJaLoRW1wf_Mk59NIiMA5bkuIE7gtL5oC33b7W1LX2zODDL4YIxhyAMY-3BF_81Qo46olzjQmVT7TsF6-h1nINhLDTLY-IOVkKZkiM9mqfU32E41_qlaEAAloyzqcT6rqGhtZ1lnXo2M1aHLp2ebYNAaYF-V-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uCbzmx-cfLZchjpvjY7eyuXkEruZd84ZYJi6ilErHO43CoxoxCMbYbgmgTtHzqfjf1u-8q-8uGFm6ZyWmk36Wozfj-m97kHk7wwKMyFYL4grHhfg6ONTBCCjG5LeVhavjt9a1dvXeqoJgxZHL-TOA7CrHCk2Yy7ff4qnExx0N4eLDL_-Do0hhy7Wvj_G4Oz5gS_iSl8pLNTUtJ3g59OpEmIGJYsndvhiBaiZO_h5HNN0Ns0j7ovo1Cmy2aueJdx7VZe0Z3ZrWl1nc0dF41vJqpfQNMnqcZcjPC31gOM9MSrUjASmKpkpvihVwSsH7e-Dm-4TLn7qi7d1qwC2aDviGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
🇮🇱
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70360" target="_blank">📅 13:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70357">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oV22HT5ujKAW5ril82QGwJNM5_HcLaY8hjeJTXkAgFKyVb2B30g5e0N5GtHpT3QQgsN4YOiHmDSVKLAIZ-lphz6kz09-1Sh1SUg3m0rTjiVwlTf8xtLCe4LPzAB_-Cbelk9Ldwe8Dyn9_dR16RtUVm1hyoSsK4OKObMu7-H81l6qTbPfZON81ZbYkMG426j3Zf6xnxzq7EX9kj5t_MWg7BMHQXiH3Q9e-w6RtZkxSZmthzOdY7b71lLX1UdPzKGCOnL6WWQBHkwmO3D1jU8oGx9PzpnZFi0XSVM3XKd5UCRE9ceUvBCTOMpuacX1o1ywnLymdqOrVvge2Zgq9P4fCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86f5f06d38.mp4?token=MPVngoaQsoCFrsrYVUf3L_gMwF4dbzpIIQx_5nALf5U9dZUFVJjNoPV4mgQxxaTsq1RybXyCZ7g60A0tFN0_X_-Q3_twkOvJ1Twlz7o8NSGxhj4YcDB63wMehWQecLKvuYvNR5hwk2ye07zhOcVxu2KnNhelK_uXdmaEmWeKW9e19RpSuh200lROvKbBC_Rbti-U__WECVxf8MhkGW8VLx4x-7mmXlKFdJ_yNbaRe_E-zSPRwHOE0OROeOJTDiJZ1kvmC4bTZPRQl6LxeE4eQ43pvfrVEhvncEEeUugfgsrGD4DcoeW2sv4aP7fSrHUGjsQyFD4l2_sZgg6wfkgMRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86f5f06d38.mp4?token=MPVngoaQsoCFrsrYVUf3L_gMwF4dbzpIIQx_5nALf5U9dZUFVJjNoPV4mgQxxaTsq1RybXyCZ7g60A0tFN0_X_-Q3_twkOvJ1Twlz7o8NSGxhj4YcDB63wMehWQecLKvuYvNR5hwk2ye07zhOcVxu2KnNhelK_uXdmaEmWeKW9e19RpSuh200lROvKbBC_Rbti-U__WECVxf8MhkGW8VLx4x-7mmXlKFdJ_yNbaRe_E-zSPRwHOE0OROeOJTDiJZ1kvmC4bTZPRQl6LxeE4eQ43pvfrVEhvncEEeUugfgsrGD4DcoeW2sv4aP7fSrHUGjsQyFD4l2_sZgg6wfkgMRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رضا گلزار تنها رولز رویس کولینان منصوری در ایران رو به قیمت 100 میلیارد خرید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70357" target="_blank">📅 13:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70355">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=CerhEi5LEdyn7z5XmErZpUbqNOvUrJCnbO5NKo-93HT2xzZJUkHaxKA_O90x1uGdBqlgxd8Dl86pzR-V0P9fbq1OLHqIP4B0yo2-vs_jUWgaa_XFcNmZKUCC-5vIkQC4R1KL20cicTUODGC_AXQDBx8WMU43FEvFjqIlMtqSzhEYfh-kHKBlzwwd9iU1uUFgwFipmBSnnxxbfh3II1qA_dcdCBH7S6Vpo-_tUWrMcSuBCGeqpyNOWWzoUaGhKk8tO02Qc_jDWqTDBE4lTE9zLY-jTO0NTmi4iU4Q2x_mIR2EafkwL1ws3rfsHvBYVySR7YS5WydOgyrg--6dwi6zyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=CerhEi5LEdyn7z5XmErZpUbqNOvUrJCnbO5NKo-93HT2xzZJUkHaxKA_O90x1uGdBqlgxd8Dl86pzR-V0P9fbq1OLHqIP4B0yo2-vs_jUWgaa_XFcNmZKUCC-5vIkQC4R1KL20cicTUODGC_AXQDBx8WMU43FEvFjqIlMtqSzhEYfh-kHKBlzwwd9iU1uUFgwFipmBSnnxxbfh3II1qA_dcdCBH7S6Vpo-_tUWrMcSuBCGeqpyNOWWzoUaGhKk8tO02Qc_jDWqTDBE4lTE9zLY-jTO0NTmi4iU4Q2x_mIR2EafkwL1ws3rfsHvBYVySR7YS5WydOgyrg--6dwi6zyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو تهران یه دختره بخاطر اینکه دوست‌پسرش باهاش قهر کرده؛
واسش مرسدس‌ بنز AMG GT 53 4MATIC+ چهاردر خریده که شاید آقایی آشتی کنه
😶
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70355" target="_blank">📅 12:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70354">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70354" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70354" target="_blank">📅 12:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70353">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTuue0_r3ICDBdcLQYGDIZgRy3cCZF4krxq0o_YOmm-hD60akXwgfP0zCmILeCcb81iyCNrJU_a9fO8OQUnlCSrey6MwyASJE2gmLHeb5EZry1Zj0GQa9zVK9omutDFYwsSHFQBc-JAP68TDXFpR6Tr_zTDKger84VswJ40Vk6Cu6Qyx9SANGAwIgV1IreD7zPE66BIekI18VUDcJnQcfCNa-3iq1wrtMQCQtkb5DnYYJb3yiAAefqUgxBuEjYKrnz7skp3s_dqwYBtZ2yvQ4jjrkbF4dbPkNdvilbNdIwzXU8j_UrABmGfasKf-Dtnl6pg2vsdxgg944kDv0204Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r30
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70353" target="_blank">📅 12:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70352">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3219c52e1.mp4?token=tGzsaK-JoLb97lGE3oegdinSivhycp6wtTi2Rpo3u55SC3Uptv7ps315iF-tCtrcw4ogb52Vgt-ybBTOQilbPbjRZxiNI03qpiMnEW6j1mEcWkpxreLdjitUA_9uFY8VNJ41OAPxld57BenGjWANzFMtDS8owwJBhUqt7gDoUA0z45mcjvFmQUVclsw2okQUrXC5694pKAgq6OVm30x8OASvgFVVO8kw8jM3Bo9t61gcn8lqic0m-l-J8OFo8mAWZrcMlMdR45da86QleAM5i_Cysl9hrMTY9mHBcWHYecER2Ysz5gjYQfY-V9F_gn-YAMjbRb7e5Dk7rxE0FbbDkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3219c52e1.mp4?token=tGzsaK-JoLb97lGE3oegdinSivhycp6wtTi2Rpo3u55SC3Uptv7ps315iF-tCtrcw4ogb52Vgt-ybBTOQilbPbjRZxiNI03qpiMnEW6j1mEcWkpxreLdjitUA_9uFY8VNJ41OAPxld57BenGjWANzFMtDS8owwJBhUqt7gDoUA0z45mcjvFmQUVclsw2okQUrXC5694pKAgq6OVm30x8OASvgFVVO8kw8jM3Bo9t61gcn8lqic0m-l-J8OFo8mAWZrcMlMdR45da86QleAM5i_Cysl9hrMTY9mHBcWHYecER2Ysz5gjYQfY-V9F_gn-YAMjbRb7e5Dk7rxE0FbbDkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوه اوه اجرای بازی "نون بیار کباب ببر" بین دو نامحرم تو برنامه‌ای که مجوز وزارت‌ ارشاد رو داره!!!
همون طور که ملاحظه می‌کنید، چندين مرتبه دستِ این دو نامحرم حین بردن و آوردن نون و کباب به همدیگه برخورد کرد...
پس چیشد آرمان‌های امام؟!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70352" target="_blank">📅 12:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70351">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c0b55713.mp4?token=RXUPesqgsmEL7xEt6ZP7HO_1YaVYdsQGCfh9d7OpKxsjst0xDDzJymLXO5Sqs_NJM5WqnleZAiAxk6l6OVl9Q1N0auguSH8LA0fnQCXf0e1xQTwUmIRqsJ-K4VClyxhRhpc9Tk68QDcqSZYcQLpZXvV-NS0FBl64mOxQsSaF7Gb1biNmycysdhTN0fv8YO2WxbABR41Hgrh4JX3IMWMUtHsXL5Z8N1P5LSEIhw0VFlGmyLz2WyLA1gQAK33w710g_czwcv3zsuXGqkn532wKoK32dib9LqtJ4jjEvvz_yLTQwIOJNDO1gAoU5XQRNtBKd1Hb9KvREaq2WIsi8BOmiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c0b55713.mp4?token=RXUPesqgsmEL7xEt6ZP7HO_1YaVYdsQGCfh9d7OpKxsjst0xDDzJymLXO5Sqs_NJM5WqnleZAiAxk6l6OVl9Q1N0auguSH8LA0fnQCXf0e1xQTwUmIRqsJ-K4VClyxhRhpc9Tk68QDcqSZYcQLpZXvV-NS0FBl64mOxQsSaF7Gb1biNmycysdhTN0fv8YO2WxbABR41Hgrh4JX3IMWMUtHsXL5Z8N1P5LSEIhw0VFlGmyLz2WyLA1gQAK33w710g_czwcv3zsuXGqkn532wKoK32dib9LqtJ4jjEvvz_yLTQwIOJNDO1gAoU5XQRNtBKd1Hb9KvREaq2WIsi8BOmiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیروز تو ابهر - زنجان ، دوتا دختر نوجوون اينجوری با موتور صاف رفتن تو دلِ تریلی که پارک شده بود!
جفتشون مصدوم شدن ولی خداروشکر آسیب‌ها خیلی جدی نیست...
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70351" target="_blank">📅 11:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70350">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab8c63c27e.mp4?token=gS_mukFWyn9PJjZz-E7qhSfoQWy_zD3AvFOIFXbHPUaFJhYeTloRn6QoUumnnY1fh5CiF7b-u_RR5DA8rYTqdtLKRPpw67eP2PH8NfeVpL9CsoiqV5jH7O59pfffH9MFQF8-6-lhHOemWPJhGxgcS8M4Sx9yE73Mx6BtEaCNGYJfKZqPlNdTaxRbe380cqmB86clYPTxJtee-APtstMFTYLQGl5UjlFqVeYOkqqk-DNiycrMJAkWUHjt9bV_qsdHPBW4VHCueiTF7VXNZWgJqGll0FAKtNfhHyU4bVuKEvo_GtJKyZphSxYadpDLaddX72BKGbQp8lLWyEOAIK-kXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab8c63c27e.mp4?token=gS_mukFWyn9PJjZz-E7qhSfoQWy_zD3AvFOIFXbHPUaFJhYeTloRn6QoUumnnY1fh5CiF7b-u_RR5DA8rYTqdtLKRPpw67eP2PH8NfeVpL9CsoiqV5jH7O59pfffH9MFQF8-6-lhHOemWPJhGxgcS8M4Sx9yE73Mx6BtEaCNGYJfKZqPlNdTaxRbe380cqmB86clYPTxJtee-APtstMFTYLQGl5UjlFqVeYOkqqk-DNiycrMJAkWUHjt9bV_qsdHPBW4VHCueiTF7VXNZWgJqGll0FAKtNfhHyU4bVuKEvo_GtJKyZphSxYadpDLaddX72BKGbQp8lLWyEOAIK-kXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بعد از تبرئه پژمان جمشیدی؛
حالا دختری که مدعی شد مورد تجـاوز قرار گرفته به برنامه‌ یوتیوبی ترانه علیدوستی دعوت شده و ادعاهای خودش رو مجدد تکرار کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70350" target="_blank">📅 11:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70349">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25ab02a82.mp4?token=VEqOlbCX478SYdUzczUhzjwsAfxeDHNH2nYXzprXis7EQ8zoxtTAprmc6hpqgIbnzIAZcIr28ZZFXMVGsmJkIFtlyIqLNghkLLyqmoSolnmpYllmSaRIaNHa8NF98-B1pDyO2CcBlKx28l0d4PqF5i0cG08yKhiVD1hDxzQUOXIxPN_QF2InBoVDMsf8EbMgZX9q54LUK4ivbz3rfclu12e39Ntv_Jz9YFHpkH0Czm9ZTeXgO4qnREk2eVUtGB7_Hhcvom12rB03Cpb1CYm_Cgv0IsbgNKO5Fdh0LN-9bIVr9IsoDleSvtCC6Ol5gN5E9DUXMcZrytbWgGEdxXQc3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25ab02a82.mp4?token=VEqOlbCX478SYdUzczUhzjwsAfxeDHNH2nYXzprXis7EQ8zoxtTAprmc6hpqgIbnzIAZcIr28ZZFXMVGsmJkIFtlyIqLNghkLLyqmoSolnmpYllmSaRIaNHa8NF98-B1pDyO2CcBlKx28l0d4PqF5i0cG08yKhiVD1hDxzQUOXIxPN_QF2InBoVDMsf8EbMgZX9q54LUK4ivbz3rfclu12e39Ntv_Jz9YFHpkH0Czm9ZTeXgO4qnREk2eVUtGB7_Hhcvom12rB03Cpb1CYm_Cgv0IsbgNKO5Fdh0LN-9bIVr9IsoDleSvtCC6Ol5gN5E9DUXMcZrytbWgGEdxXQc3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
کارشناس صداوسیما درباره علی خامنه‌ای:
رهبر شهید یه پله از امام معصوم پایین تر بود هرحال هرکی نمیتونه نائب امام زمان بشه
خداوند متعال خامنه‌ای رو تو انفجار مسجد ابوذر برای ملت ایران نگه داشت
اما تو ۹ دی(منظورش ۹ اسفنده) اون همه موشک خورد به بیت آقا که خدا رهبر جدید رو به ما بخشید
اونجا هم خدا مجتبی رو از شر موشک ها نگه داشت
خدا خیلی حواسش به ما هستش اگه ما بهش حواسمون باشه
موقع جنگ رفتیم نماز با حضرت آقا یه آرامشی داشت یه جلالی داشت یه شکوهی داشت بی نظیر
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70349" target="_blank">📅 10:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70348">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced1bea644.mp4?token=fxEn2XX9QWOy5RLk7FlVMHzCBUOzX6n8u3_zLtQi3PFOFyLruiaOmA9Jf4T-uB9CyuyP0HlSHbBw9enKrn1frs_ZyYGeHVn2vIx-4ekLn1TTYJy3CUoZUPcnBJqWLVOsvrLR82dHZwoZFN0_uqlJvuI16kt_1wq8qYflp5mhMLNMkuH1xzrSMsvt8yoXNwwg89n4O700RFToeFRjhAZu7Lld1kUyiyWOAlWUW3_22ymAwpf2waL1vv8FYcnnpTrORPmSJm82vQm2MnhaFVJYZDQRsadkZO9LHNfzCbD5vIcQXMs-hDUMEftxp5lSd2bgwutraFzdgEI2FncFhmHZmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced1bea644.mp4?token=fxEn2XX9QWOy5RLk7FlVMHzCBUOzX6n8u3_zLtQi3PFOFyLruiaOmA9Jf4T-uB9CyuyP0HlSHbBw9enKrn1frs_ZyYGeHVn2vIx-4ekLn1TTYJy3CUoZUPcnBJqWLVOsvrLR82dHZwoZFN0_uqlJvuI16kt_1wq8qYflp5mhMLNMkuH1xzrSMsvt8yoXNwwg89n4O700RFToeFRjhAZu7Lld1kUyiyWOAlWUW3_22ymAwpf2waL1vv8FYcnnpTrORPmSJm82vQm2MnhaFVJYZDQRsadkZO9LHNfzCbD5vIcQXMs-hDUMEftxp5lSd2bgwutraFzdgEI2FncFhmHZmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از یه چوپان که توی پیجش منتشر کرده و میگه:
بنده مرتضی ریدم تو مملکتِ جمهوری اسلامی، ترامپ سر کیرتو میبوسم، بزن که خوب میزنی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70348" target="_blank">📅 09:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70347">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac295420e6.mp4?token=gzdeRp0o8KgScxH6q1zFIlUrSrHtATCphzRgvGgLJ4zQKsEBnMEqAtxO74KDxjtb6tmdqcHZH0Uj3XdkklVvSAAL1dSrMWoJNmuj4zZP6B_8jyvyinYO-JDnjISHJieNnee5Sw7AV2piFT35kSBffJ6NS2j-TPcPddbD_J46wW_mzOtWrk4kiG6diWMC_qii4YiNROmdWCpCCXDRChn_8SAS0RkN5LP0EiUVTvreAhAifilZkeU8H0R4zv4Ada3jRA-tgqDcUYUdqgnujORP0dICFfaezQIFGQyIjDCl5-o68HLVyiId2vvt-CB8iKlldpVqQmozNL30qJ-oYhElaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac295420e6.mp4?token=gzdeRp0o8KgScxH6q1zFIlUrSrHtATCphzRgvGgLJ4zQKsEBnMEqAtxO74KDxjtb6tmdqcHZH0Uj3XdkklVvSAAL1dSrMWoJNmuj4zZP6B_8jyvyinYO-JDnjISHJieNnee5Sw7AV2piFT35kSBffJ6NS2j-TPcPddbD_J46wW_mzOtWrk4kiG6diWMC_qii4YiNROmdWCpCCXDRChn_8SAS0RkN5LP0EiUVTvreAhAifilZkeU8H0R4zv4Ada3jRA-tgqDcUYUdqgnujORP0dICFfaezQIFGQyIjDCl5-o68HLVyiId2vvt-CB8iKlldpVqQmozNL30qJ-oYhElaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر بچه به زیباترین شکل، جواب اون مجری که گفت جنوب ایران فدای جنوب لبنان رو داد.
نسل جدید آگاه‌تر از چیزیه که فکرشو می کنید!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70347" target="_blank">📅 09:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70346">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📊
تحلیل فوتبال فقط حدس نیست؛ آمار، ترکیب، انگیزه و فرم تیم‌ها مهمه.  در کانال ما بازی‌های مهم ملی، لیگ‌ها و دوستانه‌ها رو با بررسی دقیق منتشر می‌کنیم.
🎯
انتخاب‌های پیشنهادی روی گل، BTTS و بازارهای مطمئن‌تر  عضو شو و قبل از شروع بازی‌ها، تحلیل رو ببین.
⚠️
…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70346" target="_blank">📅 00:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70345">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=NDqWbEwlE-6ajoHTRbWpjc3vzge-qvabwpZH6J8ijcmlOZLadvHYYMQk_GkjDJXyzy1hX3N3S-KRwLZpHbkO9Zrp2Ms2foDbfmhsiWctci3NqXKoCptP_ovJ0ePStiBEz9nt5G6VghR43i2wfRyxP9WSHXH23GkdGStPLBnv-Au3zZvsLgC2ONJQSQJHKferc71zdW7jGM4Ng_Ga_pl1QGzg0vuEiFyHqgasUQc_7pDH3RRmrvSkjO8cUTqx5zcJ3-_5eNc9IH4zpxNW3mOPX6TrManixeKur9RPvEh8Ba17j0FLpVEWHjoc6bAZmiGjs_VdBEFuKExWMopZpnkqBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=NDqWbEwlE-6ajoHTRbWpjc3vzge-qvabwpZH6J8ijcmlOZLadvHYYMQk_GkjDJXyzy1hX3N3S-KRwLZpHbkO9Zrp2Ms2foDbfmhsiWctci3NqXKoCptP_ovJ0ePStiBEz9nt5G6VghR43i2wfRyxP9WSHXH23GkdGStPLBnv-Au3zZvsLgC2ONJQSQJHKferc71zdW7jGM4Ng_Ga_pl1QGzg0vuEiFyHqgasUQc_7pDH3RRmrvSkjO8cUTqx5zcJ3-_5eNc9IH4zpxNW3mOPX6TrManixeKur9RPvEh8Ba17j0FLpVEWHjoc6bAZmiGjs_VdBEFuKExWMopZpnkqBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تحلیل فوتبال فقط حدس نیست؛ آمار، ترکیب، انگیزه و فرم تیم‌ها مهمه.
در کانال ما بازی‌های مهم ملی، لیگ‌ها و دوستانه‌ها رو با بررسی دقیق منتشر می‌کنیم.
🎯
انتخاب‌های پیشنهادی روی گل، BTTS و بازارهای مطمئن‌تر
عضو شو و قبل از شروع بازی‌ها، تحلیل رو ببین.
⚠️
شرط‌بندی باید با مدیریت سرمایه و مسئولیت‌پذیری باشد.
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70345" target="_blank">📅 00:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70344">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7469eeed2.mp4?token=k8AZilFUuZ8YWJ420C0dOCHeTkIYpn9sGf02IIuAZwANh8PQdaIt6MSIcJPOwb0PHKHGBPj33OykNDYciqilklydtw8auR6kFdsVu1yfqQOGXaaQEOcOjZ7eYy-XCDAhalzIKriLtHqTDeaWBw9aL4L7zrbLPRSKPkILKegaU_BAmsbsdtjoCn0XQx433Ti45riC1F3tk8VQ4OCXCMFyd7Q64JBb3tuWPPPMr4VIpVAx0BfyT5jC1YMVEsFLzAu2Sar5W7OGlk91p-V4X0VoTRuLu9gfNaSCP93Gh8E0ck0r15kmR4nl8Z7ES3qL5-siwzkzyhNNT3TffFQpwzf51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7469eeed2.mp4?token=k8AZilFUuZ8YWJ420C0dOCHeTkIYpn9sGf02IIuAZwANh8PQdaIt6MSIcJPOwb0PHKHGBPj33OykNDYciqilklydtw8auR6kFdsVu1yfqQOGXaaQEOcOjZ7eYy-XCDAhalzIKriLtHqTDeaWBw9aL4L7zrbLPRSKPkILKegaU_BAmsbsdtjoCn0XQx433Ti45riC1F3tk8VQ4OCXCMFyd7Q64JBb3tuWPPPMr4VIpVAx0BfyT5jC1YMVEsFLzAu2Sar5W7OGlk91p-V4X0VoTRuLu9gfNaSCP93Gh8E0ck0r15kmR4nl8Z7ES3qL5-siwzkzyhNNT3TffFQpwzf51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
آیت‌الله جی‌دی ونس:
تنگه هرمز اصلی ترین اهرم فشار تهران هستش
موثر ترین چیزی که فعلا داریم فشار اقتصادی هستش که به ایران اعمال کردیم
اونا هم به ما فشار اقتصادی وارد میکنن
بهترین راه راه فشار اقتصادی هس نظامی چاره ساز نبود و اونا الان زیر فشارن
ترامپ خیلی واضح گفته ایران نباید سلاح هسته‌ای داشته باشد
تاسیسات هسته‌ای اونا نابود شده ولی آیا دارن بازسازی میکنن؟؟
ما میخوایم یکاری انجام بدیم تاسیسات هسته‌ای اونا نابود بشه حتی شانس بازسازی نداشته باشه
افزایش قیمت نفت گاز تو آمریکا طبیعیه ولی به زودی پایین میاد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70344" target="_blank">📅 00:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70343">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
لحظاتی پیش صدای دو انفجار در سیریک شنیده شد.
احتمالا موشک شلیک کردن به سمت تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/70343" target="_blank">📅 23:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70342">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mon4Gfiv2fQQS6Z7L-spWPcHhB42okhAjoh00dMb4H3V_Uf7E58nbhONJmzr3vQszJ8ghtbPNOky7527SSrO6ciHCQ-QHznpaeEtyruBx3iW0KuDz-bMnxaxfMOKJ-9rg4Qu5tNREXvf6o_XFmJClyfeZGZzc9ETFJad5nLCjpxsKHiOqc1iBGbNOFamhMhUeIIOvQe59byIgDE9tgQW9J-D6_POh1DzefajWSTLM_Bvj3mKJLSd0iovEluYnBRdRmQ-XcGCc9dplb0mmFT5bqtd1qEqnfU7YuhDGBG0RQeV0jqfuBo4BMnpBAr2NPdMTkyK2MCSThMFTp3gYjQY_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
پلتفرم X زیر توییت رئیس پارلمان عراق با عنوانی جعلی برای خلیج فارس، یادآوری کرده که «خلیج فارس »درسته
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70342" target="_blank">📅 22:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70341">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264b3e2171.mp4?token=JPYpkvjRsDWIZZ_3X2sEI5rA7zJ_jtBu87RMJo8g_L2e1t09TdfVPEtNEAX0WudPTDoVAudO1idFAk8wuKUF0Zi1alimyvNMyx08ra33TqQ3zh_n4-O0ahPDUQgHJYhmwUhaRFxQJN693lZ53jJZjIJnHf2c0OZ2GIU8ckp0S41wVr5-YQsuLCl3Vc3aBasyKrm7c72-YKwz6xJOWSOXqPUhrLuSJ5kVOWvHqWrEw0xaAvq2KFM0rQpYoOx2Tyw32PqhoU7Fx9j_QUFH497CAB0CyFhuKPCyrv0YVN8VfrRFJAxrA2DXYUTe4qxX81UBop6RPJHUFGKvGVnW46687Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264b3e2171.mp4?token=JPYpkvjRsDWIZZ_3X2sEI5rA7zJ_jtBu87RMJo8g_L2e1t09TdfVPEtNEAX0WudPTDoVAudO1idFAk8wuKUF0Zi1alimyvNMyx08ra33TqQ3zh_n4-O0ahPDUQgHJYhmwUhaRFxQJN693lZ53jJZjIJnHf2c0OZ2GIU8ckp0S41wVr5-YQsuLCl3Vc3aBasyKrm7c72-YKwz6xJOWSOXqPUhrLuSJ5kVOWvHqWrEw0xaAvq2KFM0rQpYoOx2Tyw32PqhoU7Fx9j_QUFH497CAB0CyFhuKPCyrv0YVN8VfrRFJAxrA2DXYUTe4qxX81UBop6RPJHUFGKvGVnW46687Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف، اوایل تیرماه:
خودم رفتم قطر، با امیر قطر صحبت کردم و 12 میلیارد دلار از پول‌های بلوکه شده ایران، طی تفاهم‌نامه اسلام‌آباد آزاد شدن.
🇮🇷
همتی، رئیس کل بانک مرکزی، دیشب:
هیچ‌کدوم از پول‌های بلوکه شده‌ی ایران هنوز آزاد نشده و همش شایعه‌ست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70341" target="_blank">📅 21:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70340">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7FLk6U4TXak_L-t_TN_OP150iNjcOLFKs-LyVqwar4znFRjznRx6uqs2UrERnhcqy0SrOioQBuCKG3hvo9PvlONByet-YLRZYRm0aU95cNn4qO6cCAZuEchndQq2MMvFCXUfO9s9A3ePGbkMlajZkB_S_H8ZjTozBw0KzVDNp1cdFZHjlyGtGluKsx6grmc-HSTukp7UoBa2liLIfr4JrHlIxXNyxroIRugU0PLPrJds7KuGbvUT1DLsUFDfYw6OcI-YdWyoMwdInFZZRlX6ljm_BNeTkeix1NI8YwOiu2ZCKR-bYlACrXkJgdw3Xzbh1mZ9HCrM_Z8iFfl3CsXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بزرگسال‌ترین داوطلب کنکور ۱۴۰۵ با ۸۵ سال سن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/70340" target="_blank">📅 21:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70339">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7149fa402e.mp4?token=QIW0JEByvrqlaBheo2w5Wc4FxPn6oxJr67CmVPWwWgxYMr5eDm79unNn4mP6ne7zfROoUX-0nuqPFT1av7mTQnmhkv9d525KqbWZU10yNujD8xqXyq1TBUMmABfIuvqPL-pcefShHonUbiXTvLG0y-GkU-_z7rG4RhlCWrxauUQXT9vnyvFDrDuPSs1UeMDwaNWGvxt1s8DjGEXExwjCvLf6QSUzHDmgkyDZTjMhKL-v8QMDVDX0W-_5_-DIIb2BkTJaS6K9l7S9a4YpN3hn5eWGr8JqSgo4asWY7msHzhNi-55QUlZDRjPIJN6dXwzOb2GbxXlxfEAYlgGIeTRJbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7149fa402e.mp4?token=QIW0JEByvrqlaBheo2w5Wc4FxPn6oxJr67CmVPWwWgxYMr5eDm79unNn4mP6ne7zfROoUX-0nuqPFT1av7mTQnmhkv9d525KqbWZU10yNujD8xqXyq1TBUMmABfIuvqPL-pcefShHonUbiXTvLG0y-GkU-_z7rG4RhlCWrxauUQXT9vnyvFDrDuPSs1UeMDwaNWGvxt1s8DjGEXExwjCvLf6QSUzHDmgkyDZTjMhKL-v8QMDVDX0W-_5_-DIIb2BkTJaS6K9l7S9a4YpN3hn5eWGr8JqSgo4asWY7msHzhNi-55QUlZDRjPIJN6dXwzOb2GbxXlxfEAYlgGIeTRJbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شهبازی مفعول :
نوید محمدزاده یه پست گذاشت زامبی ها ریختن سرش
فحش و ناسزا و تهدید و انفالو که چی ؟ حق نداری با این زامبی ها اختلاف نظر داشته باشی
این وضعیت زامبی هاست
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70339" target="_blank">📅 20:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70338">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e91c8463bd.mp4?token=korKnjF7wOIUgkJKszaQsSNuDs34VkEWqg-IZJYCXeeP85AYelYd47nQW_7F0KrFj0rd7ym66MpsBc3Z48f0VKQCmRONoRozBP9rKWokIst9wNRKZs-cf32TV5Fq9jpfH-bLEiDNyLjjw8YZIjfSUE2uAsGHK6k9EYZnN6UPcuYB6rFOYHcPJROYJEcyKga1870qsUx7u-eEI4jCN2VpLlzjTt6IZGweB2ylQ6_aoR_WHUAVVk6YFbrAm6Md42DC8FBk3UOEox0-xRyaCu_Obc1siAeW_VpXMcUN0Jc2nTS8HBuPAO4TcmNsYEBw6bRs2aQo659F6xLDRkYJhjTLRaHiIcqeA9RVtn4mKN3b1IcjqjViEzqlZH7306Oq7kCYJFecBxeSMqcdCt7ODX7X6Si0mj5p93enh5hehw1VMQOdWpTaXH77UvcmL2u0QIRXY1ki0cVvVHT5r09qJYmIvj1zVVp7VklXS3xihH67JFa1q0IguuLPzB9sCzNskUw4rVgI-Zu_Qlg9L36vN-W0JM5NvUVzN-cFU6Y37ICI1erWWPwWY215aBtMFK_Rac0Hec9NJ_Tez5y2OWqp_0dCLNcqttXKHIfRlk8XcIwkuUCH8uuQP8-onH1QJbf4_1CE2lMLR6S_kvDZo070FEEihsCiLvmahJ2ppg4NsPKfqKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e91c8463bd.mp4?token=korKnjF7wOIUgkJKszaQsSNuDs34VkEWqg-IZJYCXeeP85AYelYd47nQW_7F0KrFj0rd7ym66MpsBc3Z48f0VKQCmRONoRozBP9rKWokIst9wNRKZs-cf32TV5Fq9jpfH-bLEiDNyLjjw8YZIjfSUE2uAsGHK6k9EYZnN6UPcuYB6rFOYHcPJROYJEcyKga1870qsUx7u-eEI4jCN2VpLlzjTt6IZGweB2ylQ6_aoR_WHUAVVk6YFbrAm6Md42DC8FBk3UOEox0-xRyaCu_Obc1siAeW_VpXMcUN0Jc2nTS8HBuPAO4TcmNsYEBw6bRs2aQo659F6xLDRkYJhjTLRaHiIcqeA9RVtn4mKN3b1IcjqjViEzqlZH7306Oq7kCYJFecBxeSMqcdCt7ODX7X6Si0mj5p93enh5hehw1VMQOdWpTaXH77UvcmL2u0QIRXY1ki0cVvVHT5r09qJYmIvj1zVVp7VklXS3xihH67JFa1q0IguuLPzB9sCzNskUw4rVgI-Zu_Qlg9L36vN-W0JM5NvUVzN-cFU6Y37ICI1erWWPwWY215aBtMFK_Rac0Hec9NJ_Tez5y2OWqp_0dCLNcqttXKHIfRlk8XcIwkuUCH8uuQP8-onH1QJbf4_1CE2lMLR6S_kvDZo070FEEihsCiLvmahJ2ppg4NsPKfqKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
این مناقشه با ایران؛ ما از آن عبور خواهیم کرد. نمی‌دانیم چه زمانی.
🎙
خبرنگار:
آیا کارزار اقتصادی علیه ایران، چین را هم شامل می‌شود؟ چرا که چین شریک اصلی اقتصادی ایران است.
🔴
بِسِنت:
بسیاری از گفتگوها بهتر است به‌صورت خصوصی انجام شوند.
🚨
🚨
⭕️
بسنت درباره ایران:
ما شدیدترین تحریم‌های تاریخ را اعمال خواهیم کرد و به شما می‌گویم که این کار نتیجه خواهد داد.
این روش در ونزوئلا، پس از آنکه دست به محاصره زدیم، مؤثر واقع شد؛
هم‌اکنون در کوبا نیز کارساز است و در مورد ایران هم نتیجه خواهد داد؛
ما این رژیم را ساقط خواهیم کرد
!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70338" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70337">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">💎
میدونستین تو ویپاری
با شارژ بالاتر از ۱۰۰ دلار ۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70337" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70336">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/70336" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g29
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70336" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70335">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47dcddfa33.mp4?token=DEy7Fm6RrT_oSCXySR5DTO-E3I5BDjj5jAxVAydy8l3QwaGtoDaTs8PWGWCkvHFhV439ix8CRr7hO9VzBqXqO3IDoiliLBFnaL7jdliUeTnFm1KEHuPyFcosKjF90Myzo_ieIEMmxXI2CeAO9NL8FDd96eo0ZxrXpz8FM9fOARqkDt7jqjk2lg7nyji9ytZre4aVAtdvOAYoNfbhm8x0TaX_ra2kFW3JzngZVo_n9rvoFVFdBwQofpTN5kjSHU_4wuAww8qx2qRAjyjlmHIOE9EP_aOAurzcl0Ekk-52yCsymwbISaEJIh-Earf8nVRwhqZgsRxj43v879jPFgKvZad6f0Mwk35hPBN_fqjdhiLv89hxKfcfkMCI-b2MbRYfIIvbSfU-cQo86IxqkOby9M1bD5pQqQoU1C2-OehTwaaxV4GGw9nmQbdANmUF1DCsvc788kaqUe4rNkO03HA1nX741fPfityLTeSxkwvK3MQ_RMaQ69sKp4jYOu6s87mAvkhxOkdq5BHh0EOwY_OdOkf_GZaxg_1OW1mjxEleeP2LUycHkSSMT23EQGfZ6yZ2uzJFVrpfznVaQ5umhY_Af-bobjgs-gLGLzWkE4MfSaecOxPyWAAp2Z9vf7AxhrWCFdic63Un0GhVg5izve3cPXEB3Q4FIAQCAYI0KLAv71g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47dcddfa33.mp4?token=DEy7Fm6RrT_oSCXySR5DTO-E3I5BDjj5jAxVAydy8l3QwaGtoDaTs8PWGWCkvHFhV439ix8CRr7hO9VzBqXqO3IDoiliLBFnaL7jdliUeTnFm1KEHuPyFcosKjF90Myzo_ieIEMmxXI2CeAO9NL8FDd96eo0ZxrXpz8FM9fOARqkDt7jqjk2lg7nyji9ytZre4aVAtdvOAYoNfbhm8x0TaX_ra2kFW3JzngZVo_n9rvoFVFdBwQofpTN5kjSHU_4wuAww8qx2qRAjyjlmHIOE9EP_aOAurzcl0Ekk-52yCsymwbISaEJIh-Earf8nVRwhqZgsRxj43v879jPFgKvZad6f0Mwk35hPBN_fqjdhiLv89hxKfcfkMCI-b2MbRYfIIvbSfU-cQo86IxqkOby9M1bD5pQqQoU1C2-OehTwaaxV4GGw9nmQbdANmUF1DCsvc788kaqUe4rNkO03HA1nX741fPfityLTeSxkwvK3MQ_RMaQ69sKp4jYOu6s87mAvkhxOkdq5BHh0EOwY_OdOkf_GZaxg_1OW1mjxEleeP2LUycHkSSMT23EQGfZ6yZ2uzJFVrpfznVaQ5umhY_Af-bobjgs-gLGLzWkE4MfSaecOxPyWAAp2Z9vf7AxhrWCFdic63Un0GhVg5izve3cPXEB3Q4FIAQCAYI0KLAv71g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از یکی زیباتر و حرفه ای تر:)
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70335" target="_blank">📅 19:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70334">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96e27ffe3.mp4?token=SJio-OBBs1v3C0Bh8la92MGtCNjIPaIujMAxKTRxErpDwqUC6No_ZPEDyKeYEGmkdVeiq7Xj-dsTc6ZzAr2s2aMoU5ou_OLy0oFu0mqfiucjG71XZS3jWUViG4Kw8pfU7AykHzQk28FQHIWGz4NDpQyhZdt3AoJtf0VKjgydbOtbX8r93ue6i0ETYhj2xsV7V_2PBkjB_4SRZyrZ4Xz5fV_Xw5G1MNbgdYYhGj6iyajMXobpqhyVhbCvvlIFMSmw_fLE0UtHmWaIpjIkHtsaH0AX2Iaqkl9OwoGZTcLIeATwPlV8c5x_-pXyyDgHIPlYa8lvI4wUhr3P_5OxKXpsfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96e27ffe3.mp4?token=SJio-OBBs1v3C0Bh8la92MGtCNjIPaIujMAxKTRxErpDwqUC6No_ZPEDyKeYEGmkdVeiq7Xj-dsTc6ZzAr2s2aMoU5ou_OLy0oFu0mqfiucjG71XZS3jWUViG4Kw8pfU7AykHzQk28FQHIWGz4NDpQyhZdt3AoJtf0VKjgydbOtbX8r93ue6i0ETYhj2xsV7V_2PBkjB_4SRZyrZ4Xz5fV_Xw5G1MNbgdYYhGj6iyajMXobpqhyVhbCvvlIFMSmw_fLE0UtHmWaIpjIkHtsaH0AX2Iaqkl9OwoGZTcLIeATwPlV8c5x_-pXyyDgHIPlYa8lvI4wUhr3P_5OxKXpsfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
یه پسر دانشجوی ۲۱ ساله آمریکایی به کمک هوش مصنوعی یه مدل اونلی فنز به اسم «مایا» درست کرده و تونسته تو یه ماه اخیر ازش ۴۳ هزار دلار(۸ میلیارد تومن) درآمد داشته باشه
مایا اصلا وجود خارجی نداره این پسر از خودش فیلم و عکس میگیره و به کمک هوش مصنوعی به دخترِ لخت تبدیلش میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70334" target="_blank">📅 18:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70333">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3764b3347.mp4?token=nPkFk8VNwcCuHhMouKdgxeplwM5InMd6G7Waig27w0Hd2hNtlLFqA58VVdGNpSgnB5w-oA8FDA4RuRzFKyM2Dd9ZzOO4NO2D36JbmSy3-lVSw0l8lGOCZyXEpv5psidL40T7exJinCIfZNYAIAR7AKu-MkNEepYx3cvsAX8VNvIVcyXLwDk64sI-Q3x5E1CQVxjXBfV9qXog8lVx83xRjGvEQkp4EB2EDNM4983YT2EVKPgGvwpYNBR20hQu769LO0Zd3XjkB18t-yFcV68nAh6gVYKjZTafL6wTIJNlGwvWRxhUOAfMYvYNeFfhhHo91EzsN2ZcTqNAhKDG1HGjxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3764b3347.mp4?token=nPkFk8VNwcCuHhMouKdgxeplwM5InMd6G7Waig27w0Hd2hNtlLFqA58VVdGNpSgnB5w-oA8FDA4RuRzFKyM2Dd9ZzOO4NO2D36JbmSy3-lVSw0l8lGOCZyXEpv5psidL40T7exJinCIfZNYAIAR7AKu-MkNEepYx3cvsAX8VNvIVcyXLwDk64sI-Q3x5E1CQVxjXBfV9qXog8lVx83xRjGvEQkp4EB2EDNM4983YT2EVKPgGvwpYNBR20hQu769LO0Zd3XjkB18t-yFcV68nAh6gVYKjZTafL6wTIJNlGwvWRxhUOAfMYvYNeFfhhHo91EzsN2ZcTqNAhKDG1HGjxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر نقش ترامپو بهتر از خودش بازی میکنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70333" target="_blank">📅 18:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70332">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed854f2c03.mp4?token=LO3uykUozTSqDvX6RLn6ohvc6Iy4AARtKEYSSaH8oPFXdBXapWiBCYcStBQe0FDgbdjmhHNkJLi7q59AjpRXFaGBndEG4j38cU9np6l6y-oyM17f9UakQz7HaXLkmjU2DUxCoeuwzLGnV0tR8BffbjcVGiiKufrBgTMSDZKjVbRIFF_yfmnEJ7mkg5nR8AkaLRGoTyKhSfXZBinUpGxqaA_f3MQ_Sq8huBtMIZsqbZEoXAzhETQuNZA0pbS2L4Gq-sBFouA9n4jxW1zzdAGFmDcLGu_cMCj4vIDe0EJvkQwbBEvYSumW_mv0KdPqLVmP6RpGzdzOCkjKkVVSJawm-gTdyLRO8XKDpWoGx3KYZwWA-h0pYPAOD92T2YSw8ZL-hPyBCgSwRvakaKhkGfMMoH8iK_1zaoZULtnpNiL9xAKbt-F41ApwplQtxUiUQ35oLh_Eoo07uPh_KoFArTTE6VEuHhtPkAIpcNGQZaCzR9mGz6R2CDAiJHxufR8hQ1DZKctnnBfZqnnb-4dTYbLaxd6PP8Qty2_oymcy8K_HuoZ5ag3PVa8EQtllvoqBwpBOwenOTnvOPw5_zU1E1fwL_whz8Z4k9zZZp9memqLGPq9G78dLkJ0HsaDGJ5RNPEWCKp-bl_Sn5dqXjc-oXYw3kTNzizIxLeHtZb_G1uvXdGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed854f2c03.mp4?token=LO3uykUozTSqDvX6RLn6ohvc6Iy4AARtKEYSSaH8oPFXdBXapWiBCYcStBQe0FDgbdjmhHNkJLi7q59AjpRXFaGBndEG4j38cU9np6l6y-oyM17f9UakQz7HaXLkmjU2DUxCoeuwzLGnV0tR8BffbjcVGiiKufrBgTMSDZKjVbRIFF_yfmnEJ7mkg5nR8AkaLRGoTyKhSfXZBinUpGxqaA_f3MQ_Sq8huBtMIZsqbZEoXAzhETQuNZA0pbS2L4Gq-sBFouA9n4jxW1zzdAGFmDcLGu_cMCj4vIDe0EJvkQwbBEvYSumW_mv0KdPqLVmP6RpGzdzOCkjKkVVSJawm-gTdyLRO8XKDpWoGx3KYZwWA-h0pYPAOD92T2YSw8ZL-hPyBCgSwRvakaKhkGfMMoH8iK_1zaoZULtnpNiL9xAKbt-F41ApwplQtxUiUQ35oLh_Eoo07uPh_KoFArTTE6VEuHhtPkAIpcNGQZaCzR9mGz6R2CDAiJHxufR8hQ1DZKctnnBfZqnnb-4dTYbLaxd6PP8Qty2_oymcy8K_HuoZ5ag3PVa8EQtllvoqBwpBOwenOTnvOPw5_zU1E1fwL_whz8Z4k9zZZp9memqLGPq9G78dLkJ0HsaDGJ5RNPEWCKp-bl_Sn5dqXjc-oXYw3kTNzizIxLeHtZb_G1uvXdGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صنعت خودرو یه جوری داره پیشرفت میکنه که چین عملا داره سفینه می سازه
:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70332" target="_blank">📅 17:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70331">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1219ed44a7.mp4?token=RlCDonicfg_KiRMw-nPZ_gw0JgcCrXAaeY1TNyrnHgxhc6kZr4Z3p3l-bwgqJiZ-wk-bOlk0vhWJDjye1zypxpXJkZ9_BSLgLk3Hm5PsRZNEkn3seyuDZBj5bvJI6KNv8glM_DlQ3ER2tg6QDs4_PAiI-D823DF3j1UcblOgmmFhkNj2IY-VBzQz9gSLyiOnm9nbLO4zlW1dYxSGsfnPPUUas9nOiITnfmoChPpsdZMgH2H3A8B7XbMjDCoHVEqei9wUdPHs-talq6uA4JzQ7nMY5OiiAJquOWTPIJtv7vHkq0BWGdF5aKY2ocD0oX02bfLr6sZB7vv0sPLh-tsjuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1219ed44a7.mp4?token=RlCDonicfg_KiRMw-nPZ_gw0JgcCrXAaeY1TNyrnHgxhc6kZr4Z3p3l-bwgqJiZ-wk-bOlk0vhWJDjye1zypxpXJkZ9_BSLgLk3Hm5PsRZNEkn3seyuDZBj5bvJI6KNv8glM_DlQ3ER2tg6QDs4_PAiI-D823DF3j1UcblOgmmFhkNj2IY-VBzQz9gSLyiOnm9nbLO4zlW1dYxSGsfnPPUUas9nOiITnfmoChPpsdZMgH2H3A8B7XbMjDCoHVEqei9wUdPHs-talq6uA4JzQ7nMY5OiiAJquOWTPIJtv7vHkq0BWGdF5aKY2ocD0oX02bfLr6sZB7vv0sPLh-tsjuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇧
🇺🇦
🇷🇺
پهپادهای تهاجمی ۱۰۰۰ کیلومتری بریتانیا، جنگ را به عمق روسیه می‌برند، مسکو به خروش آمده است
بریتانیا پهپادهای تهاجمی دوربردی را که قادر به دستیابی به ۱۰۰۰ کیلومتر هستند، در اختیار اوکراین قرار داده است، در حالی که طبق گزارش‌ها، پهپادهای ساخت بریتانیا اکنون در حملات عمیق علیه اهداف در داخل روسیه استفاده می‌شوند.
از جمله آنها می‌توان به نیان، یک پهپاد تهاجمی دقیق با موتور جت که توسط کالن لنز از شرکت BAE Systems توسعه یافته و طول بال‌های آن ۲.۹ متر است، اشاره کرد.
طبق گزارش‌ها، سایر سیستم‌های ارائه شده توسط بریتانیا برد بسیار طولانی‌تری دارند و تا حدود ۱۰۰۰ کیلومتر برد دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70331" target="_blank">📅 16:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70330">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4669764466.mp4?token=UzCeoSajlhuzXlnuIIugNRyj6ZBngxpQDP-ZbvdFh0j-xmgD1JHrQhOryHHQS05hg84VRR025OtSBzC1ccv94EFuMN1I4ITwsHc22GetDUJkCgJROn1ccMRPGgfHnfrlNki0ikya2U-6o-WF-baLGd_oUu_1t_tpWUdo9sQGZXzwUc84_Rkdo4H0d0ewSQCIHTCQKavDfDSE3RiJu02olKDRvGsZhohGC6ojIxKKHFHC5TyF_RFUvvBzXrGdFsjbmP_2npcW2ckVek9DOCevKtWt2fo7xh4SocPrexe9B01MCEfeGRRCqfLeP9lNC_TFNEM_17Nypeb9kpIcKApCkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4669764466.mp4?token=UzCeoSajlhuzXlnuIIugNRyj6ZBngxpQDP-ZbvdFh0j-xmgD1JHrQhOryHHQS05hg84VRR025OtSBzC1ccv94EFuMN1I4ITwsHc22GetDUJkCgJROn1ccMRPGgfHnfrlNki0ikya2U-6o-WF-baLGd_oUu_1t_tpWUdo9sQGZXzwUc84_Rkdo4H0d0ewSQCIHTCQKavDfDSE3RiJu02olKDRvGsZhohGC6ojIxKKHFHC5TyF_RFUvvBzXrGdFsjbmP_2npcW2ckVek9DOCevKtWt2fo7xh4SocPrexe9B01MCEfeGRRCqfLeP9lNC_TFNEM_17Nypeb9kpIcKApCkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
جوابتون به صحبتای ترامپ درباره تنگه هرمز چیه؟
🇮🇷
حداد عادل:
باید بگیم تنگه، تنگه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70330" target="_blank">📅 16:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70329">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sejZz5a4pu4Xo5YaeaNMyxwkpEqZ8GMN86KGtt1zzBjcl9Z4DRhGMCnlegjXPQfGxY4pK3GHjKzQs3VIw1HG6NLz_SaeSGrB3xAjjYxDng1JT1mKeFbQXcKx2oua7V7wJiX4hx9H2vjea7NcDQOPkQF7SLr0clvU4eMg9Ukck9Dn6gxGY7SFK3lZWLsHQOAbrJSvNhIFhf_uNTRTGdo01TbVa7tgWHVkchEbViXlXGCqk_XxViEa7uv4p0mLBwH1ayrNWdxgd2K06Jz_Y0G6S6mDXChJ9K0OoeBzdOMyr6hqBmI8vXUwP_IHEuJdR5H_pRyy1GpW-qRzcpRDifSeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
〰️
فرماندهی مرکزی ایالات متحده (سنتکام):ناوهواپیمابر جورج واشنگتن به منطقه عملیاتی سنت‌کام رسید.
ملوانان آمریکایی در تاریخ ۲۰ آگوست، همزمان با عبور ناو هواپیمابر جورج واشنگتن (CVN ۷۳)، بر روی عرشه پرواز آن کار می‌کنند. گروه ضربت ناو هواپیمابر جورج واشنگتن پس از ورود به صحنه فرماندهی مرکزی آمریکا (CENTCOM) دیروز، طبق برنامه در خاورمیانه فعالیت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70329" target="_blank">📅 15:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70328">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85771a2a65.mp4?token=gGhniXyoy8ASqb_Dw66B94XfsmwMkDolabo5p4DZMMAZKsXDZfzMmY0Zj645FDfyKUWeD0PZAZvtvOX96lx5RMuiwb-X3lr8JJXKvOWVBXSSB0io8VRPSPmH-izGnUGWWlGvcHQFhhe3IS64WaH9MZQ_pW2bhg6oPcd0JXrchuM4cO2hWXqUuA5pLyAt6nHuL6QIia1RcAMEDbQbPuWxqwurELrot57aZf76-NWvPeZ7HXOAL7ggAaeDrt9pjA5V3K1knjBvqyRlOx8daOJ-6foecRsJL1QV1-czsfr-BQNv8-EbxoSUlDgSOj_emrOgpTrPQAU7VT2o35ews2GGbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85771a2a65.mp4?token=gGhniXyoy8ASqb_Dw66B94XfsmwMkDolabo5p4DZMMAZKsXDZfzMmY0Zj645FDfyKUWeD0PZAZvtvOX96lx5RMuiwb-X3lr8JJXKvOWVBXSSB0io8VRPSPmH-izGnUGWWlGvcHQFhhe3IS64WaH9MZQ_pW2bhg6oPcd0JXrchuM4cO2hWXqUuA5pLyAt6nHuL6QIia1RcAMEDbQbPuWxqwurELrot57aZf76-NWvPeZ7HXOAL7ggAaeDrt9pjA5V3K1knjBvqyRlOx8daOJ-6foecRsJL1QV1-czsfr-BQNv8-EbxoSUlDgSOj_emrOgpTrPQAU7VT2o35ews2GGbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
‏همتی رئیس کل بانک مرکزی:
یکی از مسئولین رده بالا که نمی توانم اسمش را ببرم، چون ممکن است ناراحت شود در سفر خارجی به من گفت که آمریکایی ها فکر کردند ایران هم مثل ونزوئلا یا کشورهای آمریکای لاتین یا جاهای دیگر است.
ایشان به من گفت که شما در آینده نزدیک نقش جمهوری اسلامی را در منطقه خواهید دید، خواهیم دید که در واقع آن چیزی که آنها فکر می‌کردند نشد و یک چیز خلاف آن، عظمت ایران را خواهند دید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70328" target="_blank">📅 15:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70326">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d602fb7461.mp4?token=DiEq_Wg_QKEdzInBMNP_QZ1sa56YwWjqud48cScwGVLAqntMJfPQQvq6qIiPGfcO9GpFLKzlV0wJYSP5S-YQM2PionrjTt-HRJF5EgTSZZHNg9OSs9n8ZLrVhH1KXRT8P53tglcMr4-4_bHT15OutjRlKmRtkZuiMpsfj9VZSdioTvsXxdSIawpz5uz2JuTGY4i7B_I8-Q4sJeiXl_ZLTrx6LRf7lu0z4ZZeeQTB91nQG3tJ6R3h_wyqnnNeH2IkV1MGkTLU0GrobYfP9Y6IuDSnIkEHFD30QtlsxaZE9CWZR4df9RLkW9gJR8_LoWqeYV1pFr6Ze4RZWRd8iQ8N0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d602fb7461.mp4?token=DiEq_Wg_QKEdzInBMNP_QZ1sa56YwWjqud48cScwGVLAqntMJfPQQvq6qIiPGfcO9GpFLKzlV0wJYSP5S-YQM2PionrjTt-HRJF5EgTSZZHNg9OSs9n8ZLrVhH1KXRT8P53tglcMr4-4_bHT15OutjRlKmRtkZuiMpsfj9VZSdioTvsXxdSIawpz5uz2JuTGY4i7B_I8-Q4sJeiXl_ZLTrx6LRf7lu0z4ZZeeQTB91nQG3tJ6R3h_wyqnnNeH2IkV1MGkTLU0GrobYfP9Y6IuDSnIkEHFD30QtlsxaZE9CWZR4df9RLkW9gJR8_LoWqeYV1pFr6Ze4RZWRd8iQ8N0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🤖
در جریان «کنفرانس جهانی رباتیک» در پکن، بر اثر نقص فنی در کنترل‌کننده‌های از راه دور، عملکرد برخی ربات‌ها مختل شد و از کنترل خارج شدند
😁
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70326" target="_blank">📅 14:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70322">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTQ1A3gB3HnObyXtLzo0GMTCSN77qQNaJ-4_H3TFDGTbbChgQbPcMbyqzQhNZAyGqKFPdgYGC1j_eg5cKzhscDbO3JmJA7e3MZrcDPgUUmsnmyjk-aKmq1yLkc1F9-LyjsIsHvIBaul1htiqxTfUXqBwnp9Bzp255L35GK3_owL1zb-uru2lqsVCzAbBQl4Eg73WJ2s0-uSE9IOZbCxRLqEuvHivQdaMlBHdLZcYKGLWnEKB5XsPBRIhzJmUaAbVWZML1zFREJrH4r88ThL-Wjir-pEHntZKdOeeyzaXz6F8VSNFF4YPmAuDa2hhTdgLmW2xAgE3cmMiH0fQL9yZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9d122dfe.mov?token=VQKF4Etu8eimPG0tJaJCa7hNgb7klRTvHnl80EH-z0IHOmRb7Q_pnoq7QsesfVfK4YoskmkTFaihffATaZDwUlr-Fd87Ck_Bu16wsmUF-6-BO6eiWwaKV5zAGlrk0tjZ9zw5o4BhR9EppbhAyiwlRoYQdz0M2Dnj9vrTeZxUFefn6PHzD0SnbGgayohtyjiCh-X7x5lbjEnm_xKAlGyeZK1Ajy4ZBMg87tFdrds7RnDNvZGIKonelaxwHY2L-9gJjV5dCiV-hJbxeswW7wAEmlhuSaYvjEsoGwpYMb6QSgEI3A4Oxu6Nu3UQptuYzUsrUh6OuZXs_o_f9KJw8Q8ZyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9d122dfe.mov?token=VQKF4Etu8eimPG0tJaJCa7hNgb7klRTvHnl80EH-z0IHOmRb7Q_pnoq7QsesfVfK4YoskmkTFaihffATaZDwUlr-Fd87Ck_Bu16wsmUF-6-BO6eiWwaKV5zAGlrk0tjZ9zw5o4BhR9EppbhAyiwlRoYQdz0M2Dnj9vrTeZxUFefn6PHzD0SnbGgayohtyjiCh-X7x5lbjEnm_xKAlGyeZK1Ajy4ZBMg87tFdrds7RnDNvZGIKonelaxwHY2L-9gJjV5dCiV-hJbxeswW7wAEmlhuSaYvjEsoGwpYMb6QSgEI3A4Oxu6Nu3UQptuYzUsrUh6OuZXs_o_f9KJw8Q8ZyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حمله موشکی شب گذشته روسیه به کی‌یف منجر به کشته شدن شش نفر و زخمی شدن ۳۳ نفر دیگر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70322" target="_blank">📅 13:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70321">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXvj2D2BtALyJi5dxaTibU_ZgvLNFpOzmTju8xsjOI4_ieH7yYUTsC9rf2pWgkYvuhpmzZjL3KElgqBvi2amlFmRFrG9KjDla6_1xvlmH6idHQsTeFVp0TTSchTixcmX98RbhRbZqD40QlytNetw34G87GQGWiny4dy35dGg_5qmsleC7W-NFy1WDu_ZtUocsurYZ2aKiAae7TrvC4q9l7FEQ8ITkDuxNwCFYpGWtXZXTVLHSPeCjGy3SQMuk4Osu7ZFOHFDmHq6JMwogoFquy_sRgprS3RmksdrQfzKKw8iaaOwgl4en1jgSTEcXNd3E_lamP7D3VTTO3FDDqWocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ابراهیم عزیزی:
ما تمام تحرکات شما را زیر نظر داریم. هرگونه اشتباه یا محاسبات غلطِ دیگر، پیامدهایی به‌مراتب سنگین‌تر از گذشته در پی خواهد داشت.
پیش از آنکه دیر شود، فوراً به حضور خود در منطقه پایان دهید و نظم منطقه‌ای جدید ایران را بپذیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70321" target="_blank">📅 13:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70320">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70320" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70320" target="_blank">📅 13:14 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
