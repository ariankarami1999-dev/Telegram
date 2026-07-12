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
<img src="https://cdn4.telesco.pe/file/R40UbZuKXA7oHquC-G2mIX8M-XVY2G5K45mKiYWzmyM7Y8IC8aF2lKcOZKgPfQOhstpgzVBR84thxhnEadibitDgChbtUtpP0y7kzdVPWLkNL4pbosr9P5SN00hk0GFDiztVgAXU9SFR3MIM4wb8CwxTMKTnSbvWD4YfpxVIf5NU52RKCNZAYm46QpU9uTRmQn9AL6naKhUbevfmlH6QOUphOr-ChHMXJIPZPsOt5mL8yja3Isj8jFPcjw5FaIOPJrXqjqKeUX2qVogNzpFGSinYqLAe52_VYS7NoXiGTMcPsX_lP4g4se35PFVZL01yXA7KHth-kSkokaNx0LMZtA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 179K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 20:18:59</div>
<hr>

<div class="tg-post" id="msg-67924">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: امشب به طرز ویران کننده ای به ایران ضربه می‌زنیم
👎
خبر بالا فیکه و ترامپ با هیچ رسانه‌ای چنین حرفی رو نزده
@News_Hut</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/news_hut/67924" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67923">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
❌
وزارت دفاع کویت:
۳ پایگاه مرزی زمینی کویت هدف حمله قرار گرفت.
‌همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت هدف حملهٔ یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/news_hut/67923" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67922">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra87xl8jfzrkjyWJgdJiUe9DuyCGw3MzyYR9BxenGQuy1tD6fkvQwgTff4ffAljeCTecyvVL6rM58ynjoXSelTol6d70GJ0dlf5W9T41-ieh59XRVbA43OsKGB2IR7j6NdmTIfNutoV0Jm2RPxlpLRmnXPYkClMXAde40_9xHJ8NtGV3SjS-icjaEEZE26E3chIdWa4QlqBcUpmWSsQSQn-pEIYF6lj44KaVFS0NxAOI3bPWjbijcm0K_3CJQs6lNPr3As7furNBTWM25ONWOVv4fR1hGgtVzKVHwI87hKZ_czlfPeY3WwSCqwH0KMZMssfg9iqlxqOo-FcrkLDlZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
ارتش ایالات متحده چند حمله را علیه سامانه‌های موشکی و پدافند هوایی، و همچنین قایق‌های کوچک متعلق به سپاه پاسداران انقلاب اسلامی در چند نقطه در نزدیکی تنگه هرمز انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/news_hut/67922" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67921">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
فارس:
خبرهایی درباره کشته شدن 3 نظامی آمریکا در حملات موشکی به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/news_hut/67921" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67920">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
منابع خبری آمریکایی:
یک حادثه امنیتی بسیار جدی در یک پایگاه نظامی آمریکایی در کویت، پس از حمله ایران، رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/67920" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67919">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
منابع امنیتی به نیویورک تایمز:
ارتش ایالات متحده، مجروحان جدی را در پی حملات اخیر ایران، به بیمارستان پایگاه رامشتاین در اروپا منتقل کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/67919" target="_blank">📅 20:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67918">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8f7jEDwMbBc5Uc5CqnUEf2dLKS4neZAIynrdbP8qqrPDXqovQdre8xPiJPGkxCmcROyEwQ4UtVqypiTmCzf6brBUoy2dHFzYwaxshpuIc8SfFTJO_4TyJSLtFv3rzKIjYeuRVWORabOKk1ybxqBb5agFLBHDKGO5P9V0aXhKv5YwGsDvzUPUHt7Gyyy5tPDA4JwUewLH8VxYg2qDqbeh-K0_K1RF9KiUtX1oUucc7OIvx2ZLmNLrb1uKm7KG7f2qehyddaiG9KP73Ik9lGXJWTkhkrpKDepMESPCtOA1FDDRx5nPNwWvy50vGh-oj05Qdh4Y2-Qz5Du0AH-AftdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قشم همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/news_hut/67918" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67916">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=lc4lP5NPArmAvn_2SddJloAvFIsx0tAf3GbXwoYcQbJjch0wMuyvOkYSuyBN0IkBvLAoRR3CRahHmsyp4FKLiWBBXSmsFtjfVz7ML81dnpI2GBFTbPCQFO3kN2_2yDYOkQyhKSjTozt5H54seu2mGXE_iwGqO5i72VfNyX7C0uKs_H87qxeskAwkxoevbRzo85Z6bJUoWOLN9vu-IXt4a5jSS7ukJ3yN_t51Bxcwyx09SKeYfkba4pmoxEM-KFRg3S0w-wx7EPvtzhMxhFr7iTtoOfu0eu7hnKhFQecNnYwdoX2dZ6IvKb8_n2l_KU0omOgv4BCzEWFg808RKdYPbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=lc4lP5NPArmAvn_2SddJloAvFIsx0tAf3GbXwoYcQbJjch0wMuyvOkYSuyBN0IkBvLAoRR3CRahHmsyp4FKLiWBBXSmsFtjfVz7ML81dnpI2GBFTbPCQFO3kN2_2yDYOkQyhKSjTozt5H54seu2mGXE_iwGqO5i72VfNyX7C0uKs_H87qxeskAwkxoevbRzo85Z6bJUoWOLN9vu-IXt4a5jSS7ukJ3yN_t51Bxcwyx09SKeYfkba4pmoxEM-KFRg3S0w-wx7EPvtzhMxhFr7iTtoOfu0eu7hnKhFQecNnYwdoX2dZ6IvKb8_n2l_KU0omOgv4BCzEWFg808RKdYPbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به قشم
@News_Hut</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/news_hut/67916" target="_blank">📅 19:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67915">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🇮🇷
نایا:
نیروی قدس سپاه پاسداران انقلاب اسلامی، کشتی‌ها و شناورهای آمریکایی را که در منطقه "کیلومتر ۲۰" در تنگه هرمز فعالیت دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/67915" target="_blank">📅 19:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67914">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/67914" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67913">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONzwFF1ViSZZ_22tcxLd_Hy_dmmXFP1AnU54XX4L2HLAgMFZgR9v77V4BOByttyfDVOlPHfVKU_iA5yIQ__v7jQ0iMIzf4q5fSFmg3vVh5b8GxTsCkv7ThqjFsMp7qus4RtHO3zjC1mylbmSwOFovbxMuQzQONn-_FljAFYMKbRZA0Kv8je_UfeWVTOTaFY3AcrqiBLGXI93mifQBWnUDv6YjWPJHuvoqE_YySugZCzqM_R5reUwkMP0IAdqVtBcuZ71tBaRWmimKnLJ_Kb7En8Jr5f8prYORBQeJvi2kf_OLJm8lNe_j3dTPqLRRYr2ycemh1arP9iLBBGeUjYc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تروری که روزنامه همشهری منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67913" target="_blank">📅 19:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67912">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=OQyuMFPJHKXnbblgWUgYP4ezo5epKY08eoLvmlzuPAEZdEWCQsP_yQwdem4ccrRAgr72AX5lGJVZ5P6qpQBOwsNQg9pN_nKO2LusZalQkv5TXAMKAnQt3xxg4DSd1Dc_OiDsG_2etXGfMauu-vnvwUzBOf9Sfo8tLojNKOmFAO0X9oFb0R_3UQQa_PWrzq6PCQQ6LUf3t-ZydiDSuVFrGW8c8SlGVjygC1FAM13mcIiuWD5jfcoJlZTEZ_JQeBcwr8zI-ig3g-faRAGISULFlEdoRTP-dz2XHqR2cSikGYZnPLUlWth1LkaGsVuDVcEyDHjSfMmyXXV_EdxwYBcd9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=OQyuMFPJHKXnbblgWUgYP4ezo5epKY08eoLvmlzuPAEZdEWCQsP_yQwdem4ccrRAgr72AX5lGJVZ5P6qpQBOwsNQg9pN_nKO2LusZalQkv5TXAMKAnQt3xxg4DSd1Dc_OiDsG_2etXGfMauu-vnvwUzBOf9Sfo8tLojNKOmFAO0X9oFb0R_3UQQa_PWrzq6PCQQ6LUf3t-ZydiDSuVFrGW8c8SlGVjygC1FAM13mcIiuWD5jfcoJlZTEZ_JQeBcwr8zI-ig3g-faRAGISULFlEdoRTP-dz2XHqR2cSikGYZnPLUlWth1LkaGsVuDVcEyDHjSfMmyXXV_EdxwYBcd9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
دقایقی قبل از فوت سناتور لیندسی گراهام با او صحبت کردم و "او به جز خستگی حال خوبی داشت"
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67912" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67911">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
حمله موشکی ایران به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت.
گفته می‌شود این یگان در حمله دیشب به جنوب ایران حضور گسترده داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67911" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67910">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=MeXz-Fm3CgYdUtEXS650SDsZZg68F857XRiKZoO5iF4k-mMDKmMexXfU3XEte1jS61LNRK2BOkAacizpdboB40yKJ2e0XD2BJyuw73VoHxNkSkyhdEciDtOntHglZRq8bzzGUFuLhftc75Aqub5iqXq_Cji1W07npL4ygEdxZiDLDQqEplijhTS4UHR6yjkEoeQmKOjVfTawUgfdbQmJtycNC7G8NDZ6WVaFO6pDheNZllsT1xtGy5TUXMZc2-2oDR-8G_9iRvA3N3oCTMsR1_V-OXyHBt0nC3YZZhJvdd06tpA9VADCCUyMtWMg2HOtA8HYt7qHkVZm9TJqTZfL4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=MeXz-Fm3CgYdUtEXS650SDsZZg68F857XRiKZoO5iF4k-mMDKmMexXfU3XEte1jS61LNRK2BOkAacizpdboB40yKJ2e0XD2BJyuw73VoHxNkSkyhdEciDtOntHglZRq8bzzGUFuLhftc75Aqub5iqXq_Cji1W07npL4ygEdxZiDLDQqEplijhTS4UHR6yjkEoeQmKOjVfTawUgfdbQmJtycNC7G8NDZ6WVaFO6pDheNZllsT1xtGy5TUXMZc2-2oDR-8G_9iRvA3N3oCTMsR1_V-OXyHBt0nC3YZZhJvdd06tpA9VADCCUyMtWMg2HOtA8HYt7qHkVZm9TJqTZfL4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کویت کمی قبل
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67910" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67909">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAHQHJve8eiPrwKc7YI1gtctGefso7dw2saA1BWC-JZqIy1a23SBFC7ZIxjWGRqwDN0YAAmNzq41jsnv0vBctwH2fa40_fWmefiQur3u8PiBUQ70XTa1XnGLKpSdxREeUOTSgl1akJ4YqLAGnD_TZ8kC_SqT_r19kqFW4KFmlKgzc5O-DBYc9F2Z4PQ5fUC4hj-YvrGWChHbtSpGs04f37emRecSVEXwYdMR8VV0c4cplOqCn7qGYumJi07fPFVCEAKke4SPLze8wKx_uaF921iKkAp0mc4kTE3Whnno2-ObT3bxZCjEPuH1SypCAplk_4J7KspSjvK4PGfFiPEl5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دو انفجار در کویت و برخواستن ستون دود
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67909" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67908">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=ge2YwuTE_XX4zb7Pf91ot3nKHyMY_mbJJeOCBm1rYjvh-Vi7M_MXs3VnYGQ4pgkhPfv6lT3bsIun91CscyWrBB4vzxWAEJQpm1kJnKrHlFMZyed7BjqGaYu_TTlFhhYxlNyZdaE5Ii5eZzfRaeuhMa5IWFCuSLDrzvLPx73wQl4hKeBR2WB7T6iqoxxxaI15GCPHfaQ4J8SNJSbKXtSq_6gs0-usOfACfwhXCJrr0BVoLJRIKNeIDb0e4LGthF7WgA6paO4E-13SeMJm06-YXyJMNzE1aPwAT8550b94yU2We6VAbMKR983QaeEpbnYpfdnw4O-OaOODlSAdDud97w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=ge2YwuTE_XX4zb7Pf91ot3nKHyMY_mbJJeOCBm1rYjvh-Vi7M_MXs3VnYGQ4pgkhPfv6lT3bsIun91CscyWrBB4vzxWAEJQpm1kJnKrHlFMZyed7BjqGaYu_TTlFhhYxlNyZdaE5Ii5eZzfRaeuhMa5IWFCuSLDrzvLPx73wQl4hKeBR2WB7T6iqoxxxaI15GCPHfaQ4J8SNJSbKXtSq_6gs0-usOfACfwhXCJrr0BVoLJRIKNeIDb0e4LGthF7WgA6paO4E-13SeMJm06-YXyJMNzE1aPwAT8550b94yU2We6VAbMKR983QaeEpbnYpfdnw4O-OaOODlSAdDud97w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پرزیدنت ترامپ:
ما آخرین جلسه را با آنها داشتیم، آنها دیروز با یک توافق موافقت کردند، یک توافق عالی برای ما. نه هسته ای، نه این، نه آن، نه هیچ چیز. آنها همه چیز را رها کردند.
و بعد از آن اتاق را ترک کردند. و سپس در عرض یک ساعت یک پهپاد و یک کشتی را به آب انداختند.
گفتم شما افراد مریض هستید. شما افرادی مریض هستید
.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67908" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67907">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILJVbCDkgMHwJEhkqCwY2ibWVknrNI3ynRSAwwbI3JUX9L6afyWcMGydNVGdt9IrtWJ7Ze6L_p430oynbsxrtGWpDsNcvdtDq-ry1BJjrQ5kro79mhTJF5Wl4PtZQsJvDs-DW8-NgJPSILp2iE-iRJEuRUvP55V9IB7eF3G0uHiLc29scM2QbhqzqKjvNX-m4BaKFIM_KRwN50xuRJW6530VWlTETs-7Xi_0UT68cCenR5KAfENWeVn8j29FHmVsyjDFTi60Q1p0kZSlvfcOKUJ2_IJYDhkTuuEmfpEqEXpZs69HEfPGVFUlRMHaDDeYXxFQ0pFps4qQ3oie6JksLWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILJVbCDkgMHwJEhkqCwY2ibWVknrNI3ynRSAwwbI3JUX9L6afyWcMGydNVGdt9IrtWJ7Ze6L_p430oynbsxrtGWpDsNcvdtDq-ry1BJjrQ5kro79mhTJF5Wl4PtZQsJvDs-DW8-NgJPSILp2iE-iRJEuRUvP55V9IB7eF3G0uHiLc29scM2QbhqzqKjvNX-m4BaKFIM_KRwN50xuRJW6530VWlTETs-7Xi_0UT68cCenR5KAfENWeVn8j29FHmVsyjDFTi60Q1p0kZSlvfcOKUJ2_IJYDhkTuuEmfpEqEXpZs69HEfPGVFUlRMHaDDeYXxFQ0pFps4qQ3oie6JksLWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
و شما بدیهی است که یک شبه دور جدیدی از حملات را آغاز کردید. ایران یک شبه گفت تنگه هرمز بسته است.
سنتکام امروز صبح بیرون آمد و گفت تنگه هرمز باز است. کدام است، آقای رئیس جمهور، و چگونه می خواهید پاسخ دهید؟»
🔴
ترامپ:
"این باز است، و من نمی خواهم در مورد آن صحبت کنم زیرا می خواهم زندگی لیندسی گراهام را گرامی بدارم، بنابراین نمی خواهم در مورد آن صحبت کنم. قبل از تماس به شما گفتم.
آره بازه ما دیشب آنها را بمباران کردیم. آنها افراد بسیار بسیار شرور و بیمار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67907" target="_blank">📅 18:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67906">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
یک فایل پنج‌ساعته از مکالمات بی‌سیم نیروهای سرکوب‌گر در اصفهان به ایران اینترنشنال رسیده که نشان می‌دهد نیروی انتظامی با مجوز استفاده از سلاح جنگی، در ۱۸ و ۱۹ دی‌ماه با کلاشنیکف و وینچستر به معترضان شلیک کردند.
دقایقی از مکالمات نیروهای انتظامی در بی‌سیم را در این ویدیو بشنوید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67906" target="_blank">📅 18:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67905">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=osHH0o5DQ9Vb3pazSjjxaB9oOKa2Peilp1Y7yO39h9ipmLcai_0_yY8UN5h4XoDx0X10eyeq2omw9LXI5oT2jyah-bZGCp8csp4GGeL7VGETO77vgOwNR1LXeMfR0CuQsAWENwpySrhm8uwCNCQDJnpRsH6UzBZxmQLE8KH9OmmD2LDwyjFPmANjOWYUqFF_QjvyfE95pDGIt65r7QkjOukTQWAIEpN0uNOokK3arjhG9GW2PxD1x779BAS7EUBCip_ZzNpCyDC3qADcSj0IdcGq8vpknSldiEne8TepkKn58Nz9KOMPcqvnEANYNz1cPQp_-Ps8cXww1bfVMlN0LSSpLGQg_SOmOlu5rpMU0JXri8zdSXKNVQvcK2NtuvMCEbSsqPLQcyvkzGy4Uyj96tknmQNq324ACbwwTi0FoIWir3XcYWmdQ3ysCs5z_WM6bM26Z148NfPhi6h4vSq7xe2OcCbdTYfgn8Oesd_PlCiFFz0BzlvYm-4-QKQQgp8gqBFB8jDUOd97kfd5ah9RMdI2a6-HAAZq9gGGcyg1ANXqHJkTMbo0Ctl9FGH2PMRr7CW7rA79YHbiteCv0dfonBeCl1KBz1A6Zkab4O1JRvGx9wFFqPKB7x7rAsNrJPcaCcDo1W6X_CAK8ndcA2j9MHjbLOg80D4MpYQzMiaOqyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=osHH0o5DQ9Vb3pazSjjxaB9oOKa2Peilp1Y7yO39h9ipmLcai_0_yY8UN5h4XoDx0X10eyeq2omw9LXI5oT2jyah-bZGCp8csp4GGeL7VGETO77vgOwNR1LXeMfR0CuQsAWENwpySrhm8uwCNCQDJnpRsH6UzBZxmQLE8KH9OmmD2LDwyjFPmANjOWYUqFF_QjvyfE95pDGIt65r7QkjOukTQWAIEpN0uNOokK3arjhG9GW2PxD1x779BAS7EUBCip_ZzNpCyDC3qADcSj0IdcGq8vpknSldiEne8TepkKn58Nz9KOMPcqvnEANYNz1cPQp_-Ps8cXww1bfVMlN0LSSpLGQg_SOmOlu5rpMU0JXri8zdSXKNVQvcK2NtuvMCEbSsqPLQcyvkzGy4Uyj96tknmQNq324ACbwwTi0FoIWir3XcYWmdQ3ysCs5z_WM6bM26Z148NfPhi6h4vSq7xe2OcCbdTYfgn8Oesd_PlCiFFz0BzlvYm-4-QKQQgp8gqBFB8jDUOd97kfd5ah9RMdI2a6-HAAZq9gGGcyg1ANXqHJkTMbo0Ctl9FGH2PMRr7CW7rA79YHbiteCv0dfonBeCl1KBz1A6Zkab4O1JRvGx9wFFqPKB7x7rAsNrJPcaCcDo1W6X_CAK8ndcA2j9MHjbLOg80D4MpYQzMiaOqyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از  فعالیت موشک‌های رهگیر پاتریوت بر علیه موشک‌های ایرانی در پایگاه موفق السلطی اردن از دید سرباز آمریکایی طی درگیری‌های روز‌های اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67905" target="_blank">📅 17:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67904">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=TuxnvlKbLE_WVYhEKZXoqvufc9mgd3O8m2nx_tvnAnaV_HOI5Ej3xrdB699NPTyi3erwx1GjFJfkD2G5IGP4JtWgVhSGK36F5XPxtNfHKXOlsd9pMWA0K55yuntzqXi3HgmFuF_Anix5TF6yVIo4nARnK-DPVTNm21-QZr3Avyfdwd5es9vrHGRfTuu3HschQLFT0zkJHwwEXXvua5ZbQ_mxA-eedtwpBlOK_AwnHZrRZljj1_z4CgUcArADCileKruBB7Ib3NxKjcBSQzok0ODH83SmkRl350NscAwidza7QhlcasG4dyB_WV7sxiUwwlDxJwG1OJm1m4lRwDhqJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=TuxnvlKbLE_WVYhEKZXoqvufc9mgd3O8m2nx_tvnAnaV_HOI5Ej3xrdB699NPTyi3erwx1GjFJfkD2G5IGP4JtWgVhSGK36F5XPxtNfHKXOlsd9pMWA0K55yuntzqXi3HgmFuF_Anix5TF6yVIo4nARnK-DPVTNm21-QZr3Avyfdwd5es9vrHGRfTuu3HschQLFT0zkJHwwEXXvua5ZbQ_mxA-eedtwpBlOK_AwnHZrRZljj1_z4CgUcArADCileKruBB7Ib3NxKjcBSQzok0ODH83SmkRl350NscAwidza7QhlcasG4dyB_WV7sxiUwwlDxJwG1OJm1m4lRwDhqJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب شدن سرباز بر اثر انفجار اشتباهی در تمرین پدافند هوایی روسیه(نزدیک بود همرزمش رو هم بگا بده)
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67904" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67903">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdilalHrhKLhH7bidO7-k_5VSdW3re6k2CijH1dCl60pTqvMDPcfslW1wB7f5nkPDvkuaLLIf24JYRxRxo4rylUr3JPhw7YZPF5G8_55VKrDl_EX0tiVivun5cyokNcmufLVDvGFK2xvpHG6U86KZYksNENzXG9vAiT_CjEGW4o5_Nalrfx0uLa2LClFc7656qc5RPK3crpFW6XK_NY3e7K6FjEu5ScbnHlXo52tU8tZxlyN4eSaKPTGStdauU242cj3mIl0RvPuPN92izihEO8rOcHHC2zsNs6Mqh3hZVUfC_IfT4C6fElf3kNQXg1BSFFn4Zq_PXBIw8f8xJiZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمامی کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای آمریکایی در این منطقه مستقر هستند و آماده‌اند تا از آزادی تردد دریایی اطمینان حاصل کنند، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران. ایران کنترل این تنگه را بر عهده ندارد. ترددها به روال عادی خود ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67903" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67901">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyeUt8Lzx7vLhRvpyLWmIqz9VkvEJDFZvX-84Rn2415lpSwoOANAxxlgUa3QzaMIlL47pS4bJPbRmuxZDpVozLCemRRltpoD5ZcH0p8tsFUapey_FzTEhitkMw7jf6McRLjkEp-dxSln5UhDbQ3k5AQWZiFDodsqo7Rlf8rDLYgZ7nxgtUAPV24n1HRdrP4lmThGMn98CMfMY3z964USVbjXy8pbhE-yJ6l0p71OxWhhNNtzWAqMUX4fRZU5aPVv-aGmh-NzBR9hLiUjrCoFFtfsVGHWJL9QbdIQGll6GgC5tQB6clpZZKAVovQbfZINpSnRZW52drrGN5cMaMGDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=bbWN_PnA3EgZCCOddGwDOObZLgqk-x9uuhdexS2LGuazOOMdt7S0bM3Hob_eNj6j7TYpV3xAfSaQICfXN4iaCljzavv7jTNHEYYYSLuPU4M076q4pl11nKZ4KT_dr8Kok4yvM1QElAY38DeYW_Uusqi8dBMeAu3hAzIzclDRthog6XfFj7aYkSBGW4qZY2tjKW9iJ1DOjxKLiH09JPG7pwu6S8copQSeyVe9gUZzQWsNazxGo_JdWgg-EuJlKPPfMAysWB-AFhHynCs-4tZ6iVyW77P2-oB-Fw09XYY9MMB67TSSpS-TL4ayGriIilcB2dkJBj5RmxvK6x3NnrtrYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=bbWN_PnA3EgZCCOddGwDOObZLgqk-x9uuhdexS2LGuazOOMdt7S0bM3Hob_eNj6j7TYpV3xAfSaQICfXN4iaCljzavv7jTNHEYYYSLuPU4M076q4pl11nKZ4KT_dr8Kok4yvM1QElAY38DeYW_Uusqi8dBMeAu3hAzIzclDRthog6XfFj7aYkSBGW4qZY2tjKW9iJ1DOjxKLiH09JPG7pwu6S8copQSeyVe9gUZzQWsNazxGo_JdWgg-EuJlKPPfMAysWB-AFhHynCs-4tZ6iVyW77P2-oB-Fw09XYY9MMB67TSSpS-TL4ayGriIilcB2dkJBj5RmxvK6x3NnrtrYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از اینکه صداسیما رسما مرگ لیندزی گراهام رو تبریک گفت
فیلم تبریکش بشدت در رسانه های جهانی وایرال شده و گویا برخی دنبال ربط دادن مرگش به جمهوری اسلامی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67901" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67900">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFdw40W9grpatxFeJ7v_7Wm4wGAld8aIG6kV-8KWs1a2BJpaUqK_YS78QTRkmB9esGrCVTJDioEQNDivKj5urfomolVVx8LG3MEPq0dMlVL0JjriegcWL6uWnp1xJnvUChuKd5Ag6nlnI35unLcw5tGyRFmSZ1NbFhBqs8KkAk6AkY0Ffe_7d4N5I6YOH_P13-5dm0wuy56nMAyTFeh0bDErsvALsMXvaGwR60k0Ci2YzMeBHiYwkrSe8l6V87Cl9I9SgP7pTyvox3fq-aNx9USMIRR20VsbzO0AhGRrAOSyI7FPsunkjhPb_JK1fqbmKzODWLw-UTQBabT4PnpIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پس از شلیک چندین موشک بالستیک به کشور قطر در طول شب گذشته، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، ضمن ابراز همدردی صمیمانه، به خانواده و مردم قطر تسلیت گفت و مراتب تسلیت خود را به مناسبت درگذشت امیر سابق قطر اعلام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67900" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67899">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=FY_kaN2JVs_ibE1RSt4Y7Sy12qJfj-sp5ZlS4NRiKXJZCg-q_ugEO3scJP0ZmNHLmbqtQNfn25UJuTAFZw9l-E_i6p0kVO2xIG7_M_UhOqC0I_IDM-zkTKF9_RHT2pM_9XcKt-HSb368-eh-kebT0Zf8PGFBgE-I5bBRLi33_39ts53zae75kBpCy3Jvd-h8BvCoqk43evMnQ3mSa0jRGOYR-sWACETwcTnCnDyDF27tb5XH5mWR2MraIUyvOEbRNHVqdaMiTPr4zQ8RWJ67Id6Jpuq_tuhcx6hFEQnyHJ7gvgNdQgNPNSrKtBf5NbIGlSpwr6rol8eKfdtGjc7OAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=FY_kaN2JVs_ibE1RSt4Y7Sy12qJfj-sp5ZlS4NRiKXJZCg-q_ugEO3scJP0ZmNHLmbqtQNfn25UJuTAFZw9l-E_i6p0kVO2xIG7_M_UhOqC0I_IDM-zkTKF9_RHT2pM_9XcKt-HSb368-eh-kebT0Zf8PGFBgE-I5bBRLi33_39ts53zae75kBpCy3Jvd-h8BvCoqk43evMnQ3mSa0jRGOYR-sWACETwcTnCnDyDF27tb5XH5mWR2MraIUyvOEbRNHVqdaMiTPr4zQ8RWJ67Id6Jpuq_tuhcx6hFEQnyHJ7gvgNdQgNPNSrKtBf5NbIGlSpwr6rol8eKfdtGjc7OAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش ممد سامتینگ در حالی که تندرو ها دارن شعار
«مذاکره با دشمن خیانت است به میهن»
میدن در مراسم چالسپاری خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67899" target="_blank">📅 14:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67898">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67898" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67897">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVFtAQ86MAylaXfE7xOaqQ3mHT6fOeoOEW2DM7IobdnCoVwfo-d93goVNcNkv2b-PCYCzzNWOha40_pn_Bqu8QAKblkDrF1Xw9wxIMfhDA8oOf85yxA5fOwc-xKoNZBC3NJrIbWqxwPWPWT7hADqt5GYcKNf021KJTkesZFqaV8pn3Okb_u_RwX8l2ol-N6XYm_V5d_UczPLFxrXYR4tBN5YMO3rKTySzd15pmIM8h2VoLUR9Q8QBD944DOINdGvKDvjJBftGTQnE3XKwpDvyidhi2riQOdGyKBcEvQQjvkznX6yC4bnNMO6fqgaHgvK3Z1O1jng-WkeMYJwROWf-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمیدرضا دهقان از اعضای پدافند ارتش در منطقه جاسک طی حمله بامداد امروز ارتش امریکا کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67897" target="_blank">📅 12:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67896">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvULATMieiLPn4GUZSNcv6Mc5K65DginSdhqU8Yk1YUM4ZpVxwm8W6KLY5_XSV--29MFEKc11Os2MQRGrKRrR3zyjXRA4-XhzLka-Vez6jVMIhmXR8dWcvkMDxJRsH3CPaL__QUxDw3R3fjpIq-GHgbfJ_HRhVYtBbyDPH3i4Mi4Qn4Eay4mlqb7G4IRo0k-TDiz4Hbzz6VczWwKqEJUfs7GNJRAxaEeFOM9IA1rz17u4Ov0j4CMPqZTjUQjBLAAjxCRybUrgk7yNgkGk7sfWSrQi3BncNq_uLnDeSV_rQKavPGsLMCXfApewE1tpLa7TChOWMiA-MAvmE2jLAem7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
واکنش مرندی عضو تیم مذاکره کننده به درگذشت سناتور لیندسی گراهام:
چقدر بد؛ من میخواستم او قبل از رفتن به جهنم قیمت بازار نفت را ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67896" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67895">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nF51OQyDSp1xoZijJUQBXccZOt-aQ_8tKQtdo1w47FLcLRc1pjREjqAc0qy7L6c28qLz9Ohng7wL59REulM201hrmJNfz08PNhQXCfqvVumC71iwq4Rc4uB6vEwiNCzClnsS_EjHPwl2KTKbbIAQ63ABgLXWCIZODW0L8rpe7dYvVYvTaANg3CG5_MLsOc93NNrN2Euqe0_Wj9CgOY5jCJVZw3hHk0IYDJ0JDH_8GtyUNn7ozqJLYjx_h9fiJwnE_8AytGcjIALjDgJL6CXBohhQjcAc1JwzW3idCcEvaVVYjrs5H32fjPhL93opd7Tz0nP-Vs40Uhwwp0h1pAsCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👑
شاهزاده رضا پهلوی:
از درگذشت ناگهانی سناتور لیندزی گراهام، دوستی ثابت‌قدم برای مردم ایران و مدافعی سرافراز برای آزادی، عمیقاً اندوهگینم.
در لحظاتی که نیاز به موضع‌گیری اخلاقیِ صریح و درست بود، سناتور گراهام در جانب حق ایستاد. آنگاه که دوستانِ واقعی کمیاب بودند، او در مبارزه علیه استبداد، در کنار مردم ایران ایستاد.
او از صدای خود بهره گرفت تا اطمینان حاصل کند که صدای مبارزانِ راه عدالت در راهروهای قدرت شنیده می‌شود.
حمایت او از «انقلاب شیر و خورشید» ایران، لقب «عمو لیندزی» را در میان ایرانیان برایش به ارمغان آورد.
یاد او همواره با سپاس و احترامی عمیق گرامی داشته خواهد شد. ما مراتب تسلیت عمیق خود را به خانواده، عزیزان و همکاران سناتور گراهام، و همچنین به مردم کارولینای جنوبی و ایالات متحده ابراز می‌داریم.
روحش شاد و یادش گرامی باد؛ و باشد که دیگران راه مبارزه برای آزادی را ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67895" target="_blank">📅 11:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67894">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTcdl1PxT_ym1lUzYmLFKk0kM-KMwTNj5WQoSEFOQqfdMnacomg4QJ6cAiSetwUFIWpNdX7w2R1o6A9RNmaS85xntGpTQ8RzYOqdEn_srUMfZxeMELP8EhkhBL4tKEmrX1_di9X2x7aYDr0Xn5UEy0OyvhXkliO-_ZBkANw60685jn-6OYCgCiSTBniY44gl3UcAezoS_ncRxJJkfp7VRDqbmXUp8g5h6RtPaCdOfX4kQh-yd1boSZ2WcePN1BMEFu7lcjeCoKntzg61adCFIJlHrHqE34ezozxLdQHL_wvLCoTw6C_-a257I3pQpS9LO5AE7nbz0W1aL8G2GG_fvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو نخست وزیر اسرائیل در سوگ مرگ لیندسی گراهام:
من و سارا با مردم آمریکا به خاطر از دست دادن دوست عزیزمان، سناتور لیندزی گراهام، غمگین هستیم.
در ملاقات اخیرمان گفتم: "لیندسی دوست بزرگ اسرائیل و دوست عزیز من است. ما هیچ دوستی بهتر از لیندسی نداریم.
لیندزی فهمید که امنیت اسرائیل و آمریکا جدایی ناپذیر هستند. او زندگی خود را وقف دفاع از آمریکا، تقویت اتحاد ما و ایستادگی برای جهان آزاد کرد.
اسرائیل یکی از بزرگترین دوستان خود را از دست داده است. آمریکا یک میهن پرست بزرگ را از دست داده است. من یک دوست عزیز را از دست داده ام
.
قلب ما با خانواده لیندزی و با مردم آمریکا در این زمان سخت است. باشد که ارزش ها و ابتکارات او همچنان ما را به سوی پیروزی و صلح رهنمون سازد و یادش همیشه پر برکت باد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67894" target="_blank">📅 11:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67893">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPtvfL8c9x-ikxhCN9OKariVK-9Z8inFi0rajFjx-f2pIHtl8br8GZUuAkcUuf2opjjYY_0haS_555299h7m9a7uoPXacaNMWXhKRJL65Q89_LqiP-nZKdu7EnlzK3m-0c0Mxdem_B_CUZtofx6aqMLlC2KU_15SSuXOA3pLuxwgUF3Lgs4r17nWZnKd8e17crNB8ScIFsH9DSnMNtrxguur4xtgL3H-BQSZ_oZis1HDLc5wOob35vXu91C7H5XZZQpqne4nOLRIJONNGNsGURIrNmmvyUuEE_k2hbsL2jY08CX2ihsFgu48Gp--KDlj55vDpdAzr671VcTQKusaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
سناتور لیندی گراهام، یکی از بزرگترین شخصیت‌ها و سناتورهایی که تا به حال می‌شناختم، از دنیا رفت. او همیشه فعال بود و یک آمریکایی واقعی بود. ما لیندی را بسیار دلتنگ خواهیم شد. جزئیات و برنامه‌های مراسم تشییع پیکر او متعاقباً اعلام خواهد شد. چه خبر غم‌انگیزی!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67893" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67892">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDxQXll24mOFqniywF86zHqRxVkVRtLfGz6kh33rdtqOYUSN4kmNh2NkmZRKTrF8DTUISOULKLrca2BejnbnfV69vdDUqqyjNVn8NZOMjhPlOs0WW9gfhdQ0ajKovNPyRPDmQ02BCSVejSSRpx0PAYUX1E0uetnpZg8DMFetJAItkOVbGrSNeymMr4kfgmlHiVswpPch_7VDETiU_-S6ML10PN1g-iQCO2UKbISlb8cxk9Gnr3JxcxNrfVQz9n5FGPjr607dc6UQFeWCc6MhwmjNAHs2Tz-4nL3FhTE4S5XSUPgtbovAKvpbbNq-mCFKWJyGUKWB0amDAULUehCOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ان‌بی‌سی‌ نیوز:
در حال بررسی صدای ضبط شده از بی‌سیم پلیس مربوط به واکنش نیروهای امدادی به یک مورد ایست قلبی در خانه لیندسی گراهام است.
این شبکه همچنین گزارش می‌دهد که عکس‌هایی از شخصی دریافت کرده است که به احتمال زیاد لیندسی گراهام است و او را روی برانکارد از خانه خارج میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67892" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67891">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edr4DbSSTBJgONJg2-CaVfTJ7wtq3z_E-CQW6MeqwnglpqAxEiQCEZUrD2x_pA4Iyi9gAVsEP07PvD6x6H2Vw-2KThf7SSJU2xYeCF1XdXA6vvrpXTmOgF2PJZh0_Alk_uq9HGFBdRl61z1gqR-BRXZ7MaGoJYUTHh-OydomlBvfUNYIG25UtlvxLq8vvIk63DJYXXUWwzBMb_3YzkHSwzUYR4Nu7WKB8AM2WAYQ1jM2NovydPbQKyIjMYjDZbUQh57Q3Iw_5IdnMEmcy6dY5MRGE4iHZVmId6rw47azmP6GOjiGOvUX-LYifmHDttqAGlFrmpFQs36CpMtcQmYRZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RIP, great man
🫡
🖤
#hjAly‌</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67891" target="_blank">📅 10:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67890">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5Q_779EexbPfh_S6llBVect1fajLIqBSVZT7lrFjtHGkbI3eBsOKDwPXEvYi0At9z_n4mQ1U7Zn1d3tPuupgvbxdzTwFdiW8tA7c38QTd1lqoKIkh-sVTVhepQneDuQ6TBCCmx3EuqUlHgxcqn5fuh53IrqmpHI3p7U-c6p6QrmmvGMnB4BofHsvllOhhUcJxPVXkPVxUVU2EfNGmOfD0nItVufbFb2RXo_a-rtjOQeXwScWMIxTk9oAupY-FlpgUMtF39k7_Kgj6USd-ExkmcLBQbFD6CKFNo69G5HPnmq8fxX-vf0Th5MFoNyu4FCeQYvv-Ys0GTdf4D8_lW2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:   دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت.  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67890" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67889">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJTJxusanixgKxANJOn2Z8UqavpcDW4MrKxUrX_2sIeDHRr-KJATF76LAnp7DM0ntAzU62wbf3G7JBgZMaGsnu-qODMXxfbD9gNghxP40zC8Nqd3Zx413lHp7B76yfILIzJKi6grFO8_Z1dn7Jx_fYGvvwfYdf-xa1Cr-aibGDmHJLBRsTnXoCtBLCQ46d4HyAwIgo_XCdWtRyiUXmfWQUdmtHaUT_W10JgPOcpLdO2Fq7n3aPD0iUXC62rs5GLfqn661mp5sXJrLV8Xpdp2s2X_phA_Xa59-F7L7ooGBoWNWcJUlMcamLX37nVgwqQXSnLGQiNuODckzPyyzDwBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:
دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67889" target="_blank">📅 09:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67887">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVMjXNhhi-NHuR80GLac8HYbXdzZy4spU5MQTiUwUyeX_wzM8lpYXw7V_WS5BWkBnrLyiIRPkIFujiU17WCa8otAUCUWP4foQIhTbtqoN39ihmQHmFMEBXvj_6Mi4683ivFY6ajKGk1mNtPs23iThd1Ozfg14VpgLcdG2H1VTjFQon8e0u2lhsQoDPAIkg21KLl1QzEuYXTMABJTr_cD1vhkV_x39k3oCpX_OS-3QyRMhnqLCqd5EfO-0j_mvVMvM8BF3_tC31EDdYmRdzQ6GEoouxrx7NF8opaxbJOTG7pLL9lP076KeiQEqYyIzyYO2NioMsX5VkWLRpN_pBVxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#فوری
؛
لیندسی گراهام سناتور جمهوری‌خواه آمریکایی و از حامیان انقلاب شیر و خورشید درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67887" target="_blank">📅 09:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67886">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
تصاویری که سپاه از حمله به پایگاه های آمریکایی در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67886" target="_blank">📅 09:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67885">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=GDoi1svG2QjkE24fdBJNMZsY9KZHfS7wDfh2TPKgQ0yk5x_z51CQBPenEruQoHRw9VwlM96qw2Ks-W2CtAoVTsAEIWwzRt2JpwlTEDr8gV3B_M1y0vEBnK2ZefD0eElpwQrkdPVD5JwFasm8d2qjRDXOe0snmMYhTJmj_tzzxR-oodf0lAToE1tx9KMRUNmjfo4K4rS7bvquAtT2720klXdMRnf9Ptop-ZqQBrNYzCleSYnopFWqzXgshJXPzX-ld1hwYvJdON7V79Dzio4TB8oq8GMPbbLYGDdbv09j7PPWEwoEsXCcKG3kezcqatFW13JBYjLEGOj6DDDFkN014IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=GDoi1svG2QjkE24fdBJNMZsY9KZHfS7wDfh2TPKgQ0yk5x_z51CQBPenEruQoHRw9VwlM96qw2Ks-W2CtAoVTsAEIWwzRt2JpwlTEDr8gV3B_M1y0vEBnK2ZefD0eElpwQrkdPVD5JwFasm8d2qjRDXOe0snmMYhTJmj_tzzxR-oodf0lAToE1tx9KMRUNmjfo4K4rS7bvquAtT2720klXdMRnf9Ptop-ZqQBrNYzCleSYnopFWqzXgshJXPzX-ld1hwYvJdON7V79Dzio4TB8oq8GMPbbLYGDdbv09j7PPWEwoEsXCcKG3kezcqatFW13JBYjLEGOj6DDDFkN014IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرباز روس خودشو به موش مردگی زده تا کوادکوپتر اوکراینی شکارش نکنه
اپراتور اوکراینی میگه: «نگاه کن لعنتی طوری نقش بازی میکنه که دی کاپریو جلوش کم میاره»
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67885" target="_blank">📅 09:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67884">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gx9_aw04jGhn4_AXotvNlfsI7AZ7RRrmrwDeqz2KTKCCkGBY41P3JavsiKyIMJo6Y9t-d9C8zgvnJCNk37abx9bqvP6yYGMuzm06Qs2djXsMvnlqXd5qD0AmEAqwKGlU2LLuCY0-UFFeHf99h_bmcs1jhFj39QnH5-ox7zlVgHDrQcdb3o8Iy7MYNCHlWFhjveAmGtJHavUI-CHxvI8uQz__uqFYSO0ujq1QeEGoymoCveoyYrYojAiPNNdEUSaskV0IzHT7HCAsRpe2gZ51TFFt7dw8mfrISFVqMlPRDsuJLjuo1Zz6jZNjMYenXMwl_Pw2YSjjKjxU8Jan3jRTmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قاليباف: دوران معاملات یک‌طرفه به پایان رسیده است. به شما گفته‌ایم: به قول خود پایبند باشید، یا عواقب آن را بپذیرید. واقعیت در حال نزدیک شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67884" target="_blank">📅 07:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67883">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ادامه حملات سپاه به کشور قطر
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67883" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67882">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه مدعی شد: مراکز لجستیکی که به کشتی‌ها و سکوهای سوخت‌رسانی متعلق به ایالات متحده در بندر الدقم در عمان خدمات‌رسانی می‌کردند، در یک حمله شدید و غافلگیرانه منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67882" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67880">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=CruRm8Q7w9QrtbmAgqSb4ETHSf_aJSXhvpYWSBm4bkT9Ye0wLsIGq0mRnc8L_y0Fb5Jb09xMDJIiAnib4mqot-08_hSINzWcAbGhUwDMz4rXR_OYatTxqpnPUl5C5jwynMCOQu6UAMmTyLpImy-xe97hiPjJGeoiuuWoMrbLOZEHRBKM7bckFPUCwhH_oGIyDctmUEIjNOUPgpPcUNPdMznpU8grcB6yvCBy5ms2isOh9A-B9K8k4gVsgZ4XHxSHZ4wamPoAUQDRtWfyg0piBXJk2eoG7L7ukxdiMYUUp-KGbzqkPBuW8XkwWu5pkbUINbNZ3BE7H2ZbEycSy6GB8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=CruRm8Q7w9QrtbmAgqSb4ETHSf_aJSXhvpYWSBm4bkT9Ye0wLsIGq0mRnc8L_y0Fb5Jb09xMDJIiAnib4mqot-08_hSINzWcAbGhUwDMz4rXR_OYatTxqpnPUl5C5jwynMCOQu6UAMmTyLpImy-xe97hiPjJGeoiuuWoMrbLOZEHRBKM7bckFPUCwhH_oGIyDctmUEIjNOUPgpPcUNPdMznpU8grcB6yvCBy5ms2isOh9A-B9K8k4gVsgZ4XHxSHZ4wamPoAUQDRtWfyg0piBXJk2eoG7L7ukxdiMYUUp-KGbzqkPBuW8XkwWu5pkbUINbNZ3BE7H2ZbEycSy6GB8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
تقابل سامانه پاتریوت در قطر با موشک‌های شلیک شده سپاه پاسداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67880" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67879">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سوپرگل تماشایی خولیان آلوارز مقابل سوئیس</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67879" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67878">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران مدعی شلیک و نابود کردن یک کشتی تجاری دیگر در آب‌های خلیج‌فارس شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67878" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67877">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67877" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67876">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=OSkDil26preV1dwFPeS3Za6SNtm2xiuJQQVAMQE8gEq1atJZTs_J2srjMwg0emKs82EZkr3SoouzY0_HLsalCMMwZWaClvGR5JlxEknwYjKgchYfKznCQy2n8EKVF9p6651ZvEqoxYkoJAOMuN1rXdnuWNdUYKtj0Z2sREumAtPd60nB0NSx0_SwAFfTtrjiHjvmVtM5Y8ngLDtEdssQ_nyRgtBLlozdl1uKXsPxJ_wwkp8PftYkHbbXVwisonzbWKd-oRoavdjOtryHwLWpRql-i6edq_cRM_W2TUpsj249XKQJnqV6M-6d1Bu1p1HdARbK0weLt7jSV1gqucXYnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=OSkDil26preV1dwFPeS3Za6SNtm2xiuJQQVAMQE8gEq1atJZTs_J2srjMwg0emKs82EZkr3SoouzY0_HLsalCMMwZWaClvGR5JlxEknwYjKgchYfKznCQy2n8EKVF9p6651ZvEqoxYkoJAOMuN1rXdnuWNdUYKtj0Z2sREumAtPd60nB0NSx0_SwAFfTtrjiHjvmVtM5Y8ngLDtEdssQ_nyRgtBLlozdl1uKXsPxJ_wwkp8PftYkHbbXVwisonzbWKd-oRoavdjOtryHwLWpRql-i6edq_cRM_W2TUpsj249XKQJnqV6M-6d1Bu1p1HdARbK0weLt7jSV1gqucXYnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سپاه به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67876" target="_blank">📅 06:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67875">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
😍
🔵
برداشت آنی
👌🏼
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی با
دسترسی راحت</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67875" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67874">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eroaPg6GG8jfUGXyfqs0BSJEnTE3ju364SG-6wNaAzlsfq3e9R133XpMnOfayOR663TF_3WSecf6w7uYz2E_xrazKS4GfG66u1dfcbwKgIyU3419lv_b_nSNNzGMhpzfgIUEM0iz7rWbDdUgt1qzecIsmj8VZlMkFssC7NkGgMEM3a5ciIBUco0AC-WimF0jJjW381giRqeJagXYQWoaxhH7f-wsBxmfrLRr7iFfKdlyHqG15HKyENr9pqfthC4vFn46qI2THQ7JWkn803-NWXkApqB3oz--XOKHcMtoBREiafdO4Xn5gXhbkbtUNw-xw0r1uHixSaiQxoEdAqcvlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تنها سایتی که توی جام جهانی هوای مردم‌ رو‌داشته تا باخت سنگین ندن
⛔
📣
خودم بدون نگرانی از باخت شرط میبندم با کمترین استرس
🛍
از این لحظه 20% شارژ اضافی همیشگی یعنی به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان بدون قیدو شرط میده
💰
🤩
🤩
درصد هم برگشت وجه در  صورت باخت،دیگه چی میخوای؟!
🌐
betinja.bet
🌐
betinja.bet
کانال هدایا
a20
@betinjabet</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67874" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1IDSRizctgL5jm_uBooUaoi_CBHl5Lgw4mN5WifmY7nCQ2ZY8MnFenpm4w6rmtmb5DSvbK6A1kVOyCOY4o0VW6iVMnfzlQ2RusljihG3nbmDbk0ft-6vnDf6E7ftjuD0HT5FUtXOh1GMTaBuLNMcvaZJLD5iEdibf23P36z0BpS6Oh_55-PRxJN2Ta5Dr3deTK_tUmFyfY_hrZRsi6PX_IqEeifYfwAsXkY3fJvLMMNC3PPAbjW2ORxkw1QzIIU1Sf70r6SPaslC0xmao65q7kaQJSy8kfctqcJgJkwVRxTMSZdCQO8gB9cQcMOO3pdJjwzzcw6YL0-FD5zVYM2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/news_hut/67873" target="_blank">📅 04:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67872">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو: تو جام جهانی طرفدار آرژانتیم،</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67872" target="_blank">📅 04:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67871">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپمپ بنزین</strong></div>
<div class="tg-text">ما که منتظریم اقا
❤️</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67871" target="_blank">📅 03:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67870">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67870" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67869">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67869" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67868">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
هرگونه خبری مبنی به حمله به تهران یا فعال شدن پدافند تهران کاملا فیکه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67868" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67867">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گروهمونو که دارین؟
😴
https://t.me/+5NElXlQWt_05OTlk</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67867" target="_blank">📅 03:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67866">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=r6C8IRA7mZcD0DubxIOxpmHaE10JU9-ralfKl2juVsyExua3DTY55FLy01NLP0T_CB6xh-wlpZIp8oFK-_k3zwFfovMNelDSwSyWhutiF8TW44ZuNFrF7IuxMrfa_r5clfnHL3qQEqe3EuH_NbcjkEdBCps1sGZP69mzTsEpMDPAnZIWK5VoQBU1F5Fcy1OVMXj_9ZWyeHe4QwJjuch21ZmtOThxH07e97iggwQSBlxsxXCZkE4po0C2Gp68pc1whl_Kif10qzJfXmzshMcmUd6Nm7ZKkkZwP0EnrjW13EEC8mC5siv8Ux3Fv9aCWqvhDKPTMvJ7owEDl4V8bc6YcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=r6C8IRA7mZcD0DubxIOxpmHaE10JU9-ralfKl2juVsyExua3DTY55FLy01NLP0T_CB6xh-wlpZIp8oFK-_k3zwFfovMNelDSwSyWhutiF8TW44ZuNFrF7IuxMrfa_r5clfnHL3qQEqe3EuH_NbcjkEdBCps1sGZP69mzTsEpMDPAnZIWK5VoQBU1F5Fcy1OVMXj_9ZWyeHe4QwJjuch21ZmtOThxH07e97iggwQSBlxsxXCZkE4po0C2Gp68pc1whl_Kif10qzJfXmzshMcmUd6Nm7ZKkkZwP0EnrjW13EEC8mC5siv8Ux3Fv9aCWqvhDKPTMvJ7owEDl4V8bc6YcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی  جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67866" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67865">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRazis</strong></div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی
جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67865" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67864">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67864" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67863">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝒕𝒆𝒏𝒂</strong></div>
<div class="tg-text">آخرین باری که کل کشور باهم دینی خوندیم رئیس جمهور مملکتو خرس خورد
امسالم که اینجوری شد
فکرکنم سال دیگه انقلاب شه
😂</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67863" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67862">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwFTNZd6Noygxfy-Vh-Gw1Xj8cPX2W0oCRL7vEE7USblSeOuPXmWsU_TIph7OTCI8qYcPoS7Un96_9AhetSI-_mt-I7sKZmjsT6kVBbmK-2PGUNvdL-Fm_y-Guu1mXYPeVmtUEL2KWzhw0eQ8cjY9yWiwELGLUQgyRyi-ZMm2Iixud2QOIet_x_Sun9LZGt7el8hCxE4BAZ2VqX9jAOZ9E0AQdtOmWYpBG3iSze4B3rYosiN6jYdhmFkdrx9D_KZDEIws7mr-MEY6XkN9qaAKWicDZ0iGI-r4lBlSFhiFwAuaL_IHmCGKnfDCgznJ7LqFwX7YiX0jynfaySidE2HkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقیش اینه به تعویق بیفته حداقلِ حداقل تو جنوب کشور، ولی اینطور کل سیستم امتحانات نهایی بهم می‌ریزه و باید بخش هاییش داخلی بشه، و البته با این مسئولایی که ما داریم چنین چیزی بعیده #hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67862" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67861">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeoJERGiZkuVXOdLu_A0N79DDf7OuAxKOhzvdJSKngLzLvCGWQ0eDeliTAISFzIUtoKxdpMfpY54VnoHEnfdGX4EMQQp17TTU-0CStpGeesmpECYv5sY3-EWM5gxArTrBKGGo3xOc2NrrxoZrmbUp0tQ2rcYo8pgIBohhKt-1Hb0KRTqQF2_RMuwRkCNqZibyZZt8ZOE8wIrcadMGnTdQ6K9yCAOWMH4oSmg-KzVuETpT8Biq1PNyQ1EuFyMD-7jOs1iBNtYCTQnFQLCUIen1Imluzxr_lGrpxQlkczV_ElzMOcU5Zbn3ZzSvz23dmEZEVYUdQHJrGLXlwDMiD2HgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه #hjAly‌</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67861" target="_blank">📅 03:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67860">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmDA344C4_uOhmd5NzpREgMz2nsya9xl0eVtITlee4WWC189z8-zkUOIFPBLIdnaybSDY5Sa4371pro3ZkglwQP61ozXxuPKhH7IxzqZEceueYzpGTTt4jsPLjp3ol34_3RTItk37GxCVTJNsU-cCpNn66hrJa-S5Otvj_fIix4H6AwqfqRR8TFTbMolobPsC8-I72yNOUxQ6zvb7fSf99KXAS0x5J3TbicPwHAfQD4p75FV74-amFAYp-uZEpKw91eWPOXJccbV93zPr1dEWXJqezneoXfmclw8dDiFoGoDRvZvxzr3N9hFfuuDoKbhJZ4E02HPu3KnF1MKV-krdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67860" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67859">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRmjyDHr_Eb54YJN8RC8C6Y1TdtA9tDI_XZGQ8vW2my50hJZZZl0pbxzPTNrZePM1QwvzKUj4rEIgMxyYLO41xqpS5rd0GLLbvWywYRsPXI8MsM4GZ073JmduCbmsbdhuYP1uNh3as3jnJge3jagfMSGXwnEctyl1RGcH-VR14gnnNZh-KIcwre2tvrrDGq2mLX2uq__3QA9N9VEQDyJpx0IcFZIDwLuAoWavbOy56N3jHaUE1lrrosIhVI8fOo4Ia720aySSal2WDT6DWiDt6QTyur13QBM8Odtk8H5UrUPSH1YynuzLhWrWv_kT_v3MuXRw9022bU6UyH0CwVFKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:  ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67859" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67858">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
نایا:
دو انفجاری که در جزیره قشم شنیده شد، نتیجه درگیری‌هایی در آب‌های خلیج فارس بود.
نیروی دریایی سپاه پاسداران انقلاب اسلامی و ارتش ایران با ناوهای جنگی آمریکایی درگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67858" target="_blank">📅 03:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67857">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
دو انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67857" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67856">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=LGQIV5rNwnMBu_nECAsPmTWC1l6t9n5Fn1eew2wlaZXAVBSs3JoPtkCe25ZrZcU-Lu2vnPRZ2Z45cgMmK8G8hubhU-I0wMWDIuMcx9hLCljOYzLenkWEL8jt2cAfRqdANAbktYtK282cQ-P8gUbNt5_r2635MeL4_2Gi9n86Jjaortttk-yAj3RJTXJY6UPX1m6FSFqhAE5t_F_1iI5hX_jTicWlBlgrQPmmpmJaeXH9iWHeEdNkHdPtLlHKKkxUJlNl2_tP_I0QIBta3GnPhjAgVoBWU7CV4-F-y2Ac9G9DyYB88zQPFIviCHbIV1y5a5Yg4QVLWm5EaI1TTrszIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=LGQIV5rNwnMBu_nECAsPmTWC1l6t9n5Fn1eew2wlaZXAVBSs3JoPtkCe25ZrZcU-Lu2vnPRZ2Z45cgMmK8G8hubhU-I0wMWDIuMcx9hLCljOYzLenkWEL8jt2cAfRqdANAbktYtK282cQ-P8gUbNt5_r2635MeL4_2Gi9n86Jjaortttk-yAj3RJTXJY6UPX1m6FSFqhAE5t_F_1iI5hX_jTicWlBlgrQPmmpmJaeXH9iWHeEdNkHdPtLlHKKkxUJlNl2_tP_I0QIBta3GnPhjAgVoBWU7CV4-F-y2Ac9G9DyYB88zQPFIviCHbIV1y5a5Yg4QVLWm5EaI1TTrszIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فارس:
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67856" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67855">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صدا و سیما در عسلویه: صدای ۴ انفجار در این منطقه شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67855" target="_blank">📅 03:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67854">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
چابهار رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67854" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67853">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
❌
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67853" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67852">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpn8oSx8yG9aYHLmy_UAY5lx8tYVDipRpdYWBn2t0GPthiacqrzspn_D5rREvojUbeA5JO8fiQHcAnmrH8Kf-AdGz39Qqs2wKyajoaFatQNrDIWdOImbuvWPNnkmhjyxpObxGaHB4zQgnRq9Ob3AvqPn7l-xvC8WWhlsS2tVh1Y3VGaNgkeCfdjr4qmP1N1ZYsDlIzCPllcX5DPBz5Hzgtrr4gBQoC1KthkUsdcpAO-W-sVKV6hlgyrR_JZUI0cd4Y_40dE9mZSR_NlZHCuMFSmWe7qITfrrzMfB0zCneLtProB4ayXWuV-nArSpd_ZFOGprQBkGrKbP_8oa1u3uyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:
ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67852" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67851">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=a9HvavzlmsJyc1QXmCd-WL7PW5fisYGWpxrJj3ihKl9C_dkzXYtbM0zsYGMcZIENIIqeWe7BbDwTyNUuPQWwI9_zVXCvowP3xd0DVW4GVMaGlpmpss0TLZIkN7JivQCL-lAy6LgfFS011gxy2Q3dQsX16ADkE4R5Scaj37A0GOcAvKjWk5A8Op-Tb9FUsFSfs1dolgBbmpaQEEjqCUJyclPuqK1pGS4kRa_0T9wsLkrc5nGCzIO5N8YqyvveZI4EOUZrxOjOlHH4Zz5KULqs7BkU85aAkWiLJO-660JLDbO-G2AfPXk7O6qav4V1wp_-46Zf_6pQ7cPhT9UrA1WY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=a9HvavzlmsJyc1QXmCd-WL7PW5fisYGWpxrJj3ihKl9C_dkzXYtbM0zsYGMcZIENIIqeWe7BbDwTyNUuPQWwI9_zVXCvowP3xd0DVW4GVMaGlpmpss0TLZIkN7JivQCL-lAy6LgfFS011gxy2Q3dQsX16ADkE4R5Scaj37A0GOcAvKjWk5A8Op-Tb9FUsFSfs1dolgBbmpaQEEjqCUJyclPuqK1pGS4kRa_0T9wsLkrc5nGCzIO5N8YqyvveZI4EOUZrxOjOlHH4Zz5KULqs7BkU85aAkWiLJO-660JLDbO-G2AfPXk7O6qav4V1wp_-46Zf_6pQ7cPhT9UrA1WY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شلیک موشک های آمریکایی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67851" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67850">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام):
ساعت 7:15 بعد از ظهر امروز پس از اینکه نیروهای سپاه پاسداران انقلاب اسلامی به یک کشتی کانتینری با پرچم قبرس که از تنگه هرمز عبور می کرد، M/V GFS Galaxy که در حال عبور از تنگه هرمز بود، به طور آشکار، نیروهای فرماندهی مرکزی ایالات متحده، سومین دور حملات خود را علیه ایران آغاز کردند. یکی از خدمه غیرنظامی ناپدید شده است و کشتی به دلیل آتش سوزی داخل کشتی و خسارت قابل توجه موتورخانه قادر به ادامه سفر نیست.
ایران فرصت دیگری برای نشان دادن پایبندی به یادداشت تفاهم پس از پاسخگویی به حملات قبلی به کشتی‌های تجاری در اختیار داشت، اما باز هم شکست خورد.
در پاسخ، ایالات متحده هزینه سنگینی را با ادامه کاهش توانایی ایران برای حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67850" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67849">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=fYiQjHHAV22_Uc1B_6cU3jNIemoHXGu2T_DZLsrifBF-dAhajlZwgxmX9ZbxfFTudcnmRYJCTDDs7nZGii4wWFSocInp4yAys0UCcYs363XqrD3uCc9SGjM8NlYO2EkwFylDUD0i8LddVfUkiAG7Z5ks3pGFVoHZspvV1RZux87oOp_GzGrAgibOYiwYbRmhL2lX2_29ViNVUH0Sl_iQdm2o6pJR2Nrw_fCXYsNf9JAb3IIWv712wzmdXHanC-hBxzuRp-jQy_qsi5n9hbezv7Zu5hrirmDe_gAsCGnYxzceEsxD4lOftVTqI4zBA6cTGyJ6QIb3ZEvhZRjJn-JqUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=fYiQjHHAV22_Uc1B_6cU3jNIemoHXGu2T_DZLsrifBF-dAhajlZwgxmX9ZbxfFTudcnmRYJCTDDs7nZGii4wWFSocInp4yAys0UCcYs363XqrD3uCc9SGjM8NlYO2EkwFylDUD0i8LddVfUkiAG7Z5ks3pGFVoHZspvV1RZux87oOp_GzGrAgibOYiwYbRmhL2lX2_29ViNVUH0Sl_iQdm2o6pJR2Nrw_fCXYsNf9JAb3IIWv712wzmdXHanC-hBxzuRp-jQy_qsi5n9hbezv7Zu5hrirmDe_gAsCGnYxzceEsxD4lOftVTqI4zBA6cTGyJ6QIb3ZEvhZRjJn-JqUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67849" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67848">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
🇮🇷
باراک راوید به نقل از یک مقام ارشد آمریکایی:
ارتش آمریکا در پاسخ به شلیک سپاه به سمت یک کشتی تجاری، چند هدف ایرانی در منطقه تنگه هرمز رو هدف حمله قرار داده .
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67848" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67847">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67847" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67846">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67846" target="_blank">📅 03:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67845">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
بوشهر رو بد زدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67845" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67844">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
چند انفجار در اهواز و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67844" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67843">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67843" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67842">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=ZUjFqULYdvv-XHFWsr4rpiEJioCgblUOYC-ffpyHuukCOSTaOHEGNyPhcaTPCFurtiK5ZGzB74H0nbj__lN4ChpeW6JZFljdU9kpYQeLeP0gFRWVEKCfh1yCGJa9PW-koA-7SB6cHaqBXNeJOEj1DrPsDxJKoq9Pm_FJbkZ-RRATD_EV131-XwkMpg_rQz95UzgR_BQVlDwmiHJ90I30_w_qs5q8_qe-s73n9wO9XaMSiYBGsyQ8EWdeDgImTXVVLIP3BMOrwFrW6lBnXmrji0iOosnf5wpYewBHWMLKz6h3qu9Vl2Uf_bnF9RulWLEEnKb7XsMRtfLqlALRnOd5EIQZ3bs1d7FdP6VIFuMpncPfrwJ_sInutwMUIh3Cwf8FFBHhhsKkAU0FwCzy9FXOH6kiyqjVs_3sDStRQaR_6LUaAbPLr6w_c3DFRv1gew0ZSCjRXozebeXICZQWMLz2yZPwMM_Jm15BAHQ4yi72apMOyPEQYC4HgCb1ewli7bj6wJpS4-OkaHlapRLgas3_IYALl30W6NbBDoQJW7rxdKYub28J7Okm2GRuiOm4PLBEuZmX_FvYcDdaIF6zAnZDyKI0mvb6EWFCVlZ6K7SwaBfTDlDNHH9zGcXt4KPfv-46vmbobzs8FWsqirJAVlSfGdV2E8fv70dMQtsSIFsWXsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=ZUjFqULYdvv-XHFWsr4rpiEJioCgblUOYC-ffpyHuukCOSTaOHEGNyPhcaTPCFurtiK5ZGzB74H0nbj__lN4ChpeW6JZFljdU9kpYQeLeP0gFRWVEKCfh1yCGJa9PW-koA-7SB6cHaqBXNeJOEj1DrPsDxJKoq9Pm_FJbkZ-RRATD_EV131-XwkMpg_rQz95UzgR_BQVlDwmiHJ90I30_w_qs5q8_qe-s73n9wO9XaMSiYBGsyQ8EWdeDgImTXVVLIP3BMOrwFrW6lBnXmrji0iOosnf5wpYewBHWMLKz6h3qu9Vl2Uf_bnF9RulWLEEnKb7XsMRtfLqlALRnOd5EIQZ3bs1d7FdP6VIFuMpncPfrwJ_sInutwMUIh3Cwf8FFBHhhsKkAU0FwCzy9FXOH6kiyqjVs_3sDStRQaR_6LUaAbPLr6w_c3DFRv1gew0ZSCjRXozebeXICZQWMLz2yZPwMM_Jm15BAHQ4yi72apMOyPEQYC4HgCb1ewli7bj6wJpS4-OkaHlapRLgas3_IYALl30W6NbBDoQJW7rxdKYub28J7Okm2GRuiOm4PLBEuZmX_FvYcDdaIF6zAnZDyKI0mvb6EWFCVlZ6K7SwaBfTDlDNHH9zGcXt4KPfv-46vmbobzs8FWsqirJAVlSfGdV2E8fv70dMQtsSIFsWXsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67842" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67841">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/todRNwf-DS5UHXz_c96CJW9PIqmt2jWF68TZxvXF5KfHh7hrvgfTqoOA5P92TW4Y5rtK1zVTCkTXqoWnI2_jQwIs855ot4c-VcexJsf8FrLhJUCq9J45qcHtNsCDAR0TVFC7Mxzgrs-O9giyWpCQ5wN3pAyYR3CuPr58NYuxnGDE7BmCvwEu4bqTiILk0AyOmexsoXEI5JtsKvXleJ28OMAiRDCz5zoXKsUNGPX1yslBg1IunM6wV9Kc5H2u4xZxghgkRPOfWjDW4GPyoXlhMmsoXczgWKNYVE05Jv4NyGnYuxZzPWLYYhe0tgIuTjaFzCQGE9x5eEuuOb6v2zsFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به بندر دیر
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67841" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67840">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
چند انفجار شدید در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67840" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67839">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:   من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67839" target="_blank">📅 02:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67838">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های شدید در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67838" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67837">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=nh6kyrX3URD03CEzB6VN047txKRcZxUcIF145P1-MYSEDsPPlYjA7qbMejmn61GwbVSyDB48ZFn48er0Dcp70fdTsb4UG-DbBiBUDZyHf8_Q2RZ66tri67kVkl44L91I9AXWTuQC1orqdOYKZfE9XnxkrD89V73f8W3b1nJIkXEr9cd33qRf_Y6QjME7CtfI1zYHvQ0cJ4xwg1UEvZAmeEqpmkPfK1IPj8MsYKok--syM6XMr1uMuE5hT9eyqUV-9KBBfhZnhjTewDHd8fF-wsAsAkI1tf-mzBQN6c0mDBZsQT8WgggBFELsH40SsGzH4nHJNML60PYJnO_heZOeRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=nh6kyrX3URD03CEzB6VN047txKRcZxUcIF145P1-MYSEDsPPlYjA7qbMejmn61GwbVSyDB48ZFn48er0Dcp70fdTsb4UG-DbBiBUDZyHf8_Q2RZ66tri67kVkl44L91I9AXWTuQC1orqdOYKZfE9XnxkrD89V73f8W3b1nJIkXEr9cd33qRf_Y6QjME7CtfI1zYHvQ0cJ4xwg1UEvZAmeEqpmkPfK1IPj8MsYKok--syM6XMr1uMuE5hT9eyqUV-9KBBfhZnhjTewDHd8fF-wsAsAkI1tf-mzBQN6c0mDBZsQT8WgggBFELsH40SsGzH4nHJNML60PYJnO_heZOeRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از بحرین به سمت اهدافی در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67837" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67836">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خسته شدیم از این چص‌حملات خدایی، قشنگ بزنید جاکشا
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67836" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67835">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
ارتش آمریکا رسما حملاتش به ایران رو آغاز کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67835" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67834">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از حمله به بندر دیر و بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67834" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67833">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67833" target="_blank">📅 02:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67832">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش‌های اولیه مبنی بر شنیده شدن صدای انفجار در منطقه عسلویه منتشر شده است. منتظر تایید این خبر هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67832" target="_blank">📅 02:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67831">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=ZZfr03YOCT5CbYWigHYVSO0ITVJYk1xXSzmqRbLPDecoicigTMsx4Izd0lz8_bhQqXqB-c5TG0MtCzCzzmfPgSc9hufXaW2MTGsXkK_MD3Q89QxJrnfsaSUVQopMhxOlQy56X8JfEGkKBSwbDfVL0vm-W7r5oYtYe7s5u1oKf1mO7KrKdOQHNjHXE347a5C6qYmGyQbSkyATyMHyJZMW_89-Gq5YgtWudG7ygI30F0eWZCWt73UfjhH3LKU5LB9znTdcJ3-Qfz0YcfeGR7FX1Y1OOK-y6t1MrMG93vcqFwodfYWP6NE9wMiptDOtxK3i5noxUdd_3YwceeFh5eVTfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=ZZfr03YOCT5CbYWigHYVSO0ITVJYk1xXSzmqRbLPDecoicigTMsx4Izd0lz8_bhQqXqB-c5TG0MtCzCzzmfPgSc9hufXaW2MTGsXkK_MD3Q89QxJrnfsaSUVQopMhxOlQy56X8JfEGkKBSwbDfVL0vm-W7r5oYtYe7s5u1oKf1mO7KrKdOQHNjHXE347a5C6qYmGyQbSkyATyMHyJZMW_89-Gq5YgtWudG7ygI30F0eWZCWt73UfjhH3LKU5LB9znTdcJ3-Qfz0YcfeGR7FX1Y1OOK-y6t1MrMG93vcqFwodfYWP6NE9wMiptDOtxK3i5noxUdd_3YwceeFh5eVTfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:
من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67831" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67829">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
تابناک:
گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67829" target="_blank">📅 02:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67828">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه
#hjAly‌</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67828" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67827">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67827" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67826">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilwnH_p2YwQAWicSbvz31fwUGnVTjs7IoaY9lJJEISU6sWQarzDpm-Rmym2i-VKlznZ6Vmk78EF7TegBhrIwQm75BYoa2mCu9GL5MC44_E1TBBdQyizU2YryYYv-h2GB_G12w8WTZxtmlM8l0mo2yG4wttZySujZg_jTnmeRIYPp5rrzDFcP7wGkV6fm-DA6TF-VnNSJhQlK030ZhGEVe_lSSOU1XsHTMl7sdXFiGW6A2oW4wVle6PqCR37BNo1ukgDfPQaVTos2ddVPotlgJ1cGxHzunpf0XTVPnTZi1NhwS54ONNtzkMdhhBEUG936E4f4Lf8kyhqGk64CGL-Hrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67826" target="_blank">📅 02:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67825">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrDJoV0JKZgMp9BVhooaDEhUb3I4Xtin36KHTN51goPBGOtpAertLJ-XE3uVAzpF5aUkzsCKKK2nZyldf4w-STNo5t8Pin9ad52s7AARpmxr49FoQeo7y4jOYi3GZdOfkuUHF4MgB_ib7KfAtwYiYOo2xZmAWJgl3s8MBULEspNag7AR5FwEeSmCAnSUeKhkxFlkmDRMIQ5tRLjLQLe2XKvFqiFezZg6Zp88iS_qugjo3a-Hjs-u67nNbwRiO3JsmXUyLMsP9viuqlDJ3jHoFMYIkXG5lCnBCKbK601ULyc9CckIQAK78hL7nwDKQMhnP7ViIX2pFPPRj6LD6Qyugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هم اکنون زیرنویس شبکه خبر
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67825" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67824">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNmxP83Ig_RO_KRXYIIm8rkr8QXN1KVs2ezVGZHLoixNmjl7vydSdbIYc7iA9bil6ZEWLbmcN4_t5fV9jVlWrCOKv1B9-jO-Vj60oei9Pg_gV3cEnzvMLXlSZXhGmkOldw6AwB4X8jlc2ed8gCG7fd22iXr0eBeZ_weUc0Cz4GtTcuo7IBOhFWv3BYnYBAX9JyMGD7BrfjwCh3dzBNhhWtktjyeYg9F6F6R_YydpEAGIRiobkUXXbRlhzQ-bF1qCwJ5ZLD4KV_XNCVckzY3g3Ns2cnoF5EuNfsUDxNiTuKovPL-JQbxnohvaKgSy_tW4dH7x6tK3zx4QJSg-f7cvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67824" target="_blank">📅 01:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67823">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
صابرین نیوز :
به دستور مقام معظم رهبری، حضرت آیت‌الله خامنه‌ای، مدظله العالی ورود به تنگه هرمز مسدود شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67823" target="_blank">📅 01:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67822">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67822" target="_blank">📅 01:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67821">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه :
همون‌طور که توی بیانیه قبلی گفته بودیم، هرگونه دخالت خارجی و تعیین غیرقانونی مسیر حرکت کشتی‌ها در تنگه هرمز، با واکنش قاطع ما روبه‌رو می‌شه و روند افزایش تردد دریایی در این تنگه رو مختل می‌کنه.
چند ساعت پیش، با وجود این هشدارها، چند کشتی با تحریک طرف‌های خارجی سعی کردن از مسیرهای غیرمجاز عبور کنن و به اخطارها و دستور تغییر مسیر هم توجهی نکردن.
در نتیجه، یکی از این کشتی‌ها که با خاموش کردن سامانه‌های خودش امنیت دریانوردی رو به خطر انداخته بود، هدف تیراندازی هشداردهنده قرار گرفت و متوقف شد.
از این لحظه و با توجه به شرایط امنیتی ایجادشده در پی دخالت‌های غیرقانونی خارجی،
تنگه هرمز تا اطلاع ثانوی بسته می‌شه
و تا زمانی که مداخلات آمریکا در این منطقه ادامه داشته باشه،
هیچ کشتی‌ای اجازه عبور از این تنگه رو نخواهد داشت.
همچنین اگر دشمن متجاوز به بهانه این حادثه، که خودش باعث به وجود اومدنش شده، دوباره دست به حمله بزنه، پاسخ ما قاطع خواهد بود و پایگاه‌های جدید دشمن در منطقه رو هدف قرار میدیم.
کشورهایی هم که اجازه دادن نیروهای آمریکایی و اسرائیلی از خاکشون برای این اقدامات استفاده کنن، مسئول عواقب این دخالت‌ها هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67821" target="_blank">📅 01:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67820">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
#فووووری
؛سپاه پاسداران انقلاب اسلامی از مسدود شدن کامل تنگه هرمز خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67820" target="_blank">📅 01:46 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
