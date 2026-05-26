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
<img src="https://cdn4.telesco.pe/file/sbMugxMv0AwGatps2FPIF2LxmgrCEMWFWu1asRiidQtIB7gf6kv9qSiNAPsTk87-yETCcWc68Bnz9pT9MkkhRKJNgm3NJkmufRxxOrsTkmV_FbC46_jH0tKu7NxgBUuEhw-m0wu0IKmhP68TO8wm0aF7Iox-cLG-9XuTHdU45sFKbYPG_c6uw768tXwU7vmlUfSli1L70J0oG5vfQnt1I0UW0cC7YWd8ql31FMAHjbjOUqZBqqLIvnPsUbCOmbS75mJ5IYs7Qz14pBbnELvOxQ_JtDO1-yUp3vVsn81br1-ZWlD17vVn5vJ4PzG_usc6qa3PPbI4M9CNa3cniLD29Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 17:41:59</div>
<hr>

<div class="tg-post" id="msg-438128">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwx11PK9m5yKekiDiJXbSzPwiHYSjGBUOEmrTKxogQv0crrzdQGmjYhdVaVM93TF36biYXZUgy5APdyeP8Nt8YGv4e1fn4BePCHYYGW59wmi_aY1PVCtWVEciKhBG9mHvOMpRtwC5ha1lIWg4vLRkRJSdrBVBDnziy_se_Y1hhOhkJul5zrM8_t9luyA5MDIMGRORu_fy4bQwmlE2Ahsn_ewyceG__2sNgZ1-tLHtTBofUmbXzwcNZE2HWtp3NrCD4gXZCAfRLqNq7mKjxUdjp_oEh7gNeZkogUkJGqpSbL749w_fUTwXUwEYcuD46tDC2arSxp4b35XyYSrh-ffug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهرست ۳۰ نفرهٔ پیاتزا برای لیگ‌ملت‌ها ۲۰۲۶ اعلام شد
🏐
پاسور: عرشیا به‌نژاد، عمران کوکجیلی، علی رمضانی و ایلشن داودی‌پور
🏐
قطر پاسور: علی حاجی‌پور، امین اسماعیل‌نژاد، بردیا سعادت، پویا آریاخواه، امیرمحمدگل‌زاده و محسن دلاوری‌
🏐
دریافت‌کننده قدرتی: مرتضی شریفی، پوریا حسین‌خانزاده، امیرحسین اسفندیار، علی حق‌پرست، مبین نصری، احسان دانش‌دوست، متین حسینی، علیرضا عبدالحمیدی و اسماعیل مسافر
🏐
مدافع میانی: محمد ولی‌زاده، یوسف کاظمی، سیدعیسی ناصری، نیما باطنی، آرمین قلیچ نیازی، شایان مهرابی و متین احمدی
🏐
لیبروها: محمدرضا حضرت‌پور، آرمان صالحی، کمیل خجسته و حسین حاجی‌کلاته
🔸
مرحلهٔ مقدماتی لیگ ملت‌های والیبال ۲۰۲۶ در گروه مردان از ۲۰ خرداد تا ۲۸ تیر برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/farsna/438128" target="_blank">📅 17:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438127">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4100b3272d.mp4?token=caYRMTROgXCO9VlF8MJdFOzbnevqXcJ9IJZaYBlWGF20-mOTtVWTn1fRI9NecH652Y8ocNUprVilhiCw_GhiKgDUkH89iw5zkFu5rOz5hRqDvBkaEWkq6A9VuzMtuuWuab_kTbM2xHA_mv4piSDEdcR3hSPayo1q9s-qhln50jWxvFKD-ZuVkVt21IuFlRx_nJScA9fAGKqSmno_0nWhXZiH3FdJ52vR-Z4FOovtXEy5ayGvMsmmApBwPTZLlcxzf-KkJR1mAcX4NgCZyEdh7NKr9MbzsJwnuH6QN08w6fkvoS-Zibg0D2WNJlKAF1S8A6hEdASmtAINvFL-TJJ49oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4100b3272d.mp4?token=caYRMTROgXCO9VlF8MJdFOzbnevqXcJ9IJZaYBlWGF20-mOTtVWTn1fRI9NecH652Y8ocNUprVilhiCw_GhiKgDUkH89iw5zkFu5rOz5hRqDvBkaEWkq6A9VuzMtuuWuab_kTbM2xHA_mv4piSDEdcR3hSPayo1q9s-qhln50jWxvFKD-ZuVkVt21IuFlRx_nJScA9fAGKqSmno_0nWhXZiH3FdJ52vR-Z4FOovtXEy5ayGvMsmmApBwPTZLlcxzf-KkJR1mAcX4NgCZyEdh7NKr9MbzsJwnuH6QN08w6fkvoS-Zibg0D2WNJlKAF1S8A6hEdASmtAINvFL-TJJ49oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از حضور زائران رضوی در مراسم دعای عرفه
@Farsna</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/farsna/438127" target="_blank">📅 17:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438125">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1VvYzgAEOZ0cHNQ34bjsH2712UOPRIbmB_OgMK9nnZa2SvpM7WVMs72WA-N4oL2tvO734u-RuafnoSThWfWrlU3YGFDlPt5Hdq5m2qGqD8qX6rjiDmxyeeAnnIu3LpuU-zIb6Emzvc3uit2n_L6BqncU5lqE_FDVZ8qMxRNwXxJ5Iu4i57Th2zrpH_qJn5A7qDFRIi_wCR_zX905Q02_2X6de01fhf-ozqo7irahWr9Yjz0JOKeQHo_t6QEKi_ebVKHhPT2K93nDzb3XE_3DsfMWubX6YT67LIeTp9nXIvWKzCuPC5de6wJJmLg_6U73OnEAa0RHV1MkHjMMnHVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
یک منبع در وزارت ارتباطات: مصوبهٔ بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴، دقایقی پیش از سوی رئیس‌جمهور به وزارت ارتباطات ابلاغ شد.  @Farsna</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/farsna/438125" target="_blank">📅 17:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438124">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8735883516.mp4?token=K936DGQZHVExAGhdnYzPPjTOf9EWMuwgoXm7Q9h2wSCVLUlEzukgHQ6rdAqM0PTDhgCDYxycmK9-oR82O0khWn61saecWGCiXSjTOmYl4tgHQsx-9gBq0M7zTVQykScAWDyhyoHvsLdFl5nfUs_ffAPtofW4w0WdogfdaqLwpmqrxLRZZ1bVKmqhbLbU4yax_76vRxlk0vPrNh2mH1uMlUsM6ynM6NeqRHSrhtpLQw51CvV1jszLFmi_t4YWoyJ_Ax8ETOKClP3nJapYSxIrc5mjt7MwYqXROVIMyjyadky5nNUyypZ6Gv7fH8aa24ngMEkWG_P3oUeMh347xhtkBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8735883516.mp4?token=K936DGQZHVExAGhdnYzPPjTOf9EWMuwgoXm7Q9h2wSCVLUlEzukgHQ6rdAqM0PTDhgCDYxycmK9-oR82O0khWn61saecWGCiXSjTOmYl4tgHQsx-9gBq0M7zTVQykScAWDyhyoHvsLdFl5nfUs_ffAPtofW4w0WdogfdaqLwpmqrxLRZZ1bVKmqhbLbU4yax_76vRxlk0vPrNh2mH1uMlUsM6ynM6NeqRHSrhtpLQw51CvV1jszLFmi_t4YWoyJ_Ax8ETOKClP3nJapYSxIrc5mjt7MwYqXROVIMyjyadky5nNUyypZ6Gv7fH8aa24ngMEkWG_P3oUeMh347xhtkBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ صهیونیست‌ها به نزدیکی سد قرعون در شرق لبنان
@Farsna</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/farsna/438124" target="_blank">📅 17:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438123">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
آغاز مراسم دعای عرفه در حرم بانوی کرامت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/438123" target="_blank">📅 17:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438122">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
برگزاری مراسم دعای عرفه در حرم مطهر شاهچراغ (ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/438122" target="_blank">📅 16:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438121">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379e1ee161.mp4?token=ClInHbfRU6jssezh12JLEmPVZ9-35pKfvlkbNsGHBSULZf8tNFvRFHPSGHuaWidrz3v_gkLVB4RoITJxZAJ6_tWmlwU9dArw5iIH4gSyXf7uZhg9yg8ALegwicjxqd2rw5SamHTL7OQ7Rhm_6r1shPJcS0z641uBVgfqjvhcUQR9bYPzmbDM2-RUKBslbgI5hlLu5xAlT3hgOFjmwPYPCrM0U3FMpPY_dBTV2SIYp7FrkFkS20Uo2ulM7xByannN_lHtkH-1qphR8qV66gfbDH_pJaiwOpDmbJG7cbLrslXYjCTOJlm-B7MXosmtE2hdiZ6Y6yC0QPLHvZ-yOw3a9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379e1ee161.mp4?token=ClInHbfRU6jssezh12JLEmPVZ9-35pKfvlkbNsGHBSULZf8tNFvRFHPSGHuaWidrz3v_gkLVB4RoITJxZAJ6_tWmlwU9dArw5iIH4gSyXf7uZhg9yg8ALegwicjxqd2rw5SamHTL7OQ7Rhm_6r1shPJcS0z641uBVgfqjvhcUQR9bYPzmbDM2-RUKBslbgI5hlLu5xAlT3hgOFjmwPYPCrM0U3FMpPY_dBTV2SIYp7FrkFkS20Uo2ulM7xByannN_lHtkH-1qphR8qV66gfbDH_pJaiwOpDmbJG7cbLrslXYjCTOJlm-B7MXosmtE2hdiZ6Y6yC0QPLHvZ-yOw3a9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار یک مرکاوا و یک هامر توسط حزب‌الله
🔹
حزب‌الله: یک تانک مرکاوا و یک خودروی نظامی هامر دشمن اسرائیلی در دو عملیات پهپادی صبح امروز منهدم شد.
🔹
در شهر «زوطر شرقی» نیز یک بولدوزر نظامی طعمهٔ پهپاد انتحاری شده و دو تجمع نیروهای رژیم اشغالگر هدف توپخانه و موشک‌ها…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/438121" target="_blank">📅 16:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438120">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9444f48172.mp4?token=aZyMTeMcKghpm-2MfyykqcMXic9RQRf-_Qe_YyWN2XCh1G419whXwqCZ6-MQS2Y_FxCBaQyDVqNktYy1BRf8qi0Fm5V0gFKEODvGS4RTHpJhL-JnEgZX3qBuCudqegO7QCd6ydmWtt0PlMT4sZE_Y-SKGeSG4vChF2aGgR6qADbuW9nVTR8AYKfeXFIZLpk1IFnsRMbNlF3qYBj07mAZFfwyz7uM2LMQhS1uPQCaxc89mG2kuH3dOe8GXVFKWHttJy7JHyUvXPOvjjgfVaqdM1vnIpPmLLn5cXJbliUuO8Up53srTJD92rw9lSNWWwst48eFjgBhWCR-jS00uJcaKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9444f48172.mp4?token=aZyMTeMcKghpm-2MfyykqcMXic9RQRf-_Qe_YyWN2XCh1G419whXwqCZ6-MQS2Y_FxCBaQyDVqNktYy1BRf8qi0Fm5V0gFKEODvGS4RTHpJhL-JnEgZX3qBuCudqegO7QCd6ydmWtt0PlMT4sZE_Y-SKGeSG4vChF2aGgR6qADbuW9nVTR8AYKfeXFIZLpk1IFnsRMbNlF3qYBj07mAZFfwyz7uM2LMQhS1uPQCaxc89mG2kuH3dOe8GXVFKWHttJy7JHyUvXPOvjjgfVaqdM1vnIpPmLLn5cXJbliUuO8Up53srTJD92rw9lSNWWwst48eFjgBhWCR-jS00uJcaKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم مطهر رضوی، آمادهٔ میزبانی از دلدادگان روز عرفه  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/438120" target="_blank">📅 16:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438119">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwgCDF5tMPaE-cQdwwWwHsZyyMBEBvl3MKRCIA2I4DFhthk1WAhoxl8Lxn3RtScI6R2AnWVpT_TX3lcE4ZX_R9_Zq1Os4VGHELTtF2YVtgC6BSZyWve7-vWi1hd9eyNMQThvlgOZ_MCSw_zX28ZH3aT4Lm4IHWKGcCvVE68X45JMc4jx5PD1a0H_dRaj8FbHOtDm9ydJhGXQhpCLRx-YrrBse2eVGlzJIXg9vj58a8Po8gs-9lsOuIhmNE_r13-4T3eaLCGYSi0CGYPUtT-fxp5ltIvy46tQP3_7oLbSwqY1GjaAr2y-rSfPPnO_nFu80CP2KDHsTSHujJvP11MdFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرما‌یه‌گذاری ۷.۵ همتی برای تجاری‌سازی دستاوردهای فناورانه
🔹
وزیر علوم: در تفاهمنامه‌ای با صندوق نوآوری و شکوفایی، این صندوق ۷ الی ۷ و نیم هزار میلیارد تومان در تجاری‌سازی محصولات و دستاوردهای فناورانه برای تحقیق و توسعه، ایجاد سوله‌های نیمه‌صنعتی و احداث ۱۰ برج فناوری سرمایه‌گذاری می‌کند.
عکس: احمد معینی‌جم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/438119" target="_blank">📅 16:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438118">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d258dd80be.mp4?token=aTAu_Z2e037c7wbsKksY3B3vhqeQDPqvcN0BovwMcT8dM5pfwSJ3d84YYQ-GmNp-2NrDzqyuuh2LYFX1Az7kwKoOqbq2kamjLy0iwiGXXmZBLlQS0OPpvknWB5FDni4zxRzle3HSG9EsGFPdcPimYq2Dm0Hyf1ZJeQPJ9tVcb_Sk6Yv0E-ZCujuDqiT5lS2su6bTTkbzbGNFjkzoLQ3fIF6y70M4bXv1jXH2E4Qgl09AjRJRpz8dMvj2J4qSp8PLpfeE4K7guHUtKZP4z_BmO3pNDQA0xXBO0eHazFwocBJpCRKN9yEgZjjNimwvqOI1j7sFvUhBxiU-S_VxesAL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d258dd80be.mp4?token=aTAu_Z2e037c7wbsKksY3B3vhqeQDPqvcN0BovwMcT8dM5pfwSJ3d84YYQ-GmNp-2NrDzqyuuh2LYFX1Az7kwKoOqbq2kamjLy0iwiGXXmZBLlQS0OPpvknWB5FDni4zxRzle3HSG9EsGFPdcPimYq2Dm0Hyf1ZJeQPJ9tVcb_Sk6Yv0E-ZCujuDqiT5lS2su6bTTkbzbGNFjkzoLQ3fIF6y70M4bXv1jXH2E4Qgl09AjRJRpz8dMvj2J4qSp8PLpfeE4K7guHUtKZP4z_BmO3pNDQA0xXBO0eHazFwocBJpCRKN9yEgZjjNimwvqOI1j7sFvUhBxiU-S_VxesAL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعلام انزجار زائران عرفات از مستکبرین جهان
@Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/438118" target="_blank">📅 16:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438117">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6547b80539.mp4?token=VtIgdMjh7P1N8bT-7XGsxcWL253GZ4jKRfSX9y32xGIugCm__3t6mi5u0tSssH6LH9tVq2A45KVHskj_MFamGw-n3FmOngByaMzPzIG0M65H67SAYRZ4GAIvOkE5J9tzzg_FcyYYRFhtp6qFJ9VdApB11lvPY2FOtDsI37JrhgkJXaM5up7mgjR_v0Me2DgdWwASrN6XfK21m3u7X2QiXlRS_0jmr9ZCI2ljLRMpZ7Avb6SaGjE3xIV9Cgw7jJ-xpQRpWElp5_hT2x-_bZHKjlEPk8rtLiNzbw8aRNDZTS2MpD-1Vgi_YvI3zNrl-vBuCDXG7HbS3GcJba9TOy9cJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6547b80539.mp4?token=VtIgdMjh7P1N8bT-7XGsxcWL253GZ4jKRfSX9y32xGIugCm__3t6mi5u0tSssH6LH9tVq2A45KVHskj_MFamGw-n3FmOngByaMzPzIG0M65H67SAYRZ4GAIvOkE5J9tzzg_FcyYYRFhtp6qFJ9VdApB11lvPY2FOtDsI37JrhgkJXaM5up7mgjR_v0Me2DgdWwASrN6XfK21m3u7X2QiXlRS_0jmr9ZCI2ljLRMpZ7Avb6SaGjE3xIV9Cgw7jJ-xpQRpWElp5_hT2x-_bZHKjlEPk8rtLiNzbw8aRNDZTS2MpD-1Vgi_YvI3zNrl-vBuCDXG7HbS3GcJba9TOy9cJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#نماهنگ
|
روز عرفه را قدر بدانید
@rahbari_plus</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/438117" target="_blank">📅 16:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438116">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دعای عرفه .pdf</div>
  <div class="tg-doc-extra">207.7 KB</div>
</div>
<a href="https://t.me/farsna/438116" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
متن و ترجمهٔ دعای عرفه
@Farsna</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/438116" target="_blank">📅 16:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438115">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f09713cb.mp4?token=HUtTowUWm7_Nz4_GqHMboKaEsqTnWIOeT21OvTiPVpKR5GtaVH9zopC8T6475POKuOcNsbSDSi_D6243XJF18MOkAgHDpbq-GJQitTOI-0mNuuKYCwOcbDLnNrNiSqD-lyTEKNLzdQpVFTWGRH_zXGWLwxpZaIVYxgLZOE61fgwRajOcPpQzsWKTlJhI6wvJYTudYokcv4x9Py1sGXS6GIgcdfKFHgWdKoJ2Y56aETML9kKGcD6kfy6nXKLTCj6FidxSvc6wpr-J_8FhVIjg8zQcd01NufwTkB8NkQAjMd1omPIuhIR5928gOHnPajVV-Sfa7qT-dGWMHNw4x3mkVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f09713cb.mp4?token=HUtTowUWm7_Nz4_GqHMboKaEsqTnWIOeT21OvTiPVpKR5GtaVH9zopC8T6475POKuOcNsbSDSi_D6243XJF18MOkAgHDpbq-GJQitTOI-0mNuuKYCwOcbDLnNrNiSqD-lyTEKNLzdQpVFTWGRH_zXGWLwxpZaIVYxgLZOE61fgwRajOcPpQzsWKTlJhI6wvJYTudYokcv4x9Py1sGXS6GIgcdfKFHgWdKoJ2Y56aETML9kKGcD6kfy6nXKLTCj6FidxSvc6wpr-J_8FhVIjg8zQcd01NufwTkB8NkQAjMd1omPIuhIR5928gOHnPajVV-Sfa7qT-dGWMHNw4x3mkVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم مطهر رضوی، آمادهٔ میزبانی از دلدادگان روز عرفه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/438115" target="_blank">📅 16:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438114">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPR2s48_L8vAVU30MMpQC69a15hM22d4YjQuIyt0cD-0oYrI51_xMPgiAlEoz_lgOU-wBTQrFKO_1w-yX51Vb0ScevVlrFG0BUjQ6Pgy35IfpUlrG-gfa0pWc859JRNcxWcsMU2RAvP2hpIllt06w2c6VFD2cP9plP-BMan0TCAK8Cn4s1pJjGIggKo2VLSYKs_1NApATsjZ0bpWlcPTrltG4gsFDNH23cyf9mwnUOTeaaqKyurbKT1cJVXkjeYxGGgsM79JrnkbzWN_7rgm-RI7GQCVsl_OYaydirNYfgtSIPsDfDkwu6MeGQaz5Ya2mRiOKXyACMtO6Ar2cFHSPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماموران بدنام ادارهٔ مهاجرت آمریکا در راه جام‌ جهانی
🔹
وزیر امنیت داخلی ایالات متحده، تأیید کرد که مأموران ادارهٔ مهاجرت آمریکا در طول جام ‌جهانی ٢٠٢۶ در ورزشگاه‌ها مستقر خواهند شد.
🔹
ماموران اداره‌ٔ مهاجرت دولت ترامپ به اعمال خشونت‌آمیز شهرت دارند به طور مثال ماموران این اداره تنها در عرض ۱ ماه به ۲ شهروند آمریکایی به‌صورت مستقیم شلیک کردند و آن‌ها را کشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/438114" target="_blank">📅 15:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438113">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otqkCLnjB1ZHcUCiwcSSEsAUPmtrGrDxx5ZBhKOjjGutpYi87U6dwRFSD5r0LbUOvjHkzWJptWq3VqFCFZS1-o17ZPj_mwGBNiPC81bu66Lx-N1v-3adzOTT-lo9BE3ud8lBUMIpfpuL15EIUc8OHMvkdILLi0HD6MDruWq5EUptpO4ISZL4ex3o4VaZi76oTOlQbQFLaWpBaD1cjGhizp6hrZA8Xq7kZ5eaMeVLInUiSu9k02QsyekFgZ8r0XQlDKesbaJQZuDVe_pPyRpC0qr3PL1cLUiyGQCHFp51Wt7uY6nupj_Y-4OimsspyiZdowtlxGqiIkjKt5w1Ay7nDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثهٔ دریایی در نزدیکی عمان
🔹
سازمان حمل‌ونقل دریایی انگلیس اعلام کرد گزارشی از انفجار در یک نفتکش در ۶۰ مایلی ساحل مسقط دریافت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/438113" target="_blank">📅 15:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438112">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYe69EDHAlA5MTSHE3nUjDPd-5y_kCbXTF6KShJBNNZebYpCpLwcW_UjeO7OY86Y_WkjV0gScnFZHbUlSN2Lh06i8AkBULxtOXvYt6BerD6wARuI99o2_YCAAV-6wvJnGLpC0X7__ITwU3yzQvSA7XE6-xN86wqMqrnFYr258PBcsL8ysLM4bxI0Ws-Kpep_xnx29eCP9Hb941rYj8BZViuEGwb7nlrc720VM7fGjDi11sohyBV7jEcTIgoi8AqIfBftn--PbPIJVHE7x0f-J6WQEWiGrEERoBwZ26HCkFYDPSz-N5IkpwShWcrGTueyy9efjv2ocZvdOqmGNMvIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلطان عمان برای رشد تجارت با ایران شخصا وارد عمل شد
🔹
براساس اطلاعات رسیده به خبرنگار فارس پادشاه عمان دستور اقدامات لازم برای افزایش حجم تجارت ایران و عمان را داده است.
🔹
عمان از گذشته تمایل داشت تا بخشی از تجارت ۲۵ میلیارد دلاری ایران با امارات را جذب کند؛ حتی روسای برخی از شعب بانکی خود را تغییر داده‌اند تا کار تجار ایرانی با سرعت بیشتری انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/438112" target="_blank">📅 15:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438111">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf6d039eb.mp4?token=dRsH-b2H41H4YhO4svLIwWbG6pBWRWZ_fwBsFFcsKsclReiJ55qQb7z_5a4FXR-jOAQcVcIceBfRibcoIDtn3l8qQs0cFtZJbUHOQutPgHQa625UrgtF62VVSekgdBe1K6sMnavQjPPZnMv9xWwMCSnIslcqpjGH5qHSfPyuVfG3r8rdegK4tD3dAE-wEUsAAqHNaeYXGW_pyoYj3ZSOTSHkiJTXjZhuzHbKUt3yewZbn38-5_gWMrgnT0hnB8HW49HUHqm0ahAY0cEohvrmUsjC0y8ki5ZF8V-PzKfrVMZuDm5f6qZWb3claPtukLh8MAUc0iuBEvZW5W7B6sYiXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf6d039eb.mp4?token=dRsH-b2H41H4YhO4svLIwWbG6pBWRWZ_fwBsFFcsKsclReiJ55qQb7z_5a4FXR-jOAQcVcIceBfRibcoIDtn3l8qQs0cFtZJbUHOQutPgHQa625UrgtF62VVSekgdBe1K6sMnavQjPPZnMv9xWwMCSnIslcqpjGH5qHSfPyuVfG3r8rdegK4tD3dAE-wEUsAAqHNaeYXGW_pyoYj3ZSOTSHkiJTXjZhuzHbKUt3yewZbn38-5_gWMrgnT0hnB8HW49HUHqm0ahAY0cEohvrmUsjC0y8ki5ZF8V-PzKfrVMZuDm5f6qZWb3claPtukLh8MAUc0iuBEvZW5W7B6sYiXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرپرست وزارت دفاع: در جنگ رمضان به فناوری‌ای دست‌پیداکردیم که حدود ۲۱۰ پرندۀ دشمن را هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/438111" target="_blank">📅 15:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438110">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOaYAqHlFgOVfWQtKtUNw2p8m7OSgHNtNXXWawASblmhOadV_PY5br3YdYIQGMMBSLtTRRof5FGwVmQpB4mIdtKVfIjCnLWhe3OgwwRnbsHvGVLSCBaTYTjMXxMS9pGxxAG8cCfGJHcYYd5nNSAfdAPkeO5ZJeXmweN8zFYaVPQlvytJqqNvomKaOcVK9DHrfv7hyWNaxybqjFz2DFX8b_JAo4o8eCDLieYPXBWMe5EhLXbBCNghJeUfG0uP50nj_CMqJB8EC6SAo0sTvC2uuvek6EBx6uwYn3r-dH4EKdpI8-Cgyx3dEAuj7yDCFlo2eInNJlJA1LREnmvz2vCE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برق اروپا در گروی محموله‌های گاز قطر در پشت تنگهٔ هرمز
🔹
شرکت‌های اروپایی برای قطع وابستگی به روسیه، از قطر گاز طبیعی مایع (ال‌ان‌جی) می‌خریدند که با حملهٔ آمریکا و اسرائیل به ایران، صادرات قطر، یکی از بزرگ‌ترین تولیدکنندگان ال‌ان‌جی جهان متوقف شده ‌است.
🔹
حالا قطر ماه‌به‌ماه این شرایط اضطراری را که از ۱۳ اسفند ۱۴۰۴ با حملات موشکی ایران به تاسیسات راس‌لفان اعلام کرد، تمدید می‌کند که به‌معنای عدم ارسال محموله‌های گاز به شرکت‌های اروپایی نیازمند سوخت برای تولید برق است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/438110" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438109">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ci--R8NJzm8mg3p_ESu5CteIXl3kujs7hX-jA-bOG9JAQdLZPLJ3NBhBeFtpEMzzT8n9JvVs_VxcblMnGQBnjGV4q-DXoyKuhkzySsSFR1KZlguIpgf5YX4rokMSNCITSWXEMTf9RH6ckosPMFgq2WnKVg5Q2hnpgzV74uOz5-YRsZjg6RqssTpr6CqqR6-SYOfXEa5B3iuVZe4fyphBLxgGeK1D9uP0dRoWvxAgCy1NsJYEDtu1t2EmR-FCzRJwM_3uLna0HVOG_Ov92yh9RfhqSnG9Bq7k2TLv30LCnye_YT7CFgzUk_e6ruhTKa0IThaluo7c6hgkWNEv29M4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت اکبر عبدی از زبان ده‌نمکی
🔹
مسعود ده‌نمکی، کارگردان سینما در گفتگو با فارس: اکبر عبدی یک یا دو مورد سکته خفیف داشت و در حال حاضر به دلیل عوارض قبلی در آی‌سی‌یو است و وضعیتش تثبیت نشده است.
🔹
آقای عبدی چند روزی هم در خواب مصنوعی بود و امیدواریم…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/438109" target="_blank">📅 15:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438108">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on6qaVGS5zmz4oogf6xolLS5dvqyGv3WDNVqU6d8XYgbJyAxWFGqhvu1B848tLFp2_ZkkOUItiFTRyThqRhReZCdkswNsbP6cL7mBUp1c1yr_2pLeB9wles6BcFB64ffbD07pmZUYtHR6SHQKCvpjyELXeCK6buHaYwx3z-uVEAh4-UA544JvUT51lXjN1423iKyOz9AK8HNAJKTjfuf-qm4Cx4-1fdTKNxmfasxUrNyvWcxpQcWhx7Uwv9ShfC7WEXPIQXuIfqtrrbE-leFgK3Bif78EQaS1GvKF6PfKMzsUbGMAKSP9GAEWCueKeFotsevmHcDxxjvkBqAZLfU4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: یک پهپاد آمریکایی را سرنگون و پهپاد و جنگندهٔ آمریکایی را فراری دادیم
🔹
ارتش تروریستی آمریکا در ادامهٔ ماجراجویی‌های مداخله‌گرایانه در منطقه و رفتارهای متجاوزانه، در منطقه خلیج فارس وارد حریم هوایی ایران شد و یگان‌های پدافندی سپاه پاسداران در راستای…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/438108" target="_blank">📅 15:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd0a764f0.mp4?token=EaqHjtoIwdkUhp-tSQW3-1F2nJDJ3QfdwjmQGbKOgp0Zcu7cAPi32LC2RI3rBQrY0Yif26xNTkd6O7QtMUJQFdLa0DcvYDKy1RedxyBb-XEmwn9aqP_kDd4VdNFknEfUav2VND1ds5KGC3rbMMChYa_gJmhNPL7R5vGq8kv67SQtdkGeQ0eKukdHsN3XSGoi451dhISnjuH50gR9lP23wAtnHxSUxFuvvIw-KNmH9A7r5hwYrz6COJpvEQgu3q2L588W-bJDmoZ5Fe_1_rDhmVgf2l6xlA-WpcurChZIwVnbCCiq29FU7JdXz_V1TiPlYvkA4DwxAs-He-QU0Y4CXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd0a764f0.mp4?token=EaqHjtoIwdkUhp-tSQW3-1F2nJDJ3QfdwjmQGbKOgp0Zcu7cAPi32LC2RI3rBQrY0Yif26xNTkd6O7QtMUJQFdLa0DcvYDKy1RedxyBb-XEmwn9aqP_kDd4VdNFknEfUav2VND1ds5KGC3rbMMChYa_gJmhNPL7R5vGq8kv67SQtdkGeQ0eKukdHsN3XSGoi451dhISnjuH50gR9lP23wAtnHxSUxFuvvIw-KNmH9A7r5hwYrz6COJpvEQgu3q2L588W-bJDmoZ5Fe_1_rDhmVgf2l6xlA-WpcurChZIwVnbCCiq29FU7JdXz_V1TiPlYvkA4DwxAs-He-QU0Y4CXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: انسجام داخلی مهم‌ترین مؤلفهٔ استمرار برتری در میدان نبرد است
🔹
اگر جبههٔ داخلی تضعیف شود و مردم در سیاست‌گذاری‌ها مورد توجه قرار نگیرند، تحقق اهداف ملی نیز دشوار خواهد شد.
🔹
تلاش کرده‌ایم با رویکرد محله‌محوری و مسجد‌محوری، مردم را به متن فرآیند مدیریت…</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/438107" target="_blank">📅 14:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0e82f84d5.mp4?token=W8U5Cd12Xkjsm5zU1t08k02IABYSNjAnRUVQK0GHfOT9hBj1HI5Pg9s7e36geZ8hVKOuEpJnsW4BQ0dAa8jUhvJ1iTGME8xzFOtRkpN9A2mI2EazRTVG2cIRTUJ37hJpoZLLYAaxMR5TLCNpF8pvrGG2X-nsgAXzJrEb_iQND1qQ5bZbgye_uoT604GoKVRXFbtNCCRY_L-O3Oe925-nAsYq0_zKuOYZrTmUTeJuDb2d3u_fdBDh370cgjb8zk57JTQLSXqnuv8AgPGqhIRFq_ajVBaUDOv6DGQjAfUVhpvPdUcjXzGVQ1GpzsNZ7zKAhG4SRisbk_lrpv4e0piixw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0e82f84d5.mp4?token=W8U5Cd12Xkjsm5zU1t08k02IABYSNjAnRUVQK0GHfOT9hBj1HI5Pg9s7e36geZ8hVKOuEpJnsW4BQ0dAa8jUhvJ1iTGME8xzFOtRkpN9A2mI2EazRTVG2cIRTUJ37hJpoZLLYAaxMR5TLCNpF8pvrGG2X-nsgAXzJrEb_iQND1qQ5bZbgye_uoT604GoKVRXFbtNCCRY_L-O3Oe925-nAsYq0_zKuOYZrTmUTeJuDb2d3u_fdBDh370cgjb8zk57JTQLSXqnuv8AgPGqhIRFq_ajVBaUDOv6DGQjAfUVhpvPdUcjXzGVQ1GpzsNZ7zKAhG4SRisbk_lrpv4e0piixw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد متخاصم با «آرش‌های کمانگیر» شکار شد
🔹
در ساعات گذشته، فضای خلیج فارس شاهد نمایش اقتدار دفاعی جمهوری اسلامی ایران بود؛ جایی که رزمندگان ایرانی با رونمایی از آرش‌های کمانگیر با سامانه‌های جدید، یک پهپاد متخاصم را بر فراز آب‌های استراتژیک خلیج فارس با…</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/438106" target="_blank">📅 14:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سفر به قطر و تبادل آتش در خلیج فارس؛ چرا مخاطبان خبر را از رسانهٔ خارجی می‌خوانند؟
🔹
در روزهای اخیر، انتشار خبر سفر آقایان قالیباف و همتی به قطر و نیز جزئیات تبادل آتش در خلیج فارس توسط رسانه‌های خارجی، پیش از رسانه‌های داخلی، موجب گلایهٔ گستردهٔ مخاطبان شده است.
🔹
کاربران به‌ویژه به رسانه‌هایی مانند فارس اعتراض دارند که چرا باید اخبار مهم مربوط به مقامات ایرانی را از منابع خارجی دنبال کنند.
🔹
این نقد از آنجا ریشه می‌گیرد که به‌نظر می‌رسد برخی مسئولان یا توجه کافی به نقش رسانه در حکمرانی ندارند، یا به دلایلی مانند محافظه‌کاری امنیتی، همکاری به‌موقع با خبرگزاری‌ها را در اولویت قرار نمی‌دهند.
🔹
این موضوع اگرچه نافی دیگر ویژگی‌های مثبت این مسئولان نیست، اما مردم این ضعف را می‌بینند و آن را ناشی از کم‌توجهی به سواد رسانه‌ای در سطوح مدیریتی می‌دانند.
🔹
باید توجه داشت که خبرگزاری‌های رسمی موظف‌اند اخبار با حساسیت بالا را پس از بررسی همه‌جانبه و اظهارنظر مراجع ذیربط منتشر کنند.
🔹
این رویه و حتی بسیار شدیدتر از آن در همه جای دنیا مرسوم است؛ تا جایی که برخی دولت‌ها و کشورها رسماً ادارهٔ سانسور دارند.
🔹
اما با این حال، گلایهٔ مخاطبان از نبود پیش‌دستی رسانه‌های داخلی در انعکاس به‌موقع رویدادهای مهم، حتی در چارچوب رعایت ملاحظات امنیتی، همچنان به‌قوت خود باقی است.
🖼
در این میان، رویکرد پلتفرمی خبرگزاری فارس فرصتی فراهم کرده است: مخاطبان می‌توانند اخباری که از منابع دیگر (از جمله خارجی) در صحت آن‌ها اطمینان دارند، در بخش کاربری فارس منتشر کنند.
🔸
خبرگزاری فارس موظف است این خبرها را صحت‌سنجی کرده و با برچسب «راست» یا «غلط» مشخص نماید.
🔹
بدین ترتیب کاربران با جستجوی کلیدواژهٔ مورد نظر در سایت فارس، به جمع‌بندی از خبرها دست می‌یابند؛ چه خبر توسط خود فارس منتشر شده باشد، چه توسط مخاطبان و سپس تأیید شده باشد.
⚠️
این مکانیسم اگرچه راهکاری برای کاهش فاصلهٔ خبری است، اما اصل گلایهٔ مخاطبان دربارهٔ کم‌توجهی مسئولان به نقش رسانه در حکمرانی همچنان پابرجاست.
@Farsna</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/438105" target="_blank">📅 14:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAEBWrvsQYans-BaP7Z-yD7QYh08r2TiJBCVFZ34dTeYVyC6QzO8nQ_jRnGWr7TQPeCSEwd1Gs__w_tOoC3Ul4BMbK_KOmtH2aXfou1lwvrFsJWusBWBFdRdaggVV52AKtimUYW_IWfKr8i32srKvEIXZE0mSCTWxdCJ4XeUIVAICGu--IJQ7QFfGrSX54UpkZiyAGjZDlb19TQzi6x7mVhPMZf8-_LCUkRucE5RN7Z51BS5hwNBjF5e5QEcEu82h9wJF5WKKHrzFcJc_nCb4jiq_GEvW4S50s726AGHcBB4XWF1FXHTC2FS1xzWgBznxa2QzZiOs3vXB2psrsLy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان سراسری برای ندای «الله‌اکبر» امشب ساعت ۲۱ در سراسر کشور
🔹
درپی انتشار پیام رهبر انقلاب اسلامی به مناسبت حج، مردم ایران عزیز امشب رأس ساعت ۲۱ با حضور در پشت‌بام‌ها، میادین و خیابان‌ها، ندای «الله‌اکبر» سر دهند.
🔹
این فراخوان در راستای اعلام وحدت ملی، حمایت از جبهه مقاومت و تجدید عهد با آرمان‌های انقلاب اسلامی منتشر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/438104" target="_blank">📅 14:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شکار یک مرکاوا و یک هامر توسط حزب‌الله
🔹
حزب‌الله: یک تانک مرکاوا و یک خودروی نظامی هامر دشمن اسرائیلی در دو عملیات پهپادی صبح امروز منهدم شد.
🔹
در شهر «زوطر شرقی» نیز یک بولدوزر نظامی طعمهٔ پهپاد انتحاری شده و دو تجمع نیروهای رژیم اشغالگر هدف توپخانه و موشک‌ها قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/438103" target="_blank">📅 14:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9156d4c78a.mp4?token=VigsxfXYhYzlju6EmtmU6_7VuhVbP5rmV8q5zN-iW63nXu2CCKo6j4zvNaZJeNQEY5Zg-k2nwj4HVtDOup92SLQnSNmSkOWFnH6y3jnG3jnQGk1qw_E4m17KdRYdtMCGk7y9rvEf1lm5Dwim9anYmF9hBCFet4gKR9NjQSlb6cbQrd1xKGaUqk0ZAlPOqTqdOvqmiL_NfuMx71lVCZ7CrOQIVslR75PWjF2uKKWuLLRUkzmH9a4h8YKFWlhxpaGxU7jxU5IAEgh56lUfYdh3TP8S9WMk32hfRQx81V_zAjDpALkgxjpiCn2rQUKJ8ftRQtq5_1rYK3_3Mss4GEi-GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9156d4c78a.mp4?token=VigsxfXYhYzlju6EmtmU6_7VuhVbP5rmV8q5zN-iW63nXu2CCKo6j4zvNaZJeNQEY5Zg-k2nwj4HVtDOup92SLQnSNmSkOWFnH6y3jnG3jnQGk1qw_E4m17KdRYdtMCGk7y9rvEf1lm5Dwim9anYmF9hBCFet4gKR9NjQSlb6cbQrd1xKGaUqk0ZAlPOqTqdOvqmiL_NfuMx71lVCZ7CrOQIVslR75PWjF2uKKWuLLRUkzmH9a4h8YKFWlhxpaGxU7jxU5IAEgh56lUfYdh3TP8S9WMk32hfRQx81V_zAjDpALkgxjpiCn2rQUKJ8ftRQtq5_1rYK3_3Mss4GEi-GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
شب و روز عرفه چه اعمالی دارد؟
🔹
جزئیات برگزاری مراسم پرفیض دعای عرفه در تهران را اینجا بخوانید.  @Farsna</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/438102" target="_blank">📅 14:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‌ سفر هیئت نمایندگی ایران به قطر
🔹
خبرگزاری دولت: هیئت نمایندگی ایران به ریاست محمد باقر قالیباف، امروز به دوحه سفر کرد.
🔹
این سفر در ادامه روند دیپلماتیکی است که در چند هفتۀ اخیر با میانجی‌گری پاکستان برای خاتمۀ جنگ تحمیلی شروع شده و ادامه دارد.
🔹
در این…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/438101" target="_blank">📅 13:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhRbMwKur4M30CsnLgO7mIIkaTgETGOuoVyOI5Uwt2Z2OjBGlhjwqbOyCC2zqYcbZafXZsJVLBLT1-gzgzYAcXKbrxpxYCMsAyBRPSpVNmkaEtETf6NsCTnd_KUstYPqyj-6d4sz-s2uL-1G2Cjnk6Dj1IekeWXzsGJ0qMhL-jBRI_JRkrc6H--b4ZYezN6ewjm75sV1URocHo2RLHnzBU3dXpxQqXswiHxB5sfgFZr2Ae0kLWAwYJ6NKOrJhK0Kv0cNqgFJMHp9we_Dr35QYCdDEsPdnxIeV4EXxbXv8E7rgpPW31lWS-LBbqyXgDvaZsxAnE21oKRATsKdEl1GDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در ساعت اول معاملات امروز با جهش یک درصدی پس‌از ۱۰۰ روز دوباره ۴ میلیونی شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/438100" target="_blank">📅 13:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438099">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌ رفع محدودیت اینترنت و تلاش برای دوقطبی‌سازی در شرایط جنگی
🔹
رئیس‌جمهور روز دوشنبه احتمالاً با توجه به بهبود نسبی شرایط امنیت سایبری، دستور رفع محدودیت اینترنت بین‌الملل را صادر کرد.  این محدودیت‌ها پیش‌تر به‌صورت موقت و با ۲ هدف اصلی اعمال شده بودند:
🔸
۱.…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/438099" target="_blank">📅 13:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438098">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtYK0zNH0WxEVcf6vup2bvMxDDYfxNQQzHeue8OT6O0S669oln5MnsD25x0CNBzk3hbp9TRe-w_wOjxUiwmwBVM0oCsBMEvH3Fj0mDGowjCjI0CRI2bOCQejzTOMxPkwIMjtn-oyUxXiuC4_OL4NrO4f5oXAbsgMGNWaOZR_q9nLUD1XI4mDkTAa32J_WsTKpnG-m-x6YPitouf1BMMH5q6Qv0WT8Gvnlwh7_LgQfTfgnbM9MlgNGqSySy6PPC9KvoydTZlBfUbkPo2GgNux7B9HH-ELlC_TlPdBO7sIrLIr3QMrpQSjA0hUmnGx6sswlaM1l3Dxw7lKt5veIy9J-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون دبیر شورای‌عالی امنیت ملی وارد مسکو شد
🔹
علی باقری، معاون دبیر شورای‌عالی امنیت ملی برای شرکت در چهاردهمین کنفرانس بین‌المللی مقامات عالی امنیتی که مهم‌ترین نشست روسیه در حوزهٔ امنیت بین‌المللی است، به مسکو سفر کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/438098" target="_blank">📅 13:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438097">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHgIZ1vOJBpCXFhTU6aJH2rZwcYDju-L0bazrmleDO6vO0NXxmD2N0wUjMY5NzTmAUQOUZp8LFOzr4RZQmwGGY7x2kAYf9L_EcGFUhsyOI7B6NOIeKHY3ywn4Ob8HEvZ4hY7HFwfKw5LiToNEufcsVmxvMwbAhk3LVOnx_GWpDeLD5g_L34NUGnBMxd_o9bYrIxwf1p2_7PlnqBoB3ebSeaDGmdpFoxsoDpPbcVFk3UKMjhrnTWahZhmhOd2mrQ0scHoj3c43q1hdriWuQfgeIczGQdfhTUQX8azbYc4QHhzQS0zXKFXfPccN_RDnE-0W2dkf204DgN1zfFVGzab7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود خودروهای آفرود به جنگل‌‌های هیرکانی آمل ممنوع شد
🔹
دادستان آمل: هرگونه تردد وسایل نقلیهٔ آفرود در جاده‌های خاکی، مسیر‌های فرعی و حریم رودخانه‌های منتهی به جنگل‌های هیرکانی مطلقاً ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/438097" target="_blank">📅 12:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438096">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‌ شهردار تهران: مترو و اتوبوس فعلا رایگان است
🔹
رایگان‌بودن حمل‌ونقل عمومی با تصمیم شورا آغاز شده و‌ تا تصمیم بعدی شورا هم که در هفتهٔ آینده گرفته می‌شود، ادامه دارد و خدمات رایگان مانند قبل ادامه دارد. استقبال مردم هم از این‌طرح‌ خوب بوده است.
🔹
پیش از این…</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/438096" target="_blank">📅 12:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438095">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qF_0Wm2vK9-8sRNLWExR8zyfrxj1-SPW-viWYW1-uOIU7kT4OA84DP7_60ELUX1KCrswyF3IjmzpEge2oZKq-PfsF73fRxljzMbgGRUoDdFTSWnNYo0FDXCN16QF7ys9fBkl-NnsZXIhsZsd1WpEhI7Jni8584XbG2EolL2NSeEKgeUYoIkFnhsu_X3moLFZnPxcWLd9W5jEJBb7DkyFiVDgG_tkKg61d15Q3cmQDUrRJVqGHL4hqGi2jSb9b0FzG_u5PZP8uii12Cy0Nqp7_r4DU0UP81uVL7XKfx7L8FIAhBjV6auQ7i0usZJsVACwWPhUqDIk4jKYWMEU-RbwIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمان بازی ایران و گامبیا معلوم شد
🔹
تیم ملی فوتبال ایران، جمعه ۸ خرداد نخستین دیدار خود را در آخرین اردوی آماده‌سازی  پیش از جام جهانی ۲۰۲۶ مقابل گامبیا برگزار خواهد کرد.
🔹
قرار است این بازی از ساعت ۱۹ به‌وقت تهران در ورزشگاه مردان آنتالیا برگزار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/438095" target="_blank">📅 12:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438094">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZW3GrksQP6Oi0BMCIwn8Kxdj8zfQq9fgZkvWlYPQO2PlgSi02bvmwHm1DHSlYgOUNttirXXYbgMAHsgObKZAfdp5QmLxtQv5Sjt3ncrYZ0V9hIBDpuwi3cw9xnNbYIQwc4VXpzEvVgaEFCghe12-gXftqpvhNS1s28ebCtP4zM3uxxyLCbAxNh5uqxQwRoimsLiY3v4KMx2DfR5na_c4Ch2dNJLAGvgn-Rx1IARJsXuBN0RwGNwLuZ6J4Xe8QxZbPI97U6nTG9sLpJt3g_XVyKjfAjGPInrSzGxloQkDyAzV_8aZqf52D3uJraROnThvjwUIVdgw8HjOyjn79EoOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی دولت: برای بازسازی‌های ناشی از جنگ تحمیلی برنامهٔ‌ بلندمدت داریم
🔹
موضوع ارزیابی خسارات ناشی از جنگ در ۲ شکل مستقیم و غیرمستقیم دسته‌بندی می‌شود؛ هر یک از دستگاه‌های تخصصی درحال ارزیابی خسارات ناشی از جنگ هستند.  @Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/438094" target="_blank">📅 12:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438093">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSkmqxZefVCLLYn3ulhBlOUasOw-KKA3oGuvMoKxMhZ0XOi0TjeuFqZdopI-b0QbqcCyuiPzkNhigctOcBhmQW5UlsHSbz5VDtBuXn3cnfC5sv6zS29EldKs4GXvKqy8wEOQ_a1gXLgqrX2M3BPEIlHmKt-6NS2eO5MBPFa5QbLHE2v_hDEOnTgmenygRZoHUY31VDXcLcipmbmNKjqdPu45Q_kRKRjN7-5srXpRAk8otbFEJhte4yQs41BjZBpnMb8Bm21qEovzYFeZeR3Q1C4n4RwhxyJDGgpR4kgOm-KzC5KRONCwf7FyaE23xNd6ZaLtDH3g5dotL_SP3Mbgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسری بودجۀ میلیاردی قطر با بسته شدن تنگهٔ هرمز
🔹
قطر که پیش از بسته شدن تنگهٔ هرمز سود سرشاری از فروش گاز به‌دست می‌آورد، حالا با توقف کامل صادرات، کسری بودجه ۲.۸۳ میلیارد دلاری را تجربه می‌کند.
🔹
صندوق بین‌المللی پول پیش‌بینی کرده که اقتصاد قطر در سال ۲۰۲۶ تا ۸.۶ درصد کوچک‌تر شود چرا که هر روز بسته بودن تنگهٔ هرمز، صدها میلیون دلار زیان جدید به قطر تحمیل می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/438093" target="_blank">📅 12:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438092">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvwHWRmsf0HVDEHyn9ZVuOamDgACMUCIUu11fDmDDdlt-1y3RUQheeRLNABMHeB8tcnC_IY7tKuHxElCbriEmF8jHhK2NsKc1elEUs7OXMxapAG1MD6hRzBrmGNk1tgMIiKD87E2RbnUleW2u6rFjZ48lsXTa191DSQF0pqOBx3hPDBhRY1dJsnfRLWUt2fUSNSr-uDGZ1QVq__4_WslHfBonPSi9XcWzBgBbHd-qXnOwK5CWWQoTSDB6jdVWwMzIuh3_iParnzxJiWKWmBSxgXTJ0NAEyLsVf5liL6RTJVLiWo29rkVh6Yw9iqLFiiDyzzSRmklwPyRY22LjM_jJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی دولت: گسترش کریدورها در مرزها در دستور کار است
🔹
مرزهای شرقی ما اصولا به اندازه کافی توسعه یافته نبود و دولت قبل از جنگ نیز گسترش کریدورها را آغاز کرده بود؛ کار بر روی یکی از مرزها به طور آزمایشی آغاز شده است.
🔹
پشتیبانی، لجستیک، اولویت‌بندی ترخیص کالاها…</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/438092" target="_blank">📅 12:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438091">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzQOe2x-NO450ivV0D5jyQ6gWbP7bokVFaT9eubItMVtAdTktceqtk-7tAna5q4nDXv1dlSHvfbvA9NZEKAZibdYLe7fTZWEix9TtZMYCa8EwKyH-BpzgF4ZlldzK-JkSrT3fDUoJHUazvy26YRDnfDMdmBvsswZkk_l97gndEU5j2djXo834ZpPE9NvSUoRZyaLXl-nNwLg5LkHxsBGG-zNd5MmrpfmtKLX5FKAReG8cK8EqFkZTalnXIcjLgqkH3dp_Lh_M1C2i5O90j9vKws8v2YDo-5kP0-M7XAlOHgTYvRzOjGat0mPWhlfMwkCNR2xUtp8W3AKZxvTn6ohZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  قیمت مرغ درحال کاهش است
🔹
براساس گزارش میدانی خبرنگار فارس، امروز قیمت مرغ در مناطق مختلف تهران از کیلویی ۳۹۰ هزار تا ۴۴۰ هزار تومان فروخته می‌شود.
🔹
پیش از این، قیمت مرغ در بازار به دلیل کاهش جوجه ریزی به ۴۸۰ هزار تومان رسیده بود.
🔹
یک مرغ‌فروش منطقهٔ…</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/438091" target="_blank">📅 12:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438090">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhMpYoQT_t68MK2fRpZykDNaxRThZeGTiaC6amr05lTfc9Xumpd5ZlUHxmgj0KxMssGIsUOCp1a49kB_QPweZ9-yRxrFYxgGccZcu6OGkJUO2DLjdkQ1CGEZBlgIxpw8aWaExKdiYqDuGhPouHQJKJIRMQwcS9M6ecvytDUB8aHIb8ifkNLchIKQ-1M--X4heL4Vv0DzQSf3te9NXmNLwH4OgkTZZZgNEiiitmaleCeifTzUDxuGVgesWMowz-nhsimxgxmsXydSTJI3cf6oHicVONW46q6yJ3EWrew_BvJHVI0JZqUOh-KlI-z7TESxfBLhGMPqBZ_7UL2sEN3Kow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی دولت:‌ افزایش مبلغ کالابرگ در دست بررسی است
🔹
یکی از مهم‌ترین وظایف دولت‌ها این است که تورم را مهار کنند؛ این کار را با نظم مالی و بودجه‌ای که دولت پیشه کرده است دنبال می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/438090" target="_blank">📅 12:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438089">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHsxLw_DJzqo5Lz9VjSLGBM1oFBG7VZ1opEX7I7VgFDY0fLZFBk0BRRVIwcnlBb3xYG08r6UwmVgll-Ljee5d2atzUBeJLJOLKrWqwg_x9fkMafV6CLSizovuNmqmRCfiZSiGvAR2E5VTNoFD7Br6hocOBg7rSKz6oX98qxuTyXJZbVkbRH0DstPSZePHoDI13e4iUAEUkqeayrhDBr2-RdwkUyFXnfG2xoNTv_yFC6khI0qFKd8fRLA2fOQFwRRgVZdYHo-Rp8fVvxwTjAOojo5KZ8fJ1ZFb_l5ABAiixfMTEnyhcgJHjwc9f25yR0H2wbfStqP6-ktaQcT4bZmGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی دولت: بودجهٔ وام ازدواج افزایش می‌یابد
🔹
رقم وام ازدواج در بودجه، از ۲۰۰ همت به ۳۵۰ همت افزایش پیدا کرده است؛ این افزایش با هدف دسترسی بیشتر جوانان به وام ازدواج انجام شده و رشد ۷۵ درصدی را نشان می‌دهد.
🔹
دولت همچنین در تلاش است مشکلات تأمین لوازم خانگی…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/438089" target="_blank">📅 11:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438088">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سرشبکهٔ جاسوسی مرتبط با موساد اعدام شد
🔹
غلامرضا خانی شکراب، سرشبکهٔ سرویس جاسوسی رژیم صهیونیستی در خارج از کشور که در یک عملیات پیچیده به داخل کشور هدایت شده بود، به‌جرم همکاری اطلاعاتی با رژیم صهیونیستی به دار مجازات آویخته شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/438088" target="_blank">📅 11:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438087">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0befa76344.mp4?token=T9Z0Jh7S1aV_DgYHUvkiUeVU3eYPY4rTixMYbj5ZdBvagfwO6HT75E8SdHGVKbfzkY8u3KrC0Y8VIWaemieLeVmLKeynpltYmiD8WOb24GwW3cOHTPG6eD1FPXCaKp62Lny_yUAr-u99FVH-rd4OoAWeQq1x3reL07e9ANNf0fE1q44diFa-ZEk3EqWO3rxWdg_D76eBpXgA9veVuiJdep-_ySKSudCn3JBtZNdncrR78pann2u29Q7pVeJ6jKlDLoe8pVrDQecwRFR8rrr21mD0lpRXatAsgceonlK636vaMCIIihkaz5jbxKe_Po0A1CB7-d4udMacsHId1qA_4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0befa76344.mp4?token=T9Z0Jh7S1aV_DgYHUvkiUeVU3eYPY4rTixMYbj5ZdBvagfwO6HT75E8SdHGVKbfzkY8u3KrC0Y8VIWaemieLeVmLKeynpltYmiD8WOb24GwW3cOHTPG6eD1FPXCaKp62Lny_yUAr-u99FVH-rd4OoAWeQq1x3reL07e9ANNf0fE1q44diFa-ZEk3EqWO3rxWdg_D76eBpXgA9veVuiJdep-_ySKSudCn3JBtZNdncrR78pann2u29Q7pVeJ6jKlDLoe8pVrDQecwRFR8rrr21mD0lpRXatAsgceonlK636vaMCIIihkaz5jbxKe_Po0A1CB7-d4udMacsHId1qA_4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخستین نفتکش ژاپن پس از عبور از تنگهٔ هرمز به سرزمین آفتاب رسید
🔹
ایران یک ماه پیش به نفتکش «ایده‌میتسو مارو» اجازه داد تا از تنگهٔ هرمز عبور کند و نخستین نفتکش ژاپنی باشد که از زمان حمله علیه ایران از این آب‌راه عبور می‌کند.
🔹
ژاپن که به‌شدت به نفت خلیج‌فارس وابسته است، هنوز ۳۹ نفتکش دیگر در خلیج‌فارس دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/438087" target="_blank">📅 11:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438086">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9bH-ggUvjWfQxdGIbqhgD-Sf0RVjnE-OMIeGePi5o_LDUoqnK3L3iTI3Ga3VX5MfT5YDzY5I8a4eO-seKBjseW97uV9tR5CBGZgqGGXydu7LlVagk2nPVIPs588aQxfGFoesi0JXKIsS-qn1340MAiIpZr3_bwnrePUDBnSWR6lFmy3qspQR_LZkKb9RTU4DbJXxDCpEpvQ3GCDM3jdO_mWcmRY4NJU9a2SLa2JZiiqB2JJO_MxoYwgBAh7vbAqyxnmB0YlTMQh6XacO0aS2FuDH4kJJjEHB9xe0yXoNU0sjmbiuSjMPKWhny94eUbuURWegVjAC1xRnXQHKUIPzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی دولت: بودجهٔ وام ازدواج افزایش می‌یابد
🔹
رقم وام ازدواج در بودجه، از ۲۰۰ همت به ۳۵۰ همت افزایش پیدا کرده است؛ این افزایش با هدف دسترسی بیشتر جوانان به وام ازدواج انجام شده و رشد ۷۵ درصدی را نشان می‌دهد.
🔹
دولت همچنین در تلاش است مشکلات تأمین لوازم خانگی زوج‌های جوان را نیز کاهش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/438086" target="_blank">📅 11:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438085">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSND32_hpNDzIycNbD7QzwbUXlv0sFFW7XH8bIjcg04H_DUUz0EQ3GEVuc7qGxFxmAqs4xa5U_YNoUNStZVjHkfDamuBI3yiXRzrP9bxfN-YpII5xMq24DFFxkxRC5QFGtgmuD2ajlTRx1AdbiidE3fEsthqh63Zyozv4NIb1zSRXftBD2oqcvSH9Bti6JMMb0bUUBXpvGxLONYgzhmVdVy0PTpUV8YnzXjtwiwEGENPmAjD9r63Qm-hpwxVj0-5eoONN5h7o5xzVB8txKP9R3fkf45rEFFaPyOXToZiBYeJ3XjYhNuvN3SLsN0wbybkHccT102XPW02-9Xtj093dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: اقتدار دفاعی کشور مدیون آمادگی نیروهای مسلح است
🔹
رئیس‌جمهور در نشست با فرماندهان و مدیران وزارت دفاع: دشمن هرگز تصور نمی‌کرد نیروهای مسلح جمهوری اسلامی ایران از چنین توان آفندی، ظرفیت عملیاتی و آمادگی راهبردی برخوردار باشند.
🔹
کشورهای منطقه به این…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/438085" target="_blank">📅 11:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438084">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSM13RuZqtWcmxtOW5vcoccBHTEo-oq2Cksf1XYGDKuCH571W_T8teXiHB22K-p6FOy31ex9voDw3mSTheDkZece7pzkbj0L3hMK7emgctNwA87wDpWXdAI42Tzmg_WuAk5rrLeSw1-ezbyNjD1ICOyS4c9pb-cx0THWTq6FKCDxWwIfbUiv2GFbGzvssvbWOReuGz-_7gVxwyiOmezB6hRz5OMymrCddud6-wQZgxzqAU-qfgnvK0d_XEPHk1YPRNaUC8hgZO4HQh0zMNhA0GnncZDO6nvk_F9Axah6pUpz41rzbIp_n9opAgKHl2IZiHzkWfgpSEE-v8cVmbe8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: توجه ویژه به خانوادۀ شهدای جنگ باید در اولویت باشد.  @Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/438084" target="_blank">📅 11:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438083">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7741215637.mp4?token=W-S1LeDFECyNVIGNs_NwVMtLSQ-GBSihjONzzKjz7eRa-qpgc6Tgh6nlrPC8A-an76nAaZCJa-_pcVwNwND9jm21q0qBTBV6pEalnefUFQSueQMvtnxn8Z9ocQ9cEORvIMVRFlDgeTvzuUiIZdaiph2P7IYGvjuGua6Wvb7E6iZjZWFwzu5d93CGGAhGw5wT4BpG7oOi4SrZZ-iMh4ki4bUgxb_n08xCDIPcJUtNy1ogHm_BJW73GA2vkdPboJjHGw6uYEAz6gf3k-vks3h5D93ce99kkd3bb_GTH7qgBE9HB_nWmoO54Ee47jts-2qOROdNikcz3KvwFVBppFsS9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7741215637.mp4?token=W-S1LeDFECyNVIGNs_NwVMtLSQ-GBSihjONzzKjz7eRa-qpgc6Tgh6nlrPC8A-an76nAaZCJa-_pcVwNwND9jm21q0qBTBV6pEalnefUFQSueQMvtnxn8Z9ocQ9cEORvIMVRFlDgeTvzuUiIZdaiph2P7IYGvjuGua6Wvb7E6iZjZWFwzu5d93CGGAhGw5wT4BpG7oOi4SrZZ-iMh4ki4bUgxb_n08xCDIPcJUtNy1ogHm_BJW73GA2vkdPboJjHGw6uYEAz6gf3k-vks3h5D93ce99kkd3bb_GTH7qgBE9HB_nWmoO54Ee47jts-2qOROdNikcz3KvwFVBppFsS9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: رژیم متزلزل صهیونی و غدهٔ سرطانی اسرائیل به مراحل پایانی عمر منحوس خود نزدیک شده و به فضل الهی و مطابق با سخن قاطع و آینده‌نگرِ ده سال قبل رهبر عظیم‌الشأن شهید قدس‌الله‌نفسه‌الزکیه، ۲۵ سال بعد از آن تاریخ را نخواهد دید، ان‌شاءالله. @Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/438083" target="_blank">📅 11:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438081">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
سپاه: یک پهپاد آمریکایی را سرنگون و پهپاد و جنگندهٔ آمریکایی را فراری دادیم
🔹
ارتش تروریستی آمریکا در ادامهٔ ماجراجویی‌های مداخله‌گرایانه در منطقه و رفتارهای متجاوزانه، در منطقه خلیج فارس وارد حریم هوایی ایران شد و یگان‌های پدافندی سپاه پاسداران در راستای دفاع از حریم سرزمینی کشورمان پس‌از پایش‌های اطلاعاتی دقیق، یک پهپاد MQ9 را شناسایی و ساقط کرد.
🔹
همچنین با شلیک به یک فروند پهپاد RQ4 و جنگنده متجاوز F35 آنان را وادار به فرار و خروج از حریم سرزمینی کرد.
🔹
سپاه پاسداران نسبت به هرگونه نقض آتش‌بس از سوی ارتش متجاوز آمریکا هشدار می‌دهد و حق پاسخ متقابل را برای خود مشروع و قطعی می‌داند.
@Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/438081" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438080">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: امت اسلامی و ملت‌های منطقه، ظرفیت‌ها و منافع مشترک زیادی دارند که نظم جدید و هندسهٔ آیندهٔ منطقه و جهان را شکل خواهد داد.  @Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/438080" target="_blank">📅 10:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: آینده متعلق به امت اسلامی و تمدن نوین اسلامی است و هر یک از ما می‌توانیم به‌اندازهٔ همت، ظرفیت و مسئولیت خود در تحقق این آینده و نزدیک‌ترشدن به آن ایفای نقش کنیم.
🔹
زائران و حج‌گزاران ایرانی در حج امسال نقش مؤثر و برجسته‌ای در روایت فتح جنگ…</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/438078" target="_blank">📅 10:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: امسال مسئلهٔ برائت از مشرکان اهمیتی مضاعف دارد و عمق و گسترهٔ برائت از آمریکا و رژیم صهیونی، فراتر از آیین برائت در موسم و میقات حج است و در نقاط مختلف ایران و جهان پس از این ایام مبارک، مرگ بر آمریکا و مرگ بر اسرائیل، شعار رایج امت اسلامی…</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/438077" target="_blank">📅 10:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: رژیم متزلزل صهیونی و غدهٔ سرطانی اسرائیل به مراحل پایانی عمر منحوس خود نزدیک شده و به فضل الهی و مطابق با سخن قاطع و آینده‌نگرِ ده سال قبل رهبر عظیم‌الشأن شهید قدس‌الله‌نفسه‌الزکیه، ۲۵ سال بعد از آن تاریخ را نخواهد دید، ان‌شاءالله. @Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/438076" target="_blank">📅 10:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438075">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: آنچه مسلم است، عقربهٔ زمان به عقب برنمی‌گردد و ملت‌ها و سرزمین‌های منطقه، دیگر سپر پایگاه‌های آمریکایی نخواهند بود
🔸
آمریکا علاوه بر آنکه دیگر نقطهٔ امنی برای شرارت و استقرار پایگاه نظامی در منطقه نخواهد داشت، روز به روز از وضع سابق خود فاصله…</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/438075" target="_blank">📅 10:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438074">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: آنچه مسلم است، عقربهٔ زمان به عقب برنمی‌گردد و ملت‌ها و سرزمین‌های منطقه، دیگر سپر پایگاه‌های آمریکایی نخواهند بود
🔸
آمریکا علاوه بر آنکه دیگر نقطهٔ امنی برای شرارت و استقرار پایگاه نظامی در منطقه نخواهد داشت، روز به روز از وضع سابق خود فاصله…</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/438074" target="_blank">📅 10:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438072">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: با همین سلاح «الله اکبر» بود که رزمندگان غیور و نیروهای مسلح جان‌فدا در ایران اسلامی، با همراهی مجاهدان جبههٔ مقاومت، خصوصاً لبنان عزیز، به پیروزی‌های چشم‌گیر در برابر ۲ ارتش تروریستی و تا بُن دندان مسلح آمریکایی-صهیونیستی در جنگ تحمیلی سوم…</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/438072" target="_blank">📅 10:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438071">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: سلاح «الله اکبر» چنان قوت و نیرویی به ملت ایران بخشید که پس‌از واقعهٔ جان‌گداز شهادت قائد عظیم‌الشأن، فرزند خلف پیامبر اکرم، حضرت آیت‌الله العظمی سیدعلی حسینی خامنه‌ای (اعلی الله مقامَه الشریف) به‌دست اشقیای جهان، امروز بعثت الهی یافت و با…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/438071" target="_blank">📅 10:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438070">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: این سلاح «الله اکبر» بود که جمهوری اسلامی ایران با تکیه بر آن موفق شد رژیم صهیونیستی را در جنگ تحمیلی دوم در خرداد ۱۴۰۴ زیر ضربات سهمگین خود بیچاره کند، سیلی سختی به آمریکای متجاوز بزند و دشمن را در هدف خود مبنی بر تسلیم ایران ناکام کند. …</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/438070" target="_blank">📅 10:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438069">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سلاح دشمن‌شکنِ «الله اکبر»
🔹
رهبر انقلاب: با سلاح «الله اکبر» بود که ملت مسلمان ایران در ۴۷ سال قبل قیام کرد، رژیم طاغوت، دیکتاتور و وابستهٔ پهلوی را ساقط کرد، دست و پای آمریکای طمع‌کار و مستکبر را از کشور بُرید و نفوذ صهیونیسم را به‌کلی قطع کرد.
🔹
با همین…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/438069" target="_blank">📅 10:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438068">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elJJBWHsVWooJJGL02rnyb3T72sG4Lp2oUApMWel7BuCrpcdCYo0VKClbQ3pYS85PpjLdSbr-TozPck2nS3YfAuPgO2MIcrTeYOLbVbCgjQ6Ma6h-pytEgHwQWL-tkHq1TDdipTJCFMgCbRWVLzFT1PidjCgtq33FyJ3YDv_NVyZVYHNuqwMj98fyLXKBVPteEER-XM-iA3L0_ZJvDYSvn4hO3ughTLP-7lSvCjTsMIPlqM9JhGRzm7oWdFT35U-qY7ORsBDe7T87HOyMA8-JeECQbrhCKE4St6eExpWrCbCjwo7fJnoNbCwLUfIoTzg38fYLFJEck9mLQz-DdDDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انقلاب: ملت ایران در انقلاب اسلامی قدم در مسیر هجرت به‌سمت زندگی الهی گذاشت، صلای ابراهیمیِ خمینی کبیر(ره) را اجابت کرد، لباس سلطه‌پذیری از تن درآورد، اِحرام سعادت‌مندی دنیا و آخرت بر تن پوشید و لبیک‌گویان تلاش کرد تا بر محور معارف اسلام ناب محمدی…</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/438068" target="_blank">📅 10:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438067">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پیام_رهبر_انقلاب_اسلامی_به_مناسبت_برگزاری_حج.pdf</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/438067" target="_blank">📅 10:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438066">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام_رهبر_انقلاب_اسلامی_به_مناسبت_برگزاری_حج.pdf</div>
  <div class="tg-doc-extra">415.4 KB</div>
</div>
<a href="https://t.me/farsna/438066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔴
پیام رهبر انقلاب به‌مناسبت برگزاری حج تا دقایقی دیگر منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/438066" target="_blank">📅 10:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438065">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سپاه اصفهان: تا ساعت ۱۳ امروز احتمال شنیده‌شدن صدای انفجارهای کنترل‌شده در محدودهٔ جنوب شهر اصفهان وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/438065" target="_blank">📅 10:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438064">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎥
خاطرهٔ تصویربردار بیت رهبری از سفر رهبر شهید انقلاب به مشهد با پرواز عمومی  @Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/438064" target="_blank">📅 10:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438062">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1clheqge7bGcYXeJrojd6F0f8JlYSI7_76HnjF8KngZrX6yRhoT50bP6MAUejMywspQSxV7I6zh7gjZ4z2npBZEYY-mg4b2W0NRDNX_XYFnA8yOSsZQmaPIle8aeTZMbOU-qgEHSWlLtb7HSOxOZF8uVOdUcxnErbQMMJXdNJK1nXIfdeCNwTD-On6uIol9w2GdTNbojwlx8u66yEUJcC-tlykm6LJGPzyUmSgkvZNhDxjhmFhjNVYPNz-2ezy6OeSjbJU_yyfd9g4NeOzzXRzNLGeHfV5-297ibzWHPxQGJmYDEazWxtGBcP0siniF5tkxQjaZeeLBr6jgr57gLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانهٔ صهیونیستی: کشورهای عربی به‌دنبال ائتلاف‌ با ایران هستند
🔹
روزنامهٔ هاآرتص اسرائیل در گزارشی نوشت: اعتماد کشورهای خاورمیانه به آمریکایی‌ها با جنگ فعلی تضعیف شده و به اسرائیل به چشم طرفی نگاه می‌شود که منطقه را وارد وضعیتی کرد که باعث خسارت‌های سنگینی شد.
🔹
کشورهای حوزهٔ خلیج فارس با این جنگ فهمیدند که نمی‌توانند به آمریکا تکیه کنند و به‌دنبال ائتلاف‌های دفاعی جدید، از جمله ائتلاف با ایران هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/438062" target="_blank">📅 09:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438061">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyyKIceBtY4_dLj-QNvGDbmqJactFLZ-BnN3BDXhZK4lg51J_VNYqiLvXSgRf2srE-vrr8bhSLPa8fkxReEOU1og-a6KfY85kuUQHOT_1C03Q37wSUuzlV7tz4LjgGlYMJgpMmqlFJGmLaqjMSTpaFwI87MYVuOgU0E9B2ILe-ZZWv4heKrHGj8-W8EbN7q3cIyZDyfTNdxIDQjjtiu49KB6lyX5c4rcKtlCNfLOBt4U8ihqz8iFaUsF9eqnR-A0f3nG6UXtomFjqmH_1jzqWP9rKvtlBJNrqngY2kdEDKX29kXVQpMlUPVi-GqJhJcflsV8PKGhLg-d1tgTQa0FiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در ساعت اول معاملات امروز با جهش یک درصدی پس‌از ۱۰۰ روز دوباره ۴ میلیونی شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/438061" target="_blank">📅 09:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438060">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
پیام رهبر انقلاب به‌مناسبت برگزاری حج تا دقایقی دیگر منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/438060" target="_blank">📅 09:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438059">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bngS3xgdwnjgSjzli3KvEWfttHc1rR6YEjVTiHbNoqI93LYNhn3DILml60G1SDG8RS75_W8zK5x5meCGeokHtv3lz_UloL66sN2N-Fwvptuy8YZIX-Pw_Mds8OXM-Am5gRRCmaGAYrumDSfoR0IBdu9SxMpauonNhIULRn8YYLasDvtBpzMrSountMXma4eKad3VmuICPvl0q5gOgm_9QePqwmSCzRgKTmxoxNLk9Wb624of2vAyASRCIxcuG6eQkeo5Nxhp6EZkNaDePOsoH1DNe1KHaLKwqiLxURGNDBMoz5rlxqK8Vvqmu4-qLTchAlsQp7ZvJ5xAGArauGzNsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار شکارچی: در صورت تجاوز جدید پاسخ ما فراتر از منطقه خواهد بود
🔹
سخنگوی ارشد نیروهای مسلح: حملات ایران در صورت ورود منطقه به دور دیگری از جنگ فراتر از مرزهای منطقه خواهد رفت و بسیار شدیدتر، سنگین‌تر، خشونت‌آمیز‌تر و قوی‌تر از ۲ جنگ قبلی خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/438059" target="_blank">📅 09:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438058">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/femtBSausd_4rwdNfWzwQWtc0SMTvezP7Yr7kZ3BzHKaSfVF7nVwBD-5Kh6RnrmrH_tpQJeOXul6xnilIZ00NKl2vn3E2DpFpMYugyEmJK7oTUHKRWpwPIMBoZYEgXLEFmFPSyDz2eKXUcFxqn_HkBBkt8N188yoIFSOteUrb61S1XCLyIQZ6Zc5z-dnfChZvsgpwrhrflplPImqpyqKgx1ZFWu4g2IQyieNGmhAzePg2aRa0KcApEGMjBStQe2chBbYifQzOu5eWGdtUjNHjrJb26gmDUx6qc45aGTzu13IV69QOOqUFuY9PcTraS2b71najydW4sn7nB3_ywGjnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: هزینهٔ ترددی که در تنگهٔ هرمز دریافت می‌شود بابت اطمینان از تردد ایمن کشتی‌هاست
🔹
خدمات ناوبری و اقدامات لازم برای صیانت از محیط زیست طبیعتاً هزینه‌هایی دارد و نام این هزینه عوارض نیست. @Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/438058" target="_blank">📅 08:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438057">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkHtiFbNoDidqwF2WVfJp6U62TRCkxCa8Pk1YRvemuZ7YmFIBD_Y2dCAKLUqm7awTll8Q30kP20mjvGNeq5UK6xWsra1-Kg46ycqWJWTlg5WMMVuDCRQDwSu3L39ssf7keym_W52qcTP9H5DF-5d8Xy2FoTNUjQomvJvmp-tE7iO5ig_EpkLQDQxEye7u6iyeLDRTLx_y0MGUwj--0AlE19Le9EAL1G9LB-Ci9ypRrrvVc0KhuSIDHmQ6hXlNbpPnPXKj-BWt3JKVrkeF8-rgopGOtTc_2YuBse52syDd0Zoh1AGl6DhhMWXS31GG2kOWGujMuGkMc9qPgclRjdu5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
شب و روز عرفه چه اعمالی دارد؟
🔹
جزئیات برگزاری مراسم پرفیض دعای عرفه در تهران را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/438057" target="_blank">📅 08:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438056">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیش‌بینی تداوم رگبار باران در شمال غرب و شمال شرق کشور
🔹
هواشناسی: امروز سه‌شنبه در برخی نقاط استان‌های آذربایجان‌شرقی، آذربایجان‌غربی، اردبیل، خراسان‌شمالی و شمال خراسان‌رضوی در برخی ساعات رگبار و رعدوبرق، در نقاط مستعد تگرگ و در ارتفاعات استان‌های ساحلی خزر بارش پراکنده پیش‌بینی می‌شود.
🔸
امروز آسمان تهران صاف، همراه با وزش باد، در برخی ساعت‌ها وزش باد شدید و گردوخاک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/438056" target="_blank">📅 07:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438055">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a08Lt6HUhFGk2sdjdI4-ENjzcknhXKOYye3VjYpOyWg5UdKR2x51XaA2QwM8QSbtDQYjmtD7ffllpAmpBpdFd500phlIGBCuk1YvcldOzX8UcQrY8N6dhOcqrqqjhvzx__Ypv8DwIiCpbR7aOiy1pRo4KgvilYX3DK7aFtOGE5mzlblQprZJ6qrAewbNjBv9nfhA4y-xeuBEhBZYBdCWf5kWvB7lbYHLCnKV7dpHcZrV5-F14tPzFMA1izHmKQJ5oEgxjkSyuWd9oSyyoURwhtefykUBX5ltMD-vQHdZk2B4gza2N898VVeECwjKLGOiaHCflDHctXrVVyk2A4Dkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاریخ برگزاری کنکور دانشگاه فرهنگیان مشخص شد
🔹
دبیر شورای‌عالی آموزش‌وپرورش: کنکور دانشگاه فرهنگیان از کنکور سراسری تفکیک شده و این آزمون در تاریخ ۱۱ تیرماه برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438055" target="_blank">📅 07:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438049">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LV5q4PpVm7bfddIRXOx424tBXYrst6aNuteldah04g_CcWdHU9hjqTgXn0nx6RjnolQZbM8uIGw3AvN1xNcEe8AHOp0MZPGmIpYRXNh_6QXqSc1xQgc0OYOI9ZVHd-E8Sv0EF8oEybKyNnkAnWACqMbF57MJRht_IAdfp0eZOvDDPf8qxf1Oi09rg-lz8v4eFlLbuxmbswX-bxeI7ztiAhe-Rhxu54Qwi_eMfJOTU_KrkxqSiEC-u4rLCVQgRoNqUQywZzzPLPrqhAO50gE0b-OruOftgWKbKDmi-Dge3IwXgT-nfRby99mzUquqhrjSk9vAh_RpNU0VLA879Qau7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEDsjnQPLrxfjV89mxPeIFIS4Drj6Aqkxp4pY4QJPaWHraePIcARAkBy7mt93Oy8plejsLrbkHJwMij0ftU8DoilTjksIMoOwhEH8m1Zr4guL0RCjEPEJzrv-RVpH-pPiTcy3dIjkNl9iLoyAS1GR-tw4vEaTuPcB4JwMou48rJcw5f0SoTTJOhUAl1E_l77e3LEnYUYJqP0GuNw1TTTV8W4K-JDtgdhlJbGsj8Em96n-_OjzopBQJ-ez48kEOpAunGCC33rEv_BqWck0ayoVGTpDZm8tzslx_an7FYLnP4kU5kmFtvumzpcd_ZXl3opgUseDhUYlGn5JswI2KEx6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZB2R5RHFH7kUciV5F3kI6OgY9kZ6Uqq47NLLygIkztEnb3fr5zrOx4qtXGvkQESrgMC03yF5t-fsfiPUCoUsmrVF_Ub3miVtZnH0plufjdyTu8b0gExLeNBKbgJpnlD58YlzbhbO5AIX6lhTLR0dBHKN9bEK20ou2Y-hm5Wy-PymJG4gGSNaPOwOhKXRJo4QdxLfG2dRHWYoAVQ53iS62ilxp1uXtOEL5Hz2X7UGU0d-O0G5MOwfPcsP_TJJ0sXpuNVm-QR-Ay6SeLz8DwpP330SxV6WNpoORIhJ8NMrezD2wBUAXanbeeaPgMyAuEUH9AXFce4XdNXmCpHRb0HDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwoJjUDS3qookwyWSS3ggEDpdD_VoChUirAgQjfCq9dZWnsHloucFIB1bRD01Z0PCKWN9FlRx9nFal-zHT-cikslbul45YFVdRuU7xnChuMJ7GJBO90FcV6AyvXvdZMBUyUwxA48D8i_9jWVOOzZf0nhtx_BPRqTUNz6JDPFValyKo2inrQLLAEPWXujWzEsgPGfvAMm90ky_q2C0085h7vfuByBXtlBCm07oASuEOs3F9KJ09EDKWs7fAWgxAP3CpXnvthmvBCJWXRfYuDS1yJ5F0ELjDyq31plDHpO-pSvlHdXt-obSsJm-tgiT_zUoc-SDDG5oOycfKFEB8cGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYgoBEsCtCJko5RZuNeXqKGL8zHvfIxInaOST5WkfHAsIxAfuSjI0baIV28-TRB54H5Sqhhdw4N6WOBSCnZFLJ9d_XERLslMI2_zeZB6cGCRIoAzV4M8S8NpO8MCDpk5PMR6r-OLKl9fi-P57oo9F7WTPYA71OsQzceffnlfVv2TK2XCxZUXv0WPlqI9xYb2ZHkAWBGQGM7I4B2-jt18xdxSSu5GY0H133IGFdHwp5SAJuD6mTR-3Tj1BKSXECi4mduF8kIS5JZWaBlJMdtHiHsC8zkcH4m0K-5k5FnJxSJajMOLfJou68wICcYlwEKz6MaM1nMSpEZGNCALPzwLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUv_72Sf6YSisJDTaeVqefqo4KhGn3Z0m1rJ1DkR4TQxpuyH3OhDHZCcl3imd6qdevxUdnxFGE1pMHrgPgrhqs8_uJXObGhUBuEgoD-dLy671jqGnWC_xN5KzBkufhm_Ti_ySFZbacUNKSAXRe2MoPTN0Q-MV0Hnr-dYydFeF_w1DT1jujax4ntIRJhbbgHQdVYVDStnA2uS8B0k54zzeITyIftFKk-9o919ing8eRnD5NA1RFzImnLxXzHIm-CfWPfsyTwYN-s8Kv0CC_XM0XxQ7c7Fvx4GWRXYkluJGS_zZyTKw5AHUEAXrz9tYFUPbdfJcayGdHKlFa06i3pfrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شکوفه‌های سرخ، در باغ‌های شاهدیۀ یزد
🔹
این روزها گل‌انارهای از راه رسیده بهاری، باغ‌های شاهدیۀ یزد را به رنگ سرخ درآورده‌اند؛ جلوه‌ای چشم‌نواز که در کنار زیبایی طبیعت، نوید فصل برداشت انارهای ترش‌وشیرین کویر ایران را می‌دهد.
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438049" target="_blank">📅 06:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438048">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mqv6xY99yQ4Cw1Kl1DB4QeGzOsqK_hORNpvqQN6iiEdc9-lTCRm5X88_UHY5cqvoSprZzX89FwiNmotkGDtOyDIZiYdVv_0xUldpK1o-eVWbWJPW3DvkDEaX4pcnBL4AfNJemSK4Ih-LXvXcX151EaYo4rYds-f9Sh2gLbwFuD70wD0wJcCBolROXrhGwXDYMI6cgcr9dsyuQMYtMBF3HopTM5Z1jsxYmmyTOjqhW5qc7NfjrQ44JW-AG76Gdpx0Lc20QHL3jNkymF1dqaMvIm7-B_EOsvq7YIqFhZOBh8CLcvl4Fh9RpLOI5L-sYffsc0HIOh3er8e9xlB74z-9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات روزانه ۶ پرواز به اسرائیل برقرار می‌کند
🔹
شرکت‌های هواپیمایی امارات در حالی عملیات خود را در اسرائیل گسترش می‌دهند که دیگر شرکت‌های خارجی به‌دلیل ناامنی از این کشور فرار کرده‌اند.
🔹
روزنامۀ عبری «کالکالیست» نوشت، یک شرکت هواپیمایی امارات از افزایش تعداد پروازهای خود به اسرائیل، به ۴۲ پرواز در هفته خبر داده، که این تعداد معادل ۶ پرواز در روز می‌شود.
🔸
به عقیدۀ کارشناسان عربی،‌ اقدامات امارات فراتر از ملاحظات سودآوری رفته و نوعی حمایت از اسرائیل محسوب می‌شود
.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438048" target="_blank">📅 06:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438047">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تنگۀ هرمز مادۀ اولیه کود آمریکا را ۵ برابر گران کرد
🔹
فایننشال تایمز نوشت، شرکت‌های بزرگ کود جهان، مانند «موزاییک» آمریکا، تولید فسفات خود را در برزیل و آمریکا کاهش داده‌اند.
🔹
دلیل اصلی این تصمیم، اختلال در تأمین گوگرد به‌دلیل بحران تنگۀ هرمز است؛ همان گوگردی که برای تولید کودهای حیاتی ذرت، سویا، برنج و روغن نخل ضرورت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438047" target="_blank">📅 05:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438046">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دریافت شهریه هنگام ثبت‌نام مدارس، ممنوع
🔹
وزیر آموزش‌وپرورش: تمامی مدارس کشور موظف‌اند هنگام ثبت‌نام از دریافت هرگونه شهریه خودداری کنند. ثبت‌نام دانش‌آموزان نیز صرفاً بر اساس محدودۀ جغرافیایی انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/438046" target="_blank">📅 04:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438045">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cf096c343.mp4?token=dGuPAVvmqQxcn5W7B17UPChRa1Q4vJGPHdWaUtsla5XlUdP7BzAOZ9d-K2oDc82fUw7gpnW7SkAi9CbmoS3Jbl_aeD9NiAKOboZmLs358o28dM9GVqBSHYQUGR12UoqDaPbcgzC2aaLMTxH1i2K47VQxUCDa2z98zhayB9jcXnKLtgFD1KXempUPOskWWQWjlX_6lczNEa62Hve8vn-LA4L-aT4AIK1wnFJB1IcuY4mcdWINaB55DEN-0HH38d3ZX_mNBfjfPg8sWxfFbv7SjvncsQF_qG2SBCdvywAqWdqzAXDQk039hsFBjZxP84uCE4y92QraFkyX0ri8ylwKkQiqVCH3i2Y0XaSiVuwmw67FWErYeLrPYHdVVDBsVFce5RM1A5GSl-XqQ6bmLjhDMRv3gE2_AxGuSDuhLpOvLTMrTre1K5uJUBTj6JSprGHthyMiJ3t5ztrGIh8c0IeLRDJ0SEuk7d2SS05KbAhY50vioaXjLwsqn2m_bbMrU9vDOzLriKzo9BNbM6BDabeKPmnUxE7gKxKk3AGVlIfJPtXkFLUVrJb1tYQFYad54CaRjAqqIZW83u7BdXz8PzM-KOjtR8ad-_5r2qhHjVu5cOGbNnLdo_esT1Aado1R632O62x-B-sMMldtOb2fMZNvLBwLRz7BJ6HKglBHv5naIMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cf096c343.mp4?token=dGuPAVvmqQxcn5W7B17UPChRa1Q4vJGPHdWaUtsla5XlUdP7BzAOZ9d-K2oDc82fUw7gpnW7SkAi9CbmoS3Jbl_aeD9NiAKOboZmLs358o28dM9GVqBSHYQUGR12UoqDaPbcgzC2aaLMTxH1i2K47VQxUCDa2z98zhayB9jcXnKLtgFD1KXempUPOskWWQWjlX_6lczNEa62Hve8vn-LA4L-aT4AIK1wnFJB1IcuY4mcdWINaB55DEN-0HH38d3ZX_mNBfjfPg8sWxfFbv7SjvncsQF_qG2SBCdvywAqWdqzAXDQk039hsFBjZxP84uCE4y92QraFkyX0ri8ylwKkQiqVCH3i2Y0XaSiVuwmw67FWErYeLrPYHdVVDBsVFce5RM1A5GSl-XqQ6bmLjhDMRv3gE2_AxGuSDuhLpOvLTMrTre1K5uJUBTj6JSprGHthyMiJ3t5ztrGIh8c0IeLRDJ0SEuk7d2SS05KbAhY50vioaXjLwsqn2m_bbMrU9vDOzLriKzo9BNbM6BDabeKPmnUxE7gKxKk3AGVlIfJPtXkFLUVrJb1tYQFYad54CaRjAqqIZW83u7BdXz8PzM-KOjtR8ad-_5r2qhHjVu5cOGbNnLdo_esT1Aado1R632O62x-B-sMMldtOb2fMZNvLBwLRz7BJ6HKglBHv5naIMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت خلق شعر «خدای خامنه‌ای زنده است ای مردم» از زبان محمد رسولی، شاعر اثر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438045" target="_blank">📅 04:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438044">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شهرداری تهران: ۹۷ درصد از واحدهای آسیب‌دیده در جنگ تعمیر شدند
🔹
محمدخانی، سخنگوی شهرداری تهران: با همکاری مردم، گروه‌های جهادی و شهرداری تاکنون ۹۷ درصد از واحد‌هایی که نیاز به تعمیرات جزئی داشتند، تعمیر شده‌اند.
🔹
حداکثر تا ابتدای هفته آینده، تمامی این واحدها به طور کامل تعمیر می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/438044" target="_blank">📅 03:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438043">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e85815.mp4?token=lWDRaClnqFaohR5Ve_XGTbWl2rdeELxE9Z0B-mteV02Oi_aPM4nQVcWR8EWb_qZxrUN_dENr_SEiX-cspdCMETRw-y5lyGPoSlKjMlx3uJd49YJ2N-DBiEdIdf6yWFnej0ZrDZJIHZ7jEJOPCnJiyQRwQUHo5HnjGbBPUlWSgU8cpcxfFFeZabXl-1q8wZY68XL1Cuujc_yls_83Xsjo-72s110FuzLZjbjFtKvsiPn4sHr2O5oXPtguFrD-UmuVUufOJn05KINbk-_r6Opuocd94zZEyC_vXnN7wW-5uM3XAYsVwaPMYW3DDKsvZMFtHgk7GVk7-cW1qfBZjNonVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e85815.mp4?token=lWDRaClnqFaohR5Ve_XGTbWl2rdeELxE9Z0B-mteV02Oi_aPM4nQVcWR8EWb_qZxrUN_dENr_SEiX-cspdCMETRw-y5lyGPoSlKjMlx3uJd49YJ2N-DBiEdIdf6yWFnej0ZrDZJIHZ7jEJOPCnJiyQRwQUHo5HnjGbBPUlWSgU8cpcxfFFeZabXl-1q8wZY68XL1Cuujc_yls_83Xsjo-72s110FuzLZjbjFtKvsiPn4sHr2O5oXPtguFrD-UmuVUufOJn05KINbk-_r6Opuocd94zZEyC_vXnN7wW-5uM3XAYsVwaPMYW3DDKsvZMFtHgk7GVk7-cW1qfBZjNonVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری فوتبال برتر: طارمی برای دریافت ویزای آمریکا مشکلی ندارد
@Sportfars</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/438043" target="_blank">📅 03:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438042">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq9Oxg2M1aQR3-92gpKPHM0f5kJjjm_nyZQFMCxoFToVIKlnBdlBgzldYqDYac4iNjVVmhapZLszfqMOfvaLlOJIWf1cXyoQaJ_e4wlRj1dENjfZS6JQLTXB-SzEtEUEM-E0M7B1da8lngrdmsS-lbpFfoVq51w-l0wnum10fudyhF6rvDk6UKsIsXHNnu9juiwgbv-TTIbZZockXpvOXdLT4gFkjfCzlz6j-nePLeCgujsYdcI_NCptH-rFhqAKEu0_2tLu82BGFak-vgzeas6hOUi_eoKtlsaRLB7BydVnauV7_7f7Z8kOEY6dDc5-WlU0VDsaHkVUmfTr63V-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور وزیر برای برکناری پیمانکاران کم‌کار طرح‌های حمایتی مسکن
🔹
با دستور فرزانه صادق، وزیر راه و شهرسازی، مدیران کل استان‌ها مأمور شدند پس از بررسی و ارائۀ تحلیل از نحوۀ عملکرد پیمانکاران طرح‌های حمایتی مسکن، پیمانکاران کم‌کار را برکنار و سازندگان متعهد و توانمندتر را جایگزین کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/438042" target="_blank">📅 03:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438041">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2iDW04NegoVjAgpt1ZWwSmC3aTcWLYwSfxH6hjve1oH7O5OiHcSGyhFnXUCedM781P1ACDMNkqmOQNk0dfjGbspS_u0m6oMQJuL5omntMB-4dDCPulGdi7rBxYOK4PdfEbc0OfX9UvIRLK3GjVGdCBgYUiewsB33pXM2Hvp9MlBN-G0etaGoqmYuhMxGI38Xo6xV3QIiQaHJ_PEmLzXIuWCzYYg38WU-NhwtQLUHhimaIHZ2IPuT5cbyIkjwgxDsIa8GT7lGfDYcVdfM-_I6ylkrekW2tNaCoO5rAjWmSHnO3gh7QUmlm6gVwJF1oMwi6zySqD9xQSx5FaVvQLV8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذعان سنتکام به نقض آتش‌بس با ایران
🔹
سخنگوی فرماندهی مرکزی ارتش آمریکا بامداد سه‌شنبه به نقض آتش‌بس با ایران از طریق حمله به اهدافی در جنوب کشور اعتراف کرد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438041" target="_blank">📅 02:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438039">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce7282d4a1.mp4?token=dtEpPQ4sfUpA-bXOa8dxXuUmB8b35wDD6-JAtPwQayVtGadz61fJkIl6nWgdR_ec0ZP39XfsDK5j62F3L2h70raMG09Hdw7kY16EcrktMoRbeqQaJczIHjFE14QAI9NXGyYk3moOt14gaCPBGz4M_NsFb8hZP_QCBwU11Z6W8BIiS8eC_38rAgWZ_XtokHD6lvz-ENmXB58sjqkzot7XSBEDYsF4kTm9gWR0KWJGf689sE-j4cjCCllimTD4HiquqkZAara2u1VCOMiHYUUvskMXb1lIAMGdes03t5_2HzMZsu2ucVyY02lpWBb9UBDfK2H7ntjmrnFnRr10tCzzGW22_Xk_nH3sU5T1Hf5hyxW7oGzljg-GwbQbB-Ttl6MtMaAXIIG-NrymibvkHFh6N1gDu9REoZ6RAx-2AOo5uhR6soP9AhtQ5hi7JuaIDj8fj7lvcpbWjnY7Qqdwk-MwZ-DSaQDco2ZjXmLwen43qcNwA-2F-9aasvJBrre2MvcFx1wguJKt7F-5D2OtI5lUf6k35HBX2RpXN48WZfMGG2M7cE6gXxxhRotpP5gT4jcE5_UyApofrsgt0HJmp4qbbGv0ger4fP1Q3TrwjY_Yd7wnTQLUZjkEOlQ9yrbX3OnFhvixuyVbZqhMNchESJ09IUD0T2sUlJbjksg9KZdNcpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce7282d4a1.mp4?token=dtEpPQ4sfUpA-bXOa8dxXuUmB8b35wDD6-JAtPwQayVtGadz61fJkIl6nWgdR_ec0ZP39XfsDK5j62F3L2h70raMG09Hdw7kY16EcrktMoRbeqQaJczIHjFE14QAI9NXGyYk3moOt14gaCPBGz4M_NsFb8hZP_QCBwU11Z6W8BIiS8eC_38rAgWZ_XtokHD6lvz-ENmXB58sjqkzot7XSBEDYsF4kTm9gWR0KWJGf689sE-j4cjCCllimTD4HiquqkZAara2u1VCOMiHYUUvskMXb1lIAMGdes03t5_2HzMZsu2ucVyY02lpWBb9UBDfK2H7ntjmrnFnRr10tCzzGW22_Xk_nH3sU5T1Hf5hyxW7oGzljg-GwbQbB-Ttl6MtMaAXIIG-NrymibvkHFh6N1gDu9REoZ6RAx-2AOo5uhR6soP9AhtQ5hi7JuaIDj8fj7lvcpbWjnY7Qqdwk-MwZ-DSaQDco2ZjXmLwen43qcNwA-2F-9aasvJBrre2MvcFx1wguJKt7F-5D2OtI5lUf6k35HBX2RpXN48WZfMGG2M7cE6gXxxhRotpP5gT4jcE5_UyApofrsgt0HJmp4qbbGv0ger4fP1Q3TrwjY_Yd7wnTQLUZjkEOlQ9yrbX3OnFhvixuyVbZqhMNchESJ09IUD0T2sUlJbjksg9KZdNcpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صداوسیما از بندرعباس
🔹
وضعیت بندرعباس عادی، و استانداری در حال بررسی‌های تکمیلی است.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438039" target="_blank">📅 02:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438038">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎥
پیش‌مرگان کرد مسلمان باز هم به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/438038" target="_blank">📅 02:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438037">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc745442e.mp4?token=Na2Gxs-1ZzrQObL-Z3E-33sWi3fNNAQqbJ4w99SBsCtFA1yKIW0z9cxmysslkJHrkm-eauJGhYfzWQ2F0LTmbrxr7CMaJ-AI1G3IEbwGBFAWACCJUy25PWibFXr5phzZOZW4-zOf6xMqeohM92znL5U1iLDc6Ja0WCXfL21oSc5oXnYJlOKmWLsYl98Oq-zepC2SS4bW8cvrqjvXSoILN8_J2TVxk4GHx7DHstt7doVCWR946uGBnoYZuWyhHgHkW7Dontn3Iu02zt7NTz1GCBdXk21HLV0K5OeuJsDNu9wsS4m6exm8NK6s0qSGiFNEYd9l-AIojB09Lmiin7HllFMr-z83ane-QvxxTkm7ayFtYyB2q0Zfeb-H-BxeutbfD5LY3Fb3gzKMIB0Y_UwQvpDub6N7gmOmoZ5qkDiiWTjW9VB7HDFPfrzvTvh33luah0oHPOJkOcsnSj4EVh0vM9dLnabkXZK6pD2TL_MALx_C_Y2RtUOw8OwLM_jjzx5cAM8qkDtHvimi-ZgfMebbvXkzMSTARSb4cW-RDYrPdA45w-2VL2coX3C8k39_e-CpE-EO-WvKOtznRJL4p_yL4HvkUW5gO__-_wldxgFE5VzwGGucUPZG0cS1oL6evnNPB02NmmINxM2Mo2VEd52WP7RQDyRBGKXqR42YBqY0OS0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc745442e.mp4?token=Na2Gxs-1ZzrQObL-Z3E-33sWi3fNNAQqbJ4w99SBsCtFA1yKIW0z9cxmysslkJHrkm-eauJGhYfzWQ2F0LTmbrxr7CMaJ-AI1G3IEbwGBFAWACCJUy25PWibFXr5phzZOZW4-zOf6xMqeohM92znL5U1iLDc6Ja0WCXfL21oSc5oXnYJlOKmWLsYl98Oq-zepC2SS4bW8cvrqjvXSoILN8_J2TVxk4GHx7DHstt7doVCWR946uGBnoYZuWyhHgHkW7Dontn3Iu02zt7NTz1GCBdXk21HLV0K5OeuJsDNu9wsS4m6exm8NK6s0qSGiFNEYd9l-AIojB09Lmiin7HllFMr-z83ane-QvxxTkm7ayFtYyB2q0Zfeb-H-BxeutbfD5LY3Fb3gzKMIB0Y_UwQvpDub6N7gmOmoZ5qkDiiWTjW9VB7HDFPfrzvTvh33luah0oHPOJkOcsnSj4EVh0vM9dLnabkXZK6pD2TL_MALx_C_Y2RtUOw8OwLM_jjzx5cAM8qkDtHvimi-ZgfMebbvXkzMSTARSb4cW-RDYrPdA45w-2VL2coX3C8k39_e-CpE-EO-WvKOtznRJL4p_yL4HvkUW5gO__-_wldxgFE5VzwGGucUPZG0cS1oL6evnNPB02NmmINxM2Mo2VEd52WP7RQDyRBGKXqR42YBqY0OS0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهار دعا را اینطور غنیمت بشمارید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/438037" target="_blank">📅 02:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438036">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gp_VxKanSyDL4LySN0_Kf8BIjCgeYjhgTyBAJcZd0wOyBWkCOE8cE3Pdpmr5P0s9EJF1FY20_N5mTmDI3rHAqSiVD2d3ieyTsbWYyS77nnA66TfgfULm4hz-wA5dMU2q2f4MeVxd2Ii6tqSD_MLSLWUqzoQuoO9-RVZOQeVcRmv8M9Zp7_5GWbHC6DveULRu6SV1q8tTffBUKwm5kApLMwScDkvYI8j5_D1hKpTEzZ8QVmkhOm7WUAG21HBfUhRFbjZAnC7NGXTclmBT_62Twrn5_mMq-KuJZSFV87imeGDX4MZVFwMhPfnLzU5pOCqgnfu1vHFsEb9jTPUBZs3Iyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۷۵ هزار مادر روستایی دارای سه‌فرزند رایگان بیمه شدند
🔹
مدیرعامل صندوق بیمۀ کشاورزان، روستاییان و عشایر: تاکنون ۳۷۵ هزار بانوی روستایی دارای سه فرزند و بیشتر، بدون پرداخت حق بیمه و با حمایت کامل دولت تحت پوشش بیمه قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/438036" target="_blank">📅 01:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438035">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad4c72e30.mp4?token=MMFLmoJbVsW64TY0BkR56l9t0HrZHw6a8paDRnVAlA0zTmfaaEby6LE-C5ACw4wR5-jEClvI5Y28rAEhceENF2OToO0b2Ad1-p2RcoTmHcAyoI5JntyXb8c5ini6yaRB7y1pm1RH6XzS2xN2vaKWfou6JT3MW8jkfMrnHab-5XiyyUEqihV4jmS7HFah1MN7kS63JhlH9x-h7qFewyrT9IP3GG1eCg4ke0iVF9C5tvbKu2vG9dRvfqldF2h56opdH99rVXi47juSut06j3EWNnlG8N6Z91_P1RyNP4YmxZfeQ0eLJOyt29_9y5zDaAJojcOlKOZ3zDAWX4aqaIXHWElSBciB_35KIV_6xsHDNGgnBOlLIR1CKhqLhIq9zFe__pNEXmVkhYhnTafGvQn7Qv-5jcXcOkx7S8zwEjjQmFzz-_h2MpCXky02AIoY8hmxilGn7irOFVE2hOZCyYZO6UPqhYG8n3tbVL99Grq1r49oyrx11v56p0tmn4HUbjx75vo_TxRU9VuN45QCjx9YLfDgR1Eu37c3im1GVYDL_q8ok6j5pjee5JI1dbKSk3HowCQ_17KUus_6yY50ZnbwErxLfVf3rDcRwUwzzb8iDc6QJG8ghobYkHxKvtWw0udCQsjW4FJVxiMXJKodjbRgdHOxyrAgE2RQTN0o7CeopSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad4c72e30.mp4?token=MMFLmoJbVsW64TY0BkR56l9t0HrZHw6a8paDRnVAlA0zTmfaaEby6LE-C5ACw4wR5-jEClvI5Y28rAEhceENF2OToO0b2Ad1-p2RcoTmHcAyoI5JntyXb8c5ini6yaRB7y1pm1RH6XzS2xN2vaKWfou6JT3MW8jkfMrnHab-5XiyyUEqihV4jmS7HFah1MN7kS63JhlH9x-h7qFewyrT9IP3GG1eCg4ke0iVF9C5tvbKu2vG9dRvfqldF2h56opdH99rVXi47juSut06j3EWNnlG8N6Z91_P1RyNP4YmxZfeQ0eLJOyt29_9y5zDaAJojcOlKOZ3zDAWX4aqaIXHWElSBciB_35KIV_6xsHDNGgnBOlLIR1CKhqLhIq9zFe__pNEXmVkhYhnTafGvQn7Qv-5jcXcOkx7S8zwEjjQmFzz-_h2MpCXky02AIoY8hmxilGn7irOFVE2hOZCyYZO6UPqhYG8n3tbVL99Grq1r49oyrx11v56p0tmn4HUbjx75vo_TxRU9VuN45QCjx9YLfDgR1Eu37c3im1GVYDL_q8ok6j5pjee5JI1dbKSk3HowCQ_17KUus_6yY50ZnbwErxLfVf3rDcRwUwzzb8iDc6QJG8ghobYkHxKvtWw0udCQsjW4FJVxiMXJKodjbRgdHOxyrAgE2RQTN0o7CeopSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرهٔ تصویربردار بیت رهبری از سفر رهبر شهید انقلاب به مشهد با پرواز عمومی
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/438035" target="_blank">📅 01:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438034">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حملات رژیم‌صهیونیستی به جنوب لبنان
🔹
منابع محلی از حملات هوایی و توپخانه‌ای متعدد ارتش رژیم‌صهیونیستی به مناطق مختلفی در جنوب لبنان خبر دادند.
🔸
همزمان حزب‌الله اعلام کرد که در دو حملۀ جداگانه، تجمع خودروهای اشغالگر و سربازان را در سایت المطله هدف قرار داده است.
🔸
هم‌چنین مقاومت اسلامی لبنان در بیانیۀ دیگری، از حملۀ پهپادی به یک تأسیسات توپخانه‌ای متعلق به ارتش اسرائیل، در شهر عدیسه در جنوب لبنان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/438034" target="_blank">📅 01:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438033">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ9SgXoC21kNNG4mZY51thdSCeqsIiU6_HPQ3RyjexnqtXI8AEMxT9w2hXUNWCfMTWewJnQgvAc-xYl8vnW0OWYGz-B4cPkBwrqjoWClOFv8y6MYSD6Rf9aM0XEY2es1Q0m8wp3KZHqyEan7qGcZbOmfZHZaynH1rJtEfTCwFlRe9uHHJ5_RijjgcGGuZi8-dogNF_Z969JfcvdBISppelI72PRLxJt1VE6y6e-jxrYb--1weY-uxBGk0Bj-VN8rIu6STY-gIXw2KrmZtUE5G6k86g160TkGi4LxonyXxDjAXgxT4T2J8vzpozpokoqThIV8IOMQJ7PdXiajOooS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان و موش‌های آهن‌خوار
🔹
بازرگانی پیش از سفر، صد من آهن به دوستش امانت سپرد. پس از بازگشت، دوستِ خیانت‌کار ادعا کرد که موش‌ها همه آهن‌ها را خورده‌اند!
🔹
بازرگان بحثی نکرد، اما پسر کوچک آن مرد را دزدید و پنهان کرد.
🔹
روز بعد، مردِ مال‌دوست سراسیمه آمد و گفت پسرش گم شده است. بازرگان گفت: «خودم دیدم که یک شاهین کوچک پسرت را ربود و به آسمان برد!»
🔹
مرد خشمگین شد و فریاد زد: «دروغ مگو! چطور شاهینی به آن کوچکی می‌تواند فرزندی به این وزنی را ببرد؟»
🔹
بازرگان پاسخ داد: «در شهری که موش‌هایش بتوانند صد من آهن را بخورند، شاهینش هم می‌تواند فرزندی را برباید!»
🔹
مرد به اشتباه خود پی برد، آهن را پس داد و فرزندش را گرفت.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/438033" target="_blank">📅 01:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438032">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KH03b8PcuuDUKcE_ktwToKdfYnq-ndoZksTDzlgAE0EulqnZ-B6y-Rj9AuVu3w1vHMdKqcD5taB8pkCjngduGMBnUafrWz2c--bAImGzReiwlkASU2MUJPyDyphMPgHrdytppKblBmFoc6lUVYscbNTdxgey-jxE6N3Ay-5dA5yRtbVVmv6Sj_DNoDEJvdgOdJZ86Uk8k88wGrgPjLJ60vDPVdOnhfiOwcYvgLsiA8DDr8eCuHf9hyrJ90njnBfrQZjl2hWGMcrqGjZ4f4YXAFLVwuFv9BRsEv_8bYkl9Z17KpFMJ7STVKwl2JGI5b22TqOkNJoeE3JGeS2NkTzJug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بار دیگر زیاده‌خواهی آمریکا دربارهٔ اورانیوم غنی‌شده را تکرار کرد
🔹
رئیس‌جمهور آمریکا: ایران یا باید اورانیوم غنی‌شدهٔ خود را تحویل دهد یا آن را با حضور ناظران، نابود کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/438032" target="_blank">📅 01:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438031">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c05b1e3c4.mp4?token=B10Wnbd-Al0X8M7vgpGca527QBHACkdkA1M2qRUNABB2A0YSwbi8KpzRX-WREuFlJlDc6hJ28WM0LUErFDCSL_0c4dla2g2AU3xbH4_Eof_GSBqDTzgjziL1fVRgljp39quHgT1jsb6vReiKiHA_0FwsHRy7VkXv4Ti7T_85J9_erHdCCdCxO-_ZGvbsNjkOmopa9Kp04uBvgN6Fy0flhk5XqUykDhWU6E2Zqu8dx8YjSN0zIwgwxEAvLOcyZutHY63Ui62JORjzq3Z-jKB-FktB_aw0DJTgbTDN3vNyglCM0fUMjqMiluUkMeIGamxafy9ZBjWiHWkf6PAbADz5gYP27kdt5lkcZh5h53ppC5gioPEmWVo4SccuM93w9ZrN5j0af0h-zuOuA5S1zzfOE0P1i1cOhLxJS08pRj4ZtrojIbhLIljdCge3l-5tgivRzlNueucllp4sYqWpnSrLKUCSzKe2ytnWjI3_puLLoKJ1u7CBCE87DA09yni9x-i-w_lMC4E56Nnom7BRp4qWZxCzEukJqwIqWp7kCiJkadl09yN7mFpfLsFaWIjvVmfQw7K6aSVivSXDt-LCTmV-kj2csjlZ2-699m14M9Cn7gZMpXssewOoDfhqcShmmISIphkq3AiG0C2ENyyNs-ahULM7Is3dY8SIizjm3e_a8Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c05b1e3c4.mp4?token=B10Wnbd-Al0X8M7vgpGca527QBHACkdkA1M2qRUNABB2A0YSwbi8KpzRX-WREuFlJlDc6hJ28WM0LUErFDCSL_0c4dla2g2AU3xbH4_Eof_GSBqDTzgjziL1fVRgljp39quHgT1jsb6vReiKiHA_0FwsHRy7VkXv4Ti7T_85J9_erHdCCdCxO-_ZGvbsNjkOmopa9Kp04uBvgN6Fy0flhk5XqUykDhWU6E2Zqu8dx8YjSN0zIwgwxEAvLOcyZutHY63Ui62JORjzq3Z-jKB-FktB_aw0DJTgbTDN3vNyglCM0fUMjqMiluUkMeIGamxafy9ZBjWiHWkf6PAbADz5gYP27kdt5lkcZh5h53ppC5gioPEmWVo4SccuM93w9ZrN5j0af0h-zuOuA5S1zzfOE0P1i1cOhLxJS08pRj4ZtrojIbhLIljdCge3l-5tgivRzlNueucllp4sYqWpnSrLKUCSzKe2ytnWjI3_puLLoKJ1u7CBCE87DA09yni9x-i-w_lMC4E56Nnom7BRp4qWZxCzEukJqwIqWp7kCiJkadl09yN7mFpfLsFaWIjvVmfQw7K6aSVivSXDt-LCTmV-kj2csjlZ2-699m14M9Cn7gZMpXssewOoDfhqcShmmISIphkq3AiG0C2ENyyNs-ahULM7Is3dY8SIizjm3e_a8Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌خوانی مردم تهران در میدان انقلاب
🔸
حالا که با نائبت، عهدِ دوباره بستیم
🔸
ای پسر فاطمه، منتظر تو هستیم
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/438031" target="_blank">📅 01:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438025">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6wlI94JB6xGJunVA2WE7eWuDvWN02PkiW0s3JGTHJ4tC-6A654TPDPHHH4BwqGiahmAlHXaLsMLPP_5nisFlRXG6vMfBYQm62zC_3BW_wo3PS7YGSilPXHZRNo4q5hXB0TyO3J9488D9aYFlLIgO_48He23NCwQ5pctoFgBL3q35X8891qcmjdA1P_75ZhWOWXXc_2A3NTbS3qt4-0Gn2mnmmsqJFs8UQGN1iQJX97AgSQ6IVbfR2Lj7YPxj1XdTQyPNYGP0Tw9Hb6XPACXQ8UwxYt3s-ODrC-3-nGSKf7jwbb1vI8kQz3JMxZvizPjyKvIzXoJPb3JNFvEboBIsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkBDT0kJIs90y4jQ1I5nI4mMKp9-4caHbCeIgz0ZOAj80mWuaQo3m6oj0J-qTwA8IgbmkxZ8DL-u9co1iBXtaH-fM8j60zQ8tI4YQ-lCIRlhuI3A4cacQdlugk6EDYFY74pe-xP1GRR1cuyjmBbfeIR_P0ksHsoYBFMhxGTxu29O4w-RtyMQxL1EJm43xYf2ccVKtDXZpPG9ssoJ8se806m_KnCJ-I67gkT65R2-z64rRVKJZ8o-A70oS2WwdX3oF1iJpiXo4oRLv3wCnnUWdIEpuC4zck0If1nXkavd4DgNpA-7Ddl2lLeWjaHVqcrbqxJhr8lniS79Vx6YWCxGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWl4ql5mG6YqhxY_JVtzh2ApeLtdXij6sEDQlkvNZaIVn5N_x-7OiU85qMG2Wb09HN9CiIQ7M39IlQPA7TZRANdMx2p4cGH1d9U7pngcFZ-3AeOOVG9K3HXFI0QHryUsh6pXNA99V60t53OHufVzYuYGusPALl0mb01hCPdtcaglXvrXb_nwBpGH1EUempAxndEWoW_Qu8tiCB4xFEngNeEWBGRn7ntgg2mSGtm7dgW-5qfaKjP6zDRp9VdSbA79AT-_t3Vh23X-TSVY6ONQhBmSj7PguyLReI9SEXhKvQs_5vKahP6VTz3CSdiDJ1kntYYVICw3yUp8Q9DscAkpBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c4sBIHz9oyizjV8ngHJyRjiB33MVbMMRearybf-A1bE736CcQuZFmIpY7FllmoSzVvDGFA2eZ4XO-TUd8DeJqPxsULYcwaGBcK0IkCeHw7v-RpLN5gCJq-4k3ju47LvduoskNRk70uwRDrYrSHlsZXJgcwLHMj9iJ02EKRzvDgIszs2cUdMz9_maeDtWv2lzwYeyMbds9Ek09Ny7maDSRquAKaOnt9PUkm90btYq1rey0hV9HdI-WPjCFSrZrtdXj1bjqIW1s9FSSUksp2ezWbxZbunkY5ILhO2KFCo1ZsBcgavq1aIHe86o4HQuGWa_JZo6rvNuh3ymlCd9T598Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DktompG3F5PFDgRTyIWqQjQTL0AIeatg59VCJTjIQsLcebksTsviClrWyELV_saPWgR4RjP9metTTLioM33qlHg74QxYHGzu730bACZa0B4cYctAOaaZUYz_s_nbbKJqNPhcCGXrtlMBaSeK8aCV9u2wuZpz6YYuD5QISNdWl0Ue-C-vjoCiVvIJljMoO2eVbcgELY1N8OriLiGZZD3SL5X53hOJZvpdhjRjAxdb1fnDk_8w_IwSc0_K_Xl7F6tAxNobtWESoABLouPjerXBWekFlV3b97umDLupIBhvFHtIR4_PuH36JVMccRs44zElDEbpIU-e15CejWlxs7ez1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TI6WiYpNTG6H6Gr7gtqRtOr7MIj6GURYaQNfGAjznLDAnGQcfw91XIW4dxY59y1UxpvymoLcwO0LN-Cb3Unz4dCTZnbExwfpri2M9qjqv-AHNH0_eNQbRClCWKtc2nAt9M7Et-iX9z2MwVeuSokZOOteCZLslBIHyLpnNf8AQXS2bCTgCFtCrynQy5Ccp0VCg5XPplKhrRrR8PbqspirPQNU0D9nxjvEUoIhn27213FG8osnM0PSe1BKrB_rv9xXtVQV6Jb87BM4Ahp2n-UAt4v_t1mv0acXObySyOiqL-0HCBSYETNnGUGUMzuqS3raYgovV7q80e2j02ebJ_LjeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۵ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/438025" target="_blank">📅 01:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438015">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxVSKLYivwtOtjFqkSz59Asz15o2Siv_V9Je8huFnooBoQ87clW3nBaCUA4zQTA3S8cOGVcQksKfM86kN8dmwldDZGOTdHN-hs270PxRibSK6YcdeyZ0BpIemPjwUIwXiKZSqMB3BvLBAiR7FBR_q57_oKz4HRRw9VexrgMuB_mKg8A543qcn9-rZx-X3m0RLm6gXDAhY-6CaHHtmk73G30TOzrKVwgUoAgAlLBJe_z-V9HfS1QCD6lA6xeeKdcLamDAH5YonqsW5A_jfHn4Tn7sfxJrYGF499G60Sf46q552iPWldoDTaaPO_UlVEh2ct-T8eQ9GI_eXUZsHjjW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffKsjkfT-Yf5p1PzodmI6BJUeePJZm1lCwdm-bZK8pMV0kb9TeE1JUipMolFvml_2HnWQOohq9j1RoeobEspMYT5npLVVylKJxumYBXyZ3RPTRdUquqH-smtiBLQWb9uWRD80rmJq2fIV6xqzG03zargTMlsuICed4opvQ8b4Wih3S3-rKDIibdrdspg1yeQ65JrkvdEfAOwZMsQvCrS9ul3E2XfnAfrsx6WZuXHIgkielLWjFaHqY5Ubgt3_DoCnNZrIC07922kcAHXyYJg_PtpMMuOECtmdtkI8eiNhLwp5pmQTPZJI1_q7nFDMJUec5S_NJaf8_Cua3qm9XOTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0qIRYoj6LrqKgPF8GNCdQb8pJ-SXCR3t2LiY7szfdJsNqdSiZqRztlr2d0G1qmHbmoc1vg4q_uRnhocXvoOBW16gx-MEpTBOgEMloYg2RTyIHaQa7lPOlOYCEKxJHKskkZwlswNCnKcrcB8TqUnM9mJslWimLQb-pBFoFFceZOpUnnSBQxzGJ1orltVDyDd3H0CI5SEiaujB9YomcbDExjKEB0AV60gzXjI1GmoMw0O5EwOjNFoinV6awATKBToFN_CZyx5bwqukDzXVvUEQ-5hLq-exVFiHFhI3BT27UNwp95gb-lEIaoEntWXvJe0D0qRgfVSnYH22ovdxa-FuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mUO2_9DjJf88OecCxOjILmbcWb2eDXeUoM7fmS_xGA5nfCL-a98cjIQdsRaWZj2eO6YZQhaujjsnHasYGqlIMxWRHwzqnSKLL04e17YCP0EozWKwHYBdjiIlB0y0y7YM01Ha7GdgGbfxijz39gULgGGUIN1ogQbM9_Nikh9P-IBpuOK-5YYQ1xydF3nq4E6uO5jDwagicE76cAN-fCT__y10wCY2qI_aZRPOJToigifFHk0qkXZkHAsyXumNxQi0LDjCnKa9_Lzz0pG2i1kedzg8hiHTc-gCEHCcviJiYKZUMWxRop3XaRBmFdtp5B58NWn7RpkFjtWEbp14RGUlPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEhmv1SVTfojT20Wo5Jf3E2o4ZRqM5eQ3HNbdyVWYChhwirBr1_dQh7_SMRp0y0NYa44GBpOSgcQUCt_Ws8pQ0uVzJWX4ZqdFBGBg2_oZkWj0xvcwnIYdkvYRhMA3QIK6t20I5J1GN5MA6MsiJFaN5u9WYzvsIKZCAPvfxOv3vqGP0EzF7jafGaAzLFvZIrhTaA1IMM7FZRbFsYaKDdvBrpurkckQoA-4Bqg6lwyGrlLcXCTwaIcV3rrPt9rVbTOzNC2dequHBNZGDUyC-8frBCPeSZ3lcHDP0koWjToLBeJA8w83zUVN86cdeiTbvzlQbBEFMRBpwPEnpKCpgLB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_fL4SjZzuB6Noft-mllF9oPAKCz3WIrNAiqTYueFlh8XUYBp0wFm0DFwDN542QLwKF5HSPXCME_CcN5UtgFw5DvoblHFtAAWt-X1yu0mnZMmNAVJ9mq_KXhHCZ7qA9QwEIUhOc5QBuSjcVyY6KUOov8wgXFq50KsalS9iLjywZZMgFlAG8odD8Sl2OvG_NKxGDda2zZFJRxuBZrrm0maJKoy2qxlplHODBWg9KL6gRxcEF_7F-0HGdSXCVbz4O_zSHu37dncefgMxiTXfnKu2AfEispkbQSlCTQbZnQ4YiXnhEXoMEu9ME9WBfpDElZjTkGEnyHqY4vJQC7UZhMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kiF7XBVT6nkXtomCAl24PRXGc-sSgCrZX53aKQcO1JCWUFlg1QrCpUFB12g3JtathLnqOXkU6h2KgP6B2nNnW5gZrtUgKGtXeYUaQpmAAbnMzx634fn72tfTA2QosKQidqr8lTXAYcfVDj-93KIIwf49WzyNGukg3Pbct_pplrlY9gnTIpm0_dNr2Zzp0yloY4W8FhMs1vHAAhXfv9DHzMifC4Us2Taj4zRW4rUeOaTt9cmv3nuIwJi6ef1Io2phxFAeNd6Sj69sw_sFjKR34jENWGJCAH_QIpdBjaaafbwDIDi3gkerdRJs5dlQucw83oh_V-sSrlGwC-zXYRfjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M643M7IL8YzFcKFQLNLzxQHzRzNVj79Y17cWhnJk-WLlWWzkHSFuIaL5Hr60Kv4aVWIE6ntEAJLWDpHUwJ33LAI_o759The5mn2kE4Mx_hgo9bMDrFFk9tUGuh2Azaap_fuYVhStMTjFQ3W9oRZF3-5znJ7IeBKQ-EcNKRt6YRG_FdNA1tTlwDsWl7GtU2vD32oeM80KSHzYS_WpwcOz2hH__WqQttq269cxV-G0059lPJKxwAUF_0aUE55elGFFx8_Tii6MTXCl4f2DJwJJqbgjRCXYimjuMPBnuYcQ49PyYmAOXiWSinNB6NJFZLQR_U-ft09IRRaPp8C-vOOOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rH2H56Ko3zp6LPu9tLEaJnUQvPO8haNszWFysj-BYUL-pVTkbozhZRugdgGlo8N8I72NeQXgdu_dTY52UVIkIKnHhgcuOt29qelgBUFmJQxqxkM8aqMJp0FPLfMipQ2WJdA7cxVZ4FFJR5x69-3w1uaclL6M4k0251U2kzsf83e2SHtTJqPYq6XfoTSb7KA_MFnazcql1ZTdayAEC1fVs2KFbNoUNA2wR0xzPH4eHWvx7yhOafH6VqZAgIKSGaDRRUY4F2YlWCfCrdZcvl6PGHe0ns2kZ5kZkj9wlcJb1sXCRbIES97WevXo2nBX8cF7HGJqxSKuYSv268Ko7hHBzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2vX3FbRz8XBhn1VhNy1Ar5fY5foQJdPUNvI61T93JLbgSRkD28XMYEY8voRiUegT2D_sroTfTkCh-ZgP7TDbK-IEb7okIml0l0kn6mp99ESXsM4CzqBobybaXXYZMVGTzJt1NPCMFHM2uENZJew2rybvBywGmDBBAGJ0C_vv2wj08DgIO7wLHavmfEpqkf3JJm5EWdfxg9g3PddBNQWeA9U5mfCc1zah4MYtWWIqhYR3gfK_PFC9V0YJY0o_ysFr8y-WH5fs1WX5JP02s8k8mDj0YNnYR2Mhss1aILlmMbp3TDHTLKhuif2mMh9EkRqA2-H_TPH6Gy-tye_BbLJpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/438015" target="_blank">📅 01:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438014">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f525GQo0BaemrbQ0GTGRG9P2avnOMTIT0LIpsADrfI_EFNvb1veJ-wBQGdra1b7IOuu70Rg8HnGjBp3_tb_BD1mBHepbu_Ia6FkZmmkbVewyXc3pVECBieu-RNSam6klwpX4C1jAN2qV12kvQmUtGU8RYr1bhSySMxPUOxAPTj0lt1Srinj1A8HNiMH2y0bl4mezP--3kYjyVQ6maTRFslWf9-EJCsQTdCXo3cLpO0gCeop2tTESaaXmv0AlfWTZFwEZqjgd5MxFveoYTD5cxMAJ3QVkC0TxZ6OJqDp6LKy2jZUeBOXRgPDspkSKjzNof3eVX1Tk-QTERVUMl4tuBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چراغ سبز ترامپ به اسرائیل برای ادامهٔ توحش در لبنان
🔹
در حالی‌که نقض آتش‌بس توسط اسرائيل به یک روال مکرر و هر روزه تبدیل شده پایگاه آکسیوس گزارش داده دونالد ترامپ به اسرائیل برای تشدید حملات در لبنان چراغ‌سبز نشان داده است.
🔹
یک مقام آمریکایی به آکسیوس گفت:…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/438014" target="_blank">📅 01:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438013">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqYN_gwMN1tPVh3j1XvPPTW5Zfh5UWqS1osNYZkq-zlLjC90Db0qtzj2DJTbiVXlB4CTXb8CkhpvHvvQVUekhKbaLbkxQSLktMgWHGwLNAdfSDfaUhv_qX1UuslfnSYzsg7DlbE1OWit0Yr3CIPd9GG67ETKAr6cMey480UcFgmpWbxdzfeAZnoKDXlmND-xPDgoZzxn2ZarCKPKlzUs_mRq5-2D6KTrC9Yn7bPvvevY57QgtjHe7RC15CmPxitteSfsaPryp2Uf4vTBvCaC13nc9hfxiqLGJIJlIso24SEvYPswi9jDZfDdjklai8qNwK-aK5T78ZOiitpJQGSWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاریخ احتمالی آغاز امتحانات نهایی مشخص شد؛ ۲۱ تیر
🔹
رئیس مرکز ارزشیابی آموزش‌و‌پرورش: امتحانات دانش‌آموزان پایه‌های یازدهم و دوازدهم از ۲۱ تیر به‌صورت حضوری برگزار می‌شود.
🔹
برگزاری آزمون‌ها منوط به دریافت مجوز از شورای تأمین استان‌هاست.
🔹
درصورتی‌که شرایط کشور به حالت عادی بازنگردد، تصمیمات جایگزین از جمله برگزاری امتحانات داخلی نیز بررسی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/438013" target="_blank">📅 00:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438011">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5255500874.mp4?token=UeM3g8tj5kYeW9v0nReO68mRq4nW_iGTga-EGqHpeJBQVEcOr11eevl24vL8XAvIhikr8pjxeBo1Otu7RzIbOxEzrLqvwbkpVKhPVjbp4OK1oLeliVffiwdINHceJQK5c52E7iTrQe8RlsLj2Tm2WCoVVrqBJXNL8XN4lFSWY6Sv44v-RNZXoPhNYBWZ4-4TocPKQvd9LiI1WWt5t-7s3-riD_AUrghzfgh0S0qMHt4XrPqviux0Xi_BbHdK_n5T3ulItgbVOqMQQr04FhhQb-x_LcwFQLc1_Lfrafvwwcq4V4FW5s1PfEyPDSlIPNdBWR84lrcSKkpXZ5xKDRNisw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5255500874.mp4?token=UeM3g8tj5kYeW9v0nReO68mRq4nW_iGTga-EGqHpeJBQVEcOr11eevl24vL8XAvIhikr8pjxeBo1Otu7RzIbOxEzrLqvwbkpVKhPVjbp4OK1oLeliVffiwdINHceJQK5c52E7iTrQe8RlsLj2Tm2WCoVVrqBJXNL8XN4lFSWY6Sv44v-RNZXoPhNYBWZ4-4TocPKQvd9LiI1WWt5t-7s3-riD_AUrghzfgh0S0qMHt4XrPqviux0Xi_BbHdK_n5T3ulItgbVOqMQQr04FhhQb-x_LcwFQLc1_Lfrafvwwcq4V4FW5s1PfEyPDSlIPNdBWR84lrcSKkpXZ5xKDRNisw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقر گروه‌های ضدایرانی در شمال عراق بازهم هدف گرفته شد
🔹
رسانه‌های عراقی اعلام کردند مقرهای گروهک‌های کُرد ضدایرانی در اربیل عراق هدف حملات پهپادی و موشکی قرار گرفته است.
🔹
به گفتۀ این رسانه‌ها، اردوگاه دارشکران در اربیل هدف حمله بوده، که طی این حملات دو تروریست کشته و هشت نفر دیگر زخمی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/438011" target="_blank">📅 00:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438010">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e3bcfd35.mp4?token=pVMI4IuVjBfVii01P013Om_92VDXigni6Htnyx8dpVxQEFxFoIaoBRsT4ZTVs3hyPqZGUga3P-rP4eFnA-IGaI4yAhw4DrgGnvO_aWMyhmy8jJmQoPsKwRIgO45H2mqNo9XvQhSSyuQx1f2gw4YYsLPbViRrSDSx8wPEcQ7hStl4mUSjJQU34cQ1M8CZJKXreTEaZtUxZ9BUz1WIPSZsPG3KSSWUOjCxrHICAB-4tkJfnSleSzEX7vwNSNU2ewbhQvrDvGElt5LYjJ5utNE8ZfD3tWn5PvU896xUxqg4S0i5LTGbzKJjAmmySrLlvbIq3NWPJo4boyacW9k0RLN1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e3bcfd35.mp4?token=pVMI4IuVjBfVii01P013Om_92VDXigni6Htnyx8dpVxQEFxFoIaoBRsT4ZTVs3hyPqZGUga3P-rP4eFnA-IGaI4yAhw4DrgGnvO_aWMyhmy8jJmQoPsKwRIgO45H2mqNo9XvQhSSyuQx1f2gw4YYsLPbViRrSDSx8wPEcQ7hStl4mUSjJQU34cQ1M8CZJKXreTEaZtUxZ9BUz1WIPSZsPG3KSSWUOjCxrHICAB-4tkJfnSleSzEX7vwNSNU2ewbhQvrDvGElt5LYjJ5utNE8ZfD3tWn5PvU896xUxqg4S0i5LTGbzKJjAmmySrLlvbIq3NWPJo4boyacW9k0RLN1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رهبر شهید انقلاب: آقا گفتند مهریهٔ دخترم همان ۱۴ سکه است که برای دیگران سفارش میکنم  @Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/438010" target="_blank">📅 00:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438009">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
دقایقی پیش مردم در بندرعباس صدای چند انفجار شنیدند
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست.
🔹
همزمان در خلیج فارس حوالی سیریک و جاسک نیز صداهای مشابه شنیده شده است.
🔸
سحرگاه امروز یک فروند پهپاد متخاصم در محدوده خلیج فارس توسط نیروهای مسلح ایران منهدم شد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farsna/438009" target="_blank">📅 23:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438008">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌
🔴
یک منبع در وزارت ارتباطات: مصوبهٔ بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴، دقایقی پیش از سوی رئیس‌جمهور به وزارت ارتباطات ابلاغ شد.  @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/438008" target="_blank">📅 23:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438007">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad9a3ece8.mp4?token=MzTbejLcRo90fpHP8RXNtsxOe0I2oO2HbmNDRs6QM4zTbkHCF7O9BWWV66dtgXv56egq5pHXu2TFpXLi4RSqBLGZT0Omdq3lf6ZJnYC01_drCnU2E6BLwwcVYWLWX5OsD33xCmlvfk4W8lu72xeFQ49YJkmDQNVGVFGqxkgO09Je4HWj848H3n38BvVZPN_qJKeqxtszl7g__vVL6vpRyjwt0JDn7sOXoVK2g6UR0z9yOrqxgrgw37Wb7PCqogcLI_4gmgQA-oG_-cu-j6fIIqXcg5cEPwmIgnDmi747OwnQg1F8lETKyf5OuSCjaYOVsXP0Vy7hRnq2m785plWB1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad9a3ece8.mp4?token=MzTbejLcRo90fpHP8RXNtsxOe0I2oO2HbmNDRs6QM4zTbkHCF7O9BWWV66dtgXv56egq5pHXu2TFpXLi4RSqBLGZT0Omdq3lf6ZJnYC01_drCnU2E6BLwwcVYWLWX5OsD33xCmlvfk4W8lu72xeFQ49YJkmDQNVGVFGqxkgO09Je4HWj848H3n38BvVZPN_qJKeqxtszl7g__vVL6vpRyjwt0JDn7sOXoVK2g6UR0z9yOrqxgrgw37Wb7PCqogcLI_4gmgQA-oG_-cu-j6fIIqXcg5cEPwmIgnDmi747OwnQg1F8lETKyf5OuSCjaYOVsXP0Vy7hRnq2m785plWB1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رهبر شهید انقلاب: تمام وسایل زندگی شخصی آقا به اندازه یک بار وانت بیشتر نمی‌شد.  @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438007" target="_blank">📅 23:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438006">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea7803896f.mp4?token=VNfkNZw1QhKJm6dOwxbh0eB7ygPaAbJHlrtDrTjiY6IjfyDYDbwnxVMo6MTx4dcgcjfEqfcfpi070_9QT9diuJPfWM72LLxkXBNiYT7q8ozPy4iQ2bt315hJ4AYEgBczyTD1sClrPSKQAc1PLttJt8jpTgsCcmRXGpg1WddF_YysDXoP84YhIaY5xps6Qg-j2wbWJ-DtO7ueHuw1ZTceUStOFDaZc7xHfIoudzfCb40ebk1plYD4gnvOsC1u29_xiBGbU7sgOObZ88Q3H15hrjrw40Chvbunq8LBul_ATj-6ZxffaF0fZ0msaqUyLOn-VCy3mcGrOH2muaPf6kSS2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea7803896f.mp4?token=VNfkNZw1QhKJm6dOwxbh0eB7ygPaAbJHlrtDrTjiY6IjfyDYDbwnxVMo6MTx4dcgcjfEqfcfpi070_9QT9diuJPfWM72LLxkXBNiYT7q8ozPy4iQ2bt315hJ4AYEgBczyTD1sClrPSKQAc1PLttJt8jpTgsCcmRXGpg1WddF_YysDXoP84YhIaY5xps6Qg-j2wbWJ-DtO7ueHuw1ZTceUStOFDaZc7xHfIoudzfCb40ebk1plYD4gnvOsC1u29_xiBGbU7sgOObZ88Q3H15hrjrw40Chvbunq8LBul_ATj-6ZxffaF0fZ0msaqUyLOn-VCy3mcGrOH2muaPf6kSS2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رهبر شهید انقلاب: تمام وسایل زندگی شخصی آقا به اندازه یک بار وانت بیشتر نمی‌شد.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438006" target="_blank">📅 23:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438005">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacf521b07.mp4?token=uDvQQz_NdMriTl-qfFBLqttJCWEGaWQZd_JwCj6vBC4ohmJeb8AH67Py16RW_QmY1c1NprAJnu2EDbo7VhgDv8OpjH-geKu0fPoWtIBMnAkQLyI7sJImh3Z1E46DDsjdfBS3v9LGcPUJ6hA5tAe1Oeqx0zK2vSvZ3Lp-hubJUtMNHdwnxipdOXDsINKkdSAb5vFZVrC-OddCQjfSuZRJkkspYTm6nJA_xOrPyWS4DTaCH2a3eqJnqw0MmuCD_R04SRq4OMyLUyMVTZkNA5rIqcYKWvBxqjqs_PYczRe_ozg6Y5FyfuUDqXsZtbIytdRp0TkhGE_QDyNmJgm-UaebuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacf521b07.mp4?token=uDvQQz_NdMriTl-qfFBLqttJCWEGaWQZd_JwCj6vBC4ohmJeb8AH67Py16RW_QmY1c1NprAJnu2EDbo7VhgDv8OpjH-geKu0fPoWtIBMnAkQLyI7sJImh3Z1E46DDsjdfBS3v9LGcPUJ6hA5tAe1Oeqx0zK2vSvZ3Lp-hubJUtMNHdwnxipdOXDsINKkdSAb5vFZVrC-OddCQjfSuZRJkkspYTm6nJA_xOrPyWS4DTaCH2a3eqJnqw0MmuCD_R04SRq4OMyLUyMVTZkNA5rIqcYKWvBxqjqs_PYczRe_ozg6Y5FyfuUDqXsZtbIytdRp0TkhGE_QDyNmJgm-UaebuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره‌ای از اولین دیدار پوتین با رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/438005" target="_blank">📅 23:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438004">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38969e4884.mp4?token=C0LJkGuOlo6YTZAnr0T3gt6bXnYkG0GyuAbjzB0ob6wG0ZgwVAJrrO4PowJCPmbOEkJs_3nUQGXfve9cDirkw1BtJOxEIHNm0HfNf2aZ9V2m7uHN1EyazqqVg71CMv0XUWV3VcE4V3eH07bXY-ENAV3-erEBO6IYqFb_S4qiQlvZoC-duyA98dA92Wduviys2TVuvHlKg4eeExhOfg-glFUuD6i5wyi5Mr1u0Ixh_WEBh13dem177tNxhUwhfzV5dAwGLdsJMHaBWgqLkKNmVNQ9y3rb0nzU9BH6NV3AXy4TJlK7oAiNEpmeKkVcPMaNsBHdRYpqtRmHTqKyVxv1bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38969e4884.mp4?token=C0LJkGuOlo6YTZAnr0T3gt6bXnYkG0GyuAbjzB0ob6wG0ZgwVAJrrO4PowJCPmbOEkJs_3nUQGXfve9cDirkw1BtJOxEIHNm0HfNf2aZ9V2m7uHN1EyazqqVg71CMv0XUWV3VcE4V3eH07bXY-ENAV3-erEBO6IYqFb_S4qiQlvZoC-duyA98dA92Wduviys2TVuvHlKg4eeExhOfg-glFUuD6i5wyi5Mr1u0Ixh_WEBh13dem177tNxhUwhfzV5dAwGLdsJMHaBWgqLkKNmVNQ9y3rb0nzU9BH6NV3AXy4TJlK7oAiNEpmeKkVcPMaNsBHdRYpqtRmHTqKyVxv1bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره‌ای از اولین دیدار پوتین با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438004" target="_blank">📅 23:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438003">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d49477a9.mp4?token=Y24rLrYfBrRnvkDu0bLzk5xGcChpE1S2p0k-ne_3v-oF9-ys39OHmPmD3MmLujm9U0guOxLus_-8-0aTviQxHIk2_Vwvth95GP13r1cTHNXBtJIfFRmmAny69P1qX5LhhPDRQQkN5KHfELy4NjVnACXE0tUMl2ch9IW5TCpfW6jcM0py7ws4EW_M7SBqfJpzbv4RrDq6E5_57unUzuLDOs17_IxPjJkAeWqrOD09vB_eMrREoC-nLWzj_ShEFTiQ3ojmPRyMGI4NR1LyxoNCwqjoSoFtoop79rzEYNxU5JbzXReQv157ZvBfuHDFMkbQA3oOP5UAEIbNTpSw5CGQNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d49477a9.mp4?token=Y24rLrYfBrRnvkDu0bLzk5xGcChpE1S2p0k-ne_3v-oF9-ys39OHmPmD3MmLujm9U0guOxLus_-8-0aTviQxHIk2_Vwvth95GP13r1cTHNXBtJIfFRmmAny69P1qX5LhhPDRQQkN5KHfELy4NjVnACXE0tUMl2ch9IW5TCpfW6jcM0py7ws4EW_M7SBqfJpzbv4RrDq6E5_57unUzuLDOs17_IxPjJkAeWqrOD09vB_eMrREoC-nLWzj_ShEFTiQ3ojmPRyMGI4NR1LyxoNCwqjoSoFtoop79rzEYNxU5JbzXReQv157ZvBfuHDFMkbQA3oOP5UAEIbNTpSw5CGQNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرزند شهید تنگسیری از آخرین تماس تلفنی با پدرش
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438003" target="_blank">📅 23:23 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
