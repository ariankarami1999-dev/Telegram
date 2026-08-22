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
<img src="https://cdn4.telesco.pe/file/FfpQrAIZoP3Qyvn-P6PUnwq_7uPmaiAvH_TfbLkzZj3JcdtXVItcW7EIAP5sFiAQDvYlWgUNgyEdUdyQ3pZgumzy0flyASuqRiMYVE9L_FMTZm_njZ1KIpEmcGNbMQ4PDCdVxI4W1D6ptDuRVTJDSXStNbAwABwnYBXkTPsjUBkfk9sDnAiQO51x-sqZ8nzEUYRc7cYooVJs-tBGY6JhzS5IUvk9yo4KdyDFRw3cg-91xRd4w8DzGbN6SsLMQWw_aEvDR4paRnmHLDcjnlpugAvss_CCiTMxtZvE9E4hLpQK8J0Imvyzmxi2O7Qx85S48K_rod3JcRD3pCkYPGtvTQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 13:43:44</div>
<hr>

<div class="tg-post" id="msg-138764">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔻
🔻
🔻
میثاقی: احتمال داره حسین زاده و بیرانوند به همراه تیم ملی امید راهی بازیای ناگویا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/138764" target="_blank">📅 13:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138763">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
بخش رسانه‌ای تیم ملی: مسدود شدن سایت و برنامه فوتبال 360 عادل فردوسی پور هیچ ارتباطی به سرمربی تیم ملی ندارد و ایشان نه شکایتی کرده نه هیچ عملی انجام داده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/138763" target="_blank">📅 12:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138762">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
قدوسی: علیرضا بیرانوند گفته نه تنها سربازی نمیرم بلکه نیم فصل با استقلال برای فصل آینده قرارداد میبندم
😀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/138762" target="_blank">📅 12:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138761">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdZUWpn8Mw3abChG2tFppAvnZ897QaoFOuhvZN9qU3OXF4icsuFwXHhyXaJY1tmClpbo9KCRA1o0TRQezosLjEy0iV1NuesGxMu0cI8a9S6sM-8VfwCi-RNuzBVEOEYxQRIngy0pNTKHF7PfcYf9xCaWSipvqDTC4TtzCMQVFCc1RncF_eQe4gBJhL7xDsi2zTF5MKepTvUt1gn2Vp8gKd434BVFFjF6pxDpUHSegXyqzRlLAdquOsTbY7I2ILOnBUQKHEHAKjbuq-ES4XentJgmWGL2-Lu__mkqInjS-wtCYbonDCHkPJB958EVvHoLL4S7GIX1gMSX-gCMo4i7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نبرد غول‌ها برای اولین جام فصل!
دورتموند در خانه مقابل بایرن؛
- امشب کدام تیم جام را بالای سر می‌برد؟
وقتشه پیش‌بینی‌تو ثبت کنی!
⚽️
فینال سوپرکاپ آلمان
[
دورتموند
⚽️
🆚
⚽️
بایرن‌مونیخ
]
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SorkhTimes/138761" target="_blank">📅 12:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138760">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e244643a2.mp4?token=oO5bNkd6MWu6e5zBRAnAEvpsn2PFzPLdLINioVVPH7qg5ZXZJyU2GRK7cMIiitN_Ac6u0YoWesiGMylZwmSQpWwpz6bjCuRjLUO5DWXwjKxmXfuifHar_pQEADJ0woCJhaAva6mmDOoMfNmECIiOywd_reg8bYulvAfIbDNBXNOoAgOnUJ0y1yiN3MqL3SgbhkzMgzary3W_1bFmNdL8CApdwz0ksLjqKTNYBtIue61tEjRtLCv6U0S4HGVguzoo5s00bB7Ja6ey4EaamCRtnHl91c9z-JWNmEgu2ZozbMewgCZE93f4qfDytmSRNYxxfwuH5w7-xHFJ4HQqDEGxYqYYHR7BIkboADg0ErqSdfqjCPLqbCQrTDUbqWrC0ldTVHgUhVYReDz2cTcLfEjbVOYaOHMVEN3UMsuLBXgZr7PJ4wDhZ3qnuYJb7B5ETOhRUnvgvMj2Lnh-Un6kG29exiBaPshncXI_xgCRNAgvb25JavMCCjA4fS4CFDhiquWszTxY5_5-sExrZlDJjQ4qBrR1biZxbyOK9vRVbMZctuAxMe6ivP1VPSnfdVp25iwkSvsBIYWP2y8vUuKgaxWf1Jn4Zy2HxOqPciKaBgPph2iGE6J9SLW6LTORfCTKgAZOhQj74KK5mwbuQVJaFXvRWeFWbUcZzz3iRHotRDWX0hY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e244643a2.mp4?token=oO5bNkd6MWu6e5zBRAnAEvpsn2PFzPLdLINioVVPH7qg5ZXZJyU2GRK7cMIiitN_Ac6u0YoWesiGMylZwmSQpWwpz6bjCuRjLUO5DWXwjKxmXfuifHar_pQEADJ0woCJhaAva6mmDOoMfNmECIiOywd_reg8bYulvAfIbDNBXNOoAgOnUJ0y1yiN3MqL3SgbhkzMgzary3W_1bFmNdL8CApdwz0ksLjqKTNYBtIue61tEjRtLCv6U0S4HGVguzoo5s00bB7Ja6ey4EaamCRtnHl91c9z-JWNmEgu2ZozbMewgCZE93f4qfDytmSRNYxxfwuH5w7-xHFJ4HQqDEGxYqYYHR7BIkboADg0ErqSdfqjCPLqbCQrTDUbqWrC0ldTVHgUhVYReDz2cTcLfEjbVOYaOHMVEN3UMsuLBXgZr7PJ4wDhZ3qnuYJb7B5ETOhRUnvgvMj2Lnh-Un6kG29exiBaPshncXI_xgCRNAgvb25JavMCCjA4fS4CFDhiquWszTxY5_5-sExrZlDJjQ4qBrR1biZxbyOK9vRVbMZctuAxMe6ivP1VPSnfdVp25iwkSvsBIYWP2y8vUuKgaxWf1Jn4Zy2HxOqPciKaBgPph2iGE6J9SLW6LTORfCTKgAZOhQj74KK5mwbuQVJaFXvRWeFWbUcZzz3iRHotRDWX0hY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
حضور پرسپولیس در مرکز پزشکی و فیزیوتراپی فدراسیون کشتی
✔️
بازیکنان تیم فوتبال پرسپولیس پس از دیدار برابر استقلال خوزستان، با حضور در مرکز پزشکی ورزشی و فیزیوتراپی کمپ تیم‌های ملی کشتی، به ریکاوری پرداختند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/138760" target="_blank">📅 11:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138759">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
در صورتی که انتقال ابوالفضل رزاق پور به پرسپولیس کنسل بشه، امیر جعفری گزینه بعدی دفاع چپ خواهد بود / تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/138759" target="_blank">📅 11:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138758">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">💢
💢
🚨
مدیران باشگاه الوحده امارات پس از شکست در دیدار امروزشان به دنبال جذب دو بازیکن خارجی جدید هستند و از همین روز از نماینده محمد قربانی دعوت کرده اند فردا برای جدایی و فروش این بازیکن به باشگاه برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/138758" target="_blank">📅 11:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138757">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
❌
آب پاکی فدراسیون فوتبال روی دست تراکتور، پرسپولیس- تراکتور، بدون تماشاگر
✅
✅
عضو کمیته استیناف فدراسیون فوتبال: کمیته استیناف به‌عنوان مرجع نهایی صدور رأی در ارکان قضایی فدراسیون، حکم کمیته انضباطی مبنی بر برگزاری دیدار تراکتور و پرسپولیس بدون حضور هواداران…</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/138757" target="_blank">📅 11:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138756">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
شایعات : تارتار میخواد مقابل تراکتور یه ترکیب سر و پا هجومی بفرسته تو زمین  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/138756" target="_blank">📅 09:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138755">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
حسن اکرمی داور بازی پرسپولیس و استقلال خوزستان شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/138755" target="_blank">📅 09:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138754">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPJSo6h7bFH2XvSkfn4zeDiOICpoS9rhbRpgJC5Uzr3BfoxQMoWdBeAsMD1B4owHFtxPBAU-Ki0i5T0WX20KiGW03mi8d0ZeJMbHAMlbTH4JtPzZgKqXqY6Ns1yJU_7Ot6UenauJHyC9nHEwBlCploN75ukO9yrkb-AY_QD0CHF9q_d_Xc6-71NtYw1Kredue888OElF8p_mqC161OvhwtIhwL0wR94yFqWcM7Z_kuXlqL0NOpy3zcZkqsU98oOQVAtjWDyf3o_Dd8AsgpstyDecZib8p7thustN4XPT6DD-AmvJXl2zEMUTVKbFhtGXonnA8AUSIshSm1m0SdJ54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبح بخیر ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/138754" target="_blank">📅 09:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138753">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">7️⃣
وقت چرخشه! | SCARABTEMPLE
🎰
همین حالا با هر بار شارژ حداقل
۱ میلیون تومان، اسپین رایگان متناسب با مبلغ شارژ
دریافت کن!
💰
شارژ بیشتر؟ اسپین بیشتر!
🎁
هر چرخش، شانس دریافت جوایز نقدی
⚡️
اسپین‌های بیشتر، فرصت‌های بیشتر برای کشف جوایز بازی
😳
👾
اسکرب‌تمپل
، با یک سیستم اسپین پرهیجان و جوایز متنوع:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/138753" target="_blank">📅 01:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138752">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❤️
❤️
❤️
سهیمه خرید لیگ برتری پرسپولیس در نقل و انتقالات
⏺
1_مهدی تیکدری نژاد
⏺
2_سید مجید عیدی
⏺
3_محمد مهدی زارع
⏺
4_سید ابوالفضل جلالی
⏺
5_پویا پورعلی
⏺
6_محمد مهدی محبی
⏺
7_دانیال ایری
⏺
8_ خالی...
🌏
سهیمه بازیکنان آزاد فیفا:
⏺
1_خالی…
⏺
2_خالی…
⏺
3_خالی……</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138752" target="_blank">📅 00:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138751">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
‼️
فووووووووووووری
🚨
ورزش سه: سردار زاهدی بار دیگر در ارتباط با ما اعلام کرد علیرضا بیرانوند سرباز شده و از مهر ماه ( یکماه دیگر ) باید به خدمت مقدس سربازی اعزام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/138751" target="_blank">📅 00:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138750">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
❌
ورزش‌سه:
🔴
الوحده به خاطرات تغییراتی که باید تو لیستش بده تمایل جدی به فروش قربانی داره و بعد باخت امشبش این اتفاق قطعی شده
💣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/138750" target="_blank">📅 00:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138749">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
ترامپ درباره ایران:
🔻
به نظرم این جنگ به‌زودی پایان خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/138749" target="_blank">📅 00:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138748">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
در صورتی که انتقال ابوالفضل رزاق پور به پرسپولیس کنسل بشه، امیر جعفری گزینه بعدی دفاع چپ خواهد بود / تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/138748" target="_blank">📅 00:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138747">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
یکی از سایت های اماراتی گفته قربانی با قراردادی ۱.۱ میلیون دلاری و سه ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138747" target="_blank">📅 00:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138746">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22323c2ffc.mp4?token=B0jNzx29hCIhQ5ZxaFsXPd61k9i-Ba4LGp6z6xUIgqog_VznLkXfwo0SJ-QVVdKQicY-5KIPfQJmQD5Tf9U55wxqcgLE7HFlnXaUEZnOiODmp6zLlachlx37O2QweU9heFiTz7pRp7OveG41INAM2kWiDd87pB-CQC2s9vA6lQftwNyrPui9sMEq_NOnSkmjhhbt_5fqi2PifdXqGyYLAf5AomaCYB97bB2tscRuNWlu3nMEAQGvVObaUO43Zc8cdWssIV5nreccMlrdiuSmfy-nnHYjU0ITPjN4WvB24ZR7kijAWPOMP3q2_vu2HQ8OF2c15lVVpT7I9nMsO-i9yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22323c2ffc.mp4?token=B0jNzx29hCIhQ5ZxaFsXPd61k9i-Ba4LGp6z6xUIgqog_VznLkXfwo0SJ-QVVdKQicY-5KIPfQJmQD5Tf9U55wxqcgLE7HFlnXaUEZnOiODmp6zLlachlx37O2QweU9heFiTz7pRp7OveG41INAM2kWiDd87pB-CQC2s9vA6lQftwNyrPui9sMEq_NOnSkmjhhbt_5fqi2PifdXqGyYLAf5AomaCYB97bB2tscRuNWlu3nMEAQGvVObaUO43Zc8cdWssIV5nreccMlrdiuSmfy-nnHYjU0ITPjN4WvB24ZR7kijAWPOMP3q2_vu2HQ8OF2c15lVVpT7I9nMsO-i9yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
محمد تقوی، در آنالیز فنی بازی پرسپولیس - استقلال خوزستان گفت:
❌
❌
«در فاز حمله، همیشه ۶ بازیکن پرسپولیس شرکت داشتند. اما جدا از شیوه هجومی بازی با توپ پرسپولیس، بازی بدون توپ این تیم، غافلگیرکننده بود.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138746" target="_blank">📅 00:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138745">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRjJKWgf67RSW-w8_yWOCSZD0L2TIceAywcYluYqBFhGYrO0KrnJNS8pCjLgEqhMKHIN5fi-skUZ4vcbakL9FfIWnLri-ZUUjfQpa4cBYp4Ye3jEi2DqIoXyScGQLJ-b5BXEveJy41rQYYEJN1FAxyP-wTWVBTMpqkoibDki6CxiL_CnE52aAZ4E8rda6AfozgfyNNa_w3JOnYw_xU3DbKXhRdIyXHfe0pI_WD0-VBwpO71oGKJlyJNrNzbo6vdeQgj_ognkcZiFdoPqqmZ_bN1PBBG-Aan0qdiyqeEzZR2zOyJ7HAvZH0YXfsd46ZTjWz1bXQ7daFPu7baMmDM-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مهدی تارتار قصد دارد ترکیبی هجومی در بازی پرسپولیس و تراکتور استفاده کند و ممکن است یک سورپرایز هم در این بازی داشته باشد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/138745" target="_blank">📅 23:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138744">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
❌
تسنیم به نقل از سردار زاهدی معاون نظام وظیفه گفته که بیرانوند در لیست تیم امید نیست و از ۱ مهر سرباز میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/138744" target="_blank">📅 23:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138743">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
❌
تسنیم به نقل از سردار زاهدی معاون نظام وظیفه گفته که بیرانوند در لیست تیم امید نیست و از ۱ مهر سرباز میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/138743" target="_blank">📅 23:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138742">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
در صورتی که انتقال ابوالفضل رزاق پور به پرسپولیس کنسل بشه، امیر جعفری گزینه بعدی دفاع چپ خواهد بود / تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/138742" target="_blank">📅 22:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138741">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
❌
روی اشتباه محمد قربانی و بازیکن دیگه الوحده پنالتی رخ داد والنصر گلش کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/138741" target="_blank">📅 22:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138740">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🟧
🟧
🟧
دیدار پرسپولیس و تراکتور قطعا بدون تماشاگر برگزار می شود
🔻
حجت الله بهمنی سخنگوی سازمان  لیگ اعلام کرد هر دو دیدار رفت و برگشت پرسپولیس مقابل تراکتور قطعا در این فصل بدون تماشاگر برگزار می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/138740" target="_blank">📅 22:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138739">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
حالا شانس ما یا گل میزنه یا میشه بهترین بازیکن زمین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/138739" target="_blank">📅 21:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138738">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
❌
فوری از عطا حسینی فرد نزدیک به تراکتور:
✅
هاشم نژاد و ترابی به بازی پرسپولیس نخواهند رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/SorkhTimes/138738" target="_blank">📅 20:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138737">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
🇦🇪
محمد قربانی در ترکیب فیکس تیم الوحده
🗣
پ.ن شاید سرکاریم خبر نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/138737" target="_blank">📅 20:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138736">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
یکی از سایت های اماراتی گفته قربانی با قراردادی ۱.۱ میلیون دلاری و سه ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/138736" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138735">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووری از تسنیم
❤️
ابولفضل جلالی مدافع چپ پرسپولیس دیدار مقابل تراکتور و ملوان بندر انزلی رو به دلیل مصدومیت از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/138735" target="_blank">📅 20:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138734">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozCFPQ6WB_Air0_i-zmwotTROLNHpfcCJItYt7JSMpl7t695L4LcnI9nbtk8xx78U6Kbxo6QO3sVy4v9tRt_UOxkeaq4vkwNB3qdihxKravFZNaPaaZc390JTYgx9IHhhi_yn5q-DFoOFAj6Avh57oIOvhpdSMAO-8vQp1DQmlPZ-Ym3WaCQyBO5PNcCpbICuQLTs-PIgVKjjKwN78Bx5b4cVP2Mbn7MaqohsQ6wQeW8NwzpairgGaqQ7QrQPs9hXC9xdRH77VTRdPFX3BlughhceEcyUylo1gDjBUQNs7eGAjyqKm0NZ6B5OAXdr8RYf4wEBnEulCpoYF6rEn2Bzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ویژه بازی Scarab Temple
7️⃣
کاربران می‌توانند با هر واریز واجد شرایط، متناسب با مبلغ واریزی خود برای بازی Scarab Temple چرخش رایگان دریافت کنید.
در عکس فوق شرایط دریافت چرخش این بونوس ویژه توضیح داده شده! هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138734" target="_blank">📅 20:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138733">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
✔️
تارتار به حدادی گفته یه دفاع‌چپ از بین امیر جعفری و رزاق‌پور باید جذب شه/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/138733" target="_blank">📅 18:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138732">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6rP_qi2wLidQRFe6jinN7Goy-dBjCoTevf5X8qeDKgGc2IJPc1zxJVXMdLVj7n8UzpSjtpIdd4_u3CgGVgpLWiQIv8sterAeUv3TCdFQceEf2BCXjsxXc9zBnhQnQxu9WQWMZnbAYFY6DDOUuT8Irslk_zxWtH3HwJa-aKYHG7OHpCTN9JTKoPikaDY3M9sxBfyXzlbUrSwAwlmZxp7SdIoMnN3KNAE0Pjm4BHtaxc4cxppOqeG7tIdtMFyRYd8ASfqPN8E7TXNtf5AVXt_3EMmyc2i_9T8R8JF_ishGNn94imDHRRMRRVX7zA-m1bZFKYQbegxWf6bkRE0N8i5DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚽️
✔️
پیام نیازمند با 3 تا سیو موقعیت و ثبت کلین شیت بهترین دروازه‌بان هفته اول لیگ شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/138732" target="_blank">📅 18:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138731">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
❌
بعد از مصدومیت ابوالفضل جلالی، امیر جعفری، مدافع چپ گل‌گهر دوباره گزینه باشگاه پرسپولیس شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/138731" target="_blank">📅 18:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138730">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووری از تسنیم
❤️
ابولفضل جلالی مدافع چپ پرسپولیس دیدار مقابل تراکتور و ملوان بندر انزلی رو به دلیل مصدومیت از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138730" target="_blank">📅 18:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138729">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xa96SNCL_NwPYeN9P_6ravFdre7DYnfN4gAAM6OJ-n_hakUw7dMemqdmnX8ClDFWRLQ2fcXdQQR4QI6W63YNZlIaErjtqDAq81UHB0AVc-9MYNnCcbvgS1yMepdPD-bVdMi4cunumSKH9j_aoHF1uGpQyd64U4dHcVzwkUIO2m4hdnDWL9Z80bN2hyPnjod_fHj5tfPe5Yf03y1gPfY-L5LSOicauvKH2qsVuMel1hBUJm6a7gzh6GMPXfC9VyqKSNQaL24y4ZTcywp1GIvD-DGXN5nnnYtBsvQrUnV_GLSIuPz7PZzRINcyaKeQYDFiU467hUt4NC25-4Cw7xeIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/138729" target="_blank">📅 16:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138728">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138728" target="_blank">📅 16:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138727">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
بعداز مهدی ترابی ، مهدی هاشم‌ نژاد بازیکن تراکتور هم بدلیل مصدومیت دیدار با پرسپولیس و سپاهان را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/138727" target="_blank">📅 16:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
❌
تسنیم به نقل از سردار زاهدی معاون نظام وظیفه گفته که بیرانوند در لیست تیم امید نیست و از ۱ مهر سرباز میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/138726" target="_blank">📅 16:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138725">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
ورزش سه:
🔴
سه سهمیه بزرگسالان برای علیرضا کوشکی، حسین‌زاده و هاشم‌نژاد اختصاص داده شده نه بیرانوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/138725" target="_blank">📅 15:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138724">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔄
🔄
فووووری: چون نام بیرانوند در فهرسته ارسالی اولیه وجود نداشته در فهرست نهایی ام نمی‌تواند باشد و نمیتواند به عنوان سهمیه بزرگسالان همراه تیم امید باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/138724" target="_blank">📅 15:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138723">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul5tDQKBHSducePzoI97EyThjiCIBprXTQqXLiwgZbIfR1FYFrgUqVhjN13n3r7jg7NbURE_b1b4mB_yzCVIwK3NV-9vA_fk0Kuk7RUZIxKjbneG23OEK22ct3gzJAyrPxG_UNv2iql4aqomvahe2Ew79BzvAFFZlujna4VZaqT_iKj4zPHFejbn-J4tbfSid9u3B2OfbYpG9F6vAtT-5GdYvEool8i9nwMrca1mP8YcRT9lXaL3WwYLwpbNJ4Vt9dhH49x1gVxaCljHfs8g0nEGLN8sANHgIYV9cnQivXDHKG208fxiIyKa2dJREwCcoliP9keO6qH6_TMDKtm1Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووری از تسنیم
❤️
ابولفضل جلالی مدافع چپ پرسپولیس دیدار مقابل تراکتور و ملوان بندر انزلی رو به دلیل مصدومیت از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/SorkhTimes/138723" target="_blank">📅 13:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138722">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
✅
✅
فقط تا چهارشنبه پنجره نقل و انتقالاتی بازه و تکلیف قربانی باید معلوم بشه.بعد از چهارشنبه دیگه فقط میشه بازیکن آزاد گرفت   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/SorkhTimes/138722" target="_blank">📅 13:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
‼️
‼️
موافقت فولاد با معاوضه بیفوما و رزاق پور؟فعلا خبری نیست.قبلا فولاد حاضر نشد در ازای رضایتنامه رزاق پور علاوه بر بیفوما ۸۰ میلیارد هم پول بگیرد.
❌
❌
پرسپولیس همچنان مصر به جذب رزاق پور است و راهکارها را مطرح می کند./قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138721" target="_blank">📅 13:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138720">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9646c2be6.mp4?token=Voh3YlpJlIp2EEXfnM0VLN5_iV0H4OnUTlPUp1GbeweRqE5LEGgJYaQMboQ5LqByKh48cPb78dtU5rzl8fcGlsQjPVGQ-PNtRQa4OEyvlBLApmtP8D7OWUvnTYT5_Pc2b_5VmdFVKnYmviIVA1XzqJxgriObwUHgSx7hZPvjtxVoXTB6gIUD6ZOrPi-rusxHEOeOcMFEDpdKPmW7Q49_wRMr2np4j9ShtCJPxsoS7pszr2v9fZgPxT9QZ_dJ2FpF_7TS2Qpxg8a7g0Bau6TJji9502xye8fgw8oBVqYm7uUNtvwS0k6trET4yMZusNjxpzDViliasuvbgrtwpUmDJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9646c2be6.mp4?token=Voh3YlpJlIp2EEXfnM0VLN5_iV0H4OnUTlPUp1GbeweRqE5LEGgJYaQMboQ5LqByKh48cPb78dtU5rzl8fcGlsQjPVGQ-PNtRQa4OEyvlBLApmtP8D7OWUvnTYT5_Pc2b_5VmdFVKnYmviIVA1XzqJxgriObwUHgSx7hZPvjtxVoXTB6gIUD6ZOrPi-rusxHEOeOcMFEDpdKPmW7Q49_wRMr2np4j9ShtCJPxsoS7pszr2v9fZgPxT9QZ_dJ2FpF_7TS2Qpxg8a7g0Bau6TJji9502xye8fgw8oBVqYm7uUNtvwS0k6trET4yMZusNjxpzDViliasuvbgrtwpUmDJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تیم
❤️‍🔥
❤️
✔️
پ.ن جونم به این همدلی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/138720" target="_blank">📅 13:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138719">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی بازی با تراکتور و ملوان را از دست داد. وضعیت مبهم برای دربی
❌
❌
ابوالفضل جلالی، مدافع تیم فوتبال پرسپولیس، به دلیل مصدومیت از ناحیه کشاله ران، چند روزی از میادین دور خواهد بود. طبق بررسی‌های انجام‌شده، این بازیکن برای بازگشت به میادین به…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138719" target="_blank">📅 13:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138718">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
دستمزد طارمی در امارات آب رفت.
🔻
سایت threads امروز(جمعه) از دستمزد مهدی طارمی در لیگ امارات پرده برداشت و نوشت: مهاجم ایرانی در الوصل قرار است سالیانه 800 هزار دلار دریافت کند. دستمزد مهاجم ایرانی در الوصل در مقایسه با المپیاکوس(سالیانه 2.2 میلیون دلار)…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/138718" target="_blank">📅 13:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138717">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
✅
✅
⏳
10 روز تا پایان پنجره نقل‌وانتقالات تابستانی فوتبال ایران باقی مانده است.
❌
❌
پس از بسته‌شدن پنجره، باشگاه‌ها تنها امکان جذب حداکثر 3 بازیکن آزاد را خواهند داشت. بنابراین روزهای پایانی می‌تواند برای تکمیل فهرست تیم‌ها بسیار تعیین‌کننده باشد.  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138717" target="_blank">📅 13:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138716">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-JnlAmkvLPrernusV9bfLNohXfz49u_d2Tj2S6DQ_j8QvWI8ECCftlzvP1ntpb2FCcCTb0BYVCHU0p-JKzYZPeybtJRfzx4YZ9r6IRfWNn5_UpE--2kuF-AFg1zXZzZwJeejeATfO7N0Ezzl4DHn4V_3ehrQj9WkpTrRukhF-8ddq2Y6oOdwsXI6BZOd1GiMUrwWzGDd0JOwT4wdp1cy3Q4x-i0bkAqFOm0TvipgV7LdGXi54bThfB2KODdgCjIfAiqkd4K1AdcdW0UmiQTZA1VJADzlW-TrEAzeYDAQOsYIcv9tv5WdaNkMNG4-Dn_-83DV7g8eEby293uCxZaRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فرزین معامله‌گری، بازیکن پرسپولیس برای گذراندن سربازی به ملوان پیوست.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138716" target="_blank">📅 13:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS9rvWQvxKWpNH5cMNLkSmbzbDDLbinTPA6s4RaroLwJOHV9dA2DBs0Uq82c1-U9FyyygJmajYU3Xw5DUP6_tkiyJha-sQAX9dLpNPYa4UDn7pR_QyUepfevb80Vjm3yPjnoeBdc9DGiRqQNymEOlIQbck29SIsoKcN7o6hryDDYMeaDXktpBVoCQjlAi7-1WrCYiTFHX1SQtaPqhHZWPT4dnG5ZgSQjE3LsYYNOUe6wmjMPSHg5xVOvlkIQeA6jUc4_9wpmLAoloWtWATlKjSgTIfX7OYzc7OpsM5Yfepq8mjAuKj6sRNlQdrNNsdWzeSVW7833Jn0tq9TcDP767Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آنا: 20 درصد از قرارداد بازیکنان پرسپولیس واریز شد، و قراره 20 درصد قرارداد بازیکنان خارجی هم بزودی واریز بشه.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138715" target="_blank">📅 13:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138714">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kurjigqb2RvbrFlemCcB_eTSICnPwLBzkPB9Tl-5T47wGLLA20M-0nTPHYhuDNLlMUdhg4pkZBAxb3T6pAIh2V_g9bk1pskCrl4BH0pTd4P5jy1TznJSD7oAuC5n2mcOWCVjnqQ8pT74LftAabNYRy9PDFgXzRZEBF2c8yRB5gVYyY3Jmm6dTHTaI4qF_hk_FM83l2-k8Mtv4ElLaRbYRBu3RuunSPpmXJee5dfuA682yon3ZCWsX_OdraOz66kgEuRYRRDsUSUtAJhGxXLzhKErzrIAoc_5O7ZxG6vEROVVwx8QOxTdIXsxm08BPDazArxE7weM6xDsnDXyE4QVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دستمزد طارمی در امارات آب رفت.
🔻
سایت threads امروز(جمعه) از دستمزد مهدی طارمی در لیگ امارات پرده برداشت و نوشت: مهاجم ایرانی در الوصل قرار است سالیانه 800 هزار دلار دریافت کند. دستمزد مهاجم ایرانی در الوصل در مقایسه با المپیاکوس(سالیانه 2.2 میلیون دلار) یک سوم شده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138714" target="_blank">📅 13:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138713">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
✅
✅
در صورت نرسیدن جلالی به بازی با تراکتور ابرقویی گزینه دفاع چپ در مقابل تراکتور خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/138713" target="_blank">📅 13:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138712">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmwBvtuZoZ5PR_Vtnn3gIKAHlz-5O_GzzIB15HdLyO-C7K1Dc8akWh52BBKgE8ckq6LG-UhymSZQTjM7pUA1r3_5uo8Ci8hlyPFuLxy8IiqJigxWnqEhVt-DGU05UQG2ofkbE-UXXhJB-VYPFmwO-eUYbVvSCn4NAUewtntnIoZSgBwci0YculDOjtLPtaJDUD1ycPM906mfxsiYdXwK_e6GEsgGO40GMuwPbaQ7ILzjMHnEylKnm1YFypRuIqM2lRLc6HDCQ2WzSgZgHuMxL1Sbda-7fet6kb_78T9pES_FQ_QQ0LAycM_Whck2L63b98qFlNwa8vEskcP2pmqDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏴󠁧󠁢󠁥󠁮󠁧󠁿
شروع فصل با یک چالش تازه برای توپچی‌ها؛ آرسنال در هفته اول به مصاف کاونتری می‌رود!
آیا شاگردان آرتتا فصل را مقتدرانه آغاز می‌کنند یا کاونتری غافلگیری بزرگ هفته را رقم می‌زند؟
⚽️
پریمیرلیگ انگلیس
[
آرسنال
⚽️
🆚
⚽️
کاونتری
]
⏰
جمعه ساعت ۲۲:۳۰
🏟
استادیوم امارات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/138712" target="_blank">📅 13:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138711">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/138711" target="_blank">📅 12:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138710">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
فوری | سردار زاهدی، معاون نظام وظیفه عمومی:
❌
علیرضا بیرانوند از مهرماه 1405 سرباز خواهد شد و دیگر امکان بازی برای تراکتور را نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138710" target="_blank">📅 12:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138709">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
فوری | سردار زاهدی، معاون نظام وظیفه عمومی:
❌
علیرضا بیرانوند از مهرماه 1405 سرباز خواهد شد و دیگر امکان بازی برای تراکتور را نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/138709" target="_blank">📅 12:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138708">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/138708" target="_blank">📅 12:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138707">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/138707" target="_blank">📅 12:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138706">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
🎙
میثاقی:
🔴
جلالی بهم گفت حدود ۱۰ ۱۲ روز نیاز به زمان دارم تا یه میادین برگردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/138706" target="_blank">📅 11:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138705">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138705" target="_blank">📅 10:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138704">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRzgkYEMLoKBA_RlCh7Js-tvdJb3XUncW2LX0xbLqAHYRSjrfqANxzj3L66svfgdFODszjsxQLi5VbqKGzd7MVtBw_QtYnAA4Tvnk-C0kS-wSqabViLGFBAdpX285k8BYX7SylKoABCKAQmFTdEIkQquhZ8Z-RztbGLXnrzaNG-qOM3IvJaeI52xom5vRihidmSajJ7DcnJcIbRmNOr39Juf8UfKo1PTYuwHxJNj-IwVwrj1EUyaWLfPbcEKUcgDnRqTb3JYU1PfmTyJAXxvHa6jIdCRLX88IhmC4qnQ9LerimuNyu6OsmAb5gitOZeFtIC3LkSROpNCYHfi6kpjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/138704" target="_blank">📅 10:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138703">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔄
🔄
🔄
پرسپولیس در دیداری دوستانه با گل‌های امیرحسین محمودی، مهدی تیکدری، پوریا شهرآبادی و محمدحسین صادقی، 4 بر 2 آریو اسلامشهر را شکست داد.    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/138703" target="_blank">📅 10:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138702">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
🔻
🔻
میثاقی: احتمال داره حسین زاده و بیرانوند به همراه تیم ملی امید راهی بازیای ناگویا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/138702" target="_blank">📅 08:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138701">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
❌
باشگاه پرسپولیس برای جلوگیری از جاسوسی ارتباط تیم با هوادار متمول خارج‌نشین رو قطع کرده اما هنوز به بهانه‌های مختلف مثل اسکان برای بازیکنای جوون با تیم در ارتباطه
🔴
🔴
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/138701" target="_blank">📅 08:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138700">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yq_wFlov-ZUGZlRFVmZjaOpP4kc3X1Re14H2vjgMlDKiJaKkTJO4lH6kI3R2p8CMX3Mr3KIZnz2l44JSGcNkHVq3BQN5rv3n7dD3KzozhhI0qUqNRoycv0jzs9X3sHWrAuMdIbAz6IbV_wY4LOweQtl3j6YIkn79x2bwZSD2_nbobFo4RRjCogfNpUeHoYs0U76vhOSSDaa88_Ulz3ZculkRkckQQT2KlBOI8-ZU-SOco-EgAU6Et31Ihmfb9xtu2cN174mMPmh1-qaLGqS2_LV5cJ3fQCo8ingUNalpelndQpnhyvefe7xLE9__Yt9CGFYXaXcTs7efRNelB2oVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/138700" target="_blank">📅 08:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138699">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">7️⃣
وقت چرخشه! | SCARAB
TEMPLE
🎰
همین حالا با هر بار شارژ حداقل
۱ میلیون تومان، اسپین رایگان متناسب با مبلغ شارژ
دریافت کن!
💰
شارژ بیشتر؟ اسپین بیشتر!
🎁
هر چرخش، شانس دریافت جوایز نقدی
⚡️
اسپین‌های بیشتر، فرصت‌های بیشتر برای کشف جوایز بازی
😳
👾
اسکرب‌تمپل
، با یک سیستم اسپین پرهیجان و جوایز متنوع:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/138699" target="_blank">📅 02:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138698">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس، پرسپولیس فصل آینده در لیگ یک تیم داری خواهد کرد و اگر مشکل خاصی پیش نیاد بزودی امتیاز فولاد نوین به پرسپولیس منتقل میشه؛ در صورت نهایی شدن انتقال امتیاز فولاد نوین…</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/138698" target="_blank">📅 02:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138697">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🏆
🏆
دربی تهران رسماً در استادیوم نقش جهان برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/138697" target="_blank">📅 01:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138696">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
حدادی: دوران بازیکن سالاری و دخالت هوادار متمول در پرسپولیس تمام شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/SorkhTimes/138696" target="_blank">📅 01:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138695">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚡️
مدیر برنامه آسانی: نامه فسخ دستکاری شده است
🔹
مدیر برنامه یاسر آسانی، هافبک استقلال، انتشار نامه فسخ قرارداد این بازیکن را تکذیب کرد و مدعی شد نامه منتشرشده با هوش مصنوعی دستکاری شده است.
🔹
رسانه‌های مختلف امروز نامه‌ای منتسب به فسخ قرارداد یاسر آسانی با…</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/SorkhTimes/138695" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138694">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🟫
🟫
🟫
بهمنی: استقلال به عنوان میزبان دربی، نود درصد گنجایش ورزشگاه را در اختیار خواهد داشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/SorkhTimes/138694" target="_blank">📅 00:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138693">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
قابی از دیدار تدارکاتی پرسپولیس - آریو اسلامشهر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/SorkhTimes/138693" target="_blank">📅 00:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138692">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
🔴
🔴
پیگیری کردم؛ ابوالفضل جلالی احتمالا به دلیل مصدومیت بازی‌های حساس پرسپولیس مقابل تراکتور ، ملوان و استقلال را از دست بدهد. در واقع یک ماه دور از میادین.
🟫
🟫
🟫
البته خبر پارگی رباط صلیبی صحت نداره چون زانوی جلالی نچرخیده که رباط بده و خودش هم با پای خودش بدون…</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/SorkhTimes/138692" target="_blank">📅 00:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138691">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✖️
✖️
احتمال معاوضه بیفوما با رزاق‌پور وجود داره.
🔴
تارتار تاکید ویژه داره رزاق‌پور جذب بشه. البته تارتار فعلا در قبال رد کردن بیفوما پاسخی نداده.
🔴
ولی درخواست فولاد همینه. بیفوما رو بدید رزاق‌پور رو ببرید.
🎤
سپهر خرمی  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/138691" target="_blank">📅 00:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138690">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
رسمی؛ با اعلام سازمان لیگ دربی پایتخت برای اولین‌بار قرار است در اصفهان و ورزشگاه نقش جهان برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/138690" target="_blank">📅 00:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138689">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
ایسنا: هر تیمی که 1.1 میلیون دلار به الوحده بده رضایت نامه محمد قربانی برای اون تیم صادر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/138689" target="_blank">📅 00:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138688">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚜
علیرضا بیرانوند در تلاش برای حضور در تیم ملی امید ایران برای ۳ سهمیه بزرگسالان میباشد تا با کسب مقام احتمالی در مسابقات آسیایی از خدمت سربازی معاف شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/138688" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138687">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🟫
🟫
🟫
بهمنی: استقلال به عنوان میزبان دربی، نود درصد گنجایش ورزشگاه را در اختیار خواهد داشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/138687" target="_blank">📅 23:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138686">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🟧
🟧
🟧
دیدار پرسپولیس و تراکتور قطعا بدون تماشاگر برگزار می شود
🔻
حجت الله بهمنی سخنگوی سازمان  لیگ اعلام کرد هر دو دیدار رفت و برگشت پرسپولیس مقابل تراکتور قطعا در این فصل بدون تماشاگر برگزار می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/138686" target="_blank">📅 23:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138685">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
حساس‌ترین بازی هفته سوم لیگ برتر پشت‌ درهای بسته باید برگزار شود؛در شرایطی که براساس رای فروردین 1404 کمیته انضباطی و تائید استیناف تمام دیدارهای تراکتور و پرسپولیس مقابل هم در مسابقات لیگ برتر جام حذفی و در دو فصل 1405_1404 و 1406_1405 باید بدون حضور تماشاگر…</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/138685" target="_blank">📅 23:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138684">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un50eICkP8u2AG41PA0bpHdAOUiXcMo46-yocOZUITG0h4fw_duDeETvIhl2kTSy6vSGobFjJPqEkPD4mPWbbJgVgM-y8JKZ8YOaLnuT_8ngheHbi3XiWcZmvX7uKgrADJ4nAWOrrh357FZWL3H-FyyjfRK-UGr3Cpjkls4wrr7MH2w0bo5bn4rsXtWvPT-v42B_HuKI8xh9quxo7XVbsesjVTz5J4CMOqPO9OtlwbZGQQdexq3_PpJpF3za3wvE2Xumqaw74tX1K7FWA0Nm2g6WUq-CaP1uJuWMgSk5OX9UBYQmtBVTh_tVK67Ph5t5xvYG1b1c8_gaaCXx3LgMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ایسنا: هر تیمی که 1.1 میلیون دلار به الوحده بده رضایت نامه محمد قربانی برای اون تیم صادر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/138684" target="_blank">📅 22:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138683">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8400611245.mp4?token=OckMbx7WDdJCkmIV_1bItVMYQLzx0FXEt2nS4tOTe7YBCBV4URQNp5RYSGDTlwNeritrQ5ez9VBRHqHb9-Ga5yUrtpxc3NLtpWRokS15mdy8OZ8e94xUDMqqAU4dy4utgflk5c6QkaY_qNkZ3Qw-PIJHFP3D-P4G3oE2RyjaFd625i5ncYuwItnzdhGNQpd2ldOhFBsvEFjYr4Whc82w-AsoSzXD2tRBq5x918qxB-Ah8UCSPO2QSOA5j_RCuTaaPQ1NEOdWrSxIychov5h7gjzsPIHor3NHsMUjwUTvLU-hQ3geEUGHlJ90ipQOatZZ3UyAnbvX-vPFZKd1CMfThw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8400611245.mp4?token=OckMbx7WDdJCkmIV_1bItVMYQLzx0FXEt2nS4tOTe7YBCBV4URQNp5RYSGDTlwNeritrQ5ez9VBRHqHb9-Ga5yUrtpxc3NLtpWRokS15mdy8OZ8e94xUDMqqAU4dy4utgflk5c6QkaY_qNkZ3Qw-PIJHFP3D-P4G3oE2RyjaFd625i5ncYuwItnzdhGNQpd2ldOhFBsvEFjYr4Whc82w-AsoSzXD2tRBq5x918qxB-Ah8UCSPO2QSOA5j_RCuTaaPQ1NEOdWrSxIychov5h7gjzsPIHor3NHsMUjwUTvLU-hQ3geEUGHlJ90ipQOatZZ3UyAnbvX-vPFZKd1CMfThw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بازگشا سخنگوی باشگاه پرسپولیس: فکر نمی کنم محمد قربانی را باشگاهش بفروشد/ پرونده هیچ بازیکنی را برای جذبش نمی بندیم ولی در خصوص این بازیکن با توجه به مبلغ قراردادش اصلا وارد جزئیات برای این انتقال نشده ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/138683" target="_blank">📅 22:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138681">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⚽️
🔻
بازگشا: شیر ما برگرفته از هخامنشیان و نماد باشگاه ماست، اما شیر استقلال و نمی‌دونم از کجا اومده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138681" target="_blank">📅 22:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138680">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🚀
آف ویژه سرویس نامحدود
🚀
1‌کاربره فقط و فقط 600T
2 کاربره فقط و فقط 700T
3 کاربره فقط و فقط 800T
ثبت سفارش و پشتیبانی:
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138680" target="_blank">📅 21:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138679">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔻
🔻
🔻
طبق شنیده ها فولاد در آخرین جواب به پیشنهاد پرسپولیس خواستار معاوضه بیفوما با رزاق پور شده.
❌
همه چیز به نظر تارتار بستگی داره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/138679" target="_blank">📅 20:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138678">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">💢
💢
💢
باشگاه میخواد یکی دو بازیکن جوون رو وارد معامله با فولاد کنه تا با قرض دادن این بازیکن ها و مبلغی پول رزاق پور رو جذب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138678" target="_blank">📅 20:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138677">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
وضعیت مدافع چپ پرسپولیس بزودی مشخص خواهد شد
✔️
ابوالفضل جلالی مدافع چپ سرخپوشان که در روز گذشته دچار مصدومیت شد قرار است طی امروز فردا تستهای پزشکی خود را آغاز کند تا درصورت عدم مشکل به ترکیب پرسپولیس مقابل تراکتور در هفته سوم لیگ برتر بازگردد.   «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/138677" target="_blank">📅 20:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138676">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pzahw5Eb2dte6OkYlnKDli97OTQqwZ5sD2nbr3wj6E5GEO90b_Jhnsyx2ZmRd-gSQwFNlObzOwRqyDSPBj7-YiLoj1bKiebAWiHlD6b1sjQYIMwwz-ICPT1R1q6hnVcSrGBzGUVJl2q9PN1MEb7KgaLBUnMiw3mvzv1HMbzu8JE13-F-YOdxLwvOZFoaCzkoYMksB54ZWM8FlGP8FP85gyTfnk4nsohJ6D5863FIIuQfROvl9c2zKyxDR656H1u_pI5-xVAwUA7khNbHQi_Il7mbwvcJ5wp23BJqxTwcalnOAx6wPEvlFI5_nMzDkLrO10l8nRmUhBo9JsChK3sldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
فوری ؛ یکی از مدیران الوحده امارات در گفتگویی با رسانه الریاضیه این کشور اعلام کرد که رقم رضایت‌نامه محمد قربانی برای فروش این بازیکن به‌ دو تیم بزرگ ایرانی و خارجی رقم 1.1 میلیون دلار است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138676" target="_blank">📅 20:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138675">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnyEhjToA-MSXkae4TZyQR-5j5DOdDzvPzNR8w6S6fOFxkCvv9jNOlPDJ6KuzxXkmmNznY6yPlTDPdJjwGwmKNqNkgzxbp-arvFMXt2As04TaeVB_0vf2RXryM15nNg1XBnZzPzJo9vGOfQrEqr9hlzayh0gk9F2EszKN1t1gEYAtf0L-RspmM44cpUGBlJuTQablRwjFRVZaqO0bbSn47ssWIaqs0rv9vScpJRFsgTHW-yjtK3DWGbsXiNl7hIB0ACteFmZx_IFoGtwbdvETbwfc1KrJYolicf_GFOnujuJ77JnHB6HaMC7KxRsnn7h80wBXAFJenXsb4tdh5Uyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
قابی از دیدار تدارکاتی پرسپولیس - آریو اسلامشهر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138675" target="_blank">📅 20:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138674">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5bbffc124.mp4?token=rTnv6VMzGGHCcm8E09oqdSG4NDczi8cMM3EpFe-ZWCf0xL_xY1CGz_QXBPmHywjIMOxmqptI4DvXSqb0aukrIV73J8hoyrmppDmJT8-py71XptwnpYqm-UQGXE2SYnbKn3MJ_i-O0ATQXMdlov7fshHQFIdi5O_FJ8DSDv8nXGMJuzf9-ko6316yr6ONywzwYgZwb4q6WCATdiHH-yq0drQxR8qpdwZPf2Zff6t0j6aykPhIRIxBZSsZnSU4Wp3GeIMq83Bp2AJcIrS9paj-Uj1k4t3n7mm_nTlX4_1Dg34-q0rvFITs186yFOPW2ezDLhfit-ZRsD9dVf0qn36VlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5bbffc124.mp4?token=rTnv6VMzGGHCcm8E09oqdSG4NDczi8cMM3EpFe-ZWCf0xL_xY1CGz_QXBPmHywjIMOxmqptI4DvXSqb0aukrIV73J8hoyrmppDmJT8-py71XptwnpYqm-UQGXE2SYnbKn3MJ_i-O0ATQXMdlov7fshHQFIdi5O_FJ8DSDv8nXGMJuzf9-ko6316yr6ONywzwYgZwb4q6WCATdiHH-yq0drQxR8qpdwZPf2Zff6t0j6aykPhIRIxBZSsZnSU4Wp3GeIMq83Bp2AJcIrS9paj-Uj1k4t3n7mm_nTlX4_1Dg34-q0rvFITs186yFOPW2ezDLhfit-ZRsD9dVf0qn36VlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
🏅
این شاهکارو از دوربین باشگاه هم ببینید
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
❤️
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138674" target="_blank">📅 20:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138673">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAbs5E2eK-8ZFCvCo_UXgtO3hmbjBw1EpN6NP_ns81KL-FNurWEAmpEkuZl7VnZbTxNqDFSAVwyleQcAE9Pvrl_fMQgc5c6dsXpWFc9vUDKiL428xCjbHhcLqLn_R2xkmHPHVnlHsfXLmvMyOyfNvDQj8aGVdEY7vQ4xPQmDElj6Tvvlq9uuJE3BInOfr0nSeAO7TUcD5oVfqm5pbpB2K_JFhepUvUSc8A6_hOBcG8_TtTWIfto3f7RBYMdlThVKIQTV_eHP4xUiZHD8Wbbj6HkEwa7IuqMScNM88TByli8BvdI3VXjsyVSiC3Ztfns4tG_dcU6ipSs6e7LRWxtrKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ویژه بازی Scarab Temple
7️⃣
کاربران می‌توانند با هر واریز واجد شرایط، متناسب با مبلغ واریزی خود برای بازی Scarab Temple چرخش رایگان دریافت کنید.
💸
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138673" target="_blank">📅 20:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138672">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔔
⭕️
احمد العتابیه، رئیس نقل و انتقالات باشگاه الوحده، در مصاحبه اختصاصی با رادیو ورزشی دبی تأیید کرد که محمد قربانی، هافبک ایرانی، در آستانه جدایی از این تیم است و خاطرنشان کرد که دو باشگاه ایرانی علاقه جدی خود را برای جذب این بازیکن در پنجره نقل و انتقالات جاری نشان داده‌اند.
❌
العتابیه اعلام کرد: ما مکاتبات رسمی از دو باشگاه بزرگ ایران برای امضای قرارداد با محمد قربانی دریافت کردیم و این بازیکن در صورت توافق نهایی این باشگاه‌ها با مدیریت الوحده، پذیرای یک تجربه جدید است.
❌
العتابیه فاش کرد که ارزش غرامت مورد نیاز برای جدایی این بازیکن ۱.۱ میلیون دلار (معادل ۴.۰۴ میلیون درهم امارات) است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/138672" target="_blank">📅 19:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138671">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
شایعات : تارتار میخواد مقابل تراکتور یه ترکیب سر و پا هجومی بفرسته تو زمین  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/138671" target="_blank">📅 18:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138670">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووووووری
🚨
مهدی طارمی برای عقد قرارداد با الوصل امارات راهی دبی شد
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/SorkhTimes/138670" target="_blank">📅 17:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138669">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔄
🔄
🔄
فدریکو پاستورلو؛مدیر برنامه طارمی:
🔻
جدایی‌ مهدی‌ طارمی‌ از باشگاه المپیاکوس قطعی شده است.
🔻
درحال برسی پیشنهادات هستیم و به‌زودی تیم جدید طارمی رو معرفی خواهیم کرد.
🔻
مهدی یک آفر از لیگ ایران نیز دریافت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/138669" target="_blank">📅 17:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138668">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0ViWknjvVc0r5Y2zHCjxm3VeoZbHXaVaIQElneuEpBNRkMfb84QOKIQC4SJKc8329mBRNyyRDYBq_Xk_13jBId2AseL8AmLLW13vp_97VbPPRis-Mto0qIIRD83QaPrGrq45KxOcZbElzdczsEDdarf5ewixbAALyrW4WEKiBcj6N5MpJn8GwzPsAxgbg9yt_Rq_4I1rmWLvTWr-pdkGTrA6rVOCvpx0V-xwDtR8vc5swvV0_iQQgT3P1sjwjQXMgOem5rFJjjn3Z0N-Mv6WoOQEbXUj6s2QmTsc0VpOyt7iV-YvfKTrJgHKZStyKUjE0CRj2LMHIDhSLSt0wCy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
شایعات: الوحده امارات با فروش محمد قربانی موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/SorkhTimes/138668" target="_blank">📅 17:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138667">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
ایشون بازم نخ داد
👀
🚨
کامنت محمد قربانی برای علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/138667" target="_blank">📅 17:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138666">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇪
یکی‌ از خبرنگاران نزدیک به باشگاه الوحده مدعی شده که محمد قربانی با عقد قراردادی سه ساله به یک تیم ایرانی پیوسته.
⏺
اما اسمی از تیم مقصد نبرده و گفته این قرارداد به زودی رسمی میشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/138666" target="_blank">📅 17:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138665">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">💢
💢
💢
💢
مدیریت بانک شهر صبح امروز به وعده‌اش عمل‌کرد و 800 هزار دلار بودجه برای جذب محمد قربانی دراختیار مدیریت پرسپولیس قرار داد.
❗
❗
مدیربرنامه‌های‌محمدقربانی  به پیمان‌حدادی‌مدیرعامل پرسپولیس اعلام کرده باشگاه الوحده رو راضی میکنه که با همون 800 هزار دلار رضایت…</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/138665" target="_blank">📅 17:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138664">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
وضعیت مدافع چپ پرسپولیس بزودی مشخص خواهد شد
✔️
ابوالفضل جلالی مدافع چپ سرخپوشان که در روز گذشته دچار مصدومیت شد قرار است طی امروز فردا تستهای پزشکی خود را آغاز کند تا درصورت عدم مشکل به ترکیب پرسپولیس مقابل تراکتور در هفته سوم لیگ برتر بازگردد.   «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/138664" target="_blank">📅 16:27 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
