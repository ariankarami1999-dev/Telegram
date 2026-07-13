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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 15:05:09</div>
<hr>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD0muKxU0borg_9FS17lI2uS3pFJOmdZgTUXKOH4mgL5D1JKPW7LGGs7XfOhpMtI-BLUbVARHuzkYAkTg4CzTjgBW-5x-rSN4zDlUVDUgZiI2Ql1iSYgKay_dPS6LltmSMBniJQ_Tz1ZIjnhG6eNRDALVFD-MUlRSrlvRhM_qb-3cYff-jjF1tvDNtoSwlDBB5d5BIoW3eQeVm9s82l60cmdPU6-4Gh-3a7Ne46hWDDhdjLURqcGEhxoAE1BGCRLC0sk7gTAc_mJBEerbJou-nxKaoUICqsWiBJeZ2yW7hkD7njAlP8KSzKe5HoRkqKzFm8NeoXEQTc--ZpQI-dDww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3mKooXnbv9QGxvWH4TEwZGDy-2LC4GV6hC_ypGAo_ABT932oKlz0rrdxv_fOqFIIdFfjYaLmWbVNWV4prjauXQpbyZhUIbjbZH8oXCtWSBCwyPO4Tds-qL9HU5f5h7vSw387i95c5j6HbIP5-kAAGcm1554GbBpYCrapQWQgpVvKLkc9_Pd7hsfE_T2kiA649wRYbefau3UTtfJBvbyfLvBdOfJbTz9li4oBUsHR20u39zGUUKGfB9kMM4KkaM0OPsrUz1Z65S-FNCByrrtHLSGmzaXQbAGdG9Ap3eoglGtM7jyuNEdmbkhkBTmjxteHFq1xVaJa6Sf-9YzMQAG-VfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3mKooXnbv9QGxvWH4TEwZGDy-2LC4GV6hC_ypGAo_ABT932oKlz0rrdxv_fOqFIIdFfjYaLmWbVNWV4prjauXQpbyZhUIbjbZH8oXCtWSBCwyPO4Tds-qL9HU5f5h7vSw387i95c5j6HbIP5-kAAGcm1554GbBpYCrapQWQgpVvKLkc9_Pd7hsfE_T2kiA649wRYbefau3UTtfJBvbyfLvBdOfJbTz9li4oBUsHR20u39zGUUKGfB9kMM4KkaM0OPsrUz1Z65S-FNCByrrtHLSGmzaXQbAGdG9Ap3eoglGtM7jyuNEdmbkhkBTmjxteHFq1xVaJa6Sf-9YzMQAG-VfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=NCLRBwhZlKLI_fQ-f4Yfqh7BkRbyhbkngqZLsXttCSlu4vr0mN2J2w4z-8sRd5yJs1UFGXENFAt2ooxUo1U5G7DJwA7viHlajx-SCeidNvlE6E0gRPcmgXwgDt2ClOtWhDkPsbNV1UcoB4WuYLgnKB5R0z60FLZSXYYuGWFf8yRhhVUsPwyVoyti0C-rWrWL89chHYRHS_4Xf2vb3efku_3PUF0f_tLdCoHDwQ9t_IbLVewkCzyedgIjq_skeW9YWGZtNo4a0DWSVHhRBfW8YHUVG_VEBo1xkahA8E5SsEPLLTT4Be_vF-vwAyWT2i8LKTRIKeFt9fzEF7LW0yYC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=NCLRBwhZlKLI_fQ-f4Yfqh7BkRbyhbkngqZLsXttCSlu4vr0mN2J2w4z-8sRd5yJs1UFGXENFAt2ooxUo1U5G7DJwA7viHlajx-SCeidNvlE6E0gRPcmgXwgDt2ClOtWhDkPsbNV1UcoB4WuYLgnKB5R0z60FLZSXYYuGWFf8yRhhVUsPwyVoyti0C-rWrWL89chHYRHS_4Xf2vb3efku_3PUF0f_tLdCoHDwQ9t_IbLVewkCzyedgIjq_skeW9YWGZtNo4a0DWSVHhRBfW8YHUVG_VEBo1xkahA8E5SsEPLLTT4Be_vF-vwAyWT2i8LKTRIKeFt9fzEF7LW0yYC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=hXJyW0voCcIHYGHIXA2kZpImc4L39cxxn2xaxQCz4Eq4Re-9Zu4qShCxI1xpPJHKAbW9LFZERxNJPE-2bz0FxCT-bfdjmrWiBUQ14ZIFp_TiBXU0b3YfDFnNlfZLcuVy26crvHBbPw3os4tXpLplsjyY3kTeMnEPVMfEsJW1k1i8wU7hjgkG_2nP3ZuJBrJOIgAP3wSpBVDctqO1aKJo4eVkfkfnneoGHrJDBr6PvbS-AbmjbgtN9wCUaEnrvFZIrszsHLZ4lQaGgImsuUbXwhXC3C_BVC5INFUjRv0DYHRQpclSOqKYHcbL8ZecAvwCQo8kQVWeyJQc78Zn9xJoyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=hXJyW0voCcIHYGHIXA2kZpImc4L39cxxn2xaxQCz4Eq4Re-9Zu4qShCxI1xpPJHKAbW9LFZERxNJPE-2bz0FxCT-bfdjmrWiBUQ14ZIFp_TiBXU0b3YfDFnNlfZLcuVy26crvHBbPw3os4tXpLplsjyY3kTeMnEPVMfEsJW1k1i8wU7hjgkG_2nP3ZuJBrJOIgAP3wSpBVDctqO1aKJo4eVkfkfnneoGHrJDBr6PvbS-AbmjbgtN9wCUaEnrvFZIrszsHLZ4lQaGgImsuUbXwhXC3C_BVC5INFUjRv0DYHRQpclSOqKYHcbL8ZecAvwCQo8kQVWeyJQc78Zn9xJoyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=M66buIgxHRfuAZz-PV3cBXnktohN_lFSNVURIFWhyNx0oN64F4vuSAT6osYH1M6-cytSuv9Y0dSJqR3xCzgm70JSmBLwb6vXSXPhZhmo-l22gGTQwgHlC34W_06FjZnO-iGZu5MmNWiWyp6EMW31INaSuyKgaHR9zq2s7rxRIvj9lBawEDA3wbQukdH2KEusn8W8ZMWPBAhxK5LfFcPgBnjJGmO-uEkmm5Dda9dXIt-BuXAY1XydKKE94lrMEZU-6PoBf1-VZDV3BqoePnxtTFSkLkg1aLDJo-FHcBtcCDDcMUI8S9zlR7CSD7oCJ6tKwSSum5v_3rGryYqwjjnbmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=M66buIgxHRfuAZz-PV3cBXnktohN_lFSNVURIFWhyNx0oN64F4vuSAT6osYH1M6-cytSuv9Y0dSJqR3xCzgm70JSmBLwb6vXSXPhZhmo-l22gGTQwgHlC34W_06FjZnO-iGZu5MmNWiWyp6EMW31INaSuyKgaHR9zq2s7rxRIvj9lBawEDA3wbQukdH2KEusn8W8ZMWPBAhxK5LfFcPgBnjJGmO-uEkmm5Dda9dXIt-BuXAY1XydKKE94lrMEZU-6PoBf1-VZDV3BqoePnxtTFSkLkg1aLDJo-FHcBtcCDDcMUI8S9zlR7CSD7oCJ6tKwSSum5v_3rGryYqwjjnbmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=qFpYyyGPRNHrt3NDdZPuko8_Bo0LvNOF4hOFhH2d5upmQHGHYy19-_zTK-huU7jDRakzQpI36ZP6Da1u4Nk0wt_Ukx7NUdeNnZvt3X7g9eoNuq1l7Xc9TIIR_vd98CSt0YIk-p5qd-G5_3BNuoNq1xe-smgxBHVtRklJ6K8q1gsAfVV1l9MGmss2hVAJ0JXUripZmzpNrXfdUsgC020uMP3dTXftDmyyXApbdkfwV89_a1PqERv9hCFINnbCLFnOlXZ2tTSKCOOPnlkYsA3ZNpOChe36W2CUY71GCBsUavRJtgNGuN2CyxxhOB9T9lTNx0muEX5-2BcpQPGJ4HTyZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=qFpYyyGPRNHrt3NDdZPuko8_Bo0LvNOF4hOFhH2d5upmQHGHYy19-_zTK-huU7jDRakzQpI36ZP6Da1u4Nk0wt_Ukx7NUdeNnZvt3X7g9eoNuq1l7Xc9TIIR_vd98CSt0YIk-p5qd-G5_3BNuoNq1xe-smgxBHVtRklJ6K8q1gsAfVV1l9MGmss2hVAJ0JXUripZmzpNrXfdUsgC020uMP3dTXftDmyyXApbdkfwV89_a1PqERv9hCFINnbCLFnOlXZ2tTSKCOOPnlkYsA3ZNpOChe36W2CUY71GCBsUavRJtgNGuN2CyxxhOB9T9lTNx0muEX5-2BcpQPGJ4HTyZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H96Cylua4WSBm4lBT13xREJimfg3cRtT9ijJRN-QqJgwBgdrpXxKL6pFEYeYKlusU3G3j7TWGtOZS8IVHyxmjHSlU9IBEgTsAf7oxG-5syrClWWMLP8FLTXzeFoa47Q6c0EJGDJDUApE_XYa4MovOtRTh-DBwP8zExW83iTxg0rSNSz9Z4hYHcgPy-2o1yau1UL32N773jC-rKGxOWXcOcCalI-hR4lzfe0CLDYtfP2eTJvbtGGRGJgfQ-GJAueUUHltKP5kJqhIV69OrzA60BH0CTCiln-brGwAsxI-uOozp8Vh-bNkXaYnXbQ6ogJkfFTdIpRdJYpMvGjQNW1UiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf4-LB8Y5bsN3LBqYKK3_PbcTeLiUclKCV3XivvZE9sdLb-1U0oyMpHAAMmXAZG5U6cpEbFMhWvTgA5p7d_CahF4s1alVi3PKWeClJEN-LlGRPMe_M0po0thqigF03-apIBrzxS8RKyzbiU-zeSd4VRmUAxfAIVjzqER7jsvCTPWngKHEgo2HzJuFEf91MCnTjv0W6fur7oV_YnJJ4sBeRtkdRwD6XfAT7iq4vF1lwt5A-DQRey4jF0sAzGj-_h5ilKImYntur5Uw9LXL_oGvfd4x_Qi60BGc8qp6nFXZNcEB6GRkpYqv0Z1BYDUr9yhEdg4WnvmwIWni6PotGA4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=YZLOrw_HRr89ZAzCut7tIEnwFmHpapY-KS7dKf3IuxN9I3R0DiDPgPjR52gv_pzm43EuI7o14eRo8SOUdkLHaYPhd9mvQ2Sawyp3Kz-ozYROYJ2mHoTXaDRM4xbpoalYH3N4RTM2UwHxxKJUZwyfPW6yiuVM2Sq4D-OmAegqOvnz2HZkx3LXQehSG8CnffPBI25TM5NdWaDPFdX1FCt5i5M5OPR1nAkpPbdNn3zh5X6RrJ2GGxKPz6zPBnpGNpnxdwOS0rjqQaniDpeIzkp6J3Mls1qraqhtpk4_XaWlZZmT7eZeu9NMQBMgRaPrEevym5VkSmMQMpVJFPpDvga3Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=YZLOrw_HRr89ZAzCut7tIEnwFmHpapY-KS7dKf3IuxN9I3R0DiDPgPjR52gv_pzm43EuI7o14eRo8SOUdkLHaYPhd9mvQ2Sawyp3Kz-ozYROYJ2mHoTXaDRM4xbpoalYH3N4RTM2UwHxxKJUZwyfPW6yiuVM2Sq4D-OmAegqOvnz2HZkx3LXQehSG8CnffPBI25TM5NdWaDPFdX1FCt5i5M5OPR1nAkpPbdNn3zh5X6RrJ2GGxKPz6zPBnpGNpnxdwOS0rjqQaniDpeIzkp6J3Mls1qraqhtpk4_XaWlZZmT7eZeu9NMQBMgRaPrEevym5VkSmMQMpVJFPpDvga3Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=SBc6Gq82EWZkYWHgjF-C4x3C8MglaSzRpRi8Rdok8thkM0jjTISQ5BKBGxzUwrX8j7vVygyVcJ0Twg9wUhCktQXAxuNq62PRqcof4o2t06L80hemOtrQsuKuLptvJZpdv16Q-nc4YSbTVQWQc3xIdujM3ku22Bybn3w4sWMNPRZCpmiLbbdbT5C9l0XNdKkxomWsw6MlZs9JWLavJVxDYzVLX5at1AqLXA0bPbgSNC00M3XRZk9pAsZOpgG19ht1W6Y2njw5cRx5FkoBhfj8kauUW9MB1IgjxB4yHP3GhBOoQ3CeyuvOWWSfcGuO86Cs_H9UqFtAJomTmoIcxoNRRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=SBc6Gq82EWZkYWHgjF-C4x3C8MglaSzRpRi8Rdok8thkM0jjTISQ5BKBGxzUwrX8j7vVygyVcJ0Twg9wUhCktQXAxuNq62PRqcof4o2t06L80hemOtrQsuKuLptvJZpdv16Q-nc4YSbTVQWQc3xIdujM3ku22Bybn3w4sWMNPRZCpmiLbbdbT5C9l0XNdKkxomWsw6MlZs9JWLavJVxDYzVLX5at1AqLXA0bPbgSNC00M3XRZk9pAsZOpgG19ht1W6Y2njw5cRx5FkoBhfj8kauUW9MB1IgjxB4yHP3GhBOoQ3CeyuvOWWSfcGuO86Cs_H9UqFtAJomTmoIcxoNRRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8fDc-xONqpMsZeSiOCbbdlI2szLyfUfQh2BaaDu62OYMShzomJwO8hzP4n6c6cc2ieUlpUKRSRcXkg5nBVUhUfbEztyvkI5Bii_RulqOnDBx1p6Zmbh9d4mJsNLSrnpYTr5zINxtwkaaOXraDjBmsuK0JjpSj1r29Lq_Zr6Tq8eKGGYvC-RzUo6rlL--I_6FAdwIEdXcopYhR5cpkHVi9tWlIyth6L9v-QSMFADXTwgTBCx5srB12xj0-4RSycULnU92miFvP8asj40hsEPUSQpddoWGNEP9r5Esz3ddULkB8SaSb9Qzg0tYmz9yaKVyMWPzychjM5ruzl6uzSQrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giGHF4JygIsYGGf8tx2De2YD8plnPWEFghhNd1KBidYRRNJr9XWlYFmPESwccbgLnbFh5SAhaC0o7eNRTc9evKaUTFSpCR7UdwsWK_6Qp29zjf_j5ZZTuktbgw79z3dQonZzXELBVmphUBZYTqlMjvU_O9KaHtWxed1jJB4ygVNrLghBq6nukoTqFqf9YMKmrT5DVzZjC5Z43kmyHGE_c2ZiqkgEOy1Y0VlN0_1jhAiWTy5r_jJV3O7ottLNuB2QPcmqnnwyo9ySnldQ-Vpio9eAM0CmsKAVtZ164pJv-8h4nj555nLpPUo5A8RDwL7xHs-zr-82Q8RtVK48s1SuDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M00xypaXL-EbqZItwNrsTTRgMPfuFEDfO9T1Vp6yVUcf3taaU9t5HPBGnTqpneNJ36LkAm0DCjCiHId8HJuKQaT9g_fXsBIBNmzbpx4Y4HhQG5R3ae6EqoF6AvrZCZwJRrZsHlYcjHS5_SMosJc7Y1mh8PBwqGWQHO332a0-rEJXbv89s4Q_PhtbvLP0T7KEFiCBFa2PUmVibc_-QLh7u-8B0DwS-YQyF9PhvvkLQ-ETc8V4F3b6DFcw_rxCqeJ1WQDEKCmGqatlzMKiVqvnQBdkSP02dg_VTKrytiBwpDYsXQrgv2QYbQwBoTCyiL0yUFlFQsv28J0eGfszqZwT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1LJntRE0imF6Dbu1gXh53LZ-jvl6GNML27-LT0E9ioLMxwClRyV0Wh5oGPrRdty7SawFjeDzq8IKP8UzbSUhQStEZH7Vw6tbCZzy3z2d6TB9DmQJVCEkOFHh8CoQSeR_maumC9uIPyb55yQ7RoXW7q7AP-bqQWGg21JETaue2slQbIkoygsHb8gNiXxNhIItrfOe2jLRkbKeltheyLEGyOvJd2yRsrZw2RagIOxGm5gjk9qPLn-PB8kGhI6fL32wFpV9xqXkj_qwznOZmlwEd-9ALVroL66WAmbB2YVRGAu8ZtPWPWjjHRQVT0V6f2OlyUzp3risk85shhXedWDsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZGCgmdxRlMR_knywyUhp5_WQLO_-KGG5nI0MOrGkLoeIjOgTPK5KDJixYMsh2PNh0_cgwgc8IqKx9zeNzjHl7mMIXtWaluqVJmYkmjh_n0nZFwT7p2X2p738YvisoQ_l7THixpWAo8Flf73HwgSiD1ke6W2YzM-4RSjoYRQugpGnNk8HOXuFSQQtL8jhslFRlZOuIFc53zZ1vr9yO6xxFBz6_6rLC39Dpv0uAAg6vivId7P8Ap_haT-Bgt2y0QDxKFWi-q1a_G8Ge7WE0KXivgBIu50J5x6NRBfQqbf31Xb-O-sxjsADTUV6Yq-KUFBoOfTnHdrMo-wjHYS1hRR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C0oAGgHL2JgnvIFJCTv2m2Dr7L62X4g2hipMNjUMvGfiXJpiQ8K-t356TfQj7P6NNE2DYte3_J3g6qc91L1oLJHFbzQKuK_V0sc8nL-NHJIeP36ogXyfuvBx-zBpjA72Uad3UO9aw9yWEKlzCgSc9GMti3bQSxN1I46uOHiHAw-fHQRhpb55XZyjFOOzVrsNcFXv7hgBJnz3j7Vjyc1g-OaKt6ezXJAr4kMFOPGP4oTupwcKFQkbViPbowD13ZVb7pXjVk4nMwKaeVQt1VPnqO6NbfHdoHEk7ldrnUPL9sBqxpwT9RzX3bLT-QkKCgcRtQhlwpASDgBa4dOicptDLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWXOt5Zlma0uyfnJG868eIxM2hFcSsNV_GIpkw49uvdW1DtYQ95NdXG_Jb_Xi-BmqJN1LiTJxKukmVom1HZ-9h0CuMenKepQv3vSwf7RyrWwxELftSaF7TEBUrVBQ21qGDsaabEv59w9seuw4m1-oJv-8nwYfG4NpbcGP1D2bczNWuAvlDSpjkgQFLruQ1htvOichtE20Y6gxB9_ncjG1GijY5jvqMA7VU-tHfTo3WIzwADAQgc83bbL2uZeb0OBOG2uBe4IKpFPztcHJgR5ni_oPi8ojZrA5UiHp9_LAeGH3yn4FHAcr5-7bx70fQ4hi0COq1lUFSFBf6rDVsjFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzZX7fwJnL6KQvhjJtjZq24jHReeC827ZRwMsy8Eng6wTdhxYhCm76I3HdQBju8jzKfkpwUGfEUQXgDVvMkA3FskHjGXPgqK6Lgr0Knu2nXaxKHoQEpHUbWQ4B6NHfoGa-5ag2IV0SKX5E0jnc3T1RUolhvtJf9vyoUG_b01WYDmtMU3jCvBFzQvrHl_gt4E-WJNlVvOzast3k3KMJQMJHcA5AfFEQXbp6wrS2Kl3gyN-hZMH9eTkkQ8z3fjhYpLmeIwJwzuP0Ksc4ggHzyg03-xC01qOzFOMROjLZp5TAvkgandBEqcohhAuaRLWu_GQcLkxMI5LU6nb4W9woch9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT5cAkafg4jTV8GH_K1liGqc3nCb5op1oAuBs9kKnlmU3NusojD5vUrFHfbsM3ozY5L_U0Pq6oQzH_9y4snTzXrIPRAyt07mqN5wVOkHnKdwlGHiTg_phQgvbAS6wV7br4bmgwu9K490XSXTVVt35Dop0lMMoaYpwkwwu4VgAIGk0MCJZLYYhxFhPmnO7bf1rR-slkhhTxHr4yJ10KlwTOxgfMOlPpLJnLwoOCvmeqeZmaf0Um2KPpVtpAg34XH9g2hZjFCTFvP4jT7RZC_lAIPFBhcFlXErEYZJguatapNj4U33OCidNDS8f8SKgScZXqQcOt3w3X3CdTmuNntdVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnCM4awXi5eaKqPJRDo1_EhGSeAk-lzNgKCsYF5SN7K-lh-51gbK0lWkCbIBYxBTBc2xXgvNVKMt2Yma6kE9XMHceSiVf9-uHGIZBZgE_KwVO0b6g5ouZmwMxyeP1JCcSoGkIMIZW_rnEjAeRwwYIjGXrxpNyGyyeaSCTl3bDayXexHuq4m5LSUaDy3D21tWPPmSBRaDP4fLDIu16m19G-rSUqQVJ91rdFyBUgYB6zHrEQt3Phy_0oXKmDDS51VSZRNCYKoDXsUBQy3thuYY0BR_JLfd3oc7905PZoHx4VsK5EgTOhnx4YOdZYrRaP_iAFGtnLd7Kcl2PiatoEaaPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXjnCVhLJpcSFKPqX_0OmF-XuuXHQFDgj8RT721yf9GBEezuGd2TkbvjPSJQbL7_k-KK6OfmsIys0coZJBaX57eYyYGc6SuUPF-uQBQ3SJHxiNSe-Rco-ndTHUwXHtZLanEWt0zENqO2XeZNJrBgB_xKfo_0h6Brwx5loE1CdLirgmtSJzM7SjhWpsWVwG-X7glGBNyQa4BnOCOhjRfLmLw1sj4vhpvV8OdVUPMSQLRIwMU6CUDT6kyS6ljnwaAHHt5Qpxi1TliUkkuK04wg9CkpwV9S5UDQYoRcId2yKSlBSgRKOyVXSMD0iHym9-40GDQPRt_tRYDGk2d4bDzXYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=t4wxrQ55tUNNrMwRhoafj6ya3FIxB4CkJcwNacdaY8hNwJ7r_KZDW0fYdXOdAkyqnKOymRZ2HcWKL9U_UX53L8cimDlw2kkisc6uOnJ_b8wOyIg8J5JQP8w4QmT-N7VLSU_MC6Vbsgw95Gr5E4JAYh9oWVc42TBut6fCB-6rtdtUf7pwFgZsik_U6n6aRwfd1mZRYnq-Xu-vTPW-HJUXhDcYIk_LYsirOk8mJfIuboBDRQ61cqMKi2UMCgqUvVIvdYoSRwyqxk0QpIMaudGT0FEh5anFE-htdeJZp3I6AbnTKGsTLt1Kc_YuvDdVedFDF1IA7ocSdBC1UcoIfxDAMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=t4wxrQ55tUNNrMwRhoafj6ya3FIxB4CkJcwNacdaY8hNwJ7r_KZDW0fYdXOdAkyqnKOymRZ2HcWKL9U_UX53L8cimDlw2kkisc6uOnJ_b8wOyIg8J5JQP8w4QmT-N7VLSU_MC6Vbsgw95Gr5E4JAYh9oWVc42TBut6fCB-6rtdtUf7pwFgZsik_U6n6aRwfd1mZRYnq-Xu-vTPW-HJUXhDcYIk_LYsirOk8mJfIuboBDRQ61cqMKi2UMCgqUvVIvdYoSRwyqxk0QpIMaudGT0FEh5anFE-htdeJZp3I6AbnTKGsTLt1Kc_YuvDdVedFDF1IA7ocSdBC1UcoIfxDAMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdSC5V7cmvZ9rjgEu_tsJvLTesJnR6Wr_GD3ZoLPd9s6eMKG17DML0db2zvIX6bQAzBONaCbE3MGXD-6dtFMCGbtFTrzujw_-_xhtXGEn2DevrP5a88WQE8jWMbZRR138RZ453sChTdlyIhiRWM-zElTGr8p_aCKi45ruZOwTWIfQ2qY1xpAmxTZGLhR_mF9Ms2SOS6iFNyLs1sPib4uaFgyEW5NDSdyCQKwYxTlLfNois0oqabLyyw3ZSVYfcsQdHGdV7I6DgAKEthYzpDJF1vrr04jfqS_xPqjMzcNrLwqlPAoZL4ft-L-hKDk-SSSSgm7GkYVY8a8x41EytSeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=afPDXK_z6jeR_TdW6O2bZqUtXo4VDIwfepMF9Nwn_B-2tWYjj5G5dN6fFZjHTkmfmxJjAb32sbAnQYGCw00nNYuEoDRINe05JwtTNTDBbK19zh-9Z2rqWvOD-S0uqlhmiHGVOyN2EoMwsOSimTZUX-fyBCW3mrZjEPzYvtLWlUE-8OwiHK6z5NayLKP5Loy6A1wYVRwvQW259UBP5hr7WkOnDDejDJ7vHPyQVZdvfH68Qvtl_Ssq_BlE68WuXxMTBm67_SzNdyIeTH35TW8TUPrkbni53RwFSWHcGdjhxIybUg0JCMWvKNvjlWZHl6cKUWYk_bh603dIMv0SDOiqRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=afPDXK_z6jeR_TdW6O2bZqUtXo4VDIwfepMF9Nwn_B-2tWYjj5G5dN6fFZjHTkmfmxJjAb32sbAnQYGCw00nNYuEoDRINe05JwtTNTDBbK19zh-9Z2rqWvOD-S0uqlhmiHGVOyN2EoMwsOSimTZUX-fyBCW3mrZjEPzYvtLWlUE-8OwiHK6z5NayLKP5Loy6A1wYVRwvQW259UBP5hr7WkOnDDejDJ7vHPyQVZdvfH68Qvtl_Ssq_BlE68WuXxMTBm67_SzNdyIeTH35TW8TUPrkbni53RwFSWHcGdjhxIybUg0JCMWvKNvjlWZHl6cKUWYk_bh603dIMv0SDOiqRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCKJO6T4Z-Q8HQfrLaBHBDkwLXXJCoPBpVVgrg8M6OHSy3Km3EUMFp-2q7VcwIkkprR4M5BhIpkNxgNaUbg4m8g4Ab3gz6-5PCdR43O5kB607RlcKXOABfplI582OrZu3g4DBptP0fsdEC6OlQByzjnopSnxNMWQQKiu0dMI1cYyzJrPAReZ2N5Rg9IeM33tnxWj1WTclDfg4vKRPfkyG5tPLK6NpXJYIMXmSw8As1e76YsfBPijhcFWTuPpbcrAtpbZ6I_HremjtcitWSoRwobmPb0Zm2Y0iEl4vD4YxPqJBgq0rs8Zt2hsLVzOhgxR5u9fbcw-pA-QTi44d1ZUqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaNwzzxTaTkE5OWXgXsR7UoQqThPrQfsvQU7iMusFQlMHOGNg0akznqMBzVZUli6zFSlUMkAh8hrzZumKboZIVLu1ficA72lVCBxxDtEDh1Z6EBHh9lmbTY33o7pT3SUvRSc-JGSI2rgMj3C4rZ5Yn7eQa4_BawFAPvSNTm-fc9-oMcGgUeYGXlsESOf7MaEYwjlbILfu_yTsjmXPkpfFs2uddv1hTefKCTyvy3jgHDG3eqzDbCfTbyhD9az0c43nw5ZxiTS5OXGMxfs3B0f_wuZj19CXU4ZFPIA-KMC111u9XhLuB6YOVUENEZVdzIn6EUs744rmf7ertzzrWxEOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=X2iSYPmOk8PDkkmNaI_g49rUltIYPvD5LII1XDvgkEVWGM44z-qjh6Owqw_F2q6P0OMB4w_M-gqeAccueFKlFUQLXSGH1IBKWGB-Agoyau2DD1wL0UzwenulqgF2jRDueLcU89sb6Qf3bxVrL14rH0Uh8tU1EXR4D0QMNOu0I1sAjYihjZ0b3i1y2oQ68-pufH7H-l47WGVy0qlNSdB5tuVeLMIo6TFwmnj-QLyz-3aKvFHXtTDihRT7z3iXGfFMup2TEFDFWO7Af4VSbmW2rNz4sy7EYTRnALBuwfLouTewg-WLz4bOF_5ZMZdkR8jwHOKdnkgTJxPphIMF1YHqh20YIURWtrdsLxkUzKN9d54jhGOQxB9SY37X22McrfWXvxP6AhrldVYJQQcFolRRMj9SU7HsB8kde5o_5TrQR_XBbS0USFupSElFEidPhj2xvLlymWUwiVo5JnGz1_xZ6LLLPr859FouIsDO8ARvEuqSQyxp6s8WrLxcvcJDZa8EbddEouPLBUX4V6ArXrVxucaXMYNc8pI0cMmGpvsQE4IlV5OGopdBnzRVkopVfgXg-hfptaPrB1RG2jwCxKl9q5z8p-1hgXnExeLWH-XHl5GS6-WVwGl8JpdimLu5xnwhvCaTbM62nGx89qU_AshHXUYuHTMf6ePBKOYZ5XyXrxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=X2iSYPmOk8PDkkmNaI_g49rUltIYPvD5LII1XDvgkEVWGM44z-qjh6Owqw_F2q6P0OMB4w_M-gqeAccueFKlFUQLXSGH1IBKWGB-Agoyau2DD1wL0UzwenulqgF2jRDueLcU89sb6Qf3bxVrL14rH0Uh8tU1EXR4D0QMNOu0I1sAjYihjZ0b3i1y2oQ68-pufH7H-l47WGVy0qlNSdB5tuVeLMIo6TFwmnj-QLyz-3aKvFHXtTDihRT7z3iXGfFMup2TEFDFWO7Af4VSbmW2rNz4sy7EYTRnALBuwfLouTewg-WLz4bOF_5ZMZdkR8jwHOKdnkgTJxPphIMF1YHqh20YIURWtrdsLxkUzKN9d54jhGOQxB9SY37X22McrfWXvxP6AhrldVYJQQcFolRRMj9SU7HsB8kde5o_5TrQR_XBbS0USFupSElFEidPhj2xvLlymWUwiVo5JnGz1_xZ6LLLPr859FouIsDO8ARvEuqSQyxp6s8WrLxcvcJDZa8EbddEouPLBUX4V6ArXrVxucaXMYNc8pI0cMmGpvsQE4IlV5OGopdBnzRVkopVfgXg-hfptaPrB1RG2jwCxKl9q5z8p-1hgXnExeLWH-XHl5GS6-WVwGl8JpdimLu5xnwhvCaTbM62nGx89qU_AshHXUYuHTMf6ePBKOYZ5XyXrxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVKms14PHYToch18dG7AcmvIX62TDOBqXyxyB_L-LoZ2wpXrWNF3DR5nxpWBUN6JJDlnDGjaEtkKP_fRHQekvk_sK_EBCrVrRiRiVIK46hAYMWpONvDiTsyhiKeQsJui7muiaRpEyEkc0jfUy2xaC4_86Dj96Hge7P5l-B-kK-p425SRjBgEgaKBU8CnOtLw7c8tBundSd_xcZAfXNxt_vyitC_MxZ7HCQUQyBQn30htx1IAtL97caqxtZrfTY7HnO6vREFxqNvZMzDAPEa9rG50VBkRYbfNgZZRpmI3oc7uCGr-y4GpW_smp76OXepwUXf9CNFl2kv2qoyWJmIvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPYWX13pefbJQC9Fl29dK9cqnwSXwCcQSUQCz7lE06ogifHKHx0G3tihSFdaYLvpJ5dBgplwcovK_YDaNCFzJvZ-VMyg7OG2cyQY6RGXjFN1hYqS7JbYr4TYzsYF6vf5p_7w2A9texPmjOsX7Nem5is7bbsHdxZPQXhx_ZWIno-cSMv6vxT4yhSLbmEbq1IbUIb2KnfYw5ui-MT7AlplF5OQjAPWl1_dC7UB-TRZlpp6BzprGqI7d-pMRIAfv9fvJsKeM-cVIaHTJvgTLnRnyiNNX7hwr6TTCo6ku74MVFRaFo_fRof58hNqpY1Rnt7SkqxsVgivPYBImlEq4xtj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP_9TusY-i653lR9aMzo-laE7ZJBoF0IEkThxwt3Mnx0Ww2p2vJqp2i8h154JVMpzl-ptvVCSymC0IYfcTO62Mi7Got_5i1nNsiqNSbBE_42JB-Oba9WE5SrBOJauwdemNgmSJxcEr35AJRY1i-5MVagXdVl8cH-KlUnCgSLLJvnVDvpxuH8ltnyN16pFAwPdy9iR2qYSZl-YNsch3aPbWMmDqo9klAb3sPQKnUuzWNz2qiqUBRdSDt92FyKYna6wObu8tUHeeM1NB8XBWcp4_3z4L9hS8dGNJEs0k0CiKxzIkLk8yPb6YyWdSRbRr8PMFmkrDor2UniC0QaXFSlgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=SDnLxYrYllCgIFz9HGPr9BFCo3EmTa15EHuhHYKHW4a_1CDQ2SWwRXoedr3p_FFW-NkIYqU9pbZKbtFfS5-2nIsB9HjHhYoxhPvqM3lw7xsXg9OFC-p_vWwzO1NwI0fnP9Qw6RGLSnWf5I5_gxQ81LpRQ-LK8Cq5WN8U1V9nCpfQiSJTAkni1TZ73D0Wdhl60PeGEn1JBXT1F4i6vTqg40ma6qX9aCXuD1YZ1TcfX-pAmNxmrTFuq1GojHX7bbB7xMj-voCo8JGR_xqixSnKt4ZlL0S53zVNRB2K6PQkWlYiOjAW-aE_nvR8mr90-KCzLyN8Pfj6cxyZuM7vSYAZ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=SDnLxYrYllCgIFz9HGPr9BFCo3EmTa15EHuhHYKHW4a_1CDQ2SWwRXoedr3p_FFW-NkIYqU9pbZKbtFfS5-2nIsB9HjHhYoxhPvqM3lw7xsXg9OFC-p_vWwzO1NwI0fnP9Qw6RGLSnWf5I5_gxQ81LpRQ-LK8Cq5WN8U1V9nCpfQiSJTAkni1TZ73D0Wdhl60PeGEn1JBXT1F4i6vTqg40ma6qX9aCXuD1YZ1TcfX-pAmNxmrTFuq1GojHX7bbB7xMj-voCo8JGR_xqixSnKt4ZlL0S53zVNRB2K6PQkWlYiOjAW-aE_nvR8mr90-KCzLyN8Pfj6cxyZuM7vSYAZ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt3xQgRJTpfSBT_NTD7kj0GuUYDa3c34slT1_SE_4pkgnLkXB9uBU3OzjtVtYGMs1WerzSbMk2DsZqsnlLUIjvF3WmuSZ7puWU8LHL5K8kDIT9FL3mhZOKQ9tcdcYFFVRXXkYve9iT4L3IHUDmjPLjTGYXSn0PPCgC0oo789VfSf1sTiWDX7gV1n642kLFwdJcH0Yp5sZoTBoQyWE7iPq_PUDg9yQOeNW5Y_AvNhuDinsnvcXZdURec8vtsa3aokmzx4QfBdYlw5lbLqzRd-5uJIkY40IQ05nxRLH26-9Te8TYPu3mnABXH8kv26VNQX8sWDw4_aUwoVlSbG17GXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3g1699thgGGGdDWEhMI5jyMjDll-51OArFs4SKvw53oOc_VQCL07fJgS-iyMxEIzSGhZz8s9PJ71k4NPGtbh9MziPH5rRSV4p4BWbLTUWIgLFqQJbyWX7zOrB73c_qR4-aDukn62qBcht5cPpjC_HMMQOI-O6RZITh0gQEXRrWB0Q-RbOeJ6MWjgh7lgJWftPXD4KcnuvQoJVC1WeNU0ZTWu7GQSCMlER0Zi_YQzMfqQs7DaY3HwXaaTTshL1RxZJqhUzRqXSnlF3ExiwQ7B2QN8EXpY3ApYNxP6efEKs7xMybhE9gFORJ0CREzqr2LcfyfJKPQDTLRNbKsOXm-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ae98ifLkbrkOKd5RfuJglIwqr0JBzDcVsWzermyIAXKxRK9xX0rETRInBe7ZZsOlyUbc4gyKYC8HZaevXVvxrHIe2iUpP1lviu6udGUp3bGVp6_aFZZ2G8k_nqoQITnK5yGYo9_42gEvlcpGcQWb7ZAVg6SWZyrQF59UmQitu90YxpZwTBaezSiD6qB1-oFxAidh-Ip6ckP1_oKozR_J8VnWSU6dWzQlL5yZGgCC98UZySullR2fNJkCD1MgOBWgi1Fryen0-_SW_LC_QedtLH3sU6H_MSupfTlFUM0En4AZnEso0Slk1F22S07SdQ0E5QmO1fzPb1-rP9kDbNJjhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHMVAab41r9B6QfLAefbJT6qSilPcSQHd1GEINV_j-R31VPn0ym905vaE4b-VIvAdFiJClIk8LmU9_ks_ZFT0p_LJAYQf_l2cTC51FCiYqWpSzQHHehfmB6Y4TB8AAIKZ8-ypBDFP6ECaRyj5-qBtcmbO3FyjfsPuu8SS8HeHDCz43AE9IssKh8Bvhgx-LnrvtqcKvsdxQ2icAfkEB92hUC1VFdWkUgn3gX-HudJ20uv1K2qw_3M72PvVFMgA957tgiMwU_BCCRdxG-5SIt5HWgdOVI2k41CaWxFl-NeI7eme_mYB5-fCsUPhmHodQz2Kp5lYmdO1AK9G9mZJf94WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-fwLMEFchIA5QQQwGw04hwM-h-w4B_tvNRscoTrt3cETI2UCOP83nuTJNbHpR8dDSdXFkikW2NW4fVf8e8imvE5JCe5k70Vb8R3XejSqZolKupXe17rxMgQeNwSTGTzjWzLw2mmVjJvvlCVGa3Stodxp2sO4jhpRsrC3f0se7o5ezZclmT71Ewn7dCWm02lwYYEclNA0JZFkSe7HVnaYa2pZEQ35au73mfxIc0DPIGPMfAnmawxgXo6uoHe5qHHtUY9Ojn7rJYB2nLpUv2OvGJsJKqf7Gl0RGXaIjIi0KGIbwDXGB4ENUdZpA3uz6XpSO7v0p9iUePPnTOXzb1XgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltzvGBcLly1tLra039i-WyeNlMEUZsTRqtf3OVFcS9JXJYGX_HJLwKjZbJolRQBKr7CsidpUyaBWGUQUqqRe5M0Khtrww-cMuuBinBD7CUWz9cJ9vwID2yFMJ7z9YQkzJ0a9WR01Xo4Scuj9sM4RdldfuXods-USOeRYiftbcchBtIwbAJb-e0M0r_yoCFUuV8nJN7uw9G40pMVZjBb_IOLLi7xvnEZuR6-_mMY0EwBiCaDZ-dTQU0nX8oaQ9Ym4yWYtG8iSFTzrH52OziaJammy9Ph0ah4_98KUz_Ep8ga5PHV9bp_tGtg09C2FIeH84NwbhNbqgENl06u8aS7Wug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1HdyfUAWByMoIk6vYxgPWVMjstkRT2UQ4bsxqI3pmTYW1emvNQKjgI-rImGsZf9hCN-k8SGLlvCgX30a1WzOn5bc29q_4qWxvjRXQY2UV90x1XWdrIfFt-oA_S8hhQDgzvLmZjbBPSNSRk_CPwjfEhX4Ib00MdHe6VoqXLM-x6J0CcKZloY-sTPemsTGI5DJuHvSq3Z0GdBdreklt5mSyjNMokuYKPxlY5m1YFBHZhRa3S8Kf5QfuCpUfpQCeYRSkO_zuIFvCQ9mA7lKG3ujLBGXTuythFfnlm-VviRiYRSS33Wh9P6gvZJewsA2iCUgzVj9-Ip0c42Jqa40Qx-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBfwbPMHTDzSCsTku8j7P1RhAnaS5LXZYupoYuFmmMxSnpLePTG2f-3f4If4mRC85aEAZ1BLCayVPv4QDwXgF_WtV-lLQ5GFBufMMRtkZABgMMiwbVit_AzVcORU4PoP5dsnIoV7pOBekgRN3JAnBULv5xEhEaBO_zkZaPPZE1PEODwMf_7clvpX9RurKuli_q_9wsr3P_9md_ePNiS5vgnB0yNrwLZtTtYipRE2YvVo-xt9I1pbOPr6voz33i4BGnGE5YFY3QeqTUbXG_LJ8zV4Vi_aXcO5ooNO8Ayv2XMuo69W-XkJWrhD-_zFkvlJcCzkJLIIDmzQFFX_c0etnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4Hj4ctwCOn-NXMYcE1li-VHSAxyzRTGfh7wrpi6-L2N0ffDoiHLSh7EhPbabl0u7HC0fUjTTY_CXI8rVmGQ5AKg3-kTl6SclTpr1Ssy7m37pB2v23CVIXLB3FA2RdExezO3WQze3CF1N-_mdUNg_hFnKllQA3V2cqbECWQsA8aZa1uMNYTb3nGHj_n9c7xkhi2q5VGgp95C5zbn37p_knjADB9rcNQOFsCsG1jWxNcFZfuNN_2iuthFOGD4i5T2Q8zWtGQjkiBZunHcH2B8fhhwi69QFlVo21Yv35d88tp_VNbEjxC2htyr7-Cq7fgU0QGVXZily4OEJv1LYtHZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTmzoOH2ZKl_XI512CAmjSlSuo84gJunDlqpLyTCGRk3xOHno71ibHb-qNFHctX8TLJy8vppeoHwPpNbM-Dk1x-6iT0xEqm2f1083gKh6IYlLSaheHLHaWqoEMK1SbzgvWdLeM343BHjoDDZLGus0vDFUEmusENmGyeL6WBTpEhTgtdSm4jM9QMlI7QWgjB62IYf7OVjhBPsRbbigmRgd6wXee23JyAA5u7poUuktQ05utSXqt5lu0K9GaNH7ggK_esIG4j6vH4BZOHlXNUsIRjthC8ndF1vFGwpi74iAETh-4PKSVBqQH4kT84MB7ss8JSnaPYWQFilnvxzUvtHuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=lCxOT3QmYOs244qfes-oEj-d1B-VEPPebVcw50-GwO0f5gTeI7NfAFnyuZ2Th-aJGxR3285dOEIx3G4isxF669QUEUglYLi1WjJAW4lm38DRfmsceEwbCkXLSUPaO5Is30XBKrErfWj512sFjAWwuvGiFBtv8qGXl20-R_YTjnWYI0nuKgpuuyD2Hi5RiLXbQMW0PXVZx8hhlmlt_3LmmyCFBQwagP5gaZewNb48lfm1aKG9x5-w2lhXeZCJGzljcmxEIpgejJ07nQDBAnA6GzedjdawKe4sNs4953mvxMCKYZ1knbprvoiUNqHDUM4E-ngmMOVimvx6LyC2SyVFSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=lCxOT3QmYOs244qfes-oEj-d1B-VEPPebVcw50-GwO0f5gTeI7NfAFnyuZ2Th-aJGxR3285dOEIx3G4isxF669QUEUglYLi1WjJAW4lm38DRfmsceEwbCkXLSUPaO5Is30XBKrErfWj512sFjAWwuvGiFBtv8qGXl20-R_YTjnWYI0nuKgpuuyD2Hi5RiLXbQMW0PXVZx8hhlmlt_3LmmyCFBQwagP5gaZewNb48lfm1aKG9x5-w2lhXeZCJGzljcmxEIpgejJ07nQDBAnA6GzedjdawKe4sNs4953mvxMCKYZ1knbprvoiUNqHDUM4E-ngmMOVimvx6LyC2SyVFSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=EzLhnQ4L4ShCFSBX8lwOxpTSyVUptlHP_W4UDiNZhBiVnl-rA6O0QePv9iZrvQVxrXlDrRSkTzbDanHn1BwEJjsRkNAjptbryR1_kusWe56G1U_k-1YsR2yg3JDvVco4pXkv8sC-Acg6nzW0CJCMa9K3xTwIMXf_wygQHR1Y7l420RzXCflWwr_wA8h_-MUXkE1Q11HWFYfb6-pe7_N6Bp-uKBVnhIgvTt6zaG_NJeWA4HslIri09OXeKk1WO2fWdlmogdDFEZ9TpLG94SsA93fESrcqb9y-uXvERP09n7ycepialccUMZgQsNPKQIW5AiYjGGTrBGoegqXPFunJp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=EzLhnQ4L4ShCFSBX8lwOxpTSyVUptlHP_W4UDiNZhBiVnl-rA6O0QePv9iZrvQVxrXlDrRSkTzbDanHn1BwEJjsRkNAjptbryR1_kusWe56G1U_k-1YsR2yg3JDvVco4pXkv8sC-Acg6nzW0CJCMa9K3xTwIMXf_wygQHR1Y7l420RzXCflWwr_wA8h_-MUXkE1Q11HWFYfb6-pe7_N6Bp-uKBVnhIgvTt6zaG_NJeWA4HslIri09OXeKk1WO2fWdlmogdDFEZ9TpLG94SsA93fESrcqb9y-uXvERP09n7ycepialccUMZgQsNPKQIW5AiYjGGTrBGoegqXPFunJp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HL3LKqFQ_sWlbVBLymMQplzqDkjEdHYaY4l93xEEPfY7sA-aDzBCuL8t7JTWnRlzmvNLKiCdakgEvsQKbBiYSPY2rUih_tTx5kuN5Ki8cUbq3CfTL0bmMJOCleWZwxyWouy_YEBBxcSuPGAu9VDWGr1r_so9mf7_bBpWjBXShmNGdeclroVXfEzpGo2pyfFJfvc6TDiMd-89tc5-l7VKluxBjWAP8K9F59wycCvNnE8D4zlgBQCKlNROg6lszQTXFSAXMV70Qt7yB9mqTa1RIoVwQM8i_NbzWxZPPeZU9D3IL532qGpOIDVE6DZtCO0Lo5-Rkl-GHls-yuq-NfV3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyBf3bzRMVoTfOclGF_ms8gE7HkDnL76nwx6OVtZ-pKCuPT0ZJM9I6tcnyc5KP3LCBqhHO0VLasQJmDeZnDxPdsiYBHXboATUndoORRWcN2l9Pw9nz_478a04hfNsvLuVOW2OZtyZkNoDCD_TR1K8SIrQa6PwCDhiwcNkWHZTPOts5gpEL8AqnRawliBEdHPWQuAwU6WDeF3YMYXm28vwMpP9MKvMAIbvrixO1qBYcN-WynaUbzK4UsxBodZbXSo7uTzC6_WxvCeN5qhyVfK-Qh3X2lhR3n8vE9EJfLHTF4b7x0gNhp2Gvkx_rTUJ_1JXwzfF5UnLuOSJQhrmHJvgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjrjBmvdspwsf20_CSq3TKnDfsrIif9lECVr1GHz3JgKem-6jIh_5OyuzU14FcGyphSHjFWkLVlcuePNXsk6OQxSDsibtjx-aqaYOaEOgNrqS29xmJNvleuQnTtUZ95JqREq-TCDxhQeWarFMUjJtlOPv2GjESg5KpmOo8ixl5T0JRPuf6m6Wl9JwK4DKi1dgy7B22IaAqlRSHw5mGsyjUx8Baq5VqObw2U4Y6dtCJeOC_jRCc3SLNRlLQl5wkRut7UwvNk1PmeVhGorDf06jzAO6KgNJnwHoGd25O96kRj1eQiCT7EBhPC5FaR5SWX3nslcXI5tt5v5R_MqdskvCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqljpP_kzodXft8xQbMO1TZDKV20dHvJAWvoYRK-OfiJKxkoIF3SUH7b1DausBjR2P8OQO8gWmGgTInn0WEkgUjOFkdK0ASWSt97e4t_Z_4xF4L56jjWimcPWttR2cl3Q9xJQEcCu8K8OLmGf3F7lMjT6gev4cZKhgfyl3k1gvHvlaO0nDV_0MjsYpst6HN-9APge_UnYOeA5FQ1g21PoN_yJUgjU-idekI0dtRNIMC-kuFR6G76wcek-eQWYt-iw8dyrm3ky8l-4dEx87GU6U-kfoBNS-544jw_wD5ue8Ch8MJd9WvEwN2TesXK13skTXD_qcBtSH-Ew0hQoVPlkPemo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqljpP_kzodXft8xQbMO1TZDKV20dHvJAWvoYRK-OfiJKxkoIF3SUH7b1DausBjR2P8OQO8gWmGgTInn0WEkgUjOFkdK0ASWSt97e4t_Z_4xF4L56jjWimcPWttR2cl3Q9xJQEcCu8K8OLmGf3F7lMjT6gev4cZKhgfyl3k1gvHvlaO0nDV_0MjsYpst6HN-9APge_UnYOeA5FQ1g21PoN_yJUgjU-idekI0dtRNIMC-kuFR6G76wcek-eQWYt-iw8dyrm3ky8l-4dEx87GU6U-kfoBNS-544jw_wD5ue8Ch8MJd9WvEwN2TesXK13skTXD_qcBtSH-Ew0hQoVPlkPemo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=cyyTzwbgLYs7-VqtbntcIlnfOy9RkApC9AZ_jW30qM3bgbjqkU_ZL4_wkWUYLhAAYxYq7FHauGKE6fHV9AxBJ254QL_914ApWFba2C62iGmuoY0w-alqorbYFLyl01Qk6JRKsEulxATQXCLMeQvCFL24nQV0IaaVk5LglteCZkF3HimnKoiDb0inX0WUouBTgbrtrKUcvzrSa_96WiTlc1hGy8GnZJ263blh2Mar9KD1G0gu5wPJEpNEK0harJCfqkZZaypS50lNcaETGU3rqtOvtzQIFTKgAPCF23IWxcyZ7UOINJoVOfs-gdF6KAkhAHx3t5Pb2bi7rE_jxL_cfkFlSXoDoA39Al8Hm4taqG9jBq7kUVtXl6Ob_jerMCojtPygqRNwIWT9T-RBQEOVzAES9WLruzrP2j_wVcTIF8ipYEpHsS2TWd2TxzY2EMjN7kNw-ke725ZfxJ6nzMPv411uOL-kSvH-CUUJ5qq-IaMaBXUjdL-J-FeXpQZYpSkCSFolmgxoiUaIR7wa7SG7U1F4XI8DJWnVWUsBOJup2O11dDOTOZmEo3HKV0zQGrpajxL-827q5luLSWsihhqz-fMXEdzcFO8lJV1c4PK3-KL-UGqUjnkuuN7K0Pv2p8jA-bR3fTbBT_OI4AQfLVrKhW-lg05gp-FiKaHk_8ZZNWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=cyyTzwbgLYs7-VqtbntcIlnfOy9RkApC9AZ_jW30qM3bgbjqkU_ZL4_wkWUYLhAAYxYq7FHauGKE6fHV9AxBJ254QL_914ApWFba2C62iGmuoY0w-alqorbYFLyl01Qk6JRKsEulxATQXCLMeQvCFL24nQV0IaaVk5LglteCZkF3HimnKoiDb0inX0WUouBTgbrtrKUcvzrSa_96WiTlc1hGy8GnZJ263blh2Mar9KD1G0gu5wPJEpNEK0harJCfqkZZaypS50lNcaETGU3rqtOvtzQIFTKgAPCF23IWxcyZ7UOINJoVOfs-gdF6KAkhAHx3t5Pb2bi7rE_jxL_cfkFlSXoDoA39Al8Hm4taqG9jBq7kUVtXl6Ob_jerMCojtPygqRNwIWT9T-RBQEOVzAES9WLruzrP2j_wVcTIF8ipYEpHsS2TWd2TxzY2EMjN7kNw-ke725ZfxJ6nzMPv411uOL-kSvH-CUUJ5qq-IaMaBXUjdL-J-FeXpQZYpSkCSFolmgxoiUaIR7wa7SG7U1F4XI8DJWnVWUsBOJup2O11dDOTOZmEo3HKV0zQGrpajxL-827q5luLSWsihhqz-fMXEdzcFO8lJV1c4PK3-KL-UGqUjnkuuN7K0Pv2p8jA-bR3fTbBT_OI4AQfLVrKhW-lg05gp-FiKaHk_8ZZNWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IueYLvXxvQKYV0seqXRau-KKKsZnqW2YvFCudAh0RbOwAjhMoqjBAggjQFMCmcAR4Y6LV7KGa5S8PfafWB746RICPL9gYkboe2KgKz_WPekqjViiPQYgSluNSI5u80kepC2AE5iFdMD7sST975cKVwgOJYU1Bntv1s6ojwn0ee1LvJO7ssgvUH2J-hCB53kE5KNgOfA1_JgHvkLVL4PW8B0tCIZ99nlq1AXdxKTAa04muo9N8tnQrSuoE0N77EICIeuJqXIXJ8Scpy1iMR_kjduMPlwwzUR0tmzDXOHjdx2O0HWusr9UOckVSg6y4r9oYLX2ppdFrEf-rIn481LEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Peip6I4b-UPahnH5E215gmmJWVGwA2J8PKSBbwGMCIrpMUBI__dCLN3lL8ipORgo73rL_-exXClGk6hQ6i_LZZHsuGESEtcszH3VxW6Y13MbIYOY3cfMmFtvESP1_MYTgqsOuHz8bEGYZR0EZEUwMoRNcI3xMS-fKIvzrHID0g5qelo2J_-qLwNTg7O_Zcu8rZLPcJagLqBiTDB_rsPGnk32fUt_OFnvuRKTRSAs0uHO_0dHF_TiD9HTXOO6OF9Pb15GdYWQksB0m2gEzh9w_PqLyUsj2EL6S1Lyx7s7lMUv1yK7tDFj3-uhjcIdyxHsyznU5psqJODVmL40hKgg3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZ3Bzm0yiDIEKbWerI_JlnMCuwR0RWfaU0OPnNR_Yep5JwHSYSK8j04YYr1meLqNP8Y2bIZyPQC7nBia89gufc74yLSCdi7Ai1tdZjL_Ljvpv_SHiM4u1UlFbF8h7410HqF47yK6hIlqeRVxpecVjjZyg0ea8vgmLP8-n9yKEtCLyC7k2RdaDvnYWNy71nbC8q9iorNKCPw-UIi_jmG6gMvCK5zGoESRZDiO4larZoZ48-qJrhtbh_48mCWsFumiD5oBMOXUZEpROE2GRIjgv8VvkQmNJCeGiXnNnf_ZiZz3IMJGfc3dVjOebdnI_2BcuVzEypv_IOOGAGTIE354aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=t2u1dTdC6z-oHZxCG7WP7NXSczGraTYAADzg_aQfCn3_ZbpU1I0ywqQ0GNokPgByi-XBselHx4QXgXFrW6pGkIC0E08BF5OnuAg63zj3x-nxo53lN5lPLwKm1NrQ_4_da-kggRvQnYWEFNss7tqUg70Q2XOQ4tD2pmfvzf7CI3ciZ78zKc6fMhUfTAB13PbmyJSUAMs5F8TLrg9O7Yb2-x83dhFEfPJM3QUmM712kb_h1FeCzseiedmGel6OKn7_fzFA1E7TN-h_GjK3triJJO6OR8pzSm1nvmkg6xEi89TEj9yZQpdPlaAeLRpPCJnYRrAXp68l_p4PkG3XlAYfwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=t2u1dTdC6z-oHZxCG7WP7NXSczGraTYAADzg_aQfCn3_ZbpU1I0ywqQ0GNokPgByi-XBselHx4QXgXFrW6pGkIC0E08BF5OnuAg63zj3x-nxo53lN5lPLwKm1NrQ_4_da-kggRvQnYWEFNss7tqUg70Q2XOQ4tD2pmfvzf7CI3ciZ78zKc6fMhUfTAB13PbmyJSUAMs5F8TLrg9O7Yb2-x83dhFEfPJM3QUmM712kb_h1FeCzseiedmGel6OKn7_fzFA1E7TN-h_GjK3triJJO6OR8pzSm1nvmkg6xEi89TEj9yZQpdPlaAeLRpPCJnYRrAXp68l_p4PkG3XlAYfwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY2mPQmcbU8mius5VeEOeRAYKp-TQnfsUsZwK1n3H-YwLxDjjEOMkDTeRJ79lyfjQFM4T07H4dF1UFngcLHKY0pvncm7LDwwFNsQ9iAncf1pt9o_t0hu55KCWMzeGQTjbmDk3m4YrG5r5OKuWMPw6PZ2ubexrycqwQjtErknitN3kYnVEekXZ2S163Da6FK8giGa9gnKBYpP-7GyxXQAPypYvw1IGPtRh2m4FZdIaeot_h6FMp_7FEm_SYKC6VGiBn936ehX61yXvubmkDpnzRni5vdXkXIgosOe5U89iqBeB0u-Yc-AXQutPTgG6O_WTD0NDqYXqetdkcMg3wRMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=frCmH7rH0RrgG3vuJpJaXxp3mPmwBW7GEuOwXwEMIU12ZXRDUzTFwvb51--McWsYZPBh2Cu__4KTJkCEm0fZ6I3LnH5yDbx3gl1YFpaeH1tAOYNc63ls6_JuYC0Ml9V33XzqkVaPQtMnbBIg8CEh1pyQE_mhAkibeLWTquLIPkF2rfjB-8WZa9lEb8m39gbma5DXozeHaC8E53XVex-Qcz24PA9A1KoAiVPLp15vfkPIaKlm1oe0h0w1vjbZlUU8rLFyu7_3M6ki6gmT-aOtxPYrtGrbF3aM32TyM8It8Pd2NzLERFW0Z6v6DjoGzTofKgiqHd9WYufgs6wdlu8-Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=frCmH7rH0RrgG3vuJpJaXxp3mPmwBW7GEuOwXwEMIU12ZXRDUzTFwvb51--McWsYZPBh2Cu__4KTJkCEm0fZ6I3LnH5yDbx3gl1YFpaeH1tAOYNc63ls6_JuYC0Ml9V33XzqkVaPQtMnbBIg8CEh1pyQE_mhAkibeLWTquLIPkF2rfjB-8WZa9lEb8m39gbma5DXozeHaC8E53XVex-Qcz24PA9A1KoAiVPLp15vfkPIaKlm1oe0h0w1vjbZlUU8rLFyu7_3M6ki6gmT-aOtxPYrtGrbF3aM32TyM8It8Pd2NzLERFW0Z6v6DjoGzTofKgiqHd9WYufgs6wdlu8-Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVDyUDbqBM3O7F6KORBGm54vRer5fmf3rnGjV7Sc9NkGVS6tmqPmKI4EDkdrzd5VxPCbKUzQVve57yCxcrsenEUrwxI3hnU26FM7E_4Rk0AtoNuFdFh7o_ksmc-wF3XG-awLKwtLfmvJ0DCyu62m_x747OIFqrY5eAYJecfo0cm-jANhK95Pa_zWSvf2rFzV6VxX30-7UPxI3oHigaZk8Cg4WUk1-M5i4dyAmy3Dcp4Zw3inD2vLaz5HBFHPNC5EHTelzAZrONR5U9p-w8JT6MCBuG53EClCiPnbiZ98JUP8wMbPLOCAqZuV58_Y9ZRa2LbM3Oc27EUuYopHk5Ydbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiyxR2ArGMDayyAwYrTwp8vi_XlQu9zjAzt3n636MvsSiEOnWWC1rQIm8a-mU0iWDlfhY5ty5ru1i7AnijV_NeXetsFwaMVFE_adocYjfH-2_SqihQ7y0hAzFPIan4LehD6H30NLS6mJ1kw2VIZuzGkG6sKyoJlTWJiq4SWs6hlzbViYd51Od72nfxKywDAd6wPZJT2b1Dk4hYjT94xjyyebNzx8QqWPzaybe948Zp_8jrZg1vqk5v46Dwcp08YnBlAS5RFwwKV89uMAldqESxEEsitBFxtLeye8u9BtRSaLjV9e4DfEssshvr-31o_bO-Nscbi0Bu1yFw1zWnWOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=M1IkNTY_c74cWdMZRoH4IElTw0BqkAuaXjfvyVQojhKGA7KEJwIikXctAilvW70atHutpWZOm6cmD8sBKm9sdxBvWRlhebZXfmui4Z_vvif1pltB0CP_gKbSkm0ShsCSFEqoli-1E90V8Ytg7kxdTokPav-mm1O8-eId1518vRSIR0zitYi0YN5yYXtwWbROgxwSCNs08fz-Qzo_d_DhiDFLVpncvtV40M018ZVORZzZLnWv3HmvxGFt5v2Ge4ZRYsJn64j1mY9_8rMVjOul67cU00ptsExjP5vyMHgObcMfDIinJYC32IPDN5gFJxR88FaB5nXdbeLFZr150ysMwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=M1IkNTY_c74cWdMZRoH4IElTw0BqkAuaXjfvyVQojhKGA7KEJwIikXctAilvW70atHutpWZOm6cmD8sBKm9sdxBvWRlhebZXfmui4Z_vvif1pltB0CP_gKbSkm0ShsCSFEqoli-1E90V8Ytg7kxdTokPav-mm1O8-eId1518vRSIR0zitYi0YN5yYXtwWbROgxwSCNs08fz-Qzo_d_DhiDFLVpncvtV40M018ZVORZzZLnWv3HmvxGFt5v2Ge4ZRYsJn64j1mY9_8rMVjOul67cU00ptsExjP5vyMHgObcMfDIinJYC32IPDN5gFJxR88FaB5nXdbeLFZr150ysMwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=ObjoCtV3ATCLJJQb9SVQBSi157tYUGjclfz40dPecVXxfxLRUlrqQdkIaJaqHKO6qlGwbxhTFdmNbXLZLjziTpiZo4fWenREvbbgIN2zKUMnwoKfHuLwQm22vSeooNo3_6-VjTt5bRJTxiOl5j6deMFsMSruiEBN6L6dA75d-h3SPa4WHxt8ICDtwYLAqIPzkK3-Y2He9zOtU0Cb4tjN8XulmwjKB0CKbbZ_Z6ngnHlzWh4eqK1lcNN4lVEXE1xTKT7eEaDW7NNvMR5nZWJlpnRTDMVy1wDMNeYH-fx98AmuGN7z6DiLYcv5QdLXbYyDBbQenHw27GRNgmGXuBVVtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=ObjoCtV3ATCLJJQb9SVQBSi157tYUGjclfz40dPecVXxfxLRUlrqQdkIaJaqHKO6qlGwbxhTFdmNbXLZLjziTpiZo4fWenREvbbgIN2zKUMnwoKfHuLwQm22vSeooNo3_6-VjTt5bRJTxiOl5j6deMFsMSruiEBN6L6dA75d-h3SPa4WHxt8ICDtwYLAqIPzkK3-Y2He9zOtU0Cb4tjN8XulmwjKB0CKbbZ_Z6ngnHlzWh4eqK1lcNN4lVEXE1xTKT7eEaDW7NNvMR5nZWJlpnRTDMVy1wDMNeYH-fx98AmuGN7z6DiLYcv5QdLXbYyDBbQenHw27GRNgmGXuBVVtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=CLDzKPueJoLXEKI9z8i8NKbUbAXh-cUg7_kjD6PiQ7UI1UHl57mvHGwSEjGelTmQX5FP-sVwEbj_NbPmttLD6gb0f8HjSSIwHBB9ZV0Nk1RCeTkNdb86cUF-JpSCpkXMYmuPeXR5F3EvwOzF6EWjDLGjIcrqBLEdTuI2PSkkFfAw-u2ZSuPzv1k1N0tP8oFh6xXhAhzbEns6pU3gIZvq9AP6-SQdF4h4GKrEMHb123h4E7sacrsQa4wb9mMivpm_j0Wjxk8DikUMAuPoAYEKHdH9fdCb2ZX_6zoucgu0koxP7HAzrP7OY0gKLBP0XoI9A6wOZwvTtwsR-68Q_zPWDLu3xVUP3ulrSD7iCxzKgbE1rbuZ_vJ3j5uu39294dOcurmJv0fL_17eftqK-275PguAwOqfR-dsn4cWAYcLdWDV4HIPHBs-90HA9LNq4UDvAWpr689PYt2kzqKMvrx6niFwPfDHFQ9AgkeSfJfjcTHUaGEPNa8H3Mi_T9GaOynefYK2NPlIH9UOixllc84BJFrT0SkHJcV2vOPMZlsVTzASXhG4qeqgZpiuxsf1rJjnkiTdxf-jEmIMqJmUnA1jl9BhyXljJgpTFz5A7hQKh_J1uMsLmgrRbzA02wEjNy4iaKUSh0PBPDaxs2eqYauDS7W8QR5eAFpWaBKjNtGh6Us" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=CLDzKPueJoLXEKI9z8i8NKbUbAXh-cUg7_kjD6PiQ7UI1UHl57mvHGwSEjGelTmQX5FP-sVwEbj_NbPmttLD6gb0f8HjSSIwHBB9ZV0Nk1RCeTkNdb86cUF-JpSCpkXMYmuPeXR5F3EvwOzF6EWjDLGjIcrqBLEdTuI2PSkkFfAw-u2ZSuPzv1k1N0tP8oFh6xXhAhzbEns6pU3gIZvq9AP6-SQdF4h4GKrEMHb123h4E7sacrsQa4wb9mMivpm_j0Wjxk8DikUMAuPoAYEKHdH9fdCb2ZX_6zoucgu0koxP7HAzrP7OY0gKLBP0XoI9A6wOZwvTtwsR-68Q_zPWDLu3xVUP3ulrSD7iCxzKgbE1rbuZ_vJ3j5uu39294dOcurmJv0fL_17eftqK-275PguAwOqfR-dsn4cWAYcLdWDV4HIPHBs-90HA9LNq4UDvAWpr689PYt2kzqKMvrx6niFwPfDHFQ9AgkeSfJfjcTHUaGEPNa8H3Mi_T9GaOynefYK2NPlIH9UOixllc84BJFrT0SkHJcV2vOPMZlsVTzASXhG4qeqgZpiuxsf1rJjnkiTdxf-jEmIMqJmUnA1jl9BhyXljJgpTFz5A7hQKh_J1uMsLmgrRbzA02wEjNy4iaKUSh0PBPDaxs2eqYauDS7W8QR5eAFpWaBKjNtGh6Us" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZnucFN_ZHKw5QJlNDHsh43VZ4HG3ciIcuH_52GsaFDaeDbbCX1edzRdaDtDcyj1EE0pDWMuwJad0u5FMJyeUfhnpkiI-EVtxNsWOdIIbqE3_hXN9EdIjge7SNPthLxLP_YH9c99yRzdM62P5uGG-L-WhUUQaaZNJNDA8Aola6rnOsG1214lexeeCuC8eG4do_y3SUvDhQ1yzSTov5dyVHjl64idx0dn_nsR3g7f3LPdtGX3mQAN2uFp0WL8Zj-YaVyn7Nh03Gx9Rq93Lptr8wiqYTwFbsRIyF97EcFdDrJVbtaw-VZNiQ2SazjZxphZscS08vIqa0mIqQzhbkdoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/su4qH9bzpCpi7Er924hX7dKH9d3lYSv5x1xniMVkZtoxP3H3TR-pXJrY7THGr82FSNIHSOR-IlLzqGnt4xGjxxkTo9ykuBnzw_b74MHgX-e8Pl97ZXhU4GLKizRjad1922YYVYIRnJmgz0LSYzxW40u7xciuN94ZjBik21Z1RBdyjBwd8B2hd_SSzHHIQf6aodh3gy7yY2oN9BAWpnNO9j4hQpILRxhZCZthT1huM866IxP8uAZFZHTVQTu-8Gm320S6z7w7xAYbCijKwCuk_IwM9p7KVznZ_ogYaubLOcDtSphmaHQ3ZyfHQ_V8uuCz6PPCv_sWTY_ve6bajM5CDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zu5kWpDrOH2YBLpsqc1ILladt_N3WAcIX6LtgmTg1FemFw-qaFNRUxdGn5iI9DYXSsidZnYTf_gZJWyeiF36UmyMswcL1HjwBG4fUJe5GRAlym-bG3Uc3w2zhYOJIkBmu6-0MKZTbOYh4KHpKaQeK0d7IPQWowtaXnJFrNhgub7MoxMd55vySKk-QCHVRrNnnBdh4ybTfxucqsr2hKEQNdDrxj8CPCgl3d66RMktF9v3qltR6nXfHzfemqiYpIeFZD--fH8ofRoGlhF0kqTMrmrCwj0icPdIxtvW99YIr4dDV8lEsQalC2xVqpUvjRVGE-IpunIPnmshDWHPpacwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=CeTN85f48zoXQCok9ojhKCvgxdD6DWCa4CB_uPqHawzZxPMERbNP44Tv-OApBJyT0XlNgc1LFtX4StULhieziN-b95t1kKfdNU8-M4N4xqXn1YAQkmSK_7TFBZM3ShFoje0Rs4IChAM9KV28FacGASwC9-00nZ-gvYioxVkfR46x3wYe596IWRHAXBUYQOhhwCSsT_8C8tvEwxR_S6KYCAt3pbOf1dB8RlgTPOncoD-hLu5K4_8TuEKIUh7BbgGBi1WNetGyoeoswxf9Df_jaB4Uc9z4GkY6PkJzus3mNwpE08VEdQKUErIaXir5Zc8f2wUAMsy9J465OhGvhD67szzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=CeTN85f48zoXQCok9ojhKCvgxdD6DWCa4CB_uPqHawzZxPMERbNP44Tv-OApBJyT0XlNgc1LFtX4StULhieziN-b95t1kKfdNU8-M4N4xqXn1YAQkmSK_7TFBZM3ShFoje0Rs4IChAM9KV28FacGASwC9-00nZ-gvYioxVkfR46x3wYe596IWRHAXBUYQOhhwCSsT_8C8tvEwxR_S6KYCAt3pbOf1dB8RlgTPOncoD-hLu5K4_8TuEKIUh7BbgGBi1WNetGyoeoswxf9Df_jaB4Uc9z4GkY6PkJzus3mNwpE08VEdQKUErIaXir5Zc8f2wUAMsy9J465OhGvhD67szzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=YJ_PZy_7qkJDQcUCxWzEV7oJl3_mtZK-ICtL3z7nLRX6Gqc0Ez5Ou5abbetepZTc9QOfUmIMlvNtoo3w5RMVVpLEGsXx337VliT6h7nO9aJNaFzoWjM30phlwf52lLbl4B3ip-EezEqpPv_G_r0mS5zialG1CKtMn8cOhvRyBhE67y_3yNuVchXwZOc1w6XtnM-MFACaLv6W_UyzrW5rVLJyyppIG4efzwx-f4cqIINieyt8b-F5n-ZBr66-AnopKsPn2qCmuLjKSZIaVfskC-MFGRmTFx-W4lkzwhG_Kq4xIQ1YDYFCkL_VVCMRiMUZHXc0Uk2x1QV7F6dbNGDhVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=YJ_PZy_7qkJDQcUCxWzEV7oJl3_mtZK-ICtL3z7nLRX6Gqc0Ez5Ou5abbetepZTc9QOfUmIMlvNtoo3w5RMVVpLEGsXx337VliT6h7nO9aJNaFzoWjM30phlwf52lLbl4B3ip-EezEqpPv_G_r0mS5zialG1CKtMn8cOhvRyBhE67y_3yNuVchXwZOc1w6XtnM-MFACaLv6W_UyzrW5rVLJyyppIG4efzwx-f4cqIINieyt8b-F5n-ZBr66-AnopKsPn2qCmuLjKSZIaVfskC-MFGRmTFx-W4lkzwhG_Kq4xIQ1YDYFCkL_VVCMRiMUZHXc0Uk2x1QV7F6dbNGDhVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
