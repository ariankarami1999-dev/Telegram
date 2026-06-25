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
<img src="https://cdn4.telesco.pe/file/JV41u49pICKvxhtDZUmkLpYUSvjOzg2peqlHugpy8sLZ7cnVeQil0gqkQ8gaD0G3KFCDAzTqiaCoPDQD5cxfUBXEuODQHdq0BI7Zq2vMWw5LfXu10RRY2jg0ChA4jnFPgjtbFxfYb6m1rIjovPlgvipke9PWJPyQ7tWHVkaOgPUW9BNsmoMLDuVEkcxdP5nFhNgN_KEUfIV43tWA05hHob9TdvXzxCFXYbneMgHlWm06pAkKqdfFda_CagrRRMqVKYT-ik0uA2fKUoRGt8GLRnNQ10CLkWOWJ9aQ0iPJFEb4t9O0xFVC9WNkQzTHO5NwtUs6E6q96VISXCRTYF4NxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 19:28:13</div>
<hr>

<div class="tg-post" id="msg-130204">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vx13orMq7PUNxp55ARuTGST77bEnNc_iSgYIztUUSAFKmVDJiJdkjoaaMO42YUI8HbKBal67lwnnYX62SRYON89Jq469jUvL0IZ3LFZWB0of_nL2XdtV18S6davwTSPrv_RD5CHbtXyt3d89Tkf-jo2SN9fKJsF6G84Lyi7euhvsdVnJETjS-V4NoUvc1eSau91uJjLKL2RtaiCHb6Ai1tkMbQTa7sBK27PiGFrAcyBiDAnKOmvyVu5qX1J0iRk09ToawbOl7QBmnf7oUiTTDqNBJMVeKODNRROEbS511DktXQW6x4WaZqQLN_VrTEplc-wnyguUY_YtcURwEuhPlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، یک شاخص مهم در صنعت هواپیمایی آمریکا پس از شش سال، سرانجام از زیان‌های دوران همه‌گیری کرونا عبور کرده است.
🔴
پیشرفت در مسیر توافق میان ایران و آمریکا باعث کاهش قیمت نفت شده و فشار هزینه‌های سوخت بر سودآوری شرکت‌های هواپیمایی را کاهش داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/130204" target="_blank">📅 19:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130203">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed090dd487.mp4?token=CmFNhjtnF6f590aWmGuBwIAsngN09H-nfqqn5Z3mxT5MsJXdOMIdZ1b6X8IXv_ehjVE93ZygiYxWI8tkeg1ewElM3xH4EZ_FP9MW7T0HnfePo-L5GSsaHcsUel76aWAgyTheJm7XQ-KONW0grn3yIYbK3296-BZVKhzHczwwFtsDIKP0SPJp9AD_i2z-XGHJLKLGKhPHLXoWuKnRzCKkFyHbqtiD2bf4LQQtjrtsratcd66LgO-0p71MLbziH5FFU1uBxUNC0Nog7IMVYgvcP1-0OV9fR0EtAc1aoEQ1pYxreeA0CDo07XSqjbYrmXisMdxKDApMJOyskDfh71rigzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed090dd487.mp4?token=CmFNhjtnF6f590aWmGuBwIAsngN09H-nfqqn5Z3mxT5MsJXdOMIdZ1b6X8IXv_ehjVE93ZygiYxWI8tkeg1ewElM3xH4EZ_FP9MW7T0HnfePo-L5GSsaHcsUel76aWAgyTheJm7XQ-KONW0grn3yIYbK3296-BZVKhzHczwwFtsDIKP0SPJp9AD_i2z-XGHJLKLGKhPHLXoWuKnRzCKkFyHbqtiD2bf4LQQtjrtsratcd66LgO-0p71MLbziH5FFU1uBxUNC0Nog7IMVYgvcP1-0OV9fR0EtAc1aoEQ1pYxreeA0CDo07XSqjbYrmXisMdxKDApMJOyskDfh71rigzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تعزیه عجیب در فلاح تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/130203" target="_blank">📅 19:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130202">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: ارتش تا زمانی که لازم باشد، در «مناطق امنیتی» در لبنان، سوریه و غزه باقی خواهد ماند.
🔴
ما علی‌رغم فشارها برای خروج از «منطقه‌ی امنیتی» در لبنان، مخالف عقب‌نشینی هستیم؛ عقب‌نشینی نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/130202" target="_blank">📅 19:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130201">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
مرکز عملیات دریایی بریتانیا (UKMTO): مرکز عملیات دریایی بریتانیا گزارش یک حادثه را در فاصله ۷/۵ مایل دریایی جنوب‌شرقی دهیث، عمان دریافت کرده است.
🔴
یک کشتی باری در سمت راست خود توسط یک پرتابه‌ی ناشناس مورد اصابت قرار گرفته که به پل فرماندهی خسارت وارد کرده است. ناخدا گزارش داده است که تلفات جانی و اثرات زیست‌محیطی نداشته است.
🔴
مقامات در حال بررسی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/130201" target="_blank">📅 19:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130200">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAE5KyZL0QdrA6XMpd8fE3kBTeMJuRtrTKyZK9fIhRaqCRURZmC6BI2z7aWLqcC7Bddg7frTjhIg7y3JwPs2NEn06ltYG1d-gUsP3ltw5iYk_x7Z4kWQT76fLyPPP7w7ti0urctXN1sk1sHDAutOgm2YFWJyTB3Rs-0rZiXxwqol_06dSwY1dWraprGGw3xzNVIBgtYtrJVTcR6SMjRlNBpyWgj7USBOaqWxLzb3v1Rl8HTbooRKgeh71y5SZBGo80RXEYFUk3L5VekCkIg6m6NEo9TxChda9pDMVegDlmw_h552iEKIbhyfTsxQFoODg34WiLjAJdmW04Wjz7OL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط ۵ درصدی بیت‌کوین در ۳۰ دقیقه؛ پایین‌ترین سطح در ۲۱ ماه اخیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/130200" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130199">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ارتش اسرائیل: اگر به دلیل عملیات ما در لبنان مورد حمله ایران قرار بگیریم، با تمام قوا به آن حمله خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/130199" target="_blank">📅 18:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130198">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: ایران روزانه تا ۲ میلیون بشکه نفت صادر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/130198" target="_blank">📅 18:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130197">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مقام آمریکایی در گفتگو با نیویورک پست: وجوه منجمد هرگز تحت تفاهم‌نامه حمایت شده توسط ترامپ به ایران نخواهد رسید. در عوض، پرداخت‌ها مستقیماً به فروشندگان تأیید شده‌ای که کالاهای بشر دوستانه تأمین می‌کنند، ارسال خواهد شد و نه به خود حکومت ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/130197" target="_blank">📅 18:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130196">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری / تلگراف: فیفا درخواست جمهوری اسلامی و مصر برای ممنوعیت پرچم‌های رنگین‌کمان در بازی دو تیم را رد کرد
🔴
طبق اعلام فیفا، هواداران می‌توانند با پرچم‌های رنگین‌کمان وارد ورزشگاه بشوند؛ این مسابقه هم‌زمان با جشن Pride در سیاتل برگزار می‌‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/130196" target="_blank">📅 18:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130195">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل:  ما از کمربند امنیتی در لبنان عقب‌نشینی نخواهیم کرد، حتی اگر ترامپ یا هر مقام آمریکایی دیگری از ما چنین بخواهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/130195" target="_blank">📅 18:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130194">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
لحظه فرو ریختن ساختمانی در ونزوئلا در جریان زمین‌لرزه‌ای که این کشور را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130194" target="_blank">📅 18:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130193">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
جی‌دی ونس: یکی از بزرگ‌ترین پیشرفت‌ها در مذاکرات سوئیس، توافق اصولی برای ایجاد یک کانال ارتباطی نظامی مستقیم بین آمریکا و ایران بود تا به جلوگیری از تشدیدهای آینده کمک کند.
🔴
ادعای ونس، آن‌ها گفتند: «باشه، خوب، ما کسی از سپاه پاسداران می‌فرستیم که در دوحه با کسی از سنتکام ملاقات کند، و این‌گونه بسیاری از این اختلافات را حل خواهیم کرد.»»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/130193" target="_blank">📅 18:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130192">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر خارجه آمریکا روبیو می‌گوید «خیلی نزدیک» هستیم به «بیانیه اعلام نیت» برای خروج برخی نیروهای اسرائیلی از جنوب لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/130192" target="_blank">📅 17:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130191">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
رویترز به نقل از مقام ارشد وزارت نفت عراق: به دلیل کاهش شدید صادرات نفت در پی جنگ علیه ایران، با بحران مالی حیاتی دست و پنجه نرم می‌کنیم
🔴
در صورتی که سهمیه ما در اوپک به طور قابل توجهی افزایش نیابد، مجبور می‌شویم که تمام گزینه‌های موجود را بررسی کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130191" target="_blank">📅 17:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130190">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed03997a75.mp4?token=uXxjt_LH0a03yejzVHC67lTz4E6p3s7RXKAa-gKDY1jmF5WMR4S5j9BTXZSD5spkXF9qHjKDUqRqriH3TeiwhB5NUquLQQjNxVXZXYQVmJPJwPijtpqZr9MpXIbMLK8C_ZWwgHTbvD_D0K9G5h7y3hWBBE194ihLYqtqom9BfeFjODD2UCeHlVqV63s1sFH9U9xTfVFDX1-8lSa4gCUM1s32wPVfN1OY4dykLkGo5oFZ28dF7mJsWxro0xqLGx9O7x7sREQqJPkzuiD8S5x3_mapXL5r3Qu6iXKFTM4L_sp3MYIBSMvklv7ISaFS2tLx1oFzvJ8fZG9EbCakoqyLgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed03997a75.mp4?token=uXxjt_LH0a03yejzVHC67lTz4E6p3s7RXKAa-gKDY1jmF5WMR4S5j9BTXZSD5spkXF9qHjKDUqRqriH3TeiwhB5NUquLQQjNxVXZXYQVmJPJwPijtpqZr9MpXIbMLK8C_ZWwgHTbvD_D0K9G5h7y3hWBBE194ihLYqtqom9BfeFjODD2UCeHlVqV63s1sFH9U9xTfVFDX1-8lSa4gCUM1s32wPVfN1OY4dykLkGo5oFZ28dF7mJsWxro0xqLGx9O7x7sREQqJPkzuiD8S5x3_mapXL5r3Qu6iXKFTM4L_sp3MYIBSMvklv7ISaFS2tLx1oFzvJ8fZG9EbCakoqyLgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیش از ۲۱٬۰۰۰ نفر پس از زمین‌لرزه‌های ویرانگر که ونزوئلا را لرزاند، مفقود شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130190" target="_blank">📅 17:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130189">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رهبر انصارالله یمن: پیروزی ایران در برابر دشمنان، پیروزی کل محور مقاومت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/130189" target="_blank">📅 17:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130188">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
جی دی ونس: اماراتی‌ها - که تا حد زیادی جنگ‌ طلب‌ ترین و تا حد زیادی طرفدارترین کشور در شورای همکاری خلیج فارس هستند - در حال گفتگوهایی با ایرانی‌ها هستند که قبلاً هرگز اتفاق نیفتاده است، از جمله با سپاه پاسداران، در مورد انواع مختلف مشوق‌های اقتصادی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130188" target="_blank">📅 17:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130187">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
جی دی ونس معاون ترامپ: دستاوردهای مذاکرات سوئیس، توافق در اصل برای ایجاد یک کانال ارتباطی نظامی مستقیم بین ایالات متحده و ایران برای کمک به جلوگیری از تشدید آینده بود.
🔴
«یکی از چیزهایی که می‌خواستیم به دست آوریم، یک کانال در سمت ایران برای کاهش درگیری بود.»
🔴
«آن‌ها گفتند: "باشه، ما کسی از سپاه پاسداران را می‌فرستیم تا در دوحه با کسی از فرماندهی مرکزی (سنتکام) باشد و این همان راهی است که بسیاری از این اختلافات را حل می‌کنیم."»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/130187" target="_blank">📅 17:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130186">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کانال عبری: آمریکا ۲۸ هواپیمای سوخت‌رسان خود را از فرودگاه بن‌گوریون به درخواست اسرائیل خارج می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130186" target="_blank">📅 17:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130185">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
عراقچی: دولت ایتالیا باید به‌طور رسمی استفاده از خاکش علیه ایران را تکذیب کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130185" target="_blank">📅 16:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130184">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f844f77e67.mp4?token=uvDUgdovuAI6w1iYyvvg8CNa9tGRlPc9Ow_i-5Gr1oCShtgWYfDbWZV5-mup3Dp2S1bhdPXFi3uJwKZOfAfJ94-PeidU7PXj-RXIFPCoBTWX-TVOwQSjSMsbc12fh8Ktch_LDLcQ-kUfIyprmN6XSN92uFyWE02OiQvfJXPAVcA_wRvXpZYnYvkOl0EpJFlduZLOjxSgRsz656y3sCuclkeevZV5n_FP_Fl6Q_3asaTwbO-y4P9QanALmN8lY_eTIg9Ctd8NAnhViCktuLjWM1K697TKNKR8ev2Nc9pzqYtSADdpGacmJaKQi6Ri7fKaUvOnc3-wDZLOTo3t-kQgvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f844f77e67.mp4?token=uvDUgdovuAI6w1iYyvvg8CNa9tGRlPc9Ow_i-5Gr1oCShtgWYfDbWZV5-mup3Dp2S1bhdPXFi3uJwKZOfAfJ94-PeidU7PXj-RXIFPCoBTWX-TVOwQSjSMsbc12fh8Ktch_LDLcQ-kUfIyprmN6XSN92uFyWE02OiQvfJXPAVcA_wRvXpZYnYvkOl0EpJFlduZLOjxSgRsz656y3sCuclkeevZV5n_FP_Fl6Q_3asaTwbO-y4P9QanALmN8lY_eTIg9Ctd8NAnhViCktuLjWM1K697TKNKR8ev2Nc9pzqYtSADdpGacmJaKQi6Ri7fKaUvOnc3-wDZLOTo3t-kQgvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
افزایش چشمگیر تردد در تنگه هرمز
🔴
بخش عمده این فعالیت‌ها شامل ۵۳ مورد ترافیک تجاری است و شناورهای کم‌ریسک بیشترین سهم تردد در این روز را به خود اختصاص داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130184" target="_blank">📅 16:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130183">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdW8XPJKuELKEsqDiToS7ODZC_o-O13Ggi0m0y2ALY9ZjO21OrRknhDFxO1BCdSHk77YfmOHHG0_OV35ajXenlWqfgtszvqXysiLNH1hy1T98MkPwg54fvVZ7p88_9i2eZ2jDuBPkZkEntKtHGMPqKwyb2jkeYDUi00L0I8tLROIBS00efljB2c_O-4K_G3jUiZCefDmOXhkrKdILwpsvrEwOxxmH9NJty56jkswN1HEV3gbW5IVFO8EPymtOLRmNqUwis4tNM0NGfd5NPdAaFz8GebLdViQK0NVqUQAFJLT4h01J2XX0NQAWMSh2DxnFrjcr4WrB_Wk1-lX5ItrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موسسه کپلر: تعداد عبور و مرور از تنگه هرمز در تاریخ ۲۴ ژوئن یعنی روز گذشته به ۷۰ مورد رسید که نسبت به روز قبل ۱۰۵ درصد افزایش داشته است
🔴
این افزایش به دلیل پیشرفت تلاش‌های مین‌روبی و استفاده بیشتر اپراتورها از مسیر عمانی رخ داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130183" target="_blank">📅 16:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130182">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCk1tl0Njsx79B1U4iEirCnDoohy6vl6X7eFiXg49JQh3PWQMgAW_720NhA3XfPfwaFuoB5yjdMs924FnmHDBnu-0SGKjSVH-jrACRmXeyGpGXmbhiuu-LK_9zJvn0ltyC0nzTWyT-Y48E8zlC9msTrG-lsHrY_b5e6lAvO7uU4mfl1iGoZWbkg0KJW6LLYO2fDJXAMzp8-V5P2M35RnEwh0cybpmVZR4i2TWpLei_qm-yh1Iv2StwfiJUD4PnBqhqlim8w1Y6cu0AtBIyZGn_67KWMC6MJJMIB3-2wggk9gSvRCiMZOyaAzLwRd2oQI4O_J6AYLn08Kl-F9p8e9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کتلین تایسون، بانکدار و تحلیلگر نظام پولی بین‌الملل بریتانیایی: هیچ بانکی برای ایران، صرفاً به‌خاطر مجوز ۶۰ روزه تجارت نفت، حساب دلاری باز نخواهد کرد تسویه‌حساب محموله‌های نفتی همچنان با ارزهای جایگزین انجام خواهد شد
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130182" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130181">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وال استریت ژورنال : ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130181" target="_blank">📅 16:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130180">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
گزارش حملات هوایی اسرائیل به مناطق غربی غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130180" target="_blank">📅 16:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130179">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: عمانی‌ها می‌گویند که طرفدار سیستم دریافت عوارض در تنگه هرمز نیستند
🔴
دریافت عوارض عملی نیست
🔴
اینکه ونس مستقیماً در موضوع ایران دخیل است، نشان از اهمیتی است که دولت ما به این مسئله داده
🔴
در جلسه با اعراب، موضوع صندوق بازسازی ایران مورد بحث قرار نگرفت
🔴
توافقی را میخواهیم که امنیت شرکای ما در منطقه خلیج فارس را تضعیف نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130179" target="_blank">📅 16:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130178">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
هلند تیمی به ونزوئلا خواهد فرستاد و حدود ۲ میلیون یورو برای اعزام نیروهای نجات، سگ‌های جستجو و تجهیزات اختصاص خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130178" target="_blank">📅 16:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130177">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k5ZGlKimQUwreejfTfTc6Sy914nYpr3QrQEowvlwBhLiVAPeCARaCOfpjzO7fWy-Cz2trhsgOvmOHMLFt1uaOD8PxyULnhKU4aN0dvnqAaU9yIca7_6Vz6_6rDXT3Kj5ZiUIKlibZ_PMczWt7BFBEBU2sZCSRLYb_Gjj2bwqOPhN4PtFcZ16-x0MTAop1wLa_xW__oCOh31f3RT4BrRqJK6eMxyp1QsEdoUYtsAT_hYwsazS1ApKXOT9eI2DAlbDJJnAhaZQ3MIzC4eXT73-WfwoVlKwJRnm6iAU2GfAuE5zx_WZJ43OIvRijsb6nNfMx-zC_K7ue4MayJLNmbAWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سلطنت عمان بدون مشورت با ایران،  بیانیه‌ای صادر کرد و از ایجاد یک کریدور دریایی موقت در جنوب تنگه هرمز خبر داد(رنگ سبز)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130177" target="_blank">📅 16:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130175">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoSceRNxJS9ZZPZRYzbYQUhNsRTxZgzrVfhe4xt9lO5oZHimmhX4pwjNNV0P8TetfeCDfr9_WQ1fVvD7XTPgqG7otZml_6qoRMqPGMOeaRu_TzVqRNBOhrL07ikiGIFjyXES5QMA-RsleuM4E9Ax75-B_EVjLsKf95JwFuuh39mPSvbSmVaZSOjEBJBomga391dnFbLpA_Ex57Zl0wt6wBnDWWqVSqiCbWMe-Go_6bEFGmTc_yWVbmJDtbo6_KWP89Cz9jOpnzcH8RaOXJDZqaCw-jKRmSkguUslia6RJHN8CKOYF1Ah3leLTQOhIp9j2y7ICXxGRMwh6nh_QB2VTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quXYU2sebykaxjoSUx61n5V9vj7xbpx9c9XxTJ06c9r7JkpC6793g5WfcVfjE2nL7rkU7IpYnaXZaOxQIH-HyK4yWGsYZFKONU3kblNPdYBYBbUgMtT7w_zmVn9aVBhnST6oPZZc-F6plqep5LfRFC5rBQhtYKes4jUZzRD6AWAC2CzC0bYr0XkuTRIn1pqmp5KXI54rV4l7S04G5m30nUgkPC4k49eRwrs4g0dyxr3p_OCuuuA3I06YHc-X7EHSjxJc8TNg0Z2l7gSRy98LnEeKMFP8_V9IUX4bw5hdok-EHbMCBWZzCarka8-9PYtx5o26WfWgly1gtx261YnLPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
قبل و بعد از زلزله‌: لا گوایرا، ونزوئلا.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130175" target="_blank">📅 16:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130174">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7mTNqVTzhX_Qkr9vKE0SqeXQnQZ0LGPjr7VeLQfj6vA_b9HSWA9odLwC1KXMmUhYZFE7lOuoftvF3YKrI5IVwU0o8eAbbfcM0z7mI_ryiAzsLr9rbMi5jZW_Nxobjt1uf37wFmYgnTyTDQ2ktI6mlE2vkf2ZGw6FbveKoef5EMgMDt2vozIr6xVq-0o1HilewnwYpaAEr9UTG-PwcLqxC_6Eid0ODD0PaJ_3X2w4MEsO8oAWQ5ZGuWVsF8ef9u_5ncHK4waVAw4VvgU2r7SzZtcMGMlpJ8d-1RKqCdiTLdpNm9-yVbiZBXFYWsL7yKZg-EMFds99IxZLXAv2_SjLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: «آمریکا به دروغ ادعا می‌کند که دارایی‌های آزادشدهٔ ما برای خرید محصولات کشاورزی آن‌ها صرف خواهد شد. عجب!
🔴
تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!
🔴
این محصول [بی‌اعتمادی] کاملاً ارگانیک، فراوان و بومی است. اما ظاهراً آمریکا فقط سویای تراریخته و وعده‌های عمل‌نشده و حرف‌های بی‌ارزش صادر می‌کند!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130174" target="_blank">📅 16:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130173">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
هشدار یمن به اسرائیل: هرگونه حماقتی با پاسخ سخت روبرو خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130173" target="_blank">📅 15:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130172">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: جنگ اقتصادی علیه ایران یکی از جبهه‌های مهم نبرد برای امنیت اسرائیل است‌‌ و ما نباید به دستاوردهای خود در ایران بسنده کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130172" target="_blank">📅 15:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130171">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c279c049.mp4?token=LwE6B6BTYJ_iMXTq8p093px7XsynkgNp0pYFermjXD77Q9Rebzlxh4eS9dlNSb4UhV7wm4kBBrn2HdF44gBWer0oegARQbuCGe3I4YddW5pHdLo9yxaEXsjf0F2eVmJSLskXYn6-Bqz_chpaHYdfxBnCuNlnr9zjFiB87msKvU8KiAN_AFam-FPwGy6swvAcIxDsZE7MoRK_Nn-ggqV2VwJoMgyDtmB1bfkz_wmQcodZ6PIFjrf9a6FR5r2q99F1mA0ttzTDxxCIwA2MadbvoS2JvZmsWuD_owoli6t2W-T-9lxlR0WXju4E6wc2K4uhb0pxBwvAwPJjOcGJ3MYUWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c279c049.mp4?token=LwE6B6BTYJ_iMXTq8p093px7XsynkgNp0pYFermjXD77Q9Rebzlxh4eS9dlNSb4UhV7wm4kBBrn2HdF44gBWer0oegARQbuCGe3I4YddW5pHdLo9yxaEXsjf0F2eVmJSLskXYn6-Bqz_chpaHYdfxBnCuNlnr9zjFiB87msKvU8KiAN_AFam-FPwGy6swvAcIxDsZE7MoRK_Nn-ggqV2VwJoMgyDtmB1bfkz_wmQcodZ6PIFjrf9a6FR5r2q99F1mA0ttzTDxxCIwA2MadbvoS2JvZmsWuD_owoli6t2W-T-9lxlR0WXju4E6wc2K4uhb0pxBwvAwPJjOcGJ3MYUWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاشورا تسلیت
💔</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130171" target="_blank">📅 15:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130170">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
امروز عاشورا است روزی که حسین شهید شد، حسین اولین شخصی بود که علیه
حکومت مذهبی فاسد و نامشروع
قیام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130170" target="_blank">📅 15:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130169">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d1e505c4.mp4?token=kLMp21DODoW_BqdSSGII5KW8i68wXAPa2AZkC7PAXQ3D1zklD7iC4gU0RzzkiPghj6Zwr2BvjeRvvkfY13s_RhcOgF9gd9nSMUs5Ozt3OmFDcX8u5E2mHCGrctgPMBtmJGn-Y5G3i_tTikLlPYpK4rVMW8PImh3I0qYwNjzu4Bsk1V5OO7okJ8gA97Pva5X48EFq7CDlZlFiNG6tHhAi2GD3kF6Ja66gJUyfi7GO5Q7nlau2mgQyvU8EoFXY6HbgCURU2F9SN8rvuiiQ959ybxiKZJnYq2opJFLf-lqqjn_LPPVca_kC03l4_Sb2wpYrrEMuY2WKPlG42Hj26g4NlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d1e505c4.mp4?token=kLMp21DODoW_BqdSSGII5KW8i68wXAPa2AZkC7PAXQ3D1zklD7iC4gU0RzzkiPghj6Zwr2BvjeRvvkfY13s_RhcOgF9gd9nSMUs5Ozt3OmFDcX8u5E2mHCGrctgPMBtmJGn-Y5G3i_tTikLlPYpK4rVMW8PImh3I0qYwNjzu4Bsk1V5OO7okJ8gA97Pva5X48EFq7CDlZlFiNG6tHhAi2GD3kF6Ja66gJUyfi7GO5Q7nlau2mgQyvU8EoFXY6HbgCURU2F9SN8rvuiiQ959ybxiKZJnYq2opJFLf-lqqjn_LPPVca_kC03l4_Sb2wpYrrEMuY2WKPlG42Hj26g4NlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: اگر کشتی‌ها در حال حرکت باشند، ما به آن واکنش نشان خواهیم داد.
🔴
اگر کشتی‌ها حرکت نکنند، این نقض توافق است و ما با آن مشکل خواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130169" target="_blank">📅 15:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130168">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
روبیو، وزیر امور خارجه درباره عمان:
روابط ما با عمان خوب است.
🔴
آنها می‌گویند که طرفدار سیستم عوارض در هرمز نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130168" target="_blank">📅 15:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130167">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
روبیو: ما مراحل اجرای یادداشت تفاهم با ایران را با کشورهای خلیج فارس به اشتراک خواهیم گذاشت
🔴
به طور خاص، درمورد بند مربوط به پرداخت ۳۰۰ میلیارد دلار حرف خواهیم زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130167" target="_blank">📅 15:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130166">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
تحلیل نیویورک‌تایمز: اهرم تنگه هرمز کم اثر می‌شود؟
🔴
برخی معتقدند که خط لوله‌ها می‌توانند جایگزین کشتیرانی در تنگه شوند، اما بعضی دیگر در مورد این راهکار تردید دارند
🔴
فقط صلح با پیوندهای اقتصادی با ایران است که می‌تواند معضل را حل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130166" target="_blank">📅 15:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130165">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ونس: فروش جنگنده‌های اف-۳۵ به ترکیه در دست بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130165" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130164">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: جنگ اقتصادی علیه ایران یکی از جبهه‌های مهم نبرد برای امنیت اسرائیل است‌‌ و ما نباید به دستاوردهای خود در ایران بسنده کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130164" target="_blank">📅 15:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130163">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15084fec1c.mp4?token=rzxm4hh1LrGti56MWcpz_6dS_UH5eJxCnHk0s4s1o1T43axXrCXZeb5iOxYnMuQ0Bt6ubZQWvPtXf5lEz9LXUWFxnC5FsIrqtuOh4E6PeU1B-B7bEuRLQh9ActSoouirfQfS8e0l6rD2rORaX1X4wduQ2vYFjsw73JD0b59Jq1cQpM6Ss-O2JRrc1Rc68_ISW1N9tEiRIQNRiEggp78ZWpWzdpUXDeHfbg-H3rmBQARS8-jwNC_Wa_YDP8TLO6LgLVXFHyLAa1l1xT6pOR1Xz6myReMlYM01Qg6s0hLhRAAUb4pqTyen5F6tRQv_NjfEXU2i8KfbBFXPta--K1fYoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15084fec1c.mp4?token=rzxm4hh1LrGti56MWcpz_6dS_UH5eJxCnHk0s4s1o1T43axXrCXZeb5iOxYnMuQ0Bt6ubZQWvPtXf5lEz9LXUWFxnC5FsIrqtuOh4E6PeU1B-B7bEuRLQh9ActSoouirfQfS8e0l6rD2rORaX1X4wduQ2vYFjsw73JD0b59Jq1cQpM6Ss-O2JRrc1Rc68_ISW1N9tEiRIQNRiEggp78ZWpWzdpUXDeHfbg-H3rmBQARS8-jwNC_Wa_YDP8TLO6LgLVXFHyLAa1l1xT6pOR1Xz6myReMlYM01Qg6s0hLhRAAUb4pqTyen5F6tRQv_NjfEXU2i8KfbBFXPta--K1fYoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو در مورد ایران: آن‌ها افرادی در شاخه‌های سیاسی دارند که به نظر می‌رسد منعطف‌تر و مایل‌تر به همکاری با ما هستند.
🔴
آن‌هایی که با آن‌ها مذاکره می‌کنیم، همین افراد هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130163" target="_blank">📅 15:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130162">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQILUwj1yQja_eaggQjVQv0unbEQ4kuetMyyJyVD62G2nLaSJ_E7Ho0Otw8rK8SNN5QKuduH5FlZZVKKiz_peoUWt3h8hukAW2kW079KSkUCoJG3R-XxRYEsFNhKh2y4Oi0larfXmjQGycTEUkz0T1nNDWBF2sNy9TZZ1AmmKKhJvpPqTpO1KNMer_eZGU9JUsA_soK13junMwP3pXzCQVZvPzvcV0k_t18OP1oPGZMRcDOr3Mijv4GVttvuXFlm3eNVkqG-a9r7rc49znny_gtZ8z4lFYEWW32V-RX45eMa3XG7DB98se0lFlW9wy_IwFiyPEfvzD1egYBXNUHj8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلیس آمریکا دو نفر را با کیفی پر از موادمخدر که روی آن نوشته شده بود "قطعاً این یه کیف پر از موادمخدر نیست" دستگیر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130162" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130161">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
روبیو: با نیروهای نیابتی ایران صلح و ثباتی در منطقه وجود نخواهد داشت/ ایران با حمایت از حزب‌الله و حوثی‌ها در امور کشورها دخالت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130161" target="_blank">📅 15:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130160">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
روبیو وزیرامور خارجه آمریکا: ما با کشورهای خلیج فارس در مورد موضوع ایجاد صندوق بازسازی برای ایران صحبت نکردیم‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130160" target="_blank">📅 15:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130159">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: جنگ اقتصادی علیه ایران از جبهه‌های مهم نبرد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130159" target="_blank">📅 14:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130158">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای خارجه ایران و سلطنت عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130158" target="_blank">📅 14:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130157">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تاج: برنامه‌های مرتبط با حمایت از همجنس‌گرایان در بازی با مصر لغو شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130157" target="_blank">📅 14:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130156">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزیر نفت: امنیت غرب آسیا و ثبات انرژی جهان تنها با خروج بیگانگان از منطقه تامین می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130156" target="_blank">📅 14:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130155">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر امور خارجه عمان: ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض عبور نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130155" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130154">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رئیس‌جمهور موقت ونزوئلا از افزایش شمار کشته‌های زلزله و سونامی در این کشور به ۱۶۴ نفر خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130154" target="_blank">📅 14:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130153">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59328e354b.mp4?token=J6puga1EeTe-ONIeO0QVOJ4esOegF-GUA0nqpPhdL_f6mIDAlEGYu2gAxf6bMIE4fzSuM7JTIhuemFGDxWV95lQhfs5YPOia00vYme_9kZS1uQIxD2eWqEsUzM0x9nQ1hl3Jsz6G1kNOe_LDM5gq5BBijBCWniAxqEkizoc9WG2fukQMKDQFCR4gwvy3rMJYtecRxdXYxrSaFnKCpnXzV1Pl7WRUeyshF6Li3-MP6t7OKorI3vcYAiOg9G3jGkbIHA48ECk33e88WpuoxAfzjxeKFvGN-TT0Lq_2RkTV4IZ_Gq7drZP-hAcZvVR77c_1XPSrMKP-qwErWi1-rktnXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59328e354b.mp4?token=J6puga1EeTe-ONIeO0QVOJ4esOegF-GUA0nqpPhdL_f6mIDAlEGYu2gAxf6bMIE4fzSuM7JTIhuemFGDxWV95lQhfs5YPOia00vYme_9kZS1uQIxD2eWqEsUzM0x9nQ1hl3Jsz6G1kNOe_LDM5gq5BBijBCWniAxqEkizoc9WG2fukQMKDQFCR4gwvy3rMJYtecRxdXYxrSaFnKCpnXzV1Pl7WRUeyshF6Li3-MP6t7OKorI3vcYAiOg9G3jGkbIHA48ECk33e88WpuoxAfzjxeKFvGN-TT0Lq_2RkTV4IZ_Gq7drZP-hAcZvVR77c_1XPSrMKP-qwErWi1-rktnXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود، من نگذاشتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130153" target="_blank">📅 14:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130152">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
منابع العربیه: توافق اصولی بین لبنان و اسرائیل بر سر «مناطق نمونه»
🔴
انتظار می‌رود امروز پس از دستیابی لبنان و اسرائیل به پیش‌نویس پیشرفته، «اعلام تمایل» صورت گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130152" target="_blank">📅 14:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130151">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سرویس اطلاعات خارجی روسیه اعلام کرد که غرب به اشتباه خویشتن‌داری روسیه را به عنوان ضعف تلقی می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130151" target="_blank">📅 14:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130150">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
حدود ۷۰ کشتی در ۳۶ ساعت گذشته از تنگه هرمز عبور کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130150" target="_blank">📅 13:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130149">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPizxcgItZRYUQ2Zz2CIalyxjgQ87fBc32mDZAvJE7Xff13TcbZATsqWDoXkEi0BemqPCJ0LPsyC3vLY59bKHFnmgnlAKJnj57ocaNcA8AZOcjihWbFerB5Glhom9SZWNsjp5NiRdaMK42TK3C3no4yARm07xeFZLdIeeMoBtObHcHLcqE2fOcTqlu_EjwgHWORkp6ejjA60uP90oAhij_rvhWWz0Q47Dl5iercLvtaTGu4neNlArNwbqozv7eK081oDwEKaHrsYTLY4vkwLELX_W4gZDOVratC8dlS_y-OvPFJC96IW52S5NRduXFS9aEXYR_WnbYDvIqVOfhu8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکارد دیده‌شده در یکی از تجمعات و حمله به مذاکره‌کنندگان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130149" target="_blank">📅 13:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130148">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
تاج: برنامه‌های مرتبط با حمایت از همجنس‌گرایان در بازی با مصر لغو شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130148" target="_blank">📅 13:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130147">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
روبیو: امیدوارم تهران رفاه مردم خود را در اولویت قرار دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130147" target="_blank">📅 13:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130146">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHjq8y6uJBWLnZMQCO1mcMsH53LnKa1j5itDu3dPbzSTB6v0gSrulr36Z_O1C7yxjfYT_gNMbmvLx45_rDy7zhqL-VjxwiG1n2DrG6X7lKfCJ1vThb2pc0VNB4mrmpmqpxlwEczlPkS02gQuNP7BQH-vEYDYX0H9EeUjKRd_1tZ4mEZikd9N7icsnRZ4_Z6_SxXljbZIq7ID6lB53Tum4T1BNrxsqES27R03F4onaol9Gl15eirUjME3Tkau771cRiKvIMqERtnN3ACK1zDNhFHKRnfMKbQHkaCaAXqO__NZU0abf4bWS4FMQMjSzIdsxUX1Fe6uT_YbHtbyJ-G6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پراید صفر ۱.۲ میلیارد تومان!
🔴
پراید با وجود اینکه از خط تولید خارج شد اما همچنان نمونه‌های صفر کیلومتر آن در بازار یافت می‌شود.
🔴
در برخی موارد نمونه‌های صفر این خودرو تا قیمت ۱.۲ میلیارد تومان آگهی شده است.
🔴
اگر یک کارگر با حقوق پایه ۱۶ میلیون تومان بخواهد این خودرو را بخرد باید حدود ۷۵ ماه پس انداز داشته باشد.
🔴
آنطور که به نظر می‌رسد خرید یک خودرو از رده خارج مثل پراید هم برای بسیاری حالا تبدیل به آرزو شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130146" target="_blank">📅 13:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130145">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر اعلام کرد که تیم‌های فنی کار روی جزئیات اجرایی توافق حاصل شده بین ایران و ایالات متحده را آغاز کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130145" target="_blank">📅 13:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130144">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
هلال‌احمر ایران برای امدادرسانی به زلزله‌زدگان ونزوئلا اعلام آمادگی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130144" target="_blank">📅 13:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130143">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
اسرائیل هیوم: به ارتش اسرائیل هیچ دستوری مبنی بر عقب‌نشینی داده نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130143" target="_blank">📅 13:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130142">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
بهنام سعیدی، دبیر کمیسیون امنیت ملی مجلس، با اشاره به موقعیت استراتژیک تنگه هرمز اظهار کرد: وضعیت امنیت در تنگه هرمز به طور کامل تغییر کرده و این آبراه راهبردی هرگز به شرایط قبل بازنخواهد گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130142" target="_blank">📅 13:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130141">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سی‌ان‌ان: متحدان ترامپ در کشورهای حاشیه خلیج فارس بیم دارند که توافق او با ایران سرآغاز تحولی فاجعه‌بار باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130141" target="_blank">📅 12:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130140">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری/ رویترز به نقل از مقام آمریکایی: اسرائیل به نشانه حسن نیت از بخشی از منطقه امنیتی جنوب لبنان عقب‌نشینی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/130140" target="_blank">📅 12:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130139">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سازمان پخش اسرائیل: ایالات متحده به درخواست اسرائیل، ۲۸ هواپیمای سوخت‌رسان خود را از فرودگاه بن گوریون خارج می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/130139" target="_blank">📅 12:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130138">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزیر خارجه بحرین: از تلاش‌هایی که به امضای یادداشت تفاهم میان ایران و آمریکا منجر شد، استقبال می‌کنیم| کشور‌های شورای همکاری خلیج فارس چشم انتظار فصل جدیدی هستند‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130138" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130137">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b25ff2083.mp4?token=rAICbS9boAoEAH_EdOvDCgOfdGtniRmp-fx2Iqd0OJGpVCxGbKPEVnDeGjOMAtYDbDsz3jOVp2rYlHRRNbI1jFGdN3ZXTBLg268wXnR2_UKNemR8-WPqOOuSNWnNI7f4mpznBU8ALkIWKJYq72LlrucIPhCbsBZIDHML1njtdLsBaaY_MB_81oOTQRFCvR3RXTXpM7EitAS0AnrBzi-08B-1b2Wlwn4k6I5Qx1x45LnC0njX-hbq2_LRSOvBVcGegnifYkk2hymvSoMe3L6qWGkqjitdv9tkXNM95j0qhzhwIlOKijLCR7KZbdmLx_MoPCqjzXiKAwOJR3XawgVHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b25ff2083.mp4?token=rAICbS9boAoEAH_EdOvDCgOfdGtniRmp-fx2Iqd0OJGpVCxGbKPEVnDeGjOMAtYDbDsz3jOVp2rYlHRRNbI1jFGdN3ZXTBLg268wXnR2_UKNemR8-WPqOOuSNWnNI7f4mpznBU8ALkIWKJYq72LlrucIPhCbsBZIDHML1njtdLsBaaY_MB_81oOTQRFCvR3RXTXpM7EitAS0AnrBzi-08B-1b2Wlwn4k6I5Qx1x45LnC0njX-hbq2_LRSOvBVcGegnifYkk2hymvSoMe3L6qWGkqjitdv9tkXNM95j0qhzhwIlOKijLCR7KZbdmLx_MoPCqjzXiKAwOJR3XawgVHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو در مورد ایران: می‌توانید آن را عوارض بنامید، می‌توانید آن را هزینه بنامید، هر چه می‌خواهید بنامید - این یک بازی معنایی است.
🔴
واقعیت این است که هیچ کشوری در کره زمین حق ندارد برای استفاده از آبراه‌های بین‌المللی هزینه دریافت کند.
🔴
و این هرگز شرط قابل قبولی برای هیچ توافقی نخواهد بود. رئیس جمهور اساساً در این مورد شفاف بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130137" target="_blank">📅 11:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130136">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8db1e8129e.mp4?token=lwNCPAmjshHpdRXr19NH3ISJH-i51nAi7Ab3Mue5NbHoXfMms9sA-_7D-PySQImjf-tyRswK1uK2oMjoV1SN9ttMWHkHzYpAItx-tte3nnHIp0cJPgvKdv3WL-YRiQUUulh5rEoWV6ZancDEh1tofaGEbrJx4G_IZKC4dCbn2H96_vYM8Zjb83Q--gxhKJa4WLuaylpYr_F6EjcKO7CVeMky-EV_a_AjkXMrW6Cm-HnW-ps4r39TmOwdygpAjom_cMjcRRPe3XA1Pn1fmHgL6si3iwByv_RcSR4XzSiyYoOGU4TGwa80cwkLPFpL4jbiRR2tInyBwtdNkF7yVhBcKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8db1e8129e.mp4?token=lwNCPAmjshHpdRXr19NH3ISJH-i51nAi7Ab3Mue5NbHoXfMms9sA-_7D-PySQImjf-tyRswK1uK2oMjoV1SN9ttMWHkHzYpAItx-tte3nnHIp0cJPgvKdv3WL-YRiQUUulh5rEoWV6ZancDEh1tofaGEbrJx4G_IZKC4dCbn2H96_vYM8Zjb83Q--gxhKJa4WLuaylpYr_F6EjcKO7CVeMky-EV_a_AjkXMrW6Cm-HnW-ps4r39TmOwdygpAjom_cMjcRRPe3XA1Pn1fmHgL6si3iwByv_RcSR4XzSiyYoOGU4TGwa80cwkLPFpL4jbiRR2tInyBwtdNkF7yVhBcKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: تنگه هرمز آب‌های بین‌المللی هستند. آبراه‌های بین‌المللی متعلق به هیچ دولت-ملی نیستند. این یک اصل اساسی در جهان امروز است که بدون آن جهان در هرج و مرج کامل فرو می‌رفت.
🔴
اگر در واقع بپذیریم که می‌توانید برای استفاده از یک آبراه بین‌المللی به دلیل نزدیکی به قلمرو سرزمینی خود، هزینه دریافت کنید، خب، این مانند یک بیماری واگیردار در سراسر جهان پخش می‌شود.
🔴
اگر در واقع، اکنون تنگه‌ای وجود دارد که یک کشور می‌تواند، یا دو کشور می‌توانند، یا هر کشوری که تصمیم بگیرد می‌خواهد برای استفاده از آن هزینه دریافت کند، چه چیزی مانع از آن می‌شود که هر کشور جهان در نزدیکی یک آبراه، هزینه مشابهی را اعمال کند؟
🔴
و سپس ما هرج و مرج خواهیم داشت. بنابراین این غیرقابل قبول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130136" target="_blank">📅 11:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130135">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
فرودگاه امام خمینی: گروه هواپیمایی لوفت‌هانزا تمایل دارد که پرواز‌های خود به ایران را از سر بگیرد، اما هنوز زمان مشخصی برای آن مشخص نشده
🔴
ممکن است که «آسترین ایرلاین» زودتر پرواز‌های خود به کشور ما را شروع کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130135" target="_blank">📅 11:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130134">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzjDEc2cQkmkbv5Agh9rTcDW2g5MeyX2g8AaN7vkGWQU6XnNFnuzI5CsL8L8ETbGg3Mp9e3M0XtG2t8b02Mg-kINCkAFNCDlGdsg33OvBZ-xAdFrlkUVwzvDKv8Nb3HDrOhg2jxv_iZ-OTnWqBbchV-J6mTjFMituzlXupfo1TdrUEFubUN3IGbh6LWq6HilPwSRzEDm43ChKp24Q3_2fqlHG-TtxQ3E4cCWy3wMChh220rCcDKsaTMKjaXQtr4JKrHYIFPVOjLQh5xjZW_3OyQfkyTixgPZ0uSMsmnilWoYLl4Y-cgHC0gNX-ESU-6xqjzF_CEnULA1_E9yAilsug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک در پی سقوط سهام تسلا و اسپیس ایکس در معاملات روز چهارشنبه که ارزش دارایی او را به ۹۷۰.۲ میلیارد دلار کاهش داد، عنوان «تریلیونر» را از دست داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130134" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130133">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
روبیو: ایران در سوئیس تعهدات بسیار صریحی داد و اگر به آنها پایبند نباشد، گزینه‌های دیگری پیش‌روی ماست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130133" target="_blank">📅 11:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130132">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7905e956.mp4?token=XECud9COCWBdvEMRXPDhr1OQwSvFwI91EnZKQyx7dIPDnny27plU9YeUeYrzcOH15-5Q4hOdr3AVM_MN9zzOANP6iM5xSanylNlRH4mnZflNSwWqihuiX0ObfiKYybBv01w_97rS7KmBSqATLD1hfvFaD7GYPlQ7VFIt3XfBMCb4O7ulNAng3ifKTh_Du1K4W2cfMR_qUVxwJII-0d7zDew1uMJG74LFL_HNAlvM9-MSF8bwmq1c0bC4ORMTmCK1YuYpt2CdGSyy7ao1RSaGS9JKtd290P4VFAxpDIGyF9Dk0Qu8BA7dKRA8MUayGoRwSRid0hTVrjFHg7nDXKRqfwHX8GY3uhL-fP8rSV58Ohvu41Iyl7o3shlzLCIO0FyK_a5F4lQ22ZvME59Ng15Ji2z2e3OMTypZu_IebYhHDSLKx8i7t2mcTtwV0jBllNlAGejF63dwVvYVMNA4PhrV1Lum1sZW8pNEhubWHWOwGbTu6CuwZa6OBSIVXuFEWYjg_47HPX_ACIYDb1MoM7dk56bifiFoqlb97bwsHFrEAoxc59I4ZuMprpZi9P0wW8_Knwlajt9Ueu7A4-98I3QK_jygOMr1CG8TDnrg9CRcplReYSX_0761qqT_gUbaDFGLs5TmBV3yWiSUpGBlUWQIqNsbbLp5hsmmx0D2dP75W6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7905e956.mp4?token=XECud9COCWBdvEMRXPDhr1OQwSvFwI91EnZKQyx7dIPDnny27plU9YeUeYrzcOH15-5Q4hOdr3AVM_MN9zzOANP6iM5xSanylNlRH4mnZflNSwWqihuiX0ObfiKYybBv01w_97rS7KmBSqATLD1hfvFaD7GYPlQ7VFIt3XfBMCb4O7ulNAng3ifKTh_Du1K4W2cfMR_qUVxwJII-0d7zDew1uMJG74LFL_HNAlvM9-MSF8bwmq1c0bC4ORMTmCK1YuYpt2CdGSyy7ao1RSaGS9JKtd290P4VFAxpDIGyF9Dk0Qu8BA7dKRA8MUayGoRwSRid0hTVrjFHg7nDXKRqfwHX8GY3uhL-fP8rSV58Ohvu41Iyl7o3shlzLCIO0FyK_a5F4lQ22ZvME59Ng15Ji2z2e3OMTypZu_IebYhHDSLKx8i7t2mcTtwV0jBllNlAGejF63dwVvYVMNA4PhrV1Lum1sZW8pNEhubWHWOwGbTu6CuwZa6OBSIVXuFEWYjg_47HPX_ACIYDb1MoM7dk56bifiFoqlb97bwsHFrEAoxc59I4ZuMprpZi9P0wW8_Knwlajt9Ueu7A4-98I3QK_jygOMr1CG8TDnrg9CRcplReYSX_0761qqT_gUbaDFGLs5TmBV3yWiSUpGBlUWQIqNsbbLp5hsmmx0D2dP75W6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: همه به ما احترام می‌گذارند. دیگر کسی به ما نمی‌خندد. دو سال پیش، آنها می‌خندیدند.
🔴
حالا، ما محترم‌ترین در هر کجا هستیم. به آن فکر کنید. در هر کجای دنیا
🔴
دو سال پیش کجا بودیم؟ ما مورد احترام نبودیم. ما یک شوخی بودیم. ما دیگر یک شوخی نیستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130132" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130130">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdM5c2KtHdqoroYhnL2UhI5UPxHslZnYK4fRBbD1ZXdDO5__kg-AM-m8m4Yl_PAnnO-bQi_kUPP1WrthlJnaho3y6-rGTNdRJ1ftgD_Z5Io9mHH-hQsjTEDC4y3s-cU1aKH7yUIRd_eQDLE-5G2xzs9xYpQal9llcJj0QlueJUmtna2-_akKp-5GrAVPHDAq_kNhazUL7yMMdAvGS4Y0RHxQOriWwSxi4Gidby2tFLocN5aNnJo8TNGDGuE6qhpquzVfBk6d-p6aOesrbMunL-LMiVLOD2dxQlBy9WSJpFeZeKWiTYY5pp8Bg4ddNl2U8L7rpEGLGH3tkj3nNVenTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_-YOVVrO1-knP02hsAOVgpnFJyHR08Hs8F1IRCrVtbQVqjEwaHBr9pkKLPkPooXVps1r1vLHew37pqInn3toGvfclJoatonfxrljf7F80ZVaaw5ot52JxMkkslNXU2MevDtKb0R4qXrQWwW9yyzF7uRjRIZmTypxk4mAnvZV71VUIOYMoTMnc_BdQrPZKgGaTKLwbvqJ88XYvKLIzOLTQ2yNP5NEf1J8U33ZyCZRgsqbQ3ihFDtnnJYgPyTkELNEnOXJWHglGhSPjLr4y6HSnyPzivFM85KQsgl9trVEbTrJJF7G7F3Ajf9ST8H0KI3H8GKRndS4-iZ0-OAz7SG_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ایران از عمان به دلیل صدور مسیرهای کشتیرانی برای تنگه هرمز بدون دخالت تهران انتقاد کرده است.
🔴
نیروی دریایی سپاه پاسداران انقلاب اسلامی در بیانیه‌ای اعلام کرد که «برخی مقامات» - بدون نام بردن مستقیم از عمان - بدون هماهنگی با ایران «مسیر جدیدی برای تردد کشتی‌ها» از طریق این تنگه اعلام کرده‌اند. این بیانیه افزود که «تنها مسیرهای مجاز تردد» مسیرهایی هستند که توسط تهران تعیین شده‌اند و هشدار داد که هرگونه مسیر دیگری «بسیار خطرناک» است.
🔴
این اظهارات پس از آن مطرح می‌شود که عمان با هماهنگی سازمان بین‌المللی دریانوردی، «کریدور دریایی موقت» در تنگه هرمز را اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130130" target="_blank">📅 11:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130129">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldKIeNRxDD9ZD1lt7AbWysdVIOv4ylOueJ9x_LECJM2Kkx-_kQ12X1WPXUaeCoXTQ71MSrATK9yH0rsakaooYV3KHHR5KpMlvl2_sHgyoDrhVhsBT7C8yf5jG96Q21LupsJBSAXpd-iynVHAQ8UPv1imDcyRlbx_UQOpNiQsJ39XBEJmFWOSOCFJ1Lh18p76pvEEOZdpIKma2Q4L5l3zprRE-lDR0RWVxRnIqqnKDn2fXOZUMmMX7HBbcc7wKfpMx55I-cdZ5zX0uLzFtnQwiRmEQbo53aSa5Uxxrs06b0eJQpCw6VjBMoAb3T7yYTsug5_fDzgiws7z-mdT0Tr_SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
🔴
این رأی، ایران را در معرض توجه قرار می‌دهد! رئیس جمهور دونالد جی ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130129" target="_blank">📅 10:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130128">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ارتش اسرائیل از کشته شدن یک سرباز و زخمی شدن سرباز دیگر در لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130128" target="_blank">📅 10:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130127">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fcd190313.mp4?token=F5T66A9MaL8uKLDQ4CZKClhoQdCfg9LCv_brexGZdFmt-_y1-bqUG8PU4qCsgu35bY3L0a-p8WmlLgVWupCLRCwzAnMN-VOgcApsYheED0-vteYpzxLq0BzO9vMObNAa7U11C7ZiKtjj-TW_TwicSd1t_O42D-gTClxgQJ64CyqfOcKmQ3Y0F8xOzEMs39C2qT7eIBKT67xihq8soZLoh6xj81qG8zzsH7DqBX8xf3S0f4jgmKpIcAI99PiupEaj-1iLSXEIUdLdtdT496c3ldg1CbpPAhXgTQAp94-Yy17Ww7TaufiuNyTAadVlb53g3p_kuEpgXJamB6jIhnleNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fcd190313.mp4?token=F5T66A9MaL8uKLDQ4CZKClhoQdCfg9LCv_brexGZdFmt-_y1-bqUG8PU4qCsgu35bY3L0a-p8WmlLgVWupCLRCwzAnMN-VOgcApsYheED0-vteYpzxLq0BzO9vMObNAa7U11C7ZiKtjj-TW_TwicSd1t_O42D-gTClxgQJ64CyqfOcKmQ3Y0F8xOzEMs39C2qT7eIBKT67xihq8soZLoh6xj81qG8zzsH7DqBX8xf3S0f4jgmKpIcAI99PiupEaj-1iLSXEIUdLdtdT496c3ldg1CbpPAhXgTQAp94-Yy17Ww7TaufiuNyTAadVlb53g3p_kuEpgXJamB6jIhnleNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در دو جنگ جهانی پیروز شدیم، فاشیسم و ​​کمونیسم را شکست دادیم.
🔴
ما باید دوباره این کار را انجام دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130127" target="_blank">📅 10:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130126">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd225af94c.mp4?token=UNmYpxeE1d-Ov6NrGylmc4wTuKj3awSyw2tycW9coTb5oK8WxBfZyPd_m7ZeoHOjd71aimMUt7R0vCnmv6-TjCeqLh29BTjMs7fv-s6xs3fgKcX1Lu5kfQS7_VmLogQ95l21A5afkCjz01Kl5Mmli6S6D1F9VeIWfJ7bGK2kI_5WDHAkMM2nQWhOGrJxpqB0PMuaXegBcD_nE5SGFBGODV8EDIdwvqCeimgu9lLnOWewt7vIJumwILlpyky1dr7FweQstND4U_8iU6t5sgyp80BhtsHvZnBOvjaN3cMkc-KPmqW74K49xMutJv_vMY3Ag6XTrdvkbduZ045CpD7LeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd225af94c.mp4?token=UNmYpxeE1d-Ov6NrGylmc4wTuKj3awSyw2tycW9coTb5oK8WxBfZyPd_m7ZeoHOjd71aimMUt7R0vCnmv6-TjCeqLh29BTjMs7fv-s6xs3fgKcX1Lu5kfQS7_VmLogQ95l21A5afkCjz01Kl5Mmli6S6D1F9VeIWfJ7bGK2kI_5WDHAkMM2nQWhOGrJxpqB0PMuaXegBcD_nE5SGFBGODV8EDIdwvqCeimgu9lLnOWewt7vIJumwILlpyky1dr7FweQstND4U_8iU6t5sgyp80BhtsHvZnBOvjaN3cMkc-KPmqW74K49xMutJv_vMY3Ag6XTrdvkbduZ045CpD7LeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در حال ارائه بزرگترین کاهش قیمت دارو در تاریخ با اختلاف قیمت ۴۰۰، ۵۰۰ و حتی ۶۰۰ درصدی هستیم
🔴
اگر نیم درصد کاهش قیمت را انجام می‌دادید، کسی می‌گفت شما نابغه هستید - ۴۰۰، ۵۰۰، ۶۰۰، ۷۰۰، ۸۰۰ درصد. هیچ‌کس چیزی شبیه به این ندیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130126" target="_blank">📅 10:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130125">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
کاسبی جدید با محدود شدن تعداد و ظرفیت کارت‌های سوخت آزاد: برخی متصدیان در ازای «شیرینی» کارت جایگاه را در اختیار رانندگان قرار می‌دهند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130125" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130124">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a188028b7e.mp4?token=W2sOLcp4PqczOL2gE9dNdL6PmO139SU082G-wjpoG7EqOGiU3X8ixkx38zf2GebE6jUbRuZIBIXOcRmBr2AafXucVWQi3kwE7n-sbgxjAESZDEu41EqN0Vwwr1eqoiOjy6hTaj4v-UvjjurP656P3s7au5A7FPrSPN3LbBVCM2StZBUq14tEEkqSeH_Y6dzdk2s4MSCbkiQi3XCTvrHqTELidaPFd5RoGdQGPEfzM65l08nkD-YDPHzlXZYvz6tUP_aNJ6i8ttZw_qPe0p-VUx_WfdKdUIuyxkwuB3IApBvBcC8KwaRrxV95ZJOStSy6fF0LfQ61AcU37_PbeMDr4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a188028b7e.mp4?token=W2sOLcp4PqczOL2gE9dNdL6PmO139SU082G-wjpoG7EqOGiU3X8ixkx38zf2GebE6jUbRuZIBIXOcRmBr2AafXucVWQi3kwE7n-sbgxjAESZDEu41EqN0Vwwr1eqoiOjy6hTaj4v-UvjjurP656P3s7au5A7FPrSPN3LbBVCM2StZBUq14tEEkqSeH_Y6dzdk2s4MSCbkiQi3XCTvrHqTELidaPFd5RoGdQGPEfzM65l08nkD-YDPHzlXZYvz6tUP_aNJ6i8ttZw_qPe0p-VUx_WfdKdUIuyxkwuB3IApBvBcC8KwaRrxV95ZJOStSy6fF0LfQ61AcU37_PbeMDr4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسیب به ساختمان رادیو تلویزیون دولتی ونزوئلا در دو زلزله ۷ ریشتری امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130124" target="_blank">📅 10:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130123">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اسکات بسنت وزیر خزانه‌داری آمریکا روز پنج‌شنبه مدعی شد که معافیت از تحریم‌های نفتی ارائه شده به ایران قابل بازپسگیری است‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130123" target="_blank">📅 10:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130122">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
🔴
جمهوری‌خواهان و ترامپ استدلال کرده بودند، تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130122" target="_blank">📅 10:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130121">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رئیس‌جمهور موقت ونزوئلا در مورد وقوع دو زلزله پیاپی ۷.۱ و ۷.۵ ریشتری در این کشور:
🔴
کشته شدن دست‌کم ۳۲ تن و زخمی شدن ۷۰۰ نفر
🔴
طبق اعلام رئیس‌جمهور موقت ونزوئلا دلسی رودریگز، دو زلزله پیاپی ۷.۱ و ۷.۵ ریشتری در این کشور، دست‌کم ۳۲ کشته و ۷۰۰ زخمی بر جای گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130121" target="_blank">📅 10:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130120">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ درباره ایران: هفته گذشته، ما یک توافق تاریخی برای پایان دادن به درگیری با ایران امضا کردیم، تنگه هرمز را کاملاً باز کردیم و کاری را انجام دادیم که هیچ رئیس‌جمهوری قبلاً نتوانسته بود انجام دهد.
🔴
ایران هرگز سلاح هسته‌ای نخواهد داشت. این موضوع تمام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130120" target="_blank">📅 10:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130118">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9dc303a2.mp4?token=SACefIMvRsY1ImIKpq9DVYs1P_wmtP0iDQ6rW3Ms4FETQyXtCl-eJgOsNEhYvJgoTjjbyySwK8Wkknre-6IjoCdcjvFk6ss3vpLtBE9NN8ZPzVS7hGkQtrCtKjT_o6v6y2fzfIdH1wcbACmpKel0JDe1srenAHKhdYaV-iUykXowsoEuUW4gMoDJyc-5qvFXsIb7qhPfIdjsSDDxqv20QLPAGps2lRE5TV8ORfV0c6gambCM0GXl0nXqtlOocjfV3wZpwi7genCvB_teFvxz9-3wpQH1sjxkCK2nz3wOBLNdT_iRO63Y6MJepgdDMUooUoNpD5cSebuPdddb3-hpo5kube9T42xis5ASVWNbs9HFyn29H-V4hBF8RATMQHnr7NtUter_ssDgaZJ2gZdzOHGAgCLCtiZCNUW10V02O4fqq8fBamxR5z3MewwmioM1EkTPAIcKzWcHXi7dNSGHZ0En4HaszuXdozfJm5WXy9K0GrDPH6J_xGjnNv1xuZx5xbvyDIfp8jxHC4gCwK-meT8jbBJBPIdo-raKsDt5urM-YKUAD_ssh6vTFE0E7jSrz0d-9UkyV4ZqflQH9KxWpE62NPz03kXDmauZy03kx1ktePKJB9BL78u2DDwVSoz4YQjgCA0FoQeTyhtvTYiCJPetpa3JmwRR8apZV8-tDc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9dc303a2.mp4?token=SACefIMvRsY1ImIKpq9DVYs1P_wmtP0iDQ6rW3Ms4FETQyXtCl-eJgOsNEhYvJgoTjjbyySwK8Wkknre-6IjoCdcjvFk6ss3vpLtBE9NN8ZPzVS7hGkQtrCtKjT_o6v6y2fzfIdH1wcbACmpKel0JDe1srenAHKhdYaV-iUykXowsoEuUW4gMoDJyc-5qvFXsIb7qhPfIdjsSDDxqv20QLPAGps2lRE5TV8ORfV0c6gambCM0GXl0nXqtlOocjfV3wZpwi7genCvB_teFvxz9-3wpQH1sjxkCK2nz3wOBLNdT_iRO63Y6MJepgdDMUooUoNpD5cSebuPdddb3-hpo5kube9T42xis5ASVWNbs9HFyn29H-V4hBF8RATMQHnr7NtUter_ssDgaZJ2gZdzOHGAgCLCtiZCNUW10V02O4fqq8fBamxR5z3MewwmioM1EkTPAIcKzWcHXi7dNSGHZ0En4HaszuXdozfJm5WXy9K0GrDPH6J_xGjnNv1xuZx5xbvyDIfp8jxHC4gCwK-meT8jbBJBPIdo-raKsDt5urM-YKUAD_ssh6vTFE0E7jSrz0d-9UkyV4ZqflQH9KxWpE62NPz03kXDmauZy03kx1ktePKJB9BL78u2DDwVSoz4YQjgCA0FoQeTyhtvTYiCJPetpa3JmwRR8apZV8-tDc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداقل ۳۲ کشته و صدها زخمی در زلزله‌های ونزوئلا
🔴
طبق اعلام رئیس‌جمهور موقت ونزوئلا، ۲ زلزلهٔ پیاپی ۷.۱ و ۷.۵ ریشتری در این کشور، دست‌کم ۳۲ کشته و ۷۰۰ زخمی به‌جا گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/130118" target="_blank">📅 09:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130116">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c90021fcf.mp4?token=csGxwWMupsU-UXFeJmHNeWFxpcUHcEVPBUN9EsEu0crmegyBjymxLW5t2fxxSxUMASfNO07Xvz_3gD1_Vi3ilhsgBvsdyMwn-Qx0M60ZfnE9nDnHLVfWL_WabXSvEgVIkIlJuPVdWenfG7m46N7wedoSTUAmrqTAqRaCh6rpM184KbUOIaqJTHipkW2Q4CaVmGZ8T4Q2UP7tkQGElJPeAYfAT7lfQogI2i0RVq8L-jamxw-AidECwl7FdHica8aQRIctzSd8bc-aaE3NCSYlE-7FuuNjJ1siZJO5YkB2yE3tg8ZgB9WlO0wXVfwCrMAFPCL0c8mJaIvnsYvuu7wc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c90021fcf.mp4?token=csGxwWMupsU-UXFeJmHNeWFxpcUHcEVPBUN9EsEu0crmegyBjymxLW5t2fxxSxUMASfNO07Xvz_3gD1_Vi3ilhsgBvsdyMwn-Qx0M60ZfnE9nDnHLVfWL_WabXSvEgVIkIlJuPVdWenfG7m46N7wedoSTUAmrqTAqRaCh6rpM184KbUOIaqJTHipkW2Q4CaVmGZ8T4Q2UP7tkQGElJPeAYfAT7lfQogI2i0RVq8L-jamxw-AidECwl7FdHica8aQRIctzSd8bc-aaE3NCSYlE-7FuuNjJ1siZJO5YkB2yE3tg8ZgB9WlO0wXVfwCrMAFPCL0c8mJaIvnsYvuu7wc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت کاراکاس پس از زمین لرزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130116" target="_blank">📅 09:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130115">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMBA4qQWt-AzyQqOHOecTrwyFnEHH5yKompnNg-MPrOZB-nIW9rRnH1nQxJMTb2Oph3LCmNwHcM0KddOZPu6wnitL3zHnkrnnlxtCoz7yfHRpnUg63DFZILHSixb-TNv_bSI1XxwsamtYzrA-qln_0W4u4z4SeuyfkM6iMD9dJaUkGCD-oITsTiDbNb9Cy9L4IShQkcSxWSzukNzGKR6tMB_7nCXZ5K136fMqeSiE7ArQbThjXoc7I_wgPn0ab4MMhc1GHv197SYZCFU3WksJPsgyBmZKSEii-Q47IJ16duOTYthesMclYE6z4-1DQcNS2_FKYpf5sIF75YghhEUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو
:
آمریکا در این دوران سخت در کنار مردم ونزوئلا ایستاده است
و به دستور رئیس جمهور ترامپ، وزارت امور خارجه بلافاصله تیم‌های جستجو و نجات، منابع پزشکی و کمک‌های بشردوستانه را به ونزوئلا اعزام می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/130115" target="_blank">📅 09:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130114">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYwQzmEbbKte-9V-kiBekM8oT0sCCeyJMVnyM_68I4nZmnwCM5LY20gl6kzd5Isb76T4PSYs9Etocj8NMnamAXISJc_8uCuIZfwxZxH52Keix21SG5xbj4jwrsaqmVuOyCMKUBbuIhVriehAL3y6rCxeMZ3rp8GyGO2NvXonAEYCas3AAFSgAabPgMKhADPh0Vphq-6zcFq4QOr5ky19pUYCrwzmctBeruOW55gnBMsBhTNEJ_u6XNRGzzrNBv84NdxjvRRbsqNFWO8z4GxdoefvWLNbfS_4VMHlUg4vITsOsqi5X-zbTZBE2LMyXSnajSnwCX_jZ0Q_iunz6HOd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور: نه ظلم کنیم، نه ظلم بپذیریم و نه مقابلش سکوت کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/130114" target="_blank">📅 09:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130113">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMCxnVIu8tKKP4irFTJOuSn1NJ1u4jf4ULznpTwJb9u5_SJ2OHyVZBmAZIXWWxvvssw4I6QgNE_vUVpvKWZyIJnp0sVJ-cWwIW1A-G7ACC2nYWOpDgmh-jMuiqNYWMuJwfqOBH4k47gzXhtuH5rwuhfwdcEEjU75iDztZtnsZc5yfeZnGh1zZyveRRJcnyoCSg-9jDrJs2d11jlUDdDvhNC9jNHmycxL0U_89jaZn1Cxx4zvSIUqT7fM_jds-BTnCjHuU9-kzT-1FI73o2Q9jcWur8qSI2HPtc-al6p8Ou7nzXpSuQAHrKmd05Q7Y-mMAFzgxfnpyeNQF_irDdFirA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دو زلزله بزرگ که به تازگی مردم بزرگ ونزوئلا را لرزاندند، هر دو در مقیاس وسیع بوده و تعداد زیادی کشته به جا گذاشته‌اند. ایالات متحده آماده، مایل و قادر به کمک است! من به تمام نهادهای دولتی دستور داده‌ام که برای اقدام سریع آماده باشند. ما در کنار دوستان جدید و بزرگ خود خواهیم بود. گزارش‌های اولیه خوب نیستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130113" target="_blank">📅 09:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130112">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzBFMEDnMJfUIRh-abkUopZ5j1KX97dSbeximqpyjN7gHYIMzwVGkvAJKV9tp4W7UwEJnHAlQrX1tjpSdG00i9tYqrXnoWTErthDnqM2PEWM6WvpdWbSzLz8YjCVVo90jmrbSzF5CvAre3NzYV-SYyQA7xogHG80hLhjBkvOhJqOZNjRc-iW0M_agHDGu8uFFzLcJ080jdlm9MW7k8780fX9dPP3_ccTiLpz6vgcRIDq6Py8nTE6Wpk-6xIGhYk8rCmoz07Xs3T3cwV1Ckv6xI87TSNRiXOckvAvItiiQCsyYco0DryMyG7wJawbWo4t304sWaB8mAHhHUsIb6MZ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت تنها ۲ دلار با قیمت خود پیش از آغاز جنگ فاصله دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130112" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130111">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
دولت ترامپ از کنگره ۸۷٫۶ میلیارد دلار برای جبران فرسایش منابع ناشی از جنگ با ایران درخواست کرد
🔴
شبکه آمریکایی سی‌ان‌ان به نقل از نامه‌ای که به دست آورده است گزارش داد که دولت ترامپ درخواست بودجه تکمیلی به ارزش ۸۷٫۶ میلیارد دلار از کنگره کرده است.
🔴
هدف از این بودجه، جایگزینی منابعی است که در نتیجه جنگ با ایران مصرف شده‌اند و همچنین تکمیل پروژه‌های بازسازی در پایتخت آمریکا، واشنگتن، عنوان شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/130111" target="_blank">📅 08:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130110">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a33b09c4.mp4?token=txWSzrTyaZB7mOaxX7y6fK3mgwHW8kd6MzlBMi5D2rwX0ZGl7j3erq8nyhAZ4-oiqK0gfe1H4PwQsru-nE9U69jsGQOe0Lpx3pfPahxlFxtcR3yXG8khoL9WlI6iPBN97UoY0fqI1wymeQcqSo5_FeBK2UYZVWn-DwnsAefIY_KyOluHhZxvWvBV7kJChswrjN05mI5dLNyTRjdkksWc-b3A03_1BwNNNHjd3iRlQCqcLP1HeAWB-6eP7iszmOv9PwM8l-xjexq_jEhqGVYKXblKksKkExDb7yEU5sgwFqLOr9OFKQvZGokf7b0Tdwzil88KqmcIGz_PYJzrtX7GP38X0Cjch04TSO0DD59pRCMeF8ixgdcmpk41gY5GnQ-vja8j3CgTD8Y5OU8IpWkMoNpRkwRWxdQWc2hzEeLCHwW1-U9jNkX3d8LV1NdQng7DIUp13Ce9nB49nxVYQUvMwhzOhOcv9fCnHPYpggXLknyJx5_XThB5128tOYJMYkhGv26D-wShD6g16Vtvb6ayfVqG_JZL-UeZYtrid60SY9wZrZJmxfA4Ag0G6u4gDwvXtwj77qnayniruVbke0KF0Tz33kXC6cPpeRkpZvLSzs47NCTDjqWvu4YL3W_yYvrf9jwmPEWG6mhBUpCTm_94l33_J5VPJCLQvqt5Meh0jG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a33b09c4.mp4?token=txWSzrTyaZB7mOaxX7y6fK3mgwHW8kd6MzlBMi5D2rwX0ZGl7j3erq8nyhAZ4-oiqK0gfe1H4PwQsru-nE9U69jsGQOe0Lpx3pfPahxlFxtcR3yXG8khoL9WlI6iPBN97UoY0fqI1wymeQcqSo5_FeBK2UYZVWn-DwnsAefIY_KyOluHhZxvWvBV7kJChswrjN05mI5dLNyTRjdkksWc-b3A03_1BwNNNHjd3iRlQCqcLP1HeAWB-6eP7iszmOv9PwM8l-xjexq_jEhqGVYKXblKksKkExDb7yEU5sgwFqLOr9OFKQvZGokf7b0Tdwzil88KqmcIGz_PYJzrtX7GP38X0Cjch04TSO0DD59pRCMeF8ixgdcmpk41gY5GnQ-vja8j3CgTD8Y5OU8IpWkMoNpRkwRWxdQWc2hzEeLCHwW1-U9jNkX3d8LV1NdQng7DIUp13Ce9nB49nxVYQUvMwhzOhOcv9fCnHPYpggXLknyJx5_XThB5128tOYJMYkhGv26D-wShD6g16Vtvb6ayfVqG_JZL-UeZYtrid60SY9wZrZJmxfA4Ag0G6u4gDwvXtwj77qnayniruVbke0KF0Tz33kXC6cPpeRkpZvLSzs47NCTDjqWvu4YL3W_yYvrf9jwmPEWG6mhBUpCTm_94l33_J5VPJCLQvqt5Meh0jG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زمین‌لرزه‌ای شدید به بزرگی ۷.۱ بعدازظهر چهارشنبه در غرب کاراکاس، پایتخت ونزوئلا، رخ داد و لرزش آن در کلمبیا نیز احساس شد. ساکنان کاراکاس به خیابان‌ها گریختند و گزارش‌ها از خسارت به ساختمان‌ها و اختلال در برق و اینترنت حکایت دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/130110" target="_blank">📅 08:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130109">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: بعد از 3000سال من صلح رو به خاورمیانه آوردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/130109" target="_blank">📅 06:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130108">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ: قیمت‌های نفت به شدت کاهش یافته‌اند، اما ما در پمپ‌ها چیزی متناسب با آنچه باید باشد، نمی‌بینیم. به نظر من، قیمت باید در حال حاضر ۲.۲۵ دلار در پمپ باشد، اما ما بالاتر از آن هستیم. ما در حال انجام یک تحقیق بزرگ در این مورد هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/130108" target="_blank">📅 01:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130107">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ:خیلی وقت ها وقتی با اردوغان مشکل دارند می گویند می توانی به من لطف کنی و با او صحبت کنی؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/130107" target="_blank">📅 01:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130106">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ درباره زهران ممدانی: ممدانی دو بار اینجا بود. او مرد بسیار خوبی است. او مردی جذاب و خوش‌تیپ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/130106" target="_blank">📅 01:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130105">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: کشورهای ناتو خوش‌شانس هستند که روته را دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/130105" target="_blank">📅 01:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130104">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237a076aa9.mp4?token=G4vAHcpZe5Ux7iGuqgqDVto7PkVFCJsPDYvdLfochQtGk-A8GGwwqfwE-4Lv09hV-mciu-r1rbwvLvXOtXo3dUex4P_gS4bKnNU8mngOSdRvKfJq26qrjCFfPNPQXOjbVBqHgRY6LksHDWuAfks348n-aZgjeyP4jdbHXxXuondxmLFYZaZ5c7Je2epzdoyHR3DGmiE2tS4hY0p8uGy0z64RADQwaIrZisYxjCfItXqCppGmkt6WgKnIqjzQS8clIqrWjbwREgDL_mOdwTPiPvnWdNI67TpNxdvoQ3zzAyy-sGPOUKsVi7nT8EJZFhAMxY0DNplTrRaFvyTja64P3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237a076aa9.mp4?token=G4vAHcpZe5Ux7iGuqgqDVto7PkVFCJsPDYvdLfochQtGk-A8GGwwqfwE-4Lv09hV-mciu-r1rbwvLvXOtXo3dUex4P_gS4bKnNU8mngOSdRvKfJq26qrjCFfPNPQXOjbVBqHgRY6LksHDWuAfks348n-aZgjeyP4jdbHXxXuondxmLFYZaZ5c7Je2epzdoyHR3DGmiE2tS4hY0p8uGy0z64RADQwaIrZisYxjCfItXqCppGmkt6WgKnIqjzQS8clIqrWjbwREgDL_mOdwTPiPvnWdNI67TpNxdvoQ3zzAyy-sGPOUKsVi7nT8EJZFhAMxY0DNplTrRaFvyTja64P3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا می‌خواهید اولین فردی باشید که در لیست نخست‌وزیر جدید بریتانیا برای بازدید قرار می‌گیرد؟
🔴
ترامپ: خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/130104" target="_blank">📅 01:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130103">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ: درست در میان یکی از موارد کلیدی: «ما اخبار فوری داریم. سنا رای داده که می‌خواهند ترامپ جنگ را متوقف کند.» ایران این را می‌بیند و می‌گوید: «این همه ماجرا چیست؟»
🔴
من احتمالاً کاری انجام خواهم داد که اردوغان را بسیار خوشحال کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/130103" target="_blank">📅 01:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130102">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4db3d1db8.mp4?token=X549M4FLp3f-dsYgb6bFXSm8_IFfSDndM3glJ9K-VOAn6tCARdJyJpIpFs06EpqOERy8S3tHX894NPTSaaj8GrEuihqTP07mg7JNbA_RoLibmaNwt4FXoHzCvzH75di-88i4cS9TwRR117Vvux6oCEQOxodNiMUKt8S4PbvKcpVL-O7ZYfnutnG5grMvK7XVBUQ8edeGKKCnqfV3He5DxKHXx7BQK9_jd3_I7HiZfryKbhpA_DX6DxBW2kEFOAbT3t7szMMNAwPwtucytnL2wLWn5STvtasvn0mk5k_U2dlYMXCbiab0ammbj_lnWBXGdSDoaK9aH-8xU-HNIFWEBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4db3d1db8.mp4?token=X549M4FLp3f-dsYgb6bFXSm8_IFfSDndM3glJ9K-VOAn6tCARdJyJpIpFs06EpqOERy8S3tHX894NPTSaaj8GrEuihqTP07mg7JNbA_RoLibmaNwt4FXoHzCvzH75di-88i4cS9TwRR117Vvux6oCEQOxodNiMUKt8S4PbvKcpVL-O7ZYfnutnG5grMvK7XVBUQ8edeGKKCnqfV3He5DxKHXx7BQK9_jd3_I7HiZfryKbhpA_DX6DxBW2kEFOAbT3t7szMMNAwPwtucytnL2wLWn5STvtasvn0mk5k_U2dlYMXCbiab0ammbj_lnWBXGdSDoaK9aH-8xU-HNIFWEBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا اگر یک توافق نهایی با ایران شامل هر نوع هزینه‌ای برای حمل و نقل باشد، آن را می‌پذیرید؟
🔴
ترامپ: خیر. برای من غیرقابل قبول خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/130102" target="_blank">📅 01:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130101">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e8734849.mp4?token=TKV5CxKynugUJUVPQcn0AHXVhtLyrwGO_KHlR9HXzQk8_BxQUsUBb52FOEfGwXbuxApwb_YwzKEtp9HrhrZhA7u2bfaFOUprluxpT3hRlToERxlV0nAIFr-IDSyOA5uK4ybvLeq495BJgcPq36k8Spilh-45Sw9TlpOSEUcBzlt7YDT0O_ZoBvVTbQuSzldkexWsJnTryTgullfkGRUf9Tup-kKkk_o1u8tO5N2oBSHsexJtAEaYzNrrKI7gyxgQ6GPT7wo8_UkDj_6JUc2Z_Yt90q8SLKDnHn4mQXUweHd5eupF6vWuTE53o1p0WALUq7mV-mG2jhCKrjFGTpGDvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e8734849.mp4?token=TKV5CxKynugUJUVPQcn0AHXVhtLyrwGO_KHlR9HXzQk8_BxQUsUBb52FOEfGwXbuxApwb_YwzKEtp9HrhrZhA7u2bfaFOUprluxpT3hRlToERxlV0nAIFr-IDSyOA5uK4ybvLeq495BJgcPq36k8Spilh-45Sw9TlpOSEUcBzlt7YDT0O_ZoBvVTbQuSzldkexWsJnTryTgullfkGRUf9Tup-kKkk_o1u8tO5N2oBSHsexJtAEaYzNrrKI7gyxgQ6GPT7wo8_UkDj_6JUc2Z_Yt90q8SLKDnHn4mQXUweHd5eupF6vWuTE53o1p0WALUq7mV-mG2jhCKrjFGTpGDvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا فکر می‌کنید زلنسکی در حال حاضر برنده است؟
🔴
ترامپ: خب، او کارش را نسبتاً خوب انجام می‌دهد. ببینید، هرطور که به آن نگاه کنید، او کارش را نسبتاً خوب انجام می‌دهد.
🔴
او حداقل از پس کارش برمی‌آید - بسیاری از مردم در هر دو طرف می‌میرند. اما فکر می‌کنم او کارش را نسبتاً خوب انجام می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/130101" target="_blank">📅 00:49 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
