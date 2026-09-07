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
<img src="https://cdn4.telesco.pe/file/Wgb402k0b2AHDzmzPSzD6ni9LB8gB416e6a12LaC6GZaHFpW0C4mNuykAPzWNbjYNwqZCnajcdIRQt9qg3wOZMgnHXkr3SfXz_eqc43GM_ESiN0CWQc2i7sbmxvgzqZlL6HJ5mB0ReymBOK9_Ef_msOVMkgNOBHrC6jHwbTbPhe8DoAl-VXnSTKDqriU0_fnluf73KWpF0WhY89o0ZqmczVfiWqNttmtay-Bn5IqzG3M27FFTdZIFOD1HiaaRHeTvgKFrhICiN3CysW5Mi1fna9AWJSyyJxgFiJkM7stTbRsnlxwOYDeIEgV4FKhXCt6WOx_rnIIkHScEf_pgOCX_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 23:33:12</div>
<hr>

<div class="tg-post" id="msg-139739">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 913 · <a href="https://t.me/SorkhTimes/139739" target="_blank">📅 23:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139738">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
تارتار سرمربی پرسولیس: هوادار دوست دارد تیمش هجومی بازی کند/ قبلا هم گفتم اینجا پرسپولیس است و هواداران بازی زیبا و هجومی را دوست دارند
✔️
✔️
واقعا یک تیم کامل داریم و بازیکنان دارند روز به روز بهتر می شوند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/139738" target="_blank">📅 23:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139737">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/139737" target="_blank">📅 23:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139736">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
علی علیپور : به هواداران عزیزمون این برد رو تبریک میگم و گلم رو به علی آقای پروین تقدیم میکنم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/139736" target="_blank">📅 23:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139735">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
🎙
⚽
🇮🇷
عادل فردوسی‌پور: وقتی به پرونده حواشی دیدار تراکتور-گل‌گهر نگاه میکنم آدم عارش میاد بگه به فوتبال علاقه‌منده! این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/139735" target="_blank">📅 22:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139734">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 608 · <a href="https://t.me/SorkhTimes/139734" target="_blank">📅 22:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139733">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zcc0rkt4lKFJroMkG-MqeIRyDp6ApjABifMqTATY0bdYu_JeXojBMuVOknXONJXyknQDNes_t3Eaj8_I0w6tVmYpCEs6HzgeCY6qf37xXFFx_Ixosc9y8aJtgA_Tk9B2wWWsPLe5_ngYAG7R742SawRqLvFg0Rdr5gjGoI9KeaIBMTb9ovU7tRggeG6Lx4TEiTYSpuSAMMPPaDb-NjXCqU7yNH4MU20_5E6KK4jQoAwypZ6WQi-NkYtlO157qX8HLgJ3UGamsoTbmDwCWZ3_JjJrSuR_G4OvnEcjd1-XGPXIkvm1ZO_ziDT0QFwvcEZtt5W8tizPKB2Q9B_QcNB7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج هفته ششم و جدول لیگ برتر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SorkhTimes/139733" target="_blank">📅 22:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139732">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: ما پیگیر شکایت از یاسر آسانی هستیم و برای اینکه پرونده را به دادگاه CAS ببریم ابتدا باید در کمیته انضباطی شکایت کنیم و جواب بگیریم بعد به CAS ببریم
✔️
بعضی ها می گفتند ما اورونوف را بازی نمی دهیم که او را  بفروشیم/ واقعا خنده دار است چرا باید…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/139732" target="_blank">📅 22:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139731">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
علی علیپور : به هواداران عزیزمون این برد رو تبریک میگم و گلم رو به علی آقای پروین تقدیم میکنم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SorkhTimes/139731" target="_blank">📅 22:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139730">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/139730" target="_blank">📅 22:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139729">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
گل اول پرسپولیس به ذوب آهن توسط علی علیپور
🔥
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/139729" target="_blank">📅 22:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139728">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
تارتار: فشارها علیه پرسپولیس؟ هواداران ما امسال اتحاد خوبی دارند و تا زمانی که این اتحاد باشد ما آسیب نمی‌بینیم
✔️
✔️
کری‌خوانی نماینده‌های تبریز؟ فوتبال از سیاست جدا هست و درباره فوتبال، فوتبالی‌ها باید نظر بدهند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/139728" target="_blank">📅 21:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139727">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
تارتار: در روزی که خوب نبودیم بردیم
❌
❌
سرمربی پرسپولیس در روزی که خیلی خوب نبودیم اما بازی را با پیروزی پشت سرگذاشتیم/ چمن ورزشگاه شهر قدس خیلی خوب نبود امیدوارم این چمن را درست کنند چون امروز واقعا خوب نبود
❌
❌
واقعا جای سوال دارد که چرا کیفیت چمن افت کرده…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/139727" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139726">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
کنایه حدادی به خداداد عزیزی : در این خصوص نمی توانم حرف بزنم اما فقط به آقای خلیلی جنگجوی و با ادب خودمان خسته نباشید می گویم. این نتایجی که می گیریم او هم تاثیر گذار است و در کنار خط در نهایت ادب با جنگندگی حق تیم را پیگیری می کند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/139726" target="_blank">📅 21:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139725">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: دنیل گرا با باشگاه قرارداد داره و  بازیکن ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/139725" target="_blank">📅 21:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139723">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/139723" target="_blank">📅 21:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139722">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
شادی بازیکنان پرسپولیس با هواداران پس از پیروزی برابر ذوب‌آهن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/139722" target="_blank">📅 21:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139721">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/139721" target="_blank">📅 21:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139720">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/139720" target="_blank">📅 21:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139719">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS_6DB41fCwqithmIQjT9YYQwU1O-SPOpta8o4GU6jAWQTBIbn4m7v-0VgyfnsDH0ryWdSnJsl02nFt0kIrSoMrtknzS6M8ULNfFhJxLQjVqjHGcjcnWBWYDkyLnCLGg-nKq3M1eS0G47G4mOLCgyRyTHF-gHzOk5Spz_ofCdqPkbLkiZaFlOeO5InPLM81pJjUqiuJlRys13ntem8zESsrP3HPrnfJN1hW4K-gx130lTOYoTgolXWMO_2uqpKYFP25PE9zKGO29FzGQXosJKfXMmm9J21_NZujdmQmxcdYMN2T4cYzhYVVaT9pAeX1OgzxJaZ20mwwsGtOgnA2KtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
علیپور تاثیرگذارترین بازیکن کل لیگ تا هفته ششم
✔️
6 بازی، 3 گل، 3 پاس گل
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/139719" target="_blank">📅 21:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139718">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/139718" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139717">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/139717" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139716">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
باز هم تعویض تارتار جواب داد ..گل دوم و شهر آبادی زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/139716" target="_blank">📅 20:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139715">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
باز هم تعویض تارتار جواب داد ..گل دوم و شهر آبادی زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/139715" target="_blank">📅 20:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139714">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
گل اول و توسط علیپور زدیم با اینکه نیمه اول خوب نبودیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/139714" target="_blank">📅 20:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139713">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
اعلام رای تراکتور و گل گهر؛
🚨
خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/139713" target="_blank">📅 20:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139712">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
اعلام رای تراکتور و گل گهر؛
🚨
خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/139712" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139711">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/139711" target="_blank">📅 20:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139709">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
این بازی و بچه ها با سه امتیاز بازی و ترک کنن برای بازی بعدی بعد از مدت ها یک هفته تایم و استراحت داریم ...و بازی بعدی یکشنبه هفته بعدی با خیبره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/139709" target="_blank">📅 20:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139708">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
تیم خسته اس ..ساق بچه ها خستگی داره ..امیدوارم نیمه دوم با آوردن صادقی و بیفوما و محمودی بتونیم از این خستگی رها بشیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/139708" target="_blank">📅 19:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139707">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
واقعا چهار روز چهار روز بازی کردن تیم و بچه هارو خسته کرده و واقعا تو ساق بچه ها خستگی واضحه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/139707" target="_blank">📅 19:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139706">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/139706" target="_blank">📅 19:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139705">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/139705" target="_blank">📅 19:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139704">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
واقعا چهار روز چهار روز بازی کردن تیم و بچه هارو خسته کرده و واقعا تو ساق بچه ها خستگی واضحه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/139704" target="_blank">📅 19:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139703">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
تازه میفهمیم که چرا ارونوف و روی نیمکت می‌ذاشت تارتار ‌..واقعا آماده نیست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/139703" target="_blank">📅 19:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139702">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
بریم برای بازی شش امتیازی ..امیدوارم مثل بازی های گذشته از دیدن فوتبال پرسپولیس لذت ببریم ...الهی به امید توووووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/139702" target="_blank">📅 19:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139701">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoF0j0WAqI0XxEmv47aDTyiw1rCdoxlJaIXwab45EQp6Ww4wUgq4VkTN-iRbiWzX5Y1qM38ou-1-dOe24RkwQng6LVVorNgpVwB00aF85IUKT4roygyAL6bAmON2FQIRWNPiB2SiDwr3tqMJ-SwhIRLVGXXmtmxWP_s4kfFU3xXxuJm7MQgdJDHIi6NCRGNKDVrZv708yE3JFxW8I-J7yfEcjU7mMdmPmtkScPh7N7pQsKFeoCN1EMPXvND7H0aznuZ4YJp5csNZWi7XOFmF7Xct-M1vs__IyUxHH1NbVxj0M_IC6ai9G6I_FhAjzr_3MB5agc3zO2mTPblwGcUQqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/139701" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139700">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/139700" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139699">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
هوادار پرسپولیس درباره جنجال امید عالیشاه و خداداد عزیزی
❌
❌
آقای خداداد عزیزی به قول سیدجلال ما پرسپولیسی‌ها هیچ چیزی از یادمان نمی‌رود. خدا نکند که ما پرسپولیسی‌ها با تو رودررو شویم؛ می‌توانی از بیرانوند بپرسی. مثل خودت با تو رفتار می‌کنیم. کل افتخارات…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/139699" target="_blank">📅 18:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139698">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
✔️
صحبت‌های هوادار پرسپولیس درباره اتفاقات بازی تراکتور- گل گهر و حواشی ایجاد شده میان عالیشاه و خداداد عزیزی!
❌
❌
از کمیته انضباطی سخت می‌خواهیم برای یک بار هم که شده رای درست بدهد.‌امروز نشان می‌دهیم که هیچ کسی حق توهین به عالیشاه را ندارد. امید عالیشاه…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/139698" target="_blank">📅 18:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139697">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/139697" target="_blank">📅 18:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139696">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
ترکیب بازی امروز همینه و تایید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/139696" target="_blank">📅 18:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139695">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=Fb230rFfJIZOGYYuEk3OU6U-smLbE_GXT0LhVx6kl88hT-6iGfR_aArr_qZXXOJ748e-8Cx17ThXSMI9EoHiKZrqLnWHSf2QqyRaNRuHQGb0w5-2StPkwqPflRwcSuvtTTEZzVkaS9ny0gi_wdKwUEIJN6azVjxOY9WIHOZNbt5sLnl2bsAeLYJsI5SWEKYkaF-4i6wValtNJQwlTEkXYFUj_TCmqHC4J_YomH7MkRMRNBgxbDiuSeHA3_sRL05flUY9zRkH2PZ-8nSpS0tp5Ey9g51O__IB3wZm96uX-iTb_mf3Qv9F7yNWpTiKeu_INL6_Vsbes8R3o1gFIB8pGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=Fb230rFfJIZOGYYuEk3OU6U-smLbE_GXT0LhVx6kl88hT-6iGfR_aArr_qZXXOJ748e-8Cx17ThXSMI9EoHiKZrqLnWHSf2QqyRaNRuHQGb0w5-2StPkwqPflRwcSuvtTTEZzVkaS9ny0gi_wdKwUEIJN6azVjxOY9WIHOZNbt5sLnl2bsAeLYJsI5SWEKYkaF-4i6wValtNJQwlTEkXYFUj_TCmqHC4J_YomH7MkRMRNBgxbDiuSeHA3_sRL05flUY9zRkH2PZ-8nSpS0tp5Ey9g51O__IB3wZm96uX-iTb_mf3Qv9F7yNWpTiKeu_INL6_Vsbes8R3o1gFIB8pGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/139695" target="_blank">📅 18:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139694">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/139694" target="_blank">📅 18:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139693">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/139693" target="_blank">📅 18:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139692">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9B8TRH4oncpeWZom6gQuMewAuRcT3f_lnvLyG4VpobOgXI3lIQxtdgDBW1IQ8flcrcqSnc7k3a45b0WovAC9LI0spljfssw1ytBsGhZy-CZWC7lTmrrm8nZFv15LoxGdZa6YQA8P88zuS4OgCrK4zOgctveiPhOy0wWquHI6Iu7kgaWd5M5qML2QZalIGylYQByGPWf-QKKj0ClBw4C4Jlb7iFPcKigWvCGTnfMM1z77xCDailHW8uYpi1eDkzAuMPGczBXcODOuuVLNWJ26J4xCvdyromkdVTIxvJ7EuHnp21nIl14JFTUPEpHOk9MXFSgEOhvZMPoGchU6CLYIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/139692" target="_blank">📅 18:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139691">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/139691" target="_blank">📅 17:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139690">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7939cefa83.mp4?token=GSoGm9uOtzndYsgH1fHq11zapWLEr5q09Y8uK6TsxO8yKzfqUDYhphsqp4YcbChDFxSA7APm7VEY3VvHDYsMasXyz98-vVniVwRvl-QFjpI7dno-0CLQCYQwbcwtHjTHAdqtC5-vR3C4lmEwecxvHtulu_MkPSVdbKCph_7mVeU-1tQlOrvW7gNgKWHnXZ9pInhjEYJ0BZN1oOVHd1UaPb_pn0I2-am96fHM9j9DCHFelbdZXAYlMaDhEjHUax_4X35IvkFJmSp-gnMVHG32sgIcsmVx2B3uctGBU_uMe7dNcwwMcfaaQnE0IFgjyxN7sMjYLRuzTuVLdpMHk5s3hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7939cefa83.mp4?token=GSoGm9uOtzndYsgH1fHq11zapWLEr5q09Y8uK6TsxO8yKzfqUDYhphsqp4YcbChDFxSA7APm7VEY3VvHDYsMasXyz98-vVniVwRvl-QFjpI7dno-0CLQCYQwbcwtHjTHAdqtC5-vR3C4lmEwecxvHtulu_MkPSVdbKCph_7mVeU-1tQlOrvW7gNgKWHnXZ9pInhjEYJ0BZN1oOVHd1UaPb_pn0I2-am96fHM9j9DCHFelbdZXAYlMaDhEjHUax_4X35IvkFJmSp-gnMVHG32sgIcsmVx2B3uctGBU_uMe7dNcwwMcfaaQnE0IFgjyxN7sMjYLRuzTuVLdpMHk5s3hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📌
هوادار پرسپولیس:
✔️
ورزشگاه آزادی درست بود، بی‌افتخار ترین تیم لیگ (تراکتور) عمرا قهرمان نمی‌شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/139690" target="_blank">📅 17:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139689">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8432a81f4.mp4?token=Rf3WJeR5Qu0jTYlugPflTs7qLitXfg14m_4bxjOgRHjzp3-5pPRkeqw30E_DiJqqrhrbxKAn4M4FgxVZsRcg6_vJgS7OTtwvBfTGoA_0tKAZzlL7hRmZR8DnSBdA9K_AIA_jwXkZfuvd4fWBdBFgXvSozrHJU8S4kWSzgiSLvG8ti5gYixLl-TSzlufF86YJUzCO2pYjHfH89Qr1_lj54wbDCnNbFqbDO2yoOuy3SaQmWmCPWPRiPedCU0HYhIXT6CGYOgQXTw2fzpLw1CEuNadnL0-Xnjq0UU4Zt93x4X6AJgjuZkxhnZzHxTfpOdLlwVbIWpVh_gHtEI3ln4c7uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8432a81f4.mp4?token=Rf3WJeR5Qu0jTYlugPflTs7qLitXfg14m_4bxjOgRHjzp3-5pPRkeqw30E_DiJqqrhrbxKAn4M4FgxVZsRcg6_vJgS7OTtwvBfTGoA_0tKAZzlL7hRmZR8DnSBdA9K_AIA_jwXkZfuvd4fWBdBFgXvSozrHJU8S4kWSzgiSLvG8ti5gYixLl-TSzlufF86YJUzCO2pYjHfH89Qr1_lj54wbDCnNbFqbDO2yoOuy3SaQmWmCPWPRiPedCU0HYhIXT6CGYOgQXTw2fzpLw1CEuNadnL0-Xnjq0UU4Zt93x4X6AJgjuZkxhnZzHxTfpOdLlwVbIWpVh_gHtEI3ln4c7uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
بانوان پرسپولیسی و تشویق امید عالیشاه در شهرقدس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/139689" target="_blank">📅 17:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139688">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpAjM3La6BXw_Lf86pC9uQmzv9dmcA8NaVB0rbWrWE3XysRen_ACNFhHiQckWW_M1HzGKRsGm1J3-olxrvk0X8-k9CrMoaOhXiIFFSFZR-a36gGxmtKp5J_wG_KnMXHR5l-C5HhidLOW9c76F5J7y3Ga3Wxt3PgUsanj1GBThZ7W7B1H7LLCzapG45gRCHPnrU7d4uw_0chTz0tTiLCp45gUAOqvh8YXspI2XmWdRx3DpbMHY53RQpfsIuz4-1i72sY4oTBtgPp72vk6lSsvICDA4hhOhufvULBQK6qXIl_Xv6T79Q9JgnRBipnEW3Rj0wwMCBmH1Za_aJ6lk1-Nrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/139688" target="_blank">📅 17:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139687">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oocBEO6d8Z2b30dr0k3_1mGnh1uZEJ3mX46BQxfbK6Z7X0tlSSlSkZHmNBbtelC9ANDuuHBo-ttsn89Xf78vP7liMAWgye0jQ1JIZTIN1b1vB4ITR223vXa6xvBSkHbY7Y9rUMld9cJhbKasvXIazBkfqWPysxdkBChjzIEa6WR5YxJJmz3oQyRSzgXEVL-b3jBPxZ2mTbWV0Vxi2FIWrwBnqmcu1ZJi7OYZExwPt9TQU1QExThQBq6ASCxI-AeySEnfSjPSep0mFybag6d3GfXBIU24I_ZhAUa6wixlDSIxtTgKkYO5ASpaOke8vGXSgHYNo1BJc7h3OkZZU9gjaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
هوادارا دم در ورزشگاه شهرقدس
😂
🗣
ورود بدون کارت ملی ممنوع!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/139687" target="_blank">📅 17:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139686">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
گفته میشه که ویسی از که از خداداد عزیزی پخش شده فقط بخشی از فحاشیش به امید عالیشاه بازیکن گل‌گهر بوده و بخش زیادی از فحش ها و صحبت ها پخش نشده و قرار است به دادگاه ارائه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/139686" target="_blank">📅 17:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139685">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/139685" target="_blank">📅 16:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139684">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/139684" target="_blank">📅 16:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139683">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/139683" target="_blank">📅 16:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139682">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ut4v6mEU16Pi-gNZeRgOVLqZrGvfRrDqGuO2Pdbv13N6Xz2aJeC_P4h32oGi9E2uJjRsNHrpHwxo-pxD5SdXsfQNEibl7QEuZYtJWKAfaBYGTzURt36fNZpdpAGZXxiES1E27rkFF3Vsw7_gMHKRcB1QgeKCfzL8PFxVHkpC33bTASBGwCSpjZJzVYCFPqQ3fjc7pzRARHumolbqI9PUM4WS6-SoOXkvwTvJSotX1PhNERS91VVK3_Xy2nbHUaSnQ2ZMOiQ3c4QTeR7kPqHYhZWoP5x4yNezyQhhVn5ftZrynDAbBATpApfypXrX7XMrqRMrZ4L20FB_n-fuZEQiWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139682" target="_blank">📅 15:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139681">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❤️
🎉
تولدت مبارک پسر متعصب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139681" target="_blank">📅 15:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139680">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139680" target="_blank">📅 13:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139679">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQWFS5e_O0MHroX94zkF5Eq3I-AhmzE0jYXURacqZxofMf5hixFQTcFwBHNx7V00Vqg_NeRMPe28QcjYa5FccLfEH_AidUdbTKkgjPO4Gpg-y2SD9DLECgLvIvB5lGv5zHLwS_yOa-UBoLC2XzplwP05pILNW5cT_IvXm3Pee5VJiyfHDCn-qILpuKyKfIdXoaQHadhIzp-Xv1Y6RcQdUhFXFMA5jyNUpaHqdHaLFgJXLUxfo5hcS730R1RmTzhq9kGp2apYD_yQPZmelsx0t9pb8e2WrSPPB7vFv-38p9ld2ZvOrti6IwDDFDDTJydXGtvYR-aFj-Ih9aPicH2_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عضو پنجم هیئت مدیره پرسپولیس مشخص شد.
✔️
به نظر می‌رسد روند انتخاب عضو پنجم هیئت مدیره باشگاه پرسپولیس به مراحل پایانی رسیده و حسین صابری خورگو به عنوان عضو جدید این هیئت معرفی خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139679" target="_blank">📅 13:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139678">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139678" target="_blank">📅 12:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139677">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
درپی‌اتفاقات‌دیشب؛ به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/139677" target="_blank">📅 10:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139676">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
#فوری؛ بعداز حرفای‌ دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌ سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌ تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌ اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139676" target="_blank">📅 10:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139675">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
طاهرخانی ادعا می‌کنه پنجره نقل انتقالاتی کیسه تا آخر تابستون ۱۴۰۶ بسته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139675" target="_blank">📅 08:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139674">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❤️
صبح روزی که بازی داریم و شش امتیازیه بخیر
❤️
❤️
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139674" target="_blank">📅 08:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139673">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/139673" target="_blank">📅 01:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139672">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/139672" target="_blank">📅 00:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139671">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/139671" target="_blank">📅 00:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139670">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/139670" target="_blank">📅 00:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139669">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/139669" target="_blank">📅 00:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139668">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd7cdc1c0.mp4?token=rfETVhxXPpVc0INSrFmXkwqDFVsv28Fal00p4nv56SYzaPoQT-1qtITNJdX7U0CrIr7q6XWOZ78RVrdhLg4kW1GJIBFo5oSgnqybeqeMLxJoU-ZPKc8L4ESqUGb6ftwwdrljjNuEv_h5311O_Gx_w4XSOfCq4ln1ujlprtyprUn3z9MxPPbK7fesAX_yDoLpnw4hirmyeVaVYIF1wM945kNUqsUOoGuPqSJFIinDq8pNAwr2qs92RJvSk2CDY9hQJRt6Z8yYdwDEp_rq8usUHVpJY5zW65g-GIfnjKSK-_I11_T94xs_eZ82j8ep1bZMxz7yIkbriFpg1uGnXxDU3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd7cdc1c0.mp4?token=rfETVhxXPpVc0INSrFmXkwqDFVsv28Fal00p4nv56SYzaPoQT-1qtITNJdX7U0CrIr7q6XWOZ78RVrdhLg4kW1GJIBFo5oSgnqybeqeMLxJoU-ZPKc8L4ESqUGb6ftwwdrljjNuEv_h5311O_Gx_w4XSOfCq4ln1ujlprtyprUn3z9MxPPbK7fesAX_yDoLpnw4hirmyeVaVYIF1wM945kNUqsUOoGuPqSJFIinDq8pNAwr2qs92RJvSk2CDY9hQJRt6Z8yYdwDEp_rq8usUHVpJY5zW65g-GIfnjKSK-_I11_T94xs_eZ82j8ep1bZMxz7yIkbriFpg1uGnXxDU3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139668" target="_blank">📅 23:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139667">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxVwx5WiPlvXbGfTK7KECgXpvIbTs1QjAHzbZsqmnODcR6DU0I2C2fb501FmPnChPlNSKrluKAXlJ0eT9rG4H7EL_BM3b2jEdQn_LBuA5aABZIXfwLzcY93qgcTU2XfU5AHxFHq73k1KFnjvmvoLZjrdTBED7CRnC12pVC1xOOPnvXCWUxAA0sXE2lcAlYJE8Hymes6JZ9t09apY-qjKVtdZMmjARRtLwiqCV1MxokL8uVYF0Cc16-RrGcb0U1RY2cPYVsn3QEM9oLGPZqV-eLDVrKMJK3Wnq2cT1_0-gKxokWdS0XmZWAzwNKFBSHoVeaL93Njyhhayp806W_YN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اگه فردا ببریم با ۱۳ امتیاز میریم دوم جدول
❌
❌
فوق العاده مهمه ۳ امتیاز بازی فردا</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139667" target="_blank">📅 23:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139666">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🗣
🗣
فوتبالی: اورونوف فیکسه تو بازی فردا
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139666" target="_blank">📅 23:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139665">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
تارتار: باید با خداداد عزیزی برخورد شدیدی بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/139665" target="_blank">📅 23:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139664">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139664" target="_blank">📅 23:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139663">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139663" target="_blank">📅 23:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139662">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139662" target="_blank">📅 22:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139661">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/139661" target="_blank">📅 22:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139660">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139660" target="_blank">📅 22:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139659">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139659" target="_blank">📅 21:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139658">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/139658" target="_blank">📅 21:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139657">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت، در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/139657" target="_blank">📅 21:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139656">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139656" target="_blank">📅 21:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139655">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
نایب‌رئیس مجلس اعلام کرد: سهمیه ۶۰ لیتری بنزین با نرخ ۱۵۰۰ تومان حفظ می‌شود، سهمیه ۳۰۰۰ تومانی از ۷۰ به ۵۰ لیتر و سهمیه ۵۰۰۰ تومانی از ۳۰ به ۱۵ لیتر کاهش خواهد یافت؛ نرخ چهارم بنزین هنوز نهایی نشده است
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/139655" target="_blank">📅 21:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139654">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4doI4wbt0QDB4Uyu_NPP5jBO8_3yFDJr-v57LZ2yAVDu7aoZQ5qlYIcFH_tr8Z29BGq8eJC997pnDFSpcBFCa8jnC4dG4lYc_eo7Qu5qghFwbjirW11qvmchWpzion7rBgAjNb16EnmZNwwveLXmYX9t_UUcBkOW9anhqZIbpb7y7TyCAg_RA5kRpJuPN5lPpImV5WA54RnM1OSuZ6rerIoYykNzjRmgGtJjPy2m73yEBP0Bu8-lxMBaSg7Wh9zb_8gAivd23DAotYxvTU9Y9lVMT0eFDpHup2sFI7U0iOHN5_1-yPMam7XbiYZWMjcxrrfAMTNZI7LWkFmpQIDBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
تصاویری از تمرین امروز تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139654" target="_blank">📅 21:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139653">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYefcY820f5GBdHi1m0dw9o6SODZ9YK1kftic1M2aExkG0ZZP0ttY2S1ddylcjW-SdqBTELnhgR--Lxs03JWKjimcrgtNOlhunW4y6hIoob7lwXtqy1sX3a4GvLF1dylYdIB39TBLoCW-XOa0nQkkeaK_KnLDX66g1OmH4Ry5QpNdkiTqZ-h_F318MRKyC7tZOVqHLLlHii3C2EB1bpd5QYK6I-Mhhshx-dIpqN1Wrs5b51Zmg1iJnifWyobOg5frwjw0UBKTSbn8D0MLoOU5FbrC5IEmEB3_0_Rz1NuXHVGAA4HnR96nIjBDuwYfkvLDwwTtQMGGhkdrtIsg7jABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
جدول لیگ پس از پایان بازی‌های امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139653" target="_blank">📅 21:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139652">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
✔️
بازی کیسه هم مساوی تموم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139652" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139651">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🗣
تا دقیقه 70 کیسه و آلمینیوم صفر صفر مساوی هستند ..و بهترین نتیجه برای پرسپولیس همین مساوی هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139651" target="_blank">📅 21:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139650">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🗣
🗣
فوتبالی: اورونوف فیکسه تو بازی فردا
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139650" target="_blank">📅 20:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139649">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
ابوالفضل جلالی در ترکیب فیکس پرسپولیس مقابل ذوب آهن قرار گرفت و تیکدری کار را از روی نیمکت اغاز خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139649" target="_blank">📅 20:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139648">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub4Dr3MRh67VPxT2LLvM7wmlqlLFoFL-2DMdqKcfLhlXtKqyG4Et7pCDookP-oOaSVzoT9hY975RHNZiUCbyH9Ib4PZHUuGDrag3M-6exNRNS4m7XKFQkIiPDuRLN8euO9aSkk3zkVkR1BdZ76drj7Qxkiv_KQXuT6AtPT1X5Hh1Vvi6p3pCGoQVXf2FuKXpM9YWJYILu4-EagcKMbETI1yxBmZLlpZy5o7QV5yqaegeAxUxKwEEa_kWDGqsA-2xCFxaZKUcKJU44uNDg6lu_RS9vBknSJqgGYU4bKZ-VXlw36QMxhM01mrBGsft-wHS91nWt6Ccmasxx8t204xHLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حلقه اتحاد بازیکنا تو تمرین امروز
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139648" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139647">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139647" target="_blank">📅 20:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139646">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
حضور ابوالفضل جلالی در بازی امروز  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139646" target="_blank">📅 20:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139645">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi6v1NEWeRQJDRqcMigDWhMlN-6juQSc4lKRzdiovueb5YACy-wXfagQcdWz_P2h-uJ9BqMV3l3QxT8MfxTcFSCaKgYaLLCQhfEl89Sq6mBDxvrxCFWeeiY4oxlSJQdQ9ckhZ4EDm6tzI6fEtNJG9xD2FB5WeC7csq7w1K2srfGhFbtVCXn-57gQC5FfJ4t7QxdhML9SxK5vz76VSFKjp5cSJNC2c-klFpdsxiwmrOR1_KQZ2j0t5e0fEmQDZ384bhvlJglMXPlMTFSVBnfCJngTqo9zWAdWIIU3Ptrqa15xgu3-uMK73BTu40WVjFlVVTohABhHu1dW2yrK1EhQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
کلاسیک ایتالیایی در راه است!
یوونتوس و میلان؛ جایی که یک اشتباه، بهای سنگینی در تورین دارد.
⚪️
Juventus -
🔴
Milan
⏰
Tonight 22:15
🏟
Allianz Stadium
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
⚽️
یووه یا میلان؟ امشب فقط یک تیم می‌تواند سربلند از زمین بیرون بیاد.
🟣
[
برای ورود به سایت کلیک کنید:
]
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139645" target="_blank">📅 20:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139644">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
✔️
✔️
مهدی تارتار: کاش میتونستم ۲۲ بازیکن بزارم تو زمین اما این برام چالش شیرینیه/هم بیفوما و اوستون و هم عمری و محبی رقابت شدیدی با هم دارن/بازی با ذوب‌آهن برامون از دربی مهمتره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139644" target="_blank">📅 17:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139643">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: اگه همه‌ی باشگاها اجازه بدن ما هم میزاریم بازیکنامون برن تیم ملی امید/منم دوست دارم اونا پیشرفت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139643" target="_blank">📅 17:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139642">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139642" target="_blank">📅 17:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139641">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار:
✔️
بازی بسیار مهمی با تیم با تجربه و با کیفیتی داریم. ذوب آهن کادرفنی و شجاعی دارد
🗣
تیم های ویسی فوتبال جسورانه بازی می‌کنند. با توجه به اینکه هفته قبل دو امتیاز از دست دادیم محکوم به بردن هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139641" target="_blank">📅 17:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139640">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
واکنش عبدالله ویسی به اظهارات رکیک خداداد عزیزی: واقعا خجالت می‌کشم در این مورد صحبت کنم/ تویی که فحش می‌دهی! شما خودت ناموس داری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139640" target="_blank">📅 17:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139639">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
تارتار: ما با پرس سنگینی که انجام میدهیم طبیعی است که نیمه دوم تحلیل برویم تمام شاخص ها نشان میدهد که در این چند هفته پیشرفت کردیم
✅
✅
شده سه روز به سه روز بازی کنیم باید جام حذفی برگزار شود
✔️
✔️
بیفوما و دعوت به تیم ملی؟ او خودش هم خواست که تغییر کند…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139639" target="_blank">📅 16:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139638">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار:
✔️
بازی بسیار مهمی با تیم با تجربه و با کیفیتی داریم. ذوب آهن کادرفنی و شجاعی دارد
🗣
تیم های ویسی فوتبال جسورانه بازی می‌کنند. با توجه به اینکه هفته قبل دو امتیاز از دست دادیم محکوم به بردن هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139638" target="_blank">📅 16:50 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
