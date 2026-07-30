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
<img src="https://cdn4.telesco.pe/file/gP7Gih_e1TfWC7ws5IrNMdfbarMNY8CbuOJ2deizAjVUQR_Xjf1bv-PDumnegGfyZ4VMQj20Qatd-PPyMjymY4vmltHDziOOEiW3KbcbA8KPW-WKt8Ap9Akx7pKOo6f6lB_mt2IQLg5l8Whn9ZoW8O1Ya4IPzwAyr4PVD_80QG2uKe8-JQ6OWjO3buC9-nZ3C7XV45n-8uxVnLv_Z5UzwwhjoSue5B9uhlrSZbQTDbXx-k-4f0N6mim2Hjkwlfy7BpywY9FseToecF6-KMEM9abKQaYGCcQVtj5ASh2TQVO_gNGOvA2Crj2PafftzmqAygWB-4eglPuCgBHCCe3_bA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 609K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 19:02:01</div>
<hr>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdQ5HU6xbeUIQEIYpsqQ63L7jB1yQWcNiTqqPbaCq9iQKl6O2cfqH1aLulBz-6UCaoDhTk409RoC-_nKPE66s-Xs7YrYfazYso9xaJY4hOxOWCgIzX4M9TwvGVjl8Kay4p-5nkfdsnb0_oyVs0AhqY56wj817aoc56NONMkBfk7vp9JAi4_rmRUEUxc_-fW0reZSRit_sAXKKzMsPSqXhwRyUDvtI_phrQ47_9yEbWneESvjsc8yup-H7B03F2h7zMERoUhsbiPP3-BZoD99XmWagB1J0Ykfes9agA5rIZUgSaWUq3Z7Dzu4C6qt2H9kN-WwXrpdQsXSOBs_Xc-f6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRtqEdq0qkVD20Wp77paUnkfx_2rFhDb46Ev_jmQigViCpARdI7ZowrVqT0hG8z0ZqCaEm_pTs2LmbO_HeT75fhq2UVNgeLVmeoIU--d4maJf7Dkns2ZAAowJtkvmp9sRkdxYM-g2BkENbGjAEQPSXApI_Annimjqur-yh6F61sPfTF-1mq0hOZ6PTXz4UVKQQF6aqOfJE0zPrWaT_nXt7yh3laD6W8MxtemS27WLUWbwoDQTqy9eG9b1YPD_0ovRtI44i4TItwRuaavqkfQr5NtBS8LKom8UxZ4l9JTClBuaosvQShLkx3KfIszJlcMTyYek3ySBuasBKvrj3gCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26829">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPfxCx_-Ahoxj7VP5BDT8A5fwR5H87T0T6LbfV28CFobn41KOLwtoQ62V8ph9HD95IX_Hkgo8XrQrYUcBiJZYIv0lgtvC6Sz7JFwgO2QZ8qUymp4_de_m3wKimSXtLVSCx97QujTxnBlyy5GGiB-aELjcf_2uQrmAu9BrQE2Z82BWxDrVYd1LTl8766Vx6byaCcyzAGUHTrwoXCj4upIelDGiPchWJTgVD20GW4qzR_vWuA_eaY4_p5JbEpubIax3oMxihLa-mwf7HLYHaO6xVnrzwEVsc0yvCYW5U46Et5yb77GuWClpWxMYbdAqSRCzt3qTodtShCCEEA0ftmxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/26829" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeqhjGsS-1tR7VVlei0Sx5M4jKZT5oZrLY9zGwwDnMdtMWR4_PDa0qKIwDEEHCQMVxZsf2NzmnIFsUO1NJtQUCkw79fCYqPyDQemHVCEZkD8U46Mj7QUZtrGI2UVxhg1wGg44p40aUqATGuSpn2CAmvYf5a0G7OdqCfxVJ9ZYeJ_wKt9rSpdPGR9_BF99GOWrVCjrRrmTs-HK-lObDXv0bYDk06VoKsfipi4c5OIPzqM9FI3eQog8FMa85OlquP57K0CdyioLMgLl-8VJN5s_sN9srgpQ-9EYOgW0lpb9bm5_SEWnk6e7AENWeRrNfYCSdKRpd0wnBuoZfiT5qiAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWuiiR5v7JNVv90V62DUm6FBfSWwJjNMNhF5Io5kA5Rg99jN_lG_nL4sAcQK_ANYyJwu5Uu48tz--A8ziOMb1we627xMBXe9gXVpF8lOovWw2Y1w8XPGxd5ovHYQZyMFt5qs8Md8aUHDg5JKszZz87VjuN_JrR_A1VB2uTZ2zP7ii2S2bkATG8hVlThgEMWTdpHffG7grpErgIA_52uQSCA86uxP_9k3Pm6DQyIMjXQ9l9JRZjgLOD3UXINTYnrjblRhr20hGqCBANumqYgooxMJsY7njINWIth4Qq3aBwiK11utfwg64x0hvIRE4JJVnzyszBhJS_tKT5AQGJviaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDz7VcMTMIivY_0ieRuoVgg6DCyAY2I2fVk0GJItEPfp5cICzcW20F0G8V0CkZDoT7G3naWMfMEe-Fd_mky6-H2dg8EsZ5qzd5sZPStGSTOvgqrJ-uuX0SyPxzfH4nAwxWJjL9MDjRd4Impy6bPY18fS8ACSAvvBBczItMmNELtqJkYMkAPYs_fSyCjPCi1Exn6jF156gYzsTC1oykYYoNp-mbBRmr0QKRUcup2i1RQUTl5k2mgbMO3KqhF7SL1QpUSF83q_J7plrYFoj81plDuzNrMA8r2VWkEtm2NmT5L8Td481C969HXbyKTzU4O72Hz45DdlAWUMlIJdYuA1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKWme0TEH_Jg-8QPA4e9JThdX-Kt6NO_BBH2JIjrpJFlIkEuIgKwDlRXdQRL5DdaeyBwsq9ymEZb3pP02atK7Z0cCEwOApi7koEo2Lh7V2zrc6c06iTZom7dE5xbUYR5xIQTY6DxDISt-Rnpa7wvUuD2538LFSwmTFV_3EZ13111QRn2681mkO8w4qPtMA-CP-h9tAIIuTBcqCq34pzKxqt0sjftlLZGeY38IAuCY3ayi5bU4cgUhI5Nl9DvY20JJuUNuJcOx7Z2P4BkDjGRdjaGdJ51tBOmGhKy3G_HE-XoYIOSV2tg-wR6img9f-UAXYr06gjIih1fcExuRfPEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1HpVsRpDDNDUP4U7KBDjC0kJwcxnZZJ-X4l_zbYg8j4nrVMMBaurdJZJhE3wF5oFptXUHscqplyxKeWvMf7u9RbM_OGH_PC3dxpaXszOjQ2W9X09xz5vMp-MLbKWlWd24BE5Hh8RhoFryUtlVlGDwJzf3LeKpQKT1ye_-HXeB8bOHTko7fCQLDiZXgxTDcKDOnpDK7b5zGn6MvaAMgT21qhaK0AVjxsiLUFC4e1u6ak9mwgI809CfFpTYHIjZ37y_kf8qtrvui4VELJh5eWxItbQvWTwbtg7xDr7HfXXYxRQsXPB1iYrnrC8fQ8mJNZgEyAPKKbTNNY6gj1Wmxyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4W2fumHRq5cUrz5IA8jIb-CGoXV5mC1xXmfMHst50SYt420xy3qIHWr7osrg31Rp9naShJRKjx1Uiso6nrGQKwAO-v7270enVKQmM4XYQudmGlH53xQso1oOrIp_hC_2PMcdKmHPaAT7Dhk8YY9p1Ov0khQZfCfG968Q6O8uy4Cp0HVbU1UOaPWP9wqMGUgM4JD5jJjVCdmmmjyLuFMzgNdLuBscWUgbFfUb5ZETg2VDP_BneD83U8y6BL3PNk8qLgElId6BA7JVlGp4gSbxLguONEdXzxSDqGQc3HeCvZr599kwYM6HdCSg0STe1_oFzG6AsYYSPQTocuEKB4HkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhGF50jp9ycu7cbd56G_4H_S8-Sw5pY-b0BlSEET8jkmjI1AMx1NXP5Om02v5S8W7_oRQ9H01n4IOER-HHG-qdYh0oYhVWzW3wRBoFKXrncPKPvVMYguQ5oonlt5wqnaMRSnLrvJfHfYA8NTqcVxZ8s5ZfBAQM-yQI_3MeJkcRvi0BXeO7AzEJZKDGmx_9RIeP-wGjjx9iS6JKfhpa4JbFRTWRAZz7efRXJZ5uLBuMhDSRonbiUL6OANsJZ5axzSRjZcUTm5vMMaVCYQNuryCdZEE6wgxrGjPNZYHg1Ooll02_GEUx_1XMOAJG8IXpK9XL7uDm4q0Lk_bv6WqMSlzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax5TwQhfiBtAaurLEcFU5J7YwVToA7hygV3yuUqqyfvwBbdaxwDfEE04XKtGBatwcXndzYXnD2cd_5gAwpx9vA4f2bXpr-v2hO6LsQiqjfQ5Va-180sfNmVxwcmPuP3Q1O3m5IBqwNRrUfiQULX0hoXmgUITqrRthKQqb6nNwRotQAjJT3F64GX6EjUKPqb3kuGBJiHNuZwDn6N6jy-iJlQCJ4IgnYYFaxzpyWryd8qI56f3lp0VwtaHigrpA8gM4QneO2ejghjYvj7I4Y0raZDuvn41114hA3BW4W0twpq4xqyIL-eka0b9s3cOGyoNiBmtyKL5VHCAsuIVxVAWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvsq_PqlYWkSFU142De9mrVd19dz73UXQyLk-RHXKxtWQ_mni4VinjAUOTI_-whrEA1_ngJ_cfRpqW9mHKwSSi_lkb2TlJo0ly3QLFpxqGQmjqircElMwtTarKX1feucjAVSTSf9QVlgpjeWCXuq_-Gg3QagVQYot7CfU_UeSnb7a6rfPitScvkURXKnBEZZ9qiGxV2M9bXSl432RGOzxUZ8hI_pQfqFOI60Sp6nl7hJRMuxM7gkGnUY7T_--WcMMdSN5KMq0HyPdgLyoh-I8-p3mVhCF9d42rqEpvelp199ZdVBxx4G7hOOgZvQMiip1glueJsr2WlblXa1l_Ydmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ld94ilESsDqG4MfwlMjKWkRyFdR4Io3mxHVnX0E482NuEqIu7rZWmB7WG9uouvBNywXCOkQraqMmW6Q28-DYwyyqh6-tQH142stsrsAdYriTo5qoDjmzy25Ajk58oXvHmLcqob4eGWxXO6rRjXfEGUWBQ4uvmv7meVCpeXgz3_t55hBWqG2ArPR9TYD3xBJlDV62SHBWVubDpNsxi0WVh5bAqbVpkl1ekYXdyW8Mz3gK-TgM4OiM3DszfZoFjnSyFb2WdGbUrfvDiOUWZcAd-FiF0vzL5VFfnfKyK9Famea5qmdGAEUnrIbW-ohiIUCwfRKO3cpaMaZRnp_uFnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNJUwjSWx7IxA64IMU_-N05J-3WFsKAS1TCwtxnPTATNtkyxXTECbxiPu-xtTCwa58hreidLMS1FhabYYp78hbVOMRolUvZX_4u3YhIvk8WA_HXsQWvk4tSfPA_KCc-ER72h_nFWAYSxlJ_5zcDgz6jEsNCYTrCSlBdAHaJVo5sMSlO2xi11ba6fnp-kIolx1-vATR8hf_sqo8I6qFAW3C2RRJnXuYUzq5wt0LyQa_WxjG_7T9BlxcgAI2vP9tCDBV3Hjvp70KDOVkJ6fKrV1leP61ObPh_llwQRhd5b3CYxxgHZH-WRIS9CBVUbMGpXdMud-1ISV7G3sxuIiC6ZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeqCHsVSmKcwfef0uuAfsyFAN89AmFOEDyXkbeieSqfhqe6Shy6iAieDcrxdALYIJiD0_y9y7hxgmHBSLsCLBdbGfw7PZEaU97bXYJa6ZZzNNz7pLXlmreXIcHiZQC98GH1ULMmWlimvanFblUsydykJbliUbo3xlvpoRoNsYPJD1DGLfFqgL1LFh9rZIXlMl08kndKozqfcy4Flju2B357xN07oF2dPbFsfRwQf5Z9yGpajf5nmaa_zAd5upWA55pNa5KtHrwL5Ky8Tzu3i2H1dBaAM_8eawMbMnlKkwGcoZBGofHcuRrMsZ00lJadZ8HKcpUnR51id61EvPpfi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_zVqty7OpBMxPod8TM7LOLu6TH5agcQElx66oUHF70rQc9rinl-LNM_NwR8qKYCMX0ptzlrIkUYGhWg2YNZ7QswzWBbNw0j_NMZSMgT5zhRy9Ng_oV5X7IimxEzvU7y4W160t65lLyqVWQrplNmCnMj80GttzJr2qWBWGd9eKvH02InGYyOS9l5a64JZzcTx2RqpNaZE5WWsEdSkchMKDsxL9f25kXldK_8bpFjR7Fhj3_q99DrwHOyGMaLE0eQLHm-wlI27VW1AyGgNwAXQXo1O1AnEN7pb3SH-sHuAomsLj4suhgHQ_uLYANsqxkcsOKKGzYpu48D8pjqOHJGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEoujU2QW28HpXPT-yPVJcOzLixNW1Z10eTvA_th-lo5rc_971i9-2ZubA_Daxn39lCmmPQnBz4h1uTKER9eqHuhfZGj69REVpajqmJIPbo7AjP4A5cTaBfEVB8ogF3BUeIXadTGpy-P-VFdAJBs5bC8lRjGkepuBkPew-iEoWHGxtuea32kJG3e9fsHs_Hroi2IDHGfdagSzacfBy4q522GGCDxrLGJ4PJHezDkWJ6c-xVBdSqSeQLQDzN0FGkaPMjjize5Hqdpb47Kx43R-Swjrx-icokMQWDax1FP2aenEUNB-rtzyJq5B38aWvNnPqLHknHU8Z63xAP3HCH_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7vZombwTJZvayKQ7KQs9Jv3LwT0RbTPZrNG11zVVdBRHuKL-JfxBiCfX5MK1vDtHaXX7oJJc2KjeyR6XWPnJZtOmzYuT7yIVmyZ1riKLcE-PmWV1ZAoRJDQ7h9NBppEaKWHX_dIS6lgG2Sujo0A0n9zgqjblwqd-CQOvkNBWBvRCsonHsm8IrJImNT_m1P5Y3ECGKBBYc5_BzyYUhklfLzFSFzVkeRUHKZMbLPTUbsvI1TTbmWwYn8qxAXBorBNTa5Tol6btyv-lZy047BZp_WyLA15pjcguOtLVJXI18ltsex_c_FEWn7tm3DoDaK4dAew_20KEETabDQDIbZsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmBXiVSnDKqMYhlnCCM3WhmCWu1dT0EXB3p3Wbw-EK2jV2f_0-cKt0vEKZ4xfmiu9VPSVhUjq-SaS-yG6e7gBIpB7IJeabMmtSNQzCsXGJeo8S5-K26fkToVQskkqdmAonss9GaFiGTiYbCHhM_PP92UG0RzDtT1nuf4oJDrE7RG0EMs8MsPabMfG0M9ypGWA5212DGp0wg0tDQ7FrNeZYhDohVFvvqjbQFBLdWkOmjWPuKhQUV3RcGeqwv8Z7nP8skwhCrRpe-3t3h192WUnUKeDRm12MLRPFcmykAyjtafgEsJda4Hj46dBDS_55Yjnc0h_RjaFOjE_iKq1KtMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26806">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBIEBOR0qy4ny9MvDcJe2F2fJhoK02bLWjlRIt87zslVjeG37G9owh3RAnKb-aL8hNlz1S9CfmSANJoJui7Uvqnt7r7VD-GGCp1r-BKixDM0I-m06Ehr1nwlxH6UqN93HPaah2--7Qc1jnl8LyP9Vt57Vdhp6O5BbO0EztkZ7Ty-BUZlFivilPbjkQ8-EYrJK6hGhS4VpFvsz7zHgIia8w5S-umIfJXQ8lNi0T6dGCt3w-Wv3asde2hHpE7aHeU_XvXM-qP-CBicaoCle-BYqB1safCKGSLTrOQPwlMavYePCfW3SvZysCImo_b8zDErLL0Q07rCWXyhSkw7Y7BFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
💵
اینجامیتونی‌روزانه‌درامد داشته‌باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26806" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0PrpqWZKu1mLPv3lxU6cAmAk9O6-LSyNpx_qKCs0V7hLogWJgR5JzUNKONW_1QnEnmYdGCWyHq4ZtXoHEDgqoVChDULTuwFKcK6HcrqMwQ5z9f89aTofE3_GYpCLNupQUJmN-8JC7e12VnSx_RNoHcmLO-GX49V3Q6wjYHu_ff4mFfH_MDNNwDB47c4Qexd5-EWixvmchKSG0FwMiNpXFrD-964EYClpnsK7D9uDkxqi-5fQ77Kdg4jIfS1M_nA-Moo0HxX63uoD4QU5l1wvyQS8wtpo6kD-YSPwqWnJpwPaw64LzhPKhVwQXLMw1UqyGkjG9h0LAMIrVBjGLkL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ple3gSemwVfU3UjSdgxS4UvTAm48R8c54wThlXKU-GM_wa5MrnKlQbyPjM8g68jKO3OLRC0x8tijFxze_sfomRnBEWG6SVM6MgiEmuB_z-sJbNnwiGZ8c99KMDJt5xjFnK2N3LisUSVLWJS8YIc53HPGBAoqwAV6NJNhn5C5qDF29IVN0f3W1whD4Ks_dWRw0JIxbjCQ0keTAFi0Y7AIBtnEdK3A23EHiO9ptk71R9Lwu7lfzLj1mYdbsSEdWqk1ELqQ1eDoNgHn6TqKsoEHHtTWRa3OZ8dhKmnRgh9UxWqz57oOnRMLD8NYFWCoMXBRsjEX-ItJhGzl-IsBCUgLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN4XLSHvtvBLsXKH8UCu2yhZvaggDImoB3mDvmvLc2TjQ52HdlK6jNHBc3NYqycm9bVS0szv4Xm8B2Fj1k-1Jw0CWoGfJyK3-2Zi5b8WmMmO5YC5VX9naIFYXI3Xg8C_aOb1RzyLMgEu51Tq98fV1ydRcgqnepcvALwuoX2XtJ5MNsFdlySi8nPROIN5XIYnxaPZZEL4Y-s7y7Kd6JBfAcMbZBwRuh0Cz9zPVgjMf4K1pzo0uDb3DL6wj1jmii-TasdRm1thkKylS2w25IaBrH3BIEc2araDnws8z7c0ra9KeFrNtwK-gh2CVCDctWhyPCAUQ_V7ogYKhyrOFD2Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QskX52oZLzwBnYf65er7ITRZBm4ZP3-m8ZkWR127g81tmE_DxN8fstunF8Y8UIah8PRzSF52AJwKmov-8VO-UTWybxv2kuoe9aF5-L_3K8FZ022NSHYlaUgLk6bJ0ynO2eXxAoPaUZmk9WeXu_oncpfO-yfubeON0FJPTT_BKYSe0ZegADF0D4dPFDPKhVrgdu-8A6AGYcOMtIgsa9rqbsLAxGz8AOwcmw5hZNOvP_Zb7Q7d3xpVy7EMz6vrM5PCHlNDX_86KiPCTV7pQqKVHTol6fYbriUKJDDHxHBViYV5n21SWBXdeonZFyZseJSJe49KL_fyx0fOrxzz68H2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoZi6PF7VZJWzMFzkZKh1qn9FsssHnQ2Bqxhs04kqfD6nFywy--emJ3MFsuRAW4DV_8ARMPuXnRZ4npC7-tSqQWWL9OINw6-28wPVUb7HOB3cFyAHAhZEkOV8xidQ8m9EjoYvugoFeMsOQh0Qhe9rbf432EhQR5fIywhNsQwSRG3mfA5j0Ef7VmN_m6DlwsGYPimajwzJWoDhJMDJReUf_-j8AlXJeK1PNd7sXKr00QxmKAFWAEujgJ9lxuRwgtkayB1rTH5etuDayOD2JLEuM5-BAgDvPhW9Qz2ye3hTeCtRcZ-CzXixNM1HqCetFfMyDEJgwNzl53hFCbTL5zVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UikECKDFSrKlAb3urrHBCyT5tFNVx29R-tDqJ2lr-vgT1e4rDf09UWIzG99YRKVPD--hF7NZ7_r7DVO0kaG_Do-RJ842LTY6jRiEMlsqnn_3p4AFREQg1Z4Q5WFt9uG23j_HUtmqz7jwvpM-gMbf7Obkr1GK6jCF9jAcCORAggfW1zYxIab4qhZD2cW18PKtxHNO4HakPrYJtfBvvRVZRnVQ9KJ0PyQNsfHcfY0zqPEyXXoKJcOYsh7Q3zmiIBTmAtLfayRicuH1-PpxFRFMqo3wGP2MyAijWrV8Mw8O4XT7SUsO7IZQLQ7eqiR6hgkOfB9NeyX6350BN3gdKWJsmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqXzCkLIMtXGKhY1O97RiCxHAooruwT1CcydwUKIGR7c4kzrrBavHDWbMtLLTzR2tzxQdWMZ0fWuHxP0y0pGK4coEfeeeO3F1aCMUvC-FIPU0-urBOZvPgulxdWVdxrv-hOSWdXYXEz2C_FoqTYBNn8dz5HVZuPH24nYC_WfPaa3XurURkApQHkOmC2a4efCI2NvJISFrd8anb1Mnx9VWdxYixmCeSrpPcfgHeVCgqmBiohzf2NF5xFxBhZSshqxXWWGYpIUntpXAqnzl1kT-xpGkIHn4BOEuhtryABfgPR7BPMWm6hrUQO7HQLFKMO4Xm-WswM-y4ZU7LvCDYmXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZKLAlL-ExMUGqoAsMb5D-v1kRt4HxjhzSKljxcWCJZXjRFCBhlm2gqXHzfRlpwPVv6GohTe9mIG33ONT4D0gtlkaNQSs3EIn3ltzS58iQLY3vLb5oul18wZ9f2Bkh0KJ6Yv0OmOVV2raLhkcBhMFWjKuBQLarQsfQbeFTstkAqXsvk_BFv3Q-Y-Unhvl6LgBD5ikwuyXgBlPTs9nV1g_6LiJFaoM9xiOWpy2FPDr2dZvhfktSZrpmHtfaQ4UQ1NkvHlcAADss3my_qyyDIbNPUmHAFRxs8lEm3-DQDIZfgJcNY-ejKCmQR3AqMD0POElobLEcDL2zEM5E9cnso4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4HoJ6m5_qruuKxpO3Lnp1nyXDdFHOqijscSsCV1Z3cIJ_cO8Wyy2AQs7WmN4CHgcdcuCmTJWOSE1kLEQ-mHse6bdEttgohjXYmEOQ7O36WRDcpraF-K7rA3BioLgd_7DeKZNdz5phiBR33Bfp7QMOGc2JUHhdQ9tDEveP5oiY9ZefyOSJXr5wKzYYf14f2z_qo3NDshZnBAbiyFGwb8sVdK-n9u2WQn551aQOIlmBflamwosMULxmbT_feZL6gI0LxEWHaG3fsVXL0809h9hlqv167D_eZI-J7lbcWkgjDXIrJwJJeaeJJVRRSDXZgAiPLDGNM5e1O_OA7Dg099Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wie6JgANgoom_Avx6vLpS7p1oZ3mO80-tZKsFuHPjHewAKJa-do4LufBgpbrbsA5sNkmONJiWSsUgXkoQpQfEH8G9ZyjZ1xgssGcHLKtp3mmIO7lfmVPDQWECpVCETddFxIiSaNokaZ3I5I0tc1PcCqyJ14MM0J1clnpcmbZjTIggne1rg5XmjugCNX0QchUVY6Ev2gaoZ6K0edn7y2K-g0QBX-dNfLX1ayOEq7ecrofYmwh_IcO62T5nOded7QoieaeBX6qrQh0XQcH-oLq5dQDXQFd37q3iG1jrBnJ8yidc3EVmZ6tDTkM_H5MwCXBmmdjgzwsHWs5RA7mJwYy5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GswMRoobA8GYonPTH4oHbCoe6yezwLNzbhfFqwXfX87e1xwTNJ9ZppJBVNez2v8kMCmuvOJ4hxfA8QLz7AeUS4HzY9baqZch7YGGHUuRtMlwojURWya-4ahPILku56Rqy-ch-Qza6jIZLE-xc9PvSxlNb6KlMBlynb2EiVXnkUEkj4lsNK7wwG7jeUCzijdfGuX7T0EwkyYa50dsCHstLSN7EyYRL70aUd4v4mIgOYihDxLr8bhpLwK9BhOeCv-OgJQaiGLTgOEbUa7ZgV8TY4VGAQYqVihgYYpxZIth1e-g1tM_a_360iqpjH1asF-S3MWIyQvFcuEI8BQ9btD0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJmTNGFdA9fpcR1jWhaSfqZnSfHboihMhmR6TcmxB01FPHTyIM7yD7Y85Fqx8e5yHYFaOSlGUWnBSrUy_OYA4adXdoBA0RIZGt3gIA1uXnfivcfW0ZEiuj6rO_D78p27JWtsNiAF0js-ELF8Kr8extCa8ITjwZcJ4Sd8W0XAB84UA2EqJFXxSKlYGH8toeoFJKCDGiNaeAVQmnSGMmlN87CcZz4aMKBsvH2rbdxtlN-XhZw3KAMSI7JHoyluBrV0jt5KJil9yZuzMhIitou46ApVk3nEvdTY_IdjZ6v3bSFj57q5kA7Arw06NNq6iUaWKCXWBBHqSFAx_UnSx2fPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=gePQE_qf8ZweeGu982E9tMqPzHepC2gC42D7Lu0d6wZEhUFYo8IczFjQHNF7_A3UgLjb5jY4NcZ63FBJFfWeEft2MO5qxTU2VVyy410s8ukJCUi9l1WzCYtOZ6F_ex9qppikCTzcxxqRAMAYWhoeRMkUELXZXn_tFDQ39_zsjfrrPWX47fTh7wdXF0ds2sWbhpRE7-z5fmxX1Afo6HPfLoWCJ6ra1t21qMErayW2aXKi3l7YN9PqYmapxssBrl_21CVQHJTrb-h6XBcjPKbagvvEUddOjyoQrgGsczJUBQcndu4vL3tjzWapvRrd0NPAfyT7zMTQLvGuJ9hFEKXMCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=gePQE_qf8ZweeGu982E9tMqPzHepC2gC42D7Lu0d6wZEhUFYo8IczFjQHNF7_A3UgLjb5jY4NcZ63FBJFfWeEft2MO5qxTU2VVyy410s8ukJCUi9l1WzCYtOZ6F_ex9qppikCTzcxxqRAMAYWhoeRMkUELXZXn_tFDQ39_zsjfrrPWX47fTh7wdXF0ds2sWbhpRE7-z5fmxX1Afo6HPfLoWCJ6ra1t21qMErayW2aXKi3l7YN9PqYmapxssBrl_21CVQHJTrb-h6XBcjPKbagvvEUddOjyoQrgGsczJUBQcndu4vL3tjzWapvRrd0NPAfyT7zMTQLvGuJ9hFEKXMCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=FPncaE5ZiZpgff7CzTL3xJEcbxG2HeSlEQEG7IzrfXgYKajDvF-XnzcW7fYHmsXt2EOD9Gty7VSbDpGhkBULTmlT9lzmTmNeMEdY3IgVeR2DMntL-ZjuNIMw3QwSavSCk96bPTwU8XDM-Fnl2pwrCFa3E-1JTArEHtconjm9Pj9YTsrj7j_NwfvrCz_WQeuYjRff3s6_yDmS-uLmetMINzyWapNbZJxzxe_QmuTy_0Ti5P2IaYQN7IoUdswyTCpJbVwS24UTMcILZhKm-XtwysWUy5aZTz-H8MZVFBpugrpD5H4d0TFEaJJrWzJOmQ6tFUg5SsGyvZBMK8p6lXdy-SEuZNop1Z5o1aLf_yu4AQ-8bQHQ-WXJnVJKx760gytELkvnDJVEOJOIGK9Non3xFy9obioi2xw5OgnQPwoC1FfXPUW6C88nfvzuS6OeyOqJ2NY21BwfEw-ZMEhlHcjp2zQ4q6vAleEnG6sfevwYJ5IPDSzrW3FcJZSb9t94E9K4SH7rJ5lcSR6K8CuHBgZpW3_bJyjLI-g3NX_dVtt5ffPvRYVW1EUi9W31NIBUsy8MCm3_cF8nqBZ-DAijp8lphTV8pgtLy6fiuohybm1i95tO2Sbp88pbBHoQqN1OGnwK1l_xkd_c_mSRC7k5R5bpWO3UHwbdqseJ-y3aWUmeipE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=FPncaE5ZiZpgff7CzTL3xJEcbxG2HeSlEQEG7IzrfXgYKajDvF-XnzcW7fYHmsXt2EOD9Gty7VSbDpGhkBULTmlT9lzmTmNeMEdY3IgVeR2DMntL-ZjuNIMw3QwSavSCk96bPTwU8XDM-Fnl2pwrCFa3E-1JTArEHtconjm9Pj9YTsrj7j_NwfvrCz_WQeuYjRff3s6_yDmS-uLmetMINzyWapNbZJxzxe_QmuTy_0Ti5P2IaYQN7IoUdswyTCpJbVwS24UTMcILZhKm-XtwysWUy5aZTz-H8MZVFBpugrpD5H4d0TFEaJJrWzJOmQ6tFUg5SsGyvZBMK8p6lXdy-SEuZNop1Z5o1aLf_yu4AQ-8bQHQ-WXJnVJKx760gytELkvnDJVEOJOIGK9Non3xFy9obioi2xw5OgnQPwoC1FfXPUW6C88nfvzuS6OeyOqJ2NY21BwfEw-ZMEhlHcjp2zQ4q6vAleEnG6sfevwYJ5IPDSzrW3FcJZSb9t94E9K4SH7rJ5lcSR6K8CuHBgZpW3_bJyjLI-g3NX_dVtt5ffPvRYVW1EUi9W31NIBUsy8MCm3_cF8nqBZ-DAijp8lphTV8pgtLy6fiuohybm1i95tO2Sbp88pbBHoQqN1OGnwK1l_xkd_c_mSRC7k5R5bpWO3UHwbdqseJ-y3aWUmeipE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCEBi82EsFbSuFtf3R8XgT9xNhLbi6DiVHK-yMIoHBoEem3hF6-57vTOfNyjAgQjTWlllzgxmBbnNBd8_eTfsNMlI9jCrtGPKfVcbNT3M1uLDK4iVkdk2s8tV0AFMrDp42TfOay1RwsmAVT5HQcTaQCayOmeJT_bFzeC1bze_ieWEOfTFu46duOfD6QasELwBMZca--KIge_NXxawvOgrN8oxM1clU32kuZ3K-YO-Yi-4n15faSmtp-iRSaYSD6_fzoPIODTcj3PT7ayn9BF7HvjdAUj_z97_HSvunb5KqG3BAjTujkb-9250lnsnyaeJLGlD5qlaN8LGcu9gcP7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCAVNXq44lXYW1xkSPpsKB4vJc7LunZxh1AgUb2FNcvSLYMaB6JA-8GI8sg-JY2wG2GfUnoQyxOazRl5_r3hvz-GTBxxXj1VZmN5KhPrtvXIkuCBwl6aAGCGhyAm8PhNOQj_zkkixromDmXCMJlcqMrqdhazRrsfyD7ayG5nWBNYqVum1yvIYXyxbY8Y8NlH5OACKePJSNBvicVjKDDCXyzaXiiTbfyNtGfGxIC7xam7RtNRP-BoQf-EOk6S2MyV-M58QyLPS4wNdE5xD-3PxBsHudhXFORFVhp7RkpRcF93m62WMIKrnvRrBfnos8RknQ9z5CtEGTcdFMdPH0vBeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRiwNbnqrMtYbivsThjtJbOJ1QxWLeXKTfip92c2993PrhDU01FVX97BzxIqkM4fNF5oRpU-YfgS8E4KgilEcKXw3zwqxePX-pC4BkWZby6C4KFWE8vPnEvI21UEWjNbBtIZ2mAynU2EYk0kmCw6wD69bvkHU3x9RzBZs-BSVWrzi1fEsngZ5y69CeB4ejP69E0FIU68lfJDY1tUOL3dZ0IEwsdGbKZA8N7UFlbCZSMxw2wIjPOYyRngqSV9Di8GcjD5EsfRVcjhncsp9bqONyW4AVu13H_UpDEjW4vmGrB5B0emBidEJsybQYdRBJQtPeyESDcqyOiBemf6SOGGwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJpsZujNIgQ0ZYSEHikNsmwgIImlwK83JZpPdQ26nGa_kdOUwSXOvHDp9NjOpg_Ld-7xaQ5Qp-bOUS3YT0bkzMuJvSzpFls-4L21FjOj2BTeyoWMC1sUNDvz4yIrTEEez0vi6eZpwTd86abuNDutlZgsnQ3dx-TAFAP7cDhn5vJES2vgPhCjZLrwL526qzZMWXuJ92FHv8qthoaA7Vm32E_5SpAaY4ZGNFHz-Lshi_g-pJRZCfYzX2Mu6akuU9lTrlFTdMonmXNVxfb8qTua9gRzS2h44vdWP5vh0mbmAUraVrc167zu4jtxPdD8prdUDWoChXUKSIyzc-CZBI0m2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHTFLtXsmwf7SixgxnfNKhyuvpIpLNFnmWiXoq8asJVflM5M-fHXFGYq1F0I8Rb1xe_9lv3OpeGHshgw4qzvr8cw_nLM6hHsd0rtBCaRngf3qrHhnZX2hXLt5GYYK5Q-xMLBJTRRT405LhX3oATrWNDe2XYi9XhYZCZyTHBUjDR0AcG07A2u19inPybFxVaaLGBVu-diH9o-XuJAJ5QSZF64rYf3BAstxV00TACRLDnh4rXkrwvtS_T4ujHHdCY8KDef7BsT9QgdoGBmjB4V7FLKnEH6mCmIFPxNWluQurnXhFXyECPnYruURow381kxdVdZFDOX3BAlE1vMLzm9dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c98UY2snqUoiF2rai5PlmaVNtQFwcO9tRpJkXMxL6kGhSqIUFP5u0D8VVPU9xR_UrWlX4r6MFHV1fgbx34NGObv-JKBACiaaDwZ2BhdAde1P1w6-XEFqHfGtJED8jHpStzuZyf0ik0eC9RmE6efIDTClTFpBu-mcS1s3R9sFJdyBknrmzwnTdVdMp5lRERjmk899Boh63QakuIO4g756C8tWCuw87Wo3eSZcATMr6tvTJBPAQOJj_6gSsgcZJvagJm16goUgC8CLw0FdzGPfBVSO5vntMq4NBRNEu7IDK_usbQqsrwjMJ_54CPGwamDdSJyXg6kAfcK0Wq41-ZnR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=E5s4lnI-5LDs7xSEsMQujZ0eTciV3-u2w27mL6j7DZTW3-_SOj0rMnl71k7-Iu8sPTm_MWwPoDcKHxoI4XgBsZPKQedHFcWMO7ghY7lY0nRYJJKXunA6jcDJAJQcmBgoa_lcqFr-75n8Kfw1QaNDK182ua752tt1spmLYclOlxOH0sFr8_WhxVwAtn_DbfKJXQne-HQJxTtSVtwkEKDqEnQ54uRZNxHUQA_0k4q0rPQk1akzcnbA_dDEOf64RA2HkZJmQ9QJyD31WjjQ6RvlhXwyI3RBhEi2hxUhFtcrAgi2AKqFlZLcJkoW_o9ca1QfOy51Xs1TS_vAOmzbgNPhlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=E5s4lnI-5LDs7xSEsMQujZ0eTciV3-u2w27mL6j7DZTW3-_SOj0rMnl71k7-Iu8sPTm_MWwPoDcKHxoI4XgBsZPKQedHFcWMO7ghY7lY0nRYJJKXunA6jcDJAJQcmBgoa_lcqFr-75n8Kfw1QaNDK182ua752tt1spmLYclOlxOH0sFr8_WhxVwAtn_DbfKJXQne-HQJxTtSVtwkEKDqEnQ54uRZNxHUQA_0k4q0rPQk1akzcnbA_dDEOf64RA2HkZJmQ9QJyD31WjjQ6RvlhXwyI3RBhEi2hxUhFtcrAgi2AKqFlZLcJkoW_o9ca1QfOy51Xs1TS_vAOmzbgNPhlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=gKtgSj84iMl6Vtp8Ui31oT4PVpULAdsv0ZsXJ7rstbqEEL0ph3TafH0znSbPjHCIq2s8u3_2LDWY7kFe5w3fmJPn5J2l8E-cQLbBLG5KcRWijsd0paNrU9UaDw5tH0YY2Lb1C28HjT1WJJFXTIDXAmnWpujbt9Rk3lvKUe_hG3h8B6iF83UbxBX5-mC1LNu9Q5P3GV9ZTxp3VY43nCtS5O8HxufjnbEcmU5QmIJU6MM9GfHL9JxvxcJR14GvtAaoG5vClotcKIB5IGrNgRS9bj5GFvlP2ZMMTEU2zqrwH-_1UEIfcj4nOcTdMz-wsOmM7yqfZ_Eu6oSyVzLYpyRNmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=gKtgSj84iMl6Vtp8Ui31oT4PVpULAdsv0ZsXJ7rstbqEEL0ph3TafH0znSbPjHCIq2s8u3_2LDWY7kFe5w3fmJPn5J2l8E-cQLbBLG5KcRWijsd0paNrU9UaDw5tH0YY2Lb1C28HjT1WJJFXTIDXAmnWpujbt9Rk3lvKUe_hG3h8B6iF83UbxBX5-mC1LNu9Q5P3GV9ZTxp3VY43nCtS5O8HxufjnbEcmU5QmIJU6MM9GfHL9JxvxcJR14GvtAaoG5vClotcKIB5IGrNgRS9bj5GFvlP2ZMMTEU2zqrwH-_1UEIfcj4nOcTdMz-wsOmM7yqfZ_Eu6oSyVzLYpyRNmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0SAGsewqwkJ_B5AnIRLOI9fsuTZvcIOGFSym8R2a8kNXGZwM_oaagAqhPnzhP-hJngOWcfxlLVlJvQGMZ1NMVlHlMxS-TAhsrJE8VKng50DLyMTTj6FEEFSRWttRdZlNF0vEFijKmacf4HPgB78zGWYPi1CjAeL2zyXswbynnfQdCA6IOVMGqIJEGZTKNk96oC7f1xKJDW1YVoRgyaRR-JX9qOWly78Oz-k83i88f4TqOqYiEKB8Mff5vlW_hFkjAeBshbuauAgguP8JEE592xUduqMPkA1thzkEZFsuF7h4dfGpgCi1lYLmyDGlO1gXDzg3atLGe3IpqHEN5uJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wn03D2wPfjrriR_P4XrSly8TifPmXSncDeZ-ul1L_FHLj0EU_4785Nj12Yw-RHtuBz9D36Zu8wUVNCuSIGEQiYp7wIx1UVfZ3HFaV781zQ77hrSYX5NJ32WHnPpufWOeGFr9k-HSnd3YivycTrYvMITGOUnOMh9Ex-9x-_kLEIvJjmHde-XkcAHaPK6-OQR7xTUsJ_XnzdY0RAEbX1FyIkSAzU7Cr0MT8CokG0B_u6by6qpYZTeVjWJNtG1AskjT0vuNDkI-3CJizCHTBUN0PYShCezI3CZeEsIMGoHOqr8z_Ouroc0RI-1yDjGXgBxFavDMUdS0i0pSLGFgglHiRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=uRdp6W8W7z2kSOeQ3gioLuVxtwl4N2J1ja2XKYVG5dX1eXyBoZkRC8nMVZdpHWySowZ9ajh_YsnhVjAdYjb09EqcB77FMfjDJ3xPK17gRLhLwY14VUbOn2Bv-O8fTJX3Lm-7KDOMmWf433dndu1_pQxHkUOK3PnyiQ4bkQuESx3p3lU0LCugNTHDhuVjHMhVBf-GX0sSxvzrCl-pNgsX4Ko79Jho-XbiX6lm28zZgPUzHvRPj9TwdtSgfTUgBTB7mSTzQewZelN6U6pCXEhz7DITtQKHNDNcuoY-QW9aBcuJ_30OCbmtVNZOvo6h6t2wdB-j6pOcMpZx7_y1njJ8hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=uRdp6W8W7z2kSOeQ3gioLuVxtwl4N2J1ja2XKYVG5dX1eXyBoZkRC8nMVZdpHWySowZ9ajh_YsnhVjAdYjb09EqcB77FMfjDJ3xPK17gRLhLwY14VUbOn2Bv-O8fTJX3Lm-7KDOMmWf433dndu1_pQxHkUOK3PnyiQ4bkQuESx3p3lU0LCugNTHDhuVjHMhVBf-GX0sSxvzrCl-pNgsX4Ko79Jho-XbiX6lm28zZgPUzHvRPj9TwdtSgfTUgBTB7mSTzQewZelN6U6pCXEhz7DITtQKHNDNcuoY-QW9aBcuJ_30OCbmtVNZOvo6h6t2wdB-j6pOcMpZx7_y1njJ8hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GL_2fQfwJ8YC_vHTuCyMZYUiqzcofs1NTntGqvKZhCX0g8oWkt6xgPPKgdMi96rnlZqP0VhnLPa_h9L1zuBD-YGfixSS0IIK9uYJBeuQjmm79hJVZcxH48wsZGtyVUkNhqVgLQ76CbQLsjPn2s5F_jW6TXHvQwp6hiOCLrOXxcTw00LeTUugNoALgG0PEkPieLca0EB9xyUOo2IEwrkPNTGzl-S1gyDgH8oD11ltu-Z54xLvOdHfjP0U8ObOKTycDGn7HghD2bc_dvcPkcXhoVV4HjIBH1QNDYNgGfkg6w0T95pt7ORU2onf2Cb5KCne5KTOuU4lKdH8dhVIutVZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehXIT2p5hRIb2UBodb9u1mz-TYJBPvcpl-fiYsxB9AZ7Jo8QgVbvLYR6vH0lZm8nPe6VRVYg7-kf6laRDZlCqapmQR9qMF4Bl7mHtEztIETIZuPNRvNXx1IkXJ0-m84bLSfsCncK4L_tEcJbRwpdzlz1_IEgU7YYvOoRG_iDd9l92CDm0wjz3pULsU5yDZIEkEC_s4raQWwzJBTt4jp9-UDd11xGHaIFtXLYDgro9FW8DDpL1DEDvVExQZdJxD4H_YdrFXnMUH3AVGUGjBTsJGdlEYJ0sO-3FMO_EP-DCkvhNfRv_RpqkxSdLApCEfrthoE7wlj9misoz9SAbHYiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=pChvTN7lx_rVjtpAomZ-OIL4_9nyAOoA2mFi2f34BjCbOAbI-wmu_dQ19jDYiipJIixWBhLqUkGPVkKCq1sX7gvbqyzzOZAS0zoPHl5dMZufanWkGhjABOGbN9TdAVUhHS1UKvbRFMAlwaplI8Eac_Q5j4zzy3hf0Ui2zMmlEUwbeApFw5b1dF2pGCrXRo-DgIvzD_f7xAfxeXYz7iexUSAJS_pjU7xEfZnT3eJT-hE3rJdHKnOMVF3VaZfEMWAPdQnteSTmjkMR-cIqn-NMX1OXz6rfoY5G-17vN-YVKDWb7TfvyN8Re1nJNBKZgICWr_r30QPxeZ4EsasUOeyLbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=pChvTN7lx_rVjtpAomZ-OIL4_9nyAOoA2mFi2f34BjCbOAbI-wmu_dQ19jDYiipJIixWBhLqUkGPVkKCq1sX7gvbqyzzOZAS0zoPHl5dMZufanWkGhjABOGbN9TdAVUhHS1UKvbRFMAlwaplI8Eac_Q5j4zzy3hf0Ui2zMmlEUwbeApFw5b1dF2pGCrXRo-DgIvzD_f7xAfxeXYz7iexUSAJS_pjU7xEfZnT3eJT-hE3rJdHKnOMVF3VaZfEMWAPdQnteSTmjkMR-cIqn-NMX1OXz6rfoY5G-17vN-YVKDWb7TfvyN8Re1nJNBKZgICWr_r30QPxeZ4EsasUOeyLbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0f0EAc8xB0gF4Ww6p5AVwGsO2biFQ38HFzPGoee9TENmhF8Uno-RNGvVWGY7WLjvE67z4F-Sw7u62jsDyt5rJ2_4OLmvo3NruvaCYT86P4P80KiP-n6V7wCCx3JzRyBCwQzyDKH-5T-P6_EdYLIAR3dzNCGeQ3Z9s5Xqlin3CCTYIbtI1LNgQX18QIvXcuuo37Yno5RgvWh6pEOcv6HMrlezKPHKUfVtQmp1_tO_8OGC4sSzMhf_sVK7M7dCG8Vr35dwviYkqNTIs2PhIF6wlag1C1Uiah3hgT2rQ-iMzuIK_laIWbtXfDF_2RhEEVduBSgk5ICZKFFPYQ9efj1nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfdUtkSUYlHMQn_LyyAXoNL7o953KoUfcocozmgkWGrOw6EJW-T4Z2aWLoa8K7YcureCP-935HeRv7YUNQH_FecWCXR8knFr16fpU5HXc8Of5Qx_qfKdEOH78DB7HlMZBkuAReqQ5qi7ZS80mgfCzYHDeDaV6UkypE5DC2uEZV11wbkIx6CBlgjV8QzdJl98pcMI12Iod2YEqdItKM6WKmGBz_uuJDwFonc4LKVlmkqjbtCQEtn1MokiiHg78yvlIeXQskyCio0kXlrnP2xrC7XBOQEE7NQLVo1D3IOXtl5KbF0zuNbNFzFPmTnvF8X1Usg52Px53n0vRfLWkSZnzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=A3hcR1ESL1PhMuKCMZjmLXbakVMmtP172Ft8qTuKryfSflV3JzKdJpm0rEggj1o5YD9wPrXLPRBxLlYa_wubAemq-uuh1MhI8Is5SQPX4RcGJD6_vhwmbEeetL7nEjjfPgJzz3tfzYL6K6X3VB6nmFPRAcGsfZ0vkC340_HPVsb3n52mpGuWYi6uoUkz-ZMXV-vVOV4wIsQTEyi1ADJRZJX0pbZWsogQ5p02NofD4SuZ7wMaGI5alGPSohcmSu7JKyTffR2Y_D7XwBmf5Z-Ur8Zie90uqZh5fkSltbCGaKIuWevvAB2A5bA28wUk5swxZp2HldrdKCcxBUFXJUkITw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=A3hcR1ESL1PhMuKCMZjmLXbakVMmtP172Ft8qTuKryfSflV3JzKdJpm0rEggj1o5YD9wPrXLPRBxLlYa_wubAemq-uuh1MhI8Is5SQPX4RcGJD6_vhwmbEeetL7nEjjfPgJzz3tfzYL6K6X3VB6nmFPRAcGsfZ0vkC340_HPVsb3n52mpGuWYi6uoUkz-ZMXV-vVOV4wIsQTEyi1ADJRZJX0pbZWsogQ5p02NofD4SuZ7wMaGI5alGPSohcmSu7JKyTffR2Y_D7XwBmf5Z-Ur8Zie90uqZh5fkSltbCGaKIuWevvAB2A5bA28wUk5swxZp2HldrdKCcxBUFXJUkITw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYj019F3lDRUnhoT656rWbhR2Wg15feqtf2Qmsf2xMnIuL9P27EpldQz1TvMGHN1E96BYcraNq4ivoaQQ0Ks5KLiekAun2xo2D3EE5WO9jRu-Gl-UybVltwsVrKV5rp-oyxqRisQ7uJBE2_LUQPTYqBQxzKMdXhaTvBVGynOf04s3vYyBsdKFVMfyfykADuLq_hX0LcIXJbvf8NIS_0LBI19SRAvIc4690gTFiV5fzBz_bpheMoWPkRvQ3wQLFWn6nJhk4lRDfpdnyO3cDDsV_G3Pt-Indmegf9-B3pFFE-qR23J_TH9rgmuEFZsZOWo-ZSvkAbMePI6-KIRzuXa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtGVyVjOLjqDMV7MvZ1v0hzd0kyzK9vjCw7kc3oYJIIaKcHPjAB6l5UKYBEieYc2TY6s21bMMHqT09VI-rGd_2rDcrP8-dDaotF3f7XOHKe-QdjgTTWTE5lSoAgKc9JjCKqSCfyVBin_ZbMQQ8C_FLl8sQz1tytFMiMWj6Fda1Ju8_yinhbqHTPxqRlf_UvBBvfuJUv0rRUGf_imEm6AYj-Ri4VLBCjzc3YtXuNseNQ8hN4lwmmODLDXmziYcePeHUIw0HBZI0vILh8dfoxdg3gzzlljG42_3KzQIUwTstUN_1RSShBbHRyXG224LAblSHP1Gq7xr4F0Mctr1967qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6E6s-gJgfAyddAYhopBWkTCRvtzHEwXnT1-MaGpuqf3IS_JKOQxSj1hCWgXfcYnTkLhUfUXklyRSZM2MtworkexFudJaGCq42dS_5KSdBkhgRFsVnxER3c_q8mh5UBwcsJMomgrhrj9cIainqz2z092MPJmCIRA7Je7wW7Ge_4ch0ChqrykMsv5qXliQHaPFL1rJg5uHDKKL2ekHX94Brh5ZDFCQbI0eaeQ9aU45ntlMATIAVjYBHYBw9swc-oL4Yi-Id3BP1diyJ8EggjeaDUdmiwDSkegXELkJ4cwZNTadkcyIj97rzk313QyK5oky1cW_2rZRhcfo6-HZ-WT_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvuKjFKxky21iHf2JPC7Z76G5pqeyvv7_J3TjakrWv8mN9ucJbcLQbRkLDWB_5t8fS9MZNVoAU7rPMpQLWkYhntUUiz5UWKbKIr_swe7bHMjn4wVs9vjrgfTcF1audctwLRoeNOkRL-zV2SWUHw6gA4Xug7dZH-TfFQBnPEvQ1TzdbgY2tt1ry5EFlRg_wDSz5OC6-1LVkRGzAF_05J9hDBhV8-2WsFUvB7F6UW_xbdggKucNomAWtuDI2UqFeJEyMmdVqu_wVUROlLXHpLllX-m3nuWqbEYasBij9OyE-oV72596b4YYEcvWMw4xQxGVplYQIwCHaKzTwKKUl2DCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZVy3ueBqyRVjrP8wwvl8b_mmM33wL63L_QNrsu1Dlf6IosoKAk4BzShqKnuA-C_OrYKk_elzoq6r12YyycJkruyBH90Q8Mtol7sTNWds9dwQZfsi9b31GL1tVZU18mc8xNkB3AD51MAU_a_QRArFG6HNQrZ4bftxoLVCXgUVRwcMOIwICefgIkD3jouxX8YoNlOerckgAJnq9rImG6HT8XX635SNsIiekg0hojs1-J0Gx_H2T_k_QasfnBRYTNauIjoCcLQj3htJs1n5B-BCoCLlYJ5WcMHtBPiB5X8ISLEGes549vI7nYABr9vswULe__chjo56rnXku1AdkqfhBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSCh8fON_d82xr515xdfUTaMj4Bh4kyHXobSSYsf6sLcp9q9WrztNgUGdT77Yg4YvHq-bOwzOBgx4PeYoPeKeSogXKk2tfUS1yruHPffDgQhVSaaEeint-F2TUQA7wIABvQdEjHbgNAA1bDnNV68mNhaMydCEQsblJfUUjnU1LxHzReCsZRF_sVbDYHjUIQcylDYxXO2fD5KbugjNS0eKa4y9QknqNoVQlcsfU5jS-jdNy1pIzBkP_LffoEhgE_ACSv8K8zS93eCHmnAJ1DrzgaZK3nMlpO1Ce4_h9pDP8eQ5eLqd5F4XnQaNJsSNcRGh1MpwsXJYpQsAftb6tIJkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=D44FbNNJIrUEI4oRJ4aPP-AOI4yF04Ej1cmv8QHwAv8vPlOb-Yd4D3MGDcaJe2afOpzYYG5VgVm25ju4vFXHjaIGtwqTfr2yOIRMOpmGpNoZub3wtlmCtvoTfSMiMKaU1DbeJVFrNfsaruNP_9mOAPeqHs16g-782XMxllZYOTXCjyq7aXij3bpJFAmvt6XqQlozq7n2UC-7-njBaJ4vfXhYpUojaLZCeCx5FPvFxMZgznkyfgT_89ymuk5zNWvCJ-Knlbi3p-L3P_T_Ckcozf0rxDrmUcRo9X_rxwuyTXXihFcqio8TP0Cc1792Pl0bTAHOYX362UzJB7vLRG6PEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=D44FbNNJIrUEI4oRJ4aPP-AOI4yF04Ej1cmv8QHwAv8vPlOb-Yd4D3MGDcaJe2afOpzYYG5VgVm25ju4vFXHjaIGtwqTfr2yOIRMOpmGpNoZub3wtlmCtvoTfSMiMKaU1DbeJVFrNfsaruNP_9mOAPeqHs16g-782XMxllZYOTXCjyq7aXij3bpJFAmvt6XqQlozq7n2UC-7-njBaJ4vfXhYpUojaLZCeCx5FPvFxMZgznkyfgT_89ymuk5zNWvCJ-Knlbi3p-L3P_T_Ckcozf0rxDrmUcRo9X_rxwuyTXXihFcqio8TP0Cc1792Pl0bTAHOYX362UzJB7vLRG6PEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR_2wjZ9yj2jSfMm7RkGSzpbMlXNICwVdZxn5ZroTZeqt8x1X7OXQsYHDeWOGW7OAkIMdWH53bqqmpvu8SJhAXfl3NE8DvohIPIpmE9-ND6a1AbvSYM7lxl1Irfq3sEotkLD5b52P-hN3HpF_w_uoizjBP3OVHSl5q0p1eoSoin8aDfjDk2JDAesamkFsJSirm5VIYKGVhAirRFOYkaZR6w4ma1sU481AIXwxz97tpuZ2pPuq15NjOT9sR8uQ2StVq-sy1u85UZCUAnG2TIyhgtAzDxqIuMnBljUHI8Ad8gqYsi9q7UUK95l4gpsU8YTEq6fGgpg53_OYFCLvAeB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZO7xQ_nbexEkBH6FGwdj0rQXMNWL77CENRVfjHCwfCBUaR0_OzSjjWpnmDnnx9c7KECz7ihb5aaixGMRPEotAQVPmLl2CzCcbKgKb_HJpW1dVn0sEd9zVfEHLBt30fnCfvxDUowUSY0dBlcHNIRpp5qEJkWFGvM7-P26WmT2miMHxpOMIgshsHv10TCLLyv5FmNiawtUkZFdlIGBesZeQ6fWxkzBjuyGwFEhFVQ_PhRikUZp5R1LzNOMSnxNRK8ej_b6Dmk79kFX98njLfBNcoutckmK9OOwhKCRQ9lmoNh-0LRsDF1B4731-YSZol4ob4lvbNv3ESssbBQQ7ZY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=uAHjpXdk9eJj92Xm3GdtWgu9hA-cIYWVrpb6tsx-Lc576ZG6n78OSFpquSMZRuHhk0Aqk42XvXR0GDwy-gMjVpyqGyfWpd_7PkCo4SSNyLQjceETXDJm8Fak5z4qbXRMhrPl7ITZYHi5CcqL9r0re-Yp9ljMqsgFZxpg38tH3ceAcVxuGjyhXpN6Gulz7mQXTyX7qWQN8QCHRXEkxeBttfVyHvICjfzJtCyCcz-9kLty-BnBODC3rXhezWcwcF6abm0-e2oomtr7QlWhgUNPVNrISD9q0va-CxLRaDEaNBachirPPwBqpA4z2L-klGvYVnuZuYbWXEGkO0wYn73LxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=uAHjpXdk9eJj92Xm3GdtWgu9hA-cIYWVrpb6tsx-Lc576ZG6n78OSFpquSMZRuHhk0Aqk42XvXR0GDwy-gMjVpyqGyfWpd_7PkCo4SSNyLQjceETXDJm8Fak5z4qbXRMhrPl7ITZYHi5CcqL9r0re-Yp9ljMqsgFZxpg38tH3ceAcVxuGjyhXpN6Gulz7mQXTyX7qWQN8QCHRXEkxeBttfVyHvICjfzJtCyCcz-9kLty-BnBODC3rXhezWcwcF6abm0-e2oomtr7QlWhgUNPVNrISD9q0va-CxLRaDEaNBachirPPwBqpA4z2L-klGvYVnuZuYbWXEGkO0wYn73LxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8jOk7_DeGHNpM4a8JQDcY9YULILokLhS4QxCD6QevlYzW2n7A3qXV3_4CV9_8517JH7nseiCM5dsZWPJYAJSG6XKrnnOpDk_IaKRvyG-7VFi0_MQk7OZ-P2QWIEq7_2Dd77xL83GjPe2RkFUoa2at4Se19Qo9NI1hN5VMxp5FWLhffB3yljdDyUnvhw0FXYX7o4qp8kCUlyBmJWvBD00y_goMv089O6nK53v8-B2c4Uybs6whjUr1hGRStaB43QV4XzJMdnZqXnXA804PsMwHY0lLBXt1cNInmAXqHEJtrxBPRqDg6Dm-PCCR4rON5BZleRkFskAiQzQxI2VFVYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFsDAyNApdn3wajzcH00SBwIM_YslZ0LS67VT5F6sj6QvH4uTyRGKyU0EH51kQr40llc1R6VTWXeqEw5dMia10tkgmQrpQEqvKyjzB4ONsNE_GjIOCh7AsnOoNnY1-CIsTpiTKZOiC3nRLy7roQrwDe3rzcOiliQmTOKq8neC9-qtMu3HS7I9C2Jt7ZmKWJarhiQzMyi_FLtZ6fau35xdoAv5wWf3at6qqf9-knYY2d_ZwBHGEk5ND-M47k1iB6bUGOjuK7MTnvwCWok622L6NTlxaVYu3WCxeJH9nz6VqceTxbaz57hCr9r_YQ4ktkHVQSLGGDlIbuXhFEPl7TKDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBielcCD3YnD1uJy7TXtxG0c1MRtENeRR4HyTqx2N4BJZA-lbJVStj8KFvQgUGIq7qpZPIkiSTO99uAz02d-SpZy70JJrWyktqGFQ5Fg_EIi7T6lMQFfgWksEa3efKikwxXSy04hJGrSxBf3zl93YG2ZVVk8XTZ5S1iO5scVnVtG8gi3i2CcFRluth3IVj6UZnI1hanaPtDoeEf51fe_mnDQ6h22m07exZwY8E-Sv_EkCE7qZJM-SlzgBfcDHZVEko2IYlgQJakBEutkNpQU5nnYaLWiPYBQ6eKBjOXCbZcg4apcQvEnVUCV8qrRl0PSRQN-97_munhHw5F5vBGfTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAfXevJx-LoivhsPtr-qs43vqsxXlMB7Q6eY4kJyEtt393r8D3KIJkgFmt7Yng-hG6b_hEfdvz0jBSNLvVbD9dFaTpjWHVQJ8FBNtHO5vrUuwi8dOdMJoLe21lFa04ezPEFbGDrniUFzd9j5jOgRfEieYwqF5Qgt_LfogsB1xAkuLfU3kHwqszxUr6KRPPkIRAtLH2DbODXuscBdYvqJqaYxiPYMn694qNIqv3iHxsGrVvp7F7Cfg7tR65p6w5ivQCIQwQiQZUNoFajmeNqk1-bwrRXSBO0Vklg7XVxcR9KMHFHlay0w650vvnpxyf9z9EUqXpz_OZJfuWDl_cDuzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLHw1-VNjYofJfmB7VAkPtpkX8jio-lTPh4cuagHGg9u9ehvPfWBc5KVBIUoydOcM6hn9nlZDTn3hMhcvFk9jpos7dZnARpE6t7tidtQEHQOpAhh2rfL4DsmUXGP9lmVg86Qj_ewas2k-b9F0n5QGZi63XFvFpfi-QmnrVuzX5E7MFY3YzHifPvNcV6MZFXaCudvbOzjLVvq9CoNizJSnzKq_RpDwbCuPo-Wn0s_zLIhWMSCCm-Myllzhr3hLHSvimEMeJx9p75--EX1I427Y4GjMAmrCLc5GjjFqwNSvlcZ8dhRdnw3mQgG_rJVxNQdbCH8RqvwoEzDfY_eRFEzGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=DY2KzUNtqW-U-O6N0ojJPBzLzEBCjmW-E5QYleXqAlClKTtkwjU4QxQXQAGQBQFN9rwg2qv_oVlqPii_EcttPcpIolS9HzyK_UfqMlG7ndLb50Jbj7QbCVNaBx80eBzzOQcDvsyaH5OdjgUWEoddyYRl7u6MrwQ9fsQtjrze5lIGk6tyLbnyyZ9y-0Xr2Zm2wSaK4gkQFgaoYUMo6lp67wK5UGRWWibLlf69zc5PnYdg6ka57VfCqj20xXT8ekJWC9zHEKzRaEUYV3QsVVJRnkOZ3g8k2RY2IPQUxpnTUxRt4d2T05u30ZQ67kPnH67Dp1p81tuYXcBIp4OuN7Byeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=DY2KzUNtqW-U-O6N0ojJPBzLzEBCjmW-E5QYleXqAlClKTtkwjU4QxQXQAGQBQFN9rwg2qv_oVlqPii_EcttPcpIolS9HzyK_UfqMlG7ndLb50Jbj7QbCVNaBx80eBzzOQcDvsyaH5OdjgUWEoddyYRl7u6MrwQ9fsQtjrze5lIGk6tyLbnyyZ9y-0Xr2Zm2wSaK4gkQFgaoYUMo6lp67wK5UGRWWibLlf69zc5PnYdg6ka57VfCqj20xXT8ekJWC9zHEKzRaEUYV3QsVVJRnkOZ3g8k2RY2IPQUxpnTUxRt4d2T05u30ZQ67kPnH67Dp1p81tuYXcBIp4OuN7Byeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPC7ZUcJ_S4XM0EBYv8ro7cdCnmON29Ck5FsqI5HTZ9-uTh18nMXx5kPXPLbOeLMFog6dg0Seig3ml9zVeRN6Q5zh-0V1TToLwzY-5YTrek8O9UjW_DZL6SL4jwNJNCH38nRj5tZTX9sJm_y9A65tsbghb1VcsRtfmUJ04dk9OY8KPIJkKs3YOgyZeeukkDQ45fNwGU_mHGpN7IRVjewdtQA4lWl4sJXomzG4VYlUF8WHBKOewt8ATaoijihARrr5k7cx112GdjhI_7qwme6sSEeO3oKyvtdlbqB2Wt7ar6ssUW4fznden_pr0UIU74uS26LtisXa9A1t-yx-IGVSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToHqfanVKn6zVXFW2SUMlwRThaPbABidnj2h2lBb0Klr1vIluL1obyrX8QxfW9zr9VJkT8F_tQY0hpxuZLNwafsXsHLZR4vHnzuk0VPppUu_43bEem7a3TFizsmyEAv9xdhdP4jR4EG209pteO9R8un-UdyVPZl1yyW4H1HKkvQgaFklk6tfgtiI10oh9aTTMPqHE1JGJScW0Z_ohQ0Y2nrSdKFR_Lq0QgrDKxv5VcXDBhfEtmA6L7xs1t85b9CkoNYHShXH1p1-nfsKxYkMa9nqEVTqxve-CytvVw13R7FyrqJE9Y8-iLI26BA6wFm_TRqlcJ5eW8ZfgV8hPArQIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=GPR_lba485x-HvZh-X3Z6fJBIDjhdjzDN2LCOeqPvKSK4mswYNif11ulSPdK5re0YMOukeBeTgaKYtEv8JbbXh4BqOFcG_ZBdP_gCXJZ-ERVuAewyWioJjcXmlYsbk9kl4JGGH11bi5fbcpIQ-DuTzrNUNxhwrFDL-y-UPpw2t5cFsWn6RybSP3FaWvNrXf4kPB3j_PlmUcyIGHcHBpEPANLOSPoj2YrfT60nEo1yciXPpfdKQwBJcr-WQLynFnbIhoHNKHPiJWJ6b1oE7cNKyZ5mnionYIPELKbSqAi3UOGCGcclzftosW8rTmzrq4e1IhZJepZjmge1D3iz1mj1qTjQjlXsyCe3MCWntn2jXFAv7vbvi2cCQltr6Y3F2Yb11X9CMx5gopo2jnxTs36IHTVDGtn74lYSEtRP_r17akNx5d1ouZNBGMH2Oc_taNKWbRYQuUTeCO-0zBT8GjS6o7I327oYByC-_0_78ox9XgQKRztDQ72g2GH-BdJgY-k5gXFonT0s7mr8LpsS5PhxYrgbSBocPEFNH7ddEt_MHvkqG3qD2EDe__mkNA_3hETotEb3n3DcQyU4LzUDtta-dtBWRuPuhHO6mCKKQVJHK1zmkniSJXknQkZCMYd8Lv72mziki0UV_iUWuRdXbjHDAfxqDOb0wy16I45N0DyDDU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=GPR_lba485x-HvZh-X3Z6fJBIDjhdjzDN2LCOeqPvKSK4mswYNif11ulSPdK5re0YMOukeBeTgaKYtEv8JbbXh4BqOFcG_ZBdP_gCXJZ-ERVuAewyWioJjcXmlYsbk9kl4JGGH11bi5fbcpIQ-DuTzrNUNxhwrFDL-y-UPpw2t5cFsWn6RybSP3FaWvNrXf4kPB3j_PlmUcyIGHcHBpEPANLOSPoj2YrfT60nEo1yciXPpfdKQwBJcr-WQLynFnbIhoHNKHPiJWJ6b1oE7cNKyZ5mnionYIPELKbSqAi3UOGCGcclzftosW8rTmzrq4e1IhZJepZjmge1D3iz1mj1qTjQjlXsyCe3MCWntn2jXFAv7vbvi2cCQltr6Y3F2Yb11X9CMx5gopo2jnxTs36IHTVDGtn74lYSEtRP_r17akNx5d1ouZNBGMH2Oc_taNKWbRYQuUTeCO-0zBT8GjS6o7I327oYByC-_0_78ox9XgQKRztDQ72g2GH-BdJgY-k5gXFonT0s7mr8LpsS5PhxYrgbSBocPEFNH7ddEt_MHvkqG3qD2EDe__mkNA_3hETotEb3n3DcQyU4LzUDtta-dtBWRuPuhHO6mCKKQVJHK1zmkniSJXknQkZCMYd8Lv72mziki0UV_iUWuRdXbjHDAfxqDOb0wy16I45N0DyDDU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ185AIDyu3BcATHSGe-C91m-87IbxlUNLXYqJ9OjMz32tDejLbtoFIBeW9gvoAOYacMJeeIvatDGa-Sq6U8hUwUec-6IzT1r3A3-wssbEmBCwzD9AJXVx80OZqaEKcK3WXvOSHElobUkxo99b2lS0-BKjP3-cQN27TdljgxntPNuhrOCG67DUcU58yvLpUMbSpnluGGh4B3xLp-AQ-L-mx29o3qXthusKSlhyUazXpkJRn2lt2qSFvMJ9Hg7TiHU1v_TMu2RozzUWaSfhtWm971LFH5Pd3pRawyotzfjG0jZMFqAs-rnZVuec6mkMogVyF30STvFLQ8Iklz6drHWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2Euq4JMkfUjoVKa6-bG8qCpvf-fwg6dJXuWP9ktGETIO2hVAKf77Me5QyqbXCx1ssNHeLAM2lvplh0rfUjEKUFsHavCxQrFAumIwr_AWSCyL2VCFRqYXQx7is86s2zZ0boMfbga4YI0r4Hu4JdKFKvBh2sEEvG-grPNBCYTVajR-hgZBzqJV74Nb1FQwnyergvTrGHJzE1BlDA_9an9X-iE4bKndiCYe94T8ZQy4aR6ARLa16-4rcA-xIt7zpffr4zqzKji6iGtPtqreIZ33d5VqBUa68n444mamtlbksImrekvYF-DdjTb7kEEmlrI8k-i86gRMiFo7DtdRfMbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=JynHIGfcmGTyIwDZNWa0WznJP-wLY2-4Iyn7Nt9Wr0rqNLvWyt-Wm9lNsQgHACNZpI5dGKWVuUZ56aEe39UMfZXQJtH4BmEyxcfufvcFgAJef25mBfJQ-FNHKhgHU7YWSHsoYmkPwrhl9rAYXCECDpE4oybwFVwqxp8ZoIRKsmlhYYuBzqi-anjTf2dM2nxws69JzC1RfdvRARQm-skvDeq5DGqPAg7k9TLUjRbFrcWLh0YYZGZ7vwo4ezBkoEFISfDkzpQZ0_r_7e-jAagrZQvfz_NZ1pe2fSvYPsL2KMuNzAVJkS745j1Yz_xUa7oW-NE2Jf_6NyRMW7UngQpghw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=JynHIGfcmGTyIwDZNWa0WznJP-wLY2-4Iyn7Nt9Wr0rqNLvWyt-Wm9lNsQgHACNZpI5dGKWVuUZ56aEe39UMfZXQJtH4BmEyxcfufvcFgAJef25mBfJQ-FNHKhgHU7YWSHsoYmkPwrhl9rAYXCECDpE4oybwFVwqxp8ZoIRKsmlhYYuBzqi-anjTf2dM2nxws69JzC1RfdvRARQm-skvDeq5DGqPAg7k9TLUjRbFrcWLh0YYZGZ7vwo4ezBkoEFISfDkzpQZ0_r_7e-jAagrZQvfz_NZ1pe2fSvYPsL2KMuNzAVJkS745j1Yz_xUa7oW-NE2Jf_6NyRMW7UngQpghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=LGSK1fuxDz6LeofakEM9Ouw0T93VpkGfAK_F728LvYValvqy1fmmVKZaYT-0exurBgjOHuKJ1euIYqrOVjxagUJaS66QXc2--3QrlkXvaCRsfKmEoPuKIf9bD-7LCaZTaOuMzapKP7alsPvk8lh_iVK6Jjuy0M86tVtTRzb7-cQOg4e9LTIGhHhOLom30O20cJus9k-2v7W4ZMCi4XXAmFO_mpgZcy1nGvJEzCggdSznebi1-Mze9Dc2uV6txvx76YQitVyPrC6ch91y5YrEhhalwmOqrDumxyP7HziqKjpy9jRhGXrm5GZi_HdD5grpkQkSI5DoyZyJojwsMOYE1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=LGSK1fuxDz6LeofakEM9Ouw0T93VpkGfAK_F728LvYValvqy1fmmVKZaYT-0exurBgjOHuKJ1euIYqrOVjxagUJaS66QXc2--3QrlkXvaCRsfKmEoPuKIf9bD-7LCaZTaOuMzapKP7alsPvk8lh_iVK6Jjuy0M86tVtTRzb7-cQOg4e9LTIGhHhOLom30O20cJus9k-2v7W4ZMCi4XXAmFO_mpgZcy1nGvJEzCggdSznebi1-Mze9Dc2uV6txvx76YQitVyPrC6ch91y5YrEhhalwmOqrDumxyP7HziqKjpy9jRhGXrm5GZi_HdD5grpkQkSI5DoyZyJojwsMOYE1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsOtAO3vGsueYVYK66bB9eDOGZ3PlKqfbSl6zEH3m-GIDsQYNMfR0vpKzMrMsjDesyN8VvpmbohMY9gisGVvPgFZBjqHsYgKuyTgiUZ5ohh_J5D3dTzGUB3TdomLT5euc0mTnXFLFnJzFuKxbkZaRO6srLsHrzL7h9qQ6oiu8Id3tKsHEMq4502x22_abb4Y_zkM4YBYuggnb8GJlCxK_XNrfijJJ0IxxGVu5gOFB07bLNvhXqrmQXeZQ0My79saO26g8jPYA7CP6G9dLROjaD36WZsKjFCbOwyV5iLE-p2PMtx5aqL9cD6RPBuGy2E0Lxd4EHQ8s8FG49pFPpay1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSMQrGuhD1I2hYInqN1JYbYcKX7vQhwBd4A57zW6sKrFlMoEtLidDYhp4uszaA_hNnwvROk5Cz8fhLx5wZ-iS2fjIh00NZuCwqHPZ-Oo4I2e9tBjuKi6pmP-H7Awm7IfZ6T0HFU6kXNLyZsXosQEWN7V3QIDo_n2c62kH2q0wvh9U6N6myjL12hBXXrkvcT3lVY06OOh5Ju-b41LjzJYu5jwcmBGqGWjzvTbyUxXXk4nipUqQQsM3EZ97txJMI-oDije_sVh5EiZZYTjdrJ6K9-RHrtSUTa8Juw4ds8fVBG3ijUr6Ev64VjD_m4Elu95a6fB4SYhJzRc4n0iLFJgRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_z-onoz8SXHV9vzzVoI6nagiIVhemnqY4jKbhehJ9iXDs2rM7kHDlIaTtZKZ_KA4nEpp2XzhnH71KbOWwLxH__o8pyadQvidA9__Z14UBPwIXtTJcKDtseNMncoQnIixd9Y7-THCE8aixeg50v01olkxOgvACsvawOr987VfeAWor1tp0V-C4KDhm5AO0Xy14gbi1_BnSOiJcA-b3EJw_9RDumJcQ2KybHNyFqCxeowjaLxjEwVWHNeWpWQVNNB-87vL9eSd5GfaRhvCTpcDtOJoRw8VC-e_rO6rghr28EmPlgXDc1PTTzcC2ELtECnzaKZ93oGJoi0VQ3sroMNbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=gVAcNLyCJYbWETqRABVJw8tZOl5BC8gE2SPspCKq4h1QJ9ev6B5-I__0Ay2WgN7f2FJqcDUQ6gB2WYVh7qxRJEQ-X_F7iRrNmsYI264aiaWmz51nGWV4p6XWgQ7Xl3FVDEU35oHwqkzYYdoSO52gNwmwT0GL50JTJMRf_WRwvWCDu8RiCu4VvcRre7SNxmvIqvfVRgnZpRXHIqh4zw7rR1Lexo9O4piiO0kJ2RFqnhDXcDmUysdG9my0q5UyFNeMevZ0kyOQdZ-orpuimV9-v6PECO4XvRDqsTiU7YJxRJjGUv9aLlrostUzugIRt3HfQ3xdkt-NmZtWy9FMZQgzQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=gVAcNLyCJYbWETqRABVJw8tZOl5BC8gE2SPspCKq4h1QJ9ev6B5-I__0Ay2WgN7f2FJqcDUQ6gB2WYVh7qxRJEQ-X_F7iRrNmsYI264aiaWmz51nGWV4p6XWgQ7Xl3FVDEU35oHwqkzYYdoSO52gNwmwT0GL50JTJMRf_WRwvWCDu8RiCu4VvcRre7SNxmvIqvfVRgnZpRXHIqh4zw7rR1Lexo9O4piiO0kJ2RFqnhDXcDmUysdG9my0q5UyFNeMevZ0kyOQdZ-orpuimV9-v6PECO4XvRDqsTiU7YJxRJjGUv9aLlrostUzugIRt3HfQ3xdkt-NmZtWy9FMZQgzQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=bFI4C_vhA8xY3akpNZD_WvZ9QxCfXe6Bou1hbjCmdvT8EI43cfksk8c8ymr5JT58XZgHxQN7h2ZulGwg-m-8W0iYkjJlsvRAC6zWiWlFzQonqNWm6etAzG8tkoATAsMwuBRJiXQh1zFZAHnUCKdOTkGvNtcOyyLq9gCeoj0l4GpVfes_vIU_8S38YE9zQMVZZaNQaS5C83HY-mGOT-k29-gB6wu4cGt3LBBB8Zbn4_gYXtfF4zG0z7bwwzx5ITXnSCX1nWJmZsD3JP5C6_o3jUwRHhex5EVRzhWPzEinHmIiUhwgH9T6ggdiZKdALGcJOYVcuYQ7g_5MnCcns5MYw6ttY-auS3n2A__r9KVXJJ-jW-AVmCCnZQDEJ5F5tqppOIGBUbcbjyl4SjkPRexVCyg0n27q6Vs7AN3mIp8oVvvGJ4x5kLjnmKieFcd4WPKIaoBI_jO7JWA1zKyr9XD_zhPmzo_QSAV2otqW4rnMLPP1r8AxpAPvUp5WiBwyaS7ivR9XmcQSfz26dXsbywpiKDgnjYd8Nm8rm5lCA4J8HNhH4bAX1Kd4f-xSVl6zt0RC4z7G0Df1I9ynLf48Ffr8Y1v-rTkWJAHKj-MJ-bntXDWaZk19mmogXp8FfR227v8PpA7t9qUd3JcShQQaZCn4UZJ310TjDPDTqQgjgt1nt6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=bFI4C_vhA8xY3akpNZD_WvZ9QxCfXe6Bou1hbjCmdvT8EI43cfksk8c8ymr5JT58XZgHxQN7h2ZulGwg-m-8W0iYkjJlsvRAC6zWiWlFzQonqNWm6etAzG8tkoATAsMwuBRJiXQh1zFZAHnUCKdOTkGvNtcOyyLq9gCeoj0l4GpVfes_vIU_8S38YE9zQMVZZaNQaS5C83HY-mGOT-k29-gB6wu4cGt3LBBB8Zbn4_gYXtfF4zG0z7bwwzx5ITXnSCX1nWJmZsD3JP5C6_o3jUwRHhex5EVRzhWPzEinHmIiUhwgH9T6ggdiZKdALGcJOYVcuYQ7g_5MnCcns5MYw6ttY-auS3n2A__r9KVXJJ-jW-AVmCCnZQDEJ5F5tqppOIGBUbcbjyl4SjkPRexVCyg0n27q6Vs7AN3mIp8oVvvGJ4x5kLjnmKieFcd4WPKIaoBI_jO7JWA1zKyr9XD_zhPmzo_QSAV2otqW4rnMLPP1r8AxpAPvUp5WiBwyaS7ivR9XmcQSfz26dXsbywpiKDgnjYd8Nm8rm5lCA4J8HNhH4bAX1Kd4f-xSVl6zt0RC4z7G0Df1I9ynLf48Ffr8Y1v-rTkWJAHKj-MJ-bntXDWaZk19mmogXp8FfR227v8PpA7t9qUd3JcShQQaZCn4UZJ310TjDPDTqQgjgt1nt6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q97_TvrOlW3V_WNCleG3z2cXsrdqKNIfEgHsI35cxsfBVqDsM522tOv-DvMIkr1EWwMdxoODGrh5O8dGaHoOvxGBAwXGMLiuZNom-kRLTxVKlbGVJraM2o11xXHw21TaSIe9OfM_CQV7XG4KxuuVllkBCV-u6wVPq1FGULrJYjlDmktOwPuQac-rrKsw2UQ11VRalZstyCFNW3HH5pXWFguvwKgZ_bRp_qeohY4ShDh9JZnKz6Co9sHNa2Ej-sHEa_ao-lz3etmpJaWdElR63ENudwnP4g2_LQ-wjklod1sJjnX8UqzKWu9tCD3UMKoLO0aINGNnGhA3aW5Hy6nrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVzAJ-jxDq8B3l_imJnGDH9TpB4CzLh568ZrFKmIMxjUQlfl7Jbrh58uriMpPTCqFYHaGVe69WGykV2HDY1_IjUKWoVRz4y_c9sonfQzZfXNHBLqW13xAazbHsK8md5sQ7rhIWL3K1VM8vcKBXdTXDnCdxpljaEIzyfE2E1lUAL1IlTBTJQwVWeEii9Tl_zm4yLS6COBe7j6E2lkUC686zSkMH7-dxnHmwZxVrS1V7_D0YuU7GxIrjTBpjuzXMMmcGa-GI8tIXZwADZO_iW6GUWfo9i9NLUo4TgcJYnfCVBXNatoHb4vG81usT2S-gF4Son_egZ6SDVRnQt_vGwqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIJHJGgTTjP_5M_MK4VORW_K4vqUYXG7ad1vGyf7Dy0F0eKZ9KOu-VojXIpzhNRD2IgQW9U4PFxUaYOSCpJgcf9MnbK2Uw3fVABi8A0zeQOrxRwwIP-6K7sUxXvgDrbxxkPyz1yu7wF850hqouY4EXN1euLTMRVLv41CkNvihmBe4zzurk3FhgdyT9L_d_IqDi28ARgvnWpFvj-MDwiONo1vJJQt7-85MnoV3zD9P_4GFh9ByMnR2rf8TRhveHbqcffh-WpRZztSEDRIIwOviYEksYhuo7zBC2b_1zOo2uySSOELe6lJ5trCCqxoIp4PJoGkXwE8dEYJZ8eYMMLPnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/InIkHr1IaY4cw065bJdYELBKVW1aq5NA4pEPFBwA66pgJMCGJc7n9PTO3tGUuQlygmLLAzK-loJBq9h7LGVEH5UNEHV-d1D6IzTA-1WUI89tqgsn7S-eyHBcdKPVcvTyC3OB2UQqGyHeURoMWUlhfbJjQlZpcCH6hRo2vQsD1Rrb9FEQhtJxLzgLSaWPpAnFhBBsgoGy4aV5PIT63F3S40McWM9IsZaJJ5lAMvowfuvP2fql1c5xuyeBP0iPrNPn-X-C5oUxvZcqFPL451cb1Ff6JdH8DtFnhtAd9tpJvfXNgw20fiZOlc3Ppsg2azbGmeMJabSjkX1hUmS-hAj7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TImg8uGrbCQ1Pu3QaCg61qJsAICjQZEktgBgKqYsjESfhbyFhmbsBkvaVkFYSgU9hq_WK_pkyx0oyS4L_n0AjUCOlCWm_0Ct_w8npfughgxdfsFPhNKwBSzrXpN_o_8y8YLs_OWdF_paTiSF3mZj1GrqnIpKeggD0bQjHVxjDf_kREvXML_koxbAMe2KdbYewAEFqg55-y2MeZAOk_VQW8eg7Mgf8tsG-qjCDaVy1hAlVIYQPPpDtdCcfxE31rM4jhATbumvBIGeWajhen2EVmGu_OIppZCyNzz60kYecvosn9Rj6cI5VFXfT5nmo_lo2eCLLG5Cw7M8NkfK65SqwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKEcl3vVFnLQkAMdv64I6QT4JlhE_tYKiuccisKyyTHSOwtPEatGxpjS8HuyzKGtSEFLHRQwyUxkJ4yEBu54E8W4pWcIkUWRINmjSdKWYzlwZT3NSxsmNjRUZU5xKi-qJVBaTxHIpRIgsUopw52lvnl_V8mL3rD6iPWM2MXjxuv-vITGNoxOQEyJUCeZWXfWKN8klfMAWYnIpNfMkl5R7Pf9aMbhpb3bGg6VHgF8BzGx_3olJFrGNazAdvykpLlr7gI6T7p3rmo44AWsFoKg6ihjtm_zbS0SPCjkwrxgBo-R3W9C5X0cXofQaWYThqwJTIBDnPwsQFT2TEGSsJ7Xdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snTk_GKf2jyIgliipNJMVcyfW_ZJkiAdIryM05tkenBgHWLrD1jPGvs_kH1aX3Tob_4srTra36o4-Hz04pY3ifVbvE-5y1PBf1M1Shy_Turzq282k50NQX9UHPmd1XNlTrqPHOQLkodxwQidz_lXBD6POfI743BTzWhxE3vmD7SQXE8oCKi1c9-I_4uGIwvq45MrSu7gHYhaMpn0t77UwJQZBcQQILIjRGms4T8kf1hFovKx4PbcNSG3agWPBpgc7wkVeauFrA7UjmIxsHsJSqAjQWE9WVjBxK9uiyo_4f3gjLvnjdpf3QGF8Q-G5Km8l-IrQMC0WTqPn_5HMqoEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=ZBhJqhOzd7s9oD6HTl2xiXEUR_34X7RYpx1AAtuwBxFnlJPzsNyduJmSBo0FNKDIElBg44RkFa1EMC-OXNTzPS8MyYgPATvjV1omJExWM8ekbDD9pwPA6lo5fQ1Cwx2y83559fDDBt4B7H0S5azvJCbnKDfHxk4vLUE9gLD4HEUd0vpVu4LWcf32uhEjFOzdR8vEHBDMppX8f1bRrSGGKR8gDH1_daZ8QOPxO7FKvIV00L8Dmp7pOzjbvi24NiWz35DkmCYztdlodK18qKiKtqmtHgQLPFVNafE66SRTCGUNw-IH7B5jNFLioDYO1zd4ZkO4ZT59uuTARo8tn42Zvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=ZBhJqhOzd7s9oD6HTl2xiXEUR_34X7RYpx1AAtuwBxFnlJPzsNyduJmSBo0FNKDIElBg44RkFa1EMC-OXNTzPS8MyYgPATvjV1omJExWM8ekbDD9pwPA6lo5fQ1Cwx2y83559fDDBt4B7H0S5azvJCbnKDfHxk4vLUE9gLD4HEUd0vpVu4LWcf32uhEjFOzdR8vEHBDMppX8f1bRrSGGKR8gDH1_daZ8QOPxO7FKvIV00L8Dmp7pOzjbvi24NiWz35DkmCYztdlodK18qKiKtqmtHgQLPFVNafE66SRTCGUNw-IH7B5jNFLioDYO1zd4ZkO4ZT59uuTARo8tn42Zvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlegeBMNDO6ANVLIIDfC8md0wYX7oDrj5vPQSwWF-gAlfkQnftcl3xvYLaH7x4SBrbqOYIELtClixwfW2KNByiG0cWjWJteUCywfIOTqsIJMmB4wJC5kEL9EGJ3tVkXcBsATTynbr2IYxDhYfaOn8rAcr2zxyBQ05SYwmeQc9_s0CWcpJoWMsV817jZZx7zwYcSSmcJwaQrpYmuyoxxByJm-QHCU8W8tPysGAZhGd18O4e4KDDNDL7SyH-nBQdF_DF-F-yxwj6HoE7qaXtWcDU8TI2TMVT-wdMaS6v10puAuelY8uq8beigxFUdFXq9CK149A5e7zzcjtQsikofhuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6ThiyuxN8gmumg-83Ti_xIocdpN2TvNqiKxyimyf5l2tFwubZjxswgzTpYBz3DOaj5cjeJdHttmNnMjLsA70fD3Wxu_CvO0Xjjkmb_VtXOnfOoHbT7t-tqeZiIc8HlFPM64qMUjwA2TIj1wbgpd0dKH3yEWVUol1fsBE9zxlEix0Z5sE-a9yk0Rh5g04vw2wbY6faowoFcjpJkJ91VzpXHloaTsQI1Jq5jO4_jle5q-YeR7nnk7gmVCa2gE95amTl-jSI6iXdfY_cxJCV_qlobP_vxsJ-MmCLip0LN_8QzhI2wtsObPIboU1xFnVJUi_N-DmSIA4qAMp2H75j_i1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3uPDZf9U1RF2FyHagaHxMjhifOIB2yMbWUofGArAk5AjiQGTQs--yS7ru4BekfEcVmHHrqtL4CqMf4BWStwwrOXpRcL0FjdVk4ljnR9NeM0m5WynhxdwDCh573Modn_IaX1203a1lZub6mmqJfYaLUl1G_GOpRD3swrQ4DjMqMqR_XXLq5ar5FMKJr1zHfvUAtAFWGK6MGhjiApPUC6Y9tT9DBk8NvRaUZTQTjHKF8PAD-EZZfVpQ_kcvrnZXcxGYuL7QNH5sLHpDx1YD4Wf7d-4P4hkUiSQbRib3DFzq2mdLM2wn4VT_c7VSIIANpweiKbGLpFUWKDTm07zNINOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-fhUWpkNL2wgWhIhUGak1Q1q1seBuea091TZH7skw8DtXw6qGQjwC-YHqgbSZe068kotec2zqHs4kVjaZCs700pBYdNw94FzSCedj7qeN2xjYeihbxfWNVhHggeagDyL5trgGp7zLK9bmLwEgQoDmsw--dEHc9_M2_LRsf25ga0LOL8e0LXiX4Uvn7tlh6NDnFQ2aKoYmHsuHye1sS6n2mH-STWqAVKX3bXEpCv6HOkibM8nQuzUjscnu0S249eX4g-Y4cqVqLRO8-7oc3ZNlTGPHrSFMXS4oWWCVkYmf-Ds-GZQGYXGB3t4COamLx8-KAaKuQ6RiFR1YtT9NcBeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26718">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=dnIcufuaX9u5m0NRJFkx9K8-iKuOuZs8q6wEQown54kI1BLlSaHc7it-GMy6dM5JymmRGbhy98lSadMznHhlNVI7uc-Se5AjR_fbwmJexuSKEYc6t3kza-XXJ8Gk-5bFVezUD3VhFotQZ_vw4y3TVnCqvuN1RyExC2NhFV2ZcUl0-E_SkoSVPv93QveH6imhwKBc48iIWN-AE0dLZVAm2wrD0BZyaetOec84PyzkMq6ZGJlm2MD1wpxdnT79As1DiLTVfWVWqpTDUKUi8Z_ocZqCd5rGEs2Lb8Eg-aR2Up6ZWdpCyXEhvS94sC3uBSdFz14tJ4tJyH2Z-WYcHkhaOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=dnIcufuaX9u5m0NRJFkx9K8-iKuOuZs8q6wEQown54kI1BLlSaHc7it-GMy6dM5JymmRGbhy98lSadMznHhlNVI7uc-Se5AjR_fbwmJexuSKEYc6t3kza-XXJ8Gk-5bFVezUD3VhFotQZ_vw4y3TVnCqvuN1RyExC2NhFV2ZcUl0-E_SkoSVPv93QveH6imhwKBc48iIWN-AE0dLZVAm2wrD0BZyaetOec84PyzkMq6ZGJlm2MD1wpxdnT79As1DiLTVfWVWqpTDUKUi8Z_ocZqCd5rGEs2Lb8Eg-aR2Up6ZWdpCyXEhvS94sC3uBSdFz14tJ4tJyH2Z-WYcHkhaOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWE-xp30dg0Ck8OSxzAqQlY43etU-Id6iaIjLgejqjdqIcRXMTmwNqj1eVpt0VpkkYt_do4_eHZCeUD8XKtKRprTk9br3cTxvYOpO-ShRFO7l3WUKw_hQgfIJ4SvkJeHfnq7LRn0VTZvwa9YvbwDQhc8fL1DWsEmbo_HRbXHvsav4JUQe3oTmfzFwpznX4CXEF_RB08fSUg8q_0lbL0EOgT75AOZN0zvbbmzKYZqcK_zBL2Yq9oupAvyvv07I9taehFghUMZBV3gBmXIzSMoFf3v1Q0ZmWvwPYS-e9BBC3ilQ07l9Rv0MDRsvppi6NWHG5LEx1wYGfpZe4NGsKpbaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
