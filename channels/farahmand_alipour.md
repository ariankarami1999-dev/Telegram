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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 23:05:04</div>
<hr>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=RI2LVf0juEZKlxEe8fOyUxqso8ZpH6MvFn3CXezzSwiiGFIWn8gngzWm09NQWRKhmClzqfA00n2pYx3rW3cHuioc_G270kGoV3ETw-6cPFB_zKuBsroywsSJcMhcyscntgslErux9BO2vHMn9wZFDUHFp370RRjkpc7XLJatTg5mELkz2cmNUZtbT2EdMvToJe1NDaklzEl4LtanMlFIrmEwjid7dJTHYQjd3IvtQWnFrrGwV7fckGuHEVYcQol-fdNfIbWFxlX5ofYYDZeHe0O9cpbLACvZHx-TOony6UPyIGnMbG09dXUbKZYcuduAaMx8QA0U9d0bAp26qCLafw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=RI2LVf0juEZKlxEe8fOyUxqso8ZpH6MvFn3CXezzSwiiGFIWn8gngzWm09NQWRKhmClzqfA00n2pYx3rW3cHuioc_G270kGoV3ETw-6cPFB_zKuBsroywsSJcMhcyscntgslErux9BO2vHMn9wZFDUHFp370RRjkpc7XLJatTg5mELkz2cmNUZtbT2EdMvToJe1NDaklzEl4LtanMlFIrmEwjid7dJTHYQjd3IvtQWnFrrGwV7fckGuHEVYcQol-fdNfIbWFxlX5ofYYDZeHe0O9cpbLACvZHx-TOony6UPyIGnMbG09dXUbKZYcuduAaMx8QA0U9d0bAp26qCLafw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re8Ivd1acJr2AYq_VM7tBuV0osFyLtc6mK3P245ttOu6Iq2qX76CrvfRCjBeqGzRuFp0QFj3RH8k0gFxMAZTGrJ1I19OFWVpaWxRrrlRAuw0p8l78rRk3nhQazHBXnNEHr2a9DqpwFos-ADwLJnvCNYCqQTT-ey2M7sDqj-KJdKgUzN-WMl8oSXrc8gHUjnty3LQsfP68x-f1-c6d2tbS4fJ-DG6T-UMDxZxtslrKxFaTWHmMrYPxDJZFJpRvEBO-8Drgiqbl0iK06VDjyPApXY3CgfxcA7oJflirROvqrGRY1LuwZ0feiJEkLq8FoKFH3kb3DfTcTbbHHoANP03TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRkNt9P_K0cLX0X1iCZoQfyrbNeOd_JITf75SFDcR1lVcltYSUOBfL7nSm9u8yzj1LlAhpNTt7Zm7wG53cl8PGIUGKVNZLLBYSNStKSZ0rTm1cvJR6lkRS-NE63ed7WZqWQ584z56Fj9tiRjwhGiQ0NIBagqU3Ip19kHXNu7LWcs1Q52OWwuslV1-OKjej2vrM3iixpL_s2iMM1pw9LYwIlUhKFggRnRyt6j8-qSQz7GAYSgtyRkc1GBiytPfid7m-w2UgPEYWa4zDMWTGHi5HLyWLfetuG8KlP-bs-oh0cnqP_AvCushNna2NMtHtkT6CaSMVBbsCbBlHgcn_y2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDMrI8sjMdcQthejeq3gW8GtkYqzNcYT-bFT8ZC2DlPDU4fC3yWfDazNq_DUd3YcFLcoiZFB56PexJFyl6MtXaAoIdZ7f-VtFtAMPZBqQu-RRBQY4jBw5MYX9JWYyge9xiS0ah0IvUgULsL_YAQmDHcixHj8gzfG6HmFoc6kWHkEb8oND8MZq6KXqG_ZP3FSmG1ymI5ayI8mEfiYD7FeVEFQzbwH8GvKaf9HS_XMUxGzWCK0nrsA4JKMzzJaKF7JcxHJLa_ek9m1QwQxHXqj5Cvu2CXuN4OOcYlaRtLf85d03HpZRi8I3j30cePJnMZKbYcMXUCn4lxXkZrk6RS3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKeAfFFZ7yFs2dPG71D-vguS7m_tGyjrM_7aOtKZesH3NAfyjMP_99LnYrvwFw12YerUneqhW1MnozlIg7sCBNZifPjorSA5nOuLG_qjkG5qed-ezX3pwZql1ZPKQORgh1OvDRA0tm6sWs4T3WjNKeWFH1zfuTgsmEOL00WffrKXZbkHcv7NZLA1mLVyLWZDQiNMPJxZGzE7LWYf7W92ciMlPb1sCxi9wKEw5HoWy5FIvB45ry39TeGeEx9AIuFbCPAWILoeDNe8QGYvtSggjoAxZtUzZfXQ7XiX6xHPSYGAUmucAu80xCT17Obm_JM5rcaLNF2hdZKaKf9eer7zCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=beGd6hj4dpjXBpdn955zRb5hQ7qfIl7f-EHjDJx6hy60xaOkKVCfQwA9NNsmBW3tQA3TCtxi_5Esbndy-JRdLKLud8yPGXyKJ0-8Fr1ztUshMmwx6jtrsAtknKwcxM7vmF2xczF6vnStRqXXsmVqeUQ6RFx0cLjZf-yHM5iEWaR5HzpYq28KkDZvaoRKHNKlP2Wit32-Ab0M8Z_fV3X1wxuz-Vaz2fYp90WxWWJyFfmoMIQOCdNKTjPDi7IRjVK7hYAUrqhcIlgSQcNZyRynC6xEScO7_ANjJK3mYxrsd9MWvQKgEqTPFA_RICFtNmK9VQVoQyVuL0SqLonkwOd5qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=beGd6hj4dpjXBpdn955zRb5hQ7qfIl7f-EHjDJx6hy60xaOkKVCfQwA9NNsmBW3tQA3TCtxi_5Esbndy-JRdLKLud8yPGXyKJ0-8Fr1ztUshMmwx6jtrsAtknKwcxM7vmF2xczF6vnStRqXXsmVqeUQ6RFx0cLjZf-yHM5iEWaR5HzpYq28KkDZvaoRKHNKlP2Wit32-Ab0M8Z_fV3X1wxuz-Vaz2fYp90WxWWJyFfmoMIQOCdNKTjPDi7IRjVK7hYAUrqhcIlgSQcNZyRynC6xEScO7_ANjJK3mYxrsd9MWvQKgEqTPFA_RICFtNmK9VQVoQyVuL0SqLonkwOd5qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMnAwp12NlLaDoxqO8kED0rGAKvT3WtaoQKSJR6_RmhFREk4uQ6s7PE2f93UJYqczht6t3pWXdFom9kuKirSPPM2WRtdhfsUHsDVK6b7xwD_gDDTkXKjlmTJgo7mQO6DkLt7b4S0etWolWbvKFylF9UNyfIXPm2RYZPLPIAZB1gG6LLlnYPTPVR_ArBRSWotu1PDSdN0jri6Ld5zG4G4WvsJmQzjpQO-SENr_qsOHFzVPhRoL-86RHLZQsiJ9mRUtgQ-6qy764CMwM1qwwYzxiu6t4UFkeLwunfxQz8DCgfVOgoDsmHE4hsbcv0QVbhJo6X7j4u_OCZxg7hWXk8rtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfzcWOLHfOEavc1MQn0rnUKWFn0kNmK-wl0X_BIamNLZcl63KleUMO8KcnLijvvE5Dw3OzXnkKVX7EQhednWYfrJkBB3OrFqI4at4ON5xcIReQ5yQmx8ZuQlFDOpTv2HAUb0BEt7ODADIGDF2NNMJpZt02_wFxAaMhDAoKzqrpEsHJgL53dpS9Wh8t4_PGJdhcP2xlRBTO-QMrH5BoH-6AuTnM6wrrMtNxAT-8mtFLb_8za0QsotEs7N53GZJMjHvugXcKQgf8f2uhoyo-ECsfjKOjoG3JOIrjUzxg0buGF8ASLYzsWu2jjpHfHnQYy6A68-DNGAioktPIR_V8v8jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_zxyULqDUA2--f-c44tN_0KSl7XEV5OrMIfWQGz5h1oV6Q9Pyf9ghDyCALa2nUM2kAomFlIxxitT7tFn5dhJJ4YjfYkQymuGTfiTjiNHzvNAscOkbb9nlN1ToonPAB_0EuWVyrVN9lhL5M_O9tO91coYQbgVMFwwCDbdtAUmKoRPim5MIyKqcd3wwCeLsJ0UioCg2x4XR7cm4YjJrqizeBh1x_w5sRFlUyo95orBD1gkeJ3JAvz3krDomR4QslN6qN2uStYAcMgHSWZRcDBW4l66xjqFd05-wib3ek_Oz5hXHzOXmsE2HeeyuTNNXHYBu7JXE-o9JZ9PjdkVZMAMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwCSKslVxtTCcaWcGvG8seXt4Fzqw3l6fI5ts3ydFbsyRZ3N5Iz6TFiJ6lBPmsFIT94GbX6OSyiFeFKpSIiGEkhkIco79zaqVwk0MCCFBlbDar1VKjgfG1VhVcFCljregP4kUjJJ00QSh-027oomPQYsmtu1MdlP3EmqAeJfKVYT9vFpofrPjHV0WLZPImMEih9da-02iZSKW8p8PZDuHBJM06nBfi1VV3Kd_w80R6MRyHt2MZSqgew7j-TRcGzDHz_1Bf_YOGopwWm0m_CxfUbFu-mzlZWsp9VQxwETHTrv7_Kj9En1S2bU4k7d13Hgdn6LqNcx3VSxuaOLXBBKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s01mF_6z944KeiLvOJqhck1xV_cnZK1LfGki4a1RKp1PqvXRPkvvvHgVpbuUrtW9_ofoe3655SAznoUHeQGfLqG27oCUIhGLl5hHsPzaZ8aToPYNWn8o977ELShSJ6PUXPykfnJB_3tzQkdLGT8DAUkK0RAPxbKW5AFiRA7UweseSTPIBbsX1BJebXJRXu8cHcumv3dd9CY8eR903q3RcYQQi-76rr9PmzuU7rKWuA7WDqVooMfH9P6r7w3NLqgur9XDS3k_8vm5WjKx8FP44eIq9woAZtz7XNB2clPW5dMOwJYQ6kPYweR9HJC_Qs-Xx9k4VK1P5xYmDdpo4sAB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=P-XIFwqoRRN1g36XHoXGf70UKkbR9BsMqF7rKWacWkFBcU0rydwxPO1WyWsY0wcbKsZwj5ev8b97KuO4yivuA4pWVqwrU-Bync3vRTuNyxvAm0t_n6z3J_rrZ84N2YMkabYZQ00wL7ZgSIM2p7MaJeb4I5RbS0sHNhMDzjsN9g5EQpxwNonZs8cjMAxZn3LOmWYxpre7eFL-Da7A4IV8leVXtudaCdYrqYaI6INBPllmwrz5D8_OdAymL0FoWAuBi4O6hm-r8OaS5c4PXLEZm39DKBijPoJ9gd185FY7cO0VwbNuPvuI32ekoSuiRNVmgms65OU1Hs405fGUDRNQKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=P-XIFwqoRRN1g36XHoXGf70UKkbR9BsMqF7rKWacWkFBcU0rydwxPO1WyWsY0wcbKsZwj5ev8b97KuO4yivuA4pWVqwrU-Bync3vRTuNyxvAm0t_n6z3J_rrZ84N2YMkabYZQ00wL7ZgSIM2p7MaJeb4I5RbS0sHNhMDzjsN9g5EQpxwNonZs8cjMAxZn3LOmWYxpre7eFL-Da7A4IV8leVXtudaCdYrqYaI6INBPllmwrz5D8_OdAymL0FoWAuBi4O6hm-r8OaS5c4PXLEZm39DKBijPoJ9gd185FY7cO0VwbNuPvuI32ekoSuiRNVmgms65OU1Hs405fGUDRNQKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=p1Lw6uRoTJBBfuQhP8GG8UfE-se1nijQ7UE-54Wf3f4KFAnI5bNovrNVq0kVi_UvnL-Ico6hnAFo5gxtduJfQWOB63FKNVxarXUPs8jRxObzbsPvf2oUtH15gvHAivpXcssD9IQ7aoc0kQBwcMlpxXmNdhMlkhDnfN3rYlewY8xm_ThU10qcjNslnfwz_yjex3EMac5APY3HlLUSqYB3bq4w7fW8Xuj9gTeITMOcG9FOkzamCeqQXfZA2HgLIxjmPFeKJ3VU3PPieQvEs78CFLPu1rG1M46LWH3M-85F0H7a5YvwHC-GW-y5dLt06o4HSE9K_J0pPgBEBSCmHbzXtUYDawPLKdaAP7Imhc7brHoQ9O-aablp2AuYgrWrGMtZ3iUJe0V34aXCCLPbIlWM8bIKxzN_4BljpBn7FUej9CVFfkktAyjnDqz3VzDIenGohVUUMHo3jeSx--K5m1eX8arDbsoV6ZV5J9ZG_b639XCRlhGjD1_ez7qbAlGauKaKfzlH03RShMXmArVkJbUx8cKYTKIT6SWG8u0iB8TlEceExhnQDz84p_l81XJxtrdcsb8RaBCdD6yBsbBuZDWI6DNy65_i_2O1Nu7CP1-_SAFvtd-WiqAjp8271Q8v6SG9C1xXT2gM3iAL-P-fPdW9K-HKuoi7Z5Skeb4nheIttoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=p1Lw6uRoTJBBfuQhP8GG8UfE-se1nijQ7UE-54Wf3f4KFAnI5bNovrNVq0kVi_UvnL-Ico6hnAFo5gxtduJfQWOB63FKNVxarXUPs8jRxObzbsPvf2oUtH15gvHAivpXcssD9IQ7aoc0kQBwcMlpxXmNdhMlkhDnfN3rYlewY8xm_ThU10qcjNslnfwz_yjex3EMac5APY3HlLUSqYB3bq4w7fW8Xuj9gTeITMOcG9FOkzamCeqQXfZA2HgLIxjmPFeKJ3VU3PPieQvEs78CFLPu1rG1M46LWH3M-85F0H7a5YvwHC-GW-y5dLt06o4HSE9K_J0pPgBEBSCmHbzXtUYDawPLKdaAP7Imhc7brHoQ9O-aablp2AuYgrWrGMtZ3iUJe0V34aXCCLPbIlWM8bIKxzN_4BljpBn7FUej9CVFfkktAyjnDqz3VzDIenGohVUUMHo3jeSx--K5m1eX8arDbsoV6ZV5J9ZG_b639XCRlhGjD1_ez7qbAlGauKaKfzlH03RShMXmArVkJbUx8cKYTKIT6SWG8u0iB8TlEceExhnQDz84p_l81XJxtrdcsb8RaBCdD6yBsbBuZDWI6DNy65_i_2O1Nu7CP1-_SAFvtd-WiqAjp8271Q8v6SG9C1xXT2gM3iAL-P-fPdW9K-HKuoi7Z5Skeb4nheIttoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=n41c3fmPwDMUpZi8uhSwO8yqcK8Tpm_od346pAPKVXkFPmkpfkmQUXJO_jdjj0YqYj4BmaLUT4U9QvhbisQEerThUEaFjGDrFYKiGNPunFFCTSB5gvFYc9VFKEFTMA21f1DG1rkUBWZxRG7bVDwIg89amfKe0_27z_GMIQkhV1IaJTexNpwjL1sbWvys0vCxrbeozk0CLX1A0OK22pnPmUWtUrkPjXBkqhCq3mjRQBdnHQ_Z1JCWDzTmzk6WKR397wPToVtBhUtSYVXPWoOlqsiZzXUa_wP7P8k4ODwO1uN5wQEOALoyvkj3E5vzk1USUhbzartvuTiXgbwmj8b77Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=n41c3fmPwDMUpZi8uhSwO8yqcK8Tpm_od346pAPKVXkFPmkpfkmQUXJO_jdjj0YqYj4BmaLUT4U9QvhbisQEerThUEaFjGDrFYKiGNPunFFCTSB5gvFYc9VFKEFTMA21f1DG1rkUBWZxRG7bVDwIg89amfKe0_27z_GMIQkhV1IaJTexNpwjL1sbWvys0vCxrbeozk0CLX1A0OK22pnPmUWtUrkPjXBkqhCq3mjRQBdnHQ_Z1JCWDzTmzk6WKR397wPToVtBhUtSYVXPWoOlqsiZzXUa_wP7P8k4ODwO1uN5wQEOALoyvkj3E5vzk1USUhbzartvuTiXgbwmj8b77Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHxt2zAbXOvo9ncK_F40XzeFVHsPOE5JJn7DPbxUzmF92kMxrQniN5q5vxYFh_mnno85mgq8sxOyRRdY5u-ZXF5Aak2fBIuscHOGWRWOJZAuqglxMl5parcsGx_m-kNXf1S-qlnWnhQ1IyVSFB9t3MX9SDobdWq9Ok5UXXUmISAjY-jXo60tF9v0huk_iFedSuE4Pwnori7Y1ObGgi_y1aNU6sFNPpLRI1G10uK4ZxtiooKEI8CAzBVLxHuAXtZcmsrrRV-1Ir0uuhwvTAW4lDJlMHX9oLEKswL_DEGEDkOWZwQkCGT5AlQ9AZZnauerlb4HA67mO0uH3BeaPi4Xww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDyom87S83of0_MXMaebstFI0bWNGwTeZBWELRs5ycGZ1yW5_agKpXvKjc7DJzZZ0s6sh05TQuYVxtkQ5jvbIoWMGyyNPfojLV74k_OowxA6M9rI7f-lL5firtiLcOLgJrFca6xKH_W3eCZ9S5iB5RFzjixFp720gvln4On0XN7G-SSLh8gnygzas1DtoJLZ3XoSTTtHgAmQbhCV1aSZLnmfoTmGX_smIssv1nIUUhtVI9gAUpOvDjGg1dU7ThQhSJ9k6FeCG9YIBhFPwbSJietkd4y0irlIs1CEmJR46E329wFw39m_N1MpStSb_3naIKN8qL5dToJzOogLSlTYPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgK2Sbz22oaZM8n0a16VyX8NafrfZEba3V8NE9ruYvd8yQk4A1kRXNYgUpATXR--vJDdY6ukFmMs5n7-8RqXHtieX0IVPCjeNSyiypXbVgQvvcVrRXF3Xm-qddoeOG7oAG1taBS0ezAMu3bayRjlGv9SsljX_z0YANcwV82uyfAZ55fmMyAVS9L2mYLMWy991TaGe3qN-hDCrL9liVWf1zUupAX6KmjA5q7dSUgVMzIBhy60fb2Z8vuFB2_QBXAmz34QR-RlKnhM_MrvUSgq--XfHZZzy5ttC-1NHJKRLG7bS5KyMLC4VhyAaFfHABMVHjdKnM6M1sFApNHZhxzqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF6KnwArEg0m5DPf6CZgMYYwnjzqJA4QD86AgvEgFs5xC8sqzqj_VN1YFYaoofySMTLecKQmd6LCgDqhFFCJvUx3wXSbkTDbFFwUaDB3WSfW9U3XbpAjyhYWhtoqcxcjBJ414tCcCmLK2N0Oht1ula7zyzaE9ANL6xpYzWo_Gl00nM-RDQEBJIF_8Nkrw-UG1OD_DqbrLa4C0zjJwIQg-qcYwOqY0NyvbnYMqfLJnDgyUb1mSBhXjW2lfzLw3F4yzq0Cf5qKQKN6DYIdB64Lmwoh8VvEVKNJjkShYPEu6zovP-Cb75ArLbTPI5VWW1N26qlg_Icm6AbcjCEQNWfVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJaAEibM70XTudpuuja2UzJ1kW23qoCgIBY0F9q9WAMb34-TxredqSWgUvtGIMxWX1niAKeLYsulK_GEA_D8FpONXPP6WhHPY4oOoRNpvvj24R3hykO1fUivU2hf-x8j1UzgDUChN9no25OBRyh6-k8xCnwbSYtrd3bpxkTMM8fVmGZXO7Ug9QnItdwbO-BZIKzHDe2Wlqhha2C4rAMDjavCOFtNswVS0awZicqCoM9V6rK55IwzivB6xM3jS3FJb6dCdEwydtxqQf7iv3JGZqx6hbqO3RCM4yJRM1WHJK-C6lUwDpYs_QUIhI9FmYgvxIP9m5UCFNspECIzcAf3AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQIDhvCB14Dt95k5QRatO7jMbp3Cwk1iYG3pTFIpaqdRohOyUxyczmqZ8oMXDRBmS9jCWukvulL5Gwk_CVn6et8089KiJSi2CC7EqkeGSHGky3sYhFFuUJchvoK8VzmE7NxfAaSuPoCppQFdS_hC6tQqOFsY6U39OrGEb-OyvEuuRIng3WNrIInW094ZKBVImQOohi1SHnhCKZaJ-nXI4bSBbMb9qc1P9pBOq0uIm7Uw9YMJaod0KZAHyHOc_JsMqw2BUlduAsCKk1Re3OJWwWztrYMqTkG3HLuLvaWLr5ppEkbGJc5yXnWSdaFRFH04uG7RG-SRGDnv2YvL6rBn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3FgjPmWSr9Jb2sfu_8EgkWAq4Lpj-qspaKuNsEncW8AG9JUgNNwGMY1TIuYw2HwoPEhxi6Lu1ylDLlphKiWouJAqqwpDSHtUNX3rnJO8YlnkRdUchgZVDtBuCsUn5AC4rOAqdZZIeGQwWxKaDis4Go4RqIDPCNUJZc4g7pMKnITU0TLLIs6xZuLvptyjZsuGkcBuwXBSqrQRYxswtZQz3Ehfm11cVzPI8d_vpCNSIB-OqpvcNvq6MCvlC8ALH_7GU7ge10eAGsIKaUy91k-lH3Tbae8bBNATk2mr5kDb5gBPFSFH34CwmGemMYQED38DmnutcmOhhpDKgwEKOXucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KB2Ff4WkxPDoqHeTivseS-Bks6Xw7S-7pH-hZQOYAYhlARwzKrAxCg1D3D9t2Dt3nZ4QEVH2pwYByGUIHsAD6TPFfLpUa8-qMnENzv6X5QRXIW4aI8IJq7JhTbksltd4iEESpxDVdi7vHrS0-o4Pb88GGA2lTRIQ77Ndu0WM3NxXsZEiFBJ2E4m4knWQ-X60RBUv2grLoWSsfACCs-JNam1pyrikhBrYaJZPY-P__rF0r9OVeIW-hMG9xsf2HRGF4Ykw3O0wqZc5l0w1SFslkB7jFRinht1XGGfQBeqTQbw6nnioOuNDcLTvi6qUtjHfiDH3ZyfAzRohT_2m0tVaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mji0rlTB9dYowyio4w4CnffPvxhsco79f2On3VFI6lTzSKAjBhF5QcWkJfJB4bfUae9RRiDpbhfeHf3m9mz1UO5MFgMfq3MY7uk33LPnds3O0A9EeR5KQJuN1JRK79AhZMCxxdS4dPkd8Me3mJQR7WxLkbBm6ohGRQ0JzJxNpDMD45ui8pQI0Sz8mNS9o2jkxMKn5Hf-ygMzq_wImsVmaqQ-zMJGpjWhWNkuJQh8iOhlIXBpLh0O2aprjiaxijbuKL6aNru7lcpbgU0ZsCe_sH3xdapIbaQOEEyC2W3plQuXUnmKlMLAceylnDHmccD70bi2CTDyeFQBGWT0PwEf3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1Q20pQ34YHGzigJ8-BMK8KMoKj-EO5F_ps-7kdeguy5eC9kS-hcyqO96JTM1PkjMO1x8qcEzop46Syd9DU9LKHluUUkNnUL0xMqGpkUc2BuKBs68wLoiqTEaZyIjSHyWdN33N0rUKFIL9fL4VOPJaupplnHzN9nBjrCm4i7hh3Sv1PWI-AvzUScYL-_LMbHT8NwrDjn9pZMkDsUMt6jas94KwyHU-rq_UmpUHgczSJRiRn081lAZXtYDvdrNeYavAZ3S_JNCll-J2gwgNaCdL25ccDhQdHNCveC9CfuXgf8JDW90iD25geTKQishZsZZvjqoIZLw2Csvaate9HOvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=MdXPKBHv283EB6sqf90lDkEjNfN57trvMgudYxsmdqsdzDAOB6CCVG50TwxThYYBfuLHnAiULdvmrgaISbKdqYZBbh3GwHlgCbz764n0rtSzHfoGIlPV1c1qIRbQLskc2Wwv0QY_Ai-dCF4TnuofdNizhMdCk8jUtD2U4TPp8x-LxFYry0VtjECNYwZ0x4YNfNHicUs_jz6tn-Of6jlUSfxgwy1VFuAve1MiWIE6UfRb7bN5R6xUJVx_Bq7-_5gyxVKBVylfC5zdUyVP_nzx9z98Zzwu-caNmnKlUhlPBTL2HCCbqAkqLXQwWiTh0HY-nExoOK_0VV7wau__PoQeqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=MdXPKBHv283EB6sqf90lDkEjNfN57trvMgudYxsmdqsdzDAOB6CCVG50TwxThYYBfuLHnAiULdvmrgaISbKdqYZBbh3GwHlgCbz764n0rtSzHfoGIlPV1c1qIRbQLskc2Wwv0QY_Ai-dCF4TnuofdNizhMdCk8jUtD2U4TPp8x-LxFYry0VtjECNYwZ0x4YNfNHicUs_jz6tn-Of6jlUSfxgwy1VFuAve1MiWIE6UfRb7bN5R6xUJVx_Bq7-_5gyxVKBVylfC5zdUyVP_nzx9z98Zzwu-caNmnKlUhlPBTL2HCCbqAkqLXQwWiTh0HY-nExoOK_0VV7wau__PoQeqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=RhXsyUY1jDgDNOoW94UymXMqXEib7DFakXJv6tb1ObDgxde3-GdYYYjThb1-2TW6Ld4whzYvw1XFJiMnTCvA1NKghoqO9cUTi8O_AFjI5R0SMzF_-1aDfjxfDUvBhHwhlaxtOhwebSesooZteBWZF1q91vt_nEQTXnjRufQlrUL3BKVodVkzwACm1EUjWG-EQ0s3nIFlGjvO7wIGyI1IkKPXR5Kym8Nw5bgQkJgRFfZ-7naSPNqXy_X7VIfvu35NU4tZX7ENY_dAIAUJKGv7kuHHEB6BmibDRbyrUTYsHN2kAb3uYJn1OTkOjMoQsu5hlXup1gPuxKbfPaeiAljBlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=RhXsyUY1jDgDNOoW94UymXMqXEib7DFakXJv6tb1ObDgxde3-GdYYYjThb1-2TW6Ld4whzYvw1XFJiMnTCvA1NKghoqO9cUTi8O_AFjI5R0SMzF_-1aDfjxfDUvBhHwhlaxtOhwebSesooZteBWZF1q91vt_nEQTXnjRufQlrUL3BKVodVkzwACm1EUjWG-EQ0s3nIFlGjvO7wIGyI1IkKPXR5Kym8Nw5bgQkJgRFfZ-7naSPNqXy_X7VIfvu35NU4tZX7ENY_dAIAUJKGv7kuHHEB6BmibDRbyrUTYsHN2kAb3uYJn1OTkOjMoQsu5hlXup1gPuxKbfPaeiAljBlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=Jax1w_Tb3V1RQ33kIm-r6Rdulzlp_9R0lIpv2cSOL8l2eVdTwFRbkHw0qVNmLJOi6D_x47tpkyPnz29Kr5IE8ZF-V2N4d1ZRE-_KDjNMQZGwsU6WiIg8k8ne456JH0Mxj1nhjixvLBBHaza2uKWNKbcPhl8AAzU_UCw7OrTUTwhuRWxiiW7AxMC52wNhQf6lX0jCcDQNmmYH5TJXI8Siw86Z6r1HEZVYzXqhZmqSINDACGTB8oKFuvLLSwWUL3nSkIa-kHFNaLu_p_1sTff3BRlppd4l5pNiGLlaamIGsBEG15ugyV7aYf7GUBWVqZ7P7tUAwtmd-uoK_d1y-tPaXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=Jax1w_Tb3V1RQ33kIm-r6Rdulzlp_9R0lIpv2cSOL8l2eVdTwFRbkHw0qVNmLJOi6D_x47tpkyPnz29Kr5IE8ZF-V2N4d1ZRE-_KDjNMQZGwsU6WiIg8k8ne456JH0Mxj1nhjixvLBBHaza2uKWNKbcPhl8AAzU_UCw7OrTUTwhuRWxiiW7AxMC52wNhQf6lX0jCcDQNmmYH5TJXI8Siw86Z6r1HEZVYzXqhZmqSINDACGTB8oKFuvLLSwWUL3nSkIa-kHFNaLu_p_1sTff3BRlppd4l5pNiGLlaamIGsBEG15ugyV7aYf7GUBWVqZ7P7tUAwtmd-uoK_d1y-tPaXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=t41t-IHEuj32nkUfZtulu7gyOJ3zxGx7igIcHu4h4aOIW3hCizH0qSO3MoAWWTlOK91VuOB0bRtYOH7xeTZU9YJSMa-A0Q-kF78RdRjludwxiNr9ijCRp0H6zw5sWTBkPKASAb4nKDG2GSajEN17uBuXFL41RTHZ1ybnz3PCpoD9_NlOwgzEsEgiwCVQA0_0b8srTAzScjTrJ37iVR50e1Kza4A1gGjnjH6RRqGAacnjdkCjDYfSzX4_8XUV3RBGAW6VkQw8wz2uDXpFq2ATO7R4ic7KStHQml_A2ZtM6zirInz2wsHRKzzFhSmeRZU3CHD_v5F9-BYckrtUCJGt6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=t41t-IHEuj32nkUfZtulu7gyOJ3zxGx7igIcHu4h4aOIW3hCizH0qSO3MoAWWTlOK91VuOB0bRtYOH7xeTZU9YJSMa-A0Q-kF78RdRjludwxiNr9ijCRp0H6zw5sWTBkPKASAb4nKDG2GSajEN17uBuXFL41RTHZ1ybnz3PCpoD9_NlOwgzEsEgiwCVQA0_0b8srTAzScjTrJ37iVR50e1Kza4A1gGjnjH6RRqGAacnjdkCjDYfSzX4_8XUV3RBGAW6VkQw8wz2uDXpFq2ATO7R4ic7KStHQml_A2ZtM6zirInz2wsHRKzzFhSmeRZU3CHD_v5F9-BYckrtUCJGt6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=A9qfoJIVDKTf9EEeHDE81O8RmM3JJwhZUoQdnLHtk81oW7DyYBWMAAZF2NuLKtcCW3tJe10yTQxxDouOqxZpczkZyT14Fi1Nc5Fi1wcXA36okbov0LucY_bYt8ov-oyU_afcsno9D-VCEPm7OIACLkc1ZQCV3cTpK2-N3Of-zEXx3NnphwboBLCeSTGelWvs-FSHKvfi0Xz-dAFKrDcZ7DqZt7pIBZ1NYcwNrThGYIOIM1p4_t8-gfptT-0P0d_bMGz2iIV8agvldDvSvB8eKHz2ESzafjKFOlXc9XAw9wo3MTxvF7dIvbbFF9QTrhW5KhXrUJTUJOwNHY7Vsbu7Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=A9qfoJIVDKTf9EEeHDE81O8RmM3JJwhZUoQdnLHtk81oW7DyYBWMAAZF2NuLKtcCW3tJe10yTQxxDouOqxZpczkZyT14Fi1Nc5Fi1wcXA36okbov0LucY_bYt8ov-oyU_afcsno9D-VCEPm7OIACLkc1ZQCV3cTpK2-N3Of-zEXx3NnphwboBLCeSTGelWvs-FSHKvfi0Xz-dAFKrDcZ7DqZt7pIBZ1NYcwNrThGYIOIM1p4_t8-gfptT-0P0d_bMGz2iIV8agvldDvSvB8eKHz2ESzafjKFOlXc9XAw9wo3MTxvF7dIvbbFF9QTrhW5KhXrUJTUJOwNHY7Vsbu7Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=By16EwzLPfqcexuhU_5Bngr7880D7KABvPBNHSK2ByRt2nDeGd9nJVdwm5q5AkdGGYOyc05MPLj5Cbgyf1SdgaMERxzb5HjDpuOGsQArL_H7mPLpAG3fnO89La-mxABBxK3-A_FhkraEWIjFGac27dLqjWRPIF--mProDUmV_tYNBQ6F4kvNCxeuaxSOXITtk3_hf7djknUdNp6dtzcyQFdsT6pMqg9a2Kghmg16E2o-oeCgcqfKDpCEevtkSjQcAkvQRkq6zNV3YVECr79jT8vOVqPaX9tvL6q6XMr5tiIwDdEHnxBIRB0BmUeutjwKNqGW_SFqF5HE4DRUik2Y1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=By16EwzLPfqcexuhU_5Bngr7880D7KABvPBNHSK2ByRt2nDeGd9nJVdwm5q5AkdGGYOyc05MPLj5Cbgyf1SdgaMERxzb5HjDpuOGsQArL_H7mPLpAG3fnO89La-mxABBxK3-A_FhkraEWIjFGac27dLqjWRPIF--mProDUmV_tYNBQ6F4kvNCxeuaxSOXITtk3_hf7djknUdNp6dtzcyQFdsT6pMqg9a2Kghmg16E2o-oeCgcqfKDpCEevtkSjQcAkvQRkq6zNV3YVECr79jT8vOVqPaX9tvL6q6XMr5tiIwDdEHnxBIRB0BmUeutjwKNqGW_SFqF5HE4DRUik2Y1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVRxXEdY5Y2Kcn2wp8K8_5KW44cBvjLQLHMfxBCrLwycdYr6xC7jhssMXFgMUlgBCE3R11I0sZrKWwMy-F42h14I3qXl5XiKac7F_eEK5FSo5XWSulusOhvbKdyLlAKBzdRG-qpdLY9spxk9syQ7fm3MytgMo71JVAf4O0DRd06jOT6dx8U24EOgfx9KZt3xAAoIa4U-te9O25JYyG5upsaj60h2EkxQJqd_YIRhbQlG_2lyWePQfkFMjLq_z6q3_fH_2wEJYt9P7oN0KtbDqW5W7_KAQSdE3foOpqccrtz87vMPcPhSIBHMiMtDtyJ26ShJAfjwCdNMEfoFIo0NAl8Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVRxXEdY5Y2Kcn2wp8K8_5KW44cBvjLQLHMfxBCrLwycdYr6xC7jhssMXFgMUlgBCE3R11I0sZrKWwMy-F42h14I3qXl5XiKac7F_eEK5FSo5XWSulusOhvbKdyLlAKBzdRG-qpdLY9spxk9syQ7fm3MytgMo71JVAf4O0DRd06jOT6dx8U24EOgfx9KZt3xAAoIa4U-te9O25JYyG5upsaj60h2EkxQJqd_YIRhbQlG_2lyWePQfkFMjLq_z6q3_fH_2wEJYt9P7oN0KtbDqW5W7_KAQSdE3foOpqccrtz87vMPcPhSIBHMiMtDtyJ26ShJAfjwCdNMEfoFIo0NAl8Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGKlue5KFWojSPDq5AVS9nGOw0JDHrGnkVmhkxFJ_6xpLVbGEGlcp51__VUK4_jw8TaNdPGiLNsJQulLwcRr30clJqM-K0YeTT7AjwM2u9Ya1WJ3zLmyn3sTtSRvpMqYGniBikjk_cCYhWFRJDYBqd7_Me9zN55cH-iQ2K2fKW1XdXq5jkYoo0BU9qYmSYBC6uB9f4A9_SLB9BLdvck2V6CzeTombkwJ5Tm7SUEMCEOzms16-ZvC6xAdOVR6ELJv3ncYKuV_RBDBPkC5KUkZ9QuMY0DBCT9SA8evJesfY5WpzLVC0bl3dNKOXgZwExeOMri2UfRavh2KEgaRQJrIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=muY3zF54ha0X-8jrV43laCEDEu4FP4y9O9imTJpGo4G33BbmbC7qNJwuKdbqR3_t7uNO28qZeLPpTqj984hZz5eevYaRHVd26Pq9h9oXK4DzgroQ-ldR5QD_lOBz6KjKediTUts-rbFsnWIIlywiCFTte5k3KNgU0PzzlcXgL4SGNNJHn1ZxuJINhdpZwwePrADtJ2p7Uuly8Gm3Vz6QwbBO1e5kZ71mr_tlXh0cxQOmTPaKZ7Wd7A7NipW_jTwODK-XlqFCwwPHdTL7Eg7PQqqfJGyOcobqR9Xz3dBHG1b8Tbr5MbVIFRsNJDfmSbi16ht6exLT0PPRepjk1CDWJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=muY3zF54ha0X-8jrV43laCEDEu4FP4y9O9imTJpGo4G33BbmbC7qNJwuKdbqR3_t7uNO28qZeLPpTqj984hZz5eevYaRHVd26Pq9h9oXK4DzgroQ-ldR5QD_lOBz6KjKediTUts-rbFsnWIIlywiCFTte5k3KNgU0PzzlcXgL4SGNNJHn1ZxuJINhdpZwwePrADtJ2p7Uuly8Gm3Vz6QwbBO1e5kZ71mr_tlXh0cxQOmTPaKZ7Wd7A7NipW_jTwODK-XlqFCwwPHdTL7Eg7PQqqfJGyOcobqR9Xz3dBHG1b8Tbr5MbVIFRsNJDfmSbi16ht6exLT0PPRepjk1CDWJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWHrZnowivAsI0i1nPVh4Pv0_ORe3pCzAEtvWv7iBE_SAFG_E39JoJqYApUl7aEtHqmmH1GsN2jaoj9zGJUCyzED1QQKbqvd_wubuczlzhnL-DIKr05Si5IRdJXasSlSzwSpX3hTYANyh1vSpM2st9cJFKwmaJR_8XTKQSEoFH8JG6RIi9RfRl2X2bHDxtNIjDBqYG2i7vfR9aFln_fwuwldd4SP0I4uCMD-6oKzYKw1dThVXTwnxMKV_TL1pi1ueiCa_NaWgnmV1Y1WIUSyghBJXBSbUv2V4ClDYnvF7KMfe1MJ9Brv2nNnna3FvxhSOX3K7lZ40z1t87oOJQK2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuYn6HHvLO68DpXmftV89S94l6tYTUsLnOpscML1Pomwo_ayJ-EmWL3rEkka1vvh6G28KR1DQ7jnlmAX1bdY1bFo0wbOp_WtQBrBKfmP1vqgtGCFJ3PcxRy-m9OUo_oKGj-7qRWrxCDgJ1WqNBcRw5KXtz4uiU00eyUYCI-LJHgaMF0SUCV0I66OstamJte6_6cFLFMktUwvZuFyl16IPcul3P_BlTHHdDmNAS3h1o9hGLu7S4kl1vwecBpUeWHS6OS0rXaK-P-hK-LJIdeCGcxfpE4x27X4Opi0DoBBGrTzB6k7UKIvTmbgEfPhOxPlWKoYGRpn0gj4__u8qGRFHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YntlPyOiB2roD7ifXjd8a3NFEbqVYNepIF68BDdIFJp6m83a-5TCv8pXANxzqg071rph68ugKv8yEpKXtgz9LQP47yWvRw9yMZN0O6fxJ5u2J2tVSmyy4yeworo6RyWD18bqm-iX_Ml29QaJ6SLSjO93itj9dMP7XcyxxqmK0DfRtj98afZ_JgCO42igOO2Bq9ZjJcedA0dJBjVJawCj4MsUUKWVYzVdGbEdlaIOapAGjC0qyoHGO-wvRma19QVuBDwth_DmzrM1mFzA_vi2cZeV3DukYXDHh9medsz8K3mncmFVwLS3h_X6rxiBJaZ9JszCsvGcyE1yQfTN1Mj4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=qySzMG6_xgqSPhTNt42kXXWhXzOiXAcRTsxVyXtOZilLzMWm13aiOO9ZTosCqEy9MZ5Q88ZtFgj7hzns9GdDvOo4jieBudU1Oc1zT58wEUPI57alMMYgyEWHVpqXIv62pZn1_qxQrdfJqiJ_k2_zQaFjdMIe9hEYIC5AG1ApEg1f-x7inBTRHr96vwgP-PJ6crsdmJjtfAPsLzYcz9TdOS2qsTg7wrRTObMUgwfbVEOhVyItJLQcoWjdA6MWS6Rp5olcEenE2Qvy7YdMhcBOGmtTRjlH35M38or-9krmNUmQCwjAwRTSYrMhhTeDDnwXIt6ZvBu7KnCiQBegrEiiAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=qySzMG6_xgqSPhTNt42kXXWhXzOiXAcRTsxVyXtOZilLzMWm13aiOO9ZTosCqEy9MZ5Q88ZtFgj7hzns9GdDvOo4jieBudU1Oc1zT58wEUPI57alMMYgyEWHVpqXIv62pZn1_qxQrdfJqiJ_k2_zQaFjdMIe9hEYIC5AG1ApEg1f-x7inBTRHr96vwgP-PJ6crsdmJjtfAPsLzYcz9TdOS2qsTg7wrRTObMUgwfbVEOhVyItJLQcoWjdA6MWS6Rp5olcEenE2Qvy7YdMhcBOGmtTRjlH35M38or-9krmNUmQCwjAwRTSYrMhhTeDDnwXIt6ZvBu7KnCiQBegrEiiAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHsKm40tIAzX7QaqY_AE65MjG6nrZqdAcb2-Cgryw6t86QR5IIWd-OJFjiCUJxowOkrozLMGVXUtVBUg4Lilf5evvVbKtlmRqaimb8Qege2kRZV8NkR-L-QwEZVmw2_kWpi2LugxLVQLF0JC3JgGxBUB1OyxgZ4BxPZ6jCqNGJyJXVXs6wAnKD2AvswgyCWK3rxlQDuImBzofmgWAoqoWWg8A_yen0ADdA5ZsQ8s8RePxg73i1Rqq-yYzeo89F-JCLS-M-37JT8aHDaHGHtDWSzPMjTJ-PacOipUDEtzaZHJ8sjzx0Z269BdrGy4kpU7qzU5xKD0E2_s2LSV10592g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxUWX-dyhZlRH5DOnZyrC0k5AtFc0ivC4PR0IjaRxqsEEnN-LsgXRwzBgCGNFcVtP36uAE24p0UQYAKky0j-Dr_qpowSU5lEWesYB9bli9wjrT1hL69EK28NtR1quvXCai2a_D9zAv3aPliu4LojOYpu0Ge8H0bxopy-I7YVOlqgYOxotUMzyJmIPSUqdYh0AoaoEoKHDGh8kWScUdnuix3sYfXm5XyqyQnwI2XLW1ZGpt-yFBHVFtiMUV7QdyWm5ak0Bm0kztgu3XNVnvE_oMx5ZmbD3G35pXJxjwWFXODoPet7wT6qskemZ6Rl1Mu_gnsEVjqrb-JtJPbpjiMhIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjVE6-Pbn0b1bkMqz9M9iOD1CrgvTg1TUKH2WabKupsVzVpQlvVhFylxZmQhR5qAWsK2oGFSOlTOUiUZUvNTNSH4Jz09ZlsJd9ntpYrcViefQZgTNsK7JG_tHiuNbEsbpz00bzGjDkN85jZHrRxfPg03DGLNuPBsX6SDv8hfE_qQoGEv8INkk6T0CrZsIcxT911pGeppL3LIPWQ-iqlR0TOZCo4jY8zoVqjVM7hr_IRGogakSBKzn6b-orPWA9mKv2QPU3dHzupRX9QSfHajUs8nTU9k4wxoW9f-wAuPwYzBincVyoi9G6Fn52g39ebDGn3VHc3N3udAdDJDLn2CbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPJJwRy6i7eexwtAdTRpMaINtb862TylNpwF4H-GbUFTxaGgaHuEwj3fZGXTSUNSBg_zGcKlvtM37KCf7qZafHeVhgmupm67FJAG7IxRnGTnf6oXho8ewC0Yd0i_tbHSEcXDmCwK1rUxZpq90wxoPI7P5djSY1eNI-J_ebuOvLDQrJbWrqgUa27gEus4M3zgAuFpby-JpuHNzI7dNaYuhFJ4YZM1xFdmWxRvcipoO2XVp2eRdQzGvgabYBYKgcbVcTLqqlLvP3W-B08VFNjqEbXik-W0ADmuyH4tn27xlMmQHhOUk2ExWsfUqzhA_MAplfChV42Je0V6R0tLWXCeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=iTW7Ib8lColh9gbAc_9eQVWfAD4llntjhRN4tS6J-cOgssXrS8VV32zrVc7rEg2YLRdBZRk0cgVOhoqdvxGyRxy6xD39t4mao0FhFq7PZenQhWxnBiapSJYGnIMdlW3StqIstnHpwwqasLSZwyh37805zx9EJNkqbOEW3I4QaAZxbltFZw9n-HZgss6botDJD_F0nI4VZ5amZhR3LW4Zj3wS4F9ehbWupgATO4lINy5MNwyTeAFBltOQFSm8p3v2VQtQQdWW4CUOSZv3eMGha-QkHotsum-uhdhCsd-qF_fFq2ctoEAdg58oKlhfX3wasZXOz4e-oSGNDQpKcznWjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=iTW7Ib8lColh9gbAc_9eQVWfAD4llntjhRN4tS6J-cOgssXrS8VV32zrVc7rEg2YLRdBZRk0cgVOhoqdvxGyRxy6xD39t4mao0FhFq7PZenQhWxnBiapSJYGnIMdlW3StqIstnHpwwqasLSZwyh37805zx9EJNkqbOEW3I4QaAZxbltFZw9n-HZgss6botDJD_F0nI4VZ5amZhR3LW4Zj3wS4F9ehbWupgATO4lINy5MNwyTeAFBltOQFSm8p3v2VQtQQdWW4CUOSZv3eMGha-QkHotsum-uhdhCsd-qF_fFq2ctoEAdg58oKlhfX3wasZXOz4e-oSGNDQpKcznWjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZ_aXC1sxdIpALVN8hMaFVB5D6_9XJRiOr7-DqOCdIq1NsT9yS7Q3UH-hhQYDrTX454MKDnNsk_ZpiHN5r10Ow6o1zW0Q1JNng72u9FLgv4Xa0SIMGHYSw_vZdM5FZlvPNq9Csf__JPEvWLWBO5CtDk2xPZHYBiYNKBKoxXlQxbGl-yrEz6aMayugGYCk60M2beI3XebqkRSf6UXxXzZpBzBBAG99naD7Dtx4hefOSHTKqdfcQGPms3boZ08XNiVW1gMUF5cWlaex8mxMqec0RfXYNLM5JB2mOb_Q-SgMYDVfq9oitWJkhEsJTSig7tXlkr2L9blxJ4lPest9tSQVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ND8SXR9iDD7GMI4fQ-1KCoWojTZugBzxq5FY6E7WKFUlkrzXHPG6lOK7Io9WH75u-TACLingCMDszQNuIQGdl4n4TKVgu21AKXX3mxdnS-yYW_FvMyg9XMfADB27inIclEp080gGnEuom24NRq6ZpPn-KsD0vuvyjFFogRB-sIQpz14Q_9-_1unr96LV1Fm0K8qy6Ok7OLSacFkzonBbDHhQmaCydjlzL9R0pqwma1C7mNuHN9ipwa1nMZ2k2zTF4hUxbPMZbxsmHbTErqofvQF1bgQKZjv6T70nO4J9UOWgCzVXbvP267nZ-L-ljrwagPMXq2vZV8YPI6IfR6v8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=D1yuIUkp3-jiDV3_T0_WrvhjO3EJZF9Jik1t-ZO9KtYt2BKIsdbcbx6RccQGYZ53ON6RsaGU_9sscU44KvjTidr0rk17VCMzsTrUvCWVxbNHGgEF2sbH2QGreb18cA_8_yq2tZExPVD8VmyG_u0gMe6TUTA8IRj0fG8Wt75uSm9P9EcTCk463TxjloDekLBxZOACNIKRsnTgz7BWfJeqmyEkyyUi3LrnFgD0vR5swWz7Yd3O-7sz0kBODfz4Jaz76q2W4EBwjwvKkMZL0sRUjDAJs8w4fenLL6_BsiRRi0CfFWgvNi2eoML0GRG7WD3ZSpjYlDqjIODvDMT0BQfb-E4LtJ0tXIQhNWUZkoMTYtZJqL8Y8v6ykLgiumGE50vrKhOZp3c9wM-JSL9t4mcGLXHYpAs5iOZSlVQ8enWaidXY1A_eCrcQOKqw6RIM-ywxqThwg0stgoJwoYJEAEUh8e7Zk3M7r_6R72EO_QQJkfBqhSsMIqvCB0s-jjYl4gry_LnZAIWi-wTG9fjTh5lp5LbwuLc4mEFjjzFQF-pkNsg6p5roKBSlhXe3OJsnUFNSrDP-kaw_a3ZDzychPdEk1Ucr26Af6eqGL_rn4o133YAg_UJaJjmXthqXHeuFlmdhhWDWC4c_XAukScTKucDh8-hBtxyDuqmMqWq-G6Jrn24" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=D1yuIUkp3-jiDV3_T0_WrvhjO3EJZF9Jik1t-ZO9KtYt2BKIsdbcbx6RccQGYZ53ON6RsaGU_9sscU44KvjTidr0rk17VCMzsTrUvCWVxbNHGgEF2sbH2QGreb18cA_8_yq2tZExPVD8VmyG_u0gMe6TUTA8IRj0fG8Wt75uSm9P9EcTCk463TxjloDekLBxZOACNIKRsnTgz7BWfJeqmyEkyyUi3LrnFgD0vR5swWz7Yd3O-7sz0kBODfz4Jaz76q2W4EBwjwvKkMZL0sRUjDAJs8w4fenLL6_BsiRRi0CfFWgvNi2eoML0GRG7WD3ZSpjYlDqjIODvDMT0BQfb-E4LtJ0tXIQhNWUZkoMTYtZJqL8Y8v6ykLgiumGE50vrKhOZp3c9wM-JSL9t4mcGLXHYpAs5iOZSlVQ8enWaidXY1A_eCrcQOKqw6RIM-ywxqThwg0stgoJwoYJEAEUh8e7Zk3M7r_6R72EO_QQJkfBqhSsMIqvCB0s-jjYl4gry_LnZAIWi-wTG9fjTh5lp5LbwuLc4mEFjjzFQF-pkNsg6p5roKBSlhXe3OJsnUFNSrDP-kaw_a3ZDzychPdEk1Ucr26Af6eqGL_rn4o133YAg_UJaJjmXthqXHeuFlmdhhWDWC4c_XAukScTKucDh8-hBtxyDuqmMqWq-G6Jrn24" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=j7dL8HfMrSZI3XLMGVCyiXvpck8NZv7f_7zRTzFiG4lP7PkE024ekh6rZg0VZcfRIuVvjthbql_GRVYI_gU4mJt4tO77t5kuITzVspVJsiwX0XVyHRYv0r-dj73H5cnmAPNPn4M5Y6AFQyoZZxMGec1EaTyWmomiijEvzDe0u0RYti_c4LEPnk3NcMWa6nJwBIgYmiFafnpcDxv6sN4Xtaz9qfnJTBPP5q1POJ9jhvC1dqB4rkQVRZLMoJ4_XREtxSi5tqaR6i9QG0yJv3ZRUZILyOuImSX05BCqHdB18-hUg_nPQ6u_2OogOFplZh9rq_Nyh8OV0wGX60Gx4AoB6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=j7dL8HfMrSZI3XLMGVCyiXvpck8NZv7f_7zRTzFiG4lP7PkE024ekh6rZg0VZcfRIuVvjthbql_GRVYI_gU4mJt4tO77t5kuITzVspVJsiwX0XVyHRYv0r-dj73H5cnmAPNPn4M5Y6AFQyoZZxMGec1EaTyWmomiijEvzDe0u0RYti_c4LEPnk3NcMWa6nJwBIgYmiFafnpcDxv6sN4Xtaz9qfnJTBPP5q1POJ9jhvC1dqB4rkQVRZLMoJ4_XREtxSi5tqaR6i9QG0yJv3ZRUZILyOuImSX05BCqHdB18-hUg_nPQ6u_2OogOFplZh9rq_Nyh8OV0wGX60Gx4AoB6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxWlTIjgqG5YQp4WUg591trPrExulG4E7yJF5NyDs-GOoME51n4Zc3mI4W7sXJBMoG7RchDDtv6B4tZRO96kPTzGQNNkKr0Z3s9Ec8LUzNCZeWH5QqG7kfLKBUMUOrz4LZKVICuVTzSlkag0V8x0mDFrKolQDUazj13v9_enGEO3zQjhBqypI-ew73Ug_u-cMZU5D5DG0Ba7cyGDBtpMl4TjPG8otU29xCpWXJrlvkQAKUrC6iSjYg_Vz4amKY725gjX49jFvXblg2I1cW3WDDsosMI9wp-Y2jB0IvVzCTNi93fq7eVTDAwkfCER5TOBYgtyXI59tK3en84AjiyGGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=Mw6yAaUYd3oTZbVwNACBEQrXbJ0SgFBu4_D9J0QSn1AmzMV6-Pe_lfaPBBhaeuSYtjxSXhc9C240PUwFKQJAlQItCoH4d_-Izn8M8QEe6W3uQBBRXG2SUq9kgMEEfBGraWrXiLNc4I20jeZVFsyDxyC9P-qh3bgcXMDmHCapStx62VbpFXF0rDkYs7Xdw8XN1tuRRF2Jk4ZabifNMm-7b-C9ObWd2J4zhCbVzKcqM4HYLLGq5uHzwZlA7Ckx7ihHrY-OYRs0pmVSJIvuwAIDUyjetRVRAA3kp4XtKld4vKiMOg198IxpLnrnwjcpQ_yrbsnFZ5CNGlyleLirTBGRtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=Mw6yAaUYd3oTZbVwNACBEQrXbJ0SgFBu4_D9J0QSn1AmzMV6-Pe_lfaPBBhaeuSYtjxSXhc9C240PUwFKQJAlQItCoH4d_-Izn8M8QEe6W3uQBBRXG2SUq9kgMEEfBGraWrXiLNc4I20jeZVFsyDxyC9P-qh3bgcXMDmHCapStx62VbpFXF0rDkYs7Xdw8XN1tuRRF2Jk4ZabifNMm-7b-C9ObWd2J4zhCbVzKcqM4HYLLGq5uHzwZlA7Ckx7ihHrY-OYRs0pmVSJIvuwAIDUyjetRVRAA3kp4XtKld4vKiMOg198IxpLnrnwjcpQ_yrbsnFZ5CNGlyleLirTBGRtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxNd795Qo74kivnjdwwMV8ze-_sfa4I9Skr95TgA0unpyW3OKWnqPftByJ7NCtFMa-iJ9drcgJbiXSFGSG0GR4eDzcxbeg44oFoiCIa7VuVvLf_tf4YkxisUWZSF7hcKgQa_1vRD0csRGvxpvIwVwyLOMiL8Sd29Ktab_Qcg1Z_8UQAHRqoBER9DhMOdt-S7DdwLsNpaGIwdg8zRfpGe1WsWPYTi2TQXGAIT1sCzohRNEJ1H0AsQUTlHA5M4LzGTghIaYH8HlcHjHvh4KU-bTIIj5TKiwbl3K_xpu6UgodocSANV9yJBxAWshB-GopFYAB57b-yLvCc_YysYbE7xzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=WdjmCUWw_waApsd5wqnNgBOCj3rGgKD0lIzBI04Fs4WmdkeCNIytlz-Juu3PQcvTdveTKPZf698gP5VyqcDKnPE1DYhTIb0JvbtfbPmY0Q-oTZZ5fXZnFtCG3KbmE-Te5azozsTLL0P4Ay_EDlhR-ZOk50OAr_6YF9gLzSUty79N19oMVoXm00QRrOuHO-kKsSxXClLytpse8FmXJ1Clzmu1jMs98PNTbL3LenUsW5RY5ph-ieSIRxMKGk95MmkQElSa1LGwe3pr6PSLw9pFwhc6hKCkvF3wsdQHfjgU1aU7mI9HcDYFyZTlB2O7jD1g6f4Lhw0A_YL7Vgv3m-jlmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=WdjmCUWw_waApsd5wqnNgBOCj3rGgKD0lIzBI04Fs4WmdkeCNIytlz-Juu3PQcvTdveTKPZf698gP5VyqcDKnPE1DYhTIb0JvbtfbPmY0Q-oTZZ5fXZnFtCG3KbmE-Te5azozsTLL0P4Ay_EDlhR-ZOk50OAr_6YF9gLzSUty79N19oMVoXm00QRrOuHO-kKsSxXClLytpse8FmXJ1Clzmu1jMs98PNTbL3LenUsW5RY5ph-ieSIRxMKGk95MmkQElSa1LGwe3pr6PSLw9pFwhc6hKCkvF3wsdQHfjgU1aU7mI9HcDYFyZTlB2O7jD1g6f4Lhw0A_YL7Vgv3m-jlmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=tPt7xIlqiy-Shi69jsJHuRk_WLGqxbjfiZnPkJrYzMWGUYQiZEP2wwxM14z_-ZPE6dc_12rozHo6c3iGTGjRyhlC7h1unf_PhRx641pXum5zYrUhuafdmbocXgQ9-5rZp-rs98PYPUqJrR_QMig8W_JXvq6LFZyQkYFiq377gGotQ0Mx9D1PMzuxH4ZCyWxNhn1B7ExPfuYEb9nstVcS4bfQdlMvejsaseQFqkKbXSCyzrG9Qb1SqWxYtfvFHUXW6q1t_cpJFp2rQMinHLc5F2qhpmN-JFd1v30FegGt45Qcfvb9BXhk0qhX7Pcq9iC9RJ4FNpshnuEe0jFR8fmiag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=tPt7xIlqiy-Shi69jsJHuRk_WLGqxbjfiZnPkJrYzMWGUYQiZEP2wwxM14z_-ZPE6dc_12rozHo6c3iGTGjRyhlC7h1unf_PhRx641pXum5zYrUhuafdmbocXgQ9-5rZp-rs98PYPUqJrR_QMig8W_JXvq6LFZyQkYFiq377gGotQ0Mx9D1PMzuxH4ZCyWxNhn1B7ExPfuYEb9nstVcS4bfQdlMvejsaseQFqkKbXSCyzrG9Qb1SqWxYtfvFHUXW6q1t_cpJFp2rQMinHLc5F2qhpmN-JFd1v30FegGt45Qcfvb9BXhk0qhX7Pcq9iC9RJ4FNpshnuEe0jFR8fmiag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ1Y2sBrGmxo3XW3STsNkByuN6Ip69AOz-17qwvl2x1GFmA4aYveGz-tURgqcEYdnzGWKebd_129Py-gd_NgI9IDx_Dqb6Vslj8hkRd0tgCWBIPP9R2uaAgr6LtrWqJ8lxiPCeWYySMovif17McmKSSud-YjvYbLS3tXvGi94lh95RfwokGpIQuQ9IT4JpNKCgZMjzf0cTf-iKSp17rovU2w2Ce27AG4sgH25tXqwFdVO6H6VfOuGT7A8gzoe3p1F1is42CzwSA0brpHdoB7iiL6LT7eDeFDwffIcUEMRUBBjUsFsl197J4ManP4PWaL3JXRg_HWd8Ql84fwKSfn8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=Kprocy8sv-SjSPu39TTopqZdW3l9nPx88OZohfsVZqBCLMXBhI4ckg8Q4i12oOOHZUCLe-tpfOuy-on3PgWZTmFLxij79a-DB2JmMFzS0hsp20ARHUAVr_7N2761klIDNG8gmyWz5lwS7eeNA17QQj9-EqcQb1vWD6JFK5xN7gjEC_2b2ThlPAjMymsbB06k6TqFoHwTd6IztQRX0y1gYtKtJzauKUi4stRC6yxLXLWer6FjbLw0u76-u1gVWH6VbqHb0aahCnsb22sHu9NwOflr-bCFfFroizsxoktMD9B76HJ1crz2E1a8gsefboYacHWWP1WzNINgbYpbVlVxrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=Kprocy8sv-SjSPu39TTopqZdW3l9nPx88OZohfsVZqBCLMXBhI4ckg8Q4i12oOOHZUCLe-tpfOuy-on3PgWZTmFLxij79a-DB2JmMFzS0hsp20ARHUAVr_7N2761klIDNG8gmyWz5lwS7eeNA17QQj9-EqcQb1vWD6JFK5xN7gjEC_2b2ThlPAjMymsbB06k6TqFoHwTd6IztQRX0y1gYtKtJzauKUi4stRC6yxLXLWer6FjbLw0u76-u1gVWH6VbqHb0aahCnsb22sHu9NwOflr-bCFfFroizsxoktMD9B76HJ1crz2E1a8gsefboYacHWWP1WzNINgbYpbVlVxrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHNxHC2mTq1LnrrrwVWb11onyQyYhSLv-Nae7EiHvXooGx-zZIxVEME0SVT-rc3qEIrRYOm4v9650Q4bDVP7Pu1PPhH-j_fZV7f4T_EKY-nGNYqkatATy7n-04syThbJiFpllnKyCr3NDxeHVL9j7t29wHGhy1q-CU_QIVTACmMO4xGi9TXc2mLPeltJ6QUmeER1wagnd4uw9bR0UNKvuhXmKqF-YRe6CZCBtj_GUQOuTMh2hgY6G-Wta5a6IDd7crKzrQDdAuie4PFO4PSesxQmLjWBd05kt1D8Sq8afLLtuOszJJC6dD3-EFqSYaspmuu7fDG7aWSFj3esAgTwWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8mOJqDu4Z52xquUbOHHWjIJqaninS46uC_V3yV_OHlgG7maJSRC64KPQ0uY4xhXDNV_Y-Sdio8oFbXM2ks2pBleEq7pu8GSpq-1uYW1rJoCIn845ZoJFm00LywsMqXEE-fn3J2zS-82LWpkPLExFWhGEBFRb5KeIVaIPFhniP3q4XZB5oVpzi81zXX17stiJOjlrLf5ioT9usoug8udFmo2ick4Pd5ClRDdXN2FjwSvtsqw781GGlzfg-TMdb8W5fZqv2tsNmQFQ4VMdxuo-ohyZSJCeMvUA6-rSgm0NWvK_RHvTXQYZsO6mzIalShdit3gIbewsbsabaJKQoG0uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUNWMAX2Lft-n0_8z8UlTX1b7Q46aHlNztei6sedU_xeR1UzDq-PvQn3HZjl1KRkngJZO_X1JfrTqQEfLSEsXcYdtCfdTh5c1XTzkAPO5PMl1FENlCorv4kBjLFIZA1pqRjPD-1WHuiYzKLWittzEsbcT2ZVtdd88l1J0liKpQ350XLmmm8AqBstlKwGw_N2eq44VdFjeAmzb5MmF5FOpcYjvp6fJYgxXMPXzWUIjtsDXmQCvkWK5vNvvtzzftx45ZR3wrCOz4WCgZDEXvRyOEPSevC_BELCvaZfF1ayJT2wG89W4xMdYWNCwnROPuBFdXjCiLeo2cC3LFCaBXP0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtISVqo3tLAs5d7GQIYnl_B4F6GnkoJi4KXsZO4vYdZI2PCUG6QD8jhpYHk2sxh8Y9ROH-Nkzpp0igA_LZBLlSREDyfp02S2W97WmgNdYWR4U5MK-6KE3tOHsggQYu8kgx0aDsx9242UVxOLaN60bb1GbDO2fvOWs8ma0iTNDTJmkUiIdGlBS9Mgc1GFHfoye7VOvvEhZNvDLfQroBQk44wxHpt9M2Mas-SI2D5s6ebkRUP2f76zqmJcuQ8ECc9KzbQuw_sntHTK6FCaOFan6lyiJ098wXst36JlaudaXFB4W-1LRG3Dp5gYEZDMvc3pbDi3E8IkVNQSf5PHCbYn8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
