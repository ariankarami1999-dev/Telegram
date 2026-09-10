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
<img src="https://cdn4.telesco.pe/file/Gw25KyPZv88yv60EfisI_Cju4JAkyVEcxIG2jfX9ziq_Q0WxvUJhLUvuLt4de37kzDhK6hxSDnx67IurxE_rE-sGSRe6g4NoyQ9NiQrf-qtBxllpCWLCwcusaxKOkqkqjrdLqZC6VdS9hRcwWOLePGAoDLR9EEy487QA0BxoHhhJvUP6jpQMHWjEtvTeGGEkyWyXMpE9sy4SrVYml3D9YkGR-AQxIkTqcjtHp_H3aSbM4lQzmqerE4maELtamiCFR8LqbjX1uMoLgEwSjX-9Z5q_9Cx1LsPfkfOWBbM4y7hNfIualOh2rwBiMKjdopu3EA5FqLdN4atFelsb6XALLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 539K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 22:20:05</div>
<hr>

<div class="tg-post" id="msg-29482">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At9OEt7s-P0mImJFpuvFaJGwdJdrAUA2Nh1x2YuJg5v8apKTMQwC3SuKD0wmQ-XxUWQ6FjBmEPJztPkxrw_oQsg2_uNzrU4djjxHBqxgD8tNeZqnt2gA0_hbUQXz3yV_xDuXou_g1dqa73HRsAoVuBGiOA2ZPvtGhAt9aA4ElU_q1Rjw88qZ4xokJ5gd8IqNRFRD6YcjrC-JZ-h_rgeOP7qIKEGuZUx3NXgoxFmx9LDPXpnvYHlK_DIDmM-zfqxKHVW1Ucjkyuz9PPaH-K0x6a2Lr41itNXgPjnpAWzlk4OU_IyTsdNjnlmAlvOsF_FaP0JmMnbnenJY-ZtKt2b7-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ابوالفضل رزاق پور از مدیریت باشگاه فولاد خواسته با انتقال‌اوبه‌باشگاه پرسپولیس در نقل و انتقالات نیم فصل موافقت کنند که گرشاسبی بابت رفتار حرفه‌ای رزاق پور در این پنجره به او قول داده در نیم فصل همکاری میکنه تا این انتقال انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/persiana_Soccer/29482" target="_blank">📅 22:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29481">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFMaoTJJ2XCbN_VWrBs25FRY9lPfVzEm-ATrQ8bFJs3OqIjOx4mNLXQR2PWUN9zYjlX2e8nun3CtvTERdoN36qLD58fuqrRpMfoNYj0_Q-rYqotoZJFj2JmPMFtaPyErDjDB5W6dXkKxzEom-BLEkf_RYY4FCRuy9Lvo20NcrtCeggevfhaWx8J9YKHvdDq7HoiqwF5u2t9QfD9r96NX9Iq1rVApsNcWRo2yae5PQ2REFwk2U884DD0PGEIaBD8LnTfGO8kklY_1z04-l82vp5gootij9BUJsxEdmdzmBS0nahkoSrqoGojNWFMUw6UmakC-zDsmqFdZQu9dpMAnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇨🇴
با اعلام‌ رومانو؛ خامس‌ رودریگز فوق ستاره 34 ساله تیم ملی کلمبیا در آستانه عقد قرار دادی یک ساله به ارزش 650 هزار دلار با باشگاه آولینو در لیگ یک ایتالیا قرارگرفته است. شرایط‌جنگی کشور باعث شد که خامس از حضور در لیگ ایران پیشمون شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/29481" target="_blank">📅 21:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29480">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q08bj5VbovLU5G-OVJE8KLAFCWLGygzZtoZz7VGnybHfsnFzE5WVMgmemWDcsHFYJa_lqKa5EVzk24ZaCP9j13OEFk71s86yogNvSP2WLIhBMISeKso859z4Zhq6upoobAdGn3qWm_Sjkc2zYSSLimB4djgZc4RyDHx0ENr-fdFDBcfgu1y8ictuofz5ZzgDOcNCGG-kEMDAg1T8DmPfWWUscp71lYDWMkVX20rZj4XT9v11PhaOMt9PWKjuUnxlyrZI3Ft5BTubbUZzrq71uOREILckUznraeCGAdD3rHPIABUOyjNLwb1dD_SrW2ERR8TgiqS0YtuQnq_PUHol6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فکت؛ رافینیا دیاز با گلزنی مقابل فاینورد تبدیل به اولین بازیکن تاریخ بارسلونا شد که در پنج بازی اول فصل برای این تیم گلزنی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/29480" target="_blank">📅 21:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29479">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYUpTFM8a2caIdz4IRcAkFZcNr0oDefb471BdME6o4pU1x2dNH4-NDdvKTdTRWYBZdEzjtAGVnRkTlJHtkGIh9MYXVt27uvQ-dx8MP6qEiaauHr5nJh3a6PdrMdeeF_MyTcj1pJnnJlnHQ38FcSomJyvn5lZ2RWA23F9T1iTqBr8qqI_TAa3AwWozeyzGG09u2PnTTMJy9YH1BQzCiFIq4WiKAWWP6GZZuwOFmN7kEe74l5LwP4lI6HDVoOC81ELxOP1Fv5ga41ZBZ75SWU2H-9vAffP396VUuk1aDvfH6ROkC_DRmo7fEDL-YcCEWkkvQkeZ_rRY0YvYrXU-ffKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ درحالیکه باشگاه پرسپولیس و کادر فنی اش به شدت به لغو بازی با خیبر معترضه و اصرار به برگزاری‌دیدار برابرخیبر در روزیکشنبه داره تیم خرم‌ آبادی تمرینات خود را پنج روز تعطیل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/29479" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29478">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw-w7dXQ3oKqJ_APuRX2bAhifm_1gXIAEHHmc9mIL4unFbanqywgf7CUYHv2gmXff2T8FEUeLHadjGWzmiucm_tYSlEmj8UAsKcd2fCk9avn89-jtu-pC6afnHjPsvq5LzehQn8j3POWtqh1ssxncndFNhHtS5Cd68tb2cGLB12I04iFNjYPj1Q7Lootb2APMKcMuDHb9bMZTMap_NX4NACzmyky0a6lCw41SYV_EdO27HmuOrjAR3U0dIH3iqD9y8-scfKfIt5MFi3yjh4aNy7LoMYTE0agrenyQ8A6gSRVYw2pwqVTCUZGs1ocVcQDrPVj-UL4ex8y7zco9XTYHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/29478" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29477">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alCsuupyHk7DyfIfrlfMNHH2Uhs8ZnFci1-81_zxOF1q2-D02E2Zs0pvfi9UEwKWGZjHqPzjawKGMTu5yVREqb5rHiwcPROytKsE6f7X_v-8makyyYVHsUwGiUt9mt1ALUR1Z_x4MamB1HwpGVgk-qBOEPXOJhDBd36UTPVIk-86A9yWirRdYwV_a4K4x7pmCESCTql_mbQ-HOlkdcqn8tRy8Iud7NzN_44ZaV4QN1pud5AfLWxhlWTi4qrBTpGOWiBkqZk-VP1KPLkIdCwrvoVKXRrKGAX8eKUgTsQNJNoKNQUVjKEWQD2lL-JgQfwL81QCUR7yb0CWDjMz8DfbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇩🇪
بایرن مونیخ
🆚
بودو/گلیمت
🇳🇴
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/29477" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29476">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu1O4uJfM7YEmy-UAPtShIk1Z0nS2FPiE-w-ecWD7_sS7NhveCtt5DDEXwPvgBNe7Ha-M5XjU1XF8LUaG_43eXM-rAjPZP_90B4XghU4K-kKTCz403LFyc7Hs951Q2MXS82T7oGZtVW8lLBwq8hsy7AeAc8gjRonBQXz3lDCDNvpiLCXdQIxaiM3vUO-Zam_y9t7MnAYhXyOhYR-VacS7oZUfEIKdyFDQhUDtUn2axodgOTm5llAYWWNhzr-sQDlQEq8hmknOVkNzvoyP9Q178WSMcN_7S0J_38Jm1I-bQV8ewb3vgQ0ATOroret0plfAbL7GPXnPKpZMjCPCcQsHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لیگ برتر؛ کار بزرگ خوزستانی‌ها با بردن تیم جوادنکونام؛ تراکتور بالاخره در هفته هفتم تسلیم شد؛ نخستین شکست‌پرشورها در فصل جدید.
🔵
استقلال خوزستان
1️⃣
-
0️⃣
تراکتور تبریز
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/29476" target="_blank">📅 21:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29475">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya43awk1tJb12HXYy-01cngsM4WI33ZeVrLu5bSAfRnztw0uCqCKjctTdF63ZkApPSNHYBvs1DOmUFTOWJA-1XtHOZFPJbJWgKi4LUBev_MAV6Msn9Il3Bj-5hl8X-hnWPpvHt8iVGXCZ2sTFYWVmRyOApCXWZRBywbxB19-bi5t9ipJdTds_P2Se_2zAMTvNUtyJbEYok0cckFLLaVQcG1hbvgLZYRZ_sCMtxjOvK_B5S5c_Gpba4T2z2T7-RUsAJFaq9pglTlerNGcxqvkP7pq3jUhry5qV3t9XVSFDwSQYKIen0V5JvYqkN2WbzA8bHowy1VtOWPD5w1Yn8Bd7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس هیات‌مدیره استقلال: بعد از بازی امشب دوستانه اختلافات رو حل خواهیم کرد. صالح حردانی بازیکن استقلاله اما باید قوانین داخل تیم رو رعایت کنه. او به تمرینات بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/29475" target="_blank">📅 21:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29474">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cd348634.mp4?token=Rsracwb3ectnY9cBoLysYe0LnTF-cRguq7_f2PVXO3IUtdyxMxWwT0kwv42SbauZnS04xtqtw9i0lCcEBEJOvs08VjyxKObY-jhtcSs64KbmijSCRfhprUekawoqP6Bu3nsLFyrjOA49SGDdfoadqtreP2GADn1SSK8vmALXbN-eGLnIq14zC93LNAPiMjEng7HdZpd2N8sX_7jDynljQiHUzYhn9TZeYPEb9oImLRgekH6aESfmZ1sdFq9DrcCaxffj2H7lPxVJxsK9zcGR8mbzoVJkbAH1BprMdFZR2usX_o-mRLI7v1lnh_6VkCT_-FZl4wA2vrkDsus5ADZn8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cd348634.mp4?token=Rsracwb3ectnY9cBoLysYe0LnTF-cRguq7_f2PVXO3IUtdyxMxWwT0kwv42SbauZnS04xtqtw9i0lCcEBEJOvs08VjyxKObY-jhtcSs64KbmijSCRfhprUekawoqP6Bu3nsLFyrjOA49SGDdfoadqtreP2GADn1SSK8vmALXbN-eGLnIq14zC93LNAPiMjEng7HdZpd2N8sX_7jDynljQiHUzYhn9TZeYPEb9oImLRgekH6aESfmZ1sdFq9DrcCaxffj2H7lPxVJxsK9zcGR8mbzoVJkbAH1BprMdFZR2usX_o-mRLI7v1lnh_6VkCT_-FZl4wA2vrkDsus5ADZn8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مهدی طارمی در دومین‌بازی‌خود برای الوصل 70 دقیقه فیکس بود و درحالی که تیمش 5 بر 2 تیم خورفکان روشکست داد نه گلی زد نه پاس گلی داد و نمره متوسط 6.7 از فوتموب گرفت. هفته پیش هم دربازی برابر شباب الاهلی نمره 5.9 گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/29474" target="_blank">📅 21:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29473">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kuc6kJLety1KXiXxNa7ea4ZQpI41feil3IVjLoHV5Jyb0Nlqfq_vdvpNQLYEAZS5fhT-73T4sCoNjvjDI7O_enZ1LbjHaMcb6OUHuE6pL5gN3eRnSbm0LBLQhxnk9yIdJ4AJQPBmKnay2VhJyPg7Cou_zdqGtG6xRk4Hb0Tz3gAXa67HVR1FpHM1qzTB6M_RQjw39bB-34ttI4hboVzGBbo4F6wKJc0zf0Tk9qjsa3SycBUbC2ETo3mWFtSyyVRyfL3UTs-LkDEZBbcpnBbI5H8Fljxys6BTnv31TOoRF-I5kcQBDkBVYAJNn18iZCCmvw0hUhp0_etfVsbS-P8d-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو گل آفساید تراکتور در بازی امشب با استقلال خوزستان که طبق گفته کارشناسان گل اول به اشتباه مردود اعلام شد و در شرایط سالم گل شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/29473" target="_blank">📅 21:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29472">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1LjXk6mbL42de3QDUY2jcQpIP8Q07QkisbNQ7nN00cdhU1zGA0Y8SAheKpmBo_2PQ949Br97c9lK7ftQVc8yeb0RsjgdcF_124hhhNq_uCnWrcUZsE3ST25mOktEYTLerDiU4EcGwoRG3CsfRA5vr5ApHEUGSqoEUXKzle4k7hbqC7o2XSeeC8aR8dvDluT1JopUEFC5ixLaNpm3SmjhfevGkE7J0Rvi4EZLxYEkbTavPDNhf-LgDPKqMWqKb3Se-sv5T3Q7q-JgtkVD76ZCe1HTfXJDXtn-DV_ywvCsCVHtRpbG3FYMaSzuRShy2bqSUkYiJCjCxyh9FEbG5v8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم لیگ برتر؛ پیروزی سخت و نفس گیر آبی‌ها در قلعه حسن با گلزنی ستاره آلبانیایی؛ آسانی سه‌امتیاز بازی‌خانگی‌روبرای سهراب به ارمغان آورد.
🔵
استقلال
1️⃣
-
0️⃣
پیکان تهران
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/29472" target="_blank">📅 20:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29471">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7Ub2vGUWHAUo8rvibK2NXa5S_F7pu4EDYdpkuaqzBtXiqcsEWmExvQFSTbebf01gHq3eeNaNBYqJnzeNu68_HjDt_qzgdnXnvXJefg5Y1MXIT8ZPQPHsM-hiNO8qLdh1E4kLQgk1HUDNwNhxW_aFSbOK0g-RFr0qDZNGfGrwTE-7jMWoeLA3u-1GoDL0bzTCVH96uOgAym28bCDfiRXEHUM7KTev0vNYGv8ZwnAS2ieoXSP6HZIwatNzz-PvwBgHuBVcNVlAt_vJ6GEo6Ks7C3vJGopIaPKziNeo82vZApJ05-W-YE-Zs-iJF6nWe-HwWduz1wcMEkDWFwGPYJLDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سومین گل وینگر خارجی آبی‌ها؛ گل اول استقلال به پیکان توسط آسانی از روی نقطه پنالتی دقیقه 76
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/29471" target="_blank">📅 20:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29470">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399d4e43bd.mp4?token=PWASY6yjGT8X2aySqAQLsNTZo7lvsuBJJl8FitzTnmJMBIaoEmUwFNsmWc6YgAIOcNR5F0dBQW7CcbbKdPAKH0XCtM1gFmB4Oc64eTk7Eq17o1qwEDqijTnWPkpur8HUWkqPGZ_Qg6obGie44Mc3XQVh-sd-jIFkpwDoJx2FMrZ8FR7DFkj33Vu_ZOuELR2DHryQoDu4xYkatRjaH48IFreqrdz0MVJjQRaJJN3KfKYvGuJgFNTjInP-HxL3bz2WMs56trZNDrw8JFhX090oKK5G-A9CtFZGms4F6FaS6dO9cRSdWDsRdG-etkVEnpJCMXGoqjyxbACIY46hLYW4XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399d4e43bd.mp4?token=PWASY6yjGT8X2aySqAQLsNTZo7lvsuBJJl8FitzTnmJMBIaoEmUwFNsmWc6YgAIOcNR5F0dBQW7CcbbKdPAKH0XCtM1gFmB4Oc64eTk7Eq17o1qwEDqijTnWPkpur8HUWkqPGZ_Qg6obGie44Mc3XQVh-sd-jIFkpwDoJx2FMrZ8FR7DFkj33Vu_ZOuELR2DHryQoDu4xYkatRjaH48IFreqrdz0MVJjQRaJJN3KfKYvGuJgFNTjInP-HxL3bz2WMs56trZNDrw8JFhX090oKK5G-A9CtFZGms4F6FaS6dO9cRSdWDsRdG-etkVEnpJCMXGoqjyxbACIY46hLYW4XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/29470" target="_blank">📅 20:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29469">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6898eb4b.mp4?token=dla1beoX0-sK-rVjwqagANuf85Pznv076FB9JJ6Zh9p9e0ZofAk0lZwUZyuh2qQNzgxtaGf2Kg37Q1QXm8d-uLvPgN0eUUsjDnVI_4lrulWPU7sHcppHGTzA22eVUmKPnfvhb-WE0p1vww7RBbc5nr3FNdcOgZOFYfW5lpMJt68IDjgmdG_tj26IkE8D4kSehIrOXIBpmD5huvVTVN8MWJj-gUUQvuIsl7IvGHMHbPZfe2ljsvAu_pxoqUgG2v1hUy574R0Oz0wk9Ly2nPzz94KOdTbLbehnaAyvChe79St8oiPpt9e7Mz_JAg7-q9wmdj3EbTXbyE2kguRrQX0wWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6898eb4b.mp4?token=dla1beoX0-sK-rVjwqagANuf85Pznv076FB9JJ6Zh9p9e0ZofAk0lZwUZyuh2qQNzgxtaGf2Kg37Q1QXm8d-uLvPgN0eUUsjDnVI_4lrulWPU7sHcppHGTzA22eVUmKPnfvhb-WE0p1vww7RBbc5nr3FNdcOgZOFYfW5lpMJt68IDjgmdG_tj26IkE8D4kSehIrOXIBpmD5huvVTVN8MWJj-gUUQvuIsl7IvGHMHbPZfe2ljsvAu_pxoqUgG2v1hUy574R0Oz0wk9Ly2nPzz94KOdTbLbehnaAyvChe79St8oiPpt9e7Mz_JAg7-q9wmdj3EbTXbyE2kguRrQX0wWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماتیک ترکیب استقلال برای دیدار مقابل پیکان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/29469" target="_blank">📅 20:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29468">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d96077f7.mp4?token=cQKz5xMye2Cio6euvzq6_qmOKKzuizVIXc8JE7QGTkcQwGJ-UEdE8SdFTiOOOv5VFamydgCrpdJICRSvwdAocD04EG2ta8iRqrk_JMcqRf7fbsSR0M47O6W_6gCuzmRgGtmpI6hvbrf5sWK754LUJb19tWC_Dxyf8YRybA-ys4J38y-YQ1TIfFh-UEka9psrbVDL-YBMpc-sY3jNIo59NelQrF0EVRMvS99JEX3kH6iugS5l7-zZQng7Q7P-l0lIHoPk9nGUtnPQTZ-K-ASVYvpltQxZX_6FE3fg38Uc_Gl9s3V2sKeUNB2VNGlxag7fxnMEvUwiHdKJ5p9VPMlx3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d96077f7.mp4?token=cQKz5xMye2Cio6euvzq6_qmOKKzuizVIXc8JE7QGTkcQwGJ-UEdE8SdFTiOOOv5VFamydgCrpdJICRSvwdAocD04EG2ta8iRqrk_JMcqRf7fbsSR0M47O6W_6gCuzmRgGtmpI6hvbrf5sWK754LUJb19tWC_Dxyf8YRybA-ys4J38y-YQ1TIfFh-UEka9psrbVDL-YBMpc-sY3jNIo59NelQrF0EVRMvS99JEX3kH6iugS5l7-zZQng7Q7P-l0lIHoPk9nGUtnPQTZ-K-ASVYvpltQxZX_6FE3fg38Uc_Gl9s3V2sKeUNB2VNGlxag7fxnMEvUwiHdKJ5p9VPMlx3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
هفته‌هفتم لیگ‌برتر؛ شماتیک ترکیب تراکتور برای دیدارحساس‌امشب برابر اس. خوزستان؛ ساعت 19:00؛ تا قبل بازی امشب کسی نتونسته به تراکتور جواد نکونام گل بزنه ببینیم امشب چی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/29468" target="_blank">📅 20:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29466">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7pqlaHnVZB7HBZnq3Yc27n_evPzM65FXzYRrIx6ZoOfAtMAA14JzNQrrx9wte1T8JnCAIcDX3vVtHQxTLJwkWN5bHs5HSEkg3czRDPncTBYuvDe9ylUZr4VtJzRYk65TXMoEz8TlZOgz7Zf66heZB1T8K2rd7urz3JNEDLBvsf-2yQ58enN8dnnDFknJvnnfIDdAUY9O1bzdW7HP7-P-xyFso9CnrvRk0OsaKjWG-BpTbBbyK7WdizzNWRbRHXkysfs1NFeinGJehXmtPdhiTQ9PAOV9i9vwEJ7a6y0toiNgxuIlG--sNE9o4zkOCu1BgH81r1Gpc2NMNUqfv4iPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjwX6keEv9kFxT6RsCosYEPU8TOl5YwGGEzHrDIJ_WlFCJVny622YUiDlJkCm5vUQgZy8E5uDLtAowI0KKKTNMF5lVe-cGl3lrkSqbtYPRaBVSNdHQegCm26ym8b1bxN3sUVeEFt1Q7FU95xnWGs1aCLkjx8vJmj0c0vJ5jDXf5W6ZfQKPdck4MOgJa8tLuKJJi8ES3EYRaTTr8Vv1pnQkMNl_z9GIk0PrOautSI170VpU1sS2hsXazYk9WnB74x27cg-f5oSqEgONqk1R8ONubxCierUAKuM9TY7EoECKX5AD68ozA1_rIepPBJf1jr8O2zwGkmluxkUHwRNtoSRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/29466" target="_blank">📅 20:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdvMzebALwKQGZ-AtzmRDtQkStJ1yIwOrjrJgUaWM2UF-YtS9izbZtMXtJKUu4VrvJMERMT9z2TVBaPKQu6dhDApbswmlVumIJupxYwbSG9tAKUlsX9gB739VPy_tZZ3kkBlgsYZTkkNJIBWr2jQ7n1x4YoXV0_kXP0bGYM51Lg3GaZOwUfvLTmh2ASt55YRshBUOkgfUX6VxkaWlC5T7DjqY1wLqHiODFZFkhHFXMqU80G9W6_FO7RpG4BDRStsAJVZZaSRM4Yml13C0-mgg1sgT6kUDOg3F_aYdPugtU3zgxGdVekY2pI_R9rRqAhwmOE_Oy9anWFacLBT2Bubpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/29465" target="_blank">📅 19:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgqQhzu4jgcGS9mMRgP0V5WFz1Ac02f8otLjjeG3Nco8ZAY9YcKFHwwAyzn-s1BwVMWYfowF1tZQhOByfsYbNMReuH-7DbC2k8f2AFah-nhmeZTIxJTsD-jr234CzSWCAbeZD6vsQ_cEmLhmLgleWdHgLs73BqZIm7z8ex1Iq8rV1ehTbKTcIVP96iMKOBJ_kWQphCOUG_TVqThoP-vo02mmYeUQ3-KiNJB4_IA6gb6ydV1ivE4whxyujQsris0e3nX_l-oZPBJ1uPneAkESFneIy5V3vcjJTMSMXLtjcm-9EtJG08OmQZQGVe7Nix3fNfvtlsG4Xi3r5Mr7LcdfMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویو توییت جنجالی وینیسیوس جونیور در سال 2024 به 490 میلیون رسید؛ وینی بعد از اینکه اون سال توپ طلا رو به رودری دادند یه‌توییت‌زد و گفت برای به دست توپ طلا 10 برابر اون سال که با رئال مادرید قهرمان لیگ قهرمانان اروپا شد تلاش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/29464" target="_blank">📅 19:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk3aTE8VjVvcf4HqV_4RVYRxn7hm7WSQs4hnnOXJKhWwyR_Z2dKTWIQXJUqTod0OpPOFbcGVTmUDCrUzlut1dIZrg3J5TMI7fqjntwfj-Lvllv5x3fT2QBc0D2_NXFn3bfn9ZkkDtXsePbql7RWo3LnI0O1_zLNPmAa3rlLhHEqgE8pNn6Xc685MjngKiFNMOXKOikaRc27hhGmBFs63baeK8Vi589Lu75Lv9GHksr5nahEBj2jumGIaEAkpiVEO2cnWiWpuDfIGuyjIsR4EfBVSFb2gR5CczzXp8XkkRKZ1F8qD_1lS9DHhdGQYavIshcwVNHm7TqODPGjqxtHFUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های تیم ملی فوتبال ساحلی ایران در جام‌ملت‌های‌آسیا؛ مسابقات از 28 آبان شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/29463" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf5ffd776.mp4?token=ZhRz7BOOUtDlKwmVchmBFc1qsdGkH4UVydxSocPp_E_FtsgkBLlbQfZ9jb3pMl-ipcjl-yVNuW7QhPyp0cNf7_lGtJEAaXx27XV2ziHHXGFyDgoI0sWKLlSXYEcA2bwXnPH0LKu9flbG43cZEmQ8--kTyxKK5kYCdjGYOB-A3YKKiRRKqyYNeC0Qiee3YOQNrojXCt7KjdiL8PgH2SzJjHFDj9XPS85vF_mvBmtG7mLC3RNNlD3vTtDU1D2J3Ri-Ad1uEzhhuLjjpa5wK1-a6-HdLBqCerAnj5K3HG3aQbEc9x66dM7NJ44rzFlO--9JWca8tjG-uECgY3xfgG-c-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf5ffd776.mp4?token=ZhRz7BOOUtDlKwmVchmBFc1qsdGkH4UVydxSocPp_E_FtsgkBLlbQfZ9jb3pMl-ipcjl-yVNuW7QhPyp0cNf7_lGtJEAaXx27XV2ziHHXGFyDgoI0sWKLlSXYEcA2bwXnPH0LKu9flbG43cZEmQ8--kTyxKK5kYCdjGYOB-A3YKKiRRKqyYNeC0Qiee3YOQNrojXCt7KjdiL8PgH2SzJjHFDj9XPS85vF_mvBmtG7mLC3RNNlD3vTtDU1D2J3Ri-Ad1uEzhhuLjjpa5wK1-a6-HdLBqCerAnj5K3HG3aQbEc9x66dM7NJ44rzFlO--9JWca8tjG-uECgY3xfgG-c-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
پاس تونی کروسی هافبک مس به امیر روستایی که این بازیکن قدر این پاس برگ ریزون رو ندونست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/29462" target="_blank">📅 19:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb94cff9a.mp4?token=DE_hIP2VtMGUIkkrzgsPvC4g47bhwTJes5RveLLJ8mlEtD6YkabMFsmboCYdH4VqIgRZmlRbtI9D0TFMVlGIXuD7mVjYxS2cI6_B2n0D2A0m3IylqbWA5uGY3JjtiM29dP3J9WuP195rRF4Uqpv-4kc-kgp-Te1x-EHJex7zGDWeM4ibQHxgDpQpO1Wn39WlZRh2MB802jbVSWIyGgINrTXYGDV4XsAbur4BauU2drn17fDsyMlBNJV9jzlNIjeWUIgdb2z19aY1WPdhipOjjqkmhBJt56rU4UK0KAlzsd6rC6EfPlt-IfnpqEYkqCcmyNRmiJ5hFj-p8KSOyqxkUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb94cff9a.mp4?token=DE_hIP2VtMGUIkkrzgsPvC4g47bhwTJes5RveLLJ8mlEtD6YkabMFsmboCYdH4VqIgRZmlRbtI9D0TFMVlGIXuD7mVjYxS2cI6_B2n0D2A0m3IylqbWA5uGY3JjtiM29dP3J9WuP195rRF4Uqpv-4kc-kgp-Te1x-EHJex7zGDWeM4ibQHxgDpQpO1Wn39WlZRh2MB802jbVSWIyGgINrTXYGDV4XsAbur4BauU2drn17fDsyMlBNJV9jzlNIjeWUIgdb2z19aY1WPdhipOjjqkmhBJt56rU4UK0KAlzsd6rC6EfPlt-IfnpqEYkqCcmyNRmiJ5hFj-p8KSOyqxkUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عصر پاییزی چهارشنبه از مدرسه برمی‌گردی و تلویزیون رو باز می‌کنی و این شاهکار رو می‌شنوی. یادش بخیر واقعا اون روزها همه چی بهتر بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/29461" target="_blank">📅 19:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1961c125.mp4?token=Wv41oS7biCWKXVnwpBfS2tVEOZjHCFCUzIStzRiczseA9K-w9gpLzR2VG5LBnIaaDalUjJX70urQrOKZERJbaosqsH0sZUl49xLxOheVkJinSDAWQanSbgrej2uZqjq4npHp13bEU0Zz9JHwbEbECjWH7LypJJyGyIQz47JN3GP3xCgGfuQ9Y8WIM592T60Gu47Bs5uVccVb81uq8-OXZLgLobiFKZTMkxPi3pOvm21YPnlAw5oTrAhdc6VuwDJXmvP8tA6-z1TCfVuHDfsoxNRJKA_svhRGApNol0dOp31NN4rRPMPl0UYhwDrwPg_OWzAGhkjU8LXpch02KMPInA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1961c125.mp4?token=Wv41oS7biCWKXVnwpBfS2tVEOZjHCFCUzIStzRiczseA9K-w9gpLzR2VG5LBnIaaDalUjJX70urQrOKZERJbaosqsH0sZUl49xLxOheVkJinSDAWQanSbgrej2uZqjq4npHp13bEU0Zz9JHwbEbECjWH7LypJJyGyIQz47JN3GP3xCgGfuQ9Y8WIM592T60Gu47Bs5uVccVb81uq8-OXZLgLobiFKZTMkxPi3pOvm21YPnlAw5oTrAhdc6VuwDJXmvP8tA6-z1TCfVuHDfsoxNRJKA_svhRGApNol0dOp31NN4rRPMPl0UYhwDrwPg_OWzAGhkjU8LXpch02KMPInA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/29460" target="_blank">📅 18:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a4f9a05ab.mp4?token=Y9RFJU97XDfS5IF75ym474naB2delqGpP-wd-KsFHn0OVUGguJ8G9L1sNrQ2FsBRbe6nQnZFhegy0kGERXgTIXF37cHZ2PwGCqOywZiiuISqh6akyS-XqIlS3d0H6ONTngObc_Dl_BYDR8A6Q6g1LVAwNAwp--JJqV13oEwdMYjYd5pPHS6sSE9oVXf3jGJVbu6GtU9XdHLMLGmszna8vQ8nhkhBjEoJ-H-ODo9DZMjfGfmKUyUi6fTL1Icd0OPNrVMEKLg5dRkGzY-sIxXM3YRladsctlTNnp-y333GYBUP6DnT83kXEFH8SzCqJ1eM6E_OzVuVvHSKjk0y0uvUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a4f9a05ab.mp4?token=Y9RFJU97XDfS5IF75ym474naB2delqGpP-wd-KsFHn0OVUGguJ8G9L1sNrQ2FsBRbe6nQnZFhegy0kGERXgTIXF37cHZ2PwGCqOywZiiuISqh6akyS-XqIlS3d0H6ONTngObc_Dl_BYDR8A6Q6g1LVAwNAwp--JJqV13oEwdMYjYd5pPHS6sSE9oVXf3jGJVbu6GtU9XdHLMLGmszna8vQ8nhkhBjEoJ-H-ODo9DZMjfGfmKUyUi6fTL1Icd0OPNrVMEKLg5dRkGzY-sIxXM3YRladsctlTNnp-y333GYBUP6DnT83kXEFH8SzCqJ1eM6E_OzVuVvHSKjk0y0uvUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا از نزدیکان مهدی‌قایدی؛باشگاه‌النصر در روزهای گذشته قصد داشته که قرار داد این بازیکن رو تا سال 2029 تمدید کنه که قایدی از طریق مدیر برنامه های ایرانی خود به این درخواست‌پاسخ منفی داده است. قرارداد فعلی قایدی با النصر…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/29459" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29458">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/071cf92014.mp4?token=a4Ont0u32AFyQ62bHYFgY5HZFkfG-H4xWp15kyL4W4F9nrVqOEsuqW73HVMK_QleWMt312Y2QCYg7I1KEFUkNanZ-2Zmvo-wJWAUSJvUmkzgOcfUZ77E3SSRlt72wmoMsvcYLOqcC7jhm5FwUPDEdU2p9zHh2zcxIxYsU8imFxnAk0YIFiG95DPFZ0lR87OS_e67TADSzhnA7olVQ216fxpeNH65ifQIhmUBLwcUM0maslt1dbxzYkEoObc64cHLVvGQ0h3Vg5hoTMSGGG82VGYu_u75felrqvYM6DC1eHKlS-zX7e0-Ie8ow1myxonSQRN-OeTjnntVfS3FFnQyim_HRDvOwLK91CB96KFvgzFHycQGl_5qqFiUox540zhf_RgEzkNX2JDno4LAvAi_aCpREcDlPzzPJzvFybldXlWeo4d4WERcuBYWe6mO1N03FB8Nbqj1Nx0A-6wa0QdyomwyWFDOi_SSAjvyEwFQvSK-WDzhyaaHzP35UIvjGKXLvsFYbXPJ7lhcHGHzwkRuWvXKLOaixQbt8S5kMmkQ_nZhZk6dzh9i5c7crar-OA3yhPwckpZaL4cdedIe5TOF2ZK7KSEwcPr0cStSJ_vBU_RecoFWuVDnSCS5Sj8Uxa0JRvd4Y0lt-5xwKvIWAzpfOYNF-uAVrEcJtK1POvElSu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/071cf92014.mp4?token=a4Ont0u32AFyQ62bHYFgY5HZFkfG-H4xWp15kyL4W4F9nrVqOEsuqW73HVMK_QleWMt312Y2QCYg7I1KEFUkNanZ-2Zmvo-wJWAUSJvUmkzgOcfUZ77E3SSRlt72wmoMsvcYLOqcC7jhm5FwUPDEdU2p9zHh2zcxIxYsU8imFxnAk0YIFiG95DPFZ0lR87OS_e67TADSzhnA7olVQ216fxpeNH65ifQIhmUBLwcUM0maslt1dbxzYkEoObc64cHLVvGQ0h3Vg5hoTMSGGG82VGYu_u75felrqvYM6DC1eHKlS-zX7e0-Ie8ow1myxonSQRN-OeTjnntVfS3FFnQyim_HRDvOwLK91CB96KFvgzFHycQGl_5qqFiUox540zhf_RgEzkNX2JDno4LAvAi_aCpREcDlPzzPJzvFybldXlWeo4d4WERcuBYWe6mO1N03FB8Nbqj1Nx0A-6wa0QdyomwyWFDOi_SSAjvyEwFQvSK-WDzhyaaHzP35UIvjGKXLvsFYbXPJ7lhcHGHzwkRuWvXKLOaixQbt8S5kMmkQ_nZhZk6dzh9i5c7crar-OA3yhPwckpZaL4cdedIe5TOF2ZK7KSEwcPr0cStSJ_vBU_RecoFWuVDnSCS5Sj8Uxa0JRvd4Y0lt-5xwKvIWAzpfOYNF-uAVrEcJtK1POvElSu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
👤
ویدیویی‌از آنالیز عملکرد فوق العاده علی علیپور در فصل جدید رقابت‌ها زیر نظر مهدی تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/29458" target="_blank">📅 18:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29457">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dD9hw-HKSqb9QV-rTNP2eq9GQ6oDSe40vga8NzKmAXMhxa-4eq7899QSDEpBPK9H374Jne_gBqGWvcWKBaGl4BsmgqxzAQec6TBlbsN7E4iSgWahXPKBkEV8dgTAZbFRdPu0FXzb7C9bV-b_eW__1PT1Js-FhvLDMR3Hf81WADm0TLHJKthUChvv23o4ohq95ajAlCeIO9-596ecibD3ascS2Q6KD0J8e1qbjaQzeZkqVgmDiwjwk3C7UadprIEaf8Eae9e2eIdBq37PVXSSvXQKngLa-7fnoZAM43eN_Z61UqjXH9IxFcf1LRL8uRWS_9_Zladyz6934VB-GM8FWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
هفته هفتم لیگ برتر؛ ترکیب استقلال برای دیدار امشب‌مقابل پیکان؛ ساعت 19:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/29457" target="_blank">📅 18:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29456">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzyVwQfS15IzKMbDxK19FEamGDggbnOlM2b74NkdCQ7DaSq54q3CvjSO01bBugx0eziJnqMCtAG_w02aNlw4lNLbfLskkk54f-n6kaeznHicNhedHNKCLBl7Wxu01HLZ84z5gdrT1CTd1aOrEeeZjmT_Lgx8eQ1LPjJKyHSGDise_hBNaT__W0-qqgOLDyYwOI_LRuSx90iKYAQNqUuFwAAC2FZYWAST3V7y0MqL6v70H5ZQgiuppHiEc2UJt8v3v7JmGGt8L3yfV-dF_o3BAigHn0ICCAdWZMuGYG1rB4_4w8iZyOl1abFZ-dzcUv4075Qx-SSPXsm1uaL-gJWMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
هفته هفتم لیگ برتر؛ ترکیب استقلال برای دیدار امشب‌مقابل پیکان؛ ساعت 19:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/29456" target="_blank">📅 18:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29455">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f74RI1WL6YdX6PNLaVIHSeraa2-Uc3SMWlwBPI6WGpgVJZP0MCZAA5VThIuih3TAzbVAkD19fyuYjJ_CbJtEiqiVuxMuEnGOfKgqULMvlZXMY7MwDIczZOUdwQHtFPD5WWaZuaW22q1xTcaKQSCZr7f25psU7-EKLwu6W2JB7mf0WOjpRTmojF8OpUvn8CR3X4GJeZ44rHv2Dc2YwzkFO4A-C28VfLA7KrFF1y1Uj_ubgJTPZIHkQHh0Nz-yOGunyP7gUBxxOO9z0b_1zl5txGZXOJC6KoYBbDvsKwivMp_LEZlilWg2tGXAdZJEjqj1g1UcVZ2BRQf1rCaoOvZ8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/29455" target="_blank">📅 18:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29454">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYBgrq6G0rKxeCW6ABUaVDTwnTASaqJx3Lm1TMt_FNsLtuKff6RRKvHhgSYGXiOinBNR5hj8tsDGmFtyUPEzzbudMpXwIpPM-W1LfUtfhei4RkkAD2mgCQMngcyNc3EC74s0AgcqR_Ag5tgheiAG3PjD9k6BdUv0b6PaFmJd5m4j_RHB9mDl9QS_vAEibDvbIZciYSA1xG0_WK0YNAv5_zPF6n04blqW9oskTMC38K8ejPhyvbDPVlryUPZF3UlfVJy_C5TTRwzKCbzROt1LuD3ghn-Wk2FhBMfZzjVjzCtxXRsCPuCWx8lCbCvhW3dPZCwto6uz24L1ia6gol12ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
هفته‌هفتم لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدارحساس‌امشب برابر اس. خوزستان؛ ساعت 19:00؛ تا قبل بازی امشب کسی نتونسته به تراکتور جواد نکونام گل بزنه ببینیم امشب چی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/29454" target="_blank">📅 17:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29453">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VThlg64qvBGu0zosifBGQkGMJtAwvFa_lanvsdC3B9vjXOAVaNdTKNEsdR8R2wk74OHtXYhDitghv3tFF3eI8Ja8LxOWqv-F0TW_eHmnJHIb_yg-oABzjcIOYHnna0IVaxIErTjCybA_hbsFZr12AawLVz82t-vzutEK-lRqPRJe-cj3MS4AwhuSnAEjccGuuVKerPEUT7qiTp7xDlHS4WmbsXuJrIzcgt3ItadD6B4iVfu2Hpk8chknjv8l-Z1bKpsq-lxMI9uSFzRUSjGzngXjH9jYKFhQnSaJSZWJQF2DJ8IcK2Vtk-hjL88f5F-4_KXfcmnU6f48DaUtY0VOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای‌نشریه‌کوپه: براساس برخی مطالعات و نظرسنجی‌ها، هوادارای بارسا تماشای بازی تیم هانسی فلیک روبه‌رابطه‌جنسی در زندگیشون ترجیح می‌هند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/29453" target="_blank">📅 17:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29452">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2-VmLDSxOWyiXAsM7-8i8vucY5ybzaIr6MnkkdAozCiV8woxK2PwQGk9W7SSmWKElJvY9RttUFhjyHF9906KL91hLjcqzct9HS_yMFw54l5pPbD3217sJmMds7EKVpHwyN01pSRMiuRLjRm9kIHelmRywz9lcIEV-RKoHojS7Vld1PE9663CcoEiolRfHSNaEYGCZ15sPcdweq032qByjqnE09C-x8nhqKLB8ss2DHydkNBv452Tss7a54ShvJX4P8jg0Bwo671JMYQ3hDihccXZyO2HTxpto216e51pxb9xWR3J6JT2hihRhTpxZk-FwJt5g5CudT0rDzwck7tjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/29452" target="_blank">📅 17:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29451">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX8hc2zlKkolUd5TmjYtVy0SdE3k0qnB7n_jR2GiVOivtoPg2BUmI3dkVmKzHzFLDPIDc9ovJSwq1Pe65DtKGybNsHMKciwzbiiX_4O5V6Z9exiSaUkbE-wH7G4GBwRGx03og-t2gpgpZNY7yz3fovBlNHQknwWb_yUrPUVUx9BH9uTJmg6nRevfhsOzEv3INkWNp_r78q-hrgixH9P3idqTyz6b89Urx_mqvZXWx_bpljwFBy0Z-BUyqE8kv-40dWDYt3T-NxiAWyK2sGpPg5PuhLMv4_GVxxx6wDgxD0jz2O9_CMfeUrYiCeDyllZNrn4ZdydFDIcUZTFiFrdaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات؛حکیم‌زیاش ستاره‌مراکشی سابق تیم‌چلسی با عقدقراردادی دو ساله به بوتافوگو برزیل پیوست. دستمزد سالانه زیاش 700 هزار دلار خواهد بود. سال‌گذشته‌ایجنت یاسرآسانی‌تلاش‌ خیلی زیادی کرد او رو به لیگ ایران بیاره ولی شرایط مهیا نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/29451" target="_blank">📅 17:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29450">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a53c9dadc.mp4?token=doLqVnSDr0cccPbqBeN73XCXwplfjlcIAvfw2B3z66Fgw8US6_8uuAwWBnd6Gg4mBEEFqXd_-rfaXmHiK8CPm3ZtLj6IH1qz-kK1mfEMQ6597GHBeCdiTzY0Wt-bcQU0bVPXGj_5aCtWNYi265ih-qE_CNVlJWFLXS-jRz6b_h1mxVGb27EIBGPr2pii-9KuP-RUixsq62nsMzoVW9SX-L_ugUgQTrvj78pO_WeO_ClWDPJJjHhN2lQlv-zaZPZeuffIGEnGgd07VDJkudnJluKQt7DuCLsn5aDACVYEl3R-P1k94C553iI-ykheDvO6Rvf8nrasXo_SooBqhe6ahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a53c9dadc.mp4?token=doLqVnSDr0cccPbqBeN73XCXwplfjlcIAvfw2B3z66Fgw8US6_8uuAwWBnd6Gg4mBEEFqXd_-rfaXmHiK8CPm3ZtLj6IH1qz-kK1mfEMQ6597GHBeCdiTzY0Wt-bcQU0bVPXGj_5aCtWNYi265ih-qE_CNVlJWFLXS-jRz6b_h1mxVGb27EIBGPr2pii-9KuP-RUixsq62nsMzoVW9SX-L_ugUgQTrvj78pO_WeO_ClWDPJJjHhN2lQlv-zaZPZeuffIGEnGgd07VDJkudnJluKQt7DuCLsn5aDACVYEl3R-P1k94C553iI-ykheDvO6Rvf8nrasXo_SooBqhe6ahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
صفحه‌رسمی اینستاگرام AFC با انتشار این ویدیو و موزیک تولد 32 سالگی مهدی ترابی هافبک مصدوم‌تیم‌تراکتور روتبریک گفت؛ ببینید چه اهنگی براش انتخاب کردند. بیشر بخاطر آهنگه گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/29450" target="_blank">📅 17:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29449">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG72aKJ9Xhq8VQKMZNVY3YKWmdcIroI_Tcn8ovK4YqtMynhlaW1Pszwe3IisBfWG1qs57aPPdpvydontXWzpo6FlrPcdXCcQoo4y8lGIJpr08Bb39PNFxZk6rU9kGPjBKHGmmeV3Th-OGVMZV6BthUddRAsMnaZjUZelMG9A6tCJcopCjg_IMkwnmDGOsVRDrFsoSUeJSO35C16PrJVZMVKpvCY-I-l8Fg_I9luBEloWifkNEHHRYQzQd4wF3vjQodUfu1ya61P02IPYrkBVh9A7M8BEmq0krG4PwfKV7AN0DeUBa0IbNUXVzYntJ6rDAAogHBsjYWBQOgLZCqlulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
قیمت جهانی سری جدید آیفون 18 اعلام شد؛ آیفون 18 تاشو قیمتش حدود 600 میلیون تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/29449" target="_blank">📅 16:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29448">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKx1nXOrVt4tiHu8in_ef72Kc6xNfxZ6AyjTRp2Odj6oH3-CVGK-vuYYH8V0_m1cqoYOQ9QSPUQ503CNmBEr-aDjynQLrT5NQQmg0Eb7ujieDwwrwiWxre1yKMiq4vxOGKPRoLdOA0zEChYa5Mtqi9c2uS5sqE75YkKkPA5yoReu_nhUWHlQ9dd_KqSwhRBqPl5ngjJldDF4dpmU2QJMuCcPhhSHSG68DJBoo_7YDmbR0Y0edCPn_46lR-khiWGinBqiopyDAhm1m59xFIG2lIOMhL35RtwgqcocGJNTBElo5hst5B44lYCcAMx5e8AFcwNzi5N5IDZ9jUzDUcQ7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارت‌پروژه‌جدید؛آرام همسرسابق‌سپهر حیدری کاپیتان سابق‌پرسپولیس رامین رضاییان رو فالو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/29448" target="_blank">📅 16:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29447">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOqCHwPgFLKsqRogHApMOTYXz5dADR6dlQWlcK77OLhhpyS-0Xy6y2pKPn6EVc8Ac6d7Wf9Cse1i7BTvLs8u46okmKSF52niRBfCkEUtQkxBS3l-vx5NLBHT_3xYNqreHj2V1xmB2ITxnMBGY0SltL2sK8GhLIXgOddOPM6I2L-UKpaot9UQl_V2xNx8Y5BXOvU045KJ9L3Wq5JNzU3dVbzQ7DSdWMyZ0qwrvArlKcT1j-6j1ABfG08MxccJfLvcR-FjemAcTPrOpNrBhES1uh6PKzBSASFZG8yoYCgrMU5e0AsLD5hJaSFskFFvrWygYhtWFYBfgMKeXLjqRgjV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛ مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/29447" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29446">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9wxNfmmQ3kTzRwRdJTwg8PXZHH7GOVyg9H1OadW_0_LoobN5iw3g-Wauhe6f7meRcYl_oTfYTnnDXLtodriejCsqkeMrwRpHh_XTx8M5aGWV5Xo5MZ510LMJM-lk6yX4ZPlQwOVwjK0MNPjOh6qep42yFaCeWZmE_AQrknHYcihel9LRPd1RHMpP9JzKc4b3VrsxwjUq6w88xBJvdtw0LWxoff8DZH2oNgntbpvOze9jJx8PnZaWeypPoV3gUntbRKkXbKEWzAh9gJu6RrrA38MCTPQ77qRtQ2UEwTWy868DWZMEdrnMKn5ta0FiwZr3MLgVq6q4XGD5wFwl2kZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
خبرنگارباشگاه‌اینترمیامی هستن که اعتراف کرده بخاطر اخلاق تند رودریگو دی‌پائول جرات نداره در پایان مسابقات این تیم‌ باهاش مصاحبه کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/29446" target="_blank">📅 16:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29445">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSaDRkKtCnOcL60_runzo6N_S3VrARgMycaAcyWMyBkIITddURKEBUxBiKyUKpOUYNfbcfYNsxe_RIdlRQwtdxm1pH8sQQWCfO5goF9Lw2Em_3i48s5B6cW8PGP8cyeh16STsikKYyD4Zh-YV14W3dFNkuuVXumAdcZ8u_ZtQZlaWirTpfF7pRF8IwFKyVS1kvjwV0X5IqFlBt6EdFdGEG348_eBZiBUS3LknWQmdT9Fjm477i9oIvBU238jqgPfS1LzoGHQdm_noawwULRnp_nJ0_mMPYAPSdru49AUGAwaH_H8q5QTiKMUkGUZMBxz_p4KKwcmUfYp2wDfzAiX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/29445" target="_blank">📅 16:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29444">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9Sno5lw5UMm660rlKoYdCGnE5XzwQ75h9ckDhTK1V4yKxjoOKMWpfN8NSmwhM_jU8rziOkJXDYj0E0SzmATflOiW6V3uCoOTaHKlVS3NdHuXUl01Dk-RKPJMRl66yWg0ahxfnja2sctiSgeUF-VO3vcgbu51JBa83D_pxy_OL-QGxqExnI8vaAv7R453pom3W6GOx5o_ykxZUoaFc_IqMY2HIwpXCFQlDam6z3UCcvPgvP8Cq3XGv96QjoHkC6naizICjT6OVfBrYrVEtKntjpXKgOy8WPBWqI1pyTyw1JZt4LQyxcBwO6jeDYFBpJCQjtv4aKUlqJdfZUmYm8rSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ وکیل‌پایه‌یک‌دادگستری امید عالیشاه؛ با شکایت بازیکن کهنه کار تیم گل گهر از خداداد عزیزی ممکنه سرپرست باشگاه تراکتور 6 ماه‌به‌زندان برود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/29444" target="_blank">📅 15:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29443">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afef3ee6a5.mp4?token=Igk89FLcYBIg2fF9NI6H2dDSGLJITrwdrxEpV4C9bBvJ48MHmREfUCBhxYRzytyfZRbW4XjyA1Z8kPCpHRJof3AvmZ7hRECf1Et2Y-6vjlEumZJehtBQMnbCxTxEm_FR-DO4SWfVRGbM65aSUvOol5Hernqut7AXBIRZThaqQlmvuzX4oHWwnLwLAGPxC3mh5bGpIZSRvZjaK8QGo1n5aK2itzUY0luQAtq3bNoR7gffqguwR62qtdPvBscDJ6H8C1Yp6qaQavmuhZnkCGG-1yp2z4d0p9ZpewxCypA0ZgjyTwWziEhOKw2Ql2W7xs6bnIMKcPMe3sFd0kTpWdGBOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afef3ee6a5.mp4?token=Igk89FLcYBIg2fF9NI6H2dDSGLJITrwdrxEpV4C9bBvJ48MHmREfUCBhxYRzytyfZRbW4XjyA1Z8kPCpHRJof3AvmZ7hRECf1Et2Y-6vjlEumZJehtBQMnbCxTxEm_FR-DO4SWfVRGbM65aSUvOol5Hernqut7AXBIRZThaqQlmvuzX4oHWwnLwLAGPxC3mh5bGpIZSRvZjaK8QGo1n5aK2itzUY0luQAtq3bNoR7gffqguwR62qtdPvBscDJ6H8C1Yp6qaQavmuhZnkCGG-1yp2z4d0p9ZpewxCypA0ZgjyTwWziEhOKw2Ql2W7xs6bnIMKcPMe3sFd0kTpWdGBOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلایه مهدی مهدوی‌ کیا اسطوره فوتبال ایران و باشگاه پرسپولیس از عادل؛ سرنوشت مسی اردبیلی که در ۹ سالگی وارد برنامه نود شد به کجا رسید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/29443" target="_blank">📅 15:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29442">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akViPJsGT9JKWAlndsWPYekXJQxWe5DeB85IaQCPcUuWeS08Ih5tRySBjvR0so1TQTeNYM1whde80LYnl3vw4nA76lOCpLaqiMCgRD-fPCfqNFKB-rnUbMUqXoii-Q0Rt4I28FMkjlZ6LDInaBR9JJnveTkQghitcisvWTUF8z_KfYFIS0A_UyrG3b6gm75_ys6RlvR_wigI-7xwcySLNCwVLrrFkHEhMxxEeXF7nlHzixohZUi0F2VSM2i9yS-jEOIzr2kxhlXSx1YXh7liieXOpNcgcP3Uhr5n_KngB9aLbwRHuAijVVWRqkeF_zuzysywvRyzizWEO1XmB54hZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ باشگاه خیبر خرم اباد به دلیل حضور مسعود محبی در تیم‌ امید خواستار به تعویق‌ افتادن بازی‌این‌تیم باپرسپولیس شده بود که مدیران سازمان‌لیگ با این‌درخواست موافقت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/29442" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29441">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzXdtmSeimnP1sxXtuT6A6tiO6ndRRv-NzcMi--Df8X3slXp_IxRY6e4T2Sga84h9ZfkKHTX8648PraxOjyNL0YOqCR4i60q1qeIOrHZeuMKz0zDgaTcpKmBN1_TmbmIl1fJKxzaGOe4uekWh5keWsE8qtMFZQNiJtr49eKoZ-cKV_WCbuvmD9gdSIEjEw1m2y6JQdDKB_-nkeGT981TqvDGM4WSRErPQ2wVzHQVYGQiu-bl_q54eaZcZVB8LtaHSPEvhMjopiiy9h4Cmy7zkXNeqO2OkG57-2sNP7WwEB7bailLmsAcZLoWuXROPUOzDA6GzTYiTlghQnUO3b7vOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولی هوینس رئیس باشگاه بایرن‌مونیخ: فروش اولیسه به تیم‌رئال‌مادرید؟ ازخنده روده‌بر شدم! حتی امپراتور ژاپنم‌ بیاد پیش ما اولیسه رو بهش نمیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/29441" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29440">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAzAq0rNUQqGEBeXHaPd-qr3naLVFz2mpKiWHrEsnTY2no-r7uqyhcG1wMBb9TKHSSR0_yUr7pQttGuqQCB-zgm8Vs9dhl_JLFFY9zhfKWoWwqCFuxaU8V_VKsr3a4mN12171PfLyfw2L0fm5PJlMF4DBtLDO8m5FfBivE8pAMFS0Pk8FllJCivwKwTCxS_yYCl90OCSMIMOcFrLzgJFHqw09bcJmYQZTcDY7bOIJrMUos_2KUJbLMdd3_57AQrAnRBz6vrcAXnxwKHg1YuB3dNoRJ8L0pGZqZ_cwnC7Qi0Yyu6xKi6begF09YFIEDYsKc_mSgG8hhe7HSK577Ishg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته هفتم لیگ برتر ایران
🇮🇷
استقلال
🆚
پیکان
🇮🇷
⏰
ساعت ۱۹:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/29440" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29439">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYMfRMUDst7tAj24tmJaRBNzgcW0QcRW7umnl8oBgic-2jFzDNBu0P6wjmySOQgucM2xNgMOAOdox9wmFI7e_UmhQtSJ190qijKxPfkSgAXBGzwP5qPp0IYYbu__c-He01NatGud6CxTeeaSuxKFaqNQK9Km2N0l7a9ONKb1yvYqajmToQyRCcGOO651EOt51elJh2xnYYVMVruaDVjlhkh82krhQSlqsVcAjEUJRSn7nBtEzSpyeZaPpRg67y4k5udKZugUZReiR9hx9ZW0eo34eJ36M_MApiH5lRyahthJrWMh0CoKEEHnBPAyCwIPd5Spor5e0YfshQbm0Gznhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/29439" target="_blank">📅 15:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29438">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhwLBwyp3g-WZeOarBERAvK1FfiKXUzKWolhpmVtoXtGv9mbdHWzVTKMu6O_0wZxpERC06rh407xSkYn8jtNTE6eDwFSnfcktaVAS_D7E4vZQEIMY7FKCPfyydtjy0gIrihkHDDrrVg7GCFF6YNcMzH4_iRthTu36UkKX7CSQCymwFnflHCN_1r8ZZ8bThPabggMINBIUmO1h3kQYdltwDyiOcczoBFGwY3VHkKi8zFbetiAkQDYtOlKu3ESElYYtjDUuad8VHbR2I6g2Rd96ZgUsagHWFyaahMYjkwrv_C-sAXwDqh_QH61Otjqqm-r1WrWYxRM1zNMa9QQuO9Pgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس:واقعا موندم چرا بازی برابر خیبر لغو شد. ما چند بار اعلام کردیم هیچ مشکلی برای این مسابقه نداریم اما سازمان لیگ به دلایل نامشخص تصمیم به لغو بازی ما گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29438" target="_blank">📅 14:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29437">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG3WUWitLz8MqGaR02s9gvL94Ue4hfWktbuGXgfl-4a3rKgcn71_0p1m0iI4ZZE1idyCei-9CojNGV_bWnNd3-kR4ZvpZvyvZE6m86F50seJTvNDESfBBN6lcQVcZbJiVe--fB0laNAPRA7_knja1YQFV9sNSgWltiiAWRiOfJlNaouQFqFLSR-aCXyyJ7t9rNtL-8GUXHFyVLC01c1u04MMTvDs3d31UjaAO4ceWXy5ojGJCaGBzj1Ihgn0pJJ0Mjlu4ipP31nc0Hc5DqW6UPWsEOvAuo6vX8MGXapAXvnIqCTH3ZV0OgKo_4dpfqysRxtGeAdfQH_6ddq3POfsxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تاییدشد؛ باشگاه‌پرسپولیس‌ اعلام‌کرد که هیچ گونه درخواستی برای به‌تعویق افتادن مسابقه با خیبر خرم آباد نداشته و این بازی روز یکشنبه برگزارمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/29437" target="_blank">📅 14:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29436">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bx5jhX7Afq57U5XYC4QyJ3j7bFpr7ZWBcloJaExE0PYpF1GIgPeHKIiqvEekOTZIaaqDyHOCRaPJq5VCVYzx3xqKI7EE3Ow6Hud_QNDquLTxEM65hLxGOMei9iIov7jmscU9N5safcxuX88_adABmn8Dg2WY2LWW7sjolpYp228clbPqb_ZFldb6n46qfgchL3xICDwJo9aE7hU9HiAWXzZQYZkMkspjoYsC53R2xArn9WxAMw3mUlk8VWsBrtJTy0wbDYpE-JWbPpAmPhpktpbpAK5OO88FlSRJah0pAFDPntJfDHPqhGRfXdIXy_Z6oGV9FGJ9JMZDOtyxoBNFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛علیرضامحمددستیار مهدی تارتار در پرسپولیس درروزهای‌گذشته‌با فرهان جعفری و محمد قربانی تماس‌های مفصلی داشته و از آن‌ها خواسته به تمام‌پیشنهادات خود پاسخ‌منفی بدهند تا بانک شهر در نیم فصل مقدمات جذب‌این دوبازیکن رو فراهم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/29436" target="_blank">📅 14:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29435">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtwNUG9Hqvk7E01WJGVp4gleiaYRBLcG-Dl0sk65oDeZtP1TFc5oxn6onOXWmAnFKBRWvJPrmKqdwIruE58FxE4SeljpKly_DhPsWyk2Wrd2AROjDVTD3TOvAX9zMb_6PPKfqqqeFNsNFnjZLerTo0aMPAXSJ5Sm_q5MgcnVaivlLfdYqE2f4cb_iRIgk3_HJMM85rrz72xSNb6kDt14PZxnBqnuyDVZPdIwyZptvO7hl2Qkw1KfS_KL0IGZ9zPiw_PgweSJqypUadWDPd5HmCP3dPaa60U08501F6Eu-lUxXvIB9ffAT91lWvKB9pTBEtii5FaUWy5_T2u6w6MPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
بعداز حمله‌شدید هواداران کریس رونالدو؛ دوست‌دختر ژائونوس پیج کریس رونالدو و جورجینا رو در اینستاگرام فالو کرد و برای او کامنت قلب قرمز گذاشت. دوست دختر نوس بعد از اون مصاحبه علیه CR7 توسط فن‌های رونالدو به قتل تهدید شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/29435" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29434">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSpzfK9O_qlaxNABWkb1Q3sD2NpW7y70FOJRpoe7BWA9X2Ly8o_An4jYuSJSed0Rt65qBhGmK4p82FFee_HKPxhatXVXt6mXd95GZM5zMl7XQFKQQ6A59m-KWv6cMv652I2TA2oR15LbOasm_wqbb-JISgoqI1xozf40aKGKLXNVXcgMnouNbw1vhb2Se7ZVJwd5UjsSIa09_vjGgRLLy7MpeR5e4SHLqs4qLZLhCvwDPc54yJKcGi4ceDRnjYsE2CIvK098WuRGqD6ORYQ7xmXJwRVfgW-CkPPi1DIr5kFGyau3vcW76AB3h3G0pOgnOxrqh8C104sJ4qZNKJoDNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رسمی سازمان لیگ چهار دیدار ذوب آهن با سپاهان، پرسپولیس با خیبر، ملوان با خیبر و فجر سپاسی با آلومینیوم درهفته هفتم لیگ‌برتر به تعویق افتاد. این درحالیه‌که باشگاه پرسپولیس دقایقی قبل اعلام کرد هیچ مشکلی برای دیدار با خیبر ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29434" target="_blank">📅 13:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29433">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhL6vo3huaqdq6dz6cOJCFF_gPPJximEVdX-GCvY-z_MV_qkStSkXj_1jmPAL6kJwZJhJxbuCLtv5qfncO7MsKPxYKAStn_LbjuzlLW8oQz3kEUyn8PN1RjGmH4uxGYmTrd9hneP7tP_wQsQ8_5ZJp9srd5FB81YvXRY5ttlyNqzuL1wYs9zKbDw9l7i6GNdvLik9Qil1kNe8iPuY5PXuknbdf6mrEZWi7M-F_VVhV30NlJ1oHRDuyQwxfPDQ-qlXTLdo7UGUdHKxSwmgKfKo6y7mBmksnaS8DutnLwFiA5MC8iLi_knyJ4D9GVeLB6QIze-RReUtwsOvSPforJz2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تاییدشد؛ باشگاه‌پرسپولیس‌ اعلام‌کرد که هیچ گونه درخواستی برای به‌تعویق افتادن مسابقه با خیبر خرم آباد نداشته و این بازی روز یکشنبه برگزارمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29433" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29432">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-MpxMC1DgpOtOspvrpym85mB_Y0zBfJyTWpO_BEcVV690U5JUNn4o7-e9ULCXE7__rrFcwkalosmGYOGm1rcC3pjnuReeBersr5JJmgLjTJbi3telRcNYb7JVplB27KeqwJjKd5HCyPWofd0x0yl_boj3cJ2s8dF6MoWlu1_ECBjbefi4ZwAkfQVfjav2WzkX-fj-ExlXCVinAUgIW3OdeBH9x33fFbPwBb_MZHFW1U0Q5kBMAjG392w6hjcmP1k5fNwY7Hso2HC_37BqS0cvYt7d1RIoPF2hcp0uStV2ozdRqU-EJpZqtvK8I77J_nTJ5Qd-H2EwCmjmYyiQYBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
تقویت فوق العاده باتری آیفون در سری جدید آیفون 18 پرو و آیفون 18 پرومکس. قیمت آیفون 18پرو: 1.199 دلار حدود ۲۸۰ میلیون تومان آیفون 18پرومکس : 1.299 دلار حدود ۳۰۰ میلیون‌تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29432" target="_blank">📅 13:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfS5ccDqYR3LYY2cFFlptOU2_3J3rJL-6PiE8ZF0CJ3qitN87sSoKyFUwjt7h1UywwqMmeytmfnfUUzpH70MaKfpjnPHKU0i9pRCKTUBmAVbUOSAcSwk8KjpjNmu47cGLD_jmew6zBKOJsQMslfGS4NQUB8d1nKm9-fYf0sz-d6_4ffl4_U-foNl3Yn5NGYKG1ACjiuF4s9L4clda1n2kfKxDrZcZqMnk8pobVdn2ppyVgOnWGSe83CI2AUl5VILGe_ZbdkjCRP2grsiVUmn-JtZQREBRROSK-02x3sm3hxlnHm6k1S0MbzGFvQ0S8nAEf7AZ2oCcQsd_ZKryzyhtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر خرم‌آباد ارائه نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29431" target="_blank">📅 12:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29430">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGWczBFtWB4IAwTs4T4tDqDJKvX5FLaOxylQexD_qdvUa295Tyzr9ZYPF265O8CTdI8scz3mHykZDAbEZ0bL940pgrB2t5u067R_lBhqXd2Ih8qER9pEE0LeRymWB36yMcSla6TpocxtjUXbdDCx2yjq3yeZJjlS8wZxy0qNlL6r-ECpwQG6ClRR3o6HO9hu7Tbbz9UAHbavLgSt5__wf-irxHWbo2oP1tvXa-Wd8ikJT9w_pCmkelHeogco-i_GV6j7FgkaFbHIM5SFnR6nAYkuu1YvY054nm2Seh-3c48HmJOQyq9DKobOv7WoX3hRoTzuNikEp6uchnsAqDX0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29430" target="_blank">📅 12:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29429">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f985df7eb6.mp4?token=Vj6avNh0U3GM7P_v6-ITubpZxtnZ2WHCPDWpltNXfgbfkpsrqRV2ovtn1I0B07a2j1StrM5MadsUnFa5TD2OjPYMIRPJ84VvSmyI_SEBg6o5YDogdcDWnivm5xHyfmua_qxVOCMdf-V3MDT9_EGNdAx5INXrq0Oj7h8M-6CGd0qzirCjdVoKWQS2gcMqmst9bJ-37kxjX9bCUh9O2B8MwuGUanB0q0GpNaQ-aiFCZSSaM6J7iNzvp2apu6HaiXTB9G_WEHM41NLBRfG5t1hzkUNZkw1tAWnS9UEN8t1m1LZRDF9t82deFLpnHiae04OH6P_HuJXdsoiElVxiTU3ScA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f985df7eb6.mp4?token=Vj6avNh0U3GM7P_v6-ITubpZxtnZ2WHCPDWpltNXfgbfkpsrqRV2ovtn1I0B07a2j1StrM5MadsUnFa5TD2OjPYMIRPJ84VvSmyI_SEBg6o5YDogdcDWnivm5xHyfmua_qxVOCMdf-V3MDT9_EGNdAx5INXrq0Oj7h8M-6CGd0qzirCjdVoKWQS2gcMqmst9bJ-37kxjX9bCUh9O2B8MwuGUanB0q0GpNaQ-aiFCZSSaM6J7iNzvp2apu6HaiXTB9G_WEHM41NLBRfG5t1hzkUNZkw1tAWnS9UEN8t1m1LZRDF9t82deFLpnHiae04OH6P_HuJXdsoiElVxiTU3ScA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
گل‌های سه دیدار فوق‌ جذاب امشب رقابت‌های چمپیونز لیگ؛ لیورپول با شاگردان سیمئونه، تک گل دیدار آرسنال و ناپولی و آتش‌بازی شاگردان انریکه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29429" target="_blank">📅 12:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29427">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUHXTTJ_hfLDIxt7c-BTU0gg_sAweYOrZEoB1iL0f5yKkFtT7R7t3KdEnNzlcE0GoDvMSzerJlx4-j3WkElINgjAjw3__6tf2FJ2_ClQQ9nlimCUJTD85jPGuzdoU8qQqW2nwTz38m1OPEyaihULpc5NYERufCKR7dx8j11xAizNbpP6GaULhl0hWy_rhkKS8ad0bJeZP3VQeFr6HM34el0cGDC_eW-WjGbb5Q9WcxOHsIbacCyK_GR8iEkjQ-ryW3xRN_R4hX81402FMbFxVYrkT5qpUbnPdGbx_D5Zr5Pm7oGw9kC0PmJGeosaALJfZnnTOIYVtVc3F7TiGY8E8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJw6NZIdcesB8d5D9dyUlzlM54GMBTn3YXT9XLDbOaZ7-IGJ64KodgNSqbZZk7jKihHJcmerEP1wALU19O5eLd_9I6U_Ox-xEW777QvBi9DG7Qx2rB6F2YFIg8qdkloArIxKmujWdqmHAHYjpik9RgBcDLgrhU65QocmEz-VAuMRzQCqqCcu_fY-Ux2K8gzat0aHaD_fJM1Emd76rYe07YyGBzylUnFT9AFgX7LjyFuzh_dCSB0ysX4PAY6D5qFp46l5toq-s7sxkgGZQGsZ6-NQRkQdSN4C5zFDjOGSGQ0Evn3NeU1sqiE5aDAZABBPi_4TcjbRZJBeJHGJmsd_DQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
🇦🇷
پاس گل دیدنی لیونل مسی به کاسمیرو در بازی بامداد امروز اینترمیامی‌مقابل‌شیکاگو فایر در لیگ MLS؛ بازی با نتیجه یک بر یک به پایان رسید. این423امین‌پاس‌گل دوران حرفه‌ای لئو مسی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29427" target="_blank">📅 12:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29426">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b139c692a4.mp4?token=pR--xMYep2KMI54_NYF67L2qSPkS_sWefxM9GC9a7Z45kPZAfgXnMMTtWHKkEppJVJeLNFBKnQel9iRAdPp41qf7QM-cZllCUGxwvVkHak7w_igoD7V5d__uGyFlmQLiNGVq6XH6x8rVmC1tkb-HMbltNQeyaXmkQJJAlI-MHlAMAOIEMO66yBGb0aiyVSoDHZGAoq0kE8ATfhAA7nvEadFL8XRcOmRVmTKwcWJkRMBESvHwD_bwdKU4_rF_ZzqKyE9EugG34veRP7B6VaxBN59hmoqXQ3g6G9IzNo3xV39YSnsFnWgZtLGeMtMp9lxrld3dv0ulgf0I6IZQIV9-dU_pKwtjdV6PX3ui6AXGQjOnwL9SJ6XMaf9g7toC9YqCteUbbcksAAq3cE00B9uKjHIZzt3BSMnIwLNjujEVVhWx3BUhZ7oKCRlQBkv3z5t8tClXloGM72VTjYhhLQTyDFOiFyRYUd_jWERhyeSE8oOfmf-8djtNwOHt8Z9W4tPFt7IgACiIofJSg732DWh99HY7b7FRnVclFWwJnVJ_O6U-TbCWWZsW8T54z17_1UpLMamWvaR57-c6ye5k8jNI26OuG0qBaOzzadiW4ax80Fdtau6BaONNysoSJO4v1pi-Tl8iNW9R-6pjcCuB2fozyw10AY6WEIgWsLuRn2xZf4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b139c692a4.mp4?token=pR--xMYep2KMI54_NYF67L2qSPkS_sWefxM9GC9a7Z45kPZAfgXnMMTtWHKkEppJVJeLNFBKnQel9iRAdPp41qf7QM-cZllCUGxwvVkHak7w_igoD7V5d__uGyFlmQLiNGVq6XH6x8rVmC1tkb-HMbltNQeyaXmkQJJAlI-MHlAMAOIEMO66yBGb0aiyVSoDHZGAoq0kE8ATfhAA7nvEadFL8XRcOmRVmTKwcWJkRMBESvHwD_bwdKU4_rF_ZzqKyE9EugG34veRP7B6VaxBN59hmoqXQ3g6G9IzNo3xV39YSnsFnWgZtLGeMtMp9lxrld3dv0ulgf0I6IZQIV9-dU_pKwtjdV6PX3ui6AXGQjOnwL9SJ6XMaf9g7toC9YqCteUbbcksAAq3cE00B9uKjHIZzt3BSMnIwLNjujEVVhWx3BUhZ7oKCRlQBkv3z5t8tClXloGM72VTjYhhLQTyDFOiFyRYUd_jWERhyeSE8oOfmf-8djtNwOHt8Z9W4tPFt7IgACiIofJSg732DWh99HY7b7FRnVclFWwJnVJ_O6U-TbCWWZsW8T54z17_1UpLMamWvaR57-c6ye5k8jNI26OuG0qBaOzzadiW4ax80Fdtau6BaONNysoSJO4v1pi-Tl8iNW9R-6pjcCuB2fozyw10AY6WEIgWsLuRn2xZf4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو جالب از حضور ریما رامین‌فر در جشنواره فیلم ونیز با تیپ و استایلی متفاوت و واکنش نقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29426" target="_blank">📅 12:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29425">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dU70vQeeH4vBJB3TpMgjlIXWXr4L63l3EkpFK1AqxNnmlUrZq1CxDhzw8BkfQAGsc2uv1Po4kyRluQEAvFdC5o2x9oDRsC-Nm5MIl8gIZTF-POs_NdK_YdBhSbLDL52cfb-hKM4paKfSpBGMyjS7lK98_ZPBxBW0JyHo5FUNHNyQpB1cjSUDBJZ35kBVT89nDru79FG2654B6uSFQs2FL-cOpxZP02BHR0opeMYOYoxX5b3QrGJ0eJe6-HGBwdt8q9PhRCoCzF4DUIY9FBuhSUcG2JRrzdf3YZ0YwFAwlySdP9Vt3jvp0aKkCPCkSv7tEAVDmBZViz4fiaIhu8mGoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی‌های‌جذاااااب
لیگ قهرمانان اروپا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
🆕
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای،مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود بسایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29425" target="_blank">📅 12:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29424">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEcSqqVsSI3FYhjxdjy0rze5mt18UyLwX3obaN8UWQa6lnOm7PWVmDFbCv8rCl8GVTDGQpIw-IPrjqKPlral3034FLqbakU2sRA03AA7XnjDg7lWN2OmFKRNV3Zxtm-hl3re9FHpZpF91BRDzTdI8VTEZiaBbeOMv052-VjU5ypmbhjxXms0L5qGv1rz3MNixVMttNryIEOK6RaspoP7ybDsYqkeiWik6ocZkAuQW86WwZhcfN3kxpxh7P5UNqhLKkpD3HqL-0t0AJgBOhMjPV6NNWdNcdeDJBcmtk0gdWfG3r1zaj__XXQxqeWenuRozv83Vbogrdgn-vEMgNFgWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29424" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29422">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tWvOmH48VOsQEgo-5tIDVlgZGPUfuzaWvosrfYZbfE34C79wNLMXdTeMjnCUEHZZrweHumrmo1YEQoxU_2GfkqxKqZKhG9CLL46DAPLEtSuc3pqxrB4wc6uR_t0byxhef85fYorSVq6xAs4lj15AG5IZh-oL0OLNqvyRqlCOERWZxxeGET3s8PD4ATJYRtt3oLL6vsovq4Jh3Pn3G3E_J8SuJjk1c_24cslyUBMXpNUwdy_0wEfuphOLdxuUdXT5PzUl64Y1qR7CXpZl6w_ThKGNcqNcb6swMgGjCQDataWnUaWWyje3RdIaL5IZgqiXtRIHtywbhtANg0y6ihCk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQI4QFnnf1N1XBmhBlDJYn_ZxmcsKB2yp1P72DpR9_ruLeoEwqeFpi6k7FfjLAYUkhLDt3GQCFZ9E46FkzIWkqmzryf_MqDvrtZBjeuHW0HfoljDcZFKcYSlInh60eubP5TNjtxIO6xyv7t-uFUYMEJeLoUEw8hOHjcPX1--e35EcxEJCQzCXbmM5LoYw0mvM9CooAGhsA0IeVTIm0IKIFyZ4GFLVCiLpUMdN4G-dkFYnWFRzsLR_78mYDE_6U34LRq7QDonWCnF_x3Em1KOXO9svYNZNOkXs_fj7guilx-MsFF9cEV1y8XvndKFpBv-EE462OH94v9cN8wj5spfKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
🇹🇷
روزی‌ روزگاری آردا گولر به‌ این شکل با رونالدو وارد زمین میشد الان دیگه شده فوق ستاره رئال مادرید. رونالدو در مصاحبه اخیر خود گفته آردا پتانسیل این رو داره یه روزی توپ طلای فوتبال جهان رو از آن خود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29422" target="_blank">📅 11:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29421">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5Vdkf3kOLO8DwaHmjpV6VuBJOr5uUj5rObrisgDSrSRw23XQJXOwcBmuLwNtShsGE50Kr3eJX3H7c1QzJYM7FdL4s_8k1h5MIDYLz0E53FIiLG4dFIn0G3_CBMohWmprKmmZwGOhn2tzhJjv-5KMOSnOcbGHKBZolGIEV8vOgcO0p-fLYix7z9DEwtc_eC-OzmIGHVmvodH_FIGWLdwGwNQng6zvyf9Y3TV7te3aBZDewDGiKB_oQ6qi-bqyJwXHHVS04VCv5Bc-Pr5oxUZ-ynZsWkOb3yRI94crD2QrO3kjdnaZfIBqdtDNoC4vMv7wUAmUypIt2lFW3lmRGSPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان:
حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29421" target="_blank">📅 10:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29420">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05d0b23c5d.mp4?token=dl_GBg4MmIaAk8Hcv5vTFdQegPSwtHIFZ_5uWJDgQHvgTOK0mWsyBcEXFdmrV1_uuMhUEVBFsRx7BzxxamsIe25LTUyg_K5bi-_nJl6bXpMf_TvjEOTqc48RS0muYR6f07ryp0GtT8Kt4_YqAa_GdZIZg7bN46LxOsIN8Tbd1CyldEu1TtNAIfYqIGDaBAl9rxF24aexnA1GGuDlcpZ6oVSCTIzChmQmC3DL9oMh3C0JZqncXZSEJuFYCdS_jeE0u4EzIB0XAAHSx-SGSp-ZSLlvp2MuUZMyb6uYlXEJ5GbDk8V-3SoarMRu-h5nTszkhLQjAOL9xXB595v5fxNnb6bM7swyez8CM5Bo4J97IY4QmPFj2U1t-b7EOEsBl2gI-XLzhEqqOSxgho7hY6VXZG6G-ssAM-gfyfNRbrKyI_DDMZ7O3KisfRaetcsmlds_sXIAZZtLj_74rWd1ZUtIIpHLiVcA7_TF4sOhKPktQ1cHYerxwkc5ot1eoPE153RVRm4pXJPWbhOCygFVeXuRF882yIe7pe6DFCabJFgH05hQPqFnwVzD-6ryytas3J46NDjdu6OoYdX61GJhG3nIwG8llGXp3skkSsBTgr4Im7sCish5eSwG1f7T0J2ZW4Ru6l2l27pVdai64cZz3G3Q2X8PC38UzwodrOzkX6j3h9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05d0b23c5d.mp4?token=dl_GBg4MmIaAk8Hcv5vTFdQegPSwtHIFZ_5uWJDgQHvgTOK0mWsyBcEXFdmrV1_uuMhUEVBFsRx7BzxxamsIe25LTUyg_K5bi-_nJl6bXpMf_TvjEOTqc48RS0muYR6f07ryp0GtT8Kt4_YqAa_GdZIZg7bN46LxOsIN8Tbd1CyldEu1TtNAIfYqIGDaBAl9rxF24aexnA1GGuDlcpZ6oVSCTIzChmQmC3DL9oMh3C0JZqncXZSEJuFYCdS_jeE0u4EzIB0XAAHSx-SGSp-ZSLlvp2MuUZMyb6uYlXEJ5GbDk8V-3SoarMRu-h5nTszkhLQjAOL9xXB595v5fxNnb6bM7swyez8CM5Bo4J97IY4QmPFj2U1t-b7EOEsBl2gI-XLzhEqqOSxgho7hY6VXZG6G-ssAM-gfyfNRbrKyI_DDMZ7O3KisfRaetcsmlds_sXIAZZtLj_74rWd1ZUtIIpHLiVcA7_TF4sOhKPktQ1cHYerxwkc5ot1eoPE153RVRm4pXJPWbhOCygFVeXuRF882yIe7pe6DFCabJFgH05hQPqFnwVzD-6ryytas3J46NDjdu6OoYdX61GJhG3nIwG8llGXp3skkSsBTgr4Im7sCish5eSwG1f7T0J2ZW4Ru6l2l27pVdai64cZz3G3Q2X8PC38UzwodrOzkX6j3h9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
تقویت فوق العاده باتری آیفون در سری جدید آیفون 18 پرو و آیفون 18 پرومکس. قیمت آیفون 18پرو: 1.199 دلار حدود ۲۸۰ میلیون تومان آیفون 18پرومکس : 1.299 دلار حدود ۳۰۰ میلیون‌تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29420" target="_blank">📅 10:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29419">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573430f5b6.mp4?token=md-XfXJaNM4MZKApxAcCB3EF-t0WwFWohi4RL5aHLCJcWJSxjSCs4WNgpT1RobFBPnI0gafHio3TcsZL3UdiJv9PgayZ1wV-R930Qf2jHRTMeFAc-R_tLOFXqBLqst96JTuXerlBqbtsbhDy8XxhbmVgLzRaXdEwhIMv9YPkcnvQCT6mm3Xg-e2p-e4heMAmT0Q5GhFhR1A2cQc_QDULOzpQrfKWqqLjSF4vfnC66RdTgjY5_NIY69xmDCCJwTntk7cBD6AWH7X6R5r_UKg2aMOWsXMCnDVfkK31VEmb_905LmTgZVN9BzyfF3jbDz-on7V18a3Lw9IlofqmCuLrwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573430f5b6.mp4?token=md-XfXJaNM4MZKApxAcCB3EF-t0WwFWohi4RL5aHLCJcWJSxjSCs4WNgpT1RobFBPnI0gafHio3TcsZL3UdiJv9PgayZ1wV-R930Qf2jHRTMeFAc-R_tLOFXqBLqst96JTuXerlBqbtsbhDy8XxhbmVgLzRaXdEwhIMv9YPkcnvQCT6mm3Xg-e2p-e4heMAmT0Q5GhFhR1A2cQc_QDULOzpQrfKWqqLjSF4vfnC66RdTgjY5_NIY69xmDCCJwTntk7cBD6AWH7X6R5r_UKg2aMOWsXMCnDVfkK31VEmb_905LmTgZVN9BzyfF3jbDz-on7V18a3Lw9IlofqmCuLrwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#فکت؛ برای اولین بار از فصل 2017/18 و بعد از 9 سال، ایران هیچ بازیکنی تو لیگ قهرمانان اروپا و پنج لیگ معتبر و جذاب فوتبال اروپا نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29419" target="_blank">📅 10:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29418">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HD2QDCT4Uf1W_nwY8qT3BkiRIztog_NvHVbCJzhiaybHDN8kogpQyOo0Sl7bxE-BG3D0tWDYGadAEGBw_lSceBfrKLIfSOH5lgP7dtn9g7huYTUUtfUwBqu6c7jfZRVQa9Q52IeuDzQ_1VEnhDdzYOaj3DpZ1PEGN-nx15i97ak1v70yBAlZADQNfd6LFW0UP77DBMex0vsJdxpfcSQlZfAg5bLaOjYiv73ydbqJlJu8lar8Xd0-vyu0QjN1BLcdEkRjcSq3PW9z9krvYbawg_2O9LcPB-T7-UYcbWAw-R-O1u8eyhctJvyY1yrDQ9jKs6UcWk6LQj7DJ32E3-M63w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر خرم‌آباد ارائه نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29418" target="_blank">📅 10:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29417">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d9326281.mp4?token=F8YFwjpFo5noK0Pcv2EcAygOBYmc-prZ4ANll90MXayn9JNo_px4bBmxpMirlVU3OC2fHX3_eXRqXLA0MUjKkUJlXTcngBanEfR9BhNZlxbpX9YxvBBZ8h81hKJayCGAErdlZ7kud2dlF3kzDXo0ldpCbYYH4FjPzosfdIHeqr7-Iwuf1Ej9NXDPJKUDFcfx58FO7ON8bwKgRIok8DPnYxLmW6B6n87y6kvXIS6Y4fXkxtIyDGuDoeeyqbQYw7kkkKWBElrHm36-DpWoPrTrPh4uP16dCFXg7DV1bMwRM7sWAAbKlsp6rky65KiSP6ypJ22TeboHMCamc8BNHV1ddA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d9326281.mp4?token=F8YFwjpFo5noK0Pcv2EcAygOBYmc-prZ4ANll90MXayn9JNo_px4bBmxpMirlVU3OC2fHX3_eXRqXLA0MUjKkUJlXTcngBanEfR9BhNZlxbpX9YxvBBZ8h81hKJayCGAErdlZ7kud2dlF3kzDXo0ldpCbYYH4FjPzosfdIHeqr7-Iwuf1Ej9NXDPJKUDFcfx58FO7ON8bwKgRIok8DPnYxLmW6B6n87y6kvXIS6Y4fXkxtIyDGuDoeeyqbQYw7kkkKWBElrHm36-DpWoPrTrPh4uP16dCFXg7DV1bMwRM7sWAAbKlsp6rky65KiSP6ypJ22TeboHMCamc8BNHV1ddA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29417" target="_blank">📅 09:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29413">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h99nSOWDQoAIyLPF4ggGHMHvaeEc5OPkdLhUrzch6RBU7mCxCO02vZtVbWqQg1kM_eNFrwOuKjisHbcgpsr7obPWTq5RfpmmgNGHOCZrfE89-yslVLzisEQaMbPleU92Im3krEbh7EEYs5vLPJtINbOj-O_8zhdmP7IwwFNmbpWq05QzIVVLtEdRe9AT0rCCVETvuLZEDH3JQQcM-TjDE_q3QpMCYeaM28oYPYtvuFSqW5t6MBoZwZopkSs3fSXze45O6X9sInRAVzu1aa1dSHPJpmwInpf9cOPPgkvVPRe25wvNgVEsytKEPw7LYyGPMs_Vf3Rujw4RUkES0ObFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
آیفون ۱۸ پرو رسماً ۱۸ شهریور معرفی میشود
‼️
اپل با انتشار دعوت‌نامه‌ای رسماً اعلام کرد که در تاریخ ۱۸ شهریور ساعت ۲۰:۳۰ شب به وقت ایران رویدادی برای معرفی محصولات جدید خود برگزار می‌کند. انتظار می‌رود در این رویداد علاوه‌بر آیفون ۱۸ پرو و ۱۸ پرو مکس، شاهد…</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/persiana_Soccer/29413" target="_blank">📅 01:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29411">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knvV7YN2Qvc5tIkbO1QBrIDfbLTVk08R9N1j0UHrh7ktiuXABAUYgG6BCWk8ia-2JbpLbEtOksg0uEtngH2oUa1P50LK3esPfWSGUsIFj7qP0Xf7OiIaiIjvCPkyWDVTv16DHNATDh57pd7oUEUjbPhq4U5Jj-FokPeysj9RaHUDyRb097UnN8InJX8dirfHBAC2odY4uZVdUsJAIcNFi82AwLQOtYy1saTKCImN4SKUToliMEc4XvAgSVLxhohAjeWt7MGY2Im-HcdZiEnAfF--JLlErtPq0OVjtE0hAgthDV9qBNwAYipPP17_079A7y3Jp3gA7cndDjP3kdrzuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ شهاب زاهدی مورد توجه چندباشگاه‌لیگ‌برتری قرار گرفته و احتمال اینکه در نیم فصل به لیگ برتر بازگردد وجود دارد. به زودی اطلاعات دقیق‌تری در این باره خواهیم گفت. حتی شنیدیم ممکنه زاهدی در نیم فصل یاغی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/persiana_Soccer/29411" target="_blank">📅 01:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29410">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1208f58f58.mp4?token=Iu0hNR6vg9kzMmEBcxfyln6nARfm92Y0pkiSUfn3iDcizoVrqiiL7y9n3rW5W4Kyw9VgFOfefsCpb8fTDDs3_vcDuCdQOdQDx7ZPBbUaCyJQqfFWObOqL9aK1QX8xDOwGshO82gMAKAKkMp9mljeQMa1QlQfVk2uZMrPyuh_krZd9T7kP7k4Rdtvf_UXTZD4xZX_dkhGi2pLOZDKcQO85X5gepuOPEuDccJZt2YfKt99AXQJ-kyMzDHjuz5ZurY9S_g02GuMC95n3yF9qXHv3CYgiubdvFPzwFPERiqBNz-pPRforO0Iu7tDQkFydrWXT15NHmeuNFdaS51plBU6MRItVOJkj16G_xdJkBcZY10eQ8GQNJ_5Qtx_pTeop2M7ybQYTBud3esou79sCywBLKktzyFXXVNuzJqv_VpEW43k-JNYRF0KVIsU6ljIZKs0ryI2y8epaMabVFLnSnWWp_Q4WOHgwWMlqq-PwKGFqTTd4-VO0PRKoQv3dhM23sWHJOJJrOzSxz0AE-iw2HaKKJo1XGgegweIA6LJErrOXtimYAqpVZh5XkprAoOrdB1HhyfWCQB-oIHA-WRLUh6KfLu-JKcko7a6-Rf1xoaQZ6Umdap2sZ77X78i7KTpfbr2StQu9-SCPGx2Be1dFRrmQZJotF67_N0eDCV9E3Tq2bY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1208f58f58.mp4?token=Iu0hNR6vg9kzMmEBcxfyln6nARfm92Y0pkiSUfn3iDcizoVrqiiL7y9n3rW5W4Kyw9VgFOfefsCpb8fTDDs3_vcDuCdQOdQDx7ZPBbUaCyJQqfFWObOqL9aK1QX8xDOwGshO82gMAKAKkMp9mljeQMa1QlQfVk2uZMrPyuh_krZd9T7kP7k4Rdtvf_UXTZD4xZX_dkhGi2pLOZDKcQO85X5gepuOPEuDccJZt2YfKt99AXQJ-kyMzDHjuz5ZurY9S_g02GuMC95n3yF9qXHv3CYgiubdvFPzwFPERiqBNz-pPRforO0Iu7tDQkFydrWXT15NHmeuNFdaS51plBU6MRItVOJkj16G_xdJkBcZY10eQ8GQNJ_5Qtx_pTeop2M7ybQYTBud3esou79sCywBLKktzyFXXVNuzJqv_VpEW43k-JNYRF0KVIsU6ljIZKs0ryI2y8epaMabVFLnSnWWp_Q4WOHgwWMlqq-PwKGFqTTd4-VO0PRKoQv3dhM23sWHJOJJrOzSxz0AE-iw2HaKKJo1XGgegweIA6LJErrOXtimYAqpVZh5XkprAoOrdB1HhyfWCQB-oIHA-WRLUh6KfLu-JKcko7a6-Rf1xoaQZ6Umdap2sZ77X78i7KTpfbr2StQu9-SCPGx2Be1dFRrmQZJotF67_N0eDCV9E3Tq2bY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
درمرحله‌سوم‌جام‌اتحادیه‌انگلیس؛شاگردان ژابی آلونسو درحالی دو برصفر از لیدز یونایتد عقب بودند در نهایت به پیروزی پرگل شش بر سه رسیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/persiana_Soccer/29410" target="_blank">📅 01:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29409">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEGlTGVOb_KOmv0aEuWgEmhyyCsqTa0FxWgBhwuStgwinngYqWSTUMRkNL1YQdUnxNFwn6ShLVg__9tnWLeu4KMvw-u5lBD-_4JSfpyEUbKTsfrAyC9DYpScjdhjrFsX14G0U0fH1k5uHXQh7BGXcbdm4tMFs7Gknu9OmBc8874H26VeoHjsaVvYR7_2OhKOs9MOuA0TEgZVC9b9n5JFkW2YFFi9Crn0EHBIR9BinFrK-LSV43_F4LN_E_ujRNly6LGeGWXJ08nw3NeREBhPRjMw43iZuzCPHCZ8fdZX0X8vakYbS6DnxdCPh4_MAUpG-LrDeHm0G5RHtkAMxaqpqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛درباره محمد قربانی چون در لیست مهدی تارتار قرار داره باشگاه‌پرسپولیس در نیم فصل بار دیگر برای جذب او اقدام خواهد کرد. رقم تعیین شده برای‌ رضایت‌ نامه قربانی 1.2 میلیون دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/persiana_Soccer/29409" target="_blank">📅 01:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29407">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODk_0y7ADxgUc2uV24myC1soaLUCKwMSMfw7_BP2Kwfm4feU2z3MDKkO_GuYCmYdpp7ONmo6_WXWDLm7RT8mTpSRz8wJz8NEhA1UCon8ulm_-bAfaToaJiWrNshcSY669RRWPwy_CQBtOkjpJOoFKKydQOuRnNUZO3hY2w_ZMY9cTUQgSE1NqlvIYDvej66ttbBZ8P6of1DntS7Vso6uzAUbDNZsWptCutq8qM4jzKPabmgpP2l103PSGS0YHbz4PJEWj0IXNUleSWapu3R1LSijowxmxPS9v-Km4PN06fxM6vfUvX5bXm7DLyIGVx5_DMi1q7S-UKPTryJJrVxS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛جدال آبی‌ها با پیکان و نبرد یاران کمپانی باپدیده‌نروژی‌فصل گذشته چمپیونزلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/persiana_Soccer/29407" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29406">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA3Jo_5hNNp5dAHW6JzRTp891APeEeLPfbCl2qeAtqAkZQXP-5WvHl_7vOtgwc1sNTuD2iZtUuvchHVlPah0tu5qjrQHSBeMiL--BfvbfzE6A443bDN0-7i6kkk5EW2qZJp1BPIz3oeyXTBjgh2EA_wdbfqxSvcceF8FrtQEc6OgJ90gmbmf7eDxsG9OWREQUaPgO74roK3aLecVkziuZF7kCxpw0w9Jfb6aZtPH9LWYY11TeQPMbpHN09K6w5yqxsf9boY-CQORRC3p2pXwOyBpfjznnnPeVnAZ8k3GKGjo1Mg1nlUFGDr4-LT_wkSWpUeenMz4BKgccsZS9q8x6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبردارزشمندلیورپولی‌ها در آنفیلد تا آتش‌بازی بارسلونا و پاری‌سن‌ژرمن مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/29406" target="_blank">📅 00:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29405">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9H5cIBaavclR9J6__uRfQ0AAOuStdvMtzJuG29CDLyD6eDdhPIRJqMyNCo25gAyqAFkuSd3Rd5mAyTGzqEq73b4xu6KgFwZ8mTyNcty6tXkZd43FjSrlb7z9aCLxM1ihny46HuvPNcdIyGlRZ_8H_TE83VDq3n12og6YVG33PTh35-RDEZGMsQnSGvNhSTfrJBqkX-xYs24mWquS263iktNlrIvKI2BTfft-oSg1p2vacs_zJqe_Ul_TyE6Wd0-48U4AxPDXcrH4I9okbSwFIaGGFrBysYMoei5EimFHLs_G-oL8ioB6BKivSo3AlJLHH5sMilgMPyDLvQ-yfn-5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
درمرحله‌سوم‌جام‌اتحادیه‌انگلیس؛
شاگردان ژابی آلونسو درحالی دو برصفر از لیدز یونایتد عقب بودند در نهایت به پیروزی پرگل شش بر سه رسیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/29405" target="_blank">📅 00:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29404">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29404" target="_blank">📅 00:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29403">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwo542z-WTn81lg3Gu3VRubWGpxSIN3iRK_RkvM8Y6F0XgKU2GvA69uHbCts8AUh4sFS-ASPqx7gBytS3s9fwl4BSubSyXBE8jFntnDf5HNaAUmOGCtjvM-6Ez_poqG_-7GPPU9TUdq6QFINe4nJmNA-0MlTLIQ1Qi5pMQMuuETfuHpEXyf3shNe3QaKa19E9N4VwfR5TJYdCTWjcHuqT9jlpN-4hCtlb147s7ocaWqpMJDd9H9uycGkpLgB-mnd8CNtzZu10ygTirR6yAI7MPIGZ2PRwqt1YVz4fNnxEkWwxjG0vTDKTfcvYr0T7LPpjX9K_DkKTDMSjpezE5s0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛ شماتیک ترکیب آرسنال و ناپولی و شماتیک‌ترکیب اتلتیکو و لیورپول؛ خولیان الوارز بالاخره در ترکیب اتلتیکو فیکس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29403" target="_blank">📅 00:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29402">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4gDD8N9HcpC--O0nVA0BeYFSSuZuip41L9QtWAwE17ceoQl9NivYy7jgkSm11CbYBnCnxbasa667DYkvGzN5ReYH04E2GUH1O8vxyEbZOrOkkeMul840_5Td_TF5CFyS9Xn23FsPJT_1TGH2P1oFbsqOCg0EOVhc64RJIMJNq3-FR426wvfD5xfPYCvR1l7jy_0jlkf3JbFS4dAQBOaAm66gJleUrkmgTZm2bTOoIRkNdSBSt-is1wlQIgMcezVBNZBoXpiSDQn4OE5NNvc_iL1m7J4RObyMzmHBvF7kqIt6PVlSeyLEnHp9HssoCbKklsSU7ekb64OGP_rH6styg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29402" target="_blank">📅 00:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29401">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7sVhO302qvoiePHAaKZzacX1E7iX80eRk-VekDpeMn6YM4Rouc6nHBRXESxqp2D4vVxYz4DHIu2ZmM8Miko3aKZIQZCxuuSe5SlROqZwuJv2lqKyx7yOEzZj3CVfsLDUlbr-WmsurLbeweEZIiN5nQIDOKB4AWYCqyQhONgQf6CwwW_SSjcxpEjHnKKVKwupRY8CCCrnRcYDq1OJhMKl21Xvg1yQKh6tQYcMfpeYMlDwSLO1I2OibVuL84q81UhrgISDrN5iiPwSRW_plF6_jJYo-C2NkOn-RUjDMYYNGJWiOF2jCp0xaBVSFA8bqAVFKTFUo8RN59dCt_jXXSRnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
طبق گفته اکثر رسانه‌ ها؛ این آخرین فصل حضور ارلینگ هالند در باشگاه منچسترسیتی و لیگ جزیره خواهد بود و در پایان فصل راهی یکی از دو باشگاه رئال مادرید یا بارسلونا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29401" target="_blank">📅 00:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29400">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a8082900.mp4?token=Ea9Z-ysYhZpl3F1YxNeuWEs31afTXUHgf7d4cKjowP3uNbnRRMV3uPd4WcHhI3HzdeBbBRoOTVDIxQCuWNB_1UtVkoHruf3y64qJ8ASOOBc0gBRaQ0HVVnpdWudUbBb80ZvLZBo0MGJ7FaVOOcI9-kp2pyP0RsRzSrJIZJJeUWSb90kk1dx5dmUmkwOZYVgg_ayEFNK-mQDBaqBWxSYYcdi7Vu-ECc1VKu8XvNFmkHKd8I6MbzkiJc8hdp_CZAdZr7I1KRxN2kvWG44-nsWqIjCsH7tCX0652YjYck-vMU3s5W4-ErxYlPfkbkYwo0Jp8SPyGcgAQBzHQd2Y_DSziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a8082900.mp4?token=Ea9Z-ysYhZpl3F1YxNeuWEs31afTXUHgf7d4cKjowP3uNbnRRMV3uPd4WcHhI3HzdeBbBRoOTVDIxQCuWNB_1UtVkoHruf3y64qJ8ASOOBc0gBRaQ0HVVnpdWudUbBb80ZvLZBo0MGJ7FaVOOcI9-kp2pyP0RsRzSrJIZJJeUWSb90kk1dx5dmUmkwOZYVgg_ayEFNK-mQDBaqBWxSYYcdi7Vu-ECc1VKu8XvNFmkHKd8I6MbzkiJc8hdp_CZAdZr7I1KRxN2kvWG44-nsWqIjCsH7tCX0652YjYck-vMU3s5W4-ErxYlPfkbkYwo0Jp8SPyGcgAQBzHQd2Y_DSziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای‌ازدواج‌محمدپروین‌باآناهیتا درگاهی عمه دنیس اکرت مهاجم ملی پوش استاندارد لیژ از زبان داماد سابق علی پروین: پروین بشدت مخالف بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/29400" target="_blank">📅 23:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29399">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxAv76Qa0RrQ9QdHwxpMnNKu26EaN8ou6MWGGhJRuxegWbKgPADF8lsUZ8TE0AY5nwYHSdwREbATJDOawk9_xMBckDQluVGUSL-AObaXxpKVUE8HpRn4OrMgsk0ld0wBzSxyEiAWQsCr_wTe3ugn2ghLkM1AJiwXgNLPMbaezWEKs-dguzagdZ8FPm7jCWtULAiqPQwecMPYO3Jik-7QFptLfVkBRMBoGo5LI0-GWjlmmNbqUqDc-mlKfnoyoyTrYAJeg7SCGOOh7sZF_9OkCjlAkenRSmyZ3x-WkwTkvxGoXOfCmd6e2qYl3y6yEb-Sy7UUcreaaa33dH9vmevFJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فکت؛ رافینیا دیاز با گلزنی مقابل فاینورد تبدیل به اولین بازیکن تاریخ بارسلونا شد که در پنج بازی اول فصل برای این تیم گلزنی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29399" target="_blank">📅 23:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29398">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiMXc0EBPvurLAZn9_ftbXAsSNta5LIYRyugFr4XBFUikqKV1oU0UoZFuULhwCTZkAl15WwdxGZWo9e5G8AXH1BktVUYNa23jB9RXlxCi3GgNunYOt9oqR3DIIXxS1MsQDzg04JlCcjjpvPIH7AN__L9Dzq8-YMWwqc96oVjORNfcZK79S1i70bf9hqIDszSR7HLNGHyq6qdEtTnC2k4x0hyADMOUlbwcCazGqgh8BXzWy3CesSzQIV_-qHmJmAYpoRvRzKxyJHVLrViupDsqLPL4ZTvOAt4YOrRLs6eQ1hiNWLDN0GF5_9Dzu0Ia6dclOdxzL2wiPPmUDW-JJrbHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29398" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29397">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdDNwa4DpGX9U-eXpMsBmeWnWbw-nTKFMlaKW5vPfBDqi44oVqy5AoD8hxVlRgYrPA9k_Y4lbUeFD9SFOt_F9VIVUWJHPn_tP907ViPgHLoZwK0T67GX4lu4gs2afC2mfRYVcTnGJxIkZ4e-ljOM1uoAmtHcVaNBPk_4nQwsni9CS6fs4wCT9jgdzv6X3_plVu0ix8K4owv97dHpddVmZuSknKrKjVpXWgaxntsCk5o5Wbxvhot4HJFgI73C-PNrONHeEVzBfvAXBaPbk51bFJFaqQ7oabcKf7w44xmOYIlzXEPNsRN80-Nca_AhfiS59LOyl4ocxISeoUdYZbGWFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نتایج درخشان و خیره کننده بارسلونا مدل هانسی فلیک در این فصل: 5 مسابقه، 5 پیروزی، 22 گل زده، 5 گل خورده، میانگین نمره 9.3 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29397" target="_blank">📅 22:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29396">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiI0bhDvs2oUbNYSJ99OLvCdEqwqQC3lIRdyHGH79s6G-TzTxHHkp1NVJTKJf3xXQHPb6mWqVEmnD5VjfDoBZ7g6o6hgvh_BmoJefVNRnSK61gJfTw54wk57v-yIncPCKeXalHjCCvWTcYSIwS3tW9w8TVXj6eKsg-Lo8G7DCiau4kpK1VvcpFrCJYxxN7dGzJ91V1V05aV1QUjHEoSVD-mz8CzgP4lQSVwLZZ8xpVshe5fUPoEEpFbbyZ_r7RYZAcTaCnvEvaV8SsIjMJS5ZB0ilmHZ_GSGwzerZquwtiCYazPpgVKzJOiybniQUC6nAwOBsRLDsq2SRwfhE6ZvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
در هفته اول چمپونزلیگ؛ شاگردان هانسی فلیک درنیوکمپ آتش‌بازی راه انداختن و با نتیجه پر گل 5 بر 1 نماینده هلند رو شکست داد. 22 گل زده در 5 مسابقه؛ عملکرد استثتایی بارسای فلیک!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29396" target="_blank">📅 22:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29395">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2m0gPFCbZuWDMDb1gsdx8D2bWZ6FfX3uCd2AeZvukHC3egxcT9-jTVNbCQhljZgGmkmY1saT7zTYB8eyaX47DizvYQk8qb8PxD2UJjz_dpU2o3lccmG5AylDBMSFQgCy-P0P_H1aB6RgMiQ_AdrIfFtXp4Z7VKtiGtMWelnl4GND7SvpAce1a7vw7jBihC0TLgT2dnwJPt3Jz3SxWzKQpbx2ptuzrF5QeKEk5QPtuAYlpCiljQrHGcC97uLZLAritvl8XwbaQKLIBLHPuPlFOziMJBwYlluxrGM6SlgnvI9yA-5bOjN2UnuEPZarSuSGt9weSM8pIhnZb0d5ueTrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کاشته تماشایی لامین یامال ستاره 19 ساله بارسا در بازی امشب آبی اناری‌ها مقابل فاینورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/29395" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29394">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adadb2bd3e.mp4?token=ByYzYXi4fQqoJBj0rM4TuIRNOX79II4TEBGpX7koMt_4Au9q-jFCYRIczlFT5KT1HKfQB5BbWaXw-LGnMYr1_ADQJl3BYlJonlkP4HJs-Tx3cqQqI-0jPuL998hQ6XoXTeUmIXEjbj5J_y9FJycZERp4hPKotnEi9peRepvDjYLuUgF_3L7oieNZGDpGAlHJFGKERSrljhRqAYH6c2EJPqsm4pdtzIwqcnYH3rbkCCIAuBr4aqv86EEFjLOsy6CrhxsmHCmQgr1NA_MpoNy3MwDYUozSm9Vjk0KpiKtFGEjfcgu5h8FnrJJyPLN36Ac_wYpZrFbvGYZ2jQe5h1IFCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adadb2bd3e.mp4?token=ByYzYXi4fQqoJBj0rM4TuIRNOX79II4TEBGpX7koMt_4Au9q-jFCYRIczlFT5KT1HKfQB5BbWaXw-LGnMYr1_ADQJl3BYlJonlkP4HJs-Tx3cqQqI-0jPuL998hQ6XoXTeUmIXEjbj5J_y9FJycZERp4hPKotnEi9peRepvDjYLuUgF_3L7oieNZGDpGAlHJFGKERSrljhRqAYH6c2EJPqsm4pdtzIwqcnYH3rbkCCIAuBr4aqv86EEFjLOsy6CrhxsmHCmQgr1NA_MpoNy3MwDYUozSm9Vjk0KpiKtFGEjfcgu5h8FnrJJyPLN36Ac_wYpZrFbvGYZ2jQe5h1IFCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
مقایسه‌عملکردکریس‌رونالدو
🆚
لیونل مسی به مناسبت قرارگرفتن لیونل مسی در لیست 30 نفر کاندیدای توپ طلا و غیبت عجیب کریس رونالدو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29394" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29393">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135ac654e4.mp4?token=C-PgiMfiF8CLndr_Ctjz13huFdQVwl01ckZsRSyy2FYdVL-X6YA9IFDY-KjhUyQucjiKQf-X_o8aOarwsGZjiQ2oP05OmdW7VjrpYTeLDsD1JVaNRtt0ziswfKyTvNLtwzDHc0-5lrlhILwoSQUSoYpEQMfBTr0ix34W4EWJEY3BomwqraqIYObFk8Nrjp8rbrOZx6O61fMS6SPZlDJy2Q1B4DHjQRlNDDaYV9MOh_juU0LImdeLDPXHyPteVPiudTD0Eqf9g6X9n6R_dQr8lEyGc25334JFhjydvMH8J3m1oAdIDv-xjzXf9DLKb-YgEt4bdmegXzZy0l0iqploRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135ac654e4.mp4?token=C-PgiMfiF8CLndr_Ctjz13huFdQVwl01ckZsRSyy2FYdVL-X6YA9IFDY-KjhUyQucjiKQf-X_o8aOarwsGZjiQ2oP05OmdW7VjrpYTeLDsD1JVaNRtt0ziswfKyTvNLtwzDHc0-5lrlhILwoSQUSoYpEQMfBTr0ix34W4EWJEY3BomwqraqIYObFk8Nrjp8rbrOZx6O61fMS6SPZlDJy2Q1B4DHjQRlNDDaYV9MOh_juU0LImdeLDPXHyPteVPiudTD0Eqf9g6X9n6R_dQr8lEyGc25334JFhjydvMH8J3m1oAdIDv-xjzXf9DLKb-YgEt4bdmegXzZy0l0iqploRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
سوپرگل‌استثنایی کریم‌آدیمی ستاره 23 ساله تازه وارد بارسلونا در بازی امشب این تیم مقابل فاینورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29393" target="_blank">📅 21:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29392">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqkc3Y02XNBuGrtAPVsWpW_BTqFa_QOXmscPkDWvTJ9fFHpIqRtBtGomaRsnAzh2KFRHvrcdoHeH_ayGaBlJ6fkt8KMU6JXT6uGuq9ISK1v5oB3UxnM8J9MscqYjVAHxByY6nbFBPDmnulqFgeqWS_hFBLToqsYFZodbyVVgyMMD7fzdQTTTf-0blNA3_tKY0F6ZGK4Xyxi1QRa-igA2HMQdi3SE66jBigzAzaxs6tu49GWz8ZZwZZN43VtAmdR22_03bpp2QR37ZGnvnE3-ftd8PZlqHa-UE3GQF4lDSERXVV_NusJxbbGJde5waiMB1PAqr0cMiXgNfOFUyhjq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛
شماتیک ترکیب آرسنال و ناپولی و شماتیک‌ترکیب اتلتیکو و لیورپول؛ خولیان الوارز بالاخره در ترکیب اتلتیکو فیکس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29392" target="_blank">📅 21:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29391">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9709bebc.mp4?token=iktw9FUcGAuaq6lTCPyoaQ0gQr59ncBT-9JuqW3OeymiILpuukAJrr8bDDYraFkUqDQhpUuQURsmb8Z6-PaFw5olcj1k7aUmW5hEY1PbRP2fy9CzcGvwXUgvu2lmDaNHpl52Nar_PriloP8wHqGlgIdpck896JjxePxrw14U8uR61B1QJvBUXubnoUSXwxs5TleNimQ2FH9ha_vB-XL5pleMmYs76HruC795dwDLx7k4tx1p_IHusTwanzSQhKdB-LZgRH1BToIlwvFaTi7LC-rJfP7r1O8ClAS89bC-yH8ijZjsdn-rTHFzGq0ioVlUSA1wcnatMz0CTMinJFDxuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9709bebc.mp4?token=iktw9FUcGAuaq6lTCPyoaQ0gQr59ncBT-9JuqW3OeymiILpuukAJrr8bDDYraFkUqDQhpUuQURsmb8Z6-PaFw5olcj1k7aUmW5hEY1PbRP2fy9CzcGvwXUgvu2lmDaNHpl52Nar_PriloP8wHqGlgIdpck896JjxePxrw14U8uR61B1QJvBUXubnoUSXwxs5TleNimQ2FH9ha_vB-XL5pleMmYs76HruC795dwDLx7k4tx1p_IHusTwanzSQhKdB-LZgRH1BToIlwvFaTi7LC-rJfP7r1O8ClAS89bC-yH8ijZjsdn-rTHFzGq0ioVlUSA1wcnatMz0CTMinJFDxuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آرش فرزین دامادسابق علی‌پروین:
بعد از شش سال جدایی هنوزم لادن پروین رو دوست دارم! بت زدن ‌هام رو بازی‌های فوتبال باعث طلاقم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29391" target="_blank">📅 21:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29390">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPExmzBY72kGK1Ab6SpKSdxL3uklo2WFCenT5-CRy0r8AqEM8i1eZ9lg_k7ImvYJGyzYs_48YnOAgShtNRSLEIm0a0zqJce2CxF2cNo_VephQZyPIExcCvVrH1aPEoRpYfVKpRPcG6u0lnGLC4vjfqGYZ7hzxiRwTg4tejWvydGF-9yB5djpkZNJkNWOFeLtfl4lRfhLuQR4bJMyDPibdaGibLIl15na3eox2E9Hhvq9ICECu8BCW-4oVH-tB8Cqh6jqIjG_82FreSXVRTJSzgqRBv5yYwc5tqHgimpbrhY-hsbxEORH6FuBQSc7v0BYJl_JhjD8wpfPhoNvHCSw3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29390" target="_blank">📅 20:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29389">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/448238a183.mp4?token=lQt-du5p1C2w8gy4l8oVzJjQU10-69my-gVCJ_yRrw2HHCzRzBRwnsNkIhPMIHcCoH-d_Ex8KnF700yluOOprsNFjQaQPefCxCwJy3HMwoP6CnyOyumT3aicXttLqR1V8FhGCivLhECICfLIlY_BYBF0QTqeiWo3uxP5XnWjVuo5SZOJ5X5OkuI-6Ui8cEhPotLU9mR9AOfLpagOpjHfAukamGkJxwU6o4SJg8XYbJTlBMKxhcCB1jeoQllNgHHQ2u-my7Wrr_Q5qvEHfjRQsdPTLFUCwwSK1WO2toQoZmADUVpzZGWuAUgRhBwxMnYbVfegDDQfPKYDkQlwi6D0bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/448238a183.mp4?token=lQt-du5p1C2w8gy4l8oVzJjQU10-69my-gVCJ_yRrw2HHCzRzBRwnsNkIhPMIHcCoH-d_Ex8KnF700yluOOprsNFjQaQPefCxCwJy3HMwoP6CnyOyumT3aicXttLqR1V8FhGCivLhECICfLIlY_BYBF0QTqeiWo3uxP5XnWjVuo5SZOJ5X5OkuI-6Ui8cEhPotLU9mR9AOfLpagOpjHfAukamGkJxwU6o4SJg8XYbJTlBMKxhcCB1jeoQllNgHHQ2u-my7Wrr_Q5qvEHfjRQsdPTLFUCwwSK1WO2toQoZmADUVpzZGWuAUgRhBwxMnYbVfegDDQfPKYDkQlwi6D0bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛ شماتیک ترکیب بارسلونا برای دیدار مقابل فاینورد؛ ساعت 20:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29389" target="_blank">📅 20:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29388">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
#تکمیلی؛ پیج معروف 433 سه پاس گل دیدنی نادر محمدی باپرتاب‌اوت دراین‌فصل رو پست‌کرده و میکل آرتتا روهم تگ خورده که این بازیکن رو بخر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29388" target="_blank">📅 20:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29387">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFMg8gpPMyeV92Cu4G9YpNF8QroOyiprtuz9rIUgtz0uFy8iPpxDn0hNx7jTRaFWQmoP89JdhvhxXP9JJshUweYx0mRtkmd4XjE21hmcrYn1NXQSat8A102tH3nwQ9lp9dn-Mu0SWza26Pb8PoM62y1E4nyJCprHsY2ydGKeX6VCKWk6x7JO3QRFg6zczKJUtrRlzmDsOBkHm-HmtGxBpxan4fSJpBGRSGZr45EbTiTOw1-xJxrJiJw3fsP1HaApbQWvmbfT10EvlMYfB6gFDLBG17E_R5E_X4n0_9aDA-UV8EkAo2OjyPXU8v0smMn8FDhwUYvHAhJDLvS7N3vJlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29387" target="_blank">📅 20:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29386">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXFlaVp41NdTUo_l5nr4LBfLTnJj6DCPxAmM-xOrxTUgzR1b0O-HKEBgLfQ3_bJOSSXw62Zak5SHMoMMM4clHBnEFn0r1Zm2ff_DJW0qXoL20X1eR59xyeRnjfIPGfgcxUlj62lUMlxjI15PAFYMwkh99hIGIfTDExDfFJJaepIgmK421xcD6-kJC6BrP5eVgN8igAwG5hja-8-bgWCD2fGaEWmeS8M0GWSEvLt59riSpDI9m4DK-iEcjA8Ss_sAi5ITVA_86hUdcoYqPHxvaurch6V64AE13_0yXCVjNcgBt3zIdb-BCkMN0abR7DAZHmrJM_C9fdRNb688QoHx4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اسماعیل کارتال سرمربی فنرباغچه در نشست خبری قبل از دیدار فردا با آاس رم: «آاس رم فعلی قدرتمند ترین و با کیفیت ترین ترکیب تاریخ این باشگاه است.»
حالا
ترکیب فصل ۲۰۱۵/۱۶
:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29386" target="_blank">📅 19:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29385">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfvncj2nytBqtuYj_HqO0CLtZXk6soD-YOj5UdvIT3D5sj5-H-5pdGAimCmuM4r5vDYV5rQlUg_u2e2gd0TJrJ0YD_cF_drNAuD1lagi-KyqHg-kk1mO0DaAWYufHTkN5lUHRi-661HJC5sa9SnPiGnlkpgBv2AH0cc8sEqzJDhjlDD6rpcrDeHQI6hgIXwTw_pNQfvMKTWBhkWx1YXpuRvepB0SuYMPgecS6-mwUb5v9O2xLQiR_VxTPavtQPx6aD1PLJpH1bCLYW420pBs3lPVn1dLd-j4BUpVPAWAFRpShD3XqcyIIC7ldB7LH3QdZMakz3-GaKPG_lGDvxG73A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛ مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29385" target="_blank">📅 19:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29384">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnBTmi0KHWHS6toU9nkjy6I3zqei6tBTTbDIDgV1HruZVvLUR31NPvMsZDghT1wl1ebomzrCygoNQJYs2FXIF8ZiV6_8gCo72EqFpkqGd9nLbmcrkLnM4cxLmSBecKRSkwS0_XH8g1ogdzBehtIQEajobv7a952fQk4wQ6sjoKBor9TUchiQvmJTXOxv9B6Bra0RcYgY_-5B9Y8VK_JuPzC-rBegWAEN1eTpN1T50hlB2_Q3ZDkclPZIH2XHCPSXSm9tDfLDazx0UvexN3RBmAHt0V8u18XmVrHRnrmEM7o_Y7QjMjSWQ7f2sapeVcfeaOHqQuzyOb39s6_9bVdZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛
شماتیک ترکیب بارسلونا برای دیدار مقابل فاینورد؛ ساعت 20:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29384" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29383">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcirCLkE7gLU-s8GHyhBTDQMXPrYHxjKf0x8pUxqbMm7Men7bS-Bd55k_CV0SWfROB-Dz3s02fl9DfFuBCmd_ODTM2_nBgaPaI_drbE2L8IyiWyRZU1mTZinJkHE1Mf-_0ysjM7e66J15bGZ5kS-io93e2-sI5ad0VEifESUH4MsCz8GO9ogsSWqKCOp4viBcWn7L8PHJHK5psQ7M2_xwtLrDUmA8iTPhsOeI3xpIDuK2Vcbcz7dRIRqLHWXNghoU80VuU3-8hVf8QgfhzMczq1wGv7096qj3GYMxBuSwIvf8YH3cWxXKap1w2V7h0TKoE9HimXJowKdQ1rWfQJ35w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29383" target="_blank">📅 18:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29382">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atzj2ohrYsapte4pcWepmrYF5Truaekh1ykUqpHI8auE88CbgnKrqdkRA0nhGmczi8JXIGS1uKQ7ASkHq0p6AV941fzF5EKT2VuHQWPcZ9dCSqEC4Ntz4SZmh1Eh-TNmPjLsp3aq9qOZd1xH389cl1tALQzlWbea7EfzirQ14qjJ2eloG8jsZeIf3-h2ibh2BQbq5DlHHumNME7ngRgdAgKbiP-JSFWW7wwKHxdo_kTZzwlv94n3gL3RyM0RWDcgT-3hVzcTpO6IBu94nLelAJID7maBre61Ge4O6kX0u7mpo8FzU1InIT-Ix3zeJiPuswjc5JCs_vkXNd93cDqLkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29382" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29381">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqfClcArr339d8dLrP4w5C0CNU5tm_njsAjZN9XBUfHNOhU0Umn3PaehKQJwVeOiDzSyWvpjssK5e1VrTQhhicIDazUfUwZ6Tr-HJ4dkbtUxr8Nl8S_vSbrhQsnIRWUeB_AXimoVcfOwGSBv8ishKzSrIger6deruzt0XZCzT8Kc7lvw6HlaxfJGD-8mS3gyjWoHKIzOi_rmDoJZPIWmmCAnsFATBt3WQC52o3svlTr9ZNeqOw-RTFv7BsWMfvW6W2pS1rWK33EYV10o03kCQxL9-ypA62ljes8oCsBj9jaF5dyfCyWLxulVxpPNqeyhXnFbOwXKoRl5n7LrImwgzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
لیونل مسی و کریس رونالدو آمادگی خود را برای حضور در مسابقه خدافظی کارلوس توز در تیم بوکاجونیورز اعلام‌کرده‌اند و بالاخره بعدِ سال‌ها این دو فوق ستاره در یک تیم همتیمی خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29381" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29380">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXi5VhdTt41tQihm4c13eRHQ4ElYrRLVaygrmADablxaCQeR1gHDewcH6P2lX5PTIO_JNtK4Nf1pB6m7-0rOcIlMqTBncP5hphULtVUrpJYKdnV4x_tm9iS9a0I2l4Nb63A87yS37p-Xo3DKbSk_WzhCIKK4S8MuxLzsm1acvWaOCykPsoznfUxz0SYDLWemuwZPfP-rcZBw8yT1NwuIpJYH0l1ct5RGB1VcysNCJ-wI4iuL_bNsRSFlP8LSZhrNPmkis27rO2TOteDtg1RSashk6Hn0OTOJj3xT7rtgy-8GVlXO9gZumhIgyg9I7pbz9O6fqFgpl67jcRS6pYq1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🆚
اتلتیکو مادرید
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/29380" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29379">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuUENezQ57nAU3sgu-KBLseBdb1CxOiFyp0bY54Q88SaQxW2yKhvt-CMerRf2ueo7bsN5zAQC5234YsZqICoao25m0sgywfUsLoJ9dl4IOLqeomukl2dZ-Jf7YgW8IUWD2uy0DYCr2CdUqaeclnDPlhB0uVIat4863-gCr2ISK--AR3PSkkrj3QSHbsJMi9UEH3IqVpYEcWWqq0paqlePKMJrE0h--j6IjJNojV9aMSQGYHpyROqrVw1tJfLtYju03WrD2I_0p6nckndHH3XiOXJ6RhtQWUYCEDHHgqBnwZxIoce4JNvr6eZyBEpArSZgtN9NRCSwMRXKjRJlsdrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛
مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29379" target="_blank">📅 17:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29378">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGfwCzoS9-slZl3V-y4ABKlWCF0K-GMml0Px2A0qZjhUfFBWkiwud2mhhxQzrl4Fpc_bIP7rriynnHu8yVBG9bpKvlenTP8l7knFWJYqXXsMGAdQJzJ4SR9_J04B-HUA4h6F9q1_5KeJQZSomwUCLGkTT2e0tOTb4tmirs38Kl0u7dMRnKbcVW7iLXtsaznTsGKbQY4Fbrk37Bot5KeZB07m69nBGFYRb8OIplwFV4qDYAeJVYecavDy5a9AWK83T2gFGRPx8N16B1PZPm9KeFdsGRLiqGOd_2F7hnF3_zUcyea-CoE2HJMjIgFSobOkdPMcF1Wm5ZuQkS4r3cVpKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
💵
قیمت‌های‌احتمالی‌آیفون 18 که قراره امشب حوالی ساعت20:30 بوقت‌ایران ازش رونمایی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29378" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29377">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1pAUpUINF_g4V0kq4pxcEq04crvw8CSsjBpCYfGbXKigqp3AaCcw3cPeT_MtXfPD5A8KaMRXIvibeU1kXWzObtnUN5mQifyx6Vuj41_Ybklrv4AcDkCMBirZzF4rZsSH7WmRYRTT5ys896cEGFMZBF8UWAMGp_1rzGF28RnzYDZFd5tlQG0xWPl7CagJNVykzBAqCSyA5C_PzMCAyAdwqrBb3KDYQRQwyHMIBGaLCA7RFAaiIOXWNc_eOtXF5F0GSIqI0TBaYj-Lah8TuwlY5lqAFzXEmBdS68tuYDu-Tu4ANIkTpFJ6gc3rFksjRebX_nGhQB7y4xITNsZqhR_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردشکنی جالب پاریسی‌ها در تاریخ توپ طلا؛ نامزدهای نهایی کسب‌توپ‌طلای فصل گذشته فوتبال اعلام شدند و در اتفاقی جالب، پاری سن‌ ژرمن، فاتح لیگ قهرمانان با ده نامزد رکوردار شد. تا کنون هییچ باشگاهی در یک سال ده نامزد دراین‌مراسم نداشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29377" target="_blank">📅 17:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29376">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cB-I5fTAXkgyQR3IvDrliwh8Kf2b05yAPBszlk1heW0nKzDFKtf9jVakIbCsKv8YeHv8W7g119JNJ3cs7viIjEl27QVxSGz8u4--YBV1akjaElpj1RSpNWZthJW-4mE-WN-E3Wtiis_71yu-MgnPtbn_Kw5_8gvMWCgzQnn12GPLcmNUAbfWg2mweY9S8j_uaLMEP6xV0escGutMSOEv91e1XsRBdb-FQyxX9pjxgWCump5AUy0Cs2ZYCJFhgLugeaTB5flw06N6XDrJmsd2To-CKjpeOkhZOpceyQaOj8bNIw6OrOBJVcjq8GwrCuUDRBgOUCcaTOKS9F-H9nCePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29376" target="_blank">📅 17:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29375">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzRFx3O_Npw29Qn6uqdojzcmQPcTYC6g0O4UIl0p2cUUBvRkuQrkm4d0pXGjjvx7bOGWCNrohZLPBpT5_SEbB0rvQDympSNJKmpIW2Te9-2ZpzPcUrxlkInxyuEFKCIfGiwZMvKsuQUieraK7a7joGSVULUDE1fVrJPlS4LnEfd4rDjzwXHfFBgOWeoPCcO68a4jUMPaLEg7uXyERa29jocETWga-SorC6EHyq_OtBkIYI4rERSxVdmBBJczZr1WvjCRmD970w87etpJmmocZIEVPmMZ215UlNoD8-RPaisWNin5FORtRe-kVV3nTtmebyUdazGokYPYA8kPwRxIvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛همانطورکه‌پیش‌تر هم گفتیم؛ بانک شهر بزودی تغییرات‌مدیریتی‌درباشگاه پرسپولیس رو انجام خواهدداد. باگزینه‌های مدنظرخودبرای مدیریت باشگاه پرسپولیس درحال‌انجام‌مذاکرات‌هستند و بعد از به جمع بندی نهایی تغییرات رو انجام خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29375" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
