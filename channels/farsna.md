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
<img src="https://cdn4.telesco.pe/file/tL4PrONFlb9XBXACl9nhLr6KAzjkq6VCdCCkcH7jOlK7icl5eRQa78Z9nIl2G9gvgWy5_xUqDwZErEjdZsklDz0_FvQZVJ6yHhbUIdlj91nkMx22XFoJQVKLlDsJc2uRBvOB2VGvvUALYVgOmYu1BKJmkToFem09mWDk_5qaGLN5VxC-bJ9OB6-CdpZMCdI9tPgDgnxtVLLESlmr3_NiTjrnOFlWforThTjZzd_24Xdj7P3riy7xuKfuNfO7t7daAEPcFPzUrruWKnyIgq1ZfQ66h7koA5N_RXI4V1KZeMNdXB_6HOHPrYy5kcRSsrJEEZJECysWtp43X5O8Dn_XiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 04:01:21</div>
<hr>

<div class="tg-post" id="msg-460604">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌ خاطرۀ برادر همسر رهبر انقلاب، از تولد اولین فرزند ایشان
🔹
فریدالدین حداد عادل: برای به دنیا آمدن اولین فرزندشان در بیمارستان رسالت، چون ملبس نیامده بود، کاپشنی که مادرم برایمان آورده بود را پوشیده بود. جفتمان شبیه به هم شده بودیم.
🔹
ایشان وقتی در بیمارستان…</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/farsna/460604" target="_blank">📅 03:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460603">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌ المیادین: ساختمانی که دقایقی پیش از سوی رژیم اشغالگر اسرائیل تهدید به حمله شده بود، مورد هدف واقع شد.   @Farsna</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/farsna/460603" target="_blank">📅 03:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460602">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌ اعلام حملۀ هوایی اسرائیل به جنوب لبنان؛ صدور دستور تخلیه برای ساختمانی در نبطیه
🔹
ارتش رژیم صهیونیستی برای چندین ساختمان در منطقۀ دیرالزهرانی در جنوب لبنان، هشدار تخلیۀ فوری صادر کرد.  @Farsna</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/460602" target="_blank">📅 03:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460601">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ادامۀ جنایات اسرائیل در غزه و لبنان
🔹
منابع محلی از تداوم حملات وحشیانۀ رژیم صهیونیستی به مناطق مختلفی در جنوب لبنان، و همچنین نوار غزه خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/farsna/460601" target="_blank">📅 03:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460600">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnNB9p4CVFxhVy2IDeFRmaQAEqSEz5N6gR5LgquNI4gzg0LUjqn4zNsB_WECHzuwtFgmUu8p1A8JRu5Bj3FhOwb0oPnwQFCQ0viVzeDRj2DiOgAWE4j7_QAgwRMWrKabpwh4c-Tjp1uVtHlfJbMF1WkKUFteAFu1yg7f_yUWDzLB27lMULPNDd1P4-xar8rKas6RMB3GcG_cBv93jZvsUJ_jN5PXjhLgpwlGVUFDbs6_c9GbW3VUmMxgYTVm8bXdByMlQTux9FPtN7MBMdH1xADDTqL7DLSZFXXGm8Waibz5CE0ofaYVVQO3RRm-0f8ZrGK5Zmn2s0QRtTZdonynXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنجیرۀ «پاسخ هسته‌ای کرۀشمالی» مجهزتر شد
🔹
رهبر کرۀ‌شمالی در مراسم آب‌اندازی و ورود رسمی ناوشکن جدید این کشور گفت که این ناوشکن بخشی از سامانۀ پاسخ هسته‌ای پیونگ‌یانگ خواهد بود و می‌تواند حملات تلافی‌جویانه «ویرانگر» انجام دهد و استقرار این ناو در آب‌های شرقی شبه‌جزیرۀ کره، پیام روشنی برای دشمنان پیونگ‌یانگ دارد.
🔹
رهبر کرۀشمالی همچنین اعلام کرد که طی هشت ماه آینده مرحلۀ دیگری از تقویت توان دریایی خود را به نمایش خواهد گذاشت.
🔹
کیم همچنین از ادامۀ ساخت پایگاه‌های دریایی در سواحل شرقی کره شمالی خبر داد و گفت این کشور قصد دارد یگان‌های جدید دریایی ایجاد کرده و انواع مختلفی از ناوهای جنگی را تولید کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/460600" target="_blank">📅 03:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460599">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39055cd071.mp4?token=fteVMwln9fB1baOpbt_orgpWFCMHvgpR6k-082L8Hl3RXzICDvE9aiOuAPcVSUyT-TwB4NM9X2TQnw-MjUFjQDB_8ApC_vNAhcuj4dH1_v1QdtirNnSWfyPgxngufoBt-_SC0yeIKZr2wWUQ4uVRKRP_blFiwuO-VCcyRUCMiYkKnEEHh3mlvtds0czR7C4oZsMCVVX3_LFhcy7Zgb5OB88aJ83BPadySPkYv5qrju034M30qXZZ9AxkNatF-n1sp3hyEl9jRpWVopofoMyp3bZ6uiHWh1fDH-HizOdaIB6ABBUvJgspDDwKG_EOuEWvOhoKf4vaXolTTUp2Aerx-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39055cd071.mp4?token=fteVMwln9fB1baOpbt_orgpWFCMHvgpR6k-082L8Hl3RXzICDvE9aiOuAPcVSUyT-TwB4NM9X2TQnw-MjUFjQDB_8ApC_vNAhcuj4dH1_v1QdtirNnSWfyPgxngufoBt-_SC0yeIKZr2wWUQ4uVRKRP_blFiwuO-VCcyRUCMiYkKnEEHh3mlvtds0czR7C4oZsMCVVX3_LFhcy7Zgb5OB88aJ83BPadySPkYv5qrju034M30qXZZ9AxkNatF-n1sp3hyEl9jRpWVopofoMyp3bZ6uiHWh1fDH-HizOdaIB6ABBUvJgspDDwKG_EOuEWvOhoKf4vaXolTTUp2Aerx-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر شهید مدافع امنیت در تنکابن
◾️
شهید امیرحسین سلیم‌زاده در حملۀ دشمن خبیث آمریکایی به خوزستان به شهادت رسیده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/farsna/460599" target="_blank">📅 02:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460598">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">روایت فریدالدین حداد عادل از زندگی و شخصیت رهبر انقلاب
🔹
برادر همسر رهبر انقلاب: زندگی آقا مجتبی بسیار طلبگی و ساده است. در قم که بودند، خانۀ ساده و وسایل محدودی داشتند. کف خانه هم تنها با موکت مفروش بود. وقتی هم که برگشتند به تهران، رفتند و در یک خانۀ ۷۰،…</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/460598" target="_blank">📅 02:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460597">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ادامۀ جنایات اسرائیل در غزه و لبنان
🔹
منابع محلی از تداوم حملات وحشیانۀ رژیم صهیونیستی به مناطق مختلفی در جنوب لبنان، و همچنین نوار غزه خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/farsna/460597" target="_blank">📅 02:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460592">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVfk1eWYYiRwyYoCZ-uLtRKFum3r37QV6Y40qBClt-6W5DXUzlMmd2w9QwH8Jq069BAoXhIUHJsCg-oMCwRQ3D18ZhTuAAMlO_QMIs3_e1ZhB0NwMmDAe97oAfaXM1Rur2zBh39TIBWQsdcjjTZWZf3kS-kVXw38qZszggRj9a2YttrMoYWcuQtmSJtQTwwUgF7iDnSXmYa7Ib1O-AQBAsvuzlvy3E3KOsIwemjlPTvDyjRrHE-q5Ne4RMGeHDcNoEI6jpJLzx8ThNitHa0WOWyLjYTYVW0tYMLaM1BH2YFt8RrhzpfroAmhsNGRxk7kfC1xQu5gE-QjMeiUHqV5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vH9OYvtLnixX4Kj-PgypmXFufnzvgb9qsuQ5IXGVskkORJG_I0c8FX5hKidsGMALFe9SMCNZSCiAI47gHT7gCWL06PzB-Ot_Mp4nSdsreNY0ZIKB-0oIpxAhrUeICsJgdOfhNb10RqFCTxhhgq7FB8gTldw7KG36sfaIiJXYltZM3ETqFWH5U7BCDf3pUr5P2IVUhnXXQWbRXVlmKAkLw_yVQtdF0XbwNtugMKswTJiRaLY3hdg5pplXJVgZHUqf6XriBib2l789TJyeOkpSHcyKYkxhkBl3pa2szp67osFsnzJOGN1_n_UEUiKqslQgEQ8HaCvTGG66NevDOyvC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fOg02nyykBdYZp9zZOAeJEI_8d-BJsWRRX0WejROhojjOJ7yseXvBiOjmGomWf14Gjxs90OcSE4ulvbrJghsSdDROC7YhLKF4bIDNN60UVSWLcakzc9crXeYFQB-l0Lyc1Kekl-dO5bHTV2hwg9MkgiIUGOTvA1Z3myTNtvEC73D4a91JdUxLuZppRO9u7Iw4BrySehHSv64iG15wxqaGDF3hWBTjhpstGcv7Y__5pXKUukqe-auz9pxuyU3BIaJTeQ9SJos_XhF3uysQ4Mn3wt-RR8B9FgafSvmDoORiGQyLjJWjtPRXfogCIGnkWf7ZFsvpKBeDJoCuXMShO3G1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqsqeSxaQ67FskSiOgmLFbE-oXcGYxR5OvVnEwouLUQDhmE3BiLrh6Zgtpy6M-X8qcnyC4ueuBDOnu12V2iZZbzOtKMtcX6mfo68QJmIUzbklmwXbJ0OylE-fPLU4HXumZh0Q9ospcw28FQWSXh1yWsLhhQ-_B42y_3qAsgdjxXGgS6bqy1lOcY9ssHtrLlqvZSg9R7khN49cVZk06ob3fOByjJtObCGNrT-HBd8JOPhN1C4OeC3O7g5gh2VH1B57BP_B192W65WhzD54wa6ekfQ1pNosHgujKDme8zXiWFRCd9LNaID0FcGKO7aqCDB6DFPHrOJNils-iecswiU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2lhY0St5I-BTRLGqrVjgyinBOOdwBGqcRb8bC0fJZdsvR33LaKT5yGfJSvw9REYZS2Po2Sw7ULoIx0AId1sAB9scsnAB5crU1-fjbfLnlvlJ8k0KO2C5lHJqCRUKcPwxXkOfXV2HIq5QwKJNF_Th8ZKG4987xjv7cxwwGxB6N2Lxqa2Lb38Rn8xCfquohFbfbMIkEpZ7rHRYILeWUE2pHTumtCVecwiGJZ8uqCvQqls_0BC9wDAmC2l_oSm3444H8PJYFGk-2OStsG9HwkQYUwUhMpFsnSPvog0FKeKRTcKgCbe2YyanblaXSALanjR5d6gjQ1kqfwjLFgDEHkJ-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
قطعات موشک به‌جا مانده از جنایت آمریکا در عروسی سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/460592" target="_blank">📅 02:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460591">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">روایت فریدالدین حداد عادل از زندگی و شخصیت رهبر انقلاب
🔹
برادر همسر رهبر انقلاب: زندگی آقا مجتبی بسیار طلبگی و ساده است. در قم که بودند، خانۀ ساده و وسایل محدودی داشتند. کف خانه هم تنها با موکت مفروش بود. وقتی هم که برگشتند به تهران، رفتند و در یک خانۀ ۷۰، ۸۰ متری ساکن شدند.
🔹
خواهرم در مدرسه کار می‌کرد و خردخرد فرش ماشینی و مبل راحتی تهیه کرد. مبل سبزرنگی بود. با شوخی به خواهرم می‌گفتم آخر این چه رنگی است گرفته‌ای؟! و این‌طور سر به سرش می‌گذاشتم.
🔹
یک بار خواهر بزرگ‌ترم گفت: فرید! دربارۀ این مبل حرف نزن! زهرا بعد از مدت‌ها پول جمع کرده مبل خریده و تو مدام به رنگش گیر می‌دهی، او هم اذیت می‌شود. قبول کردم.
🔹
حالا بعد از بمباران، این مبل بزرگ‌ترین چیزی است که از آن خانه باقی مانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/460591" target="_blank">📅 01:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460590">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌ المیادین: در اثر تجاوزات رژیم صهیونیستی به نوار غزه، از بامداد امروز ۴ شهید از جمله دو کودک به شهادت رسیده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/460590" target="_blank">📅 01:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460589">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=AIzk9VmLravLyafOXpwuQCvmeyFDjoMdL5k3hW5FOwBopc4gDJULI73nIe1KfImKK1WLCmi20GDAWRe4Ofv0Xu7is68I66ySt38cEANvlQBYLijs1Pph-QqmegqLvSgb42ILZtHWeW-NCiGhycDM2WAexg0_qBntmWBX6KypZE_pygLlXljUo-Xx68pc58m3w5VAtlUusue7BQWL6R2Djoly2N3awrJvj6326BXnOkcKEAjvX6SNXCxvD7a0sq406fbkjSzTekJxuA7yk9Gdenxr7Em0Onm4XmkxjfRogAedUW4iXTLZJFLQJI9ZHLQ9HDsGbEwISoeazMqdoSD0pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=AIzk9VmLravLyafOXpwuQCvmeyFDjoMdL5k3hW5FOwBopc4gDJULI73nIe1KfImKK1WLCmi20GDAWRe4Ofv0Xu7is68I66ySt38cEANvlQBYLijs1Pph-QqmegqLvSgb42ILZtHWeW-NCiGhycDM2WAexg0_qBntmWBX6KypZE_pygLlXljUo-Xx68pc58m3w5VAtlUusue7BQWL6R2Djoly2N3awrJvj6326BXnOkcKEAjvX6SNXCxvD7a0sq406fbkjSzTekJxuA7yk9Gdenxr7Em0Onm4XmkxjfRogAedUW4iXTLZJFLQJI9ZHLQ9HDsGbEwISoeazMqdoSD0pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهران رجبی: حضور در تجمعات شبانه وظیفۀ ملی، دینی، دنیایی و اخروی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/460589" target="_blank">📅 01:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460588">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Do9w_K_5pu3Uzy7TOlM52mOxoXFlEfxs_s8xyxA5mvVmiewMnswT1Y8HKk-2DyTtlO_q_uJEL4WJkMdXrb5TyljCr9HRB3-KKCN60d1EqC7C_-JCXdx54LdckFeNn9rzs0JnxaSFNd4YjpcDmwejKRBpV8UxsSNi0h0kNtn826Xm4bCzDFUROD8o8eKIAkxYQaTdMj6nacQs27CiVOk_U9ManaP_plz-evPHTB57Phv25JnJVzWkVHJmsbG_eeXBM7dAlwTNK9nM79vk_WMY7dcvRvvDsg1pxl2xUihUmOd3iJMhFZwXeYJR_pV5mI-1quvI4cG-REPDZAMaXbnCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سانحهٔ هوایی در آمریکا؛ ستون عظیم دود در آسمان میامی
🔹
پلیس و واحدهای آتش‌نشانی میامی پس از سقوط یک هواپیمای ۷۶۷ پرایم ایر در فرودگاه بین‌المللی میامی به منطقه اعزام شده‌اند.
🔹
گزارش‌ها حاکی از آن است که این هواپیمای باری امروز بعدازظهر به وقت محلی از باند…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/460588" target="_blank">📅 01:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460587">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyKuI-dtBRa8IZ_mmOg7D5xNO1tJ6ZDkBb9ajrTRd3LmPtLjdP7LS6YhT1tb3K5pOxv8lpI_g9zV100NhKnFz9E6CL4uODSq3435uvTw8A37N2lYfu1VOfS8dTL4q96uxb-fO3UpKU86jKl1s9YaeLudf090XzfxyyLxJYTu5I90XiW9nyumKzL_B-uv--h96AbYBAeJ0PwefIx_T-tChDZggMUoAundiJ0u4PQaQUWUX0OAO21pAa56s8OfNEIzo4hQ-b96HeYlMS0H29TrBONAuq1aYje-sQk2RP-08b24lfeg09nyEmDVrY_FOEm25RFQJ3XKq4onUrE2n-Ep7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: اقدامات تجاوزکارانۀ آمریکا عامل ناامنی در تنگۀ هرمز و اختلال در کشتیرانی تجاری بین‌المللی است
🔹
سخنگوی وزارت خارجه: تنگۀ هرمز تا پیش از ۲۸ فوریه که آمریکا و رژیم صهیونیستی به ایران حمله‌ور شدند کاملا باز بود. واشنگتن جنگی غیرقانونی و وحشیانه بر منطقۀ ما تحمیل کرد و جریان عادی کشتیرانی را مختل نمود. نفت‌کش‌ها متوقف مانده‌اند، تجارت مختل شده و بهای انرژی سیری صعودی پیدا کرده است.
🔹
اکنون واشنگتن تقلا می‌کند ایران را عامل این اخلال و ناامنی که آمریکا خود مسببش بوده است معرفی کند و کل دنیا را مجبور به پرداخت هزینه‌های گزاف اقدامات غیرقانونی‌اش نماید.
🔹
براساس روایت واشنگتن، جنگی که آمریکا آغاز کرده باید به نحوی وارونه به‌عنوان هزینۀ رفتار ایران برای جهان قاب‌بندی شود.
🔹
آمریکا جنگ را آغاز کرده، اما انتظار دارد تمام جهان هزینۀ آن را بپردازد و همزمان ایران را مسبب آشوبی جلوه می‌دهد که خود عامل آن است.
🔹
این وارونه‌نمایی، به‌غایت بی‌معنا و بی‌اساس است!
@Farsna</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/460587" target="_blank">📅 01:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460586">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ9cDXa5Lo6RxsNpW7312u4gjH1AdU56nepEpQLH8ha-JMaw1a-dOMellqKd3xWWtG3-9RKjTeEKATxM5WAIuNTU_2gmrsjEBtP14qEsIkMTIeVq7OYsEadR3Y5O502PTKzMNM_jf1sznJ-B_syx16iRbnphBvu0DZ643wBbwSzs0wqOT2r5e1HnM6QPMqKzkNLQ_Riw-N2m0mu-rYdRoNHY_Mzu1dnX95nKo7JaeOz9FYQ_HqHrd61-8oCwwixeSAobcr7HYvE6FcVXQc0So8xTta06G8T0DW582In1zaanPj5YVJ8qVFbUGaBeY7MCmVKt82x4E-VmgAN3yVhBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«پینوکیو» فرماندۀ جنگ اقتصادی علیه ایران
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا فرماندۀ جنگ اقتصادی علیه ایران است. او در هفته‌های اخیر عملیات روانی را کلید زده و گفته‌هایی نظیر «افزایش صف بنزین در ایران» «رسیدن دلار در ایران به ۳۰۰ هزار تومان» و «تمام شدن نفت روی آب ایران» مطرح کرده است.
🔹
با این‌حال افکار عمومی در آمریکا و رسانه‌های رسمی او را یک دروغ‌گو می‌خوانند و معتقدند او دست پینوکیو را از پشت بسته است!
🔹
معرفی خود به عنوان کشاورز، ادعای سقوط قیمت نفت به ۴۰ دلار، و ادعای عبور ۱۳۰ میلیون بشکه نفت از تنگۀ هرمز، تنها نمونه‌هایی از دروغ‌ها و ادعاهای اسکات بسنت است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/460586" target="_blank">📅 01:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460580">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/di4ixeGzX4-SDdNtjXBAdY3kBBxtJv5XPIYsNyMxQ7_BQ0aO8KvKAK3D2bkQPfSha57-mQ9iFM6OFXXjmBLPbAGYANw6-isftbAaJ-DL4leKyZiXA_KIW-fI09KaSnK1olE2SiDN-fEoBszo3LVRxcoBJaTmDr-akhvVgZ999iH3316mq9Rk5POvLdFRounCNn4wZwlHG5MxYOSpjHtZOVpjLe-zSmXI8kIcamk6F2L3rZzFkOxRa-AoKbHx26jcU_-x0ASMCw5FZW2ZPCnTsbjqXZq53Q1IaEHQXjGuhYIpiWFALwSA4bp-Yy4faXMNuEQ1HicMvywex8TfDCg1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROFQIpRPPeruoUwLV9zgjbWtmx6TdiearridvIxy486kInjMY8quM-1ZTey_xL9yWME7diMOfJhaBww43YZdf9KyJRmMmwQxe1nHsh0-AWbjJW_3NwhHbtGevmEWi6ScsGqX1giZEOerqb_fpG6lJ3e6inPeSqe_g6f2mlyCZNuwTpXt252zfOURnt3l_4pjdCwHeJEQ44AwxHnOc6HhqDnYBcuamNyVS2K9N5fpHaOSDnNvNae0FlVIBkmHuGsRS0_VnGIqA9f8kXHrCn9KnSwMcqEFlSet2BzNotqd42coTtaCDBiE9A3LDi65UuWmEVcNgyzZkkABnr9DUKz4Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9UKf9yhbOYUGdKOd5NIOYUpIMIaLJtk9RbAP8x4gEwtVGmjK6H6bgsWGZ9jQLY7zMZWlMOAnsYCBq-mp1-O68WzZwcIZUSO-ApzPcN7WZrq4ACXk4N99tmvb4xbh3UC6l1QDSwpf5EPLrH4UnieVv1eX0-oiANimPcvryvARDNhCqDRBst4yncgI00X3YuamTHfNwJU6AUllCgTiohhBfFPlFKAOs4SjEjrD-2TQ4xkf5ZyuGl1voPXxZ0ARDuGkAEEUROPCOI0QXrZSyWeGyRYymf6sCRDsrLAlAJoyP6muOYjXSDdw0ph_cBmYe5j45sVgHqR26aOOeDTBAvEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjzcLxA9TqEKoexB4HaO_-8P7cMyDan_lNPM2R6LVCGP_PzIlP3WL5cxl_ZyEQKUzxRzbakEJe-XzOBmM-BBVxqc4Uy_p-5ZtHZsyNNyF3UmOBQcPXZHV3dt231K44IePeUX7isP0FvoGWJ-ig4weBbcgC6QZl9oh8MKFiyqE0tI3PeAWVoxM49U8MKwbaTeFjt4Az4NHR98vDY8JFzZZ7kiA6V5IWLmuIqkngbR_LZUf8iR2Q-hU8HQ4ASuNJNSZ5tsdL1KIOj1NK7vc495umo7Kp-KHeXY2YNdzEgbXILAdiI_vYI0IRnuCMB7Z18OIQz5HqxmsgtDLtB4V26M6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWWhSo6GhoNNbTxqFphkqdkKYt6p1qwM1dfeKoLkPSl9ydfc9QnKZDasjWJJNVEMOxxZQGs5yG5ZcBINwsDfWsmnevYpeT0KzHNYDK4f_mbRwQdteccUiolhVvhl0KVhDRUjl0gw4-PLkEr315yeQ0sWvvEUF7Fg0JKfopW7jnt82AEuNKGa5jRGP7B8Z_V5NZT1vDAA-dVjWrNHNe4iIrxH15s_C3Mzndp73wheNfga8WmWQBGXCne7p5h18eWb_DuUDoMdmG9Obh667eWovOoIq6NEpBG1sr__5seT2niv0mROzs-1KL8B5L6F9v1NgVbG0BTOiAtupmKpTmcNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTf0cxIPje-5GfUSWfQo239jfnb0AP74QA8ZCvxC9z0Uk9cQR6Mf53FIqclpUE4uYGiLffIcD0OE0ImJH3H3jVQFEvFouqJVxbG-GJ9dPIDByBge_QN3MEqNxwP86il3WndBMZnPVWs94ta1I6hGzHn7ZaiOCVtt7un9aXdunpS27n3z-yqDMdAL8qFluvfFqvisZtUGhoccZh35CtuiJRWrzv87vC_W993cM70Onx2_Xg2cmnMsUWhO4fW050EYCzvslpMLwE6IFhK42y8FPQUpwhHgF1-y7JzHffTCkkaXPRAJ5_dLQOc6NC1dQu9d6cQUNV5rqLTQ2aj7a-oybQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱۶ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/460580" target="_blank">📅 01:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460570">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WibLpB6MSifJh97u4qRWfDThb44K6l0a3PZF78ikL9GnxtbvsbxEvLKBT-Uvm5Co2gbGFAcWIf802p77ifQuAZqmE61s6anpstfQUZnciAgajk1sAy63pL6kOIMDqQBozY2n6Rk5h0eY-EsXMn-yO5Z9x9PPJS8JXIecsWwuJvb8HPydXxgW3891RPOv0AHPEFtG6ZVsae-yRxPK3XUQYmcNwEDpKMtHpPEOV_Wd39AJS2TC4CPxamjp-colhpwcsboAqtjbVAxOr1Ehhc-YFUYGc2OpiCZBykBiceByKDlQYKaU0IGdsuykxNEkhSqGF4u0Ree5i8rDemVELBalTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSzdFv-mWJf3kVQQ6sxh8u6kvrGK3DY3yKSKLb0rn3m3w2StUPhBQqajKJ0HJX-tMeLZw80_1a-sGziaY7UaR0vBk7pfI6L2cbg76ZBWLkwI5MLbzJ-BjbNwFYnswpu9S3psL74a3s1zNJcWqEvQ2Q66lWxdDCXwDCGfUIzYUJOhqkGxTSjJcWis9eB7aFMyn3EbV6XtITw88YN2GnCBTpkUjYYKeMaNd7aFfsF8JHfirk9hnJHtBUENRIzy9590HRicN_LV_nGf3NR5_MN1M8dMF5bEwBTX8I-boW79KFst1RoAp8Peo5h44DVseFNe2I2WGCX9hh3eL_mbWxfPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B142DOhiZbvEUWFpOwOHKFaAcNIdrFEbVCndrhYrThTkFRmaUfydSVLyvEifEdWL5iCNn75HTDpVJ7SHX5-FztcQIEGT56nX_pLnA9bdUfuVWQ0iE58hyfgNj9fugbdHbxtUPcrFRMulHzozg3OvJM4LHl7aCiw7_wJvya-QqqnGAMkJQOh906nKmzJC0isfNzb7xjSwNueeEABsm1fK11Eq1LO7c-NNA-ftzMv4V-Ftsc0B9YFcm1YS3cuSmaRa-kKCURMaH74dpQBsEk9dzgDWtns3GBYFhFCYFaV43ZHJVXiEtFcCQdLl-cy2T2o9fhL-eZ8ArXh8lfWaSYU74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkOAbb1eL09f_iFIawtMonCzfDiadUsitad5NZQknAyKnFMx7FjTngYgyuzpTLyzlDbnsnYzNTvEJyyE616i0moeNIxeZdXuumZUVMGclnBDLYbPKKb5D6Eythh8ZTnt_vGy246djsikWpRUOvImdb2YCCxd_aA08HUqgLExPd9cw8eNT-YpWEihp5D0hcVbmIlfpUK98J70-TIqEj8mtxOhALi_8jOFVRbzuK_aEZ-NRdd_7YxuEQ9lzt2dzMUMrAdLqlZniYLV48khhA4zAMjMKjG-l_unHrGTDtufJyJ0Buo3HAEHMuyf20Zpa2mCNCaAlLuE7xGwtFrYV-K4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWrpS35gqRBPFpZ87xLOoUC5XZmuukEGOCt_eY63FBZ_VEEk5hh6DtYGs_p_NziC0DeLlPC5AzLjnlBXKww8uzSWlVU0kfbWLGNXQFp2AfmGAzhFMPndR-x9-BaKEtr7fwbEDundF2Hin5N3qyvopjVpqgdYdQ5Sw_oB97muH5l2hk-uH-L9_1goGUm44z4zGhbCS60lAGdvTDxvFWydxGv8-IdggeYuRNwSV07o-J87IY1hhGl7hVEdiZqYOqF4PDWCboabgUkzjhkF-bTM_VKijbIsbl8jQZLvy2Tctpqg_QZpU0jhLGyE8p2c9xHY8NBoIhfX5X_XHGCdciAT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbLPQ6SVjLGHwiQJwfjl3XSJVKP2yhHyI-dBN6WYGaXvB4fN8sKLebDrIvuEjqMIfhEBYvrnevstm_p9iAbKzblyBZetsRcD5crgL_G3cRZtKybbmHs4RnRsdsKP4ZkdZLpfMzWLt8DziMP_iKaj-kby_VCXORW6auTvMQV5RG99gpyXfRa9ahUyX-YNN6VU7Ht0BfmmbnurDGH_RVdJXyAUvJK2Trs_Gv6YDt26UhBt0U0s81qsz4HeJHh71NokshnI6ln3-k-TJlahUHCstO8O3oOFQLckCpx0Pf_SSBMtwGnhwHGH1Ma3yG1HEQU4YJXcjwwz8S6ySu2_kMyx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSvM3DlrIhvUAa2rtjsvndwJzFO6WvI9W-uCu7s-J5ROC2FX40FrsbN5z-raTc91W83DeJze6RXQSLpEpWqNZNT-MnKcdoMo7Ieeu8TeyAR7t2sDEC24m7nQO7FGkQjtPyQ85ojGDflLkOuX0dv9oTM4h75PaHHHjUBa3CHH16Uwq51TY6MAq3gQJrWuhfFKQop-yPDScsnIJ5BsqrGPtB6V_royMB4OHr6Fz_-GBni2hotw2zthLUyxn9DqdTvKFrJssmXiDWTZFei6wUPMiINJq0ZaqazN6ljkEJdWj3g3tDso5WQvfUGoG53aPDQ0PAAZod5uJ_CzbkuErqSl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIBcvI-D0PwygkD1Hy10RVAoKqDqUikcEfb72tqckM_lf0zRGDCI5RlEHo3_5DQxNe6Kb8QGqYX4YSQOijlaiXa6tKyGl3ON--7rLv8CQMHn-aSGn6fHTjjzfj3ikeFe0U8eB656ut_PI8_EG5Z8kyTbf-yb0JqrpPqUxtpuNXMvx8EvPZpJfU6GIJe5Sxu01FfmaD2dkWdC0B2XTiA5Phb3sXt6oRLmx8plYnsqxiwJsfwR0FaeL2YkHZV1kr6Tq7BcLdVoKIXnRJ215Y0__0bz0_NN2klknhABZopD0whTXn9CoQgTA4CZG-AokXQ3gXtkzVz9zfesaP8FTOTooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0vo_et-2KUfAzlDZWCYzHAziW28PVQKFLFSvy0x9onpFgI4aRtUlG3clEr7tGMx_ltn6D18MpFYNy-Az9ugrTQbpSJ69mg87XPx3oVeJujrNQCeBrMhnXKQOOvgKs2NkpBJ1olSIL6ZM9SMC3nQCfww6gwoJFWvKWl2UJJwvh6XthDdgKr9Pqpf9OcgWFmxI5A7H441dbkx7SnJCiqM15HScZb3Kutc5HtpoZWXxgxEX1lbccO5D5M90I_Wf_DeEuDfcNKpUZmuRIJAeIO052UeRGNGdexIr4WkdFjbzJ3upDJ1LLwWpVBcRfOkqWvZykfIKkGEuoF0IiVodQoUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akPSPeJWgQ6yxVbDw1efjI-T_jwTa1l__GMivF62W3YRjSkpHnB2BMQHGxzxXvBkEoor7e9ZJrkq7wHnQch99SFBCNRa0LiKdlqKWSIn3sksCFu4etvhrz0YmpDvJHxAmeRIfHx74WKRNPrfIa7niDXFydNiqCCnrPyFSyqTnRtOC02bX7AdimXbHSbkN9JvD97pMfXD3B6n1WZhJNhYVof7KdcRvvvMmYN8z8j-Jn189qBOVYkvM1ovdr1Qg0fxC7J6ESNzz2VFxsZ__AMpGUccSLwIoeZGS4Cn8-E7qUkGVJBtbJgCfUnp0yrn2OD3EcIE0ysn8tBmkN-MxtvEnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farsna/460570" target="_blank">📅 00:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460569">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">زلزلۀ سیاسی در آلمان؛ پیروزی چشمگیر راست‌های افراطی در انتخابات ایالتی
🔹
برای اولین‌بار از زمان جنگ جهانی دوم و سقوط نازی‌ها، یک حزب راست‌گرای افراطی در انتخابات آلمان به یک پیروزی مهم دست یافت.
🔹
برآوردهای جدید حاکی از آن است، حزب راست افراطی آلترناتیو برای آلمان (AFD) با کسب ۴۴ درصد آرا همچنان با فاصلۀ زیاد در صدر قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/460569" target="_blank">📅 00:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460568">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در پی حملۀ هوایی اسرائیل به محلۀ الرمال واقع در غرب شهر غزه، تاکنون یک نفر شهید و چندین تن دیگر مجروح شدند.  @Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/460568" target="_blank">📅 00:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460567">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a393542d86.mp4?token=dG4r0SuNIJO_QMX1MHJZd6b3dZ3IAFFnJvA_gjnx7OgekvjdQk9Sz8TxRsn-erArLhDuQ5J2X5ITKk1ZLw_Byd9FvR4edBgTaRrpQ_Hj5RILrX6tHSkAlNnRjnztWkcffgIM1yGZ6eD0HqzxHeKkNp2jquumFHTmbjxXOl-8xUbvQEOArGy8VjBoSgIG8cRWB2H5-2iAxEGlnpTOWzHdhGQOMRTzkmPsuoft2dfXYg-4c72mHGkacO1xWb0XSny4KWbOAOZfItMMis9xNrAKpvlNIJX-iVzvIDWNHEpx1E4Z3SIFSolEBCmfQQsKfReiTc1-d3Gdq2vu4lUOZ9FD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a393542d86.mp4?token=dG4r0SuNIJO_QMX1MHJZd6b3dZ3IAFFnJvA_gjnx7OgekvjdQk9Sz8TxRsn-erArLhDuQ5J2X5ITKk1ZLw_Byd9FvR4edBgTaRrpQ_Hj5RILrX6tHSkAlNnRjnztWkcffgIM1yGZ6eD0HqzxHeKkNp2jquumFHTmbjxXOl-8xUbvQEOArGy8VjBoSgIG8cRWB2H5-2iAxEGlnpTOWzHdhGQOMRTzkmPsuoft2dfXYg-4c72mHGkacO1xWb0XSny4KWbOAOZfItMMis9xNrAKpvlNIJX-iVzvIDWNHEpx1E4Z3SIFSolEBCmfQQsKfReiTc1-d3Gdq2vu4lUOZ9FD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرایان در ۱۹۰مین شب، روایتگر تداوم حضور مردم شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/460567" target="_blank">📅 00:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460566">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در پی حملۀ هوایی اسرائیل به محلۀ الرمال واقع در غرب شهر غزه، تاکنون یک نفر شهید و چندین تن دیگر مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/460566" target="_blank">📅 00:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460565">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80db7c1466.mp4?token=jpEuxJdntwjHP7Cbxn26k-PVjJYL-Y10lwaa0eB6d1jaY2o2oN6TCg7tgyIt3L6pFpm5zbJaEY6zWLYnDvxkNcKDJZJ1rE6GCuNvh9oGTLJaNdL_AgN1THsp4Krjn4oOAGSWvj5KiLKxy6KBYugKAiL5NdUAUtgX-dI1UhzGITanchExBFxBNYolE7zxaoMLZEWGiiCz3UpU4F58iIGfjORQL8BeJbaxBWS3vCRAVCJzp9gTJUpI_ROxiqMDA1hM1OmbJxzsEjSO7XsFdlDJYdIQSsjZPf9BTZ83LInqC4tn_yPtSN6fFjReQQFyiVlfQD3Z5JYujgy_4BUjWOYKHGI3xBTRTYi5BL33S_bj6oDZ7ln3ZL0VXEhLSGc9Jmo_DdlOw4UO8AR1fC60jV5KvNftbsYZy82--XKN9x0sfH9DJkyK6kwByDhVmZxtDm1nSJM1S9-kshabTLgqVhgq8CyMkk-gyrnUKVXY8DEfeDZ_0ctlwRPXBDQvOocAeMRv-ouC8t3QBnJHwaqyhWAAfKxXQZzf19Bq2VgI4iByifA5rfIdRbc3VLOOwtxqGPvhylY_64q8VXuyKSj60KNejrFYC1bnSDPvYaTFVPWhprIHfTfKWMgplo1h4z_zjiqeNNsRWu4tDkdcKFnjdQ-_DhpdqIJL-txWaZKO7hUjPaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80db7c1466.mp4?token=jpEuxJdntwjHP7Cbxn26k-PVjJYL-Y10lwaa0eB6d1jaY2o2oN6TCg7tgyIt3L6pFpm5zbJaEY6zWLYnDvxkNcKDJZJ1rE6GCuNvh9oGTLJaNdL_AgN1THsp4Krjn4oOAGSWvj5KiLKxy6KBYugKAiL5NdUAUtgX-dI1UhzGITanchExBFxBNYolE7zxaoMLZEWGiiCz3UpU4F58iIGfjORQL8BeJbaxBWS3vCRAVCJzp9gTJUpI_ROxiqMDA1hM1OmbJxzsEjSO7XsFdlDJYdIQSsjZPf9BTZ83LInqC4tn_yPtSN6fFjReQQFyiVlfQD3Z5JYujgy_4BUjWOYKHGI3xBTRTYi5BL33S_bj6oDZ7ln3ZL0VXEhLSGc9Jmo_DdlOw4UO8AR1fC60jV5KvNftbsYZy82--XKN9x0sfH9DJkyK6kwByDhVmZxtDm1nSJM1S9-kshabTLgqVhgq8CyMkk-gyrnUKVXY8DEfeDZ_0ctlwRPXBDQvOocAeMRv-ouC8t3QBnJHwaqyhWAAfKxXQZzf19Bq2VgI4iByifA5rfIdRbc3VLOOwtxqGPvhylY_64q8VXuyKSj60KNejrFYC1bnSDPvYaTFVPWhprIHfTfKWMgplo1h4z_zjiqeNNsRWu4tDkdcKFnjdQ-_DhpdqIJL-txWaZKO7hUjPaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شهید سلامی از دستیابی به تکنولوژی انهدام ناوهای هواپیمابر
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/460565" target="_blank">📅 00:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460564">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9012d9a6.mp4?token=YUYCuBZvmCFntdUx0dSKYO0i_Vj8lL5VBllohJO8nS1rTTj57c-4pezTb5zF4LZZCu4XcZmiPJZv4Jys8oQQU0FxuO00aFRtr_KHNRGe5olYVYsjF6rxU9DTEx07K5xfEOL22naLL6319TrUtxXNlkrPTRjXQ9l8OS3_JH0FZwazqI2yDyfouxBz-Mt_pbZbdeG6aF07Z4nb6H8Vbx0F8vyc2qN9DymycuHhacyWEM5O2GPAPkE9kgSd8bkk4oiknpDVPi5GiMSbYrELQPcwfTBxY0oWo4RAy7-aVo8Dm6j36XJ-yIJ-QR_W7NHMATeQedcvEdV2f0dJ4f4UZLsjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9012d9a6.mp4?token=YUYCuBZvmCFntdUx0dSKYO0i_Vj8lL5VBllohJO8nS1rTTj57c-4pezTb5zF4LZZCu4XcZmiPJZv4Jys8oQQU0FxuO00aFRtr_KHNRGe5olYVYsjF6rxU9DTEx07K5xfEOL22naLL6319TrUtxXNlkrPTRjXQ9l8OS3_JH0FZwazqI2yDyfouxBz-Mt_pbZbdeG6aF07Z4nb6H8Vbx0F8vyc2qN9DymycuHhacyWEM5O2GPAPkE9kgSd8bkk4oiknpDVPi5GiMSbYrELQPcwfTBxY0oWo4RAy7-aVo8Dm6j36XJ-yIJ-QR_W7NHMATeQedcvEdV2f0dJ4f4UZLsjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا و یک رسوایی دیگر؛ تسلیحات کمپانی ریتون در حمله به عروسی سیریک  @Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/460564" target="_blank">📅 00:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460563">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تیراندازی در آمریکا، این‌بار پس‌ از مسابقات دانشگاهی
🔹
در پی تیراندازی جمعی در ایالت کالیفرنیای آمریکا روز یکشنبه دست‌کم ۳ زن هدف گلوله قرار گرفته‌اند.
🔹
پلیس محلی اعلام کرد که در تیراندازی صبح زود در ساکرامنتو پس از یک بازی فوتبال آمریکاییِ دانشگاهی، چهار نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/460563" target="_blank">📅 00:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460562">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193a0b1649.mp4?token=o2okKgC6khaIyRHhrEGvsfpbuh-q3RBxJWjd8HVkl7IQA44S9z6xxaa6RweazehPI0B3y8HbJ4Ze91idHaKe7aIXwE1PbgX8T7dV09CBa30TIFnIZ-1m3Si4ilnk9XukEuhbgLSB1uKOLQ4ZDQpN0y6Urqh-_YHnePJwhR-IyuG_Jr2Tj_qFc8U3425FrnSP9bCF56VD-CZZIzfk7UQFDEi6sfcNU6OovUZ9ze-jzsTLyDG_Sf2YU4LERzHcfCP7CEfZepLrlOMiUg6icV8JSUhB4WweHrKNL-QbdvQLVGsQ5xDVuG4s9b0bfWBEh-FD1dUe4W3WIAJ-frdJ-A8v-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193a0b1649.mp4?token=o2okKgC6khaIyRHhrEGvsfpbuh-q3RBxJWjd8HVkl7IQA44S9z6xxaa6RweazehPI0B3y8HbJ4Ze91idHaKe7aIXwE1PbgX8T7dV09CBa30TIFnIZ-1m3Si4ilnk9XukEuhbgLSB1uKOLQ4ZDQpN0y6Urqh-_YHnePJwhR-IyuG_Jr2Tj_qFc8U3425FrnSP9bCF56VD-CZZIzfk7UQFDEi6sfcNU6OovUZ9ze-jzsTLyDG_Sf2YU4LERzHcfCP7CEfZepLrlOMiUg6icV8JSUhB4WweHrKNL-QbdvQLVGsQ5xDVuG4s9b0bfWBEh-FD1dUe4W3WIAJ-frdJ-A8v-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین مدل اپن‌ای‌آی یک بدن انسان ۳بعدی ساخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/460562" target="_blank">📅 23:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460561">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f79baf2e1a.mp4?token=jgXNqx2hE7jlAZZuk0uFrg6yly4PbZs6ye2LDe0xBt-if2KG59RX6H5FX90wvZlU-26WRp4vUBBR8VgQQ8xGZala7Ok5feGgsulVorCOqdX7p9i3USaTnMv72zHHuBo5ulcyhJHyFhsHhm96LhEVn37WPibwv0MohJ3PY6ZgYt8oHiDKct3cm1gXqSJR00RUyV2J1JL0pAErCLFKVvOzfoMbz0-dHDQ7-AjfaPwuudZIPFifxaQyDeIXCqGwOJ9CLf36fxTo4Q7tjchwYkyUxfE2vApA0_S2w6A0mc5Jz7HrSdqX8y4IvmJEylPO1FtZY65EWRyr_HjGrBPAj_MvEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f79baf2e1a.mp4?token=jgXNqx2hE7jlAZZuk0uFrg6yly4PbZs6ye2LDe0xBt-if2KG59RX6H5FX90wvZlU-26WRp4vUBBR8VgQQ8xGZala7Ok5feGgsulVorCOqdX7p9i3USaTnMv72zHHuBo5ulcyhJHyFhsHhm96LhEVn37WPibwv0MohJ3PY6ZgYt8oHiDKct3cm1gXqSJR00RUyV2J1JL0pAErCLFKVvOzfoMbz0-dHDQ7-AjfaPwuudZIPFifxaQyDeIXCqGwOJ9CLf36fxTo4Q7tjchwYkyUxfE2vApA0_S2w6A0mc5Jz7HrSdqX8y4IvmJEylPO1FtZY65EWRyr_HjGrBPAj_MvEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم گردانی مهران رجبی در تجمعات شهر قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/460561" target="_blank">📅 23:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460560">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1a55c75f.mp4?token=teLAKo8vrLmWsz4QMLOU2OHbEKDqoI0qiXgLjDrso9ITZ5dEUpZnQ5ovcOzpBuaKXY7EI1Qmug8CUC28v1OupOUUZ7Lc4m5t8fxeIEVz3UHjkQPL1gpqCKQCauMFFjMjWWV6_NMgNavO9-se2jX3slcjIL2kALR__XizIwQC-PgGinuDAAV7NCwxIiUj3iJEiOpFxU3MiIP_kUbGLaLHWYTo-X0-vUr-eySKUyeY_Ip6dOZeQcn4I68ug6msOGc0M9R3HGOCX2-fpX153MG2ooDcUNDwdNJk7EJiHAVrkh5ijmXpV3LCk4u_0SUuvrhb9x0s3QBcndnKLdRbnYzhvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1a55c75f.mp4?token=teLAKo8vrLmWsz4QMLOU2OHbEKDqoI0qiXgLjDrso9ITZ5dEUpZnQ5ovcOzpBuaKXY7EI1Qmug8CUC28v1OupOUUZ7Lc4m5t8fxeIEVz3UHjkQPL1gpqCKQCauMFFjMjWWV6_NMgNavO9-se2jX3slcjIL2kALR__XizIwQC-PgGinuDAAV7NCwxIiUj3iJEiOpFxU3MiIP_kUbGLaLHWYTo-X0-vUr-eySKUyeY_Ip6dOZeQcn4I68ug6msOGc0M9R3HGOCX2-fpX153MG2ooDcUNDwdNJk7EJiHAVrkh5ijmXpV3LCk4u_0SUuvrhb9x0s3QBcndnKLdRbnYzhvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام خلج در برنامۀ سمت خدا: تفکر فرعونی، قدرت و تجهیزات را عامل پیروزی می‌داند
🔹
همان تفکری که امروز در آمریکا و رژیم صهیونیستی دیده می‌شود.
🔹
قرآن پیروزی را از آنِ اهل ایمان و تقوا می‌داند، نه صاحبان قدرت و ثروت.
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/460560" target="_blank">📅 23:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460559">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5362dd7c43.mp4?token=bAZHEtSFgKKCDDtQOo0PzFYlzLzew--xuImLDA38uyV4cR0nZh-eZYQrHnjfFCW3kmANRs1H9D1wXExdx8JV79eX66LNEimXSoe3kUkes0Vm_ZcdjoT8ZrvmHtGCWd7n2ltMZkV_OX1bgGhgk2pfPrM-WdWbQEXdwaC9c4MxAKUDCrf6-RoL4KdQ7v6tioth44QSp0IKSukdXu1fULT9GA7o6jubkyfqw-GnSgTUeJRPz1aYGT4dQPLzqXOQ5Bxk-IO13ivq0tOhn-6q9dxjWcA3CHQgEKI_mFlpweohWrRZSkiJ88PWQqE0UMwvByv8v3vhxpImZ077ljKfQP6dAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5362dd7c43.mp4?token=bAZHEtSFgKKCDDtQOo0PzFYlzLzew--xuImLDA38uyV4cR0nZh-eZYQrHnjfFCW3kmANRs1H9D1wXExdx8JV79eX66LNEimXSoe3kUkes0Vm_ZcdjoT8ZrvmHtGCWd7n2ltMZkV_OX1bgGhgk2pfPrM-WdWbQEXdwaC9c4MxAKUDCrf6-RoL4KdQ7v6tioth44QSp0IKSukdXu1fULT9GA7o6jubkyfqw-GnSgTUeJRPz1aYGT4dQPLzqXOQ5Bxk-IO13ivq0tOhn-6q9dxjWcA3CHQgEKI_mFlpweohWrRZSkiJ88PWQqE0UMwvByv8v3vhxpImZ077ljKfQP6dAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا این فناوری را از ترس ایران خاموش کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/460559" target="_blank">📅 23:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460558">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
لحظۀ انهدام جلسۀ فرماندهی مزدوران وابسته به سعودی توسط موشک بالستیک یمنی  @Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/460558" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460557">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb6cdf6f4.mp4?token=gsx7_TSW79RK5ZsEWhMqZwk-4z2pGX2hL23TfQa0bmH-7p9fawAVWvjsPJTNhHFTJ_fFZgumvEcv5afi6eCEx-wnkdiZ3GeGEiVmQjzFC2wn5RD7toE-HPGQ60QAgssRfuCKk67sowoJa3_iMFvlF-Btzl3dRJcemROh-aBgs1hgSBbwc4icoOvsC2FlszoeSl-VgP6Ro6lLm_Od0DK_1x6mU7HiId9N2gVngI2TectBdpPp49hU9hJfpgIsqrUM7LTGLNgfiX-nv3bbTKl2Ly_xAqSF_PIt36YLBtegP6F8DzlCgnxP5-Fqi2A9rNMVXJ2f3jirKOyZDN7A2NR6mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb6cdf6f4.mp4?token=gsx7_TSW79RK5ZsEWhMqZwk-4z2pGX2hL23TfQa0bmH-7p9fawAVWvjsPJTNhHFTJ_fFZgumvEcv5afi6eCEx-wnkdiZ3GeGEiVmQjzFC2wn5RD7toE-HPGQ60QAgssRfuCKk67sowoJa3_iMFvlF-Btzl3dRJcemROh-aBgs1hgSBbwc4icoOvsC2FlszoeSl-VgP6Ro6lLm_Od0DK_1x6mU7HiId9N2gVngI2TectBdpPp49hU9hJfpgIsqrUM7LTGLNgfiX-nv3bbTKl2Ly_xAqSF_PIt36YLBtegP6F8DzlCgnxP5-Fqi2A9rNMVXJ2f3jirKOyZDN7A2NR6mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: در بنزین ما متانول نیست
🔹
در دنیا استفاده از متاننول در بنزین گسترده است و تا ۳ درصد هم استاندارد است اما ما استفاده نمی‌کنیم.
🔹
تنها در یکی از پالایشگاه‌ها به‌صورت آزمایشی از ۰.۵ درصد متانول استفاده شده بود. @Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/460557" target="_blank">📅 23:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460556">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/he1-b2UmHLkXOLK0MqE1hGIVRoCJNq-tApMywGbcw62-0AYFA3eE0F-TenLbIO_MEH_h_WHRqzXhQF6ennRqKfbK1OWSfTuiAFhzKgFF2R5By0OItTbGdgtKikB6D-Zy9h4nqrbcauejt-bV9qgrwVAifzz-GVkRT3pp-Du-kuRFrSUYluOuM1ZT9myUF6PbNEsksKIr3ZzM6LDLkaS5KkHVT75Jzit9wGBad2nf-Dw7bXPc0BffFn799I1Hsf2DnRP-N8dB1HLreddplpBLozPpqU7Oo17BaQsEgEduC1gvubbQtqVhugUpgJbRzbw90Rih3l-cG1lvXAB_tsqZeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ شهید طی درگیری با اشرار در کورین زاهدان
🔹
یک منبع آگاه در زاهدان: در جریان درگیری امروز با اشرار مسلح در کورین از توابع زاهدان ۲ بسیجی به نام‌های کیوان رامرودی و ابوالفضل عودی به شهادت رسیدند.
📝
اخبار تکمیلی متعاقبا اعلام میگردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/460556" target="_blank">📅 23:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/686281167c.mp4?token=ANfpr_kvuIr1TYDLOKFUn3TlfWGCdN9T5Y4PsmS2X7694trV_NMKBN0_MjUEj1A-J_kFI2qY48UqR6Gx_Tj2-MJKULpkH2Pn-1xoCHsVb9dBOOl0HMXYdfDXnHLugurZyINfmeElbBN5Nyu3OBQoVLxofLeZKA2ai__u5LOfmlcMr8bKoSbhOcWNndtS50jqL4ZghGrft8X70c8R_XuRbWEcqCo-ry4Z2YjEtukyrCy5jmM2uvfL9VZ1F74Ndt9EEE7xOONm42smv0ZDO3lUy_on8kSq45w15lYrYD0xW-rh9F-O6kpN1VJUIxU2Rzpf5f2hYglp53OoG2dylHiM9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/686281167c.mp4?token=ANfpr_kvuIr1TYDLOKFUn3TlfWGCdN9T5Y4PsmS2X7694trV_NMKBN0_MjUEj1A-J_kFI2qY48UqR6Gx_Tj2-MJKULpkH2Pn-1xoCHsVb9dBOOl0HMXYdfDXnHLugurZyINfmeElbBN5Nyu3OBQoVLxofLeZKA2ai__u5LOfmlcMr8bKoSbhOcWNndtS50jqL4ZghGrft8X70c8R_XuRbWEcqCo-ry4Z2YjEtukyrCy5jmM2uvfL9VZ1F74Ndt9EEE7xOONm42smv0ZDO3lUy_on8kSq45w15lYrYD0xW-rh9F-O6kpN1VJUIxU2Rzpf5f2hYglp53OoG2dylHiM9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: کارت آزاد جایگاه شناسه‌دار می‌شود
🔹
در این طرح که در آینده اجرا خواهد شد هر نفر که با کارت جایگاه بنزین بزند با کارت بانکی احراز هویت می‌شود.
🔹
این طرح به‌صورت آزمایشی در چند جایگاه تهران درحال اجراست و احتمالا تا اواخر مهر در تمام کشور اجرا…</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/460554" target="_blank">📅 23:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460553">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02b05b065.mp4?token=PAib0dHBZ2j_yjx_X9hAt-SIt59BPLi2rKa3l1ulFtelkPk7MYTcRiifGy3Iqt6XV_k3mvrfN-JKEYX_8JpyIBxqsdvgh8pCsE_YZZNes37g9NNEqATSHHuHqrA5Tt2ca3RZyulU5lnGXN0SbcuFgbaojbYZyBY5eZGNuLiD8tcVGALUMrqTLT66Swh84hnc46v1O6kae5UUM-8j6KJkS1mphqI94CZTXU6FWve4hwdHbic64Qx3HpDVVk0IC2R0VvftduGc0U3aj7_3hVtCo-17j-7sZ6e5XSOf1Hzp8bhG5QqfkYolZwShkD4yhwZqGDXExDkSorYRudLCYDkyDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02b05b065.mp4?token=PAib0dHBZ2j_yjx_X9hAt-SIt59BPLi2rKa3l1ulFtelkPk7MYTcRiifGy3Iqt6XV_k3mvrfN-JKEYX_8JpyIBxqsdvgh8pCsE_YZZNes37g9NNEqATSHHuHqrA5Tt2ca3RZyulU5lnGXN0SbcuFgbaojbYZyBY5eZGNuLiD8tcVGALUMrqTLT66Swh84hnc46v1O6kae5UUM-8j6KJkS1mphqI94CZTXU6FWve4hwdHbic64Qx3HpDVVk0IC2R0VvftduGc0U3aj7_3hVtCo-17j-7sZ6e5XSOf1Hzp8bhG5QqfkYolZwShkD4yhwZqGDXExDkSorYRudLCYDkyDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سانحهٔ هوایی در آمریکا؛ ستون عظیم دود در آسمان میامی
🔹
پلیس و واحدهای آتش‌نشانی میامی پس از سقوط یک هواپیمای ۷۶۷ پرایم ایر در فرودگاه بین‌المللی میامی به منطقه اعزام شده‌اند.
🔹
گزارش‌ها حاکی از آن است که این هواپیمای باری امروز بعدازظهر به وقت محلی از باند فرودگاه بین‌المللی میامی (MIA) خارج شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/460553" target="_blank">📅 23:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460552">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed1c55e0c.mp4?token=bG_Nbc8LjkYCg3oR0flLCDJONTacA6BRZI0KSN8CCXXccsMBULTMMeSGnm-PK1oxdF63JyoujFJ6YnJwIfhpjHSKE0w6npnmOabSo1hePOoWQ4oBrH_6G57PK_DZIoEznZlRUobfrlNpa7U6Vmf5G2DjtZ9kvHQmgdwEVfU9A6uAXB_1iRq4MzL00IU1sXGLUY1AQ9clzbvaEVe9XNTySWU85k7E0i2-sMnSRJS3F3RLasKeR20InN8OlmDu3SKR0aPNFCw-NcPcKghUkUZFjAQ0r0ERmSNzW7tnuxRMesDSeWCZWHIOULwDbOciLsXJHaqfTSbUFw1ED46W_TF53A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed1c55e0c.mp4?token=bG_Nbc8LjkYCg3oR0flLCDJONTacA6BRZI0KSN8CCXXccsMBULTMMeSGnm-PK1oxdF63JyoujFJ6YnJwIfhpjHSKE0w6npnmOabSo1hePOoWQ4oBrH_6G57PK_DZIoEznZlRUobfrlNpa7U6Vmf5G2DjtZ9kvHQmgdwEVfU9A6uAXB_1iRq4MzL00IU1sXGLUY1AQ9clzbvaEVe9XNTySWU85k7E0i2-sMnSRJS3F3RLasKeR20InN8OlmDu3SKR0aPNFCw-NcPcKghUkUZFjAQ0r0ERmSNzW7tnuxRMesDSeWCZWHIOULwDbOciLsXJHaqfTSbUFw1ED46W_TF53A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: با جمع‌آوری کارت‌های جایگاه در کرمان مصرف سوخت‌های جایگزین مثل سی‌ان‌جی ۳۰ درصد افزایش پیدا کرد  @Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/460552" target="_blank">📅 23:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460551">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af729e4ee.mp4?token=dCOz_PCmOBiXPXwcUvgH5cTtJWVOAT5hbVhPQelMJs53vm5f9IwZ0TtiSHeDlVhkXapuIHEydQIXIIvOjIORrxkYhxuC1MVKunJRd2i7Bg_Z1gInEFjwQkhWAYJt3b_NDaGwie8_xQVX2V4Buz9p4Q1v-JDABgXg8gCWyIg-s6-rRLFENakSz1LNv3FlKRIiLy5q_uFaOARuMVLVwlMjjMGRwwUYBBx5XkfKzsURDpiLKtN-O5tGDn0FQdcEQK7J6B_m7KKpYyadwFWWr9guNSyw9i9_8kNh7QgGtbB4TQlYw1zbq_A1OVfqL0ECexdVlcJ5PwgrIHHdURuC0veDCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af729e4ee.mp4?token=dCOz_PCmOBiXPXwcUvgH5cTtJWVOAT5hbVhPQelMJs53vm5f9IwZ0TtiSHeDlVhkXapuIHEydQIXIIvOjIORrxkYhxuC1MVKunJRd2i7Bg_Z1gInEFjwQkhWAYJt3b_NDaGwie8_xQVX2V4Buz9p4Q1v-JDABgXg8gCWyIg-s6-rRLFENakSz1LNv3FlKRIiLy5q_uFaOARuMVLVwlMjjMGRwwUYBBx5XkfKzsURDpiLKtN-O5tGDn0FQdcEQK7J6B_m7KKpYyadwFWWr9guNSyw9i9_8kNh7QgGtbB4TQlYw1zbq_A1OVfqL0ECexdVlcJ5PwgrIHHdURuC0veDCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: قرار است یک روز در هفته مدیران دولتی ملزم به استفاده‌نکردن از خودرو بشوند  @Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/460551" target="_blank">📅 23:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460550">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407cfd0892.mp4?token=uWQ8e0k9pUGM1AntTlT1W_j7t7N09nLzYUU_UHwEWGF9_vi1wQNTGGTwf9Th7jbvFc9Ovn0jQe5ewvLrBOZHU9loqade88j123V3tkXmwGpaGXARnrp79tf8277eHHLHv-rdbSGM6n3Bs9WuXrI8Yp4eg2CvFYn_-MJxl6zWTt4TTlVG-CxuHiVzZATsB0Cm2HMJn4Ltmzm45ql2Ov4-Y1kA-HBDmyJ4-kWpOpCWhjO1MQjsV4oqagHV_nbfUWTXzxBdlIbb5wo6U2TZ9FjxCttCFq285ehFGqiDAslRBv3accC32JN9xb4NQFV0i61BYZzxId52bVN42bitvtcbCVnR-hbvKdyRjbfWPrc9OSu3JebJAh89kFL3PZ0oCVTIxTVq-8yMaLrsQla0xdPixSm7huIQyECXMEes9X2HxFr0-Q0YGWCJOVQRVgJLQcJN9Jk-0ugyICBITbc7r4bPvCqUsrjipc0Z9TsX1XjuNe7AdzR-ko-bILsoPzVBjoFuuLV-soISOqwfT5froEUF7i635qLKcCqJjIHJu-r7Ya0SpjPHSJ7thSP4X8irdCHkCsKiYZDggM3N-hLmRJv_OfOMVmv-qO2xDOHAnCQPzFN_wgyZwRIPlig7Vf3jK2QNzLN48duxVmYy0eVUlWz0uMQ8GCuGwoQKGoNmd4ptWec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407cfd0892.mp4?token=uWQ8e0k9pUGM1AntTlT1W_j7t7N09nLzYUU_UHwEWGF9_vi1wQNTGGTwf9Th7jbvFc9Ovn0jQe5ewvLrBOZHU9loqade88j123V3tkXmwGpaGXARnrp79tf8277eHHLHv-rdbSGM6n3Bs9WuXrI8Yp4eg2CvFYn_-MJxl6zWTt4TTlVG-CxuHiVzZATsB0Cm2HMJn4Ltmzm45ql2Ov4-Y1kA-HBDmyJ4-kWpOpCWhjO1MQjsV4oqagHV_nbfUWTXzxBdlIbb5wo6U2TZ9FjxCttCFq285ehFGqiDAslRBv3accC32JN9xb4NQFV0i61BYZzxId52bVN42bitvtcbCVnR-hbvKdyRjbfWPrc9OSu3JebJAh89kFL3PZ0oCVTIxTVq-8yMaLrsQla0xdPixSm7huIQyECXMEes9X2HxFr0-Q0YGWCJOVQRVgJLQcJN9Jk-0ugyICBITbc7r4bPvCqUsrjipc0Z9TsX1XjuNe7AdzR-ko-bILsoPzVBjoFuuLV-soISOqwfT5froEUF7i635qLKcCqJjIHJu-r7Ya0SpjPHSJ7thSP4X8irdCHkCsKiYZDggM3N-hLmRJv_OfOMVmv-qO2xDOHAnCQPzFN_wgyZwRIPlig7Vf3jK2QNzLN48duxVmYy0eVUlWz0uMQ8GCuGwoQKGoNmd4ptWec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: تاکسی‌های اینترنتی از تبعات افزایش نرخ بنزین مصون می‌مانند
🔸
قرار است با دوگانه‌سوز کردن ناوگان و اختصاص سهمیه مازاد مبتنی بر پیمایش، از افزایش هزینه و کرایهٔ تاکسی‌های اینترنتی جلوگیری شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/460550" target="_blank">📅 23:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460549">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879f852b1a.mp4?token=b3Or5CCTRbKaDlfCjH5qomdCVeoykk6pWgq4NupxJNnX3UktlV2owGmPFh4ePwR9x5Rk_RlFs_WlCmHi6VpjTB91tJyDid3nQrvWGCuOACXN6taQlF29feZKt0WX-3H8r-U-HayCs-Y4VmtI87GymPoAQqEO-s58eUIc53SQuzIrrJsJfmzqpJ-uMXnqmJjZPhiEEnP7rT-Wd4mwMTjodvZmOS3Bz7ZJtHMu8lm9mFdUIGVAnUzhZAySdyBjIL7uNtmbnAr6iWLkHBoe0rUETaqRLl5RoUfm7cBqUgrZqFKp7QMScxkIMIxDVhfyJiDhFf4HNXN-VShky8Fzt2BLqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879f852b1a.mp4?token=b3Or5CCTRbKaDlfCjH5qomdCVeoykk6pWgq4NupxJNnX3UktlV2owGmPFh4ePwR9x5Rk_RlFs_WlCmHi6VpjTB91tJyDid3nQrvWGCuOACXN6taQlF29feZKt0WX-3H8r-U-HayCs-Y4VmtI87GymPoAQqEO-s58eUIc53SQuzIrrJsJfmzqpJ-uMXnqmJjZPhiEEnP7rT-Wd4mwMTjodvZmOS3Bz7ZJtHMu8lm9mFdUIGVAnUzhZAySdyBjIL7uNtmbnAr6iWLkHBoe0rUETaqRLl5RoUfm7cBqUgrZqFKp7QMScxkIMIxDVhfyJiDhFf4HNXN-VShky8Fzt2BLqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: توانستیم با برخی تدابیر ۵ درصد افزایش تولید بنزین داشته باشیم  @Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/460549" target="_blank">📅 23:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460548">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d0204deb.mp4?token=bMmdHHU_4bFusj-BL_Ankeo-JwwIxbN29r5kwdCOb3CzKT8UqMpWcU0B21VBbbwBQu6GzOHD_kdDNaAGWOorIAKHoMtBS3nzK67_ia-Co4o3_vt9jfH-oG4jgmMIg9IKh99JR_h5Gyik-Kh7u-WGBOyaJP9x_N5zzdJeZvfKHAiPbsgiGwLHbFVFXOKKWh20cyU1aBgYqdjGCiV387njeKVCeYC_O8YaVA0dCzX3izO1PNmJtvpcqP1av2Q7WsfImxm6qDQW0GWqe0_Bt1GKKQQ2IIW_WG3vXcGhuvg4uNd8f6kzCQkJ5F1hCVjkG1XXX7lxoSaqVKw8SxumyYIXNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d0204deb.mp4?token=bMmdHHU_4bFusj-BL_Ankeo-JwwIxbN29r5kwdCOb3CzKT8UqMpWcU0B21VBbbwBQu6GzOHD_kdDNaAGWOorIAKHoMtBS3nzK67_ia-Co4o3_vt9jfH-oG4jgmMIg9IKh99JR_h5Gyik-Kh7u-WGBOyaJP9x_N5zzdJeZvfKHAiPbsgiGwLHbFVFXOKKWh20cyU1aBgYqdjGCiV387njeKVCeYC_O8YaVA0dCzX3izO1PNmJtvpcqP1av2Q7WsfImxm6qDQW0GWqe0_Bt1GKKQQ2IIW_WG3vXcGhuvg4uNd8f6kzCQkJ5F1hCVjkG1XXX7lxoSaqVKw8SxumyYIXNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: یکی از دلایل ناترازی بنزین ثابت بودن قیمت آن بوده است  @Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/460548" target="_blank">📅 23:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460547">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07eb2e2ef6.mp4?token=LFp0NYlWwY4Ysz-UCon-q6RDBf-FYxM3XT_OLWtoTMHNyFGoSyE6Yq2tNNRIKpHInK5Ipssxt7-WluDg1lQcJ-NH2TyA9R8YKwQEYwPZqvTKAzL7mOfgiW3U9WDCjpoS1wIWgUU5c-n1rJ4Q70WQAT-kO_5o4qCzTO4csjI2URMokQR0lvrtee5PdasUocRffjFmrtbW_1TkHP_a8TTGbDSI6XQqEHpYWpzRO3X7Zg3XLvbI3gIM5t5wbD0aUBYcZwQn7Ivo5HfJqoAMiefNJfLMoTNU3rJAe0aaDOlyVO2pwd3jsJhWNmw_YBlwfza50c4ZagW95dgBqHLU_hlaSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07eb2e2ef6.mp4?token=LFp0NYlWwY4Ysz-UCon-q6RDBf-FYxM3XT_OLWtoTMHNyFGoSyE6Yq2tNNRIKpHInK5Ipssxt7-WluDg1lQcJ-NH2TyA9R8YKwQEYwPZqvTKAzL7mOfgiW3U9WDCjpoS1wIWgUU5c-n1rJ4Q70WQAT-kO_5o4qCzTO4csjI2URMokQR0lvrtee5PdasUocRffjFmrtbW_1TkHP_a8TTGbDSI6XQqEHpYWpzRO3X7Zg3XLvbI3gIM5t5wbD0aUBYcZwQn7Ivo5HfJqoAMiefNJfLMoTNU3rJAe0aaDOlyVO2pwd3jsJhWNmw_YBlwfza50c4ZagW95dgBqHLU_hlaSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: تقریبا ۱۰ میلیون لیتر کسری بنزین داریم  @Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/460547" target="_blank">📅 23:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460546">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b9a74506e.mp4?token=erbpDqhqRCJ364oQThe1kFjGUQjUiTUyLc69Sg4h9Rv5F-txJH_md6V093yuwGLvkUo7oUucCeq_5vTODuJQE_WIK0rD3b7iN864D_VNTjzGXLC5gQsyM0v7XlyIqNF8WpM1VwwopzOROYaExOmWrrKGuV3nYAYIQG4ey2JcfHlUnlzOGa5_SwlJuymfeLaTWjwMe0jQNCOvlG371bNjtEVHXbJmkvX-7x8GT5MWE38aCQ1zKJhNU4fGoHfJSkzJv-ccUFwSXpfq2-UtKKJZD8B0JiGUQD9jjOXsIIzmBaBwaIp_IqVvVuuTWQbVtoyFzdXKekBmtSo7Gr6PoWB5oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b9a74506e.mp4?token=erbpDqhqRCJ364oQThe1kFjGUQjUiTUyLc69Sg4h9Rv5F-txJH_md6V093yuwGLvkUo7oUucCeq_5vTODuJQE_WIK0rD3b7iN864D_VNTjzGXLC5gQsyM0v7XlyIqNF8WpM1VwwopzOROYaExOmWrrKGuV3nYAYIQG4ey2JcfHlUnlzOGa5_SwlJuymfeLaTWjwMe0jQNCOvlG371bNjtEVHXbJmkvX-7x8GT5MWE38aCQ1zKJhNU4fGoHfJSkzJv-ccUFwSXpfq2-UtKKJZD8B0JiGUQD9jjOXsIIzmBaBwaIp_IqVvVuuTWQbVtoyFzdXKekBmtSo7Gr6PoWB5oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: تقریبا ۱۰ میلیون لیتر کسری بنزین داریم
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/460546" target="_blank">📅 23:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460545">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/485560a4d5.mp4?token=usAbJfQk3aZR1-n3GBFQPtXZUABgjkx4dmQSyIMuo7a1MNb5NqrhO1EEV1U0EKcz0cjxadMmz8AJrjf8z3egIIxawrhuZLEtGUzAh5u3QdvPvcB_aFudRgu8UzSYyD5Npj4AeqGavGJHRZHlufRgz90EQpN6Cs641XeUv1lQ9BR6Qmwr0Iirvfde-mwMVm2eek7b71_71K1LHa8xaOrTYOMS3ndXSTtjgGLE56sHrHIICFK6MRC8JtOBwvDI0702qySI139-mzz5csnoYaP7KpsoEqkYX0sZge7vyCVuP4Vughec-ffxewTw6oVmZFVwMJhmVhlOgSHnPrvGUSEBgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/485560a4d5.mp4?token=usAbJfQk3aZR1-n3GBFQPtXZUABgjkx4dmQSyIMuo7a1MNb5NqrhO1EEV1U0EKcz0cjxadMmz8AJrjf8z3egIIxawrhuZLEtGUzAh5u3QdvPvcB_aFudRgu8UzSYyD5Npj4AeqGavGJHRZHlufRgz90EQpN6Cs641XeUv1lQ9BR6Qmwr0Iirvfde-mwMVm2eek7b71_71K1LHa8xaOrTYOMS3ndXSTtjgGLE56sHrHIICFK6MRC8JtOBwvDI0702qySI139-mzz5csnoYaP7KpsoEqkYX0sZge7vyCVuP4Vughec-ffxewTw6oVmZFVwMJhmVhlOgSHnPrvGUSEBgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
دبیر شورای عالی امنیت ملی: تنگه هرمز تنگه جنگ نیست، بلکه تنگۀ اقتدار ایران است
🔹
نباید کسی این‌طور بگوید که این تنگه، تنگۀ جنگ است؛ این آبراه ابزاری برای گرفتن حقوق مردم ایران از آمریکاست.
🔹
دشمن در تمام گروه‌های سیاسی نفوذ دارد؛ بهترین راه وحدت، تحمل‌پذیری…</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/460545" target="_blank">📅 22:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460544">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83bf75a8d0.mp4?token=NPgro76ChZpFDIc0oBQFb45oCbyUgFwxCXA1-IRkpX5YqCD75RKyalD9yrtJ2caEvn8IEuJhvSKyK8szmkWNXHZPOFE1LbZRjqblUjeFFWXUbz88DvYkl3jLT0YMK4WoTNtkPnEt8uQJ3JM1QiVIIbiwiZVz600oqXLetge-RJWZATq3y5GeEfBqMZSh-okk_ZDjOVrb32cYdlpLNqQYA-lbRC-JiVr1qzVu3lKDHV985S65VvdQXHDzpwFkbSzEa60WdVPHHyXZaj4H3OLizKz7-0XiRWzryZ-R0rJFeSGSdLFGPukycZRU68Dou-vTstjl4GUoJlm0mRLNp2VCSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83bf75a8d0.mp4?token=NPgro76ChZpFDIc0oBQFb45oCbyUgFwxCXA1-IRkpX5YqCD75RKyalD9yrtJ2caEvn8IEuJhvSKyK8szmkWNXHZPOFE1LbZRjqblUjeFFWXUbz88DvYkl3jLT0YMK4WoTNtkPnEt8uQJ3JM1QiVIIbiwiZVz600oqXLetge-RJWZATq3y5GeEfBqMZSh-okk_ZDjOVrb32cYdlpLNqQYA-lbRC-JiVr1qzVu3lKDHV985S65VvdQXHDzpwFkbSzEa60WdVPHHyXZaj4H3OLizKz7-0XiRWzryZ-R0rJFeSGSdLFGPukycZRU68Dou-vTstjl4GUoJlm0mRLNp2VCSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: برای داشتن وحدت باید به رهبری نگاه کرد
🔹
هر نوع اختلاف خارج از چارچوب رهبری باعث ازبین‌رفتن آن افراد و آسیب به مردم می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460544" target="_blank">📅 22:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460543">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5db25947e.mp4?token=iXqJR8E-TJNbNpyxQHfx8AXeM_X4PVDm-lT5sAAjW3M_bgixlvLvcz-SfwHU57vYFIaZ10o7Sle7d-Sd_JJ92LmQpr6IBq2F8wjTdnVlg5vF2nF5PozexfupzwthdiLK1mW6VGwjbNCtTlCoLZzANEdI4RZjPC8yMcRBJy9bT9iROYQhCFa96dt01M39wU-FtsHI3hShUMsBmOLS9ar6kleok8h_cuL6Y9IR8iqi8PJbLcNtQgvk_FG9Qyh_kIlye0WCvWUO5T6dr0L7lFwd2Q1wMY8JNWdlq8jIu-D8M49nUYjm0iyV4fjyd8cNioTL4abgW6kb9qiTBZAZNmmAJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5db25947e.mp4?token=iXqJR8E-TJNbNpyxQHfx8AXeM_X4PVDm-lT5sAAjW3M_bgixlvLvcz-SfwHU57vYFIaZ10o7Sle7d-Sd_JJ92LmQpr6IBq2F8wjTdnVlg5vF2nF5PozexfupzwthdiLK1mW6VGwjbNCtTlCoLZzANEdI4RZjPC8yMcRBJy9bT9iROYQhCFa96dt01M39wU-FtsHI3hShUMsBmOLS9ar6kleok8h_cuL6Y9IR8iqi8PJbLcNtQgvk_FG9Qyh_kIlye0WCvWUO5T6dr0L7lFwd2Q1wMY8JNWdlq8jIu-D8M49nUYjm0iyV4fjyd8cNioTL4abgW6kb9qiTBZAZNmmAJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ما حق پاسخ به حملهٔ آمریکایی‌ها به مراسم عروسی در کوهستک را محفوظ نگه‌داشته‌ایم و آمریکایی‌ها باید این را بدانند. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460543" target="_blank">📅 22:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460542">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3b2cb0535.mp4?token=l4JrFWUZTqZ0M4RtgCPM5kfjB_e0gO8Y3Sjr7Vwly00sN9WU59IxJQFooxy4OesAZAEAVkfQFuzVL_di-P6li_TdXOx7CxWHMRWGTIY2y2OxFxVMq3CVDWeP0sJLKQ5EbOMIJ4Oheh0a2dRqJE7DddM8LybmHeYcVTJ7Ve70L3Kd1Q2y0n3swwaFEtfzlVKBaWxtIvVj38XuRrjoFxcVpCdnFi2pjtcL-BXzNy5PxU_iAQu6u6zNMlgiEsXHRyKQHfDkSV5VPCFO-Rwpj3yb_NttjUbrjFt6PIRYK1v7619gEjHLsUq-DXumEYt85ybQGBR1yhYTKQlvFAORqbP6jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3b2cb0535.mp4?token=l4JrFWUZTqZ0M4RtgCPM5kfjB_e0gO8Y3Sjr7Vwly00sN9WU59IxJQFooxy4OesAZAEAVkfQFuzVL_di-P6li_TdXOx7CxWHMRWGTIY2y2OxFxVMq3CVDWeP0sJLKQ5EbOMIJ4Oheh0a2dRqJE7DddM8LybmHeYcVTJ7Ve70L3Kd1Q2y0n3swwaFEtfzlVKBaWxtIvVj38XuRrjoFxcVpCdnFi2pjtcL-BXzNy5PxU_iAQu6u6zNMlgiEsXHRyKQHfDkSV5VPCFO-Rwpj3yb_NttjUbrjFt6PIRYK1v7619gEjHLsUq-DXumEYt85ybQGBR1yhYTKQlvFAORqbP6jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: اسرائیل توانسته جاهایی از لبنان را بگیرد اما مطمئنم لبنان دوباره سر بلند می‌کند و این دفعه خشم بزرگی راه می‌افتد که نمی‌گذارد چیزی از اسرائیل بماند.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460542" target="_blank">📅 22:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460541">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e5b97cf12.mp4?token=jdo6IPO4_ud5yAjRNLCWtp-F3qXM1SYkEiEwQBUhfwPboV1dKkOgm-v3snJg0go3Jo-kMmTkN_8H7LRH3XqUQJGfuvfDrVi4fLHOpRpRSDTgXznU7XbF8yP1rijAb5ffF8eBcCGdLMUovWLWkBib6c_Rrio2OCuTGfEorjIV1YzdjGfQF35x4-ypNy4MH5oXf7TdEQEZFOE_HMD7OZGEeoMNVRpclB_bEsx8aosVQ03gv8oPdv-df0lPO_Sww7AVCBQcFGKD4emzRtlfhk1A10cMAgiRaXSu0oyFQaUewmvMR5y3N63aCLv6UD11RR7X57Y6kAt50KHFXB-sITG47g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e5b97cf12.mp4?token=jdo6IPO4_ud5yAjRNLCWtp-F3qXM1SYkEiEwQBUhfwPboV1dKkOgm-v3snJg0go3Jo-kMmTkN_8H7LRH3XqUQJGfuvfDrVi4fLHOpRpRSDTgXznU7XbF8yP1rijAb5ffF8eBcCGdLMUovWLWkBib6c_Rrio2OCuTGfEorjIV1YzdjGfQF35x4-ypNy4MH5oXf7TdEQEZFOE_HMD7OZGEeoMNVRpclB_bEsx8aosVQ03gv8oPdv-df0lPO_Sww7AVCBQcFGKD4emzRtlfhk1A10cMAgiRaXSu0oyFQaUewmvMR5y3N63aCLv6UD11RR7X57Y6kAt50KHFXB-sITG47g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ‌
🔴
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها و صهیونیست‌ها دنبال چیزی شبیه کودتای ۱۸ و ۱۹ دی هستند تا همزمان خودشان هم حمله را شروع کنند اما به فضل پروردگار هر ۲ را خنثی خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460541" target="_blank">📅 22:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460540">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f470489d.mp4?token=TjrzMCLTWeWOJK_Wqgj15_lorTx1q5a1iyDRq4c21aEFbVqNNau2y8aH4LfwWMnbxqExVPNm-vMat8raYSfbqDvDPMehABHOZJS-u16-yYmMiPNLTwOFr7HPcgHxhd62A8u-ThrcBR8TpBhNevpAwaoJXJFSxKs1k2H_2IY23SUGu1lW-milh1AleKcLWoZ_NYriTZ4mlVXGhRexJrbPUn1fYhFZeL_xQr7_9y8WNhF8zQL7bz564_ouHckbKDsOPe5S_pCEAUfv_Kc-2GVGnvZXF1nLj4HWig8HzkZfsZulNfCOT4yqsQWn0faXUSO_khGWMF_KKnYNyI7Su4LRmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f470489d.mp4?token=TjrzMCLTWeWOJK_Wqgj15_lorTx1q5a1iyDRq4c21aEFbVqNNau2y8aH4LfwWMnbxqExVPNm-vMat8raYSfbqDvDPMehABHOZJS-u16-yYmMiPNLTwOFr7HPcgHxhd62A8u-ThrcBR8TpBhNevpAwaoJXJFSxKs1k2H_2IY23SUGu1lW-milh1AleKcLWoZ_NYriTZ4mlVXGhRexJrbPUn1fYhFZeL_xQr7_9y8WNhF8zQL7bz564_ouHckbKDsOPe5S_pCEAUfv_Kc-2GVGnvZXF1nLj4HWig8HzkZfsZulNfCOT4yqsQWn0faXUSO_khGWMF_KKnYNyI7Su4LRmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ‌
🔴
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها و صهیونیست‌ها دنبال چیزی شبیه کودتای ۱۸ و ۱۹ دی هستند تا همزمان خودشان هم حمله را شروع کنند اما به فضل پروردگار هر ۲ را خنثی خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/460540" target="_blank">📅 22:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460539">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: جنگ ۱۰ روزۀ ترامپ یک‌ روزه شد
🔹
ترامپ در حملات اخیر اعلام کرده بود که می‌خواهد ۱۰ روز به ایران حمله کند اما با پاسخ‌های ما غافلگیر شد و عقب نشست. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460539" target="_blank">📅 22:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460538">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141d9dce5c.mp4?token=d14xWHgto7znW7spP-7jeIgCncGhWU5YQxNgmg58TwHBrprDRzsG_MWD1SU8mW7TX8QOM668dXBgK3xaplSAwGowBTWgR0yxJz0DndHFeFmK_D4Pz7wn7HNQtRThpd6UG9r9Wl9NiP-nGjOlUUQNQuRWVUj4dyQ8bm9a4yHwC4Er-WMuFZdLZq6dFQ4g_vtIvhTJ3GLkOxPP383ZIdA4X1mDSwKINKBT2vl3sI-m-yKcMGsGK4lvaksxRsfmYZyTO4XRhTHiO6Cjb8PQgqUt8HSD8MBvhVaAmGDRVLokDHz6NoJDDIfnlzl9i6UhftW08y-hJdef138eFPvlN-wvcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141d9dce5c.mp4?token=d14xWHgto7znW7spP-7jeIgCncGhWU5YQxNgmg58TwHBrprDRzsG_MWD1SU8mW7TX8QOM668dXBgK3xaplSAwGowBTWgR0yxJz0DndHFeFmK_D4Pz7wn7HNQtRThpd6UG9r9Wl9NiP-nGjOlUUQNQuRWVUj4dyQ8bm9a4yHwC4Er-WMuFZdLZq6dFQ4g_vtIvhTJ3GLkOxPP383ZIdA4X1mDSwKINKBT2vl3sI-m-yKcMGsGK4lvaksxRsfmYZyTO4XRhTHiO6Cjb8PQgqUt8HSD8MBvhVaAmGDRVLokDHz6NoJDDIfnlzl9i6UhftW08y-hJdef138eFPvlN-wvcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: ما موشک ناوشکن‌مان را بالای سر یک ناو تست کردیم و آمریکایی‌ها وحشت‌زده فرار کردند. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460538" target="_blank">📅 22:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460537">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌‌
🔴
دبیر شورای‌عالی امنیت ملی: ما برای اولین‌بار ۲-۳ پایگاه آمریکا را زدیم؛ پایگاه‌هایی در اردن و اربیل که آمریکایی‌ها فکر می‌کردند از آن خبر نداریم
🔹
پایگاه اردن اصلا پدافند هوایی نداشت. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460537" target="_blank">📅 22:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460536">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌‌
🔴
دبیر شورای‌عالی امنیت ملی: زمانی تعهد می‌دهیم که تنگهٔ هرمز باز باشد که آمریکایی‌ها خرابکاری و حمله نکنند. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460536" target="_blank">📅 22:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460535">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a52f05f75.mp4?token=pjidW0kdSlzGJ4d8hlCPHrQn_3skdFO_XHaLc_xKHZcFGWXDaS6goXwd0MNhkF_yUNNuENW9pZTT2WSqaXJk9XnUAc475yV8vdaL9cFn8KY-aUpqLIQql839Tr27qIBXN9MaSX2bYQdohTX2ASrmKsR5QD4tG22vAd1ZNKMJ_6TgT6vmyWfrQgz6XF5CtBR583ATSv_gUe6dvcPg_yj1o4Wj218XPJnLR2BkBJNENrpfvbh-SLqALfEfi1NsE-Ok_ue3y-Q1CMU4vAhfpMVDRPYceW1w2qpJMK7l6cuyT4R7vmP-65QyYZ35zpvFBsJ2PxDmmRczjQhIlRHumh3lqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a52f05f75.mp4?token=pjidW0kdSlzGJ4d8hlCPHrQn_3skdFO_XHaLc_xKHZcFGWXDaS6goXwd0MNhkF_yUNNuENW9pZTT2WSqaXJk9XnUAc475yV8vdaL9cFn8KY-aUpqLIQql839Tr27qIBXN9MaSX2bYQdohTX2ASrmKsR5QD4tG22vAd1ZNKMJ_6TgT6vmyWfrQgz6XF5CtBR583ATSv_gUe6dvcPg_yj1o4Wj218XPJnLR2BkBJNENrpfvbh-SLqALfEfi1NsE-Ok_ue3y-Q1CMU4vAhfpMVDRPYceW1w2qpJMK7l6cuyT4R7vmP-65QyYZ35zpvFBsJ2PxDmmRczjQhIlRHumh3lqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌
🔴
دبیر شورای‌عالی امنیت ملی: زمانی تعهد می‌دهیم که تنگهٔ هرمز باز باشد که آمریکایی‌ها خرابکاری و حمله نکنند. @Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/460535" target="_blank">📅 22:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460534">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🎥
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها حتی به محمدرضا پهلوی هم وفا نکردند
🔹
بعد از انقلاب کارشکنی آمریکایی‌ها چندبرابر شد.
🔹
سیاست آمریکایی‌ها این است که ایران تبدیل به نوکری بشود که توانایی هیچ کاری نداشته باشد. @Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/460534" target="_blank">📅 22:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460533">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb7f4886cb.mp4?token=Z14uH-xoadz5eg79Dqc6gk4qiiPGAv2zTwWr0Ku6YZkF4KB6AYnZF-QchHCXEJsRyXNA_kvixPEWFvEoqHZ8MVP_UUDR7jTjWTepTRpnxV911v4YlxMErvV8wCj-k3U_OIgLAgbiy7ihI2zdhbA3qh-iy_1RaMpvir8G1m4x1UUcAlHafKIThj_szY7lKt_WRSSr66Ct6NiZF71st2LSv8iU4_XoVAbS3OzgGZsk6GiubEZwf5MdjHFE53Sro47llq7aD-OqpeQMzXhy6_IsKp36h8NrA12REN1HwDI25RAQ4-oPXsPyFZDzvQGsOkIiMl5MOpeyRHsslWxZxw4Nww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb7f4886cb.mp4?token=Z14uH-xoadz5eg79Dqc6gk4qiiPGAv2zTwWr0Ku6YZkF4KB6AYnZF-QchHCXEJsRyXNA_kvixPEWFvEoqHZ8MVP_UUDR7jTjWTepTRpnxV911v4YlxMErvV8wCj-k3U_OIgLAgbiy7ihI2zdhbA3qh-iy_1RaMpvir8G1m4x1UUcAlHafKIThj_szY7lKt_WRSSr66Ct6NiZF71st2LSv8iU4_XoVAbS3OzgGZsk6GiubEZwf5MdjHFE53Sro47llq7aD-OqpeQMzXhy6_IsKp36h8NrA12REN1HwDI25RAQ4-oPXsPyFZDzvQGsOkIiMl5MOpeyRHsslWxZxw4Nww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: مشخص شد میانجیگران نمی‌توانند تضمین اجرای تفاهمات را بدهند
🔹
اصلی‌ترین مشکل ما در این تفاهم‌نامه نبود تضمین بود که میانجی‌ها هم نتوانستند آن را فراهم کنند. @Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/460533" target="_blank">📅 22:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460532">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌‌
🔴
دبیر شورای‌عالی امنیت ملی: برای اولین‌بار، ۴۸ ساعت پیش اولین موشک ناوشکن خودمان را روی ناو آمریکایی تست کردیم. @Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/460532" target="_blank">📅 22:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460531">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4139f94445.mp4?token=oVCObSSu2wNSig13BCj1VMZ7PmUmmpO9AZIPFBRNf-1pRDC0uIepuBmZv6xtWa0OxR_dEO8rmD5_m56zFerC-ygNDHolVrHhABKY2sK7vdqtZ9WXw-2-wS0Ki-PRee_Cc1gVIhKANy4yBnA5a1yGQE9H_0bsG9hGAs0dhswZSOzaPBMrp_C1Xwb4jGpw0MN4o5Vjg3FRU1pxPDkzDG7fBAR8Ru9XhhOTl8STn8KiWjy_HmIgVzVOthq_JQlqop2czvW_9--kGVmJLgsDE2lRBr_XNC3kCtzu_braDvuSzsE8-YnmpGpN31iSl-f2O-yyMvuvx00Jswi4pbZZzDefYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4139f94445.mp4?token=oVCObSSu2wNSig13BCj1VMZ7PmUmmpO9AZIPFBRNf-1pRDC0uIepuBmZv6xtWa0OxR_dEO8rmD5_m56zFerC-ygNDHolVrHhABKY2sK7vdqtZ9WXw-2-wS0Ki-PRee_Cc1gVIhKANy4yBnA5a1yGQE9H_0bsG9hGAs0dhswZSOzaPBMrp_C1Xwb4jGpw0MN4o5Vjg3FRU1pxPDkzDG7fBAR8Ru9XhhOTl8STn8KiWjy_HmIgVzVOthq_JQlqop2czvW_9--kGVmJLgsDE2lRBr_XNC3kCtzu_braDvuSzsE8-YnmpGpN31iSl-f2O-yyMvuvx00Jswi4pbZZzDefYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌
🔴
دبیر شورای‌عالی امنیت ملی: برای اولین‌بار، ۴۸ ساعت پیش اولین موشک ناوشکن خودمان را روی ناو آمریکایی تست کردیم. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460531" target="_blank">📅 22:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460529">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌ ‌
🔴
دبیر شورای‌عالی امنیت ملی: ما داریم نفت می‌فروشیم و پولش را هم می‌‌گیریم. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460529" target="_blank">📅 22:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460528">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: دولت از مدت‌ها قبل به فکر بوده و به اندازهٔ کافی مواد غذایی و کالاهای اساسی داریم. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460528" target="_blank">📅 22:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460527">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: سخت‌گیری‌های ما در تنگهٔ هرمز دارد بیشتر می‌شود و اثر تحریم‌های ایران در تنگهٔ هرمز از موشک‌ها بیشتر خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460527" target="_blank">📅 22:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460526">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🎥
دبیر شورای‌عالی امنیت ملی: به‌زودی یک محدودهٔ ممنوعه در اطراف تنگهٔ هرمز اعلام می‌کنیم
🔹
این محدوده از خط محاصرۀ آمریکایی‌ها شروع می‌شود و تا تنگۀ هرمز و انتهای خلیج‌فارس ادامه دارد.
🔹
هر کشتی وارد آن شود در فهرست تحریم ایران قرار می‌گیرد.
🔹
این کشتی‌ها…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460526" target="_blank">📅 22:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460525">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab9a16f140.mp4?token=X2eWmsaG17vOLdUOZrO4Q1gGqBZlYtpEIstMfUt9g_Wv7dIpRURe3DlNcnBHGWDlxKETndIT3t0YF3LwROyZPvGv3ApDT1GRgO5l2aprFS7Z6b8QPbQfBH5tWOhrHAOvVkyI9PYteg_MQlvv6FLLvv8qnyWnzP-yjXhr8yI2P8KnDMmxHK3fNVU23Gc9SHtfa5P4rE5NzmaruKlskYCyF0C7OGC7wHPjCbJqcgQGZHvUsNp5ITfqW_DiB-bmtr2yblZv5QU7dE7UUnStqO-VLkh1Q2uNlyC0XUPgXQdIS65UHDxQNUBZWycAe9wbm8Y5hX8E78t9xO_VH1bNzHay6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab9a16f140.mp4?token=X2eWmsaG17vOLdUOZrO4Q1gGqBZlYtpEIstMfUt9g_Wv7dIpRURe3DlNcnBHGWDlxKETndIT3t0YF3LwROyZPvGv3ApDT1GRgO5l2aprFS7Z6b8QPbQfBH5tWOhrHAOvVkyI9PYteg_MQlvv6FLLvv8qnyWnzP-yjXhr8yI2P8KnDMmxHK3fNVU23Gc9SHtfa5P4rE5NzmaruKlskYCyF0C7OGC7wHPjCbJqcgQGZHvUsNp5ITfqW_DiB-bmtr2yblZv5QU7dE7UUnStqO-VLkh1Q2uNlyC0XUPgXQdIS65UHDxQNUBZWycAe9wbm8Y5hX8E78t9xO_VH1bNzHay6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: تنگهٔ هرمز کاملا بسته است
🔹
امروز از تنگه حداکثر ۷-۸ کشتی رد می‌شود که ۵-۶ تای آن هم کالاهای اساسی وارد می‌کند برای خود ما.
🔹
بعضی وقت‌ها آمریکایی‌ها از صخره‌های متصل به عمان ۵-۶ کشتی را عبور می‌دهند و معمولا این کشتی‌ها هدف قرار…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460525" target="_blank">📅 22:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460524">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4831d598.mp4?token=f8F55Qs357_kLWlRyvAWGaMM6x1jR7xvUuDULlrVcEX1FOdv7gxQyq_gVGIA3eefYngHR8kdI37CAvbLmRFEN0fpu2Ys9RhwvJq9pGq9dC1Xv5kX3873MNMJ9LNXd_9nfi9uzFZRQhsmjeaaPv1a0b3CLYwLN2V-p2Um-XP5xifaWTIOToYlwoTB2R5d1oo6ViF51CcydYehCEtGdHcjrOmNGRxifK7KxOrwl6IQWomDqnj6kPA3Iq5PRNXryzqbkZqFBQVux7i870jm1HL_ddPXzE_xTOrA9UIdvzeCdaBVXYBTJxUpq2i0D5PneU03QvOuzxjHLrumS7wYaJyRpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4831d598.mp4?token=f8F55Qs357_kLWlRyvAWGaMM6x1jR7xvUuDULlrVcEX1FOdv7gxQyq_gVGIA3eefYngHR8kdI37CAvbLmRFEN0fpu2Ys9RhwvJq9pGq9dC1Xv5kX3873MNMJ9LNXd_9nfi9uzFZRQhsmjeaaPv1a0b3CLYwLN2V-p2Um-XP5xifaWTIOToYlwoTB2R5d1oo6ViF51CcydYehCEtGdHcjrOmNGRxifK7KxOrwl6IQWomDqnj6kPA3Iq5PRNXryzqbkZqFBQVux7i870jm1HL_ddPXzE_xTOrA9UIdvzeCdaBVXYBTJxUpq2i0D5PneU03QvOuzxjHLrumS7wYaJyRpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: تنگهٔ هرمز کاملا بسته است
🔹
امروز از تنگه حداکثر ۷-۸ کشتی رد می‌شود که ۵-۶ تای آن هم کالاهای اساسی وارد می‌کند برای خود ما.
🔹
بعضی وقت‌ها آمریکایی‌ها از صخره‌های متصل به عمان ۵-۶ کشتی را عبور می‌دهند و معمولا این کشتی‌ها هدف قرار می‌گیرند و هیچ‌کدام سالم نمی‌روند و معنای این بازشدن تنگه نیست.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460524" target="_blank">📅 22:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460523">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/169a2c2646.mp4?token=ZCKamG-42MhwMMUOBOr_g8-zG6xIyfh7AhwBqcuk5AEzdiyEr2yCIBJ50BHXKFimHN3gXE6qiVF7ivCWGDO49IMXHDs9ld1CR0W_tT7JmlBBfs1BzXvkRbc6iAocRKbmHDVZ62d60dOZg3eyL6CGwzGvPRoU2-svTpnZboMgR8gxfkOsATw0swLPqqTaAGvsvMMwc7aC31ipmyXGidAE3Vt5DankQ425T2IEioQOtJtBsJJbnJPQm9Yh67DmYFJrW_S7TfkKFrTewS2n4XWEiQrjTDSp2lbFHsK6uaogrs4_dI4cQ5wkCQf7TqjZaoqohLucWAT5uPtJGa2yqUERooFUw226HJ7wOzSgF-R87AJ2N8dbBzNwO5DkZxVEX_kjuoo3MskjDuUTyeP2lXanYXUhPRBDQrzTkj-dqhlgW9PXi4hyunYEwYSo83HtfbS3C69dW2ypjVl8zF2fhAh3ianFs20kWFMNXdDqhz455GxXt3GPqvIJmvZoKiiw6ihhw2c2AV0D2jlul97RFsELZ_so5f7pBl4nQ5xsCyaRFgGSsTtlHbNKUYHWJlQLaCdb86YBIaaT_FdDKvC23wkzUllKPPiCMraeYO2lT-bC5AXGRvGLfmBvX5kuRiJ2Ssgei0H7YZgnRG0VwsrjMG0bS2eS8LtIBPQ1tVWbX7zOHuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/169a2c2646.mp4?token=ZCKamG-42MhwMMUOBOr_g8-zG6xIyfh7AhwBqcuk5AEzdiyEr2yCIBJ50BHXKFimHN3gXE6qiVF7ivCWGDO49IMXHDs9ld1CR0W_tT7JmlBBfs1BzXvkRbc6iAocRKbmHDVZ62d60dOZg3eyL6CGwzGvPRoU2-svTpnZboMgR8gxfkOsATw0swLPqqTaAGvsvMMwc7aC31ipmyXGidAE3Vt5DankQ425T2IEioQOtJtBsJJbnJPQm9Yh67DmYFJrW_S7TfkKFrTewS2n4XWEiQrjTDSp2lbFHsK6uaogrs4_dI4cQ5wkCQf7TqjZaoqohLucWAT5uPtJGa2yqUERooFUw226HJ7wOzSgF-R87AJ2N8dbBzNwO5DkZxVEX_kjuoo3MskjDuUTyeP2lXanYXUhPRBDQrzTkj-dqhlgW9PXi4hyunYEwYSo83HtfbS3C69dW2ypjVl8zF2fhAh3ianFs20kWFMNXdDqhz455GxXt3GPqvIJmvZoKiiw6ihhw2c2AV0D2jlul97RFsELZ_so5f7pBl4nQ5xsCyaRFgGSsTtlHbNKUYHWJlQLaCdb86YBIaaT_FdDKvC23wkzUllKPPiCMraeYO2lT-bC5AXGRvGLfmBvX5kuRiJ2Ssgei0H7YZgnRG0VwsrjMG0bS2eS8LtIBPQ1tVWbX7zOHuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقای «سنگری» قهرمان مخابراتی کوهستک را بشناسید
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460523" target="_blank">📅 21:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460522">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348cd28267.mp4?token=gSwzFuljisF0rse_JCYen4tuuT8F1ohNU3wkhMPXZCQauKWbt-Vb3duqryJxTB-PWhgcqjZnr3984QIyEI135T6yd7pA2WxNh0Lt0KpD_ueVQAwyNO019oil3w9dRf1hY5yiGdWgwlWstdnZiP4bBj_eQAAll53_E4xfVF_3b5D3EL-eYJqFqzgezvO6x32G8V0xotusma71_qOtKiSQofaTdZgsKp0py3sM73K4UFUiUeudEuR2Vc2cUE3gmFF3ndXSe65LVT8KreR7wmKvHIVdNiIX04EIYS2V9zfLAciwgmyY9EOWOkguY-keVeE2lDQWG-oqdrXdGj9QZpfB3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348cd28267.mp4?token=gSwzFuljisF0rse_JCYen4tuuT8F1ohNU3wkhMPXZCQauKWbt-Vb3duqryJxTB-PWhgcqjZnr3984QIyEI135T6yd7pA2WxNh0Lt0KpD_ueVQAwyNO019oil3w9dRf1hY5yiGdWgwlWstdnZiP4bBj_eQAAll53_E4xfVF_3b5D3EL-eYJqFqzgezvO6x32G8V0xotusma71_qOtKiSQofaTdZgsKp0py3sM73K4UFUiUeudEuR2Vc2cUE3gmFF3ndXSe65LVT8KreR7wmKvHIVdNiIX04EIYS2V9zfLAciwgmyY9EOWOkguY-keVeE2lDQWG-oqdrXdGj9QZpfB3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان‌باختن ۱۱ شهروند سنندجی در آتش‌سوزی تانکر سوخت
🔹
رئیس مرکز فوریت‌های پزشکی کردستان: در پی وقوع آتش در یک دستگاه تانکر حامل مواد سوختی در پلیس‌راه سنندج - همدان، ۱۱ نفر از شهروندان جان خود را از دست دادند و ۵ نفر نیز مصدوم شدند.
🔹
به محض وقوع حادثه، تیم‌های…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460522" target="_blank">📅 21:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460521">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f1f5d2a46.mp4?token=O4yzn99_GzLSozVim-zzo-EaY260LWU6sidDDdmwBF8ljOzM4ZB4brvlXawNUjMTvPOtKSjCkwR_MxaBHOGfep-XAwcvsUIDFTUYwQRLQkBrcxq2hzIfDp_KkjD2MI7AV8SXKkmsSed4aspWbqRAWRXrkg73modhB519NcGcYrhnLgxJe46hEUV22rasG1P2tnsVy4NfbLwgQuyhzFTKeg3Nq0au85MCRbwHnbGOgT8A5x9NXhyAnGIVSOz_ZB7AX3biHXCWbArONeF-oT2iEg2MYkGt_wzL-d4cGidu9kGTyEAyYJR6Pp8bb1Q72YuD1e2hHLwMnXkJj6IUTt5_XpfF6xxf6ENW_cVCezNmXJhXmMZd6s0Ps1Mem6uckHjFwakCfLuhVwP9bnh-HkjIAxaiLKJ-nHJR80ygaQ34Gh0-yqFn5eD2ngfIFySrIV9QMdcNWzw9CHhso8Ou7xDEA8c75GVtW59Lbhz-gWmO18Tdnc52DM4i2hZmS2M3sD9Is3Qy2GN87t99Khvs2itMw-M9MfdzvddzhZeMQRO5TmLQb4_sfMX9N0np62_6EedTR27PPVSWHt_COR0SY-BFvRnI3_eeQ6izYSPzGk3sekuw1ZfQG63802sbfGIITebdVyY84uUfPaWbFhOHbDeEl_Qqd_9tUC0DyL5Je_F3nM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f1f5d2a46.mp4?token=O4yzn99_GzLSozVim-zzo-EaY260LWU6sidDDdmwBF8ljOzM4ZB4brvlXawNUjMTvPOtKSjCkwR_MxaBHOGfep-XAwcvsUIDFTUYwQRLQkBrcxq2hzIfDp_KkjD2MI7AV8SXKkmsSed4aspWbqRAWRXrkg73modhB519NcGcYrhnLgxJe46hEUV22rasG1P2tnsVy4NfbLwgQuyhzFTKeg3Nq0au85MCRbwHnbGOgT8A5x9NXhyAnGIVSOz_ZB7AX3biHXCWbArONeF-oT2iEg2MYkGt_wzL-d4cGidu9kGTyEAyYJR6Pp8bb1Q72YuD1e2hHLwMnXkJj6IUTt5_XpfF6xxf6ENW_cVCezNmXJhXmMZd6s0Ps1Mem6uckHjFwakCfLuhVwP9bnh-HkjIAxaiLKJ-nHJR80ygaQ34Gh0-yqFn5eD2ngfIFySrIV9QMdcNWzw9CHhso8Ou7xDEA8c75GVtW59Lbhz-gWmO18Tdnc52DM4i2hZmS2M3sD9Is3Qy2GN87t99Khvs2itMw-M9MfdzvddzhZeMQRO5TmLQb4_sfMX9N0np62_6EedTR27PPVSWHt_COR0SY-BFvRnI3_eeQ6izYSPzGk3sekuw1ZfQG63802sbfGIITebdVyY84uUfPaWbFhOHbDeEl_Qqd_9tUC0DyL5Je_F3nM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مستمر مردم مراغه در میدان دفاع از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460521" target="_blank">📅 21:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460520">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a512e5e02.mp4?token=HHJfzsWuKmW4LxbiGf_VPpRFNTmZI6fFoMxMQI-V9oWASygCUnEJ4ecQu_MJP86UPx0kLKKLzQAvm1spSWUsLdatEXj0uMjzziXWl0ICDqtu7nID5akj7GKLU4BNqX3ZuONeYZoTSG9uIlrUlRXZ9V3-GS8lNDthmOzoI8kgX487aKD6JoZE3YPWKI5Q_I0j-svEbIuxdnoFydg51S8VR-kXDjmGyI8NJc0bz8XvVll3nbC3Wf--ZCqQfD8CJaPC0__sxjThLVMmUeZNF7PqBf-QvTbgnsIxqmWXoDxeJvfV40B1u28lTJBaOTAKvdSCaB89sNbigrADFjSwudJ4Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a512e5e02.mp4?token=HHJfzsWuKmW4LxbiGf_VPpRFNTmZI6fFoMxMQI-V9oWASygCUnEJ4ecQu_MJP86UPx0kLKKLzQAvm1spSWUsLdatEXj0uMjzziXWl0ICDqtu7nID5akj7GKLU4BNqX3ZuONeYZoTSG9uIlrUlRXZ9V3-GS8lNDthmOzoI8kgX487aKD6JoZE3YPWKI5Q_I0j-svEbIuxdnoFydg51S8VR-kXDjmGyI8NJc0bz8XvVll3nbC3Wf--ZCqQfD8CJaPC0__sxjThLVMmUeZNF7PqBf-QvTbgnsIxqmWXoDxeJvfV40B1u28lTJBaOTAKvdSCaB89sNbigrADFjSwudJ4Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا و یک رسوایی دیگر؛ تسلیحات کمپانی ریتون در حمله به عروسی سیریک
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460520" target="_blank">📅 21:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460519">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4d1a7eb67.mp4?token=RClVfprpf-W0PhIp5CWG29zR0rEK_ZsabT0_9W_EOM9WxeMMV-_n1dPD7rjc4-YhNZngzoVmt82LAUtQHB7k5RFptT4oZJ4rGW5v4K6jnPKXQmxvqL5IHZ21mnzOmh4d47rog45R9-OKUBSmqAd1qV-WYjmrvkAWT7snYcP13N4MMvlKEwh58jCi-15bu5JjFEs7JrjHiASFkYhZgqz0GBjjOZ36Yol9QAetD5kajv8EYrRIWESUr2vHhSP4GwEvGdFZPy-WE5GhkMnRk14zSgNKOMM1no1WFE8T673LuYtPIgl-rQKsMur_ReyRRxQBCOg4_RUXm6eSWcM3sLCPWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4d1a7eb67.mp4?token=RClVfprpf-W0PhIp5CWG29zR0rEK_ZsabT0_9W_EOM9WxeMMV-_n1dPD7rjc4-YhNZngzoVmt82LAUtQHB7k5RFptT4oZJ4rGW5v4K6jnPKXQmxvqL5IHZ21mnzOmh4d47rog45R9-OKUBSmqAd1qV-WYjmrvkAWT7snYcP13N4MMvlKEwh58jCi-15bu5JjFEs7JrjHiASFkYhZgqz0GBjjOZ36Yol9QAetD5kajv8EYrRIWESUr2vHhSP4GwEvGdFZPy-WE5GhkMnRk14zSgNKOMM1no1WFE8T673LuYtPIgl-rQKsMur_ReyRRxQBCOg4_RUXm6eSWcM3sLCPWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا جنگ با ایران را کوچک نشان داد؛ هزینه‌اش اما سنگین تمام شد
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460519" target="_blank">📅 21:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460518">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1afab8392c.mp4?token=tt3gHbUJJZA8qnBXvyro0wu5qLT-98ObibPZtgqYn5tUymxka1tF1nvb2X0WxYgIXAAWZwaGAwbSs3hCAinTAOBYRPphBNHCfkW88U-Ci59waDFzJz66I0KJUSPV6u2Z-dzZzietrda1DpFz1JhUzj_5t7TPLbZ3FPdYJzHVeYaD4MNuDnIPwz03xOTeAXPhh0Rn2sn6eb00hoXo7aQ2Dp6sd3QFA54DQwjzWpFQdnoj3OiFkSokaLODyvr6dTWDXHmvpMx2WPZbPqfwh1ob5ZH8k73z9PsEV3ncDVEkd7dF8RLYQGsIXD6SanqBQbTnDEa9_sHRih_bDZ2tLbbaKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1afab8392c.mp4?token=tt3gHbUJJZA8qnBXvyro0wu5qLT-98ObibPZtgqYn5tUymxka1tF1nvb2X0WxYgIXAAWZwaGAwbSs3hCAinTAOBYRPphBNHCfkW88U-Ci59waDFzJz66I0KJUSPV6u2Z-dzZzietrda1DpFz1JhUzj_5t7TPLbZ3FPdYJzHVeYaD4MNuDnIPwz03xOTeAXPhh0Rn2sn6eb00hoXo7aQ2Dp6sd3QFA54DQwjzWpFQdnoj3OiFkSokaLODyvr6dTWDXHmvpMx2WPZbPqfwh1ob5ZH8k73z9PsEV3ncDVEkd7dF8RLYQGsIXD6SanqBQbTnDEa9_sHRih_bDZ2tLbbaKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۷ شهید در ادامۀ حملات امروز اسرائیل به جنوب لبنان
🔹
در ساعات گذشته حملات وحشیانه این رژیم به روستاهای جنوب لبنان ادامه داشته است.
🔹
وزارت بهداشت لبنان گفته در حملۀ پهپادی صهیونیست‌ها به شهرک النبطیه التحتا ۳ نفر به شهادت رسیدند که با احتساب حملات اشغالگران به مناطق دیگر، شمار شهدای جنوب لبنان امروز به ۷ نفر افزایش یافت.
🔸
این وزارتخانه پیش‌تر اعلام کرده بود که شمار قربانیان تجاوز اسرائیل به لبنان از ۱۱ اسفند ۱۴۰۴ تاکنون به ۴۳۶۲ شهید و ۱۲۳۷۸ مجروح رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460518" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63356e20d1.mp4?token=JogJNAI6LO7p06MbWbM3Dznbc2I2igP4xHfdOii4r5h2hvgZyFk3a627RETvc8xdM82cKe4QcvqcVAJyUqUrtLwvjnzqILRSO_SZG2PT7b_thY81cWdLaeOqPK1EPtiT01QH0K8Zz821Wp_F9NhpCm5sxfCN8XiI4TaTNVys9lsX-3jmADs24gFE5WltYTxCPyQD-MajLkli4ELwvaQ4MzYRwkQ2LgS_cefvIKLkO_z-rvE89pjNvgFwUTiaT_aaX_-jLfxsTJZdJUGtwL921cwMiMUh2XtOhrU2wB14x8izj3ZCqy2WfNtD6hv-T0r0ct1TsSVrgvwrQLLW2HF7mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63356e20d1.mp4?token=JogJNAI6LO7p06MbWbM3Dznbc2I2igP4xHfdOii4r5h2hvgZyFk3a627RETvc8xdM82cKe4QcvqcVAJyUqUrtLwvjnzqILRSO_SZG2PT7b_thY81cWdLaeOqPK1EPtiT01QH0K8Zz821Wp_F9NhpCm5sxfCN8XiI4TaTNVys9lsX-3jmADs24gFE5WltYTxCPyQD-MajLkli4ELwvaQ4MzYRwkQ2LgS_cefvIKLkO_z-rvE89pjNvgFwUTiaT_aaX_-jLfxsTJZdJUGtwL921cwMiMUh2XtOhrU2wB14x8izj3ZCqy2WfNtD6hv-T0r0ct1TsSVrgvwrQLLW2HF7mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه علی‌السالم</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460515" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/108b3f80c2.mp4?token=XG7LejaeibHNtlfvfOkMVBtl_WcC_MtlkHEOWBgcY7fqC-16_SOPK4qmjb4kntyWqXlVKCjrIr-n27TeUQC2ImWSu6KQgLep3Hv3zNDLYBZxZgAuNxfnsp44a8J4ZuWuyGWguyuOdmNgkvibVwLpboxeib8GHLbGWWM81TU1S_38w-IGjqoZmZuqe-r1KaByJEHA_DO9NyAey2IJ1XQOz_LKBnw6bu_I2B3MnXeHbvzj6rJodyMxJ5i3k17coMITZzErRz-c_-Y1qYFEU2wjLcftdnz5FVDsqtQ3sy-i6k7VH3CCWYSuwe0LGN-0jzwzPmxM2qC6X1NsH_l-Y5gUSgz73P9Fh4x0Y5Lfslo4YgxaUKJNydjBf28N54CanicvFpeARSFo-yPSkxyZlwh_gwvlpyEy6zgpYOLA--2FctUoqG3xsvo9o54s9jPKJk-tQV8GNCuiyYvMqN3E7k0AqxIvqR1i2wdvka29KszDoOxml7UWBBBOIfFkxH54P9JQjEx3hkLAR7xLVyCuPFLSAtnvyAN6_l7E0IhcygbdTbc4KyFA4CYuvE1EpIcDrNRqkCkr8_dw2Dd1z6_KEf_7bVITyBdxNDOeaVezHign7B6oiD3QrhR75PeARCY8NnYRpO0A1SoA2aBtW0rI2KzQAUpnIR0zsa8rKSn1AIEICcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/108b3f80c2.mp4?token=XG7LejaeibHNtlfvfOkMVBtl_WcC_MtlkHEOWBgcY7fqC-16_SOPK4qmjb4kntyWqXlVKCjrIr-n27TeUQC2ImWSu6KQgLep3Hv3zNDLYBZxZgAuNxfnsp44a8J4ZuWuyGWguyuOdmNgkvibVwLpboxeib8GHLbGWWM81TU1S_38w-IGjqoZmZuqe-r1KaByJEHA_DO9NyAey2IJ1XQOz_LKBnw6bu_I2B3MnXeHbvzj6rJodyMxJ5i3k17coMITZzErRz-c_-Y1qYFEU2wjLcftdnz5FVDsqtQ3sy-i6k7VH3CCWYSuwe0LGN-0jzwzPmxM2qC6X1NsH_l-Y5gUSgz73P9Fh4x0Y5Lfslo4YgxaUKJNydjBf28N54CanicvFpeARSFo-yPSkxyZlwh_gwvlpyEy6zgpYOLA--2FctUoqG3xsvo9o54s9jPKJk-tQV8GNCuiyYvMqN3E7k0AqxIvqR1i2wdvka29KszDoOxml7UWBBBOIfFkxH54P9JQjEx3hkLAR7xLVyCuPFLSAtnvyAN6_l7E0IhcygbdTbc4KyFA4CYuvE1EpIcDrNRqkCkr8_dw2Dd1z6_KEf_7bVITyBdxNDOeaVezHign7B6oiD3QrhR75PeARCY8NnYRpO0A1SoA2aBtW0rI2KzQAUpnIR0zsa8rKSn1AIEICcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وحدت، رمز پیروزی مردم ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460514" target="_blank">📅 21:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7daee69212.mp4?token=P9HBGvbAIkt8H3Zf6ImOEhRFqa3qwJRPbiSfvCrj-0XYTnuz7PqI1tamljG0xVZnIIo53b0-aaJQmvUdesGDGs34_A8JbzwUMUX3nn23_87UT3XNn2uHXRx59iobNvJyvX0kiI92YbUdjtFWW4yhhiPKJGhIaHt2oj0gvRCEMuzagD9r4i950wTquWF71SK7l0G7fVwXQTvpFIuISMIp_oCP0DbMhiHaR6EzqRquHmI5zDo_0xrIMNI-C8UCqHz2ASwssiQLd6sJMXt9auGpzXrNO4QKv-AvPxuOKh4zTlXnj3VPD1nUIcitd44kzKplwA7Wmr9kd0cHjjg6S5u0OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7daee69212.mp4?token=P9HBGvbAIkt8H3Zf6ImOEhRFqa3qwJRPbiSfvCrj-0XYTnuz7PqI1tamljG0xVZnIIo53b0-aaJQmvUdesGDGs34_A8JbzwUMUX3nn23_87UT3XNn2uHXRx59iobNvJyvX0kiI92YbUdjtFWW4yhhiPKJGhIaHt2oj0gvRCEMuzagD9r4i950wTquWF71SK7l0G7fVwXQTvpFIuISMIp_oCP0DbMhiHaR6EzqRquHmI5zDo_0xrIMNI-C8UCqHz2ASwssiQLd6sJMXt9auGpzXrNO4QKv-AvPxuOKh4zTlXnj3VPD1nUIcitd44kzKplwA7Wmr9kd0cHjjg6S5u0OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناوهای آمریکا دیگر رنگ اقتدار نمی‌بینند
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460513" target="_blank">📅 21:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
نرخ سوم بنزین ۱۰ هزار تومان شد
🔹
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد سه‌شنبه به ۱۰ هزار تومان افزایش خواهد یافت.
🔹
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومانی بدون تغییر ماند؛ افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/460512" target="_blank">📅 21:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4bd29631.mp4?token=jvltqJqF8_OksRw4XPO3wz8xXnC7BMrS84sDiaQBZNL5eQ8TuKx20KykwMiXpWgQbkuyk8uBJDZqccBxGkqnw2zIB4YMt92hTEyfUhFKU6MknPuFGcu4OPE-MIcX2A3mrjmuU-rs3Bq1O_GRgn7IlE7Sd5c9NxFM7ysE-FTcV6x3YD_5aI1zkcjTbiRmwLaqjgQKsudR5t8zTy97dizt43ACW_aB9DFeDt9qRS1464l2PzIjW9i3WPY_r-DS8_2a2PuCPy3RhmK7ZvlgtczydsbG4Msx3FSXG5mexu1EHcmrsMNbNf4Ic6YJ5rTgMMIkjhadXiu75WsDYiSihgs11WO68hWngOro2qEBAOohEpAJx6H_4YHT8y4-aEVLnGFkjoIN5R7J418Kvsl5TD6O6Bn2v3yKEk0SP7zHW7XeXQQw0ilR75cscUYS43T2fEF_4UnkPie2nAMvbqXRIAYX_hSSZZSerISGJ5DDWxpAgFlwuB0n9HaWC65OsLoOmhbwcir_iC2v-4FaBzG_pQRLFxqM9NkxYTU2gXxrddV4fbbx2SdU3XKy3t-gV-VrApD9zRNgp_b_QbDUrZd8u6VC4c6dKuufi7K6Duf-QRyxGKtRVIU985chK-CSF3hYW9htUNrJGxo39zOSAno9Mdeo4H64RE9gxAlcSxtdtwAfEBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4bd29631.mp4?token=jvltqJqF8_OksRw4XPO3wz8xXnC7BMrS84sDiaQBZNL5eQ8TuKx20KykwMiXpWgQbkuyk8uBJDZqccBxGkqnw2zIB4YMt92hTEyfUhFKU6MknPuFGcu4OPE-MIcX2A3mrjmuU-rs3Bq1O_GRgn7IlE7Sd5c9NxFM7ysE-FTcV6x3YD_5aI1zkcjTbiRmwLaqjgQKsudR5t8zTy97dizt43ACW_aB9DFeDt9qRS1464l2PzIjW9i3WPY_r-DS8_2a2PuCPy3RhmK7ZvlgtczydsbG4Msx3FSXG5mexu1EHcmrsMNbNf4Ic6YJ5rTgMMIkjhadXiu75WsDYiSihgs11WO68hWngOro2qEBAOohEpAJx6H_4YHT8y4-aEVLnGFkjoIN5R7J418Kvsl5TD6O6Bn2v3yKEk0SP7zHW7XeXQQw0ilR75cscUYS43T2fEF_4UnkPie2nAMvbqXRIAYX_hSSZZSerISGJ5DDWxpAgFlwuB0n9HaWC65OsLoOmhbwcir_iC2v-4FaBzG_pQRLFxqM9NkxYTU2gXxrddV4fbbx2SdU3XKy3t-gV-VrApD9zRNgp_b_QbDUrZd8u6VC4c6dKuufi7K6Duf-QRyxGKtRVIU985chK-CSF3hYW9htUNrJGxo39zOSAno9Mdeo4H64RE9gxAlcSxtdtwAfEBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا آمریکا به جنوب ایران حمله می‌کند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460511" target="_blank">📅 21:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460510">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJCkSmyOQRhRXpjC90fr7GWP68tohQ00r4AoDfCU9FBFDblD7AhUb-Nz5076kbabcjsGHhYkOgsLoCJpDwMc8nwtoUwz374Vjj9QubO1lRPkGnM2ibOgfaDyE9XZ1h9SbMDF5RoKDV-DZWDI0q7vrI-IgjuEYpFGmpVYbQAo-I-7Er6Ibh6FgGTjEx5tc_7Q2NVYjUN5J4PJamumszP1Mr67OAhRELQW1MTcMcLhdmVGf-35mC1cilFrDDL0CtlHPDjKR_QzcDtqXycikJswPfU8P0uM_InlCsoERXnG3kyn33VzkHsx5ZDhDh4l2d2O_cFoyQrDM3emXla7jW1vGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سومین مساوی پیاپی استقلال
⚽️
آلومینیوم ۰ - ۰ استقلال
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460510" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460509">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb438e094.mp4?token=SaqTYzHuZAkElGRBAEH0g74hU99VNtxkHZwBoCaXTy6-Mww6puULo9K9tRCHLpMaWqvudHQjiAavUgzvVW2GHC74bols0rjz7t2J2k6H1YhB-tRkrYSVTpI40r9rETklQ6B2SKIq31OMs-pfZ2VkFCT143opHrye_siboHy-YDyiCe4kyNvvwZNexL7Zzz-hs_PWyVSczztMToSskM4G5f7BVjTdU5XNoEIlplWh97xA6MjGN_Pz5FophqLw5V2pns5CoQxFxbVUvUy5lpmxpXHip8pfKXkhD_3lQTZdCbHZopGdhKtX0PeGYZN1ahf7skNqg53iLu9i5RI91ILtLoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb438e094.mp4?token=SaqTYzHuZAkElGRBAEH0g74hU99VNtxkHZwBoCaXTy6-Mww6puULo9K9tRCHLpMaWqvudHQjiAavUgzvVW2GHC74bols0rjz7t2J2k6H1YhB-tRkrYSVTpI40r9rETklQ6B2SKIq31OMs-pfZ2VkFCT143opHrye_siboHy-YDyiCe4kyNvvwZNexL7Zzz-hs_PWyVSczztMToSskM4G5f7BVjTdU5XNoEIlplWh97xA6MjGN_Pz5FophqLw5V2pns5CoQxFxbVUvUy5lpmxpXHip8pfKXkhD_3lQTZdCbHZopGdhKtX0PeGYZN1ahf7skNqg53iLu9i5RI91ILtLoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تروریست، تروریسته چه تو یک استودیو شیک تو لندن نشسته باشه، چه در روآندای آفریقا
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460509" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460508">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWKx3Igp1BpVnKD-oOxPprmh0fnozOSTLcU7tiPkr-zaWjNil2tn7TbJ1KuwoPkXLCoycn6AnjBLPaVDHipV8pmwI5pHggHrEua4Tzg4IMHZVBOSQrlKbHdP3nMZYOLQoUiWqZXqH9jef8bRRaJeSbTYWR7PEoAs0k26DC32o39W3tAVheRxh-4PL_B7Aw4wcI4y3d6KNtgIY-uwt-Plq95UlVtqJf_k0ruN5eQSwLNmEXV8B51EDN71P4pLRxUIWqOMsPagepGHJ8mEsLem2pElAjCe_ir5NYSnYyioPMkLniRB8B8IrSvazFjOshfTi-fW6BR3OtryDfABcks-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی خطاب به ویتکاف: بیشتر به اینجا بیایید تا اوکراینی‌ها بتوانند بیشتر زنده بمانند
🔹
رئیس‌جمهور اوکراین پس‌از گفت‌و‌گوی امروزش با ویتکاف و کوشنر، نمایندگان ترامپ، از پایان دور نخست مذاکرات با هیئت آمریکایی خبر داد.
🔹
زلنسکی در پیامی که خطاب به فرستادگان ترامپ منتشر کرد، گفت: امروز شما حتی بهتر از سامانه‌های پاتریوت برای شهروندان ما که در پایتخت هستند، عمل کردید.
🔹
متشکرم؛ بیشتر بیایید. این‌گونه مردم ما فرصت خواهند داشت که کمی بیشتر زنده بمانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460508" target="_blank">📅 20:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460507">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d29d757f18.mp4?token=VW6K7pzjPnnHHZyxRwwXGylmaVdqvuu7jbqHNhha0IsXvM9C236GK6B5ZGf80-Uw0nzWvO6Shg5E4iH1PxyUcpHmXkjZQASPMPCrmND3zcX_VLvv6plUA1p-oFrQNLbY0miILMZoQQWq5AkvAsEOEi1FpMTVRQqCyaFsKY66iefXGZoTkUYmcEUfPZo--Lk_EzSD-dZ_WD8lPGSk8gi1COyvFMmHPNz2XiaCox05DvBGJo1BPXYDe2e2tBtdvwxuaOgW1sHM2LtEzeJA0anrl1yk6YRopi9oViTgze-3PMREh4zvbA4BAL5IMoSRcQphbeTqGMwyYS5muaVBhMwMSBxRXxVDLSC_R1GkVTE9DzzXrcveorMWC2HVfh24ee4AS6N3S-VgOkDqoMIOmwvBQJLpTWCm_mSXYHb7tgpa2wSC7MjHUkqxdObb3OpbnDD93u8n1dVLNLcA8BUrfR5bJ65pFjXu_D48U2swoQx_h7YvUqJHUN1Tmugh8r6qLJVCELK_OmbbmfSpDejlepnSHrK-C7Xu-lIRFsH7aIWhr23BrXHG-r8RWQifWppl1AQvzzbZNmwAWq0ddicnx17EB3Nc_r-8ZsbMsJ2Zc8EaX9Knsj9n3kB-8x2g3lw_n6T1v0QRVg_QhE6wWS1und9_yGv9prmMQYcYAG5M_6YHeVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d29d757f18.mp4?token=VW6K7pzjPnnHHZyxRwwXGylmaVdqvuu7jbqHNhha0IsXvM9C236GK6B5ZGf80-Uw0nzWvO6Shg5E4iH1PxyUcpHmXkjZQASPMPCrmND3zcX_VLvv6plUA1p-oFrQNLbY0miILMZoQQWq5AkvAsEOEi1FpMTVRQqCyaFsKY66iefXGZoTkUYmcEUfPZo--Lk_EzSD-dZ_WD8lPGSk8gi1COyvFMmHPNz2XiaCox05DvBGJo1BPXYDe2e2tBtdvwxuaOgW1sHM2LtEzeJA0anrl1yk6YRopi9oViTgze-3PMREh4zvbA4BAL5IMoSRcQphbeTqGMwyYS5muaVBhMwMSBxRXxVDLSC_R1GkVTE9DzzXrcveorMWC2HVfh24ee4AS6N3S-VgOkDqoMIOmwvBQJLpTWCm_mSXYHb7tgpa2wSC7MjHUkqxdObb3OpbnDD93u8n1dVLNLcA8BUrfR5bJ65pFjXu_D48U2swoQx_h7YvUqJHUN1Tmugh8r6qLJVCELK_OmbbmfSpDejlepnSHrK-C7Xu-lIRFsH7aIWhr23BrXHG-r8RWQifWppl1AQvzzbZNmwAWq0ddicnx17EB3Nc_r-8ZsbMsJ2Zc8EaX9Knsj9n3kB-8x2g3lw_n6T1v0QRVg_QhE6wWS1und9_yGv9prmMQYcYAG5M_6YHeVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در پاسخ به یک سوال بنزینی اینگونه پاسخ دادند
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460507" target="_blank">📅 20:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460506">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305ff823b4.mp4?token=Zbq7GMEsQG-p-zUzgoCeo6Ye8OFfVqFD01oYErlkZfN3FqVYHsqsPE_lDv8irJmqCz6KIeChdKQXReTI3327LjaKFu3WcKb-9PzRcxyP0k-o_Gy4mtA8pqxVLYYZF9a89j5L2Jg8r1zt4HDU_r0Q6FerhuIedsSdBCYWT0z8ma34a5P9PT0v_93xA0jKW-ZBw_A6cqdZqRjITmbcOTKKrUgx-sCsr1i3eYSrcEviDR7Dj2F_Y6P1g4L2tGe9zecGmEMKglbSOWkWdA--HBtmUsdDrQsOlkrttWTYQuO_vbkHPDrEXbw2VqERxoygDc5KN4JxuaUYBif3RbXMijIt1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305ff823b4.mp4?token=Zbq7GMEsQG-p-zUzgoCeo6Ye8OFfVqFD01oYErlkZfN3FqVYHsqsPE_lDv8irJmqCz6KIeChdKQXReTI3327LjaKFu3WcKb-9PzRcxyP0k-o_Gy4mtA8pqxVLYYZF9a89j5L2Jg8r1zt4HDU_r0Q6FerhuIedsSdBCYWT0z8ma34a5P9PT0v_93xA0jKW-ZBw_A6cqdZqRjITmbcOTKKrUgx-sCsr1i3eYSrcEviDR7Dj2F_Y6P1g4L2tGe9zecGmEMKglbSOWkWdA--HBtmUsdDrQsOlkrttWTYQuO_vbkHPDrEXbw2VqERxoygDc5KN4JxuaUYBif3RbXMijIt1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر بهداشت: شهر میناب دچار سوگ گسترده شده است
🔹
تیمی در وزارت بهداشت مسئول رسیدگی به آسیب‌های روانی جنگ شده است. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460506" target="_blank">📅 20:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460505">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0f21f01f.mp4?token=GnIjtHZhnf-iU8IqQAhxz2UCA--XNtmpRCIVIaLUkGnkxNKAn-s8AtRJuhGotbLmNF5NCFMThAoYda-366HjwAHzOswaSZ70gsDCWglzVwVlAO1L10SEDkKllxiw3nt-1ksJxA_CjHhSq0sADEjdpCfPVPfkzHuKgz3sHWF-sKs-w9Kre8-MTaIaOQ9ooIloVhTRzeaXN-seC9GuOTp3Cm7Pl3MKGCWpZuihK5nCPvJmg1dpM_wZtQ1HQopm6l1e3q905SQYlt5BHuRw-UeNxOSFhOqpBmgY29cSAcAwAsr9Ihujfbn7khOj1sn0dsq8c_TjZ03i_Tg9VdM53UOX1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0f21f01f.mp4?token=GnIjtHZhnf-iU8IqQAhxz2UCA--XNtmpRCIVIaLUkGnkxNKAn-s8AtRJuhGotbLmNF5NCFMThAoYda-366HjwAHzOswaSZ70gsDCWglzVwVlAO1L10SEDkKllxiw3nt-1ksJxA_CjHhSq0sADEjdpCfPVPfkzHuKgz3sHWF-sKs-w9Kre8-MTaIaOQ9ooIloVhTRzeaXN-seC9GuOTp3Cm7Pl3MKGCWpZuihK5nCPvJmg1dpM_wZtQ1HQopm6l1e3q905SQYlt5BHuRw-UeNxOSFhOqpBmgY29cSAcAwAsr9Ihujfbn7khOj1sn0dsq8c_TjZ03i_Tg9VdM53UOX1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر بهداشت: در بحران‌های اخیر ۶۶ هزار مجروح را رایگان درمان کردیم
🔹
در جنگ رمضان ذخیرهٔ خون ما ۳ برابر میزان استاندارد بود. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460505" target="_blank">📅 20:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b058a2a7.mp4?token=CQtwI9zN6Mq0R8jKrUX-6ylpCI9k9AZGrrLP-ulg_7VZzlk1ZPY6iVtzyC7W1qUFmRA6UgfRwf60jKJgt9bSrk7UA5trqUE_V4LagMeVdbjEbpBaw0PHaxS_mL-q_V2ststaKKSdeC0dI-hNeKAKSCxbH55En2owGrkbEHUnUvzzlJkoy_hIPnON9rrt6CqRv1yp9b6ytlTnJ9uyKa6exWurt23_Jee7aaOKYV0QAPMjtShOWkwKQvoYPYfeJjaTyBM6mkJtalW8KmhVE_n3OGvLWCdBgqVvv5R86iSPZBoc1sU-zEbSWNNDecIf4T5zaTwupdps59aql8eqBZG7jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b058a2a7.mp4?token=CQtwI9zN6Mq0R8jKrUX-6ylpCI9k9AZGrrLP-ulg_7VZzlk1ZPY6iVtzyC7W1qUFmRA6UgfRwf60jKJgt9bSrk7UA5trqUE_V4LagMeVdbjEbpBaw0PHaxS_mL-q_V2ststaKKSdeC0dI-hNeKAKSCxbH55En2owGrkbEHUnUvzzlJkoy_hIPnON9rrt6CqRv1yp9b6ytlTnJ9uyKa6exWurt23_Jee7aaOKYV0QAPMjtShOWkwKQvoYPYfeJjaTyBM6mkJtalW8KmhVE_n3OGvLWCdBgqVvv5R86iSPZBoc1sU-zEbSWNNDecIf4T5zaTwupdps59aql8eqBZG7jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر بهداشت: در بحران‌های اخیر ۶۶ هزار مجروح را رایگان درمان کردیم
🔹
در جنگ رمضان ذخیرهٔ خون ما ۳ برابر میزان استاندارد بود.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460504" target="_blank">📅 20:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460503">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKc_fekdHYuLhCWFlZNQ5CcRdctyjCr7JO7tjXztOEG_MfEghRPMuRdT2H_9wUjrr7Pk-v9D_sNnjOwFodmjFz2vJgsmaWD44CQ5YmOgY_kTQ_1F2Yva7pcW5nZWWQNttknN8u4Dfjiu7CeJk_11gZY2o2kUtpB8viJzqyM66qsicWTKH6B7AYzuIbta61iXUamQiy5342-zztfCkoM3dSJsbSKR3EvW28L9QhUPuzIKW37LtuD5Wmb5RSKjsHS6D58ShebE9yV86p-6EQ63aXoC0lXuyo-bb_kIAQrsMTG1jeySS1VxpgYDuypCLzwwafL1blsHXo2wQ4k_IZOUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرعه‌کشی ۴ محصول سایپا انجام شد
🔹
در طرح فروش فوق العاده، سایپا ۴ محصول چانگان CS۵۵ پلاس، سیتروئن C۳ XR-V۱، کوییک S و سهند S دوگانه را عرضه کرد.
🔹
فروش محصولات سایپا در این دوره از عرضه در قالب ۳ سهمیه متقاضیان عادی، طرح حمایت از خانواده و جوانی جمعیت و طرح جایگزینی خودروهای فرسوده انجام شد.
🔸
ثبت‌نام‌کنندگان با‌مراجعه به
سامانهٔ فروش
می توانند از نتایج قرعه‌کشی مطلع شوند. نتایج به صورت پیامک هم به برندگان اعلام می شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/460503" target="_blank">📅 20:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460496">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxNvdzpFYztpHKCHl05-UfPf5PfwDe20thgHm6-7mN95BkrZk2iv09OmaFGDRzh4UB2Rf8jVskn8Z7XWC6WQCT6xpSV46vfSMLyzDTXsj67c9BYl2xqyfNNszIh281rkZsKm4_wxIknfW3zPOtJnEUyaSUgXSm7-D3YGDFPwsWOIdpNGh5_FZNHDNhode0_AujVlVN6qkfnDWuR4ir0o1WlJYXB0cVkQXhRe_PSxSAkH7yHQ7j3FqyskRqaudQ4VPgRZlS9QakOEHjj5GtHg7PhGsrEkEyNDTIEIlhmb7Sy92rtVYl2QHsH-2CJ7AkZW3wlHvSNfZP1ChNDr9jgxxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpEBzQdNGinBTLe3uvuAiWezuSEFrHj4taYCgDRom6KcQG6W8nIvAfelzKnL0pYIT63m8juUkyBdpZ1-7SjxxcIGDBBBQ8RgE0QaS4ZOW_Prdc0v6JpfnUuvVUkx5cnmggrzc9CEKEplCHixt3yTRRM_3JgLxVF7rv4i9-uDxnDYUvPJwSggAHyN48acLzL5iZNGMKTeaST2hDZttU0CFDap0N7maj-eZiIgOyb9xzby_Z_iNY6FsyF5DbNfUduOiPYo-ZL1vHnbZDqHcIe553YURtEYHp3gXLpxNJwyGFRNeDuOwSS_0GJEpqKiNZBQyHwZ8BSFzUV78RbNU_YASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJtlE7GhYvgi9qULTWzOk7yzogTgqnTgxtCLR1O5uW0tq74pD-xpJ7OCsMVe8APZfffioK046k3gVAPO6HmiHVOVMdMe7ZOwzkvUN9tTbBfJfqaEQCohpCEWQGcOtRCMvHLDc965wKYphJHZn9zOexoYIQXVgp78fNmQvzaLSxdkyZQ88wUV5ewSDPQlCqIIvgHJInSYbhMcfwrR45pvnNfWNwfyqe39jY75vnxS5UkofxTHcJ8k3gvybC_hOIpiahPMxJ_Q5Zzx3JK1CRJP_8UVJHed6L-M7ru4Cr__wZ64r5m0s-XkC2zULErNRgta3TCAljDlTZsb4NjAPnyMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/us3UXMdQ4RJqrT99wGtOphZh2fBeYCXOe8ZfdpO2HCmwusr9Es1SuIvaXVon9pvZv-5Ds_pV1M684iP3Fd-gzHL2upUtGeFLHar_MokFyl8nYzieHF8qkRAeaSbT_riXnma9ad6gP4-eg7YCJ8cY7tMxE4ZMPjTCcFZ-Nra77aXawxFZzAgHgFE-J0SBI_bDzHkmDcG8IQBVLCykVM05SWba8qM8uDvMFBeTlEpyaglHpIUg9-p8wRVDDuILuLVPVuGfrZSW2VWkA6gqIZHP4CAs0g4NN_riOKZ1HdEPtOvKg8Qh_FwUIxpSAAFGeW4LEfPG9mZuPwrYKbQU-PpvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otGyLUt600hJ_X2xHh2maCjlA7EL5fu_KqKij0yOYd_p8xIsc4xhl_52aheldAYeFsEFyewNM6Eat4HQNbYVIFBBHMQVLwgURH2zjIKDmPbvlbbjlyaxqQtMRtyvEEQC5pG3cuKIZ4Bs61LnR81eLHqCBsgt2R82Aer_AeqgaYdI1_WX5HACrvmp3HYe7zTj5qLpJHCFDM9b1jbcEj787FCvp9SBq-KqjssocnQ3T656QDuN4yxK_GaT-e55Bq6cACAjVmm8FDig-gCAGWFxFy8WqYAYVUxk-boly7bY30vy8XBLZ9AWEnWOmBhS0z7d4WxnO6g29gBLB95ThShkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFNH_VgfYE-_J8LiudA8txmJz4W_pYiIGq37IBsNz27jneXwhdDc7bKMLX0jobPVS4vslRS2RbXD2twEBbf-4tCpJ59Il6XRrj-DeZWErdSxS6uUz9AqmWYc09jTUJICj5CMF4FivKHMEQHEmHtF9aG4oqGQ_-pZUhjEnqNjUPBFPzq90smEPR3bwHhGkqXENjHO9olnpdKFCXZGSdP0CCHylhyKdu9OumrlnjLfRKWWORmeNW1tuo65Fql-ttWYw6OP8jIe8X1R9Q4F8BViRE1a7WGJDV9TCh6bdx00zbas-coMIy_4SrQ98doOzmRNZsit8IjSKM-CHGH9p2EDnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ouGRaiPlNko36B8cWvIuMsv-P5j6n__JY7dGjfnjh8amnYUktx-uP0yi-GBc8hpJATxIVMEi5v0E7lfejBDeE9P9I7JzCkXg0lX2PIUdbW3666WqVCaMmXexAWRPM4uC4YCwIhW5oI9gv3ZB_m50GLPfuuY16ruxB4GcUzs1ninxhX4yy730fbzdWdAzAf5rta-S4OY1FPy6-vVx5hN6psK1s5LWYsHDZfGre4gT88NLI00LpTrKb4Da_P5TfrLEsH0iTS1q3MSFVTsBSro2wMBfVj-wqNIT_q59FO98b-7oNO0XYeO5DbFJlYeiiOqi8ADDIHDbhehd-0MD1XvM0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تنگهٔ هرمز در قاب غروب
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460496" target="_blank">📅 20:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460495">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bM2rnrPKnkFAEwu-VUJ5_-uUdvjg1XE_onI_HJ7nUUkAhmxWko85-pxl6vxqGL7cjuQJ7iQsQuBHY-Vad92hxpllhmzlyGyQf-TDoMSslk5I3Xiano5CG5zDbwv1r5kV1rWjzK45A-xfyqb8Epe3-fkRSeRoZUSSSDPLdgmU3hCQvq-2kV6CStfUGV-0m3B6yCy73Aw4MVBdUrHUJhh-T8yr9arnjyFHfQf6DSt3pEiAW1ahn-lpCQZ7-csQv2Y-vb1_V6cstrRl567QObJiMRwvUrYFo_WAiTqNXhQ6-DpIuYLP0TbQlPnXSYER7TFjTfEqcak3K0_XaTR6gUx8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به آب شیرین محتاج شد
🔹
جنگ اخیر نشان‌داد که زیرساخت‌های حیاتی رژیم صهیونیستی، از جمله نیروگاه‌های برق و تأسیسات آب‌شیرین‌کن، در شمار نقاط آسیب‌پذیر این رژیم قرار دارند.
🔹
۵ تأسیسات آب‌شیرین‌کن در پی شکوفایی جلبک‌ها و آلودگی‌های ناشی از فاضلاب غزه، پرسش‌هایی را دربارهٔ میزان آمادگی اسرائیل در برابر تهدیدات غیرنظامی و طبیعی برجای گذاشته است.
🔹
علت اصلی تعطیلی این تأسیسات، نگرانی از آسیب‌های فیزیکی ناشی از تجمع جلبک‌های رود نیل در تجهیزات بود.
🔹
سازمان آب اسرائیل با استفاده از منابع جایگزین مانند دریاچهٔ طبریه و چاه‌های آب زیرزمینی، تلاش کرده کمبود ناشی از بحران را جبران کند.
🔹
اما این اقدامات نشان‌دهندهٔ استیصال این رژیم در مواجهه با بحرانی است که ریشه در سال‌ها بی‌توجهی به تنوع‌بخشی منابع آبی دارد.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460495" target="_blank">📅 19:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460494">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/689e5c44b2.mp4?token=Cg_1RvUnpQ86ZMfHFvn3i0f4WdpazA3FQcxPg2pYMeRPhYTPS-0xTjRCABt6n15F6LzohcT5twlVhTAAKzyeUMj680vXtGBpLdmqjXEnZAXxOWz39Ur5hB3_sUzDJx2hLu7BVb1eUFS5e1iZtQ5vQANvORkCux-AL5VuF9oEmgKQsXGeLqEw8ynzGnX7tLNWhp0IcG2yKVfvEQC1D4so-JRTDePP5dJGtLwYW-k-eHADEYGk84SEMADVMtBNkGwUdb-kUE9KU8vgpmEdy8wxE044f6ghqVZenxypoB2ayjEbilpeyRrGMfj8wn8nas01MUgd6WwJEM-ctL6LkaHDag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/689e5c44b2.mp4?token=Cg_1RvUnpQ86ZMfHFvn3i0f4WdpazA3FQcxPg2pYMeRPhYTPS-0xTjRCABt6n15F6LzohcT5twlVhTAAKzyeUMj680vXtGBpLdmqjXEnZAXxOWz39Ur5hB3_sUzDJx2hLu7BVb1eUFS5e1iZtQ5vQANvORkCux-AL5VuF9oEmgKQsXGeLqEw8ynzGnX7tLNWhp0IcG2yKVfvEQC1D4so-JRTDePP5dJGtLwYW-k-eHADEYGk84SEMADVMtBNkGwUdb-kUE9KU8vgpmEdy8wxE044f6ghqVZenxypoB2ayjEbilpeyRrGMfj8wn8nas01MUgd6WwJEM-ctL6LkaHDag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر انرژی آمریکا گرانی گازوئیل را تقصیر اوکراین انداخت
🔹
رایت، وزیر انرژی آمریکا: حملات پهپادی اوکراین به پالایشگاه‌های روسیه مهم‌ترین دلیل افزایش قیمت گازوئیل بوده است.
🔹
از طرفی دولت بایدن هم بیش از ۱۲ پالایشگاه آمریکا را تعطیل کرد که باعث این آسیب‌ها شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/460494" target="_blank">📅 19:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460489">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پهپادها، چشم بیدار ایران در تنگهٔ هرمز
🔹
مرکز عملیات UKMTO تایید کرد، پهپادهای شناسایی ایران بر فراز تنگهٔ هرمز به طور مداوم در حال گشت‌زنی و رصد تحولات تنگه هرمز هستند.
🔹
امروز ۴ نفتکش که قصد عبور از بخش جنوبی تنگهٔ هرمز را داشتند، از این کار منصرف شده و به سرعت از تنگهٔ هرمز دور شدند.
🔹
طبق اطلاعیهٔ UKMTO علاوه بر پرواز پهپادهای شناسایی، نظارت هدفمند بر کشتی‌های تجاری و هشدارهای VHF نشان دهندهٔ قصد ایران برای تثبیت حضور در امتداد خطوط ترانزیتی کلیدی تنگهٔ هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460489" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460488">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsDoUHkSa-vm15aukbUuTerh5Gc1g0k75d9IEf9-oZF51jIxAhouiirrI20o34J1ZBa1mFmVUjk4wYACBOSSVAkkH0_LgYFi_do2mEcRRgXhAjafEtMcueE170GllP5xce3Tz2ds4T74flve17-4xcW319BBdyTymCgJc_Fuf3d65f-DgJaaeCvwFF-QQUPQJd8MZ5A21nzpeMsdoTswDz6oagFYYk-XGiiUA33FEGjFt3WH4xZR8SHNbF96JyuD7rsU01ZUJ6YspNaLYmJAPOf_dHy6uZutkDS1QyoNiuCZ4_hbBAEx8HKJR83vh0up-gOy_n7EUmYRBpm2iCOK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف در پاسخ به خیال‌پردازی‌های بسنت دربارهٔ نفت ۴۰ دلاری: قبل از ارتفاع گرفتن، حسابی گرم کن!
🔹
نرخ گازوئیل آمریکا به «بالاترین نرخ تاریخ» رسیده است، وقتشه یه فکری کنی!
🔹
ژاپن که بزرگترین دارندهٔ اوراق قرضه آمریکاست در حال فروختن اوراق با حجم بالاست؛ با این سیاست اقتصادی ژاپن به ضرر دلار، بهت حسابی خوش بگذره!
🔹
نروژ که دارندهٔ بزرگترین صندوق ثروت ملی دنیاست، در حال فروختن ۸۰ میلیارد دلار از اوراق قرضه است. بهتره اسم نروژ Norway هم به آمریکا Americaway (مثل کاری که با دریاچه انتاریو در کانادا کردند) تغییر بدی تا یک کار موثری کرده باشی!
🔹
نرخ جذب نیرو توسط وزارت جنگ آمریکا که در واقع اسراییلی است به شدت کاهش یافته و با کمبود نیرو روبرو شده‌اید، یک کاری کن. شاید بتونی از طرح پیشنهادی اسراییل برای جذب نیروی جوان امریکایی در ازای بخشش بدهیشون استفاده کنی!
🔹
در آخر هم اینکه اعضای کمیته سیاست پولی فدرال رزرو چراغ‌های هشدار قرمز را روشن کرده‌اند و درباره روند آتی تورم و افزایش نرخ بهره صحبت می‌کنند (که با سیاست خزانه داری در تعارض است). عجب وضعی!
🔸
بسنت، وزیر خزانه‌داری آمریکا در واکنش به انتقادهای دربارۀ بسته‌بودن تنگۀ هرمز و گرانی نفت، وعده داده بود که امیدوار است بعد از پایان جنگ با ایران، جهان شاهد نفت ۴۰ دلاری باشد.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460488" target="_blank">📅 19:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460487">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
حمله اسرائیل به یک خودرو در جنوب لبنان
🔹
رژیم صهیونیستی در «النبطیه» یک خودرو را با پهپاد هدف قرار داد که به زخمی شدن چند نفر منجر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460487" target="_blank">📅 18:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460486">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIs6G17dgqw8pF_eXbz8I-KWHoXldi2V9RRe92OrIgtWv5_LzKC9HrME4PnFEMXCzWAUpcWtRl3h80PEVZKpi_-EkOeuIFq75DgILxcJ5Bl8gBJ78b7TsTvoFkJdfL_YwSX_TlqYViK5ACaBCVpATuygkBIHijY7wZpFUhKVDxG-sqr5yWjuPIu37EDESwb0cZmeD39VpeQuO6f44dNEAanCQclL_E99hlZb4pnstczNjsQSr4XLKwFH8leJVpvk8xPpMy8AfQAPxtZrO2XRIE8x4YwWbRy5oUG53wcGDBPZSQy3P8DnACVtg19CGFMT8g0odvMtYk5PXBbFZiFgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زن نپالی وسط مراسم ختمش زنده از زیر آوار سیل پیدا شد
🔹
یک زن سالخورده نپالی که خانواده‌اش تصور می‌کردند در سیل ویرانگر این کشور جان باخته و مراسم سوگواری او را آغاز کرده بودند، ۱۰ روز بعد به طرز معجزه‌آسایی زنده از زیر آوار خانه‌اش نجات یافت.
🔸
به گزارش رویترز، «چاندیکا کوماری شرستا» در روستای «بتراواتی» در میان یکی از شدیدترین مناطق آسیب‌دیده از سیل، زیر آوار خانه چهارطبقه‌اش گرفتار شده بود. امدادگران روز شنبه پس از شنیدن صدای کمک‌خواهی، او را در فضای باریکی که میان گل‌ولای و بقایای ساختمان ایجاد شده بود، پیدا کردند و پس از عملیاتی ۴۵ دقیقه‌ای به بیمارستان ارتش منتقل کردند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460486" target="_blank">📅 18:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460485">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52eee8023.mp4?token=WBpfI1rghIvXH7wauTv46CAsPrfiIdcBSktVkhux3Aibac36_I4NfXBkDktiv051FzSra3VDQE3HK_yjkffdIadY8QCaE3eBOVxTzCrdmUUy4Vo-eC6cJ4nOOXDWH6MF23KfUR_iVDb8m2-XXYGMYGXnQuCb4lZUBslgqM9hKUxR9AZg6svPmgQT29MPV6E-KpSfZcT0Kxsw6l7hkO43epW5oSgh3V4QcP1ABUW837iDA1F9hT7oNJP1IpbTZk9e_YVUvF014nW8ZPMFkLiUHRgddNOjMc2yQjTQdudcunLJZgiuUEgNBLBgnZ2Z6veecSxR781B9UU9RbjZjUrC8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52eee8023.mp4?token=WBpfI1rghIvXH7wauTv46CAsPrfiIdcBSktVkhux3Aibac36_I4NfXBkDktiv051FzSra3VDQE3HK_yjkffdIadY8QCaE3eBOVxTzCrdmUUy4Vo-eC6cJ4nOOXDWH6MF23KfUR_iVDb8m2-XXYGMYGXnQuCb4lZUBslgqM9hKUxR9AZg6svPmgQT29MPV6E-KpSfZcT0Kxsw6l7hkO43epW5oSgh3V4QcP1ABUW837iDA1F9hT7oNJP1IpbTZk9e_YVUvF014nW8ZPMFkLiUHRgddNOjMc2yQjTQdudcunLJZgiuUEgNBLBgnZ2Z6veecSxR781B9UU9RbjZjUrC8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرگ ۲ کودک درپی سقوط هواپیما در آمریکا
🔹
رسانه‌های آمریکایی از سقوط یک هواپیمای کوچک در ایالت کالیفرنیا خبر می‌دهند که ۴ کشته و زخمی برجای گذاشته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460485" target="_blank">📅 18:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460484">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mt3yEFATSH3ummaPAIieHPajUyQZTtO_47qBib7oMFFIzIs6Ac5S3FO5zylqXITp5uLk7pASkaz7mCiqattjW19JZ9N9pA1o-RGMxS7hou2bl3bfLd5xWvK04JTh6oLHaQx4bhg6PN434oJLQfKiJx-LRUJQyA1EKabK5DAGPT1Wg1kt54AX_ZFwr7XZE1tEk_K0e2gvxOOCyb9PKu8ZBxCoTtvt15wO67lPR4S33MIfMSDYwId2-XtiYQTnrWVtX7iZVxVi_S6XEJw4FEdg13-hyHynhlryT4OQRBgCFCH-PSF6lkktAVNiwt9f-iQcO98mNCRzxH5tguYv-vYlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت عوامل رژۀ موتوری منتسب به سازمان منافقین در حوالی کرج
🔹
روز گذشته ویدئویی در فضای مجازی منتشر شد که در آن ظاهرا تعدادی از هواداران سازمان منافقین در خیابان‌هایی که گفته شده در حوالی شهر کرج قرار دارد، اقدام به حرکت با موتورسیکلت و خودرو کرده‌اند. …</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460484" target="_blank">📅 18:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460476">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvpAaN50vn_7WZzT-U81FF1UEdgyFl-0SHu_mInZS_NTPD9Q6bz6Fp4Ig9-4PqUQCIJjTinoZvX6Bh_R9WCZd8XljifKCmHIhhUsydAd60pMFRdXla0XmBRBj8tcHcc59tODN0BEWBVSiJA094cuCCRaWgniBCe3UrLsmzbmmbJ1Isv7nX9G8AFF66qczq7N5hW-5MRHOyyKB6rPyZW496xSDzJ-0BY55aogNteSecv-D2wcfPSJqsjMouhmhd_acdXGkzj5CZsVG1OovMu__9k1YTab4-uoxY5plwGLtlD03Awxi1tamyFNjmixnq2fX4T222_XdxfdnNbaKo3eXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T09-ohlBaVTgkXfXTumFIBb2J8327JfkWVfiWHEc6ym3lDhx0nylKOc2zQZKVYH5IIW8ro89pZPwfQuaGC8ZltgFkVu05OfPL32r1eRzFgKrwncpu1kRjfhDsFdzVS2oWHeSVnJGQVYtsU8srAYkJuo2wLrQPnak-5AV9asoqS7VX9b0xPFZn22fShlNoBFQyGg6VIDXgi-SjegYuMMGzBTpP0kYZAxudvWCtXwapbG00e7nJSl1Yc_9pkvzua1Pz57PSuPobzAf_o66wxm-u1NkWr8VxAVFuioZbQAcOIVwWVowv_h-yres7z4vZQUdxf4dYW3yxukI2GG9KJtA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJONInkoAAZyED75MBPeIzFoNA0DaEB2PkU7MsRqPLPOVXA02xMfOD4zRbPnRvDjS_o5LNT7XCl2Bu-kwNmKsNvKhk15hofLwzbi4I7MbfVkVmemL6WqmilQcDuFOi2iT6APxg_OVXLpGU9qmh_IB9KkKGerrofgTKnKrB-UVFwAxcv3iHgP6A9cQAi7BL0DQ0zWIg1jHIL7tZSvR0odgPwEGhyKxRXts8BWmfBrFW7PW4N6Lu6zq--02oOX9mhEH8XTj_7VVrIMceyKKGfPpisvomungY0C1US0_gJjNyBMRtzLTMJg48jhEBGSQaNcdh1UlJp0AEmQJGaznDmSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slbK0W6h9DOSASFgd_6GbLmFxrPnZzsrrfZR39O115ckk_TJfdKc5S62o3xIqVa2A7QJUjlQi06Q_XtgpnrTwtexOYhZ334TdtFv1Ai5wo6EIjeEiI1E_kOQYexMbmxV3YyOUjtwRj2Pn8PZskSrFZLkDEh7me7uyq5EpCNh9Ae4lvGO5uAAlejrvX0OB4dIBI0UGKvdhChpiv_bi1ZPONtAd6zXFptSHmU-7k-w4VmujgR-tkStW6nB-soc4WN6iM6Qj2k-6FI4cLdTx2cWvXROgJCeLqsLOJTgncnxXGOMpGea5Qz90wib6CoVyWo3Tkk5kID7agxOqePivx0RXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcimzKYgWGeR_CVaCqHOQi7ESJpgMIzbyUtUiUGlwVibCh59wflxT5Y5UZFt7kVgyR4lEgtdQrWi1sFTUi6g2WOIsBhYxgN2viesDVpVt54Ae1tkQw3Wj-EcV04KjZFVFpjrQxyeqXTexFt4lNY_S8vVayljIF8JcG0SaK4CvILYB4mneCIrK1axkp2cB9lvfeSy3rS0K2WXZEhrvQnjgO1rlrEyIPo5goUOjHV1nXm7rj-s4qkVXQ-vb7CRf7lwiPOnAYwbt01Ep5FCH_VJ8vUv2kb3zeQWEvHfP6K010M6wGJrPx7lFttAuO0PyMdJcANRSeDvF2mEdkPAZgidnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/schWRDfCZUozfs_-H3jp3xds0wnEMpvrgPvobvrqOT_OygWOhA5cLjJn0c7372IdplHQzFfS0nWIOP5C6m05rIxO6zUTQzpzZtFtw3jKGbQmuTA8phvVrkzNTtUg8Blj0q42JcQtIgJwxd2E4pqZvV7MJeRLuYCds81FJzA2qt4hyNWWPdrf13e7bzUmE0ie0tffIqu91Bue8pSF_JiEbw3c0pUsOgliEUaXJJgTo5XNlGg2SyEFVePrKUUKc9IJX0fDgcefizc6IuR3N9VZ-UieZuN2S5ITYD0wfRk1VLGT_a9Lz6_7JV57LWRfFMxCIXsvsvozQXRlcxnW8U1qMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3ZbiIon1qs06cYetkfbknd_wx0IxKBxkRisUjQsqIkMsXk66tac8_U6EzPf_RjGzIZEH0VUzka9jS9Hs0H1AOCdkupZjK33Dib0p9G4kKHT8T1Hy9OidkovDPLCCklkl-5HXRaG7Unkq469KNgm3xUeorRB2i4BxOHIXupKfgsCSocZPzfscj-vKU0BWoj63uP_8IrGg5gmwbNOnUfEQRKUiMccFe2Jtb5WZahZIEYaR1ZSVVbOUzRwojKepWtfiU1GGQiCv32_8iVGJ-TiBc3m34FxcJBqm-RQ9rP4W4DwFkCDqQFJcLt2UgWVeYTfkOXCU3i1zY-Xc8oiPuiFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7DUeXLXOs6-ajl01r2HzemavbnWrtPqSF0qT_ApoS8hX7Te57mOH9QVm7GyCcf8FrAVDebqQiYzYOOOZoaS6gzAos5ZvsCD2ZMOm4LIw09gui1CVsQS4eaLDQ1Orm4E43pRf8YEalYz6DYsrsit075nPL3RN7pJ8eqnZRteEImpts7Zv4NfI1U_li03wkduT4XrBYUSYyUNMefyYmU1YtC2bI3zdPB0rEpEJWHuPgSsKXoVKY-Bw0KdJgI32BzP_Lw4gz4CbGY9nebsx7aT8l1E4lji35qeKMB58GOWioB7GeOx_LihBPjhcQ_ZNtcCHRWLib6Mimr_8Dw8B4YPqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
مراسم وداع با خلبان شهید حسین مهدویان در قزوین
🔹
شهید «حسین مهدویان» در حملهٔ اخیر دشمن آمریکایی به خوزستان به شهادت رسیده بود.
🔸
مراسم تشییع و تدفین پیکر این شهید فردا ساعت ۱۰ صبح از امامزاده اسماعیل(ع) قزوین به سمت گلزار شهدای این شهر برگزار خواهد شد.…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/460476" target="_blank">📅 18:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460474">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzdHEMlThrDBnMtFoHDn66ApcLYBIaG_E0DJeanYVsS5wdpW885LI92gGFFR_E6h5-mLhr0rmWQOa32eEwmY3t10FBLHRY5uUdmVjUXYrpohEF5cR1bduvdRfGYxf4nWSvWR7rx2amOU7_CvyW_ST30R_2Rw_RfVsb3ye9FiT4-VBbKaBiUjxdvreOilKask-Y6yCV-zTQdLufRISitnXDo-XYiolmjC_RAlJW7VZRApwT7lIY9oMZbOsSoru2krTJuStMX5Uoz8oOT-BuI9azjoz0IhAz3FErd-IvrGEyo-SZXPhiR6coTz6zk-pYMj-LZ1ThjfknDXsh4HNlyPJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف محمولهٔ اقلام ضد‌امنیتی‌ در  شمال‌غرب کشور در مرز اشنویه
🔹
قرارگاه حمزهٔ سیدالشهدای نیروی زمینی سپاه: در اقدامات اطلاعاتی پاسداران گمنام امام زمان(عج) در سازمان اطلاعات سپاه استان آذربایجان غربی، محمولهٔ تجهیزات ضدامنیتی درمرز شهرستان اشنویه کشف و ضبط گردید.
🔹
این محموله شامل ۶ قبضه سلاح کلاشینکف، ۲۸ عدد خشاب  کلاشینکف، ۶ عدد سینه خشاب، ۴۵۶ عدد فشنگ خارجی، ۷۷ عدد فشنگ ثاقب، ۲۴۶ عدد فشنگ معمولی بوده که گروهک های تروریستی تجزیه طلب با هماهنگی سرویس های جاسوسی آمریکا و رژیم صهیونیستی قصد داشتند جهت اقدامات خرابکارانه به مناطق عمقی کشور منتقل نمایند.
🔹
به همهٔ عوامل خود فروخته و سردمداران آن‌ها هشدار می‌دهیم که با رصد مستمر اطلاعاتی گروهک‌های تروریستی، با هر اقدام امنیتی بشدت برخورد می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/460474" target="_blank">📅 17:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460473">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3800f6eeaf.mp4?token=atf9P5AObPBs8KKnoqp3fT9U2LZ1o1cdTECAELCh18Yp-O8evhcKiDezfwwLEQEZ-SVH0d3D5ulcx9Tkej7l_nOlHdRCIvTJkoZ7mjsUQ8HLcuEgNAtOt-MGciDO6xc10EBpCIoxpOOPPrUadbKaJpCfNDJlt8tqRkS69eVF0JgjJhkZDkzfECWvt-6jYkfXLCkHldgjqkVnYsgNGGZoG3VqjisjkQsemgjUoQ0NsmhnzSJ5noqCzFxQcBrWc5F91jvIMkSaY0i_X9jhX2P8hyZGW1O1QhM9VaRtTuHWRtG1MzDzheHFQjwK1OdHXDTSzx90hnRBtXAzmjxWWbCOMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3800f6eeaf.mp4?token=atf9P5AObPBs8KKnoqp3fT9U2LZ1o1cdTECAELCh18Yp-O8evhcKiDezfwwLEQEZ-SVH0d3D5ulcx9Tkej7l_nOlHdRCIvTJkoZ7mjsUQ8HLcuEgNAtOt-MGciDO6xc10EBpCIoxpOOPPrUadbKaJpCfNDJlt8tqRkS69eVF0JgjJhkZDkzfECWvt-6jYkfXLCkHldgjqkVnYsgNGGZoG3VqjisjkQsemgjUoQ0NsmhnzSJ5noqCzFxQcBrWc5F91jvIMkSaY0i_X9jhX2P8hyZGW1O1QhM9VaRtTuHWRtG1MzDzheHFQjwK1OdHXDTSzx90hnRBtXAzmjxWWbCOMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: ناو هواپیمابر و یک ناوشکن ارتش کودک‌کش متجاوز آمریکا مورد حمله قرار گرفت
🔹
روابط‌عمومی سپاه: نیروی هوافضای سپاه پاسداران انقلاب اسلامی با چند فروند موشک بالستیک، ناو هواپیمابر و یک ناوشکن ارتش کودک‌کش متجاوز آمریکا که برای کشتی‌های ایرانی مزاحمت ایجاد…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/460473" target="_blank">📅 17:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460472">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3882c73266.mp4?token=TwEIa8rB_8jPpP06F164IzZxs7Qz6JAK1yaKz7nv2j36Hhl9_YXtj5-BE0dkNf5KMQhC2ZZ8fTy_VqjEpN8ml9KVhbBqKyf8dootMiFPDUcXGDfXWYMYqViMphQdkNZipCzpi1Q_jWYijmNSx6xWWb1hRbxoi0RKXaTOPv_2a3HdWzyA_OXoe1nKPcXp0CRjHV-KvpHRaxJEqZnT7lqYaS8b9FspYc5N_3JYTMtfp4rSOhGbQumArG8XfRwclZE4oQ09xbaAxCBWXDsLR4qPp7J0Ks8NlNGdNjusmhbmqflNeFAq-Eo1VYgXj82Mxf8-n6vaDRj4fvxedCYPNh1PEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3882c73266.mp4?token=TwEIa8rB_8jPpP06F164IzZxs7Qz6JAK1yaKz7nv2j36Hhl9_YXtj5-BE0dkNf5KMQhC2ZZ8fTy_VqjEpN8ml9KVhbBqKyf8dootMiFPDUcXGDfXWYMYqViMphQdkNZipCzpi1Q_jWYijmNSx6xWWb1hRbxoi0RKXaTOPv_2a3HdWzyA_OXoe1nKPcXp0CRjHV-KvpHRaxJEqZnT7lqYaS8b9FspYc5N_3JYTMtfp4rSOhGbQumArG8XfRwclZE4oQ09xbaAxCBWXDsLR4qPp7J0Ks8NlNGdNjusmhbmqflNeFAq-Eo1VYgXj82Mxf8-n6vaDRj4fvxedCYPNh1PEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمدرضا گلزار: قدردان شجاعت، فداکاری و ازخودگذشتگی عزیزانی هستیم که در روزهای سخت جنگ برای دفاع از این مرز و بوم مردانه ایستادند
🔹
در این جنگ جای بعضی آدم‌ها برای همیشه بین ما خالی شد. رفتن دانش‌آموزان میناب غمی است که با هیچ کلمه‌ای نمی‌شود حق آن را ادا کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/460472" target="_blank">📅 17:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460471">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iE17wwbHdNLesF4i8lQfaeHRJt-0n796LYwxK3cThYL5-QSMGm_ULZCIqMcd0OTSa0fCo8_sa671iI9O0MAnrlRlZ1B4iLYkFEh4gW2DOXPiXhSRLlQeNKC-6zcOmBBcogyiJyPtV3jV6pQI454IcIkVmChPPQnXPAOd8Z9JUrSUQe3gs3KyJ9dBR_hCYc8V0e46D1fsknV8g2irJWYKoVt0_3xxyBFXZdxNemtH84IDFerp_j-2YqfVpWY980P8Ky_Bm4b1Z5FmXgyDFZdOEhs13YNKG5dkO2gqpzdc8B39IKzO1ALDr2mZm1b4ntao_BKLZAWalJankHN8d1wnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بودجه از درآمد نفتی لبریز شد
🔹
طبق اسناد رویت‌شده توسط خبرنگار فارس، ۹۱ همت درآمد نفتی در ۴ ماههٔ امسال به بودجه تزریق شده که این رقم ۲ همت از مقدار پیش‌بینی شده بیشتر بود.
🔸
دولت در پایان سال گذشته برای ۴ ماههٔ امسال ۸۹ همت برای درآمد نفتی درنظر گرفته بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/460471" target="_blank">📅 16:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460470">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bff51e3ec.mp4?token=I70a28LhXhx39v8NxmnnceGZ78LJjYPfRiAI7mgPvirwkZVPlCFauEzwvMzUDvYOO9yz8kBtdcVIFRi1XrjCxtK1V_-WwOfyi-uelWgn6eaWYZsZ05Om4_PaVIltv4RV7v1O-0OL9LDhDL1s2yKU0buhav2XiiZ842aTEm2qFbMXCDtCQsQybp7zSuugTbCKTqiu9YQ7Tn8VJVrfSRWTIZP62-u9ag3tG3nygTaHdhPOQcTwjr7mnkUUMFhRrl-OEaPCm3DilO7NjVOnXAwDwiMtpsMpVvNK5B65oDc5p6K-l9bELJkjXUbMFiHLA5MczHL8PxUshmdMoucPu7K7Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bff51e3ec.mp4?token=I70a28LhXhx39v8NxmnnceGZ78LJjYPfRiAI7mgPvirwkZVPlCFauEzwvMzUDvYOO9yz8kBtdcVIFRi1XrjCxtK1V_-WwOfyi-uelWgn6eaWYZsZ05Om4_PaVIltv4RV7v1O-0OL9LDhDL1s2yKU0buhav2XiiZ842aTEm2qFbMXCDtCQsQybp7zSuugTbCKTqiu9YQ7Tn8VJVrfSRWTIZP62-u9ag3tG3nygTaHdhPOQcTwjr7mnkUUMFhRrl-OEaPCm3DilO7NjVOnXAwDwiMtpsMpVvNK5B65oDc5p6K-l9bELJkjXUbMFiHLA5MczHL8PxUshmdMoucPu7K7Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
انصارالله یمن: جلسۀ تعدادی از فرماندهان نیروهای وابسته به سعودی را با موشک بالستیک نقطه‌زن هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/460470" target="_blank">📅 16:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460469">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
انصارالله یمن: جلسۀ تعدادی از فرماندهان نیروهای وابسته به سعودی را با موشک بالستیک نقطه‌زن هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/460469" target="_blank">📅 16:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460468">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a99eb7647.mp4?token=vKltj5Au5v8Qo93TmjfAXkY-EM8nv1EmULTFI6FvDrTq6R2U69zqPoeX3P5VoCkGrVt6kTzmzjVvWtH5jIjW312ugr8gg-cQev1_ZdcALvgn4RUveACuw-jOUhnQTPpgp0ygHEL5FGzU9fhp0a7odldIUgfettk4E4dmtZt2P2UrcdHWVQMpc2cOae742ZIGrL1hvv32SnnWJaLDPHD5C_7ff4ByWG947QZhzMvWU9_FkcbHAIBSYnqxF4zRRrBOisYxVzMpLujxJFA3IvMiUFFeZAMLqjZ4OR10pnPIS3ZBhSCDEqeQ0xuJOcTjKKHGl9p47yq0_xEWPj0BJLAwlTkGtoTyoWXeldk8Wm5Ma8qb4t0kSd1v1WFqbdEfOx7VX1yIGLUlsyZt2gzghhj6f4oP_X6ibSqgiVuL2HRvuJsSYG6n4Rppfe5oo_915XkjjZSh4KWbHX-vcDnBhUOC72Kajvta1k3Rr8yG81lCAGacJL-93JoQOQPIacbcKrTpYhq9pJ9cL7TY9JvErhK_quUNnNMrbzvBzcGFjId7r2BNH-UCE2EsD8Mjhs__G4-T1-3Fnyqhc-QexWvFt3QRFHLHx5DawtTq_e2R41ch3cMINatEfLlYW_qHyB_dSNCNlecpsjsxZORQ42uhWLyF7jkYAKjWMctjB8mj6qT34a0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a99eb7647.mp4?token=vKltj5Au5v8Qo93TmjfAXkY-EM8nv1EmULTFI6FvDrTq6R2U69zqPoeX3P5VoCkGrVt6kTzmzjVvWtH5jIjW312ugr8gg-cQev1_ZdcALvgn4RUveACuw-jOUhnQTPpgp0ygHEL5FGzU9fhp0a7odldIUgfettk4E4dmtZt2P2UrcdHWVQMpc2cOae742ZIGrL1hvv32SnnWJaLDPHD5C_7ff4ByWG947QZhzMvWU9_FkcbHAIBSYnqxF4zRRrBOisYxVzMpLujxJFA3IvMiUFFeZAMLqjZ4OR10pnPIS3ZBhSCDEqeQ0xuJOcTjKKHGl9p47yq0_xEWPj0BJLAwlTkGtoTyoWXeldk8Wm5Ma8qb4t0kSd1v1WFqbdEfOx7VX1yIGLUlsyZt2gzghhj6f4oP_X6ibSqgiVuL2HRvuJsSYG6n4Rppfe5oo_915XkjjZSh4KWbHX-vcDnBhUOC72Kajvta1k3Rr8yG81lCAGacJL-93JoQOQPIacbcKrTpYhq9pJ9cL7TY9JvErhK_quUNnNMrbzvBzcGFjId7r2BNH-UCE2EsD8Mjhs__G4-T1-3Fnyqhc-QexWvFt3QRFHLHx5DawtTq_e2R41ch3cMINatEfLlYW_qHyB_dSNCNlecpsjsxZORQ42uhWLyF7jkYAKjWMctjB8mj6qT34a0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستم داغون شده، چون محکم زدم توی سر شوهرم!
آشفتگی روانی و درگیری شدید در بین ضدانقلاب به روایت خودشان:
فاتحه ما خونده است، دیگه به شاهزاده اعتماد نداریم، سلطنت‌طلب‌ها دارن ریزش میکنند، زندگی ما داره تباه میشه، این درگیری‌ها به‌خاطر نبود سیاست و مدیریت در رضا پهلویه
@Fars_plus</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/460468" target="_blank">📅 16:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460467">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phLBmOmYiDt0cQ6oYYA_XEp7zv3NotdgnVyAVUpahLqgl5apAnOFiUrbUHIlQk_T_rLMA_z0EXV8JfoasOeYXkXHT8KRMr-pGILtChciAI-2__6ygsarLZ3jjbrVL7VKKspgmI1B9giX3A1B-nnp8IoQ_AXink2ijRm2eLMwD1FXWm8P3IX_Pk47Dyd9XxyaVK3CAe8fe4xeqwnHz6xctISYJZTjdj8d6A3eKj0XPKqdmrXMQ7w6RVcIPnsKr0TVbsm1LwtH2yBpaBNoLmha8S4PuRkdHZXowGmsXi7oDExYxEZMRpRhKmyZdAENXwQvKEQCa-gw1BZQ2AlRzhhFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری تیم مسلح ضدانقلاب در استان فارس
🔹
طی اقدامات سازمان اطلاعات سپاه استان فارس یک شبکۀ هشت نفره از عناصر وابسته به گروهک‌های ضدانقلاب شناسایی و دستگیر شدند.
🔹
این عناصر با هدایت جریان تروریستی سلطنت‌طلبی و بصورت محله‌محور، اقدام به تهیه سلاح و برنامه‌ریزی برای کشته‌سازی در اعتراضات احتمالی نمودند.
🔹
این افراد در اغتشاشات دی ماه ۱۴۰۴ نیز با حضور فعال، اقداماتی نظیر حمله به اماکن به‌وسیلۀ کوکتل‌مولوتوف، آتش زدن لاستیک، انسداد معابر و تخریب اموال عمومی را در دستور کار خود داشتند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460467" target="_blank">📅 16:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460466">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phm8z5ZNvGFqR0eNfW2aaweebBAuO5jgGFQG0RVyPQdrBTVSr1-G-11_75Sce0Cqc3y6kchRPIzOwJI1TupExQXRDkijtwcAdka84wt7Zutpq18NSobFD4Pk92h6xXJo_rQjKdv54-KCwsWhbj1f356AP6la8Mbkty6osYcUz5uh8tK1hxxrXwGb6edHdTnPKKewrwgbnDq5MBkCmDyn5axdWs5MFoRPBg-wOvLQHRt1-XlxgzieEDgLpaRCyREfZDvGAWxGE0KyQf2EsNIeuNcywzhawzd8TN6ESP7JGkUNdRE9bE9ZuffCSIlEu0Iw1zTlU1L4xBeMxwqEhAAalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی پرسپولیس: بازیکنان می‌دانند غفلت کنند، نفر جایگزین آماده است
⚽️
بازی با ذوب آهن برای ما مهم‌تر از دربی است. از فیروز کریمی خیلی چیزها یاد گرفته‌ام ولی چون استقلالی است الان نمی‌توانم مشورتی از او بگیرم.
⚽️
چون امتیاز هفتۀ قبل را کامل نگرفته‌ایم محکوم هستیم بازی فردا را ببریم.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460466" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460465">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCTFcYQSvIQv5Uu71znSHfUB5GHbvt2JNuuaS8ZIejZpluN7YaN2YJcr1DAsj_5PH154Mce2s2nyPjiKFlsVO5dbMbmTyjVQrH1_T7aQyJ75sfQDrsNYqfTRwRozFf6CY5MlcA5cg6Z-1-5HZzqu4L4uhqwNA4Vq9OdiROjbwxZYp7SEKvtF6d7HQk4Es7vVsmx2EVRgiIexHsI53jFS7CnwzF0xdz-Ke8sVH7NFv4bLJEYIKiG8f9TSX6xKhY2OhMH-B2ARXdQx5sLx0UPBlivnpv4LFI63h0gbxKNB6X_kB5xqjF9rE60-y8natQDvrlqdFTSExHdxA6lVwB43oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا ایران، آمریکا را تحریم اولیه و ثانویه می‌کند
🔹
ایران با قراردادن ۵۶ نفتکش متخلف در فهرست ممنوعه و هشدار تحریم همکاران آن‌ها، تسلط خود بر تنگهٔ هرمز را تثبیت کرد.
🔸
این اقدام با رکوردشکنی قیمت گازوئیل در آمریکا، سقوط ۹۰ درصدی صادرات گاز قطر، کاهش صادرات…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460465" target="_blank">📅 15:53 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
