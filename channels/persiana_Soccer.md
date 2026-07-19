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
<img src="https://cdn4.telesco.pe/file/VodC7mPs4FrQXNI7816SdJh8oz1GJxa1vr6Qo63Hy4sSZ0Drh5plf5xmY9lEj6aY4UCtQLNcQzbxB99TAXB2qf2Wa1ra4Ka5NdmZi5S6dAwKE6OjMOiWkJgtyi7UHglsutJ2uc3YQZRLQbM4yD6hI63HLxwO1Afrrm5VVrhxh0LqRU9O7NY4_v03619P7ozwcAzfz01Az9MuhN_dZ5Q3BLgOEgxCoPYwdBY9XP4zztZDBLTL5dLe7NaGjg4H6t5sZSKnkQ6BsSYVUgOSv0hUZoPwVKE_6JlW7nICtdbQh-Eg6NocZEycvj09DYEJl0MYoHN-p_qHIro2Rf1FQ1hAnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 520K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 23:33:16</div>
<hr>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=ozcduTiBMS4Cxf9SEy6V1GtVcrNgGjwndbr6uSc2apOTaUnNSd2PxVRQKTuXgJbhWsyb7T4cV5Q7Qfine7dwutwNJ4Xn8pIPnw86XShb-b6q04lYl2KFVz8G4e4ewoQgtetlCvFT9jaGRdn-H7cYmOkhttZd72hIdsX8NvN_rjMb-dapcHZTVSIl5YGYooFIhL8SQLR3Wa52DkSWAAn2HcOFzkNxpjrYeAt3ub2TfdwRvfynhD_bXiZUS0bu3Zm26EnMbla_UVK-eImZVY7Bz8QIsD-3WY7STW_G8Gaxu3qeuzu-wuN4TmrHrHybNTBVZFDZRX19aD9SbkD7eCxCbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=ozcduTiBMS4Cxf9SEy6V1GtVcrNgGjwndbr6uSc2apOTaUnNSd2PxVRQKTuXgJbhWsyb7T4cV5Q7Qfine7dwutwNJ4Xn8pIPnw86XShb-b6q04lYl2KFVz8G4e4ewoQgtetlCvFT9jaGRdn-H7cYmOkhttZd72hIdsX8NvN_rjMb-dapcHZTVSIl5YGYooFIhL8SQLR3Wa52DkSWAAn2HcOFzkNxpjrYeAt3ub2TfdwRvfynhD_bXiZUS0bu3Zm26EnMbla_UVK-eImZVY7Bz8QIsD-3WY7STW_G8Gaxu3qeuzu-wuN4TmrHrHybNTBVZFDZRX19aD9SbkD7eCxCbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛
عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDDE6CiP9JTujxKJivbsLM7Zg8PA005yKapFfSloRGnBn7OW5r4qywsUas4tEtJE-18aCbSU2z5U6YBvyczP36XjN9NW8XSgFWBxxQmlbmnJGyJzxwcRih3SbKe_WU3B0dekbQqaQp5CS42rE15vWD7MCjQ-zm4Rap1cbUvJkYXF2JlccQqQ6t86MymqPaI7ooHSgVQfNAWlhLl40bX9n1JnJCCbf-tuEVv0De-b2vN3fB61qciyRsh_t-6AOlx0wOFkB3t_oGLPOGmaE97Fwd9LiESoVtWI4nEfMAu85b2AGX5awAawj8iyyk7qvM_pu82FB2NzavnTlc6ub-QTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVKZHTsvPcJbVSAOUZduvsX8-aqHqsC_zVggOQzcTofnJR5qoUeuZRYGL7UioeSsfQZkDTOAihXV3gTFzs8YicZxNliC9eIXoXk9crhKO0XRjRj0f09uP_myltklu41G3bQ0tzl-4s-L6qM4TCUayKWQEEVJNQJBX9W7z-BOHhZnQKFiNhM4K5M69YJoUC5oNVtB0CG1P6Rl8Q_j28MbU143YbvvcPyU4B0lw3U6n2Z1BpIyvLR5zpKFdSJdhGCLJzN-Qt6D0o8t63qY5pZwtN9OMYnNm9hNQ4XKPBFm5_mesbTzNOm8XLlp9VZdwV0yz1O-Efe69JOAKgvL0VN9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26089">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=puGFCwoxgcptT7vSd-HQffCyBqZYfjbczoyntti9WfufV41xhIzjfp6Q8QhKkcXNIbsHixDWdUCE0uRlERDf77GyzLsPVlbmADCA_Vkod6AFMxLEc-q4O3Crcg53K9Kwm2KK-klgntfnrxcRTPHiRfHJDb8mvaYfRsgBCZf7EyEtR27CAK8_j4GSszyz6s58QE_4lc3A-22w2c4jl-iH99VruXCq1MToEqpNa4DiAVrOq1eSigtkCcKZ9769c5JNCF3oI1fNBlukBsArsCInuBvQZzFMNwl4Zh54TJDZHStPbENAwUnY4LXzZsTjYK8mo5oSNM2dhU3NOyoQomaklw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=puGFCwoxgcptT7vSd-HQffCyBqZYfjbczoyntti9WfufV41xhIzjfp6Q8QhKkcXNIbsHixDWdUCE0uRlERDf77GyzLsPVlbmADCA_Vkod6AFMxLEc-q4O3Crcg53K9Kwm2KK-klgntfnrxcRTPHiRfHJDb8mvaYfRsgBCZf7EyEtR27CAK8_j4GSszyz6s58QE_4lc3A-22w2c4jl-iH99VruXCq1MToEqpNa4DiAVrOq1eSigtkCcKZ9769c5JNCF3oI1fNBlukBsArsCInuBvQZzFMNwl4Zh54TJDZHStPbENAwUnY4LXzZsTjYK8mo5oSNM2dhU3NOyoQomaklw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/26089" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26088">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVCuPFe0zPQgy8VRFbnrNX2lMrdIMQQ9OlcHE5yegvoCigNhED482OT3g6S62KtQZBQlnNJtAk3GXhs-GRrigmAsX76ovd1hSkCTg8OZ1o3Oq0GqpgjY_lh22Echict0NyF6QvBD77Sa8PJ6qRiKxRW3Aci2Q0cJ-4Z0lKmPl98snGlGBHkFvJ_GXieZaeSp9qCkvR0lNMQ3j1Thk_JUA2kl90eL_u53nEOzBlcTxlHCSBon9V0DzurNHK6iV1X_0mVV8dLNPzRzozrxWcTWuotTaDZV6dU4CxYVwhtrbr2FOI_lGWev19FLimAvEYqmh3Kcms9V6kqL9Ni0q5vUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/26088" target="_blank">📅 22:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26086">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68101d4663.mp4?token=TF1TUtCqoJMsPsvoONmayMNmfzF4A3OPHP03I8xuUqrW4eDXvktXWiOVtim-RWlQfS49i4LKqtrU3Z6bWakIw879Hs43RRRw3tZJB8-T8I_IspGRMoGkmkdhLM9WMAM3emKjYL3YjhmJ5kigdFLP-sw8W7EdK7E7jRT7ZMlpg81xg2k29fYB8Nt-RQ28zgJOc0snCIFo4Ng5XQ9bPTI-T2_cZ-AOmf3MmpJEt03ng6OYdLi6cxP_MfXohwQL_rPZxwGq-4DxD5L2TbHZgu3Ava2ZmzK0lA51003Igql8qtkKLYGao5dqiKB_IXov0yeSxq3Qn-zpLYeD7EG0eu86XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68101d4663.mp4?token=TF1TUtCqoJMsPsvoONmayMNmfzF4A3OPHP03I8xuUqrW4eDXvktXWiOVtim-RWlQfS49i4LKqtrU3Z6bWakIw879Hs43RRRw3tZJB8-T8I_IspGRMoGkmkdhLM9WMAM3emKjYL3YjhmJ5kigdFLP-sw8W7EdK7E7jRT7ZMlpg81xg2k29fYB8Nt-RQ28zgJOc0snCIFo4Ng5XQ9bPTI-T2_cZ-AOmf3MmpJEt03ng6OYdLi6cxP_MfXohwQL_rPZxwGq-4DxD5L2TbHZgu3Ava2ZmzK0lA51003Igql8qtkKLYGao5dqiKB_IXov0yeSxq3Qn-zpLYeD7EG0eu86XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل‌فردوسی‌پور: سعی کردم تیم ملی رو خیلی منصفانه نقد کنم امااین‌حرف‌که هر کی نقد کنه وطن فروشه نمیره تو کتم هر کاری میخواین بکنید. وقتی اینترنت بین الملل نیست من چجوری میتونم برنامه بسازم. عادل از اوردن اسم قلعه نویی خوداری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/26086" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26085">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df505731d.mp4?token=LQYCf03pAMARLl1Ay9gxKFTw-QO34qstMIjQCXqndHKxdLg5uWh-VEKy6TdSfo7oJf6pcOENjZ-s4C7Ftrsuo5P1Qrevsfs1271ZPQ4mA9p76Dkaphe4_d5WNBfc6O6DTjtTqao5_F9NuKUT6G2L8oYGZ2liHtyQkd1iGQiI_1i5Sayrycad7clfPdU8O-QIBtPx3tv1D-lfE9iiWPMPBxUQPh5FGp2u5AX74SsT5NzFlIDxH63sTQG8aqPmSpfNEZL_uSBEyJOMKU_TgBPRQQ_nZQVjLGbAjM-AlLgbKmh8iknDMaEmyp_FA39cCArL6AeqraqNjM7ymocWKW-X_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df505731d.mp4?token=LQYCf03pAMARLl1Ay9gxKFTw-QO34qstMIjQCXqndHKxdLg5uWh-VEKy6TdSfo7oJf6pcOENjZ-s4C7Ftrsuo5P1Qrevsfs1271ZPQ4mA9p76Dkaphe4_d5WNBfc6O6DTjtTqao5_F9NuKUT6G2L8oYGZ2liHtyQkd1iGQiI_1i5Sayrycad7clfPdU8O-QIBtPx3tv1D-lfE9iiWPMPBxUQPh5FGp2u5AX74SsT5NzFlIDxH63sTQG8aqPmSpfNEZL_uSBEyJOMKU_TgBPRQQ_nZQVjLGbAjM-AlLgbKmh8iknDMaEmyp_FA39cCArL6AeqraqNjM7ymocWKW-X_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی تو این دو ویدیو به بد ترین شکل ممکن‌جواب‌صحبت‌های‌قلعه‌نویی رو داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/26085" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDGoEOhUoJSpSME0D2rdedMVqW87dMz7QwoFdsNUMY2U56RXVwkJMnXupD4dD1FvNx7RSGhqAVUzegooSl6r9FBW7p6H3UDR5cxbfsAndEelwvJPmSZxsD29NRqJvCh_QDOz2QhwMfR3LfN1kvnM8uc6iQ4b0N-vrzPZdzkPLXdoy9mvkFDLtxnDcjcFar3kwmynMTGTmQETBhOyTr8USH_MOunqwNTDSZsihooMkSTlGBNQClj7tFR2tG13zYE-h8UiLIUODi2Jw32ctYAbVh_KMLrD5B6PgDsCGGBStXm_NgHi6lkS5N1JczqSD4Aa1KsHP1LQMJNc31W5SAslYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=aYhi3Jr4-Ih6txcTRNPnMyv5koIprarESbuZ1ARiFaJjCLWwIw5zf8kjnFK_b37zZ2VgXASWt1UbXGaY2LetXdTZeboI6xM2za1IkmLSAm1cNA_LuYJtnvgYP9r0bhUHtGjkvhQJLHGPXXKjjHIOVFcWyVvuTl3x_4vcGluM6Tm80f1lIAN_LZM4k7gxBG__tWhQEP0F3Ebis0LSW0lvmctIFnSnWvV5RpFCt4p1hzOZC1LtrwJ8Hp919y06mbWw2M3jSPk-wi-H7LaQP8s8_410Aco4tyOwn3tWL7TxHgI4-WQ-KvprYeNr_7n-AF2Ps7n6sVadMpNgaJ-pRCtM6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=aYhi3Jr4-Ih6txcTRNPnMyv5koIprarESbuZ1ARiFaJjCLWwIw5zf8kjnFK_b37zZ2VgXASWt1UbXGaY2LetXdTZeboI6xM2za1IkmLSAm1cNA_LuYJtnvgYP9r0bhUHtGjkvhQJLHGPXXKjjHIOVFcWyVvuTl3x_4vcGluM6Tm80f1lIAN_LZM4k7gxBG__tWhQEP0F3Ebis0LSW0lvmctIFnSnWvV5RpFCt4p1hzOZC1LtrwJ8Hp919y06mbWw2M3jSPk-wi-H7LaQP8s8_410Aco4tyOwn3tWL7TxHgI4-WQ-KvprYeNr_7n-AF2Ps7n6sVadMpNgaJ-pRCtM6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQxExJs_l7fvykYjTNCGkFga7I-p5HeXWPA7XTgmVy_Loq3z6EkZ6SbDrIWaNpH_20KVz9xEZPqB7xVsfkmX7xPY5wRrjmXW3YggkhRS86mYIHF5CnkoeDmCf4C3cnk7DWly78e1UdM75zoLMJ_1dsYDCRh0ipXYn1CsiwfDa8t67qFfyHeQyDMc-UI4pzxxLorYfV8CBrkN1rCpxUOuH0EiQaE72331jrdfw1UjZelzew3La-zIwfRzmnFzAm2r6gIRRYpXVE3GUCP-He_6gMouzqKYSE51A3VODMWND5aNH5e9d3Oq9IO48UyCIAiPits5OukNQ4pdjTHEsvienw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjmVbf8daZaPvG53aAWDKG4SjApJTHYBkcRlJKxno9iw5YcpS-RyscHTDyUuOzhENeN1VIB4lGc5vYPdW0QeTyitlBAPEBvZ0g2xwdd9mHF8WrKHHJkYl-d8Ax-Xc1rPCGw4J78mmaXCAdT6ilDuy1eNnD093oNZgwyp-hnbNT_yDxKSe0me1FU1gaUR0H0xQxT1cpDWdQ058iUtFT6be4qv4v-2tnJYOJ5ceZCxk7_5W_8KT8Pf6TWlFUtsfJVEPFkpopYRXtIZe-EPPKzA_w5YmNng6LkItWOQPbFYcf5heO9E1O3KAzqQT6478SV3ve_fFwAjTWcZuUj98jScWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnNForisJUhOT97zrMCx6oG6s2PkkmV6yWW0Y-7Klo7_boEoJbY1g3KmiYnAUzlw4X0qfWcb2V_zsBVi_Ec44921A0i-ak5sdp0jJy1NN2lhXq3mJPc2z382O9GEHtZY8tk3eAnSDFfGU5s7Z_NPiaqQDAWqSL0w5lsU7D_CJXfhyUl_8eW2-pdyRPk2wBJNnPXjykJvNf7fEdIusw-kUj2LXAVHQEj0JuF9HRRR_C_hhegtOf0CYPGJf8_Jc0IThQ7whjUGhieJvMV-LfwZsQFowsc18wxJhdhfBfe3uIIy3Tx5oORL_wC2PT6gMKj9hZaHxImiz-IysKU1LkLk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gG_CfQZZdGhQRrRAko_KQhxGfnz5T8hj3lRWy0gtcpTAEKaKSJPaZUEd9PPVtZ3BUVqbDGioA39QoSoZZ5_nrTR_4U_llnYOuHGz-c13YCVTxMXPy4wa2nEfadqUWnJLnbRJ6_l3ntg58kzCy-zihC-Ga3MJcrbm1EUWBktxz1oVMUdS92TpVhI461aQrX4nRIXfF8r1yJQg9zIL_5lYbKwouB7WwzZ3R0PBuTeZh26JPvxJH6ooqf31BztRckzgr1ff-nLtmHTCHI1icz2SfPFTv5cxIYljtXG4jCQOu8VF5ko514Yebp9iwjrN22HBblxutIgDS85DQYdT0c_3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_QZM0YhUjDdVkpJWBLJNO_3VDNpfQtN-fAHdGvpF2QgIMYfeK9Kw_qs5DK7QuLFdc_fgaSz-0jD0lVKGhZfhG7PHk26qh1tbzDUTub2bqY_1-Wm0g4s7SzlqPXGIz46ML3SHKcfPTVWXYAqSdZelNmNd8cU9GCOK9m8mqPBsYKux1ZDn5WI3AWtWHd8EcR9PrsrbmS8M3FqFLIV9NzWg5VB2NQDNfFerA9sIe8GU3RT2trDzMpOWNsPv98ZMxYXeuFcwtFeskL-XkqWMBN9Y5IwDYMR1qn41JZ2JsDqOdxe7OgO1qgYHv_Usn-V5u4h9JGAeHW8LR_kWmUHKEgzWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26075">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMVZdFKdARi07w1A9uHepQRT-JjXq_HwJXYajhSbWRv8xkHii8Pdwfngj9unaUzx7aqah5OpgHo4rXCpBaL7-uA3-S-sV9lig1cMw_BhvXQgraTU2Mu0QXsx2w5gTDsTXgmnWjZwtENis0NSMjpR18Vc1gaNV13N15WfM3_GNpUDzoMULcV8EfkIoev0i2JMAhPzEBmLVn79mQhuLeC9_om26C54ACVKNdCK3DaVYYyAtWjsPzkk4aR1F_K1JByxGslnG70Ye6C3V6822dDyRz5atdK5pRrJDu-1weghGX3792Vjx-AHCqlBxJ40JyUQAQG8GMP4fx-gVy__qVB51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/26075" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26074">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlhteimBIhnON3duFv-NsFXpAwlgOHUBmpIPGCmgB8Y9qDRcZI9Ycg067BPUEzcO2T7fciJ_J2dodyHZB8rX8kJYLXKBIWsLP4KS-A4yKvN72fppMDWmss5hybI6RbOx7FZblHNZsFHX1oagkLDiN8CkZx29d8UWwkxb5zXOrQUOQNZLdYMtX0VUfpsqN0Vl_viU1vAMps6TOtvavVrbQVLUGQWnDkGXyjZ4htcwjGVHNHQ6RFRcvynm4CUhCliQVFGYbVXr-UZnXa5Ek9VLO2QDE1a02oNd3dwTQHxy6TEenf0h_YaK-M44MxyaD9Q2U-eN6brIr11m5ttu8fjguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
علی دایی بهترین میانگین گل ملی در مقایسه با کریس‌رونالدو و لیونل‌مسی دو اسطوره فوتبال دنیا؛ بعضی رکوردها شکسته میشوند، اما بعضی از نام‌ها برای همیشه در تاریخ بشر به نیکی می‌مانند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/26074" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26073">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFlit5GmicNI0LXSf1MNSG79SETdHdzF-vqtz1JbO-tDliuN8QshNi62FE4o_iImbdaJf2dbqcTqv1e-ckFGS4rhlGV01N_TKgD9tLJ9ZaECRsDA2F4HObCuPQQ0oKYMWVuk0G0uBwl1MDbLqRkDFc1GCGNJpOiBoAMt-L6pEH3Higec08IfaYxNW_2VdN2iyUTIDC0U53ypWVE1Km6Mt4Adje_fcQa43iKzCtJMrYzXp2dbWgwRKtWS7s8y8kcxuo3UsfLZ3PxQ7CAIMeU03Pqo-VojBvm3zU89k1JzvooFKK7J0O-wgzbz9mJaWNHvR88HKq1cbPc7uSHGpgsGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین
🆚
🇪🇸
اسپانیا
📅
یکشنبه ۲۸ تیر ۱۴۰۵
🕥
ساعت ۲۲:۳۰
🎁
۷۰۰ دلار جایزه
به صورت
FreeBet
بین برندگان واجد شرایط تقسیم می‌شود.
📶
علاوه بر آن،
۱ گیگ اینترنت یک‌ماهه
نیز به برندگان واجد شرایط تعلق می‌گیرد.
✨
همین حالا پیش‌بینی خودت را ثبت کن و شانس خودت را برای کسب جایزه امتحان کن
https://t.me/betegram_bot?start=p10_r4EF37DCE</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/26073" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26072">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIJ_A7nIS7z_iyNiiGfV-zEPYijwYD9G0jImazrNbHLzPclkc0yGaHfoKZ3meiqhwCAT7csg0KloGXZT4wn0ISjzP_FPdW1aN4qkNFa4H6i3JgEh7mrYRwgDRg9IAGPrbK4k-9LMd1UQQPHE83AnyqOM6Ey65TNXW8NAhtksWY5NWmV1HgKPKGJeKgNdRvkGUukAR5-3_9HjzTAc7Hn0b9PQg2-Xfg8i411kvkc2WKZMOEm1UZfI4NolWchJAXDnu49Z3UO-QBUC43EgiH0ngQg4LRbF2z1tTUwd-vgAAmk9jNfaJWc78RjeHA28VH0OFYpSB-sgOrYuYdb_xvDJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:
عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26072" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26071">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCiShKAuVHvPnloWd7Qbc8XTLgt5qONMWoX_az4N44VTXOe4N5Y4el3OUf5kcSmE_w9BEMQ0-t8tcsDjj-7kVUiFU0mJ-aH_F29xnqYUlw4cjIcpFS3TqNqCJKjGMdnMM-X8Nk7-Z7t7HO37FOXt9k4dl4wAVGOQV96CS-fMhMq5LQBSTUP96hsSix7eu-iN8abErO4Zy1mhHzDkLcLt_qdgbkwfZuoX8p9PvNbXUk8jXyrkj4Q8ek6l_cIy6rt2naXlWPBE26LO8l9kCvIAW5U5mLh4HeT76IjaD3XSI9FaBotKv_nDIRgoESl4Q7vkzVH5RR6Zxa71U3S4VNws4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/26071" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26069">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=XjgLeiBNg7QMFDZijG84OWZL_pyVR7F3JfVnykLM2K4fuDGPLL4QmCWHeBrygQDxwrscHxd2TnJtzkZfawZp8xN3iX9iBoeH6JXG2GVsKJEEUgR3TTMlMqVYyuUHhjCQdUSUGsx-CLudsWY8xjm-FEobckUr8TrvGJDs8So9tXSwLloye5xbFDEfc7lmJxL-ilB2_OhmyqzxT9EhiuY-QjwC_UEYjrjJ0MxBAPfx-BPnl60l8HysmNkZYWAmiaqw7uKDQCbfEA9GAyqp8YO85DyDj6nW8eNdFj3NA61-8D1oOwkMROJZgHjku_aAc2sQLVzssKT4wPWX1Xjr0HkDFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=XjgLeiBNg7QMFDZijG84OWZL_pyVR7F3JfVnykLM2K4fuDGPLL4QmCWHeBrygQDxwrscHxd2TnJtzkZfawZp8xN3iX9iBoeH6JXG2GVsKJEEUgR3TTMlMqVYyuUHhjCQdUSUGsx-CLudsWY8xjm-FEobckUr8TrvGJDs8So9tXSwLloye5xbFDEfc7lmJxL-ilB2_OhmyqzxT9EhiuY-QjwC_UEYjrjJ0MxBAPfx-BPnl60l8HysmNkZYWAmiaqw7uKDQCbfEA9GAyqp8YO85DyDj6nW8eNdFj3NA61-8D1oOwkMROJZgHjku_aAc2sQLVzssKT4wPWX1Xjr0HkDFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/26069" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26068">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvyaANO9l_YlD7ax2Xol4fBvh-Kf78kxKZHI72c_bMjAERmCBroH9CoHvF5cBH2ns21TbpaF2dBEUnkgOuOPB_TxPyOzkLdXPu6FQcaEpX7w49i23jMST9B4F-Nexh2WHytgBsfF0awy8HQR2EtNVDLaD4imzcS0LoIHSLv3DyCth2ELQvIpjBBwQFMfrxfkR5HOEJcmiJicALh0QDgGpBDnEx7fKswXkbzvjpW82HjiDS3nVu4Tj6v4rXkARfZbJrkAQ7gFDICw4bWQGnd5yDeDO6BgOD2wnJpILV2Vdp0EqxqVnOyHT1u-E10Y9TvZNDCwkjxwH4FHH82Sufoo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در دو جام جهانی گذشته؛ تیمی که در مرحله حذفی با نتیجه ۲ - ۱ انگلیسی‌ها رو شکست داده در نهایت درفینال‌باخته. این اتفاق برای کرواسی ۲۰۱۸ و فرانسه (۲۰۲۲) افتاد. در این جام جهانی، آرژانتین در نیمه‌نهایی انگلیس رو با نتیجه ۲-۱ شکست داد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/26068" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26067">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsydjyRrEn_yIAZJvAmvneztY4liKv2cwALTg60oOQyk_Gv0yF8bz69Ic5a598WfTGjbAi45c3LREKPyEjvPt3kSP9gZnxYv1JqNvI2_mQAkNG5lrkcahBzn34qkmmemRkJjYXhZ72JwD7H5vPGNgY00uifNk9hiEacxmZnD8unAN4dxre4GGUfoqfA0xiBGMnmfa1A_HCnS3u0SDfXBFWfIDkoz2O0mJvI3msydd9HcoZaAOJZZG0BGQ0kZJVjvCyDBQGLh4Oz1tvdij-qdIW7S0bv5-SbrKMwsBtXmtUDaHQv8fCi_-7sAG0LzYk7nE7uHlnu9CPlMpjfJFFYipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26067" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26066">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7G54lNvPKACe2_uTWnLtGKcst4NW1eKPhSnSKrzf0S9ZoVES61_pDVcfxtlGPXlUJRruwUx78o1168sO0OACkzoSwKcczgv5TF31f7kGfm3kmu7tGlwzQgYCVFmmhQ7-U7i8f523tXXHtA10N-G-mVRXvmXdh_DMB3pSNGptKS3p2QKnqP6EYJ4qS9rr5ZOXPVwOK5ca1LkC8FT_XKrAbLxF8qkS_9SftvpFIW13umhNx7mIHCpwUJNmo7SZxpT8PMHEqHzUPgzplT1kUZlHNh509cUH3w3ignVbUOevxW_oUEBZeqwcgnamlPf4RqbguYVETKoQdbmbAsNwRzZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
طبق‌شنیده‌های‌پرشیانا؛ مهدی‌تارتار سرمربی تیم پرسپولیس از وضعیت فنی سیدابوالفضل جلالی مدافع‌چپ‌جدیدسرخ‌ها راضی نیست و به او گفته اگه عملکرد فنی‌اش بهتر نشود مجبور به فسخ قراردادش خواهند شد. تارتار نیم نگاهی به جذب مدافع چپ نیز داره. جلالی سه‌فصل قبل آقای…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/26066" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26065">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=lT0YDGn_xlfO1OZ36EUffmxWyZrlKpomz0m_Uk_sodQURdsShFfEhyGeQ42SX3j6d9QFdCW0MwOPknPQMBCwfoONKJ_jqZSSc046cZ8HmKWbFxFuBn5DeQ6lQEx0Y01M1_I4gYrioDfHHPGL3TSwPjxVN1KT5X7pbbmAWX5jpNBRcJPj_n9ZUFLfxHEPqAK9dPMX8tVL6Nl_z3z2DXzuMRiHUPt7s60l5ltCzHiOPGpJl2Hd-TLP8ZMM9tEFludgxWV7QWO9mCHjYF_R-5c6RSPy33NhkXXVjH9lOLrnnXY4pq9Ad_iY7ui4yCNdi4crSu6C18VPE2DXaokuQ0ai5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=lT0YDGn_xlfO1OZ36EUffmxWyZrlKpomz0m_Uk_sodQURdsShFfEhyGeQ42SX3j6d9QFdCW0MwOPknPQMBCwfoONKJ_jqZSSc046cZ8HmKWbFxFuBn5DeQ6lQEx0Y01M1_I4gYrioDfHHPGL3TSwPjxVN1KT5X7pbbmAWX5jpNBRcJPj_n9ZUFLfxHEPqAK9dPMX8tVL6Nl_z3z2DXzuMRiHUPt7s60l5ltCzHiOPGpJl2Hd-TLP8ZMM9tEFludgxWV7QWO9mCHjYF_R-5c6RSPy33NhkXXVjH9lOLrnnXY4pq9Ad_iY7ui4yCNdi4crSu6C18VPE2DXaokuQ0ai5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/26065" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26064">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saNzXnbGmNQ1_FYjqjtJ0BqrujAO9h0E9P6obtW7Tuxmr9Y_93oJBqjBYIZqi5NYs4hukGzCVXDG7xyYXpBfJRvABknDaazsm7_FIdTc0vee6NMhPIZecGHC_Zhv_hZaGBb_wn-801WYfujSWoyn_JJ2gKRLtUSogXra0iPWbM5cJIifrIhJO1NYw4rnEty8m9FkBcHVCgVAP9tcnZuGZglsNCI7Ja_riVYR1UxxVDIkUISTpxzMLVD9CwBKxw8z-AxG6DX8r_ksKkAtLg9Qwb8g3qNDKTei-VnsKSmWLY8C0Iksx0RMb0bsXuiQkahdw3KJXKIDNyogcbHF6cIltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26064" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26063">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=GgYX328VjNcyNHlso10Jrh2K5p_vNcqLHr9rQZkM2KpvKx1taGF8xouLHa7Q1vY3fU4urfL4inDhXdniVkO98EQysSmQzumvHf469RdwEmtJmVzFMB_yLf2ReeuuaQrj-q598mxyGcuj5wUtWzMUGND2qa1COA-HAtnlzCU8OiW_fj9bJD7Ra8VELIeHx0DvR3hPL64GNlqojdhG9UC_89xEMoMIGO-NtR3BL2h7jQJw0ER9QHDMoSVlBHNU9a0G3qCJ_Ano6P3MwbvT90Xex0KoELueO1q_J9ZCzltDIVWMkEZcraxvhd2gDzmR9YR7a25Ldt3yudIV12gjzJ833Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=GgYX328VjNcyNHlso10Jrh2K5p_vNcqLHr9rQZkM2KpvKx1taGF8xouLHa7Q1vY3fU4urfL4inDhXdniVkO98EQysSmQzumvHf469RdwEmtJmVzFMB_yLf2ReeuuaQrj-q598mxyGcuj5wUtWzMUGND2qa1COA-HAtnlzCU8OiW_fj9bJD7Ra8VELIeHx0DvR3hPL64GNlqojdhG9UC_89xEMoMIGO-NtR3BL2h7jQJw0ER9QHDMoSVlBHNU9a0G3qCJ_Ano6P3MwbvT90Xex0KoELueO1q_J9ZCzltDIVWMkEZcraxvhd2gDzmR9YR7a25Ldt3yudIV12gjzJ833Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه دنیای فوتبال را رقم زده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26063" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26062">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbXs2GOh2ibErFv4_YS6Gykk5srqRZ9JMbdhVh-0Oh6l84R5Z3n-F7R2hfsUhsNnd418scIaSAAt4JWZZq4am2V13-ygX-fzBnF6XauTlPbcyEyCXRHcFf60vOJRjeYYP_YuKwETVfHovpXEPeLYswuoG0nUX9iDBvPLJpsF6CFsCJBcFAhLYuBijzQykF3rlisXBKxHxUogMA9w3UoyMyZlePgfcnKXTkZ6O-_dz8dL7rMHpJmD99Ar7zLP5sI5VDlkZ19niet1AWjX-jsYB378gQ7lwd0hDGAsc7bTBt3XfOSToathMAayzY8m56wczDD3eNc6sygu1EeDmY8lqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026
؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26062" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26061">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBPVkw31S_J18a8Caj4jal6VRc_krjCjDby2HLeQHiUgY16RvBdwM8iSmY_Gg2farZ3KH6irP69mbQOmcFs3pauzkrfUmr9oPpL_VRCa7RrlblJdYtsUwUkbx8CcbxNWirWrSpob-1SB7NrCr-ev7KqCx3d4mbUdHI4Y_2bcOnZo93hcIOfHAzKrSG0JKe1anfuL9T409a5QBcZhiX8xAT7VcHAHSw2JDOJXEWV35iCU-1vbMXXGnGUud3hH7jRW--2fI8kx_F7FgSgqjoxeni67AfabhWXhJwhxOLDxVrp5Cea9f-qk3IZSV82cnxyP_CnwblHX-CEoOTq3W1TzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق‌ اخبار دریافتی رسانه پرشیانا؛
به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26061" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26060">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVad5Z_WeYnMQaLn4zvEE13xYJt8pFaTUBOPQw6CEIMSfK9PArRyYjGdCjISHAou9lfF7HlVXfpubt6xxaRljMUbrVUC12CcXfFDkhQ2zNxoo-jO95ZCCXL7b-TFo9O_dkB3O4c--n_qZXCQFji1-FBj19sWC4wGjkT9PkKqB17AQXrYB4CAGYvp7Fvls7PEHL7E3ZxC1pMYgiDt4KrR3AWIhi0Z6wqyv6ew61p5HzqTsZDIx5XzTvsBS7F0L8Y54vFteWRcS6_7MfX0NpY1yiRWhdTzHNqzqo_BnwjnV_kgGSLrdRQUfbQoFTd9uF0SXg-ZeKcYzPdAwoSmXI1ujg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26060" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26059">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=KsnVmmlDN7pefmXoO_DZUOIclmRKzIm0MvJMh9O4Wb-kRx9Co8o6ZFL_hpRV5fbb3DWRBVEh9In1PkwlMJh2TxJfIj0tzi8lckNV9ivTcQssYnBNpvfr1HBJBg5J1J2haPkNw-yBh_KLWOgKSHywi7qbIuKhI_utfAjbHzIi9VMuAEreKBxtC6jDZiXWWSLcuX3hD7T6FtdljYh8DVnLJ6X8npTfRcTU3w54zMpRFQwXMM6-bfy_2w9nygX5GdvCpdl2Gvi9Oz-3GJHTYHRnOnpS0dxOYbK23ZeAm68VJbneQGm0fYFACpgagHzhLNn5Jx99wpBUaF8HFL9tn96BVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=KsnVmmlDN7pefmXoO_DZUOIclmRKzIm0MvJMh9O4Wb-kRx9Co8o6ZFL_hpRV5fbb3DWRBVEh9In1PkwlMJh2TxJfIj0tzi8lckNV9ivTcQssYnBNpvfr1HBJBg5J1J2haPkNw-yBh_KLWOgKSHywi7qbIuKhI_utfAjbHzIi9VMuAEreKBxtC6jDZiXWWSLcuX3hD7T6FtdljYh8DVnLJ6X8npTfRcTU3w54zMpRFQwXMM6-bfy_2w9nygX5GdvCpdl2Gvi9Oz-3GJHTYHRnOnpS0dxOYbK23ZeAm68VJbneQGm0fYFACpgagHzhLNn5Jx99wpBUaF8HFL9tn96BVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26059" target="_blank">📅 15:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26058">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsg4vBLwJ5e6BSn_QnbOQVUXyyvFSzsuEde9fMWhVvishV0AE7fSUpY0NGBBLH__uXVfKDSvQJ5rnYoQlZk-w0r2euyFNucx4fqdQ4l3hlvbpHnyOP05yG9cOvYOtI4u5F8JAFWvOeTRAXL8A1iSDE9zSJF43riJaAhRYO0WlQ3VRdH9irULGin_teD9SofD47iQWPiT9dtdhK6QAGiZ4jZRijEsc7vA-lS7qCLG4xOJEBiwV_yuL-WCKgBSNTs9DA45kIsjBcaOTyEx2AlRMsNuMGOope6xCE6KXPLuici7QpN1ynQyjEdFmuaXI6UYnCeHS7nx0XVBfzXMu_NuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26058" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26057">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ99USyvGhOYA53cANt1qJDNkOFRmNL2Ot-xEQiFVlnzuUXeSZvH5MJlOwU2-zTZFvUgldlznWJ2nbMldCizAzvuOuucaLVe8RBc5KmOOHi34jdK1vXKiWu27pdLeQ-LLeN6lEp2irA6IMQZ4utzqT7DvV8G1jXMTaM8pWbTGLbjs8eV_-NbeE7KP-wKwGac0aZC2eDXiSKyDgQBKPsyjrwWEVdqpUMNlQw0uDNEUlKPa1w_r3oThUmsxFtShR2qX06WynxsHSS9He8ubtPitcjAutPtE7hDiByeEzTYwupH7jUVcxJrN9Fz3dXU_0Kui0KMwK7Nf6z7lIFU8Tf3fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26057" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26056">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=BqRGnoqGZSi6Ie1mqy_t5dp3BV2HfaYlDo8vg9pNzGKEFTrKsUq2Cw2ppXYXXMxx6u2_2qGFK6uMSZwiyKFSDRJPholbc_V4J0IS7n5tLzJuvz3TS04F6d40d7K8hsLXATb7ldM5e6Ow0m_FOZlgNjg7gKzL7nNO1VOMHmLkfqfbAY8ENNxGSOe4OeCKk4bvFN9R4yzHrIIJvW1nyMxD17SpMmw-fmQU1nMp-TDw1ub30C-uKP7bp1ZnVFoPs-GgNojAWhyGvgZ6xlxiNCL6xjrEqUftsrpUWV9cHKhJLvdhuC--i0aeAoHvaQhsKrWnNwfLAbOXcHG5f2or8odcrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=BqRGnoqGZSi6Ie1mqy_t5dp3BV2HfaYlDo8vg9pNzGKEFTrKsUq2Cw2ppXYXXMxx6u2_2qGFK6uMSZwiyKFSDRJPholbc_V4J0IS7n5tLzJuvz3TS04F6d40d7K8hsLXATb7ldM5e6Ow0m_FOZlgNjg7gKzL7nNO1VOMHmLkfqfbAY8ENNxGSOe4OeCKk4bvFN9R4yzHrIIJvW1nyMxD17SpMmw-fmQU1nMp-TDw1ub30C-uKP7bp1ZnVFoPs-GgNojAWhyGvgZ6xlxiNCL6xjrEqUftsrpUWV9cHKhJLvdhuC--i0aeAoHvaQhsKrWnNwfLAbOXcHG5f2or8odcrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
از تاثیرات جام جهانی فوتبال بر والیبالیست ها در لیگ‌ملت‌ها؛ دریافت‌جالب بازیکن‌تیم‌ملی آرژانیتن با پا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26056" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26055">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=RVC7KAltG8p05jvopIuBwXUZAUfMqxPGbnhgfQw8UTiTwkZ_bKsJ4BW_F5mOcqUFy0LvO2mmaeu1_xNqX3LBP6hrOoW1X2yyf71gjveVOSVPWSE37P8K7D-MP5J5DabeBBToDJeWoee0gBgweYHOeMj_FXVloBNNKrMx8zJhpQzlAelJgklmfK3qpN_Gm5dOqzP-fVHzypv06_yfa9r9pR6_cD4FqFPJ6wIh6-VtnPvughDdyQDYsUHpdEemsUxoeGrepUKXVToZ6kLkwG58Z_QQMAnz1LJ_JWC4Fgw5Sr1XvhkTSA9fwJuOx2_bqLYP4V0tsYOtzcyfJWCImeQFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=RVC7KAltG8p05jvopIuBwXUZAUfMqxPGbnhgfQw8UTiTwkZ_bKsJ4BW_F5mOcqUFy0LvO2mmaeu1_xNqX3LBP6hrOoW1X2yyf71gjveVOSVPWSE37P8K7D-MP5J5DabeBBToDJeWoee0gBgweYHOeMj_FXVloBNNKrMx8zJhpQzlAelJgklmfK3qpN_Gm5dOqzP-fVHzypv06_yfa9r9pR6_cD4FqFPJ6wIh6-VtnPvughDdyQDYsUHpdEemsUxoeGrepUKXVToZ6kLkwG58Z_QQMAnz1LJ_JWC4Fgw5Sr1XvhkTSA9fwJuOx2_bqLYP4V0tsYOtzcyfJWCImeQFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پله همیشه می‌گفت زیباترین گل زندگیش رو در ۲ اوت ۱۹۵۹ مقابل تیم‌یوونتوس زده! اما از اون مسابقه هیچ گونه فیلمی وجود نداشت. حالا گوگل با همکاری خانواده پله و با استفاده از Google DeepMind، فیلم این گل رو ساخته. این ویدئو، فیلم واقعی اون گل‌نیست؛ بلکه‌بازسازی‌مبتنی برAI و اسناد تاریخیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26055" target="_blank">📅 14:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26054">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKJxFdbnyJ6dupTscX09lgsmAFZEkA1_uD-_Z9x9jjQEdC7b_kZmSYz4eH4-3e7mcdxsfuBAeQKEzzxtk0SwULlZVOpX0K82IPwlrL1hkCZn45CaKp0Iofb12-xdLUjKGekom3KVSlI90c9DK065Mzcqxn6ze2ecE-Wctg4SFmV-9kMEJBFkzvxFbYbmqkpMajhoVfcWQNBAhErB011nRHzPcjP2uQP7H6VT_IW8C-D9-XDHf_xvOOS5029jawh7nsxvcrC82h7iITZ0Nw0n9b1fzqgMljt1H-DIS4-_d9dS5-ccAFDN-rEeWCAoBZfWThgSig0HiMDBTpKWh1elfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26054" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26053">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKSvU9_f7j-XSaEso_a6Lw2QIu1ksAm4AIIc3E13AEQ3QUWMA7sIavj_NvwYZPm9AnwlZ5yavOhjrL3FEVoacRCtGnnb6Ib-ikXzlP-EIOeXCnhpVn__fcgFWfU8pqBWskiembmExN4V98a4zm9nqvbcZwQCpqURgeWbPsuYCWtc_H_0suLIhCHPcCcdlRa3TcDAnaiv-aW6blESvKU6Usw6InwNSL0Koeoiy2mVz7T94xJOV8k-kND1LwU32Vd7ZZvlhVZQxx-nqSTR0xwu-yuChx-YvmHP_tlQlGMuQOL5eiA7T4xNbMvq7lnOMpfpEqHAn6yw0DrIB_4S4DUDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26053" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26052">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vq38ZDOVgkN3f8VwVkE8rOZX01pajxaN53NJ0tNwkwY3EMKu7eQPpSXQDNyMfHLCc8PtFK2WeiJhMBJMh5LrsjwhwMRtCJDGEimyQTqamNTGVvf7XLuQoAHw4yKjuGxhIveAg_i3qUwsQmBvmfznKc74f38iKyoeQwZT60X5YjEZZk6IFtJAhYrYEXIBSRX9_nLfVlicL-QLvaJnXQYWaZ641K2MIXa4s4kOWfrc3LyN8CUhEImRkJPG_z1VAyjrXtR3OaujuyGxsShCjCCQovQPrO1JomNyT3HhVOGJXzGzY8JOYEhL1zZlXgqnYTn8y0ivadxnYVYedwhuUCdknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26052" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26051">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpNbmGRMPp9tbNVKh8MpMqJqKs0Rk1VE30SaHFIx_FqjpCrVQ_rYbI-gZG3WOjqKff7CUYKuxRSCRZ3-D9TyimMzULDBPVsPApxhRjFLxNt7a0yC1dMgMfiUqCq7PcqiVkuTaUiJ6ZF1EhAH4TcNmoVOkFUjT8LwVMHVIE1jetLemMuyGt9u2okDkU3WQN6qZaHp6vb77foKD_HUp99cu6mU8bus8MYQsr8ReXG5GKXMFlrWs3w2xUTso3-MAax3XybtTxmoYGv6O4w7fV7JnRYRpKdARpveL2X5_IEvBRI2SQuWdXJ3qu1_qYqf30049eg_VqiiVhMJ4dv5kTfDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26051" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26050">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwB29TmiLX5uvyVLK-QwKSpLlNdnaBbu1VI8I4HTI7zUCu8yw8w5Vqm3nyLzuibja99by4ZyUcaXDevhyEqPqfiMOIF5YGd5Sl8_BT0Dnn65qEZH6nToOmvX7mji0qFEFPDe7FwjyBkqmrltJXR86e5Dr2RGdVW0c2un7i-CHUbseXhIm6AZ4qET5MBx8yb4-ET9wT-P0M_EuUDys98bRQJ1xY8UizMacj6mfQ40Pbda2ghd6BXdhgZdwtJGcjiRUkS5FBW2ZZHaBmS4otttZUZpPdL9jiYoqzAC5Ev-SDkqqwosWZkMpv4WLaWs6JeMR4WtXjhZbR3NrWSoeuQHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26050" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26049">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2h1Tzb1kgSK72MLoVWFIpLMQ81uPwLRWsyx7lCUu3ka2urr8WCmoOH8dWVtlFFSTcyUdriwisLZT5wxY5Dyo1smPPteUGqmrJdGqiYQjp1FKYAdfbGAuFjYV_WV2zkPmUvPsQrCYOHE0OOBDIA3pMYmO3LYjcs2r5gopZas_VocuZgblwFW7Br2EdMTazRr5ncjbEH2fIQNEiiSAcm5Jh6Az-WleKOMNavxa7s0q1a2mytlgHMDMifjluJ5_MBB0OyZgoGg_Byt0SZ31eULY5shuN1PWRuMgaGbbl0N8brj_PHFLQtemilPFk4WL0FEA3yVbMUIomm-qOD5nOoKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کلارنس سیدورف اسطوره‌باشگاه‌آث‌میلان و رئال مادرید درکنار همسر ایرانی خود؛ سیدورف فصل قبل بعنوان مشاورمدیرعامل آبی‌ها 250 هزار دلار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26049" target="_blank">📅 11:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26048">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrUmBL0OI08C6JYdLdjE1p2ZTzItOdFZ68CHa0glmIuRsh0EewschSOAhk5Miv0aKTX9ZLlIt32ojsmpmzBgthXZygXzAQweeoFcSeeN3K-51FhP6IZd6TwngBT-UNHVtHhuEvO9vi3EYrS93hxBdOv7REConUjZZqOOt0voSqI4dr_Ba6zm8eUEbj_knWZVzRlvIgjMrR4g507vTlMv_SwwT4wKCYpVQgpWA--H9xEKtlY9Gxmj80MReg7lyyGCAZmlnv5ceIsX6S9q9XPJ0_7ozwmkNPPgvTPCRoGIqWBMLFvGMrm8koxl4RUvRYT2xafNcta2aT6FoAwLBIBusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26048" target="_blank">📅 11:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26047">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQvz_R-7ZfOHd98lF8bgzrmg8panqiKoq41TgiK1SF8VjXDpcsBrT2qXDx7_c5rcjM1wbjL1VHDdEFu7pesZAbGExzg1i1iCoepg84aGQHpTchCv0Rp7zjk9gRv9EIxxYFdWtrMceU9C1hsUPNBulrm7hxOs3cSi_isIAg23Y2Rq1Zn-qgExONNXhCOczCMFcMU-WYslisyS3xqYm9MqHYnLOmXqG3jObuvOZkYg-gtQLGf9VrWC149i96IJG_V7FmyMZ8wFw90GsuBVgE8YQ9i8iFyXIUXX0wAagKfetVW8UhJ2Tkac6VET8lNYT1HaVfQebfpTsgpKSV2k39-sng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26047" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26046">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYNoVGU2_YBIlp7PBA8RLt8p1lE26kXSsLAcywSRjA0luwxfprcjuWNM_-oCkqHN5LHiIvFMYLHyPjuA_uuHYTL6NCYQXZ_B7WTTjX_m7TIDcrBDW2bgUfFaPpyg5rDN_JZEeb_E1UMzhbyKyWDh4rDMIIno2VTEM971aOpDf4fdC8VWGhbivZbZEFmltNtjMabfoWSXF_3vaRc6HYL-CFRLxqVRw5wbQd0jvE83LD_rcidsXytUFV0zamTarnPq9Gh6PXYZ7E2uF3RZPekS6NN7KFYBXX-4RbbZUH5sZH5lf5pcUbnwKYCK98FEF15yVemaBrWXt-z9O1MzcO9MkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26046" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26045">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgFaoQX9ImNhn9TSi1O-GFrLWQK5hSqwSbOjps3a_J5aVUIE4tyq9SMrWQtHFDKUOA8E-L7NNAf75AA2TMNRcJZtrEL5KJIiFot8zS8LUQnoHzLlMrC0E5B2ei8A_obUpsce-kbdzXpkzgoR2jehYyIpcivKMYjSkRRpGOijoufasTxZXn27w21oQdigqDQMKy1WyhRmJ0mtP20of1wXWwB_PFTt52cfAi57i0X6OtlU_2Me4JOCelWl16ip87-7aM0LQmLpTgtR6MxhZ9nRhMOO5fcBB-dpTOGAIaNyWHX2Bq7atXw2xNVT_EOPcsg8n0tStSWNpWi5EaeOJlB89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26045" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26044">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">📹
ویدیوجدیدوبرگ‌ریزون‌میلادکرمی بلاگر معروف و محبوب ایلامی و ببینید. رفته رو پل B1 کرج!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26044" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26043">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2k6inj52MHQE0E4qqpkQyDFXLTIMtc4Nb3AfM6YA2q1ztjgeLRQRcJ454zA7un74k_jAMULHpwDun6x-xmyVJg_4tMRl7EtWICnLF1vQxmmWwyAF7rESatGVIhI4vHBt5IX8Vu0uqKa2xX11faQSjbiAdxB_nCdoy2w8_0q-S7m0m8UXuLs8vwfQzOQjRogOJPI2ImILH61ni6Sx7Pr_A8pzZigaYdgRQHRzaP-eQt7OuUR5rRvd1omKp_iZ1Kjjb6ReowN9cgEul6k9gcP3DFy9gxRU0_NWruY7YlDb9lX7JcWkYIQUa47OnfjsKu91-ty1a5nw6ggKOLRAWs5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
برای اولین بار در ایران ، فری بت
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎁
💰
سوپر بونوس
وینرو
، پیشبینی بازی فینال جام جهانی با بیمه ی
200
درصدی
☄️
⚽️
اسپانیا
🇪🇸
✖️
🇦🇷
آرژانیتن
⏰
امشب ساعت 22:30
🚨
ورزشگاه مت لایف
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr28
📩
@winro_io</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26043" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26042">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26042" target="_blank">📅 09:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26041">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=NyidLaUVnLePbPltjqZY4bfyeBzsUN75dGQzy9myiOYxdpdEZVA1GcVXfDE8jrk89A5XBgFNFXA_1W0kNAZwC-TO1jLSi5Cqqsl71UNWC0asxZplXWNU11kiYVpDIWQV4igcFQn9VGqtwPUmQVz_X4Qcp24fLZeaYw1gYMFqA9zTJhMEQRc7oxkxQ2KzD6zaNUWxJw1dANDtrLVKWR2YUW099sh3o5pgfy4v8etlLjh1CInxjr4T_LgzdFZaH1cGk7KOUMHPaqI_DcnFHnyradmsMKXnrAx97hU9Y3I6R0A8FcvlHtyPISjLhXa0JalByDLzxwhQrDt_YkOZdaqYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=NyidLaUVnLePbPltjqZY4bfyeBzsUN75dGQzy9myiOYxdpdEZVA1GcVXfDE8jrk89A5XBgFNFXA_1W0kNAZwC-TO1jLSi5Cqqsl71UNWC0asxZplXWNU11kiYVpDIWQV4igcFQn9VGqtwPUmQVz_X4Qcp24fLZeaYw1gYMFqA9zTJhMEQRc7oxkxQ2KzD6zaNUWxJw1dANDtrLVKWR2YUW099sh3o5pgfy4v8etlLjh1CInxjr4T_LgzdFZaH1cGk7KOUMHPaqI_DcnFHnyradmsMKXnrAx97hU9Y3I6R0A8FcvlHtyPISjLhXa0JalByDLzxwhQrDt_YkOZdaqYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین و پی‌درپی عادل فردوسی پور به امیر قلعه‌نویی سرمربی ایران در برنامه شب گذشته
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26041" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26040">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده و مهیج شب گذشته دو تیم انگلیس - فرانسه در رده‌بندی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26040" target="_blank">📅 08:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26038">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVxzpmbEY6mITACJAKa9qjIk_hVZVBmbbDMuxOTgVyugreOb8Fzrx6-wGQ7IrtwpR_kENLRbdg40JcNCLh6-tNyLtVgDUozGdVzKmHebP7wQ-HP3AtUcsT7QXDSO0l7lxpZuzns5Ilh6HhZSs67lZSakB9Jv_BUUuNJb1B-WIuAAzz8SZuCGiqa5iFu0gL3FShKHur7frnFPdHW34SLajFccUUO10jEv9l4wqhVvLdgwRxvIH2Ri3FuP5r_eAqFuFpCL1KlrRXne11tgiTkjVCOV7YHZHbcmtLdccIbkR1iyi8Ye3jAHkOk4CiTV2NKUGroVLDsm5U1_YtDSpcRDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNdrBDbm0Myt2ESeMUowGqqf6X92OFz1FUvAyLpot6yHthRC-qYjnaFx5qMcQgDkpbLByELA-wtFHUwdPhBTJ2ug_2TmjEN7KTj_JbMXIhCKtnTsKIYcMWeIHsTmiDwXzzxMdmSWAIoMXUOA_SONcEcyt9yiIJ_1qVmv_M2i4z4aVoR9w5cDZv0HZgAmcOlKpQL_lSJgN5y6iGd-QkEpJ4vg5Tc7VdKlmvNGt89WVxti1kdDpDPMrnB3IfG7TcSHJCBvxKtGgUUKDUNBl8yMD_ogDzbD3dBGaVH4oQ4axg2N_K4TkCZHuHJVfoLwHU5Ant5_Tvx9dMzUHAliS52nsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم‌ملی‌انگلیس شب گذشته در دیدار فوق العاده تماشایی بانتیجه6بر4 از سد تیم ملی فرانسه گذشت و رتبه سوم رقابت‌های جام رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26038" target="_blank">📅 08:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26037">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgJyzOhJPCcEm1IAbpWjEHATO4MNqJNHx8iuQxF3xNnVPeRiR2zKXXE_3ykwHVXBdcZkxJZOPed9HahITDYDVLCOdMri4LzZsVLNRxOMZUO6nIrRRjNM_4tpYUn5w39pB6tso_l7iQvczspig3AnCJvLwnX6ADDsjfBKkLF0PkV3kBsM3241Mzdq66ABu6RwlYNxF4x1QTj7y4m4OE2DwB1risllgzOMkfN0mp87ad2qUPd_eL1-D_Ts4xzLjWUOEuh5INHWeofAc0xJAp4EU8jLdSOhQWi2eqk9rjyNpvyRwAZc91oCgifUiuLmSpLCIZDJ9M5ABEnarBpOGtFhiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26037" target="_blank">📅 07:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26036">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=YMhxq76v-KjlhNv4YlAZ83075_S9p16IPKbxOnvHzGhDSb5P0iL4_Xyyot2BjRcKa8rj1MJ5pAgyhimXqLL3AwYiDsA24tCaOLXoXmVbQqWcK0C9zw0oPqWRfnAjKs3pMtEYOrlfC70b2-tnnlAihO9L5BTA25yaKpyYQEPYBESsW2aHXb1yY_UFm17-jITOlszcUBE0prC2S4BVkfRNgzYdAKo7Hu9xCY7SB-0A-ysfSMotOjM7KAqgal12DqJehjEkNden9LeElsGqF_Ab1jtjcwhMAuUCVwRDz4dYCWeWPbrZ24nzdkea-g7epMPv2GYszy3szgOKYiXRR5MgZz5PclUl-tKdP6QHfih_-IIM340ZmzqaD-7Ccr6S32CwFUmtNE3LfFKE_CQXUH-iopVib7z3PXLI6PYb7jB-HFJIESbtbRd-WjYLvURDfmnPMiHvt8bWu0Nysi7_mK_B--BZBl4ykF--T8QIs4QCzWbuzY3dtssSliXJBUeoTJJnc5nr20J4bJ5oB70Ax4XYm7Pq7sVES6z1ie6jyNDPbI2WcCuRdfKdb6i2XoeP9yeLySdzT9UNdQ4lR7t0GvaIuFXD12rZ2hbP2ZS5eVd33Mn4lwRvZLG8_vHyEJ6mlFPr9Jigu8BVe3UqxXy0bKXz2pDuvTT2AAfL_MUtlzXxhJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=YMhxq76v-KjlhNv4YlAZ83075_S9p16IPKbxOnvHzGhDSb5P0iL4_Xyyot2BjRcKa8rj1MJ5pAgyhimXqLL3AwYiDsA24tCaOLXoXmVbQqWcK0C9zw0oPqWRfnAjKs3pMtEYOrlfC70b2-tnnlAihO9L5BTA25yaKpyYQEPYBESsW2aHXb1yY_UFm17-jITOlszcUBE0prC2S4BVkfRNgzYdAKo7Hu9xCY7SB-0A-ysfSMotOjM7KAqgal12DqJehjEkNden9LeElsGqF_Ab1jtjcwhMAuUCVwRDz4dYCWeWPbrZ24nzdkea-g7epMPv2GYszy3szgOKYiXRR5MgZz5PclUl-tKdP6QHfih_-IIM340ZmzqaD-7Ccr6S32CwFUmtNE3LfFKE_CQXUH-iopVib7z3PXLI6PYb7jB-HFJIESbtbRd-WjYLvURDfmnPMiHvt8bWu0Nysi7_mK_B--BZBl4ykF--T8QIs4QCzWbuzY3dtssSliXJBUeoTJJnc5nr20J4bJ5oB70Ax4XYm7Pq7sVES6z1ie6jyNDPbI2WcCuRdfKdb6i2XoeP9yeLySdzT9UNdQ4lR7t0GvaIuFXD12rZ2hbP2ZS5eVd33Mn4lwRvZLG8_vHyEJ6mlFPr9Jigu8BVe3UqxXy0bKXz2pDuvTT2AAfL_MUtlzXxhJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب‌وغریب میلاد کردمی بلاگر ایلامی از افتادنش از روی صخره بخاطر یک تبلیغ کلینیک.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26036" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26034">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=LHSyJFYnF6m7bX3O2LRC02EVTvOrs5xyXYQuyXMURR8tpsZkwl4OwfmankXfNFlUYfuiqMtcRQH7iAeClIlfGat9BRgvoALS6f0wPTLgcIxy8rJhyUJh1JzlYwZLT47rlj1udAce9tA9OMG7iIo8NUPfgj_6hc1aeU1XzVX3CrJYfsBTyOg1AS-xEQ9Jlzx01LYEwgiIqJibgNiYzIb6qyNIN1JLvxppNKLc6W_X-L9y-KVwpUMYLfgoaCGPmOB1a4SGY2jXcgiM0ASCQ0-A0wEzCbqoE89lI-VVCGqbynG3ZIf4fttob7dy1zOvwkdVqWgvbbVrN-IdNuaoGrbvxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=LHSyJFYnF6m7bX3O2LRC02EVTvOrs5xyXYQuyXMURR8tpsZkwl4OwfmankXfNFlUYfuiqMtcRQH7iAeClIlfGat9BRgvoALS6f0wPTLgcIxy8rJhyUJh1JzlYwZLT47rlj1udAce9tA9OMG7iIo8NUPfgj_6hc1aeU1XzVX3CrJYfsBTyOg1AS-xEQ9Jlzx01LYEwgiIqJibgNiYzIb6qyNIN1JLvxppNKLc6W_X-L9y-KVwpUMYLfgoaCGPmOB1a4SGY2jXcgiM0ASCQ0-A0wEzCbqoE89lI-VVCGqbynG3ZIf4fttob7dy1zOvwkdVqWgvbbVrN-IdNuaoGrbvxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🎙
علاقه‌ شدید‌ جواد کاظمیان به مونیکا بلوچی ایتالیایی در گفتگو با ابوطالب: خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26034" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26033">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛
سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد اما گاوی در کمال تعجب قبول نکرد و گفت تنها عشق فعلی من بازی فوتباله!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26031">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVi5gCsfOTBSvIleSm30YkG1Xf_kqNlD5xjxueOMIscP171ZT4ZpJbtvy1-BXYs0aa93PoTd5hlHNP0mgZdy-F8xxGPE8EVHSmK_4jwHva9jvEZjhkt9hc08qsgL67FXMeOLI-Zvz1BPoZhzOGUto9_Jq5Wy9_gXqGNNMld9mh69iyTfPlE50bvGlpiPEOyun04wERtNb25jLQJTKlzDm5CDLUS7U7NC37vN31OwWruPeoKogYURN-zZR_jR58Udhxs0XvaIe8ut5DSxgPuF2RWF0ARALIyQIh_g1qNl-6iIX7sZ_ttB9JxiwA4fn4tV3ft3kYsAWScK813hmRvQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26031" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26029">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=FLEBMTKiBoFnDFLR5_dQv_lXvL6ZdR05Lu_zbPEgKQhDELLxjFxwma89B3t4E_Go95k71a4rRZQsePNXZXfLB3_OA2n70agHdnqDWqcuVjF8F7KUbwQJk85mFFjbDyFi6qWfJ_T6cdjjB3wD8XsQkjvB6ctSYRPL1CW5_PcQR7v91xF4ak2TUNhD4F2UgCnQw2MOjWMl9-ZfVs8Gx_fk9sve66yp2GFKBJSJ5gyvc91Rmzf-IUfAKMTdslHHai3oHp4UTU0U38nhPmLPHbxIKlQpR93AXtv1ksimt0WbAZhN_10muCfUurTTZnPcGH7Awovawvt6cLRWT_yv2V6URQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=FLEBMTKiBoFnDFLR5_dQv_lXvL6ZdR05Lu_zbPEgKQhDELLxjFxwma89B3t4E_Go95k71a4rRZQsePNXZXfLB3_OA2n70agHdnqDWqcuVjF8F7KUbwQJk85mFFjbDyFi6qWfJ_T6cdjjB3wD8XsQkjvB6ctSYRPL1CW5_PcQR7v91xF4ak2TUNhD4F2UgCnQw2MOjWMl9-ZfVs8Gx_fk9sve66yp2GFKBJSJ5gyvc91Rmzf-IUfAKMTdslHHai3oHp4UTU0U38nhPmLPHbxIKlQpR93AXtv1ksimt0WbAZhN_10muCfUurTTZnPcGH7Awovawvt6cLRWT_yv2V6URQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26029" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26028">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCLvKdbfZwUKDusPr7KabTaG7FCufB0HQAA1_PlEri4c6JmoiUJzN4i5756N8lAc5WfWsS1L27kTiL304mfa70cj08eqPyl2pAjCPL-jQPyl8Vbsb83UpDlrsEjsZJeTFtjr1bGG1KyoEo0ZkP9wYRQeqhxFYS6N_LYT0ECgbpqlHOf7vfd28pc9I1obh7jZCAOb6zYJPRRkMS9wmxsjC0ZE-IzgC5UN_WYhrsjIwBD70j1M7y6JFl0-9LCJ2rI4obf2Ly_iTp8iyDmjCMG2JBYkJm4rj_G4RAB1jaGpx4o_hHB9vmMwwKl7U3_IjR3b-7fKHRgfvLXdogcE7ic8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌دیدارهای‌امروز؛
کمتر از 22 ساعت تا نبرد تمام‌ عیار آرژانیتن
🆚
اسپانیا در فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26028" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26026">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzxBpi5FrzUfFTHu6NaPhvaXpbcB1d64BXDQZW7T-4-FlrBUBmC5GfcxxDksqfwNINga4uJTGmOdJH8p76FDr5F2CfJ1KZiWdU4rs4lSapzQUzOJ_geKy3k5sc2abZaq6CqNE2sUtdkYBDymGtgXLlGbDTnCZ2seKOIDL9QvqG5ZYjHER5CB0lEqWsHtRaDibWUDfTaacf27pCLEV3Z9eKrjeD6tmwqxaftHCP6UcJ1mgfmdet1qvjE04uSR_1oQzv7mVQivS2pNF2hUnJgGg9bYBlZOHm4QF2fnWC9yozEsntBlY1S-JaPgV0nrUbxW9K32QfKNBOHP3r9NkFOHKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26026" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26025">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJqHUS7zrAtxSkMNusV1Mcb4iJv50dmSg-HXRuNO_yXYTMzhZpLvpQQhPmJJzKcPOhjMqWtfLbUbiksmRU_pwTHFaP3EBjleUaqIbOckDyQ1Yr4-7aJq_zCuRrN1DDVkghVW5JOnIdkpxHgB6p0KNkbSXtDQZ8OT7vuVwsuZ6t84gSLu0urbyAamTIYmsksF9Wf5YVWWOfwlVZ_2QNqjNXeHrCF1iiabmqUgJKZyZD2wqJANVO35AIAhhbUyW1tqxIIG2cCEe9u-DgEEHsTXlZba6rNEIPStcKUAgNoc0qRWZEq42en9GTatBvS5jCe3vznYGf2GxiN5DL0bpCHkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26025" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26024">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=gQVuJ_zwz7lNGH9CjYHzhG4cbolH2Nmtq1kekKr1hACt_Do9ldZEz1wQg7jln-b40yfiXg-HD6drxVvq1bnPpgjA01dPDpHEAt8N30ggjt2pjYJ13h0GMJ7MbQ5iZ6yIkum7bxuGQvgCdNyU0YFIEMMY9ITOYkWJzlXVIA9zOKNVzOHBnlXkGlcasyqz0ObfiYoMKfeRGjj3Au9ZRiEoeN4hhAXhQc30sp8Hgd_cA61eDsB_TwEvYyoSs9yVcCgPSYAUiIkBwrxCnEmbQIDKd8i-yZh31jbPDN9TAEhx5u8_uZwWt-Wn3CR1DMuJvOZ_qqaV_n2Vp9lLHJd4IM_wdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=gQVuJ_zwz7lNGH9CjYHzhG4cbolH2Nmtq1kekKr1hACt_Do9ldZEz1wQg7jln-b40yfiXg-HD6drxVvq1bnPpgjA01dPDpHEAt8N30ggjt2pjYJ13h0GMJ7MbQ5iZ6yIkum7bxuGQvgCdNyU0YFIEMMY9ITOYkWJzlXVIA9zOKNVzOHBnlXkGlcasyqz0ObfiYoMKfeRGjj3Au9ZRiEoeN4hhAXhQc30sp8Hgd_cA61eDsB_TwEvYyoSs9yVcCgPSYAUiIkBwrxCnEmbQIDKd8i-yZh31jbPDN9TAEhx5u8_uZwWt-Wn3CR1DMuJvOZ_qqaV_n2Vp9lLHJd4IM_wdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26024" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26023">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=YBbdoYprgfDkwfDVBDarPjgqvnkTtRP6Di1t0MMCqEVm0k6ds3UH_BfqWIMHHtuMctAFIs-Cw-dk0QRjgEeI6Whr8Bdq23n7YDbS1EoVkNrmXpT37ZkjTEbMQf_Dg0UjL-8zo3PvSFcS6Dra6ZYKxE5MYFoPgCENB-7ZNK91G-oJAD_MQTZpOWQYD10yKyoCpyq5AdQ_lLVi2Bbe6wQGZALuY0QK-5PkxtXUVaM1i38usNqplOH0HWf99kd5rf66zy9nKQakWHW5gxJPhHaksJM1CkWJlqnbM7uZubHhQo2ExJNbW315pgaX38FLldR0bv12RI8r_Spe4noB4TEwDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=YBbdoYprgfDkwfDVBDarPjgqvnkTtRP6Di1t0MMCqEVm0k6ds3UH_BfqWIMHHtuMctAFIs-Cw-dk0QRjgEeI6Whr8Bdq23n7YDbS1EoVkNrmXpT37ZkjTEbMQf_Dg0UjL-8zo3PvSFcS6Dra6ZYKxE5MYFoPgCENB-7ZNK91G-oJAD_MQTZpOWQYD10yKyoCpyq5AdQ_lLVi2Bbe6wQGZALuY0QK-5PkxtXUVaM1i38usNqplOH0HWf99kd5rf66zy9nKQakWHW5gxJPhHaksJM1CkWJlqnbM7uZubHhQo2ExJNbW315pgaX38FLldR0bv12RI8r_Spe4noB4TEwDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب‌شروع‌شد؛ جواد کاظمیان با انتشار این استوری و تگ کردن مونیکا بلوچی تولد او رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26023" target="_blank">📅 23:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26022">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrRkz70T20DdGERw5TCjmQK94M_7qt-ga497pa_S5GRMeYki30v6nxITXssFMpCTiN-nWPs8mMFia6xRzuui8vrUrqTa6LdsCLdKunvsOXnOZdHeUv1xGlr3gWMaLV5XNaw-j4-A_1IwagvfvbL5A6qaV5DgiuQumN3aDH1h2Q3tVlNlo9X-2U58fyIZ10rvbUO0TcdsgbpncYo10ySRouueGHh8n95aC5dCdGP5i3IbIG_OCyH_-NLWu7L8XqrvBYeNmcIjnV8ufaum-wNERzEeWjCY6p018Hq_eAqa2cyJSKQwOp22iDSMymjHe0AmLDYjfgbxJQOsrV_GWuX2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26022" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26020">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUOb9YCZcAWjLupH-4Zm1IiCcMah2nGMNds9rl05xWkdTHE16PMKwYei_QKPjXjnm3UdkwqQ1D8mFJagOsVEDp2U5NRbeNUDbfLSyj1YE4EhS0ZGsm5mPbD2G5sA75CI1_G3oicT0pqatSXYWuPomHgtIKJ-2ZlzSGirCuKlqh9aBjNiZcLSjwyrxMCqNDTU0ntb3Kj79wWOMhz_zv_LlNbb-t6ELA3mpEtwuM0_IiVAclrgqdaQaatZ-gplAGWk2enkdaDX3lidgvWxkoA7_ZZCCk6g3zMTqeLLgCdQoLaJGj8_MHYA5yrORwzokeetfHWc1Wt4G_MI3d6TzcbvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqFBqTZVEb2jCiZccqrcIHsJ3tE0N2CBKXR-eV5GS2vAAwk11hCyvuRBZY5yNhS7E4ZXVf6T7giJs2SQo4Jf2nJkse9xWiCpP1kNJbAia3ItL6LYRAvREA_PyrqQeZMYVaPW61Ad9PfBJSYr_e1OnrYmXfJF8M5OFO6GBZcMCGUpuXuK-32xbx9swvDuT3DzEYyhqq1djyaJvbXTGf1uGPCvbumwPH-MsrJ2PBgLbpCpn4R-OFClH47iNpHDfUBb83EeiLBhdnGqLJHQqamHJeVlFAc_2DjU3T8gZ8x4q7XomywI_AQHxcUutuBTT9iGpHQEovWSNo21hvO42VymGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26020" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26019">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsRNwVtA6TpTrpotLppIwCWHLbs4oY0c1PLlPK9RPLfuMKCPmyWA7_AMDaEAkgbfNjNH-YcrYcjhFexxC-l6LRsVDjXOpikQUwUh3MB4tixASrU7bLiXFonRy2oqAZhi5BZdRX2_1cXSJ2CPPSEAGwR9JqVWY16nDLmLzJ1Od3WBdGDKCjuRlm31-OTDGNW-RQY0tgA7yWVVBuqr3IplU5Ok7hryXuptAjg3pcl9QwAgfsDa0QpuRlNWUSEuk0QgomJvq1AB5iOULpJagx9097sGre08MjGLnNJRm0eSaMRuPjontTirTOHbjdoGUHiPkr2gGelrUFIhgT9leXP6nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26019" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26018">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6wO4VzEmEol8ZSxS_J9-Lr08ws8oAcQxhRUn92caYUYSfl-JHZvuzvgTC8-JPhNySJMgkOha9LQM5VP59WcxCvy15C_wlwMjlfoq51SYHP5afyZLkDafD5X19GJaNJVi0YexXJjUZaV7-yzriJpt88TGc061-74LH75S2UpNegvuDkx8X45CN0AZEiDTo4EfGV-v-JQOnHHObZyrmgn9MNRAO5cfpH53DRC8LkNYIXB84KkiZzGAlITfOAnD3X6UkkkF_QjU4QHodnxsEqQe-FYZF59fH8dNw4F6bjtQWKk7cYFaWZBtMxBpl8P1N4jsr7FQ2-ZDrG0wRP6aARXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26018" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26016">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇪🇸
🔴
هایلایتی‌از عمکرد آلن‌هلیلوویچ ستاره سابق بارسلونا که در آستانه عقد قرار داد با پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26016" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26015">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5CPYcKrMHvBdEsVxdlRIxNiM4ba8mXJoBB5gQFymr83IKd5G4mTRuoD7_qq5WwK9iAzTx5TourKXQodkViyTzYU9TBI5jAz8iKFoeNANQxVLAI19Va5BMW-o-HKSvlPzoK0wrz_cGIhGmwVE65G2xY96AcAGXJNYTfekA29isuRwzuv1lOxeOIfRt4fvee4f-XDveoRW6NtkA3Qzpu1Ag20Q6fJ1rWIz-Mulz1F5uTyURN8bZKoxicQkcKQG5aiyBR9yfBquSM3Q-Xfa7rnoe3OhXHgYIUWqnpdEn_8UED8BYZjhjA3pWzfm6bXfkqLCq2DKzbzImDctuUUPLTt3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه‌پرسپولیس به‌درخواست شخص مهدی تارتار با یک‌مهاجم‌کرواسی که سابقه بازی در تیم‌های ملی پایه این کشور درکارنامه‌خود داره وارد مذاکره شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26015" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26014">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIuEBxJh3ySIEMbDOjlUW-0mlDJ6h4FNE-V2Bp_Se2xIJWx3q33GE9_IHMuFOGmNSULxiv8Xf2YGzgaDJdXtkv9Z_hBeuRgMSEy_n3za2TWM0oMO3cX_HLc0I_Hk6dugbIXsgaODM80kbI7PI8svkklMy6RFlchX-2uMlk3dFXkdzWOG1tfjr1D3lT4kk9EHTAJFREkLQU8fF0q-BsIYj0p13a6wh2dZwGo5mHAlTcjrdmV4rZppntVAbCbCEF5giWltV4qBf8pVqmayVeX1MWLIeEccajbCLP46oZ-4503NYGuJjSY3PG8ivfRsgcGlHEj3wFscF2vjir0B5CyvCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری اسطوره باشگاه چلسی انگلیس:
این سوال رو از من می‌پرسن که چطور می‌شه مسی رو متوقف‌کرد؟جوابش‌اینه:هیچجوره نمی‌شه! حتی اگه بخوای با بازی فیزیکی جلوش رو بگیری، فقط باعث بهتر شدن اون می‌شی. مسی فوق‌العاده قدرتمنده، از جنگیدن لذت می‌بره و واقعاً هر چی که فکرشو کنید داره. به نظر من که اون بهترین بازیکن تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26014" target="_blank">📅 22:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26013">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=Ub4uaKu8LROnrxnAtaRNGEk7rBoBd7ZRk3V4Qm83DveB5YkWQ-ToQWE2jXRRhiD1AzwiJottml00e867G8x7SW7HFpd11_wY_ucPpAaLix7ws_3B1fOJGIChP0Xve_JD-_jbVhhuiVSvIJNfL9hynBwCRTUQZC-IbWzoxQCKgSPD2JMjDIARVlKWj-dzMxQ4wmpf4gAge8T4p34viL37opNAOXK8geJFOVsxPN18zZrRCa_mnchWHYAL2TRNIN6D1_-SLI4T575qMhai7FCseY1EedPM-OVcmuTQ2CHVYnSJC_EJNcC7u0w0mDo_7LlZAJXQ-rfAEA1yLEg3tsl_WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=Ub4uaKu8LROnrxnAtaRNGEk7rBoBd7ZRk3V4Qm83DveB5YkWQ-ToQWE2jXRRhiD1AzwiJottml00e867G8x7SW7HFpd11_wY_ucPpAaLix7ws_3B1fOJGIChP0Xve_JD-_jbVhhuiVSvIJNfL9hynBwCRTUQZC-IbWzoxQCKgSPD2JMjDIARVlKWj-dzMxQ4wmpf4gAge8T4p34viL37opNAOXK8geJFOVsxPN18zZrRCa_mnchWHYAL2TRNIN6D1_-SLI4T575qMhai7FCseY1EedPM-OVcmuTQ2CHVYnSJC_EJNcC7u0w0mDo_7LlZAJXQ-rfAEA1yLEg3tsl_WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26013" target="_blank">📅 22:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26012">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUurq_mRK6UAg-ftvEGLh5ZS6ySfxC5n-e50m2WxFuml8wUA8IorPYfYPd7idhQGBE9tEQ64eQdlE9Z2ak-AMKbf_f157crOjO7FoefheJQGWavOwtWwVgOLdUJV5vJKkNYlNp050wtuyNbkCsYuXCPXMxvRWWK52rCPKO0GrwR7tHjMCq2YGQkoAqc5lkZ9sxvTfRDlAtCrpO5oNuOp-k74piyYHV7nMFjUDoKvOXxvdRHE6XK_Uu4UyrxHes_ill9bxT5AWPlXU1pgrpPBABdDPE3PKotqG1Q-n7jFgTrPhqUhTsvQYKQUdFj82fd9gcYpJIicRrFk4KQSXZ9O_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26012" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26011">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ua6CZqFOwJS7vfvsdiMJ53koajxAKPo0GDIVm3JpDcjVwJUBpg0hfZwiWkCd2O5CuBYNHcA9aatqxGaXQtSkSemWORND_weD4agmom9K1vuYT-dGeNBfgVqHi8nFWtNtIeqqJ_ZWnZ3Jz5ett-SKlrIB6Gu-7F1kZKFaXyo0d284apVD11Ab6jrVXWVezOGuHZWKm_73mtx1xii2PihHC4LdRnAWLFYBizjLA6uFOfavPkwx9EWoMscwtwoqKHvinx08E75FXR5VnbduZ1bXuDRi7YFs6o5lcSqUKImdcmhIXKfucUoZiBlDoYdDmfDlamuCwJGijRh_n86ZRDbfkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26011" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26010">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nut1pB5HLdphR3BNUfcYj2foJUw2EXZGCpngd4-kKMXrRbE_qvLikbSO2kWUsaQ3fQPRm0y7DzH4g4Weyj2Bbv1eXZSvquD7tjk-XDJ4MTXiXwwVEEBAY_20E1v8TYBEGjdeivonCgsU4gKjGw4dCm7Cr3ywiBuE2KNP4DQT2TWRg1Yyepk-jEnmCDaz9on9LRKNLJ1PUjEhBdOsJONpvvnHSx9iCVuvPuZpPbvww3u0nN7W7QQZneueDyzrztbqfEfC9LkS-LnBKGkIbfXNuOKGlfTR08GNw95O3c2p099CpfN4sk7ZN_A63Pq7e2Am7Duqe7vlQvunAUWxSjq6Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتاین: آرسنال هایجک خورد؛ تیم چلسی با ارائه پیشنهادی 137 میلیون یورویی به آستون ویلا درآستانه عقدقرارداد پنج ساله با مورگان راجرز ستاره ملی پوش این باشگاه قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26010" target="_blank">📅 21:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26009">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT0KYUpS0c7AnYf1-m3VIS_rwbJ83ndIthmdsKLOXUiqwfDyEAaAP1RW7ZaCskRt3CXtl9BfU_nLTY4L3wsgXfEgLMT3Nqs9PVwCBhjMuDxRbLklIhHxotU1wW8lOa1kFScdZFUmOW-5DCyZRebbZNs36GS36CMV9SX4yImEKIRDi8CmrDpIp1oAgojlyTJeBGjcqDUrQYGROUBV3zcpTz4SETeABMNE-bNFbPdLariGlzsAb3Q0Xe1vYOmHG6lPpCv89BzwDrpkdoiJUyLJ4tlozVo6prVlhvgqhLPnTu02Hnq0SGMpZZdjD3bQIoULtuL1-9hmb-hqaCgZXbwuYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26009" target="_blank">📅 21:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26008">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=SEp0B7zSba1jCFOtipVCKyLDo9SlFUTyBleVg1GJAjOvGWwY6sQ9S-Hgt0gNN0QAJMeLvSlW71c5QPLHorXZ14W5_P4d8VdGVndk00BR8mzrFCN-xojR9SwUtutglG9fe6Rdl45d9LqjnjbNsGgVtHS5eOd37fCdd5f7cQP98BOXdI02qL5QQ_SSU_99GRSJAsPGu_VDTUa8-j3TeTEGFSjCmMCx34rLsd6le6Y7ZhkRbD29Xc92EY_aNBNtO3y5ouNN_xVr9FRZPO7SvYrKZvF-NJ8dNypYImkc5Gab9VaFxEPPZDyqBANfnmY2OR3nfSp3aiLZtqMx2LWLBhYvRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=SEp0B7zSba1jCFOtipVCKyLDo9SlFUTyBleVg1GJAjOvGWwY6sQ9S-Hgt0gNN0QAJMeLvSlW71c5QPLHorXZ14W5_P4d8VdGVndk00BR8mzrFCN-xojR9SwUtutglG9fe6Rdl45d9LqjnjbNsGgVtHS5eOd37fCdd5f7cQP98BOXdI02qL5QQ_SSU_99GRSJAsPGu_VDTUa8-j3TeTEGFSjCmMCx34rLsd6le6Y7ZhkRbD29Xc92EY_aNBNtO3y5ouNN_xVr9FRZPO7SvYrKZvF-NJ8dNypYImkc5Gab9VaFxEPPZDyqBANfnmY2OR3nfSp3aiLZtqMx2LWLBhYvRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تو زندگی همه باید مثل علیرضا فغانی باشیم که حتی اگه داور فینال جام جهانی هم نشدیم از تلاش کردن تو زندگی ناامید نشیم. امید کلید پیروزیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26008" target="_blank">📅 20:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26007">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGMRZ7j0uObEi-p-z6IM-JKRJNaRhTwEPMNvLsW0e78dV4xVF5adkfym0vRaRGbWIYQK6AubP8RfDQUoTqSGqiX-yIiFycyxuCAV-MI7tjRdy1LBDkSOblsphY6dxhle0RJ38KtsXHNm8fm6p5bMz8mAOLyZMhP92zPxWcva_v-IDVafC5QKVsySWJiBwCxiuGo7qFmpjQjrYxJTNawH80dBwNmU_jE_N6ptmiwxjcZHjvcR_u9P9b8kv0dnVJFBQmF4zeUHlHfsynbslcjGyv7iWRYHMW1SUVBM13_USrNo3SU9ssvDuMOmVxD745oQJNCHQ48RKef9d4F8Hez4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26007" target="_blank">📅 20:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26006">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEjpkBysEYVgl4-a7vqUxuButU-GnHWqFQGShjxMuCKOFQ3gxOYRnJLGr2EFfCHqDBvimGWcOqGdyPryUqaxkvCxeBQJ3Olk0UyfvuqBgCbZS44GLonuiGK6W3R83waIha7_37ZJ1r12A61DyRFmu7olgAcnNOtFoOsei52x6nBGshV21KAEcEu4u4jP-3sEZTRLjeasRTyhIikYLrxtCe1N4ospTk79T_HEnESbFimW141b0U3XMkpTpKr3FXrwJm7zn_GH6_TPz5cRX9bVcgOmXo4uE0VOqoF1wE9xtAibieyeZgl5GJ5JMO0XY99tY6EyHvjh_0VT4M2iSXKTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راجب خبر حسین نژاد هم‌پرسیدیم گفتن تا شب بهتون خبر میدیم که توافق استقلال با روسا صحت داره یا که خیر. وضعیت جلسه باشگاه پرسپولیس با نساجی برای جذب ایری و طاهری هم مشخص بشه قطعا تو کانال میزنیم. خبر رو بی سر و ته نمیزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26006" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26005">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogSPEgUBx0WATht76GeGf3TC4uV0Q587lXjvNTLVZFV8Uw18Lio1hoDUloGf_7rR59okqAfOKTZpI7WmXHduuiS0dGweeWAO5cS73QVbTULG8mFg-lQjgNxis1TqWdwvqB4KuiihfgEIX2xh0ylz8hZIAmCzbVYK_tVrWI2vY9q_Ldq7j50LG9nGKkKXf5lbvdpko6VzN0LPodECpKE6Iud663TA0bDtQQdIMyKN0_ZdZO9DjDupHqyEyv-Ac7hUqZpmaxzMGaBcY2q3JLMxY2U8uIzVEgc5LSzGmNM36m4TP_c3DxzYGaX5U_15oV_3fgfkGRNNmHWyfxC_H4JNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وزارت‌ارتباطات‌شایعه‌قطع‌اینترنت پس از جام جهانی را تکذیب کرد.
علیرضا عبداللهی‌نژاد»، رئیس مرکز روابط‌عمومی و اطلاع‌رسانی وزارت ارتباطات و فناوری اطلاعات، شایعات مطرح شده در شبکه‌های اجتماعی مبنی بر قطع اینترنت پس از مسابقات جام جهانی را کاملاًبی‌اساس‌دانست. واقعا اونایی همچین شایعاتی پخش میکنن مریضن. سه ماه مردم ما نت نداشتن بسه دیگه کم دهن مردم رو سرویس کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26005" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26003">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UICwqW__S5Cvrubeq3g-6KR3xpDaMgl085l6aQPDV27U8UGbxEg3PdILE0-uoFg6np8gVdkLVTLqlxPK-VQHeWVp_u09TC4ZcXL1SP4A0C7FGA-UiZHajYEPZ1PXitSD1nn2AzJ9GOP_KAeBzVphcTnSD-E_NKf3y2agwJb2hg6q7jL6CliJcD-WYn1SB3zPzvMXlYZ4yfo8bmj0Vq8MSC4fbIlAV-NM8A4tabT93C3ygBn5hCONapBXz-_P-WJQ4A4gcKwdX300XekO49yAgp24OOvKbUqrRnqhr7rLhTy9BjTkpW-Nu5fOjYNf6Ueewrbwani7BXDBnOcLyY9Stg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
آدیداس‌ازاستوک‌های مسی برای فینال جام جهانی رونمایی کرد که روش‌عبارت "آخرین رقص" حک شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26003" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26002">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=Ra0pewNzpuM_bRA9fdPpXCSm-1KiALyMaAbPrvdGoPdGDr3MGxG9hfbo42QRhfxl-1rcg89xAkgg4kK5-u6xGvpGpSjfboPjSTBeK0BvEbQi4SKihpgkOR5iMKF0x1IhqgCV_1VeyymWVRrG3qMm4rKY60xdFQVghaETv7I3kJNNJEIXQHTmW4ge_IFaWLGIITzCWjzjGDGN9VYNZO_TEpRHFkgg6r7dJRdW7HVogN-kz-Im5t-r2uKtzlYAGWhGnkDy1OqXzVyZo_5JOSmCMiweUK7QoYe4oUnn5g4QnIHbNuKi6eWIcBUxUDnXZjPlydUvZOcjS99yB8Ehkc7_iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=Ra0pewNzpuM_bRA9fdPpXCSm-1KiALyMaAbPrvdGoPdGDr3MGxG9hfbo42QRhfxl-1rcg89xAkgg4kK5-u6xGvpGpSjfboPjSTBeK0BvEbQi4SKihpgkOR5iMKF0x1IhqgCV_1VeyymWVRrG3qMm4rKY60xdFQVghaETv7I3kJNNJEIXQHTmW4ge_IFaWLGIITzCWjzjGDGN9VYNZO_TEpRHFkgg6r7dJRdW7HVogN-kz-Im5t-r2uKtzlYAGWhGnkDy1OqXzVyZo_5JOSmCMiweUK7QoYe4oUnn5g4QnIHbNuKi6eWIcBUxUDnXZjPlydUvZOcjS99yB8Ehkc7_iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ درباره مسی: من‌از ورزش‌سر درمیارم، یه چیزایی هم از فوتبال می‌دونم. داشتم بازی مسی رو نگاه می‌کردم، دیدم مدافع‌ها حسابی چسبیده بودن بهش. ولی یهو دیدم غیبش زد و سر از سمت راست زمین درآورد. میفهمید‌ من چی میگم؟ همین خودش توجهم رو جلب کرد. هیچ‌کس هم درباره‌اش حرف نزد، ولی من خودم متوجهش شدم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26002" target="_blank">📅 18:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26001">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEFOvdWQniu_72Szr823xxDZD0_72d5PmvLri7xmQdo_gGHy0zvAS-52bWq5nyOjFXN4RmbijigKCrnZAtitjMKgpwoEi301ZgXx67l6P-Aj4chqchAUy5d6JmP0aJhM75uIxcY-G1fbBZjlKjUBgDdvxToZlNs_eWFFexHsKW1slh-ye-z6i2mVP5UiLxJRW4JaXp-i3H4lkAMysMc7ELjd_vh9oHc7SiWw9VZpy-BL9pW8fdYIZPCE_35KlWOP6Z5WXXQmP2e98Q0gF7j5AY9PGFblNF0tRWsvlQG1OnRKufSyxbyElDgsYUdPE89KOfuu24cANY4egXhZVgvAJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوان‌کاپدویلا دفاع‌سابق‌اسپانیا باسابقه قهرمانی جهان دست‌زن و بچه رو گرفته و بره آمریکا فینال رو تماشا کنه بهش ویزا ندادند. حالا چرا؟ چون 10 سال پیش برای بازی خیریه به ایران سفر کرده بود .
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26001" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26000">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl3M0Qkip_8bHFXyZAnfvAla7QfNh0Taqc1xZGyJ4veO4MmfHrFceUN_12Js6wFyxmgZt5f343yzw2GVoZZQxKP9YOL0VgDoLxd_2eo7FBANALjLLUP9rcXAOTMh_3ywqvzWIni4E5qwTV_BzY-M5CdgCf75mV-37LK0NcDgUUCHVfVRrqivWLOoiUVrbzivMpYjiiRVTUZvv8JfJSkk6fKFBRu2o12kaOSmB-T_jelUgg9iggaVXrD1Y3_9AO2LD_D4WbVE-1HyxPz4_F60IThIbkdUTWK7wZCiv89syTKxIfl-qTlUBamzS37BPXNSqidMJZ_i8CT6CudAV8H2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26000" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25998">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0KfErPzStDvXNWRfQPIlK-x4HSuJdAPg3FTu6-Fdt44Gi1MMHWhQZ9BeaHJznQgUcD3ypJ-3imdPJYNRpyaP3ioOwMokSS1SCdaFHdZhm8P1i_VRJr92jnWYZSG7NsIcMsNwXiyusrK07Izjvr5zjr1utAtXevZfhzAUhaHTDL3KmEpWL2hZFGeUx17ZDZRPyQFBmjitUyNUro7AfMjUSXnV_fhTkD38_1_cUqMFK47_qyd39j0PqgjwdnwNsgQZkt0F-s4DeDQsCrdgkFPHjZ73pP5EoQjDve8_rQ82qS4qjf62y4hcfNi10jnrSynhOVU6sIGHG6Ap-kICI01BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم اومده با استفاده از تکنولوژی آفساید درجام‌جهانی2026 باسنشو مورد بررسی قرار داده؛ افساید مهدی طارمی هم تقریبا همچین چیزی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25998" target="_blank">📅 18:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25997">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/empxH6ifIgBYiVt20zEnBkEf1bCNxlwrImdP8WuO5XmZK6O7peg5_ysbLz8fXeSHQ0Sn6E3PUjeS3o0AJmBQtColQair3G_it-THNT246m5lHoBfBEx674LGgNEIXQJ0NCy_m8rA3ZBqOQLiZootOF7zVJl9nSu8178uhcnw2_jpG1S_ZNpaZn_BH-LevofWm_xuseOECCEEDUbZ42ldT7a0FReTj1LtsOuDNhBSwFmFwvZNO1JZE-M5TJpAufG8hFtan1j8gPm4tkcOnSVE7UBe8q3XDNkxnT5aB_8kawkuJLHhg1MOpUYiWWyv-zVAJcmyraOFdmbH7j650UQvKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25997" target="_blank">📅 18:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25996">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWPW_U3z1pogohp6DrKoW1lQM3WW7V2s2hatvUBNjgK8q-jViy5ULVZt674F0YZxO5HfgUsVtYotEf_Zy_RpXT6LHKp3JlMZqST3_IEMakCBtzZyxmwT7iZY1XybA4dmgIymOiARGS4gARdDMUSab2FaBLmHwwFfge_vp29ZfO-5JU4nOE4FsG_9zzcjoyA847hME5_OFe3Lvl4t91lTYJd76Kr5-gKgMP6HpemKeIk10bIfO2xfXkDT3olSeC0XEYux_QBzaGj-nNsoU0salJWnLp_wOfPdNs7kfVbMclmRjgY-EhjmfbK7eSV-VuQPBaAxyItPESDy_f8HVufvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25996" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25995">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=pIqixkx9QLYtJ5xUuOQXPEd8cuv7_RF3WDIv0vqShz0A7zO6ksVUg-Ia58S9EmvyVGBQYCb0cHEliZzlYwLXzkDyAF0M4-J0hkO59eABEwmqhArTQf0oCaqSLGSqo4hitLCNxNTreLm8NXHrw4IWxqUL-iqUsc6pglfxePB-jY2PZVFC1ID5YMAMb32VfCwlNLzExIvr_GmRM0FRh4plsYDLnbL2NO_2SiDXizioPf6iIkqiikVpI1t0EbQvTQ2nQFvyMWGJ2AJnOL-tURyeCCKi9ZA1CwpAj1cKELaKuH6ja6f-955MI90kb5larVmr-LCFQxeVoeReQy2Rj6Y9CS20_C7-Ak4GFz-nNEmvBhfbPg7mM2x5Xxoxf7QtQHS8chH2wjBu2CTHf2wzxPdPvvrsoYFaeH7zXJgHYka_i2O_cFbjG3GMCWWGQybn9doi8aB_RRn4Xjp7qlXH5CumnPlQtuerki6gQEmwGaHpQUorvoqATMejX96nyzk9-c1RKa8GQ7N9UO7cWEY9gEmJs5WeL0ZUgIobkrVBRMzyQNgauf8JO-qqyBDUcEvw3dAQ23HIfwtX1oWt0KatPUXFUvrRMqH2nnNV-6OMTCK5YG0Cb3_IcMPN0WunfynbfIzc8-Ov-hoSC3_P6-Oe_sKwm9JXru4rVZ_xru5JENFxgOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=pIqixkx9QLYtJ5xUuOQXPEd8cuv7_RF3WDIv0vqShz0A7zO6ksVUg-Ia58S9EmvyVGBQYCb0cHEliZzlYwLXzkDyAF0M4-J0hkO59eABEwmqhArTQf0oCaqSLGSqo4hitLCNxNTreLm8NXHrw4IWxqUL-iqUsc6pglfxePB-jY2PZVFC1ID5YMAMb32VfCwlNLzExIvr_GmRM0FRh4plsYDLnbL2NO_2SiDXizioPf6iIkqiikVpI1t0EbQvTQ2nQFvyMWGJ2AJnOL-tURyeCCKi9ZA1CwpAj1cKELaKuH6ja6f-955MI90kb5larVmr-LCFQxeVoeReQy2Rj6Y9CS20_C7-Ak4GFz-nNEmvBhfbPg7mM2x5Xxoxf7QtQHS8chH2wjBu2CTHf2wzxPdPvvrsoYFaeH7zXJgHYka_i2O_cFbjG3GMCWWGQybn9doi8aB_RRn4Xjp7qlXH5CumnPlQtuerki6gQEmwGaHpQUorvoqATMejX96nyzk9-c1RKa8GQ7N9UO7cWEY9gEmJs5WeL0ZUgIobkrVBRMzyQNgauf8JO-qqyBDUcEvw3dAQ23HIfwtX1oWt0KatPUXFUvrRMqH2nnNV-6OMTCK5YG0Cb3_IcMPN0WunfynbfIzc8-Ov-hoSC3_P6-Oe_sKwm9JXru4rVZ_xru5JENFxgOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیو ساخته‌شده با هوش‌مصنوعیه که خود کریس هم لایکش کرده، انقدر قشنگ ساخته شده که قطعاًاحساسی‌ترین‌ویدیوییه‌که میتونید امروز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25995" target="_blank">📅 17:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25994">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=fXT0QrJUhvgzEkKbiQtzQScARLTgNYCjJNUDY-C0BfQalLuzsJpsH0f-x0AS6lOUEMT9AcTj3kedH_5BCPI_b9WZtZwOPcwOHWoY6BwtFUfgAqPEPitxN4A-xCkZspAe8JHY9ogOsh2NDVy30IjZ3YpwKNhvVIXEIhZRM70YjWPSZHTcS75R3olN1bqIWWv0T-Tfr0NSkQuOfwcJDxaa-HlMANi02mb2QKrBYr-vZTXH9I2igSzKbvewKG_uZyg39-GGZji14fmFPVz2pEY5wApicav3zZFfU2PLKMzrYRtpb8Z2fbAT2ryArByU5MUwn-tHftfXL5yKoDreIYXP3F0VIm2OA0eWiupKn-ocp_us1rkDgKRCUrnP68SeMtgIrYqTx3DAkkgNaiuMfBLeLhTNIgnlPWbnLx6eLEEZFpXj1Si9MNFKoCKMxskBVXiv3h-j8rORo0_QZzyZrclNVwSdnbPeVsKE2Aue5BEyFZKjRCM_lckV06BnPc8odxOGQy5L_KI9SkIKoaj0rZi2Ptb5tOm6qTAEs1clV3UkuamcMYa4GEUuUhCIfo--OO_6_zlYKPOfXV7ZQr-8CDI4ifSZ0GoIxNmdmMQVnAan0g5HztGjHaKHa_45jh3qXft9GpOTii7AYZuv2C4TwCBMgsOEqvSzd1NYEiu63QIf6_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=fXT0QrJUhvgzEkKbiQtzQScARLTgNYCjJNUDY-C0BfQalLuzsJpsH0f-x0AS6lOUEMT9AcTj3kedH_5BCPI_b9WZtZwOPcwOHWoY6BwtFUfgAqPEPitxN4A-xCkZspAe8JHY9ogOsh2NDVy30IjZ3YpwKNhvVIXEIhZRM70YjWPSZHTcS75R3olN1bqIWWv0T-Tfr0NSkQuOfwcJDxaa-HlMANi02mb2QKrBYr-vZTXH9I2igSzKbvewKG_uZyg39-GGZji14fmFPVz2pEY5wApicav3zZFfU2PLKMzrYRtpb8Z2fbAT2ryArByU5MUwn-tHftfXL5yKoDreIYXP3F0VIm2OA0eWiupKn-ocp_us1rkDgKRCUrnP68SeMtgIrYqTx3DAkkgNaiuMfBLeLhTNIgnlPWbnLx6eLEEZFpXj1Si9MNFKoCKMxskBVXiv3h-j8rORo0_QZzyZrclNVwSdnbPeVsKE2Aue5BEyFZKjRCM_lckV06BnPc8odxOGQy5L_KI9SkIKoaj0rZi2Ptb5tOm6qTAEs1clV3UkuamcMYa4GEUuUhCIfo--OO_6_zlYKPOfXV7ZQr-8CDI4ifSZ0GoIxNmdmMQVnAan0g5HztGjHaKHa_45jh3qXft9GpOTii7AYZuv2C4TwCBMgsOEqvSzd1NYEiu63QIf6_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌بدونید فدراسیون‌فوتبال‌اسپانیا به سر آشپز ایرانیه یک میلیون‌دلار داده که در آستانه دیدار فینال جام‌جهانی‌بهترین غذاها رو برای بازیکنان درست کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25994" target="_blank">📅 17:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25993">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpUlObm4tESz_9HVKbzgpITykr9IxfGVaC3XCZ_JFIQaE3EmAZKrBc14fNti_g54cJe8Q9BpfkrSG1p2D-NaUdSWnLiN5SreaaWW98cGd4TBCK5RMyZzEwqC_l66QEM_GtyB1nba1PXUSygVBeouJTDPJu5L47CzyYuogr4esrGZGHv1A7VlqibPtSNNHQOiTR1wupTPCPdmIMeOvtPdrFNK-iXe1YPLKTbK7ZJhdeDDDin7di4vT6DAgs46DSff3XOwLJitS9EiVZVQHdZi6_ImINwc-e6IcGINrpIS8TL0WU0GqkEcTPxat1pXhRQ13w-Wq70pwoF1H3ldaMkKVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز محمدامین کاظمیان؛ یاسین سلمانی وینگرجوان پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و از پرسپولیس جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25993" target="_blank">📅 16:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25992">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lvxl4pooKTkSA7gbdtex8bCvmWDBIiZJSQwLgzwj0j7lul5XQgOZzWCF6diiWUXKWX_o5xzswO3dGuW3PWKTb9JsfTVkGilosSqZzzrlRDgWRXCpW5AjC5hwUGWh91MandRErPFY3N53pZPeoY05NnKhHg4kFJ_kfMVa77THqXc2ar2rke7rBmrNpbfJfWzzmiVNMppL_yvjZLr0Fk57kr3Ed3lY9rKjxBvmCtWz8uVJDwUTZu8kg3iJQ-QJnMIG9YBO3aBtjmYXVsDtFDXO_Yezis5f1wRyArBagYlRIfCr5b4Bx9YCtzj9KP14wnbA3LoXXgDOiKt8fhJgO94LTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25992" target="_blank">📅 16:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25991">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cbco2Sz6fwxMD-ZMDd0TA0lu36b_Zw5gsjkD8NJH_h8DAVaFN9-OjhYZDBoEyO1HSiGIi0NIlOrRP1Gmh2iq4G6lW0Qk41XcCcCD0mXWZK_w6LX05ToqW3db528ngwHYPB4LOSWNoUOAJBCBt4cvHwGn3vH39_VhcCEQ6mb2e2xRLD__xw2gAxHjOTMQq9ljHCOUyxKKknw8b0p9wbHtutBQbkIePXEGIec3ZgaH6xaGdqFBCjxhoKXOwiao5D5m5QPzchfWJ1z7txD-YKdeoPMq-1893bzKeYkyXOvM--Y3s2P8j9diJQxO-eglst5j4uCGESj1BIzxu-ZeXVV_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ از طریق نزدیکان خودِ محمد جواد حسین نژاد درحال‌پیگیری‌هستیم‌که ببینیم طبق گفته علی‌تاجرنیا باشگاه‌استقلال‌باباشگاه ماخاچ قلعه برای گرفتن‌رضایت‌نامه به توافق کامل رسیده یا که خیر!
🔵
تااینجاش روخبرداریم‌که استقلال با حسین نژاد به توافق شخصی رسیده…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25991" target="_blank">📅 16:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25990">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqV92r6xMJNXTiqoKWKMqhMbSaXL_iyW3OuVz6669TA8Hnox8ajhgrEpYBJ7mRWqLLvePykRrq1EP-DyPKyjFvhqCqPkseFccjJ7tZ4phixmHk1NM9up4EJvNKh5z7FhMG0s8GcVqmSkXWM-iDj93EA-UqiUFlXlnGmY1b7ibKzO1c4T63rNXqva9MSJv-JO-gdHLudEfjzwFkIIW93qpzBjeD6AYgVZXuVS4REi6cLpvB8ycW1GkBJlfcAZh0VfwwWqNbcpK2eay-rRfU26Gya2DXDu71Sk5gKopA3lpFgkUjFqMATYcgJFs2VPoO1EqZ5j3QVHD08ssS5bHnaupg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25990" target="_blank">📅 15:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25989">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScqfJ9EmZmn3bZL8a4iPqvDNpNnAqN7BKPTjXulwsZu7IImnAIrqkYOILRWrwCcdzz6Q7vy53O4LzPtecHmGbShNHXhmsFfH8BXtM4hHDZQMG_7WATiMsZ5AWnPd1Dr-7zVzfe7i0q-JYJFjvFRwI65v4U5pTWGSClpPzGMtFGqGZLITFiJGfV9TT1aGF2khJ4f0NDbT7xGoNQbA1G39XTFDQAI2V80pQXvEgzWyXEa2J0I1MG1ksrPYnv2k3hHSqJKZtV6TwLDVcFqoIjDN-EUoQpeqFbsZpq65X0cbuc0g-Fj-W2cFd__xKi_gICG0u2F7edaqesb4FFmdiO9qrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/25989" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25988">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFeNVF-rlGLrj2MkAsT0aj0IgdD-uWzdjYOqQANCQ-H8evCLaOeLRARVxULuQwvMspaTnAZ_4QC-82gu4KydCI5v8f97wlJ2hvHPILE1x4ep3ptfFNRp1Lg4_NmnVARpQqo1dXEySWLqsV3N6rTvhhbIfdl_0Oe-WJ9Dc4OJ2F4zg3_wun61KCwlxY6om1yspU3eW-aS49iqn2dCQhYZKTul-nyC104uQlbzMEI9sM_pF32DRvip35jJ8iRpmIMSproA4QyTlQSOB9YtyvNIooTOhr0PGGpGxPx_pT8baoNIL8BvqFtSblsStgSOqvmFR2Y-vzHexqWQ2rnMSlYtTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ یاسر آسانی برای فصل آینده حضور در استقلال 1.5 میلیون دلار خواسته و ازطریق‌مدیربرنامه‌خود به باشگاه استقلال گفته درصورتیکه بادرخواستش موافقت کنند حاضره قراردادش رو باآبی‌ها به‌مدت‌سه فصل تمدید کند اما در غیر این صورت ظرف 24…</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25988" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25987">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMliT-k4MxtIO_pQh6rLybmgQUqWEKGFKyOpGacYTJ-02KO76dqakA_W8WIQmDdUnQjHvpXBT0_4oJS-0Ft9mL1lQkiLbysAQzEuugsknKWra_VCuPtXwIKIm3NoIGomj-v5oDBAICg9vqZlDF-nJHm7yJ_i85w2AWs_rvwZzBeBRV73oVoE1rN2zoJ0j8lgii1tBiHUQConEluu2WDopdMc6aJLjP4bHXV1DJr1YP1ZDYGjbFP8Q-4ad8V1bcIv_6LjQD8cbiTjUJpKc2eLj2FpoiHejigvhyNlrjvGReo-TPZJ_QXnCHnDHKvptppRHWsgCWWtwExkEULdeWNYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق جدید ترین شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ظرف همین‌هفته‌از تمدیدی‌های خود یعنی روزبه چشمی، علیرضا کوشکی و محمد حسین اسلامی رونمایی‌خواهدکرد. همانطور پیش‌ترنیز خبر دادیم تمام توافقات با این 3 نفر انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25987" target="_blank">📅 15:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25986">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeXEsjmLtb2iN1HOqd0ZmlwVKBzfaAmq2O4F-0ymlKhVFC0IrjKFuTErccaRaF3gRLGh679_2XmCTTH5jbbZfJd51kB8pYrpU7CuhEsJUCq2YU5wPSfesyaN_IEcdfID-l_8jirucOyCha-XsugKIdmc3EvwE1JTlxAarUvZJC4hYPWiIT9cJhDQ4OtUBlY6K_LPa6ffRtG4vrWw2earV9TunGL7YICmkYYOG0x-_xN9W5alUaQciILRk-L0W9ECgpwavn2qQH8YpMHGaRcf2C-MsHsjFxPoWpcHQBEk_EV6JMCbUMBko4tKQww0CiIQIjf1Pgies2tQCOz5a7xO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی؛ امروز حوالی ساعت پنج عصر جلسه مهم‌سرنوشت‌سازی‌بین‌مدیران دوتیم نساجی و پرسپولیس‌برای‌انتقال دانیال ایری و کسری طاهری به این تیم دارند. طبق شنیده‌های پرشیانا احتمال اینکه این دو انتقال انجام شود بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/25986" target="_blank">📅 14:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25985">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzRCF5k7N3WjV118g7OMfsBFC1qUlywMv2tOoifM28ZAb7l1fZxlvsDjL8ugWdOfNbxjSzKx3fIhc7Es6Kp4CbNCOh1a1TI0WYzD3yc7WVTy6huSjnKVFhl6AcErLwmaRJPKsfLhhOyOfJaY7jWY3NrMh5S8nL72_YyFaWQMTqKfOMgG_7ld2dk2ragtL3HXcJymoYEhvV58umyx4D0tgstMcx98sIWSGIcrK88U4SWjpap6BRkLHGUD1PTb2X-u2hEPmMbjaLrX37irYV96nrw_EKH94injo7mzEhClnHvyKjBOnYuv0utjWLcH6nuJtPw7lu_MJkqq8gyGsFEuyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/persiana_Soccer/25985" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25984">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dz-gIZ-Hf-a__elex5GhNna3i6482seOUHPpoHvrjsXdaLuCb8OZVQl_COVa48YI5VepJvxRrEfZJIsj8erElLEN0CmNb_eBdL7EyujPodgmV7y7IZd0b0ud9F053bc1_SVJzRDmqx3gb01zwvcxB5vVPceZSi0PBCZAkE866RmaTFlAJDCKbPyrztqKkDvfTxgiR80TG2I7gKItPlQIlgkuKw0TKd_BqmZ1oQDDBFaElslOKTAjUWeFOjKvgCa0s7J_JRGS2P8D1fFSsVmCWKVgxtk8TOps7cJaDsJ9yWwvw4l6SKnEEkyHxdf-ShcuNioKoUPNIqFSLbbiu_nhSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
👤
طبق اخبار دریافتی پرسپولیس؛ کسری طاهری از مدیران‌تیم‌نساجی‌خواسته‌ که کمک کنند در همین پنجره‌باقراردادی‌قرضی همراه بابند خرید دائمی به پرسپولیس بپیوندد. زندی مدیرعامل نساجی قول داده که همکاری کند این انتقال بزودی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/persiana_Soccer/25984" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25983">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_DT_5o9doSY53Y-8RZ3JUZ0gmaCqu1nF1J-c_ol6PYPMWDXEctEAmdb6yC1Z8ovUL3nxbzt5vWNKD8ArP5XX5504jsdRE6PHBt_kDxHf9Xqv0KGhJXIBCvmcttsDzERHGcp-ZapqnjPpAsV9myF83RH4Wy8poKc0dHFfBdktvpBQPmaWS8gzm_PmX3UrkgYQh7QHLd52n8F2toMj5L3d-CDlcU6orbbtCKOgL_FODDdhPDFdOOgJaroBsZWQ1scbXNU_oOtn-MF6nDV7VtCPsapd9QrxHB6WcgAcgQnmisMhTQ6IbQh4ohvBweqn2L18AfbT-z5QEn86_WuhRCZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/25983" target="_blank">📅 13:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25982">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjNkqu1cnQNed-YdCMTGyJYhTgbe9ln9FJZ0QWbbj8Z3IwEs_VCSfoN3StmYrBFvesgA3-xkR5vSH5LhfJgYMjOJI6kbVmHCH5aUaWkxPHiBy_knHzsPEEknuSeTW3P9RLOtq5oS164AWn1HWkE5BVSAKAOSQZQe-diHn5ifPN1-w60qU8tOZI73wzltyLekx80_x_02FwvN0bY3P6Tc7mVNYRzZcIKPtGJ6oL_l2vbykyPB0exWP4azMnk_Nk5a-nXJGxOhnFLry2n-WuoYonPpaG06BF1gqV0Jwt3gR4mEcJHP4qaa8QDwDDmj8gOsUMcFdaD66lO4O7bxShosmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ تاجرنیا رئیس‌هیات‌مدیره استقلال: مابامحمدجواد حسین نژاد و باشگاه ماخاچ قلعه برای جذب این‌بازیکن به توافق کامل رسیده‌ایم و بزودی با حسین نژاد قراردادی چهار ساله امضا خواهیم کرد.
🔵
علی تاجرنیا نیز اعلام کرد که تکلیف نهایی پنجره نقل‌وانتقالاتی دوشنبه‌رسمامشخص…</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/persiana_Soccer/25982" target="_blank">📅 13:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25981">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uqs1wAW_CqVv2o_zMV31p8gcqDisPcLYpzvKjBdVNcRuFRdoOuiXi4mcUrqJDdqI_gkT6H8cAkdbYrtcJC3ECJndoukjfzYgImPHookeCB88ZcH8K4xg0xDMPMMC4c75t4yihnAiNKWFra6Q-NYTmexjpeq2TKXJc8WFqxOffmnyH4v2_WFegMx82-kb9_ZfsEfqFqJIQlKOj_i2HM5Q3ckv9yhcJhzBQDJDDaqaZrlrKVI0AeXJyNneF-KtemlAJem9ILP7oHcXTzOy0isqh_lqHXZn-ZgLiFPBa2KuQirJSIUepgSwFYfv7AA93G9cpm31navns3j4_Lsu6p9oQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/persiana_Soccer/25981" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
