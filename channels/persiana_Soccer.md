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
<img src="https://cdn4.telesco.pe/file/iIZgDxNvE0QYsCsbx9tvvJPpU8TjLLmiPtTHZWVOwkTatOxDce8exvwbEUWYnDi-q-idtG-4i5sDIT2j-zg1zMqEYv0WTvUPD2s354qdK22Rl1whXjBpSkHHirSmOvEuCicjlFTMMYuMbR1ENXK9KlSxN45IApbJelZx18fCPE1zIiwOPnxDKoo5s7IndSVvRUh5kNNfVU46e74ustR9rqBDBGGEq7DrfU4VxyIWjSZH9DE5ukwW8j56zehYYsRMM1Yzr6Ml3sdfi5jK1rHOfw5YTv2X7tJzDCzPjLHqRsowcb8mDTs1kh-YsfeD0b2xZmlfw1HjyyaOheq_8jSd1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 631K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 11:51:28</div>
<hr>

<div class="tg-post" id="msg-27447">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pN22ZNVFqwoaJ8yyQWkDLazCumaZADBPn0623Pgt1hKcWYez-mzQrEuEktJljRb_uZ2ubhUy44UBxrZMtgnvKU8R9y8pb3itTtzTbEy7XS_q4WMg-B8imfWPASKnP8RXm7hra1bFGdHkyY8lulLL-TM3NH7SDGglRHazweCbioihkKcXq4SEHi2b9li8RkbzrJ2is4mfAVVyGC2JPO5cnMB6DpyfSI_b5f5hnr4l5326sQzlSxixG_JI5elx0tPehblEk-UfVgn0YUluW9TMWyJSCq5DKMUX40hIbEFJJJyPAkB4pSyaVG0JL3qV92ciY0ucZM7dNHeyIWGg7fP4eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2FlCSsJHNlK3RMqM4RW5GjXAz8Ju4IK65fXflpzmq1IKgzFLxrufvQOtw-CQfO2d2BMjotq5CTfCYxRACzx85KcHFs34n08Ds8wmKZ-3OAIj0dT_IIjtNrdMbdpwgcJ3JAVAaRR8-U3VuTN8HXyBhbys-F5ErY-Op13xl0vZBWPJnad2WQvZoLA1NB3mIGndgGm0hYdlcI1TXEJFX806dP9CAsFC897VKfC2A8guGO9dm_uFK6_oEh0VJy4kUfjeOPOCGzUNYIWV6PYJ6f1f_aHpxE0XyHnAY_qdX8bKq_XVnW1jg2BlvHlDbtxkpsp9XJH_N5H407rzyKyM59lQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لوئیس همیلتون در کنار دوس دخترش؛ حالا مشخص‌شدکه همیلتون چجوری به اوج برگشته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/27447" target="_blank">📅 11:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27446">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzcTxbUJlWgboq3rNUhhTOx16EW_m7u5wNSzIsIrsQRClte3n8K2IP2fAHx371oqqiDyan9tP9z__9PetxZwJjswiPcYD6WUOaE5QlePmtxuUiF6zc-E-nn13_wMDwF-t4g9dkqFDO9oRpZJ2AtO5YtVFxPtN8aVDj0J-0UO1piQd-E7j0lj4jqMovYgKtmZTJiJsOLPJ_KH8ujuVGTZMoHU7FezZIJiu1gy4L5gIM5OZ7lr1BvAg81CGHbtLpD1DrBmucgQ4t9KMt3JKb77ayni2jfedgn15M3qSfoDa9L4pn7fxuH8nbojBZQSQMo9EcD2e19evFG3XhY620TkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛جرارد رومرو خبرنگارنزدیک بارسا و از مامورهای FBI: الان ده‌ها دوربین در سطح شهر مادرید رو زیرنظرگرفتم تا بفهمم خولیان آلوارز دقیقا کجاست. یکی از اعضای تیمم هم با استفاده از هوش مصنوعی درحال‌بررسی پلاک‌خودرو جولیان آلوارزه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/27446" target="_blank">📅 11:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27445">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIlN5dM_jkzcKCetKKHW77KMRE9hRrkMKYMIE9JR9uIXLXMUpGDLaVDMOnRlPIAsh_vEFa65swBuHnOUsvQdwcX5qetNRlFUYGUx8VyEI_imR0KaPXTNCjewXwou-otX4quTUO0R3ZgkbAf7-b-KjbJVLTe1IP0zNXEtr4TkGrNALEsyRMO1t8VMrtdZqIH4xh4PwfwTg8AexF9oWSJRvnXqRBTSzAE9dMlupytfx7OzI7VvqTGp-BtACXgVyFHXo2_fkrvFPurRf1imvoLHjU2Io5_PU9KurcdOSs45j3DSuvk7McetEfGQqqpaCWpykDZ5YlGeX3uwR1FazRvDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
دوباشگاه‌پرسپولیس‌وتراکتور توافق کردند که محمدقربانی راهی تراکتور شود و محمد مهدی محبی نیزپرسپولیسی‌شود. حالا باشگاه تراکتور هم بزودی از محمد قربانی خرید جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/27445" target="_blank">📅 11:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27444">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG4eo_bKfYvaHKjEM0UkTcSfEQ3OBc7jorwjBE9LAXsAJZCU--uGMkWowFNFu61WjOtm1FCYrp9aAHH5U08sCFnrCORKzpHrqpk-xnDK0lmhAgwUdLijMJpW0w7ZP7kdgEOTmdguPXRcrXonlVUkftYeRd2FpU-5RBXmyFmCs2IqMZSCoBaVGBuwdZevynlz6oDgo5LgTPSqPYp6VdmrXjMWkRqOG279XBN1vXX7RC1oO_KMW_N6345fh2LJF-rEeOC6xgj_0ZZJsqKeAionw6wcAeiUaR23CGuW3Vg1YySFyKZ4cB6PCmncVf-ZhwnyEp4hZlnKTBchLGFO8tScog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
🤩
#تکمیلی؛ خولیان آلوارز امروز بار دیگر به مدیریت اتلتیکو گفته هییچ علاقه ای به ماندن در این تیم نداره و از آن‌هاخواهش‌کرده تا با انتقالش به بارسلونا موافقت‌کنند‌. سران بارسا بعد از رونمایی از رودری سراغ نهایی کردن انتقال آلورز خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/27444" target="_blank">📅 11:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27443">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5H4Fuu2X8HZ2UZPZDrRe8V6j89NuQrzr4ajYFg82YwZXKOzQgGvQvpVzahR8G6SWo0z0tVXODqGtBdr7vPMIZYluzhvHuNKDogpeUNitLa4qRu_tU_ZDIOCZ2lekFSbpJ5dugCDHkSfhA9R7B6OC_PjLHcAm2FqVU7-CdlgOymflAdHm2i6Ef_YlHhpXbrvaHDZkLGfk4uLHlzDUvvr5Ik8ud2kqDkfQLCGF8BFxJowu2kIytemAB9_NPey7wViuFANcaC3A9NkOS_zaSA9c3jEaPsxIrTdqmFS_NzUZh5IOEs3Ee6EbLYg6zcaL499lTho9BYXa9J0rd7WriKOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترابزون‌اسپورقراره‌دستمزد ۱۷ میلیون یورویی به محمد صلاح توی این‌سن و سال بده. صلاح این سالها پیشنهادهای زیادی از سعودی داشت. الاتحاد تابستون ۲۰۲۳ بهش حقوق‌هفتگی عجیب و غریب ۲.۴۵ میلیون پوند پیشنهاد داده بود. سال‌گذشته هم یکی دو تا تیم عربستانی دیگه بهش مبالغ…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/27443" target="_blank">📅 10:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27442">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWqhSgnl8ZHh7nhyIK8OzanNjji7BL2jLAaEP1T3axe6qyROoH9OYPxAlMrygyeOAYvoE1dwjVslQBmHjHD_OJCFhKsgums6rS_CXmUMx65zsxS08RYPdWzMsj8SKRsDKvJ5Ln-CwU5luRdpA52weBRL92VH6GdOYItTdmOW_L5f9u3bgrA9pLpcF8CI5HAhcmo8krLHlFJUj9fTYKm4GYOVQdnc9Ie-k-s6ixZKFSx6hf3n-2ne-vZ70Ktp6V4_Y8Tw6omqg4qkoTgjgraueIpPHmXeJ1YNAWCEJxJmRbIyAl2YFhWYfUlog1GH5S5yNKZIr5-QBRcWoBbAkMFGXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست بازیکنان المپیاکوس برای دیدار با نایمخن هلند درپلی‌آف UCL؛ مهدی طارمی بازم خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/27442" target="_blank">📅 10:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27441">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e83727b1e8.mp4?token=TU5V4e1FHaL4Y2hIHhwO704leczVYFNlPJN35MPnBp7dwKBuF0EyYjNkdLMp8DNsOtyN_C4Erv0JgCeR9TiOSVRsCdqFC0HucfEiVi8r9JhPXVl9DF6B16A_2EaNkwzhxtr21_ts8thssoJ8-P_pY-Ju1pt59MbeVxeMaKlSztEceglbZV7HX9GuU_3o8wsashzTmk9TRHk6_yvcorQIEvQRAlkju4QYzLpfwzOOE7-hpWSwCUDw9XfZJExGfYk1Ew_coAFcesutaG_DfG29ofWsaN5fjxUNH3aCxbj5t7zqgrdNPe30ztTiDO0Ek34irqvgyK1FQCT5y_m4BnY_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e83727b1e8.mp4?token=TU5V4e1FHaL4Y2hIHhwO704leczVYFNlPJN35MPnBp7dwKBuF0EyYjNkdLMp8DNsOtyN_C4Erv0JgCeR9TiOSVRsCdqFC0HucfEiVi8r9JhPXVl9DF6B16A_2EaNkwzhxtr21_ts8thssoJ8-P_pY-Ju1pt59MbeVxeMaKlSztEceglbZV7HX9GuU_3o8wsashzTmk9TRHk6_yvcorQIEvQRAlkju4QYzLpfwzOOE7-hpWSwCUDw9XfZJExGfYk1Ew_coAFcesutaG_DfG29ofWsaN5fjxUNH3aCxbj5t7zqgrdNPe30ztTiDO0Ek34irqvgyK1FQCT5y_m4BnY_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ علت اینکه یه عده میان فحش میدن و گارد میگیرن نمیدونم‌واقعا. تو خبر گفتیم بانک شهر و باشگاه‌پرسپولیس گفته ماحاضریم این دومیلیون دلار رو بدیم. همین. هرباشگاهی‌حق داره به هربازیکنی که دوست داره آفربده. دیگه‌بایدمنتظر پاسخ حسین نژاد باشیم ولی میدونیم…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/27441" target="_blank">📅 10:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27440">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65599dd5ce.mp4?token=b5-plSKzSjFAXEyc9CADo-YQLGzdtw1Z5963xdJR2s0m6yfmk-lWRprw6izm_3WjfBajucVViIBDhCXC3ziuB254ad0IXJ_VA8zJfiIWy3mAgSu72hCex3nb0zbyeGFaz3WaHSAnJK7IH-zxV1nongjSBblg_PoVjC1NHRDoITJk7sPeeJgl1oEtPj6kwHHhQbLPjkfma7v6lgWqa76XbWvdxurR3jQXCaPh1c61IJb_PQn5LxI7Pv3ia29WKClNLxoqNOaqfn05JplBIJS95vNf7EbcOv02Uz6M-s6SQ94m-lHs5vvzabTPFm2FzO6cZzSYkaGPgY77gs3hg9vApmwbrzZF_RxggB9Q8JTLVJv17zw1X56hunx_jA2G4PJdHd2kCGI7C_BvOVNqBeyzl-8P1DEtzs1Hg6_Mt16rX5WI8fL4jygRf7cIm5gSyz9XTDYbJZePanLO0p-ZByUqg0oyKa-JD4Suyh7Ri9ES-C_Zq7EPEe0fhjOjLvi6g45jsndzBW0zD9PTP-NCahzXL8m5ZgqtEZ1ylKIWYnQr4HOMtTmcRZlEo4GVANtxap6CmeFDSrfuuk-4-aXvX7_uTnV2kdgPKShXVT_SYnL7ad1QStsGB9ozYWNDWePgjYTC1TA25yIcN8d-lvPmvRB8age95u5MVEHavdpbes5tZyY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65599dd5ce.mp4?token=b5-plSKzSjFAXEyc9CADo-YQLGzdtw1Z5963xdJR2s0m6yfmk-lWRprw6izm_3WjfBajucVViIBDhCXC3ziuB254ad0IXJ_VA8zJfiIWy3mAgSu72hCex3nb0zbyeGFaz3WaHSAnJK7IH-zxV1nongjSBblg_PoVjC1NHRDoITJk7sPeeJgl1oEtPj6kwHHhQbLPjkfma7v6lgWqa76XbWvdxurR3jQXCaPh1c61IJb_PQn5LxI7Pv3ia29WKClNLxoqNOaqfn05JplBIJS95vNf7EbcOv02Uz6M-s6SQ94m-lHs5vvzabTPFm2FzO6cZzSYkaGPgY77gs3hg9vApmwbrzZF_RxggB9Q8JTLVJv17zw1X56hunx_jA2G4PJdHd2kCGI7C_BvOVNqBeyzl-8P1DEtzs1Hg6_Mt16rX5WI8fL4jygRf7cIm5gSyz9XTDYbJZePanLO0p-ZByUqg0oyKa-JD4Suyh7Ri9ES-C_Zq7EPEe0fhjOjLvi6g45jsndzBW0zD9PTP-NCahzXL8m5ZgqtEZ1ylKIWYnQr4HOMtTmcRZlEo4GVANtxap6CmeFDSrfuuk-4-aXvX7_uTnV2kdgPKShXVT_SYnL7ad1QStsGB9ozYWNDWePgjYTC1TA25yIcN8d-lvPmvRB8age95u5MVEHavdpbes5tZyY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
تموم رسانه ها؛ خبر از رونمایی باشگاه بارسلونا از رودری ظرف 72 ساعت آینده میدهند.
‼️
تموم توافقات بین سه‌طرف انجام شده و انتشار خبر پیوستن رودری به بارسلونا باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/27440" target="_blank">📅 09:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27439">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDFRJny0lYbcqK0DyLldnBAWsQU-gCZ6Pf14Px6ALQLiWFBo84BBH24ciN419QGP39cRlDPzm0LP_r5riVIPmgBa-NqAogBAMR3qL0PR8AP7bTz6skJP6InIfKqXBbDnc6ZdrnO-sIj_fxNf8OSVSt5osUukvI2lNPzrOvcZRSVF_VzLT7Ef56TaDGfSJSOh30fjg6rzgxQzlQ6g7Zn5Fwi5tZh4E3ugFVUS3yOZVqqzkkw6Vm_gu11rHTOuIHv-zkL4yCTelO0qe5LsD-_O4ltl3apjb8JyNioiSwlE6nUZZTtDi_0Yb7NlfDfxASDJ8hpjEdYY3vp0X1RF-ekrtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
شنیده‌ میشه باشگاه سپاهان در روزهای اخیر مذاکراتی‌ باخوزه‌مورایس‌ سرمربی‌پرتغالی سابق خود داشته که بامخالفت‌همسر ایرانی‌‌اش برای بازگشت به اصفهان این مذاکرات بی نتیجه ماند. مورایس بعد از جدایی‌سپاهان نتایج‌خیره‌کننده‌ای با الوحده درلیگ و آسیا داشت که با…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/27439" target="_blank">📅 09:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27438">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mdi91_RQDN1FUgb3gwoO2MTRdK5YL53JyyHAk-6YZTX5jxuOlUj7g2vHfef2hDmpwqSt22OhHymvKxEl0h2QCtFeMDIQ3vTHj7X35yAu6fdG1apZLbBAIkfXTC07Sv8JogHTfeDOXixqmSY4padpZ5UKILwzTDCAc9vEp8UbY9e8wpFSTIpJ8z_QMwmRWuv08wlylcZqEQ9Ep7jJdLOaq1PDhC62_F-y6b0trSXu34j2O0iiHQ7U7IdWafMhQwb7tcaTQ_H0MYm4to6ySzrXAj6euBno2Vk4qk6yd1nW9De4ekI07WiKtRav6AZfDQ9z_WSN5oPjnq8uiMXuPIOLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
آنخل
دی‌ماریا:
اولین چیزی که من با حقوقم خریدم 206 بود، اون‌آرزوی اونموقع من بود و بخاطر همین باتلاشی که کردم بهش رسیدم، شاید میتونستم ماشین بهتر هم بخرم ولی قبلش میخواستم اون رو تجربه کنم و بعدش برم سراغ ماشین‌های بهتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/27438" target="_blank">📅 09:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27437">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtfXUFVDhVeHXKMhlhxQtnnrmTJbh-eJABrxfrAUy3gmEjXTlnpYU_iNokI3rD1G1OPRa6FIBZnFFgevsYTHg5l3EXI0WZgKU7gGrJbyPrqiT6PE5x7JpbEs1kgLABc95rf4C_JUKadCHYEldqZSN0yOdvBrXi-xx4rRqMuM0cs_auEoqH_EGYdD0mz8UxRpI2eFGVQ0tmWjXkY4IqTjMNBRQCi20Fe-8YC4i58Rque1dy2Lt8ZxIyE_G2jQjfezPFfH61B3trOjacTCImKM_8XWDQhiCz7MtdS-jssCYuBbopRGIYdfBqCWn5VqJzGYf7xJZE31pXeaNu6gWRNZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فنرباغچه به درخواست اسماعیل کارتال سریعا میسون گرینوود وینگر سابق‌ باشگاه منچستریونایتد رو به خدمت گرفت. از فرشاد احمد زاده به میسون گرینوود رسیدن اگه پیشرفت نیست پس چیه؟!:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/27437" target="_blank">📅 01:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27436">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olgbGi6LxeHYkv4aFv0KpWQ0P2CWeuHdfcCfomwVVBMVd79_7eAC_QcGHhO32bAYUxAinYTuKkg6Rcli8CiQSpvemrL0bhEK51M1D6ARv1vqmQzIygtX3iTXJAjXjcKDF01tSY5cKPJV9OQLytsJbBfOMv5adfIXM_YC6WzMn5Rw9VIhkuaIlm8lUr9_U6E7JcFjRtn8EZ12pToPJMmam-kkRSPmA-p8SorN4tv1DGSfcM3GY08O0DH6jpozAfHT0GreclRnRVqHQ432jVWxcnYPTVz6bg38ChfC71h2Y0MGfBksX9e0QUmMHUkHeTwsneTlz_NwFf3OE4txU_OMdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر ایرانی خوزه‌مورایس‌پرتغالی اعلام کرد که بزودی‌ موزیک‌ جدید او منتشر خواهد شد. یه‌ بخشی ازویدیوش رو درکانال دوم گذاشتیم! دوست داشتین اونجا هم‌داشته‌باشید محتوای جذابی توش میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/27436" target="_blank">📅 00:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27435">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da4d4aa52.mp4?token=IXohWIPasMWkqvDWXV1-uP9yrCnC9AGryqJnZYH6IYEVaWggvB-v23zK4MGk6rV4FdaYS7IvGxJdnkV9TQ0wLNbfRxBn06zhZt4qB0mzT9jnGKQDEk8a5voGflhWB93s9eteFV1OwMqszwJAFnAMXr-vs4nauqM2_DbeTvGOUK5Pc4wTzwg_szpiaen3jD7RKGQr6ViOKldWeEfknybRgujj0eTFbD00qKevDapLzGA73cxWbwPMjPz1bn-SrIFxE7yzezq-YYCl6V86EUswWLziK6Y7B3K0_5MqpStn4xf1soFecnArdQogJzznAHOBah7-75dCsHabT40hYGDbnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da4d4aa52.mp4?token=IXohWIPasMWkqvDWXV1-uP9yrCnC9AGryqJnZYH6IYEVaWggvB-v23zK4MGk6rV4FdaYS7IvGxJdnkV9TQ0wLNbfRxBn06zhZt4qB0mzT9jnGKQDEk8a5voGflhWB93s9eteFV1OwMqszwJAFnAMXr-vs4nauqM2_DbeTvGOUK5Pc4wTzwg_szpiaen3jD7RKGQr6ViOKldWeEfknybRgujj0eTFbD00qKevDapLzGA73cxWbwPMjPz1bn-SrIFxE7yzezq-YYCl6V86EUswWLziK6Y7B3K0_5MqpStn4xf1soFecnArdQogJzznAHOBah7-75dCsHabT40hYGDbnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی که اخیرا به لیگ دو روسیه رفت تو بازی این هفته‌تیمش به این شکل با پرتاب دست توپ رو گذاشت رو سر هم‌تیمی‌اش تا دروازه رو باز کنه‌. خنده های گزارشگر رو ببینید که برگاش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/27435" target="_blank">📅 00:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27434">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFFqd4LBjy1kVF-1TFQAGoO9d9yLtG5vfC2W5ENQurLM121SV7dqcXakO18bqrngjVjUdeKVdUHpmmJ8aWwG-mBl5KqXUHQuGxhStjItudk0an1izn9YHe7Yy59iIAPOZZdxz_j95Kc8XQoh-NSArrjWVovKXlkR4tUxt_ZW1MWwkOw8aRuUr8gqMvlel7rnb2f4-1zNFo2Tlxb1lR0-6FH3DMg4aQGVkcsQiUOpXWEJ3hEeoCx8f4FyuWjz2XFlhwN9g4K8mKh7xHweDj8D-5mzxJV9A73YL0IJJoGulBF2U0eumYIb_TKo4vWJSMxojdaDCruez4SjJB0_ZDsv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
‌از باخت عجیب آرسنالی‌ها در امارات‌ کاپ تا گلزنی اللهیار بعنوان یار تعویضی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/27434" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27433">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLw5lMSQ3Td5UOmJQ5uGvDsDGC7fSs62Tp_3oseZot6N3mz9lkRuSHoGzdlvEoGDWY_2McR9pPhjxuzg32DJTg1oCxMOalz2_j4SWZtFGdT_76y9BQ12ogWyRFiNTNNpp2mHVArVtiRuUl6dbxXC83H0qdocvbHgjk_EWuLv_kEteCf_mGEQl9vtHP516ritmkSmhqAS5a1oAvqBDFNNVrbKfzAzNVFwtyGF5hlIxg57tYJxGS0nWalpASqKXllwFNNULk585yduVQnI7IvoAm8uAk1vhMbEXP2m0AHVX09JieKhyynwMkgw0d99rk-xab8gOeS7CRDkXtuhk0wDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وینی‌به‌رکوردرونالدو رسید؛وینیسیوس جونیور درفصل‌جدید نهمین سال‌حضورش در رئال مادرید را آغاز خواهدکرد و از این نظر با رونالدو برابری میکند. رونالدو ازسال ۲۰۰۹ تا ۲۰۱۸، ۹ فصل برای رئال مادرید بازی کرد. وینیسیوس که‌ازسال ۲۰۱۸ به رئال پیوست، حالا وارد نهمین‌فصل‌حضورش‌دراین…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/27433" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27431">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQDVU4urNqoLDWCp2MK8NxWMV0M6rNDvhXHswFoY3VRhLiUnTpclrGrOwi1evGmcB8rZFYCHo-sqfNv0mBfa8Sv-XFN8kLcL3CiTRyxBaa2WRMrLl-Rd7dyGlusCPTf58U44IxTEG5mTsYCrFRVWBwUKpZOxQgm63CIZh98_hlqco1oTtJPxztVerW8_WsztBXwfvmPgeMhyDJ71r2ZxH_iFxOFb3Nvt7JHHluD7cvwUZipllOs3p83MUezeCh58kg2zFQhWcML8ACqzz47XGWVlZiHy--nT6cQSzZjojLUIKjJUzMIhxGGYTzvm7A7xZAZwJFWDBWCYyJVePBWggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
گاستون آیدول منبع معتبر: بارسا میخواد آفرش برای آلوارز به‌120میلیون‌یورو برساند. بازیکن هیچ علاقه‌ای برای بازی دوباره در تیم اتلتیکومادرید ندارد.  هنوزشانس‌خوبی برای این انتقال وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/27431" target="_blank">📅 00:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27430">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeQpmZhq9rjUnLd5RUzT3A59nil9Vr7DX5G2cqcoWjzOGj6RFK7zarakjYrvuAon1YabFHhHI6zck1u7bcQiJ6fb4P3nqdR6G4caGtEDmZCX_WyXI9sXf9Rv57MKsmpP5Nvb94_yChRBNPkRJmc6PrC-TEe9EjnNUz3JVD8BaH9AKIJG6c6bslnX80MQtjMGX0Gm9X1Vvm8ahy8dEfnl2TbUa320RnfxrEaYSUc1Y5M6o1PEj10zJB_BwcGTI9J64BmJNZ3lkC1FwMZs7WOQtgV9U0I063O9SiOOow4ShJUpQynftvpJT7ByfTsXDfMumCpC_ZzmTSbqlwiiopSCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید: حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/27430" target="_blank">📅 00:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27429">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oM2RGchvJA9wJ7SutR40kEjYCyfsYsI80mcfKJMD4lZARTD8W4HxKPN0iRP2ZrYnaNCNgFw9mZs5LmTs1xQZxLX7mDnqMreu86hT1NAxMUg2PDYX64KE8pOGOLLcOpmddEamDa_vhyvD2z68T8e8PhueCBhXEuLNiJMMLC9EHHPLpguENLvBKQ9xAYElttNUZny079sn_uw28GHfrTkGTnAy692KfsnV1dggeYikD9n6WOdR1Ki2eBEq_wuotcNTT7ggTQz7ApKx7osVYPdwX-_MhzCt253V1pW5I6g2nCpkXWIz2-tUjONbwaPkrLUiUfXIYQhrxvBc9K1Lsr3N9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آاس:
براساس‌اسناد داخلی‌پلیس، لیونل مسی در جریان جام‌جهانی ۲۰۲۶ باچند تهدید جدی مواجه شد؛ دریکی‌از خطرناک‌ترین موارد، فردی تهدید کرده بود با مواد منفجره وارد ورزشگاه‌شود و به مسی حمله کند. این تهدید به حدی جدی گرفته شد که نیروهای خنثی‌ سازی بمب و سگ‌ های پلیس برای بازرسی ورزشگاه اعزام شدند که خوشبختانه اتفاقی بدی هم نیفتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/27429" target="_blank">📅 23:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27428">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJ5YofukaXLyqKFpOdikw3UnovgcCNLE0DNisDunVPN5SRMLPQfmBQWTtdPSHax6MhUrY2WgjNs8BHG9LyZOtUZYOz_MWmUf9ojcR-U_v-13UuHXv8TIdlk-rZbcbUuMnqTxlU_IvB3DQsWURl7Owo3W0N7q1ekNKHN4Mqnm9iOllJoTt9VhKaNjzINJPCuT76uWm4_9YawN8H6uQSdyoyGZ_7-xzTUVr3UldW68lr5sueEnuPSEIC8FGecnoKwkEC4lLsEin-h6knqXq5Os396oxJxo0jydm7_eSxpErMM3iJ2dq2MlyDt17YiMYkhy2jYdv-wpTlbULSwynaqflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ باشگاه سپاهان ظرف روزهای آینده از بین‌ حسین‌ابرقویی و یاسین جرجانی دومدافع میانی فصل گذشته پرسپولیس و آلومینیوم یکی رو جذب خواهد کرد. یک مهاجم هدف نیز جذب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27428" target="_blank">📅 23:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27427">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d19eee8d27.mp4?token=V-DdYeyrvexIAOGPerhFor5fN5pahlI9Cq9WX9TIC1OBaRnFfVKee7xDbz0Xe2yetLw3--Jw4cZxpH3b4gN0Q2RqgVNF1t_9mG5tqHJIcAOtzcNCLt9Lvf_RrlK5Rwkc2V1VZe6cJwvbjFsfLHLXEGms2aK_kCrZx5wYjBqaCZQYb8KznIJlOIIvDZXHtux9uypcJxxvIT42NKy_ETNGcnlV8_4dg9G5kIS1aI2UaEtxWfTZVAZpcnvIXgDKol1O14hD_YxCiZfvrU7BRKrML_nEB8L-xoJvDAUHki_r16KbfUXWe_H3KXVAx-iy_oQ1MF7eNPqendpFplXCmiVR9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d19eee8d27.mp4?token=V-DdYeyrvexIAOGPerhFor5fN5pahlI9Cq9WX9TIC1OBaRnFfVKee7xDbz0Xe2yetLw3--Jw4cZxpH3b4gN0Q2RqgVNF1t_9mG5tqHJIcAOtzcNCLt9Lvf_RrlK5Rwkc2V1VZe6cJwvbjFsfLHLXEGms2aK_kCrZx5wYjBqaCZQYb8KznIJlOIIvDZXHtux9uypcJxxvIT42NKy_ETNGcnlV8_4dg9G5kIS1aI2UaEtxWfTZVAZpcnvIXgDKol1O14hD_YxCiZfvrU7BRKrML_nEB8L-xoJvDAUHki_r16KbfUXWe_H3KXVAx-iy_oQ1MF7eNPqendpFplXCmiVR9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شایعه‌امروزازدواج‌رونالدو و جورجینا باعث شد هزاران نفر مقابل یک مراسم‌عروسی در پرتغال جمع شوند، اماباورود عروس و داماد مشخص‌شد مراسم برای یک‌زوج‌معمولی است! کریستیانو رونالدو هم با انتشار استیکر خنده به این ماجرا واکنش نشان داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/27427" target="_blank">📅 23:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27426">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1bEIvSesDfcEtp_mEpK8UamGFNnx0MlLn1hCTmBjq3Tak9RXh-5fjjYRmdM5rq4fqprTKAQMAIUKhvVatU3nSBa5QBt4-srpVBNJdxnzvtSqm_prirP1vJK3tizo6lBaXHaoFWc4VORnFxV3LVk4_CeYsuMH8_MdmlgSiCkaP8DgI8-VYqc9xwgx77l_T3kxLB2Y2Lh8l8lTExaPgPrYEuUsN9JDw78RkOOhQzNbZnzInrp3I8xXZwjtBWKvE7iUbli5HWIQeahtRPMl3bijHGZ6g3PorMx4f_g7j001HKQoe4dazt6r5F48GLgiTSdJPykavH679QBvbBATOa-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27426" target="_blank">📅 23:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27425">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5Y8nIu-PcqF4LEg_VqMOEOr0ZlenLTrVtMIrtzJt2cJvtSD8F9IbjvsPgpu3oJ9OznZkiNogbPIv0OEzTbWS9JwSuRWTiuN1jsuw4CLldPhcEym7OCUu0nccxjhPG6Sjv7aUXsTriAeQeeIz_GGnjFDtqKtZ-zXVQA4exaSJFkWe5sAm_jVtQGgBBFJRzJm5kKBHUW4edzG3ZWvQAYPHgRtIWzntfyjUdD70Xb59yPpafB_JvyxdU4qSH3ITJXlqHKlxMWaL9jlCgX-DeiyKtN2SnxtDWj39vySI8Wpb-Q4uY2yvqrc-PI9O_Yesv-N0rROhuzQ1Jjl905VC8mR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا؛ احسان پهلوان هافبک تهاجمی33ساله‌سابق پرسپولیس، ذوب آهن و فولادخوزستان‌مذاکراتی‌باباشگاه فجرسپاسی داشته تا درصورت توافق نهایی شاگرد رسول خطیبی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27425" target="_blank">📅 23:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27424">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv-MrJUSYrMc98K4fdkqBolWsnKoOFIe9IYt_TzWwiYLHlBPwT0NrwXm4SSAt0yBnmWPhLyRvHPm1FVDU4wTblEAA1du_ucvHqnNBwp82KxwqWL3pU_vBIdUxPoGZnCUyHkghexaYdnQmjlWkwVRiP2HOn7GMlwRu_kdsOLjZZ0qrAXXROtYFI7M5yCk1mIArO9YXFkbzL22d_YzlPjSfEk1X4AYSawIuc9HfBmLvIsNnX95dQiU1IHbsVhQUSLh234UrYrX_ZSy-buNFLuTP2aK-NJaEsWDyYA9J3XJr-yLZSCvwtPIpqTiBRwp8tGqymOQuRKZeNxRnFzd26e-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری از موندو: سران دو باشگاه منچستر سیتی و بارسلونا بر سر انتقال رودری به نیوکمپ به توافق رسیده اند و این انتقال بزودی نهایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/27424" target="_blank">📅 22:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27423">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXMtOo113x3b1nE7mxhYpX_saht_RJmRl5Ut_PzhbhGsfKRBO1l2BIdpY0M0MxPbqYT685UF-BYMCIMZDQzM6F_nqqIuLLgjhLAhKR3S66GrgQx25DNec0WzxWIxWPcg3wwClyGv0Rjrj72v5eA_VHDv4sem810AxI21cfMq1uXtUijm7sn7hQtkDTxlcEB981tYqQMnND7YKPyXuHVeyniA-wDmAOGBnqhURHt3nI6A3hbQG1T85xXsaoMoyUDAbPaGwzO53Y2n4uECEK-5Yq39QPeF97VI2zCXzzCsGwsNrDg9MrMV8CDIPdMYw-HpH3Q_2yRNYkrM6aISjkkNvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
اسکای اسپورت: باشگاه بارسلونا بزودی 55 میلیون‌یورو به‌باشگاه‌منچسترسیتی پرداخت‌میکنه و انتقال رودری به‌جمع‌شاگردان فلیک رو نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27423" target="_blank">📅 22:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27421">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f508d354c2.mp4?token=i0H00PnIj8QTZF09txuCtnlGWnV4b9ikwd0kZF0eM1A-wnhML53g6wBNhv3OM8xrzDUwBoSxmNgb6I0F4-4mgZh9Cd0jocGXliSUU3fWQKKpcqj20MyF1T_DC37hT1I3Ph06fhXOUah0Hf3MbJbfOpHMFSyS1Lab2CHN-1fVChesNXRW-zZgOaSgJpxl5SUM4aUBX5eg32uCfa4k95gGi-iCP4qvgXEMjy0Trc8Jmhw8rr_dP7ojtH8j2_wdMiposVDox1-GHDITgs63xO1snY0rMlo4a19-7fkgz_9VWcJjxxrWMxU_K8ei2mdUxoC33veef3T4B4qcCuvDDgoG0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f508d354c2.mp4?token=i0H00PnIj8QTZF09txuCtnlGWnV4b9ikwd0kZF0eM1A-wnhML53g6wBNhv3OM8xrzDUwBoSxmNgb6I0F4-4mgZh9Cd0jocGXliSUU3fWQKKpcqj20MyF1T_DC37hT1I3Ph06fhXOUah0Hf3MbJbfOpHMFSyS1Lab2CHN-1fVChesNXRW-zZgOaSgJpxl5SUM4aUBX5eg32uCfa4k95gGi-iCP4qvgXEMjy0Trc8Jmhw8rr_dP7ojtH8j2_wdMiposVDox1-GHDITgs63xO1snY0rMlo4a19-7fkgz_9VWcJjxxrWMxU_K8ei2mdUxoC33veef3T4B4qcCuvDDgoG0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امشب دربرنامه تلویزیونی خود از کوروش اژدها کش و امیرحسین طاهری دو خرید جدید سرخپوشان رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27421" target="_blank">📅 22:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27420">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec041c42ba.mp4?token=DeMSXi5E6OKe1547JFO7ugm6JQtjdntGLzZUtwpr67-DPn9_TTV6JvollYeylJom0e_dBog20ovACJg-1ZrEtQLjp31RsLIXdTIrFVsXDtcGglwRHlhvvHKcc1PN3erjzk339QjSNKNsEpbmS9FF3rhgoolZozRmsRc7hyTVy5LSKw-sthdDLISmYEumbN0BI7B7raIDcofTV3DjGEDhgBDB7em3yUGum_mZ9e0bDSzGfvL35vt10qzrb6D5q-rstMqYghDfcVgA2L-EJgjm8giK0I1NAzTnMEuZiMtAKiL6mlqq4ml7YMjB41od_HCZlq6wgqaD8gBIUspYiOK73w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec041c42ba.mp4?token=DeMSXi5E6OKe1547JFO7ugm6JQtjdntGLzZUtwpr67-DPn9_TTV6JvollYeylJom0e_dBog20ovACJg-1ZrEtQLjp31RsLIXdTIrFVsXDtcGglwRHlhvvHKcc1PN3erjzk339QjSNKNsEpbmS9FF3rhgoolZozRmsRc7hyTVy5LSKw-sthdDLISmYEumbN0BI7B7raIDcofTV3DjGEDhgBDB7em3yUGum_mZ9e0bDSzGfvL35vt10qzrb6D5q-rstMqYghDfcVgA2L-EJgjm8giK0I1NAzTnMEuZiMtAKiL6mlqq4ml7YMjB41od_HCZlq6wgqaD8gBIUspYiOK73w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مرتضی پورعلی گنجی مدافع سابق پرسپولیس هم به این شکل مراسم عروسی‌اش رو برگزار کرد. همسر مرتضی کرمانشاهی و پزشک هست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27420" target="_blank">📅 21:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27419">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2458f36d9a.mp4?token=XoumrurUggW4GzJ9wkICHlvOTWh_gVPScAeC6gUA6FKvHS4hVmwWTqlGl3EerBHJb9cYT7RduIJlZb38J2Eky7frE4aHa6ScP9D3K6tjmBf6OHIAUQF4qEB2wSY8L4DSgMVI_qUQnq-4F5QqzH0OcxSW4GuHh6JHJIn8fR7wfe5r3Vv5gCwkmg45UPkiESyJufh4tyCztYDAiigZ05ot3H4FgVnlNIAFHsVj9xbRT0pCLe8Q9nUiXtwD7Pn-3RQrF6ODl-pHuVFZ-qRLMm4T3m4tVHCWCEPU8juf1KaJ1iOYtPzmmis7TsaaQVsFoRG1qHubia-SnuXU80TTYagLizzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2458f36d9a.mp4?token=XoumrurUggW4GzJ9wkICHlvOTWh_gVPScAeC6gUA6FKvHS4hVmwWTqlGl3EerBHJb9cYT7RduIJlZb38J2Eky7frE4aHa6ScP9D3K6tjmBf6OHIAUQF4qEB2wSY8L4DSgMVI_qUQnq-4F5QqzH0OcxSW4GuHh6JHJIn8fR7wfe5r3Vv5gCwkmg45UPkiESyJufh4tyCztYDAiigZ05ot3H4FgVnlNIAFHsVj9xbRT0pCLe8Q9nUiXtwD7Pn-3RQrF6ODl-pHuVFZ-qRLMm4T3m4tVHCWCEPU8juf1KaJ1iOYtPzmmis7TsaaQVsFoRG1qHubia-SnuXU80TTYagLizzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سوپرگل برگ ریزون و فوق العاده تماشایی اللهیار صیادمنش در بازی امشب لخ پوزنان در لیگ لهستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27419" target="_blank">📅 21:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27418">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDgsUTis2Om4z1BTPKbu7bYZteXoWWfEugMePwaKrc6vLO1JWhk7rHfRWaOQruKK8H0o6EzGJH-To1S-iaPztkrtDUZeISmd0bmSGdcP8ELgqj9mSB_H-pbpf9uimyS8-4b__Gs72hlx0cKMfZQmiKtk2gu9ShOjhZE_xhrJ5IjtNltQCeFMTq6gmaGLJ44SSy-bj36AqCVbNAH4dl63N_2jXW0U1NrLQBEbwDb3Lojk3JZimZnqKYipr6pwn1j3g8PxbFr3EeIb24JAfXtxw1fLYIy91aykyrCkBO-aDNjUxFslrvGXBMlN3oUpzoCCVjachV6Z0dPj--wGduIPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تیم پرسپولیس درآخرین دیدار دوستانه خود پیش از شروع فصل با یازده گل تیم منتخب کرج رو شکست داد. پوریا شهرآبادی مهاجم جدید سرخ‌ها در این دیدار به تنهایی موفق به ثبت زدن شش گل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27418" target="_blank">📅 21:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27416">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOE01qAQOvVwYLkObewLvpBQ5m1AuEV_vLA97oKUcu6yQCHXRT_c3Op00QwDTPeYq5onk7T2RYH3sVvh9UEQMVOYQFclOFc3PEXpxuP4AAVIis712WH1K3r6RLSD9r7t31akIYerypWRcmy9K-XOnAoNhV053m6f8gP7VA-kGGw_lcjVUhE9EFjaZJQ45dDCV6mnJuXHpizR5hN1NcId3jVwHbS8A36drR1t6JUApbihYG1GZc7HcCBp8X67cRVIWosZVBE3yaiPiizjHPVCTJ-qM9zPWZBmcGnPeLRFKen_OrmQCxqbSfPs-CW9oy9J1eYHzgSAxRCFfHduPF32Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojScIx5sg_IlJsvhDkPEjaBHT_d_G6Acy0ujEF9N3_aaVBuWaJnk7FpQ1ZbPcAX0ZQ2D_My9sQ83V2Rn8csSGjImx60zjg2vaOENcJ7MHTwS3XrNfqVf5vFkESrQZP1QfdFkDVfxFr3QBMfiaBQF--rm1T9UEYHBJlJR0L0u-lC45mJeBSJKjcDZX_Crm5vIL-KNR_TmjALW7kxI3jDfAy6EUIOTGSxhB_hPxh9BctODy0jnjkgqZnsWFrThTRbu5-DqpEnJaGPDpc53TqUplsZvgc1ziNqZO_znTVTbWau7PDLUOJokS5wTMJIMvPythETb0Lrm4qtfmsjh-mGrRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برترین‌گلزنان ۲۴ فصل‌گذشته لیگ برتر؛
در ۱٠ فصل اخیر، سجادشهباززاده با ۲۰ گل، بهترین آمار گلزنی یک آقای گل را به ثبت رسانده است. اما رکورد تاریخ لیگ برترمون همچنان در اختیار رضا نوروزی از فولاد است؛ ۲۴ گل در یک فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27416" target="_blank">📅 20:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27415">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srxfIUNdI_rfd1puxFs6sHTPv_zX2KX1_FyC2wzEE43c3_Jj_JuqtKqbcSYNodPiiDKuBYPWH9-5qsttLzUe3npz0zAVhKLA6crQeVYj7HOZ-SA5vCNSPEtmCboLLq6vTBvAxtxOBd-DkmfWccgn01Jj7VHzQfpUVGRg1Dykw8syLiNnN54Xugn9hu9mNokrWTgOuhyzupCGkbgakI-hoXi0VvvJJ3d-Wf9oenoUGSOjSrrVMMVJra-xyH20xzUkE1dY2zAzycFoEy4JguKZDATIPGYc_SlFepWFlR5-vBOzSNdjkS3gXDLWkYfaGeNAT2qR-riAzpyKMsi_lE5gOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ جواد نکونام سرمربی تراکتور خواستارجذب آرش رضاوند هافبک تهاجمی باشگاه سپاهان اصفهان شد. احتمال اینکه با اشتراکال مهاجم تراکتور معاوضه شود وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27415" target="_blank">📅 20:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27414">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58a8a9a5f5.mp4?token=WkSBLRb-eJHcuHdxbV17Bfanih6fzjIzkXJCvKO3KWQdWYZfE7d0fnlC15piEiyi2C31mMfBWLJvLg6t4rGc8It6QqJRSCStBfgrxdFqzHrG1tkfaVKBNNoVgeElrvLcPQ7afHb29U--kRsEq7y8uiNxH8huSmWbm-kk2NeqXnduObNsmyx2zTB9Ap0afOEcT5z0k8mCY-bd_SIkOCxgWktIDMYdnAUIEZj_9RSu08MIrUHP0xFxUaiA-3HRv1uV3Hlg_eEYTKR0ZFlzz6w9FI-Nz9xGgaqojRytiOtshEawroix4zTuJUAY2p_J_rr_Sfzw6rDFV4N9j06DHkGivg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58a8a9a5f5.mp4?token=WkSBLRb-eJHcuHdxbV17Bfanih6fzjIzkXJCvKO3KWQdWYZfE7d0fnlC15piEiyi2C31mMfBWLJvLg6t4rGc8It6QqJRSCStBfgrxdFqzHrG1tkfaVKBNNoVgeElrvLcPQ7afHb29U--kRsEq7y8uiNxH8huSmWbm-kk2NeqXnduObNsmyx2zTB9Ap0afOEcT5z0k8mCY-bd_SIkOCxgWktIDMYdnAUIEZj_9RSu08MIrUHP0xFxUaiA-3HRv1uV3Hlg_eEYTKR0ZFlzz6w9FI-Nz9xGgaqojRytiOtshEawroix4zTuJUAY2p_J_rr_Sfzw6rDFV4N9j06DHkGivg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
رودریگو دی پائول: یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27414" target="_blank">📅 20:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27413">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5820aa32.mp4?token=W4PJ6zr19c2quIYOfA2KuZ2bzprPjfnG7cEwCXTPo7n6nmlH8Uspg-7m1dq6S7ak8QFDfpqR9WnCJhtKVUedVo_QO-mWvRbl8OhcEkCGemcLSVypK9ctOEZXEsEdrsvPiwhzPqNK4Y3gTv0YrI1ei1YLfbWz5SUXjQzM5H6lpkVCJVOirRhpsRpWi9T9Ix-2jx5-19FTKMcEhaI3sYPIwyLrnr1hv_V8ppHlKvN49F2-izZXRZK1ysYqKKLU2wBciMkwK65WNu8U7Rd0cPvNA0wWCnEzyC9en0chicXddTlA0Phm8j1RxCyuFFiyQdhD648sx_lEffOeRhx7t8h1C61XCyKBVVto6WwkTHpNRzU-SPwvv27c1q2Q7U56_ZzhDDMo5E0PILrY8KiIMJ65vURKV6ogNVJzqBAiUOIRWiNQO4DeiS2i6hKldoly8MfIgmSpXcoH2mcy1pQSWSkAIYFG5BP2uMY39f1L2w44rL9qwYGpCC4DIaWLu56wXHSpDb79iGkKzrkOcWCya1_PVnisNu6SRrM0yyeaa7QPcFYIltllRCoAnhl4Gq02LtRDL4ig4N64bvxpH5l4hyVtdYETZZ6cjjFoAAVb7k2RzU-ff-bjQ1qlmZ2GYms5XT_vWCHeh9iuTLCKH4KnIeWddQ8XBOv8w5XrDjErh7Sj9Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5820aa32.mp4?token=W4PJ6zr19c2quIYOfA2KuZ2bzprPjfnG7cEwCXTPo7n6nmlH8Uspg-7m1dq6S7ak8QFDfpqR9WnCJhtKVUedVo_QO-mWvRbl8OhcEkCGemcLSVypK9ctOEZXEsEdrsvPiwhzPqNK4Y3gTv0YrI1ei1YLfbWz5SUXjQzM5H6lpkVCJVOirRhpsRpWi9T9Ix-2jx5-19FTKMcEhaI3sYPIwyLrnr1hv_V8ppHlKvN49F2-izZXRZK1ysYqKKLU2wBciMkwK65WNu8U7Rd0cPvNA0wWCnEzyC9en0chicXddTlA0Phm8j1RxCyuFFiyQdhD648sx_lEffOeRhx7t8h1C61XCyKBVVto6WwkTHpNRzU-SPwvv27c1q2Q7U56_ZzhDDMo5E0PILrY8KiIMJ65vURKV6ogNVJzqBAiUOIRWiNQO4DeiS2i6hKldoly8MfIgmSpXcoH2mcy1pQSWSkAIYFG5BP2uMY39f1L2w44rL9qwYGpCC4DIaWLu56wXHSpDb79iGkKzrkOcWCya1_PVnisNu6SRrM0yyeaa7QPcFYIltllRCoAnhl4Gq02LtRDL4ig4N64bvxpH5l4hyVtdYETZZ6cjjFoAAVb7k2RzU-ff-bjQ1qlmZ2GYms5XT_vWCHeh9iuTLCKH4KnIeWddQ8XBOv8w5XrDjErh7Sj9Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27413" target="_blank">📅 20:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27412">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsB8ly9zFZqa9SRcM2-16JdFZTRmux3O2fCenVIh69ZXiHJ3bNw4hJsL-InxMXt3xK-Gu3FObXmpvN7af5yAzgf9dgHbxPrBmNvI4HQX1OILp9bvp0TVea5DzsXujWbetDXZsqj7dy_Psj7Cq9uaQ2WKwsMYVfcT4yBcnklXtpWSOdwkYGqmmztrM2iKqPhVYs27eZQqdw7zpaUzQN1CpuW8cWp92GrmpkuM_RdpkhsyPsA3ILEppWx89ZzhugggQ6USBG6ZQRTbU9NYGef7zT1GESSxi_ZUzKKgPeU9Gv7VW0SoqPeHhH8gvAIqDvM0XjFQRqQjtHe6WcseISyG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27412" target="_blank">📅 19:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27411">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNmPz2WTuLs655l5rOHsrZDyKZYE2hHKPeKLwTRwpgdJdoqOmKRJm50O4pIjPPV3JUI_IO3H6s6JW6fEyg516LcbIeWcfVSvJogeXuUbkukg8JoBYd6p8zWXPrrrgbuWCAng9aWXVx8p1vHKq2np2c-TpBXaHSu9xhUtg-DwK3Ccv0asZQEicrBeoJ0_2rVIb92WdLfTuR8hoLmtL4AD-IZK4yCalrJRMMCvA09ubvGoVf4jW81-AkzkBaZXjGQBfLmkJPV-20lyefOMrs61zz0ZK-81eXBvCMWjM36ejUJBTtl5EVJknOweadu2JWIigFopOBV3ugvBA2l6pIqGwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تفاوت دستمزد ماهانه موسی جنپو در استقلال و تیم جدیدش؛ درپانتولیکوس ماهانه 20 هزار یورو میگیره در استقلال ماهانه 140 هزار یورو میگرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27411" target="_blank">📅 19:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27410">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1wnD-Vvglzdt4yDblwZXEliCZ5Itck4xN7590_gTVIEbREcK3xDuXs9h3x7k72mLnmyts9FWZRwz1gQEqSYbqQOOhZ1TMzCuGJd_mJf0-fB5Qs25Ata2ykkIvD_msVK49IdTtN_JnbreJZ8v4gE3-mX0MdbM5rk9zvasF9k7M7qHvyUFtQAjO9f2ChDGYKmHpjFswXDrrPiaIg0DxNDBcqfyu6ip96FGsjmR00sifVU5P25mkQy3kOhNuFBVDKSjxmmScL2ZDyA8SRFxg1yGrRXAIp9znboT5r2SF647i9nI_CT0jaMNhIqWO430d8DQOLIR4MRY9bq8wEuPO-uAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تیم پرسپولیس درآخرین دیدار دوستانه خود پیش از شروع فصل با یازده گل تیم منتخب کرج رو شکست داد. پوریا شهرآبادی مهاجم جدید سرخ‌ها در این دیدار به تنهایی موفق به ثبت زدن شش گل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27410" target="_blank">📅 19:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27409">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej8Y0RGtvsZlHAFAUffMxQ2dRyZrM1EglGjpHIFQD38URfXxtf5bwzy2nCsgqNijv3XjtHbB8YVeRBnlvyBAwLj4w5un4--RrbhyTGx5UOcDcIjVqIbUgaHf9Kk43HQ7g8IWydUfN0c3slqfARN23s5TyhofqyfAwji3q7s0544NWsX4XvGkMywTRm7r6i0BVesYC7l1nj54pCdHp9TCA9X4kGHTwElcqYqK1-PJh13n8GH9CGZMXrEPAtZHbBV4gioOWh7nT1fr41iDRfRgEkE2lfD-6hbglsqXYuvP0VB5r6PmK5XZeyBe5IeUBX7-oYngVsQiShamvlSvByS47Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛از دوئل شاگردان مارسکا و سیمئونه تاتقابل توپچی‌ها با دورتموند در امارات‌کاپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27409" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27408">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ66F1HykJfbgV67AZkfZrNY5z5p_adUZRGNIJF9WyehRdme53gR01hq1FFwAheu8FzkPJxNUHJK2y7c5Z2aOGWiq95PyZexd1S8TKoVtg01pbPTb-ZH7nq_SG_Gk_gPOe0u5C2mga_EVduKDFCScaWqNCDKrb5jD06jEqkApnoNr3oAlxDBu7VwTTZnbyMCXm2MvZe4afSHGaBz7W0pRH-6bwM99kAK7nBwFrymwwuWFC20IRzfo1JRQFZK45RNjviyZcn5Cs-gE_4hUYWjzV-JN99cn1-MtClwfxYlaq7mbR-ZTfNEc084Q7cYHDpmvKkpKnZmM7eCC1yR0ztP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27408" target="_blank">📅 18:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27407">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faz1PoZ1hZsEBBIshlZbr6b2Mpthw7Wr0IRE8P5V0PeKuCkDPHpVMXAbiFD5-VNQCty34-_g9tPMljmBHfWB0_BA5CogjHWPi_YJDSSCw7Na4TflUJY3er9-Aegf8QBe95uB27m3946xUbWzpj6_X1p0YtjtScAx8xWOJ5Z7KAtTvZna3jJP1D0TfZECyvZT9i5OOI1SNhaJFREir59SZnHukSlhY7cyIFBVi18CA0-zEFunl0-T0PtEUtTZRL_YMigRtmowySxiJZuQn_i95C4QMySyQqz536ags00rwJ_eoXE435tmKQZRx4DhS6Y_MQO2gPAPxAASyXnTASFDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فصلی فاجعه در انتظار روسونری؛ آث میلان در اولین بازیش تحت‌نظر آقای روبن‌آموریم این فاجعه رو بار آورد. حدود یک ماه که با تیم تمرین میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27407" target="_blank">📅 18:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27406">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9154dc0f9c.mp4?token=ARQUYkx6QmXv2l2GMWH6Uc3s4Vy6PPE2irhvRD92m3jMjVD2-Zf9kGv_QMkMqGwKtxKTEHeXCASvYQkyozdZPKIHxK6c2KTREhgy-qramdXyq5jkJDGiE0qAQrpu0F9g-SlxDz99omhKTJ_5Y5ypbJHDLC2g5tmdg3pt7jU347wQcJc-8IWyqxHN3dSL7MEl6CntslQtlBZwvu8FPj4RHR42oH4gla34gmyPFUGQrY2LG_AxRVQjAZ80ssAU_tfKU_KjbFDyNSjzRhO89xp-gsZR8RNB3-harOu1ItmhRgDe-RvKmuRtRA8lFtzrMMijOnY8B5fnJahAuDRJMnf4Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9154dc0f9c.mp4?token=ARQUYkx6QmXv2l2GMWH6Uc3s4Vy6PPE2irhvRD92m3jMjVD2-Zf9kGv_QMkMqGwKtxKTEHeXCASvYQkyozdZPKIHxK6c2KTREhgy-qramdXyq5jkJDGiE0qAQrpu0F9g-SlxDz99omhKTJ_5Y5ypbJHDLC2g5tmdg3pt7jU347wQcJc-8IWyqxHN3dSL7MEl6CntslQtlBZwvu8FPj4RHR42oH4gla34gmyPFUGQrY2LG_AxRVQjAZ80ssAU_tfKU_KjbFDyNSjzRhO89xp-gsZR8RNB3-harOu1ItmhRgDe-RvKmuRtRA8lFtzrMMijOnY8B5fnJahAuDRJMnf4Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت سوزی عجیب شهاب زاهدی در موقعیت تک‌به‌تک با گلر چلسی؛ تو یه لحظه هم رگ غیرتش باد کرد یهویی با پنج شش بازیکن چلسی درگیر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27406" target="_blank">📅 18:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27405">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1-FxjVUdoB_PRT5GyejznBchl2qbiZNqyxHqgc6b3t17cBUYTR5B-rUAaWB0SSaRn3W-b9TY3oDtnmrkbrMrctiOZ88_0vx9hTSXUfD2c0AnnfKDlNGMlgVF_dUrrIrcYJzCw_h1BWG_D1HJUmwiOsEpikGShq9wKHQdgUsJJSX23m1Q9dIcOxzqEEe9Acjt3CeRIprQl8huc677CXQG92cx6SB9ohJ8U5laNAQzcgn_mv9jPHALOMtq37bLeTqwOeahe_6NrbgzKij-Uw7c62jCIUpcXVchvQfj46NKz67QCKpsQH4QmzCfm2nXlRf_nN08ti_P5RRIrpOF2VdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیرو خبرریپلای شده؛ ماخاچ‌قلعه‌روسیه‌امروز تو لیگشون‌بازی‌ داره و حسین نژاد طبق معمول بازی‌های قبل روی نیمکته چون کادر فنی جدید این تیم تمایلی بهش نداره و به باشگاه گفته این بازیکن رو بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27405" target="_blank">📅 17:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27404">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKRqu1jL3C8H3hcaUKYBNVajR3imaKV6TzO0U5yHV20H7UVqT7QhsOQ2uJn4kGZkji_al9jk5vccG3oVjWYFYfXdXJXBgwQUgi_Qra-FpwZ9QA3hdEnAI2LwWFSieYB3IrRQ1Ab0OwEbV4IswIiv6r75aV5eRzRry3_Am5BVAMa1YDVkFrHIyGhwulZU1K7BsxBDAuSXSlxw8OI2Pk1FxFcIykzwfA0gf8yiRNMp9g8WLA9rRshwzwUJvNGaElzPB5Gre3i8dTe9Vw71axaCFyhziBZRIW27Oo2IeQO61FMFRryX6dsJu6dDjJZxa3-KadmI53G8HyFy0PzkeBFVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
ایرانی بس کن؛ یه بار دیگه ثابت شد که تو مسخره بازی رتبه ۱ دنیا هستیم بااختلاف کهکشانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27404" target="_blank">📅 17:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27403">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8dde9dbf8.mp4?token=Z5YprtN463_J44F1frWt3ZOc99eTo6X2wED2UDhHw9njAre8lHCGul7u46KYBv_Ooj-kR3OL-PRDM25mGCzYTO8HrQ6XfqqJ_MFsXUbrnwMEN-2sTjjChcXac0qZsCNSE_uRhLMxfKqz1PHnjOL1V-l7P8XjrKfS-AyVY2-txD46R_X1lelSozEnmiMZBEh19HGMDeB9uKcahtkgBwbKAheOEG6cOd5GkcBnwg0OTvVB7s0qMyR6fveyAbZct69YDQ_AS2aHZt3Ktg_Yp79tniBHeF1sUSQUYo2B4_4jFt9q0Ih0q5oxs-3xi6qHCDj8cPO3XZ6EAC1ZBO-LEiLKXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8dde9dbf8.mp4?token=Z5YprtN463_J44F1frWt3ZOc99eTo6X2wED2UDhHw9njAre8lHCGul7u46KYBv_Ooj-kR3OL-PRDM25mGCzYTO8HrQ6XfqqJ_MFsXUbrnwMEN-2sTjjChcXac0qZsCNSE_uRhLMxfKqz1PHnjOL1V-l7P8XjrKfS-AyVY2-txD46R_X1lelSozEnmiMZBEh19HGMDeB9uKcahtkgBwbKAheOEG6cOd5GkcBnwg0OTvVB7s0qMyR6fveyAbZct69YDQ_AS2aHZt3Ktg_Yp79tniBHeF1sUSQUYo2B4_4jFt9q0Ih0q5oxs-3xi6qHCDj8cPO3XZ6EAC1ZBO-LEiLKXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیانا؛ درصورت موافقت مهدی هاشمی نسب، مربی سابق استقلال به کادر فنی جواد نکونام درتراکتور اضافه خواهد شد تا مثلث خطرناک‌ جواد نکونام، خداداد و هاشمی‌نسب تشکیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/27403" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27402">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atZHoxRxo-Jnhq7jocfh7Z3fGcsVc9p8IM_yK2zxHX0fbBC4rvU4tDPylv6uyCE1GXeYDmBHlCt2VKBBoyxEgys7VqgdLy-8U7UvmxQICsDBTis7eoowDVns1dPRJTjbEtI3OBQOt_tfRGS1zTBzDXmeYKHE3vIrkvTspP2aCURUb9FZ2hYBcKylqd1ox2KbiloNyjsEHvGfFC9fjo4dSR92MVMd8aH6h2rKOWu78vbGr0uPRffLhXWjYzl7LYZcKDVFMCUIZyqBKtCfr2vTKu4-ueEAGKefgfH3cH8IHyxVAn_MVMOvTaWEEP12QrOmh3DReLikdQvKNxSW61Y59A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/27402" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27400">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b7307f5c.mp4?token=Il_sJb8U7uyVKbNm7n62GBg78ykvN_Imcr0n1Gy2ME5vqbwH6vdF8vrGZOW4leb-wNMyo84-i6PDg-euuGsIT785nhFFuk9jZjGLrQwP_r8uSyv2ht9eBlITVco6BgJtGQ7W_r-41jc-jtrExcHwpDqy-aH7PTcdQNvUCBWgMypoU0MtKJen5ZzyzlycLWXPOnRhEDSfBezBmTiWUf8JsXfDA0ekRBWFBDag0oN83flbB48-cadz0H8llDy64c1dAWdS4IC8DWcM3x43tfKWgJFZRR_Zex3qVTrF9RJnGccjPZ6-2Nyewdo7TwtoHrUjOAFwLGikTvojnxGcYgS0pk3D5xBC7-jrEyBNuQacUftE8bKQNcSl_CifzNC3hKIzs7vIEABrS89WXaxsyUgbag5CCatRgiu-_S7CPWGNRn4hJaXChVZ3riMQWhqI8BtJuMMKtjHtiMI5_4QZlep4xp7fa_b3iOrFTw4Deld37uzEuAbt0Okp1ZybfKtrCDk1-f7fnTQb2B5HHAhwNzaqli9ysRjSlxQhkYq52RTgmLV-5NEr2MHxJM4SjF3OufX6a61Nmv8tK74hCJ_uCaXld5itFw2pEAYxhMfRor5ao3mjj2axJS-lxXxqBoRxGjWYcUl4gbWgrwYSk6fTc9fir8eomr-7IbzkmqtRIrV7ENI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b7307f5c.mp4?token=Il_sJb8U7uyVKbNm7n62GBg78ykvN_Imcr0n1Gy2ME5vqbwH6vdF8vrGZOW4leb-wNMyo84-i6PDg-euuGsIT785nhFFuk9jZjGLrQwP_r8uSyv2ht9eBlITVco6BgJtGQ7W_r-41jc-jtrExcHwpDqy-aH7PTcdQNvUCBWgMypoU0MtKJen5ZzyzlycLWXPOnRhEDSfBezBmTiWUf8JsXfDA0ekRBWFBDag0oN83flbB48-cadz0H8llDy64c1dAWdS4IC8DWcM3x43tfKWgJFZRR_Zex3qVTrF9RJnGccjPZ6-2Nyewdo7TwtoHrUjOAFwLGikTvojnxGcYgS0pk3D5xBC7-jrEyBNuQacUftE8bKQNcSl_CifzNC3hKIzs7vIEABrS89WXaxsyUgbag5CCatRgiu-_S7CPWGNRn4hJaXChVZ3riMQWhqI8BtJuMMKtjHtiMI5_4QZlep4xp7fa_b3iOrFTw4Deld37uzEuAbt0Okp1ZybfKtrCDk1-f7fnTQb2B5HHAhwNzaqli9ysRjSlxQhkYq52RTgmLV-5NEr2MHxJM4SjF3OufX6a61Nmv8tK74hCJ_uCaXld5itFw2pEAYxhMfRor5ao3mjj2axJS-lxXxqBoRxGjWYcUl4gbWgrwYSk6fTc9fir8eomr-7IbzkmqtRIrV7ENI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی عارف آیمن ستاره 25 ساله مالزیایی جور دارالتعظیم در بازی دوستانه امروز مقابل چلسی بعد از دوری شش ماه او از میادین به دلیل پارگی رباط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27400" target="_blank">📅 16:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27399">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsstT4zozxuCY6pjwFD5CPDqOSeucfFnTxevnlVSmx2fiMEEAaYT7Rhhg5ElgEUxpLImRH0-jPAf4XD95oq80mwBIjODAvAKt7LUSPjA0SqLQIvfHaU7OVeO1vpkwCxayUoexl6OqmAx2RMPXMjeAs2al2e7QnpmR0zyUtFYBOmTbVVS6OueQrSN9cbgeTREGRQlLkaOqbZTfodLgIdGBGW8YfUSi64rR6jM-0RqBbUsvFdG4kRF3ILdkBGguBI6xv4O56zugt6nAH56NfwpiJJjkjYdM8KhBgKmyDSFb5Kig-RV-czx_f6r5S1ucHrxRvW32_CvutmkL5v9LYIwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27399" target="_blank">📅 16:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27398">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIIU15RMpbEWqUAs6wybwB1z__8wh_tgHVxf_M3KnHi5Ccvn4XKoOeXwGjGVawC--94yRGtRooOUPlvIPuQD8CAor4Imxlv-lO2-vfbjOxMmbj1MYRul8PZe_JDOmQ7vjGfJiQg6zLh4DRiy6I6rsYxN0bypwOm-t7Q33SNmYVCsTCLMicjghoEcd3FQ3LRYyOInIKUTbsjd9_K9WYJsM46aTuBOGN2lxxn5mHVe1FOS901Z8Aq1hUtkg83746oQbkkZ4tro4TMnje0uBp4ppkjp0MPAfOg_4Wf4Hhg-B93NDs36FEGVHSX_ZrE1ARKEFrSoHIE7chcy1zZ7VgKxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
جوادنکونام‌سرمربی‌جدیدتراکتور: تیم خیلی خوبی دادیم. چهار بازیکن تاپ فوتبال ایران مدنظرمه که نامشون‌رو به‌مدیریت محترم باشگاه تراکتور دادم تا اقدامات لازم رو برای جذبشون انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27398" target="_blank">📅 16:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27397">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0eb7a5bc.mp4?token=qxCQV5W2DIIbBhUTPQbRVOvUiaUdPzYuaNmKfFaR8O2ej9R7SNF7kSka1OfVccWi1QoXTLOgwLBcAXKvu4m_mHio8xfgk7hxXgROeEPRUu3U2f9taCEgjV0A9jRDJzYfKovyjHF-N28s0vmpQg0133mqJA1vM6O95nU_kCUAzWaqHS9QhtY7uTaeoqfow_4arTu4fdQuaGG_KNUGLwhmRuR2ksBEMI9gfN0rAxW49OQ6M_o30GeOtF2M2vK7cPtcKM_4hf7TqntPTKfW7TvuvFrX1RMuLx2rTeyI0-vCuyTZlno1qa7UcKzagGc9adsWCb_fKfgJ_Qe7NOBC330QbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0eb7a5bc.mp4?token=qxCQV5W2DIIbBhUTPQbRVOvUiaUdPzYuaNmKfFaR8O2ej9R7SNF7kSka1OfVccWi1QoXTLOgwLBcAXKvu4m_mHio8xfgk7hxXgROeEPRUu3U2f9taCEgjV0A9jRDJzYfKovyjHF-N28s0vmpQg0133mqJA1vM6O95nU_kCUAzWaqHS9QhtY7uTaeoqfow_4arTu4fdQuaGG_KNUGLwhmRuR2ksBEMI9gfN0rAxW49OQ6M_o30GeOtF2M2vK7cPtcKM_4hf7TqntPTKfW7TvuvFrX1RMuLx2rTeyI0-vCuyTZlno1qa7UcKzagGc9adsWCb_fKfgJ_Qe7NOBC330QbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
ایرانی بس کن؛
یه بار دیگه ثابت شد که تو مسخره بازی رتبه ۱ دنیا هستیم بااختلاف کهکشانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27397" target="_blank">📅 15:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27396">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ca826d21.mp4?token=Eal-RBuBmdAhGhO1xgfT08pLNWrpeTiXPeA3hHga2blSXjdb9Eua4qTSG-9OhNmH7v6rJmg9rXghNFSkGLxH6zo3F7na43I8x7HiTL5zzvDD1r0QuzjCvTVyqo1-ObRa3R7KBg5PHxC2hvkItJrSqFrhNJLBhKeyeY5xB76MDV25YYroOLqv58Ajkvmj3IB3ttiDw5s05RdcPBIazq4lcZPIDJIV7UcYYRAnC45r5NgUmNSWdi17dJqgDW1Ecrj3WZc5xYafdwZ4zarVll-mIlN_KbGtjssyzIVQD-v_JgPUGW2oGMmWqYgouHuPtlnXS6uEV-6KH4dSiU725fA51w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ca826d21.mp4?token=Eal-RBuBmdAhGhO1xgfT08pLNWrpeTiXPeA3hHga2blSXjdb9Eua4qTSG-9OhNmH7v6rJmg9rXghNFSkGLxH6zo3F7na43I8x7HiTL5zzvDD1r0QuzjCvTVyqo1-ObRa3R7KBg5PHxC2hvkItJrSqFrhNJLBhKeyeY5xB76MDV25YYroOLqv58Ajkvmj3IB3ttiDw5s05RdcPBIazq4lcZPIDJIV7UcYYRAnC45r5NgUmNSWdi17dJqgDW1Ecrj3WZc5xYafdwZ4zarVll-mIlN_KbGtjssyzIVQD-v_JgPUGW2oGMmWqYgouHuPtlnXS6uEV-6KH4dSiU725fA51w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27396" target="_blank">📅 15:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27395">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0574804636.mp4?token=kLhlBe4qLhv6xNOL-NvtKEgY3zSonJmYK72iAKxfkqly_CLNbMaSsl2ZgU4IbsZgXCOZlYAxLHNCfiSWEpjqEwXlmZVvBRGvmRZ56GHiCY1ClPHC-kIVW8NG51H7giDKlXdXqvz1sTwiBIm2B_C2hqcm1v4vqhq8u_qOUWll2ncGPWwjlejQ0X19tw4iP5QMyIYonQXxdH7V5x8TrZ9lcKeSfhjMEFTaKVufwUDhnZaXRxg0od5pTr2vcAYB9KzklifBWcogiAifXXOl8t9tNjp7j6JEpf54fL7yYopUATOwX5Pcd9EjHA4AdMRFEaQL-290gO-nBULl25DJ_NdVyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0574804636.mp4?token=kLhlBe4qLhv6xNOL-NvtKEgY3zSonJmYK72iAKxfkqly_CLNbMaSsl2ZgU4IbsZgXCOZlYAxLHNCfiSWEpjqEwXlmZVvBRGvmRZ56GHiCY1ClPHC-kIVW8NG51H7giDKlXdXqvz1sTwiBIm2B_C2hqcm1v4vqhq8u_qOUWll2ncGPWwjlejQ0X19tw4iP5QMyIYonQXxdH7V5x8TrZ9lcKeSfhjMEFTaKVufwUDhnZaXRxg0od5pTr2vcAYB9KzklifBWcogiAifXXOl8t9tNjp7j6JEpf54fL7yYopUATOwX5Pcd9EjHA4AdMRFEaQL-290gO-nBULl25DJ_NdVyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دی‌جونای‌کارینگتون فوق‌‌ستاره سیاه پوست لیگ‌ زنان NAB پس‌از اخراج‌بدلیل خطای شدیدی که روی سوفی کانینگهام انجام داد، در توییتی این اخراج رو‌ «امتیاز ویژه برای سفیدپوستان» دانست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27395" target="_blank">📅 15:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27394">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifiiJr6VZt1kMBR8ieUFJ6oQhurgKsMTJrw-I1KI_eCcRhMVmD7hyTvZpWHykAeJr7xKQTjSNVXVNbJQoGQ9fVsRCz5_Rwkl9GZjueVpjvPjYuj3GPcdsW_Iw2sgLcVEvW9OZztbqw0F6zyBRPi7R5PGmDiJ1UpsSMJGBetzQfooFODMxUkn64mngOeF_4hQu4P5ExJxT7d1lFrzPVGt-TUV58R6d7CPIGRlnCJR6ky9vOTAmjrujxVQwS_CdeveDjDYgGoDLmyq1eO3prJzIZZG7QAbBWHtFxJv3Dv7v0OUHnu41BphK1yuRTTNqX8s0D6svss_cPntPKW7XFqELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ حسین ابرقویی مدافع پرسپولیس: از باشگاه‌سپاهان‌پیشنهاد دارم و مذاکراتی‌هم بین دوتیم انجام شده. ظرف‌چند روزآینده‌تکلیفم مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27394" target="_blank">📅 15:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27393">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnRTCtiPWfDkKgG8Kvxwag5IruUSRNIqSOkBSrGWcjiKxKO9PR6nUOp3_l4sUq5_OaE5k6GEk2NUlZXkenvkCUsBRrNNcxLj5tlsQ-R7GhixA_w_UULKIJK4Q-k_dQlcyfG0F8SzO0KbbM2OtG-v1czA3PEUrudTZ3nt0TUG3RNdECr1pN7AIr4AqVhqcZa87nPhW_4_iS8KS4r2WgfC2kBu386XIWIwm618bHeBORlTPZMhF0Ctoc8ZpZ8nmLui1lpp1OZHTrYBmyYG4bL8EAcVDGV1iilkSLHHDd7sIS26r_ibQLMhryn69JZl1ZazFiF2BvbSAoQF-4hUX22q1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27393" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27392">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arIF4RXup1lIb-dSBkvPNm1UTuL_zXHCOWwhjYFDD9xO_khXfByOOoTPc9y4gkRiEWdpyyAZ2HeyuhN8gub9MGhnZbAvYy0okEorNFOxLJ99pMsF71bxju2O_GtJfaBEoxCeMbGgHps1N1hBBWQZl8y7pPQHXm0LxycgHvAYNPYYT38OHfPjD6uZLF3g9x5TaTQ-SHsAAFiwwW2UkgnR_VJ4mO5IKWyD0HMWWDznhBDBiL_b3V1DA_TSCYQtcQ-upKUv8pWfNxlTWQT7mz3RPdJMnncVeFxlUlHKh-UNsNtqqOwuqANrhk1NzWDJZ7PXun2wbRx3FRy7puepzPiJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
جوادنکونام‌سرمربی‌جدیدتراکتور: تیم خیلی خوبی دادیم. چهار بازیکن تاپ فوتبال ایران مدنظرمه که نامشون‌رو به‌مدیریت محترم باشگاه تراکتور دادم تا اقدامات لازم رو برای جذبشون انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27392" target="_blank">📅 14:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27391">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4ZX825WWsT6oQkjn04eT7A2U0iwwWSPz708AUsaciKsIYe8TJ5qu98lgc-D8-BshNenG3-ueCafjahdXV3dn6JkYM5BbGNPy5rv_1rVsNVGpmifSAehPOitPJOpFe-TSpryL9qmFe-3JlOj-gMIRmAsN3K5BJ07LrbSwxQ2emeapf9wnCHeIVccvFnpsP-4xcf190o-6IUFu1kzziNCvVQV-Y1HUTtX6pjrjUUgw7gQoFjC9ci25TeW4bwPLiQB12WbtZqTxWmtT9KoQ5AQYpCKyM0ZabJ_H1aARSAUiigsZHMU7o3wiVYuoSFm2rWqhTRT4j55D5vLRTCgeGod3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ احتمال داره جواد نکونام از بین صادق محرمی و مهدی‌شیری‌یکی‌رو درلیست خروج تراکتور قرار بدهد و درخواست جذب رامین رضاییان بدهد. محرمی رو مهدی تارتار برای پرسپولیس میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27391" target="_blank">📅 14:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27390">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3mC6JNE7nNbk8fUCYXUZdN-TcVCm1_rR6U9sSNBxDoIs7TvYLJ1SC7-UDvZbBo43jeDR2hZ2u_hPgWuNjDisJ-bSMAlKN1OaZ3lEzlAJKXqJiqZ7cdqNstJ0A0A7xXSK6ky-RHUOUD4nzz7EJ70kBZRo_prY6n8Ik1hkvVeXFNvuw-DTJwOpFeWQ3Stg21Da_JJfJYOvuQt81JbupiJ5w4WzHadxSHDWslOWLO7KgGALc9pkE_HOl48K51mlMVwnrrHTy89FbLfcRmydfRkjxOijpgr_0-vFl4zM0WGUmZ-xtebJV9TcPMj2IgTxdrG-eyoL_MgxtqWJjTo8rtXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27390" target="_blank">📅 13:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27389">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpQdV3vvTm5h-fu987fA-5_kVOWo2rTLzeTkYXT9os8qGRcXvjcF9tz3ICcqz4GKsms8HP_UYnYb6fYaBO8URQxQUJQSIhM2mZKkvQiFS_ZUE986W4Na2BsfUz6bjrOEXgeaBkUPFCQQbSrWhunFmvKeBhTtmEAUX59fLHNw7TtfCVolXgwhY_iM-KF1aUDwnQ2a2wbqqI_W7L-zNjEGLMemqnXmlozmdBC8FdVc6PXyrtBpu2VKn0VY3Dxzo3jD79qQI8mNM3PXoT7vY91hksshgj4Ayz8qwfgeMjukjJDVVSWoawFhYuM9MkzhkeiOrmgVblkx_JA5sreKsLXFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27389" target="_blank">📅 13:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27388">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0gKfpW59HnbdY3EKzBQZS102mfRJHX6QQLuJ17kjPOamGyp_EgPebRvy9XPUVF9wwD7Ve1Yb7GTY96o3reSSMcF68BmvErIADNtjDbHIwnYTrrzcEuRKjmKZY1B5zvOywJssLHHWAI9RGr2LiGsOd9sgipDWYQMkSEhDkE2tz7fL6ktKg2Od4JP3Sq8x3yV9jW8anIX7vVXkRkeJhyxu02CXqa8xlRfwjalHvRBkw648caUiuK6-lXFFPeVsVcaet43wVDSn4KcfAXX0EK5VEZayQWygTWtyYTQ45GC-XjdUwKjoRezuY-bNiGpYkYms1dLYVBmy8ttQ853DkcKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 28 روز پیش پرشیانا
🔴
شهریار مغانلو مهاجم سابق‌تیم اتحادکلبا با عقد قرار دادی به مدت 2+2 سال به تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27388" target="_blank">📅 12:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27387">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f7c35af.mp4?token=mAQ7DUWws6fLFJHKiPGj-SO5SWY9naiRCRRWzQkaWUzSCD6v-K0GKCW459umL6UC2P5IWMnR9g3-Cjr0y9b2VvH-B-KGhCNJq_zGRBNaRY6Xw0izovGjKoX9h15FJQon1ldN7QdMPXdBFAGhsbrR1slbZhUPU8uZGfl0vPtmINem2ERHWRvi1UC5uRLj4EX5I-CGUAJtKucSL5rFNdEMXv5wMEysYATRZU21acFoGC2HcT2Kw6MC1y5Q3AHVvK1SkdnJZ0It-KHyptP0Vg5igCQljmiZQbxzvc6A5DsYhvV3LECLddoFV-ECdRy2U9NTYyMqghnSPpWLuHhlM53O_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f7c35af.mp4?token=mAQ7DUWws6fLFJHKiPGj-SO5SWY9naiRCRRWzQkaWUzSCD6v-K0GKCW459umL6UC2P5IWMnR9g3-Cjr0y9b2VvH-B-KGhCNJq_zGRBNaRY6Xw0izovGjKoX9h15FJQon1ldN7QdMPXdBFAGhsbrR1slbZhUPU8uZGfl0vPtmINem2ERHWRvi1UC5uRLj4EX5I-CGUAJtKucSL5rFNdEMXv5wMEysYATRZU21acFoGC2HcT2Kw6MC1y5Q3AHVvK1SkdnJZ0It-KHyptP0Vg5igCQljmiZQbxzvc6A5DsYhvV3LECLddoFV-ECdRy2U9NTYyMqghnSPpWLuHhlM53O_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برگ‌های‌ریخته‌شده گزارشگر بازی امشب سپاهان و ذوب‌آهن‌ازپرتاب‌های‌بلند نادر محمدی؛ واقعا قابلیت خوبیه بشرطیکه‌درست ازش استفاده بشه نه اینکه از هرکجای‌زمین توپ رو بهش بدن بی هدف پرتاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27387" target="_blank">📅 12:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27386">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2vMajFUzgHeCjGDrvgzRF9L3UWCY2QB9DwiCnoP2US4j-w0XoMDeyS8vAcewVqqqV4aOTqyyfyf0cGhXLOgl3MdYOqkF7UCYz0TNjZ945Vt9sn0wnLx_T7Wy644YQmhVoOrkJQhZKDplKCqkseTX4bWYYSErO8DbLkn2P5vywjXxZprGMvlTjXUJ6usDUQFWfC-0huupDRlUOnfIwqWnoWys0DfFJ5DmZhi0a0GByDqGd3Cu8gwc8AgPAfG4euLNfVgQ-u1xjecI61WLiqB237mhwV5DWdRKK8VKhWRj9RXnwX_MGMsFU_MGard6X1fzZNxGBuSRcBbIxie_DECuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛ مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27386" target="_blank">📅 12:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27385">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv-gS4rfhyRlJ-Xaa2GMsWh7E_gCikVh37ozQpfo-s48SCVilj6QqTbkIWBjzN7SmGtLcFpLA1tIma_9yTrRvzc5-vv10j1QaDfGCPZxNOGc-7T8G_RDXQzgArKH28gBl84bOAcC7wwctvIPBoTVfor10go_VVTENNkFlzpT61F1n_yw8JN71UWk8i5LqzsLlula6C78oHG39I64KuDMitm6tBzUjEHAAe6hq86nl7NSgkmclZAEjGNwbZKb2k2g7S4MtLXY4mNwjmiXcvrJIvgOsrj1h2cPuvpjuPLnzdIPmNWHp4Ih44351cTNq0pZ05n7-9d2_HLxpCSsyfiLmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27385" target="_blank">📅 11:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27384">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inGsmiFtWdtFxPirLv6iMgKHXBiq0byEeqTylX_kFsz32fF2MP6Ds-3dZLMoPQ5CxKj_rg_3-Ag8v6kvyEGdbTkNREc4jPFbppfiK0yLRW9o1HaviZCZF8zVz3faPbz-LOr4ZRu7EZPk7d5-AcVMnFAPnpA_dMFxU6TAPB2LNBCum-CillNbthcx1RUS3dl_olzEgPXEL3dK2tczMxDd6kO7vAmv6TtUq0HgHxXmD8evJ394MlcW7lUi-QqAMBnSfGHuJTdcQ2BJhuOlr4Hd2O3yRQZmmN8rCL11BF-nELmqvrVENkzvbwczMKF5xCJc69G5lt-qFOrEelXxAk-Yjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عجیب‌اما واقعی؛ رامین رضاییان تنها باپرداخت 100 میلیون‌تومان قراردادش رو با باشگاه استقلال فسخ کرده است. در واقعا زمانیکه نیم فصل باشگاه استقلال قرارداد رضاییان رو تمدید میکنه بند فسخ 100 میلیون‌تومانی‌درقرارداد رضاییان میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27384" target="_blank">📅 11:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27383">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2rnggdZJbKjplyF2bDAqRY4hyQbi2_PlrnP772BYRJ3cZy5Bh7iQelsMNcms3pY5rceAoEWA6MMKTuratgd7ysNcyJnXZ4M62RaI3IPZJsUrsukvzbvk3wk6hdohz1re7txfzS9n_vt1aE4ZgjSzyFbCLhgVxV8VSCNWQLcX5PDcfDaG0gtjuNl3kIEVGvIv2PvQjBjVHfa9nTsLOy-hWp9gfhU_3aaF9l98DuFsNajimtxnI567P3TRABwVTw2R16D9PKmhhA18HRFWkGHWFeE_SYPgnO5mFi5S4lhrsexfvT5vpg8d0rb3Kx8TtbzRN5n-BvvmnepsvrtZEGqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌رسمی‌باشگاه‌تراکتور؛ جواد نکونام با قراردادی سه ساله بعنوان سرمربی جدید این باشگاه انتخاب شد و جانشین محمد ربیعی شد. محمودرضا بابایی چندروزپیش گفته بود اگه بزارم جواد نکونام در لیگ برتر فعالیت کنه بی ناموس عالم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27383" target="_blank">📅 11:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27381">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTCDelNQc-0KYEJ5paOdAkzkd06nNgsovShCtd238vMyAOPjOvt95H2m6ZrG3zw4t73Anv6594xu5_L2t7iMvwIKPuz8oPAoRahYcvdfSRTmp50DmTTE_NMuzGN-AdXub8mzU-Mw1Vj6qGBorcn3WWBySvXcZ6zB7xZWg3V12Dm9NHSwTKVov1rI9QdVJQyIlbDc4fXEgMeTzdt2D9cqXkzEmvag6kriq6bqY5KQrU_omkZdc4OOzdyadcljCthe4XQPHBscUuM-b9nEn3I_2wvCfGH1evHWQejDFpc3YtqXuY1-z1U35djIWOBk_AFqZTCPzEvNwyz6wZd1M89rRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌رسمی‌باشگاه‌تراکتور؛ جواد نکونام با قراردادی سه ساله بعنوان سرمربی جدید این باشگاه انتخاب شد و جانشین محمد ربیعی شد. محمودرضا بابایی چندروزپیش گفته بود اگه بزارم جواد نکونام در لیگ برتر فعالیت کنه بی ناموس عالم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27381" target="_blank">📅 11:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27380">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6M2pRDXQqv9XL4CbtYS2psPPJaBCQxK1iShr_tDiwhiur7lwdj-EVyvLr7JncKSXPu16WPiZsw_fJcQqVuNCLb4rr3MSt9eh7fjktcPJHxcysGL2T-sDvBipM9onA-Mt3IBsqxWt5e-SGK70PZCQxoXX3H9wMZ7GH6RxzwCWkcAruUP-Jzy29bZfPWYfsZK5wKJKg7N30MwMiyDYAOTXntHYUczln2I1lHNCetrEP1QF_xIbHR005aibE6trY4W48Okv9rxks4aRXylFM1xz_c3kduvkAk83_971EfKbA1YI5oT0lrsO8JaIx6y0KFx6oIwKpfzPhKQF77Dd3Td2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27380" target="_blank">📅 11:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27379">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwIvzdyH1VsWI9J_Qe_JsL0Vr9pUhONk_XIvK_2ecCNdEiCWUaxCzaYHzmrC6nHWtH5LjmTo2jeyZ45-5JoVdPmIa76Jm3kPykGYuSd3nYJKt4NoijMvXkNbrni8aFtoeL-VJbwurb7HgV9Tn0wDvVtPHHSe3hIDADl8JzZxNaIpMUxFb1yByFhHWbFyF94lwZ5KTru-3kgAjZk3AVCNXyNH_oO-PMUMBtVevEMVbPl9mWTbvn1d4BrUHJuwWyHBkZRm3csAvXAFeOhYqHvHyJZWSlfSHx-37fHjD6lE4tRbx8jX6QVolvjyQOLF_qN4k9jP8cMR8QZHEwM2U5ELXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ امیرحسین‌طاهری‌مدافع 22 ساله نیرو زمینی باقراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27379" target="_blank">📅 10:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27378">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox_puldqYzy-u8yShFhuS7zMHI9_b2ACArT79Oki5hknxMFfl_qsny2ScWGpRtRFOTXdbzup24BOuxKYEhk-RMTiPF1OSvc51SBniQWjRRFlXF1fTRBTzzZkINOl0nz6ujkc73EhXUiIPHS2JIAgvPriQksKXeGpaRhfE9GdeSbqyoXykRp27s6LTwhmvunO1sZd0kKSHL7DatncjwyRQRQbbvewlEbAIVROnH8CYQ3-BrY6i4QiBQJyrXsMHHwDbgvufPgCY6JOKn2S23q1S4D2u2Vths_LY9fkJAkNdJTknL3G5WY5-rAuXt4MCl1mi6qrYqVZ8C_LQwfIi8Rt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق اطلاعات ما؛ علی کریمی از تراکتور نیز آفر بالایی دریافت‌کرده</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27378" target="_blank">📅 10:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27377">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHBEqCyh7btz9q-Qs434aMwOvC74RHWucoZdaKH87Fb498g1SVFgOXxEh8fy-FpwOpHUCYnXK3ntYIVWQyPjK7LutXCJ1rbiv5IquXRwF-_yYj8dKy8HOMYVxv4Rg0aV5Wk4WUlNVUeQ5Po9oEX8L5BKOL6y_ari576NDzarizsUdASUybYOaOk9-6QjGok0lJkoAsmJjWVsHY28017BW5_FMNB3MBC1L2unklVzAy_rsdTDbdJNVrOb4JKSuaOpuOMdlJ1AwiTAn7jhK7VHxqentGZeOzWweFrBoKcNPHeNB9QPhB6zI1ZtUDAnqtjiDSDrY9RDat8A_cWjbgkMcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27377" target="_blank">📅 10:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27376">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhZQ7ancJGJOoU5XOdqU5pseb5dam_CMNb-qGDaUlLVgyFLs4ZeQD1AG6nPf6XB0VkwpDu0IoXfrlGqRglZqg-RkZxv5kD_1Jy1fv9unx6KKHN_g4pDXsiv0PVXKQEZI6rjK9H3hufffI36Iut20HXbnVtCiePefYW91BB4vqF5Kp0XvG-7TADz5Hz8wh5pK0pqVoVEyb5IpakIKctRxdX6uHtosMqPXnDnFXXSoeu143RT5pUczUB0FjvcuqvNmVpDPcQrWWbmirNiOGVB4Y4Dl217WgQgZv2OZjjhyajdWbk9KUJwyLtwKAyofDFvNMNvdFf8LgPdu1nWg926x1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27376" target="_blank">📅 09:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27375">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlIZK9L61YZstoUPLas5ufjBn1WFULNNylS5G2h-GO9wrjca33SybWe-kB4bt7PrEB08kUMPmoj0qDGDauVJtB70mpx3eybn5e1p1gaUbXkS1CW2dKHYI56taQRHBRjkma6D3B4kODtFTa7QMThIdrPVlD4TDEDYEqkwMjoH7kZ7mocFpwJCRe_I24YRmwxo7-XoWqyACIDPLNe6fqVcU2SCbqOQTn2_38_geqdfW5FMUQBuMxf8hfPzheA-WvhkUp-oRMR0BR6N9XaaONcKTl63R_xP6M4_BtVnc7xK4RDxnttBM01kyD2MNDV74Q-N9qTp3KZzUWB1BGVkyb78jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری
؛ در آستانه شروع فصل جدید لیگ برتر؛
حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27375" target="_blank">📅 09:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27374">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmFtv2xe7yC9EXlz5lR4hobmi14_9zEe_KLmiHNtk27UT42pdSAJMYsa_rpQYz32ZCWAl3E3tBS5Dy4g8fFDGSQHOXPvcyaI0um-8ZyOiXjS2NAiBFD6x7czHjtSiGwvvGwjDHwA8laU8sbnP6G6l-sBGUxipnpa55l6It5GAA6jM8bwnfTq7R2zo3bwFeuMO5T-To4-b6ccP0vXWklphxUmWLvtG4z2hqYC_QfSpCksE0nC0xvTw0vXCAIVqzyGhC-xUPpE--AqfYJY0rIVAJXJ7WQ7Kc4ktSC3d81ii0G5DbptylXlQHeExTWyv5ww-Llgq4onyMn5BAgTIV-PaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌شروع فصل جدید لیگ‌برتر؛ 10 رکورد تاریخی باشگاه‌ها در تاریخ لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27374" target="_blank">📅 09:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27373">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg068gg_HxBQq-YNquMuVECmRAQmIWEiGc2NOdamVZ1_x1ks6A-jy09ZnSFAFnONV-jfk1Io7P4gmN8u-FOeE6DDTCMaF6LQqjRxY3OlKk8LqU3gxr2bCnra8v7X8J3CHN1eLLvimGwebURvCQMPBZTrOYyDdkaUXTiqjezEtm9qPW4ZaBKYMdXG74Xei91mP-ni2T6bWRvY3nyrHMhENgGf9owIRcKT0LtH8gkbKhxxbFJ-RRrhJX-qBf8jSJRlp5RVebAKqd4VxsUC1oDQsmrS8vd4D_w1ZB-qpYpkrn4ttzftQbHP4OiGgCfqm40rEHD62Q_BYc6Xp_WkNhX3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه‌فقط پدرمسی‌نبود؛ ایجنت، مشاور، رهبر خانواده و... هم بود. موقعی‌که مسی تو رده‌های پایه "نیوولز اولد بویز" بازی می‌کرد، دکترها متوجه شدن این بچه مشکل هورمونی داره و باید درمان بشه. خورخه‌که‌از پس هزینه‌هاش برنمیومد، این هزینه رو از نیوولز و ریور پلاته…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27373" target="_blank">📅 01:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27371">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_9_rrdWbvgrSEYqLzhFIl_HAv08o1jdGZcnJ7TE042ha6_ovRi4d2XkkkdxrAFw5Xt5T4CjOjgjGkmSkdvlbONlSpI8CAs7lsWeoL9I-xkmmb7PDT3U9UtR3-qO7qEnSwniEeiJb49dqjCvodiPcP3w2KKFcLbl2OERLv1t8arQzJKL3C_MtOB1GOIsG0H4moyjnj3iTamF96USGTrpibz5DJlemN8e7N72bdURaAwfPwJZg_l0v68M9H5FkbsA7I_3Jvs00ANbyECtjPAr82-69Dik1DIQjHKHPeQZipSVyBFLdRavAlo9cHyXWxFzyhUtDCy0bknoCz0dzWeRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از دوئل شاگردان مارسکا و سیمئونه تاتقابل توپچی‌ها با دورتموند در امارات‌کاپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27371" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27370">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QREHKPCMYmzSfkBFuzVV26dFJF6W-Cdg6x7VHQgVqLzHV2JonTwBLdhziHO_Qha-9XLH4XQaNuHJyh_LV018crFF92RGhVSog93aNZ46xCbIqpEo0WlZxlwtvKaRQyUhHn1QR9fEX2sDj72wB9EzgBcTAt9ABgkQBdNsFXEfyhi5ahgXUHLo3i_uP-h5X-jujautR8bZKwOf1kacMvmnoxwuMsYMSIP8TeNqxO4PCKc5IUZTewsGVgFZOzIu5holMydPVuDkVf6Vzoc-Dev-jQNk-0aKAetH2nVa31NwMpvamkVkAQEW9fmRh-VymtthJDGVM7OmRLa4kzeEzU3MZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
شکست شاگردان آموریم مقابل چلسی و تساوی در دوئل پاریس و یونایتد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27370" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27368">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvNLft9j042xJ_-Xb6PwndHi9Xqdxzq62HRuzp9qzzb6fn_Oohi3Ej8SJEZcgOEV604L5G92L8tLFh5BlLIz7l3Qlwr2dy7nO4Ldd738V8C8LiisF9jgw8-qhWwdszxkeL5cJ8vpADDBG8hzIZOZUwckHQ1oWbWhNmgAuOPo-Rzs_mBykKqRgoI_pIu8SI12dhhTx7BNI0LMH1Fb2B9yIijWi9STDX_0nnxplUuTShtGFwMzxJr2rRL2oDdo6aJrIZ_xVSbtw4se4wBljhbPuwIqhcbIzgEN5w5WdkSDeiEvA76rU3rTFVKwo1h3OHokbls-Z7cdMk__YDwEB6iryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری جدید خدابیامرز دیگو مارادونا افسانه‌ای برای درگذشت پدر لیونل مسی که آمادگی‌اش رو برای پذیرش مهمون جدید تو اون دنیا اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27368" target="_blank">📅 00:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27367">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfFCkUQtJsVIsN_f-LXrOtyQS20Vw-sIcpsRG5zrsn7tncXtyrkonbTqeXI5nPHnAm80H0MaZ4WHOLlMSFj5Bq5Mau6ih5dLzAmJGLWn_yo9vHQ9pR3DJGkRQPxy8HfAkz284MMovJZT7ZcSgnzISAnsA_22yz8TI_RoEyOPzHemLxDlspytPSFEAgMD2Ou_-ysMjDrCRLe3wBcJnFmqOBKHBuJrtfUyIl3zs0tuiaO8rvedxZNzRibqgXtpgGnvVOYBtwOXWsm4aY90L46N1N1dkuSGV7McjNNYOqJJR4hpH_veomWVigekUX-ijiu5s5R2Br8dTJCaDAxDN8rFsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
از پنج قولی که پنج ستاره تیم ملی اسپانیا درجام‌جهانی 2026 دادند؛ دو تاش فعلا عملی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27367" target="_blank">📅 00:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27366">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKr1lrEZGOE4mTdtk1389hDvdLyBLS0Z2dP892xq89DFNE_zGstEoIT5vrcFxp_PmuVUMAyIwcff8WW4UyXR7nKX2FxllAcwOa7UvjW2YBB4VhG_PoO5K395PG3bIGykvWNy_T0oj8k_PQJXtHERUrHH51ZXL1YbZGBzf1iT4DEmSe82t1BHCE4GTcbapXP6jcXx741sDGjFk00SMCDdVwkRppSnBZMk9jo8rv7MHkdcYusjrNCPb0MFPB7efxiK6sI0Y3-v1VG6XrSroUrHLMOtcufS-WLLZpDQHw3KE73MyXLjmC2krWnGgL95WdcoMMVwUaMNOm2-jgLvt2Nj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛ درصورتی که محمدرضا آزادی مهاجم‌استقلال قراردادش رو با تیم استقلال فسخ کنه احتمال این که راهی سپاهان بشه وجود‌داره‌. ایجنتش با مدیریت‌سپاهان مذاکره کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27366" target="_blank">📅 00:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27365">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWqbcq8tD3ZQt7otXX-kdVnxVERl_rYVWg6qdAN-QTzV4xtJHQEy8gJ5gpEFfRYIMfcpbDDcPp6ODLc10-Kfw17EHii9KV9JCu5uohDPPNWj4Rq9mDzBbtoBb4pzITRKOHFDUjRTHYsZrXYcZ9rWHhsduucABVZ0ViuGS0EObY4KSaZWsXTy-A9y1kxNBFneAgY5e7zvxxYvzt-OCP9ZgSoIJ5Eodp2lPmEu4cLtuDdQO3CSupteQAOKCjoViyV2q2dX0e6yLo8rHkdc72mTb1wVaOkJeF2UT3-F87AzmsCt1bqebPUkpxeSbOhNtSlO4VFUyfbNbtxTQk4bYpbeHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27365" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27364">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVALaqT4eF3zVPvJZzjdKsSHZrWTjS0qrVSZ6vpSXKIFBC25haqo1iEwVjJpUYznVda1x7bHkdqow8d8dGBnXGzbfgsC6b8Pbod2XeQ9qq4fly62EfbRcrAI1z0h7gxAi52dsuv74V6GS1O1SjYVyKnO6aLX8ointJ9a0I0dUXYPM_38qNYfYUSW2Fm9XEiTkxtM81UkifUAL82spWfX1rrbNgPj-sMt3bCgtk_FjmPCMlyDWrV3goyWN6InjPq_72QqnIOr5qXwTmHfQJoAIClcTmW0htwCjyyPbWFqVtwFVLyAlaGeDUwtflNbM7QGvCJ9ba1KpzCfILIltnd7Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27364" target="_blank">📅 00:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27363">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0IcGhsd43bL3RCpx_78uB1s5Icv7r3cs7DNax4uN7S30oLjcJG9hWr8E4kaId9XhU1ToIdOsK1iq6iOribADUu9Njg8dWNDMF8eGqXsJnNCLwrxYXvBHRg0dpTsIXV8_i_P8Y8vQRGfIBd4ovk2VQPCB4xuV3BFXLcYfYdrNT4tBRQ32lNtZXte-SaRUqYnaZtpjTDV1l6iTDz6l3tsPchucePbwErocEdYOuI17-pUsExWBnM7-OYC9hCWd2DFah0yH3qKVLwksyrXHw0pTiBrPMYnejAU45H7kttaP8xBlfMay3XsHsE7iIJxpoGx18hu_3ZHHvivdgTb28Xh5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه‌فقط پدرمسی‌نبود؛ ایجنت، مشاور، رهبر خانواده و... هم بود. موقعی‌که مسی تو رده‌های پایه "نیوولز اولد بویز" بازی می‌کرد، دکترها متوجه شدن این بچه مشکل هورمونی داره و باید درمان بشه. خورخه‌که‌از پس هزینه‌هاش برنمیومد، این هزینه رو از نیوولز و ریور پلاته…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27363" target="_blank">📅 23:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27362">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50f562360.mp4?token=bHB7a0GeW3ho5ZD5NRj5B2aEoKalopEXTZhSmJVaQKzWf7oHTnxy3kD6ViQCXH5ohYyNtTgkhTdi5Yy7V9teow5uAT9FhPHBGwKuyh-SWJUX7OzIlWGtxuFG2bmacbZZ4PrbG8DvOjLBmrqS3x1rjUO556hU8JEmaxCsoXLsqKU0Kuw7P37kcjgQU4RbgReWTJTxe0vRRQf4JXir4vgd2e3DlwwtVCYU4PWN6uoCkZLw40IVCjXwM6v7Z9jG8xadyaYYXLkdD2zSGpAKEE9aOtDtUwzHK_5ahe38uyHz7TCEiByaZbenqkaxJRFsNvUfTZVKGw1MHaqiUPSlOohypw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50f562360.mp4?token=bHB7a0GeW3ho5ZD5NRj5B2aEoKalopEXTZhSmJVaQKzWf7oHTnxy3kD6ViQCXH5ohYyNtTgkhTdi5Yy7V9teow5uAT9FhPHBGwKuyh-SWJUX7OzIlWGtxuFG2bmacbZZ4PrbG8DvOjLBmrqS3x1rjUO556hU8JEmaxCsoXLsqKU0Kuw7P37kcjgQU4RbgReWTJTxe0vRRQf4JXir4vgd2e3DlwwtVCYU4PWN6uoCkZLw40IVCjXwM6v7Z9jG8xadyaYYXLkdD2zSGpAKEE9aOtDtUwzHK_5ahe38uyHz7TCEiByaZbenqkaxJRFsNvUfTZVKGw1MHaqiUPSlOohypw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
هایلایتی کوتاه و خاطره انگیز از عملکرد خییره کننده الکسیس‌سانچزستاره‌شیلیایی در دوران حضور در آرسنال؛ یکی از بهترین وینگر های تاریخ و یکی از دست‌کم گرفته شده‌ترین بازیکن‌تاریخ فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27362" target="_blank">📅 23:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27361">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTMQBVuWeB4ZuWTz5izIfw2PAZMb19eMpMkni0M7-XjwUR-hk8c5zXw8_uryUfjr7sTfz7Ytr37HSQDkse5B2pYNh2Ewb9yrlJhthFD_Fv52laWanv4AIcPO8GRTggSfBzzkXyKOKtF2PMvhni11GT9NKxBBAmRjtKpdOyybdrpgMqfUEG37CAsazct6I-ZKfKZ6ADlf9a1nmgjk62tC2qD0E4-iGIxBBLP1O5mNIIfWAY8tKHNSi8q5iQ50PLrKj7bj1rWJuvPQxRxS25bkd_nvYEzVGSQPpnCne2-ZIaEGR07u2fwKIi6ZkQW_ZZFg8-W3_5HFSqX3M8wzoRjRPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه «عراق اکسترا» مدعی شده انتقال مرتضی پورعلی‌ گنجی، مدافع‌ ایرانی‌به‌باشگاه الطلبه عراق در آستانه منتفی‌شدن‌قرارگرفته است. این رسانه نوشت: دلیل اصلی این اتفاق مخالفت شدید خانواده مرتضی پورعلی‌ گنجی با اقامت و زندگی در عراق است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27361" target="_blank">📅 23:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27359">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT219E6N4b0sfcjnDvFnnbF1w7nq6tYDQMiT_q0b1x0RqyWFY-zhlpw7--GDTIBsGO6m3uUis1xwf2Er0wxTm0ToVEt6-Nx1aaPNvBh-Y2234JnkSmGCcRXq1TLKcVBtMKPyOXsjNJteDdBH6X3DWtsLr7tTVXFyXdhiS4F6a-_HM8GeJ5HeI0z70dORwkEF_l4T_-UCHbvQbU7d5lt1XmMij7UlvM5cMt7aWJ9EZu1TFcIS8p1O5CD2QT4RrK8motWfu56zvxwvr3qEifNYGGz0UFdjj8HCDR0arTo4tEJiQQu239lzAK2qNOsbLU7Uvw0BrmrZ3XCjr7_qGwr25g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار امشب‌باردیگر به پیمان حدادی اعلام کرده اولویت اصلی او برای پست دفاع میانی دانیال ایریه. باشگاه‌نساجی هم اعلام‌کردیم که منتظر است‌که‌باشگاه پرسپولیس 120 میلیارد تومان بابت رضایت‌نامه‌دانیال‌ایری پرداخت‌کند تا این انتقال نهایی شود. فردا…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27359" target="_blank">📅 23:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27358">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epIA4irJ26JDlnorQMKPyv3LUlbDfSbVvvrTxU3PqbAeiZvAgh9qxWOnu-e8ff6MS4Kd-W8F-MIw-Puo9mmcn-fsfky0B7qHkvUZgsbd7X5eoSGejHenib0Laa01n_ITvbFJvZgSMps5HsXLviZx5vYLHENfi7CiW4UyX2nyquu6-iuAN0EKVPNaoKR0Xah_alVUqVuRzTFOV7qGK-p7OKOfSzAsm9qJLkaWTaiFqZ9F4WeTo1kIXxb4LieGs0lVFlCw90ZzssGR3_kj4t4t4IGAQU26vMvXV9TFQw4PT-Nl3TciX_M4Cm19Yncl5D0ohz1dRXTGKpgfF-X_UmGATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
🇪🇸
#تکمیلی؛ پیغام فران تورس به باشگاه بارسلونا: دنبال‌جانشین باشید. من با PSG به توافق رسیدم و فصل آینده در این باشگاه خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27358" target="_blank">📅 22:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27357">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8O21eG0_JRpnlYpC436Oacg5MWg8njZSTTUgonp4vsOSSNidtvBbvnzUrybu7SnhqAaAFr2eRcqZ33VtIdk3ldtOWsZSSB1sdg1PA9Zb_a6GQAaA9kDmy0tYcogO8XUG415OAC061dZmpHe9gQwymaYO15H6A9fQZoeLnbrN2M3xPejd6ULAzYBC2e-31JaXIfQbkGUA-FAeTOhJPAX4iX2P55shszf8y8Csl9FkZL9-OQesycgqk3JNmamVmhHr5ecqM9LBtbfcJwsh9UIXtYSCnKBkeeFgsM2u2A04li8qzifi_x0TBssLFwNn6PfKRf98ngtfTRiMJyFYPGKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار دوستانه امشب؛
توفف شیاطین سرخ مقابل شاگردان‌لوئیزانریکه و برتری رئال مادرید در شب گلزنی ستاره جوان و تازه وارد کهکشانی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27357" target="_blank">📅 22:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27355">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h67GDiUhv06uj3dSXGtZsXafTHO-SWAe4EVMFKj5RC-DDO1mPfgLvn7cIvLQPsh6yNhghbVm6gbKaLEl5_vuQsviAd_erfsnPvtOc14M8cvkRNlV7B2Jiyx3fIiltMR84vGtvsqMNXlrl_SDj-EcAru1jKPHWc4KRYJeNvGrmfWWsA7dYWJglJwdlU5b213xQCE_ar1gkowgEMnpQOpHaFUnimL8DpjtZpOQD1O7GDp3iWHUV6fNcTBagrdz0AA6Fz60PRGscpFSrtAxYxHjsdKljzwTpRwDKBz3KtoBkIkssTgoYpvg-RXYfAQ-WuXCzbi-EnuAtKd2efco0QyyIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B431_9_ElZXKYvvbmqqEXyLQQujgZ2ATRPYjiIStTZdysxBeItYPc7busUxUr6s2ztZX_SkstEoqDsOlfkXw5qeXaoyzFl7fh271JkxbP_3D9EJCtNsc000zmBa6qqaywxj1T3ZWkE9HNk37Y7d7aiCM4LmNsOylyqFrQHzd4SYnN_-zIxLTU1wFl5cKiA1vt3QhHBAInaGgpcelAJbcCdzpDvCjBwoJPQ0SY98LU2pMc__ODPT2kpWCcVE5Iyg75dioysceeYhFlUP_MXsDNIeqbfqw9tXCQ445RmbTlvy8eXYK5QzYrtqgz66qk5RJFaHY-9hJka3vyrrd36lTPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
دو ویدیو زیبا از فوق ستاره‌های تیم ملی والیبال بانوان ترکیه با کاپیتانی و رهبری زهرا گونش که اخیر قهرمان لیگ ملت‌ها هم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27355" target="_blank">📅 22:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27354">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TV0vHhxwkeDRiCfvcpVdl93XWbP-C-q0Bj2LxhQmJ2b03otKi9Bpmhyq2um16XxNJG6aZQO_7-GU7xMPISWRXlVfvFAVx2KVDCs5L3uxAs0rcBmwlFIsyyW_aQangRO7tUo6A_A_YjOWxxWPxBK1hb3hne6x1BWpSQEp2qwMtMHwduCxu2wVMTburyfVVME-m9cyg91Tdohfv-OoPn1jX20wuYlWMWlw5i4_afVKZjzz-7Im0KKnCd7tBp35feShqk_sOJ7Ldx51s-aQSW3LX05arP3TzXLzweXguJs-dfxTtbERffQGImThBx5vN14WY40tCYtrYIgs9Q__LxkSVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
بعدِ توافق با مدیریت برای تمدید قراردادش؛ جلال‌ الدین‌ ماشاریپوف‌ از امروز به تمرینات‌ آبی‌‌ها اضافه شد. ماشاریپوف به باشگاه گفته تا تکلیف رضاییان مشخص نشود شماره 10 نمیپوشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27354" target="_blank">📅 21:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27353">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f51b1028.mp4?token=VlTiS1CgLwhuXtVH6iyWSIeoIZgpaml4ZJMSutZzxJbdqqjlDqnRSMAmw8yLvmfne3MEV9p8ftR7ZagBdKvs-fAhJ5UsRAvDl3yoGT_haMJSvNNWF2wtTpkH0RXTOzB88mMpmj8z7xLN2geWWewlPWLDiRPczV-hv8yHrPFYVy2uAU9GX31c-YCaYVe6j2n1ZSRTimZT4yiUeXYMl9j_sHou4-BVBioEe0RzbeyEUB-iLt3xjHz4RvRKE1xzzQmKZ2kW-Ttpc66Wdf9xrTKV015yqy0BBJyWpjcvrd9TUmDzEN2hWEG8WH3rnx4QzMjoYY9d8T-9jahg5oDZ38C28Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f51b1028.mp4?token=VlTiS1CgLwhuXtVH6iyWSIeoIZgpaml4ZJMSutZzxJbdqqjlDqnRSMAmw8yLvmfne3MEV9p8ftR7ZagBdKvs-fAhJ5UsRAvDl3yoGT_haMJSvNNWF2wtTpkH0RXTOzB88mMpmj8z7xLN2geWWewlPWLDiRPczV-hv8yHrPFYVy2uAU9GX31c-YCaYVe6j2n1ZSRTimZT4yiUeXYMl9j_sHou4-BVBioEe0RzbeyEUB-iLt3xjHz4RvRKE1xzzQmKZ2kW-Ttpc66Wdf9xrTKV015yqy0BBJyWpjcvrd9TUmDzEN2hWEG8WH3rnx4QzMjoYY9d8T-9jahg5oDZ38C28Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گلزنی دنیس درگاهی دربازی‌امشب استاندارد لیژ مقابل  سرکل‌بروخه درسوپرلیگ بلژیک؛ قلعه نویی تو جام جهانی 2026 میخ کوبش کرده بود رو نیمکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27353" target="_blank">📅 21:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27352">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qekVmRJhZu_LxFyH4MjLdDw1Bg0uuJ_3SAv7QwDxfdwaucNJFpVtti_Z1aIJBXvcGk3rnHHc-A8bPNj4ibczJed-FqR1sZKaPgjWkHMVVG3ohT_-FIo2DDj0788Wrl__8L3YmnKrftWe6_yZG5pZH29-hgivB8VSIkdyvgNb3qRlw_5tfncG6Q279kAFYEGTxpCnZ3Qj_PewRYh4U6AmQwzxTPuzGkV9ZnEWVNolGFmWwet1ptjJopXk0NztYgrkGxUlGa7BZlCT2e8EjqWhvzS6b0xFiHLmRYJ-xb_JAWcnDzt6VOo_nKPBk6FvFROloV9lqru1rsH2KiO2foqoYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تراکتوری‌ها با پیروزی 2 بر 1 مقابل شمس آذر در دیداری دوستانه به استقبال لیگ برتر رفتند. شاگردان ربیعی در هفته اول به مصاف پیکان خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27352" target="_blank">📅 21:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27351">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbKvvPiY98m3p6yJLtJbB83joO2WcCW6FKPyITl5tAlumZq8zneGtLkGT3eVj3VwHT0BnVjWyewXcenpBw8T34bS3UD6T6is04_LGbtnULh_yWu4HN7tHtwrtzEEA8Wa37leLev7BTBqyhnhdbYGpcBPRXbThtjeycYCLlXhhpYuDmGj5FmflSvkc1lmvBnhnPBVGQucbzV_Ib1f3rpSOulK23YOHsTwcj4sWC5HbFOeEZjMeJiOGbf6iqhh0FGWASXGVCk_gyO7DpCLIGm5Ea5Xcsit97GAq_rMWpMtVHMOTRrTyMuohZgfAstdNuCcDsGw2tPeh3j-1pIQUALE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بعد از جذب کوروش اژدهاکش؛ امیرحسین طاهری مدافع‌ میانی22ساله فصل قبل نیرو زمینی که عملکرد درخشانی داشت در لیگ یک برای قراردادی 4 ساله بامدیریت تیم پرسپولیس به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27351" target="_blank">📅 21:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27350">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24945e30c7.mp4?token=DLsODBrhiTdBDKPZdW3DSNFRoVKqghQUFJfXB3nazKA9Gtar4kWmhKuGFvgbg8sHYiVGssISsaKzxrHrXLf5W7xDqFXbVdBYSlkczlgnL-I_UHCu1PDwed6bDv9ts2vDeRSfQOOvgWkYF7_gvOMIuRZnOXwPcBY5HyOmUjlomQrXgUIA-X7YSutthSPo1zK5Hgkwh0mW930kjo7kDBqAIxKvzZrXlQDtRI7AA4RGiAQ8qXEegYaTpGQm4uZ9l9lwwDTR0wpoS_LGmJpeu5AOrTyd1awSzdTuyuXRArqSNrame9_ah5Av-zWhgofEty2PbwUZE6tgh47LbFi0CHvjVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24945e30c7.mp4?token=DLsODBrhiTdBDKPZdW3DSNFRoVKqghQUFJfXB3nazKA9Gtar4kWmhKuGFvgbg8sHYiVGssISsaKzxrHrXLf5W7xDqFXbVdBYSlkczlgnL-I_UHCu1PDwed6bDv9ts2vDeRSfQOOvgWkYF7_gvOMIuRZnOXwPcBY5HyOmUjlomQrXgUIA-X7YSutthSPo1zK5Hgkwh0mW930kjo7kDBqAIxKvzZrXlQDtRI7AA4RGiAQ8qXEegYaTpGQm4uZ9l9lwwDTR0wpoS_LGmJpeu5AOrTyd1awSzdTuyuXRArqSNrame9_ah5Av-zWhgofEty2PbwUZE6tgh47LbFi0CHvjVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇪🇸
🇦🇷
ویدیویی‌زیبا که فن پیج‌های باشگاه رئال مادرید به مناسبت فوت پدر لیونل مسی ساخته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27350" target="_blank">📅 21:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27349">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe423c6dd.mp4?token=TCUvQBz89cKt116aqa7lpejIJvnG7u9UabahMrxIWTsT0jUYcF_l6C7zIqEnq-CFoD94XmlQkNluyVFTvCegwQP0hMYiOJU4qfoD0axrUZDJQxaxtjqyXK3DdM9zxeOanSDcYrH2oEcywXxWOqDny5hfGYwqyK2T0wtAlVhnAAa_nKQ7aGLaO7TvyMvF-lODnhA62TnzFLrqocmEGCc3pcJfK_-pZqgDcBXhhSY7yJj4m_bDhl-yJKH-K-B2ZLzoD2GGm4FaK6qzTmVlidaFqEs6_NKy0DIF7OcRjLxiFcleXNOrL6b6yvKEWLH8KOxhKzHNZswAUKYWE8By6vZtdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe423c6dd.mp4?token=TCUvQBz89cKt116aqa7lpejIJvnG7u9UabahMrxIWTsT0jUYcF_l6C7zIqEnq-CFoD94XmlQkNluyVFTvCegwQP0hMYiOJU4qfoD0axrUZDJQxaxtjqyXK3DdM9zxeOanSDcYrH2oEcywXxWOqDny5hfGYwqyK2T0wtAlVhnAAa_nKQ7aGLaO7TvyMvF-lODnhA62TnzFLrqocmEGCc3pcJfK_-pZqgDcBXhhSY7yJj4m_bDhl-yJKH-K-B2ZLzoD2GGm4FaK6qzTmVlidaFqEs6_NKy0DIF7OcRjLxiFcleXNOrL6b6yvKEWLH8KOxhKzHNZswAUKYWE8By6vZtdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
واکنس ابوطالب به صحبت‌های اخیر مجری‌ های صداوسیما درباره آناهیتا درگاهی عمه دنیس اکرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27349" target="_blank">📅 21:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27348">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCVkP_pCFyKYAZfUet27FWdfacKFJ8lSMSZ6uQ9rvls0Dt2bmpUvwsITfd9M_PPjc8hsHmKmR_n4inSTLu1wNQdc-xLMVIjTUP8brQO6RpKeGYfHemKyXU01vv25JmvS5XxZTCdq8Yyrm6FXjQHMRVh7yU4I6-7TcsdhJ_vYxuOXC4Slaumt3gtgrLiyRzZPTSFE1OWGTJNQma3xbxZFsGR6e0-x-Vf8FPUmaiLxEjUTkGyPzxchp3oILmXp6lBSGuxsoAx0aMoEo1w4I2NrWMZpRlGuHuwCvuVx4ad0BDU3uC0H84LXMQ8nT2X2cvrEfGGh2AvlaMK2kcYN4TWoZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27348" target="_blank">📅 20:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27347">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYsMAthtMc6sPHafgndPI6vSOkDkDZ_gVUhsXSayyXNJBO0xVS3ZfESWIhX1Poef3EOjyG50Yz6_uK-htmwrD88Q6EHOGhPszXzYIMikCMm0Sh3b5sFypUe_as6wEg02ttOElQddCT5QCzmSdVH14An6eadQx-BOyejGhldAV5vsSw7ffGQ9IVsHg8K74CUVV05N8sBGAMUwvWaZKE4i6HIl0FvFIG8R4WLoYpC5TLgvuMnLv21SITe_0KH9NUAUStQJUyJ0G7dbpzj0JmuIL4JbWBerLFsSDcAiCplU7uMKsMg8oNI4rj0RZYy0wqBXN0SRhloBxCt5peSYENsAJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس برای‌ جذب کوروش اژدهاکش مهاجم 18 ساله آلومینیوم اراک 150 هزار دلار بابت رضایت نامه او پرداخت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27347" target="_blank">📅 20:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27346">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ae3Kp4TMyItO3mFGlS0zNiTJCnSK6nMLmIQpxxM3I2hyBeUfCiAkPfP2mncVZeZMIYQOZPQJ77EftDRTHq_LTjLs4uZfEd3OW0guaeiqazkU3QngaUeRKubIn2CH1xP5Orj32fkKkG6uL9Ab8yxFrwP1XElKn95goUaHMXE4q3SfXscPVCYWScGLTAtdseV6BDSfvtl6vVl-Iqzu4h0PshMpg3f-jTI5XZTDtmCijD8E4e63l5UNUnkT2Sucs_oPAyp9DgDTRQTn9gRSTWDYPTogMEvTLfDVp97QSRKNCZLJBIjB7Ggfn3QjI7QqUhdIOxXlbZvhFvkoo3I_64XdAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در فاصله دوازدهم روز تا آغاز لیگ برتر؛ تراکتور امروز در دیداری‌دوستانه بمصاف مسی‌های شهر بابک رفت و به زحمت دو بر یک این تیم تازه لیگ برتری رو شکست داد. شهریار مغانلو و هادی حبیبی نژاد دو گل پر شور هارو به ثمر رسوندند. هیچ تیمی در این فصل بردنش راحت نیست…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27346" target="_blank">📅 20:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27345">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_j0ybBYL6Ie3c3WTK1qxqglscNHQhBGBiMmgF9AoqhOFymrRoBzSZoW17cTEXxAHRxfwWKhyH1PEecUuPMvuiQcRR6jyjHpF25lVpPX24PcTZcI8AaLLJ-WPFge4n6vPAkaone4mgaHWpE7_XFYkMujQplWaMAJVLp2VeWZz4uv2E70rikP28lGGqZ9iQR1__uHHwjNuLP-q2OhMtwgLjENatXHhpj0gvkd6AeGVs3yYo4qUJOegFbONTrgiuA3naj6RLO-jQZ2ofdX5VzEFato11U2Px5dMstInw_4p7deixhgiAbR5_3Kh4VUCUCE9xn_dS8CiRmLemzaL89lJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
#تکمیلی؛ خورخه مسی پدر لئو مسی که همچین اسطوره‌ای رو بزرگ کرد مدت‌زیادی‌بود که با بیماری دست و پنجه نرم میکرد و دربیمارستان بستری بود. دلیل اشک‌های لئو بعد از گلزنی به الجزایر تو اولین بازی آرژانتین در جام جهانیم همین بود. در نهایت، خورخه صبح امروز تو یه…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27345" target="_blank">📅 20:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27344">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT-biBbASa9d_QLPo4Lh4MdSH-WYzKL8OrZ4mnXdTbMiBpT_2QR8IlctzAtlpanybsABBtZIeHt1EqE6aHyl66X2MidSxwPIHVzxm50Bil0MND8grXmJY7Xd-e7ReWeQJLQw9KGFu_B4_YyVap02v7wlI6mH5M4dbrrRY-FFZcYxhM5INPvw7XrxfzeXhaxSTtIDgcKYyR1RD6Sq-CqTJvLljLwiEMqT2S4Xzy3DxB_p37QK_BJKcNGAf_cSKMKJSowcRiboCfXJqjzthOw4o2r0K2IeyrK6y-FJNO0GRevwwrfQ6-nl8TcDzxfz_DEXVuVY25SGm-N3pdGHelSe7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
رضاشکاری مهاجم‌سابق‌سپاهان و پرسپولیس برای‌ عقد قراردادی یک‌ساله با باشگاه پیکان به توافق رسیده و به احتمال فراوان راهی این‌تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27344" target="_blank">📅 19:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27343">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lonvLdUdEctZEGT5AhU_wptPbmFIB55HCHZo9ndWf_B8V1uLaYnmgWxd-mjLOkto__qYpf2ESqqBnzjQmQ4WgRnnX3NcrijLMxOOP6kwu3mtearZvrQHwc0HSR-0Qjt7v4wHmCZdh4ONb9sfrnVBHdZYIXRP19estW8eCBeo4n-usNFI2vMbRdbnjuQUJQi5KMatL0i7AVRvmWJ-ZvawcnNfXlqQvZ39OtBXHSRIizC08rNDBcssfiQARkqPd7KnLVBSkPlqabHTI_TR3B2qFeZy_mO8DUJ6Ou0bFB20jah_0eEQU7IIwtyuBysy_0uWSkdLmn5zk_nPJu-f76Ww1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله ماخاچ قلعه علاوه بر آفر از سوی سرخابی‌های پایتخت؛ از دو لیگ پرتغال و لهستان نیز آفررسمی دریافت‌کرده. یکی‌ازشروط مهم حسین نژاد برای پاسخ‌دادن به آفرباشگاه‌های‌خارجی اینه که رقم رضایت نامه او بیشتر…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27343" target="_blank">📅 19:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27342">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQXiQop4Jn-70mYeKUsC5DGmekZk1Zql-_bp_epP43C36HogHGZo_LmNe_NfarRYDkM8mPbCQUm6pQfVoKu9pkz2uA-Dj_wSq9GiTQXgK0H4xqZqj3JPN5E_8fcoCuzp6Wq_ag0zuaCJMik89URd1IForWXUnUqlD4Ztv-SLOyWuq-c7DaxWFlel_uLGbL9QDf8Dp7c3N5HUZ4tajXIIPDp8phjLU0YFK17qZQsV2-zu2UolTBp6qgiZ1ZK4m6Th_P9-aavVjtskOFhhTB8aj5MeD19hUhxQpFDz-ZGZX29Yzej2hmyxcrcOg1-SGkMt0bdcKEYHkoB6uCjYTmoT6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌سازمان‌لیگ؛ دوتیم استقلال و پرسپولیس فصل جدید رو هم در قلعه حسن خان شروع خواهند کرد و فعلا تا هفته ششم هیچ خبری از آزادی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27342" target="_blank">📅 19:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27341">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ao90ZgC0_bCtXP2Bi-cEnklVKXZ7Zs48Ol_GdisIT3SrnFIBwCws0O9OpTAlUmNQQExvv07nyuktVPebjlo9IcFwQptK1tkUnOkxwupYEOEMeuDad_rA2BLu9iQ2TJ9Qp4Oyxh_6D1igjzD7K22P9COOH3wl_nDlpcniuJlXuTbq-AqtS2HlxQ55zPrvvuCeXUdnQbrb39FllJ-ILm9bE7dtT79-cvSD_97tPmVNf2hEHwK7jZCRk3fPgnt3S55Rgp2dxMrSh6YEFXWRHwx5PBKrkmtxbss9RM8k9W8cj405-OArvJOe8PEo8QlYtElbgv7J3rw9zLGpLdqMOODdBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
باشگاه رئال مادرید دربیانیه‌ای درگذشت پدر لیونل مسی فوق ستاره آرژانتینی رو تسلیت گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27341" target="_blank">📅 19:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27340">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4cncY5C6r4Huvv8DR6WiXzrwjx81auhjRRDM3Kz5CCK3KMibEAV9NyjUnVeVcWmg3D7ne1wkg6JRunAXRlYByNMbbxhFR1CU_c54aFMoRZBp0mQZuKEQcN-mbJM9UjDeLOAgUV8kVgK2_Mkk6UVLWZ6jQlSKQ6BJo5pfbmYXYDSLXePqiGy3EoKVeMa73rHmbD_5Va1X8EbBEYIj88etV3DE7Z2IlSrE-Nufp_iVQCJ35mVEIFyJnNB1w_awUaikmosLSG0m2UNgPa4o0BdM-X1PNtB-cPxsHRB-cfu7CEZ7EVd4v8Tcoi09Cr_-NAEpdnvkIVtFBJgFiA4AWosVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
#تکمیلی؛ خورخه مسی پدر لئو مسی که همچین اسطوره‌ای رو بزرگ کرد مدت‌زیادی‌بود که با بیماری دست و پنجه نرم میکرد و دربیمارستان بستری بود. دلیل اشک‌های لئو بعد از گلزنی به الجزایر تو اولین بازی آرژانتین در جام جهانیم همین بود. در نهایت، خورخه صبح امروز تو یه…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27340" target="_blank">📅 18:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27338">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqKhbJmRbWbrF9lE5YEuPFDy_gfH6QdZG0waa0MQToWhWoilMZ9fulLipB6818dHDvPjgo3I_EQSHkiEjGA2akloQwMuz6cZ6_F8K4UWbt_vm4bwNQKi5M1LZnMWJAoJI6nkyj_Bk7lfg9S5vfv2NThhZnxaV9oQ9WYDIVSzQHCBgSOzy8VGWY0cDFbS_0_VxuR0AQAepabIy7_ioj3ZTHBaAfOpj3rh1ckMdsAAcL5efSz0keBG_Z757nocv7qzwYtRypqUHEkT4Wm_K_lmEzXPqiTwp1lzSes_uAQ5XAKiS0ouOfU9H-XAAiA-gZsdNpuqoJ5LOMJ8v9R368dMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وزینیا دروازه‌بان‌کیپ‌ورد درباره‌پیشنهادات متعدد باشگاهی بعداز عملکردش در جام جهانی: من میخوام جایی برم که منو واقعا برای ترکیب تیم و مسائل فنی بخوان. نه فقط برای مسائل رسانه‌ای و تبلیغاتی چون الان یه پیج دارم که 30 میلیون فالور واقعی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27338" target="_blank">📅 18:54 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
