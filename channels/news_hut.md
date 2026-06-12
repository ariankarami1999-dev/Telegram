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
<img src="https://cdn4.telesco.pe/file/lHjXCm15g_ZmsLKrDgTkaWYaGBNyXs7AkZgnlAReowFgaE8j5-_foP-Zb5nOI2M8kn4_jQT1y_AkoFHK9SSf2l64Sa7T3oa-4V6GjjKJjJ4VcWzteSxTYNwIPvHpJC7iDtf2d951up25tbnbxihuU4uMRS1w-Uhpx4GplZyCUnWuCqUeJ7tFHr21JtF4xh-hhkK6eTWSnJHhXrAJjO-L--4x_13_fsKz2-jRtqZfS6fQ_1DmF9fDEupHC229Ox7Qa3ZX_Z42Xvy_emzrjg-Ihgf3UbbJI9bDy-AmeqL0akYb9dV9hM3-CzNYlBhbSXqO5zTFlrIcNhMJt2NbZL5Rjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 225K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 22:28:47</div>
<hr>

<div class="tg-post" id="msg-65954">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
کانال 12 اسرائیل :
توافق قطعی است و این به نتانیاهو اعلام شده.
ترامپ از ایران خواسته به صورت علنی درباره توافق شفاف سازی کنه و هشدار داده انجام ندادن این کار پیامد هایی رو به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/news_hut/65954" target="_blank">📅 22:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65953">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
رویترز: امارات ۳ میلیارد دلار از دارایی های ایران را آزاد و به آنها تحویل داده، این اقدام تضمینی بوده در ازای اینکه دیگر به این کشور حمله نشود
@News_Hut</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/65953" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65952">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu8yG4rUfCx3YntLOhRAuriJw0rk3t2jNg1lrEcuKk7A1NVpMUA9xY256ZL22-3nPRxwOso5CeHtHEuXZ68vmclhbwMWNZHPuowjTRNUVwG5SB105cvKr055z2rMuPwNtUQMJcVpb-VYUfquNQ6lYeXI8ExlmMZJV-T7trpWpMk4JjJ-bGVv9yshvqt8LLMngedI6llDD-64mNEn8ATWRKO6rCY8KgjEH7aE4tBlHlvVF1L0pIk8fGGg6FZJ7tAUEqncAQdMUcL-rm_BcR7UTqk6cV1id3oMsFvK0KXWiWRohiYWKDr6cmuxMsWrPhvPiJaUUE6BHEc_rTsVGXFlsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#
فوری
: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/news_hut/65952" target="_blank">📅 22:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65951">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmcFuz9GPyguD91iLSJ4l9vywYw3ANJ8rFLtYIsg-Vrqr32MAYE6mAzAvYFso7HcCDxFxUFFc_74kFnoxCJUSfgvVI_WytS7dC6O_Ir2ltZ2rBhuXROSbEaErTfKvLt6Kh3oXJ4aQOgusXt9xdB1ic5NUWNvX_RzeO9ibkuDpIRNQiYIL1c4t13z5gW8SqZ00WRdye6CVqMHmGKs5e6os6V-Hn9KteO2nAhTyZMQJXG3kDLeBXmLNFdVkRFGakagMS7L2U49JGtj1_qATkqNsJDIAIuKREdg-Fkzw0evnBaQHHogtNcBNTgl8muy7UF_3MWWfbKQOOr1eZJybg55fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا به شیرمردان سپاه اسلام و حضرت آیت‌الله العظمی سید شیرمردان حاج آقا مجتبی حسینی خامنه‌ای، خوب دارین کیر می‌کنید ترامپ زن کصه‌رو #hjAly‌</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/65951" target="_blank">📅 21:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65950">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHlwQxF_Vqsl0YtcxnHNAFcKxJqJFawv5PT_fnMEMp3LkL8wCzMboNBay97cb-6yBWMdyUbgEpiu5MkS9Nee3c5iqQkmcWiMYCbBIMqrS3BNn57rG_R7rxDXeJiPoJjA4VZy2RYw10kTg6OoB29Rd-BsUq_k8V7OsIB0k8cnAyHqsjF2lbU5i-n4w92_-qcZJg6i2Swb__SIp3X2H8gt-6sHLFEGJZ7saapwTsSdprPzizuP4Yqvmp5dak1NW7-jg4PeZlwGmU3EA6Esgx2kxM9dS-sbHWiivBqGglpyLSPxTXcWC-BJEnQDO9p3ZBqKFvAgQAbjL4FF3gacP0e_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است.
نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/65950" target="_blank">📅 21:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65949">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
الحدث:
وزیر خارجه پاکستان امشب عازم ژنو میشود
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/65949" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65948">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز هفتگی پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/65948" target="_blank">📅 21:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65946">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kwt5oNeFK9uD--4YpgpZ546iXIsxFdFDZqC3TKcPwvU8yiLv3yCf8Tx0SPsPfOfZaNZ6L9LIRMNoaczXxWyp2PXi_f5xwgm1xe4L5OI-Aczlgi98OmU4ohF1LtQqr1S4DNhGZjU3AKJkuctVPOQUlKumOwmnUD0uHwv2wpEi6Fjt0tlp61jXv72doEPJfB9V7_Wh_-C03hTkl3oROWH9j8G7kyW9qny3uDtM6_FoJtLUn4I31qhJwhhQO9Lzvh_IzblZwJ7dLr8JvmK4N1djS0dzb6CrK49R1h0ZBtfrJFDKEsn3_CmtIYqWh2eLZqNZJmKU65YX4hEW3XEyr6qUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز
هفتگی
پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
نفر چهارم تا هشتم ۲ میلیون میلیون
📈
۵ نفر از اعضا به قید قرعه ۲ میلیون
🏆
فقط پیش‌بینی کن و برنده شو
👇
➡️
@PishWin_Bot
➡️
@PishWin_Bot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/65946" target="_blank">📅 21:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65945">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=OwWmCLLc4AgM7UpmtIunX8bROhMS8u68ZXnP-wD6VU6VndeNthNN5eMy1j6P5kTFRNWuBwhuv1HTGc_3gnSnzuwwACuqvCp8RR020P2tAn4maq4cq98vyVxisKstZd5xKyf_0fVvWWwdZhiv5VmE5BbU6kyBRYAOb2MvJTZsnWW8vkcxJxpZ8tgIK60E5gEBRfn82slejpnS21DeF4wTubNIdDS033jsQ_lb3TVthSjSPouH7p-IWGkr3AjSw3b8DQmTE6bmPvy1Eb2jw1G-WUoSxH4QSE4GwKM3ABNYE9Xx5HJEGhs-R7VZJvlufT4xfAzfjolCj7PRcqbSs0-Iag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=OwWmCLLc4AgM7UpmtIunX8bROhMS8u68ZXnP-wD6VU6VndeNthNN5eMy1j6P5kTFRNWuBwhuv1HTGc_3gnSnzuwwACuqvCp8RR020P2tAn4maq4cq98vyVxisKstZd5xKyf_0fVvWWwdZhiv5VmE5BbU6kyBRYAOb2MvJTZsnWW8vkcxJxpZ8tgIK60E5gEBRfn82slejpnS21DeF4wTubNIdDS033jsQ_lb3TVthSjSPouH7p-IWGkr3AjSw3b8DQmTE6bmPvy1Eb2jw1G-WUoSxH4QSE4GwKM3ABNYE9Xx5HJEGhs-R7VZJvlufT4xfAzfjolCj7PRcqbSs0-Iag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهباز شریف:   در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/65945" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65944">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVHpBXo4DLuq-qNomU3VvbYdzSRb1tZhkxwh_MJHwRlvTsqzD-Ieyqu4g7Rj0UJ7iqR6u9-4Bnge-gU74yhG1j6nXhzCWcWufchNP3a31A--ND8mL5cMaP6ZiBas8KFMIjMkHBi6lClZjH4Jkg_-U0dj9OIkRNnRaBcouQfukl1Xqp2ylg4hOrBRYuEObUUrYSKwqtafInP7YY3VzIr5iQ1iMUaAIpA-IfSbOGdDPgFwP2sxPRtbh96VHhw7Coi-zMnzLLO7oDM38HVGXmeA-D33yxMtcaYn2879REw1C1jJbROsgfqhm7ofDXsBXd9rue8IuzTi0-5OQDyscpYDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهباز شریف:
در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق توافق صلح حاصل شده است و پاکستان اکنون از نزدیک با هر دو طرف برای نهایی کردن مراحل بعدی همکاری می‌کند. صلح هرگز تا این حد نزدیک نبوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/65944" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65943">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b6a7c560.mp4?token=nbG0Oymmfzulz_6Q4mboysczj1ZPQmXBuw9pTAZRPfbVcBcGzwkW-Nfblulw6JnnNR2O5l9E9lJ6z4EolBHA5g9FdR-90DJ6OrMtlVsNIF32ivWqRRcXyjmBuRGf6xcxvvTFnUuRDazsLniK_BlKM98QGKbESpXNbQcUVOk-Iiy_sr8YBH6UF8Zj_e746jhm_HzNwaJGuK8XzGDrFRZ0keWR14XnGcb-_JFARpFOG78aN4wpYEUGsFNVr_E1XIF-pTsDByP9jwk9Sifmhnc3UNYJTnH5IThKbSXrNAKOS9R3C2ypRAqRdvHx8ak_PkcdrfZday3oxOhq9nUdKG1JNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b6a7c560.mp4?token=nbG0Oymmfzulz_6Q4mboysczj1ZPQmXBuw9pTAZRPfbVcBcGzwkW-Nfblulw6JnnNR2O5l9E9lJ6z4EolBHA5g9FdR-90DJ6OrMtlVsNIF32ivWqRRcXyjmBuRGf6xcxvvTFnUuRDazsLniK_BlKM98QGKbESpXNbQcUVOk-Iiy_sr8YBH6UF8Zj_e746jhm_HzNwaJGuK8XzGDrFRZ0keWR14XnGcb-_JFARpFOG78aN4wpYEUGsFNVr_E1XIF-pTsDByP9jwk9Sifmhnc3UNYJTnH5IThKbSXrNAKOS9R3C2ypRAqRdvHx8ak_PkcdrfZday3oxOhq9nUdKG1JNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از مراسم دیشب افتتاحیه جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/65943" target="_blank">📅 20:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65942">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOu8nuWRBX_Kt0-8O7Gb4fS_JKdKju3CSjLgvEPHDWhwvWpnEQJTZ3rGBwucyifFn6jHFUDeg4uyS769QdkDj5uhljN0z_4y1N-b_fAsOOr1e_NW0wZwjrvci6iyv9vXs-axHMEX3j7EKUchzEORSuBKHLa7RTuMVqdb_1MWLdERhHdXVAYxvRP7rQKe8k3J2hj1fAyfwdEvi1z6Nva5oaEDH4kGuKAzYUDmkQJvhezn3yxdMMIxZf743Wegf850k8O56ljO5IuXnhmSKtPlUiJU4MS-xfXWiaCjyHNzWN_7RNnIQXIuggjuisZ2X-Jpo0z4MHppakUgK3Qe8J8LbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندزی گراهام:
ایده یک صندوق بازسازی ۳۰۰ میلیارد دلاری، با توجه به اینکه چه کسی مسئول ایران است، به نظر می‌رسد بی‌معنی باشد. این شبیه طرح مارشال برای آلمان با وجود نازی‌ها در قدرت خواهد بود. آن زمان این ایده خوبی نبود و هر صندوق بازسازی که به نفع این رژیم تروریستی باشد، اکنون ایده خوبی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/65942" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65941">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65941" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/65941" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65940">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/samNzQYV8ACxELDw41PWpWpmwzcAumlSLJOUvL44FugvICzXxxOwfEyontXBpZXr1cKtrB3KBui8JUOVRV5of7DQUDjMbQbskVSNRfvCsw3uush4TyBqjyZ4dF44NtLoCtfVPUvLAxMZ3nljtqqHwM2BRXXV053a1eVwEihTkLbMeA3GpeA5ao33KLUMtQjaIvVG0b1HmHaTRVdWzf9Dmem9OdsFL21_7QRH9kwJAuKtUcp9IjM2rqi2XryvUzvu_lK9JklygbqteQ6BLlo1WJ1Hu2-92fhQb7tPYhpwwVwgn0RnvlT4j9fem_Jk3tjaHrgwxV-d_U7tmNepsI5Htg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/65940" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65939">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oujOM9tE_s8MDhmD8jfsEjObMj-8P8jPbFTs2igpms3I5Blh7dAtEEWJfBStFjgFcc8qGIaoqoJqZAGdIHItVLx2mJ8liJR3NPCjYuqf0aBYap7fJ5KjiPjcyyE_RoNo10YvZdz9tpr2XdK2syhE-zUmyjNPtR-hUz2FeirxXT_K_0pXzRIqQq1-uDKrHyRE1KltYLHnuqJVdI7vpkqiIt6li5a34MBKy99EAdpLpPSVEP61TLlmdrUCvIIVsnNXtbH5aqJay8F-83foW1eSUQxDj3EdxvQoONgz7rE-Yw4rOsqxpcUdgW8GyTYrlgRieiXCfqPOHzvJPB0X2J3leg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ناوهای جنگی و دارایی های هوایی نیروی دریایی ایالات متحده همچنان به گشت زنی در آب های منطقه ای ادامه میدهند و محاصره علیه ایران را اجرا میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/65939" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65937">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=gqrpGCYTwbHXr755tqNulWdTzXfMER1kiLuRhNZIMtazagw6oR6LmCuabAnL4TL2ZOsO1OWzELlGYXtdoAvg-qP0CUmsAVJ417kRcTBbvFdX9fiP31WRcDI4EZfHimUsRroU-3TqNTbg7ZjaIoXzq2a-m2wpuuRgERzOPdqHnOzDFysnjQ_FRvK833B9xEwYnanOlJyhkcwJyZq3Cnh2wALskWG6bfo0bxZnnssXlXXits7hQHzZT3Th8QkU8bDcYQlXhuUl1bJM-NAkwbkfD3WPALufCj_nRaN2Qy7YydbxvOeyUU2Q4MTnU8Ay1yrou_LdtEhgZldmle0P6PEemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=gqrpGCYTwbHXr755tqNulWdTzXfMER1kiLuRhNZIMtazagw6oR6LmCuabAnL4TL2ZOsO1OWzELlGYXtdoAvg-qP0CUmsAVJ417kRcTBbvFdX9fiP31WRcDI4EZfHimUsRroU-3TqNTbg7ZjaIoXzq2a-m2wpuuRgERzOPdqHnOzDFysnjQ_FRvK833B9xEwYnanOlJyhkcwJyZq3Cnh2wALskWG6bfo0bxZnnssXlXXits7hQHzZT3Th8QkU8bDcYQlXhuUl1bJM-NAkwbkfD3WPALufCj_nRaN2Qy7YydbxvOeyUU2Q4MTnU8Ay1yrou_LdtEhgZldmle0P6PEemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی قبل از جنگ ۱۲ روزه و ۴۰ روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/65937" target="_blank">📅 19:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65936">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI7shHJDCXge3eFqBHAw44OP0CHP8nphkjI2PKoSedoascBW7ZhHr8EvD4Yzq7YAituchejgRoJ634xGGBBiGInIhvc4kia_W2sVBI703P0DNxpdHnMTpbK22n2sLGWGg6AQHk-XCrshLTUcM8CAp3HhE0fw52JSqmqdXtfQHSJkn4tKgubrYMqyeizY1UuTFfZrlb6FlKDvpSgAyyVzRrBiZ55lnXNjVQFJdzPIZbD27FutIJBDdO3G76Vx5S0EOim-DiC8P8kBGAIR8JXlKp25dS0SGYrK7EatSbJ6CGVfj_AgK63wzYz52Wzm6s6mykRRpADpeQR8UjE8W4Rihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: تفاهم‌نامه اسلام‌آباد هرگز تا این حد نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از گمانه‌زنی در مورد محتوای آن خودداری کنند  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/65936" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65935">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
جی‌دی ونس:
اولاً، ایرانیان هیچ وجه نقدی دریافت نمی‌کنند و هیچ وجهی صرفاً برای امضای یک توافق یا حضور در یک جلسه آزاد نمی‌شود. این توافق به گونه‌ای طراحی شده است که نگرانی‌های ایالات متحده و متحدانش اولویت داشته باشد، و اگر جمهوری اسلامی ایران تعهدات خود را انجام دهد، فواید اقتصادی به آن‌ها و کل منطقه سرازیر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65935" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65934">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تا دیدن اعصاب ترامپ تخمی شده عراقچی یه توییت زد گفت رسانه ها چیزی در مورد جزئیات توافق نگید :)))) #hjAly‌</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65934" target="_blank">📅 18:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65933">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65933" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65931">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-1pIGIJo-rT8sJOFp4Hs7pI16xzSVXV00i5qQgHMBS8qkuLVd-HmcyXz9lEFLl2RIwDKr-h9afFyEgaypFGBuF7095kucPw-kCpBeEq4PRLyzXAyEhOxUKD5piuBmhe-b3RGwhKMqW2_44EBFMVs-C4M-LlhEFddUhSLivNVq2f-lDlptBwKF3DXrMjDmwG7Wu7b_aWib5hMsowFpPW_WGskF84G2dWNXhk78IBzVAfodIC9iU0q-JAsn31UAcne1_xcB9vzYYi8IQUbyVKlkUC4s5lt9rbsQxFvRQp65kB7_c_ca54xKdSumYGMMweqL16Fi96KguEG5A4fMLC3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbDGx58PySt2-kkDRnd6oN0W3HyF_K6McCWbFbudK64AmJTtemAAFzxD6tUH9KpSMdf4xwRDE6y9L-c-pdwPpUB2Xnhp_sBY1s9o2q83O5ZJ7dCUC_7PDDVfxaF-ND1GcSlYWASAbG-PffLro18t6b84nktT5lPr7OzgaWdMl-2_JO5VwOOZZPl8UaWggY4GkXnGF1T5HVSDhqTPJwkNLHZPgGrQtsR_9py5q2toaFrVTAUzdv0LAKnL8KyE38vvpg2Ede4C5liO0YzGbbxh1jVv-8OUo9z0MuFI8PKpRVbkwmz_IepVm2imL3OLPoYL_XcZehfwYGAjg0x88a-VbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برنامه امتحانات نهایی پایه های یازدهم و دوازدهم منتشر شد.
شروع امتحانات از ۱۳و۱۴تیر
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65931" target="_blank">📅 17:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65930">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=bi54Q0r-40p4gf0L6DxE39m3AmKCFhHrXZDu7NpsZjPb8cxtYxelRxqdqqq48uWwtwrXz1jAcy8AHPTaPuQNzXnHQX9WMX7G_Q_pYBbBTWOYIhbKM3i3YmmCj63sA519O9ktyvQlVNDQqU5XhsnjQpQt3QihJhLgm8HRVixwkOADnnxGxz46MsXuzF4Pt6TQ-h1T4qKJNM3kgKTGjYC6QhFGctC5twKFg1UrBIb_2cdWK6wLCUtg6PJeHKMqu-ogTkrKiuV0VtSG8JU8MPzBgZi71UCnY7dGt_wxvZmvZ9wEGl1FpEHOO-3cRL9DQ9TKEe8_V-MvIYJEMREf5a9Wzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=bi54Q0r-40p4gf0L6DxE39m3AmKCFhHrXZDu7NpsZjPb8cxtYxelRxqdqqq48uWwtwrXz1jAcy8AHPTaPuQNzXnHQX9WMX7G_Q_pYBbBTWOYIhbKM3i3YmmCj63sA519O9ktyvQlVNDQqU5XhsnjQpQt3QihJhLgm8HRVixwkOADnnxGxz46MsXuzF4Pt6TQ-h1T4qKJNM3kgKTGjYC6QhFGctC5twKFg1UrBIb_2cdWK6wLCUtg6PJeHKMqu-ogTkrKiuV0VtSG8JU8MPzBgZi71UCnY7dGt_wxvZmvZ9wEGl1FpEHOO-3cRL9DQ9TKEe8_V-MvIYJEMREf5a9Wzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین طهلیل ویدیویی بنده از شرایط خاص منطقه برای عزیزایی که تو دایرکت درخواست داشتن
🙏
🙏
🙏
#hjAly‌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65930" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65929">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=LCNmPyPZ68inCAezB_hgbPSsSn7ARWhMwrTr3Rtg9e6ywGJAdOFN1zKWY7hL6Bygte3ODEwz97kmJYSkjB3zWLe5qyr1kQ5kB_ovPBXUpiS8saGAgezLzfzN3v2uZEvU-Tf2PNL_hQRF5jfUPZ52kCCAf1Dfw_9nUXv4WXFts2D6h55cFihbyc7aC65O1RmZJc94nW1T5tc5ZXn0OHk72jyN2yLmHpDSlpZI1EKuaKmHKbFmkpOlAeiwNk6m4v0xXJ1cvbablB_BYS6ua65amahteEJK570WXp_nSBOgf2T5gDvepWhCtocV0x45VE3lTPVUOu5WXkMEtFGsv1d39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=LCNmPyPZ68inCAezB_hgbPSsSn7ARWhMwrTr3Rtg9e6ywGJAdOFN1zKWY7hL6Bygte3ODEwz97kmJYSkjB3zWLe5qyr1kQ5kB_ovPBXUpiS8saGAgezLzfzN3v2uZEvU-Tf2PNL_hQRF5jfUPZ52kCCAf1Dfw_9nUXv4WXFts2D6h55cFihbyc7aC65O1RmZJc94nW1T5tc5ZXn0OHk72jyN2yLmHpDSlpZI1EKuaKmHKbFmkpOlAeiwNk6m4v0xXJ1cvbablB_BYS6ua65amahteEJK570WXp_nSBOgf2T5gDvepWhCtocV0x45VE3lTPVUOu5WXkMEtFGsv1d39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه ای ۶سال قبل:
هیچ پیام مستقیمی برای ترامپ ندارم چون اون رو شایسته مبادله پیام هم نمیدونم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65929" target="_blank">📅 17:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65928">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65928" target="_blank">📅 17:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65927">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
ایرنامتنی رو منتشر کرده و گفته تفاهم نامه پایان جنگ دربرگیرنده این مسائل و موضوعات است:  ۱. موضوع هسته‌ای دست‌نخورده باقی می‌ماند هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65927" target="_blank">📅 17:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65926">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csT-9BajWAkSfalrlvG82n3criDu4pfm8s-tf3oEdEsJB7baTo77K1cAY505aUkxAjG6uxELSCjYh4Ib1xQUQBEHuCCOBra9oVYFVstPh1VzRICq7fraf0BwVSevKcOtF9xGhFBJ0Bm6FlM4D-Gk0MjHNYtN9VTtQ7gPylUvULbqpRsEGeiNbBI3tm1vtepcK8n3BaoM_Zd9Mc4dPbQ-pPP9WZQVQk_MUog7Zm1PTZEm7tbj60R7LmYjg5XhgdLyagBvBfLhaLAXPEzTjMTY_FMdZKiPko9srMSb5PPvXkSRKWASGvWgxMSsynI-uZlQczOIU0Fj8ROTqRhYASVZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلاکاردی عجیب در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65926" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65925">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Og6gyaHrqOviBGLpvjIQTuFN98G8aA8ej-LBny974rKVCp6WeJNBUqMcIzyfbw2q4bp5YyLVrEn81Xr4Ozj1jbKlUGQTcC07hDQKm6NLm64zjdl3NS0AKRlFv52qcEm7mAVSkHyTC7Il8Q5l1KFmEsqJElydqKZdDGSFBBmiWKdaZjFGgDF0zt60R2PAChMf90sNxcaWJHaEUIk0e0d1dK6QluJtrz3RJrsZLW483EKRoBRwr-No4BD_z2kUqAiNQAnNX9NE9Er-g4T8qoPTqtIUENKtHde0TbD91M95QYydMPLKcmaV1N1hz6v2YKKCBKNwDgMGTvC4I-gNeV99Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
ترامپ در سال 2049:
ایرانی‌ها هر لحظه ممکن است توافقی را امضا کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65925" target="_blank">📅 17:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65924">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKLU63msdXx907LgFjHa49GWLkpqr5wz5NEREIuxOJmHB2aWo3BJywgqrg3LkKe9korLNs1eztfD46CLLwyZh2hhE8k30mBwaBcfSifvnbPL72kIiblFgv0am-BypAUbOR5L9BLeBA7-Ig1AMeBsAXdwtux8O_Nem4C9Ymfk7YnZFho65qzs0vI4FmP9syiTtJI7_TZGVpMbIS0FSMLZEV7VpznhSqJxIl7Z0AZpGC-WW1G_s_lx_3_9J2j2Hpxfh1ZYFb2gojwDk-AaOutTfoHEjl-Yd38cOLhb_J0Fl5uiyHMst87vZU2SOU_zMNGX4by7VkFCQu6UCsLskGwk_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
مرندی، عضو تیم مذاکره‌کننده: یکشنبه در ژنو اتفاقی نمی‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65924" target="_blank">📅 16:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65923">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=vx_apZnqbdPY3lXA4mnQ_8StKejbLrRiMfPtKu92uUzYR59Wza1TcKoUQxzajjEGfIFxHjTMdESvSNOpXcIuB4QcDYc6aSv2utprt9754wsGU6ZGOKhKvUUV-aHcEb3O790Mda74jr93Qi7sWfKOOwlFNCwAwpzEAkj-2BHiy5b-66VkGM2aJ5noHDw1qE2b-NVTtMUQPoUq_RQvrYIVIw-1Isz8CBNphRWoAnn5QOYBI2Bz0Tqi6EhFKeNj527STasEyo0mMv_lk_6LU1jslZ22qPk-rKsoq5gBeKEbA8bAUP4A_ouelVrVeeGcT7ZYMRdxdqhsgefm2mAIDBafp7wZugqRnAfp0hhOuob9GHY3QQwSM-pRv3LlULFy07lErTHHAC84fcKCi8uMhY2kjo5qHawQBNeJKecxMbFX9kON_mupDaKOtNt4l9KNLMgPDczfEEei3eWuaNdKXKlaR7jWFTC6S-di9ygDnqj6Z9bGNmvvew7y45EVlqk6dOtyJpQSOg4WjEsz_o1Qldu-PCseVzn0NPuG5CY1qTAg76Dos_UtJzluMscUeEE8uL0Gw8U__izHkZtvC5_3K9_PX_dMvmrby2F4TsTF90nVu4UCtjxNskFcSTgEjkSvEoPLdIhlflxTarpVSttICQHecML0uQr8K_oh0Tg9MFjXQEE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=vx_apZnqbdPY3lXA4mnQ_8StKejbLrRiMfPtKu92uUzYR59Wza1TcKoUQxzajjEGfIFxHjTMdESvSNOpXcIuB4QcDYc6aSv2utprt9754wsGU6ZGOKhKvUUV-aHcEb3O790Mda74jr93Qi7sWfKOOwlFNCwAwpzEAkj-2BHiy5b-66VkGM2aJ5noHDw1qE2b-NVTtMUQPoUq_RQvrYIVIw-1Isz8CBNphRWoAnn5QOYBI2Bz0Tqi6EhFKeNj527STasEyo0mMv_lk_6LU1jslZ22qPk-rKsoq5gBeKEbA8bAUP4A_ouelVrVeeGcT7ZYMRdxdqhsgefm2mAIDBafp7wZugqRnAfp0hhOuob9GHY3QQwSM-pRv3LlULFy07lErTHHAC84fcKCi8uMhY2kjo5qHawQBNeJKecxMbFX9kON_mupDaKOtNt4l9KNLMgPDczfEEei3eWuaNdKXKlaR7jWFTC6S-di9ygDnqj6Z9bGNmvvew7y45EVlqk6dOtyJpQSOg4WjEsz_o1Qldu-PCseVzn0NPuG5CY1qTAg76Dos_UtJzluMscUeEE8uL0Gw8U__izHkZtvC5_3K9_PX_dMvmrby2F4TsTF90nVu4UCtjxNskFcSTgEjkSvEoPLdIhlflxTarpVSttICQHecML0uQr8K_oh0Tg9MFjXQEE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هگست وزیر جنگ آمریکا امروز ۴۴تا پرس سینه زد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65923" target="_blank">📅 15:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65922">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
خاورمیانه در این مدت
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65922" target="_blank">📅 15:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65921">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
ایرنامتنی رو منتشر کرده و گفته تفاهم نامه پایان جنگ دربرگیرنده این مسائل و موضوعات است:
۱. موضوع هسته‌ای دست‌نخورده باقی می‌ماند
هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت ۶۰ روزه پس از امضا انجام خواهد شد.
۲. تنگه هرمز؛ نه واگذاری، نه نقش آمریکا
ایران هیچ تعهدی در مورد واگذاری مدیریت تنگه هرمز نمی‌دهد. آینده اداره تنگه در چارچوب یک امر منطقه‌ای و از طریق گفت‌وگو و تصمیم گیری مشترک تهران با عمان حل و فصل می‌شود.
۳. پایان قاطع جنگ در تمام جبهه‌ها، از جمله لبنان
هدف اصلی تفاهم‌نامه، پایان جنگ در تمامی جبهه‌های منطقه است. آمریکا تعهد می‌دهد که اسرائیل را وادار به پایان جنگ در لبنان کند و عبارت «تمدید آتش‌بس» در متن جایی ندارد.
۴. آزادی دارایی‌های مسدودشده با ساز و کار مشخص
بخشی از دارایی‌های مسدودشده بلافاصله پس از امضا و بقیه به تدریج در طول مذاکرات آزاد خواهند شد. تهران تضمین‌های روشنی بر اساس ساز و کارهای مورد نظر خود دریافت کرده است.
۵. غرامت جنگ در دستور کار
خسارات وارده به ایران در تجاوز آمریکا و اسرائیل از جمله موارد مورد اشاره در تفاهم‌نامه است. ساز و کار اجرایی دریافت غرامت در مذاکرات ۶۰ روزه پس از امضا مورد توافق قرار خواهد گرفت.
۶. جزییات رفع تحریم‌های اولیه و ثانویه؛
موضوع مورد بحث در توافق نهایی
رفع تمامی تحریم‌های آمریکا و قطعنامه‌های بین‌المللی در مهلت ۶۰ روزه مذاکرات هسته‌ای بررسی می‌شود.
۷. سه موضوع و ۶۰ روز برای توافق نهایی
در مذاکرات ۶۰ روزه تنها سه موضوع بررسی می‌شود: استمرار برنامه صلح‌آمیز هسته‌ای، رفع تحریم‌های یکجانبه آمریکا، و ساز و کار جبران خسارات. هیچ موضوع دیگری در از جمله توانمندی موشکی ایران، دستور کار نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65921" target="_blank">📅 14:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65920">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
متن توافق پایان درگیری میان ایران و آمریکا تقریبا نهایی شده و منتظر تایید نهادهای مربوطه هستیم.
متن نهایی تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65920" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65918">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QlztSVCct7Rgx1x2BrQ5R47n4Baek8DaGgk0Ofi606troSxXbbkf5LiZOjYd1cMOReb5-Ti98fjF5IO12zTEG-tze6Q7m7lX_kYoJ9ZZ7oG-XwDofK0gerbSJGlSt4Jn8JuqAg6_KR86vskQQAqcRPZMumiRKULzqr8DXzMZsurXIN1S2FZG_iuF0mVEO6D1RbXHNj-4sesKOHsVcRbj5bl4jQrEe8S1DozVMyoBmbIMsW9-iltFZkzc2eWwsizoSHHMjKfBVwthdajs7rAYKQsxxELR1pVmcY67i0ZMk-c1sdZyS9prceIjct1dhnpbAsAeewqUKb1sn89Xtb5zSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PDGP2Hh6UCg8m4sjTw-mPmpeCBaWFxiDYLS4JxkBhZ67FmHbg4jYp_a64JPHDXOL98s-yupRrYW6VSKfZS-TERJGSH-MpU0DjtFWeojZdTZG5_63ZQ6TzZPk_DrOx3Xb_RIr-P-u_lNVxIq8ncNYOLciO-YxReIt3-7YVSJXv8j2XNWy_mJIij8BpOLCI-yvmIAz2C5fphlTMFWUT8HsQ2nPa8q6Oe22jeS8lbwRYzjqzYy3vysFyPcg-HZCtgCR8Q8oGk5nAUXxs-Njhr-eKD7_bXuLfHuiBB0Af9dAy_KZv_LGnje4UqCd2D22RR1c-Fp39b9bUl5l8Lad9YXNVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصویری که یک پرستوی نظام در تجمعات شبانه از خودش منتشر کرده درحالی که چاک سینش پیداست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65918" target="_blank">📅 14:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65917">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=HTh0rso3ldWCe52_d6FGKjjVYDZPKzcwKj5_Z8995h9Zocx28bKNzwXQXnMPgp0PN4rAo9ATP1iaYstYCaU1A3YVUNX2nNmqhjHEDNJag9LvwCwTSb91sU575A1QxKV_ZkdKCljyRpnZTWmeP2rnoP4rF81qsC0J9LbjlCpwgEovkYYCzafcK-_bZrzFxKKmMnpQEXy1_QmwxqPwvDFbSS2nNQL96O1SchjQOpKkaNm0VTqKTKm49AKpmMjcQxq9dTI_2eIP-nEyqedluNTC3sqT9ULE6SUcaORPFG8jMRP8eNbYF-fNJoXv9mwmbZHce2A9Oy2rHl9fRPR3gXpfuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=HTh0rso3ldWCe52_d6FGKjjVYDZPKzcwKj5_Z8995h9Zocx28bKNzwXQXnMPgp0PN4rAo9ATP1iaYstYCaU1A3YVUNX2nNmqhjHEDNJag9LvwCwTSb91sU575A1QxKV_ZkdKCljyRpnZTWmeP2rnoP4rF81qsC0J9LbjlCpwgEovkYYCzafcK-_bZrzFxKKmMnpQEXy1_QmwxqPwvDFbSS2nNQL96O1SchjQOpKkaNm0VTqKTKm49AKpmMjcQxq9dTI_2eIP-nEyqedluNTC3sqT9ULE6SUcaORPFG8jMRP8eNbYF-fNJoXv9mwmbZHce2A9Oy2rHl9fRPR3gXpfuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وزیر ارتباطات: بستن اینترنت امنیت نمی‌آورد. وقتی اینترنت قطع بود، وزیر اطلاعات، لاریجانی، رییس اطلاعات سپاه و بقیه ترور شدند. با بستن اینترنت، جوانان نخبه مهاجرت می‌کنند و این ضد امنیتی است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65917" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65916">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
ترامپ از زمان شروع جنگ ۳۹بار گفته با جمهوری اسلامی به توافق میرسه
.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65916" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65915">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=tWA4k7RzzoV8zNhFwwX8TtvksQzXi8lwbM2unqtSZlzA1qDJZotp4hcRbVaAUA403lLtFOVF9MvtXwp5rGK2hqGn1QIgZBYSmoxL0Zt1xc1-gLjS9KePvseQAjlk1Bop4TTFkoXCFq52RuYzG004PLwOBFNHtGT7a3J5ylUTbnauZoAOL9OSSJX8Xsbos6r5YFQG7C1bVrkepzJV8hQgyx6F33ySiL5DEWShPzGdJKanfFq05-ZCzaiwaVg_o6I3VIKct4vA6Fcd3YXf5CLW253d4Rm0QhHJOh7UlrxrESpMZ7VpvvWpB2eJaqLx3sgvgupL-qPXT5HNaJBsV00nUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=tWA4k7RzzoV8zNhFwwX8TtvksQzXi8lwbM2unqtSZlzA1qDJZotp4hcRbVaAUA403lLtFOVF9MvtXwp5rGK2hqGn1QIgZBYSmoxL0Zt1xc1-gLjS9KePvseQAjlk1Bop4TTFkoXCFq52RuYzG004PLwOBFNHtGT7a3J5ylUTbnauZoAOL9OSSJX8Xsbos6r5YFQG7C1bVrkepzJV8hQgyx6F33ySiL5DEWShPzGdJKanfFq05-ZCzaiwaVg_o6I3VIKct4vA6Fcd3YXf5CLW253d4Rm0QhHJOh7UlrxrESpMZ7VpvvWpB2eJaqLx3sgvgupL-qPXT5HNaJBsV00nUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آتش بس در خاورمیانه:
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65915" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65914">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65914" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65914" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65913">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=vnPJy5QyZ1VqIBk7-kPyZ5KFXqox7EeEy-Lqi8vnC7ENYMbBzwH3930xml7J1wddaOAiRw-y9awSthSO7Y3OgWmLf_ZI-vPw9YN-yO3fsRPVauHDEz7jNxMzImiSvVD8ExvMkxTgLSmATODvaxjZWtWjBhotwrnHqABkxLaNvI-4aTupZYdQ6tmuEwmcqAy4WJoeXXcSuKLf8aD8THsrdyOB0wXOrXNb1o23s-44sCZM0x_ZSoGubUwJnATHheDhLiWD8SmWPgaMZlc18cGiCpt2q-fkPcFKtEPovUmR49rPC8XEJaNPsKIf7GuFD7YQWllm4XHJxw9mDQpUrV-i8YqfARdmWJdUz_5xVmouEJiL4FRr2sY_dooMLIn2yH9cYdBr4H-LAGcdaBBQg69bNR0sLwbC7_10WlnaXHWjJF6PouBuLcIjQVoqSYjgdcVXjcDX_Rkfl5QrCOBkvpxCFKDQo1NrZNonT9yS-mtnAv-LAsaARqF2yMyOJK54o69wtns6q0CIZ1pY-jDkH5U7o79NdS_v99h19PGCZa-wgwtrd3_OIHyvp4iR5Ymy_q6u6iPBVJ6PlWWxQM-P5V4umDOi4wzzYrjp1ndSwTGEkrJrgFrmdH2h6p6JK3rVcBm3wE7yuq5cUplupsiSFbdeHto-JQwjBh8SP5szQ-1rWTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=vnPJy5QyZ1VqIBk7-kPyZ5KFXqox7EeEy-Lqi8vnC7ENYMbBzwH3930xml7J1wddaOAiRw-y9awSthSO7Y3OgWmLf_ZI-vPw9YN-yO3fsRPVauHDEz7jNxMzImiSvVD8ExvMkxTgLSmATODvaxjZWtWjBhotwrnHqABkxLaNvI-4aTupZYdQ6tmuEwmcqAy4WJoeXXcSuKLf8aD8THsrdyOB0wXOrXNb1o23s-44sCZM0x_ZSoGubUwJnATHheDhLiWD8SmWPgaMZlc18cGiCpt2q-fkPcFKtEPovUmR49rPC8XEJaNPsKIf7GuFD7YQWllm4XHJxw9mDQpUrV-i8YqfARdmWJdUz_5xVmouEJiL4FRr2sY_dooMLIn2yH9cYdBr4H-LAGcdaBBQg69bNR0sLwbC7_10WlnaXHWjJF6PouBuLcIjQVoqSYjgdcVXjcDX_Rkfl5QrCOBkvpxCFKDQo1NrZNonT9yS-mtnAv-LAsaARqF2yMyOJK54o69wtns6q0CIZ1pY-jDkH5U7o79NdS_v99h19PGCZa-wgwtrd3_OIHyvp4iR5Ymy_q6u6iPBVJ6PlWWxQM-P5V4umDOi4wzzYrjp1ndSwTGEkrJrgFrmdH2h6p6JK3rVcBm3wE7yuq5cUplupsiSFbdeHto-JQwjBh8SP5szQ-1rWTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65913" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65912">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
کانال۱۲اسرائیل:
مذاکرات نهایی آمریکا و جمهوری اسلامی در مورد برنامه هسته ای و مسائل اقتصادی است و برنامه موشکی در آن جایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65912" target="_blank">📅 12:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65911">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
یه‌یارو بیکاری بلند شده تمام اسکناس‌های کشورای مختلف دنیا رو جمع کرده و باهاش ویدیو ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65911" target="_blank">📅 12:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65910">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
رهبران قطر،امارات و پاکستان کسانی بودند که مانع حمله دیروز ترامپ به ایران شدند.
سران این کشور ها به ترامپ وعده دادند که توافقی اولیه با جمهوری اسلامی دردسترس است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65910" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65909">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9247426e69.mp4?token=KRp80intJySKBt-dcWy3sCAbgcnG5woFiizaUCqzGElGlhKli-2_9BS8l1VjspZgHMRsecquWC5FjDsPnShCTBYa3h_noICoWashzejLT_GPQHO-W3GjRLp4w-jjeVgdlG6YeD2-pAqAjnFYItlLgjbKw7p3cMuCQNUMgCi3Ze9-oAJAzWkt3zK-pQ5C0pEFLpVmsHs0r-icX1OsOz-pD7ckj6ZBOc-zYoJ8Od-Hmw3nX3E0vbTujSAywwNfgjvQ6gkSDo5OonvpTwpWe0YMnI7qplG-Pvg4uNXS3wWueWKlSgdMEROmkPP_chSjgSwVHjYsYuTrEknnjCobBH8qaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9247426e69.mp4?token=KRp80intJySKBt-dcWy3sCAbgcnG5woFiizaUCqzGElGlhKli-2_9BS8l1VjspZgHMRsecquWC5FjDsPnShCTBYa3h_noICoWashzejLT_GPQHO-W3GjRLp4w-jjeVgdlG6YeD2-pAqAjnFYItlLgjbKw7p3cMuCQNUMgCi3Ze9-oAJAzWkt3zK-pQ5C0pEFLpVmsHs0r-icX1OsOz-pD7ckj6ZBOc-zYoJ8Od-Hmw3nX3E0vbTujSAywwNfgjvQ6gkSDo5OonvpTwpWe0YMnI7qplG-Pvg4uNXS3wWueWKlSgdMEROmkPP_chSjgSwVHjYsYuTrEknnjCobBH8qaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یکی از کشورهای آمریکایی پلیس به یه زن مشکوک میشه که ازش اسلحه بگیره. تهش طی تحقیقات زیاد متوجه میشن اسلحه رو تو واژن خودش مخفی کرده و با تهدید پلیس مجبور‌ به تحویل میشه
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65909" target="_blank">📅 11:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65908">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
خبرگزاری حکومتی مهر:
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا منتشر شد. این تفاهم شامل تعهد آمریکا به رفع تحریم ها، خروج نیروهایش از اطراف ایران، رفع محاصره دریایی، بازگشایی تنگه هرمز، لغو تحریم های نفتی، و پول های بلوکه شده ایران است.  آمریکا موظف است طرح بازسازی اقتصاد ایران را ارائه دهد و در حالی مذاکره نهایی میان دو کشور باید در مسایل هسته ای و اقتصادی انجام شود، بدون بحث درباره برنامه موشکی ایران. این پیش‌نویس نیازمند نهایی شدن در نهادهای مربوطه است
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65908" target="_blank">📅 11:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65907">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک دیپلمات از یکی از کشورهای میانجی که بندهای متن فعلی را با من بررسی کرد، گفت که «ایالات متحده و ایران در مورد متن توافق به توافق رسیده‌اند»، اما اذعان کرد که هنوز تأیید نهایی لازم است. با این حال، هواپیماهای نیروی هوایی ایالات متحده دیشب با تجهیزاتی به مقصد اروپا به پرواز درآمدند تا برای احتمال سفر معاون رئیس جمهور ونس به مراسم امضای توافق در ژنو در روزهای آینده آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65907" target="_blank">📅 10:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65906">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
⭕️
توافق قریب‌الوقوع جمهوری اسلامی و آمریکا بزودی در ژنو امضا خواهد شد و به‌نام توافق "اسلام‌آباد" نامگذاری می‌شود. طی این توافق یک آتش‌بس ۶۰ روزه که لبنان هم شامل شود، شکل گرفته و ایران می‌تواند با پول‌های بلوکه‌شده خود کالاهای بشردوستانه تهیه کند
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65906" target="_blank">📅 10:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65905">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=Kw2zGybDqqS9qfWJ_5Dy7BRKhCgwCjLqOnOLIh9PjyEBHqACgCLpOcNFlcSK53elFOvRnoCKAw-ti1-WNCfPheT85ECM4WzqYx2fLOIAoGf0jzDb_DY4aMb7SxA_j5NqPovx3s2BYH21dRi3uwkWnVvf6vRoOGjyd3qHDPM2QkBg__ZcT9NK2BcY_m_CKG8enfc187Xud6B0UVM3ngJJcarNn93cEGOec9zvkoGq4YIeipqW0Ba3RiBSHnlWKII5iWIvKkm0wbuvPVz96cYZSYPvPxxU2lArNQHDk63Yk77tf-8TSJWsn5uHcfidYK5o0AH5-bagf_cTgSWrXaIjgFDcdPxx7NKI8HxTmLMjGWqtmDTwCm24HN6mmwP94DPdICi_YsLWfJv2DaLK8cc0ckJ-Aj77eOSxFW8SUQCZy2-mnZFqxB4_0nqKJOdNZIeqcKE5ck9Pl7PK4DaL8dDnVcB_kWGiY0pxjxb3TJJ_NGoLCf61FLQlzE4PEyNoatZ4uawadvYAqg6BukyYbsi386T_6dDG11_qPG0RCK5dbzsGn30jLfZHxk5379vxTVL4AwQkuVDSAl3qtdBG8ObTaDOOPKcRhe3c3MKHSszh5-jqLO4IDwa2Dd2PSSSn-bN0LyA9S7gvMmTBQZ2APQGPBptQxMYRpUqnNw3YLbQ1rQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=Kw2zGybDqqS9qfWJ_5Dy7BRKhCgwCjLqOnOLIh9PjyEBHqACgCLpOcNFlcSK53elFOvRnoCKAw-ti1-WNCfPheT85ECM4WzqYx2fLOIAoGf0jzDb_DY4aMb7SxA_j5NqPovx3s2BYH21dRi3uwkWnVvf6vRoOGjyd3qHDPM2QkBg__ZcT9NK2BcY_m_CKG8enfc187Xud6B0UVM3ngJJcarNn93cEGOec9zvkoGq4YIeipqW0Ba3RiBSHnlWKII5iWIvKkm0wbuvPVz96cYZSYPvPxxU2lArNQHDk63Yk77tf-8TSJWsn5uHcfidYK5o0AH5-bagf_cTgSWrXaIjgFDcdPxx7NKI8HxTmLMjGWqtmDTwCm24HN6mmwP94DPdICi_YsLWfJv2DaLK8cc0ckJ-Aj77eOSxFW8SUQCZy2-mnZFqxB4_0nqKJOdNZIeqcKE5ck9Pl7PK4DaL8dDnVcB_kWGiY0pxjxb3TJJ_NGoLCf61FLQlzE4PEyNoatZ4uawadvYAqg6BukyYbsi386T_6dDG11_qPG0RCK5dbzsGn30jLfZHxk5379vxTVL4AwQkuVDSAl3qtdBG8ObTaDOOPKcRhe3c3MKHSszh5-jqLO4IDwa2Dd2PSSSn-bN0LyA9S7gvMmTBQZ2APQGPBptQxMYRpUqnNw3YLbQ1rQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه خبر:
با صراحت میگویم بخش عمده ای از شروط ده‌گانه در توافق وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65905" target="_blank">📅 09:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65904">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=LDCFnMjDH4tDhugA9DndVzpssjvmiMYF3Ar2I9q2GhsHgVXe3jOmZWjcFiJj14-EX1gAlCxXQrVw_bzi3fcG_VkruQyzzR1BOdn1Z7CWGxlLzRnQTcBkpcj_8zbRrc53Ofp1vOQUvkqTlXu22RTYfwKfZX03VVBVNQLhhNpSYQLsye_24a4Fyi2erqkIxlw82lCTfiJO9YO2tGYUAoq5w6X8fB7QvNJB7tU7NPZ7_V3Gmj3GprUAyphQ1hpzPJue1bYs-eXS5TFqHW_9C6ZkVc5i2T7dn_zxUnaLjWP2ZD5vqt4_pQ8XkF1NA_cOFMIJrzaG_l4NGUNkCzmn7Z6k7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=LDCFnMjDH4tDhugA9DndVzpssjvmiMYF3Ar2I9q2GhsHgVXe3jOmZWjcFiJj14-EX1gAlCxXQrVw_bzi3fcG_VkruQyzzR1BOdn1Z7CWGxlLzRnQTcBkpcj_8zbRrc53Ofp1vOQUvkqTlXu22RTYfwKfZX03VVBVNQLhhNpSYQLsye_24a4Fyi2erqkIxlw82lCTfiJO9YO2tGYUAoq5w6X8fB7QvNJB7tU7NPZ7_V3Gmj3GprUAyphQ1hpzPJue1bYs-eXS5TFqHW_9C6ZkVc5i2T7dn_zxUnaLjWP2ZD5vqt4_pQ8XkF1NA_cOFMIJrzaG_l4NGUNkCzmn7Z6k7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته شده ترامپ بعد دیدن این ویدیو تصمیم گرفته که توافق کنه
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65904" target="_blank">📅 09:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65903">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3oNpFp8Hy50x1FGbsF2bSzKROlmq8X4fn4HpDnuGoFuJS_0lfyr-enIFiI4Ceycw7PuwkVRXbpzXtE7yD-ouN-RiVKRwpDjqd9oDdDe67K-7NiAt_z9Y592YQdJ7CY_-__WY2k5qf7CzmsJhMNU_PJ2zmQwrYetnDaeoET4Zm5a7FvomqAj92eO4A3ipCRmE6qT_QOejJYopapr2Zq9Y2wKT9cioWqBd3OawCZ2qh4WqZK5XXRYgSahTxBnxUWhEHkXS8WmWuykTOIT_8Ur1Ie22928S6ZoLssPZhVDasavWNi_ZwLlNvDqtp7MWiP-K6XAIWJe7MJf2X92sbg_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین:
اگر همه این دولت‌ها با این توافق موافقت کرده‌اند، شگفت‌انگیز است که چگونه همه این دولت‌ها به این سرعت امضا کردند در حالی که ما اعلام می‌کردیم که در اسرع وقت بمباران خواهیم کرد.از آنجایی که این توافق انجام شده است، آیا می‌توانیم آن را ببینیم؟
در این توافق چه چیزی هست؟میتوانیم آن را ببینیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65903" target="_blank">📅 04:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65902">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZQb1MSaEjIcvE6tjthgWOOizAw4uad8fUULb9ho_r1nnsKzs4-yBcno8afWThFjK7aCtMLD855HCyid6HtMrh4rN1pM0_GPyMgxLVK2x4eFQNg7wEt3OrpgZapQHlJBc5qTeTh5gz43ONGNGCS1FfTh5IJQaInJPCRBIidwwzBTLHsjgwxoKu894WEYJIPtpUXtD3aOvl9lwqQ1Zk3t6eL8v3ljWC8hEu5DDAKELHwG_kcFqAZIQbhi661It4eUTzbPWKcnKVm0sjh3SapB4xVkGZ5GCThXKH9ML8lezI-lE2My6jydaNnOEy93Qhcwh2pLzFL8DGK_XLlbqeiUXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دقایقی پیش زلزله ۳/۱ ریشتر در پردیس تهران به‌ وقوع پیوست
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65902" target="_blank">📅 04:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65901">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
رئیس‌جمهور ترامپ درباره ایران:
ما با ایران توافق کردیم. معامله بزرگی انجام دادیم. هیچ سلاح هسته‌ای وجود نخواهد داشت.
مردم خیلی زود به خانه‌هایشان بازخواهند گشت. تقریباً همه چیز تکمیل شده است. ما هر آنچه می‌خواستیم را به دست آوردیم.
نکته مهم این است که هیچ سلاح هسته‌ای در ایران وجود نخواهد داشت. یعنی نه توسعه یافته و نه خریداری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65901" target="_blank">📅 03:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65899">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=gBbThlRr5HhEk_ZUkCost8ZHlkn9piGwfRpZGXPz_fbMjmW_zTL-oXCshoYNU0X1oXHfyh02mWwKFUOcoZJJ6znv593dhFyV1r6qth80lEeJPKz87SpRACAzA6fpLIFVH40d_DdOda4UJqTmw_ey1FjMzr5PFpj3KtOEkd6JqDXxTyol8g_Fnt_Qlh4fFqPs6reV9P7HZPC3rLZnPBTSyhb0hWHP-fWNbJ6q70Sy2Yy7b-F2fJCrwTmQSXXFa9RflLRV3AzJqkLq-JFLVnHxyWrTumw3vVGU4TAZXdMW8ftTiqri12qqyA4LkKQTwCh7-zGZ_ULN111d3MKhrfsqKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=gBbThlRr5HhEk_ZUkCost8ZHlkn9piGwfRpZGXPz_fbMjmW_zTL-oXCshoYNU0X1oXHfyh02mWwKFUOcoZJJ6znv593dhFyV1r6qth80lEeJPKz87SpRACAzA6fpLIFVH40d_DdOda4UJqTmw_ey1FjMzr5PFpj3KtOEkd6JqDXxTyol8g_Fnt_Qlh4fFqPs6reV9P7HZPC3rLZnPBTSyhb0hWHP-fWNbJ6q70Sy2Yy7b-F2fJCrwTmQSXXFa9RflLRV3AzJqkLq-JFLVnHxyWrTumw3vVGU4TAZXdMW8ftTiqri12qqyA4LkKQTwCh7-zGZ_ULN111d3MKhrfsqKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ درباره ایران:
امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود. این ۹۵٪ از موضوع بود و آنها این کار را به قدرتمندترین شکل ممکن انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65899" target="_blank">📅 03:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65898">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65898" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65897">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hVCis5oO5Teh-Yq7yN6HkZNHW7fTOPYdAsLRKeQzcJwGu1gZJrQ8nabu3DhLcGVQkM9v_4tFB21sULGmOpgiCjDxTUoA6-S9Y4w83RA0WTbjah13ViXueDMPKPByLn_V569PhPoIUkkJ6GpCSLHFcfTGE23dP6FPGtTkZx8VSqmS1gIFJ7ml21hR80iy9evg7t4HmB5HDD4Q1s7RJ7VhbPILJb3a02P_JsqxF2NiTPZhxnU0cAy-aY4a-gUqSu5R-cmeqMXr3h8zjMau52Mu_XO31DW22EjosmVOQDZf7_7xqrECie1X6i01QodE7nTQ2C-4DhI1_5DU3bIa093kWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65897" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65896">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
صداوسیما:
شنیده شدن صدای دو انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65896" target="_blank">📅 01:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65895">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B26t_YEG3Frv9TB5usWyGOwhQ6w_FjLpKZPeneSSNYIvg8jxPKMjhMhQZDlP607x2RB_skOA5sNTHE_hYZEMrWJF6qjc_i5oMX8Fj2KaE5q_QgDAp_SafalNKcz4-jyykod8fXunZ6H1T-bQ4VWKxMnghSe86g02P76TT-0OCqcr7ceE2az8MgLP0ZP88ZmSWpC7AsJzQ_qjqSscYVwOusr5Xyj3_1EWI4RPD8yW7DwfWPYlE-lGqb7Y0r_vaeezRfC9Za-CjTSSHnqOd6ShgO3Z2IVmNdj2DtNufmaVhCxGG5x1A9a-nbx7JtVtWqENzafgPvu7cZxwPEEghhurpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اعلام کد اضطراری یک F35 در آسمان امارات
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65895" target="_blank">📅 01:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65894">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دیگه نمی‌زنن
😭
#hjAly‌</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65894" target="_blank">📅 01:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65893">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
فعالیت سوخت رسان های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65893" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65892">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
مهر:
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی در دست نیست، اما با توجه به دستورالعمل‌های مربوط به بسته بودن تنگه هرمز، این وضعیت احتمالی می‌تواند در همین راستا باشد
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65892" target="_blank">📅 01:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65891">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هایی تایید نشده از انفجار در گناوه
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65891" target="_blank">📅 01:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65890">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
منابع محلی در سیریک صدای انفجار شنیده اند اما هنوز علت این انفجار ها مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65890" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65889">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP3ftwETEcQ1D_YpSZA_Ezun0T71xURgI_dDBIOMkRwo22l9uLN3S0zy3JHvj8g4N_u-bS1AaRp0vcZID8W2Jpz9wSrheVhaBxjlPr07tePP8EEE4L7NzHJAZ4FoShaowZPDEwUDYz1vqlIPI5xWPcmSaa578QvEzsXKMEieGJiAj8wA1IhTh3wxGoRcho4M3ff7HBV_7q2JFMNS3XZIhBDRVM9H5AaOT6FO0CMlsyfRoiv0RTy0DBwuHawXtxqEWZ3xJXOTIKz3juiP7m-akK3eA2BSJMkVTYXG9xIlCvIrIf16N0Us9ZOs6bSwufTBe80gO9zYbtrjzl-IB29xaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💥
تنها یک پست از ترامپ امروز 1.3 تریلیون دلار به ارزش بازار سهام ایالات متحده اضافه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65889" target="_blank">📅 00:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65888">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐌𝐈𝐑 𝐌𝐀𝐒𝐎𝐔𝐃</strong></div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65888" target="_blank">📅 00:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65887">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما به نقل از سخنگوی وزارت خارجه:
قطر و پاکستان به‌عنوان میانجی‌ها فعال هستند
وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود اما آمریکایی ها مواضع خود را تغییر می دادند.
ایران ثابت کرده است که در آنچه را به عنوان خط قرمز معین کرده است مماشاتی ندارد.
مواردی که درباره توافق مطرح می‌شود گمانه‌زنی است و موضوعی نهایی نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65887" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65886">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwTBfOWHYHi33IJXqozr0n-g3oU_LbBAEd2QmHG8JKUvzXOEBMosdr2YgZsFYsQJpAizjizMpO5PUPfWoLLVnSdPf2d7vGOJxKLtAir53uKD6G5D9qxzbGsK7zzCET9vtOaX5VNhMs7pntbregMILHDktIULyFSXJjSieBaANSdVItOqF5eQ7_QoMa4O9pG7B1mw-l5sXtPWxBnchfg-kp4Q1H-sI9AySYMUg73dCWrRvdI77IK6xh3AS-lzGCffnoRTedFrqe88_cZfToUxiPqUYB-Z3oVkd2C84RZJ9Xv1p782RrjfxsgJ6rrx8VWpgTLs2euQTAaqaMVN_5g8iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:   رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد. اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65886" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65885">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.  @News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65885" target="_blank">📅 23:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65884">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:
رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد.
اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات شامل حذف مواد غنی شده،برچیدن زیرساخت‌های غنی سازی،محدودیت تولید و برد موشک و توقف حمایت ایران از گروه‌های تروریستی وابسته به آن در منطقه باشد، ابراز قدردانی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65884" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65883">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: بعد از توافق سریع محاصره رو بر می‌دارم
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65883" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65882">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65882" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65881">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ نورالدین الدغیر خبرنگار الجزیره در تهران:
دیگر همه چیز قطعی و تمام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65881" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65880">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65880" target="_blank">📅 23:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65879">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=ZiVqP0D2sfNcWAl3DYAks-cX2vtt06_uPZfAWCRZUclad5djnRZYmR-TMWYZRpw_-y9VlgxTxOrNOBECO1IUqaGGgRAYVBBN9a_-J71qP7Q3GEX86MhGjhR-UCfv0H3t-t53cX-zYk1RWlpQjIw1-KgVGAsZki2qI9i50BG0h0jnX-7xI4CdH974GpJPuaa2B0vzhTLzm4o5JazmsDc-kK2FMKYJo238HaAYapY0fCoUexunaXbcJq4w0ctMoe6gQncOKT40OpT7bEux35M6lL8jXEKCwBAKDbSF4eN8-P3uWdddM0HqftChlNKnH9sAMkizxSAo3BEtnP907W8c2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=ZiVqP0D2sfNcWAl3DYAks-cX2vtt06_uPZfAWCRZUclad5djnRZYmR-TMWYZRpw_-y9VlgxTxOrNOBECO1IUqaGGgRAYVBBN9a_-J71qP7Q3GEX86MhGjhR-UCfv0H3t-t53cX-zYk1RWlpQjIw1-KgVGAsZki2qI9i50BG0h0jnX-7xI4CdH974GpJPuaa2B0vzhTLzm4o5JazmsDc-kK2FMKYJo238HaAYapY0fCoUexunaXbcJq4w0ctMoe6gQncOKT40OpT7bEux35M6lL8jXEKCwBAKDbSF4eN8-P3uWdddM0HqftChlNKnH9sAMkizxSAo3BEtnP907W8c2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری
: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65879" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65878">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=HL6_6aRn3XbNrsnRaFEgvy2dzE5VF9fERJpk9UN26uHDcMQBEebMA1BJBfcVuSfjoTu3YBDDoDFZzi5v3GP8CVpp5oKAjwG4UODDMkyXyabuK0cT2lYVwLs17SHAb3BvT8AuQXpwxEmSl2wHNeHPjxi7A-jEHmE4FOrvMRk5KPOYwWQoghToKN3-8Bb7yU1q1tXwDKviVy3iEXxxEVBcrCi4reJjqUC156sXfRyv52pmbWR-tHJvk_H5KFSlJushXd6Z8be5AmAM3BIalJ3vcRmPktt9x2aKi8diyuiZ1Ri80t0Z2AucquJ4SR5REj7o9_hyX9KCe7cg9Wc6Y5zVLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=HL6_6aRn3XbNrsnRaFEgvy2dzE5VF9fERJpk9UN26uHDcMQBEebMA1BJBfcVuSfjoTu3YBDDoDFZzi5v3GP8CVpp5oKAjwG4UODDMkyXyabuK0cT2lYVwLs17SHAb3BvT8AuQXpwxEmSl2wHNeHPjxi7A-jEHmE4FOrvMRk5KPOYwWQoghToKN3-8Bb7yU1q1tXwDKviVy3iEXxxEVBcrCi4reJjqUC156sXfRyv52pmbWR-tHJvk_H5KFSlJushXd6Z8be5AmAM3BIalJ3vcRmPktt9x2aKi8diyuiZ1Ri80t0Z2AucquJ4SR5REj7o9_hyX9KCe7cg9Wc6Y5zVLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرِ واشنگتن #hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65878" target="_blank">📅 23:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65877">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
منابع شبکه العربیه: طبق توافق، آمریکا تحریم‌ها را کاهش می‌دهد و محاصره را برمی‌دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65877" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65876">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOw9nepQ4ztZ06aT_ibByLsvT05EieBCElKcpLuXP9jyGchZ-s-zRHVE6yDyk3CxIv0-XUvrAlwX1gT1xb0ZpEc_MYb5S5CaRpJ6QrsXMhfdIwMXCxilqkYkZ9CA_vJZHUJdiOWplVlKZBHGnRF-qzylk45Qn-KXyGOoSIT-cvEpFXeRYvWzJPGPyhE4giBK_TJ-LvsTapUdTqJY3ObbpyfpMJQRidZIxEfuCdgPSq8HvWDJ4QZt5G4lSluF2ZpxqhQ8D25DcO5t3VBgBWu6xe4P803eZErBo1NBIufMvOd1gfUNr-H_EFmTy6MxB48dX4fKvz5Blzt9UjjROUEU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیرِ واشنگتن
#hjAly‌</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65876" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65875">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=swqirH3Emh9JFeehMSUVxsW_DHxAfb8LC40gRlczZEKt1Efb6oCXY2Nz-nRlXIXmXx7lNptGODvRmh2vJ97-G5id3XElKyEoPmK6vfN70to-2NNVYeUE9YsK9umWhSyH2Yzgtj3ULi7ZNuvwM7eDVnrfxGljSc6cByglryL9lYQcs7XCurnC5sio1CHVUaXXZ90k3_p-gtB9DA0OTGlXvf6g5cWy6n6ZB2-K9ZJL91Xbn0_yoZx3qsuoOrilfDRcBcMo686zhlbtoG0rxWEimC8wub7Mje5zTJi_OPu-qAhdXPPljWP4CFDsB6dCP-eJtbsi4HSnAu8KhYf9HpF1JF-I3dp3Gk_xXDqZBpu0rmz5KmEsqcH-pDKSjAtx1e8y3kD3uKAcDMM-g0JypdUUa8BywpSUezBK-TyhBl4QK03rg1gDVC-xrqX-y9Xf1xIVIx_shGuzj36pezo2gn4k_xkeXEF78bcHXUCuMmUxZfk415sRgFQ5M-frLX8-eqZ1P3DfGBl0i-eBUr37OKc-sSGDmUbRZtUd-03I7-rfcBDbFhQTFHJwltyGd2n1ccgLZEkFpCqqPNWWim-Tx25AL4sNPptLcWS5rs7sLcgc4dhZwiCcigYPaagstUk_68c7eBQyyMZCJt02s1zGSD_MI4umJH2m2iXc5l1DGZ7r-s4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=swqirH3Emh9JFeehMSUVxsW_DHxAfb8LC40gRlczZEKt1Efb6oCXY2Nz-nRlXIXmXx7lNptGODvRmh2vJ97-G5id3XElKyEoPmK6vfN70to-2NNVYeUE9YsK9umWhSyH2Yzgtj3ULi7ZNuvwM7eDVnrfxGljSc6cByglryL9lYQcs7XCurnC5sio1CHVUaXXZ90k3_p-gtB9DA0OTGlXvf6g5cWy6n6ZB2-K9ZJL91Xbn0_yoZx3qsuoOrilfDRcBcMo686zhlbtoG0rxWEimC8wub7Mje5zTJi_OPu-qAhdXPPljWP4CFDsB6dCP-eJtbsi4HSnAu8KhYf9HpF1JF-I3dp3Gk_xXDqZBpu0rmz5KmEsqcH-pDKSjAtx1e8y3kD3uKAcDMM-g0JypdUUa8BywpSUezBK-TyhBl4QK03rg1gDVC-xrqX-y9Xf1xIVIx_shGuzj36pezo2gn4k_xkeXEF78bcHXUCuMmUxZfk415sRgFQ5M-frLX8-eqZ1P3DfGBl0i-eBUr37OKc-sSGDmUbRZtUd-03I7-rfcBDbFhQTFHJwltyGd2n1ccgLZEkFpCqqPNWWim-Tx25AL4sNPptLcWS5rs7sLcgc4dhZwiCcigYPaagstUk_68c7eBQyyMZCJt02s1zGSD_MI4umJH2m2iXc5l1DGZ7r-s4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره جمهوري اسلامي:
ما توافقی داریم که ایران هرگز سلاح هسته‌ای نخواهد داشت، که این کل هدفی بود که باید از آن عبور کنیم تا به این برسیم.
اما ما به زودی امضایی داریم و اسناد تقریباً در شکل نهایی هستند. بنابراین خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65875" target="_blank">📅 23:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65874">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
دونالد ترامپ: در مراسم امضای توافق حضور نخواهم داشت و جی‌دی‌ونس قرار است عازم اروپا شود  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65874" target="_blank">📅 23:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65873">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRMliZ4F_2HY7tUSzbDVsb_-OHKrzD_CFv2W1mVZ3L5Q-tXCrI62sdo-xCT4l-9ekY1-UwqgFGgxGPYuyu7BBXGBUTd0qGkAKOWYIlEXBs1L905R2E4TapRS9xlq8I1CqufgqkAK6zjWt3o5lyUbArbHOhVAHhWawAsSq4blzcIl4wzSzeXKGrrDTweYJfWSDAaRLCff84xO1TRkV5ABJ0sgcq2lHByoB9euyNgcZaZoSCM8ibbD54hN-EdvZNOdbn7salbGkMn50WPQh2A4g3UhENT-JV4kc_yN3T7G5Db5c5ovSyHFf-obu3wlRwEw2icSTmvHaY2nEns9uauWpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره داش آخوند های حرومی تسلیم شدند هفته دیگه جشن آزادیه
🤡
🤡
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65873" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65872">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ترامپ: توافق با ایران بزودی در اروپا امضا می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65872" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65871">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ترامپ: توافق با ایران بزودی در اروپا امضا می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65871" target="_blank">📅 23:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65870">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
دفتر امیر قطر: تمامی کشورهای منطقه در خصوص تفاهم ایران و آمریکا رضایت دارند
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65870" target="_blank">📅 23:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65869">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGiVrEz7iB5gcSoQAqos5c1r0V2agpy2TZxrqH-QpFRJS4zUFgg_p_S4hPE3objkxzgmL6kx2SU5fTbW69KflHlrufCxdO70edlnWYVcAmKHVW0GEJrrtQoTjOCqVTqkd3XAeAzg55d01MVPy-kaHx1IXn5WOaxKUx6q7cZNfzwedXHEig1aPVMN_7Qp9CGdPkiu1ME0pjOFTFk4kyfCjDHF4PmjWy9wpmF-A9yRs2wP1bLorsbSRK3Z0jcOIOdrHWfgEiDFgon7Fqh0FtbuVLCsFEMdNeYvhOWthTxKtUlvZ1XT-B2vk8ZLTgivTpkJXg0x-oCXx3nMTF8PeNmBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
صد درصد بیمه ویژه مرحله گروهی جام جهانی ۲۰۲۶
🔥
⏩
تا یکشنبه هفتم تیر ماه، روزانه با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های مرحله گروهی جام‌جهانی ۲۰۲۶، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد در هر روز از رقابت‌ها ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCUP1
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
✅
دریافت سرورفیلترشکن اختصاصی
💻
@BetForward</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65869" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65868">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
ادعای اکسیوس:
منابع ایرانی امروز به کشورهای منطقه اطلاع دادند که توافق «اصولی» در مورد یادداشت تفاهم حاصل شده است، اما تأیید رهبر انقلاب همچنان لازم است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65868" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65867">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
خبرگزاری حکومتی فارس:
‌ منبع آگاه: ایران هنوز هیچ متنی را برای توافق تایید نکرده است
هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تایید نشده است؛ این را یک منبع آگاه نزدیک به تیم مذاکره‌کننده جمهوری اسلامی ایران به خبرنگار فارس گفت.
رئیس‌جمهور ایالات متحده ساعتی قبل در پیامی در شبکه اجتماعی تروث سوشال ادعا کرده بود که ایران در عالی‌ترین سطح با متنی برای یادداشت تفاهم اولیه موافقت کرده است.
وی دقایقی بعد در اظهاراتی مشابه خطاب به روزنامه آمریکایی نیویورک‌پست هم گفت که متن مزبور جمع‌بندی شده است.
ادعای ترامپ در حالی مطرح می‌شود که ایران و آمریکا بامداد پنجشنبه یکی از شدیدترین درگیری‌های خود را پس از اعلام آتش‌بس پشت سر گذاشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65867" target="_blank">📅 21:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65866">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
آکسیوس:
به گفته سه منبع آگاه از مذاکرات، قطری‌ها و ایرانی‌ها روز چهارشنبه معتقد بودند که به متن مورد توافقی رسیده‌اند که آمریکا نیز آن را خواهد پذیرفت.
این منابع گفتند که اختلاف‌ها در سه موضوع کلیدی کاهش یافته است:
سازوکار آزادسازی دارایی‌های مسدود شده ایران - مهمترین مسئله برای ایرانی‌ها.
تمهیداتی برای بازگشایی تنگه هرمز در طول دوره آتش‌بس ۶۰ روزه.
چگونگی انجام مذاکرات بر سر برنامه هسته‌ای ایران در طول دوره آتش‌بس ۶۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65866" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65865">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: زمان و مکان امضای توافق بزودی اعلام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65865" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65863">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🏆
🏆
بزنید افتتاحیه ببینید
🔥
🔥
Persiana Sports (بدون VPN) Bein Sports (بدون VPN)  لینک های m3u8 رو با برنامه های iptv player یا mx player - pot player - vlc پخش کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65863" target="_blank">📅 21:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65862">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(ммd)</strong></div>
<div class="tg-text">🚨
🚨
🏆
🏆
بزنید افتتاحیه ببینید
🔥
🔥
Persiana Sports
(بدون VPN)
Bein Sports
(بدون VPN)
لینک های m3u8 رو با برنامه های iptv player یا mx player - pot player - vlc پخش کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65862" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65860">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IQpVspbsS2L_cKQS1N_WQG76aaruVswRXjHw8WKE0s_EXqNNSqmZ_GZju5lrSv19-C1sCeiwhIWeW49yLpdwpwMT3yKaqtiHpXNmtY6JhOTsmurQLNVMGW0Cd0nNBfD2dIlnw6SoGPrd7jwrcGbHemiETYfVx4v6XAktQzJrukZmsNugK74kSluJpScSSsXKA6b8G5gWkGRVGjtYHz2R2sSYQvr-5JYc886rDxr3n1zOMaPqINVjZIfEPcM_IVnkAeRwlyfiwnCRSxxXnCTLL22RF6QUFxfPp-xu3unFScwTnqfn55yQmmpIKpG7FQnLpzIHc9feEfn4WrV1i6Qngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HtEeiluXSa0sE5Zs1TdSJL737Ne7KiU_LKO7AD-0HiB4kdUGm2yTc_TTYCpgSldudjk-pSIm59q8U6X-Zckf4MdZoxRPBY1GG7IFsMxOiyBTpuxXopEWAzfrWa4YBevxtxlu4U-JS5mK0etD81FdZPkj0cOVGb-yMg9Fw2lZKtou7CpeO3KyNTFg7YgMo-_FsA3XwwudaFJ7jAre_zSC7XFMmqVZTvltLUna8fcdXIPmzP8E8gda6Mj9iC4BZxqXpOZLF4OlUgmvQEi-CWTCoNptZOyvRen0-ydtn4At0FYrpiwCNANbOTh5MDM-a4KJLKffMDfD9H0LasuwEmROng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اجرای شکیرا در مراسم افتتاحیه جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65860" target="_blank">📅 21:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65859">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJvYLl-ltOrk-yABTSr-BGuWDo0qFGiDsYNty4Oh9wMPhE7K7DdH-QP-JlQOaKSsRDiKTFNCNSX6FjdIFt2aOB-HFNXQ4vFlz0lfqn-h_xoZvePkv856l1gr3zfRat8oYsnTNsWEbpF2nCcPDDHr3ktzJL-jJK1R22hJkKSN8u1isrQMj6abdp6Bmu34RN0uOUIjpKp6MdepufCfx1AvZgUDB4Zn3HYjnTe1-9qKe6j60E9oXfEbVuZHa9HK7zsADWFLfTB40I8F0wEhl6pY3pkMVStfjttctc5lxnkYfMnrv9PeodEWzkkEsl103BSRmwczAWEluegAh2g6hsdPFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت سپی هست داداشمون
که در تمام سه ماهِ جنگ vpn هات نیوز رو برای پوشش اخبار تامین کرد، هواشو داشته باشید و می‌تونید از داخل سایت بطور زنده افتتاحیه رو ببنید فقط کافیه یه ورد بزنید
🔴
لینک سایت
http://Chosefil.com
🔤
لینک کانال
@officialChosefil
#hjAly‌</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65859" target="_blank">📅 21:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65858">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ=حرومیِ کاکولدزاده #hjAly‌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65858" target="_blank">📅 21:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65857">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ماشالااا تراااااامپ شیردل
😤
#hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65857" target="_blank">📅 21:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65856">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr_e0uxoT19SK6WtbJlQlWMUApMZKhTTlhU5Aub2htUQ6nMvIhba9X0BR27X-n_y1dcJwb4XDcmLbC_AgwC1_NhQ8dI_eBJ7edw1icq6Xwn93ylsGPaPhoB2kyLoxhkD_VcC9q4ESOM6z6HLmSBkkWJodV11FnO-o0_JEY-BjgQhicRt4MaVQRqjUvUKOEFOhmwDbS5kcdaI9MiTI-_eG1uP4OEDUv9om-MEO0abYKgkx7A7ADS7N8TsSJOCp-9M9mRpWmx59nCqx7Q728jOFkmuahYCMjCH0Va3D9cfLsmlgW2UeMkCaevDYzSGU1mzzkKsb6devoWixhYxwR6Gxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
حملات و بمباران‌های برنامه‌ریزی شده امشب علیه ایران را لغو کردم.
با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایرانیان برده شده و تایید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده امشب علیه ایران را لغو کردم.
مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات فراوان، توسط تمام طرف‌های درگیر، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران، تایید شده است.
محاصره دریایی تا زمان نهایی شدن این معامله به طور کامل و با اثر باقی خواهد ماند
زمان و مکان امضا به زودی اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65856" target="_blank">📅 21:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65855">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
#فورییی
؛ترامپ:
حملات و بمباران های برنامه ریزی شده عصر امروز علیه ایران را لغو کردم
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65855" target="_blank">📅 21:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65854">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
علی‌عبداللهی فرمانده قرارگاه مرکزی خاتم‌الانبیا: صادرات نفت و گاز یا برای همه خواهد بود یا هیچکس. ترامپ اگر خریت کند تمام منافع و منابع نفتی و انرژی منطقه را با دستور قاطع پودر می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65854" target="_blank">📅 20:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65853">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e36d42b7.mp4?token=tR6e7oTNIpfYigOprCwP0RHdK9VjL-9rIPsUj7TO_WJpn6aaZI5hl9DrydSAYLub9JZAT7f5MlbeeaaFYNNBpJMgFjOK85ZelR-OWXJqzbepecxrq3kig4BHIXj-VQ4mQKEey0qsTvaPZ_Hd_tquMJZBrbn6Q9UigPBIjurirTpklTbkJ24uM0ECz1m6GtS2ok6f1azfReBnNf5x3Nhz5snMpfnahFVv36nRA600C5MnUZIEsfBMKeBtDxSuI3Q7AOqor-j0Dr0aDkAUpXEFA_HR9sAB42H28GhjZ3mY2Ds61XTVh9s-R_XooSMpF-dndhSDPTifZYv5ASJPcy6Iag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e36d42b7.mp4?token=tR6e7oTNIpfYigOprCwP0RHdK9VjL-9rIPsUj7TO_WJpn6aaZI5hl9DrydSAYLub9JZAT7f5MlbeeaaFYNNBpJMgFjOK85ZelR-OWXJqzbepecxrq3kig4BHIXj-VQ4mQKEey0qsTvaPZ_Hd_tquMJZBrbn6Q9UigPBIjurirTpklTbkJ24uM0ECz1m6GtS2ok6f1azfReBnNf5x3Nhz5snMpfnahFVv36nRA600C5MnUZIEsfBMKeBtDxSuI3Q7AOqor-j0Dr0aDkAUpXEFA_HR9sAB42H28GhjZ3mY2Ds61XTVh9s-R_XooSMpF-dndhSDPTifZYv5ASJPcy6Iag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
تهدید وزیر خارکمبه علوم: اون دانشجویانی که پرچم پهلوی گرفتن تو دست و پرچم جمهوری اسلامیو اتیش زدن تحت تعقیبن قراره مجازات و اخراج بشن
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65853" target="_blank">📅 20:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65852">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khFRZwDgQcvGNnydnfVs0gksojl9U5E59A2Gu1B_Wq0o7QVprtrc_Gdx1_ag_G8qA_z17JXS0mhFzT6B0PtprpK-ZPeQwBTgtdMP49oFiABU64yYwI5gBK1Nvh9XPyShdEGEY1fBy_S3KsA49VLblNopLSBWVcziAqQTv_s9v5VyfDI0QDHWGXXGNU-chDBHLhveZ0hwCKsZJsBRisCDpDyNQpjYki7te3cptPW09UzyhjdbYFFcu1FzTLpy8wBzYxKsu052vjsd77vPr7E5dvrGyOxZ_1VnZsuKgzbXqpANAfjDpLRBi-T3p90ReANjQh1lfO0pVd0KPb2WDrES5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قالیباف:
استراتژی‌های اشتباه و تصمیمات عجولانه، کل اوضاع را به سمت بدتر شدن تغییر می‌دهد، زیرساخت‌های انرژی و بازارها را منفجر می‌کند و باتلاقی بی‌پایان ایجاد می‌کند که سال‌ها در آن گیر خواهید کرد.
شما ایران متفاوتی را خواهید دید.
زارت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65852" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65851">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8YFM_EqZO4DlkOjjCVucKOh_ic9YwaIqKOQIpG7x3knWs4A9TvC_JNrkpbHk2bQs1iPqj1ZYTkm_np3RG8igh8kPVJ4hr2toIGFQKBNMnFXqTd4QMRNRMo6NAvsGoJpYpzcQ-UxBehtrBykAZwHNqcBMX0ggfC-2fxwZLPSCCaz_f4js4MpdWLuUhVJB8gvll7P93TRzSlGQp5ZIUNiesWZahftp5A7xPS_XEcOdrFNfINCFbjbZxKEcZSSPMAVfiK1f1zbsGFS9UYSlNaUwOU7sUgDKZPL99uWNJsVgphmTR_nnzTFlzwi-0jid6hxdhYUu90WAAaBQNOQ097eog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
به‌روزرسانی عملیات در لبنان:
سربازان ارتش اسرائیل فعالیت‌های خود را برای دستیابی به کنترل عملیاتی و پاکسازی منطقه شمال رودخانه سلوکی در امتداد خط دفاعی مقدم به پایان رساندند.
منطقه رودخانه سلوکی توسط حزب‌الله به عنوان مکانی اصلی برای عملیات پهپادهای انفجاری و حملات غیرمستقیم علیه سربازان ارتش اسرائیل استفاده شده است.
این نیروها صدها سازه تروریستی را منهدم و بیش از ۵۰ تروریست را از بین بردند. علاوه بر این، چندین سلاح از جمله دستگاه‌های انفجاری، موشک‌های ضد تانک و موشک‌اندازهای ضد تانک کشف و ضبط شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65851" target="_blank">📅 19:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65850">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZ1DRub9UZrRsHzGcQHsMFgM7dxt2d98grAu8iaT9lnVp9iN6gCAQ4XnN-W3hVxWj1n3_sZfwYp_kfNpsp_AtsxOiCDFeuBHz4n3DoNzk1kKmLp6bOtR7GLP7vDiFLjjxu0irlk3CB2egtDeEGlV2DqImbhZgDM6d7z65Fs4-B50DLETOiTzANKyDm3lpQcAu-br3ccTzGnA2z5AvIL36442_XndHIZKTWc12iTF8Pzgtc57mYohqQUWUdKoYL3KFKXjySYvJK1Wtgkq7rYbFbXfzyjfxXJxjY4rOVrpNfcQrwQniEeycFUxJPtC5-xNp5VRij_wgFDlFwcfL0Ci5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پست جدید سنتکام:
تنگه هرمز همچنان برای عبور و مرور باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65850" target="_blank">📅 19:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65849">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
الحدث: ترکیه، مصر، پاکستان، عربستان سعودی و قطر قراره جلسه‌ای فوری برای جلوگیری از شعله‌ور شدن جنگ میان ایران و آمریکا و پیدا کردن راهی برای توافق بین این دو کشور، تشکیل بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65849" target="_blank">📅 19:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65848">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
جمعیت هلال‌احمر اعلام کرد که در پی خطرات احتمالی حملات امشب، در آمادگی سطح بالا و کامل قرار دارد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65848" target="_blank">📅 18:59 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
