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
<img src="https://cdn4.telesco.pe/file/A2kF9hvfSXZqGgwrgH2TS0L56pP-y0zKMLjrP3hhl4goqUmxHot539CVnglkH-ym1oTteANtC6OyLXvQ8O3DGW8i6o1rU_LohdKMdEmc4FIgWxEb3KiHQFtVcuUtD5mZ0IcDW-3BHopAUaGqTrCURybNAozAJLwQBVYqEkz4Sy4Fl1wmA8mQ_ermW2C-QNFz66gJZnN5ufHUq6qaWtNzvn_NY8GL_KdtRFT2mnW5G_3mDXMrYJQf2TQ9ZOaWjdgFPKrsAGT-MwRnH81aWP1RzoPXBo1OXdjGlJUy0vVRa7RCUto_M6Z1ZkRHn3XWSZWrN8Hj0jOQzn6WIbZLVMje0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 150K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 23:41:34</div>
<hr>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=P_7xWwNzaw6cz8Ck_92kGJBu1aQfbZ4jKSKy76bO5vQ8-yDXfs6yOM1dRX41nxR1YkTckm0nv-OjgBldH0r0ucaXBq9xZS_1hTG7spwb8SWZJ3aqPLaLMXLAfzaoMYI9hjFVRkGx_QhlnrG8U7GBr_OGiNtx6_OiV-ua_-npgxy1T3EUlpsnCI2n4lG3EUhJtNtJ5H4ACRt4XD-WO-eKEVDh1T-mwmDqlmFAEw37es_BKR5NxDvWTJlrsJhzflIXrIulfHDQ9rSbtaMu-F_Qu29Ufk6OwRlo0eYsxPd_D75sL9Y2ZQwcrQNOlUO0KqSaS01PqRpHyVnFon_MW5A-fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=P_7xWwNzaw6cz8Ck_92kGJBu1aQfbZ4jKSKy76bO5vQ8-yDXfs6yOM1dRX41nxR1YkTckm0nv-OjgBldH0r0ucaXBq9xZS_1hTG7spwb8SWZJ3aqPLaLMXLAfzaoMYI9hjFVRkGx_QhlnrG8U7GBr_OGiNtx6_OiV-ua_-npgxy1T3EUlpsnCI2n4lG3EUhJtNtJ5H4ACRt4XD-WO-eKEVDh1T-mwmDqlmFAEw37es_BKR5NxDvWTJlrsJhzflIXrIulfHDQ9rSbtaMu-F_Qu29Ufk6OwRlo0eYsxPd_D75sL9Y2ZQwcrQNOlUO0KqSaS01PqRpHyVnFon_MW5A-fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=u2ivBJJaRADSOtJ8oEaTR8UwrwcvVvi0CKzsE7RiU9T_olX-C2PG8FoiwQCuBPJa6ZwZesHgxeIDBql3ErW7RVoBT34FMGZHEns9KeWTfWCGcZqMyFq-7BKOySJ0SNutLSRo2LwGyYNAVbVXBo6Tm1TafKFhBIh-Wtqa7VrGKZb6ALFeUkZ_VuAQtf4PjSCtW5eQkwO3M8yN9tFfP6LwEYbw-NkzlDjRWpuLDps-3PgwkfFlyFVrWxHr-xf7N_Q7B0IIz_55UevTaeK7qCZg9Gf7mkBDTRUi_IRFrIEB0-2jv4U04jfjkj3inQeCS7TqPZcC7nBdzR1aMRrVLhxpWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=u2ivBJJaRADSOtJ8oEaTR8UwrwcvVvi0CKzsE7RiU9T_olX-C2PG8FoiwQCuBPJa6ZwZesHgxeIDBql3ErW7RVoBT34FMGZHEns9KeWTfWCGcZqMyFq-7BKOySJ0SNutLSRo2LwGyYNAVbVXBo6Tm1TafKFhBIh-Wtqa7VrGKZb6ALFeUkZ_VuAQtf4PjSCtW5eQkwO3M8yN9tFfP6LwEYbw-NkzlDjRWpuLDps-3PgwkfFlyFVrWxHr-xf7N_Q7B0IIz_55UevTaeK7qCZg9Gf7mkBDTRUi_IRFrIEB0-2jv4U04jfjkj3inQeCS7TqPZcC7nBdzR1aMRrVLhxpWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=HSsKfbG6yjTEMlQvpVJ2RLO96VeCQY66FGGnc5BoEl1Yr8ASzjpLRztAHYoR1EeB-Q1wFx_Tso3CTiczZnx7-9gLn-9UF0-9IsVWVmaoVALG1kAQfPTBZsKxh0LtJac_C7psjWQyYaV_HjDYvsqoRYYHI1yEz90Wew2ZYcOrJsreGx0tcEbomtP4Y6uCVnD_Ck4--oLN5DfmUWdtsgsz2HNjJJvyDs92T-zcXoXPxJfwFPbauaZ0cl-KP4ym4RhH4LYCg1NfPdoy06s7CEhl1MsHnSFDt4z19wLT3s__kg8VLslxA-t4PIKkM6jYIY7QDQc8dHKknHgDgR_otck-wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=HSsKfbG6yjTEMlQvpVJ2RLO96VeCQY66FGGnc5BoEl1Yr8ASzjpLRztAHYoR1EeB-Q1wFx_Tso3CTiczZnx7-9gLn-9UF0-9IsVWVmaoVALG1kAQfPTBZsKxh0LtJac_C7psjWQyYaV_HjDYvsqoRYYHI1yEz90Wew2ZYcOrJsreGx0tcEbomtP4Y6uCVnD_Ck4--oLN5DfmUWdtsgsz2HNjJJvyDs92T-zcXoXPxJfwFPbauaZ0cl-KP4ym4RhH4LYCg1NfPdoy06s7CEhl1MsHnSFDt4z19wLT3s__kg8VLslxA-t4PIKkM6jYIY7QDQc8dHKknHgDgR_otck-wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=m2_tYk8N5ab1Ct2tFVffz85uPdj2Qyz-g9Vnwa1eZROXE-AwLAySAG6o9-wSCXCG7vUSbSqFifxKtaEZptZtZnMTafGW3XPsv49iZliZ0YNylUGLZ2VprgX1RJ7xqrFoDvvB7Gq5Jv-EHCwJ__LZdXX6xGO3tw1sAjOIGMqbTwoZujqWU5pOTFoZWM8GuUyyIkprnBOzJ-ZKHcYo9XrpHaVZ_L-qd2Rf01aP66rw8G4TSqmvV3GaKOksaAzFp5LL6qYZUN8g-e54mgGHZO4GFqtoGAS-DNqdnOY_lBTFluIN23uynwtCFBQc5aDX6IUz2KNmXb-o9Ou1VGA8aIR3yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=m2_tYk8N5ab1Ct2tFVffz85uPdj2Qyz-g9Vnwa1eZROXE-AwLAySAG6o9-wSCXCG7vUSbSqFifxKtaEZptZtZnMTafGW3XPsv49iZliZ0YNylUGLZ2VprgX1RJ7xqrFoDvvB7Gq5Jv-EHCwJ__LZdXX6xGO3tw1sAjOIGMqbTwoZujqWU5pOTFoZWM8GuUyyIkprnBOzJ-ZKHcYo9XrpHaVZ_L-qd2Rf01aP66rw8G4TSqmvV3GaKOksaAzFp5LL6qYZUN8g-e54mgGHZO4GFqtoGAS-DNqdnOY_lBTFluIN23uynwtCFBQc5aDX6IUz2KNmXb-o9Ou1VGA8aIR3yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEEgnEewKE4UslcEgzbabMID-mn_5eBMUY5qvQbxJiKS5oqmVotiSIdz6JpeFKdl_WbE8zmZbMt7jZMQdREe5_JVhi4dYqQ0Y9XTBJpEzA2K2hh_zrrnAU7KWiC0DwFWKJSH_7kxBG1454Mi-_NzbiLYKkS4WFmgpIh25536NNAZc9_yQwy0C0V-Vyw8q6GrpmXzYyMuWt6tEiUABIKENM748cVt0Ig7YxPC6eIswl6kq_IndBs6Fg3pJxBBsIVNb3G7AVxW2iMBr-0Ezpv6rbHiBCSzzC4ajGvdqFQXpPux6YE2mEip1o-8uPIUChf4_MXynlHzxmBQdSdSumSqYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u21hxE6TBKmi5QqsWR6ujBfbVtUfs4cORZt8lx1lNeuQnDNXmHIjfP_5n9QVYFhkOJkk2LH2WvR_heJfr0luf5pB8kJSfem8WJdodX6jMj52J8gw6HI9hWC0kwUms_88phIVVCsSTKl0eFQW1Ad__PvdSmYG6Rhs1wpaGKLFrnLKpicR1MCxmj-mXEebaNxGl-ymc1x0UL2f5wOPLluV1fBGSCjS11kGGRvGGKzqOYXQbJL9cJUDUdmnadm_zEpa_-BYq_WQKyXh-V_bnRhR-0w-IUA5OlsdRGbXAR332nqL4DZsSuEpg-6NaXLQ5qcXtqYWYMDAjwd34J5joFZuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7Mh_vlyTE37MFQDkyfLJVwubVzlwM9u7uuXzcx9UMU6Ud8ZXyVswaKTI-EM7-z4nTve0I1TGjD3TM3SgZev_e-8-ZzgzrgPTAR04lW3r3WtCAm-bK7sbSssUH9MhnWKNLy09V-GljXz-rL9Gj9GZXr6d_BnaLJCs8Vbakn2qxb451Rtrr2lPEviX_cnN8WrdZfbAmj8jmG5s4dhQp_AvYjgSr5lcbt45PfMfh7JTyHxWQxD5aUs5RQxNpwvTkaYGNMHpQeSUL3xPMRPfMwdw_HSyolO98yAltOJ1ENgDSu4RRzuknaixBuqre_UHE1069xffQiBSK_ijFltSjQwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=U9Y_K_e88nQ_ZSiaf2dKFRplKIqPK0jiUvWxuvYeq__mU2XR1I3ID0z36-xzyE9iWMsI_pfZvwrbyyG5kd7iqnUXsCNnu3eREPPLUWQtESOBdVtEwrElCtDSh6XalPqa4sDTnpIDP2Nyw0NUxTbYU2lnQkz3sMCUmVc-Fxw7DkzAXJ0TTKp_bl-SUJp6kenr8agxwXkXCshiOgBXixdl8MuhqT9YfgNh3pDQJ-kaR_fPHT-htJshswuAkuFqynxEHHGUMCQNC4RuUaJ0Xq-B44U2rI5jzDYgQPpkWw_NH4odCQ0X39IWWu-CMPN83n4KuNbKIsi14YcmyNzN0w3ixw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=U9Y_K_e88nQ_ZSiaf2dKFRplKIqPK0jiUvWxuvYeq__mU2XR1I3ID0z36-xzyE9iWMsI_pfZvwrbyyG5kd7iqnUXsCNnu3eREPPLUWQtESOBdVtEwrElCtDSh6XalPqa4sDTnpIDP2Nyw0NUxTbYU2lnQkz3sMCUmVc-Fxw7DkzAXJ0TTKp_bl-SUJp6kenr8agxwXkXCshiOgBXixdl8MuhqT9YfgNh3pDQJ-kaR_fPHT-htJshswuAkuFqynxEHHGUMCQNC4RuUaJ0Xq-B44U2rI5jzDYgQPpkWw_NH4odCQ0X39IWWu-CMPN83n4KuNbKIsi14YcmyNzN0w3ixw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuUvtr5U2ttOpQuxQDkDLMYiWefbqpnQU6CVxIt6eFAOOHWSw0o0ifwLYUo4nuT7Q30qnGB-AykD_5dJ9c5tjiC-QMv6BiruzJlPKHOBE4G2rhsFjGDyJ20DjAmKqEJIuXmAyOhrGZ8vxfOPDX4ZVp22SwScAFpnR3IPNWxnrc0BjBJNKWXFzKdoQfAy8Yqp5FvEhYfHkS33PkWHWbZqqD_Hemey-0tKLtGqOfZJkpbRIcaoFaOR5OgGPqbfpiAbIXiubLoxBUTjCPFxinO0qYqK3s7rmyd29A-UdoNOUtZuIKxvuSu_HB1ieEKiabAtmSoIxr7K-opKaGxBAS9iLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnZTGdNnLP8UfQYOIY5sDGZdSgwsAS8lNLreJeSU890R_7wLAiZiP4Yw-aDd7MKPGIqmets7WzjFxH1Onpp1npsx_K94WffFC8qwY60odu475hxItTx1O5XTIyZ1O2fE5Juvgf_rfeU5tfTMcJSwalzjGp9x5HdZSjJ6-HjRXLMj7ThVfEn0xmD-fj5FiLizvXCLNtdCSy4Q0jmPE9M36O1BYXvOr_KAbqniurxJqine6l8Z07FX1efiY-XXe9sMKTGhXRG2y8XUdQPoLjHEHhXkouhIaQgtwl8ONc1SM0Zz3c4R4i15WR-jebkij0gFB2hrDJuwVM5QLZQFtZA-EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=d4mYT9k21vLbdJnfHSedmHBQNm27pIxDSgIl-m5e1_YjVnzd_gLx6rzCrunw5xHcACfFWAr8a9dHhfBiK3QXSbadQvrqLf9SlU1V4jUr91XmUhWU8UjgBjLC_Dm5UoyBjgogQIg2qP2BrAjy4fwpW1EDdhk-OomBlh-Gz27-b6q8vgMB5rZDNZYAZfAzrYn3uq4G41mRj8xDVfw9v13T94lJcSNcy6PmXxyZXKtIC3VOrr49Vl6nQGzHSGnCDT7s3KdvLgAIsP4KqqdRwZSO5tIaQGxZonoLdGGkLvwzO00DgTv8DifoprJsoVHESICcbFKDejvsGrWpMyc4klUdTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=d4mYT9k21vLbdJnfHSedmHBQNm27pIxDSgIl-m5e1_YjVnzd_gLx6rzCrunw5xHcACfFWAr8a9dHhfBiK3QXSbadQvrqLf9SlU1V4jUr91XmUhWU8UjgBjLC_Dm5UoyBjgogQIg2qP2BrAjy4fwpW1EDdhk-OomBlh-Gz27-b6q8vgMB5rZDNZYAZfAzrYn3uq4G41mRj8xDVfw9v13T94lJcSNcy6PmXxyZXKtIC3VOrr49Vl6nQGzHSGnCDT7s3KdvLgAIsP4KqqdRwZSO5tIaQGxZonoLdGGkLvwzO00DgTv8DifoprJsoVHESICcbFKDejvsGrWpMyc4klUdTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2RPDkiriB_WUbRPPJcZQGtUvOsBM0WylXl_BYW8NMCdxgSDZYVfAyhVhSSkrYKAlkJOi9xOGkcOJZtngKaEAGMZqlemrkte6sJeeN518U32hkbNBibc4ipjIZyefjtVztVnET-KpKcbE7H-bcTaTWB5YepXK2jcyYLlkvLDqEGEwpwmD2WI_vZ9BDCCFOWrGBCDt9BvXukF0yON_Yc0qsFZ8MXzVDs2m7TX-ZrR168TciGGDfdA2Oac5EKAl3q9ZhjcxVZSB9aGd5vM38jaJTxj1Tcpiz85K8sIvhZRxucHJdlvdYuqRY91iBoCt369UT80nEilyAPqSgl1PFtEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iINLIwQJOe-e-sTck44oowJ0GlZRX0H_oiga6eqDVqp1wBEh4RtHwdE-_hVODyZxzhOqu2091IRMmIVOGFS8-OBkLHMasdMVo-7enIhbwOJOqw5NGBsm-zFyTIuwz8pmXN6srgbXGTZ770eW4A5NOGDXRMOI7u8lwl8ZoiD-amnjhvTMUZno-k43QS4-JU_5TVhO0Ir9xwV7lF7d1_54g65wdKEYgFYaInSK2eWL2Tg54pe3f3wxYeDe3RpRohpVnSnUlIn33QQY7dg7QlmeiT21EmBllfg5CHke7WMCVWA71yCCju80pYU6-caOF8PZm2IvhaJfweFA7hfHLk7ZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYXKLhzNkBrgoZZCKmio6fvj-Y8l70W8Cy5mBW4hujzD7hopl1RyQ8zq_N9Qf28Bwem49Dsj_ZzSxZh2LbzeGad7OahnkoA-oM1IkcDu5Mq6NpS-RRjx-9GeozkUY6RzMqtG_2Gd7X5MSAHPLtT5OrKeIEwY5uJclwv7iMdNnyC8I1exK9glZ4OASidvipoZkRq4U9wqmUqwrYPiCq3LRAnz_hMJoOIybbommhh2A2-3-J6-qI_Uq4-Iu_L0MJoNwz5K4FJ0wYDs2BCIR1q9hzyP0kD78yJ38ujSbZCyTDW1w5hySZsDA3NeP6LmPv_G41H4XCobj7auC334uFnVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-e7s_oqzMpRSJx0yNYDL_KOGbYRHJl47Ayu5o135dtT0Ejf1Bl2Hu445h11tKqNR2QaD2N5_Wq4OQTguYnYpszvvxasj0CVCOIylp4U3bN-9-n6PyNREYyL2SOrZywSwFT3pH5Y8tU7OqYIVlsQXeKvteJhG4tmPnIBBzLg6qiadz477Vlm3IqZJEnvHc4qjeDJOIXY8hyoGTjYeBOk-Gtfc-X23ns-cSQhghGIUZtBiI9GasDUgqOTHNDZie_Z7NXC52T-wAgib6MT_Gtn43QMdW0drD69Sv_qmgt-pjn4xM3htVJn_KRbITklBA3WuuH3_px0Hz9YYV2WxLx4lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=sNIGGzvHjwqF9K8jf4aAY36yBbcXLPCS7UZsGU1rPVPh5u4XbugFTXlSKfmU7e6FvzK4eEZQ2VnUM6800TKtPsF0weR3YcMQ2HeUKhD9hrgl8vARDa3Eu-QVtkBFxc6PiZoyz-lTW3TAhtiL4YsHv6rAWG-y4vBs2SSndJg1AKLuL3s2pzHsoQyCinE4yX1rtsUnJokbU9dvZsss9tppzW0P1Igfjea1m1U2w2bN6XWgkXusVjRaxkIEksDZ0pVzlwQXRg7zrYIKsOKKnE7r5y7MhfT0PlEViJxfwWOz5yyoCk1mDlllOzsl1AR8ZfBvoiMnXbQEftSEujpwJnnIpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=sNIGGzvHjwqF9K8jf4aAY36yBbcXLPCS7UZsGU1rPVPh5u4XbugFTXlSKfmU7e6FvzK4eEZQ2VnUM6800TKtPsF0weR3YcMQ2HeUKhD9hrgl8vARDa3Eu-QVtkBFxc6PiZoyz-lTW3TAhtiL4YsHv6rAWG-y4vBs2SSndJg1AKLuL3s2pzHsoQyCinE4yX1rtsUnJokbU9dvZsss9tppzW0P1Igfjea1m1U2w2bN6XWgkXusVjRaxkIEksDZ0pVzlwQXRg7zrYIKsOKKnE7r5y7MhfT0PlEViJxfwWOz5yyoCk1mDlllOzsl1AR8ZfBvoiMnXbQEftSEujpwJnnIpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=Vnl4TS2pQodfoVkymFX7mqG_fzGX7VHJmMlznV13NI8yNI4Y7TOm3e4f9_fIuDx_VMOcqZGqx4SJqFv1e5k6mXhrE-65B9Cm8sNzEN0eVDyfTxeJSToaT6CgPQZHQPy9cltIPx5BCOnEhwmfmbInQt9zE_skQujoUfHE2bMkeX_F-06rvJTD8iwqid90OLSyALVy7kmmIXoEPIxpCPvss9nwjYZd0vNZFwGw1QFLzprBS4b8U3n5bjuzzdGP-l5cu1pqa0m8Le5DZEHa1R_1-DgvVaJcJ5fEpRlCkTXpsHrZXyKuJacj2HLOYkt5ib2hsaO3iwmS2lf9zPr0rNEc3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=Vnl4TS2pQodfoVkymFX7mqG_fzGX7VHJmMlznV13NI8yNI4Y7TOm3e4f9_fIuDx_VMOcqZGqx4SJqFv1e5k6mXhrE-65B9Cm8sNzEN0eVDyfTxeJSToaT6CgPQZHQPy9cltIPx5BCOnEhwmfmbInQt9zE_skQujoUfHE2bMkeX_F-06rvJTD8iwqid90OLSyALVy7kmmIXoEPIxpCPvss9nwjYZd0vNZFwGw1QFLzprBS4b8U3n5bjuzzdGP-l5cu1pqa0m8Le5DZEHa1R_1-DgvVaJcJ5fEpRlCkTXpsHrZXyKuJacj2HLOYkt5ib2hsaO3iwmS2lf9zPr0rNEc3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEZ82PqCAF4RNKh18RXaVEZeGKnZ2U4ccFZX_K-79RwlZ5yKolNZJef3zpqbcS_m1af6TLmAJ8qbkDUYIRcqtBw3Ft50LFGl9YDO7V2TrxrtjaEIKrnknWep3CGEKMyyBRk-Ln3xlxBi0lcyw19_6lf1DWA1v_4Zv-yOEyBPsSHxLvs8LfyaEaBtFQWZOFCvdMXnE63MWeZ2pd2_TGAmhFnoeE7vIozFoZChRywdh1sA0Jr2PPu_S2MiNdxC-WRitQtfnW5VP8A3h9R4gh8kdf6FZrNJ-32JVGHoh3adj4nrdkT-rJCrxD-t_LK4M43IqrBdrEDDJk4kea4xM7d8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=S6bbXlU28kKB01ZfqIF3sZ3fvkQMv0qUVnhXJVEpGdbsx8Ue6B3VzN8CHW9JiKwkBMnAEvO0ZGfBJ5nxcEM4eRcqyrN62nEs2eTeXwSyvaCbwjy0n2pIDAi9xGvpja60nKD9Ixomv3NDxUjJOYt_nyYizATIU9DfdzjMGesMMITJD3u-6UUPzNlmcJTfzVNRXBe7BwbUo7w99V5yXJZmpxeAjo9_pVm3edmEM9wn_2vTw2F1pbmcP1wEdXnJ6DEOLzr9kFpGqI43jAw56DTFiO_VIj5d8cot4yifYs3P2yiMTZZVcyUsMuqW81PedVLaYufpdmazy44TfJsPaDvQOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=S6bbXlU28kKB01ZfqIF3sZ3fvkQMv0qUVnhXJVEpGdbsx8Ue6B3VzN8CHW9JiKwkBMnAEvO0ZGfBJ5nxcEM4eRcqyrN62nEs2eTeXwSyvaCbwjy0n2pIDAi9xGvpja60nKD9Ixomv3NDxUjJOYt_nyYizATIU9DfdzjMGesMMITJD3u-6UUPzNlmcJTfzVNRXBe7BwbUo7w99V5yXJZmpxeAjo9_pVm3edmEM9wn_2vTw2F1pbmcP1wEdXnJ6DEOLzr9kFpGqI43jAw56DTFiO_VIj5d8cot4yifYs3P2yiMTZZVcyUsMuqW81PedVLaYufpdmazy44TfJsPaDvQOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=gHmHnkLUVG29Q7k8G12m-pFZgzTcBDpZYsw1ctcXjHTRLg6RUNqIIlDJCN5Fz2nvUX4gSEsQCbkG4TZah6az1wrfKsDCK_ZEHVAaAhNL5uJlavkCdkew_KGQP0S4P8vW7U-yJxMycLevOUir8MjpR8z5C8u8Rx5UkyKJtGN7saoWEw5tbIvPekv80wSsfw_hCiCYHFd3ZBOcNSHZUX6LA3e8oDhQuUqes7CLNY1ZodUtEjbXjrKhIOOOkntY6b8-grp56m6vc2B4Ca0YTSqGveHqhkawp1mPS7tLNRLhXGuaCpsBmN6252zxdP1-K8bRGgbkTwle7kd9oJjPkjKzSR-fFPZ7cZT6O7-XW6NnL5aT7mvhilz2gK1C_RqNGMjyeswoxWn3insyxQ9nnFtiOc4aUjm74rYqJD634fHKyEK8no9C8O7joGh-qWoah8ZNgu3G0r2AuGPAf4EIrPMPQskjr9XxoSXS6c_ckccsGjo309InI61SX1qLiPRFMA6QxouYLZmETJGUIoc4H0lWyhw52w5V2eEaMh_DDsSALw6YBmo9uoJ9reet8JDFKCTt77LR6bWyyu2Lb62uFowNaLo9zsdsb5T74gfogTw5L236_xGlko3UmSS0Y_uve1xe60kC1H4fPvyz9HyaerhZXAKOF-i2LT4ibcRLZg1JM_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=gHmHnkLUVG29Q7k8G12m-pFZgzTcBDpZYsw1ctcXjHTRLg6RUNqIIlDJCN5Fz2nvUX4gSEsQCbkG4TZah6az1wrfKsDCK_ZEHVAaAhNL5uJlavkCdkew_KGQP0S4P8vW7U-yJxMycLevOUir8MjpR8z5C8u8Rx5UkyKJtGN7saoWEw5tbIvPekv80wSsfw_hCiCYHFd3ZBOcNSHZUX6LA3e8oDhQuUqes7CLNY1ZodUtEjbXjrKhIOOOkntY6b8-grp56m6vc2B4Ca0YTSqGveHqhkawp1mPS7tLNRLhXGuaCpsBmN6252zxdP1-K8bRGgbkTwle7kd9oJjPkjKzSR-fFPZ7cZT6O7-XW6NnL5aT7mvhilz2gK1C_RqNGMjyeswoxWn3insyxQ9nnFtiOc4aUjm74rYqJD634fHKyEK8no9C8O7joGh-qWoah8ZNgu3G0r2AuGPAf4EIrPMPQskjr9XxoSXS6c_ckccsGjo309InI61SX1qLiPRFMA6QxouYLZmETJGUIoc4H0lWyhw52w5V2eEaMh_DDsSALw6YBmo9uoJ9reet8JDFKCTt77LR6bWyyu2Lb62uFowNaLo9zsdsb5T74gfogTw5L236_xGlko3UmSS0Y_uve1xe60kC1H4fPvyz9HyaerhZXAKOF-i2LT4ibcRLZg1JM_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn5QQnV6zuTFsYpRQPS05KlYZTnBmspQVqUzM04t_aA_N-2Cg56NaNbNOzhPNrPdU2xkvgp0k8wpOuqDDc-J0XwmaknS0s9Nv-6jTUhQxuB2nwwILEDlhywbxPE2DHNfYd3A7v-Va0hMOFs-SsgeKPPrVqL0U_fHu0IZd7PHcRuEZr_xKJL51qMfRMgpqCOGFhD5vP1y_BZ9FanI83dP1-s4ARNVk_o2D_Arw4gpHYV-IAQ9YEGV8INGJd9SK_yP4AsVN8u8s9Rq6Yj3uQph4bSXkV5A9TaL6i9l7XvKjCzNvXt2GO0KEb3_YthVF_1yi6PcWXxbT-oy2SA87BxTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8y8dSOFhGftEFtB2GkYZJSkSMbSOoffc1yMeKnwrZVB4YC-zx9S6kY4kd48NALGw_ZP4t561nDZeJcBt8kduQ2zt_L5a3DGp8k72cgQ-jjJ_lFLz4-2hpeTXjnONWXxICQiQsdvRLRZrLQ9b9f2w0KHSr6MFfxn5lQb8HeRAIwgZJSAtzAIn--Go-LJjkwOmtCna5gzgt5YDOYx5TW_UfuIeDeHr5TnCPj719EoYmhrCb4wi0sLFngfgSP1Woye5Hz4o7IFjVd1SKStUQLtjQSJ3-pMGHUKQ_YF2qN9gh5U5FOxUVLF_JjKryok0-lukT7uQV9wf-UFaLE-KpHoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HALS0fGIfVd9PhNCGqVVmTXLUQgF3X62dxWrhnLZMq8hM3nWUjPezmmOm775PCof3EYdgt5YbZCzUnzPlajb5pjzBMGf_OYppsZ81yoBvGgqOagrKgf156ZSi100wLnmfSHHGsHRw23TyVm6rtF9ZauHdCTZnKNI6GirJduOVrXwnwcNgEqkcE3AvtHqnSbghQMHSGjOro2Ina88QjaPTpW4hdvqgBXwLYF81tc08bCZ_mBWKKaB6d-u9ptDYevCv9Lp_fppJf9--wSiIIqBPUiDpWd2_KrdoNhIbG9y-QMPunZX48d51S1ieFFD_I-tKeOvnkfu5UCvkS0iAw-E2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRJ7TTGs2Ofl8jong2j-sno1zEHUBkmLj_Gl2EPO-WxYj9RrPG9LOR5ewe0cepztxxUHGHwf-QG0Ba6a329KNdVOkcUMnEGYJhNZnktH5usS7NmgMpJRfSJRkJEw5xY0AXkThUCDk4xSQ0sJZmmBLcW0Dmm7SsB9_9C8ABIjXtyyHjWLtEj1lL1TenIaefrqC4juhpTeAT7URNk8ZqsTqjk4zrh8HFcT-yjzDw61Q_GlJmznveAi6GhtC8EtBLOClaVrmaqFCU1A1YXtn4elZSQMv_ravXg3jDCU5u-I2YIGgqDtPpBsQFWiYurVzbSlxhfyHQX-nr5fHW1vTuY7eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=PoMfqO5j-3kzg8TyBBSTL2kwQ4e5X-v1Du48cFatYAU5__MJ3zPuixctrQlcbLjo01h9F_4Y2DPnRyFfQa4zEl2-ou8e5XiMjnXIo8vppQObRTXC-C5SJhNDex9dqpETmpKceY1N87UudMUT1iT_IOVePJbzTVS4V3O2CHAnz10y332_9RuMLCuXoT275kWAQGSPEagiZZpnjbyPx8taw2NmO7B7pcsIz_u5S2iFyGVGqd2uCZP3ZA3e7v60vgcxMn8xhFbCRmVzOyOQ5FrgdA8Vcl7baU-BHHijK9icMw2xcIe0_fdcvtUNOX8T97buz_nbPvSV9CervjB1NI18vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=PoMfqO5j-3kzg8TyBBSTL2kwQ4e5X-v1Du48cFatYAU5__MJ3zPuixctrQlcbLjo01h9F_4Y2DPnRyFfQa4zEl2-ou8e5XiMjnXIo8vppQObRTXC-C5SJhNDex9dqpETmpKceY1N87UudMUT1iT_IOVePJbzTVS4V3O2CHAnz10y332_9RuMLCuXoT275kWAQGSPEagiZZpnjbyPx8taw2NmO7B7pcsIz_u5S2iFyGVGqd2uCZP3ZA3e7v60vgcxMn8xhFbCRmVzOyOQ5FrgdA8Vcl7baU-BHHijK9icMw2xcIe0_fdcvtUNOX8T97buz_nbPvSV9CervjB1NI18vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldDoKVmhqW2Ty9ITVMyPL59qNyFMSHrDA0C3mmIYWFYijBbxLdhWBSuWXKPjmTAluvOmOazwrwZn5qCEhwi2dHyGwDVSMa1AB-9DSUEEV39GLmhSzkCWUuFh05U6FVcN59QIRt1OgZyWxGGXGkzvdSQ1ZBWDimKkDZzumCsxXG65i7Q9g80xznv7ev02gvuTK5hkEav53i03GXRtTgnS70ROpQV4ChGCllB6OsxHIiiLOMDl9SBEJPfqT6VW2hzVAMYvT0DBXFUbs_N9ZW_a_1NLij5XH6qkEgNmVp0h3oBbgWOxM_D0_0_wCkFe5oK0YFY7DktwBnRpaIaPjZXTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu2hOnPx64uZ14BlnG_XdAIq6OuRaiFLMJeGDch5BhSLWaEfOfpfQBbmI1tdOiSCXOYWtmOMymi1gYCIEd040oT_XSlRgAnH35tquTTwk3tE7y4dfxiYo__Ff28b7hCyVNjeb_a8EkeB14sRc1euE73lEOX3Lzw_6wZgoc1HTfsyxChWEN_eX7Tp34h1sI_B8BbB7O7d1J2d3NDiVVaI4o3JNUqiTR0l-w6NZ3_bvWOjZL_SEW9s5r-l-RRlr0pimuvY-vBLMEAAzDQtqV3l6UEyBXViiZDw6mZzQeIpbKaOsLyUBfY3gkt5V8I1TFGGkADN1ztD7mai_sJJA58Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=EaChnUoo6Isd7r73__CLtmWSlrfe6ZEps5DsbMMJVkSL5vZzAAYqXwDQ26EtSlMlwi8toeXw1nhdmLsY_-Qh5znEyl9f9tqNx_z6nc2jMnYmcoh4qjj4faUbU5qTuylgvmjknWcD0Kma9agb9lQcYttxKo6EWRO-ouEK6js2xVjyIecAcUWPlrytsSVP51BFQ1NiJwzpDkBfUXG7LOV2l99bdtzcuXIRQU4LQ8MlP55ZfUqOV9i9N5QNQldUuYirBwLFf_H1r6RPeceFjJlr6XaJKRDZPNTGhAEt0bDGgJGu13mkYAGo1AHyGsm2tDC95d0qI5Z9HW0c7oh_BjP9tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=EaChnUoo6Isd7r73__CLtmWSlrfe6ZEps5DsbMMJVkSL5vZzAAYqXwDQ26EtSlMlwi8toeXw1nhdmLsY_-Qh5znEyl9f9tqNx_z6nc2jMnYmcoh4qjj4faUbU5qTuylgvmjknWcD0Kma9agb9lQcYttxKo6EWRO-ouEK6js2xVjyIecAcUWPlrytsSVP51BFQ1NiJwzpDkBfUXG7LOV2l99bdtzcuXIRQU4LQ8MlP55ZfUqOV9i9N5QNQldUuYirBwLFf_H1r6RPeceFjJlr6XaJKRDZPNTGhAEt0bDGgJGu13mkYAGo1AHyGsm2tDC95d0qI5Z9HW0c7oh_BjP9tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=gffN4nA4NYQ_geiOs5MfbXwKoquRHt-JsOowBDGKeHMLAALrv414y9BFunBRIrOo0-johMIF4ocut5ydvG2mRRVwjl0zNqn8LkNRbP8k2aikeJXCaEAVPa1_jQ5nmG6Iik0ZRxvQXJE7WCLCutseUXeu0kuoD0Qfz3k2n86bnn9VVglcgrljvr5EuPdWwx1f8SPbn4KaE5KYTPcBx4m6ZSUwSQ8kGuk5mEXwGKRiyvybx7lnxzIVMp1sbcQvbheiqRy54xTyl6BdGRpsPg6X0SKrLsIgkfUNIwIDnLg76TsQrDRTmuXkMM9ALcpiDHKsVK1qoOCh_oOzMJxT1D8lfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=gffN4nA4NYQ_geiOs5MfbXwKoquRHt-JsOowBDGKeHMLAALrv414y9BFunBRIrOo0-johMIF4ocut5ydvG2mRRVwjl0zNqn8LkNRbP8k2aikeJXCaEAVPa1_jQ5nmG6Iik0ZRxvQXJE7WCLCutseUXeu0kuoD0Qfz3k2n86bnn9VVglcgrljvr5EuPdWwx1f8SPbn4KaE5KYTPcBx4m6ZSUwSQ8kGuk5mEXwGKRiyvybx7lnxzIVMp1sbcQvbheiqRy54xTyl6BdGRpsPg6X0SKrLsIgkfUNIwIDnLg76TsQrDRTmuXkMM9ALcpiDHKsVK1qoOCh_oOzMJxT1D8lfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=DtZ7Gq_kjfI6lpY7Suy98XIReDKYVwgf7okSSJ1pL7S3w7RAK8tijDb1_548Xq5_4Yjy_xL0y2k04wVLLyEbbvae3xaiSSoaQAb40fXHQhWESNyc1B5QmlQDR-lYkvtviyH6YbyZMrRIAhjIr-Nc2kaAU2c2_3caLp0Ku2GWfx9JcTWMx3x7NT6LL4TYdkrJ0taYlz3vEU8SeMR6o9rxM7V52M2lBqMlayiD3mYqLrj5mB8x6-ItYhmWrZoKFjIvgL-JJHhl7NTDG3q-196JfDlSnIENkfbhVIOguwDPK7acB2Q0LauzDrES8FYic3TBxQDplO7dNJwxrcAIL0gN6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=DtZ7Gq_kjfI6lpY7Suy98XIReDKYVwgf7okSSJ1pL7S3w7RAK8tijDb1_548Xq5_4Yjy_xL0y2k04wVLLyEbbvae3xaiSSoaQAb40fXHQhWESNyc1B5QmlQDR-lYkvtviyH6YbyZMrRIAhjIr-Nc2kaAU2c2_3caLp0Ku2GWfx9JcTWMx3x7NT6LL4TYdkrJ0taYlz3vEU8SeMR6o9rxM7V52M2lBqMlayiD3mYqLrj5mB8x6-ItYhmWrZoKFjIvgL-JJHhl7NTDG3q-196JfDlSnIENkfbhVIOguwDPK7acB2Q0LauzDrES8FYic3TBxQDplO7dNJwxrcAIL0gN6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=MTwqjsuJBa2v_74dPudk5Vq3lEdiKhfgHjOaunIaCDBglrgqX7akucu0TYg3zrU5p3NX1yWA50Wls7bkJ_zDoAr-tsqhffNGS0pHQUutBfMGhmDP-WLq_tlNP6FI3knkJh4NBbF95huhRJrtpvLpgdKYG9jqLjeKCtEpZZVLBsVU1HZizfZr4BidnfZ4s6DeH1WGTljkv7x1PffXT5xbxojNICmXOuUIKuzksTdvT-UmH3MouFmm3p5YxWQX7GBtgrtHD7Do7OSYsQQgDyMeiG2DpmnacjupOGSonx0OCVyyWu9wzl2NLPxuTcE1Q2uMdjnHI4N1igCY7WuET6SWKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=MTwqjsuJBa2v_74dPudk5Vq3lEdiKhfgHjOaunIaCDBglrgqX7akucu0TYg3zrU5p3NX1yWA50Wls7bkJ_zDoAr-tsqhffNGS0pHQUutBfMGhmDP-WLq_tlNP6FI3knkJh4NBbF95huhRJrtpvLpgdKYG9jqLjeKCtEpZZVLBsVU1HZizfZr4BidnfZ4s6DeH1WGTljkv7x1PffXT5xbxojNICmXOuUIKuzksTdvT-UmH3MouFmm3p5YxWQX7GBtgrtHD7Do7OSYsQQgDyMeiG2DpmnacjupOGSonx0OCVyyWu9wzl2NLPxuTcE1Q2uMdjnHI4N1igCY7WuET6SWKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=Zqv7QoD0vzX-QLg079dgnUCACeKQZjK7au3295n4_iRLfTAF5DKuR6RHRfow5OU7SAhWJFuj7xS4v2Ju7y8iH7dyWsk36S8VEmc-wI50sBOI3vkEesWRX8Tz2Bvz4E_aKXo5MpS5OgSKZUM7ZmYerB29XKgMP3baocVANHsb7378crpC3HQbdySBPolIQBlue7dEOINFZNRbtJ5EORt9-57Yb3wPQmW-08kuECAthdCvdH5CQ3g_Ox1RF_VZ1d_wWeAIp3nd6smwMf46_LbeT6S2Sv4XZu2grmZVCBrdKpH_8563a5T3DIGXuTtS54bKoEt9nz_AVH-26iZugWME1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=Zqv7QoD0vzX-QLg079dgnUCACeKQZjK7au3295n4_iRLfTAF5DKuR6RHRfow5OU7SAhWJFuj7xS4v2Ju7y8iH7dyWsk36S8VEmc-wI50sBOI3vkEesWRX8Tz2Bvz4E_aKXo5MpS5OgSKZUM7ZmYerB29XKgMP3baocVANHsb7378crpC3HQbdySBPolIQBlue7dEOINFZNRbtJ5EORt9-57Yb3wPQmW-08kuECAthdCvdH5CQ3g_Ox1RF_VZ1d_wWeAIp3nd6smwMf46_LbeT6S2Sv4XZu2grmZVCBrdKpH_8563a5T3DIGXuTtS54bKoEt9nz_AVH-26iZugWME1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=qG6UTyN_M81YHqVPE_NlGQivQtb162sR-nr5HsUSxQhhZ62xI1PRCAjAN6MZSIRSH4pDRggfhriysUf4NqXNlgWfq9YHQBNGkoRAetjdIo5R1O6sFi3deT_JpP56wuLFjg1vGAS5qRtFN0h6Jua1qVzfVXzPkl7ukOrlTRjGG_D5-DfT3jOVEOK-U4nFAp-iv7H7by5JeI9PsGh25ywXhfi44QRvNHxoJMlhX0DWw-ZJEaWIWI-EULkSWGNI6Vg5sMkA8su54D2QSPFdK18S1jxpdDSlgc_CZcuFiDsnsOuWWM54Sv1dheObTMLIDRkQ1g6dF89GxqE-nSdxvqGcpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=qG6UTyN_M81YHqVPE_NlGQivQtb162sR-nr5HsUSxQhhZ62xI1PRCAjAN6MZSIRSH4pDRggfhriysUf4NqXNlgWfq9YHQBNGkoRAetjdIo5R1O6sFi3deT_JpP56wuLFjg1vGAS5qRtFN0h6Jua1qVzfVXzPkl7ukOrlTRjGG_D5-DfT3jOVEOK-U4nFAp-iv7H7by5JeI9PsGh25ywXhfi44QRvNHxoJMlhX0DWw-ZJEaWIWI-EULkSWGNI6Vg5sMkA8su54D2QSPFdK18S1jxpdDSlgc_CZcuFiDsnsOuWWM54Sv1dheObTMLIDRkQ1g6dF89GxqE-nSdxvqGcpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA1Ac1AYbaYlS-WlEXOiVNCiGZKoduUSbPo5Lu7h0xVYwreC6PspjyxI-E_An5mWwtyevvzeM9EWIbd6sdBVF3G34rqCexmSubMaDEDPMRQI7jU1fLgheECieyW634iImlsJGPWsd7ZFTDHtaawXVCdFOYT9UFbSyM8CI_tRVBlorZkp3lhWqrQtFS_RtTNS2LlrYCN6oYhuhrw3oY9f3AoX9-cJsy0fxqyzgptTHTnVOaIf4ZegBsPgu4ifWzbESdsR8CU0HQBgPA1NBYUhJpxJbAjo3a7sI1VXVBvepYPJqWgM0OZfzbLaN0ociDKgoPCG_C3B9jyFpKQCHkOxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la8nJkVM-wuCHHT8xB3H19YqjjzhKWTfPaU_lNBciCxArw_9ZC2lIRmslkAcp6ELoiGnDDBc0LNzDAqDix1EW-hu2kABDsx8yquJBe-kUx_HgHeNRywFs382FR8uHsY7lPvWTGkKwJVg0RL5OI4D-0gp8AM9ONGvJHXwZXVTE5zlpPMbQgPPA4UEeep0JK7lNUe7LLcByR_g7db1ZQDqzJdIz-7Fa-BROixPYtC7kkJo8a4bOMdKnLjmaxkg3e7dFgsceC-gn885Y1FGOUoaqR094tRW9XGwSni3xlZFYeDEH6ktFvsbNIQfEG6YjKymCixsWbaZjQnlh8UdEsMBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtWDNwtu31kVZXCIbdCY1mRjbtv_-LCufgd9Uk1fX0FL80gFo9yV4qGkKcUEczs0bykWd13HAUHZOVY9PaOq1Lrj0puMP-r4xAL7WyVXLeZ1mSSJm869pZ_eSDjxwU4YfYwGcfE3YZRt4rZnUXw9h8VZrwNTHlMvPLCYHMLAIUqPyM6X8NB7jiZMXbWPvFrMbzdJ2cvqw_GK4ZXgAuuMxltoGzalwg1-Ber8GMIpYY5jKHHXOrafsdLhNR3ncCn30b5ukatNx_O5cr2_JVgtcF9PuQKpnlhYzCOeidlqr5T0gdHcNJlhJNw5NdQdfeu_KLMh5_bjJ-P1R22DTV8bUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=tnSkWIVbOVMvzKuKgsHh1E_Ve2tAGxCsTlf6bCplHgXzhOUnwYwivhSVW6gZbI6UxCPe-MK7_p_LrwDe7IdnhjPQknwxDfGLVvz-QGlTsRPhrspzvQ6BbAggj-yKXttekiOmsiSE_aP_N-iOglANzQE_u-S_P_cUeVsK3S1MoN5FFFCMvkngQcgpvtUMtyP9nq50Fu80Xs29ENgbNFi9d4X9Kwo6aNdFyhfBGN9n2MnUKEA4bTD9vihLCHN99M92f1vtkkdtkwu6C6SGqVN1HRVlhU32XKWiOR4oTHN5hwtmFmKInCArmUkO48MD21pV8YXN-ZtKX08GCLRNoJhmhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=tnSkWIVbOVMvzKuKgsHh1E_Ve2tAGxCsTlf6bCplHgXzhOUnwYwivhSVW6gZbI6UxCPe-MK7_p_LrwDe7IdnhjPQknwxDfGLVvz-QGlTsRPhrspzvQ6BbAggj-yKXttekiOmsiSE_aP_N-iOglANzQE_u-S_P_cUeVsK3S1MoN5FFFCMvkngQcgpvtUMtyP9nq50Fu80Xs29ENgbNFi9d4X9Kwo6aNdFyhfBGN9n2MnUKEA4bTD9vihLCHN99M92f1vtkkdtkwu6C6SGqVN1HRVlhU32XKWiOR4oTHN5hwtmFmKInCArmUkO48MD21pV8YXN-ZtKX08GCLRNoJhmhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=mjkltXe3honxR_yWplcnH6NwFGUzpbWVyyHzQrNHTsbG3SvRangsDA60Wr3F3lx9pnU7p85OFexRKwSrdYIGd84brmkgMMU2ua96RsPiYsc5z4g5ODJ7t2YxMRW22GJ3tvcJEsq5XfnKy9l7TzbRucdhKdYMuY3PSjWXkiLWgWLBIBydxQHDnnArFCGsTFSq0m0yH1dl_IgJYt_Vp-6GHG_UPpZ5XSWVBmcqQxPaw7lugN1-6rx7VH40f9SF64IUQt5_SYZPf8BKaccNT2yumy-LCtWb1QG39-oZTPJKxclOzrYTo-0NU2_T602e-7QKbvOqSpO3cqKEosBGmLM2AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=mjkltXe3honxR_yWplcnH6NwFGUzpbWVyyHzQrNHTsbG3SvRangsDA60Wr3F3lx9pnU7p85OFexRKwSrdYIGd84brmkgMMU2ua96RsPiYsc5z4g5ODJ7t2YxMRW22GJ3tvcJEsq5XfnKy9l7TzbRucdhKdYMuY3PSjWXkiLWgWLBIBydxQHDnnArFCGsTFSq0m0yH1dl_IgJYt_Vp-6GHG_UPpZ5XSWVBmcqQxPaw7lugN1-6rx7VH40f9SF64IUQt5_SYZPf8BKaccNT2yumy-LCtWb1QG39-oZTPJKxclOzrYTo-0NU2_T602e-7QKbvOqSpO3cqKEosBGmLM2AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=oSgBNrui8FIRjXrG8FJeXezxOH50GzBy5PIIB61dWiMQukjzGE-2RhbWMJRvyJpGEkNA4i520WnIf-CRnwZ-zFSceue440HeicY7cbldr_O7EofH_F0fpbohAJy6xbto_N-YWCOOb3EkrZVvoXfk9ccjU-QBZzPcDI1X21CyWuZFi0xXvfE2rAdAG7KAGNH0sOf6RT-UrZZMuowjmtqvgNcN1QxI3lKl18jjPU4FwyXIG23NdN3Isz1yv0FJWpVNgOXcqTmglzAnA1Z67xkg0zc_5YcIUQ1JfJutrWhPWfYyDd8v8bOPWTn4Hb7YADFg6LqEWpmxW6omMQb9QjXspw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=oSgBNrui8FIRjXrG8FJeXezxOH50GzBy5PIIB61dWiMQukjzGE-2RhbWMJRvyJpGEkNA4i520WnIf-CRnwZ-zFSceue440HeicY7cbldr_O7EofH_F0fpbohAJy6xbto_N-YWCOOb3EkrZVvoXfk9ccjU-QBZzPcDI1X21CyWuZFi0xXvfE2rAdAG7KAGNH0sOf6RT-UrZZMuowjmtqvgNcN1QxI3lKl18jjPU4FwyXIG23NdN3Isz1yv0FJWpVNgOXcqTmglzAnA1Z67xkg0zc_5YcIUQ1JfJutrWhPWfYyDd8v8bOPWTn4Hb7YADFg6LqEWpmxW6omMQb9QjXspw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUzqEK7hCUjfIML5DKiflY_nNRFTxwdw2-6n8XftFLOYZ8AHazwwWzQX__lwUbGxN65Vli27bEKN8lzvNW68xxKd5xJU7sZsrJsogNm5-Ef27ZoFJxRfj_W26Vju6gI8WENRJi-coJsSh2qRuxkcfRUHmx7uebwlCsL7PIjqb1sYQtwu7-FxEW84CFOFPBKyHt6C-asWcYqmBMcA4Jq-Y3XXb4_6DgQ4CZLWKxXHWd391SSbwN_Lt0R6jhjCGA5c0pBUqeFKdto0Z7ZpTfVSah5-DBPR5b0mItwGk5VrALlLWyAs_coc5hB-B1coFiIMzU4j1HkZPI9zmrN91TyEQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=pyQbcK3V7Kz-ORLDV0icoHIkmpzcmLOK9qGEK3lCggPKeWoJuYH579At65fP1dBN91MyG5nvEuBLvHpKNJrsOB0LTwNMN0Qm0IzpLkJeqa8K27IJIG57mwoqxIljtCUiOypr5ZcCYzKaDxAQ269l1rrKaPBz39BmSnUTkX7mdUwVJX7HW2Td_7lDQGnOhN3JP4D_AJffbkveYlzMGkMmLp1P1cfB6VjjV6NVTFscgjrNlrmA_P1MttcrDGVdEu7CHyWSIi-ypJFg3Sx0FnUgkWmmwLEUvfdqPAdoE8N5YvhwxQ-ZyFx3jnV7H1hKCkiLm1Udbgalj9eY2YGQRbH2Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=pyQbcK3V7Kz-ORLDV0icoHIkmpzcmLOK9qGEK3lCggPKeWoJuYH579At65fP1dBN91MyG5nvEuBLvHpKNJrsOB0LTwNMN0Qm0IzpLkJeqa8K27IJIG57mwoqxIljtCUiOypr5ZcCYzKaDxAQ269l1rrKaPBz39BmSnUTkX7mdUwVJX7HW2Td_7lDQGnOhN3JP4D_AJffbkveYlzMGkMmLp1P1cfB6VjjV6NVTFscgjrNlrmA_P1MttcrDGVdEu7CHyWSIi-ypJFg3Sx0FnUgkWmmwLEUvfdqPAdoE8N5YvhwxQ-ZyFx3jnV7H1hKCkiLm1Udbgalj9eY2YGQRbH2Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=rPd5z-KBTE4OzmldUUeguAozlyrN51qD3aWnbiNQEz7N_mUiCOaVHM0SJT0mkEqbb7Uprp-Bkj9HUqAjLz2c_X4Vh7Uc6who1VjnnCbc9f44c5tHRNyfucBoo-j3Jn70nujWkoaMvm6cFNrc89ppL-IVyv6FzmfN5bLpj3pCf6ixdSSX1iJedJGWfy-dyhDBcLFHzBl6u9b_uHkSDLlRTsXXyrO8onRj5CO1RHpJTcJinulKByRlFp23ylhbd8pMfTCQ9RR8vcopvbOvBigXBUuCqBzcNyGQ_q1xvOCgac95dYZGxy5DkjLOIGWowQIYvm-0vis1RuXUPTrhMM2DIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=rPd5z-KBTE4OzmldUUeguAozlyrN51qD3aWnbiNQEz7N_mUiCOaVHM0SJT0mkEqbb7Uprp-Bkj9HUqAjLz2c_X4Vh7Uc6who1VjnnCbc9f44c5tHRNyfucBoo-j3Jn70nujWkoaMvm6cFNrc89ppL-IVyv6FzmfN5bLpj3pCf6ixdSSX1iJedJGWfy-dyhDBcLFHzBl6u9b_uHkSDLlRTsXXyrO8onRj5CO1RHpJTcJinulKByRlFp23ylhbd8pMfTCQ9RR8vcopvbOvBigXBUuCqBzcNyGQ_q1xvOCgac95dYZGxy5DkjLOIGWowQIYvm-0vis1RuXUPTrhMM2DIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7tpMtnRkHKZPrcAgT-tMlQHUkLBm8TKQL5wh7pEI6WmUpe_F7Nsf-FsapShO-STayp8h_S0Q2FwuNaDHT79J9kpaDS_HGN_zFmzNMSAqfsan36u2qoH39bE2d6q5swFWmAMteu4ULKeFYOslFcpflNxhh2eq-n69_0FnRgGCx4Pt8QFedDkYYpACxrkjb6RXLJ6BO_a0eMtjaHD0WgAmOZZ64-w1pO9m0ax7cy4DOs0jEZ7s7RpXNbk1CxOX8Zy5GjdhSBXAHv1QOIzrQU_Pyg8T581J2LdjNlLNOd4FPqj21Seu9JEfijkN4WL26U4JQ5oJvkJy1xvDyVJ1VEJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=qAVKgb2iyiACXFlGfSgOQEs9HDwlczUzBFU9THEL8OvB8qjdHeLkwPohjFp7sA9IAobzxupZs0jG6PpW03LKXoxV-QvbP61dD1WvMQYEiitRbJS2eQ1LrILjzL-ZD2HPf-33w4771QqAN7lcgJa_2d7AizUqb6jZZ7wwHZqYwomq4LQexLQ79DjHSLMruv3K7Lki-tNzSUAE7q45y7qtof4oGCZg3IakXXdqU_HcVtL2neRqiLBKq0QRcSAZkWfTGqeCrWBJdxXZPR1B4W25n-3VEJaQa6Wsj2LnjlOd_O1hKTkiy9ccOJQcpW3Vux5uyTeneHYb6E3q4_X3jPA_Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=qAVKgb2iyiACXFlGfSgOQEs9HDwlczUzBFU9THEL8OvB8qjdHeLkwPohjFp7sA9IAobzxupZs0jG6PpW03LKXoxV-QvbP61dD1WvMQYEiitRbJS2eQ1LrILjzL-ZD2HPf-33w4771QqAN7lcgJa_2d7AizUqb6jZZ7wwHZqYwomq4LQexLQ79DjHSLMruv3K7Lki-tNzSUAE7q45y7qtof4oGCZg3IakXXdqU_HcVtL2neRqiLBKq0QRcSAZkWfTGqeCrWBJdxXZPR1B4W25n-3VEJaQa6Wsj2LnjlOd_O1hKTkiy9ccOJQcpW3Vux5uyTeneHYb6E3q4_X3jPA_Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=NEUagFprsBxyje01mPgtrF1A669NZJzwMPvmy26PJnGb6yNIZUQ1qk2uxrO59b3vi-pgVLdjOXdGHP6CYVWZcSIsoLFYcOxfWWP_0k5c9k-m17sDywAt35B7Lb2P1aM07BbtfvFwsDBsoeigU-59lbF6w1Exe4aPH_B9GmoJncl-kYunO6HT0sSnoIVfiUOYlL3PLREnBja1wV1iAXH2fQF0qqf5zjuXM0cVLpJaiuu-yQvml9sfuui4ju03ul2WvlHZQXgGTU8pBCpS_oh0uB8gUAXhoQtaJlQSyF94OGKNlloAHayCkzkHtFWXzIYVc-U3A_fIioJqJm5WHrd9fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=NEUagFprsBxyje01mPgtrF1A669NZJzwMPvmy26PJnGb6yNIZUQ1qk2uxrO59b3vi-pgVLdjOXdGHP6CYVWZcSIsoLFYcOxfWWP_0k5c9k-m17sDywAt35B7Lb2P1aM07BbtfvFwsDBsoeigU-59lbF6w1Exe4aPH_B9GmoJncl-kYunO6HT0sSnoIVfiUOYlL3PLREnBja1wV1iAXH2fQF0qqf5zjuXM0cVLpJaiuu-yQvml9sfuui4ju03ul2WvlHZQXgGTU8pBCpS_oh0uB8gUAXhoQtaJlQSyF94OGKNlloAHayCkzkHtFWXzIYVc-U3A_fIioJqJm5WHrd9fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=LqaYd4tp88m9PMxAYxjVbN0l1hKeukQgxN1BEoJCCDo2dvEYVG_t3YnvIpB5fsxZ5V_0ENeYlM7qTMfrqF02SfWIz0HOtH2VWzs0G87A1Siq6HGeN-CkieSoe2__5zTn2XhEuxL-tHHyBVQsXauowUUk8KZu2E6XvACkL6P7EBZIZao3xrOm7eAc8cgWkFIEl6DZPsFYQycks2_wCCz3oOKxBMARLdr-75BN4HT9AxXqFMKqVXLZ9XTDechZOP02YSQvqfxkzYvi7gnGg3uQzBahVqkW409Z2o0iiW8w-5J7GRuDvBWzQrhDPbUlv0RRjfjS3A2dtnykT_rMA-eMvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=LqaYd4tp88m9PMxAYxjVbN0l1hKeukQgxN1BEoJCCDo2dvEYVG_t3YnvIpB5fsxZ5V_0ENeYlM7qTMfrqF02SfWIz0HOtH2VWzs0G87A1Siq6HGeN-CkieSoe2__5zTn2XhEuxL-tHHyBVQsXauowUUk8KZu2E6XvACkL6P7EBZIZao3xrOm7eAc8cgWkFIEl6DZPsFYQycks2_wCCz3oOKxBMARLdr-75BN4HT9AxXqFMKqVXLZ9XTDechZOP02YSQvqfxkzYvi7gnGg3uQzBahVqkW409Z2o0iiW8w-5J7GRuDvBWzQrhDPbUlv0RRjfjS3A2dtnykT_rMA-eMvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iccaAajgw7Xmt8KhP73_iKthx3zXhDjpUkYrPOPzQBgcb7YFsgJvJGJ-DmWS8o2e1V_JB04-sr1xEMWnIQhhh8u4N0vwTcl2OA9JxtFY6lh1BJ7z9Y1Q3sK_he3rjZu1ek81mGRVfMBy2KtwCT8_7Pn0A5Kp4ixhpOzINyRlwbAzqfkH5yXB9Kj_leojsyVrwddzNmqrxAmUuvVAJefJx9CVrvKb3j39zUQ6D2_LG6rfp_OU2NBbtewWPDjJeIlNrCku4Knf2r86twWUcPeCsHVp1KQFVgbNI8fk0pf0PcqoroicoWEUOCY7_3ro4u854fOKwzsHJGtohT_jon2h1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=vbaNSyDNvFakXTAKkUuR5knF4j2zckhr9myY1iGjhhRTjAHPrzMamfWjsUztp89dt2Jj3nM6mIGWDgK-nC41GfheJquCeleLLXR4CM6jgQ6FSggomnsc6U5pcKWR1glV4vwjXw5NpMHEPAIFwH2376JHkUBlNm2WUmUXd6LxmBWJD_rcVAaNRra03p3kIzvFA7lbzhABcUNghkCxlUEjvkn8cOWvK4eCKajqkuBcheY79qKsfaaVgnVgP2HPFaR9xGXT-bhmkRjy_lttoi6JVBfmpACcO8tGsuUyTAuKOI0yTXvOHeh-zxHgqDOp2x68AVcI_NUs14xtjMjzh2MvFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=vbaNSyDNvFakXTAKkUuR5knF4j2zckhr9myY1iGjhhRTjAHPrzMamfWjsUztp89dt2Jj3nM6mIGWDgK-nC41GfheJquCeleLLXR4CM6jgQ6FSggomnsc6U5pcKWR1glV4vwjXw5NpMHEPAIFwH2376JHkUBlNm2WUmUXd6LxmBWJD_rcVAaNRra03p3kIzvFA7lbzhABcUNghkCxlUEjvkn8cOWvK4eCKajqkuBcheY79qKsfaaVgnVgP2HPFaR9xGXT-bhmkRjy_lttoi6JVBfmpACcO8tGsuUyTAuKOI0yTXvOHeh-zxHgqDOp2x68AVcI_NUs14xtjMjzh2MvFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
مقدار قابل توجهی از هواپیماهای باری نیروی هوایی ایالات متحده (مدل‌های C-17 و سایر هواپیماهای سنگین‌بار) امروز از اروپا به سمت خاورمیانه در حال پرواز هستند.
برای توافق دارن میان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=n-wCxJXbKilS55A9EHiyOKy2g4pJTP_yyDNIb8fbw_3_QHl3gmJju6yKfyMaStZTrxdTeryBE5kMpPgX0HJIKpgJGXQn0HyQvC14imx4R18GU7FjtLRMXCHJKc6uNlPzk0vzlPptPooSvmFxtWK0aNmHjHdMxUGbTqJjCeencwzVSgkRbjVAxX77sCmirWnlxhKRevndQ2qSgFQxUgtuTtfqDPon1f8XrhOEC18MgK5WWu-2_sZG8y5RTPAqyLmpGtttWpn6ql5VyIpCOpAq1fMNno4cgh1Hl7BcDwQNAuxUPJR_5nY_eib8tWzgf_pdbnEgG9COlJrBDBWTDKUpXIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=n-wCxJXbKilS55A9EHiyOKy2g4pJTP_yyDNIb8fbw_3_QHl3gmJju6yKfyMaStZTrxdTeryBE5kMpPgX0HJIKpgJGXQn0HyQvC14imx4R18GU7FjtLRMXCHJKc6uNlPzk0vzlPptPooSvmFxtWK0aNmHjHdMxUGbTqJjCeencwzVSgkRbjVAxX77sCmirWnlxhKRevndQ2qSgFQxUgtuTtfqDPon1f8XrhOEC18MgK5WWu-2_sZG8y5RTPAqyLmpGtttWpn6ql5VyIpCOpAq1fMNno4cgh1Hl7BcDwQNAuxUPJR_5nY_eib8tWzgf_pdbnEgG9COlJrBDBWTDKUpXIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTZ55D3bnbqPVC7kyc_btBATI_0PaH2nIHcqLHWwStsthJG5sn_62O_qZlp3y2KweCKe-Ls1NtujoE2w972kL06MuRbPae2X2wI0IbhXi1eLRpa703BKX0HA-EC1NfcH5vOQzww-9eoymUN6YrYciCrUpf4Qh6Kc_SYtPPh67Ip4lxO2NlcmrPEbZcp-c__aCMfVA0lEPm2dVuSW6xclSoEq-4fhFo19ixCbMzjkHaYFSlB3yWlydaqrF8_DjMJMiWM2Zhz5cJ-lJso2qO0nC5_l02Ksr0A5_WNm6Fbr8H3TAq4M47HfqgSnN1M5sJQBuruoBkgN0OqfvsS2pz460w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GV7UFmYGJoEb7y-fUZzHrdEkWZGr1Xb09bzyvQEqSOZndjnjApPaJGA6nKzal7YZHNZzrnl92ReaUOmYtb1TnTTV1ycmkGMwA4_eN0lwq0QbX20eqNVdfx98gcD4a02mip1qUawc4BAaODoBqvt8aRqOL6ghagDjyO1Z7kfgE2xpYM6SP2w72rFFlEYSX1GBFk3UmYVTNEY8-_l78_9WzdxbZ30t-cDVA5Jl_4ZKIxhiVotRBPMQIpOAyWlgqdBYd61MTqpdmJ2d8LO43ZnJT3tR1f95cLJ1387jeDRfcRrjbe5-xEIa9eUqtoLMmKs-l52NZK7t60Yo_Dw2U1T8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLrooYrS6Rhd8qcgF8s4vUVWeVlJAPRutVylsBWdc71gAnOWnNZV1Y_0_qSWx5W5AlhWZkUXQEwJnMY9GAKql_QSm69eB6Pe6h-62Ugu-CMqxzxcTlPP-UPFwBZ-ioCbXMdsVQFPVfhdwpUqsYuFbWAm_4bW30NRJMnoS33p6A164qYu51jrm250SAzAqvM4fuJU8kZENQ07dSYILQc-5qt0MVgftZ5t2Sb-RNQxHSExl_nrMw4wuKX7RFKhJ0KAB8J3ap64Ro5T37ttc_-WaozA-CLu0wMv3SXkq_dBbesO2uoEjoru308dS7za_V6T_67PHfZF0ZiUyayQSy4biw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=CxYWwYCspGHxcSyUNZakV53ozf-3Xddh3ZnDUbFRFfzwoEkghltWm7Slt0lGvMrPSIGe3l3IVSVcGUfXgR-8i2BujyYLeiDg9WNkCYD-sSPy_UIijkDPZMeCXXTmDVPUQ7hPlYxXGQ7uPiwGB2x8VHAxedNhlBgnO54QqMmWBaeYP5xQTQ2jSASiQylYBays8mVHUCI1TmgcuYCNnIRtI32tH7uJ1W3e7qgAR72bTxfSvrzXtNP36PK5lOS5QPQwr_jS5FXL3oB78UrZOz0GITXEKOSv5YKutYETccFcU3TG2tFwEtJiZCE2V-pgEUjzkfwUYee6Vr6TqpYHEM46vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=CxYWwYCspGHxcSyUNZakV53ozf-3Xddh3ZnDUbFRFfzwoEkghltWm7Slt0lGvMrPSIGe3l3IVSVcGUfXgR-8i2BujyYLeiDg9WNkCYD-sSPy_UIijkDPZMeCXXTmDVPUQ7hPlYxXGQ7uPiwGB2x8VHAxedNhlBgnO54QqMmWBaeYP5xQTQ2jSASiQylYBays8mVHUCI1TmgcuYCNnIRtI32tH7uJ1W3e7qgAR72bTxfSvrzXtNP36PK5lOS5QPQwr_jS5FXL3oB78UrZOz0GITXEKOSv5YKutYETccFcU3TG2tFwEtJiZCE2V-pgEUjzkfwUYee6Vr6TqpYHEM46vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای تهاجمی اوکراین در یکی از بزرگترین حملات از لحاظ حجم آتش شرکت بزرگ تجارت الکترونیک روسیه، Wildberries، را هدف قرار دادند.
این تأسیسات که در شهر کراسنودار واقع شده، به‌طور کامل در آتش فرو رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=RDfrnGkL08yoxPqRvinCcGRrjxW3P79G8sIvhSJNO2VP0U5UA_-3AkbPbnIazZgapAmQyF6oSjh8GqUDSv0u2Ul54NDl57nRN-1smz-UqbHmTI4netDY_OQJez6RadWM1ESA9BFBxhX2ijzsCTPItwtZj6Sa2q14Gs393yFbIuA-3mXc6SHnrQUQrHw2TCIwRcf8IGaFSFYA-QKsPxzSGO0Bp-0PyFOVmMgLdh_tL2l3DAtZnHTbqfzOt7_moL4WArBLU9HJnv1yCKSeZ5uWFSx1j-QbqxuekOPMRh20ZcbJ_YSMWkrVP5XB-oLDS-ol05y8Cs4DoxQgFnOk7JI9Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=RDfrnGkL08yoxPqRvinCcGRrjxW3P79G8sIvhSJNO2VP0U5UA_-3AkbPbnIazZgapAmQyF6oSjh8GqUDSv0u2Ul54NDl57nRN-1smz-UqbHmTI4netDY_OQJez6RadWM1ESA9BFBxhX2ijzsCTPItwtZj6Sa2q14Gs393yFbIuA-3mXc6SHnrQUQrHw2TCIwRcf8IGaFSFYA-QKsPxzSGO0Bp-0PyFOVmMgLdh_tL2l3DAtZnHTbqfzOt7_moL4WArBLU9HJnv1yCKSeZ5uWFSx1j-QbqxuekOPMRh20ZcbJ_YSMWkrVP5XB-oLDS-ol05y8Cs4DoxQgFnOk7JI9Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.
اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول از کنگره مجوز می‌گرفت. اما با رد شدنش، چنین محدودیتی اعمال نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQuDvv7XpBx-7XlLuNZoYMFiuDI2NRnCgymkaGqXew825A5ibo3BS1b0yxtTYwPPY8I0DQkyye2SRniiIiuGiU825Da8vQ6nk-HEkN3Z4F3Zdl3DTYLIUlcJtZLpDeuFaK5wffvaxTcFhTYrwY9w---92dUSOCx69Uqijj9lZFufVe7Pr6BAK1ve_XUWQbzqCe2wAj4amdc6yEahEN_T-xgCae3UssU7_RKt1FlS0N5XEqDZD2V09WxTNAy_Dm9STn1LSTIcKtrm3v5ZMQrOiApsGcpbEAUp0w-11bPOY70qSQ7CnJKOhqW1Mhsg_faWL5nBVZyCBD-P5E1Gpmn-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=RPVboSO_1QWPg8ods-OI6MoS8nFSprOcOPPj4ouLs5cgv5hP5PI0PY1TGMpBQd0CUabk8W3D-u_OVpZae6nJfDWlWt3xgj-8usjOGRb_ayI7EhmvHOwBJj8nr1F1J4JlTS3wAg8s_SLGecd-jSenz5Paomo7m-HZID2BHhmnaB4cMX1-HprpkmsF4lcVMgnneSD12rf6O_2PGTEQPIJB3hh_HEwajGVh9AH3wUhd3P8MP3scr8EZl79Q6ClsA3asbn0JowU2WwI0hR9vldCnRnpT6tt1LBCzWv_5wLlUjispVJfemSzvFfJsqRPAcW-Guu4ErJ3uniWrJxmQxqyFIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=RPVboSO_1QWPg8ods-OI6MoS8nFSprOcOPPj4ouLs5cgv5hP5PI0PY1TGMpBQd0CUabk8W3D-u_OVpZae6nJfDWlWt3xgj-8usjOGRb_ayI7EhmvHOwBJj8nr1F1J4JlTS3wAg8s_SLGecd-jSenz5Paomo7m-HZID2BHhmnaB4cMX1-HprpkmsF4lcVMgnneSD12rf6O_2PGTEQPIJB3hh_HEwajGVh9AH3wUhd3P8MP3scr8EZl79Q6ClsA3asbn0JowU2WwI0hR9vldCnRnpT6tt1LBCzWv_5wLlUjispVJfemSzvFfJsqRPAcW-Guu4ErJ3uniWrJxmQxqyFIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ساعاتی قبل سپاه پاسداران یک نیروگاه برق در کویت را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=aKu4TAhuTP_sHjS-fQ-MP_fFgFvhpbGYUUbgAPA-Wz2_jyA0ltK77Oj4_HgIYyGSM_6m9WrMtKYp-BCSE2qnNSLosf3zjUdFbERC6vGD78sSTYlU8Otp43u-su5gQFuaLLYifIdywIC16YLqtg78NvXfAgGNlsZt1pihajbwU0l-wWBCoxZneUWvEHto-WVKkuYEVXx1CFhAR_fBrmgg-wME8bddGnldjKhnM54zQengwCR9CS-4579K8VcQMWVaWTdZq9RmwwBy8SImnD2WmFwv4pjyDqiDD8RdO5YT1g5NdKizofx1_RDADW_Y61PHcbY3YEdqffCrjOfQ983Nsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=aKu4TAhuTP_sHjS-fQ-MP_fFgFvhpbGYUUbgAPA-Wz2_jyA0ltK77Oj4_HgIYyGSM_6m9WrMtKYp-BCSE2qnNSLosf3zjUdFbERC6vGD78sSTYlU8Otp43u-su5gQFuaLLYifIdywIC16YLqtg78NvXfAgGNlsZt1pihajbwU0l-wWBCoxZneUWvEHto-WVKkuYEVXx1CFhAR_fBrmgg-wME8bddGnldjKhnM54zQengwCR9CS-4579K8VcQMWVaWTdZq9RmwwBy8SImnD2WmFwv4pjyDqiDD8RdO5YT1g5NdKizofx1_RDADW_Y61PHcbY3YEdqffCrjOfQ983Nsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__LvV1603-8DD2nL5wo7LWMHnx7vWeW0wEVVTe6XPofLSkGylmUbo2EDtU_QGEUPXdxMgmG-CaWyeia2S9vsOkHZPnIP1Z26kKRUkCucyGnj4GXwjXFkGmynzSKO4WOIPyALkIdo5bRRixlztle5ooiPWfxNStkNYQ81qUY4U700xRpiNAuBOZvElIUvPK4qJE573cblNAztRoorKHPEzJyVIBUFzgRReJvtfJCju8RkU1iCW5DIu0rLtEVzjqhPGo0cB0zLopkFeiX1T9G0MVETIhXkYhY1JGrRxyKZG8wmf0EYqyBalv9dnAMQ041agbcsD8z3op8tnk5LXB7OovyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__LvV1603-8DD2nL5wo7LWMHnx7vWeW0wEVVTe6XPofLSkGylmUbo2EDtU_QGEUPXdxMgmG-CaWyeia2S9vsOkHZPnIP1Z26kKRUkCucyGnj4GXwjXFkGmynzSKO4WOIPyALkIdo5bRRixlztle5ooiPWfxNStkNYQ81qUY4U700xRpiNAuBOZvElIUvPK4qJE573cblNAztRoorKHPEzJyVIBUFzgRReJvtfJCju8RkU1iCW5DIu0rLtEVzjqhPGo0cB0zLopkFeiX1T9G0MVETIhXkYhY1JGrRxyKZG8wmf0EYqyBalv9dnAMQ041agbcsD8z3op8tnk5LXB7OovyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVzzsIsmsl5rZyjbeiylwaKKM7Hf4J3XKbltc6kA2F_lqRdvTFjjfAZ81_BeRoMvsfDKutST7GbZhd4WbnHMxvW--vMWa1rbAG1yqJmJXxT3e5AtGVqdOXEYWvOSRx6N096Fq8tH8vXzVsW28q_Xs_30epthX3fYUCQRYgtnjDAmPAQ6oauw3Woo8-TlpGk0soRcuIzmSONuWDTj4-aATeiT9FRr-JqEjEK24Abu6a0W-PeT3AK7V4XxMtEMF2pqJ2o92g1vUUOcKUdqHUUZp2aOqFaeiEmacYMmlLujEvUYEOTsE2AjcAtn47qqNTPKuvpMLnGe5hrN2WHmqncitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ2UTyZQX-paGjrUiH3g24AAdkdSXoN5tcCJZMp1l7pE73w14MFad7QlghX_0FkrexWbyr4ZMD2xeQbx8fewlhwN44rW2A6nEqvyu9nDiTYxYoWYoz6bavAjeVogWiCawh0P4BZHQlvNE3GFuF9l4IwiinKt4EbfvHL9ZH9HjR0rDl06qUX1rOHnS2lqCfBEeVpfwlXnK8ft-DhISJRrc34pc8iPQe6tVX3QnSVs0SoXu3Z-K_LOwZgZQCKcT9efIbrbw6Blb25_cZVkSxfzibwtvGt3CkLS4e14V5fnoUCnaBVtBUTXfkj08WDExpMNb5yvhN3mp1P1Gbz4YZ7sIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آنها می‌خواستند ایران را تنبیه کنند. در عوض، خودشان را با نفت سه رقمی تنبیه کردند.
استراتژی ۱۰/۱۰
👏
👏
👏
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68867" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68866">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=iIYXnqijtDVlENQeaBwDuGbGHOkSoOe_n0-2ZJAQ_Rf5G_SPXsqJU4ydvPz78HiBjnc3s5dNx_MNvSGB2H5GiPZiWCwB026uRXUdIIKzZ6QlODCsk8eQm8c7DCM5VHy4JUI_JwShjd2zVLaurgwkv_bO4U0jt-uM2f8kn3-NJ1IusAVATy4_gp2tLTsXuh1GoLmtJUWAzrRVJ94p3-qQMc23QuspVtjAr66ZvcPNzTfS8Si2sm4Dvzz9Pu-LjpNAPVzKV9k1rM8oONR0HdW7t3KGFP6oP4qBIi0c1MMESvs_Qov1yGM4PW9sYXW5L7igrmx6w6fB8gqaSWelv-usjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=iIYXnqijtDVlENQeaBwDuGbGHOkSoOe_n0-2ZJAQ_Rf5G_SPXsqJU4ydvPz78HiBjnc3s5dNx_MNvSGB2H5GiPZiWCwB026uRXUdIIKzZ6QlODCsk8eQm8c7DCM5VHy4JUI_JwShjd2zVLaurgwkv_bO4U0jt-uM2f8kn3-NJ1IusAVATy4_gp2tLTsXuh1GoLmtJUWAzrRVJ94p3-qQMc23QuspVtjAr66ZvcPNzTfS8Si2sm4Dvzz9Pu-LjpNAPVzKV9k1rM8oONR0HdW7t3KGFP6oP4qBIi0c1MMESvs_Qov1yGM4PW9sYXW5L7igrmx6w6fB8gqaSWelv-usjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8rwR8eA1N9Gw7xvi3vX_hFW2_kHmsoaT8n3s6eBx4_r6N7-uiUOjqD-3Bh0BzC3fx5cgkYvfldSh14QEg9aO3lV3eBtwlphsJ1wlQ-uBNSwj0-puY70iwhLQ0KcbFpXENBRmqNSsfKoM1KJ_RUqKxiDii2MGrAcuHhQ0o6sUsa6UA23Xgk7s5-7W9RSXw1KTtqNAjBCKKtN7rNDtADCcbQT0fjAJ7w0EOp4o7w4VMovxpo8GkI8ubwJ1_e-SuWtI7pT0Rw1NUXkZdyVbwvKVb_yhlQW-sOhfhhHpFAqZchrWtvvQMCE0Wh3PJQaJNh2UgFq02ux591zhA0yaJ3Vkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68864">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ همچنین گفت:  همه چیز برای این حمله آماده است. اگر از اسرائیل بخواهم ظرف دو دقیقه به ما ملحق میشود اما ما به هیچکس نیاز نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68864" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68863">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری؛پرزیدنت ترامپ به کانال 12 اسرائیل:   من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.   @News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68863" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68862">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K42MY2gKIkNv6_1mWSh8ZjDzVfqi3oGQW7o70tTF1kOna8EXf4b7FFtDofXQaSHL-9dm-52zXk7Hjo-T8v6feHVfn7oca_iSQa8lvS-L5h7EoXjBKK5bWfMZPN_bfpXB-TvGruB2aq9orvrZOAxqP6VHnqa99WNegMT89nIQXPzGq0yJ6hGSJLFzPFTIZyhkbWOiL2g_obQh4cpVgnmf0nEMsBLJboVn3ShhQ9h3QFeDDvr4fCUYFNhlmrJUF6nFrmIJjaLetsxam3NRtufrQ9vy0rLsIpatD4xeMQGTz12XYqQGGuOdyTFFsYcruh8_si4TJereS0QKnzOaf2SZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛پرزیدنت ترامپ به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68862" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68861">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=OIcvT0oO5UjHpRLQWSjpGUHdZ4__0RgD9vnPDy8A7szqBK57qYc-FtDnfpqsF7lZcNmzCndldKW9nN3ViUfDOlsVfP_yOz7dPs4UDsqi55uUsldJwvWB4Fd_H-QjiPOllB_KeTZFQ51Nd7Oi5mx8vTinBFvkx0WkChDEv1yzVK89gD8Qls7JAh0QLMWwhgR-5DGSR25SDcjfHrz1IFMNZAz9pfG8HQfMczROxvYBh_fpfzdht48m9hqdhOVY_fFQ7i9ZCZ4Eq1oShB_dSbIIn3Clx27sSC8JVXMIxNLB_eKfX27JaF9usLGdOdh0cGfQI_XXQd9tBX_SEm0fmyrLXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=OIcvT0oO5UjHpRLQWSjpGUHdZ4__0RgD9vnPDy8A7szqBK57qYc-FtDnfpqsF7lZcNmzCndldKW9nN3ViUfDOlsVfP_yOz7dPs4UDsqi55uUsldJwvWB4Fd_H-QjiPOllB_KeTZFQ51Nd7Oi5mx8vTinBFvkx0WkChDEv1yzVK89gD8Qls7JAh0QLMWwhgR-5DGSR25SDcjfHrz1IFMNZAz9pfG8HQfMczROxvYBh_fpfzdht48m9hqdhOVY_fFQ7i9ZCZ4Eq1oShB_dSbIIn3Clx27sSC8JVXMIxNLB_eKfX27JaF9usLGdOdh0cGfQI_XXQd9tBX_SEm0fmyrLXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من بلافاصله پس از انتخابات به دیدار ترامپ رفتم و با هفت اسلاید بزرگ به آنجا رفتم.
اسلاید اول، اسلاید دوم، اسلاید سوم، اسلاید چهارم. "این کاری است که ما انجام خواهیم داد."
نه اینکه بپرسیم "آیا به ما اجازه می‌دهید یا نه؟" بلکه من به او گفتم: "این کاری است که ما انجام خواهیم داد." و ما به اسلاید آخر رسیدیم و من گفتم: "این پیشنهادی است که به شما ارائه می‌دهم."
شما بمب‌افکن‌های B-2 دارید – این بمب‌افکن‌های بسیار بزرگ. یک مکان به نام فوردو وجود دارد. اگر لازم باشد، ما خودمان نیز علیه آن اقدام خواهیم کرد. اما بسیار موثرتر است اگر شما بیایید و به سادگی بمب‌های سنگین خود را آنجا بیندازید.
او گوش داد و در نهایت موافقت کرد. من بسیار خوشحال بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68861" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68860">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008b12665.mp4?token=LPdljC_r-KeRiqLCZCoNwEzjLK6QOV0mhKQVQKy-zX7AID-Cn964XLTEdKkrkfoiqyIkEnfc7I9Qo1HBEiWupMS6oE_fbipgY_UydcqyZ4cBZLjXYfDSar4N6lprhzIQlPlCgSP0DwUy6BgMV6DfdtIzReXyxtD5PmxU_XA95F2KLXVoj8k_usE0H91ffby72fVBzdjg3BbM_sswsoU69A8Fw5lJvNNZmQe6pAIduYN7ZE2tZyaSqruZdrEUcRHuum_TA5mEzFuA7rnSnvXrVB8hes1lcYcvh-FCnbD_uth1izAtOq_TBbew-xqoA8w6BP3e6P-jjmc9A0QApojK0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008b12665.mp4?token=LPdljC_r-KeRiqLCZCoNwEzjLK6QOV0mhKQVQKy-zX7AID-Cn964XLTEdKkrkfoiqyIkEnfc7I9Qo1HBEiWupMS6oE_fbipgY_UydcqyZ4cBZLjXYfDSar4N6lprhzIQlPlCgSP0DwUy6BgMV6DfdtIzReXyxtD5PmxU_XA95F2KLXVoj8k_usE0H91ffby72fVBzdjg3BbM_sswsoU69A8Fw5lJvNNZmQe6pAIduYN7ZE2tZyaSqruZdrEUcRHuum_TA5mEzFuA7rnSnvXrVB8hes1lcYcvh-FCnbD_uth1izAtOq_TBbew-xqoA8w6BP3e6P-jjmc9A0QApojK0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری:
الان تو دنیا کدوم کشور با ما دوسته کدومشون دوسته بجز مردمشون؟
⏺
ثابتی:
اونام دولت هاشون مثل حسن روحانی تفکراتشون امریکاییه
⏺
شهریاری:
توهین نکن حسن روحانی امریکایی نیست بعدم تو در حدی نیستی بخواد بخاطر این حرفت ازت شکایت کنه اگه تفکرات روحانی رو امریکایی میدونی یعنی تفکرات 80 درصد مردم امریکاییه..
⏺
ثابتی:
کی گفته؟
⏺
شهریاری:
کی گفته؟ اگه جرات دارین رفراندوم برگزار کنین تا مردم بگن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68860" target="_blank">📅 18:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68859">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇮🇷
هشدار سپاه پاسداران به انگلیس: بیش از این پروندهٔ خود را سنگین نکنید!
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68859" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68858">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUYmazaMOcD-LX1M7wUlwhvH2TDUSkon4_VymqLutycgAWRn3TG2WnGdRgI5B3229lGUdaCRBlg3kd49idwNk8FBTnmU0uzYrQ8CcMVy-ZVXNVv8_xanDP5brqdNeCRqwafrK5F8RsXIH2HJDO0-7w5oV-h-CtCxtuE2noWFbw6IbshfxL6BcMLJsM6BYI8rBsxBaBiZMTyi4clBGuDN7oiIBDBiuQRmvK12TKUjgUE7CcsJQOW3yEE4vpGtDAjOEWxbfe06aZGYTv-9cajNSI7icUafDj_9OsZGUybDy9ZR_B61fRbcwkYUEp5kYUI7reOBrWKG7Xq8tdYi-QUGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
نفت برنت بعد از تقريبا دو ماه، مجددا 100$ رو رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68858" target="_blank">📅 17:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68857">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQAblIL40badJjaw0g4tplSmxkU7ospb5viKXElwI5BbTFBMegYNsZs9xPDM8oRXmPF5J2XuqNpg4I1lvPiQHeghHTrpo1QRH11j8dLfzopiuT2jFNHo3B69FOF7j2KV-HeZPyI-cd5EBcU4N-EULysq4Goi2WVhu5gZQPDAyfrLjvGJat2Dv_HzXy1WQH5ErCpu8a_uggJs_zKPdMRYQy11VLnDi5vIcCfWIPaiC4MMlDvn4zs_tRy-Kka4QuHcHVBwiztdunGsFw7xKZYWsi2IP2IlLGJLFYEA_nG_4KRRiGjmffUKI8p48RSwDbgwGFALY8rA3g3EwWBQjW7ysw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس:آمریکا هم‌زمان با تشدید حملات علیه ایران، بمب‌افکن B-1 را مستقر می‌کند.
مقامات آمریکایی اعلام کردند که ارتش ایالات متحده روز سه‌شنبه از یک بمب‌افکن دوربرد «بی-۱» برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران استفاده کرد.این نخستین باری بود که ایالات متحده از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش، مأموریتی با استفاده از بمب‌افکن «بی-۱» (B-1) انجام می‌داد.
استفاده از بمب‌افکن‌های «بی-۱» — که قادر به حمل ۲۴ بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز هستند — نشان‌دهنده تشدید و گسترش قابل‌توجه عملیات نظامی ایالات متحده بود.
هواپیمای «بی-۱» (B-1) می‌تواند در ارتفاع پایین با سرعتی فراتر از سرعت صوت پرواز کند و در عین حال، سنگین‌ترین محموله بمب را در میان انواع هواپیماهای بمب‌افکن حمل نماید.
در بحبوحه تداوم تقویت قوای نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان بازگشت به عملیات‌های رزمی گسترده علیه ایران را مد نظر دارد. مقامات آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68857" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68856">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=bzxcTm41HcOIm4_naGPF-FZmughKjgfd_a8YKNkIpj05Ipuq3h1wpm7hp0DdypfnPJ8ijezLRnx8zKmQ1Ddb_VbXE2K9DEO_phfQR02FLabWGKyabrKWSqxDRnngl2uw39C-0h4uMfL89QkMtox-uAjvNufuCTxqcXmT7I2ZQ4T7fdp19h_Oq0IwHlsdE5B-zbR9nV_b7DXaHm_XBQtK6aUnvZWtDykJFEy3vetwINLGbEbBgo270SBkd4g_Uvmnme4_kglVbnihpe6RRvt4uQsSGfWntFidAsxfS78pE5XGAIbBziC3_3k7_Mcu7oIgQrCZ0qaRdwhsrqRv1BV3Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=bzxcTm41HcOIm4_naGPF-FZmughKjgfd_a8YKNkIpj05Ipuq3h1wpm7hp0DdypfnPJ8ijezLRnx8zKmQ1Ddb_VbXE2K9DEO_phfQR02FLabWGKyabrKWSqxDRnngl2uw39C-0h4uMfL89QkMtox-uAjvNufuCTxqcXmT7I2ZQ4T7fdp19h_Oq0IwHlsdE5B-zbR9nV_b7DXaHm_XBQtK6aUnvZWtDykJFEy3vetwINLGbEbBgo270SBkd4g_Uvmnme4_kglVbnihpe6RRvt4uQsSGfWntFidAsxfS78pE5XGAIbBziC3_3k7_Mcu7oIgQrCZ0qaRdwhsrqRv1BV3Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاره کردن امضای ترامپ هنگام شلیک پهپاد به سمت پایگاه های امریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68856" target="_blank">📅 16:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68855">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:  یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد. از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه،…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68855" target="_blank">📅 16:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68854">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6QUlHJhkjr2ctvwLH8ythMW80G75Mc5pTP_UlCCtr6c10OweCO6cdspHL3eiCt3PdxLLHprHlDwWSqwJ9m8YtE3EB2OSJtKTEe5aOBige0ggsl_o1C66UxGdkOnSFDFc2paaz39HQ_FqpdF2MefwKwPAFWo1W9UZ8dlcScghudBnadTY0yXwOH_Qg-VOKy7tK4bHAAI2l92e1xNs1_oQVkNfOk5VH57Ki6fHaXTmkJxZABUbFggMZL0hy22wX75S9hpcz2isuO0FLIOFN7jmcCe6fIH5_0QvwA5xedyBaH-WBX2ZAAFW90MGJ72F72gyaVUiLvYo0Nf4H-2Q6H9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛فرانسه در حال تخلیه کردن کارکنان سفارت خود در تهران است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68854" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68853">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMPXNsnP7iY0itZSnyA2W6vFoEKOn9uQAg3-033Yd1az9Lj4hezv1RX3cUVP77zI6HqfhSQwqO_WlC4b6RVCht-dawS7GEcH0X8gKSLW8tjd_fC4q-Qo42AO2r34sF9WNh7k_efYcAaUP43LKTtkx-SgEv1YST-VzFxG8RdYeaS7_yLe_j8ZmNDQ58N7w70kTuBSPsMS-QWr6ZDt4PglGTZ5bH5jF3OSEzymhpXfXX18fGBwjwgD_oi-Hp9RFXTHBpq2cCW0tAo6LeqcTmXLwOMX-w7eJNe2cOJzvdOmM_rgmsI-tw_uS8EZ0U_8fhd7Ej_n-pU-b6OBV34aSscMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد.
از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه، اکنون آن‌ها دوباره فعالیت‌های خود را از سر گرفته و دیشب به دو کشتی عربستان سعودی شلیک کرده‌اند.
لطفاً این واقعیت را مد نظر داشته باشید که اگر آن‌ها دوباره دست به چنین کاری بزنند، ایالات متحده ایران را مسئول خواهد دانست؛ چرا که حوثی‌ها نیروی نیابتی ایران محسوب می‌شوند.
در آن صورت، تنبیه نظامی سنگینی علیه ایران و البته خودِ حوثی‌ها اعمال خواهد شد؛ گروهی که عملکردشان تا پیش از این بسیار حرفه‌ای و هوشمندانه بود و اکنون موجب ناامیدی شدید من شده‌اند.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68853" target="_blank">📅 15:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68852">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsWJF1YF1bTPlvzMBQj4KcO4xWPFXo-UHI91_QFgSEkdptwgwmFi_0hCex9q2AGJGj8YqYBAqnsgfrSv7DFQinIlWFPq8zGNHCANTcfUnO8LBqt4xZYmdtN62oHse7yHBvkjjVEakmClewpB_BTUKRtXdRa1-0LS_cT3WacSIOP8aIy4Ex9R5h_yXlii3SjI1_ZYP4rpO4-xsxyvbHN7ZrJdFgNjvnxKdqDnYg_8A0lpMqORBCS1hd8CxsPQTcscljiJRYrLbdirSuFnAgPJ4adv41NE7jfmeu1CADLmvHgtSN7FhfknK38MgNTKcifAPVmx7ZHctli7-voepCMEkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توافق هسته‌ای غیرنظامی (که شامل هیچ‌گونه غنی‌سازی مواد نخواهد بود!) میان وزارت انرژی ایالات متحده و عربستان سعودی — که صرفاً به مصارف غیرنظامی، مشابه آنچه ایران و امارات (و دیگران) در اختیار دارند، مربوط می‌شود — تصویب خواهد شد؛
اما این امر کاملاً مشروط به پیوستن عربستان سعودی به «پیمان‌های ابراهیم» است که بسیار محترم و موفق هستند.
ایالات متحده با تأسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) مخالف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68852" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68851">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=aD7jeDhfQeANpRSnyH9OrHgz5BaD7ir3cYpRihWUZIDU7a868omyIxEzLIvc-aVibrQo4Fl9r_X7nU_HAjOOob_Ddoj3jbn_Zd_H1oQLE6kmr9EfORM5Yh2LHgaJ09uFOUHOLi_Ev5R5FiwuvWnlqnI8lt9dneRv8485zN356aAYjy2sX9kMPwn4GCFLcNdWkRI4yVe4QYubzQJB2e69a3NEhXvWAvZA1MJRsT6nDcSKcQcPj3JVkmC0XLZ_AprfStCLThNjttNCMKUp2IS3wx9rzHkmqU0SsbUPL2cNqbZ6gqO0zQnauF47nWXDZfI7KbooLDN5XBclJS_-O-0nOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=aD7jeDhfQeANpRSnyH9OrHgz5BaD7ir3cYpRihWUZIDU7a868omyIxEzLIvc-aVibrQo4Fl9r_X7nU_HAjOOob_Ddoj3jbn_Zd_H1oQLE6kmr9EfORM5Yh2LHgaJ09uFOUHOLi_Ev5R5FiwuvWnlqnI8lt9dneRv8485zN356aAYjy2sX9kMPwn4GCFLcNdWkRI4yVe4QYubzQJB2e69a3NEhXvWAvZA1MJRsT6nDcSKcQcPj3JVkmC0XLZ_AprfStCLThNjttNCMKUp2IS3wx9rzHkmqU0SsbUPL2cNqbZ6gqO0zQnauF47nWXDZfI7KbooLDN5XBclJS_-O-0nOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو فروند هواپیمای «EA-37B Compass Call» صبح امروز وارد پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) شدند.
این هواپیماها که بر پایه بدنه «گلف‌استریم G550» ساخته شده‌اند، جدیدترین هواپیماهای جنگ الکترونیک نیروی هوایی ایالات متحده محسوب می‌شوند و مأموریت اصلی آن‌ها مختل کردن شبکه‌ها، رادارها و سامانه‌های فرماندهی و کنترل دشمن است.
در حال حاضر تنها
پنج فروند
از این هواپیماها در خدمت عملیاتی قرار دارند و قیمت هر یک از آن‌ها بیش از ۳۰۰ میلیون دلار است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68851" target="_blank">📅 15:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68849">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDo3F_xIjFr6LzK4JGi05dU35x9DwdNt0DTE_MutftAcVDdivwPi8VdmaCs2hFkzwvk8WT4sascBftRo6SsY3hcUbEIDI3Wmn2Z6V42na_akyVUFv-mrA1deLF5aj1Y-ZimobM50bPVQDpZx6-zEL95MXKdmM2PQBBIIDMayajKLhA9gEQl4jqqjxJyt8gQ8hracKt8m1h9u_vc5WkuCVWUjpdJIGp6IuSC6p23uHsO8ktGEP4lIuxWPSu2J__haBiBsffF5X-LM8Le9JbmckHMnyDLlfhODqtC-w-z2JafGy4Gcy4wZeEwwSTgp_IFsnh5Mu70dXHk3LtT05bDKUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=RTBF2LmcTj0YBAZ1kTRulOaPIABQ3xI0uoL8JhFGvYu9oULG9MjghW5p5Z76H4BTCnwc5Ch1ffdH2ywn44-N0qDpWTwtvp1Oq2_xCWxHO-JFZDg1RgkVfT7kirDmJWbQU_R-TOniORclDDZDv8y5kQnszasFFnH_8SgOmjq_Bojv5bMGHQnsG4yda0_-svPT700YyOtspquNzJWYpbLBBI7dM4U7RLkft8U-X1p9Q2s-nBRGsWT6V26MN63YnH4rNH_2gD2EOi9Fn7lFInNHxtIKe-CoeVxvKuvVqBZpInnghG7ok7qm-cwYoIf40hhsq4_TGS7PEqkSlfLtU9oQUZD3VaSOuWCV__-R9OLaoyy5CzozcNsgJNEuOEdVNsbMWiKz3FSJXS2PE0Megh_a96FzgheW9bYMOp4WSf1zP3YcAKVdWx2s2vyoikHGdaJR_YDAziis-14eqh8Kim3iBerMQCTyNCCd7QcAvUMdOkQXFad3_TuqZi_hRcNH_Fu7WOeWElVMcZpc0BsBFXfVOPXGPDjtFKEb73PejlgINQF03eGrS5tkXygzLglIIpOumJW98pMJDVBJ4-RmJiUzov7F_xotwraiKQrNHrtzl5Ii_9OUrrTnafc9YAopLLsFPMFtVue-TcAREoE81MdjbtXZdfCwtkgjHJ2-lN881Os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=RTBF2LmcTj0YBAZ1kTRulOaPIABQ3xI0uoL8JhFGvYu9oULG9MjghW5p5Z76H4BTCnwc5Ch1ffdH2ywn44-N0qDpWTwtvp1Oq2_xCWxHO-JFZDg1RgkVfT7kirDmJWbQU_R-TOniORclDDZDv8y5kQnszasFFnH_8SgOmjq_Bojv5bMGHQnsG4yda0_-svPT700YyOtspquNzJWYpbLBBI7dM4U7RLkft8U-X1p9Q2s-nBRGsWT6V26MN63YnH4rNH_2gD2EOi9Fn7lFInNHxtIKe-CoeVxvKuvVqBZpInnghG7ok7qm-cwYoIf40hhsq4_TGS7PEqkSlfLtU9oQUZD3VaSOuWCV__-R9OLaoyy5CzozcNsgJNEuOEdVNsbMWiKz3FSJXS2PE0Megh_a96FzgheW9bYMOp4WSf1zP3YcAKVdWx2s2vyoikHGdaJR_YDAziis-14eqh8Kim3iBerMQCTyNCCd7QcAvUMdOkQXFad3_TuqZi_hRcNH_Fu7WOeWElVMcZpc0BsBFXfVOPXGPDjtFKEb73PejlgINQF03eGrS5tkXygzLglIIpOumJW98pMJDVBJ4-RmJiUzov7F_xotwraiKQrNHrtzl5Ii_9OUrrTnafc9YAopLLsFPMFtVue-TcAREoE81MdjbtXZdfCwtkgjHJ2-lN881Os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقوع انفجارها در گذرگاه مرزی «عبدلی» میان عراق و کویت، در سمتِ بصره (عراق)
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68849" target="_blank">📅 14:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68848">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJwd2kgoke3KAPzcDNVhiS4UfhoI_tpr9blyC5h0Vi7qo37FSGItPaB9I2_y3kMagGFz9GJUAKVJQPHHzkFbMKwTqUo5M7wmKTqyPOcb1o5BvMB84xKVhS7NUsajLtGTB9LljosHMV6OJLELYHtSwSlL_o1Pdgy_8eTAn392R0qY5VwJ9PTtuPM98aHUCUUTSEpHISf7bYYatNsxeSl9fxEtT8MBFh5uZQVv6ukutD3h2kSA2boWDziLidJKO1i5SEAgZ3zSayqZE-NUonRzJgtr8IKWISP-p_GBGy2IL2pnXM6KcnzS21eLJkbuDopXQu8XZQK8ISuRI3N88Tl-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابوالفضل ابوترابی، نماینده مجلس:
دولت مسعود پزشکیان با ارسال ۲۸ نامه به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، برای مذاکره اصرار کرده و او را «تهدید» کرده است.
قالیباف و پزشکیان در «تله مذاکره» افتادند و «باید به عقل هر کسی که الان حرف از مذاکره می‌زند، شک کرد.»
اگر جمهوری اسلامی «دو هفته دیگر جنگ را تحمل می‌کرد»، آمریکا و دونالد ترامپ، رییس‌جمهوری آمریکا، پیش از آغاز مذاکرات «همه خواسته‌های» جمهوری اسلامی را می‌پذیرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68848" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68847">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=d8NsX0Z6BFEWyByNYSgd_dKHLU9zpkyiKIANV8eVgkE3AwJcC9BvdXNQAiFr6BtFMwOxfvlfCbe42htX9diml3JrKVbOLz2oEBlMq_5dkq-9I-vrydBmIWsyrLZnXOaV9ovgjSyCuG2DsRtUt1AMLfOOBsLXVKZoo6ey0PAp53kbjqoX5nD6tnnjCZfdkdShhRgEzr934uZtK8tnqSC5ctK4cvN0KpmVhtlyjMdJ1mrFemyX_F2kUeXkkrJXPLtuuqh_Y5By4P-sFWPghwBNYQ2PpBL5LPbHUjj3rQLvYXvWO8NLUtkuMZsRLSMmBB-vS4_qjPKHVwPSHev4IcTY1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=d8NsX0Z6BFEWyByNYSgd_dKHLU9zpkyiKIANV8eVgkE3AwJcC9BvdXNQAiFr6BtFMwOxfvlfCbe42htX9diml3JrKVbOLz2oEBlMq_5dkq-9I-vrydBmIWsyrLZnXOaV9ovgjSyCuG2DsRtUt1AMLfOOBsLXVKZoo6ey0PAp53kbjqoX5nD6tnnjCZfdkdShhRgEzr934uZtK8tnqSC5ctK4cvN0KpmVhtlyjMdJ1mrFemyX_F2kUeXkkrJXPLtuuqh_Y5By4P-sFWPghwBNYQ2PpBL5LPbHUjj3rQLvYXvWO8NLUtkuMZsRLSMmBB-vS4_qjPKHVwPSHev4IcTY1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه حمله آمریکا به حوالی بهبهان
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68847" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68846">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMO38UsNGE8oPBq7swcNkimjOGth39Sh8ji3uz7XHSybgyQXFsACXrQDLG65Cq9X0OFqKUbuJooHNjylmH1QlpBdvWXomz4K5UqyLjwtUmHl1-xYkylL3uo9jd8kdJubOjESPdb8a91ZMhdCxRicM-uPANb6xFbptc6hE0k3qz_CjhNZdlTLPRGc-i1CkHpIW-osOvVIq8pPEK2ASwNxXL8AZvZuD6m8-0k_ps42I3UyMoR-81dU0YykJckVn3XYlQb6FF07JypXHjRIdUgvYSqKbadudPCWFDNHsrlXeWr1xbmT6viR1wid_GYGFG83hkIgfnm8cvNnLWfNQNJ80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68846" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
