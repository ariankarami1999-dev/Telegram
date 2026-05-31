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
<img src="https://cdn4.telesco.pe/file/GyrzGtBQIJjVpURtcAMX6LUspG4VzmnDizIOQie_RKHl9s3RvXIbUDWva7RL9jwmj8UnwJU7d4QP3-_amWb1lxsO7bzGRwhu8Zxu3Ck-lSlTdhQTzjOsgpAVjmqjJ02jmn7aEJGZxOMMalioEsHOz3Ww9asYyX9Pm7KEjRoMvT8fiMMW2IVFCty0bkwQ4BLvGMeVekzAh8jcvJMgptnLm8ElVeczl2anHpribJRtKOpyG-8RhyNqvo3GSQI-senNCDLavdBCX1VTrJZi4PHToeHD4Gkc_MIMVOTpynK7YBo5I0Nx8rpFMzVkJm0uFLgyXV4lAoBSHOBUhDDegODkQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 16:27:18</div>
<hr>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmIvLdkJtJ-H4ashSsXFRPIF2CkWhQsvVcP72lPeieY88PM3NITPXi_o5ftMjwS0DAEThjv4hrDjv7-mBOIPN6xOENUH2SIVs5LRnBb2y510ZDXWul07shbE8j7h_46PJUWbZdC7NlKcKNGjiVqq9YsynGehqkp2LjVyzukxyu9P9fmE5sefN60AVu2SUx38mq6O-JzeKJIqZxAVxpIIyR4Z8DloYWRAuSn4W6z84JtzUZtf832B8MpJXLHq87KBTooL4t61EtXtSC9-weuyK6Bz1I5go74PyCH4oUO4P71WgyPftKVlHwvmmb0R8srtWUl4-gpXBbdiKLrMaIka3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3y5v9TVPX2Z6WqVIxW4dEikujMlxZ4gzAzRPSL3sRovpP2nrg_baDiavHpTCk-MfmZSKScdh-Nm73PYUbZfzg5sanuSn7zoMriKDP7Lx8tor8VZnl5HOeAl5Wxpn_BImobCzgi5PW33XDJDwdwC1Q2oKBgMQjfE8eqLSNHLLuH9XviY3AACVBk8rwcmwgDZPReky2rQ9lqbAOk7aBpJvzr-57J-MgaAaO2bBaDTCY3sfFevBvbUprbJ8qB8z_arJi-t5GhtQx8MLIPWptVCzgpLFVUrdaKRFpwCaHtJwKJKdyEod4BEvsOmgXCpQDMBcxHw1R2qQQc1MzVZZB4lIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=E00oJc9EyoqeLC8pfYKtV7GnU1PjpfQp52NStzGDesMeiWRzN31ZvuScumaLQpGr4kjo-r1mw_837f_Qhfk-pHVmgCsJRIY0ailiHVVcFBs7lgeJlfftf3-RHCGTnTbjeZfs_QVX1V8UprIHo7bXX0uDYqO1rFIY7hraDdrAQROLJx2Xt5IPa-B9vpTfJNdVjKko4vog43KaVpCF69MhVTq1FoYEBvwUPwjUAxJ4auP0e8hM0C7iDDRjyaPjLh2mZuG1RNi_KCtaBF0mdpo_im99niOO6M9BO3K0U07_l82wazuhdTjljbZeQ-otnpBpTp8qhWxokt_MypraXaXy0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=E00oJc9EyoqeLC8pfYKtV7GnU1PjpfQp52NStzGDesMeiWRzN31ZvuScumaLQpGr4kjo-r1mw_837f_Qhfk-pHVmgCsJRIY0ailiHVVcFBs7lgeJlfftf3-RHCGTnTbjeZfs_QVX1V8UprIHo7bXX0uDYqO1rFIY7hraDdrAQROLJx2Xt5IPa-B9vpTfJNdVjKko4vog43KaVpCF69MhVTq1FoYEBvwUPwjUAxJ4auP0e8hM0C7iDDRjyaPjLh2mZuG1RNi_KCtaBF0mdpo_im99niOO6M9BO3K0U07_l82wazuhdTjljbZeQ-otnpBpTp8qhWxokt_MypraXaXy0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=sfqjqhvYJHrUzDtd16e4xmZKH0NHJR3VrgtrifbD1As3G1OeH9C6HGerHNWNJFCFqSZFZ2no7e5xIo8W_IHQWuemBYJc167IoVgbxQFJY00pE45s1u-vmLA40gSLjWEAsbOsEYl7yK5NiOqyKBwysp0fgPlkvaFWj1zuaongXRUUfMgfpgVy89yAA1Ikn2-Dsd6LbZi9cJRTBAdOpN0w8Ifmt8Fa8CZQZUJ5pT9yrO_hyqX7eex-UHk4j0jHakCLj-nvUegveYRhX4XcSrmGwzDwhgiGBUKBv0iE2uhnjPiepXeTvk0RGkvmQ4OkiUq9uUjKL1q_sZOa6PSKFEUqWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=sfqjqhvYJHrUzDtd16e4xmZKH0NHJR3VrgtrifbD1As3G1OeH9C6HGerHNWNJFCFqSZFZ2no7e5xIo8W_IHQWuemBYJc167IoVgbxQFJY00pE45s1u-vmLA40gSLjWEAsbOsEYl7yK5NiOqyKBwysp0fgPlkvaFWj1zuaongXRUUfMgfpgVy89yAA1Ikn2-Dsd6LbZi9cJRTBAdOpN0w8Ifmt8Fa8CZQZUJ5pT9yrO_hyqX7eex-UHk4j0jHakCLj-nvUegveYRhX4XcSrmGwzDwhgiGBUKBv0iE2uhnjPiepXeTvk0RGkvmQ4OkiUq9uUjKL1q_sZOa6PSKFEUqWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRqi7Lfn_3lGj7QiqiQ_tX63UhxMLubkf4GHEN_vQrhKl46xrZcHPaOoC4VzH5cENbTIqrbK38mmnGeonjTOzPniZfk_Kk5JjqFtFnBEMIKFd698FHP3rFqYDnXnn_pCLjiFrhmOc3S60dgJkFtRB2UOb6ZugDbml9BOVBa5sKXSRR6zMNWOz7PiCwVAmZ4kuvqCFhEzDQR4uLIY4J7uhMI8Y7bVOy7YuwsF5uFABnTRVtgncdQ0nQSRBd33Zc6xpGxj6c9TZMKrNYUCmi1dlZhEK8vwjY6TYtj1gJOH2q0SZlOQSsTbqKBA06BAJmW2wCsjudviSNyO-QrgULKT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PchmgV0Pk6aXuN-ZVDCAogkduEMHwTwXliejClCzGghinkGUAXjyhSy-DTRnCWiYnsh5jOpD7E56-IYzfXjgD7M9VqTDJZQ_j4tPcotU37oskAIhWG3KpQFC-AV_tQk4auHK7__luKoEB2OTQgjRwCKcZTOLSSXcq2E8H5k9_tBhPh8NpbjvPfPdd0DSOH43SdE9Kx_QoJiCOcUlgvo8fOvI1QJ8_tWFh-txixRu6UQVRLxBfWamWQfbz8-U5Vhz5DNgAGhbO3VoRikaRV3GP05EAS12GQsEKsXQSd5P1LWwoO6ERld2gEjvMW2na8sBEcl0Jm6UB1gZ6LcETELg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf9AuUzZBGWHMWBK4_uVpkf08-DEgdMiEzGgZhpePCuCbzow1i4w_ZObT7Py8tunmAJ_m_QCBwa-2HjPrHg-AHCpkHGivXGSW1mdiy5u8myaZWBwgRQZ3sGy8ZPfoU2_JwA0Y8uc-Vi8DPXQDbbV4frshqi-A2wrhNRiR5k4mpprbR9jZJbh-AR6SWb_Nu_xSE3j243EGVPHv4bDjHh59QsEqLPt02_dNhhawFIpVj7qc-yHbiueSeccComI4jziZaxB9eQZFPboDkdspvgVUr3Fptc9b8G3YKhryHo0mUgzOpVGP-Jz-XFWbZsQ2e5BvkqlAzHjTclgNrmZOOwJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzg5-__0tS-5U3UwOwBgufgPSdyfkzsv5AVHjc7jLEHds9zGXbWDfeQsSPxM4qZOZO_sWOLbGvzgEyDBjTVbo7uUYMnL_2W5glcn6MucycUSKBQReRCdoyYXbzRRn2SuughsHqGXeqK--FQBto_StiqRAPkR_bsMO6qcdxkPHrCaMFzi6nQ99uYXLINnvp5fcJE1aT7QCcbz5d2awLdVh-0R04uCWNrnJqEqRl2hvDqlUKlc-24dsD4ffXO_6KVsuBPPc84A-iXxYNYYDgEDi-66X8b9BKugZGzfhfeQQteqz2cd-jlCAoxT-hm8uH0EgOgLY1HERMbhw3rBH6u8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgWGi2nrkK29-HZnRsEBwi9I1g5Id3cVvHExadPDdISuXoppw37-GEt_vIC_-VJvVy3KzfkgJ9pNqbQGaBIAlXCxJTOSjhswcjzZaQ54Qa8F0A759DEokhngaavvngcUoOqEoSWG4tdeISFVdtG3JiQNvjzinZ6TsZVw-hLntW_wgJ7-AcwPpXCy99Ihr2WaxFhe2gFPWQ9nYpsU2oCI6xfdiAnjSXH7mATPzuy0PyS-m3e54ORQcV5wtzrJXh8kZzd95zdZBbBM7cNO_fOpgzTi6pGCh_wuSlLgGRyWbWFc9XN-aj5dWENbJy_SFLfXdJGcFNQOa2l3GQvOFXzq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0G0SyujWNqYlVKFSb9AiIWOeMs7XCjoCWiCv-7plAUZZ-P-lp3qhp0G-TS04ES6RLACUySbHGPtL2iobTK9G4i_JmAkVUDM2nalGP_1kCXdC_mRaIrhAnDWpJBvPKkG3bBJo0hHpF_Hot3ID9iYSaoKPwurMzY3M-b5OGXdFQwsstc9FuMtNedzORPd42Va89NhLAzzzeWMbt0wraBZctbzNKFAZZvBb-WVcxiG4e-vVSTp7st74fHuCzsHwGRvXaOlf9pJy5wriCkJNOe1dBYRJQAqcoJTefCavhUlHJ4FLSFMtSJ_2NhzbwDQTD4290e0lUzoOKsT3IUEvTDlfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hhc1aWzUQRJdfj0-WfndOfmYzVmt147o45tLgLB08jclml1NZc7zHAJhLehiOiFaetT2SJhbtLKZV8C8mw2NkM8nS0qoAINOR_vVaqRns4Xl76Q26cLyZxdmtLox-tKzOdyCfgJSnhPIqq9_mTHjuBrF_f2uiSsI5LtCZb9b3hFAcAC0cnheaJxtpuX66aD5aUlLcCTobjJu9tNNdRbpvY68OoBQLog_9tRb7SwYWqKAsCkDWN7sX3KgD5bMAlXC0ex71RYlOI_4HDmGDJ_U7Jn2A98CLzf3fnad28w_UgMitCuDT_Rgc19EEiw4UOoevy4JWwv2mcDD7KZP-fLZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjRwW-fmklmaFCBQReABZ3Sym-EjxOUqvGnIahToy6Ub6FZaUrtcEhpzfYtbev4L-E8PYWv7WeLStNrJ_0hRvVAGKWVt13BVUGsUNcNTDxqdiCzjA6f-G8ywupitU0kkAwXySlUPBFJXjSnyKIkzOfNEpXn-oGNkDIfrFRTPGQEHAfFTGIl2XtOsLnkJ2ORo472kWrWyEfH9ulrvu97keV3IwYvIlMotYI0_Szu-y-VI8Ae-QUhDIwIwLIoNFX7ZwE9USX2SRstM2KBonZ7O1PfoGJj3yIf_tiHBWFDF2wO33igEBJEz8jEFbgHvy135soy3xXZMS0Qbon0aQ1hFmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=hdHTJiKPz8lhSmjhPQ4Vj0FuGAUY0RQoUHC6XKkKei9WAtkygj_aAwQq0yYMw4jmdnpWruOvixc2A9C_HA-C_oq43ABNvtRc_MlzJUFroWH9x56FQTMkqOi84arhNbScZ2RUAbhjLlAUEwxfjd-pfv-lYDErYlNB7IyAsLun-g6NGNtChopElToky4s6p9JB6LZH0tpSpD_u3zBUURGWTatKA58g9IrfCwksGP-s3Nzwo6xNMaRX6cVLuOgaXVMNJ75BB5FekTmxMZN9NUjzYk0mBjmVJmBLXR7ZywPAX0NlgA2r09QYLwIdetyO_cnXwbIkl9TQ4_rba7klgEmiRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=hdHTJiKPz8lhSmjhPQ4Vj0FuGAUY0RQoUHC6XKkKei9WAtkygj_aAwQq0yYMw4jmdnpWruOvixc2A9C_HA-C_oq43ABNvtRc_MlzJUFroWH9x56FQTMkqOi84arhNbScZ2RUAbhjLlAUEwxfjd-pfv-lYDErYlNB7IyAsLun-g6NGNtChopElToky4s6p9JB6LZH0tpSpD_u3zBUURGWTatKA58g9IrfCwksGP-s3Nzwo6xNMaRX6cVLuOgaXVMNJ75BB5FekTmxMZN9NUjzYk0mBjmVJmBLXR7ZywPAX0NlgA2r09QYLwIdetyO_cnXwbIkl9TQ4_rba7klgEmiRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=n5gOWGxUx-PX0TooQROhD7aS02-bZyywQ-hPXmn4Du23qt1vBHw8HpZKconEKGArMZLNLI0sNf9RpeP_dZu6gw9z_n6Ay_-VJVUT6qz3qigohL3KAUq7w1KPqqwUC1UaG7pEogDIGfmme1qlktn6Y5FHXKTGUWP5d1ERC7LIeI2PEyGHmcjvTnTpw_cSpNbdD8KjHM_YoeMRWLICunliKWQVkRKs0AKxL0RPMJKnUxvVYY3OCk5wb6fp1iYF7M8JN9-Oix8voX3k_4VCzpEULEMkV6yDJ7aMqadNjLqc74r1uypGpD_DWtsbhdfw9jgabn8goE79AHK0DPRCcReKbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=n5gOWGxUx-PX0TooQROhD7aS02-bZyywQ-hPXmn4Du23qt1vBHw8HpZKconEKGArMZLNLI0sNf9RpeP_dZu6gw9z_n6Ay_-VJVUT6qz3qigohL3KAUq7w1KPqqwUC1UaG7pEogDIGfmme1qlktn6Y5FHXKTGUWP5d1ERC7LIeI2PEyGHmcjvTnTpw_cSpNbdD8KjHM_YoeMRWLICunliKWQVkRKs0AKxL0RPMJKnUxvVYY3OCk5wb6fp1iYF7M8JN9-Oix8voX3k_4VCzpEULEMkV6yDJ7aMqadNjLqc74r1uypGpD_DWtsbhdfw9jgabn8goE79AHK0DPRCcReKbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQahXi5lC0w-fJzYAUXU4wn3sfrmCUhx_7RwQeVUsskltcvZ2oZq9uLhmZYSrglsMbdBTvrjFrN__heju8NjrbGU5mUEn9H2zjY-v6Fny5iXPQhzD2RnOyF9YEhZ-G3WooBqMGo-a7g19R4fYTktyQVwrhrIk8KlP1CxxYxpTySe7WH4Tm8tkTGCHitQkXjN15zu0pPqgutlOURd-8Ht3LSHcGp-_IaKuXyo6JojvY5ubPf2GyBCvWvdMW5IiUPuKxcx1ibzZ64folw2e6D_S_t-oA-e2VuiymFOlvrpaN0Ak6ceugvspO3mOk5CGknmTeae4hUS-g4ZbKGkdSbkHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lc93j-ZuO-EtJxgHrAdzHDEX6WPZ76dUW83HRmW8dxgX3uT_qGT9jQdIs0638ovkAUyqeGw0PBQOZrUa3f7jgZTxBNJ1o8nDmpFHMI-iuXbQomQ5fNR1LbGgBDnzleiVIw0sZnOXVsbCq3uIz9a_O09rHPX_BhksEmMMRpQ893oVAQRK7GTJ9kq8tDMCkIeSDKk3-UGw5-BaWGy6A0MCtRss7OsJdUMYUGXjErBBOvqnV6yJe2nvt-Rn8s-u_f3ZIivyecmn9kDUmMYd4zDhUr1gS0egQW5yLDyc3M6aen1T4LQ0qOg05iBJ8VnFGa2M38h7AhedJk1kxom0jd2SMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=OUe2a8qsfkQmc7zlxjog8Xg6JgaHt5I0SeuD_LQbMXegAGc9B_WcUsk9BQunLbbShJ2Ny4_SUv3Bc9u_4hkd2YLIQr7xT7LDFCkV6zOp5qGsWPCUuSrI_dQ8sD4dTjje9qhu-61ZqA2QxvidKWVg5fDJytj83EoOxjRG8AnKLpz2OuQ6VzsW-s14aF_qO0-xpoVx5AmTaYcK2wG3IiylBnAOSEqj-zLoVv35vPZVhODjl7lfwYYsxUx81OoxKVpZcdmZ5mZQSqDuR_2iyGQcCosFsOn85SU-7ghLDCsllXvrJ7RuIBpGUzn-1gLtePwVJkNUIhtP98N-DgrEipRH1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=OUe2a8qsfkQmc7zlxjog8Xg6JgaHt5I0SeuD_LQbMXegAGc9B_WcUsk9BQunLbbShJ2Ny4_SUv3Bc9u_4hkd2YLIQr7xT7LDFCkV6zOp5qGsWPCUuSrI_dQ8sD4dTjje9qhu-61ZqA2QxvidKWVg5fDJytj83EoOxjRG8AnKLpz2OuQ6VzsW-s14aF_qO0-xpoVx5AmTaYcK2wG3IiylBnAOSEqj-zLoVv35vPZVhODjl7lfwYYsxUx81OoxKVpZcdmZ5mZQSqDuR_2iyGQcCosFsOn85SU-7ghLDCsllXvrJ7RuIBpGUzn-1gLtePwVJkNUIhtP98N-DgrEipRH1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzH4kr6lc9HUptUSNP87zZuyGphHNsX4tKsgu6EUtdyudHfhHK2BhJ5PJRMr4kCZGIX5x5Jn5q9rFnO0ZDSAXV0niAVLyius6wPlSalbm9ILWDy2JNKmmh17byDZKS3rlRQg1Ohf7B-39534Qti77WD_Xk5NWoI7C-wsPK_6vdCAYk1GlQzSZu7kqp7leaI_7o1BmO5Ardz5Vw-62tImw8QfUdH4smU_gJ09mHfsxSxi7ap0mLmkNA_NOijuBJ1nbsvZ9HFUCeQFlEdRLdtp5G2HX-gaJr2CuAoi9CGhW66D3-aUkYiEBXJdMgpioKiz-fm1fzuvf8Ds0C894kVxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=U0wRv_blgs4gw4s8jwSBsQgZpEgmx9mjXiSC7rckBKFrb609WTOwMIO6iKF_aPJuwWKXXMqP8foGSKzjtnb-NLZ4Is9UtWHnYDsprPiAH93ztTe98xyGbe4PK5UTSMK2cQcFp8fqr1MDHpbuenNaRJdnifxi3hfXdw8cIdRHMgVA-LaJ_QGzystWdB_M99rpkD60CCuIM3Kt5el0ozwLPoXvN7pkn7bXoOiVEAiWvO2kot3hg9LxEuG3meKskxT3h4f2pH95nwXRIw-Y7WiglGSdf7TzBHqw4oKYn9lWzBXgenJu1-C7wYsfVE-3dHF6ZF-Xl6Cex2nQqgS_7-oV5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=U0wRv_blgs4gw4s8jwSBsQgZpEgmx9mjXiSC7rckBKFrb609WTOwMIO6iKF_aPJuwWKXXMqP8foGSKzjtnb-NLZ4Is9UtWHnYDsprPiAH93ztTe98xyGbe4PK5UTSMK2cQcFp8fqr1MDHpbuenNaRJdnifxi3hfXdw8cIdRHMgVA-LaJ_QGzystWdB_M99rpkD60CCuIM3Kt5el0ozwLPoXvN7pkn7bXoOiVEAiWvO2kot3hg9LxEuG3meKskxT3h4f2pH95nwXRIw-Y7WiglGSdf7TzBHqw4oKYn9lWzBXgenJu1-C7wYsfVE-3dHF6ZF-Xl6Cex2nQqgS_7-oV5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=lHjKtsuQdfPWTr22MT4Fw0FoYcnpSBcKN1cdE-BomXm2w1cP6mD9_j6nqraT7ce-qpyiBlzO-9ek9Lfg9SG8zvcjDrgP40RBtGaWOiRtj5Oc9boVAlMouQRS-eRBOdPQbniBiaIJAnS2ebCltfsI1dvFLynj0EiJC-Xh1NwpT2kSJsTV-9sBdqb9tr3an-yZAofPrEmnPtpZdvlzmcEmm_nqKAl6keq1AJ-vGY52edHk2xROl4n-LTKSZ2vtP_MiAfTs_rIt6mhD0TCM7nzJECkAQiUz98IR6a3irMIJQvPAiUpbpXKIS4804kih3_V9OT7aUJD7JYfbn2uTZF0vAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=lHjKtsuQdfPWTr22MT4Fw0FoYcnpSBcKN1cdE-BomXm2w1cP6mD9_j6nqraT7ce-qpyiBlzO-9ek9Lfg9SG8zvcjDrgP40RBtGaWOiRtj5Oc9boVAlMouQRS-eRBOdPQbniBiaIJAnS2ebCltfsI1dvFLynj0EiJC-Xh1NwpT2kSJsTV-9sBdqb9tr3an-yZAofPrEmnPtpZdvlzmcEmm_nqKAl6keq1AJ-vGY52edHk2xROl4n-LTKSZ2vtP_MiAfTs_rIt6mhD0TCM7nzJECkAQiUz98IR6a3irMIJQvPAiUpbpXKIS4804kih3_V9OT7aUJD7JYfbn2uTZF0vAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=pJSJ3TecpyBIV-RiTySez76tyhCu9hefr9BK0oJqRTd83stFr1_BlbcShIlqOgFcVPMOsSwJjWpkLw-5fHBnl20D4BJW_Au7JWEl_oYspc0G7jjE5de7N2Xt8X6az5_hLyBJSCvFmDd56M2dAWpRWfbe0TE7myalqPPccMdncUT3cXb_qpfAH52_TI8IivEzv3lu0-aBSiVkcpW3Exxtk5VX1CKTDZVtHbr7U_T4YenUZQAMbzGoaun2Q7kalDn6RjOkuZOsShl7pc_Smi86HrDqj_2H-7j8PI3vRwb-CJfPu2Stxdii2ZOTRkAw91g9_crTkUA4Gis-F7REFA6lsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=pJSJ3TecpyBIV-RiTySez76tyhCu9hefr9BK0oJqRTd83stFr1_BlbcShIlqOgFcVPMOsSwJjWpkLw-5fHBnl20D4BJW_Au7JWEl_oYspc0G7jjE5de7N2Xt8X6az5_hLyBJSCvFmDd56M2dAWpRWfbe0TE7myalqPPccMdncUT3cXb_qpfAH52_TI8IivEzv3lu0-aBSiVkcpW3Exxtk5VX1CKTDZVtHbr7U_T4YenUZQAMbzGoaun2Q7kalDn6RjOkuZOsShl7pc_Smi86HrDqj_2H-7j8PI3vRwb-CJfPu2Stxdii2ZOTRkAw91g9_crTkUA4Gis-F7REFA6lsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=M3iV6-3xsbxvU9Wt4BirOVWrNDbXk0fYppcMdBYQ3pwm9aBZ-P9XDhXZv4zc_qXtdF0GU0V6r7Ozukgpd5bn2dxyI2CXro97Q8YjvEEtYZfCC8rmxPxL3ok1wQYYxvSmHlV4cV0JnPtMEI8qW7YpzvE8b80qHEoSFYVCPNq704oZwK0KnHtvRz0vwgNjShyWpkkw5e8GZM7_G1XSO65t4wMiDa-y4B8_M1FVDhOkkl5HcIcgcSWKnJuK2ogWM0C7es0KP7HLHgVd-otGOfUNVcHQu3ZgolMDG6ggEJdL5fGqWLTcMT_thB928HdzGIIJhHqKrmrvj46l7U2lEff5bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=M3iV6-3xsbxvU9Wt4BirOVWrNDbXk0fYppcMdBYQ3pwm9aBZ-P9XDhXZv4zc_qXtdF0GU0V6r7Ozukgpd5bn2dxyI2CXro97Q8YjvEEtYZfCC8rmxPxL3ok1wQYYxvSmHlV4cV0JnPtMEI8qW7YpzvE8b80qHEoSFYVCPNq704oZwK0KnHtvRz0vwgNjShyWpkkw5e8GZM7_G1XSO65t4wMiDa-y4B8_M1FVDhOkkl5HcIcgcSWKnJuK2ogWM0C7es0KP7HLHgVd-otGOfUNVcHQu3ZgolMDG6ggEJdL5fGqWLTcMT_thB928HdzGIIJhHqKrmrvj46l7U2lEff5bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=N0rUH0PQaV7R9Q-wrXsBnadQn5Ibavl71TgXeTQu4_xzzUWawnndNJeKIWwK9l1K58m-vZcBkVRbPoChRnBOx_b_wReHJEmwZa15Zx1Hb5sps0JvQodfEqJCG7l65IWrXABtGb3durF6_pInZ0QEajofs9KOCVym4hHZHS7g0N9Mbosj1f4bmACGkR0pC1esJwCUUtPtBrHWaBxIqJzkacfXuVrcZryfg7Xuc0pPIdD4NW0S9UareZtNYIRoq2Y2dkZXdszEUr43fdNxTpoa1TlE6QD-gSKYP0RqzA6jhP0OYCvG4jQnz_z31lgWy6ST6s_U09uFN3hfpY7xkiUKiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=N0rUH0PQaV7R9Q-wrXsBnadQn5Ibavl71TgXeTQu4_xzzUWawnndNJeKIWwK9l1K58m-vZcBkVRbPoChRnBOx_b_wReHJEmwZa15Zx1Hb5sps0JvQodfEqJCG7l65IWrXABtGb3durF6_pInZ0QEajofs9KOCVym4hHZHS7g0N9Mbosj1f4bmACGkR0pC1esJwCUUtPtBrHWaBxIqJzkacfXuVrcZryfg7Xuc0pPIdD4NW0S9UareZtNYIRoq2Y2dkZXdszEUr43fdNxTpoa1TlE6QD-gSKYP0RqzA6jhP0OYCvG4jQnz_z31lgWy6ST6s_U09uFN3hfpY7xkiUKiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=Ljt4lLdQFgCRQvTWc16BzpzTnmOTq8OLs7vC5OHXaMfLECRa3oqR9as4cZ7QP8PMq4O0Oe2IRt2-OlkOYeNlc0vK-I8_89syWkMmCVoPRoEwN5dX_I4yRyFO4oIoUfi-iVJTSTdNWK9pAU84e1q0nII6NE0DNrb15-UHbmF4g9waWP4jzgzcO7oq7zN8NFWpK29j-wGsoTXwPa_gGCe54WXsdCtyTjO9YGD3_ktVp0a79qRqnvYJShXhECvnh6BMGfFq96tMgRyjUEtE7K9mDAxdnxXDCka0z8Hc2krYmr8pmHjkjp6NGBrxPfv5F6V4nTgwTTnX9Lhxzvktfu2AmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=Ljt4lLdQFgCRQvTWc16BzpzTnmOTq8OLs7vC5OHXaMfLECRa3oqR9as4cZ7QP8PMq4O0Oe2IRt2-OlkOYeNlc0vK-I8_89syWkMmCVoPRoEwN5dX_I4yRyFO4oIoUfi-iVJTSTdNWK9pAU84e1q0nII6NE0DNrb15-UHbmF4g9waWP4jzgzcO7oq7zN8NFWpK29j-wGsoTXwPa_gGCe54WXsdCtyTjO9YGD3_ktVp0a79qRqnvYJShXhECvnh6BMGfFq96tMgRyjUEtE7K9mDAxdnxXDCka0z8Hc2krYmr8pmHjkjp6NGBrxPfv5F6V4nTgwTTnX9Lhxzvktfu2AmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nj95zVHLplMZ-Widbp5pR6FBGatmTjWxO8Z2KhOxyRBI20WYVlMs88beK-WhpZm02Wm42LA5qbpI8gNjVVTchd-4MqS6O0hoDz8cLuFd0J8UFC9Ow-sDfeDOLdGRQIs0_acD9WGAJU2IBiOBPVTt5pAUpDwuIypcpk81N3oXHlirb5e2mF6S871KYmhKgkIHCMDokVdx3JcAfzEUkt6VuQGw-6OiTILtMwI5YIDpqCafZd5PBc1FrpE0CzDRsjD0XVGEWlvvR0oweiXoPIeRm8wbv8XPvieUHljvrj7R_B56VhlQKAkkWWCrgF3ZOr9HFUbIeMfxBzeI1BsBHXjI2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=pc8iTCMEESYgiGo-hiSCeNOUbamq6rSi5SkkSIhqn5RAuW3VO-LyXoF86NXJsqQzkiUZS2qktP8fTzceg406hfCE4Qw3Ai0vsDCKg2dAyKmeK9ovMl3wyQeG4xebT0I13rtFTCDuNuw44QYig3qeay7RnMY1HN69u4F8UQSfTapuu1nsC0pkAwOed6FtM-ikKYON2ecjBQL_znLZWSE9CWUz_ctSm6EX3yJlK_AwlNCIQZ7CUH5MNrXoZAYsLGk0WQ20a73HQ7Q5FTNheIjvoHQ9OUddZScwrXU19fWg4z_kkTZ876I-YGwf7zDmceynBF_LnVSuJsru_vlkY21ZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=pc8iTCMEESYgiGo-hiSCeNOUbamq6rSi5SkkSIhqn5RAuW3VO-LyXoF86NXJsqQzkiUZS2qktP8fTzceg406hfCE4Qw3Ai0vsDCKg2dAyKmeK9ovMl3wyQeG4xebT0I13rtFTCDuNuw44QYig3qeay7RnMY1HN69u4F8UQSfTapuu1nsC0pkAwOed6FtM-ikKYON2ecjBQL_znLZWSE9CWUz_ctSm6EX3yJlK_AwlNCIQZ7CUH5MNrXoZAYsLGk0WQ20a73HQ7Q5FTNheIjvoHQ9OUddZScwrXU19fWg4z_kkTZ876I-YGwf7zDmceynBF_LnVSuJsru_vlkY21ZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHtPEU5KfzuSroCU-I4nTKoTYBxcGrgeN6jHXWPDkZLzYNNWCXNqaAnCvHvYT7nz2M9Y_DFp2unNz0V6FUhzDsIJXHmqQnhNqyQ3or8wLCRwzT6c34YDBmomUA38kmg_4IdWpvr-8LQSxAA3ctli8sbbq9n8fGURae7UzLRsib35TN1UqnxDYNFvEK-WCDsmQIcr3JDcJvBIcC1VovbvIL2IGz8FHLBHBeF3bcWdTPQR9UNEK4_nVvh1zzLuqiSIVYqAj8G5aUNuaJKenEdJIBuRJaX4Yqr_RiKgqVX5MvMzd6fGlUHQP-AT6E5C_Ymm9Xj4FiJlT88rNbHPlZ-8hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=BRSUNz-Vm1cMOzPJjADmyYCyvTHaAmLQ1UlNtby2B13-NX9ySF-x-9QYxPuhuaIyTgCkED6Hqmva9FpklU3bmAtmsQ9PQ7GLHS8wSOHZtwCVXA4Ro6XtB-Fj0CjXNDPbtMf5lL9_FJ3c25ihlbbsQn9hMNu3kZUTrrUQv35Uus1V3vGkaD5YXZni9Af1TkshpqhkYO8F1EdGHhsDK_ZFHQsynz_oAYVR1ZUKe7pZs0EsSG-ov9q4RxrgiWhRrJmS0Bon4hLUkszu4O0CvQCWqq2dmzU8ABsdzll5VVyS14KnSlM1GjIkx2p2ad_Iv4TO0Ol4JQKvElHg72wA9TBKdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=BRSUNz-Vm1cMOzPJjADmyYCyvTHaAmLQ1UlNtby2B13-NX9ySF-x-9QYxPuhuaIyTgCkED6Hqmva9FpklU3bmAtmsQ9PQ7GLHS8wSOHZtwCVXA4Ro6XtB-Fj0CjXNDPbtMf5lL9_FJ3c25ihlbbsQn9hMNu3kZUTrrUQv35Uus1V3vGkaD5YXZni9Af1TkshpqhkYO8F1EdGHhsDK_ZFHQsynz_oAYVR1ZUKe7pZs0EsSG-ov9q4RxrgiWhRrJmS0Bon4hLUkszu4O0CvQCWqq2dmzU8ABsdzll5VVyS14KnSlM1GjIkx2p2ad_Iv4TO0Ol4JQKvElHg72wA9TBKdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrE6_z7DK8bxObIWnyaF9LDZk36z8qfTQeUPsSl1vGONpzXXRFCz5OGLOLXtkm2PeClHjQh3SwyDtIM7PYWeb7X29EcLq1z-DlFyHWONDaHGFO1D5EjVg2nTjvx1l7NmXcN-gP8EK3dFDsyYH33eX0tJzSJJoE8K9e9NWzlUBH5NGsxxzQ7FNw_kSWsENZhEwNrcjMwBfzsk5mmv34XbAQ9nS0AO-R0HvVz7R0tI99chZ9XMYfUaVoyVD9vnoAbWUtmvpVrLQCz26NQTsll2US88q4eCKCSeIGs6cPQxBJOCPi2y26i62ARQAp7LeF0ktT8lTe2xAWI3l0BdKpFP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkkTDO6eAbuaDvAozdVUbLU4cQJRJcM8s1IlbvQB-RZ1HiORv5ZkDTikvqFTCtpCO9zHL8lo3B16pIMLLkEXUB4w2LzhU7j1KuuZiAIVqL7rBKya1frvtrcD4pZLXufdS0mE5WGlZXeFwP1jJBn96WXUn2LQwQM9Hu1H_i8y8ECwjxBsG8JYIyTP_WCa9Fyl-rdZaW5XM1dJOlpTVTeEVWeoCg5RmOZ__ZRVoqftTmh_pYBWlU8mJdBnaUHjON9n84gmhq3AO0j_pZ7tEiB15T4bCCKg5IZmrI3o-ifSySHAViWvUT9XCW0qWgu6GqmnTkrsxXjLIIxfKf2Da7gQRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDzz38TKt0HtRulzDiifHB0u04jzci0xmAcoC9EbNe18V6K97HCOw5EZ-3naRd-f_be8F4fh38TAdZt-ne3rHn5QWdNL8tVO5pMJx8TZugjx1tpgdnZi_wvGZhPjXBO87-iGFsSDFMxM46XKhCFA7-FohvmdCaHwjKn9qybrDjC6Wb6l5_JEP5poSDQtrL6rEDZHzScrD32C3EtSUve6B_lRORUZKLMTIj8ddHrzJzWXWwMrpEpngsRYtexCD7J5mHbsS_4Xr2bUT1K73kAr2vXTRhhILxT40T-zzqVFKO1WfZqnEcsvgIHpEU2Oc9zB0nokFYYIh4p5KKcUuXHm8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLrzPKHcxE4amsyVnTgcruYm99sp_mJATL9bX2PfDuA93AEgbpW8LT3Xslrnrj35vfVK3dGsBGSWhjKj8Odjy_VdFWZVykV3SYQFm-nD3r2U7JW5NOzYTfdNY-7hBczfNkY5f6cUQP53ZmNc8V3qKS_77ijP8tnNMDEiL63z9i62REZB6mRpKgdqzWnQjS6aNO30cPQQ_eHJDU8Ot4if8IaFeQg-ddEYTRJ_7tJ9_nLRwS7kmz6LVTGyUfkBD_xVPvd_2E0h0SI-ifvguInq_paUlOq8YNho_32pAO4julzJhn9f8d-oS60HL9ffNTeYiMiAmgAYhTwYNKVVSkmcXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKU4w4XKD9e4L81yzW4ZR_UGEsmtLqD_hAk83Wfhx-57ZXrXCAibBkw9A4fl6uBVBaqnwRzUPPBRfCjVx2PasBrZf_W2lhs8MR8eHTsB-HUsO7r9Yx1qEx9wWrx-uv2dwS_EvK3CO54R2l6fA3DLNaLVnSFx2T5W_inGNbfFuvyC7gqEkKmkhTqW8Ukl0ERd_JGvvxQJzwVcRvAHriiSER7wuYakELkGxdb56bm_7UWvhTy1VpCkOaLJUKpdaAeVUdnA1ImNkIb_Tl3VDEfCZvchHbeCCZuVci6BdoYFCbESR9w2Ch_8K_g3kXTgApJimZEZ1VUCxq9yOcoqFt6S8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsIWB2S826ZyRHV3hB0bB3RBwLw5cUNWjDtgUk0USzSFMJjvVWHEtZVBHPHoOQ1yL4vWMGxh_aE1OnPgTNcbfqP38eMqzMKi5-CXY71VvmypYQRFsTCLaD0y9EeO0YbIdHpPJsHrlehxHtky1f8tOerqu7fJGw7kg6SuGfR_9FIgeROJJFj--pHSPXs3ocfSpuBc7VD9-GAvUWgVsKdomnIZ3NVRQp6EXW8AbItimm1ooZviNxEhWYW2DOSSKjhUMwCw9yKZu3zBMLbQSElLydORJKDN02AR3x8_25DbQuX2_st_Jl3DyZu_dOs4FtBYOn4_ikuMf4K76msphGkAOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slS6u5-Ef5ux-TNaozMDaJ6RwVSVPAf67L_DE5otxO4Bmks25IgsG12zippeb6J0DdaldYtV7dNtWo-B9VB9mbhRrYjBCDCNV8iQJRQ8DxNrGgYGTXqrVKjSFgH9rpfddP9h9dR_LuhA6GKxu_eTJ6Y-fGGR6RzmjmdALCqDeW07xriiCV0eY_58kpH0P1kbw6DhQCZjTatt5kQofxxpWRopDH5KV_NjdT8fsoKGMebBZGfW0T4bbJv4K02CNyyX8PfxNn8PHZAdtJrHde8wQtLde6PUGqlidBE8IdexRrGkH9qmrcPq_38q5JCgDffKXuuEC-9ptDFAs90053mg1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1sFnhm3tdhrsvV-kzqRxX5-dEb8vJgLUc1yNiYsbnjXxZAERpd-RxvDfG8ZhEsh2yPfskXS__v8ie4eJz3HKboqRJeZs90W9e1GPymk5vH7HCXzy9Fi2f-B02hIOqdZvNs8QWZyQ636g8nYqJSunpku9w1aDXjFU1z0Lqi2_4GeqQnl1n4KHeEFDRDUB8NpxCzylpppiHGHjgeQkmzCEqklJUixvf_ySJep2yDPAFOvZcLBo4-DVExEoBsOgkeSXfj1BuGHQqaiLFQBTPFWOoyVxKAwe4Z56tQxeL_aPMurk9bdUj6Xgq9qeu0caEku0AlCGS_ulFutGDs3z319-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=d4hKZePEJW78QPZcYbcZWyW_xzTxx2BsW6qME-XjE-ZKNXQ5zRfao19jjX2CIKGrTbA8eB41qGIwmwn0HrjMyt1et-usZFMfdsjSw9yc2jUPt7t8YKfXxDfrrxDZ40GlSbrFKbXJSmLbmkj21CdntDxy6umjlse5MILRvDmBek8IETqvbr7tttEwZoQpNI6KWT9Qd7okaEQ_8dNXbIX7bj3myyXQj1qYXObRnLegmVi9ruuMTsrRXkTdhfgadyO7hFIJonrgxdzriD3hcYWs9l2W6UaOIMZoxoKTK-tOlk6nHlHOJ5cG6ivTqfOn2aUy4oTxEhYASDc3KfssLdMNhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=d4hKZePEJW78QPZcYbcZWyW_xzTxx2BsW6qME-XjE-ZKNXQ5zRfao19jjX2CIKGrTbA8eB41qGIwmwn0HrjMyt1et-usZFMfdsjSw9yc2jUPt7t8YKfXxDfrrxDZ40GlSbrFKbXJSmLbmkj21CdntDxy6umjlse5MILRvDmBek8IETqvbr7tttEwZoQpNI6KWT9Qd7okaEQ_8dNXbIX7bj3myyXQj1qYXObRnLegmVi9ruuMTsrRXkTdhfgadyO7hFIJonrgxdzriD3hcYWs9l2W6UaOIMZoxoKTK-tOlk6nHlHOJ5cG6ivTqfOn2aUy4oTxEhYASDc3KfssLdMNhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQXwtmt3oAkP_EUyeOc2MdpT2_lG40R4_PYM_kjaTKJeitqalIo7xRWBj_t4W0Mj6KhLT44jvSz-8wNPv1VeBrIRgFOzVkPa8lqhQrRC3GCOnv1IlRG2V8m0-TTIbpB6b4ym_qUU9awxVSq6qwvhBaDicBX_ikaaLOTcNywrSMJXlHVTRsfYgVHfs6ppFYSJWRQqkKhS-FTnwKn7eMpm6ue8M_ImcawYYBnmxeZClymvm9wf7wMBlr8JBGSs0jWVGhfz_uMsJo8TVNCy3KgaY50-XdunDfArwFHs4TM2HtpOnj1-it3U-mHOtaAteC6Z2R5FuH0ie5aWZet48bdb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2PxmyGe9p_I6A1oloo2_pvLbGc97f5DUnwITGetNTZaHcTp3gFo1iATH8M8ln8Vc6RvJAuR0TU3h0HLIxxSqL9PCHx3gUt0Y-rJ7PyQ9hZWXCz22VhmamacMEDWH-vbaQfezh8dNhbGterkqcOJ6kjH63uqQT774v_EZdA_kA1ruXw18R0NNkmjjIlyi10ZjsSrWNRu8qapg67kd0WuPkHNl34G0hulMLGBrazdLSdQTn8i79whVvHzVjEKGYHV7-1K3wV0IVc8sjCofxviXvTXzSEOtrDL-gq-YD517SAHJIRYqGMOKhFt8TCfmpmoOiwjYKdHIdya3zZXTAPVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j70w26V3xGtLOQa6vTmuS4dZU8CjKyuSHNFTU1bDrQZ2az0u4wKGQKFfuX7yGE2Sb-E9v5fTbV_t9efLuQk4rNEH7vIvRCfpGv187M5EpPE2mFcOQNpgC2X4EhnFaioQ2P-nDe7k2NlIx4v9JwmY8ztyxDNO4ryc9Z24UJRAKW6Bfi_rUOYICam0uDDAQdE4jRpHiTprmoyQvwathuuUDFDbwpQAiyTGUC3MNbEvXVEtPoboE3wp0z62tSjRUWpYr7N4A7WORssclqOC_ELEc8WYDq9IeQT47TjyNI0zLB7wqR9fNMrssUuwDJ-1PJKz2ZSpFrG8VccBRX66uWm8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdp9QlJaAV9OZupr6ILM-1y_UuGKm-Z1DExGhHZberPP1ep9Dy-Xet20VY8LUxS4YEKcgNJfvV28yq8xroUCeVZqJhj4RceeHVUBgeJ4d9fFyo_mBttzk25of8BArL3ZrTYWfc4ZMo4U6tyyYjB9dKFXWS8DoRjpF17hvj1pcztB7GePYk8CrbMbbZO-RdS9kAGh4wM8OTnuM5iBYBIduGkeLjdlOUi54JH8DZX1gQO8qJvKlc_Q3mQgT02p_L0lbEn-49OWX3KrSt3Ce3-wM6frwqki7C2p4ttWmumF43SHrtTOuoAquRZtx96naZrnbP1l8PGV8mGZMTTFofpbNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JH0K4-Dnl1YQp0Vt4GniT344sTbrzU9MIQkzzbdAMPzmP02aj6Jm-4gVDUGH_TUFziArDilwMOGxAxjZdal4viymihZoi-YtJLDnWGJfz6VEQZqdhbTVE8oa21OeJeCmPyL_yDxvdxFNA-kuWkoLN-REUtFzHwntug_i7dI4RKypDN-UwYDdnxNiJTYw8rxyRdRsWk0dyV4UqK7Ue4tSqF98uo0KwclsRgKXxkacOMqmQRI59bTfvz4KBfgha1AxQGxVGf_C_tPh-KeTspUBTQh1h8cMWWaR3iOa3ubjqo0tiOuJfNQMCK4skJHzlwWGhjnueFA3uoAOcFaj0IL_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=nWiVf8JaQbnQAZqRAsBlTGZV2eDxcHrUltnU9fCze0lQ_H5rvp34bVYgwhqJ0Ll3OzbijZCTE3AVc2sGOllL27TF6Q8p5ktznJKilZj7ym0Z0ux8ScLiD1mMk-LpvNZFbN95Z2lWjxoXh7UElnqFbcBc0iERsqBO1AoPuEx1-D--jolvzG036hiZ1RvJBuSbkzbVkB6aSc6FD-4kVpQ2LMR8UHenUwYSgVmGJos0gti8NgWvf5o77ej8ALut5R5thjy7vQa8SJRgle4UF5oVNO_3ywi7ldrS0SkhNEm2xuDyi8zpHDntyi5aUFnU0v6uoDpDdgjzon8uWvS-oaB3rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=nWiVf8JaQbnQAZqRAsBlTGZV2eDxcHrUltnU9fCze0lQ_H5rvp34bVYgwhqJ0Ll3OzbijZCTE3AVc2sGOllL27TF6Q8p5ktznJKilZj7ym0Z0ux8ScLiD1mMk-LpvNZFbN95Z2lWjxoXh7UElnqFbcBc0iERsqBO1AoPuEx1-D--jolvzG036hiZ1RvJBuSbkzbVkB6aSc6FD-4kVpQ2LMR8UHenUwYSgVmGJos0gti8NgWvf5o77ej8ALut5R5thjy7vQa8SJRgle4UF5oVNO_3ywi7ldrS0SkhNEm2xuDyi8zpHDntyi5aUFnU0v6uoDpDdgjzon8uWvS-oaB3rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZyQP5Wg0_00In6wRv5gmFpKgKd51EytLdNzm9sw_pBvACiZlrEHEiLaYvfPBqzaJ1r6XePYEJsUTQAyrk8iri5pUMPGuUQRmqgrg-jvAynbxQgQcSO-w-LRxS7P-vo9j0PXFVa6k50BKhU_TKOrlSrGpj9NXuhuCEjCXtLT1rJiyBU17F_Ol6CKycN1YWwtRJNldqCep4QHnno3aj8vX4lUgfILl5_j05mFx9K3xyzvzD0Wy2pF1v05fq4ByF-u5N2TchY9ukFjnaEn-_PHTSdgKBbhDMS7foh3sPEayUD1FJOrdWoAuknMJ13AOneF1VrG76ZFKoHrZq_F9eWsrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=DMhnSMSkhYAqmVLACtsUf-8qsxCnUeEqjNDUk5JWkQH2D_XOGRK8aEJRX5r86hWsdGkxS2OtzXVtGqLbMRHs_ZdTTFOlGlNpCa8TnGuRvOv9qObl9vWXmR_0LlHeLmuOaUHtOUpsWvyPIt645P5ye43JZjpNNxKwv6K2WKnkccC5IGFLhvMVuQEpUttEJ6wxIPkih0VxE0cSLx_nZ9VkyExgpVmVemrs5YEvx1rFsb2bm2b-6LQ-gDKRhD0u_2kdEx1eKObE5PMuIeUOU7rXVrthfNyEdAy-ZjEnsW_ggUqysLu_aCg5_aNvvrCsMKCFcHDDuYO9X4q1zzcfGED6oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=DMhnSMSkhYAqmVLACtsUf-8qsxCnUeEqjNDUk5JWkQH2D_XOGRK8aEJRX5r86hWsdGkxS2OtzXVtGqLbMRHs_ZdTTFOlGlNpCa8TnGuRvOv9qObl9vWXmR_0LlHeLmuOaUHtOUpsWvyPIt645P5ye43JZjpNNxKwv6K2WKnkccC5IGFLhvMVuQEpUttEJ6wxIPkih0VxE0cSLx_nZ9VkyExgpVmVemrs5YEvx1rFsb2bm2b-6LQ-gDKRhD0u_2kdEx1eKObE5PMuIeUOU7rXVrthfNyEdAy-ZjEnsW_ggUqysLu_aCg5_aNvvrCsMKCFcHDDuYO9X4q1zzcfGED6oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=Nk8JWzmsfaB4eTypNShXYOKn5e5vftY30e93mDZ7axCI2jbklIeEdkqS8XSvCsUh6O8myLFfXzrfKXu51trlt5UmBKRwX3lQBT9stQpCuvry81OzgkLIPNKgXuEE4NP7tParKU78-3ESrRbTyDRCwCsrySTLHqvYW20R2AAKtfSHORxqk9laPs2_8Oy4FDHd_U2kty-ltXA4x508QFBRN69-8egzqKrhwr-SpS5KDlGxxCzue1rAa-0KmNJv74HlKG15MTBBixrRVMW7kyBfVyQ9EFwusYvlM-smh6EPYjCEVlFwKLrcky52lTzuQbPvFrp7S3PDH8bIK7pDhVCG2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=Nk8JWzmsfaB4eTypNShXYOKn5e5vftY30e93mDZ7axCI2jbklIeEdkqS8XSvCsUh6O8myLFfXzrfKXu51trlt5UmBKRwX3lQBT9stQpCuvry81OzgkLIPNKgXuEE4NP7tParKU78-3ESrRbTyDRCwCsrySTLHqvYW20R2AAKtfSHORxqk9laPs2_8Oy4FDHd_U2kty-ltXA4x508QFBRN69-8egzqKrhwr-SpS5KDlGxxCzue1rAa-0KmNJv74HlKG15MTBBixrRVMW7kyBfVyQ9EFwusYvlM-smh6EPYjCEVlFwKLrcky52lTzuQbPvFrp7S3PDH8bIK7pDhVCG2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-6gLuPRM_I2QIsqkvf8w6DswzPWIVnONVKrMWiWRoou_58RA6F7OYAU1IEWc0fZY2k-cjFdvYRisshmumT4GLMN77ilC3rXOAA5sOMXt_5d7SBfF0hqt6Sd-icX-g9oWUgD8Dvk3t_HN0kOW2WmsiSOiPAW9zxd988TTahG_8c91_KR2rXbik-ifOt9YbmaXlEogtGXC0TAM2fEM_pKnaFPTKxSlgPL_H9qgMAuujES7GBlNqT_ueY3XqzHktomCRyUoHMvv1WMNSm6KILUN_7YFV82QvqlhIiHXwYzq6riGeesxsUZLsci6LTMw9gYlnLgM8hm_pDRWwVJNQMLPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
🚨
🚨
ترامپ :«من اکنون در کاخ سفید هستم؛ جایی که همین لحظات تماس بسیار خوبی با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی؛
محمد بن زاید آل نهیان، رئیس امارات متحده عربی؛
امیر تمیم بن حمد بن خلیفه آل ثانی، امیر قطر؛
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر؛
فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛
رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛
و همچنین ملک حمد بن عیسی آل خلیفه، پادشاه بحرین داشتیم.
موضوع این گفت‌وگوها جمهوری اسلامی ایران و تمامی مسائل مرتبط با یک “یادداشت تفاهم” در ارتباط با صلح بود.
یک توافق تا حد زیادی مورد مذاکره قرار گرفته و تنها نهایی‌سازی آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد باقی مانده است.
به‌طور جداگانه، من همچنین با نخست‌وزیر اسرائیل،بی‌بی نتانیاهو، تماس داشتم که آن هم به همان اندازه بسیار خوب پیش رفت.
در حال حاضر، جنبه‌ها و جزئیات نهایی این توافق در حال بررسی و گفت‌وگو است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بندهای دیگر توافق، تنگه هرمز نیز باز خواهد شد.»</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8bEIMzNswH1dfssiUC6USuunbr8omYFaGzF0bLMvzJpilRLugxPXr3C1N1NcHppV2xaKJItP3qyIF9PylBs1hu3zTarh0piaN_5sPKNpLEEPImoVbOFQdFEEa2UpRzAlbHHjBgJYut8AFPj3DQ9B39-pwF3w8g08yoZ496a9km4h82mlrVNHIHtUdlYU-n8yI7iUvO8ESQmTwl4MBhKr9MuqsBiJ-ij9TyhQ676R9JCVOuYrtalgTCkbha-8li2Gwl7pvMaBkWYCSTpQsTMPSBlUxfG86diPX-byA7Z2uwc1MK4q-8E-ZEpQtuSsBCg43-Z7UzEqbtnm4tOqT7Llw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=P6M5WLIUWt5Fi9nT0PcdsvZWkBm54QUKUXYk2jTaJipBDmlRXeM-uw1UFbFwVxH_wENFu92I5GI6pN3if59P7bgX_aQ54tjAVd5crRQtuEg1Di0MK49qRm5gKp8M5lq5Zxi5FtOcpyGpFnKxJf6vYGJ49ImfNxcnNNOqE1zmRRrUP0HI1MwV2otmYaaJkbxcgkWrfvuUTeYhxyxyHPwNUitYjFovWw4R17AtfJPhekEKB-QaoQ69oqrfAgsrffHDe0RjGSjBoa_s12CTAvK6JT0wFPifepbXGOw3wLJJvwJKy7kFhqiIUjJehZXfF2ZM4rDs40sUpjeyGCU1Qkm_oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=P6M5WLIUWt5Fi9nT0PcdsvZWkBm54QUKUXYk2jTaJipBDmlRXeM-uw1UFbFwVxH_wENFu92I5GI6pN3if59P7bgX_aQ54tjAVd5crRQtuEg1Di0MK49qRm5gKp8M5lq5Zxi5FtOcpyGpFnKxJf6vYGJ49ImfNxcnNNOqE1zmRRrUP0HI1MwV2otmYaaJkbxcgkWrfvuUTeYhxyxyHPwNUitYjFovWw4R17AtfJPhekEKB-QaoQ69oqrfAgsrffHDe0RjGSjBoa_s12CTAvK6JT0wFPifepbXGOw3wLJJvwJKy7kFhqiIUjJehZXfF2ZM4rDs40sUpjeyGCU1Qkm_oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBqTxg44_AM7JpxWYvACUSh1bRQkkCr5Tl53OV0TYE_TccE-ALY99g4yb8Vi-h8ufL_Hs_aWW2ZeeUdNO0qvlZTr0bhXxWgCgfNnvEdciP1tuLsPqTuKTmbt3zO4F18MvkLgm-RecQzjocq5f1iEBy36X3AmSXRM7ddYlTVOaVrN-GBD-mhdOEdKnIFbBBEjv_850N-ynMNtvTLbmmR5WiEVYmLiGLs7ijlrl9Ti-oxw4Uc7Hz8KGlLtYFkz4q9_apNTgOCHgbJov3oCUxDLaSenygZnQ-1KpdEvenmJPBP1v2DD8LpFf1PaYHbWghnnanUkpspA2c2M1aVvESuswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال دریای مدیترانه، اروپا، نماد پیشرفت
آرامش، ثروت، هنر و معماری و….. است.
جنوب مدیترانه، نماد فقر و بی‌ثباتی
و جنگ و سیل مهاجرانی که
از این سرزمین‌ها می‌گریزند و …..
مصر، در جنوب مدیترانه، برای ۹۷۰ سال بخشی از جهان یونانی - رومی بود.
لبنان و فلسطین هزار سال، لیبی ۱۲۰۰ سال،
تونس و الجزایر و مراکش حدود ۹۰۰ سال.
تا اینکه اسلام از راه رسید
و تفاوت میان شمال مدیترانه
و جنوب مدیترانه شکل گرفت.
و دو سرنوشت متفاوت، دو چهره متفاوت گرفت.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8LtLzLl4C4VP2A4BUccEt9hPc8c1J5XcP0wBEla28mQJ4mD7Dp2TSZvdaOHHlXcscVKiKUPq2MWsugTh9C7C-vpgw324UupBdILYV3RCTlunrLb-HgV33Kq2CFYy2TcaC-QdWV1DuWgPzND31a7zbPUtElw3kKrJw9iIWauggdqL7VYkxttCqtVus5efLIe399rezDQSM4HMGoimfEipvw3UU1rUv4MBn5hczThxZb_ELhjwSqyySsrCp9b2iPxJNk9tjfHP_ouwmeEkkSMnnNadkQ5WIUTsjYk-WiPwawWBOiZ84nwSZ6dDtNwnGKvNlaiScebRGQHkTtDYBCtTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ8KyR7ClgPJEMgqgYRd2QAGWCM8SgZxbSD1f_IfT2Yi0tHEZ4ThqH33sc3tCMeMvjFGhBr5a8OnhfqZ346YeB4lTXb0C7m2pLpQ7npCrgc4mFuIOJ3cvpREShrUe06G3idNJKDrjhH4hijhoA7llq5u4RoMbzD45dBeSX54nJ7PX_IN-z7Oaz7niWw0VvciLZ5CE3mEHSOozQcKxTp_scDN612GuR_O5qnGDd7HUwi2yT2n9VIyorqbignxuKXowBnaabPNxvj95ph29toA1z_4CHF2E_0Qy3_ATg2jGRmjbEKffLhPMbQgtsvCvwyMNTqBYE2opCnp-VivoPAddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDQ2Ky-XoiJIvtVKWx_wamELrzoCXtPPSdgyyoocGKUVyDFKwCBiS35nNGqoX4Xquq0RCv7GK0kwOs4ChEjYMM0RY05POEm-QacTo2v6_4rzCywnvktTzJxbXptyJixtR1lNmjDGKrWXgbR9KuN3rHU2S79eswUrpegjU4UVi8uZgydfTYuCWozUV1MPTkwKz8shx9m9VLir1hqSvIq280ycj1Hjz7CDF2DQij3ZD2AbnAjxeLBwzKaYELVyY9Fn0PX2KZhki0Zs-eOBdtpx5wSKyHkr5Cpq0tHb6dTPvuODDa8nL7UH_1UARyNXlsNxMMMbufhGmjYrkDuEVUvgOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
نیویورک پست در گزارش اختصاصی خبر داده که طرح ترور ایوانکا ترامپ خنثی شده
.
فردی که برای ترور دختر ترامپ تلاش کرده «محمد
باقر
سعد
داوود
الساعدی ۳۲ ساله و شهروند عراق است که گفته شده توسط سپاه پاسداران آموزش دیده.
انگیزه او انتقام از ترور سلیمانی عنوان شده.
نیویورک پست نوشته که الساعدی از اعضای ارشد گروه شبه‌نظامی کتائب
حزب‌الله
عراق (از گروه‌های نیابتی مورد حمایت جمهوری اسلامی در عراق) است و گفته می‌شود
آموزش‌های نظامی و اطلاعاتی خود را مستقیماً زیر نظر سپاه پاسداران در تهران گذرانده است
. او با قاسم سلیمانی و جانشین وی، اسماعیل قاآنی، ارتباطات نزدیکی داشته است</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM0qwzroGIRNvDzrBjCiNyWRDbxPHJJJrnOrce8F7t2wbowgx7DAHiyvqKe3cDRspMUVEKa64qsVteFWvdCwfW6KkCumvpbOHl7_6Y7pG126NajhWluReNsm1F3gYsxKBuAgxfHFEMlsIlaPdR01vuWl72z_OGodGJOP6G6nkNoicoLXGgWRd9aqqGJpybvIscZXIdw6XWIo1g32lbwgYojqrQUaNKJzKeen4aNBtJ9AW3vninqSp36CGAQ2v6d2V-Vwomn3XH9hr_JQ8N5OsYD_x6Afl0PVrVwVOZv_avyMcZ_IlScKo3Z_cNPavsAHtEld84E-Ymi03DO7yoYAAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjLoaYeEdAhspvPI4bKKasMNWgUXOn9UNaM3QilXcg2outH-CX4Ehr9dUYVdEitUGRy8kzGdaSgLxdCZ1FjtkNm2Vt5uMqQNsiAZp52fZzXnoh3WdW3IULjPQ73xtRJcikgXmHBH_x5bgIO34XYIzJEhvMM81ezkOXrJgWy8vbwX_GtyzZxuQDOSLdlLvgPOCFxfA7Xq8LNo5zK_L39c-8ThRqwvF61JVA7Jlx7mr7vw1PdDxqYG85uDkHMQOdv1B3HMRrWZ3qczKv9ZCie-12fvVvkIcnKxUOtoXJ9BXGsbmzRuV4n7rt-04q5jVaFEFC3qtpKbq-tK2cAesuYrag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">مصاحبه اختصاصی با قرقاش: ایران در موقعیت ضعیفی است، دور دوم جنگ فاجعه‌بار خواهد بود
🔸
انور قرقاش، مشاور رئیس امارات متحده عربی در امور خارجی، می‌گوید دور دیگر درگیری میان ایران، آمریکا و اسرائیل «فاجعه‌بار» خواهد بود.
🔸
آقای قرقاش که در نشست امنیتی گلوبسک در پراگ حضور دارد، در گفتگویی اختصاصی با گلناز اسفندیاری از رادیو فردا، گفت که کشورش از یک راه‌حل سیاسی حمایت می‌کند، اما در صورت بروز یک دور دیگر از درگیری‌ها از خود دفاع خواهد کرد. او همچنین گفت جنگ کنونی نفوذ آمریکا در خلیج فارس را پررنگ‌تر خواهد کرد.
🔸
رادیو فردا
: آیا امارات از مذاکرات با ایران برای پایان دادن به جنگ حمایت می‌کند یا ترجیح می‌دهد آمریکا و اسرائیل فشار نظامی بیشتری بر ایران وارد کنند و همان‌طور که برخی می‌گویند «کار را تمام کنند»؟
🔸
انور قرقاش
: نه، ما به‌وضوح تلاش زیادی کردیم تا از وقوع جنگ جلوگیری کنیم، زیرا روابط ما با ایران در حدود ۴۰ سال گذشته همواره رابطه‌ای پیچیده بوده است. ما همسایه هستیم؛ تجارت، سرمایه‌گذاری و پیوندهای زیادی با یکدیگر داریم. موضع ما این است که حل این مسئله باید از طریق سیاسی باشد.
راه‌حل‌های نظامی، همان‌طور که امروز دیده‌ایم، پیچیدگی‌های بسیاری به همراه دارند. ما همچنان از یک راه‌حل سیاسی حمایت می‌کنیم، اما این نباید بهانه‌ای برای درگیری‌های آینده باشد. مسئله تنگه هرمز روابط را پیچیده‌تر می‌کند، به‌ویژه در مورد دسترسی آزاد برای تجارت و انرژی جهانی.
🔸
رادیو فردا
: پس در واقع، همه‌چیز به جزئیات بستگی دارد.
🔸
انور قرقاش
: بله، جزئیات بسیار مهم هستند، اما ما همچنان نمی‌خواهیم شاهد تشدید نظامی باشیم، چراکه می‌دانیم تشدید درگیری‌ها در منطقه همیشه به بن‌بست منجر می‌شود و آن بن‌بست مشکلات بیشتری ایجاد می‌کند. همچنین باید در نظر داشته باشیم که منطقه نیازمند ترمیم فراوان است. به‌طور مشخص، امارات هدف ۳۳۰۰ موشک قرار گرفته است.
🔸
رادیو فردا
: که حتی بیشتر از حملات ایران به اسرائیل بود.
🔸
انور قرقاش
: بله بیشتر از اسرائیل و ما همچنان در حال پیدا کردن پهپادهای زیادی هستیم، بنابراین شمار نهایی از ۳۰۰۰ فراتر خواهد رفت. کار زیادی برای ترمیم روابط باقی مانده و پل‌هایی که سوزانده شده‌اند باید دوباره بازسازی شوند.
🔸
کامل این گفت‌وگو را در وب‌سایت
رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRN4oAGpPnowuobufDQoSHkzM5rR9pDnQ6jDUkqsLNSe7bWiFnjyWY6PV2PbTdE0A9OEc8lWIHkXTrzq0VMBux2vekjizTMKdVm0y-mj1pM6JcA8MxuWR2kuV-89ggygFNxr0aADQUYK32czcIcIUM7ctUL9smXvJYSlt2FR1nCzdmGrZ1NL4QZhaOavTzXuCrfq6ogCNG5JcE98W5kuoeIFoVgF3lTxrg4SS0am3wkuQhgF8BaQa8bH4cHIzirxW5BXiNejSDLFYamI32PgQpRuBwZlI-r0M4UpwoNaB7fE9gU4CfmMnvTGoQKBCupupczQPFs4CD9xRGPa4Hz-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUch_h4aZdeSnKBpjK8KUr2H3LBmANWJKG570KlDj3f-f-LpVSbMSS1ruBbsBN3GNnL4NBAj8iFDnAyOAIPQyTv_nYSLuLCEYGeSPYx3_lfj4PUxdRY-SbKuuzTVmirHra-06j2ubYZRAG_jv6srKvvNVHNFL8kBDsFnOPQDLAC-l0zCnp_6fvRxEG7q8kqY7GhcX9-qZwhIrkMs1jlAxksRVHcXyTslPQ0qyoWL0jI1CDSzo80ddqyyeeuy6rlUu_7-us-osm6eb3xVLt22D0Zkrl-bB_ZmQ3RnRQFbhe9mr3GEzhHrWqEVaOPXrcNz_3WbS_werTNkgUlbpA5RNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVQ1-7BimE00RvNIi7aWv1U0twPT6NQEIOp5kaNCPQb8bbxFyC1v-ZPmNnyDrNV8e4UdQtjJ0JtLYXFW6PgsgtuAcICjQG8fBMuW2tgDEdbN21A4LFz4ubeBa6DVr47PJ22dGF7uovug7d6z1IJuDLhZpDNDRT_secO6pv76r-UfA703U4pn0bfPa2LsaXkozHs8gqu48OwrzWU4UkftyRDc9Pir1n8Ti-9VlNu0ryRkwCaPtfLXU4ynBZdDAhjraKnx6PbQxqn4V-gcYy1Xj8_ofXU-bGkvGZo5TBiynph50clQK-ZuKu_3KbHHTHRoowIIuLE3Y_TXO1W4RBC2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EibGhB0G81V3R7bb5g4Rsgfo3kZTWdMqzzqm9i5lQq35bLHdJre2pcsI_XAN741Ec7pugrsP6J2ZdkGRfh3mrkz3gwJaav3u4_jcQtDEKe2QG-YrBt-NR5XKR1W18VcjuNlnM0LZvA2Pawi2NGGFKk1lNpRzbWiXcTdyD_xRmiPbV7LkJ60cW7uPma9WOI1Aw14ijkrNh6k-emtvhYe_Szo_miCBtpE2DCH8YuFngGdeDlkfHqL8SmFnbgNmcvjWENOui-xFrIOALXLh26_DcDvncpDC5uT9lCKo2jz7J29Ifl-DnqOiOIVsHlpB726swlLPQKiL3tYBoQ3G4uPWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTSlMff8nScFjpMRZ4UPw4ajYgcBL7NE4T2GSmKxNbz2O4GuRcJC4ceygVxDej6gno_ElEDxngtY0wzNrxLt2GH0bs9ry-ViVhtieADjIUOQG04YOS3RBdZRnGztjfyVKQmCs8j7O2kzuZWQ4RMSWa1qZMGkOlv2HMwnU02zCSFeGiZRlaIzhJfiQ5vFuTv0m9sVRnR6GpkVEt_owcMaTbNk9EhuFBkXSklHWPH9JpSG841GhUtC4EZCT4xJSjVpI_eSXHP8RF0Dth2okF4tbWUYQKiKvwpToeIZ8NL6WvswYDT1FJro8dfAfp_TOKLvATfFp8UJoFWXzw6C-0L3gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=Bmxmio6w6xBaj55xN8RhWheixUPwu5qMgMC7vXyk7G6K1SC9mZWtr0ereSIcu9ftsWQGPPlhdnVV8zEZ_Z5udmKU3DHtKRioyiA3fgO4eDNMKjgpweTSyTg5r6y-vY5yHqHwJOKGlsNAGQARu7N3BZmS1TSyCI0M0Vmx43PKRI5cObbvbNhcY5gbjOGnK9dgSjei8Oek7YucVEL4YhiefydPjYpHpz54j3ZyGeChCzke8hc6-x3bG6GBAnrLIQr11r9Y8Nvn_-90mLu-kk76Wiieuv-65RBw9y6TDnSE6iCsoY4iol23Xhv85027CHxerr2rwy0XfvwEuuw8zHwkoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=Bmxmio6w6xBaj55xN8RhWheixUPwu5qMgMC7vXyk7G6K1SC9mZWtr0ereSIcu9ftsWQGPPlhdnVV8zEZ_Z5udmKU3DHtKRioyiA3fgO4eDNMKjgpweTSyTg5r6y-vY5yHqHwJOKGlsNAGQARu7N3BZmS1TSyCI0M0Vmx43PKRI5cObbvbNhcY5gbjOGnK9dgSjei8Oek7YucVEL4YhiefydPjYpHpz54j3ZyGeChCzke8hc6-x3bG6GBAnrLIQr11r9Y8Nvn_-90mLu-kk76Wiieuv-65RBw9y6TDnSE6iCsoY4iol23Xhv85027CHxerr2rwy0XfvwEuuw8zHwkoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=sXhXIjgppyYjQIsUIqoVoQmPl_ZqO-WgIzLD0R-SWL-08pZKPi2vxLf0rxwce3MTONEjriOmOisjpKCE8sQWq_sSbfTwPjU5a4fZ0W9FexqrIfzxw4teFGHAXydWlt4ZDgj3n2p1EsbMDxny1l6S3PfMVWv0PGEiBfJ5eGYfVdLm6l9yFRqdV1ft1oMhAVqVTisk9JMbj5xRLEvmREia3Z3vVnDFvPifwr9cVS6wXvjjw8sluraxXq-Y8XnfeQBRC1HLCQ5-IGwam6LFmu-M3SjJ3wSk_WM_BR8S0j2zA-ZHIhA-KFtzG9hd_SAwkCBKnua-444UyeW3SS6-lRXwqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=sXhXIjgppyYjQIsUIqoVoQmPl_ZqO-WgIzLD0R-SWL-08pZKPi2vxLf0rxwce3MTONEjriOmOisjpKCE8sQWq_sSbfTwPjU5a4fZ0W9FexqrIfzxw4teFGHAXydWlt4ZDgj3n2p1EsbMDxny1l6S3PfMVWv0PGEiBfJ5eGYfVdLm6l9yFRqdV1ft1oMhAVqVTisk9JMbj5xRLEvmREia3Z3vVnDFvPifwr9cVS6wXvjjw8sluraxXq-Y8XnfeQBRC1HLCQ5-IGwam6LFmu-M3SjJ3wSk_WM_BR8S0j2zA-ZHIhA-KFtzG9hd_SAwkCBKnua-444UyeW3SS6-lRXwqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
