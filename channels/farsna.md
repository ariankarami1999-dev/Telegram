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
<img src="https://cdn4.telesco.pe/file/fldyJwPOM5x17hiZWuEO6bH7Wq8f60iZcvc01qljUUbhex_jc_galL05S73ryRqoHxT7bGScSDtOYwttEXmiWO_-Kb82fZB1thcxRkn3Q904gzMShbMrpP_WgOVBJT-828PH716NZ9YZgDLdF2dqPaHFPjn9ffMyE4RuCaf8QY4FxOOYGRPjpyfpwuBJCbepgO4VC4RyMI4_o0XCpcx43ukyLPA36uFJHyqvH1Q8hyjFylwZ3BQn2piKf0-lGYrW4JBtrYlWD4uUEVI0KStxKv-zDJbdEV_OsOU7Xlw-4Jn9ob8u_GrU8Ci4tB1R260yF4-XfaQAf1qNMQU7hwKVxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 19:46:29</div>
<hr>

<div class="tg-post" id="msg-451676">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
منابع پزشکی در غزه: از بامداد امروز ۱۳ نفر در اثر حملات دشمن صهیونی به شهادت رسیده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/451676" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451675">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b49763aaec.mp4?token=oUsK9CrpPibxiG0byywML41rZYUqQrW6cpZZ-J5mATdpba-qDunW3ZrYbfrSKsYh54PDaynR0KS_W7YkX6JRtUkL-BFvH_f7RftWQ7EghUuVwy_GjXi8UH-pbSf3jtat4v_w1WluOaKHdRoL_GXqALBvwzUem3f7ImjEOgFCmJiVCheVoyYw_9BKKnALYH5rz38r-v07K0ED5MUuSBlcFn9hwAjrIOgHPdGls7c3DMZEKrS2h6dhCxefhGaB1Dl6SNC_3WwuG9cKB0wk7ajbQVU9tKYMSYA4GXEQvVDpswCuOgINIX4sI33AcM8Pu9jfW3MlchJjeYBRx-uWGEQ7Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b49763aaec.mp4?token=oUsK9CrpPibxiG0byywML41rZYUqQrW6cpZZ-J5mATdpba-qDunW3ZrYbfrSKsYh54PDaynR0KS_W7YkX6JRtUkL-BFvH_f7RftWQ7EghUuVwy_GjXi8UH-pbSf3jtat4v_w1WluOaKHdRoL_GXqALBvwzUem3f7ImjEOgFCmJiVCheVoyYw_9BKKnALYH5rz38r-v07K0ED5MUuSBlcFn9hwAjrIOgHPdGls7c3DMZEKrS2h6dhCxefhGaB1Dl6SNC_3WwuG9cKB0wk7ajbQVU9tKYMSYA4GXEQvVDpswCuOgINIX4sI33AcM8Pu9jfW3MlchJjeYBRx-uWGEQ7Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ارتباط ما با رهبر عزیز روزبه‌روز درحال افزایش است تا بتوانیم با رهنمودهای ایشان مشکلاتمان را حل کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 634 · <a href="https://t.me/farsna/451675" target="_blank">📅 19:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451674">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c33d92d4d.mp4?token=p5GufM9pGbnhoWME8FyppZZEwh7nIozpsU3Exxp4bV_39P86cQMnofySOismCvnfW2aPj3DlzsvXh9LwUIu-xPBbXSKjODHMGqPB_JrFba4UfKuLo9LNtZAHOcVvCi2HIhMGb-oFF1nh_mzCQnJrYhuIrqLRWijdj66LOVd8NZs8QAbBV2PMackbQzjB3S0Rr7oRsHe5L3z_1aju0lAFHrN1pW_B213ubxxxwheeQjRNYebBJm8lIJf1oBFIFk1bLxRCVYqnBxDt5_PXXzhV0ytqk6q8PayhBKGyu1qGJ3wBzK04QX2Cmb4FOQgVX-cuCiU-pb6Un55Rgt2rGQcLUHGHZlHgs4BO8fZVKV850R_nd1m1ejrnHtC_3HRkx1EVoubRcil3gV7XqmSVG_aGF27RPUFytk1bA9futL5B-jHPKrTb_9GClqeoSZSzBq1d8Gy7Tz8j9LBJCg5AKigBraCY8GkPKHmyCFGaJnmjkmLSkM3OsnK5qzszljxmZ31p1KMIn27Obh3RsAyU1-5N2uOrDUQqIL9KaUN1vHLlK_16xTELVvk0xYSMIs-8VCvQkKVknZ07BfRz9lLR3qAV3k8MLUbBRJXjMGmJhpW65CUS0PkIolwaeHQ-q9Jl3ACua3LpG-cAEpUv5jtTw5df3oLkYKb_yQ5auDQAqQK7b2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c33d92d4d.mp4?token=p5GufM9pGbnhoWME8FyppZZEwh7nIozpsU3Exxp4bV_39P86cQMnofySOismCvnfW2aPj3DlzsvXh9LwUIu-xPBbXSKjODHMGqPB_JrFba4UfKuLo9LNtZAHOcVvCi2HIhMGb-oFF1nh_mzCQnJrYhuIrqLRWijdj66LOVd8NZs8QAbBV2PMackbQzjB3S0Rr7oRsHe5L3z_1aju0lAFHrN1pW_B213ubxxxwheeQjRNYebBJm8lIJf1oBFIFk1bLxRCVYqnBxDt5_PXXzhV0ytqk6q8PayhBKGyu1qGJ3wBzK04QX2Cmb4FOQgVX-cuCiU-pb6Un55Rgt2rGQcLUHGHZlHgs4BO8fZVKV850R_nd1m1ejrnHtC_3HRkx1EVoubRcil3gV7XqmSVG_aGF27RPUFytk1bA9futL5B-jHPKrTb_9GClqeoSZSzBq1d8Gy7Tz8j9LBJCg5AKigBraCY8GkPKHmyCFGaJnmjkmLSkM3OsnK5qzszljxmZ31p1KMIn27Obh3RsAyU1-5N2uOrDUQqIL9KaUN1vHLlK_16xTELVvk0xYSMIs-8VCvQkKVknZ07BfRz9lLR3qAV3k8MLUbBRJXjMGmJhpW65CUS0PkIolwaeHQ-q9Jl3ACua3LpG-cAEpUv5jtTw5df3oLkYKb_yQ5auDQAqQK7b2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اربعین امسال با یاد رهبر شهید پرشورتر خواهد بود
@Farsna</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/451674" target="_blank">📅 19:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451673">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoMmdsvvOno-AouebgYzCAczba1gCIc9pD-GiomdorX1Az7VgQc3fXxld0UlBmK9Qwi7GeDqae3RxkSjhaIaAMOWfK9ASlfaW5pVPqYXTi74AmXaB8WelkyJphfjav4G-0366jPHnYaHtz2htUEKU8BOOVp8OX5TEP52ub7LYLv6m1lsnXjSPg1nJcHsZ5HYYc_tvpNBdEJzkHHMwJVD5oXiFF6t1TjotFXsLIKo3uXTPWCtdUtGEoFP9QqfhhPR_hoxUgGK1WHZkdaFo5TQkkjhy2b3Oetm24W2XBUX62HXNd0z5AOuw47jikx-ZoKhD6HFX7Xpv6q3YpMyFgYPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه یک کارخانه می‌تواند روح هویت یک ملت را در کوره هایش بازتعریف کند؟
🟥
کیمیای آگاهی در کوره های فولاد مبارکه
🔘
در چند فرسنگی اصفهان، جایی که افق با غبار درخشان صنعت گره می‌خورد، سازه‌ای عظیم نه تنها به تولید فولاد، که به بازتولید معنا مشغول است. در نگاه نخست، مجتمع فولاد مبارکه شاید تنها مجموعه‌ای از سوله‌های غول‌آسا و خطوطِ بی ‌پایانِ تولید به نظر برسد؛ اما در پس این کالبد خشن، پرسشی بنیادین در جریان است؛ آیا مرز میان ماده و معنا در کوره‌های ذوب از میان رفته است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/farsna/451673" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451672">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRnAnJdo37io9BVf8Kvq59qLF54fnxqPO6MUUpxcM0hAFcILciPga4_Ud5ZKym5hi--_8pJiuxySXGu9D7ibQhEHhRyLX9MEyUyYKp9RJOoXzgIKwaJiIO2Kk-emv1zkFd5kQLKqfiIrglqrYy-GlBJxHuSsvW_E6-bVHFocNk_x_j7t0XPXsWnpJGOXZX4c6qiq9ZhlIYGi25oiG5A2XJmML18GBdA7w9R-SQAo4_4ab4uePs24iZV0cnCjvOMhieLpmWIlS5NEVylJtydgBSX2fOlhwXAVPzx3oGLTzMUtTp4wWmb8kJJ2Dyoc7xSZMfrdzP5UxsnD-Ypr0z5DLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
ضرورت ترویج فرهنگ ایثار و شهادت
🔹️
دکتر اسماعیل للـه‎گانی، مدیرعامل بانک رفاه کارگران در راستای تکریم مقام شامخ شهدا، با حضور در منزل یکی از شهدای والامقام جنگ رمضان، از خانواده این شهید گران‌قدر تجلیل به‌عمل آورد.
🔹️
دکتر للـه‎گانی طی سخنانی در این دیدار اظهار داشت: همواره خود را مدیون ایثارگری شهدا می‌دانیم و تلاش ما در بانک رفاه این است که در مسیر خدمت به خلق، با تکیه بر آرمان‌های بلند نظام مقدس جمهوری اسلامی و فرهنگ ایثار، گام‌های موثری برداریم.
🔹️
مدیرعامل بانک رفاه کارگران تصریح کرد: دیدار با خانواده شهدا برای ما توفیقی الهی است تا با بازخوانی رشادت‌های این عزیزان، در مسیر خدمت‌رسانی به مردم و میهن اسلامی با روحیه‌ای مضاعف گام برداریم.
🔹️
در پایان این دیدار، دکتر للـه‎گانی با اهدای لوح تقدیر، از صبر و استقامت خانواده این شهید گران‌قدر تجلیل به عمل آورد.
🔹️
مدیرعامل بانک رفاه کارگران و هیئت همراه در ادامه با حضور بر مزار این شهید والامقام در گلزار شهدای شهرستان پردیس، با قرائت فاتحه و نثار شاخه گل بار دیگر با آرمان‌های شهدا تجدید بیعت کردند.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/farsna/451672" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451671">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/farsna/451671" target="_blank">📅 19:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451670">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc1730f80.mp4?token=iUMRb6FQ3kQiJ1kkxFvivVi9TyRt8WGxa8r-_XFOOG9o4lyHytUvOqKHJ_SqOvGeWtnmQZrnZ9-qoUWRllvYij3n2Y5WAD-WEVyCRHbB_4_x3YntTOjWvfos7syLkgGA6Ga7Ur9I9FlrKOlV5t1Dc4k1QYM280d8JAFdYsK1DFkVmd1vBuWwjOqZkZyCR-7E-EcfzUA_8A565jMyup5eOhMjAH5rHkaHxerJTEGKm47SZi10vY-xg9S21VPsldQY5-FBu3ikscXG0Lpem_mEvYi7F3qsVKnY0Cv3rEfG4A1F5BrpQ1yrd3aZuQ2B3DrgIrRdWtrBc0NcmLSkcYBKKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc1730f80.mp4?token=iUMRb6FQ3kQiJ1kkxFvivVi9TyRt8WGxa8r-_XFOOG9o4lyHytUvOqKHJ_SqOvGeWtnmQZrnZ9-qoUWRllvYij3n2Y5WAD-WEVyCRHbB_4_x3YntTOjWvfos7syLkgGA6Ga7Ur9I9FlrKOlV5t1Dc4k1QYM280d8JAFdYsK1DFkVmd1vBuWwjOqZkZyCR-7E-EcfzUA_8A565jMyup5eOhMjAH5rHkaHxerJTEGKm47SZi10vY-xg9S21VPsldQY5-FBu3ikscXG0Lpem_mEvYi7F3qsVKnY0Cv3rEfG4A1F5BrpQ1yrd3aZuQ2B3DrgIrRdWtrBc0NcmLSkcYBKKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهاد: هیج مشکلی در حوزهٔ تامین امنیت غذایی و کالاهای اساسی نداریم
@Farsna</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/farsna/451670" target="_blank">📅 19:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451669">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfdd5935a9.mp4?token=QPk9GT8gUi2vPpPU7qibbmdPKTLXg4yfjpast8-J2d63FzcBMNh35BTNw8DVZvOPKXfbMQ7OglhKeoAJUG428Hglfq2dPsjOrWoru6NeE4shLDXA1yzHXM2nXFQHy9EvoOCGYyPK2kwciSv80d24Ti9uPPSUlKHOw_x3A0iJxGgIpn_-leMFC61CH5T5M6EytyQ2kmSAuG15Koz4phigztEhps41HQOvTYgzhasW8FlZh8-t4ICFRaKGnbkL_ypjJ4rzXDoclT8WCZJxD-06xGIlQRKyQOntp9L6xJc8_EAy3mt3YmOgFhH_hYWarqwxxRJT3oW9UWj8vrfE1nYJuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfdd5935a9.mp4?token=QPk9GT8gUi2vPpPU7qibbmdPKTLXg4yfjpast8-J2d63FzcBMNh35BTNw8DVZvOPKXfbMQ7OglhKeoAJUG428Hglfq2dPsjOrWoru6NeE4shLDXA1yzHXM2nXFQHy9EvoOCGYyPK2kwciSv80d24Ti9uPPSUlKHOw_x3A0iJxGgIpn_-leMFC61CH5T5M6EytyQ2kmSAuG15Koz4phigztEhps41HQOvTYgzhasW8FlZh8-t4ICFRaKGnbkL_ypjJ4rzXDoclT8WCZJxD-06xGIlQRKyQOntp9L6xJc8_EAy3mt3YmOgFhH_hYWarqwxxRJT3oW9UWj8vrfE1nYJuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از خسارت به پایگاه آمریکایی Tower ۲۲
🔸
پایگاه نظامی Tower ۲۲ متعلق به ارتش آمریکا در شمال‌شرق اردن، در نزدیکی مرز سوریه که اخیرا زیر ضرب موشک‌های ایران قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/farsna/451669" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451664">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epYrcpdv4Wb6_u5Earlno1AGglMySQLFw0c_vr5mmab95rlRVag4VUJLIjSBoflNV3oBmVEoaYLbctTf2bn48uRplBkrSEt2VJajsP5qDMIelBY2BuTPg5Rjw4WOevV04iIJyhuZOrCRZlBqbDBDojK3rTNTpOuJciku2sL2qL4PYegc0IXpDmIeq6bQ99-UWPAHITmevG5E-aBarId2H_b9LQJ1ZDHkpXq_OjnK1uGN0EoahoAZCVzh70UuYEFu15P-5VXGx9hwJ1vu7v2ldTeRzFK6WPspFTAA4heMdHQBqywNUwnHFiKO0_kAIBUlEZJ3H3mPHrq_viSkqsk8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eabAdHgIert0njTucxQGJ1xUpv2WtovO4TuABtWmJ0R_GqV5JlptU_f4bm3UEaJtzZ01jqggNrHK2H-IereBAp1mZOXWvsh5aKAHpe4lysKta_7UbuRZTniRpJNZ3p0z4w8xSt48PBDAAELmOdElwcT55eoMBNrqGk2JhlWyS_SYgoF-UB9BDlvuX5kJ5W4CidCYvpnIibeyBD4UeqcqxqGn8gsKUxTX8AbAkTWgM3FHRYPIzkH_ckzHhVz-RjrVSjK5Sf8Sdl3UB1pmFIeZqsK3UkTNE0TzWzS8rYYMlT13qXVDGcgl_8LNTE0w7LxC0I4robbu-i4An6OoCLAXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNVLXTdQMxIUF1eXP9MZSSBNyEl0qy_VB3hCEa02adwCcFFeH3b4Bdr8AqE_WMKXYY-2Ph90PVqabhspxGDpNS26cY1ytaL__PEhNA_qc06cPIX3GmdWFoEmryi5mG1JYYyG_34ZoCq0aIknS3BF7GLJ3J42hcorK-hrZI_Dm1DEoj3PX4UvpCOZTWgvVpfZkfekVZLqi1RIqqEcz8po4SnPCLxCIbJIvjCjuHdlTNIYjjxq-YxfQp_iLVFZUGURBLkYJQxb1EIcBuexkpMR_UOxbMbvDyByXKMCifGke_g_WSYVlXMWScn6WSaLDQvh-7W4m1VO_ILm9bBkptNN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rv5V-um5xN0FJqHi2VBoqi1QJrUVTrGs2Jkr1wU1yk5pegljv9K10KBI4tneWj5CawPh9rEMcRwZtV9y4sASrdoFvfKsY0fhhRGWC4104w0rQ-D6d8lTNBqChkD9hvv-wnRw5SC4EIblP91kUSizN0Xc389EMiHIUXfF-22RT6twn01W-jIcnH943h8v1e2mxwwxt_Pv7KYzfyQM_pzqZCsYRQNu1X1vClOBDezdyz_RJkRFsWHZwAfFcleaWdEKMLQJWGLKT1vhM3wg3XX0HWTmiRmDLROVH7BrQCVweW2tflh-3zddwmi0vdWegzpmF6iBtCZhkx7pxFa1zswgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xg4gonE-YDEd-iebWs1oCu6pOXE606BB2kqkp6rNw7Oc89Z6srPPjNdndRD2LwPMKP9W0s9Xsa_pAU_qLyhLhlDmiPsPRAMO-vwwY7SZ5opvIynYi1n_hGS6tJ_wnZblPOZuEK452MWV4783CemFQXAA8pw836l54z9wlzv5sw6azTdT6VTpLx46KrOSn7DghuelVDepvRDgFnK6U1c6ByaGwuaLoTmLpSmi4owXqrHHe_2gR1xaqOI-npKtQGVGVDMkZ4qqSRIvl1KUJhH_6KcOGul2_dBdVG3hjqVN3IbWMPx-zmMj4k-rcY3Tm25FQ5BmpgwRsgYiAY6CUNC14A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گرامیداشت روز ملی صنعت و معدن
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/farsna/451664" target="_blank">📅 19:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451663">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f2d573af0.mp4?token=SGQB1sGLzVZYpSda19IZFkcptggoiakUQarCvKrulLbpTDpKQM0s-UZddcaq7013MYCqBafcGhWbvNMeZCGf6oMF1RaKm46ar_0expDqPocRv436QPOhaUMbeUE6dzWfp86Nm45eXIBjz9eGzf_Vfn3F9iEgry0MvtkbCftN8iWDLM8AiWHscEjL6voC9SSQprkhOb-efXFXSPpaXiStQ_T-wbt4i4OBGQeCyZAz62Ka1uWgdY6QrsQiIzmm9QVhvAja0Ybfm9agDiO67srjm_lu4phuaDPe3AVdcJIf-aHjqVlCUbdVsbXra98z2wJWD_6lj9YEMZJ6Quypb_G59Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f2d573af0.mp4?token=SGQB1sGLzVZYpSda19IZFkcptggoiakUQarCvKrulLbpTDpKQM0s-UZddcaq7013MYCqBafcGhWbvNMeZCGf6oMF1RaKm46ar_0expDqPocRv436QPOhaUMbeUE6dzWfp86Nm45eXIBjz9eGzf_Vfn3F9iEgry0MvtkbCftN8iWDLM8AiWHscEjL6voC9SSQprkhOb-efXFXSPpaXiStQ_T-wbt4i4OBGQeCyZAz62Ka1uWgdY6QrsQiIzmm9QVhvAja0Ybfm9agDiO67srjm_lu4phuaDPe3AVdcJIf-aHjqVlCUbdVsbXra98z2wJWD_6lj9YEMZJ6Quypb_G59Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ تهدیدهایش را دوباره تکرار کرد
🔹
رئیس‌جمهور آمریکا: ما ۱۰۰ درصد به سایت هسته‌ای جدید ایران حمله خواهیم کرد.
🔹
آن‌ها دارند تلاش می‌کنند یک سایت دیگر را بازسازی کنند. ما به همان سایت ضربه خواهیم زد.
🔹
هر سایتی که حتی فکر برنامه‌های هسته‌ای در آن به سرشان…</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/farsna/451663" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451662">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913265ae74.mp4?token=eq2pL_aMDfnJUCaD5JJnZcY97nz7uq8Lf809OgQp2SqhwhRQVS4iLR11zzDpLf_0vUVD1sqQw3ENObez5KErCf6RAin3IrFza1fpzjBEtxLON1EOoNItej9pN12JWukmc_6Fq4GIHFbHV1m34S1WqRcli2LlMw7QvowAFmsqiA78N5AAU6NF8ihR4V6QSL-eDeqzcubUKjkhRZedIw6YAiZfi6Qk-OqcYQEnkbpehP0LJx54UVyQu87ciXK3_Fu4mcfzTX9CWzqspNZHAfOtQOcIg9Iy16uPaLKYIK9bneUDbjskKE59ObFh01rF5E_CQsRXS00J1L4NIJyC55cRtkpSSkHGJadjMU5Cih7n9TcZ_00oaxhJbyXMygfyjEH59c8222n5ZLw46vR-V2ZR0KlDTKaXxkms8sp8368KwEYqX4XcyUNOfcBnjb0G-LurzHPhgoIoUIrjcO0WnIHWLsFysP5f8zBk8DNnzW57GIXv84ewt8euzz7_pgSSJVZBXURM0Se9t9QEx8UYApfgNkwr2DynAVcvP5cWf88UlpeCUBCbYn5eY5905sow2LUt_Y2S__IHRar0OvwaASZy2gbW8G4ySd2xSctqF6C3zeqajU8Ut-aWmOkj8Qjcx5HIt11zBH6g-TiDDP3gH7GpR4UxGrtUh2mAPd9LSQ-TeLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913265ae74.mp4?token=eq2pL_aMDfnJUCaD5JJnZcY97nz7uq8Lf809OgQp2SqhwhRQVS4iLR11zzDpLf_0vUVD1sqQw3ENObez5KErCf6RAin3IrFza1fpzjBEtxLON1EOoNItej9pN12JWukmc_6Fq4GIHFbHV1m34S1WqRcli2LlMw7QvowAFmsqiA78N5AAU6NF8ihR4V6QSL-eDeqzcubUKjkhRZedIw6YAiZfi6Qk-OqcYQEnkbpehP0LJx54UVyQu87ciXK3_Fu4mcfzTX9CWzqspNZHAfOtQOcIg9Iy16uPaLKYIK9bneUDbjskKE59ObFh01rF5E_CQsRXS00J1L4NIJyC55cRtkpSSkHGJadjMU5Cih7n9TcZ_00oaxhJbyXMygfyjEH59c8222n5ZLw46vR-V2ZR0KlDTKaXxkms8sp8368KwEYqX4XcyUNOfcBnjb0G-LurzHPhgoIoUIrjcO0WnIHWLsFysP5f8zBk8DNnzW57GIXv84ewt8euzz7_pgSSJVZBXURM0Se9t9QEx8UYApfgNkwr2DynAVcvP5cWf88UlpeCUBCbYn5eY5905sow2LUt_Y2S__IHRar0OvwaASZy2gbW8G4ySd2xSctqF6C3zeqajU8Ut-aWmOkj8Qjcx5HIt11zBH6g-TiDDP3gH7GpR4UxGrtUh2mAPd9LSQ-TeLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
تصاویر ماهواره‌ای از انهدام مرکز اسکان نیروهای ارتش تروریستی آمریکا در پایگاه ملک فیصل اردن در اثر عملیات موشکی ایران  @Farsna</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/farsna/451662" target="_blank">📅 19:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451661">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnOH_HXPDTXsfkKi6Ue8oTIWEhPrBh2yNP1XvbuoglZw-C7IdUk0YGXfGYSL0qpgvEQ97fLmUtnFN3Ds9srcyQVzRXzGEhhxF_90MsL2CvL-g7T0a5V5NP9GvA31kgFbWYLdraX1fr97hHnW5yP4hIzoSITV16rJczt8NN_Qydz_AN9evG_owhvJ1I_5TM_jV8exFItCBJI6RY90SRIuh_8s6o7Y44F2uqfumsxtL4Rjt2uIqHMVLviVGhUNR1x0U3HqjlPU2O2Ehsstyk-IGqBEjbVUd6wF8kUmG3ASyyNQBpv7S6V4FgXPVD7pbbY0yy3681EKpzaZ_9x_mfW0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیلی: دوگانه «جنگ‌طلب و صلح‌طلب» تله تضعیف امنیت ملی است
🔹
وزیر ارشاد دولت سیزدهم: هرگونه تلاش برای تقلیل فضای سیاسی به دوگانه «جنگ‌طلب» و «صلح‌طلب» نه با واقعیت‌های امنیتی جمهوری اسلامی ایران سازگار است و نه با مبانی علوم راهبردی.
🔹
به اعتقاد من، القای این گزاره که هرگونه ایستادگی در برابر زیاده‌خواهی دشمن به معنای جنگ‌طلبی است، نوعی عملیات شناختی برای حذف گزینه مقاومت عزتمندانه از محاسبات افکار عمومی محسوب می‌شود.
🔹
جمهوری اسلامی ایران هرگز آغازگر جنگ نبوده است، اما دفاع از منافع و امنیت ملی را وظیفه خود می‌داند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/451661" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451660">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b70551d5.mp4?token=PuazLs307bHVjUKsSysKhgHiwhTM1qVW0R0xxOpghR23F6YY7fdGXxeh8MOW6NIG6iScIHrWfQCN8KSf50GHNCPhGFmnD5vlO20-sin6IcBW9_TUz-0EqmuAC8EecPXHPKIIx9MsMnj8jjoI5KHQIZDBdeYvXFAD2T0qdrBNxZuEao7yFKsKk9199P9H44tzTjrpRzgGbFfMt8Zsoz6t9g5Nl1Tkk2QxcvelW0BH0Jz8KW8g1sj0-n5t_CajmOvKLEyY-OJCwZmjqFWkX89duEwIsGZydaj5I3YUYZoQsVgEy4NH8kleWQNPR3eBA3qA7xTbLDPvIQqOyWitA3iOLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b70551d5.mp4?token=PuazLs307bHVjUKsSysKhgHiwhTM1qVW0R0xxOpghR23F6YY7fdGXxeh8MOW6NIG6iScIHrWfQCN8KSf50GHNCPhGFmnD5vlO20-sin6IcBW9_TUz-0EqmuAC8EecPXHPKIIx9MsMnj8jjoI5KHQIZDBdeYvXFAD2T0qdrBNxZuEao7yFKsKk9199P9H44tzTjrpRzgGbFfMt8Zsoz6t9g5Nl1Tkk2QxcvelW0BH0Jz8KW8g1sj0-n5t_CajmOvKLEyY-OJCwZmjqFWkX89duEwIsGZydaj5I3YUYZoQsVgEy4NH8kleWQNPR3eBA3qA7xTbLDPvIQqOyWitA3iOLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای اسرائیل درباره انتقال هزاران سانتریفیوژ ایران به اعماق کوه کلنگ
🔹
روزنامه وال‌استریت ژورنال گزارش داد که دستگاه اطلاعاتی اسرائیل ارزیابی کرده که ایران هزاران سانتریفیوژ غنی‌سازی اورانیوم را به کوه کلنگ منتقل کرده که هدف قرار دادن این تجهیزات در حملات…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/farsna/451660" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451658">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133652fe64.mp4?token=tPmvIeqQzZMXbbZ2IbdSVSI__BxhJfAksRoaK-dGXsNv3UHOnhPmvYIByveHcRu8_mLKdxtjJ8zbTnvIawsG_r0f0z-CklTJmXbqv_pgXSgrEKs8kDKkS3ZtahwnR9sOgqtTfaZIkhWM-t-eZ-Cruv4pE_SOF5mNKHDPeW1LTbKYEJoa_9S5jChdNT2vZslW-DA8X85Zg3MUus1_0wiQVfnZTjVU7b-Sl3LuFv_b6UwCEja6AYSJ9MNWf4v8rF_3UQbmVW2ltbp_XykSejWCNTzAJn-M9AIerDmobEgtOu7z3QwHIbpYfduOfze98b-qmlGtPHBmeN5QftN8GkZ1ujbiQFSRgnODXaAN3H-OI0m0r73LRuZ_tpggDgPPHzzmE-y8nRY3thrDU9MTyWLgGEQfaSZju5dCIjpJJadMxnzQu2EIo089InF_UcZpfO8JMV6pAKLFSRWGFuUOcJ7dQvOpjHx2YNskYwm4RTMu8cOSIMK4X-SKuragJD0i2St9_ZyzcJZ4c35HSlAIrsaPiS5uokwCo_Dx8PvVWZe1OBIvlymG-HxZfSVINEqIHlF977CP7yKy5euOS4yfAGX6PvY4bPmOPHj9zoobTctL4PIgQpym6LNrqYV_gN8m3l2vtnwDap4PX2VUjPQHB5SZCm3kBQhETy0C4RDjosjOpsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133652fe64.mp4?token=tPmvIeqQzZMXbbZ2IbdSVSI__BxhJfAksRoaK-dGXsNv3UHOnhPmvYIByveHcRu8_mLKdxtjJ8zbTnvIawsG_r0f0z-CklTJmXbqv_pgXSgrEKs8kDKkS3ZtahwnR9sOgqtTfaZIkhWM-t-eZ-Cruv4pE_SOF5mNKHDPeW1LTbKYEJoa_9S5jChdNT2vZslW-DA8X85Zg3MUus1_0wiQVfnZTjVU7b-Sl3LuFv_b6UwCEja6AYSJ9MNWf4v8rF_3UQbmVW2ltbp_XykSejWCNTzAJn-M9AIerDmobEgtOu7z3QwHIbpYfduOfze98b-qmlGtPHBmeN5QftN8GkZ1ujbiQFSRgnODXaAN3H-OI0m0r73LRuZ_tpggDgPPHzzmE-y8nRY3thrDU9MTyWLgGEQfaSZju5dCIjpJJadMxnzQu2EIo089InF_UcZpfO8JMV6pAKLFSRWGFuUOcJ7dQvOpjHx2YNskYwm4RTMu8cOSIMK4X-SKuragJD0i2St9_ZyzcJZ4c35HSlAIrsaPiS5uokwCo_Dx8PvVWZe1OBIvlymG-HxZfSVINEqIHlF977CP7yKy5euOS4yfAGX6PvY4bPmOPHj9zoobTctL4PIgQpym6LNrqYV_gN8m3l2vtnwDap4PX2VUjPQHB5SZCm3kBQhETy0C4RDjosjOpsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نیویورک‌تایمز: در حملات چندبارهٔ ایران به پایگاه هوایی موفق اردن دست‌کم ۲۴ نیروی نظامی آمریکایی مجروح‌ شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/farsna/451658" target="_blank">📅 19:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451657">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAE5Uq69NflospUrDyDneFNr-IKtau32MPpwhznpYkZUoYcuCpazdCr9S_xeGNzX1GDfWfkxUyorO37z30B87j-CoKkq9hu3DHQ2dxVylMTzcftEZqcfsvkKPGcK7df01MkKUboPdgyLvN5l1H036naG5LFj3ljs3_SV80OqumcjPv0kmAZfjUyqi6rXsH4ifkICNQD4LHIG7erbeYMJxaXvehViq1UdNTmsqKpAneYyJRdi4PPM7jmC9i5bsD10-vphCfHZSnKgBcmJupR1B-lkt18uPjzhCZtJZXr2TamQWPU9ZEo-Rx27ZmY85yUR3dK4obRGIw14rle3Ku7mzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: ۴ استان جنوبی درگیر جنگ از قطعی برق معاف می‌شوند
🔹
استان‌های سیستان‌وبلوچستان، هرمزگان، بوشهر و خوزستان اخیراً درگیر جنگ با دشمنان صهیونیستی و آمریکایی شده‌اند؛ مردم سایر نقاط ایران با صرفه‌جویی در مصرف برق، این هدیه را به هم‌وطنان خود در این مناطق می‌دهند تا این ۴استان از اعمال خاموشی معاف شوند.
🔹
بساط خاموشی‌ها تا نیمۀ شهریور برای همیشه جمع می‌شود؛ این وعده تنها مختص به مقطع کنونی نیست، بلکه برنامه‌ریزی‌ها به‌نحوی انجام شده که با اقدامات کلان مجلس و پیگیری تعهدات در وزارت نیرو، اقتصاد برق اصلاح شده و صنعت برق بتواند روی پای خود بایستد، بدون آنکه فشاری به مردم وارد شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/451657" target="_blank">📅 19:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451652">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iu66idIitPNiEOl9J2zSTUPccTWGQUmhpxckUs35xxiH-lS3FV69W81bgyO5nn5ua05ZWXjoODuDVBAQcmVG6XZhp6nUv2Od2riJDkEf42Ervwqfu7hVj-aqp3iMoFg4pI9dpM0skYRaWt0aQFAS7ZssY5ilMMa_yP9y52idzxBaSkOpzpm_ni4ym6X3-tGabTwYlcrFjImijzkzu1m_5QOdUEmioAId1sAjmuY2YT3QRIt4Xaygezmqus9adL8Bes1ZKR9oPMm7Sd1JDKDNMaSSdIEUK_6WBnpXGKKTCO60jpmwAl00MN_VLHoLF7L_i4KJ2G8Mcd0CjIKit973ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NgCOTThkhWjeR3wOaChMOYp6XYf5QSoJoa871wKob9HzDuzO7Pw7nEAMmcfDO_Y60MulT7tEglZqkSnqFPZit6AtsQCRDys2KC7_vxFj_4H-v1y0cmfz0jwXJ6HAsspE6AOTeiLzR7hbg2mxRuYXRUYTh3kTO62LLOKocfCuKZ92l-0IUBgftg-yVBYCgrubD1sHdCyfvbGl9xDvSSNmfErRYmycqtvdoddnANv4xFc0Wn2GbMEwz7GQLJOxsqv89LGmdHdhX9fjs73KbvNpNEQr5_7qMapwY3CRFEuElSWnfqfAE1SQ74hvLGWK4JV8_bM3pQTsXvbC_Cul0G8aPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwWR58PG7QVetXSSFopLp2lDMdjOPCJcn-CvUffWUVeZF1aYwBXFwNj0VpHknkQsWzEeigDCHGDb7bX1Mo79fghmJ9c7VssqwNpgHzveUP2YL5vHd4b69Ud2Ald5GBA7IaMqhes2cbice-kbBYj7pz1e2u1GNCqnOu2I46-YuFOwyaAMpl6lWiNw98kOzRsZzzRDsgIWn65g1dGfe1xbJOdqe09j9dae-9T3NMj62q1iThGbT0H4hBTevr8wC_whCtAKGjm9lPSXbyCkR5-jBHoQbCqk31gHsANrB0s9O-DsGWDaX0XPWSVpJttfk9UjgbjVo421-KjurghJ_-0CYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLodbSZ_mUbc-jwePqhWIWlRoFgaE5EQqLeCGf1KdgzHsvHUXhudacyVo26xfvQa1Zj0YXJoA7AzP5NfK95u15Ofivb1RafLvL_EUwPES4pjmChqEyPo02iE-THkIHpS8bP0NV9jCbG7AfvmuZboSSzczBke5nq1XMtubg4UugCfRkG7nk_9yd0LRxlmBVsULGstawEP_mv7fWorqSdd6Ox133FRQeKPGoYHbSWejNVesLnuT1KqASio52fA5EOGTV57IRDnqmX4M5-56O3c0m-h9yGB-VrGXDyQW0RwoqoBAu-K79MxgZKZB7XN2-SJRvIcT-KhNmzbpxuCWEyJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kaPMU_fMwy17aNsOUfyQup4xo9IbYQ1xkQpaxPruDsGAqqscMc_5QWaIoAHjUpo7DWSzb3SWrR9KnlRfZH5CURP6W-lpwXIaYFGKHYtNyVqxQiCRZtGFijoNGt76ccLvZ4Hfb7GTgNJKEdXu_MpajrrjiohNezu3piXFTqENuIuHlVvxQCDe_r-1029Rdto1cFdSLNVYTcAtT3kz0GkYv3_XYnnSZk2-32o0TkOfNUBtthxFw4YJXAoD62B0pGEjACKIPSd6ujnZs2q6jlp2hXDiLyzs8PubzKDMT_LUyk6bHdLykiFHCQymZKxeirfZ6AERn-jR_bzPxsiWA-k2xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
با کوله‌ای از خاطرات جنگ راهی کربلا شد
🔸
سفر اربعینی سیدرضا مفاخری، جانباز ۲۵ درصد دفاع مقدس، از کرج با دوچرخه آغاز شد.
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/451652" target="_blank">📅 18:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451651">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-OWRIuY_H3iuxpIbo9QLeUoNlGQIFyBsDcmScLFl4CUQ0VP2d_g0LdlNuZshp1wIlJ_vZxeRR2pgDGjWG6SebrrHkoaP_PxvqAY2E4BfxRwq0p324Upf-WETK_sjdQRn8rw53pl9Dd1K3GYct9BnhtX6NOLPnBmlSvmHYWrmLruZi6IrxZ51it2uI-WwJOmgl_ReY4CbT8fWXVBgGUJcu0sqiFuiyasRvkPVzrw2tdOorKJGK4bYayC1d00m7Ysbfw7-JAtzKwmizEP6ZZKGKXcPx_kK5wCu633vt8XM8ZmNhpuGQJIPyh_saxbrky6WCJBZ_eohmHNbeO4VkT3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنش در تنگۀ هرمز بارگیری نفت بصره به هند را متوقف کرد
🔹
رویترز: به‌دلیل تشدید حملات به کشتی‌ها در تنگۀ هرمز و افزایش ریسک‌های امنیتی غیرقابل‌پیش‌بینی، شرکت دولتی نفت هند بارگیری محموله ۲ میلیون بشکه‌ای نفت عراق از پایانه بصره را لغو کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/451651" target="_blank">📅 18:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451650">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4ebd229e.mp4?token=b36L4QIOCwqwi8rdu8QaJ6X7tlVSC1k7OvrWipJQJRC3sytN-APe9bGfnH-j5bzk0bbf1B55cOVaxwmihNLYvvmDa9yH5CZ2Lz6VduhKW78rfJBqz4jog30Wg04rlhScNaluBDi93NIMw5dES-QOyf6MNs3bSrAD3Lz3bFSqik3Rc0UqHlxcr_bMGCvXKK41TUM84AmN4rVYJcft-wmaZizhVCtTUv4kegSK3diIhqGcr74SmtE7-_Os-UIupkuo5mu-0xxtrHTUHQxtN9vGL6UYbBwH0nNRZcMgdgBPmfsW2zKzlCj5qXtAtYn_tnCEGnQcdBfiSAkCoNA2C1bPpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4ebd229e.mp4?token=b36L4QIOCwqwi8rdu8QaJ6X7tlVSC1k7OvrWipJQJRC3sytN-APe9bGfnH-j5bzk0bbf1B55cOVaxwmihNLYvvmDa9yH5CZ2Lz6VduhKW78rfJBqz4jog30Wg04rlhScNaluBDi93NIMw5dES-QOyf6MNs3bSrAD3Lz3bFSqik3Rc0UqHlxcr_bMGCvXKK41TUM84AmN4rVYJcft-wmaZizhVCtTUv4kegSK3diIhqGcr74SmtE7-_Os-UIupkuo5mu-0xxtrHTUHQxtN9vGL6UYbBwH0nNRZcMgdgBPmfsW2zKzlCj5qXtAtYn_tnCEGnQcdBfiSAkCoNA2C1bPpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نسلی که برای نوکریِ اباعبدالله(ع) قد می‌کشد
@Farsna</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/451650" target="_blank">📅 18:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451649">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnqR7WbofCEgRa92Pu-k-WeT7FaNchI2eeFrjwMd3KIna-nC8DDgn4C5z0rJP99oJo0P_3RKfsVVqryGwXdH5XDNCgZk9bQ_71Qr5xWl9Y2zbHAoFxeOhQgMJCVhtC7yYZSH22r0BA85AAI-mFyr5AnZsB18EB_20lcwWJgKj5H5nZV1HkO2lEHpyVG7vqcXeDJ0fRHi7k0QGJo6hErwYoJTzO6I5n_VPDs8wG48UPbE0BvYUFt0e4rkARDbjfiD8sGfZssWmxPArBxFVBArM4ZqbS4Gqgui6WMvFJyuhh1Hq8neW9lMXx1wILjDbmJxvbdIY2XUwSQmqE3uc1tVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
به قعر خلیج فارس فرو خواهید رفت
@Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/451649" target="_blank">📅 18:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451648">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S73Rje-B7C2GvXWZ-qV9DV1ZSM1BYCGmeVQFCsFpt9JXG4BmJ8iOtxXkzDf9rF29-uDPVnVz_nqhRyq90jPDZWWUhdHZN9MGF-yPyNxNiB2MewNVvShadgxkl00RpDcJu7_P36LTlmZzUeuNjZfScga0VBL9zQ5-1vJOnLHXK13OWtF3c2aJnPpS3CqTW-QGy-nmudqz4ofz7XoEYvhLWfx5TCP-UTdFlxYUPbNJwDDqI0R39wXEqk61o15sDD1BBItbXGM8n11ynoeyAAK9i7fcdSl3vKQwro3SQetbm9I4BqeU796n2uUNri6Gq3V7yNdh0qAadFoCRQznRO9IBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی: ۲ نفتکش حامل نفت عربستان، درپی محاصرۀ دریایی اعمال‌شده از سوی یمن، مسیر خود را در دریای سرخ تغییر داده‌اند و به‌سمت کانال سوئز بازگشته‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/451648" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451647">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DycHMpp1ASsXdN5kZ4SGH1VUr6ywV2HPedAnfY5pGreHzKN8wUGVVUKZnEqs1vYmcLoXzj4dVh9v7WME10ienOVhZrkw7P64dEr-wr-67fHpdlxvfvLUIUVVaiMX0lgaqCbR2gHr3rfSRRcjylYWexka6VvTYQsuZrRq1g2lk8OUbETg4_wbEWMgnb2i6_FdfU7CA5WcrxmnhpCbVhcYCpKduVW8uwLHOnonYI7bjR6FYX72rpyLcozm9z1E2HaiBk1evfyfeusbG25-PwWGB0d-Go-MbBLsFrxq_1VnNp72dr2rxoV6hv8MV2iLAd3T9WeL_8Q3EimjqqA1dtMCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین معاملۀ پساب در بورس انرژی
🔹
بورس انرژی ایران: با عرضۀ ۲۰۰ هزار مترمکعب پساب تصفیه‌خانه آبفای تهران، ۳۰ هزار مترمکعب از حجم عرضه‌شده برای اولین‌بار مورد معامله قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/451647" target="_blank">📅 18:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451645">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۹۹.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/451645" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۹۸.pdf</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/451645" target="_blank">📅 18:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451644">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RihDzKM01bF3Oo7mZJZZAFhPLGDcRVgsMt4PVikgm3u9jt6H2Dtby2GIXv6swaIcewgCD-4aEEDIg_Ngm4UFKZZOuiLh6tHeplNur7koasSUK4e3SjuK9PPgj9GicCvyH-Vs1K-0RgMTKo7rs05f5W10MqOYeo5p-_xEQWILpMkyJlhRcrlDYEanuJp1yvBX9DKpkphcvIxEy31czAvssejLx-GdvjiYQ8GGpLyIqwNdeESyyc1J2-w9NuB8OaTbBUYFuK6Qfcdqc8QK0szBV7EPhjBFrk1I56urgLPkMq_6A60Nfb9AKt-2MYtiu4APxkzWS857FtruvMUTIpqwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور اهالی فرهنگ و رسانه در دل جنوب کشور
با حضور چهره‌هایی چون علیرضا دبیر، سعید حدادیان، یامین‌پور، خضریان، حسین پاک، خانعلی‌زاده و جمعی از فعالان فرهنگی، رسانه‌ای و اجتماعی، ویژه‌برنامه‌های در جنوب کشور برگزار شد؛ حضوری برای روایت از همراهی و همدلی با مردمی که این روزها داغدار حملات دشمن هستند.
@Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/451644" target="_blank">📅 18:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451643">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRC5EFRF6Jck4sneW2KSDL6zzrcGxf9QYDp3ufzz3FqiKDDQ7svHGOZoK14D5gsSfWMZpNfPUMjJUz4tF_Prdk0wEXlZ_Z90UxvcLkN7_aZU0o1gmmoJdRhR97v8JJurrg7gemgb5-E9t-qQDp-v0Aw6ExueaZTzUxhsH_8DGRVBpv-SY4XoneeLCg77wKVSDgYTfjyWSNuNQGHaeXDLX9RuruHw3YXbt-X-wwkcqqapuXeygQtbMFmcSfxyqNjHyT-m0ii6SJFVsigTXH-82UOivkEFJSn0vHMVOxzs-tfJsohhxt3q8DJBIvVJzo8lbeYYjDPRqHy9-iTpkm6lMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
مجامع شرکت ملی صنایع مس ایران؛
🔰
سهامداران «فملی» ۳۱ تیرماه درباره افزایش سرمایه و تقسیم سود تصمیم می‌گیرند
🔻
شرکت ملی صنایع مس ایران (فملی) مجامع عمومی فوق‌العاده و عادی سالیانه خود را روز چهارشنبه ۳۱ تیرماه ۱۴۰۵ در مرکز همایش‌های بین‌المللی صداوسیما برگزار می‌کند.
🔹
در این مجامع سهامداران درباره افزایش سرمایه ۳۷.۱۴ درصدی، تقسیم سود و دیگر دستورهای قانونی تصمیم‌گیری خواهند کرد.
⬅️
افزایش ۳۷.۱۴ درصدی سرمایه در دستور کار مجمع فوق‌العاده
🔹
مجمع عمومی فوق‌العاده شرکت از ساعت ۱۴ برگزار می‌شود. در این نشست، گزارش توجیهی هیئت‌مدیره و اظهارنظر بازرس قانونی درباره افزایش سرمایه ۳۷.۱۴ درصدی شرکت از محل سود انباشته، از مبلغ ۱,۰۵۰,۰۰۰ میلیارد ریال به ۱,۴۴۰,۰۰۰ میلیارد ریال، برای بررسی و تصمیم‌گیری سهامداران ارائه خواهد شد.
◀️
ادامه خبر در مس‌پرس:
https://mespress.ir/x6RM
@mespress_ir</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/451643" target="_blank">📅 18:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451642">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/451642" target="_blank">📅 18:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451641">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8_N-_msim9cJcj0aGEb0JHtEY0yz30Q3zmvDrchOD3GI1tHF1Cl4vQu0eEeuwtUpaGOuif0j3oFGKzef7xO3UpWc4iFX6zRDotdHY-J8RByCilEg0MM527v7MGZTCtDc_q204P5irETLHzIaYvYgQczl3W35fyFqwGzOEPGelY4HHUJrlzZGWOz9zLRRYCcyeCBlVpSswdJ5DjqTPIfwbPhORZZqU3-ZwIMv7cHKQ75ebHCUEu9ikyNfEgicnxyRmpAZcLA35ZBEg371Z0MUDCbSOqpUwP0Guw_Ec-P2MIvKqiQqMf0C2Hf0QWpR0auQ4xKVTUCsbsC8PjI1E7jZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صداهای انفجار در بحرین و کویت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/451641" target="_blank">📅 18:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451640">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjqfF1SV2ZvsKaSJ_nPRnGG3ISspxLNX7iuVxeyn5WD6F-RMT7zWWUyzUpsI_u5DQT1KakS11_ZWUF1GGaIXgPvGDdlpihGsJM3qNWNnjUrdU-tmqxWNlNZ-5xyLvAhNBFzeRhoZs0QBnpcpRPggx5f4PZj_iYW62LbHRJ1bwvrZrUNrwZlWeaCcWHtHqf6YKXbRxOPbDL32zUinfBH42cdGrgfZRy78QIDXOWoMbRwjmy4dy-UqSbSYJg5hUfRFuYPECml81lW_c84aIPDM6d8_InfZNa3TVwEx6avf0WNkgk-DuXw9qYQWzDN17QC8ndxsK1EJgfTqy9yG_qj_Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«استادِ بی‌تعهد» و فروشگاه اتکا؛ افکار عمومی منتظر ورود مدعی‌العموم
🔹
انتشار یک استوری اینستاگرامی از سوی فردی به نام رحیم زاهدی، که خود را استاد دانشگاه تهران معرفی کرده، واکنش‌های گسترده‌ای را در فضای مجازی و رسانه‌ای به دنبال داشته است.
🔹
زاهدی در این استوری مدعی شد که مادرش به دلیل نداشتن روسری هنگام مراجعه به یکی از فروشگاه‌های اتکا از دریافت خدمات منع شده است. او همچنین ادعا کرد که پس از تماس با معاون وزیر دفاع و رئیس سازمان اتکا، مسئولان مربوطه ضمن عذرخواهی، برای دلجویی از مادرش دعوت به ملاقات کرده‌اند. این ادعا تاکنون از سوی وزارت دفاع یا سازمان اتکا تأیید یا تکذیب نشده و هیچ مقام رسمی درباره جزئیات آن اظهار نظر نکرده است.
🔹
در همین حال، بررسی‌ها نشان می‌دهد زاهدی در صفحه شخصی خود عنوان «مشاور وزیر نیرو» را نیز درج کرده بود؛ موضوعی که روابط عمومی وزارت نیرو آن را رد کرده است. این وزارتخانه در گفت‌وگو با فارس اعلام کرد که وی هیچ‌گونه سمتی در وزارت نیرو ندارد و عنوان یادشده جعلی است. همچنین حراست وزارت نیرو اعلام کرده است که موضوع را از طریق مراجع قانونی پیگیری خواهد کرد. پس از انتشار این واکنش‌ها، زاهدی تمامی عناوین دولتی و دانشگاهی را از صفحه اینستاگرام خود حذف کرده و تنها جمله «عدو شود سبب خیر اگر خدا خواهد» را در معرفی خود باقی گذاشته است.
🔹
این ماجرا دو موضوع متفاوت را پیش روی افکار عمومی قرار داده است که هر یک به‌تنهایی نیازمند شفاف‌سازی و اقدام قانونی است:
🔸
نخست، اصل ادعای مطرح‌شده درباره نحوه برخورد در فروشگاه اتکا که نیازمند پاسخ رسمی از سوی مسئولان مربوطه است. آیا واقعا به واسطه تذکر حجاب باید از فرد متخلف عذرخواهی شود؟
🔸
دوم، استفاده از عناوین و مسئولیت‌های دولتی که در صورت اثبات جعلی بودن، صرفاً یک تخلف فردی نیست. وقتی فردی با القاب جعلی در فضای مجازی ظاهر می‌شود و از آن برای اعمال نفوذ یا تأثیرگذاری بر افکار عمومی استفاده می‌کند، این موضوع جنبه‌ی عمومی پیدا کرده و باید مدعی‌العموم نیز به آن ورود کند. حرکت‌های حساب‌شده‌ای از این دست، اعتماد عمومی به نهادهای رسمی را خدشه‌دار می‌کند و نمی‌توان با آن مماشات کرد.
🔹
این نکته شایان توجه است که اگر این فرد واقعاً دارای مسئولیت دولتی یا دانشگاهی بوده است، مردم حق دارند بدانند چگونه افرادی با این سطح از بی‌تعهدی در جایگاه‌های علمی و اجرایی نفوذ کرده‌اند و خودشان به‌جای حل یک معضل اجتماعی، به عاملی برای ناهنجاری و بازتولید آن تبدیل می‌شوند. استادی که به‌جای روشنگری و ارائه‌ی الگوی درست، با حاشیه‌سازی و القای این پیام که قانون قابل دور زدن است، عملاً به تضعیف فرهنگ حجاب در جامعه دامن می‌زند، شایسته‌ی چنین جایگاهی نیست و باید پاسخگو باشد.
🔹
و اگر عناوین مذکور جعلی بوده است، موضوع از یک تخلف اداری فراتر رفته و مصداق کلاهبرداری و سوءاستفاده از عناوین دولتی محسوب می‌شود. در این صورت، نه تنها حراست وزارت نیرو، بلکه دستگاه قضایی و مدعی‌العموم باید با جدیت وارد شوند و با این پدیده‌ی خطرناک که می‌تواند الگویی برای سایرین شود، برخوردی بازدارنده داشته باشند. اجازه دادن به چنین رفتارهایی، راه را برای سودجویان باز می‌کند و نظام اداری و علمی کشور را بی‌اعتبار می‌سازد.
🔹
گذشته از ابعاد حقوقی این پرونده، آنچه در دل این ماجرا نهفته است، مسئله‌ای اجتماعی و فرهنگی به نام حجاب است. بی‌گمان، موضوع بی حجابی و بدپوششی به یکی از دغدغه‌های جدی و مبتلابه جامعه‌ی امروز ما تبدیل شده و بسیاری از بانوان در این زمینه با چالش یا سردرگمی روبه‌رو هستند. این واقعیت تلخ را نمی‌توان نادیده گرفت.
🔹
در این رابطه توصیه شده است که همه ما نسبت به هموطنانمان مسئولیت داریم و وظیفه داریم با دلسوزی، صبوری و آموزشِ همراه با کرامت، زمینه‌ی اصلاح نگرش‌ها را فراهم کنیم. اما این مسئولیت هرگز به معنای کوتاه آمدن در برابر قانون، مماشات با تخلف، یا باج‌دهی به جریان‌های حاشیه‌ساز نیست. قانون حجاب، قانون قطعی کشور است و هیچ عنوان و جایگاهی مجوز عبور از آن را نمی‌دهد. کسی که خود را استاد یا مسئول معرفی می‌کند، بیش از هر شهروند دیگری مکلف به رعایت قانون و الگوسازی صحیح است.
🔹
اگر فردی به‌جای کمک به ترویج فرهنگ حجاب و اصلاح این آسیب اجتماعی، با القاب جعلی یا سوءاستفاده از جایگاه خود به دنبال ایجاد فضای التهاب‌آمیز و تضعیف قانون باشد، نه تنها به جامعه کمکی نکرده، بلکه به اعتبار نهادهای علمی و اجرایی نیز آسیب جدی وارد کرده است. دستگاه‌های نظارتی و قضایی باید با رویکردی منصفانه و قاطع، هم از حقوق شهروندان صیانت کنند و هم اجازه ندهند قانون با حاشیه‌سازی و اعمال نفوذ تضعیف شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/451640" target="_blank">📅 18:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451639">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4b05777b.mp4?token=lIYyrmLH4axDHIx3YB-_n0tEJCIRnV6v6o8VkuVC2TluuKFt8peq6EZoAm7KV2E43xsGKmxKO8lR8SaBmkwalngsnBd6rJSHdxZ5auYP5ue3XsiDSGAd5TtuLP8lMIeggB0tMv1aTvEI0a7lRR1OL-RMBZaT2PfrqB7bgGxInsc67HL_AD_siQl8pNuUFZnjeHRoULDBavZjek7MOUEF7rLEjNVyy73qLEiQ5qQGIv882kXkIiKnjk28oWbMOTcGrKvl6J8RGTe4jNJeUhKWydLsZf8YpmRXiPp2K6m73c_t0Ip5ySbPqDYzSQ9u0xpjY3YolQieSCGg-BRXkXZq5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4b05777b.mp4?token=lIYyrmLH4axDHIx3YB-_n0tEJCIRnV6v6o8VkuVC2TluuKFt8peq6EZoAm7KV2E43xsGKmxKO8lR8SaBmkwalngsnBd6rJSHdxZ5auYP5ue3XsiDSGAd5TtuLP8lMIeggB0tMv1aTvEI0a7lRR1OL-RMBZaT2PfrqB7bgGxInsc67HL_AD_siQl8pNuUFZnjeHRoULDBavZjek7MOUEF7rLEjNVyy73qLEiQ5qQGIv882kXkIiKnjk28oWbMOTcGrKvl6J8RGTe4jNJeUhKWydLsZf8YpmRXiPp2K6m73c_t0Ip5ySbPqDYzSQ9u0xpjY3YolQieSCGg-BRXkXZq5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خط و نشان کودکان ایرانی برای ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/451639" target="_blank">📅 18:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451637">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌ قالیباف قانون برگزاری جلسات علنی مجلس در شرایط اضطرار را ابلاغ کرد
🔹
طبق این قانون مصوبۀ جلسه علنی ۲۲ تیر مجلس، در مواقع اضطرار و شرایط خاص کشور که بنا به تشخیص هیئت‌رئیسه، حضور نمایندگان و برگزاری جلسات رسمی مجلس از جمله صحن، کمیسیون‌ها و هیئت‌رئیسه در…</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/451637" target="_blank">📅 17:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451636">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwG_ztzORrHLpSwK3tPK3PnxDLysmYymwGiYbSLt4ZlojSSJgK2iODRDWqEPFBFksSmug7IduwOBavZYbdwgVp4e_9iWrBywUDe9-1Vp63BCCJwMLs0PzdmH4d7fVaESwVaANcPTO_87wYUDqU1OFTwWQ_6N15W2YfHVU1PXK4z2-qu8fUp3_hR3TrIXaej71mgS7sREqHWzQmVcFhj1QqTqxpVAoE7ldz27BhDvb9afSOQmLMQfKAtX5_LUt1Gfp9JZwhrbSF6asEma6P6-jiOuU-H3g8tM0kOgQdwXeF64JVlDbqsDhJ2rbpFc6Lw5bcsKcHek_hyriRpM54JD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی: ۲ نفتکش حامل نفت عربستان، درپی محاصرۀ دریایی اعمال‌شده از سوی یمن، مسیر خود را در دریای سرخ تغییر داده‌اند و به‌سمت کانال سوئز بازگشته‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451636" target="_blank">📅 17:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451635">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b9a6787d1.mp4?token=HyPSqARc7PZEy4vdkHhuWZUnYAoP7hiiMgY-lVU0RPCu-FkuxeGPMJkcyG5-X514c-97Mqx2115xGMkDyDSAtVFC3SpzBcZ0mlSuDXTVHMOAvThEk1TVlLY_gKXIIzkNVDdWmyhOPSwQ5xrV1gFM7zDXEq_m1_op3MhZomFv6s9UuwZVbdvdtJ_DANaUGCbdKGB14g3Jte4OlUPnDcd5R-vRHzDBKpTliPoQS8Bs92ktNbftIvDCNPFzm7al8qtid9Kw3gYUi-I9FrkrFtu9YqQeyZ5KL3dni87p_PKA7kFKUrHqd0EHVs46vQ3NKwEWKTjmDcqSbx3RgnnIVn-v1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b9a6787d1.mp4?token=HyPSqARc7PZEy4vdkHhuWZUnYAoP7hiiMgY-lVU0RPCu-FkuxeGPMJkcyG5-X514c-97Mqx2115xGMkDyDSAtVFC3SpzBcZ0mlSuDXTVHMOAvThEk1TVlLY_gKXIIzkNVDdWmyhOPSwQ5xrV1gFM7zDXEq_m1_op3MhZomFv6s9UuwZVbdvdtJ_DANaUGCbdKGB14g3Jte4OlUPnDcd5R-vRHzDBKpTliPoQS8Bs92ktNbftIvDCNPFzm7al8qtid9Kw3gYUi-I9FrkrFtu9YqQeyZ5KL3dni87p_PKA7kFKUrHqd0EHVs46vQ3NKwEWKTjmDcqSbx3RgnnIVn-v1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراق مهیای حضور میلیون‌ها زائر اربعین
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/451635" target="_blank">📅 17:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451634">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920b3a3802.mp4?token=fikvODHuMz_cl9eKMeeKGpLfFR9Eo7TaEpoj0CnXyZRyLiReJxEhBY5Sz-pLis3Q86EUmPhrZJQRXAbrrRojTg1hIeWEKwompPWLNUc79tBWyiNRoXxLcEXpX-NmpazpzqWwD2qy3GvmlX_FPIyVPKxoupun_ADfx-IpBmPXY2J8YFqz6lumaO0443aMRaxfymxTeBR4BrMbF4EUtz5dIcvahZoGB6mB3Q3D41_qU8NC_UICSI0HqXCIG2DaZDtmf8zZbr7imPlegeI52RKwf9zKVAM-LT9aKN58A1FAyKWXModQzMXSxor3EgY1NmhroIobNMAXmxR5sC8-Z_9AXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920b3a3802.mp4?token=fikvODHuMz_cl9eKMeeKGpLfFR9Eo7TaEpoj0CnXyZRyLiReJxEhBY5Sz-pLis3Q86EUmPhrZJQRXAbrrRojTg1hIeWEKwompPWLNUc79tBWyiNRoXxLcEXpX-NmpazpzqWwD2qy3GvmlX_FPIyVPKxoupun_ADfx-IpBmPXY2J8YFqz6lumaO0443aMRaxfymxTeBR4BrMbF4EUtz5dIcvahZoGB6mB3Q3D41_qU8NC_UICSI0HqXCIG2DaZDtmf8zZbr7imPlegeI52RKwf9zKVAM-LT9aKN58A1FAyKWXModQzMXSxor3EgY1NmhroIobNMAXmxR5sC8-Z_9AXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دفاع دوبارهٔ رضاپهلوی از حمله به خاک ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451634" target="_blank">📅 17:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451633">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صداهای انفجار در بحرین و کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451633" target="_blank">📅 16:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451632">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فرانسه کاردار سفارت ایران را احضار کرد
🔹
وزارت امور خارجهٔ فرانسه از احضار کاردار سفارت ایران در پاریس به این وزارتخانه خبر داد؛ این احضار درپی ادعای بازداشت کارکنان سفارت فرانسه در تهران انجام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451632" target="_blank">📅 16:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451631">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1f14ee037.mp4?token=DvpoPbm0x4cEKQWT_XNVGeiKS65panEw2oUcVEiOtxtOqT6urXFqBdn-ACfQFQFmsEH3B7FRHP_aqT8sjdkkUnz_XhKd-NZvl5IzxXpwjfhK9ABroz_KghQ_R4SoClmKDqoUorYDsZwiQT7fZKO2KmDOO9Kkv-8eXLG5vzW6eAZbeZGlQxsRcj1ofMqbYpMbxVi1292bJ2ICSp9d_f9znYHsZUfUjS1PXJN0RZnZqCRA-XurA74jZdgsHsM6KEvfIB7kcnizg-gOQ2RCN3lMkwX92qRqdaRmoRlefsJ8dOOa0dvUQCRd_Np-V2r9Z86Bbv04E02p_FztX68DQ5d1BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1f14ee037.mp4?token=DvpoPbm0x4cEKQWT_XNVGeiKS65panEw2oUcVEiOtxtOqT6urXFqBdn-ACfQFQFmsEH3B7FRHP_aqT8sjdkkUnz_XhKd-NZvl5IzxXpwjfhK9ABroz_KghQ_R4SoClmKDqoUorYDsZwiQT7fZKO2KmDOO9Kkv-8eXLG5vzW6eAZbeZGlQxsRcj1ofMqbYpMbxVi1292bJ2ICSp9d_f9znYHsZUfUjS1PXJN0RZnZqCRA-XurA74jZdgsHsM6KEvfIB7kcnizg-gOQ2RCN3lMkwX92qRqdaRmoRlefsJ8dOOa0dvUQCRd_Np-V2r9Z86Bbv04E02p_FztX68DQ5d1BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امارات چطور وارد دهان شیر شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451631" target="_blank">📅 16:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451630">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu6PeZuaWn1xgJsMeV1j2iNhquu_a_gLF8e-ganjsCZCDS2l-gEQVLtfS2sX598MwkLhwqevub-zdT75qgc0VtDIiJsIWOEF5q64WlXk8xe--W0f23E64jHgRqu2oc8B-MF1vaUCn-343UU06dXmNeLbcowbXTJw9Jmww7QTA7VLhWyCK3UmDPxoFsXZszqi_ABNXm9mvT6dg4G0fL-8gUwhzh7YWw69AxLWmJwjHDH2e4nTxX06sbU4B3eg5F0QtBTloShA-9qdqOW2VfevZo-0xHDvDlI8gCOYrwrIfvprsNUDPnDwJhEoKnx25IhKlu_hIFf6r9Ch0bolpXAtcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار جنگنده‌ها و هواپیماهای سوخت‌رسان آمریکا از پایگاه‌های منطقه
🔹
به گزارش شبکهٔ ۱۴ رژیم صهیونیستی، آمریکا در واکنش به حملات گستردهٔ ایران، اقدام به تخلیهٔ پایگاه‌های خود در منطقه و انتقال جنگنده‌ها و هواپیماهای سوخت‌رسان به اراضی اشغالی کرده است.
🔹
همچنین یک تحلیلگر مسائل نظامی و امنیتی در شبکهٔ ۱۴ رژیم اشغالگر، اعلام کرد که آمریکا در حال حاضر قادر به حفاظت از پایگاه‌های خود در منطقه در برابر حملات ایران نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451630" target="_blank">📅 16:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451629">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBn6V239bPVVgkcZ_vefKsdDEThaNTtKjKJs1v_bO62kzhpk0dVwkBleLlYG41YPFwuvbATQEMY1IQG4DFceivF5ySvkOZmETfXQ0fBVCI8tE71SRlrc-KGA16kdimJX7iOEE7PSeRbyUa4nnws7kK3bHTIwhd0W6z8BuBZVoU9cf2c2sednunk6u8nemI9ThAy1M-VCF1poC1_jnEgBRnE_KxFQsiIs0W5_xo6yiiyInJL2EcGivN7Q7mM4pqRQj18GMrEoAfISfVp6eUu7hAJwAJeL_Nk1EvqguOWabc6fOBYMeVJ3UdKtHJrxUnPMgc-kw_jOCdBnw-UNkB9ruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت و نان عربستان در حلقهٔ محاصرهٔ یمن
🔹
نیروهای مسلح یمن با اعلام محاصرهٔ دریایی عربستان در تنگهٔ باب‌المندب، مسیر جایگزین صادرات نفت این کشور را هدف قرار دادند.
🔹
عربستان که برای دورزدن تنگهٔ هرمز، بخش عمدهٔ صادرات نفت خود را از طریق خط لولهٔ شرق–غرب و…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451629" target="_blank">📅 16:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451628">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt9vF3WTI4I6X0wyJShMx60u8UCmgUBugS0YuDIoH7aSl8HARmwpxlyPwJdRdp_BWhSDKZ1CaCvGVCLlmZvce9F75_XF9PwH30j41arDe3zm_huxB-tQe-MfFvTJTinCIen1yQvkV2VY9cKnjlOxwfDtiSPT6jjirlZ7mj3Ktn0ao_z4BiTAa2ZTfVEUbxolf_7tXgvcJF3OkM-Lv7zcQfHDYeYqk6uOHNkuKEkLXxgh3iv-ZRG3Mby-7Qhq9f7rno8iEqXBSst-oLa0ZYjyoXNzhHE020BMyoi-Ye3R05AfFqqJrKc0PYbh67qGTyAKv4Bch4DJ_NPzrgZ3pLXkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بهرام گودرزی مدافع ۲۱ سالۀ فصل پیش آلومینیوم با قراردادی ۵ ساله به استقلال پیوست.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451628" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451626">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVaWntrDWdmPqyaV91ZFhvcE8sdV2Z6ym2FtGjkNf9ZRi9Qr890cqde-HeBQ4KO1vgEbp22rRi4E5OdAEJwWb7iJD16l4yj3_SeHEOVFWiI3L8_ITuzJiGLTSK_huxbW0R8nrQqr6qLCY7G2NVyGL1C-CvKvEWbdGbGK1BtfnAh8i0tuMHxiGluscJC6rDFaAqPRjlfuplghA_USUw4BDEh5_ckIC39cQjRuLP-CeKYnF6wWT-iWRrV48wAK3yZBKmRlcmDcRSwGEIYmt92m0CidWizYp8ohN5AzuTrdJqaezOJQJ4XW47ZkQQGptXnAGAyXpD7hQ4ODNczTakJw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZQyxMOybpdta90uELFmG-sl8XdUG9XyxWio-1cQO7WhBX-w0F0faLVEOgAm-G4apDGuTzlYP8npFiAJwCEvVn0F39gqWCwe2aqLrNBDPeCfMQGHA1fFQF1kki1GhpAGImxFvURVDp0Hs5uwxwiIGnlJIs5PNLwpmSia_yrks9n5RJGtzM8j8NlKl8wfcO0yNj3AWjqa56u58bYyd17AHA1lb7YPYUDSK7U7OxjSOrSZsUpAVRY6pw4GDZo8AVRJp98vrf5JHgU0z_tcF8kaIPhmxeuAJzfTwKT46yNRJTuFGXhTVIl3yLDhbYN-z9E-_oFoTtnNq875RMpH91Al2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نارضایتی اکثر آمریکایی‌ها از عملکرد ترامپ در جنگ ایران
🔹
بر اساس نظرسنجی‌های منتشرشده توسط فاکس نیوز، ۶۹٪ از مردم آمریکا از عملکرد ترامپ در موضوع جنگ با ایران رضایت ندارند.
🔹
در این نظرسنجی که توسط مؤسسهٔ ایپسوس و روزنامهٔ واشنگتن پست در ماه جولای انجام شده است، تنها ۲۹ درصد از مردم آمریکا از عملکرد و نوع مدیریت ترامپ در جنگ ایران رضایت دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451626" target="_blank">📅 16:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451624">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8gxPS0a_S9NRpLAPJYyjx2yFWwXaXB1KcITaK-4M0vjmkuQ3vxSl5o6GjbECUdoDCBjjzJaIgUr7UitGHnm47sJsZkVtPSTYRdmuObv__p3v1w420Lm6oPv4b-Tbmg9c684NubqbsZuDUuO7cEB_kv-cFi4KFfh8IP0alKR8-kt2QwqMPDFmMNbTtP0kyNT88Mmbgj2qydmt4pVG42JviCb6DzCoPhmjWAIEDF1OiFVLuN9JEO6SzpjFbTprjBurPv37MevIGQ0F_FjxLz0prPHIqYoeTvkS-Hr6JVpMcDgym87_5yJHngFpnS8l7Jlv94ymtX-Yl1VpHh_3YOv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفحص ۶۲ قطعهٔ دیگر از پیکر شهدای مدرسهٔ میناب؛ ماکان هنوز مفقود‌الاثر است
🔹
فرماندار میناب: درپی عملیات تفحص در مدرسهٔ میناب در چند هفتهٔ گذشته، ۶۲ قطعه از پیکر شهدای دانش‌آموز کشف شد که پس‌از آزمایش‌های ژنتیکی مشخص شد که این قطعات متعلق به ۳۲ دانش‌آموز است.
🔹
رئیس‌ دادگستری هرمزگان اعلام کرد که با وجود انجام عملیات متعدد تفحص در این مدرسه، تاکنون هیچ بخشی از پیکر شهید ماکان نصیری پیدا نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451624" target="_blank">📅 16:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451621">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-text">منتخبی از پویش‌های پیگیری شده «فارس‌من
»
🔹
شما
گفتید
: به بلاتکلیفی مسکن مهر اسلام‌آباد غرب پایان دهید.
🔸
معاون مسکن و ساختمان اداره‌کل راه و شهرسازی استان کرمانشاه
گفت
: با ورود دادستان و فرماندار یک فرصت نهایی ۴۵ روزه برای اتمام و تحویل پروژه به پیمانکار داده شد که اکنون با گذشت دو هفته از این ضرب‌الاجل و افزایش نیروهای اجرایی، پیش‌بینی می‌شود بخش‌های باقی‌مانده طی یک ماه تا ۴۵ روز آینده تکمیل و واحدها به بهره‌برداری نهایی برسند.
🔹
شما
گفتید
: به وضعیت شیفت و اضافه‌کاری کارکنان آبفای ایلام رسیدگی شود
🔸
مسئول روابط عمومی شرکت آب و فاضلاب استان ایلام
گفت
: تمامی فعالیت‌های عملیاتی به‌صورت شبانه‌روزی و در قالب تیم‌های چندنفره انجام می‌شود و ضمن رعایت دقیق قانون کار در پرداخت اضافه‌کاری، تعطیل‌کاری و شب‌کاری، استراحت قانونی کارکنان و تداوم بی‌وقفه خدمات‌رسانی به مشترکان نیز تضمین شده است. است.
🔹
شما
گفتید
: برای تسریع در تحویل واحدهای مسکن ملی اردبیل اقدام کنید.
🔸
معاون مسکن و ساختمان راه و شهرسازی استان اردبیل
گفت
: از مجموع ۲۷ هزار واحد طرح نهضت ملی مسکن، تاکنون ۱۴۰۰ واحد به متقاضیان تحویل داده شده است.  ۳ هزار واحد دیگر در شهریورماه آماده تحویل است؛ مشروط بر اینکه دستگاه‌های خدمات‌رسان نسبت به تکمیل انشعابات اقدام کنند.
🔹
شما
گفتید
: شهرداری کرمانشاه معابر عمومی را از دست متصرفان آزاد کند.
🔸
شهرداری کرمانشاه
گفت
: با رصد مستمر محلات، به متخلفانِ ساختمانی و سد معبر ابتدا اخطار داده می‌شود و در صورت عدم تمکین، با قاطعیت با سازه‌های غیرقانونی برخورد و تخریب خواهد شد. از شهروندان تقاضا می‌شود هرگونه تخلف و تصرف معابر را برای رسیدگی سریع، از طریق سامانه ۱۳۷ گزارش دهند.
🎉
شما نیز می‌توانید مطالبات‌تان را در سامانه «
فارس من
» ثبت کنید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451621" target="_blank">📅 15:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451620">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e708a1f5.mp4?token=WMSyF0Ufm0cVTD3K1jbXCSCsG8ljhy_8i8KPABnbwLrgkRfmINzgHYOFZZ5qMPZdRgcsWWdYz9-vgTsJA5v_YFGlEgc4tRUPfG6noKsFFSAQOUJezf0ORM_I1ljdHuWeVDzs8FdoVjolNBOTRs5L2x7TeVa_XKScbNyc7tlxDM9qE-B29YFmUGdZxNgReTHuI_8RYoVJVr1jZ3aCaBKZjFPTCc7tIrIoIlNzPLOuhLXx8_flnSk1KpKhD41dBDRIvlRlUlNiY73Cha830IK0AOqugtY88JmH_a29hjhdxui69iNhN6pevK0HE5rQJGqqyi6U87anK7Dtzfpj4RYS1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e708a1f5.mp4?token=WMSyF0Ufm0cVTD3K1jbXCSCsG8ljhy_8i8KPABnbwLrgkRfmINzgHYOFZZ5qMPZdRgcsWWdYz9-vgTsJA5v_YFGlEgc4tRUPfG6noKsFFSAQOUJezf0ORM_I1ljdHuWeVDzs8FdoVjolNBOTRs5L2x7TeVa_XKScbNyc7tlxDM9qE-B29YFmUGdZxNgReTHuI_8RYoVJVr1jZ3aCaBKZjFPTCc7tIrIoIlNzPLOuhLXx8_flnSk1KpKhD41dBDRIvlRlUlNiY73Cha830IK0AOqugtY88JmH_a29hjhdxui69iNhN6pevK0HE5rQJGqqyi6U87anK7Dtzfpj4RYS1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تبلیغات «انقلابی» موساد در فیلترشکن‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451620" target="_blank">📅 15:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451619">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIi4-WwgjGnnbP356YitOObm2LMpUl7jqtonD2saOjdF2ArGIyPBQhSjtLAKbObNcR6dem5HKPDyRm3lL7OK5lusPB7iN3NG0o66TrlPixBg2k63iQKmdUo1Jt4j9lHJJ5MJD-QoiKH5fL0WR4pwsnUFqLZ4TZ3fD-TjwY_5FfPHmGvFyPdwWiD2BiH0rApisTDurNPOdYORWDZX0qyE7Vxa7gpGLMg8xSpGo02wcBZC_eRohXjN5cxQTgZO__g0_E3_I6AnVxcRmXo48LSatdhtkD33kgUgzqomU7LeG5HVVa6edjBwSr0ILODsYpfHMLXqsEikuOfp00ASzIDV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژیم صهیونیستی: شهردار نیویورک باید بازداشت شود
🔹
سفیر رژیم صهیونیستی در آمریکا در واکنش به صحبت‌های شهردار نیویورک، دربارۀ احتمال بازداشت نتانیاهو در صورت سفر به این شهر گفت: کسی که باید بازداشت شود نخست‌وزیر ما نیست؛ شما هستید، آقای ممدانی. او همان شهرداری است که کمیسیونرش تلاش کرد با نماینده ایران در سازمان ملل دیدار کند.
🔹
نتانیاهو به نیویورک خواهد آمد و شما هیچ کاری نمی‌توانید برای متوقف کردن او انجام دهید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451619" target="_blank">📅 15:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451618">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8a3eeac6.mp4?token=DgwflQSrV5Sr6Bqos8kK25QyzBnLJ4xf8kM1JkHPPxIKUHwd2xaoytr1HPr9_6ppbnuQYQiaA8Mwk1sS5ArNzoyc-NnR1JQkEXFR9-GUfxAQ4La2eLn0DpOJLSaHyBwFvAIoD9xng8riSbjpT579jQ-pX-JVR8ERgcn7IaTTvlQtF8szKIKUrzCVgEa0E-Z-NW3Kgg7_7D6bLBGlBZSm4uaGsuPIzyr25AK8HIMZM3vnB4W6B-8eIKdVZgFKWoAUHI-zPfOXeAl1zrIzJs1YcB2Vx1AKu0rhPrJw7kk4Iyk2nMTyFrttX07RevRg8ar0j7GFpJTzvuaTXtQRfAGEoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8a3eeac6.mp4?token=DgwflQSrV5Sr6Bqos8kK25QyzBnLJ4xf8kM1JkHPPxIKUHwd2xaoytr1HPr9_6ppbnuQYQiaA8Mwk1sS5ArNzoyc-NnR1JQkEXFR9-GUfxAQ4La2eLn0DpOJLSaHyBwFvAIoD9xng8riSbjpT579jQ-pX-JVR8ERgcn7IaTTvlQtF8szKIKUrzCVgEa0E-Z-NW3Kgg7_7D6bLBGlBZSm4uaGsuPIzyr25AK8HIMZM3vnB4W6B-8eIKdVZgFKWoAUHI-zPfOXeAl1zrIzJs1YcB2Vx1AKu0rhPrJw7kk4Iyk2nMTyFrttX07RevRg8ar0j7GFpJTzvuaTXtQRfAGEoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آورده‌ای نواده به قربانگاه...
🔹
نمای معنوی و باشکوهی از حضور دختران خردسال در جوار مزار شهید زهرا محمدی گلپایگانی، نوۀ رهبر شهید انقلاب در رواق دارالذکر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451618" target="_blank">📅 15:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451616">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d75d3fdc03.mp4?token=jbET60bYjTwfYHwQuYDs2WU1nbMdmSDbEzBqPQDQzV7AVlrikCW6og2x4sWCYeWtjiyDSx3S_YjogzUTZZ0sYCaSrvxnxHOEHTFQEGkVxBmO6exGmGq9C_uB4WNksrmS9isZppv5qHN9XrASHtEOQsYmaFWxf7E1uvifP9Xi8B7oRVmQQNrYNHk7CoMiMnSd678OiyjOrDLG3v64FYonEWLuXK6VXnhP5-HiI7Brw7fzA0A5WLpWE_DjES1o_EFFUCB2968g6cIEOAJPb_tyZm6U_mGJdlGfqiImPpg69VPsB5hi4w3fUgY88tMYrnZmfzoF4zlM_B1IJ-QoU_2mlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d75d3fdc03.mp4?token=jbET60bYjTwfYHwQuYDs2WU1nbMdmSDbEzBqPQDQzV7AVlrikCW6og2x4sWCYeWtjiyDSx3S_YjogzUTZZ0sYCaSrvxnxHOEHTFQEGkVxBmO6exGmGq9C_uB4WNksrmS9isZppv5qHN9XrASHtEOQsYmaFWxf7E1uvifP9Xi8B7oRVmQQNrYNHk7CoMiMnSd678OiyjOrDLG3v64FYonEWLuXK6VXnhP5-HiI7Brw7fzA0A5WLpWE_DjES1o_EFFUCB2968g6cIEOAJPb_tyZm6U_mGJdlGfqiImPpg69VPsB5hi4w3fUgY88tMYrnZmfzoF4zlM_B1IJ-QoU_2mlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیاتی از آخرین حملۀ آمریکا به برج مراقبت دریایی چابهار  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451616" target="_blank">📅 15:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451615">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaddca6c2.mp4?token=PFwHLBMOFgVD79t__uQCcOX7se4eIhk7TcrDKPttYZ75JvQSnG1a8Jwqbf6GXsOFvExUo18HRjUSkCT1tly7ThJ-NvCbIxC2lek7nwbRItF-bQd40DAFTJXavNWYI7SdHE9-SvWei3WMHlb0N_C1Txle7b8tqRHutIOn4BAdD3JeYPIsSv5LG_WUl8eaDk7_4VfDAOoTthCXYui958iTBqOBZPI78mXXREgGB_I6llMHYXLX5N5kmS_CwZgXAUWcX2qtW2at70KH0RWaByYJa0uqiTF7bkieh1wU7SXI2Q6xjWsZHSfkme0G6vIrFcg-Lf9GNJbWknIpcJ1u1WB7nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaddca6c2.mp4?token=PFwHLBMOFgVD79t__uQCcOX7se4eIhk7TcrDKPttYZ75JvQSnG1a8Jwqbf6GXsOFvExUo18HRjUSkCT1tly7ThJ-NvCbIxC2lek7nwbRItF-bQd40DAFTJXavNWYI7SdHE9-SvWei3WMHlb0N_C1Txle7b8tqRHutIOn4BAdD3JeYPIsSv5LG_WUl8eaDk7_4VfDAOoTthCXYui958iTBqOBZPI78mXXREgGB_I6llMHYXLX5N5kmS_CwZgXAUWcX2qtW2at70KH0RWaByYJa0uqiTF7bkieh1wU7SXI2Q6xjWsZHSfkme0G6vIrFcg-Lf9GNJbWknIpcJ1u1WB7nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: اسکلهٔ پشتیبانی سوخت ناوگان آمریکا، محل تجمع پرنده‌های جنگی، مرکز داده‌های اطلاعاتی و یک مرکز سیگنالی و مخابراتی آمریکا درهم کوبیده شد
🔹
روابط‌عمومی سپاه پاسداران انقلاب اسلامی: مردم قهرمان و با ایمان ایران! دریادلان غیور نیروی دریایی سپاه در امتداد…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451615" target="_blank">📅 15:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451614">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فوت کودک ۳ ساله بر اثر حملهٔ سگ‌های ول‌گرد
🔹
دادگستری کردستان: درپی فوت یک کودک ۳ ساله به‌دلیل حملهٔ سگ‌های ول‌گرد در امروز، ۲ نفر از مدیران شهرداری سندج دستگیر و علیه مسببان این حادثه اعلام جرم شد.
🔹
سایر عوامل دخیل در این حادثه که مرتکب قصور و ترک فعل شده‌اند، شناسایی و با آنها برخورد خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451614" target="_blank">📅 15:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451613">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad19ca0b5.mp4?token=moafXhRF96IcftfdcEWdnteoaz8hkcNIYZCmFAKgsnHGtjzJU6j2qtUTdSxYC2VCuLFDijEtJm9eM8zpvuavUH1bhnxTi-CCel3HlTCDrteYbGxIZegX8pS4E4vS30B9a4ehLIVkyQ6Yjnh-xxFBQEo57iOyKbSaUuiHvUyEWYFln9YO4x6ZmWNm5UTK0fQswTt4dk-0nvwfAEHBOGrgq8rOivTwv5bEpCjgh0DYvXj-RNjg-KNf37W55GWL9i1aolAmsZdE2gqGfVquVcEgKXdSi-Va7JySyu4-jFUeas3-CjazwCWHQly73XvIkuyzGjvqassrGSeTu0fGWvrzKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad19ca0b5.mp4?token=moafXhRF96IcftfdcEWdnteoaz8hkcNIYZCmFAKgsnHGtjzJU6j2qtUTdSxYC2VCuLFDijEtJm9eM8zpvuavUH1bhnxTi-CCel3HlTCDrteYbGxIZegX8pS4E4vS30B9a4ehLIVkyQ6Yjnh-xxFBQEo57iOyKbSaUuiHvUyEWYFln9YO4x6ZmWNm5UTK0fQswTt4dk-0nvwfAEHBOGrgq8rOivTwv5bEpCjgh0DYvXj-RNjg-KNf37W55GWL9i1aolAmsZdE2gqGfVquVcEgKXdSi-Va7JySyu4-jFUeas3-CjazwCWHQly73XvIkuyzGjvqassrGSeTu0fGWvrzKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدیویی از محل منهدم‌شدۀ حضور نظامیان ارتش آمریکا در پایگاه الرکبان اردن
@Farspolitics</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451613" target="_blank">📅 15:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451612">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILaNge5tPuIqysTb5BBZxQp_9XDtXTsA9BeP5V6I8GdQwXIZM4r3xwy6jgZJ-5IwO2ZzMUl80vq4kaiQ9V_2dF4Z6wz1Kw7kHwsHkeyDqeARon23Zz5R8XXNqKe-anNuEl6vp4pfw8uyLol7oG24T2K9Za4d-1eQ6cc3Xh_PX6-djsybP0IWSBRh4GNWp4YjN9JTvveSdpK9bf3A4mvLftcgnXRRNvKT_o5tPGbrBxHqsjnYXbOMznqA_JdOoQLsSYe9BTfvn9lvp9dtvaBRL6tRZyoF7OOogWxx16TbZOOj1CjhFDTYCorsdh89B06JwF1FfaTQPDCLRebqHKv9IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت رفاه اجتماعی: یارانهٔ تیرماه دهک‌های اول تا سوم واریز شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451612" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
نیویورک‌تایمز: در حملات چندبارهٔ ایران به پایگاه هوایی موفق اردن دست‌کم ۲۴ نیروی نظامی آمریکایی مجروح‌ شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451611" target="_blank">📅 14:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaEDRpyhnItcaxii_RpOv5YtUL4lUPXOcJlp7mXC_K_xb9X4WJ03xhRmSHpMwkAFb4ZOoMOMXDapgRTnvMXrO_H3BuSh-zkcy6YIZR2jBRsOHatCmvdErg2Q9z1A-atfH_lj72Sd524fKNVseM1NZ8lt6w5HpjysNZmDOlcKb3ef2vAfK6OYP-iKYN3aYnooTGCwwSP532YfxlO_MhM7f3THQ7PvIUsIU9EUno8G5kY3cDfAIE5kR_LJ5jxxycywvwhh1jJpYIfBS-0SxcwC30OyUMfDcSmKsa2y-pFAgbkWeeJ7cGMWOuIakNTFKQLtEaSh3tR8FW0ElmTnmrjWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ سردار قاآنی: رژیم صهیونیستی باید بپذیرد که با وجود همۀ جنایت‌‌ها نتوانسته مقاومت را متوقف کند
🔹
پیام سردار قاآنی درپی انتخاب خلیل الحیه به‌عنوان رئیس دفتر سیاسی حماس: عرض تبریک انتخاب دکتر خلیل الحیه به عنوان رئیس دفتر سیاسی حماس، باید این انتخاب را به شخصیت‌های…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451610" target="_blank">📅 14:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEzzBWdGcWkq1CDf1JCLkFPGjSQUi2Xn3ydwONZIzDE5uMPuxls445TRzSNotRuhBc0FTwLGbnMLV-14pdZCZ2BqnBIerOq5NUS1MvW8K8ow0cOeaoqK6njMOSpn5QEBsTgHGIM_Kk2aZuB5cWj7Yl2LHE-JCvS1ZmVrMGC5gRoDS7jnQbq16Qn7SnvV6YD4p5g4IbNyAKpQQaivQnAVQ2FSwF_ZqQnyhBabYz1gvOcPbBrAKjOClok88tc8WEAGFfSvezZ6nkec33NjKMPLeWeOIxV_tVKdMG2Bisi1NpoD87bOBXGpU1CZDVMWNkkNpwCk4ZnILPyA2alrSQBpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسال‌کنندهٔ فیلم پرتاب موشک به شبکهٔ معاند دستگیر شد
🔹
سپاه ابهر: فردی که با فیلم‌برداری از لحظهٔ پرتاب موشک در آسمان و ارسال آن به شبکهٔ معاند «ایران اینترنشنال» اقدام به همکاری با جریان‌های ضدامنیتی کرده بود، توسط سازمان اطلاعات سپاه ابهر زنجان دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451609" target="_blank">📅 14:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451608">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95c26614d.mp4?token=sR3B9uwtMDvzrgpq_jL1kSqo4unJUbii3cHwmSrg7kCyycS3AwgQfiEVYW9p2hGgH2Z7eGCTCIqU8FTZsMDeh_xbYuUThULvmY-OnzwuJN-3p3aJQg0W8EQL5VLlv01JuVewoaK8jMJ1fYZMWNguuOInopaF5onMANd66f2GPBzYIixP2KOBjFiYq8gVOKoMFG8Uskn5exsbh2De7BGgj9nAJLhpIDGWksvyvsy4yyl05tKe-QMQ22aggtPQXbzCNzsvK3M2YsAKHOULl3AFeuMAjXk1wbViq_j0m-CrTqTw96ssw_DiwhQGGlPKAwJmpEpneNPs8LwXZZv8Jv0iWyNJWgbmSmixg9X5KcSArBl40e_RVUlnvhDDTQmNGPTwDdwlW8ahv0asxoPSl71NXer_Aq03j3xmTBQogE5fKOFGCdH9ENiKPbB-rQ18SyZUuz-nHfzuI6M5teqR54C-7TEv4IvoPaVFRAOIJxiJ9_S9UuhdZrpmevO8Vb7uV6iT0nppFF982Pp6lJyg6N98NOgJVM6gZWsPhLio0KH3fxFu49EAJKEATRtWvS8YxjluXeDQts3X0pEShRg7JIJOyf8uIAXRRnIlHT6uxki53wusB2mkSeSOnawD-GJdsfwnmuXNZMuWnPkGvf6PkK9uqYPUT4ldCLUWUSODJrO_BIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95c26614d.mp4?token=sR3B9uwtMDvzrgpq_jL1kSqo4unJUbii3cHwmSrg7kCyycS3AwgQfiEVYW9p2hGgH2Z7eGCTCIqU8FTZsMDeh_xbYuUThULvmY-OnzwuJN-3p3aJQg0W8EQL5VLlv01JuVewoaK8jMJ1fYZMWNguuOInopaF5onMANd66f2GPBzYIixP2KOBjFiYq8gVOKoMFG8Uskn5exsbh2De7BGgj9nAJLhpIDGWksvyvsy4yyl05tKe-QMQ22aggtPQXbzCNzsvK3M2YsAKHOULl3AFeuMAjXk1wbViq_j0m-CrTqTw96ssw_DiwhQGGlPKAwJmpEpneNPs8LwXZZv8Jv0iWyNJWgbmSmixg9X5KcSArBl40e_RVUlnvhDDTQmNGPTwDdwlW8ahv0asxoPSl71NXer_Aq03j3xmTBQogE5fKOFGCdH9ENiKPbB-rQ18SyZUuz-nHfzuI6M5teqR54C-7TEv4IvoPaVFRAOIJxiJ9_S9UuhdZrpmevO8Vb7uV6iT0nppFF982Pp6lJyg6N98NOgJVM6gZWsPhLio0KH3fxFu49EAJKEATRtWvS8YxjluXeDQts3X0pEShRg7JIJOyf8uIAXRRnIlHT6uxki53wusB2mkSeSOnawD-GJdsfwnmuXNZMuWnPkGvf6PkK9uqYPUT4ldCLUWUSODJrO_BIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در ۲۴ ساعت گذشته ۴ پایگاه در بحرین، ۵ پایگاه در کویت و ۲ پایگاه در اردن هدف حملات موشکی و پهپادی نیروهای مسلح کشورمان قرار گرفتند
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451608" target="_blank">📅 14:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451607">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f647aef9.mp4?token=JQ9H-tAOFF7Ig6i4mM4-Mgahzmf-qrOimvSYiYRpltFnL1-4weeu5CloV7aioAIEOToQlN5FZIkdlDWrobqJn9P9LBkgqA-k28fD9OFLDVr4SRKPqbODoBtNg0MleIQWmG2Y98JQE_5mAWs6saiw12IzS8-HzUulwZNSJEB6E4CzCH4CJkxuU4_vrGS02TRPkdZ5Z-sDLyqx4IngKaUkpo6VJlrPwpDc6cM0iGseNvTOPe3a8Lf7_VprEkiKw8k1Vokp7NO-UglctpL8UoX23Ry6P9UHajr9iDs4sHO6G2YLvSYAIpfLej3phjXyPF3HCE2kEB3YsQwX32UCd8Nuqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f647aef9.mp4?token=JQ9H-tAOFF7Ig6i4mM4-Mgahzmf-qrOimvSYiYRpltFnL1-4weeu5CloV7aioAIEOToQlN5FZIkdlDWrobqJn9P9LBkgqA-k28fD9OFLDVr4SRKPqbODoBtNg0MleIQWmG2Y98JQE_5mAWs6saiw12IzS8-HzUulwZNSJEB6E4CzCH4CJkxuU4_vrGS02TRPkdZ5Z-sDLyqx4IngKaUkpo6VJlrPwpDc6cM0iGseNvTOPe3a8Lf7_VprEkiKw8k1Vokp7NO-UglctpL8UoX23Ry6P9UHajr9iDs4sHO6G2YLvSYAIpfLej3phjXyPF3HCE2kEB3YsQwX32UCd8Nuqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برافراشته شدن پرچم ایران در بلندترین ارتفاع خلیج فارس
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451607" target="_blank">📅 14:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451606">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KI7owN-2aQCv8zOVfS3K8Tc6xtpMyxWM-4UYkU0A8lEPQh6qED7PrHdSn0vgWC8wlCH_E--hud9p6E8KfdyN4yxSwpYgBFHC6LCLMZoAul4n0p0z9ityd9tjsGGxvLVEB41E99eNLZ8IxVd6TzUXlCkE2GqzRJ_nEVCUxmUdb1kkTVd5bFhIZvApnkjD-6DROmAERNCSj79UKQPl2NXMxmx5PYC0GenJsfo-UxyLmXvnuYpN79SubRT7nQ17uAeN5W-GeKEfQ8n4Jg2V5-qk9SxOZgL8bNcqUb5unrU3tGO9sFnt_mfCYzuTgHlT6vRWUauGV6RUwu-2JpsGwsQlVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
منابع عربی: یک پهپاد به پایگاه نظامی آمریکایی حریر در اربیل اصابت کرد.  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451606" target="_blank">📅 14:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451605">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6945763e.mp4?token=WounplrBSfv_01RZ1MrXsHsIoBJbjeNiUJpdK_91GbsICiP7Q0SDK8dyh-8VTFDTdOzpgOgBs88RgWiuvAKvr6DcYP8btSMLxnYmX8O_D1egH26yBbNJ9H4f64gDxKiH1PBXRenfjp__rDNKwJni6xnJe2hEbR7jTwk6IYvb0E5wyuPhI2G5GPSCzdnSSytPjMc1uIuFqE4cXB7Uz6sZ20NxtUQwkiawaaLO_5MyWkYOTEfOtlGSf3FbTTTQc69oAh1Pbr__QJRq8cbpImCe68f79Qnzlma_otUCVPSMWhS4HzSU9sTWnLJGEq7GB-BaKic4rWKg7OO1snSc4FEm5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6945763e.mp4?token=WounplrBSfv_01RZ1MrXsHsIoBJbjeNiUJpdK_91GbsICiP7Q0SDK8dyh-8VTFDTdOzpgOgBs88RgWiuvAKvr6DcYP8btSMLxnYmX8O_D1egH26yBbNJ9H4f64gDxKiH1PBXRenfjp__rDNKwJni6xnJe2hEbR7jTwk6IYvb0E5wyuPhI2G5GPSCzdnSSytPjMc1uIuFqE4cXB7Uz6sZ20NxtUQwkiawaaLO_5MyWkYOTEfOtlGSf3FbTTTQc69oAh1Pbr__QJRq8cbpImCe68f79Qnzlma_otUCVPSMWhS4HzSU9sTWnLJGEq7GB-BaKic4rWKg7OO1snSc4FEm5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: به وزیر نیرو گفته‌ام، برق دولت را قطع کنید اما برق صنایع را قطع نکنید  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451605" target="_blank">📅 14:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451604">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e57c20be.mp4?token=ABAc7b6D-U4iBWPjXkRtiZ8G_gYJ9P8lubTdn9I_ZpdHAvovwEKj5HDCbrkjKRL_OuY9Bhc5SkmD6RnFqnVT54Pas4beT-2-uVNfjTvR_RqcQvJg7An6MU4THdJ5Yo8DYoRbiSKnaQ3e-2YUthP2c4QhItlCrmvEjBChoFKNp13hn1eRYm0Ny7PJxc9LBC3XUF6uVMsrJtaXvE3tBvXTUZuZOHvcBBcYZMqG0r82dtDxrIXSW2y2LgxGeM8IbhiFkqOywawVpUvL9Aw7uZYWlAqGxbucN0BDTyaJzTMFPAIPnM511B4uwR9ejk3kuiHcRmvJM9yhVVB_ScGmac_KrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e57c20be.mp4?token=ABAc7b6D-U4iBWPjXkRtiZ8G_gYJ9P8lubTdn9I_ZpdHAvovwEKj5HDCbrkjKRL_OuY9Bhc5SkmD6RnFqnVT54Pas4beT-2-uVNfjTvR_RqcQvJg7An6MU4THdJ5Yo8DYoRbiSKnaQ3e-2YUthP2c4QhItlCrmvEjBChoFKNp13hn1eRYm0Ny7PJxc9LBC3XUF6uVMsrJtaXvE3tBvXTUZuZOHvcBBcYZMqG0r82dtDxrIXSW2y2LgxGeM8IbhiFkqOywawVpUvL9Aw7uZYWlAqGxbucN0BDTyaJzTMFPAIPnM511B4uwR9ejk3kuiHcRmvJM9yhVVB_ScGmac_KrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: به وزیر نیرو گفته‌ام، برق دولت را قطع کنید اما برق صنایع را قطع نکنید
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451604" target="_blank">📅 14:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451603">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کویت: بازهم نیروگاه‌ها و آب‌شیرین‌‌کن‌ها‌ی ما هدف قرار گرفت
🔹
وزارت آب و برق کویت: شامگاه دیروز چند نیروگاه تولید برق و تأسیسات شیرین‌سازی آب کویت برای چهارمین روز متوالی هدف حمله قرار گرفت که منجر به وقوع آتش‌سوزی در بخشی از این تأسیسات شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451603" target="_blank">📅 14:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451601">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5nd_1AMM0RISdjArurDjTVH2DHJqM_XJO8SnYJ4d_y3GU0EgvZoHuir-cEolAQ6d5ReWFrC9EEMPRHqS-pLcgCW07ayeIRx_NuBWzt9DsRnrjBeeTDuVWlZzVF_Jh43g3JaRXdTTAm9FSVg5GNqaUK6Lk1R3eKXN235BOYiTGfrrUcWYL9tw__Mjtn72nkzkK5WGY--nvyZVTaVz5SemyGLhYL0_743qZG91OmtitoPez_v1T6R5ibQpwJaq_TWym39xeiZ-tgrNwuQ-15HNbOFJDMgNz1lqNfEDJqhInJhpC5h1NMHhl3NQdoGFyFHjP8jTpuHSAHdXLyAelMNyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hlJ2B_otTOwz7siFNq1969125CCCRb-HyanWwZ5-CNHHGE8sEdILrMfEHmwgo2Ki8LihiySTnfksgvzn8fechY7pyC0yLjH_KcAs-BFOHznQw85E8W-zJGrZntVJ9cTUAUtJto4phV4NaN-6lfRmS18qiEoMYXGyiFcyGm2736bCC0qyN0gkqWjdX8OUOE8DRurlJzMdLP4zNOoNUugXEu30JlASf3feimeMeQwzOnq2MR5XFgaz0PLWd_4KLgZsQObbLutp-PoatzsPg7wZ8uNriOYlVDXpzlzJljMllk74HNXX2orCXS7vA8-aFUEniP388kDFNpyW7EHj_98c2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
سپاه: تعدادی سرباز آمریکایی در منطقه‌ الرُکبان اردن به‌هلاکت رسیدند
🔹
روابط عمومی سپاه: ملت بصیر و همیشه در صحنه ایران اسلامی، با دعای خیر شما عملیات تنبیهی رزمندگان اسلام علیه دشمن آمریکایی با موفقیت ادامه دارد و در ادامه موج ۲۴ عملیات نصر۲ رزمندگان هوافضای…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451601" target="_blank">📅 14:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451600">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ادارات کرمان فردا تعطیل شدند
🔹
استانداری کرمان: با توجه به افزایش دمای هوا و با هدف پایداری شبکهٔ انرژی، کلیهٔ ادارات و موسسات دولتی، به‌استثنای مراکز امدادی، درمانی، خدماتی، نظامی و انتظامی و شعب منتخب بانک‌ها و بیمه‌ها، فردا تعطیل هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451600" target="_blank">📅 14:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451599">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZVeI73_ryzCXpEF_qcG6rXfaXEDZJ8-1QRvN2klUwEtqjAHxEZSwnOXaoKS4OjU7i-SO2VjMKNtj__h3agN5d8-QYei5UJkyBv5l0wsEV7R4-1wnE0WU71iMySoTX9xQ76n3RwqTAaYcZhoTGGiTT95bSwgfxi6nJZtGgKrWahF03ked0MmAb2eJwVRLRS1fhlxTXbOAlmKmLro_6YbPY4FBGX3osEtDQEltMqO3lfvJTpQkCyzFeb2Osv1rIzWvURVKmSpHNyE4S-nHI14T2IeMRCImKue1nNitTzAPKmI4YSKy2_pRHmv5msNTjR2-lu19Thy8KGwdcI2zVxJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکذیب وزارت نیرو دربارهٔ ادعای فرد منتسب به مشاور وزیر
🔹
وزارت نیرو درپی انتشار مطلبی در فضای مجازی دربارهٔ ادعای «مشاور وزیر نیرو» بودن یک فرد و طرح موضوعی دربارهٔ بی‌حجابی، اعلام کرد: این ادعا کاملاً بی‌اساس بوده و فرد مذکور هیچگونه سمت، مسئولیت یا ارتباطی با وزارت نیرو و وزیر نیرو ندارد و با جعل عنوان، اقدام به انتشار مطالب خلاف واقع کرده است که در مراجع قانونی قابل پیگیری خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/451599" target="_blank">📅 14:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451589">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QipHrTzw8Jesi3qGmRhj-tJk7d7zTEdm2ENXUwzMvG5SefBqbkGLA8eqgZVAj51I-YKRu7d488et766Y0bSXU6MtDykwDqWY8a7p4tw0vpzBJGfpUVSOY86HC6FywREC3Cm_3bgTJpE2R6tObKHnjim_zakTr0ciWPDkzS3E2ylIylMl-_3wVgihDB-rR5jZxxMTsNButD4sGZY0oAP3t7bJ9PewsVylyiU10__NJawKlx-0Hdv0cQd1ZnNkYRQoglWG8gQt5Sj_0Mfb8S08wXGlJz0K5uCyPgpnGdpBi1WVJZFi9jzMC_EQwXVRV2dxHO2TnWKNUixa__2XGtEb5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RL2zc0whJ7J378_50S8Qu7iOUTfuumQMFl5SmPvlR73p19LtMs6VnSE-CPe_H9F7hQnuqf1C-9isie1ptIOGYM0wKtivKBrjHJnAJFOKUz0zgFFvXCBrKZc6WKpsptNhLbwGobW45_sXCrm0bpgo2b267YQDRPsQ6MkINMhXU5gGf0sLwlR5Hn0VeE4tY-l5M5KWWMoXnS_ApM1-FitxFNHc1qi3-qWtojn9E9YVUy0sTz26gYLs9xWdO2uI8yJemzoHVWr4NRei9de6SUb3wUrNloYEyL6x-w634UfSwgZBvwlXX4y6kYAxL4JeG3bxRaJXxMyPV5wXJPFt9soSVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tL4sfmkOAhvQVW4BzEJvD2FPqHQm7M1uTk1LmlPCRS2OMtKwyPYUObx7rnhONGIS61gbPvEwMjdfsav4FUC113EBNCTBngrjZbvVTN86rcnS4v0x1SYPovihT4aJgBZKov17e3M95LzVbNXjeotmPPb6nDT3S4XMef_B-Y5lHN0gDudohs1bGp4fwvJVM6dPryuQKNIOkAYsEQTsqn8dKlT1KrvwY5PTtJCVcy6MiR-cNr-67zff-TCVN-cOcLqXdumn9w55zrrhR5EhRy37pnPytvFvlA9QJqyZk74Zs3U6J2A9RZrABgyGCOPmHyt-6kbV1LCgLrH1t0tH8rDwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ic23RBPpQDya3ho9OljMBxQXqg57tXqSh1VMFB5-a3sVIBUZ2mPmmmgWouQdKAnoYL5jfWy_icldfUAWA-wWTv2ymI5BV0YRkPVhwrF5dMFzyoeLbkf9lhd5WBCAMX4yIixpd6PJEF1ygyHWNSlmlZO__VYakS-E7IpouT1jQhbpxCoLt9A4N0izpRsItlMoULmW2HyA16FGvii-duoi53211rAvX78r0GQCRghgs7wH_s-AlQMP9CljUQpXOmONb_y5U40UEAwA6nw7qpeR46_ZN0y8jG-xJ2wS5fXIE9i5cauiZbRF9HFGIT_cdzZ6TdAwyzkCns6VltN6avswNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDwrTXssOFGn9ltg57J3UKW96r03qCykrvN9uvzh4Cnyepz9fLhP4rWStDgl8huN1h1K7RMbqGzAiJrozEpXTOOhAdp8S6PmCQhwstOz07O7GE-DtlwFwTQlwukTobkXYAjQmzIP0bn-nAtOU-BhmLKO8lRHvssHwrUPp25aSMOGQ1gFzAmyBpzorFdqtp12r7hY5-1dw18KFoOsAN5qyIJD2D6cEyMP3LMXH32UUifG_VSTTyFESlRSYgI9xsFOcKT2yuV0rcM2AJUL4mHgRY0aCauFzdaSj1S1-5RffsZ05jJkkatD2d9UbOfGrNIZzxn21qaIjPtKmkUf1RA7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOsevBoPRiH8ZBCAZCviAlc9ySLAIXQHvLV3U4HgHeDecDtXXFvjOlgXYAZY0aN5RptP5ik-36mZVOD24gagAGC3RnPZTLphuLOk049MHjkpuba3H8a0GFPP7bBkI4bDM95pV7yW6lSjsijfPyIPtF15-l4iiTeON5u-a2c5Nz3WninrNa9SNGWanl6AK8H0o_KCUMINS848mPsHegm0vSU8RzsKFVyraY5NiJDm6Z9-9qKfOMSKQUo7rUI4zNOKz9AWxXoDZpQwo1Vm2eR0Bdk3Bw5z3LPhT2T5LqDkRghWARVpyq3zJveizUDsqtbh3h3tl5ulDl3mUitYNG4vrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AH_fHFtxOtrhs5nj4YWr6cPFGCAd7hUYv7gViBPoZQI5rd8DL6c1gmbajxuiAbFLhEHdVLuZe-OBQRlPAic7Ni77E5kmp9dHW9T9yeKg3GD6Q3rMpWlfQ0bilfhk5iwi2qSkgx7pOxsfNTIaYg8zbWviqEZ1xrPc4CANhMsgn44YmborskvseWHPRHctPvQjp7Q0VsB-yFYzt4JI2_KHXuwIbXnP5uG--UUN2hbbXbs2Hp_3ef6USgT-0Rs3Gq9GehbKgHe5UG25vGbtEjdRVBAqVJAidYhyQAM_WnvGr_E9qyTriXuBQYyV5qTMmHJWJ47mRHCXZ1eSUZnIjK2n9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L9DgODrEM10IE8gW7qeVzU38z56FOSPKXD-btoWUpzqLi_Klf_06C6DD1nOUxFH2JedTUDUF58uERT7hxGT2O1G4bd2G3Z4FxRhzspg0RPgIGaDjMQzJxXMQt5OFCRQiiDO-NA0v5LoH80VKPPa6FNOhJotZAb1IzZJqs_xEtXiv0lzAJf5gGfJ54F1-bvdR_5hrdMZxGnwtxTVWNhi8-mVxJg-q-MUzJMy2pqtSSnF0Q0OUK1Wbc6KhUL5cexD79uxOYJ7MbbH8TARiuPWQessEeirS5aG266nJ_Qmc3K0xwt6XjcylOO_kmTinOTEJIyUCA7afQqGZMpjQJmL6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gt2tEstuUGPcsSRBnRyWzDRYdUmaAmZKdY8kOUcrruJzrNVZsPHEn5tzcMPGacGCcCyDFQm9doL1a0ZHf814UXuSO-_naX6dpCi-qS92RqauHWOckxxGVAPBgkhiFa66j_JqAWaIr1VbMfBACWe_hiOMfZ9HrTFMg7LIaC5s_Zu4FTVdEMhq2wWYuwqu8N1XFYwGpQAXSKgXyTMeyizjNmGFU_dk4dFn2c8d8UITIp1OpeWzxgU8YKKmqfNdpK15MjTJJVuJ8dAzg0eeX1-iwwakKHjqOzQpmugA7KVzu6NDTxQOmcveDCwK-Wbx2KbHs_LSAdcLtpaMGqUPkkllSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfL-jikLgR9L2rTmsEZQeCL--ufcz-aqMJbrPeg4Zr3EXR5yYqqMM73j29YEBDQbI1NgNKtlyumzSVBDLMZ_MBkiaaF8wWpKRzjhkUxhdyKY16Guvb8bHa8tbrJ7DU78iujh5V-oA-wyKax5G7G6pzmuaZ2vxA656ypHovB7WRa039sTq0N1gp6K_dEb7-VcNxaBax-dD4jHrGimysJzyOm1vw044vMnN3Gk8L6c_MQk_i_VWCBEgJBEk_Yz2I7TjyXAC6f1O3R5FtREcdNSNTxU5-lbaXX37Q78lq9htftb6wOmAjZ5IskMGwW5S66CkoMOYWXLVJV3xuMTmNI2sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار اعضای دفتر حفظ‌ونشر آثار رهبر شهید با خانوادۀ شهید سلامی
🔹
همزمان با ایام سالگرد شهادت شهید سلامی، حدادعادل همراه با اعضای دفتر حفظ و نشر آثار رهبر شهید انقلاب به مقام این شهید و خانواده‌اش ادای احترام کردند.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451589" target="_blank">📅 13:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451588">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فعال‌شدن آژیرهای هشدار در قطر
🔹
رسانه‌ها از به‌صدادرآمدن آژیرهای هشدار در قطر و همچنین صدای انفجارها در این کشور خبر دادند.
🔹
منابع خبری گزارش کردند که انفجارها پایگاه آمریکایی العدید در قطر را لرزانده است. برخی منابع همچنین از هدف‌قرارگرفتن کشتی‌های آمریکایی در نزدیکی سواحل قطر خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451588" target="_blank">📅 13:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451587">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjSWglgdl6_8ZAYamaBly516E_LtB_wzvloqMVO1ljT_4FqTFydMFTcstlKPQSSBd2UxMCXfvCDJOG85bzJGZxw9QaxIQEscMokPYgpzYJa_NX4ZIAkRtCgMefyu-DuBjQDbV2tIiON_NnzoRxXnWCSdH4koQmRH_0JgSlD9b-QxRpE6r_NRwgJpDqliZrUIwNSSGEMcqcSWrh8QTaSLKPd7ZQRcHOIZ5rMKRGPfgLx2SnFopYj19MSzisVnRq1X5-EkHTpEgfUE3DWcvpVxNlBg8K-r5CqtbuZy_IbJMcP_pLmIxoInSBk2J7VWzazLHmzd0SZThKcOgeTxLXyt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو حزب اعتماد ملی: نگاه اصلاحات به غرب باید اصلاح شود
🔹
مازیار بالایی: اصلاح‌طلبان باید مفروضات گذشتۀ خود را مورد بازخوانی قرار دهند و با توجه به تحولات داخلی و بین‌المللی تحلیل‌های خود را به‌روزرسانی کنند.
🔹
میان ساختار تصمیم‌گیری این جبهه و بدنۀ اجتماعی اصلاح‌طلبان فاصلۀ قابل توجهی وجود دارد؛ مسئله‌ای که بر کیفیت تصمیمات این جریان اثر گذاشته است.
🔹
تحولات مهمی همچون خروج آمریکا از برجام و جنگ ۱۲ روزه نشان داده نگاه این جریان به غرب و الگوهای گذشته نیازمند اصلاح اساسی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451587" target="_blank">📅 13:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451586">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9KDlIR96j2QTHcFgsfzFx-MBB0Pj__0ty8aS7xavdmmMiOpMrGY17PqQybPRMhvL0kL9zWYOFA2GbtJUQXG4FtqrsQP8RFZvR_mHNUCcwAk4Pyyv_YnqBfobtV4oWLK2YSDETPIB6P2bF7KgULjLmj044OWoZs4mMbpDknEkjTK5hFciaiAOVabbDMxSGUItzr_G4nBYO3YCeAQimXr2baF4XKQn5bUllx3hTiFkKRfXc5xFyn1fc1uVMgCYXIzVMGwf9SYXax7m4XlbyU2KpRib9VpXYXcUe3x6sSzPKdJS8TbvZLk9iVKLCGb-UaKFQX9Cgntie1YASf-EGXvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف پل حافظ تهران منتفی شد
🔹
نیم‌قرن پیش پل حافظ در تقاطع خیابان حافظ‌ـ‌طالقانی ساخته شد و قرار بود چند سالی به‌عنوان سازه موقت باشد. از ۲ سال پیش ماجرای حذف این پل کلید خورد.
🔹
اما رئیس کمیتهٔ حمل‌ونقل شورای‌شهر تهران امروز گفت که هزینهٔ احداث زیر گذر به‌جای…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451586" target="_blank">📅 13:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451585">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای هشدار به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451585" target="_blank">📅 13:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451584">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای هشدار به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451584" target="_blank">📅 13:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451583">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRCoq4ClzK7enD08y4PGYTJRdUi8v7W1Pn7Xd7WhRppXLBKtEW9mqF3O6Zk7nbIkE0nQFxgemxuw0pgEMcZw4V7RZOHwRnQHWtggeY96FNZ2r4YYDh6oYKBN-QJeJNTCGdEQeGgCnrh_JOVcPIw8QjSLifyrgyUIv3qhx_qgZSaNFimn1XhlZh3Rnb5ECjiZbLqvGg7djW9YuIGGAmMK5mPOhVWAErPegFTAInCo8DlxlsA3QYKITenCg981R8g7AX9CABsx_SdV080oPqzZxOijqYgWEOAoqFr-jJ9zWUv3lw987uF9G3nv1e8n8XiI-SA0BVd1NucuX7DeiRDYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با جهش ۷۴ هزار واحدی به ۴ میلیون و ۸۸۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/451583" target="_blank">📅 12:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451582">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiiYRbng3NaHiAC-GG1EIbVq87xsKuxFOU__MSXy71tY6_0Td1HQZ_CKBxCCmpban3lg7LAL4rJZDrNpWAel4hWWy3fMqioWeDsUBzXJ8zGnR-TjOotzRnPDEAfZXdrpcU5ig8Ksc500eZb6IN29_JD0piys6G2tdlc1qPa-jhMJpVOUTlmdI39Xq8PtgYtjdakx3XGp5YkqCIDQeAKOXmKNTiJddc5tPTeZ7YpAkgCuiUtwp_KsCgfGFgLitY8hR9grf8mUyS2tbk_iMLT2JsSBDLO57pja10FJcApTfGTFVVLbIxlWWoAKai2VmDifRCmL50JB_p-W9YRwr6jS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازدید فرمانده نیروی زمینی سپاه از یگان‌های عملیاتی در خلیج فارس
🔹
سردار کرمی در ادامهٔ بازدیدهای میدانی از مناطق ساحلی و جزایر راهبردی خلیج فارس، از یگان‌های عملیاتی تحت‌کنترل «قرارگاه مقدم مدینهٔ منوره» سرکشی و وضعیت عملیاتی یگان‌ها و سطح آمادگی رزمی رزمندگان را بررسی کرد.
🔹
سردار کرمی با اشاره به جایگاه حساس این مناطق در راهبرد دفاعی کشور گفت: آمادگی مستمر، آموزش‌های تخصصی و حضور مقتدرانه یگان‌های نیروی زمینی سپاه، رکن اصلی امنیت پایدار در پهنه آبی خلیج فارس است. رزمندگان سلحشور این خطه با تکیه بر روحیهٔ جهادی و هوشیاری دائمی، سدی مستحکم در برابر طمع‌ورزی دشمنان ایجاد کرده‌اند.
🔹
به‌فضل و عنایت الهی، مردم و نیروهای مسلح آمادگی پاسخ‌گویی به هرگونه شرارت از سوی ارتش متجاوز را دارند و انتقام خون قائد شهید امت و فرماندهان شهید نیز به‌زودی گرفته خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451582" target="_blank">📅 12:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451581">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار و اصابت موشک در نزدیکی شهر الازرق اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451581" target="_blank">📅 12:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451580">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a53d40f85.mp4?token=gBFBV8tPoff-YYzzN92p0yAOFTrPA5NP-hJa0Cr0Y0ycQXUSYkNb4x--lBlzBu6aqKOPIwu9rVyZ7wAVqdwsKJyQTJNUtSg2bAoU1gZ8Gu5q3hwS8NhheEiKSxzBPPqTnSgwJQvfPgJZqfdhro-OD0PMp-5CDjQN_78WrgWfauNsuiqIEmIfMt8AiQj1D_jUAVzPidl1iQLuSSj6nBNbYPI05D8b14JaNUzt2NZaxfakzJLh1mtoZ1HmQi1uAQxQwWZBzva5jD7Qyw4jAbNwCtJrlGA7prUNN5rMoP_QY4o_ncTBNbwDNNcpmFWrHVoxTUBeO2KRw5U68U5H9KWo34cfgDao9at29oChbl65bX6P5AaNIO1ln_cTo5NiweZlLJdIDi6T8KqA_h8blWBaHkzQI6Y-p8Dcp27a0zWORne6Jm58Z_UKnKvb0YAytIMjO5CcLq4yQgm52j_9iZ44alb5z85WwKer0KrRpF2PdSXy-2C5aifqffqqX9jHogqttuPUgDPw1CBdrKvcsoVXrgGsxa6y2R8QrOvpvX26yOH2KppiC8DrHCjo5PVJUHNU2wZrbA2dcGU8XqOaLxwqyryoN_9_SpPPnuWP-HOzqtY3bOp9dkXZ5KScEUiCQ7wH69GMP0Epait-Wu92ECHF3MR_1EaR8dAkEJLiJjJiwrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a53d40f85.mp4?token=gBFBV8tPoff-YYzzN92p0yAOFTrPA5NP-hJa0Cr0Y0ycQXUSYkNb4x--lBlzBu6aqKOPIwu9rVyZ7wAVqdwsKJyQTJNUtSg2bAoU1gZ8Gu5q3hwS8NhheEiKSxzBPPqTnSgwJQvfPgJZqfdhro-OD0PMp-5CDjQN_78WrgWfauNsuiqIEmIfMt8AiQj1D_jUAVzPidl1iQLuSSj6nBNbYPI05D8b14JaNUzt2NZaxfakzJLh1mtoZ1HmQi1uAQxQwWZBzva5jD7Qyw4jAbNwCtJrlGA7prUNN5rMoP_QY4o_ncTBNbwDNNcpmFWrHVoxTUBeO2KRw5U68U5H9KWo34cfgDao9at29oChbl65bX6P5AaNIO1ln_cTo5NiweZlLJdIDi6T8KqA_h8blWBaHkzQI6Y-p8Dcp27a0zWORne6Jm58Z_UKnKvb0YAytIMjO5CcLq4yQgm52j_9iZ44alb5z85WwKer0KrRpF2PdSXy-2C5aifqffqqX9jHogqttuPUgDPw1CBdrKvcsoVXrgGsxa6y2R8QrOvpvX26yOH2KppiC8DrHCjo5PVJUHNU2wZrbA2dcGU8XqOaLxwqyryoN_9_SpPPnuWP-HOzqtY3bOp9dkXZ5KScEUiCQ7wH69GMP0Epait-Wu92ECHF3MR_1EaR8dAkEJLiJjJiwrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کادر درمان پای کار جنوب ایران هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451580" target="_blank">📅 12:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451579">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxrkt8PHu_hDDS-zelS28FJjLOZzJdB0UdxZehHbkjw3RLNHpxlPxjTlaRdw_yoOsa2gv5f1oml1JSkNibYNx-A1sDYjSh0oSCXsGTdd9Kwn8eG8R-M-Jk4DqlZOmCfycpCXa2an9rDrT3xBRdr7omEnLyGAJli7vPCKsApCCtKkyEz5elAHeok0KsaVNXXlwp2XHt64x8hePOcGT_WTZlBCh65Ms5rBeET3Og3r0rdAf5P9qKhmnhiVb-8oMchtYa2lUdDSd-8i68pwCECWNF1aF259qIrNDaSixItnBt2Tl6ro-zoVOd5-sfuq_mBUqYK6_9_WJSJn5zHe-lUlkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
۱۴ میلیون و ۸۰۰ هزار نفر با مترو</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451579" target="_blank">📅 11:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451578">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XURPvQ-jGwVbroIg3oQ_HkdC4sQbOAtLEYy7lOhEjQIxj8qyCzjeaFO01WK1Y7hwMNP2Cynz2HYapbjwUUKbZy8yjteS68eaua1sZuXNRoyFDSD2TeEQEfBpCj3-qmrpZZvU_5D4rlhhXenZGJiJao6QKJ-px60sVVgGdcXlxdDDyzbSOYme1d7_HuX95w20GlZZvM2lt2M7SCA6a4T3wt5jO-R0xCUBR8bktzj_EQUkAfYkmuT-8m1Q-zaRCnJuyOIW9ZpOc59vHdBcW8FTcLjdZKI5OQt7xK0Mee6pNLojAdvBJ6s-bYyJNZA_U48_LR7r6mJUnRL_ELgCADVUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بهرام گودرزی مدافع ۲۱ سالۀ فصل پیش آلومینیوم با قراردادی ۵ ساله به استقلال پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451578" target="_blank">📅 11:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451577">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL9x5w3mdAX6rdLuxvJt09I8qD-anh16SmhVYvGzKK7nvHZwiXLdzsUa15hbSqYJ63eMzv2WYBDWsWJ1GhmjJ7zVGt0-vu6PETsfwODfFJS2HxiKWjAE84wD1NNCwop6Gnq2Z8fLRdCdWuAiV5TlcgjtmWOhiZV16m0uFPe94ypA5nEIYJVDQnzhl9r0xykUj3ywSTH-aCW-Wjwd-U3KaxeGReAnXNrILSmwF8v6-2cTkrSE-DAGrlu6U8VJ8UplcLCc238_X71G_N8zq8tBVBb-Liy7jR9OH9wP7ZWO5i90YLgVHiBLs0PhnxrdQsSzzu88IdKCNq-iaEWVA7BUlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حمله به یک کشتی در تنگهٔ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس گزارش کرد: یک کشتی در ۱۷ مایلی دبای امارات هدف اصابت یک پرتابهٔ ناشناخته قرار گرفته و سیستم هدایت آن از کار افتاده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451577" target="_blank">📅 11:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451576">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208cb5a281.mp4?token=ErNe3LjrPtjYEoRWRqb12daagWwmI3RPr7QxnpytV5s7XpTHhieK2neE_SmsP0c9DtXUKPea7aXyNGCkA2R0zTw7SVTMq5LGlPqh8cLlZx03kxwpZrLTMwUf0QJwinEdQTFlF0BUONPEANp1YPt2es5G-Z-GnV6xP3CGRh7OdgbUuQAQBh2190in2AEX7Yg93udQRwC436CJpKV-IPfuRXRkPzl9vZmpuHYGm-wConuD_uzwgmdxFvnqoSJ8YozzkXfbYmF5QXmeChkap9xrIT2spdDh0KO45sVdGxgkyrcq8IZwdNM9Minbzy6Sy84hJFE1bh5HLR9LdddR_BmmBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208cb5a281.mp4?token=ErNe3LjrPtjYEoRWRqb12daagWwmI3RPr7QxnpytV5s7XpTHhieK2neE_SmsP0c9DtXUKPea7aXyNGCkA2R0zTw7SVTMq5LGlPqh8cLlZx03kxwpZrLTMwUf0QJwinEdQTFlF0BUONPEANp1YPt2es5G-Z-GnV6xP3CGRh7OdgbUuQAQBh2190in2AEX7Yg93udQRwC436CJpKV-IPfuRXRkPzl9vZmpuHYGm-wConuD_uzwgmdxFvnqoSJ8YozzkXfbYmF5QXmeChkap9xrIT2spdDh0KO45sVdGxgkyrcq8IZwdNM9Minbzy6Sy84hJFE1bh5HLR9LdddR_BmmBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: تعدادی سرباز آمریکایی در منطقه‌ الرُکبان اردن به‌هلاکت رسیدند
🔹
روابط عمومی سپاه: ملت بصیر و همیشه در صحنه ایران اسلامی، با دعای خیر شما عملیات تنبیهی رزمندگان اسلام علیه دشمن آمریکایی با موفقیت ادامه دارد و در ادامه موج ۲۴ عملیات نصر۲ رزمندگان هوافضای…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/451576" target="_blank">📅 11:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451575">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVI7SHaX6n3GIFUzeHWhmpHzvoR_fWwBJoB0pOvdT8VNLC__WEKsyEh7hrNCoOK89RRHpqcwgj2gCOMtq7wy2OXpubETN1BOjnKUNS8U4Yfwnd2Jx-HuLvbzzsWWyiRnjdnxMv_7xJbGyhd3XmgpcoB0Q2temPAsOj4vCkj0RCVXbTy8iemjj78wJmXC7MhxYGTcKk1tKdMgK3HDCjf_3x_E_kjTM7EACn_38v9ouTi5_4pSLfZvihrIU6TO7X6cp4VoJJOFh0wTUwU-lzGT-cu5lmNlD8kTKJXYRNIe0hFqFhKunVVZ47CMaxSa7OI5XbuOjgqFNEoeR3DA2it7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت و نان عربستان در حلقهٔ محاصرهٔ یمن
🔹
نیروهای مسلح یمن با اعلام محاصرهٔ دریایی عربستان در تنگهٔ باب‌المندب، مسیر جایگزین صادرات نفت این کشور را هدف قرار دادند.
🔹
عربستان که برای دورزدن تنگهٔ هرمز، بخش عمدهٔ صادرات نفت خود را از طریق خط لولهٔ شرق–غرب و بندر ینبع به دریای سرخ منتقل کرده بود، اکنون با تهدید جدی این مسیر روبه‌رو شده است.
🔹
کارشناسان می‌گویند در صورت تداوم این وضعیت، عربستان برای حفظ مشتریان آسیایی ناچار به ارائهٔ تخفیف در فروش نفت خواهد شد؛ موضوعی که می‌تواند سالانه ۳ تا ۴ میلیارد دلار از درآمدهای نفتی این کشور را کاهش دهد.
🔹
همچنین اختلال در این آب‌راه می‌تواند هزینهٔ حمل‌ونقل و بیمه را افزایش داده و قیمت مواد غذایی، دارو و سایر کالاهای وارداتی را در عربستان به‌طور قابل‌توجهی بالا ببرد.
🔹
طبق برآوردها، در صورت دور زدن باب‌المندب، زمان سفر نفتکش‌های سعودی به بازارهای آسیایی از ۲۴ روز به ۵۴ روز افزایش می‌یابد؛ اتفاقی که هزینهٔ حمل، مصرف سوخت و بیمه را به‌شدت افزایش داده و موقعیت صادراتی عربستان را تضعیف می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451575" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451574">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbc6a1ed87.mp4?token=rFivLev8G1h3_Ng6JvKlTp1De0AusohR4Nwfgv23GfUQYEEJRPFK8-YYpKyjCswTZCJpIC7Wqlf_e-MKCQlnJPbDpAi51Yd_D8_ddJ7P_2Nq7Puorz3YKiEizlWSSy67ZOoxT_-gl_q0JG5AUUOrjId8s-G_cMjED1RFnwjlc-jG2bEeW9AWtCE4k6IHg4ihMw4YqhFQn2SZTkbGuXkJKXZzEo8D_RpFJi6UTKUCSQ03gAV-f2iVnDS4G_Gh0HgCUYybY0H-x0h_cj7r8hSiE3VmeEVzUGJNEe_XQaYdSwvJE9VmWQw48V-ZmdMq1ukRXNaetLqEavShpN8wm-3Kgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbc6a1ed87.mp4?token=rFivLev8G1h3_Ng6JvKlTp1De0AusohR4Nwfgv23GfUQYEEJRPFK8-YYpKyjCswTZCJpIC7Wqlf_e-MKCQlnJPbDpAi51Yd_D8_ddJ7P_2Nq7Puorz3YKiEizlWSSy67ZOoxT_-gl_q0JG5AUUOrjId8s-G_cMjED1RFnwjlc-jG2bEeW9AWtCE4k6IHg4ihMw4YqhFQn2SZTkbGuXkJKXZzEo8D_RpFJi6UTKUCSQ03gAV-f2iVnDS4G_Gh0HgCUYybY0H-x0h_cj7r8hSiE3VmeEVzUGJNEe_XQaYdSwvJE9VmWQw48V-ZmdMq1ukRXNaetLqEavShpN8wm-3Kgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایگاه شیخ عیسی آماج حملات پهپادی ارتش
شد
🔹
ارتش: از بامداد امروز و در مرحلهٔ بیستم عملیات صاعقه، پهپادهای انهدامی آرش در چند مرحله محل اسکان و استقرار نیروهای ارتش تروریستی آمریکا در پایگاه شیخ عیسی بحرین را آماج حملات خود قرار دادند.
🔹
پایگاه شیخ عیسی از کلیدی‌ترین تاسیسات ناوگان پنجم نیروی دریایی آمریکا و مرکز عملیات ارتش متجاوز این کشور است که عملیات هوایی و کنترل پهپادها از این پایگاه هدایت می شوند.
🔹
عملیات‌های تهاجمی تا بازداشتن دشمن از ادامهٔ تجاوز به کشور با قدرت ادامه خواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/451574" target="_blank">📅 10:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451573">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZN1Lc1KDW7hzOLK2MBYg6AvACNTHdycZs-Eah2ycza1J5MmaiEBis3uicdyG_K7sj8FC0kf3moc_NvYIO9e8qxxT0uAkgnx1I3Ubrnu_bhH9tFPfCz-T8dx4VUmoZk3ZqYDMly1mX4J_XzFusRpHySfu52uy3fbrhxIJe-kIMCJ1QapA0pp2Yewp6Cxy5100kuXnGokLMwBjJ_G9FYVbyW2ZfWPWyZpmJmSMtJYk5y9RYEpJ6TD7OiHAPZOLgww8ZacBqjxtQOeX_RML_4np2EEivkbSqXrGAsEbMpJ4vH3yvewKFgTzov5z13BWBEhF844OEvUICWbMkbS7leCogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعلام کد اضطراری توسط سوخت‌رسان آمریکایی بر فراز خلیج فارس
🔹
یک فروند سوخت‌رسان نیروی هوایی آمریکا که از پایگاه هوایی الظفرهٔ امارات برخاسته بود، بر فراز خلیج فارس و در نزدیکی حریم هوایی ایران کد اضطراری ۷۷۰۰ اعلام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/451573" target="_blank">📅 10:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451572">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌  شورای نگهبان با برگزاری مجازی جلسات مجلس موافقت کرد
🔹
سخنگوی شورای نگهبان اعلام کرد مصوبۀ اصلاح آیین‌نامه داخلی مجلس دربارۀ برگزاری جلسات در شرایط اضطراری، مغایر شرع و قانون اساسی شناخته نشد.
🔹
براساس این مصوبه، اگر به تشخیص هیئت‌رئیسه، برگزاری جلسات در…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451572" target="_blank">📅 10:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451571">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01a320bc1.mp4?token=XHVSY4y1FlMUkINyueW5fUVgB_vxDLHgkvJdfJR0nM9_znj-QCMNXUi3Klokgh67jLlnSd3Hal2S8kPsNp5shd30Fv8KXfb1owJEJMjOQQLUH4OZ2aIJVJH3pWGnUtGxjybbz4_VQ3CSHMoYbHekCTn24ZEV9UBYgbtqKakojQSI1tD_kv-KKQXepl9S1m0AeypytW8_M_GHtZegXG00u9_F_SD8y02q9tb_hX84_gngGi4pxI4geAsMr4KYiSxjOVBetQDfPENwbMMt9K9bRzTqfTTqVyxmZm7NfvDTGqK4nQKpwy8cpyyMFHHwrYS0IAQHWptL_Tw1N2sVpmLI2IwumcXNRTLHYo_q_o6XVmbAu2hFconX28vUXamMqkxBCJFPBNQBO3q7AD084Xn2Bs_t5y2Z2fFcte9tzeHxyDJ4exQfCCrFdnjahzqurKw3I4XrrZoSGFvGvbFrz5Y4kSaB_vrt2vFy1Y6D6zBUX94AYGvdHMjYw6gkFwoaVnlOoraXllpbSjVmdnb0AaLNfzRy5iYDvFx8qF7Tvv5_52ekGv9FF5GEWg7EWyjDmxyWCnpOrG1WxWAU4CEtfXaPdl70Uuj2uLmWjsH-j0FIN-NHQbrqNOLlHPMS4zQyPwiPWlRmW_EpswfmrQ6a3wnlJ-L799xrIFirYKSIbh2Na9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01a320bc1.mp4?token=XHVSY4y1FlMUkINyueW5fUVgB_vxDLHgkvJdfJR0nM9_znj-QCMNXUi3Klokgh67jLlnSd3Hal2S8kPsNp5shd30Fv8KXfb1owJEJMjOQQLUH4OZ2aIJVJH3pWGnUtGxjybbz4_VQ3CSHMoYbHekCTn24ZEV9UBYgbtqKakojQSI1tD_kv-KKQXepl9S1m0AeypytW8_M_GHtZegXG00u9_F_SD8y02q9tb_hX84_gngGi4pxI4geAsMr4KYiSxjOVBetQDfPENwbMMt9K9bRzTqfTTqVyxmZm7NfvDTGqK4nQKpwy8cpyyMFHHwrYS0IAQHWptL_Tw1N2sVpmLI2IwumcXNRTLHYo_q_o6XVmbAu2hFconX28vUXamMqkxBCJFPBNQBO3q7AD084Xn2Bs_t5y2Z2fFcte9tzeHxyDJ4exQfCCrFdnjahzqurKw3I4XrrZoSGFvGvbFrz5Y4kSaB_vrt2vFy1Y6D6zBUX94AYGvdHMjYw6gkFwoaVnlOoraXllpbSjVmdnb0AaLNfzRy5iYDvFx8qF7Tvv5_52ekGv9FF5GEWg7EWyjDmxyWCnpOrG1WxWAU4CEtfXaPdl70Uuj2uLmWjsH-j0FIN-NHQbrqNOLlHPMS4zQyPwiPWlRmW_EpswfmrQ6a3wnlJ-L799xrIFirYKSIbh2Na9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهره برداری از ۳.۵ کیلومتر دیگر از بزرگراه جلفا- مرند
به همت سازمان منطقه آزاد ارس و با مشارکت اداره کل راه و شهرسازی آذربایجان شرقی ۳.۵ کیلومتر دیگر از بزرگراه جلفا- مرند به بهره برداری رسید و بدون تشریفات خاصی افتتاح و زیر بار ترافیک رفت.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451571" target="_blank">📅 10:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451570">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q96xtvyFeOJVmtALCeeSUrs5rhQz0vG8DmFO-3tEPpswvbtbFn-OgKT5pZjGyQLi8eeMEFjY6bWI_N9duYMSYicvVub7dyQsxIqYmet66bMgxLCTK_YXXU8LrvHEEN_tP1Q2BTXiGXKKaL5Xg4EwTPpjqYj66nUflvDI75gTHyCMZ564-w7DGkkPvfXNt1fI7O24xvTIo1TCjv5FkGMi8MicnWHWHaXGznKT-yPHdmqLS9JpMA-spfBE9Ue270VU5EpuzX8owh7y-ELYGwN2uwvx7_7Jw6odyMJ9s2SfgPItpST3Pa7EAvQsjqc8GNGBiyMtVh71ChZbIEmY8RCw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیریت هوشمند پرسنل با راهکارهای جامع  کسرا
شرکت دانش‌بنیان کسرا با بیش از 26 سال سابقه درخشان و بیش از ۳۰۰۰ مشتری، ارائه دهنده نرم‌افزارهای تخصصی مدیریت منابع انسانی:
🔹
حضور و غیاب:
قابلیت شیفت‌های پیچیده، قوانین اختصاصی، گزارش‌ساز ‌
🔹
تغذیه و رستوران:
رزرو و توزیع آفلاین و آنلاین غذا
🔹
حراست و انتظامات:
مدیریت ورود و خروج کالا، خودرو و مهمان
🔹
مدیریت پیام:
اطلاع رسانی سازمانی
🔹
ماموریت و مرخصی:
محاسبه هوشمند مأموریت و مرخصی
🔹
کارانه و پاداش:
مدیریت پاداش، کارانه و اضافه‌کاری تشویقی
🔹
ناوگان:
مدیریت سرویس‌های ایاب‌وذهاب و حمل‌ونقل سازمانی
مشاوره و دمو رایگان:
🌐
kasraco.net
☎️
021-41452000
#کسرا
#مدیریت_سازمانی
#مدیریت_هوشمند_پرسنل
#مدیریت_منابع_انسانی
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451570" target="_blank">📅 10:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451569">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451569" target="_blank">📅 10:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451568">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4KL87HJIw45_JLd_b9lmswwjH4jDXhRLlH09mnJgSu_hNInZu7QNSTc5JCiFQNe9N682uAynSVnfuhMc0aQt6TZMYprwlPvsjLSCARfuwBxsgLYM1U-6JiJCQBnobdLmy8Ck49ziMYpU3thsgVcKGk7nr_pyHck_7UGHC1lhV2k1atsWCrhmlTRWiQC4dCbzt3S3sEnemCA94DRatqQ0DpDk3a2ZhUBot7D-TdEgG5bpXLBBIDEGRIkS0SZ1HQpYNO5MtL33FMbApY4xCYyZeiku5hUnO1cwDFg4XRA4OdfS_J3qTLAfel59IHtUblK8cRmBui1mOnT1gaRObj-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای اسرائیل درباره انتقال هزاران سانتریفیوژ ایران به اعماق کوه کلنگ
🔹
روزنامه وال‌استریت ژورنال گزارش داد که دستگاه اطلاعاتی اسرائیل ارزیابی کرده که ایران هزاران سانتریفیوژ غنی‌سازی اورانیوم را به کوه کلنگ منتقل کرده که هدف قرار دادن این تجهیزات در حملات هوایی را دشوارتر می‌کند.
🔹
به تحلیل این رسانه آمریکایی، رسیدن به چنین عمقی، حتی برای پیشرفته‌ترین بمب‌های سنگرشکن موجود در زرادخانه آمریکا هم مأموریتی بسیار دشوار محسوب می‌شود. با این حال، همین مصونیت، آن را به یکی از اهداف اصلی آمریکا تبدیل کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451568" target="_blank">📅 10:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451567">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWbp3NCe3eWK33zyptYT8ulJXgEXOXrphAOliP7cKVNnxeFzwo3f_ZiC0VMoFjZn81iEucjR2J2KOJqKefRDeMCHceN0ZPvKt82DAYcIYJsw1XLxKQ868H80SvWiqdWAkolSTMb-XYzfBVQZYyi342ZTfsDmMFKCkbJs5QdpHa_8jcEon4fgSr4oEP_ATNohqXHb7HSDduOI0qFodjv1voNH2NpKzk9xO4k3MYfFQIfDQS27Ql9SrpDuODsWwzPLpeXd_gjgHs-2zwfTg9b3OWL9Uia8YqUR5sZhIrNYA7Z9qCF7KwKRWLEirKs4eNNkhz5FoIioQ-WeA2TEWirDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعزام ۵۰۰ تیم درمانی سیار در مسیر پیاده روی اربعین
🔹
رئیس سازمان بسیج جامعۀ پزشکی: ۵۰۰ نفر در قالب تیم‌های دو نفره با تجهیزات کامل و به صورت پیاده در مسیر راهپیمایی اربعین حضور دارند تا در صورت بروز هرگونه نیاز درمانی، اقدامات لازم را برای زائران انجام دهند.…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451567" target="_blank">📅 09:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451565">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74b25a7be.mp4?token=SxV2gMk-n5d2NwTe3p8ZeFHGRcbjHLuWwJ0bCOaDPXYvemuXK5yjIEBcO2ubcyHLWRhVeyONTNrj-d8DTKg4fyQysHPzdL8oEsTpfj1A61XQVWqs3kWH6doPw4KUcMTGnyC4IhoQexmD8Biz-8-2t5bmprIHkRXTvh1UwB7U4fzvsGdhzNEbwQ_-E9kYn69nDZsLo0iAt8OXZwOsFoZ_RZyyRl9fxkJUocpC3jaQst7sFSQpdhsaJ-q2J3JgP0EctUJ6P8dnYS-Z35p648B8Zb8bgPxfoA8xP-d7URb4HIuvw_zD47xZToGj16va-YIxxHq5jGnAD1oj81fFkECTMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74b25a7be.mp4?token=SxV2gMk-n5d2NwTe3p8ZeFHGRcbjHLuWwJ0bCOaDPXYvemuXK5yjIEBcO2ubcyHLWRhVeyONTNrj-d8DTKg4fyQysHPzdL8oEsTpfj1A61XQVWqs3kWH6doPw4KUcMTGnyC4IhoQexmD8Biz-8-2t5bmprIHkRXTvh1UwB7U4fzvsGdhzNEbwQ_-E9kYn69nDZsLo0iAt8OXZwOsFoZ_RZyyRl9fxkJUocpC3jaQst7sFSQpdhsaJ-q2J3JgP0EctUJ6P8dnYS-Z35p648B8Zb8bgPxfoA8xP-d7URb4HIuvw_zD47xZToGj16va-YIxxHq5jGnAD1oj81fFkECTMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسپانیایی‌ها از خجالت پرچم رژیم صهیونیستی درآمدند
🔹
مردم اسپانیا در جشن شادی به‌خاطر فتح جام جهانی، پرچم رژیم صهیونیستی را زیرپا گذاشتند تا بار دیگر نفرت خود را از نسل‌کشی رژیم اشغالگر در غزه به دنیا نشان دهند.
🔹
هواداران اسپانیا همچنین با برافراشتن پرچم فلسطین به دنیا نشان دادند که در کنار انسانیت ایستاده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451565" target="_blank">📅 09:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451564">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShyEni06X_rwGOnJ3UlaVdi3nR03J1tBCTAf0JBVcS2q9NhIxn1onytSbffF6_Ikl3RYnJ2RnI_Re7TG7LL9T0Z5eWN5MYtf_CZPK2f8Sk5jGGd_XRAXSdFsi1wUTzbwLg5myPvaIXoXv92OO7uTO1GM-jAewgYdau8oVFo9RuXirAE4Sm9gg9JF1jAFW7VubTD3LKFx5OKYodC1Zl1I7rGzXJ1Du15UBf625BdWwMU3uirfjlkIYQNOzZeUa7rteabCZjCe6MTJo-N8JMMLCc2xXgeK8f9-oFAGCfEVczwTzTCxi21EJUsx4qEF-7mw0OgdRfU5OYOn7DBhke-22Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منبع نظامی: تنگهٔ هرمز همچنان مسدود است
🔹
یک منبع نظامی در گفت‌وگو با فارس: تا زمانی که اقدامات خصمانهٔ آمریکا ادامه دارد، وضعیت تنگهٔ هرمز تغییری نخواهد کرد و هیچ مجوزی برای عبور شناورها از این گذرگاه راهبردی صادر نمی‌شود.
🔹
کنترل کامل تنگهٔ هرمز در اختیار نیروهای مسلح ایران قرار دارد؛ هرگونه تصمیم دربارهٔ بازگشایی یا تداوم محدودیت‌های این گذرگاه، صرفاً براساس ملاحظات امنیتی و منافع ملی اتخاذ می‌شود و تا زمانی که تهدیدات و اقدامات خصمانه آمریکا ادامه داشته باشد، تغییری در این وضعیت ایجاد نخواهد شد.
🔹
مسئولیت هرگونه اختلال در امنیت کشتیرانی و تبعات ناشی از آن، متوجه طرف‌هایی است که با اقدامات نظامی و سیاست‌های تنش‌زا، امنیت منطقه را به مخاطره انداخته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451564" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451563">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امام‌جمعهٔ اهل‌سنت میرجاوهٔ سیستان‌وبلوچستان به شهادت رسید
🔹
سحرگاه امروز «محمد انور ریگی» امام‌جمعهٔ مسجد علی‌بن ابی‌طالب(ع) شهر میرجاوه در استان سیستان‌وبلوچستان توسط افراد ناشناس هدف سوءقصد قرار گرفت و به شهادت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451563" target="_blank">📅 09:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451561">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در اصفهان
🔹
استانداری اصفهان: احتمال شنیدن صدای انفجار کنترل‌شدهٔ ناشی از انهدام مهمات عمل‌نکرده در جنوب و غرب اصفهان، بهارستان و صفه و ابریشم تا بعدازظهر امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451561" target="_blank">📅 09:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451560">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
سپاه: تعدادی سرباز آمریکایی در منطقه‌ الرُکبان اردن به‌هلاکت رسیدند
🔹
روابط عمومی سپاه: ملت بصیر و همیشه در صحنه ایران اسلامی، با دعای خیر شما عملیات تنبیهی رزمندگان اسلام علیه دشمن آمریکایی با موفقیت ادامه دارد و در ادامه موج ۲۴ عملیات نصر۲ رزمندگان هوافضای سپاه با حمله به یک مجتمع محل استقرار نیروهای ارتش تروریست و کودک‌کش آمریکا در منطقه‌ الرُکبان اردن تعدادی از آنان را به هلاکت رساندند.
🔹
وزیر جنگ آمریکا که خود یک جنایتگر جنگی است، این کشته‌ها را قهرمان و تعدادشان را بسیار کمتر از تعداد واقعی معرفی کرده است.
🔹
بدانند در قاموس هیچ ملتی نظامیان بزدلی را که سلاح‌های پیشرفته را برای کشتن کودکان معصوم استفاده می‌کنند قهرمان نمی‌خوانند.
🔹
آزادی‌خواهان جهان به‌زودی این جنایتکاران جنگی را به سزای عملشان خواهند رساند.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451560" target="_blank">📅 09:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451559">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بازداشت ۳ نفر در شهرداری بابلسر به اتهام فساد مالی
🔹
رئیس دادگستری مازندران: در پی دریافت گزارش‌هایی مشخص شد تعدادی از کارکنان سازمان مدیریت حمل‌ونقل شهری شهرداری بابلسر در جرائمی نظیر اختلاس، ارتشا، جعل مهر و فاکتورسازی نقش داشته‌اند.
🔹
پس از تکمیل تحقیقات و جمع‌آوری مستندات، دستور بازداشت ۳ نفر از کارکنان شامل رؤسای سابق و فعلی و همچنین مسئول کارپردازی اجرا شد.
🔹
متهمان با اتهاماتی از جمله اختلاس و ارتشا در بازداشت به‌سر می‌برند. تحقیقات برای شناسایی سایر افراد مرتبط ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451559" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451558">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین ویران
شد
🔹
روابط عمومی سپاه: با توکل به خدای قادر متعال و در هم کوبنده ستمگران، رزمندگان هوافضای سپاه در ادامه موج ۲۴ عملیات نصر ۲ در پاسخ به تجاوز و تعرض روز گذشته ارتش کودک‌کش آمریکا به تاسیسات در دست احداث و غیرنظامی دارخوئین، زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون را در بحرین با چند فروند موشک کروز مورد هجوم قرار دادند و آن را ویران نمودند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451558" target="_blank">📅 09:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451557">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
سپاه: سامانهٔ راداری دفاع موشکی و یک هواپیمای اف ۱۵ در آشیانه دشمن در اردن منهدم شد
🔹
روابط‌عمومی سپاه: ملت عظیم الشأن ایران اسلامی! با استعانت از خدای متعال، در ادامهٔ عملیات پاکسازی منطقه از رادارها و سامانه‌های پدافندی و هموارکردن مسیر حملات موشکی و پهپادی گسترده‌تر و تکمیل شب سیاه راداری دشمن آمریکایی، رزمندگان غیرتمند نیروی هوافضای سپاه در ادامهٔ موج ۲۴ عملیات نصر ۲ در حملهٔ موشکی به پایگاه آمریکایی در اردن یک سامانهٔ راداری دفاع موشکی را تخریب و یک فروند هواپیمای اف ۱۵ را در داخل آشیانه منهدم کردند.
🔹
این منطقه جای متجاوزان آمریکایی نیست، ارتش کودک کش آمریکا برای پیشگیری از تلفات بیشتر باید منطقه ما را ترک کنند.
📝
گزارش تکمیلی این عملیات تنبیهی به استحضار ملت شریف ایران خواهد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/451557" target="_blank">📅 09:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451556">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32edfad20.mp4?token=uM0HY-cjvIi1uwAIT-eQwpq617yjKh63czSJHr8HGVQXGxLreXflyLfavK0zyNMVLFAGbddOf8yAx-jY6zZaV4ah4-rPfJP_7fjPYmayEHm9gFqBRYrJXdBqo2AyhlvldYhhic1PXGlX1MpSg3m8eHXk81llrPEc3qbL-7FX_zUyjUT-D2D-as_UBNUD_l5vGPG81R4oyJ_fA57NIsQosBELTgwLy0WuTZ1RsH487z6aqosxxfD2WcUi568CsBGQGiR2Q_bAdxVKDKJpI9bk_98CENIkxJc0pqORVTyuCg8ia9aAUwbJ8PWz_i7_lC-ZYa9e45s8lcbsq3hyBN1mDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32edfad20.mp4?token=uM0HY-cjvIi1uwAIT-eQwpq617yjKh63czSJHr8HGVQXGxLreXflyLfavK0zyNMVLFAGbddOf8yAx-jY6zZaV4ah4-rPfJP_7fjPYmayEHm9gFqBRYrJXdBqo2AyhlvldYhhic1PXGlX1MpSg3m8eHXk81llrPEc3qbL-7FX_zUyjUT-D2D-as_UBNUD_l5vGPG81R4oyJ_fA57NIsQosBELTgwLy0WuTZ1RsH487z6aqosxxfD2WcUi568CsBGQGiR2Q_bAdxVKDKJpI9bk_98CENIkxJc0pqORVTyuCg8ia9aAUwbJ8PWz_i7_lC-ZYa9e45s8lcbsq3hyBN1mDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا امسال گرما را بیشتر احساس می‌کنیم؟
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/451556" target="_blank">📅 08:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451555">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb851bd1b.mp4?token=JBVug50hTCUD8IMW9WaUVmlIOkBK4eAU1MQNnmY3CqzOI_RNzgu1KjBY7GkoF5Hz4NVKY3o8nXjgyucEIzJM2wVYmkh1otSBHWqOhUSMeumm8Qy-irzCYhBjizHNeCW9yAI6abn9P8xH3zeWGw_miEb-nc5IEo9LEztVDbkfMVjYuyZBHVgVXgdNojVzxGHqyl1434WksBhnRUlgZsKkIj1dbuoUtBWwNEEkpiojSP3tMGt1WsBlNr_9hOmcyHcJemop9Mp-yvVDgbBYJ4xaaj6VO559v3yeDMHLsufNm6ynOGq1y2cNGyU5StwzqW7xB2MFd1uwMPlDvQXOl_j3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb851bd1b.mp4?token=JBVug50hTCUD8IMW9WaUVmlIOkBK4eAU1MQNnmY3CqzOI_RNzgu1KjBY7GkoF5Hz4NVKY3o8nXjgyucEIzJM2wVYmkh1otSBHWqOhUSMeumm8Qy-irzCYhBjizHNeCW9yAI6abn9P8xH3zeWGw_miEb-nc5IEo9LEztVDbkfMVjYuyZBHVgVXgdNojVzxGHqyl1434WksBhnRUlgZsKkIj1dbuoUtBWwNEEkpiojSP3tMGt1WsBlNr_9hOmcyHcJemop9Mp-yvVDgbBYJ4xaaj6VO559v3yeDMHLsufNm6ynOGq1y2cNGyU5StwzqW7xB2MFd1uwMPlDvQXOl_j3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز به‌کار چهارمین نخست‌وزیر چهار سال اخیر انگلیس
🔹
برنهام پس از ملاقات با شاه این کشور رسماً نخست‌وزیر انگلیس شد.
🔹
استارمر، اول تیر ماه پس از ماه‌های فشار شدید هم حزبی‌های کارگر خود، رسما از رهبری حزب حاکم و نخست‌وزیر استعفا داد و حالا برنهام چهارمین نفری…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/451555" target="_blank">📅 08:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451554">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ادارات موظف شدند کار مردم را سریعتر انجام دهند
🔹
با ابلاغ بخشنامۀ جدید سازمان اداری و استخدامی کشور، دستگاه‌های اجرایی موظف شدند با بازنگری در شیوۀ ارائه خدمات، زمینۀ ارائه خدمت در نزدیک‌ترین و پایین‌ترین سطح سازمانی ممکن را فراهم کنند.
⤴️
مهم‌ترین محورهای این بخشنامه چیست؟
🔸
ممنوعیت ارجاع غیرضروری مردم به ستاد مرکزی ادارات و سازمان‌ها، مگر در مواردی که قانون صراحتاً چنین الزامی را تعیین کرده باشد.
🔸
ارائه خدمات در پایین‌ترین سطح اداری و نزدیک‌ترین واحد سازمانی به مردم
🔸
واگذاری اختیارات به سطوح استانی، شهرستانی و بخشی
🔗
جزئیات بیشتر این بخشنامه را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/451554" target="_blank">📅 07:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451553">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QV6LhwIgyPO0_uVZ_Uc4uixi6V6-Pg2Smr4965KKlF7V3SPPZRAylWJYl-mae1b1STdii5Z99PhYCq1D5SktFCzADcuQfcQXD6DizuNkiByqSbp4P--Q64vSPG_P8W8LyeCBmGOFk_sV6WdYTMNiYOHz3O096dW1PPPMx_BGe9sOZiUpfg1QEhP7BLp0jj7C3-QefbMfxf90WM7k3qypPo_6huc3471f_vyh694n7hZSaLcRrA9Hj5g5sjYboW68bkPwUL2iiJqAebHfy5MMo7RvcUprhDZd9bv9OaIGEYVDUs3jFlmPoGDvVerHlEi-_oQ85rf5VtvI6T3KIyb0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژاپن حامی تازه تالاب گاوخونی شد
🔹
معاون سازمان حفاظت محیط زیست اعلام کرد که برنامه احیای تالاب گاوخونی در اولویت طرح‌های بین‌المللی این سازمان قرار گرفته که بخشی از اقدامات اجرایی این برنامه نیز با اعتبارات دولت ژاپن انجام خواهد شد.
🔹
این نخستین‌بار نیست که ژاپن به کمک تالاب‌های ایران می‌آید. دولت ژاپن در ۱۲ سال گذشته با اختصاص ۱۳.۳ میلیون دلار، به یکی از مهم‌ترین شرکای ایران در حوزۀ حفاظت از تالاب‌ها تبدیل شده است.
🔹
پیش از این، تالاب شادگان و دریاچۀ ارومیه از این کمک‌ها بهره‌مند شده بودند.
🔹
اکنون نوبت به تالابی رسیده که از سال ۱۴۰۱ به تدریج آب خود را از دست داد و سال گذشته، خشک شدن ۱۰۰ درصدی آن رسماً اعلام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/451553" target="_blank">📅 06:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451552">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
سامانه‌های موشکی هیمارس در کویت هدف موشک‌های زمین‌به‌زمین ارتش قرار گرفت
🔹
ارتش: در پاسخ به حملات موشکی شیطان بزرگ به مناطقی از کشورمان، ساعتی قبل و در مرحلۀ هجدهم عملیات صاعقه، نیروی زمینی ارتش با موشک‌های زمین‌به‌زمین، سامانه‌های موشکی هیمارس ارتش تروریستی…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/451552" target="_blank">📅 06:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451551">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42c0f762d8.mp4?token=Fo3EsDPEgnXC-rYjqArSsEsAAAvsFxKjxOIUrBvhqPBzXdBb5c-pVdjT_c4pdxEfJ8hfrbp0eOT1y_aT_sOTBdcDzwHP2wyY2U1QGWWQu0IafhBXu-dkPuaUS-mn1Vjuv_kK3tf0kwXBjTNKmduSqvi8Ju--pGh4eqcdnEA5cFbMa-6trEaDI4XgNmiqyg1MdPsA19P5XL4LMUyFuf9Wtiom3098emKewoaRfYM9dUMR-VYptmbNAtF79L1d84V9pm1bAEenfX7x0MBu4Nq8pMotIavs9JZdlP06s-yb_jQ7cxPQj4b_8yBr9ZXl20c8jyglfTle45iYLDHJWFU0iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42c0f762d8.mp4?token=Fo3EsDPEgnXC-rYjqArSsEsAAAvsFxKjxOIUrBvhqPBzXdBb5c-pVdjT_c4pdxEfJ8hfrbp0eOT1y_aT_sOTBdcDzwHP2wyY2U1QGWWQu0IafhBXu-dkPuaUS-mn1Vjuv_kK3tf0kwXBjTNKmduSqvi8Ju--pGh4eqcdnEA5cFbMa-6trEaDI4XgNmiqyg1MdPsA19P5XL4LMUyFuf9Wtiom3098emKewoaRfYM9dUMR-VYptmbNAtF79L1d84V9pm1bAEenfX7x0MBu4Nq8pMotIavs9JZdlP06s-yb_jQ7cxPQj4b_8yBr9ZXl20c8jyglfTle45iYLDHJWFU0iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حماس: ضامنین آتش‌بس، حملات اسرائیل را متوقف کنند
🔹
مقاومت اسلامی فلسطین: حملات وحشیانه‌ای که چادرهای آوارگان و خانه‌های غیرنظامیان بی‌گناه را هدف قرار می‌دهد، تجاوزی سیستماتیک در چارچوب جنگ ویرانگر نتانیاهو است.
🔹
ما از میانجی‌گران و کشورهای ضامن توافق آتش‌بس می‌خواهیم که فوراً برای توقف تجاوزات اشغالگران اقدام کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/451551" target="_blank">📅 05:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451550">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBuRx29Kfy5Fg68obP1xToO7es3KLUct1JSPDfKZLxlTW_EyUXVntXIm2WA7qZFoo8Qm7DXAMByYqvcN8ggl3FL1fhEkDh2BVDwJfiC6cUrhss1YMLF769UAtjp6H5JbnLd7PRSj_kLegp3GnBBx3IGdqP_EytTG5eK2Cz52L92EOC1_YQEzgTTR9wjfzNq5reYZBuK4V6WzgiyISm8Ell2VUSPV7nIUhCHny7rD_L1h-AMG8R-sYm1D3bCPdp_PyrmdvQM482rTrHCuqyjC-R45FuJKTA5LJ7BRWMo2UhfmC7xBA7Y7NdK4sqbnHNmK3CLgk_iunHa487C3ow1vQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دود آخر کارخانۀ قدیمی تهران خوابید؟
🔹
کارخانۀ سیمان ری که سال گذشته برخی از خطوط تولید آن به‌دلیل آلایندگی در فهرست صنایع آلاینده قرار گرفته بود، هنوز نتوانسته مشکل آلایندگی کورۀ شماره ۴ را به‌طور کامل برطرف کند.
🔹
سرپرست ادارۀ حفاظت محیط زیست شهرستان ری به فارس گفت: مطابق مادۀ ۲۷ قانون مالیات بر ارزش افزوده، واحدهای صنعتی که پس از دریافت اخطارهای سازمان حفاظت محیط‌زیست در مهلت مقرر نسبت به رفع آلایندگی اقدام نکنند، مشمول پرداخت عوارض آلایندگی معادل نیم تا دو درصد خواهند شد.
🔹
این مبالغ توسط سازمان امور مالیاتی وصول و به حساب شهرداری‌ها واریز می‌شود تا ۵۰ درصد آن صرف اجرای طرح‌های زیست‌محیطی شهرستان، از جمله توسعۀ حمل‌ونقل عمومی و فضای سبز شود.
🔹
هزینۀ نصب و ارتقای تجهیزات کنترل آلودگی به مراتب کمتر از پرداخت جرایم و عوارض آلایندگی است و کوره‌های فعال کارخانه در حال بهره‌برداری هستند و واحد صنعتی نیز از ضرورت رفع آلایندگی کورۀ شماره ۴ آگاه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/451550" target="_blank">📅 05:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451549">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شب سیاه رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه
🔹
سپاه: فرزندان شما در نیروی هوافضای سپاه شب سیاهی برای رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه رقم زدند، و در موج ۲۴ عملیات نصر۲ به‌منظور هموار کردن راه عملیات گستردۀ آینده و از میان برداشتن…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/451549" target="_blank">📅 05:11 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
