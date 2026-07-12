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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 21:22:18</div>
<hr>

<div class="tg-post" id="msg-67925">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=GL1fjW-gMmAYNzta1YXZW9oM9vOPOeDKBCVjjqiw4slkf6muMaXoyeexDMADZgG219wq6PRd0-91rlrHeOybTRLro5-sJHsqhjbbLc-hAy1Ldh9IjPSOSqiRzCAYGribJbAHTlxlL-oafuXN1fwD9DTw5S164UQNldffUdA-AyV3H9psDWn8hEp67s4e9tIJ5NlmmE6vyjLl7UFfkhUsiZ8RhThxF9Kgvu-V_V7G2zxsru_3QfWcj4fm1tbt4n-Povnr63K3jj86Cx5gP1uhcKK5S7sPwHzCwlroAPKlGmMZY7eeRPIcMR0qYeDW8vDqyUq4CMfyGmACWf1yLuPKYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=GL1fjW-gMmAYNzta1YXZW9oM9vOPOeDKBCVjjqiw4slkf6muMaXoyeexDMADZgG219wq6PRd0-91rlrHeOybTRLro5-sJHsqhjbbLc-hAy1Ldh9IjPSOSqiRzCAYGribJbAHTlxlL-oafuXN1fwD9DTw5S164UQNldffUdA-AyV3H9psDWn8hEp67s4e9tIJ5NlmmE6vyjLl7UFfkhUsiZ8RhThxF9Kgvu-V_V7G2zxsru_3QfWcj4fm1tbt4n-Povnr63K3jj86Cx5gP1uhcKK5S7sPwHzCwlroAPKlGmMZY7eeRPIcMR0qYeDW8vDqyUq4CMfyGmACWf1yLuPKYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کانال 15 عبری:
ارتش اسرائیل با همکاری همتای آمریکایی خود، در حال تمرین سناریوهای مشارکت در حملات علیه ایران است.
ارتش در حالت آماده‌باش دفاعی برای مقابله با سناریوهای مختلف قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/news_hut/67925" target="_blank">📅 20:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67924">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ: امشب به طرز ویران کننده ای به ایران ضربه می‌زنیم
👎
خبر بالا فیکه و ترامپ با هیچ رسانه‌ای چنین حرفی رو نزده
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/67924" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67923">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
❌
وزارت دفاع کویت:
۳ پایگاه مرزی زمینی کویت هدف حمله قرار گرفت.
‌همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت هدف حملهٔ یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67923" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67922">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra87xl8jfzrkjyWJgdJiUe9DuyCGw3MzyYR9BxenGQuy1tD6fkvQwgTff4ffAljeCTecyvVL6rM58ynjoXSelTol6d70GJ0dlf5W9T41-ieh59XRVbA43OsKGB2IR7j6NdmTIfNutoV0Jm2RPxlpLRmnXPYkClMXAde40_9xHJ8NtGV3SjS-icjaEEZE26E3chIdWa4QlqBcUpmWSsQSQn-pEIYF6lj44KaVFS0NxAOI3bPWjbijcm0K_3CJQs6lNPr3As7furNBTWM25ONWOVv4fR1hGgtVzKVHwI87hKZ_czlfPeY3WwSCqwH0KMZMssfg9iqlxqOo-FcrkLDlZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
ارتش ایالات متحده چند حمله را علیه سامانه‌های موشکی و پدافند هوایی، و همچنین قایق‌های کوچک متعلق به سپاه پاسداران انقلاب اسلامی در چند نقطه در نزدیکی تنگه هرمز انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/67922" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67921">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
فارس:
خبرهایی درباره کشته شدن 3 نظامی آمریکا در حملات موشکی به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67921" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67920">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
منابع خبری آمریکایی:
یک حادثه امنیتی بسیار جدی در یک پایگاه نظامی آمریکایی در کویت، پس از حمله ایران، رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67920" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67919">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
منابع امنیتی به نیویورک تایمز:
ارتش ایالات متحده، مجروحان جدی را در پی حملات اخیر ایران، به بیمارستان پایگاه رامشتاین در اروپا منتقل کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/67919" target="_blank">📅 20:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67918">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8f7jEDwMbBc5Uc5CqnUEf2dLKS4neZAIynrdbP8qqrPDXqovQdre8xPiJPGkxCmcROyEwQ4UtVqypiTmCzf6brBUoy2dHFzYwaxshpuIc8SfFTJO_4TyJSLtFv3rzKIjYeuRVWORabOKk1ybxqBb5agFLBHDKGO5P9V0aXhKv5YwGsDvzUPUHt7Gyyy5tPDA4JwUewLH8VxYg2qDqbeh-K0_K1RF9KiUtX1oUucc7OIvx2ZLmNLrb1uKm7KG7f2qehyddaiG9KP73Ik9lGXJWTkhkrpKDepMESPCtOA1FDDRx5nPNwWvy50vGh-oj05Qdh4Y2-Qz5Du0AH-AftdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قشم همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67918" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67916">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67916" target="_blank">📅 19:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67915">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🇮🇷
نایا:
نیروی قدس سپاه پاسداران انقلاب اسلامی، کشتی‌ها و شناورهای آمریکایی را که در منطقه "کیلومتر ۲۰" در تنگه هرمز فعالیت دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67915" target="_blank">📅 19:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67914">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67914" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67913">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONzwFF1ViSZZ_22tcxLd_Hy_dmmXFP1AnU54XX4L2HLAgMFZgR9v77V4BOByttyfDVOlPHfVKU_iA5yIQ__v7jQ0iMIzf4q5fSFmg3vVh5b8GxTsCkv7ThqjFsMp7qus4RtHO3zjC1mylbmSwOFovbxMuQzQONn-_FljAFYMKbRZA0Kv8je_UfeWVTOTaFY3AcrqiBLGXI93mifQBWnUDv6YjWPJHuvoqE_YySugZCzqM_R5reUwkMP0IAdqVtBcuZ71tBaRWmimKnLJ_Kb7En8Jr5f8prYORBQeJvi2kf_OLJm8lNe_j3dTPqLRRYr2ycemh1arP9iLBBGeUjYc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تروری که روزنامه همشهری منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67913" target="_blank">📅 19:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67912">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67912" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67911">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
حمله موشکی ایران به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت.
گفته می‌شود این یگان در حمله دیشب به جنوب ایران حضور گسترده داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67911" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67910">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67910" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67909">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAHQHJve8eiPrwKc7YI1gtctGefso7dw2saA1BWC-JZqIy1a23SBFC7ZIxjWGRqwDN0YAAmNzq41jsnv0vBctwH2fa40_fWmefiQur3u8PiBUQ70XTa1XnGLKpSdxREeUOTSgl1akJ4YqLAGnD_TZ8kC_SqT_r19kqFW4KFmlKgzc5O-DBYc9F2Z4PQ5fUC4hj-YvrGWChHbtSpGs04f37emRecSVEXwYdMR8VV0c4cplOqCn7qGYumJi07fPFVCEAKke4SPLze8wKx_uaF921iKkAp0mc4kTE3Whnno2-ObT3bxZCjEPuH1SypCAplk_4J7KspSjvK4PGfFiPEl5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دو انفجار در کویت و برخواستن ستون دود
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67909" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67908">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67908" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67907">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67907" target="_blank">📅 18:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67906">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
یک فایل پنج‌ساعته از مکالمات بی‌سیم نیروهای سرکوب‌گر در اصفهان به ایران اینترنشنال رسیده که نشان می‌دهد نیروی انتظامی با مجوز استفاده از سلاح جنگی، در ۱۸ و ۱۹ دی‌ماه با کلاشنیکف و وینچستر به معترضان شلیک کردند.
دقایقی از مکالمات نیروهای انتظامی در بی‌سیم را در این ویدیو بشنوید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67906" target="_blank">📅 18:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67905">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67905" target="_blank">📅 17:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67904">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=PsW40PPThMbO7Q2_z2PAudJX3ptq-Rq6nGT2TgQWWJDJqhZpsb_rCaFmTd0nlw-Xi9S3X77cIKTmm4R4akYaSooTniBJycG3LeFgtsl-SsxSm_tBAIVa7UWmC5eW9Mv_1BRaDywT8lR4tnFYeFTO6ELeoGxah_cvigYSGXRoBdEKLGEaSXznDRQNH6OGIqw1TtxV5tHw1wKka49FTYhVF1V5rin-pyTM6durvfIY1CEzc3nBo7fnFz79VbvHn_jvEczsWBIPSOp6o-LVdKfL9nJhWGHwFaaV4c7kWYQMcoViEAlm5SQTgABq_RAZs5T25_gEoX263RyusPPc9PQzlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=PsW40PPThMbO7Q2_z2PAudJX3ptq-Rq6nGT2TgQWWJDJqhZpsb_rCaFmTd0nlw-Xi9S3X77cIKTmm4R4akYaSooTniBJycG3LeFgtsl-SsxSm_tBAIVa7UWmC5eW9Mv_1BRaDywT8lR4tnFYeFTO6ELeoGxah_cvigYSGXRoBdEKLGEaSXznDRQNH6OGIqw1TtxV5tHw1wKka49FTYhVF1V5rin-pyTM6durvfIY1CEzc3nBo7fnFz79VbvHn_jvEczsWBIPSOp6o-LVdKfL9nJhWGHwFaaV4c7kWYQMcoViEAlm5SQTgABq_RAZs5T25_gEoX263RyusPPc9PQzlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب شدن سرباز بر اثر انفجار اشتباهی در تمرین پدافند هوایی روسیه(نزدیک بود همرزمش رو هم بگا بده)
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67904" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67903">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-m8Jq9vVmqTskXSPKKeNUgLNTTkpVbucYqtHCzQoJwbO4-KVJzRw0DHQmS8Bf1HqI1dGWH5SV0hSuP3v10Sg-YLY9P_9PTyqBjui8CUOgv4AoTY3a51arfRjS-sOhY4lSGQpUwO35n2Vft_Hge9TwUmBBGf5sV9RYBNPEfMJcqPCz4YKj0I11fFvOWymeWB94RR7YAsL06i6nTLt7my-41duAPT5S-6aQ6BxSxsac8tcnZ4YKN41jpUTNp2jLlltBfzvpL5NQ9KtxnGf1nFWiUF0VU5s5Uo1aCJcQd9PVHP-mX_KJeHDuAGOvLtpKA2W1OuqKlk07QIRoo_qYA-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمامی کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای آمریکایی در این منطقه مستقر هستند و آماده‌اند تا از آزادی تردد دریایی اطمینان حاصل کنند، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران. ایران کنترل این تنگه را بر عهده ندارد. ترددها به روال عادی خود ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67903" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67901">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8QdmLnRyL1dKLjXiSyTq1lei41KrDiLRB5B693eiT5JLYGL74faL4MFeebFIuUZRL7ffBl5TXAUGJvdVxMg3Zl3uuskAQuBTuoXd_s1NJY6sZZpyk__L59hO2C2pkWGrrbYT3j0bpSKdMtrDydqdTJoaIRZyq1_QTPRk1ru0qGsjihbbNxZtLhW6r2DVK5O83HuY8tDjnNy7nJ4UN5C8Qa0Bq9AcIvO3CtgsKWLrYR182QYibgwnYg39mgC8IER5vdCOojd9DdyUaR991JL3W1Jxgubb5fsTmlCA94AvlB2zrmPwjt-_VAZFunIhBlQzJTTtceeeWb8fCm9Mtg1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=NmHQ0emjQYrxaSqSWiv4Db8FnQNpDWxEsRDJEr-RQvRacQTD3sE-uSUwNI72djBZA7lQMnilslmgkO5E_J4gao-8VtJT1pebfXIWh08GawfXp2fb8Tr2PJGx9rAx1pDRdSK8FC2XKpBPtmr8HwN5LjN5GIx8KbPPjutD3i91nNCcLJ4sSesVqDWHv62ZYg6Xv1nQRKOzTFUKGlH-PvtEu6NsSrJPu5Hc1p74eZubjcpNc_5UMXQkgjFv4-kVdx2miXJF9RRUbrVvjdgJp4cmDwLymklLO-Du7i_7bJ5-ZecFC0Dzm3YfVfCbQYf6Qv_eNvL9ZEMMVThBoX_dDjPJLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=NmHQ0emjQYrxaSqSWiv4Db8FnQNpDWxEsRDJEr-RQvRacQTD3sE-uSUwNI72djBZA7lQMnilslmgkO5E_J4gao-8VtJT1pebfXIWh08GawfXp2fb8Tr2PJGx9rAx1pDRdSK8FC2XKpBPtmr8HwN5LjN5GIx8KbPPjutD3i91nNCcLJ4sSesVqDWHv62ZYg6Xv1nQRKOzTFUKGlH-PvtEu6NsSrJPu5Hc1p74eZubjcpNc_5UMXQkgjFv4-kVdx2miXJF9RRUbrVvjdgJp4cmDwLymklLO-Du7i_7bJ5-ZecFC0Dzm3YfVfCbQYf6Qv_eNvL9ZEMMVThBoX_dDjPJLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از اینکه صداسیما رسما مرگ لیندزی گراهام رو تبریک گفت
فیلم تبریکش بشدت در رسانه های جهانی وایرال شده و گویا برخی دنبال ربط دادن مرگش به جمهوری اسلامی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67901" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67900">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFdw40W9grpatxFeJ7v_7Wm4wGAld8aIG6kV-8KWs1a2BJpaUqK_YS78QTRkmB9esGrCVTJDioEQNDivKj5urfomolVVx8LG3MEPq0dMlVL0JjriegcWL6uWnp1xJnvUChuKd5Ag6nlnI35unLcw5tGyRFmSZ1NbFhBqs8KkAk6AkY0Ffe_7d4N5I6YOH_P13-5dm0wuy56nMAyTFeh0bDErsvALsMXvaGwR60k0Ci2YzMeBHiYwkrSe8l6V87Cl9I9SgP7pTyvox3fq-aNx9USMIRR20VsbzO0AhGRrAOSyI7FPsunkjhPb_JK1fqbmKzODWLw-UTQBabT4PnpIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پس از شلیک چندین موشک بالستیک به کشور قطر در طول شب گذشته، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، ضمن ابراز همدردی صمیمانه، به خانواده و مردم قطر تسلیت گفت و مراتب تسلیت خود را به مناسبت درگذشت امیر سابق قطر اعلام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67900" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67899">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=rwdqkM7op32lKRhcEoxy-8DDwdH563DEyE0wSST-7chDa7r7eD_UsW_RN-Ep1rMA6KnoHl6OfxotTwGPY3qTXMNRdAj9BgWJEyqZx5s3aW8_ZFotHoDRctbXR8QSPygUQACqcpqyNmZs31LD2X0PoKwXcSzMsAKxhV0o0w4Nwexe2gO1LKZ31pf38g4YQOfjDM-kx_taQBConFYtvPNC68LMxPWJ_N4fyjHDCRdBJT-dDZZr0_VOL2E-6r8GogUpIxI30yR7UbYBn3X3aQdcs6RI7Uk9dcPbiQo1RmnFxE5e20S-CO2FKNODe-1ArUI9Xz3eUnGCCeDl5nojnPupqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=rwdqkM7op32lKRhcEoxy-8DDwdH563DEyE0wSST-7chDa7r7eD_UsW_RN-Ep1rMA6KnoHl6OfxotTwGPY3qTXMNRdAj9BgWJEyqZx5s3aW8_ZFotHoDRctbXR8QSPygUQACqcpqyNmZs31LD2X0PoKwXcSzMsAKxhV0o0w4Nwexe2gO1LKZ31pf38g4YQOfjDM-kx_taQBConFYtvPNC68LMxPWJ_N4fyjHDCRdBJT-dDZZr0_VOL2E-6r8GogUpIxI30yR7UbYBn3X3aQdcs6RI7Uk9dcPbiQo1RmnFxE5e20S-CO2FKNODe-1ArUI9Xz3eUnGCCeDl5nojnPupqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش ممد سامتینگ در حالی که تندرو ها دارن شعار
«مذاکره با دشمن خیانت است به میهن»
میدن در مراسم چالسپاری خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67899" target="_blank">📅 14:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67898">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67898" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67897">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWZnfUHbRyefd8E0T7MGN1MdvvY1YbovwQqhEPxK_TUou_SljhGmjRM74KAkblGwPJgV6I1Lyc-9BPjAJCwbsQ7s_-vQ1doCeTovuS_58K5xV1evhLDoj1EWcucU1WJBkaKeQlIITSsX5CXjvbvsHjXoiyXsikVP8Im19B6w10eITkhx0YzHF1Hvk1dBfleadYpkQuRhJ3wyWyo6HFnVV_f7RyUkp5gOOUo7Vtp5pjteKYTMZWYzdSWiypauuID0RqDEKwNRRMNmByBsu26GL_XH_a4OLDFqtIeH9a63Wje1Zl9CYSVIOLoaQWApmSi20fjQAmw1RpeM9eEILG4RBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمیدرضا دهقان از اعضای پدافند ارتش در منطقه جاسک طی حمله بامداد امروز ارتش امریکا کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67897" target="_blank">📅 12:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67896">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsR4Cu3ce_puDdLHz3iop8VgX7usNc17R_gan0JaOg2f88X2FRGPmOUkmfVjSH41R_zmAjGdC31qZFfc_RZvnwTHhiyKBHVrbkk1FIXoag_GSxlB-y-_gu7KFjgyBudgvzPuucLlQxGBO19Od6KyiZ31C2TkIPmVN3B2WtCpFl3QCzQoh8RFRyc2jiTxAkcxFhyUm2OtEuWqd-TDTnptHCDG6E9iUBLgoCikOEwavOKyAjqflEzPW0uPftei3cBsM4ZmF0NjLXv3QDnK7gYcjcJX7D6L7cz0QXcpJF9yL1UbsXi1yDH7tiH3qh8R9qVkNoES8Yi-EAUxU4YAeK7Y2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
واکنش مرندی عضو تیم مذاکره کننده به درگذشت سناتور لیندسی گراهام:
چقدر بد؛ من میخواستم او قبل از رفتن به جهنم قیمت بازار نفت را ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67896" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67895">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgAgWkiGJHxzKoLUXTiwTXNfZkdam9khx7jtKXcIcN6eRZvXHy8s8GA0CQ21hNw5JPQSi-m1UiNFb6rs_GzTKyHYJTcDf--3BDj_gzM2p3bvBk2BCM4zF9dfDNS29f1g15T9U9D_Cilsm6rOfZHsK8G2sx_weUalgauT8Bh-Rh1xECtKo8cRBuy9De7X-1srve4oXnXVkiWyeO-vieQLq8VoBqVgj4a7RSShhiVTg5tYE6t3Te4NsU6x6QFYLoW92r4mdTnT5g-JdUKUttYkoMJDJUXHRRbUxVu78aKQSGNzEsrTgDZCPgLm7h9rsiaFTsINhbmB-H31ztZ9lCNqjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67895" target="_blank">📅 11:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67894">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue3nuifXfzDPLXqkZCh5S00aqc0WVBi5TenV1C9GHqCaHITFK1mPabc5OnNxclos916DHmMiYJnybsTppGNCI4ZFpUKcb9SY3UI9PTmF31U4Xh_WpgaESLRYSGxcE-Quv-1zdrAxBMm244RfvQIBDZj0MBzbG59NUwT69Mw8IlQPUp6crxAHMn92X3pqLaC-mha1VUCKXBy4H123Kxqz4qSNlRJPW_o-FqeVcBzheDj8wtW96qckCfTX4mXsj2rBgFs6cbQ_xLGE5p-qiNgdcjnjsp9Bo0H7zuz5iTsh1KguiiV9tO2BliVIH2RiHMKoMPkVlLCxd5X7AVNwbVn8IQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67894" target="_blank">📅 11:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67893">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ryo_ArJ12qw4e-LbWoLDm43FRN1rtm3ovLn3j8G_DN5crlX5WyYB2-DjeXsjm6iIZ8CxY25TFlCh31u-ZCdRSiXJnVIfnKiJB4EmzdRPiTSFOXAukzXdhdLa3oltsEQxkpvJmfZNP0CNvVcp6nSHem3cHwJ6YBxQOGF6qKDOO5q6S28J4kvrGvIhEyzYDgO6KV4c_imKq8wFeRa16oKtf6IwoYe4xzZkkr4aayaQp1_S-Xj7lxMFNODfvgkVAU-HH-fubfgJhR3s0momvebeB65ZyfdnnkYFNHBo--oXi0Par0klMH25bzaK4ZiNgyPMtNtqXgmEBktes7EMQgEsfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
سناتور لیندی گراهام، یکی از بزرگترین شخصیت‌ها و سناتورهایی که تا به حال می‌شناختم، از دنیا رفت. او همیشه فعال بود و یک آمریکایی واقعی بود. ما لیندی را بسیار دلتنگ خواهیم شد. جزئیات و برنامه‌های مراسم تشییع پیکر او متعاقباً اعلام خواهد شد. چه خبر غم‌انگیزی!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67893" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67892">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4Y6xDU-xXWaO38iTeDsGeV1YplsMl441yIpT33JIX8mChSAQ7MLtLDCzo2_gwnLDcs99XRsAjsKn71SsJzbStMxxOxUENJSHl46mor0WDd3lh9BSBnDi4J-cgsQg7S0FUFeylvtD7oKfD17Inz4YL8lUoVx1aZy1v0kd6jqhTSD8srbeRvITDGXkn3dxJ0GOgW4UNbQuJq-5rDPPqbvmF9XMCGHYKxF0QfIMoIHNZcqAlNCxSj4AUUnGCYxMiE6YJBrwYJSGOZ0KyVirJHs6lhhzA9TDGCP2ienQ2TOaHdqz83cYyIOonbIFHaYVnaJwT2Pnj6-n-eONK64mfLudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ان‌بی‌سی‌ نیوز:
در حال بررسی صدای ضبط شده از بی‌سیم پلیس مربوط به واکنش نیروهای امدادی به یک مورد ایست قلبی در خانه لیندسی گراهام است.
این شبکه همچنین گزارش می‌دهد که عکس‌هایی از شخصی دریافت کرده است که به احتمال زیاد لیندسی گراهام است و او را روی برانکارد از خانه خارج میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67892" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67891">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbXIgjBKcszvRlToqgEFYnEpaahJuBWUgqqk_mOGC_ocgvQtryayvazzulW_C_S_WCMtE5JruNZJT1XjOeVzk3MzaAaxzPwFNLRzxhWnHZd-UZk_QweXGUviXvuuKma-b24HOwF5MvEOPNh6SpHWajoFepDf2zPl_TodoX6OSvlR70rcqBZ7Z0MAMoLbz_mFeuNjp4WPzihqYOcJIy_qw37KUchp6CStIy9JXsXBBwRuPW5opQr1vJvNiKRpvXfHkyVS3haJXnbo_esAksRMFjEFCX5n_czl26Ih2QefFaxbtbkQREwUz6vJyzAlvGgiNTpbkKLfMVUTivipMfHlQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RIP, great man
🫡
🖤
#hjAly‌</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67891" target="_blank">📅 10:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67890">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5767TDdOpSiTrVDvwr0AgUTJALpbW8r7kO-yhO-9ZKER1w2NihwjaEVxlf6BSJ1t2xnt6Qftc7F2H_kn4fDDo0VyH0NrRi-em_1lvfzKeANv9LD0LnhM1gXNRxF3f7vYmS77CoBxetpdSDbi_KRqV92ysYHS3sjN4tFeXs_Oa5BKYtg0GFhR0Gtx-AJGTrbYHH35FZS-cDmCoD4h2rFlrO1nej18jARZh7C5kMf3ftq_f2Zy9rLAN4zyNFJatgBg5GZZWV-Nx5ktQc9-V5V287ARCQf4xssSWvud0QYSZziKEBK7UWktlh680JbT0w-xFEOm721QqgAcVau-CdCKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:   دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت.  @News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67890" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67889">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLj2phToMEOc-SREo5lYvuMncMmChzVbVeMdN2LmYBiofhNFPhafE6RFthBfSbr6prhrUwaWvKYK77MhnSLT0AadX_6QKgzUUvBcbNcu4DvzsrrnlgREHe4cbMT0P_hmKNU67T1Yo7ho-PmqfjGrImzHYqBsk-9pHFHkBNulWkslt8KcmoEF4m-Kb4h_mlYepAZW9kwKJwbew80u4_oZTshjgL2TnHJZ5GyExOCWQyCbdmsOq8FjplRSkt8u2QxFu-X3WSVfvxGGC6oHMAlgBTd2c_8Ly2b1zOj7vpY5JCRCFVi16MjLi8YEl1ZRCsiWENdk9VIecb4rHSO9Ylyhnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:
دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67889" target="_blank">📅 09:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67887">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vghBtCag7FNut0bzTKAU5im6tCWAqd6v_94jp7J660nZr4TB4gznQ6DjgIhHvhtPA1pxsbdYzMMcb3mehqid_PlxvGLXtV9MkKuHl_d_nEYz2Zal3NeoZMLWnMujmeijaGz60b7rMK1jAVDsHBcUR3e_cLPoYfCv0IBY5IRmqrFQiN5qlcgrtJFx4fTPb_4j7CD8BoU7OsFApaQCOOkTQhrMfohBL0ZLLLSzrIRmVfTbonk9HcLYLFKiAFfWxmTLjSBJ0vd7tqtMtTc6yc3pzboo2VMnXkNaJJschqinlSlNBBxne83mXg9r6yOA7gicl8_T1nJKH_mFqdLButGSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#فوری
؛
لیندسی گراهام سناتور جمهوری‌خواه آمریکایی و از حامیان انقلاب شیر و خورشید درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67887" target="_blank">📅 09:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67886">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
تصاویری که سپاه از حمله به پایگاه های آمریکایی در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67886" target="_blank">📅 09:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67885">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=YpZ94Jtqd3ypvmhe-l3xm6WzwwspFHKHMfaT0cVNOgQ0sFn0whI9bivS7SVYg0sU04V18Umv1j6LlSmZJp1WNziYQiAbuU3iS_bhuegKkAqDkKY9odkcOoB7CWmWyem5IvbX9kO7n__CAWXzMajlw7OHSVEbnjrN06aLYEO4czi7vfSaFhRZVT6KTwClz3IsR8fnP4ghUCZWXfHZ0EM7BDrIpiV1ju9DtMKNViry2Ni0iMQzYPSS4qqp90QIcTi3Y8OEgpHhA_AdCwWMR5r-8ehXZT-4AbW46Buuhj3ja4Nv9CLAjHwWIAGjwjIqzi91NitErkFe6mQ0Pxn6dBuhkIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=YpZ94Jtqd3ypvmhe-l3xm6WzwwspFHKHMfaT0cVNOgQ0sFn0whI9bivS7SVYg0sU04V18Umv1j6LlSmZJp1WNziYQiAbuU3iS_bhuegKkAqDkKY9odkcOoB7CWmWyem5IvbX9kO7n__CAWXzMajlw7OHSVEbnjrN06aLYEO4czi7vfSaFhRZVT6KTwClz3IsR8fnP4ghUCZWXfHZ0EM7BDrIpiV1ju9DtMKNViry2Ni0iMQzYPSS4qqp90QIcTi3Y8OEgpHhA_AdCwWMR5r-8ehXZT-4AbW46Buuhj3ja4Nv9CLAjHwWIAGjwjIqzi91NitErkFe6mQ0Pxn6dBuhkIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرباز روس خودشو به موش مردگی زده تا کوادکوپتر اوکراینی شکارش نکنه
اپراتور اوکراینی میگه: «نگاه کن لعنتی طوری نقش بازی میکنه که دی کاپریو جلوش کم میاره»
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67885" target="_blank">📅 09:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67884">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzZrkFKEfeuvfkf1L6sJaL68r7EvaX3uvdVcl-68rvFzQZbdwAWaW-kyESx43UejZcg2oryGhA5afQvNE3H6Dh46E2GcsMYVZmMKYNhxKLJ48zUg0sgKQ_CEXkaroLREu3d3VThZri6JgMM39vQQSoNHa_egOhVgIYJ3XWhYafRhKcYoVyVuxvc_RG9mInkXej_wAQ03Rgr10llq6rfVy9Zm1ug4ASp50mH1xUg-17LbCJ8iWww8nEPm2oeMP8sPPwLY3cPac96leo2ENR1RDILLikeQrX7rooHJk0A6ngRWHS68CNPRR9Bk6zKqle6Hja9h9dIHxeYFyj03jhZGgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قاليباف: دوران معاملات یک‌طرفه به پایان رسیده است. به شما گفته‌ایم: به قول خود پایبند باشید، یا عواقب آن را بپذیرید. واقعیت در حال نزدیک شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67884" target="_blank">📅 07:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67883">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه مدعی شد: مراکز لجستیکی که به کشتی‌ها و سکوهای سوخت‌رسانی متعلق به ایالات متحده در بندر الدقم در عمان خدمات‌رسانی می‌کردند، در یک حمله شدید و غافلگیرانه منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67882" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67880">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=FdUZ7ABQpy9WPNHSynRTv8W-BA6KplIvSPNtY1fWJET1k11OKVTnjOXtk1_x-jSKsBFRq_gPAnne_zd0VeTIO3Ps4Yb6c2fQLncsh_F4jayQ8L6DNf2tpGcLVSvqFfpa1ZHJ_BJJWXTY005ndcoL727WLisYXjel9c2olGQSluNr6gD5XDGWQWDzonR3EVvjMG3uYqLqnBGmEcED3DkCKlEqVdh6TX-59ZhhIfCfAGgqMC12MbGV2kcFlaohoAU_RKcpbfcfNEHHBmZLNXyNTv67rCXHltBLbIxyaAFdnzMH9OD7LDjqfoKhI6smqY6TOCempluBSmYYHz5XP9Lt2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=FdUZ7ABQpy9WPNHSynRTv8W-BA6KplIvSPNtY1fWJET1k11OKVTnjOXtk1_x-jSKsBFRq_gPAnne_zd0VeTIO3Ps4Yb6c2fQLncsh_F4jayQ8L6DNf2tpGcLVSvqFfpa1ZHJ_BJJWXTY005ndcoL727WLisYXjel9c2olGQSluNr6gD5XDGWQWDzonR3EVvjMG3uYqLqnBGmEcED3DkCKlEqVdh6TX-59ZhhIfCfAGgqMC12MbGV2kcFlaohoAU_RKcpbfcfNEHHBmZLNXyNTv67rCXHltBLbIxyaAFdnzMH9OD7LDjqfoKhI6smqY6TOCempluBSmYYHz5XP9Lt2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سوپرگل تماشایی خولیان آلوارز مقابل سوئیس</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67879" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67878">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران مدعی شلیک و نابود کردن یک کشتی تجاری دیگر در آب‌های خلیج‌فارس شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67878" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67877">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67877" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67876">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=IoNz7chhT9gXTzOrYh9pBD5iaygH8PxBQ_w_XYcDpkPgu7DCcGFu5vFqIEvOPuHn0WWWnB3Sl1jOrvnxMyxZMB70ov1hbTWuBeRZXDmiHRc_8QhqNH0SPCSFVVK4ndcCwkUfqcnFvFaTmVD3-er19hL-RNSGiiJF-dj3Ppq9PYsmhtC8zUSCT6rL3W1yMiqu4_2EiY2dtetVnZyjQ2qycGcQYOXIUKyZ4RAxxN1qzWcyXsxvKjdPGXTCUEQx2Y48zICakbAvQyU16FgWgCzYJ8L2jZhSxjcsWPbwtbnCV669VjbsH3p83QErGrWLBSEXQZA3gVhsr29VnDf79uBhlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=IoNz7chhT9gXTzOrYh9pBD5iaygH8PxBQ_w_XYcDpkPgu7DCcGFu5vFqIEvOPuHn0WWWnB3Sl1jOrvnxMyxZMB70ov1hbTWuBeRZXDmiHRc_8QhqNH0SPCSFVVK4ndcCwkUfqcnFvFaTmVD3-er19hL-RNSGiiJF-dj3Ppq9PYsmhtC8zUSCT6rL3W1yMiqu4_2EiY2dtetVnZyjQ2qycGcQYOXIUKyZ4RAxxN1qzWcyXsxvKjdPGXTCUEQx2Y48zICakbAvQyU16FgWgCzYJ8L2jZhSxjcsWPbwtbnCV669VjbsH3p83QErGrWLBSEXQZA3gVhsr29VnDf79uBhlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سپاه به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67876" target="_blank">📅 06:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67875">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/As3tjJw7MRmsaPG6ev_nOgfyhNzLz2PVzqTrhmw5RAJOAeN8xBDOfkKEnzD_koErtpPdFFPbioHjBpdHkiwGyNOPCbLkZrAatPERL7nqf8ilELhiwpZSP1_wB3UyzuX2MlWboy0oPPwuejIu0OhzO-NWI6WUyiNCbfYvtKsgd57H1J-OCBYa4_eFDoWs8CssKNtTGIpCcR_fDwYTTbA5cWtvQwttLSEp2a_H77iRF2TP4-0pCJaxZPDsdVtVQs3tFrdbSPhZ9Jo6Uz4Dx8LWmZNvYVbhnniE12ntk9-QqYNztYnXnd4r3oQXQOaG3yfL6dqKnmPCLrXtBNsN7Mez1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67874" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDhSi4YMHDh-CStF82Y2nj0ZvLntpZK_1MHszaIwfe7eGhZcXJxq6Szfo7wI4NzJ11zCiIRu06c0-226XZWtlCgiDsX0Bx2_39z5X6DnC7h7XLCVTyWe0bxY-LR346rA9uvRxSSHUyykmFf8nSD4g3DC8QVQV2iHiF21DSfsK_soz7pJ5HsSK9HN-ZwSTYolNmHrk9TroT4xWrvxbQg-rVohJMRxtxenEsN4OYeVLTVJXqPPtETliU5REyu8eryVPtZ2pm8-KIF66TTk7gYFvUp8lN7csuI9ZdYRDzzgAidjqC8jp_u-hgG13h1guJhrFDcK1HYV3KRkErBjJkOMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/news_hut/67873" target="_blank">📅 04:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67872">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نتانیاهو: تو جام جهانی طرفدار آرژانتیم،</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67872" target="_blank">📅 04:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67871">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپمپ بنزین</strong></div>
<div class="tg-text">ما که منتظریم اقا
❤️</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67871" target="_blank">📅 03:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67870">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67870" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67869">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67869" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67868">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
هرگونه خبری مبنی به حمله به تهران یا فعال شدن پدافند تهران کاملا فیکه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67868" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67867">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گروهمونو که دارین؟
😴
https://t.me/+5NElXlQWt_05OTlk</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67867" target="_blank">📅 03:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67866">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=N2DZWoUbK8bBxCVY4pdOZw1XDrluCm4RfCTZWQ8vjZVPmW0Z8eM8jzwOM3vdGoeqWd8qjrmOEmyVSoyuBi1ULwVuA2J-TUav8yf-VKM3ODNnPqWohiJ30LJd8NSO0mxvRaK2FW0UzPWKxhz9E9snwWTg-7-9QjhYU5k-zWATEDGMbx94Uo44jT0t1SI9-UynWFd7UWech2DHm8XOOtBOEBx5ZXuDsPAtmh0HWHEywAzMEpCPD2yiW_a8JKaJg2Cq6QchrTZc0IVUjCpuWA1oHkN33YXuCZlyIZuNBFRbeAtcOJ4GwkMO03207vxU5kZqtBl5MbYKCW7oPYJ2N20V9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=N2DZWoUbK8bBxCVY4pdOZw1XDrluCm4RfCTZWQ8vjZVPmW0Z8eM8jzwOM3vdGoeqWd8qjrmOEmyVSoyuBi1ULwVuA2J-TUav8yf-VKM3ODNnPqWohiJ30LJd8NSO0mxvRaK2FW0UzPWKxhz9E9snwWTg-7-9QjhYU5k-zWATEDGMbx94Uo44jT0t1SI9-UynWFd7UWech2DHm8XOOtBOEBx5ZXuDsPAtmh0HWHEywAzMEpCPD2yiW_a8JKaJg2Cq6QchrTZc0IVUjCpuWA1oHkN33YXuCZlyIZuNBFRbeAtcOJ4GwkMO03207vxU5kZqtBl5MbYKCW7oPYJ2N20V9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی  جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67866" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67865">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRazis</strong></div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی
جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67865" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67864">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67864" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67863">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝒕𝒆𝒏𝒂</strong></div>
<div class="tg-text">آخرین باری که کل کشور باهم دینی خوندیم رئیس جمهور مملکتو خرس خورد
امسالم که اینجوری شد
فکرکنم سال دیگه انقلاب شه
😂</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67863" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67862">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxI--PrVNh3lFJ5j9sMP0nxHKRzt2QXTMtQdDvoSJrpHVuvzC_w-Dtegt7M-1xmeXfXlQgFAlv4is_0ejVqYmZt4lvFBbPFIBdYbcVEMDYGd2bY1Kbg0PR5CL1KN534gV4nkfcsPaa9UgZ1g0rACiAlthzIY-u0Hw_5lNgwx23hZXuv8enCUtXjUrSPbQKOOqyypzUChRPsRbVGCEnxhx8ZWVgRoiT21axEWGJ1g9BafhNOZmD8VfRX3rKgsselGI_sF4ryjxX_BOHh3sTGDOwvkQ2tjJ66_XSw9T67FNFeQgwoP18tOnvRIpcQN7RbeIoG0w6O2QHp47z19w4BOXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقیش اینه به تعویق بیفته حداقلِ حداقل تو جنوب کشور، ولی اینطور کل سیستم امتحانات نهایی بهم می‌ریزه و باید بخش هاییش داخلی بشه، و البته با این مسئولایی که ما داریم چنین چیزی بعیده #hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67862" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67861">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6aMNme6tC9x0_bFZgZKoIv4ZRkg8MZUVT4pxX3bs4SCoGsXaZfdMaDlBwq_VQ0s0m5KN6GiCb1nudlcsd0vOCTwJu4GbW40nian5W1iJ9fUpOVUvJd4jCqosJd4Jgcw5iqkBAgQK_SUjFvWo8_M4O4v7OmQzwWb31yw3z1F0iBbiYb5vxN_nQAVztBupKa1cJDRa9TUCgIFWdIBz2PIfjyLWIl5jr_v3w6ktBIEh9Ito9-gtt0HkawPFM386J67KS5KQWMkmEAYljKmEr8bMv05TOwp-GPGA5md13tYWJwekrG-iz8ITMscg0FCVFIRTnP-tY4LGB-DkBhx3bHWHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه #hjAly‌</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67861" target="_blank">📅 03:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67860">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeyiE2ILDEiMikKToEukp2Mld0gthr864tglFmDJ8bsk9N-JoLvZXYrqMGLC3ky9XCGR6V75OG1VwOLpmTLBrqoOD7HNOK76yNkd9sIfbmvdbUOR0DLkJpLEaEEsUxb5i0C7m7yaEICouQA5mrZIaZymADbW9d3S6irTPUt8TgHBUbrAMYwhcMKBGrNsg1KRfz6P85Ul91ssjAB4WxEZTNlVOQOvxdoGf4cGFHha52mTFU5axUq7hKChniJzo3Tez-mZA01vnFyWGh_rZJD5khwiVidNHdh0WMW0vTgss0rHPsSxUTiC8uupEVe9_AtSacGLK5TGVBz0SH5hoHZjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67860" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67859">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-qAv4cu2kTsayRCC80zhHpPYJCqxAEqspGemlV_3Id85kDVnF1JySUdQztq2K7WrpfBioSD2erkOiVnMUPV5157KnNHJrN7Yrbxf_VZsmktJ7Fd-dw9tiho5Ti2aTTMSZojy5rqmysDF38vl4Mtg7JHM5REqiH7A13EQBBS85Oju647I9cE_yMvF3Xd2YG66Xyl7gj3odgPDMwJJqPXPFwq7pL-ZSDKOYsRJhAuheFVY1OifwBoFTYQZjsJ8Hpyz3H2aB_A7IBDMXotpToPC7FAXwnVxJCUbw99eQaJ-Xi8K1sltd-DsVox1M1-RMdAwF8ms4229m4yRzBju8-Aww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:  ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.  @News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67859" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67858">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
نایا:
دو انفجاری که در جزیره قشم شنیده شد، نتیجه درگیری‌هایی در آب‌های خلیج فارس بود.
نیروی دریایی سپاه پاسداران انقلاب اسلامی و ارتش ایران با ناوهای جنگی آمریکایی درگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67858" target="_blank">📅 03:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67857">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
دو انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67857" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67856">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=YAA9D-MRmWMqNNtEqihCwWjQ69vKyoj5qukvmd4Bw-hSmHIraTogkvfdFq-BmTs04NNF34_An9AKKPzOIpZQjqZilFe4WhYmp2Ye1Y0LVuWug_FrAeGAIzbK-RmcHxrc4zSQkqLhDLVTLbzJ-bM0h9WYqkA4bGPpn9D-zpEGId2Y9B1V0rm5s5AVf6lJFj5E7thCaGdn4cQMk1IfyGGIsJ_9OPwEOYMnylEOFB4NTFiwdZljh-jDL9UTyaXeCSVBPOCtt_Mul62kLi3pjdcLM7XqcL8_tA7VVQS4HaqV5aom8LFMKJkv2Lo1B5q_GVyoWx5P1cWMSK4JJ_hXChfH-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=YAA9D-MRmWMqNNtEqihCwWjQ69vKyoj5qukvmd4Bw-hSmHIraTogkvfdFq-BmTs04NNF34_An9AKKPzOIpZQjqZilFe4WhYmp2Ye1Y0LVuWug_FrAeGAIzbK-RmcHxrc4zSQkqLhDLVTLbzJ-bM0h9WYqkA4bGPpn9D-zpEGId2Y9B1V0rm5s5AVf6lJFj5E7thCaGdn4cQMk1IfyGGIsJ_9OPwEOYMnylEOFB4NTFiwdZljh-jDL9UTyaXeCSVBPOCtt_Mul62kLi3pjdcLM7XqcL8_tA7VVQS4HaqV5aom8LFMKJkv2Lo1B5q_GVyoWx5P1cWMSK4JJ_hXChfH-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فارس:
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67856" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67855">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صدا و سیما در عسلویه: صدای ۴ انفجار در این منطقه شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67855" target="_blank">📅 03:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67854">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
چابهار رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67854" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67853">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
❌
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67853" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67852">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4M5NesLzdogrs1Lz6ZGj-a1fupd-Cre475BZ1rwQMkqdg4d_LQAui_OXkIix9SselcjEVSJbSUolYBOuQnH_NPc363NV6Lm0zszme5P_y0sWI1PwhPCg_B1fcbED6VAbJMIx7IlQ9efwuxF1ZS8OuBNwbSQI1Txk0qhRXt-qgvPRNGlMAAGUjKyv0_NVsO2ajXgtsLKa9FT65IPMmmdpSrVWgrSWyCXfJ2dNVgXAy4_i31JJYQmA6Ef5KrL5nZ_LDqe74YVcvLrRl0p1zPfhY5a-DJsH3IhywtZu6YnwCPy59wEAel-Bi7wEYUgNhtgEPOsW6qt9yIwHIePbhAzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:
ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67852" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67851">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=rYHHjdUrJXyCfDKGZVB6Y6d_uPA5KerLpVqp37tqFLZxoXlF1s2d3siq-Phz6mDczUmcu9BRAJpVx3HZ-eP-2PpB22PPfUIoJft0_W33Vu2jNJqw3dmTKWO_fRTwUmVXvkC-o0u5GxiIbyl3YTklSu-ejQEX-jYyrzkTR6UEvg8sksVdOWBBvITgqiZDuCjVotWwCsDgu3smePolZyx3gceoFUebDIaIAFRnksH92G0LWyhN24DP9j7M3Lp1w3JAcmliy0MlDD9R_-sCj_3X80CITSlnwpxttOlLEN7n4a4i50yqAurpMx6QhcyYCO6eAGkziCVY-f9uMB4OfSvKWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=rYHHjdUrJXyCfDKGZVB6Y6d_uPA5KerLpVqp37tqFLZxoXlF1s2d3siq-Phz6mDczUmcu9BRAJpVx3HZ-eP-2PpB22PPfUIoJft0_W33Vu2jNJqw3dmTKWO_fRTwUmVXvkC-o0u5GxiIbyl3YTklSu-ejQEX-jYyrzkTR6UEvg8sksVdOWBBvITgqiZDuCjVotWwCsDgu3smePolZyx3gceoFUebDIaIAFRnksH92G0LWyhN24DP9j7M3Lp1w3JAcmliy0MlDD9R_-sCj_3X80CITSlnwpxttOlLEN7n4a4i50yqAurpMx6QhcyYCO6eAGkziCVY-f9uMB4OfSvKWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شلیک موشک های آمریکایی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67851" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67850">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=sXB6lTXS9KbO7VLqXvT_8-_gJU5hOsfqlWQcIeDrcXTmjG60HwgtC07MsTpVZFb4brmf-4vM0qdYWpHkhjnsvDCLdCe1Czpz34IqV3bBDF5Swe9brSK0890pdnOFygBR93uNFzuM01LD56fP2AvyWe5-0QZNE0khB8LFbUYggXrlTfsDBSAOGki629LBSHu03AK8-x5A3azXysGcolK7xG8mNkQ9BPwL60nNmono2eSyoptyfTZ5o6mvkNC5OV8P3RWpxO_Ijt4oKO3wnpUOsXulKe-LQHyaLJYIZnju6VxDYQnTRBfolfHeEnVRfTwjL8zxRd3m8IEkLakkJfq8lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=sXB6lTXS9KbO7VLqXvT_8-_gJU5hOsfqlWQcIeDrcXTmjG60HwgtC07MsTpVZFb4brmf-4vM0qdYWpHkhjnsvDCLdCe1Czpz34IqV3bBDF5Swe9brSK0890pdnOFygBR93uNFzuM01LD56fP2AvyWe5-0QZNE0khB8LFbUYggXrlTfsDBSAOGki629LBSHu03AK8-x5A3azXysGcolK7xG8mNkQ9BPwL60nNmono2eSyoptyfTZ5o6mvkNC5OV8P3RWpxO_Ijt4oKO3wnpUOsXulKe-LQHyaLJYIZnju6VxDYQnTRBfolfHeEnVRfTwjL8zxRd3m8IEkLakkJfq8lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67849" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67848">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
🇮🇷
باراک راوید به نقل از یک مقام ارشد آمریکایی:
ارتش آمریکا در پاسخ به شلیک سپاه به سمت یک کشتی تجاری، چند هدف ایرانی در منطقه تنگه هرمز رو هدف حمله قرار داده .
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67848" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67847">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67847" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67846">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67846" target="_blank">📅 03:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67845">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
بوشهر رو بد زدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67845" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67844">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
چند انفجار در اهواز و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67844" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67843">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67843" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67842">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=rbhmwfJDgCBK5MZaKmxWMw4Iz7xGfc5enaq_aAyhOTzHhPvFPm3HqS_0dteyF6kp6i_mQa8nSycMfDPC5xCig_unoG6x-Taetx2cho-MWEWCOnrBbVF5xer7B4mFdUtkW9eRuquesFDVo6dcvqrO5j_ByhMnbpEALDYPKT-iv2czS3lqcbLgVKlX32LsYLT6teM3EjrR0mTpro5e7LS4lDm0rZ2T23-VBTe6fBPAaHOZMrvLGn88d2tjwWbdG_abeMXVxXJWLtoY3Fp17kzNa0EyAUgeN0K_8PWKKZy_26BmlwbS7FS6K9k0aewgCy2ciq_dffU4Jp8_uDn40Yo9eQOAmRlBrxOqlW9GZ2i8AwAA9u4SpuXr7mGtTfSaMIOriJHYyGCbHTAmUvDXJnuvqVnbFqbHwyC8Thu5qObOsCxvoRm4_8vjtH2pbC7bF3Apncy-uK3vjWELHKbB-N3bc73tOknpCwDBCR3uyJ8FkFDHe6kOMnkmOGmcm8P9IBVA2nUM7dzxXSyQFXRtckeEM51TocMB72qSCvwfqGAyhQTkZKSZRBPXHFoEPTiZfLWAxLaHP4xigykR29-74k1vvYBT9wWDtL56lKaBdv53ppPkZkz-yUKZDiKy2uCvvcZQJg3dM3vjFvrEGcZ28xVnIKTuUPtDJkSrd6KKumA3hhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=rbhmwfJDgCBK5MZaKmxWMw4Iz7xGfc5enaq_aAyhOTzHhPvFPm3HqS_0dteyF6kp6i_mQa8nSycMfDPC5xCig_unoG6x-Taetx2cho-MWEWCOnrBbVF5xer7B4mFdUtkW9eRuquesFDVo6dcvqrO5j_ByhMnbpEALDYPKT-iv2czS3lqcbLgVKlX32LsYLT6teM3EjrR0mTpro5e7LS4lDm0rZ2T23-VBTe6fBPAaHOZMrvLGn88d2tjwWbdG_abeMXVxXJWLtoY3Fp17kzNa0EyAUgeN0K_8PWKKZy_26BmlwbS7FS6K9k0aewgCy2ciq_dffU4Jp8_uDn40Yo9eQOAmRlBrxOqlW9GZ2i8AwAA9u4SpuXr7mGtTfSaMIOriJHYyGCbHTAmUvDXJnuvqVnbFqbHwyC8Thu5qObOsCxvoRm4_8vjtH2pbC7bF3Apncy-uK3vjWELHKbB-N3bc73tOknpCwDBCR3uyJ8FkFDHe6kOMnkmOGmcm8P9IBVA2nUM7dzxXSyQFXRtckeEM51TocMB72qSCvwfqGAyhQTkZKSZRBPXHFoEPTiZfLWAxLaHP4xigykR29-74k1vvYBT9wWDtL56lKaBdv53ppPkZkz-yUKZDiKy2uCvvcZQJg3dM3vjFvrEGcZ28xVnIKTuUPtDJkSrd6KKumA3hhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67842" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67841">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dB6lUn3rWKZCA5u9YfUlwbSPzOyjpvKTiTYlemKrN2imec07Yxnxn9uK07kVJjSWmiyCfAbp3A9hGyDOvLI75BKRkSr47lmJ9CL2h-Pqwo5atDjujRIlfPqmyCzeOjN8ZnyF-IZXRuSl3Zk6iEp9WVzH32sPf8fmJROWx5tOWBQfLoav1AwYlEdXilJ9ZzRmgeduxpD6Jx12hyQoI-WFXmDaupB1vPJkeYndB8dw2p4MhyJeDbcrTVReMSeW-442MLzhBC0or9-kwht33n4VqXXbPRHoUl2LXZfES4jKy5Snz1Wfz1jttVvTl-TrpS1FVLbZQowoGouosRpEPeI-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به بندر دیر
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67841" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67840">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
چند انفجار شدید در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67840" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67839">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:   من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.  @News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67839" target="_blank">📅 02:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67838">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های شدید در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67838" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67837">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=r37DIhCDHKIBFCOxDEbXPFcVQiqbZMU1aIVnDQIPP4bMqFOLBILNj07V_7ZGxiCVc4rOwmOEWvGWXW_XBMbAGt8BsFI-E5_1V9YzudSQrlU4Y8kYGR8iBV0-J21Bkmqz2p2BMjJHntQTjo25HldF9w7ZTRr-LB7JcSWTuA8a5zyhzgxSX2A81ckDgktVGd-OuRqeJ_OrbyS6TrhTiSUpOn9attKQiP1s_SP-5zr_SbekFKfYfpe6a7_0rwopLiQ-LWrkPA_ttJTBv39k8XWExkVPLCh_Jb4MlsN9s0SPf8BNXd_trcVnsGQ19cfxAdOUmUYUjLi8pGT97-chvGirNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=r37DIhCDHKIBFCOxDEbXPFcVQiqbZMU1aIVnDQIPP4bMqFOLBILNj07V_7ZGxiCVc4rOwmOEWvGWXW_XBMbAGt8BsFI-E5_1V9YzudSQrlU4Y8kYGR8iBV0-J21Bkmqz2p2BMjJHntQTjo25HldF9w7ZTRr-LB7JcSWTuA8a5zyhzgxSX2A81ckDgktVGd-OuRqeJ_OrbyS6TrhTiSUpOn9attKQiP1s_SP-5zr_SbekFKfYfpe6a7_0rwopLiQ-LWrkPA_ttJTBv39k8XWExkVPLCh_Jb4MlsN9s0SPf8BNXd_trcVnsGQ19cfxAdOUmUYUjLi8pGT97-chvGirNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از بحرین به سمت اهدافی در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67837" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67836">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خسته شدیم از این چص‌حملات خدایی، قشنگ بزنید جاکشا
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67836" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67835">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
ارتش آمریکا رسما حملاتش به ایران رو آغاز کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67835" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67834">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از حمله به بندر دیر و بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67834" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67833">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67833" target="_blank">📅 02:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67832">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش‌های اولیه مبنی بر شنیده شدن صدای انفجار در منطقه عسلویه منتشر شده است. منتظر تایید این خبر هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67832" target="_blank">📅 02:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67831">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=mTmFyodkEK-3o70aiT1qcOd4k2pjLHRjbCEA9U3rVNGH1bfI3fIh8EVtivQ7WcB_mJu2Ng0shAG3y3j7vgZnDIljg7iUwgmT2zno3qFDMzqmYOK8z5R51kCR3Rti-lmv81ZoKy7hSZLrhML6OxEA57IKZ_PmIr1eFgmNWvMxZbursll1UQjrSh_wnKo5sMjuv3PteS3bYI_J_boWsa98hqwAAulY5cdPG9Z9aLDymcxJ7oRswzGVyJRbTUrsOzTzqcKnqTmjX2N3but3h7y7MmE4LIXPf8UEEKncJIhqh4eB8EspalQj52cwV8zTBbo7t5OXAQ80KzMB199ZwPRsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=mTmFyodkEK-3o70aiT1qcOd4k2pjLHRjbCEA9U3rVNGH1bfI3fIh8EVtivQ7WcB_mJu2Ng0shAG3y3j7vgZnDIljg7iUwgmT2zno3qFDMzqmYOK8z5R51kCR3Rti-lmv81ZoKy7hSZLrhML6OxEA57IKZ_PmIr1eFgmNWvMxZbursll1UQjrSh_wnKo5sMjuv3PteS3bYI_J_boWsa98hqwAAulY5cdPG9Z9aLDymcxJ7oRswzGVyJRbTUrsOzTzqcKnqTmjX2N3but3h7y7MmE4LIXPf8UEEKncJIhqh4eB8EspalQj52cwV8zTBbo7t5OXAQ80KzMB199ZwPRsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
تابناک:
گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67829" target="_blank">📅 02:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67828">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه
#hjAly‌</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67828" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67827">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.  @News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67827" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67826">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqGhVCDUC2hi_Eqn4aQOHnw_Dy52WRZ-27iKpmwr4GjtYAsyG80gUshn3N73xxG27tplYfEIUKnGJZyfIYLEKlGbJg0TzGVukpQXxv9hspr63jj6dvMuAlpeh65NCEKasB6636dkAa9MiNaIkEbQfcNmiSDK8t_hhkpqMhRXVt22iiSNoUq8d1zNs7JPqr8nlWG3I_m1m4VQA9QQpxTF23D4VyAUHIxaHCdV7HDziw9PR0mIXaIT3QW6C4Wxv3iMgcUOJQdz0lXFCMHqpEtke2xce5vZj3BWHCQm1MoGhmmfJxsQemUcpVRDEQ0_u7Tf0MeEgQ2n7fK9BvGXdrAiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67826" target="_blank">📅 02:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67825">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYdxIPn9vFHn_BIgeWBZUJRkfBslQAmuFokWhGp5QB00bLxosWVk_0w1zxJ6YOSYNxfqC0NHa2ufArvBtnNAFQkZwf9SIlTF0ofXM0An0f9E4XzVjiO_drY9aBcql4X4tkSI0s694CiD_1dTYjh6Bn06hc7i4fxykLA5GBhkBw1vM7scrnEf9CnEm8zLtxUHt1b-fBOK-PmOHLzX6im4wFxuyaEhznZGNxnL-02R1e0YZJz-7McKXxSwpY3R9tTQXRl3-hMpxklK-XSZyGgs9xDfahu2pbSBV8OkfyCAWPnRyN-tR_ks8skstx6MECIU06cElDq1bCEJg-Sj2iyWdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هم اکنون زیرنویس شبکه خبر
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67825" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67824">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZQHZcWrfXGvePE3-MC_vgmzgNgq6NWFI-HYw7D3dvvTS-0EUW8DJzWVu4-QX-qpjPn57uJDU1P4K8bDhFt4CPAXpBsj0yHXN4U0ibGOgi7B-h65koFrqo36XbOSTL8ECNMNwxNx3Tunnku-8w-ExnPkvC12atPWeOLyaWNXn-A5MCJJHuadLFko_XKJgn5BeraXccDb9xHvYqYNdjXt0_bR2XVcbOB0fc7tobbsTAtuDmdG_A_cS9MRQQ66IOlaMKlDAOOBkubYW_gWZQwYUdX8KOGCi3Dcw7ovTZC8HiQQrpapzDeFODnqTQyNo18fypCdp-_kyIW8YCbnyxg8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67824" target="_blank">📅 01:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67823">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
صابرین نیوز :
به دستور مقام معظم رهبری، حضرت آیت‌الله خامنه‌ای، مدظله العالی ورود به تنگه هرمز مسدود شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67823" target="_blank">📅 01:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67822">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67822" target="_blank">📅 01:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67821">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67821" target="_blank">📅 01:49 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
