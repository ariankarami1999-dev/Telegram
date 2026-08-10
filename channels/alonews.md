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
<img src="https://cdn4.telesco.pe/file/NOdS1mw16UxGbuWYo7rOaZQITdOdouWDHoROdzR9b2vpQS4lQ50uvoXfOZmsw_2YGeBkiVWnro3sSxwsV46qBNQM0ft2GI6JvrTOEG2zkFAWf9I7I24b3zeHSXDdKw_kaa5yg4iDXTJO-EAFHTYRwq0B2AjCVdU6L-4bW99TtaLQD99pECG-YnfoDp78-V6PrOcjjwyK1VZWMayC7BF6Hi7YW7cry6B3E-1Pv5Q247HEIQaxhUBn2ZiFCJxnaL8E90gqb1lxGh6-M5V4oLlnX_fFRZshV3df1YSVNQGRS1jOsq0iPAeHqbtP4ALdmE-0UESYTNYUcPbCyx0OR9ZNIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 971K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 19:52:48</div>
<hr>

<div class="tg-post" id="msg-141008">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiYhKZxKprk-8IhQl44ZjKQxkoz-y0URH9K64IGctV7-n9KbywjYw9mcjwi04HB2OA7Z4-7vztLFCFByeZVtqDgI1OAdu2Biyuol2hABHcSisXCAc7c4vxZa3FkJB3ueJwQPvrc5kUrJI3mETvVpsdVNcfMkOXt07Ix4j9JimH-hhzHd-AWV9Pt5xi7tKtGibzkL1MKVp20lgvoTHXWUYu7cItDgI_0v5gmuXULEcxqrIkZRFl3RrLIYyRYhO6WB7sEBPs3afaQxkMmkZ4wC3S8zNkXVMhrfacv3YIKUUASXFJaSHHMYhRyeIJoQr7pXIx0oSZnUzdy6U9CrxqjDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: ایران عبور ناوهای جنگی آمریکا از تنگه هرمز را برای همیشه ممنوع می‌کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/141008" target="_blank">📅 19:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141007">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSM3J-Dy8y9oIMC4usw0DL5-q_KSW1P72s7FLsEwOuy683AbCY4AUzxM94os7wJq5DzYaIZA0ATNRTIuEvXhubzp0kMqytyi4uUpl30Eg9tmYMSNz4Lcsk2VuBF-6_8ygddAW-I4ivJFufnPpdfox0xwz0EjAgK19C6Dpw0AdviU1hXkMOvxZ-GF0Sehjj4jFyWq78JE-ssTz0dQVWPVkfWh9afhF0ZRXleQ_Dp4rKaoiDrMuZ5ptqt_Vo9OWExrBIunuuj0GAEpFPxLK4V-HigTnOpecZV1SJE-KRfzhvSOfVy3ZLReli1fUT4eaApl92g6V_eoZ2OVNsF46I0-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🚨
تاحالا شده دلت بخواد ترید انجام بدی درامد دلاری داشته باشی ولی علم کافیشو نداشته باشی؟
🔴
پلتفرم TimeTrade یه صرافی انگلیسیه که یه هوش مصنوعی در زمینه ی auto trade ساخته که باهاش دیگه نیاز نیس برای کسب درامد علم ترید بلد باشی
همه چیو به هوش مصنوعی بسپار خودش اتومات برات انجام میده
✅
با این صرافی با هر مقدار از علم و دانشی درامد دلاری و روزانه و لایو داشته باش
🔥
👇
https://t.me/+BO755zQm6VM1NDE8</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/141007" target="_blank">📅 19:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141006">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
براساس نظرسنجی جدید شبکه CNN، محبوبیت پیت هگست، وزیر جنگ آمریکا در پایین‌ترین سطح ممکن و در وضعیت منفی قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/141006" target="_blank">📅 19:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141005">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2fLNWUcpWMl-_mmYbpMG8VGeKCLMqn2R9SPv1UZrgUZOG4Wpc9Y7z12DMNGCx02jrhF6mipaPGlZad9KHjBZVMMrHecZZjp5v8CzAxdJR1Aw3O9HOUjNT0NMLZIM8Qr6cuIfI19i1W6T-Wr3R21tTkO4waeWv1TuXQSuAgpWInyaGNebYZMJytsmVsHX3ZRUlcU1e6Co4c8FnxIoOkjAV-YCaW1JA94BBbvwl2__Y0C7Zdo7cNONp0zZAUH6H3KaYOhOKalz2S_ndbNGTRuFfJhjbSdsXMOkhHA5yRe332QgQM65FF5fXb9tATKvhQRRX-pEpXUJdtfsB8D-YAd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی
:
ایران آگاه است که آمریکا در حال بسیج برای یک حمله برق‌آسای بالقوه احتمالاً در کنار نیروهای اسرائیلی علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/141005" target="_blank">📅 19:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141004">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJsc6Fhok9tiscZVBUUY8_-hgBNxVUVtd7RuNHdZD2Otqhd6c6zeSUk7LQwqOjGTL6HzRu9JuEjkQNBTp55VYQVSIXEmuEIJZZh6dtwzu5UXPG9Lk3Y_JT_0uE2KUSZgSsCsIBjl5Uu9sO9xnGCMNQilnVqdCZEHlgoiHzblXrr-G3IMtliY1gDXGnDYR5Zf_qepzyzptf1ZOuE-79PzaylpDDLMPpoWea_6q49tbowFWHbcUsQsG_Orffi4NGYCIfMfP7YgCGBrT7TRDZYJgCQvaboJXRxxBlnOb3rm8bYwLqx7TvwfmYNCxKvru8nTgeVxg8GPjeAOG4-bDu2eRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعضی مالکان بالاشهر دیگه ریال رو قبول نمیکنن و اجاره رو به دلار میگیرن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/alonews/141004" target="_blank">📅 19:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141003">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V70eoqIJghRxNPdEWTVW9AYnT_yri-Fd1fQ7ry6X6WnhtKgDZLeGipeQBBlzK3tXU5B59-sB7ZO_0P_iU34drwKx5rx9U59xAYcr56di_NTvOEAVq4l4U5xcco9dtQsC0ikGM8vf9RQiOmPfREtZwEHMo0LgUfRIxOVeinmslJWXX9FsV48MHxFt5y2vQz3eKYzgi1xdQUYrSHTD-LL7q9zIzV4hW6e6ibQSHuiBiRTwP2dahxjzge3I3lgP02u0_MTQ-F43DPlB3B70HRBqFRZo8fmUjs0dfyum-1zBPbhXHUGD0SP9pjND6iBZDMxGEVZSF6w0tkZ7iDK_lD8kgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعضی مالکان بالاشهر دیگه ریال رو قبول نمیکنن و اجاره رو به دلار میگیرن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/141003" target="_blank">📅 19:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141002">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648f985ee6.mp4?token=FVo_exaff6zPpjDAUlqJHBmpX0LDx2nCeBGds3Qw9iV6lFcsujICHN-v0jWyiPEKbwEhQ7zv3lmV-V6FMJdrKZXN1ZYPGR2gfMGpdQbI50g9RUvMcsUls9dWjhVETzytJlopal2dVxOT4c552GGzVYt_Ddu9ppNk0RetHE-EJMPSC9WgJ9kNudtX0IPeVtEqZ6PmKh_4MXoGlxKZt4Z2_py4dNNhspadMMrvFUH4n3JZ7LXzmkflwqFLt8u5Kve8aXf45swUuMFha2Pab8XvWLz017dB7qnRxqRddoPDUpsAM4RhVZk9yvR92ugHhqllAtVZ_GiBCY9GFaARCHZn1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648f985ee6.mp4?token=FVo_exaff6zPpjDAUlqJHBmpX0LDx2nCeBGds3Qw9iV6lFcsujICHN-v0jWyiPEKbwEhQ7zv3lmV-V6FMJdrKZXN1ZYPGR2gfMGpdQbI50g9RUvMcsUls9dWjhVETzytJlopal2dVxOT4c552GGzVYt_Ddu9ppNk0RetHE-EJMPSC9WgJ9kNudtX0IPeVtEqZ6PmKh_4MXoGlxKZt4Z2_py4dNNhspadMMrvFUH4n3JZ7LXzmkflwqFLt8u5Kve8aXf45swUuMFha2Pab8XvWLz017dB7qnRxqRddoPDUpsAM4RhVZk9yvR92ugHhqllAtVZ_GiBCY9GFaARCHZn1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرین تصاویر ماهواره‌ای از تنگه‌ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/141002" target="_blank">📅 19:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141001">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dh7f1DGmp0Cjg-h0uHan8TjfdHdVNDpT8NFzrSjToGLHN_YGKk3hwkNSNEwqQauxFj3KI96Hrc7f2M-TediaLPJ3cJndf4uDoKzxPACv1L9KogcWd3OsDP4Ye44HNZWpmDT9Du9kdRQWbTqB6W8Usl4h6ryd1bqbrfXGKncikTMNEsXeSmjjHd0XU7Qa1-fr1SwDFgjCQO5tWQxQV3CxoFVoV3kiyabiFTOFNoUg9eRukmJHgVB5LPLIw1s40rvwuCuh5E2FoVVQoTWpoeRMetw3dW5NJjQYoY9D9ujrdhuwkAW6tYFzPutNrrk6ik2SvENzZbrxk-po-FAhFrQKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روبیو، وزیر خارجه آمریکا : دولت ترامپ زلزله بزرگ کلمبیا رو از نزدیک دنبال می‌کنه و آماده‌ست از مردم کلمبیا و دولت این کشور حمایت کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/141001" target="_blank">📅 19:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141000">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای خارجه ایران و آلمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/141000" target="_blank">📅 19:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140999">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1689f5372e.mp4?token=eCOuEOsjacHQOyueErN5pD0vnSSXVi_ruKxE3o1dr0QLqjkqBM7_nLpYAtfIoo2WEYUuPG8KC4edDhra5VxZZFGHW1vy0yVX0owoggqLmvzv3cmG_RxMR_mlqs3HyQ6da2xmaXvaTdriH96U7uWtH05qruKF6P_pqOOnkZSCWxF2Q3ePOm0iH4JZt7GEH1tQsXfXX-ZUFxVeuYTW65FWmUs9qdanuOFPwYozsIX4lxCCqaGoG5PZjR2yNgMsBvA_BzW8Ded0nOFUEEW_T5hL79BLTDYzedowWU3hHaV7C7H4A803X8mai635GkeyF2SOLrvocp4L2LFapxihEmR2_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1689f5372e.mp4?token=eCOuEOsjacHQOyueErN5pD0vnSSXVi_ruKxE3o1dr0QLqjkqBM7_nLpYAtfIoo2WEYUuPG8KC4edDhra5VxZZFGHW1vy0yVX0owoggqLmvzv3cmG_RxMR_mlqs3HyQ6da2xmaXvaTdriH96U7uWtH05qruKF6P_pqOOnkZSCWxF2Q3ePOm0iH4JZt7GEH1tQsXfXX-ZUFxVeuYTW65FWmUs9qdanuOFPwYozsIX4lxCCqaGoG5PZjR2yNgMsBvA_BzW8Ded0nOFUEEW_T5hL79BLTDYzedowWU3hHaV7C7H4A803X8mai635GkeyF2SOLrvocp4L2LFapxihEmR2_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نفتالی بنِت، نخست‌وزیر سابق اسرائیل: من اصلاً نمی‌خواهم بنجامین نتانیاهو را با لباس نارنجی ببینم که وارد زندان می‌شود.
🔴
برای بسیاری از اسرائیلی‌ها، او مدت‌ها پیش از یک نخست‌وزیر فراتر رفته است؛ او یک نماد است.
🔴
من هیچ مخالفتی با او ندارم. نمی‌خواهم او را در زندان ببینم.
🔴
بگذارید به خانه برگردد، به خانه‌اش بازگردد و هر کاری که می‌خواهد انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/140999" target="_blank">📅 19:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140998">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
با حکم سید مجتبی خامنه‌ای، علی عبداللهی فرمانده ستاد کل، احمد وحیدی فرمانده کل سپاه، کیومرث حیدری جانشین رئیس ستاد کل، ایزدی جانشین فرماندهی سپاه، عظمایی فرمانده نیرو دریایی سپاه و طائب رئیس بسیج شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/140998" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140997">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxmuI4Ydn7VmZ08q7AhQsuAmtFHBwRdUyS9kowqSCyy5mU-rxeRAdECfr3JrtDAD2ALjaQFNzn5J-cNA6MYl7n2j3t9c_M4xssrCd6FmFKRtKV1cQsRPrxMig0Bm3Vg2OxnfFC_Du7wMev8qRd4yjPDYszTC7NAfoHB3Jp86UBvaj65j5rIVdu2F3LN5XPl4bcEAiwawV5_aolX5z4UliK8sh6bL0F7otaE0_l2nq1CqktGprtM44SNTMSNXHE2niA2RkaY37hkeohDfhgM_BOSiCjH_vw_V6cUxF2d01gnxD1tvNbEyKsvSILc6okxJXHQ-nHIlz8n4mw8b7xBkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش عراق از منهدم کردن ۸ مخفیگاه داعش در استان کرکوک این کشور خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/140997" target="_blank">📅 19:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140996">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ad37751f.mp4?token=MpndGc_c6mmUnTswJycLa3mveU0IcH3l40O4alUSo4l-b51HrnQYOK3GQH39HNrBEsPCH5XO4_KYtOh8E1IiUWvtVaujJ_w5h13m5lwm573aRFKtCbAAHGqhu_rGXSP-ZOUvneQb54CIzgAVUTj9_KB-vtHSuivtLCvTZFfVILzRXuEYuQ-GduQnQjMHGeGa3yQtbFSqXCxPMBCigRcjz_0NAAd524kO-WIqGuyXu2fjrq9ioC4ltXpTmS64jMcZH-TcbD9Bo8cwvDYzq2ZAM08zdLPckcR5JIRlWE6K3BR6m1-8Lzp27v66qdxJ-pzD9-z5on1XMs1MD8w7jr-LEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ad37751f.mp4?token=MpndGc_c6mmUnTswJycLa3mveU0IcH3l40O4alUSo4l-b51HrnQYOK3GQH39HNrBEsPCH5XO4_KYtOh8E1IiUWvtVaujJ_w5h13m5lwm573aRFKtCbAAHGqhu_rGXSP-ZOUvneQb54CIzgAVUTj9_KB-vtHSuivtLCvTZFfVILzRXuEYuQ-GduQnQjMHGeGa3yQtbFSqXCxPMBCigRcjz_0NAAd524kO-WIqGuyXu2fjrq9ioC4ltXpTmS64jMcZH-TcbD9Bo8cwvDYzq2ZAM08zdLPckcR5JIRlWE6K3BR6m1-8Lzp27v66qdxJ-pzD9-z5on1XMs1MD8w7jr-LEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی پالایشگاه زاپ‌سیب‌نفتخیم در شهر توبولسک در استان تیومن روسیه را هدف قرار دادند، این مجتمع در فاصله‌ای بیش از ۲ هزار کیلومتری از مرز اوکراین قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/140996" target="_blank">📅 19:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140995">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
زلزله‌ای به بزرگی ۴.۷ ریشتر در عمق ۱۴ کیلومتری زمین حسینیه خوزستان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/140995" target="_blank">📅 18:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140994">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نخست وزیر پاکستان: تفاهم‌نامه مکه هرگز برای تجاوزگری نخواهد بود / هدف از امضای این تفاهم‌نامه دفاعی تقویت وحدت در جهان اسلام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/140994" target="_blank">📅 18:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140993">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGlDFzT4_LmxNMTEn2Fnhv0agps7WiIvLYI_2cTkBMu0v6PZEaaBr4nO5GtkghKQt2cVcYWiCkljHNb9jAAlJucmewarD9EFvbAOchYakAWomNfe5_12qw4qVHvmv44hdkF1_rsbIvPMY8F_YZpTyKLMreRXXG92ix4c6W6r4xhQl0x9hcloxgA7JZxShZzKkvppskfwB3VKlWDxi2P_M7vOl37u1dbLfu-CavS4dCHHUWmj-NwknWkj4hMbOCZEqCJUpj6W5WsHt5A18CRiogixfQDfb6PDYzogqERhe-28o7fBWgL-SSx77hr2pZ0-lbhunshRTY7H5iaLDIIX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده همچنان حضور خود را در زمینه سوخت‌رسانی هوایی در فرودگاه بن‌گوریون کاهش می‌دهد، به طوری که تعداد هواپیماهای تانکر اکنون به سطحی نزدیک به زمان آتش‌بس رسیده است، زمانی که تقریباً 20 فروند از این هواپیماها در این فرودگاه مستقر بودند، طبق گزارش کانال 12 اسرائیل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/140993" target="_blank">📅 18:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140992">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رویترز: شرکت آرامکو عربستان سعودی اعلام کرد که به دلیل حملات انصارالله به پالایشگاه جازان، بازگشایی این پالایشگاه به تعویق افتاده و تعطیلی آن به بیش از یک ماه افزایش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/140992" target="_blank">📅 18:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140991">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزیر کشاورزی اسرائیل، آوی دیچر :
ما اصلاً خلع سلاح حماس رو نمی‌پذیریم
🔴
ما می‌دونیم که حماس هیچ قصدی برای خلع سلاح نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/140991" target="_blank">📅 18:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140990">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر کشاورزی اسرائیل، آوی دیچر : پاکستان، عربستان و ترکیه ، این یه ائتلاف سنیِ خیلی، خیلی مشکل‌سازه برای اسرائیل. به نظر می‌رسه مصر هم به این ائتلاف اضافه بشه
🔴
قبلاً محور ایران، عراق، سوریه و لبنان وجود داشت که ما اون رو از بین بردیم و سوریه و لبنان از بازی خارج شدن. حالا با یه ائتلاف جدید روبه‌رو هستیم
🔴
باید خیلی محتاط باشیم؛ پاکستان یه کشور هسته‌ایه و باید نسبت به این موضوع هوشیار باشیم
🔴
این وضعیت، نیاز اسرائیل به ائتلاف با یه ابرقدرت جهانی مثل آمریکا رو بیشتر می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/140990" target="_blank">📅 18:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140989">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
مهر : تا ساعاتی دیگر احکام انتصاب چند فرمانده ارشد نظامی ایران از سمت سید مجتبی خامنه‌ای ، منتشر می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/140989" target="_blank">📅 18:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140988">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NUGHIGkmPnbsaVejVH9Iht67I3ZNVzs5TTbiUuM451BT6FQ9in3KahUaKBLmFG_0gbxpn-BJb1ts6Ba2m8bgwJxvg2IKIHD1Y09hbNddXRSvPrH5xZ3oaVXBXjB0_HVwhtr2yYc-zDcEzETRN_s724bZh7zrNwMMIt5oomeP6MjBG3aNTvIOfag7EedjVPIq8Rh0QZ1PVRhMbZCkUur_P-h3ceGfGJpaUI64mfVQadfnPJqPg5GsNv4DoXzDj2nqOnb_pg22aJXuVNVxYNHmSiybPzSzXNYYdC8HpBD_VcZ_6nU8giB3ZiKvX0shEhuqu6TFIJRA_PS62ZHCNFpFBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان زمین‌شناسی ایالات متحده تخمین می‌زند که تلفات ناشی از زلزله‌ای به قدرت 7.4 ریشتر در غرب کلمبیا، بین 100 تا 1000 نفر خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/140988" target="_blank">📅 18:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140987">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
الجزیره: به دنبال بلاتکلیفی درباره روند مذاکرات برای بازگشایی تنگه هرمز، قیـمت گاز در اروپا ۸ درصد افزایش می‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/140987" target="_blank">📅 18:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140986">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
شرکت سعودی آرامکو، تاریخ راه‌اندازی مجدد پالایشگاه ۴۰۰ هزار بشکه‌ای جازان را به تاریخ ۳۰ آگوست به تعویق انداخته است، به گزارش رویترز.
🔴
این تاخیر، پس از حمله حوثی‌ها (انصارالله) در تاریخ ۲۷ جولای رخ داد که در اثر آن، مجتمع گازی‌سازی ترکیبی (IGCC) و منطقه ذخیره‌سازی نفت این پالایشگاه آسیب دید.
🔴
همچنین، واحد فرآوری ۸۰ هزار بشکه‌ای این پالایشگاه از تاریخ ۲۷ می به دلیل "مشکلات عملیاتی" از مدار خارج شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/140986" target="_blank">📅 18:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140985">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رویترز: قیمت معاملات آتی نفت برنت و نفت خام آمریکا بار دیگر افزایش یافت؛ همزمان امیدها برای بازگشایی تنگه هرمز کاهش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/140985" target="_blank">📅 17:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140984">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نتانیاهو : ما می‌خوایم جایگاه اسرائیل رو به‌عنوان یه قدرت جهانی، و تأکید می‌کنم «جهانی»، تو زمینه هوش مصنوعی تثبیت کنیم
🔴
ما قبلاً این کار رو توی کشاورزی، پزشکی، تجهیزات پزشکی و خیلی زمینه‌های دیگه انجام دادیم
🔴
و اینجا هم همین کار رو می‌کنیم؛ در حوزه هوش مصنوعی
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140984" target="_blank">📅 17:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140983">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پهپادهای انصارالله به سمت اهداف خود در المخا در حرکت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/140983" target="_blank">📅 17:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140982">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f0b445a7.mp4?token=HNQ9CaWtWfSb-LwloKdf3SDLf4AGztnTrr4ig430aRthJsS4fCNhJgYmKQ4GIoAyHYq3HPlbpMRLmHQsp39Uuq-Schc1dS4wkDP7qA68Rrn-YEXsjYGZ0Z05QNPkCwf9darflSoyhtFQzAGwttbgfZkJQbzNrQN65fCzdMScSbmgcATnlgmbtJ_NkG630BRaljfWtxYvf5b1tJdxY-NANkDp7rshODQqtObWUVwHG1mr9Z05XGZqMO_n4Pjx5qeN6Cz2tq6q-498YBGTSY8INRNP3N3L4SfR3oROwIkuMvE5JUFuNYrR558de5Jc9IuncgnoPELAQOS80sbkKq71Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f0b445a7.mp4?token=HNQ9CaWtWfSb-LwloKdf3SDLf4AGztnTrr4ig430aRthJsS4fCNhJgYmKQ4GIoAyHYq3HPlbpMRLmHQsp39Uuq-Schc1dS4wkDP7qA68Rrn-YEXsjYGZ0Z05QNPkCwf9darflSoyhtFQzAGwttbgfZkJQbzNrQN65fCzdMScSbmgcATnlgmbtJ_NkG630BRaljfWtxYvf5b1tJdxY-NANkDp7rshODQqtObWUVwHG1mr9Z05XGZqMO_n4Pjx5qeN6Cz2tq6q-498YBGTSY8INRNP3N3L4SfR3oROwIkuMvE5JUFuNYrR558de5Jc9IuncgnoPELAQOS80sbkKq71Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی دیگر از باقر خرازی: آیت الله مجتبی خامنه‌ای اگر در این سه سال از دفتر رهبری طرد نمی‌شد، شهید می‌شد؛ مرحوم رئیسی هم قصد رهبری داشت شهیدش کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/140982" target="_blank">📅 17:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140980">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68266a2f51.mp4?token=YRCh5JSgSZE5OkNVyEQbo7Rue8CNHPIXYVVuhmVvajFimnSRV6BCdGC5wbNrIVeVyXOGG7ixaoYNYZAx0d06fWnAubYUrrMV_gDOco5u_98-OmtZMCI0ltzlMSI-EfspgY03nIAu92B-NH1Oxfo7ug3fiB8YML3g5V1KWn_9-5UXbCH4Z5VvKN6i5pqVTtZGHSQbT1vWLC58XxfunU8_lofil-Yk5kS0mLYLv7tpL-61f5u4W7MIHdcfXr1_lWxGv3G7IjOq-0HhzImtYeGsuJKmKaIz_fm0yBU4nuPRoW6QG_c9CF9w5PdGTr0v1czU51yVirc3nNrRpPLQI1yL8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68266a2f51.mp4?token=YRCh5JSgSZE5OkNVyEQbo7Rue8CNHPIXYVVuhmVvajFimnSRV6BCdGC5wbNrIVeVyXOGG7ixaoYNYZAx0d06fWnAubYUrrMV_gDOco5u_98-OmtZMCI0ltzlMSI-EfspgY03nIAu92B-NH1Oxfo7ug3fiB8YML3g5V1KWn_9-5UXbCH4Z5VvKN6i5pqVTtZGHSQbT1vWLC58XxfunU8_lofil-Yk5kS0mLYLv7tpL-61f5u4W7MIHdcfXr1_lWxGv3G7IjOq-0HhzImtYeGsuJKmKaIz_fm0yBU4nuPRoW6QG_c9CF9w5PdGTr0v1czU51yVirc3nNrRpPLQI1yL8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک Long March 7A (CZ-7A) چین حدود ۸۵ ثانیه پس از پرتاب از مرکز پرتاب فضایی ونچانگ در جزیره هاینان، در جریان مرحله اول پرواز منفجر شد.
🔴
این هجدهمین پرواز این موشک بود و دومین شکست آن محسوب می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/140980" target="_blank">📅 17:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140978">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7220dcbe.mp4?token=Qm0X6LoOBROBUmyCVKiV7VZ09ss5FvtTvT_j3s8XG98ruRYGxPYDPraIA8vxT5V0-i11QhQYWOPiN4y8rZmCUvW_1h094X8vzSU3wtiFW3L61LPGDv-IOOCzupHBAlWGpMwfF9X5wK2-qjNFzUPuCGQKbfjEReMo-A1CKExlnt_ZcnnhvKVtAOwU--k9aC_Sm7A2szebVFaOT0NLKB5tD8HZt8m_6yBuP0mlXl3UMlnHY27nrcWZu0rvtl2ZyRsJfiG0INU6uSO45GViLCeYK3DDUxG-Ivb56dvxgR-mqDwPUqGk1d3tS6uIH62w_fOTNPmskvTpka9jhQsZall7Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7220dcbe.mp4?token=Qm0X6LoOBROBUmyCVKiV7VZ09ss5FvtTvT_j3s8XG98ruRYGxPYDPraIA8vxT5V0-i11QhQYWOPiN4y8rZmCUvW_1h094X8vzSU3wtiFW3L61LPGDv-IOOCzupHBAlWGpMwfF9X5wK2-qjNFzUPuCGQKbfjEReMo-A1CKExlnt_ZcnnhvKVtAOwU--k9aC_Sm7A2szebVFaOT0NLKB5tD8HZt8m_6yBuP0mlXl3UMlnHY27nrcWZu0rvtl2ZyRsJfiG0INU6uSO45GViLCeYK3DDUxG-Ivb56dvxgR-mqDwPUqGk1d3tS6uIH62w_fOTNPmskvTpka9jhQsZall7Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از فرودگاه بین‌المللی ماتکاینا در شهر پِرِئِرا، کلمبیا، پس از وقوع زلزله شدید.
🔴
تمامی پروازها و عملیات فرودگاه به حالت تعلیق درآمده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/140978" target="_blank">📅 17:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140977">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزیر خارجه پاکستان در گفت‌وگو با عراقچی، درباره تحولات منطقه و توافق دفاعی مشترک مکه میان پاکستان، عربستان و ترکیه رایزنی و بر هدف این توافق برای تقویت همکاری‌های راهبردی و امنیت منطقه تأکید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140977" target="_blank">📅 17:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140976">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پزشکیان: رهبر کاملا سالم است، کسی که ۷ ساعت میتواند بحث بکند قطعا مشکلی ندارد
🔴
پ.ن: دیدار اخیر پزشکیان با سید مجتبی خامنه‌ای ۷ ساعته طول کشیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140976" target="_blank">📅 17:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140975">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
الحدث: سفر آقای قالیباف به بغداد به هفته آینده موکول شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/140975" target="_blank">📅 17:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140974">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
عمان: لکه نفتی ناشی از نفتکش به گل نشسته «کارولین بزنگی»، تا حدود ۳۹۰ کیلومتر مربع گسترش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140974" target="_blank">📅 17:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140973">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مارین ترافیک: تردد در تنگه هرمز پس از حملات دو روز گذشته ایران، تقریباً متوقف شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140973" target="_blank">📅 17:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140972">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P55ItyWS8HWzHCNh1lle6NSN1poAzi5DuDKHt0Gfi3PjZWvQB_eZBB7514GrH1rCNdLT_965R_jMB7THZdrudFyTDpXgC_ECSALRitPSznxSyd-reDdKwnTkuOuscMVGq5sJnHRoQg8c0KweYBhBx4FJlXkwZ7JRm_1k-j5vWB_Pw2WvD9bKiNB6ztUYm8YczzZPc-VpvUNQZ1OQBNwexKHJlINyt2jwpCwMwfWKzW29bzhw6X6BFIN_GkEoWTVZZnFx8JlYdFTFHZ7KmUsXi6BNbT7Ho6Sw69kjak-pPq0t2-erOxmI_SZNk2pBbJ4SgyBjJdbq1jsZX41FrI9evA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا علی دبیر ۲۲میلیارد بابت قبض برق از فدراسیون برداشته و پرداخت نکرده و اداره برق هم برق فدراسیون و سالن‌هاش رو قطع کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140972" target="_blank">📅 17:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140970">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjrSpHXQJwvJ6obAAk7ILbgl1DM92kcgqzSBtGKsLn1rABdd8DLx8HR9l2zf9eGleWjnfaH34_k4ESkSIkmZLDfdZuDA038lXLrdgWtrIQM50uy_VnvGIOBMW5oyTvXYchOClSADELH5ro5iaxhgF4Nikh568VOwC-DVF1UZ39J5_5SX4er5KSamIaTh21UEDZ85MQBSPnvB9n7-gXB7q8MSrInj2aQ1jaWxjWiP9uCBNGll7ovyNVSkIb3cSfb1k4cLlrxmJNFYhry9eyi_j00hihI6LU1DYzk-uE4CRKJhcaIuFLNMlY6iV-MiDuP1qFjZR5K0qJ6EvZCqQX2dvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgqlfZy0gfkx4V51T_XgPo2AnCnlwAFrhr3_3B_ZcsKRx6pl4h4FeMgeu2qxI8G3H-XCLrdZrUZzog1zxJnjdYmRBZ9yqzbG4qk7_6uLMiwK6-VWxYwBClBq6Ddg2AeDw7VlE1upiW7vKUR_I261xXzCGLCrHTwGJrknqwmoGWcObX7QQzgfdx3YYo49mkjxMs31Py0sg1bhsdaXdOexZs-WP-RdBEjR2K6v_hb3LthWmv2vFsk4X5jtza0-ilSoJReg46U5gNZyVvnNzqprm0L4JPGssiz6rMu3mwSPj6uBUVh31gsU5GBCzGoKdW4ak2GerqtlFF7kJKTNziSATg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
زلزله‌ای شدید بخش‌هایی از کلیسای جامع "بانوی صور السالواتور" در شهر مانیزالس، کلمبیا را ویران کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/140970" target="_blank">📅 17:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140969">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtE4xG8Pt-Hstpg6beocUpfsyOGhIKORtlFzox1uJrsj2ByGr3zHuP-SbzgCVAhTYb-QfPlNFocc9_1OaXpTjL9mTsjgw1kyQcY5i5XHBt536pFcPsIk4I3yBurL6yN7b3AcqHj7N_PFsFjNi2xBUG0N1KTO9fkjizeUVNSlMSHAg1SEZCmczfQ1ojeIJy2j6iCyNnbJYo56cEGyqgYPO7t5aBGnPuszGb6luhw9-KeXtjRCZnwaMHRsaR92m679lWT9MGUs9ErPJmo2E0pWIqDPq5xZYcPhEXkNk8R4-zbeaDBQhyd-XQhcxFggB0bSb4NeGyeGfAVRciWzObzRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از صبح امروز تاکنون، هیچ کشتی‌ای از بخش عمانی تنگه هرمز عبور نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/140969" target="_blank">📅 16:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140967">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTWsfhKMFAHLb6iBfjva66rt4pq4omAPFiILmIhFJBw9_5cf7qIdZJf5UEhNwT1mycIzGcw--tyqKKS525JCeDfQnlfVtC3js9OfWy1P-DgWkRgQSBzHIGtUYtYHXq941p75SFvyjnLOzOcgRKKwJn02QIl0rloroqCsGVR3g1Hmuxcq5uT3Rs0MfL0YtjIYM2E_rChWCQK6dOcbAdQVGR_Igoo2DMZHReWAlgyJ1fv2B9_OooOBLDttNIAkDGObSXMWFVI7UWXj5GJSZKI2PRKbUOpYXW0z8PV9TfE7ja5eWktAcmcqADRqIGCzR9soD4Nt4nojTqijMi2teQSUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHZNf94Gb0qqlGoEvmai54mvP81f79KWd3XZvNN_Mwyv8HbJThW9DlITr-nlGHar2eaecH_loHynT9VlJ7qiWfLD8W1RJafZAscRIdKlGjzciFXyijLvrd805FrhFNdWw90Jt2a_QLk-4VDDHPoPB3xz2zFdZxfdyU0gqC0SwQN7DDDCE1YjxCgD0Xqm4Q8K99uPGAhgGzQwZrB6qi0H-SWc5KrmaTZoei3dT_aivossv4k1guafChKt7Q5P6Ktw4K4pKXSJna-YSEqmyh0q98yPnYAaey0ZkjU-A9_gtwBGYGuXYLMNfF_TBxRVSKP-abOUJKi8kvVk9lE6TqVSkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وضعیت کلمبیا
...
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140967" target="_blank">📅 16:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140963">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f74da9a2.mp4?token=TFtFsTH9fxhB9wqNjKyvKbuIkLali16Je3DDHFH7tUo2XBlK6KUys0Z_xvh7VkWjCTClvusiljoYQR66mIantuCGu8cVG_zaqDhRWpCSCEAu2MdCilHWwqkquJImTSAI61-6SF4HcdNbZdUM0eQemuwLG_Ounc_HXoyi4cl_DzWNfzp-I186lEBvLjLEvqgS6igaZ9jLSV08lnGZ5mW54AF6hg_EdbvYSVwQ-PVEYznWns3MSgN5_fCQnRVJTC9H7UO6pekXE44eCVx2s25bmm1t2zJDph1i1ofZEjAhehozoiXYElMHPKPRqBIFRxatD85fHzncTmARwCtA8ibspw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f74da9a2.mp4?token=TFtFsTH9fxhB9wqNjKyvKbuIkLali16Je3DDHFH7tUo2XBlK6KUys0Z_xvh7VkWjCTClvusiljoYQR66mIantuCGu8cVG_zaqDhRWpCSCEAu2MdCilHWwqkquJImTSAI61-6SF4HcdNbZdUM0eQemuwLG_Ounc_HXoyi4cl_DzWNfzp-I186lEBvLjLEvqgS6igaZ9jLSV08lnGZ5mW54AF6hg_EdbvYSVwQ-PVEYznWns3MSgN5_fCQnRVJTC9H7UO6pekXE44eCVx2s25bmm1t2zJDph1i1ofZEjAhehozoiXYElMHPKPRqBIFRxatD85fHzncTmARwCtA8ibspw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از زلزله 7 ریشتری کلمبیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140963" target="_blank">📅 16:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140962">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
فارس: از این به بعد خیار و گوجه شناسنامه می‌گیرند!
🔴
رئیس اتاق اصناف کشاورزی: «برای گلخانه‌ها و محصول‌شان شناسنامه صادر می‌شود.»
🔴
صاحبان گلخانه با مراجعه به سامانهٔ یکتا و تکمیل اطلاعات ابتدا برای گلخانه و سپس برای محصولشان شناسنامه می‌گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140962" target="_blank">📅 16:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140961">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
یک زلزله به قدرت 7.1 ریشتر در کلمبیا رخ داد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140961" target="_blank">📅 16:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beLI116lWfyOJ1DmSe9yAFF-_jgTC9UdGwC8EWoG9iidURn9HvH1KG5Ut_LhSSY58i1m7dSmpOGYXSY_xyUqEOQnJ6xfYNOcrllR7Sv0V5pR_1H_9QWmpqQh7o3gLd28WCsZU5OiuEJAk-cVnneQ4dUNe82zxgz2LoGkDQ2ILhWYbpZaaxr5BXL5VgoNFIJdsjUuNrRvyEzC4XIx37Z_v53po_QVzY95w9S1RF-SOlcBCSJtcSYJIvlf-ZQx2F2dFiy7qqydAGL7jOBIzTOWJpE1doAmaQKdDzl8adIm6i8DgIj4AZz9EfaxFh_gQC9YgHBQS44_njubJjQeXnvH5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش Financial Times: قطب شمال در حال تبدیل شدن به یک مسیر جایگزین برای حمل‌ونقل دریایی بین اروپا و آسیا است. کاهش یخ‌های دریایی باعث شده مسیرهای قطبی کوتاه‌تر و عبور از برخی گلوگاه‌های سنتی دریایی قابل‌دسترس‌تر شود.
🔴
شرکت کشتیرانی چینی Sea Legend قرار است این هفته نخستین سرویس منظم کانتینری خود را از نینگبو در شرق چین به فلیکس‌ستو در بریتانیا راه‌اندازی کند؛ مسیری که از راه دریایی شمالی روسیه عبور می‌کند.
🔴
این شرکت نام این سرویس را «جاده ابریشم یخی» (Ice Silk Road) گذاشته است.
🔴
طبق این گزارش، مسیر جدید می‌تواند زمان معمول سفر حدود ۴۰ روزه بین این دو بندر را، بسته به شرایط یخ، تقریباً به نصف کاهش دهد.
🔴
یکی از دلایل افزایش علاقه به این مسیر، تلاش شرکت‌های کشتیرانی برای دور زدن مناطق پرخطر و گلوگاه‌هایی مانند باب‌المندب و دریای سرخ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140960" target="_blank">📅 16:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140959">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فیلتر پلتفرم‌ها بدون تایید رییس جمهور ممنوع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140959" target="_blank">📅 16:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d09a4e0f1.mp4?token=KA8W_P3s26g0wcww3ipvRNfw6whqjrQ8WUbfyFskxTjuRlR2KbRDr6hQEMqA4zcjwLcVVVhvHBIh4QT4kmZ16ICi7C2hvx2lQKybYOqOf4HtHf-M0nwfQvI44JPWqHFwvDebIH4_j3dI73j3H7BFsowy5Yk2u7P7AZ42AyILZfqV2Dmu9OnUkzRBviKUjcFDGGcXJv-4My_nygtAzIzlTqS3XZi4dI_vTOqdc__xGYlFlTwM6Ss3sBeuo-VKXYwCYNr5IKSBBJKoCW2lfEWMwMjsg1v7_iszKJDu0IlXMHEqyIP_8SqAFql4YZ0vmFWAD2e3_zu-t2xriBS6KS7sqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d09a4e0f1.mp4?token=KA8W_P3s26g0wcww3ipvRNfw6whqjrQ8WUbfyFskxTjuRlR2KbRDr6hQEMqA4zcjwLcVVVhvHBIh4QT4kmZ16ICi7C2hvx2lQKybYOqOf4HtHf-M0nwfQvI44JPWqHFwvDebIH4_j3dI73j3H7BFsowy5Yk2u7P7AZ42AyILZfqV2Dmu9OnUkzRBviKUjcFDGGcXJv-4My_nygtAzIzlTqS3XZi4dI_vTOqdc__xGYlFlTwM6Ss3sBeuo-VKXYwCYNr5IKSBBJKoCW2lfEWMwMjsg1v7_iszKJDu0IlXMHEqyIP_8SqAFql4YZ0vmFWAD2e3_zu-t2xriBS6KS7sqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تایوان امروز برای نخستین‌بار یک مانور کاهش عمدی سرعت اینترنت موبایل برگزار کرد.
🔴
در جریان این مانور، سرعت اینترنت 4G و 5G در بخش‌هایی از مرکز تایوان به مدت ۳۰ دقیقه عمداً کاهش داده شد تا مقاومت شبکه‌های ارتباطی در شرایط بحرانی آزمایش شود.
🔴
هم‌زمان، آژیرهای حمله هوایی نیز در منطقه به صدا درآمدند و آمادگی غیرنظامیان و توانایی حفظ ارتباطات در شرایط اضطراری مورد آزمایش قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140958" target="_blank">📅 16:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140957">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGnMleCT8BZgNa-vJJEN7sWJy6BAiuCM_D4jQIowsL2kOTfS-Op1mhQREAw5fBLBEx4_6Cskb2KOEE7AIgtZhTf6QqMEWd5efmvbo7jnenTEalmTW0PjI9altBW-y8zxDJB_hQYqWvdAKDurm1elHfpSiOSvpt967tI6Ug4qRpZN_eGOqm2rwlZmp-sWQ8BJ0TsMFgXst3TT140--wd_Yjk6UJrt12Jjw55Xf3rCqaa_9uacrgoUYh9k8gzXWL2H6IQKkM7eMfy1a1p970jl7vmdFAg88ivHmn_qeh4Xxf_cidrbpn0wyAFpsOSW8M9cGloj4hAoFT-yxUXGULQm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اشراق: حماس پس از رد نقشه راه خلع سلاح توسط نتانیاهو، تماس‌های میانجی‌گری را تشدید کرد. این جنبش مصر، ترکیه و اعضای شورای صلح را به فشار بر اسرائیل برای اجرای توافق فراخواند.
🔴
مقامات انتظار دارند جلسه‌ای در قاهره با حضور مصر، قطر، ترکیه و ایالات متحده برگزار شود تا بر اجرای توافق فشار وارد کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140957" target="_blank">📅 16:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d393d66f2f.mp4?token=PrAqAECFxldO6Gyn6O3VNKWz6JG_pin9r-mK2DXmYe3e0a4VTAY5Bx7hIs-on7-vOVyxP3BqXegP5kQGhIazv9HkWYCSPQNUjd1ukhZ7ZwE8vc7raovuFxgLFIQnlnl3M4FdN1DNIn1ccHcCAmcFwj5Lu5FOUvMqJXVXNjLv_i8kQI5pGahbcW4DcIDk1MMzGvzakeAj9Ghvqi67nzGamGTJe9hxxWmHnw675qpyl6ZVlyLTTW7DSI2EBx9WKclhuB2eiCqspGGtvWMcBeUSiL0uCWy2OQKhWtc2nV6nx8wTwyusWr4kEH1PTSDov_RpxQhxJ1uwkJiJLMe8l8Z3JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d393d66f2f.mp4?token=PrAqAECFxldO6Gyn6O3VNKWz6JG_pin9r-mK2DXmYe3e0a4VTAY5Bx7hIs-on7-vOVyxP3BqXegP5kQGhIazv9HkWYCSPQNUjd1ukhZ7ZwE8vc7raovuFxgLFIQnlnl3M4FdN1DNIn1ccHcCAmcFwj5Lu5FOUvMqJXVXNjLv_i8kQI5pGahbcW4DcIDk1MMzGvzakeAj9Ghvqi67nzGamGTJe9hxxWmHnw675qpyl6ZVlyLTTW7DSI2EBx9WKclhuB2eiCqspGGtvWMcBeUSiL0uCWy2OQKhWtc2nV6nx8wTwyusWr4kEH1PTSDov_RpxQhxJ1uwkJiJLMe8l8Z3JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای عملیات ویژه گارد جداگانه یازدهم از گروه نیروهای «وستوک» یک چرخش نیروهای اوکراینی را مختل کردند و به تجهیزات نظامی اوکراینی حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140956" target="_blank">📅 15:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140955">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
دو جنگجو از نیروهای دفاعی شبوه در حملات گروه انصارالله (حوثی‌ها) که به مواضع آن‌ها در ناحیه بیحان، استان شبوه هدف قرار گرفت، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140955" target="_blank">📅 15:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140954">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رکنا،  اولین عکس از خانم بلاگر و ۵ همدستش در قتل حمیدرضا رجب زاده مداح تهرانی را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140954" target="_blank">📅 15:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140953">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hbz1W00XR47Pn8soCt5_NxNrkqycEE6gZDAYgJLZSvfu-wIwzKQwueuHqVl84qLPI1wsQ4lAhBDpQeRSYjt-icHSJWkp72zmIDKVPQOMWz0h74udwwnMg13-x-TibyMnT_ul7frzPjUB-faF9y1MfBDxKCbLnCJre74whF3EBFLWFRnH_H8gwIsWA9Rm7bRLFrbGl-Uuk0zoV8mAuYphFnX4WRo11mwwDmYP0DzarH877U8SaHUJutYuGDWDygUpxA2PZ1C0-b5XvFkYhG6AHHbwW150JZlS1Q4xOWhjDneswFOZR5poD65hu-C7sMtt_uk4M-T_fUU7NQAtVer2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رکنا،  اولین عکس از خانم بلاگر و ۵ همدستش در قتل حمیدرضا رجب زاده مداح تهرانی را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140953" target="_blank">📅 15:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140952">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سخنگوی سپاه، محبی : موشک‌های ایران دیگه فقط از یه نقطه شلیک نمی‌شن که همون مسیر رو برن و به یه نقطه دیگه برسند
🔴
می‌تونن وسط پرواز مسیرشون رو عوض کنن تا از پدافند دشمن عبور کنند
🔴
حتی بعضی موشک‌ها می‌تونن حین پرواز مسیرشون رو به سمت یه هدف ثانویه تغییر بدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140952" target="_blank">📅 15:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140951">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: «توافق مکه» ابزار تقابل نیست، بلکه بیانگر تعهد جمعی ما به صلح از طریق قدرت است
🔴
این توافق ماهیت دفاعی دارد و علیه هیچ کشوری نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140951" target="_blank">📅 15:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140950">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نقدعلی نماینده مجلس: قانون حجاب باید فورا ابلاغ بشه چون بی حجابی هم بخشی از پروژه دشمنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140950" target="_blank">📅 15:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140949">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
چین، هند را به خاطر تعیین رسمی نام برای ۲۷ نقطه در یک منطقه مرزی مورد مناقشه، محکوم کرد. این اقدام، تنش‌ها را در حالی افزایش داد که هر دو کشور تلاش می‌کنند روابط خود را پس از سال‌ها اختلاف مرزی، تثبیت کنند.
🔴
وزارت امور خارجه پکن، اقدام هند را "غیرقانونی و بی‌اعتبار" خواند و گفت که این اقدام نمی‌تواند ادعای چین مبنی بر اینکه "زانگان به چین تعلق دارد" را تغییر دهد.
🔴
زانگان، نامی است که چین برای ایالت آراونچال پرادش، که هند بر آن حکومت می‌کند، به کار می‌برد. پکن مدعی است که این ایالت بخشی از خاک چین است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140949" target="_blank">📅 15:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140948">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
عمان: نشت نفت از نفت‌کش «کارولین بیسنجی» در مساحتی به وسعت ۳۹۰ کیلومتر مربع گسترش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/140948" target="_blank">📅 15:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140947">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7a5d5e08.mp4?token=iDP_FBv3NGfvlu7TpY8GfVToMcpxRbQ-4Yt2Yv3nPAuiw4XEJpMfuMgdIFnoHAFMFsJgn6tXiSGiwiqB9Fcr6kGESKjWJhJMEBDhIuOrY3Vk6OKa6Aah2K-0ZLEQNjsLovFVacX4HYNklvyyDsaAOhWCn9r5Vdawx2kdK3U-F8DH90lO7nX1p-GQtahjJRlYU-uAfvWKiNBvKQykEjbaknqgYNzYHLfiko7t4D-PgJU3pJDJWrcZ8XI5vWXUnK7cymD1uxUhmyM-obsyOIwk2EOaLmUIfhkrBtlqpcXDF3HlxAt_rBezLLk0z0cavKbiKcVGekFR4GjGQqqVBxjJMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7a5d5e08.mp4?token=iDP_FBv3NGfvlu7TpY8GfVToMcpxRbQ-4Yt2Yv3nPAuiw4XEJpMfuMgdIFnoHAFMFsJgn6tXiSGiwiqB9Fcr6kGESKjWJhJMEBDhIuOrY3Vk6OKa6Aah2K-0ZLEQNjsLovFVacX4HYNklvyyDsaAOhWCn9r5Vdawx2kdK3U-F8DH90lO7nX1p-GQtahjJRlYU-uAfvWKiNBvKQykEjbaknqgYNzYHLfiko7t4D-PgJU3pJDJWrcZ8XI5vWXUnK7cymD1uxUhmyM-obsyOIwk2EOaLmUIfhkrBtlqpcXDF3HlxAt_rBezLLk0z0cavKbiKcVGekFR4GjGQqqVBxjJMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله توپخانه اسرائیل به منطقه «بنی‌حیان» در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140947" target="_blank">📅 15:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140946">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
الهام علی‌اف خطاب به پزشکیان: جمهوری آذربایجان در پی تحولات اخیر در منطقه نشان داد که در کنار ملت برادر ایران ایستاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140946" target="_blank">📅 15:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140945">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2DOdmdaQbUTkApYDSJnJ6pedb9txXy-o-euBqMq9Xdmo9_je-B9LRBw49IlfIka3ntMZkaJ1QMXY0gQjHjX9nnRk2qjFD0VlJBY0LhMwMIpoTXwfCYcMRjwGc_nSqdXxkVMyBoMvddtM4tH8OXBCBKMe4z4I4tKUPi-VY1eZAXYAdkNbYrUyGsLh82u5N_92YnyCIH5xYQmMzYwQamFdd1oUoeYL-v-yj9WidF9_C0SFSLijyb5Af6QzLvfH6VAQ7ND96kA_0TCZQIFLV5Q3IvjFu-7wIj13D7lc2duuBxCCxfY-NDMm1s0c-VIBwlzxKNuBpJQOyYYP0z4RwhNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهرداری تهران از آغاز خرید خانه های سانتی متری خبر داد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140945" target="_blank">📅 15:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140944">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فرمانداری سیریک: مهمات عمل‌نکرده در بندرکوهستک امروز به‌صورت کنترل‌شده امحا می‌شود و احتمال شنیده‌شدن صدای انفجار وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140944" target="_blank">📅 15:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140943">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
به گزارش بلومبرگ، شرکت ادنوک امارات در حال بررسی ساخت پایگاهی برای صادرات گاز طبیعی مایع در مسیری خارج از تنگه هرمز در ساحل شرقی این کشور است؛ زیرا جریان انتقال آن ماه‌هاست مختل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/140943" target="_blank">📅 15:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140942">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
واکنش بقایی به حرف ترامپ که گفته بود مذاکرات چراغ خاموش و مثل یه بازی شطرنج داره جلو میره: به هر حال چه چراغ خاموش و چه چراغ روشن، ایرانی‌ها شطرنج‌بازان مطرحی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140942" target="_blank">📅 14:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140941">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trXSok7Vc9XD9qLCjp9TwmMMUqFqV0FCqN8mxDlIrNJRLII1ScxKYloIuTQKnZxdMGTMyBMS2j6GDgc0ZeM1WP9VDYuAFvm3rIXbEcROKcN63CrWSaZAMYLjhRWAn4ekscHz1S1Ze41IglkIZdQYSz6H79i_oFrUkwEGQdl9OXLCtttYqOZeV-GVSIUbM0R9EsvpmRG18uOLy8_KQhBV3fEF4Lue1nzSAQ0RrjE6i9lla1fZJxZBo0IwrRThgnucUcQfvsD9uMeyqMvntur9jGz0l_07lV0hleW4_uI3hvlk7LgtQ1BAKgVSdkk0IDX4BOU2LxZ_y_TsJeQh2iBlvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جرجیا ملونی، نخست‌وزیر ایتالیا، در آستانه انتخابات که احتمالاً در بهار آینده برگزار خواهد شد، با افزایش چالش‌ها از جناح راست، لحن تندتری در مسائل مربوط به مهاجرت، امنیت مرزی و هویت ملی اتخاذ کرده است، به گزارش نشریه پولیتیکو
🔴
حزب "آینده ملی" که توسط ژنرال بازنشسته روبرتو واناکی اداره می‌شود، با کسب بیش از ۷ درصد آرا، تهدیدی برای جذب رای‌دهندگان سنتی جناح راست از ائتلاف ملونی محسوب می‌شود.
🔴
با وجود این مواضع داخلی سخت‌گیرانه‌تر، اختلاف اساسی بین ملونی و واناکی در سیاست خارجی همچنان وجود دارد: ملونی از اوکراین و ائتلاف‌های غربی ایتالیا به شدت حمایت می‌کند، در حالی که واناکی رویکردی ملایم‌تر نسبت به روسیه را ترجیح می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140941" target="_blank">📅 14:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88110a2e13.mp4?token=nYLt1HWv_OOiv_Qb90md76c3VuKTWgYpHWjms1hioZNOnitivVfrLPF7Yptz4M77JJ1H27ilGUpHOnsHq7Pa_-zfPIFry-_aOH2dk92ChiN8W9YwuMXeUj6BlNrpLLHNeBKBQi9-5wrX5KvAmwPsqNuhuhIUZEuhyakvg_41p4YI_9XtZyYNEx3IdeQ1neqhDS73AuaZzotK_JKPBdz7fuyy6gvfx-bCzlEuX4CR7q1ARYMpZ1JfGLaddCk5iloFTFCwWnP42_AmCRTDzXBROYuxgrKjV4a3baJEDDB7PvFNXAhW3fzWvuHm5ojDUQesP0VDN3PnCjBDA56jNF6KTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88110a2e13.mp4?token=nYLt1HWv_OOiv_Qb90md76c3VuKTWgYpHWjms1hioZNOnitivVfrLPF7Yptz4M77JJ1H27ilGUpHOnsHq7Pa_-zfPIFry-_aOH2dk92ChiN8W9YwuMXeUj6BlNrpLLHNeBKBQi9-5wrX5KvAmwPsqNuhuhIUZEuhyakvg_41p4YI_9XtZyYNEx3IdeQ1neqhDS73AuaZzotK_JKPBdz7fuyy6gvfx-bCzlEuX4CR7q1ARYMpZ1JfGLaddCk5iloFTFCwWnP42_AmCRTDzXBROYuxgrKjV4a3baJEDDB7PvFNXAhW3fzWvuHm5ojDUQesP0VDN3PnCjBDA56jNF6KTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دستگیری پزشک قلابی عمل‌های زیبایی در شهریار تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140940" target="_blank">📅 14:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
قیمت تتر امروز با کاهش، به ۱۸۵/۵۰۰ تومان رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140939" target="_blank">📅 14:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9flFYgJlWUotwrgdbk-FWlr88skvhJldhMglTmHioA8816Rq197DzFupPX9mBcoi5PLUUu7Km7HeIo69y-oSgtV62luY_A1v6h61wm-ddSLAlqe87_DEwg8f_VGUXJcTN0hy20j_CF7-8MuIH8-FBS_V_eUGjTduBUwVHI4eNFeLoJmNm-n09j5Dtd4jYW70rrCbQDHfZpEt72-WCiEZ-DrDdB_P1G5-2sW4kiZN0LV79yTEgyRbDZ9L_a3rj0hmGTr1i3_N3zvZe22N9a7ERm7L1A1eCJw9w9mlMcARLvYIRABxYGVg2eIURcrxwEHT6hFH4uj6V7Mrxu9i93-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گردنبندِ ایرانی «گردونه میترا» که در کاوش‌های باستان‌شناسی در کَلورَز گیلان پیدا شده است و دارای قدمت حدود ۳۰۰۰ ساله است. کَلوُرَز، یکی از روستاهای رستم‌آباد در گیلان است و در بخش مرکزی شهرستان رودبار قرار دارد.
🔴
این گردنبند طلایی زیبا دارای سه نمادِ سواستیکا است. و نشان از رواجِ کاربرد نمادِ سواستیکا در ایرانِ باستان دارد.
🔴
سواستیکا (卐 یا 卍) یا گردونه خورشید، یک واژه‌ی سانسکریت است که از دو پارِ "سو" به معنی "نیک" و "استی" به معنی "بودن" ، تشکل شده و معنای «هستی نیک» دارد؛ که در آئینِ مهر، نمادِ خورشید یا در آئینِ هندو نمادِ ایزدِ آفرینش است.
🔴
در فرهنگ هندواروپایی، کاربردِ این نشان بر روی اشیا برای خوش اقبالی و نیک بختی بوده است. استفاده از این نشانِ باستانی برای هزاران سال نه تنها در ایران، بلکه در یونان و سایر تمدن ها متداول بوده‌است.
🔴
متاسفانه به دلیل سوء استفاده حزب ناسیونال سوسیالیستِ آلمان، از نشان سواستیکا، به جایگاه این نماد صدمه زیادی وارد شده است و لازم است تا با جداکردن وجه والای این نمادِ باستانی ایرانی از جنایات حزب نازی آلمان در جنگ جهانی دوم، نشانِ سواستیکا را به عنوانِ یک میراثِ جهانی پس بگیریم و معنای والای آن را بازسازی کنیم.
🔴
این گردنبند باستانی در موزه ملی ایران نگهداری می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/140938" target="_blank">📅 14:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ ۵ میلیارد دلار ثروتمندتر شد
🔴
فوربس برآورد کرده ثروت خالص دونالد ترامپ تا ۸ اوت ۲۰۲۶ به حدود ۶.۵ میلیارد دلار رسیده؛ رقمی که در سال ۱۹۸۹ حدود ۱.۵ میلیارد دلار بود.
🔴
بخش مهمی از ثروت او همچنان از املاک می‌آید، اما در سال‌های اخیر رمزارزها، صدور مجوز بین‌المللی برند و دارایی‌هایی مانند مارئه‌لاگو سهم بیشتری در درآمدش پیدا کرده‌اند.
🔴
مسیر ثروت ترامپ بدون افت نبوده؛ او پس از بحران املاک و افزایش بدهی‌ها در سال ۱۹۹۰ از فهرست میلیاردرهای فوربس خارج شد، اما در ۱۹۹۷ دوباره به آن بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140937" target="_blank">📅 14:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frdQyD9orlFyF_hbQVBm7adog6CGhI-ATepOliwFudeuSGS7R8115PDM2fz9HNlzNPuYP_FFmoHMNzT_qR94zPcVSoMCDdjnoRO_jvq8bxwFc65P0dTMPZ5y0CMkmXD0TDlJle3rG2jMX_WOXqLsDUJQixl7dFG0RE6V4w5mjSJurKrFxZTEMKpjIrZT-RaGeXdmQJ_SKPq0sdKjKz_UM0Ju2gB_8N1auVL8RQ3LUtPDK7xjlTZ5gJ7IE2U9i7ZC2IAS-aUil_0VWNaRcUgb3c6o3qAKx97AMD-bWHZ7CTjvrFLWD1a9FymoGKsmKWHJpFgFyNJd6_Q0V3dJuO24IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات سایبری گسترده به بخش های هواپیمایی، انرژی و آموزش کشور امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140936" target="_blank">📅 14:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏
👈
پزشکیان:  در موضوع بنزین نمی‌توانم دستور بدهم که از فردا فلان اتفاق بیفتد؛ چون ممکن است کشور را دچار مشکل کنیم.
🔴
باید هم در داخل دولت و هم خارج از دولت با دستگاه‌ها و مجموعه‌های مختلف گفت‌وگو کنیم، دغدغه‌های آنها را بدانیم، آنها نیز دغدغه‌های ما را بدانند و در نهایت به یک راه‌حل مشترک برسیم.
🔴
ما تازه به یک تصمیم رسیده بودیم و می‌خواستیم آن را اجرا کنیم که موضوع استیضاح وزرا مطرح شد. اگر وزیر دیگری می‌آمد، دوباره باید با او می‌نشستیم، گفت‌وگو می‌کردیم، مسائل را توضیح می‌دادیم و به زبان مشترک می‌رسیدیم.
🔴
در این صورت، عملاً زمان دولت برای اقدام و اجرا از بین می‌رفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140935" target="_blank">📅 14:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
پزشکیان:  چین و روسیه در مجامع بین‌المللی از ظرفیت خود استفاده کرده‌اند و در مواردی قطعنامه‌ها را وتو کرده‌اند.
🔴
حتی در رابطه با قطعنامه‌های مربوط به تنگه هرمز نیز مواضعی اتخاذ شده است.
🔴
در مجموع، تا جایی که آنها امکان دارند و ما نیز می‌توانیم، در حال تعامل و استفاده از ظرفیت‌های موجود هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140934" target="_blank">📅 14:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رئیس جمهور:  حجم مبادلات ما با پاکستان در حال افزایش است و از حدود سه میلیارد به سمت ۱۰ میلیارد در حال ارتقا است.
🔴
ارتباطی که اکنون شکل گرفته، استثنایی است و قرار است این روند نیز تقویت شود.
🔴
ما اختیار داده‌ایم و اجازه داده‌ایم که دستگاه‌های مختلف مستقیماً با کشورهای همسایه ارتباط داشته باشند و آنها نیز این کار را انجام می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140933" target="_blank">📅 14:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزیر ارتباطات درباره خبر «ضریب دار کردن» اینترنت: این موضوع خط قرمز منه اگه این فرضیه اثبات بشه، شخصا برخورد جدی با اون اپراتور می‌کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/140932" target="_blank">📅 14:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAhW_rbLe5dHYByzn5wGYMGIt40Z0d7bdFIwBO2okh9Ij7TAOc3nyM3Qr0VEh6kpztHMQ_LqcTWccGVfwgPeuglj9yB7jaHJ5CX5PzQqFr3QX99XaTVyxGgrqtXJmUk1tjqn-_wK8p0krOrVacGErO1RmBXcphPpUw8fxHSFkT9arR46w1KfEmHn5gcP-wybLUrRCgIxjXQN3O3DimCLxgmGQGy-eci4M0Q8cUPLLrFc62tzyC8lFJyM3gvs52flE3XLzzgxmXkr29BE7To1LF7W_z8iUp5VZddR6UmJ5IYaei-acAtcN242ZOHCikow4NbtQNolQnJBAu5Jm3rIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین : یه سامانه جنگ الکترونیک ضد استارلینک روسی رو زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140931" target="_blank">📅 14:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سخنگوی دولت عراق: «ما از بمباران مقرهای حشد الشعبی توسط عربستان و آمریکا اطلاعی نداشتیم و یادداشتی را به شورای امنیت سازمان ملل ارائه خواهیم کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140930" target="_blank">📅 14:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140929">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
پسر اسماعیل خطیب: بابام ۴ بار از ترور در رفت، ولی بار پنجم دیگه نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140929" target="_blank">📅 13:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در پاکدشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140928" target="_blank">📅 13:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از یک مقام آمریکایی گزارش داد که ایالات متحده قصد دارد پس از دستیابی به توافقی برای از سرگیری تردد بدون مانع کشتی‌ها در تنگه هرمز، محاصره بنادر ایران را لغو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/140927" target="_blank">📅 13:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140926">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بلومبرگ: دونالد ترامپ، رئیس جمهور آمریکا، مدعی شد که آماده است به جای حمله نظامی جدید، اجازه دهد فشار اقتصادی بر ایران افزایش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140926" target="_blank">📅 13:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/005fed10cc.mp4?token=b6VJiXJt7dkHYhG4myOs-Z_48HQwrgP9478hyep4hLMMLx6uV70Lk5jOVe_-oPzIDMQ-LPhEQ-t1saOMXDRDkqs2xVKSwJQmaSOdj4F9yvwMvi8tCmzC5RY9gmjZ2PhNj-WRzqFuMm2ggvkSY-dOCm-zZ0xixmHzh103kp7Yu9_f2JNTr9olQm3DviQfL-HHSd6NQL93gz4Xsrig6_2JL3yRgYQVx0iYge_diVSlQMESUznK2Udyo4eWnzEiir8PKZJCsatgWH_V-k8N_wfeN5v0gRbbWYizYcmKcl-zTjET1QKErgAh5yqx1gySB7dB_0gBI0kQ30uzUKJdZflwrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/005fed10cc.mp4?token=b6VJiXJt7dkHYhG4myOs-Z_48HQwrgP9478hyep4hLMMLx6uV70Lk5jOVe_-oPzIDMQ-LPhEQ-t1saOMXDRDkqs2xVKSwJQmaSOdj4F9yvwMvi8tCmzC5RY9gmjZ2PhNj-WRzqFuMm2ggvkSY-dOCm-zZ0xixmHzh103kp7Yu9_f2JNTr9olQm3DviQfL-HHSd6NQL93gz4Xsrig6_2JL3yRgYQVx0iYge_diVSlQMESUznK2Udyo4eWnzEiir8PKZJCsatgWH_V-k8N_wfeN5v0gRbbWYizYcmKcl-zTjET1QKErgAh5yqx1gySB7dB_0gBI0kQ30uzUKJdZflwrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صبح امروز و برای بار اول پس از سقوط بشار اسد، جنگنده‌های Su-22 نیروی هوایی سوریه بر فراز مناطقی از جمله ادلب پرواز کردند.
🔴
غیر از هواپیماهای آموزشی-رزمی L-39، این جنگنده‌ها نخستین هواگردهای بال ثابت مسلحی هستند که در دوره دولت جدید سوریه عملیاتی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/140925" target="_blank">📅 13:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140924">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
الجزیره: ممکن است که ترامپ به حامیان خود بگوید «دیگر نیازی به حمایت از اسرائیل نیست»
🔴
الجزیره نوشت: ترامپ در چند مصاحبه اخیر گفته است: «اسرائیلی‌ها به من احترام می‌گذارند و کاری را که می‌گویم انجام می‌دهند» و «من تصمیم می‌گیرم، نتانیاهو تصمیم نمی‌گیرد.» بنابراین ترامپ در واکنش به رد طرح صلح غزه از سوی نتانیاهو، می‌تواند دست به اقدام بزند و به حامیانش بگوید که دیگر نیازی نیست از اسرائیل حمایت کنند. او تقریباً کنترل کاملی بر پایگاه سیاسی ماگا و جمهوری‌خواهان در کنگره دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/140924" target="_blank">📅 13:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140923">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
نیویورک‌تایمز: تنگه هرمز به «شمشیر داموکلس ایران بر فراز سر ترامپ» تبدیل شده
🔴
مقام‌های ایرانی نگرانند که اگر تنگه باز شود، ترامپ بدون اینکه احساس کند نیازی به حل و فصل این بحران دارد، از آن خارج شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140923" target="_blank">📅 13:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140922">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEXFp7EI5F_uRdzkYY_oJWymowywvitMWtSRiCAiVm1n0gAhcfjVzJIHABS4kykODaqq90Nfk-iAs4sB9nzgLgMlkYthCgZC49W20T3OQO5aZM2FfE698Uz-Yg6j3AFhiDJ9Nvx9dkWCu499M8n4Db65JP78yae3TYWuvZotA6EADKAIhYdXOrL7i1vYoUpZLUX0nLT1IKp8fj5JMVD3TPjCwRPhEGLO-FYnaxxugSiAGu8zkAK2Ft-RmDFnRnr1ByXOZjkbLTk1xSy3JIdTpgM-zF6RE763mwpoYXpYem8MzsxUJh6-7fsU5pkqkjg8lbMDN5kUVbclj4WHGw9BlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۹۴ هزار واحدی شاخص بورس
🔴
شاخص کل بورس با رشد ۹۴ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۶۵۴ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140922" target="_blank">📅 13:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140921">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نایب رئیس مجلس: بازگشایی تنگه هرمز هیچ راه‌حل نظامی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/140921" target="_blank">📅 13:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل:  کاتز، ویدئویی منتشر کرده که توش اسرائیل چند کشور رو بمبارون می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/140920" target="_blank">📅 13:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_AWk9KPBvg8kwAhrCyGclvnnvN9qBI7DFd387pa6B01O1fRMsbHJu6BgCr0SSJ14yzubcFVqaplKofofzWA-gQqB7X8G66Wiwk2sxFWkl6MLm5buS8KTak9hL7Vwov1GhLphhGE-M7DEAxlcm25GeLXw5LBKAt0FwFSF5d1GGXZHjZgSWltym9uQNSY1j1g6UtQaKUwKoWDScZDv-3E35H76NKWB_RDAD4WOUvxrO1XgFOQbV0V5XUF2qHkkcRC9-SDltFYckQ5zeJHTU4uBA1PstuqZxLsOyyC1AJY5Hsy7DVG2ESNL3L_T6dg79H27MDl_4bvno1C0RiYJVLiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور داخلی عراق: تمامی سلاح ها باید به دولت تحویل داده شود و از این به بعد هر کسی بدون مجوز دولت، پهپاد به پرواز دربیاورد، به عنوان تروریست با او برخورد می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140919" target="_blank">📅 13:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140918">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
۶۳ نماینده مجلس به توسعه اختیارات رئیس‌جمهور در فضای مجازی اعتراض کردند
🔴
طبق این اعتراض رئیس جمهور نمی‌تواند هروقت که خواست به قطعی اینترنت پایان دهد و یا برنامه ایی را رفع فیلتر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/140918" target="_blank">📅 13:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140917">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مایک والتز، سفیر آمریکا در سازمان ملل: ایران بیشتر از اینکه هز وزیر جنگ آمریکا بترسد، از وزیر خزانه داری آمریکا می ترسد، چون او کسی هست که آنها را تحریم می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140917" target="_blank">📅 12:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140916">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3eecf6773.mp4?token=de0kRoNIwwjNhTWwpXboz7XIba3MeDbXkfdtiCixEnqOW5ViKvwZO3ulIAG0fWqBnhJyLZt3Wu1NO_U4vQieEbyt8zQxtVZ7fp9Cck0aBBMcauaOLcIG_qAb44LsaZ_0f1xAnrRIai56RFxHnpIT5Vdl9dSCDERX_kc-S7Db7Bpb1w4r492Ia0lC1deW8q01b1UC9Xwe9scHcc0VqCD5kfroICvhacQm9QboIkrhOccBvAAa6wXV6kwbbGYvuAVRo8fTwflLGxk5Xd8GKpZHCU-i3OCcGX3j5pgxXweu7RbV1ht0UzCzGDZy2qKuoph49ECi6TRBV7iFo_RZ16Sj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3eecf6773.mp4?token=de0kRoNIwwjNhTWwpXboz7XIba3MeDbXkfdtiCixEnqOW5ViKvwZO3ulIAG0fWqBnhJyLZt3Wu1NO_U4vQieEbyt8zQxtVZ7fp9Cck0aBBMcauaOLcIG_qAb44LsaZ_0f1xAnrRIai56RFxHnpIT5Vdl9dSCDERX_kc-S7Db7Bpb1w4r492Ia0lC1deW8q01b1UC9Xwe9scHcc0VqCD5kfroICvhacQm9QboIkrhOccBvAAa6wXV6kwbbGYvuAVRo8fTwflLGxk5Xd8GKpZHCU-i3OCcGX3j5pgxXweu7RbV1ht0UzCzGDZy2qKuoph49ECi6TRBV7iFo_RZ16Sj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدیر عامل شرکت توزیع برق: به ازای کشف هر ماینر ۳ میلیون تومان جایزه دریافت کنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140916" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140915">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd3d7d8977.mp4?token=Y5rg4gUOxJGxo3Yps8c7P1cjTwQpWUHOb2pFb4pmMara45B3TllA0Z1XolINtGAUCzzlmuDoEaLJiVPshsTpgohSdVa8jxBFefqQLFHvvlk2jJsHdSN_G6k5fZdqE__gehcwX7jGdk1mCZm0kCDvGsJurCzdhn0Y2SUy6aVXYGztW3Zqv2v_AydDQF4dTaSL6WP1FFl1e7heFR9RGTmJKy_Qvi5dHsln2ZP2ErtdtfAG6EIivh6S1_f7d2aHchSfsOD7U2zQdBLuO6Bte_dR5TJYL1hDaTncI2yKfT_JbhXC_nl4eZyUrahWYZ6xKB6w4stZ2ymBWmKVLJ_F0rF27A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd3d7d8977.mp4?token=Y5rg4gUOxJGxo3Yps8c7P1cjTwQpWUHOb2pFb4pmMara45B3TllA0Z1XolINtGAUCzzlmuDoEaLJiVPshsTpgohSdVa8jxBFefqQLFHvvlk2jJsHdSN_G6k5fZdqE__gehcwX7jGdk1mCZm0kCDvGsJurCzdhn0Y2SUy6aVXYGztW3Zqv2v_AydDQF4dTaSL6WP1FFl1e7heFR9RGTmJKy_Qvi5dHsln2ZP2ErtdtfAG6EIivh6S1_f7d2aHchSfsOD7U2zQdBLuO6Bte_dR5TJYL1hDaTncI2yKfT_JbhXC_nl4eZyUrahWYZ6xKB6w4stZ2ymBWmKVLJ_F0rF27A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برگزاری مراسم اربعین در لندن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/140915" target="_blank">📅 12:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140914">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a8c9073a.mp4?token=PavfA8qzgajI7iA6T2ZhHgBXvCj0TIsdhqOINYiT162JtS74v4MwVyY3H0KDuzf6LNVs_B7tHJvdvljYoBPDmx92G5weZovAlV0ESM9wL-RCE-NNjvaLDY2cTbjinwTmXjUgrwO9xOxf1ETcfQk7rOevSy0oBAtYY_mdnMbn2jPXIkRuypfzFJxDSjodRHLH5WpYSzNeWdepTV91CcDaHDGl7qdWEIajOlCcbjgmzpx1IyLex3V7xGGc7_hwg8Got7gDge1l37E1APuKsSVj6YoKEn--E6lK3ydteDahUsym7QZf5cwvszUw3VHkCTKCDyocKuBQNOYeTFQvSJE7Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a8c9073a.mp4?token=PavfA8qzgajI7iA6T2ZhHgBXvCj0TIsdhqOINYiT162JtS74v4MwVyY3H0KDuzf6LNVs_B7tHJvdvljYoBPDmx92G5weZovAlV0ESM9wL-RCE-NNjvaLDY2cTbjinwTmXjUgrwO9xOxf1ETcfQk7rOevSy0oBAtYY_mdnMbn2jPXIkRuypfzFJxDSjodRHLH5WpYSzNeWdepTV91CcDaHDGl7qdWEIajOlCcbjgmzpx1IyLex3V7xGGc7_hwg8Got7gDge1l37E1APuKsSVj6YoKEn--E6lK3ydteDahUsym7QZf5cwvszUw3VHkCTKCDyocKuBQNOYeTFQvSJE7Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجید شاکری، مشاور قالیباف: ترامپ با ما توافق نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/140914" target="_blank">📅 12:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140913">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رئیس سازمان هواشناسی: احتمال وقوع پیوستن پیش بینی ها تا این لحظه ۷۰ درصد است.
🔴
بارش و ترسالی احتمالی سال آینده نمی تواند خشکسالی چند سال گذشته و کمبود منابع آبی را جبران کند.
🔴
مردم خبرها را از مراجع رسمی اطلاع رسانی پیگیری کنند، خیلی از پیش بینی های منتشر شده در فضای مجازی قابل اعتماد نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/140913" target="_blank">📅 12:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140912">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بقائی: ادعای نتانیاهو درباره ماهیت برنامه هسته‌ای ایران دروغ‌پردازی است/ ادعای بمب هسته‌ای ایران دروغی ۳۰ ساله است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/140912" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140911">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6c2ee8a2.mp4?token=tt2aC4x4DqytTLMmBCPcaVYO1eR7huIWnT-5WU2TUPKHJV8boNXMU6kEdRrq4jogp_aXICKpFOa4GNfiOiX75nADAeeEzg1YHBgOPn9hY2L152hgec_HPdFTsrWUbJMp_d-ijAwu3B7sK4QNJHACmmrVZf1y5Rq9B40NYQmSZQe4CTnHoTiu1pGOFmqs0f9wfexEZuzGWE8GATm6fV9KJCLsj1eCh5Bljt4OHXhpXGh6viYbYufgk9xonLTpP1eTT4Ofwe8lNACN_pqlyB4DG43UV-RN_j8ShZDiXlud7GkBGgg8kLldctSoil59tnkrOERgFKSSl2cXKZeGi-grpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6c2ee8a2.mp4?token=tt2aC4x4DqytTLMmBCPcaVYO1eR7huIWnT-5WU2TUPKHJV8boNXMU6kEdRrq4jogp_aXICKpFOa4GNfiOiX75nADAeeEzg1YHBgOPn9hY2L152hgec_HPdFTsrWUbJMp_d-ijAwu3B7sK4QNJHACmmrVZf1y5Rq9B40NYQmSZQe4CTnHoTiu1pGOFmqs0f9wfexEZuzGWE8GATm6fV9KJCLsj1eCh5Bljt4OHXhpXGh6viYbYufgk9xonLTpP1eTT4Ofwe8lNACN_pqlyB4DG43UV-RN_j8ShZDiXlud7GkBGgg8kLldctSoil59tnkrOERgFKSSl2cXKZeGi-grpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تراکم کشتی‌ها در تنگه هرمز کاهش یافته است، به طوری که تنها ۶ کشتی در ۹ آگوست از این تنگه عبور کردند، و بیشتر آن‌ها از مسیر مشخص‌شده توسط ایران استفاده کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140911" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140910">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: رفع وضعیت تنگه هرمز مستلزم جبران همه نقض‌های یادداشت تفاهم است که آمریکا در حال انجام آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/140910" target="_blank">📅 12:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140909">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-Pm9N2kEw_AEC8NZ7Ap3aXfexAqBJzhjqWT0rexccaRO4Dq4DB3ze5YZC1rntWnl-jQ66nBStriZZ0Af2eRUlmkAk-Bd0g4engikAwa4bdwP2oT9lx35VZ390y11JmHc-ZXGWIU__Sm0FgBeYx0UgxlVruwHQ_vHiG1SxkwhnGnrZUHUvnr7SmUxynWTN3Nzvt83T4gcdST_rjOAQ9b-Wlb5a2hvuH7Cl_CNH4eIXkiw5knpNMuofB2VisP4_VRfdL6aWqyKH5oLdE-xRu0Fvdaek4HeU2EanCie0a6b37ngww9SR25qMtHJRixhlXdKmwOoKz6Mz7Gqr2q0M8sVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: ۱۳ میلیارد دلار خسارت، صورت‌حساب سنگین حملات ایران برای آمریکا
🔴
از آغاز عملیات «خشم حماسی»، ایران بیش از ۲۰۰۰ حمله هوایی، موشکی و پهپادی به پایگاه‌های آمریکا انجام داده و به ۲۰ سایت در ۸ کشور آسیب زده است. خسارت وارده به تجهیزات و تأسیسات آمریکا ۱۳ میلیارد دلار و ۴۲ هواپیما منهدم یا آسیب دیده است.
🔴
با این حال، آمریکا آمادگی کافی برای دفاع از پایگاه‌های خود را ندارد. گزینه پیش روی کنگره و پنتاگون روشن است: یا حالا برای حفاظت هزینه کنند، یا در آینده با مشکل جدی‌تری روبرو شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140909" target="_blank">📅 12:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140908">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXlkQ4JvGi0v7jcWr_tK0qUlwoHRbAxJJo9kRIZx8pVEGLAw7mj9siz5wPSGpZQU6JjNDxjtASmooW00wF77iKT9ylB0XlmFeDhuf7coL1PnmC7kzeRqJRGT6Rt0Xazrsys1OangnCQo5ZSewYBqXYlKz_x9y1QWKkWCp8P2aNVi4JW1toQJwCuLGEZ484NerZNMm6duQHJXdAm4PWuOnuw8BsNmj5yMBS5vaH1InT-uys4KFRmNRZAbiT3TYceUFJf46rzr5zA-kggpnOlbpAKPbvgwKpPBWLceqJ8rLa51CzhBOjGvOqiFMMEu5oN9Fl0UAdXcG1Kxl-xPG6tGqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور محمود احمدی‌نژاد در جلسه دیروز مجمع تشخیص مصلحت نظام
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140908" target="_blank">📅 12:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140907">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: به هیچ گزارشی، چه مثبت و چه منفی، در مورد میزان توانمندی نظامی آمریکا اعتبار نمی‌دهیم
🔴
موضوع مهم برای ایران حفظ آمادگی خود در بالاترین سطح است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140907" target="_blank">📅 12:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140906">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سی‌ان‌ان: شروط ایران برای بازگشایی تنگه هرمز قیمت نفت را افزایش داد؛ برنت به ۸۴.۵۸ و نفت آمریکا به ۷۹.۲۸ دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140906" target="_blank">📅 12:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140905">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی گفت به کانال ۱۲: هیچ شانسی وجود نداره که ما اجازه بدیم قطر و ترکیه به عملکرد ما تو غزه نظارت داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140905" target="_blank">📅 12:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140904">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=rHkaDW1Q9rHbXeEA2aVdCx_TEdGeFxJA0l2KyhYkA7g4vmH0HKziEyAoTBwZUCB1IlyxuAWB9K5Y3PyC4gfm6CzmQhM-vZdeRcEvMhHLRFp94hYOE8yYJ90yIjE_Nmgxcbxq05SV2trKPOSnMcOAcuMI4ZT4ziV5CC1jOzi4F_FECylObeG9zuiuX3Yc_5blNMa0cKfk5XlSGg_xA7SGSrem0dQP8bUEZhg_xyX6gaEUZzqnnBiU3-YMqRUg4gLEaFy0--jnqJl5HpxcS5no5zh3uwOf0x71h1ALQgj8qv0c6ZzBLRyWt7VBJUkmSv5CG-oLB-R4PwDpr16CZ4i4VmbUfMmBVLJ0Bnxlu4SmaSZmfV56qvxAJa-4SWO0edJ4GdvuJJCpE4lSeTNoOIrhDAn1sKGGvtLM_JDDSCgfGmFLCuztoHhRB397FettmRp8rlUU1ZfmqPssbfSnlopGaDTH5gNkdec_lj5rC61-CpK-wNnEsWA9NbOgwG-pshPi3KRGiizWK0sBhxHwURFdEMWzZoxXeP3a5Bss0d_SnXAmAWEKfKFnB9iMIQ-b1D7BCFT3XHPdyM9f2CmzZu2nsULA9Q08RvWSPEKcN08dMckkI6JzPo3UDpQFarKK7-Fez0-jkGHRSMd8B_aPz4VIR2ulsWYmkHqZKszkYXwh6cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=rHkaDW1Q9rHbXeEA2aVdCx_TEdGeFxJA0l2KyhYkA7g4vmH0HKziEyAoTBwZUCB1IlyxuAWB9K5Y3PyC4gfm6CzmQhM-vZdeRcEvMhHLRFp94hYOE8yYJ90yIjE_Nmgxcbxq05SV2trKPOSnMcOAcuMI4ZT4ziV5CC1jOzi4F_FECylObeG9zuiuX3Yc_5blNMa0cKfk5XlSGg_xA7SGSrem0dQP8bUEZhg_xyX6gaEUZzqnnBiU3-YMqRUg4gLEaFy0--jnqJl5HpxcS5no5zh3uwOf0x71h1ALQgj8qv0c6ZzBLRyWt7VBJUkmSv5CG-oLB-R4PwDpr16CZ4i4VmbUfMmBVLJ0Bnxlu4SmaSZmfV56qvxAJa-4SWO0edJ4GdvuJJCpE4lSeTNoOIrhDAn1sKGGvtLM_JDDSCgfGmFLCuztoHhRB397FettmRp8rlUU1ZfmqPssbfSnlopGaDTH5gNkdec_lj5rC61-CpK-wNnEsWA9NbOgwG-pshPi3KRGiizWK0sBhxHwURFdEMWzZoxXeP3a5Bss0d_SnXAmAWEKfKFnB9iMIQ-b1D7BCFT3XHPdyM9f2CmzZu2nsULA9Q08RvWSPEKcN08dMckkI6JzPo3UDpQFarKK7-Fez0-jkGHRSMd8B_aPz4VIR2ulsWYmkHqZKszkYXwh6cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: تنگه هرمز از زمان حضرت آدم تا 9 اسفند 1404 باز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140904" target="_blank">📅 11:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140903">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7feda1ed7d.mp4?token=GYNDuCtq0C9OY9LcDCHDFoGELk_iqM5x_kFu9TR8yO5vr2nBaJ-zBOTYgKI0m1-c9cZyO8kUOgBb4Tok7X2PEyczNEu6iCECsbrXETDo1118PfoOJKauYt9qmo4hiyehpeQsczHExUFzq_VBFp-79vhcQn0EoU0Wbe8fkNvu1j4rwOOHnGnSmsiC1tLFgXOT3xgnzZSqY8x1xlKJyl__0eclZti9iyRbdXehFA_D_KJ4OoWUZxHkYcUYQHNOtNplIhWcr5_kEJqu1GYHM2VsCoiJzhx-sCOfCpm-Gshx1Ar-GeFpzADSAlNX8egfdJ-LDDxNeLiS4oDE15w06ZTwcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7feda1ed7d.mp4?token=GYNDuCtq0C9OY9LcDCHDFoGELk_iqM5x_kFu9TR8yO5vr2nBaJ-zBOTYgKI0m1-c9cZyO8kUOgBb4Tok7X2PEyczNEu6iCECsbrXETDo1118PfoOJKauYt9qmo4hiyehpeQsczHExUFzq_VBFp-79vhcQn0EoU0Wbe8fkNvu1j4rwOOHnGnSmsiC1tLFgXOT3xgnzZSqY8x1xlKJyl__0eclZti9iyRbdXehFA_D_KJ4OoWUZxHkYcUYQHNOtNplIhWcr5_kEJqu1GYHM2VsCoiJzhx-sCOfCpm-Gshx1Ar-GeFpzADSAlNX8egfdJ-LDDxNeLiS4oDE15w06ZTwcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی در پاسخ به ترامپ که گفته بود «داریم با ایران چراغ خاموش پیش می‌رویم و مثل بازی شطرنج است»: چه چراغ خاموش و چه چراغ روشن؛ ایرانیان نشان داده‌اند که شطرنج‌بازانی حرفه‌ای هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140903" target="_blank">📅 11:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140902">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: دعوت‌نامه‌ای برای سفر آقایان عراقچی و قالیباف برای سفر به پاکستان واصل شده و هر وقت که زمینه مناسب باشد این سفر انجام خواهد شد.
🔴
اوکراین باید اقداماتش علیه ایران را جبران کند در غیر این صورت ما جبران خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140902" target="_blank">📅 11:43 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
