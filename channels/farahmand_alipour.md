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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 20:57:42</div>
<hr>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re8Ivd1acJr2AYq_VM7tBuV0osFyLtc6mK3P245ttOu6Iq2qX76CrvfRCjBeqGzRuFp0QFj3RH8k0gFxMAZTGrJ1I19OFWVpaWxRrrlRAuw0p8l78rRk3nhQazHBXnNEHr2a9DqpwFos-ADwLJnvCNYCqQTT-ey2M7sDqj-KJdKgUzN-WMl8oSXrc8gHUjnty3LQsfP68x-f1-c6d2tbS4fJ-DG6T-UMDxZxtslrKxFaTWHmMrYPxDJZFJpRvEBO-8Drgiqbl0iK06VDjyPApXY3CgfxcA7oJflirROvqrGRY1LuwZ0feiJEkLq8FoKFH3kb3DfTcTbbHHoANP03TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=EKV-mxHILkQ25pkiYWeGMXFoA5nu0GnK601VfxkhIrmDmaDVqTD4AMTJSAmZ5EtkqXBA9H8nsWMGyZibx7FQbeZUK40ge0YafVcSc_TaL2e2YLnCUYlNzYTLb_-YmcFPCrI2OnAu2mZfcf5V3mru_FWPgZw7J09YhElH64umP-ul8TuZWnNgUHftJznDs7n45J6i4fiSEHL3SFUAJJn5vxeAk8ui3JBql4RtztO5KrQHYxV2purCnrwaobae-kFVTTEURo0RyKLIM6G8lMOZknzzm8lw-gQj0RIjUqUsibHVTD7tZCK663-VlslFjxJHV78s2KJfoacygfUNyF-XkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=EKV-mxHILkQ25pkiYWeGMXFoA5nu0GnK601VfxkhIrmDmaDVqTD4AMTJSAmZ5EtkqXBA9H8nsWMGyZibx7FQbeZUK40ge0YafVcSc_TaL2e2YLnCUYlNzYTLb_-YmcFPCrI2OnAu2mZfcf5V3mru_FWPgZw7J09YhElH64umP-ul8TuZWnNgUHftJznDs7n45J6i4fiSEHL3SFUAJJn5vxeAk8ui3JBql4RtztO5KrQHYxV2purCnrwaobae-kFVTTEURo0RyKLIM6G8lMOZknzzm8lw-gQj0RIjUqUsibHVTD7tZCK663-VlslFjxJHV78s2KJfoacygfUNyF-XkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRkNt9P_K0cLX0X1iCZoQfyrbNeOd_JITf75SFDcR1lVcltYSUOBfL7nSm9u8yzj1LlAhpNTt7Zm7wG53cl8PGIUGKVNZLLBYSNStKSZ0rTm1cvJR6lkRS-NE63ed7WZqWQ584z56Fj9tiRjwhGiQ0NIBagqU3Ip19kHXNu7LWcs1Q52OWwuslV1-OKjej2vrM3iixpL_s2iMM1pw9LYwIlUhKFggRnRyt6j8-qSQz7GAYSgtyRkc1GBiytPfid7m-w2UgPEYWa4zDMWTGHi5HLyWLfetuG8KlP-bs-oh0cnqP_AvCushNna2NMtHtkT6CaSMVBbsCbBlHgcn_y2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDMrI8sjMdcQthejeq3gW8GtkYqzNcYT-bFT8ZC2DlPDU4fC3yWfDazNq_DUd3YcFLcoiZFB56PexJFyl6MtXaAoIdZ7f-VtFtAMPZBqQu-RRBQY4jBw5MYX9JWYyge9xiS0ah0IvUgULsL_YAQmDHcixHj8gzfG6HmFoc6kWHkEb8oND8MZq6KXqG_ZP3FSmG1ymI5ayI8mEfiYD7FeVEFQzbwH8GvKaf9HS_XMUxGzWCK0nrsA4JKMzzJaKF7JcxHJLa_ek9m1QwQxHXqj5Cvu2CXuN4OOcYlaRtLf85d03HpZRi8I3j30cePJnMZKbYcMXUCn4lxXkZrk6RS3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKeAfFFZ7yFs2dPG71D-vguS7m_tGyjrM_7aOtKZesH3NAfyjMP_99LnYrvwFw12YerUneqhW1MnozlIg7sCBNZifPjorSA5nOuLG_qjkG5qed-ezX3pwZql1ZPKQORgh1OvDRA0tm6sWs4T3WjNKeWFH1zfuTgsmEOL00WffrKXZbkHcv7NZLA1mLVyLWZDQiNMPJxZGzE7LWYf7W92ciMlPb1sCxi9wKEw5HoWy5FIvB45ry39TeGeEx9AIuFbCPAWILoeDNe8QGYvtSggjoAxZtUzZfXQ7XiX6xHPSYGAUmucAu80xCT17Obm_JM5rcaLNF2hdZKaKf9eer7zCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMnAwp12NlLaDoxqO8kED0rGAKvT3WtaoQKSJR6_RmhFREk4uQ6s7PE2f93UJYqczht6t3pWXdFom9kuKirSPPM2WRtdhfsUHsDVK6b7xwD_gDDTkXKjlmTJgo7mQO6DkLt7b4S0etWolWbvKFylF9UNyfIXPm2RYZPLPIAZB1gG6LLlnYPTPVR_ArBRSWotu1PDSdN0jri6Ld5zG4G4WvsJmQzjpQO-SENr_qsOHFzVPhRoL-86RHLZQsiJ9mRUtgQ-6qy764CMwM1qwwYzxiu6t4UFkeLwunfxQz8DCgfVOgoDsmHE4hsbcv0QVbhJo6X7j4u_OCZxg7hWXk8rtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbwKMmlnjznzJhvSbLyX22gPN8odk7N2FNb0tye2wyZSqMvKL0-QndjFI_6t0B2nhdV7CfyJ-WepjxSNvQjPBveoNxCC5NABxPlgt7PrXtTBLdyUfwUBQ30ou9oQy2TA2cg9IbkSQru_5EKqMy60qHwvMyjEJl5BVa8ywaPNswnVaU9FdQoMUBMUY9engmHcc5QIottiqlyZShFsS-sVJ7BcDGXrhKOlvBrrhHLI-lLkZrsHO3BEhiavfJ0H1YZ0p5JSgUvEulSaCoYGV2k-cdExFSQb7mDHEFcvAHwrA2F_O2makb6davd6Lw29tDxsj-GIq6Ps6LjVBlqKuHjHVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZhdSNZMTNhPrdn_c0Q37go-aYeV9k_WeiNGEivhwCCls7qEZG0JxEZx66UAodM6VNLuHeYCi-qneQyZ77HQ5qWpGXYf4D-dQHy_zQPS6RCoAJ7KG-dwnYCodpm9-iG9j9WNZhleZyohhqxOaaxmcgl2YJBbFs14-heUH8bt_O43xlr5KHnYrRLnz2ppTJ3ZYE3dN3bx1WwP--NaokdISqQcRUeaaqdmdsax7fLqUM7Jg5aGTY_d8AR0DR9OZYn10su335YJIAWsjW_rkP7sSIpQK4PprL_qys7mbpRgold2J0T4PMvR6qCJ-Ovu9gZg0ozmCSJqFpcRr5aX5U63z_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heLtQGoQm3U_dKoJ9Ybrl9Yyuc9tzxNpvaaC_4qJbuBhBrdy1qbPPPMsM2mATPKgfb768tgujBt2YCP0YM3vlXFPAZnLwVeiehC33gBEu8Log4DDxbzPKWs4wd3yh4yJfxozeJuM1sQMeVgrgk117Wf0Yd08RvqcQmmIi2eZYnrMWf-oh7db7UIcQz2gqTBAYC6FTIBgWVVonS9ogDXWpaNQMd69wlwscIYcKmrsQdlfOjDIBJ8yQ8J1gMTIalssxcIwWWPTnv4QpPgVX9ZdhtOY7gYAmDLxH4-t8e_10f3LVwAKFW-M9rhq33Z3uxKJ2AnkYf3r4uTQXfkFfO7gRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=geUq6VYyZytNh_46FIlPUbBnjNInuVq0lCJlWjQcHRXvy3WDcv8Aq1xLFmX-VdaYEJu4ILKykPRPc3ARQ9Yf4BN1w6byeplh6XK3zbKh_G1kC_doC4J-Kq885iDwbyUI-pW1i91kvs32-ULwDMogvg2LIfWCZ2_xShnikB3jRb7lPRLvLpNdqD5pQaB22szoZLDtE6xQavVXN7KThLhzzaLqT0MuifJA_C5N1X825aiQzXyZTDdwnhuK70OlpB1-8uoWRF07hvhuMFKOrXBl9OcJHcCP7rQlMJ8hANt1sr9c4J1Opaj5mij4bTO-_bEUWn8kYxAhm_tv6AnHdZRIkhxJR5BqIN09pGJ_N2c6HAAihowqIUAqvwzbxYqG19OTkgSjTQhKyg4S9UNOQ3elGJDuodkRtnwrurNI7yifqul7aN2kRYr08ZA-eoYy9JZsJSm-m1tPPbQwRQm6eOJLozJbQgyxmo1gu8673kWmCVXX8-Jqp_xoZwIYi9rd0exPXVzGQVpOtlB2FZ7SdLA5ILvFKBYJbTuynjPklrgSVAnhm3QmZ9mvuHCUySV-hEbtE5zntNm45e7l9_M_Mr8eP-tMtDEPnpWr2a6urJg24t0MBemDldK_1QHJ6G-100vYh2hj2L2CtDoFO1Xolu8HjwQVIwKNn59NMnm6pcCzrGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=geUq6VYyZytNh_46FIlPUbBnjNInuVq0lCJlWjQcHRXvy3WDcv8Aq1xLFmX-VdaYEJu4ILKykPRPc3ARQ9Yf4BN1w6byeplh6XK3zbKh_G1kC_doC4J-Kq885iDwbyUI-pW1i91kvs32-ULwDMogvg2LIfWCZ2_xShnikB3jRb7lPRLvLpNdqD5pQaB22szoZLDtE6xQavVXN7KThLhzzaLqT0MuifJA_C5N1X825aiQzXyZTDdwnhuK70OlpB1-8uoWRF07hvhuMFKOrXBl9OcJHcCP7rQlMJ8hANt1sr9c4J1Opaj5mij4bTO-_bEUWn8kYxAhm_tv6AnHdZRIkhxJR5BqIN09pGJ_N2c6HAAihowqIUAqvwzbxYqG19OTkgSjTQhKyg4S9UNOQ3elGJDuodkRtnwrurNI7yifqul7aN2kRYr08ZA-eoYy9JZsJSm-m1tPPbQwRQm6eOJLozJbQgyxmo1gu8673kWmCVXX8-Jqp_xoZwIYi9rd0exPXVzGQVpOtlB2FZ7SdLA5ILvFKBYJbTuynjPklrgSVAnhm3QmZ9mvuHCUySV-hEbtE5zntNm45e7l9_M_Mr8eP-tMtDEPnpWr2a6urJg24t0MBemDldK_1QHJ6G-100vYh2hj2L2CtDoFO1Xolu8HjwQVIwKNn59NMnm6pcCzrGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_iNKRqUyxHXgBrM1n1LYr8RYWDqiAuV6k1jHakbkrPsZGjlvwLCYzUfT3qEhDZy_BiaeUomyCI1RJyMAz3ziSwYLV2oTH3xMy11_pT89ZrjXfRECs4FGqx__7gmg102TqozSAjipNMvpDVYBIWwgstblvhUXoBGZ7Vs_gIAKaLJyKjkDVpkDouvSv6ib6c-0tPjlZCewU5KVnqZzjvNy43FSjh2sXWXKYdR-8vwiM7ok7h8ydpCBCX_ZdgU9udNmBJxqXtNr4okbzGyWvqgSUc2zUSFkSpaFbHTZ9XYICHdWD9e-DCWmXqQetSEa5s_0J9nw0QHd5UKnsIcbbsX6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=HQyXG50YrZi26-3ISGnPrwd8JtvCnOsKxKAC436Rb3QVkDt0zeWoENRAxc06Fx0p3s8fo2HenahmUFLQ9tJBLrJJuOHo_g90UfMZ9G0EVrXGdl-ZLQ9NtuxkELaO4LkDtxrlaivsLszKyR7NyWd1tAI5Jwa1tEbq4l98SJnFsmHB8J3v7ZlLxRTR_MB1PjGGqeacPz9-dnrKUmXcsVBuzWPhVL_xknRYs03GABZXPLLdlPfzn6gk1Z4UKkQryoHz4xI-kU-kuKVB3OMlY35kU40EypqW72cjN82HD6VC5Ks-AshMRGVX7jSPKDIkT9dKxtxAEj6Kvyequg0KqkoAMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=HQyXG50YrZi26-3ISGnPrwd8JtvCnOsKxKAC436Rb3QVkDt0zeWoENRAxc06Fx0p3s8fo2HenahmUFLQ9tJBLrJJuOHo_g90UfMZ9G0EVrXGdl-ZLQ9NtuxkELaO4LkDtxrlaivsLszKyR7NyWd1tAI5Jwa1tEbq4l98SJnFsmHB8J3v7ZlLxRTR_MB1PjGGqeacPz9-dnrKUmXcsVBuzWPhVL_xknRYs03GABZXPLLdlPfzn6gk1Z4UKkQryoHz4xI-kU-kuKVB3OMlY35kU40EypqW72cjN82HD6VC5Ks-AshMRGVX7jSPKDIkT9dKxtxAEj6Kvyequg0KqkoAMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=KgLJjhUxqe1-IoKIgs-ys5ZkjrcO8gyjswAd4zdsvfjvOVnDhgVUnXVmuzQ9pWc6YklAGc1BZA5-gpEHSJzmgBQWfsCrKNr2xTK7hzhO7o5I2xGZ2300ofm5NNxnoanPWgBxqC11GwkPqpx8oQkr648jihEGCVCEGTEJWixxuOl8fIe6istKcHcplK_5EvWq_WoCbU7jExho-afZeyDBsbfx1OS2HmBYq1nWdWWJ4uSb6etswAbnm97KcxErIwlzKUNYIUiULFRfGj4ReNXfIh6-LDUTQaw-Q158mei0ML5NQK6WGx0xw9JTkUfjpyFBCfUqhCs0pgNALz2E3-ppTlKoeL39ENymC2BNjhMSwBo9yDrlo3QEU0xIRJmWHeuuimKKBqNMgoiTqewKseZmOG3F32TkH2dv5kRae0w9u8qbLjaDxpDy19IRCtA2pBXGlWKqvawO2YPBb981CeOVrV_a6q-sNV4tY-SCgckzLu9R0KC4XoDIaG9AaX4R0muFaabOncdHC-qf5NvJv3aMJ1yiqjHqd72LIMeXSZCitPLQqVBUdLyAAfr96i5vyVqBMZbjj0QTSG3AyTGWIut-DZiIzdSO40idYqGvywOFLOLb6tbNCp_Egln15RamfJX6gL1yUuW3SPPahPhwo9QPaAi0BXzHnoBBzsi_qoiwyxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=KgLJjhUxqe1-IoKIgs-ys5ZkjrcO8gyjswAd4zdsvfjvOVnDhgVUnXVmuzQ9pWc6YklAGc1BZA5-gpEHSJzmgBQWfsCrKNr2xTK7hzhO7o5I2xGZ2300ofm5NNxnoanPWgBxqC11GwkPqpx8oQkr648jihEGCVCEGTEJWixxuOl8fIe6istKcHcplK_5EvWq_WoCbU7jExho-afZeyDBsbfx1OS2HmBYq1nWdWWJ4uSb6etswAbnm97KcxErIwlzKUNYIUiULFRfGj4ReNXfIh6-LDUTQaw-Q158mei0ML5NQK6WGx0xw9JTkUfjpyFBCfUqhCs0pgNALz2E3-ppTlKoeL39ENymC2BNjhMSwBo9yDrlo3QEU0xIRJmWHeuuimKKBqNMgoiTqewKseZmOG3F32TkH2dv5kRae0w9u8qbLjaDxpDy19IRCtA2pBXGlWKqvawO2YPBb981CeOVrV_a6q-sNV4tY-SCgckzLu9R0KC4XoDIaG9AaX4R0muFaabOncdHC-qf5NvJv3aMJ1yiqjHqd72LIMeXSZCitPLQqVBUdLyAAfr96i5vyVqBMZbjj0QTSG3AyTGWIut-DZiIzdSO40idYqGvywOFLOLb6tbNCp_Egln15RamfJX6gL1yUuW3SPPahPhwo9QPaAi0BXzHnoBBzsi_qoiwyxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=mSpGvxeGwpFodENB3dtzb-PALD5KdBvPr0qqiaQY14TKCzyjPR8m1ozv2p8orr9Skh6XqKw2mC81tkWhDYzDhpqgUV8TMmdXeUa3hdkkPakmvhargki-_XnRpPIY1RRyn7JzizwdIje42hhUfotC--b2nrj4CTNeYqam5x4COWGvZtB-M3k9GVDiGPJeLbDpm6_9f1hmjznn8fFQhJZ2bw4JmhppP5mKREw5Wibv7AfqpRC7y9AXRDFNPaWCqZc2v7yQvklG_SMFr0C1_QMlAiQnp3k5b_fHaDkP93k-mFuHjnQV60auOzOSnXe4E8gKb0IFxH4_jB46yyktzsx6roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=mSpGvxeGwpFodENB3dtzb-PALD5KdBvPr0qqiaQY14TKCzyjPR8m1ozv2p8orr9Skh6XqKw2mC81tkWhDYzDhpqgUV8TMmdXeUa3hdkkPakmvhargki-_XnRpPIY1RRyn7JzizwdIje42hhUfotC--b2nrj4CTNeYqam5x4COWGvZtB-M3k9GVDiGPJeLbDpm6_9f1hmjznn8fFQhJZ2bw4JmhppP5mKREw5Wibv7AfqpRC7y9AXRDFNPaWCqZc2v7yQvklG_SMFr0C1_QMlAiQnp3k5b_fHaDkP93k-mFuHjnQV60auOzOSnXe4E8gKb0IFxH4_jB46yyktzsx6roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyjcuNTl8cKks12yOBN8cWLGmIoAdO0AI2GPxY9b6q8wfLv-Ymby0AVdXRo6Lw8GdISifd7m8-CivgbNFDCPtA1nTK8bE3gTTYkOkNAchyF_LcSca39v_y00UKbVbaDtrXILtqMQ1iXS5HaaUUdNt1TIYDggt7N_9GNzGVIwXakAqR6jE1fRk29qFG1NYnjSDbSwUMRR5q70IaEfWhD64AUkfNuHvYWMikmCvYBltqo00KgECEW8WQ0Bj-rzQHyUPgb7CVuUT29W-I24S8xS748yUOVlfV9N2zteyLue7hwS_zkkj8rs7s8-CeoXDg9MFuZ81o26SyaZJ6-r_L4bjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhMstQNZ-8ppcxRzi4FlyOKKkicX55XrbPBulqQqO2pKDiO1AbOhtSL2tuD2Nc2WtwtgXdbfpXxmmvpAHp06ENg5p1w2lDns_4acynIrRBcQ1jbGY5bFw1vhj58nJq6-7yzzvay3ESyIYMkcx63e8h7eLx8bayaX_qJhSYhp6jZB3UZSMlhYY2_5O1xVD4-5GSdsB0g789Mtvqdlz3RG9jxhr10BOmbFmJqvcbMMGyUD0bt3Iq0rrVs0yYHTlFWsq46-2M1UjJUQamnyEOOdEGLqQX1QHJ2WJSjcKA8ax5O9ZDLaIrm1yqwfqxVtVqHkrkTXjlKOu2650pxnAtme8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUcELrQ6Bp1OFwb4OPWYjhO5x4PGjGhHtmXc0vmUsBYLyeHCArFnRhnmv_xyHaDCjI8kRBZTn5ymeIPgppi5h8y7NCXplq0TiEjxR4WzAVxKPPZvtOqcvN38vihgWabBpYtGuMv6Un41trktqSYRFieMPL6l3Z9DtWJsmoKvZc-3PHUiEeLwGjskg_ckG9X8Afr0if3bFnedHbH1c6XaB3kVjZdUhd116CI9Xf-OUWMuI0NZIhpymK1goeZOqNd3F02WLEFZgpFihSp_J-cJQOla--8HTmbfBYQOsleVjxAX7M4eIknqPk2AfWdRh4O15vp8vrlUl9x9FTu_8KP70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9F4hWMqPIB1oHm_teo7HiQdDpe8wlNjJ4T6dVZwPe5DssjJpZZBJLJamxb9s2hx1rO24vrqXlLAG6_su1CW-N3jvqLu9dWhL6oEzva2cMbmE0WKOGyM-Vqy-Q50MeSOXIkOurR1cxC1303GTF-59IGP-PTgBe1P7lUeDRderzU5jjBJqW6nGqyqCQ3RHFigthRw39ENlueazO6tUgcWbKzNVNmJCeZfDE8HKCAo9vo-QGG59gwyy8nEbFGJG6ccuIxlHs0F-EXkRcpRESeBm6vsjkmFweOLfbboDOlCrkgMU3p_iYbeib2F-yAHb55cIeO0U4iXje0NGBjSnYZwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCk9wBS9tU_uw9c6374Pb2L_94FUdWhsOirfHcYpxsXK1b9rF8RQjDEjIRz9V--rOruL6KQMdiieYBo6wyjkVW-vLM61xvJt5-h0Msxnmcsesffd-Dtu9ndlvKkLRxVI6w6zlgu5WGQeaTJf-ZOuYOci7VCQQIqcvyfEfbtfIQJvkqYRtRN9M8e-SF7YbWo9SLw6fJ4UXFnWjQn3LfSUohmmz3rKm3VCOMZlt2IfK5gcnA2NxVKbwGqkDM8HPI3uB19_7rtULcXDjK98CYmi9IOTpQQEmaE71hem9-OXnteZwkOKFIULdGYg4-EG7BJu0j26mn2wRYF5m_4G-6BMvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=UifKMw6oohxXXwDy_DEZy77Q7NuRMoLSPnfQg3Tga0Z-FJ-24_Cvm-sVbwl7TFmZxyu9QSYnt47sIlc-r6k1mDu3ruGWXbQfVMTc5_IAXSTogtKGrQC7Bru-XHA15ePNmI29nlfHaZ14vHdhKMi72pfvJM5PG5OEK7avmKRIccnf2JWfYdF61er95F2aZTi7E4lnOLITgMpYFIxl6XL7rDoyWH3Fe2mOG3zRl0l_Oajqtpwknker-gqSC2SNXkVsEYs6unE0QY-d_NFswJI9yGJ3Yrgcs5ciKNb0W2uLyXxHQYLBh3oY0T9Sur53g8xJfVYznQ7n35EF3hZx3MG93g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=UifKMw6oohxXXwDy_DEZy77Q7NuRMoLSPnfQg3Tga0Z-FJ-24_Cvm-sVbwl7TFmZxyu9QSYnt47sIlc-r6k1mDu3ruGWXbQfVMTc5_IAXSTogtKGrQC7Bru-XHA15ePNmI29nlfHaZ14vHdhKMi72pfvJM5PG5OEK7avmKRIccnf2JWfYdF61er95F2aZTi7E4lnOLITgMpYFIxl6XL7rDoyWH3Fe2mOG3zRl0l_Oajqtpwknker-gqSC2SNXkVsEYs6unE0QY-d_NFswJI9yGJ3Yrgcs5ciKNb0W2uLyXxHQYLBh3oY0T9Sur53g8xJfVYznQ7n35EF3hZx3MG93g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlQztVzhQe-1r4I5cZIWeL4xKVDa9ijuGCvfZuevIg5wgMG2VzohqEquLnT6IWtTAoGVnYE2KwhBIjvnefcLfYG5J5oBecT1OOuR0tWn305eg6xzaqw66AUKylTsvX7c3gYLdXuPD7pji5XcPO8_y4JeIUXPDo8ZQyAdpaX76Hj4DwZX9IJf5o9KWR3OvON38m_g_wXuMF9_Tz_2NF_1glUfejixrJ4tels6w1tDAPNakMnunFzJSiflDRAkuVU8diUu23qO_iKAlQISiWNrQ-lIZDx9sYumautfaWpGSb6b672mH6iIUQh5m15MJY3lILYIWigFpPbws7xcGS0ipQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ookyk2tTexxPp950mnn_gspFJ-GkT97qYYBmiCAe6pV_iv0Fkik5N9f7waBO0p02kkAH4sk_BOmcKSBDsCu1rsFNO5stUyAhFWrn8iiJ2ArJNdQFuRv1mVVOVthTIldYxTeIl1wOHzBOMs5fobtQb9sEMbSkTg-olvNhlHzbeTZsEJLu2ir1pzFl9Q3c2Bxh1qtNx6JRDJ8UlWLtxZNcWxrI7x3KawZ_wnH5SFAhGD_KwPYju-FNH5E94a2U76MPYVBUKXe9Q4YyJlJJsHpe1euM8fDYw3ysKXtS3mz_uLP8WMqwJk0trzts5qgmHI-Xql9PjSPMYBViZ1-hQEC8KA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6QphQ6k0JcqYCKVy9fbl8Cxv_CXnxlj1urnx8RGgFnmWc210Vp4ZTy1A9iLRN1UQK41wfKuyqAguPFU9pRDSgiaSPXJZAMfJIhesER-kSSQZImhCmOgGHDqQtIFQW90OAZqCr8_N5yh8Bei5odVnVFp-EQJFbkZsUyjDf8vua6f0eeY1y9lwt02qhGwF6VZwC1mz8c4GA4bj8_rWb3i2ux9DxENI4ySw0HND2lHS-JQw0LtJjebUUYNNrrBEDT26EKkIUGF3yfYihgjQUZHp_NK8BW86SWEfJ-RY6UQSHhaLlhBztQ3m2g5HiIbM3O9fZOW1saOR1UisfB9g97dPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gpa774GGSd7Rt0BNa_05bHgONR_RIdrgfec_-Z0Fyj3PIbegCQ1pAJtw58BnmNrmpMVcfh4Ttvmfg5rGqYpcIwFFztX2krcnQlMZ7FQ7RPFmHdHKkJppg2a8-w52E1sF_E-Y3_UUL9JKQOW8-oXsg8Rcqoq2UG15gT8NYVdkKl_6EHWHFDAUzrd77XhoZJ1vpgsDKUKcPEO-eyPpmVztXPE2iFAR6fOJweh6Qj_l9BNxnZqUrU4B1xGeJZHGCWlFYW7vRKw6KA_LhJKhpZKv06DVdIj4rc6_cWUuWITOjpgJZRkUJoyuCvWGeWVX7CPZzW_3CFhNKPY75Q3aCsAUiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyKv5O-jouQ-2-1HRbspL66zmfkLySKGXdnQf5hj8verZW2a4HFWRb9j_B27bGLLKRzWicR0MG9zjmimkQ7IaiKUh_Z48dL0dQ61SojwnnbDx8jrHRaF-mdqMK7THXp4r23r8_tlLVzMU3lmIE7vQUtC42H-dvuUcJgb7x8-quub_IFHLdbEjDUvjmHAwfOYM71ymKksexyWadenY7DloDaa_bp0AxtEf3XPzXEFB7CA4VXU4Gl9S0C1s_HZOU9EZn6Nzy_rWVdMPTuxvZzKjjvcQKgkjy-DkY8Knx8_7jnxOjJTzNWgfrV9LnA13BjzDdVISJeis74wnpGOzMoXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVR2KrTofYnF1HeT-otyCmSG_rOW01_oySNhQdgfeplA_IwFOK2iE6b4dXN12je3dXaIYLEr7BEbEhgLcbIS1xKNPvn8I1j6kfcTn8kxfSIsKkuNhx6GoNv5QgdYJirSeP2-PO5GUTzN-oNd7JdpUCfHgoFaKXBMfnxvWgL9xBaflVjlE1mq5ksW-hqCovlqDCBFu8a0hhNYeT2qws8aprBoFd5u9TsJR4nRs4BmqHfcomteoDF9TLbxMbGvYBm7gjubdt7ZTbz16TvYtqxEVeQ1jh4IM35Cw9jNiiYYuOL6SIUEHfdldgyGwKmJRjQNTdr5Ep2aJnO-8q3sR-jakw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixDo_a_g122VzyYUjflgb2LnlfVQySjoCsNHs-DOsUdEmFNrVvDLCb5yrJyoD3n35Q0LTDdjNjOwPvy6hlB1EOMDxdnNEfYK-IY8NLTxRUpKVt-2gwN39b-SOe7aSzU4elPCgogg2eG3yil-KFAAQy_SepMHpdpJO3inEUJiXO_o5COMINZHq7gONPWYJ4-bX6Mel6M4ow3t2cvMXy77dGONVppWGHZpmuHOdzU3G_Xyve1y4406V4zFosCW-q8GdJjbj8DAjrZvM3eGE3_yKSoYaJ5CFOAfI17EUOYKjBZGkP-VvFM5baUMyf9Cg3pDsIiuG-PphMO-fAXgoBNiwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3xAv32l8MfXT59FopWqzx2AqML64_05EG2s9O-A_M9JuCzQI2ePrns2SyqxC7lS-vQGWDzlbCHG2Pw-Dv1QqUkQ_YVyTMm2TOqF8J9GCNWF9IcQjnW13g4sD1SKM9AcrwCbjgbrMPXvWNG7AP4B8y0tAtwkpmVTw_uIScN8Vf8VMQaXcAxhFrHoOKzxOoyJ5p7e6WQav9m5rZSwEpVhWQ6yph4_7gn809zcu0XWLK9x8J8AV050irJJJErHrEXPlHCTt079BArFuXb02kJI-mydDqX-fBJPoc9pDSYRTNlRtCsE6EkkT1DUcRUdpW55ApNqHaGEjJuoV0iYCyS25Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=hEHW_teM7XN_83z8q5vzAkjf5k2vzQEXNdk9r5maIPfEpcDansB1dJaxPO9dyHQIkOesDCi1wif8AR95Ma_eGD1vnrb7LEtYb9lDMg7GjKQaVxvlhOf-DTTvjV9BRXiQeoneWcvaHWdrW_PwzDRA47Mo-LSu5p7xOh1t7ZYu0snRcBc58EiE3VjrTngj6hgMVBm7bLu1zmCVSdqPbmofwoY0clcDGzxHsZJdnvlEfegNNPHZADnFdKuGjj73ZnbXAXNy92urmGJPLdQLWJs6zdMGjFBskVoVH1g3ZY3IE9T5U8LqnB18c-3XUskUgLq_yVeX4CgrkArHB42JSB3X6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=hEHW_teM7XN_83z8q5vzAkjf5k2vzQEXNdk9r5maIPfEpcDansB1dJaxPO9dyHQIkOesDCi1wif8AR95Ma_eGD1vnrb7LEtYb9lDMg7GjKQaVxvlhOf-DTTvjV9BRXiQeoneWcvaHWdrW_PwzDRA47Mo-LSu5p7xOh1t7ZYu0snRcBc58EiE3VjrTngj6hgMVBm7bLu1zmCVSdqPbmofwoY0clcDGzxHsZJdnvlEfegNNPHZADnFdKuGjj73ZnbXAXNy92urmGJPLdQLWJs6zdMGjFBskVoVH1g3ZY3IE9T5U8LqnB18c-3XUskUgLq_yVeX4CgrkArHB42JSB3X6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=BLwu8jRr0yaSN_bhHjxH2YazvoQOYtjqmNOXFDzflAK9_9pkdPPeD0vD2OBk7ibENLiD1YDqSdZUr4xpVgWM0rhwbFLpp2TzQSFx46i3Gso_wvwu7glNS3fQp27vMbQEPbkOi9S0tDe_AoARU3KBW4676IJOaV5CcgAdjbqFZ04YpIlDfhnP7lmN7BGKY8gqZUx2o7rh3mvBEKvEQSo96rWxOxAPy1Vzin3qrIzBsixPEXjFAumA6X-ysm3QRveC88HTupZ_jcxrIUh04KtJYlJbql9o_eNYBdW2VdsP98FAenbZQDazNSXFwXDX65pMENj1D_CE1nJhAPHcfWmQPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=BLwu8jRr0yaSN_bhHjxH2YazvoQOYtjqmNOXFDzflAK9_9pkdPPeD0vD2OBk7ibENLiD1YDqSdZUr4xpVgWM0rhwbFLpp2TzQSFx46i3Gso_wvwu7glNS3fQp27vMbQEPbkOi9S0tDe_AoARU3KBW4676IJOaV5CcgAdjbqFZ04YpIlDfhnP7lmN7BGKY8gqZUx2o7rh3mvBEKvEQSo96rWxOxAPy1Vzin3qrIzBsixPEXjFAumA6X-ysm3QRveC88HTupZ_jcxrIUh04KtJYlJbql9o_eNYBdW2VdsP98FAenbZQDazNSXFwXDX65pMENj1D_CE1nJhAPHcfWmQPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=EgbBMDJZmpTamczNv0Qnx45Ib4CrmBKbz7VVOKTzmiY2kCGxwZNURkGjZeCDD2-p4jbI80kCjBirTiNy7kZmCrvtY3gvFQ2aj92wL9HCobL_v5DicQMH7PW1PGxZjYvg207fJ-DgJi6n5IHfQ5OMmq8Dkin82FUYbjbhPOMUqjiqZumuvQYcSnb05T9YAEi90-Z0uHisMUtu-muf5MYyA-LbCJNKe55VlWibnAie8zR0uEPHM8JUbLG8PVuEsb6XB8hf-DCqq3szybfr3xU7a-XBRfotygtkJ9jjREUoWffE-Xj_OWgMJaQ_BFijqo1fziqfmFffvNjHwHTahq5JdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=EgbBMDJZmpTamczNv0Qnx45Ib4CrmBKbz7VVOKTzmiY2kCGxwZNURkGjZeCDD2-p4jbI80kCjBirTiNy7kZmCrvtY3gvFQ2aj92wL9HCobL_v5DicQMH7PW1PGxZjYvg207fJ-DgJi6n5IHfQ5OMmq8Dkin82FUYbjbhPOMUqjiqZumuvQYcSnb05T9YAEi90-Z0uHisMUtu-muf5MYyA-LbCJNKe55VlWibnAie8zR0uEPHM8JUbLG8PVuEsb6XB8hf-DCqq3szybfr3xU7a-XBRfotygtkJ9jjREUoWffE-Xj_OWgMJaQ_BFijqo1fziqfmFffvNjHwHTahq5JdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=W3TKTec6Z9uQR8PjC_TURYUz6AKV36exsE39bEBM_zOksHP8bN2H0gGu6D_FYdnjSVor9dVKOs3T8LOsTY3umZhbDaBvv91WHelW9dxLFhJKXYjCcMfouoz8CHoUpvwIFXYHAepCQ9uEHDSeKv_MaeMSW85aje4nUA1Kk4XJ6a-MFoi9X_UlJeJC354ej8_9JtQoH4HfXCrSnDLYXdtQc383bOv-8J9UGeIJ-VWoXuKhH_WO0stsHe5kang7gvCdT6s1B2LYV7y42K9hnaVxXpm38fT26UEX6-BTxZ3OdJ9SoZmby08wU741xtgnWbrTDPfsOqcCkxWHMYcT1cs35g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=W3TKTec6Z9uQR8PjC_TURYUz6AKV36exsE39bEBM_zOksHP8bN2H0gGu6D_FYdnjSVor9dVKOs3T8LOsTY3umZhbDaBvv91WHelW9dxLFhJKXYjCcMfouoz8CHoUpvwIFXYHAepCQ9uEHDSeKv_MaeMSW85aje4nUA1Kk4XJ6a-MFoi9X_UlJeJC354ej8_9JtQoH4HfXCrSnDLYXdtQc383bOv-8J9UGeIJ-VWoXuKhH_WO0stsHe5kang7gvCdT6s1B2LYV7y42K9hnaVxXpm38fT26UEX6-BTxZ3OdJ9SoZmby08wU741xtgnWbrTDPfsOqcCkxWHMYcT1cs35g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=prboAo6frNs4HAUqAmbRqxZs8eO-mPlWA-kq5UQVuh-LPK-4Nbj3-pzd92pj-heNcVWguTHo0xzvyKSNILgCCBSWT2MrHzO6tjnKA6n5x2bDFs5cem11teKB5l-MAo-889uzlxhPCbT4eom9Ny3ftATaqmhyXwKJOPkZ6IucUldzmi5IId5kVmwyHoH_Ez4F-Fuum1aRg2pYTpWyX_oXrC0WR66YeFAr3ab0RxPEtzquzPviRHt8bwEsmQ9IMDsIS9ESTTAU9oFiYdbncrfl_7YKpnpVOjLFdELiHvnvDMWAqboAryxncSxv3MXJmdzjaeJoLJK230nZq9vZusjKNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=prboAo6frNs4HAUqAmbRqxZs8eO-mPlWA-kq5UQVuh-LPK-4Nbj3-pzd92pj-heNcVWguTHo0xzvyKSNILgCCBSWT2MrHzO6tjnKA6n5x2bDFs5cem11teKB5l-MAo-889uzlxhPCbT4eom9Ny3ftATaqmhyXwKJOPkZ6IucUldzmi5IId5kVmwyHoH_Ez4F-Fuum1aRg2pYTpWyX_oXrC0WR66YeFAr3ab0RxPEtzquzPviRHt8bwEsmQ9IMDsIS9ESTTAU9oFiYdbncrfl_7YKpnpVOjLFdELiHvnvDMWAqboAryxncSxv3MXJmdzjaeJoLJK230nZq9vZusjKNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=ejtn1X8tl40w645zbuePlDnyladmKbz5JdYk5QgfwGyvHnaG-x-tqrZ-P3yAMcLYm8AWfOl5L39Qy6PP-BM9vOohrpSBsXi8GIGAvxcFjMSQ-aiBeXqnT6wjh5JQeVeWkDDgwAQbqI62Nm8pgghwEBUidqwqLB1X5HHTb0k6Ks8bYvyY0ExI9ext96KxjjaPmv8PoHRWtjSqk1MIJtps4T28sPuQDSa-BIi5Yj-BRzpkpecoo-v69YRSe5LmLxJPVtGk7BZ_KKT13yU7ET19yJCZ1UNuEgA-eFEiPNWpBZeyxzJaL1-gqGsT7xR0i8Ucutm0K5EGAkTb_NYYzchNOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=ejtn1X8tl40w645zbuePlDnyladmKbz5JdYk5QgfwGyvHnaG-x-tqrZ-P3yAMcLYm8AWfOl5L39Qy6PP-BM9vOohrpSBsXi8GIGAvxcFjMSQ-aiBeXqnT6wjh5JQeVeWkDDgwAQbqI62Nm8pgghwEBUidqwqLB1X5HHTb0k6Ks8bYvyY0ExI9ext96KxjjaPmv8PoHRWtjSqk1MIJtps4T28sPuQDSa-BIi5Yj-BRzpkpecoo-v69YRSe5LmLxJPVtGk7BZ_KKT13yU7ET19yJCZ1UNuEgA-eFEiPNWpBZeyxzJaL1-gqGsT7xR0i8Ucutm0K5EGAkTb_NYYzchNOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO933rmGAqECZSxQ1C8r-0rnvOfylJ6ZSOwRDb74ht5ZqQhMvQwKEjwWRwgHcN_IR0xmAL-LjPlVa7E97a5m0cgqv5hWd8FC-mYf2_XGx1gaj-454gGzXF_XQ6nREfx4nOV9Cq50YvQqZzI3BVVJIkuiDGDQIRgwqkC7z-9dj-EHy6xL9fSt1y00kz18SSkWAcB3veKafJ9N8cHNzP0mGNFzA41tySCdaSsQPu1B9E7nLwgp0SACnJrXGI1mDHMlES6HQYMPpVc7BLX1UUFS-m_veIjOLjKyMDhiDH3m1EFZ_RpKZk1SZuIKsLBj7wTydNm6j3U-tKsvSQhrEB2EgGEc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO933rmGAqECZSxQ1C8r-0rnvOfylJ6ZSOwRDb74ht5ZqQhMvQwKEjwWRwgHcN_IR0xmAL-LjPlVa7E97a5m0cgqv5hWd8FC-mYf2_XGx1gaj-454gGzXF_XQ6nREfx4nOV9Cq50YvQqZzI3BVVJIkuiDGDQIRgwqkC7z-9dj-EHy6xL9fSt1y00kz18SSkWAcB3veKafJ9N8cHNzP0mGNFzA41tySCdaSsQPu1B9E7nLwgp0SACnJrXGI1mDHMlES6HQYMPpVc7BLX1UUFS-m_veIjOLjKyMDhiDH3m1EFZ_RpKZk1SZuIKsLBj7wTydNm6j3U-tKsvSQhrEB2EgGEc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZGVTR56brhjHeaQgJeiOpBW3_TO_wP51Vo-VwA1Am2eY8yC-8N-b1MLLBnlXPKBRX8JgWLkCqkufeuBN-9LEQaupD0bI0CwRQzihWD4psVhXs3yQV9zKIELANqCaA3jDviw6ouppEbc9Jt7aAM96n6FqJQkVACUGEOvNfCGCCKrlOfetUd5hu3-kphyHsQxYe6GmwaFXxpaVNJvINXV0cvWocQMH84-rN-O2M_Pv7I_mM2jq3mc6xyagy4asFj7MAp70sIm7gjcqY2SNaTPSNlaKvMwrCsVbGMd6LMVKuyg4rR2k2MPzQBU7bv31kvaIDC3qz7vw01bDxYRqf3G0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=IJiP3SEmgrjnFntMhQ8BaxH_5-fAy-hYCkfRt2PAkVacdkZsm9OJNafLtso0uSDBNPP21OaC_FhACA73BXcUQo-M83VaEFpI_vvohSnBmIrks93YOnWNLrBmfz7Hf3mqbn23OdsbcNIaQkWHWeMmnwOgBkqX9p_NQ7-zzN9o9jTCp0sDAYoa1DoZ4LlDwko6Xx-pe7vQLs3L6JiXtbJTzwIbsAPIZThLAR5UwH4fsWSyeUc2KAj-wM8HB0uYOiUcx1qpwkbKd3QUYbvSAcmv7GIMSV97PQBZrd8fHA6t1k6MdXBHIwE6rjoki-hxVcM2vJT58_XRug5-8tsJLpUyFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=IJiP3SEmgrjnFntMhQ8BaxH_5-fAy-hYCkfRt2PAkVacdkZsm9OJNafLtso0uSDBNPP21OaC_FhACA73BXcUQo-M83VaEFpI_vvohSnBmIrks93YOnWNLrBmfz7Hf3mqbn23OdsbcNIaQkWHWeMmnwOgBkqX9p_NQ7-zzN9o9jTCp0sDAYoa1DoZ4LlDwko6Xx-pe7vQLs3L6JiXtbJTzwIbsAPIZThLAR5UwH4fsWSyeUc2KAj-wM8HB0uYOiUcx1qpwkbKd3QUYbvSAcmv7GIMSV97PQBZrd8fHA6t1k6MdXBHIwE6rjoki-hxVcM2vJT58_XRug5-8tsJLpUyFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu4v_d4qV4mkgikiQH8jpzhLr8TfYe96L4Uui_euiUxUtzGLdC4-nBvTjfepQcTFn3_NgEiZuwjeRb_243lppkYjhndMgjBRDV57EUDRVBX-Y_4lf7eWS0KxMs06I2Dvdk0g6cWeJNLRY-EN-NGU-jQJcBUEtpsxUL4Xq5dOmfvPCQdJhAxSS5s44AwaFFn7JjmYxbS3d4rUTmnXrElOv0OwWp6Sw3CFeDJ4vMwIDfpQkZiHSTr18oNYQyCiO2lqqwJ4uT_4a7Ab8dXO5Bmru9nAS8Vho3Qi6N42Y9_MIWfImzSQOm3BLZNd88HTMxS_tpC0WiJf5G2JVq2svEo4Aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5d4vvGLRxYoN7IS__2vqOCHtjr96wCmkuMLpLPGcOY-V3NDxlcJGE1dGBWeEwYFYWI5l40quFvCzpVGtFZoOF9mHa9ieNqgCM47bwHEBh0VNHxDim1GsvISlLhHudHEWu3FfF2gjRQIiW6yPywZn-5Dao78PUesC0FUF8S4vQ3P6LDUvPn4uxL1fY28edR1UeD67l3lSh9gAbbzKq4JVUmGt0YHzXVKScJggGENeGER51Q140nJPDM71krWAtL4tYeujQKXZDm88MXuUyF8uryxFnosTX9Oj-YPTCS7qB25aCtFTrxK4Phrvov4pBUjY431RvnFGn-5ctg1iQxvhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB3UT7n57NZ0gEop3-NB8nfk2_xqbn1xDPgOBWR6pnPw1JYN08sDHoMih5YkfxyLixE_uE-54xd0myVnS7VhZiN3nSX8CMLRt0xqj0eXE5A20KW3852IAHD-Ei6hTcd3JFgdpObGx4ZynImpPq4kDGu6OLlrMvSQa2mbwr3rNSBRnUlU_hXZ1IL6jIdLneqVYFds5Vk7HkBAvKcspsOL0hD-nYCmUWCLYByftmaIXuNM85daz00lrjuEx3XwnjZqG2QPr0UR1aa_wt8UYfjtyXkF2F7edfZY-8OYU5gt60Oau79qWMgTO1YMHI-JfQZLG-4qn6Y_WRpFlm9YFuAi2A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=CPCFQTvB7DaMGlTtel6V4ftzGUI1QAuMOZqZCXZyLAr_UJiNz1nN_U5zzWpSM-K0KrkY5dpG3TjLv_AAynDVcdjvzOckqfGLZaxkpj48smu74EW6RfgHlGvJFMcZqbrLOyQYkgXIK2iQCgBQGZEmtyCXDRzec6BPDO2_GgeftndE1_nIrN0yPavj-bqZ9HZ96Sw0tO2jDXmNX7__r6YP6cIHc9z633F-WZESsIBFBoXsNJN6d38uSsuMQhJ9H4Jy3EdGK0IxgmMt8YX1InlTF5-hERkBVc4brrK19V206yH-BGt_zs28n2EbW42rtuYBPORHuJoL_czbeWx2dydGfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=CPCFQTvB7DaMGlTtel6V4ftzGUI1QAuMOZqZCXZyLAr_UJiNz1nN_U5zzWpSM-K0KrkY5dpG3TjLv_AAynDVcdjvzOckqfGLZaxkpj48smu74EW6RfgHlGvJFMcZqbrLOyQYkgXIK2iQCgBQGZEmtyCXDRzec6BPDO2_GgeftndE1_nIrN0yPavj-bqZ9HZ96Sw0tO2jDXmNX7__r6YP6cIHc9z633F-WZESsIBFBoXsNJN6d38uSsuMQhJ9H4Jy3EdGK0IxgmMt8YX1InlTF5-hERkBVc4brrK19V206yH-BGt_zs28n2EbW42rtuYBPORHuJoL_czbeWx2dydGfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdhSfrZfPLUsVXtb_yB7_OOi0nvhnL9UN9QKNXKjfGCLGKbGcyKVFiATx1Ny-VqViFM9U0ce4MVOgLPspvzciMaBvcmS3InGfy5-lGh7zs4hSXKX25ePJ9g5t5kbrjx_jh28Z8X24Hl0kvoujL9z6kJ3iIwgC8IHiS8tMN_cdL3Y5M8fvR2q7qLAgaCzyljxyu6E0DNreXuCrbgatvOKLzRUsnoYUU6qbImm7gUtG1rHKfNmtRi-S29KXWpMwAQZHREFbu5mM1JPNE8A3bXKJ3RIl58O8Z2Xtw9xeS7bjIYNnC698W-1IlT3uRSDqi1b1T-JObG_e_r0HuSQBWyiYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ4SoMsevYTM0abDK_zdsYiplz-URvh7p1xD_8wRHeFJihgNAFAVV6M4B2umeXzg-AZMZjvu7SY5i2DHfmaZQzBplvcMeEOEW60yjbKYnryHnmc5_1Y3FCvJF9SM2SUGyWIIxrzQ11ZiFxDhabee2vL3ybwGs7iZ7i-xsUs-NwQLYxbGEpYdsUp5efCw28Ozl3sJ9RFllsaTgGsRwLxCM30HAmSi9P8_OwewyrJwlIiZPxnRYbZqXrtpkeOcJpfZnVDvsGHlKEQMSLVUH_JylZup4f5BuvGoGvQ48plB9MKt2EnYs2hqVz5y4hB_WE6snpdO6nyeNn98Zml9wQeUmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-hiZrwk1C_Oq3v1UmXvVzRsFbTZwUxKeFzIXCG4yG2dAxmDEO-FwC3aaLrU7ZsrZZ0sg-Nm31L6jOOQfOVBMYiomMIeyBvMaUBuAayvL_aoEO4IR7fiKERmMuYV73FLBB3YgqxO78kCVLMFAxyQUy0YAaXNsglOZmcO4yG_RbGq6bGJ6su8IXlIdi1rlpcIYIkkjrPp_uJPeRrYVR9K-omrMSh25hop7MaeVYetg_7arLhBmaL_jHFbdS-eUs79spwu9ewh4Hm6Tn8NGfaHofNQgQogbCs7Nh3h7B3HKXWKpiHfapV787u1T6wyfk4Lk1r5vqioocmzrgv3gDDoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrtU6Ek8hB-e17OVZSwAlv2bL5lv66XYlA9x7F7E2gF4Rj6jqrXKS_cSbw6_Oxl5GGddpRWP5vEHtmLR73utwqT-bSHqS3PdVulb-IlAMWUnAfHeGy0TliDFrNwe8OkIoNGV9BCJSt4xH_LHaD7KY6QNn-eFtj7yJt_AHv0Wp54CzVX5TwFlSAISDeXzSQf97WNB78kOZDFi-zPlKvvwHCZFqLuuh7SGK6960JIY8iwaOFgiYj2Wc6aDX-XizAd-FpFTZ16TYyG3xjonHrEEwPns4S2PEA8a4ZS5QIK_J0zxWBOszDnHUvxmuDsimVNTo_FEjmJTeKd7lhs-CUhJsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=IbVAQDfjpXVmz7Ls8qDTZch-By7eQ6Lbux59mkAfFKVxR1BY2QvdrGNTET_VhiCcg_V6K7aO7E1STl8qFXJeY1-074_NvDz6uQiivinzD9lY1DbZPkKrq486LQzALmhWf0LUW8azv1Fr_cAQbWnhRXSDSAyL2GA8mwVeF497QctJuMJNARMUq7I7AqK5-fCmT921tsoGrCrhKMm0OXtaIVD5bS-NdlKHYSscnEaO3UTMX9gBiD2DJMni0-ybGb9Upj6lSNCjMZbcS_YrSBAOK-06nXujARNs1BLS8mDK5cd0hsyOHE1-ulIfsgjxrFtQqxngltvPZkXJn2nVpDbIaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=IbVAQDfjpXVmz7Ls8qDTZch-By7eQ6Lbux59mkAfFKVxR1BY2QvdrGNTET_VhiCcg_V6K7aO7E1STl8qFXJeY1-074_NvDz6uQiivinzD9lY1DbZPkKrq486LQzALmhWf0LUW8azv1Fr_cAQbWnhRXSDSAyL2GA8mwVeF497QctJuMJNARMUq7I7AqK5-fCmT921tsoGrCrhKMm0OXtaIVD5bS-NdlKHYSscnEaO3UTMX9gBiD2DJMni0-ybGb9Upj6lSNCjMZbcS_YrSBAOK-06nXujARNs1BLS8mDK5cd0hsyOHE1-ulIfsgjxrFtQqxngltvPZkXJn2nVpDbIaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUR8CRbU52EbWUjyAyOUBuGIrWHVvvgbcAOxWUsH_wtewCzCp_LE-a5_bmP3CDql6tHibaKKp8bNd_4SkmQg7-Lyh4nvX7qccrVkOxLopU0xQWjaO4gay1fg44GMJHtLqygFAi5bZ0G-t_2dykXbsKeshOxVd8XC3ebrY_WTeFGHu4V3nr28ks-WtLzr3W6VqAipkiX0Yxqo3dIH2Xz-Y3TlvbQypes4CHpR4ubsETOHPz2ZJNnnjIkaNwFNIY1IoYXsSaJEAeURW6cOpBdMQO_TceNtUEtW417DmjPr7-GgI69HfJMfwiQHkO_5wXCx-5khvE-oaz8etDneVjFdUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhMNzycdkAFyrTv4aADU_Xrgu7RZRh9smT_fsRrI4VsokezkveluDGuMLWjKY8YEv4xAYHc6e30gjcF15FnYMJcCRkGnO3F_oMgAEmR7_3uBBF_RyySTBe6x0b0fzQR-fz8Y-ZZIu8R_x7lmG7zfMibuB7o6DPa0pdjU7hoOUAD31dH5RexsNRgaDq4WGB9XAhDcPyj1p7yAeEYXiS-Q6n-tr8B_oIH18L7EgQvENU88uEuW6GOwlTnzXkMP1RMh7qrNIIXkRQUN4qdUOUNPHJDfoUM3JV5wQ3SRzEI85T3FSIa-M4ZES0jYed2p38SWJlR309JK5nhWNdy67uzjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=dUIvEsojHkeeNVT-S9N0OpGkXIkDtBbcUrTnY2WjXW6GZOUOoWudoykKIQPS3vOAYXhWLigAYv24ullktIj9kv9QTg0Mw_h77-0MSfr_L6jm5fY08LE-sl90mHbcM5LX3_oEikG7t7WR6nTrqMp-PtEdVTw8nkv7md4rnM4wKP9fkLI-sdnbrWeajNsK4ABsgaso0gGf4nkggmfzG75QfSd-a2uls8mvDXuXipqfXukuboJyQ5mtBUo9ydRhUoKSXRALo2xwhHVXX2mDzfT4jBrwJyDYgH4ruzHCVRg0cUfNBTcWnG7EPXHfuCqQuRA17pHABwSzfhkB4lWGVTkP15rZkSfROCskQTZCsUUVJvdbfqqpYvrpPYrgKLJPZyOmQdW1Yp-4X9c_aQiXJY3psiW6QFVpd0z068s6NSOV76aeJWqVXMisDtErve1bUULJfIz1aGIbDV-r6VPHAwXXizi2NLq1eZE15XLCluk1PpEMoit2A4iXkcCWjY145R0m-OtNhHDH0v1rDdC-Nq8fjZcfVAWsm34YC5OIiJ_mgcsLDJxhFghxy8UmvnPmWHjYf_EFZ2G9N0-FwT6x1riW_QycC4nJECXyhG6QkamZItPk5buRWG8Gb7Ct_PYkEnSl9WkJSSLDiNbpRuHsEcy2H4AGZkuixMmwjjoejz9FfRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=dUIvEsojHkeeNVT-S9N0OpGkXIkDtBbcUrTnY2WjXW6GZOUOoWudoykKIQPS3vOAYXhWLigAYv24ullktIj9kv9QTg0Mw_h77-0MSfr_L6jm5fY08LE-sl90mHbcM5LX3_oEikG7t7WR6nTrqMp-PtEdVTw8nkv7md4rnM4wKP9fkLI-sdnbrWeajNsK4ABsgaso0gGf4nkggmfzG75QfSd-a2uls8mvDXuXipqfXukuboJyQ5mtBUo9ydRhUoKSXRALo2xwhHVXX2mDzfT4jBrwJyDYgH4ruzHCVRg0cUfNBTcWnG7EPXHfuCqQuRA17pHABwSzfhkB4lWGVTkP15rZkSfROCskQTZCsUUVJvdbfqqpYvrpPYrgKLJPZyOmQdW1Yp-4X9c_aQiXJY3psiW6QFVpd0z068s6NSOV76aeJWqVXMisDtErve1bUULJfIz1aGIbDV-r6VPHAwXXizi2NLq1eZE15XLCluk1PpEMoit2A4iXkcCWjY145R0m-OtNhHDH0v1rDdC-Nq8fjZcfVAWsm34YC5OIiJ_mgcsLDJxhFghxy8UmvnPmWHjYf_EFZ2G9N0-FwT6x1riW_QycC4nJECXyhG6QkamZItPk5buRWG8Gb7Ct_PYkEnSl9WkJSSLDiNbpRuHsEcy2H4AGZkuixMmwjjoejz9FfRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=G9SmyiJjcgZw2QR0ykzY0Vn-QwNANLaZ6QjFNOUuf6JSgZHottVD_CkWAw5iUI-s416muVA-j7PYc88x9itPCcXRlq2L_f2g7jiowAP0Ar5DhAFYdwmrAOoS4N-Cm4W65Qc1fMVNP6YH7APw2rMDkD66BK3k-fr8wiWlUJ7VAOr9jWRbaWl6vEQu2rcKYZBrOWRYTgSaG-O556NeZTleZYGfT3ZOmx_a8kqpJBzXTfbxvtQgilp1_1gaDsstxujh8grVKn2vq8ohleD1L3Va7Vn2YjGesghJ9JyqiPZ3AmzGVAH6L4zt6OJ8QwFT3SlS8018K8QKpsxeUc6uQdL3jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=G9SmyiJjcgZw2QR0ykzY0Vn-QwNANLaZ6QjFNOUuf6JSgZHottVD_CkWAw5iUI-s416muVA-j7PYc88x9itPCcXRlq2L_f2g7jiowAP0Ar5DhAFYdwmrAOoS4N-Cm4W65Qc1fMVNP6YH7APw2rMDkD66BK3k-fr8wiWlUJ7VAOr9jWRbaWl6vEQu2rcKYZBrOWRYTgSaG-O556NeZTleZYGfT3ZOmx_a8kqpJBzXTfbxvtQgilp1_1gaDsstxujh8grVKn2vq8ohleD1L3Va7Vn2YjGesghJ9JyqiPZ3AmzGVAH6L4zt6OJ8QwFT3SlS8018K8QKpsxeUc6uQdL3jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jf2BukutKcQWyNKksq2heym6hp8kwQyZtNntBf9zt2-vWAQYXHe5kL168FRWoLaTXo_996NP9wLg-I-fPDFijNM9VMBsqafmc6BabAApeL5tzdLKsiLdwmTEC-ZN5PubbhlgeCIfalnLXzafwJyK3WT1_ab8WdqS6izNlyQyd9av4gKzPKbZoin9wDbnoYE7fdh2yaC4p72e1KJiElGZBHCuPO7vNDCBEhdLz5QW98_UINPD3FpM3vuTDPYfPPdxobSmcK0qIRGbzXLrLGo2QyJrhtlY1EpFFC5sVicd1lJao0E3aFlSkNWUJzr116HYZGHupLAD_qhMIbN9ct_Ubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=ZZ0tcVAwg-hbjA5k7LzwPmsPSou4NktNoVyU9BpaWiLEhQvMei9E3pVisxa7a1hzpP1jbil6sfglFbvxF-aMhX4dlH1pBjyirzP7BturA1igY0_S7CEqLm-B4CW22ATSPrkJ7y-a-IHBQ4wwEx79XnaPjJSU1EWs17frrN73PeSRRx7_-ZAAGCB0nGcq6TT5uJb5E_FSQZZx-CzEwMBFeLVYCl8WJwSnM68RhgLVcy7ucmK65DD0mcWb0OopvXd2Ko_n8ZB0-fgo1lbbegVdaO6NoGcrGfbivEY0MvgP02GWgydzb8x-CC0f5z2x3Y_m8dyuZsrdo2rt5UMyj0Q35Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=ZZ0tcVAwg-hbjA5k7LzwPmsPSou4NktNoVyU9BpaWiLEhQvMei9E3pVisxa7a1hzpP1jbil6sfglFbvxF-aMhX4dlH1pBjyirzP7BturA1igY0_S7CEqLm-B4CW22ATSPrkJ7y-a-IHBQ4wwEx79XnaPjJSU1EWs17frrN73PeSRRx7_-ZAAGCB0nGcq6TT5uJb5E_FSQZZx-CzEwMBFeLVYCl8WJwSnM68RhgLVcy7ucmK65DD0mcWb0OopvXd2Ko_n8ZB0-fgo1lbbegVdaO6NoGcrGfbivEY0MvgP02GWgydzb8x-CC0f5z2x3Y_m8dyuZsrdo2rt5UMyj0Q35Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ-hJjOfBYEMCkIYLvKEa2UvN79GgXAHQpIJ8W7M_7P-kHiXEp8JgwNQlslWXRhHgolD-osd0ItLm12UBm8yjv16kWd_uGiAt4oUCyXK591tobQ0XNhPO9E0cqZtsUfTLBhigOn9u6_pvkPng40T3VvE3VUBEP86V1sM1B7xyemavE3qkj30bvil8IYpfkzVbADPiCxW3mWfN95RjhOFJIyeTlgtmifZbwbHtEFsUCTxfT7wZm_XXqpniy8ylXQS7i-t0ECBYie_6_ri5aQz9s-3HTmOK1xGt4p1X1rKpYy-wo4BCpNnaQSsR60whjtEON8kPZ5ios3I9WaKtbbaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=NTdZi7y0PUHPZGqv_5DhRVN130YVHnGARPgllRXpoPOIGHRyN5vZKDyMXhY45X5QLVcfdJp7uVaan-W73McYkUfxKbgLAYLflcvuigBP88HNnshbwHkJd324BXMkcy-KtDTvE8tMQLtV8gGeeqUIWMhAYZQpJgoiX7i_Jfe8gUGEb5sDSKf0wXuCQ-wK9NUG7gmwGksK-CKJaaU0A_noDZ26V0Gx0HjBTvZcU-jiCdPkWdHi75IZjX5U1j-2rRLydR4tUPs2XjrMyImtWTBNyczZm07ZFAfRPtqb_wmCYYxdqnp5Dr-eDVJ2lNupmDJtHT4wyMozx5E4Y7BW3Hytug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=NTdZi7y0PUHPZGqv_5DhRVN130YVHnGARPgllRXpoPOIGHRyN5vZKDyMXhY45X5QLVcfdJp7uVaan-W73McYkUfxKbgLAYLflcvuigBP88HNnshbwHkJd324BXMkcy-KtDTvE8tMQLtV8gGeeqUIWMhAYZQpJgoiX7i_Jfe8gUGEb5sDSKf0wXuCQ-wK9NUG7gmwGksK-CKJaaU0A_noDZ26V0Gx0HjBTvZcU-jiCdPkWdHi75IZjX5U1j-2rRLydR4tUPs2XjrMyImtWTBNyczZm07ZFAfRPtqb_wmCYYxdqnp5Dr-eDVJ2lNupmDJtHT4wyMozx5E4Y7BW3Hytug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=D47iwngbAL26qGIv78sdwVjA9Q3MKOSz_TLMr1LcMyoXBntTF6f4VO3UCCrOiT96cWXGw6GrqZVC8fmyE2j2r1DRHteiKHv4B4EwSTTEE0RLG9PDmqVIjDGQQi8-oMYbh32En_hqxrvp0iPUQZwxOh80ctZws9jk6PZbt9kupeBZVEdFCOIz0YDgeuD_4LWd4n3SGLS1FxHJ3FUAq2rXkgeqCAFSv9L3ClmRZFUHNs8NDtfij-WopSNKtLCHteIXDrZFyoss9FWYLNSJwSGF-F1OjZOT1lLjx4Whj-nHCVZKD0ZFfG5z-kpiHLcFS_KM6xlu2kb3PX2hBo3IaRG9gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=D47iwngbAL26qGIv78sdwVjA9Q3MKOSz_TLMr1LcMyoXBntTF6f4VO3UCCrOiT96cWXGw6GrqZVC8fmyE2j2r1DRHteiKHv4B4EwSTTEE0RLG9PDmqVIjDGQQi8-oMYbh32En_hqxrvp0iPUQZwxOh80ctZws9jk6PZbt9kupeBZVEdFCOIz0YDgeuD_4LWd4n3SGLS1FxHJ3FUAq2rXkgeqCAFSv9L3ClmRZFUHNs8NDtfij-WopSNKtLCHteIXDrZFyoss9FWYLNSJwSGF-F1OjZOT1lLjx4Whj-nHCVZKD0ZFfG5z-kpiHLcFS_KM6xlu2kb3PX2hBo3IaRG9gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxLns_VSiEnnUdKvVVA2fQJL4GWRlB9M77DpebZ7-PBhb2xiYfwjxXek6kHlurAIExEv9jrsSTT5vXH5rIV13Dnc-zseuNm3sSokxrRDP3GrBj5NIak_4Rl7JD0R54uECp1am9hL50n1eB1ZCixt-c4Xhs-bnw0l5mO5KOZrETyJGxU1uy_IPg6T5FPvYxT7BqfC684P2TDLy0pFeM2hi7zNQdC0WPW4tsrPZdUjntyEzxBz5YZ1HBSdK4dLILDH6Zta0dSQ2G12S_HikbGBsHPBB6KuM8UoO4nmfb1agjpApuDvoHadsEdOU96UxDR3ArGho_F_LO5qFsSj7Sr7vA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=GXrN6i-8ykCDwoHVvOULukxjljdQVx0kEmxxQ0IZp14vfR-r8fs9VygHGKf-aOYCc_JgrD8AUkL_9cpCMixOU2bLgrzGIJNkB9gBxKukqQAYuO8CLWi346Ku1o7_ySgtkH3naWIAIst45c9kl9o3_A5KjceEIQLSNbCThah3XU0JurshGAoGIX9LVGSq_J9LGqNUr3E2gfT0fYiTTakJdAQC_wdFKiadKDbDWHCT8Hi0sMzyollK35meA7_MNvnzFyvQEn-z3BngtYveF3eImP5XD3RsNPkl7hYXmaCJRRoXxkU2d_cUBcnXCZ4pUt2b4ulAXj8sAtAxTw__3MCJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=GXrN6i-8ykCDwoHVvOULukxjljdQVx0kEmxxQ0IZp14vfR-r8fs9VygHGKf-aOYCc_JgrD8AUkL_9cpCMixOU2bLgrzGIJNkB9gBxKukqQAYuO8CLWi346Ku1o7_ySgtkH3naWIAIst45c9kl9o3_A5KjceEIQLSNbCThah3XU0JurshGAoGIX9LVGSq_J9LGqNUr3E2gfT0fYiTTakJdAQC_wdFKiadKDbDWHCT8Hi0sMzyollK35meA7_MNvnzFyvQEn-z3BngtYveF3eImP5XD3RsNPkl7hYXmaCJRRoXxkU2d_cUBcnXCZ4pUt2b4ulAXj8sAtAxTw__3MCJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naLNVrrSf2GwXAUpK231uYPDuqCVHi2xYWZl82FLypEzD934a65MCsHxjcCEUSMgAS7n3VJHFbGruA3wCTnuGugbUYiOSnWPkMt-vrOyq9R69L9aEB0IxAfn1-6L8T2n61V0IMIZmVtrKlupBZdCRCRNAACogkYcuGzc99VlUwF9IGVoAMPppUHIuLiBkBrcvpJHTfPACo-Bu3eKoooj3qAy4FDXtlWmKjty3t7bVsvNrVuwQP2vxhEV5mxyCwljox8lflBe61582k6BGj4isLYWgedXhqPLeuf7JTQukXrvSIn-dU3LSdRTM1fMWnqNeiPBo5_mxJibnZOQL-Q3WQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnQJ-usHe9WdHTMrOzNfIM0aSCgXZlfwrjOW-HTXCXRfr07LC0Veri8eGlQp6S-Z55jNsspUYtjhn-_KCH13SF1pzpduNU3QS5jkRm1AknfzuxsFdCaRD9yCwbHPjckuzTgy2AYi48flVSdUaQdAzVj0dyXyBYp4DcSaaLqZA9_FEoGgsz7CjehwqOlFscTeQS_aun9TtekvbyLBpjjmPUrWYz_oZ_6W0QbQ9qe5Sg_OzwLsJkkDUuCh1OoCN7LK1iWuKICnMFPwaXWWvwayP6BK3E5_KhN50uPD1qH71qqm54HpBCh_QkZCKCcwrOTRzi8X_WLhQyqv21kAgYXIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGrPXKyCUyz7-Jtt_h_PPxv1JauuVM-JMEHvOm0IUvK71kiIsI55q9957QYRiMGnqLmfpKceKlrqDPX7q7BIW8VcRehdWiW6e940MwPMTQzuqL0fOvwdyF8BrAERvBoF3CSvOA1ObOZPsocIPbvBw0Ccprh-TcBrc2UtGxuwYvpuFZQYqiS4u0R8hG4o7IlVnjFEW3RFd_LLGUaEQ4S9DjbOAK7vY3Xo8l6exClLgyVH8SnEj3wppPbfVAaCOjJVdHfVS-eExW7ba9zffuLniHjXIX13WTaS9OecjM8J40h5d8Oz_cwi3cj6Q-YXfc-bRRiV_XVE1qPRAKQQcyJ6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y104SE8k4Su2d0bTxxGZf1ssARS98PJHm9jBN7aJqGICfl6dNh-H1Y65b8-cLnVq-hNSxG0dXz8v1htovAk_07qjsmhcOnXpn5QrsTt2dG_E68XbnnJJOFqAgG5x4V6CsLsYF2ej12sxhKey2WyWj3yYuNcG8_PL6YZ0m4ePG8axToPf8-cQT-HkzN6By9Mz66H061T0tbASQGEPPyWv8BvBPPTbn5HpG3CtQ3GgRAIYzckpJj1HYXBp9MGKTWftg9z289CxulFa6My8kCqL2O9ozNDFsjljTJyOqrGMcI765gzTDNLlKEKy-3iXfrkloVIqPz0SKv6Cf5ZVtB5mEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
