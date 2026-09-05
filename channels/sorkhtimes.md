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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 17:26:02</div>
<hr>

<div class="tg-post" id="msg-139580">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇿
پاختاکور ازبکستان 3 بر 0 الحسین قهرمان اردن رو برد و به لیگ نخبگان صعود کرد! بشار رسن، هافبک سابق پرسپولیس یک گل زد و یک پاس گل داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/139580" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139579">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
محسن مسلمان به کادرفنی تیم امید پرسپولیس پیوست  مسلمان با پیشنهاد بهادر عبدی و بعد از جلسه با ادموند بزیک مدیریت آکادمی پرسپولیس به عنوان مربی به عضویت کادرفنی این تیم درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/139579" target="_blank">📅 16:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139578">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hid2kwPy8ytqksZ863fpn-jPSmWfxmN2y3C9kn-P_zY1Ez8q8wFcsl160NK16CaIk3grGn-qcIZofzVclMrQJn-Pj7-9OVnpiRrVfT1d7NDlzLceZBOze1qGE-xo4zOEuUhCxgjwWJgQb8sHMPNZQAwC4Ljh44-E2PXZn-fQxaDQq_Dxn5JqTJV0Nb2BUDw1zoWvaTCRlZJHnqVlQymuH11Y6GoBs1wFnxFdgVE8tiafwf40qX0wHVziGEqo64n4di-HGmy8srXDFripm3gxVxrG5KhGojKQcx3H2TUXm-cDoMQ6vjiF3J1PibtSDZQRGXYijXJzw-LaXx4qcr2pbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
حکم سنگین فدراسیون فوتبال علیه مهدی قایدی
⚪
با رأی کمیته وضعیت فدراسیون فوتبال با توجه به شکایت علیرضا نیکومنش از مهدی قایدی، این بازیکن به پرداخت مبلغ ۱۸۰ هزار دلار بابت اصل خواسته و مبلغ ۵ میلیارد و ۴۸۹ میلیون و ۵۷۰ هزار ریال بابت هزینه دادرسی در حق خواهان محکوم شد.
⚪
نیکومنش مدیربرنامه سابق قایدی است که گفته می‌شود واسطه انتقال این بازیکن به شباب الاهلی بوده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/139578" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139577">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
✔️
روزگار خوشِ «مملی»!
❌
❌
محمد خدابنده‌لو بالاخره در این فصل به فرمی که هواداران پرسپولیس انتظار داشتند رسید؛ هافبک جوان تیم تارتار حالا تبدیل به یک مهره اثرگذار و مهم در ترکیب این تیم شده و روز گذشته هم در دربی ۱۰۷ فرصت داشت یا یک سوپرگل خودش را در قلب…</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/139577" target="_blank">📅 14:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139576">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-kvd0_cOeeGNMCdzFKSH6XAiHGtkJKvkqShsjOLcXS4BT8rkl-YjtvKgv6kS1vme78NAXhEZ5PKD1oNbiDp5Vrwh3IDMS98EvUWqc5W8RnUIfa6GDyJHgpox08gosrLVe7PdxCwtViC5jYBKaPOyKo97EtudQKP2Nxi8bFqgyRQ5NQzz3L_vvHQalNBL5J87PTBztHfNQUeDeAEjo7-OEUEYQnbcwwgHfp2lVTaPC2hLMfe-7QY3Y6iAEUbXuzzG8qMOcW_gZRE1p-6IzIpRggWlKgQxeegUmIKXEDo6-gftTQ6G8WWHg6R-DdQGpFqptyzpyHCCVcBaErpQHB1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کنعانی‌زادگان به ۱۱ دربی بدون شکست رسید؛ اما رکورد همچنان دست عالیشاهه با ۱۸ دربی بدون باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/139576" target="_blank">📅 14:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139575">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
⚽️
✔️
پیام نیازمند با 3 تا سیو موقعیت و ثبت کلین شیت بهترین دروازه‌بان هفته اول لیگ شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/139575" target="_blank">📅 13:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139574">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/139574" target="_blank">📅 13:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139573">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-YgUDbv19mJGnz6Qgz0WeSCHFA6h_lhwxV3CmZQGqWzsZUnFix6Dt84jFfjkpGVOk5jiV6GwH55ViOxJmr6wPSzJ-iuxplDxyLXg11UeCrwXjWfYoyeMeR7Z9oI-dFJUSLbNoKf7Dk5RXIw-N2MCe-r3GRoatO1MRyPwe9WwaU5gZLqS4ieJnRQdH6lDW1ApSZ8u-YfClRsYvvMutghZkTMe4id9gMfwFFCB4XqfmqnjV5RayWdTkNIwQQ1oMUo9x-qReflh7gbZ2_52AnzXClF3MoI_Bp41J8A-ReSjfHqmBgAmWsMQGROJIEbRvcmgubXdcW8dvcJaT7MfjwBNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیس از سوی کمیته انضباطی ۱۵۰ میلیون جریمه برای استفاده از مواد آتش‌زا و سر دادن شعار علیه بازیکنان حریف و ورود تماشاگر به زمین در بازی با ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/139573" target="_blank">📅 11:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139572">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
احتمالا در بازی با ذوب آهن بیفوما زوج علیپور خواهد بود و وینگر چپ پرسپولیس تغییر خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/139572" target="_blank">📅 10:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139571">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/139571" target="_blank">📅 10:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139570">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم در واکنش به صحبتهای قلعه نوعی که گفته از خودگذشتگی کردم اومدم تیم ملی تیتر زده که آقای قلعه نوعی میتونه دیگه ایثار نکنه و از تیم ملی بره و برگرده لیگ برتر همونجایی که تو ۱۰ سال گذشته هیچ افتخاری کسب نکرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/139570" target="_blank">📅 10:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139569">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚽️
تمجید ویژه پیوس از وینگر جوان پرسپولیس!
◀️
امیرحسین محمودی در دیدار مقابل مس رفسنجان آنقدر درخشان ظاهر شد که فرشاد پیوس، سرمربی مس، از کیفیت بالای او تمجید کرد و حتی از بازی نکردن این بازیکن جوان در پرسپولیس تعجب کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139569" target="_blank">📅 09:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139568">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139568" target="_blank">📅 08:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139567">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139567" target="_blank">📅 02:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139566">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
✔️
شنیده میشه عباس کهریزی ستاره جدید فوتبال ایران پیشنهاد اولیه استقلال رو رد کرده و گفته تمایل داره پرسپولیسی بشه /ورزش3
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139566" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139565">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139565" target="_blank">📅 00:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139564">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139564" target="_blank">📅 00:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139563">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139563" target="_blank">📅 00:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139562">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139562" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139561">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139561" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139560">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎤
⚽️
وحید فاضلی مربی پرسپولیس: میتواستیم بعد از گل عقب بکشیم و به راحتی برنده مسابقه شویم اما فلسفه تیم ما این بود که برای گل دوم و سوم تلاش کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139560" target="_blank">📅 22:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139559">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139559" target="_blank">📅 22:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139558">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
برخلاف شایعات هفته هفتم لیگ برتر کنسل نشده و قبل از فیفادی برگزار می‌شود.
✍️
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139558" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139557">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
✔️
کم بازی کردن اورونوف بخاطر ترس از مصدومیتش هست و داریم دنبال راهی میگردیم که نهایت بهره رو از این ستاره بگیریم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139557" target="_blank">📅 22:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139556">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
✔️
کم بازی کردن اورونوف بخاطر ترس از مصدومیتش هست و داریم دنبال راهی میگردیم که نهایت بهره رو از این ستاره بگیریم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139556" target="_blank">📅 22:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139555">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
جباری: سبک بازی ارونوف و نوع بازی تیم با توجه به تغییرات در حال هماهنگی است و به مرور زمان بیشتری برای بازی پیدا می‌کند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139555" target="_blank">📅 22:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139554">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
معاون وزارت ارتباطات : با اشاره به تجربه قطع اینترنت در جریان جنگ اخیر کشور به سطحی از بلوغ رسیده که حتی در شرایط بحرانی و التهاب شدید نیز میتواند بدون قطع اینترنت مدیریت شود و دیگر شاهد قطع اینترنت نخواهیم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139554" target="_blank">📅 22:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139553">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139553" target="_blank">📅 22:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139552">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139552" target="_blank">📅 21:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139551">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139551" target="_blank">📅 21:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139550">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139550" target="_blank">📅 21:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139549">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139549" target="_blank">📅 20:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139548">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139548" target="_blank">📅 20:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139547">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👀
❓
محمودی ۱۵ دقیقه هم بازی نکرده امسال… اقا تو پستش ترافیکه درست ولی نمیتونی هر بازی بهش ۲۰ دقیقه بازی بدی بازیکن روحیش از دست نره ؟! محمودی چند ساله دیگه عصای دست پرسپولیس میشه اگر آقایون نسوزونن بازیکن رو…فقط بازیکن هایی که از گل گهر آورده رو بازی میده اقا…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139547" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139546">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
با اعلام باشگاه پرسپولیس، آکو باتری اسپانسر جدید این تیم خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139546" target="_blank">📅 19:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139544">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139544" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139543">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❤️
❤️
باز هم بزرگی و عظمت پرسپولیس در این سال‌ها به بهترین شکل خودش را نشان داد
🔻
🔻
در سال‌های اخیر، بازیکنان زیادی با آرزوی رسیدن به پیراهن تیم ملی، راهی پرسپولیس شدند و پس از درخشش در این تیم به هدف خود رسیدند؛ گولسیانی و گندوز نمونه‌هایی از این اتفاق هستند…</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139543" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139542">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: ما پیگیر شکایت از یاسر آسانی هستیم و برای اینکه پرونده را به دادگاه CAS ببریم ابتدا باید در کمیته انضباطی شکایت کنیم و جواب بگیریم بعد به CAS ببریم
✔️
بعضی ها می گفتند ما اورونوف را بازی نمی دهیم که او را  بفروشیم/ واقعا خنده دار است چرا باید…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139542" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139541">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
جنجال و حاشیه در اردوی کیسه؛ با اعلام سهراب بختیاری‌زاده، صالح‌حردانی بدلیل رفتار ناپسند و درگیری با سرمربی و یاسر‌آسانی در بازی دربی، تا اطلاع ثانوی از حضور در تمرینات کیسه منع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139541" target="_blank">📅 18:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139540">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚪️
⚪️
⚪️
فوتبالی: سهراب بختیاری‌زاده به حردانی، مهار اورونوف و بیفوما رو سپرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139540" target="_blank">📅 17:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139539">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
نصیرزاده: شکایت از آسانی، دنبال نخود سیاه رفتن است!
✔️
تیم‌ها با شکایت از آسانی دنبال نخود سیاه هستند؛ فقط استقلال می‌تواند از این بازیکن شکایت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139539" target="_blank">📅 17:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139538">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139538" target="_blank">📅 15:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139537">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
رضا جباری:
✔️
این نسل پرسپولیس از لحاظ اخلاقی و فنی بهترین‌های حال حاضر فوتبال ایرانند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139537" target="_blank">📅 14:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139536">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
کیسه و ترتر شش امتیازی شدن و کلین شیت و حفظ کردن امیدوارم فردا بازی و ببریم و پیام هم کلین شیت شو حفظ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139536" target="_blank">📅 13:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139535">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
🔹
تمامی گل‌های هفته پنجم لیگ برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139535" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139534">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87b97822e9.mp4?token=nVkQxEKPM-M4VGvsnguJHIwIbJDb0TtpoRfeK5Fk-R3Lx1m9UyveQOSTz8bjqn64SoXLWjCU76qiAPzpf3cZmwz8GK2uzkUNWdGAMJTAw5FXJkB0mOtqVuiy4oerOxhtqfVyJJXoPus0m0ycfmXhU1tU-_Ni8nikISJFr7miiLE5bQseToecnPH13vF9DbkcRsyf6f3sgGsAuxC0A7WNjnyql1YsbeVTnPY9R4dxMoSvL53pyK1VJ8D3vCG1WOq3NamCRxXtSJ4TrUp_7CUWedHZVmOWiH3DRNx3FHKnyrVhBeSYCualwjJxJ1NKLvxSmWA5htlQf8bIWp_fNpbS5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87b97822e9.mp4?token=nVkQxEKPM-M4VGvsnguJHIwIbJDb0TtpoRfeK5Fk-R3Lx1m9UyveQOSTz8bjqn64SoXLWjCU76qiAPzpf3cZmwz8GK2uzkUNWdGAMJTAw5FXJkB0mOtqVuiy4oerOxhtqfVyJJXoPus0m0ycfmXhU1tU-_Ni8nikISJFr7miiLE5bQseToecnPH13vF9DbkcRsyf6f3sgGsAuxC0A7WNjnyql1YsbeVTnPY9R4dxMoSvL53pyK1VJ8D3vCG1WOq3NamCRxXtSJ4TrUp_7CUWedHZVmOWiH3DRNx3FHKnyrVhBeSYCualwjJxJ1NKLvxSmWA5htlQf8bIWp_fNpbS5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
گل محمدمهدی محبی از زاویه‌ای متفاوت
▫️
▫️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139534" target="_blank">📅 13:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139533">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
فنونی زاده : به حدادی گفتم حواست به خلیلی باشه میخواد مدیرعامل بشه و زیر پای تو رو خالی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139533" target="_blank">📅 12:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139532">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚫
عادل فردوسی پور: با دیدن فوتبال ایران میتونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139532" target="_blank">📅 12:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139531">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139531" target="_blank">📅 12:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139530">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139529" target="_blank">📅 12:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139528">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
فرصت به ستاره خاموش سرخپوشان نیز خواهد رسید؟!
✔️
✔️
مهدی تارتار قصد دارد بصورت چرخشی از بازیکنان جوان خود در ترکیب تیمش استفاده کند و در هفته‌های اخیر شاهد بازی کردن بازیکنانی همچو سلمانی و لطیفی‌فر در پست خط هافبک سرخپوشان بودیم.
✔️
✔️
حالا بنظر میرسد…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139528" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139527">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
پافوس قبرس با هدایت ریکاردو ساپینتو از پلی‌آف لیگ اروپا حذف شد و راهی پلی‌آف لیگ کنفرانس اروپا شد. تیم ویتبسک بلاروس هم که میلاد محمدی را در اختیار دارد، از لیگ کنفرانس حذف شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139527" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139526">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: هوادارا فقط میگن چرا اورونوف بازی نمیکنه؟ خب وقتی بیفوما در آماده ترین ورژن ممکن هست چرا اوستون بازی کنه؟ بیفوما خیلی خوب بازی کرده و حق دارد فیکس باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139526" target="_blank">📅 11:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139525">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی مدیر پرسپولیس: بیفوما الان شرایط خیلی خوبی دارد و دارد خوب بازی می کند ولی دارند حواشی درست می کنند که چرا ارونوف بازی نمی کند. هواداران ما  باید صبور باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139525" target="_blank">📅 10:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139524">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGmUsb2eon62gfOrFsZgxuywb9M2rvBHsMuQmq0-GI4v7qRM1suLB0OmfBlUkaaUgDRAJyrvb-zQeDMRv4uB3xYfhY93BDY2kegJwGY5wDGJ-9h7BCJY__NLZiO_YzaINjEw7A2--mlJJ1TcezuktjqR6CA1hf_G-cGCFHzg98c5HXgHads4yRlYrif6BAZ8sNc48zLp1ZbLpQywfsshZygDtPC28G6e0Ub_KgiH81VPmr5KlNdAoGhrovH3bzQ7uC_9Ga7y-5MTDd9gu5NmdPaZIn4fqa4o0ti4FYUOQ9cZEFLctX406n4MYKQPp3eqhlGtFzg5h_z9EKphMWTIWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❤️
محمدمهدی محبی زننده ۲۰۰ مین گل تاریخ دربی بود
👌
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139523" target="_blank">📅 10:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139522">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❤️
صبح آدینه تون بخیر و شادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139522" target="_blank">📅 10:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139521">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDfaGVDKpCmxjQGIrAGLK3fZjKRQPbDm_a6c33NYYBCjAxcqsdOIML4i44PN6JAmgb08vHAcsuQUjjXQZyPBi6TFYiNlveJ0c-AwOlPe3OggZA645FTYiVlQc7PbJ861uRnnSV25lwldr-tDDzQYiDkFM2tT6J1wp4b7hyydFmKIb6VNgKjOL6xXnFns3wuqEoj2yciO_ivrEHQo1ttmvauno0BR5BoHGwCnYDyeMbF_skC3KUScrAxf-G6EMXjxyZpw8anxhw-X_kuJEIFYzJC5JhnWlYe_oifexVsytAL5TRzXc57HIizS7O9c57rDaDjK2zxzGS8VC3xB40Nyqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139521" target="_blank">📅 02:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139520">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7wP3j_IdgK4bpja8g1wDsBMEnJF_7oYaNyQ5uEXcS6y8THS-nPTAPldg-SdKhmMcAC5Wnq8sInsy5fCpbJgeiXq665SwCrGtDRgkNh0QJfv2w_89JSWIONuFHWcN4WITDhaxOK-3ZVCr_oQB6puHxxmpz1bnUcLChWsTSpWePASTPfaTHyK8IvVyFGduqKLY4mI3ehmtL6Dh1c9YzLJh9II9XGNAVKbQ5rHsrXPOj0FhujQwRT15s4glVDIftbc__CslNw8jo-IH4k7a--ruPDo2gh6p9NxrmbT0hOxVG8RT8lFkMHyq1TDoS_FaDgfK7iBdBuS7BdQMd1NE5wMZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139520" target="_blank">📅 01:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139519">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=BeI0zQwhlLWDDFval-lpZlUV2Si8y9kHdTCfLJAfCw06tuvDsWvEVSMNl_AmL9oR7AYGyXXB049Ig_GRIB6_r_9t2AEPGhk7Lpvh0cUapbrwE5Vz5OyswbPkN3P2-3CWbrYMerqzPqcvr2E-BGwGG7mBkNL7iSUrG7jLQPnL2FFKMsR0PM0bLnfaFr46DWhcDoAz9zvN15CEStbknGk2foglxka_hAGlnLFKIpjSXA__xqbRDGiuMbsO3jqqYRkJ9yHAYhvH7AiVE5AlgsvyuUR4TbYd19C4S95hqH19IbXgi5kIQ2uRnpGVxaNUu7A65zdXji35DhWZpyLL6CycWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=BeI0zQwhlLWDDFval-lpZlUV2Si8y9kHdTCfLJAfCw06tuvDsWvEVSMNl_AmL9oR7AYGyXXB049Ig_GRIB6_r_9t2AEPGhk7Lpvh0cUapbrwE5Vz5OyswbPkN3P2-3CWbrYMerqzPqcvr2E-BGwGG7mBkNL7iSUrG7jLQPnL2FFKMsR0PM0bLnfaFr46DWhcDoAz9zvN15CEStbknGk2foglxka_hAGlnLFKIpjSXA__xqbRDGiuMbsO3jqqYRkJ9yHAYhvH7AiVE5AlgsvyuUR4TbYd19C4S95hqH19IbXgi5kIQ2uRnpGVxaNUu7A65zdXji35DhWZpyLL6CycWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139518" target="_blank">📅 01:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139517">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: شما تعویض های تارتار در دربی را ببنید که تماما هجومی و در خط حمله انجام شد
❤️
محسن خلیلی: اینجا پرسپولیس است شما نمی توانید ناگهانی 80 درصد تیم را جوان کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139516" target="_blank">📅 00:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139515">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚽
🎙
رضا جباری:پوریا شهرآبادی جزو 3 مهاجم برتر لیگ است؛بازی در پرسپولیس پرمهره از بازی در تیم ملی سخت‌تر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139515" target="_blank">📅 00:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139514">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBfACb4oB3r1xc2KtHBelvmwq7ehVEkh_MI1mteIY1KZ16Cj6RcIrmnArs4SqgxIQczCVW9k2V6HmwnGLgN1DmllKRW0PfqYAPDjTFxiXrAMuFGMNy9gXoQDqmZ4B_KZig61lqacANxAI0-tAfhp6JSnltVzeFqu8E9BGm9fUyKgR8Qc5sVZ3-_sDUEIvt9bJlIhgkSP8sEBM3cQcjNbDn6KJPcec9nPHjOCSFmQwmEEmtkqbve6xbcVJgOQJDrkZeIbwmSEhbUMzb3AaBwIeSGY6d9pgL6lkjCs-noLjYq_jjbdYl3TGYv_loo_fGhljTpw-3iN3BtZdK4t6CTgwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👤
محسن خلیلی:
✔️
با کفش‌های بیژن طاهری هتریک کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139508" target="_blank">📅 00:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139507">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
جباری: سبک بازی ارونوف و نوع بازی تیم با توجه به تغییرات در حال هماهنگی است و به مرور زمان بیشتری برای بازی پیدا می‌کند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139507" target="_blank">📅 00:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139506">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e2475d08.mp4?token=dnq100c9Cnc6D6KSnJ2u7lv1j_IR10g7kZu4kMceE7f_RaIdxkZI8Kr3zd0Sk9rmXICjfbOCd-FEPIyw64uGxdq_gqFeqdqhzanL8llQOxgXXTjGbUYO5x5LhtGAO-3v7mnye8w8yuNZqFsQuqn6BGGgXAnq_dZmcR7V7Y8ZoJzdR_zGrbWwJQhIQuhGVJutvzrxmBm3QCka-BafaMZfLBRaf48O2u7oFPmzhtQoUT-5z0VjjjwMPOdRPWbTt0QCctG0vi0AUiWav-AS7GWGPfNhs5_3hChCkInbTBb1ibMBF5lb6bqZv0BFH1PlCLVV7CYPfDmaSCuTDRQwxQtxBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e2475d08.mp4?token=dnq100c9Cnc6D6KSnJ2u7lv1j_IR10g7kZu4kMceE7f_RaIdxkZI8Kr3zd0Sk9rmXICjfbOCd-FEPIyw64uGxdq_gqFeqdqhzanL8llQOxgXXTjGbUYO5x5LhtGAO-3v7mnye8w8yuNZqFsQuqn6BGGgXAnq_dZmcR7V7Y8ZoJzdR_zGrbWwJQhIQuhGVJutvzrxmBm3QCka-BafaMZfLBRaf48O2u7oFPmzhtQoUT-5z0VjjjwMPOdRPWbTt0QCctG0vi0AUiWav-AS7GWGPfNhs5_3hChCkInbTBb1ibMBF5lb6bqZv0BFH1PlCLVV7CYPfDmaSCuTDRQwxQtxBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a595378b0.mp4?token=ESwP2fBnhSh3ejQi_oXxaOKgs86usLt6qE8950K0VzaSBNy0fjZcLa-4xwO8TFvwBTNy9iKb69iki5u2ZOQ1MnyCttjZgq4YLGP2A_v6UpI0HPRvMZqLdChwyixYGZJ4VRSvcBdLz1PldaNlqN0djIJfVjRDYqofOmfKFx3fGG5rxFpYJE1mt1IX2PCfF9pqhs24YgbfEvZrjmJ8SATCkUvuboYwSjNOHTzp2vZanvXj5l_TOB6QqqDUCDkDSQfrE1vMi6cOdFomoWa_jwP4EV7Gx3TqtyPdHP0eAb5XGfMEBn56fLMH9k2iIpNFM4MZ_ddpxb_9VDVDEwfCa6JRxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a595378b0.mp4?token=ESwP2fBnhSh3ejQi_oXxaOKgs86usLt6qE8950K0VzaSBNy0fjZcLa-4xwO8TFvwBTNy9iKb69iki5u2ZOQ1MnyCttjZgq4YLGP2A_v6UpI0HPRvMZqLdChwyixYGZJ4VRSvcBdLz1PldaNlqN0djIJfVjRDYqofOmfKFx3fGG5rxFpYJE1mt1IX2PCfF9pqhs24YgbfEvZrjmJ8SATCkUvuboYwSjNOHTzp2vZanvXj5l_TOB6QqqDUCDkDSQfrE1vMi6cOdFomoWa_jwP4EV7Gx3TqtyPdHP0eAb5XGfMEBn56fLMH9k2iIpNFM4MZ_ddpxb_9VDVDEwfCa6JRxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzCWNC26ggIlsHxpMf-NFDmGoePu0Kiw6Dak5l6PlsUHy5BhT71sSpvyYSk_2IlUiTuT2cyZigxTZf7lcPRCsGBXR5DTFcSG9UNgFqoDW5k4tLf5G8F_J2603bPQu3dyEA3thep-0GvFwBj8lhU5DFbxdxYTtrE9o_ddDT5CI030CuKh92eRKjMp0nDd6YQoyqo1ZccULjtTSOmFrVoEVTS6Ag027fO0CzMJHfClS2KPBZIHFo3iN3EblT9Ab2MQH11HIW-rvYYprxEAkBlQP-GJASJeSX_8WRK2u6mdFbUd2W7rH2g1QuGrEfIAmsIJuLsRWlu9t1ewGDSL7ZbGbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تست های پزشکی تیم بانوان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139500" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139499">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqjfLQDbLNJ0mor1wGPOcLeV0L99ScNw74QdBThulkAhu8tgkfRvRdcikgff-qkyaUySzcAbdiJcuZrwAWnNlZfL6Ogj7GFa3u36_eGK3CrxAkWgbhTriJ2ZYqHu8nf8Msa3Z1c9jV43dxExptCnKe4e_mvyl9iDXHEsUcQIMC3LrPP1Uy-mL9sKv-O2JdH9SVrjhdci2T0uFjBKvVkm94_wGItaEAEqHLEfelpcq7WE8cPEXKTPQP0UgPpQEEsKux9IktZ2I9Lifg8i3K31GeHXnvZK94H0aFKTlFM3MAPLb2YySkRJmgn4mFz-dFMyhRx6r384V_tQW56CJHP98Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کمپانی دیشب یازدهمین بازی بدون شکستش مقابل استقلال رو انجام داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139499" target="_blank">📅 22:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139498">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVKVa2lqljFySZ07QKhSkb5vozYe5EvMaFN2ruMLiOP0LM3zkzST8gwss7W6GuE-tWLwgyxyB4cfi9fqjpOodK0icOzfXiyN6sD8bh26DXCosBRG2O52pLAfYZ4zkMZC1J5c14mr_3z9AJb03XlFXqEdIwNOa6ssz4PSViaT9RZjUMtXPI3nNTVU3ERafzKvtZmE9pgl4CFComQyYaGX6eWNR0UfSaW9-elTWciPz3De6n6SD83IcUWqba219XYNIsBzRb-ytFdCBetPfad_o2xZsPGKwLJdGCPLKqfmF3OKHC3jIGn2GuE2aAHpjqLTMp1ZY1zmmDb33n9LwoalEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKFq0eHncyTWn_rlfSHLUC53QA2ksv9jxTiHjfBNkoXri5iSZtsyBz1OHvMNciybc6NE1LfAJvHBea-T6IsdEFmEYdrO1podkB4to7xsZJgiArPOP0V0_W5SZeWDEWCM1_ShZhhLqd8o_V8wKILySt8P084YQODBUYuoTkfoVAhCXg6m20IDyPsTMmDZsPEhSXgQrWIjdAwgy2UHUx5vGmQp2lq5SFAEDjNMhSDK4VtrAjfkrrnP1Vz-gruv2MJmEQgzVG9NWVsD6nmOicihx_Xi6PYNrVRQcAmx9_wjsH1pdIXao4WE-vYBvwepSocArwoafPDOZ6YnWFKf_lbeAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn3d6MHHDMzSaMhGBlitOL7fAbg9V1slz_rthCUB8w9watKu4mODO7PmmufPck37pFtrOqqANkkgq_6DrykJ5UzwPaZ7Cruw2S7JRG-1CFbRUKmylLRYTJlkZNUoBn0PUFtmYfJKpzXvVbTsSqC9fIdjb6sHQusl6d0pbCEMyZP2sEJ_Wr8nYt_btiBl4w3-2YZfNFzGb1et-jED1vNTVzVE_LFwKfs9gZ7mp1Nbv5dYzkX_xf58OZRW-z4RDZwuYIi0GrWVLi3Cob9mBirSotPB8Tsi7JajR6LiXy3lHtUgQ98J77GKMeMwg4xGUIW8d70B6caIZtsHsyRg3VQupw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139494" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139493">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwWlzrb7ss3SFFQeEy9AIHYYgw2GpMdBLphFhYyXK5TbuK3L23rzHXLZx5rUJhMcu0cUL7Bx6RJiYKzi_A5SOcjgDD3wkh7BC_HUL6AmxkUkPzs08kDbgrtyJwvLYDRtvZAEmqN9AoVq8xaU0vRkqROC31P17ri01oAA1L-9udmM7YpiP_rwBbXT8vcIAlUpGWlIIBAa0TtSydcP-BUQMynnEIolPw1HLv37STypCkfGrPEHA2HNYMXB-jdoE_Ayp3Yhbt7mQydARtKcx94YLmCHoQ2JvqoVg8S2Gyy5zwkkIVxpb1HF05Dj5pZvaR6u97BZ9lMXbIJ58irNWvgKlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حضور ابوالفضل جلالی در بازی امروز
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139493" target="_blank">📅 19:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139492">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ova-AuFNdswJEqPnchtvJDJITyTVag4LK5wrQxmspPS3nmaJ2prU4a7couMgj1rqu5ZbVeNatZdueeZYaucjyxnUW0Dn300DCnJmU0CPMr5MxTzc_3yL0bg7bIpBIPeKy1J5GdC_-hH90Ok_Zpagqv-1ONIQb1q4d3Flvc5ViexuNRjKGF36q6yaRXVXeDhZU1HCRJ1RtI89bYOAsgkDqRpnUWpOOv68DRZ52tmjokfOyKvBFNHceKTRiyQcIGiuBgkClheCS6UAt_Bhwq8y8Jr7bVIDgRs7IOq5cWisg6i-x9bEt96mbd91I3TuzZwNA0ny6xJarIuQvd47Mhkozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
محمدمهدی محبی زننده ۲۰۰ مین گل تاریخ دربی بود
👌
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139492" target="_blank">📅 19:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139491">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">#بماند_به_یادگار
🔗
💯
تا روزی که اردوبادی و اینانلو داخل هئیت مدیره هستن این تیم رنگ آرامش نخواهد دید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139491" target="_blank">📅 19:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139490">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi48FSng5cYVaPYgDZJOlUgO4_SUlQQoPb7JOZmn9zBIv9h2mP9oPSMM20Cmu-AJF1RRarfb4A8yRN89kSiXWuEKKVLHFiWrolbX_kjGK-3uP6Q5sQoNE5btlzTewAFgSrUqTapdRp060u8Ck_CNJV-LwufWdEmnAZSxkvXfAwmNOjGEcI-b7Wz78dFQjqDx_BL2eU4RrR9CTxipt0tnciV-d03fajCgkRrU97AwBquPN9YXpnxU5zwPEatmpv06z8nWJ1VlB3bUnWGCyZBWifVOoMjpJ9eiGtecAzBErV6DWlCSjMc1TIWP4CHhNwsdyD4sFzNRJZlPtqffCxmhHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
پرسپولیس امروز در دیداری تدارکاتی به مصاف مس رفسنجان رفت و با تک گل پوریا لطیفی‌فر به پیروزی رسید.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139490" target="_blank">📅 19:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139489">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFdXWKyQReKu1ZrTIDFN2CS9WpooMTQGhrvCoPoj8PcOGrwEXFWNUN5CoClouxcyMFuKxy1Sav8EhLko0-3ThXkH9f5ZolJlH3ol_a14kU5e3sv8VheCNio3iun3wEvb-um7blrmNz3rMJLFBlHQUqZp_xRmCJyc5sKmCJZfGWJL-PGa0yMWRlyj-n7TMWMDwZI2qgGYHhYWxXmCK2Zx_nW5ldj3qou4B5GQy56kNhZGWp2HgHFD6VAIowUVC6ejxdHPVHl7kz8EHa2nisdqZqzMJdh6VTbJYSb8qCxHlzy-h-TP2_gzaN1V0n_DacxoRpgh9XcPXyMpLITq_4gYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
محمد عمری از فصل قبل تا الان توی ۱۷ تا بازی برای پرسپولیس فقط ۲ تا گل زده!
⬅
⬅
با اینکه آمار همه‌چیز نیست و کارایی بازیکن روی بازیِ تیم هم مهمه، اما هوادارها اصلاً ازش راضی نیستن و انتظارات رو برآورده نکرده. امیدوارم بازی دیشب براش درس عبرت شده باشه، تصمیم‌های درست‌تری بگیره و بیشتر به درد تیم بخوره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139489" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139488">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139488" target="_blank">📅 18:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139487">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYGxqegOqkmAQFWBgoBuUI0QE4ZR0T4ojBXg-g9vLQnEgKCjR_IwOgTY51OkXaM1JNJ_EUvws9ecOv2FwKF1v8hd-SouzGtFxGHEmqHSeqVE9FyRHhuySPwYAsAhzPBUlT9Y9xl9Zncn6ysngw5xIvjC3rGv68sh04StMKPDDsIfWg7UCBV82UL8ez_8BKYbf9SY8rjXwClPZ5U-SALUtxX3lorFp-eHH6YYEaQEhTaSAZuQKyoX9RgDhFm-eeSRLf-lS9AM-_ceMShjOa9mZ93Ci1H-YlKZ3lHZrNqswYGy8YJtw66vnzo8zaO0nH3Iz5t7-5qsp0KKHzClUfYHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139487" target="_blank">📅 17:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139486">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
دانیال گرا مدافع مجارستانی تیم پرسپولیس برای هفته پنجم از لیست بازی خط خورد تا یک سهمیه خارجی سرخپوشان برای فصل آینده به خطر بیوفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139486" target="_blank">📅 16:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139485">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
خبرگزاری مهر:
🔴
پرسپولیس پیشاپیش شکایت خودشو برای حضور یاسر آسانی تو دربی آماده کرده. پرسپولیس اعتقاد داره کمیته انضباطی و سازمان لیگ صلاحیت لازم رو برای پرونده درباره یاسر آسانی رو ندارن و استعلام فیفا باید منتشر بشه
🔴
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139485" target="_blank">📅 16:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139484">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139484" target="_blank">📅 15:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139483">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=alPrZg5s5BLD5_ytG92aapRccdp4g6908IYkuYJaf-CH_mJuU00wsxFAAP5GZJ93tODWAE53rHkqT_Ftm3BG114boGMxBTP5wzx-bLZZSMLhF4FzbNqdkYAe1JiP6IaNSLp7jCKtV4ne393OyiQDGXYjjD_hdAhX4dtnrjxRkwj4Xqrzz2u65WvgsoDN0aV8P8ecfPOITgG3Ntjq9dZqR7CdZhRYXwGnse52FSYYE5X2XYH6kg1rWqZffb-dnYCXt78t33JYcAplPbr_zE8PUyrBT_u66mShzCoNzNRMhihyamNOV5x-u-ByYWLVqTgtuwueRHU77rWX9VabDtHjQW8phxSydgj28SBM05Lny6Lurpw_mOuTnmciXQTNa9zoVYgsTjWzgz8hGu52UdujSZkOJHG4hWDVaLQTTwSlg1v4_9TPaTX3sVvqgfOC5is51P1hJv7_0DxPZDprTlJmQQb68nZSwCQF_BYtaNR9rX3MLIVIIb38eYeubBvY2i7TpF7GFeQzNjvQpKQUePemswqLDFrjO7JjK4YFeRqK5CVr0Fdz-oTgyv660AaCQE38FpdM4fDpJM6Hm2ShMUmantrOp14H1L0HvchfmcWpN2LTHeyqOb5XLxS2L2OczEfoxi6Y56Cy9Y7asbHWNn-ECRyxB_kTZF9lTeqXAe-n4Gc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=alPrZg5s5BLD5_ytG92aapRccdp4g6908IYkuYJaf-CH_mJuU00wsxFAAP5GZJ93tODWAE53rHkqT_Ftm3BG114boGMxBTP5wzx-bLZZSMLhF4FzbNqdkYAe1JiP6IaNSLp7jCKtV4ne393OyiQDGXYjjD_hdAhX4dtnrjxRkwj4Xqrzz2u65WvgsoDN0aV8P8ecfPOITgG3Ntjq9dZqR7CdZhRYXwGnse52FSYYE5X2XYH6kg1rWqZffb-dnYCXt78t33JYcAplPbr_zE8PUyrBT_u66mShzCoNzNRMhihyamNOV5x-u-ByYWLVqTgtuwueRHU77rWX9VabDtHjQW8phxSydgj28SBM05Lny6Lurpw_mOuTnmciXQTNa9zoVYgsTjWzgz8hGu52UdujSZkOJHG4hWDVaLQTTwSlg1v4_9TPaTX3sVvqgfOC5is51P1hJv7_0DxPZDprTlJmQQb68nZSwCQF_BYtaNR9rX3MLIVIIb38eYeubBvY2i7TpF7GFeQzNjvQpKQUePemswqLDFrjO7JjK4YFeRqK5CVr0Fdz-oTgyv660AaCQE38FpdM4fDpJM6Hm2ShMUmantrOp14H1L0HvchfmcWpN2LTHeyqOb5XLxS2L2OczEfoxi6Y56Cy9Y7asbHWNn-ECRyxB_kTZF9lTeqXAe-n4Gc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139483" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139482">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139481" target="_blank">📅 13:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139480">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139480" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139479">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139479" target="_blank">📅 13:37 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
