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
<img src="https://cdn4.telesco.pe/file/WxuZ89O-BXjMGhPSv_jIizBAMEBMDCekDM6dAfj_P1priK4yAnSlpXfo9kiAAudCTXabTFDHvbVxJ7FAUkWkUCfXyTYGUTh7MjguOHXi1oV7Tvcvn0MKQEd79QdG552M7zcrFnVpatSJJ5HonNRmDGG0pTH3gdSAoZ4uNS-qmITl7bioNIMIJ2UVTyIPWAM-SJCIKjzgigH1AO6lMUkC21vVoug8a97ubkeBr71e5OGrZP2nZjX0anjmVXabZwbMAo--40rPtT_Fu4Qv3VCtRL55cHJ0nazlq043FWwBpupDd7pwLrEkwO4zMpPl_43ysyeStvRmVAEs-sojncV56g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 14:49:11</div>
<hr>

<div class="tg-post" id="msg-139576">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-kvd0_cOeeGNMCdzFKSH6XAiHGtkJKvkqShsjOLcXS4BT8rkl-YjtvKgv6kS1vme78NAXhEZ5PKD1oNbiDp5Vrwh3IDMS98EvUWqc5W8RnUIfa6GDyJHgpox08gosrLVe7PdxCwtViC5jYBKaPOyKo97EtudQKP2Nxi8bFqgyRQ5NQzz3L_vvHQalNBL5J87PTBztHfNQUeDeAEjo7-OEUEYQnbcwwgHfp2lVTaPC2hLMfe-7QY3Y6iAEUbXuzzG8qMOcW_gZRE1p-6IzIpRggWlKgQxeegUmIKXEDo6-gftTQ6G8WWHg6R-DdQGpFqptyzpyHCCVcBaErpQHB1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کنعانی‌زادگان به ۱۱ دربی بدون شکست رسید؛ اما رکورد همچنان دست عالیشاهه با ۱۸ دربی بدون باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/139576" target="_blank">📅 14:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139575">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
⚽️
✔️
پیام نیازمند با 3 تا سیو موقعیت و ثبت کلین شیت بهترین دروازه‌بان هفته اول لیگ شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/SorkhTimes/139575" target="_blank">📅 13:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139574">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeOYUO6E31KQgTtXdVOevo58fbexe24ajVUw2KBEtgxG50ldB81dfmyP3r-bduVH2KJyJwwA1L1bR-HnofODA1vZK29mdu18mCqOdinVEFRub3Mjxyp8R3nuamdM3VSQNny18iGnPanyKNEFx_iT78_VEe4dK522LSzRSdjfBqjHWte3t2XqTbqgbZlOpwRzkT1yU0Ys17aY9Oe11_2LUGO5g9Tuxc_CNfTbaf_lELaDKWS25_QhRxO-5FMZTy_eXo1-am2BTCcdORSpn748X_wHaGf87-w9XAS5ZaxVQEzd8DAwpu7K5R1D1mqtoyTppZ-GXz5HPZ3ErC5u7_q69A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد بزرگ در جوزپه مه‌آتزا
🔥
اینتر و ناپولی؛ جدال برای صدر
یک شب سرنوشت‌ساز در سری‌آ
[
اینتر
🔵
🆚
⚪️
ناپولی
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SorkhTimes/139574" target="_blank">📅 13:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139573">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-YgUDbv19mJGnz6Qgz0WeSCHFA6h_lhwxV3CmZQGqWzsZUnFix6Dt84jFfjkpGVOk5jiV6GwH55ViOxJmr6wPSzJ-iuxplDxyLXg11UeCrwXjWfYoyeMeR7Z9oI-dFJUSLbNoKf7Dk5RXIw-N2MCe-r3GRoatO1MRyPwe9WwaU5gZLqS4ieJnRQdH6lDW1ApSZ8u-YfClRsYvvMutghZkTMe4id9gMfwFFCB4XqfmqnjV5RayWdTkNIwQQ1oMUo9x-qReflh7gbZ2_52AnzXClF3MoI_Bp41J8A-ReSjfHqmBgAmWsMQGROJIEbRvcmgubXdcW8dvcJaT7MfjwBNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیس از سوی کمیته انضباطی ۱۵۰ میلیون جریمه برای استفاده از مواد آتش‌زا و سر دادن شعار علیه بازیکنان حریف و ورود تماشاگر به زمین در بازی با ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/139573" target="_blank">📅 11:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139572">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
احتمالا در بازی با ذوب آهن بیفوما زوج علیپور خواهد بود و وینگر چپ پرسپولیس تغییر خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/139572" target="_blank">📅 10:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139571">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
‼️
🔵
🔹
رسمی، با اعلام فدراسیون فوتبال موعود بنیادی فر داور دربی پایتخت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/139571" target="_blank">📅 10:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139570">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم در واکنش به صحبتهای قلعه نوعی که گفته از خودگذشتگی کردم اومدم تیم ملی تیتر زده که آقای قلعه نوعی میتونه دیگه ایثار نکنه و از تیم ملی بره و برگرده لیگ برتر همونجایی که تو ۱۰ سال گذشته هیچ افتخاری کسب نکرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/139570" target="_blank">📅 10:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139569">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⚽️
تمجید ویژه پیوس از وینگر جوان پرسپولیس!
◀️
امیرحسین محمودی در دیدار مقابل مس رفسنجان آنقدر درخشان ظاهر شد که فرشاد پیوس، سرمربی مس، از کیفیت بالای او تمجید کرد و حتی از بازی نکردن این بازیکن جوان در پرسپولیس تعجب کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/139569" target="_blank">📅 09:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139568">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guzjj4ZNeUWyPFQlFLyhpVR_V9Fl22_TwasDFpKLttx-zA4VGc0KkfWy7Pu6LszgNsEDthf-zUMloieMgNiobq4xo_zlwstO_5ZiviYMxAqZYYzMDt8TIUK422maYq9n19l0fwX6muIzTe6BDX_F9eLoMtosVWoKkZdBjFcuOHkysvtP9nYammP19kq5ZMPCxal_EZeDA9OOMh6U9RY2qhiZfv7CdfIiIjEYwteayO-APIlqQZAo2Uo7i4IguxkUD33CrGxN2WGfvETAHSCMQ_W7umSoZ7pcDgFDhXdbkJZKZE9HlfmkVn61d7cnBI7IUfwfyvpQvjjcTjEoEBwKKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/139568" target="_blank">📅 08:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139567">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORHlvyVi7_uIpL3Gziuj_xbjgXbNwsP7LX50fln9Iz5c3jKfGXHOg8hqdt_dE3y_TM7yBmQjARtkrlExUOB6DILeIi0SngNJexeE_CR-AHeigQ80RsAd0Vf7fNwELpXGVtXg2Opsyz2gM_wAVDXe5ztGq5vluvjB05s5wOYGcsYMG2rIKExO6xKxrpcIn-9BSZ2yLi0_OXk-bK_lqgHK8a62lxX-I9L5WQtXSPkDYNOkD9twjgxCqsMf7Ju15J-ZrU4ET6Pr-hjabT53-Rdb1_JnwoX-cenxaFeqadrH71iLvsRMIES6rVbH7oJOrr5j6V9W1DAcZ_m5HUXX-VeTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نبردی تماشایی در یواس اوپن
واچروت و تیافو؛ جدال قدرت و سرعت
شلتون و شاپووالوف؛ دوئلی برای صعود
🎾
ولنتین واچروت
🆚
فرانسیس تیافو
🎾
بن شلتون
🆚
دنیس شاپووالوف
🟡
کدوم ستاره‌ها از این نبردهای هیجان‌انگیز موفق بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139567" target="_blank">📅 02:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139566">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
✔️
شنیده میشه عباس کهریزی ستاره جدید فوتبال ایران پیشنهاد اولیه استقلال رو رد کرده و گفته تمایل داره پرسپولیسی بشه /ورزش3
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139566" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139565">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
✅
پایان دیدار تدارکاتی:
🔴
پرسپولیس 1
🔴
آلومینیوم اراک 1
✔️
گلزنان: علی علیپور برای پرسپولیس و عباس کهریزی برای آلومینیوم اراک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139565" target="_blank">📅 00:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139564">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
تارتار در بازی با ذوب باید به بازیکنانی که بازی نکردن یا دقایق خیلی کمی بازی کردن بیشتر میدون بده تا بازیکنان اصلی هم کمی استراحت داشته باشن
💬
خدایی نکرده دچار مصدومیت هم نشن
💬
🗣
🗣
مثل ایری، محمودی، سلمانی باکیچ
💬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139564" target="_blank">📅 00:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139563">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=RAOEEwgAFwU0Q_NBTJuXsqhUapWxi7QbcOdYoPgA11PmBJnfRtbB2YutgtlI5Ng46MP-Uh-y48D-F0TQAr4n6c-bGCuRhm2tDJbNmAsybLJok_dKnvXFVuJ2KnFWMueHQQyOYqkoThJALa3fTlLRMGRwSXC2SsLETyLQNWcr3x4yS1pzjKopbr0YG4-BIX41D0fGA0lTw9qgdx_-TrhrTT4cOrjh9DXWKGNkjC4i7tiybGb63fbDJSKSL78l30nhoUq4PxhOJ9zfGDQKmquEZS7UYTcBxg-site5ZxnMTjpUxMktNWkvUMWy_O2wTznJriEWMcB-ILBvbKkKG7pkyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=RAOEEwgAFwU0Q_NBTJuXsqhUapWxi7QbcOdYoPgA11PmBJnfRtbB2YutgtlI5Ng46MP-Uh-y48D-F0TQAr4n6c-bGCuRhm2tDJbNmAsybLJok_dKnvXFVuJ2KnFWMueHQQyOYqkoThJALa3fTlLRMGRwSXC2SsLETyLQNWcr3x4yS1pzjKopbr0YG4-BIX41D0fGA0lTw9qgdx_-TrhrTT4cOrjh9DXWKGNkjC4i7tiybGb63fbDJSKSL78l30nhoUq4PxhOJ9zfGDQKmquEZS7UYTcBxg-site5ZxnMTjpUxMktNWkvUMWy_O2wTznJriEWMcB-ILBvbKkKG7pkyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمد تقوی، در برنامه هت‌تریک در آنالیز دربی ۱۰۷ استقلال و پرسپولیس گفت:
✔️
✔️
«از معدود دربی‌هایی بود که همه راضی بودند؛ تماشاگر راضی، مربی‌ راضی، بازیکن راضی. یکی از دلایل موقعیت‌های زیاد گل، دفاع نامنظم دو تیم بود، هر دو تیم به سرعت به فاز حمله می‌رفتند.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139563" target="_blank">📅 00:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139562">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a36a4cce3e.mp4?token=OURgLc6SnfepXZerYhrfV-4KWw_lW6-0U0ljY7FAIJe-0Dl77uvmeNSJQrvpdYZI30jRj6sy0vBVji57hdLd1SXsdTJTXWQThDCWcZhqE1JrEUcTQCFk2bAZBj0JqUc_DnFlNnu8Nzx1wJ_GK0OVKd7Bu34zB7KrKgs-VZ2ZN7fZW0IFvXJvWWXWw0VS9MsPYI0GDy3nmC9ogqbt0ozERqkAFjZ3-4XYxHbHVF1_yjCmIMx700kfaYCmgXtBCZx2vetnFYU0CBTv9FVd-AjVMbg9Ny5vIr6vwsyyQ8nubWvxXhZbxrk7FPGPu0IVI2LOBhL9A6jWbeTMEI_IRJrQvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a36a4cce3e.mp4?token=OURgLc6SnfepXZerYhrfV-4KWw_lW6-0U0ljY7FAIJe-0Dl77uvmeNSJQrvpdYZI30jRj6sy0vBVji57hdLd1SXsdTJTXWQThDCWcZhqE1JrEUcTQCFk2bAZBj0JqUc_DnFlNnu8Nzx1wJ_GK0OVKd7Bu34zB7KrKgs-VZ2ZN7fZW0IFvXJvWWXWw0VS9MsPYI0GDy3nmC9ogqbt0ozERqkAFjZ3-4XYxHbHVF1_yjCmIMx700kfaYCmgXtBCZx2vetnFYU0CBTv9FVd-AjVMbg9Ny5vIr6vwsyyQ8nubWvxXhZbxrk7FPGPu0IVI2LOBhL9A6jWbeTMEI_IRJrQvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
درخشان: بازیکنان پرسپولیس هنوز به هماهنگی کامل نرسیده اند. قطعا پرسپولیس در ادامه لیگ بهتر می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139562" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139561">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdba32ee42.mp4?token=ByEXXJHYqp9jBCm1QCOYchYzJ6EfLaGR2_65mNjWHl4WaJMF1_g72wEwMyCSfq-3qhN7rBM74S4G9810K_GAPdVmnHkVwmezw2d3Ju01POoXyJP1GDW-ss4hsNUJhDhlYEJACzLQzkt8zM9fg39CmomOZAs6KBuHH2QIDdcu4Lk-Id0zHj6JjqdIit31XSWUM3QuhRt9cS9jij-TRlYm4u84lpRkFE2VN34i7ZOkm8305TdfsPkBlhBTwfUXJoUA3trl15gH-DJ03TMY9hJGPAambRRwKJIdnw0r2d0ITfTuoJ79tD8kjgBYJqteNuZdReQynWKAGEeKRUDX2JPKCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdba32ee42.mp4?token=ByEXXJHYqp9jBCm1QCOYchYzJ6EfLaGR2_65mNjWHl4WaJMF1_g72wEwMyCSfq-3qhN7rBM74S4G9810K_GAPdVmnHkVwmezw2d3Ju01POoXyJP1GDW-ss4hsNUJhDhlYEJACzLQzkt8zM9fg39CmomOZAs6KBuHH2QIDdcu4Lk-Id0zHj6JjqdIit31XSWUM3QuhRt9cS9jij-TRlYm4u84lpRkFE2VN34i7ZOkm8305TdfsPkBlhBTwfUXJoUA3trl15gH-DJ03TMY9hJGPAambRRwKJIdnw0r2d0ITfTuoJ79tD8kjgBYJqteNuZdReQynWKAGEeKRUDX2JPKCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
واکنش حسین عبدی به عدم دعوت از امیرحسین محمودی
🗣
حسین عبدی: امیرحسین محمودی بازیکن فوق العاده ای است ولی وقتی من او را حتی ندیده ام چگونه دعوتش کنم؟
🗣
‌‌پ.ن: ما که از خدامون هست دعوت نکنی ولی این حرف عبدی توجیه قابل قبولی نیست
⚪️
بازیکن کیفیتش مشخص هست
🔄
همین دقایق اندکی هم که بازی کرده برای تارتار نشون داده قابلیت هاش رو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139561" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139560">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎤
⚽️
وحید فاضلی مربی پرسپولیس: میتواستیم بعد از گل عقب بکشیم و به راحتی برنده مسابقه شویم اما فلسفه تیم ما این بود که برای گل دوم و سوم تلاش کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139560" target="_blank">📅 22:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139559">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f9d5f0dd.mp4?token=FmGvTytu-HMQx8AIyLwxu6P_kXSjjYlwfeaQlz0ufbutO5ygGdloU1cRWf-xaABoajGQdNvk0pq7ttiQeUxZI9baHJq8IUUMcLv5jAh51abpn-uZlEQT_Ne8O_Ib7P07wyrsKDJLL9cB2sWa4g27RtpwQeWCPhMTVO7ayQuQPy1gbeFKru4WWatAvWOcXJncyypdo6HwsUQZ9Zk6s3-y86j3HWwITYoXpFzxGUZ7VU5tSMaaV4lIMV5_2DPjJND6HDTNRs7hxyff6JjEjrJs_Uc12-nmvipP4Bl1YHsVJDYLnNloe68Mq_8snUOmok0mF5y2W2_ZPmUYT4mDLMiKCn-9a70meO-Z6hyizMDBKh3i1FwCY4-3R1RuHQxfM5MLJbesFLhTQmz3JX64RbaxejHCVbIlS2ycHk5uvprLux-a1fIpU3FEalY705Ky4AsTu_hBzL9Y82h6_1yEff1MlqxGELzJ4FaQaxQlP7KLIwqo48bxLE09Rir_mbkdLBr0rUbwAnnRHH9E1s_P-W9ajSsy33kT145NJ2vr9U6rmHb8IQcHu4iMVb0SS0HQrtahD5dpxe8DZrMh0Mb6v0iEeY1gePU9jDeGjvLyH13on9lk95DshCxTGfsknxEJZKD9G7RX3RbGkawEqZGPOsUmbLLXaVpr_TNrZBq9PFeRhTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f9d5f0dd.mp4?token=FmGvTytu-HMQx8AIyLwxu6P_kXSjjYlwfeaQlz0ufbutO5ygGdloU1cRWf-xaABoajGQdNvk0pq7ttiQeUxZI9baHJq8IUUMcLv5jAh51abpn-uZlEQT_Ne8O_Ib7P07wyrsKDJLL9cB2sWa4g27RtpwQeWCPhMTVO7ayQuQPy1gbeFKru4WWatAvWOcXJncyypdo6HwsUQZ9Zk6s3-y86j3HWwITYoXpFzxGUZ7VU5tSMaaV4lIMV5_2DPjJND6HDTNRs7hxyff6JjEjrJs_Uc12-nmvipP4Bl1YHsVJDYLnNloe68Mq_8snUOmok0mF5y2W2_ZPmUYT4mDLMiKCn-9a70meO-Z6hyizMDBKh3i1FwCY4-3R1RuHQxfM5MLJbesFLhTQmz3JX64RbaxejHCVbIlS2ycHk5uvprLux-a1fIpU3FEalY705Ky4AsTu_hBzL9Y82h6_1yEff1MlqxGELzJ4FaQaxQlP7KLIwqo48bxLE09Rir_mbkdLBr0rUbwAnnRHH9E1s_P-W9ajSsy33kT145NJ2vr9U6rmHb8IQcHu4iMVb0SS0HQrtahD5dpxe8DZrMh0Mb6v0iEeY1gePU9jDeGjvLyH13on9lk95DshCxTGfsknxEJZKD9G7RX3RbGkawEqZGPOsUmbLLXaVpr_TNrZBq9PFeRhTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
⚽️
وحید فاضلی مربی پرسپولیس: میتواستیم بعد از گل عقب بکشیم و به راحتی برنده مسابقه شویم اما فلسفه تیم ما این بود که برای گل دوم و سوم تلاش کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139559" target="_blank">📅 22:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139558">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
برخلاف شایعات هفته هفتم لیگ برتر کنسل نشده و قبل از فیفادی برگزار می‌شود.
✍️
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139558" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139557">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
✔️
کم بازی کردن اورونوف بخاطر ترس از مصدومیتش هست و داریم دنبال راهی میگردیم که نهایت بهره رو از این ستاره بگیریم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139557" target="_blank">📅 22:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139556">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
✔️
کم بازی کردن اورونوف بخاطر ترس از مصدومیتش هست و داریم دنبال راهی میگردیم که نهایت بهره رو از این ستاره بگیریم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139556" target="_blank">📅 22:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139555">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
جباری: سبک بازی ارونوف و نوع بازی تیم با توجه به تغییرات در حال هماهنگی است و به مرور زمان بیشتری برای بازی پیدا می‌کند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139555" target="_blank">📅 22:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139554">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
معاون وزارت ارتباطات : با اشاره به تجربه قطع اینترنت در جریان جنگ اخیر کشور به سطحی از بلوغ رسیده که حتی در شرایط بحرانی و التهاب شدید نیز میتواند بدون قطع اینترنت مدیریت شود و دیگر شاهد قطع اینترنت نخواهیم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139554" target="_blank">📅 22:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139553">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf52d5a19e.mp4?token=QCGQSnf3WDAkifeaU_fDJfP9NaIWcXyL27G7YZb1vla3wDn5kdo2fBHZ5LHb_QkTr3X3E2xhwFZ1WKVcgO-5T--wKzyAHSv6NuuVx5oD2uMd5JLS4KlyaP6PvncGEzT81_gxN9Iod7mB-DkHfsqKf_CqF8GLTdWw4nyzHh6qYjFeb_VY1pubF1HIzexbXNAAB9XZERUvqTb4EBFUEa4dW0xLM3RwfmoWOVXlsh9U9lpcIYR6hBO3Jdy1nw_xmKhvnITfeN7qqyNJjT_zRG5eZTimkzzF2f9FC4zuo_bteTvAt4g298ZPgmg0wPHgIbut8GnP7kJX-GmdobuyQkDchw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf52d5a19e.mp4?token=QCGQSnf3WDAkifeaU_fDJfP9NaIWcXyL27G7YZb1vla3wDn5kdo2fBHZ5LHb_QkTr3X3E2xhwFZ1WKVcgO-5T--wKzyAHSv6NuuVx5oD2uMd5JLS4KlyaP6PvncGEzT81_gxN9Iod7mB-DkHfsqKf_CqF8GLTdWw4nyzHh6qYjFeb_VY1pubF1HIzexbXNAAB9XZERUvqTb4EBFUEa4dW0xLM3RwfmoWOVXlsh9U9lpcIYR6hBO3Jdy1nw_xmKhvnITfeN7qqyNJjT_zRG5eZTimkzzF2f9FC4zuo_bteTvAt4g298ZPgmg0wPHgIbut8GnP7kJX-GmdobuyQkDchw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
#منهای_پرسپولیس
👾
عبدالکریم حسن دفاع چپ سابق پرسپولیس، به این شکل با پیراهن الشمال در لیگ قطر گلزنی کرد
🚀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139553" target="_blank">📅 22:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139552">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rF0i-3URGl3ko8Lxmp-gy6RBOQgkPPExFc6ev9Bi35e1VEy31b0yJUb6fWf0O9I0dew3We7kdrqoFd8P2ymTINQdIQIRyQx8gRv4wwolvwnMaUUQzG31OmwEulMTgYzo4v50lW7083Jo_wAjXvOjkcUIUypqNIY2pM-PvIQ53M8Uzwk44rGPVgE15Qy_ej3E0C_WZ79KIAmiajb9N_W_NkdPOQGlfE_zEac2iMSQp9r7zCkr4sipy3r0rNaQH4yaRFvfCfk790z1MLK3WOMwZmUCn8vJJI_zc4TcT7ay0jtHNWb9QOc6wIA-lk6lwas9VvQQvO1akouW7WB55jwLLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیورپول آماده‌ی شروعی قدرتمند
ایپسویچ سد راه قرمزهای مرسی‌ساید
نبردی برای فتح سه امتیاز
🔥
[
ایپسویچ
🔵
🆚
🔴
لیورپول
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139552" target="_blank">📅 21:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139551">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139551" target="_blank">📅 21:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139550">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYD08U6m03B2q5y7T8OWamxOmv38NvUst4TK1Kzcl5AqXR-2MxJzNbRUVYdSbDKzbeJF07WFNnOB23oSmXGz0zDQ12_Wybgtqk6Ab7y6pdsUlPcfR0pE9fJHWoGI2mrP9RAPn6HMC1UpsD-FrLcfqn7Zmc1zz5E-D8o1pXNdkk7LjRhoB15OzHMsHu7vZff6WWWIBWiwjUeocl4RdNyApWKiIqeVbo3Mwzkv6F-seMJd2zFA7DZgc__M5z17My12_XPvXdP-5teehAolnj4pMEVt6EfDzT-Rdg4fGwPL5fDpBFyixXw4rP72dhnsAjMsqGSoS0ZY6sZrHhx-8NGXew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تمجید ویژه پیوس از وینگر جوان پرسپولیس!
◀️
امیرحسین محمودی در دیدار مقابل مس رفسنجان آنقدر درخشان ظاهر شد که فرشاد پیوس، سرمربی مس، از کیفیت بالای او تمجید کرد و حتی از بازی نکردن این بازیکن جوان در پرسپولیس تعجب کرد
!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139550" target="_blank">📅 21:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139549">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ejjr7ZcNU8Ycuo2WTNZ6MbfNdw68PTxx1cUPXdUBpQNKj7O2JO17t6XIF5jk5aJmVbrI13Pjcw49HmKHUNufv73gxysOVK8ejngXJiF-ErejEi4hvWAhwsuab0u2BfSbD61QEWQHenfU6A5j2JksG9mOa--7xn5d3bF28hG3r99HSlzk3B0myjAdQU9zsvDun1S4zZfJuxGZL57k1jMebyrRHb-pRm4Hxi9xJFMYJ4xb8P38xzf-ceQVShvGUKZxn86gH9UpUr_00NWPfuMRGA312wlyBTPx5k0SMc0b3F0SiXpqukCzGE6S1ILtsCT1vhr0rjUSuFc5rlISHJ2_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
🔴
از دیروز که باشگاه گفت پرونده ، آسانی رو به CAS می‌بریم به هـــول‌‌ُووَلا افتادن‌... دیروز تاجرنیا و امروز این هوشنگ اصرار میکنن که نکنید بی فایده‌ست‌!
⭕
اصلاً ما دلمون میخواد شکایتِ بی‌فایده کنیم چرا آنقدر میترسید فشار میارید مانعِ ما بشید‌؟
✅
اگر فایده نداره پس سکوت کنید بزارید خود (CAS) معلوم کنه شکایت به‌حق هستش یا نه‌...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139549" target="_blank">📅 20:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139548">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139548" target="_blank">📅 20:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139547">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👀
❓
محمودی ۱۵ دقیقه هم بازی نکرده امسال… اقا تو پستش ترافیکه درست ولی نمیتونی هر بازی بهش ۲۰ دقیقه بازی بدی بازیکن روحیش از دست نره ؟! محمودی چند ساله دیگه عصای دست پرسپولیس میشه اگر آقایون نسوزونن بازیکن رو…فقط بازیکن هایی که از گل گهر آورده رو بازی میده اقا…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139547" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139546">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
با اعلام باشگاه پرسپولیس، آکو باتری اسپانسر جدید این تیم خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139546" target="_blank">📅 19:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139544">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKzTOMrX46HUtU_reW5lkrQGyi432grRln3cwy80BkO2TBOd87EI2oZaCPq5DJk2EQ_ePBWplt0Esc-8wq7W94lB_LLc56ZUeqUi5COH3bhnExDw-4hdPSU9ivMY336kp8I0AOQGL8uPg6--O1vnd0qHySFyjoBFGHYeOqsf_L1RL5jDmv4Tas_ye-Gh1K-YOtMMLIQ9zObdT5X7XOcNhlar5Y7KX7OiG3BH5Dyq2oCGInVSaTwaOREBH3CyMUkKxu9MMjH83ziopV2876YsCXj0Xs8B7k7jTIjbj7-oYYkBZB7dG5GhVb9l6Vrn_8rWQnetO5GhSLFkI0zYuqXvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🆔
| ورزش‌سه:
🔴
❤️
با ادامه‌ی روند فعلی مارکو باکیچ از پرسپولیس جدا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139544" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139543">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❤️
❤️
باز هم بزرگی و عظمت پرسپولیس در این سال‌ها به بهترین شکل خودش را نشان داد
🔻
🔻
در سال‌های اخیر، بازیکنان زیادی با آرزوی رسیدن به پیراهن تیم ملی، راهی پرسپولیس شدند و پس از درخشش در این تیم به هدف خود رسیدند؛ گولسیانی و گندوز نمونه‌هایی از این اتفاق هستند…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139543" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139542">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: ما پیگیر شکایت از یاسر آسانی هستیم و برای اینکه پرونده را به دادگاه CAS ببریم ابتدا باید در کمیته انضباطی شکایت کنیم و جواب بگیریم بعد به CAS ببریم
✔️
بعضی ها می گفتند ما اورونوف را بازی نمی دهیم که او را  بفروشیم/ واقعا خنده دار است چرا باید…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139542" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139541">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
جنجال و حاشیه در اردوی کیسه؛ با اعلام سهراب بختیاری‌زاده، صالح‌حردانی بدلیل رفتار ناپسند و درگیری با سرمربی و یاسر‌آسانی در بازی دربی، تا اطلاع ثانوی از حضور در تمرینات کیسه منع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139541" target="_blank">📅 18:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139540">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⚪️
⚪️
⚪️
فوتبالی: سهراب بختیاری‌زاده به حردانی، مهار اورونوف و بیفوما رو سپرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139540" target="_blank">📅 17:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139539">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
نصیرزاده: شکایت از آسانی، دنبال نخود سیاه رفتن است!
✔️
تیم‌ها با شکایت از آسانی دنبال نخود سیاه هستند؛ فقط استقلال می‌تواند از این بازیکن شکایت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139539" target="_blank">📅 17:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139538">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b00df71c.mp4?token=fUB3fj6zp_KscjAO6TeradwVEF1SkeusVo_Hn1DHpm6w8uy1amoyKlv_z5jqvcawD3vgxC1YhxnCNEjHG3tgqflu3-UmzhhvifpySL8YYmV8I1lyFiE6n-VdVQ58Jxj1jcTCeEDYbKRgJp3Ao-fxAtQjxlgL8wkPw35ZhU0FQTQqDmSoUA9XP1emrI7-dUK2xQe5uaxFpyRuY13VkXg7Gq5KMzxBhRuzlZtwSFDQqER-E0jcK28j0V3MrS8gwbeotRJ6JsTu5p_WgWIenQb5OvkpB0QBSX0TzSGx0r4Jr4Uk8Zr2DjlNK3izI17gwCLPX7yF3AFlFnVM5b9dnRrUQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b00df71c.mp4?token=fUB3fj6zp_KscjAO6TeradwVEF1SkeusVo_Hn1DHpm6w8uy1amoyKlv_z5jqvcawD3vgxC1YhxnCNEjHG3tgqflu3-UmzhhvifpySL8YYmV8I1lyFiE6n-VdVQ58Jxj1jcTCeEDYbKRgJp3Ao-fxAtQjxlgL8wkPw35ZhU0FQTQqDmSoUA9XP1emrI7-dUK2xQe5uaxFpyRuY13VkXg7Gq5KMzxBhRuzlZtwSFDQqER-E0jcK28j0V3MrS8gwbeotRJ6JsTu5p_WgWIenQb5OvkpB0QBSX0TzSGx0r4Jr4Uk8Zr2DjlNK3izI17gwCLPX7yF3AFlFnVM5b9dnRrUQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
نصیرزاده: شکایت از آسانی، دنبال نخود سیاه رفتن است!
✔️
تیم‌ها با شکایت از آسانی دنبال نخود سیاه هستند؛ فقط استقلال می‌تواند از این بازیکن شکایت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139538" target="_blank">📅 15:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139537">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
رضا جباری:
✔️
این نسل پرسپولیس از لحاظ اخلاقی و فنی بهترین‌های حال حاضر فوتبال ایرانند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139537" target="_blank">📅 14:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139536">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
کیسه و ترتر شش امتیازی شدن و کلین شیت و حفظ کردن امیدوارم فردا بازی و ببریم و پیام هم کلین شیت شو حفظ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139536" target="_blank">📅 13:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139535">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎥
🔹
تمامی گل‌های هفته پنجم لیگ برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139535" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139534">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87b97822e9.mp4?token=RXll8JHwEQuG9TpWznsyc6tcudsfWMDnwl_Lxdg_eoLHEjuBVdd-MOZYzRbKS3ZXA8Y6FHBLmErzrtwfcfWe783-PhKvcfYBeRuM6y7FVSt5yJWuqPiq436bsB0TJdBJygZcFgIata-X5JPTOe6K0NoMINqehJbznJ7rAWZKvwMluMikFbvit3NCyRYCkdLDDapS-ualJTCB3C9UrIuKTPlheBaagXX90oxoEaRuFJgW49dXaKGZL8hTNW4vRVvMb_NbMicK8QalnFcuduyheAM0CpTquKd4_4gXyRqF01oCekoMhEo_0Svg6gP6uYITGcluhVZLBsxGvVQIpqbc9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87b97822e9.mp4?token=RXll8JHwEQuG9TpWznsyc6tcudsfWMDnwl_Lxdg_eoLHEjuBVdd-MOZYzRbKS3ZXA8Y6FHBLmErzrtwfcfWe783-PhKvcfYBeRuM6y7FVSt5yJWuqPiq436bsB0TJdBJygZcFgIata-X5JPTOe6K0NoMINqehJbznJ7rAWZKvwMluMikFbvit3NCyRYCkdLDDapS-ualJTCB3C9UrIuKTPlheBaagXX90oxoEaRuFJgW49dXaKGZL8hTNW4vRVvMb_NbMicK8QalnFcuduyheAM0CpTquKd4_4gXyRqF01oCekoMhEo_0Svg6gP6uYITGcluhVZLBsxGvVQIpqbc9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
گل محمدمهدی محبی از زاویه‌ای متفاوت
▫️
▫️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139534" target="_blank">📅 13:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139533">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
فنونی زاده : به حدادی گفتم حواست به خلیلی باشه میخواد مدیرعامل بشه و زیر پای تو رو خالی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139533" target="_blank">📅 12:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139532">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚫
عادل فردوسی پور: با دیدن فوتبال ایران میتونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139532" target="_blank">📅 12:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139531">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=Y9lphQRHbhaLH51_3HbWaxf7RDRTv0pjaaTz89uewkauknSRJAmba8KVKDO-NlJZ_45RxrL77EqanMi_G60GDnM6jb2h_2wZwRzuR3VMzrWWtrXyYo5_t0Yev_E0O7EoOCGY_4L5OvWlN5jYM5IfjGeFIgXf6hVycOAp3L2OtcNzkTpNrNnx3TKQXXLCaaiC61GTOU6xkQRfvnygOYAT8bA7pENvOiJvatLvMAcIZl_EJh5bF8KSggxH_4njQExfSWbDuR1wzqRWHi3HyVQ4eVTkq6yzdR5TI_KcXa3tDrEdH-uY8KJrMFivPbRkBdtc2DCOhlJz2jA51B5w1qhWdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=Y9lphQRHbhaLH51_3HbWaxf7RDRTv0pjaaTz89uewkauknSRJAmba8KVKDO-NlJZ_45RxrL77EqanMi_G60GDnM6jb2h_2wZwRzuR3VMzrWWtrXyYo5_t0Yev_E0O7EoOCGY_4L5OvWlN5jYM5IfjGeFIgXf6hVycOAp3L2OtcNzkTpNrNnx3TKQXXLCaaiC61GTOU6xkQRfvnygOYAT8bA7pENvOiJvatLvMAcIZl_EJh5bF8KSggxH_4njQExfSWbDuR1wzqRWHi3HyVQ4eVTkq6yzdR5TI_KcXa3tDrEdH-uY8KJrMFivPbRkBdtc2DCOhlJz2jA51B5w1qhWdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
اتفاق عجیب؛ نیمه دوم بازی شمس آذر و تراکتور ۱۶ دقیقه وقت تلف شده داشت اما داور دو دقیقه اعلام کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139531" target="_blank">📅 12:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139530">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139530" target="_blank">📅 12:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139529">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
✔️
شنیده میشه که همکاری یحیی گل محمدی با باشگاه دهوک عراق به زودی به پایان خواهد رسید و این مربی به زودی به لیگ ایران باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139529" target="_blank">📅 12:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139528">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
فرصت به ستاره خاموش سرخپوشان نیز خواهد رسید؟!
✔️
✔️
مهدی تارتار قصد دارد بصورت چرخشی از بازیکنان جوان خود در ترکیب تیمش استفاده کند و در هفته‌های اخیر شاهد بازی کردن بازیکنانی همچو سلمانی و لطیفی‌فر در پست خط هافبک سرخپوشان بودیم.
✔️
✔️
حالا بنظر میرسد…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139528" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139527">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
پافوس قبرس با هدایت ریکاردو ساپینتو از پلی‌آف لیگ اروپا حذف شد و راهی پلی‌آف لیگ کنفرانس اروپا شد. تیم ویتبسک بلاروس هم که میلاد محمدی را در اختیار دارد، از لیگ کنفرانس حذف شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139527" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139526">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: هوادارا فقط میگن چرا اورونوف بازی نمیکنه؟ خب وقتی بیفوما در آماده ترین ورژن ممکن هست چرا اوستون بازی کنه؟ بیفوما خیلی خوب بازی کرده و حق دارد فیکس باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139526" target="_blank">📅 11:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139525">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی مدیر پرسپولیس: بیفوما الان شرایط خیلی خوبی دارد و دارد خوب بازی می کند ولی دارند حواشی درست می کنند که چرا ارونوف بازی نمی کند. هواداران ما  باید صبور باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139525" target="_blank">📅 10:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139524">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMHL34F-FDLS8za8HRdIxqZdvnmh1bABiUerPj42mGXNat33u61ns0yVGvXmiISZ3qyDUy0gsD82RzOD4omyxrL5vyzJ_rk_1Mi3I3lcX28FmAZRub6w_U7IHreQunjiQ5jVKKwoJs-IWMVAYyNYA3yVuu90XUX-mRsqWsE1iRPZjgILhUAIwnPsCnrkboknxs1t7eh4-xiQ7ASiryPeXDUks7RyhXyp9S6lFep5Hf5RinsL-holWPqbILNR4MDvJG7bnLJ92nTvlrEDrQagC7MnLZ8YIFV4UdHNUeQVHtp-8X5hAQonFhka3FOCzCpuUF3GT6dGr7YNpsHwoN82zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌬
پایان دیدار
🇮🇷
ایران
3⃣
_
0⃣
نیوزیلند
🇳🇿
👀
✔️
ایران گام اول را محکم برداشت، شروع مقتدرانه شاگردان پیاتزا در مسابقات قهرمانی آسیا
🇮🇷
۲۵ | ۲۵ | ۲۵
🇳🇿
۱۵ |  ۱۲  | ۲۲
🏐
#قهرمانی_مردان_آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139524" target="_blank">📅 10:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139523">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❤️
محمدمهدی محبی زننده ۲۰۰ مین گل تاریخ دربی بود
👌
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139523" target="_blank">📅 10:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139522">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❤️
صبح آدینه تون بخیر و شادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139522" target="_blank">📅 10:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139521">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfcO8PkcaBTIZzU_lvpM-pPBz5LAi-4pRSjP7_qh_6LV23L4n3YoC3xXi_DZuDc1yIHqDLmzhHDZ6trf3nTllTGEsuHRojqWKCuYOjSRrXA34gjn4s5hXacMf1Xqor44xsCH-MlpJNy0mamkRbuj_7EBk6wNMQtgc469-fokc3MVFmhMIpWBTbqumwZJDeQu1nhVtxpJKWZMWtj-_TIWJvHlzaHgVAz2ppTiLUo-x6Q0HXwKXiV9KQqbY1z-PpIphjDsL_FjuvsEldqETH2vnL8uo5dICtIfCWO5VPnSalnn2EzcdETxNlLXhOIFgqGK6_kLFUjZgm8qbYrda-dLyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل ستاره‌ها و مدعیان در نیویورک
جوانی، تجربه و انگیزه در یک شب هیجان‌انگیز
زورف و تین به‌دنبال عبور از سد فرانسوی‌ها
🎾
گائل مونفیس
🆚
لرنر تین
🎾
الکساندر زورف
🆚
کوئنتین هالیس
🟡
کدوم ستاره‌ها از این نبردهای هیجان‌انگیز موفق بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139521" target="_blank">📅 02:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139520">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk-iDqT7qHsd8QAzOU3LdHPD6YiCiTC-G7mdH7mWyZSn1osBD-cpTva2YrLt5KGHC55v2iFfh6BKONvR_mEAJur_BSFfbkhxiv6H-pF3OHWs-GF6jcHssLvtEbL4U78xze4Z3YjRoedjEwU9X9Zi4TPomwhqvf9AvqYq55TWhL1cQrHjY00Th8nqCxQh2-_JBT1ybAsI_oN7kojiW1AzAGnza-oMppwjhbpLmSaSD12A71WGZse4qmMyDT1XVuE9_OkYvUgL_3IWPfBM5_s7lo_0GEQc0eDSGO85tPMs9jrgRp9YXQPdlgZtUb34_4mgdwnaQ6VpusDi_ZtYn7G_xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139520" target="_blank">📅 01:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139519">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139519" target="_blank">📅 01:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139518">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=sqst6SEXQjrURiLpSyI9Dbb5xRN_78Bh_LgB6zpqvwR701AgC0bXg1qNuoUFmkgm2Y0q9XZU37QmrVcfAAET-yRne5ZuJm2QxhfQRrBZWw-cwZWlnwhRDB67JI_Fp7AwCRlb1j3xGkUUb1bdWvjSks-K_bzOzN1hgjhw2H7z5qUlEml7t7Vr1rz6oaY_G1d07cgx3O9SZYeIdrSooD48LmoKt39nZBVxaoQ-NxZ-LOHYSPh1buV0tCBe4IAyM3PW2fshVzYWiY7BEi_BGPIsRdQp1uAp9wgHymhySV1hglqhqlzgR1Izvy5a7GZhukoF-1A2dIAW88oQwLxwsVr48w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=sqst6SEXQjrURiLpSyI9Dbb5xRN_78Bh_LgB6zpqvwR701AgC0bXg1qNuoUFmkgm2Y0q9XZU37QmrVcfAAET-yRne5ZuJm2QxhfQRrBZWw-cwZWlnwhRDB67JI_Fp7AwCRlb1j3xGkUUb1bdWvjSks-K_bzOzN1hgjhw2H7z5qUlEml7t7Vr1rz6oaY_G1d07cgx3O9SZYeIdrSooD48LmoKt39nZBVxaoQ-NxZ-LOHYSPh1buV0tCBe4IAyM3PW2fshVzYWiY7BEi_BGPIsRdQp1uAp9wgHymhySV1hglqhqlzgR1Izvy5a7GZhukoF-1A2dIAW88oQwLxwsVr48w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139518" target="_blank">📅 01:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139517">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: شما تعویض های تارتار در دربی را ببنید که تماما هجومی و در خط حمله انجام شد
❤️
محسن خلیلی: اینجا پرسپولیس است شما نمی توانید ناگهانی 80 درصد تیم را جوان کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139517" target="_blank">📅 00:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139516">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: شما تعویض های تارتار در دربی را ببنید که تماما هجومی و در خط حمله انجام شد
❤️
محسن خلیلی: اینجا پرسپولیس است شما نمی توانید ناگهانی 80 درصد تیم را جوان کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139516" target="_blank">📅 00:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139515">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⚽
🎙
رضا جباری:پوریا شهرآبادی جزو 3 مهاجم برتر لیگ است؛بازی در پرسپولیس پرمهره از بازی در تیم ملی سخت‌تر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139515" target="_blank">📅 00:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139514">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
خلیلی: بهترین نقل و انتقالات چند سال اخیر را امسال داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139514" target="_blank">📅 00:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139513">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
دعوت بیفوما به تیم ملی کنگو بعد از درخشش در پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139513" target="_blank">📅 00:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139512">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه استقلال:
✔️
سرعت بیفوما خیلی عجیب غریب بود و مشکوک به دوپینگه! ازش شکایت میکنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139512" target="_blank">📅 00:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139511">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4EL_TAPNbunL3KtB2WgheUq1Daqy_DpBumNUfM3-3PCiAmErpUKKgi3SW9su6cGoFoMTdyKudrNFPBcsGdpUJq_39Swt_ns0X8OU_seKGWLwclnOFQyH2BAczbpHohzrkJOand6TJuH_X4IU3ql2o25mg-_oFLTBVb5I9JwuxIXM2i5WNTfSo6p5yelPZ7ifqecDOmXDuVDKiDaFG-AgaU5TP1t88ZXQv9P78i_5Q-3qzc1zWLlZWe7HmJ7oWA89zDSEf7xz9H3-Sia7MfXZup7uEiWWKYCmVq_AFYQalbSyA2w8w0bO8sVbkcAEqkRt-UOQf6mSRnCFvXjaq49Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🟠
جدول لیگ برتر در پایان هفته پنجم
👑
تراکتور با فاصله ۲ امتیازی همچنان صدرنشین است
👀
فاصله منطقه سقوط تا رده پنجم؛ تنها ۳ امتیاز!
❌
چادرملو و استقلال خوزستان؛ تنها تیم‌های بدون برد
🔼
تراکتور، استقلال، آلومینیوم و فجر؛ ۴ تیم بدون شکست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139511" target="_blank">📅 00:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139510">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: برای دربی 5 بازیکن جدید در پرسپولیس بازی کردند اما استقلال تیم پارسالش در دربی به میدان رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139510" target="_blank">📅 00:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139509">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: من شاهد هستم که تارتار واقعا دارد در پرسپولیس زحمت می کشد اما یک سری هجمه ها روی این مربی وجود دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139509" target="_blank">📅 00:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139508">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👤
محسن خلیلی:
✔️
با کفش‌های بیژن طاهری هتریک کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139508" target="_blank">📅 00:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139507">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
جباری: سبک بازی ارونوف و نوع بازی تیم با توجه به تغییرات در حال هماهنگی است و به مرور زمان بیشتری برای بازی پیدا می‌کند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139507" target="_blank">📅 00:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139506">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e2475d08.mp4?token=ryrJF5TfybtGmqEr-gVN1fiwFjGsddt3NrDrVo5X4thpJ3F8DWm6MQMJPjV4Q3pJ_Cb1Ti5RXBWHI8j_Bntss4H84bBAktAWtNQHg_Y2glOQsGGwsbaN2_QXfqQpfzbd-6zybf0E3eaM-MFZlMDH3qohrRnz-_kll8Aswev2oZ3Lk0R3-kt42SbwqbfIjpAwGetWj3tbFLez3t-Azpsz6k8zy1ZqtBBb-wHQuWbXJILDD60qnTErz_QFcGmSVUseDpfyo3lax9eQF1-VLbFavGCo_nDKjarnk_yIzbyEkI-DmIZPWrK76BbnpXuQ6MynTBjLUBicqwYTr0ODphIRww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e2475d08.mp4?token=ryrJF5TfybtGmqEr-gVN1fiwFjGsddt3NrDrVo5X4thpJ3F8DWm6MQMJPjV4Q3pJ_Cb1Ti5RXBWHI8j_Bntss4H84bBAktAWtNQHg_Y2glOQsGGwsbaN2_QXfqQpfzbd-6zybf0E3eaM-MFZlMDH3qohrRnz-_kll8Aswev2oZ3Lk0R3-kt42SbwqbfIjpAwGetWj3tbFLez3t-Azpsz6k8zy1ZqtBBb-wHQuWbXJILDD60qnTErz_QFcGmSVUseDpfyo3lax9eQF1-VLbFavGCo_nDKjarnk_yIzbyEkI-DmIZPWrK76BbnpXuQ6MynTBjLUBicqwYTr0ODphIRww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محسن خلیلی:
✔️
با کفش‌های بیژن طاهری هتریک کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139506" target="_blank">📅 00:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139505">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
🇮🇷
نظر محسن خلیلی و بیژن طاهری درباره برگزاری دربی در اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139505" target="_blank">📅 00:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139504">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a595378b0.mp4?token=IbG8VX9x2gScwerLePsd4-eL2Lxc8urYWT5d08m1pUKLWputAM1D2Wv05n0oyHQh9sFnYdIYcC2fbOuL456kRHSDIpPZLDHW3UFTBntGmmNqHBja2lWhHrrSoerQGpQtBg1_ZnQg00VjR7tw4AeV1EidNe-t0Pqw3Ky0RcxrW-sJA1xRM-6VQrffAYTw2iMtAecAV1d4By4mT9VUu02jBOsSovOFwyQSKFBjpiicwPujCTUjHGmHwzPuH-YDE-G34ohqH9ONBPtisvp7aEfLrEmpSvcFQbe9P3DZTo0eHWLMtpGcD4wiuD9JQZUEZgvXX6ivRd0iWdpI3BIhJ3JfAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a595378b0.mp4?token=IbG8VX9x2gScwerLePsd4-eL2Lxc8urYWT5d08m1pUKLWputAM1D2Wv05n0oyHQh9sFnYdIYcC2fbOuL456kRHSDIpPZLDHW3UFTBntGmmNqHBja2lWhHrrSoerQGpQtBg1_ZnQg00VjR7tw4AeV1EidNe-t0Pqw3Ky0RcxrW-sJA1xRM-6VQrffAYTw2iMtAecAV1d4By4mT9VUu02jBOsSovOFwyQSKFBjpiicwPujCTUjHGmHwzPuH-YDE-G34ohqH9ONBPtisvp7aEfLrEmpSvcFQbe9P3DZTo0eHWLMtpGcD4wiuD9JQZUEZgvXX6ivRd0iWdpI3BIhJ3JfAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
محسن خلیلی مدیر پرسپولیس: ۸۰۰ میلیارد بودجه لازم تا ورزشگاه آزادی تا چند ماه آینده آماه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139504" target="_blank">📅 00:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139503">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⚽
🎙
رضا جباری:پوریا شهرآبادی جزو 3 مهاجم برتر لیگ است؛بازی در پرسپولیس پرمهره از بازی در تیم ملی سخت‌تر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139503" target="_blank">📅 00:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139502">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚽
🎙
رضا جباری: کنعانی و علیپور با رهبری‌ خود نقش کلیدی در ایجاد همدلی و ساختار کلیدی تیم دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139502" target="_blank">📅 23:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139501">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
جباری، مربی پرسپولیس:  یکی از جذاب‌ترین داربی‌هایی بود که در این سال‌ها دیدیم. تیم پرسپولیس همیشه بالاتر از همه‌ی نام‌ها است. دنبال ۳ امتیاز بازی بودیم که به آن نرسیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139501" target="_blank">📅 22:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139500">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3xCy4G9lJUeQ5YXn7HpJMbqianXpU0AhG3MHjXi_OU8UrVA1UmHqavIAsCYZI-l0_kJyH9VURrwMcL4wpFfaJNtaL6xQZf6fKk-wycR4gpogTD0Km7sTqh7U9cqwtr_scVWw1jQ-NfEBTS99Db5GkRn0LS5MAaQdFFdfJOXW0xC-YWmMtreCLyhMrf2K-t9MdV-XPvKHgvBRmhi60kx_EN2LMgN7rQQ_UbagJ8T5MwUv4aHgZnDOtRn81rIy8oiJu9Cmu7XUlTvd6fgeYULcey_oPnaHCjHl6o7mJ-s9TGp-lsXUhZDpPSMIjjDzrPLzoaNPt2T6Or-AyS2-7L-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تست های پزشکی تیم بانوان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139500" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139499">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK4MQFe--3Gp9W9MoemlvMYIk4hWWADfIyZAqJW-ZwWiCF45JtHv0REe_V9mY6WwVWeNXAWZqBtkAAj8fBbAWJWmqkHbgPS502-hZQj628L46tdCaxsaMycj6MSm75IIJJZZ-WnvnVKQKJsRX62bDq1pGxB36aZuqv_6BVhg4S0cYrH3gmEk0Gcqc3wbC2myFkyYkISl76ytaU8G3sdPoaCOndgteHcCq9lwU-y8Q-v8y5G-ZdvBsEYOKg6hsmQr9YlO2cDIL1-jtSiZDDRTO03e6ePaA4OI5ymMvyXOTPHMcF4LwqANh8S1ICtJI_pWdaJQCBKxteDyv71F8tSeNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کمپانی دیشب یازدهمین بازی بدون شکستش مقابل استقلال رو انجام داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139499" target="_blank">📅 22:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139498">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvSIzqwWRrm7H_0fCcnBW6bIOYWxE6zjkXWUEuuL7bYtXqIr2e0zVV2A5kh5XkJnKlpaPge3Z5pTol4lArvo5ot0k7pcT-J-8iiMIur_3vwR0jUFJqzMDMqO8aPjR1eBSjBnPcSxqModfP_A4fdlQ-_TcDeXNwDI_uNtM2Y3aDT3NWEaDvk-pr9JXfK0njbkKDANZ2OiIUyU0QJl0Qj1tpXPdhVBdCnVw1WFe_8BzVqG1W12MNADnC3xWv4fjywqkmNxCEd7WW-SmzGIAv8LImgQS-DXOh1KKp_jfFf3Fu2yxa-7hhl1Qk0Th9RUE4CsGHtNwnzGL17FJQ8X9a0yGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139498" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139497">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
تارتار ضعف پرسپولیس را پیدا کرد!
✔️
تارتار به این نتیجه رسیده که پرسپولیس نیاز به یک رهبر در خط هافبک داره و نیم فصل قطعا در این پست تقویت خواهیم شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139497" target="_blank">📅 20:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139496">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FS3qeLqJy4W5vuzuwaOIspuct2R9jYXaYEJUVA_comLwYZXjXYE81UJ42rQ8XD3jCHsypYM0McAcRVoY8On6k2hDHawtr75nK1uJwXkRM2x89Z78wlkzaK8N7P43XBfbeGK7hkUaPfECF2n_8mzHqLbuhp9evEG5e3gNsfgOXdCs7nKk_s5Wsv8ts1R31_45dXFRHaCEds7nRIfvCFW7xZTRlZdl0v-razS-uPendaODhdyJPhwlkqyyy69BTfn8P1eYpE5A-M5EGB8OaJl6jiM1-QQJsXeObrW8urEpEg3vGrsWWSFaJMBOqbGb0C_PXLA6zSz21MgQ7NEWUhsTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🎙
خلیلی سرپرست پرسپولیس:
❌
مصدومیت گرا از ناحیه آشیل است. تارتار گفت اول باید او را ببینم و در مورد ماندن و رفتن وی نظر بدهم. هیچ اختلافی بین اورونوف و کادر فنی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139496" target="_blank">📅 20:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139494">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc7XsCU-Sr46_UR5zECvr9fMOt3UiNousw49BnHtl02JAKMHfdpDREu1kYmJp4dqH6Yn9eTvcV5i1mpP-IvjlZI-OQB_mKiRaZlJpuowbl_h9a1vpBrSVs-EEToC0a1DX60pMzAmMFhGT6IrSjggsBhVCtiQnmMZA9P-oHxapgyeT7tj5jG8MjnuC7UZhATqv7ae7XX0HtbOEbYwcvFv_9sy9ccHgUZuiVek2n3OnwSvzyDiAcgbDVRQqqX9NzAVxk_SJTpuo77qzMtDH6NSwPL8ye8UoE3zDseuBdwHUPs7w5I_PIfQg6fH6pYKR5KweLcePhXAEQ5QFxOifta_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد سرویس و قدرت در نیویورک
فریتز به‌دنبال عبور از سد بلوچی
شانس بیشتر با ستاره آمریکایی!
[
تیلور فریتز
🎾
🆚
🇮🇹
متئو بلوچی
]
🟡
تنیس یواس اوپن
⏰
امشب ساعت ۲۰:۳۰
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139494" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ7-JC0V_e5HpNe1Ay_4Izmsb_5GhkmLv1xg9mulB1IUOq6EOoPShgGbOJSDQ33pGMeLLUFdMLoyc1OQWQTs__Wv_QUI5moRgRpyaD76fU9qLGfYzqDFms-L6K_OUMFhKHB3hSyGKyRXxQSwNBR-QUf1tWyy5aaknH5esIWjdaakOp1p3DT-qQedKS171WyjkWDhWieSCWdqv00Na2E3pFMmNon0GMXnJ-7TFwHzzqOpAe3otjBwWLHeN98feiDhW7t4NsJA-Z5YFUoXPohdB1dl3khP7NI0Q8blU1kCiKdBUTK360C988YlIrgoVPeUgsGJ_YbwIebtcq4wzEGaSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حضور ابوالفضل جلالی در بازی امروز
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139493" target="_blank">📅 19:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYG6H70ILodutaHC_Vb6cHKlHrzCeaioVSPV6vGW4tZgUjl7PUSg-7vasbhiMMnYOzlWwWHDHlwgYWzw1FwEQAc-XNUXTjL25IccvyMbG8SzFZTSBp_TtzzKQOuRJlO5vvNNTOpGjGT3hBdi7NWfHXLs2YME0TAQcoQYpYRbn_ePeZbfwSJX15DnJr3cer5xepKKjHRv7qVHkytQmbobBET71gDfgj3f8-mSUv8jiJO4M5xRKKtteHPy-6JZaCfpO-hhcgqrOvYNqsVH9wUtNOyAHwfZ1fBI0bLmjiAinaH-IdXgRX86uR5Lrn7puvVmhiSWqmpP9H1ASHDg1aATGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
محمدمهدی محبی زننده ۲۰۰ مین گل تاریخ دربی بود
👌
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139492" target="_blank">📅 19:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">#بماند_به_یادگار
🔗
💯
تا روزی که اردوبادی و اینانلو داخل هئیت مدیره هستن این تیم رنگ آرامش نخواهد دید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139491" target="_blank">📅 19:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is3Pl3_Qhv4tiR71Q4Q5pR42Ne8KgzT3CgIWXpgb0i9MvTvFD7_Jmkf3Dz9OyvVTn2ruhsOUWy9IsEyLrNQNjOrjhnNbqwFC2IOipqr_hQfdFUzogu_nC_HgvazW2wMa0bxPsyOT8_x3WSCBU_25PEzYm_OzjGbQsuDwF08lqClYduc4mAGVSfaxtGWR2ggF5_jepfrL-d7iEuAHkngGwUbZNrFQN9O2TlNSEsCO05spuMsgkoMj7PodG2ejOIsjhgoLSUPKy17GI9UR9FtEUvglM2J8GWLrQHNy2vgACybrAVGSddcwmw0Ta03xLD7DVInlT1XThSxcvq2F6v93uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
پرسپولیس امروز در دیداری تدارکاتی به مصاف مس رفسنجان رفت و با تک گل پوریا لطیفی‌فر به پیروزی رسید.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139490" target="_blank">📅 19:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139489">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v90stKCgq1ZCxA4w_-s2__aEuOPOQSWO_VMX4BF7FE4Q13rFizrpkGsEE4UBPdQCgyBtQGnLtTjcFq3rlkCtYRPoL83adiqAhEI-PaGJAXdBUxH3_n-6x1XAQUjZgHP3pTth7EM_WhdAp0Y0pO3fB_K3lf_VhqJ6jPTqzn-6Y70H4_ZaKaE_oA1zsY5ainoykSdr3RAmiUgwuh5BrnQcmDofuuYcjq-KCEq1n6fK-R8OPDFcZhJF-vma-CKGwea7eZzsSE0hwr1l1p7ZpY5r8d-4aTDAKXVM89Sgu-RQRitJCE6ssovUaWrV1ewT0IWgYBwwBDp04IP0TWdaMUhL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
محمد عمری از فصل قبل تا الان توی ۱۷ تا بازی برای پرسپولیس فقط ۲ تا گل زده!
⬅
⬅
با اینکه آمار همه‌چیز نیست و کارایی بازیکن روی بازیِ تیم هم مهمه، اما هوادارها اصلاً ازش راضی نیستن و انتظارات رو برآورده نکرده. امیدوارم بازی دیشب براش درس عبرت شده باشه، تصمیم‌های درست‌تری بگیره و بیشتر به درد تیم بخوره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139489" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139488">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139488" target="_blank">📅 18:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139487">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3Xuu2SaItUB8mEcgS20AoxTIRpUPZZ5urYRBMqqqpo6cPxmUS9gI43Fa4orxtW4QF56ff_ALfMbXLDnJolVOTXDRzVDtMYlEnSi-beNh8BSYFGs_3xUS5tb-MGmJz8eoFVBE17BytK23WrVPcNK0ZoP6HMyYnEAP1cZb0y_3OGvJ7RabvQOAPm9UI1H-Pi6ZdPKSpI-87CWiSBu-LGWEhEwjWE793HSACtApugSAv6UVZbuHLl3fFVDPuci0VsGSMj9cwH2GjNeU5A9uNuzbwbn9m9EgIgl2cDCInm2xknDY_Rtmpoi49HJFmOa0gk8aFc3XDW3oyCZ-ddOhAfXPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139487" target="_blank">📅 17:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139486">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
دانیال گرا مدافع مجارستانی تیم پرسپولیس برای هفته پنجم از لیست بازی خط خورد تا یک سهمیه خارجی سرخپوشان برای فصل آینده به خطر بیوفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139486" target="_blank">📅 16:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139485">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
خبرگزاری مهر:
🔴
پرسپولیس پیشاپیش شکایت خودشو برای حضور یاسر آسانی تو دربی آماده کرده. پرسپولیس اعتقاد داره کمیته انضباطی و سازمان لیگ صلاحیت لازم رو برای پرونده درباره یاسر آسانی رو ندارن و استعلام فیفا باید منتشر بشه
🔴
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139485" target="_blank">📅 16:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139484">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
❌
❌
طولانی‌ترین روند شکست‌ناپذیری در تاریخ دربی؛ پرسپولیس با 20 دربی بدون باخت
✔️
✔️
کیسه کش حسرت برد دربی رو به گور می‌بری
😂
🫵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139484" target="_blank">📅 15:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139483">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=D0hMV9dSTG4KCZU86K9dmN1s1jhXcuf7DOFfiTubAe9x47ZezaVCDEbGg_E8SEjuiw-15oxmDK3Gvz8xq-9KWs6HHKk9Qfu9vAGdRst1hH5sXiUpoL1ZzfSTyVv6S4yMhdzML0IFXzx--teZ8hKvBmaMV5EOoHJRvNKSlLAS2XKsNNKr2iEAp4VmWu16WTXyuXm7z0q30C3s6hmuxHsE5VyXEah8WHigRXsQ1TjpnPGotBOxlImIxLjTi8S54tsicUmWkDQ5aha3n7RA1fze_6YI0oP57KDJQvHVqLsa_anz-UsZd1cL2TWnJsSlx8cOub-S75puGCKlcE9-dJlMQ4YIoXKFGVuFfukPAswPM9IKmHLUCGrAXsQEOiJQKEl2vz--2VB4Owriv-Q9fhfvV7qXXHXTM9uQea9ROnFYAiU6aGeKtb5ovx0YQRZfQQF3FeKZ1q9JW8Bm5oGAyVQQpNPlhHqT7RiJwMSuhTMJ4WVYn5zgdM2cXf_ULw90QQ8gsh1pWpoTUXEY2s_wbcr4Y6TMddkt8qEWw5waV9iSZs4SBf-2Y_w4PnpR3WrILleXIkQOSuxJuTXheeYf4--wftOWhZ2ENYNfWkXmRa-3P7kbH4uLP5qRXv6t7GcVCS9zLsTO38pkgP2wA0Ox2xLG9NG9pEWamFTI2m1ffJn4-ck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=D0hMV9dSTG4KCZU86K9dmN1s1jhXcuf7DOFfiTubAe9x47ZezaVCDEbGg_E8SEjuiw-15oxmDK3Gvz8xq-9KWs6HHKk9Qfu9vAGdRst1hH5sXiUpoL1ZzfSTyVv6S4yMhdzML0IFXzx--teZ8hKvBmaMV5EOoHJRvNKSlLAS2XKsNNKr2iEAp4VmWu16WTXyuXm7z0q30C3s6hmuxHsE5VyXEah8WHigRXsQ1TjpnPGotBOxlImIxLjTi8S54tsicUmWkDQ5aha3n7RA1fze_6YI0oP57KDJQvHVqLsa_anz-UsZd1cL2TWnJsSlx8cOub-S75puGCKlcE9-dJlMQ4YIoXKFGVuFfukPAswPM9IKmHLUCGrAXsQEOiJQKEl2vz--2VB4Owriv-Q9fhfvV7qXXHXTM9uQea9ROnFYAiU6aGeKtb5ovx0YQRZfQQF3FeKZ1q9JW8Bm5oGAyVQQpNPlhHqT7RiJwMSuhTMJ4WVYn5zgdM2cXf_ULw90QQ8gsh1pWpoTUXEY2s_wbcr4Y6TMddkt8qEWw5waV9iSZs4SBf-2Y_w4PnpR3WrILleXIkQOSuxJuTXheeYf4--wftOWhZ2ENYNfWkXmRa-3P7kbH4uLP5qRXv6t7GcVCS9zLsTO38pkgP2wA0Ox2xLG9NG9pEWamFTI2m1ffJn4-ck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
❤️
👀
✔️
تو این صحنه کسی متوجه نشد ولی وقتی از دوربین نزدیک تر صحنه پخش شد مشخص شد نوک انگشتای نیازمند بود که باعث شده توپ به تیرک بخوره وگرنه گلو خورده بودیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139483" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139482">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
20 بازی بدون شکست
🔥
✔️
حسرت کیسه در آستانه ده سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139482" target="_blank">📅 15:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139481" target="_blank">📅 13:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139480">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭕️
⭕️
⭕️
با اعلام یاسر همرنگ
🚨
کوپال ناظمی داور دربی شد
📺
موعود بنيادی فر داور var شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139480" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139479">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139479" target="_blank">📅 13:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139478">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYxrBqESW7pmCfrv62o0zmOdC_Je6GfVBR_8pnaF6QaA_OHKT6OLTkcQoy1b3gps3b2vJmneHZAkhVMu_ehBrciob3nViWeRk37Z87IbZ_cLkCcFTMg8Vk-LByxJIIMLgRmwuXFRMilLgVLRpVqB3MeilX_ajX7Gc9P85qFbnLsYmwvBqtWj4q_RTbhlL8yDrhQfbnn3yZsKH1CAKKDS6HjDJm0Ij94ONEpbeD_GEha6esT1J4hStSXIysfsi0wVphSVJWU8uQn4SdQoZAubqGL64uMNslgrWn9eO-h6MmYjpjXoRKOHGjrkv6ueI9ug3XB4HxiV5t265BP9WtpmFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سوسیداد و سلتا؛ جدالی برای سه امتیاز
دو تیم آماده برای یک نبرد نزدیک و تماشایی
کدام‌یک دست بالاتر را خواهد داشت؟
[
رئال‌سوسیداد
🔵
🆚
🔴
سلتاویگو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139478" target="_blank">📅 13:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139477">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔄
🔄
🔄
با حضور یاسین سلمانی در بازی دیشب حالا مهدی تارتار به تمام بازیکنان پرسپولیس بجز محمدحسین صادقی که تا حالا در لیست قرار نگرفته بازی داده و تمامی بازیکنان با ذهنیت آماده به سراغ ادامه‌ی لیگ میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139477" target="_blank">📅 13:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139476">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🤩
| فارس:
🔴
❤️
🔄
تارتار امید چندانی به دنیل گرا ندارد و حتی درصورت بهبود مصدومیت هم نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139476" target="_blank">📅 10:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139475">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139475" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
