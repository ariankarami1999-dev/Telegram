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
<img src="https://cdn4.telesco.pe/file/fqXI3Xj7SOQHnyhjSsW8rji3UjtoEk-wYlTSRQFMgSxRn_89B3UbHcMhDlQ5SOWR7Y2O446awa-LFPrazbBddvbuWPggNReTDCA-YUIM-Wp7PIB9avLc7mGs5QBCG47UtHrByTm2OdJliTu5FOH3zvjgJKM3ity7GRwOo4OF3sBM4jtD30G5am3IRk6kSXUFmpwPVAwkLBC-TCJn553PFPrE1RUbVimNn1nJU-yBrrv4IxX34O4h_7EmvmGWhG0qUVH_nYLtdqrTqQ-Y0fclfj8AkquO-7BMe9G5e5HYsKrWoEGtL42BviWfxf0WyggkxF2OXNr_RjKEyDqa6ZgGZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 470K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 15:01:28</div>
<hr>

<div class="tg-post" id="msg-30184">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8_WZr3WskXAV8ZhCbDrc8jQgkdaOjEJaURJOHafvK7KYDiv0PA7YirTjDaw1U_dCJ7vOKEN6a7fzpk0vVZxl1QFkkEVYsGjF2gG_rRmlTgNTnBMmJ86woZ6w7N426etn3a0p1ZyQAskkPimViBm5CM2U5ynUwt2-9ABrhR7e15Tjw-CNZpWX8swtK5e4BV8aNI079ZSVjWpjckWqgo0Wzw_-B24nql_oHlblQCnuEFk5uoR1ZtYFlHNYxi-E9Wg1VgiOkkZNuKx5Mih6trfCAzB7Kt9xRWfjKECmyHqgwUtu4tneCvft8IjZe996QSUrHMMUSDqr7E3EQ8bv-uczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/persiana_Soccer/30184" target="_blank">📅 14:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30183">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVeZGgusF-PBdZaTYkSEP2EnrtKwQUgUqSQ_8fBGZwFSVhyicXcoOchDiKunlS-gh2EMzorE6wU_UVw61u3zKL4IxQk7-yjmUT1tVyUfe7p6tP-6O8nDHZs9MwCUfT5bnRNa8FiNVemKG24p7nxRNpl-2q33Dyo_LHBv8lbk_QnyCX3d5v3EfYRRWW0Rx96ZN5x2RLtwyzbEBBqVhWwM14k7vaRWrENWXksHBgrSbcNbji0Q8dsUthn85hpYmk1T2QA93tanjkGtBykiMLDvNMZhynq4R5KdrQVJ89E8gU3XPzEx4QWvZmiZrQg1gLK_6Kp5uNwjHa3NFKF83hEUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/30183" target="_blank">📅 14:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30182">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVmC5RDc0LiVQyYX49cbxsPfRxIhac1UoGhfZ1svOkn-MaiZE2lRBL9epIEzLr8EITcXOQ2C-uV7SLomEq8x-dIP2FJmhgz7XUVb9GyKoxF_jXaP1OC9Zarw-IE2WqfZ8j7OMcrHM4fAGts_6cj0GHqWxRC38giwixzMNKs6WE-aiMi6o20nlflDBKAG45TCj8Az6DT_B9jRsPQ4xslBodrSguYDnq1tJunCSRfnWw9Y1kzr-aC751yYWCh4UIoy_pd0bfGQ1_zxoaBTWfN0K5TkglE1RSADUonKAcULfkPUI9T7VCbvmGV99jls_N6goOiG8DuZ0H_lSwiRbeqftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/30182" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30181">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
آرزویی‌که محقق خواهد شد؟ درحالیکه خبرنگار فنرباغچه چندروزپیش‌ گفته‌بود آرزویش اینه رونالدو به این تیم بیاد حالا رسانه‌های عربستانی مدعی شده اند؛ رونالدو در نقل و انتقالات زمستانه به فنرباغچه خواهد پیوست و شاگرد کارتال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/30181" target="_blank">📅 13:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30180">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4ME-oMSII2MxiVVWMtUa1lGsFAANbH9ptZZrRn8O9m7tojFyoDtmwisMkw1AHvUodRJLW93srg_ebTWcpWU2GHRVwlkazeKEa624BOFj4FrcU0ab5Bg4ikohFlVju5CZzjCQI5Wq2Ifbw5LtitZymnOfjyUGatscJxSi7ILxFNtp3I09OVLLz_1BdiaWPWSrsOFwPpANSfZGpvKcKpGtmpsrTwhYJ7W-O_dqg9Fw_LnT2PYtG4EKehvdFVMW8Oo85phzcl_3OQyPPQa3ToJUGZ3pVpdEAN-LU7BLdYlF7__gjo2qkpziNln0qXaBiyW9iDM4T6suRN4zG1eeRDymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/30180" target="_blank">📅 13:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30179">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9om5WKuR9cjaFvliULWxu-ackRGUMBEu3fzRMNJv3jUgBCrebKGVzpX7oC0-NjxSOXJi2ZmfIMKBort62udDU-h9RtE1Wg95Kf6ZV3SeSVH5i8q4kETjBb8i6_3LM44F-epu09ITYj3zRYsSrfQ2X_3xrmrepe6s28Opm1nYnTCLccJgCgVk5EEp4NIjyXRBFlXhFE_v4IEbLxITC4BlKOdjLM6ZwcTKwZ8Vi1La6MlxFNTGb5aitHU5yd96fd3V_CpizkTWmFK4nVCdRzh7MPouCx2kFcRdKnJ_R2CTV5jxOCycXc-5H_NLZFOR9VOmpqq0OUMf707RZBxQInA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/30179" target="_blank">📅 12:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30178">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSwRud_S5v4puuIlo7fxvf3ZE7FbWjWel9rBJ0VX08rR-4CQQgla5CJFTXuOcVujzv2h4Eu1whZATIAndnUcWwfCJWPLUwbPQCVmIibuSj7QCiR1YDP-feaG6bhPGb013Wz4tP3Nr1rXkMJLMPHko_EFp5UQz4iRDvyc11718oeFU59Ho-ZfdgYYJKh9nRnZ3XQD4eHDaITfJW012-l5Lt0jRyYD4semkewrvedsSREeMeNVokrTVxmNzlfW00M_2RKFDryUX65whdgbkf0IyCkQSIfwc3svj0JrSUjlW-S5_m6GguXwKllanRJQDXylwhd3cefoN4PUPmExIGTStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه بان تراکتور در جدیدترین درخواست خود از سازمان نظام وظیفه خواسته کهه یک ماه سربازی‌اش به تعویق بندازند چون مریضه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/30178" target="_blank">📅 12:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30177">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qighfA2dSW9FiiwDN1N0xdyXR_U5hXSjpktW67k8Qg4WRdsWumcCAZIQld2NlRN48RbSL42y3G9N6jXh5FA9HQVl0pKv5-2LpBf5o8y08evB0vjzrGugj0uVUlJqah4DDrLPLA0rTnJHMJoAgM0sQ0AYepfnrNPne07zGVt2iOurQGJ_JUsAoazNUyPLbbzDEkELgUqF3Q7QRdiu8zlits0jcb-MnqpmrcnPunLkkj-6mCRn70CQrZbJV0wVNENhHCd-x4tHoy6NObU69fTOOd0F4wV_apXq84XelohCWxDDroV2dvaO9QxjBTDyLNUk1yLpRltRvUjUp3W4RWHwrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/30177" target="_blank">📅 12:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30176">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b904658a51.mp4?token=O-YgSnUG6ScUQLuHmmTzyKB0ebk68MaHY6cIh8aB_FDIU1H0qq2-zDD3Iz1qnoN1Bp-VKkrGnNNwSoRUg2qKzZPQOgnBqnydI7IZGD8stQHS5QT8zg2A69QxSruyL2Ze4X-xIzN_4oFNj0KoL-PdDhHaNCBz4jfghEMMStKebU2sR49ETaJFWhdqYLA8xLuFuI0ns3khHruAvBHazZEdalVy3E0w1SgWKUSnPjyrz1IQuat_Tz30HpW1m0lzRfQv1ExusjSY7GQpj_P2JpZUbQUjJt0b47Tik9XiYh8T5Flt9eHTnjbTnqn8-oObs5WFC55sngg74jJJhyJc3e73Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b904658a51.mp4?token=O-YgSnUG6ScUQLuHmmTzyKB0ebk68MaHY6cIh8aB_FDIU1H0qq2-zDD3Iz1qnoN1Bp-VKkrGnNNwSoRUg2qKzZPQOgnBqnydI7IZGD8stQHS5QT8zg2A69QxSruyL2Ze4X-xIzN_4oFNj0KoL-PdDhHaNCBz4jfghEMMStKebU2sR49ETaJFWhdqYLA8xLuFuI0ns3khHruAvBHazZEdalVy3E0w1SgWKUSnPjyrz1IQuat_Tz30HpW1m0lzRfQv1ExusjSY7GQpj_P2JpZUbQUjJt0b47Tik9XiYh8T5Flt9eHTnjbTnqn8-oObs5WFC55sngg74jJJhyJc3e73Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه‌های‌محمدسیانکی‌گزارشگر بازیای فوتبال به شاگردان در مستطیل سبز که منجر به گلزنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/30176" target="_blank">📅 12:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30174">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=SxTw2JFo6ulY_wpo2SX0R-vQywRtM4khfiaJls0VpQosd8SJDR_7qh6UHYFXsYbL3QpSjkRIoBU9taiKjh4zArvFW7soSrQSentxDgWW59BRmYY69rg2WvgVsiYSfvLQj-Maw04QKw8N6mki9cDH0t9cqF9oD_O3urMvXzzK-H7vEwD1rh6LrEMyBl1kssSXNd8fIYjUNlyjfVE_BlvMZSVrbozcwIymyLVMPC0ikhQRoo1yJ3YKX3F8RRD8mofAat-o0Vj5lZs8NwXD9NWLJ0ESTW9XVwn_oTTbVrNiT0oMEaCkuALSYY1A0WmkkqjeV9_p9CIX5jMljNHN6FOSRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=SxTw2JFo6ulY_wpo2SX0R-vQywRtM4khfiaJls0VpQosd8SJDR_7qh6UHYFXsYbL3QpSjkRIoBU9taiKjh4zArvFW7soSrQSentxDgWW59BRmYY69rg2WvgVsiYSfvLQj-Maw04QKw8N6mki9cDH0t9cqF9oD_O3urMvXzzK-H7vEwD1rh6LrEMyBl1kssSXNd8fIYjUNlyjfVE_BlvMZSVrbozcwIymyLVMPC0ikhQRoo1yJ3YKX3F8RRD8mofAat-o0Vj5lZs8NwXD9NWLJ0ESTW9XVwn_oTTbVrNiT0oMEaCkuALSYY1A0WmkkqjeV9_p9CIX5jMljNHN6FOSRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کل‌کل‌کردن دوستاره‌انگلیسی و آرژانتینی در بازی امشب رئال مادرید
🆚
اتلتیکو مادرید: جود بیلینگهام: تو لیگ قهرمانان اروپا داری رو من تکل میزنی؟ کوتی رومرو: تو جام جهانی داری با من حرف میزنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/30174" target="_blank">📅 11:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30173">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/driLqOkT1g6RSqdPZOO7njs-RsbNrmEZ8q8ETRTF0NPr6_HhnAKOQ6riNSeJc-wNnZ8KYA8cVU72ZM5YnC8yaALufQA2c4iKj7OqWTpjmSJ1__ZUZqXP6XQztHFvWD_xG5g__7sphZ5CANPgEcAZpOzm1D074ZmbeaI-_zjSW0tbznpexvezQONTkvrNf7VnMPxfzRACNXQH0P0Wb-JtCaxpkouC1zVD2irpLFrKrOCWbnkI5pr-KaSluR5XnNgjlt2w117EOXbX1QIdBMAF1nu0V58XTS687Qa1Fs-40I2vbMjYm7DvLr7kBNsFZDVUt9bjxHzuMgvnSfaPmNJaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینیYekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🫰
لذت بازی های کازینو با 100% هدیه خوش‌آمدگویی تا سقف 100 میلیون ریال
🎮
بیش از 5000 هزار بازی کازینو زنده و اسلات
💲
🤩
🤩
🤩
فریبت ویژه واریز با درگاه های کریپتو
⭐️
🤩
🤩
🤩
فریبت ورزشی برای واریزی‌های ووچر
💱
🤩
🤩
🤩
کشبک اسلات ماشین و کازینو زنده بدون سقف
🛎
گردونه شانس یک بت با هدایای نفیس
🪀
هر روز تا 180 فری اسپین (چرخش رایگان) در یک بت
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r30
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/30173" target="_blank">📅 11:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30172">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWneZox1XSVjfzs2o-9oEqdomOGgQPxF7LBsPnxxUbJ9GhYZ_C-fLzDqwvFIf4z5cVl4UAN8HNboZk0fclWuiSevUSwA5S9kIBKbsAsLxOure3xtVkQg9R9dEEgeVLmZeT3pSxVrtknqE_YSC2zz-gbyC6XuyzNNpdJ-7QMwHrBE9ZQW_wMG3GRF-JlsB-jSIoWSZJNskHcAqWAvUeHZA8pS4ii71ioo5BrTaJOmEn54ZGd-TR6Nj64Mj-85T1aLoHgdqAyg3aRRi0cNeQs_luN5gRpKEFd_uKZjCQ_1OJqc5Cv6xhn5sCAGmGMdGK_KLbOhiOl5m_tY0k_qvtRjBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
دو مسابقه استقلال-شمس‌آذر و تراکتور - فجر سپاسی شیراز در هفته یازدهم رقابت های لیگ برتر به دلیل بازی های آسیایی این دو تیم لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/30172" target="_blank">📅 11:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30171">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpV-59mAU-tBR7DXe_fDD5gPxUnpnKHv-xNV4Ona5l0BCtyUm7QxhVRG8uoaNhC2g6dO6V6VOm_7heIiB0uaVsiiGl-cw6r-4D90eH07mIDwem2Y3svG86_d90QgOIM6VAYxOvS6vgEjq8b9_Qh1CxzNgLoRWxU7Rn0Oxwlfncoufwb7KVfvcbarQM_IuDWhxnzv9GW527oKqWMvPkOZyuVLa6HWJy3pwDUwGhQBghNmvGJrnhndUWDylvAV06TZgjS6s9T9tpiMil0P_FKqATqePqMbTYHUmKI4QzkoZzyoQY51CY9MeoRPnSBvOPyWjVEqi0NG8jS50gw0Q0iTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت نهایی سه نوع آیفون 18 پرو، پرومکس و دائو اعلام شد؛ آیفون تاشو یک میلیاردتومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/30171" target="_blank">📅 10:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30169">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyXduN1jZ1gv5DO_XnC6Asbg-WCiR4FHlwBJ7ReuaxgCrRbPsRvx4cb5NIrwY-23tzUq9m2FUfAQ-3hrDSsQE4hQCuHrKfz8oQZlHQAQOq9pf41IrxzvYYowDr4Ok3crJfqPwgultPKD6Bv7LU8MkPtoDgcC1P4Hm_1dszbAsQndpgeidaR-83mT0FYWyB5m_JvpJcsWtet22HlINsx0CbeolaEsqZsZnh8v8fvXf7bFcVZ9ifA3IaEziM178uDER0nCK10ic9_BZWwhe8_HVi_MZgvWlpt3sgZX_PLKqtbkMQcb1yFIgpCkgg1jMRCe2OP0yh4xSupsluyzz_wkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORF3CqIp07sJ66HnZjzfRjB7PKVoqChwn4B8ufV7l6QnexMBIq7EY7j17x47Z2cR6XVYoqTxP8gGQwFIC_dph3oCIof3lXc0FdjBYHvFQXnp6uN2JIqEafyyBmNXZigfXD1jnvH5U4OwliVM54SHc6uWYOtAUhrG1Jtth55SDUOS3hn_NvylcbP3ClEk-6SPhvmID0mroWdkX7_rGSHC6f7GU7ESeQcoPW9K7WusI7v34xAkm7itFJ5GGlzVeMV8jPoQl2Ln3i7IR-BzBDj9iizfh12csjLgkiQ1liOGKvrROHuvTv51wDxvpSeBewVLThA4SVuMSqfS-IXO4LNbkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/30169" target="_blank">📅 10:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30168">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUB6Do67XHhluEMILsyxCWDBvv49GgL9butaw_7X0lLxht4An8XMo1UnZGADNdprJqIHdft4xq0Dr1fXU3edml7pbkBdDRPGY8Ln98KWPy4X20QNrmNGBrtDNgAjLv1YO_pESXFajPoq1NkMhJwSxboYquNheH5LyH_qGsvmX472RPSMR_P0SVRpVQ4ZrgJWCxBxTTpVGmTYUK-HMo1O5oMIbdgUtZ5tkqau84ASugk0huNrPaqOGaENuhh_DrvKFkAKe_OiHVIef0lwzsmX6__-A9yrW_kJvCUJjm2WP42Is6nSLB80F8Gsq-mRzG87GW33yZ4MXDno8KIs5kWVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولی هوینس رئیس باشگاه بایرن‌مونیخ: فروش اولیسه به تیم‌رئال‌مادرید؟ ازخنده روده‌بر شدم! حتی امپراتور ژاپنم‌ بیاد پیش ما اولیسه رو بهش نمیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/30168" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30167">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015580725f.mp4?token=H9mJMUWHVUk6vUUOB6i9tSM1xDsW0jqtGmqzSgfXNaAPLqwF2DMienGBTofeSQPk6CJiJ-zQhGY98T5g336VrAdOh2ypWQBbl-ogn1gp9IL-L-mAXQ9mtBo7pFzD7NvErEVStuQdV3H-nE9MKRUVmwjNuUZsqIPwsWlmBomff96Z90j4gf3e91ePbNymUeDZH7lhqf3A9gzouhxfpPu4RXgbsP2SW70Hk8ysXWFFvvDFnCvWhJmUxC4FRhzmwt8-KzJTMG69wYqMVq-WSp2sZt1gfSzE-v88KBnYi8y22OT9RUceEVQ3DgKJSrZZmEMhC2TveEIo5ymT-r5OsT6XGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015580725f.mp4?token=H9mJMUWHVUk6vUUOB6i9tSM1xDsW0jqtGmqzSgfXNaAPLqwF2DMienGBTofeSQPk6CJiJ-zQhGY98T5g336VrAdOh2ypWQBbl-ogn1gp9IL-L-mAXQ9mtBo7pFzD7NvErEVStuQdV3H-nE9MKRUVmwjNuUZsqIPwsWlmBomff96Z90j4gf3e91ePbNymUeDZH7lhqf3A9gzouhxfpPu4RXgbsP2SW70Hk8ysXWFFvvDFnCvWhJmUxC4FRhzmwt8-KzJTMG69wYqMVq-WSp2sZt1gfSzE-v88KBnYi8y22OT9RUceEVQ3DgKJSrZZmEMhC2TveEIo5ymT-r5OsT6XGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/30167" target="_blank">📅 09:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30166">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2_Xl5SM65dsx4t3QMnfnw5HkjkYHWnUmqlt3OeTZob3Ma3o8ZT08hxhotnQuupY40lZx8EpwrGXaAITK7pwP02fPRZBu1hnVS3ic4WDmoz380KBcmipyvDQgOeSWM9schsJPK-GpM7ByJyEPVkBh_j6c_kcnLYThczbdL5SdQLUXS43SD7uI5ABDOXw1WbnRxzFyc0wSUZTuzZMGlGJX1X5Z0K3AsVVxcNJ5aYJ8IeIy5EZwbaNAVoDlim5pRDc4uvoqT9zRBScgNzRPPriyrbaon4Pbk0rhTPrglfN6cHSiDdrI163UfXX3nbBZ3Kmro4OUV1uuCeE1yU4_tDjUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/30166" target="_blank">📅 09:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30165">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=YtEcb7Mk-EmdLMLc2sRlughLawA-bINEq_lKQxhYua1E66PeZDJrC9bQUI_F7L-q_kaYDCmf5bZxhasDz0i_azEqRjxAlfbpxY1tSr3mzYkWiupM4MFafxczqjCU6pYDuoPlzd9waGK0zh3lp-r9gQbmvgRi_afUfw6CsePIelh5fd8QyG-KZ2pboUdkwkwMyRHkarsS1lY-NJmWWUMR-zsceg8SrAG9yY8zNvMjWmBhw7GXSMRD_z8WZDS0sZkS97Fda_hEhEznl1b_-TVXFSulpzWR7oK0aWvD0H_hw2QWVgTDhCHV5FCGwvriKr5GyM49FbUwoEYLq9rELTKPIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=YtEcb7Mk-EmdLMLc2sRlughLawA-bINEq_lKQxhYua1E66PeZDJrC9bQUI_F7L-q_kaYDCmf5bZxhasDz0i_azEqRjxAlfbpxY1tSr3mzYkWiupM4MFafxczqjCU6pYDuoPlzd9waGK0zh3lp-r9gQbmvgRi_afUfw6CsePIelh5fd8QyG-KZ2pboUdkwkwMyRHkarsS1lY-NJmWWUMR-zsceg8SrAG9yY8zNvMjWmBhw7GXSMRD_z8WZDS0sZkS97Fda_hEhEznl1b_-TVXFSulpzWR7oK0aWvD0H_hw2QWVgTDhCHV5FCGwvriKr5GyM49FbUwoEYLq9rELTKPIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
مقایسه جذاب از عملکرد کریس رونالدو و لیونل مسی که ابر ستاره تاریخ در فوتبال اروپا رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/30165" target="_blank">📅 09:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30164">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7M3M7C57H9xdgTd-kgpj1BCQ7EroBt6J9QdLWNvyJe_W723x1MNx-MoRcO_HTnCzodEaYBwoB8aw-gg_FJsKVoqiW7vQGJZIQU9bgVriW0pSXAFmwIQrYPFrTmcKiS5AImI_SvOctMNVT9nsO5hwCI5LkazP7oF1oxRacL0fT1TW0NhQYXWECAaZcSAzUddNHxcg-4W7AWkSIUH7qgjrqD5AHeJCfmH0b5YrAJRn_fXCoD_slPV3ozJG9K-hS31dnvAGJLWXBTl7o-2RdgD7HfXwZmA5C5TlELp5zR9v1SRWOqje-0fLZHKmcIKfXbtGPf-8DHPySCD4OX6sJ4HFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30164" target="_blank">📅 00:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30163">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEqTi9ezswWxzn7n8DI43dgWjvfggOnBJlOmcgVFBONZbw6R85zhYUGEF64v3QSwgXB-iyAi17ld7KEuljOn3LyzS2jMR2RKR7On_R7IaaEgdZhy_DLGTE-MgU8tlayp7AH2GdvO1GRtYBQl1h3BEFGaj9oSoNkyP3fAhc4aiPf6zHPJC7DgzBkaZYGLnCxkxxkHxsS3Pb1RTWhE44R6sy3KARXefvq1Cpx13V6CULTMXpMgGGBt3OgDIWWzyvDbJs9frS14mS_ajvtJIAQVRqegFmZkYfERgWQmEbirU1FjUAYopPao_vz58JthhaWuvL9cG9klPP8dfp14tE6qGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
الریاضیه‌عربستان:جدایی‌کریستیانو رونالدو از النصر در ژانویه قطعی شده. رونالدو قصد داره به فوتبال اروپا و لیگ جزیره برگرده مگر اینکه باشگاه الهلال پیشنهادی نجومی و سنگین به CR7 بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30163" target="_blank">📅 00:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30161">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVnXDskv8rCVbzvRYCBO8ylQAw3Jjw0D_Eiy96fkVWKD5QGg6GV3chxg9hOTuFzesaWjwC3R44Ztn4LStvcSe6q0gOAKP4tDwCiN9U1nbEKa5imKy_2y0m48bqJSoNY7IvFLAUZv2XGUFvgANHoX_1X62yvOfvo40-u3240yw94h_FPIIusTpmc7Sg9RR-8WD4VnAUf7hHeAhANzrmn6uVW8dLVVXj9bphbjLt1_V-6j_raGxDKCJjwHCXqS2xVC81jyRhVvBwqZPAbPGloLwgHWXKAjW5EWmf55KjGAM8zZ3gKBisDOxT4aNMW4zbIRa8d0ShAx_pBaWayKMgP4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ جدال خانگی لیونل مسی و یارانش باسن‌دیگو پیش‌از آغازفیفادی و بازی‌های ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30161" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30160">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHMgq-6Ujtz02jQZKXAgR3XhnYAvUy4cK8RqKvf8VT4UxMoxRsDxmtfufE69tU0znUT2JwNBHGUpPVGMoBGnScKxuOzhr_apMeg-F2vGvzMh47a2tIF03fJp_swHcrRArCCs5P76MovbjLVV_-UTFhZcUJZ3b9Kfx7QJKkW6CQ6ehFw8iQ7y-ZGQeI2KGytC9fQA7B2M1JtRRPmqYAfLxZkXWWHnhO6sNGtHhhTJb2l6gA4CQsSs2YFzm_mJJjfQmx8hS-1aOUw6aqk47J7NZGnAEwEJnTFxukz2BQQ4e3f5FejFFZna3wwjUUK4LYKTLl40VBOIitMc4mO4asOMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌بزرگ‌ال‌چولو در دربی مادرید و برد اقتصادی لیورپولی‌ها با تک‌گل ایساک!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30160" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30158">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30158" target="_blank">📅 00:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30157">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba92349391.mp4?token=U6Zz3xZdjI3RK267m8CbyR_28SytkeVwg-itaPZYt_ovzs-2mfecJ1xoEycpyVeN9U4JRHzzgf02AeQdU2AGawo0c_UF_y3EwOptWgVJqa9RyhiiMzexX-XU3vIFG7KjEv4_Uv_rH_hwFcUilUiihUQ9loD-uUpzkrJdG_V20jUHrhGOPsxlgPp1-gDZV9eHaWs8lxYt20IFeq3BDfVSj41Fg7FvQ01U9awli9NQvVo5jvaMj2e8qYo_ZQ4CA5iNL9zKYx7GaxxS9FpXQDhuPerDu1PvOgVPQyLZGMXbylJKwFIx6IthzA5vTNrHR-AI4YLFHCFNB3wtd1OjCwwVQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba92349391.mp4?token=U6Zz3xZdjI3RK267m8CbyR_28SytkeVwg-itaPZYt_ovzs-2mfecJ1xoEycpyVeN9U4JRHzzgf02AeQdU2AGawo0c_UF_y3EwOptWgVJqa9RyhiiMzexX-XU3vIFG7KjEv4_Uv_rH_hwFcUilUiihUQ9loD-uUpzkrJdG_V20jUHrhGOPsxlgPp1-gDZV9eHaWs8lxYt20IFeq3BDfVSj41Fg7FvQ01U9awli9NQvVo5jvaMj2e8qYo_ZQ4CA5iNL9zKYx7GaxxS9FpXQDhuPerDu1PvOgVPQyLZGMXbylJKwFIx6IthzA5vTNrHR-AI4YLFHCFNB3wtd1OjCwwVQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30157" target="_blank">📅 00:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30156">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUdk1L5vXFZNBfSohAC0YaZR70vaKirVdieDHbwU_C5GBrDRpt_gAaYEjO3f897uaxPRJClbJp77wi1onqkGBExHap2TZgi2vGqK5S5aCoDp7SrmWTmWZuB3pJv4pdYJ6sUkVpeV_LmWlDTbB2A0G0fCM75oivONkPL-WAB4SkzBMqISKM8Fhq23vd0zbSeo8t-QS7TQ9P9_KhAmkmxRKyrgA0lL_QpwrQaXYBiZhuqE3GZswUlEpHCyLRKxpwG0QEh6zxsyF0rDqVrBAqrp-6kR4OZqMDHhqqb6Jp4MwxgrRay5rsdsnuevvTU_uG0RXjrlSuM7_68XGIT2eQGlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇦🇷
کریستین رومرو با سران اتلتیکو مادرید برای عقد قراردادی چهار ساله با این باشگاه به توافق کامل رسید. رومرو در دوهفته‌گذشته پیشنهادات دو باشگاه آرسنال و بارسلونا رو رد کرده و گفته بود به سیمئونه قول داده بعد از جام‌جهانی‌راهی اتلتیکومادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30156" target="_blank">📅 23:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30154">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bj00u9Sj0ZHcz5i4MJ3K9ibKlev9YqlLSE1O2yLGjzodC546zMhzC7NInWFyxOHBccvTKfJIIlMB6G83r76CQLJrakfr2E4HasAbL12AjdvLVvkNZXlsfp-gGk-EHJ1rzWTkHfdLoCi5aApmggVRXHVG0QTkl7MT55_06QGdo9HAvXpIO3OwzSXjlUhMCNRLLA3N6bh_M_9GyCPjeYOIvKdJLyG2IAHSl28trNva18Vt2rCHWN4d-x2ao15c6ARviXhdcDch14fUOPyJb28x_-StuENmYUMNS6kr_UkV2pW7oMO0RCraGs3xwMtpsLZcy40pb7r6emptiAuF71Qftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIuBA31P2tVENnMR9WRBdmiibk2q1lb2ZIN19oHtOWUl2d-Yt0Ev0SXB88zT_PhapY5c2CYFTwnRQjpvdOJwQLHfrnLi4v-A1iHWisEmmGYelDvWUov9I5gJrqHoaJoCkeOloYfoUKoYujWDmiz3-Ra0B1XvNW1YajxvgscYAqJsqkMr2IAsFroZu4_e_NKNcLgMTeKrnzDEsEiQKZDSbcek5YdGb7SQBo0R3bwGG2xVq0Ne5vrhEIRdd9aN2P56toT9VFx_WZhCPCDEA8a3GNPTl8yi9pcU6bga8KibEsavEx6fD5Aqnt4Csq5qkT6VVyHzfmPEmdbzlkGjVpvKcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد رافینیا و یامال درفصل جاری همراه با عملکرد کلی رافینیا در بارسا؛ بازیکنیکه بعد از ژاوی داشتن میفروختنس فلیک احیاش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30154" target="_blank">📅 23:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30153">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dy72Z8jXsstZEgt90oZva5vQptdzOq7vaw7K-X0WdpyZ2o2-k0i-atDo1fF26b_nb0L4kZiuDyZyCLqeYvCh8lz41TBiN40Inx4lzO8EFJJNEv7TqRzNMcRHaddVgKGhEbPrWWI1WAQuhkMnYza1vgxIA3PkJ5fKf_stSgS1awPz18BY6acj56JPpPhJq3cgK9gysbXg4rAgyPilk-g_f3biQo-WObgIJVWgIFWvEvborVmObHVdMLorLdAU8_LQAIwWHP_J25vzz1WojROr6mUvS0Xan2_ISPAfk_vfo6wVcC0Hj4poCt0nEyc3LnvP4_enVcCFDNa32QNIuUpmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
مصاحبه‌‌شدیدالحن خوزه مورینیو علیه داور بازی امروز مقابل اتلتیکو مادرید که از نگاه سرمربی پرتغالی رئال‌مادریدعامل‌اصلی شکست تیمش بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30153" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30152">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDSerppMspNOY7WG-pzTicwqc33PpyLPeM7lpueKmgqcFe2wHs2BrmjOs7HYDhL-6iLy2ToCoAIzBeSHXFDD03WjHvpUAubPVbw3pr7sQKrGICWlQy21P1DqAMQlwjW1rVjAuVrY9weS7zzbZ8HGKlo7FcNlf2XtyRd2yC8EMjOsLkEFsbo0iz2xVTFuOMTMrRW7wAkDQpwXMdW2z-kfOr_fhegSsPdG2j720ei6DRCAo7dY93CEMAeqcFo1cBI0TKQailZYLLVWdrgD7PbGtcStowI3rzUn290AexHBIwmPw0PI2xMIoScpaoupuFwgUa0wEkfgOwiX5-15g3JEKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
به بهانه آغاز فصل جدید رقابتهای لیگ نخبگان آسیا
؛ نگاهی‌بندازیم‌به‌تموم‌قهرمانان و نایب قهرمانان باشگاه های ایرانی در رقابتهای لیگ قهرمانان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30152" target="_blank">📅 23:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30151">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30151" target="_blank">📅 22:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30150">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXsMMot-DGehqk3Brdn6aL4ZycrUwc3qDstxswVkfvS1HZ52WItGr_1H8MQkdKWDO3aW0Mgo6gm7g2_fuFyS6O_Z2ydTTv3oO6iL1Ihd2ezsLZESHFDBvj2kXGHk8pDDVI0NAEeY08i0pMNpjVKaH2Iis71D4SOXyt9dtjAsMI-ed4R8DjgwSVs2-OgnA7PMcHqxL7VrP9p9_3f9lBRzSswpXBqiTF93UKuD0kdhXXfdEpmDAHXx2GwI2_oL1wJB7lilKrUKPBQJQT_STaLYiG2ZBzS_efd6BXSXeBW4h-JeMjNq-GFgSCrnsI-OpB95HC2LtbcvzvIyFztVFH3IRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار رسمی باشگاه فنرباغچه: بزرگ‌ ترین آرزویم این‌است که کریس رونالدو قبل از خداحافظی از دنیای فوتبال یک فصل برای فنرباغچه بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30150" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30149">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCxaZk4rwQsCqCLrF_ZseuHuschmXggGi50IEC2o8ZmtrhvRhrcOn9aakvmk61PpjOWaVgPme51vy0Wl6WrQYhsDfBlIDELu2jB4HTUBY-52Sr3Y7mH_aBL0sE5ksdskIUFr0CPQ-pFmr2b4goCL0qPUODxch1-ZyyFjVSONQUma8uPkBulfYENcprF-gJ__0AStRDOQ_0LPvWUDr9DUSmSqKWoXCBvhJbasGVbLZFlcEpZx93beY8VG94UDxmf5fW-DiZtTC1mFWNnFgYcxWaFir9uWBGhtYose7rTvrzwoxKGsvREVPHHAkhAqfXb75c6-FQvGLn6uiR3CC4mIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فده وارده کاپیتان‌رئال‌مادرید به دلیل مصدومیت 3 هفته دور از میادین خواهدبود و احتمال داره دیدار الکلاسیکو که سه آبان برگزار میشه از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30149" target="_blank">📅 21:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30147">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚽️
⚪️
شبکه رسمی رئال مادرید به شدت از عملکرد داوری دیدار امشب با اتلتیکو مادرید شاکیه و گفته سران‌باشگاه دارن برسی میکنن که لیگ کنار بکشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30147" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30146">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgVSI9iV2ehoyJYrni7PTDjICY4Ghc7Rp0tElBhavYvGsO1sYXRBs1uMg0Ozs-IfCpK02T-l34oVe90twkDal8OGnpVr1gd9i2xZzJcFcwXacp2qR3Pagb2BvM_jWvq7jlUqjUVE1GIV3R5N2nO-4USMq9AJ2LI-xdiJBtxqbefvigPPCafZOyTjIdoWL-YANWUBUy0TytxenfxIpVTdOcezfaxO8cnJokez2P_DGWLh5Qlc3AL4E0_gTEZCNg7FUMj7htNeY0V5ItOELlWMaNUNK5E3hvVSkeN1zlfc5J7u2HPfNk2Rb8rYFiA5o3HgLG1xULtOKVDSG82iYqJn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30146" target="_blank">📅 21:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30145">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfHe2PZY7nj4cMsmhTSD7Gmcpq88Prf9MUGUC2aX_PvMLdxEVJG08EXcOeReWMYqAy6PCuBn4vXy3Vww6VqRy5SAGeho8VdG8meNbVsuENL5wfV9zQIxiGknKN5_4eAPGXrD9EdwQsPQ1aOC5C8P47SrO0szvl7Fh0_DkdSAtFoLisSeG6SIDJSyH2HnRvQobp8zIffyYvVSz8JPVlzC4GJ5vfOV2i-oUQ-pYEyhWvbWhXB3Jbos81zQ_9sxF3rDNYFPMkCLUFiyJtB4i6kivneP7XwPH0eBKoSI364rDZRI1cRGtHtoRY939bMvZAsVFZmNeYh9Yy8_8BOVrQN7nJAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfHe2PZY7nj4cMsmhTSD7Gmcpq88Prf9MUGUC2aX_PvMLdxEVJG08EXcOeReWMYqAy6PCuBn4vXy3Vww6VqRy5SAGeho8VdG8meNbVsuENL5wfV9zQIxiGknKN5_4eAPGXrD9EdwQsPQ1aOC5C8P47SrO0szvl7Fh0_DkdSAtFoLisSeG6SIDJSyH2HnRvQobp8zIffyYvVSz8JPVlzC4GJ5vfOV2i-oUQ-pYEyhWvbWhXB3Jbos81zQ_9sxF3rDNYFPMkCLUFiyJtB4i6kivneP7XwPH0eBKoSI364rDZRI1cRGtHtoRY939bMvZAsVFZmNeYh9Yy8_8BOVrQN7nJAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛ ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30145" target="_blank">📅 20:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30144">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=n5-dbit72MmO1skr41V33iIXJIxzPapCEZ_FECQryy-KL-EOKeNRjkorlvaouP3v-1G-orOWws4CqATLU46SNN259Z4-T8yq9YC9zHpMaEzaYEq8WX5qGj8_9-kcJj6ATn-vIgmfzLUechnjTElKRFmjKH6tExl3dj2PkYq5IhrfXxOD4_E9DCO_DJD1zq8SlfGZ7UGJrKgI3KAldh1LzeogQxv7PrxcawFGfzqK7fFyn7yWLMdjSl1IWYJhLYIXfhKWgoKv-RuUOaWnBkBdAcqdnWDKlZE481KBo4G11e5e4m0V7qnRAmUW9xTGvQtzNCbokr_HuyFem1n6MrkA_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=n5-dbit72MmO1skr41V33iIXJIxzPapCEZ_FECQryy-KL-EOKeNRjkorlvaouP3v-1G-orOWws4CqATLU46SNN259Z4-T8yq9YC9zHpMaEzaYEq8WX5qGj8_9-kcJj6ATn-vIgmfzLUechnjTElKRFmjKH6tExl3dj2PkYq5IhrfXxOD4_E9DCO_DJD1zq8SlfGZ7UGJrKgI3KAldh1LzeogQxv7PrxcawFGfzqK7fFyn7yWLMdjSl1IWYJhLYIXfhKWgoKv-RuUOaWnBkBdAcqdnWDKlZE481KBo4G11e5e4m0V7qnRAmUW9xTGvQtzNCbokr_HuyFem1n6MrkA_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛
ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30144" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30143">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=dgREOh5aCVjdPbfsWkuL8Ag-0f1K401KVU7cD6gjZhjasBIxvzm_c9WFO_Y8enc36-v2w9DNdoIQLQQVK8DGKUfbpowjeGPFC1WRU7d-mQXkYQFpWqK75hABreyx_ZobJI6UgrwiK5V36KjAKhjlrzJ6MdVxJL6Mhb8vYLGPfSwKVVI9KTEu03IYeYkLEs8EogIE6JLf7cqdFBhiTpvLooCbjDZEz_maSvd8YKlkvPRt4vtpEmy-5A31uf7EnvKbWI3eZ9i-F-CLkgvNeJhEJ63zZJUvtqMpM-ccpcm4PbzrANXlpd31d2SZBwPD8iETpxwQA6MS8c6TOdL7v9WIpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=dgREOh5aCVjdPbfsWkuL8Ag-0f1K401KVU7cD6gjZhjasBIxvzm_c9WFO_Y8enc36-v2w9DNdoIQLQQVK8DGKUfbpowjeGPFC1WRU7d-mQXkYQFpWqK75hABreyx_ZobJI6UgrwiK5V36KjAKhjlrzJ6MdVxJL6Mhb8vYLGPfSwKVVI9KTEu03IYeYkLEs8EogIE6JLf7cqdFBhiTpvLooCbjDZEz_maSvd8YKlkvPRt4vtpEmy-5A31uf7EnvKbWI3eZ9i-F-CLkgvNeJhEJ63zZJUvtqMpM-ccpcm4PbzrANXlpd31d2SZBwPD8iETpxwQA6MS8c6TOdL7v9WIpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30143" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30142">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNAfUKVMClgwz-NrmPurcK4Pv9NaPjqqj6GomkLhptxS47kMdNlZDuJWkwZhnz9nYVG4bAJSNuIrZLvESOrocpRwmKi5NpcDHqtJgEqv8HVCPv2mGwW4YEihiQMVW4icCKVlrCH05ypkrb7TXTMuy6I1t32ZQIJIiyRL1DrPoPltVXvd7XeHfOtsAdp8XsRYKB8U73A_yT_1FSm0-3RqCHA79EK_YaajKlxi0_7jBOPYox6DXzkyQOtzpb6dxqxdar12HLzB8minV4jibSMuUh1RmSvDbp18LIY9HsJL3tYVG05p4qVxH_WjIJ6s5c5G1otiqJY5PyQW9hz1U_WjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30142" target="_blank">📅 19:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30141">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zra0COy4NtdjDjemUCRDPOE-ppKOTYz3Wq7IpIWXubzasN-ZgET7AwGBeaJxTijDZTqGtT2L2LxpGeYqUE8pPePDMlPbxgSF3gaM4wRNS0kGuEy-NiuNx6dTscKj3akcKXalWgW4VPXco9fKkGCS8jcN21NSPrKm1VEIrWMyKnPOeOR_ZXwx_EGDn7fGimwbOahG1tRz7XrP_Wjr7NO2pF9uwuTrYOvxgj9G6TJrkFKxsOkz4gnBaBXN97Qec9N95MjpqPMnDvnM5TQi7Npit_ekc67dCiMb1nmF0kriewbrEmrZFhQa3nwE37-pN-X2CvhYdQC7Gi9VnBtPy0Y98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک ترکیب دوتیم رئال مادرید
🆚
اتلتیکو؛ ساعت 17:45 از پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30141" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30140">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jb7yOaVtm4dU8rTwTcDFQDQAugg5d2AgegFfZ0ZmWP9d9wLBkLFrAUqJ46AoIB7SJkkl_s74nu0ZsFcYJhpkUyalkAMIVWZQM9TkXCKe_nID7hxJTYPTGqxA6uYUrIlmoZgtnopTphvpcNo1crNS9Yt_ZFjhBLWmeVN5-QkL1H6FjBZBmd2kUWF8oLyUEX4X3F4DFI0ObtIBFZ7WspM67YoS8RE4pT6ONTz5nf532qhYRFf_9xbK3YR1muyIpi2-6IlKeG2zP3I3RAcKvYyWs7Yr5EUFumnQsoAopy97qEeBZy9oksi4FQebLlQurBT6lexpNy3KlCLzzi_1ZjSGFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30140" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30139">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=ptRvoMGPTqOFMlgccbnI0Tj5TPSmiteiPFn97079uSKbaAjrK5LjUMPbqU_66QbvU6BSu5grnwf9qlhtwHaWbCVU5sUBR8QsqgqEuV-KkEgMpaLrLd7AULZqIt6mTCERCjxupw7BFy9VKG34JgifWufBOcVpRHdE-k3YcOALcgR9dntE2Lxaxtw1r8fH5UlY1lbh6WFHgK_oFF9yCKSgFCP6hDSKOZpBbhJRBbOVFpKPXBsM0BEDZ-ThxUeh0gvPs0QalF5BagerkdsiYw6xV7M6DREIvSxiCvfrYt0-ghDXD_BwtbXM9G27WAZy7jObpq1W7myxk7kV-TfFQbSqHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=ptRvoMGPTqOFMlgccbnI0Tj5TPSmiteiPFn97079uSKbaAjrK5LjUMPbqU_66QbvU6BSu5grnwf9qlhtwHaWbCVU5sUBR8QsqgqEuV-KkEgMpaLrLd7AULZqIt6mTCERCjxupw7BFy9VKG34JgifWufBOcVpRHdE-k3YcOALcgR9dntE2Lxaxtw1r8fH5UlY1lbh6WFHgK_oFF9yCKSgFCP6hDSKOZpBbhJRBbOVFpKPXBsM0BEDZ-ThxUeh0gvPs0QalF5BagerkdsiYw6xV7M6DREIvSxiCvfrYt0-ghDXD_BwtbXM9G27WAZy7jObpq1W7myxk7kV-TfFQbSqHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطرات سمی امیرحسین قیاسی از مصاحبه با علیرضابیرانوند و جواد خیابانی؛ بدترین مصاحبه کل عمرم رو با علیرضا بیرانوند گلر تیم ملی داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30139" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30137">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEL4LAZXRrCjCQLbqmIYvsOZJtdasP9HzJJJNS4CNg7lIdXfiCFoK_hTl4qGs8JmunB61h66u1oKcuoolOo5Ks--GbV1rMBKko-iHeAlSoThSBf9XuNIOgR4Iojldfg189suE8QqDFcTlslzcywm8ESEjHaIdcohBEfvN7gcFkHSPQdjeoytQzLEb-L_xUMFsiUgUlW-5ghlyTv52GOH40ctd63LvAZ6T_ZnSNA1zW2Yz8o-a0NZVRLfKeaIfThnRQofla87jTbNA_erdBmSfVRRGfECBOyr-es_60UjXkfILqkCHppd2wahZjDmLRZiBqz2YlbSxPRRPCKmsaydtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30137" target="_blank">📅 19:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30136">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqwnWh6Gb37zcO6na9WV5h-f5UUQ5rzsqAHqdjfWZ-XT1pHz_MP3ZwiDTCOp4jYEFVOYN0Q_muZNTHaPh31z-j3SGQeFTEvebPsmyv4VoWA5JvHvCfa2VALYf6wHrxaOfxZSDTogXdovJS9goJmNFETp15GBjr0ZGIPpblIQrngPEk3hfry8MyqCeAk1cCUDOpJG73eu0VbfHziFpvlAxqlIksvmckgkmEiM_c9GwdJJm19hgB6JIY-ZX6qvoNaZd4xd3ftk8LpdUi9gj7g_FOUwUEsJNouEa9_iiaZhrWJ2BWz9od6cjyVO668mxO25Zf0b8tCofnU1J6ULFEAGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30136" target="_blank">📅 19:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30134">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=JVT-DnZbut2-vfbURkCkK9E5Jvi2vAH1x8_bzBgTak6FYOJJllrJGC7lf54XttY4kLk6MlQvSp_YFeeENFzpAfHlqzzb7r5ikwEj58KWV-BuCG1XHHN_V7_pBuEEoxXYqhR0xMlCdpzvtuHPxiL-FnXoQ1FFkx99Uszz-osCUj57fKvhaSTNbW50s1gq9oZ9lyhle9lr05kQqFrtiFDYKj5c5q-w1JoR0fTN68UqQqI2pFBwyCGhp3kdWfORUVMyva-4_DcezgWfRTVgKZEVoXRHfFkaoOzAnJ1fJovb0bpLlZWoGP4OKnQKsDSOAZWHHw8D4hhD1N4Hr0OQfyGhzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=JVT-DnZbut2-vfbURkCkK9E5Jvi2vAH1x8_bzBgTak6FYOJJllrJGC7lf54XttY4kLk6MlQvSp_YFeeENFzpAfHlqzzb7r5ikwEj58KWV-BuCG1XHHN_V7_pBuEEoxXYqhR0xMlCdpzvtuHPxiL-FnXoQ1FFkx99Uszz-osCUj57fKvhaSTNbW50s1gq9oZ9lyhle9lr05kQqFrtiFDYKj5c5q-w1JoR0fTN68UqQqI2pFBwyCGhp3kdWfORUVMyva-4_DcezgWfRTVgKZEVoXRHfFkaoOzAnJ1fJovb0bpLlZWoGP4OKnQKsDSOAZWHHw8D4hhD1N4Hr0OQfyGhzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌جزیره؛
پیروزی خفیف لک لک‌ ها در دیداری خارج از خانه و آتش بازی تماشایی سیتیزن ها در اتحاد با درخشش انزو فرناندز. گل‌های این دو مسابقه رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30134" target="_blank">📅 18:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30133">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsFcFEjuHl4GIxgr9jVz1zwtOT9HzoeQOpft3Td8etSxeWm7hZP0yf3VLuff5rYUnwD6IJfeGNREgyqIHov3fhxpk6yw2r0G4MGgdkEUf5kyObbdJ9ThsHcZqUoTf0zRkrRoFFqYQZuqNS3UzEmsx7nJaBJk7hD2SJXd8lYcM1KRkR10MxzN_spJQUl4T2cbODb0RTcOSDlKSmPr06h25kHotz86gvSJZ9Qa8MVBxrQtWpJXPG_POxUfXQvMMe9Wth_eVUW82xDQB-TGWbuBu0jPvw15Y27CSqMHfzRsLi-ySUMX02yK30GAq7EgZ8XFipkwEWIaIuQmvti8EKvFvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رفتاریکه‌مایکل‌اولیسه بااونیکی خبرنگاره داشت این بنده خدا هم ترسید اولیسه اومد تو میسکدزون ازش پرسید گفت اجازه میدی که بغلت کنم؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30133" target="_blank">📅 18:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30132">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXKn31iUyLiNzhjwVJQqiW20XZWIt1HvuTmzUg59DaIoLgbZJFuzSzNTJWgfyrJ46zr5eOcrBRkoxNWjBblIykBzlSdNm_HYfvODL_xzNAZyUOA8J372IDm-V2Ko9iVHa4DVH5We3JnXje-Wj5MLDTdOpJZOcfIz_hqyp7jx8Mzr-3pUxmpO0XLy3yBS6hKuhyuBv6ESgYdSoGNzTK65Wnety3qfK9sEy7h_bBdFlTB25Bsi2WIi2bEyMw7GjvGRRonwgRYryBgoO9h8awJumKtj2fQhFfp5ytBEoEKdtijlwAG6KRLcZTrVVliYjhuRsWKVicY1Cxe9i_A2-1g7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
پارتنر لامین‌یامال:همه‌شواهدنشان میدهد که یامال شایسته‌ترین‌بازیکن‌برای گرفتن توپ طلا 2026 هست. اگه عدالت برقرار باشد یامال برنده توپ طلا خواهد شد او اسپانیا رو قهرمان جام جهانی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30132" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30130">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=fGhmUrxAXeK3cEb4NsTb-br2Ckz1V3ixFlu-YPItlieNEeyOU7mHTSQYzgOukmGHtkH8TTmqgd8Mu_qbhQ0MTLcGhhvvdg3wfNEKypcpeBiKSLNito35fOG7WTmbp_n5UmV6rI_HxsXP0O1GlN4z01BDqKf_6zMAAIKneU1S6wrXaQhNA6_FESrCr35Xd7V-2T8KJbvnSI9xqdp2hJHoh2hPjeBKQBom4LjmUg91mEP2lXQjPMnRzYO9KExM3KcfgPc4erhL6MTeKpk-D_0NbgGtAwvooZ3Ct6UEpMKTZck7NOhAs4jctYx2RRxP4h1fh7TLtbKI4pqaXQ3Ytx29ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=fGhmUrxAXeK3cEb4NsTb-br2Ckz1V3ixFlu-YPItlieNEeyOU7mHTSQYzgOukmGHtkH8TTmqgd8Mu_qbhQ0MTLcGhhvvdg3wfNEKypcpeBiKSLNito35fOG7WTmbp_n5UmV6rI_HxsXP0O1GlN4z01BDqKf_6zMAAIKneU1S6wrXaQhNA6_FESrCr35Xd7V-2T8KJbvnSI9xqdp2hJHoh2hPjeBKQBom4LjmUg91mEP2lXQjPMnRzYO9KExM3KcfgPc4erhL6MTeKpk-D_0NbgGtAwvooZ3Ct6UEpMKTZck7NOhAs4jctYx2RRxP4h1fh7TLtbKI4pqaXQ3Ytx29ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ از مصاحبه‌ تاریخی‌وفوق‌العاده گزارش گر صداوسیما با یه‌کشاورز؛ خیلی خوبه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30130" target="_blank">📅 17:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30129">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=HZ8gnCkMtMZF2-ifMkJ9ub3yv4wESjWLPgROBWjunDbJE3m0xxPKruJ-jmLWiDl3w75nHaZEzKHw0_IWyxd0MeHKQvA4lo8mmsUHUiwRoZVLk616xP4pBzxmhwcewvLUj-N1edia86Mb4wuvYlVw4hSJcWGt30b58PYD-P75y0imEtYubCDGSsJcBjwkmJI5r4BR90Zak8HUL_jLHTjkSRXfSSFWQ7BgU2d_wxlP_ea1r_4BiSBUEUDdzGrIcns5OcqDKl5ngxHioG-klWliGJevhdGY2K81T8vNtsjlUM_iYVFXg4Zh5ylhzjHD4wAi7WrrhifM0mzM_b1aYJO9Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=HZ8gnCkMtMZF2-ifMkJ9ub3yv4wESjWLPgROBWjunDbJE3m0xxPKruJ-jmLWiDl3w75nHaZEzKHw0_IWyxd0MeHKQvA4lo8mmsUHUiwRoZVLk616xP4pBzxmhwcewvLUj-N1edia86Mb4wuvYlVw4hSJcWGt30b58PYD-P75y0imEtYubCDGSsJcBjwkmJI5r4BR90Zak8HUL_jLHTjkSRXfSSFWQ7BgU2d_wxlP_ea1r_4BiSBUEUDdzGrIcns5OcqDKl5ngxHioG-klWliGJevhdGY2K81T8vNtsjlUM_iYVFXg4Zh5ylhzjHD4wAi7WrrhifM0mzM_b1aYJO9Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه مهم مهدوی‌کیا اسطوره فوتبال ایران به والدین درباره زبان‌انگلیسی؛ حسرتی که مسیم دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30129" target="_blank">📅 16:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30127">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8xV_2g2kV19NZOBk3Y9w-qXpajAx4o9W4dW4gb1i7qnb2gxO_KqKzOB4pTdAIvtCIlv6TJFpHGcOWnw714r8dEWU8JeoNqF8xXIPeG-Mp1WcVfKvDLlcXUkn9mA5IfHZq0r9zLBYwW7_2Ef2JSYSE6z1alo4zYGfxIGETMG8bL9ybR2JHNBjYg_whQe2w990gm43OFZdZmh80m7EwqwVpXX3fMcZM5Q2k472xNdw0eEwDlhF4AW51wIQjqAUH0Ops35NUpW6vR8NxxtRZnXZwF_h30jFDJKAQUEWeegSv4BDZTZjI4wrW2glAUS5pLGeo1zBBm_jPRo-RXAQjKRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsIBT9s6pfIZE17JGfyKMN8RpI8XkBDYiLT0yGEAZ2FlMnD2DMUslSQOQPfA2knMVw2eKp1dqm9KDaNvrIL3SIOk44NWySiD4GNMsy0xCwoDu2XTQxMdCrDmzSqfUMIBZEhu7ct5fv4p-N0ee9NYpFk8TAa9MBHf9gZQX_H4vW_b2wntcXw2QM2RIt0lOOe-4A5mZUya8ThodStPJe18LKflDcfaKp9lGXR3qt2csA1AD1R_GLxJ-1v2W7-uvh_Ui1BdK-MQXW3sCj7D0oydmpLjTHTlNnKGAAJ9kw_IdCaFUCXNC8c8H7dojdRdQ_hgcGp8R-SneaDFqeBou2srTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30127" target="_blank">📅 16:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30126">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6_FpapALdvVM4ghWOtmwK_gSLqZbnB59WWHcVQXly7Tbp8w9KflokRN29nKRHmNpchLw3-PXrGSiQ6OpExTMP-1GVUUC0IcIcm9QGjchdR5bB4us3zleI4ytoNIXYrrysphyMixpjd2g843g5OTDUsqxiPUlQ66DeKo-eyAFx9pvmHll1VGzgV4vXY4099vTrz_vQ9FOYM43Bp-R1j2tTXqo0nn6djFf7IjRagpHPf9JvYuKoSMnmomYJLy3KIqQgszaZj-oGxDSxsWnfXi6Jt5nh1gfL8J9MSBxy4kQ-U6lU3sBLiezCS8FSRBrF0Fp2mapPUWXEPLAvNfx0Vbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30126" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30125">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTJ5sBfvalcmj9_safd0IEP8ugMRNhZ-dSYHGncmJPUDzahD58_wjBNkFGa0nZ7Ib4RCHb-iL5-1v-60EOuXLXbP1WoxdLuOvDqPf59BS-JABDooaDc0UhcFD3X702dDjG1cWAY7dfI0U-1ps_dTcbhMzYk22_rkOcRxReYrlIYCDtTwOaXPFPT4FCl-1l20Ziw1RX_f71hrjqqnIIvVumXUVdg523tCIUHOMbkXy_JbLW6jO5k3QRE8xzPuE0GaY6Ki6LF1BtcSN00-TFNqiZW33Fey_-IetFerWRwzdcjcpdy-O--lZTjMtvwCQe5Xl4Q1UQnvPfguA_Oe12LYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛
کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30125" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30124">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJhv3DXz2gZlndqaJgHhgUn4q4aSwduyjJeVnSnt0OEdASgzULKSluOatgMhQcTMGG4R9if8OtXnbCtGw5u0Qc-sgWPGAu4n6eZyTng6yuzimQl3kotKmThms1cF7SyYrrIJe7KcgmHDueS_5kUj8MgUzsPe1-InINFnNQ-fRTzLAqfIoLwzGSFDP3VmW9S6AHtwll-fcmfEGgY2XWaQWGT7kQwT2fLQaJ-aylMveRShse9aqNURZ5MDB8BhDnfR37a20-8Cupx8jNI0u44fNvB1Z8dfV_GGOdBvivUxsUqFsJCs42Mxa_rTlsjt9GP6wneSLUtCRXOQ5OaiPI-ZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30124" target="_blank">📅 15:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30123">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZOxsX6wuEL0g3J7tsJxJX6iNA3EZPMUzIEstOvGNdx5mruyPiloTLkkhnTCMYzhgaHdidbc-dztcQU-fa4COaOem3X-IC5mOm5WS9TxX_xQKkFp9fyJ3OlgHBoo1D1OcOpn0FOoGxH4iXC6VNPtpqv0GwvXWTr3EgPNUeam0DU2N1bdPdnuG_ndCw8RgrEMiQ5Hro5rJqT8xTz7z-Us2XuOZ1TuDFZVWHny7g5cb09r275R-V2GqB6bvvYEVdMArQOBfk0pLlJkSJ0pJpcPYaXeeefUH24sznLJ3h2zaZkOowemB663ErZpeepN3lZFwmxyEV0hU2ZcXkd7P3dRNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مقایسه عملکرد رابرت لواندوفسکی و هری کین در 150 مسابقه اول با پیراهن باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30123" target="_blank">📅 14:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30122">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09969a195.mp4?token=R6uf7q3l7K6XxnvMOJ0yVA2T_-f54zP7Nc38kMDve7dE4cjnQME4RhRyuOIYsvvMRGMsVAkRQR8k2NLvHp6dq6hbl0nbztlNL00Wpr0RD47z7YssEYnr5x9TWXBqzlqZHpZdUg8CEGwLexXb3s-IcQlFEBiXImkTHGwRit38HfJH1F5fANYa4nu5B-dwqyzhIUcuIHM3KgfjJrxW_WIBvAd5kty-XBjoHKL0PVGpg4YzqXnFbWA4ySJ71QAv03_j3nPVzOepuFhOpCe2xOjaNf-uzoBYHfda9zbPTsah9f5PM9fLjrgms5BH9hkG8gVt5tIiqUR6Bc5J0T0PHX6NTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09969a195.mp4?token=R6uf7q3l7K6XxnvMOJ0yVA2T_-f54zP7Nc38kMDve7dE4cjnQME4RhRyuOIYsvvMRGMsVAkRQR8k2NLvHp6dq6hbl0nbztlNL00Wpr0RD47z7YssEYnr5x9TWXBqzlqZHpZdUg8CEGwLexXb3s-IcQlFEBiXImkTHGwRit38HfJH1F5fANYa4nu5B-dwqyzhIUcuIHM3KgfjJrxW_WIBvAd5kty-XBjoHKL0PVGpg4YzqXnFbWA4ySJ71QAv03_j3nPVzOepuFhOpCe2xOjaNf-uzoBYHfda9zbPTsah9f5PM9fLjrgms5BH9hkG8gVt5tIiqUR6Bc5J0T0PHX6NTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب‌ و شنیدنی این نابغه هفت ساله اهل شهر تبریز: در آینده میخوام پروفسور بشوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30122" target="_blank">📅 14:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30121">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIfB2GYqJHl_of2twxUc-mPb0n1Py0iPCQBmDPph10pAS4TbRqzEGNkc13h5W3Da2KER7Ht-Ch5cJcyy_HWjTTpPMVrT0yUojKlSDxc__UHqLGJrAcYpwKHapcVGmALHXjYVzEMhXV9beTDkPRx6SJqnXJtBtgF3VluYOljcdnr54X1HVPQ5SE3VpRYUiG6JfyHpIry4-MOFCYFqkDMQAAHpRuRV4LfVwtlOiMke6mclDMmZqUUdtpFXy57e3qmImQZz9Z3oMl4ZKZ6MIBInb9jEfmW4NK9lwNYtWo7OjVgXZkW9SPdo3I69iyVfvTMbudkdR_XiT3oN8rCeLHpqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق اخبار پرشیانا؛ به احتمال زیاد سعید دقیقی سرمربی‌جدید نساجی میشه‌. فرهاد مجیدی که مجوز فعالیتش درلیگ صادرشده دیشب ضمن تشکر از مالک نساجی به آفر این باشگاه پاسخ منفی داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30121" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30120">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxOXQv5qUissegjOg6GqwqJ6SQ--Xznq0MjQ4L3zDBTYL2RDMVhHxjTVueyHswXMz7WspeNmljB874clVKaJf_UToTT8PCnXOE8BlvkcK3yz-Qd-CcV5aFRx5gJnrFSAkGINygqWP6vdKUL8H31jFP92fjuUTYWhhN_R9VjAF947y2yOddPBF0ZP_UbSjlnU1jNqF957DkJOfbdSTa7rbO46o7a9trq4_F-MxmeFNyTjFchDIOTEmp2w9F34XXgGn_OZkXCvwPk6Oi3TfLWmQphxqq2s-s1Oye5go5crF5_-lYCF6yb9iKiFG9LEBBAVB3cqH0-ltVu7MYCtphacpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها:
رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس رو گذاشته بود. تعداد فالور های اون فن پیجش هم خیلی زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30120" target="_blank">📅 13:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30119">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=WDg7H5BpmBr5IwqGvtOALY8DYRpQCBh1ugSFVXtby7-qAmZznfmk53sPUqEH8EoHNl7LG3K3pqQi-d0bjgql9fRoMaeTdAiFs_hqjr2Bn7ahJ1gq2b2rpERNQZoDJW9ownQuHYaRaaTDIVLTxrmB7n9yLKTDM6vM_03eNXxyFiTwV12oazV8L7ThOcPSWDHdd2gIRYYGmxh259pCTbc9NmQXrEy4dABw7yUHBaNg1sFX6VKfxt1fKbilDev1DqH5AOaByqBVsAtbGI-ciAuZkrmJZU0qxHz20k6gZlCNTRvlKDPJ2RPpdyS9PKKcYdsJQWQjKiYCPpC97OaL41M0Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=WDg7H5BpmBr5IwqGvtOALY8DYRpQCBh1ugSFVXtby7-qAmZznfmk53sPUqEH8EoHNl7LG3K3pqQi-d0bjgql9fRoMaeTdAiFs_hqjr2Bn7ahJ1gq2b2rpERNQZoDJW9ownQuHYaRaaTDIVLTxrmB7n9yLKTDM6vM_03eNXxyFiTwV12oazV8L7ThOcPSWDHdd2gIRYYGmxh259pCTbc9NmQXrEy4dABw7yUHBaNg1sFX6VKfxt1fKbilDev1DqH5AOaByqBVsAtbGI-ciAuZkrmJZU0qxHz20k6gZlCNTRvlKDPJ2RPpdyS9PKKcYdsJQWQjKiYCPpC97OaL41M0Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#تقویم
؛ 20 سال‌پیش درچنین روزی؛
ژابی آلونسو ستاره اسپانیایی لیورپول این سوپر گل فوق العاده تماشایی رو درلیگ‌برتر انگلیس به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30119" target="_blank">📅 13:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30118">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCqQQuWVjxEoEadElfG7TQTDrD7DG8M1QjTfcG5Kl7dIp6YgVUiqeFbipY986ooJzpay5BavbxXqPW3hJZQEsY1HcXT7RONb12Gpk-vP2p5EZnKNyfGbDl0-BC6_w8iI7pjcepzJTsNuwNadwt5DqL6AHgJ7FPu_Q8mYiXoV8LOAhigF8IXt0l60NbFGP2P16oK2UgjJAVUxZ7N4r7-OoxvLaalpesbWmDjrq9RjturwmoVD6RdFjmXo2Q9710mqxaPPDRJYX0iuZLVzRWje89Pj_DIAw-zOXFrjWCx_n7dG51CB0frRLlEsqJCW8bmmsKl82ZjeSJftH2-7aNLp6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30118" target="_blank">📅 13:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30117">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCZo80Lh0sZpLiAp8EPn6XI_oSWCaTSgCBVyuxe2FoE8jreEcPHLEZzwjHoB69OIeIyABbOHIAJVI7WCdgXC-kusebp8QL67YdORMluPxLe_VDr_RotmB7c4ru9lSX9Km7B7-VTwYZpr1vwHSeDLhvuQF_JaiYGW2c4GWH_ogPAn8zkjpnnI7PdsluAZQnhfYWEig-3OjLZjjxNFb2UgD-skm7jFcVySvTHthA3HcY___9JvIv2kVpQnvmlNV1qMG5dOkNtiRaYFQhRlRSoOLj34kWpCYPhbqQFB2P9jWELM1C0yWKM9ygEOddR0C0pW1kebR0L0g1RgEHD0QUVKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم رئال مادرید و اتلتیکو در تمام رقابت‌ها به مناسبت بازی حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30117" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30116">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwkFSujVdUR4WyByTb5gXYopH188GnzQrVKuX6z3d_Rxuiyc084wouz5GiNo7rcM_FbOWErGwJUIkbAKmMXlN8urZytxg0rU8w5VngqlIqGDudiMkfxl7FOEk7uEmhrxFnycz93B5lBkh1bdxSlNifC6aXfwor9iZj4ha3EA6ekRKabcpr8xRFnG_AxqVxchw5spSlgot94KINdhvh__qENMuXTO8eqrVd7A3C8dna9L2yP4M95YpYBIjElboRAYHySkC5jlaDa_9Jf5C14enTtKDkimBLlgt5sPINqGlsGX6cASS-B3KII3sBKQS3qS_dKX-t-XuaovQXVay7Wqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عباس کهریزی وینگر20ساله آلومینیوم یکی دیگر از ستاره‌های‌جوان لیگ برتره که مدیربرنامه هاش درتلاش که در نیم فصل او رو به یکی از دو تیم استقلال یا پرسپولیس ببره. شانس سرخ‌ها برای‌جذب این‌ستاره 20 ساله کرمانشاهی در حال حاضر بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30116" target="_blank">📅 12:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30115">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnsUKm2POFxo3myjsAH3hJXj0MAxBEURgIeB4U9D2ZtEwAK-xuB6r7pHlLmDbiRbnMVtajxm7f_TMdJbTCVAr6sNhLacMlW1BsD6kCUuO9RXolda2Md1OoVsPwbGIc29w7f8AllFOsDclotTd58dHwU3Zvsbsokqo5usU2FhMMNUnPr87CUR0KSBG-efUglJPdPG4F6hxt_HG6qRtxIpBlGb22hs3omRchIWqyv8_FvTrhJoul1OAlcH_9baFi3nc1VdvdYaR9Qu06pR2ievQNofXPAd_0Sw0yIbJPvKRRMbx1VoaMSCtbPTozHqNt9IKi60-HkDrd9tV0GhYBYILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇿
لیست‌تیم‌ملی‌ازبکستان برای بازی دوستانه با ایران بدون حضور ستارگان استقلال و پرسپولیس! این‌مسابقه‌دوستانه روز دوم مهر ماه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30115" target="_blank">📅 12:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30114">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30114" target="_blank">📅 12:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30113">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyAZJeiDFtNB2VWyAEfjFUGWNrYZEE9KgLvXcFTZ39alukQ5j2DbF2K66V_0C_HU7g68BX3E-vH_3vI4SF8nO1Tn7UBIVORMG51y0Iz_pW_JDWTG0k3KjY6qsX5TooI2Mpk-R8OiQDgn_xC2DX-ms-t3J-mwhX_xMt40HbZ39K3sAnIuEx9oCPtAAUyCb9f57iAcHtve-ZVY78BWVGtVKs5gIki_DZtTJM3w7qvb-jDCXXIpMejJI8tx50JNc7LnBkEjqAITak2Zy893b4HFNHU7NIj9tY21Lcri1rM26T7jRUk7rMGvxqhefCQWUcVN1vjaWWJevAPSwKGnEAWWqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال اواسط هفته آینده بامدیریت‌تیم فجرسپاسی جلسه‌ای مهم برگزار خواهدکرد و با پرداخت 50 میلیارد تومان رضایت‌نامه یادگار رستمی وینگر 22 ساله این تیم رو خواهد گرفت و رستمی آذر به جمع آبی ها میپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30113" target="_blank">📅 11:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30112">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBzJmyU9JHlpx6arDOepfCFNHJW3lpJLWhxTLMz33ZPnMtlUoFsMWf7c6o05a3IhszRTYUnSF1Ee7AAzp565eqqzEIti8DuZanH55ZsLIVWMFPr4hE6vxJjuRHk5Qm4Bdv4IsZIWBFFW6o49mbLgEZmMNDHBTpxNPX2I-q9rGN0FO7suNV1bao3QKDT9H4_OmwwjLHk35PQRNiI1ELHbBtSi0NDs10RARwMrIfWxwj4iQrO7M0bxgB-DIUYu6jKt7DYzFuHbrwMCCu79MDV7P8AdWYVspq_FdZEbDrCWJs1ZZjui86cQH7r0XdZFAT853Fh4Smn6uQ95powr3j608g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز تنها در یکقدمی رسیدن به رکورد رونالدینیو درجمع‌آبی‌اناری‌ها؛ از رونالدینیو تا رافینیا؛ ۲۰ سال بعد یک برزیلی دیگر در بارسلونا می‌درخشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30112" target="_blank">📅 11:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30111">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bxc9RIU6RW5vPwMo0tBEcZ9vWo1sUG1QtRHvkLTUF6SwkBLlIwhgkhgHwVyH2rZqRUuK9Ehql-8DqizhJbPTDvN9ASDz4N2vZf9vlCYELkQx2tEkg_O_Qd1eAQeFjRn0ack7gJGW9wcB0QUrRjdHPHjWbC9QYkjzy4fXK6igsz8FVXFUGPg09M0VtdZjcdq0VS7Rr3MZJS0g684OqXawQuQ3JcvXd5rNY9qSgW4MBYfCpomfl9qjNZJlrajl36-YYXuA8VI82yeQMfEuC65FP52IcSGM2lruUkAY0p3UQc5Kul9GF2vul3Mq9tw1KamSLRRzJLSaxMzpQItPoDVyGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌آپدیت‌شده‌سرمربیان‌لیگ؛ مجتبی حسینی اولین سرمربی جداشده درفصل جدید لیگ؛ سرمربی بعدی نساجی‌به‌احتمال‌زیاد سعید دقیقی خواهد بود. فرهاد مجیدی آفر مالک نساجی رو رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30111" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30110">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3eLLhg7vDimtjrbXrJ_LW5_C6OjvjqaXdACJ3TK76u-jueCesXklhER8zkrwUaoKGlfW58r9clbtP1k0wQOPttRnawF2E-kJgoNCp5H_aY8xWyqaAmcjo6nrCiJKooSZtNnCwYWgkXyGzpIrS5EaXMd4-8mKRe-VGHig0vpVV28ayGGDsPUUH-Io36U9Mq4E9WMPlZrYWzf0vsw5HrZRdNKcdkY9jVXqiFB42cVxmoVJQsdTVwdF4LM7GEi1kKOH_ODoKr6QSvp6drBrSZR5PrUCt4TNyC9TBzEhllmWEN6oqnoHDQUqtqjJXGY3lfk6OaxzfpBY0ln2xhUFXHZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تیم منتخب هفته اول لیگ نخبگان آسیا در غیاب ایرانی‌ها با وجود درخشش ستاره‌های استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30110" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30109">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-Gc9RV-4lpKUmESvIv_NcsbgEdnVWte3cBY8026auL5hTT6q4TCVAFGK-30bHrqzxSe00siCPTUGUV0aPIL5OU1nJOc-4p3loW0I2u-hMXst9TITtakHb-hZwu-kUXhYgJiRzgi0hN_c-hja9vAZDVZXq5rbUrzARDrwQ2cmEHT5mojnq6oYgIIh0LIRbhR4AKx9abYXVlXJx_5Q8j2337LK0Zp-LjHMiIgJcJC_ifUzgUb7veg0PGEeSO8zQmlVite0bzDuxC9ahQ686HnmSUhoYBlAy_JKP6zucV7xmeh6YtrqEB6_nFStJlpI_aTyI8xpg4ORrGHazNr90aUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
⚽️
لیگ فرانسه
⏰
شروع بازی ساعت22:15
⚽️
مارسی
⚽️
🆚
🗼
پارسن ژرمن
⚽️
💯
اولین واریز، اولین برد بزرگ
شروعی هیجان‌انگیز با
🤩
🤩
🤩
🤩
هدیه خوش‌ آمدگویی ورزشی تا سقف 250 میلیون ریال
🖥
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با روش های ارزی و دلاری
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
با هر واریزی
🤩
🤩
🤩
هدیه ورزشی شرط‌بندی میکس دریافت کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r29
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/30109" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30108">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30108" target="_blank">📅 10:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30107">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqziE3Jyq53SYwqM5A90QyGJJ_ssDSgPQOYt6CNaY6MIgL4N3LGZ-oNrNY2tyjpXwNZiowuoitwU_rpdVAj6oZZV_kW3vWfQRA7CXebDUXO9EZFmTkpc5QMLPUJwKyxybxQqhLIdcsTuD8TLNSdF3U0GF_tPECOwj26qhgy2yw4CQ7Zn3I9l1jMI1sJLB1hT-8GITCv_PXqhpNIh0kEnj-qmLzNz07QIVw0NhqtHShRpjEtBrcaSrV2HySCHr-cwVX3erXNMMyNyyUHkUwx2p4FXWghf8TH5H-mc_T2OZ7U7BGM6R6Nr0uIKLAhVG72ToIwBz8MHO1AIDiR5Uhjdnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شرکت EA پیش‌بینی جدید خود را برای جام جهانی منتشر کرده و بر این باوره که اسپانیا جام را به خانه میبرد‌. این شرکتم تاکنون دقت 100% داشته‌. ببینیم کدومشون درست درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30107" target="_blank">📅 10:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30106">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqWPY8ovfMDcxPe_371Qhm4tJ0kxeQaT3xLbF5x0ItpzfBjU0eyJGjYarl1_YL87HGRc3h36f3xXiEh34W2i0BYqcb6jCEe_y1tH45PYSzP2s8CyP-ZGlICnTTVlwJH8kNhfiwCwexJIe253BJgxKD8Q0-Mbham9pljX8Ehry2ky4svHjA7m4U8endNjcNS8psUTw_Q8HD-gtFziGMmoF2f-Y78ZVs6-v9VRkFBQ1azUBF_HlvbGlbSD1I0y76jMct4zSkHD7ruXoO4edO1mZpy0xbhd4aOWuQLlSkl_QUvKU-vK3yKGOhYjdSGfZvCM6hKc1c-phu_AGoDZqwh95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت فولبک‌راست‌بارساکه‌دیروز به لوانته گل زد شروعی خیره کننده در این فصل را ثبت کرده. هزینه صفر و خودکفایی از سوی لاماسیا عاملی‌ست که شرایط اقتصادی بارسا را در سه سال اخیر بهبود داده است.  قرارداد بازیکن تا ۲۰۲۸؛ دستمزد بازیکن، هفتگی ۶ هزار یورو؛…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30106" target="_blank">📅 10:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30105">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gi5iJz6pbwjaR-GFgLBqbEDMjOgtCzLwq49sN_V6y12b2lcbHDMxNfNClWRn1lsffWoVvdzHBzwG3KBrkgU8tuBrl4Ak9dg31ZfSATWuk86EdVzne3G_UHrMe5piNz5LpICHHjb1jMFB4X2f7u16aZ9QX6pPPZRANJEjSVACV0ZqcHxNqabAJ4653qR3unXWBdbKzcHfjghDqL1HbD-KRFEpPhbkY_5ftB5mxFhWlv5QRN7zCWSXkByyTsNuTcBO7q4K4KQyluIu-C0wKjBeBEY_DOfo-Uua-j8KWgHjwy0isA3Nn5w7E61-hd03ei-Z9jpvXnti6lbHRuJl8Zfj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمد مهدی زارع مدافع میانی تیم پرسپولیس که‌هشت روزپیش پاش هشت بخیه خورد از اواخرهفته‌آینده به تمرینات سرخپوشان باز خواهد گشت و مشکلی برای همراهی تیم تارتار در بازی روز جمعه 17 مهر ماه با صنعت نفت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30105" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30104">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-WvSiFLB5kdigjrbHTSIWow7Yfm0L-nlfOzCrP0MRplqRLzRnyx2ocg1ObGndsOk4Azgg6C-8jO7OaxDMCOgwfit0zH05Po_fPku3RdiMt_-Xd0bANB0SW2c57RzHX43AO2HF84hMKlPFAEnAgIx9LdQp_K3LedRYVAe8MCunilhnX8vHnHm_QPLLGxCG1-L2wHKKTt33pjo25FfcvuJKPC5vIisTUhXKp7Ot-QAPLBrDY2exaR27UL41ZS2mAU5m0XXIRW8l92bA1SdYvPp8cFZXAfZUnxCv9BzB8hU1b5mL_6WGc6m3q5K96BlA1jyj_d6np91QmfFySmoVzBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30104" target="_blank">📅 01:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30102">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH8DeG9RZnfo1FXPQVqUMWSctjC91KXFGIZ3wH3RautgHjgs4KKv749BJp9TrPack2yN7zI0XTX8JEl7kbQhUihtDO3l9w3YUbP9LuDCnu36gnrpBsB9-eJjlhzin71N-OYQ4dKJyXAUd-KYjGPAfZa4LpUeatUz5fDVTxCRnoAt5NoVkBO1Z4QIh9cAf_759gHIhuOORMlpKSELDzQW-sBMMcawWM6ZkPkpI1Ia2TzHqbP6nurHL-00gEeRgPKfzxqmQTnkIKHO1ecaL701J5HLiGk4QydhBlX7xVI8coFGyLUhW3wusr5qkoKVulXWXF41Yu6Gv8IMxgVHRWTKog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30102" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30101">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFgEWKG5z5PoF-_sLuPtgZEVilNDjyyg9Yv6LHDkp7dUnHA5bfy3MM-YhI_FTw4N1uj_anpo5RkeJe_x3rvEqdOQUe-GZZ9MFTG75WKRlIvG0IGGx4dMvYcNP0nTlbvJzeTvoWTQYpx2XMcdzmKcHemikFUogcLpbehjAy5Ev13kJHey1y5k1PyJnFQbZvxE-DNwG975ronD7kQbAT2aoTB1xp9Of98EICBlQ8cE0nrIdKAi8fCc_j4_kvxM1OMsgim6FujXQHoln64QdXuerx9yA-aL_1b4QTCTK-oCzlX7T2SJgTtk5zgNiqs_hS3lbyIj49AAhZowlLXNaf75Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد بارسایی‌ها با هتریک رافینیا تا تساوی در دوئل آماده‌ترین تیم‌های سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30101" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30099">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qq4BZw416Tx1HDKiI4tlDa-PvT_kU32OoEfi8I-mRihUbYlxXzXJuOpHVGnwNKRlDERaVjOLM8AGlCiS_RrvVS_NLbavjJ4qUpnUqoqJekuHdCWXw2nD6u_0DkFoBCUmt-OgNSteSMhVaTWW1XFfhEt_fW7WGS8qrYOTuez33tTQqhoWmZM2825qZdesqYkoZ61QDLbmHSTVQtlxHrKdXrSumWu-wXU5BuQotVmbTd689zJPk5lzoeW_Wz4qZkqhZ_htRSmMkWU7Z9Jn5bCGpDdiliA9YB4eihDkYv-Lhr5NA17KUdS6cdgnPsFc2ZlliN6Ap7Ajhy6hsJg46t5m6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTVgbdXqrIq3YsdDy1Axidg8beiGv-eEB-4oiTGkqO3N9yYu5Q5dPjpj1NlRPzfqpvtciaMTKXAHnEspOcp_Gv3ncz-wrtu-2czdSNrQs9FpEF802lSfnTEg0tmyiSHtDR57hNqETMLBAuBbM3dAEyAFkilGQSTcH3UMVgmXpIzXZ0xziAXs5tImGZ6A7xJTmyDsj-CTJYV1Fxe_nLEiQJ9Ge1BrsRcZ8pmH6pcvEhD3GvfHF5owMLWCy5CsENqIbTgYuS9sDmODU_yQz65-TrSAKo3LWY7XqKdPKxWimLwsZpALKuYbz73gDi3sTerLo_PHXu0fajfmgtGlca-oRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30099" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30098">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFmI2FLrmZIKL0pMHF7Jhs329OUL5gemaTVrJCWakvr_Ugw0cR4ZXW8zbPWpwp2j1PwZBx2XB_NVZCol0WxRaV3DK4zWxsjsLBki3rurLovgc-Eaz7nI25ajKyQdG8jQ08OO0DUffs7WSWj43r-iaMAdviAAIKyp0yXvRKcn0JJBI27nUueBcRgwEn2BXfBBPzDnunXmbKjiT4G2-WKAoUFtWElR1GADeGoKy7Ne_D4KXoavRmdMnv-rY3UBbn1E_nE914db94cokFGLWylcffyVEsRnbpD42ymEs2g1TgpCjdPJZg3nYzB0j4bKPIJrk5e8UzQS0kts4I2rqEvjvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30098" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30096">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifO1wYvMIDuTEW84y1K-V7Ipu1GtBbYT7xMlh2E59Zwoxfuw4F8mhptcbqcyKKlT2Kxt7-5iQSc-BoOBFDP7-X7p4eqgFi2xWoN0j7Pv4-VymbLqcbD8JW4aoqRoaomyvnyjBPx2oW_S2t3sW7PxmH90MYw1lBPuxtmXctjQM1vosixOsDt9QDReMVhGdGfXwvXHBILiAUVQEifRSPC2Zc5A5Ll30S5A8KbEP8v68dYdwuN-u3B4Zkt4-P_ZqSQWKSMIWyOmRB2kDQXMXHj3wP7bqDxgOAdlWxff0KpnSYpU4ux4OuDPYM_cAa50V-kqCVtf3bX4R6sTzcbuVxIMNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30096" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30095">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9hInkzINjrEnYbPsJ03pOaqCNgetypB729yVOfUQUDdfJPzPtzMt8XItLru3Cz_nst17GOBIj6HE6g3irWvshUHlQoQrcMRsZgn0-V33Kw9tBw8oMx4AsJi9ogAcDUeV-oXb-WDdO8biQ22aBUtl3bE2JlIR7E_hOBBW8HQ-bdxcwosaGHP95gMa0arE_D8LHTBaa2IUkN9mkWM7ugaE8Es5S44nuNuwEOkZA1dp8YYNH2k7dgwSikHTT3EIciAg2Y8UqoEkZ_psaxZr3yDOJXBPsioyXq_CuGKT5dBeUF-9as-Kb4tQ2EDUsCtw77j_kSWOjp-Ro0bYAjTJyYBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده خدایی تو سایت پلی مارکت ۶۴ هزار دلار بی زبون روی پیروزنشدن بارسلونا مقابل سویا شرط بسته. اگه‌این‌اتفاق بیوفته ۳۰۲ هزار دلار برنده میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30095" target="_blank">📅 00:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30093">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klYZ65L9l822A8qa-kbEyYI-Vula9geDdvB3hB88Hv5L8k7cLCi2GjQCJ8REiTonHIrK8yFY-H5eL4bb4Yno8L1t_eYoJOx4zMe1BNQ9E8SXEDbhAHM0kYM13Jh3dvttQGjDSyfzx-khPkCrBFjCpoLe1tYaeYVpPs9O-qPoXh23KsrhFswhcsbKgjL_5hrS05WzLfiN5E_gbhDHuPnomBS9zvf3Nk-iVKdnfJDcZ28QKJNYg8LIYYQtIea75g7Y89RdwHl66YexWf7eI1Xn0UknYdPInESwI0oi7kL-91MqExYzCN8H4eAQq3ggMjMTq1l-1SwBw1RtHQKzE3LD3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
گلزنی دنیس درگاهی دربازی‌امشب استاندارد لیژ مقابل  سرکل‌بروخه درسوپرلیگ بلژیک؛ قلعه نویی تو جام جهانی 2026 میخ کوبش کرده بود رو نیمکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30093" target="_blank">📅 00:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30092">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnVE3uGKIXWcPUsuxi05e5IwTwl0Uk9oIe2MpkZVpKnRI_eBUq4Om2t4YE8zcHRxeZoceVAogr8AZnyYRmePs8x17IUDAcDeXNzpoDjSY83Kf8qd1yvqnwFmM1MXiQjwiudXXsBVHNWjS0jzusUuS7zLXqXZxuQ_T5vIc9WQWsyqcgiEiWJwDCUXVzpbyDaMpzUdt9etpKkx820kfxTXzwWpItAfHU3E_QtIIxaPBpbPhZZOAhSM4Rpp0N6DEzSGmqpR2mGUGfaHN6hxXVVSOd84-uVtgRvG7Ps_PeOI3koJw3LOJZwU3SzMoBrmbw_-biYH6veYizw9L5AUCg7cpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یگانه اکبری و آیتک سلامت دو خرید جدید باشگاه استقلال برای تیم والیبال آبی‌ها هستند.  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30092" target="_blank">📅 23:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30091">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRpllZ4ChsPw_lQGf7KbRU4lW4vXTxAdvsoQiiolQlJxVTrMJauPxtfNPmfSKhr_V0J_ATfZj7R0nrIFEF9Xb0MJZPX5iCBgm8fiRODvNveo0ulGvKS7NQOT5yi82kcVU6OvF3s9WJGDC40qgsu5-FvbhU01AlzOYV6Lyffb3xLpd0tY2Cp8BXcdLV81GpxLaIj9opBXkoNzXmixd8_52T_f-M9lABHdVxYZmY2f5bgurUNGp5V5ynSkbQum60VdS-d3Wrx47ZT52B2Ng9ARoQ0s5UixFs5fet2M8pTiZ7e8lib2sURo6Z4uOjtab7TsxIcPGnGvQ-9wSGiH-YI3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه مسابقه فوق العاده حساس در انتظار فوتبال دوستان همراه بامراسم داغ و جذاب فرانس فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30091" target="_blank">📅 23:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30090">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇹🇷
🇪🇬
درشب پیروزی پر گل تیم تزابزون اسپور در سوپرلیگ‌ترکیه؛ محمد صلاح ستاره 34 ساله مصری این باشگاه باثبت یک‌گل و یک پاس گل و نمره فوق العاده 8.7 ازسایت فوتموب‌بهترین‌بازیکن‌زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30090" target="_blank">📅 23:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30089">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4xLcRJVfaq87Q9M_zwPS6jQscBzjGxy6N1cgY8NJk6G3TQKs-waKIxwmDKV3Vz51ITpGi3FwfmiP3mbNEMbxsNjVGBuy0OBQPZ4Dm0VZX32aZgw6tzF6Y2ODUg-P8V6N-vJGYgXLeexM-DvSuuX__OjY00L4t6XJiQ7uz0GbJF2-Sw6mAn7TAU351-w1YJ5PbhSmEvK1NbGy3PDwXK0xzFmzcVvEtvj18fgMFD_8EvL2JHPL_Xh3Dpx_lgkGuv4I_ljfJQ1ASWcHclXpsm0KQ852oEOf52NjRejWQJuoeF4Qw2WfmJkVqDfT5el9ElheoK_ZNi81HigyF_QAU9YEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مجتبی حسینی باعملکرد دوبرد، دو مساوی و سه‌باخت‌از هدایت تیم نساجی استعفا داد و بین محمد ربیعی و سعید دقیقی یکی‌بعنوان سرمربی جدید این باشگاه قائمشهری انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30089" target="_blank">📅 23:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30088">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4B--gfyC0UEiubr7B_3aOYlCkECowleHbIW-ePYiYTTueWINgSgWHig2kQxgri6ApoAeboFTcvYWpgmT6QYzswJHqI7jOvBHkd67FIbjerHvKXfesYNlkv_D6AhqFA3nr2WgV5kZ5FXTHVjD47GUCbwH-zpgtEyBEFTJGXB25nAhtK8ANUEbdg4oUHr9HPutkUKvrtbCCP3obFAwIVx2ciHW0b_Xc5E4NU8qPIP6cEZeb3NcnWtDIBR_xAlvKbZoss23phed7NxOE372_thfO55Ae_VUYVbWhU2WnrIsZbIxS5tEd8_XELZibixLXyV4UJ2fmW5geF2GKldzzQdhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم‌بوندسلیگا؛بایرن‌مونیخ‌با درخشش اولیسه آتش‌بازی به راه‌انداخت و با هفت گل یونیون برلین درهم‌کوبید. هری‌کین‌به رکوردتاریخی 100 گل زده تنها در 98 مسابقه با پیراهن این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30088" target="_blank">📅 22:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30087">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ig-RQ1wZkGCTLb_Fyv8lIY4S8xGCqzWLJK_b0Prj3GtDlzv22CLBpkQ5CYZLKCkZD3Eb5XnYvfcHkU3lsNQI5Ard2CDP5GTAN8vSYHDWr0-BWaD2ga1tu79-C275ZfGxh4gXIg7MxeMuQoQBiUbpdhjBnNwNqfSU9ClZWCEZbxUul2otMj0rM308lJIp5SgTR4GugNi3hfVPRWQLQWQgbGq1erqUAmA8On-xCf2B8ErvRzsZVgktUcVDIL7ETp3nLi3sZvJXybb2kbwETjllC8EjfDPP0aF4snvYqfQ3vmHNZ1hoaDEK_MviWT-rM2Diic74VTDUJtNRdzhJwL1aSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30087" target="_blank">📅 22:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30086">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDNGbYPPeMvtOshDfuRSjr-J23myfqCKNd1gemrXBtzJq9hHuGn59_pi3Y6eZajXzWsNuRQNmgltwqZA0NmXTrhdq_lpMn8ylO_i8nZFJhRvYDYmAs5NbiNdp3tpNkNendci5tgDrxjQiYfrEpAEWopXrxnQLH9wEqEn1gGelBITqWwLYoy3C47u3Qi1TdhDV5uYLCo0Fn6OvEQxdWpckOWom41bggkQEa6EgvGVPtPrzigaJk32kMMXwGVqtBRWWZQNoPQvz5JLfQ3CAJf8eTVaB8BGjOTpnGJV_S6YqogrnxVLwpBkPVpXBK2i1UcdbcUtQ_aU7iP9xmwYyM2PJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30086" target="_blank">📅 22:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30085">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiIeOWHN11G46KyxV9OJ842d7B5KAx4KHxbTx5rOXF6V7FnD3Wf4dV9L3OnB0LRl1qblMurCLp9SP8sueGr8UfEuTjZt7qzKiNJ0he_IMPcBqm75JDz0FqfWG-QqCTmTgzqa2CJPZhDDrYVd9mM5U_oH3G3nT-56l8rWGxm_ZiCXlqFSZumdMPb2oAd1akwCHcIXcR5vYWlEcz0cr-a-df3WuRaqqSZiTAXx5F6TbLtjtVrPNUE2N72B_Uiuk5Waapxga-UiW3Se45OSem9mxbYjPClXp9oizgJo9UAZyqfGD0e_kc8ZdmtGKVjS3Ug7TS0XqEs5hrfS7S_DtwYGzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
دومین گل مهدی طارمی با پیراهن الوصل؛ درحالی الوصل امشب دردیداری خانگی دو بر صفر از العین پر قدرت عقب بود مهدی طارمی به این شکل از روی نقطه پنالتی گل اول تیمش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30085" target="_blank">📅 21:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30084">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9FLDAf5TUI1nq8_fS7VhaoRDsBNpF5f4ZgFcAlLuS0pfGeDQ3Anga3QIMZrlmk2hl3kM90UFjOQC7K9f2wnjVJX22T3Un10l2mEORfnLDTZ426njxH4ysez8ykmsZDty-3W-U5uo58heZqoD98cwwxYGTqmcrzj3yRXFZt681Se3xQV9wNkNRdtC44u-r01BLYw13q_XfPfoyuqIiLlXXZxp4FN-YA8CbCG7-AZ8qrutqQLNAjGjuPp7XabMrvR0KwaA1_uOzPb7EDl01nTts7sTsqMpnG--Q_K-syfsMEvxdw8CKk-FIvtbIjc2-EFq89f-pLm9ZMjN-mw_qFRWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30084" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30083">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2ht0EWAjFRi9SCBOR6vVhJ3gE8NHQPm1nvYJDtgtH8k5KJvhojUjcBF3rv4NtEhYu-W5_ycczd1-8yT2smYF8VyQHFkuCZ7fdiJBUMkQQ1z7tCdjVQit4C3vX8dBjasW_mYBNzN8FjiTIw23dxT-AM8bKIiQfifyorG8i6nt3tG1ZehfQX3Y6i2BsRa9bZngyQNpNBj-2NgnB5IPanOiOAXL9EXu8I2QTxO-CDf4wN7IUE9sA0m_bGFPegZ3bETbdlok7e595S-i0Fwvmi969W8WZLSnPm8akjEel4WHfmDtThBVOayORhbCHPED8KDHBSlhMf8XWABC-Zqc3rNCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا
|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30083" target="_blank">📅 21:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30082">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZEgHYIWsC9pOT0N0H3Xh0pwHuKB3h3Kx98IVhReOxRh2Ogs_KZq__PA5cHkLHJKy6Aiiz-bZIXDcTAwSERVyW6TQKvT0XXA4K9cV2fDLVe_xnEcyAyUDYVrJQGpzJ2sWPnhcVjU1XwC8uW0Z45i0dledbs04ZPEg-hvOzOOjdTWqYiN47EidlOEf3Kf9-dcgXHHkaI2u-8ULnHp4lcqqFtGFlEz0JpkoW81H12cABKPZW-0VP8oxsuvbKoJVMsNXcAIY5nagEcXDg70c5bObhxnzmBArtEAHsbdHxGO2RWjWZlrCBo3Kt3ad8meM-FVxUa_x567O4YuxYMeZN3weg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
ویدیویی‌جالب‌درباره زهرا گونش ستاره تیم ملی والیبال بانوان ترکیه و یکی از بهترین‌های تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30082" target="_blank">📅 21:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30081">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csmfyOEpto9VRfJwNA0mcM9OGhw7vXyNQc8RLm1KRhYdgp41K6ve6TBB2zWy2bzrktZNZk235swXjF4QV_jdrhTTHRtkHzAC4yxh4fKYYZZsUEHiathfaPwLcfQDKD9dhMsWhS2RVo-9nY9zdlcCl35T1L9PEuz92Wjfa-7HmDOJ1EpEfw6vL5VuZh0logA3Tzz3VbjxT7593mZIfP3ysSPY8yWKEYDS0aQH4g9vA5GHc8XVmTsQr_YKhSOH93CrqdU04WIXNTHLY1zrf4jDw50PChyr7QDp9FX2Q-f4aX0FBfnaOhzG2O1-yoxFe0DAbvDxIHKSrQFN2g7uMCGH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30081" target="_blank">📅 20:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30080">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=XBbxJeOQ1n3Vtb1j0BSQ-CrUBdliJ1u3TOub3Ii7sSeEvyw8Cm9WBOhbY00Fo5LZhOC_TGpm4c2tNKaGg-UiWGW6cxScm-hhcqFeh7ebnFULpwTQ6gRM1bj06yzALYU0GOtAL_7FmYnWissTtKqRVEMFPTK6vehN-MN0LEiEBiYT9HQKT6RXI9kFf1mMcpH_ZuufZ3r0LQ_NozcfTg_lOVzjwffao4MmMGmUWLoGlT4Tt-rxBXVPrFi11wPXFXrwRP5hK0QA9_zZtAshSKTjnOqCbavmDv8TV8WMB78WTCx8DWgA1x5nxgFVMmV4nUsmhF4dquUmi9pNWZ_vw37Z3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=XBbxJeOQ1n3Vtb1j0BSQ-CrUBdliJ1u3TOub3Ii7sSeEvyw8Cm9WBOhbY00Fo5LZhOC_TGpm4c2tNKaGg-UiWGW6cxScm-hhcqFeh7ebnFULpwTQ6gRM1bj06yzALYU0GOtAL_7FmYnWissTtKqRVEMFPTK6vehN-MN0LEiEBiYT9HQKT6RXI9kFf1mMcpH_ZuufZ3r0LQ_NozcfTg_lOVzjwffao4MmMGmUWLoGlT4Tt-rxBXVPrFi11wPXFXrwRP5hK0QA9_zZtAshSKTjnOqCbavmDv8TV8WMB78WTCx8DWgA1x5nxgFVMmV4nUsmhF4dquUmi9pNWZ_vw37Z3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
اولین‌گل مهدی طارمی با پیراهن الوصل با یک ضربه سر دیدنی؛ گلزنی ستاره ایرانی الوصل در بازی امشب این تیم مقابل العین در لیگ برتر امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30080" target="_blank">📅 20:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30079">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQzIkvfsKdsDVXFxkJXJtkiI0tXM9V53i34Xt3Q0B9k2to7Uonj1q23PGcy9VQeeXzTGnDlbvwxVCBg2JFADcaxRv3O9hJt0_eG5iZtNOtKr_eQ7T_FJkmUXCFIQjh7ajQ95r_5ueXKoHLYEFe-bGF2ji1WUordfZXfBBNw1CUQfOZXW0LvWIdq5zjWrdlYM-lLIp9kjGiDotOJSGSJQeUqxWey3O-1cf6HEqT13-_VwJhoQQCsQtUoeWzmTQFAkJtDec-45nP6J05w6MUtr8oymagl_4HZPZyFqt1txoZJpaD5CalD0d4-izd6-sh7QloKI9ltSlHqgf1BfakkuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شنیده‌میشود میلاد محمدی از وضعیت خود در لیگ بلاروس‌ راضی‌نیست و ازطریق نزدیکان خود در باشگاه پرسپولیس پالس‌های مثبتی نشون داده تا درصورت موافقت مهدی تارتار به این تیم برگردد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30079" target="_blank">📅 20:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30078">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbYkEbo7X-J9Bq353ywSGtmcEJOZuSZ0pXMZlNpLjm6gtTV9UJFuas1AJN4ROxT-L8SQgNRbditZuZVuyIDHviMi7L4Ogztd030y_zedh9S0XnUc6yS8mLFCeSZwTLV1TwPZr_hHRK3vNZGqx0R7cVB_ku0cvmzOUTgbmWPKItiemguykp02Iz-o_hzDWfm7jNxQM0ti3gBDtbCqRoi0lPg9silFYFIGG0fwHf9HatZLfyf5ozz7zoVE8WEg9A5fKPnqU6DuDO-dWVo1IJBODMd5ELsugBGg6-XbKDGuZaVOefqtkwYBS1yeGoDQ_7GVVx2U6-YIdJ-FJbRR-OVdww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
ستاره‌جوان رئالی‌هانیومده صدرنشین شد؛ چهار بازیکن‌رکورددار بیشترین‌تعداد دریبل موفق در 90 دقیقه در رقابت‌های این فصل لالیگا. نکته جالب درباره دیومانده 19 ساله اینه که مورینیو فعلا زیاد بهش بازی نمیده اما این رکورد رو ثبت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30078" target="_blank">📅 20:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30077">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz6Y7BcwH8gT21JXUncqyXnCZMmFVim1-O1gSbRVU5GV0iZxoFrDPK4Kn1EfpzOw0L0_d_qGKbRW_cTCW2xrGlykK59sHn61HJZPA0g3p9gyJNNuRZjWgbCuTStTRIbhlvNCcqBg9EWQ8hbagLDM7UJ7bjV7zUN63cRUzj2tUtn1wMv-TOTfT8n4NdAQXkSoyC8Nhuvs-l2ZTUp_1IHA3attpfVvLcaOt53UaOzQu58EUfCfG3sSiqRjEOOWldg32Y1L2GiB7UoLqaEXB0dAXpu93Yhx_amqCYog7-dXd-2jLYhnAoyezXY2Ts5Q79Q0-EOyeDPkPcRsUxddWHhdKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآمد لیگ‌های معتبر اروپا از فروش حق پخش تلویزیونی در فصل جدید؛ نوار سبز میزان درآمد از فروش داخلی و نوار آبی درآمد از فروش خارجی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30077" target="_blank">📅 19:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30076">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🟣
در هفته پنجم لیگ برتر؛ شاگردان ژابی الونسو در در دیداری یک‌طرفه‌متحمل‌شکست سنگین سه بر صفر مقابل برنتفورد شدند. برنتفورد برای‌اولین‌بار بعداز 88 سال، تونست توی زمین‌خودش چلسی روشکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30076" target="_blank">📅 19:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30075">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swLtNqMLwQTopqxs9Ehzfciz7JkqivRQqadOHr2-PRFXGU7FvZzp28gK45Gi7W7edyVmoS-GLZp0-O_8uwtV1fxTef5OOvRUaqGapTqFZlWVy6n8-my8UGqrnsaLFZp5UQZIQCwW9avI9S8Zd4Lxhz7HajX0B1yvAbvL7b9Jk9HzxcKs_DAwz74jjUeZB8-O285gd8XUS7y6g-uIH7IrpyYhatWw2Z0-WWYZJdgIrIBFCJddSwKdUZpGieoT5wDbZcFJSsMe0AYxQuH2-aHAHiluJuzrfqUUxhnLPCPRd1pOJKp_5Fj0nmRRwmhAfHdyxEDpH2iZFphGDM0DWpQpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام دیوید اورنشتاین و رومانو؛ بعد از منتفی شدن حضور ژاکا در چلسی حالا این باشگاه به درخواست ژابی آلونسو درپی جذب جردن هندرسون کاپیتان 36 ساله سابق تیم ملی انگلیس است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30075" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30074">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=hlrqct0uwCq5zy0a5Cx6RMYTtZVqTkGErlfBsV-t9V6kx_9xmuPcSpFtNCqRSikz7xwzsC-KFv0_LqxLhE1TvTwTGKxh06pYx6FtULSQwo1JE0ZSjl6Uhhv1ttNTwgfpV_uzm7mF9HE93KbsQKZqcgDwSo9xpQySGVFGr1G592g4UjHhDuOGe216tXP7oB8MNTVHodYJ-z0dpHxkDg0BsU420GxeXCVXPtHnwDDnmI2xTiyym7jHZYZnI_u8l4nslSvkR8Nfl3Kkt9sY23VliDrbUIOwbB3GAM9IFzZd9XtrfBgcrUY-MT1xSV0G9VbptX1s9k4Du5jZvC0bFOI7BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=hlrqct0uwCq5zy0a5Cx6RMYTtZVqTkGErlfBsV-t9V6kx_9xmuPcSpFtNCqRSikz7xwzsC-KFv0_LqxLhE1TvTwTGKxh06pYx6FtULSQwo1JE0ZSjl6Uhhv1ttNTwgfpV_uzm7mF9HE93KbsQKZqcgDwSo9xpQySGVFGr1G592g4UjHhDuOGe216tXP7oB8MNTVHodYJ-z0dpHxkDg0BsU420GxeXCVXPtHnwDDnmI2xTiyym7jHZYZnI_u8l4nslSvkR8Nfl3Kkt9sY23VliDrbUIOwbB3GAM9IFzZd9XtrfBgcrUY-MT1xSV0G9VbptX1s9k4Du5jZvC0bFOI7BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30074" target="_blank">📅 18:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30073">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6rWUckBRlgczhPUKoYJT81lvvejKR797agvWLxmAmG7_XX221wJr1ard0NzfDbM6MZPS3NnS9IIJ1gaxapIEqWtZVEo2TrO9LogdR0JRUSGpSFTcIwP9YyZzVGp8rbRdy-1KL86VDivFsdERAKLnBVvn3K_fjENLxE47kPgjI1c2YKMGfrvTetwnhCTl3MX89r1AM-aUU0npAZ__6htiJfsaYUv7k8P4cDxm7aVW8wnO_bzBnrPkpMvH0czTIwVt-ExlLEiRIq0q2pLoJ8LnzVRBjYk9CNs6OBWeeSA81QbhNHVGcy0S-Vl49M2tWOlxUijRdqJBv0VbAjrF2xUHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ دستمزد بشار رسن در پاختاکور سالانه 600 هزاردلار بود. این‌بازیکن در نیم فصل قراردادش به‌پایان‌میرسه و علی‌رغم اینکه پاختاکور دنبال تمدید قراردادشه اما گفته علاقمندم که به تیم پرسپولیس برگردم و اگه باشگاه بخواهد حاضرم مذاکره کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30073" target="_blank">📅 18:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30072">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=g_Q-msRWxKRYKQytA1xvt7YBEa2nho5W2DfMLZvFTEeoxHuPyJLGlPKn8zEL-GiVIWuLmk_4ixVLpHDgzmzGR9mxkdeS2y4BXPos6qI6vvidbZE3amvX-j6vu_mDG0Y4Ouxxqf8nxxKIoPRpmGjQuqHwvcqKIkaPr12jXrm1VaQye-D_buEHkhphHH221vGXS-TBL3Wz2-f_ntnquosPbsmI_Yxp4QOxytbNkvKSA-PX9Oio2vuIFTwO-3dlafeXFIWoWlDuIHJj0RtRlY27ESYrnxhqLe7-tEr0DTIF5_98Sf9tgvvUl9r-h8c6SnVUL5qXZrgyLb9ArSkl0-t3ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=g_Q-msRWxKRYKQytA1xvt7YBEa2nho5W2DfMLZvFTEeoxHuPyJLGlPKn8zEL-GiVIWuLmk_4ixVLpHDgzmzGR9mxkdeS2y4BXPos6qI6vvidbZE3amvX-j6vu_mDG0Y4Ouxxqf8nxxKIoPRpmGjQuqHwvcqKIkaPr12jXrm1VaQye-D_buEHkhphHH221vGXS-TBL3Wz2-f_ntnquosPbsmI_Yxp4QOxytbNkvKSA-PX9Oio2vuIFTwO-3dlafeXFIWoWlDuIHJj0RtRlY27ESYrnxhqLe7-tEr0DTIF5_98Sf9tgvvUl9r-h8c6SnVUL5qXZrgyLb9ArSkl0-t3ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج الطلبه و دهوک که تحت هدایت علی رضا منصوریان و گلمحمدی اند در فصل جدید لیگ عراق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30072" target="_blank">📅 18:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30071">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMPKkbzBX2nPqVTLcUcDqHbNdH6obFOjy0WRBgV-1DBW6Dd1wVJf2m2OenEroL7YX3D_bNZMC44ixeN0B7Vw6JDD59aUQfWx-kH4KT_QM9o1sKsA_2EBIHlquh2ryOhdRAe7OBNtpkyuKwloCK1YN7iCh1Q0hg1_qEodUjTcBqejZTBWNgCuC9HGGNCT4iBBv-sVnTaveSGb26AylOECPwek5_DsonPZWGvyCJPA60B7Ki5K5LpO6-rpHrCLJijNAdh-M4OGGl6C2QmewQBbRYhKiSa9ZBNIAIM19qbo-Gc_-Yisop6P1QqhDsQbWDfXBcgKnXVtjBTDhS_NsIyJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30071" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
