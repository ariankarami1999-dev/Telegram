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
<img src="https://cdn4.telesco.pe/file/HZgd3rN0R4cYtz11uP4V7_rli696yxEQvqnAydyoN9WDYGotzNpHUdNu4DJaGgsgtZy32R1g6X9OqD2euTPT_8Dm-wt5kz44rgw8OF0nntmksYmRX1doMc56i3Tw1GLVlnIjD1T6i3tVpBhFj8R49orfECZ1VxGtyJwaoicB9Z1gdtWKYPzPTGx4-ZH1PL95AIobZD0rbegRAoxdliPfxtNvk-0aVAtT4D04r6Lo32-KQcamFz8_YZ7I6XRr9dQp_2pgdw00tCKrI3jw1juNj45uCytL2ZpZnydoynqv98WVKgIw-RhzRLU0B_qD4kGzzxoN7Vw487geeC5ZLorV4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 01:23:42</div>
<hr>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O07E_z406qk9KhIxHXiH4rDy6WpaS0l11ZarOMDQD0TTyc635mHfDYYMg4kL08u6-HEXQK7FIyAKx95N9MjWq3hGqmmd7wQNgAkH2mFsVduIChjfFKI60CebQhOGoWxlUfZzhk71TkULT0VV38AP6G_-fT5CkQF-b-X9pBcWkBbJn6uneTlrnclKrGgy7TGuz0QPKNCfRsrG08ADHM1sLhvXpXgVOVwYxO5dsFOrgY7ul7UQRPvTjP3TWfp3YvdBRX2GnwSF4QQMLRrdnjCBcRbd4Iu8fmhLGDa-tht95C5s9z3bcrQYfmjNs2IhJMS1cYPRr2DgCEGb5vQT6mm0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منهم صد بار نوشتم!
جنگ رو برای خونخواهی خامنه‌ای راه انداختن!
بیش از ۷۰۰ کودک لبنانی رو به کشتن دادن!
جنگی که نه به خاطر لبنان بود
نه برای منافع لبنان بود،
نه با سلاح لبنانی‌ها بود،
نه با تصمیم و اراده لبنانی‌ها بود.
یک گروه مزدور تروریست
از جمهوری اسلامی پول میگیرن
که هر چند وقت یکبار جنگی با اسرائیل راه بندازن!
فقط برای زنده ماندن شعله‌های
خشم و جنگ و کینه!</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=SeWkIfxZ1chyMbAAtm5c0LKNkWbqR2iEHAXoj7V68xtpBWCi1i_T-auBP2Xmk3wDTzvqTyA7jqJKQ86yCI7Raz1t7dKFp58JPNocDsFdHpBZrDOrVWM09Q-6Pnmhqry5jiXQbmZGy5M1WdQhyltqhRUkZ8D0N2fFjD2qBx-msSU40Gw52cmzH9C_OgnYiU6yCS-UhjegKQxtWIAN3IYKNwldihqnibq6pG8P7NDzz50d15zT-T7vCHLu9K-LvkwidKxTkUrIAzcSHqVLgZSiTJTtjgAzHVaGxcePfz5zIlIRDajGxvVnsp1VI-GiyMMXV0u89fEiqGtK4pDGIVfeFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=SeWkIfxZ1chyMbAAtm5c0LKNkWbqR2iEHAXoj7V68xtpBWCi1i_T-auBP2Xmk3wDTzvqTyA7jqJKQ86yCI7Raz1t7dKFp58JPNocDsFdHpBZrDOrVWM09Q-6Pnmhqry5jiXQbmZGy5M1WdQhyltqhRUkZ8D0N2fFjD2qBx-msSU40Gw52cmzH9C_OgnYiU6yCS-UhjegKQxtWIAN3IYKNwldihqnibq6pG8P7NDzz50d15zT-T7vCHLu9K-LvkwidKxTkUrIAzcSHqVLgZSiTJTtjgAzHVaGxcePfz5zIlIRDajGxvVnsp1VI-GiyMMXV0u89fEiqGtK4pDGIVfeFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=RI2LVf0juEZKlxEe8fOyUxqso8ZpH6MvFn3CXezzSwiiGFIWn8gngzWm09NQWRKhmClzqfA00n2pYx3rW3cHuioc_G270kGoV3ETw-6cPFB_zKuBsroywsSJcMhcyscntgslErux9BO2vHMn9wZFDUHFp370RRjkpc7XLJatTg5mELkz2cmNUZtbT2EdMvToJe1NDaklzEl4LtanMlFIrmEwjid7dJTHYQjd3IvtQWnFrrGwV7fckGuHEVYcQol-fdNfIbWFxlX5ofYYDZeHe0O9cpbLACvZHx-TOony6UPyIGnMbG09dXUbKZYcuduAaMx8QA0U9d0bAp26qCLafw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=RI2LVf0juEZKlxEe8fOyUxqso8ZpH6MvFn3CXezzSwiiGFIWn8gngzWm09NQWRKhmClzqfA00n2pYx3rW3cHuioc_G270kGoV3ETw-6cPFB_zKuBsroywsSJcMhcyscntgslErux9BO2vHMn9wZFDUHFp370RRjkpc7XLJatTg5mELkz2cmNUZtbT2EdMvToJe1NDaklzEl4LtanMlFIrmEwjid7dJTHYQjd3IvtQWnFrrGwV7fckGuHEVYcQol-fdNfIbWFxlX5ofYYDZeHe0O9cpbLACvZHx-TOony6UPyIGnMbG09dXUbKZYcuduAaMx8QA0U9d0bAp26qCLafw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re8Ivd1acJr2AYq_VM7tBuV0osFyLtc6mK3P245ttOu6Iq2qX76CrvfRCjBeqGzRuFp0QFj3RH8k0gFxMAZTGrJ1I19OFWVpaWxRrrlRAuw0p8l78rRk3nhQazHBXnNEHr2a9DqpwFos-ADwLJnvCNYCqQTT-ey2M7sDqj-KJdKgUzN-WMl8oSXrc8gHUjnty3LQsfP68x-f1-c6d2tbS4fJ-DG6T-UMDxZxtslrKxFaTWHmMrYPxDJZFJpRvEBO-8Drgiqbl0iK06VDjyPApXY3CgfxcA7oJflirROvqrGRY1LuwZ0feiJEkLq8FoKFH3kb3DfTcTbbHHoANP03TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=eqPeDj95TNkx-BDcuhGDCT5Sj8IcT3fswfrVXM4_u_wS36yGj9qkYPr24VmV_zpn1U2iYehiSNfHdvvjMjRa1oqJSVw8HwA1PZOOTL0CrCzEpl8sN5JSZeZZG1xkdTraxzGc9TcJipy2GE6td50o7M0cF_v-Nfs4v_pGi1lKaji9QOCzHgd9XAGEME7oGlz-BlJGf4j0TnkscDoiNkB3FzmU-viM6mPJozcG60pq1dIxlNw1ASSGMgbScJyShx442zO-WrSK0lNefcX3YyKinIq9GrIopWg2lntYN-UgmtyvE5wZmlEwSw2NEKZDRsscZcghqn77ANTVx9N1vdlicA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=eqPeDj95TNkx-BDcuhGDCT5Sj8IcT3fswfrVXM4_u_wS36yGj9qkYPr24VmV_zpn1U2iYehiSNfHdvvjMjRa1oqJSVw8HwA1PZOOTL0CrCzEpl8sN5JSZeZZG1xkdTraxzGc9TcJipy2GE6td50o7M0cF_v-Nfs4v_pGi1lKaji9QOCzHgd9XAGEME7oGlz-BlJGf4j0TnkscDoiNkB3FzmU-viM6mPJozcG60pq1dIxlNw1ASSGMgbScJyShx442zO-WrSK0lNefcX3YyKinIq9GrIopWg2lntYN-UgmtyvE5wZmlEwSw2NEKZDRsscZcghqn77ANTVx9N1vdlicA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=FbmtZNzAr8XGlE3yUGss62nPZnQ4-lbsynqViBaFo6IqiwOpuQNZUBtzhn5L6B1Y5U1_bsmcuj_k-jV7dKjd6Za_C2Li2KPo-aWOOqsQH4Ydwp4YyT7EF1PAQVzeYAql7XOfGChc5oksUgTcj5vWo71-c7o87Ft_t5Kg3QlMs1PoB3Et7UkJGKh9yyy1_rzlbNv3CXzsOxYf-BdykgUJDw_doFRWpyBJXf8DOQskBOZAbUqslVO4Cw11CxQNyAwZiiCJcgobCScWy5BAptGuIQEZfSe_EfGsBbQ6S0iTRDN3DbKTDymyc8Vu7R5vW73gJylyspsWgqCwGlBNlSkjWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=FbmtZNzAr8XGlE3yUGss62nPZnQ4-lbsynqViBaFo6IqiwOpuQNZUBtzhn5L6B1Y5U1_bsmcuj_k-jV7dKjd6Za_C2Li2KPo-aWOOqsQH4Ydwp4YyT7EF1PAQVzeYAql7XOfGChc5oksUgTcj5vWo71-c7o87Ft_t5Kg3QlMs1PoB3Et7UkJGKh9yyy1_rzlbNv3CXzsOxYf-BdykgUJDw_doFRWpyBJXf8DOQskBOZAbUqslVO4Cw11CxQNyAwZiiCJcgobCScWy5BAptGuIQEZfSe_EfGsBbQ6S0iTRDN3DbKTDymyc8Vu7R5vW73gJylyspsWgqCwGlBNlSkjWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRkNt9P_K0cLX0X1iCZoQfyrbNeOd_JITf75SFDcR1lVcltYSUOBfL7nSm9u8yzj1LlAhpNTt7Zm7wG53cl8PGIUGKVNZLLBYSNStKSZ0rTm1cvJR6lkRS-NE63ed7WZqWQ584z56Fj9tiRjwhGiQ0NIBagqU3Ip19kHXNu7LWcs1Q52OWwuslV1-OKjej2vrM3iixpL_s2iMM1pw9LYwIlUhKFggRnRyt6j8-qSQz7GAYSgtyRkc1GBiytPfid7m-w2UgPEYWa4zDMWTGHi5HLyWLfetuG8KlP-bs-oh0cnqP_AvCushNna2NMtHtkT6CaSMVBbsCbBlHgcn_y2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqOYY5hyBR7EOfZZ5KIuNUn8BR0wpR8j29XZbyrox31TTFKxO_fZ9PxPxoGXlmZ4LwOY6D4ScQ4GdhiWbkM6gsJwBQjKvpKfUR9RLtUjdXmv4IXpgt988FS67Iay-hKyh3cLbE_BkfKjFMb6wkGmGKNB8Cdlsip7CAnvEocKm0f4nKh87RqKYK_MMEuCYisbZ-zRWMV9n8udDXADHyHhpiuyoJPWrgFeObtmEO6LMcy5dLgmUE7Uix_gqJ4aG7YmF7rIDvMZkrI5dC3Qi2znE9C4a8ftSI9N1Z3XTr8h-XmFModztDJVjta3AQGsO0W1zXGY4YrZ3NtAWJXkJc9HnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای حزب‌الله ۱۵ سال در خاک سوریه و در جنگ داخلی سوریه مشارکت داشتند
تا اینکه یک روز همه شون فرار کردن!
مجبور شدن فرار کنن!
نیروهای جمهوری اسلامی با کمک هواپیماهای باری ارتش روسیه به ایران گریختند، نیروهای حزب‌اله
هم زمینی به لبنان برگشتند، گریختند.
و بعد به سرعت نیروهای احمد شرع
سراسر سوریه رو گرفتند.
بین نیروهای شرع و حزب‌الله ۱۵ سال
جنگ و خاطرات خونین وجود داره.
احمد شرع اما در این ۲-۳ سالی که قدرت گرفته سکوت کرده، اما اگه نیاز بشه، می‌تونه تا ۱۰۰ هزار نیرو روانه لبنان و مناطق تحت کنترل حزب‌الله کنه.
انگیزه بالایی هم دارند!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDMrI8sjMdcQthejeq3gW8GtkYqzNcYT-bFT8ZC2DlPDU4fC3yWfDazNq_DUd3YcFLcoiZFB56PexJFyl6MtXaAoIdZ7f-VtFtAMPZBqQu-RRBQY4jBw5MYX9JWYyge9xiS0ah0IvUgULsL_YAQmDHcixHj8gzfG6HmFoc6kWHkEb8oND8MZq6KXqG_ZP3FSmG1ymI5ayI8mEfiYD7FeVEFQzbwH8GvKaf9HS_XMUxGzWCK0nrsA4JKMzzJaKF7JcxHJLa_ek9m1QwQxHXqj5Cvu2CXuN4OOcYlaRtLf85d03HpZRi8I3j30cePJnMZKbYcMXUCn4lxXkZrk6RS3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKeAfFFZ7yFs2dPG71D-vguS7m_tGyjrM_7aOtKZesH3NAfyjMP_99LnYrvwFw12YerUneqhW1MnozlIg7sCBNZifPjorSA5nOuLG_qjkG5qed-ezX3pwZql1ZPKQORgh1OvDRA0tm6sWs4T3WjNKeWFH1zfuTgsmEOL00WffrKXZbkHcv7NZLA1mLVyLWZDQiNMPJxZGzE7LWYf7W92ciMlPb1sCxi9wKEw5HoWy5FIvB45ry39TeGeEx9AIuFbCPAWILoeDNe8QGYvtSggjoAxZtUzZfXQ7XiX6xHPSYGAUmucAu80xCT17Obm_JM5rcaLNF2hdZKaKf9eer7zCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=beGd6hj4dpjXBpdn955zRb5hQ7qfIl7f-EHjDJx6hy60xaOkKVCfQwA9NNsmBW3tQA3TCtxi_5Esbndy-JRdLKLud8yPGXyKJ0-8Fr1ztUshMmwx6jtrsAtknKwcxM7vmF2xczF6vnStRqXXsmVqeUQ6RFx0cLjZf-yHM5iEWaR5HzpYq28KkDZvaoRKHNKlP2Wit32-Ab0M8Z_fV3X1wxuz-Vaz2fYp90WxWWJyFfmoMIQOCdNKTjPDi7IRjVK7hYAUrqhcIlgSQcNZyRynC6xEScO7_ANjJK3mYxrsd9MWvQKgEqTPFA_RICFtNmK9VQVoQyVuL0SqLonkwOd5qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=beGd6hj4dpjXBpdn955zRb5hQ7qfIl7f-EHjDJx6hy60xaOkKVCfQwA9NNsmBW3tQA3TCtxi_5Esbndy-JRdLKLud8yPGXyKJ0-8Fr1ztUshMmwx6jtrsAtknKwcxM7vmF2xczF6vnStRqXXsmVqeUQ6RFx0cLjZf-yHM5iEWaR5HzpYq28KkDZvaoRKHNKlP2Wit32-Ab0M8Z_fV3X1wxuz-Vaz2fYp90WxWWJyFfmoMIQOCdNKTjPDi7IRjVK7hYAUrqhcIlgSQcNZyRynC6xEScO7_ANjJK3mYxrsd9MWvQKgEqTPFA_RICFtNmK9VQVoQyVuL0SqLonkwOd5qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieEhutb2TPBsPUsSMePt1GI7n6UjUt7srBoymC4CUpnj6IeJ9qilmBBOwXxgYN6R4UIGC-jxrSlZfokCAtR_oD8AhpZFxo6ZVtDHDVzb3aK1QioXRSKLQsYgEDnnnDfBIxBPXhMRIqU4za2Om8NlmZCIgXHHiqTnbl3GJuD_9O2qJmQ09YWHvjf8jkANdnqQSS3lGXHuFAtqumIaQqAGP-mDaKfbJHJyO_4XVkFoV_l-mddx-Zip0ClI5hUEx_Gt7iC7Yzy61GE1WaWAf3vJ0QRo6x1fkcriVU9gFwRA6CNChdOKbsv612yZfy6X-JTAY3yv9pyzZttogBKi1DeONBUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieEhutb2TPBsPUsSMePt1GI7n6UjUt7srBoymC4CUpnj6IeJ9qilmBBOwXxgYN6R4UIGC-jxrSlZfokCAtR_oD8AhpZFxo6ZVtDHDVzb3aK1QioXRSKLQsYgEDnnnDfBIxBPXhMRIqU4za2Om8NlmZCIgXHHiqTnbl3GJuD_9O2qJmQ09YWHvjf8jkANdnqQSS3lGXHuFAtqumIaQqAGP-mDaKfbJHJyO_4XVkFoV_l-mddx-Zip0ClI5hUEx_Gt7iC7Yzy61GE1WaWAf3vJ0QRo6x1fkcriVU9gFwRA6CNChdOKbsv612yZfy6X-JTAY3yv9pyzZttogBKi1DeONBUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzOtuF0z5Wujey2F3OdslOG2FbUAK-T38vAZWIM9QzCUCQ20JiVQExwCGez6fwoNbJWiSNNRxxlPK2vksG5_HeghEPJeZjhmDrYSqah8o3nxHuUUjvhECSRciyTbV4EipyWQXQlJSUR_heBSgjgCF0VClBwY7qGB_MpJi-RudDpKIJKKyAH9n10R0_sTeNt5RohWiXt5eaRqDcVr6X9lB8dcUh7Mpy6yDMJRBcfJx8L3TmoiM_mUGjWyRIF7-V5pc6w_G-iIBEkUVB0Cs4njsqHjZlReNFavrEkDWaunhwI9RjU2lCzMHQXBmlosuieZr_mksFW1-vbSpo2aiAOQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JM6noaXXxHdRvjLLbFG_4yAE3KrqErHXXRgoh7cpL2eS6b-tEL0gQKKzSu4XAJz-48UoCugrmRVgH1uACMQc-IZ-UrAd4anwWPGnWLW2kWLpvJqHH5E-f8GlcZemsQ8Ug-mbNgGWBDiUkGtmOTCutZqQ-EOn-VVRare94zZvghOhaWavr8vDij4DO8sZXw7Url4UYL5yBKJaNZ3xVFRLcQxNQU-7-qK2zj6E_NM0KfgzU9X2_8BsF4dXxhRUW3Jp61fmPq9DU-4yXpyb-pZFjtJaVou7eJ4UKy0DTCWbDVGUmYAhIUV3T-IIHKcsS3HKKT99SeV2VbhwayaqUPvimw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hn8oHz87UiSD4uFyWWAeW8PuGf-J1UW_2FV5vUPDgYxerMglwG-g4J03sAni4-qh1u5yrdpGu2qbWfKOCU86ZRbg-iwGpaD-9Q1GZ2gmjRzxf_dJrhY0UPqU1dxtFeMf7RTDG_614r5lmDGbUo8u77tXuUfSonOxManmios6Ol48VGMuKgZNlbQ-Mxph4haYzUKNQD-86mqTF7B-Muc7IaqD_1ec6jMwV28zHPND7RUbF4KKYNq2TtE6hJX6MtlF46jQFAdFOAHP63JmsxZeTCExVj6GnwiIdecmVu6rHzuNb8x_ajY7DnNPiH_W2Ub8TYywAgl3EYOfvJokHxYjUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_zxyULqDUA2--f-c44tN_0KSl7XEV5OrMIfWQGz5h1oV6Q9Pyf9ghDyCALa2nUM2kAomFlIxxitT7tFn5dhJJ4YjfYkQymuGTfiTjiNHzvNAscOkbb9nlN1ToonPAB_0EuWVyrVN9lhL5M_O9tO91coYQbgVMFwwCDbdtAUmKoRPim5MIyKqcd3wwCeLsJ0UioCg2x4XR7cm4YjJrqizeBh1x_w5sRFlUyo95orBD1gkeJ3JAvz3krDomR4QslN6qN2uStYAcMgHSWZRcDBW4l66xjqFd05-wib3ek_Oz5hXHzOXmsE2HeeyuTNNXHYBu7JXE-o9JZ9PjdkVZMAMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTVBzCvp80xpeDnhEokjRsqVl2RoBBXzAQdN3gOza_jAkPu_qclZFoTnzBtLwK7QaPxTBmx_GNqERxCAA2zPNyzNYc-e6y6oYDW7SXBEScHRCA91_pqitQavNvoQaw28dEEKWwZYs_kuFj0ER9BRMpBzP5TEh32JwgLMH2GzHmKwYhpt-lZJy_ZhLRnzsWrQ62nteRZC460kjQ7iCzSOEKOwaidbYORYDHagewLfyHLtSWIgKQ2KpzkOeAndFxi22sNmXX0sg-WXXJKHOVldiMa44nqYx9leNbo07W06teNe4YxmZoHS8O9-D8DI8bMRRb2mngMB_OolWMFkqclFyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=JRQc4fWBWhQUHhRry2U2yfnSAzYaceysaOPkLmFdT2uCAaifkPDWez0egxw5tJcVlh1kcOCcREZLg4u3bTD8_WVu_3aCIKj5qDu6R_iJz_05e57eIETQWWZE-RbLOl9ZqH6LS3KBNzY01iPPjY789MGoDuvftZBakSoeQuYVWqUizDbMxtkfTkEr1limfOILua4fnEu0_lBCRYDlVGAFN3iW8ui5fgFIXzF01g7z18NK0LiQqFWHxg-XlDzUNIvIbY4HJyLYkU5BBe42edyihHo3kgqNWQenH69bxj2sV90znbe9n16KiBP6v53_yMf1yQ3-JMk1WG7zRTc5gvdGsrsfGZlIrP6jahs_YIgl5wfO19ZpHpLqTPOwjQLKfV89XFl6s_kFQHfgzLI2H_qxQBihOvlNIXzFEivckjzUIdE0w08kKECWfhUYv1vbpwpkcCubXMUnml0YcP_jwAwEKCw0rxgwu0GYzZ9VJ7OBAhNhrjZYdgwiwgro08sT7_1ReFVTyEKWG7TM1m4wCChCVc6-dSzR-bzHJ5ORkIPqX_NcdDBY66_agEGBlzBjcwoLc7Zv_CpocUApjmmr_El13vDdDckSs4gW3Pry-zLpyskDP0mhbL8pIjfz8YfTSg2n8v2UgRMjyztqj2-bvW43zOfoBwlPN1Qy2_G2vUN97AU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=JRQc4fWBWhQUHhRry2U2yfnSAzYaceysaOPkLmFdT2uCAaifkPDWez0egxw5tJcVlh1kcOCcREZLg4u3bTD8_WVu_3aCIKj5qDu6R_iJz_05e57eIETQWWZE-RbLOl9ZqH6LS3KBNzY01iPPjY789MGoDuvftZBakSoeQuYVWqUizDbMxtkfTkEr1limfOILua4fnEu0_lBCRYDlVGAFN3iW8ui5fgFIXzF01g7z18NK0LiQqFWHxg-XlDzUNIvIbY4HJyLYkU5BBe42edyihHo3kgqNWQenH69bxj2sV90znbe9n16KiBP6v53_yMf1yQ3-JMk1WG7zRTc5gvdGsrsfGZlIrP6jahs_YIgl5wfO19ZpHpLqTPOwjQLKfV89XFl6s_kFQHfgzLI2H_qxQBihOvlNIXzFEivckjzUIdE0w08kKECWfhUYv1vbpwpkcCubXMUnml0YcP_jwAwEKCw0rxgwu0GYzZ9VJ7OBAhNhrjZYdgwiwgro08sT7_1ReFVTyEKWG7TM1m4wCChCVc6-dSzR-bzHJ5ORkIPqX_NcdDBY66_agEGBlzBjcwoLc7Zv_CpocUApjmmr_El13vDdDckSs4gW3Pry-zLpyskDP0mhbL8pIjfz8YfTSg2n8v2UgRMjyztqj2-bvW43zOfoBwlPN1Qy2_G2vUN97AU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9nge0AAev1DfFJpXTLDxa7J_Iuvg2fWNEte1LBspHCcLnEf9Mgumdh4wH4_v16kf7R5Mf-zkzZX2r9wnxNvQmDRAlaY2borJMB-RxfeXwYKOxel65Ly37r4YdRVK7GYk7W3diX4VWbs7svGJga2EEFVw7rwRqSneOa86iDlGGVvBYjnUV2iaVt6gSMTJbuqrv4oGxUfGBimR9S4U0AyeiuT3ew1c9n-LU6Ykz9znIKYq8JGrDHl60uZWNk1Xq-Tkc6-VSXYJhMvoYt1R7IMWSHb6s_Z_EDgl67GFiDlw4IvGR5tQgmvcXldHKxgVvxwPs9AW-BMagA-KUAbO5mTdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=SZj6-Kk1DPMlHHBB8IkLKiLTtuq7ujadfjodJS8Nri0Po_KYxrIZb9oEJE7xSYUmoG9XYGmQ8am39sXJmVYbWuOTVAOWJn-qjZYkB7rzSNRKIfuvVioL7CcpTn_ExlDogWqkfpT6Rf662LF9wVdbZ_2QrV7ZNNdohs3aQUQVhnNBgfwvNCihUclDDrevtZik00xAkKiIYG1HCCrqinaF5DJjqN3_j5XvdKHnD2w-myj5IwFKzRu6Dquf_k-QM0XzkqxYTFPUEbbwPzFKrUwIKHqMTVikrXOaabq5qZwik1Qj080cdYOExy9PN4WC_AV79ET7sZzr_Oq23alJYo-mr4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=SZj6-Kk1DPMlHHBB8IkLKiLTtuq7ujadfjodJS8Nri0Po_KYxrIZb9oEJE7xSYUmoG9XYGmQ8am39sXJmVYbWuOTVAOWJn-qjZYkB7rzSNRKIfuvVioL7CcpTn_ExlDogWqkfpT6Rf662LF9wVdbZ_2QrV7ZNNdohs3aQUQVhnNBgfwvNCihUclDDrevtZik00xAkKiIYG1HCCrqinaF5DJjqN3_j5XvdKHnD2w-myj5IwFKzRu6Dquf_k-QM0XzkqxYTFPUEbbwPzFKrUwIKHqMTVikrXOaabq5qZwik1Qj080cdYOExy9PN4WC_AV79ET7sZzr_Oq23alJYo-mr4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=Ew2LhWmdPFRr0rqHw17ZD4HyUmzfPtDKH9lOt1GJlY50M2RLypCqE4VaLZ4REXwp7Qvx5vxiZN52TinfhGjJpIL4JcrDFwtq934NjNmZyMNVdQslM8KPqmn2X_OzeZITqWfZNWXcuGayk-CeGAFv9sySnLTxXo_eKEYDwSFgvu6uw63Ai1PWk-aSn0Fe3zC0saQkUXnAd_zgVO4BIOPlJTjIEBOraBQx9R8DfC5_j18EuRUm4aXb_5acCdJv9gQZzbteHBMfXkM2NQXx957zG6qBSDEiGY3822toJF9illXEmbuUdrCGKW2n6FUSqTN4OcwDpcUlJTnYsIdLfmK_PpF3y3gSz4wqWiZYUJVSlxzVKlGEkbiX7Wx1t1-BGHgSZgh08n6n3Tkpoyy9kin75jpNFPCYQBTB8ZK-QpyeN5EdIGuBgX2rFj6wp4dt9ih2tE1TWrdXIdCZa-pofZ4n2gN-vV7_P3LAw_2i1Qwz0lcGKGBArVsozKcsegUvvl7VafXTQkwejGw1WUFqamjHDyJAuLa4LIS_N4Y4rGWTVDoEGWCJhQoWcNw1Orf0brfBfnwUVbqLl6s_owIoVEOsdzC2OycsgIqtKmCoiVg0WUJr71gX4IePSHvDvQaiocgwII5hgvo_G-nxzzu3KLwMM5FpZSD7FsuJ8Zk2RI2ANJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=Ew2LhWmdPFRr0rqHw17ZD4HyUmzfPtDKH9lOt1GJlY50M2RLypCqE4VaLZ4REXwp7Qvx5vxiZN52TinfhGjJpIL4JcrDFwtq934NjNmZyMNVdQslM8KPqmn2X_OzeZITqWfZNWXcuGayk-CeGAFv9sySnLTxXo_eKEYDwSFgvu6uw63Ai1PWk-aSn0Fe3zC0saQkUXnAd_zgVO4BIOPlJTjIEBOraBQx9R8DfC5_j18EuRUm4aXb_5acCdJv9gQZzbteHBMfXkM2NQXx957zG6qBSDEiGY3822toJF9illXEmbuUdrCGKW2n6FUSqTN4OcwDpcUlJTnYsIdLfmK_PpF3y3gSz4wqWiZYUJVSlxzVKlGEkbiX7Wx1t1-BGHgSZgh08n6n3Tkpoyy9kin75jpNFPCYQBTB8ZK-QpyeN5EdIGuBgX2rFj6wp4dt9ih2tE1TWrdXIdCZa-pofZ4n2gN-vV7_P3LAw_2i1Qwz0lcGKGBArVsozKcsegUvvl7VafXTQkwejGw1WUFqamjHDyJAuLa4LIS_N4Y4rGWTVDoEGWCJhQoWcNw1Orf0brfBfnwUVbqLl6s_owIoVEOsdzC2OycsgIqtKmCoiVg0WUJr71gX4IePSHvDvQaiocgwII5hgvo_G-nxzzu3KLwMM5FpZSD7FsuJ8Zk2RI2ANJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=Ku1t6yX4Py3NBbnhbWo1A9QpGbqpwwP-VeZrd6OwlJa76ozinG8hirlQ5nb1i95oLotvssDLFIPpXJ4rW262I2QoGw6GSkf6jMSikDJNQ4FHUr54Lf0Hv8DpsS2pT8VXd5XXMhXGRTS-pQBnPdeXki1Sx_jmPAYAeQie3Pf6SitHV-80x213dMBlMH_buipsUorD95zI42Aw0_8egylUEMV3A0hduewatwgq9iRl5dtRYdl60xYAhDqqrvbakfDouKdLfCCGpY2uBwenr3W0J5WlBzGALAOhpK06xAvPQENeeCMQXXe6W3pEGgbIJFs0J_3NL_UXCc45bMxdJypQNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=Ku1t6yX4Py3NBbnhbWo1A9QpGbqpwwP-VeZrd6OwlJa76ozinG8hirlQ5nb1i95oLotvssDLFIPpXJ4rW262I2QoGw6GSkf6jMSikDJNQ4FHUr54Lf0Hv8DpsS2pT8VXd5XXMhXGRTS-pQBnPdeXki1Sx_jmPAYAeQie3Pf6SitHV-80x213dMBlMH_buipsUorD95zI42Aw0_8egylUEMV3A0hduewatwgq9iRl5dtRYdl60xYAhDqqrvbakfDouKdLfCCGpY2uBwenr3W0J5WlBzGALAOhpK06xAvPQENeeCMQXXe6W3pEGgbIJFs0J_3NL_UXCc45bMxdJypQNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmeiNhKPQYNji2XBpa0cxF4WlIwqNcALvJ3y6iv1hxWSPdCeT2NeJaP3U6YwpvTQ7RRuQvkhnP936VGoJSNWpkmT4sewHwWGS1Mt1gZMWNw-rGktqdabbNoCC4w-7T_d1BXMgICkovChdzhsqcXIn5UcBM8kdqKsdYEFn_7mQC5O-DE1j9i3xdFXyYruY-ze_nmN7U-U8rpOFCuHo5HVRMxfsSHJeG6687NJLNqL3JU76wqNoF_hWT23Yc5yXcV24ND90-55cKbm9EzUpNFXQeWDgwE48m3GdPyUh3mdxDoyIT2u_AHypK4xdg9VbFECZ_E5lkr1rw_PHYwAGlRq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDyom87S83of0_MXMaebstFI0bWNGwTeZBWELRs5ycGZ1yW5_agKpXvKjc7DJzZZ0s6sh05TQuYVxtkQ5jvbIoWMGyyNPfojLV74k_OowxA6M9rI7f-lL5firtiLcOLgJrFca6xKH_W3eCZ9S5iB5RFzjixFp720gvln4On0XN7G-SSLh8gnygzas1DtoJLZ3XoSTTtHgAmQbhCV1aSZLnmfoTmGX_smIssv1nIUUhtVI9gAUpOvDjGg1dU7ThQhSJ9k6FeCG9YIBhFPwbSJietkd4y0irlIs1CEmJR46E329wFw39m_N1MpStSb_3naIKN8qL5dToJzOogLSlTYPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiK18EU-HoI8enA9U_oX-f2CD-ynZK4y4plX1x-UbjlSsFrgRnsBkQBrzRPA7cZxENGrvNYlbkqV_zeqIWEeFf6O9z_p68x8jl-gyP2zmpOevZpCSS9wJhSlQygYc_JYjsi331of_rgSrWi-UaDxO_QRUcPrpHtuXiVTbUW97knyLs107HolGXpdr13BgxyHvE4JBbfk6LFl1OMFfLWnMsbgg5lx2GOQaoMbdvvofvn5CDoRhj7GW6qL_bqGK361iRbcH3kNXZsDmt-TWdbYgb5CqN-N6yqeuBvQAfMRgTMMSucbBAXfpNJMnUqPp_HdPC__OjcHWoHGLmDiwziJvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1Mz_GiLkrI-WjJ3bCXCpxmHrM5RLHyaLmI1Hwh5Ai7Jc1obsWr8IpZxPS9i5AjBSuD2f5gvzLf1km51EkwBIqyHweCoY3-VIzfLtecLtbwQmE6JlmserdHp9WlGCxj676C64Q0-SghT4snti-nGszEowGx94Fomb6KJ32PFNKQ0YCoHmyy1jFfgiDWy3RxdXKO5jj-K3o3npNzLqc8e6rwJIwdevwtjWy8tBrljebgjWZC_mIuoTCKsLEEoDlRgfeBwtVa2t_yAIj7NWC7NuqNylh5GORgmxBeTZQHvdv952EvyfJ10c_Tn5fVsbLSxAA_S40fMB2YYkng4dpDDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNHhy3kpEdeUEulAcjw4sXEMgVDz_VSlEEQNebn7NK0b2buz1g1PAHgYAsdwa7GGUnJ4NN3aoKTSiOnb3k1_Kt2osgn85UIDYa7rLhRuPn-nXEdu8C5gEIKf9-7GmJpqM3K9uld6ToAhWWzKCNo9yTLWK-aIfOU7VjUJLw30snKuwPnlTsf2f57or87ipvXwoMvXHSyYJKn3Gn4Mi6RKSwoWuSUSu8jpLIKO_VLUt7HS99xg7uhY_WOwXdN8f5QdCdWpeRo8HFB4CeBW7K72jXgvVFtRt5Y6H7HQ55d5Ma_1Nzmya3sKPJhmAF3r068pkN3prjTvrIxHoHp8GMjrxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=TRNT5ysC0uVzI-6ufGa4spylNxqX-5oHPrzvRtj_9rqHlWRzaLRD75L5i1xi2hOqLwbFrDd24qLtPFd5vHd4jFccvdO7KHFQkbO8ry6lQ-ShRJ9H6vQ3-B3n94ZBB-xVYCvUl57tLkXFN_DDvFoEJSDJEM0ylvdq00-unMyomfi0dIHNpqGBdXWpzhTcbJcFIo15KM_jQuhSpbtNhfG2uKKUsovIE21FmA1JnVqCaVv0-dq8MOJNTFO_HCypXWjzm6lsJuZiIrFUo_uaIg-ObuB2R7w5ODW4cM46nYJUvGpE9Vygf7PGD97Eb7MQFj0yNNmK7vwCLvygz_VaUbfHoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=TRNT5ysC0uVzI-6ufGa4spylNxqX-5oHPrzvRtj_9rqHlWRzaLRD75L5i1xi2hOqLwbFrDd24qLtPFd5vHd4jFccvdO7KHFQkbO8ry6lQ-ShRJ9H6vQ3-B3n94ZBB-xVYCvUl57tLkXFN_DDvFoEJSDJEM0ylvdq00-unMyomfi0dIHNpqGBdXWpzhTcbJcFIo15KM_jQuhSpbtNhfG2uKKUsovIE21FmA1JnVqCaVv0-dq8MOJNTFO_HCypXWjzm6lsJuZiIrFUo_uaIg-ObuB2R7w5ODW4cM46nYJUvGpE9Vygf7PGD97Eb7MQFj0yNNmK7vwCLvygz_VaUbfHoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9ZZOa2roceL4sSFEYD8fehdxN2Zxk9esRy1g9KZPWyDLhss10nQ-OW93ggSEp8vsaMLTuVsJ5lZxhOZc0HY16zGRqJE8TYZN2pKKIyNd-e4SHIfroMkYNcBPY5w89GSExhqn2zmMJCvCVzNJI588iXPR9mpk8CjxO61rRcHGVy5MYjR-iwkH2Z5S72saUJ-vIUOXx8Ed44wJZxVg7M_miyTLw4nMtumDu972IcU-EOTitMjSlgfSdwyi5VgNl03NrHgM25gb2JSE7Qa01OB0GfNQPXosErKakj9i_ASpkuCyUVdU576tRlYZTaWDmI8IC7U6mfGXrI5aHKQiXerPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwgR18xOqUEMtL-Fb9G_uRxAXs_eMBHxujC2PKvb-R8mPHv_mLvPCnGrvEOQtsclyirlLNt5myf1AFvnjPRbal2C5Th5AmT3MFdJrSiKULUkHFs_W_hVwwu51vCknrz_bSM8D_FbutxOFBFHVocYQpB5yQojvfNBJ_G1nOp-oneluQpd1_ysSxvcqQNlVkt-sz67bqlLloRYtjsCYfgiA8W7Sw4hArWzqdX9omCTVORSLRw2xCxutwoRM2-LkudRAe10VZ8MJoM58dLjSfSwca1PYD6X-Qbdl6tr8oGjHCfiTlvdVVS2wXzL6ZBm9kktZzJkEE3-kvbjRmi5ncUcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnYNV-8rKS3514uafM_f1aEGS72RetNjL9VGEWRRROUWoAkh3npB30g8CSR_W7AhmaT9R7y3osTFuk6_lQvg-kfVczZbAXTAGM1sD48FhNHRwJU0QVFbFtS_QxN7XriI-Bkmkgf7WmG53qsO5HodmK8HcCbh72wztrFdJhHZAOlcHgU4LGi2DCXkT8QePyRZGZQV3tCooj-86PAgdJdlX6H-a3NY4tAK281PCQhxY6Oceg26bMbFGCVLMj81EYnGpO7vLEQCgjJ8NtXYPVjCQGIn0Gl2uYDTQx5o2MoKQMNbyC-RRmjGqq7cQbVeFLtZ297OJ2e0bPrJSMW1XakfDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC40m03jqylvxMQdn5mnUvBJJAO9QmHux6C2oDKpj-EzAGU3yBSMagOj8et38TLqzEr3kuCPu5dC-Jtxvhon0ML8O-5L_fF4r6BPCmVnJcHKXP3TSomzDdokWWdrdUdQEbHqaRgznfpmwfGey5CGZ1P4F3AMOLWXRCXlo2XuoA6LUUjZJXA9GB6S5AAdmvxLeVDgyBZBtrDZWvTwSyR6g2MZLYUeM9_TyXozXkigu747_AbpscTDp3Tkv7QnFxxCi_wjn_ar2NBhb4aG7cnZ9902PXRzYZDVJ2J08au9EuUA--khKsAFv3yRo5odAywQqJKP1m3MqHBdNon34N9Www.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAC3bdRnFgKrc_YdSGqTNJzFWsDNeNznk0b0t90zzBzxcfki4qtnzAGW_ZJcAR46lwwHWsUjFTOgfEhChh2G1b6V4bQ-J6ylr0eqO6jySRzVG5-sNBa0vYNf7lW--j9xYGYaeiAG-5PI7afN5QqMiZVKNCWAAOZZC2SoNV2cQ9uHSktMS24W7yJg58xg3lxubFnbd-q_Lg-CUe-ZOtkAPB0Xps3lKYMsgLSzmtaA1FaWMPe1yE-_qnuCovhnkef7HJrihHlI6H708pzjasGSFOf16QCeSn1dvfOWv8cpkBqDaW5EcOnttOpO-ubY5nvXc1vPu5t8NZX8-zn0CDM-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OtCFYijBHhoZsKLBxpVPFSMgfbPMRwM60PFMQxFBXn4_jEQOUZ5_poYs4XljP3Nbb8kYHxFJB_fFwxQURK0wXAbIHJCE6k9d17lvcvmy8SqF2povXZrazy-VcV9nR8G9_t6AfRYtYuzerspZAtxfc0TluvkAoZXwxobkPo2G4YMQb5_aXQ4Qqv85DSaElg0SQU4eqlPBLOrUyTrbBz3pPZc8BKqp-G_rZdm4Lk_NPV59cNowCbn3NpqgxtTjBQ1y_4PRPdSsmFTxE3lxuI4WFN9Q8S3QUoGf0Z62ie2nvJzfc8bwC6mPOQDmKUlTN3ywlOIO1VJcm9L6Bqks-G82yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inGkOSsok2xCOUbVDpBG3ISTsinOYBCgxESlgHVLEthwIAt83LJvIpAvnCY71f-a4RWZ3KVQcpJghCWYstuaUApqjroKrW4fz2BV1vLDpNi28Yy958hAq4KavVNSpl0HhErf3LqXSF3Tpq3fTx5Pzgmt6GoRbQLyYdDWtulahEGmNJhwY9ZTvH9a0xW_aGaklVz-cbV3vejQdbc3X3wst01-Q9WAr7qRnVXn7RS6d_Ah3H5k6b0FBQVV2Hd_datFK3IZfdu87qEplf4ZhW3GRO2e-Oh7L4C3XhtismnxfHDzjqfPEh9wG97k80yc5v3jlFBN_eVgVkNwRsLG1-Swbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل خبر از حذف
«علی موسی دقوق» از فرماندهان ارشد گروه تروریستی حزب الله لبنان داد.
علی موسی دقوق ، بعد از سقوط صدام حسین، توسط جمهوری اسلامی ماموریت یافت تا به عراق برود و به ایجاد گروه‌های شبه نظامی شیعه عراقی دست بزند.
او از ایجاد کنندگان گروه شبه نظامی شیعی «عصائب اهل حق» در عراق بود و در کشتن ۵ سرباز آمریکایی در کربلا دست داشت.
اسرائیل امروز با حذف او،  پیامی چند جانبه و جداگانه برای حزب الله لبنان،
جمهوری اسلامی و البته آمریکا فرستاد!
فرمانده‌ای را حذف کرد که نقشی کلیدی برای جمهوری اسلامی و حزب الله داشت و آمریکا نیز از حذف او، نمی‌تواند خوشحال نباشد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWaMrxGQfEfQx0hhxYLm4lL2Y5OpTjT6VbwVfk2mOkD9Lj4y3qi1bJMwPrs9-Hu20m7WBp7PafNSWSFevLNnrEo1LA_fn4CDXFRlLH1TXYZNA4AYRebdcsjOaYptOIjWu5bqQa0Ntts4mqoyV2E2HANWSdePu1kvzpV0dH_NueySaC_uZef9fFBL0YJmpXnkZjN9WqtNM2cM-xBxncGt64uN8joGgSBiWaa_s7Z_6e2ErsKS-5HvpM6sjF5lY_h8GpaZn_vt9Ptnon6vcZ3UkwqHf5tA5UZXSK8xMLSu3xCyaqBdLXuLc_mZJW9QVKbGCk-kQHCDX8-6ywoY0Ctfnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=vjWyF3Ud5J3byuIhLVK91xhNdkZ9EXcjLUxKw11arszXaRG1oBUL4zO-5t0K_i-8LhCfHb4ocF9-y1c83nzPlM0i0_ZzLoKr7wP4n5_QDamyPNgIH317AQ08nNthIp27JXoBbLbcjk9JjlF60YlG7Oj6joSC9ixh0csQxCNuz0bZ6f0LUwtYCz7ze7bWchEotFjMcSZIjz9sBWbctPytoth95jK5C7eGCwo5JxlAG43JUKDE6Ebh20UCN4lRNaP7_yzfxzmNmgMcXmFr82gTeWT4g8kHoR2htu_mfE7bCvbFZThcjUPay8EQt6pbcRxVdStKIVkZ7I4w5eWemBMKGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=vjWyF3Ud5J3byuIhLVK91xhNdkZ9EXcjLUxKw11arszXaRG1oBUL4zO-5t0K_i-8LhCfHb4ocF9-y1c83nzPlM0i0_ZzLoKr7wP4n5_QDamyPNgIH317AQ08nNthIp27JXoBbLbcjk9JjlF60YlG7Oj6joSC9ixh0csQxCNuz0bZ6f0LUwtYCz7ze7bWchEotFjMcSZIjz9sBWbctPytoth95jK5C7eGCwo5JxlAG43JUKDE6Ebh20UCN4lRNaP7_yzfxzmNmgMcXmFr82gTeWT4g8kHoR2htu_mfE7bCvbFZThcjUPay8EQt6pbcRxVdStKIVkZ7I4w5eWemBMKGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=Z8m6nWigoivIqEQgFny38Oyt85tyv4nfl2Bq22WSRHPw1NNdMMAqMWjdjmY-2OdaAdFDgD58Xu6-Ndf80Xn7QN15eov54qkJxfonJzl4xFMN6trwjdY9Gn8iR96tZ8pwhZ-XbePBAw6cbhuHPgzX1IsdkOQzXEA_oYtP1fcA_Qjqb5shpy39mLopgwQXXyA75Li2Bm2re7Ut-TOur2Tq3vk1eb0W25EKkelbXs4ebXjJLq1SAs0fiokdETh7O2QDXKEh-LRKNeSNnUCeWP0oKxORx4mJLX32vqdNEulER-7krPJMoKpF28tRUKeod9cncb_MO6bPbgN9PQ6i-LM8CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=Z8m6nWigoivIqEQgFny38Oyt85tyv4nfl2Bq22WSRHPw1NNdMMAqMWjdjmY-2OdaAdFDgD58Xu6-Ndf80Xn7QN15eov54qkJxfonJzl4xFMN6trwjdY9Gn8iR96tZ8pwhZ-XbePBAw6cbhuHPgzX1IsdkOQzXEA_oYtP1fcA_Qjqb5shpy39mLopgwQXXyA75Li2Bm2re7Ut-TOur2Tq3vk1eb0W25EKkelbXs4ebXjJLq1SAs0fiokdETh7O2QDXKEh-LRKNeSNnUCeWP0oKxORx4mJLX32vqdNEulER-7krPJMoKpF28tRUKeod9cncb_MO6bPbgN9PQ6i-LM8CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=JvvHME2ediKxeOWRfafL6nHVclyrpOR53WuoNMaSo-YzsJw3Nb6XqCr0K_RRkJQQoSfgg1p0tcfaIFmvNDRJM1t4ixQkm7IRWkJjeDE4naRWrsQHFgBke9iVd6TGM_GEp6F7bD91Yvq95IYRFnOZeKgYe7i-5MpBGCkXBvgWLMEmgubK1yYfrh9b9SHkF50NwQYpNIFcTLH9bbsJgp3OSzN1FPil08rYjYV_47UOQP68i-08xQiPUjjJo42BwJx1fmV24wtUYveqLZu3M5CDwGZeQxmZnDsaAx1eIwKYLic_mtqgzo5kNDBF13Le253poSuVi-fXMFz918y7POs0nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=JvvHME2ediKxeOWRfafL6nHVclyrpOR53WuoNMaSo-YzsJw3Nb6XqCr0K_RRkJQQoSfgg1p0tcfaIFmvNDRJM1t4ixQkm7IRWkJjeDE4naRWrsQHFgBke9iVd6TGM_GEp6F7bD91Yvq95IYRFnOZeKgYe7i-5MpBGCkXBvgWLMEmgubK1yYfrh9b9SHkF50NwQYpNIFcTLH9bbsJgp3OSzN1FPil08rYjYV_47UOQP68i-08xQiPUjjJo42BwJx1fmV24wtUYveqLZu3M5CDwGZeQxmZnDsaAx1eIwKYLic_mtqgzo5kNDBF13Le253poSuVi-fXMFz918y7POs0nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=llQrRn3M7sD70uH1ZdIPfdlG-52ppFizU-Jj-ONNbt3I1qAvGEdpCYD_UxHcBfbP5ilD00TbMfmtm-lLAY-ZLLOy69p0bt-39c8LvaK2Tvio27PJ27gAz-T2483BsUA5KIDjCgbk8BaoPRiopPzqSJY6uTr6mfh3AoMZSwmZnam6Pm19fPNIoK_m9qYSYoa8nB-JZxp9VMzyJkjey_zNbbUK_bEwak0kle6eUVSiuNHq7VJ1AdXpzOZ-cDgNnMMx76xY2m5lyT4_FUW7gEKucF0sgyhaQbM-pKS6Lq0__n1S_BFfhBs15CXNiV1oAcKTcsOgy8PE8Nvsbwalih0QkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=llQrRn3M7sD70uH1ZdIPfdlG-52ppFizU-Jj-ONNbt3I1qAvGEdpCYD_UxHcBfbP5ilD00TbMfmtm-lLAY-ZLLOy69p0bt-39c8LvaK2Tvio27PJ27gAz-T2483BsUA5KIDjCgbk8BaoPRiopPzqSJY6uTr6mfh3AoMZSwmZnam6Pm19fPNIoK_m9qYSYoa8nB-JZxp9VMzyJkjey_zNbbUK_bEwak0kle6eUVSiuNHq7VJ1AdXpzOZ-cDgNnMMx76xY2m5lyT4_FUW7gEKucF0sgyhaQbM-pKS6Lq0__n1S_BFfhBs15CXNiV1oAcKTcsOgy8PE8Nvsbwalih0QkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=ottc4gkRagHiX2RF0DllJZGlpMOBlBQmYF93RcZTzBHHSN-QI5r5whrq7gxWAyfUgc62OKvfedbkLbWFqVfDe74_YO4SLO1S4hEZRbEtI7MSRVKuXxd4qtYS8dLPKBaHRbHDOjgjnncun9fa3erTARoIBxeNi-UiCVpQw87NPaLivqqoBgmsvvHqQdZrR3LqIDAZC8q12WDWTC3HJ2fMiSRRxV5jkDNbTarbj3S1jfWpIeK-ExHelFpNHahGLEB5r8gB_nGmMYjki1NDylo-sauNTi8z3i3ePgVRQCoXjqBG_ebN9Vow_cBzNB_z4tCMpnpW6j0TCTc7aDcjkh_2yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=ottc4gkRagHiX2RF0DllJZGlpMOBlBQmYF93RcZTzBHHSN-QI5r5whrq7gxWAyfUgc62OKvfedbkLbWFqVfDe74_YO4SLO1S4hEZRbEtI7MSRVKuXxd4qtYS8dLPKBaHRbHDOjgjnncun9fa3erTARoIBxeNi-UiCVpQw87NPaLivqqoBgmsvvHqQdZrR3LqIDAZC8q12WDWTC3HJ2fMiSRRxV5jkDNbTarbj3S1jfWpIeK-ExHelFpNHahGLEB5r8gB_nGmMYjki1NDylo-sauNTi8z3i3ePgVRQCoXjqBG_ebN9Vow_cBzNB_z4tCMpnpW6j0TCTc7aDcjkh_2yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=v_W4DgXY_Sb5lnRB9yME0UC51XRKiSVyg-0d-YdeI368GJZF6xmml5i9gSiApl0iXaeS_bqrSp5-pMPu98eYCmQDjhGRfvyIqIIocFz0GmSXn_RLqhwFbq7uBpgN4G1FuEHakvw8JObpohPFAYfW_GJOCXqr9M2xGOmKQvS0w6zh9_OBKRIuKsJ_KZx4tTd6Y7ddPuOeZKmF77ZZ1u-ftiv0SJOKo3uIoQwOWEyfq4_DaHif12Z6xlx-BMqOJ-wHnPW8myRUghu2R2f437jwfewkwqPT2N2oZ14MEK2yDKfbjhzn3WzK_NAOcMJny7ZEUFLah8jx-ZjsEF-6oNh2Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=v_W4DgXY_Sb5lnRB9yME0UC51XRKiSVyg-0d-YdeI368GJZF6xmml5i9gSiApl0iXaeS_bqrSp5-pMPu98eYCmQDjhGRfvyIqIIocFz0GmSXn_RLqhwFbq7uBpgN4G1FuEHakvw8JObpohPFAYfW_GJOCXqr9M2xGOmKQvS0w6zh9_OBKRIuKsJ_KZx4tTd6Y7ddPuOeZKmF77ZZ1u-ftiv0SJOKo3uIoQwOWEyfq4_DaHif12Z6xlx-BMqOJ-wHnPW8myRUghu2R2f437jwfewkwqPT2N2oZ14MEK2yDKfbjhzn3WzK_NAOcMJny7ZEUFLah8jx-ZjsEF-6oNh2Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVZ5voESNF_jr8QWjRRrR98AbZTVzR_nTh0RgXg367F7DPYy3NLzWoNDXQQ5bwKYXzr6zFcjR8TiX1avbIYHddzTg_rXl7re47OY7svkwR2vzLfRJKCK_EaIZM9EMQkIceElmreWCjymfZ546fWAeMgBvZ6eO4z95UrzXtWjyg4bTvag0t3AaE7cBRSDwd_9L83q9QqceCXl4mbkAWHAE-W33iWCCITHg5KqgFM0qWMUD1h0QpykQ2skQi56PfDemex96Ue3wL_a-XrV88ysiaSbfzCoqulUwWVCaUqb0_-oxWyK-LqxWoBFxCe-S1PCfigkZ7mjyrhPIpXnHWkOcKjs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVZ5voESNF_jr8QWjRRrR98AbZTVzR_nTh0RgXg367F7DPYy3NLzWoNDXQQ5bwKYXzr6zFcjR8TiX1avbIYHddzTg_rXl7re47OY7svkwR2vzLfRJKCK_EaIZM9EMQkIceElmreWCjymfZ546fWAeMgBvZ6eO4z95UrzXtWjyg4bTvag0t3AaE7cBRSDwd_9L83q9QqceCXl4mbkAWHAE-W33iWCCITHg5KqgFM0qWMUD1h0QpykQ2skQi56PfDemex96Ue3wL_a-XrV88ysiaSbfzCoqulUwWVCaUqb0_-oxWyK-LqxWoBFxCe-S1PCfigkZ7mjyrhPIpXnHWkOcKjs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8RPrb1kjQaIyUyuQCCyF1Bj3d8K9vIW_rgmor3Gk9XLTBAcStWV2zm9-N3tqUWfGUq9BYlWmxQn7y_OGZmWtlKBqG3yMn-zlz7KzOB01xYQ6qw_8JHKuEEeBhuekiBmLJVlm3KEqBiwWTh5kk-vSl8ZQ-1UsI2HBtGKyMj_B75C4nTL0-lx_kOYPMhDJRzk0GtVnffeyIsmJhqt-LQ8mQMR8I10cPfMk_hPHdNtkIWran2nN3L1-S8uV4-x2qjHvtsDxY6ux3f5iWGQ3djOo8LvspfQMCcCwLV8FEkpJ2mPHB_Mzjj3mYjqFSwxC6rmZAvszOD9mhQ3hfcZlH-Enw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=J9t4M9alV_CitEuKrftPQhBWPadCD5VYCyByDNmksQRd_-QwWyZmoI6cgV5fnbvHjrRhzdT19PPHr-ayDHj9d76qIKcZuNHpte-8X93vZ3Bt55qkxjCjuOmA5V4Wp6c2cjO9xfx-AIlAC5gw9gz0_cs8yxDVbJDTQZaR44hbe0k9LLi2eELgFtEgb3FO4ZFrEI5SDwhJkP0NQvNnf8TBruf7_cBeyhvY16FZO_GfMOrPc_aJ-1R82yGegbOcD6TXa_iNiazD6eLyur4vg7krPCrE45JqeRH1KqFrcoKffCYJ7u9c_sjJXvrcAWtIA71UHaZq_yohAaNqmJ74MLXPug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=J9t4M9alV_CitEuKrftPQhBWPadCD5VYCyByDNmksQRd_-QwWyZmoI6cgV5fnbvHjrRhzdT19PPHr-ayDHj9d76qIKcZuNHpte-8X93vZ3Bt55qkxjCjuOmA5V4Wp6c2cjO9xfx-AIlAC5gw9gz0_cs8yxDVbJDTQZaR44hbe0k9LLi2eELgFtEgb3FO4ZFrEI5SDwhJkP0NQvNnf8TBruf7_cBeyhvY16FZO_GfMOrPc_aJ-1R82yGegbOcD6TXa_iNiazD6eLyur4vg7krPCrE45JqeRH1KqFrcoKffCYJ7u9c_sjJXvrcAWtIA71UHaZq_yohAaNqmJ74MLXPug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr1d0XRai6iK1aY7YQm-Shc_F1Iw61XDT3PwioJiUC_0mAwBW2KE5Oy5fJ9_skprsgxyRler1bL978JrTwCcKlyUPI58lKsKYvHtjNFF3TJPRRzYX06zCEjrNKJGLOiGeQEeRvwNo03Ia7mlGIFecDpeVsIKegEhJNY5AgWXafcNbAyBgXhpcDSraBScbi9Uenws3CImFSS67otTGjEJCXPGdv1VL2rSo4upevF2Joc3UjXkSaEOGhFZyc8hqBpen5ANddGEkwJSJ-f-J0p9TxaiS9eM0Unqq5Cb6SZOvXFSjfsx2jw9-6N6GXP-RqfjQJx5RP01fsX3pv90NA-MRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nqpz7PwduenxLwy3bVSHsOILRf-mdaOUfETuSmmupFaDVv2D2B3-SEfv7iEGLy6EfisnXiXXN7nV2ubDcOkGV1Jum7-nJKOOcTfJu3WzH0NzwVqjIYfM3teD0MAuWNlZL_guqIZ9NHUlky9gLSelLjJUuXinLfY57_xDp8e_mznQSmfDXUFmEcNbvaMVc9IGllc-DU_WPm85VaovzLRU3BV_WXZQzwbAXZtVSFdguGDA7cpX6PTHb6pdgeoNuew8EoyhRDnUgH6gQPIKGp7KnGxFzwLHLg_YDb3blSoVr-IxihhJhzrs7RIzVhtrfP4g7MKxieuW9Y92mTwVgWMBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvFbrAOIpUEPH7R6l6Kc-BozZjqpzTZa-rbGLM_j265-5_ZgZ-V5i3upQovGkeW5F92zSvScVHzRkq-2-1c3UppFPrGZJY4qKQjJyOkFbkXnwtTp_n3CELyok4eOY0Pb8Ztbl0XngrGL-UUxn2ZPYuIyEkxctkh-A19lemGTnZ5deftTLcw2jYbpv5kxLWZy-Y-A093mY-Z7RxFiDBB8vHCJzYQXE9CWy41r5CxXe34K6y152_NaaJLwzNVV6mnjVHROyb2dxAjBdLiP-XeftadPCNB5HmNb1FlqU3-uLpZ62u9mOSJM3U3ku0BxwHOHKFhEGqH8G4OwKIJQcgqexw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=QvkR2BneN8g79Aru981F2RrgSFvZcqwDfaDpTOYPuUwnIo9IzzRw7uS_m6iJZR57zdMW6Yopgf_JYFaEQtw4yLwUVhl6dI2P0WkD1I4BNEGkOzQiK-SfeOIGo1rdeJ5IP7UQ4646pXyQpWFk3wW7izdb98d8wUL0fLOjZFGlnwGkBZb-JZqklobz9wwEWwYaQc4qi2tkeciwI7hovowZ-ncvghBNQ8EJvEsOdiRz9pEKtclvFTgW4L84ftmhadaGGc9zdIprV-PQ4vAkOltUwB1sd6n2lpo1xmNeoMiHKwo9MJOYHIl8MUQXpH09w2EoJvn7VdJSkipzyHno6PB0JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=QvkR2BneN8g79Aru981F2RrgSFvZcqwDfaDpTOYPuUwnIo9IzzRw7uS_m6iJZR57zdMW6Yopgf_JYFaEQtw4yLwUVhl6dI2P0WkD1I4BNEGkOzQiK-SfeOIGo1rdeJ5IP7UQ4646pXyQpWFk3wW7izdb98d8wUL0fLOjZFGlnwGkBZb-JZqklobz9wwEWwYaQc4qi2tkeciwI7hovowZ-ncvghBNQ8EJvEsOdiRz9pEKtclvFTgW4L84ftmhadaGGc9zdIprV-PQ4vAkOltUwB1sd6n2lpo1xmNeoMiHKwo9MJOYHIl8MUQXpH09w2EoJvn7VdJSkipzyHno6PB0JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbOD-1WWxiabwW-W67Pf21dbOBulPZsBloYYYAOgAMA64Rq7jJPZwGQTnoNuKkuYnee1Nd9gKp2CvOiS6KDyJFQcdSuNopuoBUMrYhQrfOX4hud9t0GKw5cN3rk9jLp0he1VheNT5pVyHOpcwcZ75EERQkxqH1HJGri_M2nn_HKdXeVTmdeeERxpIVJOIjGvlXroEcoxFAUVIdWgpQmY8nUbXcLjGDEzy4hp-hlh5m4Nh0NXSMn6_M4drR7xA9EM56AheMKp0S1TMHe7-Wnv_yH27wIm3ORIxw-2-wSiAVHKYYzOefnKnypgFaNasuf_fwPnXKWlMivZlKMO0gd9Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRMdkGFOil27JVuda28-g4-3-16EtrYMQUtqYHzxrNajpzuMERIIAvNWN0Cy8qsRiFklfwFIiYHREstMlfok9HEZo2uoPcA_4jb7UQ2j0YZqDbxfrPFWVPHud2JY7TUWRjnbTMuQA2tJQMWGjb8tY_ziDM9mQi7IVhDYYTVkK91T2lLXXztm9TpljWuyZVZ1xq6eYq_okhp88Z7_RyeQxHV3ARhuKMZNQTkJTTHXKVBIVHRe23Mvoh9W9wEKgX1XWNSTSvoD_mISS_ZfZeb0oJ9-0CGWA0EouhA_A9PrI37EP8HThP93XnNslJv3KwZZb0ogo3o2wgQcwN635w50kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ofruz8RvLLgZCN2inXr6JtLEBehqy0ITMZnxDE1eZ4FJJd8VNJtFEjSWnlcUINVpozcmP0VFX-etNVvGaCcxlQMehMHsnhatNVgJGbPakyNkjXGBDGlSFQHr7YsADxUfwJwraY_nIJi-iwK9YI1oaqyb0r8Qh332s3EZmQIBsZ39iJtiEQ2N_5ANWayHfA_53O8CxMgqaBTbavYNEV_UyBG8aYvNVeiYKE_1YK-_QTRv91VBwVMDl8_17L1Uqcwc2CAoB4URubQ5tRPLt1KvoZ0xx4-ZKc0fnteu2CaXI18QlXFKpxGA6sU_0agrmz526RvtLksb9_uj4xUQiAhQAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8PUA1FV_XGF0vekhRtlNZ7LFBWQrLoplkVC3kB_O2HMPgSAtejmunWf_xgSiWwpThOJd8cLK1uZ8_ZRjYqZ3L_2-bI88eXE_bvZHJq9SWFKwBIhisrftxPkGgxjSo_87QBudBlxVlzxL2THs3unuJM3VX4HfvtNcA_V0Oy0H-Trh5gBkeqnenG4qtu8rNUWgFXmGOOtNkuecG2lyvsgXTxVnRzv1-4NjUiIIShg9JOrZcSlnezOBv4p7sucR-vbYvIFv7_H0BXNVDaBjGJeXZij39z7y1opOvqV9iIF2OXkRiqzU0Yeeic4BaduCxcQOWzhg9JONvM-bO7CTOjBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=vHx1gIoNbA5HR8pi7obyGJCzvKYByL-j0cLuxv2WTEKz9b84N_SfPfSAlsB-6YW_O9mG84yoWNW8kjkoeNwAIeYLpNRNw-dmhVZU6NTnRmJ60hAKwR-3x4vmOTlMJHKbJPnaw-2gz4RGbFd4MiKYubKM1TlA4PkJfWqiQ2Bi27tWdhid_TTWyGx9LfHakJAJamwMtp9TGDXiu2_UuN2XimJoHnTBpHpmuMEP7xXv6HEWvhhiw3-voB6tLbivqybtjQcIrxcfIOtHcu7bqoJhIhL78lkC5yME1BV_5CX4COCH9Os8a7dR2UytkiQlbBgr6mpfTX5WFaoQ2QTw35MtxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=vHx1gIoNbA5HR8pi7obyGJCzvKYByL-j0cLuxv2WTEKz9b84N_SfPfSAlsB-6YW_O9mG84yoWNW8kjkoeNwAIeYLpNRNw-dmhVZU6NTnRmJ60hAKwR-3x4vmOTlMJHKbJPnaw-2gz4RGbFd4MiKYubKM1TlA4PkJfWqiQ2Bi27tWdhid_TTWyGx9LfHakJAJamwMtp9TGDXiu2_UuN2XimJoHnTBpHpmuMEP7xXv6HEWvhhiw3-voB6tLbivqybtjQcIrxcfIOtHcu7bqoJhIhL78lkC5yME1BV_5CX4COCH9Os8a7dR2UytkiQlbBgr6mpfTX5WFaoQ2QTw35MtxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز میگن دشمن جمهورى اسلامى
ايران اينترنشناله!
همين چند سال پيش تلگرام دشمن بود!
حتى «روح اللّٰه زم» رو به خاطر داشتن
«يك كانال تلگرامى» ١عدام كردند!
توی صدا و سیمای نکبت‌شون هم گفتند :«شاهرگ رسانه‌های بیگانه»! یک کانال تلگرامی!
قبل‌ترش وبلاگ! ستار بهشتی رو به خاطر نوشتن در یک وبلاگ کشتن!
قبلترش مشكل «روزنامه‌ها» بود!
چندین روزنامه نگار رو كشتن ، دهها روزنامه و نشريه رو بستن!
قبلترش مشكل راديو بود!! دهه ۶۰! امت حزب اللّٰه بیاد گزارش بده كى توى خونه اش راديوهاى وابسته به دشمن رو گوش ميده!
تاريخ جمهورى اسلامى همين نكبته!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mymAhNkDkjCinvvSPP0iRXwuuFFnlOUfr4aerhmI9u0rqp_BqxEgy4OE22bOJxJ9Z4nJgDNMZzx9efWlsquFDShBQkaxC4YOhF0mCjqTD7-wMwLGb1J4ILIXXWogSUUxr_BH2JF5cuRzIh45CxtSX8Nmgf2arKT7VEKEyV8r369tt5kk-jiNlHvMWKUDf6IzbtwsjCybbBA5zKs4QWnsNYC68U0H-XyibXwFGyWbcvo8ZbQZcnXJM37OVzdJxDkyHjiV-skEe_Cu4bpnm7EBDZGC-k8Hxz2eiHDI1gCBf9d4kolyqf-kUF4n38n1U80cCmqoIAtuUm6mHbQVVxeX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن ترامپ میخواد ۱۰ میلیارد ،
۲۰ میلیارد از سرمایه های بلوکه شده ایران
رو «آزاد» کنه،
و این رو همچون یک پیروزی دارند به حامیانشون القا میکنن،
جمهوری اسلامی بعضا سالانه
۱۰ میلیارد ، ۱۲ میلیارد دلار تخفیف
نفتی به چین میده! از سرمایه‌‌های مردم ایران!
اون بلوکه‌ شده‌ها توسط آمریکا یک روز،
دیروز و زود نقد میشن،
این چوب جراحی که شما به ایران زدید
هرگز برنمیگرده!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDDj3mSruwx0khH3hJIT4j6LZiC1YJvGBuC-oxSAukD1nWHd00i3uXAEl1rB9aXkpXM4_RAA0unC8EC3JZhjM09cBxp-5Y1aJ4OK16EoJH7l8Emp6P5c6pp2MDhyDpQmpetwlGZKZg7iskbtHkD291hJ8WBdBzPVxFwXraFR-qfapotFhqG1Q4JHAWSfyn7MLHfsUx63lyscl7L3uO23gRLU2CT3XKh6JV5jlgZ04z927JM1dwsXbJD7UhJzNaDlrELJwbxIfuNsg_0CRz59RT0LMN_DHTf0RJNqcxDWNiI_estMlgpzj7RZFCcrahuewDt_lHta9fDuk7TrbvJMNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=kyxX0uMhGh7sUIszAmkYA4sXsTFu3Dwi6p0OkXoJM4_OcJF_PxRyBGVzCTPMu_8qfCxDo8ov0U3ElGIfNmrE909w79sSzM8vgfAuy5ck5U8GTeBpWLDdNWMaC1e5qvOWMNObYxvuBrXTVC5gvNtulsouRB_V7hsev3Qz6NBbz6eT0AnI_A0qQIRoLPscPxdA2DnHy0TEDVjCOhrXgTnJO8-Y606RGH86zWJDtVjS0qbOFVds4StWbXbjtZMdsdf8s5fqSizQ9UNgrlRhwW8ySVJLv_DpR-xHiaXaaAxBiMdTHuMUJt0fkL8GuklXBxIuqSv8VMX5pW7Zht_3gW07hbX0iu9_grdXcnapN5785SZ7rdt0DLGlaoXymPY_6c33zUDPb2yuHAIAKMHNdbN94viX_b0Vxlg7LRv-pDq1Ss9ivF4GZGn5oTs82Kb7eHcAIUbog6EgJQhE8ISguH4JZKMYGMy6gbM6cDEF1vYAZfSpKaLD7TmXvlprMJKuFZHP8NjJekqWBKgY1tiPyYVUsr8AmLox_mDnxXV94CnI15bB57QKUZJV6Kxz2JqNejKCgvqf_lF7RwxQ2PO3STURGnEP4K9zJsawPmuUFL9fbyMI-fio41mTKLPfJ7deEx-lRednYeiST0j9NkUeDvs-xRulu7_-XPuIZ-8tgaT0a68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=kyxX0uMhGh7sUIszAmkYA4sXsTFu3Dwi6p0OkXoJM4_OcJF_PxRyBGVzCTPMu_8qfCxDo8ov0U3ElGIfNmrE909w79sSzM8vgfAuy5ck5U8GTeBpWLDdNWMaC1e5qvOWMNObYxvuBrXTVC5gvNtulsouRB_V7hsev3Qz6NBbz6eT0AnI_A0qQIRoLPscPxdA2DnHy0TEDVjCOhrXgTnJO8-Y606RGH86zWJDtVjS0qbOFVds4StWbXbjtZMdsdf8s5fqSizQ9UNgrlRhwW8ySVJLv_DpR-xHiaXaaAxBiMdTHuMUJt0fkL8GuklXBxIuqSv8VMX5pW7Zht_3gW07hbX0iu9_grdXcnapN5785SZ7rdt0DLGlaoXymPY_6c33zUDPb2yuHAIAKMHNdbN94viX_b0Vxlg7LRv-pDq1Ss9ivF4GZGn5oTs82Kb7eHcAIUbog6EgJQhE8ISguH4JZKMYGMy6gbM6cDEF1vYAZfSpKaLD7TmXvlprMJKuFZHP8NjJekqWBKgY1tiPyYVUsr8AmLox_mDnxXV94CnI15bB57QKUZJV6Kxz2JqNejKCgvqf_lF7RwxQ2PO3STURGnEP4K9zJsawPmuUFL9fbyMI-fio41mTKLPfJ7deEx-lRednYeiST0j9NkUeDvs-xRulu7_-XPuIZ-8tgaT0a68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=N7ZcjRNvzXnJShXHF1aws4sNDfJVMhwbXPYTk7q7V3ko9FIaxiI97EP0t8P2VgiM5kHt5wRiGcXWYSIoSkvJ1VBZjIvpIQ5CHJ3mQPoRtPaIQQ20HJy2C9EWewWPU-iaEQxXpHWjbrLKZKVfP_GcSJocXpdSxh-lYAo2U3fne8TqlscTyZyKYxFHrc5Rgbrd1D1KhFQXWyUeGxSnZP7rmqzZBZaavZFQ7JL9BxxRwrlUox01WXmZhuQGqmttQCk9nIP9V5MsFRpaj7GjN07joeRU3E89pVEEx-Btabg0CBqYLPeu6huFz1UlUjR7j_H1YqaTA-1Nxv6M1V_ILpmC2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=N7ZcjRNvzXnJShXHF1aws4sNDfJVMhwbXPYTk7q7V3ko9FIaxiI97EP0t8P2VgiM5kHt5wRiGcXWYSIoSkvJ1VBZjIvpIQ5CHJ3mQPoRtPaIQQ20HJy2C9EWewWPU-iaEQxXpHWjbrLKZKVfP_GcSJocXpdSxh-lYAo2U3fne8TqlscTyZyKYxFHrc5Rgbrd1D1KhFQXWyUeGxSnZP7rmqzZBZaavZFQ7JL9BxxRwrlUox01WXmZhuQGqmttQCk9nIP9V5MsFRpaj7GjN07joeRU3E89pVEEx-Btabg0CBqYLPeu6huFz1UlUjR7j_H1YqaTA-1Nxv6M1V_ILpmC2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvmPqABeudzx-5Gzx9zlzq3N-ucgOW2FjYRP9K6wbu-Q6AvPIMzCnIQyW3R7KTjE3rwSc59yKI3SavCeeOUKW9y-yiXSIMdYr9a9ZW5W4XJ0WPsOUG-lB8JA786hCWrws4hywdDCIP8tYopl1HYi7jE9DPCiOqnpnPExPUKy_-O-iVLVMR9itWFuuC9OA5wnJcGxgMz2cmaUh2sOjq6Am7iJdNc564qhH7gAQMu4AKhwXIU0VgnDGbgRvrzZYKTsqfgjQ5mJ41tJ7cghGeEVg9Pg_VCpy3KPwDz_foiCwz3ZtPYbU31oLJgUsodILy-C8pUX67McYu4u0tLDDA65pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=bEhMJ9Bb_2PHFgT3tBSvY4jhsYlZHFIRaLlspR4x8Z8lSk_kzYyYrGQ1JxMkZjeXLYQxK31k0hifyYafh66Q_Si1At_qwRhGMEAk44BCPoi16ShfB6fuc4KNHHCnoFvt9tjMe5AX7Gc3QwsxGWNn2VXnaLk2lUwmALisVAO7X0MMqFBGx8Wy4Msxp3WDkE3VBBYa0mrlBQX63E6EcPvnf8a7ZebNR-UXotFUWZ_OnMallYluHVwBI3g6eYLvwWN1IZkXlu2Dl8q0L0H5vDCBn3rxn5Aq15x7naOQZCq18vKfmbkEktEefs3WikDyoRTHqUVkAOBiThGS-Og1T6yqSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=bEhMJ9Bb_2PHFgT3tBSvY4jhsYlZHFIRaLlspR4x8Z8lSk_kzYyYrGQ1JxMkZjeXLYQxK31k0hifyYafh66Q_Si1At_qwRhGMEAk44BCPoi16ShfB6fuc4KNHHCnoFvt9tjMe5AX7Gc3QwsxGWNn2VXnaLk2lUwmALisVAO7X0MMqFBGx8Wy4Msxp3WDkE3VBBYa0mrlBQX63E6EcPvnf8a7ZebNR-UXotFUWZ_OnMallYluHVwBI3g6eYLvwWN1IZkXlu2Dl8q0L0H5vDCBn3rxn5Aq15x7naOQZCq18vKfmbkEktEefs3WikDyoRTHqUVkAOBiThGS-Og1T6yqSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmzgBtVH_OmtgGt_pbKfI4oNh1pE0aY3izIxRCoqz1tE0EMZf2-GlG7llkDwUXPh4Zm2upKhpukEfqorwxInCQ_DkqDkrGZx6BdgBRtYOW2oywhoN-l7ylQqGJrVdA4CUivKCSor8q9ZfriXjAfdkbIG-T_Se-zBOm4EON96L8uq-rdOmcQ0r6CZrishlchE5OmU07lmMA9RfHlfnyXvwPfcbEcJsv9UelJuBwAn0OTq5fVVL4ldQrEirlW9PEMhCCPM-CbMYPUtQCExPqTBw4K61oKitJCKG6OR2ELC0rqFoC-JCutUjAvM9e3RDG9ZryE-xLUtWHbG4Ptmoki4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=FLhYVy8GTiwdyl1LN55p_hU-VNRCBBzNoMo_OZ5q4H1n1zfrNvh7GIn04Wmh9o4xrWb-VW1sGOWzQ_884n3H_JlPKKaEpPT22O59XYBTgTRkdDX5p2I3ASun5yjgPsD0A3A2ssPARiLLg_Ijku2AS2VrWE8tSgnKy9ahmU2umBu9AsNvI8u85Qfm6ETQkOxBPlxtgPK9FLw7to9lnc_Fk45LNKLfXAOn0j43VI5HtK-pcg7v-u_khuXrINjTdtt_-3kAKOwL3GMd3ul7_Mazt8XnZFt-M13vHl0CH3bxLfgyadzQhLqjDBuIzvvXJN3yNgAOV-UEYu_i5I2J3O5E0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=FLhYVy8GTiwdyl1LN55p_hU-VNRCBBzNoMo_OZ5q4H1n1zfrNvh7GIn04Wmh9o4xrWb-VW1sGOWzQ_884n3H_JlPKKaEpPT22O59XYBTgTRkdDX5p2I3ASun5yjgPsD0A3A2ssPARiLLg_Ijku2AS2VrWE8tSgnKy9ahmU2umBu9AsNvI8u85Qfm6ETQkOxBPlxtgPK9FLw7to9lnc_Fk45LNKLfXAOn0j43VI5HtK-pcg7v-u_khuXrINjTdtt_-3kAKOwL3GMd3ul7_Mazt8XnZFt-M13vHl0CH3bxLfgyadzQhLqjDBuIzvvXJN3yNgAOV-UEYu_i5I2J3O5E0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=FpgZgcT7PS5VEXAEptVyZjlvi1NDJmE4_2oJtJ6RHoaB2-Pu0UJQ15hiMgzLwpFaMkKc_WbXCe280G6CF3ZOE5oAHqkJkYKsw8VoFWnRvbjbOHqU6KjbOK-WEHjT8o-ATVx_Yts0FspiER-T16sYMn4pQywrE2HqI2rYaK-QvMQkHAmbh1tlZweMjC84xe0VxEOp4e3HO529yTuK7SrDbgzoUgn9U3AckoAlevlwRfX4B5CFCK6SVTdIvTykmX5WjraN53E_QOHEfrYgyCGeza1C6XBtfaoVtg9lZwj0VbCfuZcFAeHz_kIMzHxEfbD-wvt2RKvNpOeLXyoFFZU9pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=FpgZgcT7PS5VEXAEptVyZjlvi1NDJmE4_2oJtJ6RHoaB2-Pu0UJQ15hiMgzLwpFaMkKc_WbXCe280G6CF3ZOE5oAHqkJkYKsw8VoFWnRvbjbOHqU6KjbOK-WEHjT8o-ATVx_Yts0FspiER-T16sYMn4pQywrE2HqI2rYaK-QvMQkHAmbh1tlZweMjC84xe0VxEOp4e3HO529yTuK7SrDbgzoUgn9U3AckoAlevlwRfX4B5CFCK6SVTdIvTykmX5WjraN53E_QOHEfrYgyCGeza1C6XBtfaoVtg9lZwj0VbCfuZcFAeHz_kIMzHxEfbD-wvt2RKvNpOeLXyoFFZU9pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVvXk7BB2vq3daq0nNjBCk7z1oKjzKpr-9XpnvjkJcXIHy503Lw_s4qGPfaef1RkhC6LSDQkQlec3E0ZDHcmTsZLMtQuiYiSdYJe5IJS-A2oX7FYPc2211qlPfiX7Lo90DI6n5O_x7Js5PmgofrsM1uwDSOztrWN1eLLPLElBPkfch7pbNjgcvfEa4GWR5cqm2n1bH1crOx7i0TTnxx_4Hl9eronEnz2kMlS4aY4uyKuL7YJLtURu81XH19AGmJH5xfA0-i-KuB1MWt2H0SPXK9jbukJCjGcKLeF_siYY3BHtLfa3FWGRK2VvkGFIJk9LfsUhdFw-u-959jOqfTbgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=WRWjWI5bhOTx3p5zB1kw24o_I79O93ZB6zOwyDEvS4sj_5kOGynW402GUw8ZSf51Wv96rmBqge3qb-9-yEB3aOT1PT6zStAtZHSsNJsrPvD8veVJyvwhxsT-3X9x8P8cvdYynuZ8_415Jz7PruQeuQ_5JOlbSRqXmA-sc1tDiEd-mFq_Rg_9Yf7U0cyfK9GHtQ7yFRsmn82jmIQrCCDIJfAU14QiPhc0O3-8JU7pltGzXQUPdoGgcXSoGPW9HwdcvI9TUOXnkAnn_sy3F6cxjEKfgwMFeZea8bfRRgi2IlIJ_cZRCM4_Thuy2GfO21SMFLm5E-_TnV57NNGBU35THQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=WRWjWI5bhOTx3p5zB1kw24o_I79O93ZB6zOwyDEvS4sj_5kOGynW402GUw8ZSf51Wv96rmBqge3qb-9-yEB3aOT1PT6zStAtZHSsNJsrPvD8veVJyvwhxsT-3X9x8P8cvdYynuZ8_415Jz7PruQeuQ_5JOlbSRqXmA-sc1tDiEd-mFq_Rg_9Yf7U0cyfK9GHtQ7yFRsmn82jmIQrCCDIJfAU14QiPhc0O3-8JU7pltGzXQUPdoGgcXSoGPW9HwdcvI9TUOXnkAnn_sy3F6cxjEKfgwMFeZea8bfRRgi2IlIJ_cZRCM4_Thuy2GfO21SMFLm5E-_TnV57NNGBU35THQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8-OqRShubpf7HGBDb_FCQ-rdciGRzyi2Q4lz68Tc-QquvR53VJW1Pu1C6BfOHDuJvYg2MlYXT_Lj1wIBZdp6W8d-NsFjpezHqSD8LOMtFotzjVqZoL0nrY-35b-3r6rdiO09brJZySQs-1WSV1nIb_VjfS5BBSHxg3kjlNTrp0ZEWiiqOnEGBUaTKwFTD6mj9UjipRbToWxxfb5U7bXx4Eorf1rbGpq0sX4ctEHhwiIIAsTqIDJwUlUxFeZ1ps3cCcZ7ZtDXFWyDhMBW-xswdQZPJqhW2ZNjtz3opHbawu6xEnKbo-L3S2z9GlXFCtSC3Meagft4dU-iTf4NFIj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
