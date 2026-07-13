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
<img src="https://cdn4.telesco.pe/file/Ra8fXhCG8Sx112UG1xK3ndbrPnrnlubteoA9kIX9bFCitPWBxuv9cu6DytwQy2z8m-m3WNpb5WZmMEU0HziPmwP1uAKW1IlDWeGRqcpfUjuSTqt07kZ4HjnXb-rRYQnn754XMSN1Y9qZjjExYrNsZLkn-t5Tx5yIaCvvwo7ZtkYS7KxumhecxLydi19D5uSFn7M6kw1sUXq5eAHju0OoRumG3wDNdLJKWZxMjMQ4MJNAhHkuW-gxh13zfArSfowCLSbfUq1ouZkcgSKoOOEDVEmVXd4U5ewhYLYRZugAJgSLNSQuV1sNLZaXKOmK4jeHzGbgxWXHh5EeAriwWhEYzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 17:39:15</div>
<hr>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WodYqipS_f4drNmmCLsdRxnfGxzGkE9AkTJYlt6iYnbfZzpcem_vZa9XsBaKEOvSAaJS_9P4agq_4HDGsFuhpDnKDi4f_yl20g4i4VnX5VRvRwZjsqeI3k0hYFcBkl_50ci6CaCiwoK5eQSFlUdWVlEC9_fmWzJJII_fcD1Xm4Hli08-szxeI5M5cofnOrv7sczl_plveVieSIP0-SPlVyGO5B6KDtQXtIgIIdS0307oZLj9XGchYE1ovAEvBCtvr7ED8F3pTX_OQ7Mfe51nSWXxp5-fo8oRAYQ8eatbkykGSa_ID3sxuAT6UwfcnPmEOCzsTTm56gLFDpK8GOlyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD0muKxU0borg_9FS17lI2uS3pFJOmdZgTUXKOH4mgL5D1JKPW7LGGs7XfOhpMtI-BLUbVARHuzkYAkTg4CzTjgBW-5x-rSN4zDlUVDUgZiI2Ql1iSYgKay_dPS6LltmSMBniJQ_Tz1ZIjnhG6eNRDALVFD-MUlRSrlvRhM_qb-3cYff-jjF1tvDNtoSwlDBB5d5BIoW3eQeVm9s82l60cmdPU6-4Gh-3a7Ne46hWDDhdjLURqcGEhxoAE1BGCRLC0sk7gTAc_mJBEerbJou-nxKaoUICqsWiBJeZ2yW7hkD7njAlP8KSzKe5HoRkqKzFm8NeoXEQTc--ZpQI-dDww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFm_pvl2dRzeWo1nYU2vlAXkzIKSDiHGpsHh_ejdOgH6qhZajZ5n9vcbXbM_n5Bvzq7waf5xUaqRFUs0dyD_w55Vn537Er1apNb8at2yVwpgODAIq01ndlbHYy03U1l3P_7Jl28tbRmTRgVBGxCsp8DpInjUMAonLJBzKiXn8Nu_JA-oXtf10Q9eOH9eUQH_6qrpCzS4Iwei5IKIutnwL4hfkYf-lOdVXvXnWyVLxEilYycXesgeq8JTmkjiIZG9LAv3m2WYRmRK7G8fz4tprRObbYV_HgQjy2IVlFX9HqVKDXu1nc6Ekehh-9l-pCT5JiBhdqN_F24Dz_U_R-f7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»
شخص امیر قطر به تهران رفت،
همراه با نخست وزیر قطر و وزیر خارجه  قطر،
اما برای خامنه‌ای،
سطح هئیت قطری به رئیس مجلس
تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم
شخص خامنه‌ای شد!
از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی که قطر برای
خامنه‌ای و رئیسی قائل شد،
خودش به تنهایی یک توهین به خامنه‌ای بود!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZy_T-3OfghHmboNPupBrtUINwJxIJ7jPjwSm9mpKvcc-YzW4UYns1St5dJ4T1JxOkyEAld0vx-ITtvKgYS1eJbsdYfC8J3BrdkAaEL-YhJxft4SlFhxNVhDNWtgIlDSK5EFLYB2lFbO12DEOtOyJfK5RlNjvJwooL7KvlIUM92d0Ds8raaSBQmn5Vw1uN_hTLOCHvOFBuAVIpbGzE49oP0t9D_Ny0KvgNzu83E4qjFwG8KvPXb8uibtSsq3BG0dUWZJBwsuy0gW8F2m1PmFNAMhOXPzlJGM12F4w3LQsE0oBmmvAdwFrF1WxSVe67NU-GNUZCO6A8miUCgZnbWymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطقی که در دو روز گذشته
توسط جمهوری اسلامی مورد هدف قرار گرفته.
عمان، قطر، بحرین، کویت و اردن.
عمانی‌ها از حملات جمهوری اسلامی
بسیار خشمگین هستند.
عمان همواره یکی از دوستان ج‌ا در منطقه بوده  اما حملات مداوم ج‌ا
به این کشور باعث شده تا سران این کشور از ج‌ا خشمگین شوند.
🔺
بعد از اینکه در آخرین روزهای جنگ ۴۰ روزه نیروی هوایی امارات دست به عملیاتی در جنوب ایران زد، ج‌ا کمتر به امارات حمله میکند.
🔺
عربستان هم در میانه جنگ ۱۲ روزه به طور رسمی و جدی به ج‌ا هشدار داد که دست به حمله متقابل می‌کند و ج‌ا نیز رویکرد خود را تغییر داد
.
🔺
ج‌ا در هفته‌های اخیر بر بحرین و کویت  و بعضا قطر و عمان تمرکز کرده.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3mKooXnbv9QGxvWH4TEwZGDy-2LC4GV6hC_ypGAo_ABT932oKlz0rrdxv_fOqFIIdFfjYaLmWbVNWV4prjauXQpbyZhUIbjbZH8oXCtWSBCwyPO4Tds-qL9HU5f5h7vSw387i95c5j6HbIP5-kAAGcm1554GbBpYCrapQWQgpVvKLkc9_Pd7hsfE_T2kiA649wRYbefau3UTtfJBvbyfLvBdOfJbTz9li4oBUsHR20u39zGUUKGfB9kMM4KkaM0OPsrUz1Z65S-FNCByrrtHLSGmzaXQbAGdG9Ap3eoglGtM7jyuNEdmbkhkBTmjxteHFq1xVaJa6Sf-9YzMQAG-VfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3mKooXnbv9QGxvWH4TEwZGDy-2LC4GV6hC_ypGAo_ABT932oKlz0rrdxv_fOqFIIdFfjYaLmWbVNWV4prjauXQpbyZhUIbjbZH8oXCtWSBCwyPO4Tds-qL9HU5f5h7vSw387i95c5j6HbIP5-kAAGcm1554GbBpYCrapQWQgpVvKLkc9_Pd7hsfE_T2kiA649wRYbefau3UTtfJBvbyfLvBdOfJbTz9li4oBUsHR20u39zGUUKGfB9kMM4KkaM0OPsrUz1Z65S-FNCByrrtHLSGmzaXQbAGdG9Ap3eoglGtM7jyuNEdmbkhkBTmjxteHFq1xVaJa6Sf-9YzMQAG-VfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pr14YxQu6ARRgyuXuQk5HGJXXUGi7aujlHEsHmu958hvFPfAFA4St2eNZUlqYrsQSH2T4YrFP-F40jI8-c226nCFA25Q4M1mSajsW4kym5JioDFHoF_-PS09CLvg-2lBkn9tfFioY0hGdf1_xTGb-u01WWNJtKDklBMq-0kk1CqTC4EfGAyiU1vRmF5D2uPgYOXsvetbYIUGaZAbK7FS2V05VRlHuENCIaryDaHGBHqs0JORzpdCujoBCkx76B03UJeLnAbBC3BWyjsFi6pumB-aAMAuNmXYrQ1Cp6hP0mDqlo7DqULg4bGgZlv_EVQXV66NysSZCeXAr-D-GZye8Bs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pr14YxQu6ARRgyuXuQk5HGJXXUGi7aujlHEsHmu958hvFPfAFA4St2eNZUlqYrsQSH2T4YrFP-F40jI8-c226nCFA25Q4M1mSajsW4kym5JioDFHoF_-PS09CLvg-2lBkn9tfFioY0hGdf1_xTGb-u01WWNJtKDklBMq-0kk1CqTC4EfGAyiU1vRmF5D2uPgYOXsvetbYIUGaZAbK7FS2V05VRlHuENCIaryDaHGBHqs0JORzpdCujoBCkx76B03UJeLnAbBC3BWyjsFi6pumB-aAMAuNmXYrQ1Cp6hP0mDqlo7DqULg4bGgZlv_EVQXV66NysSZCeXAr-D-GZye8Bs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ارتش آمریکا شب گذشته به ۹ شهر
در استان خوزستان حمله کرد : اهواز، آبادان، ماهشهر، بهبهان، شادگان، دزفول (پایگاه چهارم شکاری)، امیدیه (پایگاه پنجم شکاری) اندیمشک و خرمشهر
🚨
بندرعباس، قشم، جاسک و سیرک
در خط ساحلی و «خنداب» در استان مرکزی نیز شب گذشته مورد حمله قرار گرفتند.
🚨
جمهوری اسلامی نیز به اردن،
کویت و بحرین حمله کرد.
🔺
ویدئو : ارتش آمریکا این ویدئو
را از حملات دیشب خود منتشر کرد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=NCLRBwhZlKLI_fQ-f4Yfqh7BkRbyhbkngqZLsXttCSlu4vr0mN2J2w4z-8sRd5yJs1UFGXENFAt2ooxUo1U5G7DJwA7viHlajx-SCeidNvlE6E0gRPcmgXwgDt2ClOtWhDkPsbNV1UcoB4WuYLgnKB5R0z60FLZSXYYuGWFf8yRhhVUsPwyVoyti0C-rWrWL89chHYRHS_4Xf2vb3efku_3PUF0f_tLdCoHDwQ9t_IbLVewkCzyedgIjq_skeW9YWGZtNo4a0DWSVHhRBfW8YHUVG_VEBo1xkahA8E5SsEPLLTT4Be_vF-vwAyWT2i8LKTRIKeFt9fzEF7LW0yYC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=NCLRBwhZlKLI_fQ-f4Yfqh7BkRbyhbkngqZLsXttCSlu4vr0mN2J2w4z-8sRd5yJs1UFGXENFAt2ooxUo1U5G7DJwA7viHlajx-SCeidNvlE6E0gRPcmgXwgDt2ClOtWhDkPsbNV1UcoB4WuYLgnKB5R0z60FLZSXYYuGWFf8yRhhVUsPwyVoyti0C-rWrWL89chHYRHS_4Xf2vb3efku_3PUF0f_tLdCoHDwQ9t_IbLVewkCzyedgIjq_skeW9YWGZtNo4a0DWSVHhRBfW8YHUVG_VEBo1xkahA8E5SsEPLLTT4Be_vF-vwAyWT2i8LKTRIKeFt9fzEF7LW0yYC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=hXJyW0voCcIHYGHIXA2kZpImc4L39cxxn2xaxQCz4Eq4Re-9Zu4qShCxI1xpPJHKAbW9LFZERxNJPE-2bz0FxCT-bfdjmrWiBUQ14ZIFp_TiBXU0b3YfDFnNlfZLcuVy26crvHBbPw3os4tXpLplsjyY3kTeMnEPVMfEsJW1k1i8wU7hjgkG_2nP3ZuJBrJOIgAP3wSpBVDctqO1aKJo4eVkfkfnneoGHrJDBr6PvbS-AbmjbgtN9wCUaEnrvFZIrszsHLZ4lQaGgImsuUbXwhXC3C_BVC5INFUjRv0DYHRQpclSOqKYHcbL8ZecAvwCQo8kQVWeyJQc78Zn9xJoyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=hXJyW0voCcIHYGHIXA2kZpImc4L39cxxn2xaxQCz4Eq4Re-9Zu4qShCxI1xpPJHKAbW9LFZERxNJPE-2bz0FxCT-bfdjmrWiBUQ14ZIFp_TiBXU0b3YfDFnNlfZLcuVy26crvHBbPw3os4tXpLplsjyY3kTeMnEPVMfEsJW1k1i8wU7hjgkG_2nP3ZuJBrJOIgAP3wSpBVDctqO1aKJo4eVkfkfnneoGHrJDBr6PvbS-AbmjbgtN9wCUaEnrvFZIrszsHLZ4lQaGgImsuUbXwhXC3C_BVC5INFUjRv0DYHRQpclSOqKYHcbL8ZecAvwCQo8kQVWeyJQc78Zn9xJoyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=M66buIgxHRfuAZz-PV3cBXnktohN_lFSNVURIFWhyNx0oN64F4vuSAT6osYH1M6-cytSuv9Y0dSJqR3xCzgm70JSmBLwb6vXSXPhZhmo-l22gGTQwgHlC34W_06FjZnO-iGZu5MmNWiWyp6EMW31INaSuyKgaHR9zq2s7rxRIvj9lBawEDA3wbQukdH2KEusn8W8ZMWPBAhxK5LfFcPgBnjJGmO-uEkmm5Dda9dXIt-BuXAY1XydKKE94lrMEZU-6PoBf1-VZDV3BqoePnxtTFSkLkg1aLDJo-FHcBtcCDDcMUI8S9zlR7CSD7oCJ6tKwSSum5v_3rGryYqwjjnbmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=M66buIgxHRfuAZz-PV3cBXnktohN_lFSNVURIFWhyNx0oN64F4vuSAT6osYH1M6-cytSuv9Y0dSJqR3xCzgm70JSmBLwb6vXSXPhZhmo-l22gGTQwgHlC34W_06FjZnO-iGZu5MmNWiWyp6EMW31INaSuyKgaHR9zq2s7rxRIvj9lBawEDA3wbQukdH2KEusn8W8ZMWPBAhxK5LfFcPgBnjJGmO-uEkmm5Dda9dXIt-BuXAY1XydKKE94lrMEZU-6PoBf1-VZDV3BqoePnxtTFSkLkg1aLDJo-FHcBtcCDDcMUI8S9zlR7CSD7oCJ6tKwSSum5v_3rGryYqwjjnbmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=qFpYyyGPRNHrt3NDdZPuko8_Bo0LvNOF4hOFhH2d5upmQHGHYy19-_zTK-huU7jDRakzQpI36ZP6Da1u4Nk0wt_Ukx7NUdeNnZvt3X7g9eoNuq1l7Xc9TIIR_vd98CSt0YIk-p5qd-G5_3BNuoNq1xe-smgxBHVtRklJ6K8q1gsAfVV1l9MGmss2hVAJ0JXUripZmzpNrXfdUsgC020uMP3dTXftDmyyXApbdkfwV89_a1PqERv9hCFINnbCLFnOlXZ2tTSKCOOPnlkYsA3ZNpOChe36W2CUY71GCBsUavRJtgNGuN2CyxxhOB9T9lTNx0muEX5-2BcpQPGJ4HTyZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=qFpYyyGPRNHrt3NDdZPuko8_Bo0LvNOF4hOFhH2d5upmQHGHYy19-_zTK-huU7jDRakzQpI36ZP6Da1u4Nk0wt_Ukx7NUdeNnZvt3X7g9eoNuq1l7Xc9TIIR_vd98CSt0YIk-p5qd-G5_3BNuoNq1xe-smgxBHVtRklJ6K8q1gsAfVV1l9MGmss2hVAJ0JXUripZmzpNrXfdUsgC020uMP3dTXftDmyyXApbdkfwV89_a1PqERv9hCFINnbCLFnOlXZ2tTSKCOOPnlkYsA3ZNpOChe36W2CUY71GCBsUavRJtgNGuN2CyxxhOB9T9lTNx0muEX5-2BcpQPGJ4HTyZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs-XK4K4YAawv_idYm_nSQwA6-HEVhqUZL4mEUouidXpUu-V44CWw4ueozAYP-jBuHI-zQL4qX3scC_aXtG3SwCheWc9d5TaNqJuA83EpUsvGaIfAMFwJcQxvD-ySQUlFP5K_9DUK9rfzgen0dXpXv-IDZtsfzeiY2z06lEPfZs5szY1Epow1vtIYgWNMYBGXrnJ5D_xos2PqqG8M-YT4tmIZWA-okKT0tVEd-btiQF-Cj0_Jec4AMKfc4e9RKzwrnA5XnYJKNyKHnIYGiZQdhLnw2aQZjsjXw91jpCLtxo6eY2-RhMQH0OxtOwgEPayvbFTZZ3S4ioIDdQGeJMIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY78kTGMXOrCRBes7hDKZszEM2L-BD0-lFw-gW1C041d7-N4x0nXfElJMjb0wL9uvvruoZMEpykUFjEJvhowLdTsl12namZJLjy-iMDPjJ8cAqq0Ch3w0z5W5PNdbvF4B9njjiwmmhgZrk-M-3cJmowBenX3ObIXHDg0W45JeUN5mUTuuHnOAnRZKYVjtQ1AEPJH-ZI_kB_cK1icYfi4A0oYEgsHnX_dvIZJ3JXEqSq4yc9VP-CEUUWbGptNOAmpPbASPClJD97zv760bmrUqnpm9lm3-3coh2UnEU7HuhVOiFH_znKtzG_APctJeLbax8k0yWel7HOkM2iPH4PPvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=hUJQzUTxDwS3gMZOxLyeVg1NmjfIPvORo9il7e_E-4IzkI0MR4Qc9FTFD9Ed6PpFaia7_xUSzNCOduqrwHJIl-Idy6LZ5LwJO_gzU3iIXMLdCLBz902NfRyWlxftYGtGu-zHkx_qAr1xC1Lt3nqcAbXFgIP-hIqPi8OqhQr7ywKLqfOgoaxqfuhctBmjfW8JKX3LiIA7Ufp07XJfr5eL69QNYBIS6r9tR0JDengSEZkoLkcfUv88ze8z_1_CMyr0d31nCNAs-rExeGErV9-jN-zwNt3IM0o_xL_7GTNUprA4t027fJ1612XFqMG-Jw0yhP3J_CEjsYvehb7CvU3Z1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=hUJQzUTxDwS3gMZOxLyeVg1NmjfIPvORo9il7e_E-4IzkI0MR4Qc9FTFD9Ed6PpFaia7_xUSzNCOduqrwHJIl-Idy6LZ5LwJO_gzU3iIXMLdCLBz902NfRyWlxftYGtGu-zHkx_qAr1xC1Lt3nqcAbXFgIP-hIqPi8OqhQr7ywKLqfOgoaxqfuhctBmjfW8JKX3LiIA7Ufp07XJfr5eL69QNYBIS6r9tR0JDengSEZkoLkcfUv88ze8z_1_CMyr0d31nCNAs-rExeGErV9-jN-zwNt3IM0o_xL_7GTNUprA4t027fJ1612XFqMG-Jw0yhP3J_CEjsYvehb7CvU3Z1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAPxjKwM2ykOhwfZjeuVOce7D74QFxxNrrAruxCdDgRKWM7k6baGtO03OM3gY2hFq8Teb3wN-T7Cs6_RyRYZoDMi3jbCMssHKZk0lQFOQ9rGCKn_iU9pU3MF1ZiglucPk7DkbHuEKh5XJ_LQKV9touhCSKmeHSWmf_YuWP7wazSv4MKJkbCbH5BWIwNqAzBLd2A827o_kZda0-ceBGMmPw4dawoybhzAYQUBLyfqmafY1VfdfrFUb97NY6vohIycTnMsOVrvd8GH_B4ZvdFgF-c29PP0azQ_9_RVSFiK9LKhlJvCIEwuJQIZjyEPYMKO1nCZXEAONSPTEBN3YK3UDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این لیست عاقبت و نحوه کشته شدن چهره‌های اصلی که در کربلا نقش داشتن رو نوشته،
خیلی جالبه، چون نحوه کشته شدن اونها تفاوت زیادی با نحوه کشته شدن افراد در کربلا، یا ائمه و… نداشته!
یا با تیر کشته شدن،
یا سرشون از تن جدا شده،
یا تشنه بودن و کشته شدن!
مثلا این رو نوشتن که ببینید عاقبت اونها چی شد!
هیچی! همون عاقبتی شد که مثلا نصیب بزرگان اسلام و شیعه شد!
مثلا یاسر و سمیه چه مدلی کشته شدن؟ به مدل کشته شدن سمیه هم میگید عاقبت بد برای کسانی که مسلمان شدن؟؟
در مورد یزید نوشتن در حال رقص افتاد  مغزش متلاشی شد :)) از روی پشت بام‌ افتاد؟ روی پشت‌بام می‌رقصید؟
بسیاری از تاریخ نویسان مهم و اصلی از جمله «طبری» و «ابن خلدون» نوشتن مرد! نه در حال رقص و نه متلاشی شدن مغز!
عرزشی عقل نداره! با عقل دشمنی داره!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=KEZNqbvqGhfREXZHHvNmTfXJ4eLbrwaQpbf5P60K971y-6Rvn98dgCJKicDQtRRJ7jW9DMoa1C6UF6kD_AP7KWzMXiO72ge1-6PG0e3Pb-VYdaGcuxb_O5_EJA1nLrYlPYLNw00F8ADb0B1rhfO8RPQ6954b3Ey6_NMYbmuLTjAGmo6C76avW-KWKJH8l03Saf68ornY99-K_uXYLqip3ROiJztztzl3zRArroXT4yHAslKvB-fz3JUERyAF87MOB6_laj75dN0ruPixZKLXBavR7JRfRtq88ojeO2-uwLk5dRIlndPPpg8NW_iKMu7xuYcSAWD2VOIEXUSDH2eKhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=KEZNqbvqGhfREXZHHvNmTfXJ4eLbrwaQpbf5P60K971y-6Rvn98dgCJKicDQtRRJ7jW9DMoa1C6UF6kD_AP7KWzMXiO72ge1-6PG0e3Pb-VYdaGcuxb_O5_EJA1nLrYlPYLNw00F8ADb0B1rhfO8RPQ6954b3Ey6_NMYbmuLTjAGmo6C76avW-KWKJH8l03Saf68ornY99-K_uXYLqip3ROiJztztzl3zRArroXT4yHAslKvB-fz3JUERyAF87MOB6_laj75dN0ruPixZKLXBavR7JRfRtq88ojeO2-uwLk5dRIlndPPpg8NW_iKMu7xuYcSAWD2VOIEXUSDH2eKhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7r3zaf-T38mwQhXGP0OR1Q8-cZxRD419ds-sDB0tXycZsQTI9OsWscsPe9LzgMuW0hoDdCJpO7TBGeNBMipd-FW9VeS8Ce60yuOP5Htu_jl9le_wLdVWZOA5VSz8XfQxOduvUN6MObxtNW8MwsCcTa38PH4Vnocgx4BWube0wEDNZsiMpuXR4cUpOu4EreuwrzEd5wFJgcGOdkRkTcInAMr7xg2r0BYde0ozmDwNRf61UD5esKqN0ygUS-JMxE2qeO0HlsJLahDTBCjRSeSnrXBHV1O-KVzNjMWnhvsZ9IyPdlD5TZXLrt3tW8cZYh6D9A2maQdP3o5h_4xBWuoSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdUZfmTKRJmJOA8wYvlRNkpAJTurrVrMpM6RRGW0DVBtUASLoW0N7bTKaUKEOHeY1Xla-OzRkytghmn_C3K3i4FJHnTUQNAc8ORBo154oky3pDrc2b2OUDDarFexKLt_UGFYoV3cS2Vq1aFhVzW3CyM3ZajpudrKm9jKUZXUKWTgkVU6xDzziI1nRZcH06SjwPIqPIly4I7YbIXESQaGFV5g7nCUrjvAQR4iZ8JrQNoTi18sgnVd_QWHj-yA_0DLsnpl9cJAXxFXDmJ2HyQjYUkXb6tcUBSZEKj_I97ybUyilHEVlocyIptl1ErX7ZZG5jbusWHbeLk82ZQOWWWtTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gS_qnWHs80IZ81uNmpMCI1OFvuefavBNMNR-pyelr7Xmr4hz35_tQGbJMkGKIS-FStS4UwCGzFSoxXKAa4JdnSNc3nUI1wXOaq4D-RiiDsrWrKuPFU7bQHJQMxR49j2vqvEGNRsML3h7mC0UsO8DuIPCsaw1nO0UDuZF8QuNur2K_erhZMU-vvSYr-6FRAF0QmUxpN2VPV21g4osdiH2PeR54QL0sZ2QS7ENxb_ANYoLt2x6yAuEGNVHxZEUhjThwfbWTrw2ki7IMb28d73MoyPSK93JC1TIYoq65IeBaM55Q2VOWs60B7mIWKFOtkf-l1wLYobDO2NUOqOJwMpI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAHV9pFbYCbH0qqNehfrSkCE1KY5PMaNVRqHrEpL4qPT9girptssvSuDr1naiR8u1C3nvYQ7oNRkAtqSDLTpFnHrhk8p4wdQtm70I_sCePXYkfsRrgMoNzR-MJSQrz_sFOQCsGB3vIQZdCs9ITRB-n1WLBfPtQPpWy4VKu6BsB21r6WGl_Q8cRbF1ZMRY7BRaW1f1-j80kq_SLlkqPRr7dkKVR8-QRktX5bXJslfw9gUViEMYravFP5nb-I7aoW8Ix6GZs1H5RcdRJ1pj21znweaggROSC63Xky-7rb4CZHRuLO9iDvDDWGCvvgoluc0VRKC_BJlVaOGN_D1Q-G9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TpzJnPjyMlCejrY14zx55Hs-uB3t6zpZTNmXR5pnnXxxIPZlRYbTkhqP30TknGy4AJpWP5B7hZOyUii5D0e-9bXOrW_fdNRJkoD0gerJiDwvc2ajzfZgAmNsGUBEWCvwJdAZMFZYCynmoLqYfC2mgNj7KWV7rf3oK2LkMUrBV6dYLq49TdOq71A4P4EZPnZ3IpbtSkWWlXnZV5mJhcLEPcidqDlqQpk4IyPhpT5Qavzs9Rp6efUpAV8nNb2v4zDPBsvROrOqhVsVDbrrrFkdVj1pCiE5lXDdziRbP7i4giTHD44sS19y-zIByQs8_kfcWOxcLleIR3Ei2nkCrHbwww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RT9DgW6EVNrDe0BL2OKm0gBpCOvUcP_DktqszqAWNTzMJl6h53hdExuiOP2RQvYoytoyYLxtyj0mSZCh10ljXqyyvk6a62pEaP8fpPaTgfc9QRvOwUZBN4GJq0lpDdppwwmJdHgLyPkM2hRAFucKplx3azC7xahD-rF79UcYeKnZAxxOpdovm0i8VDknroraHkagDo1B5mUKQM25v-pP3RYzGdMaLp6_LLwpZt8Pby6tsq0QTAgc5FbahdvYB3NubY0aBS9A9QUaObawqND1Yue2_fsGJ69jbVD2iw31Ldr7sGWIb_uGucwlYeZd1tcIo9B084fjuXSTPIy6s2oycg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF4VLRqvG2iyNZbi_TgGwAzf36hWUTxG4EZUI6M8DL7tHoTqmZFPzhmUThpAjgEq0b7K4lpgK3ajXp0k2pKXJfNy9r7hHVGcX2cR_wfb0Y-oedTce6_WAyzfU5hf5bHUdC8fuqr8ue9m42pbTZc7i9z3wAzFKr0eR0VPZXupo04lWgVFLNNxoqC7M-7ppo4d7Rys8CzN5VcxImojZVhlVVE2Z6KujocfuXQkQK29b3_5zRkOcdv8P1gr8pSlO-XhSXJ_U-9CgcTCAcmzYpg2IJsgzpWRHtm-ob5o2Yh4j6-u1PW6vUA0dcrMHqS7HxsdOGULRiz-KTR178C77_ZiVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyvSXh1LMbB1GuIfizgd_x0OZ6n0MQpUAax7XIXimyM1PwKnkjRW3QSjcgBOCac9V-_UWoaOKMLp3UjYFVS-ENl8zXVj2xYQ3zpVpk-2IzW0q1wrFMG6h2rUQT8zifsSYjkpz9ZUAzZcY9N4lapsIrPWuFSS1zWQsykqckXMZblErGrXYiJJMDmi6vu1V9QdiF2w0HfpgdmHm9j8Dw4eySZc8Om3nIOdYKvD21sixRYNyRFPZTcQxRS3dk2DlFnwm4s9Xaw7DWPfVx03VeJnt_Y2Sswkz4pNgD529fpjlKZTaAUlq_sgH3IfToLA8IILR3gPbA7yQEfQ_39HJC1kAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLY9H1-5edVxO03g34wSKEphzZZB7h9ehwj9qqdDTDGHyV-YBK4DTY9iRdziz5VAPFv-UektM8l68stTDvu56RQXU2F-AKcM56SFdZVzgdnlMZ0ApbhGuEnB73Rs1xL1pfZBUJsLx86rstonL6F-CCsDdtCVgftqpPYZ1ePl3-mpoNVld9epHYxmXxXY8TF6Jmm7HtHf-lz_egMh75TdAQgbDm1A-sO7ssltckcTddinnzToM9N2TUe5u0M16X5dJgmX2sSIEHqSysIZm_nl6M4qLNda2yFgBv37oVDTqGN31R5ew5IXdYigG_PrP8Xur48uKWxwXWNJP1MrhOQy1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-w0tyvar6g264cVj78Beff-ct7B0OLsSVqO5OgMEfOQgCkAGqarxK9blpfZ9Zb0DuQbPs2vASqXb6vLRI773oreQVTd6cyonCcfFd7aiWYXYssvll0zxCyIU-zd3Il2sqYq2xZhIICMBnYa8naoenpxA5Q4A1GORpqcDxiQziySobrMYDWDN_tpqOdo58GrX_BRTHtqZyQqnSYhWNLa3iwvKAlrit6OXQLW-FNWmCF2Lo1T6Kaw7e-AAasz-QuXVUXnsqD1nObl70-VZQIzI6frQnPeuS5Pk1WToxEOER7C0o-9dv4d8bFfEfrCvIAufNkYfjVDJb7TQCKKqYyIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTYuc8i6IdVy304ubdY12B2-E5zg0gHH6DTDna_t-Igpk2jQ9DwzR1rE6UVywcN5SBHXrpk7sfM_Pt_mJ0ZYsdCBD3xC1rPmo7LGL8FLupxKD-697n-EByOoROtDQLEd5PBpaynQ5OerUCvMhwmpEG3u1nnI8Y9OhphU-9ygOOsbhw2zIKLEsgHA98SCzvlMSjz6jTv0iExWFLw-Kt4jSUpkzkWghKq-3IgLroWUQ3QmIGUC6_1nv5uZ2w1euNY_qddOU2Qrj4Qkt3RWpckzfJWJZKsS0icSFzCcsjg_CeHpjGLATsQQR7qSJMIu86LavtY3B0XS_-oeQbTBMdmfIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=WtDMV-Hfq-FMUjMxtRNvUow3ANtTeTY8vOhmnM9cGvywEQYPw2oniio7GVlJIEKz2UtPNyf7g06g18Yzqhwm4ZQaBJQRfl0-OMTn1B05fjMaGFkf6WHMTUYJQwlaXLGbucKnKZTwpqNDcIpW7vhlXbGRv-bdtfYiCnghjXHNaRgpQI38LPs985-Bft25iDNmVRTsKnwUweoFGsdDim8LC8VPhEzulw_hqqS901NvJdomK6Xl1Z9Eo-CZv6ZV9UpoRrSrEy6ws3oRkUAT6OKl0G2pFiUDxkSqeCD_JQ-gUmFCGvl2K5ow8bcHXaPIoBXqJGB1grv98vwBNXAU8pDW0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=WtDMV-Hfq-FMUjMxtRNvUow3ANtTeTY8vOhmnM9cGvywEQYPw2oniio7GVlJIEKz2UtPNyf7g06g18Yzqhwm4ZQaBJQRfl0-OMTn1B05fjMaGFkf6WHMTUYJQwlaXLGbucKnKZTwpqNDcIpW7vhlXbGRv-bdtfYiCnghjXHNaRgpQI38LPs985-Bft25iDNmVRTsKnwUweoFGsdDim8LC8VPhEzulw_hqqS901NvJdomK6Xl1Z9Eo-CZv6ZV9UpoRrSrEy6ws3oRkUAT6OKl0G2pFiUDxkSqeCD_JQ-gUmFCGvl2K5ow8bcHXaPIoBXqJGB1grv98vwBNXAU8pDW0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
سپاه: تنگه هرمز بسته شد / به سمت یک کشتی موشک شلیک کردیم.
در بیانه دقایق پیش سپاه آمده است که : «در اطلاعیه قبلی گفته بودیم تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت.
ساعاتی قبل، این تذکرات نادیده گرفته شد و
چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند
و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
به ناچار یک فروند از کشتی‌ها مورد اصابت شلیک‌ِاخطار واقع و متوقف شد
.»
🔺
جمهوری اسلامی به زور میخواهد که کشتی‌ها از مسیر آبی ایران از تنگه هرمز عبور کنند و نه از مسیر آبی
عمان.
🔺
آمریکا از جمهوری اسلامی خواسته بود که شنبه - که دقایقی پیش تمام شد - ‌به روشنی و علنی اعلام کند که تنگه هرمز برای عبور و مرور باز است، ج‌ا اما دقایقی پیش آنر‌ا بست
.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pv-QoCuU1OhemD3_xnoAIbOabsy_EiQHmT4GA46ERQq6AX1q1HnMLzYFP6zvMPRzBGXjANmDTDPKa_lbr1T1_cPEG8lFZ4nwwliwmRVVPFgGuhbTzFi5oKxTb1mt1mMnRypM2t8za_Qxx65oUJvgnEZnhGtw3mO5c9GegdcwrkTU5FqYGF5MKcS-KMsmS0RH6pv0sTmitkNFuFQ8AFIZ-D-_ENib49voD_xqhGu2FX27Mj6gkB-vzg1uvnRUr8xKHsunaQXYlvaYvbxnLIwC1O_siWpgcg5-h7lyLObfGLexzd74otRL-wVWD6wYMu0uVtrG7JxL2KySNGc_T_ko9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=iesfmeubmOtKETLrX95iDNBXrrtNTkJeS4XCj1bitnPlBmHAPrMbbIO1S3k-TTC8PkJq6xHRdaKXowkNw0UBrtxwOFdGGXTNCP_gd7iscAHPZ0SWw4jy5KqqakTRbm9aJMb-izCxBpNkYKGJFz-WW78SUSHy7UWtTTAv0gFcCmXy4MH8oQv8NVu63MvhMmH3RnbOYN5JhtYZd4OfnymLP6qx4gelzrwNnsbHwGRF2XieGnfqbSmwWJcIiWM8TXFbrMAtsvUh0HNSpGH1sSl-aPWsFfvthxgJn3MqedjzsbwFbROkcT7GgWG3vZJE9Zlq1n87gBCWObHmvhmFJVruTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=iesfmeubmOtKETLrX95iDNBXrrtNTkJeS4XCj1bitnPlBmHAPrMbbIO1S3k-TTC8PkJq6xHRdaKXowkNw0UBrtxwOFdGGXTNCP_gd7iscAHPZ0SWw4jy5KqqakTRbm9aJMb-izCxBpNkYKGJFz-WW78SUSHy7UWtTTAv0gFcCmXy4MH8oQv8NVu63MvhMmH3RnbOYN5JhtYZd4OfnymLP6qx4gelzrwNnsbHwGRF2XieGnfqbSmwWJcIiWM8TXFbrMAtsvUh0HNSpGH1sSl-aPWsFfvthxgJn3MqedjzsbwFbROkcT7GgWG3vZJE9Zlq1n87gBCWObHmvhmFJVruTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwNs_ogjXK5y3rKSLVcXew-Xca0LDEz8kcKOnr68M1LO0ZKkskouFpH8OjTTVGw1Z_KJZD8wJ6271VneZkIaVltDKmnoY2ruwYMbXzxT0ozQFmHCXRVKab3DoNFzyfr4mDshcKpnErO_FRM00NnGvKV4x3J0_Af2jXirxmYjfBc1Cr1JIlEM5P7korcEt8_upYDX-Lkw9f3ni0wvk91MM6wRUCPpU5-8Ds0ScPBkl0KgvNB7MhyOI-qroh7cMVwDAB8v2InGqhbBqNmwEZfRC_EuKeHbfHWdwPe8ANgVwbbWdjGj0_Xnr1hdfsncAJsJWJ6aOjnhsACc8gWTdDY02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdLd39yL0aiCkIoXyOFxTP-lkaRbcR93-Flmabx9TZB6bEab4QYSBZL1KYZ2KOAPMSPXVHDE30Wb2eBDlvNFAShIHkcYNLBTPaRpHAGWvz3rY3gKFl2167cELFKrO8oXtqeaKK1DQc3XlxV4INmpNqzSL5athpayarLlWsh8AvyKi7gH6senZFuuqIOZG4-II-E-PSbNTXcZ9AuTETotC0jHdc9DDAxB-74pz-v1DMQsdECos5ARmeYGQ7G4H7nuT0750iT1eOCA2CIYDq2SmtSO-Vtlq8ZdHpEN6hqBhNh3F3rN1fN4XMM1eYu9ILmi-BZ_Wlc3kNOJiKGyS444Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر یک مجله ژاپنی
در آستانه جنگ عراق
که پیش‌یینی می‌کرد جنگ جهانی سوم راه بیفته و…..! رسانه‌های غربی هم پیش از جنگ، ارتش عراق رو باد کرده بودن و بهش میگفتن : چهارمین ارتش قدرتمند جهان!
رسانه‌ها عامدا اینگونه می‌نوشتند
تا خطر رژیم صدام‌ رو پررنگ‌تر هم کنند،
اما این باد کردن‌ها، در عراق هم باعث میشد
که فکر کنن بسیار بسیار قدرتمند هستند
و جهان به قدرت اونها اذعان کرده.
رسانه‌های غربی با «قاسم سلیمانی» هم همین کار رو کردن!
و بعد ترور شد.
تروری که ترامپ هر روز یادآور میشه
که اون دستور کار رو داده!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=AD4oE-3Nr0rfmUMlKN-4EmAO-j3zedu8m8r0YFqRVmTaG_2-_NwkduH-a83vC3RzHblVYPe4PQs95AJtKxkgkSBMSeoXiNAsJi5ggHtas8A5yB6C_nEPx6pJIWxT7zfkarnx_UeukmnV2tNzMFxNsHReRg3IydkwL-9mJYkuq67CinjlJbcxZKgzxpQEijmBAdMVN0A0IO0bOzb6FHjTKxq-1V9L62E8uyNTubF7rZUcLmiv2kNRVwnVD1-dZrTZc16Fh_7aWxzdAaI6HPjD8HQPf5dFeQ0un5dXnq83El71Nfg1xzrwb709SfdvSAhlu9HGQSa5dTxhynhHkRe3UzSlRzOj5_9794yfZ_5Len5XsdV7UMyeNKAV86JxBFhE5LIolTJNBWHTpz7tg9XKamD3UpHDsGg4xlzOfUZ6QnyQI4RsThAko_qUPHB9G4K98htc9ke8J4EdP1_HNBX7B3BhNgMsnzFl0Cll0mzgqjt9_TYuiWufkVB_dfDeysCLUZZO7c0sVX7ltzPEig0qWQNjlkOXMVh0fnQcpXmetPVTF3UxLVAVP2qI9_x3clfFid8IE55kMF-x48VtlPh0jZVFeBTQuo4x6KQA3OBcRmutMvwr0EQ-5Y4ZdxCuaqg__PwXhkZbSjiQWOJemgIiA0jHA7L7-Y5Y4PqahVD3P3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=AD4oE-3Nr0rfmUMlKN-4EmAO-j3zedu8m8r0YFqRVmTaG_2-_NwkduH-a83vC3RzHblVYPe4PQs95AJtKxkgkSBMSeoXiNAsJi5ggHtas8A5yB6C_nEPx6pJIWxT7zfkarnx_UeukmnV2tNzMFxNsHReRg3IydkwL-9mJYkuq67CinjlJbcxZKgzxpQEijmBAdMVN0A0IO0bOzb6FHjTKxq-1V9L62E8uyNTubF7rZUcLmiv2kNRVwnVD1-dZrTZc16Fh_7aWxzdAaI6HPjD8HQPf5dFeQ0un5dXnq83El71Nfg1xzrwb709SfdvSAhlu9HGQSa5dTxhynhHkRe3UzSlRzOj5_9794yfZ_5Len5XsdV7UMyeNKAV86JxBFhE5LIolTJNBWHTpz7tg9XKamD3UpHDsGg4xlzOfUZ6QnyQI4RsThAko_qUPHB9G4K98htc9ke8J4EdP1_HNBX7B3BhNgMsnzFl0Cll0mzgqjt9_TYuiWufkVB_dfDeysCLUZZO7c0sVX7ltzPEig0qWQNjlkOXMVh0fnQcpXmetPVTF3UxLVAVP2qI9_x3clfFid8IE55kMF-x48VtlPh0jZVFeBTQuo4x6KQA3OBcRmutMvwr0EQ-5Y4ZdxCuaqg__PwXhkZbSjiQWOJemgIiA0jHA7L7-Y5Y4PqahVD3P3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM4nOSPjj458Ll3g2B5a_b9H4CAb2zQZ5-7OVZBSu-t5zj3jiOjwNNsE0XjiiSAztdUycD-OEuwYmi-87AU9ZdrEu8Ov2l8olbwS7xCH6fLa4xOV_xR-gyEwUtBdKIaIX5FEUP82-mteLzx-3wWhYA3n0T1YMbhP8moPto_Se48dneGu67s6V3GQtByRAXIwn4afAeS_85YHdyagDvsFYduQ5xGMfdLEboC5VhUPG5T0smNgKJCLTpPezyQrtEwcoZrEBSMemL1xE_4rI-y-fdn7XdbtkCedvZ2Kq8qNqV16_hw-4R-J1EILgq5Vrwfc4pfmM9gi4zVnEhWIi0UOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q12o0PY2SSfkqmyIwkC7SRq5YY4anEVoIQeQF0BJsclyIzlvP2G8M2RUvpTF5f2kk4nYcnURE_Zw50yCdvgmID2KvvHDchsU27J19zOGL1cEEXjxB7zJ6P8RfqZR0KwL6l_LIRHF0_ve4c1rZ9bp5saQPueGCc-SmMlanl2wenhuUJ5729U0lY3744_jm2IUCoOmE07W7yckS32_Yy9aq4MhButmHlpLKTevj4QRqpkFpKOIdE2xErhMjf9BodXa-KjAp82ZIUReaNskrnFaLZn2EN9CaccJ1JpmwfCwLbu17zJDnVB4qKDW1nNBlqlWts2fXUjxwlWpnUcVRG_YwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tN9Plq6f2g-7zuaE50f2Nuizvpurlb8l_yAlcwcn0eyzs4xXqZOPnWNyqYwuh1sCDpCu5qN7FUMDpC3vQg6JT5tbJ2Q3xOPu-8U-xkP4FijRc6D9wtqVNt4WvNF0ptGVVlbtrTCkoOfPp6mwUJMI6LvwrhMnQEKtstO_XPfYj-pBW4f4YU0Z8MqW_SwsAGztjGz80cwh8QJJ5KetxRLCnWr3NW4Mdy7skR6soFJ_1tMBHDrFLjvfPJdfOawBJQq33khtLb8dFCrGJggkuU4tgwT5QHT3-9J7XnzCZB628-wE565sO9WfzjEpg3wG7Q2EPZzH-6B-1h4DlBLYOPX1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=oP1wthPq8rGUcZBddwFJ-rTmFTxWVMGtWvttKBE__9FGpunK3X0gaKYUQEZbBSmY9ySpiVxsZe2kf8NKnQil68KN05JfE2mDqCwCIZYGbJJfLvPhVki8E3APVsubkzmhLtdmj4ju_UAyoQRxg8YXJovxKnPvpdksos-r_oMgc6uod3-ZXMfsfmoWd5qDI0J95pvtw95x3cC5TFAyjCNV85zIA9Qh37vp4rDtiAlBqMRxfTw2E5tMfZauv6RZvKIfiOcvAzaCSoU0OHA6cAPI4F9YytVls0XvU0BRU0_vgtPaNR4vacebZ7lqiKmK224vZg1UNKI1uOUh9vmeEKZ7hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=oP1wthPq8rGUcZBddwFJ-rTmFTxWVMGtWvttKBE__9FGpunK3X0gaKYUQEZbBSmY9ySpiVxsZe2kf8NKnQil68KN05JfE2mDqCwCIZYGbJJfLvPhVki8E3APVsubkzmhLtdmj4ju_UAyoQRxg8YXJovxKnPvpdksos-r_oMgc6uod3-ZXMfsfmoWd5qDI0J95pvtw95x3cC5TFAyjCNV85zIA9Qh37vp4rDtiAlBqMRxfTw2E5tMfZauv6RZvKIfiOcvAzaCSoU0OHA6cAPI4F9YytVls0XvU0BRU0_vgtPaNR4vacebZ7lqiKmK224vZg1UNKI1uOUh9vmeEKZ7hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B92zDbO8pJmYBeuAbRr0oti0SY66Fn8Iyx32vifZNCIWW9hz1psfJRQLIgJZ4m-7amx-LTMN9NeO4419tsgks-yGGcrUfhYQ5zzougicQeUkixdRXpClRLT3ynpbTGV1TwxHVQRMZZS5F0Qusb28s3_dB78fm_wLAVrrJBDxqH0a9ATXoiHxtJ4SgXTlp8FKBYgUXNF0mBZrlaStCY6nIcbcZk3ZMzOGhrZsGPYGUQxiNwXBXfu_ExHTPj8P0kmA8dh0cdEtxCieb4qrFBcF7NU-0QufxUwrNjNpJQjVZ2CnlONIn5wZ5q4mhK5lKLuGvqpDm5kwMql6cEXNkSyj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ts4oq4-H9xT2yQXlDvqaSXe3cv_VOoYGaEjn31dWA6tzuzlcJr1cRAdhKhNu8i6sLmxGwe3r9KShFVp2lQc0L02Ctl91f-lWHbxYA8gsgaiFgG_1AwdF_UPYUxb8B9VoVPO24uYiSk9PvSg-GWnctTVeYsNtczkTvILm3RMkVZVZUFxRdIoLbGJDKAMUw3v32nPRZEWrp3GAL-kdhkxO4CP0mB-hIU09baIA5sYktotr3jvetrsadfZ5hKvBeGbMLamoQiJ6s5-T-qxPjhwzZOImHIBegymn4rY30zY26afN4J6jrh-sMWwYmkRT5qj8Xcw1OviMbN1NJr_J6WNtjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQv7w-JmwI5I33YOcfgvmEBLLAFMW3NUpk99u4rxQ9m4mLJQQAN9Pe9EAxDzOEVSSUrJJFzF2hMUn4zCCFvfe7LvMNCuLh91cDmCVV3G90VIR4HIu6q56jgV76t3q6H30qQLBxmtp8D_I2Sovx7DoAhIz1cutrwLPIGJJaHanvLg61UiSHgvBTIgqJzB2h5xQ4MMmuilUvJt7uhYYJsvK69UngDEObfDXpAVV3x-UPrCiciv88JFyEU8-ZXO0XpzX6UyXqV1kgOSjuTJ-ffImeSoXHtcY3L3L_qWHVuaNooTznR8drLKlBClLNlngjB6O59hNznoL7YUKIvllNC51A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooe49XZia6nD-8ucCCXGh6WxPzMSTyE3f7wDiLtU06c5x08ODBAZAZ1utp_SZBcknV40i-K9qCtS7sdYnWUOSYnZDYjEY3BCYkMpKWiN2u-r78x3M5BJc-jqq6gSoBEIgizdLZbkuxUC9sfjD-dVCCTstc0JTdc5tXrRUoTD1bMZXpm9oqw0WMO0EU5Zu6XnEexItMSFp5zkFFFlUdrr7oxuOfZMDGlWcmqNqPm8KaRZLnoLjJaEeOE57gXIC6nZ6uYXjrtgvkLcUgP9F-idOQIJTqiccmVTzNs_DY8CxD-_BWRsddkmzAPGb66R_CUQycUlnoSk0WEAgzqgY8z-dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIEm_sMHObrA1n4wPtsla81G9na2BJ8kopjFs3cFBoD5bj9ns3Ysc2v3g6WCGwz1p3bWpEn_TiWX1TAn4iMCzQ1V2JLggcs07FkqZSC_D1utq6DxylaNfb1LneO3K4uCKwc8yXia_HbhFXIxe8lxVmu2Xr_am5-HGsVNkpHg7iDNYCsi-xufPz5E0iQnVtRJdBWavPDqmJuoGVcl1KDDM0kSgZBXlkp_eG-0Z_0D7e4KHp4Ql24Si_-s3VjJDfZhR2H1PhYWsWg4Pc0G1pTqfZzhLWsjtp1gnEJy4IFCc5Z6wbZ-VFKMOb-lAe4JyIW0ngAsgpHi2Qc-j58tug9EjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xz_tWCwVz9DzwOzH2XQVLR1VawEk_UG7Hf3Vc_GjaJWpldQN4oEYNBpaS8lbTFBsnQxqYYVwysUzxO_JM4fAgYo1Dcs-VBjwUINH9iFi6hWA50_xAP04_KK0xrPi-1GxW9piWOtzfOcfJ97vxkUp3h-zkzaCT3N_pcklrtSXX6rBOSp16hQUuwJbd7fNS8g6Av-1qqDsQr4G0pwPAIy7BCqDyzZIGZbgiE3F-NQHU-Kedh5DcaWs8JEygzDn4W2tr0z4C48KKFTPpMXpefTisG9echf3sZfDPkkCT2njoe624-D2plIaHgtJ-1ekodsYyyp-uVAXf9WN4X0bKj_8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_e1aO8K3DxFZVsb7b6usQgr2pJ6pLJHAPfKAgkE0bjn64bShJBmdh_xZF_ZZ-OPtTDt2BwMBP_AxVklK9FuqAGosmid-cliSTBIoKyZs6pBNfaUafB1ZPKaCw3rALgFIBbKbq0ZKuHUHkqnPrvxSRRfzwlRgAMB08ZJ6k5tE4YHFoflhHNiSbazJCfW19WdevqIoA9sE7HTI3X8yCELeFJRd-VgBC5VABGpqCgxfSQDD46lq9egPouq_q2zwPPuHtDDLzO5w7Ok8KotwSvl3e_flYRxd54wfJIdmw3eBZE1zEU5Hogvqdm9MfkOOuqMoJE13VD_oo8PjIBJjBJNgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugoCwwMIZAWzlljvkRp9YenBFD-Hr9Bt0j1vzzSCoaVIyFNEv4qKTHDO_s-ziNyKkdFGOCxMjim-POBXY3U0EE6oC6Nid5IL0syctJRnvVF2ID2Lj6rO1wrilXDNwFCBxGGPGzbN1omhS1BLPSKOG8PjNvrzW3gVFEuNKDF-XXsYv2KrhtQVJJxD-okkL8an84Z2l5AKQw2a4p3imU-L8dwJPV0F7uNsDCQDYgPd60MTjmry99zLeVLYNJuzznA2DlC71k-lK7xZM59IU4xK4WGTUmJCzp7fc0lwBMoO9o8-kZN1vz7BzxCzBhn5p4OSM3K6q8cDFaCKnQMYysZMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pSQodl2blufFRWBZQMXxC1WXWEcxZmTIX8Lis2e63Op_QWLuxqa9f0B5rLY0uKSvgnHWly_Q0PI5QaE5y4xU9N0hYan2A7iQFjdJsafNm-OAL6crLFraXAW_zqRqO2fJKWDadCYZMzKrGyxsT6LKDy-deucqoq6PV2BE-iNiDDHVvlmnr-oOPWLT0MqVhqerI6gWctEsknLp0XX0ZCjIS8lI6vx-qq-zU8llbWchQdg0kLOnyO25x--QD7eYhKQzhjnUyYQnX5y2qxyqnqu5o_kFpE9jPoi-aOnKHAbxgXWea-XdKV1FXxkjHP5j2NFGnkAMuEw9EW6jwRz6VXr_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8RoW9tXu_055WqMlyj1Bj0k5x51zaUwB7OFSijXexil7YP9RtvTGW2oBi6ruuFFUHfmL5pet7zmVfc9xXL_GXdI2sxsaC-NDcwSgy3Z_M4ycMq_8XXpu5vjenCoQtQID9tMtfMoUwcJgY6Q2oB0WvxarXlE0eVqOg7rqpZXYeuGTLNzwX9ggXIpJklsnbSSZqDAW2V5THxjBJ7XWV1yFov6xlMUKw1tbtN4ckiA8a-nwLJtxUmi54CfHLf2emFgJ6JXV2W5W7W3Ourpoai7TjSYAwBEWJlfi60U65YBRYC43imtMz3wm5FvbEhSK6oev5OEbfIghZPoq4mgba8-fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=MEdV0sk2bnieUt0o72RpcR0jXkEGlQ7PhAtg0TXBeqpA3vQRaFdfmaRzn-_T2tYyKmBizZ-Byfrnn6Zeqasc-WEQUOpdp_VGvLFNidtYRB4-Qp4xvJsyFzg0UKmPJBnVsSn8jdyBSWL3UwANEUa7m5K5BWN8K8sizbxbYpCc6NOw0i_HFs_g4VxP7RfE1F0VlbSSjABLhwTmAx286QeC2RAZLAV54miKIWsasBdOaPnRlHEzvgjA7CYcn_XZDWqrxLxmJtCQip9lwiN1kZrh7c13htdeDw3YH1tZKmFgD1FKrTOfpo4-pLpc0nQd18vi14lkDUZog1rsoSu5H74kGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=MEdV0sk2bnieUt0o72RpcR0jXkEGlQ7PhAtg0TXBeqpA3vQRaFdfmaRzn-_T2tYyKmBizZ-Byfrnn6Zeqasc-WEQUOpdp_VGvLFNidtYRB4-Qp4xvJsyFzg0UKmPJBnVsSn8jdyBSWL3UwANEUa7m5K5BWN8K8sizbxbYpCc6NOw0i_HFs_g4VxP7RfE1F0VlbSSjABLhwTmAx286QeC2RAZLAV54miKIWsasBdOaPnRlHEzvgjA7CYcn_XZDWqrxLxmJtCQip9lwiN1kZrh7c13htdeDw3YH1tZKmFgD1FKrTOfpo4-pLpc0nQd18vi14lkDUZog1rsoSu5H74kGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=nr5ygb1nswrl3SEiAipEHv9c7o0iDTqgHVdB2HlCG8Sj8fI9rexnoH7RWVJSkm_nT-waj4Q0q7S5SGOu7shARfxkre8aTPkvThhd_HTIRHYphflR8vjyxNABqOpXhdEu-HzE5UvredUvgcYaDiPRAXHBehJgYrlS2a2iR4lPa0Yk_lyPZ-wypgVfB-yzIi696aC7qXyrxppsQL0kdPPqV7grIZAE4BDwqpdr_vJvY3wYZzQk7dOQTb7wwqPdhNGsX1Ld5dJOkdd-Z2Cu2jNKLSnDrJqWJKOKgA9kQphfwfapaSVDiR0nM4cqf4CGBe0k-Ole-BKyuEvBv9-62dsqg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=nr5ygb1nswrl3SEiAipEHv9c7o0iDTqgHVdB2HlCG8Sj8fI9rexnoH7RWVJSkm_nT-waj4Q0q7S5SGOu7shARfxkre8aTPkvThhd_HTIRHYphflR8vjyxNABqOpXhdEu-HzE5UvredUvgcYaDiPRAXHBehJgYrlS2a2iR4lPa0Yk_lyPZ-wypgVfB-yzIi696aC7qXyrxppsQL0kdPPqV7grIZAE4BDwqpdr_vJvY3wYZzQk7dOQTb7wwqPdhNGsX1Ld5dJOkdd-Z2Cu2jNKLSnDrJqWJKOKgA9kQphfwfapaSVDiR0nM4cqf4CGBe0k-Ole-BKyuEvBv9-62dsqg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2ArRYXKuTDRen6Qa0Ka04Ut4ZcqoEfUZABhbMYbK92suFR0bVBPwJd1-f4F_sX6jtSrw2DWkDege1qkla2BM5Wa1eLYVo8cEAq0Ki-u1yjVXNxOpeEa0OxC43JbnPSoBSAHYpplm8qgZ2kc4053jYLqMN_Xj3xPJz4vx9L2RGY31CfKf1lY5WVs5fEBl_Ds_jGywXOb5OXVs_kxrPPtkX5Bo3fAkB-eLYvl1qhQPJp28XOgMqD3fVphm0C9Zysd3t53oRlvbLGVkmhIzEQX4yreY7QY-FVdaUmBsrOZZHZtPov1MxCr5gBvtJ6NnxUm2S3UsPpyQg12bNCoNf4ZPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDkdXxZsCeZCbe84IIaL08fRMYbNf-5r9duUSx26NPBvWTKBkrDinovqv9XAX1wZDQsRfgewdEk3d8VcHtGdzYAcWRuDMaZhVLK0W6V63C_5iY-2DgHkHU9VbzXDKBBEpGI5jAGfaP9J1VeGudoaY_U7A0zAz8VDnTdzlaMsTwl2YHeBR8PQWWcAkEGppggn3t5b-K_mxkuXCqH92cr13JoTBdRrcSnWITUwBPPWTkdD2Q0GIxsHSGnVF7I8InwrWeemS73HUM9o39PmmTYglXmrQpqItiTh9RFa01yIt_9ZTUfzXXkWRV2YP6t1s-_63YWd0voc8MhHnikq5rrp9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3baoUEOibU-iM1Z59jPCQ_1EFLeMcRojLcdSLpwQQKsc5E-k29yNgTwcm62SmOkhGkWg3YP55tXjJiH7kktOrFjCPROUp-hr5zqENMLvJij5VjfWA5X694wp_LQsE2qem2_iqc3ABiJ3FhLPYQdj0j_NhJIWo4PZS0ZvAmyHSko3TNPRvNqIxhv5F2SbzmeMfSJLzqY8KeDN1kAeaTDfiEPXD6saIvtbx15eLRZuXRbpgEoECTSIw2Km2d0aIwI44KTgo6NRlikdnM34RVbFt3xOE6CKScafqNIUc_NF_Gx_IDcvFCmxOt0xuKFCjmXGUGTi2247kpGNeehiAfahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlrpyxVYXTWoJAYNiWUS2VSl8CEtJqpgc6-bx6Pmgx2QiFV5Y72nJNOUnq62k50HKHNLd8-IoxaG4mgEecH8hKU_CZCzyzYaJMZaTRIcAUgmv5OsComIxZIfAK5jrqC5BWwv01v3sWml7KZMD2eJ_WPXD391Wr2IYPizPu5CfjZKQ-VifIOIYEQ_U7FYrAwKgC8qs7SBfNWIt9E-GE7Ivnvz3HeEL4Ts4HedvSsAGI3dN9q3-S4orNJDmFCLpURIyeebTmbVSoOSJVGMiuoJFyxkss0LZ3CDuvrXoTqnd5Zrzzafm8qzxqavsUiJ5FGzHqadi3utJlVdAg1OifRXycy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlrpyxVYXTWoJAYNiWUS2VSl8CEtJqpgc6-bx6Pmgx2QiFV5Y72nJNOUnq62k50HKHNLd8-IoxaG4mgEecH8hKU_CZCzyzYaJMZaTRIcAUgmv5OsComIxZIfAK5jrqC5BWwv01v3sWml7KZMD2eJ_WPXD391Wr2IYPizPu5CfjZKQ-VifIOIYEQ_U7FYrAwKgC8qs7SBfNWIt9E-GE7Ivnvz3HeEL4Ts4HedvSsAGI3dN9q3-S4orNJDmFCLpURIyeebTmbVSoOSJVGMiuoJFyxkss0LZ3CDuvrXoTqnd5Zrzzafm8qzxqavsUiJ5FGzHqadi3utJlVdAg1OifRXycy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما
که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!
همونجایی هستن
که بهش گفته بودن
نفت آمریکا در ۲۰۲۱ تموم میشه امروزه
در ۲۰۲۶ آمریکا بزرگ‌ترین تولید کننده
نفت جهانه!!
سال ۱۳۸۷ گفت بر اساس محاسبات کارشناس‌ها تا چند سال دیگه  دلار و یورو نابود میشن، در عوض و در عمل این ریال بود که نابود شد!
کلا محاسبات و آمارهای شما همیشه خیلی دقیقه!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=BuWupn351V1x6YFA-bH8N8H_1j7lyqbASUqyQJoact1J1Cj5gHg24uAij6EseiqMP2Cj0Bs_uFgBtRtfzRe2xOFl6AreSVmnm1by9rEZZJP17ZiDW0sSVM6WqX4v-fpOtF7mgwn2TQ6ZiDYOpEBg-JvLefK7KVtraZ_lBowJaCNwV39a5PK2bIQ6NTmCX5NVNsOjGxoL0K9JZWx2-MMp-vj6jAWEfeVZb56jHHrA_wLqbuDEGXvcMOa_9lUG45rSDRGAGi3AqqaX0y6g1nN_GONKaoIuNNJmxL1k84ab3EyRroD-97F2_FEdNKWMHBbiEDS2hA13DXbn8NjD5OYBGLWbg8VFz3gxgQYFEaXPaIPYseyZMN5umYtqjo-vfjQ5gRJF6ZsJYzfVPrNZazw-9HxvpWkLXEV8Ia2-z9fa8yaUi-QvUZqk-5E1Z3DxpC0c21zC2AFI9xF7DVOWzj_rtEeJtjam67PrE7NHn0AgxNIF8FDAbAmGdn0NH0hPb0nOU6ppn8J3GTsTZi2hO9Zd2xDQWbe5u0QaeZ3C4-euAOS0O1IqrXXbxmEHwH3CTE92hh6D0N5SsPOcsuUVB1Q-vZQTBKKN7N5KjWw6eFrXclOYtHiPA6yuNDGTzv7JsAsCSPiaMukj4W9op9rDopDKg4Wa1lo47xhAoJY8jW78CuE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=BuWupn351V1x6YFA-bH8N8H_1j7lyqbASUqyQJoact1J1Cj5gHg24uAij6EseiqMP2Cj0Bs_uFgBtRtfzRe2xOFl6AreSVmnm1by9rEZZJP17ZiDW0sSVM6WqX4v-fpOtF7mgwn2TQ6ZiDYOpEBg-JvLefK7KVtraZ_lBowJaCNwV39a5PK2bIQ6NTmCX5NVNsOjGxoL0K9JZWx2-MMp-vj6jAWEfeVZb56jHHrA_wLqbuDEGXvcMOa_9lUG45rSDRGAGi3AqqaX0y6g1nN_GONKaoIuNNJmxL1k84ab3EyRroD-97F2_FEdNKWMHBbiEDS2hA13DXbn8NjD5OYBGLWbg8VFz3gxgQYFEaXPaIPYseyZMN5umYtqjo-vfjQ5gRJF6ZsJYzfVPrNZazw-9HxvpWkLXEV8Ia2-z9fa8yaUi-QvUZqk-5E1Z3DxpC0c21zC2AFI9xF7DVOWzj_rtEeJtjam67PrE7NHn0AgxNIF8FDAbAmGdn0NH0hPb0nOU6ppn8J3GTsTZi2hO9Zd2xDQWbe5u0QaeZ3C4-euAOS0O1IqrXXbxmEHwH3CTE92hh6D0N5SsPOcsuUVB1Q-vZQTBKKN7N5KjWw6eFrXclOYtHiPA6yuNDGTzv7JsAsCSPiaMukj4W9op9rDopDKg4Wa1lo47xhAoJY8jW78CuE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tR1Z8JzIQR_rqbzpjIqw_b-Lj1laPqWg7qL7uU9BxzS-0wNG6TQNYIdp6FcRZHEksW8vj0SEPa4es2ZLYmJmaoXZQaOdkzaZule7OKDcrsnYpQWYnonHU9GISAItnMImz9JvkvlilyO_FQuOXA452giDzsRm3yOHjXmOKHoguLXmWAc27HlGdvZNagsLOeXDJ7apbteaJVJTdqEsx8aKYbLscnIgoAR1yI-5LWNqmKL5PFy-h6jkwW5xOX0qftoXonHgkcJU9AZ1Mm6mnP9HGIv0ru_OhpUU8KVQfX1veMljiV8_EWsivwH1CQZTl9drih2uaGdUgwIt1WycckxEKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_aalwymGckIF9ldVFkMEgl-cgx1Sfi-xxVwpV6Y-GIuW1yPtQzrprPiWlGTJvYve6EqC9ld5u2lb18eSRGsu2LgnkmFUu9frxrDTemUrChrlb2BXz3DbQaC68NkS3DNJa7wqitUjWWptg_Ev32QKEzoJhKUN5ANCP_1qQ4yhgJXQ6WIleRd82MGRXzpxMPFS9fHhq5_QYskwMr5OLZ4F5LpumslRuEPR82a_-MBH0FqlEJTvivuJ0q-58O4jZ3n7xozMcflfq0fMYrjrrdsax1OYHQkiPBSQ89iQLiIyLdBnXTwiXhYhUA-OswvkB4XLYqcCjoaeGRzyoNaehzIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb2CwYEPJvX033ntMr8P2JRGBuK1LM_lJmAMjd4TQxm9JeC3fHuS0GTWEwwWnLHV7cWoSK0t5xQGmL5O1lxIdIG44dPnAQrNdQfTFUDmGnNz1YrkCD023COQdQg7X5b1p_AxZTwFlXktZGd1SJcdCE6dEjhvL2ZB3AnT9mckpWFYfYvvCmQiRjb1lM_ET8UQVM-Vj4MkBhHlC9Cvctt7FLTVq3-gYHwqJq7M_HbTYl1LinhV_SX146MAlASpNOC2YuP3SYC9jnKDMJBaqjn5yqaYsnLGcV8MDBNGpMxJ6c_3mIv3ksAGJNE5YZ8nMliI_g62dYJVNqgptGvsCYHlKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=eWpxEFLdKGFPkRSAfZ1SecoT1qQBPhy8azEsmT-IdaruBa_txe8RTM7qanE9tQGwYQAw0qCZr9OtBaISVy4is6uGj8SX1r5laBQ2TSydz-14WC5E2UmGR4q0othurdJK4lOZcmUDy3Qw0sTb1Uw71jASrsgaa43cdhwuYBiOojc7lMM1ZfiwQMvUVI7rTL6XnaesqAHYPd4rA1tMWVEiL_IZzQmbh9U3lPc8JHLkF2P1cYnscSK9vZIT8ULC9o30twbFhxGVM8exMMQWqX2miTENyh5gRTFdXuFcWjmOCvLEl_BYMtf9SGterXyv37FVVAtY2j6-TK7gxl06c6_4Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=eWpxEFLdKGFPkRSAfZ1SecoT1qQBPhy8azEsmT-IdaruBa_txe8RTM7qanE9tQGwYQAw0qCZr9OtBaISVy4is6uGj8SX1r5laBQ2TSydz-14WC5E2UmGR4q0othurdJK4lOZcmUDy3Qw0sTb1Uw71jASrsgaa43cdhwuYBiOojc7lMM1ZfiwQMvUVI7rTL6XnaesqAHYPd4rA1tMWVEiL_IZzQmbh9U3lPc8JHLkF2P1cYnscSK9vZIT8ULC9o30twbFhxGVM8exMMQWqX2miTENyh5gRTFdXuFcWjmOCvLEl_BYMtf9SGterXyv37FVVAtY2j6-TK7gxl06c6_4Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWcU8i7Fg6NN405YlmAv4Zzkv77df_U7hemSzUR4_qYlEAzPayCUCU8cye6cTmyebry2T-8gQJy8K1vd5L4-HNMr84nxByjzKxIty_C8XNwiq1wM23FOMxFS7WOLl_LUGAVA8gwZPNMddScW5ZFnDkHaC66o15orhigfDouvCiZ6LsWU-s-OTWxhgOIgcYkCF5xFbs4yWmrg02nA85ds8tn7DpzEi8SB7rvma-lytCFC15ZoerMu4TR1BcCXMgOJbanPMcuM0TtFl7K22mgM9zKm9DH9zSmFcB5o2hsrQbJhfMvC0BKb5FxSyFzyaFU0kujYtEmITEGpEG5lG_M2PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=Zt4UPKORgk4XKHv0sEasMMwEaMYX9Ge4SNcVgX0t3ITp0lUiqpIya5WNC5uctKrPZfdE94IzcG321cQ-XLCjP2_oT9_7Fa2HaLLL6xYIq7AiZ05RspeDAtIAGmvEThgCfuqude9epM1L3e3y_QtO_WHZqatkRby9ZwRqXCvUyvz1O1et9ils9PoGQc0yyE_cV-XPiONEs78sqhA8Kb952C5Qa9TqOPnfIkFRPJXPFsvFpU89zHAg5nhntkyY7-5RAE0FiFAlAjyXAssJM3Z77Z_rtqyxlQDaTSTKoh4WZHMMXXcqmBBIvM7QPZbW4b5xKEmismmaB1RL2eJv-viTxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=Zt4UPKORgk4XKHv0sEasMMwEaMYX9Ge4SNcVgX0t3ITp0lUiqpIya5WNC5uctKrPZfdE94IzcG321cQ-XLCjP2_oT9_7Fa2HaLLL6xYIq7AiZ05RspeDAtIAGmvEThgCfuqude9epM1L3e3y_QtO_WHZqatkRby9ZwRqXCvUyvz1O1et9ils9PoGQc0yyE_cV-XPiONEs78sqhA8Kb952C5Qa9TqOPnfIkFRPJXPFsvFpU89zHAg5nhntkyY7-5RAE0FiFAlAjyXAssJM3Z77Z_rtqyxlQDaTSTKoh4WZHMMXXcqmBBIvM7QPZbW4b5xKEmismmaB1RL2eJv-viTxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvLEd-oQzhmii9f46XPnw9eMzIpdb_PomI_rAq1LqEWz46x2mjP7wgT3wb_IuGipyGyp8mWwwMrPGYSzl2ZPT-n7SMC9UN9y-XGP2LPWhGiXgE5XjRNueT7V44yEQB33kZnYuTf44Ztm_a5wK9-evdh5qmkRbuzVP-t4sZ2AbBdbSlRUo550Si3LKUITX3vScXtMd-u3wAG2OyeFOJj-Rye5Xeuj_Od-hHvPJ7lr-AqLZBhOCoLVegZXkLi-JRZ8VR3TQi7clQjQ_738yomiskXuaLZp1yZusaJKBgP6TswZGr9t2HMHaBtpWoYDON27Ap76xxAk8zjOlO8VXL4cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9nV8QRfGuX5dP73VqhxKALBxWi4r936KE6MuJfshv3hobcWy9lnqkuezbkV1l9M6jYfQ0RaoIvhH5WuAljhht0W1mcE28w4-3sGE1va2AcWsTGbXagsBhjLfGVSZogQVGce9gKO5R9s9pD_bmq1xiQRPIln4J4q7Sd5NBrl7oNobkW3qHqsIB3LXQ3pz5bcX_reV4z1FlJj_cuO99VlVk0urn_Ugxvxm1sEsHMdI0Sdz1F3j20ga1lX5SdUE4tbNBmIVRQK10RIXXEtZspsBwmEiuqiXJpFXj2MKugMkgnA_1TNv82mmPiXVuad8NVGJqJpUKIhtgHwxbsvFVZWqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=kxGvIN84GZWqETetYbK6I235kvJh43pl8Ja4O9fnt8OoS87pusXWRRelK2rPm0DzWw3t_tY1N46MDfw6ivimY-81P26AcdsG6-B5XOq9R0xUPm1iLZcNaChPBsZ4YwvzteMfEyTlMLFpnfsNTYnNKWUWo9e0Tq7xCu1iy-h1GywrvNM9cNIRGjILTfG9YWWGlvy4v3Qkb94cfT4xG60G2c3V4xrGa8utdfQPyFPRKumNKMC_y2VNv39PDe4AixoFiucQvtGRrEYWX6Wm8oAdN3xf79GBXayb0ppMq-SaWzotZzsx_YvOfEoHekKCA_T0PIznJhdi3YmQFBAX0WMj-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=kxGvIN84GZWqETetYbK6I235kvJh43pl8Ja4O9fnt8OoS87pusXWRRelK2rPm0DzWw3t_tY1N46MDfw6ivimY-81P26AcdsG6-B5XOq9R0xUPm1iLZcNaChPBsZ4YwvzteMfEyTlMLFpnfsNTYnNKWUWo9e0Tq7xCu1iy-h1GywrvNM9cNIRGjILTfG9YWWGlvy4v3Qkb94cfT4xG60G2c3V4xrGa8utdfQPyFPRKumNKMC_y2VNv39PDe4AixoFiucQvtGRrEYWX6Wm8oAdN3xf79GBXayb0ppMq-SaWzotZzsx_YvOfEoHekKCA_T0PIznJhdi3YmQFBAX0WMj-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=GVRlKk8gohQ_ZFFIqethrl0KKVLdD0JvvDRiqxef2LcSx_UHf-tz2jEOuJvd6WWcdRjYU5CNeG818DmDfpDsxdaPtEFfwFZdon67P1sL1cgOy4g77Qauu9HSC5vij6-Xvv4hh1omoV96pE3WufeP56CBlQ0-fQCpWELVEA24faztaZrqtgFT0KrsiPoZxkL9iPtLuI9hUaud5vj-InFICcm0dKh8AAP80-0-DoeazVoWf7Wh8vigLnbY_DC0WRqEdPBSUIIO7ceA71NyvcrY184impSaX8sBcqUiJ6B86g_Vn1soWw42JrWTBtCXtmNJFy4DT0GMZZMxRAyIF5zZMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=GVRlKk8gohQ_ZFFIqethrl0KKVLdD0JvvDRiqxef2LcSx_UHf-tz2jEOuJvd6WWcdRjYU5CNeG818DmDfpDsxdaPtEFfwFZdon67P1sL1cgOy4g77Qauu9HSC5vij6-Xvv4hh1omoV96pE3WufeP56CBlQ0-fQCpWELVEA24faztaZrqtgFT0KrsiPoZxkL9iPtLuI9hUaud5vj-InFICcm0dKh8AAP80-0-DoeazVoWf7Wh8vigLnbY_DC0WRqEdPBSUIIO7ceA71NyvcrY184impSaX8sBcqUiJ6B86g_Vn1soWw42JrWTBtCXtmNJFy4DT0GMZZMxRAyIF5zZMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=EC8XrWl_zKrnRq73YuBcNNX1SdRirw36PzUqhloOLbM0I2iCRJokG2ptRcD9dK_2bRTR6O-F2r8_fEpTcQcCeTttmSdbjTmlQHVX1GDRwsQvYttTk9pHt8ZVCoLuBKftejUbc3_JxgeCWsCCA8zHQhJ-q41puAwPonRUcbWVknL8FYBtbXG1c1mk_lp31Eb4Tt37-9_TPq0xyF69uFHWLK-JhFlbaCDEfp2lF_UzUIMQhb_iaXL1ujtpxNMxQBSlkfUDjVS_xvj9ruEqTBUhhPsXEOEU7S5D7fGtBsd3kXyLBluZ0h0WSr5y5vGdpRn2w5zS_XRs7Qnf88wOwIsqeUPNFEvZbavU0udryVUzQc4G06ODZFqirlW08zwkkx1zSbLpfMkOKGBRGxF-C_pWf9_SuADlcjcJxTxw4s7RLVOx8G8J8M8NTOp0_Dqxz7-gF3CjdNDnTw1TlqWNg8yHmqPspAypyZ9UfZWCewEBd5UhulN8LZG4gOfRVyrySTMH1_-IZeNPvW4pd2mDZtd8BquncDNafaAbvAHB1yaeLABbOxCEtaAcCFdulm5BXdkmIW78H4zPGSTAbOSziwEm2usCtc4oEVQnYBJNcdjcd5JooynUQXqTqADNqF0DURvLH_BqVq2DPqUQwWMNNKmXvPdzsj8__5uoiQVc1tQEixc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=EC8XrWl_zKrnRq73YuBcNNX1SdRirw36PzUqhloOLbM0I2iCRJokG2ptRcD9dK_2bRTR6O-F2r8_fEpTcQcCeTttmSdbjTmlQHVX1GDRwsQvYttTk9pHt8ZVCoLuBKftejUbc3_JxgeCWsCCA8zHQhJ-q41puAwPonRUcbWVknL8FYBtbXG1c1mk_lp31Eb4Tt37-9_TPq0xyF69uFHWLK-JhFlbaCDEfp2lF_UzUIMQhb_iaXL1ujtpxNMxQBSlkfUDjVS_xvj9ruEqTBUhhPsXEOEU7S5D7fGtBsd3kXyLBluZ0h0WSr5y5vGdpRn2w5zS_XRs7Qnf88wOwIsqeUPNFEvZbavU0udryVUzQc4G06ODZFqirlW08zwkkx1zSbLpfMkOKGBRGxF-C_pWf9_SuADlcjcJxTxw4s7RLVOx8G8J8M8NTOp0_Dqxz7-gF3CjdNDnTw1TlqWNg8yHmqPspAypyZ9UfZWCewEBd5UhulN8LZG4gOfRVyrySTMH1_-IZeNPvW4pd2mDZtd8BquncDNafaAbvAHB1yaeLABbOxCEtaAcCFdulm5BXdkmIW78H4zPGSTAbOSziwEm2usCtc4oEVQnYBJNcdjcd5JooynUQXqTqADNqF0DURvLH_BqVq2DPqUQwWMNNKmXvPdzsj8__5uoiQVc1tQEixc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U27NGOtnO-HEiHsmQLBCZJS1aFNRvXMPMydYiaj5aXXAdFTbCkMSvyF6H-xjyj56uRJY1ZuX-az3rM3zLNNl_OjDBDqLfhpR9G6LbWkENZIeMsE-TkgN-jATngRjIfQJmTziS1Slje7Xzp0Afqd_N1eQXkZz74ISzpLyUiwPoVjgk_E23CGWlweTLR0eZ-m5BA46a2_y8b4aNbHKzNf4HSbzPkI81Pxo87BPSf9QIEgydlaDB0cay1kWTTuDsSbDOeeHz3V-jmMNCAT3B1Uy2ZXi23neQpmLJ34nXxch1_WANnlCJBYnzSUcO0ZefI0jtpa8xJFkNhpyJI5NARymcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtYUrkr4cl6Vo9Vlyl4aOccFABo4Y9Rmtvkt-4M0nyr7FZU6yJWE1UIvMKJb5NeRttTYFxERNr3PV_9W-gaVlI-7hCNMSRcgmy6RbAde9BQPcoHYaJ2YMRv60u4OI_YXoHEXBkV8gX9IjmRX5KF-k5ve_EU98JYjtJ3S1vLZ9W9n6A6omHoeNQyOJY-_M73yvRQsK7a4BesrEZSN1pILR5jHalTTGfd8NRURcL1qNUQzVhwOS6YjxYTTfsL5bCRPwM5kqTXHYWeWGBSjS6DJ99bGg8QSsMKirDM1GLr8RJaNSvonKhHu_5qUGnLajccW2uQ7FY4nWtUgAWfAV63d_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgL_KszgYPbXisXxRcoBV0KZIA20PCz91kmFKa-y4ePJY0NbZXUG9xJJYR663uK-8xmDqHmcjSO0j8gzYHM4VR03u9BqeY8nK8V2nnFUhvAJXNWJ7nRPGMwm-ch2J3CfXMyYxQKX4K5vQ7KhIPff4MOXArV27zHF13atBOTQ0s0mHnyfuK2FEe-4da3B1dh8jaYY7V56vYSZST-GLcOwX7h-QU1RKh_cOWojjqXY2C7afZAfsGhCzVh8Ix5ZSnHbzJ5wB8BMuHi3tPLmdxWKTXUVVFvIKR7ThIraecT3LAPUPRBkqnEPHluyhWKD9IM9_8chGb_I3PqicT3BFZe4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
