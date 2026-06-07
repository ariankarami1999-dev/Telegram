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
<img src="https://cdn4.telesco.pe/file/r6I4cdydSYO42GBGHRdQjjk7g1N8eAAqamNc-aGQSkFTe-1oAQ_nGMDQDCu9eXyGWiw04m5qGww-yBCcOwNjDsjCDLxmKDDL7eAWtj3q2fG2saNl0W5y6lziIfCnJJ03b6rG6jqImFdDLPzML_oUpH-JPLJHh268aAyHjfz8EWVgKFW12jfhdxr6OlMxhFiJhVKyzxdDUjR2ojH1QMMmjyOOtM3nZK2XUY7Zr48Sd78EilbQNZkC270__tXFqdhTXAufFQYrYtl3QgHYVWgUK9omHi8bO0UTtt7fIga1WdBbH-UC-qp0Q36oWdvTuXyHl00T8nl3VjZ6A_0fod38WQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 173K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 03:30:22</div>
<hr>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcIZKiInmeKjbz7gucWvpbmiH-8Jm1qXw_c5t7QROBxAg02RiFwLoR6yQL9qwYWtKPmXgs2AMDjYbjQzjvU-QgwWpyMtr03k6tptKbzXRMdFLI0gXi1vQMzsHunH8V5IvOecny5d-plp_J6YofntItmxTZdh9ynoIy6zCioFiZV8X-80M8RvMm5rCmtEYykH9Ucaqlz7s4AheKzZn6iS4LmlKDe4G-e2HVmDVcAZ2rGPfLJtnzmEwsMfZolF74anuO462lVFwDgoAVszKlmJ7lmf60o0YUE-9BpG6opaXrM4-QpqQEyHyoX65hOgs8XzDcK1F_tAYykYX4jDDamBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
تقابل شاگردان کارلتو با مصری‌ها و جدال یاران مسی برابر هندوراس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/persiana_Soccer/22914" target="_blank">📅 01:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_cGA5EC6fNsiEC6Qt-xtpJczXqgLl8Lnx6RdJyKz4MnkXVWkSCaEXKM7EVEWs9jJ0osaSIxqXaTnlWSzmKlrON8p3NO6fIhgCgIjT_F4Qgs2ENSbz6hyFRmmMBgpivZZT8MPTuGkiGGgsOjXqLfIPYNwqeB-qaLI6Vs-jy2sEi35_z7YYhXnje-aJ1DRw7vkORdCuIzM3oRmsK7yWE2SaiAC-wvXzYRU_VOeVJNM7eM688R5AZo-Y72eYybcOqJcVSMygucWGIK3IVYQxKqlROcnsg7b4Siin6BYt96LfX3_aoMYPIqn-NAdAFeSrDVdkqbfD12T5qw2Q62z1qllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از بردپرگل بلژیکی‌ها مقابل تونس تا برتری تیم ملی پرتغال برابر شیلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/persiana_Soccer/22913" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvLLkO536MxvJoQ7KU1-KR4WS0P02LRidK6-ZYsBtsgBCJhqzJftDuuasfmZFnYate8GFC39tMDkOkTe60w7SwT0iCZvgUizLVue9KWqMKvUy391C3xyLD-9mTqrZeVBYAU6PU_XhrlKbY5aIwTY4X9koGNvWketwRmYd6Dy_2WL9UH1mnmgrYQS6gWkl0ptu8KOrlnGgR1Hqh4PxDinbXnRFg9F3pXM2_7_B6xV-ur_9d748Bn7me6r0JoKr9Wsv043HX8wcztNsNtESJil_ZM7yT1WKRpqfIbr0-mVp9aP43Zser5cAtAQOE7IZyfYpt_CCB0RTleT9cSHwP5Xnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/22912" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22911" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22910" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22908" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22907" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtB1zB68hpxpTBnZKUp5x-vIzcV16x-5mY0ZkcapYPDOAqPC3rkj17NI9WhOKupnFt2we3wSseISKmfQIgnUQ89u2MMvY94wYOFwSjMj0zMWc5YuQQ11mRzhpH975mI473nyZz1NbYx2I3dbDicPNO963_-zlxGjp1WcDmmBtdu7iO1qDmRcVK35Gl1u5VbD563aHPS8IXcXaoKkoLEWEhQiwXbtc8QtwftbPpjF65kNcjENzfa4Kg4sbPV_GrVXs28-qy-uZw0MJlrKkrLE9k7oJraNQGZyLK1s6u_MTxikNKl--TVDwii5hZeaolf7aipYKoe5pOC7bJHJhFtjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
#تکمیلی؛خوزه‌فلیکس دیاز: مایکل اولیسه از طریق‌نماینده‌اش‌به‌مدیران بایرن مونیخ اعلام کرده که بعداز جام جهانی 2026 تمایلی به ماندن در آلیانز آرنا نداره و قصد داره راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22905" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7O4ED3dK706BpzIKC5oRiik3YNibmNFsiqwCTfpfm5z1fuRmcLhdBdLHBD9cxlzgwqHm-mOU2X8vHL4ZZACgLjbLxbzu3e8_dSGYlf2NWZIDxP3xALUWuJ7picSkqDaFAYAEXtYTyhxSkEJFGUFB254lx0OpPXgYlkzly7xfIS2cV2IIpPntYSFnZsO36F2-pVXG8JbPu6fbo_vrtrrqDhODVPvK7V_z9iL2dUhnCYSULGYYdWUoGZHSsGsUISuw_F_D4_d93js7WYozU6375ZXTL15mDxpbVMxoS4QW2o1VW_xeLISisiwT1KQkCEckducJYIPj_nRNuC7Cxt0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق گفته رسانه ها؛ یوتیوب بزودی طی روزهای آینده بطورکامل رفع فیلتر خواهد شد و همین الانشم روبعضی اپراتورها مثل مخابرات رفع فیلتر شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22904" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/22903" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhsJtp8HlHJ2ayvkDCnPaLqnzk_MHpLPjJNujYbIiRDJPcPpiAQ8yW_HCvDDRSNxgP9MsMXKpZPoygZqNM6KndasVVFSXT01jHY9yeFOGk8DexVZV-LvzGvwXOHv7BOxqkAMK4yYKQwNaXwoU9CYtEFjifjTVcx47zyjyJtqJd3_wGNvzoRTolxwsujrteXVXhz-g9GaAg9yWEJnkhQKfTzAJnVD8s8Jm0XUYxxvqD__hPpsKJK3lb3eJl3LVsg_N_5ALsGZGdr5gD6PR0kDBq1PGKDHtaW1Pj0yHS-fLjSZlWDyB7oelgnUD_-zbC7Hu_K6NmGf640PA84qnUfQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22902" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22900" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBSAeiqmRDWubKHCtpghixLQIz_veQ4FEuccDxi4Y8rfgiCXcsJvrd07LrQkC1BdowBN4Ube28re3Rlc7ddRml4gCBb3Y1zomIH4e_0PrDk68A--yi3Fk5ABmb-VjlyxdZ_MTHhKun291k6uoKs-EMvKtA9aQVCh1EMxLXNXKfZHAqhqlsJU6HRw6x_5IvzD9GxYCDkpz1szYNO2enrbbczSI2mbFS8JbcpxY_0lDXbiwKomscqp_1A_2UFCyNzEf1Ey5atQGJ-hnPsG3Up772wFj3Cwdh81CirJQAwRqeXv33SncwnJ0Om_7G-dQ3h4e51PetYTrfa2m2Tnn06i5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22899" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDcjEtjTflPuTBoFKo6EBeWO7_TDG5NDKK8kglSccSpxIfoU6OsQXHrC5roEPlFK8kNmUOYvAulwQTO9mRdnO-R59_JG9DT_GZMPlyXEu_nXPG4skK-a9aZ3rgGqumnUaCpbgeos4P8-vbDbPu2RlAIRTy8qekdM0t-G3EaEh6QCkiOxJQWCCAQuDrQ05-ukdOi-_fydUymF7wk0dIgOc78SUlhdTHp8OlyXJnxdBQUcONUzBTgB429GwgIQuoOw1SVCmHFR2_W4URRZvlorkqu_HzW46qK8d_p0t7wda65ZKAgVh4VKDJnhWtHVM3dfjTXbxwnwqP85LT9OvKp6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال با فروش جوئل کوجو به تیم نفتچی ازبکستان‌موافقت‌کرده و بزودی این انتقال‌ صورت میگیره و کوجو رسما از استقلال‌جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22898" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22897" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22896" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOBQ7IFImwswuiMZKWw6SQLoFj2a8hD2TqnCvVZ_VEdF6K3e-iGDwtJYEMevV8DWcJlSeb9bvaxhnFS-Vvps3gwUkvueUaCEIH_EcYtJvJtuW39F7aUiaT9FNjKp8-VM4BNPRv9Y4IAoYuXrU041rRnvQ_aQLQdeDyhoZnxFly6bZSEsesd6JZtogvQZBy1ZHpFW0-tWqlJFTiflr1yxDTikSyft7ivGZ1GCc7_51c2AS6O1I36I67t1-6FjO7NptpfYr6SENI0_YAWjocpVMZ97FGQIzDtnTfQbOFbv1QCqQGmI-EeWOkpkg8n3b5wo6NUbZmpAUK8KlDT1gQMQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22895" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22894" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZn8I9yTAuKXWI-l0YUXfAus01I95Wh84w49JhZnVBSEcct8WFnI2qQjlMtmpspoACCaaSgmW6xFHW0zZjiBwSjTy9nlzyThYEB8IEXvuuuBw0bCUGtjYPlQv_-Exo4-cFz2LcSttg2GmqNsk31kqZLd9hISI1kfnA3pP2dip0lQJu8PVk9khN6YoasLfZjHId9BcNFRC-6CkZlx4f93OZAjRvhdGq2YTz9zsFUWoan_TT77IyCyTibL9uhvTm17OekwaPIiWEXbhsQJdsk3LvyR9P8jhH0rBjVq7l0WZWqWm1dPVRi99Z3FIHMORDmvXGJD_5kFjwMU2XXmU_JLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22893" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnnJd1XxBkjbgBWIDQn3PZRrwELIEvv-cRgmq5hGXqWJhjKn0xjYM4qqXJ16kjKZ8Feim5rISj9kDClowpXr8BWaO0danU_yR_tBOb-URd-5jLPX0Y93w6MnTANGwATn8sin03adfKJEDGtcjU-GsjTT8BU7Xk-jY24j86XMWDq3vZU4-y11zRHaAxpvCQ-GteH-0OMIGrgj9HUWrGwLtOIcBvS4b1IGPNi8-a78VFEAuGJziPj4oQBbTWQD14nmlPG6aCvwafGMlrOCtYt4miwAOQD4xBlTEaEAqWjiD-jBn3dSgTie7fHclgnXPL2m2d1Bg9ObQ-CQDU-rS-3uHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22892" target="_blank">📅 19:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWI7V8WeD7DC9AdWdUP6dmqmWHoLjzWmInLDkRsXAf8Sd4PoHdBVlmwLcwmeE6JDxiB8cS24gcrpFeXdJCYAHz9S4ooyLIdw4QOukDswfunui_ilZJlBuYyUfckKtktkoveTcSexMn67MqihqdW56qIZzh6NjHmzh39GcA6roataLzpmhbWPddbCbnBvWLk72FkctfFI0g51mybUZ6q4M50pnUXUWcjFQequbeBQ7ZeFGogI4g5u15hbBSzFmSdiC1llkgoDEi9CAO69ApfaIXyrwTtdW-KAV1MPVB0kewIqYrd_aa3JaZjuyGpX1kmNqdQER_O5FmBYSyNbm544GdS0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWI7V8WeD7DC9AdWdUP6dmqmWHoLjzWmInLDkRsXAf8Sd4PoHdBVlmwLcwmeE6JDxiB8cS24gcrpFeXdJCYAHz9S4ooyLIdw4QOukDswfunui_ilZJlBuYyUfckKtktkoveTcSexMn67MqihqdW56qIZzh6NjHmzh39GcA6roataLzpmhbWPddbCbnBvWLk72FkctfFI0g51mybUZ6q4M50pnUXUWcjFQequbeBQ7ZeFGogI4g5u15hbBSzFmSdiC1llkgoDEi9CAO69ApfaIXyrwTtdW-KAV1MPVB0kewIqYrd_aa3JaZjuyGpX1kmNqdQER_O5FmBYSyNbm544GdS0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شنیده‌های‌پرشیانا
؛ایجنت‌مطرح فوتبال ایران که ارتباط‌خوبی باستاره‌های‌خارجی‌داره؛ بار دیگر ارتباط خود را با خامس رودریگز ستاره 34 ساله سابق رئال مادرید و بایرن مونیخ برقرار کرده تا درصورت تمایل او رو برای فصل آینده به لیگ برتر ایران بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22891" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22890" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWHnOLi99ZPVEt9JnxVZD9aSZf8NG8jwCB6p4lqix7uyXRq1IibzFmx21QZ76qBpZhxmJHNZGYSfGLVWMR1Q8PWneblZCvZHYKR0yup2n3Lo8NRkf5_xQeZStKi4Wn1i-Yjs5SMUELrJmmseXCk3eLFWgnJrRN4nSE16UEeHc68zL4kLnV7oU1CO6fQ1E_s0mFWLYoN6FAwv4pJTZWOVXwEj7aLN76p3DK8CkH3uXT7CaKCqPBxnScZ2sIxeLuqJ05U2x9yeViXqjVLc3fRC4W5h4O18lXG1m0V2F9O8RCNkaZICl_63bjPpUAIsYM5TMxrsLcWF6ISqr2ySC2b7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22889" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22888" target="_blank">📅 18:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miRA47l1wWbczRPUquI-zCnK1mQwugzW732wHJKDaXt0bmvQYMjCdL5HzcbjLXgc6rSap87JTSKD6d6XcaZV32TQfXSqGYzVdI-glSWLyzeF-a3PSPcYBZWAq_hPVK8WbtbFv1-3u92bS1_hy7KDB0fvtsr5Rq1mZYjxLZg0Bd7ssy5czbLrdCWhKAJX97kVL99K41FdWCAJi-xO07PdbugasY20EG6Un0MgYgFk7zJzJlztexZlfKL3RF7H7pL1rMjqjsupOyBO5Vr_S4NxXH47Gi0IUt9MKnD_ztSwvD71Z3B7uZol2u4PxzZpl3mNZtDb1sKsTwwtwxtn9yGvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌ بندی لیگ برتر بعد از سه هیچ شدن بازی گل گهر - چادرملو بسودشاگردان مهدی تارتار؛ پرسپولیسِ اوسمار ویرا برتبه پنجم راه پیدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22887" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22886" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22884" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej23QF5MfeA6CJPNGUhPCrUNMsRhyAfOy-4IFbIQ9aetVkCPi_Ro_HG1l5Nqy1awhvZ1OyIP5HQvd4jUUHjNwOAWuT3KMc1vw8PKRRv_-dGGq-qByVDpTDrEIOuIqNpJellhfL1hKVbbDsCks7Ctms-fE_7w5ofKGvBOo0WkYBqEpYqxgbAa6jsMNuWgB-hBuuWwm6UHV2-InWTkN8dU3emtirOeahHJ1uIF1_ceHHCX9jJsUVVis1NbWN7WWQ5HdMop0DbVedXfS9FBULO8yltr_K-_-Td-f8Q1VK6RRNnrbiVgpBfy9fsqaY-tgczbMM2i5XDUvx8o_MBsPyaEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#تکمیلی؛دولت‌آمریکا: به افرادی‌که حضورشون درجام جهانی ضروری‌بود ویزا دادیم. دلیلی نداره به تروریست های جمهوری اسلامی هم برای حضور در جام جهانی ویزا بدهیم. ما هرگز اجازه نخواهیم داد پای همچین افرادی به خاک آمریکا باز شود.
‼️
مهدی‌تاج:اصلا درخواست ویزا ندادم…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22883" target="_blank">📅 16:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRARahkgY5wpPf7qKrNgEAE0CqxEHndl_j9I5OdkcH2sy9XHoEEN2qwdcsYoMtDN7D_TJiDGKC33gOLikfJnlVriuhevu0riUUJUsCb-YnbRaPNU0iut65Gme7kbed2PUE5HPzOwvaZjd9_GPf5Ixf9eSfAoazLmNUa2H78fAiau1tbl0sUAe6iJw6awnYrd_P-7qTmPyYWKumfbab4qDUp4IWoQedSRYv8Fw-nJL4S7ZNHghDsJXw5k5K9qn1R8SoCJStNLnU2NASUY9SjhGDFYx-KqPHeTChSJZlqdZodn_E3hmHmQ153Ax9wP_qa4wtOGGcyb8ydUIN9zqqwCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22882" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeFm4WApxBatFFsWjst2Rj_rhrw2sML-cYAuG2VJr_V6l2A1XRkxP85qymxgNx6NF8I5Uvf-1loeVifvOoYk2zDSrtfM_zfByq8xT-rnODNZ8hDtI1rGprfwPqFUu9XDpQNZZuvWKHqwjDXOfGYt37agBkSeePCSTTNuLDd3pl3B433JHTwJolntPACzmtkaJ2GiVQQBdAQ7NzuEqdOowp_K8PoJ0vfLakA7SKyPtnyjIYk0YkYdp55TabUGt0WF2Mb9k2KzVHXnMAvkXYLO-TCYhZErWWBoif5CIBW9yOqobla7JBbUshclt5kaEQHRmOAD2tmhrtKJSrws6PKsYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22881" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22879" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMjTjbUzpVCnqlF4IfKjEttCk6vPF2PDCJoS7_ZiNj7XYZoSj0bJvB79RxBC8UiPUV3maDjrqLxkqWJRHLOeR0aEbS0F0s9QpcogyoqRRL9AQz7JK3gtgj1Ai5JrQVaMmrrVBaJBM3U46amWtfyxcR2BUo3OWS8B9GaHMlrlmpgE_bLwvHjn_LwDc_ED4eNhgRvhEFLtclybROrSWZoztyXEW0fhx_kvWYxhjyHKlpB0gWny9FSNIfS0nU1SMVFvLRAiHDnlamhQ6EX5bZbQJXaFvX8LFFpKWhhp_Nmc0S3-1Otel79d71aYYB-_8ehyg8MF8MSEbgG8Gn-NvaXyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22878" target="_blank">📅 14:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCm0p3DnKdmy5sEgbJktWclm4lFI1QLcuxg59ySDN3K4YBfJlvXoZgJzDM6pBE6gLiA-r6J6PEOBjXRp7XGZrNviznGYZMdT7yHVRbSS-13krcKWthhtJYUu56WCxZLAABEXs0NjiNoVS_K25wW_4hP8YxdaCTKJZ9igmJxgKR_kDqXNFdI09TT4shOPneM6yXdG6vCiShv8uC3O0INO9q3QH2ZxdI8GkBAZOLKDJleP_RJaQddjled_1KLiEgvpwGt6LaWYLXyWcrmaqLfpCxeiSIPvw8Rh6CvXRAwMHqdLfL2qVLkbj4xAk7JxOc8OY9DzaqnxU51wDqJ-8-4C_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال با مدیر برنامه‌های موسی جنپو برای فسخ توافقی‌ قرارداد این بازیکن‌به‌توافق کامل رسید‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22876" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22875" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMU1UzeLPGjXybovFUzCJLV8URnO00lXOUMO1LpRHedDR6ku2Ol7cEK-m14qS5_VbKeKNYkfe6YbaN9LKD4L8JwU405nf3wZ6JlNpFlCNGf6OwHYkjMhkh5OXDpF_BssxRokBwA4PzpFWIYcgSoIGKroRwNyYaj0y7uhT9T2Lm3b6S5lbqhHaFCnY4pon10OtFW_bTpGcLCZC61wV2dQg2rH8js0C0YJ08dLyNCGi7gXn1_mzEaZHkR46HS4KbULvn1wlQjs9qDU2KvPV0WlbaI0bD3kVzch8m20UVmt_YC-LYtRr5GlNZggOm2u9ynlT-QFdzZ58DWI_Z1mh9z0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22874" target="_blank">📅 12:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqNxC8ZQS36BDWqV5N0L5vhtFcTi1e1NM12q3YLFXCEb1g_GkkEAl4K1Szl_QSGn_eknN72QRH7sbIrg8DTKA_obSIg2beBRjxmTTRsyUrR65yLHVU_XqaK0eNgvqetaLLXAJNIeJDwJAX1z7vprV8kqJa1C2d0zE6IoK1SI6Ncgo-mr6G82521mZCAdtpw0zJdjiNgYo76aSrKW8UMpa2aiDZfbqsQCmcE_O8mClURDh-Y7Vo3s_IIYz3bzuHuKIOytVgnkll6owzPpIA-v-_YWSVyFn-7wzn_x7zmWxQH0X1kTiVYqJRurv6r7rtlDW6ezrmM5LVU34ERKNEhKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
#تکمیلی؛باشگاه‌آلومینیوم‌اراک: در روزهای اخیر مذاکرات مثبتی با یکی از اعضای هیات مدیره باشگاه استقلال برای فروش محمد خلیفه و بهرام گودرزی دو ستاره جوان خود به آبی پوشان به توافق کامل رسیدیم و به احتمال فراوان این انتقال بزودی رسمی خواهد شد و پول خوبی به‌باشگاه…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22873" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDwxKyIT6ozecTHC34_qBYSERdmAebWj2Xd33ojwdtLyvVcJKkj8VeQz6AKV--7hfhpkIT_mPf6co-sy1_Zb5t1fPfOwIoTmRfRoh8yRW0LM6NasWhz72FRapgfG4n7LaX8Y3AKgA7_6JW6rFTL7iDKpgdH1NzoOxLS2Jso1rKngPYOI4Jq99ZPzBgSTI5ZPwCj5VWVuDFs63m1aH74s2k4GuCVYS613yg11RZAY1smN-d4i2jJcn60E1sh4Rgjgmzrn-sFBF9z715uxnaqN87IlItrj2PHZ4EkSgD_wHYr-kaASYM3tmsgnqL7EHaKuvG_SUdTlfK6ArhxLCvvqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل‌نفراتی که دولت آمریکا براشون ویزا صادر نکرده و گفته حق ورود به آمریکا رو ندارید.
‼️
مهدی‌تاج رئیس‌فدراسیون، مهدی محمدنبی مدیر تیم، هدایت‌ممبینی دبیرکل فدراسیون، محسن معتمد کیا مدیررسانه‌ای، مهدی‌خراطی مدیراجرایی، مسعود اردشیر افسر امنیتی، مهدی ملک…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22872" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsN6SziF7V9dF24471M13MGOe3WM5QrAJ_6LYCR58ju3hhirnevyATNpYRz3NYmp6N0oA8uVGUaE9DKhHHGrZ_zmkqYQ4K8fb5cZjB6YmNg5Xdl0cn4bYOcFJo-uUtqgEuKLXz0kU8R8CjtU5phI8blyJa9U8Wbh4HlH6WNCnjW9y7LWo9jnayRDZYr8xle_GyvNdsLnkvkZ7m3OyxGVyjq9zxU79-ye9_m21tKbXO7v4UlakypARE6zeBk270_RkQOySHsgfZNFuTNCnHtzZ9r3hhqtqZxSTeWoCn_VDWleQ9NhGI__OL4ujkb_b2vTYkmLav4Xi34gdBSqNsZjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام رسانه‌های معتبر خارجی از غیب احتمالی چندبازیکن تیم‌ملی ایران در رقابت‌های جام جهانی 2026 به دلیل عدم صادر کردن ویزا از سوی دولت آمریکا به دلیل خدمت در سپاه خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22871" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22870" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22869" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIdQAtsHX9k9jDPU9oulIxOTo5ytbDrapBHizv5JPgnTFu09agEuP2rztBuExhi3-rRD3IKAzoKrgKmMWjO2c3uwcS9Y24_pgSk12BMUvPnIEYWLvRK19okppx38FGoa6n7kjSF1ou8L_dBTjI6bUnnEd63iqYM2wxhRw0shaxsAuRjAMgp_WQ6jd8TyF-sWl2_NFt-9iylHT-KhdmiOu6WbgWLwKB5CcdEj1EfjVjLrPpiggdfUVVnuEwhy6WFAU1nZaztXqnD3Hzwe8t3SxWKgCi-U4djJG7YLDRHwCbwrTAryWvYmchh1K5ZjVlNkcQUscCF6EYAwuzwYg_tlhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22868" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vo_OW3SQ4EHYD64uuzqdaOcrk9Ml1IIsGPta4aH5NZtuj9yAtAbOt6pyLsj1zh1fHPMrYtSuczFc17_1ObzFEtuhC_pDkz0Cjb7O8orSKt4fd-Lu_na--SLP867gYcMB57NfuK15iKMpq6Zs9m6dobMIT1dTu__QW4mjYCPv7RCQTVx_0sFSZm5ktTYJVCXBKGSp6CTadBYAPoAHVrF8GJ-uYl-3zVL5tVB99H-0QJjllSXUFvogA5Mfb3ikMPqe79vjFoyhwsejAuvN_7TTQgOGtfMi2dOE2jbmwf02Wx3VKWzbu5MBfUD51jBqK4uwRUFsnQjjo44FDBijcgQwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22867" target="_blank">📅 11:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=boSnJ59wP0ntiPXv1yEIT6rrgUgJI-Wwz9YGiKp9Uuc3gMKSJJbeNklX0z5lIm4gKm3Ny3DmDylaGqJQ7zucCI7ijLtsgN2ojKcl9FiXmRlH1QdEpcXUSmgop3XwZh3KtXFg9giQQHSJS33JYSa2MAi0U5IEU8eS1nqzu5GLQLo-Y11UJgDdRaKsRYqm9vmGmB_0GXr8Zl-sRrJMa5z77BR-cL5X32RhOwWdlfKmA_pc-GqplQAR2DRNDecaczDqoXmujztR5o53Wo-c5DlOhaCOa5iMnd1hsVmvh66Gkm-XIhjyweltmRTAi87A9-Bvn3f2wcn7vpl6kKy73mnDfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=boSnJ59wP0ntiPXv1yEIT6rrgUgJI-Wwz9YGiKp9Uuc3gMKSJJbeNklX0z5lIm4gKm3Ny3DmDylaGqJQ7zucCI7ijLtsgN2ojKcl9FiXmRlH1QdEpcXUSmgop3XwZh3KtXFg9giQQHSJS33JYSa2MAi0U5IEU8eS1nqzu5GLQLo-Y11UJgDdRaKsRYqm9vmGmB_0GXr8Zl-sRrJMa5z77BR-cL5X32RhOwWdlfKmA_pc-GqplQAR2DRNDecaczDqoXmujztR5o53Wo-c5DlOhaCOa5iMnd1hsVmvh66Gkm-XIhjyweltmRTAi87A9-Bvn3f2wcn7vpl6kKy73mnDfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعدادی از هواداران پرسپولیس مقابل فدراسیون فوتبال جمع‌شده‌اند و شعارمیدهند که پرسپولیس رو به جای گل گهر سیرجان به لیگ دو آسیا بفرستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22866" target="_blank">📅 11:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">▶️
هایلایتی‌کوتاه‌ازعملکردخیره‌کننده مایکل اولیسه دربازی این فصل بایرن مونیخ مقابل پاری‌سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22865" target="_blank">📅 10:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22863">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=LH37bTf9Ts4VEiM7jpwJbZQ-7vVUjH0SMpO8Jv9bjV6N_ryLo7v90simpF96XjLfBi4NRHBQr9TDFYkVwErm9T4vUpPj12RC8CBV2D3R2qbqev1C2Mj2UOwSWdsaNfif96cQQYblvvCD3pgzOM-9BhPzcFARur-ZLXcZnbabUNFzAolGjvq-_lgJeihvE9_ONrhP4mqo27z0WHgcjWz_8biMpENe694vtbgVSANs546WVMj_W80VqycBzB9CmRuLVMUoFkZ9ZjjLm4RdCdy-rCW_WB4CUfdgcc-zmYBj5jXRcKmcEUc-TEfcc5SpMh9iqNIS7wO-61-mSYPbJT9EJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=LH37bTf9Ts4VEiM7jpwJbZQ-7vVUjH0SMpO8Jv9bjV6N_ryLo7v90simpF96XjLfBi4NRHBQr9TDFYkVwErm9T4vUpPj12RC8CBV2D3R2qbqev1C2Mj2UOwSWdsaNfif96cQQYblvvCD3pgzOM-9BhPzcFARur-ZLXcZnbabUNFzAolGjvq-_lgJeihvE9_ONrhP4mqo27z0WHgcjWz_8biMpENe694vtbgVSANs546WVMj_W80VqycBzB9CmRuLVMUoFkZ9ZjjLm4RdCdy-rCW_WB4CUfdgcc-zmYBj5jXRcKmcEUc-TEfcc5SpMh9iqNIS7wO-61-mSYPbJT9EJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کیلیان امباپه: همه فوتبالی‌ها قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهانه جز هواداران بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22863" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22862">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-00WfqD1eeOfJQ_Km52hjJYUFOgGtrk2I85TgqDXTRT2rFg_Mi75nOC6CQZNl4DiM22K5XMoHnD4NmtIBNY4qfxEhzM4vHci7DHdypVaCMYTE2wCsUqzzYTmCD7vGVdn6J28kSSlUSuFdJHvMtW2P8rf8lCFvhniWLrKu_nGfNL8XSCm3n2tRIaIsIefMh0vxLsXbGyOWgyfUextsoaB-h01aLAYsJo1C3ffEIwHKhRzlWnsLgNrMmRMbSdjmCxG7ge4YuZFFmS7uhrYr-txQJFz27toT_Kudb1ci70pUWk4X297fbXRCeFKnNCB6OI4osY4u_Dwk8bcLE_vv2Eow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین‌سرچ‌های‌ایرانیان‌بعدِ88روزقطعی؛
بعدِ بازگشت اینترنت مردم اول دنبال چه چیزی گشتند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22862" target="_blank">📅 09:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22861">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=UY_d1YdyjSNWG_nN3WjWnkXr6DniGDGibUQxkX8dk4AKcDpENSnh1D-rg3ENj4bHkqL_yjaekss1xbweGKRRd7bnAF1KmcHt4-n9R2YGFZzXwEH566n5nFFT02tqIN_FBbb9YpBIpOcwG-_BmBeFfrNKJrlGsHxAZ0vIT6fINJ9JRSDvrYMuEeb3X0sX-NPqj0JFN45KIWi1BeY-pejkJY1o0JVJN_K-wOqHW5-bXRbcG-YAn-n3ViGRmdUoDrSOgy4vXd3osUFnCYrh96hDoAyeNrJr5Nke9c7HcsdBpits4268Jn5JCyojAsmx7OSdY2xLPHx4a0KSc63nk0BmbBcvkadr1NmgH5s7X2D_Py9Z8dCDebhFXZfTLvUZlOGnQOLR-hzRb1BfqQ748FsEitZgF8exLebIyVdRkOPEFqnJ1fasbOi1TjPonSRDRP9glqa32DLXMxMwtCymhiJ9ypNoMzbn3gfBB7RbAFRXjIX4j3M-eb_vh0Fk7FPMn3HVYab37tOXg4uA7MBITyNS3U_rsYEIfxUZH9JJqed7k0rkXu3vi28D2GcURaWKObvBE60-XEPecmC9RSwKQg1cKpSPQOGhEuEIektnO6fTa7jQ-Cj-LebAYjOc46wSEPqMKE7eYNRLE2AGs88ZK6y--3_NtVUWpo8SjpGH6gaed8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=UY_d1YdyjSNWG_nN3WjWnkXr6DniGDGibUQxkX8dk4AKcDpENSnh1D-rg3ENj4bHkqL_yjaekss1xbweGKRRd7bnAF1KmcHt4-n9R2YGFZzXwEH566n5nFFT02tqIN_FBbb9YpBIpOcwG-_BmBeFfrNKJrlGsHxAZ0vIT6fINJ9JRSDvrYMuEeb3X0sX-NPqj0JFN45KIWi1BeY-pejkJY1o0JVJN_K-wOqHW5-bXRbcG-YAn-n3ViGRmdUoDrSOgy4vXd3osUFnCYrh96hDoAyeNrJr5Nke9c7HcsdBpits4268Jn5JCyojAsmx7OSdY2xLPHx4a0KSc63nk0BmbBcvkadr1NmgH5s7X2D_Py9Z8dCDebhFXZfTLvUZlOGnQOLR-hzRb1BfqQ748FsEitZgF8exLebIyVdRkOPEFqnJ1fasbOi1TjPonSRDRP9glqa32DLXMxMwtCymhiJ9ypNoMzbn3gfBB7RbAFRXjIX4j3M-eb_vh0Fk7FPMn3HVYab37tOXg4uA7MBITyNS3U_rsYEIfxUZH9JJqed7k0rkXu3vi28D2GcURaWKObvBE60-XEPecmC9RSwKQg1cKpSPQOGhEuEIektnO6fTa7jQ-Cj-LebAYjOc46wSEPqMKE7eYNRLE2AGs88ZK6y--3_NtVUWpo8SjpGH6gaed8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
#تقویم؛ یازده سال پیش در چنین شبی؛ بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22861" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fml0i1ntiaLnHC2zWzq13OOwGrZjFC4kcMy6MBO7l3aK5hryfLwkew7REBD-bFSj2GfyFBNK346LNq9TgEuMFxRBt_ucA-COcP-rDThC6D3dz8R_ehLMqEE91Hag0vhda8Ib3JpuPE68HL9a4sIW7lsRNsOlm8LXFtXsJIW8-PmPKBkIABuCjwM6SsQHx4lI7rnMlX_p75DFHkYxbwFuXz3mTnN7op8r8t2iOrzMY_URmhpN4h5oNArOe1YraEoE7b1v580r6mSpBq4IsSBiYCRNMC4r6TQTHNtpmORrrxnl1QMloGL7OFtENmJf1AQ_swNAPVixSuvSkcEfAYUD9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sp_VZeNtqXDniYbTH0svVQbiHBnqVEiLr853m90AVUMQkf8ZeqDXh0j8AVgGY5q8IE2E4Xygm7pj00wRrDHBiZz2Dfi1FhvbB5K1PU7gquca8MGBsHK74Q-B5FJmzkAJzr_bkYyF7o2UbfnfOUToND2xctkGq1KiC1NDDrD-bVlKFWCGJScshAo9FPsZMowbsf4dTEZdsEh_mGdqAg3KEpEJK3bFD72jNzNIO6IigmvamBUuLh_i6T1vmETiup18tbSG8r7aA_YRzPtnxeWiMa55pRK761MtPZPuF1gC-aIWjWdOsNUBo_lHiGd4BN4zcL-bevgoHuMWlYBkWOZjiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تقویم
؛ یازده سال پیش در چنین شبی؛
بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22859" target="_blank">📅 01:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbFPW7SxdylN3GsGTWB0dB-bfQN8k00pCnbbrPT9j0gW_WxGeXApnwonOm8ZLmsFzgmFNrmwFP4U7pfLcW7xNyp_rBG-W3uc4eqKPHaMOu8zqsKlcgGmzO30OTafpYGD4k2ZOpKxW8DXoeluEZnUsPTD_CwfopY0x194pVzjGt3SEnBlPC1uEeMuoNIa064nSA-lAZOybX8d3AwGzOxbePMcbjo88PjwBJr1nJTy5Yb1L7ei0QX-jEpwYz3wiWIDA52iqKLs8reXjo5JNXCS0Zj7Z1Qw0kLYE1BjAm9JznZy88cITeNQaRvSYZQb4tXC3NeMuiTcMoR_JqZq56xv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌کامل‌دیدارهای‌‌‌امروز؛
ازجدال‌یاران رونالدو برابر شیلی تا تقابل آلمانی‌ ها با شاگردان پوچتینو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22858" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJlCywdk1_CVNais_GaQF2VMhlds2RXx8Lf1xCTBKPaXtTjGAWOpKUiLaoH0dZPXEifuwqndrhMwt9X-MYRRjPBOcC6mVdRXVMAZ46TOPlZMb8Hy_kBTMJRSTBYHcHKKJYM7XCR9hPDLDLMsYABCmGWeBL7O_HJifKEJwxxLkFqFawHgUSVlSfgagFFVWrAz8_Oli0HqJ6QijM6IcX2WMNBtVR6TJCrNqSBlkgKf32ONh53kMMbUlhcYbu8mgp_XMa6bI10mRp26Fvxl0o2V7dAUJq5bItxhBOH0Ke0n_bezcxte0ScPqBOzsyCPeejohKo8cJGStWkxcZjeK1cubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌ روز گذشته؛
استقبال مکزیکی‌ها از جام‌جهانی 2026 با جشنواره گل برابر صربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22857" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22856">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HihDmdyuIXfwrQ-7zz-ItM_QNZOYy1E4Wyy05jjZw5PgjfPFlSR0SGC5CG9ASIrKMZJ2wP11Dkvvr3SjfmWRxiSIOr_MbDOtGsTWELqBnBY0_d2Tr9Cfi54cOB7PCswNjC-dnoUiP--LM18_HfECVOKFUIASzftLUMfHcj3rVa4z9Ux1LxQhhps1rZfSFTTC6Nwmk1LmFSVRWuP-wm0D8ex6o4lgD1598jeBCihM6lSpIUs2qODKNW00lLABQhLqz4YDEn3LUQwGvGih2uAK4uQHNVOzBT57gbbjTw0QqF27WZIGvC--pYqdeyQbSeDsFXOuWi05-_jFKBExb2VxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شوک‌دراردوی‌ژرمن‌ها
؛ لنات‌کارل‌ستاره 18 ساله تیم‌ملی آلمان درتمرین امروز این تیم بشدت مصدوم شد و رقابت‌های‌ جام‌جهانی رو از دست داد. ناگلزمن سرمربی‌ژرمن‌ها بلافاصله آسان اودرائوگو ستاره 20 ساله لایپزیگ رو به اردوی تیم ملی آلمان دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22856" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22855">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrHqqjzAQk0g8fY55mHQHhOzys-4zWuqPsDOOSbr_PtnXXcjePbr81fz-W4YSvjonmHUKi59_ww_P7GzaZjWnngh5fOEx0oOOgpvC4HVcES0eaFLPzcEfeG6LaqhrwVqid5aiX20PuAjasPgaOMZhRuZpJRY9RzuH0FKG_VC5zXn67-UrPRtWesVb-Wi51McoAKPLVD3ob3wM_MUsYtzKervdVUlTFttnG91M-6uC-DrOyddD_nVi-VFCbT0ZLt1L8XcaqaMZDQ2s5kLeTFEVA4vY8HFhv3PvPWGXZ3At4Ot4Be_3Yc_87r6RjOU75pIaedLnYZ_bT3gmb5hTUSLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22855" target="_blank">📅 00:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FawihzzJsnPD63pKO3Fp1NNoN2Dgu6_9rpp6JI9Yw5r30S8tldh70_EenivxMooSBWI0QW4XFg6eP6zWorxp1QQw90OXoM6JTDSL3pesEnkzQqev1VG2sJ8fgR7hPfg87iHYUNvmOlnak_m-lqpkFUWEBfrGvClH4HOaOaGsHy_xzHfPLY1Zqnoo4nRwgxSzOU8DmXPBYOYw6g237GZxZq-yCUY6WKPHHxu_O92MgBYdTUWI_WjR5MfReHDfVkhd-IeLBa8RgdEixlHGkkOBQdDsDuHB1x53SW2qJBsIwK4Qa4G-wdxkCHbaDdbeoyJeNsY8z9QnD-rtUJINAKCaFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چت‌جی‌پی‌تی،دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت. همه برنامه ها دارن رفع فیلتر میشن جز تلگرام،اینستاگرام و توییتر؛ سه‌برنامه‌ای که بیشترین استفاده کاربردی رو دارند باید فیلتر بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22854" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22853">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=ShnWqvfn9DepkNa9X7zvqw74H5asUcb_nBRqSirUyvlPfVthAd7S8TbPkFHPanuTcMQrTW0x9WP-EFtNO8VmBFYvyohT-SSnYYepfmJoYJ1SR1yQ7JySLunBzGWFalwUyBRnMCfWsfQFeLb_OfAvmhCdqwWHb73si3Li-hSiOxFOXo6mAsZ4KwiVQlaWbsTlIA9jFYcleNlegtSlFefXKowS3B9Vvt5YaoWz-bo8ynhzv8Z8GVUTLn2akDTNe3fK3ZQYGuMfyawvlFZWrr5fwK9_5TyaIT5szBxMyeYh0O08J6ykl_wfdtQ09rcqDlOPNaOQ9slxQggP7b0JT0Uo3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=ShnWqvfn9DepkNa9X7zvqw74H5asUcb_nBRqSirUyvlPfVthAd7S8TbPkFHPanuTcMQrTW0x9WP-EFtNO8VmBFYvyohT-SSnYYepfmJoYJ1SR1yQ7JySLunBzGWFalwUyBRnMCfWsfQFeLb_OfAvmhCdqwWHb73si3Li-hSiOxFOXo6mAsZ4KwiVQlaWbsTlIA9jFYcleNlegtSlFefXKowS3B9Vvt5YaoWz-bo8ynhzv8Z8GVUTLn2akDTNe3fK3ZQYGuMfyawvlFZWrr5fwK9_5TyaIT5szBxMyeYh0O08J6ykl_wfdtQ09rcqDlOPNaOQ9slxQggP7b0JT0Uo3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع جدید باشگاه رئال مادرید هستن دربازی روزگذشته با ساحل عاج؛ واقعا مدافع قحطی بود که فلورنتینو پرز رفت این رو گرفت؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22853" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewpi6Ghsg38SToSEWhKI3O61blH6CZPsI9VFat1qB8pO1Urv2QefijS6rsE5No_0XNOrf_3mCZ8hiZwGDOTZ9dH0avW_5_sZLF9dxftnvYJ7BU5-PFtsimueEA7XutRMXxFQmakBdtRozn4lwuJVR2z7k_Ke1H-jBBJ2tCE9YzFMhCfthgYp-SpLHTE4acZc_pgQiH3A1eV8E5owVHobGOjbV6g3iACNU7cnjwmkKeZSxc53iaQi4MFV7oHJ3pTm-O8t1QfMIKBCubwEk6DdQOpoL3lWX42caRuW2GB80FCma9Eg-pvd3Vd9eZRmbkJCrqG6v_czeFwe77Gm-9g8FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
علی‌‌تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: یک‌‌نفر از اعضای‌هیات‌مدیره تیم استقلال در طی روز های گذشته با مدیران باشگاه آلومینیوم اراک صحبت کرده‌ تا انتقال محمد خلیفه رو نهایی کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22851" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV7xPGjpY7d9fz3KMdvrEX_iX6JkU6GdZOITrgiCyd_l9T8-xXVYmr7VlIsjkFJTYiG1QHj5M4nHCJe1Yat6rphezi0Ulm64I2cYBoXldSArq2Np7Nx1Xi0azx0Kc4mxwL2x9y4VsdXyP3yUCttxeh8B0eduryaf40uGRGwYfbVmqEmFBiqAnLvoUBQqtrHffCDzbe2NyF8qqtXSHounBOq_Zm7n-fuXV-A47gUWQ9HPVfZ1IKfM8BmKu0NBq9rKsMt7s7XPgQ6zciMANEBoDdAb3S_gkR3IqejH2Uy8f_XH45RpObIbe1pszZYXw5zqoIm6C0e6l5wI5KdbI0dm6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22850" target="_blank">📅 23:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=Emr8lPSU-p4x2mcT-1yvUSkkzL46dAnA2qnD-hoq2ZjMRwTfSgTgzMWMc5ttoyoPtA068jy7O5tVDsz7sFhBL7Ap84De_4YWQ1HHrHpmDSzRYXFyAsaviy0pY_kLZ-AGqrJRh5qxi2rR_tWtj6zE9w65GUg_9yCliBkrR-gMGCTAQToLqZXM42Suf0oXXN6otnM2aq1cAcfIRZ_gYkuy4k0CQrk5LaBxdw3Ub8pv1I7wmO7kSyimGPFr-1nY1Hu4pZelAVrI6NqM9lCbRgHJ2167zhrxp0U_p8_PtiKCgQspRfDMT0n55cXVLnqRscbPVO_I4ION4W-QIhWoRz4xJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=Emr8lPSU-p4x2mcT-1yvUSkkzL46dAnA2qnD-hoq2ZjMRwTfSgTgzMWMc5ttoyoPtA068jy7O5tVDsz7sFhBL7Ap84De_4YWQ1HHrHpmDSzRYXFyAsaviy0pY_kLZ-AGqrJRh5qxi2rR_tWtj6zE9w65GUg_9yCliBkrR-gMGCTAQToLqZXM42Suf0oXXN6otnM2aq1cAcfIRZ_gYkuy4k0CQrk5LaBxdw3Ub8pv1I7wmO7kSyimGPFr-1nY1Hu4pZelAVrI6NqM9lCbRgHJ2167zhrxp0U_p8_PtiKCgQspRfDMT0n55cXVLnqRscbPVO_I4ION4W-QIhWoRz4xJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه آلومینیوم اراک اعلام کرده‌است‌که هر باشگاهی محمد خلیفه رو میخواهد باید 100 میلیارد تومان ناقابل تنها بعنوان رضایت نامه این بازیکن به ایرالکو پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22849" target="_blank">📅 23:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=Owb-fjw8e0p5guuPAhC8iukByA8NbQfjFaBjA-0LCBBF36ODQv6JpDEaxP9TyE0BvuzooP_qErdql62Szvvn-xAyhMO3lVsZVV1y-EsSg2c_CvC182cL9x8xyWpL57eGPXKchNQy-iLiYTaFfQP6148IkjqEKQK2oDF-CycdjyOYxNv3VOxLYOgH8OVwBq0yszoEoftkHltF6FeR3mCLOImWuj0ylh9KgQ25X6y29AMNeZaU1E2_xfgqceMkDpelwSSxWBhoFUbu7Hh5GmuBMR5OkvbzI1z3H1wGyeEH99Fy3tfYaB6npfqYip8ZgQ_e3yhzEucmq9AmQcYXYNDG2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=Owb-fjw8e0p5guuPAhC8iukByA8NbQfjFaBjA-0LCBBF36ODQv6JpDEaxP9TyE0BvuzooP_qErdql62Szvvn-xAyhMO3lVsZVV1y-EsSg2c_CvC182cL9x8xyWpL57eGPXKchNQy-iLiYTaFfQP6148IkjqEKQK2oDF-CycdjyOYxNv3VOxLYOgH8OVwBq0yszoEoftkHltF6FeR3mCLOImWuj0ylh9KgQ25X6y29AMNeZaU1E2_xfgqceMkDpelwSSxWBhoFUbu7Hh5GmuBMR5OkvbzI1z3H1wGyeEH99Fy3tfYaB6npfqYip8ZgQ_e3yhzEucmq9AmQcYXYNDG2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22848" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22847">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODVU7bvQu0oj8ZsgbzZtLt1dH83sRSLjaZ5DuSUOwmxkeJNVH9B7nvbwOJxt8up9AUcRfHoU5Y9aHlIf2_PJ9AMe8Whsy7jsey2irgVj4WYY_DngRdYriFIh_roztoxifoGx5Na3jQZtx01fYhWPmO03KknIcRDsKzEQl6vF0pw3ALskeNocTxtkh4XAtlO-9zimf091FciIbqNDER8TlXIDNauw6T-upW_zd-i6HbCWEdv56XlVYsMcMuzYS5NUprixxDBjtovFGxuBKnz6ZmFt2t04IirC7anHukkyq6uM4s8Iyc_uB1FyE5XVReShM7Oom-hDLGXR1-eg1ib26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه ستاره رئال مادرید: به پیوستن مایکل‌اولیسه به رئال‌مادرید بعداز چام جهانی بسیار خوش‌بین هستم و امیدوارم هرچه زودتر این انتقال دوسر برد برای ما رقم‌بخوره و اولیسه رو بزودی در تمرینات رئال ببینیم. او یک بازیکن فوق‌العادست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22847" target="_blank">📅 23:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22846">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">▶️
انتشار موزیک ویدیو جدید شیدا مقصودلو همسر ایرانی خوزه‌مورایس‌پرتغالی برای جام جهانی
🔥
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22846" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22845">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=QGRF4EW-Nh68u3iXUL04KZqLUQc0tlk0oSbTN8sizsBvwN1fWWDoOpV72jgXYQqzJWSb3qEauTUTYTBosr1ob1-B-H-1oVeCNtmzTn436oh-bqcZq3bEtFl8BzBuUUKFiVY1rEKhT5Ya-19D8nzE__jXPL4smr7i22qQS4DxgdqkB8C9YJXr7D6Xs80G88JbN-gNWcLWQYFeq9REyW0-u8fKZ1QPJnENMqO2qCwuL7HqWl9DWET7x_r3DwgaaD95NLfaLdNjigKzyHJXQ35KUvA5Hoo7KNyzeKnSrL8RMhbzMK8HI5JKuCo8xcsNoPHONvNQ5RALyXfqGCssh8m9Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=QGRF4EW-Nh68u3iXUL04KZqLUQc0tlk0oSbTN8sizsBvwN1fWWDoOpV72jgXYQqzJWSb3qEauTUTYTBosr1ob1-B-H-1oVeCNtmzTn436oh-bqcZq3bEtFl8BzBuUUKFiVY1rEKhT5Ya-19D8nzE__jXPL4smr7i22qQS4DxgdqkB8C9YJXr7D6Xs80G88JbN-gNWcLWQYFeq9REyW0-u8fKZ1QPJnENMqO2qCwuL7HqWl9DWET7x_r3DwgaaD95NLfaLdNjigKzyHJXQ35KUvA5Hoo7KNyzeKnSrL8RMhbzMK8HI5JKuCo8xcsNoPHONvNQ5RALyXfqGCssh8m9Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22845" target="_blank">📅 22:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=Xd2vPuHwwX_GlH_4_iDMeMdc6cJaKAdOsx1quvgPUUYvtjEwTN5xZ1AatFkmulCrfpvzG33hPuFyt8teMss9-9iM80iLXf7xn0PTePM_3bdxhrWrLG13-wmA3OUxNKBetRsiP3li96amWsKk6Ke9BGe8zBETuX20garl9EYA5SLRKl9pssYWJNXzMhw_BNVFuVYh4griX16ptcqYRL1WFZuQ_8qmrscYMYzdsFEJRb8e-e33-vFN04ZFzxN9sbvd4aZpdYEPuZasKggo83DAG_uoUZsTSwmHe6bhmYul_R16zPzzHfeRWKVr4BeMNzwB0vEWdehzq6vyOfnICsXFBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=Xd2vPuHwwX_GlH_4_iDMeMdc6cJaKAdOsx1quvgPUUYvtjEwTN5xZ1AatFkmulCrfpvzG33hPuFyt8teMss9-9iM80iLXf7xn0PTePM_3bdxhrWrLG13-wmA3OUxNKBetRsiP3li96amWsKk6Ke9BGe8zBETuX20garl9EYA5SLRKl9pssYWJNXzMhw_BNVFuVYh4griX16ptcqYRL1WFZuQ_8qmrscYMYzdsFEJRb8e-e33-vFN04ZFzxN9sbvd4aZpdYEPuZasKggo83DAG_uoUZsTSwmHe6bhmYul_R16zPzzHfeRWKVr4BeMNzwB0vEWdehzq6vyOfnICsXFBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ویدیویی‌از قهرمانی تیم زهراگونش در سوپرلیگ ترکیه؛ زهرا گونش بهترین بازیکن فصل لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22844" target="_blank">📅 22:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=nuoZar7kuuuKEznFPkCrQ9GwuTKmtdUNUC0wXQMYyRkRAVPUUoIHf36ZART0xK8TNlnr7v5TJyXlgGFX9-qeiFnw99pCFqMDtbrOv5TEZL2zN3t8tjFpO8p_Hi4lxuC8E4T9YX8vVtKYk7v3auFLWXUANzgKNXdkOWYc-SI7mwrmHRA5WFaiA6f-OueE5cYo44q9_FTuhMQEVNx1GvNkDQUfif8IP_qUsAwTr_0SY9NKwH0XfY7F1ojL6Ek0AtJqaREDLHY7Ow5SdlOn5xccXgj-xgu_QbOZor1TxB1MNLaR_uM2BE_FM7BJPa9ZTxv1xMtesk2OWNcQ_9IvclX3Uqall9HfISOubPdtL1B3d30_ob9KV27FqVhMMPGJ2yE03fsRhqXXWy8Y9_CGwVvYMJ9cYqOclTIyBQ8dz5mMGWF2mLoS1zsy5Sg-NbKtgSI1GVtRMfoVUIoNT6rgI9wQtnIXSLaWZeSKExGwqr-xwZ96-5T74m40fSh-Bf8y5W-YumNk8otlgSjTPIjc4PHagSBkI3lr9Uk5plCgaWNA5D0G9lG5wl8o2huDr2DEV0UXjsw54Zj_FoSoaz9F2NB0HDewd0AlQU6qLE5o1s2ICIHpUphE3Eff-fiuoTi597u2qOtmRQENQdZnImu_5XRrZajLR-EvrQB4bDGqct_2SrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=nuoZar7kuuuKEznFPkCrQ9GwuTKmtdUNUC0wXQMYyRkRAVPUUoIHf36ZART0xK8TNlnr7v5TJyXlgGFX9-qeiFnw99pCFqMDtbrOv5TEZL2zN3t8tjFpO8p_Hi4lxuC8E4T9YX8vVtKYk7v3auFLWXUANzgKNXdkOWYc-SI7mwrmHRA5WFaiA6f-OueE5cYo44q9_FTuhMQEVNx1GvNkDQUfif8IP_qUsAwTr_0SY9NKwH0XfY7F1ojL6Ek0AtJqaREDLHY7Ow5SdlOn5xccXgj-xgu_QbOZor1TxB1MNLaR_uM2BE_FM7BJPa9ZTxv1xMtesk2OWNcQ_9IvclX3Uqall9HfISOubPdtL1B3d30_ob9KV27FqVhMMPGJ2yE03fsRhqXXWy8Y9_CGwVvYMJ9cYqOclTIyBQ8dz5mMGWF2mLoS1zsy5Sg-NbKtgSI1GVtRMfoVUIoNT6rgI9wQtnIXSLaWZeSKExGwqr-xwZ96-5T74m40fSh-Bf8y5W-YumNk8otlgSjTPIjc4PHagSBkI3lr9Uk5plCgaWNA5D0G9lG5wl8o2huDr2DEV0UXjsw54Zj_FoSoaz9F2NB0HDewd0AlQU6qLE5o1s2ICIHpUphE3Eff-fiuoTi597u2qOtmRQENQdZnImu_5XRrZajLR-EvrQB4bDGqct_2SrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
کاشته‌های‌دیدنی رونالدو در تمرین امروز تیم ملی پرتغال در استانه شروع رقابت‌های جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22843" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H37GBtjcsJdcN3IHx0H8Bd3uzdu9kGd8gAaLa90m2xAbw-PP6NaTdQs8AWBcY_J7dHXlbXJ99wi21S6GsxdzYYPI_T8KxsR0qsPGsLlb6siEzfFDDtFg3yRZDfpprp7wICep_GTLg2gkg0HkCp4qdRk6E1x-OM1QcrLuRqtfB0nC_LETn_u1PPgA_CK9kQSXFnuBMq1MBnfBZEhXRH3oOPPTV9sRev7upuuXm14WmB0CiUM44CuMStur9p3X03Y5xZ9NBMeEjS2Jl7ZSo9xpnS-vNr4KZc9UaBIzWJk2_A6dRjtee9NPXfcvTGeRjB5AjkxGgC8BaXlfVrbTy2o0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22842" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ0bvYi_ct7GMkYn1VcLP0amkgdqCVt9sH5Vw4kBB6rtNkKA6LOjwompuI1WXy6OhzaF8XilDnqwi7yQeysjFfZ_V5YUoBDFwRJLUpmUoqcdP5g2eChqxYbcYSuWn0ERYZCf8d1X8F_fskORa3ZFr31TEP3Npg1uODzWwjTeB1HcmyDQGi7Div3D-lvrXg1F6VX6-ALakKR8Cgs3LNqjaiQfyMLE5dVTvEWTsFNVhtgXsvLYAok-EUa__B5F7sqekV8ddO7yftZeUb39EjFUcEcKQQOkH7oZH5a0tIXamdwMEOddQ7I217gzpLzkF64zAbuM3vBztzi-P-dEWRyS-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22841" target="_blank">📅 20:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=rk1vyzT-yVTTpXktWDwy7T_QYri_91oGfsm8lvUbVho4e-LjR8XodQQeYlEQ6jn_LuJN9jD9rZ0RTN881vsyGKv3nz3mkPIfALC1BaYD3WC3mCONRn7C8_sgariVUKZ7QvfxNaiqSVbZ3SguVVG5Rxs35dNq2yk-zWFdyhyEjhDQAFXU3EtIQ26zIbBBOlhM5kuaRifkBOz5EeooViSBQRGsuktwPaO7uwobwSs1k9P_ouEh_OY2l-mCX33BRjKPUatsD3WKjPMzfGPFvxSvaftbzSn0cEIa37X9OhcMLKV1lhM_Yy380pkidPqU7fB3TZ88C14u_1A46FFQPHVWQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=rk1vyzT-yVTTpXktWDwy7T_QYri_91oGfsm8lvUbVho4e-LjR8XodQQeYlEQ6jn_LuJN9jD9rZ0RTN881vsyGKv3nz3mkPIfALC1BaYD3WC3mCONRn7C8_sgariVUKZ7QvfxNaiqSVbZ3SguVVG5Rxs35dNq2yk-zWFdyhyEjhDQAFXU3EtIQ26zIbBBOlhM5kuaRifkBOz5EeooViSBQRGsuktwPaO7uwobwSs1k9P_ouEh_OY2l-mCX33BRjKPUatsD3WKjPMzfGPFvxSvaftbzSn0cEIa37X9OhcMLKV1lhM_Yy380pkidPqU7fB3TZ88C14u_1A46FFQPHVWQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
@Persiana_Soccer
| Out Of Context</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22840" target="_blank">📅 20:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGN3Wnw58wxlb-Rz9WzRdLNtrPSqbMaolAzK3PdBNXCR9lCFNkN0tC69yIF9RCWyESJr5jnEloZkZcH43iyUH68PpKTDd3oWiUwwZDjKbJeIgjHu4xXjeYrxu-ilJcHs5n4hKBSskTdYqQ8HdLHk7gZY7IhgUH2ej7DAsl8Ehx5OIjHwXegAbhz5WvUITpzVPo3_D-0NyAAX5x46IaVN7toRfqj6GQaaVtCJG1Op1v44gIg758IzfjGX2_Rpo2OCwrL2PK2iSbgyroK-u1bUaf4AyjMB55jB4Ldn-ljyGCjFStvZrJfo0Ej77kBp_1ZPHxovOrJvBfw7dPyF59LgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#نقل‌وانتقالات|ادعای اسپورت: آرن اسلات بعداز بر کناری از تیم لیورپول به گزینه اصلی هدایت باشگاه آث میلان تبدیل شده و مذاکرات بین این سر مربی و سران روسونری بزودی شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22839" target="_blank">📅 19:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDvSchi8wtHPrSTULtKDGo9VSXcweMmwuIj7eO4JBZrC52_BkaV6_BsLsc9S1rIphbINPITksUESLNZjDNgDoVoyWlHHTMjsli6Kaj03rBsFUGUnnkLUqqgAjINEWkKjMdfLKBkvkE0LuAmCXr_jROruyNDaYiTklPqTifN5JnWm481p4j9MGGgF2Anb8Yug2oAzbnzOv2D9WdHswFjVlEaB6bn6UOw3dWX25Hm8vvwfjNOq81l-kK-zrbP2Ey3Lv3i2XQQa6X7GM9qN9ruSO3rswwidJnSHDim6a_TSCrUm7ChHHOpsh7EE4Q2tICgLWnLK6yNjx34HL58FtSv7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22838" target="_blank">📅 19:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma0nPNqZUSqNdWajIiAYL0pmcrMdyw99MctNya9lEcbU7wvXYpqzMeEbZE4HIfsIl3FoZXZyPdbe1_IzKekmO29Dd74ddQX7xVjuQqcRdEPoY3OUvgPY_6-U4eywXi29pvQQ6XJBaJUV28bdc4wVbOUAkRFhDkOaOCPL9hj47gjP7oXBqyt2cNNfum3JtSEaH5PUGFYlO0IHcBS_u4aUMRllbRrxcrN1SQhRKhrpcAAVvcotmteLB62HtyvCdgd-_JwRivD5Lds9DdescnwBtE0bQHKj14AdkIic9rYXnR_HWuHRjWqTZsbkMV7_r_ISOCZN9Qx3RxIYbmDbi0HbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=Y8xXRFlsEpBsFsGDk388y71egOJZJeWP5szNRAPVn23G4E7ncXwr_NB3BLBogTrFcnFo5QWkiC5P00OZyFLLtGyPdQ5OSJu-LC8EiYJ4EIGBgwBiBVzy5geYHrC4PEkRzNS1udXCbRhCVlgL6AjojnOhdAq9aTYV3jmxgwIvF6vMl5vzDeQLHKg7uR31DsAUbLA-cjzzUnD7n37wvKxOsyA5QtEM8DmvdflzXagegsHEj63x0IdlJkyLM5oTDKczDrah0A1DvGolV-0cUGBppDrXW1eyqtZaReliZ5UTo4FFRqqD5sFTOmCH4kTHAfM35SwrbiGsySp02k86YUCbtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=Y8xXRFlsEpBsFsGDk388y71egOJZJeWP5szNRAPVn23G4E7ncXwr_NB3BLBogTrFcnFo5QWkiC5P00OZyFLLtGyPdQ5OSJu-LC8EiYJ4EIGBgwBiBVzy5geYHrC4PEkRzNS1udXCbRhCVlgL6AjojnOhdAq9aTYV3jmxgwIvF6vMl5vzDeQLHKg7uR31DsAUbLA-cjzzUnD7n37wvKxOsyA5QtEM8DmvdflzXagegsHEj63x0IdlJkyLM5oTDKczDrah0A1DvGolV-0cUGBppDrXW1eyqtZaReliZ5UTo4FFRqqD5sFTOmCH4kTHAfM35SwrbiGsySp02k86YUCbtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارلینگ هالند جدیدا تکثیر شده؛ نسخه هالند جونیور، نسخه هالند پیر، نسخه هالند دختر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22836" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBXQFyVMrTK-87Es89IUskASwJS1qrGUeMAv90nlAOTnrmvLue6TObsva4TA8q_-lIeGSkVmXfxprAkBFyQsBjhTJxDfK9IKs0wGm_b0mnoGPx3iL3g2nCIGBeCOLRl79pkhZuAKhsZHjMSF9DIj6S_GqCNU38rhQTYqb5-OWFWcsomYbLJSyyJZu1Mz4sL3HD-4cAnRkddb6dx8H69ymDZmoLgivfMAbpNgUr3Ap3mSprtL7oLIzF5Eid_LDTXHd-xLoguM2_6JemwV1Jw-ZMJwA9zyw6DhG8efUXV9rrY5B2wnupZI6UIsj4vsQN5CH1aYqIfVx7r-9YXWOYHB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22835" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpA-jnuviVGlrXHqFVj4hTb8aOHWX1SAXewV5Zm23Bl-eYLfDZcDEWrWAw_5Lm7TOU8Co98LBdY_VHDzdZ1tMWI4N5g4oVoipYrUNULEsUTEPA6cB-lnTaE7uHPPfTHgYCotx8hOEMT1RENriInA6gzKZ52BvBdI46hjNybG5iJfxX4Ghb7yGkDAJrYWk8tx1sKAVNGvChJlDirKZQwCW-HX6Itq0tFWDvMkdpvoxl4XmYbA1gh_X-Axxix8LTm0vv_SLI_XoFsplIw_lHmVM9qcUx3g78wFu-fT82keGpINFgM0FRzAY8rEKCSK5hxGGKBwOs6eIqLwFL_G13EiQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا محمد دستیار تارتار در گل‌گهر: باشگاه پرسپولیس باتارتارمذاکره‌کرده واگر اوسمار برنگردد تارتار سرمربی می‌شود! او می‌تواند تیم پرسپولیس راقهرمان کند! باید چه کند تا سرمربی شود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22833" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwXvzmwmuGeZjeow6fc7FRIzGRlNfWvsKTvIlNX6nc7RJBbLfdmAAgmpmDqM-XxiE41zkP5v8A-x5yDJjJKk93if7xmcZqid3AzmYGKZF2r5-HrsBengK94fA44b6Lqy0lCXDxobDSv_o6Fi-_XqkBWE3GqrvcMsK6Q2wnu-vQLT0pWiiCUQA_jYdkVpWMywI2IwtWfkcJY1e-GdyUtoyRS4Wb7UxhBNZb4SxkcHHIQ6LkaLm7h4lDQbw6pOkOCe5qHe5fMUWj1Kby1wvj4F17JL2Mjp4qd1uA9195hro5RJ6QLjNgwUkf_g1aXp8_4abSvjO52ZwYjQHsDnXUpYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22832" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK0wdQqMufaYRGn5eWwecgzQ--Pcwt3jILVwGlNaPk002mUft3ILm5J1KKfay92iIb6Hyy90o-jOcP0MqHeXe_zlvS9qbJfG4owMyfDTnv3hm3-kd3uJAAIsI2PsOAut2gYbC6QYeBOvoo87pgeShjjZhQ0ql2TA5nZJKdSahO4RLYhZF2XIIrykW11-_Fs0puidltU66emDshNFNwUUlM4iAItcFsYxeZY00A3HpZgZyaHzeXeW4itiWeL97sBrh5h4yd47UhkylLWrD1XUKZw9Eo2LwZl3NVoQRlgogcI3o_WCFtjlf8FtBAggNDQ2498NQt0bhls-Pub-FEHcaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛‌خوزه‌فلیکس‌دیاز:طبق اطلاعاتی که بدست آورد مطمئن‌شدم‌که‌منظور فلورنتینو پرز همون مایکل اولیسه وینگر فرانسوی‌بایرن‌مونیخه و روز سه شنبه پیش رو آفر 150 میلیون یورویی خود را تقدیم سران باشگاه بایرن مونیخ خواهد کرد. خودِ اولیسه هم در جریانه که پرز میخواد…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22831" target="_blank">📅 17:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-mD6zuEDT9lZ9Mz_i_LrodRpLZVsiNz38GLzViDN_HjRQCdJzDPK3A98y6enSNPecvDrm7fC2OsDjQ91lKdbFIoB2bM7bkFqNvq3vfNPby9qoPzkFzm3_GqQblUeZfjJ8KP2h1MvPOxgYKAWlbSR7EEo6_2rMKijKveY0fhrkpaytKPahBdGWOoP_Qb_qIJIJC_IEjoJEymMOdEorNwcvguuAVpMUVu7TxzgrfpcErGEeWQsK0f6BQZBRL2k0WqkxdJWFLX5Mlm5-r5OVafU7AJSfcgk5KCSkoyqVORFCaenBLVPBwu-pSgzSOj6tYSdgkvcg_mDj2ARIFntB_xnw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/976cd07773.mp4?token=GGYnbCueXC0mITi-PqzPWZqS2KYaktFsDbzOaahMWzwb1s1mvoPpZre88p-XxtqhQnz97Ob9FKLGDkLnaJ5Oi_NVk03hrPTrSLNIMEumKkdCVtrwNMPQUWj9IGMf6YpgDpvgQEntQ2zIZ2ENpxM_DfF8_7M7_7Wx11BzOTbCjy6vd9eGx3MVp1ksv6Y1p4WOuYXtPBH9uulOg2O4M4LNJ45Fn20fBYk92UYGdgQO4-JCRqF7hNHYdsDPG53PTdj5cdvr_zN1G-HjQ-dOwF9h3VVx1_ijEpld7ibP6Fehox5i6aOC4OhPn3ezEP0euOSE4yd3ZxCAfuyJ5g3Vf0N2Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976cd07773.mp4?token=GGYnbCueXC0mITi-PqzPWZqS2KYaktFsDbzOaahMWzwb1s1mvoPpZre88p-XxtqhQnz97Ob9FKLGDkLnaJ5Oi_NVk03hrPTrSLNIMEumKkdCVtrwNMPQUWj9IGMf6YpgDpvgQEntQ2zIZ2ENpxM_DfF8_7M7_7Wx11BzOTbCjy6vd9eGx3MVp1ksv6Y1p4WOuYXtPBH9uulOg2O4M4LNJ45Fn20fBYk92UYGdgQO4-JCRqF7hNHYdsDPG53PTdj5cdvr_zN1G-HjQ-dOwF9h3VVx1_ijEpld7ibP6Fehox5i6aOC4OhPn3ezEP0euOSE4yd3ZxCAfuyJ5g3Vf0N2Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ابوطالب‌به‌تیم قلعه نویی:
شک نکنید این تیم قلعه نویی تا فینال جام جهانی میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22829" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYlCE3fZJ8qc6DT_pkHlRNv1ZE5J9lUuA7r07354n1AolOeW1vM8MxVVqaDr47mDj9ETrKZ0AR7BtYgVHeOtAhNXlzGQg8aha_Ghcv1RA0GCc0LVTof32geetpNJj49ZEPKOdyvJQyBtlcA79vIlW1V8LSGFNe7LVvw3TJvBOoVErIdUGcSayz78HoTYLge24A9TkjK_q6ZEmILSYmfLIhcP90UBeENLSdzqOzSYkQ2vdeEebcydONzUBbuS9XBCmqNUSDhqk9r79AfOzP32Z2VY0xo8I0ESgplyI5GcVjGsaGDQ0S22I-6lvLQu33RiYW05_T-vYxgegwMyfA0YWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22828" target="_blank">📅 16:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duOohLght1NeV0pPiBNLyQyS2L8YvcV4BD2yMKK589OPRQrXD1siV8ScxG-ain6Occ_8uj7BbIwFALIj9jKxwh5b-PgzdpSNygRR4GgrCQOT4gwJF4d0DKw_yXiqejidlPZqhECOyBEwNLgRGAbexbBUfoodVdPCXTzr8qzgo40xWSYMmgFDAzveWtp3tKnyR6xhZQ1JCaQ7Bx8XGxKgGf9W4JA4drbOOmwZrhR1rD0YwzP9VWMUj1Pv6UbUp-M3PkrP3lgIQYayJFfcoOYx_hQNU9wQQpdtXImwGgrwF50jjU1AQW7P1aVAIaFYLdhGP_TBAV47OTFXCppq7DVqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22827" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=Yu_eej970_o9OpmnE_5ha8RIkYvMpTpfg1hMqr-UFO2U_Xfr-VKeVBQSFDKHn0C4tA763yXxwy1WT5aUDUSqHwc_hwVtBKcIlBYd-C0eUfQWRPa3gLFEyx6PYFFnTHWh_JBw05LFXMswwX6017Vdkfd2O8y2hv3xSyE1_tbippvjYg96TsshRapFKf4Aue0VlOsRPSEP7eg5dRF7nMjPKSlXvMnAp_UUYPnvOUH9f3sd-stCVy5ZNtb-GqU7jkwR3HoOtAXXtc2itVexDUvJr7fTjUKTckrlb-42_lXPfYfhSTirbCy9QFIuQo5kp3ilIs9R8qFGn7CvfzVdNNPdtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=Yu_eej970_o9OpmnE_5ha8RIkYvMpTpfg1hMqr-UFO2U_Xfr-VKeVBQSFDKHn0C4tA763yXxwy1WT5aUDUSqHwc_hwVtBKcIlBYd-C0eUfQWRPa3gLFEyx6PYFFnTHWh_JBw05LFXMswwX6017Vdkfd2O8y2hv3xSyE1_tbippvjYg96TsshRapFKf4Aue0VlOsRPSEP7eg5dRF7nMjPKSlXvMnAp_UUYPnvOUH9f3sd-stCVy5ZNtb-GqU7jkwR3HoOtAXXtc2itVexDUvJr7fTjUKTckrlb-42_lXPfYfhSTirbCy9QFIuQo5kp3ilIs9R8qFGn7CvfzVdNNPdtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYGpCLkDXEccLqqoIDZhIOofQwyc9edchizUBgm1oxzi7qoe_brIFKSC7aYfUCaFo5_MKmSrC5h4OiV9fof0ph57BbvqA49QRXc5wAeteTnWZe5CaU93g0pWIT8sSD9KNhzSF3kpxpP375TkwsqtScxNBFlH9vjsctMLa4fWmhY8RiALhImizI_a49ctun1c0UzF4cdz0YpW8II_6KeRX8Xqwt_cRY-XEBSjFk47dy_IXIw9e58s19UArcrXZSVSXMtC_SXXAICcCPbrQ3-P6f-FQV_fjU8ANfFcQMAowT2peQgPTTrm5S8bk88U7eKbIDdUKHVHtGEb5-zT8XRbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل هفته سوم رقابت‌های جام جهانی؛ از روز 3 تیرماه هفته سوم شروع میشه تا 7 تیرماه‌‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22825" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooBQ-O8p6ylEpkX_-Z5fDEcVvRiCnqJEqxziSPZ7jrOXnYjrxA1ZEZz_BFDsfrhYMuFdu2G-liajtHOgJGtHsJl3rI-GMhVREJAu7TH8ee8fOPPNZC6s3LsqM1wjFkPSRr9YuAzImByU_Z9iEFfJ7PQNFw6v3aIfL_RZoSeK7SLSm-eYRvbFictxAPken-sRTvlI7mi-cfN1XuXyeZu4cE0p5dST0rC5YkmMG-r1LtIJ1KzDSQeAvgdNvn7Ghy_2n_q7bl1BkfKpoD07c4CGdJh6Wlz0lnZYG3mjX_HEdKDlIoTLFJ2ag7hSjXPyJhcPJEin9rgxMTIaPNrG4pdl7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نشریه‌ کوپه: رابطه فلورنتینو پرز و خورخه مندس ایجنت فوق‌ ستاره‌ها خوب شده و مندس به پرز گفته هر بازیکنی بخوای رو باشگاهش متقاعد میکنم. ایجنت ویتینا و نوس همین مندسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22824" target="_blank">📅 15:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0FKNf6Pl9jcFoG88eGkS90FFsTelRzk21DYSo7V9Ng1IEW9Nq4JnB6x5go7zkxhobpUJII-TMLjUul0epNR7eUfvFl85AIeKm5MKvqNlcpCWF6SEWcLYOrTKogIlWIVgYyVsHs_0jf52WCh2tBLOguz4uAmCYmxOAZg_Liergq4azuKeaWbhoo7VokyjHU0qoekt6rvVo1h6XIikbfivuylEQmM1jtbgTeuVqmHoXzATTUSdKbCSYyWfCT_CMpfQcMLOb8Oqk7A3NcRuQc5CJiYL0G6x-f8cCGx9KAqlvcPory15KgbXpyQbR5bCT9DpN5XpT_7pjuHYOTo8lR5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22823" target="_blank">📅 14:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwncCbRhTXFQr4GXpNd0jTrRV6wYYuo7sx8aDMoo0owjnDC4zObSaKLSMWDtfkhdMursm7zVlFm6xB76Cv-VRth_bgFsRSvL-wc_yTCqhSNHFpp9X-vwkzDEOi8oQBgZCQLCKfwTh8TtcrF5-ZF2cCKY7mYDYXcmPR8vFKMU1-bSwdN4F7_L6YMNb0D5p2gLYHFn4o5QsqtkwjEwv2Elx4RHOLGPYBGryBf6aMgHSyWYRytysq5niOhi3U9TyHi-8UgbJeKtyXTx_14tJr-mlCW2mAqIXtlca0YZw5ZG8x2wRS4iAonnkadpB6sDMet0dRwumi-Vbm2oXFC_n79M8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22822" target="_blank">📅 14:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=KfiUD7p9NB5s8kHZ1I9t9Rk6zaTBzJXRzB9Hx2nZrRqnaJQfOWOmNdJJipWgXoD8yQsxkp54gxTgESMAzk1vzOUDI8ggtxTwIqbhqDoyqVpgSttfgo1vdJNkdSeKGfllacFvJTpPuGoDILrOR1UYIKuP9Z3-IMYbd3a4OIOSCrZ-Q7OfIy0Es9phyN_ZvpTzFW6634h6_vzlq0AjboxnXM7lT5J628tvb2cLYxoFPFlTwHL3i1Wr4pGy0uF3yCWF7YpEzF6JgN50sHJMrzEmSEHgbsYQnpAmJt_BuiJO-rb5IExyt_6Rjo40yvKl2jJT-8mPybeJVCZqtGV3z4QWeGA3pKj_1uLNGGXydkRRLzrpNM--0WSUMXHbKcLumHKhhOFUpBbCehN6qF80TsSScFmlNvs0fbaWp5Mt2Z0z013f9X6EEfaDQaBtDtEvrBvxDJN7RBHOwqsRg-jSksejyrRFanq3_0rHZPtgwsNwNGQ2bIQLQCfQxF8-QIjOLZLQ1tc8V6kqwc7YK4jEPZyh9E47L54cmiJBBQ3lugLkOOHjWKEgQ1DbKZhaP4RkL2OvhEsW_dRJgsCgqe_DauUCI_ItD6awkuLPqckWePkTFkKsnavs7Y39IikJtVAXufzAokvCFcCAMvYBAOVtv3OtgujN6k5N9KTbBna253hqCwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=KfiUD7p9NB5s8kHZ1I9t9Rk6zaTBzJXRzB9Hx2nZrRqnaJQfOWOmNdJJipWgXoD8yQsxkp54gxTgESMAzk1vzOUDI8ggtxTwIqbhqDoyqVpgSttfgo1vdJNkdSeKGfllacFvJTpPuGoDILrOR1UYIKuP9Z3-IMYbd3a4OIOSCrZ-Q7OfIy0Es9phyN_ZvpTzFW6634h6_vzlq0AjboxnXM7lT5J628tvb2cLYxoFPFlTwHL3i1Wr4pGy0uF3yCWF7YpEzF6JgN50sHJMrzEmSEHgbsYQnpAmJt_BuiJO-rb5IExyt_6Rjo40yvKl2jJT-8mPybeJVCZqtGV3z4QWeGA3pKj_1uLNGGXydkRRLzrpNM--0WSUMXHbKcLumHKhhOFUpBbCehN6qF80TsSScFmlNvs0fbaWp5Mt2Z0z013f9X6EEfaDQaBtDtEvrBvxDJN7RBHOwqsRg-jSksejyrRFanq3_0rHZPtgwsNwNGQ2bIQLQCfQxF8-QIjOLZLQ1tc8V6kqwc7YK4jEPZyh9E47L54cmiJBBQ3lugLkOOHjWKEgQ1DbKZhaP4RkL2OvhEsW_dRJgsCgqe_DauUCI_ItD6awkuLPqckWePkTFkKsnavs7Y39IikJtVAXufzAokvCFcCAMvYBAOVtv3OtgujN6k5N9KTbBna253hqCwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhLFL-DTUB62kE-l7te1lWwq_JZiYl-WQR9n9hTcqFKu1_L2qRb6P2tNSWDi1LXQt5XC1NhgRbywBksJLZmeCw5oNZ4P-TQxc_SGRlLuZrpYu1YnV26EzM7g8WhcZ5IKl55wE5OmByGG3gQoDC1tTXedsxsoiPzmEZ9Hsns-By2Je8MOAQKemat-PQ6EkmCR0L6KU4Cgw2ilEN6Y4ZYrh85iKrUpkelO1DMPpUKndwqfPPCdUYU3tFgG1aAhRH91jHbFkiu_C6p8tszIz2hUOGT1r0l5oE6RN94903-ZJ9DMuehvbqslWPLyJKA6ud9Wqtw9bu9DKlpVMT-lvx-Bb8uU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhLFL-DTUB62kE-l7te1lWwq_JZiYl-WQR9n9hTcqFKu1_L2qRb6P2tNSWDi1LXQt5XC1NhgRbywBksJLZmeCw5oNZ4P-TQxc_SGRlLuZrpYu1YnV26EzM7g8WhcZ5IKl55wE5OmByGG3gQoDC1tTXedsxsoiPzmEZ9Hsns-By2Je8MOAQKemat-PQ6EkmCR0L6KU4Cgw2ilEN6Y4ZYrh85iKrUpkelO1DMPpUKndwqfPPCdUYU3tFgG1aAhRH91jHbFkiu_C6p8tszIz2hUOGT1r0l5oE6RN94903-ZJ9DMuehvbqslWPLyJKA6ud9Wqtw9bu9DKlpVMT-lvx-Bb8uU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
من خرافاتی نیستم ولی شما این بازی ۲ سال پیش پاری سن ژرمن با حضور امباپه مقابل دورتموند رو ببینید؛ واقعا انگار طلسم شده بنده خدا
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22820" target="_blank">📅 13:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpQsCKNdf2gVPLVK6qL7WzvAu76rTt8UWvEEbrg1IATbFfF99Ie11mi-YjeXYp1uFsKlZPc3rm_c4_xhj5kzmW4prf3VTO8kkMWaeqFjOH8BJt60RTisSJKGU9T81JrYf9RzvO6XCuSJySck1_8CmJmuzWMdLVqxJJK_Kk2ROh13RzyDuUx3vEOqMi8002iURkUZor9O4gL7A83wMJZrZhCbJlaG8AsAk1W0AVQwitYROfjnOBTjfKHxHrOvkIzDWPDXVKsW4NIt-cHds8TgnjynKmNvL0uiBGD_JthvLEKNfnHfQZ5a1tx7cJtkUuXjGpEnNS_qs2m9P5WzLHEWfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
#تکمیلی؛ باشگاه پیکان قصد داره درصورت توافق‌ مالی باباشگاه‌روبین‌کازان، رضایت نامه کسری طاهری مهاجم19ساله و گلزن این‌باشگاه رو بگیره و درتابستان سال آینده با رقم بیشتری به سایر تیم‌های لیگ‌برتری‌بفروشه. رقم‌فعلی‌رضایت‌نامه کسری 800 هزار یورو از سوی باشگاه…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22819" target="_blank">📅 13:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqS9GcK9Hrs-A3NJD490IIzFzdJH9csBFSbJkaO94fJa0ZBCm_4GHtSxT_geqBkrHpc9ohETDJyxJ4twy2xRowyIQa3F8ZcDLuqvRR5OIHbpjJgJtnKrhD6BLjWrpAE0Dhmc8DCV3EOfCsYaHL2lbXgoSHOH_RkPEqbm-Mp63hs12BUMDGpQmVo9sP29YST1sZKCfWduA7tyN2EyRCWZr0huE0M-cQtuFQmoPmNNwTWDWyhtuwnI3q4F8I5JgygIVDCTr53r1vQ29RPDuk1uIclgsivwvBWyyqI8Y6W9RkOtRJqnGWnB6-dYA_9CQddmchJKolLyFzYOml5i8qlU33wU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqS9GcK9Hrs-A3NJD490IIzFzdJH9csBFSbJkaO94fJa0ZBCm_4GHtSxT_geqBkrHpc9ohETDJyxJ4twy2xRowyIQa3F8ZcDLuqvRR5OIHbpjJgJtnKrhD6BLjWrpAE0Dhmc8DCV3EOfCsYaHL2lbXgoSHOH_RkPEqbm-Mp63hs12BUMDGpQmVo9sP29YST1sZKCfWduA7tyN2EyRCWZr0huE0M-cQtuFQmoPmNNwTWDWyhtuwnI3q4F8I5JgygIVDCTr53r1vQ29RPDuk1uIclgsivwvBWyyqI8Y6W9RkOtRJqnGWnB6-dYA_9CQddmchJKolLyFzYOml5i8qlU33wU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازلحظات خاص و بامزه پپ گواردیولا سرمربی سابق بارسا، بایرن‌مونیخ و منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22818" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9DaJd__KvJZLOui45ALMcEZP9_3wPy2TzYG8ej5gpM4WuRHZCy-yEbbEYkrFN4WFqY74DuUo1vk-ImJRc_wnovsl5n7lFx5lTqj6ggKHEX333_DgujXsuH70UgO56CYuiI6gZ0TDKZWmEXStBY0XMhjEEVRv75cvJMu_0lRS1z2sCXYA5JqQZbS_0-7DEvPYySXx40OTb3XmyBqIomBSZDAtR-f2CXX0zziNSW34MipxCqRt0eHiaTvM0NIJMAs9FazGCs9dhXCEEJzMd-f7-IJdE0zXLRHntc8rBecbb8wihx-lRSoMSB8aFHlPUz-azsYf2Xn1AGpBvxKGJOzeg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=hHL8S4TLSbOiTT1Kbg1Z3RFO0fMlVzRbHawEH1TEkXfOQntjI5ccmp5CGPfaMdDL3yFF-_loSswvyRpBpUh20GoXZelm8SJVc-Y0lCG0T60Wo4-tgITPuhj8sCpGahiodL310dtXYsETey-dPPPW2X0oY9OewmxRbtA_sTgbr4DjLrD_7EWY7162al1QrCPfHQJgh0CnmGfSN4Thm5CT-pmJpBwTs-CuBDysSLA6RYXyL5Lle6WEnXBToQUQ2jA5ZlMCI_f-ZxvhTwxUpTWy6tZPtiin9FGNTzj4tvR8bNAA3cAAuJ7N7Op18dT4i4aQy3-hGBsb5C8uGrP8qQVFl78S2gnI91DkAKMZQVI4QSKJOy1YKXkIbY9GuKmNps-BGFvIsW8H2oFFx_RU9x21MgFqnlZW4uBf-9rSO0bSa4Y8-RWFNbzQhFiTjNfDERdfgTtIPY6vT8bvBLDsDEbWwSCKdsDAOgkr8xNTVBY8Fl38wmI3UHu1IM7SX9amq_hYZf7IrrszaJ1U85cjNqb_4c8gTQht_fq9bVjBTMAgy4M-MvzqiQl3njxinJj5exW25w_OzJ-oJN3-ZHDfk6V5c3jL2Tdo7fUdG_rTuzJ0iT_EA3KkNAuVnOsPVuqf3sUqvhkzPbc50L-wCap-PvxV91J2cJw1wN1wExhlAVxOQZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=hHL8S4TLSbOiTT1Kbg1Z3RFO0fMlVzRbHawEH1TEkXfOQntjI5ccmp5CGPfaMdDL3yFF-_loSswvyRpBpUh20GoXZelm8SJVc-Y0lCG0T60Wo4-tgITPuhj8sCpGahiodL310dtXYsETey-dPPPW2X0oY9OewmxRbtA_sTgbr4DjLrD_7EWY7162al1QrCPfHQJgh0CnmGfSN4Thm5CT-pmJpBwTs-CuBDysSLA6RYXyL5Lle6WEnXBToQUQ2jA5ZlMCI_f-ZxvhTwxUpTWy6tZPtiin9FGNTzj4tvR8bNAA3cAAuJ7N7Op18dT4i4aQy3-hGBsb5C8uGrP8qQVFl78S2gnI91DkAKMZQVI4QSKJOy1YKXkIbY9GuKmNps-BGFvIsW8H2oFFx_RU9x21MgFqnlZW4uBf-9rSO0bSa4Y8-RWFNbzQhFiTjNfDERdfgTtIPY6vT8bvBLDsDEbWwSCKdsDAOgkr8xNTVBY8Fl38wmI3UHu1IM7SX9amq_hYZf7IrrszaJ1U85cjNqb_4c8gTQht_fq9bVjBTMAgy4M-MvzqiQl3njxinJj5exW25w_OzJ-oJN3-ZHDfk6V5c3jL2Tdo7fUdG_rTuzJ0iT_EA3KkNAuVnOsPVuqf3sUqvhkzPbc50L-wCap-PvxV91J2cJw1wN1wExhlAVxOQZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محبوبیت بسیار ارزشمند علی آقا دایی اسطوره مردم ایران و فوتبال آسیا در بین مردمان کشورش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22815" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2UO5YV2Vg8M_jRx2oncPfz9PxFotGZNnGYUYVa-y4ptBmXD9ujO_SMet6PuvTY4YXWUwDFPQF7homiAir_SXeRCaPOeDHrMbPSjIZSl-TxzpweuRyaYbjJFMH-tRYNJBXr6KyMHbM9QVQbSRPim53SkirP3ljHvsiHyMt-6HaijfbTU6mdmhraSII0iiSDSemjX2TvS2yC8bzctEaSloe5Gxg_3_JmhawPpja8MLDdVdXnVnE0m3NLaPbzFELXHvAf4pUTpukbMj-JrZmjrrPszT_HSy87S9qWk0YnydGVFlGsBkBuRWpQgLVZhhlrLsHGnKmuQlvMP45OGOqA1dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22814" target="_blank">📅 11:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPlBq3ZCzXJTr1N3iHAM3_zBZ55Tpm7KvJ7xDyw-pwlayy3thBeoulaiMCsU-O8cNFf2Dj4PqWIwzdm5o0srOvs9aA9U5kmZw6y0WJSzYU0xrZj5AkEbPXJFa9PyJICSTnKRbZ0KS4FRFwO3AMWuQ68ulX5Idn0Qk3y1g-4xa6Xf2lFX92_-o-hExmCKsiTzL1QRUgTTtrDe-8kE8SXPj-GKAt16ET2fHOIZY_Q39zF-3mqVekIgRQAiLS845uFG95UQ37AqxV_i6LhZUvWBAuXlnnvnlUCWjtRB0lK2kypVYssOdbrMyZvnTciCAdeRNrpBPNslagpXjjAAJmWq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت باز شدن پنجره نقل‌وانتقالاتی آبی‌ها؛ باشگاه استقلال برای فصل آتی رقابت‌ها برنامه‌ای برای تمدید قرارداد آنتونیوآدان گلر39 ساله‌خودندارند و سنگربان سابق رئال‌مادرید از جمع آبی پوشان جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22813" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cemmuIr-bwL1GqTTFr9dxDmBqPtuQE-mV1iQG9memKfkxFHFx-hRHI6QTFnstgMbH9fYCjt7BnTZIiS1lpxOAQ69Hn5tGQquSo-k-qCq_rPpzj0aI4ouwmegfUBO0YwZ_p2yidq2HDrb_Sfk3foNQCSPv0ZryOW5Ix2ssQIR8ybgGIKQiGhwLBo4RuJ9nMQqY6KZsrE5Zkv1XRf68j6-liWI2rLMYjtKJB9LpyrTeHrhd5Hn5EfMg71pUeAVWrjv6zlbvzM6r0p8VrXMmV2dmkPoSCRCQF7RmjsKRTR0V84-MH-YGXpsoQuL1KkS2bGgEBl-YwMnTaGd9g9ybUpWTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssGMPg30m6M1wukMgItM28siCmcVRcwvpPF12S3yLF8OGsxm-I_LqKtJ_9J1Exwj-zmsmrvAyI-gCZtMNFIb7NFfHrej_AU4odQq7TZzs21y1rZtvcucxj2AbHn8KFswOMrUQJjjNVcTwG9APB6PNTVnZ8X_fc5X_ZlKrZLkvn1JEb2qaJhyiyzWWSlM0iJhVmt-eV-d6hOHeUQJqslTjmWG3USAn1biLT68634KvnoobGK7QlOcJatrdEwkFp5UqKsEGFIq9hOxmGMbJmlxgI6uDQ7MKcE8DSp8HmLx6KXx4nnaBLINhgr_v8JVN8DQTOeOKzHDD4BsEvosjfQdkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22810" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARcVNAHR8Ki7RXGKEHKl-eT2h_szc1P80uCOhRKnM4mgZlubEMdMa9roIUxDhuP26qOKcFfxKqvyaHs0dmSMj3rLkyQQKYQOrF7gSddC4UacBy4bqTKoAHTeEhfi-l7I6LXNZMAXW7XDI59_HBlEpHAS5KwZeOOEhM0cje3K4tKeFTtmIvanhnqyh5Xm5fJgGB8ic7xcm8hbf3xCtxIAcLB1Md5eyYzwEgrl2ac0HBaf1iQ63uShD4-JsGDHb_4kSIxMwgeEOmFIfUl2qYjwtSDcsUSU0bTbdBhlEj0npDy219ICDdRgbvTmRo1U5cvAFu0aVspBH2FByyFeaNrwRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شماتیک ترکیب تیم منتخب فوق ستاره‌هایی که مفت جام جهانی 2026 آمریکا رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22809" target="_blank">📅 10:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22808">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUsMDg_fy6ub_K6I-787-UBN6P8M9a8mM1loBIsloW5jaRp5wMOFKDPPNaEpJ0YqmpqclPPRxaS-ssL2QcATrGwdfjXLGmiusOrzDQxuk3sQYrqB_IUJbL4dqxgYxEawzjhsV1enirfYnLb0Hbz86-BjP8qmi9TBdWfScr3L5DuFwe_4nn_HHsAdGTrW9aG21p4bjuktxfpZi4Je-_kJAjJ__WB3JWa27I5REx2Y2buB-5EoCRMrsinNQklBUbKsu_V4DReCLJhYgJBYBVG4kgB2XapepQ4m6KX4_WO8HKGMWBsaiOIVzSxvBdPESQPR2OgNdgCPRvhDV-w_EDZsFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/22808" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9EPXOhBgA9KFA729jQ_mVv5nxQPL8OoKom2KuwDpgOrw448dknkZg0YObrtApakn5mNxCbJQ10uson44f9I5EgHhO3gUsNqvp4lMPrXSGydzh2DPEGxVKAN71AsLAOWLUAucd_E9A9bkF1JVBTiP-A9t197b1v6iAewHVEKTooASYsFEKJNhQ3Py8i5g1N-PCSQRvRPpaK0XRCCfPUPPRDCTx9m-7PDjxjod9VbsvgmRUZ6yDDFJ3BcZwUkc4Wx4BGt5710tNFnIOkfEYE5-ZxoTsDqL8hbY6EgOb-t2-aHwAyKFTfmixzG1F8-sgtieSuEd-FQgG_rjTQ2Nn5T4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-3CV4mhsT9eAPJdJ0YOb2UkfcTCsuCtJFBCQV_RUX8j07pr-Rn96ONhNem_2JyCwwhFxpghV0zFz9ucf31Z0vGdgTiIcEt2dQQQeE3USnZDl9u-LhP4HnVVZHRc6X_ZO9E8Un4Hn6n__KOFwmO3EnBgDy9PDkImYticWae6ip2C1B19qLnSCarEsyPFrIFYsBl5JR80PM4O5ekphwzFlE4CqQFF22Fg6bLeVjNq2C9VjFiABEOATaRNkMoyP1uiRhk9jKjMFRSQ3ZwpeLPgSpg_qRSlbIkf19VcoEdKXR1ijdfao8t7ayP9k8mMB32c91mMwOwLkLq9Ebrl6_ny1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0d6y8UoEM-FVD-DFylhF82LCuzujH3Dy-qv5nJAqKcmD2NptCFASamH3VqGfCuUJFnBcN3XGJI6k5fI8Vhdi129hDeT-eQsCEOEvIrPDE921mWwh9c1FUMK5OaagjMPLFVoMmSre5Yyzazu741jsHpxhPHASSRNUGP9AUhDU6teLmo59hCGitd__VGoTPoh__EF8U72SRsQlvOLssG7IbX-htb6fkiqSmdUvj0Oasul1ClykKvcjBUK8vZCazCHG-kfq71ly2K9-rlmXu8tauuJmlFTvSPuTA2pOWEylv7gQGMYNJ-xqz70yxtmfJ1FuEUTKYJMOogpQK67vrGQng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_zGAKod6aOU_zonasa-9w2kxxmx1ZeXAkWd5jfVKQEBVVfYlHzVs9vfZoamAA_67BHpv9PQO6PaaDl9ZdCP82oL-wFbOHHUr2lJQs6K9OokPlGObHoB8lwhFtLJm8QCFITddsvWheHGmjxUQ7WjThChSCvo-riF4qFoBJ7qD0dcuf0--1AJvX7rAYOhNgliGYngD44rAHAr8dCvOK1NLY7fXZRMjCAnr6CRCJYCWH0-SRYEO-_epPOrJjWEYD-Z8JOrSKy1DwFpe6cpylr4CeXxxHE_-__EnfklVV3VuIFEIfx6X0dX0HFm_dAOUprxXyjr9cy_nRJbCt48kz63TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJMrR9ZzJ6mxxgiS3voFJuv8SmZmYk1YYr-ONd2-GPs3sXXS4M2ohsmNDqNt9EV2NDe-qn3pYkTmAgUYA4_Ih9M67imsnGbHSN_qL3EYzdgpVmEI3u1g38Xn_sTUP_TFrevO4CJ1d6R8QxsPx_9uTgujg9c4xdy90li4xgMNGCWt6uDOP0QN94WkQ6gyhR1YvBvwG1_72eI5oupuxeQQ1HgHLRSTdf-eztrxzl-sqDpyfYWIPYCmxwN1y9uRAHxRhfVtCrMPHp-YnrprhE-zT-ZmP_b2-az0zJg76_JTlze8zhY_4dtEfJcc2zopve_zn2rqbUVQXaJIRHw4IIj-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
