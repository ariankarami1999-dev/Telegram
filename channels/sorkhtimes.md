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
<img src="https://cdn4.telesco.pe/file/ceML0zhtlD_dDClh53uFW7cgMw6-_RudnrZLzcInUCmVt9F_tNUuuqkHlyntAD5mOpn5it87DxDuT4xQC-Dyyf_U7_L0g1LjZemaM-r-UEqZKNOgB3-fESs8wXk0M_QXzbrCRufJPvPk7dZ6319wVb5MAVp2t-OUSkrnvCQCy7KMg8yozWvQ00Tq1tpexL3EBdYHBcPuUg4c0Zcq_D3BDQa-J6Nn09TwBrAFcl7wPRHQD0BdGf9vfb7wsYNOSV6USJVH7Bvp-Ow6831c7kT3ssV3hGTerkvhIo0swPSfpOF5EzOrulCPMS_x1-kwhFAYyOUpO-VShDG5ck2hmZe1Ww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 08:58:33</div>
<hr>

<div class="tg-post" id="msg-139747">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESoSKoqMlmhffZ2qMOrrv91rZ0fqr_PMNkNiQy7TrsII82Gc7nCkQjIYs6GAWDz7Utt7cpVkidvEVjzCa5agA3UIzQILNmzX8WyiTCrBF6IdT7yFAtX9C8F66IqRH5ObtHogSY3Nx6ztgfJNbrqJCOasv_eOedRtrye6oIp8nV6POV_GPeO4tAZD5e4grU4pKzdK7KjgTIP21Dvi-xeZSN648CMhpmimqPQ2Bd53UmnCcC6IBJsNtfK00o4ulsy-_UA8ZqwhLXW5CG5QcOLa840yox6vA9in9DlvU9uGgmuD9y738Adh-G8DG_5G_q7N2tHbhhLY4ESaPYDBzveboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
جدال جذاب در یواس اوپن
🔥
[
الکساندر زورف
🆚
لوسیانو داردری
]
⏰
بامداد سه‌شنبه ساعت
۰۳:۴۰
🎾
زورف با سرویس قدرتمند و تجربه بیشتر، شانس اول پیروزی است.
داردری با سبک جنگنده خود اگر ریتم بگیرد، می‌تواند زورف را به دردسر بیندازد.
با این حال، روی هاردکورت کفه ترازو همچنان به سود زورف است.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SorkhTimes/139747" target="_blank">📅 01:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139746">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
✔️
پیراهن پرسپولیس را بپوشید و به تیم ملی برگردید
✔️
در دو سال اخیر گولسیانی ، گندوز ، باکیچ و بیفوما از پرسپولیس به تیم های ملی خود راه یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/139746" target="_blank">📅 01:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139745">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/139745" target="_blank">📅 01:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139744">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
تازه میفهمیم که چرا ارونوف و روی نیمکت می‌ذاشت تارتار ‌..واقعا آماده نیست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/139744" target="_blank">📅 01:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139743">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ae53c901.mp4?token=JC3z-OWFwF5_g_grZU-j9WLksGEEf72ynGCLtxpz6LpnQnpJJK8muzBjfKDfNTIMmkkxgW31mBIgiamWrfmZRL0vnWzyKBRLzynfxYIUPsl54hp06DKROwg_GU6LjdbKNYHsqjlDMpM_nvd1meiUADqFpQw16X10lNN3MwaELuM9QpbCwv2lpJM9VemVQjUFam5IV6k3rCOa_YaETbMUrF5-jjKA61n6oyHf5R91CGZ4TOmaff-mMs3NHjXK1sGYDmdHpmy27a71BUwJaPWEAt1pkDJ2QE01FUEhe7-Mx8akffseT3SPrQKyXXESsRInx-Ffi7kRD_RhxmNFRvUGOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ae53c901.mp4?token=JC3z-OWFwF5_g_grZU-j9WLksGEEf72ynGCLtxpz6LpnQnpJJK8muzBjfKDfNTIMmkkxgW31mBIgiamWrfmZRL0vnWzyKBRLzynfxYIUPsl54hp06DKROwg_GU6LjdbKNYHsqjlDMpM_nvd1meiUADqFpQw16X10lNN3MwaELuM9QpbCwv2lpJM9VemVQjUFam5IV6k3rCOa_YaETbMUrF5-jjKA61n6oyHf5R91CGZ4TOmaff-mMs3NHjXK1sGYDmdHpmy27a71BUwJaPWEAt1pkDJ2QE01FUEhe7-Mx8akffseT3SPrQKyXXESsRInx-Ffi7kRD_RhxmNFRvUGOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣
حجت موتوری مدیرعامل ترتر: به شجاع خلیل زاده و علیرضا بیرانوند در بازی با چادرملو فحش ناموس دادند، آیا این درست است؟
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/139743" target="_blank">📅 00:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139742">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa88055fa.mp4?token=awt2_GhO1nGZcqI4FlfZJLrPu_xzFFgKSJNrx5hexbShcX5aHE2PFtI_lr62HKgcSirAts-HroD7RyQmxLxIXR_aL8C4w9z0sqGc1g2heR5bd1rrBmssMgQjeO15b7N_6Mi_y_e1XsFbM2O0u5h1vo8buxl4ixX5kF6s2X0IwN2Da5I7wJn4Z_9UkWwfF1Qf7q4uRPHJgGAuJoVEXFlYHXq69ZWk2GFvLU92b8VfyGz0eKDn_48N0PRJDPDZMA_QhevySRaCbXVhl8Ku866ntWTWJCn6MV_HYlPTO3E6f0qO5pcReIlph-dx-qyCtJEmOpz2KYtPX2tudYIfD13Low" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa88055fa.mp4?token=awt2_GhO1nGZcqI4FlfZJLrPu_xzFFgKSJNrx5hexbShcX5aHE2PFtI_lr62HKgcSirAts-HroD7RyQmxLxIXR_aL8C4w9z0sqGc1g2heR5bd1rrBmssMgQjeO15b7N_6Mi_y_e1XsFbM2O0u5h1vo8buxl4ixX5kF6s2X0IwN2Da5I7wJn4Z_9UkWwfF1Qf7q4uRPHJgGAuJoVEXFlYHXq69ZWk2GFvLU92b8VfyGz0eKDn_48N0PRJDPDZMA_QhevySRaCbXVhl8Ku866ntWTWJCn6MV_HYlPTO3E6f0qO5pcReIlph-dx-qyCtJEmOpz2KYtPX2tudYIfD13Low" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
حجت موتوری: ویس های فحاشی خداداد را دوستان اول دادند به شبکه های معاند، اول آنها پخش کردند
🤣
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/139742" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139741">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومانی بدون تغییر ماند؛ افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
✅
✅
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/139741" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139740">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
🎙
⚽
🇮🇷
عادل فردوسی‌پور: وقتی به پرونده حواشی دیدار تراکتور-گل‌گهر نگاه میکنم آدم عارش میاد بگه به فوتبال علاقه‌منده! این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/139740" target="_blank">📅 00:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139739">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b0cebd97.mp4?token=mO46ngW_JtEZyIZbPMPYequsqyYU8jPD6VaVRU3h_ZNxRnC5_82hgWCCbA2kc3LEXPIQMYALzS9O9EJN5M-gDl5tYGbbBbHH9-ifFS-gFnsVgyymzYa91qb4yxR0nYPUGVCm4nyMn13pGhjxB3UgyvVZ2rgP0e5_pWu3cP9VIOlIa1_r1t3agxrTC2LyjKR3MatTPkPUaQYHzbNAqCj6Zr-RpmTZaZ291g5ky0GSThndYCL8v4zoAjosNIWWXPZfN5_P1RUi1t8UIwTFogZiHt3_jtbGON3eJGi7otyBVte-B8Kf4CbknP0VJb423tI-V7T3TUaHintIH1oAfI_5Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b0cebd97.mp4?token=mO46ngW_JtEZyIZbPMPYequsqyYU8jPD6VaVRU3h_ZNxRnC5_82hgWCCbA2kc3LEXPIQMYALzS9O9EJN5M-gDl5tYGbbBbHH9-ifFS-gFnsVgyymzYa91qb4yxR0nYPUGVCm4nyMn13pGhjxB3UgyvVZ2rgP0e5_pWu3cP9VIOlIa1_r1t3agxrTC2LyjKR3MatTPkPUaQYHzbNAqCj6Zr-RpmTZaZ291g5ky0GSThndYCL8v4zoAjosNIWWXPZfN5_P1RUi1t8UIwTFogZiHt3_jtbGON3eJGi7otyBVte-B8Kf4CbknP0VJb423tI-V7T3TUaHintIH1oAfI_5Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙️
فرشید اسماعیلی:
✅
کابل VAR را کشیدند چون عجله داشتند که زودتر بروند؛ در گوشی به داور گفتند که پنالتی شده اما داور گفت من سوت پایان را زدم!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/139739" target="_blank">📅 23:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139738">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
تارتار سرمربی پرسولیس: هوادار دوست دارد تیمش هجومی بازی کند/ قبلا هم گفتم اینجا پرسپولیس است و هواداران بازی زیبا و هجومی را دوست دارند
✔️
✔️
واقعا یک تیم کامل داریم و بازیکنان دارند روز به روز بهتر می شوند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/139738" target="_blank">📅 23:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139737">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/139737" target="_blank">📅 23:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139736">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
علی علیپور : به هواداران عزیزمون این برد رو تبریک میگم و گلم رو به علی آقای پروین تقدیم میکنم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/139736" target="_blank">📅 23:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139735">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
🎙
⚽
🇮🇷
عادل فردوسی‌پور: وقتی به پرونده حواشی دیدار تراکتور-گل‌گهر نگاه میکنم آدم عارش میاد بگه به فوتبال علاقه‌منده! این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/139735" target="_blank">📅 22:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139734">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTMJ2zMUvj-OfYYtEE6MOCuuUUWn_vVF-acFkCaXNK8LScWqNEE94W1JmASZim7405KwN6rV98P3Y1MsgmeQ5-hlETNEJ_Gtb1mkXof-z1Vr1vEFv9bfvuzeg5YOKN8GuVlEiqi9QOLYjh6ZYofj_9a4ey4mITPFRIlW0dyS8pOSRfhyTd28-X30y1GesW_uksH0DMYw13g3-mec_1dI9HvJh6IFgSzl8Dx1ak3WzO-cWbCtel5NoktBFlEB7ERyRwIKNeyPc9LLjVAiEPq5ySc6yRTOqr_UEPt4R8JSpbVpFbJTeNQ2NpD_vYzk8sJis1EmO-46U0ag3mnQqiwEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک به اوج خود رسیده!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/139734" target="_blank">📅 22:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139733">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zcc0rkt4lKFJroMkG-MqeIRyDp6ApjABifMqTATY0bdYu_JeXojBMuVOknXONJXyknQDNes_t3Eaj8_I0w6tVmYpCEs6HzgeCY6qf37xXFFx_Ixosc9y8aJtgA_Tk9B2wWWsPLe5_ngYAG7R742SawRqLvFg0Rdr5gjGoI9KeaIBMTb9ovU7tRggeG6Lx4TEiTYSpuSAMMPPaDb-NjXCqU7yNH4MU20_5E6KK4jQoAwypZ6WQi-NkYtlO157qX8HLgJ3UGamsoTbmDwCWZ3_JjJrSuR_G4OvnEcjd1-XGPXIkvm1ZO_ziDT0QFwvcEZtt5W8tizPKB2Q9B_QcNB7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج هفته ششم و جدول لیگ برتر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/139733" target="_blank">📅 22:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139732">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: ما پیگیر شکایت از یاسر آسانی هستیم و برای اینکه پرونده را به دادگاه CAS ببریم ابتدا باید در کمیته انضباطی شکایت کنیم و جواب بگیریم بعد به CAS ببریم
✔️
بعضی ها می گفتند ما اورونوف را بازی نمی دهیم که او را  بفروشیم/ واقعا خنده دار است چرا باید…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/139732" target="_blank">📅 22:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139731">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
علی علیپور : به هواداران عزیزمون این برد رو تبریک میگم و گلم رو به علی آقای پروین تقدیم میکنم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/139731" target="_blank">📅 22:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139730">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/139730" target="_blank">📅 22:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139729">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
گل اول پرسپولیس به ذوب آهن توسط علی علیپور
🔥
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/139729" target="_blank">📅 22:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139728">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
تارتار: فشارها علیه پرسپولیس؟ هواداران ما امسال اتحاد خوبی دارند و تا زمانی که این اتحاد باشد ما آسیب نمی‌بینیم
✔️
✔️
کری‌خوانی نماینده‌های تبریز؟ فوتبال از سیاست جدا هست و درباره فوتبال، فوتبالی‌ها باید نظر بدهند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139728" target="_blank">📅 21:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139727">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
تارتار: در روزی که خوب نبودیم بردیم
❌
❌
سرمربی پرسپولیس در روزی که خیلی خوب نبودیم اما بازی را با پیروزی پشت سرگذاشتیم/ چمن ورزشگاه شهر قدس خیلی خوب نبود امیدوارم این چمن را درست کنند چون امروز واقعا خوب نبود
❌
❌
واقعا جای سوال دارد که چرا کیفیت چمن افت کرده…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139727" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139726">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
کنایه حدادی به خداداد عزیزی : در این خصوص نمی توانم حرف بزنم اما فقط به آقای خلیلی جنگجوی و با ادب خودمان خسته نباشید می گویم. این نتایجی که می گیریم او هم تاثیر گذار است و در کنار خط در نهایت ادب با جنگندگی حق تیم را پیگیری می کند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/139726" target="_blank">📅 21:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139725">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: دنیل گرا با باشگاه قرارداد داره و  بازیکن ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139725" target="_blank">📅 21:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139723">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
🤩
دکتر پیمان حدادی، مدیرعامل پرسپولیس:
❌
امیدواریم روند پیروزی‌ها ادامه‌دار باشد. طبیعی است که از بزرگ‌ترین و پرافتخارترین تیم ایران، انتظارات بالایی وجود داشته باشد.
❌
با توجه به مستنداتی که در اختیار داریم، درخصوص پرونده آسانی از باشگاه استقلال شکایت کرده‌ایم و در صورت حاصل نشدن نتیجه، حتما پیگیری‌های خود برای احقاق حق باشگاه را از طریق دادگاه CAS ادامه خواهیم داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139723" target="_blank">📅 21:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139722">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
شادی بازیکنان پرسپولیس با هواداران پس از پیروزی برابر ذوب‌آهن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139722" target="_blank">📅 21:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139721">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=ch6ejz-1d45N1rE3SmCmrK1QXuG5Aq4y2-7EOTI4FqlDWc4E1wqQAoXSKRg9YyJAsbSogN29s-vw1Uc2nBFiA089ryNiQ9dAMbRWThwjyfrC0AuqPtQRCioGx1NlBph9pWqTuduws-36aCiiXCxeiV-piO2_uwyb8N7JZZ79jaxhU8RYkccYvCEn99fdTJezqbkPP88fV1LHPVYd-TTCh2XjIssUh2kq8RXrxZqlgG8P6msYxp68yh5gnaspV_HYYInkQUSVXgomY9uMyiCzcYIoHQ-hnfpUdOlybpIjLu40PevP4pd0gUrHskYXsWIxkcK0B6Tb1jOh6dJaDBVTMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=ch6ejz-1d45N1rE3SmCmrK1QXuG5Aq4y2-7EOTI4FqlDWc4E1wqQAoXSKRg9YyJAsbSogN29s-vw1Uc2nBFiA089ryNiQ9dAMbRWThwjyfrC0AuqPtQRCioGx1NlBph9pWqTuduws-36aCiiXCxeiV-piO2_uwyb8N7JZZ79jaxhU8RYkccYvCEn99fdTJezqbkPP88fV1LHPVYd-TTCh2XjIssUh2kq8RXrxZqlgG8P6msYxp68yh5gnaspV_HYYInkQUSVXgomY9uMyiCzcYIoHQ-hnfpUdOlybpIjLu40PevP4pd0gUrHskYXsWIxkcK0B6Tb1jOh6dJaDBVTMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
واکنش جالب هوادار تیم به عملکرد پرسپولیس: بارسلونا هم بیاید در این زمین شکستش می دهیم؛ 2 تا به بارسا گل میزنیم 3 تا به رئال!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139721" target="_blank">📅 21:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139720">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809956e0a8.mp4?token=kSrO15e5oiT3J6xwCFCNhdGQINGph43drYETm_KicQCpInyQRnyXdm-xK5OvLEczBVGB-iw77Thh5SOp-uwPU5NFHz2AaIpz_dmVKvb_AC73MV8yjmbuc8CRTDVF9otKrakJv_y3w09O0yM9R838gP2iPFZ4DplYDYR-PabpEvSW6jmF43_N_M7FnJuLac6v4ae3HcUxSw54MD6a6isgHa3qAjgSyZ5m4tNSAlxICys2eXEe-oNo-k47iBLq0zlAb2LHk2Kw0rPYcMS2URqaYcbl46xUorPyU43ijUCFWjr154BuWBP21KFAs6OdgA19EJPoT_ev5f_TdheIihn2Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809956e0a8.mp4?token=kSrO15e5oiT3J6xwCFCNhdGQINGph43drYETm_KicQCpInyQRnyXdm-xK5OvLEczBVGB-iw77Thh5SOp-uwPU5NFHz2AaIpz_dmVKvb_AC73MV8yjmbuc8CRTDVF9otKrakJv_y3w09O0yM9R838gP2iPFZ4DplYDYR-PabpEvSW6jmF43_N_M7FnJuLac6v4ae3HcUxSw54MD6a6isgHa3qAjgSyZ5m4tNSAlxICys2eXEe-oNo-k47iBLq0zlAb2LHk2Kw0rPYcMS2URqaYcbl46xUorPyU43ijUCFWjr154BuWBP21KFAs6OdgA19EJPoT_ev5f_TdheIihn2Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی بازیکنان پرسپولیس با هواداران پس از پیروزی برابر ذوب‌آهن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139720" target="_blank">📅 21:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139719">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS_6DB41fCwqithmIQjT9YYQwU1O-SPOpta8o4GU6jAWQTBIbn4m7v-0VgyfnsDH0ryWdSnJsl02nFt0kIrSoMrtknzS6M8ULNfFhJxLQjVqjHGcjcnWBWYDkyLnCLGg-nKq3M1eS0G47G4mOLCgyRyTHF-gHzOk5Spz_ofCdqPkbLkiZaFlOeO5InPLM81pJjUqiuJlRys13ntem8zESsrP3HPrnfJN1hW4K-gx130lTOYoTgolXWMO_2uqpKYFP25PE9zKGO29FzGQXosJKfXMmm9J21_NZujdmQmxcdYMN2T4cYzhYVVaT9pAeX1OgzxJaZ20mwwsGtOgnA2KtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
علیپور تاثیرگذارترین بازیکن کل لیگ تا هفته ششم
✔️
6 بازی، 3 گل، 3 پاس گل
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139719" target="_blank">📅 21:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139718">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139718" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139717">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=rKBDS4IxOSPKBcpkinXiygFaHoNuBUY8uwnX96iE8LNAaWj7UTb1fbIsK-_i6DRdu1F_NzgNrmPdDNjN9ibcEoKj8KBjT34DZz1plkwjShke8HoOpvuG2peGoXjTZXUFV6t4WlxP4Q6n8AsnA5CW8euAfMbtGusoW5q5etV4gUlJn447CWy06jTF34ZvLPnaUekR1zyVw6Z5AYCxPgZgHwW-usU_xragne35n8_hpBSkTcxZ4QzL37aprhNU6VTRYOPgf__AiJMcuvlMEfsq2W544YRYT8KHcAy387F7z7JZ6YJMrvku6Lq7ImDonPysUEHiGBry47uShdmmBVT1yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=rKBDS4IxOSPKBcpkinXiygFaHoNuBUY8uwnX96iE8LNAaWj7UTb1fbIsK-_i6DRdu1F_NzgNrmPdDNjN9ibcEoKj8KBjT34DZz1plkwjShke8HoOpvuG2peGoXjTZXUFV6t4WlxP4Q6n8AsnA5CW8euAfMbtGusoW5q5etV4gUlJn447CWy06jTF34ZvLPnaUekR1zyVw6Z5AYCxPgZgHwW-usU_xragne35n8_hpBSkTcxZ4QzL37aprhNU6VTRYOPgf__AiJMcuvlMEfsq2W544YRYT8KHcAy387F7z7JZ6YJMrvku6Lq7ImDonPysUEHiGBry47uShdmmBVT1yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139717" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139716">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
باز هم تعویض تارتار جواب داد ..گل دوم و شهر آبادی زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139716" target="_blank">📅 20:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139715">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
باز هم تعویض تارتار جواب داد ..گل دوم و شهر آبادی زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139715" target="_blank">📅 20:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139714">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
گل اول و توسط علیپور زدیم با اینکه نیمه اول خوب نبودیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139714" target="_blank">📅 20:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139713">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
اعلام رای تراکتور و گل گهر؛
🚨
خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139713" target="_blank">📅 20:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139712">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
اعلام رای تراکتور و گل گهر؛
🚨
خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139712" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139711">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139711" target="_blank">📅 20:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139709">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
این بازی و بچه ها با سه امتیاز بازی و ترک کنن برای بازی بعدی بعد از مدت ها یک هفته تایم و استراحت داریم ...و بازی بعدی یکشنبه هفته بعدی با خیبره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139709" target="_blank">📅 20:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139708">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
تیم خسته اس ..ساق بچه ها خستگی داره ..امیدوارم نیمه دوم با آوردن صادقی و بیفوما و محمودی بتونیم از این خستگی رها بشیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139708" target="_blank">📅 19:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139707">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
واقعا چهار روز چهار روز بازی کردن تیم و بچه هارو خسته کرده و واقعا تو ساق بچه ها خستگی واضحه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139707" target="_blank">📅 19:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139706">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🏅
پایان نیمه اول
🏅
پرسپولیس
1️⃣
_
🏅
ذوب‌آهن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
0️⃣</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/139706" target="_blank">📅 19:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139705">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1X2CqKy5P0TX-hhgz23MRUpdG70luoqEbM2dkUm0dFSpfr6zILmnUV23FoIibc5yo6JI7qY7fjWtAftYsirT9rZzVA6SpJ22kf0UIV9HIFrckTg1ru0o2p7WvJ9x-KHCixhPKhKyKu_Navpl8GuZKt1S94QDW5gEiRJ_cmLSyNONfO30Pc-zgz1SCUJc0YIRQW_lSmeLBMu69rSffw5i09tfARqQdKKnSVTsvVkrHFdMvCfYVucvZUM6PKimRfHoich6H1MBUXGv6DW-k8uEYQtuUXR0mUGgRbMjM-Kk_rwh62gj9SwUQDqj25nH0YCMErB_woU1sPs_ZaOUwlKwCWE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1X2CqKy5P0TX-hhgz23MRUpdG70luoqEbM2dkUm0dFSpfr6zILmnUV23FoIibc5yo6JI7qY7fjWtAftYsirT9rZzVA6SpJ22kf0UIV9HIFrckTg1ru0o2p7WvJ9x-KHCixhPKhKyKu_Navpl8GuZKt1S94QDW5gEiRJ_cmLSyNONfO30Pc-zgz1SCUJc0YIRQW_lSmeLBMu69rSffw5i09tfARqQdKKnSVTsvVkrHFdMvCfYVucvZUM6PKimRfHoich6H1MBUXGv6DW-k8uEYQtuUXR0mUGgRbMjM-Kk_rwh62gj9SwUQDqj25nH0YCMErB_woU1sPs_ZaOUwlKwCWE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول پرسپولیس به ذوب آهن توسط علی علیپور
🔥
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139705" target="_blank">📅 19:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139704">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
واقعا چهار روز چهار روز بازی کردن تیم و بچه هارو خسته کرده و واقعا تو ساق بچه ها خستگی واضحه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/139704" target="_blank">📅 19:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139703">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
تازه میفهمیم که چرا ارونوف و روی نیمکت می‌ذاشت تارتار ‌..واقعا آماده نیست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/139703" target="_blank">📅 19:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139702">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
بریم برای بازی شش امتیازی ..امیدوارم مثل بازی های گذشته از دیدن فوتبال پرسپولیس لذت ببریم ...الهی به امید توووووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/139702" target="_blank">📅 19:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139701">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzBECpwe9h3lS9FYPe40SBdQ2TxsHxFWl6104f_6p3jG09Z9CRfbVDVQswyzLyadNYFm5caY5bJDppkV7L8xnkqVosc_EdexuM3BDcq7lkHjCoC7SlGi9hvqiofZv6GGnWwQE0isz7rpTtqAnxkq0FQTp_mvK7gjDcit9QYIdoB9WEa7YKOz-Lvq0BReqpUYz8rKmi7GbBWh6lv-Oq8vTF2O54VPT1H6pygxeyfhtPXGC9zekKXJx189jfh4R6MELABFIlPBTDn05eiYrpjQEKZ9M3LOd12W-vAxriZ8Zh8Jmu6vmnUY6l_fuStjk9kyyFBtKXn0kh32gjjsCbmEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک به اوج خود رسیده!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139701" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139700">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
شماتیک ترکیب پرسپولیس مقابل ذوب‌آهن
🗣
اورونوف دلها فیکس شد
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/139700" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139699">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
هوادار پرسپولیس درباره جنجال امید عالیشاه و خداداد عزیزی
❌
❌
آقای خداداد عزیزی به قول سیدجلال ما پرسپولیسی‌ها هیچ چیزی از یادمان نمی‌رود. خدا نکند که ما پرسپولیسی‌ها با تو رودررو شویم؛ می‌توانی از بیرانوند بپرسی. مثل خودت با تو رفتار می‌کنیم. کل افتخارات…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/139699" target="_blank">📅 18:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139698">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
✔️
صحبت‌های هوادار پرسپولیس درباره اتفاقات بازی تراکتور- گل گهر و حواشی ایجاد شده میان عالیشاه و خداداد عزیزی!
❌
❌
از کمیته انضباطی سخت می‌خواهیم برای یک بار هم که شده رای درست بدهد.‌امروز نشان می‌دهیم که هیچ کسی حق توهین به عالیشاه را ندارد. امید عالیشاه…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/139698" target="_blank">📅 18:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139697">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/139697" target="_blank">📅 18:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139696">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
ترکیب بازی امروز همینه و تایید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/139696" target="_blank">📅 18:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139695">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=mT7pmRL-y_GZugo2vfO0t0HsFEGryug_hoRnXmwRhPvscMJWz9mP-WIXr-5E9TA8H0Qk0BiIzJcjqBLSisWr6iJ5tB1xby3HQbwl6ZrN4M34QMG_JNuPoSZkzaiPsczdTI5cAKkRiMwksY_5uxj4FTHOMtf4zxTsTouQK1gXt81XpF9OIiF_UC0NkMDd34PyyPlkx_lCaEIs-GB7LcLLIz_sRGUHfT77-3WW-dpTZ5huN3A6OdJbaS6KRo7XdW85LPPkhvDHJbqI4ip4fKmA3I6tzplxqSChpYizR21mopSBHINuEfUrZv3DkqZrksnyo0Ds0MMrApdaUAITCA71Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=mT7pmRL-y_GZugo2vfO0t0HsFEGryug_hoRnXmwRhPvscMJWz9mP-WIXr-5E9TA8H0Qk0BiIzJcjqBLSisWr6iJ5tB1xby3HQbwl6ZrN4M34QMG_JNuPoSZkzaiPsczdTI5cAKkRiMwksY_5uxj4FTHOMtf4zxTsTouQK1gXt81XpF9OIiF_UC0NkMDd34PyyPlkx_lCaEIs-GB7LcLLIz_sRGUHfT77-3WW-dpTZ5huN3A6OdJbaS6KRo7XdW85LPPkhvDHJbqI4ip4fKmA3I6tzplxqSChpYizR21mopSBHINuEfUrZv3DkqZrksnyo0Ds0MMrApdaUAITCA71Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/139695" target="_blank">📅 18:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139694">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
✔️
نیمکت
✔️
امیر رضا رفیعی
✔️
ایری
✔️
ابرقویی
✔️
جلالی
✔️
باکیچ
✔️
لطیفی فر
✔️
یاسین
✔️
صادقی
✔️
محمودی
✔️
بیفوما
✔️
شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/139694" target="_blank">📅 18:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139693">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
شماتیک ترکیب پرسپولیس مقابل ذوب‌آهن
🗣
اورونوف دلها فیکس شد
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/139693" target="_blank">📅 18:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139692">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skaNmknMTqX0s7_byauyi_-fwp7J-igztvTrOjAg_RmVUghlU0wGjTdsIYjkHV12CYk8d-u0nNOPt1gdQsBORnNV06473SdJymb4DqF4i1l_7YJ3yf4I4uub4xMmO86m5nzQHVtaHd8JUXuuxz-SMgONDb1QfPVL5FTb_W8aKhqYOEqvBaG6lQhx6qR1h48QwRwwNOy6P52rB88UBuym6rM2wXEkfUGJxToZDgznQT74REvj_u-ivL_dAQ5lIM4iwwxQXaeZcGhPiDL2bhEmEgkAT0RMuky294hP_jrGTaAquC4ZMP-bK7ixej571eQAygkag2Ilc9w4RPJd9J1cbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/139692" target="_blank">📅 18:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139691">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/139691" target="_blank">📅 17:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139690">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7939cefa83.mp4?token=cJc_6ZvgsysVZcN_E4kFDXEBjhA0JhoUDpLvvKH70j7VJI0OHT0DqRSYxg182JnOgJ6iWaQYIQY8PHBtdmHNAk6PBtdofvmhXEA00v-oHFQDvGs1tReXEEJLWob1z4fnDhLyzYN2rEMcaQsfTcGjVH6-HHk3lypc-mJQjaDCClJboLHnC-FeUMxywJ76ZK_SXXbOuSWgUzuiq25bjmhtXUIIPlLMAq0KL9pptazMWTca28UPoVeACXWWc-qXl7zzptYUhGDKOFPv9k_Vx_IUMLukNkzapbpinbKxQh-NseY-sUWyO_Jj0sEWDoeypk_Y7fVXQk2ipwTy9AY-toncmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7939cefa83.mp4?token=cJc_6ZvgsysVZcN_E4kFDXEBjhA0JhoUDpLvvKH70j7VJI0OHT0DqRSYxg182JnOgJ6iWaQYIQY8PHBtdmHNAk6PBtdofvmhXEA00v-oHFQDvGs1tReXEEJLWob1z4fnDhLyzYN2rEMcaQsfTcGjVH6-HHk3lypc-mJQjaDCClJboLHnC-FeUMxywJ76ZK_SXXbOuSWgUzuiq25bjmhtXUIIPlLMAq0KL9pptazMWTca28UPoVeACXWWc-qXl7zzptYUhGDKOFPv9k_Vx_IUMLukNkzapbpinbKxQh-NseY-sUWyO_Jj0sEWDoeypk_Y7fVXQk2ipwTy9AY-toncmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📌
هوادار پرسپولیس:
✔️
ورزشگاه آزادی درست بود، بی‌افتخار ترین تیم لیگ (تراکتور) عمرا قهرمان نمی‌شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139690" target="_blank">📅 17:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139689">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8432a81f4.mp4?token=nOeImuthzl2TgPvjTEdCobiuyGyvXj3GSAYUylaMxMpwAUxKMY5AUePIUIYd85qwWdgHCPxyELAcf2AkDRUpho1Hp7xtn8pO5g1Z82dGeLn310pxUUQ7Ych_jKPoANXe-B-Jj_NhyCenn4YVkaqjynm_LPR2lwljy7mMy0nyEhsEPc6YX1T8Von7e38pg9FWpWcBhyjLHNc0Y9-UyuBSrSDjfvzuELbKDX1SVR1FD_i31XohiNZRyPiAOgDS3CFlNIGEO1_Eyb1hjU1vnYTqT0mP5H7bl5Z4NVxwr8Oy8CQ_b43mzXaIrBt1QfrnkZog7e-yH4QC0JgCrt-ZCDKFJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8432a81f4.mp4?token=nOeImuthzl2TgPvjTEdCobiuyGyvXj3GSAYUylaMxMpwAUxKMY5AUePIUIYd85qwWdgHCPxyELAcf2AkDRUpho1Hp7xtn8pO5g1Z82dGeLn310pxUUQ7Ych_jKPoANXe-B-Jj_NhyCenn4YVkaqjynm_LPR2lwljy7mMy0nyEhsEPc6YX1T8Von7e38pg9FWpWcBhyjLHNc0Y9-UyuBSrSDjfvzuELbKDX1SVR1FD_i31XohiNZRyPiAOgDS3CFlNIGEO1_Eyb1hjU1vnYTqT0mP5H7bl5Z4NVxwr8Oy8CQ_b43mzXaIrBt1QfrnkZog7e-yH4QC0JgCrt-ZCDKFJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
بانوان پرسپولیسی و تشویق امید عالیشاه در شهرقدس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/139689" target="_blank">📅 17:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139688">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqs537OZivm0b5kir1nC9eOqrCqM_cqzmEnwj_ZLCxU0Ap0R3v3JmL0iDsdYOxebDglukwmpBbcsvM8ur7shk86B6PYk3lCFOfRPMS5wYLXZn9AqYccQ1b10n4JExfMywYcoC7m8zEbrzIu9p8rtlp7lfW9Dpc9XIEe11ACQ5HbhDKrppUKTzMY1Yo-NU7t-pJsF2RAp4d8PJHtr-FDeRimLhm4WNpQQOOwpou6LDQ10qJnSLtVBheMQ-GaPcepMBAcRVMGAKp3Zj-1wfusxF_a3tszwc6tQxDB47AcqUytrUgdd11FT5AcbbXlzpuP2FiB5tKAklSPeMpczFhDJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
عالیشاه وکیل گرفت
❌
❌
شکایت عالیشاه از خداداد عزیزی به زودی در مراجع قضایی ثبت خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/139688" target="_blank">📅 17:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139687">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMdRVxqnlK3dj7LLr6S_isHF4StneZ7UKii5HtNE09Ptg2W8i7RSeHqklxjvm3gBlemdy-ZTFuhQ81vhJG8X_iw8zwvy2TOCccg28jhQhHSUqcy65gJvHSh9EIBcUFlJq8tMG-9mSfVypdG5dWqa56ahdMc-osn0vOMRoRvnFzJQ1IXxSII_NjVYJ-OaDZsboTKaTSQYWcOpAOnO-ZBovKWZZOyHpPMRRTc6S8AaNUQA9l9EJiK7OxEI4obvLwPH74n89q1rzfMu4lusFRfYb2gbMd4ojD7aJ1l0HuRaPAcK3f9rz87KmUmvMjcgB7mY4USFyr4NyadiyVRefH-1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
هوادارا دم در ورزشگاه شهرقدس
😂
🗣
ورود بدون کارت ملی ممنوع!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/139687" target="_blank">📅 17:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139686">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
گفته میشه که ویسی از که از خداداد عزیزی پخش شده فقط بخشی از فحاشیش به امید عالیشاه بازیکن گل‌گهر بوده و بخش زیادی از فحش ها و صحبت ها پخش نشده و قرار است به دادگاه ارائه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/139686" target="_blank">📅 17:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139685">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
لیست تیم ملی امید اعلام شد.
🔻
اردو برای اعزام به بازی های آسیایی 2026 ناگویا از صبح فردا دوشنبه 16 شهریورماه در هتل المپیک برگزار می شود.
✔️
✔️
اسامی دعوت شدگان به شرح زیر است:
✖️
✖️
محمد خلیفه؛ادیب زارعی؛آرمین عباسی؛محمد امین حزباوی؛مسعود محبی؛دانیال ایری؛یاسین…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139685" target="_blank">📅 16:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139684">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
پرسپولیس با مدارک جدید دوباره پرونده آسانی رو پیگیری کرده و معتقده حضور این بازیکن در استقلال غیرقانونیه. سرخ‌ها میگن مدارک جدیدشون کامل‌تر از شکایت‌های قبلیه و امیدوارن این بار نتیجه پرونده تغییر کنه.
🚨
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139684" target="_blank">📅 16:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139683">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139683" target="_blank">📅 16:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139682">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIVpw7escztH_x5Jf7PiyuK3-DSG664c5ZolG9rweAPmgRhZfiB-DHq1ZrUO92Lrlc7yFD1HjSlfro5PWxQdgCuLeD8BVUO1DmVy5yKUgkB6DLZov5I55OhFObGDsdb81Yx-gMewJaYY4Kiw3Bh1R2Z2LYoKoslxRT64ycwJ0g9BJChMdbohS4J2g1bI8eN0VpXIVXYwTmMkfB6mGgbrAkP6XgHqHktuRnaSxYR3FmWqdlMr4T7OxhEQiDLhOny1oK_MgWTQZKPJZ1SSh_nXqWXapoIDngSxOR4bDFFMsBvIzu63p7chU6f4bU3IrvvSiyF9g6NuRu4-cRIKzcQ9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پرسپولیس مقابل یک حریف سرسخت!
⚽️
ذوب‌آهن آماده برای غافلگیری
سه امتیاز، پاداش یک شب بزرگ
[
پرسپولیس
🔴
🆚
🟢
ذوب‌آهن
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139682" target="_blank">📅 15:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139681">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❤️
🎉
تولدت مبارک پسر متعصب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139681" target="_blank">📅 15:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139680">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⭕️
⭕️
فوووووووری
🚨
امید عالیشاه با حضور در دادسرا از خداداد عزیزی شکایت کرد
🔔
80 ضربه شلاق در انتظار افغانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139680" target="_blank">📅 13:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139679">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jlm3wepIOV_vAe5BFC4crmLltIEmV180hNVTPHwAyElc1Q_iX0EplOIM9Qn9_3WfZoXwQqnV5dXl-qDrASunA3z9eMnMV6QXVvwz4sSWfSeiAnJtFO6LUN1blw95bHKClJytwxjcp4HryDu_EtOlSBvydhtZhbIucq9I5DzAAqJ_V5d4quaOkF486U9M_InY3B_JhmpX7cHsV32SX-GG6nh0PMGg_jFlUGhegh30_pF5RwgJb2j9nZsZahPOgMTGvBimQefq9_yDBtNJVv8VZxQsTjUFf6xHXIHepx0DGatJmltOHtROZY2EHFZoRTpdq4CDl0E8SK-1pzFDtFCs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عضو پنجم هیئت مدیره پرسپولیس مشخص شد.
✔️
به نظر می‌رسد روند انتخاب عضو پنجم هیئت مدیره باشگاه پرسپولیس به مراحل پایانی رسیده و حسین صابری خورگو به عنوان عضو جدید این هیئت معرفی خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139679" target="_blank">📅 13:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139678">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭕️
⭕️
بهاروند: طبق مصوبه هیئت رئیسه فدراسیون فوتبال لیگ نیمه کاره قهرمان ندارد.
🚨
🚨
پرونده جام حذفی فصل قبل بسته شده و درباره برگزار شدن یا نشدن جام حذفی این فصل هم هنوز تصمیم گیری نشده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139678" target="_blank">📅 12:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139677">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
درپی‌اتفاقات‌دیشب؛ به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/139677" target="_blank">📅 10:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139676">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
#فوری؛ بعداز حرفای‌ دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌ سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌ تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌ اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139676" target="_blank">📅 10:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139675">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
طاهرخانی ادعا می‌کنه پنجره نقل انتقالاتی کیسه تا آخر تابستون ۱۴۰۶ بسته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139675" target="_blank">📅 08:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139674">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❤️
صبح روزی که بازی داریم و شش امتیازیه بخیر
❤️
❤️
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/139674" target="_blank">📅 08:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139673">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
می‌خوای پیش‌بینی کنی، ولی نمی‌دونی چطور حسابت رو شارژ کنی؟
وینکوبت کار رو برات ساده کرده!
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
🟣
آدرس سایت وینکوبت:
wincobet.com
🔗
همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژت رو انجام بده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/139673" target="_blank">📅 01:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139672">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/139672" target="_blank">📅 00:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139671">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/139671" target="_blank">📅 00:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139670">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/139670" target="_blank">📅 00:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139669">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/139669" target="_blank">📅 00:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139668">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd7cdc1c0.mp4?token=ovQy8Z40dE7_nbP063qjZWFwoc4pOzmrTOib3N-mFpvVr3wufqQhF6v9YpWyF68WMuXxqf8Uwgsk1FZ1EdqyaM1CX0jyaBuSEYnqlaBV2zCFn1JQiKBWTRfDVX1R6Rw3ASD0LDwjsHr06lNz4mcpklWDaMhBiwlrPjtYqMcaEJDoet_gzt_heuAvYQfN0U2O27hdD2fjYxojmOvpGNK-yJ5nKf-0EPOaeS-QNbhup0EIGLVH3VNsCFRwKV9lhlAC30MweywHtwQ9s3PuZgsoHukXPEH2Y47bm9u7Mn62Y6t1fGGE5Xbe5d6tdJSICzrFz9fU-ep-VW_W7zjpVhNLLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd7cdc1c0.mp4?token=ovQy8Z40dE7_nbP063qjZWFwoc4pOzmrTOib3N-mFpvVr3wufqQhF6v9YpWyF68WMuXxqf8Uwgsk1FZ1EdqyaM1CX0jyaBuSEYnqlaBV2zCFn1JQiKBWTRfDVX1R6Rw3ASD0LDwjsHr06lNz4mcpklWDaMhBiwlrPjtYqMcaEJDoet_gzt_heuAvYQfN0U2O27hdD2fjYxojmOvpGNK-yJ5nKf-0EPOaeS-QNbhup0EIGLVH3VNsCFRwKV9lhlAC30MweywHtwQ9s3PuZgsoHukXPEH2Y47bm9u7Mn62Y6t1fGGE5Xbe5d6tdJSICzrFz9fU-ep-VW_W7zjpVhNLLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چشمی باید اخراج می‌شد
✔️
✔️
حسین عسگری:
خطایی از این واضح‌‌تر و محکم‌‌تر نداریم مصداق خطای شدید و اخراج است
✔️
✔️
تورج حق‌وردی:
با شدت به زانوی حریف ضربه زد مصداق خطای شدید می‌باشد و باید اخراج می‌شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139668" target="_blank">📅 23:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139667">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpZvW-1pDhR2qwQHUxTS_KMgvmRWBfKEosqlle7SZdfhE1ADddRwFX8A0Zm7ozmvuMEbq32Q7z4iXDcny_zRBsBYdFo9hTFgiKmZ__0wFA10kO3R6Rysxx4dlncLrWIhZ5qbgsd2HZenaSEa7u05luf9AYlfgyQ23A41KOkZCtH1z4cKfHGvn6727XrewqBsphMvYgoU4XVf2Xc0BU_upbfUFllRun8e1g3_HE2SOl4GEtMppzADooxpH-GI-qWsnejC5yFQ5HpWZPV_v0TEMYSHZrBZ5_KNgzb-QgaRNd2B8WQzZl88W2lMt7cQO2M-_C2CK2dyhetRk4CtkhHNkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اگه فردا ببریم با ۱۳ امتیاز میریم دوم جدول
❌
❌
فوق العاده مهمه ۳ امتیاز بازی فردا</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139667" target="_blank">📅 23:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139666">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🗣
🗣
فوتبالی: اورونوف فیکسه تو بازی فردا
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/139666" target="_blank">📅 23:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139665">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
تارتار: باید با خداداد عزیزی برخورد شدیدی بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139665" target="_blank">📅 23:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139664">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومانی بدون تغییر ماند؛ افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
✅
✅
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139664" target="_blank">📅 23:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139663">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭕️
⭕️
فوووووووری
🚨
امید عالیشاه با حضور در دادسرا از خداداد عزیزی شکایت کرد
🔔
80 ضربه شلاق در انتظار افغانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139663" target="_blank">📅 23:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139662">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
لیست تیم ملی امید اعلام شد.
🔻
اردو برای اعزام به بازی های آسیایی 2026 ناگویا از صبح فردا دوشنبه 16 شهریورماه در هتل المپیک برگزار می شود.
✔️
✔️
اسامی دعوت شدگان به شرح زیر است:
✖️
✖️
محمد خلیفه؛ادیب زارعی؛آرمین عباسی؛محمد امین حزباوی؛مسعود محبی؛دانیال ایری؛یاسین…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/139662" target="_blank">📅 22:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139661">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/139661" target="_blank">📅 22:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139660">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/139660" target="_blank">📅 22:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139659">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139659" target="_blank">📅 21:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139658">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🗣
محمد عمری و پیام نیازمند به ترتیب کاپیتان سوم و چهارم پرسپولیس شدن/فوتبالی
🤝
🤝
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/139658" target="_blank">📅 21:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139657">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت، در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/139657" target="_blank">📅 21:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139656">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139656" target="_blank">📅 21:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139655">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
نایب‌رئیس مجلس اعلام کرد: سهمیه ۶۰ لیتری بنزین با نرخ ۱۵۰۰ تومان حفظ می‌شود، سهمیه ۳۰۰۰ تومانی از ۷۰ به ۵۰ لیتر و سهمیه ۵۰۰۰ تومانی از ۳۰ به ۱۵ لیتر کاهش خواهد یافت؛ نرخ چهارم بنزین هنوز نهایی نشده است
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139655" target="_blank">📅 21:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139654">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWj38SaWD8jSsvZj8_yJivq73PLhJX2ympmbO4M5QLsix072NArpF5VelT7sNFK0vefGGbRxIZAzteG6oP3-WnH6tdEOF-fmcftyo_Rb7nWbymNuNtA5gJDXcbMyRFRDkT39vTmgZ8Y2IxRasSJCGeChcaaE-gpl84qbrLF4gJSzosNR-FnKNGaHi89vN-yiL7rNUxSxUuIRsrP5EidQRaYTm4hbiG6CZ9dwRj2GuYbvqSj6IojAmq0C6j4J1R6Nc90xqAlozj3QnKyG9-P678ldkoXf-owHcUUTHcUl6hq4eY7L5uNS_VAERGAQ3fSNzyeFckoYkHxL2PWUsBT7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
تصاویری از تمرین امروز تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139654" target="_blank">📅 21:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139653">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIU9iZ66Qb-rXlccA6XZnYJALuvSYfDAQwlFyoVCBvBqe9d0nlukHQ8yCjMVrRHqymgW0zrAnOu-2D1lHBwkaLNmTQq5BhO9GwePhwrHEwfhEdHoF6t-uhHqTWO3SZuPwUkWdDn3XV54bE00SYr8qat3MylFRpKg6cuitGGDWccb1-tN8lfa1gGOLBlVHx_-KGccuQwyuR-eD519hXv-5OJm8GMRjCzED-ryGwATqZaohuX5q1lDIrif541rqAFMmXsXNVF20lw0IXgVbE8ZUWxsWCGY4C_JuL-3KikN-XFMUtb7UyNnsY-6I65AMh86UkxnuwZaVUPZ9Cays7ohRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
جدول لیگ پس از پایان بازی‌های امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139653" target="_blank">📅 21:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139652">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
بازی کیسه هم مساوی تموم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139652" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139651">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🗣
تا دقیقه 70 کیسه و آلمینیوم صفر صفر مساوی هستند ..و بهترین نتیجه برای پرسپولیس همین مساوی هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139651" target="_blank">📅 21:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139650">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🗣
🗣
فوتبالی: اورونوف فیکسه تو بازی فردا
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139650" target="_blank">📅 20:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139649">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
ابوالفضل جلالی در ترکیب فیکس پرسپولیس مقابل ذوب آهن قرار گرفت و تیکدری کار را از روی نیمکت اغاز خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139649" target="_blank">📅 20:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139648">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGUUSuhy-1LTqHm2wwHY8sZL76inJJM8S0XJy0ZFo0TTJiArQ56X8wti9PhGIX-IvxVssmvRXphx3aNqQwIWJUCrJGHvKNGPgaJzb_yFiApCgs8Y_urSrio1F9LI3AHE3Yvp0dTBF8PeYjDsjjgAarys16lwhfRhwE3UrW_JLxLX9sBA9Ea2NIGozBB3J85adDEiTYYRXbYI5s_uXueasLtoV0PETeZd22JQ4iYipKW7rQXkEr3q8eGfTmHdYmwQ30Vm7cAQOUyD9SdJyvaSyXbZkG2YrYeHQ4oRFRSu9-QKVRHayTsZQUicx1V1i6VITECvPbUO0RDeyCHv3KFfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حلقه اتحاد بازیکنا تو تمرین امروز
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139648" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139647">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139647" target="_blank">📅 20:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139646">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
حضور ابوالفضل جلالی در بازی امروز  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139646" target="_blank">📅 20:28 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
