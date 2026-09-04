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
<img src="https://cdn4.telesco.pe/file/eAMM251mj5LMAALZBfm-wmOw5is_4zCHZ1PNoWF-c-vVXgcL7FJK2TqZsp3wldmUyXvwNe9fHe667qRniCRH0Ns69WmXEz68RSt0tlg85qSFf0InW7UAs_HNIBHijI4QUZND3Ge12EGgrnzoPyRKoqyuFmQlfb4xNXwsBnO6CPi_BaWB8IIgAJ_S9amNxPRajwh746A5l1ytvsgf0CQ55t_wq5XoMAzFP1MOPWOQYjOeaKVr8H6yyImwF-60byhiYU2M2sRUECAZp0LjoaUZFYVdQNwosPnnbDja3u1yOtN3BQYxaxQfF5HAwYIJTD-RvsaXUayztZfjB5i3wn8Qig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 608K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 03:13:40</div>
<hr>

<div class="tg-post" id="msg-29083">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLeAePrSs5JA5C7AFnmIs957Kp41Q95SiX9pfZpoRGf6-tWL4F3EnG8MxO6-akPEGbls4bkIVc9MuFscLWpFau0Vp3yHCv9gBIkdFoSvaYWNFldFjpNfJLacy14oOVMt_e1PoEUF0DKzSkiYaBM-der539UdO3rzqI8AM7RtWoD9uS9pZgLN8uizU96rcbMJvY0vYhxCszd-pUMkXvngIfGrfo_Mg6Qy9mTjuQU4qf8ogBzQQpfGbqvRYa1URUuoxzbnC4z0EgkdiGLZ7QnOOR1HUnaYGn8IxQK-dYor0lBy6fbVtF9NCRYzXFpf0zqImbtzM1NDblOdkM6jS5LP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌وزارت‌ارتباطات خبر داد: حتی اگه جنگ بشه هم اینترنتمون‌قراره‌برقرار بمونه و همین که الان اینترنت وصله‌نشون‌میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/29083" target="_blank">📅 01:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29082">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAhHO7y2F7U6-QoTjc7DktF8xgDD7xe4RT0p_g1GS5PbgaMlt4yX4FhCb4KFQWcejMk8vmVDZM_Du64kDzDx5nGW1-UwY23qScbyYl1EXcjOtq7lR9g0H8iBFbHGFUy3GscA7Mh9TT14HWtHkMeH1vTEJKcSQFXs3OpslbLCki4SyE3QfbGLiqeOqZGOPXTY-kj_WZYgWqRLu_DQpv4Ln_7IO2KXvbUHbu23NuXDeRWUHsFFk0BRlqNrWPq3A6dmk4EndIt9BHy1TG0p50r_1_HwZEm9xUQsN6Bv0Wnl0pF78mozKLjD1zqu80iqPI8LKcdKanilDFPrHJRGsdnwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/29082" target="_blank">📅 01:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29081">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pfq_zW4UADcp7eWDJN3k4fwBqMC08Ml8dctsjwy-871-obAwxDG21gEihOjl118RzNXHaqCtPHiJvKk2JIJijVHkjp6kU7UY4SFmzoS5gv8FqBO7b8p5kWLqZ2MaKJ-e3jLLfY3YEvwHs9EH7ooam4gnKvp2LV67CFMJ_Ygxo2GOXv4uWyBePwm3zne8pPly2GM7O5WH0riNt_CBL3P83Ikr7-QHcHU0cgvZ3KCHOFYndcnE_zm2shzIr-uSEcGMRaOo9NrPHdY6YOSEDBdPYUyb0uNn8lcXZMupi7tNH_D7tGpXQPEv5nW9uHP0Q3X2p_OsRm2cChMh596IisK3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/29081" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29080">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNo-x4s6CtzWhCcXc9pxiyGQWdb6I33NJkZFMeav45OEUNhE4vXfb3YCOon9MINysawdRXMxBg7hvpqhMhJCsbFDYcdQ-uZx5O8CUTAVJ4AUOtLP7r-JsTi7dgO5QIjwkt6q3B77HQi-QHeWkFGWYJPr5NMeE12ffv3oXFdcPCAmF5m5PrOoVVhmQJJxDIpwlqmOHIHBo-C7ShkdDI9nerphIq42ByeZshkcfYIk3JyMj2x99TvBzSc-X9Efcgr4AiniMyT-YjiYCA36W891Qq0QMOWXbVx8tIg5pMdzoKeTVWrpZZiGWpSliIkwAB2rojteGvOOKURPLPlDj04UDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/29080" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29078">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL3IgvPq6xfiffTvwianQXXMEH283d5nmEJ2upohcPY8kIOfHgY9Upj8efU47R_-LbOr38QEfTX0YRy-lAfG1A9V5f353dpf2ZUaWOEMdyhPYyrIsYsgaLmQVHCe2s6lewlVMGbhDftucDLGuTQSivNwCZMokFFtCy3jHUL7uFqtLyUVz3ZXCbIvFLiwDLR1nZGFwUrEGQYy-Ljy9JrYnPehnTMTql7wvhBmzrQfNDW4RNZGpyMAJV2ig-MsLlNJ5dypbSMrBlUyIige0Qgb8bmVreUGHIfrw16-noDsNpCw8WHJ7NrEz37MP6Xlfimh9BcdDV8HM5CVNU9gevz8sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/29078" target="_blank">📅 01:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29077">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEWaUkdesOqXtgBMxUxxSQ9oH3DMxX-CRLh40ZU0ZLx8Uxx8w_zZP71wfRYjH90JaDAyCgAuWlq8OWfP77kpo30hR8R3QobXpftdObILLECsmvdZbicLazXFimS2SDrWwrVHNiGuH4TW39w6l5P__7t77BRCCXo3rlfiz_dGfeXmVoidc-6Fhr-HHtmdXooDqj-gpWaOBmZ0mLfEgdBRVrK20rTRZjs4cXNFMjc_f4DN86iheZtOSyk4amnOSghhhe16GCScWcmLT3tGJLDBm3Q49Hpmw1F1OftCBWDnGLW-wLvD2l2DxTXKNDyp1vvmXwMOvr-cJXtQ6_G_QQjSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ از جدال مهم سیتیزن‌ها با کاونتری تا دوئل شاگردان نکونام و رحمتی در تبریز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/29077" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29076">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYrQBjCz6HX-SHvdTr6iPrsEItSyBSzzsSTtkGEmJirzr7DuivsoUGJzpGF5LX6x9kOhC2fM-M5okdklI2UndI0x3PYQ2bjxqULdTr0cVNBeYuqZRrC0erU5BhL_PndJunuMTukTit16eaQmb6ChNcw87AL2A22MJMqSLp74ErodRDCrzMYd7j1BCy4bHHjiJTxiQMrysCap8rKGPYBpu0WiX9LGY8hDfecaGF5KufKBxf18_MKrXVume9dXPjtQKas2LvsnzoXJbNc4b8kvhDbm9ihUbmh2NmRY14IXrdUNS2itSTylyJ64hh_c5UGmzxYDb4Q9ZlNqxitHhQgTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبردلک‌لک‌ها با دبل ایساک تا شکست همزمان و عجیب رئال مادرید و PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/29076" target="_blank">📅 01:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29075">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbJ2HX7RkjWUp7klwaykKNYSg4oF-yWWM_C02wF6P81FV_gVdogpKlBrDfzETwo1UKBLMNQ18jHTioJM9_FQjXQwUziq_XyFdTc7BTOM1BBA5qUlARgn8v9OAyKa5onSBKwAb_nVqemktd6DR27B3n6CpBKa3SZuFXi6-wihSfwS1i3MH_XsSBJTZIOJSP_ZeT_df8V-ymaZG5SnTUHmVhxKAE6os7sGR_p8VL3ivHJE2XjwYpA2ZAzUCvc232ZpEgQTHEE0ZT4P0sNTiXmzkrksjjX4UAYMcT_8RbLo3nrCldBSMi78k4hcjSj0cJwarsJQMkXY00iJI53TFl_Vvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/29075" target="_blank">📅 01:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29074">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qlav1IT0-570124oPYtArymsDlKHpk5ml-8nSwc_VWgFBT2Svgwa2XIFNEz2_PYaJYO3oJ8TiM5sx5aeY5xiHz81MWTI6FrobCFP3xADKL1A8GLUNmllEQMYEX06uYIa3fmLjYqL5_KFzOJ7I5Jl3CvOXv13AhlGI6poGE2FVTOzK7NoPwk1ZWR7XpMQBlGwpKWKmuTo9JDySOLt1SmWnriNb7grMYO4MqvOKh84wl3lnG2_VZxNYR8yl3XvZ9rqDKmrYB-XYw3_spUZJs-hP_tFjQFz9UeqqlCYhKpKVf6twWWTefO9xxkANkyesqc2Yxvv_LCjY1jv5_25Qwvopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/29074" target="_blank">📅 00:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29073">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRhqNyBEtqY6E4OkYgbiGyMTxgySm2Vfa9Q3hsxpH3zkal3vkBQeAdUT7BP0FABr4VCludKo2jY0pOQzmn2v7qqd3nVyVPAEx5rZCjCgamDTEiGz9p0eZuqiGbpiSU33i5EcO4bqyDqzr8H_dVDszRggDag8_IVFTv0DGq6eA1jSNykX5d7YHWuylGn9tXpDBA5YZSR3ykeozs2hwDY8CvjMu8NrFE8h5wKSJIc5jv96a0iD9822gOlKw-5mTBLhDUatrwR0QJB-x6fC29eaGeLfvQXSm_sG3vZ5lSmWnbGk1lN3U_d8-asGb31Lv06F2Istn8i-1tq0HITDWAsjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/29073" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29071">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRbVZxgLlH8kfuowAFTzBZFNPgFsZUv3iGb6MlMw7ASEmo816oZLKVObPpJ6G4Mz5xiKmtSJHajEEYhpnlS6EX4zB8crHV8mc1b0uLyX8ntNNyaGkiKZ_LcrWF4iii8tSA_VKau74VvmxRtukbbCZ3qNpb0-fgfFF14OAUli0E93Q1oakwiiHrlB66C9zNV1n_qdc4iyQ8Wuq5t4sUp2U7k4rgmtPRN0moXljeWCIJt2S_J2yE79HyMioNVKzqgbC1SIZvoIITabIHE5ZTWdthIJWiZI1IWBC2x23BGTXcL9jhNSV7eWtQWgkVT1_1IwJRhRA7yQXgsjtScSAljZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شاگردان آقای خاص بالاخره طلسم شکنی میکنند؟! رئال‌مادرید از آگوست سال 2021 تا به الان نتونسته تو ورزشگاه بنیتو ویامارین، ورزشگاه خانگی رئال‌بتیس این‌تیم رو در رقابت‌های لالیگا شکست بده و امشب هم تو همین ورزشگاه با بتیس بازی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/29071" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29070">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGp8U5NsWlckF1XA5Jr_lNg3yoAKkXqo3zSYXVzPiojsEgF3lza2vOhn4cuwrgveVjx_u0IfpHzVF0f-7oZ4Q7VDSgM2haPK6jucz9e59hv6qGnoUnysld5QM41Il-Xgyakt3grZ1e8w1F870fThpyTWSvnQp5CCId3ekP4kWBL7Nja0kPdUyYSdPBbBpbO5KlJ6tzIuFlZdexKBeKr8cYaYwlXQ6Hvtb5PhRkyu-M5B0iSXaGXt9K_7NNUMf2_r3mZ1KdvrC1c2Cu3r0Octxt8gNK8kxPr4KkSG9o5QvEErgTKBdH0PlMdoKeBfvJuLZLCillXqMLnLZIBO2jeP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/29070" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29069">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
سوپرگل‌دیدنی‌عبدالکریم حسن مدافع چپ قطری سابق پرسپولیس در بازی امشب تیمش الشمال مقابل الشحانیه در هفته اول رقابت های لیگ ستارگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/29069" target="_blank">📅 23:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29068">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pd1FM-Xki3P5h6oDYqg_zU-GGkK-2r9QErn6S_v9uXCCBmIzQls0UnbvjpipgzD4g6Xlf7r46-4xd4G6tfJ17FTh99ebHnSLe0NHP_5z3jo0FfmND4KnOOxDItgiIB1s_XeetcveSFUgO9PIhp4HrGCjDisEAfo43q0FqDiv4qOKVpM5HmucCM8CD3rtRXaE6YKcmWvP11XqEyXbW7NSg98JmJIVf6_bBiaEsbLERUrib-_A1dgiOMD4wW14BBfDGsVw0YZ0PiZrdBOXdzXEgxxciRwr3DjFd3FqUYp5Zi47gonQxLYOaBhxhmPrrgj0rgFgOmHvd86DU5suGxMC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پاداشی باورنکردنی برای نمرات خوب؛ یه پدر مادر کرمانی به پسر ۱۸ سالشون قول داده بودن اگه امتحاناش روخردادقبول بشه دوس دختر ۱۷ سالش رو براش میگیرند. ماشالا پسره هم کم کاری نکرده و تاتونسته‌درس‌خونده و همه درسارو با نمره بالا قبول شده و همین چند روزپیش‌رفتن…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/29068" target="_blank">📅 23:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29067">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGlmelvZxmQll7e8gnZiQIBXmotLVVWT532fAQnneVDYqCMUd9ejSFM-wkIm8TcJmLE7H9FqcYJ4vQ-jB4tRBgr00oBcpARYBIG546_eEiZq_VCcNl8A1V1ZK6kkakxNWcatDr-rDtI9k9R6j-4EtYsXy6sCBMfbaZGw2TFbSkEkpMGe5K-iGf5ZHvUcez8oHqnEkuHooZqZgwLP9qjT1bWlf1s7Z9Olh0gai69Qm2iURUjJTnLj3z7yQm4_aSBMTs1RNe8-N0s8MIWTND-Fvo8DCge__HCXxlKK8xfq0DvvgeaLepAfhHIr4asfEs7v91WMJP2vvmsua30pFhEQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
پرافتخارترین باشگاه‌های ایتالیایی از حیث گرفتن انواع اقسام‌جام‌ها؛ یوونتوسی‌ها با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/29067" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29066">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRSRmuqrKlK5E5sN_Y797B5Pn0Gs64b5mI4OrpsCTsjmWGCc5qdiIeADWFbbyi9F0gIjBAcsNUn8oMrGRRxjoztBaySOy_73l75a7S3rN0ZWlve5tS1Y88_Ja0-LjWKZyT9hYB5keI1Cva_KVa3FfDQHOBPZThBSM0yytcr64J1IJzUPXfcvMpa_PG5whQkhVwMDK2Q7_GX3hoRl-T9kur1D-sE2BHMhT6NEvo3zJnMuxgCwZhJE62t6jYhFRGlMxbat3ZSSpiFaAnIOOQj2wD8xlHcFLRZT0pGZFhituN2JY20grYSn2iHvOADwBQZYQ9aB6f5vpP2FkT6kYbbFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رگی لوشکیا ستاره فصل گذشته تراکتور که با قراردادی دو ساله به این تیم اومده بود بعد از جنگ قراردادش رو فسخ کرد و با عقد قراردادی رسما به الظفره امارات پیوست.  این هافبک آلبانیایی در ۲۵ بازی برای تیم فوتبال تراکتور ۶ گل به ثمر رساند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/29066" target="_blank">📅 23:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29065">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWvSRcCICRiskRIHH_E3LOUgTAvhTNZyT_9hyiW8t1x6rPD_4UsOgAfdSs_U3jtoQkQHvQPzR7EDb47mrJcftCo3t-IZsLUTWvVVueIM4h0BsRNbibImzsaw-RUK8dClQVA2-KnLhuivcStFleJVNo5QT51heNhkBPKzu_z2O9enngJC1pJR5RlEPVxn4-geqAJLOnnth5tMwgW8oJmEfue9Tiwm5UMe7Q6ChuwX222luNOHuWNhpq0Z4Fng0FrIQnzbZkQHLxJ8Y2sojyf0efIxXm3_2g0GVeQCNvMfpl3IVoYTsN5d3oYVfajW7ti8W1h1M0RJJyPxfwotnymOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/29065" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29064">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXOBGBkOXNA5VaaRiQj8REq_B98Dz-bTnicnvw3jr6BiguV1QNzpcuy98KiFg6Q60114ezuBVHwKk-9QxrC5lSf-dn8h4-YDvqcZOve3lmbN8G8kTm1_ntqtZBW-3DPqSmG_CHFIKoDQxF6TPVG3KQC6iwH4uw8OrmzXre74D03jPkm6bI9DEx-tLmeYWZmjnE91BXvdRr87ikXUDVe0zeoalsi9eGEl9kuP7R6LeeFh9vYy-RKLx-GXsmU42VZ-NssRmg_Q2zM2wn2RZYxi35200MuBZsPKa-4cvkBDE46tmFbWekuOlIS7e5QijGROaUyRMnmdg-I8W3_Zg91n7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/29064" target="_blank">📅 22:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29063">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJGalCUD8dQ8Eo39gyQQNaLEgyWykLhrhsk23sfNpv-1L4ytPORwgxZMRucHomfyokENOW1CiL-B8q9VoRNw2Y1Im2Xu9ty2WwXXPUObNy6xscZ5osbjUmWuG-AIZVn7VkE1lkts8JBxBYXo5eNviW8smDcrjB5wnIEwQS1kT_EWvWN_IecC5djEfQKY-lyNTW_VqP9P3upeDxQzt4GajpZSEwreRONUz5yFafcDOEBi_B40723wUTlrCexyM4KPHiEDNHWatQWpyv9l-FUHC6DAGkJNf64WcOcr6DXBBj95UB1X2o1GkSAlSlVri9uYnDWpy2f1xWb-5RIFLV4Zag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ویدیو صحنه‌ای صالح حردانی در بازی با پرسپولیس اصرار داشت کاشته بزنه اما به توصیه سهراب بختیاری زاده یاسر آسانی پشت توپ وایساد وباعث اعتراض‌کاپیتان آبی‌‌پوشان به کادرفنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/29063" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29062">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsjCYlvdTcIJd8bPpmthLRiVHKd8jYdLZrvNaHlyxRBXurMNCS2xkzXP8xT917CyC39zBIfWRLCmG8C7PiFxMOXgcxz5imp-R-Krh9oexDiQPcjweH2xfZy2C96MOaLkmPPoe-dB96Y2GKvFnLmVy4aauamDwxPvSW1LTtcK-ecyW4eiWjGUXJYIR9HllDiEWd_26sDB-e85x4mHqjgwSeGnKT7MjIn5iA2F_cMnssO-Jw8KqylgLNrnPGcPsLAFKCB0ConxUy5tlVWfeAJ5YCYaPGqKnnaiX9jHQMw_CxZBGiHHVScqQqpOBTmtIfxEVZGSuMvDsVtgdJqHHwurKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فرصت‌سوزی‌عجیب‌وغریب و دور از انتظار طارمی 34 ساله در اولین بازی خود برای الوصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29062" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29061">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSiJHjTOy5GxfFw7O7zNRNZ1H656WL6mfBGBwUTcg5QZqu6FrI55YngdxTTm2J6YibzsqRC2BgT7I2iXB4vphHNA9VbzOr9l9JbWW_P2bpCJZFnl5Vb-4D4OunV4bF6WXLfLxahXKrK1Frn-UPgrAYIysGXRvzjLVMhLiFmUOnDYTU8_UjVdFgkgkWLeGMWOAL9vFsG0_qgyOvhYzsE_NHrHGYB_PFOLOxf3s6CzoWRGAbEM2vmq3U0zKX6EcXDIgOXXd3h0FRA4B_XO7gAMeptZHdspnt7cOyj9oky4tnE4rnSkTlT2i3VIkjmArXGfMSCSLc_yRZ-VHx_qtCMsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/29061" target="_blank">📅 22:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29060">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=bsgZlKmSrpDtmtF4FNtXOxFck1bhOMVF1ygx6CwXX402YuEvZweRnnlP6aVFrlKIFgjkRBmDIBVXvbnfVqsTmyJsQpSZw1FEMqgg4ITq0eyFmrQG_xr-3LlSehsqImG8WWL3Za6_stxXFZ-ATWJh3y3kZeKIAjlmSEAFF3Wxg1ftS1dLBoNmCr3KRbeYNWHSIXADLw2SfWe_yAjXdFV2Cpzka3ka0crl-tGvfIY-DzLK9dYigyKppd15qVOdWKGaPfRNfWnBeMY05Cr7lrbmOYMDEL3y56Xcawwg0GIAJIObOoIycBjBbH9brmhMqhoJdTnsaUTtECunSkIpxl0Q0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=bsgZlKmSrpDtmtF4FNtXOxFck1bhOMVF1ygx6CwXX402YuEvZweRnnlP6aVFrlKIFgjkRBmDIBVXvbnfVqsTmyJsQpSZw1FEMqgg4ITq0eyFmrQG_xr-3LlSehsqImG8WWL3Za6_stxXFZ-ATWJh3y3kZeKIAjlmSEAFF3Wxg1ftS1dLBoNmCr3KRbeYNWHSIXADLw2SfWe_yAjXdFV2Cpzka3ka0crl-tGvfIY-DzLK9dYigyKppd15qVOdWKGaPfRNfWnBeMY05Cr7lrbmOYMDEL3y56Xcawwg0GIAJIObOoIycBjBbH9brmhMqhoJdTnsaUTtECunSkIpxl0Q0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس کامل مخ زنی به سبک مهران مدیری در سریال جدید او بنام مردسه هزار چهره که از امشب فقط جمعه‌ها از شبکه سه پخش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/29060" target="_blank">📅 21:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29059">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEXEEVADXqmquCQ_Wg-jKgCkJF_OvfcsKq7PSjhBXf5dFy0JR-2vr6pS9sYkX4byCvaYRu3pgwfFEe42o_J_jMmUzsLInGSl-APFqu0080FI27A5mDnHhWxEI2rMGfRFIfgYvP-BYuIs6erBnfno2R09ivdhrojCoviUCpDZ9Uaz73PoL9gXk6CpXcjyHbuFmmDP1MZ6wXlSNe29M5jrKLhtKy_WhfoBOutrVG35H8thW7p0YQgyePDoy9pFiYmezckyW-MM5TB-CXU_XZSfvcGYKbVAWl73vfiuLKoBEFUnv7kk2RJXev72bkMXooxIzXZRdmcqspW6kZRE1jUq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/29059" target="_blank">📅 21:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29058">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=E_Ry246ESrQWAxLG6-f8J6NY68dGI0ageYZmA70EVVBXjQAH_bSIfSh3Sk3E9Pg0nv0T47rEe7MBAMYxyJjaXdng2lsIcGRq8sXBo6I4qIxXx04_VhHiCYvE3o869wp4lmK7gm2C0N3KDc3-eJ2wx0bE0sdOHisQU81G-MModjWTPAEcCUufRFgoIq9YP18PCKS_34vDodJgqF6uA_3vcf8NWVNhn8FLiUoyfDlBf1KGW6ifQYylgBu3WmAxUq0uU2v39Z2N9bAUMeSyelPoY4kARSzgQAzrFkI3VZ_U3x9ffgq8CbqbhQIq50Nb7sutfIiA1uG2TGggXQ36JOUjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=E_Ry246ESrQWAxLG6-f8J6NY68dGI0ageYZmA70EVVBXjQAH_bSIfSh3Sk3E9Pg0nv0T47rEe7MBAMYxyJjaXdng2lsIcGRq8sXBo6I4qIxXx04_VhHiCYvE3o869wp4lmK7gm2C0N3KDc3-eJ2wx0bE0sdOHisQU81G-MModjWTPAEcCUufRFgoIq9YP18PCKS_34vDodJgqF6uA_3vcf8NWVNhn8FLiUoyfDlBf1KGW6ifQYylgBu3WmAxUq0uU2v39Z2N9bAUMeSyelPoY4kARSzgQAzrFkI3VZ_U3x9ffgq8CbqbhQIq50Nb7sutfIiA1uG2TGggXQ36JOUjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استامپ‌من‌کیه؟ بریده‌ای جذاب از سریال مرد سه هزار چهره. امشب‌اولین قسمت این سریال پخش شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29058" target="_blank">📅 20:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29057">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=uxfSwWmGja7HpRkuxhXIdjI5B1iImTvqZ8N348Qs37TwrPyPmnGnCIgnT9unvEUgtwGcgOjd27KEbrKCXSJ8ppHeIPI6LdfCqV20u8BY_mJLLeodUklrgnLHLwezov1yAJz5MhLQy2WkS7xB_b1kG5YJ6r3VsUR9OIgyWtWSYiP77V6K4mNi2NSGW1SpTAyhKVFmAvhjTzUwQOs_FzMMQfy5Y6_YVL5UcyhrQkIgYK4oI0v9wxSKWaGg2Pis6BfCukp7r1mjaWIST5NBfJK1pCT0zSgqxnba0dVoWB82klxwqBnivGvypfKl5B62hvGW12Ki3Qi3m4GYRG06gihyAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=uxfSwWmGja7HpRkuxhXIdjI5B1iImTvqZ8N348Qs37TwrPyPmnGnCIgnT9unvEUgtwGcgOjd27KEbrKCXSJ8ppHeIPI6LdfCqV20u8BY_mJLLeodUklrgnLHLwezov1yAJz5MhLQy2WkS7xB_b1kG5YJ6r3VsUR9OIgyWtWSYiP77V6K4mNi2NSGW1SpTAyhKVFmAvhjTzUwQOs_FzMMQfy5Y6_YVL5UcyhrQkIgYK4oI0v9wxSKWaGg2Pis6BfCukp7r1mjaWIST5NBfJK1pCT0zSgqxnba0dVoWB82klxwqBnivGvypfKl5B62hvGW12Ki3Qi3m4GYRG06gihyAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
🇰🇷
سون هیونگ مین کاپیتان کره جنوبی:
من همیشه‌گفتم‌که‌کریستیانو رونالدو الگوی تموم زندگی منه اما بنظرم لیونل مسی بهترین بازیکن تاریخه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29057" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29056">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY7IlKPtSdQNmr_J9trOT__ZqZvFa54XR453mFz7HEE2FWOExq7uQOsW3OTYU9dEOP34o6OM-1ZCAYsoaOZu7Ew2KqFBqwgA4eYpSCHTA9-WyG40bLPPhY-tYXdNIzbb8-xGdx6h1hvCFRCxf3vU13HNS8QLQfhnnPwg6ceH0rWl4V70IjtsN0UJQ9X8w1jz7A0mnQpVgD2L_qx6o3jw0jlTxOb4k1tD1XFnJjz5EuRBRcM51h5WWC3xs0apMEBPdpWIScrJRzBqAPXA-ELA51L9taamX1VuBlb4r-pEbW9uzm4xgMAMDsR4dmGexpHL4yakKjaNlbLWXkxoN7KDMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29056" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29054">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D01OmTvvurkuwYCpvZQPbOb_Te7yJ1ytlda0HOa6PJUqzoQqdQQypl9ITAD8J8X_TFi9s6KAmrFtT5kvQZquf132ZJWXTnpckm9HM_UhegQMfmmGx_roIvnn3ZD3akX9EhIZ2Mlj_TcdHnLJ8QlbHxVWVxesXBrYYNys1uylAR1EmFe9ettmwoVFwAvccmL9YkFB1MVgm2nnQbzvybwuUnQJV89KJa1uoNmm_idv_iAb_sCAIWS0AZuELejs0lOsIAd7OMuZVMSeUlP7wRJY81HR8pI2a4ymFzLZLrOviV_ZNYC1KBnbcRXWXOnEJZs4VxKLnGtLNwb9K0CqzAZT9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlgsVPOew2D8smBbRzNvSFqLo-gmYL6U8Q4C0rMGLJ36YHVLjSaCVBsatkTPRsBy1OvuRqzmcJiDsRsvTjnSC56xLtM9_vCZXiKQyiu_e9IvAR15LAMzerTK9MvsVcYMbN43_WaZjZZEa6NQYTk_PR1aN1ZJepcOe2zelVy1Y_QTPMehpv_ICOV0nTOldjJcjQLZW34LPudWbQNq3c9sId1CcsGDO9easfhsZLgBmylCHYz5qGJRcrviGAeis3TbCDM6HK9R9_KufvDj9hBUDhkBm88ULDr3Dh_BMnuxXQJ_KMkLiF9LmNxRDLyeirWya-TlWpDJai9i_kE3uEl0lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکو خمز و شوهرش برای ماه عسل رفتن توکیو ژاپن؛ تو کامنت‌ ها ازش خواستن یسرم به شمال ایران بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29054" target="_blank">📅 19:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29053">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2OY8s2DwI6iyJsKFMbUe26xN5nQKUm-ZCyhjqY0jQlHO-NjJzcxYlyyaP_rP3c031tFCIY4dRWq3O8p3WPTrEwWeH2vUxOFvKWjGyHAY063bRGrwIjGSamAApJ--_zccqQ74aGSNV81IB5sre_B7CFaVji5bdoGT30oOYJjVlXAmpJSYZWcTDxaYVqRWIPTZu-DSCICkeiISTFxpZthf-dJVlS_GXIzQO-X6PsyN-KHkzcuxsE3QhxDQFy-iLB8anyYAyGcu1b_foO54c49B2NP11ZxwVQOGdrqI5rYpNnvO8bS-xDA4OJyHboPKQ1I23awlNue_I9fqWgvjGuQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29053" target="_blank">📅 19:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29052">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=Y4A6UeEOXoIyEyWBkcqLI_GrmQnX6rpm2-AjjLFOMrk2KW7LwkmPS6_i7kFR8RJ0hSpd2FRfOwkG_96vlaPI68D8o4lBQQmf9ihlYAyUeM0iT-KUxk9at60OBslDSx_21Af0iBfinBnrHhIls--GGQqarF3aTbjzSbRVFGN-qFz1UJcLGLBqmxAMo-e5LYNkmfUhEXCNg0oZnQNe7HHqYS0fPYss5fBOolearWoADYMfEgl2yi-cSKnMAMzH1qCbFBMsQGtPl0PN3rBliYR1aREYDTHYJ6knXpm0ulFxDE8z3wOt36Nry969Tq52Wc3M_NGIbnIBWzlT6Lojs_rfrKraWgyOb6hT8HneA4BoQFIw7y_p5qFhaSA58X1K6qV3tm7HJ8V11Suw97Qd4zcS24R4Wdu-fsdnITb2jmiyzHTMaItGEkfJORksiG2h0DFSJ0kZrhz0avGEKbHJRgJ3oPsjA7JqydvpnYjlDdaCUSPjMoMpdrdJLaq7NDtqns81QRyrqMurieQFr3sY8nugIDGux04trLHk87jDd5c6RZ8Gm2kVXsUZqfOMNLJV9cutZpToLDGQiov3uqTjikgVwJLpqy_-uTwGXClVN7LTJYGzKYLZu2ltpymKmKMURnLgSHGxWjUjbs5JpQ95hPEWYmWHfI1P7RAldMDAJcpGtCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=Y4A6UeEOXoIyEyWBkcqLI_GrmQnX6rpm2-AjjLFOMrk2KW7LwkmPS6_i7kFR8RJ0hSpd2FRfOwkG_96vlaPI68D8o4lBQQmf9ihlYAyUeM0iT-KUxk9at60OBslDSx_21Af0iBfinBnrHhIls--GGQqarF3aTbjzSbRVFGN-qFz1UJcLGLBqmxAMo-e5LYNkmfUhEXCNg0oZnQNe7HHqYS0fPYss5fBOolearWoADYMfEgl2yi-cSKnMAMzH1qCbFBMsQGtPl0PN3rBliYR1aREYDTHYJ6knXpm0ulFxDE8z3wOt36Nry969Tq52Wc3M_NGIbnIBWzlT6Lojs_rfrKraWgyOb6hT8HneA4BoQFIw7y_p5qFhaSA58X1K6qV3tm7HJ8V11Suw97Qd4zcS24R4Wdu-fsdnITb2jmiyzHTMaItGEkfJORksiG2h0DFSJ0kZrhz0avGEKbHJRgJ3oPsjA7JqydvpnYjlDdaCUSPjMoMpdrdJLaq7NDtqns81QRyrqMurieQFr3sY8nugIDGux04trLHk87jDd5c6RZ8Gm2kVXsUZqfOMNLJV9cutZpToLDGQiov3uqTjikgVwJLpqy_-uTwGXClVN7LTJYGzKYLZu2ltpymKmKMURnLgSHGxWjUjbs5JpQ95hPEWYmWHfI1P7RAldMDAJcpGtCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#فکت
؛
رودی‌ژستد،کوین‌یامگا و یاسر آسانی سه بازیکن‌خارجی‌تاریخ‌باشگاه‌هستن که در شهرآورد های پایتخت موفق به گلزنی شده‌اند. جالبه هر سه تاشون با گلزنی مانع باخت تیمشون شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29052" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29051">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=XxvkLKM3UQPYDnPJjFHtUzC-7n_biSIO5-I2jk51Oe0lrX0POCBB_XzMzfGBbRrvTsseLWSp-8PB6KYurBTlAZ66ckDCNChsbNnay6mvXHz3GOYy0APr2UeGoTp2APTRAHT3ew-teOYf46vxIljG1HuTx_anGvQdJtRJgy6WuwHEXher3FQ66dgd_RZse6-_xNnbfB0yfK-62kt3S6sGWhArSZ6jEFD8bWc9qg-wEUh-iZBMWF29eFiBqGydXM1duVl__0qgGOWIoZq8h7HiK1TSWn6OqcmyWYuvm7r1A3N6HHgVijTrgcXAu7czXyVNfl41puvHe80qLcwGmNaVyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=XxvkLKM3UQPYDnPJjFHtUzC-7n_biSIO5-I2jk51Oe0lrX0POCBB_XzMzfGBbRrvTsseLWSp-8PB6KYurBTlAZ66ckDCNChsbNnay6mvXHz3GOYy0APr2UeGoTp2APTRAHT3ew-teOYf46vxIljG1HuTx_anGvQdJtRJgy6WuwHEXher3FQ66dgd_RZse6-_xNnbfB0yfK-62kt3S6sGWhArSZ6jEFD8bWc9qg-wEUh-iZBMWF29eFiBqGydXM1duVl__0qgGOWIoZq8h7HiK1TSWn6OqcmyWYuvm7r1A3N6HHgVijTrgcXAu7czXyVNfl41puvHe80qLcwGmNaVyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29051" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29050">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4yGZSslhzedIsa-94Jf3CHIvtXnaG8EZMTRkAj2tp2j_CS5bwpXSe8_I5vA9NE8Jb7ELPnsTtj1l3HwpOpOFRCvqpWrJUxk6h-GveOWMOKItlgkunKJFFdGIU_QiXSAAQJK9vwyxjpaXedwKRLjFgIRVyXdEhnZCY8DaLYkTOCbR1GLxrs6rs9vDmfBdLLOUNAzRw8nfh2wVwyLwUqGC_4ivhl5dAJsLyKKonlvf_3vn0VCx2ZXJN7NNHiKjgrkoJsvB1wST5NSDMl3P5itbFMl4EKZ4hJX4pMo3hHYV84BK6APVSL_EfWB2gKZHhJlyeIlR0PdlhuejI5Bh1R--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
هفته سوم لیگ فرانسه
🇫🇷
پاری سن ژرمن
🆚
موناکو
🇫🇷
⏰
ساعت ۲۲:۳۵
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
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/29050" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29049">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDfjRQ5rSZ58Nq4qLb9oytctivx37WM9Vpn3QIOaUZ2QcXpiDh9ZBqJwpxXgZz43MTht-SgoFkoTHMFBJVjuS-Q0nCSrjJ1SiqcbqM7usESJ3LuVnyNq5TO5dVwtv4jbArAjlcTyS10p8cbtWSjNV5ME8Gc9SIp72UBg-y3acxdXQ1NW6kTHdH4_0Zp3Djky0hJbHNOZ4s5tX_oh1k00bkUsr5X6eEF_oeIYVEEcI8pmv5alk1s7mnoao2rIGFWgePq-RtQlcQdwARI00D7DcUmjmfiXkQmb5MUlvCGkhPHKE6NIrtlq2TSTb27q6qYsacykrSDJnZozQhh2VU8lZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29049" target="_blank">📅 18:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29048">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SldhEvyIPDVjBPERRH-XJyvo8_EKt7XeNVF8HqIIsNJgae0VnH3nSRxncpzDPcNnBjVS4iI4p1xlhYLwjVLXOsn3tUkvIPzKrUvcpLpqL16fnI9RCB06XGwy6rpkdrkNWm91nMgmtFvnjOHkA2rQr4KdYaeRMMch8v9gzFTIXqwXd7ghonO3QbKQsIOlP3Jn97uh8AA9S5IpzdBVZ_e1pOw6Z2rIZZjSXnZtzCEbmbWzId7ih_AdRQ78XnC9JvduH4kvik549LtUuc_0YBXs9FWXcnVCEQlCFfhczNJspk246XFtMBjTvVp-crYHnX7QKLxZy3s8jQWL5eEI4DHOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یه‌موضوع پیش‌پاافتاده‌ست ولی چون زیاد پرسیدین لازمه یه باردیگه‌بگیم؛ استقلال در سال 1399 و 1400 دوبار درضربات‌پنالتی پرسپولیس رو درجام‌حذفی شکست داد اما طبق قانون فیفا ضربات پنالتی صرفاً به‌معنای‌تعیین تیم صعودکننده به مرحله بعدیه و نتیجه در آن…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29048" target="_blank">📅 18:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29047">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9KOxamd6ISM6tGWs_lbCZ-lu74MQZULsLjehbQd054l5DAQO_Vp1XmzZPFFqfKOum6z3M2XaS02lXGQj4zq7u9fS5YBhiixbUtvzZAz277j2DBXoaAnr-3jqnIPeK8xlpHX2bdQh9cFQTk0299p_9hHo2OSXN7W0iS1g347IYNu2SJkxIG320hdNahMHOg3p26pnShSkS6BLU-opoFmg9xynkoqcjxtp4F9ZYgqKTFmr7kLXlGONO1CFgLuri4mGWlju_eR7j_2MY00VbpLb_NwJWdLqlO0uK-enbPoATNdzlcDorOdlwaa4vZkH9SX7wr4HrRBhzto-mwTFhVQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29047" target="_blank">📅 18:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29045">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNjeS2Dk0uuMutyUYK9HL-9e6ieaqCywlM7dnNDoF4zhMmeKLD2qIECx9v4AGjkmMPK62BdW9cQRYleD3XDST76cdZwdITK1MMpFCQk-R-6ZYQvn8NBcsUDVgm_a-HcbOiD_wUMZMG_QauP0NRNOszVzzQqi4uqoNENFmqbe4OuUTWsYax4X7ZwXjf9lqMfWaZWMWmtTp67SAf4R0p0Yw7U9NLctXGD0tkMh_3KvPbuWuFoK3HgPOwa7e-lE2BMv1gudcgURCGquano7mFsAv0TBdS8oSpRq1jsL9VY8j7wmM2uA_bFAQ4mFypjk68-ftsGrjzN3Ggy1q1qsfQQ_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=dsGd_zaPxQtqnJ8taSdnojhKtE3XQZbkdgVkH0gMaYulVEWNo836C-TNp1YxDMryGIP-_8tlQ9tedMm-3ip3B5iJ2yLB-afpUQKHMmHfNMi31ytakLM8og4A2kO2o8cvSH-9YuZj-BzIVPhbRcFW5wt3-tPM70hcALaJ4u7zbISDKoxKgzAmHdX_8eyw4d5WJODgBVXfwQYwt6kE1fIUIcKfVu3IissK82Ie1NECA_YsSC3A_Sq5KiZjQSGIY7WEjd0yCnaO2uVh-H7XIYqNsZjX_Qc2V5Y7R1F7K3yTN9qkOCqEXXDor8h0wgfnIQZiC7RNEgfjdSefuxdLv48xLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=dsGd_zaPxQtqnJ8taSdnojhKtE3XQZbkdgVkH0gMaYulVEWNo836C-TNp1YxDMryGIP-_8tlQ9tedMm-3ip3B5iJ2yLB-afpUQKHMmHfNMi31ytakLM8og4A2kO2o8cvSH-9YuZj-BzIVPhbRcFW5wt3-tPM70hcALaJ4u7zbISDKoxKgzAmHdX_8eyw4d5WJODgBVXfwQYwt6kE1fIUIcKfVu3IissK82Ie1NECA_YsSC3A_Sq5KiZjQSGIY7WEjd0yCnaO2uVh-H7XIYqNsZjX_Qc2V5Y7R1F7K3yTN9qkOCqEXXDor8h0wgfnIQZiC7RNEgfjdSefuxdLv48xLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29045" target="_blank">📅 18:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29044">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=f09kFnU9jkA5boRtilekglHDxSnY0krgBFvI7fOKpq7pfr_NTpjYGjQ6Dzeeaxm2VTJgtVcbv0LbEG3zwMncRblKgykZEOte9UvO-tdJNesTmHUwGQtnFnpjrTi9ibITSxCM2_Lpq-lCkyINATX1pbMSbneJHXaVI2rq8By969Bb4Lt-9kSSd85qzjeTwCnkeFtlqM4Dqw9D-WQuEj6ySiCu-2V6j5WEKyAchey4m5CRhJkiUIbOEDMV3BI3VFbAKhd8ji5yMDcpKU4oFPqhVwdLSHGrBj3TgL3190gncx2he13XrOaZliFtAoyAAl6cwB8WEPdyxhhf_q-DXrFyjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=f09kFnU9jkA5boRtilekglHDxSnY0krgBFvI7fOKpq7pfr_NTpjYGjQ6Dzeeaxm2VTJgtVcbv0LbEG3zwMncRblKgykZEOte9UvO-tdJNesTmHUwGQtnFnpjrTi9ibITSxCM2_Lpq-lCkyINATX1pbMSbneJHXaVI2rq8By969Bb4Lt-9kSSd85qzjeTwCnkeFtlqM4Dqw9D-WQuEj6ySiCu-2V6j5WEKyAchey4m5CRhJkiUIbOEDMV3BI3VFbAKhd8ji5yMDcpKU4oFPqhVwdLSHGrBj3TgL3190gncx2he13XrOaZliFtAoyAAl6cwB8WEPdyxhhf_q-DXrFyjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29044" target="_blank">📅 17:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29043">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBfNwwWchQVLp9ccFmTh5sj-n4FNMUryzoRTEb0WMn6rm-Kmjg8auEhJdFn6-_Z_rOCpGpk3WT89-UY9511y-SAN1M7wA2faGyKa9wC6nxLfW733jAOFo_xT10opoYRqaJI9VLVsXQLjfsO9w4w54j0awC3uMD8vMamZc4B5byw44qm8DyQm4B9516_S5lpfB_UaI7MMkAEf42gpQdDP1bE9hZDSSTJWpCVpv9B_-R5UKUqfRQFOkAoEhszj_3DZN9TAWy_0ms1CD55ZkLQwphlrBOoSG90XKwkjK5KzwgcBAmIONsY6ImFxWdVzHuqqPQB4Y9Rk2LTOLQXRP_dHbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نظرسازمان‌لیگ‌عوض شد؛ دیدارهای هفته هفتم لیگ برتر براساس تاریخ قبلی در روزهای 19 و 20 و 21 شهریورماه برگزار خواهد شد. پیش‌تر اعلام شده بود به‌خاطر بازی‌های آسیایی تیم امید دیدارهای این هفته رقابت های لیگ برتر به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29043" target="_blank">📅 16:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29042">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29042" target="_blank">📅 16:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29041">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep8dSMgq7bvHi4fUu_8KOfajXjY70OYKxOojRC5ObcriY4wGAbUf3jYaO-mWiDGTxd3Om_iphAc1k1vIsGcQQZwLcbzBS1iZYOy_nAZP8i48oi93fx3MPSYXL65vhb3txdRXV0_Js7NeRUnZrvV9oZxjCH0ktjcZGJErqRHSRDYsvrya2RSUhmvZDQuumkWiMY30FV0niwgE04Vd9CXrbluRtWP5-4s9JFtx-dIgZv1Gu4poOKhPym0vVqOmWcSv0I1pK32Hm2llnenQWcONKX36GW4RQdWaUWkUG3EFFRiKYN0xXpU7X2wJqOxy39o8njP6nf3FUiKJqGX7IEaz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29041" target="_blank">📅 16:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29040">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyARmuUmnRPduzk82QjwF5ZuepkbW_veqmdwgJLUyqxLbt9Y0thpkqoWJd3bwN3BF_NY_NCgNE2j9FbFgeXfQcZma-MlpUS3tDhT__ExqP9IRnDMYR_tVNO4bhhrT8nsE6-7Hgkm_BHhyWG10BFdkU7pBkvXIvBmDoRsBAmRCsJoaqTwVHnRg2rNbiwitYy1HZqFj5bXfz-O2gwfJpgZ0sbQTZfXS6nxmfIfz-ZbaZEw-fuhgOdHMqevqhp90rFL9NYTAe-UkpbmjCkbATv4YgE50MryS6pGjQZloXOBfbjafMXR2cNNe_Cy8JTrsA-k59Q-yQxMY1rhxvO0IGe1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته ششم رقابت های لیگ برتر؛ بازیایه‌هفته‌بخاطربازی‌های تیم امید به تعویق میفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29040" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29039">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iBQZ1yFiC6OrPmNpEc-27vjw6YCXH0giiN2snEl1jCQndNIQVP11IVhMSgQ066vLAxEtQnqNgVPFJp6wWv40JgJuz56mnBsv8-OEkcJhua8usUSAYSpITdDB7AAZKBcnhfvQuGEGoLlgpym5157GnIcTmLcN66sgvkHWVB4CuuzPFAjnU6F_joTPZSDyoc49UvvOOMyhO5US_75e0S5pb__7p99570Z0X_m050iQKpJ2u1bhfCDtCQh2VHpknz_EoMdgGccHJVygw1apk-G0Ce9loja5a6LA6fFsDE9bLlDem0iOKGYjtR7t6NrIDikbnQRHuKmKTUzZmYkfVtWyuXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iBQZ1yFiC6OrPmNpEc-27vjw6YCXH0giiN2snEl1jCQndNIQVP11IVhMSgQ066vLAxEtQnqNgVPFJp6wWv40JgJuz56mnBsv8-OEkcJhua8usUSAYSpITdDB7AAZKBcnhfvQuGEGoLlgpym5157GnIcTmLcN66sgvkHWVB4CuuzPFAjnU6F_joTPZSDyoc49UvvOOMyhO5US_75e0S5pb__7p99570Z0X_m050iQKpJ2u1bhfCDtCQh2VHpknz_EoMdgGccHJVygw1apk-G0Ce9loja5a6LA6fFsDE9bLlDem0iOKGYjtR7t6NrIDikbnQRHuKmKTUzZmYkfVtWyuXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نکات‌طلایی‌درباره‌قطعات‌مهم‌خودرو؛
این پست رو یجایی سیو کنید، رعایت کنید که هزینه الکی رو دستتون نشینه و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29039" target="_blank">📅 15:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29038">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyQi5g2en-5YeMIbJupz-d8r2bqeYEenNHRQqHxowg36bzIeSqylqONBrRci9p1x5iO6XFL_U2cY4YNI1gaDYTPiLRxd117lW3qlmkbDmrbXr4jxy3hyosHN770_f7iKc_61AD7G1J5igQs3yS9vw9lf5enTDtINw8Inbw3ZKKXSTV5Odm_aOyT7ee4YHGk8p5EJwUIGeaj5m3tgU6jkd4FrApdO8PX4qqzxjDjAPtBeyF7UNCN11hgTOo-q_RTcaW2xIQYUd_c36s5obJpkiFv1mpJLt7cQ1GZO4-nKCUAk2EXYenRlhr_HxtB3nO4w7B-BMejLpzakfrKOJe6d6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس قرارداد زینب عباس‌ پور مدافع میانی جوان تیم بانوان خود را تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29038" target="_blank">📅 15:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29036">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_lA-Zn5sqV7IYcfwB4TdaN3Ozx7AuJ1ArcG2UkRwGHjoN4t_ZgR0nVyGp8Se8hQAEBW2AuZ2nfWqiEeL7u8uBG3WCjMVOEg2tq1oNip85BymObDsKKCKyCQCIMTVqBfsUR9--CT9MTI7OntHu8pFHf1z6egfn16DAotCq4HNL21H0HOJ9zk1AiAVuGCn2XiztCktIakkmufCiSwkXAIQ_hM-9vyaE2BMZNbXj1G8-ewhAouzIu23vQbq0CuC-Yr3c12fhq9igyXcnubcT9Fk_sNOB-VHhrSca26miLwDxIHJYEhbWpkMuk2Kz3v3htQIDpZ-EaHycCtuIZA3WJ3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7lFCTDZGn1AlS5287jxg69w5vaM2gySPSuwQ9-JIp3-JVpy41GQ8xhX7r6HzM3oWFiGxJfh3lududPyckgotr4A5lnMxLabrjzA40azcp16mLCw8B4yoxqf3dD5mZZD0ul2uY1hR3cIb32XvRrMMG9jkrWVpaVfVvIixnF9VJ-Uo6btSXeyUEdj0UnKZ7ssM84X7TmtrPANXdZS_MUNT8eQqkXr62ALUq4k17wtvh3enH2R8cRhHNwaaJzhFUaqCTOvG91t2Z6gFPBqrlvQFciVEtp6JVkgIhFqzZmthsgwTp2iv3C43MBKrpMh6Nt2waOlVDPSMYV77ccMqBHO3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29036" target="_blank">📅 14:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29035">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQ2LIn69vcffIXouL6s7DE95xdJe3hyhtgJSyGWYBjzh_ROgrbv_23FUNs-4mxx8KlIp681L9ot8YTMhRev-f891K6M5C6lJgUlA0QddO7ZptRS6xwoFqRw2jezHKNkfW9kFAvNzRg0-Sl7H6YM1uNK8QP9vyY-pVHIHi_ma9sOs6kIPajUNyiJH2uh54lypkuZ7AU3J3Kn-azxEVPCMy0nE5O-dGRQzD0Nwqw4bPx2YzoZVgtCg6bMhrjBgeo0RJeg93EUtZd9yjI4TUf7n3Wgfis5KqCfiN7Bc75fvAk0Hrf-SEH8PuXp7SuEpIHYBkSr47PAv0HLEfs5berioBu9M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQ2LIn69vcffIXouL6s7DE95xdJe3hyhtgJSyGWYBjzh_ROgrbv_23FUNs-4mxx8KlIp681L9ot8YTMhRev-f891K6M5C6lJgUlA0QddO7ZptRS6xwoFqRw2jezHKNkfW9kFAvNzRg0-Sl7H6YM1uNK8QP9vyY-pVHIHi_ma9sOs6kIPajUNyiJH2uh54lypkuZ7AU3J3Kn-azxEVPCMy0nE5O-dGRQzD0Nwqw4bPx2YzoZVgtCg6bMhrjBgeo0RJeg93EUtZd9yjI4TUf7n3Wgfis5KqCfiN7Bc75fvAk0Hrf-SEH8PuXp7SuEpIHYBkSr47PAv0HLEfs5berioBu9M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لبخونی‌صحنه‌جنجالی شهرآورد 107 پایتخت؛
کاپیتان تیم پرسپولیس غیر مستقیم به سامان فلاح میگه من کاری میکنم به تیم ملی دعوت نشی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29035" target="_blank">📅 14:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29033">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCjbZIiJq4XKSdJtN9nYP_V8DxKQw0DYSyCQ_wdEZDB-BocfCnkjPuZbbcWFNolOH_FNJv0jnRCCmQAIPpeM2i3olmOrSi9KdzWrnKgZqYkvdDkIE-FXgC-qtYQmre_43ik7WmbCGP84mn1NXEcKa0apq36zAkZmKKVqrTWabWk7GrSE-MIZWg41t9m0wLDCViuNuHguuWPJiLohSFMgNw4UwWr03oMzAjgZ_GuKhdQmVMaMbjJSN2_8ZOxUk4fG5lDrq2b7r1hzmjFSIs3MT31_W387JqLSTFF14noXtpUY6CMKS3_4VhJNN8OZz6BULvxDmFZB536DDtjWblGMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_2ZACWubCK1ABG6YSO6C3kIJ6Z7UBHl9K_1zYk_fwJD0a3cAP3RE6INdyTAwHtWhEbk2tHRWQdQlSBdv25XNAqbi5Wv6cfc9hqRpGYxLlkWC5XUOmAzxWbuzez9_jSu5AN4lsJ-6o1CiognjLEg1k24x0mXjaPAS8tLTfkTSa7FysncPcpahpS6SFJAuJWLZ-TWU0ISVLWt-GAX-oPY5HmPSdOzptMu6SE-fdVFtTVmHfAhoKTVoL9Z9VoWTDYWYuic8S3OY4lcL9B4k0i2WB4qVc6yPqrWfly-u_CBJ776cQZNc7xw7aDq2oDP8OinQ07aiGu5p_7_40A_q2xkzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29033" target="_blank">📅 13:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29032">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUw2drwT1RHECqMbQ2Or5zKiCcU9uaDetsYTkIgNF6CCPmF3dwIUEIbD5p4uZYa2ILZZlk3_rgyOofn_-G6hOv7gVEgYrLd1ljq4mxy9ahrQzuFqK040T2zs5wmrDhS3IxipjNRGE_TYxPJ58CqxuG5f33cZXlAfMAgzEykfuhxSjejEHCl5zUA0TkF5OESEwymaSovcLobaG1Pasbp7YjGp3vv0bGlMSc_dDxEp_OF6krgpYIwvegc2VX-prCD8TKPa8mOLXOij7DioAuCqWr3p9Au_jRihb9-ntKnS_NDNSz5fABZknRN0MEimFaaSkhUXH67FnvN_Pi-jwJZyJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
دیگو سیمئونه سرمربی‌‌اتلتیکو مادرید:
3 بار درآستانه گرفتن کاپ‌قهرمانی چمپیونزلیگ پیش رفتم اما هربار کریس رونالدو اونارو از من گرفت. قطعا اگه رونالدو نمیبود من الان سه قهرمانی UCL داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29032" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29031">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=VBZchwcwitj4fYIIDJNvSF0b2NZoJs70g9r4gdLwMWZQBnTswjqEX5fKwOykd9IQbzyCtKJBhVRwQ8eK301Vis1ZJPGB-D3Go6OUHzhXja4Qze0WKWpwgruOPy0GVULqyzKFOGgF3j3veYYyElx2ZZDEUSR42kTPqn23p4j7K1HcJnl2YPLRYOr-AL_HkZbN4NRLv6UXOddCSfEAAnA3qu6E1ZLh2D4jX0GoqzpTOK38n-PGtPgJqFqzy9zvdUF5dD9XU-iKBEVBkyOfS0OCZlGL2YZqNHbviF6vvyz4rGJiXFow6cB4BAl0JykRbTYQzDSdA0gc2UWJhCPpAD-NvUCfhKjuPNLojPuNTeetAJOpxwKLhJq6_mbiXcTju8BIexLmakOhuv_PwfHzlU_io_qhcfwb0M7SiAd1VmgOjpAUcWgEcicepNGDSpUrw0JvfxH6zDammLcE0UGJqp40N7liKdRydz3luaVfEYX-V3TuBFxyh5vTpkcfrQqmU2hKmlFX7cMEUNuw8QV9TDDpVj5M165iO0SQwgFiyf0ZZgCPthdEalJx55THnjzpIQyFcZEv6pT7fOdInwUfts7k7n7XBEk6Gd53atFOGdkLI9iFWmgL9JT2OWXnRLOohiHylmlkJfrwvRenZohGSgPaHNIYCv5MSrqpwqrsvvok-wM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=VBZchwcwitj4fYIIDJNvSF0b2NZoJs70g9r4gdLwMWZQBnTswjqEX5fKwOykd9IQbzyCtKJBhVRwQ8eK301Vis1ZJPGB-D3Go6OUHzhXja4Qze0WKWpwgruOPy0GVULqyzKFOGgF3j3veYYyElx2ZZDEUSR42kTPqn23p4j7K1HcJnl2YPLRYOr-AL_HkZbN4NRLv6UXOddCSfEAAnA3qu6E1ZLh2D4jX0GoqzpTOK38n-PGtPgJqFqzy9zvdUF5dD9XU-iKBEVBkyOfS0OCZlGL2YZqNHbviF6vvyz4rGJiXFow6cB4BAl0JykRbTYQzDSdA0gc2UWJhCPpAD-NvUCfhKjuPNLojPuNTeetAJOpxwKLhJq6_mbiXcTju8BIexLmakOhuv_PwfHzlU_io_qhcfwb0M7SiAd1VmgOjpAUcWgEcicepNGDSpUrw0JvfxH6zDammLcE0UGJqp40N7liKdRydz3luaVfEYX-V3TuBFxyh5vTpkcfrQqmU2hKmlFX7cMEUNuw8QV9TDDpVj5M165iO0SQwgFiyf0ZZgCPthdEalJx55THnjzpIQyFcZEv6pT7fOdInwUfts7k7n7XBEk6Gd53atFOGdkLI9iFWmgL9JT2OWXnRLOohiHylmlkJfrwvRenZohGSgPaHNIYCv5MSrqpwqrsvvok-wM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29031" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29030">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVvqGIyPNYXVfiOnU04ujdH0sSkNnxrwc4TAko8YL49vGLDLbn30ns8T6uLjts76CULWZ95fASCjBAZLZ_JsNIHVt6mflPh8dGCBHNQxAV2vyVX0THXcmHPIL-ggR6EDVycyB7clDTxvWzKAqnhQROxz5aFCYeJm8ZttHOum6B0O1DAzHNtPPPS0NGUA7HRqTwqsJhtY9BWF73S54mq5su5V0KiUS5q5Rh2aI1TdBJpxDRtyoUD4yJXleAOvafN1bHAp_xJ0Q6F802Vp_HaUcQVl23SNeh6wJORYkvWLRUbD97RBuwV2wPKikgxITPpsHC67VuvMaFFSnIR8bPkZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته ششم لالیگا اسپانیا
🇪🇸
رئال بتیس
🆚
رئال مادرید
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
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/29030" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29029">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmoHw41y142BNqCAhoVPPjvYldqtuXYlN9sg9tKsrpfM6xNV1JsKOdvHc9kpYNFkTWtT-q4dSz6JDTnTQBhKu_w3Rp-BO9mHbYQr_bGdKz78yDY_dM02vPlnKWh89wL1IByVnYktDMdcrJqIyKfRR_1RYKTqtKtvlcz_CIB1O0-lVZEyPM-BVyKI7AJ45Y65z7akAiochmbYvlMRmA20jAa2AGTewhweyrkJHq5knd_Rh33nIzubytc-9TtXXP4197mpk0Ve6cgFe7PRU5wrsK_gxqJKrVUa7fSlppSRaU-pY7jGdLLHG0q5JD1yrwwtOMA2UwWV1DENGGrTKDzMkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
نشریه ESPN: احتمال اینکه لیونل مسی و لوئیز سوارز درپایان‌فصل‌جاری رقابت‌های‌لیگ MLS ازدنیای‌ فوتبال‌ خداحافظی کنند بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29029" target="_blank">📅 13:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29027">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4wF2lm610y1IqhHx7EGxOPSp-JQXXTP-kjhV9itZa0YT3ku2eHnRJRNZAd31d-rU-S66-IzCY404EHbZ70KBOReHvMfqOKyfvYSBO1fwe88CI_KBXWOHPHcq6r7yM-YdqTm5-YanwqpjbwOVUvSUCWvS9Wzn3ZQFaG_TAVp5tfPsajn20dhtBdwsIOGN7Npa-9PPnsHNqG8yOgb763b5WBm94vFXhVA13zlnBnvHR92ZnJfS2t5sZRhGIpD0KY4qG6wtLxdmQBEsMHbErukaE0G5Kq3g7W7iu1Bq469vxmRgXx39NDeD_1HYbuLcMUoOEvSO7WTdde5i29AnA6V8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nblSXHbbmNeOoF5sig2xltCMO3obuQ5LnvTJgg65WwnKIVsE9LwMwMvKPlCX62rKGXZifm-b-mZPSelnUridk7FVIcjNkrQcGlvr-5Kn12V4K7FbeNYNenf8uaRzVDyHiP68jZ9739XFlzL5GDQ3WYzVparIOM5r6nBJCE8qo1Asnn4v8Zx3PBHmiEESvo9t2B0etuHrSVUTVI4JasESZuby7W1HUJ_de4Rdk3CNQABu9vIBJCHT7HXbb4IXpsIA16Zg2sZ69mbdD1GMo4kJWRw29YF3L045sWA8xBWEhCacCUpuaaj4Q0bLUJ9b5zo6p2NQ5Ek9Wkb2Ddy6eYGtTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29027" target="_blank">📅 13:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29026">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJAEah9fswP1bysHox6BWzVIHf2F1rzTUQAO42IwJWNASNrngo2RsLAhWvHWyZHfMLB8o8E9aVOr6SAJ5w1fq2QaqzYv8RuUPXPwBh_RI6oyUI6xCipAVTbFvQVTT-N9UDFyqX7XgG237ERPtkE_PNs8iWiZGEQWvGd5QCKWeIraS-og0j4oKyo_ivbS52q69keCkecMeycI7zKogXDdeSfoE0IYq7FWv-6kxjnXEMMiAYpBsYBdwlMRESrxmA-QMHGqA6m5nFAwaAwpI_WxC5piK_embVRNcF2T0t7uNIt1_UwUG_EOd9LKqG5a3ETqDXJ8nrTqHYQyb8IsSs3fow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29026" target="_blank">📅 12:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29025">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLCjAPjEv5ipXUGw8tbm6_ftLT5XD-n9LV6BJy7wSFM4qNt-9LmFvwZJRn2c4npMQamY76snhki7_rO01OoKNdlrN2Hi3UHn6HygrNyh_6HSo_IpXj0pNRKgjA4uB6DsSw9JS4j-yjx-SuWewh9cr3MEoydzKVVQYlH_t3xhJdcPMf-zB8aw4YsjoztxnEMRWqCugaimOrwgF5oucrUBfFM_QD4XL7ZT9C3QFlQmHWiFpEeE-5-0yAe4YHs3F-n525IZdmfDAIMv2UB1RybAnpsAkWmDVhyX3UY5ZC-e9TGlx38twrxuWECY8Zi_Nrv1W4i-y6JgvxmCKvGXZvHhiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29025" target="_blank">📅 12:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29024">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doea40GbuKm0bPEsmlMdHvqGGLfC1tHoX3zAac7UrF9Tf4akoYgdnsNOobz5jRDCLgJHmh4p_BJvqe-uir6rKLe21rt-asYYVRkJYQ67CaAS-m4n-M8SxWNVB1KurrEirgR4WVCDMMZLCLF7IHcjAREJ4K1y5Soa3_lxaK65NcCOapHx5vMmsvqkVh9sSX7iE1oIFl8ZNxYXxISZt49mPknOErhhwL1UdsRPM2MhlVQpM0opNsNSCU1DKO7-W6UgVop6f8_UKzIosXxswOBrY67pptWPpOlr_vUp8-MfbegMJ-Lu_8l6LALmLX5x0YxHw7HUsR27xMn82r85zni_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌نفری‌که ثابت کردند که هیچوقت برای شروع دیر نیست با حضور علی‌آقای دایی از ایران؛ اسطوره دوست داشتنی مردم ایران فوتبالش‌رو از 23 سالگی شروع کرد. ماهی رو هر وقت از آب بگیری تازست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29024" target="_blank">📅 11:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29023">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=N4ee0PDiN0rb-xr3SejAFhYFc9ohhTOO9eNEylew9SEBzDrZ1wX45E3m5GKX0uFA2t2Lb_-nQZkAz6pskBGMZDdMW85NS1oA9FwRYvQaIzJKoBZTKjiLV51etUgyOeJOsVBNL_IR2Q1BNqU8yIQkYzcyiDKjVisj2ck3c_5R6NV-510IekZzVuymDbDRUHwAzygz3Gzat2aKkg_DljKfCCokQvsxgbVVvC-NNpICPYdTaqrBWsvyJgD9DblrSaHFfWGD19zJWFfE_uL_6Aqmtq2klflrkGFKbM15E3z493iowgxQVkHMPcBvFzagl2BPt65VUDJjtzfm2DbTq2inDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=N4ee0PDiN0rb-xr3SejAFhYFc9ohhTOO9eNEylew9SEBzDrZ1wX45E3m5GKX0uFA2t2Lb_-nQZkAz6pskBGMZDdMW85NS1oA9FwRYvQaIzJKoBZTKjiLV51etUgyOeJOsVBNL_IR2Q1BNqU8yIQkYzcyiDKjVisj2ck3c_5R6NV-510IekZzVuymDbDRUHwAzygz3Gzat2aKkg_DljKfCCokQvsxgbVVvC-NNpICPYdTaqrBWsvyJgD9DblrSaHFfWGD19zJWFfE_uL_6Aqmtq2klflrkGFKbM15E3z493iowgxQVkHMPcBvFzagl2BPt65VUDJjtzfm2DbTq2inDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29023" target="_blank">📅 11:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29022">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">▶️
تمامی گل‌های هفته پنجم رقابت های لیگ برتر؛
دیدار هفته‌ششم مسابقات از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29022" target="_blank">📅 10:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29021">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARSG-dNEl7EGf1pIGV-dATl5I8f73SzHOfoZMSn-z-3xxA-ZIm0_Afevpb6ayf2dljG85XFRz0SIcxdZnPNZJ7sp42oxQe0QRq9sts7cGru1yUVdG4WfwST-PyM3Zo9GpZKORdfsXggvCddGH_WiDSR0szw6TLRRwYbW8fjQ5kL0LmWAPJ9snCrzS8BzoUOLi7Qc6QmRfJTquYi0VUgIRxl3bucRicVJWyMn61wmBXRN45glj03qqizwD1AShAbY-8w93mcC0MmmMZpnSZSrAq3_Gy7X71bUoWYv7NdRGD4Z5XALWNSW99SMpSbqVEYHSCP3OvLYq0B0FhN214Nw0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های ما؛ باشگاه استقلال در نیم فصل تموم تلاشش روبکارمیبره تا رضایت نامه مهدی قایدی رو از النصربگیره و این‌بازیکن‌رو به استقلال برگردونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29021" target="_blank">📅 10:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29019">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIrGM8soarm_l5iACksFMjUBcO5DUGJRBHOv1cimKhh75WSOb8Inv0kGksE8ep88gvXxEvhsaMj9-aUF6i1XJ99Tk3hG4YBPK3yvbiBnBtm1U-f-f4mZc_dno0zRHPW4Qfz0TYiMMCUNzWJ7ZEebCdwR6po5LsifG2uYjlP7d9GwLpCoUQDDNfoT8DCsy6-1HV5Nc-s4a_uhQ-ea4cY8seoLuaS-tGHgdtJGLtzsLIT1QY9mSBkz93LwggUWPMB_wfuKXGqH05d8yo3vB5xc9-UPyYOXqOrSS4ndDJIhp-NvtqEccd6MPy7yG6Sma3wgINzSc9t3xh5muMJ3NWOEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFGtQMBGSea0mPE520BNUsr0f1D-DJiKesQbH7oeSgsKiOlhUr4RcOpPqEfKqi1-Qcf-ra88PTBUDJK718J8H0OMt3EJcOn-2x_SkmEojFushOLJPKytdbTKaKK2TzlpL8Qs_uzGgt9Kg4z2YvVRLXgO3UqyfUF-GjbTjx-4vj3x68Q1VYyjG6EJAmyyhGtg3YFYD3N8etmcI4utFR3Ao6t2ExTsQEiVbIfhKSdsRB-NWFNal_zCwdPxL66YMrKhp2ZD8g_f-XXM90oaVfHcqewXT6ChOlMyKIw3HqQIUxppXrJRq1qht750Flt4BdrhvNv8D3yZtJgdoAWGQKQTMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29019" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29018">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0JhNFic6sChTLAg-NGc2lrEVR8T61DtJxKj-wl6h6RhJQcdvxfwYh1WVwKLtQ1sdcY9Po99Eu8rtxm7Hs2PPo_xdJKQIs3TTZtoVp0kocV5UOR-sN3op-Ubqk0BBQ_OiD28-rKXDBnGsTBi1zblyPwIvq-6CYttw7IIq92Izh9wdRqUw9yfcUfUp-dZ8E4fcuMlYzs8O5rkFAwuI-QYsPoqxn8zVnAlgVwKfNguc9HWhFveb-cPSQ30AAThF8yRJg7_Fl4I1AUHCmLnzc0UcBSNfZ3sYGZT0tcMPfSqSxVg9et7Ukg41l1xi74O7Bt07EKa-nAhM42tEQnpJhwh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیزری‌جدید‌وجنجالی‌ازسریال«مردسه‌هزار‌چهره» باکارگردانی مهران مدیری. مدیری درنقس عراقچی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29018" target="_blank">📅 09:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29017">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSVQqM9uiNzoYF_kFzeRXkoZ_YgOmlLsO-GMVWSh8F1VMCLIWO-4Mf26jxrEI5MQrq4a65yj3MgcmrTWL4ha9Aktwi0owRXRne5G9OezR_04jDQqaIf15UreRzr93ky2hv8GFVE-JE3oKggfoWYkSm70teW26f5deF9AcR1VdXnc2P7xazDSc7-dCIBxDupKlWd5uDWy_gqg14wIszbUznzhEDlMeeWGFPEMUKekehudtPBwwvtsJ2skg1-FbBNbGyWtgTIlTc4e16pXfxgcLMDiE8D6Zw-U4iJFxbyd2irCp5eUve1ssk_BR2SIUkhdheHM8waxcuEhf7YAm8VaKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
گابریل مارتینلی و همسرش بعدِعقد قرارداد رسمی با باشگاه الهلال عربستان؛ مارتینلی در الهلال سالانه 22 میلیون یورو دستمزد دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29017" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29016">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEuk7-HQjqk4q6_kzeeDbRNX0dpk7Jxz8f2HeESf0Gywkaa2NMhjqVJs7dPhznNtXNHzn6LyEYl6YQWHRMfFDy-H06x0tmsLxwEFvrjfhrtzreTericxn9CeRdD8lB4R-MJ6QTITgVIIV2FHsYqzTXLq8OJlxvn4tWJ3vk4BcNGEphF23Cn5vVHkNVB9p_A90I3sThpO815XhXXrWyL5Yd6QBCMs7PD37phJ7JVGnUgxCeAiNWRS6UWTmfeXW6sNrV2SK9sXQuOU1TbNNzkyrbfy0-kuBgyLS7CGUkTlBPbIWU-H89XR1hRInUZiddsi87za3S_IdQKfedK9bbs5Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار: من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29016" target="_blank">📅 09:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29015">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw1jHSaHCWiy4kjat6B3fhOjVOPWHzw27uWVAEcePbyCHb_fITuCVmN-6j12s1gdKMQ3y9skYD56emE_8i-5_LFlGBF0PLyqe3LX970do5fkIeHbBRMYcVXeZt8eO91MiSs9jm5t6tWfL7nWgeBq44YIP8gqO6GF34exQuzsvRN1UBWvyzYaqLDdod3rsWSTiXwdgCOuBQ93xEbD9PrLX9Vd9yC6KkriQWnf2vVRPhX_5gRnDGD2zGnLRg7qCkqEUoSOks1vKb6MjHmfExJ3IVKKFshG28OkJk8VLnrWlKmPyGiaUETRd6n3dnlG7x8x4tdLd6wc1JiCTjHJlbGktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی دو تیم رئال مادرید
🆚
بارسلونا برای الکلاسیکو حساس دو تیم در روز سوم آبان ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29015" target="_blank">📅 09:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29013">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmoOssu_UT0iSxvqZ3tW4asSKxOkJU5GyCe0VaOW9Q4Po048_UqdvLoeNuJmUAkr815TdK3vfPtdb37fRUMWWGxTA1Gr3LYSImHY2JknhdrMr0Qj_JMVvgNFoyilC79O6RtbBgRC4WdXcxFnQACtsZ6GtKPdHYmmfcvD1TSyvx5y9PJoHcLCDEYDCzblfMTJNJyXlM4sOh2a9ZTSV2hPWgcSp1gosW-zlvYLVl4BAqKdmURmqCCixIXJAS7znQ4Rc7XOjAlYnDtb5NuUbCa8f3sbwos789DGHMIxpG5XAaj5y7WeXrbdL3HBn8GRskccqj4u54hdIh-mUoD2XlORdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از دوئل‌شاگردان مورینیو و پیگرینی تاجدال‌لیورپولی‌ها باتیم تازه‌وارد پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29013" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29012">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbGNZYM-d6miezXke6U1VKqFcGW9EO_m9gy4idipMweevVpQRPFS2-KohpMZdVl7GyhtrSvP9Tx0BXTiOIpJHIQWBM02OXp4wECAfj44nr8WwRzDzWkpGzk2SSwIvLmoLqRyEgbEIZ_7QGLFcHk0NW479DpH4M3Wz7PC-i8JLHzmRKjhVAK9GyHsOZYxffKlu5Ssnmbh1ULn7bV4THJajciHN7J-b180EX07tDaarNYgQYYWu6iPDH9WC9l5pp7EQPbuXbzMeVypn3wLQeHl5HPH2AjnzcHWxWBDMbdqwFYF0rQu3dTJEhtBFkhb9dFAv3fNDp9RrsgUr_jaToe23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌ دیدارهای‌‌‌ دیروز؛
حذف یاران نیمار از جام حذفی و برد لخ‌پوزنان در حضور 64 دقیقه‌ای الهیار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29012" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29011">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=OlUGfQoYLcJvV7YWRE3OAkpuVQXKlsAmBgmct4S118DHQtNcb4pzTtGI2vi18kIbqz6_qf4-9kAsipBJ4lWsJIiav6f52kuFX_0L_YwhUZmT3Vc_JeEHZ9PI2DTyzPSkMl6KJyr9vbjA144WxKwX5MD-Thsx3oTRfMU4w0_umgbpferY0zu7b_u3-81jaG0btpSq5Xifm_lAx8v1jyCbuTDYYZvfqlqAxcJrdn7mWy7jxVYo3od7jf1bZZJlqxr65YjqLxvkXKN-ZV9PK2a2_GEVbZzMxXlV-OiPZ_fNWS7qaxEArnJyvSoAHDe5GSVWmPmbYeGDXvmJOZeFd5HQ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=OlUGfQoYLcJvV7YWRE3OAkpuVQXKlsAmBgmct4S118DHQtNcb4pzTtGI2vi18kIbqz6_qf4-9kAsipBJ4lWsJIiav6f52kuFX_0L_YwhUZmT3Vc_JeEHZ9PI2DTyzPSkMl6KJyr9vbjA144WxKwX5MD-Thsx3oTRfMU4w0_umgbpferY0zu7b_u3-81jaG0btpSq5Xifm_lAx8v1jyCbuTDYYZvfqlqAxcJrdn7mWy7jxVYo3od7jf1bZZJlqxr65YjqLxvkXKN-ZV9PK2a2_GEVbZzMxXlV-OiPZ_fNWS7qaxEArnJyvSoAHDe5GSVWmPmbYeGDXvmJOZeFd5HQ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
ویدیویی جالب از آنالیز کامل و دقیق دو گل استقلال و پرسپولیس در شهرآورد 107 پایتخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29011" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29010">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHUELOQVr4acrCYXJg5j84wsGP-j4uN3FaCon6DXp7B4FNOrm9oUCZHKI3rjxuCbvH70_ualSVvApGuxs4gVLx6DijknzDSuUTmDlVGYSst1ULXbCn6TYiTDv96kiN9ZqgfBeHEO8Suz0xLO1ZNNnZRbde6xMi62CPt1czrMEdbQWHn6JZSj5TbvCAy3Q2IboIDtRawerptfmAp8i8wjAkn3RgsQxEyyjuPBdGVzeHIgUNy2F5Y7QydStoO2D8Qm2sIqH__CiHD1wuzEMcaywOFO9WP04qM1wp8hfxyfnxgRDlu8oGKede9BK7wCz7r_gOkPNAJLUerk-g7BAgThxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29010" target="_blank">📅 00:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29009">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAYn_wyjCxPdrUQB7M7cOEui9ecOaE_q1KPqp4Q2mK1IPKOW69QSPC2Hug_V11tr5hnjZGmpCILQBaZqd6hulydB8s9c7Tp6YD9JNd51afyVG9ypqXwQ4k05RT9DB42ei8-cZJHo236fO29thpZrwOlbtPOAu1TDgdUxuoQ2gR7FMZuNjLfoNgATRMwAi2C5t6gX2WbAePRWPKBX2VrJMzNu8ZEmZONHQat3dg3FX6U2sqSRSu3SVhOqIq9z4a39BDrTUXfunDgnrTjh9PsxOeZFDRWZE-_zKEPfXxhXfemEfkR3ABlN2xakdv4zjnk3-TPB6pFHBhpFuwb1nxW1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29009" target="_blank">📅 00:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29008">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGWQ9uSfTQrfaCcl3odZuVOoSPPWqBt-del4K7P7WYnKHOdlk7IWvorCKhmh3G-dWzTLff51XSzKyGa4kfUz6Il7HGAhZLQem6xoR1r0gonmF2DYUb7aJ5W9YXZ55KZM042Ml3TwGCwtps-cGRKCzLmf4TjhFoKasv5nzypflbdumTPfWJ-PJgewD5Og3CvADSpLxjoloszt_QJdB1lPzYuNkY8qtIHEBDzQyZ8eo0O2ktvpMQhYrdpAt5yXvnbIhIl-bV5bt-ZkY8W9xeRFS8GVx4pn_D8OGCAIsQA-06DRLWpx4wHNqT7bpP558zy-ruUop8EabxFz-Gi015-YYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
مجری‌ویژه‌برنامه‌چمپیونزلیگ شبکه TRT SPOR؛ که گفته امسال بارسا با فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29008" target="_blank">📅 23:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29007">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbTC4OFn54q8flDMPEPrxzjGVNyGuz_rauj_RcbUaG3sAMM5aODjp3uAGtB7x7rE7-XdbIwVrbqWdMPU2UbMArXdcwiqJ6w5zAwHtTfq3Dx6nhZorSVpukgjN3CpW7MNhMeXwQXOFr-sR1BAZW03HNkDRoeZDpUP7bGNFGhdHZ9nWOOFr4wdBbo6hn9P6FSwbSc60UkGCGSSor5CfroI3wIfzgdbDR-nd1RKjIU0jX5LKjFcd4HC0FGOFOmGlsZ9hRj98hXBB8J9ATF0wJz64FQQHU98EA0teT8fupEkux-MKrLx9OpFJno1Q0g1kgf74Qm7qJ2DxEy-9qOISAVi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بااعلام باشگاه بارسلونا برای نخستین بار در تاریخ خود به درآمدی معادل یک میلیارد یورو دست یافت. این میزان درآمد عمدتاً به دلیل افزایش درآمد حاصل از استادیوم است، باوجود اینکه تیم بارسلونا مجبور شده است تعدادی از بازی‌ها را در استادیوم یوهان کرایف و با ظرفیت کمتر برگزار کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29007" target="_blank">📅 23:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29006">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6KrUi51PvssNCoXJFyF-8Dt6KTAf5m7UnIrmLxWgzJ7WY0vxmg5tkRcOvW3FothmH1Po61-_LdPufYasu9AfuBCo7QzMDwnRvm8QAjl_LrxP1qS9FEQFvGM83GAP6YuyDrALyWfhCRkxGsVzX-HlZSxOg9fBj-hpWYrIOjMF2f7OJMgJ236NcVa_32U7235as95vu6X3SZoOi0xQ72mafzuE32qI00ebbr_8uG9uqY7t4ps4mvkomyL1jLygv7isabTBh-KX7eBPhdwDHr2oGWZyFUL6SHvzb7NQ09pf2OBM9m_xlZnnHdd1-5jADfC52LZfoARhPaLx0MfUklFaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29006" target="_blank">📅 23:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29005">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIYJFq2mc1iPPw1cEMu6-OA0CgXw4La7aVWxv31Y1jq5T567yjmSqFyO-MMZLGV0SfaKrrnmxPCmwePNlrbW1jv1Y1bXZogRlyUGpKgOUvad0tn8u-bQTqkKhWfV5OT5TFz5P8YLzCoKWLVRc89QfwYf-fX_qJBdznOo61hB67Fat93PzN0nnyPyEnrahNM0ZEXOOTBLS7XeDT9v78LLY2ZCFv4ZSKwJkiV9ZtSRgWt-wcM00L-QSdkS3ez_-95JOdp0zqBg9fgr6ooGrfYG7b7-ZrHphIxriBt45NL074XLKJfzaKwMkaAAELXdKZ3dn7HfTdi7KB8oBqp_DWwejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇾
👤
تیم فوتبال پافوس قبرس با هدایت ریکاردو ساپینتو امشب در بازی سوپر جام قبرس به مصاف اومونیا رفت و با برتری یک بر صفر قهرمان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29005" target="_blank">📅 22:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29004">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNTUP9AtyfB7HB92fI9dYcoMK2VXdTFfMBr5MfGgYCSrQ5K7OCcbs-_I5X5eFnr7THtepY8JWefBe2Ty2X29szfywvG3PXe5lkGwJkvGFeOsvCQWbC1TwskS0YHKaZLnyQ4GE4SCOMuMuGQSRLnZ0ugh1YLN5WdcSxAm6kokaoyo-YOwsPqGw0S0JdGKM9HQgYbKisBrLcvtwDI-2CxkoAaPGNTfEYGDWVGiIPk4mImmwgCWNIaN7yW128DajPhVqI0CMJ1EghTZAR6MZVkyjhlKeZ3PVtMvRMpFivSINcBk41ZQylTs2rLF4zR4UTcjVwCBvyDePOkxgfC8GQVwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29004" target="_blank">📅 22:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29002">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5B3WAIa3iyJe3SSFqX85vBFOxznBS3REwo3ay54cXehot3JQVeB0t9DfQfZC6G2pHfaTYh_pfyEjfthJtBP2v5ROF_mqrc-rYqAil0wvfePJMN1K_7b_LpG50D6oJgtx0QAA3CHEBUncGMy959aSqT1pZY_a5-Dl5N2Gi7WW-QzPl8E6cbhweh0e-ep1QytFsyk1st6-IOfnDMTYRRvxkN2iHaq7cNRP9d3s-7sff_5xAqRDMtkkMOJz09m-fZVDfUpbC79wxqUyfmCj9d0lSoWuuzb27lkC6d2DN7pU8FuKHlwVaM85kfQhyrYKaA5K-7BM7xXhG9FAsFyxD7edA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOsze3nmtxGdMDN7x2_EJ-S0xx2buj7k67Ru8h0oR0Rv5UEsVtZgmtLHLmMwNS_-RNMKtD2GFGujhVzfmM7kZ5HsUrYzlnOrExYO_gRPudOXSYxBTjUWFApN1oJ9yZN9l5T4yKBA_qKFRTNqsFhF9_pAUl-ZTwm8v6U2-Iz8isDvypcANzzichd63aJ1ygSVhomrSLFhY2wxcjnG2fqJQMPkGbzfyDnvgDWHSepWSNTEA8TPs5k7or9nHpApQnthfmiOLtlG70EWfrHxo_-4pgm37bcTC_CoCF59Jbne1gbvVu7yWt7pMPBpddcq2b6BmNIPljIUf7gIyvQ0IrcqDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29002" target="_blank">📅 21:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29000">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VgLZpcxL14Wh2mcVwQHRzhlk8aqz7EiEhgfb81WpFU4EImO2gUX0dc4hHcngCk2ZUpf-xFAWsFf0tyoGRx2-_b5ENEaCETz0a4-2dIodNzBbJBfu1TCFfsNZtwIdp4PO7V1xaRs1NyDxpTJYP5ItpZ2DnUHJ5j7nvVBoaI74ufCGBwI_qij_pacjnTF-V19cAM8nwrE0MsaKPOIUuzPx6gdu0JqiHo2HV0IERcfuo6UEN5uW1-XHdzWm7PtKF9UXKbHd6uozpo8s5vontFup6rf8D7QXUQ1ny9vcbE5yLwAJnfuyTBQXV5ryKtU7jKnIloXQX_AMpTWn335nnFgKaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvgHXitoCEwJV9u294NgwSaL7eaJo9p3rsD-YprOldRpDsg8wlUDCfSMWVDP_ZvfdmvF1npn3U0t4N-42IzJu5zdTkviWDSxrY1KWPaMqUqGXS6dOiuwvlD9GIpYxzlc0ReNYs4TS9uHP2oINbY3VrjIv10UE2srpAmW2DZx0k8rS3_IlVxCgRl6PyaDnNa_UN_ugl6bxIkLlTjMEqBAMYDRAT8FRabKd-uc-8Quw_zHJQVKJmeO0buhYv19-mCzNc3C5FRSocGtOSJDtuzb_-w-E3J8kV21X6jSzlWWwDqJeZ2_LFyqsKkGXY1UetrrpXIW7TU4IfoM4QUWgJeHBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه‌بدونید 3 باشگاه بنفیکا، منچستر سیتی و چلسی روی‌هم‌برای‌جذب انزو فرناندز ستاره تیم‌ملی‌آرژانتین 282 میلیون یورو هزینه کرده‌اند که خودش یه رکورد برگ ریزون و بزرگ حساب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29000" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28999">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j98sYOzMsroMOO0sJC1eWZQupNsnDldoSc2oNM_smKicJPVs8TcAeCpCmpziLEltHhdNbhB6BFR7bT5onb8cip2QoeWe2UGUr4InG40SYcQhZeN6Bl92yURJZPSXR1E3D2yxWwtpQtN10qMG_2UpMd7po4kr1XLEQ3kw5J0PiRfRTFLDqzKRCrvt40Cjc_ZN109dlXYCm1eijuqDOPkvX1B0iZEXrfG42JCzOxOXagts0QL8e_H_b_cHipfCxRAcMXZRQS0rjq3fFTU4KaQmCr2BOJiSlz3U5cOug6IMjdAzYi1NpNjtZvh_rA_4F7X_3RdH5CIN-JBOfqzvhPb7ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درکمتر ازیک‌هفته‌باشگاه الهلال از گابریل مارتینلی و اولی واتکینز دو ستاره گرانقیمت و جدید خود رونمایی‌کرد. عربستانی‌ها روی هم 150 میلیون یورو برای جذب قطعی این دو نفر هزینه کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28999" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28997">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mepYh3qCxps1RnkFUsXc7mkt3tWENEw2WUwW8CP6Go8VUCCqm0UxTjjGibbRRGYud8IobgDsot1KMuYaBI00WnioodhtbEpZjhbclyyCgNXshj27bnWoo8VxwpgujAX9Gezm6KFCwIaXgyBakNw2zmt-EPdNuPcmjQgzZS0jSo4MfvcK9Txcx8ZINrzy3iv1eIBKQ6wnykpnW3ejl4kuzkPmVmPPdHf4BYdsJqKD5ot6TPs6wGEh0B-khC2QyYDP2GF_g5rirUzueVG0QYoCnr5fGTkWffrKLLZ3mNVyjmu2_ygaP5qgjtAZEuj2tYVbQ_jjy2Dv45LiDuJEoxPzWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28997" target="_blank">📅 21:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28996">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6XezcO5gcfRqRMuISjE_ZLLj2Cg-QZCsfwS9qfhf_qP2KiaPrGjn22Vk_eyMFAZ0ghWonicq08ZMQnohNEVw5hu8wttwgKw6Mexvq9-EoDeG6O9h4wShGQDIkf6lTMNwppVQJHB3j9pj_S6tmSNVzKfTibVG8J85XB3Z9_xNaXUcMHchAVa-qEj8aiBoSrnw3cA8Ham6gz0RvdzemiGqXDtnm8ndxCrU2JhJyJPJRknWiLr8pTzh-Efe_GOYiaANhSjPWQ8CNHx5ibO6-b6c8QO_2dgFpGoM10sGBgJSj6dQ_1rHNiso_x2GXlTzKo955yAqDnJ1Obxd-hGYJDKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28996" target="_blank">📅 21:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28995">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=F9Vx_KMfoYB6r7FxXGx2xfs1D_RAOkJYGhwtkwhox0kuYOahHk5dP9NXHGk5JD3MhdC7M4cR6M-a2a5wjofSvvkuzk6XviEYTzBIYVPuvjjMv57ZiIh3vC8BCjqxFKxBAChoUxE-J0n46iA9u1p60BEfXJcL2PL9pVvi39jXImQtCmi1inAZJWRVTcablvufzh3zS3_qEKiVNjId7BiYKlv67qlsj2n-JlCd0RDPVr0Xh_tavpKWcRFX0QS_hTBpQA1Th5ZE3n1KbPyktMO96_nGyWq2uLLTvwoCfApqvRtc1z4QGS0bH_moh_nr1WsVDmMQDB21Qevk8I1k2NMmtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=F9Vx_KMfoYB6r7FxXGx2xfs1D_RAOkJYGhwtkwhox0kuYOahHk5dP9NXHGk5JD3MhdC7M4cR6M-a2a5wjofSvvkuzk6XviEYTzBIYVPuvjjMv57ZiIh3vC8BCjqxFKxBAChoUxE-J0n46iA9u1p60BEfXJcL2PL9pVvi39jXImQtCmi1inAZJWRVTcablvufzh3zS3_qEKiVNjId7BiYKlv67qlsj2n-JlCd0RDPVr0Xh_tavpKWcRFX0QS_hTBpQA1Th5ZE3n1KbPyktMO96_nGyWq2uLLTvwoCfApqvRtc1z4QGS0bH_moh_nr1WsVDmMQDB21Qevk8I1k2NMmtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28995" target="_blank">📅 20:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28993">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TM_hEQ2a2yJQ89DDm1VEkKnarTz8O9pfEYLJZYezgpZ7YVqVjFAuPZ4Gvh4dlP2SLYEsa9LK4Lgca2xaLs9_ZvJ8qNpn_h6RgOIlExDEDnAj-Ali0j6f4Y0zYfxJOH7sKimRRhk72gWpIZnjUfU5JD60V3OLrQFODTz1N1p_EccppsDTKWDUuiiOqPmoIWdf-71zTAkLQ_AVCopymj_HdCWwYExJV26JIw4vc0jHYF8qT9hJnQ_Frr5IIMlsXf8zdJ8r2FuKHaxZre-LohvPwJwRKrkpdI9O2PnE9EorT450V_VC-Cnw_TkBb_agQOMOv4mDcEHexOUqyH7s0E9WVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پوستر رسمی باشگاه الهلال برای اولی واتکینز ستاره انگلیسی جدید خود؛ قرارداد سه ساله امضا شده و سالانه 20 میلیون یورو دستمزد واتکینزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28993" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28992">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_Mdh4bRxmTOccUCUVOLiL-Jc4REJLL94ZlTIefSQitChTn6OI3vnCoDIj5MBsykwE_mZqNW8nFE_9nkctq6mH45jtAafYT4WFOhdFJLjqmfQgsQdXvWct5JVXMm1HMAe3KrE1ikLiV8T9IoIk9YwTECnajOodu6KcyJ2GFFeR8u6_mkUp2d8_smkELvOeWwTqp6_80qikQWR45La1puLXRvL2fbmT7adreo_84pHn8gIteRPHeQGEP5Dvn6GeCdcSvXBrAFJmyfGIJDz93_qWmodC1iikPma8U4Awc-44lWLQ6wDODIBOv5W9cx4siOAYCtSBdM5iUtUTw_-4lcAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28992" target="_blank">📅 20:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28991">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agms0Gx5HOe_jZftkq3y_G927AJ3n87TFH51v_XLwk-nY7sa5nkDDWiOk1X0WpXCxMdn5TMBG_NvkPXsL0jHcjPmNBM2zTr0f5CgtLwCQE0SZtYBH1g49EpW_xMRPdm7goV35nwS8QHPSzcs9hIifdRzg6tQuD-6VTjECOq1dY3sRqPEmEDxA19k266v5niCuWCUEbNT__f6kKUr6pyRVm4xC4mbff8ceEfZhWQcx1dBt-JoHLgUVhStETKjlJloWsrCBCCVjZwfMxfNFtib2fYkEg3Jipu33P1CtbA6n4Hoqk7EyXLGdpjol_o9ezFLRO9Pbz56pOxOe1uwD3ixPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌باشگاه الفاسي مراکش، کوین یامگا وینگر ۲۹ ساله فرانسوی‌سابق‌استقلال به تیم کنگ آن هانوی ویتنام منتقل‌شد! کنگ‌آن هانوی فصل گذشته قهرمان لیگ ویتنام شد و با پیروزی در دیدار پلی‌آف مجوز حضور در
لیگ نخبگان آسیا
را دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28991" target="_blank">📅 19:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28990">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇦🇷
ادای‌احترام‌فوتبال‌آرژانتین‌به‌مسی تو دقیقه 10
🤩
بعدازخدافظی لئو مسی از بازی‌های ملی، قرار شد تو همه بازی‌ها‌ی زیرنظرفدراسیون آرژانتین، بازی‌ها تو دقیقه 10 یک‌دقیقه‌متوقف بشن تا مسی تشویق بشه. اولین بازی، دقیقه 10 ولز سارسفیلد و بوکا جونیورز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28990" target="_blank">📅 19:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28989">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2uxUQam64rSl7nWahm3ifJFAqCRBi7S7w31QYmtwSAr3ojm5IV4zOEFt-oP9sdWhS_bB7hK3u9cufkxZtlSaCNE_MLI010bWGoQvzOywrDoIpKo6bv6YI7yVfBdxgmofU7mZaeOCUUCDThWQLPwiDkcVrwIiNEsPed0hGSqN-4GYuBtJOrlOqx_IVJEHsRBX3hNi-wr2Ji0-R55LKp8XnM7lLSHcwMAGYD0W50ijU5RoDp0avheUQBt3ZhP15nIU3GZuFu6OnsHczlMJni2VjVkI-H68ZIX40IwAN1lfeHo7w32biFZNY3hU-cTy7L_N2Y_7Fs5wZy2YZyimglOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بانوان هوادار پرسپولیس در ورزشگاه نقش جهان اصفهان در بازی روز گذشته با آبی‌ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28989" target="_blank">📅 19:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28988">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=X5a1KIP457ZK-grWS9Qr1BVwVLXBD8GgoyCQl3faAlPzoSk2EfGMerapYW0z8alu5ozs2XmpirhoNWxbGvsHXshzTAsZmfsTvsORH8NECA4V8VLvhPkc1qEodJzSa5wHVjVSKcS_1WSPZyDhSQZTMr8cVh4UpFM4RYxj8ur_DhKJHaBDegleZdH4keKfDbxg7nbdxdHFrTd10flWx6GMuuNiC8W9mhL56GFe5dKUgcLsnrAy3q6smRCQdcPMJX3ISSm-lYQNr16xF1_ILy-zUF-7WfEG38ALQ5y53wsnyvGT3FDHXvUmeG62Eabv2S9_-TI55Fyss0CdEc1bk47wig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=X5a1KIP457ZK-grWS9Qr1BVwVLXBD8GgoyCQl3faAlPzoSk2EfGMerapYW0z8alu5ozs2XmpirhoNWxbGvsHXshzTAsZmfsTvsORH8NECA4V8VLvhPkc1qEodJzSa5wHVjVSKcS_1WSPZyDhSQZTMr8cVh4UpFM4RYxj8ur_DhKJHaBDegleZdH4keKfDbxg7nbdxdHFrTd10flWx6GMuuNiC8W9mhL56GFe5dKUgcLsnrAy3q6smRCQdcPMJX3ISSm-lYQNr16xF1_ILy-zUF-7WfEG38ALQ5y53wsnyvGT3FDHXvUmeG62Eabv2S9_-TI55Fyss0CdEc1bk47wig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماره 17 منچسترسیتی که سال‌ها بر تن کوین دیبروینه فوق ستاره بلژیکی سیتیزن‌ها بود به انزو فرناندز فوق ستاره آرژانتینی جدید این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28988" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28986">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILqRa--zijMgNcCAGYvmo2UbZkLfCCFHS4shkUs6DoFmJ4LGYjTagDUZl_SpqdI5wxMHp48eGZHaGtsJ0uDBzDaw9hkXlTEtZnUZ14z7aFAoEGUVV9snAO2BVEj27Y2kptWzeuLXUya_VrXC_CTw4BuBdC-JB2YUsN5072qVruJY5Jv7oHMw7C98GdRN1yEJtFKoIz2rmj_df7ZEh_UuJ2JHEF7FvAJYQ7bR1b1YMRM7XrrTmECQy_TaOpsYLaBymxJjWpRDexj6f8mhNlMkECWHqyVz1McpXXE-gxNk0vG41kYvL03XjIi5y3rPL_7KS80VBPkzyFCdXRuUBw_I3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=RSBnhzpXR1BhIwNUzViLIUai1aPewnuapDOZ_7wfuwfgI3AyX1aEhqvZ2-qdFfTjk0-UIiHkakJ2bJuDwBP7E6ZoyR0OXn78d6iqcsNbVfPyJyUsyrfRXosRpDAp15RGRBSuozGxhm_o8z46CaOcU4IrfP4jPtOQf6Xt5-sAtLxSqftBYymN5fb6hdSozWLynkOEp9cmMbC394A33mHyd1yTT6-xCU0QcXYgN_bKksORfoFAqecYIjkU_hkJCDkuspUPzQoDaOq6XDAKPiLux2CSu2zwbuGEeHTqhv3PxnUrRzljxjtF1U8N2d2eRrr4rO8dSPx1JAt1WmA1JHhvEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=RSBnhzpXR1BhIwNUzViLIUai1aPewnuapDOZ_7wfuwfgI3AyX1aEhqvZ2-qdFfTjk0-UIiHkakJ2bJuDwBP7E6ZoyR0OXn78d6iqcsNbVfPyJyUsyrfRXosRpDAp15RGRBSuozGxhm_o8z46CaOcU4IrfP4jPtOQf6Xt5-sAtLxSqftBYymN5fb6hdSozWLynkOEp9cmMbC394A33mHyd1yTT6-xCU0QcXYgN_bKksORfoFAqecYIjkU_hkJCDkuspUPzQoDaOq6XDAKPiLux2CSu2zwbuGEeHTqhv3PxnUrRzljxjtF1U8N2d2eRrr4rO8dSPx1JAt1WmA1JHhvEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا:
هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28986" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28985">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huaULBsrxl_07DJ3auwceciRJQ4PYd95I4Z6fs3uTDDUY88lCkxl1Pfa9hfpiTRQzdebTEfskwiYOB4E_Q3h6o4Dn0aBfGwKuSP3kvFUCrZ-hMI9r3Yo-qEij_PvzX6ou89oz9y14lnGj9cZ_IR7H6fIOOnlFqI0uAULuELzlw0Y3GszFubsRrkEStkWERuU6a39bxrXpO0Auz-TqXQIAzxb262ZmJLxpXj5y_N0RbHu9ia-Fc8oKXk5rU-DXl9mTPZMfAcdwvuvfT_UDinbTPCZ51F5oeymJqbU7V18ki6gTfqXQmGNvy8Tx8kgihLVTyunGnvOIFAtrEdwYUtxqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28985" target="_blank">📅 17:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28984">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWygRpOOGkhMB67cpuhbS6DsYpfXVJN2mdlzURDYs-uGx49954RQl_czhBPpz9RhmmHRaCqc9UDRgS6_30bgCstsLPEHrHace5jikomovd7EP_GUNO0FDzv9onmg2H_TjNQTZ3WGSa-AC6pDlvopFFEAqcZkxLWq4wo_FFsTeybpb_LTrQbrHTFnWePk3b7vZLsCm1pupGGruePSZDI_BX5d8bA4-_oCqeh2vUGfETMV-jHhsmxoqdD87Jp7_0ZcimfsTfvDpG3Ngxihz9qsZY6JZ5LHjSFUXN10eSXfdiHuvKBOaIrUQiK7xY6mWtJ_VzeJ1cUOlVMHUPNm9kHmdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28984" target="_blank">📅 17:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28983">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🔵
هایلایتی‌‌کامل‌از عملکرد ماهان بهشتی هافبک تهاجمی جوان ملوان بندر انزلی به زودی با عقد قرار دادی پنج ساله به استقلال تهران خواهد پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28983" target="_blank">📅 16:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28982">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0sa6B2R0oqRdXSupLwOAvSUNSWEsYiqMhlzbou2MqFgmFcC44x7ZgKysefBuDyYL8ecTzJvQ6Xr1sjXUuXgNdakJAj_iPtwc93UxrB5CrjHqSVzyaMdS0_pW3OG5hgaA0hPk-U78t35oQ-7ze2x5I_gqhux3Nfzkh7u94fl6B7k1GZsdH3fgsmKXE5OvFVuGtrMJ-JvN4WwYLBY3zyK9PPQJt9iJfxViPH2qptcjtJwCr6TwuQZKI79BV3d1b5rlzqYcy-WxVC_7pf6zaE2ILf99PebUFze-LfJB0vqt1gUTdWQ2DrRa5kfcViE5P2aFvt3f_z9WkDkF28EZO3Jug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار:
من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28982" target="_blank">📅 16:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28981">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjWYj4SsgehTpSbeRoukynuXu79zjYosBy7ET4TKVkkfIW8C7jLDSWuM8HOUgqrdah3HX3Pr6wAgRDbsMB9TpynDiWzM6aqwIjtOqox8Yh56fMAhj_aJcgocsJs4Du21PYAjhg0J16QJbCRhaopcJB0HKLOx5qJOevIvvuh2O6CgXgtdnvJsTibhMJ-66bjbAz812oAYJuh6PFE4hOVklSQZnQOt70QoIQc09YNaP2rsF9s50ElWV9uUUdPzJfsFhT0_5K9OH7lnpWNqVep_XKDGqpOcRIxBMTwjyum6lNgyB9CJSvJMb61DjWe5hHr3sp1MRZellNYFLV50Gf2gjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل‌گرا مدافع‌ تیم‌پرسپولیس برای پنجمین هفته متوالی از لیست پرسپولیس در رقابت های این فصل خط خورد. درصورتیکه هر بازیکن خارجی 60 درصد مسابقات به میدان نرود یک سهمیه خارجی میسوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28981" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28980">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqwQz0PlNM2rDr6Snlg-AFycqBD5G1ti6cSrK9Gq0uh8Wo1rvtbBh7UxBfj1BTyb22qOw6A0_GwGWdUds6qDSXeDRdi142S5sVzyfo47vfJo25ZWXY0MbO3ogi25xEpygElWB8vD8mLrLGVB1ftXoK3gUlwPl4DKyU7dTJu6Pv5KKjgBY0jNPpnCCGs7HsZYTq8s1Td8_eeHvpGRWpAMZlcrS9aG0Bd-MXr3Nzm-vZskZeKwfymeJnHTrZppRvhYGuwpnEmW9Vzro4LTC9c_7BfcBVVwVPK9fGORs9bcsEvR_pY2ItGe2Vny2gZbAEvGIRF2IM6_soOHigYYsP_CNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28980" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28979">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LieopOYKDmvi-_ZUfTygGbJdWzOzqlAaEnua2mt_oRPIVUielecxLWqi15gQrF6AIwWiOUy48wp6G_SseDahf92-uxmW5tYC8m_K9bgsLxN3tUCEmr8pLRHehNBu8VtLO7-L2lQSIHNCbU2wKwB3ibpSRY8OYFmNT8_GSE2A7XHLgZGYFm4kQwtAMMUhi2_0IqT-A42J7NjjJNtBl5j6JjDg4SuqxcsZqEN3XR08L4LUauuvFo1o1ztktCc173UjuzjE_K53uIpckYBJr89yxMtXSKH5MzAzmgLiyHZ7qXDgOULH0voBzLr03-PDXcQBdyc_bm5s8_Fc5ur_r9l6eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پرسپولیس با تساوی یک بر یک در بازی روزگذشته برابر استقلال رکورد شکست‌ ناپذیری خود در شهراورد پایتخت را به عدد 20 بازی رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28979" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28977">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e310c473.mp4?token=THc6H_lzfrPaNSjjq2hyANYFgHIaAA0mg-ZOAQwQ2KCQhE9pIMjpRJRzhnwb4CAAgjCYAhnEd1bZItS42_4FEXrd3MpQSz-Ey02U-VI_bzRhhq6tScPPF23C-rFOYJWG77-fKFrFb38ImOAcCzyngRdKYz1v6bwmjPnsM1yoYyIq8HHOkrpbYNWLcwlXCaa6nEXWnuoKeZWCCDaJEtBDFQn0Hhafo_6lSdIynvb4D8iqwlF7VctsEWm0dRvxKsn0AKVR430pOzTycs1KJJXGttcoC6W_n6zjEN1KKT2l939gAlxHAeroTlNdvGpCkO4xVWIwxirNxX2Ak8BhSyMqUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e310c473.mp4?token=THc6H_lzfrPaNSjjq2hyANYFgHIaAA0mg-ZOAQwQ2KCQhE9pIMjpRJRzhnwb4CAAgjCYAhnEd1bZItS42_4FEXrd3MpQSz-Ey02U-VI_bzRhhq6tScPPF23C-rFOYJWG77-fKFrFb38ImOAcCzyngRdKYz1v6bwmjPnsM1yoYyIq8HHOkrpbYNWLcwlXCaa6nEXWnuoKeZWCCDaJEtBDFQn0Hhafo_6lSdIynvb4D8iqwlF7VctsEWm0dRvxKsn0AKVR430pOzTycs1KJJXGttcoC6W_n6zjEN1KKT2l939gAlxHAeroTlNdvGpCkO4xVWIwxirNxX2Ak8BhSyMqUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های علی‌آقادایی درباره تقابل روز گذشته دو تیم استقلال
🆚
پرسپولیس در هفته پنجم لیگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28977" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28976">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9de6749c.mp4?token=bE_NQenJKOR7miJY3TX2n47hPYFb9lHXF4yq-ROys4wCrQRJOcwWNrFFXPMhJ5eytbwFDDnU0JlO5gM1jKqUj-vcZQRALR84KJrjDP27Lko_JMM-iKIw8kmuea1Zo-axWkH70zS5BVlzSEI8zBwlKbMcwlmfYvqOOvSc2XMUgW-Kfd0T3inIuk_IyHnFtA4RorhfajJOBMNFkikqpq3BrrjJNELJsAIlPG8qCp_oaaaG3QhbNJMIH62oyf3ewU0UGdHpO__YBC1uaP4bN4XbZQ4GZe6bDsVt-TbTHKuIo4ZrsVnXQ2iYagbtUp9HtPEFyONf_RSHZl8FbkUlocAo9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9de6749c.mp4?token=bE_NQenJKOR7miJY3TX2n47hPYFb9lHXF4yq-ROys4wCrQRJOcwWNrFFXPMhJ5eytbwFDDnU0JlO5gM1jKqUj-vcZQRALR84KJrjDP27Lko_JMM-iKIw8kmuea1Zo-axWkH70zS5BVlzSEI8zBwlKbMcwlmfYvqOOvSc2XMUgW-Kfd0T3inIuk_IyHnFtA4RorhfajJOBMNFkikqpq3BrrjJNELJsAIlPG8qCp_oaaaG3QhbNJMIH62oyf3ewU0UGdHpO__YBC1uaP4bN4XbZQ4GZe6bDsVt-TbTHKuIo4ZrsVnXQ2iYagbtUp9HtPEFyONf_RSHZl8FbkUlocAo9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسین ابرقویی مدافع نیمکت نشین پرسپولیس دربازی روزگذشته بااستقلال خطاب به محمد عمری: مدافع چپ تیم استقلال خسته شده دریبلش بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28976" target="_blank">📅 14:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28975">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbA5IhNfTfzxFH17QxlyKgzgKVhzLTDpIQqO_AhmXfE7-ZQyVD-QvZGftHL8dkTeuVldl_Ryxv2pObTZl9TwkwNTuaESuYZCoUgwET-bfL3wRsc2PQErbkJYSk_2_2WWR-nUczunS3soMicZgo1CR43j6A6ONo1RDwA-oX5pray3gIJ0S3qlRr5ZEdZbrP1DmrYNGJfHEGKxA9tfn0ZqkbPgGJSI2lhBU1avY111iBaya3-SshCOYLi-0ZUu4wqw0dbqR6ZfKUuDEkyjr8sZ2f2aF3-eYSKkI_eqVcGyAAOwaQvBd5MDVeMN6BsiqUf5PDa2zAoI9h94bLCKXESWEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28975" target="_blank">📅 14:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28974">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21e3ccdf4.mp4?token=Uh-h1prQvvUUk1loMxatLF_80bWF5gi75e80PWDByAENwOHL1DPWLGSEXtI-A0agfvp1HYV1YYTf4CkiKxDcXR-O_87wHO1hveLcmtkRSowlLIl-TB-S2yUnP9tdgHCyNGMIqM5BD6Tp9EmLxiu21PjsnRYgGN6LgXA3zPBPqaYPNLj-SjxfIwL5AacUSOlsMGAm8a_m26_1m-57bw3tOJM6_s1ijs7af-e7sxotvUdT2QNwAC06-AzChm_s-njYcf6PrJmDPHfgwchVs5qrSwXtd7VU7w2RzdQIbZzL4aj4G9m6ZwvzZpyUr6FdSSVX4jGwlRfg4Cm6I21PeO2sDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21e3ccdf4.mp4?token=Uh-h1prQvvUUk1loMxatLF_80bWF5gi75e80PWDByAENwOHL1DPWLGSEXtI-A0agfvp1HYV1YYTf4CkiKxDcXR-O_87wHO1hveLcmtkRSowlLIl-TB-S2yUnP9tdgHCyNGMIqM5BD6Tp9EmLxiu21PjsnRYgGN6LgXA3zPBPqaYPNLj-SjxfIwL5AacUSOlsMGAm8a_m26_1m-57bw3tOJM6_s1ijs7af-e7sxotvUdT2QNwAC06-AzChm_s-njYcf6PrJmDPHfgwchVs5qrSwXtd7VU7w2RzdQIbZzL4aj4G9m6ZwvzZpyUr6FdSSVX4jGwlRfg4Cm6I21PeO2sDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تمام موقعیت‌های خطرناک دیدار دیروز استقلال و پرسپولیس در هفته پنجم در کمتر از یک دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28974" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28973">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9WX1SK0CvW_PSuLNQnhMXB9o-84s_o1SYLFmbMGvkIUGtLlwi0--Jyrja4LdyjxjZ4ESoEaPg6BwdQ5iaQSbZZADhOeYlAi_JGHN9YjBSUjW2NZg3BzhJiUztgNla1qCE91ITZq6CHFvrXiCHR80in1tQamx00iP0QJ5RDZyVIDVmQnhFYT62GRTCXYqVFcBCdLdyKxRKANSOVrfo1LTbZ1QDS1-dh-BU5HiRcjYg4dojbRvJNttM4IZDE18Lsetfl2WZu32PzqRWflmUQkPDBawtH1ZNhH77Upikcbx2YUe5Bmqnx7Zd8lxKswYaG73fl-YsZTP56W710IBZZSgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28973" target="_blank">📅 14:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28972">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0exKmpssgnoCZr-SllnC_KmPjlntNwNErkZ0D5b1RuI1GvX_0CBuEfwFOctugdFbtje77pbGd5Ed-PUASmXnLnWtK9qKR4l21J9lOx3aMcGHKcIcF_rNp8fDT3cHFpDGzrS_7mkvZOqGG_ibe7BFeOHwCF1L2d4gHV8F-BLHcYaqin1fTsZJRKkAhAGmEc6aBsInedMPXoniGJzbO2Vq-3b2shvl8EOqaoM5DnNfGLg8STTamrJxbMDLI0dKo5Wc0B3boBFe9cPzSyMfPZqrKW3N5MWZe9_PaGA7edIe9U8it_XmpbeRivPbt2GDzt6apzos7MwFvRfCDNxTxX1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ: رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28972" target="_blank">📅 13:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28971">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePkvGfSugLXz9jowPdAxDxyFuQP96DN9XAsJXZ1k-knCffRmY1fjeHtguNgELBfPDg3emD-E6FngbZB2_lJdjrHUOxgTeXsUKsvW5xycSwdCDIWflNSx-iAhgv_lNrMDm3b-BB-o_YohQuY91V3vvpxm83mT3ogKj0sKsc5AlzCaualahC3Sh387Up1oVadvcpxHSxzfUa7vKPZHj44AimuBNhVpmaMkRJSzk28ACoTrHxc54TogTIN7hXm_sUZeKNSHdgCdcRLVe2aWL9ZsqGL59P9AZZQ-8PzXjUU8E6JIZ1RL69cBHRiK0VD7tRk_eMaPCHIdXtywGA_bThdnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28971" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28970">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Du88_kLFXaYqEvqgOSCsXDq7a1O3ifQzB2CUnaMm19E3yWhEt9Nii7EMUgp5u_QFir6YPj944UUw6qhu33gwr9JHvjRbz7XUSdXSMwtBdfbLULUWtNA4unqHoIuKG70gzTOhy0eYevnBgni_cGvPq5X44Sj0AAacSESDqOW6cdaF2MbZgqwW0FFKeih1jHAqOxgW9YvqPeIYu_irlkP0fQWwKfUxTbqLy7mtPlfll1DUh-AipDhP2eYRB2C6bDHF7YG2JO7yXUTQ_F760hLk2flruQk-18pVMoLYHSIYp2h2qD7-MVlgGw71N-UzmDQeTJG66M0A4RIdlKkzPyVq4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28970" target="_blank">📅 12:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28969">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=YsfXi_eIIQaavcpRhJglqdy-lcQmjGS4binINUA-WRkYP3oSpUKePpCFaMbOsxhXTFDfXQrF4rFopVMCrzClX2NLrdKNza3fyxegET0JiTVU9LfQtqSGCKTMBMUsgbOEp0bmp8VFRV_TpbJF8PNb5Fyei-eMOWrs7zZsVouYX5A0AgA8bEZrfVYVGxR5JzfD_u_SIaEW9BPz1b2BMxCgE2cKknrmpK6pc_BiX1o8-rXuhEjI_u6tdnmbDZ-EduU4u6DPhElyqX-mTOIxhXOXAYO8jXCRur6ql7MsMdWC9JnZ9c_IrWHXn70DdNID4qsgCKuUN1dnofd5mxLZ2EZRRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=YsfXi_eIIQaavcpRhJglqdy-lcQmjGS4binINUA-WRkYP3oSpUKePpCFaMbOsxhXTFDfXQrF4rFopVMCrzClX2NLrdKNza3fyxegET0JiTVU9LfQtqSGCKTMBMUsgbOEp0bmp8VFRV_TpbJF8PNb5Fyei-eMOWrs7zZsVouYX5A0AgA8bEZrfVYVGxR5JzfD_u_SIaEW9BPz1b2BMxCgE2cKknrmpK6pc_BiX1o8-rXuhEjI_u6tdnmbDZ-EduU4u6DPhElyqX-mTOIxhXOXAYO8jXCRur6ql7MsMdWC9JnZ9c_IrWHXn70DdNID4qsgCKuUN1dnofd5mxLZ2EZRRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قهرمانی ارزشمند و شیرین کیانوش رستمی وزنه بردار ایرانی که عده‌ای نذاشتن برای ایران وزنه بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28969" target="_blank">📅 12:28 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
