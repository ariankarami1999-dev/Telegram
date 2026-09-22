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
<img src="https://cdn5.telesco.pe/file/Rxp8Jq9QvP9p3SkvCpTHyogW1RcAwetaXZ9QozbjxXtqt2WklehWBWAZD0pXzBgQf38ftqx7Nf8zir0TntWrpp2iFvHyDW7NXhhVvNA0HBB1WJrdkMzSmJ9dDwAPaXDqOq6FSwcGnZxbjYo_wQD_H9099OR10x0oj5eR-Z-mol5l5qeALhCjH7mXw9ItxijRKKPM8pyCYESskuhdSAWglqCn2STWpxJUj4e5A-fBuJAbkSJsScdnUpMDlsDq-HKskEl0cXazeXG_H467uKlISMRKXfRuOWvVUBwcNFoz8IVSFYxwjLqBnVGSJfLNOvpb-vY-P66mry8nZe6Gszneaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 405K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 08:42:09</div>
<hr>

<div class="tg-post" id="msg-107044">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=AqyI9jhV_bwvvhaxmlVfrIYt_SUPLgZrt_jO-EcPQ0KyslMzNoPldr0NR4dxVeTpvvLkN06WIh9IngphUnSsbXOlzGL-jYSAoczZpRrZOLeCI68RsYzovsbT5TFWiKsRmaeK0FOLTLBMoe-dM-2ehsPZrLLAHQFjhHTcGxKLFTkqP3XOdQ6eLmnC7Lw43EJpKflFUDtKejLxFprJp6P17YZ-DHx1jBLYxSUYvmVor9lq09z5JZj-tv2UiZq56lArjwZj4xA9KYzZKHLk0IRtDxNx4dzv1xJ-cGWszABCmXY6ilhdEg-tu7wtnpPtysTgPMySP1tyBx97paMQ-X1znQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=AqyI9jhV_bwvvhaxmlVfrIYt_SUPLgZrt_jO-EcPQ0KyslMzNoPldr0NR4dxVeTpvvLkN06WIh9IngphUnSsbXOlzGL-jYSAoczZpRrZOLeCI68RsYzovsbT5TFWiKsRmaeK0FOLTLBMoe-dM-2ehsPZrLLAHQFjhHTcGxKLFTkqP3XOdQ6eLmnC7Lw43EJpKflFUDtKejLxFprJp6P17YZ-DHx1jBLYxSUYvmVor9lq09z5JZj-tv2UiZq56lArjwZj4xA9KYzZKHLk0IRtDxNx4dzv1xJ-cGWszABCmXY6ilhdEg-tu7wtnpPtysTgPMySP1tyBx97paMQ-X1znQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
شعر خوانی جالب قیاسی:
«مثل رابطه سهراب بختیاری‌زاده و صالح حردانی
مثل حال دروازه‌بان بعد از تک به تک شدن با یاسر آسانی
یا مثل حال اتوبوس تیم ملی بعد از جریان کنعانی»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/107044" target="_blank">📅 08:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107043">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/Futball180TV/107043" target="_blank">📅 01:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107042">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPTJGHGRLoG3dZszpT0lGqNyHwEVeSbrk5Rn8MGwEj_Jp4EnvXyEcV_8I8TOwSq-JtmAMeRJttWKOfOxgdxMqTRI7y4e6Lo2d0CemLJs4Bq9IS5P0o7S-w0aZocvVOi6mnn5v2lwDMAlM7HGhSLk-Iwptl1hSp6F9MIbDfQgibnP5e9fJikS0zoeBafVm2tBfLn6oyAxeACC7DNPk8T6IChE4FuqLe59R9GzjB27BGrGH5Tulgegj3OnTxXZ3xS09x59b2CR250DpJEMzsP_FVG9tNvvJGG1rD3rhPQWCv7vbI-akwArAPhOLRE28v9G80gMq-NfM_tGn9TCee0uHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/Futball180TV/107042" target="_blank">📅 01:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107041">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=Bw8AT4cAuC-na5ivkPkPr9Has40BxGRP2Htp3LDQdgX9LQ1r46yUZfJ92bi1eKap66ayY7a8uWkXj1oFlmdIgslC0yHVFY2_eEnSuHFyqGzTVXs5dHQcy9Bdse54CzZHA6OpiVyJBJyt1g7tejV3CbEO8XtHBUGJrtakkwfBImKO4wMHa_6OFx99zzjgZwmq0_apdB0TPcuV3e1RwNGvJ6vQPMzZ8BF8sOARZGgHiE2I7Zsb8TZMkHrAiyzpVDsEv1dXZdGZ3pvvHPIF37F3uZSwPrGL5qVHV45e6t5P_9j_lnS9VSDL5eutx2_AP1j_i1aio4bBNrLsCdoco4JH_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=Bw8AT4cAuC-na5ivkPkPr9Has40BxGRP2Htp3LDQdgX9LQ1r46yUZfJ92bi1eKap66ayY7a8uWkXj1oFlmdIgslC0yHVFY2_eEnSuHFyqGzTVXs5dHQcy9Bdse54CzZHA6OpiVyJBJyt1g7tejV3CbEO8XtHBUGJrtakkwfBImKO4wMHa_6OFx99zzjgZwmq0_apdB0TPcuV3e1RwNGvJ6vQPMzZ8BF8sOARZGgHiE2I7Zsb8TZMkHrAiyzpVDsEv1dXZdGZ3pvvHPIF37F3uZSwPrGL5qVHV45e6t5P_9j_lnS9VSDL5eutx2_AP1j_i1aio4bBNrLsCdoco4JH_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🐐
🇦🇷
رونمایی‌رسمی لیونل‌مسی از پیراهن ویژه خودش در آخرین بازی ملی با آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/Futball180TV/107041" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107040">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b37185041.mp4?token=n0YyOWsI4y-b1DY8WZTOwAlBDIJnDnFx88APASe8JHWag5fy6FzeJcXKxB8cgbdEevBC5A5Ls0c6oENM9gBSYmSWh_StVHYw80ysajTkyyoFjRMm5qaEohAdNNL6XtFr0gLEDVa_Z79gIBE1uRClb2U3LwF1beI2PhwfESg-1xQd38lXYEjbncqvIIqGKLn18NX1ZOqTPGGOKyR7fdNXm9j6XE7xZkCZPO7TS3C0AHzKkezGyhjTNvkmOFMng-QkkoKn8sz1tKjaxZ5zsJ5pdKoInw6lyE4fxNCavFwwnE44WC1fKxm7WbQU7mbqlido3BeLxT9so3X5hMVs9LTLWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b37185041.mp4?token=n0YyOWsI4y-b1DY8WZTOwAlBDIJnDnFx88APASe8JHWag5fy6FzeJcXKxB8cgbdEevBC5A5Ls0c6oENM9gBSYmSWh_StVHYw80ysajTkyyoFjRMm5qaEohAdNNL6XtFr0gLEDVa_Z79gIBE1uRClb2U3LwF1beI2PhwfESg-1xQd38lXYEjbncqvIIqGKLn18NX1ZOqTPGGOKyR7fdNXm9j6XE7xZkCZPO7TS3C0AHzKkezGyhjTNvkmOFMng-QkkoKn8sz1tKjaxZ5zsJ5pdKoInw6lyE4fxNCavFwwnE44WC1fKxm7WbQU7mbqlido3BeLxT9so3X5hMVs9LTLWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام علیرضا بیرانوند به میثاقی روی آنتن زنده: اگر نظام وظیفه اعلام کند من چه زمانی باید به سربازی بروم به جان 2 تا بچه ام فردا می روم سربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/107040" target="_blank">📅 00:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107038">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNusIgU0QQjhz0w-KSLAJurBa2sWsKvUcMFij9ELBoDHq_F9_3evgjKb7oUUl4FFKPwA78j6HRMH1uxFk1gsRjo9b5ewfV3mSG_MF9bkS6_oerouexChtFotf_Bh000QBOUrfdW_F2XWkshOO04JrN10k4CIeOM33yaEwC6mLxVfCqfDV350zW-UZBlYKlM39hWMhpdHef1bWFyRnRnFRmBwyyumrUx9Q-One7XPl8oFsu0Tvul0Rk0zifHYc31JzHzXS6jXlwHowO7OGPAFR8FwGWpa20gihMjl0AnVMcyOOEaigHqVU0BwkwNPlQCrQpe1iC15_UwqgvD0yuzU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtPraDYdJY3aH1szWVL_ZmXB3psm6WJ2yYT6QmwRtxN54L_isd6H9BarE5oBMpuhSJGb6EwxOmNXP2mqU2pDa1jIzWqFTWIuIUK7Y8wsqN5-1-GFcUckU5uzUyVnFZiBdVXpIfcXjZ3mRibQq32osDnQO2cs8yphlo-pO-ZxSiUAr4nHnhr75nRWmZaSZyT2sxXMcCeGWWOzzBrEukEVLJm9Lh9xoiKZhiJkT1mBntnexYwrXjWpxTfPYU-g7TTlEegDDdHqFOu-MLiYfpmcj4nZ0AJJen-Un_s9s_sz3mz6JX_nOFgkw50xay_mH8GyaHa14GuKT0g5J9vnpu1DmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
❌
دلیل عدم دعوت اللهیار صیادمنش انتشار این استوری در ایام اعتراضات سراسری دی‌ماه ۱۴۰۴ است که باعث شده حداقل تا چند سال قید حضور در تیم‌ملی را بزند مگر اینکه به مانند سردار آزمون دست به پاچه‌خواری بزند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107038" target="_blank">📅 00:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107037">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
⭕️
‼️
اللهیار صیادمنش: در اردوها به بازیکن احترام نمی‌گذاشتند. حرف‌هایی که جوان‌ها نمی‌توانند بزنند را می‌گویم. در این چهار سال ۱۰ بازی دوستانه روی نیمکت بودم، ۲۰ دقیقه هم بازی نکردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107037" target="_blank">📅 00:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107036">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
⭕️
🎙
اللهیار صیادمنش: تا این افراد در تیم‌ملی باشند حتی اگر بخواهند هم دیگر برایشان بازی نمی‌کنم. در اردوهایی که زیر دست این آقا(قلعه‌نویی) دعوت شدم هم چیزی به من اضافه نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107036" target="_blank">📅 00:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107035">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
⭕️
‼️
🎙
گلایه تند اللهیار صیادمنش بابت ربط‌دادن عدم دعوت به تیم ملی، به مسائل اخلاقی: می‌دانستم قلعه‌نویی هیچ اعتقادی به من ندارد چون اصلا هیچ مسابقه‌ای را از لژیونرها نمی‌بیند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107035" target="_blank">📅 00:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107034">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsfNAnx9uRnC0MNPmfqiVLkD5cEhks0mBnKENJ6FpOY9pPUP_Z_yFoTC5H86VNJrGNSRS5swbrgrILudS-dkgM5lQs5BRhHTgvKWDzeh-FsZzNMmMsGa59OMrAqmKOtOKD54jJcKIbVyMeR_1Q__Mn5p3MatGRWQwsleYrjThdIf9juGPy-7wbU-o1iOXxbkKcrvtIAo5JaqTDv7TjM091zpLisZlcklhEHD9CQAoWveBCIjs56ALGcAFbFbGj7SVbkeJ45F06YfljOGPIDrHFWsThAF5G4d9aYqhTU438Xo5-VJtlzqiXjfTo3Tqb5d2DE2f0PC4lH_JyxRQMBiSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
خاویر‌تباس رئیس لالیگا:
🔹
باخت دیروز رئال مقابل اتلتیکو صرفا جنبه فنی داشت. درست است که اخراج یک بازیکن حریف نادیده گرفته شد اما اینها بهانه خوبی برای باختن نیست. امیدواریم رئال‌مادرید واقعیت تیمش را ببیند و دست از جنجال بردارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107034" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107033">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8238d2e025.mp4?token=TUut6RswOxmo624kKraGk2sHmOfPMdFy-NqShg9JEeeVFj20KdrKej98qYqMIcyKQgilu84qlxO606ju8NPD6APFwGp4K0xeXbSVjkDiGfVXESJxEEfrQCUHeY4jHEE6mN3Kl64jRGAGNx2U3a2vpDF7bpWlR1yYH7BRyHWVMxUMZ6213Omsq37RTeTHWDwWronN59g5dfZu_9P-YWKJi3C1DZHdRRujw0gjteO_OKYAXMc_hdhpYZGndmTIj6wHo8NuuQD058fmKw9_Jzp-lyr_VwXdSLC-WRa3ZHYH5YVDCD2X-fEmErDe-_YTzKynV0tMBgo2pOurrgdEuNC4EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8238d2e025.mp4?token=TUut6RswOxmo624kKraGk2sHmOfPMdFy-NqShg9JEeeVFj20KdrKej98qYqMIcyKQgilu84qlxO606ju8NPD6APFwGp4K0xeXbSVjkDiGfVXESJxEEfrQCUHeY4jHEE6mN3Kl64jRGAGNx2U3a2vpDF7bpWlR1yYH7BRyHWVMxUMZ6213Omsq37RTeTHWDwWronN59g5dfZu_9P-YWKJi3C1DZHdRRujw0gjteO_OKYAXMc_hdhpYZGndmTIj6wHo8NuuQD058fmKw9_Jzp-lyr_VwXdSLC-WRa3ZHYH5YVDCD2X-fEmErDe-_YTzKynV0tMBgo2pOurrgdEuNC4EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
میثاقی: اردوی تیم ملی تمام شود سربازی علیرضا بیرانوند تعین تکلیف می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107033" target="_blank">📅 23:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107032">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e4355f95.mp4?token=i25aS632vrVFW-zzOVKdinnczfmfh4kHidpCqKB6n80RHeRLYd1iYOBljauMcvU0hBWOJnOVqMyRAtu8tKfAnlOI4gjOyGIbLDE-aHqEk33iNo1SwpXNRJTmZwizW_ykIoo9pEh1vke6cPjiAyPUamWB3w_kkvJp-TDMmGM6hjsvZDAMKaqZUoZrGOGaxQ1uj-zfWqdRxZ4euT4meHKL7QkOPXm4gohoSSFLZz0ZUsnUCEkyt6oSH5mIUSQZha7rn5eBYJPNoPj3HhvyUH1YD4Ykydt-yBQfAONesRV5_rxGLZHUzZ4MJevJegfeUjOfWywkeZGwrZJY7tn4E-a4UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e4355f95.mp4?token=i25aS632vrVFW-zzOVKdinnczfmfh4kHidpCqKB6n80RHeRLYd1iYOBljauMcvU0hBWOJnOVqMyRAtu8tKfAnlOI4gjOyGIbLDE-aHqEk33iNo1SwpXNRJTmZwizW_ykIoo9pEh1vke6cPjiAyPUamWB3w_kkvJp-TDMmGM6hjsvZDAMKaqZUoZrGOGaxQ1uj-zfWqdRxZ4euT4meHKL7QkOPXm4gohoSSFLZz0ZUsnUCEkyt6oSH5mIUSQZha7rn5eBYJPNoPj3HhvyUH1YD4Ykydt-yBQfAONesRV5_rxGLZHUzZ4MJevJegfeUjOfWywkeZGwrZJY7tn4E-a4UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ابوالفضل جلالی بازیکن پرسپولیس: برای هواداران استقلال احترام قائل هستم. آنها زمانی که در تیمشان بودم به من انرژی دادند. در استقلال بهترین عملکرد را داشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107032" target="_blank">📅 23:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107031">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19a96e43d.mp4?token=B0IZ2SZK9IzT5qhIQ4n37IrtWUd6xaPaXXWxO6UYsjQaWAX2BPVaFiHH1TpxH72jzzrofu39t2PCob1cHwFu42NlWJRdAIPycvsi1_cTor2at763qEHHREf175cQk3P78oQkH9DN0TZHPNrbXkrcwHC4JM4jh7jf5HazKrpUVd4xSST8PfS5wUWvSnZaYxeQRrhdGAY4F1sJga88Nz7cMIoFyUkzjAI8yes1F9bUi63EFIpX9i8DXdUf0cwAudhQnzIjBifNQV9hoJtq-Ivg7_6SGjcfNdPHzRVOzgR6C_atGxQEWxq5mTeBxMNG6S1boZEd0XS-FR7GpzOIDL1-_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19a96e43d.mp4?token=B0IZ2SZK9IzT5qhIQ4n37IrtWUd6xaPaXXWxO6UYsjQaWAX2BPVaFiHH1TpxH72jzzrofu39t2PCob1cHwFu42NlWJRdAIPycvsi1_cTor2at763qEHHREf175cQk3P78oQkH9DN0TZHPNrbXkrcwHC4JM4jh7jf5HazKrpUVd4xSST8PfS5wUWvSnZaYxeQRrhdGAY4F1sJga88Nz7cMIoFyUkzjAI8yes1F9bUi63EFIpX9i8DXdUf0cwAudhQnzIjBifNQV9hoJtq-Ivg7_6SGjcfNdPHzRVOzgR6C_atGxQEWxq5mTeBxMNG6S1boZEd0XS-FR7GpzOIDL1-_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
ابوالفضل جلالی مدافع پرسپولیس: الان طرفدار پرسپولیس هستم، عاشق پرسپولیس هستم و سرباز این تیم هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107031" target="_blank">📅 23:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107030">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fa04dad9.mp4?token=r-xYtudgE9d_yqVsARCiZsbv3ci9VRDqXQtBC7ihXkQ9u5N1-7PSwaYiw8J43grWg6ifyPuLXelzvfmOhKz2yqQRh-NbUJBlR_J4FqJoOh_6FIVsLjKMOJ7WyrDoqQrLXbdV2fSNHpERTA3_ovA3GeZk46xflk0pN5CoOwXnRPClV7jowZfajUO9nljwv5aRWS9w2yzjLBQtYuBsGmpvEMyOFiVkq13GRNZetsMNxA6Qu1JSNT5n9XacjAyqYdLQZ-ZYTHtMcEx9u66Wo0MAwJzYdX6HHJ-sF9ulyxVksaA7VpxjnX46z6q5YfbdPY6GWUQg_aE6NtKnC3Abcd9OKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fa04dad9.mp4?token=r-xYtudgE9d_yqVsARCiZsbv3ci9VRDqXQtBC7ihXkQ9u5N1-7PSwaYiw8J43grWg6ifyPuLXelzvfmOhKz2yqQRh-NbUJBlR_J4FqJoOh_6FIVsLjKMOJ7WyrDoqQrLXbdV2fSNHpERTA3_ovA3GeZk46xflk0pN5CoOwXnRPClV7jowZfajUO9nljwv5aRWS9w2yzjLBQtYuBsGmpvEMyOFiVkq13GRNZetsMNxA6Qu1JSNT5n9XacjAyqYdLQZ-ZYTHtMcEx9u66Wo0MAwJzYdX6HHJ-sF9ulyxVksaA7VpxjnX46z6q5YfbdPY6GWUQg_aE6NtKnC3Abcd9OKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
💙
ابوالفضل جلالی: ساپینتو شاید از قیافه من خوشش نمی آمد که به من بازی نمی داد چون از نظر فنی مورد تایید او بودم/ جالب است رامین رضاییان هم همین مشکل را با ساپینتو داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107030" target="_blank">📅 23:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107029">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11cbab4a72.mp4?token=GHu3zOZtAHDAEjl3ND3QCNHQ0AtcFxYn4ugA26PfkqBmGZw2wn3fSYwttGnwOBCiiFrlhxWfolWMpoFqEIr-tGMBqtkoUXMlsFBJjwZ-thE7VkENvJmHYblNHj9RklolDnptyHxep0_oixUtgTTsoVV_WpqDNzOWP-OVeJOUbq4nDa-kk9rGeMzvDS97M66jXjC4f0RikR502t4n70RtIkZO3r4pQzJJdWJq4Kqzo9REw0dHBD0ZDSlfk94tALt5dvrplqdh0TkqG37qbMYMSnG6GzXBFnkLn99DCvVLhViguiGFWlLsMSqHV7x9Or33Dlo-vhiufsvJgtbOg6Sqow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11cbab4a72.mp4?token=GHu3zOZtAHDAEjl3ND3QCNHQ0AtcFxYn4ugA26PfkqBmGZw2wn3fSYwttGnwOBCiiFrlhxWfolWMpoFqEIr-tGMBqtkoUXMlsFBJjwZ-thE7VkENvJmHYblNHj9RklolDnptyHxep0_oixUtgTTsoVV_WpqDNzOWP-OVeJOUbq4nDa-kk9rGeMzvDS97M66jXjC4f0RikR502t4n70RtIkZO3r4pQzJJdWJq4Kqzo9REw0dHBD0ZDSlfk94tALt5dvrplqdh0TkqG37qbMYMSnG6GzXBFnkLn99DCvVLhViguiGFWlLsMSqHV7x9Or33Dlo-vhiufsvJgtbOg6Sqow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید الهویی مربی تیم ملی: درخواست کرده ایم که از اول دی ماه اردوی آماده سازی تیم ملی جهت حضور در جام ملتهای آسیا را برگزار کنیم
🔴
میثاقی: با این وضعیت بعید می دانم تیم های لیگ برتری بازیکن به تیم ملی بدهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107029" target="_blank">📅 23:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107028">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12081ba765.mp4?token=cSTIQdQBp64SmL12fDgUMuHhQGB3dhUqpTOWj7Glv8U5dFlURNP3Yod9h626NF8dgouW4AIEULLdF6iqrwE_PpMBE9F9FJ9sCsE7EuHJiuvkGYpMDKkW09NjAOuJGtOkXhRVX1KyH7Vm6pZ8YrSxsDNsqeaCPocEJ8XcHd77DP8EV-k5Fh4eXjYuTCAz08MWvaTV1RBCpcuj0fzXASn8s2bcVjYnSbLOH4-B19De_xswWGTQZfQVNYYubqHml8qd12ZUe-uvx4HYUCOq24COmtEiBP_Isl3yKFc4gpdaotyselcBFcAoXtURbicFc647dsxEgn7jL2EelhzDwDTAhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12081ba765.mp4?token=cSTIQdQBp64SmL12fDgUMuHhQGB3dhUqpTOWj7Glv8U5dFlURNP3Yod9h626NF8dgouW4AIEULLdF6iqrwE_PpMBE9F9FJ9sCsE7EuHJiuvkGYpMDKkW09NjAOuJGtOkXhRVX1KyH7Vm6pZ8YrSxsDNsqeaCPocEJ8XcHd77DP8EV-k5Fh4eXjYuTCAz08MWvaTV1RBCpcuj0fzXASn8s2bcVjYnSbLOH4-B19De_xswWGTQZfQVNYYubqHml8qd12ZUe-uvx4HYUCOq24COmtEiBP_Isl3yKFc4gpdaotyselcBFcAoXtURbicFc647dsxEgn7jL2EelhzDwDTAhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
سعید الهویی: پرونده حضور احمد نوراللهی در تیم ملی کلا بسته شده است و این بازیکن خواب و خیال تیم‌ملی با حضور قلعه‌نویی را از سر خود بیرون کند
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107028" target="_blank">📅 23:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107027">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogWULGuuCmMSmqyEf1bQOje9z9kD__pZ-97pWR7jTeGeQ2rjP-Hj6a9MfQfvVxPiE8bbBqciaTjbdlsYrOas2NvHBwzsBYxCLUyAtvS2hXAx82RCYe0npSEQCDrWms2h7nf515a5DKbeiM0MGUhJf1kf2Q8mnumMJTUz476ZdS2QQ063d1rlUhxmOfdmA0aVlTMnqaIiTejwUGRJ-aWlgMDVmYxPdLuObGyixVKFeDulJd5eqhobRGEIUemz1wVbZ0G6Urp1GyVUAc6LSvo_z3PtDoI5C369WxOqJF7wlER5EmJlHviGw9CS7WDdfuexR7x9HYPgK_DcOh83PGhi5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
سعید الهویی: الهیار صیادمنش به دلیل یک سری رفتارهایش به تیم ملی فوتبال ایران دعوت نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107027" target="_blank">📅 23:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107026">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c45095faec.mp4?token=T_M5UO0moSWZA-2k-_2HoKhbgXsUJc1fDB2S8YSXHCvgODP2PZUM4D2Ij-kxhQyBk8NvrEj4OIdz-dZyAL0HAUWjzo4_rvkS2Qn-2SwCmb43QJc9wmS_tfZ-d_BMq94XCsU_d1NjyR4OVEgnC0bdf3OnbEIHlRt2kc3sGfaRLPfwV9sj907DzdM1ZY7J5AvbOojNRAX0S--tcOUb9TEVvAN_95HSXmbgpcAEnJM2Hk9msdkIuOhWqYD4NKUaIJj-vj6YJhNdVl17aJP2GUgAdN8JOowaHUyor40T4Zl1UrglIZPgAfu7cPhB87BBEDPzcHq9KjwQ1bG_Qh8LE3YM6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c45095faec.mp4?token=T_M5UO0moSWZA-2k-_2HoKhbgXsUJc1fDB2S8YSXHCvgODP2PZUM4D2Ij-kxhQyBk8NvrEj4OIdz-dZyAL0HAUWjzo4_rvkS2Qn-2SwCmb43QJc9wmS_tfZ-d_BMq94XCsU_d1NjyR4OVEgnC0bdf3OnbEIHlRt2kc3sGfaRLPfwV9sj907DzdM1ZY7J5AvbOojNRAX0S--tcOUb9TEVvAN_95HSXmbgpcAEnJM2Hk9msdkIuOhWqYD4NKUaIJj-vj6YJhNdVl17aJP2GUgAdN8JOowaHUyor40T4Zl1UrglIZPgAfu7cPhB87BBEDPzcHq9KjwQ1bG_Qh8LE3YM6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سعید الهویی: الهیار صیادمنش به دلیل یک سری رفتارهایش به تیم ملی فوتبال ایران دعوت نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107026" target="_blank">📅 22:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107025">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
🙂
🎙
به مالکوم گفتم Bro, Easy Football!
کلماتی که از درگیری شدید علیرضا علیزاده با بازیکن سابق بارسا جلوگیری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107025" target="_blank">📅 22:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107024">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
‼️
انتقاد تند عادل فردوسی‌پور: پدرمون در اومد این‌قدر با ازبکستان بازی کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107024" target="_blank">📅 22:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107023">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee3019bfd.mp4?token=qtog0vlaxWBGycKsw6x7n7DPKORP-X0CiiWllL3EyV9yl2Ryoz9FY_qrEy6UN2jbFatZefJZn5XvvTZeGjHiHDxQTnFZ5TVU5AUa0BPhwPXN-9mBAlorNMF7ecQMRkh12aBum06LXbsuPPGu3PtCjRztSLhDAv8cBTjgzmAogJCDhQCVpAkEQyO2wu1s5BOBCQmrmVsTgLQ0DRgfEF2zkHBhdoN8ygUcIOy2z0nZPsJyB487Nja8-2cLVD6gUwWCUv3N0VTrIfwvN90Vp9R_UAi7mWpdEnjha2Jpd4IQ_2KZWdOMHU45TUpqWim9uITjnFGAl_hcMzZWc5xGHcghOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee3019bfd.mp4?token=qtog0vlaxWBGycKsw6x7n7DPKORP-X0CiiWllL3EyV9yl2Ryoz9FY_qrEy6UN2jbFatZefJZn5XvvTZeGjHiHDxQTnFZ5TVU5AUa0BPhwPXN-9mBAlorNMF7ecQMRkh12aBum06LXbsuPPGu3PtCjRztSLhDAv8cBTjgzmAogJCDhQCVpAkEQyO2wu1s5BOBCQmrmVsTgLQ0DRgfEF2zkHBhdoN8ygUcIOy2z0nZPsJyB487Nja8-2cLVD6gUwWCUv3N0VTrIfwvN90Vp9R_UAi7mWpdEnjha2Jpd4IQ_2KZWdOMHU45TUpqWim9uITjnFGAl_hcMzZWc5xGHcghOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ادامه شاهکارهای داورای لالیگا این صحنه رو هم دیروز داور بازی دپورتیوو و بتیس کارت قرمز تشخیص نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107023" target="_blank">📅 21:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107022">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107022" target="_blank">📅 20:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107021">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0JcNqL3JyxoBpwlbyMpawDxC80Y0-rl-VVqbbpqGEFkmnF09tRCYdpWgjEuCqDOgqPnceKUrAm-ro3-cVha3jHOBHjmTrYiulh-t7Z1p3C9l80WqusDnzmRW8G8QQAzis-BeD_7Qt1rJpcUuoXsTD9GZMhpJsGDnWHm85AaelN8-4bL_Z3CQiWjQ-TfUOiaemtQ2UHBR65jBsR4LxRbVVfwWubq4O3YpQ2S4WFrQCTxxSk6kAK-UBvXA4tdC00dxWVve5dMdMNkoTgrkSaV8Yfvi7Q35-Vu_taICaTTvE92ACegiurReyz-SN_4VFA_PmT5K1bP1jd5M6U95_WO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
مقایسه آمار نیمار و رافینیا در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107021" target="_blank">📅 20:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107020">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=O45DNC4cTf3HxyTxydjtpXOdsjr8YRzm1juGjlUH8uUqtaD9bXuxgbh1g9V30qjfZrqbHUh8WVZ1om1Ze4s-AvxT4k2NHh1vc9OPJ60eQrnbAmF3ItVLi2iaQgixCdwIeQk5FbNS-nUgkIRVMx8vQwDI_fzNqSu1b4tnsSUc8zGb1kAUf3aGSOqY3bLMFDvMGmoOY7hjJIPyotgxgfOmdWQnClnYYGRlkSnfuuCe46C3yRBAyX4sBujmj158yvWFslKRJccfHiL12WSUm2wudJDkwH0ovb-wZjRylnaJIkYhZMXWqliMQSlxh30igI--errkKbbYaznp2gIlwLc14Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=O45DNC4cTf3HxyTxydjtpXOdsjr8YRzm1juGjlUH8uUqtaD9bXuxgbh1g9V30qjfZrqbHUh8WVZ1om1Ze4s-AvxT4k2NHh1vc9OPJ60eQrnbAmF3ItVLi2iaQgixCdwIeQk5FbNS-nUgkIRVMx8vQwDI_fzNqSu1b4tnsSUc8zGb1kAUf3aGSOqY3bLMFDvMGmoOY7hjJIPyotgxgfOmdWQnClnYYGRlkSnfuuCe46C3yRBAyX4sBujmj158yvWFslKRJccfHiL12WSUm2wudJDkwH0ovb-wZjRylnaJIkYhZMXWqliMQSlxh30igI--errkKbbYaznp2gIlwLc14Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
واکنش اتلتیکو مادرید به عکس‌های پرینت شده مورینیو در کنفرانس خبری
: «همین حالا به آزار و اذیت داوران پایان دهید!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107020" target="_blank">📅 20:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107019">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=h6zM61MPML26WvrC2lWEsDwny3X1sh6G8VJOw51MKov18SH9KonbFtXWD3R3uLHTmINXTHmE84_Pag8r_DT12LA4LPwOdnWs4Tlv6ioX-_N2DHfPx3LXKwEwwynqYGKP45kgVqP9xbeCz29e5nk2EHSCP1jFxB5YRcFIv3kCFSmNhq7EorYFPsDVCXYAEflpYqT2iIgzulnQF-XqtcwTn028aQgltMOhiSkjJ6iVGuYNK9HQHjwzQqBHoYfsrXzQkefLMJuq2kxIWETBsyHqlMLhAuGq3RBjs3-ggNGPyNp6BEea4rFxyR87nV2ZPf0gowbWsm2cRJ_HYSZmTE9Gbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=h6zM61MPML26WvrC2lWEsDwny3X1sh6G8VJOw51MKov18SH9KonbFtXWD3R3uLHTmINXTHmE84_Pag8r_DT12LA4LPwOdnWs4Tlv6ioX-_N2DHfPx3LXKwEwwynqYGKP45kgVqP9xbeCz29e5nk2EHSCP1jFxB5YRcFIv3kCFSmNhq7EorYFPsDVCXYAEflpYqT2iIgzulnQF-XqtcwTn028aQgltMOhiSkjJ6iVGuYNK9HQHjwzQqBHoYfsrXzQkefLMJuq2kxIWETBsyHqlMLhAuGq3RBjs3-ggNGPyNp6BEea4rFxyR87nV2ZPf0gowbWsm2cRJ_HYSZmTE9Gbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت رختکن تیم‌فوتبال رئال‌مادرید بعد از شکست دیشب جلو اتلتیکو!
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107019" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107018">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=S_40_nspWMeE1smUbxPf7oFElhnrsGvK_0VEFn_h6wnrLbkWLBjBRHdR3Itm7g9OQjsn-jP81ZOIDGAL1b4Uhf3PQbCiDSma4qzOkv_m7nslXr0HDUM2YUSorDI0zwzeH_YyTMJh6yFAcFvkASmq1GcO3piKdk-cVTD3KFazCBfiMSQt3LwaUL3bOchyMx3EDg1DqX0BKfEj2O_gBlmRw-RHHgoSgLjMop2wFhEMZ5VYCqo8a6l_x6H2JtfRS853k9Kpq6X0DyCIIRH3xhm-fKSjrErLfLzLY8oCvlDXof0VTVoBbhdlBZPDZc9V0mGAMvmFFki__h27JV-9hUu_RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=S_40_nspWMeE1smUbxPf7oFElhnrsGvK_0VEFn_h6wnrLbkWLBjBRHdR3Itm7g9OQjsn-jP81ZOIDGAL1b4Uhf3PQbCiDSma4qzOkv_m7nslXr0HDUM2YUSorDI0zwzeH_YyTMJh6yFAcFvkASmq1GcO3piKdk-cVTD3KFazCBfiMSQt3LwaUL3bOchyMx3EDg1DqX0BKfEj2O_gBlmRw-RHHgoSgLjMop2wFhEMZ5VYCqo8a6l_x6H2JtfRS853k9Kpq6X0DyCIIRH3xhm-fKSjrErLfLzLY8oCvlDXof0VTVoBbhdlBZPDZc9V0mGAMvmFFki__h27JV-9hUu_RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «ک…، خفه‌شو» دهنشو بست و این شاهکار رو خلق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107018" target="_blank">📅 19:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107017">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=V8gxZRj7Rwy3d52TTYeg6-dDd2G7kU6JKlkptp-A3Y6jGNRRdU8eGOzO-CvNOPPKwBBc1knS1jAC9C9iiAVpmjIGtpYqTU5vd5gD3TmJNkwjpXkQpcoWO9Rbv4S9cXcsWzlRF3B1PINse673EJELBEfvAhNiq-Ehxs2wV0yt4Mqtu_2V5ZlI-K232TI9PrvIGMVIrfaIMn5PesneGUloFdkwASNsRz5_uffYBUpnigZY6YSn16JkQBv2iY0a8dCKs-jvo7XAeaWQlkRt0Gjpk0gk0gY6C2IUDNqAnKA__p0NmCGKDrP1I9HUv8JhANz9iz9znpLqtxmo6-TQfaBcMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=V8gxZRj7Rwy3d52TTYeg6-dDd2G7kU6JKlkptp-A3Y6jGNRRdU8eGOzO-CvNOPPKwBBc1knS1jAC9C9iiAVpmjIGtpYqTU5vd5gD3TmJNkwjpXkQpcoWO9Rbv4S9cXcsWzlRF3B1PINse673EJELBEfvAhNiq-Ehxs2wV0yt4Mqtu_2V5ZlI-K232TI9PrvIGMVIrfaIMn5PesneGUloFdkwASNsRz5_uffYBUpnigZY6YSn16JkQBv2iY0a8dCKs-jvo7XAeaWQlkRt0Gjpk0gk0gY6C2IUDNqAnKA__p0NmCGKDrP1I9HUv8JhANz9iz9znpLqtxmo6-TQfaBcMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت هاشم‌بیک‌زاده از استخدام مربی خصوصی رونالدو برای رساندن مدافع تیم‌ملی به جام‌جهانی ۲۰۱۴ برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107017" target="_blank">📅 18:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107016">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=YuWjvaYbIwaNlqFQySwG1TG2S5Um1zYfw5W1Y2Z3pssrb0pHizkkQbmpBMy0pRs23i-nB3FMNrR7Q7MuRwSubkqQktYWJH86XzPvSY-gDqBRRCW7wYXy8iXgqJZ_PUNXxB3z4RjsEv03q0Crazb7Z1IJOUbPNjZr52cxrilWq1vMriobJ-uoXb4wi8djxBXDJEM5LwMcPzvC3757eFEKnM_PFxgYWF-N7VppdfJkdP8s9bu0F70rjJ1IoWokHOboFD37pagPgV857Mxm8yW0v3O3a_IrwHMDoWR6Oa_xvrnxwadGpHydM36s6QjTLyAn_MBcrbqaETqx1xfCR--UhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=YuWjvaYbIwaNlqFQySwG1TG2S5Um1zYfw5W1Y2Z3pssrb0pHizkkQbmpBMy0pRs23i-nB3FMNrR7Q7MuRwSubkqQktYWJH86XzPvSY-gDqBRRCW7wYXy8iXgqJZ_PUNXxB3z4RjsEv03q0Crazb7Z1IJOUbPNjZr52cxrilWq1vMriobJ-uoXb4wi8djxBXDJEM5LwMcPzvC3757eFEKnM_PFxgYWF-N7VppdfJkdP8s9bu0F70rjJ1IoWokHOboFD37pagPgV857Mxm8yW0v3O3a_IrwHMDoWR6Oa_xvrnxwadGpHydM36s6QjTLyAn_MBcrbqaETqx1xfCR--UhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرحسین قیاسی: مهران مدیری برای حضور در برنامه من اصلا هیچ پول نگرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107016" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107015">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107015" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107015" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107014">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzumOeOGnsqUXvWQsNg3V7rKUCpkj2NipPSfOvMsQnPoPZTJezI-uKUM2PmMcrMtZCJFrhmH7y-zFaF7nu2e4OxijYrU5C_JnMx_xzItuCPuQsv47PF41waVrkIVWK0HazEuNsi9KSQhL6WfD0-tgQhCIfZEpQ9_7jBZZYM2E_s4uBgQPPpoNNeyHtJP617qxRzFlwKVJqRTPnxk89mHCg7KQPYmBwZcM-dUJ7K6RCuNRcyLNfJ-dBZRfI6b0nFyVr4RpggV8JHZG6fBM6Ux52504BBHt_teMXGVGB_PLtsrsmr38_HqKD9iaae1ZYlhhNiABviR46yiY-A92zvhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107014" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107013">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=UKiEIaG9xMgNX5whfylBV6NMleeJx9Gr1lcWBymVTW-j4BYIIGBe0tFzbebxTB-uz3-GBG_igmIczJaRIyi9Nwwtlq65ShXE70FAkl72QHi5FhxbxTLOWKUV68LX883rmN6f4QI3RLpF0AP_A3bwCSAAQNEbsZAtUizZQVab1Cj2zR4erEJRLz0hcQtP3_Racc7o3-2dmh2Ng9xdzXlQKXII-tivOBHFZwD4QGfohVt15yxXR6pAuOYbXiVzc4oRRupPZir35HXJf7xFIwXZH-TOSy4HQ4jLXauN-_-19V5WrAM7inGhuc9qfWbP8RLpp_WWwG75MlBz3VQ5ox37_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=UKiEIaG9xMgNX5whfylBV6NMleeJx9Gr1lcWBymVTW-j4BYIIGBe0tFzbebxTB-uz3-GBG_igmIczJaRIyi9Nwwtlq65ShXE70FAkl72QHi5FhxbxTLOWKUV68LX883rmN6f4QI3RLpF0AP_A3bwCSAAQNEbsZAtUizZQVab1Cj2zR4erEJRLz0hcQtP3_Racc7o3-2dmh2Ng9xdzXlQKXII-tivOBHFZwD4QGfohVt15yxXR6pAuOYbXiVzc4oRRupPZir35HXJf7xFIwXZH-TOSy4HQ4jLXauN-_-19V5WrAM7inGhuc9qfWbP8RLpp_WWwG75MlBz3VQ5ox37_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
بهترین گل‌ دوران فرشید اسماعیلی کدام است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107013" target="_blank">📅 17:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107012">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfpnvsRhOzefhvmqckA9tJLjg5hj4BCJLXhagx08gaNJZiEICf2E0Q6eHmWhIUA0LjJnkoQj0wjZ_OTfC4edYYsdHC1-NZI_gPwb8C-Di5AtZBc48QCo0LqJMH7Uv4WkodwFqYiGl-5OYNKvQhnR39Bb4GMaVsFK7LYKPfi-bLMXC4B7icL5DW7UbKdjoL-dE9XW4zTnLanBTnHTVuQwZBt1ZyNyYHLIQw-fCXS88cYkbQYnvENvQagPDWvOZcoyCpWAZd5cZf6ZUEH1MtdS304eBL3L7DuN7_g9qp8HGqEjadfIvRNmlMcsN7Bx3-gzOpywt5E31dwsjDwtW3i_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سه سرمربی آخر منچسترسیتی همشون پنج بازی اولشون تو PL رو بردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107012" target="_blank">📅 17:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107011">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226cc241a7.mp4?token=KrON_hufmzRlY-s_Z-yO50QgMKHa49yDr5OxX5lyadpDQuJav_1OBB-uRjvoKmHoO3bMbnnS8ZTPgDqeyB1d5Sr07TzYfrjC1WCfYSCi139bYdmOLysCwN6VGxdrfPVwsTnF9wIN260-rHRv_xm_Ewr4jGOfecyEbppC6mQkAhXhZt9X4XP4RSyhPjNrHe68-Ve0mRRdFDovi8NH5fzdgbvu5d6RyW4a4DYzwvgeYKE95hVhMezsCR3yo_I2anqSp4ll_0GB22mPCSachyDKAp6mdvIPGXukz7busx6Ta2_Ck4-l_qUTaH1zeh7SScjVRQys7MTg2e-KS7qdWvnb4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226cc241a7.mp4?token=KrON_hufmzRlY-s_Z-yO50QgMKHa49yDr5OxX5lyadpDQuJav_1OBB-uRjvoKmHoO3bMbnnS8ZTPgDqeyB1d5Sr07TzYfrjC1WCfYSCi139bYdmOLysCwN6VGxdrfPVwsTnF9wIN260-rHRv_xm_Ewr4jGOfecyEbppC6mQkAhXhZt9X4XP4RSyhPjNrHe68-Ve0mRRdFDovi8NH5fzdgbvu5d6RyW4a4DYzwvgeYKE95hVhMezsCR3yo_I2anqSp4ll_0GB22mPCSachyDKAp6mdvIPGXukz7busx6Ta2_Ck4-l_qUTaH1zeh7SScjVRQys7MTg2e-KS7qdWvnb4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند شروع جذاب و یک خداحافظی تلخ. این فیفا دی رو از دست ندین.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107011" target="_blank">📅 16:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107010">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
⭕️
⭕️
⭕️
🇺🇸
وزیر خزانه‌داری آمریکا: تمام شرکت‌های هواپیمایی ایرانی از ۲۳ سپتامبر فعالیت خود را در سراسر جهان متوقف خواهند کرد و از پرواز به تمامی مقاصد بین‌المللی منع خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107010" target="_blank">📅 16:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107009">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTLwL6DGFMxgbDkKTvIJ8DW6mQk9yBpqXGqJnSLe8LJEsrctmTolgtGpkrT4GUafVrivj3gcte5ePWebcM7hSJ45MF3v7UPTAjD3J3PRbDcIrStEW_yzS0LEHLmcs7YEjE2i36l2NUadAWBpcOZQkKkBC9cPQzqpu_e9qQzQdbq8oTL8jfJ9qZs0NmIrvkLYzp8YU-vvRZFnyMiBGj1_sEzQfGVjl3tTZXblhylN3c8A5C2IH-kzAMSySMtfo7YujDFq2Kt_8-hkQotVaW_eLYuQVb-UKfztpUwCoaYWBbA01TB-pxScqWQXXfBRC2O-FcSWf8J8VJZsQR3JBVPa2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
آمار درخشان اللهیار صیادمنش در لخ‌پوزنان لهستان که نتیجه آن عدم دعوت به تیم‌ملی بود:
🔴
۱۵ بازی؛ ۷ گل؛ ۲ پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107009" target="_blank">📅 16:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107008">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d7084572.mp4?token=OreVuD1S8lehy7FzfsQj1pf2wHr8YHS_V9OGcHhBhYsz0iQ5RVbI1OL8_RWR17DUSFjCZ_qLHkFrcWrwBO0mSPptQVY81V3VTZVN8t9k8FWzOl4QP_X20l9aCaxjMVKTd268qxa0h3NdqoUhHu9qsYDDR5Kj-Jz5xC2KYjsUOxafHEX8Lnp4IFMYUls__z_Uj3tJe3X9VTZD47ZdvcJ4Ju6mNWTKuWeE2dVghwYkIlFAyQ0p18XOoHU0Q6KYI-r5OwmC9fXjRii-xOv56m9IKAVyOoJAfZUHgLPQOzjeGkxyNAvPaejxadzJ29oR3JeUfOvbM7p48Uh5PkN3jb0ung" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d7084572.mp4?token=OreVuD1S8lehy7FzfsQj1pf2wHr8YHS_V9OGcHhBhYsz0iQ5RVbI1OL8_RWR17DUSFjCZ_qLHkFrcWrwBO0mSPptQVY81V3VTZVN8t9k8FWzOl4QP_X20l9aCaxjMVKTd268qxa0h3NdqoUhHu9qsYDDR5Kj-Jz5xC2KYjsUOxafHEX8Lnp4IFMYUls__z_Uj3tJe3X9VTZD47ZdvcJ4Ju6mNWTKuWeE2dVghwYkIlFAyQ0p18XOoHU0Q6KYI-r5OwmC9fXjRii-xOv56m9IKAVyOoJAfZUHgLPQOzjeGkxyNAvPaejxadzJ29oR3JeUfOvbM7p48Uh5PkN3jb0ung" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
افشاگری یاشار سلطانی خبرنگار: روح‌الله رضوی کشمیری، مجری جنجالی شبکه خبر ۱۷ میلیارد نفت از ایران فروخته!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107008" target="_blank">📅 16:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107007">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBo25NXVEm1ybXZF6cYwtJCl8Rp0S0f6LyEHHm2WRnDTKfxZpRA-O0cpWa_3hZtBAuEUP_s5fWFQti5ryIXKCwrKV58_lt6iomf44PGGHnqUzwL8534sJISZyyGG8Srl9fNcB9917EikUfxcO0PEKNjxXdOSX-9qQ1wUY4GD5idhDSkPvcBcZdIttizf5njZGxp5Yrv86-2i8b2qOUXAdq_7EEgMZJLF0uuXPf96wc9Jl3jVhSW6R_0Uw9GaxKmk-NHeHYLCIYbTF-2xCTnJfpaOPueCCkQTtfy3Vkm08j3sJGBuBOhUs0r7psBGJkr3v2UMqQSPYAJKfh5KW_0zXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
دیدار دو اسطوره محبوب و مردمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107007" target="_blank">📅 16:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107006">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e35b261cd.mp4?token=jwZNttxMLv73dRJBUeaKrG_z9eik14TqgW_Xmvr3gPa55DcL-nmUcA7EGSU0481qliM2MMjDiy8YksbQ9HTXsXcbJ4jk25aSfupGJ4mNT2X1mZKBiiQxqQX_VZEMLMxhXbH6XO4_3KBxaEWjm7C66Mt0mosXARpETvFIaAWQ7UNxINPF1xbb27n7Ck6t785u_ntJjtsr1f-u2ejf6bOLRs3EerPQX_MLbuIyHLX1aGg_3OVDlFFi8K7VivTf0oF_Y8hLVBgll_AYs8J-touiHYHXRAiS4nBHA02rfR5JsYtV8nCTpMcUiurDUxudmV7u2EtN57c1WlzVDxbmBR7OZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e35b261cd.mp4?token=jwZNttxMLv73dRJBUeaKrG_z9eik14TqgW_Xmvr3gPa55DcL-nmUcA7EGSU0481qliM2MMjDiy8YksbQ9HTXsXcbJ4jk25aSfupGJ4mNT2X1mZKBiiQxqQX_VZEMLMxhXbH6XO4_3KBxaEWjm7C66Mt0mosXARpETvFIaAWQ7UNxINPF1xbb27n7Ck6t785u_ntJjtsr1f-u2ejf6bOLRs3EerPQX_MLbuIyHLX1aGg_3OVDlFFi8K7VivTf0oF_Y8hLVBgll_AYs8J-touiHYHXRAiS4nBHA02rfR5JsYtV8nCTpMcUiurDUxudmV7u2EtN57c1WlzVDxbmBR7OZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مانوئل نویر در بازی بایرن جلو یونیون که انگار خودش رو دروازه‌بان نمیدونه
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107006" target="_blank">📅 15:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107005">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4379faf506.mp4?token=hLtdsdY2bQBMrOC5XSejD0mS33_M_zZjjnG_rIM-2FeMa9earK_R70x63qQiJY03sSs-IEb-6f_zYTbf2mOuWGTdBMemu7P6yEhvP-NxhU-_ffLPSmbhXX49qymNcTGPFgxSg96_21zgJ48EnHpoNJ_CtfCMtbu5j7jMjV3dij7X50X7wk8U11R98ww-CWMQqZQaiQw6B7HNPXmzz1naNMDi4APwSZiF-7ynC9QRYk3VbTji1SCWhlCO25W79pLzCGhELBbYEaR7-fMCivCYfx1skr2Fw02iQhVHMZ8NaXX40M_rTsXvV3NrSj0TtmWo5k9sepHmcAx9gCYQu6nZ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4379faf506.mp4?token=hLtdsdY2bQBMrOC5XSejD0mS33_M_zZjjnG_rIM-2FeMa9earK_R70x63qQiJY03sSs-IEb-6f_zYTbf2mOuWGTdBMemu7P6yEhvP-NxhU-_ffLPSmbhXX49qymNcTGPFgxSg96_21zgJ48EnHpoNJ_CtfCMtbu5j7jMjV3dij7X50X7wk8U11R98ww-CWMQqZQaiQw6B7HNPXmzz1naNMDi4APwSZiF-7ynC9QRYk3VbTji1SCWhlCO25W79pLzCGhELBbYEaR7-fMCivCYfx1skr2Fw02iQhVHMZ8NaXX40M_rTsXvV3NrSj0TtmWo5k9sepHmcAx9gCYQu6nZ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تمسخر امید عالیشاه توسط مجری صداوسیما پس از فحاشی زشت خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107005" target="_blank">📅 15:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107004">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxbgHsiuAOqCBjUkWec-nMkxIhSRAxH_R_fn6AHWirJD-fPAPsLeld__Ja4ti3-2eoYiE7j56JcoFShcY3HfWwk__ed0a7yxmxKpFHGwxKDoyuyrcaPE8IFrvL1rjI6h912VBbaVsjUst_p8olsUrvGFzQLMvk2qotdJjGcwEhSbv4E7TAGNeTEzoCQ0R62X3HhTu1Pst0OPVu5fHsYqoSf5EnhJHzbwW39C1wVoReZwVA-JLkkNmdwu0y575FKijvWpDrS3fZKJsFFQDryJQdYSSmLiPbF01wv_8kBie84XEfkFnE_7SoqGZIV9I-jgsrrYsFxZdXlFulwxq0TqIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107004" target="_blank">📅 14:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107003">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBJ8fP96VsY-JupBNKMAEiDfFZ_B477T6B84z6k1x0vqirSCpAvynT5PMXixPGSjCjBigChpJtN1JmKuWmcBsqpNgF7bymwA57P35U10Q1ce6nvhJ3dwAc-rFmFMmwx6OlMf8wZz2FMyIekNxCx432pcrvACeu2vxWxVVlfnskUArGjYW3aAE4hEyaNGInxx9usaoQQpk2F3za6RULnv58a2acpYNHL0fSUip84SkNxkfOISTygT3M3pyJ9iwWz40TIa1iTqTfULGB_Bxd2zRXNcRjDHHL9mxPd4CV_kSFYoP7jpqJjQlGD0HLZd71Cr4aL5dQanzb2lLGQ_OMM7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد تیم‌ملی اسپانیا با دلافوئنته تا سال ۲۰۳۲ میلادی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107003" target="_blank">📅 14:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107002">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=Iw0LMjvC3jA4RJN6xd37YEcjW5fEO9qUlODOeOT2uh0-xeRF4PtRlhTnfXTP0s3mBGPRbgvX2mkchcFvksViKJ58BZ3mqhUnXGqyos7PblCm5FQrIo7aSMBkh4RcQVL21CkwN7QT6KNniMIAfYZsvvrOKnnNLqGHC9gWKQlxzT2OrCqcyFoj7Xq7oG73BBFmpD_3w2jcHKoRyN_fAcOhDtyFpMk_WNuP22BaT6w6jAD_AfYFG4b6v_6_ZuqbuHJgbWc6U6T3pg66cYNoqMRgyclAL7rXROG1MXDcqGz5PIwpz8Dg4gfXPjByr24nQrSztDaAYDkHqwbKc5xR3TISKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=Iw0LMjvC3jA4RJN6xd37YEcjW5fEO9qUlODOeOT2uh0-xeRF4PtRlhTnfXTP0s3mBGPRbgvX2mkchcFvksViKJ58BZ3mqhUnXGqyos7PblCm5FQrIo7aSMBkh4RcQVL21CkwN7QT6KNniMIAfYZsvvrOKnnNLqGHC9gWKQlxzT2OrCqcyFoj7Xq7oG73BBFmpD_3w2jcHKoRyN_fAcOhDtyFpMk_WNuP22BaT6w6jAD_AfYFG4b6v_6_ZuqbuHJgbWc6U6T3pg66cYNoqMRgyclAL7rXROG1MXDcqGz5PIwpz8Dg4gfXPjByr24nQrSztDaAYDkHqwbKc5xR3TISKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
🇪🇸
بازیکنان رئال‌مادرید و زیدی‌هاشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107002" target="_blank">📅 14:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107001">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH1oGu_fQOVg9jEyg3G5JCgJA076OxqakPr6Ogm504Au5QisNegppNzG23kNbTinAyf2bRgT98-sr1nbG7FvOs8LZVFISdPKgY_DlZ5yCRsLwI34RTTLpRIa5iIiVaZFp3nlje7ruKKddE19zgFx9EQz8Fbt7XG6ws30tKyO99sk6YCIH70Qg6U-SxvmDA5lUTmNGJBDmQ5hZd3zwYWybREIF7dnHbJnmuYc5yVlNYmbRSnYInlJAUF3pAAmOIuZZUYZ5Zhm6L73z_d-b6_339tzcTrAZFya5cOE5ejmhi4zQhxutRGo653NADICcC86gC_q1kk7gnoSRStWhyOaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین تعداد گل رافینیا، مسی و کریستیانو پس از گذشت ۷ هفته نخست لیگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107001" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107000">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7xn5MIsg5xrIPljYykE1Buxx0THJORm7V092mqEsSZRxiB5Jy1SMz3ltlNbmSWnpVuGitvpqg-eayacJ7WAHhGwB7Ds3dXtfdvV1x2UvOdM3exU7yTBGA0GhkYyXtWmjS_r51BgRKhBL0lHDcSpaSpbiZ-i1-09GeDcHPuqJsW7yInC1gL-6ECWOhfBdu6dgp57IH1fqTIM_ED0uHjaN88WER6-2ia0ef6sT6RswIHdPd3UzcMTJQyonIpRAQIL6gW-YIgFUTQ0kSmYtABUfMkuJfCG33YG8aqnapuE5LuBRX8-fZxx6_ml2q1uTsg2qI8XkSWwcENaREFDfLB7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107000" target="_blank">📅 13:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106999">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=mrTBX2PJOegaBx4-Ssql8Ul4usmfyMcr79iww_6KWzDVkHFej0DG5ewyQbPDmAASUkxjCPEsyiV7JfhhQHrMwOjlhzMJg7bZoZKuYtFRYBvoKjBvwXbWrYARgmJ6-YxzcjERGqw49EYpoYNAVK6N5sZbkfsAu7V-Zt3U-7bSKQ4rbuzteYq9feilDFiAnpSFJmu1WSuR229vLe-L4gtMMV7dsUEBkzDfMiDl5n8QrxXvFEKxGtqHRacP5eQA_3NSePfGbmyrXauku_8GnX1Of9-jQil132C2Ih0WIeu5DK_2v95DIHDjg6uef3V9SsnhB4LIVl_FNwwjCmQBXHZqdIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=mrTBX2PJOegaBx4-Ssql8Ul4usmfyMcr79iww_6KWzDVkHFej0DG5ewyQbPDmAASUkxjCPEsyiV7JfhhQHrMwOjlhzMJg7bZoZKuYtFRYBvoKjBvwXbWrYARgmJ6-YxzcjERGqw49EYpoYNAVK6N5sZbkfsAu7V-Zt3U-7bSKQ4rbuzteYq9feilDFiAnpSFJmu1WSuR229vLe-L4gtMMV7dsUEBkzDfMiDl5n8QrxXvFEKxGtqHRacP5eQA_3NSePfGbmyrXauku_8GnX1Of9-jQil132C2Ih0WIeu5DK_2v95DIHDjg6uef3V9SsnhB4LIVl_FNwwjCmQBXHZqdIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
اولین گزارش سعید زلفی در پلتفرم اینترنتی پس از جدایی از صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106999" target="_blank">📅 13:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106998">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXaqbuidWjrBmfcRe7DKwsTgJCrfLeYeY44XWQJKjYqh5SYZAPJbuuA5JYal6plTbNJ-kaPCeBTetVpAXeopCIv6BYz58KwT0jLJB3UCw1B5ZnPFoEbmof7sCT1d-ccjBGxrDn4GjjB5JDAjSCi3OxJI-mNz7WUoDnAKP50ogzoyQ0rZkL7qBagXoOwUxaw448iKs01oQCHUxvD2lT6sEhsKB9d_To8fpVkDz64E8ywcyU6vTmiLk1qtKYF2hEPg11_nnrY4b_6uB2CxHRFxG_tuIJgj063RfItS67hm7TWpPU7gUERcbPLwacZHC2SRbCC3NK2OnIjb3SfraO1-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔴
اینو حتماً تو اینستاگرامتون فعال کنید!
برید:
Settings → Data usage and media quality → Data Saver
با فعال کردنش، اینستاگرام مصرف اینترنت کمتری برای لود عکس و ویدیو داره یه تنظیم کوچیکه، ولی اگه زیاد اینستا می‌رید، تو مصرف حجمتون حسابی اثر می‌ذاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106998" target="_blank">📅 13:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106997">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-QO6j4Rzp0HvTi6MDZ9T_Sva_tQaeA88wbmOJeLrf4TzfTSeCfpH-dZlCTEmwJ3xUQdMHOqpm0B48zbeL64QphJOmcrOFMsM5u50mbibuMEdQd7G85_mQjF0RG4XIVngF3xHUGt7hwWb5hA6j343bcXHGKGFqoEoQTFVNk_EP9SGlAp6Q7lsB6ZPaehSgrmxJKtDIPA6tG7PcFc3o8bWu8B-dK0c6ld4FRbvg6Sc9KUVwcsS7ZkC4iMuXUO0GFO9aw7RQ1hpeaogeYOqTAEoxzkXjuXBo0-rdTsIxVLdGqTjIlIMm4fGoR2Ui6Wz1Iw-lcttf8oEGEuFZ9OWrdaRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🙂
استاد گودرزی
: متاسفانه پارسال نزاشتن پیاده تا آرامگاه کوروش بزرگ برم؛ اما امسال دیگه میرم
هموطن راه در جهان یکیست و آن راه راستیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106997" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106996">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=BNj3i2d6mbkhAztd2nsbtYJO4qP4bK6LGTeHWPnTuB_hLAI0djw6AZpheySWGPIXFGlV7AJ67U2MLcYILIxCdrZZeaS0J--bT-RY2PpBqZ3Pp9ccREDi4zWvgAZgInUny1Job9VuCCH6DbiW6zAI3ReFOr3egW3cMdt2eDZqesUOxt3kxEfO_4KCJNYN319iQmwxLHtOFOMSytQlyIs32gKlMYANehYkTgKB6lhlwqLR1DqwXHy2rdMXfvfsuhn_bKV-vcNZTzDvhUy4Kj2zlnX8tR2QwJv4w681xFmC3FVndv_8pI8lhymcCK3JNLAVluoRprw3h4VR2Sn64_F9qIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=BNj3i2d6mbkhAztd2nsbtYJO4qP4bK6LGTeHWPnTuB_hLAI0djw6AZpheySWGPIXFGlV7AJ67U2MLcYILIxCdrZZeaS0J--bT-RY2PpBqZ3Pp9ccREDi4zWvgAZgInUny1Job9VuCCH6DbiW6zAI3ReFOr3egW3cMdt2eDZqesUOxt3kxEfO_4KCJNYN319iQmwxLHtOFOMSytQlyIs32gKlMYANehYkTgKB6lhlwqLR1DqwXHy2rdMXfvfsuhn_bKV-vcNZTzDvhUy4Kj2zlnX8tR2QwJv4w681xFmC3FVndv_8pI8lhymcCK3JNLAVluoRprw3h4VR2Sn64_F9qIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
لامین‌یامال از مدعیان اصلی توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106996" target="_blank">📅 12:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106995">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zmq5H4My4Fg5S0cJi--DeCiRQxVTDZL71GuHlYB2TQYjX2GQzcE5bzogUDeRQizfg7L-BYc71nAueBHM3GWbbX5NYJ8ZU4Y2HWbt4ohz7dWJZPIsV2qH3uwhCP466l1LrzXS5ofytmznD5XK09GamWN_f4js8YJjeFmavZbArjiPyjBafwswam0I6ibtt72-xE9pPCnTVlzAbmCdlwFoHNoL9AlXHbmqjVScXXjYlVuk2iV6Wn8EG96FDaL-ursugdC3GJ2qtJTi_e-UXgyzKWszivRaWRIvALfGySGu9DRYNo0__yJetNrEiccwkAlbP7VKA6Ic9Bopxfgaqy3cDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106995" target="_blank">📅 12:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106994">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THGD2oQjSw0uSgRcmEwLJ02C_2dfGUY0PJ971mz0UTadobtdX9CBNZBRztTa-dJM7PH__ThZUSJvpY_ePBSMnXC6PTJbzlu9wI1lDr3iPNvV9V3ito70vGht_3xVi-1pI3Pbkb9ULJJN4UMjiGfWp8Xq-GG06nHwzPhOlzWB2nMvALrmCo1NgB4GXFC_yn-LA3B2WnQMt-skYS0svwROBfajxiHKNi04DdTJ1aaxRpoTOAyUjGN0Vqkuz-NkWF35JVXxyQEyVPNOpfYybS2qDVjw4WrowcybCCgE_gNyklR0gxZev7M2tak8ex8PrneQqk_aG2Uayp3UH9fzHJpx4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫡
🔥
بهترین بازیکن فعلی فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106994" target="_blank">📅 12:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106993">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1dd2f2cd.mp4?token=CGR4ISDnI5Y2k7w00CgLK7viZ34PL2PHcn6nzF8jaU3bm9UP_lkP1ZD-1RSRJtKFM7EOduXde2OwNw4IQm2hzMQn2i1vNK6nR0R1IIni0rLkYSAHh3jPssaKpOj2bxuX5ZR8dxz_hNkUzgo2lfZE40WVVebOuZKxpYkC8dCNV1XG5WUPHU21PrFnDx8sqIvmRVqE8vJRtju74tNjYFEDOjs4rbTjU6r92xqMBvHemS21Z6lKUONGS2voJEhEZMdt2cIzVjtZSjCIIW5WgGUM7BY-PSFo-hVYAbR3l-F0n0U47d5E5l-moTozDUj2xAz-qCXhnhhsoDDS6ykhJXeNxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1dd2f2cd.mp4?token=CGR4ISDnI5Y2k7w00CgLK7viZ34PL2PHcn6nzF8jaU3bm9UP_lkP1ZD-1RSRJtKFM7EOduXde2OwNw4IQm2hzMQn2i1vNK6nR0R1IIni0rLkYSAHh3jPssaKpOj2bxuX5ZR8dxz_hNkUzgo2lfZE40WVVebOuZKxpYkC8dCNV1XG5WUPHU21PrFnDx8sqIvmRVqE8vJRtju74tNjYFEDOjs4rbTjU6r92xqMBvHemS21Z6lKUONGS2voJEhEZMdt2cIzVjtZSjCIIW5WgGUM7BY-PSFo-hVYAbR3l-F0n0U47d5E5l-moTozDUj2xAz-qCXhnhhsoDDS6ykhJXeNxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند ویدیو معروفش که با هوش مصنوعی درست شده بود را بازسازی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106993" target="_blank">📅 11:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106992">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETmKAlVE74prLjXPC9W84fPtaIcaXv1_ForWWJj8meFA2lN8eFnkI3pNJZsrKRlmSr14CpSftMPUjTjQXyh40dQy_4v6Anz6aOU5nvS9dnxBQTVwJPJ8vwWzcgT5EC_35IxGL3qeEZRkifE8Cw84t3aeAepzNglwTgs5MNiaXJTCOFuQ_DG-diWtSkaLcj7jZ46G_kj6AFywx9qFTZpCFpZnSPq3VfQU-PALkxJ5rc-9-m1AOP0sz5_BMu0mXOriSowz5ol-aym9gYaj_mnfNapDDG-4pSGA-8m0lnyd0kVOSLbM-9gsdZv8lMBc7gW8Duc3o3bJBYF65ifGH1HDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
‼️
اعلام رأی کمیته استیناف:‌ اعتراض تراکتور رد و محرومیت 4 ماهه خداداد عزیزی تأیید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106992" target="_blank">📅 11:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106991">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0476c7864.mp4?token=qn4FiJTO7lgqflGrFzHGydsumFRkMo11o5N3o3TbgE12L2TE-YKM_haNEJoHoA0qr9Yv6CJ-8-8QlGkLmk6YYMqua3qJepoW2nlA6roySzBuHVeqbvjdBdXFXSfkgSB5GQ4-ZrO1PvW6p3HoWP_IYXxgQToGfg27EiyqvVKZLzOr3N0dZjZRUkTS_tDL7cttxeMpMw5w9JTUVXUrkVCcoI4zKnimFRxvNXWUmk83RtHoqrhUIpxdQFEeLvSeDCFV_HwUybOSFQL3P1pEwnV8_bSwWYY5XOD8BuEq2G9du4wijhK8xdjRefr9B5T4Z-sdBJk_VhEOIDum34CQfzYHRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0476c7864.mp4?token=qn4FiJTO7lgqflGrFzHGydsumFRkMo11o5N3o3TbgE12L2TE-YKM_haNEJoHoA0qr9Yv6CJ-8-8QlGkLmk6YYMqua3qJepoW2nlA6roySzBuHVeqbvjdBdXFXSfkgSB5GQ4-ZrO1PvW6p3HoWP_IYXxgQToGfg27EiyqvVKZLzOr3N0dZjZRUkTS_tDL7cttxeMpMw5w9JTUVXUrkVCcoI4zKnimFRxvNXWUmk83RtHoqrhUIpxdQFEeLvSeDCFV_HwUybOSFQL3P1pEwnV8_bSwWYY5XOD8BuEq2G9du4wijhK8xdjRefr9B5T4Z-sdBJk_VhEOIDum34CQfzYHRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
‼️
🇪🇸
ویدیو سال ۲۰۲۳ بارسلونا وقتی که یامال ۱۵ سالش بود و شماره ۱۰ بارسلونا به آنسو فاتی رسید و براش جشن گرفتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106991" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106990">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106990" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106990" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106989">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTCM-t2YLytlPFuXaAwgWi8V5wFgCfIj_sktEpf0MW-i9yFDrv3qPfuv3CSCoGQuGZh_xI2IkPrzRwE4VAOSaQWMezdu_AFCkR8ofk6gMKuP3yc8bjMLpdC99WJyG1rE2vJRUwGDYGnotyvwME5qCqu8S7RNj9QGz5W0pp45D07qG-xCNaKFaDQrfp87KoyYxjopJrVQsD2obb3zVoB54-D0ReC4wg8VAG0w1ZQHv0J3saJZ_ud6f4QznNmCJbX2CSqJa29LTHQgOgdIXq8-y-HxvwetS9P3NllG7SmP5Wg2nPYbO5KuJQjXSbUFhUwzo4YeCphuyg8R1oNYHaBmNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106989" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106988">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ee4811fc.mp4?token=MWkMjr0j9TsXtoQtBkNfWYnIlFKkjPipWzS-IyQz4JEdJqZjG30rS7qt1KoFMHy0LHiBRBslf5Xb2p80ZB5Nx6yLlSB7MPcourp7oAl1BtHvEr_deVBQdKMJTtBZqaDg1bCvqv3zTma2JPU_l6OGkIojQWDA5_Ub2CT3niFfXcx0Gr9mYJKKHxSeUuc5DScbEoyYe07GPNTYPZZMhFZ5hnRE6HEidK4z50ysfPnsJ1tLj1V8E16JDHAwo4p2q-fYJzogvIzE3GnDDdYKmYVBGkNVsXT0YB0jCUf_nLKsRJr7d1ZVedgjJ0NPi1c772yPWX-rirsw8tZMIoveg5fqhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ee4811fc.mp4?token=MWkMjr0j9TsXtoQtBkNfWYnIlFKkjPipWzS-IyQz4JEdJqZjG30rS7qt1KoFMHy0LHiBRBslf5Xb2p80ZB5Nx6yLlSB7MPcourp7oAl1BtHvEr_deVBQdKMJTtBZqaDg1bCvqv3zTma2JPU_l6OGkIojQWDA5_Ub2CT3niFfXcx0Gr9mYJKKHxSeUuc5DScbEoyYe07GPNTYPZZMhFZ5hnRE6HEidK4z50ysfPnsJ1tLj1V8E16JDHAwo4p2q-fYJzogvIzE3GnDDdYKmYVBGkNVsXT0YB0jCUf_nLKsRJr7d1ZVedgjJ0NPi1c772yPWX-rirsw8tZMIoveg5fqhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدای کم‌گوش بدید
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106988" target="_blank">📅 11:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106987">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9186ccb478.mp4?token=UTI-wqX-x2XtVgiELbUv6cjrynVla_CVZA3PPZ7bN-ebYTJns63uZNztn7pLQ7TenDbvQk5Xwsz0pjmwLUfdkAUcw9Yw7ZuIw3K52fBcQxLqKhFfL8dZC51gedSkkhXD4EDknOiOpac4MXNB4yUGW68OgML8yk1R5eUVdNLeZy-YQo_fVxwDPEHWqabhSY-oWNifyYWgkz7paPsytXUIZHXpL6zp1Yp9uzfLWLCEHDzoN7bDLtiU0y-YV7Xo_FQwCHVIwkAptM59l5U1jmrsR07NjVoZGwd9hyrel6Dyom0sVhBQklA01TJrx2qbSJC5LfgYDX6d-b0S1nVpXMnjXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9186ccb478.mp4?token=UTI-wqX-x2XtVgiELbUv6cjrynVla_CVZA3PPZ7bN-ebYTJns63uZNztn7pLQ7TenDbvQk5Xwsz0pjmwLUfdkAUcw9Yw7ZuIw3K52fBcQxLqKhFfL8dZC51gedSkkhXD4EDknOiOpac4MXNB4yUGW68OgML8yk1R5eUVdNLeZy-YQo_fVxwDPEHWqabhSY-oWNifyYWgkz7paPsytXUIZHXpL6zp1Yp9uzfLWLCEHDzoN7bDLtiU0y-YV7Xo_FQwCHVIwkAptM59l5U1jmrsR07NjVoZGwd9hyrel6Dyom0sVhBQklA01TJrx2qbSJC5LfgYDX6d-b0S1nVpXMnjXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
تعداد‌گل‌های این فصل رافینیا در مقایسه با چند تیم مطرح اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106987" target="_blank">📅 10:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106986">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxMx0wJkst91TrYqx7v5UQ7DTzwZnbLEgrO0uUNOQe52MdOiQMtCK1WP6uCAp6yEaDDB_d_Ft-hFCPYVcpnsTnopzBJ4kwu88b8JHgECWTGhuXTgH1AtdLkl2QMCkCSAR_HOT3cr7ArcnUgXqSo1V71OS30F27A4FIKPdPusEHT6yxYJwlZ9V-eyOIYlIWPOJB232w6kmZQk-JNzpcC8djGw_do08twpMMjUf3qYapcQXfeh4BqpMTX-jsN41i5Xw-Sfz-lPTjnfArX8n4TqS-Xt8zp4pmd5E7rHmHI3mOXp903PUmKrAiV2ebla6PTNMRSZfkDDMQjBk-PDjzorFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
احمد ایراندوست از بازگشت شادمهر عقیلی به ایران در آبان امسال خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106986" target="_blank">📅 10:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106985">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a7263425c.mp4?token=o7ojyut6bm4Ur0GDCnc9bcpgskqmLhta3Eym10ybzkUj6SVSGK7ToBgOB7KF7tGE-PAn6yMBEGfv5EWcKIuwV7sZSgNtrAZ5aYelqlW9_DZRbTBovdKXUwwOPsOnKTsX4rIVB-n8CQSfEAnd6q-lOEDlWT0dPOm74GhFqvQ_EIcOQyw6CGJIEOFvc8HsQLdxy8tg7klz1PgwSKtZ00WpBlHBm8H-eMi33jVDWEsaw37dZEb194jwh-8O8JqzTILR_fL84WcHqMBM39OWUlYOhWfNFvAUb1o9ZBwjyGN_SBvjAj-WqflreteswO7xgd0faA9Hju1zS1_uRNcbsgwRTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a7263425c.mp4?token=o7ojyut6bm4Ur0GDCnc9bcpgskqmLhta3Eym10ybzkUj6SVSGK7ToBgOB7KF7tGE-PAn6yMBEGfv5EWcKIuwV7sZSgNtrAZ5aYelqlW9_DZRbTBovdKXUwwOPsOnKTsX4rIVB-n8CQSfEAnd6q-lOEDlWT0dPOm74GhFqvQ_EIcOQyw6CGJIEOFvc8HsQLdxy8tg7klz1PgwSKtZ00WpBlHBm8H-eMi33jVDWEsaw37dZEb194jwh-8O8JqzTILR_fL84WcHqMBM39OWUlYOhWfNFvAUb1o9ZBwjyGN_SBvjAj-WqflreteswO7xgd0faA9Hju1zS1_uRNcbsgwRTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🟣
گل‌تماشایی لیونل‌مسی از روی ضربه کاشته در بازی بامداد امروز اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106985" target="_blank">📅 10:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106984">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a81f86f53.mp4?token=ClK-W-Br7Epn5d9xacxnlZY1kvii9FQwWjzp06L-r2LYHboxG2x9W5shdS0-BolLgIdfP70uGm2bhlc6fc6Ah0DyFu2A-8naTDxabznFKoaGrZeC50hw7OC-UekTn4xCOOZHTgOWF1XHLoDj4VjA1g37F_REIR0rrhbdqMUeoGLVNT_2BX43QK3b42fasYToS-IHPR38zg7z2X60jcP6aoCJSaGwyjNnscj5E-ZInOS8Crd0q4FyqIadRFUh7O5jEDfjrPne_F8PTWu-59vdJfobYCZFbEQhVes70TCKGeN8UK2b31qauKgXwqmRmDIkF8cLI5iJ-wLsK3CfatJtYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a81f86f53.mp4?token=ClK-W-Br7Epn5d9xacxnlZY1kvii9FQwWjzp06L-r2LYHboxG2x9W5shdS0-BolLgIdfP70uGm2bhlc6fc6Ah0DyFu2A-8naTDxabznFKoaGrZeC50hw7OC-UekTn4xCOOZHTgOWF1XHLoDj4VjA1g37F_REIR0rrhbdqMUeoGLVNT_2BX43QK3b42fasYToS-IHPR38zg7z2X60jcP6aoCJSaGwyjNnscj5E-ZInOS8Crd0q4FyqIadRFUh7O5jEDfjrPne_F8PTWu-59vdJfobYCZFbEQhVes70TCKGeN8UK2b31qauKgXwqmRmDIkF8cLI5iJ-wLsK3CfatJtYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لوئیس گارسیا پلازا، سرمربی سویا، پس از شکست ۳–۱ مقابل بارسلونا:⁣
اونا خیلی، خیلی، خیلی، خیلی خوبن. همین که تونستیم باهاشون رقابت کنیم، کار بزرگی کردیم؛ چون بقیه تیما رو جارو کرده بودن.⁣
توی فوتبال یه‌سری اتفاقات هست که نمی‌تونم درکشون کنم؛ اینکه رافینیا جزو نامزدهای توپ طلا نیست هم یکی از همون اتفاقاته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106984" target="_blank">📅 09:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5061d27e31.mp4?token=E9yxrpTaZdtCu2aVkHMCI-X5CSyWjdJ4KrayZd5OktDYrvpA-jFFkliaMwMHviaYsFY1NhajmWEVkSIDPxPyGgJjhBlmaWBsBQ4drF82T06wjlH9-iHoB1RuNzyr0rHo6C9tc1R5PslvFTAGXjm8YfXtHq7V6x3Xmw4H6XkgnQW6d_cqydlLE2sRn6s2MvtDWOb71VHceLkLq1b1WWBy1kKwNTWcQF-dAhJMhL7Ko3R3ovgQiVsxCJsPo8740aNYJskzDNwlQKTql3Jqf51OlQnb58pP_O2o6MDkwTHhkOUY8gxa0b_bpkmGd_xuSDg_pZPltUqwSWHnWjEbT2iIgDW3Af5NNtp2GQXVi5PzuANbECNZbsCtC3r9M_aPdb0I5lBozOLlqBy3hn344Ns9a2S-p01Y8R6fFiFEKVEuh9Qg3BhedLlLzc0md52zvFdyhCImjzBuOCRsozYdOZW4SkKATvF5-zjIXGZm8MqPdbEA0knBIbCmmxbKlrEHbCZVpqoJHnhbvcxRTRzn-DRetla9Ey3OQtoo59bew_qZnOgrAcCuVItHJHnX_KMUJq2LF2UGaVNw_bj34Bnu_C5Ig0X7aT2XFk9IlfLfAZ9IJkRQJx_sNFuc8EoZdvLbN6K1cBiasqW_4_emZCUoBhmiiOidhBeg0N-f8OE1e5vRYcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5061d27e31.mp4?token=E9yxrpTaZdtCu2aVkHMCI-X5CSyWjdJ4KrayZd5OktDYrvpA-jFFkliaMwMHviaYsFY1NhajmWEVkSIDPxPyGgJjhBlmaWBsBQ4drF82T06wjlH9-iHoB1RuNzyr0rHo6C9tc1R5PslvFTAGXjm8YfXtHq7V6x3Xmw4H6XkgnQW6d_cqydlLE2sRn6s2MvtDWOb71VHceLkLq1b1WWBy1kKwNTWcQF-dAhJMhL7Ko3R3ovgQiVsxCJsPo8740aNYJskzDNwlQKTql3Jqf51OlQnb58pP_O2o6MDkwTHhkOUY8gxa0b_bpkmGd_xuSDg_pZPltUqwSWHnWjEbT2iIgDW3Af5NNtp2GQXVi5PzuANbECNZbsCtC3r9M_aPdb0I5lBozOLlqBy3hn344Ns9a2S-p01Y8R6fFiFEKVEuh9Qg3BhedLlLzc0md52zvFdyhCImjzBuOCRsozYdOZW4SkKATvF5-zjIXGZm8MqPdbEA0knBIbCmmxbKlrEHbCZVpqoJHnhbvcxRTRzn-DRetla9Ey3OQtoo59bew_qZnOgrAcCuVItHJHnX_KMUJq2LF2UGaVNw_bj34Bnu_C5Ig0X7aT2XFk9IlfLfAZ9IJkRQJx_sNFuc8EoZdvLbN6K1cBiasqW_4_emZCUoBhmiiOidhBeg0N-f8OE1e5vRYcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
✔️
سوپرگل فوق‌العاده در لیگ‌کشور مکزیک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106983" target="_blank">📅 09:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106982">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9b6fbcb00.mp4?token=E7T2FU7OZ3WGBpGx61GaC-AswxGii0fQKYLfZS8uNpiEc6rToIs4QCX859PP-zt6GtAjqX1-0GYp7rK2Vhj77TckCC5qRGefDpRJYCEoKFftZAfWic6sK89aXC1SCYPNt1Ae-DhZgjVt66ZMuoidxJLnKBjD9ksCVknqwfGj6eHH4LvZ0fyImAlvHjtESxH-3F7Lqecd0-PeNu4xJixvpkYAVYeF4PnxXwdv-2P4_AS5RwnRuGkroYNDLi3qtljXHx2-OLSdUviUd99224306JMFP8eMMZXLwQpyjpw8ei9392buGlDhH0dPM8w0HrMbVEioN57tmjWsk28ZhvKB8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9b6fbcb00.mp4?token=E7T2FU7OZ3WGBpGx61GaC-AswxGii0fQKYLfZS8uNpiEc6rToIs4QCX859PP-zt6GtAjqX1-0GYp7rK2Vhj77TckCC5qRGefDpRJYCEoKFftZAfWic6sK89aXC1SCYPNt1Ae-DhZgjVt66ZMuoidxJLnKBjD9ksCVknqwfGj6eHH4LvZ0fyImAlvHjtESxH-3F7Lqecd0-PeNu4xJixvpkYAVYeF4PnxXwdv-2P4_AS5RwnRuGkroYNDLi3qtljXHx2-OLSdUviUd99224306JMFP8eMMZXLwQpyjpw8ei9392buGlDhH0dPM8w0HrMbVEioN57tmjWsk28ZhvKB8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فاصله بارسا و رئال به شش امتیاز رسید.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106982" target="_blank">📅 08:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106979">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXAXFxrCgmUfTvutylVQl1Gd32GzJEw_ViFDftZEExYtDOYyxVe9MChIJrM61PnrVRFEOhM4yHgoTm_SaIgCzWUOz5Vzt1ws40-8EH3D5h4aY8OLi4WgtoM5t53eRcMUDt42cTRCIg26W6VUFE39hlaxrWq7RQobMq13NnUJgQwssH9pmvaX7qrfMVJAZdRf6muapArmg2QzPP7ruaGbhiDuY0HoPm798NQNMGIPGYvReemC8p4_1M38qZL3Jk_QejL6zFoETn_L8jjAzVb93AKo8bm3mxnWSOC45KQD_UGMbEVM8R4BHGKzuyQ3h_4ytOfkKhDqPI3bPIQH0Cjdhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
سیمئونه درباره بارسلونا:
🔻
انگار اونا دارن یه ورزش دیگه‌ای رو بازی می‌کنن، نه همونی که ما بازی می‌کنیم. مهاجم شماره ۹ نداشتن، ولی یهو رافینیا از راه رسید و ۱۲ گل زد. یامال هم اگه اشتباه نکنم ۷ گل زده.
🔻
توی زمین خودت بهت فشار میارن، زمان رو ازت می‌گیرن و از ریسک کردن و گل خوردن هم نمی‌ترسن. حتی انگار گل خوردن باعث میشه بهتر بازی کنن. اونا الان بهترین تیم هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106979" target="_blank">📅 00:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106978">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPA_a-auiWIAi1kGIaZhTmjKTE8kqD8XefrS7lX621Xl02QZvwt6nsIb_eOvhE6kES8IFLFiEUdPyA3j4biteLxC3rq3wmI1g6Bxvn-XRFXeBw9uFygQHRAlSnHHAuIRMUv8eXVv1LZxoXPrjOGlQpOy1jyBXXCsljxeYpSVrJ93-vYTuViv-G9cbzzetkpFKqIle7u875K6ja8ylkicANhe-ZSkJc_WmS1KvNTEklfNJrfs_uK8VMHHLWhKgKOfN-IFwkcHjC0v1ONgPUbCd8mokU0wvUsTvuBZiWjGfi1fmmSP2P1ADCQvrjF91G4xeuCxZnuWd7smGN_1Z7dPXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⭕️
شبیری‌زنجانی از مراجع تقلید شیعیان دقایقی پیش در بستر بیماری درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106978" target="_blank">📅 00:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106977">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIUgGhmzln4E6Sn-fM2mRwWr1nrbOQDoZBzB3zkVlV2IflINojGrhBfo8lxdvFSYdg-1r1-J1Iu66fFH6H2J_7CrodUxfbO9VLImGHQa6YVR03joDqvwO9gLS5YACZ2ovqUS4mSI5kvO-NHPWHE4t6pKXzf-k0eHYirCVW-cjU9A59cew4Egq_Dytf_wvgX32owNf9ZmC78n4Qj0kX1AC2NVdlcg0M45BYu93Rw-cTMs_-Ci8C54A1au9N4Dq8MfC-lsPfZ2Ga0aMoUTCIxJtoAg0mkqvPRUWqhoA2PxtkiYZZvhkF4S7qQp7dqHLAmzsnfLjurTKEnkijTof5yoEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
خوزه مورینیو: به کمیته داوران تبریک می‌گویم. آن‌ها باید از این نتیجه بسیار راضی باشند. همه‌چیز بسیار عجیب بود. بازی باید ۱۱ در برابر ۹ دنبال می‌شد؛ چرا که اتلتیکو از دریافت دو کارت قرمزِ مسلم قسر در رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106977" target="_blank">📅 00:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106976">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJaL8sEYjMLXipmv9OD4nMaJYdTGfRC_4y5nqiFkaqLJp-Zl3NWBTy0_04v65wtimRsKHu0DzuOyzY7YHWZhui3t5F3NPcnQ6vakSVIDY4oJKPOfHL2BMLyHBNtF3fi1bQCsA_Q4FDUG6x0fRpdNUeefEXH9uShb6B565TCxorBCXFDUGPgz6wIWxF-Vt3Mq21tkRGlwnxGwoXEO-yBUfnQ2InedAsjAkYx042qfPZh8w4MZFiTe94ut9vVDJKdRhU7aI0Baceg7yf1ufUwh51cttvmY4-Ejl_Glad1fDEdiXkU0onFKVwyr0ak17uBTy9-ig5c6auLbznP0929eCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بارسلونا در فصل ۲۰۲۶/۲۷ تا اینجا :
⚽️
۸ بازی: ۸ برد، ۰ مساوی، ۰ باخت
⚽️
۳۶ گل زده
🥅
۸ گل خورده
🇧🇷
رافینیا: ۱۷ (
⚽️
۱۴ گل،
🅰️
۳ پاس گل)
🇪🇸
لامین: ۱۴ (
⚽️
۸ گل،
🅰️
۶ پاس گل)
🇪🇸
فرمین: ۶ (
⚽️
۴ گل،
🅰️
۲ پاس گل)
🇩🇪
آدیمی: ۵ (
⚽️
۳ گل،
🅰️
۲ پاس گل)
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گوردون: ۴ (
⚽️
۰ گل،
🅰️
۴ پاس گل)
🇪🇸
پدری: ۳ (
⚽️
۱ گل،
🅰️
۲ پاس گل)
🇪🇸
اسپارت: ۳ (
⚽️
۱ گل،
🅰️
۲ پاس گل)
🇪🇸
اولمو: ۳ (
⚽️
۰ گل،
🅰️
۳ پاس گل)
🇧🇷
ژسوس: ۲ (
⚽️
۲ گل،
🅰️
۰ پاس گل)
🇵🇹
کانسلو: ۲ (
⚽️
۱ گل،
🅰️
۱ پاس گل)
🇪🇸
برنال: ۲ (
⚽️
۰ گل،
🅰️
۲ پاس گل)
🇩🇰
کریستنسن: ۱ (
⚽️
۰ گل،
🅰️
۱ پاس گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106976" target="_blank">📅 00:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106975">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773fad15d7.mp4?token=AWMTbAxgAALhMQUGjA2Sk6LqY_fPYgCQoyZmDodq3b6le6oyvcmsGkGE02XNf5WE2Mnd5p3faXiFT58v_wGTGhs5LION5Se8aQ5iB9Q2tMUz1BWW-YMzZHOoj1Cf-pQHWiBsMnAWksE7rzZNnFWsCVtMKeTid8rgx8NNwdSx5TAICVpBKIKjlmeTI9-9xACo3tlqtSCTgjCxlL4O6TOmVJDv1zskZwZC-JKRdb1RI4pzTCQYZZKq6u0wyTcwUCsY-gHbF5UDD8xNER6-r9BIPxVUhEpXwu5-YkMsQHNgJ-MmR3vl0y0mbH2K7h6nte4zWaKyCPbwzkwYvVVgMZAO4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773fad15d7.mp4?token=AWMTbAxgAALhMQUGjA2Sk6LqY_fPYgCQoyZmDodq3b6le6oyvcmsGkGE02XNf5WE2Mnd5p3faXiFT58v_wGTGhs5LION5Se8aQ5iB9Q2tMUz1BWW-YMzZHOoj1Cf-pQHWiBsMnAWksE7rzZNnFWsCVtMKeTid8rgx8NNwdSx5TAICVpBKIKjlmeTI9-9xACo3tlqtSCTgjCxlL4O6TOmVJDv1zskZwZC-JKRdb1RI4pzTCQYZZKq6u0wyTcwUCsY-gHbF5UDD8xNER6-r9BIPxVUhEpXwu5-YkMsQHNgJ-MmR3vl0y0mbH2K7h6nte4zWaKyCPbwzkwYvVVgMZAO4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم پاری‌سن‌ژرمن به مارسی توسط مارکینیوش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106975" target="_blank">📅 23:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106974">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f22d5f48d9.mp4?token=LHuVE96HLWIU5xqNgUBO-i03BTFEIX26MekwOppldiGLzZG5u6dviGlrYMZWhvq9pDKic2EbtWMrJ3Akc0eZz1IxEmVYPkYcR6VAMhndFSWqnE3sN1H-ptF42XG9TMk9JAEetXEMiK03JQ6VEIQYxmbr4EOvuWv7cRz1XIiM8koT87NKmh4hp7NYMEushr0DqRNRXUTlWepNJcp1TluNok2UAG3aiO4qUHSXoHG9YeuYICwVkY2nvyYuqcJO-MYwiF8AKKMdVagUhPK_VCuIsy3il_tTsdQvZn5DQspqk-dPdej9H4yL2qWf2ZIhCUBDn_MTsjBJCo65ia6E1R4B_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f22d5f48d9.mp4?token=LHuVE96HLWIU5xqNgUBO-i03BTFEIX26MekwOppldiGLzZG5u6dviGlrYMZWhvq9pDKic2EbtWMrJ3Akc0eZz1IxEmVYPkYcR6VAMhndFSWqnE3sN1H-ptF42XG9TMk9JAEetXEMiK03JQ6VEIQYxmbr4EOvuWv7cRz1XIiM8koT87NKmh4hp7NYMEushr0DqRNRXUTlWepNJcp1TluNok2UAG3aiO4qUHSXoHG9YeuYICwVkY2nvyYuqcJO-MYwiF8AKKMdVagUhPK_VCuIsy3il_tTsdQvZn5DQspqk-dPdej9H4yL2qWf2ZIhCUBDn_MTsjBJCo65ia6E1R4B_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی مارسی به پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106974" target="_blank">📅 23:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106973">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed04c10225.mp4?token=DMO1wPNi8iQ0pPY2eHEnXqUDnvOcult-6P6Qsdo27ealpCtzSfG8l9ZzsRh0iNLQ6vU7flaaur9znY5lt5mTOqCeFMI7MKTPt9zQ9yngxxRteSdwQipojQTqpwM9J8AJasbr33bnfuChMddd-1fxAFugvZdC1nnwkjtd2aopX4o77Pqp288DTAEzz71DDAkIVy21CcUO_6r7FZWs82QQeFAsXbRD8mJ-GjJvKi2mezFOqEKhzcDI0gwnrVlLe3hR6Uhf2wGam6W1Hpm6CvqrzDoauu679y11r1PX9zX5-8U38pgOc37bxEAqjAsi8VZr2QktNBxfGop190wi-W6NdKQXHU_pJjz8pyFL2mlk4kGbjBagj9ImGP8U5pCqiYOxDDDSGaDPYzwWukSkkRXSpfxaVHao8To5KIeGwfjiBUUScn8zbrZrJW9BJ7Ltdlo4aWwmVnzCbYejZa8_yEv_LXFpMQtBDr6ZRLwMDwt2F9Vj08aJAZ6szsI2sf3lwerePRRCMyI2S_7odU9sIJNHU2FvlI21zkQCYNIoI5iO9lD5Y9-7LjITfN6EPcTEaPm2pyfaBxg0xs5TcQvGDQQHShLEYfpCCNFYsfSD5Debhg0bYU9it29jSARwgFi_cSCZgCrUd67x8OCGPQc7Wo-fU7LCnrMkkbuCthHSJbVEflE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed04c10225.mp4?token=DMO1wPNi8iQ0pPY2eHEnXqUDnvOcult-6P6Qsdo27ealpCtzSfG8l9ZzsRh0iNLQ6vU7flaaur9znY5lt5mTOqCeFMI7MKTPt9zQ9yngxxRteSdwQipojQTqpwM9J8AJasbr33bnfuChMddd-1fxAFugvZdC1nnwkjtd2aopX4o77Pqp288DTAEzz71DDAkIVy21CcUO_6r7FZWs82QQeFAsXbRD8mJ-GjJvKi2mezFOqEKhzcDI0gwnrVlLe3hR6Uhf2wGam6W1Hpm6CvqrzDoauu679y11r1PX9zX5-8U38pgOc37bxEAqjAsi8VZr2QktNBxfGop190wi-W6NdKQXHU_pJjz8pyFL2mlk4kGbjBagj9ImGP8U5pCqiYOxDDDSGaDPYzwWukSkkRXSpfxaVHao8To5KIeGwfjiBUUScn8zbrZrJW9BJ7Ltdlo4aWwmVnzCbYejZa8_yEv_LXFpMQtBDr6ZRLwMDwt2F9Vj08aJAZ6szsI2sf3lwerePRRCMyI2S_7odU9sIJNHU2FvlI21zkQCYNIoI5iO9lD5Y9-7LjITfN6EPcTEaPm2pyfaBxg0xs5TcQvGDQQHShLEYfpCCNFYsfSD5Debhg0bYU9it29jSARwgFi_cSCZgCrUd67x8OCGPQc7Wo-fU7LCnrMkkbuCthHSJbVEflE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول پاری‌سن‌ژرمن به مارسی توسط فران تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106973" target="_blank">📅 23:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106972">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2832d49487.mp4?token=MttsAHZqfkUe0iGockSDtivdcEMgia1wvkPOzatVfsmHHaHaI-Of-CMWWLWNG7IC3PC5bPOJu2wqB5gVXmF2OIgqTF-gpzy1f0Crh3R6EL49w06LVZZXcCK9E0CoC7rSiNIzGfyeCC6WLFqw1Fhb70caqjDBLb6qOW2fcJtsxPQ1rKxkPQ1O9Fr9deJEzXdm-G-I61GThPgqlB_VWdtO-cS-nWfwjF7L2yGaPiqkNu40juQxbjd8JBETSR2CrzagQHKTnwlpaFlB_YeY5WrwJI4iJ83y4AgJDfvUzLRH_zuSoO2mS-02eIwlNB8DTuWViHLkyRovz7AvZDxbAaUm6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2832d49487.mp4?token=MttsAHZqfkUe0iGockSDtivdcEMgia1wvkPOzatVfsmHHaHaI-Of-CMWWLWNG7IC3PC5bPOJu2wqB5gVXmF2OIgqTF-gpzy1f0Crh3R6EL49w06LVZZXcCK9E0CoC7rSiNIzGfyeCC6WLFqw1Fhb70caqjDBLb6qOW2fcJtsxPQ1rKxkPQ1O9Fr9deJEzXdm-G-I61GThPgqlB_VWdtO-cS-nWfwjF7L2yGaPiqkNu40juQxbjd8JBETSR2CrzagQHKTnwlpaFlB_YeY5WrwJI4iJ83y4AgJDfvUzLRH_zuSoO2mS-02eIwlNB8DTuWViHLkyRovz7AvZDxbAaUm6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم لخ پوزنان به رادومیاک توسط اللهیار صیادمنش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106972" target="_blank">📅 23:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106971">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PURWPkStsoxDPkXD7AcWJ3HTRZzdg_CTt3ZxAlKeGxGcHiq1qG69EeRW6F3__UZm2SCXj7i0iMY7En8g_RhlL-THNyXTtlaC1Csa-rblEP4RLtRuqPJJrqriUvSx3q845pF752WFY5dSItgcFRREZK9Xpc8f_7Jh8Ga5bADwki9LyPcqEH_7UVZWLDcM_zC-f5y3g7Zp_TL5GIgN1Ddk2XeghooB2nfOFx0QwJEW0cXyRB83mRINb9TogLvE7sagBsJ9wdkQVWQsSq9WZOs7K17htXOBiECRvsx9VjhV7ttggT3iahKbUDpZ8CAT4cRpCIM727oVZuSMOnEdQKGmLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ترکیب پاری‌سن‌ژرمن مقابل مارسی؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106971" target="_blank">📅 21:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106970">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=CmWaBMG7U3tKDK44BEavVYkCtKCppyGlvmEE9wO3qG9wdxLzs5nVsR8IuKfoHmL5T82bul7Sv-myIL4eGkq_giP3lRw483pV9uRr8-cF_YqQeVV2hLOXbYiYqnq8ltqX_d8cVsx2oXWQ4Mrz6IwFsWkIkcbmknwsItZNI9lzM9dn-8AcfDdd69eHGKRqIby2iPXqA8mAA2ZkIza05pXYZ-y1rJUlbquQJiwAYmSUETfJO8EcOrAT6AtWqyVAyBFrE47h9S2qHNPT_R1d_LMzy0vEbZ8Otc8MgEhqS8ajUCPOOk2VmglGj6Je18f1YGXFCYFgEFZjtb4Y4sqtd2E9AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=CmWaBMG7U3tKDK44BEavVYkCtKCppyGlvmEE9wO3qG9wdxLzs5nVsR8IuKfoHmL5T82bul7Sv-myIL4eGkq_giP3lRw483pV9uRr8-cF_YqQeVV2hLOXbYiYqnq8ltqX_d8cVsx2oXWQ4Mrz6IwFsWkIkcbmknwsItZNI9lzM9dn-8AcfDdd69eHGKRqIby2iPXqA8mAA2ZkIza05pXYZ-y1rJUlbquQJiwAYmSUETfJO8EcOrAT6AtWqyVAyBFrE47h9S2qHNPT_R1d_LMzy0vEbZ8Otc8MgEhqS8ajUCPOOk2VmglGj6Je18f1YGXFCYFgEFZjtb4Y4sqtd2E9AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
توی آلمان یه دختر تریان (انسان‌های که فکر می‌کنن حیوانن) به یه خانم حمله می‌کنه و گازش می‌گیره، به پلیس اطلاع داده شد، هر چقدر از دختر اسم و فامیل پرسیدن فقط پارس کرد، پلیس هم اون رو برد مرکز نگهداری از حیوانات
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106970" target="_blank">📅 21:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106969">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzYg_m5FtnxbbM1Qd-3GfrRe51CxO5carJoxlC__mIPCmXpmFW0_VZP_i58k5r76QruvQ5WD5x9YCJeRupH1eMhEfmVpuzfK8D-LiBS41kVJXXpsL3wz_u94rMRsTgvRcPWZwTTlzqvwx04bDF08Tz6friYYoq7i4ouw_nQhyV7XXukJe9xn_DahBB8OQuLAIxnXljNJdd7G2vHL3KFfQUs0K6RAYealr6FSkpLowPMBfIdt6YpEm38bzSV7hKaAPJFIchCxFiS5cui23YqpVEz9R0XW2qqW2IRqVgn8CDbwcDc-SzdYc2GIHajDTCpBsxWi-R04wNC5I-YhYAzb_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مورینیو در ۱۶ فوریه ۲۰۲۶ که مربی بنفیکا بود:
تو یادداشت داور نوشته شده بود که شوامنی، کارراس و هویسن نباید کارت زرد بگیرن، چون بازی برگشت رو از دست می‌دادن! من خودم سرمربی رئال مادرید بودم، واسه همین خوب می‌دونم اونجا اوضاع چطوری پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106969" target="_blank">📅 21:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106968">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ir2yPSuw7YxMN9qVTMSUSWCxDsGsL2HoBjTb9ZbnGPI4ksS8wlFyFAzPbkPHkXM8-y8mXbWot3_7uEKYkM6cq685-B5fnLli_oeKuSosOXrLxRKHAyAnl9xk1jkZWIQ8lHMtZIP7trdHX2KoB3EUZeCBoXIWn5v37Vf6S25HdpKlK6lYB0IqWTLBO7HiLcw00MNP7L1xh6x7hUcICyG9Zoz2GOMMFvMUyuB-7kZlsz5fQkiaO9R0PkltccHT9EhznjR6kS3PfkSEeXWUvvvfrpN5C-SAe6j0X03pnr7WEZUwt4Ok83hOPavQpTo9SWtCTFhqTdpV80MFPYjGjvKYsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نتایج درخشان منچستریونایتد در پریمیرلیگ؛ عجب کسشری شدن بعد فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106968" target="_blank">📅 20:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106967">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=q14jsc9aKiR-MegT7cwWD80omvUDxfb4TCQ5xAgmqxj1CNvJqvgF9HBkB3gIwEiLYGV_EkRz41eugz5d_dGyXVOzgueO_lDBHudkKvMZZvy_z8hml1NuGsRLJxmK2RH_5w1GJTTWfGpNi4TKsTCGiv-BtRQjt0Tjy6G0uGscVj3N6JeIaGwY-E3lBPuxxdQz6FgZ2rFoKVxIM99ydGrQkKRSs2QkEZ24GBjsYPVyjBU57LGkL5kvG30uBRgpsMCtcD3Gefla-MIoOQVFyd8W-Ngvi6dhsaEskdif8H-LjlEpvv0xDvaeMVYsuTqEJyVCfDBiG9B1L1tZa7pTMMCyfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=q14jsc9aKiR-MegT7cwWD80omvUDxfb4TCQ5xAgmqxj1CNvJqvgF9HBkB3gIwEiLYGV_EkRz41eugz5d_dGyXVOzgueO_lDBHudkKvMZZvy_z8hml1NuGsRLJxmK2RH_5w1GJTTWfGpNi4TKsTCGiv-BtRQjt0Tjy6G0uGscVj3N6JeIaGwY-E3lBPuxxdQz6FgZ2rFoKVxIM99ydGrQkKRSs2QkEZ24GBjsYPVyjBU57LGkL5kvG30uBRgpsMCtcD3Gefla-MIoOQVFyd8W-Ngvi6dhsaEskdif8H-LjlEpvv0xDvaeMVYsuTqEJyVCfDBiG9B1L1tZa7pTMMCyfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول منچستریونایتد به فولام توسط متئوس کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106967" target="_blank">📅 20:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106966">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0SLTKTOvlNYZHjk0HKf5palLNlj9Q2A3Ra-w5HhuhJ1mw82XtigfoU87g0zuozOtcqjUY_DYT-uO0obYqYgCmVgsXmSxtawhcHdl1GfaUL3w5FrdqetsHPS_RsyHc0QKSyj4wuKpqmWx8x4-L-T2rLNlpzyGYh4OuY-IKsiCgE-5LGvsWjrmPpRxDh9fdKKIVbYXfqUcuMzbYkFsi2eFvPTLAUKgK3WS_dofW6yNnHEfHrEVQSeduL4HyH4N3EKvtPkpIRwQIuZHYuEc4ZQKueLtbW3jHme4gTO5DxonhYcBwSYU8pV1-1nZ4G22FKV7fyr1zMCi72uBx39VOzOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇸
رئال مادرید Tv:
🔹
وقتی پای رئال مادرید وسط میاد، برخوردها کاملاً متفاوته.
🔹
لالیگا و فدراسیون فوتبال اسپانیا اجازه نمی‌دن رئال مادرید رقابت کنه... اون‌ها یه نقشه و برنامه از قبل طراحی‌شده دارن.
🔹
دیدن همه این جریان‌ها حالت تهوع به آدم میده... اصلاً براتون مهم نیست که کثافت و مزخرفات تمام لالیگای خاویر تباس رو برداشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106966" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106965">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34da8be998.mp4?token=IOP-lyN6SEItZtDIbWonYQzYYefc4eEaERQfUHdydQyFnCWsaR7kSl0qutsH1dwNFcc75Amvndsb-a1W5Y6L8Dn-I85F-6dWjHIHcgAkkE7Z1OHSGxVjdSj8pg19A1qAHHGoPT0fDauUCpm8mfANucfjAGVJbPew-_Hc8crduccNYzMfZjpDAGQCN5UWeZ4S82Nc3yRby0BsEPvot5C_UxpyUXTyS4druMRIdNBeL2wZdp7Rv__jwg_VqLQ7Cduk85YmZ8-RnFeUV_lMJrrtwA8GNY6E_3o-94SgMAIY5QZhsjf1Dmd6QKNqq0xSDBoHZAwSIZlSRFwQ8K6nSCGQNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34da8be998.mp4?token=IOP-lyN6SEItZtDIbWonYQzYYefc4eEaERQfUHdydQyFnCWsaR7kSl0qutsH1dwNFcc75Amvndsb-a1W5Y6L8Dn-I85F-6dWjHIHcgAkkE7Z1OHSGxVjdSj8pg19A1qAHHGoPT0fDauUCpm8mfANucfjAGVJbPew-_Hc8crduccNYzMfZjpDAGQCN5UWeZ4S82Nc3yRby0BsEPvot5C_UxpyUXTyS4druMRIdNBeL2wZdp7Rv__jwg_VqLQ7Cduk85YmZ8-RnFeUV_lMJrrtwA8GNY6E_3o-94SgMAIY5QZhsjf1Dmd6QKNqq0xSDBoHZAwSIZlSRFwQ8K6nSCGQNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
حالا که بحث جنگ دوباره داغ شده؛
اگه تو آسمون یه جنگنده دیدید، سعی نکنید بهش شلیک کنید یا سمتش سنگ پرت کنید، فقط این فن استاد رو بزنید تا خود به خود به آشیانه‌ش برگرده :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106965" target="_blank">📅 20:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106964">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=e7FE7QnOWfzJyVG_ncyuNYsxUqgw3J4TN_pBnX6O3PBAxa7JwN-D2RxIlpEb0O5eLQ7eB1fu1QqJBrqIpiIUkOaSje1LMMNvr2G52VmVgTIaEkcVyf2H9I1odrgyoF8Rci7F7joMzOE77oIzhC1ioRv3-4DUR-2ngbUCd1k1p0lL8yp5yhBgbH_RypdOKPHqEcGzy1iKjz6AB7GedhIxXQszAqL8trv0m_yHJb85Mo2xRhWa3XnyFUCC0MJjRbKL6JfQ4HQjrXz1raG0g8EkX9Spc-Eg4C7o0Ru16pns_oq8vSZqxjoaeRji_yaXJ8YUNclRJFv3fCc_PwWx-HlDsYFsDuh_FXdEmhYIUEXGLG6OUCdOaWc47k4NIteaJZhxstqj3RM7p6W70qkS_rlCSGz95lsucPdZhLeigLxbCiuAc93ta02vd789nyx0EqdbJirF5-jPAbF7S3u0_mrJsXhUBC7lEf0LYrmVrefHgh8JkOsV-xE7v4hBr5KjEcLrOf0cfCon3tnh9d5pI54KDGg6hdTXepP9LB_I14GvqPxxOv4usQgGHqi1-TGLnTfWCMrepePooQqrwBiDfdRxs86MGiN4p4J5C4_2ClaBe_TGqo66xl5jZkt2zuqwvSXWz9iQmUETXsqpgn4E1u6s7rlIZOgvQ7raAbPR9srkZqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=e7FE7QnOWfzJyVG_ncyuNYsxUqgw3J4TN_pBnX6O3PBAxa7JwN-D2RxIlpEb0O5eLQ7eB1fu1QqJBrqIpiIUkOaSje1LMMNvr2G52VmVgTIaEkcVyf2H9I1odrgyoF8Rci7F7joMzOE77oIzhC1ioRv3-4DUR-2ngbUCd1k1p0lL8yp5yhBgbH_RypdOKPHqEcGzy1iKjz6AB7GedhIxXQszAqL8trv0m_yHJb85Mo2xRhWa3XnyFUCC0MJjRbKL6JfQ4HQjrXz1raG0g8EkX9Spc-Eg4C7o0Ru16pns_oq8vSZqxjoaeRji_yaXJ8YUNclRJFv3fCc_PwWx-HlDsYFsDuh_FXdEmhYIUEXGLG6OUCdOaWc47k4NIteaJZhxstqj3RM7p6W70qkS_rlCSGz95lsucPdZhLeigLxbCiuAc93ta02vd789nyx0EqdbJirF5-jPAbF7S3u0_mrJsXhUBC7lEf0LYrmVrefHgh8JkOsV-xE7v4hBr5KjEcLrOf0cfCon3tnh9d5pI54KDGg6hdTXepP9LB_I14GvqPxxOv4usQgGHqi1-TGLnTfWCMrepePooQqrwBiDfdRxs86MGiN4p4J5C4_2ClaBe_TGqo66xl5jZkt2zuqwvSXWz9iQmUETXsqpgn4E1u6s7rlIZOgvQ7raAbPR9srkZqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول فولام به منچستریونایتد با گل‌بخودی لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106964" target="_blank">📅 20:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106963">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eez4MwGMrEWn0BcjEXLu3PUJsDYovgOONy3T9SsEJkqmVzz3p53YxJX6srKCI07hsMN6UAK54M5hOCmIoh-xSCoZaYlZk595nNze4a88SjI4AMpPR_9B6y3qGLMTOjwI7iyH2b6vSHc9-JMh_nla5bIXnP3emyejzHeAF_8_aZykLgV2s7Fn3gYbDVY0xWsFFW-oaHGcss-ss82gd5Mw1rdVGcTfFH58HHK5wjY_cJz6kAeoK7b_zUN6dtK9ecxoAs0qiKmk8bTP5EL2ivU9GAAGjD-U8TlTWAnE-gO6vpO2YqaG8huj-WPpJQH-lyOlvLmF_Is9vAE10axGHMBoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
خوزه مورینیو
: به کمیته داوران تبریک می‌گویم. آن‌ها باید از این نتیجه بسیار راضی باشند. همه‌چیز بسیار عجیب بود. بازی باید ۱۱ در برابر ۹ دنبال می‌شد؛ چرا که اتلتیکو از دریافت دو کارت قرمزِ مسلم قسر در رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106963" target="_blank">📅 20:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106962">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVS-RkTABxMvTvhpDOOarUn9-zJx3fdKT7uRpvfT8PPbeCHiFBfI9e5P76fMBLm-M8M4TVFr0GPcVYYOlV_qfVeLMyBQNyGPCK795Ky9mjCUv6JijzozpGA_8VbWCEUGUS6QjslA-yW4WBCGkdx3kRg14m3KX9mPf6et_2ZMVRApDrQ6oF-svJ_rTPlpLo6LnmaJpbQsysYRPmaPVka3rxCWGnKglKosyKDIZtQ1lm0KMi5oaVknp-OGItiwphhF0zGucYxJajSqZlzKCmoxrvRJWn8j_nrTWSO4Cbma6apb89eshEVvaR_G83ujJZE7ZmlBo0X7ERhFrIccOtEQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
کانال رسمی رئال مادرید:
اورتیز آریاس داور بازی، رفیقِ لامین یاماله…
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106962" target="_blank">📅 19:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106961">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6M8rjkqM-HThfQJ3fVWpYKgizq3jPbYzrazELc9dIvPxR68P2MGkFedoOdjtVNuSXiiMmsocr2-SQ8-IbKHOSiFJkczOAhbNAkH6rKIb9SQZ7cL3vnXTNaOkkcaMmYoPdK2r-NCJQbPtTthWSLsy_dALbBH8vN9E16BLzAhzt7uMh17Nd2CD4yqLpKSbc1S0HEJef1oABTwGfAPVSRF_A8RMK8NJ7qmnNmFVJYF7AugGnHyqyr5ivjaFEVun162LokX3cZurz8FogS4i-Ialg5P8wGhY9ojTNOe0RGyyvHuOlULUDBiJChdpf5mSs_MNgSl_nQq3-irbN03Gy7YIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106961" target="_blank">📅 19:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106960">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Afx-2J8o2WcQse0K5iPQxncuKq3hllYkKOhwTW5xVvsFhCIDw_kOowY2cq7vvy_05f4Xr6pAgW-SpFag1HEVcyiJP2fOrSWmb2ZSvE9RM1UFFfz06psj6INKe_keeD7P4vUEVHchdV-3aJPf3MbEt_il7CGJhmCyI13DLKtifHtY-tG4KZGplknLMRu1xdwM5JFCi3HU0Fph0zCHx_KsnFO_vnZX66iUqCarYdyvQLmfCotcs4SeB-diCPETIp2Vg-nHerI7S5-DKbpI5cLYWlegMNLagtslyr8ft-Y5kqv2Q0rbEn7xZVOsdhnKWRTns9IeqclZOAZKgNjtjgQWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106960" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106959">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jd4GxjPNii3wNPybGdZFm9X3L_uu2eJj-64huQpVz12qbMq6s11AvdEtEebuTxFLIuGwp8PAKbbFaFrrEzgFbYLEKH6pXMQ2QEMrD1wB4rnRr6zOLHJ2eqahlfxIDB7gSnxr4tZo5VXApZl2S-eGxI80Z9dNeqeCp0BeOLy2SXsXCPZn7W6onNW9NgZultvN9vuh_HiHFrGo7uSAckL8Gy0PeGg5bB597tZTIPscwsIIiOjMUV5qewqKaFo9LTNtjJtwqCSNFtsUUgsLO6juHUJ3Ya_kVWyIdKMfxLlklEsB-oWAWC5lDtwrYyDsih4ed-XvCeHCnPA96gjLnhWaoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106959" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106958">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">۶ دقیقه وقت اضافهههههه</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106958" target="_blank">📅 19:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106957">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دقیقه ۸۹</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106957" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106956">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رودیگررررررر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106956" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106955">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رئال یکی زددددد</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106955" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106954">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106954" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106953">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یا حضرت عبااااااس چه توپی گرفت کورتوااااا</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106953" target="_blank">📅 19:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106952">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اتلتیکو دومییییییییی زددددد
🚨
🚨
🚨
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/106952" target="_blank">📅 19:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106951">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106951" target="_blank">📅 19:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106950">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7be2074ac.mp4?token=MCJ1RbLzrF26_SQ0UwchnNDrJ5rNVvXLJeRw9X7iz-5lxNl7RVuEA7GC8Q8z4v65HJtGwoDPTIPxFcwNllzn_4Dich1dKrYtanBBL7MxMUOWCzXpkse11aFa6OcAm0i8OhJxEjMMV0wImYuN6cdl-pLgZg3DtkPhEYikzL41yAILaDIXYH_xhonBjVCJ4A_HbsxuLO4Om2vLcZadg4wrlZkaxF7O07Zjlhs-QGjV_DkKl9GuIMnn2XdPdNRdOtxlYRiiU9Avo0H5F8qVtVUfLu-sxcJbiBXqNCML_wIfF_RXJsjbSl4mBxBU-Rhbxp4VuIOLPGLBgRczNT6jBKb08w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7be2074ac.mp4?token=MCJ1RbLzrF26_SQ0UwchnNDrJ5rNVvXLJeRw9X7iz-5lxNl7RVuEA7GC8Q8z4v65HJtGwoDPTIPxFcwNllzn_4Dich1dKrYtanBBL7MxMUOWCzXpkse11aFa6OcAm0i8OhJxEjMMV0wImYuN6cdl-pLgZg3DtkPhEYikzL41yAILaDIXYH_xhonBjVCJ4A_HbsxuLO4Om2vLcZadg4wrlZkaxF7O07Zjlhs-QGjV_DkKl9GuIMnn2XdPdNRdOtxlYRiiU9Avo0H5F8qVtVUfLu-sxcJbiBXqNCML_wIfF_RXJsjbSl4mBxBU-Rhbxp4VuIOLPGLBgRczNT6jBKb08w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌اول اتلتیکومادرید توسط گریمالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/106950" target="_blank">📅 19:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106949">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اتلتیکومادرید زدددددددددد
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106949" target="_blank">📅 19:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106948">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گلگلگگلگلگلگلگگاگلگاگاگاگگاگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106948" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106947">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دین هویسن اخراججججججج شدددددد
🚨
🚨
🚨
🚨
🟥
🟥
🟥
🟥
🟥
🟥
🟥</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106947" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106946">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پنالتی برای اتلتیکومادرید
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/106946" target="_blank">📅 18:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106945">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
کانال رئال‌مادرید: وقتی داور طرفدار بارسلونا باشد، چنین اشتباهات خنده داری کاملا عمدی بوده و پرونده نگریرا رو بیش از قبل بزرگنمایی می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106945" target="_blank">📅 18:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106944">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106944" target="_blank">📅 18:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106943">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYU8yIXQlxeSGWxlo0R3quVpgqwTJyOAsJVJGdwwrHE2yH5qYmCw70Afqid2Lqq3HDICQWhtJKNpCWpMdxnNpCO9WNGyva-fZ2T17kMhJqfTGWvJ0KV_Rywj-1IlEsjCjHMpHdCUfkTV5bPIiU0whBX_XBpEGVIfg4hxO0ee_s6NIrDD3pkIrfWzqVpNdvPDb2Qdq9p8-onZMqlvssM1mAE7LbQyx2OIzExvbwhbUsFysezRor4CPXkEiKgSUKUaKyym4tRqb5ciChuA1-W-hvsxu0UYOpa59qf1Z-TCkBJUsa8eyGmpurCH-oQTtWaSHSodZPB4fSXcqcODytxueA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106943" target="_blank">📅 18:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106942">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrrawlOPxYu6hSp_D7_L8g6hUE9esPIQKVupOL76ADpR1xc0BqsS_k6zviZHhsDDp0L6UzX86Bgx8_W36IO3KhLAN5XHxms4Ti19iEVg3FdRtgotecqsGgEZSlpX3Um3vW1UKKPw2wJDS61OJRgs03qEOBAIILpf-0Ul6OCjqUeg0PpCy5OX35tEBurSx_bhPdmK-EEbbhm_rwziviURJQ03aOc5CUoHeFUlSRwYEpV7mWIW4rMO4dsfSYUjc3PlySpwL_4CatthJiQ5mw7JJRCNd8lRxTxRTB0rZGMCzZ2cc91NTFssNJWzCxfX7Oev8Rygp9boyTbsKJMJmMbBSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
با گلزنی به ساندرلند؛ ارلینگ هالند اکنون مقابل تمام تیم‌های پریمیرلیگ که تا به حال با آن‌ها رو به رو شده، گلزنی کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106942" target="_blank">📅 18:27 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
