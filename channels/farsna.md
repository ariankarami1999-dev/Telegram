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
<img src="https://cdn4.telesco.pe/file/DM5pz3A82iLdrLYW9uqHyvZx1Bvg9J_nxzj7ktlOlOaN_wds7n-IJYpYAGGF9SIxk5MTk091Zk2nMoSmMNXPyXca6b1r54uqUFR6ySg8Pa3JLvAhPD2WiONubsJg4Zs5PuzSv5cJEIcqGYhBPpGj2sALuQkuqstLV22SotiWJso34WGcl-G0VjSxsPqzq5KFeG1IQg2hK-Qik3pNLmFj_EHtPK9P4b5jwvqSfVK_REaWInwIFkVWgtj9uPyA2YzqBIC7MmoIizzH5LT8WEUhci5I8p-mRP-EteN40VaaW8PREqBhXld_rZRJaPTdypHN1XF4TOO432G3uRnuZgGu5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 13:59:26</div>
<hr>

<div class="tg-post" id="msg-440910">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd21840df.mp4?token=QMcllL1dSkl0n5-ebcziSo2TN7Skqx55n6HcChxfOv3fybHfXu21EcMCuX0ulO8GzFvetxUdcAwbpLwc3jL1grTUUnBUBYxeznSJT-6vAgtHN25aq7g4hnHO9EjJHZ0h0bRmbZlRlSEr4z3DeBeXh9x_Br1RQR-bzQk_OHDtndGOPb4FSgRByTVwF5r18Nqd66eVhmeb4_IsgPDuE3q60zqvJM_Jf73VFTjanhe2HAObS4IjbAzm2HLmCPNlaSkZTfakhNqEUqtB-t0a5K3oi9DyznWNFFny1cnQFdaLFqwJtRGwy81ffiL4M2FGn8VSdlc8n8XUnAN91GX2qscn3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd21840df.mp4?token=QMcllL1dSkl0n5-ebcziSo2TN7Skqx55n6HcChxfOv3fybHfXu21EcMCuX0ulO8GzFvetxUdcAwbpLwc3jL1grTUUnBUBYxeznSJT-6vAgtHN25aq7g4hnHO9EjJHZ0h0bRmbZlRlSEr4z3DeBeXh9x_Br1RQR-bzQk_OHDtndGOPb4FSgRByTVwF5r18Nqd66eVhmeb4_IsgPDuE3q60zqvJM_Jf73VFTjanhe2HAObS4IjbAzm2HLmCPNlaSkZTfakhNqEUqtB-t0a5K3oi9DyznWNFFny1cnQFdaLFqwJtRGwy81ffiL4M2FGn8VSdlc8n8XUnAN91GX2qscn3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس هلال‌احمر در خبرگزاری فارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/farsna/440910" target="_blank">📅 13:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440909">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nU0HBvpYsCKjgqExWODhlvKIDzOQsN56EgMDdsDq2bi6pW1ia9PFgYfVoxQO6Twuzf4fKYfV6fQV24kSApn7Fm0YK8Q3XzMEdXnvMXUMez26N3uq1AgM4t-saO80Lh08N5e-hAYki2rFy1vuhfYLZ5mrOHUnRA4Np7ijqgaCiHUQEC5v1LVDablNTN3TdgpZaBse3VKhU4PFSQPbxEcZPa-kA6f168iR87ngdW8QmYOry2v6v7mgNJrXo--UkNTDeqBrKpBCyuL4Y_vf4ExUgekoHUUuuMXlGXq_7yLXTnNERwvZ5FNGOmVlj_uiyBpsVWu6SUq0tGhX_0prf4jTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
😇
رشد حدود ۲۴ درصدی سهام «سمایه»؛ بازتاب اعتماد بازار به مسیر تحول بانک سرمایه
🔵
گزارش «صدای بورس» با نگاهی به روند معاملات سهام بانک سرمایه، به آثار برنامه‌های اصلاحی، ارتقای شفافیت و اقدامات تحولی بانک در ماه‌های اخیر پرداخته است.
🔗
متن کامل گزارش را
اینجا
بخوانید
#بانک_خوب_سرمایه_است
‌
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/farsna/440909" target="_blank">📅 13:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440908">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جانفدایان اقتصادی ارس (۱)
مجتمع فولاد آذرآبادگان ارس
در روزهای جنگ رمضان، منطقه آزاد ارس با همراهی فعالان اقتصادی، صنعتگران، کارگران و تیم مدیریتی خود، اجازه نداد چرخه تولید و اقتصاد متوقف شود.
در سایه مدیریت، هماهنگی و حمایت‌های انجام‌شده، واحدهای صنعتی منطقه همچنان به فعالیت خود ادامه دادند و ارس به نمادی از پایداری اقتصادی در روزهای بحران تبدیل شد.
شرکت مجتمع فولاد آذرآبادگان ارس از واحدهای شاخص صنعتی منطقه آزاد ارس، یکی از مجموعه‌هایی بود که در این روزها با تکیه بر توان کارکنان و مدیران خود، تولید را بدون وقفه ادامه داد.
این قسمت از مجموعه «جانفدایان اقتصادی ارس» روایتی است از تلاش و ایستادگی کارگران، صنعتگران و مدیرانی که در روزهای سخت، سنگر تولید را حفظ کردند و اجازه ندادند چرخ‌های اقتصاد از حرکت بازایستد.
#جانفدایان_اقتصادی_ارس
#منطقه_آزاد_ارس</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/farsna/440908" target="_blank">📅 13:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440907">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/farsna/440907" target="_blank">📅 13:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440906">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پروازهای فرودگاه هاشمی‌نژاد مشهد لغو شد
🔹
سخنگوی فرودگاه‌های خراسان‌رضوی: با توجه به شرایط پیش آمده کلیه پروازهای فرودگاه بین‌المللی شهید هاشمی‌نژاد مشهد لغو شد. @Farsan - Link</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/farsna/440906" target="_blank">📅 13:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440901">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_21UjEaoCsOV-cko_JWLTv4LRiPpbXgtqGGgM02MKQo5iiUUDZj-8b6-f624Wso02CNP6Joc0w6sYB-44m42rmQfeZZRvFiqKX5bVd3gbloSNHav1qws4Olh9yIgv6uP-BS2v6Hv8j4a_b2u4ZP3gh3ijbhyaRDwrbuX-4Yyqg0hrjptdWNUm572rKvLyn_fBI9VtfsTyZcXPcgKy6Dv8MecO-I9FEVcVlOTcsRZsi3VfhLYZ7GG3o7bIWHdY0iwnCHqLkYZ52LbYZsE5UmfVYv3DbbfG6SsL7lqViTym3-S8GL1XgheEYaYxj80dd4ZklquIkSlmocKZ1yfFB4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ih7u3s4iytJTVJMo7TBFsyDq-Y-Hmui3zPG5_pxYZnoVnactlX2oHPnYCEwaIa5ZN4rG6NcBO76tCF0X7YZjf-MmiQ8k5ylTzj1ZpU34-dUIqvjD8FnP3atIgESUdn0AjceRLFsT2XI5sebq6xTETEICQv0PHY_a9tKXtM3todzPZbFnneHPlyWHvUE1XnCnqcg7wCDiyh4f6NV4cy5BxKMZTgB-tJve-fT0X2BJI7SRgr7r8sz1Hur4o_OwPLNtvWEdY1jiwiW757gP5gYGVvl-hmAAbpf0a8-S9AnL2h6PuMkkns5mroTqYM59bXk7h8iU12KN5wPv5NvDBEbweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qA-UL-GkBYhvUnyDyrhGK7azpOJzWxDjxuYqoaAwigJZ3vA3wkoSzmxpXBJy8pvgL-Jo7Dk5YJ84ouXq5G34XNO9FdQ6LlOOL39ZgcYvR3wvcYKa9nUcPndhMLfLVsDBRV6DaBYenhpu4WpK1QTVyoFZLmFa2aA1ywldBCgGdYRjBTC3OfrYJ31ORcQWA__pPNHL_eXI_aDLTCBwYa8c18Yj3gWTANBGCaxmCjbdAPuoNF28n_O62w0ZRD5dRTwx2kmhrLNttPUtGhOtqRGy9LALI_Ob4BNdlvLxRCM30gxeDjJdmbR9HQ1l0W_Egg4ZTPi80BruxsZcHruM8GKmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8YrwecVo2xc0D9I4e0oy-thaNrGeBeB8mXzUNxBfvLKKJP6r8vLlASu87NJXzvePq-6bK9pO9wgBpAV7_kl_yqxJvbKjcfYlCZrbuFzMm1n6mnbTTSG6FrxphwzdUY8caXrZsARo8naOm7kL8uqLBQFhDic0nRLOJlgtrX11Z_E8pDgkoVIv09rX7kbtdpXuNJJMUTwP60vUHuImfygLJOmy3HR40_I6Ra1uxHYKLwWpmqFGsirWt8rnXTtL5Wp-9peRDjMnhbqlWz8NAAXMQbN51j-fJSuPGwc8dJV4Wv4rpS2u58TlgFyVYIT1oQFYlWV3Y5wfsjP5_WDhWle1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2Xi7EKEo2ftYFjc4jili7CrpDhEfO9gEX11Ru-cDMf4yC6Bzesrevd64_oXP5IApUO0QNl5MckAbXHpfHqET1HZJ0fKkzTRewtrjZUmm1WCrsihpholzOjbWxL22ow131Yn-YmFH0cxBvvgnaJZy_HHKlK0zUdIxyY5lqaqhSXVYQTO1BetT0MULh0E8bg7qykRZbu0VS61g9fHFeGAyexqaeJYyVSDcVnHEYqrh9DbTEA-cr-Ijz6oIs_Nd76wu2Uv2CuIGXYZzyjDgGypWMSi38dl_g354zCUM0AtUiW5J4tL7jI1aqZ1EMzlutOdFZD6aR5VvOD1Uu9TyiaqyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار اعضای دفتر حفظ و نشر آثار رهبر شهید با خانوادهٔ سردار شهید سعیدی‌راد
🔸
سردار شهید مرتضی سعیدی‌راد همراه با رهبر شهید انقلاب، در اولین روز جنگ رمضان در اثر حملهٔ آمریکایی-صهیونیستی به‌شهادت رسیدند.
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/farsna/440901" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440900">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFcc24uXus_Luwkpj-fDKX7HgVnU3nC_iepBbxxgAdwVPQbAUk0QyhalIIT0fQPefe19nZd6XoIwDqP1pdTdN9_uuocYQq0JYVcz1uz-phXJBxxdu_hGuDHQn5CplBTJlHYMeU2wyPuQ38RNU3gMDqbhuo3RJPBQVHu9LroHHDHxUmXg6OMhT8xNOJ9zS-wJwhaOa94FaRqGObcK0Tzeyw6ITLofa42seFOKWMWqVJPG3c5WFmKtE6n8c7ostfYb2GC7NqZQbkg78s2DtGc5sDWEH4JsULNPAJd_DcG28-dsL_v7pKIUzCarDkcqgXbFEe1xkAZ9R-d7rJl5nrdf8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عبدالله گنجی: روایت منتشرشده دربارهٔ جراحت پای رهبر انقلاب غیر واقعی است
🔹
در خبرها آمده بود که یکی از اعضای محترم مجلس خبرگان رهبری در سیرجان گفته «جراحت رهبر معظم انقلاب در ٩ اسفند در حد قطع پا بود که با درایت پزشکان مشکل مرتفع شده است.
🔹
با پزشکان معالج شخصاً صحبت کردم. هم تکذیب کردند، هم از این خبر غیرواقعی تعجب کردند! گفتند اگر صلاح بود از قول ما به مردم بگویید «از اول هیچ مشکل اساسی وجود نداشت و ندارد».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farsna/440900" target="_blank">📅 13:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440899">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6f3658ef.mp4?token=prI6OxXNLx32-QMkLw7YH5O2Q6OIDZ8QduCKVb-npvE958ZD7iqIadH3E4cofQEEypF3jF3T70EeZ52cxFifGavoIn_MeLvb471RNbglWJ5MV9XPb4W9okAkkXQdBBXvWdUx-Z0dylxzHYaOIUecDvt7ke2S8XjhIqLfTbXmW0Ja0ZFPzkOPBRzbrppKS7bWEPLHF0zrRiLhl-CHC9hDHAXINt7Sf1yZVej4DuJbcTMFHz08lJY7r-OGiLVzjjlC4X9AbVbS001O6flLtHvc7wxr7-6iFX_zhpUfuQOaB0jsZjR3_3KZd062R5PBJTsGNRdKWnDhChjUsnyF6a-lPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6f3658ef.mp4?token=prI6OxXNLx32-QMkLw7YH5O2Q6OIDZ8QduCKVb-npvE958ZD7iqIadH3E4cofQEEypF3jF3T70EeZ52cxFifGavoIn_MeLvb471RNbglWJ5MV9XPb4W9okAkkXQdBBXvWdUx-Z0dylxzHYaOIUecDvt7ke2S8XjhIqLfTbXmW0Ja0ZFPzkOPBRzbrppKS7bWEPLHF0zrRiLhl-CHC9hDHAXINt7Sf1yZVej4DuJbcTMFHz08lJY7r-OGiLVzjjlC4X9AbVbS001O6flLtHvc7wxr7-6iFX_zhpUfuQOaB0jsZjR3_3KZd062R5PBJTsGNRdKWnDhChjUsnyF6a-lPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار مرگبار خودروی بمب‌گذاری شده در مسکو
🔹
همزمان با ادامه جنگ روسیه و اوکراین، مقامات روس خبر کردند که یک نفر بر اثر انفجار خودروی بمب‌گذاری شده در حومه شرقی مسکو کشته شد.
🔹
این انفجار در نزدیکی همان شهری رخ داده است که سال گذشته سپهبد یاروسلاو موسکالیک در آن ترور شد. او که معاون رئیس اداره اصلی عملیات ستاد کل بود، در یک بمب‌گذاری خودرو کشته شد.
🔹
دفتر دادستانی منطقه مسکو اعلام کرد که بر تحقیقات در مورد این انفجار نظارت دارد اما هنوز هیچ مظنون یا انگیزه‌ای معرفی نشده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/440899" target="_blank">📅 13:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440898">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
عاملی: تصمیم‌گیری دربارۀ قیمت‌های اینترنت پرو مربوط به شورای‌عالی فضای مجازی نیست
🔹
عضو شورای‌عالی فضای مجازی: بسته اینترنت پرو فضای تبعیض‌آمیزی ایجاد کرده و قیمت‌های گران آن در شورا تصویب نشده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/440898" target="_blank">📅 13:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440897">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiVt5m-rQWJFF5nTQfLCNuGza6YUg3qbV9qd3ldrow-Bp9J1iztaWSfvRB2oteKkmO-FNJ6bQI6UKirRtgfnPzzvGVVOKRA1Az-kw-FxyOwdxxPZV2-zjzPxLdiBdYwW-AIIesgz9b7zuxRJnWgxIF4DkIEg2O7A3YsODFSFC0hoc9MuJZ6kCqCHhJTV_PK7_Kqg5D9BuOTYmjgfLpNVMT21LaM6EWTLY5ZNoqd_yPVU81TWuQl6Fz6LxasM-CzXNRAh7VBh9RV4C5JGCM0zF6MjttBoxPko49Ws67ZIbAR4oyn3H--L0h814K8AKGFI6Bx08e2C1D-TSNliXGHIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تعویق انتخابات شوراها با مصوبۀ شورای‌عالی امنیت ملی
🔹
رئیس ستاد انتخابات کشور: با مصوبۀ شورای‌عالی امنیت ملی و درپی شرایط جنگی، انتخابات شوراها و انتخابات میان‌دوره‌ای مجلس و خبرگان به تعویق افتاد و زمان جدید برگزاری آن پس از اعلام پایان جنگ تعیین و اطلاع‌رسانی…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/440897" target="_blank">📅 13:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440896">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5x-4f8iWWaK_SSwzmx9naanKPYr9GG7gd6Q6Zv7LpbhorcO5k0Hcxm4cOPAMsELV9jpHzzKXOdSwn3KzVqVRcFBmXKERHF669Xqpd5NU6GQEpmroQUIurrmDdTJOCZwsHyKZhYLUcXniLUd31cGgdNNhCX4FEW-TkVW_0IGnEwb3qKTY3VmbXKo-IuYUMcxrb8GYDhIHyVrgskSdfbw3MXXbzyi2nFtw5T3nwiH7xIazSy8UQbffMw5VwOpU__YUpRq9rMuN8BlAY8gnbRXFh5QCjHm8yJ78v-rlblUJnpnuiEkCZNmiwNaH-kydIwEbhNMdsfWCjGuI39Tvs7QPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با جهش سه‌رقمی ۴.۵ میلیونی شد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۱۵ هزار واحدی به ۴ میلیون و ۵۴۱ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/440896" target="_blank">📅 12:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440886">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6kgoUgTSshPJuzXn4srX2HXP4xAd-G0Yezstsd-1NE62wsHR8Trbx29dbASwZT0XUVPHSPHMndOA1_x3ro48y27LRKjIaYWs2omiDexl8zRnf5RhrGFXMFDPg-z13r9tom_9WbO9ZoX17ErUXmo4xKHg9-OF6LBphnXxCYcHLsSGhRfRf9lx5DJfwx8dtfLtJN-xaNXMzsUpm58KapmVOCVRTQmmcqqi0d_V06uhBUQrKTrKRvEcoQP5vNeK34wPoG9S3J1PHBvD5AJ5YwXIoyPkD_NftTYtuu74rwvWMV4uKN-gYLsADVvSjrZsIb4aMWYeIhiYPGE-cGRurQuyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQLkUYgMjMfjXK_Ddf283X-n7sC58mSNkLOvWbX6InWtRCQ02miujfAUjCcARRLwObdHtvkdE-l6lnCvbdpZy9w83g992RjJBlA6dh4KkwM9KJCbNIvcfj0EAdLq0Ksqn5rJldlDki8SDpF96BQJ5DWwJOFCkE0ykfaw8BHMwwu39wEQkzmv6WSGqS75E4jvSK9PR3eRNbv66dvH7_EDfnHYJ2HUhrqyp3vBfLXbIIWxYrpOurZpesg-OpdUQIRLs8DnpIsARSCKl4Y5EvATPR4j8xsnr4NF-nw6htkC_vdxoJKTvAuWklOwF7q-7YqsBCCMWqY5QA95WBlsw0HHew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_tqSs76g4pHTO9rejgFb-Dt3nI5z7hQ7pFas43kifIyXiOfgqNufxQwIzAaF2vDaPb4POrRQzYUS4q4i9uxb1Flx5l4RWdo-cpfs2aSJWNSqmWyDKYIx8HNY0v5do4nClNAT_Ie2d80DqLI4VpbF3pAR5tzxgqjFr7fCVv2nQ8V6Sl3MqzviNiSXsz9TnekifoSGTC8Gz-F67bLXgf-p0gZBdOtKOMUbj6av-4U0gHQOTRLnKX-THpjUNjjg41krHp0tb7mCFZ6tzZYWvn8REI2K7hJXtcAEA7C025lnA0Jc0bpOjIYahzp1AS-1AP8OcFJm8KeynCKjFq1psA45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QaAkEYEAa2w6U2rFfQGEwZyP5x9eGBq6HFrYF5-nV2p2c75Lv4OOMbKRJrJ-FXIqRaKhYkY7-XXHhA3uwzX_L1ZUeFtJgp_Ptj9QZr7s7AtdhMRCGtgiLk15tuA1zYyxtmrY8WpUxO-Cb_q_S7Yf7Ma5pVVpZhmshwPOd01gJBgrH4CnnvWkcNbZPbketgjqc7-Drv2MWgZTGS1CMtsLE2TvKlw96Km9iB0AbdAeNxoqsDwIPrWmh0X1dCsPpjYLU9JBXHabywaApasYLvNYhAn1kSq7OPv7t3n03ggXfV44UThUhBW16h5wmCnU595NyHssFHZZzU1DQ4QMfJaZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcuS_JG0wltgaU9_4kCcbWTRsAF86HXx_bI8SJWl-RkSbhBIvoMgpTs0vq56eq2ZYBciPdxjA4Q-PnY0HaXn3QqBNkvC2UglF5BastfKfA-7iaC0HA65rtyBKIAcg9ndg_KRp1QelErg6X1qa8GkJYq5-V_4-ZrjMNoBBkJ2TzsYytMf86Br4WIqHO13r9c9eMzjyxjmvykq-vPKpq-YhNq6gMk1EOefWK4IEv4m-vPgYpHwCzx1nNSqSylZvUVf-LsIo7QIFcHFuzuN_8z-nKsQv03Rk8KSCMY07UDEjo77yAu9mFbCT3qF7Ib6FKOotRIXcI8J_gw7DhOsLw7_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7iPA0IwBvxmyrzkz0pu8c-5NZNKpLFXRrbm1WGwF4IRbzwCYSqT_TK_lraKW4Mp2ho5gHuHneVjKBN6J6kJ7DzReF1roKU_tIW5Fi0rTpgA_V4rIMbstJ5FBqcCwjUUQuD634e2C3LrWYY5jh6xWZw4zaKT0mF7DhazzLQU_fTJ9yDmB5bcoIj2k4jnQPeEEj4ZjC_NikUuFzLHgV-CN4ngLMRLW5IsDo2l00cntsGLohHrE7bcAjAmda3HFCWZL48CFbLRmx1Wt3VXOZzyt4XDHQD9csrR6RuDzDI7X3_KB2RF8HjP1WOBZyWj-PYECg7QQoTfPX2KdhSTsqu6iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNg0oYHVMRgSCj_O68DtnxHv87WIRFvUrFo_C70FVpGrzM14k8Y1T_Atr9c0p4JSCSdpEAitbnG33eD44UEgrk4zLA3VIhQiXhpQuMU6pV4QxfQJ2XZopvTX1-2CubMNXrSMCcc8nKs54Xx-3wA4NbQJ8q0dTDOpisM3eHSj6Nv_UyNgkxIxkYtcLdqb98eTakoF9-0a6R4WWoX4sumfbZ0wHQUw2uD-7NJ7rc2TC09ScdNjY-N6enDQGzSkjHY0JXEYP1zKmUxLjy4PSB-A-5FbTWPawBSRBO4TV0e2XqsIvq5ZadnxLG-UZ7jo_FxwMbw2v_d4zPYhDzrn4fcHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X69juzC3kv7PSMPz6G8dVAC6recAU9BLTNp4BeIxdXC-PFpXuOZVpTvVg2aNpfxjvzAr70r_vMS-44UvvGkFR61qqwuvSu6-lqw-mSINqf2t02E2H5u7Ymn4oJr_E-tAqiWeXaTFAqHG4e0dQxG502U6Q0es2g0azPo6O8vtW9XVwmMCF7bjDkyyO06PflFNuP-rH8Ia88EjHA0WpKryh5Z2TrUOg0Wf5nyFjxgJ2aENvDLBDtSnea1E8GCs5FIR_z0VYOmuL_eqAirQZdSrzZkp6nsjevnmEYBcWVQWfyd2EUFUMoYyZ6CSuyLu7_qekSkSjhlYNQ7i0NsxHLUJlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTVuly6Td0YRlZnEH10CAGlVnQsYinkCQNRow8A0onzlhYcLgR4FNhu99sl7tHZJjlf93hfgjt7TgdFxVk9_sgiMO5FoukQTKgu5IAMd0YsGC_zvQie7GSaJ3Q-fpZX4VzExTZjUWfZy0mN7z73rNbFCdsKMJI7iEzZLCtVkH2mp1Lp1KqRax_EMLVhFqRSxWVGfwPNCnrYBwc2ybuea5pxZifkaIxXQH0vNsU6m7ITjKiIcYsQjFizKkiVoUPZY7Y7j-tKeZoQZ8bupAjSPUrsTdqAw8whYQZP-kbMtxbT1UnDmZPxQMNl_crzPUjoSb52PH816f6g7ld-1ezEZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSK8d48xAhFvHDYIRvpY8jYwm6YL9rqLlIdkw3QLC2cEwzP01DkdULpzocMxuua9yNMHQVmX7dPSSXYLXYRfpofjYwFhyiQrAq3TB_Z8qJNPaiEXVQP5jONJFAT6srjRoUEk-CuuSOQExglKTqeNshAs7hwUIOn99NyoOsVCcCnHhKaFT_QSEu8Gg_9s5pRBJVRWPrXgexVA5ZnO5oKr9zkH6JUZx42sPfyQaC_Ox2lYsFtbb7IH4_bxpNuIsHP3QY_3PikD-pqj0pyK8XQNSuYg8pbB-HrQ0vOB1rU_5jizDkg-LmpQYW_AsNse8jxokttSvQp4RON_5bxpJYONzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی به‌جامانده از صدمین شب بعثت مردم
عکس:
محمدحسن اصلانی
@Farsna</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/440886" target="_blank">📅 12:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440885">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOGoNlHggvfziX0rvatjUlLlEdlPKGNlPJxMQplU-pxw0NK6-t-wtcsYIOnIjEwf0KbhDkbEvxTv2fTahC3yyCus_gHDwiALeMFNXBSVh77qPW5g410dMkUOemMtVK-moXlU-yTowYE6t0l6GzuHRHiFhyGILrP3gyfXwdaNWluLgcMbWTJnqwgsdsflA4OvreNmCy6fuQ33TrloKBaZkQfrCbJalKCEwPKixxqIhduOkbuzufu1RUG-pqP5EYRbasNdkrkDtjolPyZKE-9D4EoucPiQYSorAC8EDw6-Ny0m2DHmM3M4JuTuC4trlkdHLoxn2iZQKk3jgqMaTryeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعزام محرمانه چتربازان آمریکا به اسرائیل برای تصرف جنوب ایران
🔹
خبرنگار آمریکایی کنت کلیپنستاین در خبری اختصاصی گزارش داد که در اوج جنگ با ایران، «ایالات متحده به طور محرمانه چتربازان خود را به اسرائیل فرستاد.»
🔹
در گزارش کلیپنستاین در وبگاه شخصی او آمده است: «وقتی پنتاگون در ماه مارس اعلام کرد که لشکر ۸۲ هوابرد در حال اعزام به خاورمیانه است، یک موضوع کلیدی را پنهان کرد: برخی از چتربازان به اسرائیل اعزام شدند.»
🔹
او نوشت: «یک منبع نظامی درگیر در برنامه‌ریزی جنگ به من گفت که این اعزام با برنامه‌های مشترک احتمالی جدید ایالات متحده و اسرائیل برای تصرف جزیره خارگ و ایجاد قلمرو ساحلی در داخل ایران مرتبط است.»
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/440885" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440884">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">توقیف اموال ۱۳ متهم همکاری با معاندین در فارس
🔹
رئیس‌کل دادگستری فارس: پروندهٔ قضایی برای بیش از ۲۰ نفر از عوامل کانال جعلی معروف به «گارد جاویدان» در شهرستان زرین‌دشت تشکیل شد.
🔹
در گام نخست، اموال ۱۳ نفر از متهمان این پرونده شناسایی و به‌نفع حقوق عامه توقیف شده است.
🔹
انتشار محتوا‌های مجرمانه و جریحه‌دارکنندهٔ احساسات عمومی که امنیت روانی جامعه و ارزش‌های دینی مردم را هدف قرار داده بود، از دید نهاد‌های امنیتی پنهان نماند.
@Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/440884" target="_blank">📅 12:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440883">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNQPgZ8Fmgxh8i0d9ZqjfBJ0yXLWnlo9FIlV8IP0v4ek1Tq81hFHX1a9DAt5kUW5WsYl7x4Zwk2StaFe7SnkzNiyq8bg5FNpV_zkuJSk02zgnDS-zjZhA9iGWbWsHD8nqGWs29ziVbdzwa0Rf20RjAjp2WCL1dCf94MiOvzbMjee1nywOWmNxrEoA1_fQlsFRyXSBRpZVu89lr7B6ghVDHIBIVEKIoTD3R--COPjdyZGYqteBOTN-QVl2C99y2f4Fsy15Uet5-e3d4Gcn1PiGJiGX1g-y64He4TZQ7_vSvR7-uz9_X-skjbaoIPcES5TSvNm3vNw9LoSTU3Zqa7DoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین وضعیت اتصال اینترنت بین‌الملل
🔹
با ادامه روند بازگشایی اینترنت از عصر امروز، از ساعتی قبل دسترسی به اینترنت همراه نیز برقرار شده و کاربران از اتصال دوباره به اینترنت بین‌الملل خبر می‌دهند.
🔹
داده‌های «کلودفلر رادار» نشان می‌دهد ترافیک شبکه اینترنت…</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/440883" target="_blank">📅 12:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440882">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1826abf8b0.mp4?token=j3BX-1oEv6LewdMgtV3LoQ2tzkUaqBbTbeOj_XKvCP3T48kDNXs0lgnJ1jFSvtkfWRvCAadkx2AYHuicAfYf09XNlMVlsGYyEks0mrpEUbh6Xt5Y2-kFxk3VUMU2PdL5F25omNk3eP-j-wgrrNfwKWT4AKTIaK1PMNzOwBapli6A3ut74oH3TaC7yJQ41eaHzUWmCCj1uSmddcuQKJdmwilkQ6meiXaJQhDl1WHDua4k9O4bX0l2v3hIXpUZa99po0PBRzXoW6GcQHUvtBiuDO4_yY2n4ffgdAcQUkPq1bP65uQnX6LtArMEJm2XK9_z0CIe9yTGdwM4l-KMKf858A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1826abf8b0.mp4?token=j3BX-1oEv6LewdMgtV3LoQ2tzkUaqBbTbeOj_XKvCP3T48kDNXs0lgnJ1jFSvtkfWRvCAadkx2AYHuicAfYf09XNlMVlsGYyEks0mrpEUbh6Xt5Y2-kFxk3VUMU2PdL5F25omNk3eP-j-wgrrNfwKWT4AKTIaK1PMNzOwBapli6A3ut74oH3TaC7yJQ41eaHzUWmCCj1uSmddcuQKJdmwilkQ6meiXaJQhDl1WHDua4k9O4bX0l2v3hIXpUZa99po0PBRzXoW6GcQHUvtBiuDO4_yY2n4ffgdAcQUkPq1bP65uQnX6LtArMEJm2XK9_z0CIe9yTGdwM4l-KMKf858A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امام رضا(ع) برای ماه محرم آماده می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/440882" target="_blank">📅 11:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440881">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آمریکا ۲۰ درصد اینترنت را برای ایرانی‌ها تحریم کرده است
🔹
درحالی‌که آمریکا از «اینترنت آزاد برای همه» سخن می‌گوید، بخش قابل‌توجهی از خدمات و زیرساخت‌های اینترنتی را برای کاربران ایرانی مسدود کرده است.
🔹
براساس آمارها، از میان حدود یک میلیون دامنهٔ برتر اینترنتی جهان، نزدیک به ۲۰۰ هزار دامنه برای کاربران ایرانی تحریم شده‌اند.
🔹
این محدودیت در میان ۱۰۰ هزار وبگاه مهم دنیا که در توسعهٔ محصولات دیجیتال نقش کلیدی دارند، به حدود ۳۰ درصد می‌رسد؛ یعنی نزدیک به یک‌سوم این زیرساخت‌ها برای ایرانیان در دسترس نیست.
🔸
ابزارهای شناخته‌شده‌ای مانند Adobe Creative Cloud، Figma، Midjourney و Canva نیز در فهرست خدمات محدودشده برای کاربران ایرانی قرار دارند.
🔸
در حوزهٔ هوش مصنوعی و توسعهٔ نرم‌افزار نیز تحریم‌ها دسترسی به برخی خدمات شرکت‌های بزرگ فناوری از جمله Oracle، GitLab و Google Gemini را با محدودیت مواجه کرده است.
🔹
این موارد تنها بخشی از فهرست بلندبالای خدمات و ابزارهایی است که به دلیل تحریم‌های آمریکا از دسترس کاربران ایرانی خارج شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/440881" target="_blank">📅 11:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440880">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkBjy9WA3GM7-Le7el4CBNVtB7qfBbqpUdJ9WoebBe5A9Al7sELwrJ_0XS8i8IJh9dPn5S5vbo16A9bsRKCa_dYYrNXauhz7V9GIvFSaOR_QcbATiekcifvSwM5n5wWAPFcH_1wPXgR4mWzPLSIz0ShEjDpIogaDQrVMwkmK8HJ1a5LySB4KLbJ-5qotGPtz7Dy9QdDmEWqmbrOqAYpdfbGgQ_tmxX1bbrM8iWtSy_-BucmCUAoXKeTLm34lfnWMilIVLoPK1EvbyCpra5JQvo3VchTh51bLG0xAukphQVA1Gu87euvx4YNJ-W4cAq-DFg3lwS-A7_1Fnl9usZTDOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیۀ شماره ۱ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه
🔹
برنامه‌ریزی‌های لازم برای برگزاری باشکوه مراسم وداع، تشییع و تدفین امام مجاهد شهیدمان توسط دستگاه‌های مسئول و گروه‌های مردمی، درحال پیگیری است؛…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/440880" target="_blank">📅 11:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440879">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ade9a5ee.mp4?token=pbhJEHUnXaFVudX9wnFFLY0AnrRo3hzEcV-olx1okH9XJSdZ0SvmikvIvf_jjtQNaYGuVGtxUnZEhwSFpBpwIZGxjHzrMQrCOYeafm3AZ2FToeC_WYeXXtbqIt0AFs05ZFUu0za53UNr54CmwZnfprNcpERD83PHAPCysXFoKdwfjDYX4s_EjT17XOpNxkqIzb1vIsB-tHFIMrDDbfW_FSwrJyRzmVgj10-UTmkBYlcPMnG-qRagzh5qH2XBwR0Vy5fgbu2-Vf-8cYjt8GrmaGiYEFgJiySSZrByqxffIBS_xeiOdHgt8VmeiUHVlnudABSWv9SBRmM7iHwFxtrxjUWdQYb9KzwFO4JGKC6XJY9kt5wAK3kt6y6STVfc9bNhgtokcA-r7UJdzu_c_aOXV3lkUvcwZ7psVltrJbwgpcTsIyYEEp2_w-F4Xv08tHnVLDg_STXXhB0EFyi88yiqNj8KVb1tsqqDJxIJ-Bql0xqfzQKQPDOk0j39q7eMQTFbIPLO3TKUlM7aji7sINO5bZUbu1TMTUAnEhA6y_ExdPXpp23qZRT98mrXeL3D0aQ-a6mEC80IsnBSXAFfPhlY7763XD1oVfLHVcK4QyfzAKM9pZQswjuWHXw8im9QCUKEr8rIb0zDy8wEijxonsYWu_aLx3wBz11QythccZO2YFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ade9a5ee.mp4?token=pbhJEHUnXaFVudX9wnFFLY0AnrRo3hzEcV-olx1okH9XJSdZ0SvmikvIvf_jjtQNaYGuVGtxUnZEhwSFpBpwIZGxjHzrMQrCOYeafm3AZ2FToeC_WYeXXtbqIt0AFs05ZFUu0za53UNr54CmwZnfprNcpERD83PHAPCysXFoKdwfjDYX4s_EjT17XOpNxkqIzb1vIsB-tHFIMrDDbfW_FSwrJyRzmVgj10-UTmkBYlcPMnG-qRagzh5qH2XBwR0Vy5fgbu2-Vf-8cYjt8GrmaGiYEFgJiySSZrByqxffIBS_xeiOdHgt8VmeiUHVlnudABSWv9SBRmM7iHwFxtrxjUWdQYb9KzwFO4JGKC6XJY9kt5wAK3kt6y6STVfc9bNhgtokcA-r7UJdzu_c_aOXV3lkUvcwZ7psVltrJbwgpcTsIyYEEp2_w-F4Xv08tHnVLDg_STXXhB0EFyi88yiqNj8KVb1tsqqDJxIJ-Bql0xqfzQKQPDOk0j39q7eMQTFbIPLO3TKUlM7aji7sINO5bZUbu1TMTUAnEhA6y_ExdPXpp23qZRT98mrXeL3D0aQ-a6mEC80IsnBSXAFfPhlY7763XD1oVfLHVcK4QyfzAKM9pZQswjuWHXw8im9QCUKEr8rIb0zDy8wEijxonsYWu_aLx3wBz11QythccZO2YFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین سالگرد شهادت سربازان سیدعلی، شهیدان حاجی‌زاده و محمود باقری
🗓
پنجشنبه ۲۱ خرداد، ساعت ۱۷ الی ۱۹، قطعه ۵۰ گلزار شهدای بهشت زهرا
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/440879" target="_blank">📅 11:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440877">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efad1994eb.mp4?token=Ja3YaFk21c9Dx_zl1R2xEMa3V0SlKregF11XwuBkbjQ0l9Nxi0u6MQNJlqxZ0UGdFkoe3gKJWpTVIWL6tF79SmMPBNNeNpZhHMz75b6CNW-dTNVKM8m-imlRmM8XEd2x9gVstHvCOkHtaxXcWfIQoim7MGSPbFRJe3TTSh8ZEfhrrY73jFVMrZMfFaxfduQhC00470cgjYFs0Emhf0J4g96Hta7tRPcp5MNHljhGQ66QP08xNnLEsPlWIvvGa1cNCI2_e0V_SEb9ud-uLn2grHvbyx5-1jaIMY9ZsZQI6rxKzxiIS6PBM8FzsvNLWwN36CI_slzlw8tsDfOZfoCPUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efad1994eb.mp4?token=Ja3YaFk21c9Dx_zl1R2xEMa3V0SlKregF11XwuBkbjQ0l9Nxi0u6MQNJlqxZ0UGdFkoe3gKJWpTVIWL6tF79SmMPBNNeNpZhHMz75b6CNW-dTNVKM8m-imlRmM8XEd2x9gVstHvCOkHtaxXcWfIQoim7MGSPbFRJe3TTSh8ZEfhrrY73jFVMrZMfFaxfduQhC00470cgjYFs0Emhf0J4g96Hta7tRPcp5MNHljhGQ66QP08xNnLEsPlWIvvGa1cNCI2_e0V_SEb9ud-uLn2grHvbyx5-1jaIMY9ZsZQI6rxKzxiIS6PBM8FzsvNLWwN36CI_slzlw8tsDfOZfoCPUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رژیم صهیونیستی باز هم خواستار تخلیهٔ شهر صور شد
🔹
ارتش صهیونیستی دقایقی پیش برای ساکنان شهر صور در جنوب لبنان هشدار تخلیه صادر کرد و الجزیره هم از حملات توپخانه‌ای این رژیم به مناطقی در صور خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/440877" target="_blank">📅 10:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440876">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سخنگوی شهرداری تهران: با توجه به شرایط موجود در کشور، استفاده از مترو و BRT در هماهنگی با شورای شهر تهران همچنان رایگان خواهد بود.  @Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/440876" target="_blank">📅 10:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440875">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5b736132.mp4?token=T2PUQv9dSHV0DZx3NbajuYMrBAG_BwVAxKoEzlQxQVMCR0MXAgxc69osX8oQZqEd0qZS-yCry61vVPGThipSiM8y-T8HaJyZ_YhzhJ4MXi-kzaSRxTXGgJIk2pYXUbMxUdsYTqSl2vr2PL-2y55wJxTKGV43rLvswlJduiKfP8Umbt2S4Xh2I7X3yhPjBMkgT5aqlElYtUWuvVirz8ZG4QI2JH-F96hu9WllplWWbGszUXeF9HMZbqYXprQiUF4lieB8aVJGx1YYYAJeI9Q-Jgp9uHp7YtSuAzoSOCP3H3mVn_yVB4lBv-a6BHfVoxdLT-yXHmBU5-0y8cWk6hZZeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5b736132.mp4?token=T2PUQv9dSHV0DZx3NbajuYMrBAG_BwVAxKoEzlQxQVMCR0MXAgxc69osX8oQZqEd0qZS-yCry61vVPGThipSiM8y-T8HaJyZ_YhzhJ4MXi-kzaSRxTXGgJIk2pYXUbMxUdsYTqSl2vr2PL-2y55wJxTKGV43rLvswlJduiKfP8Umbt2S4Xh2I7X3yhPjBMkgT5aqlElYtUWuvVirz8ZG4QI2JH-F96hu9WllplWWbGszUXeF9HMZbqYXprQiUF4lieB8aVJGx1YYYAJeI9Q-Jgp9uHp7YtSuAzoSOCP3H3mVn_yVB4lBv-a6BHfVoxdLT-yXHmBU5-0y8cWk6hZZeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قوه‌قضائیه از توقیف بخشی از املاک علی کریمی خبر داد
🔹
قوه‌قضائیه اعلام کرد: با استعلامات صورت‌گرفته از سازمان ثبت اسناد و املاک، برخی از املاک علی کریمی که سعی در اختفای آن‌ها داشته، با کار پیچیدهٔ حقوقی-اطلاعاتی در استان البرز شناسایی شده و ۲ واحد تجاری…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440875" target="_blank">📅 10:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440874">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌ فدراسیون فوتبال: اقدام دولت آمریکا در ندادن ویزا کینه‌توزانه و کاملا سیاسی است
🔹
در آستانه آغاز جام جهانی، دولت آمریکا در ادامۀ اقدامات کینه‌توزانه خود علیه تیم ایران در تصمیمی غیرورزشی و البته کاملا سیاسی از صدور ویزای ارکان مهم مدیریتی و اداری تیم ملی…</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/440874" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440873">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxpK_yjjSXeERaZjDT7M2z19A4gjqcUfGX4ppg2fM6HGxwrs1bt3s0cin7I0zi41nxbmf8zUFNz6YjjSMOS7IAhvJ9qDR4Len0ZgneFo_XRs_0-dKa5N5lksGcw7LwIQXCzyd4IqIp5Z8TQYdO46i_qTb70Q3gFMnnintdPuO-rPJBf5gCMJZ0Oz2ytkP5Q-b-Yxey6Xa9C7GzbG7eInWSysCLW9F0zTI1mNIhrdYJ8hE6VbicYW0zIdQ55aHev-ERyblgL2i6JzbhipaXyixhHXqrTmcUTF1bfcwiuK8LJauvHX7mmBGv8gtPNOkgVV6jqQ2ICbXvnLd3YHsEq-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در صورت تداوم تجاوزات و شرارت‌ها، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/440873" target="_blank">📅 10:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440870">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c45693aeb.mp4?token=HkhH_7lFqaIfUktlHKACKL4SVE-0-CsaWULHa9KsaZ7KRXgCXdSvBAN-ivD4q2rGTuk9AtjzG-fVp8a1uNREQz3aCWgzvkOyoAKd9N6xNjH8FKEPH9QsvwiB4WlpzIkcyFTwlVglSQAjWJdiW1py3Wk7mJHWAvDzf2p1HY_v3Q2Vl_psW-Q4S5BNo6akmre_RqSr--jqbZRG6deGXUZeea9hwVzjxh7nj-xYWwC0qTAEMAj9Hv37OaGoJazhZ2MY7KhDiKZs6T1rvKwt13GjAjF_3Vr4d9cThrFKVslP55ogRizbIxry6tDae8zmgJfhKALLJCPH6azYkeD6IR6W7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c45693aeb.mp4?token=HkhH_7lFqaIfUktlHKACKL4SVE-0-CsaWULHa9KsaZ7KRXgCXdSvBAN-ivD4q2rGTuk9AtjzG-fVp8a1uNREQz3aCWgzvkOyoAKd9N6xNjH8FKEPH9QsvwiB4WlpzIkcyFTwlVglSQAjWJdiW1py3Wk7mJHWAvDzf2p1HY_v3Q2Vl_psW-Q4S5BNo6akmre_RqSr--jqbZRG6deGXUZeea9hwVzjxh7nj-xYWwC0qTAEMAj9Hv37OaGoJazhZ2MY7KhDiKZs6T1rvKwt13GjAjF_3Vr4d9cThrFKVslP55ogRizbIxry6tDae8zmgJfhKALLJCPH6azYkeD6IR6W7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش ترامپ به هو شدن در داخل و بیرون ورزشگاه: فکر می‌کنم تشویق شدم
🔹
حضور دونالد ترامپ رئیس‌جمهور آمریکا در بازی سوم فینال ان‌بی‌ای با واکنش منفی تماشاگران همراه شد. زمانی که تصویر ترامپ هنگام پخش سرود ملی آمریکا روی نمایشگر بزرگ سالن به‌نمایش درآمد، حاضران در ورزشگاه او را با صدای بلند «هو» کردند.
🔹
با این حال، ترامپ دراین‌باره به خبرنگاران گفت: واقعاً عالی بود. فکر می‌کنم بیشتر تشویق بود. خیلی بلند بود و بسیار پرشور.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/440870" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440869">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47eae22ebe.mp4?token=k5Yn3eT3xzCWEGXTOLmZFIefbrbj0CJyQKISch4EbO5ooe_0wsoIJkAwNhGfl3J_YGHLjLHM0JxSl2VQ_mMaoqcjJJc2zCe_LucU445PW10lgCmzsJ5piiUypiqtUOTOzrZEaT1XvX2KT-8YubNMH0GSa8of02cA3nrw1BSio1H6qAQVNnroBI4IYggEiLS5zyUcj_kG3uy-sZuNHTPr_DVg6ySgcyjY9V_uURD-sraDQS2H4GO0IH6ZUccNLD6GU5hsHqnA_FacVSTJiJycFyhOJRaP3tRMbV_8bfuykJ-EsuVLbE3RlCr9PKjJkzmy9NdYsInrrIh8M-GdE5Bd0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47eae22ebe.mp4?token=k5Yn3eT3xzCWEGXTOLmZFIefbrbj0CJyQKISch4EbO5ooe_0wsoIJkAwNhGfl3J_YGHLjLHM0JxSl2VQ_mMaoqcjJJc2zCe_LucU445PW10lgCmzsJ5piiUypiqtUOTOzrZEaT1XvX2KT-8YubNMH0GSa8of02cA3nrw1BSio1H6qAQVNnroBI4IYggEiLS5zyUcj_kG3uy-sZuNHTPr_DVg6ySgcyjY9V_uURD-sraDQS2H4GO0IH6ZUccNLD6GU5hsHqnA_FacVSTJiJycFyhOJRaP3tRMbV_8bfuykJ-EsuVLbE3RlCr9PKjJkzmy9NdYsInrrIh8M-GdE5Bd0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیلم دوربین مداربسته از درگیری خواهران منصوریان با مسئولان فدراسیون ووشو  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440869" target="_blank">📅 08:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440868">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
سقوط بالگرد نظامی آمریکا در نزدیکی تنگۀ هرمز
🔹
طبق گزارش نیویورک تایمز، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/440868" target="_blank">📅 08:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440867">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2030c628b3.mp4?token=SR7iOkm8EI4Zgrb6Dz1Eo92clrq6U9V7P5U0E4nmQrwkw6WEyW19QgtzbjLMEC_nh_UYzLnln5ACjaDn-bOtzueNqMI4JfBeao6_j1T10QMoVGQsv_XtageGnBV4WZDTK-msd7shNrFPt9AvzvY9RSxw_wHiDGqwemMXNRXf9aymLrlVTRVvdVYw0rm1FXDdGNs-b1xgH9kproaVUDwzSd2elbT1X2gZpUGKRUqOAzaDFKYTSRJpytjxdrO9f3kn2WiYPehTH6lmI4o9-SzXGwwRcEUc-ffkx20Gbq17MnVdCu12YFvDS5Dn0wBpFldKvHl9ohA1IrOBwNMUFuuyOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2030c628b3.mp4?token=SR7iOkm8EI4Zgrb6Dz1Eo92clrq6U9V7P5U0E4nmQrwkw6WEyW19QgtzbjLMEC_nh_UYzLnln5ACjaDn-bOtzueNqMI4JfBeao6_j1T10QMoVGQsv_XtageGnBV4WZDTK-msd7shNrFPt9AvzvY9RSxw_wHiDGqwemMXNRXf9aymLrlVTRVvdVYw0rm1FXDdGNs-b1xgH9kproaVUDwzSd2elbT1X2gZpUGKRUqOAzaDFKYTSRJpytjxdrO9f3kn2WiYPehTH6lmI4o9-SzXGwwRcEUc-ffkx20Gbq17MnVdCu12YFvDS5Dn0wBpFldKvHl9ohA1IrOBwNMUFuuyOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افزایش ۸۰ درصدی قیمت مواد شوینده از دی‌ماه تا الان
🔹
مواد شوینده در دی‌ پارسال ۵۰ درصد و اردیبهشت‌‌ امسال ۳۰ درصد گران شد.
🔹
چه عواملی باعث افزایش قیمت مواد شوینده می‌شود؟
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/440867" target="_blank">📅 08:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440866">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz0jsqR9VQ5yrWYvgjhWLNPv_zddZ5dmcfsN9pZRl1k3fpu7EM8yD20h_KChFk6pzUCnY_yZZRujiPXR9YKZwLxZk_K6b_ZtCwYZCPLSTeHL1mTFyiU2dn4Na9DVMojiGUFvhOhnQJkxy-7J8SIxYIJFIGVdPPz9nhSnJINLeDyeTRVUSiMBSAWR9_MKCKMGs63-vlevp1KinGw2SlQ_7j-0APb9J3uuHzJx06pObM3BLNcQOmcd1p_2bO8T8lxRTB28zUqVVd-TkAKbD2ivzvXEincBic62SSC-Ysi2SRE_kWZAv32g4PtIuR1YIB8FdMk0iJm3aqdOH6_B37CPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی کل سپاه: آفرین بر شما مداحان، شاعران و هنرمندان متعهد
🔹
۱۰۰ روز از درخشش بی‌نظیر ملت مؤمن و شجاع ایران می‌گذرد‌. بعثتی الهی که جهان را شگفت‌زده کرد و زورگویان مستکبر را در مقابل ارادۀ ملتی بصیر و مقاوم تسلیم کرد و ان‌شاءالله پاداش این ایستادگی بی‌مثال، گشایش و فرج برای بشریت و هموار شدن مسیر حاکمیت قسط و عدل بر جهان خواهد بود.
🔹
در این حماسۀ ماندگار، ستایش‌گران اهل بیت و هنرمندان متعهد، از ارکان اصلی حضور با نشاط و شورانگیز مردم بودند.
🔹
۲۲ ذی‌الحجه سالروز شهادت تجسم عشق و ایمان و منادی برجسته آزادی و عدالت و ولایت میثم تمار، فرصتی مغتنم برای تجلیل از این سربازان سلحشور سپاه امام زمان (عج) است.
🔹
آفرین بر شما مداحان، شاعران و هنرمندان متعهدی که در حماسۀ بعثت عظیم ملت ایران صمیمانه در کنار ملت خود بودید و عاشقانه پای آرمان‌های قائد شهیدمان ایستادید و شکوه و عظمت این قیام را دو چندان کردید.
🔹
حشر با حیدر کرار، امیرالمومین علی بن‌ابی طالب علیه‌السلام و جایگاهی چون میثم تمار نصیبتان باد.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/440866" target="_blank">📅 08:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440865">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شهردار نیویورک: ویزای یک‌روزه با روح جام‌جهانی تعارض دارد
🔹
کارشکنی دولت آمریکا علیه تیم‌های شرکت‌کننده در جام‌جهانی باعث شده تا زهران ممدانی، شهردار مسلمان نیویورک به سیاست‌های ترامپ انتقاد کند.
🔹
ممدانی در بخشی از صحبت‌هایش گفته، صدور ویزای یک‌روزه برای یک تیم (ایران) برای شرکت در جام‌جهانی با روح جام‌جهانی تعارض دارد.
🔸
هنوز جام‌جهانی آغاز نشده میزبانی آمریکا به دلیل کارشکنی‌ها و برخوردهای تحقیرآمیز زیرسوال رفته و به سوژۀ اول جام‌جهانی تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/440865" target="_blank">📅 08:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440864">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
سقوط بالگرد نظامی آمریکا در نزدیکی تنگۀ هرمز
🔹
طبق گزارش نیویورک تایمز، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/440864" target="_blank">📅 07:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440863">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_AjxRS0h4ZqXbhxzZ68KmCyhwu6Xf-fgXaWDdeLUnpljBPMZya1nLh7KA07afYzdlYK2zk2g9tAul8XkWvkpgK0sl1sSwJ_3Q4g30Te79PkmMqmkBNbzjpj-Hthd8dcR_fzSR5MRFNZcLfenrwxhcvX-jC2drHGI7xTg0er8ot3BE5wSNb_xlRI3ivHM14S4MgYB50jIsZ3egQbG5rnUfehjfH395nm35dyIozNQjNJRv5ui6D3p8dcGpD_nIvZnvmBkUtPocus_kCXcVWYbw8LEOzgAAUa0TO9aDRtdisJWjE8zoo8C_x_q6PwHXTShJKVNoIuLFKhUyox8Sc4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح آمریکا برای بستن راه‌های غیرمستقیم تأمین فناوری چین
🔹
قانونگذاران آمریکایی با هدف جلوگیری از دسترسی غیرمستقیم شرکت‌های چینی به تراشه‌های پیشرفته، خواستار تشدید نظارت و گسترش محدودیت‌های صادراتی شدند.
🔹
نمایندگان کنگرۀ آمریکا معتقدند برخی شرکت‌های چینی می‌توانند با استفاده از واحدهای ثبت‌شده در خارج از چین، محدودیت‌های صادراتی واشنگتن را دور بزنند و به فناوری‌های پیشرفتۀ موردنیاز برای توسعۀ سامانه‌های هوش‌مصنوعی دسترسی پیدا کنند.
🔹
این درخواست در حالی مطرح شده که دولت آمریکا طی سال‌های اخیر مجموعه‌ای از محدودیت‌های صادراتی را برای جلوگیری از انتقال فناوری‌های حساس نیمه‌رسانا به چین اعمال کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/440863" target="_blank">📅 07:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440862">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رگبار، رعدوبرق و وزش‌باد شدید در برخی مناطق کشور
🔹
هواشناسی: در شمال استان‌های آذربایجان‌غربی و آذربایجان‌شرقی، اردبیل، شمال زنجان، استان‌های ساحلی دریای خزر، ارتفاعات و دامنۀ البرز مرکزی در استان‌های قزوین، البرز و تهران، شمال سمنان، خراسان‌شمالی و شمال خراسان‌رضوی در بعضی ساعت‌ها ابرناک، رگبار و رعدوبرق و گاهی وزش‌باد شدید موقت پیش‌بینی می‌شود.
🔹
در شمال شرق، شرق، جنوب و جنوب‌غرب در بعضی از ساعت‌ها وزش‌باد شدید و احتمال خیزش گردوخاک دور از انتظار نیست.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/440862" target="_blank">📅 07:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440861">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ادارات البرز از امروز با ۵۰ درصد ظرفیت فعالیت می‌کنند
🔹
با اعلام استانداری البرز، با هدف تسهیل شرایط کاری گروه‌های دارای شرایط ویژه، فعالیت کلیۀ وزارتخانه‌ها، سازمان‌ها و دستگاه‌های اجرایی استان البرز تا اطلاع ثانوی با حداقل ۵۰ درصد کارکنان و به‌صورت حضوری خواهد بود.
اولویت دورکاری با چه کسانی است؟
🔸
افراد دارای معلولیت
🔸
بانوان به‌ویژه بانوان باردار یا دارای فرزند معلول یا فرزند شش ساله و کمتر
🔸
کارکنان دارای بیماری‌های خاص
فعالیت‌ بانک‌ها چگونه است؟
🔹
تمامی شعب بانک‌ها فعال می‌باشد.
🔹
مدیران شعب می‌توانند با حداقل ۵۰ درصد نیروهای شاغل در شعب، روند خدمت‌رسانی را ادامه دهند.
چه کسانی از این بخشنامه مستثنی هستند؟
🔸
تمامی رده‌های مدیریتی استان
🔸
واحدهای عملیاتی دستگاه‌های خدمات‌رسان و شهرداری‌ها
🔸
مراکز درمانی، نهادهای نظامی، انتظامی و امنیتی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/440861" target="_blank">📅 06:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440860">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPcMC5R9TCIr644V-0l-E_NdyfrXSn2hIePAPiBkhg0t3YBJR4VaoejWhHKxceGzfxGx4HDReTaDOzdHCrkBMYsRjnXeSnCo1DMxR0ndjNC817UbQYsMHNTsk2FjAksi_Q1UUtRpTmvaqASBvNFL4QZEfttdEnl45p-BCE2cGcsVgTFIrqclVmSonBK_-vUJPQUDxzMFLuGqotW3iGhLnzRI1H9AaNI5CqFwhy8HBAvaMA6w4SVciK27iOAsBCpmjc0rxHSmeEBp29QOtvlTcS-dnwPPWC7CrqHl6r8WJQ-YY06Dsjd7FvcdU5AO2_0OwEncErdCNDtQa-jYQqnBLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سوپر ماریو گلکسی» اولین فیلم میلیارد دلاری سال شد
🔹
در حالی که هالیوود هنوز در انتظار نخستین ابرموفقیت تجاری سال ۲۰۲۶ بود، «سوپر ماریو گلکسی» با عبور از مرز یک میلیارد دلار فروش جهانی، نه‌تنها این عنوان را از آن خود کرد، بلکه جایگاه مجموعه «ماریو» را در میان پردرآمدترین فرانچایزهای انیمیشنی تاریخ تثبیت کرد.
🔹
این فیلم که محصول مشترک استودیوهای یونیورسال پیکچرز، ایلومینیشن و نینتندو است، پس از پایان اکران آخر هفته اخیر به فروش ۴۲۸.۵ میلیون دلار در آمریکای شمالی و ۵۷۱.۵ میلیون دلار در بازارهای بین‌المللی دست یافت و مجموع فروش جهانی خود را از یک میلیارد دلار فراتر برد.
🔹
فرانچایز «سوپر ماریو» یکی از موفق‌ترین و پرفروش‌ترین مجموعه‌های سرگرمی در تاریخ جهان است.
🔹
ماجرای این شخصیت نمادین در سال ۱۹۸۱ با بازی «دانکی کونگ» آغاز شد، جایی که او با نام «جامپمن» به عنوان یک قهرمان ظاهر شد تا یک گوریل بزرگ را شکست دهد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/440860" target="_blank">📅 05:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440859">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65515e97a2.mp4?token=hDdf7rf4HnsQwwQj_ePFsNn6yYtFBwHQwD4G5DsBWLg3qRIzoDO1lJPHStTi-EiBVusv4jQ9JxhtFsD1UpNfR1TS--STk8cM__8Xdy9dyc7ursU0JrgLVr6vcs5bIQwbrJLgt6K-yFG7VrluJc2ChMrEvEwwQgE5P0ONGoHKUKw6eEYPi2ofab_T045EnJYVF8jJ6--oNLJ_CQbSyLM5hLJFJyvFGsm_zhOdHdvDJuGBZMTaEtNxmaHYhg4uKl0-WdY7pRFXYHM5X0q5oC4VebAPNt7T_tpvk4bcHSI43hH2AqKQo6vkqdtoi9LuY6mLy3ZvL9RsQp1k2VoW2WUk_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65515e97a2.mp4?token=hDdf7rf4HnsQwwQj_ePFsNn6yYtFBwHQwD4G5DsBWLg3qRIzoDO1lJPHStTi-EiBVusv4jQ9JxhtFsD1UpNfR1TS--STk8cM__8Xdy9dyc7ursU0JrgLVr6vcs5bIQwbrJLgt6K-yFG7VrluJc2ChMrEvEwwQgE5P0ONGoHKUKw6eEYPi2ofab_T045EnJYVF8jJ6--oNLJ_CQbSyLM5hLJFJyvFGsm_zhOdHdvDJuGBZMTaEtNxmaHYhg4uKl0-WdY7pRFXYHM5X0q5oC4VebAPNt7T_tpvk4bcHSI43hH2AqKQo6vkqdtoi9LuY6mLy3ZvL9RsQp1k2VoW2WUk_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از پدر و مادرتان برای خدا حساب ببرید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/440859" target="_blank">📅 03:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440858">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بانویی که تعمیر پرچم در خیابان را نذر امام زمان(عج) کرده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/440858" target="_blank">📅 03:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440857">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انصراف تیم ملی فوتبال امید از بازی دوستانه با بحرین
🔹
تیم ملی فوتبال امید ایران که این روزها اردوی آماده‌سازی خود را در آنتالیای ترکیه برگزار می‌کند، از شرکت در مسابقات دوستانه با حضور بحرین و چند تیم دیگر انصراف داد.
🔹
گفته می‌شود این تصمیم در واکنش به مواضع و اقدامات برخی کشورهای حاضر در این تورنمنت علیه ایران گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/440857" target="_blank">📅 02:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440856">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVoM3kt6KNiizgMLJlq3fI-1Jy4USllI-HGB2gfWoIMwnacXOHv6JoVRmCp2gZq_c4DQnBBlYd0hGr5jDhPfck9T8SVx6QcIFWR6FskDPbD0WgkfTSU9nJqhfMyOBqG8G0PC8IqA_YQ7InJWow9ZattqwOMl3j4RfUEU4IxcZshA11_kPdCNQ2O8XOkZNf94bx6wVG42NBOblnDH_7uwRrv7uS-i7BSTEFWt2EDfPn8NOWw8CSulcvy0SibRH0Z30qUOgUwHmQFflNfEI5JmDgpNGer0a4GHfyAONjmrGxCCDz8YC_euw8OeIIfThFhRox4URXojWlPs4b8LV6LLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی داور افتتاحیه جام بیست‌وسوم
🔹
ویلتون پریرا سامپایو، داور برزیلی قضاوت افتتاحیۀ جام‌جهانی ۲۰۲۶ که از ساعت ۲۲:۳۰ پنجشنبه بین مکزیک و آفریقای جنوبی برگزار می‌شود را برعهده گرفت.
@Sportfars</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/440856" target="_blank">📅 01:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440855">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دو شهید و ۱۰ زخمی در حملۀ صهیونیست‌ها به شهر مروانیۀ لبنان
🔹
وزارت بهداشت لبنان: در حملۀ هوایی رژیم‌صهیونیستی به شهر مروانیه در جنوب این کشور، دو نفر از جمله یک کودک شهید و ۱۰ نفر دیگر زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/440855" target="_blank">📅 01:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440849">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cG5Vl6tPPBl24xgZDgetfgn0-_tNO6JP-30tDntI5EEbhQ-KtJ2_iTSzcCS2jcYOM_Jkd4mRUu8L4LVNx4wiA8P704LChCKRZ8TWtp92SqeZZgT9OdC_qZ5qzAJpugqdeLSU_PzgtEwcU_qkzDBCaSwqIXxx426cUhfSKE8vtOZzktRp0lOdmw5GJcS-5Ur_VrrC_kuGz7Tq25bxaDcKg1VtPvoInxQNdQIQskXO_9MUPyRIz7A4bkRQxfJX2L-yRbQe7miN7yifQ3qyBBypSM-rdf6inqTvl_DvcsZctYRmClW67pHsvd8IM0m2NKoaD9Ey8NyGU2Xq1Wwc-yyGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iq33YrChoPVv1ReDVBLcH19REjnrsn1vA_XAeTkKTNN3Vn_qCW9SXAadGY_ZAXpAVCM7K3uLdZoyQgk1rFW1JBnwOupiUK_Kjy0GoWI_0t_eGiK76tmUzmh0MqoWsOYl01UNObKAzCjLT4f1F5f_MkOO8TF2d2KiMeQTsPr0CDrwM2VyDJqlYKbg4v7AcyS1wEdyHJaxph8B7_JuFbgxKlBZB_dpIlQu46TtefF8ATZ5PnIDqC1IYmb1M8Dy5NTKqDGm2c87uwSqrRD3LuPaWdBfVOirspsXiSE1XkpAuOAt6sWAUwVdBExdJ7ZP7r_lYCjYjpXdmQeFUKE15ZR-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5L2XkrMBYyiUOD2K9gwjNvKuRTgEIPjMSk5G8HH3rQoHpVuKimHp8STGtlrCkGANFZ_Kfi-MnWqKmHC2GUXLSar115LfD16Q5mK7nd_2xQ9C0t80s86cX3xQfZ3EW111-YeLmyeTRj0L6PSC94sxIqC2rF1OidVo-XJhiw-oKlNnpC2mB0Vu5sQuVz-eBt15JoQrz45ivVFg7gdgj1zg_W4OdfmpfvA8EpacQpGy6WlsBqPZeuRTQMkMSVFgOUecO9wBO9LNcNuwYRbLhy-VPCXsfx4JUyAWDrfApQ2RJk3GDTCzmJerQccfPD3dHJ_n7Ug0DshGJ_FvSN29kT7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1auoFXWq5nMLPtuizv58mSYdwgPgvudsL67XQWoZOiqXiQy697-sZ0W671NCm8ltzL7un1sCN9zkP7lwubPoE7zvYW9WVDe2tsPtBYmNziCDPu_t04L-ms5AU1FxNYMgpsJe4jg9NLOARSkp09-Pbmlz2wq6GNTgN02eNqO7Cx8mA68PPZ3Z1Gg37Xued5XdRXVgdKj-eHANY9FdKM47YP-T-FBMAz6bWTug8IfymDnC1ODr0FKbSKjjUc4xDtdjJTQSLrZIS8RNpzn_Haz8onp6QbpNJtmrrvOVh5Bzd8jKd0T0U_0R-BsyHyDgGT5XVKjjZzlvN7iQQJkUtaFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a55EHGVRxgI6VShp5mgMd9-lZm5hMO9hsOKZPoSSQEEENMH4jORwEe8xk1kZ3em3dV2xCTa2DlJlTnRv9dN7O3R7JhTSzZYzWdiuysQeBr8IvVoq-agqmHzNx2aP0TozW5IrtJNy2y-sHA4XfIzVW1gwuLcClx5_dtEYAdnecYUJ1sHPDc3UK5I5lPDTiztn_fdPxTmK0I-rTDNStk6G32V9iTEnG-C70k_gB_YE09NyJQ1-9h1YlPRB20gTKsORN6RaIC3OaXYIIzoZwtdnW2KfLTCQJtMnhKBEps7cLIHmuXOFD5x7nkO6dmxn0AKQk8hfXfAT-xcI6QdbACtXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3sR6fX4cqp3GYFD-_KZEIHgsveBUJTJlZShnQTQiJJOjRi7aEmywlMl3YC61IEYi4odLWIKSZt_Zkvip-ehEEgCWTkkuECe5cYCd7vHc_2e60o6XVgPm9yNASRbkABC1E1A9GGlLpAJ4UeczooEEwpTa73V-ma59galXEUV5rhZ06zv5VqpH503w7sN_z6oBB-6G_4eO2EA0B57A1UqKTXNB1WLdgJqfi_VOLEQve5FmFLD7uTqlzwfLSwyy-njBqMROCS4HnzpfYcHPmGNuGWNZTSQiW8viMM8K694-HY2YByY5ccDzAd-X2OjqSs8u7U0_pgNYxlyGl-jSOgXRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۱۹ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/440849" target="_blank">📅 01:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440839">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBskTveuduqiIPM3QS-Eam6J9ufhzOo2zRfam7MRlRt3KQGP-rDOTaDes29e_Z8DTYUWSJFJRfbilaILt2AX9DwTUWGAgzYI7SFaP8fnTv1oYN8SRqGkmIJJUbhZIwz1kC4QdqppZeH3ymzZuQcRbXRFNwYv6iylgYG_GVW9OwZfzkDdWhxNN9lwB6PM8Ibikdeb_1D4Lpg3x7s0UyTay3eZC2DclVfz3MR9Odbr8ZqqtFXlUzkD2tz-6ErmRcjuAn0nbQ7l6S__7TXv-4Z4Bczqwl3qduuMxYp3n-oK7kyX9rSa4MAtHviLBPt2WBkcjlZDtA5ogdW7213-DyOieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dheJq2bzTrdx0pwbEnLG5wCz0w7-nXJRMO-IHoyEg42jF5Qu1fQuEttBMeABxaqOfI38XLVUzpAB9ox8q4K2oeZnn8JqpWDWIi65I_XR2RcqQxwCK4FgY5-MaZTwSSK1d4qDLj0HXZtLiMhOHQ5GvN_iPh-8n6X_14YeHSGEwWsTSV6s7QfaemwDRXbAGN-MC7zkhTtRLad7KHGoyB4YrMH-N76lTppgMwbJVkRnkvHUjh4G7aDx2U6uV501U9QAj5XJCzKh2g_W6UBFavBclAS24KpGGeFh81GRVjXbOIhCxfvKWHjxlouwhlEdFr_9gTQfFSElgRsAU3EvdJ9BvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAaxdalgoye4Ubj8tpeY3FqVPXGzrL2qWIYXfMiL0o38UTteCWlzHKdklqg62PlzK24_hzoN4_mP-5zx9Vmfzs2_hnCNdApo48uPu2Wci62MDzKLL5_Ba9ZoMWNTsBwFULgImglwANRyOIMXm-HNC5vSQGsqGcGP0xlgg8TQrV8EVuz6I3uP9GgXAHlFNrPr6Dt9cjWzTR85h--YUKPrb_ersUddFnZkDRFzaFvk5pd59pc1MqR3FOzwFAWKc5_NLq_v4TEmawFH6Xx4Zz_Q0pE10w6b-LybJMpb3vooQ0ReN9OWieSNjwON_c-He0RarYWWj5UjjxzrapbuNMYTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nFpBhWFp1AJxFD6-4gxBjd7b1dEZLuDqI7-lVJ3ajOatPs1rrXPPFQ2SEKVQuBOd4GgiCoRMsPomx0RAGRbSgTgCvtdB88eFXSeW-ky7wxdnB5zVFuBqsCEKM5ml7HmZicb3rIUDuuWMwQbkV5bxkykpDBgMxxNp1GVF2IoVcm_s9H9YosTz5tFc3L5zxxCzdRU4k_GppOktChWu2DMqiucDXIjhiIW1q1lxocyYT-Kq8LDGrFHK57FNE5T9eBb5YM2mVcYmyNUEjCHYflfY0oyQDKCtbAA47S02P5lanwktigxtwqVeLTotmEkYH-kM5yyNhO9IcWbILcc0CMvqLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CafUiww7SE9TcwzIKChRPQIwviV_nFJ9OdqF6QrV8nxZP77f76hoyZ969BE4zgPfhCRmXiVMyXV9JqTchU384cV0H8D_wKRhXmOd90Z8h2YXJ43rLEGhylp1RjfLAPqNUzI28hKEeQWchUVB4Ld8Wg-crvKE8n9I17t471oZGvzG5Gd1c2u2JiilBB4XB1Dk-qAev-vxM1W01hvd07tuoB0vWowgncEER8hNHHw-foY-9Ot7CGQVKo6yFONHK91T7DW54sgKA-0ko2P-1QQxWKaBqpDPdr7fdHYlA6O_5c8zmvkEz9vegNGpsxk7wTDPpCexGLwl0J44EJ1P7PEUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNQxqUr7EwsH5Su9qWXw37QQedV8eH_w8s67x6ccMmLEFAIRRLtC21mN01BaPBQ7Nv1mUJBYSMuV0wkeQprf_40JCpD1efpWBGQ25QJ4sLlAqU09fe0cGREZcuYSvRP46jHtf2gjkiwpLYck8J52hXcN47Nm409otuiJHyOx4oV2x-MgkaDVESB6R4RCmHyP18uPbXB_3TMIjJmv1HadEJHLZk5uLimn53FvvSAq64O15hFdBCnlQ5GSB17j7Wh7JUFO3sl7wj3RiKUo48Wtgj5hQRMXNg7XHZwERRFfwSGvkKaiDNPvwNE-9_ykt6h20D77m--NGb0t0zAI0sY56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBMtSYGnwU12XwRb3OQvLmkdhr2-cA4QMWGZjnz0BqlUe7-8ToOW7dAPaDYXmyV-cTrkbEz9JX04DdK4O1OiHr4DCTv9dRGVtLXR9vA3Rdw5St7qA14PRe-KGv5piHXNhgKEDyngim0iQM2oW46eOv10gyZYm3KfPV4QuEXywdScYvOam08IeJUYcpEuJKLC_VoQLwkhtMl539GqLSKFN2_9Ql3URNC2-0pW9JMZZrhHpQIopk80ryEaxcw5Uy0BgYJvYHB2Kt6EXrAmbcJwrCPKYRf2zztyGN_B-icR3xPqk70-4dlIM1WFjLq2yxwyn1LfDMD48oWIlbGZszHISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhaU2-l4RigxY2bjX4WN3qT50QdIqJQw9RrCS6b-tiHLCeUKdrLffDFirUf25PKsk55bBXvY__zYVg0Rx-OXsy7C5MR0mDC0t7nJF-KfP-tQ-3Xk__AyJ_3DH6tzsxYgS6uz7z8P6a5KmJ6adL3lSVjDsCTui2LSL8m487iig6k-WZmHh5a6NxiNZdTTWAPK1SqC12j1Q-WHs0lXkcE9mfCjNBD1Zjtado0jvUzpeqWNIMhY8Mbzq8YIk0mWR9wgN7uUa1SWn0nmC4Rpqbm8vaClMpylw7JWhUnevFShV5u5oJj4gKsI_PQnzaPHoPKuVGPIblhyg8o7UMkRVjoK6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4_aS-0_6yl3mf0r0axTq52W9lGe6Ob-FjiV1LMNd5Sqb_qIwog2PbHS_VoXq2wwu6bbHouHGcTPt9TXT5Bfyh6F6VXK6daBqEkaznBlIMuOmXPyvYlkT83REyHYkKRWxeA-kvkLxcrdM-HEgaYaB6gi46jMhbw9rKi1OW8oSnucFc9CeSfTssxgff8QYWEwjcJkBIs-KF_W_lD7wKC6SaVBkH1cSm94aHPR6kDTPD1gZoPGO1vVnH-dOm8fZDP0IXDoKwlDv8BsQ9ffxC820uL8aAN65eIC-ZldToRcqiA0vmtTMv2vBBB5fKnXHTtc0UHaRkhlGYHZKusyqH8BIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_A7JXmorJ4laGcOHib57OjUXGM3sX6uyU8Hh9iHF2DGLX62yVAW2dEAhxWz4DkQgf0_zC7MT6sjbhDQgBXaHMFWT4Z6Vo-0xpDCSbvGb5U2joTSnMWxiIszsrtfVp0z-TO-mQXhbseJN-d29Aez9GB-8cuBlPnWK38Wui9vIMgm4oxszzeTKFdFmJWVN9Yo2I3LukJ9iBbAMZ_Vrpl3uPCgHwMQMC8s6F89eqr3q1zD4D8pfmnBG6jSj7NzoiYA8POqxM7IX13PQ6bYoSi-LkPyCA8nyqMaOhHfgOSZIAyzqRnpHMNHbTXlrOK2y_5x-tHO6KTX81TXE1bqhilU4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/440839" target="_blank">📅 01:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440838">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7e4651d4.mp4?token=lCiEzbAOnJNyc9bytMUAP37QRJVpCozv4Qj9uQwxuW8M3z7qqcDF5QdoHIrWSJh623PuZJORPsA0vbNpUh8Xx_YF8TUu0PCffhRSkpN3GrbqVzp-7LBCMD4rh04Idf6EFcbArb19uPCTje2rHJFlSWnfubjYeeTeg2Y2u8s7VCjqXmVMvqdxYZtJDfFuOtjjKfg321r4ECpqjdOCmbgTv4Gt9cT71ZIoptUPO5AfJ3mqvjeP9JizxVq1X63G_EB313Px2NFjcHUrvJwI3RqTtcj6M5YOAXLX6RvsVtwlw2lzPr2jMT-S7YwRivs4NPsEof6OVEw7NmVK30u7LQPIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7e4651d4.mp4?token=lCiEzbAOnJNyc9bytMUAP37QRJVpCozv4Qj9uQwxuW8M3z7qqcDF5QdoHIrWSJh623PuZJORPsA0vbNpUh8Xx_YF8TUu0PCffhRSkpN3GrbqVzp-7LBCMD4rh04Idf6EFcbArb19uPCTje2rHJFlSWnfubjYeeTeg2Y2u8s7VCjqXmVMvqdxYZtJDfFuOtjjKfg321r4ECpqjdOCmbgTv4Gt9cT71ZIoptUPO5AfJ3mqvjeP9JizxVq1X63G_EB313Px2NFjcHUrvJwI3RqTtcj6M5YOAXLX6RvsVtwlw2lzPr2jMT-S7YwRivs4NPsEof6OVEw7NmVK30u7LQPIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بقائی: افتخار به دزدی اموال ایرانیان شرم‌آور است
🔹
سخنگوی وزارت خارجه با انتشار ویدئویی از اظهارات وزیر خزانه‌داری آمریکا که با افتخار از سرقت اموال متعلق به ایران صحبت می‌کند، با اشاره به فرازی از نمایشنامۀ «مکبث» نوشت: اکنون او درمی‌یابد که جاه و مقامش بر اندامش زار می‌زند؛ همچون جامهٔ غولی بلندبالا بر تنِ دزدی فرومایه و کوتوله.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/440838" target="_blank">📅 01:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440837">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">زمین‌لرزۀ ۵ ریشتری بخش‌هایی از استان هرمزگان را لرزاند
🔹
زلزله‌ای به بزرگی ۵ ریشتر و در عمق ۲۲ کیلومتری زمین، منطقۀ سرگزاحمدی در شمال هرمزگان را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/440837" target="_blank">📅 01:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440836">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olZ90u1XiHHhYrFoZv2OHc1x3U2bNvp6XXKq_TfBJlNcbxA4HToMNCpNR7bcwb-UtYblxWBlv7DI078baSS1mLDjsAmTUGYQvF7uzqLdePHXU_iz4Qi3D5QynEIHGc6nJI7amdFlIg_dVBQRsW7Ol1aL-vJJMq5xkAuNO8KgITvqL4lK52NNkeyDFAelTj4ntgl6IC_hwmdBxQPARVga8helHodmYT0hyKfm17v1mfRl3VJ4WKBVo1LgicjTjBbMq4MIgZoU_4Bgy1Bqw2O1nQxm9bfQxp7muHWMEtthh-Tb9G0gy01pw-7rAxlrfi6gvQRUF9b7pUC5GCvdNouXMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط و نشان ایران دربارۀ مذاکرات با آمریکا
🔹
شبکۀ الجزیره شامگاه امروز دوشنبه به نقل از یک مقام ایرانی گزارش داد که آمریکا تغییراتی در پیش‌نویس تفاهم‌نامه ایجاد کرده و این مسئله قابل پذیرش نیست.
🔹
وی همچنین به طرف آمریکایی هشدار داد که هرگونه نقض آتش‌بس می‌تواند بر مذاکرات تأثیر بگذارد و ایران به‌صورت جدی با آن برخورد خواهد کرد.
🔹
این مقام که اشاره‌ای به نامش نشده، تاکید کرد اگر آمریکا پول‌های بلوکه شده ایران را آزاد نکند و به تحریم‌ها پایان ندهد، هیچ توافقی حاصل نخواهد شد.
🔹
وی در پایان گفت که برقراری ثبات و امنیت در منطقه فقط با وجود یک سازوکار بازدارندۀ واقعی در برابر تجاوزات محقق خواهد شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/440836" target="_blank">📅 00:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440835">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae82c887e8.mp4?token=pN2nIUinWQnIlVk7XE4nlMtQu-MLSLNL9FKJ6rKpgp7yCPB9rHg22f9eMVtdIppiGpmH8vEiF2ZGqXSO6yyX2l7thyn_dI4vOYVi3f2Y_EyCyHbEsdhcP2C5jVJPDCo8xTYACg4ZH-5eZf5Dm7-BrdejTs-I2wRAKPzQo_YlPKVuBLM9AgE7uh_vjyen6BBCJk70zsqhvrnwl6BcZ0iJrL-3GNPPw7W7T3g_kvBSchiWs2qU7aFI2g7lR03xkHZg_I9miJyaqkQm9BfSRUZ1JNUVmuk_YHlRbVi5dRaLEckzcnezAGnTjHrrI5VcmXXj8b8IY1bhpHHpLgShOFUxtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae82c887e8.mp4?token=pN2nIUinWQnIlVk7XE4nlMtQu-MLSLNL9FKJ6rKpgp7yCPB9rHg22f9eMVtdIppiGpmH8vEiF2ZGqXSO6yyX2l7thyn_dI4vOYVi3f2Y_EyCyHbEsdhcP2C5jVJPDCo8xTYACg4ZH-5eZf5Dm7-BrdejTs-I2wRAKPzQo_YlPKVuBLM9AgE7uh_vjyen6BBCJk70zsqhvrnwl6BcZ0iJrL-3GNPPw7W7T3g_kvBSchiWs2qU7aFI2g7lR03xkHZg_I9miJyaqkQm9BfSRUZ1JNUVmuk_YHlRbVi5dRaLEckzcnezAGnTjHrrI5VcmXXj8b8IY1bhpHHpLgShOFUxtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا خوزستان؛ ۱۰۰ شب حضور، ۱۰۰ شب ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/440835" target="_blank">📅 00:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440834">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کشف تجهیزات پشتیبان هدایت جنگنده‌های صهیونیستی در جنگل‌های تنکابن
🔹
مجموعه‌ای از تجهیزات فنی و سامانه‌های زمین‌پایۀ مورد استفاده در پشتیبانی و هدایت جنگنده‌های مهاجم، در ارتفاعات جنگلی شهرستان تنکابن در استان مازندران کشف و جمع‌آوری شد.
🔹
این تجهیزات در یکی از مسیرهای اصلی ورود جنگنده‌های دشمن به حریم هوایی پایتخت مستقر بوده‌اند.
🔹
این منطقه در جریان «جنگ رمضان» یکی از کریدورهای اصلی ورود جنگنده‌های اسرائیلی برای اجرای حملات علیه تهران و مناطق شمالی کشور محسوب می‌شد.
@Farsna
ـ
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/440834" target="_blank">📅 00:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440833">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">۵ شهید و ۸ زخمی در حملۀ صهیونیست‌ها به شهر صور لبنان
🔹
وزارت بهداشت لبنان اعلام کرد در نتیجۀ حملات هوایی رژیم صهیونیستی به شهر صور در جنوب این کشور، ۵ لبنانی به شهادت رسیده و ۸ نفر نیز زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/440833" target="_blank">📅 00:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440832">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBtJFch8rw1uXT3EOQ0fLVvhTxk4BbAERNe1deMOeDAIEV0nML-C96cvHpcppFVxvySsBYS1kcR6AMioxTULkeD4SEmjzm8uW166cEiHrizMhMfb8txaD--PFqmXlrc_HBr0c0zuJLkZbS0VC4ZXuPuSnUYJnO-pOISwJTAoULqSYYyLynKWHr-aYaGDdnaZhqs_r2kl3ctLGe-p1uktnZA7DfBFJ5H8RbH4uWQJvdrA5yWPB43rK6S0C8gmn78CIf6hJaOvPHEGbHRotUPdxodMEmTUv8rQFMLC1VrJffiRzfyLxnhJ2Gd3bXhrISD8jpj0vp8WULcYz2ZvnD17Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
فرمانده هوافضا: حضور در خیابان را تا زمانی که رهبری اراده می‌کنند حفظ کنید
🔹
باید با پیوند زدن «میدان، خیابان و دیپلماسی» عزت و اقتدار را برای ایران و ملت‌های آزاده فراهم کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/440832" target="_blank">📅 00:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440831">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da8c2c141.mp4?token=tf-WdP8dOZW5SD_wQH9OdDQ7PFYtLakOsYVTxCS5HfcXyEbpYL2lUABRNVgsmyzvg4snpjD7nLq6Pm0g2MeO3fbrKh8-DeSuMuBlfw8CFO_sZtnu7GrkPl91sb9h1f569yvLNhd4Df8r2WEv0Nzl4yTIDrsivdwFE2NziopM7_KLGLdlp9KW3pQRHEgnpyDjgeKS5_SLEUrtgHrScaW6RkZ70KNO41lS5iKqS7KYI12g-iwB8VRj7uEEaWHuGvtxOqz0oIODM0bEKnGNXcy1YPd_J5PEPtvYgFtACS-Pt_lwsvg8Gmr7_8fwl8CE1cSRNOeDlGNOOkVbvuHesCA7gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da8c2c141.mp4?token=tf-WdP8dOZW5SD_wQH9OdDQ7PFYtLakOsYVTxCS5HfcXyEbpYL2lUABRNVgsmyzvg4snpjD7nLq6Pm0g2MeO3fbrKh8-DeSuMuBlfw8CFO_sZtnu7GrkPl91sb9h1f569yvLNhd4Df8r2WEv0Nzl4yTIDrsivdwFE2NziopM7_KLGLdlp9KW3pQRHEgnpyDjgeKS5_SLEUrtgHrScaW6RkZ70KNO41lS5iKqS7KYI12g-iwB8VRj7uEEaWHuGvtxOqz0oIODM0bEKnGNXcy1YPd_J5PEPtvYgFtACS-Pt_lwsvg8Gmr7_8fwl8CE1cSRNOeDlGNOOkVbvuHesCA7gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس صداوسیما: سرمایه‌دارانی که با امکانات کشور در امارات سرمایه‌گذاری کرده‌اند باید این سرمایه‌ها را بازگردانند یا اموالشان توقیف شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/440831" target="_blank">📅 00:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440830">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
برخی منابع از حملۀ پهپادی یمن به اراضی اشغالی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/440830" target="_blank">📅 00:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440829">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd2299f3a.mp4?token=tYuZNiZWCEaHv0CSy2WvVXeYsVtpVAD-YNNE3AllW3tcuN7avwFt_PZoYD2reahr2bdRsLYdtMTfz_jlr073lAr6jDtnbvR7et5Q689PHut49cGVPsQk0qzTwyi109bP38ltiRjJvsdVWNHG8iQQDcQQ5KY7MFIn7I1n3Au4GbTNerE1--whQKEIETpS1e7WzA7sBl9l4qEKBFpyKoWPGuPuQaJsGaOgEyEfyucENjzOKAuGQhBD4-qBdFqwqZIzHVndnktMk4YCTF5Z7kxzn0X0LwqGgHZfO9YEQZbJtpJKLX94ZFZ3e9FY0tieg6AiFncHvRE2_Y4O_L6WzKoK4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd2299f3a.mp4?token=tYuZNiZWCEaHv0CSy2WvVXeYsVtpVAD-YNNE3AllW3tcuN7avwFt_PZoYD2reahr2bdRsLYdtMTfz_jlr073lAr6jDtnbvR7et5Q689PHut49cGVPsQk0qzTwyi109bP38ltiRjJvsdVWNHG8iQQDcQQ5KY7MFIn7I1n3Au4GbTNerE1--whQKEIETpS1e7WzA7sBl9l4qEKBFpyKoWPGuPuQaJsGaOgEyEfyucENjzOKAuGQhBD4-qBdFqwqZIzHVndnktMk4YCTF5Z7kxzn0X0LwqGgHZfO9YEQZbJtpJKLX94ZFZ3e9FY0tieg6AiFncHvRE2_Y4O_L6WzKoK4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«می‌مانیم پای کار وطن» شعار صدمین شب تجمعات میدان انقلاب تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/440829" target="_blank">📅 23:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440828">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfLapd-0FKoTbXyXLxg3eys1dPiEcx0tFu07uKdgCyKropjdTuIlMGFGSaj26URwdkK9IZB-kHAbzRTn2hnYbGMBrtLLoAkffUbW1xFTJqCgIqtU5euncTfnXYppEDKAkGe7iq9Jj1cB42URyYFdrrYLWqop6MwlPH171O0CsPozB37HYoLq6ZGY_jVVOEjumYE3Y97aLfrBAOE1MiYPQDgIepYVrCJ2GgaipazezUZb_zxDtkE7Xj-KEciu0YCUgDKMecKOJaNbfKjEr544PLI-snrP5XbCDBQdgLQ8v2_KtUdpPKh3wyTZCpofPWOIWJ-9sk3GTt-L4gRI-Ztj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو کنگره خواستار تحقیقات درباره حمله اسرائیل به کشتی آمریکایی شد
🔹
توماس مسی، نماینده جمهوری‌خواه کنگره آمریکا، خواستار تحقیقات جدید درباره حمله اسرائیل به کشتی یواس‌اس لیبرتی شده و خواستار به رسمیت شناخته شدن بازماندگان و کشته‌شدگان این حادثه شده است، مسئله‌ای که به گفته او ۵۹ سال است معطل مانده است.
🔸
به گزارش الجزیره، امروز سالگرد این حمله است و در ۸ ژوئن ۱۹۶۷ جنگنده‌ها و قایق‌های اسرائیلی در سواحل مصر به این کشتی آمریکایی حمله کردند که در نتیجه آن ۳۴ تن از نیروهای آمریکایی کشته و بیش از ۱۷۰ نفر زخمی شدند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/440828" target="_blank">📅 23:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440827">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اطلاعات جدید از کمک‌های اردن به اسرائیل در حملات علیه ایران
🔹
یک منبع نظامی در گفت وگو با فارس: بخش عمده‌ای از حملات موشکی جنگنده‌های اسرائیلی علیه ایران، از حریم هوایی اردن صورت گرفته است.
🔹
جنگنده های رژیم صهیونیستی به دلیل جایگزینی تجهیزات راداری و پدافندی غرب ایران، در حمله اخیر از «مهمات دورایستای هوا به زمین» استفاده کرده‌اند.
🔹
همچنین بالگردهای ارتش اردن نیز در عملیات رهگیری موشک‌ها و پهپادهای شلیک‌شده ازسوی ایران نقش حمایتی قابل توجهی به ارتش اسرائیل ایفا کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440827" target="_blank">📅 23:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440826">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4970268c70.mp4?token=Y8DwexGw-e4MiWm11dVWkeKiU9Un2hIWi5HMxkl-qnvhK5HSWDzjGAFOAa4nAvq_RyrvD8Q07L0vsKHr5cgC0jsbyv72-Im8Qt0PpXmWu7xNUtfp23M21CcHoSCALt1UIOnDJqTLMcMDcTqUVVwkutBrdeaoASahkVylj3lOVh-OaWlqyWAYr8-QMrtxCNo8cY7XyFItNXJRlVLWnXbbzvw7vKCZjv-TkQ-M7uLg6QYAQCIlrqitREJ2TUQPIDs0C_J00aw3NzCBz_lvheYLcVjiKQ9XrwhMuXM9Rw5u_PhLpgEf3xYGJ27tZ9jiNFTTUBu_Hx0lUoVK2a9F77IO-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4970268c70.mp4?token=Y8DwexGw-e4MiWm11dVWkeKiU9Un2hIWi5HMxkl-qnvhK5HSWDzjGAFOAa4nAvq_RyrvD8Q07L0vsKHr5cgC0jsbyv72-Im8Qt0PpXmWu7xNUtfp23M21CcHoSCALt1UIOnDJqTLMcMDcTqUVVwkutBrdeaoASahkVylj3lOVh-OaWlqyWAYr8-QMrtxCNo8cY7XyFItNXJRlVLWnXbbzvw7vKCZjv-TkQ-M7uLg6QYAQCIlrqitREJ2TUQPIDs0C_J00aw3NzCBz_lvheYLcVjiKQ9XrwhMuXM9Rw5u_PhLpgEf3xYGJ27tZ9jiNFTTUBu_Hx0lUoVK2a9F77IO-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپاد شاهد پیام‌رسان بوشهری‌ها شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/440826" target="_blank">📅 23:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440825">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mqe0-Uom1FKiJUJrXmcvPJGOb3JEm0Dm-62uaTT971GO1T2jDVmNEC2aZN03Bstmoj70aDcqk9bpl93f3czhPoH4ItvN5HicSXr1MK2sqA0R2p7PfPh14N8-rstCm8obOCyG6uS8-Q_Eg_P1Ymmk_DyJVNXhCl_u-hujGbWsEEFwF4ue8NCbWWUfPFxGSdM4TwWqXoWB5Rx141SP06K4k_I_WL2N1_kShcxD6HgnBYpCFGTN7Ol5Xkb0duVJz4DcphfKq-0xkFrUbW4fDdeQl0W3BzH2ydD5YvHjth6o3ZtiiRD6c2uxSqyYIG6jwKVgUGgO-geRExpXO9ghO2hUJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما؛ از اتهام سیاه‌نمایی تا رپورتاژ برای دولت؛ نظر شما چیست؟
🔹
رئیس‌جمهور و برخی از اعضای تیم رسانه‌ای دولت، معتقدند صداوسیما نسبت به اقدامات دولت «سیاه‌نمایی» می‌کند و این را در روزهای اخیر صراحتا بیان کرده‌اند.
🔸
همزمان، گروهی از مخاطبان نیز از تلویزیون انتقاد دارند که مطالبات مردم دربارهٔ وضعیت سخت اقتصادی و مشکلات معیشتی را به‌درستی منعکس نمی‌کند و اقدامات صداوسیما را به «رپورتاژ خبری برای دولت» تشبیه می‌کنند.
🔹
از سوی دیگر، دولت بخش عمده‌ای از مشکلات فعلی را ناشی از جنگ می‌داند؛ اما برخی کارشناسان و مردم معتقدند در کنار تاثیرات جنگ، بخشی از تورم و نابسامانی‌های اقتصادی ریشه در سیاست‌های پیش از جنگ دارد.
🖼
نظر شما چیست؟
اینجا
در نظرسنجی شرکت کنید
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/440825" target="_blank">📅 23:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440824">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96edf34919.mp4?token=TFjudCmvCWgvOrL2oDhhczsDL0INHtOSK8cWh4Kp_j9kXK17fGTK3SEXjPkoKR1pzoMDTbWo6vtyZG3krOfj2dxXXf_qNWVzED2Ltz-vPFD9MXJsAnNwAlTwfpafsypz6hjgp5ZDNIBCr64xhzkZwY4t3flFfclB5Agw4CJxqs734iNDArqg8shL8mP_QpTNreqQGPrdBhP-cpwBG429jN4JoYSeUJMA3JxUzvzg8D36ir3GGzy6MT85wAjg5J-mbnhqtTi4v6H9bSBbsPlV-fvZwapEzJb9LsBG5Gg2NPsxWSnHXwTginBYY_ykz1tPVdTEVYpxz6KkCiw-rfzZkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96edf34919.mp4?token=TFjudCmvCWgvOrL2oDhhczsDL0INHtOSK8cWh4Kp_j9kXK17fGTK3SEXjPkoKR1pzoMDTbWo6vtyZG3krOfj2dxXXf_qNWVzED2Ltz-vPFD9MXJsAnNwAlTwfpafsypz6hjgp5ZDNIBCr64xhzkZwY4t3flFfclB5Agw4CJxqs734iNDArqg8shL8mP_QpTNreqQGPrdBhP-cpwBG429jN4JoYSeUJMA3JxUzvzg8D36ir3GGzy6MT85wAjg5J-mbnhqtTi4v6H9bSBbsPlV-fvZwapEzJb9LsBG5Gg2NPsxWSnHXwTginBYY_ykz1tPVdTEVYpxz6KkCiw-rfzZkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علویان طبرستان حامی جبهۀ مقاومت
🔹
اجتماع شمارۀ ۱۰۰ مردم ساری با شعارهایی در دفاع از شیعیان لبنان برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/440824" target="_blank">📅 23:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440823">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366788534e.mp4?token=DfZhFzVsdnEUUzaxOgJNbLK4vTWKS8RxQ7GBkU6hbF2jhVbW-k5qDJYZURx8teStQJyJ0EsxwMH84GEYQpOxaerj1oEJSyT8eIsg8QNupw1qep3DUwanjk_0QhqpvkYJBt1FD-XAUChXO7UFpjbF02mdJ0MdY5G3B1xDJcN30JghGV9pjYGXqVqlHUvYUYwez445HlQsooBW7c-lN5gHTFvdo7iGUXE_aiKgt-G8v4nlzraoxdueXg2r1DjNMH4mnvU-V-leBrGC8DMPNO_54lznFwQGFwa6BD39Vlfry5BWh1sYeo28YnIl7oxdSZYVn0-ZZiPMpKo9NGNFhDDBHm7odNT88tEMSc3hpxPEzKiKQ3RmCNuyW-j5fMhC5_w2u5iVxMxG1IeUDwyYhH6SRKKo2Xlc0GFDPqu2xWgk_qojlE1zt8j7ZrllvFw4yREODk0zDOtxcCy6qIekxa91rCNxg3y15eI0j83oIKMBls-PE-Dc1Yin8KzNOrRtCiRehzP96c7J0Tca8UMWz3PqjvMp0w2nELXMG0h7GCHbevxAuA4-I5GoG1VMxYjGawnYVl3Dl3GuJN2E6916v_z5R8hcf0JAL-gBOarukBCQi6-kYq9wwQfPK865CMjQYKcOa458mrs3tjW0pKWodTGDBx23bNusJCy5unkVhMQ6zf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366788534e.mp4?token=DfZhFzVsdnEUUzaxOgJNbLK4vTWKS8RxQ7GBkU6hbF2jhVbW-k5qDJYZURx8teStQJyJ0EsxwMH84GEYQpOxaerj1oEJSyT8eIsg8QNupw1qep3DUwanjk_0QhqpvkYJBt1FD-XAUChXO7UFpjbF02mdJ0MdY5G3B1xDJcN30JghGV9pjYGXqVqlHUvYUYwez445HlQsooBW7c-lN5gHTFvdo7iGUXE_aiKgt-G8v4nlzraoxdueXg2r1DjNMH4mnvU-V-leBrGC8DMPNO_54lznFwQGFwa6BD39Vlfry5BWh1sYeo28YnIl7oxdSZYVn0-ZZiPMpKo9NGNFhDDBHm7odNT88tEMSc3hpxPEzKiKQ3RmCNuyW-j5fMhC5_w2u5iVxMxG1IeUDwyYhH6SRKKo2Xlc0GFDPqu2xWgk_qojlE1zt8j7ZrllvFw4yREODk0zDOtxcCy6qIekxa91rCNxg3y15eI0j83oIKMBls-PE-Dc1Yin8KzNOrRtCiRehzP96c7J0Tca8UMWz3PqjvMp0w2nELXMG0h7GCHbevxAuA4-I5GoG1VMxYjGawnYVl3Dl3GuJN2E6916v_z5R8hcf0JAL-gBOarukBCQi6-kYq9wwQfPK865CMjQYKcOa458mrs3tjW0pKWodTGDBx23bNusJCy5unkVhMQ6zf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کدام قهرمان شایسته این مدال است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440823" target="_blank">📅 23:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440822">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9Pa5wHE7vULHaN6eBrJ63fMPAFB106FxicP0BNQS4Fl-UNMFUk-v5_RXtcXeIp5JYhRdv9mHngo728ac_-nyaPoCSxzAUHqucNJ8KG5iirFoWSJ3S32xDVZKD1DQbzdJk0tsra1EGlo3I05Br0G3jedz1WPxGJBYcn-B1TyP0r5EuW65NfYvQ03HUsMZsNz0QpAcBKNPvVa12xBju_cpqU4JdEcWqdtkXhn7FvxL5W5EhzSh4o_lu1QKGLODSsvo9SCbFgGQlC-xkjvxCCuNTUPPgSjjaNDDg9G3FrRasKg8NPPaKDee6phEuC34Wji1k0ejmisFqlGaeW2s-0JYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام آمریکایی به آکسیوس: نتانیاهو برای بقای سیاسی خود نیاز به جنگ دارد و ترامپ برای زنده‌ماندن در فضای سیاسی نیاز دارد که جنگ پایان یابد
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440822" target="_blank">📅 23:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440821">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5710e1356c.mp4?token=Ku4pqqzgquD_6DnTT5CZBEQ3aaqmIQjqtvFFTCZQ_OubvzTvhtFgp9XpHql7pzdeXeR1ikcTCbkBDcj_eQV8cQ-DSvZUoGgcrgpKOtSYsotASPqKmfHjdbtsxkAanOeazCGqjMAS7K8_jxj2OvFJzu6OVOCNns46sJc7ngG0rdUWj4GdjLNYRs-voIc2IcAcdIwdrHQWPpYM7MDiN0oR7P-J9_jz9yvalyMqMXV19tK1J9bf-e8etmNAOwnaY1s9Lcb3faK-nyqbG65_njGb4yvP4yuKM8Qw3Zg_2jZw0zFokLXc6sAIZyTmLt4SO-qOuDlLi_Hl0HnuXKAzeYyj_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5710e1356c.mp4?token=Ku4pqqzgquD_6DnTT5CZBEQ3aaqmIQjqtvFFTCZQ_OubvzTvhtFgp9XpHql7pzdeXeR1ikcTCbkBDcj_eQV8cQ-DSvZUoGgcrgpKOtSYsotASPqKmfHjdbtsxkAanOeazCGqjMAS7K8_jxj2OvFJzu6OVOCNns46sJc7ngG0rdUWj4GdjLNYRs-voIc2IcAcdIwdrHQWPpYM7MDiN0oR7P-J9_jz9yvalyMqMXV19tK1J9bf-e8etmNAOwnaY1s9Lcb3faK-nyqbG65_njGb4yvP4yuKM8Qw3Zg_2jZw0zFokLXc6sAIZyTmLt4SO-qOuDlLi_Hl0HnuXKAzeYyj_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن:‌ از این لحظه تردد کشتی‌های اسرائیلی در دریای سرخ ممنوع است
🔹
یحیی سریع: در چهارچوب مقابله با تجاوز آمریکایی-صهیونیستی علیه محور جهاد و مقاومت در ایران، فلسطین، لبنان، عراق و یمن و مقابله با پروژهٔ صهیونیستی «اسرائیل بزرگ» و در راستای…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440821" target="_blank">📅 23:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440820">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">Live stream finished (1 hour)</div>
<div class="tg-footer"><a href="https://t.me/farsna/440820" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440819">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎥
۱۰۰ روز نبرد مقدس؛ یک حماسهٔ ماندگار
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440819" target="_blank">📅 23:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440818">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43b9e87bfd.mp4?token=aaTvomlpOVe3HKmI5AMrdVi4YiMc7dp5w4C0mDgETscgz_PJwhbH9kwWA5beFv48y5f1zCUQH1yNiQu75SR1hmZVEUIr9sH3lhNIY-jKmXSeqOw9rli7oWrAQ3Mk0d8WyZpdtz0yVMMTAThArW-mC0H8Ig3fFeiJXXRhNFP1o5XyuWtDqdKQMZ5z3PjXi-cM5qq4s65M97NS6ABo1ud2sEYtHBmfzoL4d48JB-9Z8xU2GdntB7SER7ylTwb-Dpappi2A1FRkz4OTO72iRzUVxFS9UK9JJ-a728N4A78tupK8xzl90Ilp4p6svrf1cpOCEsMeiuuFX5lqCNRir_iupDn_z-oUWLlh_obvxeX38oCSWDo2fzJhglW0ZaqT7EHnymdunTPWhxHEdWHQ_Y_Xo10VIDrrpeh3KuCqTzRiYlt1PMYaUYqxB4gP0gVa_5WZOWMgr6W7GttH0ZAUbGJG3biEo8K5eZGOMWIWhwb2dBEDGtC0YtBx72mU-m4Yi-5MZSxFWU57-kbHCZ7vSBRXw24-o8UaGBi9P5AjUYtRDMi7ZizU1RwpgWamugkxKK4nTayRPozlwu2sOm-xWQdVhDa8UVn-ZTK6s14nQzltfxU_2OyeJ_KD2MTlV74vBviKDxpw5ERMw5UtZjlGEu7HQRcB-q36e1F0CYV0AHjHW64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43b9e87bfd.mp4?token=aaTvomlpOVe3HKmI5AMrdVi4YiMc7dp5w4C0mDgETscgz_PJwhbH9kwWA5beFv48y5f1zCUQH1yNiQu75SR1hmZVEUIr9sH3lhNIY-jKmXSeqOw9rli7oWrAQ3Mk0d8WyZpdtz0yVMMTAThArW-mC0H8Ig3fFeiJXXRhNFP1o5XyuWtDqdKQMZ5z3PjXi-cM5qq4s65M97NS6ABo1ud2sEYtHBmfzoL4d48JB-9Z8xU2GdntB7SER7ylTwb-Dpappi2A1FRkz4OTO72iRzUVxFS9UK9JJ-a728N4A78tupK8xzl90Ilp4p6svrf1cpOCEsMeiuuFX5lqCNRir_iupDn_z-oUWLlh_obvxeX38oCSWDo2fzJhglW0ZaqT7EHnymdunTPWhxHEdWHQ_Y_Xo10VIDrrpeh3KuCqTzRiYlt1PMYaUYqxB4gP0gVa_5WZOWMgr6W7GttH0ZAUbGJG3biEo8K5eZGOMWIWhwb2dBEDGtC0YtBx72mU-m4Yi-5MZSxFWU57-kbHCZ7vSBRXw24-o8UaGBi9P5AjUYtRDMi7ZizU1RwpgWamugkxKK4nTayRPozlwu2sOm-xWQdVhDa8UVn-ZTK6s14nQzltfxU_2OyeJ_KD2MTlV74vBviKDxpw5ERMw5UtZjlGEu7HQRcB-q36e1F0CYV0AHjHW64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۰۰ تاریخ‌سازی حافظان سنگر خیابان در قزوین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440818" target="_blank">📅 23:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440817">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa9f4bca8.mp4?token=QvO1c9AqmdYgveR4dDwmfzo900Xp5Le35iZwsUajdZWaxmgWfmLk4lNxSM_3kuxK_tUPClzoS_Qrvw98-xzFDWouPFQLoepGaR4DkG-6dK7zas2TLoQvlhzjrhJuOiQEp-lS7cXeEhqLh84Rbgw1fblKB3iSVzVYC5rgjasppm-z8lL7cqP74fdHzXR8RJp6ufHtrHC1Izg5-cJYhSIZgRXBE_LMBIGtpFgdNVI3Tha7se55kC2Gzb7T9zJkWsSUoR_gOsbWhjk6Y-rMrejjMbwo3Q_IT_GpKv6BbZaPfwLaNo6OfAZQNMiqXbmRVZcDv97Pl35jFt2i-4Ga5YSjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa9f4bca8.mp4?token=QvO1c9AqmdYgveR4dDwmfzo900Xp5Le35iZwsUajdZWaxmgWfmLk4lNxSM_3kuxK_tUPClzoS_Qrvw98-xzFDWouPFQLoepGaR4DkG-6dK7zas2TLoQvlhzjrhJuOiQEp-lS7cXeEhqLh84Rbgw1fblKB3iSVzVYC5rgjasppm-z8lL7cqP74fdHzXR8RJp6ufHtrHC1Izg5-cJYhSIZgRXBE_LMBIGtpFgdNVI3Tha7se55kC2Gzb7T9zJkWsSUoR_gOsbWhjk6Y-rMrejjMbwo3Q_IT_GpKv6BbZaPfwLaNo6OfAZQNMiqXbmRVZcDv97Pl35jFt2i-4Ga5YSjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدمین شب اجتماع مردم اردبیل با این حال‌وهوا برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440817" target="_blank">📅 23:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440816">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGH-bm9lkXRO_hFzA2D-KI0l5MQY3Fjyb4whakd5iba4zT1o5QTnGILFEAsjRcfrjUw6frIAMiaGQ4k-zN-D7xVq-9asC9HOud_kKtDqoSjRUlSy0AQGn31eKZPqG9f0DXKcp1dnxsI5Z5fwpM6Ep2Pht7AR93AxXEUNVRNnCQXZGz9LiURyEIbwZ-Du7246S1MwjO8Bp7KiUF2PNF_N_EGbvqu-pt-D19EUsNqjiE5Z_Mj2eQAEc4xRuJA-k32bE4ZL64hxb7gSNNNE70xqctvCsKtIdl45GJWPMnTVsJ31DXk4u9_csUCnCG9XIECxU5PbA2WxnldmcPci6ae0eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بازخوانی صحبت‌های رهبر انقلاب دربارۀ تهدید به گشودن جبهه‌های جدید به روی دشمن بنابر مصالح
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/440816" target="_blank">📅 23:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440815">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0569e1cb09.mp4?token=YwjS4imv6WjDBrnUBDbuVCg25cLIBnA3dq4aNzL9vB37quVp0FWAQWA4w9E54pg9Q44sJXjEvLcRA9_SBfLYFtkNtKwg1TJnPWEZDtj6FUZEP6vdOMrSaLUudHvBihJqW3odo1q5X6DFT-QlFwunsApGovLo8GYbKeHYZWpNVdBO4RqcOiZKO7JrHxlvpt2gfXyv9GDbILPlJWscEsg3kHBSdPf1vk1khPGMPoqnGljo5jDkZ8px-OiqPkYcyFjJ8N9t877WIZEXLmZEStdlinybAfAupyT03NqHmhcPdas3n0NY50romEfm8O2pETdStHAUhk-dIYmsSsFnwPWzqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0569e1cb09.mp4?token=YwjS4imv6WjDBrnUBDbuVCg25cLIBnA3dq4aNzL9vB37quVp0FWAQWA4w9E54pg9Q44sJXjEvLcRA9_SBfLYFtkNtKwg1TJnPWEZDtj6FUZEP6vdOMrSaLUudHvBihJqW3odo1q5X6DFT-QlFwunsApGovLo8GYbKeHYZWpNVdBO4RqcOiZKO7JrHxlvpt2gfXyv9GDbILPlJWscEsg3kHBSdPf1vk1khPGMPoqnGljo5jDkZ8px-OiqPkYcyFjJ8N9t877WIZEXLmZEStdlinybAfAupyT03NqHmhcPdas3n0NY50romEfm8O2pETdStHAUhk-dIYmsSsFnwPWzqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جبهه‌های جدید در انتظار تداوم اقدامات خصمانه  آمریکا و رژیم صهیونیستی
🔹
سردار سنایی‌راد، معاون سیاسی دفتر عقیدتی ـ سیاسی فرمانده کل قوا: رژیم صهیونیستی و آمریکا اگر بخواهند دست به اقداماتی بزنند که در جهت توسعه تنش باشد، قطعاً ایران و متحدانش از امکان و اراده لازم برای گشودن جبهه‌های جدید برخوردار هستند.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440815" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440814">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تحریم‌های اتحادیه اروپا علیه سپاه پاسداران
🔹
اتحادیه اروپا روز دوشنبه تحریم‌هایی را علیه دو شهروند ایرانی و یک واحد از سپاه پاسداران انقلاب اسلامی اعمال کرد.
🔸
این تحریم‌ها فرماندهی استانی نیروی دریایی سپاه در هرمزگان، همچنین محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه، و حمید حسینی، نماینده اتحادیه صادرکنندگان نفت، گاز و محصولات پتروشیمی ایران را هدف قرار داده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440814" target="_blank">📅 22:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440812">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e2d911ca.mp4?token=pubeNtJM_u33Bc_r1pCtIE9rEkQavyuM-xfqkvfolwPZXjWq1fRATPl1DZlHBI8Ajxfwatd5BM1OlfyyGpXNy_oSDzX1G9rNDvCLUVlfOT12n4VjLYQssxZNb_CXBbh85tKdkHa-j6yGGUtZroQjNn1yTvyG8o-J2h68KtY6cByEEd6ie1EhrxRtRemKgXu0iup2n902CnKcYF9XwTxB3slzjmvxinj5Wn55b2THbrS2nmITdEbIeOUZy6e6Okx3eq1a30FkFsNfn9l_MIv6cECZ_V0Ef-1FXAAxW1wKGz9RRCfz1GWSKe6L43pDKcVVnFSEVNyhykkbcGD6ZdaFfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e2d911ca.mp4?token=pubeNtJM_u33Bc_r1pCtIE9rEkQavyuM-xfqkvfolwPZXjWq1fRATPl1DZlHBI8Ajxfwatd5BM1OlfyyGpXNy_oSDzX1G9rNDvCLUVlfOT12n4VjLYQssxZNb_CXBbh85tKdkHa-j6yGGUtZroQjNn1yTvyG8o-J2h68KtY6cByEEd6ie1EhrxRtRemKgXu0iup2n902CnKcYF9XwTxB3slzjmvxinj5Wn55b2THbrS2nmITdEbIeOUZy6e6Okx3eq1a30FkFsNfn9l_MIv6cECZ_V0Ef-1FXAAxW1wKGz9RRCfz1GWSKe6L43pDKcVVnFSEVNyhykkbcGD6ZdaFfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ اصابت موشک ایران به پایگاه رامات دیوید در اراضی اشغالی   @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/440812" target="_blank">📅 22:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440810">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-text">واکنش قاطع در ۲۴ ساعت؛ روایت ایران از هم‌افزایی میدان، خیابان و دیپلماسی
🔹
درحالی‌که تحولات منطقه همچنان در کانون توجه افکار عمومی قرار دارد، دو رخداد مهم در ۲۴ ساعت گذشته بار دیگر بحث درباره نحوه مواجهه ایران با تحولات جاری و نسبت میان میدان، دیپلماسی و افکار عمومی را پررنگ کرده است.
🔹
نخستین رخداد به واکنش ایران پس از اقدام اخیر رژیم صهیونیستی بازمی‌گردد. پس از آنکه تل‌آویو دست به اقدامی زد که از سوی مقامات ایرانی عبور از خطوط قرمز تلقی شد، پاسخ نظامی ایران در فاصله‌ای کوتاه انجام گرفت.
🔹
این واکنش از سوی برخی ناظران به‌عنوان نشانه‌ای از شناخت دقیق ساختار تصمیم‌گیری کشور نسبت به ماهیت تقابل با رژیم صهیونیستی و حامیان آن ارزیابی می‌شود؛ رویکردی که در آن، تقابل نظامی و دیپلماتیک دو مسیر جداگانه تلقی نمی‌شوند، بلکه در امتداد یک راهبرد واحد تعریف می‌شوند.
🔹
دومین رخداد، انتشار پیام تصویری سید مجید موسوی، فرمانده نیروی هوافضای سپاه بود.
🔹
او در این پیام بر هم‌افزایی سه عرصه «میدان، خیابان و دیپلماسی» تأکید کرد. این موضوع پس از آن نیز از سوی محمدباقر قالیباف تکرار شد. تأکید همزمان مسئولان بر این سه‌گانه، از نگاه برخی تحلیلگران نشان‌دهنده انسجام میان حوزه‌های نظامی، سیاسی و اجتماعی در شرایط کنونی است.
🔹
در این میان، بخشی از افکار عمومی و کارشناسان با توجه به تجربه مذاکرات گذشته و سابقه رفتارهای آمریکا، نگرانی‌هایی درباره روند تحولات دارند.
🔹
کارشناسان معتقدند اصل این نگرانی‌ها، تا زمانی که در چارچوب پرسشگری و مطالبه‌گری مطرح شود، امری طبیعی و قابل فهم است؛ به‌ویژه در شرایطی که افکار عمومی انتظار دریافت توضیحات و اطلاعات به‌هنگام از سوی مسئولان را دارد.
🔹
در عین حال صاحب‌نظران میان «نگرانی و مطالبه‌گری» با «القای بی‌اعتمادی و ناامیدی» تفاوت قائل هستند و معتقدند تضعیف هر یک از اضلاع میدان، دیپلماسی یا پشتوانه اجتماعی می‌تواند بر انسجام ملی در شرایط حساس تأثیر بگذارد.
🔹
به باور تحلیلگران، یکی از مهم‌ترین چالش‌های امروز، مدیریت همزمان دو جبهه دیپلماسی و رسانه‌ای است. در چنین فضایی، اطلاع‌رسانی دقیق و به‌موقع می‌تواند از شکل‌گیری ابهام و گسترش روایت‌های ناامیدکننده جلوگیری کند و در مقابل، تفکیک نقد و نگرانی‌های مشروع از تلاش‌های هدفمند برای تخریب سرمایه اجتماعی، نیازمند دقت و هوشمندی بیشتری از سوی رسانه‌ها و افکار عمومی است.
@Fars_Plus
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/440810" target="_blank">📅 22:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440809">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54db1a816.mp4?token=d2uwLJW4vjocUojjAaDbST3gv2h28hluyA1pRtSs_BtK4pf7CxhqHgg5HiN6CIa7r4pl7xxCLADIaR7vxKEeZGtbga-eMEJwJkcqtEVPwz6OLvDTmDqdgKfUshegjI8vS45AfZ3WxsWgJS11nyRNwn9o6tFp_OZM8RXGFqB17YfHf4INSEi0ddVpnvJcXmUpqSdEZIQM-32cGDlwwei__u4Tyn4XzRzLWQaaW1cqIoCUC7L7Vk5TvPZUTljcEr1odSDQiBu4KrAdUifFHrK-v_sFq_57gVh2KaJub7HBv1osNSqTyESeX3Qmn2hzj7192g3Lt_h-gxPDFOiZv5_GFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54db1a816.mp4?token=d2uwLJW4vjocUojjAaDbST3gv2h28hluyA1pRtSs_BtK4pf7CxhqHgg5HiN6CIa7r4pl7xxCLADIaR7vxKEeZGtbga-eMEJwJkcqtEVPwz6OLvDTmDqdgKfUshegjI8vS45AfZ3WxsWgJS11nyRNwn9o6tFp_OZM8RXGFqB17YfHf4INSEi0ddVpnvJcXmUpqSdEZIQM-32cGDlwwei__u4Tyn4XzRzLWQaaW1cqIoCUC7L7Vk5TvPZUTljcEr1odSDQiBu4KrAdUifFHrK-v_sFq_57gVh2KaJub7HBv1osNSqTyESeX3Qmn2hzj7192g3Lt_h-gxPDFOiZv5_GFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار در مقر عناصر ضدایرانی در اربیل
🔹
منابع عراقی از وقوع انفجار در یکی از مقرهای گروه‌های تجزیه‌طلب و ضدایرانی در منطقه «سوران» واقع در منطقه کردستان عراق خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/440809" target="_blank">📅 22:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440808">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHK_7kmOSXau844wWU2-XgGtrgFJhRz-1eiHd1LcUFgY9c82tzyTj7fPhESy-LIYs4HJoVZkkPaJHqIy1_UA-xY43D2BLA9k6EbbZLapg8z-ymfd_Cqo42_35YudC12y8UMS5QMTfl08rUVp-nGMi9JlY7Hn2U0Aqnx4S6GD34wPPszjN1ISKdDsBa44kUIh8rreMJV_ZCVa2m-feA-y5UMj_1_q4bn4039iSsPzncZe0zk-69NvbkExlMP0loWTQIyKP8cEHInwfDlaiElc9zOLklAJNO0kzxirls-QAp1ktjS2yQAWM_ulUcYQg9gBIXPtnxyNCJOiHRaxCxY8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور لبنان: فعلاً قصد دیدار با نتانیاهو را ندارم
🔹
رئیس‌جمهور لبنان که در قبال تجاوزات رژیم صهیونیستی از جمله حملهٔ روز گذشته به ضاحیه بیروت مهر سکوت بر لب زده است، گفته که برای امضای توافق عدم حمله با اسرائیل مذاکره می‌کند.
🔹
جوزف عون که به‌دلیل تداوم حملات صهیونیست‌ها همزمان با مذاکرات مستقیم دولت لبنان، تحت فشار و انتقاد داخلی قرار دارد، به شبکهٔ سی‌ان‌ان گفت که پیش از دستیابی به توافق برای پایان دادن به جنگ، با نتانیاهو دیدار نخواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/440808" target="_blank">📅 22:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440807">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75ba9a2e68.mp4?token=jVVT9oxfFv8kChfiPqvpwSuuPWxjkd19dUTneoRrnlNI_jvD4fIe-WCputqcRLtIm56g1L-Nu9WcOHWCth3Yc222AgDxnr_WfNYd5jcIlxt1Yhe3QvOOXA78EvlxHXO0yuXWodjyHLvHJLPmxVHS5UQOhPF5sQepFbZzO1dP1hSIEeljLHr_rzZvDocjDBExUyWw12c0k5Z48q227ucL5B9XMjc5FUTW0r7NpkgIbLJCfGb7-TJYkfIsC5tMNQr3UKhNFZ_hJ1MzpDCbrMpKAqyAp6-r2paEzKMyXpSm7X-UpjV6J1-W0xE1vHYLynnYbpYAeXc88Wrm7y28lPtfdogD8M_dD5qWm1zolieDyaM_i_TX_mQEvVRUbTPRz0BSoab35B2UZBiClVfN2cuVZ0X3gKPw6C2w6Qmlfs4xaKR3z1S-XxOeicRfKAyoUb2qAQE7goPUlYi4AC8sOg4212IUqeWcRo6ahBdWhagoHfvZd782it6_sZhhjvMoTtYbLtA0zMjkfeOz6R-9g3cnR9e9Kwl6wN6b-2mtvsiiKNVbIcGUNJnJ9ybCibsucLwzeBpmJZ0OL8itHtNSkaF6MOWrmmuVLRS9IJKY9f7-RiI3nzELegKiTiyCnIzTZ4ahL20zyuMaVwBF7jbH9NM2iZTXOc7NqZNTmligupRe7BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75ba9a2e68.mp4?token=jVVT9oxfFv8kChfiPqvpwSuuPWxjkd19dUTneoRrnlNI_jvD4fIe-WCputqcRLtIm56g1L-Nu9WcOHWCth3Yc222AgDxnr_WfNYd5jcIlxt1Yhe3QvOOXA78EvlxHXO0yuXWodjyHLvHJLPmxVHS5UQOhPF5sQepFbZzO1dP1hSIEeljLHr_rzZvDocjDBExUyWw12c0k5Z48q227ucL5B9XMjc5FUTW0r7NpkgIbLJCfGb7-TJYkfIsC5tMNQr3UKhNFZ_hJ1MzpDCbrMpKAqyAp6-r2paEzKMyXpSm7X-UpjV6J1-W0xE1vHYLynnYbpYAeXc88Wrm7y28lPtfdogD8M_dD5qWm1zolieDyaM_i_TX_mQEvVRUbTPRz0BSoab35B2UZBiClVfN2cuVZ0X3gKPw6C2w6Qmlfs4xaKR3z1S-XxOeicRfKAyoUb2qAQE7goPUlYi4AC8sOg4212IUqeWcRo6ahBdWhagoHfvZd782it6_sZhhjvMoTtYbLtA0zMjkfeOz6R-9g3cnR9e9Kwl6wN6b-2mtvsiiKNVbIcGUNJnJ9ybCibsucLwzeBpmJZ0OL8itHtNSkaF6MOWrmmuVLRS9IJKY9f7-RiI3nzELegKiTiyCnIzTZ4ahL20zyuMaVwBF7jbH9NM2iZTXOc7NqZNTmligupRe7BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ حملۀ موشکی یمن به اراضی اشغالی
🔹
ارتش رژیم صهیونیستی: ما شلیک موشکی از یمن به سمت اسرائیل را شناسایی کردیم و سیستم‌های دفاعی در حال رهگیری آن هستند. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440807" target="_blank">📅 22:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440806">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چرا جنگنده‌های اسرائیل وارد آسمان ایران نشدند
🔹
پس از حملات رژیم صهیونیستی به ضاحیۀ جنوبی بیروت و پاسخ موشکی و پهپادی ایران، اسرائیل چند سایت راداری را هدف قرار داد اما به‌گفتۀ منابع مطلع، جنگنده‌های این رژیم در این عملیات‌ها بدون ورود به آسمان ایران و از خارج از مرزهای کشور اقدام به شلیک تسلیحات دورایستا کرده‌اند.
🔹
تحلیلگران نظامی این تغییر الگو را نشانه‌ای از افزایش ریسک ورود مستقیم جنگنده‌های دشمن به حریم هوایی ایران ارزیابی می‌کنند.
🔹
البته این اقدام با پاسخ سریع ایران همراه شد و سپاه پاسداران پایگاه‌های تل‌نوف و نواتیم را هدف حملات موشکی خود قرار داد.
🔹
پس از آتش‌بس ۱۹ فروردین، شبکۀ یکپارچۀ پدافند هوایی کشور با بازسازی، تقویت سامانه‌های راداری و افزایش هماهنگی میان مراکز کشف، فرماندهی و آتش، به سطح بالاتری از آمادگی عملیاتی رسیده است.
🔹
در جریان جنگ ۴۰ روزۀ رمضان نیز پدافند هوایی ایران بیش از ۲۰۰ هدف متخاصم شامل جنگنده، موشک کروز و پهپاد را رهگیری و منهدم کرده است.
🔹
کارشناسان معتقدند علاوه بر توان دفاعی، قابلیت بازسازی سریع سامانه‌های آسیب‌دیده نیز به یکی از مؤلفه‌های مهم بازدارندگی جمهوری اسلامی ایران تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/440806" target="_blank">📅 22:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440805">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8932184e58.mp4?token=pLad6ufV8-YrgSOklIvTkIhQEUGQx-k7ZH2IUxKImkMcY-gVcOQ4cUgNfv5JUham3DjO0lc19Fm5hHIYIoun53LYw-qWaza5NiBLdIGgdtopYnfYMujWImzf31X8hg9wNzrSML_nc30Yln-MKzCZYkuHLSSn1u_LYvU753Nlr9A8zAO0QU53eNS_YM6c8xzFncqgJ6MNgoypQMoybQvPTKVhFuOqid4slk8DL-yRzkiY-5P9uZGPLAdRhlZU6-ALvFkGYbjaJOCTtQVjdfkEkkwCzrPSbFG0yjKOXJW-537U_uu9pC6FulOk4-W1VS1a7YF6V02X8Fzj0xLvjlGtpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8932184e58.mp4?token=pLad6ufV8-YrgSOklIvTkIhQEUGQx-k7ZH2IUxKImkMcY-gVcOQ4cUgNfv5JUham3DjO0lc19Fm5hHIYIoun53LYw-qWaza5NiBLdIGgdtopYnfYMujWImzf31X8hg9wNzrSML_nc30Yln-MKzCZYkuHLSSn1u_LYvU753Nlr9A8zAO0QU53eNS_YM6c8xzFncqgJ6MNgoypQMoybQvPTKVhFuOqid4slk8DL-yRzkiY-5P9uZGPLAdRhlZU6-ALvFkGYbjaJOCTtQVjdfkEkkwCzrPSbFG0yjKOXJW-537U_uu9pC6FulOk4-W1VS1a7YF6V02X8Fzj0xLvjlGtpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازیکن آمریکایی استقلال در ایران ماند و ازدواج کرد
🔹
تاجرنیا، مدیرعامل استقلال: بازیکن آمریکایی ما در تمامی طول جنگ تحمیلی ایران با کشور خودش در ایران ماند و اینجا ازدواج کرد و قرار است همیشه اینجا بماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/440805" target="_blank">📅 22:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440799">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f36use2-ROLD4ZwqoZuxd55wudnhxF10XYWS7AKTWkMfOHYbMAEGzag4SA4k93l9aKm7pT8acl1v3GIdFBZy6Jzi6zKjuYGqhz9F2ObTprvyv7fcofKxCsnia256z4TS1aCQQ46HEBRjl8Hiy5Tm21u_43AVOEvFgPcbbH7Tyx3E4YcCDJIcsL2ftxnH4xexKobkhUpcjYxb26yUt7bHVDo4JVrRw_anrQsGw7hZIwfvh7UxiPGD5zIiO6IfsnQAXMLv7iKbJtthAQRQn5yyRkzvd-OKwQXsn5SpqltxqzdngySkaYeeyFF3Tu5BDBYkUZJnj_HSKWVh6699RTX1yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UznnyaQNgML52Z1dv_fWOBPTvvqT5socUVkVtBCtghZApEas0kBzzgwjq05wXd-3trdw5z8U2ptxpfZ8RF58Tm_YArJ_irlMtNc8Ol8uPYEfSbc1pB82Rw67HVwawEsIyDM1iBytvxaHuXW7yNOXof-OaLZ2FAd5jVOSBTgtCXBqB1VJsAFYo7rMVL2AHAVaKOA3aADIruU5v7RoDW0wa9cJKCN2DHgY6QcYEcP9iUqAjMZTV4yiSzT3FPbzdZ8SVJlCns0uKM6vp8oS6g9PvC6qB7xEYYITXXbJNyd6-UyB_hdUQ742xu_4jOCEd3bEXlT6JhMDXQaCT-IzHt7T9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abLh9jZYzIpdfftzBCyL421yH_Bx7ZUX8UJMIpKnhU5bgqIFszfbESbYuYB0_682_OElgBwJZsFTGkZI0E-kw5doiiZOXudtX5_6D3OetWcNn183fqFpGlSO6MxNFWA43a-SkYnr4QoRiWbluoOTVFTV1m1FfPwdvIrVJAzIVK5H5rE6b_YBdrfkVY5xalZcddudcCAD1gOZeVvPMLnMyp-XO5nj-FEFRip9D9dVSUBuF7nWSs0gMDbnQQc1bwhsPduz3l5zMr5I04hxXFwxCcnQwKMZhrwDChOkkUGuJ3dtNKpj6zODMpzSvA9gScmvwk2RQTH6Mdk39_DskXcusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWPTYgJn9B9ARxfYUd0urPiPaoGngHn9b6FmD_3TP_Y1VFouxZLj8bmADiuScIB1rs6lgW9IMx_9tq__leqYHoJ4Y5xhKUxmijjB4tweK4YvKNeY_xo70lqME5Ns0FRyhzQkVrthataGJzF8Oc8jgQjKW5caOT1fAaz9f0LS9c1E3n5GB6rzMpIJtaPqNf1UwA1qR2Ozuo0cCueg-rdiiVSMzplsfPfvLdiGejXR5uekFhg_2oFjbHb1XzLcQ3ivMbSAiFd2gmHkWFv7X0PWBjhsfexiQysOuBAFAAJnkkW_fJL1Wfs4jhdArmB5Rux5eAHA2LdP0X3aroOLH4NeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_mzO7nRBZd-0TYtI6vlbJT1RzCEvIiqCggKp6SzfqGdtKZ3CTh67KkKoSiRs662lI6Z2rKU-Cv8hlxbhg63mNb1uWiAMealSaaGWFJ_WFrbRx7H877iFJyTyKxjoTLBjBTPEdWDrjxZF8bzcr6DkDKcQDfijPaOsB9AwbivUrOVICn1sfl8mDh3YiRZsruc6j7G5ixuY9f6CqprPzZzZmkLAmZaMgyuNnjq845jvPO49NgmY_fMSXUPEpWsPE_oUNh5f4f3DgWxUFE9vmqkqHATELh-8sJrDf_0IIGhDTK3GirNHBBvwhl_S40jj4rDZ0hEtwkgt3yoQIEN4LGGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFUZxJEhAByJ03a0lUcaPA6ZIU2kbigT5WWbuq0hTQ1fGGmRhNyuQbxr3dauaK--2pmhLQJGX2D9p1vOY-kjgB-qbVSWSz-6Y86-L-PyWaoyqd8QtxnFzKTxponQoODbEDTZ9ZpNzOjqGfGEQ1p9AaFYJGU9cIdL_xZv08Ype6yHj4r_QT03HFpTbItjpHYlZ_Zfj-sPHl4CvOYaM4JeEOicHRAmc0OLUyWFLzJJF73jRZu17BIXVSOL0zawzJC9OJqHox6nEPOLgLWwI5ryvTd33IMmPnayfdpBAeASaJtos2GcZ90v6NjzKyHFWrad-O6CD6U8bxvRxMe1tZJ4hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نمایشگاه عکس «تهران، خط مقدم مقاومت»
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/440799" target="_blank">📅 22:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440798">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fef4612464.mp4?token=pyAs-tbbxRdYUqed53CMLeWruNDY59hIVPLM7UxhYm5AbyaEyy9YTBUbvf-dwnrHFbGlJ5j0tkiNSTYGJTB25aYEXsooPr-rrAY0b-NFL6FU8kum0CzVSikh2C5wAez8gMPSS47NyhMmbBN8XIcIiwOpIK9G3XQpgusBuJA7pQy_B7IujxI2mxQQ1d4pW4JWFpZ4VCu26AmZ6kECnVZe64kO8tT1Wnigo965wz3mIpza1bCd-zzB0Vm30WBNpMZDi3K-pLGDWQNXQr8-FY-Nvt8AkwhnehXiTkLf6LkdFY3VpVCxmO6xlxgnm73qaQg6uscwLO7upWQGSu2t0sLMqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fef4612464.mp4?token=pyAs-tbbxRdYUqed53CMLeWruNDY59hIVPLM7UxhYm5AbyaEyy9YTBUbvf-dwnrHFbGlJ5j0tkiNSTYGJTB25aYEXsooPr-rrAY0b-NFL6FU8kum0CzVSikh2C5wAez8gMPSS47NyhMmbBN8XIcIiwOpIK9G3XQpgusBuJA7pQy_B7IujxI2mxQQ1d4pW4JWFpZ4VCu26AmZ6kECnVZe64kO8tT1Wnigo965wz3mIpza1bCd-zzB0Vm30WBNpMZDi3K-pLGDWQNXQr8-FY-Nvt8AkwhnehXiTkLf6LkdFY3VpVCxmO6xlxgnm73qaQg6uscwLO7upWQGSu2t0sLMqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: موشک‌های ایرانی به اهدافی اصابت کردند که بتوانند به حزب‌الله در جنگ کمک کنند.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440798" target="_blank">📅 22:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440797">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/440797" target="_blank">📅 22:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440796">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f48eb8557.mp4?token=o9fry0RgqgtVybO1oSjGSkxfF63NKlk3CYjCL98DL1h5NLVIw0GVXIn3T69RiUhqhTy41TVxsqxgKD1Vp6IvP_G_Oy0KDKAgVGGqitC50240Vv1Pu43L76327ACMRfXdZ77JW-Yprtl7l6d90A9Lrr1oqjyODnFN0NZWN5leC9hxIespqjr0GqYhJ3i7vExjIWs7G76Gebd2mygjWu_BukBlxSzcq9wKRjSKcBRtO3wZHjdnRvM6GR5O55aX9qbdg9bERud8A6NDmV3al8-MshcLpuJbtonf9NfFN63Wn7TKz_hgfZtqsc5hX5RPKhK1RD-IEgW19ycCYUGculq4YB9Y0vGqQdiSXbhW5fxcJue_JbXPrNvPX85e6vNLElcm6zFJcMYkdA7oLrXgLS-nuBAgt3hH5X65_SDibp4YbolRFDOQepL6vbbndjUnJIXOjh4MrA0RxVNxbhN1tu9RsuozzJkZabvF-CFl1Ya3mZPzNiWT8p5f9t5sT9Pea39m2JuwLwg_VD-UqOcI--c8BPj38YT8ggN0p6tLtMW3QXg5dmLaC_W8VYzfQo9nApe1PgSlHOp58L4WbbrWlHtE6ykVmsHVUUVE5jegeEHQn0f-zC-Epd9RcEu5erbWmWOmn1Yy0EJyBhwB1GlhxLLu_3GKbVxMrjsw0s93zvXsQnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f48eb8557.mp4?token=o9fry0RgqgtVybO1oSjGSkxfF63NKlk3CYjCL98DL1h5NLVIw0GVXIn3T69RiUhqhTy41TVxsqxgKD1Vp6IvP_G_Oy0KDKAgVGGqitC50240Vv1Pu43L76327ACMRfXdZ77JW-Yprtl7l6d90A9Lrr1oqjyODnFN0NZWN5leC9hxIespqjr0GqYhJ3i7vExjIWs7G76Gebd2mygjWu_BukBlxSzcq9wKRjSKcBRtO3wZHjdnRvM6GR5O55aX9qbdg9bERud8A6NDmV3al8-MshcLpuJbtonf9NfFN63Wn7TKz_hgfZtqsc5hX5RPKhK1RD-IEgW19ycCYUGculq4YB9Y0vGqQdiSXbhW5fxcJue_JbXPrNvPX85e6vNLElcm6zFJcMYkdA7oLrXgLS-nuBAgt3hH5X65_SDibp4YbolRFDOQepL6vbbndjUnJIXOjh4MrA0RxVNxbhN1tu9RsuozzJkZabvF-CFl1Ya3mZPzNiWT8p5f9t5sT9Pea39m2JuwLwg_VD-UqOcI--c8BPj38YT8ggN0p6tLtMW3QXg5dmLaC_W8VYzfQo9nApe1PgSlHOp58L4WbbrWlHtE6ykVmsHVUUVE5jegeEHQn0f-zC-Epd9RcEu5erbWmWOmn1Yy0EJyBhwB1GlhxLLu_3GKbVxMrjsw0s93zvXsQnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
و باز "وَمَا النَّصْرُ إِلَّا مِنْ عِنْدِاللَّهِ الْعَزِيزِ الْحَكِيمِ" تکرار شد
🔸
این‌بار برای لبنان
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440796" target="_blank">📅 22:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440795">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3aed63888.mp4?token=H7F8vQzj_K9Ro88fX6r66gB855pHZqb_4g3EE9oSW-aoSruxVDiHDxHiD-P4IYSOUq26EHcqIbnlOZFj7OUeFGIy2WJpjvLTmrPKsoW4j4xtnWpBkJyQOMnCr1RPUiOkkPcBb7xPw3qiqmbExRXNHgnWFstNnEG0S3GMuHhoujCD4cXJix4IBOGnuuyBpOYencS5GVQGh6wZXLOYlhagahv2E4g9wJXxVysGgEZx2DlFs061fAw7gCOfx4v4Mh8cAWH4rJolDUg4yIo30Nwzz_nPj2zFIZhpXMP3Lfu6-xRHCE3E93A5F0sDXYHaQdItiSH4q9y2T9FnC9axo3o4GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3aed63888.mp4?token=H7F8vQzj_K9Ro88fX6r66gB855pHZqb_4g3EE9oSW-aoSruxVDiHDxHiD-P4IYSOUq26EHcqIbnlOZFj7OUeFGIy2WJpjvLTmrPKsoW4j4xtnWpBkJyQOMnCr1RPUiOkkPcBb7xPw3qiqmbExRXNHgnWFstNnEG0S3GMuHhoujCD4cXJix4IBOGnuuyBpOYencS5GVQGh6wZXLOYlhagahv2E4g9wJXxVysGgEZx2DlFs061fAw7gCOfx4v4Mh8cAWH4rJolDUg4yIo30Nwzz_nPj2zFIZhpXMP3Lfu6-xRHCE3E93A5F0sDXYHaQdItiSH4q9y2T9FnC9axo3o4GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشت‌های گره‌کرده؛ سندِ اقتدارِ لامرد فارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440795" target="_blank">📅 22:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440793">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4345ef7985.mp4?token=DxjAOCHLXq9OT-iHlV6czMItVM3HQcV1D85WlbX8szUXCk6KsmaQArJ4lMvIsJDTUFXheVV0KDn4Ob3kH2SYlUlIb5UWyZwZnRN6yUYHvA4CPbOyUp65rJb4-lVU4E-yeGTK3lZ3q0l2LQyhQwjPzsQ2ZchxICf6wglbOmQLMowCMRYabGv2_UZaHFMVTwf_iwjSjdo-9MStCD8qnY3Ian0RBp2dno1JahKBGoAXDnxFHwb-orDEaAbjZnz4Rbt7G1R3EL_0VXBrqM26eBturAmRkcnk8TR2hZo-YWTmlmyykeKaztlKATrYST2wxerz8s2i8-HWBwVodPsTT4EZiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4345ef7985.mp4?token=DxjAOCHLXq9OT-iHlV6czMItVM3HQcV1D85WlbX8szUXCk6KsmaQArJ4lMvIsJDTUFXheVV0KDn4Ob3kH2SYlUlIb5UWyZwZnRN6yUYHvA4CPbOyUp65rJb4-lVU4E-yeGTK3lZ3q0l2LQyhQwjPzsQ2ZchxICf6wglbOmQLMowCMRYabGv2_UZaHFMVTwf_iwjSjdo-9MStCD8qnY3Ian0RBp2dno1JahKBGoAXDnxFHwb-orDEaAbjZnz4Rbt7G1R3EL_0VXBrqM26eBturAmRkcnk8TR2hZo-YWTmlmyykeKaztlKATrYST2wxerz8s2i8-HWBwVodPsTT4EZiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بالاخره شب ۱۰۰ هم رسید...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/440793" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440792">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ec953b5f.mp4?token=qsvbSxrxuE-29GafnGRNxJuEDnQqrMVc7zvO_mulyB-9-aNXCxHEE4maYCURH38sxwA4B0UCqWWOYtG7iOqAWdcUvVVN5UUa02n0fnDlkM53uNxH_x1ycr0s_ZVkMqlv1flOt62HpSkjU9u4ZClzv3v_iUABfWVJQhYnpaBf051iuvnPDdWL28BmpqUt_ytMAVTYBOMbtODLrbKwr9iNCLKqXbNEa9V9bq1vvEdIqBbVfSDw2f1q4b9W3HGrSi0Buz8LNhUQjaaWex42g2dhi7SRgpkwsJQJBg7oY50sTu55sUM9SVu5vrZzew3e8ZAaQ02W3aEb4X6Br_oVLsf9mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ec953b5f.mp4?token=qsvbSxrxuE-29GafnGRNxJuEDnQqrMVc7zvO_mulyB-9-aNXCxHEE4maYCURH38sxwA4B0UCqWWOYtG7iOqAWdcUvVVN5UUa02n0fnDlkM53uNxH_x1ycr0s_ZVkMqlv1flOt62HpSkjU9u4ZClzv3v_iUABfWVJQhYnpaBf051iuvnPDdWL28BmpqUt_ytMAVTYBOMbtODLrbKwr9iNCLKqXbNEa9V9bq1vvEdIqBbVfSDw2f1q4b9W3HGrSi0Buz8LNhUQjaaWex42g2dhi7SRgpkwsJQJBg7oY50sTu55sUM9SVu5vrZzew3e8ZAaQ02W3aEb4X6Br_oVLsf9mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: موشک‌های ایرانی به اهدافی اصابت کردند که بتوانند به حزب‌الله در جنگ کمک کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/440792" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440791">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTgyanmnKet8BTiVyg6B2Nslo-T8nFBdkKdky-NxtYbB3yw8BKEuOjCj1uqsGpeQGDcpVDAPjANCZR0Y53hsf2St90nn9qesvwdTy_c5DzkjsGeG90_GRVxFL755H50EsFYhdJL39qchLG30p2uYqXTy38lymolwk9NtjRCPDdV32pcreO4ltDOY8vyDQPK49lDiW0jAEooRAFO8LLQ-Q6_FSyfYo2-P0dWGMgoK4YI8bG3Cb4wYybUEp4ID1GrT8FubwPE8BRPdrWotM1JLDMRT81VI8BHyW5jbB7JBwK3EX2M5aJnHqeaS1-y4DGVmab7tXcQBU0ZnnP_HZFU3fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
بانک صادرات به‌عنوان موتور تأمین مالی ایران جدید؛ از دانش‌بنیان تا محصول نهایی
🔹
سرپرست بانک صادرات ایران در بازدید از مجموعه دانش‌بنیان پارسا پلیمر شریف، مشارکت همه‌جانبه در پروژه‌های دانش‌بنیان تا رسیدن به محصول نهایی را محور اصلی همکاری‌های دوجانبه اعلام کرد و بر نقش این بانک به‌عنوان بانک پیشرو در نوسازی و بازسازی اقتصاد ایران و موتور تأمین مالی ایران جدید تأکید ورزید.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/440791" target="_blank">📅 21:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440790">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromماجرای جنگ؛ رسانه تاریخی سیاسی</strong></div>
<div class="tg-text">🔴
ماجرای جنگ۲
👤
به‌روایت جواد موگویی
📽
روایت هجدهم:
لامرد ۷۲۰k
نسخه باکیفیت را در
آپارات
ماجرا تماشا کنید.
🌐
@majaraa_media</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/440790" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440789">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/440789" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440788">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ba1ff455.mp4?token=RGPFiovhg-QvpD8zBkwUyVVryb9nZB8pI_aeQRhkmzElt6C_ifJU0Z0xyN_Dqi4jqpEnkk5DxLocH5yQc6gQE944uY01lilpBWlNJqo-3jGb-ihrHZ2OT4CHMUB9LFDqrhK6rSMXilVKHNyLru1HpWwkQvQlmNAUAOIMiJDH0-KfvOARGHEvbjj4GIil27goly7pv834eap_tGkJamku6Pe8Wr8o9SmezaWPOdsrGPGTisSL1vDrRP7s9ilR9lA6BvZofx5hcgK0JOA8XSJK_6vlATqot_TFQk-wsv4VBPQbQUtHxqtpExPztBK1b_ALRoerGDL_bJfXFcNc032zzgmiaUCGhgZCbfPiXeN0zSKp_ZxkLRV--xtxHF0fkkNOtHG38sCxCjgG6KPT5YT4l5uYXWG_Mv9MFB6ltWUhWcnjP39ncoqUnB3ACkKZ7gt7iF3qC4N7lLicIfICUbdRymdXeXpAkDtMPwnlaFrniDxVmiJY0LFk8Km90VYi5Q_mzpzBsFLVaZI1MHRnus7geBWBC3rZt0FfsdZIhvP9whWZVOpcUqZbBcnbe_gFDSILK6yuN7_PLw47KRlIz5UZYol9bHFcKAvNuglyTbjL7I5eckRxwYnf7R5kK9PoqMGowy5j6zticfY8XwMTLHm6oYklURYzzhngRgsSzMoMHPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ba1ff455.mp4?token=RGPFiovhg-QvpD8zBkwUyVVryb9nZB8pI_aeQRhkmzElt6C_ifJU0Z0xyN_Dqi4jqpEnkk5DxLocH5yQc6gQE944uY01lilpBWlNJqo-3jGb-ihrHZ2OT4CHMUB9LFDqrhK6rSMXilVKHNyLru1HpWwkQvQlmNAUAOIMiJDH0-KfvOARGHEvbjj4GIil27goly7pv834eap_tGkJamku6Pe8Wr8o9SmezaWPOdsrGPGTisSL1vDrRP7s9ilR9lA6BvZofx5hcgK0JOA8XSJK_6vlATqot_TFQk-wsv4VBPQbQUtHxqtpExPztBK1b_ALRoerGDL_bJfXFcNc032zzgmiaUCGhgZCbfPiXeN0zSKp_ZxkLRV--xtxHF0fkkNOtHG38sCxCjgG6KPT5YT4l5uYXWG_Mv9MFB6ltWUhWcnjP39ncoqUnB3ACkKZ7gt7iF3qC4N7lLicIfICUbdRymdXeXpAkDtMPwnlaFrniDxVmiJY0LFk8Km90VYi5Q_mzpzBsFLVaZI1MHRnus7geBWBC3rZt0FfsdZIhvP9whWZVOpcUqZbBcnbe_gFDSILK6yuN7_PLw47KRlIz5UZYol9bHFcKAvNuglyTbjL7I5eckRxwYnf7R5kK9PoqMGowy5j6zticfY8XwMTLHm6oYklURYzzhngRgsSzMoMHPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه انهدام یک تانک مرکاوای اسرائیلی از دید پهپاد حزب‌الله در ظهر امروز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/440788" target="_blank">📅 21:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440787">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkdnVVgKJcHtKyEY-WzWBW5fa8Fy3V5yDTpYhy1kAZPDTVKOZT6ntcZwlw6YczU-1HZip8NNy29-wIXmjD2MzjhJZWkubNNLIAIFR6Ifkq7qh7Sf-MjP8ukIVEUDIhqve8MVD77qPfL1_XGgThP_pSg-A-rLaASj3hoJN7-gCMZpHMTET7yxMlNbYhIJBIELLMvTc-CbwJd4MjIhp004R8TFmoyKCLnY_QY3I8rKsJ-n1n8QCnpKKKq9C1MTbm7t7r1-E9y2buJObb6JrN_V_Nqk5_ZH13fwxFpsRnzwMRYcDXIJxLgMe0LchiDsDggw7pI25byetyP5loM_p78E9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استان یزد فردا تعطیل شد
🔹
مدیرکل مدیریت بحران یزد: باتوجه‌به مصوبات کارگروه مدیریت شرایط اضطرار، غلظت بالای گردوغبار و افزایش شدید آلودگی هوا کلیه ادارات و بانک‌های استان یزد فردا تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440787" target="_blank">📅 21:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440786">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2483b6ad7d.mp4?token=ho8jLyvJPbXZrVS3YyYxZcT4MpJOtEQT1Q56Fr_RfXVq6vlUsNBI0eeAGb6QrFJQ2jXwrznq0O_WHr7RFXy0Oe1jH-eaZ97tsWeZnkLJb_8S7BgJb5FhNXB9uuxFACrFYg2hMLrhUpRq3J0b-Qd2ArOcFogRfU0KgjoCGws1gjLIFaqxaC9hZGk5I5I1Fk1oNmX5IkTsL_N_P-bClhl9sIroULd0jJZpWlTgY_hI7jbRZnLBGLvxu38ZRX0xZf1Qlk4jSwnLvXu7nPKScx-PhNlDK7qB3WmIsauKWrueVK8ammChBydYC8UAYnyxegNtu1UvqjXEz0lX1oH_diVHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2483b6ad7d.mp4?token=ho8jLyvJPbXZrVS3YyYxZcT4MpJOtEQT1Q56Fr_RfXVq6vlUsNBI0eeAGb6QrFJQ2jXwrznq0O_WHr7RFXy0Oe1jH-eaZ97tsWeZnkLJb_8S7BgJb5FhNXB9uuxFACrFYg2hMLrhUpRq3J0b-Qd2ArOcFogRfU0KgjoCGws1gjLIFaqxaC9hZGk5I5I1Fk1oNmX5IkTsL_N_P-bClhl9sIroULd0jJZpWlTgY_hI7jbRZnLBGLvxu38ZRX0xZf1Qlk4jSwnLvXu7nPKScx-PhNlDK7qB3WmIsauKWrueVK8ammChBydYC8UAYnyxegNtu1UvqjXEz0lX1oH_diVHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدمین شب ایستادگی و مقاومت اهالی جنت‌آباد تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/440786" target="_blank">📅 21:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440785">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSNuWtjifYN4rWB1BsXq0sB1LHdocJAy5KajRtpL9LppgoQe4W9p_wFgpd25kJuTu8mYostxHVWYeqYmFtKftgihg-YPnRTmtmL8L9zALVg7EGVNv-xCdZoSvMUuHzPaXiG1ImWgZmDu9i_8hZzVbjb9zUPHyj3ZHF72yMA3pAdOLC5VHtQ8371mBCPpGD5rp5eiSi0-lHZ31oqyPlPMciFmL2GTJC-SrtDVfanlg_tqc1GAKutLCeXxBwi8Ukmc6K9kZ9GqbWtezi88Hy8FvgmfVHijBHdCNWbYHXuw2zRUnT8HqmwbbSEEtbqvlWph4_MZXVZmnYaULoDySF9grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: از تنگه هرمز تا باب‌المندب و از خلیج فارس تا دریای سرخ کمربند امنیتی جدید مقاومت خواهد بود
🔹
شرارت‌های رژیم صهیونی و آمریکا در منطقه عکس‌العمل جبهه متحد مقاومت را درپی خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/440785" target="_blank">📅 21:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440784">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06f78a514.mp4?token=Dgnfwf2dRUhlB7NqbmekaU-H_kTBbQ5-bDOLEYjhrUssFEE2g5T532EICDKF81QlwtqFE9KU_utQc18tYDFr7VZANSZgN0j_37RoCpmt4_Wivc7I2lmyrf99lS87R-U2g4lsLUZBpfd7amGaEAkQDHqc5n_ISCpMpjXIHfYCJ80FkMQD4iT78i547WNntTo4WV5KD7jGrBCExxdpBZbGHVUKn7s4_BwdGlPNs11s5sKae0QOWHFqsifbivjuszGSVz9omlMET_kkRY6FYSKsfidT_EPRDDcQetbeYqZ7SHeWqyGK38HX5LrnGVtsvesKsWL5udszvpusno_ywYdMFHSVUOkuWUUdJHqv0NWUkuj_HYAJ-SaBDTdZ97ztqTDDS2FualKKUsvToMu5livkA5ZrZGRy7jgnBX6kj-QDemCm3aGbmzscHDCJ-WH_yFY5c1Bhtxhn9bnpFfrKEYP2iVQ8yL5G2N6xyFxqQhf0Kw5L3_yy2XfUoQ-qq8GxhxkfNpPeBr9OqZ-8ChV_dj3uK_0lDBT3dEeusNVYNoOtlVEHtvEl8NKA9pXFOX7on8Fz1zwKf7Z1r9sQ7lsP7VHAGm0aiPmSqL9JD9Cy1Vm99bbuGEbwXgCuvxzlcwUEV2P7jI4Evh2qgD2Uc40YhcgTiduk4uRuvYFTWK7kKVeIIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06f78a514.mp4?token=Dgnfwf2dRUhlB7NqbmekaU-H_kTBbQ5-bDOLEYjhrUssFEE2g5T532EICDKF81QlwtqFE9KU_utQc18tYDFr7VZANSZgN0j_37RoCpmt4_Wivc7I2lmyrf99lS87R-U2g4lsLUZBpfd7amGaEAkQDHqc5n_ISCpMpjXIHfYCJ80FkMQD4iT78i547WNntTo4WV5KD7jGrBCExxdpBZbGHVUKn7s4_BwdGlPNs11s5sKae0QOWHFqsifbivjuszGSVz9omlMET_kkRY6FYSKsfidT_EPRDDcQetbeYqZ7SHeWqyGK38HX5LrnGVtsvesKsWL5udszvpusno_ywYdMFHSVUOkuWUUdJHqv0NWUkuj_HYAJ-SaBDTdZ97ztqTDDS2FualKKUsvToMu5livkA5ZrZGRy7jgnBX6kj-QDemCm3aGbmzscHDCJ-WH_yFY5c1Bhtxhn9bnpFfrKEYP2iVQ8yL5G2N6xyFxqQhf0Kw5L3_yy2XfUoQ-qq8GxhxkfNpPeBr9OqZ-8ChV_dj3uK_0lDBT3dEeusNVYNoOtlVEHtvEl8NKA9pXFOX7on8Fz1zwKf7Z1r9sQ7lsP7VHAGm0aiPmSqL9JD9Cy1Vm99bbuGEbwXgCuvxzlcwUEV2P7jI4Evh2qgD2Uc40YhcgTiduk4uRuvYFTWK7kKVeIIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بعد از ۱۰۰ شب شما مردم بگویید...
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/440784" target="_blank">📅 21:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440783">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3LWwK49leNsM7ciOc2dptu8EatB4KQT81w2lyc4n1lohlkEJ5q9E0xW8tAvbeni2GJ1sSkJ9UrLPGU6xlN7TXJUXmle1E93PFefRdL8kKTfMaPB_037LWK1fGA-EHUxW1dXSp1SVN1QZwykQG93gYwa0KDv_SFXuqivOxhP4VpQVTZyEWzaOgS4odWx1IQhCG8du3afCyGpIa_QHkPsfwodt4info8GHHyY7LC02fsO4-kEQh4as6GHyYoZ0vYh0KDjLgjynaJ3Xtw8NHkLoMuJe_-YD5R_JdrvfFTLILaY5HuQJT7LdhQSLr6xFCuZoyCp8ddNCiffo6oSHThVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروازهای حج به‌جای مشهد، مستقیم در تهران
فرود آمد
🔹
درپی بازگشت شرایط پروازی به روند عادی، ۳ پرواز بازگشت حجاج که قرار بود به مشهد منتقل شوند، ساعاتی قبل در فرودگاه امام خمینی(ره) تهران به زمین نشستند.
@Farsn
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440783" target="_blank">📅 21:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440782">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5A5Ntwz9mj3DyLRufMayRDkVJiJKHEKY3QCEckngB_z2LVduyp17LytmCVYyZPR-43bkWz7LfSyRvrOb7Xd2tqWVbwhgmts_8b8ySb-D1x74MnDp40hY1jQGjG90DrL_G4LAipwGmSQlJ701TO2Zg7DSdM22ayXsFdGmsHJgUStGu0sMUjYSLw-F0P28i4cTxE_D38dtwXXYN7ncw_p3Nb8nnAgKhxAiy_pP1HInxlttZQB7yOTUqGd56EZp8GxSj8NIob4R5lIxpjB8I7VF7OND2qxtN7oPsFIhwxj8UdeRcZE3w7JaFePR5hY6aMaSE5SMg6eNow-lf8Udy-PAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع امنیتی صهیونیست: تصور نمی‌کردیم ایران تهدیدش را عملی کند
🔹
روزنامهٔ اسرائیل هیوم به‌نقل از منابع امنیتی رژیم صهیونیستی گزارش داد که تل‌آویو انتظار نداشت ایران تهدید خود را عملی کند و به‌سرعت به حمله علیه ضاحیه بیروت پاسخ دهد.
🔹
به‌گفتهٔ این منابع، اکنون نگرانی اصلی اسرائیل شکل‌گیری یک معادله جدید بازدارندگی است؛ معادله‌ای که براساس آن، هر حمله به ضاحیه می‌تواند با شلیک موشک از ایران به سرزمین‌های اشغالی همراه شود.
🔹
این منابع اذعان کرده‌اند که واکنش سریع ایران باعث شد اسرائیل به‌جای گسترش درگیری، عقب‌نشینی کند و در نهایت به سمت آتش‌بس سوق داده شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440782" target="_blank">📅 21:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440781">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
🔴
قالیباف: دست نیروهای مسلح ما هم برای اقدام همیشه باز است و براساس تدبیر و برنامه‌ریزی درست و تصمیم تصویب‌شده عمل می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/440781" target="_blank">📅 21:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440780">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌ ‌
🔴
قالیباف: برخلاف تصور بعضی‌ها که فکر می‌کنند بین مسئولان هماهنگی نیست، هماهنگی کامل برای رسیدن به اهداف وجود دارد. @Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/440780" target="_blank">📅 21:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440779">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌
🔴
قالیباف: ما در مقابل دشمنان ایران، ۴ میدان مبارزه داریم
🔸
۱. میدان مبارزه نظامی
🔸
۲. میدان مبارزه دیپلماسی
🔸
۳. میدان حضور مقاومت مردم
🔸
۴. میدان خدمت
🔹
سه میدان اولی، پشتیبانی می‌کند چهارمین میدان را. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/440779" target="_blank">📅 21:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440778">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌
🔴
قالیباف: میدان نظامی موتور پیشرانِ قدرت‌ساز است و دشمن را از فکر حمله دور می‌کند
🔹
میدان دیپلماسی نیز باید در زمان مناسب، این اقتدار عینی را به دستاوردهای ملموس حقوقی، سیاسی و اقتصادی تبدیل کند. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/440778" target="_blank">📅 21:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440777">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌
🔴
قالیباف: قرار نیست یا فقط جنگ کنیم و یا فقط مذاکره؛ بلکه قرار است به وقت خود جنگ کنیم و به وقت خود مذاکره کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440777" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440776">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
🔴
قالیباف: پیشرفت مذاکرات در کنار انجام عملیات‌های نظامی در خلیج فارس و موشک‌باران دیشب رژیم صهیونیستی نشان داد که ما باید درک کاملی از هندسهٔ میدان مبارزه داشته باشیم
🔹
ماجرای لبنان ثابت کرد که میدان دیپلماسی در کنار میدان نظامی می‌تواند دشمنان را عقب براند.…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440776" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440775">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌
🔴
قالیباف: اگر دیپلماسی را صرفا گفت‌وگو در اتاق‌های دربسته و لبخندهای دیپلماتیک بدانیم، از همان ابتدا شکست می‌خوریم
🔹
از طرف دیگر، اگر صرفاً به عملیات‌های نظامی و جنگ تکیه کنیم نیز نمی‌توانیم از حقوق خود به‌طور کامل دفاع کنیم. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/440775" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440774">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌
🔴
قالیباف: صحبت‌های رئیس‌جمهور آمریکا دربارهٔ یادداشت تفاهم، مخالف بخش‌های توافق شده بود که نشان داد آن‌ها نه دنبال آتش‌بس هستند و نه دنبال گفت‌وگو
🔹
باید برای دفاع از حقوق ملت ایران پاسخ قاطع می‌دادیم که به لطف الهی نیروهای مسلح ما با اقتدار به وظیفه خود…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/440774" target="_blank">📅 21:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440773">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌
🔴
قالیباف: ما نه می‌خواهیم با وادادگی پیش برویم و نه با شعارزدگی بلکه باید با اقتدار و عقلانیت ایرانی به‌دنبال یک پیروزی مهندسی شده باشیم. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440773" target="_blank">📅 21:04 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
