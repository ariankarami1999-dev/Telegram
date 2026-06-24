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
<img src="https://cdn1.telesco.pe/file/aEC37PnoxOPuq-UUphTpSuVweXPHqUcNcC0I17bVu7-vyIV29edZ1KdCKR6hjULyW6ndciwCV1cj4Lid7J-_jCo9dskKc55U2-ebq1y8o2bJ189snVdEJkvnJhrr3yPyEraK2fSsL-lwg7Q2Zockn5UFY9oqELepvORGQwaca5jDFIxS7Fv9Cc6QrCejHDfhV0iq7RW6OBUi1Kef_HziElYlam-UG7ucCwuxldAvKZtYBQ-80L7gmIiKyOlM34_vAMR1VrnUY1ejgnu876LCk0677toznkpYXkoUV4ByLYTH7AWdNM1mFbc_yCQEjj_8hlyMRbnbuQqQNp598X5-kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 160K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 22:38:16</div>
<hr>

<div class="tg-post" id="msg-4007">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حالا ای کاش قیمت سخت‌افزار پایین میومد یه کم
😢</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/MatinSenPaii/4007" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4006">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NjwAmULcexwCZMRbjiZuTDCjV2mo_tRphE8MtwJmuRkLkaF-8N2wD7FslxIUjNT0gyZ5dooQs2CVm9B81RbOyUGwpbAakhh09nV0AEPTz5dAbVZZvbsTUGLSQd1ZQDX8EhC370SskAkJ8M6EpRL4MwWBrXo_N4Pu1lYQV1Lil0BwVB-wAoosJHFi01vQoi_nf-_XrJUDZw9igt70pYvpsmg-L6XUz3geBoJqzPjlOyAX_WUIKwnpuwt6srt8LfgT-IJ7CCCWQs4sCDwxpBgOPFgh6tVO2zfm8MzdRZQZGKg3YMgPzXQvSZ68UqnmW4ow9k_gNP9syYfDwdNHT_Sokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تراشه هوش مصنوعی اختصاصی OpenAI با همکاری برادکام معرفی شد
شرکت OpenAI با همکاری برادکام از نخستین تراشه اختصاصی خود با نام Jalapeño  رونمایی کرد. این تراشه که از نوع ASIC است، به‌طور ویژه برای فرایند استنتاج و اجرای ابزارهای هوش مصنوعی مانند ChatGPT طراحی شده تا سرعت و پایداری خدمات را افزایش دهد و دسترسی کاربران را تسهیل کند. OpenAI می‌گوید فرایند طراحی این تراشه را طی ۹ ماه به پایان رسانده است.
خالق ChatGPT که پیش از این یکی از بزرگ‌ترین خریداران پردازنده‌های انویدیا بود، به‌دلیل رشد تقاضا تصمیم به توسعه پشته فناوری اختصاصی خود گرفته است. نمونه فیزیکی تراشه Jalapeño هم‌اکنون تحویل OpenAI شده و انتظار می‌رود استقرار اولیه این شتاب‌دهنده‌های هوش مصنوعی تا پایان سال ۲۰۲۶ آغاز شود تا زیرساختی کارآمدتر و ارزان‌تر برای آینده هوش مصنوعی فراهم شود.
✍️
دیجیاتو</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/MatinSenPaii/4006" target="_blank">📅 22:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4003">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-armeabi-v7a-release.apk</div>
  <div class="tg-doc-extra">33.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4003" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بیلد کامل اندروید SenPai Scanner، با تشکر از
Hidden-Node
عزیز</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/MatinSenPaii/4003" target="_blank">📅 21:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4002">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">توییتر هم دیدم چند نفر گفته بودن اما گویا منطقه‌ایه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/MatinSenPaii/4002" target="_blank">📅 19:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4001">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کانفیگای کلودفلر روی ایرانسل واقعا دارن بد کار می‌کنن</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/MatinSenPaii/4001" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4000">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tUVJAdwKtfUBRrIFchN0QnBO-pGLnQygyRDYNBwRScIm195AQgbYaHPQaBgup1siMLKl7Xql0-AoINsN5MDuz3o6xkiYX0uWB8he_Ph2xYHTMZw6lrf0oGyefF7LgqUG5-jdwUPqdRUFsyrWVU3C21_hee223uCDuZ_X-r4UL5M-vngTbvBuP7sQbdQD0ZRtdghNP2Fp5mmygUbhFoQtVJOauTLuu0KkNlGVgkbjkkb7ftjmedo05Vq-rL0E0nH5YwBAQ5Zd0iGLJlOJhDFTSWuI8c_Vwybc7tTev6mQljsLrs8aKP-JTAJHAVXSgErvBFdLehOmO8dMvj72vOyPgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس رو هم دارم نصب می‌کنم، به نظر خیلی چیز خفنی میاد. به زودی تست میکنم و ازش یه کم کار میکشم و نظرمو میگم</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/4000" target="_blank">📅 19:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3999">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟  یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/3999" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3998">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3998" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">به زودی نسخه یونیورسال هم ارسال میکنیم.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/MatinSenPaii/3998" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3997">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟
یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/MatinSenPaii/3997" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3996">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">برای دور زدن تحریم‌های اندروید استودیو، قبلا هزارتا پشتک وارو میزدیم. همزمان Shecan میزدیم و پروکسی و وی پی ان
🤣
اما الان با پروکسیفایر که وسطای این ویدئو
https://t.me/MatinSenPaii/3372
آموزش داده بودم، به راحتی هرچی نیاز داشتم با کانفیگ‌های کلودفلر دانلود کردم. با pdanet+ هم میتونید دور بزنید</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/3996" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3995">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">برای یه کاری دارم اندروید استودیو نصب می‌کنم و از الان گریه‌ام گرفته
😭
خداحافظ جای خالی روی لپ تاپ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/3995" target="_blank">📅 17:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3994">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:  برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید. برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/3994" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3993">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:
برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید.
برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.
بعدش روی آیکن مربع (سمت چپ فیلد Name و آیکن سنجاق) بزنین تا همه رکورد‌ها رو  انتخاب کنه و بعد پاک کنین همه رو.
اینکارو که کردید برگردید توی قسمت overview  و روی Review on Blocked Content page → بزنین.
توی صفحه بعدی روی آیکن سه نقطه بزنین و گزینه Request Review رو بزنین و I have removed the content. رو انتخاب کنین و بعد روی Request review بزنین.
یکم بعدش باید آنبلاک بشه دامینتون.
هرموقع که آنبلاک شد برگردید تو قسمت Dns Records و روی گزینه Import بزنین و اون خروجی‌ای که دفعه قبلی اکسپورت کرده بودن رو این سری import کنین که راحت همه رکوردهاتون برگردن.
احتمالش زیاده که مشکلتون حل بشه و دامینتون برگرده.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/3993" target="_blank">📅 15:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3992">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">از اینجا مستقیم میتونید برید سراغ آفر دیپ‌سیک رایگان اگه گیج شدید:
https://www.openmodel.ai/event</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/3992" target="_blank">📅 15:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3991">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اگر دنبال API رایگان هستید، OpenModel مدل  DeepSeek V4 Flash رو به‌ صورت رایگان در اختیار کاربرها قرار داده https://www.openmodel.ai/
✍️
0xdavinchi</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/3991" target="_blank">📅 15:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3990">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uTX9LyLQqkVoS7dwIYcHSRSSeczILY4gSGk34bLF1RL334hLWVHnd0IUmlcwZmALo7b1v_NQB-s6UXJkLD2Q8hknuIdYEBqAII8tOgodHxva3oV7TIqoGzIzVJOn2ewdFNuj3tHcZ9BaYb2oE4lKzy---BdhmIujLkoJluXIqwE2FL_snw77LYCQdThfxck_8bUKq1swoXs9auARFwRaAT31WYB__3I0FbxC7UrNxBGfK373HKZFtvNiD5RpQ_vFlSCPmfDUH60kijAPE9hB2wHPEAWOMUYTYbBPWVp1Iq5Z7tm0UJhNRSmEdVJYoKOzZ9DU3VnpOXClRR3FFvGH_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دنبال API رایگان هستید، OpenModel مدل  DeepSeek V4 Flash رو به‌ صورت رایگان در اختیار کاربرها قرار داده
https://www.openmodel.ai/
✍️
0xdavinchi</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/3990" target="_blank">📅 14:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3989">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OiRW-a2oqooP5t3gr8oKllEJ-tFViHqQPU27S0EMbDjo9FM9Uty56Ljr2a3a0zcSUArXRVVwDVxT3o6S1laNxOx7lloC8EkctVmoyewAsK-6Hwiz8Kb-18LqAY_3HDBA6BzgsQ3lFVMUtQoMT3-8hBL8mOPW1zGFneopqEJBup7bGtJ93FP17Q4Kdmf6tUbxze08WpfJfzzTOXQ8u2ev47_kK-snizWMVNdZOGkJh2NzBQFde1KLFqE6vuJfI1XjR9_WiX7PRwU8m-x0vB_xS7Xg8s5ybRDldDUQcsPPELbVk05Yjaa8KXYIyxqbclzTeXNi9A2AxrDDL6NGFSOk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت اومده همه بازی های کنسولای قدیمی رو یجا جمع کرده واسه بازی آنلاین، از آتاری بگیر تا سگا و نینتندو و میکرو..    Site 1: retrogames.onl‎ Site 2: retrogames.cc   @Linuxor ~ fireabusefyan</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/3989" target="_blank">📅 14:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3988">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8v7qlbFDGSzwhWwaOiMv2c-hITDyi1pQZ5ByvP2MxkN18xhv8nVDnwCjr-faVwPB3TAEvDQPzPaJhjTuveGqL27j-CyEVnQKwhyajbe1OGO567dJYV0YAN-kewES-nUQKi8Bo-V9-cRlFgE-9c7AKNpgYA7KTFAY0UwAhTK8ApOO_qmdm6oQGzxB--WJ8FQc76Wp786Lv2uqi2YxSvdaWVLaPD-D88xnwRVaMRW-iqAKa8rhWNrsfE_yAJxuttdTDCZHEMHyZHn4n1odY43w7CBzyMmqSthhmMRkb7i1s0WR6iMJa5FXH_riSMSkK0RCTXGCHXvP4t3gYTSY474nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت اومده همه بازی های کنسولای قدیمی رو یجا جمع کرده واسه بازی آنلاین، از آتاری بگیر تا سگا و نینتندو و میکرو..
Site 1:
retrogames.onl
‎
Site 2:
retrogames.cc
@Linuxor
~ fireabusefyan</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/3988" target="_blank">📅 14:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3987">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده
اول باید چک کنی آب وصله بعد کارتو بکنی وگرنه ممکنه گیر کنی
✍️
ادوارد وانیلی</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/3987" target="_blank">📅 13:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3986">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gobjThbazPehRzCTzRWD85LyigKaEpy-AyGi-I2PajJq2Rgfk3PSqZwmx1utJE-UdELXpfS35IUqWopw39hn0YQOM-cEuuXOidvO6vWuSrUifHsDph-ShMWiaA3-7e6eS37m9_nOy5SWbX1-cnRPROEM6yFtqTHSobsXQuBePMlZ_R_jrDTn5TdY5epUVqAQB9R1vq5sGR8QGCOwkmEOGUfFaHeBfm_yq1ui8O3i892MBt2mz2zW00d2USnofJqlWIIp67XDCaRJvwGmrdptKdiVKs0MpKg8nY-WqjvpWtdWSUGWXtpZUk47mytvHtqeEQ986iElen_eYUU6atHmGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر می‌خواید که توی توییتر یا جای دیگه، ننویسه عکستون توسط هوش مصنوعی ساخته شده(نمیدونم چرا برای خودم رو مخه) می‌تونید یک بار اون عکس رو توی save message تلگرامتون بفرستید، سیوش کنید مجددا که متادیتا پاک بشه و اونوقت اگه پستش کنید اینو نمی‌نویسه</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/3986" target="_blank">📅 11:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3985">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CcSkV9xCBQcgScyFEzDWxCSs4qw1Awr3-NPksnY6ywe-4alxB8T1HvFya0Orh8bKdaLZadccphH-N1mVcWNQQdQlyoOopm7LrBCdqInhOm9UNDNZm_ndCsYHy9-08mvAMO8l9b4dQPsTFjcrN61DJmn3mA7oX84PYyNNrUfXEc518lzNKcuewNpRvUxblXcB_KwEBPrcRWC7PQalFJq9iGCU8aLi_Zb_K9sSjaChaX1nQf_k3dSVBn44-zUGcpYojh5K_1LhIHvHzZkZAO1Eawdo-yIej07k2_EyVuCsbXFZzRoX7ZKmUwFQ3x4ips-N6Hhx4_OG6syb4jTprQvkyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیستم بانکداری و کریپتو رسما تبدیل به طویله شده</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3985" target="_blank">📅 17:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3984">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/3984" target="_blank">📅 17:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3983">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/3983" target="_blank">📅 17:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3982">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Iwana Proxy_1.0.apk</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/3982" target="_blank">📅 15:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3981">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIwana?</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Iwana Proxy_1.0.apk</div>
  <div class="tg-doc-extra">21.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔰
