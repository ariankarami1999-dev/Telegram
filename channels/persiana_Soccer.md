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
<img src="https://cdn4.telesco.pe/file/JrsEPndXhLSjgYLqJVYtMPs8BKmyyFw6I7YufMwrAmGr0ltk2v91X0R6QEfJP_UaeGn28zUvMlTG0FUF_mH5St4Y4_fYF5xAISMptj1K59NCaCBeUCYIObIal48mL2bcQGyHXLZ_1sJzera8WgmnXupcWYiHwXsoxntCvG2JyyeAIP4oURvC4rqelfBpsMBacRGGXHbuqFnpFfrbQPSEIKAFhtGdilZ8gAFX-EPz-jQUWrHzICM1lYnfobjsc-6_CW5WvkYHpqLqWU6o7R8VHwUJAIbNOtQUKPSjRdu67mw0tu53ahnVKrK2IO8_APifon-X93ujEtC7H1BBwdGFmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 172K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 08:32:57</div>
<hr>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcIZKiInmeKjbz7gucWvpbmiH-8Jm1qXw_c5t7QROBxAg02RiFwLoR6yQL9qwYWtKPmXgs2AMDjYbjQzjvU-QgwWpyMtr03k6tptKbzXRMdFLI0gXi1vQMzsHunH8V5IvOecny5d-plp_J6YofntItmxTZdh9ynoIy6zCioFiZV8X-80M8RvMm5rCmtEYykH9Ucaqlz7s4AheKzZn6iS4LmlKDe4G-e2HVmDVcAZ2rGPfLJtnzmEwsMfZolF74anuO462lVFwDgoAVszKlmJ7lmf60o0YUE-9BpG6opaXrM4-QpqQEyHyoX65hOgs8XzDcK1F_tAYykYX4jDDamBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
تقابل شاگردان کارلتو با مصری‌ها و جدال یاران مسی برابر هندوراس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/22914" target="_blank">📅 01:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_cGA5EC6fNsiEC6Qt-xtpJczXqgLl8Lnx6RdJyKz4MnkXVWkSCaEXKM7EVEWs9jJ0osaSIxqXaTnlWSzmKlrON8p3NO6fIhgCgIjT_F4Qgs2ENSbz6hyFRmmMBgpivZZT8MPTuGkiGGgsOjXqLfIPYNwqeB-qaLI6Vs-jy2sEi35_z7YYhXnje-aJ1DRw7vkORdCuIzM3oRmsK7yWE2SaiAC-wvXzYRU_VOeVJNM7eM688R5AZo-Y72eYybcOqJcVSMygucWGIK3IVYQxKqlROcnsg7b4Siin6BYt96LfX3_aoMYPIqn-NAdAFeSrDVdkqbfD12T5qw2Q62z1qllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از بردپرگل بلژیکی‌ها مقابل تونس تا برتری تیم ملی پرتغال برابر شیلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22913" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvLLkO536MxvJoQ7KU1-KR4WS0P02LRidK6-ZYsBtsgBCJhqzJftDuuasfmZFnYate8GFC39tMDkOkTe60w7SwT0iCZvgUizLVue9KWqMKvUy391C3xyLD-9mTqrZeVBYAU6PU_XhrlKbY5aIwTY4X9koGNvWketwRmYd6Dy_2WL9UH1mnmgrYQS6gWkl0ptu8KOrlnGgR1Hqh4PxDinbXnRFg9F3pXM2_7_B6xV-ur_9d748Bn7me6r0JoKr9Wsv043HX8wcztNsNtESJil_ZM7yT1WKRpqfIbr0-mVp9aP43Zser5cAtAQOE7IZyfYpt_CCB0RTleT9cSHwP5Xnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/22912" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=gVWPXJSDehIUvFzo66Z1Ik3gjlSeHz6H6tpScPffSNJuyo-3yNi5Y7f4cQVLZ73VyEZWd6AXl1Gzfc6rCRAcAYGF2o25xZeYmFKW2RoLi5lZYpU040PZJOL6a5hajYKtf51R1yPSlZCpFSB0DtTqO-ojD5eiLHzg7VdRXo4DrtaaLNeM0ej_YcQjTfQYllcUkO4lSijhnWzT7JjaO8s2hPQFgpH8vP2qSvRMp_2iStLt0nD9eCfqa2_fgh6OxzDy2DwP39tQBKQFhD07RB9Acm3RoxFHgmT1AZfT56-kXGUq_u2Z0ebzpSPQzu8HGqh3pkge34UID06mQhIwuCoDdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=gVWPXJSDehIUvFzo66Z1Ik3gjlSeHz6H6tpScPffSNJuyo-3yNi5Y7f4cQVLZ73VyEZWd6AXl1Gzfc6rCRAcAYGF2o25xZeYmFKW2RoLi5lZYpU040PZJOL6a5hajYKtf51R1yPSlZCpFSB0DtTqO-ojD5eiLHzg7VdRXo4DrtaaLNeM0ej_YcQjTfQYllcUkO4lSijhnWzT7JjaO8s2hPQFgpH8vP2qSvRMp_2iStLt0nD9eCfqa2_fgh6OxzDy2DwP39tQBKQFhD07RB9Acm3RoxFHgmT1AZfT56-kXGUq_u2Z0ebzpSPQzu8HGqh3pkge34UID06mQhIwuCoDdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت شدید مهاجم صنعت نفت؛ ویدیویی که روزتونو میسازه؛ فقط کامنت‌ها رو بخونید
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/22911" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=EyT_SoeODX6M9dbgPDppUXaIuIMiPvEJAdDf8g60eJ2NHInNJ1oV9W-xJ3GBWNI9hE6NnIrQL7Pss2mItcrTWfhXd-dxUgC8uq4l6n7oA8LQLW47cfSztJkEySynMyD2EKw5-YmVqZKZjTMFr0We-AK6wH1syTlV3BGjvTuDfK-IkosjQImpl-5_QiVQ-1nIuJrmnF-aj0b-KIUphqB2QR91IHBAzm_jQuHn67g2ZB4rGEsNmJnvIvAg9l7h5q2-XnHIELyYqqQ1Iwjt0g-3H3ZoApJy8xDovXgf-pCjKfeCH9l9oKq06qHI70ArlOz-fneDCQjg9zvfqOUCM7M1Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=EyT_SoeODX6M9dbgPDppUXaIuIMiPvEJAdDf8g60eJ2NHInNJ1oV9W-xJ3GBWNI9hE6NnIrQL7Pss2mItcrTWfhXd-dxUgC8uq4l6n7oA8LQLW47cfSztJkEySynMyD2EKw5-YmVqZKZjTMFr0We-AK6wH1syTlV3BGjvTuDfK-IkosjQImpl-5_QiVQ-1nIuJrmnF-aj0b-KIUphqB2QR91IHBAzm_jQuHn67g2ZB4rGEsNmJnvIvAg9l7h5q2-XnHIELyYqqQ1Iwjt0g-3H3ZoApJy8xDovXgf-pCjKfeCH9l9oKq06qHI70ArlOz-fneDCQjg9zvfqOUCM7M1Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
امباپه27سالش‌شده؛هالند 25، اولیسه امسال وارد 25 سالگی میشه. اینم لیونل مسیه در 25 سالگی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/22910" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22908">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sC4koS21ZBv-LAdE1aLVbWjQOm4y-6D1U8jz7W-9aHS55iGfSsEhuFOuyKZolARqbXuCVcBgLI5HhSg4eVRB7EO9TKjm2yvogMCwbvT6ml-hCr1iHkb7f2zoNCBzWdj4anzURSiRKcAtXN-7W4_xXVy_sODNWUVMFp4HTkS-YcK562VDlCHpzvOiBHOnL5A0AHKtKIcmQDoHGapUMXyja76JvVAlFKQIaz-rfvaox7-yABd7wgP8B9ds1WagbxxTCGeew0yUjws2uR182tVJLFDuLjMVqGSBG4vOqmA8rUkST00BddEG5UX0pNbI7VAiDOp3RApF1uCOz6RIq-MUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
توم‌میخوای‌از مسابقات جام جهانی فوتبال پول دربیاری
؟
🥇
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش بینی جام جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون e16:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/22908" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=kiRhr7cs0u-e-IypNX1shV8rmJxEoiMVlu_-ufdXLUg6o-nPnEIK4zzEmcFyFU5IDZfr2pC8eH6Xsw_UuKiDKNcN_tT-wAvodlUSIyBQa3krmccOp575wO6RIdAt-1aQTZVm2nXbpPO9-ZPxKaFhT67V3J49wJcTAbKheOPlhtBC5k3MYRH_1d2zNOW4R2jGateKFZWp3rfALnpDrJRXXOEjYRjuP4bTwJzqD0hTAXjL3lllJmWFvC1yHJ591DuTJGyxWAIXigNTvl07jur3NsbJMP_uA3qTU48qdyzZcGh4IB52G5ZIWPQcFUjP-JK_ohm5BemB9woVWJ3wNeovEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=kiRhr7cs0u-e-IypNX1shV8rmJxEoiMVlu_-ufdXLUg6o-nPnEIK4zzEmcFyFU5IDZfr2pC8eH6Xsw_UuKiDKNcN_tT-wAvodlUSIyBQa3krmccOp575wO6RIdAt-1aQTZVm2nXbpPO9-ZPxKaFhT67V3J49wJcTAbKheOPlhtBC5k3MYRH_1d2zNOW4R2jGateKFZWp3rfALnpDrJRXXOEjYRjuP4bTwJzqD0hTAXjL3lllJmWFvC1yHJ591DuTJGyxWAIXigNTvl07jur3NsbJMP_uA3qTU48qdyzZcGh4IB52G5ZIWPQcFUjP-JK_ohm5BemB9woVWJ3wNeovEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی‌داماد مجلس خیلی فوتبالیه، کریس رونالدو فن هست و به‌هیچ‌وجه هم اضطراب اجتماعی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/22907" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=vB0eRPgWDTtQyXCebQ2haugYCsxpxihIl9YHmM6zlHaB3f9qg7IiPakKLLy8VD8JsfOLltFq3IAglr5PDo_GOBLGOi2oONKG-QF3Eoc32a5YpmlQrcI0jQGBON4TmCpqqtwEcQbxVIunDo5GZJeY5snhZrhAsfDWOxK5jONdwh2QS2LjbV1kYbFYWp6v4CO5CipT5-UMXS1HzSSnxbv0KXoI9rmV6B2w0sdHOTBGB7yq3c2QD6fOO_S7ID_KZ6gEEHKG6YSxlt7RvARCIzxI6UDtaA5htf6WTtN5M4N5LIL5O5Z7faH67REwVIOlMXqwaqbJ9CLHsrAn-9XZEwM8hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=vB0eRPgWDTtQyXCebQ2haugYCsxpxihIl9YHmM6zlHaB3f9qg7IiPakKLLy8VD8JsfOLltFq3IAglr5PDo_GOBLGOi2oONKG-QF3Eoc32a5YpmlQrcI0jQGBON4TmCpqqtwEcQbxVIunDo5GZJeY5snhZrhAsfDWOxK5jONdwh2QS2LjbV1kYbFYWp6v4CO5CipT5-UMXS1HzSSnxbv0KXoI9rmV6B2w0sdHOTBGB7yq3c2QD6fOO_S7ID_KZ6gEEHKG6YSxlt7RvARCIzxI6UDtaA5htf6WTtN5M4N5LIL5O5Z7faH67REwVIOlMXqwaqbJ9CLHsrAn-9XZEwM8hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtB1zB68hpxpTBnZKUp5x-vIzcV16x-5mY0ZkcapYPDOAqPC3rkj17NI9WhOKupnFt2we3wSseISKmfQIgnUQ89u2MMvY94wYOFwSjMj0zMWc5YuQQ11mRzhpH975mI473nyZz1NbYx2I3dbDicPNO963_-zlxGjp1WcDmmBtdu7iO1qDmRcVK35Gl1u5VbD563aHPS8IXcXaoKkoLEWEhQiwXbtc8QtwftbPpjF65kNcjENzfa4Kg4sbPV_GrVXs28-qy-uZw0MJlrKkrLE9k7oJraNQGZyLK1s6u_MTxikNKl--TVDwii5hZeaolf7aipYKoe5pOC7bJHJhFtjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
#تکمیلی؛خوزه‌فلیکس دیاز: مایکل اولیسه از طریق‌نماینده‌اش‌به‌مدیران بایرن مونیخ اعلام کرده که بعداز جام جهانی 2026 تمایلی به ماندن در آلیانز آرنا نداره و قصد داره راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22905" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7O4ED3dK706BpzIKC5oRiik3YNibmNFsiqwCTfpfm5z1fuRmcLhdBdLHBD9cxlzgwqHm-mOU2X8vHL4ZZACgLjbLxbzu3e8_dSGYlf2NWZIDxP3xALUWuJ7picSkqDaFAYAEXtYTyhxSkEJFGUFB254lx0OpPXgYlkzly7xfIS2cV2IIpPntYSFnZsO36F2-pVXG8JbPu6fbo_vrtrrqDhODVPvK7V_z9iL2dUhnCYSULGYYdWUoGZHSsGsUISuw_F_D4_d93js7WYozU6375ZXTL15mDxpbVMxoS4QW2o1VW_xeLISisiwT1KQkCEckducJYIPj_nRNuC7Cxt0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق گفته رسانه ها؛ یوتیوب بزودی طی روزهای آینده بطورکامل رفع فیلتر خواهد شد و همین الانشم روبعضی اپراتورها مثل مخابرات رفع فیلتر شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22904" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsTp3zPjiS3VyQvtgOBj5NLyIZZ7QRA2dgmk2lakvx2HQuS484AnF-p43pBc3tlNZyrlAmyYmpm1jDByRmtj9ImxJ_KMH3uby33g659ZwxxNvrw4d9Hdv5fKC2s7Nxgn-AtsYV-ThyiI1zOEgb5oukzpINyuEof_FKscekM_tMhSkSnM-OvAjE8PYX9dDBStTair7ObE2NhbDpL0rczi3mFMLHLobqP3Ff79ArB-DYr_YIqqtWVJRy37gTGrEM-9yKL-xv_DFU6oTYUd1usp3cfFrQolh1j1_fPgMmA0zuxjaXJX4FVVKC4VoDlio7dJkgtgCZUBAghkGnWFw0xTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌اخباردریافتی‌رسانه پرشیانا
؛ ریکاردو آلوز ستاره پرتغالی سپاهان که با شروع فصل جدید چهار ماه از همراهی طلایی پوشان محروم خواهد بود به مدیران این باشگاه اعلام کرده درصورتی که محرومیت او لغو نشود یا به حالت تعلیقی در نیاید قید حضور در فوتبال ایران رو خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22903" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhsJtp8HlHJ2ayvkDCnPaLqnzk_MHpLPjJNujYbIiRDJPcPpiAQ8yW_HCvDDRSNxgP9MsMXKpZPoygZqNM6KndasVVFSXT01jHY9yeFOGk8DexVZV-LvzGvwXOHv7BOxqkAMK4yYKQwNaXwoU9CYtEFjifjTVcx47zyjyJtqJd3_wGNvzoRTolxwsujrteXVXhz-g9GaAg9yWEJnkhQKfTzAJnVD8s8Jm0XUYxxvqD__hPpsKJK3lb3eJl3LVsg_N_5ALsGZGdr5gD6PR0kDBq1PGKDHtaW1Pj0yHS-fLjSZlWDyB7oelgnUD_-zbC7Hu_K6NmGf640PA84qnUfQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22902" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBfsvKoly6_bLn28_7FiU2WZCEzBKrRzr29k6HoMkNjQDUcrpsM_xG5kMFkCs55BrocHlF-BlGW5MQX4HmJn239q7nNWG82GGvrevsCpYeMz4leZgdZGepXnJhtGAbZUyvzqo9-Qg8B_5y1PuArYukdOEGK-vmzMTg3rHDH9PS09t1G7qpFyDm-KuFITNUJrIvwfnw8Ar8Nv3U3ybTk2RRitXWnWr2juG3M7PSDsdqRkdC975wiHItBEetgY3NaDcn9JyviKLHDpk6ULfpYOwY0qxSauzqVZB0rOiA6EzYK5S6Yr5ekH8caZuOUdLZk8F93_GvtENBZANtfjO9JYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7PQgrnq4H4LpvVi6UB4i3nHDdE3H0Fff2htHfgdngA8HpVi6C0zzMtwE35EM9nKLZA9q0RA6kF_FV4gatX4QMlDg4Rdgj6kCTEBnPKcGUI7_kkOleClRCWaZSGPCbrdGhCYbqMxHnyqGMAxf_mIZsxolRNP_n5cYmUs0hKXFpTZZ2V0en9FEazpJ1C7RI4WUrQC1NObH3sZoQdVxIbh408i5zPHLgIXzxo_-WYCBS7PQVyvEoihTW2r5YODe3tx5wrOAYl6edpotJqGHaUxuaiFyZigxwqdaKuI09tTRJTijxQqzOBa5urdFHDYAXmjizLX3NMoLC-gHdCMqWMmzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار
؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.
مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی نسبتا جالبی را پیش‌ بینی کرده: تیم ملی برزیل در مرحله یک‌شانزدهم نهایی توسط ژاپن حذف میشه، آرژانتین تنها نماینده آمریکای جنوبی در ¼ نهایی خواهد بود و در آن مرحله مقابل پرتغال‌میخوره و در نهایت‌ فینال بین هلند - پرتغال برگزار شده و تیم ملی هلند نیز قهرمان می‌شود. البته این فقط یک پیش‌بینی آماریه و تضمینی برای رخ دادن قطعی آن وجود ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22900" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBSAeiqmRDWubKHCtpghixLQIz_veQ4FEuccDxi4Y8rfgiCXcsJvrd07LrQkC1BdowBN4Ube28re3Rlc7ddRml4gCBb3Y1zomIH4e_0PrDk68A--yi3Fk5ABmb-VjlyxdZ_MTHhKun291k6uoKs-EMvKtA9aQVCh1EMxLXNXKfZHAqhqlsJU6HRw6x_5IvzD9GxYCDkpz1szYNO2enrbbczSI2mbFS8JbcpxY_0lDXbiwKomscqp_1A_2UFCyNzEf1Ey5atQGJ-hnPsG3Up772wFj3Cwdh81CirJQAwRqeXv33SncwnJ0Om_7G-dQ3h4e51PetYTrfa2m2Tnn06i5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22899" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDcjEtjTflPuTBoFKo6EBeWO7_TDG5NDKK8kglSccSpxIfoU6OsQXHrC5roEPlFK8kNmUOYvAulwQTO9mRdnO-R59_JG9DT_GZMPlyXEu_nXPG4skK-a9aZ3rgGqumnUaCpbgeos4P8-vbDbPu2RlAIRTy8qekdM0t-G3EaEh6QCkiOxJQWCCAQuDrQ05-ukdOi-_fydUymF7wk0dIgOc78SUlhdTHp8OlyXJnxdBQUcONUzBTgB429GwgIQuoOw1SVCmHFR2_W4URRZvlorkqu_HzW46qK8d_p0t7wda65ZKAgVh4VKDJnhWtHVM3dfjTXbxwnwqP85LT9OvKp6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال با فروش جوئل کوجو به تیم نفتچی ازبکستان‌موافقت‌کرده و بزودی این انتقال‌ صورت میگیره و کوجو رسما از استقلال‌جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22898" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73008adba.mp4?token=HPpqGv9dfLr8jZEtAEVtpRREXZOfaTlpcpZFOSxc0UZD-y9qj23ITq-pUJht9A7az6j2JadjgawJCQ-JVHDeJZFnbSZAJpasVzWbqUXsxbE_NBxWR9k-xlSGwMb3G8QPnH3fCc2UIkpPI5wRj5P2LLI6_L3XzDTon5yPrZDvRJgV8qQJpTroP-dK5bGs0bZvSlcOm6V9QNsmsSGEmuuuRTZhfuL8IcUHflW_zHBCIBswfN0g6Ms8UaO2A1hGSY7BoLQ2nCUNHB5jjYjG0CHzTbvY4qPKIXEx77r78y-zvhlWCb3n8mm2eIFztppsC8iFNU1lTZWR5oPS-U7xq-l4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73008adba.mp4?token=HPpqGv9dfLr8jZEtAEVtpRREXZOfaTlpcpZFOSxc0UZD-y9qj23ITq-pUJht9A7az6j2JadjgawJCQ-JVHDeJZFnbSZAJpasVzWbqUXsxbE_NBxWR9k-xlSGwMb3G8QPnH3fCc2UIkpPI5wRj5P2LLI6_L3XzDTon5yPrZDvRJgV8qQJpTroP-dK5bGs0bZvSlcOm6V9QNsmsSGEmuuuRTZhfuL8IcUHflW_zHBCIBswfN0g6Ms8UaO2A1hGSY7BoLQ2nCUNHB5jjYjG0CHzTbvY4qPKIXEx77r78y-zvhlWCb3n8mm2eIFztppsC8iFNU1lTZWR5oPS-U7xq-l4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیکه‌مسی شخصیت‌منفی بود؛
آرژانتین ـ هلند؛ یک چهارم نهایی‌جام‌جهانی 2022. درگیری بین بازیکنا به حدی زیاد بود که به نیمکت دو تیم کشیده شده بود و این موضوع باعث‌شد مسی به قدری عصبی‌شه که یه نسخه از خودشو نشون بده که کسی تاحالا ندیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22897" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22896">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf6OgrGAcmvvPWlJQ9e9F5BQBwRnMAD9FCqjle_2fWKFfc466KZtBmn8HmACbLWTKsD_yD9hpWYP-3LzwonXPVpmo5D10PvBfykAj2xHfYBJYk0xcjccX-inEmDW85s9edWeYWZSmh44ATjuhWkj2DrG6IdTIuyvOWbaCxx1Cb46OdbiJcXZdP8AMECdzdA3UOYnsEgpwxNcgV3TQWC1DH4UDgVKA26NVqU3wXinWjA2q9ilw27WML5SpBb-_qy0HGlMge_EcuNI-lZfX7QxSTK8AfVn6NbfORb3woPlXPCJD8yktGGI38o9vBm9cETiwUtWTwAb-R1p3tX_kX-DTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید باکارت‌بانکی ایران انواع ووچر و همچین‌انواع‌ارزهای‌رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
16
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22896" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOBQ7IFImwswuiMZKWw6SQLoFj2a8hD2TqnCvVZ_VEdF6K3e-iGDwtJYEMevV8DWcJlSeb9bvaxhnFS-Vvps3gwUkvueUaCEIH_EcYtJvJtuW39F7aUiaT9FNjKp8-VM4BNPRv9Y4IAoYuXrU041rRnvQ_aQLQdeDyhoZnxFly6bZSEsesd6JZtogvQZBy1ZHpFW0-tWqlJFTiflr1yxDTikSyft7ivGZ1GCc7_51c2AS6O1I36I67t1-6FjO7NptpfYr6SENI0_YAWjocpVMZ97FGQIzDtnTfQbOFbv1QCqQGmI-EeWOkpkg8n3b5wo6NUbZmpAUK8KlDT1gQMQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22895" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=rZJtu3SmfnjKL4U6qf8tUic1A4txOYsOTwMWZLAgW9IqI2GjV1tWSOQY8S5nnGQqQJtiR1bJq5ySNEAwfk6WzaQWXTV0KU1wt6WdpvYTeqWltxU6QDBaf7elAVpqqnivACmZQ0rqpx7V-WWjKlpWMPk6xyXX0RKyyJcMDhyMuSbVs2ZbOhuhVot46IviSg5Xaw70Q3U-5YqYta9399m4bSW3OhXzdFz6TYJGS4n4ntLR8aFOFDOHTlaMcnTZpbIPe_pqNDZ6eAuWhm-SZ4H1X7rSDCAFEasFwLcWe4q5kQBPLjATv6CAwhWftG0QWTEG54eREublTeWX2vmWldbCcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=rZJtu3SmfnjKL4U6qf8tUic1A4txOYsOTwMWZLAgW9IqI2GjV1tWSOQY8S5nnGQqQJtiR1bJq5ySNEAwfk6WzaQWXTV0KU1wt6WdpvYTeqWltxU6QDBaf7elAVpqqnivACmZQ0rqpx7V-WWjKlpWMPk6xyXX0RKyyJcMDhyMuSbVs2ZbOhuhVot46IviSg5Xaw70Q3U-5YqYta9399m4bSW3OhXzdFz6TYJGS4n4ntLR8aFOFDOHTlaMcnTZpbIPe_pqNDZ6eAuWhm-SZ4H1X7rSDCAFEasFwLcWe4q5kQBPLjATv6CAwhWftG0QWTEG54eREublTeWX2vmWldbCcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇨🇴
وقتی بازی‌های باشگاهی تموم شده و از بازی در کنار هری کین میرسی به بازی در کنار این:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22894" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZn8I9yTAuKXWI-l0YUXfAus01I95Wh84w49JhZnVBSEcct8WFnI2qQjlMtmpspoACCaaSgmW6xFHW0zZjiBwSjTy9nlzyThYEB8IEXvuuuBw0bCUGtjYPlQv_-Exo4-cFz2LcSttg2GmqNsk31kqZLd9hISI1kfnA3pP2dip0lQJu8PVk9khN6YoasLfZjHId9BcNFRC-6CkZlx4f93OZAjRvhdGq2YTz9zsFUWoan_TT77IyCyTibL9uhvTm17OekwaPIiWEXbhsQJdsk3LvyR9P8jhH0rBjVq7l0WZWqWm1dPVRi99Z3FIHMORDmvXGJD_5kFjwMU2XXmU_JLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22893" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnnJd1XxBkjbgBWIDQn3PZRrwELIEvv-cRgmq5hGXqWJhjKn0xjYM4qqXJ16kjKZ8Feim5rISj9kDClowpXr8BWaO0danU_yR_tBOb-URd-5jLPX0Y93w6MnTANGwATn8sin03adfKJEDGtcjU-GsjTT8BU7Xk-jY24j86XMWDq3vZU4-y11zRHaAxpvCQ-GteH-0OMIGrgj9HUWrGwLtOIcBvS4b1IGPNi8-a78VFEAuGJziPj4oQBbTWQD14nmlPG6aCvwafGMlrOCtYt4miwAOQD4xBlTEaEAqWjiD-jBn3dSgTie7fHclgnXPL2m2d1Bg9ObQ-CQDU-rS-3uHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22892" target="_blank">📅 19:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=M3Ln5cidRHBbERdA9WFn5uWlHhivlpgZkFa5x_szcxSdZXnK6p2wB_xfxrkUuxAgeiyB3Wo9l19YlRaRcyJkymfUhd3jQVehuQmh2HIrg2PajOy44S_KVyuUTvpSxtD_K-zNGVMmcXrB7itmT1rkqX4JmczLACmlpstpSvKBe4eznWPYVB8j6KbgUYEjkomkiEU0SlT3Iw2EmcvgKw8OtFZrK5-xforA-rfRK8eFB4tjQzF0rfDuGci741pz4LF9WgvjI9MRWtte10Pt8El9485NdvVKH9VG_4IIXhIr9fytQV8bvF_cr3VPlMGil6vHf2NrOZiAAybq-xUaKZqIdZ9PJBmWO8kjlwI-79gdoK0UXQAHg60wclEVNsYCThBPo-yJdxAC2ccN1opji2VnDjx38tg4hCoVyyWhnDGUp9F2Q_XEc9ObUtfIs46Y9j-NpUHYdtb7zwASzksmVqk_-vh7K7wjhEIpTVJ5PNFXslbb_UXIaSBoMnqE4MHGmSRxBEhOVeyNeJZ_lYOZtc2nlOEeONcVnoda6i1cZWRStDCOTQBbCdiOadXFOerY89XXaabd5Q44oq_Z3yx3NY_bGXzBSR0xxFSgxv0Yt6MkN7DJLYxNLepd09wPSE9xi8VUlxuwL2TW04b1esKUsCmMB7sart0fiucnxbXF3xBpgfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=M3Ln5cidRHBbERdA9WFn5uWlHhivlpgZkFa5x_szcxSdZXnK6p2wB_xfxrkUuxAgeiyB3Wo9l19YlRaRcyJkymfUhd3jQVehuQmh2HIrg2PajOy44S_KVyuUTvpSxtD_K-zNGVMmcXrB7itmT1rkqX4JmczLACmlpstpSvKBe4eznWPYVB8j6KbgUYEjkomkiEU0SlT3Iw2EmcvgKw8OtFZrK5-xforA-rfRK8eFB4tjQzF0rfDuGci741pz4LF9WgvjI9MRWtte10Pt8El9485NdvVKH9VG_4IIXhIr9fytQV8bvF_cr3VPlMGil6vHf2NrOZiAAybq-xUaKZqIdZ9PJBmWO8kjlwI-79gdoK0UXQAHg60wclEVNsYCThBPo-yJdxAC2ccN1opji2VnDjx38tg4hCoVyyWhnDGUp9F2Q_XEc9ObUtfIs46Y9j-NpUHYdtb7zwASzksmVqk_-vh7K7wjhEIpTVJ5PNFXslbb_UXIaSBoMnqE4MHGmSRxBEhOVeyNeJZ_lYOZtc2nlOEeONcVnoda6i1cZWRStDCOTQBbCdiOadXFOerY89XXaabd5Q44oq_Z3yx3NY_bGXzBSR0xxFSgxv0Yt6MkN7DJLYxNLepd09wPSE9xi8VUlxuwL2TW04b1esKUsCmMB7sart0fiucnxbXF3xBpgfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شنیده‌های‌پرشیانا
؛ایجنت‌مطرح فوتبال ایران که ارتباط‌خوبی باستاره‌های‌خارجی‌داره؛ بار دیگر ارتباط خود را با خامس رودریگز ستاره 34 ساله سابق رئال مادرید و بایرن مونیخ برقرار کرده تا درصورت تمایل او رو برای فصل آینده به لیگ برتر ایران بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22891" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=rWvSUEC-gfbfRM8_m8YGhotY8IspBhmpW68DT0j6Q2KIBMZFonDj2DdI7ivlz-BpdzwDI_4zUn5KrcgyaRFF0YOxncF2R0N2A0rfpPtD6JuSCb06mrRz3CvGQXwaAenlu0JwO1wiQOQLWMi83TlFAwsxPdGsEWO1ZeI7xrMa_YKYcmcs8zBP6zet0qDjKKSpI39O2BoBDD-i0D0V-hYJz7AcI0PMF7VfkCArhNXOkffE9KZEudCsHSdSuBPF_q1qs2t4RWV9Ey81Nw7b0mgIp9LuPNU3_2n36a2pYKKo131QlLC5XAxPLQhG8lSU51ynSYs5V7gchClK5modBv_qFk6r5puBppULeX3Aqq1DchV6c6ebmVsgyZA22FXni2kB17wk4kBy6V5UiR90DD4y1XlTO5cUBiE6s9bX9kUEC-KSoDy7q1E32ADNmKiAMz2LUP7CrUrDQhJ2g7_D3D3BaX7WXeh_f5fmfyGm2FdPnoR2maZl-pHDp1-TeHcrMU7x5jDNXmHHmFCDpm9TtxSQfpzBqIx7rwXoOfwaGL-kd8YBcrz-WOjYuehgrFN1xaP-vuRBNcyoUc74BrITiOhLAGkAJEO_R59efjESEJPiH4qTrQGryzKNnPPyRRMpK9FxbVl4T7TIieDBl4-fNUWVte4d5z947eXYRxwMRIRAct4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=rWvSUEC-gfbfRM8_m8YGhotY8IspBhmpW68DT0j6Q2KIBMZFonDj2DdI7ivlz-BpdzwDI_4zUn5KrcgyaRFF0YOxncF2R0N2A0rfpPtD6JuSCb06mrRz3CvGQXwaAenlu0JwO1wiQOQLWMi83TlFAwsxPdGsEWO1ZeI7xrMa_YKYcmcs8zBP6zet0qDjKKSpI39O2BoBDD-i0D0V-hYJz7AcI0PMF7VfkCArhNXOkffE9KZEudCsHSdSuBPF_q1qs2t4RWV9Ey81Nw7b0mgIp9LuPNU3_2n36a2pYKKo131QlLC5XAxPLQhG8lSU51ynSYs5V7gchClK5modBv_qFk6r5puBppULeX3Aqq1DchV6c6ebmVsgyZA22FXni2kB17wk4kBy6V5UiR90DD4y1XlTO5cUBiE6s9bX9kUEC-KSoDy7q1E32ADNmKiAMz2LUP7CrUrDQhJ2g7_D3D3BaX7WXeh_f5fmfyGm2FdPnoR2maZl-pHDp1-TeHcrMU7x5jDNXmHHmFCDpm9TtxSQfpzBqIx7rwXoOfwaGL-kd8YBcrz-WOjYuehgrFN1xaP-vuRBNcyoUc74BrITiOhLAGkAJEO_R59efjESEJPiH4qTrQGryzKNnPPyRRMpK9FxbVl4T7TIieDBl4-fNUWVte4d5z947eXYRxwMRIRAct4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 سوپرگل دیدنی‌از روی ضربات ایستگاهی؛
از بین این پنج تا کدومش رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22890" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWHnOLi99ZPVEt9JnxVZD9aSZf8NG8jwCB6p4lqix7uyXRq1IibzFmx21QZ76qBpZhxmJHNZGYSfGLVWMR1Q8PWneblZCvZHYKR0yup2n3Lo8NRkf5_xQeZStKi4Wn1i-Yjs5SMUELrJmmseXCk3eLFWgnJrRN4nSE16UEeHc68zL4kLnV7oU1CO6fQ1E_s0mFWLYoN6FAwv4pJTZWOVXwEj7aLN76p3DK8CkH3uXT7CaKCqPBxnScZ2sIxeLuqJ05U2x9yeViXqjVLc3fRC4W5h4O18lXG1m0V2F9O8RCNkaZICl_63bjPpUAIsYM5TMxrsLcWF6ISqr2ySC2b7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22889" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTTzBqnixPLb_m5n4M7NgRFKZ6pH_CXk3iDf5zUtsXvXAan0OBRFZHF0dm0kYZLjoPRG8qPqEE4bJk7b8J6pZ0lwgW9r7jjShKnDIQ7KJY5FafFS9z60qVth728elc3URQa5HqXYLy7KYzmLp8dPkd_iof_UrDPpuJO48sJefyg5k-W6t9smmvdnLYSlfP7Vd_lmJBobA2XgjBS2v-T574ZxjW-7LR4BJ34sg4Z0yqLKaL5nA8-opYkHQlwJxNVAvgLmEx1Az33dGJSFifcYKg24yWGmiAmFI-mfdMxLmJd9iEg88aMlCcglaoB1JEkE7EsHytpB-mZoTUebatWYPfE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTTzBqnixPLb_m5n4M7NgRFKZ6pH_CXk3iDf5zUtsXvXAan0OBRFZHF0dm0kYZLjoPRG8qPqEE4bJk7b8J6pZ0lwgW9r7jjShKnDIQ7KJY5FafFS9z60qVth728elc3URQa5HqXYLy7KYzmLp8dPkd_iof_UrDPpuJO48sJefyg5k-W6t9smmvdnLYSlfP7Vd_lmJBobA2XgjBS2v-T574ZxjW-7LR4BJ34sg4Z0yqLKaL5nA8-opYkHQlwJxNVAvgLmEx1Az33dGJSFifcYKg24yWGmiAmFI-mfdMxLmJd9iEg88aMlCcglaoB1JEkE7EsHytpB-mZoTUebatWYPfE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
انریکه بال؛
سبک بازی فوق‌العاده و تماشایی تیم پاری سن ژرمن که ۲ ساله هیچ رقیبی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22888" target="_blank">📅 18:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miRA47l1wWbczRPUquI-zCnK1mQwugzW732wHJKDaXt0bmvQYMjCdL5HzcbjLXgc6rSap87JTSKD6d6XcaZV32TQfXSqGYzVdI-glSWLyzeF-a3PSPcYBZWAq_hPVK8WbtbFv1-3u92bS1_hy7KDB0fvtsr5Rq1mZYjxLZg0Bd7ssy5czbLrdCWhKAJX97kVL99K41FdWCAJi-xO07PdbugasY20EG6Un0MgYgFk7zJzJlztexZlfKL3RF7H7pL1rMjqjsupOyBO5Vr_S4NxXH47Gi0IUt9MKnD_ztSwvD71Z3B7uZol2u4PxzZpl3mNZtDb1sKsTwwtwxtn9yGvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌ بندی لیگ برتر بعد از سه هیچ شدن بازی گل گهر - چادرملو بسودشاگردان مهدی تارتار؛ پرسپولیسِ اوسمار ویرا برتبه پنجم راه پیدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22887" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=couni3_i9qN0T7yhUgK3g2JehuqYLkLEHOyWHR4NfZ2xpAil3QTmuneSmFZdhu0Y4yONJP9JBnlivyoX-szZpixoWfF3ZIUuVyPwFDXXOs8TeAY1oReopQJiKluVU8L3tThmiZMiRHIGKGFQPUMfQ8BL56_wVIEZHYHRHVR_MV9P87FH45K8M_x0kvRmVXpC6nQUcnD8pAHeqiDCzapDO_rBqMDVralNr58mkTjgfIfD_sSl_hZ2MKKwCjU1Rag_3JD8kct-dItbY2rPAcqgCUmWU86GtGFNEmo1Vxu879WDTYb4EUyRPI6tntf2jwEtEv593swhHqGHuBDHvuCgPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=couni3_i9qN0T7yhUgK3g2JehuqYLkLEHOyWHR4NfZ2xpAil3QTmuneSmFZdhu0Y4yONJP9JBnlivyoX-szZpixoWfF3ZIUuVyPwFDXXOs8TeAY1oReopQJiKluVU8L3tThmiZMiRHIGKGFQPUMfQ8BL56_wVIEZHYHRHVR_MV9P87FH45K8M_x0kvRmVXpC6nQUcnD8pAHeqiDCzapDO_rBqMDVralNr58mkTjgfIfD_sSl_hZ2MKKwCjU1Rag_3JD8kct-dItbY2rPAcqgCUmWU86GtGFNEmo1Vxu879WDTYb4EUyRPI6tntf2jwEtEv593swhHqGHuBDHvuCgPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد‌هاوقتی‌میبازن
🆚
وقتی‌میبرن؛ لبخند برای پنهان کردن درد و اشک برای رها شدن از سال‌ها جنگیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22886" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpwVgp9s1ofl4lYsp2EkBJz_jUA6zif5n_iZj3jfgHnKx0QyQX1WD3iY-YGyW9mE1fv1-fL68VYdkIkuOMOSKhnFYqzTihR4MfNH46kjYxPCCBp34vogzvA-GG41G6EBKsOhoHcOM5IMOuahnCDCcBNdTcquBpxSQ4ca13b2ZDFmwAungKbKCMgGfNmGBygHiNGtSebi5pFU6G0oKbIdeHT8uIp4uVSOSw9yz8tB6vyNn9d38pqNzGWvKWUkJCL-u6kCju72oC1aomW-fXLeGOB-4I8_kcCIptYnMdXrzGqPYdMlsJvcd0-W84qFzm1IGT8dWDhDfR8MUiG-UEFRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDNB4M1cbdq65D57DNSKXkhubEMMR51D35MjrnSvpe3ouHgYqKDrr1YNSWHnxc603v1GtsClf4YlSgRIICJ0QZhz22OVAMOpVzha28Xu7PTa719jEf8wJCDyBJXTrMqltVlZnKFXgMWQqpzEJ9tUEY0bkWmBZRnGVhAGTQbHaF7EludJWocdbq-ght9207gC0NK7mUMWzvvf25AhfXNMej3gKvRQwbNqK65137a7n6RYn4RbNmVF5XFZK5Z2Tnbq7y7m5c9tLkHu-GYSoksnDLYtTCrewdPfNXgTbbp0mex6QsIRLOXA-Ikbp_1E7iYAY7WWgme_Cm1D3whcbd6bhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🟡
🔴
#نقل‌انتقالات
|شنیده‌ میشود آتوسا یوسفی خواهر آریا یوسفی ستاره‌بانوان سپاهان مدنظر تیم بانوان‌پرسپولیس قرارگرفته. آریا هم مدنظر تیم آقایون پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22884" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej23QF5MfeA6CJPNGUhPCrUNMsRhyAfOy-4IFbIQ9aetVkCPi_Ro_HG1l5Nqy1awhvZ1OyIP5HQvd4jUUHjNwOAWuT3KMc1vw8PKRRv_-dGGq-qByVDpTDrEIOuIqNpJellhfL1hKVbbDsCks7Ctms-fE_7w5ofKGvBOo0WkYBqEpYqxgbAa6jsMNuWgB-hBuuWwm6UHV2-InWTkN8dU3emtirOeahHJ1uIF1_ceHHCX9jJsUVVis1NbWN7WWQ5HdMop0DbVedXfS9FBULO8yltr_K-_-Td-f8Q1VK6RRNnrbiVgpBfy9fsqaY-tgczbMM2i5XDUvx8o_MBsPyaEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#تکمیلی؛دولت‌آمریکا: به افرادی‌که حضورشون درجام جهانی ضروری‌بود ویزا دادیم. دلیلی نداره به تروریست های جمهوری اسلامی هم برای حضور در جام جهانی ویزا بدهیم. ما هرگز اجازه نخواهیم داد پای همچین افرادی به خاک آمریکا باز شود.
‼️
مهدی‌تاج:اصلا درخواست ویزا ندادم…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22883" target="_blank">📅 16:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRARahkgY5wpPf7qKrNgEAE0CqxEHndl_j9I5OdkcH2sy9XHoEEN2qwdcsYoMtDN7D_TJiDGKC33gOLikfJnlVriuhevu0riUUJUsCb-YnbRaPNU0iut65Gme7kbed2PUE5HPzOwvaZjd9_GPf5Ixf9eSfAoazLmNUa2H78fAiau1tbl0sUAe6iJw6awnYrd_P-7qTmPyYWKumfbab4qDUp4IWoQedSRYv8Fw-nJL4S7ZNHghDsJXw5k5K9qn1R8SoCJStNLnU2NASUY9SjhGDFYx-KqPHeTChSJZlqdZodn_E3hmHmQ153Ax9wP_qa4wtOGGcyb8ydUIN9zqqwCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22882" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeFm4WApxBatFFsWjst2Rj_rhrw2sML-cYAuG2VJr_V6l2A1XRkxP85qymxgNx6NF8I5Uvf-1loeVifvOoYk2zDSrtfM_zfByq8xT-rnODNZ8hDtI1rGprfwPqFUu9XDpQNZZuvWKHqwjDXOfGYt37agBkSeePCSTTNuLDd3pl3B433JHTwJolntPACzmtkaJ2GiVQQBdAQ7NzuEqdOowp_K8PoJ0vfLakA7SKyPtnyjIYk0YkYdp55TabUGt0WF2Mb9k2KzVHXnMAvkXYLO-TCYhZErWWBoif5CIBW9yOqobla7JBbUshclt5kaEQHRmOAD2tmhrtKJSrws6PKsYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22881" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22879">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gxXLxpKjIr6JsZXuXxRXHE7xM3D2HR9BAZewxV-zPvfKelY0uPpXUZFwcZEB8-LxXhokslnae-XXtmDXCsIqcXcdl1Jutb2M5bDteTUQn0O33ELwJqK3dGP9Enr5J8bmFj7_j1nfnsDDdRp3KdUAc-KTouAij5K7rKYOa86uXuHqCIyji-bgn12_K4bt7GdMZBj47masx_Ypi7w_KLDj3goIOi7PN_4zhr7w-w9ggm88VRf03j8zbR-Xj5TYqhUw_s5y00gHQxd6M_SraJ1UsbRq7_yi6b9CDMwZpCZaH1NDm3s1cn-FPPriiRZZbidxv_-7IJmsEYEyZ3iIt8O2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOu3geg7z9AA-p2sbfvpD-5ciYWvvemdsa_iFsVPdefjgVKMO0fHBJ-JgAcE9ocDQhnSWM4AQxqdS3cniagglg2kW5u2U_VGiyH-Ntb7H3JBjDut9DsMl9eAVv-HupplUd0IvISO4A4UbAcwlZWbKUNIITmRhKF4hXmiL2zbFLwq55jdXcIMywf_Tap9NaQ9t63pt5_J--Fpm9-vTzZjyoXRj-jEDEr2FR6u1rS3va2GqG6urMbG9fXIjAiwBRsBtXLhltI8w0bposiaa6f5N8FJj2zueBWvSblTEuLN-o9ThlN41BtGZrGq8CaI-QEXA_sb_GOL1jvLn7HcjIxmHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
خط حمله هشت تیم مدعی اصلی قهرمانی در رقبت‌های جام جهانی 2026 آمریکا
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22879" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMjTjbUzpVCnqlF4IfKjEttCk6vPF2PDCJoS7_ZiNj7XYZoSj0bJvB79RxBC8UiPUV3maDjrqLxkqWJRHLOeR0aEbS0F0s9QpcogyoqRRL9AQz7JK3gtgj1Ai5JrQVaMmrrVBaJBM3U46amWtfyxcR2BUo3OWS8B9GaHMlrlmpgE_bLwvHjn_LwDc_ED4eNhgRvhEFLtclybROrSWZoztyXEW0fhx_kvWYxhjyHKlpB0gWny9FSNIfS0nU1SMVFvLRAiHDnlamhQ6EX5bZbQJXaFvX8LFFpKWhhp_Nmc0S3-1Otel79d71aYYB-_8ehyg8MF8MSEbgG8Gn-NvaXyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22878" target="_blank">📅 14:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVG-EMJSlX5ipmAZ2aUsIry-foZ9aihKXh1uKhmZtRSwRCSD-Lgphx69AZBx0iAAySZFoRTJBJansx3z4HQMLpSuDahDeUNs5HkKFk5jgn3vX2IZtjJzsB9ZrrutR6FG7iIgz57kHTMUUog45kmjilftLWOBgLg_Zr-GSyFlN1fgN7T5OFZWI-sPs9J-_qKZ6jIDvkWdjpG1nf81QBYwm_aX4UCuPGBEX1CKECPZIJ50iUpG7gKiiY0aP1noI9GcdAucF3s7sVFMVIv56pddu7s_g2YDAdShTMN5MTMOfxuNM3j7u85pMQuSzLS6GbM5lHf0Ya6ErhCyVQKeOy5Ukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال با مدیر برنامه‌های موسی جنپو برای فسخ توافقی‌ قرارداد این بازیکن‌به‌توافق کامل رسید‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22876" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22875">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=Smo9NPTqdIn6mNWvYP3hcOiqwges19Mu6nHImGYoAma9JmHxyS7_6it-7kaFEx_SpoozGmzQ1b0bpOt2vT36oJtuj6Po5ftS8vuCRqYNo4Cawro6W4GB_Ghu2LSpl2JVbJMUpiWURErmKUcNZlfGLWtXB5wvyZB4MHQ3W4xNNMTU9QIJFFRfcZ-EM6MivlxB6m9DJJxBTR4Yt2AvwkAG3tb3VkTi1d4yEYodFd5HWRWvAPkfAIIP0eec2VSTERHmHjmgUEMnXh1nObgqR66ihH3limiuIHK6wbBat4tZ_Th5O8A8CIsstmKW2Zi7lfCTuErgKbgXTqVxkxgbpeHw8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=Smo9NPTqdIn6mNWvYP3hcOiqwges19Mu6nHImGYoAma9JmHxyS7_6it-7kaFEx_SpoozGmzQ1b0bpOt2vT36oJtuj6Po5ftS8vuCRqYNo4Cawro6W4GB_Ghu2LSpl2JVbJMUpiWURErmKUcNZlfGLWtXB5wvyZB4MHQ3W4xNNMTU9QIJFFRfcZ-EM6MivlxB6m9DJJxBTR4Yt2AvwkAG3tb3VkTi1d4yEYodFd5HWRWvAPkfAIIP0eec2VSTERHmHjmgUEMnXh1nObgqR66ihH3limiuIHK6wbBat4tZ_Th5O8A8CIsstmKW2Zi7lfCTuErgKbgXTqVxkxgbpeHw8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22875" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMU1UzeLPGjXybovFUzCJLV8URnO00lXOUMO1LpRHedDR6ku2Ol7cEK-m14qS5_VbKeKNYkfe6YbaN9LKD4L8JwU405nf3wZ6JlNpFlCNGf6OwHYkjMhkh5OXDpF_BssxRokBwA4PzpFWIYcgSoIGKroRwNyYaj0y7uhT9T2Lm3b6S5lbqhHaFCnY4pon10OtFW_bTpGcLCZC61wV2dQg2rH8js0C0YJ08dLyNCGi7gXn1_mzEaZHkR46HS4KbULvn1wlQjs9qDU2KvPV0WlbaI0bD3kVzch8m20UVmt_YC-LYtRr5GlNZggOm2u9ynlT-QFdzZ58DWI_Z1mh9z0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22874" target="_blank">📅 12:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nf-hfKc3cmk_GAS1IYnXr_KVnKTb0rgg6v8haKtFu56aZ90ZDaBVb2YedOClD0_nWef7HzRRBy5t3PH01MxWzBYekJmXcv09TGkw2cQhas54aTJnfjwnVvdrsPhp8gpJq0j3GXMiEo3jmGtBM8oaH2F8gqWnlnj55Oph9gqjUAMW3B-Mm2vb3dfBJ-cG-QawLfMt3kUuPUoUfL_dur8ubKnkkQDDH5TlCS77bbNzBhgSnkm3taBSMwNzYo-pIE7LszGQsp0wfGpwGJCouh_GXc-JGxBYfZg3ptd73WB5L-Jv5ecWpqguY8Eg0crsD3cTY99JdJ9wWlXmSBhq-cH9Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
#تکمیلی؛باشگاه‌آلومینیوم‌اراک: در روزهای اخیر مذاکرات مثبتی با یکی از اعضای هیات مدیره باشگاه استقلال برای فروش محمد خلیفه و بهرام گودرزی دو ستاره جوان خود به آبی پوشان به توافق کامل رسیدیم و به احتمال فراوان این انتقال بزودی رسمی خواهد شد و پول خوبی به‌باشگاه…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22873" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_NrwUgsJzbR-QBnCVMhzAjQ-psIXgxP4KiL6jNFKAqG8ob6x_BqlSO8kxZDxStAuRzWecXp5Nm0ToNlzqxXPa11bJO0-bXZ8Vw-_YcynBDxaTmidt97nn8SXl0WEnnD1X3jgbC0PaNyYScIYv4X6ruX9WuktdKfMzGs0f1CoSTnoEmOyGRymNk8owoKerMqSG6e9CQWnPiKmWKpg6m1HG2377zn1AyXLKVoRuNyEN3_u6DLPJsAItnA1oVIfgZ4fTd-YepEPUQja1OZVfLMdn0bUy8Ih9oez1S_E05s9D8IV0CfxnW9ak2ICtQW4OiGeEoxvvhX2uIUpHm6NVptow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل‌نفراتی که دولت آمریکا براشون ویزا صادر نکرده و گفته حق ورود به آمریکا رو ندارید.
‼️
مهدی‌تاج رئیس‌فدراسیون، مهدی محمدنبی مدیر تیم، هدایت‌ممبینی دبیرکل فدراسیون، محسن معتمد کیا مدیررسانه‌ای، مهدی‌خراطی مدیراجرایی، مسعود اردشیر افسر امنیتی، مهدی ملک…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22872" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssLSm_SR06Ve3r2ZHCdkcNjsakaq5dmYR36t56MkEZXi3l95alqVz3nHUnyUmiMGSp68s1L_9bzlicBybVs-UxEHe5Y5iwNbvxd9c2hFMXiuntQJUjQ6_it0-k6O4CYpkzJssRZsKZRpK0-t3p4exPnLSgBdc3cEgaL6QNt5otbf7r9k2nYb7M0iAwIpWAOA6DB7corGnLK5g96v60GJcR0NvATof6LDecGFMexCKX4epE44HW4tddvwX3Ewg1wgCMPovgGD4D2Dzu0x9NgsAkNjq4GAK7mDtwURAE1ZIRB1Ya1KzS052v3YVHzfZqHe8oOPme38ROpGoozZhBNg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام رسانه‌های معتبر خارجی از غیب احتمالی چندبازیکن تیم‌ملی ایران در رقابت‌های جام جهانی 2026 به دلیل عدم صادر کردن ویزا از سوی دولت آمریکا به دلیل خدمت در سپاه خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22871" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=JHlMRwMMaGMQ1TsMq1fJSsC8e6VqhKFLmXwPkkruRSruz38NGnpFeFvyFGtBj8Ne8QWG1GDC-LW_lf2wKNQv9Gf5tF9OM4p_EU3VhIvbm2n_nsuZQuv_8KqUDCvAq2kKUbviV3_lnE8e_Kan0wCr13daa4Y-I5BD2jyFTLwX1u8JAYFV9gxOMB1tMxHJ5RL6K9uJ3U5gKxbgESJcX9U8kAFfz_8JsYFaxvSMZ8Ow5RPEe8DtyWwve3Is-ms_iRRL1rLMecJDjfbMhNQoYAtw6ox2D2RlsJbRgiQRu65p2lbvc5Fgp9_CL-kB3BlyD4IeVxVVqiEt06WyOHyBvK3zxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=JHlMRwMMaGMQ1TsMq1fJSsC8e6VqhKFLmXwPkkruRSruz38NGnpFeFvyFGtBj8Ne8QWG1GDC-LW_lf2wKNQv9Gf5tF9OM4p_EU3VhIvbm2n_nsuZQuv_8KqUDCvAq2kKUbviV3_lnE8e_Kan0wCr13daa4Y-I5BD2jyFTLwX1u8JAYFV9gxOMB1tMxHJ5RL6K9uJ3U5gKxbgESJcX9U8kAFfz_8JsYFaxvSMZ8Ow5RPEe8DtyWwve3Is-ms_iRRL1rLMecJDjfbMhNQoYAtw6ox2D2RlsJbRgiQRu65p2lbvc5Fgp9_CL-kB3BlyD4IeVxVVqiEt06WyOHyBvK3zxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اجرا‌ها و موزیک‌ ویدیو‌های شکیرا برای جام‌های جهانی ازسال 2006 تا 2026؛ کدومشون بهتر بود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22870" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22869">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🌐
اسپانسر رسمی لالیگای اسپانیا
😀
مورد تایید سازمان Gambling Judge
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22869" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_kw1qdMAA68JMv_vQgPtH5dlsYNMtPstd53fa2vHhI5Wcl6Dfj5-X39yHhmVd0IY3zyqPvB-SFhsxBOmOHnB11qOj0aZw6hxpRpamshZCLJJI_3tNJIovzTf1LzKYCL-WUF9wcQikiEL3iMALqaPqc4d0mD2BrBngAVqu15XUqboVOjZPhPTXF7A2Npeik3lnBJE2KPVv0oyz6Tq6rZ8V5ck8Z9g07_xyNYC2hykwrGgOeY175Ba_MbKRKrrgsHQl9JS_wpu38eFQX6Hjx7sCrqJsoud7PYH8nB0UMusgWOhtW7pn7Y7DQ2Z_B9BhS-Vn1Uv09IdfRLT_wcqCmyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22868" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAdFbcMma0yAE2l1f55NJa5BLaPAvYI0m18i1cuyY9QtDdcEaV4xvMoio3BaQ4k79GNdkQ8hKmS-f4EtGgQ2rT7s-1OP4RflEZIvZuvgMgvnHLNHdI1GX_8U35V6vZ6MM0Cnzz1JNy66dBj1n-zhkf8Bm99jYhdcSukR7mQ-ttHGhGv-FIvubUggj-Kr56DRPM9AGsMa7u39KIrF5lJjDqD9rdwisKycf5wTbrssnz1BmyYACESj-kJHZAG9K0jTOyOpE4hXZN-_j81VuMaJ-xfD9gTZ4MTVPCL_VRyzKd5HhTK3PzXACJC-5UAoqO6utUXRvVLVBYRXzu6CgRwCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22867" target="_blank">📅 11:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=ZlGUZFKT1W2XB5IvC10TfJojCKLTN9a_1V18-7yfJtVmCLmK-CzuGGyXN8_xbb3OSPElWOyF7xU9vJTYY_3s-8CsdBNIfy7iMm1p18cUp2URTSl9qJppvQeQ3tkuBpc9nOZRvcuU6WrzXBj3-fNoiimzyPQiFMdLPMy0ORGTNH81ZkSi-dy470NR4Om0kVWh_0Kot42pi2ZbmFYBtKuUElgsLIJBLAHxKPctdmL9Q9jYYzK-l_IhN5qKGMOZrJ8v8A3ogtxQY2IkhnE1M-kXLEQUmVJFM4Gq7_7vVJENVBYLNY4miByDiITHWYxbCjPSRd1uVZcsSow7hQuOflmhww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=ZlGUZFKT1W2XB5IvC10TfJojCKLTN9a_1V18-7yfJtVmCLmK-CzuGGyXN8_xbb3OSPElWOyF7xU9vJTYY_3s-8CsdBNIfy7iMm1p18cUp2URTSl9qJppvQeQ3tkuBpc9nOZRvcuU6WrzXBj3-fNoiimzyPQiFMdLPMy0ORGTNH81ZkSi-dy470NR4Om0kVWh_0Kot42pi2ZbmFYBtKuUElgsLIJBLAHxKPctdmL9Q9jYYzK-l_IhN5qKGMOZrJ8v8A3ogtxQY2IkhnE1M-kXLEQUmVJFM4Gq7_7vVJENVBYLNY4miByDiITHWYxbCjPSRd1uVZcsSow7hQuOflmhww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعدادی از هواداران پرسپولیس مقابل فدراسیون فوتبال جمع‌شده‌اند و شعارمیدهند که پرسپولیس رو به جای گل گهر سیرجان به لیگ دو آسیا بفرستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22866" target="_blank">📅 11:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">▶️
هایلایتی‌کوتاه‌ازعملکردخیره‌کننده مایکل اولیسه دربازی این فصل بایرن مونیخ مقابل پاری‌سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22865" target="_blank">📅 10:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22863">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=VJURH-pZM9Mnwi2DQYbB4mp3YkDGsXRtzV6jsTjHNgXdE7tSA8tn34eVZxsP47UsV2zTf8TIZhX2q_PdakGBbr048b3yIxYK4XoTPRVs31BIYXnF5xb_8c7O4xw2fzDBz6GbVSJiwnuWZang4PPlqVwtl9VNZVd-AG8B2doiCcg7JqiuwQHcR436xmrjZlhd3RD2lr0ihVeIlffCXpKbeDwWrEyKa4TobJjcBUHK2E52FO3EUUUmUUKWWjkTmzINU8Gfs-tdCE5dftjk-E_bit3OkI3iORdjXHhlMdqEYEsN3N8LYwu9c0WE_yh0U1qFwkgkxXBC3PNn-acGmGeLHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=VJURH-pZM9Mnwi2DQYbB4mp3YkDGsXRtzV6jsTjHNgXdE7tSA8tn34eVZxsP47UsV2zTf8TIZhX2q_PdakGBbr048b3yIxYK4XoTPRVs31BIYXnF5xb_8c7O4xw2fzDBz6GbVSJiwnuWZang4PPlqVwtl9VNZVd-AG8B2doiCcg7JqiuwQHcR436xmrjZlhd3RD2lr0ihVeIlffCXpKbeDwWrEyKa4TobJjcBUHK2E52FO3EUUUmUUKWWjkTmzINU8Gfs-tdCE5dftjk-E_bit3OkI3iORdjXHhlMdqEYEsN3N8LYwu9c0WE_yh0U1qFwkgkxXBC3PNn-acGmGeLHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کیلیان امباپه: همه فوتبالی‌ها قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهانه جز هواداران بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22863" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22862">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcctBk-3F6pUVVzjKAZONpYxu4WVn7iTl-QIB_tfS5Kv8ShLO9aH4A3xbBhF7aocwnX2YQIxNCOlYVNNl-qT7lMLvyIxkZM__9btYAyDb2_CDMaY5Acl3k9Xtg9mrbTxQ36R-e5aQHwC5A9O2YVupCRNuINT6gjfmAhK4KzuUF_yeyuE5HnU71anD8iW6DaQL5KBFRqnAQbTKYEn4Xzz2ph3ABAseXbYgOBAJPtl2QcBQnv67n3-s-tOmJTUx9EGq18InxIpnc_MqI9IqGTRv95dmw4CHQYp-26AqcFDpzNGmd48HcpFCixdYtA1NbX0GkWoLdPsNRWdGGsQFW81OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین‌سرچ‌های‌ایرانیان‌بعدِ88روزقطعی؛
بعدِ بازگشت اینترنت مردم اول دنبال چه چیزی گشتند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22862" target="_blank">📅 09:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22861">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=BY7dO3NkVi6KXg2EdWUQqY8xwix97F92_bb5d_NSa5DrQ1e6M7TEdfOcmrEwASLaFX78oBeycXahsLyt3v6zxVCiCuEnamrqWzq6fWHspD8TCDF_AqMAeZsGxo8thO3WQMceBZf4nbKXpfz7xlfOmqEmJJEXVb3SaeYdVsR2qQ9-8F46if3XusH0cYg9RUp_Q0Na4XeFf9EXF3rRKJ0lRn4FWO8sSufXqjtHGOBoMX2HlFBzHM6BIxvfMhunuG2XglDduVEdmRZ182OilkNbM7FYMw54Ab84KbdELV0VPnRAHjyzRhqqUR-tqPcejM8mNsxMQpv-sgtnTAl1ykGOzBgxb2cunKUybeq4J0J6IWtn6Y4lFlcYxxkFqGGPNZGe4HQYeuBYmdwkK-NIt8IW5Dc5xA_jRA9QGgMVyV1l4UBSzKs37kHDhOPR4hnyteVg4YZuAy4jJmEMUEyTncAL5wxczgio10ybkEnKHyCfy_9zvuHNYxQXDoZbhZWXCdbH40wWnUvdRAF8RMQRnyvmE9Qac-nqFI-ncms-nQ1hWnPJapIg3LABd2G9tPPNq1ORO6ZsXwNP5LE5vCYsWymdnZ0_hVyX7G1TfIIheueXeTDN2BRf952GyGPRQzdGT551ulCjiWx1oyjFHYan55MouOfrj4NMizh141bgp3spb6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=BY7dO3NkVi6KXg2EdWUQqY8xwix97F92_bb5d_NSa5DrQ1e6M7TEdfOcmrEwASLaFX78oBeycXahsLyt3v6zxVCiCuEnamrqWzq6fWHspD8TCDF_AqMAeZsGxo8thO3WQMceBZf4nbKXpfz7xlfOmqEmJJEXVb3SaeYdVsR2qQ9-8F46if3XusH0cYg9RUp_Q0Na4XeFf9EXF3rRKJ0lRn4FWO8sSufXqjtHGOBoMX2HlFBzHM6BIxvfMhunuG2XglDduVEdmRZ182OilkNbM7FYMw54Ab84KbdELV0VPnRAHjyzRhqqUR-tqPcejM8mNsxMQpv-sgtnTAl1ykGOzBgxb2cunKUybeq4J0J6IWtn6Y4lFlcYxxkFqGGPNZGe4HQYeuBYmdwkK-NIt8IW5Dc5xA_jRA9QGgMVyV1l4UBSzKs37kHDhOPR4hnyteVg4YZuAy4jJmEMUEyTncAL5wxczgio10ybkEnKHyCfy_9zvuHNYxQXDoZbhZWXCdbH40wWnUvdRAF8RMQRnyvmE9Qac-nqFI-ncms-nQ1hWnPJapIg3LABd2G9tPPNq1ORO6ZsXwNP5LE5vCYsWymdnZ0_hVyX7G1TfIIheueXeTDN2BRf952GyGPRQzdGT551ulCjiWx1oyjFHYan55MouOfrj4NMizh141bgp3spb6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
#تقویم؛ یازده سال پیش در چنین شبی؛ بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22861" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htVoqHU7Z-j3T0xGgrOHtDvgH5d75omRdA5m1fszAmO1F1_4SanN-tstEVAXiRJ7NUkx3B5k7ZxJfC6yy2nQq_pwO9VPaJsGWzZIrM06RjOo2JwD3Tza_M3xRkgFeZFykWGTNJzvK4a6BfLphb-YCH0Vn0wJvUKKw9dj2QGb9RJvptu0sKMP9NmoLlZLJ5gLGHSC9sbn7QfM1d7bhRmlqRxQBsbvrI5gPFNDbwJx_t_SHCFGF2J03-jW3JYYJGWtU_Rmkhl6xwnIGWmouryRVFzvicIoyf5svJJw4WOsEzaxMHusczxB8Om-bsx61QdGVDZRDqL53LhOr-NYn8Y6ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8B7A0_-Eo-IvopSeM30VsHKVyOIC_IQs2TFi6isVSazuncQf7qNmC012Fs-i1TQn5NXXOXWSbU9L1wXfu9mvQ4lapVfS_a7DPlBHw_SJGIZAphhfbtQrViQuZMwWHsdjOHgfnr9VrjBE1rMqf1oMHr40YexzjDLBplRYnd_Y3d6ycgElbB2D09Xayy0rVLgjCpoxeplsxoQyfVRRNfZwD2URmN4DlhrLpR3UMGqf5vU6DBPYZzfvLhjtM4119ZmCcMREfURBt-A8z4BQcEY4LaisQQX6s-ZJmW-c4BYSIK4Q7KS5BuzKU7iUkc3bCaRMAYyJPBkWtoCRMhfkG2-jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تقویم
؛ یازده سال پیش در چنین شبی؛
بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22859" target="_blank">📅 01:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pteo75c2M3G-qX94fv4eV8tmL-kQ4AyXCBxvWBk2eMqz1XdzylWOGkpHQhT4cA3viRNhx_6du6emOQew9Ym5IQmEncJXEfm8grIPQoVMNzmp-KnXC-g0ajG24W1OwXKxQ2nIrJeX4rF3d4KdUX9jg8j5J1NnKD4hqoFoE-BGX8wEy4GyFcmmFbilxD1xmFlwcw5wLLc0vDYIXTcJ7WC6hl-YFhCX3paTVcmY7p42_22PHtq9rf8ztTkwmlVyVjeCAXcrX6ZAdxzJ1iRH4Fb6Pus4KMaPnp3y_pd5TPiIjv2_l0d7Gm0FkK4sWxgcn2DI8GFI_ISAlYJ5gnKZuF-6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌کامل‌دیدارهای‌‌‌امروز؛
ازجدال‌یاران رونالدو برابر شیلی تا تقابل آلمانی‌ ها با شاگردان پوچتینو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22858" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQPulw-_MjshGDM7M6NMUXCbWX-JOBLch-6Wi9jMkBJ8lozqk8YByr_A3mG7Px4P52maAT47nmlg-YUwqr3R_IEdI0VepTlbYLM-YIECCb6fnsOHAvWCIQSdsZLskzwfKe7BvhDUCFCfec8_R0HLs2pgHm9D5OqaJuL8puNO6sPNZF4fM7wIWc_brx2yItL2yemENqVXRJWJMe6r-dCAbx2olWy09Lq6wFrYCHYYui49yeI6LIBDyX-ifHt94MAaQb-6gqklrkvONAmWSuHrSDKLF2EIyAJVMmkOc8-D8ZwzMVfz3jw2Qlg2L3rLfJ_dHudkAdb28CjfGayO5niJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌ روز گذشته؛
استقبال مکزیکی‌ها از جام‌جهانی 2026 با جشنواره گل برابر صربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22857" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22856">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYrCh87r6PeOIR3blkKWJTY6dyPwAtUo1c7CmdnnV3K1tdvfnipE-4eOwSacW2k84-q0SUXNcycGkKDiVdsp4NuGzbbYjiBy0ejoZsSVfTXqO0q1aAC7zhzXDJzEd10x3pnFfgVlXmt6O6du7JbtTppQQO1uZ5Iv7qHodbXhYMNR_qWZ8OqjRR669Xa7KkQHWqj8C4RQfYGm8W2vdpQVbg4RTDUfAAOqDLEHwiXf4N3FpDGLFxq3lK4RnJyqFhPxIXlNdK0yLcryVKs4liC9kHHq7EB7_A-RN1-_6IYdB1fTFR8-pZ2HxlMoT2qROhKgX35JWLdEB92IDP0mN_VRag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شوک‌دراردوی‌ژرمن‌ها
؛ لنات‌کارل‌ستاره 18 ساله تیم‌ملی آلمان درتمرین امروز این تیم بشدت مصدوم شد و رقابت‌های‌ جام‌جهانی رو از دست داد. ناگلزمن سرمربی‌ژرمن‌ها بلافاصله آسان اودرائوگو ستاره 20 ساله لایپزیگ رو به اردوی تیم ملی آلمان دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22856" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22855">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvRB_4a7aWWKFMlLqoK8C1R206odoRgNRU1aIYQVbRMWU6wOOAkhwWcj43jpPmyIpdyUFZJ3EucJxWiM0FNyDBSUC053gHslabPJqGhR-J6w4ix7Ft50sLq92NbJ1l8JhKDgCtXuH6j6JEhokKTk8aUuJxbj544WuhYCdkyK_IS-s-VglQTRNxuJ-aBeIxzEI_u0vbu9q1KCgSVWXTcdxzLjIzOZeVLstUx2mY67r5IWYkEFqcylGZ-rQBFty4Xhhne_ndMcQa67ccUZaqAb-talEZbFVBnoQuGMlcVBtxzilXjXm5cC9J20YFQGQzm3J-Bcr6faCuNZBAlCytFPiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22855" target="_blank">📅 00:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5dUEbIUb8yKe0-qFiw6nbGcVsy5Xv8FgwvjwhAx2dXsGhTeqH4SCAxiN8yt5fGTbGGebuj0QAaDyl2ev48b0cp-b3OGWOHNwwGjE1zIE_bl9jV39yTjRlLASp8WDxg-Aezx05rCaXCy5X8IpjPM_eNoShyfcJFnDJjJatrVoqLFY-2T9brN-U7Qvpe5z9twHncJyAJyalGU3jTO5lg8X_MgsJ3ssfWBBRB1uDdA3P6DqYcAYFiSUZCew3PiP5BHQZLr8WvVboFHzvKUD9url-04G09u2NQcgGKaEe_rziNVpXdo9Uk274POpuRmqdkjJxpUzJW6yqyHKQ4q5ySmCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چت‌جی‌پی‌تی،دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت. همه برنامه ها دارن رفع فیلتر میشن جز تلگرام،اینستاگرام و توییتر؛ سه‌برنامه‌ای که بیشترین استفاده کاربردی رو دارند باید فیلتر بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22854" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22853">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=nqh6olJeMcbYf_fOHUzR2sckwaRy5ien3jT2Z8jFoBC5M-4yPZTKaNDdMWO9pNaYtmWXGx0DWmM59lAirOa2-5ow3WfWcUSQa2WpxR_VKwlCZINEwTx1qQS2_iZwR2R1feSBZffN3p0RUA6JBC4iOCMDBBOZskBFUrAlTqLeUzgTcH4bsyRZSU3ouyBHLBp9UEH2GnTo2MPIFduf4MppeUWSaBIogKhnicTWcz1euFMU9mz2Ymunb66IDKZkCM3YYkhxLrvCQDmthqzQy60031Dzfo-3YTBVReKhqms0PQuaFC0JdORBLYVVTvSx4QVuBei9x2TVrHHQWoXr_IUR0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=nqh6olJeMcbYf_fOHUzR2sckwaRy5ien3jT2Z8jFoBC5M-4yPZTKaNDdMWO9pNaYtmWXGx0DWmM59lAirOa2-5ow3WfWcUSQa2WpxR_VKwlCZINEwTx1qQS2_iZwR2R1feSBZffN3p0RUA6JBC4iOCMDBBOZskBFUrAlTqLeUzgTcH4bsyRZSU3ouyBHLBp9UEH2GnTo2MPIFduf4MppeUWSaBIogKhnicTWcz1euFMU9mz2Ymunb66IDKZkCM3YYkhxLrvCQDmthqzQy60031Dzfo-3YTBVReKhqms0PQuaFC0JdORBLYVVTvSx4QVuBei9x2TVrHHQWoXr_IUR0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع جدید باشگاه رئال مادرید هستن دربازی روزگذشته با ساحل عاج؛ واقعا مدافع قحطی بود که فلورنتینو پرز رفت این رو گرفت؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22853" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmoFXaBbS_a8dUZEyZavvdzHgq77KYCoAJLnb3v8_Tf-6xgQfNUldFsHUSoDcCgGs88KF8P3k1LDvsRPcSB5GrIWbj9PDMzzFO_WiyDDU8OJpEi40KHkOUti_Ez281a7LyQf8CRPKqkEI1JQA06UI3p8w7ptOG2xAZLX8JKybj5hWiobAQBKVvhP51kOHE-WrYTzgKj-mefeMk-TpUFLL0j6h004CKlhysLbCPqqA0NQVVpdNJ4tWyREb-sRD4KRfjByV0Xg1zxjL9nhkXL6C7XCleWOR8_HLfiCtDpN7_7ojdNUUr_FIVM1t978A8weYyyDGWWleW2fPovCF9bSNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
علی‌‌تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: یک‌‌نفر از اعضای‌هیات‌مدیره تیم استقلال در طی روز های گذشته با مدیران باشگاه آلومینیوم اراک صحبت کرده‌ تا انتقال محمد خلیفه رو نهایی کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22851" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgvmVkxm4wDeWeMofUQYBjdXeRJQwoflEUqhx3C4iixWEhTw17m0emBhmRKzkqxXbC2BmlLuh76ty6qjCQJuSalcGDShyt_eVYn6QiDh_CGPBo3Ai4QmfZ_uWYDid2wXNA0qj8vkrLc1NQfS7h7VZqNLHfHqAo7sStcWTUTdqiY_5VtpyB2t2dZJrvPohQ8eE3W1OmBqzrnXibhC2VFU5Fc2-y9cxBfv0z8jDd9AniTQ1AzFUWJkwUGUqKC4xV2Im3GUx7EfGbLfVv24p8XhDpn6-GQW5cRqDN4yfOsdNd5LsBPXPC55pjHk2Sf1-02qmGQYa0jn8B6apM8884AVzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22850" target="_blank">📅 23:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=RKamiRBZO_M27-8b3TMOTSXsqoFExuLGXvDxsGi6-tjvr1i-QAA_2jN3qaydagI9rBI5iBRHgCa34s7jfoki9bzRb0WBh5s03om1K5MN9VsWyle_EeMiX-wAjMSqoGQfPzu5Gm-dXCq7muxE-eaZWIo0B1f9taAJytK56RNF6lFcTZv9UEDnG8Um0LlxwmZ-PVeERRLtVgdgNx0lQ8SKWZr1aRSUf4DkDo5YY2g_ZshdyiadFyycRUu5SxUYMgN0eCXT8l76Z_wsgbAb6eFcqLDQE6vIhkk6QaXYy6IKe1kHGEt6Yycxxlyd5VSLpgoPn3fTz8sDkqLhW6nFORgdqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=RKamiRBZO_M27-8b3TMOTSXsqoFExuLGXvDxsGi6-tjvr1i-QAA_2jN3qaydagI9rBI5iBRHgCa34s7jfoki9bzRb0WBh5s03om1K5MN9VsWyle_EeMiX-wAjMSqoGQfPzu5Gm-dXCq7muxE-eaZWIo0B1f9taAJytK56RNF6lFcTZv9UEDnG8Um0LlxwmZ-PVeERRLtVgdgNx0lQ8SKWZr1aRSUf4DkDo5YY2g_ZshdyiadFyycRUu5SxUYMgN0eCXT8l76Z_wsgbAb6eFcqLDQE6vIhkk6QaXYy6IKe1kHGEt6Yycxxlyd5VSLpgoPn3fTz8sDkqLhW6nFORgdqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه آلومینیوم اراک اعلام کرده‌است‌که هر باشگاهی محمد خلیفه رو میخواهد باید 100 میلیارد تومان ناقابل تنها بعنوان رضایت نامه این بازیکن به ایرالکو پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22849" target="_blank">📅 23:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=byx7Yky7Gi1r9dFvtBv3RBZgu2PemIvGA1aIh5qGjpeSa7ZiqGf2STCsyjP7nYy0OaHZH4eBzTI4gZQCQrHDwMOYt_NMBiGakABq7649bL-oMq2IZZbzvm5kH_z5EUmiHuEfPQjuKWb7zuUznoJENjysLSeJRdHlC0XCSKPlqhORqBAU8s6QsDpOIMQ-kon8FA-tYv-mb4-76aRDyQcbAEV_wjjH0yfLdzzmra5LVveZhSmekH4XXD8kNsnxMXxQfnVQG-bRorkuRzn8NfDKROZqUSvqkD7i-RdjqejQsMSFWDuqJxwExv9tPA73gLwZo86ySIxv3d3j2TE5jMziaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=byx7Yky7Gi1r9dFvtBv3RBZgu2PemIvGA1aIh5qGjpeSa7ZiqGf2STCsyjP7nYy0OaHZH4eBzTI4gZQCQrHDwMOYt_NMBiGakABq7649bL-oMq2IZZbzvm5kH_z5EUmiHuEfPQjuKWb7zuUznoJENjysLSeJRdHlC0XCSKPlqhORqBAU8s6QsDpOIMQ-kon8FA-tYv-mb4-76aRDyQcbAEV_wjjH0yfLdzzmra5LVveZhSmekH4XXD8kNsnxMXxQfnVQG-bRorkuRzn8NfDKROZqUSvqkD7i-RdjqejQsMSFWDuqJxwExv9tPA73gLwZo86ySIxv3d3j2TE5jMziaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22848" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22847">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hatgxsed3rf6myx1soz5kJZJI7w9pfk96PRKWnpqjksarPnwvu9YdjqlVnzh_wKLaF4UWMR3mqCWczWQNNZtT1ofsWP9peeTjy43_y3hTLSeF5vWTrEuxHVPZ2a5RyTboNLQ9cqTOcA_pF-QzqryYQAQdRmfKrwH0ggvebQqy8CEbTsIltkARTbEkp8CFV_ZORexu46H9-rDj-ucGdWKA31HXFXaXbqnynWtEDoJq0Zekoy-BJeuAtoXtZnToU0KRFgirHH1PmEOSU9p7PZ17XfJPzxJgo6PBN1WQ9OppH4jPHo8WUYX3OAiUCamXY-fdkwxVYqOThp-9pMogLqrQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه ستاره رئال مادرید: به پیوستن مایکل‌اولیسه به رئال‌مادرید بعداز چام جهانی بسیار خوش‌بین هستم و امیدوارم هرچه زودتر این انتقال دوسر برد برای ما رقم‌بخوره و اولیسه رو بزودی در تمرینات رئال ببینیم. او یک بازیکن فوق‌العادست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22847" target="_blank">📅 23:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22846">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">▶️
انتشار موزیک ویدیو جدید شیدا مقصودلو همسر ایرانی خوزه‌مورایس‌پرتغالی برای جام جهانی
🔥
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22846" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22845">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=UdfuMeq1hLoh2bC3bs2YTrXTs8iK0L_QjBKN3Rx-4wFmN2fcXA6km-5QkxlP8-r3OYM6xriqwT-Y0-wSIrfBG8hGx1Og4Z9RQ2pRe2ididIXiukVgKJz32zhDkGNy2Dys4VlR8ZLt9nOMe5KZ1eVdoqaiZ-CO7V65P7hR96MoiYIkumAgQjkppg-2S2fzoexFg6HJj4MzXVrmSdkJwIAwq5uVRkgKDHF2O_5gfz5ZxpAOgc6R1F6nvb4dUcdmluqZRwB_jJie6ZKiFxCWVvSfTS6qCQQAYURI2yOF-DgLfQBThM9nDR33maM1V4X6ch2gT9p1vcgGX0MnCtMdVUdTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=UdfuMeq1hLoh2bC3bs2YTrXTs8iK0L_QjBKN3Rx-4wFmN2fcXA6km-5QkxlP8-r3OYM6xriqwT-Y0-wSIrfBG8hGx1Og4Z9RQ2pRe2ididIXiukVgKJz32zhDkGNy2Dys4VlR8ZLt9nOMe5KZ1eVdoqaiZ-CO7V65P7hR96MoiYIkumAgQjkppg-2S2fzoexFg6HJj4MzXVrmSdkJwIAwq5uVRkgKDHF2O_5gfz5ZxpAOgc6R1F6nvb4dUcdmluqZRwB_jJie6ZKiFxCWVvSfTS6qCQQAYURI2yOF-DgLfQBThM9nDR33maM1V4X6ch2gT9p1vcgGX0MnCtMdVUdTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22845" target="_blank">📅 22:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=Faal4j9bQ0oADv2yFhcnOoijsqPxrWy7rCqs3gzMV0iitXPatfbpKzhZ7MyfxfywA4m0NlRHFKMfU36GLQKjViwdMxgbnqrmujivngGyMWp73k9_35iFsZdon7UcoXbWzerHFmA6ZvhXwMqTkhJNnBPsNsImz_7QPuLJaLRq9fYy6fsmRtXc5mXylKo1l9woVhfq36nw32DRrZcUgxL_inaXi4BlUbGxYe7S6G9ybwGE_rh20tOFpxaG3w_eBNXCX0a-ypNdAbbuKhqtXlYBiiDLEreDAt00ZN7PDINjU9ulo8N-AwCa_ehJf6hZXg8Gs6FUrwOZPnvxNUFPlRJ9Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=Faal4j9bQ0oADv2yFhcnOoijsqPxrWy7rCqs3gzMV0iitXPatfbpKzhZ7MyfxfywA4m0NlRHFKMfU36GLQKjViwdMxgbnqrmujivngGyMWp73k9_35iFsZdon7UcoXbWzerHFmA6ZvhXwMqTkhJNnBPsNsImz_7QPuLJaLRq9fYy6fsmRtXc5mXylKo1l9woVhfq36nw32DRrZcUgxL_inaXi4BlUbGxYe7S6G9ybwGE_rh20tOFpxaG3w_eBNXCX0a-ypNdAbbuKhqtXlYBiiDLEreDAt00ZN7PDINjU9ulo8N-AwCa_ehJf6hZXg8Gs6FUrwOZPnvxNUFPlRJ9Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ویدیویی‌از قهرمانی تیم زهراگونش در سوپرلیگ ترکیه؛ زهرا گونش بهترین بازیکن فصل لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22844" target="_blank">📅 22:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=cIn2VUd8pa9W5i6C4qYqMMqC6Ik8CuG4QL3OXV7dgKu0zoji9uuupY0xFMcAbv4Q17ZEP81SFzu5ohsdHhVdrSUxIYMSuviBbiFGP1oNPjQa7aaeiMc7Xzr8tvwZnmnNPuWc5W2UhkVbycV716VA6cM3D60jUSlSj5EUcDfEF-0obFxBYnHPXMTXMKebT4SUFIKtCEQFs77XuqFjodUnrClSWjaZy_ng1Lgl1Xt4zjv8gndF4A8bpY-eN53mOzZo1apR778kK1Litvfgbk24gsQT14Ik7s7-kDfUQpFGC8r5ru9YnDDg9nL-knLOGkFLap3Pf8VbeOcX-w3CyxwefaTPqlgVyGVrHhOCarQ21m59LHjorZIDK7jf-mq82bZJ_JmAnZVSgglEx2j_TcwcWd3tSGXsgsm-dz9OVRDKaIAy_n71s0xmUwnu2Ehn_115gPMewaXtHpFJa9rssm6dLsJs_jgAWJdspou2wdV6dfCxH03myV0nKhKPJrE492qVKE7k9fpNTkYQZKzfhmzfoiz59LeStC0Fnk8noUfJ2xKra1YS2ksUPPBb9ShNgOPh6Yrxp1o-g_IuKVFmvIBDQiKxQhE00DVlno-tnap7eK-wqpj1SiA69nvx51Q3nDo6PNokIoyVZZvmrLC7s4pnlj3nmx-hONvZMhxa43Rt_o8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=cIn2VUd8pa9W5i6C4qYqMMqC6Ik8CuG4QL3OXV7dgKu0zoji9uuupY0xFMcAbv4Q17ZEP81SFzu5ohsdHhVdrSUxIYMSuviBbiFGP1oNPjQa7aaeiMc7Xzr8tvwZnmnNPuWc5W2UhkVbycV716VA6cM3D60jUSlSj5EUcDfEF-0obFxBYnHPXMTXMKebT4SUFIKtCEQFs77XuqFjodUnrClSWjaZy_ng1Lgl1Xt4zjv8gndF4A8bpY-eN53mOzZo1apR778kK1Litvfgbk24gsQT14Ik7s7-kDfUQpFGC8r5ru9YnDDg9nL-knLOGkFLap3Pf8VbeOcX-w3CyxwefaTPqlgVyGVrHhOCarQ21m59LHjorZIDK7jf-mq82bZJ_JmAnZVSgglEx2j_TcwcWd3tSGXsgsm-dz9OVRDKaIAy_n71s0xmUwnu2Ehn_115gPMewaXtHpFJa9rssm6dLsJs_jgAWJdspou2wdV6dfCxH03myV0nKhKPJrE492qVKE7k9fpNTkYQZKzfhmzfoiz59LeStC0Fnk8noUfJ2xKra1YS2ksUPPBb9ShNgOPh6Yrxp1o-g_IuKVFmvIBDQiKxQhE00DVlno-tnap7eK-wqpj1SiA69nvx51Q3nDo6PNokIoyVZZvmrLC7s4pnlj3nmx-hONvZMhxa43Rt_o8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
کاشته‌های‌دیدنی رونالدو در تمرین امروز تیم ملی پرتغال در استانه شروع رقابت‌های جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22843" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNKIRQxXEM6aCFDfZwLN_ESU5CoRw-SU_1ak-N6j-nlSwE0WohblWHrU_Awae6_hky7oa5w44w6k4sb9cLXf52a7qMH8xtG2-YOk5_LWTF8zrf9Ds5raoKfMSu2SejhGLiIvQpFUwJW8BYyABxTE6SqQhd9ri-WCPZyMzm11gRS4r0DoG8sHNYvydFPHNKRyDwQJAEagUgKD5UQvjqcolYAGizvsy66fYGks_MDi2tEXFdOujIaRWSIEvp2lUH_4sh_6xkbcryzQbpHExTf_0plwl7KI4btkdiw1ipJJHYwcxEZHFfyANJVtVpLr3RSOF9jmNv7tKZD_ZapFXQxq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22842" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apEb25OqEhwjGY_-wNrZeZJRDdOnsjin2P4UuPEB-X5q8Q5Xg2Pq6K-SjevsaBZ5vuk1RNb300SXb_2BVn6ELAzUjTMWMqJJN0sueoz6IF9YJ8RET0X0G5SkhnG7rLVgTKoEnNoV9w-buZBdEBue8bHVyr4ajEi3pTC_W-VyTlMrOqsifweRmn2NtxpPmq_4Mnus9zmsArg6WeOX4dLEKKmqcNI1GeP06GIDsYJ4lEb61i53mdnli-cYy_ox07y-HfajWS2ZvYc8Y4aab4eJmxAZQyT9hzNAvzJEHDfuiNps0cCSp67aMMe9p_v5qvI-CNHwnwPXuqErgLaaFyN1-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22841" target="_blank">📅 20:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=cqPPsiM5QlxRehHcadq_lKLyB_exdY4jT9jYkPCjnOOP5Lv2NYeo7jokQFH1aZt0bRIpf8wp4vXITeibfXn0h4VJipua6gezsahUWC6GNF6CJiW_CumPcowsGBP-_XzVsogpDyKUczhwn8G2SWCVKl9C53WGxT1ukkEGm0xDcsDTW5RhrLkj1P2UEtvjL5EYMEr7TizR5gsrh7GCm-X4YvznOFompx-_6pgpA-ot6XTUFTFCw5RHCOoZQOSOR7JvTjCrfA6mbD_N5SENwK1_J7swOxLefVMX-jJdL0Ye42SeQJHXgdsZxSZQnb9iwg65Y5qtc_QfydkaTOLIbAXViQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=cqPPsiM5QlxRehHcadq_lKLyB_exdY4jT9jYkPCjnOOP5Lv2NYeo7jokQFH1aZt0bRIpf8wp4vXITeibfXn0h4VJipua6gezsahUWC6GNF6CJiW_CumPcowsGBP-_XzVsogpDyKUczhwn8G2SWCVKl9C53WGxT1ukkEGm0xDcsDTW5RhrLkj1P2UEtvjL5EYMEr7TizR5gsrh7GCm-X4YvznOFompx-_6pgpA-ot6XTUFTFCw5RHCOoZQOSOR7JvTjCrfA6mbD_N5SENwK1_J7swOxLefVMX-jJdL0Ye42SeQJHXgdsZxSZQnb9iwg65Y5qtc_QfydkaTOLIbAXViQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
@Persiana_Soccer
| Out Of Context</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22840" target="_blank">📅 20:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdneyKM0q2PRilTZBL0hBTRsdpT99Qrkl-tj0-ubo0xu5lJSjAFWHweHRRuYhpgx2e_X--tcLn9YmGhAEol_qtQ-YDdQoTUv8b8YeMCDWusohxyGAwhldml4vqhYGvxZ-5yMpr96rAc61EZBbXYgzPkHeaFg_MBO0_yzhtZ_3Nfn5HP71OsefLiCArL_uElwtymKRHR3Vf1Ca2Ud96UpVspess45doHFWBEyohEFcvVbzCwBq7P2e-pCqy_C-vPROv9k8JQ_iU4Dy_uShPihwN_RaXhvExGlHfBFRPoeA5F8Grsgr36qH9rdXU2mwOPfoi_ji7LL3lB2Mq4CsnQKIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#نقل‌وانتقالات|ادعای اسپورت: آرن اسلات بعداز بر کناری از تیم لیورپول به گزینه اصلی هدایت باشگاه آث میلان تبدیل شده و مذاکرات بین این سر مربی و سران روسونری بزودی شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22839" target="_blank">📅 19:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlRkxWwFQAZixfBE8dFYl_AIxQQmwifSDrFcZXJG6PfLAalO3DOVJ0ZIwwp_kLi67_yZnm-z5WNoAZWVLMfzNaoY0f1d52Yd1wC6b1PNhe3wby759hY3chBHOcQK54cP9HPq0RXQbvWkPIU7Kb5M9cSJ-jsL8o5njO0kVAg3qGBtXFHqR7rSWD5E8FXblWKQzarC3qzHxA6BBftBZ6AAuufrQ3y_4cTbsNoLqCaE_1vLc-MqtXd75khtE3SuUjl_K_4P6BTG2nv7VAvm7hcgBLlIOJZhoa0-8X0ktVRYcu_-GK1vjEvHpY3bUo1VucklqxQgpYA5W6NVJUlFdpHHnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22838" target="_blank">📅 19:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHpSC4CWJUtm7407L51N62FoqeGuTzD44kf6xvSAsbJaEYY6DtsC1CwYvsojsj3SLS3lJ1wRu2ZZtf0L0e2GnlKJafFHlsLJJB2M_tkwwBJk9aH0XWqcPmpVzZqPmAoqsdVWaz_2D0CWgG0PrFCdxeG5zylSO_iKG4c3IeLZZPGEoFZKOtQ2yh1rznRX7bn8XFAeJ4ldi0DaUE8zT5BPdM7kXLi36jxWut0CSDENwbq4r_urHiZtKmwh6beLDg_W0Bqfk14GItfm9hzk4quuPPWIgYJlJUjLiH0dD9YKTBktaTAn8XpLOIyTMRxjC-w3WsauxtB-azaW6zebCWOSaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=YonDGiHYt-q3BrUsKg3idqqlsHPHKjmKiROHZIUCKmib7UBy--XYkZM50AH_TdcG-6kZ2h4lqq4Y1Slw2XV9gmtH9e2ntMW2HIL1O-qJ0DJKiorfaSGhX7wsDeN8Pa7LAFiSYeCmLeYlP635k26UR06Xf0MmURg-pLkM-1zl1rAL5o_Ydvpz0QWEkwf-8AiC5SF1WtxCeJ0_cdU15rBe5TUNmt6EJpxQ5I217k9MfwKtR495VbdiuoQEqBbXM9zfsIdfFiTtA9h7Vgzn6-KwED-3ECH-p3vflVGYRjw7oc9oiiveSnUZLEnMi_VhG7_Hj17b1qSYPG40r7_YgtriPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=YonDGiHYt-q3BrUsKg3idqqlsHPHKjmKiROHZIUCKmib7UBy--XYkZM50AH_TdcG-6kZ2h4lqq4Y1Slw2XV9gmtH9e2ntMW2HIL1O-qJ0DJKiorfaSGhX7wsDeN8Pa7LAFiSYeCmLeYlP635k26UR06Xf0MmURg-pLkM-1zl1rAL5o_Ydvpz0QWEkwf-8AiC5SF1WtxCeJ0_cdU15rBe5TUNmt6EJpxQ5I217k9MfwKtR495VbdiuoQEqBbXM9zfsIdfFiTtA9h7Vgzn6-KwED-3ECH-p3vflVGYRjw7oc9oiiveSnUZLEnMi_VhG7_Hj17b1qSYPG40r7_YgtriPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارلینگ هالند جدیدا تکثیر شده؛ نسخه هالند جونیور، نسخه هالند پیر، نسخه هالند دختر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22836" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov7pFvmVcJePgrzpB2Xa-bucFABrqk6iuZkW13CTfz94Ziw1YJACF_3GivrwUgjMZgOimdjyJBWpOJds5_oy8JDX6e93psShx5xkDJoPLH1Y4Jr8w2BdJup4dCvAt0VPxh9TUS0MFp4fjGxnfMEOGjph_QBiD-Y4m_faUIEhC6cGU7xrgoDi8NWye1_3kYlgvuprbz8_jT4Xg7ybNtTZNVD1FffhCHpdMcHfrNm5QRi2OiF4WANP_oocjNBnuM5N9E4YmnQIZY1UgUKBeFVok6FdrJzoUp5Pn6AtmmlGieYY_VI894hF3ku7cD8pjqNcjc6r5lOquBYZnk_JmtxqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22835" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwJbq-RzZScOsCp0X-V1PnthUlc6-rN54sRSdZ2HNTnuFDRqMUioVn-bu6kiVEM3IMuqrZ46aEq99WNZbMy4cIW0CfQieXui7vtPMBZEawcG0kjYWLTPx4VrCbKLd0zTZIqfnPbeNQSaXgeIvHxHLyjXjpGzMbgkfG24mEw_VVQAGHQDFjlZK3qK-QoQXQZZrjcmcB0snJDwUU0AJv3GFL9AzdFBqIrTK59oWqMv1Jc5A_YrWh3AytlGXE5gz47Qv1GXUemtly9NOlUAF6dcIk7AuvVX9_JPAQ7iNhDJFn2zRECyJYM5wn8vLBg1-gyrtrZXeaPrPrpS7rnHjR5JwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا محمد دستیار تارتار در گل‌گهر: باشگاه پرسپولیس باتارتارمذاکره‌کرده واگر اوسمار برنگردد تارتار سرمربی می‌شود! او می‌تواند تیم پرسپولیس راقهرمان کند! باید چه کند تا سرمربی شود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22833" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7ZGR0q1nTc6Cuz8OOemb2nR06ZI2e1MYQX-gi6aMTE49CjfLYjpG67QTG9GeShrcbW-YwvUqoYqJ2KLguRVEJrXywcAJ2q9ZiGFNXuOq8AVBw0jXs1RyJONDfRG3EXupsKvFAMS_JYsxSTyAV6xcksSUjIn39WMP-_W5vrnFjNVu5eD2kRABURZoPTAq2i8h22-xJjUuvOItiHxYgAJK5RWEjsGlttjYuCs0dOS8h5xqWNdM2ZgCH7p67GPoa5tuW1cauyBHo5fMUp_WnqPiSluFutw245dlF7qlfBZCDUTexBad9EUdwQfj1ypU5BfXbyy7Dn9sw2s6VgZqWZSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22832" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLg1P0fuJU2gLm3IsJO5EwwRFLPocaQRejrq8XDL1yNrjDgK054f8OZuKperBucplrptmLq6G-EP0E-sF9cYHCPIwpmtrM_1uPD-E2LrCPiL8IQjgcacAzZdarfU18fHZJwpj7sxJEVLhcJ6cdQ5UfAZs2iU6gTE6-neWXVP4mfg3IpLDis74W_DLXFlZYqdrvAb49oZkE549gbxJsQX99NdfgshsOnjTzst-NsA8pgWE9DHuzarakrol-35bixE5b0RZR4TxwhX1YBEqTW75Wrnc47l5OLLx6pqVQD_F4qry1cKWXGAmCkpPQTuW2VO5A0rYO14pYNLW1ha2binqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛‌خوزه‌فلیکس‌دیاز:طبق اطلاعاتی که بدست آورد مطمئن‌شدم‌که‌منظور فلورنتینو پرز همون مایکل اولیسه وینگر فرانسوی‌بایرن‌مونیخه و روز سه شنبه پیش رو آفر 150 میلیون یورویی خود را تقدیم سران باشگاه بایرن مونیخ خواهد کرد. خودِ اولیسه هم در جریانه که پرز میخواد…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22831" target="_blank">📅 17:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndMniKsFWJi0xl2QG_GoX1n3JaROlkCLQ94iaGbspgXIYKChs2rL3Fs_zJmtRzVaEMHlho_X9oT2C6xxRI_I_xzgpMOSfsn-tV9z1D4yaBelAu8pRyIUIh8KRmigCi9Jk2p-k9JZduX0_M99cphNhXU0qBGpN1LKXcBpWUkdZmVY-IqPIrBNHo4xl6Jv8Vp1bGiWz9M4dayKWPdTDwk08IbfbeKanxfaBIO0HHF3P1kasMDJR9PpiwP2HG2-YNnw80FnkPePZDhc8WkiN8RO3DwDpmsBzQobjzB8KG4K5hmNzG3TjNYJsrCO8agwqASYcD4IdgV0Ii-p0p-68tgTTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خوزه فلیکس دیاز: علی رغم تکذیبیه شب‌گذشته فلورنتینو پرز؛ باشگاه رئال مادرید بشدت علاقمند به پیوستن مایکل اولیسه به این تیم است و قطعا در این تابستان برای جذبش تلاش خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22830" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976cd07773.mp4?token=essaNsYJgAhVNO5E-GTbyYwx3pJ4kTYKCediGa_AP0UW-dVVPehp9aLoK-o0saTbHONo14KmBjw9jZTqmYlzt6N1lvp2mXsNLKogHo0rD8WRaSiFx0oB4oFnzyBeF1C4SmlVC-tm6OSO5ygX3XkRuwmunOTGHz-LV3m3g7HKiFZbVOB0FgYd-uIJep0s4vl4heCtHAJnyla8LSJeXGEMLGrIomW2auP2Lgx63L1h7yoXP3Sh5UFAc1MAVYQv7qzeMq-TKr-aOZw2VXxdxlTWEHuoBmo2TtCZKA-QH_1ZHJlhC5obm2CjKDkTzFIqC_d9fo2UuY0uvMhFYYQLVJrUTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976cd07773.mp4?token=essaNsYJgAhVNO5E-GTbyYwx3pJ4kTYKCediGa_AP0UW-dVVPehp9aLoK-o0saTbHONo14KmBjw9jZTqmYlzt6N1lvp2mXsNLKogHo0rD8WRaSiFx0oB4oFnzyBeF1C4SmlVC-tm6OSO5ygX3XkRuwmunOTGHz-LV3m3g7HKiFZbVOB0FgYd-uIJep0s4vl4heCtHAJnyla8LSJeXGEMLGrIomW2auP2Lgx63L1h7yoXP3Sh5UFAc1MAVYQv7qzeMq-TKr-aOZw2VXxdxlTWEHuoBmo2TtCZKA-QH_1ZHJlhC5obm2CjKDkTzFIqC_d9fo2UuY0uvMhFYYQLVJrUTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ابوطالب‌به‌تیم قلعه نویی:
شک نکنید این تیم قلعه نویی تا فینال جام جهانی میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22829" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz333G9L1ORl-FQMaXB1-x0XPPsDlIV2a81mCAqRm6SBpEq9G2D6k2ndgvS9WW4CZu7fpOSaOTW8zV_krrJIRvr4A9JJ83EEWn5VOyOvoF0D8YM9o0Ff6nriZtenZjRU_2_JJBrGvBJkGcL37LZs-673oWTmtLbFArXzEDlE9dCHRzjzeS5C-9SBgyUmI24jwoXYAh3OWMFuV4Bv4pN7PVuagMzgehEM_0xErmNTyrnpCzbZo6YNQ1hrJ_zft3zqx5g3U1MOhxkmnR3AO3HBv1FuRVyXxan7BHMx1Tk9lmuRQQCuDTmZ-vqXSbXaHBaoyAb2JGlMFy08c--O1zu4cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22828" target="_blank">📅 16:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVG7A-mOBeGOiFA0Gxbqtrvpl1MTcGT5WX30MF-f9ktJGghIcvpNZszexhwp5iyBW2cTahPnLx3jYssw9IMjXjUGFEK10oGxi0GtWr_HJh8yTSX65w0HIt-IrS8VZYoz0bXJhq_rS_Wsoobi6PVzNpswtyzm3BdZfVUjfJEtwdWWwQsGjuLKYiApBkxv6f_F0iu1lznlOcT4kg86wtNzAhbaGyyElXqdrFIeHKzmGmH__lMvKCwp94j0DkPd7F_oPnP1-zHTMP7kgbRL4NDe4GY4KdC6iWIlqBJiYjLEZGfA1sHTQmOZNuxOLH0d6ZTpwiE2LSZwl5HxzRmdJiDlyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22827" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=KJoYEA5h-JPPgrZr1NFiNMenF-n4NO6mbfW1HDhamhCU6nCI6f0MF7kHlsuM3tgtva77uIaNneOpPVTQ1vAQYjPYK4jKc7D3ZaRGBt0KfyfxyexCKWz_GsBj_L0TiBALoHdsimSs-G0MqbKx_eiFwXhrG1UXu1VpZd0CQrfyTUaIlFfNR56rVq8ZWNdgIJ15Oylhoy8ifgKsQfd9ubXU2ON91YuDreekzhsdtMxVlOks0XAXHrzWmfWUjrRGC1BZu2Har-mIfwWkGdIr2gcJo8B9HZhsMxqaW8-TAMa5TmPwe1fZbiddNp-HtI_tO_wLN9wFllf3SQ60Q1ODWcUh4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=KJoYEA5h-JPPgrZr1NFiNMenF-n4NO6mbfW1HDhamhCU6nCI6f0MF7kHlsuM3tgtva77uIaNneOpPVTQ1vAQYjPYK4jKc7D3ZaRGBt0KfyfxyexCKWz_GsBj_L0TiBALoHdsimSs-G0MqbKx_eiFwXhrG1UXu1VpZd0CQrfyTUaIlFfNR56rVq8ZWNdgIJ15Oylhoy8ifgKsQfd9ubXU2ON91YuDreekzhsdtMxVlOks0XAXHrzWmfWUjrRGC1BZu2Har-mIfwWkGdIr2gcJo8B9HZhsMxqaW8-TAMa5TmPwe1fZbiddNp-HtI_tO_wLN9wFllf3SQ60Q1ODWcUh4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22826" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22825">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InJ9e5xxdBQ-fOQxlDaQZ2lMUVnN-uvnY6He8ZrGd5bYAEGnGrs9bqpOmDIEZm_n8H6HPAK6sXabSm5nntLVIM6t1cXo_ekUBMqhozng8agrjS4KbtJH4rOojwjbBTMfogSj6Fa2IHvYJxUc1gmts_mHjVip6CGkIUvYFsBMiS5u8usuKWdBam0ld6zWovpgUOyez-T40HxO_qGfU_8a4pZ-iueEb4Y3N4rCsnLGwyWPJLi-mgW51xD6t2n8PEBGEtJVduQ0Dw_tBAJLOaPde5-2RbLMjiGNc_2YSjoocnz8yNLqbilrqWriiN7e8PU2zXx7kAvL8D9jCSvlPXub2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل هفته سوم رقابت‌های جام جهانی؛ از روز 3 تیرماه هفته سوم شروع میشه تا 7 تیرماه‌‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22825" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxinR6Qyg5yX8A4Kclnr_8SLARlvTB3TMxnIxIgBXdc78uhnH_2EFw8gND9zQg27xvm8SEq3zfvQ-x-ZDTjeDOPgfIuKMPa0yc3XIlC3PuRxJlsCfxAPyNGOkxvQGRgc9mAQO4I2Fe_QH1PuHFWMwmz_wJGG16K2_Ett3jvoE9MafIr6hSO20Psl2C8aSDrLYx0rMyGiwjkAn1GplSVesHuEww2RH0QHIyzX1k8F8qi-gkVJco45ODljhpDY6W3hBRg53X_CvPMELu6iKYpF9iT-LLPCdq9WpMPL-xVVkSsoDEcMp1YHiox32yoSXu4K1H_o7nhKRrQCGIcafoFHkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نشریه‌ کوپه: رابطه فلورنتینو پرز و خورخه مندس ایجنت فوق‌ ستاره‌ها خوب شده و مندس به پرز گفته هر بازیکنی بخوای رو باشگاهش متقاعد میکنم. ایجنت ویتینا و نوس همین مندسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22824" target="_blank">📅 15:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi08_l3UIMF1PE94p_MhzPguGChCr7MWTBFRITigDPqr2RK6L3CJl4MoD9NcciMrUlYUtb92_K43HJy7VGy-UcJRlcbdV7YbzyclmqBS8F3FLgCpvFRBnPto0Y0OJYWdWsrsH4RaiRhKmUM0WBTCR_kXYugox5Amwg5dkJUKDL5SFpzg6yvB_oXrCgP1BL5ijnru8aqVaIrTml3OAdSzOg_9Ez5jlMbAsXsPBzfGsgg9yUPD7A-a7lBj66KsYwn27zk6ghneSA0f4Tr8ujBShhr3ugMJgvT4LJl-sUS4DRNBQGwyvO_CZs_x0XEHNodJwcSZrNsGENWBbOWtItJReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22823" target="_blank">📅 14:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fuz4PsruFTqWYTiQqJScBvEn3i40ud7mTF46RT_CQW-e9f3TlS6zRwj0Zmm-4Yhh9fl8rWOVXXPGIW2Lic274DPSBU9zU2pAWBkAbeL4rdz0E8Lx0AWfjo6JnOy_OG-NHQUcBfMtpvRgOo9ZkztqbE2wnEPdCtJfLNvxCj6-qk2bcb0UcFD4fdzHT8fiownDtkP9csA8ok4LmsY7_kj8b-Zp_rriBMlwyUSfEv5IJ89Trl5vYwRD835gBUrPDPfMYAYnEQOTYffAWGCoMO06dccL2-Zxyf9UNv3ysc-0SHAUUeggyMuTPIWm3-75zJAqYKZJuFqC7ALPiWYYSC3kXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22822" target="_blank">📅 14:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVJP52vUSGNdrdM4ZyWlCIdPM28LQjgrdCm4wQ3ZjFNCcUyt8uRmkyqIlI1tKjIlPG4d9D6_TNiiXu9zOHoYzhuE0XbCnu_YqHlScrHBSer2Vq3oKmKzVb2qZtwWtlFVpLqqhOx8cas6E8NukMap84y_XRkVPcMCKZPYk7l_m6nYtjueK63QeZoWmpKGiyOvMSj2siJHRINw2lLrMfqBC7HA97nin1uj-Q53-MB9UYSaIyw8w4mBbgE8fLQs9KqOhugzEiolqkB9bLGXVTsMIRZ899OcuwdYfIqUTDrAkoOKIvgbUL8OV0WC8qkyRD4Tc9Bdner-7KG3Yw6ZMu8al9XY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVJP52vUSGNdrdM4ZyWlCIdPM28LQjgrdCm4wQ3ZjFNCcUyt8uRmkyqIlI1tKjIlPG4d9D6_TNiiXu9zOHoYzhuE0XbCnu_YqHlScrHBSer2Vq3oKmKzVb2qZtwWtlFVpLqqhOx8cas6E8NukMap84y_XRkVPcMCKZPYk7l_m6nYtjueK63QeZoWmpKGiyOvMSj2siJHRINw2lLrMfqBC7HA97nin1uj-Q53-MB9UYSaIyw8w4mBbgE8fLQs9KqOhugzEiolqkB9bLGXVTsMIRZ899OcuwdYfIqUTDrAkoOKIvgbUL8OV0WC8qkyRD4Tc9Bdner-7KG3Yw6ZMu8al9XY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی‌از عملکرد خیره‌کننده لامین یامال ستاره 18 ساله بارسلونا در رقابت‌های فصل گذشته لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22821" target="_blank">📅 14:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22820">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhDXbWQ-6SqGP_KxGAEGLbaM1N5fMIblurxTyarnCJMmJNDuMacyZuJQu3LJXn_c1xRqQSVf9pLV18PFge7Kz3zb_xS2Ae2hn7O0FxPHAEMAArGmcIGgyHZ_zFlsfU6u28FtNLdlYZBuZNp_7XlwH8cJ_jiBF2J8Zxt1iJmg15nuNp0YXp6L_tQW74SGeXnebawTsEMNITIDaDyP4qkxd0r-YISvdO2qujNvEnhi7NPTZbK-AJsvALUtOfIOHmTAPgTSNQFtCnjKG_swMO-7I9eGf_G-XMko_ZSyWU_gxT4AR-FKumFftqVAq9RAqKF7MSdOh8b-V40ow5Yc2s3j6nhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhDXbWQ-6SqGP_KxGAEGLbaM1N5fMIblurxTyarnCJMmJNDuMacyZuJQu3LJXn_c1xRqQSVf9pLV18PFge7Kz3zb_xS2Ae2hn7O0FxPHAEMAArGmcIGgyHZ_zFlsfU6u28FtNLdlYZBuZNp_7XlwH8cJ_jiBF2J8Zxt1iJmg15nuNp0YXp6L_tQW74SGeXnebawTsEMNITIDaDyP4qkxd0r-YISvdO2qujNvEnhi7NPTZbK-AJsvALUtOfIOHmTAPgTSNQFtCnjKG_swMO-7I9eGf_G-XMko_ZSyWU_gxT4AR-FKumFftqVAq9RAqKF7MSdOh8b-V40ow5Yc2s3j6nhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
من خرافاتی نیستم ولی شما این بازی ۲ سال پیش پاری سن ژرمن با حضور امباپه مقابل دورتموند رو ببینید؛ واقعا انگار طلسم شده بنده خدا
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22820" target="_blank">📅 13:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBOU7qzoch85inJ7muo1nMQ-8nlUq3PmfAVvVWMnrpS3uF1JDafrhlS1jV2ZSBL6QyahkBY0mKNhbjCBuA5IHa52dSx9HewURc7vIZBT7vXUU4A2U8E76iW1oeVrlfNwK2DAlDH1KmyEnev3XJrXqf65lBXnTkzzvYSSDpkn1rX3j_JSsPU-qKPmqXe5LaPa-vqKAmJyM0XDjxfwjF7X5obmDHH1tDn2hHN9mch1Rvssv0nG3JbDe-Z1G6J_a01_yT7xrn7NZRrV41Er6kFdfeBE7ytX8OItU1poSIPGfkSRCI_F9V2UjVbyfMYxLdcQHpcbOO_wP68tUJJ1VRiiMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
#تکمیلی؛ باشگاه پیکان قصد داره درصورت توافق‌ مالی باباشگاه‌روبین‌کازان، رضایت نامه کسری طاهری مهاجم19ساله و گلزن این‌باشگاه رو بگیره و درتابستان سال آینده با رقم بیشتری به سایر تیم‌های لیگ‌برتری‌بفروشه. رقم‌فعلی‌رضایت‌نامه کسری 800 هزار یورو از سوی باشگاه…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22819" target="_blank">📅 13:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqY8Jwv8c0bXlCrZYW3mwx8HsXD5_FfW4HFnE1NljWkDbp44mbVunxAsJrIY3l1I70qNtVhMvHzdyTSixLqMJlsAspjwAvVI1cQ3PGFy3uIJBndiESe-vGqp5DGhdVB_ZlXKycJ-xhtEfglZTwrHlYvPdX9qzeX2wute8YOwm8KFByKIkQ2vufobP_R0rIKqdMaC-NLbd6gdXFaPeEeOIEBFIaty_xhTB1pHyhf0C17H1TD2K3BEM_4KD9c3wojJyMLkuEetXnFH3BV_HaZ2iOTfhn95bSDbIGeOsIZX28VeSCRzT6gDvIuglXn8wyV45ORN1EBAV9XxE1L8LgocgkQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqY8Jwv8c0bXlCrZYW3mwx8HsXD5_FfW4HFnE1NljWkDbp44mbVunxAsJrIY3l1I70qNtVhMvHzdyTSixLqMJlsAspjwAvVI1cQ3PGFy3uIJBndiESe-vGqp5DGhdVB_ZlXKycJ-xhtEfglZTwrHlYvPdX9qzeX2wute8YOwm8KFByKIkQ2vufobP_R0rIKqdMaC-NLbd6gdXFaPeEeOIEBFIaty_xhTB1pHyhf0C17H1TD2K3BEM_4KD9c3wojJyMLkuEetXnFH3BV_HaZ2iOTfhn95bSDbIGeOsIZX28VeSCRzT6gDvIuglXn8wyV45ORN1EBAV9XxE1L8LgocgkQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازلحظات خاص و بامزه پپ گواردیولا سرمربی سابق بارسا، بایرن‌مونیخ و منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22818" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVekviG3Fw3bHgpZ3zrJ4BW5sRJgjb74KIaVw8tjZ7rRjByac-2JAEAwsmWvT4ahDqxrLyfjWd8y6yQ9Ur6I5C7AImwLKHv31dsJt6dg4zXzgOFKIgvM4ReeJZNdAkI4a5g062wSzYReiuAt3-dntMHL1-5gRCYVGVgZlR--yHbq6Ih0M57N4AfuKc0d6uuIIlkKCwotFbAkcth2pBx_TLBfExyoHhmzg06ximk0J27giCV1M_BxWiz3cuKL5Kr7dcUwEH-03qRfNs4IkR9wAM-Lm7SGftl61Ir6gN5Ge0DPo6ubP4UOrSb1DXBqlJEF1F1K7JwJ54NnPrIGmWhstQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22817" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22815">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=OgRKTYSqFrAlR-A1x1oWXn4ZkTD4_Pk8lZcbnOA113tnsFa9JsP0wLfGoGqLj5Bu0bZj_ElJZ04jTWOeeD4NDuP8ulvJfan_9y-Czi21Zz_6yjhhhx0Q6_QW8IOOEWUkFEIKs8SdyYb6cuYw1mh9nPM5cJ-oDrSiSNSYoPblZE41n9GM-pyu6wRLI-EIKuFEzXq4KekgXbVWcb6TkpnmIM4qTt5D8pFQjKNRETS_KpUj2PvDgzpY7Vatfc2FggHaxyRZ1Xc-mZhoI-5EMXRe9Iek4qRpfBPvOsEHj3kAsKszSVyB1hM-marpJRAYIRP0CYGByAWXcPWbAOGy518eWCkM-D4Hvv3uMYKdwBrTXm3Xbbxx-DHFUGkOYRHz1g4YAR8hFHNJjyhIQqRbiD4UI2kXUU-fgmhjA3cGM3NlpHT9_sD-ru240AjoCaSMiljYUkahLr-N_hnkx6AZJp8QpbI6MXyyM1hRKkSzMHgfK403tc-CCEagpI58HraP2P6d9sYQBJtBTqEA4V8E-3rI5Y9YL3HQX_HBv7OE1K4zL9Tr16c0zVF4Temth2q9O3-DFz-6EF6FTDbmTznfr_WQTOVLTp9pQR05mQpr6f5iZz6tTeWAFvRgNz4KXil45-45EnaCJr-20OwY91NAUT26UpszP42lGfN9UQLB5tT_lNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=OgRKTYSqFrAlR-A1x1oWXn4ZkTD4_Pk8lZcbnOA113tnsFa9JsP0wLfGoGqLj5Bu0bZj_ElJZ04jTWOeeD4NDuP8ulvJfan_9y-Czi21Zz_6yjhhhx0Q6_QW8IOOEWUkFEIKs8SdyYb6cuYw1mh9nPM5cJ-oDrSiSNSYoPblZE41n9GM-pyu6wRLI-EIKuFEzXq4KekgXbVWcb6TkpnmIM4qTt5D8pFQjKNRETS_KpUj2PvDgzpY7Vatfc2FggHaxyRZ1Xc-mZhoI-5EMXRe9Iek4qRpfBPvOsEHj3kAsKszSVyB1hM-marpJRAYIRP0CYGByAWXcPWbAOGy518eWCkM-D4Hvv3uMYKdwBrTXm3Xbbxx-DHFUGkOYRHz1g4YAR8hFHNJjyhIQqRbiD4UI2kXUU-fgmhjA3cGM3NlpHT9_sD-ru240AjoCaSMiljYUkahLr-N_hnkx6AZJp8QpbI6MXyyM1hRKkSzMHgfK403tc-CCEagpI58HraP2P6d9sYQBJtBTqEA4V8E-3rI5Y9YL3HQX_HBv7OE1K4zL9Tr16c0zVF4Temth2q9O3-DFz-6EF6FTDbmTznfr_WQTOVLTp9pQR05mQpr6f5iZz6tTeWAFvRgNz4KXil45-45EnaCJr-20OwY91NAUT26UpszP42lGfN9UQLB5tT_lNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محبوبیت بسیار ارزشمند علی آقا دایی اسطوره مردم ایران و فوتبال آسیا در بین مردمان کشورش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22815" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-d50jb-dk4bynzLnYKOJpJwZE1sqXd8_5NAQptHxB477u0ncDDjzlRd4vVV54RAdcTgQvzBDYz9q8woM2zJ3huLkoB4pIDk1tlmihYWHVxL7nuEOIGhV8mFFRqe1cb2d2QWoEoXix8FmWzaehXyZzk3mkbC0XrpTochm6eL1eMrA8fp3LLf1BDa2j5gqn3c1x2MlJk3-KnLIbE74xJOLnxLX1dzXEcodaRgJCXtsIclcI2Hp48rXjVydzPa6klBGSh2C-4ns2EzPCQL_3ldcNPzjLPEAxn7qxJ1VOnXvj2l7M-GVumj7-0u_JmgOlyzqTIG5JyXSgOmpfoV0aVaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22814" target="_blank">📅 11:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNQ3PAuTIVAWmIdA9lqIFlur0slZGcPo5IXsKz9e-qrgeEGniJVgH7BrW5LLHxmBhuHD2UKarCFSO4x1vRIkvDdSLKAkVcp63LGXBPD_JvdzqgautB7EQO-d8lMexw3O9_9yratyro7xKn2IROsmSkC-8trvymVy3GJiIMEiC2mZGpyNmq0anvDeM5SDGlrnbbUFv7AMazn0JWIN8adK6dT1uzh0itII1z16As84tDM4c_Gc0AaJeLNBrPjob71EHNuvfy2vJKLaPGh_9FsVAyWkJzILMWgZF9pUNdOtYNs3cNuHKn0q6XQR9jZIsRcpod62wevyuicLYvzlzVRtmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت باز شدن پنجره نقل‌وانتقالاتی آبی‌ها؛ باشگاه استقلال برای فصل آتی رقابت‌ها برنامه‌ای برای تمدید قرارداد آنتونیوآدان گلر39 ساله‌خودندارند و سنگربان سابق رئال‌مادرید از جمع آبی پوشان جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22813" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfbZWRDJYNVlAZWYc_7EGbRomYBvuV0ZL1ZYplQWjABUMQ_8zToKli1Hj1DHGSYMleRDgBuknZUhRVpVMYk2NLsBUz7xZptgZJMXhyxX95SOVNrQlvi3P8K1_v8rfNFCYE-gTqr0Ca-35Nd_aIDV6SGypitFZy80coiPuUZ5mn8a38OmqetQdxuFHcUG4BKTv_FwkoYDUMmcLC2B_dZFJ6Ie-A8M7yaHBOv7vtk1G8OZ7c3VFemMZlG4kljY1Wi61k9ihrBQZijMoKuQYt11kG-6GVmxgt9MewJIFcGGG82UrHx0PZUvVtgW9icTnTlDA-EMvSyMdGfdm6bvP3Mzzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
👤
طبق شنیده‌های رسانه پرشیانا؛ سروش رفیعی هافبک 35 ساله‌تیم پرسپولیس که بازیکن آزاد بشمار می‌آید از دوباشگاه‌فولاد خوزستان و ذوب آهن اصفهان افر دریافت کرده. درصورت ماندن اوسمار در پرسپولیس قرارداد سروش با سرخ‌ها تمدید نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22812" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koLtEN6nVC9GqHInMj4atmtbO5NklqVb_WZyVZD9DqyGwSV83cJSh-MWP0yvs5rWzEUL3wX5YtbrgqkcLUoPv5J-JKeGv_l9JQAFVlmirzoo_f98bwa7HhSroI9-y12Lx3K4TIzxk1wnrBDxqTvOVBafzezwG0bAx6X5b17_QIcGm4TazRLu2sZVK_OM5_ZX_Z7_w33_UW4d94KQ7jJAuwQmjTwmYKC_foSabJ1G4JAUj64VNd0JtgdxBthn4LA-HT901LKqbgoVG_VTJ3cq9QZcm2S_YW4tZiH2hEmJNb8HBZzW_M62tFT4_xmBcaiGjxbdgrHQWuk1vyZfr2NcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22810" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PG7nJQ99iBXJ05J2Tu2xIIdgdyFVAzuB-VpNDMX7iec8wV-at6ZQzux7LnxRbutJm4vGZvDZxgRILEPf4RO0DW0t_T8zbSsJ2i3mahNth35bOGrEkhH0b3nWT6Xv6wGM3sVLGIJsS7uo-OP1Ep3YFovYIUg6eM52Ay9oE8D7MGLdTTN6dFuNK3-QVrebSAls7LaU-qCHr6NiZzGmH9-GPdRp6rIk91VXeQZtaG5K62HqNwIH-WMFussc3bpBAgyyGhOjjCtU5jVKQbEBcuaDKq5vZTwIyEnYtbPo6IPI52ebFc8sSY_VhaAiDOy5O0B-HQKf93VS76LoAT09gIOiAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شماتیک ترکیب تیم منتخب فوق ستاره‌هایی که مفت جام جهانی 2026 آمریکا رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22809" target="_blank">📅 10:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22808">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwKyC1ZH0XYdvd1iltJi_gOFV8U_SKNdTgxPCltkldeU0j4kalXgxrcBSDOEjQ7Ik4MgeaDwwjqz_Aw_RZ_33WYTTHkG5l6AffHDr8Wm5PjdFk32hyPHQYltlW4VLNkWjsdIaGbx-40eMCR3njuiaVtkRPmI9ud7yheM7uNbEphuV6QsgClo1FvLvUFs33wMIlHKUnE6LzFu15P_y47_oahM9NBi0tzr0NgBAyzDCoAplYuqvbn-LUdPEUO7c0EuilMMZLCbowCubnDVQO_M7UZGWqFk0PW6Tm1tQ7Wy-_-98tovfVhTwLGO3uhNBbZOegWVXMBRarZqT0OvJWFd4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/22808" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u69W-SYIGPedZvZ7wMIISDtjoWP6AVOj9NNbfZVBm-KI8eC6G_uaJzjwTrg2soFrl9HyWt3luJqLEnS29XoA7TY5FFBsXdmEDGMpYSK-APtCD1IXHdsqbJOw9ZDiT_xaVZ4NCV9vkLVzKycso8QPxhTdAJALWlXVBDELYC7YjVBqgqwKqG14hYkpub7_0z3qHAWp9swc0uxupg3p1O0LiZtlnfxnIJjPmfWRuncUI_6LAxLmT2oiBU308aVsa0ZNwLS_osWS1cH-osree2UmnaXsjzkrFerlSr3OYVmTCG59Sv710ZHBUw_Nz7FGQfMqxNZX1VFWJZ4Jn1qIidca3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TklZekdEoLcOdX8r6532kacbMNZNE2tLUHoA9i66A_8v3zpIJTiT_yEbtazb8G0ppWibf45Xr5hDLNeFKXqKeBPjZaSbPxelIvxy1QAvAO6nvSk36QsSwO_tOGAbvANyUS3zIXfZbovSWST5xEAoNoGUkzxOR-CUgZYQb6X9vrIX5vJcu0Mgxb7gCKNBg7hbqLeKhRwzMBJ2Ejm5E-YoeUW89FufIAs6jeYV85A9BoAYR_KXAfqghOn8f33W8ZhxDhUv8Li_hBMpXUkLWllQkuDc23HkSqkYvprI8VaEGlO-PDyyaiFRQKH0Z-uuEIpdFq3eYkTnX2m2Qg1dnRZd4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHXBhSN6UPrPJiMolTmLmQLOsR4fKfp9ATtglg_GIRjqZ_HQioQ71i3aJHOEDNsYqylJMsRJjRt_ROlFEoA_o6zSoQd1UH1YuXSrhDi5z4o7xSe4YcbKRaly4Lt6vCHQUnmC_2Bxyc4nxpUNXbQwvUZDEhqVsvX44-sElRhY4wY3RDtnd4dm95_gAcuJSM4CulNnE86Uf3Q96p1jd9LLhlfMtO0YbnHMFUBk5frwPbprUkQtJ6fhvu6yxibeLE6Cl7ndlGkUTr-Z4zLf0bvu039Gr6tHQopQKKV4n4ymaYA2MS4-pkIyWh4G88kCOfsHKHYtvl81-DacMPmQZlWSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEZfsMK0-TeXSDOD-bNuTn7gA2T2fDDdIMYZNwYNXCie7KyOuHOZCxfVC45WpbIyxSdFNAlcEI2YrnPzFXtLfExKgXVJv8k5op-MvokDLm9bJ-jFxx-okZUvIvgS5H96g7Sdej6i_kyrzHh1zaZp05XWa5hg5wxiDICJksZSObXh4Sr7M0wUBHK8ms_6RFOkLYaDf1u7lRZFpEErqoBTE6mKZC9ZcX2-SKCAFIW0DFv4sh45UQfEaFt-ArRby_1P_z0TCPiy2r5ndz9KTbr076I2xNYsF8HDMtDHKI4Zohxwn2AeG3qQ-4d4EPHV6-ohtYbP_jazc6exhHX_o41oPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqObTwwX-EDxaBkSzRn2mVP6xMtuvKienkPxnYkNSqlmQqbfHZbPlO2VL_lnxc80QksN-NldQSj0HF6LdVuI4pyP8tcCsG-9lTLcMNtpMNQq6Ibp2n77DanaYQt9lLexsXztXxwlNviWWzAtWE9gaYj7J3-J3O-7y9olNcDKgbQeVeSZNYTApWCVH--c_VG4cXTrmiHPDcetbh1TdBjR0QIjmBv-gmrPNo58Z6ji3T3cKkivgmsY0YB7kd6dXfEQFZXJRJVJpnZN3NGJu4sXgG89olXQ_SqfFCMb0XT1kx6gS8gQwVaRAKM0miSigZ4N5IdQ_VS1YajdGmzOcvL-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
