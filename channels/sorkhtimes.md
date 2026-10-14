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
<img src="https://cdn4.telesco.pe/file/Kct_bWr6bykHBygcjDHUMRQEj27Rhf0q548toW-pVlLwFTc5BIeGRfdPRfw-4ZFWxi8nqN4NWrRj2wjydoBBWl6UDHts2mnyxxEtV2OY4GS62ncw9LsoubH-w-T1LlUprFFf6obJbxga73hqg6pEhhTNU00CIDqnv5NoEbh7Ph0oBsT2PWficvlV6qHug8oNr0QNBbL9p91DOaHjyeX5etkS1vw8Ht0AkNdWWYZ0iirf0QXEWpCZ6pbU9UGaJO_WS-RmMEEOcAP8gea_7ljWokjLWaC64c-_leSOg4SKS8t9OOGtC2INTf9Pfx0enX64Xu_LbEnN8QYi9ZOq6uXLSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 05:31:08</div>
<hr>

<div class="tg-post" id="msg-141418">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WihoNsy5GidSOYSi0iSwSbFnx-s_sp91KT4w4qOTQrvoKzPyIaKnkB4GLixNOyaMjsZElWM2plV9--m-8ZCya_VtoRzqdlG-1QL0WGw7dv2pGBZNIxZv84b1zLPoC0_5ue1VxRKy6iUR1hXgbAoGQ4qGZ54lv83COr9X7I-C2Le6Nvz6KaDs-1xFY2MboN5z06Rro_OvCwuJddz8SgHN6vYU426jcPD8p2HJXdzqfmZyy3AI6XdLGImj7U2LQKOtMvhtNrH6O47yi8v3XwX1zyzGDXBo3shMzDO7LvXpUVBD9TQZlXMSRlSaNyiMqB9-QcHFMu1rvCWRPt46njdxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرداشب، لیگ قهرمانان اروپا در اوج هیجان؛ از نبرد سیتی و پاریس تا جدال تاریخی رم و رئال، یک شب تمام‌عیار برای عاشقان فوتبال!
🔥
⚽️
نبرد سیتی و پی‌اس‌جی، تقابل سرعت هجومی و کنترل میانه میدانه؛ جایی که کوچک‌ترین اشتباه دفاعی می‌تونه تعیین‌کننده باشه. رئال مقابل رم از برتری تجربه و کیفیت فردی برخورداره، درحالی‌که لیورپول با وجود غیبت چند مهره مهم، شانس بیشتری برابر لاسک داره. دورتموند هم روی کاغذ برتره، اما ضدحملات بودوگلیمت می‌تونه معادلات بازی رو تغییر بده.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 991 · <a href="https://t.me/SorkhTimes/141418" target="_blank">📅 01:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141417">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SRlvL49XNuRq71emfmVNMz9MM8AWOwSfVUZov4IqoQCdZe2e1l474z1V_2czjeLhxYnkBtAI2g5329nCSN2FUfAriqREdBAmp8sdX6RncjwpjWyiMFX57k4f5WBbZPlqTwuxLS2EipjcONYgQZ9G4MKEPMO4UPQ7gzJJ_YCmJ2pOlPU0Hbgp0h6cKfkQ6fy21gHTV4H-dXjIxg73aqIDnzNz4pLYzoXl5cS5ERRrqIMkHKhkuxb2pixXT2cmL8IHVO3NA5C7A8BvoURmVator0lg8vtX0ZMJYTniJTLWJWNbRZhQLMZfg3wwO3iTxFW0KcEhegXJlCD4Dln9kcmFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
مقایسه نیکمت پرسپولیس و کیسه در دوران محرومیت
❌
کیسه بجز ترکیب اصلی فقط حدود یک همت قرارداد بازیکنان ذخیرشه ، این وسط هم دو سه تا جوان هم گذاشتن روی نیمکت که مثلا ما هم اره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/SorkhTimes/141417" target="_blank">📅 00:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141416">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHGWy09yAOkoLQHJEFehOc5sExIJKhNY5X7S3ptl9Jbp1Xs164pw40zbR1M9m6Nrz9jv3Mkq8H1QWQt260BFNr7GV2LFRSpSanYMXK2f-dzIwYNFNEhEZEQ4yaCpe02ay5RnGpuAK_--w6dr2qVryiU2ZOcImJSZ9ZJHQyzKRuEhKbEkivjWqyo2h0ulTmCZsy00Q0XiK70mfQ9xI82n3M2ahthrhvn0btiopy8cbv5fzgtwwV38s6Grk3fTWiIUWPlWGjmtP3hiXyhMm96zAS8M7rsWVFEZzu2qnSK1g3zgtkeiEcdruo9uWO_-AUnUT59cod0S9R7zVMaW2DATLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کریستیانو رونالدو : من کامل‌ترین بازیکن تاریخ فوتبالم! اگه کسی مسی، پله یا مارادونا رو ترجیح می‌ده، این دیگه سلیقه شخصیشه و منم بهش احترام می‌ذارم. اما اینکه یکی بگه کریستیانو رونالدو بازیکن کاملی نیست، یه دروغ محضه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/SorkhTimes/141416" target="_blank">📅 00:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141415">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsxKW0NaqxgGa5Esitz5NfJ14U-arXb2fxSpSmjj1fLWGSG_nyxOD3_ZfQTGMR5iXfONdgvU6njDYY3DkOvOfKdqn_Ffk7Lz9TyswgqBWxTVpJl6cvP0rM-J3xW4EvkE664Kp6wQXApbbmMwoOqnwnS4N2z7ROQr9xoB5R6ceeQ1rKW1R1lHTP6kTPYwOPpaSAVfCnRUlcBINg8e4tJj8FNq_eHM-884UwgGJkc1fyVow7acveeu5adyubs8b6tsH-4IBWxGP_K5QrlBwXGEVYZVv73_DiEhfMT5gbjoQwR3c_P_7-eYdqI3wFPr-BUXfGd69oxXw6RonEYvkEZ5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📘
⭕️
سعیدی: هیچ‌ نمونه مثبت یا حتی مشکوک در لیگ برتر فوتبال نداریم
📘
دکتر رضا سعیدی قائم‌مقام ستاد ملی مبارزه با دوپینگ ایران، وضعیت کنترل و مبارزه با دوپینگ در فوتبال ایران داشت تاکید کرد: در این فصل از رقابت‌های لیگ برتر و لیگ آزادگان هیچ نمونه دوپینگ مثبت یا مشکوکی نداشته‌ایم. باید اعلام کنم به طور کلی در ۲-۳ فصل اخیر هیچ‌نمونه دوپینگی در لیگ برتر و لیگ آزادگان مثبت اعلام نشده است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SorkhTimes/141415" target="_blank">📅 00:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141414">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/141414" target="_blank">📅 23:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141413">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9243295073.mp4?token=VPvMtKOt4Y6h_HXX-D7QQ4n44KLf9b3IF362HMtpCB9XziZWizGlmiF2Y94NSfNLCxq6pMQtLyicVoI-E7c-KiBZLQC4yeDtgOACKdSk6EGIcdQBKbjBudOdBlvgcV7Ml_yvKsvTiUgkqMftrAlQfV2fQjqHhfTt067eqOtRU5oL-2wGdnCdNLcTOZIhVtNJvwWmZxhjJPMJEWtejCfZfTx_PwuYABshkdfaORtUBy_lT7rszkYVsCX_dlghdGIUsyQLNpk-QQPkq2ULqJrY5vcs9iz4PGaH-_rLGiBmAWVSCQetJur-CTwI0lCqhXiKXSqxkMWNTQAb1un-IRor9YutPFZKu0EVHdESFhdeTDLH_mIC2dNhh5sRPG_Cv4oe9czaR-c6DYGRaKUBSAcmrrxRI3FRQ_W-ogCK7PMPq2yQ8Gr-cctxeXiugbye98Bjt6o18Epu8iB-REJ1dR5RqYsfXK9AyrMshEa6BwuIhnn-K4_ENk7cZw-5c69xY8pjBMJwfp_99KLQLmGOFHaJO_7DL4pcgYQzWEZ4PXLz0nlX6pbIw5imtZESp2yUrhNFcptXzOFkEQkHufq2gB_FjFY1F6lFpQ0dMxutez_N_4bOcjC2vfhVpkWIlR4oG0HJIj3GUQdbUWEmqVUyQf0LNksNqAlDlfTDF2p6O8055iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9243295073.mp4?token=VPvMtKOt4Y6h_HXX-D7QQ4n44KLf9b3IF362HMtpCB9XziZWizGlmiF2Y94NSfNLCxq6pMQtLyicVoI-E7c-KiBZLQC4yeDtgOACKdSk6EGIcdQBKbjBudOdBlvgcV7Ml_yvKsvTiUgkqMftrAlQfV2fQjqHhfTt067eqOtRU5oL-2wGdnCdNLcTOZIhVtNJvwWmZxhjJPMJEWtejCfZfTx_PwuYABshkdfaORtUBy_lT7rszkYVsCX_dlghdGIUsyQLNpk-QQPkq2ULqJrY5vcs9iz4PGaH-_rLGiBmAWVSCQetJur-CTwI0lCqhXiKXSqxkMWNTQAb1un-IRor9YutPFZKu0EVHdESFhdeTDLH_mIC2dNhh5sRPG_Cv4oe9czaR-c6DYGRaKUBSAcmrrxRI3FRQ_W-ogCK7PMPq2yQ8Gr-cctxeXiugbye98Bjt6o18Epu8iB-REJ1dR5RqYsfXK9AyrMshEa6BwuIhnn-K4_ENk7cZw-5c69xY8pjBMJwfp_99KLQLmGOFHaJO_7DL4pcgYQzWEZ4PXLz0nlX6pbIw5imtZESp2yUrhNFcptXzOFkEQkHufq2gB_FjFY1F6lFpQ0dMxutez_N_4bOcjC2vfhVpkWIlR4oG0HJIj3GUQdbUWEmqVUyQf0LNksNqAlDlfTDF2p6O8055iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
فراز کمالوند: پرسپولیس آماده‌ترین تیم لیگ است؛ شناخت کافی از پرسپولیس داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/141413" target="_blank">📅 22:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141412">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
دبل سردار آزمون جلوی الاتحاد توی ۱۶ دقیقه ابتدایی روی پاس غندی پور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/141412" target="_blank">📅 22:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141411">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
ترکیب پرسپولیس مقابل خیبر از دید ورزش سه
📊
سیستم 442
⏺
پیام نیازمند
⏺
مجید عیدی
⏺
مهدی زارع
⏺
حسین ابرقویی
⏺
مهدی تیکدری
⏺
پویا پورعلی
⏺
محمد خدابنده‌لو
⏺
محمدمهدی محبی
⏺
اوستون اورونوف
⏺
علی علیپور
⏺
ایگور سرگیف
🗣
نظرررتون؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/141411" target="_blank">📅 22:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141410">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
تعلیق دو جلسه باقی‌مانده محرومیت امید عالیشاه
🔻
کمیته انضباطی فدراسیون فوتبال با درخواست باشگاه گل‌گهر سیرجان برای تعلیق دو جلسه باقی‌مانده محرومیت امید عالیشاه موافقت کرد.
🔻
کمیته انضباطی پس از بررسی درخواست باشگاه، با توجه به سپری‌شدن دو جلسه از محرومیت…</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/141410" target="_blank">📅 22:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141409">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
از تهران تا خرم‌آباد با کاروان پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/141409" target="_blank">📅 22:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141408">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
❌
محسن بنگر : امید عالیشاه اهل فحاشی نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/141408" target="_blank">📅 22:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141407">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785f027d31.mp4?token=iDeybf4MzwxHpip2VcXAwi-ovbFqonr6oBbcol2ikKO9Iw1Aa_Q23XXu9EtadjkS6HpW6P1qYiQK3ct-_5jDcL9907oQDNwx7r3yiK3GXm6v8XHsFzwQ-_hY1ylvXQd4iZBvk6uvMfH99jyrHsAC_bjMGCo9qIDfRmgr2sWVsbqqKK1TgVNcemTy16CKMZKUBzG6PQrA5MdZDjlLeLeRypgBuz1cVZ1V67PT6hL7n2iappT8qWHijUIGIiwzVNbPw95_Dn2zBUvY2H2jEPlYS9gMRd7O7_syEhc_Tcvxv3UmrD3497kxNGqgj_B69s-1Pn_X_8xK3S8pM_i46bpxCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785f027d31.mp4?token=iDeybf4MzwxHpip2VcXAwi-ovbFqonr6oBbcol2ikKO9Iw1Aa_Q23XXu9EtadjkS6HpW6P1qYiQK3ct-_5jDcL9907oQDNwx7r3yiK3GXm6v8XHsFzwQ-_hY1ylvXQd4iZBvk6uvMfH99jyrHsAC_bjMGCo9qIDfRmgr2sWVsbqqKK1TgVNcemTy16CKMZKUBzG6PQrA5MdZDjlLeLeRypgBuz1cVZ1V67PT6hL7n2iappT8qWHijUIGIiwzVNbPw95_Dn2zBUvY2H2jEPlYS9gMRd7O7_syEhc_Tcvxv3UmrD3497kxNGqgj_B69s-1Pn_X_8xK3S8pM_i46bpxCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
وحید امیری بازیکن سابق پرسپولیس پس از ۷۰۳ روز موفق به گلزنی در لیگ‌برتر اینبار با پیراهن فولاد خوزستان شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/141407" target="_blank">📅 21:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141406">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rwxe7fujb_96-HHskN5lmNnXqdY2GlxzGSTnpEuNXP8Sscj-HnFtEIlmNXg-IWXTqA81noXY4uT-cDSrtsYbdxWRRhuOXyLWti6AdqArDpnK0bcaK73N_K_2ql1ZEiLIGezw44FHio32m6xcmVoCBE2IGHOlpXBGhdd0f7L-VGJlNjy15Lr078rjOxoVLK2elTxebA8yf2coM_w4v-BWogJGl2rCr60NaYLUFvDHmr0e2P1OxQfSqqnYd_YTuORnjD6g9nOc1woG5pI6ZMLYqdgqR0D26YbD6EuzpGKN5Zy0zQq23BbQEaLh24Lu4v0adwz59svk2mzRUyUmDsV9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تارتار به نشست خبری بازی با خیبر نرسید.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/141406" target="_blank">📅 21:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141405">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQTCbmH268qfZ23mq2STGpV_m15f3JlssrPFvf0G5J7f2-vUAgQJK9CtT-NVrFaxU0XCnel6NeoKna7DBd_vu-6mGG9djkrDTRptTZagwJH49x6Y4nMB4oOa9vd4faUN7NN9hKrxmHamnzBtuV_m7O6Cy258vsFwKNKBnl0BqgKSMnR7xWT99EJSx2cnmaMdD3ta-IOKyToAHLVx5P4BzYt_IJ_5CktkU2BgxFPMw7s2neKn-9o_LTQb34Rt6foSuhdK2fF0r2nc1v-S1KrrE9u10mij4mDO-6GXGeA1WQosD94MdxGJVjMDsFyb1nBsDyfSAzmtBOSkKPckWD16LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
جهنم استانبول در انتظار غول کاتالان!
🔥
[
گالاتاسرای
🟠
🆚
🔵
بارسلونا
]
⚽️
از نظر آماری، بارسلونا در ۵ بازی اخیرش در لیگ قهرمانان و لالیگا ۵ برد داشته و در مجموع ۲۴ گل زده؛ گالاتاسرای هم در شروع اروپایی‌اش ۳ - ۱ به اسپورتینگ باخته است. بارسا در ۱۰ تقابل قبلی دو تیم، ۶ برد مقابل یک برد گالاتاسرای دارد؛ با این حال، فشار هواداران در استانبول می‌تواند بازی را پیچیده کند.
سناریوی محتمل: برد شاگردان هانسی‌فلیک.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/141405" target="_blank">📅 21:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141404">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨
مهدی تارتار: از فدراسیون می‌خوام که جام‌حذفی رو برگزار کنه و مام حاضریم فقط با جوانان مون بازی کنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/141404" target="_blank">📅 19:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141403">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8f94fff6.mp4?token=mf8N_TBxxElGlK90q5seKusK7DkvXwSkbdhmJrss_9gWFLsx06T61RxlJ2s2SsKco5agy_YX8DdCeVsF0E1fI1xJMGbL2v3Uu3f60awLG0Y35uTQIwE15zKcLMlHu_W3Dpz9nDuypk_0c4P_1jsBlUfuM3Rk2SOlV4NaW2DPfefgvRDDUawYWKZC222rXLAUkmDYSBK771Til4qPfUHwkHaCEX3PwpN0SY7pglmoSLSc5dWQL9WC5XBtXaltCpLv7-RwYlXGiokrIoF1moRewr5nhvq2HzjoQXZtIzmBiO44J-GiEVSTttK4i4LmRrgavbM83eH5QM-1pz0CnMJD5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8f94fff6.mp4?token=mf8N_TBxxElGlK90q5seKusK7DkvXwSkbdhmJrss_9gWFLsx06T61RxlJ2s2SsKco5agy_YX8DdCeVsF0E1fI1xJMGbL2v3Uu3f60awLG0Y35uTQIwE15zKcLMlHu_W3Dpz9nDuypk_0c4P_1jsBlUfuM3Rk2SOlV4NaW2DPfefgvRDDUawYWKZC222rXLAUkmDYSBK771Til4qPfUHwkHaCEX3PwpN0SY7pglmoSLSc5dWQL9WC5XBtXaltCpLv7-RwYlXGiokrIoF1moRewr5nhvq2HzjoQXZtIzmBiO44J-GiEVSTttK4i4LmRrgavbM83eH5QM-1pz0CnMJD5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
وضعیت درب محل اقامت باشگاه پرسپولیس هنگام رسیدن تیم پرسپولیس در خرم آباد با حضور هواداران خیبری
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/141403" target="_blank">📅 19:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141402">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
تارتار : بچه هامون دارن به تناوب بازی میکنن، دست یه مربیم اونقدر باز نیست که بتونه 15 تا بازیکن رو بذاره تو ترکیب، انصافا استون هم تو تمرینات داره تلاش میکنه، من دارم میبینم همین قدری که تیوی بیفوما داره تلاش میکنه استون هم تلاش میکنه ولی به هر حال گوی سبقت…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/141402" target="_blank">📅 19:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141401">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNDW7hx8OOS_N9Q2p1QkkOOiFDwU_x4-JclWQE3q7mrG-B0sGKUFV7Q1N1DJ-1pk7_74kC2sP5ZOYV-FpMq_3lgdD6q-I1YPx9ilSeMudxPvylDmou7ULRh1NThCpqklR1YGoDalg-dudFh15Ctt80UPUDipAKllGuPbG1Dei8TlDKUDNYRBW_IIXTGGRNM1rexIdKQaG8DaqJsOs0hSipbJTKiyiD-cS_pewfKRrOSjnGtGuSJsQLYJEebMT8stCm_tDxniZvGy_YUoFAdqyq6ZguW6o94eaLbXgucFlWFT9mwDtQWERlsQEiz3SSj9Ohrege_6UhRNGK15nxJM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☑️
جدول لیگ پس از پایان ۳ بازی معوقه هفته هفتم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/141401" target="_blank">📅 19:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141400">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
بیفوما در آستانه دیدار مقابل خیبر دچار سرماخوردگی شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/141400" target="_blank">📅 17:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141399">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
شایعات : بیفوما با برخورد با یکی از بازیکن های جوان پرسپولیس مصدوم شد و بازی فردا رو از دست داد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141399" target="_blank">📅 16:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141398">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141398" target="_blank">📅 16:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141397">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141397" target="_blank">📅 16:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141396">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNrpsi5PYVveBeqcOYegY3e2JZS_RKOJSKw5x6nZYWU9WYV9juTARXsO_6S-KZiRoGgfo5bEYtrfisAns43BdXOVra_hnMgoIUTyEbmYTxjbSc7C4ee8vpFEgZf2esP9q-TNa67k1r3rQVZtt56G1TKTL91ScWQv4gY2HHGGioRJHV5UPIDDfoZfHK1UhJmGCdW_2rvHT-_Hp0EAt47j40k9-O5ufuWENMdZGYT1JP8sdS3jTKG2EOIwO3aeKXF9Xx6dUYH7siWq7kmRaiVR88fbpZlE86b0AKUTQNJAjmSECIbmxe_lpvuy3SdPD7wLwMMCMe3K-K68hlO2KmXltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهدی عبدی در دیدار فردا در ترکیب خیبر مقابل پرسپولیس حضور خواهد داشت/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141396" target="_blank">📅 16:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141395">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
◽️
عدم حضور در لیگ‌های معتبر؟ بازیکنانی که در امارات هستند با اسناد نشان می دهیم نسبت به بازی با مصر 25 درصد افت داشتند
◽️
تغییر در همکاران؟ نه چرا باید تغییر کنند؟/ در جلسه هیات رئیسه من 10 دقیقه توضیح دادم و یکی یک…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141395" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141394">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7WcvA_AoM2QmBwEmdJRLi4ge4NY-L0pVfFgjCSnV771xEffOjzSjTnWy7MvB07QpgVzqB3ufXqtTzYdHA3Bae8wCkYdYayN1owhUPJaUQAAoqd_qLh2eB0_GVw721xAiMnowidhUsow65DEUyygX3eFi_UmOcYi9S1KQz8ulE1SY_meLhmRq0y5JyfO6diI_qy-fo4Nz86fFhJ5UN464iGRlUP147-k_XgpZ-w2asLcjkXqmTZCn6ILrE89o1SEzx4yRulSw1lDdqjcGMztJljJZ0utnjHlHY80xHI49yyRtr-YOYfyCR0nkl5u_13-f2uVmt-oB0zxPnz0qmiNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دانیال ایری به تمرینات پرسپولیس برگشت.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/141394" target="_blank">📅 15:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141393">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
حسین کنعانی در صورتی که فردا بتونه در تمرینات گروهی شرکت کنه مقابل خیبر بازی خواهد کرد اما اگه انفرادی تمرین کنه به بازی روز چهارشنبه نخواهد رسید
✍️
خبرگزاری فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/141393" target="_blank">📅 15:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141392">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POlBb9QM8x5cS3NfakpnpnbkyUxxsKGjaQR54Joa8Ui-ztw2UkI5QrwgNRtomKu-_FORGhkxjj4rMzh3jDT1c0_S9CQNcy3Vp--dggwV5kojaHF6psr8RblAtqqDuRqWkwpEPN8sRx60Nat2P5M6gzzgdb6dfs5s9PI3UP--P_o65N0OXS309r704OTE6scq3ZRbnlboNiO3U_UPc6sjmveq66UNWIwYqR0ZQjCzVqMbm2RbtlI60W04XHrvSFLCC0xQHbcYgQyK32mxzSAxkZVIC69caLfV7QEpLtbfdvxYoIHY2jF1srSL-V_1LsQ7IfpwSxgEwQeS2StTGZ5Rig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
برنامه چهار دیدار معوقه هفته هفتم لیگ برتر
❌
پرسپولیس در دیدار معوقه هفته هفتم از ساعت ۱۷ روز چهارشنبه به مصاف خیبر خواهد رفت. پرسپولیس درصورت برد مقابل خیبر، با 19 امتیاز بالاتر از استقلال و تراکتور صدرنشین خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/141392" target="_blank">📅 15:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141391">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
رسیدگی به پرونده محرومیت بیرانوند اول آبان در CAS
❌
❌
دادگاه عالی ورزش اول آبان‌ماه با حضور نمایندگان حقوقی علیرضا بیرانوند، پرسپولیس و فدراسیون فوتبال، دفاعیات طرفین درباره حکم محرومیت چهارماهه این دروازه‌بان را بررسی می‌کند. امکان حضور آنلاین نیز برای…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/141391" target="_blank">📅 14:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141390">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
به ادعای خبرگزاری هفت ورزشی مهدی تیکدری از بازی کردن در‌دفاع چپ ناراضی است.
✍️
هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/141390" target="_blank">📅 11:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141389">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d8d44f8.mp4?token=GzkrBI65Ucf3X9aFO7Dm8ZsKoKRcfv2hKo5V1bk9lqdkfqxpCYMquJ_l6gcLIHRFix6Tqq_Bhe1a6Md0W2xheEwKIinBWR4xgvIJkOy0f_9R9z2pGTUfluSnJjylDAe4BEocAeEiflfrdVOmqgYh7FgqZx7fnaQ0aBuH7s1Z8yuFYl5Ob8G7aDZT78SDzmdnl6URhCwGmvunzQp8U1Xb4KjQlGw7-v-3AZAu_GWfaMpAeQrL03_iCdvWcGL2I_9ZfxWmJxpzNOtSTugtIzeznvAC12Mll_3O4R7eWBJ3SUseY8Ac_9obCd-TovQOppqUQmDQ7DtFN8MyVGL6uzMeiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d8d44f8.mp4?token=GzkrBI65Ucf3X9aFO7Dm8ZsKoKRcfv2hKo5V1bk9lqdkfqxpCYMquJ_l6gcLIHRFix6Tqq_Bhe1a6Md0W2xheEwKIinBWR4xgvIJkOy0f_9R9z2pGTUfluSnJjylDAe4BEocAeEiflfrdVOmqgYh7FgqZx7fnaQ0aBuH7s1Z8yuFYl5Ob8G7aDZT78SDzmdnl6URhCwGmvunzQp8U1Xb4KjQlGw7-v-3AZAu_GWfaMpAeQrL03_iCdvWcGL2I_9ZfxWmJxpzNOtSTugtIzeznvAC12Mll_3O4R7eWBJ3SUseY8Ac_9obCd-TovQOppqUQmDQ7DtFN8MyVGL6uzMeiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کلیدواژه همیشگی مصاحبه‌های بیرو
درصد، دلار، ماشین، میلیارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/141389" target="_blank">📅 10:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141388">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
افشاگری میثاقی از نامه وکیل آسانی و فسخ قرارداد با استقلال در تاریخ 14 جولای!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/141388" target="_blank">📅 10:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141387">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ri-FB9rVFvUPMJIp22WELMLmfVNtKGoBKrQFcQcEQvZyq1XC-odBUAofw2Pc2w36-Cv_rXCPDl6yGJkEN4jTHfnRLnJk_lfOKGfhAIFUwRVddU5mEQvHbxUDpB2wNnKbMF1N9-nMMQiJ9Bw4WOK2JkGNKzQheenKIe1B-hZClM84Lz4WUhrwX--MBttZamClMTCCx2REviq3ZeBP5WW4qKvJpER1gHB_rORQntkEhE7XJr4UzshOhI9sDMLN6Z1eu47-D6vDUtHLwAPfJI-RmBVGoaNa6Mgrb3p3QMc903qJ_aUcpOtpbRbFO8qMQ14wplwWnMhqMMWarqlVRDlv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📘
⭕️
همین یک‌ قاب از تلویزیون و دوخطِ پشت‌سر میثاقی که نوشته « با اثر فوری فسخ کرده است» کافیه برای حقانیت شاکیان و غیرقانونی بودن این آلبانیایی شارلاتان. همین یک صحنه بسه و دیگر هیچ‌!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/141387" target="_blank">📅 10:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141386">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
افشاگری میثاقی از نامه وکیل آسانی و فسخ قرارداد با استقلال در تاریخ 14 جولای!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/141386" target="_blank">📅 09:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141385">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
◽️
عدم حضور در لیگ‌های معتبر؟ بازیکنانی که در امارات هستند با اسناد نشان می دهیم نسبت به بازی با مصر 25 درصد افت داشتند
◽️
تغییر در همکاران؟ نه چرا باید تغییر کنند؟/ در جلسه هیات رئیسه من 10 دقیقه توضیح دادم و یکی یک سوال نکرد .من گفتم توضیح فنی و گزارش را دادم و اگر کاری نیست برویم چون قرار بود تصمیم گیری کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/141385" target="_blank">📅 09:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141384">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎥
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
🚨
ماجرای بیرانوند و وساطت برای او در بحث سربازی؟ به هیچ عنوان، وقتی قانونی هست باید یکسان برای همه باشد
❌
بیرانوند باید شرایط قانونی سربازی را انجام دهد
❌
او تمرکز لازم را در این چند وقت نداشته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/141384" target="_blank">📅 09:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141383">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65a8965627.mp4?token=W-f8MjpNE__PbO6c9lvXJUKgHpfw5G_1UjBi5z-x513SU9kTdvFGKI_L09LHYQC12E_1XxTZV5v3jsvUJAskpBlgZik77GbmOPWyAdh3FHeGqgHYIYribzbtcHdb4vF_-EBVZDZgNrCRdci00fzv9L2D0QDfE0SlvHRVTPeiQwcrP7KmIVXlUCoYupShfR7GVx7Z1BxQga4GqB-u2tsEshhLV7EZdEDD9pSTThCjW_Be6kDxyg2kr-JiCl5z1ZDIe37GXsU91vwFUquQKRIgs5lMMRWTmuesAp6xn0YRYlhqSgvrWUaRIbYX-oCt0zEefgV1CexZaFOwwe6RIGGCiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65a8965627.mp4?token=W-f8MjpNE__PbO6c9lvXJUKgHpfw5G_1UjBi5z-x513SU9kTdvFGKI_L09LHYQC12E_1XxTZV5v3jsvUJAskpBlgZik77GbmOPWyAdh3FHeGqgHYIYribzbtcHdb4vF_-EBVZDZgNrCRdci00fzv9L2D0QDfE0SlvHRVTPeiQwcrP7KmIVXlUCoYupShfR7GVx7Z1BxQga4GqB-u2tsEshhLV7EZdEDD9pSTThCjW_Be6kDxyg2kr-JiCl5z1ZDIe37GXsU91vwFUquQKRIgs5lMMRWTmuesAp6xn0YRYlhqSgvrWUaRIbYX-oCt0zEefgV1CexZaFOwwe6RIGGCiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امیر قلعه‌نویی: کنعانی زادگان و علیپور؟ کاش تیم پزشکی بود و می گفتند که آنها مصدوم بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/141383" target="_blank">📅 09:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141382">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06a6489f2.mp4?token=UU2FfAoWd_R6FbwKUeFbcIX_HQnDheBNRl2988on8FbYgI75qM4wdCGg3cbYGkXEjTsvMJQnMH5xvJZ6CKCwIDA11gyQEp8kbaZn3HcwqqqabD4R1-Bc_Ud4C00Q5KaBaF2ZrnMzMWG28-hWeLDXjRh0huDBadz0rZPKv5Cpc8OWqxcfignj23Dsz2Ln474bYsDY2mnorn-dxLV91ruVJbibI9tWb9ox1paHUSSsLy2YRRLcgBM8KPZj2sw47Zydf6hZg00ayR0V5CrSuB0np9xFMwQkelRqndlUpOAWf624AxDFCD4XUH0QneQWz4oyUedT1YDoBei67FSpdRJfuFoMh1vWITQh2XK8M1BADhoHLqQ8eO1RKTW5Vu41A95VJRIDStB1ehWg6TpYPcaEwb7dXjrerREH-FSHL-5n1C7OGnoGjYJHhvcYL8HX3tmpOn9StZhr7NdTnXQMwgMtFsWIFYwFJRiy10g8NTTe7neRR4DByHVA6xVz5u_zOF3TBRD7wnJHUefHdpYkaTOmy5-mQZaRK_RsxiNdhcGEVYlly9glb7H-zJK25PlBn5QHru26uTuO8Xq0kRD51it3CM7Wcm7wmhqVNe-UkLmZC7BOiQZMjImReB0Uz17F3LhbI0_xQq8jwqul6kWCcn5AE-cZqP51p2NcmUHStA2DuTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06a6489f2.mp4?token=UU2FfAoWd_R6FbwKUeFbcIX_HQnDheBNRl2988on8FbYgI75qM4wdCGg3cbYGkXEjTsvMJQnMH5xvJZ6CKCwIDA11gyQEp8kbaZn3HcwqqqabD4R1-Bc_Ud4C00Q5KaBaF2ZrnMzMWG28-hWeLDXjRh0huDBadz0rZPKv5Cpc8OWqxcfignj23Dsz2Ln474bYsDY2mnorn-dxLV91ruVJbibI9tWb9ox1paHUSSsLy2YRRLcgBM8KPZj2sw47Zydf6hZg00ayR0V5CrSuB0np9xFMwQkelRqndlUpOAWf624AxDFCD4XUH0QneQWz4oyUedT1YDoBei67FSpdRJfuFoMh1vWITQh2XK8M1BADhoHLqQ8eO1RKTW5Vu41A95VJRIDStB1ehWg6TpYPcaEwb7dXjrerREH-FSHL-5n1C7OGnoGjYJHhvcYL8HX3tmpOn9StZhr7NdTnXQMwgMtFsWIFYwFJRiy10g8NTTe7neRR4DByHVA6xVz5u_zOF3TBRD7wnJHUefHdpYkaTOmy5-mQZaRK_RsxiNdhcGEVYlly9glb7H-zJK25PlBn5QHru26uTuO8Xq0kRD51it3CM7Wcm7wmhqVNe-UkLmZC7BOiQZMjImReB0Uz17F3LhbI0_xQq8jwqul6kWCcn5AE-cZqP51p2NcmUHStA2DuTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی: در پست خدابنده‌لو، عزت‌اللهی، قربانی، حاجی‌عیدی و نورافکن را داریم و به همین دلیل دعوت نشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/141382" target="_blank">📅 09:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141381">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW-WQA6IrmeUdjqzI2zYbbaGXwIz5Y8O43EBTmdDxRajmiRl0Ada9M0WISiNstwHlZJz411PLXM_jpZa1XuqaftsrGOCPSjmb0aHOfXjgxkSfEvubwnZEYytAFtgkaAEL6UXmmz1iQaRT3sLJ6VCYiPz9qPsT6dMZdsoGD3BfkOHnzKTLrOoZhoLSuzlkvbsMj-jm2DY4IS_NX7h1biavsOc1Fv3izUePRPHYyQAn-UnLcvkHBLrihlAuJxlIPWMyPCa6r818pebJ_LBOJfCUGx3-Q34JNtSjm8ZMXQW8rankxevVScaXfk3lUgEaH-QIu_oIeb6LNGnRUjnNwguZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
به رئیست بگو خر خودتی…دستتون رو شده؛۳۰ مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141381" target="_blank">📅 08:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141380">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZeenoEisiMMM-AasXprxqUXmvErWGwUlIhshX8sva-gLAZTlfNrxMtPy4ic-7BISCfGchwQ4Oh4L_ykb_v5amYjLF9r4TgcR288WXSxVbAepXzU52rpyx29214zJuhdTYijh16oxfVefUSdA0pBnPiaC1E6uvWltO1rfxr844jtt_krNdJGxwIjZJsNWq8e_rAD90zzbc3M6B4kRYLeZ7TU5sYGQKuqZC0SLh_Tkr5mRiy-nbzuCN69Hn4pK_HptNWs6pLQpEERi6-WNv6HbC8dcj_8s5ES2CP5ID9dyvSM_gGGx0Valadg55UMVM_US_aAt2tRs3E0Q7ksF0i7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرداشب اروپا در تب‌وتاب شب‌های سرنوشت‌ساز؛ جایی که غفلت، تاوانی به قیمت امتیاز دارد!
🔥
⚽️
فرداشب آرسنال با ضریب ۱.۲۱ و اینتر با ضریب ۱.۲۳ از نگاه ضرایب، مدعیان اصلی پیروزی هستن؛ بارسلونا هم با ضریب ۱.۲۶ شانس بالایی مقابل گالاتاسرای دارد. تقابل اتلتیکو مادرید و منچستریونایتد با ضرایب ۱.۹۱ و ۳.۶۴، از جذاب‌ترین بازی‌های فرداشبه؛ درحالیکه ویارئال و ناپولی با ضرایب نزدیک‌تر، رقابتی متعادل‌تر رو نشون می‌دهد. دیدار لانس و اسپورتینگ هم اختلاف ضرایب چندان زیاد ندارند و همین موضوع، این مسابقه رو به یکی از دیدارهای قابل‌توجه کنداکتور تبدیل خواهد کرد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141380" target="_blank">📅 01:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141379">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
گویا یحیی گل‌محمدی در یک قدمی سرمربیگری تیم ملی امید قرار گرفته است. فقط کاش یحیای عزیز حواسش باشد همه بازیکنان این تیم باید زیر 23 سال باشند. این دیگر اجباری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141379" target="_blank">📅 01:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141378">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⭕️
⭕️
⭕️
هومن هدایتی مشاور حقوقی ورزشی:
⭕️
استقلال تخلف کرده و باید منتظر حکم سنگین باشه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/141378" target="_blank">📅 00:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141377">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
با توجه به مصدومیت حسین کنعانی و دانیال ایری، زوج خط دفاعی پرسپولیس برابر صنعت نفت آبادان، محمدمهدی زارع و حسین ابرقویی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/141377" target="_blank">📅 00:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141376">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
آسانی که مصدوم بود و جای رزاقی نیا اومد تو زمین ...خود آسانی مصدوم شد و از بازی خارج شد
😎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/141376" target="_blank">📅 23:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141375">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890159133.mp4?token=pYk3QGNurIhC1rqfnAmTjmxbSZrjn5wf5YIeSop7zFBAu_C6dLHfQ-ANEHT-JnevtYDg5jaL4Eff6nBBEQ68FswUXmqa97cmqte8XcvrX-t_9VIKke-MlhP7Q06StGKPgiAJlQK58z4NxeYCWg4UtOSRZ2rweovr_-amA5pj6qj4XpELuj-yGcUlbFSMgJPPt8c3CQC8F7iXiGEL9kyw8lT7TXATHooneSI9fQm9-DcuO1ylTVkx3FlD-MmeWmWL9PyqqlyYLMJ8rV0j7jsiPjSIgSyJ2M3uDG8n2BwWUkMcWrjCyBOK0XzVSaBU6cErbhavYciP5PTVmfiiJjb9Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890159133.mp4?token=pYk3QGNurIhC1rqfnAmTjmxbSZrjn5wf5YIeSop7zFBAu_C6dLHfQ-ANEHT-JnevtYDg5jaL4Eff6nBBEQ68FswUXmqa97cmqte8XcvrX-t_9VIKke-MlhP7Q06StGKPgiAJlQK58z4NxeYCWg4UtOSRZ2rweovr_-amA5pj6qj4XpELuj-yGcUlbFSMgJPPt8c3CQC8F7iXiGEL9kyw8lT7TXATHooneSI9fQm9-DcuO1ylTVkx3FlD-MmeWmWL9PyqqlyYLMJ8rV0j7jsiPjSIgSyJ2M3uDG8n2BwWUkMcWrjCyBOK0XzVSaBU6cErbhavYciP5PTVmfiiJjb9Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گل شماره ۹۸۱ اسطوره رونالدو
❌
پ.ن فقط 19 گل فاصله تا آمار عجیب و غریب 1000 گل مانده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/141375" target="_blank">📅 23:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141374">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✖️
✖️
سیدحسین شریفی به عنوان مدیر صدور مجوز باشگاه پرسپولیس منصوب شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141374" target="_blank">📅 23:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141373">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8WOAt3giGga4rtepGJDUNLDPnsX4ikOYlOpSpsZtazdzVnU9wEKliqEDcRgd0WPYiYKeiqOgcrmE-sNqIfQVPgw5sboalWGjg_jDn4oef2tF5zmQY8D8y4LXALt1Mov-AeNkBilryXhFxTHSPKBcun9p-QZl-cFeDXfOlm5Rc62mtmYFwPiclit5QxCtFOAt5Gep1mJ6C3TqBI6xNoyHFepthWtTF8W3DTveUIO1WDkcOuANTttz8GHgdMP8iEhJ4UnWA4QsFAVWJ5zFtIZKKNKGKpIqZSKTyOc1Tw0yxyscimxnqx9jNmomKUWlO14Eqwan5_BE_Qg3uRFHNcsaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زوج خط حمله مقابل خیبر
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141373" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141372">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVkhdMhzapMtLcVYiBoKcNjMeqZAKqgGqiHpxzS9fpVjk1-z4i2QGhhehhfV9rVTABhZyGiQeBUpODu7C_gluuY0nX88Eec7sPquJEimVudgujSWDkivLJ837sf0ODnQi5eCKhk7uzCKWUrUxZ5Lnu6rXIVcheGOubvvJku2lJkIoAY0wF89Wasxa_IK-dXAsPkUgOhRw9FkQuaUD-vjJFjJct5qkc-P8vANt0VtU1FL2ABAjBCgEduWYadE6U4rRa2qbioG5cNSXgMSCb5CarodjtI8eYT5yMfSQl5V-u1XJG5OisuAKq_bnj5v4rhFhjF-HFT7ouq_B_dFQW2U4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
احمد کونِ دروازه‌بانه الغرافه واقعا اسمش برازندشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/141372" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141371">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
لعنت به این آسانی ...ده دقیقه اس اومده تو ..گل کیسه رو زد .با ی شوت دیدنی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141371" target="_blank">📅 23:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141370">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
الغرافه گل مساوی و به موقع به کیسه زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/141370" target="_blank">📅 23:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141369">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
لعنت به این آسانی ...ده دقیقه اس اومده تو ..گل کیسه رو زد .با ی شوت دیدنی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/141369" target="_blank">📅 23:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141368">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
فوری/حوثی ها تهدید کردن اگه بازی النصر برگزار بشه ورزشگاه رو میزنن
❌
بزودی تمام ستارگان فوتبال از عربستان خارج میشوند
❌
العربیه:
❌
❌
نیرو های امنیتی بخاطر حمله حوثی ها سریعا رونالدو رو از ورزشگاه خارج و به یک جای امن منتقل کردن
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141368" target="_blank">📅 22:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141367">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn4dcb3SqHHw4h2px-KXU7hDN4aFKQcpa0iqvbJUyicuwlXAbnOb6Y4QJKJxQLtMa05sn91u9sapqwY2Ut9EC46kh-ftjOEcfV7cP68R2rSJGPe8J1um6PSBoQCkvzqyWuWZsxI4CXmW9Hxb09Q2CVbJKI1Qn1m57ldkiFRuR3OG0tl0_VhL6b9HGCYSiA9ZSRs6b9LPL5n9kqJNb1dzTHMsLGrD2CX09dmDYk4_BqAths5dOzH01oX8k2ZtO95FLgz6Dlw2owZ8z64pWzaxQKSns407bJ6wTjW8HQZGyySJmMbZWdZGiuPP_9FHHhJv07ZbgVfEb_DnOEGHDM_alg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پویا اسمی مقابل خیبر هم دقایقی بازی خواهد کرد/
فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141367" target="_blank">📅 22:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141366">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
فوری/حوثی ها تهدید کردن اگه بازی النصر برگزار بشه ورزشگاه رو میزنن
❌
بزودی تمام ستارگان فوتبال از عربستان خارج میشوند
❌
العربیه:
❌
❌
نیرو های امنیتی بخاطر حمله حوثی ها سریعا رونالدو رو از ورزشگاه خارج و به یک جای امن منتقل کردن
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/141366" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141365">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔵
💙
🔥
نماهای دیدنی از سوپرشوت یاسر‌آسانی روی گل اول کیسه به الغرافه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141365" target="_blank">📅 22:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141364">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
احتمالا بازی های تیم های بزرگ عربستانی هم مثل ایران به خاطر شرایط جنگی شرایط میزبانی و دیگه ندارع و تیم های عربی هم میزبانی خودش و باید به کشورهای ثالث ببره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/141364" target="_blank">📅 22:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141363">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
بازی کیسه و الغرافه هم شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/141363" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141362">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
‏بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141362" target="_blank">📅 22:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141361">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=gwKwVU2ZGzr1DRDd769zUG7D479vsXehXYJOeiOljSEJPChT40TFob7D-CA0ZKQORXdcRBwFD6Eyp-vAcdlZWwgio-tfOpfIMcp3Ldhv-DIUauzO95y2FIpTA3OLXU8VhYZ3o0X5SVxXilQt0zSEPVANe1hssfEY7bNAg0cUWyyXm2oPbxnf6Wpjd2k0ifQw2ciuh-fCegOOAIdmTgptcpHre1GkUbbbLbBQGv6VD6lVsRS1hYx7S8kcNERkcORkGMcJgZIJNwO3bSmuIZptYt0ahIB4tf-3C1xtkRStKNOCilUa3B6iB6nXNDolCVXqAtq_4VHheCXguE2Rd-QmIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=gwKwVU2ZGzr1DRDd769zUG7D479vsXehXYJOeiOljSEJPChT40TFob7D-CA0ZKQORXdcRBwFD6Eyp-vAcdlZWwgio-tfOpfIMcp3Ldhv-DIUauzO95y2FIpTA3OLXU8VhYZ3o0X5SVxXilQt0zSEPVANe1hssfEY7bNAg0cUWyyXm2oPbxnf6Wpjd2k0ifQw2ciuh-fCegOOAIdmTgptcpHre1GkUbbbLbBQGv6VD6lVsRS1hYx7S8kcNERkcORkGMcJgZIJNwO3bSmuIZptYt0ahIB4tf-3C1xtkRStKNOCilUa3B6iB6nXNDolCVXqAtq_4VHheCXguE2Rd-QmIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141361" target="_blank">📅 22:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141360">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
واقعا ی بازی خواب آور و بی روح و سرد و مسخره ...بازی صفر صفر تمام شد ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/141360" target="_blank">📅 21:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141359">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
پایان نیمه اول |
🏆
هفته دوم لیگ نخبگان آسیا
🎙
تراکتور
0⃣
🆚
0⃣
الشمال
🇶🇦
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141359" target="_blank">📅 21:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141358">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
حجت کریمی شلنگ رو گرفت رو بیرانوند
😂
❌
❌
حجت کریمی: بیرانوند سال گذشته 100 درصد قراردادش رو دریافت کرده، در حالی که طبق مصوبه سازمان لیگ تراکتور می‌تونست 70 درصد قراردادها رو پرداخت کنه. امسال هم بیرانوند 35 درصد گرفته، در حالی که بقیه بازیکنا 8 درصد دریافت…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/141358" target="_blank">📅 21:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141357">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjOqeyQ6OZHEaDpuV21l3hsl5sRloO2vZLBin_GFZ8ruiOpiDIJ4G3PDJzzvqTXOlUY6ppqum62qi-KfWJpAl-kI4TG24abveZIZm2g6KZTlDejImanVZbWytWdBCRkJE0Ki8cafSa19TjnOpjw_LNm8GupEdSR0NpnBg3gV5NsFEU6qotXahfgqpotrooi2bgiRRphSoBZJJSTTEx36oi0r_8XDDl0SNl4tgEd1NNgbJpE9I-wA-T-PS2ZTn9o8EKlakuNwisi6vyFdJQKfXcLVsWZ5gN-8NpQrMwUvqgHZe3g5o1j_MPQ2WrUiQm4jj4gitrEXAD4ys0xw7_RW_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/141357" target="_blank">📅 21:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141356">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
سرعت، برگ برنده پرسپولیس تارتار
🚨
فرمول تارتار، ضدحمله‌های سریع و برق‌آساست؛ پرسپولیس با چند پاس سریع از دفاع به حمله می‌رسد و حریف را غافلگیر می‌کند. البته تیم‌هایی که دفاع فشرده داشته باشن، می‌تواند این تاکتیک را سخت‌تر کند
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/141356" target="_blank">📅 20:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141355">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
فوری؛ کد سربازی علیرضا بیرانوند فقط برای فجر  صادر شده و راهی این تیم می‌شود. او به دلیل تأهل و داشتن دو فرزند کسری خدمت خواهد خورد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/141355" target="_blank">📅 20:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141354">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f780d2f1fd.mp4?token=KiZKenrzj6Fedjt9NDo9G4nAovjU7uK6nF2zgiT-GReQmvPkMW350_bzwkcch_PAnWoYw8KjawmQ6mICJWHQU4EfM5vlPn0yKA1IdRPe8Rz_OeNcPDMw-wkOMt5hwwl-GB4VoJ5CS8HhivX6BI6OTAhNgD5rG-KZKi1YSzctZkFXs7UAsHyYBKMKCcRIh7DqckUw24Jp11GxLcw09YdVIP1-iWg5fkGGHgkp5jsXETnjKrSTWjO9D7w3eYF-Ql7_H4cJ2VcxZXQwEKzN2o38p3IMO1qsI3qkhTRNGVBRfeEkCgfyKvvVUpNBfxJ2Uqb6Gc1GAUpONqPf6GAiZLZq5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f780d2f1fd.mp4?token=KiZKenrzj6Fedjt9NDo9G4nAovjU7uK6nF2zgiT-GReQmvPkMW350_bzwkcch_PAnWoYw8KjawmQ6mICJWHQU4EfM5vlPn0yKA1IdRPe8Rz_OeNcPDMw-wkOMt5hwwl-GB4VoJ5CS8HhivX6BI6OTAhNgD5rG-KZKi1YSzctZkFXs7UAsHyYBKMKCcRIh7DqckUw24Jp11GxLcw09YdVIP1-iWg5fkGGHgkp5jsXETnjKrSTWjO9D7w3eYF-Ql7_H4cJ2VcxZXQwEKzN2o38p3IMO1qsI3qkhTRNGVBRfeEkCgfyKvvVUpNBfxJ2Uqb6Gc1GAUpONqPf6GAiZLZq5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پیمان حدادی، مدیرعامل باشگاه پرسپولیس، به مناسبت روز دختر در محل تمرین تیم فوتبال بانوان حضور یافت و با اهدای گل و هدیه به اعضای تیم، این روز را به دختران پرسپولیس تبریک گفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/141354" target="_blank">📅 20:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141353">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
بغداد بونجاح و ریاض محرز، دو ستاره الشمال در بازی امشب که شروع شده مقابل تراکتور غایب هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/141353" target="_blank">📅 20:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141352">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq6lkyaCKkCFrRnf4gsOisW2-gUFT9fAWHfY8D3SXjXv5mhY8Y3SchFGIpTWsVQ_-1bwWjmc9EgG4AuBzeD4dEIKvcrKnNWJDlIOk6s624PZncaXlSJuaTXyUOsbWlkwVfcG9HOmusljgI1n1lhy2p6nLe2S_hqJ3cMsOvPYSVGig-ec7mlqx4uUu-dnX0gtLMZQT29E-fxpjKYMxr0naV-3XeZt-V3ZPz0PB4C_xTdmtKTQC8YW_HRwi3QQaXCzBMXw096iyKlhpskw-zSAJBVBoto3kDHR1i-JK9XwR9hwfpZf5DJS8K7YA7boXCg681VIr7KT0SgcLHtDM2hl6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
Al Gharafa
🆚
🔵
Esteghlal
⏰
Tonight 21:45
🏟
Thani Bin Jassim
🟣
الغرافه در ۸ بازی این فصل ۱۷ گل دریافت کرده؛ نقطه‌ضعفی که استقلال می‌تواند با حملات سریع از آن استفاده کند. استقلال با روند بدون شکست در ۹ بازی اخیر و برد ۳–۰ مقابل السد، از ثبات دفاعی و اعتمادبه‌نفس خوبی برخوردار است. با توجه به ضعف دفاعی الغرافه، گل‌زنی استقلال دور از انتظار نیست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/141352" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141351">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
علی پروین: فوتبال این روزهای پرسپولیس من را یاد دهه ۶۰ می‌اندازد، این تیم قهرمان خواهد شد؛  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/141351" target="_blank">📅 20:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141350">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🆔
⭕️
⭕️
| ورزش‌سه:
🔴
❤️
پیمان حدادی در پرسپولیس ماندگار خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/141350" target="_blank">📅 19:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141349">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✖️
✖️
✖️
✖️
با توجه به درخشش مهدی تیکدری در پست دفاع چپ، پرسپولیس احتمالا بازیکنی در این پست جذب نمیکنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141349" target="_blank">📅 19:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141348">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🟣
تراکتور در مسیر قدرت‌نمایی؛ الشمال آماده غافلگیری!
🔥
⚡️
[ تراکتور
🔴
🆚
🔴
الشمال ]
⚽️
تراکتور با وجود شکست در بازی نخست آسیایی، در ۹ بازی اخیرش ۵ برد و ۲ مساوی داشته و از نظر دفاعی آمار قابل‌قبولی ثبت کرده است. الشمال با میانگین ۲.۲۲ گل زده در هر بازی، خط…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/141348" target="_blank">📅 19:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141347">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از آنا
🔹
باکیچ به دلایل فنی از لیست پرسپولیس کنار گذاشته شده و مصدومیتش کذب محضه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/141347" target="_blank">📅 19:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141346">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOXBLjyHfU0St2DH_DxeyxvgEyDYQBEg7DMgGYCLDgDJ3CzPqjb1Vv75cZq3rPuhHgd3YSstcmMMo0zwQFzqBKpenWmW20h9K9ZgNFarYTo6FYtmJXUbkzZB2SMMZ1HTPkH36XLG5Un7bv29CBOEIJDZ4EXI_FREbfXswkbL8XRLpKSunrDuSr68zBOv1PRRuLwEVIbZjQZ72bNBk5P1KAj8Fu2TSq4JWBh7ukf2boN6U6m7qFneZ11q858fBqtjkz9xRlpfbTeU7TbUIx9DUd4vs9LHvTxyzLdqcc_LX_IQjNJlComDCCfaUj739T6V9cxOQw6Q8QyDDunAqa51hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گویا یحیی گل‌محمدی در یک قدمی سرمربیگری تیم ملی امید قرار گرفته است. فقط کاش یحیای عزیز حواسش باشد همه بازیکنان این تیم باید زیر 23 سال باشند. این دیگر اجباری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141346" target="_blank">📅 19:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141345">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4rwnp5vGKcwGz_nhWGnSUaI_P3hOB4vmrPvv0I3_l_7QKJ8MX6KZPeqIS9DblRapXSuajwKZSZQqTbr4AW6XD4e2oB1zajwxMVDMoGNirPoCSmmKaOT4Mg68UgyDd3vkoRhCH4LhqW-dKxuK4BBmg3mqkb_vD5fpEW8dgqX_2UfXgwSyoj-jnsCaQDOEHl__99va8M8Vmljz_11tdV8KeHlyHzaeeDR-Gfz-UQkIRb8IXllDbePp4nBYJWL1hlDTZH7RhhvXr71lm5AF19Xw9D7a-5cPJcKCWVY8XY2QyUcB4EqukNTft_IlTB37LDANwvnxHY-onAN5kuyiFS6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
مهدی‌تارتار به مدیران پرسپولیس اعلام کرده که اورونوف غیرقابل فروش است و این بازیکن باید در تیم بماند. تارتار معتقد است که با وجود سن و سال بیفوما، حضور اورونوف جوان در ترکیب تیم ضروری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/141345" target="_blank">📅 19:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141344">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSP8uYPKpDBDunw2CKmOecctTAck_-x9n0rpmMqKriUyh6fsa7cA5ptAFzcUL7M3jnU_Sorpe-KKnLMN54h75CrEHccXVBG0-Wxqo0Gl9PCiNNFMsnEk7BCaGunx3VQc1D0KgLP-v2KHeblmHn3olSwF_BKZFWsI-jG89nNjk6-ahUOdukge-e-kHjLXTl5YVnaBxCOMqzyipx1tkJ-dhYOH9fb8unfVvMm5qWpFeu87gYGbhZOoMS7weLWRy03UuazeuL4h403sS-n3ljMp84n5ChZcjjkp52mBsUmKP7IWUWLF0jYlHY-FDm_KgVMDTKnyYYuts-JVYpQTLdWeLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🆔
⭕️
⭕️
|
ورزش‌سه:
🔴
❤️
پیمان حدادی در پرسپولیس ماندگار خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/141344" target="_blank">📅 16:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141343">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
⭕️
⭕️
⭕️
ویدئویی که کاملا توضیح میده چطور یاسر آسانی واقعا فسخ کرده و پرسپولیس باید دنبال حقش باشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/141343" target="_blank">📅 16:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141342">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
رد درخواست پزشکی بیرانوند  اول آبان؛ اعزام به خدمت سربازی
🚨
🚨
ماجرای سربازی علیرضا بیرانوند سرانجام به پایان خود رسید و این دروازه‌بان باید چند روز دیگر عازم خدمت شود. دو درخواست پزشکی بیرانوند در این زمینه مورد بررسی قرار گرفت و‌ هر دو رد شد.
🚨
🚨
آسیب…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/141342" target="_blank">📅 15:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141341">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/141341" target="_blank">📅 14:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141340">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
قضیه پرونده آسیب کتف، پرونده اعصاب و روان و خالکوبی بیرانوند در کمیسیون پزشکی پذیرفته نشد و به صورت قطعی از اول آبان سرباز محسوب میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/141340" target="_blank">📅 14:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141339">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/141339" target="_blank">📅 14:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141338">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
❌
اول آبان؛ زمان برگزاری دادگاه پرسپولیس و بیرانوند در CAS
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/141338" target="_blank">📅 14:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141337">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXHVdlZHC1ApSESYds4OcnkiBqD41qYuREkivGMf-GRkoUwD9dmLk6Nbfv0YP0sGBj-cMa686QkzY_Ju2eqGMxeIvm9b1mpbOUPkVrSov-LNo5NA1iXGJEvdy8uqQmKbHQZmVeTCINv44WIhuG8pM_m_P5nvsmWPTYqvFy0V-3yZp2YApM3FPYudoWAJBMA9i34-mPyWXmD0FcRfjmzbynpVMILr6VHQSBQ1coXQntJMBy3u3-d60lITynJRhntZ9F6tJ1Ue1wp9yFcqiERE_jpFni6wN9xUTHO8tiHk2yByS2Y-uec5B-w4iAT4tLxp9Lp_CtC81dSGv2ibJ353ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
استقلال در دوحه؛ جدال آبی‌ها با الغرافه برای یک شب سرنوشت‌ساز!
🔥
⚡️
[
الغرافه
🟡
🆚
🔵
استقلال
]
⚽️
الغرافه در ۵ بازی اخیر ۸ گل زده اما ۱۲ گل دریافت کرده؛ استقلال با ثبت ۶ گل زده و فقط ۲ گل خورده، آمار دفاعی بهتری دارد. استقلال در ۴ بازی خارج از خانه فصل، هنوز شکست نخورده و فقط یک گل دریافت کرده؛ نکته‌ای مهم مقابل خط حمله الغرافه.
سناریوی محتمل: بازی نزدیک و کم‌گل با برتری نسبی استقلال در فاز دفاعی؛ الغرافه با استفاده از میزبانی فشار می‌آورد، اما استقلال روی ضدحملات شانس گل‌زنی دارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/141337" target="_blank">📅 14:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141336">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
بیرانوند به کمیسیون پزشکی رفت؛ در انتظار اعلام وضعیت نهایی
🖍
علیرضا بیرانوند، دروازه‌بان تراکتور، روز گذشته در نخستین جلسه کمیسیون پزشکی در تبریز حاضر شد.
🖍
بیرانوند که به دلیل خالکوبی به کمیسیون پزشکی اعصاب و روان نظام پزشکی ارجاع شده، همچنین برای بررسی…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/141336" target="_blank">📅 12:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141335">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
باشگاه تراکتور به صورت رسمی به علیرضا بیرانوند اعلام کرده حق حضور در تمرینات بزرگسالان را هم ندارد و باید به تمرینات تیم امید برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/141335" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141334">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8bNUk5vinVQqwYo2p0XjuwKG4H9Jh4H85tyZneFe2Z0ABPUPyzVxFT9drcLYkU4RAxRQ6ngDX_pnwMTmVDYHRPgLRh5nwhUG4E35LDiz_hYTnrA5tZASRrQ_yYGq5kfe0TZZCrh1epso55_avw5u3wzN_dRJKnF_u5zsAr5mrsE97m5iQjhlPFNKr_4sucDWUIy2r9WE5uuqWW3B3E-UHRq-mw1OYNVLJbTibyT4Z1ypAS5Y4XdEskhMOvIAY0HpR7mmTDRUwJGTecPdMEQoKdW4HrR4ra-pUVdAsJ9EIY0a13euSVT2GgbsKiSf4267dLk9MM8Sk1saRR6p2IJ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پوریا لطیفی فر در بازی با نفت نتواست عملکرد خوبی داشته باشد و مقابل خیبر نیمکت نشین خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/141334" target="_blank">📅 11:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141333">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🆔
| ورزش‌سه:
🔴
❤️
دانیال ایری از بعد بازی با خیبر در دسترس کادرفنی پرسپولیس خواهد بود
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141333" target="_blank">📅 11:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141332">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcbMVE1URLgQrHtUkNL60jRAyS9dTlZOCvxIbnsyg7CzGOiObfjKX_GAOt5sbKQbQeq4feCyLb2ySA7-QvNE0udFtl1x5ALqCYh8d2aFrM5DTckb8pXy-B0BKtuoChRHIk1o42MQW2zA47zQtx2DFrcZHRoyLWo42wC13FKmLQ3gZRXzF8S9pXWrniQmkqxosTHPkbr0yJNCBKmr5kCgqfn8_BpzSB39xbYfsbs3tGtZoGGKng8GnCb8x6pEFx5CfoMAuDqUs1zrJiVNl_aj_-K01_APawadNrGkNpyuwxBCxyUNbPMTvSPg-FjOnkkc9Uk48ljD3LLn8XIHgB6vtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اورونوف با به ثمر رسوندن 4 گل دیگه، تبدیل به برترین گلزن خارجی تاریخ باشگاه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/141332" target="_blank">📅 11:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141331">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
| فوتبالی:
❌
مدیران پرسپولیس در دوراهی تمدید یا فروش اورونوف قرار گرفته اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141331" target="_blank">📅 11:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141330">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🎙
تاج :
✔️
امیدوارم ورزشگاه آزادی بهمن یا اسفند امسال وارد چرخه مسابقات لیگ برتر شود.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/141330" target="_blank">📅 11:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141329">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❤️
محبی؛ ترابیِ جدید برای اورونوف
⁉️
⭕
محمدمهدی محبی در ۷ بازی با ثبت ۲ گل و یک پاس گل، عملکرد قابل قبولی داشته است پاس گل اخیر او روی همکاری با اورونوف، نوید شکل‌گیری یک زوج جذاب را می‌دهد
🔴
محبی می‌تواند با تبدیل شدن به مکملی شبیه ترابی برای اورونوف، هم به…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/141329" target="_blank">📅 10:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141328">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPcw18kS8nXzAUag6r9WvVYgJ703pljkZSE8fnC-y_W4_o1F53vPCnkqG4IafsYfFuJrfPMOLl8N3iwwftjHKf0YHOQNblhPLswINoiqPjsmbm7SoKgCCm4YvLCRHJUZHBK2u29ubk-RicpAn9eOfalBYVAcmZyNl_GC2kmzovCytg_gidlL1iot4kssUMtYbIbqtByOM9jCJdrpt0-hMwz5VUuMrDgFcEb6VAqOLdojQwBN6dHZ_gIYxDuxWeOTytyyoCiCgl8RCA0yybxCsM8ECdy_wEStuM1_r3RukRrUmnBx6zDvf7Hypz7qYfz1hmUL4NJCsQXsrpr1AeBMvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/141328" target="_blank">📅 09:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141327">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2R_dFsMsAylyNTgY1zIHVqSmXaGas8bdEjdac1VXBoy_zRKkPJMEYc2I5mHUsWzFUe4H1LqWD5hNMMSfz_sp5911hcBmR2QiwBrRnyPDEu7tRC9PFJaKtknuSHgx067kTC5PM4Lx2cE8wVITqAA2pN2FzY81Rax0VsYlDr4XmRMKZq9WhlZlpH9sLVadekUMXKnGIQyy2f-pXTJDvoRTPX-R28GoIsxMx1TeS8uP0SXWQbmS3FtpkgSWm0ao1D7oYMtmYiBD6FQKmkZDIRTjunENhReVTlqaR-QXzTK3twpGCbeRm0qiJ87B9Lm4Vmohe8oWJC8TW6e5G011P_Sog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
تراکتور در مسیر قدرت‌نمایی؛ الشمال آماده غافلگیری!
🔥
⚡️
[
تراکتور
🔴
🆚
🔴
الشمال
]
⚽️
تراکتور با وجود شکست در بازی نخست آسیایی، در ۹ بازی اخیرش ۵ برد و ۲ مساوی داشته و از نظر دفاعی آمار قابل‌قبولی ثبت کرده است. الشمال با میانگین ۲.۲۲ گل زده در هر بازی، خط حمله خطرناکی دارد؛ اما میانگین ۱.۶۷ گل خورده نشان می‌دهد در فاز دفاعی آسیب‌پذیر است. تقابل قدرت هجومی الشمال با ساختار دفاعی تراکتور، کلید بازی خواهد بود؛ تراکتور شانس خوبی برای کسب امتیاز دارد، اما غافلگیری در ضدحملات دور از انتظار نیست.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/141327" target="_blank">📅 01:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141326">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🟥
واکنش علی بازگشا به شایعاتی که برای برهم زدن آرامش تیم ساخته شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/141326" target="_blank">📅 00:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141325">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZF2XBRkTUytJjoYWqGjd9L4y8g6qJ8DdSnDW7drP3p-uEsUWHTBQnWhD7SGsocODUhhnK0-kGMNu7usMzSliO7PrVZ8HNtueOe-i1DYopZd678w2bwWO1o18eyDiP9cgeF3m7LHNBxceGpLAq42b_R7xmONKgOcerPFtR2vDqJZtS5MbX7FtnS3r3HVl0NN3yuMc4F4N2JQz1IIISHDMT0wAQWUfw7WGrH4CaAle-TC7s1A2hlwbzPKLxYJFVZGvoNYa-3hhrcGcYFyt7Ch2BC0leEjQx2r2w7anqlClrf4HOykJp2po9jfwHbh1tg37Exa_9Mpw9uOtrM7C3vtww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
واکنش علی بازگشا به شایعاتی که برای برهم زدن آرامش تیم ساخته شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/141325" target="_blank">📅 00:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141324">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6166ade5b.mp4?token=rrWi7HptEjWvYNeZdXClV3mV9dUWFn-qVyKvqKo-3KSS6wrXfZvZQiS2Kp7sb5utW2IBil6x0GGSr22HRulZ3dwJ2JFDJmysP2kkdCcv3Z7qt9SpCzI5TxwJMaosfh_WxgKOsbENwKAJ96OAw1P3VK3asgJZLlgUKSNF-3xBmUJHUDOnm0gTXeNxaOT3pc6ixAS_Grnpb5hVS-pSyfuwZEliAFxvxUQgUSkTi1Dtto9_annpvxS2Yn6dMuxM1MoYUy0f2NeS2pghrqHEXzLDhG7ZkAnobaqYtrIvXvgEWQ0pNp5psSO-So_b5HGb9aBhKp6pr6BbXTBovaSzLVCVioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6166ade5b.mp4?token=rrWi7HptEjWvYNeZdXClV3mV9dUWFn-qVyKvqKo-3KSS6wrXfZvZQiS2Kp7sb5utW2IBil6x0GGSr22HRulZ3dwJ2JFDJmysP2kkdCcv3Z7qt9SpCzI5TxwJMaosfh_WxgKOsbENwKAJ96OAw1P3VK3asgJZLlgUKSNF-3xBmUJHUDOnm0gTXeNxaOT3pc6ixAS_Grnpb5hVS-pSyfuwZEliAFxvxUQgUSkTi1Dtto9_annpvxS2Yn6dMuxM1MoYUy0f2NeS2pghrqHEXzLDhG7ZkAnobaqYtrIvXvgEWQ0pNp5psSO-So_b5HGb9aBhKp6pr6BbXTBovaSzLVCVioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
⭕️
⭕️
⭕️
ویدئویی که کاملا توضیح میده چطور یاسر آسانی واقعا فسخ کرده و پرسپولیس باید دنبال حقش باشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/141324" target="_blank">📅 22:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141323">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
پشمااااااااااااااتون بریزه
‼️
🚨
🚨
🚨
با دستور مسعود پزشکیان رییس جمهور جمهوری اسلامی هواپیمایی مخصوص رییس جمهور برای سفر مستقیم استقلال به دوحه در اختیار تیم استقلال تهران قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/141323" target="_blank">📅 22:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141322">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=In-NUZnFD6G6ALt7LONxogofurW5BuaJS3umKeHObPEeLzrQLuUuuGn_bROobEg45UZk3gDJefLIBoIOsAXFEeKA_usOz0GtzD-YKD_dyXlf5aiAMxKLDiYtYrZi4GYThIoAg3JoaYfswoAkk6cYqop-V_lRHFnslLMPZS7gTcwF28K87auZOgkvo6J-KAXmH4c-NShqaZSCfuJh487rDmpkFYJ70FY4xV-zLr14gofyJmUJq7VOEGfqO8YM40u58yl-qHWUPYUYX34Axfro_KpGiKnMtIzw24d1OM7a5bR0tNnp76Ld6tGBimZKkZpVVSWh_IuZawcF9bZ0UzPkUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=In-NUZnFD6G6ALt7LONxogofurW5BuaJS3umKeHObPEeLzrQLuUuuGn_bROobEg45UZk3gDJefLIBoIOsAXFEeKA_usOz0GtzD-YKD_dyXlf5aiAMxKLDiYtYrZi4GYThIoAg3JoaYfswoAkk6cYqop-V_lRHFnslLMPZS7gTcwF28K87auZOgkvo6J-KAXmH4c-NShqaZSCfuJh487rDmpkFYJ70FY4xV-zLr14gofyJmUJq7VOEGfqO8YM40u58yl-qHWUPYUYX34Axfro_KpGiKnMtIzw24d1OM7a5bR0tNnp76Ld6tGBimZKkZpVVSWh_IuZawcF9bZ0UzPkUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🎙
پیمان حدادی: از اول فصل تیم گرفتیم هر یک از تیم‌های فوتبال پرسپولیس گل بزنه، یک زندانی آزاد کنیم و تا الان ۴۳ زندانی رو آزاد کردیم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/141322" target="_blank">📅 22:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141321">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXC6ecQyF5HjHL49Xw9OnVpbGUsVw36HalodoRmS2_1_9lwFug9vBwE_X0qzoJn_9Stm8s8S8BV9U2WP93Faw_PkPxDLlM-jH7EfPTRYVeMaAd9ZsqBeYaL70rgy0HEMwEmb8et6cVD6Em28f66vOVl5KVyARwsQB3o2wkZ8CKYtWPpyAUaexnBuKhkB87IPyprEioxJUu4ELOYePaM4VXOgrhzAfHNHoxAfYJz-fTYBq2mrP_lmTgW8vK_PS7rNBi7i1uZxnKibdjGOQUeDUV8F_XxkPOKn_ImPjCjJ-hyxW3BiaYLOcDXO7vEKTt7GyBQYwz29tJ0yTFnslRVxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دانیال ایری از بعد بازی با خیبر در دسترس کادرفنی پرسپولیس خواهد بود/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/141321" target="_blank">📅 22:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141320">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_BihNv_hom0pAPW-MmEqQy5YvvmkJeDlaE5iGmJtvCN15XqQXfaaZ6y3noINeRglmcPu2-eNyBtSx_3s1uVN08x_tBAVDcG3FoiQ9lO9A82wnvVgZUEDELMQhrrm5Gh0GGxINsE5vqlH994MRozlHVpDaZiQ1NWpQpN1fUuW4xqF2oJ1fncqmStrb45aNRMwL8SmFtltFcrzFmvx-TuGLJ07hQMUtigUJlCKrzgJ68SUoGJU7003Y0PvQ4Xtr9S51YumBDYlEZC_TaQCepmhPPn4EeE3GRT3LZ_M0cdIQKZfEjPEI5ZqkaMrzKnI8C8UlBe1up6uvV6BvQRqUNzHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حسین کنعانی در صورتی که فردا بتونه در تمرینات گروهی شرکت کنه مقابل خیبر بازی خواهد کرد اما اگه انفرادی تمرین کنه به بازی روز چهارشنبه نخواهد رسید
✍️
خبرگزاری فارس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141320" target="_blank">📅 22:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141319">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7cDLcjV_IGIvLwwhOglVnMJaxKz9LcsodKEgNdnOyee30v3fIGCHUaZo1r2D-vtWg3hfXsSchYSEIhPS5I_TMStdLliuBPogCQzUx2LcTulw4GHKZiJlGim5vqEtRb0pBpQqHZJV5hPiwvaynH3xlul_zfngEHp-PH0NWR20C4OgrBACp3Z6oJxOoov93YJVrvWcU-Z6hLaUfBSgy6387BccoaJnOW6DKM93fdiC0oy0b8VnzYLbmzWyTJxyFcMlQlz8h-BaEYGY8HQnqjXtXff6-mJzkIjIcs3Gt9Lh3In-N6Az67Z8AQq7bY4JZmKwxmnQsA-BjmljrZgazbIZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
فوتبالی: تارتار قصد دارد پست دنیل گرا را تغییر دهد و از او در پست هافبک تدافعی استفاده کند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141319" target="_blank">📅 22:12 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
