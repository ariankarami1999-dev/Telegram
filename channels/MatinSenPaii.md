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
<img src="https://cdn1.telesco.pe/file/qMzAWoUUxrpB7f0tHMj4z3wZ22YfSv__GjHBcj7jVBwYUI7tTTvEvzspa0YsUZZyJ6SajzuA8CxZ1bLNIS6Ib7lrOQMYCt5n9qBoFfts8WY5PL5HaxkL0VsDCA68neHlfeW0tdfnozkkctmasElkp6GnIW_H4eBeSyT3KqfC5vRpOZTYM7tWj9e5hD0shN-RXMk8Z6NGm6_ibDmlfLpvN9wSCq6rN94br4wgJpOxCyrGTJ43RQFvxyORN6WeFfxlajQYL3sudvkTiiamRZlTw_AcajyC_QWD1ynSaE5PrCczS8ILJgqwWMtA8rZbpW5EH-Mjr7MVL1db9JMPT1xjkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 05:38:28</div>
<hr>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RUdasHMFJwkUUQXoWGBkj7A-SsW3Ps9nm-LhcVoEenp6gZ3Y9pWOKetnPd9Reu16pB-z9hzUJafsxvyVbXA7N6s9-0taGbM7DwuL-RDSl6akHbr_YIk8SA3oL6xSp8-7yzrAYhG6JDOXB0vrIneuMwBlxAVwlMdvIRw1nfrYzLBvcg_JM4QnkjN1eGp-7tEU7RQA2RJAOw8sXbsV_SffSF3j-7rWFIEe0QYpvyyNjsOV1K3hxUZlzff37dSjI_np1CTKvzevE3ISxcvtmaJy7fKW7g4z_lhuEb2gllB4fgTI7UckoDG1Jh_iuprwyLUo66duswOZT_tXqoHb41JIQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/MatinSenPaii/4938" target="_blank">📅 23:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nu-3gEcQtqxYMtRIiIped9BWvY5zD9AlFaESPms4Fw2-A-Bx3ugIGbLoxN9FXixMPUNg_b8eDTneoQjTn_GuMTPa8T9adH40L4fOW4dtmCBGDSKv-UgKUhiQxNqxpRIaJ06nS-NoJ3yzPUi76-TTaC08FAH7itgTjjrlaI6o-l2fMEWjEoBwn-hQHafS518ZfQrxvJYghxHqEXJe7EBMo50wFu1pV4LTHw-gTS7r7znsKgC7G3FLtppmItHPMoRTEclUt6i7Kuk7s9iRbT7g3Wsv1iP9t17NPqziqEuhfrKGV7teqgDAAI1HMfX99l4Hdcl0HcjPwP6R_mAnkgmtYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/MatinSenPaii/4937" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">به همین راحتی.
تموم شد و رفت</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/4936" target="_blank">📅 21:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fJAPHnyBF-yWy8wQFMHdTsqavlSt9xJZdcjXUcohGH2ObD4hnpW1GRjHAMGzfGFLdq5FiZMOsoks6rQbVn3Ay4P74MTR9_jYnEMSEDcO4p-8LUyhWv6kLJ90OKiZoCFCVFB-CrkgaeM-k-pPxiHN1JDOgo7hrcREJUQs_PoT4F3aPCf0DfiH25cwa2eo4cT2UtI56MXqZkrdkd3xuuf_Gqrd9A1QlcJxB_5iv3EbcSluaFmgtWcOQ5zJ3XZeqN51n1efkfrlyVwld8iTF-urWQYbg9ROk3p5Ny0yGwKugGe-GaDJjH3IrfDxCbDgSlaHhNWEi3hMHpVOwZhEspiGIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/MatinSenPaii/4935" target="_blank">📅 21:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZyQWF_n0JhEtaHjDKT1bj41pQuNiF-vcAhAu_6_o1MIYte_Zez3AgWq9MYKB7Oxq0xsheEewlQr7EgYyEUujAEXjUE-Ay66QFCfvU-divTA99e9D3WR4c-k5V735wa5vbrQ-D92V6yEVqpJVAWHQC5nnqyfoTrTe97FFXY_EYfQxofR6w70kMvIjC64LquC00hrszGw2DVddrPfIZPuizt0YD4eClp0mPvRFzuT2MiUGoQzESq-GXwCTAHg08cftyqu6DzWx49MES4aN59vW0v9MFpvEM5lTqwWyr8_EFrnbjJpHkvsX62gmwFmk13GoTV3rDeCoqydz6qLQg7gA0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/4934" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WIskxBn0hiG7wTmnJ8bCT6Gwd0j2Sh-pncj2Omce2rs12CjOAuhI9V7NlaMrHHu48sbXjQM5XQCJoWoJFMGfuCx5j5tMbzH-ktcP7CFNR3d9h1l1kuFmOhTZRZjogxy0aWk0V72OlYYaYc4BP2yJSg5-pxHI65PU2INuNmHgg1fE2VeNZq8NMVhkxw9fjwtHtCuaggpS1RGErmD_rpkS2BNC8K5LaFKn8G4gbjDqXoClQpCTqyZlnvcOS-Rirsyp0qJC-T9TzY_jBQu-9REHl9J3FDoitnItG-cBjABgqXxTtK0nGEkGTjMD1764nop8L85XjCsrfO49x8kHEQWKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/MatinSenPaii/4933" target="_blank">📅 20:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eZY8r5PseT6vCRi0Ovio0ZOvsdQNDHG1UHyG0InRkkt5kd0qmAaIGrBcFTn7XHN4aZJ6isEzDcj2IUlDhrraSqzWQV3UmvbC7N00SqYNFoL5ajAZyKYAeadcDBOLGt5NFAa46KKqSf4xWkU78YI4gL3qoT77xIG8XgTYXZZpciadBT6VMGEunRaUxz3CAQ6qHVa21tjoq0vE5m3yA4mDqPLCkBNz0fvqN-rA_Tx-Den46aOSSvAMeeM0zjg5EXLC6QrajTPIdK4Se5uFez8gGXei3DSM_PkwvOB-mSi0RILHA6rtsvY5BOQ2AJBiLiPDaqS68WX13m9AjD6pRbqUFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله
محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود.
باحالترین قابلیتش اینه که میشه Mode شخصی ساخت.
و از معایبش هم که بگم، درسته UI سبکه اما کاربر عادی ممکنه یه کم گیج بشه
و همینطور فعلا توی فاز تست هستش
و ساب ایجنت‌هاش هم مشکل دارن
پیشنهاد می‌کنم ستاپ فعلیتون رو ول نکنید بچسبید بهش، صرفا در حد تست
مدل سفارشی هم که می‌تونید اد کنید طبیعتا. من الان OpenCode Go اضافه کردم</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/4932" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WvIrVXaHX_9AQTBk29UWUNuKehAXPHrCc-KXkjQ4d97G-_yii8xEq4YbAJdvmQTiy7rb0rwvNZYq0rpEu-a6MdQcXMfSw0qLjEEttBx8rqqZFQjj5nIG4aif7J83J0REtt0PE2e_VXc9BQckWjL7hpP4iJrEiZ_m2EbnqWZTPw6Lp1BXyvlXHAO1m2luuPoV-JUFmRq2LOnNmmMx-6CyL-sMnunz1Lb9TC11RIMuNv0H-TGrWzhdb0d_9mavgdHr6tlT_kTgh3khLnPK4pHRMA6a5EMQTYpQKxktWd7zZjSx_XJgoal7u3vDKoITX_KtNbCYFL5GRhP2uoZ6dpVj7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود
😂
😭
اینو چرا پوش کردین مسلمونا</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4931" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔺
ابزار کدنویسی متن‌باز DeepSeek Harness برای رقابت با Claude Code معرفی شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/4930" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rtb7ZoQLAclqVzHoM5dLoOhWI_brMrQ2vejfoa_O3Tl55Iu5fP26d3LrI1BeS-C5m4zFiRPHvOQRFfxu321Tb8kI-lYpJzFzgvcpy4DQmGgQldnqieX7pOLWC6rHdnGNxqczIyCuUQSzHtZK3yumKBfXUtTuH-FsKaGVfoYEFXR_PncSqkuxiUPzA4WY6cmpbysQdqKEhImUQSQld24loEZnmoXXdINo2tvoUW-g2JOHGrIkOnx2iU31Hf2YmtLRH3c1yJPzEA5YcafMn0oVQYB0MtRY4BAU2UtNQSTMfvX3sQcZ9jPpjTiKdaHQOSW4Lf2HDnO1ApZdy7uPOLtOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه قابلیت خفن برای هرمس ایجنت معرفی شده به اسم Bot Mode
به جای اینکه هر بار سشن جدید باز کنی، می‌تونی چند تا بات جداگانه بسازی.
هر بات پروفایل، عکس، توضیح و کار مخصوص خودش رو داره و حتی می‌تونه با بقیه بات‌هات حرف بزنه و همکاری کنه.
https://github.com/NousResearch/Hermes-Bot-Mode
@RepoFA</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/4929" target="_blank">📅 18:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جالبه که من دقیقا سر Kimi3 هم همین مشکل رو داشتم توی کلاد کد.
الان توی OpenCode + DeepSeek V4 pro این مشکل رو دارم
سر دیپ سیک فلش هم داشتمش اینو توی کلاد کد</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4928" target="_blank">📅 12:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uYUEspiy4Y7W51wyDlOX84IFH6ziE5RYjakEf4IeqWLJW3QFOz7uqujEizO6DFv1G6F4LoUAhy7jQBmP9pFJQUre2H18g6-RnxgB8gFXw570gSrpMJRa5q0aRUmvpxqGBPm6NRRNarvKTWt8Fa_yuHDIUp7UnCNmS_NrVYVdKXHlIQX5WI9njPiy3W1pXU5uVHvxbcDA6d7sLpUDRo5urhD37D2x0Tb5qn9Xssx4dBo5lg_kf0slAd-3LM5hssGpFlfxTh_I_XIi9QQNJFS_4MY2z61cZWl4pTaJ6H3vsTC_-Ihfh9xhH71QG6bGsOXaSBA4mCDdKD2-i3fxCjj4vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا عوض کردن VPN فقط باعث میشه که از اول شروع کنه به Think و من اشتباه می‌کردم</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4927" target="_blank">📅 12:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4924" target="_blank">📅 12:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4923">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c15mQx3uxxVYkg9RA3g-tgQfvGU6Nuc_57VQjrLqW5ehxkUM_wRDvpTnfcIHN-umSHnHzjwy_5yh6DaHIIqT9CKYTbSMKjLkRGBE00QEGcR9KW9Hh1Xz4OQRijNsQk0hAF9U09vFyBHaHqAHQDlYJ7iTBXTIZKHRxGPfU398m6Tgyrj-ALua5udgrfJRia2b93dcJ1HUdLwYB-GcMJxT_i8ChhitIKznkdfx-cSIUNs2xQIyzILvYDrZnAWC7feDZrGxwt0HvhlHbh9KaDwmSwLPZOLKyFGtB3zHs6th-muaaiUT03T9JcdSvLY6-sDTOqvp3p5rtpqYE-WJ5Fz1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو
تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4923" target="_blank">📅 10:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CeynBGKW3c_hNj3dhSef1nDS6zybXys20AdA1KvFe1r-qCUYlnPoOAr-XTDkjdYL2Bgtem56sKjm1EA_AM1V3faW9ay0cI2_IStC4oYoywpEDbWzYtl0sGg15kBidj8LyBNC2sOzHClzfBnJtlnkiXshMXexugqPldcULzgX-B835aqKAOwqcnYAi1SnvNUu-Yrv82K0nD50yKit9Xb-i8tnnmqlrOMa2jJsi3pCbF73qPB_o8Xmvr46WMlr_Dkl76LxTsEQ2TlWZ_aXfYgLkk3fJcJG8DQ4Sds3Oal7rGzVQeSC0kS9CJgQdh41pe-AHmV_vtIsPxsZshMDhhoQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از پلن فری هرمس که گرفتم</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4922" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lbYT84ojLcLIdNfN2eA3s1U2lM4tzKbGnh2O8aU37t1BN58uprMgvN5lmKzhvL5ahe7yprhsFBaqbqL6ppRPz4viFa7faSeOblAf77YEvAhvT8n3pV-9c2wHdsSQ43B484sbK8bI0vb1C8k6x0mLSPsFkunUmYDzEmt9MIBMVQv1eAOxPs9FdHx5JJ1oxgnU-E1rbvw3SSeOp5D69T9ULQ8I20oCw0Iro3jv1ZDhhabpvSEndVMxTAE3BVs1Zy2BWV4DPY1qwDFu5BdQxDia7IxC05_S1FjqlrTLPQKyeL8yI8FFurnng_cqWcGRLH50QCcGiK4lEqmO2rHHMnD5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4921" target="_blank">📅 20:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اگر روی 9Router+Antigravity به ارور 403 می‌خورید، یه بار اکانت رو حذف و دوباره اد کنید درست میشه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4920" target="_blank">📅 20:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4919" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QSnfDZ4Njt-jenm4dDWq-Whe39pQRPKPhDOcTU3rutRXh3PCn6D3TO80nJ_G7LTwsALtIVxX5ouFMPiOnYOEQlpj1ZFOSo9ibCbHPj7caqS05wg7iRVXzmP-ZyiXqSfx7KqXXJIFW4NJ7Ezlb3i7bxqrWEHLJ9Q5rcftKaDGUkuVb3sKNrSK6WXbmFpx6QyS9u9GBh3pJghyOExokaFOn5fWR9w0yx5DnmAcXExJVshWt83l7F3jLdMwRyTJKP8rk4UtD-01PO0lK8SEVmzk-u4xWiTduTMhylKMRwEfOX1_3wEG2k3v9mh6uos2F90Or5LaTxuM4IpyWwnKgWEasQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4918" target="_blank">📅 19:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nfit67JKvdemjxXRnb1TipufJGEah6ZoLd8jWAtQxbTRhRo-P0KIr84RgV6feDMfzT9nAadoClGu3q92sitYSSfjlBepI77ZKhk_FvIsj-x-48CR7-3pq84EypXpnCVwlSFz0BbdONkGX_R_8LOGvGj_rOyVxgFPacWrnkqikUCfXFvnk4LBRZz-v_-Fp62BrxQ2uKfaz-4zJVOYHJV44ExargonL30vZ0AefIqsaY2fYZ3VBzukuHMTEy3oHg5Da5sX-kFyZFlBI8iHvdjpn0EsXKoBTwoWAj7mYSxPGsqyQ_Gm32666FyIVHIHxjhgiyQLxI4pBYbhWhhAii0AsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FfJ9w6064ve4kbk2dXQ9eeGkfzkRcFufB2dUrA_gfkx5aOlTR0iX2vKY-4D4SFRZXEIFvIvr1ln9HVH7zJ3uj_xjbffNMbGObIdCL3OD7w1K3-G518q7PtRdag5ulMD0GsFro_ius3hXn-qqJZ_ZoGiciHcO1j1KLOZwNcMA3In7k5PgkpOaCx7CslHgMf7JMiRe2G6MtA_NTOPEKOd3i099JnS-6K1GR7hOuIRq02Vi_xESB_nTndLu78hHYnhjIdB_gJkfgybFKOCGMan8TwDH7GdfZZDE3j9s4RrnynDIg0es6-AmkL_bgiGMl0YiFVBd4MsGnfhBgvB39x-U9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cnrIC1HHSTMEwYs-HD7tCXZ_WBXrc0DpJyEdCur5KrVwmLrNHi03bX3L6FwxFVtBymdcxk5U5X83ihPbPyWykyy6SsfkxgKJHzPqyVSE3xkNoy8HDI0tS9WDux6wqmHKZ24TIAcJisZMg6U4yvP-q3whqoNAVWt8PGK7HD7j4kJL_I-2N1KML-nUq1sxyshT4b2p1SMpi_b_5Qi43qfuGh6L50gE0G8WiDLHU1OFODSP1_qavbDDW_ZRxtenAFfiSYDfYk6HCQl5qrIOILhwJ4yFSQy4cG0AiUZqG2S1HlqXfRxrTptVeqeeRkgeMzWYr0AR5xmlY273jHAUIoI3MA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی
خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید:
https://app.mpay.cards?startapp=ref_PzwXZ8
(لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید)
1- بعد از اینکه وارد وبسایت شدید، Next بزنید تا با تصویر  اول رو به رو بشید
2- روی Apply بزنید
3- با ایمیلتون لاگین کنید. دقت کنید که تمام هویت کارت‌های اعتباری شما روی این ایمیل هستش
4- بعد از اینکه وارد شدید، با کریپتو 5 دلار پرداخت می‌کنید و کارت برای شما فعال میشه. از USDC و تتر و... هم پشتیبانی می‌کنه. برای آموزش پرداختش با نوبیتکس و...، می‌تونید یوتوب رو بگردید. من خودم با Trust Wallet زدم USDC و مشکلی نبود.
5- تبریک می‌گم، شما Visa card دارید به اسم خودتون!
مزایا:
- می‌تونید توی تمام سایت‌هایی که نیاز به کارت دارن و رایگان، اعتبار خوبی میدن، ثبت نام کنید(من توی Nous Research پلن free رو فعال کردم)
- می‌تونید برای OpenCode و سرویس‌های بین‌المللی، با شارژ کردنش پرداخت داشته باشید(کلاد رو هنوز امتحان نکردم)
- و تمام چیزهایی که سالها از ما گرفته شده و ازش محروم بودیم.
- ایرانیکارت و سایت‌های مشابه، با مبلغ‌های فضایی و میلیونی فعال می‌کنن همین رو. و به نظرم 5 دلار، منصفانه‌ست
معایب:
- برای واریز به حساب، باید اول 25 دلار شارژ کنید اکانت رو و بعدش می‌تونید به کارت منتقل کنید. تنها محدودیتی که بهش خوردم همین بود
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4915" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LpOI1kEJx71AMQEBY7SCQFhCMnVOkGQJKwSoR_PSx9GLCKTN8EpiyM6Ms-aXLGsWDc-oIhC8zUfcnI8lxhTJFoUe_P27njy3hutrZjOmbbe2fJQGRs3Z9HNXvB6cO-xq3IznE2mriOg6UnLQ0YwEfflaIM-4Gqu0vp_hL_tYhLwOc0yYkPLiXI5R1OizlsvsZ8q1cRbC6uSHLpqveCiovVFwTQoi5e12fzVzB5raPvRqkCc44VN9TL4XSRFZ4gi0G26Z_r7tm4fcHSZCWjHzqcYIx5sTV8u6A7L2UW2CbBizWCPl5y2LHpPy2GUWlyNLYbi3vNPu89A-hCvtGv9OXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.  از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4914" target="_blank">📅 19:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">همینطور روش رفع تحریم آنتی گرویتی هم چون یه کار کرک ماننده، باید همینجا آموزش بدم و اصلا نمیشه یوتوب گذاشت:) چنل سر دو دقیقه استرایک میگیره</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4913" target="_blank">📅 19:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.
از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم به صورت متنی</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/4912" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این دسته‌بندی جدید کاناله، با ادیتور جدید عزیزمون محمد.
پلی‌لیستِ "قصه‌های مدرن"
قراره چیزای باحالی با همدیگه بخونیم و یاد بگیریم
🤝</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4911" target="_blank">📅 18:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kgl0rDwbo-ZvisqM7dkYbg0NAx4oO6QwZQPNrS6Q3fkcibu1K1OrvFoescOMMzJqTguDjwcFM3x0vUgBcUDmi1HhK0GlnVFzdv46Lj98qOstFhBjmUT0dNsHbSX3MKgjb6zPsfA2PSJd8QbKleY6pb3S9u5IkCnCQVHMJ2elS8ccmYu5LVqu_MBbKZvL6KrtwFYpTLbL1XhhGeBKy69gZqlxyTdMH4hpoFdhaMe6djqmxsXwsOCnRWDTmTjOXK-_5xrFAxU6yKrZ6MrbG5e5Zp4YR2dZ2GHt17KpxaFV3CnCaO3jGGXN3KWRt6RXVQWMZI5z54ompeIfHw61q1fTdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
قصه بارکد، خطوط سیاه و سفیدی که دنیا رو عوض کردن
هر بار که کانفیگ V2ray اسکن می‌کنید یا یه چیزی می‌خرید، دارید یکی از هوشمندانه‌ترین اختراعات قرن بیستم رو استفاده می‌کنید. اما داستان اختراع بارکد اصلاً شبیه چیزی نیست که فکرش رو می‌کنید؛ نه آزمایشگاهی، نه تیم مهندسی‌ای، فقط یه دانشجوی بی‌قرار و چندتا خط روی شن‌های ساحل!
توی این ویدئو با هم می‌ریم سراغ:
➖
اینکه بارکد اولش دایره‌ای بود
😂
و اینکه چرا تا دهه ۷۰ روی زمین موند؟
➖
لحظه‌ی اسکن شدن اولین بارکد دنیا روی یه بسته آدامس
➖
بارکد دقیقاً چطور اطلاعات رو مخفی می‌کنه
➖
چرا و چطور QR کد به‌عنوان نسخه‌ی پیشرفته‌تر بارکد متولد شد
📹
تماشا در یوتوب:
https://youtu.be/PAHA55mHLWs</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4910" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">و اینکه مدل رایگان Hy3 خیلی از Nemotron3 ultra قوی‌تره. از اون استفاده کنید</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4909" target="_blank">📅 14:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XHNaMLv00AZk_72c-kPJR9Pew-Ek9bqAohnDwCqdD88g1Uz8TaafpEQXG_IunrjAjye7WEB7s07glJCtQUjKWkhKyp1YwQHhk_z_LHtwaVOwGPy4BADSlmZ_fF46c60B2823cSM1w7PkIvXsjoiYIA4f0Txr9oBMZpEIHSyLi1UE2Dy8UK29RdiQae2tlas7lHtmClWyqKqsL-UZB5u_73iOzvYGniCREynPsiWzJjI9RP5Cf9e1gd2MT7WQ_QXcoDu8X4gWqiV5k2scnL-qY_dyzZGi6otISBrvbpeyLFSwA5tDiYMR12ypqpPJqavGcMFTSJNvaByhO_zL6mmj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا به آیپی‌های کلودفلر حساس شده کانفیگ‌های کلودفلر رو با آیپی‌های دیگه chain proxy کنید باید درست بشه</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4908" target="_blank">📅 14:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده و فقط روی خود OpenCode در دسترسه واسه‌ی خودم احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4907" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده
و فقط روی خود OpenCode در دسترسه واسه‌ی خودم
احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4906" target="_blank">📅 23:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حالا که شماره مجازی و کارت گرفتیم، هرچی سایت api رایگان میده باید شماره چینی تایید کنی و پیامک بیاد برات
😑</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4905" target="_blank">📅 22:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4904" target="_blank">📅 20:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RGDb27AVooVVjB0EVY5Z23xacEacb68xYr6rNmArO7hg9BZ4PV7q4S1RCttb9rtXB4QiefvhBY8qQ8B5quYUtUsy3iu7kxAWuLiUtqPz6LWLEns4Fxd0AJWMoihbpKH21iui4BcTJAjl3MGi366u83ZaR0nxaoyXskCEwfYTCJpZO1GK2aQmT83HmOU0I82rDpwKngmtzCz0TG4rqVfOLVK7n_zlflCpx8o8ht7LGVzJqRqYVY1bZpTRbPPLu64K9_JzRnIwFGJgJS8_lpdLwuEMmrwjtNY2SD-xJ4IbMAQM48V90xxW_PBza5-rIqQY-MvwiQ8w8MIDOTSczMJpkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4903" target="_blank">📅 20:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یه مقاله از 404media نشون میده یه شرکت پزشکی که ادعا می‌کرد تحقیقات و peer review‌شون 100% توسط انسان نوشته شده و ابدا AI نیست، در واقع کلا از AI استفاده کرده. طنز تلخ روزگار ما
😂
https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4902" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CBVTyOwLjDzLp96LMFYwIKn_TxzedJWaG27Gu-FPa_qbYB0jYRvjk8yAxIxF3SiUhQgjzkHyuRUaCYmVAr60PWtrt8TnCyFv0XxvndoXjW2gKFUkcbkRW0fZAJOtE5IlW7rPoTl-JqOn0xuJCaGdQBNkH2rFcm0izMKEhCVgMCPl4wMCkc_VkMiPM6zytCsuZySzf6whaKiVz-f7d-e1YCxL7fKz41NOxNYxzAKSoibc-my_GzvODkEnHMS1ciaPhBzzHrDpzx_XCN3tN5fzuOSLLlNxG9UbNHIrKWUCZPQqPwgo6GWAR6sXcRPCKp1PPTqRpPj5No-9KnSnLpigWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اینا تروله دیگه ایشالا؟</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/4901" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گویا ChatGPT قراره تبلیغات داشته باشه داخلش
😂
تا بتونه دسترسی رایگان همه رو حفظ کنه:
https://openai.com/index/testing-ads-in-chatgpt
اتفاقا به نظرم خبر خوبیه. کمپانیا می‌خوان ضرردهیشونو جبران کنن و طبیعتا بهتر از گرون شدن اشتراک یا محدود شدن دسترسیه
اتفاقا با این روش، شاید بتونن مانوردهی بیشتری روی دسترسی رایگان به مدل‌های جدید داشته باشن(مثل رایگان شدن GPT Luna)</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4900" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">از این به بعد، همراه هر شمع لیرا یک تگ بذر هم براتون می‌فرستیم؛ تگی که با کمی رسیدگی می‌تونه به یک گیاه زنده تبدیل بشه
💚</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4899" target="_blank">📅 17:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLF6UO-gUas6WrcHRZJ9q6uAHaYJA_1-NgwHkaMeSQQXT-NZgtdUM_8n3cGz9MTxXY23YsY7xTa0GlXhF89J8oLDp8VVNv0VhrvwTPky48tD3o7jHvekyPPVIkA8fR9-QI3Eoe0JvKPbMIayE5RvxdxTkkg4riz2lx0xSLt9ENX_fN7BEUrx5KB97R5UhuLzUiUb2hJWTKFCGhwGwVyqSLVC0aEmdTbdFPBFlk7Et3AeoLPjkirxoaJw2lVknRQMQzCjBefxj3Lx1bh5uhSRqSwKf2VMwKCZozZ-uCAqOV6Vae9yojz-mkeCRd5r6DpTWbVWzl7Sc50eB5eeB8_gzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون حرکتی که برای کلاد زده بودم رو برای آنتی‌گرویتی گوگل هم زدم
از لینک زیر می‌تونید استفاده کنید ازش
[راست چین شده و استفاده از فونت وزیرمتن به یاد صابر راستی کردار
🕊️
🤍
]
https://m4tinbeigi-official.github.io/Antigravity-RTL/</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/4898" target="_blank">📅 13:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4897" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا
جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/4896" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4895" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">Building_Applications_with_AI_Agents_Designing_and_Michael_Albada.pdf</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4894" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شاید بپرسید پس چه کاری؟
حالا برنامه‌نویسی آره یا نه؟
باید بگم که نمی‌دونم حقیقتا. تخصصش رو ندارم واقعا که بتونم تحلیل کنم
و به نظرم باید ببینیم AI به کجا میرسه
اما یادگیری رو متوقف نکنید حداقل. به قول جادی، یه چیزی یاد بگیرید(هرچند جادی میگه ai، استخدام برنامه‌نویس‌های تازه کار رو replace نمیکنه که به شدت مخالفم در حال حاضر. به نظرم تا حد زیادی نیروی برنامه‌نویسی کم شده و فقط متخصص‌ها یا کسایی که واقعا علاقه دارن یا ایده‌های طلایی داشتن باقی موندن. حیطه‌ی برنامه‌نویسی هم مهمه)
اما خب حواستون به حرف‌های غیرمنطقی و امیدهای واهی هم باشه.
و سعی کنید خودتون تصمیم بگیرید. و توصیه می‌کنم حتما علاوه بر مهارت‌های نرم‌افزاری و پشت سیستمی، یکی دوتا مهارت فیزیکی بیرون از خونه هم یاد بگیرید
❤️
نه تنها وضعیت دنیا معلوم نیست، بلکه وضعیت ایران صد پله بدتر معلوم نیست</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4892" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NvJ-OYnafw6Cz27r9-8I9_lnWDOyrStwTiIshXqQrqGZsU70qu3SpuJErqfH4UXciWwLBH0dZUD0jvw_-XU6uQFDMyY5-gLNHaDCBtZhQ-OBJscsAuAR-oUPRvl1orq1-zgp0G0VDSpvg-xw2MCj8mfmN6rXPQ6WinKYU0igcV2ppWTDkCUhto0Ncs-6fb5qiNgQKR5Xltegcs-S7pz1X8AUeVb53eGMbh--PuauvCZ602ReWMekwiG3A6dBdj-m83Fu0SYeOMLf45J-n8c2YcVZZUNIiDBwaV_wPLZdm5BIM3wwZ2iOlg7zAWWmjbTKs9LT4dS2ngR_AxQiANvakg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">21 سال تجربه توی گرافیک دیزاین، UI/UX و Product Design دارم، الان هم که چند سالیه با AI سر و کله می‌زنم.
از زیر پله تا شرکت‌های اروپایی و امریکایی رزومه دارم.
سن‌ام هم دور از این 35 نیست.
بدترین زمان برای ورود به UI/UX عه، قبل AI شانس زیادی نداشتید، الان که اصلا شانسی ندارید!
✍️
Diego JR</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4891" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o5ViJVFUpITJYJ_dfK9dFMh7Q3LL2gr1G4hlLzahizoWJDscFKzOiX3k2eZIgL0etzP7gaGnMhyVYaZ_vEa-WyDeJBpyfUAghiX0yUpbEeadkIWWoV5kyeToyFDgGUAJUniWnf3p2r1FN-4ve8IQuK14stfsJwp0_EP8E8pxHHIyfFUKokI7IO_0ASafXXjSL66SilVR_9YsDOg9t4PPDVVII4q7R1DFgTpc5Fc2P0prck3j13D0pMiwtmUiFvaxrzHPZqwyffWFiy32SD6ho5VxMvs2sHDGoquZyQyo3DOzpCf6q7JcZvSiDE1EuEl4b2brevYxCN7arJ_f523rqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نشستم با Hermes و WinDirStats سیستم رو یه کم پاکسازی کردم</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4890" target="_blank">📅 20:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کاملا موافقم و به نظرم هیچکسی "عقب" نیست
با کلا یکی دو هفته می‌تونید به ایجنت‌های جدید و api هایی که هست و... مسلط بشید اصلا نیاز به تلاش خاصی نداره</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4889" target="_blank">📅 17:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">به نظر من کسایی که هنوز نرفتن سمت هوش مصنوعی آنچنان ضرری نکردن، چون الان استاندارد خاصی نداریم هر شرکتی چهار تا Agent برای خودش راه انداخته و داره باهاش پروژه هاشو جلو می‌بره ابزار های هوش مصنوعی یه دو سه سال دیگه پخته می‌شن و شرکتا یه همگرایی به سمت یه استانداردی می‌کنن اون موقع دیگه یادگیری هوش مصنوعی اجباری می‌شه، ولی اگه هنوزم کسی نرفته باشه سمتش با یکی دو هفته شایدم کمتر بتونه تمام ابزار های ترند (نه استاندارد چون چیزی هنوز استاندارد نشده) رو یاد بگیره
عجیبی ماجرا اینجاست یهویی یه ابزاری چیزی میاد توی یه ماه 50 هزار تا ستاره گیتهاب می‌گیره بعدش فراموش می‌شه و یه چیز جدید تر می‌اد!
@Linuxor</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4888" target="_blank">📅 17:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نمی‌دونم واقعا یه سریا، کی می‌خوان بزرگ بشن
کی می‌خوان به بلوغ برسن</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4887" target="_blank">📅 16:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4886">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">«الو بابا این پسره منو اذیت کرد بگو سایتشو بزنن فیلتر کنن.»
خیلی سایتای فیلم و سریال و انیمه و... همینه وضعیتشون.
تازه من دورادور در ارتباط بودم در جریان یه بخش کوچیکیش هستم فقط</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4886" target="_blank">📅 16:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4885">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">با ابلاغ مصوبه جدید هیئت دولت، مسدودسازی و اعمال محدودیت برای پلتفرم‌های آنلاین از سوی دستگاه‌های اجرایی ممنوع شد. از این پس، تعلیق فعالیت سکوهای مجازی تنها با تأیید رئیس‌جمهور امکان‌پذیر است و مسئولانی که خارج از این چارچوب عمل کنند، ملزم به جبران خسارت‌های مالی وارده خواهند بود.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4885" target="_blank">📅 16:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qWk8WPsmFO4x-fJ7OxLhrI9yHLRNu573lPPWITZ0fQSGl3Zki18S8l6DfbjaWRApdVlgXQ7VFc8iDwuOiic5XcjSLG3eDhZCYHBZCRhC0EFb90kYWQCC1_qLwaCOAeJdhbYSkdtUSdn0D6CZizj9WZ8kHmIpfbWpPt45UPWMA5-TP74H9lHZZAdgvcRu8k9Y9m89f6HN9anHCVUC65FLmVUXEURJPaammKFlaeBjzL5a8hykN2_eYjm8NUS6Qy55kconDyEsMyyYo5fqURu13QwL1VppEF_cAyLmlui4L5GmdLeVm4V3ILS-6cJqffJ6T0GEYV7NYWz8Ly-ZIY9odA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Free Movie هم بامزست. دو نفر می‌تونن با همدیگه، رایگان فیلم و سریال ببینن
https://freemovieir.github.io
هر فیلم و سریالی بخواید، لینک مستقیم دانلودش رو می‌زنید اینجا  و Room میسازید و می‌بینید.
در واقع استریم نمیشه. Time Code کنترل میشه و چیز باحالیه</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4884" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان، یه توضیح مهم درباره پروژه X4G که توی ویدیوی بالا معرفی کردیم:
بعد از انتشار ویدیو متوجه شدیم که به نظر می‌رسه بخش قابل توجهی از پروژه X4G از پروژه RVG گرفته شده، بدون اینکه اعتبار مناسبی به سازنده اصلی داده شده باشه.
🔗
پروژه اصلی
(لطفا برای حمایت استار بدید)
https://github.com/arvin341az-glitch/RVG
✍️
برای اینکه از سمت WhiteDNS حق و اعتبار سازنده اصلی تا جای ممکن رعایت بشه، این کارها رو انجام می‌دیم:
- اسم RVG رو به عنوان ویدیو اضافه می‌کنیم.
- توضیح مربوط به این موضوع رو در کامنت‌های ویدیو پین می‌کنیم.
- لینک گیت‌هاب داخل توضیحات ویدیو رو به ریپوی اصلی RVG تغییر می‌دیم.
این جور اتفاق‌ها متأسفانه توی دنیای Open Source پیش میاد. ما قبل از ساخت ویدیو با هیچ‌کدوم از توسعه‌دهنده‌های این پروژه‌ها در ارتباط نبودیم و طبیعتاً تشخیص اینکه یک پروژه از پروژه دیگه کپی شده، همیشه از قبل ممکن نیست.
ممنون از دوستانی که این موضوع رو به ما اطلاع دادن.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4883" target="_blank">📅 15:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=ak9ZjEGFZuj00t5oW3wWjzzdl-ohByRvHzVxafNHfvd9Jjx-Lmhi2-Rc9hdUhuCbJXXpsDIWpcKe0akuvFAWTpjjalC6N9Cp7dcGjFCIGf4I5P1iW1Yz1tcDvMxmtIE0QpCGJsbM8x_HJ1cfeGfEOilSREIE0mNFNobW_nAQG8oODrd8eVxon8bgflIE4CideWZwErUoejvVoeM2xNycmmQhemb81MaesY43pyYtq2tTl8_MTITqW9ywtfnRcaNaULZH_NlwQhseKNxvtiHKZLvENwuTuiEYdV27PZ0Q0KDoo27EMtTEWK-aezSVO16Bmz97iJVv4UQjx5_1t74uGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=ak9ZjEGFZuj00t5oW3wWjzzdl-ohByRvHzVxafNHfvd9Jjx-Lmhi2-Rc9hdUhuCbJXXpsDIWpcKe0akuvFAWTpjjalC6N9Cp7dcGjFCIGf4I5P1iW1Yz1tcDvMxmtIE0QpCGJsbM8x_HJ1cfeGfEOilSREIE0mNFNobW_nAQG8oODrd8eVxon8bgflIE4CideWZwErUoejvVoeM2xNycmmQhemb81MaesY43pyYtq2tTl8_MTITqW9ywtfnRcaNaULZH_NlwQhseKNxvtiHKZLvENwuTuiEYdV27PZ0Q0KDoo27EMtTEWK-aezSVO16Bmz97iJVv4UQjx5_1t74uGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/4882" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست قابلیت های هر پیام رسانی رو داره:  - چت های شخصی و ایجاد گروه ها - تنظیمات پیشرفته پنل کاربری - پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ  نصبش ساده ست و با یک کامند انجام…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4881" target="_blank">📅 13:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZethRise</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p4u05SG5uGOb8vweVolj3MiIpbTZJ0zTvZR4FWl3LEYIZPVAS56EuwWXyksCQKZekf6XnDAwoGoS60U3rO0scLVRV85DF0N14VgAVJg-3FW2AfCAPcJaw6mJSh3UtjkgjveB5QZdw6yY_ngYyclSMA-vV-f_G-5vMsT9dQzFU7gKoIofUQlOVqieTvd-InWde24tztTsYKm9R8YOZLDGm5ynfMwDIH9u4SykebRhBNJOVhmmgnUugG8kInAKgD0aDh-F-rzf2CzaQD1KrHjKtnhqVbaodzccOW0jbQOY3U-GehgPqiTDfspuvQBnjhgzAWsx2uiHmEoNyYYrrv4FvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست
قابلیت های هر پیام رسانی رو داره:
- چت های شخصی و ایجاد گروه ها
- تنظیمات پیشرفته پنل کاربری
- پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ
نصبش ساده ست و با یک کامند انجام میشه:
curl -sL https://git.diastom.xyz/ZethRise/FelFelChat/-/raw/master/install.sh | bash
و سپس با کامند
felfel
در ترمینال سرور میتونید اون رو مدیریت کنید!
درحال حاضر فلفل چت ممکنه مشکلاتی در UI داشته باشه و همچنین در backend چون نسخه اولشه (v1.0) پس اگر به مشکلی برخوردید توی ریپازیتوری issue باز کنید!
👩‍💻
Git Self-Hosted Repo
📱
X Profile
🚀
Developed By
Zeth</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4880" target="_blank">📅 13:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دو تا از دوستای خوبم امروز همراهم اومدن و اذیتشون کردم و کلی تجهیزات گرفتیم
🥰
🥰
به زودی خبرهای خوبی در راهه</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4879" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۴
🔧
رفع اشکال آیکون نوار وظیفه (taskbar)
در نسخه‌های اخیر، منوی راست‌کلیک روی آیکون کار نمی‌کرد و امکان بستن برنامه از آنجا وجود نداشت — تنها راه، Task Manager بود.
مشکل از حلقه‌ای بود که پیام‌های آیکون را می‌خواند و روی رشتهٔ (thread) اشتباهی اجرا می‌شد.
اگر نسخهٔ ۱.۰.۱۲ یا ۱.۰.۱۳ را نصب کرده‌اید، این به‌روزرسانی را حتما داشته باشید
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.14
@whitedns</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-text">📚
آموزش اسکن Resolver و استفاده در WhiteDNS (cottendns)
اگه دنبال یه Resolver مناسب و پایدار برای راه‌اندازی WhiteDNS هستی، توی این آموزش قدم‌به‌قدم نحوه اسکن و پیدا کردن IPهای مناسب با Clean IP Finder و استفاده از اون‌ها در CottonDNS رو توضیح دادیم.
⚡️
🔍
کاربردها:
• اسکن و پیدا کردن ریزالور های مناسب
• بررسی پایداری و سرعت Resolverها
• استفاده در WhiteDNS
• بهبود کیفیت و پایداری اتصال
📥
دانلود ابزارها:
🔹
Clean IP Finder v1.3.6
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.6
🔹
WhiteDNS v1.6.0
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚡️
ابزارها رو دانلود کن و طبق آموزش پیش برو.
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
امروز اومدیم با یک
#آموزش
کوتاه از کلاینت/اپلیکیشن incy
🔥
داخل ویدیو به چه چیز هایی اشاره شده؟
. ایمپورت کردن کانفیگ ها
. وصل شدن اتوماتیک
. تغییر dns داخل اپلیکیشن
. تنظیمات مربوط به تست پینگ(مشکل پینگ فیک کانفیگ ها رو رفع میکنه)
. وصل شدن به پروکسی لوکال(باگ کانکتینگ تلگرام رفع میشه با این روش)
🔛
خلاصه:در قسمت dns از quad9 مقدار گفته شده استفاده کنید،تایم اوت کانفیگ رو بالای ۶ ثانیه بزارید در صورت باگ تلگرام از قسمت پروکسی استفاده کنید.
دانلود اپلیکیشن اندروید
دانلود اپلیکیشن ios
دانلود اپلیکیشن ویندوز
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4876" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P8IOoWGa23SF27oDxHicTXYZlFbPm2KyQJP0JpuUA_37-OjKzevrBpQfGI104WtQQFLl8bReQwnrVO0j164Z3PMFIhseRM9LofyRifHKSUcsD2LDPJvuldK4pcBKk7Dfpf57aVSpTwHtFeiRo3E9R5RsNzjCyalipXSfe8Y-KZ0RovzuoMQcQa9mnjAj58-Aj3HNXCfDzUD0M_n_RYtUer2fURmJY5NzG2T60m_qCLKrY8sx8-yq9PHaK_xjQ6nsR_rF42YiZQPeHvKeUpKSSubQpiKvOjokaKMVCtlFIL3wq-WYLq-95dJmD3PFI76ICxz1R__HE5M2bIHgODpHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز دوم و هوشمند برای ایجنت‌های هوش مصنوعی؛ پروژه‌ی متن‌باز Synapse
🧠
حتماً دیدید هوش مصنوعی‌ها بعد از یه مدت حرفاتون رو فراموش می‌کنن یا اطلاعات قدیمی و جدید رو با هم قاطی می‌کنن. پروژه متن‌باز سیناپس، مثل یه سیستم‌عامل حافظه‌ی طولانی‌مدت عمل می‌کنه که روی دیتابیس محلی SQLite سیستم خودتون بالا میاد. این ابزار فکت‌های مکالمات شما رو استخراج می‌کنه و فکت‌های متغیر (مثل شغل یا محل زندگی) رو به شناسه‌های مشخص وصل می‌کنه تا با تغییر اون‌ها، مقادیر جدید بدون قاطی کردن جایگزین قبلی‌ها بشن. سیناپس اطلاعات قدیمی رو کمرنگ می‌کنه، تداخل‌ها رو رفع می‌کنه و به صورت خودکار مانع ذخیره پسوردها و توکن‌ها می‌شه
👍
این پروژه به صورت سرور MCP ارائه شده؛ یعنی می‌تونید اون رو مستقیم به ابزارهایی مثل Claude Code، ادیتور Zed یا Cursor وصل کنید تا یه حافظه واقعی و تحت کنترل خودتون داشته باشید. سیستم بازیابی حافظه‌ی ساینپس ترکیبی از سرچ معنایی، متنی و فاکتورهای زمانیه که همراه با هر حافظه، یه شاخص میزان اعتماد (Trust Qualifier) هم به ایجنت می‌ده تا بدونه اون فکت چقدر معتبره.
که به نظرم یکی از مهمترین قابلیت‌هاش هست.
با سیناپس، ایجنت هوش مصنوعی شما به مرور زمان با بازخوردهاتون هوشمندتر می‌شه و تمام داده‌ها هم کاملاً آفلاین دست خودتون باقی می‌مونه
✌️
🔗
لینک ریپوزیتوری پروژه:
https://github.com/Danialsamadi/synapse
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4875" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8wgwOd_nyeVCpDdqhX5gTHv_CitJqDOUxwRbz4tUSJGq2iTwqZTVNBI9phpYAfF5PdqFundLB-oxTlJaLDYNa9c5cziQ7fSRM6xXVqVL1dLQRj3COGR4HvDJlm0sKR5K8ig3t_ERMRma2jfCGnThzy3xOQ6R4ReOdPm6o5fiotyXmsyKKJr1rUzpGy3rPOKegUSE0omEB93qR3pcDwLmcQVm5lC9WSqKdOMVfE8q7GpZb4Iq_g8UknE0N7HuXtXHLuXuo91aHpYQGgpQisgWLGJzBIckANXWvmkRKQWUocxMWCKZtSI1DqsCs9b79RhoxVHQn-17mLP0gQrSFTPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OotvdxcIRz3A_pIKri3GYHssX5de7s4EezFxatvkUwNaqgbNxx15Ej9FndnUxlZjlwcQF_wTqL4Ht6uKKl0eS6U0AvgKDx00ea20XI-pQy5vrYc-c_j1bK6QefVSBp_V2shb0FV8gEvMKXurnZH8GmorqpfU1TOXa0EXz0QizBqZwtajxJvPUNgGa876Vq-7gCN5Pyjms3FtutiToVF8uo3hvzoLNpkbruNLWlLd_IynoOwWf6L1ap9Hr9VTvequ_yIFzwN9oh_37b4RodrK-cyWzXZv-7k6TNrV6-y2wXcj21nUDcMvSzMurbPJwblOmTrTbUWHGEosuu0V1ctNkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mJPBhaxZ4aoe3wH6Q1ANH_QfwDIBzvbqojyQOXg6PKZ-NKe59wryNkgP7_047K083E51bFUvZ8EKoxTfXxgKjV7paBXXY-rsEW_NjhEptdcMgKGf6zywq98ID6Bh0gyTURHNseLyOLlfWXuewJJ8n0ayieOl2G1uXBaYxqe4uLTDLoaMrHEkScHzIg2c9Ty4a2DZ7mRNsuiHoTUdz8cRB0pgZcLM4WcKr4H6itHKz88HadvhyEg2sFiAqP-wqoYWCib4g7s5SVaZ61aZKc6fNmSNfOt1o6gE13_hWpNvoZYxR35zX3MZ_xL9yxi2uYS4l14GwK7LNlQlyfxnV8eZ-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دسترسی رایگان 14 روزه به تمام مدل های zed code
ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده!
​مراحل دریافت: وارد سایت بشید تیک Free trial پلن پرو رو بزنید
zed.dev/pricing
با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
✍️
CypherDeveloper</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bfjXvxs_85pCA9caL2v-e6spJP8MJbAzTvIrB3yOV3QCdonty8k35WglXYtRsHDPffMpHsyyQXp-IblaxxnCoEcpWLo6sS6YohjkXEdrnx185pi34GIl6YYepvQPorpZZ3iXRiUIfOas8dJ7Zd6fzzrFcy-KKurYgn5DfQVT7bkZeuenU-noOLJ9PGlSuKxkC4_6g8NnjX3FYAlwkvSi71I9ybT0avGDfvUEIPZ8u3dMm_MGpNr9LTBmU8Pi1LOd8V4dwP3VGjzK8eC92UrijxVcjDkSfBiRq4dayoXGka2qEbKG3aLQGFRGL1iZAtaVqMHexKRz5mJCeeMiVyRe0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=Slw8JVxD65oJQW2jalEmARtRUi4n3S4ylORIMHhrooRktez3_Co6usuvgoQljy230PdNjYuJWUIqraCpLSWnSVE0TNS3DrCKCV38FJkssvgswYAA2--juDUKdmEXWYddc7pl0sxPR5XeNI4091KJq_lqnClfI3yrmyxZKzN14EDAv7X5ducC3kEIl4yr9c9YVw6OeAPROasKIhXourLwqxqVohCQY9S7Kvx1zGShDu0w99uUeUe2UkgcJ0i1vT4zWL9OANBHZupyqjJaRR_0UafMVyBt0GEfeqi-lIOle8KT3M_POPVPzpE090-lXUll0BkIprdobLDRlbkLt4kTDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=Slw8JVxD65oJQW2jalEmARtRUi4n3S4ylORIMHhrooRktez3_Co6usuvgoQljy230PdNjYuJWUIqraCpLSWnSVE0TNS3DrCKCV38FJkssvgswYAA2--juDUKdmEXWYddc7pl0sxPR5XeNI4091KJq_lqnClfI3yrmyxZKzN14EDAv7X5ducC3kEIl4yr9c9YVw6OeAPROasKIhXourLwqxqVohCQY9S7Kvx1zGShDu0w99uUeUe2UkgcJ0i1vT4zWL9OANBHZupyqjJaRR_0UafMVyBt0GEfeqi-lIOle8KT3M_POPVPzpE090-lXUll0BkIprdobLDRlbkLt4kTDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=djUg1GvtQPNLqmaTPk_8A-cPMd6AKjvmdmPN2usSxqvO-wu4NGo59iu1AkUCG7nXa5dpzPaBV6gG2gAiVubhb0tjbAZgK-UUytysI8W6qrby5LdU7Pn1WKoJGjhD98ojb1Avay47kXJ9pXzC0IDG0uBv4L3kcKoIO1tsbST0yVHqhrf1f4SfjIjkUjrORZx_P3oL4kZ87I437lsEm-WchgBFPUWBMV6Q59OliWyuCzGHxPQrjMLbIBvGwfP5VZm-wL3Biyv6uz1O4VmbRXPbz9UkrljPhbFPlfeKi17kg0YNZfc7tmtyHfHmgG2-nAbfANJfd9wZK4Y2YmL7BFjDBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=djUg1GvtQPNLqmaTPk_8A-cPMd6AKjvmdmPN2usSxqvO-wu4NGo59iu1AkUCG7nXa5dpzPaBV6gG2gAiVubhb0tjbAZgK-UUytysI8W6qrby5LdU7Pn1WKoJGjhD98ojb1Avay47kXJ9pXzC0IDG0uBv4L3kcKoIO1tsbST0yVHqhrf1f4SfjIjkUjrORZx_P3oL4kZ87I437lsEm-WchgBFPUWBMV6Q59OliWyuCzGHxPQrjMLbIBvGwfP5VZm-wL3Biyv6uz1O4VmbRXPbz9UkrljPhbFPlfeKi17kg0YNZfc7tmtyHfHmgG2-nAbfANJfd9wZK4Y2YmL7BFjDBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XxP_QWe8qO0a-dIuo-dWnJ-VrHh92KOcp4ANs1a2CIdyapl1mzunVcKmldO37u8ukDbXKpaFGy9rYiomHTPJYOlEFzyHqYN6LqLfAPUMEj8nN07BkZrREjkMW_oAi_A3A2E6eAiliVbPilghnHAV3wBwvPXl5fX1CP_29CCcE3boZqFNg2j6nvB0HeRAB7nJOZbv7jKqyIr7H-OxbMdhtfY7PsPWu-qrV1i7TYEfQVPZYA0ntDYFZx10bkTxrtbISdpgEFqPrO_GbH4ksGdvL_smRAQXzvQcUzR2SvdM5RI4MhS6Pjg6T_7m0eg09UrUiZ04YpVDGXk5eqiHxyBqEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vPaXOz01hM2ORAP59rqxUSycFt78cVPk-ByRc52ddX3R4RG8vRH29q2qaR7IuahjCBZBxesWufihzm-98-LbKps2ODfPx8Lp9aVxCCtqLH9mtWYiN85OwQss9btKQc8lV07E2Ruf331_XafcF_DGufRIyzUcpLgorZvyJf4scZh4GdGmqfL4s3_FNyLihY_rhvFiHl4Ftec_WDSNcDkVkkQLVCcUXg_W-bh4rCkiE6FByYk2TMwUAH8Ff8r0g18gsWf0HvEtxpeSGb1iUqnMyhXltlNDPQSZTThW9WYsq0_bvypRGcbtxkc9sowaf8aONLCtvFpShwdPQTFltol8dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/heMUAZb0hJTTB-xgNJow7n_I6B9xrr0UfLyGefIKVyFWwfAuks9NY7l2hvSQjfEIazpOpeeF2ltPUWBgX_glwlVn0c88vRjrs9seyI9w2JsIqFDpg1E2fW7iKCdDFT_yqGfh9tIE7ReouSlnqp1vxccIJDykEOvUXNnRic0-fGJ9QCW0m7pf57q7U8gwOGXIeWOVuOuMJNguFaU1T6k8e1aNGqHMynLTAeeAZnFczj1CZDvElVwOiWG_VfGD_3iw1723Sur5yJA-B_5msifekMdAbma6lJGipqpj4-I7H9Aaag9jJGluAGrMTs-2vYX6D5LZ5bgFzWIA8lWqqW10Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MWvM4Bk2GvilY7GsGHD6Z4o-MjPXV-PrrZttAGTrwj6e1iJJPLxWNQYXA7Kgf4kzNqsgj-OqK7ACncyQgN82Ax-Z1ZZEnDaNwsRd8UE2gKOU4CwUnsTQ3hJgPqUc_PfX9_dC55v-QZOpKM0x9MpkkKIPuiTtP8sOUmdiumgRbjGKYPvAqEoq5YW6j4qys8mdlJqZDh15vfKDc2pcojWYZGRHHp-MbNg6MgXRpAUe9TyrgX0LX62qSA0agZhXLNNIr5NTKqdNf4tQJpuH_ukHH6A6EjEsu4ZVufX1JTUkRR6DKn8aj5cHNya1KS85c5VQzXN1DDT1_u-BLFLYezjuVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ Hermes، ایجنتِ دوست‌داشتنی ما، نسخه v0.20.0 منتشر شد!
📊
این نسخه که بهش "The Herald Release" می‌گن، کلی قابلیت باحال مثل ارتباط صوتی زنده، سرچ با منبع معتبر، وب‌هووک، اتصال ایجنت به ایجنت و بهبودهای شدید پرفورمنسی داره
🩰
تغییرات و ویژگی‌های اصلی این آپدیت:
1- گفتگوی صوتی زنده (Talk to Hermes): پشتیبانی از استریم صوتی زنده با قابلیت قطع کردن حرف ایجنت (Interruption) و کلیدواژه‌ای که باهاش بیدار میشه (Wake-phrase).
🎙
2- منابع و استنادات دقیق (Cited sources): توی کارهای پژوهشی تمام ادعاها رو با منابع واقعی و مستندات و سیستم راستی‌آزمایی (Fact-check) لینک می‌کنه.
📚
3- وب‌هووک‌های خروجی (Outbound webhooks): فرستادن اطلاعات و رویدادهای چرخه‌ی حیات ایجنت به HTTP Endpoint‌های خودتون به صورت امضا شده و امن.
🔗
4- ارتباط ایجنت به ایجنت (Agent to agent): پشتیبانی از پلاگین R2A v1.0 برای شناسایی و واگذاری کارها بین ایجنت‌های مختلف.
🤖
5- سرعت به‌شدت بالاتر (Faster everywhere): سرعت لود اولین توکن (First-token) تا ۸۰٪ کاهش پیدا کرده و پرفورمنس اپ دسکتاپ به ۶۰ فریم رسیده.
⚡️
6- پلتفرم دسکتاپ: قابلیت پیش‌نمایش زنده آرتیفکت‌ها، کیت توسعه پلاگین (Plugin SDK) به همراه تسک‌بورد Kanban و پنجره دسترسی سریع به دسکتاپ اضافه شدن.
💻
7- تاییدهای هوشمند (Smart approvals): پیشنهاد تایید دستورات ترمینال بر اساس تاریخچه استفاده و قطع‌کننده هوشمند برای لوپ‌های ریجکت شدن متوالی.
🛡
8- قدرت‌نمایی در CLI: اضافه شدن ابزارهای اسکن پروژه، مهاجرت ساده و اجرای مستقیم کدهای شل.
🛠
9- هدایت بهتر ایجنت وسط اجرای کار: قابلیت اصلاح مسیر و دادن دستور به ایجنت وسط کار بدون اینکه پیشرفت قبلیش خراب بشه. نسخه‌ی قدرتمندتر Steer که داشتیمش
🧭
10- ابزارهای خودترمیم: توانایی خواندن خروجی‌های نصفه‌کاره ترمینال، تشخیص خودکار خطاها و بالا رفتن محدودیت تعداد تلاش‌ها.
🧹
11- اتصالات جدید: هماهنگی کامل با پلتفرم‌ها و مدل‌های خفن جدید مثل Buzz, GPT-5.6, Claude Opus 5, Gemini 3.1 Pro, Grok-4.5 و  Vercel AI Gateway و رفع باگ‌هایی که داشتن
12- قابلیت‌های جانبی: پسورد Vault داخلی، فشرده‌سازی خودکار سشن‌ها، لوکال عربی، فایروال و مقاوم‌سازی امنیتی روی ویندوز اضافه شدن
🌐
این دستور رو توی ترمینال بزنید، آپدیت میشه:
hermes update
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانفیگای کلودفلر من هر 5-6 دقیقه، 1 دقیقه قطع می‌شن نمی‌دونم چرا</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4854" target="_blank">📅 17:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">راستی این ویس با میکروفون گوشی ضبط شده و با هوش مصنوعی رایگان Enhance شده و به زودی AI اش رو بهتون معرفی می‌کنم
🥰
https://t.me/Editor_MatinSenPai/3</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4853" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید:
https://t.me/Editor_MatinSenPai
شرایط کامل توضیح داده شده
❤️</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4852" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ty96HwSUkAxsF4zY8jnvfzPZUHS3H-9c6xgihs7NeUIOd9In5-z3qRUFN1dDWh39TPlfh2ZXGoiGJSa5B61MfI0fi9JkAkWJCZKLm-fHLh499YSnXr9-dsq-PNEgz4jZblxNA5ECoj1I6cIfYCzA80q6KKEXm8dg6bvyPXCgisZYDPf5sz-WsXOUKErjtIBSr17kd5C0agk-oPdd3Q51utBtjNpxeXsMomCWXOzBOV89D2BYmnhZJeNK6VvXEDyUiwipZH7RWCnH2bv5QXt-NHg7Hd6Hli3fpyjVV2m66z9aWSJSDwR16sN9raXmhpvudBjl96ktMuVuJjE27Uyj7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ INCY که امیرپارسا بهم معرفی کرد خیلی خوبه
دم برادران روس گرم</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4851" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست  https://t.me/RasadAIOfficial و برای خودم هم جالبه کلا به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4850" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست
https://t.me/RasadAIOfficial
و برای خودم هم جالبه کلا
به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4849" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YOy-dC8qDsB6_ko-6cPRrKzlQksYSBjGG96IFqcWCoiG4n0TWPuc7MsRrcyx4Wq-dqH7swAUVAxUgxz-pVZnIxlLvT2x2UQk1UMIletKMdXDzqgNv0QhnZ6I45CHbFkatmv5zCgTL4SAQLal6qQBnj9UN9m0zk6OG6el5GuxtXi7wxhFite1sxifpYm0vz6mfaa2NUqFELF7c__BjMxriAsPyMqXwc5mOORvGVF5lki3bV-0GoeArbi6V-92G41_7hw_DaypSlYlz5pbZoOcGmmBCPLzr-5AHMALiIrWHR4vWNw647Xo_qBEud9iUgUALvuC62QDDwxKHVJvf4Hqyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Iv9nqaWfqG2MdsNj0oJX7ry4enNbMc5s_8o84PPGrEsZh_w3t8GPDtuBk6KuOxKpWgJA3xCtVfYrckEXFj_KM9Q3Cvbr6uTy_aPoFAdqNi-AugBbXPyKQLG-7KwdRNm1bk_dU4HMHadkV0UiNYGL5v6_cD_Us7LbuJ4lD8g2Rl5spOFoxtUVZoVecSwG8BcUthrSR5sJikUDwL-zIZhHgcXnyGCO76uRC2-30Adz17e-y_wH_3MDrsVy0_cU7P2Nz6NoHPbwMkTR9IwYYlTFbVnjVjTOchVHSetIiuBFXm34JvFGL6eQLOVY4JUgu7QMt3sARg8eqLyStD8QcnUkbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KE9izoglOH631b0b4sS3Cm8hhu8Eloo6Nr1XcERS7Ix7l6NBnd-6K6kvL8ik-Aqy2WWizKIQDLSutTo2dEEgkGrIBdfg5-SCXcUlXv2AXAy7JfYudGYcumhtN43RLJ-62WaJ7HuBug56LRE-_XlMEyRVSWQBxpvc8NQnYb_CykNP0z87DT6KlsfKaBXaQsDZTVN6_toz_K5f5AGF9BMxV_MotXWFRbJRixgCh4jQ8pEDle8-0aGClZg2eEqFNy2r_PNTssKy5JQH_zw93883xig64ezA8ae_50NVElbseI0gOKsHfB7JotJ5_SggEJjvU-680_AslwqjXVwMqorCpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم برای رفع دائمی مشکل هرمس با Antigravity یا مدلهای دیگه، از اونجایی که گوگل داره به پرامپت اولیه سرک می‌کشه، بهتره ما هم هوشمندانه عمل کنیم.
وقتی متن خاص اول رو تشخیص داده، متن خاص دوم رو هم تشخیص میده اگه هممون همون یه کار رو انجام بدیم.
پس چیکار کردم؟
این پرامپت رو نوشتم و بهش دادم:
توی
soul.md
هسته‌ات، برو و تمام چیزی که نوشته شده رو به یه لحن دیگه متفاوت باز نویسی کن. محتوا همون باشه، اما کلمات و چینششون تغییر کنه
و بوم! جمنای دوباره فعال شد روی آنتی گرویتی</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mC03Jf0hWvEp6diCU8qelC-vS4JM5_ODni8IwCshNJtRqzk0h0OPvEB2qbbe2GhsQ9wY2ub5c-ex3doffOup0YD0ujhNRCJXyWJpfy9kGbf1fnuQfuzR4HLP8uae4CoVkpdVOijCyUrOqVbv706XWNsimdsivnHSnn7uKhQJH05I6vuhmngvFndC8e9U3bX_Tj0Old7fmYcYQF8wIdgFHJY_mBDouflgAQvqZXOpe5Nde0YtXscBg7xCzJ-l5IwNTEzBkR6BJp2ML-twE2_iZLvfNdq8R6czYBP4bD2TLflqOvyxilJ5-lI-VbQlQvoZODLvX3vqfURKVeDXsyj1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SQOAOqI1OAvXcWA6l5WLimvYde0-Qa159AwSuuKIeeZfMnBxg8UL3fDY_z1wqSCOwEz5x9NTMoAtlyXfx6aLB9Uo7mclsAe5Zsg_0IIsafP4UyZ4tpCsWw_qV4l-5xg04lxQK-5pRhlFXvLtCmbqeCCM_4LbWKuOhlWdx05BMxEmiCOfh_AvgYK1vkWWCeUAgYAISRyX2UosVe_vJXIzH8w5ype14sdngbcL5FhXOhrTdGZflQYJ4mKrtp89stNPvwyLuqHzlM8rUFN4P7Qb2c1ME-tIa7JQqruonrwpfNY3PYYAjazI9uGA6A3nZOEczYWoUaMTSR5MiYzG6BjWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mBY1BoOBOvqp91aSjfarsrJNT0mKMbBHBpw3nd_9w4vp1HIn-KnNbUKhQiXWUAqHmvFVszIIHpKPAZW4QhAKoZBQV3yq6oXpNgnr-6TiNbcCIBO-hnkEVro6chQnHlTr2XlVDjIkC6nZ2GArsGOgbBjrqGSNpX2HJYYChb5dIaq3_QuhQsZAIuShZIBMkp80qIUzX7_6IdFG1HJcrXBKXy-lrlEgX_yQbtN6z9kUQ8dO4WUAcVhjTFYDO905XcZCREIRcS3YWBZuRc96WdKKfmQPqklBCHv5In1f8IzYD4z1nOKOePHLlhKX86I5rLQiEZ4FyU5XR0sap_TBjZ6NWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NzwCnIh8uvmLN65uuebUqVy0xKEVprNXPeJpf9dK8OLGuQslSs6rkHboSllxl-_hCdv0nSNYLcYC4oDRVQt0CwZkDYex0GisLmU9g64ax9TMBCXAJROBPUNpSXgPBwewic1cf-v8MplpLzPdY4BJJkZX6q9eaAgrR5S0Vf7aLydlPdPu5OWsBmPsIMqeiES1QoC46whlEByeinOTk6K0tM5iNmlrx6ftkJJeCh_-kfdWChI0r1fiXmCkapqCUS1u5IDu6n4ftRjmcrndhTuEY274AJa6k1El5sfSSbIjWJ_wmoHREXRl82053NZoInN0qBQa_6dtfKbw3TnylO98Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رفقا ما داشتیم خریدهامون رو به دانش‌آموزهای بی‌بضاعت سیستان‌وبلوچستانی تحویل میدادیم که یکی از همکارامون گفت یه خانواده‌ای هستن که چند ماهه وضعیت خیلی خطرناک و بدی دارن.
بهشون سر زدیم، دیدیم کولرشون چندماهه که سوخته و شبا موقع خواب میرن تو حیاط و پشت‌بام می‌خوابن، اواخر هم فهمیدیم بخاطر گرمای زیاد، یخچالشون هم خراب شده. بیشتر پیگیری کردیم فهمیدیم خیلی وقته که وضعیتشون این‌شکلیه و کسی بهشون توجه نکرده.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4839" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به زودی قراره یه چالش(چالش هم نه) ادیت بذارم، و ادیتور بگیرم
خوشحال میشم که اگر دوست داشتید، داخلش شرکت کنید
اطلاعات لازم رو می‌ذارم تا فردا</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4838" target="_blank">📅 00:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xu-6cocz9WjVx38hJhmDwnyYEwIoh4NLsfB-vr5IrZTrmwE5ygV-zGa3KqbN7XLX9BHH1We_XR3ACDSBAtxM2IUdP-nue44ukfO_-uE4JXzWgv6aYkEU7NyxyRogScfBmoCdpp_Xi9cyCqtwRHHIXsIbzqvGWMvof6vJxWcaO1UTtgiwn0CnFeNOuo9eP5L-oFg4UfoJgt790lpZR5R_r5BP4TiXcQ4mpeiGZIGzBTcNuqON3P-CLBGji7fwt0Rs6QTSgro-0BHxgeiFf3FVG5ANhKQQXuFCnDb4L_Gac1u8vzIVDbCYXSHAe_QoZKvEQfHYPlEZCljZTIPDdo7zrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4836" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1ja__CmqyiZPVkKjAX5PXoim4CdJgcBMJEgCD07l2CCxAGFrkvezrsn-0tJAXvtMtSYNbtk38YVVebYF-5s7Apcbfj5UynY3TzgI6gL3leqnJvTva0NuDzk3LwxSnUZCX1-iPimA2HZD4gWNuk4kzaTXEPczEhnm3tLzDuydig_4cE97jSWnBZFl3YjXr4PtDtwj2-fxja0GuUvqJ5OcRCA3Z-jRcFzAFgrykmtAXXKXoR6eqZFR14fIswa10DJOs__wCUInX_Nn8Hc3LR2jkjSfk_vrrAEhkCvVC0BAy7t8HzD0bEuRnGtemZtFoQVST9ZjooO90UefA48_k9SMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگزین متن باز Fonto، رایگان، تحت وب
دیگه برای استوریاتون پول اشتراک ندید
😁
و اگر دوست داشتید، از بالا(علامت قلب) به سازنده دونیت کنید تا لایسنس تجاری بخره و فونت‌های خفن‌تر واستون بذاره.
لینک پروژه:
https://github.com/FontWoW/FontWoW.github.io
لینک سایت:
https://fontwow.github.io</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/4835" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">و به هیچ وجه، به هیچ وجه روی کانفیگ VPS نذارید.
فقط روی ورکر و کانفیگای رایگان
چون به سرعت از طرف دیتاسنتر ابیوز می‌خورید</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4834" target="_blank">📅 19:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AFA9RV-ZFqifvcXukPgxfquKJQhrTwEnAoW8msUojWB3xi6P4U6qGlWIw7fxcmo9dpAPDTd5asfItSEGuveFTNilewOL33IdvT26GSOWbVPKR7AH6HinykxAX1BU2EUSfXQAPkODu32PBoSacw4nm8BqWAVTzyAwqR-hcobPcKB7l2SxKjUEzB_oS5ciTxIGtb6rURu5cpAGYL8fszanpiBybqlNrQZT4UvknJFQkmR1t18hIvpbuwOmQ3Wv4yFQrT2MFMa0fanERCIZ0cZ7cmfY-kj_bJ1GxJVIXkbC7OXVahbh37P4jGa54E2RnI7myftKrKLSYvnFLTwwaiWBPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n7WPlr5usAuo_6jQrJgN-UNO7epwpeEqPxDxptFF_3S8FunG9rZx8XcumIX0JrtH1sU3ddk3_ERQEsimCoaTQw5P-62FHCJ9_Rzd9740JbbxMC6CIuvp34LBsR6Ot8fSdmGlid53i77l7_JPGxzSE_ftgji1vSX9lwJpHMWmq5ce8kMN4c4ooZhlase0R7qmHdST6QWfaaV_axMIXrWw5MKJHRXfbpQXY2fDduXjlbxjGZAVpfTjUCzpO-nQzca03aMvcqRrbMVlCOmoqzp0p3GHA3KSvr0SmKnxFCGXZNQujJgu0BgDA60kkjQr2bG_pcSWBWgHHrvx4HQp_sJj6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4832" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/etcddSGjZ5DSvdhFxnhi06tVeAoW5AI8xid_MVkWvQPGhslBZLGBZpSakftmEs8maEgMnT4BtgmQ5_YqIthRUkNCclkiP8fSz2C39hEoXR1s5fpr7NK0pXYVLwYDCXqgC5LgWjIruHNOolbVLuLEqhmBSbNGK7NZSCO1TK8hR6bJBrGvhP3PFPyielMGSxZdIdGti4jwuRYk4QDLmpKTEEpjLjR-z4n9kVJZgucix861dz7Q1CK9weLXNJAnFyLkbGnpQm5mRW9MMSuaLezH9BjXgZ8jqNjmr2kGvPt5W6WclnVGeojjqEFWVkiob_SBUJyhQD3mC-5LtiH4n9Q0Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید: https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4831" target="_blank">📅 18:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید:
https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4830" target="_blank">📅 18:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4829">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خیلیا ایمیل دادن پرسیدن با چه شرکتی کار کنیم
ببینید شرکت‌های ایرانی همشون یه افتضاحی به بار آوردن. یا چنل پروندن یا..
من هم شرکتی که واقعا کارش درست باشه نمیشناسم. ولی خب متأسفانه وقتی مجبور باشیم، چه میشه کرد
الان خدا رو شکر دوستم واسم نقد میکنه از خارج از کشور و میفرسته و دمش گرم</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4829" target="_blank">📅 18:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r1vYdbIXG0ghGRl39oIrL6RzsRdKOka6JCQfVNGmHh-d7t0XLtRTp5kHghVfNlX2FGWGeK3o0yxMH_vecQB4tg4lcwyay6lte0z5pylMpt6c5ZiHSg3QsZbURQu2BGAOYaic1fDdS83FarhRT4iN2BjE7Zg5s90immjuPdLKrTgZXxCi3aJxU85bJ0vw5K8dUPuhTDovj2sRV4MTpZSRaJMZdKJcct-HBWX2jp4SFkTg6KjCvWgsQJo4ahHdciDtdI_zZPFACT3Y_M92YdDq_6zB2rzLaclsDw3NNtIxOdxIgyksf4c3wPOzJvCG_EDFfM5WWyNWT6VbeMNhLRd_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q9IDgMUs1LflCBgMfZ61STopwFn8oPTfdYrThcKaUe5gd605mI_35Q5u3awEhKEoGWXnHQILGFZlK---zqfLY0TmG_8eoUju2_cnWLTVM83uYuQWW_wMB4wlNxc9At2RDtB_DN3VBvpiuOq_EDfigU09brVM8WXEO27o4YR47t7-Yig1dZJ-vFyIg3eSwPV2bXBtgv5zBsYf-m5wjDq_CLBOJZ_RNrYY4-za0j255xGHzef9QVThVq-6ENHYtA_dpGDQS7-UjpRCooYfJQmKz7vbwCTpM57_Lm2O1kjderq2l-nMCWmMIVLF8McPkt6NFIGM_g3eW6LLZFssIKoaFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادش به خیر. زمانی که من یه میلیون تومن هم برام نجات دهنده بود، یوبر این شکلی جوابمو داد و هنوز هم اون سه تومن مال 7 ماه پیش اونجاست:)
تازه اونم با قانونی که یهویی گذاشتن.
همون روز ادسنسم رو قطع کردم و کلا حسابشونو از اکانتم حذف کردم.
هیچوقت با همچین شرکت‌هایی کار نکنید</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4827" target="_blank">📅 16:42 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
