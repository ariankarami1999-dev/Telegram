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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 22:22:48</div>
<hr>

<div class="tg-post" id="msg-67926">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8D00ijlgyxyRcSDswn21JO7vkgy4QVHV3zTfVgd9b9pnvIO51c39NdaoYybiHxEErr4-_0HeTR1CeUYS5BdDLMTJWYMjiBsMcj8ax5fWw_9dRLU5_eHTVW6Hp1O4_bIEQW3Rtvh2oyCbj2sQ7LyOxwDCIFMDZzdOgHbEZAiVbandkyvcKIYGAVWGFdPJh4IpMnBnYu8nOaiSvtcxHE9hsptOjgKdzJ9Rpik7s3sA3Qu8fttBNLyzg4yXNCNV9znCYJQHV6O9vcKDH-I8Mx4Lg5CAh4_yhvEAE_b0sWuch3fu9UeRy-5f9tuEUA2Ub09l7tlpefbudeliiswTv9lqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آکسیوس:
اندکی پس از تماس تلفنی با پرزیدنت ترامپ در شامگاه شنبه، سناتور فقید لیندزی گراهام در گفت‌وگو با فردی دیگر از وخامت حال خود خبر داد، اما گفت تصمیم دارد مراجعه به پزشک را تا صبح یکشنبه و پس از حضور برنامه‌ریزی‌شده‌اش در برنامه «Meet the Press» شبکه ان‌بی‌سی به تعویق بیندازد.
وقتی به او توصیه شد فوراً تحت مراقبت پزشکی قرار گیرد، گراهام با شوخی پاسخ داد: «الان نمی‌توانم بمیرم.
هنوز باید تحریم‌های روسیه را پیش ببرم، تکلیف رژیم جمهوری اسلامی را روشن کنم و روند عادی‌سازی روابط اسرائیل و عربستان را به سرانجام برسانم.»
سناتور فقید لیندزی گراهام تنها چند ساعت پس از این گفت‌وگو درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/news_hut/67926" target="_blank">📅 21:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67925">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67925" target="_blank">📅 20:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67924">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ: امشب به طرز ویران کننده ای به ایران ضربه می‌زنیم
👎
خبر بالا فیکه و ترامپ با هیچ رسانه‌ای چنین حرفی رو نزده
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67924" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67923">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
❌
وزارت دفاع کویت:
۳ پایگاه مرزی زمینی کویت هدف حمله قرار گرفت.
‌همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت هدف حملهٔ یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67923" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67922">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra87xl8jfzrkjyWJgdJiUe9DuyCGw3MzyYR9BxenGQuy1tD6fkvQwgTff4ffAljeCTecyvVL6rM58ynjoXSelTol6d70GJ0dlf5W9T41-ieh59XRVbA43OsKGB2IR7j6NdmTIfNutoV0Jm2RPxlpLRmnXPYkClMXAde40_9xHJ8NtGV3SjS-icjaEEZE26E3chIdWa4QlqBcUpmWSsQSQn-pEIYF6lj44KaVFS0NxAOI3bPWjbijcm0K_3CJQs6lNPr3As7furNBTWM25ONWOVv4fR1hGgtVzKVHwI87hKZ_czlfPeY3WwSCqwH0KMZMssfg9iqlxqOo-FcrkLDlZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
ارتش ایالات متحده چند حمله را علیه سامانه‌های موشکی و پدافند هوایی، و همچنین قایق‌های کوچک متعلق به سپاه پاسداران انقلاب اسلامی در چند نقطه در نزدیکی تنگه هرمز انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67922" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67921">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
فارس:
خبرهایی درباره کشته شدن 3 نظامی آمریکا در حملات موشکی به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67921" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67920">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
منابع خبری آمریکایی:
یک حادثه امنیتی بسیار جدی در یک پایگاه نظامی آمریکایی در کویت، پس از حمله ایران، رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67920" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67919">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
منابع امنیتی به نیویورک تایمز:
ارتش ایالات متحده، مجروحان جدی را در پی حملات اخیر ایران، به بیمارستان پایگاه رامشتاین در اروپا منتقل کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67919" target="_blank">📅 20:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67918">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8f7jEDwMbBc5Uc5CqnUEf2dLKS4neZAIynrdbP8qqrPDXqovQdre8xPiJPGkxCmcROyEwQ4UtVqypiTmCzf6brBUoy2dHFzYwaxshpuIc8SfFTJO_4TyJSLtFv3rzKIjYeuRVWORabOKk1ybxqBb5agFLBHDKGO5P9V0aXhKv5YwGsDvzUPUHt7Gyyy5tPDA4JwUewLH8VxYg2qDqbeh-K0_K1RF9KiUtX1oUucc7OIvx2ZLmNLrb1uKm7KG7f2qehyddaiG9KP73Ik9lGXJWTkhkrpKDepMESPCtOA1FDDRx5nPNwWvy50vGh-oj05Qdh4Y2-Qz5Du0AH-AftdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قشم همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67918" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67916">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67916" target="_blank">📅 19:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67915">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🇮🇷
نایا:
نیروی قدس سپاه پاسداران انقلاب اسلامی، کشتی‌ها و شناورهای آمریکایی را که در منطقه "کیلومتر ۲۰" در تنگه هرمز فعالیت دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67915" target="_blank">📅 19:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67914">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67914" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67913">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONzwFF1ViSZZ_22tcxLd_Hy_dmmXFP1AnU54XX4L2HLAgMFZgR9v77V4BOByttyfDVOlPHfVKU_iA5yIQ__v7jQ0iMIzf4q5fSFmg3vVh5b8GxTsCkv7ThqjFsMp7qus4RtHO3zjC1mylbmSwOFovbxMuQzQONn-_FljAFYMKbRZA0Kv8je_UfeWVTOTaFY3AcrqiBLGXI93mifQBWnUDv6YjWPJHuvoqE_YySugZCzqM_R5reUwkMP0IAdqVtBcuZ71tBaRWmimKnLJ_Kb7En8Jr5f8prYORBQeJvi2kf_OLJm8lNe_j3dTPqLRRYr2ycemh1arP9iLBBGeUjYc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تروری که روزنامه همشهری منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67913" target="_blank">📅 19:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67912">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67912" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67911">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
حمله موشکی ایران به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت.
گفته می‌شود این یگان در حمله دیشب به جنوب ایران حضور گسترده داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67911" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67910">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67910" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67909">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAHQHJve8eiPrwKc7YI1gtctGefso7dw2saA1BWC-JZqIy1a23SBFC7ZIxjWGRqwDN0YAAmNzq41jsnv0vBctwH2fa40_fWmefiQur3u8PiBUQ70XTa1XnGLKpSdxREeUOTSgl1akJ4YqLAGnD_TZ8kC_SqT_r19kqFW4KFmlKgzc5O-DBYc9F2Z4PQ5fUC4hj-YvrGWChHbtSpGs04f37emRecSVEXwYdMR8VV0c4cplOqCn7qGYumJi07fPFVCEAKke4SPLze8wKx_uaF921iKkAp0mc4kTE3Whnno2-ObT3bxZCjEPuH1SypCAplk_4J7KspSjvK4PGfFiPEl5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دو انفجار در کویت و برخواستن ستون دود
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67909" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67908">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67908" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67907">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67907" target="_blank">📅 18:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67906">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
یک فایل پنج‌ساعته از مکالمات بی‌سیم نیروهای سرکوب‌گر در اصفهان به ایران اینترنشنال رسیده که نشان می‌دهد نیروی انتظامی با مجوز استفاده از سلاح جنگی، در ۱۸ و ۱۹ دی‌ماه با کلاشنیکف و وینچستر به معترضان شلیک کردند.
دقایقی از مکالمات نیروهای انتظامی در بی‌سیم را در این ویدیو بشنوید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67906" target="_blank">📅 18:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67905">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=a1x8mazWJyboBGgjo4hu0wPJRrIFHLPqX6AOD8u8qSGG4EfQn4jZBEHxlZ-QpE_vImTUsoOuqdzot7A3ND1bTEWsNfUw-8ZOOkNdgxipKceCRb4FNjKan8_D_G-h9N_r12MXJfNcjuagjjhoJJ6LiOvPcn5x4Lxt4ZpkC0dX8eWF801vdWON07p6zsXREswz3Jz5iSY5tUqe1gZimMRDbCwEEHMHe-L4Bm6qtl5WJr31_jMusAOfSoZ4CMlpd4JT2FrSnm68AiWs7DfZ-AY4tFVZFiGhn2Lliu0kxD_mgCARbdIS9M4H1UgzHr9xsl9973ziAD-DnnJeJMtBAk0HDKkHuGVrXXCT1bflBK5I3JtXoBzfvBwh7YsA2ylzJj3ZJ4gaeXQAcb_UDgEyg4USx8bR1hpJmtzegIW1tywZK-Amg7nbA1ulLyENwHVPtsnfAgciBSUwsEnVYqezALM5oWGkLOVNyYhKGJaF6hvMf4olGlBRIar9irlGTPLyqOHqtVFrHvm9i-bD3P0ZzrM2vth5TIOn5SBmsCaQNC2sJEaeebWLGl1TB_Q2Nx3r9dWu9k_98JDiV3bvKF0i_ccFQJ4_PzEx-qSHL0UNGYeyTqJNPh-DbDZRv-KGDPmWzkXAFQc8OKoS4d5DQbvybwR-yicAJX_qKeFzfg0jVRQvoGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=a1x8mazWJyboBGgjo4hu0wPJRrIFHLPqX6AOD8u8qSGG4EfQn4jZBEHxlZ-QpE_vImTUsoOuqdzot7A3ND1bTEWsNfUw-8ZOOkNdgxipKceCRb4FNjKan8_D_G-h9N_r12MXJfNcjuagjjhoJJ6LiOvPcn5x4Lxt4ZpkC0dX8eWF801vdWON07p6zsXREswz3Jz5iSY5tUqe1gZimMRDbCwEEHMHe-L4Bm6qtl5WJr31_jMusAOfSoZ4CMlpd4JT2FrSnm68AiWs7DfZ-AY4tFVZFiGhn2Lliu0kxD_mgCARbdIS9M4H1UgzHr9xsl9973ziAD-DnnJeJMtBAk0HDKkHuGVrXXCT1bflBK5I3JtXoBzfvBwh7YsA2ylzJj3ZJ4gaeXQAcb_UDgEyg4USx8bR1hpJmtzegIW1tywZK-Amg7nbA1ulLyENwHVPtsnfAgciBSUwsEnVYqezALM5oWGkLOVNyYhKGJaF6hvMf4olGlBRIar9irlGTPLyqOHqtVFrHvm9i-bD3P0ZzrM2vth5TIOn5SBmsCaQNC2sJEaeebWLGl1TB_Q2Nx3r9dWu9k_98JDiV3bvKF0i_ccFQJ4_PzEx-qSHL0UNGYeyTqJNPh-DbDZRv-KGDPmWzkXAFQc8OKoS4d5DQbvybwR-yicAJX_qKeFzfg0jVRQvoGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از  فعالیت موشک‌های رهگیر پاتریوت بر علیه موشک‌های ایرانی در پایگاه موفق السلطی اردن از دید سرباز آمریکایی طی درگیری‌های روز‌های اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67905" target="_blank">📅 17:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67904">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67904" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67903">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndbcxU60nI8CBPbLXgEQBCAF5VNjuR3CyPaJeRvDZ1NZLd9NGeGf4iSQW3JYAlluR5UpEQcMmKy0b2GjJAW7mCzHQ31lgxxTUv7n8L1E54KJbI_SHwXnc6w-zDMafL8eUxcBwJZB_Z7tI5PJKjpsYs0CljviExulO5otswKybpumP8V6cnls6o6mnT4sBWPdaZ2OYW8AfDgs9poAMVvl8VHfoqn4RTIBwNH_Qca6yFRbzK7Ih4maHOfj9NWv-j8m-5d5walOA3R7qsOvHhTiE4vMnm33fSE9kZXl11i1xzjR4iIc5WVL2FHOn2vO8mLbJsE0esxn1ZyyBWLzeylp8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمامی کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای آمریکایی در این منطقه مستقر هستند و آماده‌اند تا از آزادی تردد دریایی اطمینان حاصل کنند، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران. ایران کنترل این تنگه را بر عهده ندارد. ترددها به روال عادی خود ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67903" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67901">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4gNnwB55gpt1LDWyCTh57QBLAm3D6HFfzUDZKu_nhbrO0yBPUb-0ieVa1FybxHlz25srHRfPnqIKSshppvBNn3rakBJgiUQ8xe75VvPiACXxlnZ-jK34y392qmHe-FRvkHmM0gY8ErgsaCvZm6_QT11Y4bH4KYorfaG0pIqWu0NEK38mbt94FnZ1FFg4mlA33guHx_QmJVG1RlMx5483yDo-rRdSdxK2E1og60-68eTUy1eqZwvAAAUtVWjqZnwFxhfCYGHwF5djU6BTfLAvRBoZP6lLLsZL6VVzwNrrHGm5iX1-LaIQrqy8GrRGyi7T8AQUU7eI538GtXFwiLmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=VLS7pxFx3gFXwXFnxrSKTqtbxCkvyNCg_zpXHthfjf-VF_LOQt6XMnH1qbsQszI3KEz1NdpekMflwT_9-LsSG3bWrRMn8YmB5GYPCW2-dbkm4uTvOb7lulcYMjnsPpu4O0J3IeO0X7_jUmfTOl2O31iLRmbp2MBHoP8mHE39YtxnscjN3Lqabe5zZ7BN979DtZWlT4dBtZIGwSQKT_GnDPxLEtla4LI5MyGA5lnFvLQ5DWqAHBEalHtKGuV_9Ikm-dp0TlRuhklyJEimtlZ-x8bk__bJd4TLGX23TDRNhdCiLDiBUtUH0pgVYlRorEScJN4-nv0Y-PnnKp9_tBNNOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=VLS7pxFx3gFXwXFnxrSKTqtbxCkvyNCg_zpXHthfjf-VF_LOQt6XMnH1qbsQszI3KEz1NdpekMflwT_9-LsSG3bWrRMn8YmB5GYPCW2-dbkm4uTvOb7lulcYMjnsPpu4O0J3IeO0X7_jUmfTOl2O31iLRmbp2MBHoP8mHE39YtxnscjN3Lqabe5zZ7BN979DtZWlT4dBtZIGwSQKT_GnDPxLEtla4LI5MyGA5lnFvLQ5DWqAHBEalHtKGuV_9Ikm-dp0TlRuhklyJEimtlZ-x8bk__bJd4TLGX23TDRNhdCiLDiBUtUH0pgVYlRorEScJN4-nv0Y-PnnKp9_tBNNOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از اینکه صداسیما رسما مرگ لیندزی گراهام رو تبریک گفت
فیلم تبریکش بشدت در رسانه های جهانی وایرال شده و گویا برخی دنبال ربط دادن مرگش به جمهوری اسلامی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67901" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67900">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFdw40W9grpatxFeJ7v_7Wm4wGAld8aIG6kV-8KWs1a2BJpaUqK_YS78QTRkmB9esGrCVTJDioEQNDivKj5urfomolVVx8LG3MEPq0dMlVL0JjriegcWL6uWnp1xJnvUChuKd5Ag6nlnI35unLcw5tGyRFmSZ1NbFhBqs8KkAk6AkY0Ffe_7d4N5I6YOH_P13-5dm0wuy56nMAyTFeh0bDErsvALsMXvaGwR60k0Ci2YzMeBHiYwkrSe8l6V87Cl9I9SgP7pTyvox3fq-aNx9USMIRR20VsbzO0AhGRrAOSyI7FPsunkjhPb_JK1fqbmKzODWLw-UTQBabT4PnpIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پس از شلیک چندین موشک بالستیک به کشور قطر در طول شب گذشته، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، ضمن ابراز همدردی صمیمانه، به خانواده و مردم قطر تسلیت گفت و مراتب تسلیت خود را به مناسبت درگذشت امیر سابق قطر اعلام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67900" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67899">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=GMCwGxjrgq6zqFKoGoeA-rk8LgEUrL8oqPwpi4NKYEWuxLp1k8w7Q0rpyCqHkVPjQVq-JjvEvErT_nWwcJ7XcbwRUXKL47PKUyk3jq249-5APCLpRLClVCbmP4V3rRH180IdmJuhHNq0ghE6k58r-pcvy86muhNSVk1nlCG_hTl7v7PfAWppQtWFUKSDfABC-6xXWnucl5fE3hCdKT0ZwFzAtYAY_8oS7EZpGk68Km9BMJK8Vx28Y6bEvyGr6eQ-IM4Ows5-3TNkY-BnTG75TujM53Es1lZXrH1iSKW6fhmqtsdmJhHfh3TgYbC6Fqjj2KnEvlFkp8YgdE785wCbCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=GMCwGxjrgq6zqFKoGoeA-rk8LgEUrL8oqPwpi4NKYEWuxLp1k8w7Q0rpyCqHkVPjQVq-JjvEvErT_nWwcJ7XcbwRUXKL47PKUyk3jq249-5APCLpRLClVCbmP4V3rRH180IdmJuhHNq0ghE6k58r-pcvy86muhNSVk1nlCG_hTl7v7PfAWppQtWFUKSDfABC-6xXWnucl5fE3hCdKT0ZwFzAtYAY_8oS7EZpGk68Km9BMJK8Vx28Y6bEvyGr6eQ-IM4Ows5-3TNkY-BnTG75TujM53Es1lZXrH1iSKW6fhmqtsdmJhHfh3TgYbC6Fqjj2KnEvlFkp8YgdE785wCbCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش ممد سامتینگ در حالی که تندرو ها دارن شعار
«مذاکره با دشمن خیانت است به میهن»
میدن در مراسم چالسپاری خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67899" target="_blank">📅 14:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67898">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67898" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67897">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz_tEmJrM4EVo9DF7-oi5wLwtCUNJWnQZGLRuuTamFye2-SQTkvFyVmQXbqBFXKG-Skyb1e-FisVkeAtiLHeGB08wxH_reJXggsm6yKdCZ8DQB_SY-B9l8K1W0DRP5ClBfKqzPvkiHtRM3LTQKfv4F7p1hVJGcT15pBE7TRDu4V-vvYB3e_vZNeFeAFh_x8AqZ1ZBRLdEPBdnwinOAIldTzZUysv4BUzv0vrUFajfg75HxGTYjAXjoHy41S3O4WQKdGeT6m5ap8WwXztfHnrQ5rYlesth5p5fbppLMp34digrmDW6PqVHPLCx7OZxrJr9oWvN4asjRNJwAYhv0XYYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمیدرضا دهقان از اعضای پدافند ارتش در منطقه جاسک طی حمله بامداد امروز ارتش امریکا کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67897" target="_blank">📅 12:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67896">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiQQ-YAP6UB4EyZnfwG_3yNMP3pZGRIa--M0aPx-qqngqquM6MYS-6GA8lJpJ1jMisAfZqE6lVtro8Woh0neHLoS6X5uMlxsDSuWja1yRH7IzpDVyr_4rntTEe3zrpZ9tsNxUSnWtArXZ2zH4n-YUK-Z5BlxEmyUfotrKNS2Sgttt0b9aSvpJd1zxUb3iluQWcMyMXa8uqH8WqhHyebYp3A13txv2UUV7BqFAW_P9c6QsNO08E4hpymLdHEsq-hGft1phaosy6R1vnEXFLWseQRJS_MAmldmfNDLs38ozwWDeYP3FlE01YXfTpIBjBYtlPiA3nUcfa73TbVsNWHAKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
واکنش مرندی عضو تیم مذاکره کننده به درگذشت سناتور لیندسی گراهام:
چقدر بد؛ من میخواستم او قبل از رفتن به جهنم قیمت بازار نفت را ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67896" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67895">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67895" target="_blank">📅 11:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67894">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma18DjJOCKG34x4lB66MZObQZ5KjHC2YrZr2lOZoIUFc4G13z8xftkLJ1WmtbtOgMhwhZMe_JHTIJKm3V_XsLtq0jHkF7IMBhNwQSbgezegbqZtuRWLP7G-f4gcimI4ewcDrUKbAU-CaalZ3JMgxg5ZFqXuj2gdJU01RaYTqJyCry911zc3xbc1sfyPfe9-O5nufnpk5_ATQoqYrKj8ZW0VUbpY9ijDWGwzH11p1szvKgH9rTlT4ZgRSw_BccvPPtGVo2eBZPLsxO5GcIiIPhIQ_N6C_R5mCRecJrEgBMs_pFE_fQHbEIbXDEvOWl1g6VBiSCbOlXhrYtuKW03hIqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67894" target="_blank">📅 11:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67893">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrCb1Z2wzKobisQ2qnNb17wiiikHwiPnnQUIGwJb2UACnePrf3ktYCP_OMSHauumlGmiZtybx2Zlh1IrxVDGeEr-vahqh-m63KDutmy0X5QGmgdzEQJ7SgCYQoVPgB_1d7ly2zUlfeKtKscf3zaCVgQbEBLJtvvpUEXdt-Y6rqyt5fBObTFa8RtX_lIrprMfLwoj42q-xLYIF_OpmFaLKqEbk_twdRZu4rfyCQV2cOcnyCzQUXAzOKBrvdp5Hcw6t8uDhTlO8mumMEtDAVjBLVu8EMBG1sOHSQ7VNF7dXLwrNUV2YjJgwateiOdHyfzsJEuMLlt8LX5Daz-gXcw5HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
سناتور لیندی گراهام، یکی از بزرگترین شخصیت‌ها و سناتورهایی که تا به حال می‌شناختم، از دنیا رفت. او همیشه فعال بود و یک آمریکایی واقعی بود. ما لیندی را بسیار دلتنگ خواهیم شد. جزئیات و برنامه‌های مراسم تشییع پیکر او متعاقباً اعلام خواهد شد. چه خبر غم‌انگیزی!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67893" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67892">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2UGqr5l-L1VCQ7SA10gfzW6yyHEXcP9bbCg6O7dZtKPZSQV98rERi9cIPW8go5Mf3gLNQbRgrnZBTvQ9YfiyYcWQuZDGGd3PmBkIcvVDGGmH3nEbXTOrPVQxbFkTZVOtjAiFF4HeajpA02EA8QPqFiSkV46IbiPJsZNXCefeEtaCvyRdmb9qERNgVjg30-U0baTLvPxh2b55SUyJCMpUrgz3Xg0fFc6CQOkBc3SpPNRPTQUb3Bry85g5gDj_WndWgmM01TgKrgjuMRZJrLT2vB6P9zM3O2EOq7U49AagiGs7BMGf-PECQ3-NyUTODh0AWOxt-jQwapEBFxbQpj2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ان‌بی‌سی‌ نیوز:
در حال بررسی صدای ضبط شده از بی‌سیم پلیس مربوط به واکنش نیروهای امدادی به یک مورد ایست قلبی در خانه لیندسی گراهام است.
این شبکه همچنین گزارش می‌دهد که عکس‌هایی از شخصی دریافت کرده است که به احتمال زیاد لیندسی گراهام است و او را روی برانکارد از خانه خارج میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67892" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67891">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6xhRBe20zYIB4PlWIcI00p5hICxUMclE94qHXkWcti2JM6o2XGItxciWIOEid5yJdp0e-KiVX8sEZFUss-uF4WD6h3-nx7tiL_TEku-ZePndEFCvaUm2T5M1gkJiIcSrBs4LDNsZM8h8j0IETQ0WgGtu1PjxIb15G1zGOZ7NQXo8ogxztKw5ivAAjbLglw0G-QExTVdPP07w6bEnYhvS8Bw-xL3Cra_qBlEaXgVWVNoqUbHR-Sf3qnVN1pyyafc9UgvWc2ymEmC8VN1u-sTRwHopkL-03-JsLlxJZVhEPf7rLJ9eJh5n2LFQr3GnZRvVmcugKdXf6pbxVKpxzdjMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RIP, great man
🫡
🖤
#hjAly‌</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67891" target="_blank">📅 10:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67890">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-WEiLcOpRsotnU3R-zPsVpZayKysFhdJSIZO2UAuu61kcXANucfBJa5ps-hNIoTHGA9t5NUuHTpj1hZGnEvy0gHgnSL9qvbJSj2TLmDfqIERKtV_zUL-0_NQEMqkzaSjX7LO1jvhU7Txmgk6wdkck1Wd5F59hkD0bkCNqJ20Bnpjv8Wu7DefDphJa6ZTOWFLjxKrOnw8thJtr5jdvW94oJlIAEAHsHzCMNK6SvliIyNXsqlKWgh5WZvkBTi6oW8y4hbGAGKUHPeI29zlKnKYF_LiW60VwmEo4P9w3e-tiFtJIAAc5eSaNtPNTxuaQLybeneSmHBz_YrW_WQdu8GnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:   دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت.  @News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67890" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67889">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcBudbR_g2yHJkiLPzTocbOIkzSLePFzMMWfpZ-wpixOoDNcGmFRYRE6cIb0WaHR_n4xKsff68lYqQBd4pfMJ2YQ3WWpsG-oAJYBOHAIglBb46JjPbPjGdCUKvuwXv3NANMxWZScSPAxl4OrLaFELCCSbjSQe35VIl4Csla5BUrP2VUlvmVj3zELob3pS321cMsa78O0-r9tRzNZ9r-nQGm3EbBhGj253UvTB6SMeiIx08ilxYAkQYCnV4PycIFYczZzSwufaGuhjOF0Z9f4CkBxrEGl-gNgTnK_lmxwwETKxmnhVXQ1QKfm7Q7ptctAEtyhxvVcEAvaWLRR6WrYiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:
دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67889" target="_blank">📅 09:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67887">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCzeExb0dbG4kOvqN7XrotTAY4fXZuStjjSgOOy0b9zbgQRTvyZjAxOXZQActr-U_AWAi1DQ9FK1mQBDraVHr6UPXGvOEYozXU4nckSDg0pWBa94akuRFRph0BpZvJxZItYZDIWFSiIv5QzWhNu_64Cp0-oU1oqN10nUaeN7FvyQSMcyfhVcZyIOX93eCqI2LL4E1pwfmuuAJSnsm5yHyi9vgLBSaIRcrSdiGn8beaYLaetveLdcFr09xFFaRj79jyLM4RtwPtoZ82K3GhxwzAqu9j7A5Gan_4a5OUFBIhPz-XWZaGpE7RmTtvzNEUCabNYFvQxraZ9stOmbngQvVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#فوری
؛
لیندسی گراهام سناتور جمهوری‌خواه آمریکایی و از حامیان انقلاب شیر و خورشید درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67887" target="_blank">📅 09:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67886">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
تصاویری که سپاه از حمله به پایگاه های آمریکایی در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67886" target="_blank">📅 09:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67885">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=OjJHnLSZwSl0RGLwR2JyJQmtkJQEQiH1bSgAWiwTfHa_encwK3-WcgAdC71E1iMV3HITBcq0jDHoD5RrnmSt63iK1vTWggTzzwYXlM9nwy7fj6YPTuiLGeOVteITPjUNLfouzBtWZGh-r-nOP2lUpz2Q8PBbZplFVGECq8lj2mpZMDB2bFwM-bdmhsAzMdpOOj_XQuqrlLCOzinSA3_BVLFp8HDUMezVaMw2eMMv04hMwgcFs4VtVTsapGM4iOTUO-vrFgsAAcpWGTLxBz7_XDrunBA2grg76aFpWc58kZMUFbz4MXdx_XwN06yeqLNk3GXdl-_VGgpoUFxsaukIrYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=OjJHnLSZwSl0RGLwR2JyJQmtkJQEQiH1bSgAWiwTfHa_encwK3-WcgAdC71E1iMV3HITBcq0jDHoD5RrnmSt63iK1vTWggTzzwYXlM9nwy7fj6YPTuiLGeOVteITPjUNLfouzBtWZGh-r-nOP2lUpz2Q8PBbZplFVGECq8lj2mpZMDB2bFwM-bdmhsAzMdpOOj_XQuqrlLCOzinSA3_BVLFp8HDUMezVaMw2eMMv04hMwgcFs4VtVTsapGM4iOTUO-vrFgsAAcpWGTLxBz7_XDrunBA2grg76aFpWc58kZMUFbz4MXdx_XwN06yeqLNk3GXdl-_VGgpoUFxsaukIrYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرباز روس خودشو به موش مردگی زده تا کوادکوپتر اوکراینی شکارش نکنه
اپراتور اوکراینی میگه: «نگاه کن لعنتی طوری نقش بازی میکنه که دی کاپریو جلوش کم میاره»
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67885" target="_blank">📅 09:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67884">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCbDRSr1zuXQYH55hXF7Q4nsR1qVZGyDgPSI1YW7XxGc6NOR2AJqqrlfj8xHcKv03zYZn6awqtgMo1dbnuUDlFBTWBTbGqAuZOGk_1LL1ZCy5v-RrTXP0c3LeKRDki1z6IV316nsEBp0zzFUPjWieVUWZo84YXfl4HJvOqTOzVhQPV6mq9GBworA1yQ8Ibrcp_miE88Z2nJet5pVqv6dSnBjZd2kvok2-CzPDZLkuPv1oh3dQEcyJ7v2CvaaSg-CZ1W4bEyQlrlAT1_AT9nAm8cjmxz0XgRXJoc-B7MUaIA6V7RfzX8uDqwAYYgq--L3F8x91D0HFnJ69cFa2Br7HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قاليباف: دوران معاملات یک‌طرفه به پایان رسیده است. به شما گفته‌ایم: به قول خود پایبند باشید، یا عواقب آن را بپذیرید. واقعیت در حال نزدیک شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67884" target="_blank">📅 07:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67883">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=e-qfgEUlvSpmGls59OvVnOW-sZ4SNCxp2tDjrS47eFc7Oamct5vq-8KJFf4iY5LYBY_626S5XwtDOjc-88Dctn_YuzP-bRaqMx3jL7kZivfn1_THrn9XMEvxYhzsU1zKT0bQuTlQbdVOen8uXEHQSgd6awi5IAO-oInBkKmjpv4CmrO2sKA0DcW9LngZosCQb2jU4VoIOqNoYFzIJ7f-QrjZ7GVz7J8EapyPb8uuY7FqWBniLlFZQLkA6270Nb9Ndr122o97TxS7GUCPDKx7oq7EbuPn5Y_OhVkLQiNMHEHEb4WtjZj6EOagQhExL5EDNvlCyfJUX2SL6HjgzLA_Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=e-qfgEUlvSpmGls59OvVnOW-sZ4SNCxp2tDjrS47eFc7Oamct5vq-8KJFf4iY5LYBY_626S5XwtDOjc-88Dctn_YuzP-bRaqMx3jL7kZivfn1_THrn9XMEvxYhzsU1zKT0bQuTlQbdVOen8uXEHQSgd6awi5IAO-oInBkKmjpv4CmrO2sKA0DcW9LngZosCQb2jU4VoIOqNoYFzIJ7f-QrjZ7GVz7J8EapyPb8uuY7FqWBniLlFZQLkA6270Nb9Ndr122o97TxS7GUCPDKx7oq7EbuPn5Y_OhVkLQiNMHEHEb4WtjZj6EOagQhExL5EDNvlCyfJUX2SL6HjgzLA_Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ادامه حملات سپاه به کشور قطر
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67883" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67882">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه مدعی شد: مراکز لجستیکی که به کشتی‌ها و سکوهای سوخت‌رسانی متعلق به ایالات متحده در بندر الدقم در عمان خدمات‌رسانی می‌کردند، در یک حمله شدید و غافلگیرانه منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67882" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67880">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=a-HGv9F2DTHMUIvoF9-LemDB8WjFa1tpVcAtBszcgr3tWOq9r6JJL_R-Gd_DJd5Em3SjZmjG_aESwTbAV3LmQrQCETix5ek2RLOVXt8rjIsXPgfPURtxqpzoUL4ldren-q1KN5iTjDMOnTu0P2V_nDHJ5YxiHuURlWMch-KxaGySWPdPWnfz9ByEMBLuT5BzYHQh3PRUruznx40j0QnzCcyyoJHvkSs6bSJ2FYMcdUYxiONkkBrKchqy_NOmIy5lhwHLJ379TsRUOzD02iYUtPkhckkVrgJSFyoUyyeZq_bY99l4A18Ua7_6nDwmpV_859w0w19K-Anc7E8W1XvKRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=a-HGv9F2DTHMUIvoF9-LemDB8WjFa1tpVcAtBszcgr3tWOq9r6JJL_R-Gd_DJd5Em3SjZmjG_aESwTbAV3LmQrQCETix5ek2RLOVXt8rjIsXPgfPURtxqpzoUL4ldren-q1KN5iTjDMOnTu0P2V_nDHJ5YxiHuURlWMch-KxaGySWPdPWnfz9ByEMBLuT5BzYHQh3PRUruznx40j0QnzCcyyoJHvkSs6bSJ2FYMcdUYxiONkkBrKchqy_NOmIy5lhwHLJ379TsRUOzD02iYUtPkhckkVrgJSFyoUyyeZq_bY99l4A18Ua7_6nDwmpV_859w0w19K-Anc7E8W1XvKRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
تقابل سامانه پاتریوت در قطر با موشک‌های شلیک شده سپاه پاسداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67880" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67879">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سوپرگل تماشایی خولیان آلوارز مقابل سوئیس</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67879" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67878">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران مدعی شلیک و نابود کردن یک کشتی تجاری دیگر در آب‌های خلیج‌فارس شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67878" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67877">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67877" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67876">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=lCXh30yhdCGtfbk_UPXIFb-3i0krHLxgz2q-CN1UPTjjNDwUtBHW5QhxzYDgm4B9f3K9pTYEPtbtXoQ_xC-xj7d9RL8zb9wtQyP2hCCn4SJ3fAyPxYf_yG4c930r-o5l9H2ticBYnk8qmKFM19vj8ok5qPK0-MHyPbU2fg5he9vwNS4vonYo8h--h3MqZduCSIe7qeWU4SPqxiurU9n9mLUvS1JCipmsxrq792y87gUo6Wl8kVtR5b1GRWz64gVnEAv4QRYVUJtU8-3HXX7stm845fQW2j8OVkIjd4l9j4xQfVT4qhwsUj-96UbHDQofewbCcXoiXK4H3H28vKBnZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=lCXh30yhdCGtfbk_UPXIFb-3i0krHLxgz2q-CN1UPTjjNDwUtBHW5QhxzYDgm4B9f3K9pTYEPtbtXoQ_xC-xj7d9RL8zb9wtQyP2hCCn4SJ3fAyPxYf_yG4c930r-o5l9H2ticBYnk8qmKFM19vj8ok5qPK0-MHyPbU2fg5he9vwNS4vonYo8h--h3MqZduCSIe7qeWU4SPqxiurU9n9mLUvS1JCipmsxrq792y87gUo6Wl8kVtR5b1GRWz64gVnEAv4QRYVUJtU8-3HXX7stm845fQW2j8OVkIjd4l9j4xQfVT4qhwsUj-96UbHDQofewbCcXoiXK4H3H28vKBnZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سپاه به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67876" target="_blank">📅 06:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67875">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67875" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67874">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFgcQn6inIWjVQmGjUnR3HDVIPVFofYhynf_AHJyJ5iRGf1Oq2BYz36Helpl4FKOVNIazIACi0SyDnivBF3c8oFpFcQ8t1Z12DQkrQpYetpxk2qygepQRehcnj1U6HInbrX2xUCSf6Y1jxI2kTHwKnT2RfpWJkThrdcUeiQqQPTTeKCirx-K-5ddjNPBg5r4OrEjyNRsa720Y_p3RQzfl1UfddE4USApRDx4u143wimLLm6ovevfa0fiUsDogB0WY2bPIj5-50kMGGEyjn85_cst1I7LhrhNEmfydoV7vQIYoy6yPmY8KAWN4EEWxK7vFuE-9SYtVKDA4Stu0e-92Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67874" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeW55h76epjI-FWM8AYtIzAjcvi6kICvffYTMOfycbX3rqTaGFwadVibiCOQ8flYaRTjcSZKfOBxLd9E8ZXFSimyvPQAkwv-xEhNPVwmycpkGrizllQKYGCHLxbgpUey8iLQAwZEgbqydLjyZG9GeQrF3jTNSvtEpUKQyBs373v2NJGBxEu7flfRptA_RMSkJRXLScie2L-M6bdkXEY45PUC97rIFNWA4thFfkyOOjlLei3HnK9cZVq3hBbhXqPwvxfNVnrojB-9zfkMgvySiuKwtMYANJ2-Ix-TJEbvKo4c_7Zoz65DfBx6hZN0KIX8wv_VHyb1uk6YSGnpeeieVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/news_hut/67873" target="_blank">📅 04:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67872">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نتانیاهو: تو جام جهانی طرفدار آرژانتیم،</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67872" target="_blank">📅 04:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67871">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپمپ بنزین</strong></div>
<div class="tg-text">ما که منتظریم اقا
❤️</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67871" target="_blank">📅 03:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67870">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67870" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67869">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67869" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67868">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
هرگونه خبری مبنی به حمله به تهران یا فعال شدن پدافند تهران کاملا فیکه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67868" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67867">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گروهمونو که دارین؟
😴
https://t.me/+5NElXlQWt_05OTlk</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67867" target="_blank">📅 03:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67866">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=DkcaTeAHyXzPDyGa4jcI-mIA6NtNplMzBI2fxNTwgfEi8s7zx_j7_x3-vsUn_a5VYutP2OWMbIKdjzMFWDBKGLe38xiA4n_Iu1CcdhP5FJn3JJ_uiU5c_XPNJtPux0Ke8_960WbsgvVRwbCQ9CLqyVhDLNUbeLI6TUXZrkLrSFjTGcLQGOoHwWUvXfF_CLRTQ7X4pGmYXpoIyuK4T_UtzkXg75H75CnYScyTPQnQjd8TOZ2Qazze-i3ttIsvjvoL7XN9NihZNdKDhSZjLT8CTKyuUbdm_zfhFXRLB_DCIXEpuu6fhQwVA3GZWYC3FqFDJvj9MtETygwHhIe9xJl2cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=DkcaTeAHyXzPDyGa4jcI-mIA6NtNplMzBI2fxNTwgfEi8s7zx_j7_x3-vsUn_a5VYutP2OWMbIKdjzMFWDBKGLe38xiA4n_Iu1CcdhP5FJn3JJ_uiU5c_XPNJtPux0Ke8_960WbsgvVRwbCQ9CLqyVhDLNUbeLI6TUXZrkLrSFjTGcLQGOoHwWUvXfF_CLRTQ7X4pGmYXpoIyuK4T_UtzkXg75H75CnYScyTPQnQjd8TOZ2Qazze-i3ttIsvjvoL7XN9NihZNdKDhSZjLT8CTKyuUbdm_zfhFXRLB_DCIXEpuu6fhQwVA3GZWYC3FqFDJvj9MtETygwHhIe9xJl2cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی  جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67866" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRazis</strong></div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی
جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67865" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67864">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67864" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67863">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝒕𝒆𝒏𝒂</strong></div>
<div class="tg-text">آخرین باری که کل کشور باهم دینی خوندیم رئیس جمهور مملکتو خرس خورد
امسالم که اینجوری شد
فکرکنم سال دیگه انقلاب شه
😂</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67863" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67862">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y97S6YA9j9v7ADMWbMdF2wBCSiKzfuq2NC-iku4P9giGKq6xTuARgIz3ulHE1xD92Tzx9S2mwBpkvKCnpfIB45w59EHItZthIAM886UGIAOHVX7KpValcT5KiTiPSpt6jAfOR7odyg4-HzKSIOL7gUNAZNHyteezOc6EHbdcPKCEHctzaQMnXJC1LCUqRDIXF_nvSxMFKX5wHdhbI1guKDBZuyytPXvp8DxtWjlIwgw470ilumiQuAf5aKDVrJu0tQzK4R88Fr-tsiJsLU-PGmDgSJ4ihf5vE2DoqXLAWd2Cj7aY0-vDonELfdCtq_PP49ozuViTPECD36Fc2KBESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقیش اینه به تعویق بیفته حداقلِ حداقل تو جنوب کشور، ولی اینطور کل سیستم امتحانات نهایی بهم می‌ریزه و باید بخش هاییش داخلی بشه، و البته با این مسئولایی که ما داریم چنین چیزی بعیده #hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67862" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67861">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbXvxdVr00D4vwOfFT1_stIvbGlV5P9g_UR8bpzWCd0PUAB5zLwt_n7GOOE9cg8zqDYbZ3INnkPxyu9lDm96inlQsuzVAByaH-ap5GZHrhVqzFzXOq6JcoI0dKZ5liEzOWqb_ERtx8SxlIPRD2_aMfulEoOVFDwUxVFg-kv9qXxaRhnsjleMkuhAAwZtSMmSTCvG8AcIc5RDVlbtDF-7POIBpqeAV51w2NiepwkxvMvCbR3jV05wiEkwDDpTn-ScJbPPQ1tDQnjFHDpQc7LMZ27yneCfPi0lKv97uCXR9yrFPVoYp8RiDMc2OLbu8NK1XuvE0XIw6xJUjL6eSAlS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه #hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67861" target="_blank">📅 03:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67860">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sy0KR2HPLidl1rj5b_T76ShJcVXX5q8s1KEs8DfA3tz7wbPGaxMYPaVN6L0ixiF330ZfMBR5CzddGAruDUOR1hqdgxf-StgLRpEYZtzuE0K-CYdnSgna9Vh8t1DmbG0dyavARYW3QHjj0mOgxBkQ9dH77_5d5gfrBJzrPRBYN2qvaPg-hOTmorCmna7OxUbrK8YzkbA-AtLV-1XVxYYta0oiGQ68nNZznmBd3EYChyq63ISDa_-afmZKPXwUZd6kOlcSDhNJqjYSNmVPhRFkDLw4ITSvjJEcfx64qVgZR9wmqiUK3g0_skNX-XLRU1xxwe7W8IkocBVSIQj0KqBkbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67860" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67859">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNh4ahlsXn8bQ1nNloeBm1In0Q1LKb0e7j57ON27Zug-Xfox-LGTODQpGVsDnOCy9BiUeXlrxo6tV6gdXyFFepsQAb8TTzHH64h12aki7VFFkm6dayttryyAPRkoULfU_cvNnyrf6eUT5juAMUbf3qq0lGdzuCeq7VPcZpMiAhhd3NhnaPEb4CqXYVq9n_fe0xdlveowQth1DrAKd80rZfP34fmO2sM_60t7ws7sMU79KQ06qIt3abEGzYC6AuzFdL1dYkXqDP5yRw7n2nQC9gSG_iyEixLzGX3bRL8C8qof8T6FtcuI8-EzGauNN5Q7-jmehrGLAoo3iWv6jlMQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:  ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.  @News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67859" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67858">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
نایا:
دو انفجاری که در جزیره قشم شنیده شد، نتیجه درگیری‌هایی در آب‌های خلیج فارس بود.
نیروی دریایی سپاه پاسداران انقلاب اسلامی و ارتش ایران با ناوهای جنگی آمریکایی درگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67858" target="_blank">📅 03:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67857">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
دو انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67857" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67856">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=lPaIgYlJV_u2WhxUp19EjlZFEr6w6qOcqICzDwMsOrkoZ6u02j671nJNz3umHUc2L7CP1Dci9Mzwvl0uomMpwCVp2mlmzwlzNJ3We7fxzkPB9g_bwinDF3WOxbRjzq2u2tZTmqAruSXKpo-oSAL0k-jUnDK45jo9BYkd8uPhMljyhLXa1pfs5T-0FBzFGLGSm1yOjcstfmCDgr1STAD9Nh51opEE-hIp0BlnnBwlfnHJ9_MbgItoN5uHIgJHAvHilpMwlL-MFM00KGqjYJRyOlGSeQdAvVyhbJMwsy_dqOw4d0mwOrTlpJYwsmrBN5GBRSUqr59NLifZseTZXESRTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=lPaIgYlJV_u2WhxUp19EjlZFEr6w6qOcqICzDwMsOrkoZ6u02j671nJNz3umHUc2L7CP1Dci9Mzwvl0uomMpwCVp2mlmzwlzNJ3We7fxzkPB9g_bwinDF3WOxbRjzq2u2tZTmqAruSXKpo-oSAL0k-jUnDK45jo9BYkd8uPhMljyhLXa1pfs5T-0FBzFGLGSm1yOjcstfmCDgr1STAD9Nh51opEE-hIp0BlnnBwlfnHJ9_MbgItoN5uHIgJHAvHilpMwlL-MFM00KGqjYJRyOlGSeQdAvVyhbJMwsy_dqOw4d0mwOrTlpJYwsmrBN5GBRSUqr59NLifZseTZXESRTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فارس:
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67856" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67855">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صدا و سیما در عسلویه: صدای ۴ انفجار در این منطقه شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67855" target="_blank">📅 03:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67854">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
چابهار رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67854" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67853">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
❌
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67853" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67852">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKmVYdkUsiaXxLgmIBYPugv0swFwsCpU52EbjOyB4sF6ZK5weB1MqedjCa4g07M0kcHDFUONei3Ylz0L0W7ySJd3SJwTlKE-v6HWHjjaXHjdGd363EDT3AMsYW9jHBukk-DxvEuIQ6oPmdUsbvXL1_UvmG0L1x102XD1hL0Poeps06kLLs0Uq7iHi5IwJXf_4U-AexXP5YGvGFWBXYGFwRVomeewUcvn1eLvr68WcZ_QfvUWPutnvYRG-CKzoO9kHP6e3N4Ywnkq6dvOaXMSKJ1gX6nIkrGdnbB48gIbbUkR8QMIrmgD8U9g6lOxKYo1Xecf4nl010F17vzEPiy4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:
ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67852" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67851">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=NFH0aVQlYYyID8XNl8wYnxXLs1m8hBTqQjJZbwO9Pa0U_AYdI40opS6uWhkzeIiZv-oRYORUgXMWwXCfuAHtIlO0e2NP5If0D_nrn4jI9O1nkXk6FfL9U0_r8jpSRCoowT9i1r1V101Png9Vd1D9jXpDHQUPbSCJZJeaMcA3G3pQYeucEJ93vJ-Xck4fT2tLRxjdD6QrjSzpIlDdAKp4OmyI2CwjITClR39432e-XFwbsBwIM8NpdpbQOejhfwmmaCGofdFxDPGEljdbkAzrhCf-ouIaklEFgxspp-_EY1XASRUJUkwfOAkuqMMrmZZnF64POPmnyjjiqlkwuU6CCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=NFH0aVQlYYyID8XNl8wYnxXLs1m8hBTqQjJZbwO9Pa0U_AYdI40opS6uWhkzeIiZv-oRYORUgXMWwXCfuAHtIlO0e2NP5If0D_nrn4jI9O1nkXk6FfL9U0_r8jpSRCoowT9i1r1V101Png9Vd1D9jXpDHQUPbSCJZJeaMcA3G3pQYeucEJ93vJ-Xck4fT2tLRxjdD6QrjSzpIlDdAKp4OmyI2CwjITClR39432e-XFwbsBwIM8NpdpbQOejhfwmmaCGofdFxDPGEljdbkAzrhCf-ouIaklEFgxspp-_EY1XASRUJUkwfOAkuqMMrmZZnF64POPmnyjjiqlkwuU6CCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شلیک موشک های آمریکایی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67851" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67850">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام):
ساعت 7:15 بعد از ظهر امروز پس از اینکه نیروهای سپاه پاسداران انقلاب اسلامی به یک کشتی کانتینری با پرچم قبرس که از تنگه هرمز عبور می کرد، M/V GFS Galaxy که در حال عبور از تنگه هرمز بود، به طور آشکار، نیروهای فرماندهی مرکزی ایالات متحده، سومین دور حملات خود را علیه ایران آغاز کردند. یکی از خدمه غیرنظامی ناپدید شده است و کشتی به دلیل آتش سوزی داخل کشتی و خسارت قابل توجه موتورخانه قادر به ادامه سفر نیست.
ایران فرصت دیگری برای نشان دادن پایبندی به یادداشت تفاهم پس از پاسخگویی به حملات قبلی به کشتی‌های تجاری در اختیار داشت، اما باز هم شکست خورد.
در پاسخ، ایالات متحده هزینه سنگینی را با ادامه کاهش توانایی ایران برای حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67850" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=ErHPYPUVUAWAk2xaW1f4_aY-0YySPjFNMwq1kgHO3I_T3rFZGmRdjI75Ez0_IaQ7YFfoVu1zKQ7mNERrmdYg6dHD1bo-rg5DiV0c0F5tkkY6B571lQG3K4bWsCCBpopNXJHi1h86yE6DkJfKHC6EU641yqMJxhUGiWOQ-rxk1tH_Z-numIGnEkup3q1yVOt2Hi_KisbFYYSI_7z40eMdhjebqrRNRRYgjpgat_l5gKMUs6xRvdJPnnwnlzZLXwKhA15v6tOs4-S2DZxBKp_8VaRd4Qmr9f_0w6GHTjTSmrS7iYq8npxBvJY6JxfwZjN5r3qTTrOIRT7YMJyV8Ii03A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=ErHPYPUVUAWAk2xaW1f4_aY-0YySPjFNMwq1kgHO3I_T3rFZGmRdjI75Ez0_IaQ7YFfoVu1zKQ7mNERrmdYg6dHD1bo-rg5DiV0c0F5tkkY6B571lQG3K4bWsCCBpopNXJHi1h86yE6DkJfKHC6EU641yqMJxhUGiWOQ-rxk1tH_Z-numIGnEkup3q1yVOt2Hi_KisbFYYSI_7z40eMdhjebqrRNRRYgjpgat_l5gKMUs6xRvdJPnnwnlzZLXwKhA15v6tOs4-S2DZxBKp_8VaRd4Qmr9f_0w6GHTjTSmrS7iYq8npxBvJY6JxfwZjN5r3qTTrOIRT7YMJyV8Ii03A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67849" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67848">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇺🇸
🇮🇷
باراک راوید به نقل از یک مقام ارشد آمریکایی:
ارتش آمریکا در پاسخ به شلیک سپاه به سمت یک کشتی تجاری، چند هدف ایرانی در منطقه تنگه هرمز رو هدف حمله قرار داده .
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67848" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67847">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67847" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67846">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67846" target="_blank">📅 03:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67845">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
بوشهر رو بد زدن
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67845" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67844">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
چند انفجار در اهواز و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67844" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67843">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67843" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67842">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=nL9220uTN7D68tMtE7PXfKJRGIIyhRDEcyYQVpJV4P1BlVZk2W7FYItkYqwgKH3FoTKMlkgUEvvR01csfrX7obLhzzpREHB5x1YPH3jcArtJCAHz-Wv45Kupy52XOjpcMcDn5nyhRRJ8gK5eohOq7mxhvc1hEQxtkAPDQZbuhITC_gGPCskjrGeoCpb9fHnP2K26n_tPp0j1AFz0Wrkbevhid7-dkW9hFIyMjM4CKU-chUc8HGuzhezhZYQto7Q01tMvcBzt6Db8YjLYm7uaKNDdujJlLU2rRnc5WY8pq8w-PB9_ycijpwPIbp0pv2s9teyzNNJSz6n3-jmCe7Ut4k_YPgUHca2GJOj7IbDtBrusTck8UWs1f8yOl88Apace1IJaDTrfnvl4DFf10bJ-r2yz6XZsrIYGFM7DHGJkzTgNCVJ2GaCo0wL_ThI0Szk-O_c8ZxuaDpJkAXVfd-Im9bvw_RyUcdbUggOi5wT5W-CG8Rj_3U5ut9nducg9hVMjaFW52ybIddzI9JDe-l6KYJMCpBXRxaCmnOWWI9bMSNlS98a1rnGFUgx1PAq9oXjjQHfnVEXD44gCUNox49wnkbD-I1lLBn__qE-8zm_YFK9Dwmu3QUYF9c-IWkbJ8_5nC81Lhy08Hw2BMSQXPUXiEnVboZrp1XG296hicQDMLU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=nL9220uTN7D68tMtE7PXfKJRGIIyhRDEcyYQVpJV4P1BlVZk2W7FYItkYqwgKH3FoTKMlkgUEvvR01csfrX7obLhzzpREHB5x1YPH3jcArtJCAHz-Wv45Kupy52XOjpcMcDn5nyhRRJ8gK5eohOq7mxhvc1hEQxtkAPDQZbuhITC_gGPCskjrGeoCpb9fHnP2K26n_tPp0j1AFz0Wrkbevhid7-dkW9hFIyMjM4CKU-chUc8HGuzhezhZYQto7Q01tMvcBzt6Db8YjLYm7uaKNDdujJlLU2rRnc5WY8pq8w-PB9_ycijpwPIbp0pv2s9teyzNNJSz6n3-jmCe7Ut4k_YPgUHca2GJOj7IbDtBrusTck8UWs1f8yOl88Apace1IJaDTrfnvl4DFf10bJ-r2yz6XZsrIYGFM7DHGJkzTgNCVJ2GaCo0wL_ThI0Szk-O_c8ZxuaDpJkAXVfd-Im9bvw_RyUcdbUggOi5wT5W-CG8Rj_3U5ut9nducg9hVMjaFW52ybIddzI9JDe-l6KYJMCpBXRxaCmnOWWI9bMSNlS98a1rnGFUgx1PAq9oXjjQHfnVEXD44gCUNox49wnkbD-I1lLBn__qE-8zm_YFK9Dwmu3QUYF9c-IWkbJ8_5nC81Lhy08Hw2BMSQXPUXiEnVboZrp1XG296hicQDMLU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67842" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67841">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOZeTRzavVyvhS97QS2Zn7Gifw-ZCxL3vvaPIrzIGiDphKPjar_dSSg9fmxVjQBFLs-gzZJIiYTEs8BD7EG7Xz2PBwhxVGl0pmRvds56dA7IkodOavcaM1SyKUYui1IqK6JexJI-laaMGxWzJnMutJqwHoUI_3F4PC1PN4ysHSJFia-zVHKAPycD_fses6ldhydBYX-MP0TjrFE6Pp5kg16HxAbp0aGxf7lEekkPCtQKzpQ-Lrj_bJtUlL_20njYu-dsR2nism-9Yl_Q7tBIV5XuMQxCw_ZPpD6sIKSll6nAizFSOdtdoJptbDDOaAQd7fScTEErywT2FKsqy-UMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به بندر دیر
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67841" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67840">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
چند انفجار شدید در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67840" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67839">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:   من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.  @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67839" target="_blank">📅 02:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67838">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های شدید در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67838" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67837">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=vSiZ3YSXzlALx5-8dUBbgkIEpUcdXiJZqdl-08aKZrq0voggLoZiNRYPNLmfeTW6PWxzF3k5VYjGIgtZ1wpp9ocPXkNpvee3J5APwlvYY3QjEVQ9t99pDB2NNcT8KHi8GVS4A1HVOnZ8a7xz2ZxTmOSzS2O-VESMo0DJsG1RL0VUW9l1MNXrGx96VE2S9OCIlC4uUoCUQfmKdkdoQ7n6D1qOwXrPD3kA_sWTC21cCl2T4uP9P8YzkZBlzs-ZCLSc1MQ4re03Ej-rfd81b0arnXaxJmhJHIaw8CAtGRftNXLL2E4MfsO_tVW7UTBWaUpDQ24Asyjf18DcBxTnXt2Y3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=vSiZ3YSXzlALx5-8dUBbgkIEpUcdXiJZqdl-08aKZrq0voggLoZiNRYPNLmfeTW6PWxzF3k5VYjGIgtZ1wpp9ocPXkNpvee3J5APwlvYY3QjEVQ9t99pDB2NNcT8KHi8GVS4A1HVOnZ8a7xz2ZxTmOSzS2O-VESMo0DJsG1RL0VUW9l1MNXrGx96VE2S9OCIlC4uUoCUQfmKdkdoQ7n6D1qOwXrPD3kA_sWTC21cCl2T4uP9P8YzkZBlzs-ZCLSc1MQ4re03Ej-rfd81b0arnXaxJmhJHIaw8CAtGRftNXLL2E4MfsO_tVW7UTBWaUpDQ24Asyjf18DcBxTnXt2Y3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از بحرین به سمت اهدافی در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67837" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67836">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خسته شدیم از این چص‌حملات خدایی، قشنگ بزنید جاکشا
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67836" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67835">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
ارتش آمریکا رسما حملاتش به ایران رو آغاز کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67835" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67834">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از حمله به بندر دیر و بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67834" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67833">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67833" target="_blank">📅 02:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67832">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش‌های اولیه مبنی بر شنیده شدن صدای انفجار در منطقه عسلویه منتشر شده است. منتظر تایید این خبر هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67832" target="_blank">📅 02:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67831">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=lA19pVFaZGjubDPCuNgGhvahKT1hZ5vH8LQZbbLYk0hYr3sJnAQXgbMjMiXP_1-c3zKBEy1IR3doe8nFnuMjJmlkL8_stVWFcpaZawPnSivExvdU228u_NkzjD7C_Rk6UXCgfLkO5WwQlIeJsJW4HyXBInzqnKXeaDouf-H8eMWPdUqSGkwjh_Vwub3thRuMS2eOR7hD6OymnD0NW4c96rXyocmwQVUtloqHznILxv-RRtBulX0qjdI7F-gylpH8M3UyIGyJ7otwOESDGc996oNdl7aIw32Sl6YoB7UJhXGiyGd32RJdnnl_Osnhf5Yu65jucgQQqIuctqOY00vr4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=lA19pVFaZGjubDPCuNgGhvahKT1hZ5vH8LQZbbLYk0hYr3sJnAQXgbMjMiXP_1-c3zKBEy1IR3doe8nFnuMjJmlkL8_stVWFcpaZawPnSivExvdU228u_NkzjD7C_Rk6UXCgfLkO5WwQlIeJsJW4HyXBInzqnKXeaDouf-H8eMWPdUqSGkwjh_Vwub3thRuMS2eOR7hD6OymnD0NW4c96rXyocmwQVUtloqHznILxv-RRtBulX0qjdI7F-gylpH8M3UyIGyJ7otwOESDGc996oNdl7aIw32Sl6YoB7UJhXGiyGd32RJdnnl_Osnhf5Yu65jucgQQqIuctqOY00vr4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:
من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67831" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67829">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
تابناک:
گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67829" target="_blank">📅 02:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67828">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه
#hjAly‌</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67828" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67827">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.  @News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67827" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67826">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqcNVyIe3XWS48Jl9ONI1jEr9vDmVvfR9d6CCKDDUahrGO-SRiEVcgDnNtfmQ0Ue0d3MRJLX31IPOnKI_dNwc0en-U0RKRJKrqH6_FHQ-bYISbPt_BWmSwMNpx6RpLX2c8cgBRK736vymdxb9ZFJS4Gibouuw55x7fJKUlaqr146qn4eLu4-d35fDljfFaF8KB7yJS8lFPTrztvcY4AVNIO6Co09s8qFrttttzz0gFLchmVb-AuPXpHQxcK2DoCLyQCqyydwt2vJWCeha51gNuU-1_Z_17-0ievT7dlTaUUwolc-gsNGcHqa_vvVmP-ZOn6L4d07sARxdmxcbroyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67826" target="_blank">📅 02:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67825">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvjttxgohYFJdgoWUYB5y0Jq4NiTdCmCmK3qMV7XsLuls6zdkbcErEmg0p5uslhE_7oYTwqnbPZlRqRNYKKvZ_BckdQuUmMAjvj4CxdiOLRmeG2YO11-5Du28cq8fqWXMR3QzEnLY5rJ5a15xPYH5_q2rcqnjm6zPwuD8UmMB9kOGyiG5jMzqnla4ZdPOR5j8GhEn__E_dbxVPRkz6NUgrVRjmMaOfFBiM35Y2rjOuEtvTHUtvU8o26wVpS5eztMtN8w9KofmI5x05DflShOPJvGA8v46ORXGYgJdKjLObG35_wJ7wPhI6CSxMCQLtzs4lSxUzmnsMGHVuZHfTychA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هم اکنون زیرنویس شبکه خبر
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67825" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67824">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQRz-p_pTx5BUCr0ucNp8rB413ep7OpMc43wfzDUEEmJgPPVNUpUS4DbqiEfWqBVsALXJABZuK-3FO9eAhrw1UxjMt5ODpo_OfzT2p6TsEjfnFIdRSGsvOZaIOQ3Lh9ImTNK-VYGj3z3Izy7acWFdK8AJ4gj6Bnq73FdW_a-dXMt2i2VIzmPaR0w-SuJD2JoDAYI_VMWbDEpjFdCQc15XCttg9L_VTDnhKtPlOJR9eWC-OmPB-g_3np5IbpUFDDPePY_T6elY-axBvHMHx445BuIphSEvYdUnVDgYy2VgTQ9OHCcwQB9gBJ4Om9eVbtJN5m46Oeac0oBnpV325IA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67824" target="_blank">📅 01:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67823">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
صابرین نیوز :
به دستور مقام معظم رهبری، حضرت آیت‌الله خامنه‌ای، مدظله العالی ورود به تنگه هرمز مسدود شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67823" target="_blank">📅 01:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67822">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67822" target="_blank">📅 01:52 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
