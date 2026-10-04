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
<img src="https://cdn4.telesco.pe/file/Z5P0Rgbq6jBZCK3Y3sNxSfo0pwNkRda6IAY61ySDJd2Oomd3KaMMbvalNPD1_liIuTZYsSkk0P8zSQbwWlip0RwXSJ_3XJ5B_q0YiHVlxXhLKXstFxmptKrhIYAm9O52AWsxZmElfXXKaoMu1Ph1kWVjy2jve_n-J7Y7e5fI83ujI2a5_Y-SjXXhwg99HhJdB4Ivs4GJ88a4UabL0biuBJpvSTbFgx4ErrzY0s7LYIQhfpW8RZ8Li8ueSFu0JYeIi3484mFT5uJE7HyKhfEyMgjgV_8A3N7hxTAQl-Tv4aPrFW7YIkKIJqh7vCNC5S32YzglLZDHaDWy_xT9CRWXHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 20:42:00</div>
<hr>

<div class="tg-post" id="msg-150972">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزیر نفت استعفا داد
🔴
بورد سرپرست وزارت نفت شد
🔴
«طباطبایی» معاون دفتر پزشکیان: با پذیرش استعفای محسن پاک نژاد طی حکمی از سوی دکتر پزشکیان رئیس جمهور، حمید بورد به عنوان سرپرست وزارت نفت منصوب شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/alonews/150972" target="_blank">📅 20:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150971">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ایال زمیر: باید آماده یه جنگ غافلگیرکننده باشیم
🔴
رئیس ستاد ارتش اسرائیل می‌گه که باید خودمون رو به آمادگی کامل برسونیم چون ممکنه هر لحظه یه جنگ ناگهانی شروع بشه. این حرف‌ها در حالیه که تنش تو منطقه هر روز بیشتر می‌شه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/150971" target="_blank">📅 20:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150970">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XauByKVdNVQfYrLp4vSjNKva4GrUwvk7IMw1t2yjA59GgHIBveZMbZoQ6Alnh6NVjaTGcR9yrKtpvXphPj52JUI4uOWuRrXNt11phgW4l2b2JuRDq7zbOpk40kK22iFCJXdvDfnSs9CZQ4L_tbK2ccHIlnyAfzGu7irJPCzTMmFOqyri0ftkBoedP_Zyid-s01jrOrneXXHXmfKkUO4KvRosy9OUoGSvIO7gTjki5ebqfuWBp-RwuUV5QGj-9lw3zraBHVvzf7_60f39n1vdy1cuYZp3qOsO6V2ltHbtSft9QDCCKRGplWgMMPfdp4P-IvQiqO8k1YPgAmAMUTAwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاید باورتون نشه ولی نتانیاهو تو اسرائیل میانه رو حساب میشه و رقیب های انتخاباتی و قشر تندرو بهش میگن زیادی به فلسطین و ایران آسون میگیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/150970" target="_blank">📅 20:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150969">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d8f4fd4a.mp4?token=Lxu9CX7bhPMINCTgXQVTY2NeeZEoGSqgRUI_uY50Ax1Jt2puxoFQ4VN9CjUipY84Y1dRQARqt9WqA6HQt34Q2rnxHSMF_kLP8bf10h9QNpQgvlxBjM1TyNuK5byeSv5noFqxayx9vlU8gAdMEaajJuC9svzh1CzKd3VUuXBxMB0_CWJmTfVjhfDHnbBF9joWMsD-Pz7jYWTQBlydq9W4sd2sRSLOgEhacwqWyHCHCkZFIkSZMH8nzQCaqqQD9OjewwCrl5jFUR4zdx1KN68ujIj3ncBhl4oVaWL8bkiIIX27UDsgC2DSvFb--TVQPyn9I0a4JBoXh-vfMwX2OGFKuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d8f4fd4a.mp4?token=Lxu9CX7bhPMINCTgXQVTY2NeeZEoGSqgRUI_uY50Ax1Jt2puxoFQ4VN9CjUipY84Y1dRQARqt9WqA6HQt34Q2rnxHSMF_kLP8bf10h9QNpQgvlxBjM1TyNuK5byeSv5noFqxayx9vlU8gAdMEaajJuC9svzh1CzKd3VUuXBxMB0_CWJmTfVjhfDHnbBF9joWMsD-Pz7jYWTQBlydq9W4sd2sRSLOgEhacwqWyHCHCkZFIkSZMH8nzQCaqqQD9OjewwCrl5jFUR4zdx1KN68ujIj3ncBhl4oVaWL8bkiIIX27UDsgC2DSvFb--TVQPyn9I0a4JBoXh-vfMwX2OGFKuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمار جدیدی از میزان تقاضای استارلینک در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/150969" target="_blank">📅 20:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150968">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbpJir4k2bKLLb_wQ6gi3bQXSVN89o1BGqwadFpH5uernY105w3CJZaf5XLuNx7czimfIU6VoUN2hGKtEoCKDK5M1FvzRGOxzFmOHqCTuorJuYerXq2Sk7hMFzRMeBXwmjUyGt7ehnMj0la56lcXOFl7HohGUxvAzwOcJojL7VGrkDVwuguH-Og4v_L8h0Q1mb9pmnTL1XE9_ZLe4A4ejGwhob3AJGPKFsRIP05icbPbvdxAGZP9shMiRpoCDjF0jHKODc2L_KvV42R4qR-jbugrxi-TFl_FW5zOaqNcB_8oTEak1yWZjNfo-LCAF5ElEUURefI3NuumxIDtdkSu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسپورت ایران در جایگاه ۹۷ رده بندی پاسپورت‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/150968" target="_blank">📅 20:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150967">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
پشت پرده ترسناک دلار
😳
‼️
خبری که بازار رو ترکونده
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/150967" target="_blank">📅 20:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150965">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7wmAdnYn2kMYaBEHMrAlkD6g1dZsIbp6HgLpAysqWfHXK4QeVHUnOumJLdOI_roRLDirDqvQ9ZRf-gb7GrC1ffYVlbh0BlrfzIBrT4te5m-TOKy99ajWf9aaYAMWYyb_9AxTrlEFZo4lfIQE2Dlr5SyCYA9IOU9tW47SB2-SzEgc9sZyEZW1FKRPalRhJFNaOg6vNutl0hQFLuR9cnj8YyGz47lvyrYeh_34JJarQWRBXOQNnenjEp1vBDFw_hGPq9AqEOmcqVmyOsjgZsOFZxG8t05tsIYsDYOMkN_TLnXeE3UIRMyJXQwSju0iO2k0pTOg09IMqfRQHL067JV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bo0e8wTaSxD2LmWAHwnqYX4IVL9SJz9e81Qx8F0NptSSBjQUBdfbRt3LbfUQhBjFoNA6_GGjomKOjCeOkabLn3mfWzFAzAvvEOtvaIG99m5y4E15JAvjYbYNvGlOGeZ-r5fEUQoOsaP_OhuMgcjQl7LcrSoowp5oSqOOleuk7Orqwm5LTvwaeMWo9jvl9Zzo-KlJHVD5heIroqZ2szqBSNkFAMZum8aNFOe_IX5du1pSSvnPF2LO_phsPQ3UZ6r2mhajAOhCEMAIaAiT4YlpxoTGIKxYUroiPwsdRa25z_p-qqnhFfO_bsGSNe87iX_vawv7LZcCSiPS7SDK1gxvzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نظر برخی دانشمندان فیزیک کوانتوم، تصمیماتی که الان میگیرید ممکنه روی گذشته شما تاثیر بزارند و اونو تغییر بدند.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/150965" target="_blank">📅 19:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150964">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
3000 سرباز آمریکایی در اسرائیل مستقر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/150964" target="_blank">📅 19:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150963">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0340afb1.mp4?token=b6cS7V6Dfm_8plkvjC94Z7c98-7myeplefEJcBUqbabIO7cjvbtu3ryIEAdfzLrYWzcZBeZ1rTHgCQTXxLriEsFresiQsWXRTu0k_R3OG3Hdz9HCexQfQHY8p_e4QPSGSOnsXRxw7xAJ9DktL5S8b78tMqMV17nLhpvoccCyKRJoe1y61Ozfpuk3zIWJoClTx0aPZPXfcqAg83k-kxduAw2piAA4f8S7-cWTcSl_WxFiZ8PJakR3PKj4yKJ4fCveuwXZ2up57ADlCFfk0W-Yk3uVs1fqG--mf9Ytl6t_uv7xsILqoi7qLB-wO5nLcJqUcig5iV3Fuiz35nXPmAtxGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0340afb1.mp4?token=b6cS7V6Dfm_8plkvjC94Z7c98-7myeplefEJcBUqbabIO7cjvbtu3ryIEAdfzLrYWzcZBeZ1rTHgCQTXxLriEsFresiQsWXRTu0k_R3OG3Hdz9HCexQfQHY8p_e4QPSGSOnsXRxw7xAJ9DktL5S8b78tMqMV17nLhpvoccCyKRJoe1y61Ozfpuk3zIWJoClTx0aPZPXfcqAg83k-kxduAw2piAA4f8S7-cWTcSl_WxFiZ8PJakR3PKj4yKJ4fCveuwXZ2up57ADlCFfk0W-Yk3uVs1fqG--mf9Ytl6t_uv7xsILqoi7qLB-wO5nLcJqUcig5iV3Fuiz35nXPmAtxGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در یکی از تأسیسات آرامکو در عربستان رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/150963" target="_blank">📅 19:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150962">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
اورشلیم پست:
جمهوری اسلامی کمک مالی به حماس را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/150962" target="_blank">📅 19:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150961">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری/سخنگوی وزارت خارجه:
تهران پیشنهاد مذاکره هسته‌ای واشینگتن را رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/150961" target="_blank">📅 19:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150960">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آکسیوس:
ارتش آمریکا درخواست عربستان سعودی برای بمباران حوثی های یمن را به دلیل تمرکز به روی ایران رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/150960" target="_blank">📅 18:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150959">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر انرژی آمریکا به سی‌بی‌اس: رئیس‌جمهور ترامپ به طور موازی به فشارهای دیپلماتیک و نظامی بر ایران ادامه می‌دهد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/150959" target="_blank">📅 18:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150958">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdpHikD2h7sHZ-Q97S3E7iG9A3asN79DzavLKQ6Yhzq2Bi7vCiqYnX3hk9akvsRecyeZRCNoelRBpBIpSZUjRpWcTdx9Y9Q2jPMF4Kb8E7ox54IjCuJHRDBIOjKd6x9csPK6x6ZsQwTCRWK4UnITreywqN3_cHCWvcq9difbCeckOARL-fw2_HJtr14xfzay8mWqG3oss1jk5y6Pir3YcTWMAnXx4sDLbJR4quGF-4Mw_wu0nGQaN6luXHDOWQeAN9VYyLD7UlEr-crq09Vv-D-M4tx-z3o4dUDemI104JMVQurMvO2bpofHunpDktFmMYOSgZSCakpyoJBTcFDN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از تهران که در رسانه‌های بین المللی منتشر شده تحت عنوان تحولات عظیم در ج.ا
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/150958" target="_blank">📅 18:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150957">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a09eee01.mp4?token=p_9nKredju3TjMfuDFhy8QhprFEoOGSYGBAwHjGcGASeD9tQZ-0hxYNkFd39kq8TwUMRXGf4uZZS7yodNLJ-DNdU3OLw6CU02cuLzdBtx7h6fazxxB_DgyRqAGYfYcZDcDHatL76_wUnJ6Rp5xfKHd--HiWPG3kgnOlI5KfnHwZ6tcwj6I59AB0sY_iZLRvWBvEBq0UjzwhqbG0CgKxDSyWKIUG8UIha3-rPqBG2znGRXuvXn0t8B_rlDRTKOlrwjQ9QObdUw5Xw8R-7E7-TosRM02tVKAdCGUqiseoGO7H8cfiFysqVIbA5hIdLx_eBkVGFHGnQ_-tdchf49CeRaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a09eee01.mp4?token=p_9nKredju3TjMfuDFhy8QhprFEoOGSYGBAwHjGcGASeD9tQZ-0hxYNkFd39kq8TwUMRXGf4uZZS7yodNLJ-DNdU3OLw6CU02cuLzdBtx7h6fazxxB_DgyRqAGYfYcZDcDHatL76_wUnJ6Rp5xfKHd--HiWPG3kgnOlI5KfnHwZ6tcwj6I59AB0sY_iZLRvWBvEBq0UjzwhqbG0CgKxDSyWKIUG8UIha3-rPqBG2znGRXuvXn0t8B_rlDRTKOlrwjQ9QObdUw5Xw8R-7E7-TosRM02tVKAdCGUqiseoGO7H8cfiFysqVIbA5hIdLx_eBkVGFHGnQ_-tdchf49CeRaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی یکی از شب نشینی‌ها، به یه دختر بچه گفتن بیا یه شعر حماسی‌ بخون تا علاقه‌ات به حکومت رو نشون بدی؛ اونم رفت و این شاهکار رو خوند:
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/150957" target="_blank">📅 18:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150956">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
بازار خودرو به شدت ملتهب و در حال رشده، کوییک به لحاظ قیمتی شده قیمت همین ۳ ماه پیش ۲۰۷ و ۲۰۷ داره میشه هم قیمت مزدا 3 های نیو قدیمی
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/150956" target="_blank">📅 18:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150955">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akVr3cI2Lc-y7wA0n2sexh0GdAnfLu1Gc0GFTmviDY0KIGO1CigzQP_fJLICHq1sQC5_XTUno4b9ZDNkIG5vWbnucPC-FLQX-HuU_A2bkoGp8wxWntRxLuYy8dAkdFTAp2TSUR-KWWsRPUc5bEu1xO2JDPw0unASR3-UOEY6i5JiCs1tZiGaUrJtOEFB5yWypvl3DoB2Fkj9oWwi4FrXKd4KsRugoCesCeLToxrzEY3VfoRZhYU8u3ZeJDNi7DsQ-x4Xj9mqTJ6SyIt5Pp7x1zLUwpUQ5RObJmN7PnA5ahV-cOyuBi5TjIg_onnEXBKvFPfz4zsg5GXtfbYJtPUT2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی: آمریکایی‌ها میگن ایران ابرقدرت شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/150955" target="_blank">📅 18:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150954">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84aef80fb7.mp4?token=YD7zlKc5R3XGDUgaF6zVCm9njRmatJ395QfYwG5Ym7wpAEIdbbwSqmUkv5IyDwzSNJaQtB3MYSr6qTzlSvfK9RYIcnHddKrkQQAmBFdHXeWtLcfZs1Q_IfjMRJzHN2CuRrI62tK06f3pDbPcaFuV8FfEpMZiLIqT0CY95KnTyvD7tHpKnk9nxUgBQ1C6YGoVNwYfDPnjpqatR74rLKOaCzDN6pBAWRQcJp-dxlmkG5W9851hUxoJRphUzQL4j5Ar8Eks5pC0vq51R4Kl2cVSmkeexofGqi74jn9uYY3hk22XLCF0tAl1BDQ8hdD4ATgUNFfpE_Ve9i1iu_HW4PuF-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84aef80fb7.mp4?token=YD7zlKc5R3XGDUgaF6zVCm9njRmatJ395QfYwG5Ym7wpAEIdbbwSqmUkv5IyDwzSNJaQtB3MYSr6qTzlSvfK9RYIcnHddKrkQQAmBFdHXeWtLcfZs1Q_IfjMRJzHN2CuRrI62tK06f3pDbPcaFuV8FfEpMZiLIqT0CY95KnTyvD7tHpKnk9nxUgBQ1C6YGoVNwYfDPnjpqatR74rLKOaCzDN6pBAWRQcJp-dxlmkG5W9851hUxoJRphUzQL4j5Ar8Eks5pC0vq51R4Kl2cVSmkeexofGqi74jn9uYY3hk22XLCF0tAl1BDQ8hdD4ATgUNFfpE_Ve9i1iu_HW4PuF-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرار هیمتی از خبرنگاران
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/150954" target="_blank">📅 18:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150953">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
برآورد شبکه CBS: اگر انتخابات میان‌دوره‌ای همین امروز برگزار می‌شد، دموکرات‌ها با ۱۱ کرسی بیشتر، اکثریت را در مجلس نمایندگان می‌گرفتند
🔴
اکثر رأی‌دهندگان معتقدند جنگ ایران باعث افزایش قیمت بنزین شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/150953" target="_blank">📅 18:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150952">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
زلنسکی: آمریکا در تدارک برگزاری مذاکرات سه جانبه است
🔴
ولودیمیرزلنسکی، رئیس جمهور اوکراین گفت که آمریکا می‌خواهد تا پایان اکتبر مذاکرات سه‌جانبه‌ای با روسیه و اوکراین برگزار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150952" target="_blank">📅 17:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150951">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزارت دفاع روسیه: دو کشتی باری حامل تجهیزات نظامی اوکراین را در نزدیکی بندر اودسا در دریای سیاه بمباران کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150951" target="_blank">📅 17:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150950">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ارتش دولت یمن تحت حمایت عربستان سعودی عملیات نظامی گسترده ای را از سه جبهه به سمت صنعا، پایتخت حوثی های یمن آغاز کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150950" target="_blank">📅 17:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150949">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UX06ObxdEEY_2NXpZUnEH_jmi-Jmr90tr6dXVGSkE10sDvEfVDJy_5f3ci7RqGfNHN6UxuSob_sQV_D3C3TT8_Gjp4bODpxSnagrKdDyehqp608UTzdG-h1cM28M43nPt5N_imvLxldjrMsCxc6MOY9xkado4esIjSwwUiGkXywEfF1nWBVQIRZxroIZ7kr8kfgeh376KYti-1jeDFTp40R-YvYRbm0WO9uyfuNnKX5JCTJlmCY9KmAAGO9J5I-2Chdfikg-VMmKc2zgv4o3MYvTxxZndmUn0NqGHAQ7-iGfR4XVXDLlhPTXAvY8C59IvA-h5K0NyAd4Jd7XXXRLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: ایران انتقام خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/150949" target="_blank">📅 17:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150948">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150948" target="_blank">📅 17:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150947">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ناو هواپیمابر جورج بوش پس از ۶ ماه حضور در خاورمیانه در تایلند پهلو گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/150947" target="_blank">📅 17:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150946">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbnWpUEzhksbWEjavZ966WSWHxs3T4coGnG2mzSpfFDjP4j9gStq_U_snrLh4JxXq69Kpr6YsAsC0XZ281lP48e82RYmjlCZWfpi7onuqaqIorikkLbdhKTGLT5kaaIVNbCbnLmCiCnwtxiNfS7zWeraR8pHbI3pm6scvGVQhmGXV4GflPESA-_cB-dXaCHLZqNKFYWYNdQLoxfn8Qrqh8EBAgTV4SrOwWleYekH_lQKCEwA4yx9sGvdXhS0S4ReOy_OFsSWo8ekTdolEiku39etywu0-3rglnft2AjjGK5u9Rq5TOy_ECBUbiq-WlDUYUdo2R6f-ipNkfwc6ATvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل: حال امام خوبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/150946" target="_blank">📅 17:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150945">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
این تحلیل ترسناک رو حتما ببین
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/150945" target="_blank">📅 17:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150944">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری / معاون وزیر خارجه: آمریکا پاسخ طرح ۷ روزه ایران را ارسال کرد
‏
🔴
این نظرات در مسیر خودش در داخل کشور در حال بررسی است و نظرات نهایی ایران آماده شود، از طریق مقتضی اعلام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150944" target="_blank">📅 16:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150943">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWNFSSTxxzu8QKiFaakonKX9S1asIvfBwSpwE9U5KbOifSSuLj-x1e673o-TVsTZXJFlIhpaFDa1Ode1gNdv7ROSG6U1VInrcbmv9gJxqn4Q4Y8JD29zMPIvG3SoU2cD9N-J47LtMI7xvj6Iu7RdGcNFkDd72v3VmqLtYHUr6TTtRlh5jcuU1Ilx4sQzuw2qBBwQsGnN5v7G-r9PBjEQI_UKGHFeHGBAo7Rh1xXdatPjmEt4sUhwtGqm5FvHqlVbS_emgfZIvo0JN5bodAotR34n7huQ7LiwPosDmicLcUQctS6wQgNMpVuyU4RzXC2RDmQY2Mr-bByMKXJVHYQfWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
کوچک زاده نماینده مجلس: اون مردمی که میرن ارز دولتی میخرن، دلال و دزد هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150943" target="_blank">📅 16:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150942">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=LQrHyB0TZvQSTVxNadZMvI9WENGwQY97x6MhCiiZhJqP7MpBPF_aLq7YRwUYLsI0dqudXn5u-38d0t8-Gv2L5HHIciJe0PR-r-tE23TL1xdxnD53-z3e1hG0QYlYi4TmTaAQNf7SI838-03FLB58qgdHvoNjza2ra9BuY3tWVg9pVEpPhiAK6MVmGQ1iC1OFra1-wImDXPL9CrXi_XrYND4zCRJpqDL6K55A38zgCfxuVAKFSwF7O1D2-OsOkVw3__N0vYpf_nEZNewNL5QgKocw1-ml1BTTQL1yFFode5is7UUO2Aw3HNKkbm4ZB1cbkTlHjA1xqNaWv0yZ-txkRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=LQrHyB0TZvQSTVxNadZMvI9WENGwQY97x6MhCiiZhJqP7MpBPF_aLq7YRwUYLsI0dqudXn5u-38d0t8-Gv2L5HHIciJe0PR-r-tE23TL1xdxnD53-z3e1hG0QYlYi4TmTaAQNf7SI838-03FLB58qgdHvoNjza2ra9BuY3tWVg9pVEpPhiAK6MVmGQ1iC1OFra1-wImDXPL9CrXi_XrYND4zCRJpqDL6K55A38zgCfxuVAKFSwF7O1D2-OsOkVw3__N0vYpf_nEZNewNL5QgKocw1-ml1BTTQL1yFFode5is7UUO2Aw3HNKkbm4ZB1cbkTlHjA1xqNaWv0yZ-txkRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی یه بالن فرستاده بود هوا تا اوضاع هوا رو چک کنه که یه سری نگهبان معدن فکر کردن پهپاد آمریکاییه با برنو زدنش
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150942" target="_blank">📅 16:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150941">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
دقایقی پیش یک هواپیمای ترابری سنگین نظامی روسیه تو تهران فرود اومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150941" target="_blank">📅 16:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150940">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نیویورک تایمز: کمک خلبان پرواز فلای دبی ارتباطی با ایران ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150940" target="_blank">📅 16:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150939">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2a27e50f8.mp4?token=LeZ4XJ6a0y2WQ7ZqAYK3L0CHTdaPqrMqrX8TofKMsKSpG4uYQZkzWPkssO-mjFgBnpkUDftRniXiqXvlW6dJbJ9nssI9N6PBjvvqC4pV4GYcpL8hUx4Wg5TB1D-Zmd6BsMTfNr0V9_psriLmCGOtMJl_LvjKFmnix6C4VFRSOgLxeDFGxiw0NEvJJOD12DgV-NkSQCFFLD338LOoamh6u0c30Z1xQWMmzJxRJ3G0nmei3UG95H3-5YoUuohssgmp1bdbljdii9UzDdNXHINAdOi-wRnzWPrvzrDqjgZXQD6s7sl-H4chys8ddFmiwyKNKWC_OBh8GLtL_YAynF5j5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2a27e50f8.mp4?token=LeZ4XJ6a0y2WQ7ZqAYK3L0CHTdaPqrMqrX8TofKMsKSpG4uYQZkzWPkssO-mjFgBnpkUDftRniXiqXvlW6dJbJ9nssI9N6PBjvvqC4pV4GYcpL8hUx4Wg5TB1D-Zmd6BsMTfNr0V9_psriLmCGOtMJl_LvjKFmnix6C4VFRSOgLxeDFGxiw0NEvJJOD12DgV-NkSQCFFLD338LOoamh6u0c30Z1xQWMmzJxRJ3G0nmei3UG95H3-5YoUuohssgmp1bdbljdii9UzDdNXHINAdOi-wRnzWPrvzrDqjgZXQD6s7sl-H4chys8ddFmiwyKNKWC_OBh8GLtL_YAynF5j5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی‌ها خانه رئیس پارلمان یمن را تصرف کردند
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150939" target="_blank">📅 16:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150938">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7e5a3bac.mp4?token=r_Ks3rA6mKIVDfERdf1Zlf1KpbbV2S-KCSJOaHGVX3nJ67k5naPDXppryLEDPK0N87s2htrAIW6dG8RW5Yw0jCAzdINt6Af0Ibgpaia98uMMFaNwzJRnxyKaqPJA3dhlu-bQP6anZke1M8bSM-I6Y1IBnK4VRcoORiNbM9Ax69dB1ox0jvQ0Ym8nWA3p1Jhpx-5Ittuf6xNThKT1XC6dzC_xE681OtY2A2HLvZiJv5pXLlub14mk2lsm7iNog4yxk9VtFFhP5EuD3NHa2g0eHi6NOE6T4bIPjGDcvTQWmu7bJjoX1QCd7DcTnv-suuHyi-Y9OWbep8_3O_Bgi94U_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7e5a3bac.mp4?token=r_Ks3rA6mKIVDfERdf1Zlf1KpbbV2S-KCSJOaHGVX3nJ67k5naPDXppryLEDPK0N87s2htrAIW6dG8RW5Yw0jCAzdINt6Af0Ibgpaia98uMMFaNwzJRnxyKaqPJA3dhlu-bQP6anZke1M8bSM-I6Y1IBnK4VRcoORiNbM9Ax69dB1ox0jvQ0Ym8nWA3p1Jhpx-5Ittuf6xNThKT1XC6dzC_xE681OtY2A2HLvZiJv5pXLlub14mk2lsm7iNog4yxk9VtFFhP5EuD3NHa2g0eHi6NOE6T4bIPjGDcvTQWmu7bJjoX1QCd7DcTnv-suuHyi-Y9OWbep8_3O_Bgi94U_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت اسرائیل: چشممان کاملاً به تهدید تروریسم است
🔴
اسرائیل در زمینه تروریسم با چشمانی کاملاً باز عمل می‌کند.
🔴
ما می‌دانیم سازمان‌هایی وجود دارند که تلاش می‌کنند کارزار انتخاباتی ما را مختل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150938" target="_blank">📅 16:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150937">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDJSQfg8wJ8xMJwONzp2VNLsxehCEbVMpAkHYmh68ycYd3IUVXNT9ssXaX2UyvyKySKcbxTTWMxIy_by_mAaA1KtdyQl-CBNYTqI4z9jTiTQg83XoxSkz3MlZ1_LRkKFRSn1BzIM_j5p5JoxqQF2Rr0gtJ4V7xMjqATUtj7GBOb5rApveYLLA71636fD-SGb-UOOqqpSZQd92_M7i_cpLJxsJ8H8XCSZLnAsf4QuLBs-50-1KaZyJLeuAdjSdJJz5FseowonPnVuGyPQI_qaxatWChNnTmtuP-XGnRoOBzPtxc68fNLSg2P0Ipmhk2I-diqh3O3JEsHxjg742v7eUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : او چقدر دستمزد می‌گیرد و از طرف چه کسی؟ او در تمام پروژه‌های من حضور دارد و اعتراض می‌کند.
🔴
افراد دیگری هم هستند که دقیقاً همین افراد هستند. این‌ها معترض‌های مزدور نیستند، درسته؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150937" target="_blank">📅 16:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150936">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb1eiSWKRAAW9k2vLXSfkVQkjqgZeCMHBnew1g-wZm7prjwJorw_b31eXibYkjHu5VtDXFLLHt6Ja9Pt-ejiQ4NMZ_Wz7sNq-ayt3Ji1a9e0viv_o5kztD8xiTLXVIOH1resba04RKgPs1aQQRq792eLDp96of83taFlSLxePMI8_QF-ZCaG93Yg7IRX0tuGaBd1g-9VQyuJV8Yi_xGrE_mLn504ggDpffkggHozY1F3V1kvYE0Bg-BHn0dKOvfMgucrcO2g-j0mLL4GPIQPjgYLXJd13gpgs8AV1KwU19GklOdmftyRf8CFC2MyH8LQ_8Url63kdXUscuMGxPB0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از ایجاد یک "نیروی فوق‌العاده هوش مصنوعی" (SIF) جدید در سطح فدرال خبر داد.
🔴
ترامپ گفت که این گروه ویژه، تلاش‌های فدرال را برای حفظ رهبری ایالات متحده در زمینه هوش مصنوعی پیشرفته هماهنگ خواهد کرد و همچنین بر تعامل دولت با مصرف‌کنندگان، گروه‌های ذینفع، گروه‌های مذهبی، ارائه‌دهندگان زیرساخت‌های حیاتی و شرکت‌های فعال در حوزه هوش مصنوعی نظارت خواهد داشت.
🔴
این "نیروی فوق‌العاده هوش مصنوعی" شامل آقایان جی کلتون (مدیر سازمان اطلاعات)، اندرو فرگوسن (رئیس کمیسیون تجارت فدرال)، امیل مایکل (معاون وزیر جنگ و مدیر ارشد فناوری) و اسکات کوپور (مدیر اداره مدیریت و بودجه) خواهد بود که مستقیماً به ترامپ و سوزی وایلز، رئیس دفتر ریاست جمهوری، گزارش خواهند داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150936" target="_blank">📅 16:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150935">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
اصغر فرهادی: آمریکاییا خودشونو برتر میبینن و اصلا دموکراسی ندارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150935" target="_blank">📅 16:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150934">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muZGp55rbL4yM-8mLIBMSKC9hjosKW4o1NXshKftu4s4cIvYltk3nhBVlOs9nCbZoRFLm7FCpb0Q2NLkliZo1rAk6H5d8HoKnjqncURqgbfRB1PRCm4aqGQUrsjPtjiMytioDizf1Hy5ksHGwmiuUCOnsz3-GKpIn3B-YutAXc0g-ba7irOg-cmfMb7kdLahaZ2xymojIE7MYsnZQz4Lnj9kPIgUt5b-IrXp8gcprrhjBYInIOpX_f0ZOsZJHaaZI8W-Wly34rVoa4L8c4ldAdr1zbmiq648ubzOjhoNzQptFXIWAg49A0dBipRdxUfiQ9Nbye7vx2_ecQ8_r2ObxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، جان کوال را به عنوان نماینده ویژه جدید خود در امور گروگان‌ها منصوب کرده است. پیش از این، آدام بوهلر این سمت را بر عهده داشت.
🔴
ترامپ گفت که بوهلر به عنوان مشاور ارشد، "به انجام وظایف دیگری نیز ادامه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150934" target="_blank">📅 16:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150933">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
گوگل دسترسی کاربران رایگان جمنای را محدود کرد
🔴
از ۹ اکتبر (۱۷ مهر)، کاربران رایگان جمنای تنها به مدل Flash-Lite دسترسی خواهند داشت و مدل‌های Flash و Pro برای آنها حذف می‌شوند
🔴
مشترکان AI Plus نیز دسترسی به Pro را از دست می‌دهند؛ کاربران AI Pro و Ultra همچنان به هر سه مدل دسترسی دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150933" target="_blank">📅 15:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150932">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=pZxM2pNBJjem7sA61xSB12S5OsKKSc-Mjt7MSvYa0fzFVdvSkNEmU67-z4SED77NDUYDQcVU8PSG6U7mly3vEie_ZEjhtAgvL5CMmvoK0puea8sw83mjqVK7i9i9khgmi12ei5At62T5jDtYTLyVmlWbDEzr2e4u5PWc2nbrpQmUD2t2T17LO3Kd1H5ZllM0AqVjBF90-_YiRJX90CESPWR7KVRn2BNYqrxAB7qM5wNMijmhLyWqjOEsrRjxzVJLqc6e5KkcgSiEnJRVGNN98rx1pr2AorRdPe5R3z8rkAsBrcCyb2XIvAZagMl5eOmxktc9zWuR5u9aj50_L5k6HkiaNQ0uoWAsMtJm4x77huiq9hDxTNW5_pjx2dByWuks_AG2tAvG5PA8et1_PK3Snno4E2RUeg-VSWRt7zbXwyGyPuKp2N15tmRQdPm57hpuyw_YXhoCU2iZqZHrYPF5HfnAanxKBS4DFJxgUxyRG7MxSQ0dy0-didZ0UDhwE77lpX4NCU8x6VIb8rfLU-PG9Z3AKBAmtwxrgAPeHPqqOgU9k3tMhCHRh2hM9tRDMhgyrQHsgChrc54yvjhzSgNMU3Gcqe2pYwjVikXKmPzzy8_CXweDqrjgE4Myo_ebYAaqKBYV2IroYj1uYJFp4xBtmFdT591pVUf4qXH1nk4L6yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=pZxM2pNBJjem7sA61xSB12S5OsKKSc-Mjt7MSvYa0fzFVdvSkNEmU67-z4SED77NDUYDQcVU8PSG6U7mly3vEie_ZEjhtAgvL5CMmvoK0puea8sw83mjqVK7i9i9khgmi12ei5At62T5jDtYTLyVmlWbDEzr2e4u5PWc2nbrpQmUD2t2T17LO3Kd1H5ZllM0AqVjBF90-_YiRJX90CESPWR7KVRn2BNYqrxAB7qM5wNMijmhLyWqjOEsrRjxzVJLqc6e5KkcgSiEnJRVGNN98rx1pr2AorRdPe5R3z8rkAsBrcCyb2XIvAZagMl5eOmxktc9zWuR5u9aj50_L5k6HkiaNQ0uoWAsMtJm4x77huiq9hDxTNW5_pjx2dByWuks_AG2tAvG5PA8et1_PK3Snno4E2RUeg-VSWRt7zbXwyGyPuKp2N15tmRQdPm57hpuyw_YXhoCU2iZqZHrYPF5HfnAanxKBS4DFJxgUxyRG7MxSQ0dy0-didZ0UDhwE77lpX4NCU8x6VIb8rfLU-PG9Z3AKBAmtwxrgAPeHPqqOgU9k3tMhCHRh2hM9tRDMhgyrQHsgChrc54yvjhzSgNMU3Gcqe2pYwjVikXKmPzzy8_CXweDqrjgE4Myo_ebYAaqKBYV2IroYj1uYJFp4xBtmFdT591pVUf4qXH1nk4L6yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رشاد العلیمی، رئیس شورای انتقالی یمن (PLC) که از سوی عربستان سعودی پشتیبانی می‌شود، آغاز عملیات نظامی گسترده در تمام جبهه‌ها را برای بازپس‌گیری مناطق تحت کنترل حوثی‌ها (أنصارالله) و احیای اقتدار دولت PLC در سراسر کشور اعلام کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150932" target="_blank">📅 15:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150931">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
اگه از بازار جاموندی اینجارو داشته باش
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150931" target="_blank">📅 15:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150930">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ایهود باراک، نخست وزیر اسبق اسرائیل:
نتانیاهو در حال زمینه‌سازی برای آغاز جنگی است که برگزاری انتخابات را به تعویق بیندازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150930" target="_blank">📅 15:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150929">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilkw364O7cQQUSS6Y0eDoldZ-FNUuqznUV8MOPkTaGpMleXBwnND3kE37i4SRqYnD-B4AV_rHMLTJ2FInOidPrHEIes8aJoyIr1zQspx4YNShlynF6r-Q0mvL67wvtRsQXEUcAVBMi5-0l9S07yT1lzwk00yBW2cgJ-PbCF5xITIqN6oKfHUOMFZjyof15RAkCZP73sIhfOh3yzXtA2Yk3HwrjYaQgXKI5my7QlDSMO7Jvl8WAk5R2L9YO8lVKH0QeqBJ6ojBxfJh3u1F5c73dkHHzjw77ct8hQFTsceoEFNFWgjKhbE1hN9Vgue1bNRbQmR0pEqnIt0OTCeyl4bCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین برف پاییزی بر دماوند نشست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150929" target="_blank">📅 15:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150928">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
کوچک‌زاده، نماینده مجلس : مملکت رو دارن به آمریکا میفروشن. من گفتم این جنایته. به خدا اگه از جهنم نمی‌ترسیدم، امروز خودم رو جلوی بانک مرکزی آتش می‌زدم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150928" target="_blank">📅 15:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150927">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e6ff2766.mp4?token=PitSHUvJYAQQF4MuAq9Ftv-JwLs9S4haJWp4mubmBvDzvMoSFXU_gRyF1mWlB6ti_hczo0xfa8DBwpZGn6V_yS6LYZPzAz-flBh-m7F9aVSJGCPGp6FUXqt_YK1-72mQBUw-GRxa6dXJSGuIZDh6APcyt8hmaoW4wl_xIuSdCwUIgB-rvqHxSn3H2OtL46bi_F8n8ouxY2phgeV-JBq1THPsSdo-AMKWPWSKKC-6eM4iMsgOxBqoujBr_HxFdBADZ8J378vg1huaGHoU4YTvb2dPjPACc5BztGe_faSHxkxzZ4pse_SFdaKF4Hx668UROaSJa18vTGIZVNinBeaE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e6ff2766.mp4?token=PitSHUvJYAQQF4MuAq9Ftv-JwLs9S4haJWp4mubmBvDzvMoSFXU_gRyF1mWlB6ti_hczo0xfa8DBwpZGn6V_yS6LYZPzAz-flBh-m7F9aVSJGCPGp6FUXqt_YK1-72mQBUw-GRxa6dXJSGuIZDh6APcyt8hmaoW4wl_xIuSdCwUIgB-rvqHxSn3H2OtL46bi_F8n8ouxY2phgeV-JBq1THPsSdo-AMKWPWSKKC-6eM4iMsgOxBqoujBr_HxFdBADZ8J378vg1huaGHoU4YTvb2dPjPACc5BztGe_faSHxkxzZ4pse_SFdaKF4Hx668UROaSJa18vTGIZVNinBeaE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از پاکسازی یک سنگر نیروهای روسیه توسط نیروهای ویژه ارتش اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150927" target="_blank">📅 15:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150926">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نایب رئیس مجلس: وزرای پیشنهادی اطلاعات و دفاع تا پایان مهر به مجلس معرفی‌ می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150926" target="_blank">📅 15:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150925">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تابناک از احتمال بازگشت گلشیفته فراهانی به ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150925" target="_blank">📅 15:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150924">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا از حمله موشکی سپاه به یک نفتکش در تنگه هرمز خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150924" target="_blank">📅 15:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150923">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnX3DP-Mymf6UrK-N7zK5ARQJePVYPi4EwJfrXFUmJZpewQjo-1GMtIqBTgQ5nKNsDnKIs9OQAo5Q7H4DYSXThAjafWyjlIqC6XpxivmWxWElCCVzCT7RSslAz_cN3mSZI6-5t1UA4_ekiCXLEOQvg8VhpgUz-k1yFqv8NTTHcBiQkSIYZTE24hgULAiD9_mDmVVAXyCO6mG3tVsvLv_AcDZcdDJyQhJgflpcquyo3GumDT95-mJ6w_-V40RekAKmprKV9VBOgtiIv-j6FcskYismBHyHT1gp8v5b3Najx2OE73nalWXT3JhjFrTLPkwep4SW8dwAXYV3HJctguphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حوثی ها کنترل العزاعز و المنصوره را به دست گرفته‌اند و به سمت الاصابح پیشروی می‌کنند و به حومه شهر تربه نزدیک می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150923" target="_blank">📅 15:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150922">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کارشناس صدا و سیما: تو راه قله‌ایم و کوهنوردها میدونن که نفس آدم میگیره تا برسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150922" target="_blank">📅 15:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نیویورک بهترین شهر جهان در سال ۲۰۲۶ اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150921" target="_blank">📅 14:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a486bfc79c.mp4?token=CP43feDyzLzhYcSyMqyUipgY7gfpbqNMaFIN2SnB3TloNhqr4Qyq98rDmqcDsIjnK23DCJ1Vt3ioClPbJ3E13oq-kt6c2eoPOCJqkSxPrdBKDv-NhCQ6FiNjC7bvycS1wJt6n1_qikdIZs28GOJlJmqQX_5m6c4C7uB1Ms6tYsI9iImVKUucT-fHJl7WqvCxsxt-IDZEsGqf6oSvlcs9RBoWhP3kAPW_55pq-NkkKUq7EaSWef5M_Z2j66YQCBA_YxaRUr6EBEJzn0ajOj0-XUy8ns5hANVfBsGcIlF0p9U8DTjJcWKb6N_OG3Y9yrIvJmh0a8HRycp0nQZKJdmoWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a486bfc79c.mp4?token=CP43feDyzLzhYcSyMqyUipgY7gfpbqNMaFIN2SnB3TloNhqr4Qyq98rDmqcDsIjnK23DCJ1Vt3ioClPbJ3E13oq-kt6c2eoPOCJqkSxPrdBKDv-NhCQ6FiNjC7bvycS1wJt6n1_qikdIZs28GOJlJmqQX_5m6c4C7uB1Ms6tYsI9iImVKUucT-fHJl7WqvCxsxt-IDZEsGqf6oSvlcs9RBoWhP3kAPW_55pq-NkkKUq7EaSWef5M_Z2j66YQCBA_YxaRUr6EBEJzn0ajOj0-XUy8ns5hANVfBsGcIlF0p9U8DTjJcWKb6N_OG3Y9yrIvJmh0a8HRycp0nQZKJdmoWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ثابتی و شهریاری تو کره باستان
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150920" target="_blank">📅 14:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150919">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fecd2cc8b.mp4?token=okZ05fIhVyHD_ePpMoSb7AqHL9HwUXA8gMbo1-K8qx250EUQuMRKcgFbWgkOYqpEJS6Y12KgmwgnJ5gLLzIfPdlkSH7qwdqu10rU4hqWLn1p5m4naAV0rNIDg4tuduUy1iacu53TWLwo5iaazvizJtT4PWq0KmpdnHXH4N4e3X_TSQ2-wvLHcRIsvebxmrRhdpxsEG-yJVtqxQP6j5_EAn2qEdsF7bZjgC-C_JHqOxQ69LqTk7en68ZvngP4aKhWGn0drmgVE1tvQXinnK7g5chTmxUKmXjXYsg3TY9aW3yEqzYLRnGyJ9ymu8UOGEbt5PcHgiIU3RLF6YvZage5Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fecd2cc8b.mp4?token=okZ05fIhVyHD_ePpMoSb7AqHL9HwUXA8gMbo1-K8qx250EUQuMRKcgFbWgkOYqpEJS6Y12KgmwgnJ5gLLzIfPdlkSH7qwdqu10rU4hqWLn1p5m4naAV0rNIDg4tuduUy1iacu53TWLwo5iaazvizJtT4PWq0KmpdnHXH4N4e3X_TSQ2-wvLHcRIsvebxmrRhdpxsEG-yJVtqxQP6j5_EAn2qEdsF7bZjgC-C_JHqOxQ69LqTk7en68ZvngP4aKhWGn0drmgVE1tvQXinnK7g5chTmxUKmXjXYsg3TY9aW3yEqzYLRnGyJ9ymu8UOGEbt5PcHgiIU3RLF6YvZage5Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
عرزشی‌ها بعد از ۱۰قرن حرم امام رضا را از یک مکان مذهبی به یک مکان سیاسی تبدیل کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150919" target="_blank">📅 14:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150918">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZNSyXGzd2qhjTltKX-jz2k0YPqhWJ7g_Cy9GiFkzIFvohOt7scegyaFrcUd-QAtuykf5oQo9TylrS1aYO4gANsxY4IijzFMwhv_S8YBwsNEcwkC_LA1x5qrNpqZfAnxntn2adUWRBGIQPWem43aQ6qo3dvbiWNtUZ1_XMYCtNqQbDOQ7wVAczjnK-i5c4-Chh93Ca_llk81yXeHAtqksf4uNIA1xp6wtId_dB1PgtOIA1XMlstAH8YjYGtFnzOGrKQjX_e7J8Bq6gQEls7rQwi4NWkZa_1hHraoQE71FBxmCbHX4XmvBxAtjDzQCQJESIcIVRYB6U3ZnZu5uWGgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هزینه اجاره یک سوپر نفتکش برای حمل نفت از خلیج فارس به خاور دور به حدود ۱.۳ میلیون دلار در روز رسیده است.
🔴
پیش از آغاز جنگ، این رقم کمتر از ۵۰ هزار دلار در روز بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150918" target="_blank">📅 14:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150917">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0558dea8d7.mp4?token=Obk2i5VR-DKNWBIQvCJK_oJn8bCPJHqiTnW1nCB9QGr8Y-U1xZNwjHNTuBBsuUuyPpUQ1BoYne7JtfIvEallsH-cIuZiaGu_jsoRDBjCZy7ISQ3s3JI79QpFCzB3tNwrL10UBjSbohSRqey-afMoEPXVl-m2C6OeQKMnuYJu6WdcYr2yR7NKVhUiPOsI-INvoh9h_F3by4dXPMS-b_qqU-xqLwQftR2lvMqP5Ug82flO_lHXJpCDvCiXV_EebacGAVlsAy3pZTplXuhbQfMLPQi4W9SNnDFWs5FA7lf2ELRg6QZsyGyftLiRL7zZ-bEdcdRJWu1iSN47ALBqrXjqwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0558dea8d7.mp4?token=Obk2i5VR-DKNWBIQvCJK_oJn8bCPJHqiTnW1nCB9QGr8Y-U1xZNwjHNTuBBsuUuyPpUQ1BoYne7JtfIvEallsH-cIuZiaGu_jsoRDBjCZy7ISQ3s3JI79QpFCzB3tNwrL10UBjSbohSRqey-afMoEPXVl-m2C6OeQKMnuYJu6WdcYr2yR7NKVhUiPOsI-INvoh9h_F3by4dXPMS-b_qqU-xqLwQftR2lvMqP5Ug82flO_lHXJpCDvCiXV_EebacGAVlsAy3pZTplXuhbQfMLPQi4W9SNnDFWs5FA7lf2ELRg6QZsyGyftLiRL7zZ-bEdcdRJWu1iSN47ALBqrXjqwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به صدا درآمدن آژیر خطر همزمان با دیدار زلنسکی و مرتس در کی‌یف
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150917" target="_blank">📅 14:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150916">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
بابک زنجانی: وضعیت گاز خطرناک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150916" target="_blank">📅 14:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150915">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
پشت پرده ترسناک دلار
😳
‼️
خبری که بازار رو ترکونده
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150915" target="_blank">📅 14:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150914">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
کارشناس صداوسیما: تمام اتفاقاتی که داره میوفته از نشانه های آخرالزمانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150914" target="_blank">📅 14:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150913">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=kfJzraNLr4z7iv-5NiCPK83lZkTy_pR468lNqICl5TBGk94mkZWASDaBttNY0fxfIxDPiMGN0cTsbPl7zDf246qDubxIduReZ3gQotROssKiHrweHGSS2nt8bBs2B4REBCLrpdxxHuYI6D9beZFWpbC870V4MuOapmEQLll75XfpSNkuowCKBvq5IYpAWpt1EmYNx1kHSKuSnvZBI0UtIlcTinjdwqP7t7YVJWtEnZcftDfBqm1KADstXQttEpF6WZwrG3QdEWy6C8yx4dq-FqjsRmTpJnyxqVFGy_t88CWMxS2801LrzCaTA-vZL2DSbyHzzS2dXynYjBidz89h722SjaTQtrcTC5I4hf2gKICE-P0sY_AFpSjLSm1sXM1y8h0ERS7WCQENp3fHO4jt7Tf14NLDtTZEqKgkH671CUE5SsfgLzgUN5S1a91ibB2HF2mDLPmTp53SXnjxuqu5N7gQDyRrD1jK1EorLB0N2mXXLQkrHSx4ejJvicibhxq_D0wEXCElqx_r4yhH_G2cUlMFsIsbOx-fXNF866msaz93nPwcroL2opALaQ5DNYeBdRWF-KPIbJWjkf18LKIr2FftWYi36ZaDoOh3GFHCLnIc2P54BTaGrFvEQeOlTllgeGfFqPLrJZnrqVdTrgshGpXgRMhBY6zyiClbnto8NDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=kfJzraNLr4z7iv-5NiCPK83lZkTy_pR468lNqICl5TBGk94mkZWASDaBttNY0fxfIxDPiMGN0cTsbPl7zDf246qDubxIduReZ3gQotROssKiHrweHGSS2nt8bBs2B4REBCLrpdxxHuYI6D9beZFWpbC870V4MuOapmEQLll75XfpSNkuowCKBvq5IYpAWpt1EmYNx1kHSKuSnvZBI0UtIlcTinjdwqP7t7YVJWtEnZcftDfBqm1KADstXQttEpF6WZwrG3QdEWy6C8yx4dq-FqjsRmTpJnyxqVFGy_t88CWMxS2801LrzCaTA-vZL2DSbyHzzS2dXynYjBidz89h722SjaTQtrcTC5I4hf2gKICE-P0sY_AFpSjLSm1sXM1y8h0ERS7WCQENp3fHO4jt7Tf14NLDtTZEqKgkH671CUE5SsfgLzgUN5S1a91ibB2HF2mDLPmTp53SXnjxuqu5N7gQDyRrD1jK1EorLB0N2mXXLQkrHSx4ejJvicibhxq_D0wEXCElqx_r4yhH_G2cUlMFsIsbOx-fXNF866msaz93nPwcroL2opALaQ5DNYeBdRWF-KPIbJWjkf18LKIr2FftWYi36ZaDoOh3GFHCLnIc2P54BTaGrFvEQeOlTllgeGfFqPLrJZnrqVdTrgshGpXgRMhBY6zyiClbnto8NDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور بیژن مرتضوی و همسرش در دربند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/150913" target="_blank">📅 14:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150911">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkVha8_GWs6ZG7Tz3mKlOmje8YvmCv1b4oWqkzdfxAv4ZltWQpI--8-M9x2K-H0tc86PTRJbsfE741_PgM3YmEo9ZVoam2kxU3flWwHQgOb6rKULilZL1Hl8h155WV93EIldIB6i5uUfROpShx6WUc56z_eoWRE71bOnkPJyEVlQUCo1wW-dEX1t7pc9WHeNYVsLhz7qMquxLmIbNAlRdJ5C54yHFbloqCXj_IDRDhISKV4XaPc3okbPBwNIq3UCN3RifIik8oEdpBEBET8HMRB8HOdEE0A9z70UFa6wJBjxFKe9CMs4PPFRCSBhzk27VUOJLBdC3uA_wUP3BzQKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای حوثی به منطقه العزاعز، نزدیک تربه، رسیده‌اند و در حال درگیری با نیروهای وفادار به عربستان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150911" target="_blank">📅 14:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150910">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
قسمت ترسناک ماجرا اینه که با وجود خبر تزریق بانک مرکزی و جو امنیتی و بستن صرافی ها و عدم نمایش قیمت، بازار بدون واکنش به مسیرش ادامه داده
🔴
قبلا این کارا یه مدتی موثر بود...
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150910" target="_blank">📅 14:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150909">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: بحث خروج ایران از NPT بسیار جدی است و در محافل سیاسی کشور مطرح است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150909" target="_blank">📅 14:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150908">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نایب رئیس مجلس، حاجی بابایی :
هیچ‌وقت مذاکرات ما با آمریکایی‌ها موفقیت‌آمیز نبوده و دلیل آن این است که آمریکایی‌ها صادقانه با ما مذاکره نمی‌کنند.
🔴
هیچ‌وقت ما با آمریکا به تفاهم نخواهیم رسید
🔴
اکنون در واقع مذاکرات با آمریکا در حال انجام است
🔴
برای اینکه به یک جمع‌بندی برسیم، لازمه آن این است که از یک قدرت بالا برخوردار باشیم
🔴
تا وقتی ما از موضع قدرت و اقتدار با آمریکا حرف نزنیم، آمریکا همین روند خودش را ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/150908" target="_blank">📅 13:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150907">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9J5jp2vakHWlqykC4eTzUbPXZ-WTSbzpwVg5w2HXCC-epDSNyE8_vACXW8E0PgOTjxsQnAWjpLHdKfa6SgMNgQVGr1Qxzqza71HYM93bGyrETFqBqT0n4wyH0UhbeEfN9JR5C0Z_tDkzin3RjQPhAVBP8tdI_0wEJ4jGbJPNuDqjRUYcD8S-WhkRD2kcEn-xT3-8AFaYb7kOu--U__C6prxjmpDQ1uNGzODuJgxV4N9KkL4JvX94FHR22EvwZ5PllY2NBy257-Vn34APY7aFEtSgDiT9SrNEN9lowkNi2ZnkgpiX1nrOSIz-hDQsrskTzmU6dqlQzDo-dCXrKjQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی: حملات به پالایشگاه‌های روسیه را افزایش می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150907" target="_blank">📅 13:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150906">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سخنگوی ارتش: برد موشک‌هایمان‌ را افزایش خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/150906" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150905">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
حادثه‌ برای هواپیمای اماراتی در پرواز دبی-استانبول
🔴
حین یک پرواز شرکت هواپیمایی امارات از دبی به استانبول، ناگهان آب از سقف هواپیما سرازیر شد.
🔴
نکته قابل‌ توجه این بود که آب دقیقا از محل قرارگیری تابلوی خروجی در داخل کابین می‌چکید.
🔴
برخی مسافران برای در امان ماندن از ریزش آب مجبور شدند پتو روی سر خود بکشند در حالی که خدمه پرواز در صندلی‌های خود نشسته بودند.
🔴
هواپیمایی امارات علت این حادثه را تجمع بیش ‌ازحد آب اضافی اعلام کرد.
🔴
با وجود این حادثه پرواز توانست پس از حدود چهار ساعت به مقصد برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150905" target="_blank">📅 13:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150904">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
قیمت دلار به 272,500 تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150904" target="_blank">📅 13:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150903">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
منابع عربی از توقف فعالیت‌ در فرودگاه بین‌المللی طائف در عربستان سعودی خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/150903" target="_blank">📅 13:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150902">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما و کشورهای غربی باید در نظر داشته باشیم که همسایگان ابدی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/150902" target="_blank">📅 13:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150901">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8d1fjnYqqndSmXgoMu0NXa_E4cSJF9oD-pO6Z0QCtzRQ9-WO24ecixByl7hEtYP_gSVMHSOAq1aIRKfJ_jI2wWTAJhCUgQWA_87MoR8_wlgvzRPwrwTflgouVVOmEgRVodLi-F6-IpKuM9GNkFWvNRWq5urrmGaBxB94gS_wpUO3OQkdH4ZGJdAJDSxTHmRzBCJWDleyMtj0uymoMM6zZlpTWGEMUtlhFy9q_MqzyMsOCAdAKdezDrJdkM5luykIvDdGfn-w-DdmBhLSO6Y5Ldo3vrx2IqstOl1OWc7BD4Em0GPxBlS1ZI9S5Bsa8lfPJiNbB74doWtOaFUU6OZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله نظامی سعودی در منطقه بنی بکاری، واقع در کوه حبشی، غرب شهر تعز
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/150901" target="_blank">📅 12:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150900">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EysiYdyWZQIiHhqSNDI24bQmTIXckPOwacmgELMz2ENSoo2BcE-kds3XqkEg-V6b4dJ-WMm6idDU-5d3xL1TfSQHgCjIKy_biKm9QHZ1ZBPuCV_0fAYXk4SUEaCnmBIJo-1TUmO-D2iL7bSHj55iHhjN6vLqqL-ChugYu7te7z2JEzU3bvP007xALAcXaJpn_oPnNq0VSbvY0UR5Qbsr1KCSJMc1bac5j7Y3kivXwUU7UlpFjWQ7sEsaN5T85gBBkXTgcWEL5h5CPMaUfIP-ZnvDeY9DPSlqhOXUQ2DcWDfCyLIUfy7qRohNlW_unsw3DrmnBCdzrnSAVG-K1pxmpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز تهران _ نجف که قبل از محاصره هوایی ۷ تا ۱۱ تومان بود ، دوباره برقرار شده اما ۴ برابر رفته رو قیمت و شده ۳۰ تا ۳۸ میلیون!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150900" target="_blank">📅 12:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150899">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
شوک تازه برای رانندگان؛ قیمت باتری خودرو تا ۲۹ میلیون تومان رسید!!
🔴
قیمت باتری خودرو در فهرست منتشرشده برای 12 مهر ۱۴۰۵، از چهار میلیون و ۹۰۰ هزار تومان آغاز می‌شود و در مدل‌های پرظرفیت به بیش از ۲۹ میلیون تومان می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150899" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150898">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این وسط فیلم....... بازیگر تگزاس در اومده
😐
📥
مشاهده فیلم</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150898" target="_blank">📅 12:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150897">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ec665133.mp4?token=dMqlQRqrBT85tseeCwHVmFoluBmYWW1Gb_pvZM0gaAciTqCn4rfsSn7Ishozsq1AvNo1F8TdBQOukzNQd8mfUVe3uZYsbOl65qhIBhjMafj_MpH49SKondz2mYaRaAfBZVJpjjmCitCeDDuNTkgZJFQfMxD1cgqc1d_z9ggSGrVCSVQNRpzckpnxi1fStBbj9nRc-NIgAQOgS3yjrTRm6nvTPH8hg9hASA4p8fFFZd6XI3MDSjGvlhgd9UB6QTDOmjnPW-iEyYLtMLLRiDnCEJt0RQBKaNCZsIfZTSEXquWMM-xQ1m2IVk1yOft7nwdCiVuC28eqQCU1vf-WrGI2RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ec665133.mp4?token=dMqlQRqrBT85tseeCwHVmFoluBmYWW1Gb_pvZM0gaAciTqCn4rfsSn7Ishozsq1AvNo1F8TdBQOukzNQd8mfUVe3uZYsbOl65qhIBhjMafj_MpH49SKondz2mYaRaAfBZVJpjjmCitCeDDuNTkgZJFQfMxD1cgqc1d_z9ggSGrVCSVQNRpzckpnxi1fStBbj9nRc-NIgAQOgS3yjrTRm6nvTPH8hg9hASA4p8fFFZd6XI3MDSjGvlhgd9UB6QTDOmjnPW-iEyYLtMLLRiDnCEJt0RQBKaNCZsIfZTSEXquWMM-xQ1m2IVk1yOft7nwdCiVuC28eqQCU1vf-WrGI2RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی‌های مداومی در پالایشگاه آرامکو در ریاض رخ می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150897" target="_blank">📅 12:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150896">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rh3K_u67nXF8IByHQR9G9z53bPpnN8QFVDUk-WYk5yCUp5vmleclzuRHN33vN9x2EGy9A8OkIkB-rFuRvmWJ_mUI-u_iAIyISFGB12A_5ilQ_BLNhdIudKwCmpn0j8_6awfDTTeD7iPVRvCKjIXhSs_RvYKuvXSq7BV2QW_v3w74YC81di8Ni2xZvhBRcQz993JaMXG6l-lvSAEDLKVyp-Dg0nQDNFN8mUwu9ZKi-m6v3R4zST4UnmlEObgwXiPjreKjsKZosCwSX-zSErHf6J4riEW1UODxhd0-PjXUQIZQVfJx-tGf1NmHZ4WuZya3QwTk4RG950oPIETYQSUEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس جنجالی از بنایی در ترکیه؛ شباهت عجیب به آرامگاه خیام در نیشابور
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150896" target="_blank">📅 12:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150895">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/631cd6d323.mp4?token=mYRtob7BvlCkMs5gUxj5IBVNXDd7TslCoJUZBllMtx5Enlba80I8Tv4P7-AzDGCEav4fBUJ1lWDu0OuuYWaJB0-gzdxV-0xC92uPcsHBQgBM9V2AF6CJ0iFMnG7oBO2cBleDVPGZafWkVQPEHfWHISs2OKWDz51SpinXG9KQ5GdsP1dV_MnaH1vcUzZdjVkeI24T1Kt20XUNBs84jmYZ5wSdElXC735IaywZI60StboqKwmToNG08VEJvW5G183sMejaVedgz9u4lQEo5Ik8OsX12w6QmJLDnW27QgNXZHGeLaziJo8XAb4_HYMVMbGSg6MofJd4T_EvvWh9wqHqvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/631cd6d323.mp4?token=mYRtob7BvlCkMs5gUxj5IBVNXDd7TslCoJUZBllMtx5Enlba80I8Tv4P7-AzDGCEav4fBUJ1lWDu0OuuYWaJB0-gzdxV-0xC92uPcsHBQgBM9V2AF6CJ0iFMnG7oBO2cBleDVPGZafWkVQPEHfWHISs2OKWDz51SpinXG9KQ5GdsP1dV_MnaH1vcUzZdjVkeI24T1Kt20XUNBs84jmYZ5wSdElXC735IaywZI60StboqKwmToNG08VEJvW5G183sMejaVedgz9u4lQEo5Ik8OsX12w6QmJLDnW27QgNXZHGeLaziJo8XAb4_HYMVMbGSg6MofJd4T_EvvWh9wqHqvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای حوثی به پیشروی خود ادامه می‌دهند، پس از اینکه کنترل دره البرکانی را به دست گرفتند، و به منزل رئیس مجلس نمایندگان وابسته به عربستان سعودی رسیده‌اند، در حالی که درگیری‌ها همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150895" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150894">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رئیس هیئت‌مدیره صنعت برق:
احتمال خاموشی در زمستان به دلیل کمبود گاز وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150894" target="_blank">📅 12:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150893">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
مجری شبکه ۱۴ عبری:
ما او [خامنه‌ای] را کشتیم اما هزینه خاصی پرداخت نکردیم او که مرکز رنج ما بود، درست وسط تهران ترور شد در حالی که فکر می‌کردیم ایران کار دیوانه واری کند تنها 40 روز جنگید و سپس به توقف جنگ رضایت داد، 2 دهه ترس از پاسخ ایران در صورت ترور خامنه ای اشتباه بود، ایران اراده لازم برای انجام کارهای دیوانه وار ندارد فکر می‌کردیم حداقل کاری که ایران کند خروج از NPT باشد اما این کار را نکرد به هر حال باید از نخست وزیر شجاع خود بی‌بی نتانیاهو تشکرکنیم، زیرا او بود که ریسک کرد و پیروز شد، نصرالله، خامنه ای، فرماندهان نظامی ایرانی و دانشمندان آنها را کشتیم و پاسخ تنها چند موشک بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150893" target="_blank">📅 12:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150892">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
بقایی: امیدوارم خبر اعزام ۴۰ هزار نیروی پاکستانی به عربستان شایعه باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150892" target="_blank">📅 12:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150891">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بقایی: اگر در آینده باز هم شاهد حمله به ایران از خاک کشورهای همسایه باشیم قطعا به شیوه‌ای متفاوت پاسخ داده خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150891" target="_blank">📅 11:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd3dfb4ffd.mp4?token=W05POvMQZ8HdxZLjoEZMhuGDiucS7EYjZI8P_Rj9Xz7Z4jV8KKhaIsCqw7VzdU0OIImE59Ea29oM-M07P61-jh1dAG8YYotagJEAohSbmsLdr31Md92O22xRkLcut5nhv6BjmUQxjJEWq-1gI8aDD-c56xUsqjTV3EBk3XStYdVVZCFraPEhPnT_ehDAAMuEEArS4_ofC-RiBAGAcIYruWxPd73pPiybZO3aX9KgClN2sN5wl4Sb0iysOmihonHL-8WDECulNM9jZVWfOYrQhkzW0CNLQD3UDrOcIcYMBE4IYuQPQCCGUgi_xxUnuCe1FpbQzruhYQ4ZHhzNiwarkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd3dfb4ffd.mp4?token=W05POvMQZ8HdxZLjoEZMhuGDiucS7EYjZI8P_Rj9Xz7Z4jV8KKhaIsCqw7VzdU0OIImE59Ea29oM-M07P61-jh1dAG8YYotagJEAohSbmsLdr31Md92O22xRkLcut5nhv6BjmUQxjJEWq-1gI8aDD-c56xUsqjTV3EBk3XStYdVVZCFraPEhPnT_ehDAAMuEEArS4_ofC-RiBAGAcIYruWxPd73pPiybZO3aX9KgClN2sN5wl4Sb0iysOmihonHL-8WDECulNM9jZVWfOYrQhkzW0CNLQD3UDrOcIcYMBE4IYuQPQCCGUgi_xxUnuCe1FpbQzruhYQ4ZHhzNiwarkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بارش باران و سیلاب شدیدی که توی شهر ایذه، واقع در استان خوزستان رخ داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150888" target="_blank">📅 11:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: پزشکیان در روزهای آینده به ترکمنستان می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150887" target="_blank">📅 11:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: در مذاکرات ما به موضوع هسته‌ای ورود نکردیم
🔴
ما فقط شروط ایران را به آمریکا ابلاغ کردیم
🔴
ادعاهای مربوط به موافقت ایران با بازرسی‌های آژانس بی‌اساس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150886" target="_blank">📅 11:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150884">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b636ea50a8.mp4?token=hY0u5cvV1KYIE-m4NLvIjg9-tPv2tol8eLRQMqxs6CUpJ1sIfKzrkt2LfNTZBliuArtlmoXfF4t5HmMkQsWdZRaJJhQJLF_s6Eg9VIyjFj0D99YCGC_cQsipBSfENVHaaqZKKvq_cSFOWn9VvWnAXIyjin_nyJG7IJXgHYMNm84-Ow8Kjslyhm0XXZ4bQzxLkusYudWZWCnv2wdaFz5e720yYCqJ_-7iSaY6j4bwuEK-8cN-AnRwDZRSl3UGRt5Zpqz2bktgE-K2vXVH7I4Ra7sVciFzfFVL_LzEVhlZ7QwNTrtIcWBOon00I9Yu_GlFBP1M85itWhZsQBsffIqhXg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b636ea50a8.mp4?token=hY0u5cvV1KYIE-m4NLvIjg9-tPv2tol8eLRQMqxs6CUpJ1sIfKzrkt2LfNTZBliuArtlmoXfF4t5HmMkQsWdZRaJJhQJLF_s6Eg9VIyjFj0D99YCGC_cQsipBSfENVHaaqZKKvq_cSFOWn9VvWnAXIyjin_nyJG7IJXgHYMNm84-Ow8Kjslyhm0XXZ4bQzxLkusYudWZWCnv2wdaFz5e720yYCqJ_-7iSaY6j4bwuEK-8cN-AnRwDZRSl3UGRt5Zpqz2bktgE-K2vXVH7I4Ra7sVciFzfFVL_LzEVhlZ7QwNTrtIcWBOon00I9Yu_GlFBP1M85itWhZsQBsffIqhXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله موشکی روسیه به پل مهم کی‌یف
🔴
پل شمالی کی‌یف، یکی از مسیرهای مهم ارتباطی پایتخت اوکراین که بر فراز رودخانه دنیپر قرار دارد، هدف حمله موشکی روسیه قرار گرفت.
🔴
این پل از مسیرهای مهم تردد میان بخش‌های مختلف شهر به شمار می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150884" target="_blank">📅 11:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150883">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
بقائی: کمیته ۶ نفره شورای عالی امنیت ملی پرونده مذاکرات را هدایت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150883" target="_blank">📅 11:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150882">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رویترز: ناو «جورج. اچ. دبلیو. بوش» با ۴۸۰۰ سرنشین خود وارد جزیره تفریحی پوکت در تایلند شد تا پس از شش ماه پشتیبانی از عملیات‌های آمریکا در خاورمیانه، تجدید قوا و استراحت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150882" target="_blank">📅 11:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqb3h_1_OrZKMt03ttcprn1Lb3NSMNUSqFQw_YbiY93RSo1aEUXDxIYYzKzjyBPj9uo8Al6Bf6TD2jSSLpIzLbcRtaUq2B9LYoUDWITaREkWE-eiCMT_5oeTHOqzgIKxIH5YSVbxayeAJZEq9HsHLFPu7GLOd_2SFw7whvBtPpeXp1RrNYIfoxDhRd9ecU6VDsCXVeSkFJoTEWZ6xXWlc-AivaZlx3ZBdhwBmmi3fpHYfEKZFgp1j5tG46qk7-siWF2_vlycoRU7G4cg0GHOwOC4hNq-EU5ax-ybqrlqWkGLNsUwtru5PZLyC8xknp_vTaYJiZ6jDmZYNLmByVqZ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران‌خودرو قراره ماشین جدید خودش رو به اسم «پژو 207 الیت» تولید کنه و با یه قیمت نجومی بکنه تو کون ملت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/150881" target="_blank">📅 11:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150880">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219d012c04.mp4?token=IUB52jloCIOlmgwc-5peTJXoOcwMfyz-7Q6pre2vrXhiuRYy90YQal1u-VStr2x8p5aHMi7qLGmqnzeV8lgxTaMT5Qn0lAZywr1NlB6eu0Ce8U5MfWqdy9_fgEOpVmV-NhefYeSmUuO8dzojSEJRaaOt-sOEZdAiaXrMsrY2WD6aPIxjrZ9E_-KJMET7_jgBHnYJfNnvUzSIluMbPsAgZdZR_XS8iKt46eP_rrc03n6RY3sc46_J4i6YoTVxlzds3K8gco1y4HDRikiguxLw0v39AFIDIn8J1zWPLbh-oUReOKhZL0SqSPgUT5WxPSHbsDT8qL8gX4W94wCmnaUkKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219d012c04.mp4?token=IUB52jloCIOlmgwc-5peTJXoOcwMfyz-7Q6pre2vrXhiuRYy90YQal1u-VStr2x8p5aHMi7qLGmqnzeV8lgxTaMT5Qn0lAZywr1NlB6eu0Ce8U5MfWqdy9_fgEOpVmV-NhefYeSmUuO8dzojSEJRaaOt-sOEZdAiaXrMsrY2WD6aPIxjrZ9E_-KJMET7_jgBHnYJfNnvUzSIluMbPsAgZdZR_XS8iKt46eP_rrc03n6RY3sc46_J4i6YoTVxlzds3K8gco1y4HDRikiguxLw0v39AFIDIn8J1zWPLbh-oUReOKhZL0SqSPgUT5WxPSHbsDT8qL8gX4W94wCmnaUkKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار هم اکنون 271000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150880" target="_blank">📅 11:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA45Iq23Z29W1rDccdqAxIfTl-XfYAxJsAnQcg7SeAK5W2uScHjs7m9avMLFfObiyMiLNgg9EBTTRaLDwpVl0exjpcou5H15nMTLlmsk7T9MnVuJHXvzFvzrLYyGR_lSSHxwqItTmDuQzfWDcmNXbE8weExIV5htyZupPxPPp8xuqFaUDcxEMah8zKfo3wuXIRuqZlQ_BVRWxJXlLiEyGRA7y7Tvmg5X3pISIBL928jdARvcNZHq3Ku15WCDm7mkQAxikzzNf9_5snGhll98_dOicmnmOv_V-lGJRvqPXE0Fi-IyQifJ6ynXevxv3v1T0mrL6vPzpMGVY7v9Iya5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان دریایی بریتانیا گزارشی درباره وقوع حمله‌ای در تنگه هرمز دریافت کرده است.
🔴
بر اساس این گزارش، ناخدای یک نفتکش اعلام کرده که کشتی بر اثر اصابت یک پرتابه ناشناس آسیب دیده و اتاق موتورخانه آن دچار خسارت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/150879" target="_blank">📅 11:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150878">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
دلار به 271,000 تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/150878" target="_blank">📅 11:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150877">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
عراقچی: بیش از ۵۰۰۰ جنگنده آمریکایی برای حمله به ایران از پایگاه‌های اروپایی بلند شدند اما پیشنهاد ما به آنها برقراری گفت‌وگو با ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150877" target="_blank">📅 11:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150875">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baeeb81cb5.mp4?token=srwLGf5IkWzdyywIFTbkkGnT_MVUv_nhxFfZ7tl_3hFNzGOskah5M62gsSHIXMg_wov7ret0DQDQK99n1RMFpyBsiTEfwN4lwkMnbaunx6CLml7HKW5ruEj2Tpxtt-AWh93DyiyD40jTyGdi_dkDk8gLljA4IKZvwsM0lNKQrgd9QGU-aZ42O9cPKcBL7EEv1mHkxA_AsSIG7_PlAdyyejaVNTpCUiC62alv_xoBnp5GIMiTnIFlo2u4xNiZ2i92BqPnT549R29_aJxpIvYStoq6iU7cBhyU4Yx_qWEsNrnZPeueZ_Z-Smxohy20oxMxPEqPeOvxSwQTVTbhtdiErA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baeeb81cb5.mp4?token=srwLGf5IkWzdyywIFTbkkGnT_MVUv_nhxFfZ7tl_3hFNzGOskah5M62gsSHIXMg_wov7ret0DQDQK99n1RMFpyBsiTEfwN4lwkMnbaunx6CLml7HKW5ruEj2Tpxtt-AWh93DyiyD40jTyGdi_dkDk8gLljA4IKZvwsM0lNKQrgd9QGU-aZ42O9cPKcBL7EEv1mHkxA_AsSIG7_PlAdyyejaVNTpCUiC62alv_xoBnp5GIMiTnIFlo2u4xNiZ2i92BqPnT549R29_aJxpIvYStoq6iU7cBhyU4Yx_qWEsNrnZPeueZ_Z-Smxohy20oxMxPEqPeOvxSwQTVTbhtdiErA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در پاساژ خلیج فارس عسلویه
🔴
مدیرکل مدیریت بحران استانداری بوشهر: از ساعت ۵ صبح امروز، مجتمع تجاری خلیج فارس در شهرستان عسلویه دچار حریق شده است.
🔴
بررسی‌های اولیه حاکی از آن است که اتصال سیم‌ برق عامل شروع این آتش‌سوزی بوده و شدت حریق به دلیل سرایت شعله‌ها افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150875" target="_blank">📅 11:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150874">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4SaIBHR7QN89G7tLIUm-ha-HmAMgKZjT-m4e4iV2HqkJITuu-5vyyVa99DVkO8O9oshA--6AEy5ApY3wFiKx5RWEoPVKR3S9qyM7Ab5Rnf-yOX5NmdR9ulDnjcJNZKJgRuvNGTiN4Lspw0yp8_RofZmB5Hy82a_fFOwnoZGURpNSGAK9YXKL1AQt2zZGO6sGH8WZ2CZzLeRqX6h9rImkEHdrQCKrmEQciiGeZS86ikC56ZJr2qcK6QkNvSrb-fULtsDU5xT4WFcEP9KlXjPs3r_7HfiOjcMoGjAoMbsWQBI05_LpiScW0qjgiQy2HqPDN1jS8oz1PexTQXzK-bQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماهواره‌ها، دمای بسیار بالایی را در منطقه نفتی خریص، واقع در پایتخت عربستان سعودی، ریاض، در ساعات اولیه صبح امروز ثبت کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150874" target="_blank">📅 11:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150873">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
روزنامه یدیعوت احرونوت: یک نگهبان امنیتی سابق در دادگاه بئر السبع به سه سال حبس محکوم شد، زیرا حدود دو سال پیش با یک مامور اطلاعاتی ایرانی ارتباط برقرار کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/150873" target="_blank">📅 11:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150872">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slOHChprruebmlJPdVoKjOcF5r09DDh_jefbWg6BRdxjCNsh2n7z_lslYID7u3rEWwm3rPGt7nKai4yXTJN6c0KnsBi4RDql5Ulhh2Dk99D01vJC72mIgy6pvaVy_GKVyibWGzS2U0-DdRsStDmNoXjk4B9-EdGNK3lrgHbGUKm0YEop6iaG6D0W8qo3PaPkerDxXlJuUVKoj9hD5nviF_NGep4bHv6UNgPiueeatzf0n0SY7JbxrhLOi03ELoMQvbTXxC80hb4PDMH-DRGaJ5USpwg4Ot8UcE4hk3EXJMpoIlAdtSC9OofFxRON8lC1m9WmNei7yRdJ6YMlgVKCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسامی جدید تو تهران
🔴
میدان نوبنیاد=شمخانی
🔴
بلوار دریا=تنگسیری
🔴
خیابان ارم=خرازی
🔴
یه بزرگراه جدید=موسوی
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/150872" target="_blank">📅 11:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
قالیباف: در خصوص استیضاح وزیر کار تصمیم‌گیری می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150871" target="_blank">📅 10:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150870">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
عراقچی: هیات ایرانی از آمریکا اخراج نشد، ما طبق برنامه از پیش تعیین‌شده خودمان رفتیم و برگشتیم
🔴
همه شروط ایران برای بازگشایی تنگه هرمز منطبق با تعهداتی هست که آمریکا باید بپذیرد
🔴
امیدواریم که آمریکا راه خرد و عقلانیت را اتخاذ کند، هیچ راه‌حل نظامی و راه‌حل مبتنی بر تحریم‌های بیشتر وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150870" target="_blank">📅 10:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150869">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68bfbde948.mp4?token=kkoarO6QGwF0iNLp8qLM9IVJfQmrbgbEMbfh8O8fMW2qUtHdEILgD_tNcoNqVdfg75yPNfPXY6oBr663T_QsISSUvSCDE4s3jTSXq4hgHYnWPG_qusbw3n2L9LsIUxUOADG4haQA0KTTALDPb9wy9Bdgk9MQyKonKbZb7rxdJAuSYX7uoKoMNEFS11rlqpwrcImnCjNv7TeiwxjhQHhXzy-zDMFKHeJuTOCYt6It_9pLUmOYH2gt80HsJa41GGTJ5wSsE9-1EvEVlMOTG3obpbMfbAxE3yPBVKQB7XN-CtuE17Ek-mvq9BWdP0htil5RrsuXKv2-LJP5aDKgnvnF-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68bfbde948.mp4?token=kkoarO6QGwF0iNLp8qLM9IVJfQmrbgbEMbfh8O8fMW2qUtHdEILgD_tNcoNqVdfg75yPNfPXY6oBr663T_QsISSUvSCDE4s3jTSXq4hgHYnWPG_qusbw3n2L9LsIUxUOADG4haQA0KTTALDPb9wy9Bdgk9MQyKonKbZb7rxdJAuSYX7uoKoMNEFS11rlqpwrcImnCjNv7TeiwxjhQHhXzy-zDMFKHeJuTOCYt6It_9pLUmOYH2gt80HsJa41GGTJ5wSsE9-1EvEVlMOTG3obpbMfbAxE3yPBVKQB7XN-CtuE17Ek-mvq9BWdP0htil5RrsuXKv2-LJP5aDKgnvnF-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: از امروز خنکیِ دما در تهران کاملا حس خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150869" target="_blank">📅 10:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150867">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
عراقچی:‌ اگر ‌آمریکایی ها مجدداً به سمت راه‌حل‌های نظامی پیش روند ما آماده‌تر از گذشته هستیم
🔴
برای دفاع از خودمان هر اقدامی که لازم باشد انجام خواهیم داد؛ اگر راه دیپلماسی را انتخاب کنند، ما همچنان آماده هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/150867" target="_blank">📅 10:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150866">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhDHNJ7_EVPXq8b-aTw6YgwnyWmFEVeXiep63OBoRsq9aOvlINLvEA-jpLTKSPjBnzYP6JbG8M4DG35J9jC5yat95_sbgUAHFwxwN1nX3GdAaRLn4k03ZlkRSrKv35bPVNFpTZe6jt_gvtuGgVOffS0BKZTvaW5OQ_R6m4xfLj75mrwd5LFDUFCyVTS5UtGXlDGSHOiIlwlzhviR1n7kMiaTKKvcXfK2RkgrEcXVNMxjnWdYeELoYWn29cXGvB4gszI71jxMtjf8FMYWZbPDp82U0xsj6jQ1rhTMQQeT6nbELdHdOmIGrBqKsCP1Bm60Z0i4-WWNwuKuyC64YzSYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: کل پایگاه‌های آمریکا تو منطقه نابود شده، من خبر دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150866" target="_blank">📅 10:39 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
