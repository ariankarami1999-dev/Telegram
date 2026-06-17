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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 17:36:46</div>
<hr>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=RI2LVf0juEZKlxEe8fOyUxqso8ZpH6MvFn3CXezzSwiiGFIWn8gngzWm09NQWRKhmClzqfA00n2pYx3rW3cHuioc_G270kGoV3ETw-6cPFB_zKuBsroywsSJcMhcyscntgslErux9BO2vHMn9wZFDUHFp370RRjkpc7XLJatTg5mELkz2cmNUZtbT2EdMvToJe1NDaklzEl4LtanMlFIrmEwjid7dJTHYQjd3IvtQWnFrrGwV7fckGuHEVYcQol-fdNfIbWFxlX5ofYYDZeHe0O9cpbLACvZHx-TOony6UPyIGnMbG09dXUbKZYcuduAaMx8QA0U9d0bAp26qCLafw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=RI2LVf0juEZKlxEe8fOyUxqso8ZpH6MvFn3CXezzSwiiGFIWn8gngzWm09NQWRKhmClzqfA00n2pYx3rW3cHuioc_G270kGoV3ETw-6cPFB_zKuBsroywsSJcMhcyscntgslErux9BO2vHMn9wZFDUHFp370RRjkpc7XLJatTg5mELkz2cmNUZtbT2EdMvToJe1NDaklzEl4LtanMlFIrmEwjid7dJTHYQjd3IvtQWnFrrGwV7fckGuHEVYcQol-fdNfIbWFxlX5ofYYDZeHe0O9cpbLACvZHx-TOony6UPyIGnMbG09dXUbKZYcuduAaMx8QA0U9d0bAp26qCLafw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re8Ivd1acJr2AYq_VM7tBuV0osFyLtc6mK3P245ttOu6Iq2qX76CrvfRCjBeqGzRuFp0QFj3RH8k0gFxMAZTGrJ1I19OFWVpaWxRrrlRAuw0p8l78rRk3nhQazHBXnNEHr2a9DqpwFos-ADwLJnvCNYCqQTT-ey2M7sDqj-KJdKgUzN-WMl8oSXrc8gHUjnty3LQsfP68x-f1-c6d2tbS4fJ-DG6T-UMDxZxtslrKxFaTWHmMrYPxDJZFJpRvEBO-8Drgiqbl0iK06VDjyPApXY3CgfxcA7oJflirROvqrGRY1LuwZ0feiJEkLq8FoKFH3kb3DfTcTbbHHoANP03TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgmlffjzE_qrw0K4fcb3LQ2iexas8EVdu0cykiuoK4Fy6L_MD8sZL-s_CTNJup1hheqtReGr-ZtUQdaH6BSDhOAqzSyHbLrkU-ifQRnNxZcf2M1FULmSmUS3Ai9YT9hEJObZx4gSJP10kRBTTRdSdYNz-cOHNOMaWYgFYuIJ-ma6lrEvxJsDEppERlOQSHXfux3C6cwwdgc1iMlHS_AxH0JhGsvoGGGPBDiOtsZ57LFJ4jHZG3JsrEwAF7S3_9fQfJFLZk2smlIaPORCNezHOhFJrg9Vc8vO14AyAlAnDHV2xLDVwmLEikTH2NsEpRbJU64XtwDF1Mt7fV8lFhsbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDMrI8sjMdcQthejeq3gW8GtkYqzNcYT-bFT8ZC2DlPDU4fC3yWfDazNq_DUd3YcFLcoiZFB56PexJFyl6MtXaAoIdZ7f-VtFtAMPZBqQu-RRBQY4jBw5MYX9JWYyge9xiS0ah0IvUgULsL_YAQmDHcixHj8gzfG6HmFoc6kWHkEb8oND8MZq6KXqG_ZP3FSmG1ymI5ayI8mEfiYD7FeVEFQzbwH8GvKaf9HS_XMUxGzWCK0nrsA4JKMzzJaKF7JcxHJLa_ek9m1QwQxHXqj5Cvu2CXuN4OOcYlaRtLf85d03HpZRi8I3j30cePJnMZKbYcMXUCn4lxXkZrk6RS3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKeAfFFZ7yFs2dPG71D-vguS7m_tGyjrM_7aOtKZesH3NAfyjMP_99LnYrvwFw12YerUneqhW1MnozlIg7sCBNZifPjorSA5nOuLG_qjkG5qed-ezX3pwZql1ZPKQORgh1OvDRA0tm6sWs4T3WjNKeWFH1zfuTgsmEOL00WffrKXZbkHcv7NZLA1mLVyLWZDQiNMPJxZGzE7LWYf7W92ciMlPb1sCxi9wKEw5HoWy5FIvB45ry39TeGeEx9AIuFbCPAWILoeDNe8QGYvtSggjoAxZtUzZfXQ7XiX6xHPSYGAUmucAu80xCT17Obm_JM5rcaLNF2hdZKaKf9eer7zCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=beGd6hj4dpjXBpdn955zRb5hQ7qfIl7f-EHjDJx6hy60xaOkKVCfQwA9NNsmBW3tQA3TCtxi_5Esbndy-JRdLKLud8yPGXyKJ0-8Fr1ztUshMmwx6jtrsAtknKwcxM7vmF2xczF6vnStRqXXsmVqeUQ6RFx0cLjZf-yHM5iEWaR5HzpYq28KkDZvaoRKHNKlP2Wit32-Ab0M8Z_fV3X1wxuz-Vaz2fYp90WxWWJyFfmoMIQOCdNKTjPDi7IRjVK7hYAUrqhcIlgSQcNZyRynC6xEScO7_ANjJK3mYxrsd9MWvQKgEqTPFA_RICFtNmK9VQVoQyVuL0SqLonkwOd5qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=beGd6hj4dpjXBpdn955zRb5hQ7qfIl7f-EHjDJx6hy60xaOkKVCfQwA9NNsmBW3tQA3TCtxi_5Esbndy-JRdLKLud8yPGXyKJ0-8Fr1ztUshMmwx6jtrsAtknKwcxM7vmF2xczF6vnStRqXXsmVqeUQ6RFx0cLjZf-yHM5iEWaR5HzpYq28KkDZvaoRKHNKlP2Wit32-Ab0M8Z_fV3X1wxuz-Vaz2fYp90WxWWJyFfmoMIQOCdNKTjPDi7IRjVK7hYAUrqhcIlgSQcNZyRynC6xEScO7_ANjJK3mYxrsd9MWvQKgEqTPFA_RICFtNmK9VQVoQyVuL0SqLonkwOd5qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMnAwp12NlLaDoxqO8kED0rGAKvT3WtaoQKSJR6_RmhFREk4uQ6s7PE2f93UJYqczht6t3pWXdFom9kuKirSPPM2WRtdhfsUHsDVK6b7xwD_gDDTkXKjlmTJgo7mQO6DkLt7b4S0etWolWbvKFylF9UNyfIXPm2RYZPLPIAZB1gG6LLlnYPTPVR_ArBRSWotu1PDSdN0jri6Ld5zG4G4WvsJmQzjpQO-SENr_qsOHFzVPhRoL-86RHLZQsiJ9mRUtgQ-6qy764CMwM1qwwYzxiu6t4UFkeLwunfxQz8DCgfVOgoDsmHE4hsbcv0QVbhJo6X7j4u_OCZxg7hWXk8rtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbwKMmlnjznzJhvSbLyX22gPN8odk7N2FNb0tye2wyZSqMvKL0-QndjFI_6t0B2nhdV7CfyJ-WepjxSNvQjPBveoNxCC5NABxPlgt7PrXtTBLdyUfwUBQ30ou9oQy2TA2cg9IbkSQru_5EKqMy60qHwvMyjEJl5BVa8ywaPNswnVaU9FdQoMUBMUY9engmHcc5QIottiqlyZShFsS-sVJ7BcDGXrhKOlvBrrhHLI-lLkZrsHO3BEhiavfJ0H1YZ0p5JSgUvEulSaCoYGV2k-cdExFSQb7mDHEFcvAHwrA2F_O2makb6davd6Lw29tDxsj-GIq6Ps6LjVBlqKuHjHVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZhdSNZMTNhPrdn_c0Q37go-aYeV9k_WeiNGEivhwCCls7qEZG0JxEZx66UAodM6VNLuHeYCi-qneQyZ77HQ5qWpGXYf4D-dQHy_zQPS6RCoAJ7KG-dwnYCodpm9-iG9j9WNZhleZyohhqxOaaxmcgl2YJBbFs14-heUH8bt_O43xlr5KHnYrRLnz2ppTJ3ZYE3dN3bx1WwP--NaokdISqQcRUeaaqdmdsax7fLqUM7Jg5aGTY_d8AR0DR9OZYn10su335YJIAWsjW_rkP7sSIpQK4PprL_qys7mbpRgold2J0T4PMvR6qCJ-Ovu9gZg0ozmCSJqFpcRr5aX5U63z_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVG_ztyV0P_3m4VyfBtKxy6gMtx1td5H3osaROc8tPYdmMvyKjCp3O88Mis-yHX5TvvjjlCduuTSHBkXqaH3XCPDtX6g3UTk6Sg9s1IOFZ3uYdf9IkUCNL9Z34uOpoySZv6Ys-JoCocm-i59HO8B8lJ194fRnFPz_bG15fo5JmWeqtGX7KxKJjms26E1o6FxL3ebc_f0E5nAGfy2UxBjmm2pEPFFlXady8a_fUbTv459cwL17ukE4bmfbx_-RQRtmrUSsWdfqGSSJugIBj_rzlbsLiID1h2h9IBZ-cSt_7RrXKiYTwJJbKtnXx_BD1oJ-QmdsArMauCOUECjU-0Teg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=I6TfowwLjfNPlqAbZIoorsT1h24MAT5dZIqq9EghdjTkTpL0C6t3SaYvoVNMStabHox940Pqth8ZenzweFo8bfh5WWNsnryNHVrqZyV8QD8D8Mmdp_zCQRkmGccYIPMuvMRN5nBOvfPZiUIbAH_cu8A1KAVnCuiFClgEYqonLUYDWsiwxnLECvdaLhsa8cOK5T5dlr_iIxYGC1rpnvX6Wy9aB584afcHYru7FRWdQVrNVgrGcp_7Wq2XCQteN7jfgJooxmGehDZc-vIXwKdlpTSAtJ8L_M6aUgb-5xPGobgCg66ww4ZD8XCME2kpIotQc72X3stQ2JqdhO8IXL1-q6Pb0v-2yOvpis-qROJdqmTStoU_2fy6WVS441Mdymatv_PZm8jC0-NyHHTzoh24kjEtrGR6GfnhJzjIcWjuikdksQtD6g5OLXspalnhMmqPgb48LKtkwim3G9mM6C7RKmqjBO9T9A4mqe1dqn1PC7LzAtBbk3yA7lW6hFlvdpFxniUzvWQhHoxOp6YB4sqQ-2K6ai6B86M3qrcDF-6khFwau--M8FE_KspN3U_n40Zvf6EUd2xQxfQv7nRcIh0oY199hE8BSdEyyRP8y8FSkfMwYVobqYxda8nZoD_Dd6eJaKlVtdN0cnzh0WmkZB3-mjuhKZHsCf-_rPHvcb8ldK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=I6TfowwLjfNPlqAbZIoorsT1h24MAT5dZIqq9EghdjTkTpL0C6t3SaYvoVNMStabHox940Pqth8ZenzweFo8bfh5WWNsnryNHVrqZyV8QD8D8Mmdp_zCQRkmGccYIPMuvMRN5nBOvfPZiUIbAH_cu8A1KAVnCuiFClgEYqonLUYDWsiwxnLECvdaLhsa8cOK5T5dlr_iIxYGC1rpnvX6Wy9aB584afcHYru7FRWdQVrNVgrGcp_7Wq2XCQteN7jfgJooxmGehDZc-vIXwKdlpTSAtJ8L_M6aUgb-5xPGobgCg66ww4ZD8XCME2kpIotQc72X3stQ2JqdhO8IXL1-q6Pb0v-2yOvpis-qROJdqmTStoU_2fy6WVS441Mdymatv_PZm8jC0-NyHHTzoh24kjEtrGR6GfnhJzjIcWjuikdksQtD6g5OLXspalnhMmqPgb48LKtkwim3G9mM6C7RKmqjBO9T9A4mqe1dqn1PC7LzAtBbk3yA7lW6hFlvdpFxniUzvWQhHoxOp6YB4sqQ-2K6ai6B86M3qrcDF-6khFwau--M8FE_KspN3U_n40Zvf6EUd2xQxfQv7nRcIh0oY199hE8BSdEyyRP8y8FSkfMwYVobqYxda8nZoD_Dd6eJaKlVtdN0cnzh0WmkZB3-mjuhKZHsCf-_rPHvcb8ldK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ7wqajq0ZM0Djx3nloCOAYEKVNE-_coIWbugO5HcxnqyFeYxNp_07XcztXY6nE3SMVoPA3rZmPRnBbR4QPHpWGt0NnOKVZ0kMSgFlWn26q6VdvRcNDLOsNtPdCPvqSlaIE3ryqCfH_dh2i32KvwB_-0YFkJgT4WvGeaUdAWB7aElHhojN_HN0_L_xiPb0qO3PeN0W5O0itZMIdyNgf_x6p4wX0cmZLRCPKvRNNThdPWkNR9skjJdofxvYuVI7PDuzmBjJojy_KljoM2a8ycryUC78dYgAALtBqU_dhQ2PlUrq4-YNuEu6QJneVW1ZANk94Oa8l_D4fefO0DQShRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=jAemEnTVgtF-EMz-N911hnA_XKm21LRBOPyAq1iZG6xyVD1kpTtTCO8pQ17Afd1FA_V7m3u7xwIrTce-aXjKUQjSrwZanlymrMVjZ0KpkEq_YBtd5CPm_icaz1w8PIW8rbcK48f9p6bkqyBG9QTI__HXUrY42OEDjkEG0tfZzG7lwrwp30Wc16mpKQ2fVQSZyKodOBesgXqqVu1kx85mLQKKEtbOBloAL2g9ifZu3cR5RvRoEm6IyqLfZ9X1PaYpl4i-oPU9k06e4cA-PfQJC0x4qRaPi9kD9-1PCFjurtLle2S4x9o-_0Ic9WH4r0837mOOmVl26BN5EEewr85_dIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=jAemEnTVgtF-EMz-N911hnA_XKm21LRBOPyAq1iZG6xyVD1kpTtTCO8pQ17Afd1FA_V7m3u7xwIrTce-aXjKUQjSrwZanlymrMVjZ0KpkEq_YBtd5CPm_icaz1w8PIW8rbcK48f9p6bkqyBG9QTI__HXUrY42OEDjkEG0tfZzG7lwrwp30Wc16mpKQ2fVQSZyKodOBesgXqqVu1kx85mLQKKEtbOBloAL2g9ifZu3cR5RvRoEm6IyqLfZ9X1PaYpl4i-oPU9k06e4cA-PfQJC0x4qRaPi9kD9-1PCFjurtLle2S4x9o-_0Ic9WH4r0837mOOmVl26BN5EEewr85_dIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=GT4mQ27PGapnYy5USyeiZfLK2XTJ1dVHQEdy-4Fr7Rou1W8RFbvejPq4UWlWkFHNAV5DWJWNw4iarlaXWXn4B340QKSgvN2hhsQzuvYiaWW036ZXAOz5YcJ9M_w9FPp2DDA6O9kzYYZ9-2SI1XR6SIvLTWOiN9YiBxua_5zfG2WD9BBJuWHZZeBjCZGrxi5JKVKyZ_jNFtDkifi2T8ojXkMlEY0KDen5RUPDI5P8l3IfSiVCyTeiqiLBBza07dR5nFxVkNHQRqDQCRtCnroi03O2w9nrCZnzBp6UbI5RYo4YpfFZHo5egtGu3JBghJxeLN3Vv6-W8mXl-OMn29cdyyCfkENWpdvryjqevaiEYfWfKtDWNBhKtZF2eMd15OJsmYvmUqEjq2sdXyH_KJWLguvxY-AkRoB6U2XhgjqaIMOs4WgougXLn_tnichz9KdfGvHWlCrND9ktDBHLobCv3i3Yde0DKwSGdrdxIUKPfve1lgCbHgOmUm0EJKWb-CXitET7zcDTaRTQIX78BmXXwL0uPMgjLZsESc8Yu-qjjOLlHMtdPMuYy4Rs47un99JGNm-CCGszV01JjHrXh2Ce94PBUs2t5ga1UbaCU9Oj5-XloKo3_-00cNvpMLlw2uQ90bhXU6l08mcuvNd2HvY7EACs5fqBmd7c_QVqyPdS-Q4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=GT4mQ27PGapnYy5USyeiZfLK2XTJ1dVHQEdy-4Fr7Rou1W8RFbvejPq4UWlWkFHNAV5DWJWNw4iarlaXWXn4B340QKSgvN2hhsQzuvYiaWW036ZXAOz5YcJ9M_w9FPp2DDA6O9kzYYZ9-2SI1XR6SIvLTWOiN9YiBxua_5zfG2WD9BBJuWHZZeBjCZGrxi5JKVKyZ_jNFtDkifi2T8ojXkMlEY0KDen5RUPDI5P8l3IfSiVCyTeiqiLBBza07dR5nFxVkNHQRqDQCRtCnroi03O2w9nrCZnzBp6UbI5RYo4YpfFZHo5egtGu3JBghJxeLN3Vv6-W8mXl-OMn29cdyyCfkENWpdvryjqevaiEYfWfKtDWNBhKtZF2eMd15OJsmYvmUqEjq2sdXyH_KJWLguvxY-AkRoB6U2XhgjqaIMOs4WgougXLn_tnichz9KdfGvHWlCrND9ktDBHLobCv3i3Yde0DKwSGdrdxIUKPfve1lgCbHgOmUm0EJKWb-CXitET7zcDTaRTQIX78BmXXwL0uPMgjLZsESc8Yu-qjjOLlHMtdPMuYy4Rs47un99JGNm-CCGszV01JjHrXh2Ce94PBUs2t5ga1UbaCU9Oj5-XloKo3_-00cNvpMLlw2uQ90bhXU6l08mcuvNd2HvY7EACs5fqBmd7c_QVqyPdS-Q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=JYBCmbcAwjyXbs55btaZALqCIYYVZHIxU1RJV3SUHM_pGCrNtdosGyWhRet_Qb6yiN63XLUJGUqIHZBzcMFwhNyb3Wz3x-BZsdq77FBTdw5QMGcCHmFhhhX7nNSiJK7nh6_SlMASKZktxaobhLZ7iKXCqVFRKLSWBdC7UFWHs1ygzq6SNDxPS26PtYaoLJ9MQKrU484rQ2w6kJPv6QA7cGg8clidJfAaZEzR0XzdvIds0_RNeFgfPwZhhaKIpEDhQkDHO8TXeRf82Vdzsj5CRlgC4YLId39GaInYfrEIH_24yCFsZv9amm8LC6G4uPaMaRjyhtRvBmipoYuTZl1jbYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=JYBCmbcAwjyXbs55btaZALqCIYYVZHIxU1RJV3SUHM_pGCrNtdosGyWhRet_Qb6yiN63XLUJGUqIHZBzcMFwhNyb3Wz3x-BZsdq77FBTdw5QMGcCHmFhhhX7nNSiJK7nh6_SlMASKZktxaobhLZ7iKXCqVFRKLSWBdC7UFWHs1ygzq6SNDxPS26PtYaoLJ9MQKrU484rQ2w6kJPv6QA7cGg8clidJfAaZEzR0XzdvIds0_RNeFgfPwZhhaKIpEDhQkDHO8TXeRf82Vdzsj5CRlgC4YLId39GaInYfrEIH_24yCFsZv9amm8LC6G4uPaMaRjyhtRvBmipoYuTZl1jbYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQD5L6_uxNx8Ahf0VwOvBZAwvyMPKgOAv4gbAfLRijlx_XuMT3yXIwYGl06duqzxN-72ErOkWw0zCNy4QsZ64Ey9n5wb-WwrprHbt6h7YRHiKHDpiCSrefI814ozpAjOECIl4bMFii2HVp_9D-qovTXojnW3axXah6_S_D__xVlGkpUfuWeGMUkZiafoFdUxjbFfj_JUXr94Wy6FdrJgs8qo4rlxL2V9FsGsxCkeNlEk-F3C-Azi-3XJ6fsAhhlSIC27VQWGwyv2olC0pn2G1-AuAIO1ekxNXiTaXWDbWHQsttc0YhS-dFspLM2IjhakbqsY496gZXqlWIlawu305w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdO-8c2bhjmVVFXGrClBHUmvRAFaK3pmrd6cisDfkGqvuR005tndv5qj0o4kR1m3P4cC_RhHEf_HnFrkj3oyEXh72lYxApg5Fu5BAcPUCAnJrB3Dn8wt4YnyuNScZMvIbmH-LNz7r4P0cHUgmwXeChqJGmVJ37Lb08Bxt6PnaVIvRFyWuA1yrDu2OgWR5A-7LAf0kjKN-zAyr5h9WfwhyI3_5zU4TRMp66ecBEmcgvxYHr_muTSM98tEdmQhiBDyuLTqbe1ZVHN8_uXV5gcVp68_XwjJs0UX6GZYQ61r87Fi9o0RqMgvWcG0LGz9gFUBEtoFm43n6-UrQoPpNBVcJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaCWH_nYYYQXh35bBA4kIrsmOaX9fhxFNBB4v-Jd32y79UzVopp5Qoa7cwYw3YNLKhcujLr4n_OGSRrqGH0_2WcMr5VkAbYwjwK_kvy0H59jRt2OWlMGOVC2NyqjDeqF5tvEAiZAE2CHqpMuIJ9jehUkpstAF7_HeJQOMqeOj4Fb3Su5RBr5RJSUcbnFpfdYsj5U8MTaD0Din6hhwtY0wSRmZkVYBl6tath190qBGhw3lofgqjNnsBdnIBo0OJZjTt4qzcJwtEXaMgGlAE-rMqmiZuq2jVeM-g5buwsDzGCSheR7uMsr1lpcj_5YqGIHjM-IDZTTrpaiJYaSdKwLHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJP9Xh1fKsDy6p2ncm_reuRSyxM-aNsvTKISUOgN5C86FystKS_kfll7OqaB60RS1Laqm_gtUtcZBy2JdSS_N5B_ziFlXS22hIrxd9MToH0VsO6UXyfQW7Qn5WxpW6FYlj9vOJ3VhBgaUXIQV1yYXRILiL4qlWd5rbLtHCOWPW1GwSb0FG7md_vdZbFG2hvWKDpLD9lMARqsJGREYts7E8DxfgoDXR7sNGd820Po4rzrBB1zcjmqf6qimaZyIrSJrP4gRllyBiJfooucg2G_7XuqxAV7lEDw5yrQFpdiT0Zg9YpdfBKqNqIVeEsrF8LaUP3fEuoquLTd-0WG7pG1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaCOXkH-tl5hjbb8zgjl_xaE7FfD56A-_MUMgFo6bY8PxThQ-i4cwMFGpTFPOrBXUrJ3q8lS8MZLd2uCgOMhBFrZboNx-k0hheYpc1TiUchm6SuyjmdnNuLBmCFaJngFBM-6F2gewb5otTcPJ1ZBO3KMDUziNNfmgQC0-vfjrlR7AoEMO9IEQ58_HPlXZUYIHl4J6q7dOtMHc_3KAMj9M2yGY8duef0XopOtxdicLpqlbdfh4LoWzJIOjXdGh6-eL__IGx0FdMcKc45uvA0W3g2mK0KC-Miu1ayJnlMeVi3iDScAq_V6FP8DBru_-mW4Asf1MhdXKpVwzJP2CtgCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=IIAbiSSAbQqy7492FlOglIn8VEQilZlz-pXHmAjhbEZlxX__n4BAarUUY8Xp34Sh3zR3f_-dWQlWa28nS6esnkcedFqytEa8AZyLVOi2EYkRKDbNmN7g13bxGTw1ByhDA8Gk7i-UP4mhTfo7onF-2w377H-XCPti3dsw1VrYuGRRAizVLpEu9iR2oGr1v3lju096qquHMVdzio3mxBvKvRpBie49lgq1Iu0WnU0HngkyXMJyzFUtKjdrPkZZfLYSZlD16QdR1tETQGfN7scsRD8dxaGa_LOwRwugNZN8tVRZOJqPHLAVe31hdtTBvAFOKA3R_0X5KsbDRv2SY8DNeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=IIAbiSSAbQqy7492FlOglIn8VEQilZlz-pXHmAjhbEZlxX__n4BAarUUY8Xp34Sh3zR3f_-dWQlWa28nS6esnkcedFqytEa8AZyLVOi2EYkRKDbNmN7g13bxGTw1ByhDA8Gk7i-UP4mhTfo7onF-2w377H-XCPti3dsw1VrYuGRRAizVLpEu9iR2oGr1v3lju096qquHMVdzio3mxBvKvRpBie49lgq1Iu0WnU0HngkyXMJyzFUtKjdrPkZZfLYSZlD16QdR1tETQGfN7scsRD8dxaGa_LOwRwugNZN8tVRZOJqPHLAVe31hdtTBvAFOKA3R_0X5KsbDRv2SY8DNeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZKf9btUUkaDNk-k_0nxKvGhz00UMAOv7plQqjCa8weNapQe5IUs3gY91oul27GU-Oqko4PTCuv_7oYQVE_qzZuyntcpClNW6UMunsGbTnOQBuVG3xqg0EebwM_mF70ujG8VTmosZddgPCPpi6M5RdgWTyVvUEmQ7jsoRT4PmY-kmZz_VwqxZTgkS-RhN6H5ZJBxo6t9hpdWupI24btUdEjB4CghE0ccXVXeAE_5nZ_PTtR2VleWzpzi-vl88r-Z7fxh0iKGWOcHJye2fgPib1JzGKzEzMLGZbxOVyAoUwSdDdHIL3n9ALIEGdsZypCyZIEVe0Da3MeaqjdMOkdmow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaxPMprcjRql72wVcQDk6da3ppGUeS1lZ3didzWI0uwmJneLMcGGUHzaDfD0RzlIKlPhVJxTRVLfOqsj8Zcn9onYjxmYZwSe16KpBE2r70FhsYza_r5ZNI15jYuecoK6zhMa7_tbHGE8iLRNxSN4Gl1isQmqw1oZqzf6Z8f7nbcummrJ_IqV4aMzg4IFY0ozC_oIYodFFJaTPdOxKFE0C8WYUJoPKdmm7CCXG4_8ai7YMcovK8A7ikA6Vor-BTN0PRl6qgdQh_PKVDc7tflawGjmUkKxbDqogUOGDa7icyxnqQ4hhww8Cpqh98OArW-O8xTQYpvRPPHIPfSiUV92-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8Ql8AYL6iTHaTD0TP_NtZqAYAPtgcNy1qlmMuPpmZPAwEkqS7Ao-XRWbSKwGsnoNJX4VQhaBB2wlCGn_GHHLAlyZ8G-Np1S1tL-pR9Z0c_TiVhQ0ePdnbrUkkiZTh0QrvbRaXIsKJ9gKEqeUMvdZ9Dl9aKH3kKb_iEQmLDm6Ba7RtPxCqGTVO0oFmUKwZcuN-EML058MgE5T1zOQeIkVP_WCAxnYrSQvhGathzZtyv_7bcB28T5jj1l8yLYFcPihjfFH9nYnsgILRLmNcPbpq2h0PCF_x5h2TY-gBqpZjneJA7QbxP3xkyVJlbFBj7w3ToSvyG6eGIeZN2Kb0Xn9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw2BwZuyShe4JVFUUVe6m9stRfVu5__pMuQ_ZMD7CNSGrUnBh-4NxVCUTksSTkDp81S4W-7PNf9vJ3f_4VlDgZmWRsre1QmtvXykDflN8LqNe37KR92AIHURMQeZzKZAvcpN8Qd5gSpVpN4a-aJsj4SK0Hhl1hrX4DlqcGFzhDpV-dLbcAFbBPDhIy2lclG3D-cGIYcFbDkT69yfTmQbgFvi2PUXonK8IkCYw-CV6EYidckEXr5s_35SZFaYiJ9hBGClROoYqXPcLbJCX4i0wOnyFDOlyX4opTb_e9K2to1AkhjRsHq9HvYvSlrLYNREDA7N_fA7Kt_TmZQIVOYczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJK5f_bctBt8P2xRTVc6khzXDn3r0gntNWHweDN1AApWrFoIBSpFA2GrTDfEGG9v85E6494ewx2Qsqsu4c18diBLlPZ_QBW1PRaxoif4dPY2EZXbwVhsg5uoVS0Qys_iZ25PSV0qQqHheVAVMlstibtXXm8X9a6ygbaIiN5ziVPfFH5McmOJW-NwE9xoBmJhk9uyj0Ftjspvh4-MiL9h4TmdWdDoRbfsRCroucWvwYaKDG0fU0TGSjguZtqMW9FwMLSa1jgqP4U0xdpotwfKg5MBAc6tdFKBWmTUjHVXEM99Qn9E8GMthn3Czc_5yyxkfK68ohtVT9mZTluRY1eTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEWgy9Vczc4kiVhFgUiAcGrJSivKjx2UUP5-3dnnz79xrW2eJfvCgDgk3kOo5w2PWJTcKbEwAyTKQbLXUJDwJGNOa2PVuQubEJyrWK04hTv-MsPk3qGvZo3Km2fLlbSxXL0ZiCUk0PwPib9rB96ds2_ZHriCoVZCFGIanOWGxvJnPuJOPUYhexj7ODrdxOmhYNXoAcyx4C4tkb_Q8gLIwZxq0U67SDd_Honb06LlpLu0d3-reLd9L37rUi5Nzk4qHi6LAzeyTMfyrmzwvROSMiafmg9chBCWQSXi4P3OLBiCrvG1wRXOUEKorjNbeKiUZ-VJUn90JLTh6FQibYYgqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quyHWXyVzK1YZ-0lY0MRndTv29Tlf052CbHgEfM2GZn1dq6VrHPbKrrxwJYMPT1kEZaXw_cqkeisnOcBQ1Rnh889hRbG6i9sXWqYkUvLYCvA9vg3L1vH52zLRy51H6P6h_r_ezpt4zba4eRVJuWtH4C0ZeknMedpB4M06XIDtlb4XwNzACtSn7RYd3pADW3cNVlSbPdq4acaVhx2O3DzSh6pm9XegQYsr4o4O4s3EMDQUHHu4IftFNnWXFFn2W7fgwjBonSVi9CZwO73mIZ1fpBa1boNF4F1YQV0v4fW8Ek1EbFA9TuexGMUziXUSbWL-SuRX1j6QFy7bW-KalH-4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYVxVwuX4ZVpeEWlck-KyxJ9QmhgnloYY4F6Z0ITAkHTCJO30L5nZ2u3JDywgSGaayU-YD87-9zmQHQ9HkOfBSs-GeX5fA4CvjeUBmjnP9sE2WxkWfYEgHuehHZ07ZbRyuPhSgatGuVeprWIpwyeeneSk7MFWjyPb4MdU_j_1Zc3aYuXCSsVVjXrURigMoOOqZYNTroA3hW19faEe3xgXoft5O6MIszkCBVX7sxKyX-e8Xo59Yp8i-io1mzC3IsFD9A5j7gISCxA6h8GJfx_4Ch6k54RUi_UPgxjvAi2Of7pCmrjr28bnbwMHm3pebKwlUbL_AXw1ea2VFKBOStbMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=LCUBUkBzdQCsIdGlQ5csdKlO0kWzAlMhaBdtSJ-CDhkQ95SulTK_xSklwBfXUmu57a4bmSydESjNMl7E2rQj6_6zdSkmQ_MqbM2RfM4xnWZ7hGkJvPs_WwT6_lJGKAPAaQi9yOaIo7CezqaQuYBsv33xePBYBYCaX8ZYKDOOA4JeDnoR17IwIkYw7wxd2PqrFTRgnFqJM84o7MJBPETBMN7LgygiWhGfxG4wXUB9rV8uCcr9l4DNqMleWJhWQq6-pgI48ur6e7xo-Ldxb3qlVsLPGJeoVrPZZmJKCMogUtQnkXZZ8JXNeqOKSSjp5411jn_FhpCWWUj1XXICM3VAoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=LCUBUkBzdQCsIdGlQ5csdKlO0kWzAlMhaBdtSJ-CDhkQ95SulTK_xSklwBfXUmu57a4bmSydESjNMl7E2rQj6_6zdSkmQ_MqbM2RfM4xnWZ7hGkJvPs_WwT6_lJGKAPAaQi9yOaIo7CezqaQuYBsv33xePBYBYCaX8ZYKDOOA4JeDnoR17IwIkYw7wxd2PqrFTRgnFqJM84o7MJBPETBMN7LgygiWhGfxG4wXUB9rV8uCcr9l4DNqMleWJhWQq6-pgI48ur6e7xo-Ldxb3qlVsLPGJeoVrPZZmJKCMogUtQnkXZZ8JXNeqOKSSjp5411jn_FhpCWWUj1XXICM3VAoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=ozq-QrPhAAoGqUzmBpeEeH_GSdYKsU2MnMR0wQHVVJuQqyF0yE6SoLhJ0Lt05e_JD3twofrUZpZ2Z6E8YTelOe8KY00uSWzEaWyCIKE0BY6QEgrmiD11UO7ksV9TLQcaWIM4Aorgse6T2pk-MOCK__5vgK0b1jaGpa7RzkbvN4-BhKjt5VckZCvFG-pc8D8I5DYvoRVici-R-iJI6YCqU9m9peDfJ1YDGjey45hzyxPwHCFcJeNUn5JnZhLIJGa0iQxqnGzo5AXHbYD8SyBRCLDkPY8jYmyasAuEO_VNplisQfEIS8L_3sqlLrRCSJ5LzQa62ih22hwoovQdaVz7og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=ozq-QrPhAAoGqUzmBpeEeH_GSdYKsU2MnMR0wQHVVJuQqyF0yE6SoLhJ0Lt05e_JD3twofrUZpZ2Z6E8YTelOe8KY00uSWzEaWyCIKE0BY6QEgrmiD11UO7ksV9TLQcaWIM4Aorgse6T2pk-MOCK__5vgK0b1jaGpa7RzkbvN4-BhKjt5VckZCvFG-pc8D8I5DYvoRVici-R-iJI6YCqU9m9peDfJ1YDGjey45hzyxPwHCFcJeNUn5JnZhLIJGa0iQxqnGzo5AXHbYD8SyBRCLDkPY8jYmyasAuEO_VNplisQfEIS8L_3sqlLrRCSJ5LzQa62ih22hwoovQdaVz7og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=fdFmkaHOOvLSKe93i6Wq1Pl_dC9_RiIJ5mXuMOZLz9TYz3G1qc2hdwesRl29r5o0L1rTetxZAqNM4dxHJK4hN-N_Ukm6sx-84Y_V3VwfayNlj_rGqQb7AThZSFD0pSEgJzMJdL9AaIXoeoXuWKFtID_5gNtiShnO4ozIYuE2STfyA9MtJUN1DAJqzcdWJceuhSX0vBCZWCN1S_p2WuwdIbLmrM4r39FBRbaRW5t5tvcyy4a_Wt6yVXqx9KpzMcmuhyEniPuQZwA6QMZ0taDZnpReC5xfThxk8Ogs-lbuOvrGZTxQK4vc2kHsOmvC-4HkDzdQ2fZEtoHuxzOPnC8qCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=fdFmkaHOOvLSKe93i6Wq1Pl_dC9_RiIJ5mXuMOZLz9TYz3G1qc2hdwesRl29r5o0L1rTetxZAqNM4dxHJK4hN-N_Ukm6sx-84Y_V3VwfayNlj_rGqQb7AThZSFD0pSEgJzMJdL9AaIXoeoXuWKFtID_5gNtiShnO4ozIYuE2STfyA9MtJUN1DAJqzcdWJceuhSX0vBCZWCN1S_p2WuwdIbLmrM4r39FBRbaRW5t5tvcyy4a_Wt6yVXqx9KpzMcmuhyEniPuQZwA6QMZ0taDZnpReC5xfThxk8Ogs-lbuOvrGZTxQK4vc2kHsOmvC-4HkDzdQ2fZEtoHuxzOPnC8qCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=lFwetKNieZbV7Tld03spjrp-xplUUxVSe990FJ7H8g92bfrf6c9dbDtKzy07h4tsqJMcIarh9poxbloCaJAKHGlVZPNAYQ-EMRvGKUCH7AslrDvgDNqNotHhPUnBp1gaUllN813qzg5uX_EE9Gd6nQk49rd6jB0kSSlveNDxuZ4KFsc7Nsy5gqryYytncCh93ZKKUbYdJMAVtmnToEKOr2wgaADBhhiIPdK4WqXUOhgrjYu8HL-TJE6jkzS9a05JAvTbg6shuBPRjJInL1zs8q_7ushwr11-T1U-JVrcTE2dFq_I84KUKv1i03LCIO9g2sIlykA32j7a6a8iFQuN1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=lFwetKNieZbV7Tld03spjrp-xplUUxVSe990FJ7H8g92bfrf6c9dbDtKzy07h4tsqJMcIarh9poxbloCaJAKHGlVZPNAYQ-EMRvGKUCH7AslrDvgDNqNotHhPUnBp1gaUllN813qzg5uX_EE9Gd6nQk49rd6jB0kSSlveNDxuZ4KFsc7Nsy5gqryYytncCh93ZKKUbYdJMAVtmnToEKOr2wgaADBhhiIPdK4WqXUOhgrjYu8HL-TJE6jkzS9a05JAvTbg6shuBPRjJInL1zs8q_7ushwr11-T1U-JVrcTE2dFq_I84KUKv1i03LCIO9g2sIlykA32j7a6a8iFQuN1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=BfEcpKx0NoQPU3Llew2-tnborCOFCV0kLKCpeXSU4aKyLyVUblBwz_2T9YvwjcwCdU4EOHuiE5Hh3f2DyptusC5c-qHJ8Ix6O01_q7cg5TZ_SbW9eH9KCUjacMHiSD_hlWkpx5n1fUhSW-PdmR6xmMIyyHpMdEeHUjleAk6wTtnbLzFPG_VYoqjIXQjO7X1zAvMBUUTOVWp5bhNuoclFhnQpI06uiJCjRT24asPghAA0n8g3hfbXdmwhoB79QPzUN0BUcwbN6gOBNFIapSQVSnTbBEv8tsWHRbIhocL89dgfxcER9U1mS6rI1pYBQI1F5uLWPD9H_0cyKqG7A03E3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=BfEcpKx0NoQPU3Llew2-tnborCOFCV0kLKCpeXSU4aKyLyVUblBwz_2T9YvwjcwCdU4EOHuiE5Hh3f2DyptusC5c-qHJ8Ix6O01_q7cg5TZ_SbW9eH9KCUjacMHiSD_hlWkpx5n1fUhSW-PdmR6xmMIyyHpMdEeHUjleAk6wTtnbLzFPG_VYoqjIXQjO7X1zAvMBUUTOVWp5bhNuoclFhnQpI06uiJCjRT24asPghAA0n8g3hfbXdmwhoB79QPzUN0BUcwbN6gOBNFIapSQVSnTbBEv8tsWHRbIhocL89dgfxcER9U1mS6rI1pYBQI1F5uLWPD9H_0cyKqG7A03E3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=nvwOncoXHGOgKwTAEpMvOn5wl7lwjal1d931MffhZ2kHH6LmCUjKdBJahrMqJGNTljtm0Xh4OEYezSNQK-UDbcv0YJ-vuxT-jcwZQPdBVFKdiU2PLRm0yDR75UC77IcMosFwV_1WK8oRmCKUXAy1c5Dtra3HOE2_G2-dXtkzlu0e90XfYveomsZuowK41okHYZOg1zm8Z458pF23PgpyM3KDOZJlMSE_xuxgdCgUAO2FVQjzYPyyNeDeEiCaWeQbfIlYlros_sjPIgXE7hmzPqUYMSIqhJKzoJeBZi7xtrwpW0slSZmyOTrVzWsek9uSO70dPXOaks03wNmsTBINvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=nvwOncoXHGOgKwTAEpMvOn5wl7lwjal1d931MffhZ2kHH6LmCUjKdBJahrMqJGNTljtm0Xh4OEYezSNQK-UDbcv0YJ-vuxT-jcwZQPdBVFKdiU2PLRm0yDR75UC77IcMosFwV_1WK8oRmCKUXAy1c5Dtra3HOE2_G2-dXtkzlu0e90XfYveomsZuowK41okHYZOg1zm8Z458pF23PgpyM3KDOZJlMSE_xuxgdCgUAO2FVQjzYPyyNeDeEiCaWeQbfIlYlros_sjPIgXE7hmzPqUYMSIqhJKzoJeBZi7xtrwpW0slSZmyOTrVzWsek9uSO70dPXOaks03wNmsTBINvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVS00c0fHiFd_LxkdnWnGWOVv-4D8DafIoYG-TwnG5hkgVuRbx25NtXVVFYng9qE3JMHond8juo2-4kYcyhLtSqUesh3xu90g2THFyez26naadZAB5V_ZC-2oBYKBQ9pfr2RVpwXSeGDhjN2eYIS8Kc3bSaeYHsFMEb5HWd0fT7FvMh2OWsUIJUYyqOewULY34DoKhK41niFHpn9HqWw1jmxWz-b4yjAiWQEi3NnTiZkoWFHjE9mfO8-fZD_4gMJx1JlpiP2jwiAeU7pykj6l1lpqUj6sMNVrApr66iSzAgEAaIR3ryTDUMLUaEMSp9xEhr95fQy1lmIiE0CfF8WK_8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVS00c0fHiFd_LxkdnWnGWOVv-4D8DafIoYG-TwnG5hkgVuRbx25NtXVVFYng9qE3JMHond8juo2-4kYcyhLtSqUesh3xu90g2THFyez26naadZAB5V_ZC-2oBYKBQ9pfr2RVpwXSeGDhjN2eYIS8Kc3bSaeYHsFMEb5HWd0fT7FvMh2OWsUIJUYyqOewULY34DoKhK41niFHpn9HqWw1jmxWz-b4yjAiWQEi3NnTiZkoWFHjE9mfO8-fZD_4gMJx1JlpiP2jwiAeU7pykj6l1lpqUj6sMNVrApr66iSzAgEAaIR3ryTDUMLUaEMSp9xEhr95fQy1lmIiE0CfF8WK_8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVTKpdE9ve2X-HMc9cVIfu_8uWBDz77OWv7xCqb6CZDxPMly3d3E10u7EyBmfVDIrQ5HflGlGcSDaYPGRae6gD2NWSP5b4XSkcZ79EOqsuMCBER-CIot7Rhh4d9OBZIZgQygsmSxHX4Vvmk7iP77xvaSZdZIj2sp8RegZ5ySMuZiA2xFdZxwiJ52SImS21gNVtBZr3xLvHeDtLfX8_FGmq0L3qir587NJ7WeJV_fzwrjfVAD58D6tiLej94f4xfwmE4lYOqfzNNOAPAD2rE2y49yQ-HLmorR5PjHWNyZfa6ybOX9oGeqUVGQfS8zREKO72eaPtDwsfVB5AwEZxpmcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=upS05gyEy8wUdSzs_aq8r3Tcwv__2A09Li4177gsnIsef_lU1TZhjVVYs3VRwK9YqeZnqBBXnN-wTF5T4e9mDsT9baUXS2haVGsvKRD7Hu19udPWrXQMKTLTV-qdnUvWLQy_i0go6LIl63aJA8psxohBj7sF5RmTgabbapeuZks8qZ9MZZWOsmLvKvSxqbLXLd1xbPuDnV40GM-zISCLUkeIuRoVg9ZNxIb1NARGHc3A-ikJ-64NfhTUjepE7v2eKPCA0U9Ya51xpvNLBdVKF9VvhLbHvRfTB8ReW2EObVUNOp7j850cQXU7XhNDub-IznwdyJegUbtJYdDR9U5ciQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=upS05gyEy8wUdSzs_aq8r3Tcwv__2A09Li4177gsnIsef_lU1TZhjVVYs3VRwK9YqeZnqBBXnN-wTF5T4e9mDsT9baUXS2haVGsvKRD7Hu19udPWrXQMKTLTV-qdnUvWLQy_i0go6LIl63aJA8psxohBj7sF5RmTgabbapeuZks8qZ9MZZWOsmLvKvSxqbLXLd1xbPuDnV40GM-zISCLUkeIuRoVg9ZNxIb1NARGHc3A-ikJ-64NfhTUjepE7v2eKPCA0U9Ya51xpvNLBdVKF9VvhLbHvRfTB8ReW2EObVUNOp7j850cQXU7XhNDub-IznwdyJegUbtJYdDR9U5ciQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKS5Abcd-dZ8TeEYznr2FLb9THf7jM0bYdgwmbB6mYSi1fO6O-qlee55dQsgvF23XKxkxRNb38X2IdjJmTm0POnjhww6oJNxYYXYQSnIGZGwmpdDBbGdN52NJdgfJRyc1OpeUVVf1NpKCF8wzsskbQIQlbpmSsxT6JVYcQ47_2OUst4oo_07l0jXNQ82Wcu_aKSEjdq30kMRS-KHyjI25PoIWvExzvfMJJT1Ut0sxelpr8jkQ4dc3vbd1Y0y6GnC6-Zv6AK_xNEiD3Sp4JLsHb6-5t3Y90U8QR6Zct3EuENkehnSjI5Yk04XY-MUbmzV0gVYBeiezRDUK_EKFoY0_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcP1czKUEFern2Cpba98cj4iQwe9u1ecAP5rR5uDyoWtM32QNGYTikkbYNtRT9l5ek9b_rBssfOabYZ0zTo4B6jvX6_WNDslMqehVW9KW4FHw11IW5H44bKtt2b0yo3bOlGcwBeC86DTdRPI3CMfD4VN8jrl2VlOnwBpOwdrYFu1wkPaABvUFzPav4NJMpEJsw7ru4T8sBsZS1wNBnTBVN5JlRdZAfTuhrNtNcw9VZMpOk6xAhL_1VHW2W8pVl_lfY4PhAtcSQeah5AX19IQzGaLZ4b7CmI4zoq-bvVADb2Pen-rYNQwhp01As-6v8LtPVYlUZquU35d1BGkx04IIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHT8LPPmyhzH5AaHnwwmfIwwbN-vYa049bvmP3qt6bfJAaszuVSKmiKOxbFkmIh3jueI2GI2ol-BOkCF0zESNz3KoE-ih-fnTVY2czEDTGfaKjrlmpS8j6PIyO4Vdco1bq33BsuhgrkVGjMuGvfrFi49mvWFJ_GB2LvURjk6sPms3sIXVQg8Bp6gjtqGe3OK-Ddk8JN2YRWMYR0Iyi1UYPrM1Cxz_TBqjeNgdi4x_CmnuXGZj5p-uqWQAGez1rCiAg0U582SPZl5y30yKwihs4ANGYznfp4c0Ev0coF6w9WqcWzgcw1yYenM6WFBPeQpHgFDH2wopLGVCXRoN1P6mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=OPW1oz3D9qnHiEnR_cXkqcbNJgqHnZizC1Fu2AvjRJNTsXRlPqpvLM863SXvuc6hFzKcZGm3nE8u38Za8BWM2UJpy5sPPXrWlVQ_2jeDkqn9sEKQcVf9tDvrXVk0kougNlM3d6H-V9SQKuK--k7hhELsKnSs_izAmVf95sts35TRJOJCEeCUlDXwqU28r87osRvZLvYlzi6ZXUKI8pfALwJn_msvSPsSJPIlUh2hLyismECEzRCeO48C4vv2q2n39-Jq9b7bcwhXz7LFYCXHDT5XCunLzV23OT7pVEz78rSrwXegVAeV7ZnQN9HfoTBq0Q23oH_10E9p9Esj_3fUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=OPW1oz3D9qnHiEnR_cXkqcbNJgqHnZizC1Fu2AvjRJNTsXRlPqpvLM863SXvuc6hFzKcZGm3nE8u38Za8BWM2UJpy5sPPXrWlVQ_2jeDkqn9sEKQcVf9tDvrXVk0kougNlM3d6H-V9SQKuK--k7hhELsKnSs_izAmVf95sts35TRJOJCEeCUlDXwqU28r87osRvZLvYlzi6ZXUKI8pfALwJn_msvSPsSJPIlUh2hLyismECEzRCeO48C4vv2q2n39-Jq9b7bcwhXz7LFYCXHDT5XCunLzV23OT7pVEz78rSrwXegVAeV7ZnQN9HfoTBq0Q23oH_10E9p9Esj_3fUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9DrsLbgkbqYdjkpb_KZGfnJa3gnGYAvKy6ed45Z7wDRbKyfAk6FOluTgVi7_1QGfaysfCda9U2oHq5egunSVQdjw_F2WAu3H7BC6DUEQ6Q9yhVlZcYEXVSsbYN8RQOtc4byLrQBADxQl-QRd-VaCKm8M4tTVfnhl3-6N2L9z3mXNZB9YJHj09fYORPh12l1ejcAvCBB4YPry3A6tG19_QcF1t9Z3wveHAOVB_-EBmqTDUaicPkWoUp60V0D5LimifFEakLWnvCMQOceZVvNrc5kvocvq5oaaushYvevmjT0VzqNXoXYt-kbAj64J4jYytp2-eaLScxz8hYxaMEBDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vntvPL61-hpz0yUZTj23autCkvxfcRPljbPM6dib0grdKtiMgmI73X7u2G2qVgbV7ZhxUU9e2yoNpzKiyq6Tbdxx4IIrZ3bz9Ei_Aw8UrvHFSj2-3DTIcRph41QHX_cTZGeG6BAOHu92V9NXqsWayHZQdpGmQZdj3Yo940YJ938wsz88VCaf-UUGSVpFwfZMGEQAy2Ubdcs0C3swa29-RQ1Rfhp_jyZG1_Od2QOT-qvV2G5dLSzyy0Ktyu5SMTHbGlJu9FLRwvZsn_7R3nQGsjEkLf7gcWMQNLLKZHEDAN2dDEXKJ8G9ElTYGBzugGcVIR5ishLMzI30H6SGGqbtkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDfOrpaV4OkDdnicw8If7ffxEqlw066IoSIq5JFyvke7OeiwHgVTaADb2gG0xyMp6Zi2irhRLqN0gcymTm8hsVkqU68xNiXnAGZTgp3Dxpncvkjpict5v1nX8gYI0xtHrboo-13-ntoLXtHm9RKO__n5LYYkP0-ufqx7qb-2GKcsUqWvP9RkFanulOmST_ZygXMSIYg_8sh1-zH_0uXzpsULoc63DVHK0bkAvHRBP8YRHyAmvVGGOoPvMfPkH3uDpEtLBvWdUPbDJMHSX0r-syfdNH7510oj4FBn6AGSkgiEl8e3v9LjWX_0axhAc08kw8_pUNlTrTbnjQx89DN0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg1Cp0Y2lG3koDJZo07-af_BkC-GIwa_jbOufOcRlWb7FG8XWRDaqxrqJ1pyAiz5dUwpTA7nmmCuJ6WGWuXzYvfc0SuowXvHQ35glGEkBw-HZomWp7s1b4eNpmuOtMg94KxKY-AnN4lxZfnfwyhmRciG3r5Y8yQ68eF3XWulei-46exCmLn1q2_m5b9C7irxhwf4fsV__-RUcVWkDP31AU4-jGjH7QGlM_XHatC5W6kl1xDxstIEPMBgWHlCG8BhMPXWhAvS9x5isfrSjuEqX_IDWLat92UCgOB80lMOkh2mOYIV1KsA6bdEpv4VueiDdDe1VOu2uxTUGa1vr7tOkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=mEuaskiRVwJeRVEgBfIHl8Ok86swCR82XWmGRWD_R2P-7sgjeDPTH1rmVBt9WZhWXz5BzdCuZODUWeqymRpOplR23Uk9ReDNNfVp4ubsls2Hby75gUl4tpOuv_0X1Xh45xS-torPt80fMb4ge7hEp60z1UGMAKHRJfluHAWFA4OAjR4aqpST5Vso1YgyjKafIB7GNI5N4rEhRYfxfVXdMg2cB3NweteQC5xNAi_n1ENR33ut30iBkQ1AL1bdUhSVtgSTR6yhgytzXJFxMNtJa7KyOi9_7AxLAHEUxAEedHCpLgvDkPA_RSx06zEGS_TDk6SsNHasu-fyeeLEPqrc2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=mEuaskiRVwJeRVEgBfIHl8Ok86swCR82XWmGRWD_R2P-7sgjeDPTH1rmVBt9WZhWXz5BzdCuZODUWeqymRpOplR23Uk9ReDNNfVp4ubsls2Hby75gUl4tpOuv_0X1Xh45xS-torPt80fMb4ge7hEp60z1UGMAKHRJfluHAWFA4OAjR4aqpST5Vso1YgyjKafIB7GNI5N4rEhRYfxfVXdMg2cB3NweteQC5xNAi_n1ENR33ut30iBkQ1AL1bdUhSVtgSTR6yhgytzXJFxMNtJa7KyOi9_7AxLAHEUxAEedHCpLgvDkPA_RSx06zEGS_TDk6SsNHasu-fyeeLEPqrc2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKYLxxY84BLVPs_4QaWhkBy6FrbXkKB7HnpGVPODo-gUxHQjohGzmcFP7uc4khow6g2W87nxlUjBNOPvdCWMQgWKnJDBLDsHJITv5mNxhkiJtbr4T9Tzz7TGA55uww3O_dOtMqTYK3Us3r1vxlDHIMEU8ThTAP5a_FITFWmUwdair2l9AhVfn_tfBJEGFGKhRrXgSINXombTkKqQuX-x_EKk-rudjphUBRrMFuD8hkheNPjlnyKalO9F_6ovXYPLe9u3yiHxr7LmScIFKO50rou4Rf6NtXQ5Bga2jqdv9JvLW87iEtVF0DpjMdWOB1z8GTDP8xS_0Uq5dp9It24uUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOCsIMFNntcEtjarsDB-K0FvpLASaYFis7fmB8EYpRvd7dpT92SExCMcpY5Ux8UrC-U7LqNlTSalhjYte7prwD7dC7Sp5hrymJm66mTTU14cNlkGa92gxNYRns-F5hcvjxTv1uDtrfdZgjF1PfuijT-Jeva8wkugjP1a1dfPg4BmhrI5s-3ZvifLsFL5Mrx9HMU62yjsuH4rTFg_97QWsGBlM3cCIQl3im5V_oJr_ywGbLb1xZB0-M6C5YfuFOw5b61rboBDj6SjeJSJwH0PEF185o7F2nEoqgbvgguentFvt_hOA1Vzn8HGOWNDGagThsmSWPJME-YuNMH94tzZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=oSE7FMDX6uceRlyTsjC_6iLG_gxktoH3QacVjSc7H6hRABTSOafInoS44kbvk522nRsq7lRsaOEtiLgWqDXVAzRid_Y0blwGf2DYADdAVTzY6qbLc_fxlgWXOkT-ShVR9Skr3TtidRtNG22AiVvqlvax7BCzlfycOeq2gLlAbYKVZPPZPYbar4u5bTabao_7vDyLl7Xi4LPCTeIVfsGQRHXdAypU6TNQE3GxySOCbvtBW4QSA8RiXKCHNa4uDceWyXSwyBXUIT_yH9tUokg6tfAJx--EhSxSCBjYPf6H7x9agIZaBIdWv7l5AmBdoLCzgfbCBZLjEdzGwfFH1P8UlExLaFmdf-m8c_-au9Qyy8lHJAVpR9pMADD1XNrmYFumuykJIWCHYIuCv_mRSsFZ8iGBn5-oG0ltRBGzEBpw3PIXiSeuz7_WK2AfqoSncDAwOle93LEJVxKarTK1brJ78FQxxzOQDh0flWZr_yD8JTp48dferUOIToNBPthTUYghPuvJUldhhnvznLXLr12bCB3nVIXgFrwTR_6m4nTclYOZyeQgBhocwIrxp-EYiIXquB6mZh5pAZH0GELzBlDqntS-SdCctAHdwRFpw0qo_fQRHapL4nhaj2aFQdrcfwQBpFEU5REEEGJmtRm8I2qlOYYXXmU4fZd_BCbtzcDH4Hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=oSE7FMDX6uceRlyTsjC_6iLG_gxktoH3QacVjSc7H6hRABTSOafInoS44kbvk522nRsq7lRsaOEtiLgWqDXVAzRid_Y0blwGf2DYADdAVTzY6qbLc_fxlgWXOkT-ShVR9Skr3TtidRtNG22AiVvqlvax7BCzlfycOeq2gLlAbYKVZPPZPYbar4u5bTabao_7vDyLl7Xi4LPCTeIVfsGQRHXdAypU6TNQE3GxySOCbvtBW4QSA8RiXKCHNa4uDceWyXSwyBXUIT_yH9tUokg6tfAJx--EhSxSCBjYPf6H7x9agIZaBIdWv7l5AmBdoLCzgfbCBZLjEdzGwfFH1P8UlExLaFmdf-m8c_-au9Qyy8lHJAVpR9pMADD1XNrmYFumuykJIWCHYIuCv_mRSsFZ8iGBn5-oG0ltRBGzEBpw3PIXiSeuz7_WK2AfqoSncDAwOle93LEJVxKarTK1brJ78FQxxzOQDh0flWZr_yD8JTp48dferUOIToNBPthTUYghPuvJUldhhnvznLXLr12bCB3nVIXgFrwTR_6m4nTclYOZyeQgBhocwIrxp-EYiIXquB6mZh5pAZH0GELzBlDqntS-SdCctAHdwRFpw0qo_fQRHapL4nhaj2aFQdrcfwQBpFEU5REEEGJmtRm8I2qlOYYXXmU4fZd_BCbtzcDH4Hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=PRtXbJJVNVaoiwHxpv_zAtTc4d4soNbHxsgim1bWjxXS0Y2qv5C3X7T5dGPKwEfJXT2jQdZdrXoV7XiI7KWrm_XNodI51Mgu0Aj4IZ71SDIu53V5EWOynHQJ-2CUFUfOmQ9WJXgtdUMsk9hMZoNdNUQD3WybCXYznIw1da-zN2NIjcDlaAjWV3FXMP5-rCPZyKyoL7rH4R8ICp8qdnovSLwR4OiLL8mtNftRk3GRT-ZvQo_YiOun5g80Gnc5EFPmK_7DpsCGeGkRGY_TNlxOMt9-kC9Y3ska43-zgsydue_GXJjZuHQ68ZEG8_XvNSku8vQU2ZngwqGVwN69Nzmr_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=PRtXbJJVNVaoiwHxpv_zAtTc4d4soNbHxsgim1bWjxXS0Y2qv5C3X7T5dGPKwEfJXT2jQdZdrXoV7XiI7KWrm_XNodI51Mgu0Aj4IZ71SDIu53V5EWOynHQJ-2CUFUfOmQ9WJXgtdUMsk9hMZoNdNUQD3WybCXYznIw1da-zN2NIjcDlaAjWV3FXMP5-rCPZyKyoL7rH4R8ICp8qdnovSLwR4OiLL8mtNftRk3GRT-ZvQo_YiOun5g80Gnc5EFPmK_7DpsCGeGkRGY_TNlxOMt9-kC9Y3ska43-zgsydue_GXJjZuHQ68ZEG8_XvNSku8vQU2ZngwqGVwN69Nzmr_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwYD6_GtNZjEHva2brR1Qogt08M4TRztt6AARmDhQ_vzGKiykGZhqrLnZtzTR8LvoIQMTuK7kv-TCOUWaGflTEWosf8iJfT-XbN0LKmTKpSLiuFwbbfLOXf28hDi1nZASHuFBzLimEdqf13sHs0lDi7tfAJaIKPvGtQvwmJWnrvxUZbHpzEfj8Yjb7p5zSm6LyST0K18vqMHXnCGkl8wKHahhRPFMNGg9nMKm2iKej16XoXazGYoA4-PHI0YldCf66CGcYZiED2v1FCf3rhko-jvxaBD0NR_atKDQMDEO3QHR6B1emTVPPWsqs8ik1QuaBz950uzM8cXUpP0Wa5MgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=TWG7Diz74iYzmCipj7rBZJkZ0FlZ3NND5IgZxS7-8y9pe0_6aHGoVgm6l6-bv5Wg4TabrWOoNAHvSUBSKN_yXirhBAEgU3uN42Yr2BPpA-vG9XwuSqM1NvfcdJkbcNkH_jFuXoJCVXeUcfgrQb7Wo6P1YbHRZsDumJzk2mGHoTtK7fxTZn5-xHyklBBwg9H2VXzXvtVxP2OEmVtgR2qaMeLrF6Rq9tDugrHhhVk52dAjdHVdfVz08Igd9T8TIPYTydc9cFUCSnsYQrxYQJSPNSzlPU5PmITWKbHS1II76I2AJz6718TxvW8hby3efg05C8RnYp3Uy723yC7bvhsADw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=TWG7Diz74iYzmCipj7rBZJkZ0FlZ3NND5IgZxS7-8y9pe0_6aHGoVgm6l6-bv5Wg4TabrWOoNAHvSUBSKN_yXirhBAEgU3uN42Yr2BPpA-vG9XwuSqM1NvfcdJkbcNkH_jFuXoJCVXeUcfgrQb7Wo6P1YbHRZsDumJzk2mGHoTtK7fxTZn5-xHyklBBwg9H2VXzXvtVxP2OEmVtgR2qaMeLrF6Rq9tDugrHhhVk52dAjdHVdfVz08Igd9T8TIPYTydc9cFUCSnsYQrxYQJSPNSzlPU5PmITWKbHS1II76I2AJz6718TxvW8hby3efg05C8RnYp3Uy723yC7bvhsADw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jm_KpZ8BIp6mhvJNtwuHY7rfD8qm7IMEM4fmEgJUBfk0asGeW0bJDWqnyIOziea_RudBj6iQSjSVfQwMDcyvac7RVxdUAta0yeEa-Rmuj_XcUoTzJW03fle4HWju3NJyLYYpsDtbuNl3RpnLGP7kxVLGLIXKo9NoXwu_jtTselnzHFb_1Bwxl2N4fDps8ij-dBBcVNtF5Iz8RSu66Wrv1PHh1LV5GhuoiTiI_nJvA7eDiBceEtowuKiQYejs5rZ8vwY2HQuVL4MdOECfUnC2ORc5FFUOZ1hvXLHRBhSnIYzGK0KkV6_0KPl_pNswBAQhjAqznwQ1WIHhgXg6QZj9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=ZWX1aNyLTmkxOOyih6hD7I9H529ICSdLiOU3GlIX-P9cf-uShyBk0N32XydobPgIF0KfDp9ETDgmb29egbtSp7zBTw5E6S2oQX3AltsUYD0LTtGsE5VnC1FMfKlS-4JT8cdymnw6MsvHWV4wwUX--I2HtHSLeuuh0EtZGFxI4gAGbKLC3S6zGJazEPdgEigIswtuiMVf0SFAkTrGOUwUhVuQHXn-SvB9hoIk05Yqg0QxxOdIg2JG5aMj2XQC5pdx5j7-rw1kZuFwEBisSlmBkQ306veF75IvJpdDn8ipRMouDwTNXDpBYig5xv482aFUScmB0M3wN0VomO5bt3uWjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=ZWX1aNyLTmkxOOyih6hD7I9H529ICSdLiOU3GlIX-P9cf-uShyBk0N32XydobPgIF0KfDp9ETDgmb29egbtSp7zBTw5E6S2oQX3AltsUYD0LTtGsE5VnC1FMfKlS-4JT8cdymnw6MsvHWV4wwUX--I2HtHSLeuuh0EtZGFxI4gAGbKLC3S6zGJazEPdgEigIswtuiMVf0SFAkTrGOUwUhVuQHXn-SvB9hoIk05Yqg0QxxOdIg2JG5aMj2XQC5pdx5j7-rw1kZuFwEBisSlmBkQ306veF75IvJpdDn8ipRMouDwTNXDpBYig5xv482aFUScmB0M3wN0VomO5bt3uWjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=RMZ5QkhwEIULykwdqyK22JWAMVZs8eIVMJuwgpq6PjWlKl7QVhLpjyapMRwCAfLKEnSc2-m-oxC-dBxAzQq47BHfjXLRYNnhN1TioxcpF9E96Wsp6atJp4y1w93H6O1TmwkqbFbh5L_uxwmb6zMWaU-whjWkhxb0_zuNFxAJ6SanULM3LYLq2GpcvUvGUtm2Nog7JjznPk70cP0raPuCjtnGjtvZ8B1NFRuRBfxP74gYgAFj0t2O7cGotkIHXKk-n1v629sofNYnyTM3IL3gOJTPxNTmiqc6GTOyWqu-I6lAdgOMtNDc5cu_Hm38uiy3Gx7gnxkajizvOcUgWa7evQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=RMZ5QkhwEIULykwdqyK22JWAMVZs8eIVMJuwgpq6PjWlKl7QVhLpjyapMRwCAfLKEnSc2-m-oxC-dBxAzQq47BHfjXLRYNnhN1TioxcpF9E96Wsp6atJp4y1w93H6O1TmwkqbFbh5L_uxwmb6zMWaU-whjWkhxb0_zuNFxAJ6SanULM3LYLq2GpcvUvGUtm2Nog7JjznPk70cP0raPuCjtnGjtvZ8B1NFRuRBfxP74gYgAFj0t2O7cGotkIHXKk-n1v629sofNYnyTM3IL3gOJTPxNTmiqc6GTOyWqu-I6lAdgOMtNDc5cu_Hm38uiy3Gx7gnxkajizvOcUgWa7evQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRC4r0NKXI7I-pzuiF3mejxixNtLT-yo369EtRt1XriRyd9KSp2FYtTicaJeXLc_aMEvByrabTMmULvZBOu4RWLrNi5SkWX_gjwChhmOocbiYPw8yNSiwoJWXVtK9rZ2ngF_WRHO09CnuExZQbAj7wQKWdU2bRs64kdHatQPiaEu22LrQ8S2tJRrslz1SQRk2neqo_iWsvxfbkSC5iv0ogtt8BgFT5gwDPvpdzHh477XAEYKCR0mD-ZnfyIA4aV83FdfN93ymbNNugOvqjPrR7aH9hBM_o2XD880Q0RiBnEu6smq5qeQhbtJ6s8eGY4rapWWqNIyYZ90cmnFrUkANw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=VAT9iAJV3-GWbqEp-sgV4q6e1AqPGc4NpJBffJHregpcGBcDr8YkreJS2d79Eky8CJVz0QnQtItc8S708LhW92YTHLDNmWZYNgMrDsabhzLXBBrVY8AwzIQrrrSkZmArt-JuAZ0Bq9jlQCsA1Mlkx9tKAdc7bqmki3vFBXptSE5NFAPPy3DaZfLNCOZbZovbIhhSIbemPceMQiGzwDoKWnP_GNkDlnKShIojw4aKNOkzVhsg5W_oPZ1inSmvL_UlobSFdnBpSv35CjQSb8F-sweWlax3zeB0Pq8-m50V_5B1mYzcZGRWV4PNRDXMfM3s9dpJgC_tbyAAJomXXo8ulQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=VAT9iAJV3-GWbqEp-sgV4q6e1AqPGc4NpJBffJHregpcGBcDr8YkreJS2d79Eky8CJVz0QnQtItc8S708LhW92YTHLDNmWZYNgMrDsabhzLXBBrVY8AwzIQrrrSkZmArt-JuAZ0Bq9jlQCsA1Mlkx9tKAdc7bqmki3vFBXptSE5NFAPPy3DaZfLNCOZbZovbIhhSIbemPceMQiGzwDoKWnP_GNkDlnKShIojw4aKNOkzVhsg5W_oPZ1inSmvL_UlobSFdnBpSv35CjQSb8F-sweWlax3zeB0Pq8-m50V_5B1mYzcZGRWV4PNRDXMfM3s9dpJgC_tbyAAJomXXo8ulQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGKmo2V6g55dRofpqe4gvyqJ9rjE8RizVhsB42m2HP_rIkvU4c7fak8CH3jVlxSlZnYFHQGEGemxkGwH2oU86lGpUvK-iSLFy4LVxhqKvd3dt30yUJvZK2kMVtYQsW4n1SccDKZR9u1aVI9dkrkCvbc2EF5Z1hNOCB9Qn-0XDBadEi_z8NPZ1x4RFvhfOo2L8hwbKsQzR4vx100zD9Lxuo_o3UuC9KQ3LTZTXNF41cPU5ooc37we-H4Y7HGucpme_vp0bbY4YTmgdZbV98evzZ6hyTh0dbPSvPvqsY9C0YKWxCWI_RsAusZ8MnTPBr2o125ipubX0yhDzu79_o1kGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsLZUo0MFJX8M-LJtFvGFHwkpepmWMyqQj_QrME_hRBqVdQAu1ZiSQlGA9_0BSCbtpbcepJxq7Py1dmR92cGIsVycJy4bBLGph6NapgHDv7Byv0C_psaKUzK3urEKHfKDqz26nonca2wWhzMz23WZhIqA7eWwIt0SfKKmWJvfc0eHpcs7p1EOnv-uu67JehnXdUgHAufmGSkcXNNcubD0ddWe1CJcQCZIMf3c7dPLDiR-10_uhdV2BuzIs8PGl15y4Iur2MGrEoL-EZFxqyJZTyUoJKQKzQCZbOpNwGZvsT0oVNQXkVgLwJpH9MFRjEG_RlbUePPUcxvQUWX50iC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr1xkLfSDZoM_9rasq4rycvUPkkdEjpeldkJLRTWzv-n_heYZPo7gu5Zpuvd6O1eZVZ7J95bN8a2SHEeqJL_WcsYks2ZKb6NGgaQ_5wS1cUl8laEE6_cZJIxK4lx0jbCzvJsZLIEKAF8JRg1Jlk3okCjDPgdU_I1huK2dRcoVwgABn7AmN61YZV4QSrrgWI_Qs14R9hScS17l9NEIK1x5lrf_2D55xQU4rdCy_pNf8Wx8lJGzlFZHlSrKy5pI3G45AiA4lR0BEYJR-mXZbSGNovIQGIwRAAZmPAfZColBKJI_Vu31Aan3YIvgViJOy6k9FE57pPeau8rqjX8hZnorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPgE5LXnIfqX-uIaWG56-Ld6c1BDqvQVcinxmC2iDunKvAFtIVwQYjtRLi7MmovJw62EL2ekQFCJ0r1pB2ZbgcH5R8ubI-EcX2eSmlReKzjNGOay-MOIccNPWx-iP3IPZkP7vNDZQi5dRBBdwsVckYGvaG6CImlpBEl0DmkLMXPRoCcrbW1MQC7BVTKKlPQhGW1hH49oDNT1ei41IW2BdkUgbdGbltnSbsEiBf-ylmw0cKttY_zxJraHYmFTYUaR7khwcLdcDXFIvwLgxZTHDRNp09hV3lQNfZfyvsSmMWTJ6n0Xqzz9Ml6ZT2XQnkRxauXwpRU5WuG2RQeop4a0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dp24n6nPSjEFT2JUVSU2GGrU_VLj4RUjSJDDArjAtjPDVDBbx3aK0UikzknVtPu1zRHrViEYCTVIOHZVumjEheL7Z27c8btBfTieQONaTjfl-sP8AvlAcYUX4xDOrdfVL7kTruqbYHSHELbzJJYra2U59uGa_aY0MjSzvavAtfTsVYgqGfqr1H28lszDUWe0UmdiX_rG5nuY6GTY8FvwXyuXnLTzuccBFV49IpokGmS_xXH4TsM4gJL0a1n_vX39-JOddEi8jOAmFMt1cqinRdZiSv4Yt4-NvI1ApVYX7yU26kE_haSP7WFor8xX-OjINJyB-BMR02MSUlslUjnIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
