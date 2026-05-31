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
<p>@farahmand_alipour • 👥 61.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 13:13:25</div>
<hr>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3y5v9TVPX2Z6WqVIxW4dEikujMlxZ4gzAzRPSL3sRovpP2nrg_baDiavHpTCk-MfmZSKScdh-Nm73PYUbZfzg5sanuSn7zoMriKDP7Lx8tor8VZnl5HOeAl5Wxpn_BImobCzgi5PW33XDJDwdwC1Q2oKBgMQjfE8eqLSNHLLuH9XviY3AACVBk8rwcmwgDZPReky2rQ9lqbAOk7aBpJvzr-57J-MgaAaO2bBaDTCY3sfFevBvbUprbJ8qB8z_arJi-t5GhtQx8MLIPWptVCzgpLFVUrdaKRFpwCaHtJwKJKdyEod4BEvsOmgXCpQDMBcxHw1R2qQQc1MzVZZB4lIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PchmgV0Pk6aXuN-ZVDCAogkduEMHwTwXliejClCzGghinkGUAXjyhSy-DTRnCWiYnsh5jOpD7E56-IYzfXjgD7M9VqTDJZQ_j4tPcotU37oskAIhWG3KpQFC-AV_tQk4auHK7__luKoEB2OTQgjRwCKcZTOLSSXcq2E8H5k9_tBhPh8NpbjvPfPdd0DSOH43SdE9Kx_QoJiCOcUlgvo8fOvI1QJ8_tWFh-txixRu6UQVRLxBfWamWQfbz8-U5Vhz5DNgAGhbO3VoRikaRV3GP05EAS12GQsEKsXQSd5P1LWwoO6ERld2gEjvMW2na8sBEcl0Jm6UB1gZ6LcETELg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf9AuUzZBGWHMWBK4_uVpkf08-DEgdMiEzGgZhpePCuCbzow1i4w_ZObT7Py8tunmAJ_m_QCBwa-2HjPrHg-AHCpkHGivXGSW1mdiy5u8myaZWBwgRQZ3sGy8ZPfoU2_JwA0Y8uc-Vi8DPXQDbbV4frshqi-A2wrhNRiR5k4mpprbR9jZJbh-AR6SWb_Nu_xSE3j243EGVPHv4bDjHh59QsEqLPt02_dNhhawFIpVj7qc-yHbiueSeccComI4jziZaxB9eQZFPboDkdspvgVUr3Fptc9b8G3YKhryHo0mUgzOpVGP-Jz-XFWbZsQ2e5BvkqlAzHjTclgNrmZOOwJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzg5-__0tS-5U3UwOwBgufgPSdyfkzsv5AVHjc7jLEHds9zGXbWDfeQsSPxM4qZOZO_sWOLbGvzgEyDBjTVbo7uUYMnL_2W5glcn6MucycUSKBQReRCdoyYXbzRRn2SuughsHqGXeqK--FQBto_StiqRAPkR_bsMO6qcdxkPHrCaMFzi6nQ99uYXLINnvp5fcJE1aT7QCcbz5d2awLdVh-0R04uCWNrnJqEqRl2hvDqlUKlc-24dsD4ffXO_6KVsuBPPc84A-iXxYNYYDgEDi-66X8b9BKugZGzfhfeQQteqz2cd-jlCAoxT-hm8uH0EgOgLY1HERMbhw3rBH6u8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgWGi2nrkK29-HZnRsEBwi9I1g5Id3cVvHExadPDdISuXoppw37-GEt_vIC_-VJvVy3KzfkgJ9pNqbQGaBIAlXCxJTOSjhswcjzZaQ54Qa8F0A759DEokhngaavvngcUoOqEoSWG4tdeISFVdtG3JiQNvjzinZ6TsZVw-hLntW_wgJ7-AcwPpXCy99Ihr2WaxFhe2gFPWQ9nYpsU2oCI6xfdiAnjSXH7mATPzuy0PyS-m3e54ORQcV5wtzrJXh8kZzd95zdZBbBM7cNO_fOpgzTi6pGCh_wuSlLgGRyWbWFc9XN-aj5dWENbJy_SFLfXdJGcFNQOa2l3GQvOFXzq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0G0SyujWNqYlVKFSb9AiIWOeMs7XCjoCWiCv-7plAUZZ-P-lp3qhp0G-TS04ES6RLACUySbHGPtL2iobTK9G4i_JmAkVUDM2nalGP_1kCXdC_mRaIrhAnDWpJBvPKkG3bBJo0hHpF_Hot3ID9iYSaoKPwurMzY3M-b5OGXdFQwsstc9FuMtNedzORPd42Va89NhLAzzzeWMbt0wraBZctbzNKFAZZvBb-WVcxiG4e-vVSTp7st74fHuCzsHwGRvXaOlf9pJy5wriCkJNOe1dBYRJQAqcoJTefCavhUlHJ4FLSFMtSJ_2NhzbwDQTD4290e0lUzoOKsT3IUEvTDlfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjQ7PCnJhOx8TwfAaZ3_6l7Yzh7TpgmQxNncHSckGd5COzf-k0kJxAhoUWNYR-zESKlKjJSY5X0gDx2fVTedNrMGW3GvVAQwLdFSOsZadl-zxQqzA4MGw0Nj_At0720cjrW9lnGuGfbyL2gdWPH5WJGsW7jumKNtOUyd5GbQJt08g7BCA6xtSDyXkbpJVDL_V0xakglW5lQo_vvI_Fc2GX6VyOyu-Hnm0G3kq-gKFvQ-ObUkRiOM6U4bMhNeNsMA-EEys-j-cJqpiK6nMJJrq-lfXDwz5IulQzt1q4gPtf09FZNsAkgaa8_nSIgARPtYpGIpJ_m7jh8NXU_rDrcIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/br13uVRb3SFFeaGRcVhImJ6MagK1i9dmvBlr5w6pajhUDnQJeBCT4C1rm-10f-ymKcQFs_rbUhIYGRopzlXA5e6oOiawDuKy5qOxV3SSiiBb0WX0GCqt24rUnc1NQ_-oixv8On3ye3IxGy8gvqxN38DSg_Wl-EN7gjlzAxR6UFAieA55VmzsS9v0_-qYkJPbATAzyehaEOm3jwG7jqtz-b0regKy2dGIz3DnPgdf6A4nXRXjvCFcBM0RpziWWh_w21qc365VmWcIk_ItjcYen-Rfn8eBLOhIcQI0C0gKkKzUgjR6BNDUI953ANlvFCqbmLg635rzFYTZvzh4CwDXkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=hdHTJiKPz8lhSmjhPQ4Vj0FuGAUY0RQoUHC6XKkKei9WAtkygj_aAwQq0yYMw4jmdnpWruOvixc2A9C_HA-C_oq43ABNvtRc_MlzJUFroWH9x56FQTMkqOi84arhNbScZ2RUAbhjLlAUEwxfjd-pfv-lYDErYlNB7IyAsLun-g6NGNtChopElToky4s6p9JB6LZH0tpSpD_u3zBUURGWTatKA58g9IrfCwksGP-s3Nzwo6xNMaRX6cVLuOgaXVMNJ75BB5FekTmxMZN9NUjzYk0mBjmVJmBLXR7ZywPAX0NlgA2r09QYLwIdetyO_cnXwbIkl9TQ4_rba7klgEmiRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=hdHTJiKPz8lhSmjhPQ4Vj0FuGAUY0RQoUHC6XKkKei9WAtkygj_aAwQq0yYMw4jmdnpWruOvixc2A9C_HA-C_oq43ABNvtRc_MlzJUFroWH9x56FQTMkqOi84arhNbScZ2RUAbhjLlAUEwxfjd-pfv-lYDErYlNB7IyAsLun-g6NGNtChopElToky4s6p9JB6LZH0tpSpD_u3zBUURGWTatKA58g9IrfCwksGP-s3Nzwo6xNMaRX6cVLuOgaXVMNJ75BB5FekTmxMZN9NUjzYk0mBjmVJmBLXR7ZywPAX0NlgA2r09QYLwIdetyO_cnXwbIkl9TQ4_rba7klgEmiRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=OUe2a8qsfkQmc7zlxjog8Xg6JgaHt5I0SeuD_LQbMXegAGc9B_WcUsk9BQunLbbShJ2Ny4_SUv3Bc9u_4hkd2YLIQr7xT7LDFCkV6zOp5qGsWPCUuSrI_dQ8sD4dTjje9qhu-61ZqA2QxvidKWVg5fDJytj83EoOxjRG8AnKLpz2OuQ6VzsW-s14aF_qO0-xpoVx5AmTaYcK2wG3IiylBnAOSEqj-zLoVv35vPZVhODjl7lfwYYsxUx81OoxKVpZcdmZ5mZQSqDuR_2iyGQcCosFsOn85SU-7ghLDCsllXvrJ7RuIBpGUzn-1gLtePwVJkNUIhtP98N-DgrEipRH1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=OUe2a8qsfkQmc7zlxjog8Xg6JgaHt5I0SeuD_LQbMXegAGc9B_WcUsk9BQunLbbShJ2Ny4_SUv3Bc9u_4hkd2YLIQr7xT7LDFCkV6zOp5qGsWPCUuSrI_dQ8sD4dTjje9qhu-61ZqA2QxvidKWVg5fDJytj83EoOxjRG8AnKLpz2OuQ6VzsW-s14aF_qO0-xpoVx5AmTaYcK2wG3IiylBnAOSEqj-zLoVv35vPZVhODjl7lfwYYsxUx81OoxKVpZcdmZ5mZQSqDuR_2iyGQcCosFsOn85SU-7ghLDCsllXvrJ7RuIBpGUzn-1gLtePwVJkNUIhtP98N-DgrEipRH1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzH4kr6lc9HUptUSNP87zZuyGphHNsX4tKsgu6EUtdyudHfhHK2BhJ5PJRMr4kCZGIX5x5Jn5q9rFnO0ZDSAXV0niAVLyius6wPlSalbm9ILWDy2JNKmmh17byDZKS3rlRQg1Ohf7B-39534Qti77WD_Xk5NWoI7C-wsPK_6vdCAYk1GlQzSZu7kqp7leaI_7o1BmO5Ardz5Vw-62tImw8QfUdH4smU_gJ09mHfsxSxi7ap0mLmkNA_NOijuBJ1nbsvZ9HFUCeQFlEdRLdtp5G2HX-gaJr2CuAoi9CGhW66D3-aUkYiEBXJdMgpioKiz-fm1fzuvf8Ds0C894kVxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=hhzjrIUPCyAxeHdiumXdZoeTVD_ye4iD20QMFJE_cxnkyLaO5Pb1oSHO9mJH5EwrwwMxDddRI5nwKQki2h6yabbKzz9w5Sh6x1YQZvM1M9P5Yan_LxrFXYwt1Hg_I_foTckf14iE4lhTbif-vaZ47ED0UQhq1TzeQkI0GwBCXzDwq83Zd3SXo3riPJ4CaMrm_psQPjFhz1pEQaxJs5IN5RINL0bqLAShignY0O7Cv1MB1DNZ1AWN55fiECEJf0qumcx1-ewY-tXu2abquXm8N_nrfuJ-4Ml4DrAErX-lr4sBk9ReS9QEgBdAkM6Z6H_zyc-vXiOhTEEHiZRgul8mgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=hhzjrIUPCyAxeHdiumXdZoeTVD_ye4iD20QMFJE_cxnkyLaO5Pb1oSHO9mJH5EwrwwMxDddRI5nwKQki2h6yabbKzz9w5Sh6x1YQZvM1M9P5Yan_LxrFXYwt1Hg_I_foTckf14iE4lhTbif-vaZ47ED0UQhq1TzeQkI0GwBCXzDwq83Zd3SXo3riPJ4CaMrm_psQPjFhz1pEQaxJs5IN5RINL0bqLAShignY0O7Cv1MB1DNZ1AWN55fiECEJf0qumcx1-ewY-tXu2abquXm8N_nrfuJ-4Ml4DrAErX-lr4sBk9ReS9QEgBdAkM6Z6H_zyc-vXiOhTEEHiZRgul8mgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=kkWCAYT6boA63iDEFKDldjaBURJunNS7I-pqKW9Y4q2CzT2_F4GWohilE1iZC8d-IUmMBnmsIK4_OvC6sTeqf6P7IZ0Cc0XvLFQywoLFGHp_GJsxDiupxyeUEcL_lO1pAyUAmtDHkzGb6aJc0tZ5AnWp1-yakxBllN-v4MpXFx8Lj3yQ9lq-PYQwnl2PuQYy90PE6HMdU4d91Eu85PPc9wpmclKnJn7fdB4Pb-INlJ2WzYvD67j4rICGGZqhzF-P_TUaFHKsGDn5_19IiX81DXJtOhtsa5-vErMVpj5RudZx8BEPgoCJGPNupeOMvQWDE8CRFrVn-S9luTPNmEhEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=kkWCAYT6boA63iDEFKDldjaBURJunNS7I-pqKW9Y4q2CzT2_F4GWohilE1iZC8d-IUmMBnmsIK4_OvC6sTeqf6P7IZ0Cc0XvLFQywoLFGHp_GJsxDiupxyeUEcL_lO1pAyUAmtDHkzGb6aJc0tZ5AnWp1-yakxBllN-v4MpXFx8Lj3yQ9lq-PYQwnl2PuQYy90PE6HMdU4d91Eu85PPc9wpmclKnJn7fdB4Pb-INlJ2WzYvD67j4rICGGZqhzF-P_TUaFHKsGDn5_19IiX81DXJtOhtsa5-vErMVpj5RudZx8BEPgoCJGPNupeOMvQWDE8CRFrVn-S9luTPNmEhEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=I3eUuOrTV48udjSuPJXGUG1KuOFUAZ76fMmJ8_bSlFE1MkoHq_7hjp7-dCyNBalFwJrRJHWeHmqDJRZ_BfOVGTm8jn68Rqz7jAKpsBvsJZkq415auAacvrJskWZUR3LiPkuCFwIMdqqUKZkIcFJpEQgm457lpvHVKgmKOxt5lQ-lqgzLMZ9lyRVkvO36JMvT1sAumendotGim3--Ii6MxGrwaZgqU9i119NzvZeBEV0iQWyCMY9nvnIBm2IRn_tDSN0F4gNAeafZGvqYOfE70B3YdGeU7ztF486-yVBZqdhmu_Yb5cfs_EPnWUykJEYoU_60yIoI0IW5MOc_aCWGrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=I3eUuOrTV48udjSuPJXGUG1KuOFUAZ76fMmJ8_bSlFE1MkoHq_7hjp7-dCyNBalFwJrRJHWeHmqDJRZ_BfOVGTm8jn68Rqz7jAKpsBvsJZkq415auAacvrJskWZUR3LiPkuCFwIMdqqUKZkIcFJpEQgm457lpvHVKgmKOxt5lQ-lqgzLMZ9lyRVkvO36JMvT1sAumendotGim3--Ii6MxGrwaZgqU9i119NzvZeBEV0iQWyCMY9nvnIBm2IRn_tDSN0F4gNAeafZGvqYOfE70B3YdGeU7ztF486-yVBZqdhmu_Yb5cfs_EPnWUykJEYoU_60yIoI0IW5MOc_aCWGrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=UE5StvsUViN7hPEc7tzIpcjKceCVb2iNbbUrA8HodtHUtpwvOguLX9uXHQtwWpSlz_cvV_5HbigeK_xb3gb3d2USJ27jSJ8mgMUTriarx6NuTstSPbIZDklazHERmnyZJm6s-1y9H3SwiJz7_56otS6DGuhEM_A5GVn4R5ZfKuY6IIeBGTXR0R6UJ8OgBTuq-ne9hzqPoqvF6CC3etBm6gnbZ8aJvcZ2eQyV9VHq_p36oQcpWJEPIPpAOt8lcH-7ghBg-31a8Y4etVAw0hlXq4xOyUrrRXktxwPdX50JHssBEde5DMi2n6QWarKZArJkymjLgkCrHpFpu7UjdbgVHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=UE5StvsUViN7hPEc7tzIpcjKceCVb2iNbbUrA8HodtHUtpwvOguLX9uXHQtwWpSlz_cvV_5HbigeK_xb3gb3d2USJ27jSJ8mgMUTriarx6NuTstSPbIZDklazHERmnyZJm6s-1y9H3SwiJz7_56otS6DGuhEM_A5GVn4R5ZfKuY6IIeBGTXR0R6UJ8OgBTuq-ne9hzqPoqvF6CC3etBm6gnbZ8aJvcZ2eQyV9VHq_p36oQcpWJEPIPpAOt8lcH-7ghBg-31a8Y4etVAw0hlXq4xOyUrrRXktxwPdX50JHssBEde5DMi2n6QWarKZArJkymjLgkCrHpFpu7UjdbgVHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=EYTmjf45pb2UKtLdicaoBgCR_WoWfiZVxbAaOqZYRkIELm1iVnDJuUg-AH9s2noPEDqFhTY3Aog_j7dxBPugqrIBCCeNj1iQAo_ufzlyhA6aNWP8RXV-mwLHqNMjBVnlvkgQbikTk0JFGhir6utAsngxMsIcnZuJWqaaq1-3lRcUMGLze0fDTgkM2BgXcnf9JilVbbOryn6aQ7tTMf8d1yQYHfx4eUX13d94J1u-_WI88-odMq7dPoCZLRdTaYrSr2z_-DZxM2gD5Y7SDcVRwB_b8OR80cF85RRb6eJhNtk1J48_2Km8oKOZRt34Xo4jTwD3-NsxwlCuFFb1pu213w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=EYTmjf45pb2UKtLdicaoBgCR_WoWfiZVxbAaOqZYRkIELm1iVnDJuUg-AH9s2noPEDqFhTY3Aog_j7dxBPugqrIBCCeNj1iQAo_ufzlyhA6aNWP8RXV-mwLHqNMjBVnlvkgQbikTk0JFGhir6utAsngxMsIcnZuJWqaaq1-3lRcUMGLze0fDTgkM2BgXcnf9JilVbbOryn6aQ7tTMf8d1yQYHfx4eUX13d94J1u-_WI88-odMq7dPoCZLRdTaYrSr2z_-DZxM2gD5Y7SDcVRwB_b8OR80cF85RRb6eJhNtk1J48_2Km8oKOZRt34Xo4jTwD3-NsxwlCuFFb1pu213w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=vKWHhdMN93eHmLa0XxJl-IdNbA84d6pDiaNNl9KbQN6nc2ODWvgxOxGTUKwvs3nyfnhdUEzmLbg4chq6FJW8MybrjTqW3tra1HXvKUgjayLiPWi8bMPsXBvD8-ovTfPm2x8hF55JyPMEV6Sy_if6RviWnzjdeZbJeRlQ8BPJrwGf86uEtskS4srzH-rwybS8VTFtLfReO_4Bh-USxg-VwZf5zrjWYaFwd0KhTV4S82y6xJSvinVMLLZhMfdYeJ69Njz0hNOOFjFXdkxZCtIjTsPPFE8aK16pGPTXAusBTcysLxkvNy7aDfn_DuM9U3n_ZTciV3sMruswzOPjDcSXAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=vKWHhdMN93eHmLa0XxJl-IdNbA84d6pDiaNNl9KbQN6nc2ODWvgxOxGTUKwvs3nyfnhdUEzmLbg4chq6FJW8MybrjTqW3tra1HXvKUgjayLiPWi8bMPsXBvD8-ovTfPm2x8hF55JyPMEV6Sy_if6RviWnzjdeZbJeRlQ8BPJrwGf86uEtskS4srzH-rwybS8VTFtLfReO_4Bh-USxg-VwZf5zrjWYaFwd0KhTV4S82y6xJSvinVMLLZhMfdYeJ69Njz0hNOOFjFXdkxZCtIjTsPPFE8aK16pGPTXAusBTcysLxkvNy7aDfn_DuM9U3n_ZTciV3sMruswzOPjDcSXAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1mdeJp08E4c0Qk4ZA70tbZFKzcTZ6-BzFzFbJD1vVVf9dlo3_7kGDOuEfMuov8LcsNzVcHnXjH7P7KVSimihN5CUmhtG3jBqngA-9QHPK4VgFkDvfRSuDleDEOyLjrAdFdG8xcSbD7s0IuXpiKMWzSXJ3TAEO2ikkEDgkG01DC0SGrKgN73E5dDUfBoz3NZ0aIj_lT8YjosjjIHcnrq-tUVjp_BR35kjHD34wZSnkAz6zckmWvckkN8LK09PCFwjgnYBc_-OdwugHtbBovu8H0uheW40j6Bt7ruFZeotPMLSeOWFFN1wWomOUqaK_2nKnj1oQS4bsfhxnyrpHlnZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=pc8iTCMEESYgiGo-hiSCeNOUbamq6rSi5SkkSIhqn5RAuW3VO-LyXoF86NXJsqQzkiUZS2qktP8fTzceg406hfCE4Qw3Ai0vsDCKg2dAyKmeK9ovMl3wyQeG4xebT0I13rtFTCDuNuw44QYig3qeay7RnMY1HN69u4F8UQSfTapuu1nsC0pkAwOed6FtM-ikKYON2ecjBQL_znLZWSE9CWUz_ctSm6EX3yJlK_AwlNCIQZ7CUH5MNrXoZAYsLGk0WQ20a73HQ7Q5FTNheIjvoHQ9OUddZScwrXU19fWg4z_kkTZ876I-YGwf7zDmceynBF_LnVSuJsru_vlkY21ZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=pc8iTCMEESYgiGo-hiSCeNOUbamq6rSi5SkkSIhqn5RAuW3VO-LyXoF86NXJsqQzkiUZS2qktP8fTzceg406hfCE4Qw3Ai0vsDCKg2dAyKmeK9ovMl3wyQeG4xebT0I13rtFTCDuNuw44QYig3qeay7RnMY1HN69u4F8UQSfTapuu1nsC0pkAwOed6FtM-ikKYON2ecjBQL_znLZWSE9CWUz_ctSm6EX3yJlK_AwlNCIQZ7CUH5MNrXoZAYsLGk0WQ20a73HQ7Q5FTNheIjvoHQ9OUddZScwrXU19fWg4z_kkTZ876I-YGwf7zDmceynBF_LnVSuJsru_vlkY21ZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iy7xkZLvgduXhZ2fOoYo1mWGcLlu_Mu403K3JU0EGvXbJmeU8sVo5w7_Pe9EqGLH6xhLOTFioHhIuIn5E5Dem-0H2kgC9mfLqezvBZ33Q_9E0nw_lnK441gJXkcL55VvqtG57yH2kG2T4gWIhID1D9DJzhyhzEzpMNqTP18iGTJ_7WdiyfApju6YSnSWN0wycqpAtBF4-KDOoJexHYiuvL5s6nM_AiSu-pgr_T7UPUKUX4f5NT2ZxhX2FKpW4sd3DAbgGSIDyqlE-q0pCb6_ch_OLc2Vye-8s37hcSfZhuhcUyExHRQx23HfhTz-DQN9sv5YdwhXlpZnDBtoec4rUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=vp-lagswVMg-4SjIOFTO3vRU18Rd-efTtX3fbcqcOejmpTGXYOkoYQHNbPqUHNESDwubp3ny-md-bVEsaOXtGZRiW60xJxnz1LW5aGvAx6c0ztFUWYcjt3DEGaNKAF6XBbcBEwcFT1cDP6y954YXh623HQX_Ft2r8gy_5eYh66nxnV0Mm9fuKOuDlju6AphmEGi5MePwQAv2QwQHivRZENWDfVzPlt5grqvigaGJMDB3JTdTBfsY7LsPGtWgd655A1jEIU3j1SGaDaU-Dht5n_WrpshovzIpQNJXUDKI4vNzflEZLRZnQRzr7a3NxHITTluiCKKQXQ7NIQkG-hbLQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=vp-lagswVMg-4SjIOFTO3vRU18Rd-efTtX3fbcqcOejmpTGXYOkoYQHNbPqUHNESDwubp3ny-md-bVEsaOXtGZRiW60xJxnz1LW5aGvAx6c0ztFUWYcjt3DEGaNKAF6XBbcBEwcFT1cDP6y954YXh623HQX_Ft2r8gy_5eYh66nxnV0Mm9fuKOuDlju6AphmEGi5MePwQAv2QwQHivRZENWDfVzPlt5grqvigaGJMDB3JTdTBfsY7LsPGtWgd655A1jEIU3j1SGaDaU-Dht5n_WrpshovzIpQNJXUDKI4vNzflEZLRZnQRzr7a3NxHITTluiCKKQXQ7NIQkG-hbLQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4bnqo8eaXwMrj9TNgVnzC561c9T45g5S_C7DHOlNHcIDzbsNqzZ0so9lnxzZUd0fH-eJXEmO9HKPfB3fLVWKZhEnLoOdmbnNZPLpuo1YqIKY67LOnRBul365p6hhG5QbzJup5mWun6db4LfyzCsZcXdkliOtzaDqv0jm17XoIElXxtWkXVvV6-O4SDGQH_-4wCqReEjzD5aINHetgkPNvLXu7s1B3ItZplVo3DdEesa51a_F75Kw6K-VhQ33WgxZnUaIwkUx6DF-HFp-tUsjBy_JGtNcnDjZ2HC6BX_F99Ybc3WlzRBHxJh_qPVNpXXWEdDom2GAmtILexo29YDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImLyB8ubZVLNRi2ChK4Rxgdinq6vv1CutT-SxdQmgX3-Wt1hfiSg2hJBhthGjntEHr_SL6Dvut09baKc840azfwfjd4olRBNMijRTXHogQVZieKWCNbpC2cxYfCcv5jHAf77IuEOogTjCauOAhVGEvQfATnGFqXg61d_QlL83cZtg4ZoTsZvu7ymOf0NSthfDuZ5-JFJ8Qj45LVHPAW7YVgTv91QOnUSeUuGJmPkl5c5ffgwBnk1Dyv1SCiWAlhtWYXs3xSo_qz2CCeAt6MPQXcuJMBBLQ7HvcUU236OgoPMntC_FSW1MoApkpZCm2jLYyQHb0HawoRjc4_lCsPdpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3Bop31eWgSpiIcKHSixl808LgeaNQYTU-VPizBqwoY3-SenUKbq8Ae3SaX0j2cSaynqRB4K39OuDr8f00FI47UolDCSlr6HciPsTMFdpdWyiKTTfDUKvyYEuncGmUKClTn8ERRu56-9-utjpZazc_MZ83q5BmYxKYsDw7uXE6x4z7c8-CWKje865XtLLLmCNwZuS_epLWHhpnxv_26Q1Q_N3FHBpnTP3yBSoaSylddz7P-ztf_ftmceurgJb90secYrPyYCE84wSXl_CYd9iFl2WRV-CoE4ami1IBw6UUFcDIXYSqzNRIDNF1rDNM1LVTBhze3zn-5mdvRPRrxjEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ66kYjEZc0eymQkfdKOufN58ADsbBCd86v7LFcHQhSTCh3hCxhyK-h-yNH1POJytxX2Hy4Gb7FmvHyZvYJa3zzCCXZQZarfjoGT6_X84Y2QdiWgfJMzMqFvx3_3bsrTaStE-PCwLMFSaGu6a7-CRsb91O7xu80yZrFGzceatVZCWCdKkklOIwt5MiTr-OXOsquChTSyqlaBr4DJFMJ99qOQxatnKeZMtRYvPXexa3rckmNchwNveDDk6fSs9D9PIs4452_W5V1USsZbfkNaZkyAeCcUyAlvHkBqD9g9DIXpCDK3rzsRoMEDs5YJkNbluMT6gLNf1yTlxySfM0TakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl0_ufbW8OIPrze_AoXiQAEDUU6eUAMCoOkRd8SMQQZjZzQCMpdCfs6AsEcONjOZY-wVhlEog-TU6kL9Wc2eshdHsEdec98av_LT58mh0dlRzsXwobIlkitby9gXNHkPLblbjAqQrOSn_bPSCAL5DR05OfgsnIEcanlli2ftsLru_LuFvBxAFyqE0u9pYHarUt4iAoNSqgOgrXAqkaq4tKQWRdoRMFygPMI0bduOp8OMZKXoIApztkvPg1NCHjdS5a9GjWS26nsjm8G6bTLw3Qw1bDdUkT56_6r0I96uceIWW5cszTKhrcj8buvF0rNpy6IU1wPW9YA--pdgSOiYGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsIWB2S826ZyRHV3hB0bB3RBwLw5cUNWjDtgUk0USzSFMJjvVWHEtZVBHPHoOQ1yL4vWMGxh_aE1OnPgTNcbfqP38eMqzMKi5-CXY71VvmypYQRFsTCLaD0y9EeO0YbIdHpPJsHrlehxHtky1f8tOerqu7fJGw7kg6SuGfR_9FIgeROJJFj--pHSPXs3ocfSpuBc7VD9-GAvUWgVsKdomnIZ3NVRQp6EXW8AbItimm1ooZviNxEhWYW2DOSSKjhUMwCw9yKZu3zBMLbQSElLydORJKDN02AR3x8_25DbQuX2_st_Jl3DyZu_dOs4FtBYOn4_ikuMf4K76msphGkAOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuD0XDpDmPXF2PYzrfwtuXo4Eqta2fJL6piAL8EZOJrZhaGMe3ObhtupPJZEObcgiWsDm-B3cu72TF7JCdeuwZIZAnFyqgiVQt1J_H_V0j0Wu-RHIbrUtMNoRZsh7XrWex-935cqk8sQdd50Lh8r0oEP8KlkkHztpl1lsGX9gCvsa8BDDiWsGCUyJpm9bb9ag3OYnarh0UU89UwwkGPfNZDHxqygkybe7Tqr__nydKEXMhGZDJUfSFZSoqIDqQwM-ErgAcJFgTq9h4gkewNp5ZKGk_tJIGLhcjzjAZ2ldagh4RNiwuyLJOdWixlkWjrWQDqSboMFwlWvvOTeB6MZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5HjBsTBvhIMGHs7bcrnzKwESZDOZ7vV6HTf_0Q62MM3ULETkDDoo_7ZiCgJ4eJNNU13oP4yucxpoTYHSS_-sMShQwl6hHUzOylZm-yGw0RMo11kbHLTupmy8sgKZ8oSZpzm0Ul7N6xm893U4ef2h9L8kf8hlXYMfu4a5QUNZJUEHWUf-meZ8yro5Tw1aWXYVCn_KTz6LgnC04v2KwcA8pLYZqcq5SWnGLJUTs1R4K3eW4kNolIAglOAeEdHxT4vMSn7i4uCEUl8yuDi9TwspYhucU115w_81RvgnHh8-GSsHEuZhrQtbQcv2pwU9bkJsIj8Bvj985yWyX17ZH9eaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=uFFwz5MsDK2gkfF50CyN0uSqEr07Fn4YBFp7flaGyadoUb2NO5FGKqExz8ojgvC1yaM3qZDuJgotnDg_mZNOX5wafryos0sErZKi03FYgM7TRSunCi3HtAHaOKd2LYWfMcz6vzWYTIaHy6-X38q3D56cok3Sr-RD2_7rTSlaynDwKn52kZZVq9h34z7FT_Nm1phlqneXlYF6wOsMGFhBkrIiDcx4AJQxacfnKUiA2l8NYZz8Ndg3Sj5soXpaAUxSwDEja-eHpV_F9eCd6Cq_L0UU5XYc9e2crBmeX1Olafgb1RAMOj09qPu0p8aKo2Q02VA7bb-dalG7iqegaaiGjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=uFFwz5MsDK2gkfF50CyN0uSqEr07Fn4YBFp7flaGyadoUb2NO5FGKqExz8ojgvC1yaM3qZDuJgotnDg_mZNOX5wafryos0sErZKi03FYgM7TRSunCi3HtAHaOKd2LYWfMcz6vzWYTIaHy6-X38q3D56cok3Sr-RD2_7rTSlaynDwKn52kZZVq9h34z7FT_Nm1phlqneXlYF6wOsMGFhBkrIiDcx4AJQxacfnKUiA2l8NYZz8Ndg3Sj5soXpaAUxSwDEja-eHpV_F9eCd6Cq_L0UU5XYc9e2crBmeX1Olafgb1RAMOj09qPu0p8aKo2Q02VA7bb-dalG7iqegaaiGjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3q7puYYPqOkif7boH_uKJns_XaVRw56NkVuudZER_s1NTXG5uF_Q3OfO5osyzVCDoseqryMWsnObhHCHuo246Oyjvob3ZuwA4DjhuF3diWyeJFeftgd-yWjk8QtwvmQ6m44NtNMh5tQGSQlETex08TvXnatCN49yZMhfqjh4Flm4wmrSAx7RnOiwEgLkdBOVc72INxPbeK9sq4M7tqfUfEXwLGQWUsLKoHHff3FDs9i0TP1vR0bqHvNZGJ0VjorSPS_Uv3fYNoGv7L2JRQFGtYAq_4_1n3QMR70CdJ8s0ouhynSTLIHIDUIi7wcdNB6gA3GlvGsriqTw6uvtOnyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2PxmyGe9p_I6A1oloo2_pvLbGc97f5DUnwITGetNTZaHcTp3gFo1iATH8M8ln8Vc6RvJAuR0TU3h0HLIxxSqL9PCHx3gUt0Y-rJ7PyQ9hZWXCz22VhmamacMEDWH-vbaQfezh8dNhbGterkqcOJ6kjH63uqQT774v_EZdA_kA1ruXw18R0NNkmjjIlyi10ZjsSrWNRu8qapg67kd0WuPkHNl34G0hulMLGBrazdLSdQTn8i79whVvHzVjEKGYHV7-1K3wV0IVc8sjCofxviXvTXzSEOtrDL-gq-YD517SAHJIRYqGMOKhFt8TCfmpmoOiwjYKdHIdya3zZXTAPVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1tvB6i4QBnxWOfZoYbJ9ulew8Pl7keJWabCyv7-u3SpgrRgjxqsByGu3cAKK9hx9Dy3NfaUvmegGqt-98XAFBCid7eqLSd4OVwSZYOcTtXB3WsEpQCclUU2wvJ7AYoK19OyJnRagsrWTdt6P0eitV2zTN2t690_B6Tpcs2XUFH3G8dLEMaL71l3KQwJ70jk9LEcEsolizCscbq5viz1QcirDSTKHpbW8AizbIYHWWnsfvEns3HBF2WpymRRUeT3C1x15w8IVCiSAq7RrtCffgRpJpP2q5r6d1E48Yw3RwOprbhHrr2tazKydw1j0jlzKmt0ccEaA-VL95kAnEtPZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMRZhzrGshSnrpLUARHr1fIiBHo7jcD_dcQ590eOiNYYffcv_R6sO05IEG23XIbP5Hw-ZkrzaWej-AYWPLHRVoc1yDMful34HAxLC6u_Do4U8xzoBeWrXU-jQZo9pN2qmCoJAmxcal_ZnVp8NR26mJYSBrW0jOKLeEHXvtts6TmapxGTl7SE4nR81rGOUyiQuynI1a-kmiHZowqUV6yBqUbNoy9bMkfKSqEupKK_cPBHuJJZ2kdfX26ng8n4i0ANw-FbuVWqDbO20CAdCo5WQrz32A1pfhQBDsoKmt8OBvbFSBtd4QYgz_oQ66OCH_Z5Tos4DTU_S4SPoz3zf6eqog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXwmDbvAOyK3WEd-FJRtH9JJrS8D5--kpAIrmp9zuFDxee56FN_agTwC5eVoCJxbSbT4ge3LUXR-3zcD64Smn916p7A8c_SXUh1Ldg4x9dMfKA8RO2dGx4_hC3MU2bx6jy0WX9arczs40V2Uo4kCfHPILblg9T8GtrE2ml5RXmtUmdxHLojusJ4UwXYrVp8q4VpgM7ZUjK1VyAqaewT5XOsm-iaOE8Npx3UGuL935WQSvbCKmNEIMNW93dArbtCRhIn3srOzdLIGKXO_7Szkf2EK2iv8ahtC_1yT5o_dK1hi0a5YRNQyFxaDwVaywOm7MukNdpAjuTPN_Us0P2D0Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=PtZQUmTiXm-gQ3MBNJmJiCHsmeQqQYgI1EBuBZhp6XagJR5eiD47XJIYHGqXsHBbom-XHwwSrqUFmDFqRx2OevHjRQ62-_hbe67edNQ2ZdGDJFq9DJ5FtGYL4REEp6WbGuN58IDPdCoGXeVYw9AxnHMJamR2R9Ys7Em2nUtn4z5CSvo6BxLNdpoxIf7M8D63EI8cRrpBoZYQGbuS69vvJXkQba1EI7v4OgC9JnFesPcTuHEIYntgH_P8IpprnDdw1Qk1BnbGJ7cEkpU5NrdVtXnQtbw7NC1tHS4LTbdVr829vZEVBCCzU1W4LljpO9bOQmMP8UiSfaxxExRWomJybw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=PtZQUmTiXm-gQ3MBNJmJiCHsmeQqQYgI1EBuBZhp6XagJR5eiD47XJIYHGqXsHBbom-XHwwSrqUFmDFqRx2OevHjRQ62-_hbe67edNQ2ZdGDJFq9DJ5FtGYL4REEp6WbGuN58IDPdCoGXeVYw9AxnHMJamR2R9Ys7Em2nUtn4z5CSvo6BxLNdpoxIf7M8D63EI8cRrpBoZYQGbuS69vvJXkQba1EI7v4OgC9JnFesPcTuHEIYntgH_P8IpprnDdw1Qk1BnbGJ7cEkpU5NrdVtXnQtbw7NC1tHS4LTbdVr829vZEVBCCzU1W4LljpO9bOQmMP8UiSfaxxExRWomJybw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gonBty0tK4gRWBchbS4ANKYNsM2FF_PyF5m_x6KJUyX22VbqXxQaQTcKiLvP7xzsI7nUOypMQWQ0VVBvSh-FpJxMrGCkwUw9wKcnA6N_-f6op-p4CuVI0VnEzqb1LRJUZCpQSPZBIMRArP4oJac7bB7nEQla2DYc4-_5Lk8klP6QO09UMfI3-O9sx6o4m_PPy85y0P25TIKjykI2VYX6LNuY0ld61pa-ZKkRaj3MhSgFej_wrLeqizNXIm1-7sFMLpSt-c6Hb7cn29gfbomKrZVk8IckecS3Y5ZRr2qisTjML3wOVwqnVTjCQFn52uDBvxXO4l4rP_UTv-HETGMBng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=Afd35B9VHe_6_LGN86e_BgHOjR6uYnwKixXWRtcFsSnwgfxBaBNHur11naVXn2cCw2jzxoG_38GXcknj_AekMN2_sXORVOzbpLV3JKoZcgfJawMquhvWng0IS4Y5HbQpuvtZOFtWFCp8B76ydXvzWtncMU8AiUNV-dJsITImiijBw9hrVKxqRqwk-Fpfsc9OWHcl-AdCTuE-FdBr9RbeDyPGa9KntMIx7ziqmyPnF7nbjR4cpT7vmKm5_sBFfClMyNtjvEd0tgJAyxAfKL9gx5EIKirRWb3jHNEyOwuPGAM_9Xl-xL4Xi8DGn8OM0hwCtEmuc5yuLcDxjf_KDqYrOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=Afd35B9VHe_6_LGN86e_BgHOjR6uYnwKixXWRtcFsSnwgfxBaBNHur11naVXn2cCw2jzxoG_38GXcknj_AekMN2_sXORVOzbpLV3JKoZcgfJawMquhvWng0IS4Y5HbQpuvtZOFtWFCp8B76ydXvzWtncMU8AiUNV-dJsITImiijBw9hrVKxqRqwk-Fpfsc9OWHcl-AdCTuE-FdBr9RbeDyPGa9KntMIx7ziqmyPnF7nbjR4cpT7vmKm5_sBFfClMyNtjvEd0tgJAyxAfKL9gx5EIKirRWb3jHNEyOwuPGAM_9Xl-xL4Xi8DGn8OM0hwCtEmuc5yuLcDxjf_KDqYrOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=ed1Ww-EZgkNEJcZMHxy8bmui11kPlz4Oy9u-L9B-878rZTAFsxEq0-bXQatYrWaeUNkm060ay5gQVSxduHsusiw1jSx6EBeWx9yt5yh4XCehzGFxIX_KW5NDEDf9R73qfwLWYsgAbEH1NZGq4hpT4NlrzXLXyadG54bWJvyH6Oc5UDhe3yfPHk2Xw3UATqsE9UT34W85tihbWmQ4z2y0ZaA3oJ1DQoPUaL0VNVdQVgir0J2a76E2VLO8iGJ7uKG3EHC3KXO7OhTV9oNtTKqmi_3jaBrBLhIdzo-aIkEf8bg2VwFDaxEAdu29PedhVuSgVgi22gXiYcwVyoRHrysJLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=ed1Ww-EZgkNEJcZMHxy8bmui11kPlz4Oy9u-L9B-878rZTAFsxEq0-bXQatYrWaeUNkm060ay5gQVSxduHsusiw1jSx6EBeWx9yt5yh4XCehzGFxIX_KW5NDEDf9R73qfwLWYsgAbEH1NZGq4hpT4NlrzXLXyadG54bWJvyH6Oc5UDhe3yfPHk2Xw3UATqsE9UT34W85tihbWmQ4z2y0ZaA3oJ1DQoPUaL0VNVdQVgir0J2a76E2VLO8iGJ7uKG3EHC3KXO7OhTV9oNtTKqmi_3jaBrBLhIdzo-aIkEf8bg2VwFDaxEAdu29PedhVuSgVgi22gXiYcwVyoRHrysJLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snkXqg_zTqmTDdRp5UNGG06D4D9jtzWFYNYGKU1Jd-phOF8H3JUkJhLnHZIDUhzZKM5pDW2JvpxtblbNtKQsJzj6BWPRSnvrmy8oh065MuqAp9o6mwQNNS3K36IsSwLriiQUAliKbUzfzAsjJWnIwjx-66_mamfHcatbqv0WBjXOk7ePWvIKgS6s2z-ueZO3HvU2qU5NNtaFtw4NSGBimJwu1z45_nAZ7qZkCkCLeCydaxYNFNK7Do2x9l0UsbtDIbQ5eLHqmATTkz4iC_Ce1uu7k_BB9_Xftvrz3oHwa2MHRMhkWDpICZdiQREVkmKW610GBr-tOX_0rp4yjuoisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U__-Ewv08jeQOEf5FrRysOnpZN6cbVg4c0u4sPZlPpyp4-etxAE1hcwWH0S_ZdYm7gacAaEmSmExAHnyCxzBk6OcHg8epoHw-kfA89Y-cmWZtOwoJsechdSO3cl8E_tVOF9Vk9-Ya-uXjyxMVaUY2yFvAONiGhjFIaIm-xvE-N7BU_LWwCIAzukEp_tuedFragw8oUHHv5JNzOQdEZlMzhr5ISXZADo64IpgVAoKSpt9DBwmVfqJeZjI9FrctJcwEqiDTaTaF1pjqix2QeYfo9ym_9jPVoHrdukUpq7m1Xr7rbuTmn49WBy9EX8LxzuT-Nqzj9Rv99QUosZpdzoR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=nwoYrQuqQtFCGgey2WA5GYzB9LvGNsBu4iRRtR5OLkdUpIGxUSaBGrIMfhlz2bUQwp7Wk8ot0gM5NkCjrUHmXGVwU4EIXFggyaFdOFpP5-3PqH98L_W_eLvYExjfBorbc7i6-dkGz-06MEpC28iB_76g6c5UsZ1L_YOPsutMyCQ38FUh_DztXL6-BsKkpPAN4Zw0Gni7IlA0Sm1YuMXQZJiMX8S-GEVoCenno0-pB2i7VObYeZ54-vvzte6Q7amhIAZsCnS8P2uxZTDoBAKu6PcmARpB5twXI6GJz2O0qH5PhSXe-CL-7ymJilequ4TWIjTMrld2reHRGDcqZ8HOkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=nwoYrQuqQtFCGgey2WA5GYzB9LvGNsBu4iRRtR5OLkdUpIGxUSaBGrIMfhlz2bUQwp7Wk8ot0gM5NkCjrUHmXGVwU4EIXFggyaFdOFpP5-3PqH98L_W_eLvYExjfBorbc7i6-dkGz-06MEpC28iB_76g6c5UsZ1L_YOPsutMyCQ38FUh_DztXL6-BsKkpPAN4Zw0Gni7IlA0Sm1YuMXQZJiMX8S-GEVoCenno0-pB2i7VObYeZ54-vvzte6Q7amhIAZsCnS8P2uxZTDoBAKu6PcmARpB5twXI6GJz2O0qH5PhSXe-CL-7ymJilequ4TWIjTMrld2reHRGDcqZ8HOkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HULt79ojyc6HSXAdHN97ahZzkZJw3DmBUKmk-4oK8nP0h8pmYWiXUiJ3sJfzUOYN94fjSwdlUGB0IGn2ZyJ4-K1CaT7UpwXwZNcfh9pZSb5IRGhiC9oEO5l1tCpTToQPh6rRT-T3cqj_pD577CLXBcH-1uXc_VhU59nwGMbQnxHR4gNw1H7eE_izuFaPz-rsjnghVGiTZcYK2xCebXFp8ApCdxUmmUG99lnDYevgdqlwV75rlwJUYk_WY1XyGFovcttdy_jlaRlB9edFup9jUTDcBfNvfTShQP06pVz9iYCWklN0Q_aNSOdgSgVobr3dai9VORAbEWZNz_H88hZeKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNT6hkjeCl2sDGz0YoOcrAJ1BpUwGvsJYAvfXmT-BkT8iMSbQKfX5zRCGkY_AuBi-tuACy8dPrt-goDQL4u9nzPQQKgI4kZoxRZDDppvbieqMVHZRS6RYPYZgAu1YUNZAaf7Vng3m8TG_j5XN3BruekvHiS9fUo1Pm1kGYkyd9EtrbnFW1AjLIo7a2k65UtYeKQ9Y_erH5Fqpb1jGGVIv8YVZrzpSMgkIxZ_HlF9fmNp1TM91JhBUfNKaqqRgsyS0sYq0wL5cizzKIA9s37BHyTMOlhzfn-wxOCt-sv6GeNSqz-HsDgYqTWKxqoTZewQjuuIkVSBuDPQIz0EdlQT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjzuyVBXOBGOdlcBK_WA2vxrFRcNlIUdmgLxuTtbepk9q_eM2aBbbt9kYOluAggIv4RY29vMsJqKCC0ivg9MuR7M_QVfeAdcPP-MJpIwwiun7zVfQ3OEkmuEsQTtJfOO0NYCXjgHRdH96BRXoX7OJpSkzrB3r2JQgaX6Xd4yVqyJn84zY5YtmYquZ0pnl7D4eTjA9wCoGxge09bn5zuhNW-unfXtcliYNwEko4ztb1USBcW55vUOXy0bpiiwHRwhTFOniYtuz1eJXvhlHq7P_O954LgPajhghueef970SzKf809w3y6dHhXz5rbEdMBIRopRtgfTUWUc5zNkga_CBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZxYV_lsb6d3gSbGCCgmfdaCVNgUNeDaupl-JR9SzhGqerxiK7elGikxB8ZxI83eDcOVjDnzBrvlwM3w-ObE1tA25zLIOfJ2rM3JFvoI0SuNARe2idJ99ppkX4-R7xOKQkYu5Bw2SOH5xwV4ud2aWxYntd-GKqAOZacoGimlB0OFbjW6-SmtC9kqfUrzRsFxD999jSNoBbJdAZFOM0MIdYLNuJ9X9On5Ly2Sm4mohyJ1w-9ZkimSTllaqy57zMmFJFHj2hQ57c6KiXOXuXRVF00CorjZJXxgDdwHDKJx-kdx9tkQyjz97dfDBDB1ue5I5VAPcqvIJmx7Tk13sOOi4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9yPKJXh6-468v7Bv6qimH0haBbysX4FB4vG8xMaQTzvJx--oQVKAWDQTZwd1Cwkireq16k5ImRPapMwysYZwjD9jm6UUkCAJXuAhwDZjRI9fFB74I5pfH49ib7STox_QkZ-gyQlN-cESg60HRCoe8ayTHc04nr8ot3-aOQBexcvLyywHyZ3K6DABLSq3fc3h74c4y-0ss20NvYrP2tz7dLV3VJtdwC1taPrdstf1kFztodyBfDvoyirDdy1URyfzeD0T19VZ4WEjUlDZAMkwoxtvirH0tJ-l7O6QlZ4xbJhUmfSmuq6b6dthpnvh5d646ctMS6baS0sK1IdUaCTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtoqXoXxA-oOM28bQ-KY2UxhbRlpb5TuVHViPRDwCNjyQvf_mdp_3nW_N52sXPL0nfq4oqtj-08a6K7k3gKFyCZbrkB-p5XlbTtkwLLa3SHv5j6CcRgt6Y096uOFX0q79gyubWrRP53YniIu2TkaGxKgcHkYAZbABE9-JGlUrwOLxM2g5mmADwpKsjju10wRjKiX4bUX1Djh1TBFCAIkF139-Qx7P2PGXOsnyrLJ8CA_KywaUHEB7JkGO4ybF4OxOWwlA9o5tKB_yn840qtSj9fupBxaOIEK18lp_vzruImVbSpuWc6zK-mDVVOIz6t27d6YjRiMBfSU2h1slW9r3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRN4oAGpPnowuobufDQoSHkzM5rR9pDnQ6jDUkqsLNSe7bWiFnjyWY6PV2PbTdE0A9OEc8lWIHkXTrzq0VMBux2vekjizTMKdVm0y-mj1pM6JcA8MxuWR2kuV-89ggygFNxr0aADQUYK32czcIcIUM7ctUL9smXvJYSlt2FR1nCzdmGrZ1NL4QZhaOavTzXuCrfq6ogCNG5JcE98W5kuoeIFoVgF3lTxrg4SS0am3wkuQhgF8BaQa8bH4cHIzirxW5BXiNejSDLFYamI32PgQpRuBwZlI-r0M4UpwoNaB7fE9gU4CfmMnvTGoQKBCupupczQPFs4CD9xRGPa4Hz-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ferh-b7rqhY6pzjeZfCnjrcBz-z1jmo-qLkCw3hvIsaDFv_t7BgRI8ZIQ4seztrCVLofZQDaqEAeuoVnzyjqdubfZVms25O7LjN5SMGiYnHXcw4uyLplI4t1GveMvIQGOt-J2SDXwMC8Jlg1iePa0Lq7TKlV7pmdRHyumK7pA1EMsbuF_0V82HOVZiD5XC-mortM88OP3eGPAKuPwkk7FlQeVAA3MzpV4jorxBKfvgDDFA6cg5cg9WffWESdPoRsqoA15G1G9iTdPfOxbznRdH7Xo9rpbIyozB7fvkpLARF2BTS1VXq_klaOyQoTTiKxJJ8ChaTCB6dfrM1rhDq2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVQ1-7BimE00RvNIi7aWv1U0twPT6NQEIOp5kaNCPQb8bbxFyC1v-ZPmNnyDrNV8e4UdQtjJ0JtLYXFW6PgsgtuAcICjQG8fBMuW2tgDEdbN21A4LFz4ubeBa6DVr47PJ22dGF7uovug7d6z1IJuDLhZpDNDRT_secO6pv76r-UfA703U4pn0bfPa2LsaXkozHs8gqu48OwrzWU4UkftyRDc9Pir1n8Ti-9VlNu0ryRkwCaPtfLXU4ynBZdDAhjraKnx6PbQxqn4V-gcYy1Xj8_ofXU-bGkvGZo5TBiynph50clQK-ZuKu_3KbHHTHRoowIIuLE3Y_TXO1W4RBC2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPChrrE-nJjG5eapxTX4VgXJfBLxiARgWjR5WC0ZldUP2A0vHF_JtZlIOO21URP5lK0YLMViFsdn4vt2B6PBfzkXU03XnXFfTalMDCW1kZvudqzYK0yb78egaSOXgNOuj100LMk6F0eYuoVwJWSHk0GgTmnHI2ugV6siX494HsdjpJwZTFBTuLSePE3foxqgIDCooZENRwaJ2Oh4YqCb3F9Nu6Q3eeR_NfEg4doxXsy0G-SG2KLoK7BfX6uP7YLWxZN6hPx3Bh3XUM5au-YE3Oa3o7MCTMFzH8oXjSxM1-QSEmR0lf9RaEq0vIWolzuEve4j77zretxcd9P19LbNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_vdWVeluacIT0JV4KTcwPnGn_djhcZr6bTY7-Gmj4njGwOWuZTELNWPjNb6twE8qMSu_EGMEas4uDFRKTC1116cRfMuVwdG-UosOfH3L-9b9bKNoGPRT53pNue6OrIhXV4F1ga__6LPuYXP0R-eTrH_Zn2AKN7oq_wmHsA9njCFjCvsbAZ0wpTbDOxBj3dg59KaQKniY1eWiv00wYAp1trs6jbDiI6vK56oS7WZ9r0CXeq8mTD2zG5tlI5Q5GIz5Bj4F5EFZgU-pCIVBlkKvPyITe4YUeJZ_1lCJMnp1N9jGc2y0LDCd_H2JdvorM-pN10LPEbp_3NA85nd4l9UwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=fvH6QzURFMNHvjb3NxTRm_lDObrSEygOv5cPMfvXpUTL-0PakmtGdyn4HcNWRdtbXYqwfqkA3_eUEFsaJ_j9L1k8g_Ul4rXIJBCedIQdfS1Y-MS9eiXTSyNeOgTFUGFutpXdCR0IXLTFZcpOxc1z2LkrcjaoGUkCTnFolVawgPCommmkHUFljHz5EWlaEzIWrm3h6P1WLlIXG3duGHM2oqJBOxxUjchyjja6MwOrVhPp_TTjB_aq_wP0rVV8SnNEsj_gEOtY9PLSOd5pEpFj4vEbay0fwhbcHUqR6lmVod-1cbnKIce5G-zL_mpxG3zVI7l_XqeHoD9ADcwpl1S2gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=fvH6QzURFMNHvjb3NxTRm_lDObrSEygOv5cPMfvXpUTL-0PakmtGdyn4HcNWRdtbXYqwfqkA3_eUEFsaJ_j9L1k8g_Ul4rXIJBCedIQdfS1Y-MS9eiXTSyNeOgTFUGFutpXdCR0IXLTFZcpOxc1z2LkrcjaoGUkCTnFolVawgPCommmkHUFljHz5EWlaEzIWrm3h6P1WLlIXG3duGHM2oqJBOxxUjchyjja6MwOrVhPp_TTjB_aq_wP0rVV8SnNEsj_gEOtY9PLSOd5pEpFj4vEbay0fwhbcHUqR6lmVod-1cbnKIce5G-zL_mpxG3zVI7l_XqeHoD9ADcwpl1S2gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=Un6lZlWq8pgKfGy4CBqTMh-2MQH2xdx74Qc9GWfCIxs5WMEqyQlpTecx5oPYPMA4Ps4-QOqc1vVHLfzIF-WNOd21_oAZhfnFrVVb7Q5K-gp2mpIPOZ7KDgjsBkl8QhJf96Xyk1l74p54j01jRiX3TJxXU2jOKHWR_fILwExLZkdXgS3iqVw27inTZe4WqDqGPWS2s1sfsbrUGWJhCQiWQ1FVcXkkll4ToEbcGodqwRj6GicZWqjdwt2K6cyByOsr7L2vAmYrCdDedDG6AIXONu16h-9jejuUgvP2F2f0upgXYTinycPwT71euymj6g1jEcBGuVa2J2Xvj7KkGchh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=Un6lZlWq8pgKfGy4CBqTMh-2MQH2xdx74Qc9GWfCIxs5WMEqyQlpTecx5oPYPMA4Ps4-QOqc1vVHLfzIF-WNOd21_oAZhfnFrVVb7Q5K-gp2mpIPOZ7KDgjsBkl8QhJf96Xyk1l74p54j01jRiX3TJxXU2jOKHWR_fILwExLZkdXgS3iqVw27inTZe4WqDqGPWS2s1sfsbrUGWJhCQiWQ1FVcXkkll4ToEbcGodqwRj6GicZWqjdwt2K6cyByOsr7L2vAmYrCdDedDG6AIXONu16h-9jejuUgvP2F2f0upgXYTinycPwT71euymj6g1jEcBGuVa2J2Xvj7KkGchh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGSBcVzm2Lbvorw49J8_5R5Z24hib6eFKr5Jp1uOZXrHaeO0bITO-P-GPkck8CbNJn-bgMQCY5za5g8k_DoFWTdU1O8zmninIxzhYQZ73ywq0SeNkyWIY-mShgrnMXYR4c8PpZyWdk6Z0yh47o6WMf70poK7w9wQ8v2GHYTci1-St9rrgKqaPad9hy6Eor_cpJ-_LtlCw-bN8Gqob4s3mmiQS5uhLofFQ5cof072Nb2WreWrXQpzSnIxhuynJ7MwpDbiaR1gKtBQIy3k-b3NHNa6BFAMSIVC8cSj3yWYkM1dgNFkwMAGgCL-8Y9ZntcC_8Uo4H3AZ6Nt4b6ITSG89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