Iwana Proxy v1.0.0
با این اپلیکیشن میتونید به سریعترین پروکسی مناسب اینترنتتون متصل بشید
✅
آدرس گیت هاب پروژه↓ (اگر استارز بزنید و بازخورد بدین اونجا ممنون میشم :))
https://github.com/Iwanian/Iwana-Proxy
مثل همهٔ اپ ها نصب میشه، ولی خب
آموزش نصب ایوانا پروکسی
@I_w_a_n_a</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/3981" target="_blank">📅 15:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3977">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">با تشکر همه‌ی بچه‌هایی که PR زدن و مشارکت کردن توی پروژه تا به الآن</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/3977" target="_blank">📅 15:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3975">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bx0lmCxGW5MNs1PCBKQrzwplZW55A9ykgpJUZagOWjOcldnRJ_BjZTsglLZgTmsagQug7WtOc30P16c9YasCfegnZS4tGMuHZbBYW0aKEd5TqvIDMVAPBsM8qGiRgnNNHxJXv3A4pHAzfWI4866GV1khvjnYaGsko_ePbjwGdNcM2K3SulV9JDr6Fs1Sf_GoYTuOzOXQzqgPRSHtZ63VZcivAMpJFAAb0PZtcVLw6hZvilTrDSiPeMHpeZiWaQdHqJJbjh5wYV22dXpcJnCNmXYgh8JHpwllcnj5j7du12vK40_UE4cDeZ2BIfjZPQxhENHYpBwYGlKzy_tYerUPVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qUbmD4hQvetWUO05D3zsInQWgIJRtQ4DvSPNAjFiu83OvaFhGXdtXC6PgLNz6yiAabxz-Yh77Q8kvr9gAcJQms0iPWnSloS_z3DhGkij2F6gcdt_ab3e9iIqygGx-65qnXPah8bKpH-17Nt_KBP38dQSCAGNQDN0PRizwicStq_g4G3wEAhrbVhJDRP7xswBy2p1QAlB8W2lcswcyifatg-XpwGm93LhPxx8lvVmzJZ1vz6kEYuDZKXDywmiojqMiSVGMsE8XYbMX1usxa_85nPJ4yTk-BmwEppMOMeGnQ6EwdBfIks1HtUYUe22e3ly_yqlg_9Sj7PCVOhiAr0bIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متوجه شدم که SenPaiScanner تا الان بیش از 60 هزار بار دانلود شده
سایتش رو هم
Samim
معرفی کرد. می‌تونید آمار هر پروژه‌ای که خواستید رو چک کنید:
https://github-release-stats.ghostbyte.dev/</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/3975" target="_blank">📅 15:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3974">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/3974" target="_blank">📅 14:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3973">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بانک‌های ملت و کشاورزی هم Came to the party</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3973" target="_blank">📅 13:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3972">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/3972" target="_blank">📅 11:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3970">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GrJEUvJshKwJcKP4VB5GP-FTwjxphZ2joQPubT53yZtR8pBj--rQt8ySq7F-Vgw8P-QDGh5cJwCTO33_vPhAtquyXTbtQhM422NrE4i2eHxPnJ68G4nhNj6QbSZCcSW2WDuonWzDXR-cKT8saF36QvFYi52lZS31pG3wgy3T7WVVvWBYWVCyC5JCxqk_jaaFggw2-xRMEpqPrMJYEv0-dqW4lg8yd7Hk_fEyNC2DEPD9k_2sZ_I-vIjRcoGDjN3PzMW-kQ4iEb0nSAmXw1l_Ghr0o6tTZMmxYeaN4YTxk9d3sW-jLSxHDycnBm8CavclMaYzqDeqMsyLzOLh0anggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/um6xV0nLDsxI0DY9uNzx2rTEmZ4GOor309g9bkpQQNnIpAPs90HZZLslyEPz_qcbMcS5IwbcSg0PVp4Vaq3xklyXmIDs68fwLSf_L6j-vmTsbrj8jLI0fJ4nEewo6RbYaVp7vAwc2I-_r0W6NUvenuBPCUUcoNy49hFyXCNHRzui1QDaz4pIclF6SqYt09HWDqtA3F4u2OVoMeSh2BxsmitwPu2v_gm7rIpN9-2p7wBEZfLNNb0tYfrz4bi_2tJc4m9NvakPWKmgyuNHYfJ_srStnJDUyWxHjYFEOEu6FtWCB_EobjvAMhlqTs5LcBXVSPW7P0kuu8cleBHCEDW4EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس اول: یه سیستم که تقریبا همه‌ی گیم‌های پی سی رو بالا میاره با بهترین کیفیت(عکس از
glock saint
)
عکس دوم: لپ تاپ tuf a16 ایسوس که اون هم خیلی از گیم‌ها رو بالا میاره به راحتی.
و طبیعتا با لپ تاپ شما هزارتا کار دیگه می‌تونی بکنی که با Steam OS نمی‌تونی</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3970" target="_blank">📅 21:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3968">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OFswHtIRnuiTWZjnZLL5eMuu97gMyd7MlhEcbMKakF-IXOc4blOGz6yc1p-IVW4r47WHA6QSY7nvNVYluRzoEgaGcfskEH13wzsBHfobhKOQXbAYdAmuEBcplqipv6qHN-NIXs6GL4L4eyWgtCGzkDUTenBYu-DKmrHXLjkw-TmoJKg7_A3KipGwURMPNxOF4Uukg4zQ6w2CKGqL68BAap9FltSgVCJx1yjq5IHKntyxXmO11M1r3yXTXRcqDj4MWgs3iiOVwowi0ksnw76jFUqQwHxNjzsQTqFeyhMhnU3QetrPArtJDxIj-ASnA4KS1RzJ8oHdwckVXp2I52t1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sfYwGMuqxca64eb-Dy3AE2BOuvV_1AQkppqG-WvbKIKdD3jTV7iemzQGFyzy6LxIE5Svxu0I5jxtIUou7znYdF791L275vTbXTaagNuxxcVVpprIqQ7Hx5pfi9Psa-kqKGVX8E9kBv_N8nr-OVmUGcbQodoEJuSZfKTIKvh--q1DvS16kQjrovNfM-szOL9k9iKdbdmIHbG8aF60IO2RqhjtY9cgBXYsKhgwDq7i0ktkVJt32r3f-VG4Sf5NiYR0BdXkwMIaH93Ee1lGmQnxWjqGskB_-bFkiqMgObctd0NR13Cu5wmGfKAHfbaXcEUv5dENDbi9vw59M4mj3vQnjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کنسول استیم ماشین معرفی شد، با قیمت پایه ۱۰۰۰ دلار!! تازه دسته هم نداره باید جداگونه حدود ۱۰۰ دلار واسش پول بدین
🤣
تازه پلی‌استیشن ۵ پرو با اون همه دبدبه و کبکبه قیمتش ۹۰۰ دلاره
نسخه معمولی ۵۰۰-۶۰۰ دلار
خب خارجیا می‌تونن با هزار دلار سیستم اولترا خفن ببندن؛ حتی می‌تونن یه لپ تاپ tuf a16 ایسوس بخرن.
چیزی که دیدم، کاربرا هم توی ردیت به شدت ناراضی بودن و انتظار قیمت زیر ۷۰۰(با دسته) داشتن.
میگن که به خاطر قیمت رم و... هست که انقدر گرون عرضه کردن، اما هنوز هم در عجبم از قیمتش</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/3968" target="_blank">📅 21:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3967">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یه سری آموزش راجب ایجنت‌های کدنویسی قرار بود داشته باشیم به زودی، منتها لپ تاپ لولاش شکست و دادم تعمیر کنن
😳
رسید دستم ضبط می‌کنم</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/3967" target="_blank">📅 17:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3966">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from᯽マティ️️ン先輩</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=btRMmRTf-ncqJOHgfVSCJvShMU3rE5mv7KEj7Ypv5pGHc-RYVZNwFptMphHd5sHQVwtRiVvPFXdJ30syQHzew3SlF_SmKTqK9KceEGkJtdFa60NVku0OtvnPzRL1hDCv1Kb0qLzcL9nr35LWpxbCgsUBOfavom-KtxxVfK-N-B70x41Go2U07rapFXQl17UvJvFuPRjk6Oj1ahoyWDU7kCB8THdU-Q9-nELAc-a8RkRvw6xWbz8QrDcoyQDwMJ0EvKbSRQUdE2ZK_64i_VKXPuLuV_9ZOzZ9RBiqsnLmz2I43jUjjQelM3uzsSx-Dxy4cpEk2A4A6TUQv_ADa1ExCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=btRMmRTf-ncqJOHgfVSCJvShMU3rE5mv7KEj7Ypv5pGHc-RYVZNwFptMphHd5sHQVwtRiVvPFXdJ30syQHzew3SlF_SmKTqK9KceEGkJtdFa60NVku0OtvnPzRL1hDCv1Kb0qLzcL9nr35LWpxbCgsUBOfavom-KtxxVfK-N-B70x41Go2U07rapFXQl17UvJvFuPRjk6Oj1ahoyWDU7kCB8THdU-Q9-nELAc-a8RkRvw6xWbz8QrDcoyQDwMJ0EvKbSRQUdE2ZK_64i_VKXPuLuV_9ZOzZ9RBiqsnLmz2I43jUjjQelM3uzsSx-Dxy4cpEk2A4A6TUQv_ADa1ExCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر سعی کرد عملکرد و هزینه‌ی GLM 5.2 Vs. Opus 4.8 رو مقایسه کنه. و با هر دوشون با یه پرامپت یکسان، توی یه فایل Html، یه بازی Backrooms بسازه.
نتیجه‌اش جالب بود. این هم پرامپتیه که استفاده کرده:
Act as a senior game developer. Build a technically impressive Backrooms horror game in a single self-contained HTML file. Embed all CSS and JavaScript, no external libraries. Raycaster (DDA) with textured walls plus floor/ceiling casting, 480x270 internal buffer upscaled with image-rendering: pixelated, infinite 16x16 chunks from value-noise/fBm with a guaranteed open street grid, procedural textures. WASD + mouse look, F flashlight, Esc releases pointer lock. Dynamic fluorescent lighting ON by default (never hard to see), warm yellow fog, vignette/grain/subtle VHS, Web Audio hum + fluorescent whine + footsteps. Psychological horror, dread over jumpscares: footsteps behind you that stop when you turn, lights that flicker then settle, a far silhouette that vanishes, rare spatial anomalies, randomized timers with cooldowns, slow escalation. Save position to localStorage. Return only the complete HTML.
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3966" target="_blank">📅 08:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3965">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">امیدوارم جای بهتری باشی الان...</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3965" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3964">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام به همه همراهان عزیز،
متاسفانه یکی از اولین اعضای خوب خانواده WhiteDNS که از روزهای اول قطعی اینترنت خالصانه در کنار ما بود، به علت بیماری سرطان از میان ما رفت.
از طرف تیم WhiteDNS، این اتفاق دردناک رو به خانواده، دوستان و همه کسانی که دوستش داشتند تسلیت می‌گیم و آرزوی صبر و شکیبایی داریم.
یاد و خاطره‌اش همیشه در قلب ما می‌مونه.
🖤</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/3964" target="_blank">📅 16:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3963">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:  https://yout…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3963" target="_blank">📅 20:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3962">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:
https://youtu.be/CPrePbvbbic</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3962" target="_blank">📅 20:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3961">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W44r76YpkY_e3qMji3b9QVqxXc_Sk6G0Qe3AtS28oIAzwtFpn1uYQ72Fwv3-zxHyMdpfA6az18ijukwApYaMgQ45LmJYYnEAH3yKQtEDi19e79rRYGSSEd1gFEUNXEIaC4UNmiw3DDnI0ij5UKi2n61vb2bqQQRHVdhuw2KBJDyjCsuwIJWbkcGAC9r6TIoCVwRzZmP4bjFNmSWrx8K2Ge7PJvzbpyJsxhtuUQcyC5eutAVaA415SApJs2W_rY97kNh_ztkcb-VHLzyLncdkSJTgA_CV4LFpQvkvYpxrA6QFvR8wImSQf9zBWISdH9B82KK-0APhmg7UssTX1i_-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✅
نسخه‌ ۲.۲.۱ BPB Wizard منتشر شد.
۱. قابلیت اضافه کردن چند اکانت کلادفلر به Wizard اضافه شد. این قابلیت برای بچه‌هایی که اهدا میکنن و تعداد زیادی اکانت دارن خیلی کاربردیه.
۲. اسکریپت نصب خودکار برای macOS هم از این به بعد قابل استفاده هست.
✍️
بیا پایین بچه
آموزش استفاده از ویزارد رو قبلا ضبط کردم:
https://youtu.be/uCRKnrQEQYU</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/MatinSenPaii/3961" target="_blank">📅 14:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3960">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا...
پروژه نهان که قبلا متین معرفی کرد رو محصول داداشم دکی واسه دسترسی رایگان به اینترنت آزاد با روش ورکر رو بلدید دیگه؟
حالا میشه آسون تر حتی واسه کسایی که مبتدی و هیچ ایده ای ندارن هم ساخت با کمک ربات:
@itsyebekhebot
شما وارد ربات میشید ساخت پنل نهان رو میزنید وارد سایت کلودفلر میشید و طبق راهنمای کامل پیش میرید و ظرف دودقیقه حتی کمتر با کمترین اطلاع و دانش از ورکر یا هر چیز سخت دیگه ای فیلترشکن رایگان خودتون رو بسازید به صورت رایگان
❗️
نکته:از بات ایمیل فیک هم داخل کلودفلر میتونید استفاده کنید:
@TempMail_org_bot
هر جا هم گیر کردید بهتره که به من پیم بدید
😆
آموزش ساخت پنل نهان
@yebekhe
👑
@xsparvin
🍷
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/3960" target="_blank">📅 12:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3959">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">اگه میخواین بدون VPN، به سایت
x.com
(یا توییتر سابق) دسترسی پیدا کنید، کافیه این گام‌ها رو طی کنید:
1️⃣
وارد این مسیر بشید:
C:\\Windows\\System32\\drivers\\etc
2️⃣
فایل
hosts
رو با Notepad باز کنید
3️⃣
انتهای فایل، این خطوط رو اضافه کنید:
104.19.229.21 abs.twimg.com
104.19.229.21 x.com
104.19.229.21 ads-api.x.com
104.19.229.21 pbs.twimg.com
104.19.229.21 api.x.com
میتونید بجای استفاده از 104.19.229.21، هر IP مربوط به cloudflare که تمیز هست، استفاده کنید
4️⃣
فایل رو ذخیره کنید
5️⃣
مرورگرهاتون رو ببندید و دوباره باز کنید و
x.com
رو جستجو کنید (بسته شرایط اینترنت‌تون، ممکنه مجبور بشید که چند بار صفحه رو reload کنید
⚠️
توجه داشته باشید که در این روش، ممکنه
x.com
(یا توییتر سابق)، شما رو با IP خودتون شناسایی کنه، چون که شما بدون سرور واسطه ممکنه متصل بشید (به
این دلیل
از کلمه‌ی "ممکنه" استفاده کردم).</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3959" target="_blank">📅 10:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3958">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وقتی اینترنت گوشی رو Share کرده بودم برای لپ تاپ، بدون VPN، بهم آپلود 0.02 مگابیت میداد. اما همین رو وقتی با کابل و PdaNet+ اینترنتش رو share کردم، سرعتش شد 2 مگابیت. یعنی صد برابر
امتحان کنید شما هم، شاید همین اتفاق واستون افتاده باشه</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/3958" target="_blank">📅 09:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3957">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CNwn-bRt6LmeOYF9U33gs-R6kPsnm9Ol3fTdg3qr4t6CeuMCenGN_GUycLFG96ryka3b9U-fxL_2aR7qEZhZKX10KKs-FSQPcM0MnusJ7LVppNU2v3a1HnjcqkotUq2fV0dt7w7NFtMMwd4G4Sik2JgefnDDetriljtQG-ae22UEqQb6nKgAJZ_JW42EOiTIvl_9u1aE_dvs2O1EkkVSikFpxhTSvlQYPjLRo6BU2ZDQVoN6OfO-q3omqBkGIqX9DNP9QKwRncNNK3rK_YZqrBi4YeLqroLyd0p3GBLCqg8eLU5ISTXLATNNSl-rNEEwDXqdJvPttYY6EUrcwOdvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل در حال آماده‌سازی یک «ارتقای مغزی» بزرگ برای هوش مصنوعی خود است.
تصور کنید یک کارمند بسیار باهوش دارید که گاهی در کارهای طولانی «تنبلی» می‌کند یا برخی جزئیات تصویری را خوب نمی‌بیند؛ حالا نسخه 3.5 قرار است مثل یک متخصص ارشد عمل کند که نه تنها چشمان تیزبینی دارد (درک بصری قوی)، بلکه می‌تواند مستقیماً نقشه‌های مهندسی و کدهای ظاهری وب‌سایت (SVG) را طراحی کند. این ابزار برای کسانی که می‌خواهند از یک ایده خام به یک محصول دیجیتال واقعی برسند، حیاتی است. اهمیت آن در این است که فاصله بین «فکر کردن» و «ساختن» را به حداقل می‌رساند، هرچند که احتمالاً برای این هوشِ برتر، باید هزینه بیشتری بپردازید و با قوانین سخت‌گیرانه‌تری (فیلترهای امنیتی) کنار بیایید.
نشانه‌های فنی در زیرساخت‌های گوگل تایید می‌کند که Gemini 3.5 Pro در یک قدمی عرضه جهانی قرار دارد.
این مدل که به عنوان پاسخی به نیاز بازار برای «هوش عملیاتی» شناخته می‌شود، بر سه محور اصلی متمرکز است:
تقویت بینایی ماشین
استدلال چندوجهی (درک همزمان متن، تصویر و صوت)
جهش در تولید کدهای گرافیکی مانند SVG (فرمت برداری برای طراحی وب)
گوگل در این نسخه، «دقت جراحی» را جایگزین «تنبلی مدل» (تمایل هوش مصنوعی به کوتاه کردن پاسخ‌ها در وظایف طولانی) کرده است.
با این حال، این پیشرفت بدون هزینه نیست؛ گزارش‌ها حاکی از آن است که کاربران با یک «قیمت گزاف» روبرو خواهند شد که این ابزار را از دسترس عموم به سمت بخش‌های تخصصی سوق می‌دهد.
همچنین، اعمال فیلترهای محتوایی شدیدتر، نشان‌دهنده هراس گوگل از سوءاستفاده‌های احتمالی است. در واقع، گوگل در حال بومی‌سازی مفهوم «شاگرد اولِ سخت‌گیر» در دنیای سیلیکون است؛ مدلی که همه چیز را می‌بیند و می‌سازد، اما تنها در چارچوبی که معمارانش تعیین کرده‌اند و با هزینه‌ای که هر کسی توان پرداختش را ندارد.
✍️
Gratomic AI Bot</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/3957" target="_blank">📅 08:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3956">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کافیه یه آیپی تمیز بذارید توی بخش Advanced, ip fronting
زیر ۲ ثانیه کانکت میشه</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3956" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3955">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/3955" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3950">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3950" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3950" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3949">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJWhru6sLM9XfgyQFiWRGZMvDbjhkkohQPhRc4XYM2DRYkibjtoudghVGwRydIvW4rMnqO4HdRJ_dtKGjJoI5CHFGPGeSu52bbFENzpbxEh58R5QzWSUXF9VAmr4HG3BDGUtZTB4W5I8trqOBLEQMp9VZ8QHV8H9tE2Z9z5XrYyDHgijE2h2i4JtpOk5ctKYndiAk022b3yjtrD9rkL5G6oLtmZUDvmuF1PZXq7K9MUTKFGQIjmjhzoQaLvzYmk5UiaWbXgAI-ZpMlSmmKkUkE3W4LeTdczBWbAfsCCv4j8piS_a2DAic1OoRgAozbI4sYnEmKNiehqyGRdNLhes5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه
• ظاهر اپلیکیشن تغییر کرده
• امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.
• پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.
• با کمک یکی از بچه های گروه، یکسری از مشکلات امنیتی اپلیکین رفع شده.
💬
اگر براتون وصل نمیشه، فقط و فقط مشکل از شبکه شما هستش. آی پی تمیز پیدا کنید و داخل فیلد IP Fronting قرار بدید و براتون کار میوفته.
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/3949" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3948">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/3948" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3947">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q1qQd7f_8LXsdTkklkMJYTYdBnjRQy10uaBeYgW8_nSkAIbw7P5fpTLfE5m1DwSTjKQHD7eFIJoYyYDjy3zMoT8opMPIPATajU6bLH_YRbcRr4sRelIDIUAlcwJ0U6R_lSgRwzI_GiyyJpFBND3efjtvv64RD4cdmrX9di6Qkk_MSj1QAOQS04GScfufvPS1zQPXgFXtj8-pcB4rA_ouKw9w722zMXbuSfKUxYzJE-3wHzY3kERApM2pXav0dG7jM6SUUrMQ2p_cfOv5McXQ6jrrHp4vrrtJdMcI4RctUaStmstjN8rWCpvT0m4n-hm4suYqXYFB8qUr-qeSLRgW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از contributerهای پروژه‌ی senpaiscanner، دوست عزیزمون hidden-node، نسخه‌ی اندروید اسکنر رو توسعه دادن. طرز کارکردش دقیقا شبیه به اسکنر دسکتاپه. نصب کنید و یه تست بکنید
👇</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3947" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3946">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">✍️
دوستان برای جلوگیری از هرگونه سردرگمی، ما در حال حاضر سه اپلیکیشن مختلف داریم:
🛡
۱. WhiteDNS Application
این اپلیکیشن بر پایه‌ی MasterDNS ساخته شده و مخصوص زمان‌هایی است که فیلترینگ و اختلالات اینترنت خیلی شدید می‌شود.
در شرایط عادی فعلاً کاربرد خاصی برای استفاده روزمره ندارد.
🛡
۲. WhiteDNS VPN
این یک اپلیکیشن ساده‌ی VPN برای کاربران اندروید است.
اگر فقط می‌خواهید راحت وصل شوید، این گزینه برای شماست.
🛡
۳. WhiteDNS BPB
این اپلیکیشن برای ساخت و راه‌اندازی BPB روی گوشی اندروید است.
یعنی بیشتر برای کسانی است که می‌خواهند خودشان یک پنل BPB بسازند و مدیریت کنند.
🛡
۴. WhiteDNS Installer Bot
آیدی بات:
@WhiteDNS_installer_bot
در این بات می‌توانید کارهای زیر را انجام دهید:
• نصب MasterDNS Server
• دریافت لیست IPهای سفید Cloudflare
• دریافت کانفیگ رایگان VLESS
• تبدیل کانفیگ‌های خودتان به کانفیگ‌هایی که پشت IPهای سفید Cloudflare قرار می‌گیرند
🛡
۵. WhiteDNS Installer Wizard
لینک گیت‌هاب:
https://github.com/iampedii/WhiteDNS-Wizard
این ابزار برای کانفیگ خودکار سرور شخصی شما استفاده می‌شود.
با استفاده از آن می‌توانید سرور خودتان را همراه با پنل شخصی 3X-UI راه‌اندازی و تنظیم کنید.
❤️
یک نکته مهم:
اینکه اسم برند ما WhiteDNS است، به این معنی نیست که همه‌ی سرویس‌ها و اپلیکیشن‌هایی که می‌سازیم حتماً بر پایه DNS هستند.
ما از اسم WhiteDNS به عنوان نام برند استفاده می‌کنیم، اما راهکارهایی که ارائه می‌دهیم می‌توانند VPN، BPB، MasterDNS یا تکنولوژی‌های دیگر باشند.
@WhiteDNS
🌎</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/3946" target="_blank">📅 12:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3944">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hb4QGN4QtQ3R0UHp2bK9p83fL1bvEqtrsf7GONo6_6vSeVpZjMxc6_9TGdYAXZHvdVd8qXmNb-0IKqTi03VrMZWfayaSariRYg4AIIVZTJj8gRF6Jd5LVUpXf65oRoc8uJmZBOt83fjYjl4-0iY0NQVdhAQnMC2AETysvn9pAPfy1QP9_Yq-jVc-ZnzsgluOTr_awR2hdM80nbR9woOgdiOeuZb8D-HUc7toj3x8PuGEM9i8wuC1FKbEHdTWBAzutDdFo0qf9SscMr_e2p-9F10c44G9kiTDvxqaqZZPnfptuPQikkeBSVbsiSWQGMjLLL_dxQBzriC6IIG-ebXTZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IHHVkchEbyMRi7vuqZIBXkE_t5_KQE4SWFXKDSZTG6rZWbXafF_MXCP2twNMxlZBZBp0Kt8AC00fwGv8mly7yAbm1UcQGhyJ7JZ0dRZ5EE3liEOY5N8fiUxUiExXHXQFcnMew0igWmUA9QdcuhieYE49gR0lQnZ4wWdPtZgs8rJZSv3Wa1ryEMGEgQARVJZgffLJA7eR1axWXRmU3wgn3ZBlAPGwJS9uOyLNZLV3WCtrNtON1K0X05KWxIjtAjWcGsu2w8jvhz8X6BRuw_Hxthay3YZi8b55xXXUkvX7m5qPQa-3dMYP9kdp8GiihoKUL3xk_l4GlE2VDITn917sxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از بچه‌ها اینو واسم فرستاد و گفت گویا V2box، به صورت آزمایشی SNI-Spoof آورده. یه تست بکنید ببینم داستان چیه:)</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3944" target="_blank">📅 00:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3943">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز
❤️
در چند روز گذشته متوجه شدیم که بعضی افراد و کانال‌ها، به جای همکاری و ساختن، مسیر تخریب و سوءاستفاده را انتخاب کرده‌اند.
این افراد که ظاهراً در فضای اینترنت آزاد و کانال‌های مشابه فعالیت می‌کنند، برای جذب مخاطب بیشتر حاضرند هر کاری انجام دهند؛ حتی اگر نتیجه‌ی کارشان آسیب‌زدن به پروژه‌هایی باشد که با زحمت و هدف کمک به کاربران ساخته شده‌اند.
چند روز پیش اپلیکیشن WhiteDNS VPN را معرفی کردیم؛ اپلیکیشنی که هدفش این است کاربران بدون نیاز به تنظیمات پیچیده، فقط با زدن یک دکمه به بهترین کانفیگ‌های آماده و تست‌شده‌ی ما وصل شوند.
اما متأسفانه برخی کانال‌ها شروع کرده‌اند به استخراج کانفیگ‌های داخل اپلیکیشن و انتشار آن‌ها خارج از برنامه.
دوست عزیز، اگر مسئله فقط بستن مسیر دسترسی شما بود، ما ده‌ها راه برای رمزنگاری، تغییر مدل درخواست‌ها و محدود کردن این رفتارها بلد بودیم. اما شرایط اینترنت آزاد و محدودیت‌هایی که کاربران با آن درگیرند باعث شده ما تا حد ممکن ساده، باز و قابل استفاده طراحی کنیم.
مشکل اینجاست که همین رفتارهای مخرب در گذشته به پروژه‌های خوب و ارزشمندی مثل Slipnet ضربه زد. وقتی هر ابزار مفیدی به جای حمایت، هدف استخراج، کپی و سوءاستفاده قرار بگیرد، در نهایت انگیزه و امکان ادامه دادن از بین می‌رود.
واقعاً هدف چیست؟ آن کانفیگی که با زحمت استخراج می‌کنید، همان چیزی است که بخش زیادی از آن در لینک‌های ساب ما هم وجود دارد. چیزی که روزانه هزاران نفر را متصل نگه می‌دارد فقط یک لیست کانفیگ نیست؛ پشت آن اسکنرها، تست سرعت، بررسی مداوم، فیلتر کردن کانفیگ‌های خراب و یک سیستم کامل قرار دارد.
ما این ابزارها را در مدت کوتاهی، با انرژی و فشار زیاد ساختیم تا به کاربران کمک کنیم. لطفاً به جای تخریب، کپی‌برداری و گرفتن انگیزه‌ی تیم، سازنده باشید.
ما از نقد، همکاری و حتی پیشنهادهای جدی استقبال می‌کنیم؛ اما سوءاستفاده از ابزارهایی که برای کمک عمومی ساخته شده‌اند، نه کمکی به اینترنت آزاد می‌کند و نه به کاربران.
اجازه بدهید این مسیر ادامه پیدا کند.
✍️
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/3943" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3942">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این پست سگاروی عزیز رو بخونید، و اگر دوست داشتید همکاری کنید:
https://t.me/AiSegaro/120</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3942" target="_blank">📅 18:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3941">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">تیم داشته باشم، دوست دارم از خودِ شما کمک بگیرم. اگر دانشجو یا دانش‌آموز هستید و مهارت ترجمه دارید، این می‌تواند یک
کار نیمه‌وقت منعطف
برای شما باشد تا در ازای کمک به ترجمه و ادیت، درآمد کسب کنید. آیا این مدل همکاری برایتان جذاب است؟
هدف من این است:
سریع‌تر به محتوای آموزشی مورد نظرتان برسید.
هزینه‌ها برای هر نفر ناچیز باشد (پول یک قهوه!).
بالاترین کیفیتِ ممکن (ترجمه انسانی) را تحویل بگیرید.
یک زنجیره همکاری برای دوستانی که دنبال کار نیمه‌وقت هستند ایجاد کنیم.
هر پیشنهادی در مورد نحوه قیمت‌گذاری، فرمت‌ها و اجرای بهتر دارید، در کامنت‌ها بنویسید.
من تک‌تک نظرات شما را می‌خوانم تا بهترین مدل را برای شروع استارت بزنیم.
این فرصتی است که با هم یک کتابخانه آموزشیِ قدرتمند بسازیم!</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3941" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3940">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxsmvqTs-OaBJXUlGnngWIOBFRQxlJ7538EF_E1HpyOqGHsTqBrNz5TRvsCw_yrxTkoGzZhQwMUaVnLiIC5BU4uFVeP2ybfJZfbrDtOFOwyLa1ZvhGY-HvTmYe1tftVRcoSONlyQufdQoTvwsyLf-4e61o5rf_gia1doVwJxjCuRDtXpUGX6-m-BJSVpY0zmBbJJeMK9mgZzouFVuh9ocRv1GvULk7gKQX6JMl3riNaNDuhIYkrhQHx1ZjQqaBQA5K3YCDZqFFhNX8jvnJi4GOxKK9GBbAkbeYdbtSGXMf3F3WirJdHNEpVe1Ohnzwu4ARp3vPvEEoTy11U_pJ7eZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همگی، یک پیشنهاد ویژه برای دسترسی بهتر به محتوای آموزشی!
همان‌طور که می‌دانید، درخواست برای ترجمه و زیرنویس کردن ویدیوهای یوتیوب، یودمی و کورسرا زیاد است. از آنجایی که کیفیت و دقت برای من خط قرمز است، فرآیند آماده‌سازی ویدیوها (ساخت زیرنویس، ترجمه دقیق و ادیت) بسیار زمان‌بر است.
برای حل این چالش، قصد دارم یک
«کانال مستقل»
برای مدیریت درخواست‌های شما راه‌اندازی کنم تا با مدل
«مشارکت جمعی» (Crowdfunding)
، ویدیوها را به صورت عمومی و با کیفیت بالا آماده کنیم. در این مدل، به جای اینکه یک نفر هزینه کامل را بدهد، با مشارکت چند نفر، ویدیو برای همه آزاد می‌شود.
اما قبل از شروع، می‌خواهم «شما» تصمیم‌گیرنده باشید.
برای اینکه این سیستم عادلانه و دقیق باشد، دوست دارم در مورد جزئیات زیر در کامنت‌ها با هم صحبت کنیم:
مدل هزینه‌کرد:
به نظرتان چه مبلغی برای «مشارکت جمعی» منطقی است؟ (پیشنهاد شما برای ویدیوهای زیر یک ساعت و بالای یک ساعت چیست؟)
فرمت خروجی:
ترجیح می‌دهید فایل زیرنویس (SRT) را جداگانه دریافت کنید یا ویدیویِ چسبیده شده (Hardsub) که آماده پخش است؟
یک فرصت برای شما:
اگر تعداد درخواست‌ها زیاد شود و نیاز به</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/3940" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3939">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LYkPO31Dl-Da7NDACGYxjyvWEw-pR6CtzRTqQXSLEoY6fVXdwIJinNIX-RaoBX8osXGsjYFUchef92Zb9b3fgGsXhCSJgdn2v0iJauWHUXQtzWol7Wsn6_matjjoBqr2RYn62hCGmza4N0ekhY3xk9YQWrSg-I1CJ0RJTZgMyez8Fvsy0KEBkpIneI97NwS6J2556pxZMI7N6o6V-vuHkertfj3nMc1hp5OpWlIBquHJPk5VMjI_IuCCzxN9l9G1P1lnWcXev9h-htfN_fQxq0_2_YGFWMVZ9nsUtS6iKQQxR7hSqxkZZaNW0yIqRp6FKnxWUYqWlhgZhT931aj3ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی از دوستان این مشکل رو داشتن که تلگرام واسشون باز می‌شد، هیچی دیگه باز نمی‌شد. یا یوتوب و ... باز نمی‌شد   مشکل احتمالا از کلاینتتونه و dns اش. باید تشریف ببرید توی تنظیمات v2rayng و Domestic DNSرو از چیزی که هست، به 9.9.9.9 و یا 9.9.9.12 تغییر بدید. همینطور…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/3939" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3938">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uek92Bbpt2lDJT4TjJPMmggojwTh2aOqvqGqn-Neh3x7HMK9eObHSkxLxBkDDFctdZlKrbvL8qxSUqozNaJfieMTYQbswW3dXYioZxGyw1XDYSUezNfVYnGdT9OOzvAZUDg6ECJxrEU2XQj4rIo09B36wpGc2GfRQAovPKMp8D6_eBGyhz9_FgMNaL7bgsyeWt4MXPXdx2w1J73gEGAhy-5tg_WKByYS0i4dRuw3OKY5yAuRBJJEmU4VWdcEgSJQ00KFWRRZuGTb1MMDs3Ze6WZQyvqE8448XSzU9txe6sIUYNby4sor5RIT908coWN6eMBSlb2Grui-n5TFFWCahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
بدون دانش برنامه‌نویسی و کاملا رایگان، اپلیکیشن اندروید بساز! (فعلا اپلیکیشن ساده
😁
)
⚡️
لینک‌های استفاده شده توی ویدئو:
1- خود AiStudio گوگل:
https://aistudio.google.com
2- پرامپت ساز ریک:
https://chatgpt.com/g/g-6a319e2a22648191836468df375a3763-prmpt-sz-ndrwyd
⭐️
توی این ویدئو:
1- بهتون نشون میدم که چطوری می‌تونید از یه پرامپت ساده، یه اپلیکیشن ساده با تم دلخواه تحویل بگیرید
📲
2- توی مرورگر، Emulator اندروید بالا میاریم و با اپلیکیشنمون کار می‌کنیم
🏆
3- و در نهایت، اپلیکیشن رو مستقیم روی گوشیمون نصب می‌کنیم!
📱
🤎
اسپانسر ویدئو:
خانه EB، خیریه حمایت از کودکان مبتلا به ای‌بی و بیماران پروانه‌ای:
https://ebhome.ngo
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/3938" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3937">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ویدئوش آخرای ادیتشه
🔋
می‌ذارم تا ظهر</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3937" target="_blank">📅 10:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3934">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kTdcAzRZUBtw3uPVNpmT5wt8dj2DiOm96gVvS8wX2t9Jaqt5Rqs-a_mUniUXG9dD-ad21k03-76y0RWmStNApHU5lgaymIVNt_gUgCEEU5ys9CvFrvFHdRdueBLF-g2jctQyMOPVIm1CgjG9KKJriWG7t3zkk8hnLhbquhy_ZCKk8vPN-s1mpOecpthDDk6B7FHhkamfXq-5dNYeiHR1ECLGrhuOk4T_n5f_koLq152QAqGlzHVJ2VSLTm1b6QePSm1uoF8ZbMVhZ0O3ay8-cjNwHkWZckKuCSZGZIHBjCAvlNiuRZbnctwjkLFSuKPJu9NIlZK9_stJLR4zIeLIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DvWcNxiML1koOLRVHs3ZVqlsCEoMxCvhvTP4pqfYKqh7txvl0Y5DnjhS2ziTAAXK-fmnHFHlPJUXzD9ctUATbVOvTPOUzJueYvlAdq7J5Ijvo2ujMvBSQCRtgoWGJC82c43WFqF_hu1QbbGs1tZL3yhk1Rpv6BcWEEaSNz6-EgJ6Z7VHno7zkoqm1ucXgt_p6z9JDkfKCZjyb8Hjx_V4_P14u-B_s3eOQBFljSmoSnzxmLZWKuxEZXmtHLqlguqQjJfb9gnbu9ajDtv3xHElorMFy2Rgknk5d7VDu3rCXd64Sl8yTmcrQJ33YPY1kbavvVm5g6Lps6iVU9P5HMRQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z7bQ7hWWi1Eo_y2pQ9BRYTT3sbKqiC02lGLGvXLF4CP86OZWuWD4NpMI_SROlYh5DdUTci_FpvCAczbY1oXgBq6-QxWbIESTPHJ1u6INu5cLnZGxUgHaFW8HjWS6l3UZhIcOmXZhEevOq8tc5md0GNxlZl6xgoCk9qdaaLnU9Q29eojp8ixEq4ZngKXbWoSyKdZkQP5nEJkUjK4a_Na5oW5N0W9XJX26gZHIqt7rsh_kaR7XpTz_1xOHVS2u-GL6YU07B7h_x1iA8OX5nUmtKr51uQUJ5aLGIMu-ufEZUslrJiEbK8XQjVoHzqc4TbdCY0ic7LdR-VsGELaXZsPZHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه اپلیکیشن مسخره‌ی اندروید با AI گوگل نوشتم مجانی، توی بیست دقیقه
ویدئوش رو ضبط کردم که به شما هم یاد بدم. اصلا چیز خفنی نیست اما خب بامزست</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3934" target="_blank">📅 23:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3933">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">میگن Cursor یه چیزی ساخته که SpaceX اومده 60 میلیارد دلار خریدتش
نمی‌دونم چقدر حقیقت داره این حرف اما سرمایه‌گذاری خوبی انجام داده. به زودی CLI کدنویسی grok رو شاهد باشیم احتمالا</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/3933" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3932">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3932" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3931">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ورژن 0.0.3 خیلی بهتر شده رفقا. حدودا بعد از 20 الی 30 ثانیه وصل میشه روی همه‌ی اپراتورها و سرعتش هم عالیه
منتها می‌تونید از خود Wizard استفاده کنید و بسازید برای خودتون</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/3931" target="_blank">📅 18:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3926">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.3-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3926" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3926" target="_blank">📅 18:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3925">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3925" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3922">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W7VfGjvz7DCNDPmrbGCffuCJdM-wYfaPlp_bZIouzoZkQ-FvZOQNSroIxr9224-_j0xq3y18a78xhNHfB0rz0cwwbTBDTzFO9-W8fhEUkjMHwTWHq1od1jbH3wF5TCiwHy-NKeCeIbyWWJh4eh73g8bU16UsaOy3d3NHetNL_kHDsaUbntmoRay3E7Nzjp5xynZO9tqf3a-b6hawpIjYZckOL9uqXK6X_yG0D09qVuu5ZMGmIw0Slv6WazHWFzNvKofKsxk13-Id0dm9EEfc_kiiAA_EGcxAIJth02zrFKK9h4P8_fZtzhFeHYEs8gfotyLdcp7LLnkBePU--euJTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/huFC1Jk4c0uXuK7lCto1lDRRqj9cluEGVUt-RSSlopPbGBqHjfvCaedESoRFJyHWRmPNJ5p8Zz0pWYXOWpKrA9xMFvSsaEHV9RdjMy6TpkGn4Dhpr6gmNYhGrUahdujjCcoADwWdoG9Wz4rkPKnWG56xF1UWbuaouCm_KIiG9d0bzJ4iLPwSoUDF7rjHRBE5P1pjigJGHVeM7ATotvZkuqgYZff13MCqmndp5dPugKpA04tT4PVkwztOwsgC6WUtSrUVOWCPJcU40oW42zKaspsKSIVRFCvsXRKCEi9VyrEHabKDhVWlHJGX03inNZLZcDTwirt4-rSTNTsWarH3_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s96eiISeXYOt18Q0bQ5lI9i54GrzoVo7zixv8fswo8X-bMdhn-LK52Ws8jJG22SMwBGBocMZ8f2kIrbTs0lztdogkC994sZkZINF72NK_6dSZxtLag969cjH0VF8NnMO4aPkyk43QgVKc5G_HNdLqw3ro-WnIRRrlzoAd7I4FnKUQX2Mu2LbV909OW7dp7jzjGl9nfSxmMqIPc2N3Cu9-MBDICg2y8eJwT0bvELKp3BYrbV1omdi_z57gxscPrXlabuK8nY_XZr-84pEZsztWolhUR0YIquylvRBIq74NNxmwBwDIpmHpV9SWC87rOLvm794h1HnGrRqoS9PQ2dfZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بالاخره قابلیت ضبط صفحه نمایش به همراه دوربین سلفی، به اندروید 17 اضافه شد و دیگه نیازی نیست این کارو با نرم‌افزارهای مجزا یا تیک‌تاک و... انجام بدیم. کلی قابلیت باحال هم برای گوشی‌های تاشو اضافه شده؛ از جمله foldable gaming(که توی تصویر دوم می‌بینید) و ارتقای مولتی تسکینگ
اطلاعات کامل تغییرات:
https://blog.google/products-and-platforms/platforms/android/android-17-features/</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/3922" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3921">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برق داره دوباره نوسان میکنه
اگه سیستم داشتم به جای لپ تاپ، از صبح تا الان 15 بار خاموش شده بود
فکر کنم باز می‌خوان قطع کنن اه</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/3921" target="_blank">📅 15:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3920">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3920" target="_blank">📅 14:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3919">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vQ7jr5fOTvmdi9C8SnqtQUaBsp1hOrnLgFmOS3i7AojDKExsxgxEwXASsyQGKczJcBlGzw_-w7CBI57Ni4dEyuyFJ6b2B9yhQPVKALI4oFYnOzntQKRBhhx-LPE75v9a0W5PscIcweq9qivEwclEZzbg1hy47_EIxXkoNYUpfGA4wOUh2i2T0rib1U8YtR5bW1g9di1PtWxHDgZOWcEeGOx_z4Uxwn3UA_zCeNkMraAXsz4nn3NcAf95FAnRGCcrHpa3zEu7r3qKQFPPFHHXzlJJg8JzrJhqMm3ndg62zcVth-Y6uKd0MyO0zDHres8LgiLPBcITBTu2ov_70lvDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3919" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3918">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FtfyromWsDt1wsvR4Jcl-gX-BCLSAy8hpEB_elzOD2eAjDWHgIObhla4UCqR51AOpq3j2WZD1kHKMnQOoCEim1KoaTa9NzWjKJgUB0xxmkiM4l9n4skJ5tEf89pbdZNq65zBfomQK9SnttcvP4dMpbQ9DirLGupCgqQ_nsMEmfwvUjAT29njtV8vkF90lH0AygMDfQIXMzDilOvTzfjhShHd7COPO2nQR1FeaRmUmdMQfUtD9WJw7i4sFOTF7FfPzY6VeDuwoC0go2jd3SCl_o8CRSiylSsrMViV0xKTIUFLRwkNmDJ5eKJsL03taXdiTNRRiXWDI0PgjRJIeTawXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیدات کردم مهدی جان
🥳</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/3918" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3917">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iuNpZ81zbr5Ek83NppOkmhl3b5C3heYSWzDlgRzEr6ARYiHxPfwZMhliLMmNw7eG7uOF49S1VCGXBGR2YZatUOeWfbQSw0gcBvoRb5g9GMOd2bXQvm1Np7djQoTLFbbtSLscND6P1VQcAFBt5aXBwmck4zaEVA2C0qVhiyt9grFI7GJdN8ratyRfANnBMWnMigCaMJPNTYQsLAraLuZLaw5WwU3RhaTWpDGZC1C3HpMwt0E-mkgZkY0FwojBqx0-jKi5zwLYtefPt1MQEe1Y-Pj_85ZNC5-TQ-28VpDDkcfSMLM2RQCgb3W2Bhp4Ef7UohZtFs0otsJLkXjGdJkIJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندتا از بچه‌ها تفریحشون اینه برن وارد پنلی که من توی هر ویدئو میسازم بشن و پسووردش رو عوض کنن و برای خودشون لینک ساب بسازن استفاده کنن
😂</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3917" target="_blank">📅 13:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3916">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/3916" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3915">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MaIdTblUgZ7xypSNWcLfD_Nnv0G0FY_tDVcQ7EWle3YQvuRzdmtYbS29oSStlrl8mCfl6W5JevK-mWBQQB9OWXAkQw1-6zaXdYg9zNOn0mB5LvNC-C7X4X1dm6wq2JowMbPtlWV5xGYIApbGbPSTmj60BC38DHaew5P2io7bmJi9mZaZEJJcPcxmCGWJCmiBywCtXZP8soxS-3X_0b6lchgvXcNCSlVZyMDHjnSfrZe2yHCf-oXUvab6DNpxAPL8yL1hyCkpjDU7jBXQEtEfrS1buPHe7Uk8L-nj4RecQpBpb-uH0ATQc1mZcU-93FgZN9PDFlx4dY1KJHENxG47wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/MatinSenPaii/3915" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3913">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3913" target="_blank">📅 03:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3912">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">من که عددی نیستم والا نمیدونم وحید آنلاین و اینا چطوری هندل میکنن که آیدی خودشونم گذاشتن
😫</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3912" target="_blank">📅 01:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3911">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3911" target="_blank">📅 00:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3910">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3910" target="_blank">📅 00:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3909">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا من داخل این پست میخوام توضیح بدم این بکاپ ها و این ip به چه درد میخوره؟
ببینید قبلا یعنی تا چند روز پیش شما تو ایرانسل اسکن میزدید واسه ip اینا ۱۰۰ تا میداد برای مثال ولی الان هر  چی میزنید ۵ تا به زور بهتون میده و ip اصلی که
188.114.97.6
میشد که ملت روش وصل بودن رو بستن
❗️
یعنی ip ها کلا رفت تو دیوار کاملا خاکستری شد
اینجا (patterniha) بهش اشاره کرد:
https://t.me/patt_channel_x/68
بعد حالا همه ip ها واسه همه جواب نمیده باید ببرید پشت gpt با یه سری ip محدود برای sni spoof استفاده کنید.
جدا از اون میتونید تست کنید این لیست ip ها رو که واسه شما وایت باشن و مستقیم بتونید داخل پنل های bpb و نهان و... استفاده کنید
🫰
ip:
103.160.204.34
185.193.30.94
45.8.211.57
199.181.197.1
159.112.235.52
170.114.45.239
104.17.21.111
104.24.200.94
188.114.97.6
آموزش ساخت پنل bpb
آموزش sni spoof
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/MatinSenPaii/3909" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3908">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vl5ubumEeAP-CHhp3HOQYTiFx3_gW-fskzqxJb1ZLWi3hMJIIbWpYU3QYT94R3L6DyKHODlfpZ_foAKEh-TIaW6FGbeH7qn6ZqT9ZQLlLCy_YIQoVnu8D8ykoXecVpIlAE3m_8R5Fcoe8vWfih_kmNLF_GAJ4G094dA_Z1kbCvs2WZONWq1f_8aH0l1uifeftTyjHcqlyTiTLa1vVMf25Hmt8LeG_EAFX16uQfL48WQZj-RmnON4FtBcF6X1QCT-vxcHF_6bVo7wUFPh3-fgqyhv60GkrRTCNA5X11u9ix0t547eg4dLXDemXDJ3-RcNaE0cQ1D0gKkp7-2f8sWdqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3908" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3907">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">متشکرم از بچه‌هایی که دونیت می‌کنن. چه کسایی که استارز می‌زنید، چه کسایی که به ولت‌ها دونیت می‌کنید، همه باارزشه.
من دسترسیم به ولتم قطع شده بود و مجددا وصل شد الان، دیدم دوتا از دوستان 3 و 20 دلار بیت‌کوین دونیت کرده بودن. ممنونم ازتون
❤️</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3907" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3906">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3906" target="_blank">📅 19:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3905">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی نهان:
https://github.com/itsyebekhe/nahan
لینک اسکنر:
https://github.com/MatinSenPai/SenPaiScanner
لینک ربات ProxyIP یـ‌بـ‌خـ:
t.me/nahanproxyipbot
لینک ویدئوی اندروید:
https://youtu.be/2otJfXgNWCM
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل نهان
2- اتصال به ربات تلگرام و api کلودفلر
3- ساخت کاربر و مدیریتشون
4- رفع مشکل وارد نشدن ساب در  V2rayNG و ارور 1031 و 1101
5- اسکن آیپی تمیز با اسکنر SenPaiScanner
6- پیدا کردن و تنظیم ProxyIP بر اساس کشور یا بر اساس سرعت اتصال(توی ویدئو نشون دادم چقدر سرعتم بالا رفت برای دانلود)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از
YeBeKHe
عزیز
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(نسخه باکیفیت‌تر)
💰
دونیت</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3905" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3904">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">داریم تستش می‌کنیم این رو، و خارق‌العادست. دم ویسپر و پدی و بچه‌ها گرم واقعا توی ۱ دقیقه پنل BPB ساخته شد واسم و الان دارم پیام میدم باهاش</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3904" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3903">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">معرفی نسخه اولیه WhiteDNS BPB
نسخه اولیه اپلیکیشن WhiteDNS BPB منتشر شد.
این برنامه برای کسانی ساخته شده که می‌خواهند پنل BPB خودشان را راحت‌تر روی Cloudflare راه‌اندازی و مدیریت کنند، بدون اینکه لازم باشد همه مراحل را دستی و پیچیده انجام بدهند.
با این اپ می‌توانید:
✅
به حساب Cloudflare خود وصل شوید
✅
پنل BPB جدید بسازید
✅
پنل‌های ساخته‌شده را داخل خود اپ ببینید و مدیریت کنید
✅
پنل BPB را با مرورگر داخلی اپ باز کنید
✅
لینک‌های سابسکریپشن مختلف پنل را ببینید
✅
سابسکریپشن‌ها را کپی یا مستقیم وارد بخش VPN کنید
✅
کانفیگ‌ها را تست کنید
✅
از داخل اپ به VPN وصل شوید
✅
لاگ‌ها و وضعیت اتصال را بررسی کنید
در این نسخه تلاش شده همه چیز ساده و مرحله‌به‌مرحله باشد؛ از اتصال Cloudflare گرفته تا ساخت پنل، گرفتن سابسکریپشن و اتصال VPN.
اپلیکیشن هنوز در نسخه اولیه است، پس ممکن است در بعضی دستگاه‌ها یا شرایط خاص نیاز به بهبود داشته باشد. اگر مشکلی دیدید یا پیشنهادی داشتید، خوشحال می‌شویم گزارش کنید تا نسخه‌های بعدی بهتر و کامل‌تر شوند.
WhiteDNS BPB v1.0.0
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/3903" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3902">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3902" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3901">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB
خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3901" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3900">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مقامات هند، تلگرام را تا 22 ژوئن در این کشور مسدود کردند.</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3900" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3897">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hpv8DSVjjl7HrT0NzT0PcNS6ywH0VqMX_j04-LoV7csZbmg7Ea3ayooeXh8RC_Sjd6fbmfpYZA9cHMCna5czvBSSCR-WcUxfKBlW9qgk3HYW3We0mUK9rS0JUrtjMn7WVbiHm63vLbKqHrYtXlDT6-mEc3uL89M-YYpRKV5Kojvsm1Zt8D3kwyNGP2TE_u7FDNk9_RHruC01myEeJrH9TsX3wFS6tMk_wIIHWlwq0uoEiFlTSPMhV9dwtjHvEemdsoA56KCXJt633J0T7R8qZw6yD8eUlJO99JIZOsD3lHjRtqrH9taIeIFzW4NUrWFRSR1j7pNzj4SPGY6HMSCqyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pM-k4yJSnnTeIytJJGRUr4KbEOm2Bth30y_eRzDbo20YSbwV1vcoWE_lwlLfY8cVI2Fqm3R90hgXB0Nbr1AZzC7AHiMFOLpUG4BefedZpLKLv1zENkhV9UPH0vGUx6XP8EZcXNMuNJTORvL7r4lEeo5MoIHRyfpcjt5MEWnAaUQ-NNfpv5wTSssJqnOiLYPi-kSE8I0O3KTjyaGs6xYQWV-K9whsOEy4GU-wqMDTLMlrRSHtZtEvPPcMDc-GqRgWH1Gw5m4FxXf-IbUeYIlaBrsByie5SrF863NdpgUT43Fj-EvcgMgxoKALTg0ZVe6_tahWNm2b-oclN93svhQkMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m3dN5xXxbQPdmRJuyndC25SGYj05zX_3m-CvJ1r9eG2oOg9uDFFZHabCnPFJpHlIYGT_MsY9d1bPLtmWjlN9NTlw3jFeDQhigOIHsJjI7lTikE6YNbkYzkoCjuJdqiQBygDDIrfOagPF_Oov1tefcVQHo1KJkYFXSHdHowa-o5MA6PDCapYI6mHLOXyFNRaYCSZgwM36b-Ae5GkXBxlsKQKatRLQXX2zmeCRApRstNkppUjfltTW2zbnedJO3AlRvQg_bP7DctfBLmv8Z6AbUnV7MwayWQBDyq1GtNVPQFWZoxouiNp1WDKkqK-vWkMjBg8u6TZLKsIoBgzsQm0pkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد میگن چرا کامنت‌ها رو جواب نمیدی
چون 90 درصدشون جواب توی ویدئو هست، اما ویدئو رو کامل ندیدن
✉️
مثلا اینا کامنت‌های ویدئو BPB هست</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3897" target="_blank">📅 12:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3894">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jbYirOIEkr9mk7awYuZHFZJCRJusjJ62IAuXUZz-RVLFlX5eOFXRGFz3Af-tIJbHq6BV49hSDDaPKs-sVPl_jkolse8NgI7fxnzXCYrLwdIuCQKNtyX38HEXgAw43wiwW-Js9w0xwJY3hsf6oZXM2l7BV9llxNsv0ClhWSlKCzBtazbrWnfpymicjwmFpvaSFzRPkRej2-IxEWmGtWb1l10PP3yHdYJXx25K2GawXoHQmId_3HJmVUyjVgh3DBSqRNXMp4VtI-7Pkf5lajoJVEptHOZ4lKZX_mEGPBkDi0wZahkpLQsQPWlEzJW2JyEcE1KqHxGfyqXIQCGp1kvSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/seX3BoU9Lp_gFblp8ne9Yrzo1oGeZ81omo5UAQlqlOrx2y5oJqarH1-yKo_86WF9f2JP2Lg6_Fka4-2rz26O8cb8e5NXWMvRAFtYDw184D4Y8auCWs7eQSpboMyHeYpGxfnGz38KvNm7znXhjowj_Gih8n7SsD65K8Jf41thGP7vVBoY_439Lvpl3sxW-LHatVU9Z2ZsGfX3uuAdlUQpRsxpEdzeAJr447nhIYzxg72EsMbdF3YSmSQVJBZSSbiy0O5hnUXYl9aBE6ttY2kV8FMgHFPTJL10HUsb8FehUIy9uBhPCqYvD4q79X-Gn80jo69RaF9htwGv5kEh2mDelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NM9j8hyMosruhzZRePN64z1OndQ65EGImTAs8A1EH6TcPZ0VttNURGU9OxClcHnyTd5vCo5kC3OEyfOku2YmdbLlIq6FfgXJAUZnDOhixTDVLTi_Z7EdwoqnGHq31WR5viY9MlhkXge-2BFpJMpEaC2dhGtOdI3clXmE0yq_UlFi1qUABgvzNIPBoBVpXIjDeWdZCdq0UNIZPNjhncf08O1qcgQRLkyv35hlf5S56hZc5MDK1MajNPMuauEUXmLFInTCw2D-O_no4g1QGzCv7WikbEqu56lSXfqdyYEwOU5_tim8Hh7U1Ry7zVXPOAIjlxMRZx7ajCvr82j1-d-VAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3894" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3893">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">از دو روز پیش، دیدم که سرعت آپلود کانفیگ‌های مستقیم پشت کلودفلر روی یه سری اپراتورا توی منطقه‌ی ما به شدت افت کرده.
و بعد که چک کردم، متوجه شدم سرعت آپلود خود اینترنت خام کمه و زیر 1 مگابیت، و مشکل از کانفیگا هم نیست.
پیر شدیم برای یه اینترنت خوب</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/3893" target="_blank">📅 09:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3892">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شمع iced blueberry
🫐</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3892" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3891">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seFhADh1B_dh7pnMIELIZSv8gePCYMrnDSypuq5GZtXE9LtKp9sYnXP_N8Lt2oV3EahbYnTriPJsPFa5yu1ZUJYWKooUOaBk_VDe-MMhvpVxvILJnYKJ07IqraNDyNvT1k_T5hrWrQuRssXuAjS52gQWgM3_niksmbe6XXJHrxsTfxrXWdEWAKBR7Vti3lLS5kBkMw5uN8UXPpQXxR5QUQZF5Ev_p9D5ffRXQXxrcsAoe3SuH6Dw_tTS3f7fgBRbohNH8Gu7OLCm_iC0TbMQ1lY1UjdxuPgMSpbI5tSzR_e9C6hqae9Sz_U-WQnHninz03AO3EtmwUDWfm8lT7x1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
جدا از همه چی رفقا این ابزار رو خودم قبلا ساختم این ابزار چیه؟
این ابزار کارش اینه که شما لینک ساب بدید کانفیگ میده با فرمت های مختلف و همچنین این که کانفیگ بدید بهتون ساب میده یه سری آپدیت ها براش میدم تا بتونید مستقیم تو اپلیکیشن ها استفاده کنید ولی فعلا داشته باشید و ازش استفاده کنید.
لینک ابزار:
✅
https://xsparvin.github.io/Abzar/
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3891" target="_blank">📅 13:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3890">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hT7Ls9a7YYHNhnTvJMaEVPWuNCv5wVU1OT7sSpBmn5V-j_Lj21MQBXPEkuzFjDVrJ8KEsqQazmSB0077CxKvOxfUqCeaE1b1TcQ5G9OrhOqx_7dkb6l6YfITs08FQCtZ-HRUfir-b6W5DMWuWc6Jtdi_rl7nlOJExt3fMblexaYxEfxbQMjIv4cyqPrDKkx_maUbGGhj_SNBDYGMAyLX9owrWMWjd7ZEb9iKCRG19AzDksNwdvG20u6V1vqPkRXHrX9Mf_-eWS1WHe76K5YqP9I9roY-gEJeUzuzfgLGh6b14M3LTRKYByTlOIXiIqd6CEcxrdr3_9ATBEBZU-u4jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اول که ممنون از لطفتون و بازخورداتون، دوم اینکه اسکنر حجم زیادی میخوره حواستون به این نکته باشه
🧐</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3890" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3888">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ohynwwZp_7RmDhoACayOdp1ANp0ZU-FhOS_Xx5xe2RAR9EZqz6lc9cF3cgsSXix8taifWd1tqABXWI3Y55F1K7YEXRlUpZqIsmuotBNS8eeMlZ0lk5ORq_HP6V61IqNBLXn-FH4DzVP6sVEVgKW758aYEzlDy0_3JXgirUtTU7rJKbZ3pdQwQpl-w7gSNrwuwEYUoypjJVgnfRupHXR2Si0nbtxXDQxl-Tj7E6Us4p_KGfWOJhpczdo8JMV_Bgq57i9dVvnBG853-j5_4fIZNjsGnbzzZm-zx4HVmgf0aXN25I_3pVd-DJramDK8_xnsbTWTmh6OiP_LjOq7bPBTnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fUbCOEofqzb4aBCTqlzLgAoSa_MocF9Z515roBOV-xPae61TUQkT1NXw9vqZhFvHL973Mf3QWCFr065ApKl11tLsygL1Sj9gMWECHOlNn6f01le2SKsUkOG6hRA_KyMNxWu8abmrkiPxc92K0UIQvoW4cqZjaVPzKHJeG0ReYZdgOCyt53fZ7U_VAMrNxDm12k9k4KoDphRK1EqDhSY1iLbAzySE7utIzYXXG7_c9olJKU9Fhd1NUc1LDL0kHrn1NkFJmuD5aITNz2R0b-1rWJad34Ol9kfKOFEwEShvvsnVmke1IyEirJ9B33CJYqczpleG47K1JayR4tH_61DYUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور: @nahanproxyipbot</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3888" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3887">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/clUosUQF9GuInxzUxR25ltklAVoasLNs8_f73SivFdvt2ALBoqfG-e1WZUlgd8mznBGGXwlLahWT-vXtO2IB3-rxdx2MBZkdireeksMx5lzVhySQXcZxvnFeAVL3MygBcKu5jowf-Ls97AKK4WsQsuAHhodeNlSMEu9quCd5X_ALCe9Ut5l-ZMg9S7qNf6tKJH3KdEqIvOWZPGppaptxr5Q3YT-0smyegD6qLLE0KH0MGhbvZECGoPbRiKd_SmAgTEREIXFi7jdwW8X5UpSTCfpwjN8Ct-64A1yevZL49IFPb88iUXgngTkP8OcscqT6rOdwJOx7wPrWOUZQv2TgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور:
@nahanproxyipbot</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3887" target="_blank">📅 10:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3886">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خب قیمت دلار اومده 165
انگار جدی جدی توافق(که نه، تفاهم) شده</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/3886" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3885">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SvqHKgLdnLrNVjNkxjwoiFq1lyv7UqiOtcohQZF5VXSh7TTOHwXaZSKu4aHh2AlOrysHpwLcgPMqjaIJLh3iDWqOHoMXfuMWqIJ1LPpENWKwKLFVWiCJ059zC4ECSfUzLj6XkXb992T0QbggpaGGKvWsnBBVzL0_wJvRFtgDLQSZ0b0QLaxxcH8kNuemvhK3B-w-kVTbof6xCkXvxXh8f8YLdNW-w6BCM1em7gouGyt2v_EQ7iZXpe0MoLKN_zlSj66_h9hQ4U07CmiEw6vgNhvaJxL5kT2X5EDsfMpKuPRXOCH5FTsCPgtlVi6K1mKaNcCyT7KcgvpBIxS-EQy2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پروژه‌ی جالب دیدم به اسم SurfSense، که بهش می‌گن جایگزین اوپن سورس NotebookLM
📞
اگه از NotebookLM میاید، باید بگم که SurfSense همون کارو می‌کنه؛ صرفا با کنترل کامل دست خودتون. خلاصه بخوام بگم، یه agent تحقیقاتی اوپن‌سورس و با تمرکز روی حریم خصوصیه که شبیه به کار NotebookLM رو انجام میده.
👍
مزایا نسبت به NotebookLM:
• اتصال به ۲۵+ منبع: گوگل درایو، Notion، Slack، YouTube، GitHub و افزونه‌ی مرورگر برای ذخیره‌ی هر صفحه‌ای (حتی پشت لاگین)
• آزادی انتخاب مدل: ۱۰۰+ مدل از طریق LiteLLM، یا اجرای کاملاً لوکال با Ollama و vLLM
• بدون محدودیت داده: هیچ سقفی روی تعداد منبع و نوت‌بوک نیست، و دیتا روی سرور(یا سیستم) خودت می‌مونه
• جستجوی بهتر: RAG دومرحله‌ای در برابر سرچ تک‌مرحله‌ای NotebookLM
• قابلیت‌های تیمی جالب: به شما رول‌های Owner/Admin/Editor/Viewer میده + چت و کامنت و...
• تولید پادکستا بدون محدودیته
😭
معایب:
• نصبش هلو برو توی گلو نیست واقعا. رو اعصابه — باید با dependency، API key و فایل‌های Env کلنجار برید
• هنوز کاملاً production-ready نیست و در حال توسعه‌ی فعاله
• باید خودت میزبانی و نگهداری کنی؛ طبیعتا که راحتی NotebookLM رو نداره
#️⃣
جمع‌بندی:
صادقانه بگم، NotebookLM همچنان ساده‌تر و آماده‌تره ولی کاملاً بسته‌ست. SurfSense سخت‌تر راه میفته ولی دیتا و انتخاب مدل کاملاً دست خودته. اگه با self-hosting و سرور هم بخواید پیش برید، به درد بخورترینه.
🔗
ریپوی اصلی:
github.com/MODSetter/SurfSense
آدرس خود وبسایتش برای دانلود مستقیم نرم‌افزار:
https://www.surfsense.com/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/MatinSenPaii/3885" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3884">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3884" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3883">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/MatinSenPaii/3883" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3882">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eL5Yg30-ib_ioOLwg_kwb3zCJ-7dCRNFgu5xBLJaROj-UYW99SH90ibmZ4UPMW26mxv88y9Uic3ywfP7WcpWbt3vLlG89nv_S_6qEELE8RckdNWfOt6M-OtvOj6pKEAllQbmBjc8hD1HEDhHi86oDnVO-br14_8-ObRcEhaMkpNSsKi8M_KrYGLb9ZXskPjyl2-JRpdLZfAyoUEcW783ZArLzKCm1AA5rMZOFgcH7nAXyWwsLznpOkmgQJnfJND55nDqyQiy5F1Ki5hI-N1quRMZRB9_fFLmz23IFz2Sl1VOSCj-FMW-z3Rmlx_Bc9jl3RiuelBn0e7_B9jVSjhwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو برای اسکنر یا هر پروژه‌ی دیگه‌ای می‌گیرید، ترموکس رو از گیتهاب نصب کنید؛ درست میشه
https://github.com/termux/termux-app/releases</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/MatinSenPaii/3882" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3881">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bB1t6kgES22x12MksJWyPCXuknstU3Vm6keUgxbbiO1coRSAkxZcXOFZkd8EDxcIoS2__Mv0wG9srdP830OXWfPItjpMwsBpjXXWBiz1TFEO2k6JQU0N_n4JlEwqlpEZDngg6GfvksFk5KUPIclrbIHx1FJIjtcnm18PWb5BWzcvFrNY7FUJfNBlurcgox-YVch7PAfuQxaHjdZM97DKrhcCrp8pi1SxuaPlNpZTqNwWQoEz7gu_Zs4RkRTdMAt0l3xdx_VWsnIHBWuPh0zaur4742koofaP_hjFKoPnBxBFYIPI4kjCP_t12TPQkuoKR2OFn1ibfwcX2BOqM7rxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان خودم با سرعت عالی وصلم روی ایرانسل. ۲۰ ثانیه طول کشید حدودا، منتها ممکنه تا چند دقیقه طول بکشه. ولی وقتی وصل بشه دیگه کانکت می‌مونه و قطعی نداره</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3881" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
