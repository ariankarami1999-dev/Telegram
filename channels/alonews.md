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
<img src="https://cdn4.telesco.pe/file/jhWrHEXaDTewVdE73FgELzETTSfQ3LI-ETZeGK3gNg4Pi0uP9yal59u1pPDFG9oX_lpbn0ofCgfaFVyHfgUZ-r3K_x7XPF1FXToEJcWtHpvL_GIS7jLwFi82wz_uQ_n2PoHKb80ZP83-wdFm6Ba_jXYAs6XhOGrOEB2xssd4ulb1O2Ek3J4co0O53SMaScyRpwa7XDKEmGOdF7qAu4qwR7w5eI-T35odgi9RrOnAlVuPX1jqbLFp5cxDSriBQQocha2NZ3YMvDz8Z5PzeK5npMO70OyrE5wJASwCQPY--laJRE2eeAm3Ku0prJeqP6InbzFlwRI91l-oQ6XIs0Mr3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 991K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 16:02:47</div>
<hr>

<div class="tg-post" id="msg-139393">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نشریه اکونومیست گزارش داد چین اندکی پس از دیدار دونالد ترامپ و شی جین‌پینگ در سال ۲۰۲۵، ارزیابی و آزمودن واکنش متحدان آمریکا را آغاز کرد.
🔴
این گزارش می‌افزاید پکن از آن زمان تاکنون به‌طور مستمر دامنه فعالیت‌ها و اقدامات خود را افزایش داده و فشار بر متحدان واشنگتن را تشدید کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/alonews/139393" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139392">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkvcLtMNKdF005yBHcTvKOeWUhgbEgj_VCW-dT7yJKb1hE4HIAzbKIVGjp63PUg4MCaHVQjD9ebRcBWQVwEp1VnL6ExjjdnWvroDlZKSZIAbaU6ls3e2cQppL6U4Gjml8CTcX3DKvQ6LMKRvjeDDA0PzipKSbS6xiq4UxOcYHDpopL8GlmVJbk51eHHHfo3da8KNYNWWvhzhSi3ooulVdPu8OSAdPFGtu-CNp4U4lqTGuH6OXuBIY6oEEmV0rwdGjcc31bheUr25o51C66Tt4hqOuw6oSuBCupyAc191u32yPcHWK8eFoB5cLGwHNlU0dt30_jfts9YFBkRPZNz5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چرخه مودی ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/alonews/139392" target="_blank">📅 15:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139391">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
مشاور امنیت ملی عراق گفته است که توافق شده است تا یک دفتر برای نمایندگی ناتو در بغداد تاسیس شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/139391" target="_blank">📅 15:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139390">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ادارات خوزستان دورکار شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/139390" target="_blank">📅 15:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139389">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سنگدوینی، عضو کمیسیون انرژی مجلس: ۲ تا ۳ هفته آینده قطعی‌های برق تمام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/139389" target="_blank">📅 15:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139388">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
منچ‌اوسینت: کشتی حامل گاز قطر که تحت اسکورت آمریکا حرکت می‌کرد، در جنوب تنگه هرمز لنگر انداخته و متوقف شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139388" target="_blank">📅 15:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139387">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
باراک راوید: جمهوری اسلامی با بازگشایی تنگه هرمز موافقت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139387" target="_blank">📅 15:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139386">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مدیرکل فرودگاه‌های آذربایجان غربی از راه‌اندازی پرواز زنجیره‌ای تهران–ارومیه–مشهد خبر داد و گفت: این مسیر هوایی از هفته جاری آغاز شده و در روزهای دوشنبه و پنجشنبه هر هفته برقرار خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/139386" target="_blank">📅 15:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139385">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epbC9OPS19AEzt5-Zs6pBQykEGplFMJkt6V9Hdj9DuUx1ANwvT2g7Ra6HlatQvWjrjEqm8NDJnMXZClVXwytodGpYWtAUVUe8mDDy9B0FjxaeN-LunLWe2XFgaz5_Xg3p7MHPTo4384U3tWbjUp9FI-45CkGPHLW3MA602K0rFCyulLMqvszDc_Ae9LAtuQoF4LoUbzDdtib1Brwh0SEXZIJIAeHMVwUetRP38JT-PeHyDf6bHDsal3mLq0LFzfqYK-IF3S2TIv8Mw9QPHH6rUKtAL5cYWZO7XMaf8IK-tn9PgLxETK0nk3amsvmYnMbq30V2y-0TipFf-q-d9rbrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید: جمهوری اسلامی با بازگشایی تنگه هرمز موافقت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139385" target="_blank">📅 15:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139383">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jC5VcoyCl7NfpfcLWFMYiHIo8aV13vCGaro6hq_yYfsuSD_bsDxuAMnEHcJ2esyRFk5pROWcHyVoRR1qbsW-x8YCONWUj9u_CVHEmta5igH59Yvo-jTcoyJIowZYFUeFmakp-tLGE0Nsf10-t4JXXLORFg1S0OOrfApBFAucCf8eVd5cUvaIior_5lrkEsggrX6_V75iuWrIUMyCjVZ1zHFpNrvEzkm0vcoMEtOmv9V0prfmILnOw3n2K7Ohemrhcq0GQ2VUIheIk1F-3UknObp9Nix1ITzJE-sPfLfuUY4m00dvuHwRlX_5Sq5rJZekfEF3PuYjSQWTqrfQ9sE9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvQzIVqmbAiMoE8KStSZ-mhPTzHy69ufwCxrwjp9JUF9kffryNtpM7lqaEIZA28JC4q_Fv2KCJcjMl81ZaiERoL-yaXNyxthe7cvFkeSR-bCjkYKpMevqn0Ut4rYG8PJ-HQKn8HOHKyYv_-H4wZFNTkLUyzshaIBrrdFgh0l_cICbYj3S2Hz5bI0J-HKqDdZvzsNwJOg5j5ugFvHbkAI0BROf_4bc7Lr_6Fu1MaZF0QollOEdSiig9iiXArEbarT0nw2gtLQonZOaQCdosZd6VH6ICopY5P5DTkowuTs1Ff4W2-zuICrZMQ8KsYc06KcXHxILpi4HNDyTj9CVgwHcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تعداد هواپیماهایی که از پایگاه‌های هوایی اسرائیل به سمت عراق و عربستان سعودی پرواز می‌کنند، بیشتر از حد معمول است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/139383" target="_blank">📅 15:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
عراقچی به نجف می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139381" target="_blank">📅 15:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری / آژیرها در اردن به صدا درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/139380" target="_blank">📅 15:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139379">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d12df834aa.mp4?token=AdrbHiFctJT1dFJjCkq0JA3re48izVN6ce1wsOiaK5avICjllRzUT2hr-QLSDsMcOGkj91oboJB5ANWPc5d1LLJBZNtG7da_W7LRV1qO5CIvspTh1BA80WEoOQ_2LQis10lohNxqMt5AaAEX4rKridoFrHXCpwixahcvZvW25txi5XSP9MsZB2yqgAMpTJAWzC_h4l_9tKxuW1qcMW5jljbbdKebWyURq1a7hpkuNgCGHT1Kq9sRCGBOQp4GX8CrCJ2IyIeKvlwbqnwowNhYADp6rHXty9PFY4zzuS77vAZGffD19i7UkI_hb8563i2N-WehpbwSDFWfQXtBpbgstQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d12df834aa.mp4?token=AdrbHiFctJT1dFJjCkq0JA3re48izVN6ce1wsOiaK5avICjllRzUT2hr-QLSDsMcOGkj91oboJB5ANWPc5d1LLJBZNtG7da_W7LRV1qO5CIvspTh1BA80WEoOQ_2LQis10lohNxqMt5AaAEX4rKridoFrHXCpwixahcvZvW25txi5XSP9MsZB2yqgAMpTJAWzC_h4l_9tKxuW1qcMW5jljbbdKebWyURq1a7hpkuNgCGHT1Kq9sRCGBOQp4GX8CrCJ2IyIeKvlwbqnwowNhYADp6rHXty9PFY4zzuS77vAZGffD19i7UkI_hb8563i2N-WehpbwSDFWfQXtBpbgstQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما: فقط یک پنجم موشک ها مصرف شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/139379" target="_blank">📅 15:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139378">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnjnwA3AaYaC7IkTRZ3Fu4cGzgJ6yqHRPCntVHXP_5Q65xx5pytT46vRDgb8uw0nlEMjAbow0ZhSM5_9NtMCqZFstFUMofedUGiAqkj2t5iF82ROX9wo8nSNa6rgi5EhW7Soc3YmI3qRzsVcq0xLfCXzoxE31n2uFebjKcLLW8uQQxc-uBYYQpA-iYpEN-cF78lmrymiWIuuhYv9WG3OABRyhnvV_8aLwXAOKZsvvH2xzKF9fsj7dXIx-vMUK_q5ndjTm9nCInUAulFyvJRLcqopU6eMBivm2eTDUL3lqrtcM0aDpnhG8l9iGI8ZYzD2Kgkr1m3bd_fHZD_QGv2-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای سومین بار در طول یک ماه گذشته، درگیری‌ها میان نیروهای انصارالله و نیروهای مقاومت ملی یمن (حامی شورای رهبری ریاست‌جمهوری) از سر گرفته شده است.
🔴
درگیری‌ها هم‌اکنون در غرب ارتفاعات البرح، در محور حیس در جنوب‌غربی یمن، ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/139378" target="_blank">📅 15:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139377">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سازمان اوپک: هفت کشور عضو برای کاهش روزانه ۱۸۸ هزار بشکه‌ای تولید نفت خود به توافق رسیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/139377" target="_blank">📅 15:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139376">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeMn-2evDoExS-g7Bp8QpWmkHgJZUxtzShxJHdR6JTgWdmOcIyBw-dHmmy3_21VyuwCw18zDxpzhrlTUWkPcawh2uKnn7QdF-xk0s6CTfmtlbVhTel2sbkUZj4zNDGpV13uwyrhGnRRZ6CPrFEd3GSIYgEzBAFnPR5yA9FYnQIOlb1ZAhCnTp55ploW8qQBp9QkS5-PBXTMsFIGbfqvyjKYdAuN-P3cje_5EVDGzJHcWqYBdv1jc4cBfqpunkXudIys2Oa6WmQayXqoeiSOKgRG9uTYW5TRxB42Gz-pTsMRMqo3C7YkZudUwVcgWcUZmJmfG1Wl538EqSzlpAhJ-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان، نماینده مجلس: عده‌ای در ایران با انگیزه‌های گوناگون از جمله نجات دشمن مجددا به فکر مذاکره افتاده‌اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/139376" target="_blank">📅 15:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139375">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد یکی از فرماندهان گروه حماس که در حمله ۷ اکتبر ۲۰۲۳ به کیبوتص "نیر عوز" مشارکت داشت، در حمله‌ روز شنبه ۱۰ مرداد (۱ اوت) به جنوب نوار غزه  ترور شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/139375" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139374">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAfvcfa0nMZrpqYW38ydSry8J2m2yiBgeOkQrPyu7y5J4QY71qnytoFkQgRmdKR5DCVErE_4dXqNC7Jq7GGFXEg7WhqFn2W-1eSqTeHkO3aitZiqW_cIGU_Q0s22-y75YHVdwFW_s6zpoApaFfqT8pWMh2EoClldaelK212LKEpGRclG8L2BFyL1orL-oGa6d5J-BeT2l7BoKTMjfnmv_lEzfpQSuIwWkgs2ymCbe_AiqpTp4K7cOY-NfPwSEvuLFy0fVgTXgSoTn7Akd6U6psWQ8JXZ8T_0_ymXhn7pSzv376UHRnEWSPBWBDErS3hWd_gunaWT0AW8DvO-7uVLkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسموتریچ: نتانیاهو به ترامپ گفته نیروهای بین المللی غزه را اداره کنند، یعنی غزه منطقه بین المللی شود.
🔴
من با این موضوع مخالفم. ما یهودیان باید غزه را اداره کنید، به نظر من راه حل دیگه ای وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/139374" target="_blank">📅 15:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139373">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
مرکز آمار:جمعیت ایران به ۸۷ میلیون و ۶ هزار و ۳۷ نفر رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/139373" target="_blank">📅 14:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139372">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
یک نماینده پارلمان اسرائیل می‌گوید
بعد از تقریباً سه سال جنگ، 966 سرباز ارتش اسرائیل کشته شدند، 24000 نفر مجروح شدند، صدها هزار دستور احضار برای خدمت سربازی صادر شد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/139372" target="_blank">📅 14:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139371">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2t23kvCODhkx3IS9409q1SP2ETBQIESsi9NDMFq8O6YJlg9aVknTv2wp1KcWxvdczbEk-75iy8V-oh6EFRxhn30WmPjPouA9zgO-AoXWBHBYzXBEG52uhar3YdGrIgNFy1Y_wF8jcD3t6HBXFuSXCRMbRl5Vi8ByZEz19qYkJ-hSk5fn2160XXvlpT_R_LXAotllfODHcQK7Dv_5iWIyHsWXWc9DMEgsMWAtixg7hC64I-gsNaAZ85bQALtdnPM6CDFfynzjSx1S3Q37hcmTnzb1N0DOHHK6a-NjigewUA4cknIGfSOqhjKwyXf7lRK2sR3hj9njIPxwB1bAGiYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه های اسرائیلی با انتشار این عکس، تغییرات خلقی ترامپ در هر روز هفته رو نشون دادن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/139371" target="_blank">📅 14:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139370">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXhOoqk1Owh7RinlyJhw8GcNAR0LyesLaiAddkW3KgYIzURdYgl0Rmhiye5qk47H8DaSzn_9KFk7MEgeVoQWI3pYSz5f0-jzUZvlbUCYzdh-7yRJOqd0DIQRAL1jRNrtV77WZnIKUQdNalkvaZpb8Ya1RvhQizgtqMxkrRII7DmVs_8uYq8z38N6hFLWxtu4djXx6n0ZtrX03em8RhEIaxS_He2-48_AkhEbrGp9FPyDxC4v8w-shCqrJR_K8QwsrhpWmmuGB3mXv-rMvwIE6IeBLrt0fOm7GlJsYntv4cxbeB5emkcBKEXDKmuYSbEiJH3_LwwRiqleka-42L3KNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش لبنان اعلام کرد که در پی حمله‌ای از سوی اسرائیل در جنوب لبنان، 5 سرباز مجروح شده‌اند. این حادثه زمانی رخ داد که نیروهای ارتش در حال اسکورت یک خودرو نظامی به منظور کمک به ساکنان محلی بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/139370" target="_blank">📅 14:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139369">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
الجزیره: سیاست فشار حداکثری امریکا علیه ایران، به رقابت این کشور با چین گره خورده
🔴
یکی از نشانه‌های تغییر موازنه قدرت این است که واشنگتن پس از ناکامی در جنگ علیه تهران، برای آتش‌بس ناچار شد به پاکستان، متحد نزدیک چین، تکیه کند
🔴
با توجه به گسترش روابط پکن و تهران، فشار ایالات متحده به ایران، تلاشی برای محدود کردن دسترسی چین به منابع انرژی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/139369" target="_blank">📅 14:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139368">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه قطر با وزیر خارجه عربستان سعودی درباره تلاشهای کاهش تنش در منطقه به صورت تلفنی گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/139368" target="_blank">📅 14:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139367">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
آناتولی به نقل از منابع پاکستانی: میانجیگران پاکستانی و قطری «خوش‌بینی محتاطانه‌ای» نسبت به از سرگیری مذاکرات متوقف‌شده بین واشنگتن و تهران دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/139367" target="_blank">📅 14:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139366">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
گزارش مرکز آمار از افزایش قیمت اقلام غذایی نسبت به تیر ماه سال گذشته: مرغ ۱۹۰ درصد، شیر ۱۵۰ درصد، ماست ۱۳۰ درصد، روغن مایع ۳۴۴ درصد، روغن جامد ۴۰۰ درصد و سیب و موز ۱۰۰ درصد افزایش قیمت داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139366" target="_blank">📅 14:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139363">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJXZ3nKtH2NoE4ehPZGSVM44d4nAIppH42D509rFG0SHWq71uBjs6rCq7y13WSEl1l8wrRPkTalr_o9z7newBwAzqloYCDfrHYKY48c3P-oJ6KWI-yLrStk3uPfuySXmjM37b54FkmwUVrH1k8NIQUJWOA4N2Sf2YrueY5goGwsOGlUJv-ZEIC_tVRrrFD5ggGNVkEGWBF1kcB6WWdgJSJKH7ie437fuN-7uSzmtOJ3XQHa2VW-3lxrSNPMM3QNUo3zDeRyD8PmNXG2aS4XjJFbdGhjxythBTf0jM3ClTWZbkCwoDmCFJ9Ztd5wNPJ5N3Zf5q2eWXsORh1T2urvCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-3MCIQz6w4uTmV9aZRn8QZfjOQpPzCkZmVy7lOClNafu0v34WztNcL1J3kcKu8Nf_sUKlGYkrb5Ds2jibaDtp6iXejPlLZAw5EbvnoqLljCvPLTsHW_aWHMhrlhBXUl-A7M7c5D7t5icxU_LxreP2PEnbJg-yV9-3ritGX7CEnQP1WFvUQzNfbGDOPCJdrDYKyPk8WIVrTL9kWXaI9pQXikpOlvIQzs3tEBc_s1r-9k_V9OsAiYsX8-hID71FGOCIlDkKcyyOcA4UVRW7DkZvebKo6M9-oUqIitfVKzIrcFcBnku3byHUvtyXGCPFyPWZzZkQT-ufvpJuURU5rItw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uN75FmSu4T9k8Nb1w6EKeuCsV1sGR0RPlnQzQ40s9S5IfNRsdwIM53LltHgmesxgwn_n9Ha4qIrc_VcT98U2b1YCBFSBd6bZZY4FfIbT321Y2UpQQJ62x7sXLLXXTR3VPqyf-L3DJUJC8T-YsV3WY5q2bWU4HZpV320lClQxrEK86TgOEBIR6uH9rnyy8ZpDls0kn8t0k7TLrta7i26vkDpS54W6_CCuwrtRZYgzHGvva7WEQuFtpB-WECH8gPNH4EQrf0i0Db0r0UESWgNb4FQ10AygdtoU1eX-NguU-scBb12G53AEek99UPE4npsJycEFxnKPXyMfOLM4y-HxXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جدیدترین
برآورد از انتخابات میان‌دوره‌ای آمریکا (۹۳ روز مانده تا انتخابات)
🔴
شانس کسب اکثریت در مجلس نمایندگان (Kalshi):
۸۴٪ دموکرات‌ها | ۱۶٪ جمهوری‌خواهان
🔴
شانس کسب اکثریت در سنا (Kalshi):
۵۳٪ جمهوری‌خواهان | ۴۷٪ دموکرات‌ها
🔴
آخرین
پیش‌بینی امریکانا از ترکیب احتمالی سنا:
۵۱ کرسی دموکرات‌ها | ۴۹ کرسی جمهوری‌خواهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/139363" target="_blank">📅 14:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139362">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
شبکه العربیة: جهاد اسلامی فلسطین با توافقنامه خلع سلاح موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139362" target="_blank">📅 14:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139361">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
قاسمی، عضو اتاق تعاون :
آمریکا با محاصره دریایی ایران، امنیت غذایی جهان رو گروگان گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/139361" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139360">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
شرکت هواپیمایی پرتغالی TAP تعلیق پروازهای خود به اسرائیل را تمدید کرد و لغو پروازها اکنون تا ۱۵ سپتامبر (۲۵ شهریور) ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139360" target="_blank">📅 14:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139359">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
تحلیلگر صداوسیما: هدف ترامپ از اینکه این همه تهدید می کنه و حمله نمیکنه اینه که حمله به ایران عادی بشه و دیگه قیمت نفت و بورس رو تغییر نده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139359" target="_blank">📅 14:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139358">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8wTQ8xQAyHlNTGflF1BQEmHQoCNX4i0KmUaX615504CbTEqcfYslZ1zaHsr8ldeKEHgQHrVSB-OHdnnkT4lJLk6WP70LrY3NuwAZgZDJnalNE7v6nEOTUwBZ1A-RBj9SydVcb66sHZDaMDLKxcX3WfBD8f6S0lxtw8qklypPhgZ5qeeCgOs_0ed3hf3237SrCk6CgI_ZKq1C-1FvxMy9739Kz9Rfz-Fvzu16gAVIsieECq-FRPlxpv2bzLFg8q3KIwSOe4fuL6jMxlcH-BuQ-X4IjujCioFAhxPrsaAXl4HId130VO15tv2ZBqdmaQhCSUsaijnq5eYySxuu7bTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک تخریب قدرتمند تحت کنترل اسرائیل در طیبه جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139358" target="_blank">📅 13:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139357">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
خبرگزاری رسمی عربستان (واس):
ولیعهد عربستان با ترامپ درباره پیامدهای منطقه‌ای و بین‌المللی گفت‌وگو کرد و بر لزوم اولویت دادن به گفت‌وگو برای کاهش تنش‌ها و تلاش برای دستیابی به آرامش تاکید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139357" target="_blank">📅 13:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139356">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=iDdnTKlzkLEyGoJXHXny27bGtXEPrLVSpphe_cC5f9fn-fAjt6F4lsgcZsuwnnPgXdYBRkQaUF6WvkSBGBtrtDovT5WsNZmuMCfZMRCQ332Y4yi0WPkWGb6HbiXH-H3Axr81xqMdzLEdDIcrO5RLI0_JyG7CjH3Fj1wPDk1ZeCifi3-wdpYu__uu9YeP3Jck-Ngy7QKnBDac0taD66dkob1fZPFVDB9xRh8jQlqjWOGRfAAJ-6J2xMRC1q_i3xiTHCy4q_8u59rIxYzQT0nzp9SCQPi8RnaZKU2e7zhC-mEDCWAVE2DtgLJcdyu-6_xxFISAVpRyX6hUNiWI8uNETA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=iDdnTKlzkLEyGoJXHXny27bGtXEPrLVSpphe_cC5f9fn-fAjt6F4lsgcZsuwnnPgXdYBRkQaUF6WvkSBGBtrtDovT5WsNZmuMCfZMRCQ332Y4yi0WPkWGb6HbiXH-H3Axr81xqMdzLEdDIcrO5RLI0_JyG7CjH3Fj1wPDk1ZeCifi3-wdpYu__uu9YeP3Jck-Ngy7QKnBDac0taD66dkob1fZPFVDB9xRh8jQlqjWOGRfAAJ-6J2xMRC1q_i3xiTHCy4q_8u59rIxYzQT0nzp9SCQPi8RnaZKU2e7zhC-mEDCWAVE2DtgLJcdyu-6_xxFISAVpRyX6hUNiWI8uNETA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدا سیما
:
تنگه هرمز همچنان مسدود است... تنگه هرمز امروز شاهد بادهای شدید و ناآرامی‌های دریایی است، اما اراده رزمندگان ایرانی استوار و قوی است و بر این گذرگاه آبی تسلط دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/139356" target="_blank">📅 13:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139355">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏
👈
شمار قربانیان مهاجرت مرگبار به سئوتا به ۹۰ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/139355" target="_blank">📅 13:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139354">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری/ ترور یک فرمانده از نیروهای جولانی در حومه شهر درعا
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/139354" target="_blank">📅 13:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139353">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
بلومبرگ گزارش داد کشورهای اصلی عضو اوپک‌ در اصول با افزایش جزئی سهمیه تولید نفت برای ماه سپتامبر موافقت کرده‌اند.
🔴
در صورت نهایی شدن این تصمیم، روند بازگرداندن تدریجی عرضه نفت که از سال ۲۰۲۳ متوقف شده بود، از نظر برنامه‌ریزی به‌طور کامل تکمیل خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/139353" target="_blank">📅 13:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139352">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
بروجردی، عضوکمیسیون امنیت مجلس:
به احترام اربعین سکوت کردیم اما پاسخ به دشمن تو راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/139352" target="_blank">📅 13:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139350">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فووووری
🚨
به نقل از آکسیوس، سنتکام کلیه حملات خودش رو به ایران متوقف کرده !!</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139350" target="_blank">📅 13:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139349">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CocwLqiGt2SPiZu8e59lnHrGrAPl5npIUzktVEd44EDEx5z04fhxGSgGtBaabrJP0DSexyMXTvHOqHiuZJbvfc60j4TuzI_VKHb-yVVR9zR6qA-LEfVURGxF9tb3lX8YliiXt_Mz9pzUZMNo5T3DeurMKwxyZBknhpiXbN3fnwDJZfSAUhpoxQqOzRK3J921_Cg4CUjQkLbXek719cMVrihYTaw7zV3xwtlUHuJ9Xy8qSTsMILIfEBDmGwW1tIMj6Z0W5QR0eLgzCP2zaHLvpBFZn-Jf7gkkl6ir5Uhk6oeESJU30x2WMpKCc2gFDfFUcLtY7dGlQ94W9kBCWvZArg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس‌نیوز در گزارشی با عنوان «وضعیت تقلا برای بقا» مدعی شد که ایران در واپسین مراحل یک «رژیم درمانده» قرار گرفته و هم‌زمان آمریکا قلب صنعت تولید موشک این کشور را هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139349" target="_blank">📅 13:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139348">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd816c7b4.mp4?token=MCWyd8Um_fStPeoIawJYeAyHx20BnbDhIDM9mBVBGwnOlluc3tc_AphLktbi9_nLzMxWREoOF3A7ufyFOvLIhgno614W5xkoZ_AL-nKJii-Z8yft7aVc6xhJw3du903RdxBXnEFIr8c4txGzD5TFFRJNiU3Z8acCLEGkS9jFZeTF7-5TQItkLfrq2w6EdjWtQEWTdOVWALUE-WlWd2qKqNpr6Xe6-hoptNB9DVLbAQLImECZdOlmiru1AvTYlVj9ATPb1YCijUDXTpbNip1dL1a9l95Rax8AvtqUyerrdvc3et340cyyAS3jbx9cCOw5mU6twQc_L5vvfpqtgrNJTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd816c7b4.mp4?token=MCWyd8Um_fStPeoIawJYeAyHx20BnbDhIDM9mBVBGwnOlluc3tc_AphLktbi9_nLzMxWREoOF3A7ufyFOvLIhgno614W5xkoZ_AL-nKJii-Z8yft7aVc6xhJw3du903RdxBXnEFIr8c4txGzD5TFFRJNiU3Z8acCLEGkS9jFZeTF7-5TQItkLfrq2w6EdjWtQEWTdOVWALUE-WlWd2qKqNpr6Xe6-hoptNB9DVLbAQLImECZdOlmiru1AvTYlVj9ATPb1YCijUDXTpbNip1dL1a9l95Rax8AvtqUyerrdvc3et340cyyAS3jbx9cCOw5mU6twQc_L5vvfpqtgrNJTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بر اساس تصاویر ماهواره‌ای، پایگاه هوایی شیخ عیسی در بحرین که توسط ایالات متحده استفاده می‌شود، اخیرا تخلیه شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139348" target="_blank">📅 13:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139347">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
العربیه به نقل از کانال ۱۲ اسرائیل:
اسرائیل قصد ندارد حملات به غزه را متوقف کند مگر اینکه حماس خلع سلاح شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139347" target="_blank">📅 13:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139346">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سخنگوی دولت: حذف کامل کارت سوخت در درازمدت منوط به این است که به طور قطع بدانیم هیچ مشکلی از منظر کارت‌های بانکی وجود ندارد
‏
🔴
در مورد کاهش میزان سهمیه بنزین به زیر ۶۰ لیتر هنوز هیچ تصمیمی گرفته نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139346" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139345">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سخنگوی دولت: دولت در حال پیگیری فرآیندهای قانونی برای صدور گواهینامه موتورسیکلت بانوان است تا با رفع چالش‌های حقوقی و قضایی ناشی از تردد بدون مدرک، وضعیت این گروه از موتورسواران را ساماندهی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139345" target="_blank">📅 13:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
العالم به نقل از رسانه های عبری: جسد یک افسر اسرائیلی در حالی که اسلحه او درکنارش بود در منطقه النقب پیدا شده است و احتمال خودکشی این افسر وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139344" target="_blank">📅 12:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
یک منبع نزدیک به تیم مذاکره‌کننده به فارس: هیچ توافقی دربارۀ بازگشایی تنگۀ هرمز وجود ندارد و اخبار منتشرشده در این باره کذب است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/139343" target="_blank">📅 12:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139342">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
یک مقام ایرانی: ایران درخواست نکرده است که ترامپ حمله نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139342" target="_blank">📅 12:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139341">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocppzBzxm0DvBtZTAmWaUO2PVIzaj4cbhMC-6uYlYUmqU0KVKICtWmRq8MuAXFr-Cqa1i2EXE4VILzJuu9L4VIzeJoesEc6Im0e9kRU7xeY2p9o4UHPLJBE3TgFLle30ftrdVm5obs3WV3Y8CL-m_0fTLT-uG2Ak_xuTgPQ5HcKlrrn6nDYsthqbnXlARZ8Yll7PsznQS_yihzgdrSgbeQWma6SPESBRx-DP6AHLfaoebp18fV0LkHN4hzieaWTMQVSjfDvRIgpDJMg3TDHVxCvuDLJnk_QXo_NxKdr5xUp2PphgYUDmUsd5ErBEbFnsytE0xF81lf3_Ev_JfcR6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جهش ۹۹ هزار واحدی شاخص بورس در پایان معملات امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139341" target="_blank">📅 12:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139340">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsDUaNiXT1TbdYiBWxkyP101zak0ItXjLwmufrLephuYIIjXSpKTHFkPV5TCFCN-JPBQBjdYj1Q0UvXk4VYClwt8zLy3fVF5lyeQuVOfWCX2C0rVmo8BRXN8cJWu72T7hI9vSEz8cYxamBLOHyllAmLQYZ_kEERkL21K_HGeNFgLD12m-3eb4wA-r3nMCKrhoO3EIKoNf7kzOJSkh_SNAKCxsSOzolf0Jz7lfJnEUa-iQOpMNfMn1aa8w2shlaoaZy94SVOVDFObN5fc_ilh5tXpCa58YSg_spJfOgtp1clOLHFoUULGrJnSZFToBiO2JVCDXxLjtjelavt7wtoafg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هوش مصنوعی "گروک" اعلام کرد که از زمان آغاز جنگ با ایران، ترامپ حداقل 10 بار از تهدید خود عقب‌نشینی کرده و حملاتش به ایران را لغو کرده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139340" target="_blank">📅 12:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139339">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نشریه Middle East Eye مدعی شده است که دونالد ترامپ از اسرائیل خواسته بود در صورت آغاز حملات نظامی آمریکا علیه ایران، به این عملیات بپیوندد و مقامات ارشد جمهوری اسلامی را هدف ترور قرار دهد.
🔴
این ادعا تاکنون از سوی منابع رسمی دولت آمریکا یا اسرائیل به‌طور مستقل تأیید نشده و عمدتاً بر گزارش‌های رسانه‌ای و نقل‌قول از منابع آگاه استوار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139339" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139338">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ستاد مشترک ارتش اوکراین: یک پالایشگاه نفت و یک پایگاه هوایی در استان ساراتوف در جنوب غربی روسیه را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139338" target="_blank">📅 12:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139337">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnWS3yUaAPN7HGjBinuqvEwO0i2Yzj0LwRDHF_nC0cKjILMIUhhddhajYlNElEo3n5RkTzNcQgcVYSijOYpJCL_2MEpz34waC1aKvhTzeKxu8ZO3CWaxrM4ZmVOOsLGqMHHPzZigN4C6ptPvATjQTxvoMn0BC0yFqEK-V5oivUNYWvsaD-AbCbRvfnuVwTUhjrEKJNwF9fsalGIc3LJ50UDqQcx8fv5i_dvmhx5lkUYW6ZtspYilf8zFtuV7UyasVZjPz2rgMl5c1anB5ytsubjcn_ApHnnOeAjR9LMmjqNUEqC2D5W6DxmImMCVfRIVdg2qLWkjmatElXxgmzbhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش قیمت تتر در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139337" target="_blank">📅 12:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139336">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سخنگوی ارتش: از فرصت آتش‌بس و تفاهم‌نامه برای واردات تجهیزات و بازسازی توان رزم ارتش حداکثر استفاده را کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/139336" target="_blank">📅 12:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139335">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
اسرائیل سه شرط در مورد توافق با حماس مطرح کرد:
🔴
اول: مخالفت با انبار کردن سلاح‌ها به جای نابودی آنها.
🔴
دوم: مخالفت با مشارکت قطر و ترکیه در مکانیسم تأیید توافق.
🔴
سوم: عدم محدود کردن آزادی رفت و آمد اسرائیل در غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/139335" target="_blank">📅 12:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139334">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
خبرگزاری عراقی «نایا» گزارش داد که نیروهای آمریکایی مستقر در پایگاه عین‌الاسد در غرب عراق، عملیات هلی‌برن انجام داده و سپس به‌سمت منطقه بیابانی «النخیب» در غرب این کشور حرکت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139334" target="_blank">📅 12:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139333">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4BbFlCY-uGGPkhT_sSD1OSVFwFe50rrZWPMfX1N4Y8dMB9AnqAVMXMDuDpKUow-CrObiGiduV8Wi8YZHj98PF2CWnOrLnqeU9l5LtJ03Y8CjlLSc3w6bop32fNJRKKKSWIrHM3N0MBIjBHeOxoIXCowRFtkKD4zw8PlXIcLMG4-yCpRypEitSljjon-t4Tp4r817WRfvTsl8Z3UouHrNcs6ZXtNG7V5o13y8tTr3gO449samivifDurx7PfhQhs2mxlsLF-85QEGMER3B_A9-tpIjgB7MACXugU9fmKMs6souEVj-d9NB2lNiKCS1ddRC35JyvNqDupfH7yrRH0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری عراقی «نایا» گزارش داد که نیروهای آمریکایی مستقر در پایگاه عین‌الاسد در غرب عراق، عملیات هلی‌برن انجام داده و سپس به‌سمت منطقه بیابانی «النخیب» در غرب این کشور حرکت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139333" target="_blank">📅 12:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUPj6vo0XKJ8bThd8BWSHRsM6iM7UqQOdzcJF29D50-fx9LpmfPHrJjOV0eCnh4VvzvdY_iGPSbkV_o1nMRETw9DaXxaZNrqEMTZTvHoAFb-ALPwC0WWM2kDKyiuL2eIR4De_xtkDi2NsKDwJiIWfRgDzaPZr-tZG4X8HSdrxqrRbxNPahrkYDs5B85l9X5M7JiLzuadpdEeoK6MTYxyzViSLmKY8WwblzaM5CPVwaGDYRDXKG3cTTVtb5o6QoGuWpYEVyC2JRaXxxrI1UZYCViqJI5k-a2MzJdPqY41nQSq1sX-wkXpnbAZ7XnJLrTs-mK0lBKGpTMJ-ujjkUXe7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین یکتا: باید انتقام آقا رو بگیریم تا امنیت امام زمان رو تامین کنیم
#بدعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139332" target="_blank">📅 11:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139331">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
الجزیره: ایران در حال بررسی یک پیشنهاد جدید آمریکا برای کاهش تنش‌هاست
🔴
شبکه الجزیره گزارش داد که ایران یک پیشنهاد از سوی ایالات متحده دریافت کرده که می‌تواند به کاهش تنش‌های کنونی منجر شود.
🔴
بر اساس این گزارش، تهران با جدیت در حال بررسی این پیشنهاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139331" target="_blank">📅 11:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139330">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تو کربلا صدای دسته ایرانی‌ها رو قطع کردن چون بجای نوحه برای امام حسین نوحه سیاسی میخوندن
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139330" target="_blank">📅 11:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139328">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
همشهری: از مجتبی خامنه ای هیچ صدایی منتشر نمیشه؛ چون آمریکا و اسرائیل از روی صدا هم همه چی رو میفهمن و جاشو پیدا میکنن. فقط ۲ یا ۳ نفر با مجتبی خامنه ای ارتباط دارن. اون احتمالا توی کوه های قم یا تهران قایم شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139328" target="_blank">📅 11:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139327">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835653bd72.mp4?token=MDeBSGwSQ32pgIk05WYg_6ERs85X2i-IRAtVuSax81i_Lg_jsC6oC7cIdaGcrbuXR0uQ7Rj9V_ul64-zY1aulud82jXG9NuA4a7v2Gq2mIqDf2HXFHSpzwnIFPH4013iDcHumf_Rq1iSMIf7hLZ0S2HaqOSZOVIpmCn2fDdZ6YPGJgMwuH2-qnXM6gHS2ESjQeZjwhs3M7DWEJ1a_w9_z5zI2R0MgcK9wMVELrMlMHmvrYOnNYMcbKJFbSc9uEm2b5rihgbfl7VmKuGFHPu_OpuY_1Si2Rz6MnomQ7i8hl-Kf3kI3z1BT4uS04R4S36MTe-opHXWep-grEGjIRaVpBROUXB5ujg9YlcvY6U4gGnaALx_Qe8SBMtjSzeM90iZE-EUPu9BjyLRfKPJaQcy2F0AIQOSEV8Yb_676SxgwtsXk4m4aDl28q_ZnbKXWN6vyrZRPNO_XSKbyyC93q7sX46UANPFO8vcvsY2LN-DPnaKRtrarH78cP0iWaRM4hwHgcndRKRLd2VSOwcVuB5Pf6GzyWg1V6s_eweVwi6eJ_0Ko0uIzjtwORMhpUEvPY4dB0-kd4VlAK5netZSDdMebH4CRx6KhRZu9KWOCq7QrRWijFM0mtW45pwEIhb4x-JcTFhlQN4BK67efvIA929gYQHd1_4OKGM9mkbyZQY9ne4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835653bd72.mp4?token=MDeBSGwSQ32pgIk05WYg_6ERs85X2i-IRAtVuSax81i_Lg_jsC6oC7cIdaGcrbuXR0uQ7Rj9V_ul64-zY1aulud82jXG9NuA4a7v2Gq2mIqDf2HXFHSpzwnIFPH4013iDcHumf_Rq1iSMIf7hLZ0S2HaqOSZOVIpmCn2fDdZ6YPGJgMwuH2-qnXM6gHS2ESjQeZjwhs3M7DWEJ1a_w9_z5zI2R0MgcK9wMVELrMlMHmvrYOnNYMcbKJFbSc9uEm2b5rihgbfl7VmKuGFHPu_OpuY_1Si2Rz6MnomQ7i8hl-Kf3kI3z1BT4uS04R4S36MTe-opHXWep-grEGjIRaVpBROUXB5ujg9YlcvY6U4gGnaALx_Qe8SBMtjSzeM90iZE-EUPu9BjyLRfKPJaQcy2F0AIQOSEV8Yb_676SxgwtsXk4m4aDl28q_ZnbKXWN6vyrZRPNO_XSKbyyC93q7sX46UANPFO8vcvsY2LN-DPnaKRtrarH78cP0iWaRM4hwHgcndRKRLd2VSOwcVuB5Pf6GzyWg1V6s_eweVwi6eJ_0Ko0uIzjtwORMhpUEvPY4dB0-kd4VlAK5netZSDdMebH4CRx6KhRZu9KWOCq7QrRWijFM0mtW45pwEIhb4x-JcTFhlQN4BK67efvIA929gYQHd1_4OKGM9mkbyZQY9ne4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همشهری:
از مجتبی خامنه ای هیچ صدایی منتشر نمیشه؛ چون آمریکا و اسرائیل از روی صدا هم همه چی رو میفهمن و جاشو پیدا میکنن. فقط ۲ یا ۳ نفر با مجتبی خامنه ای ارتباط دارن. اون احتمالا توی کوه های قم یا تهران قایم شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139327" target="_blank">📅 11:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139326">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
کان نیوز: نتانیاهو و کابینه اش از تصمیمات لحظه ای ترامپ کلافه شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139326" target="_blank">📅 11:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139325">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
منابع نظامی در یمن اعلام کردند که نیروهای مسلح یمن با عناصر وابسته به عربستان در جبل هان واقع در غرب شهر تعز درگیر شدند.
🔴
همچنین گزارش شده که در این درگیری ها حملات توپخانه‌ای نیز صورت گرفته است. این درگیری‌ها به منطقه الصلو در جنوب شرق تعز نیز کشیده شده‌ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139325" target="_blank">📅 11:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139324">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
یافته‌های جدیدترین نظرسنجی ملی مرکز افکارسنجی دانشجویان ایران (ایسپا) نشان می‌دهد ضریب نفوذ اینترنت در میان جامعه بالای ۱۵ سال کشور به ۸۹.۳ درصد رسیده، به‌طوری که معیشت و درآمد بیش از نیمی از کاربران به فضای مجازی وابسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139324" target="_blank">📅 11:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139323">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83658f6aed.mp4?token=fKv9YJV9oAGUowASi90K6dvvQ5rrGok5TQ96QMSoRdF6ZYTEwaZn7qax3MDUx-mm260cVHjGNF6LdKYAW_sjlWNPLa3yP5gsJkT89A0yt_yvl7_Fucsnv9U5QYr-Khs51pH_x5DnFZdI8owaj5BkhPfOl-HaEOnimSKyALcB1gkAWRUZuOjoGnsxVuuxR1n8TqKm366Rr0IgaPiqUBiO5kYfGAc1FSHc83HfhGN4-BKvXzgX3awIilwKlLJAWWQJExDBQyLSK-EUgH1vTkX_c9EGOKu3k6ie99JQg03rMYmRuHzZOH6BO_oC7rXFUHwqrtnpYZrPg8u09YVPArijZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83658f6aed.mp4?token=fKv9YJV9oAGUowASi90K6dvvQ5rrGok5TQ96QMSoRdF6ZYTEwaZn7qax3MDUx-mm260cVHjGNF6LdKYAW_sjlWNPLa3yP5gsJkT89A0yt_yvl7_Fucsnv9U5QYr-Khs51pH_x5DnFZdI8owaj5BkhPfOl-HaEOnimSKyALcB1gkAWRUZuOjoGnsxVuuxR1n8TqKm366Rr0IgaPiqUBiO5kYfGAc1FSHc83HfhGN4-BKvXzgX3awIilwKlLJAWWQJExDBQyLSK-EUgH1vTkX_c9EGOKu3k6ie99JQg03rMYmRuHzZOH6BO_oC7rXFUHwqrtnpYZrPg8u09YVPArijZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رقابت در اوج؛ چین با پرواز موفق «پلاتو»، مستقیماً به جنگ انحصار ایرباس در ارتفاعات رفت
🔴
این پرنده جسور، برای تسخیر دشوارترین مسیرهای کوهستانی طراحی شده است. چین با داشتن بیشترین تعداد فرودگاه‌های مرتفع جهان، حالا بازار عظیم و تکنولوژی بومی را به عنوان برگ برنده در دست دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139323" target="_blank">📅 11:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139322">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQyHfLjKWGPw1oTuUB01xXT4Mv13P2bF-rP9uBxa0FRzmWsUPm1CeJNstga98iTQ-PDF3aJCX1yrDKcUt4SgGLjmfyIPVfqbrTYfBzQpITfoSPUrHyUE-OgILkstBDZJ8bDMrohefVZd2l6kdUNJDZlsFfHA0sH8GGCZdAhL0fra2Tdwj9XyQ9vgkRqTKbTmMSGavdvoICTO6yk5aWHHTr0AzGzKBT-63wBd5Qp14n8FLtmXaexPbB4dQGgDe_yq_eowPvIRb26RvAxqMYvXMw4G5PycRlq053EALGc9SrpFjIW0BZZIsGn70BmCpq35h3k4Wo_HwABzDukQ8Xj34g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۲ عبری : عراقچی با توافقی که قطر و آمریکا برای باز شدن تنگه پیشنهاد داده بودند
🔴
موافقت کرده و به‌دنبالش ترامپ هم حمله‌ای که قرار بود به ایران انجام بده رو لغو کرده
🔴
طبق این توافق، کشتی‌ها از سمت ایران وارد خلیج فارس می‌شن و از سمت عمان خارج می‌شند
🔴
عمان هم موافقه، اما خواسته مطمئن بشه سپاه هم به این توافق پایبند می‌مونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139322" target="_blank">📅 11:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139321">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0nCGjWHlcTTwGedHVaxcEdsyuSbjpjTAhjtJXVOhcFm3ELx0kPLN-OeXeX-IaBqsv8cHsy-GDC-UF9Kr_5AvOEDtG5GNy4nG1n5Rj9Sc0mvVfVzkBar-SxMr4-OQTqagaDNOT-4p36mcgxL07Ge1xIK6yXb3RwhtYdIT2eeyL1du9G_jaap-t6VmANJgmL4BvgNsDFr8nFSgQcZVOCHNyp_pxhhmIHGghO4k0a0CRRm7bw8QdMwLR8ajzT7kVq3On2a36NP-qLuCpxUB0Y1pUhR1CK2PEXuu9LQ0C59NgHPYJkIJOQ9s_WPVrzaWMAF1DI3BdnJtQYOS5sqxViM9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنوب لبنان دیشب
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/139321" target="_blank">📅 11:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139320">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دولت ارمنستان استعفا کرد
🔴
نخست وزیر ارمنستان: طبق قانون اساسی ارمنستان، در اولین روز جلسه مجلس ملی، دولت استعفای خود را به رئیس جمهور تقدیم می‌کند.
🔴
رئیس جمهور طبق قانون اساسی استعفا را می‌پذیرد
🔴
اعضای دولت تا زمان تشکیل دولت جدید به انجام وظایف خود ادامه خواهند داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139320" target="_blank">📅 11:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139319">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
منابع عبری : اعلامیه ترامپ مبنی بر لغو حمله، بار دیگر نشان داد که نفوذ نتانیاهو بر رئیس جمهور آمریکا تا چه حد کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139319" target="_blank">📅 10:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139318">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری /  باراک راوید از اکسیوس: ایران با طرح بازگشایی تنگه هرمز موافقت کرده است
🔴
به گزارش باراک راوید به نقل از دو دیپلمات آگاه، عباس عراقچی وزیر امور خارجه ایران، بامداد امروز با طرح مصالحه‌ای که با میانجی‌گری قطر و آمریکا برای بازگشایی تنگه هرمز تدوین شده بود، موافقت کرده است.
🔴
بر اساس این گزارش، موافقت عراقچی یکی از دلایلی بود که دونالد ترامپ را به لغو حمله برنامه‌ریزی‌شده علیه ایران ترغیب کرد.
🔴
طبق این پیشنهاد:  ورود کشتی‌ها به خلیج فارس از طریق آب‌های سرزمینی ایران انجام می‌شود.  خروج کشتی‌ها از خلیج فارس از طریق آب‌های سرزمینی عمان خواهد بود.
🔴
همچنین میانجی‌های قطری همچنان در حال رایزنی با تهران هستند تا اطمینان حاصل کنند که سپاه پاسداران نیز از این توافق حمایت می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139318" target="_blank">📅 10:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139317">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فایننشال‌تایمز در تحلیلی نوشته ایران با عبور از واکنش دفاعی و گسترش درگیری به پایگاه‌ها و مسیرهای حیاتی کشتیرانی، ابتکار عمل را در تقابل با دولت ترامپ به دست گرفته است.
🔴
به باور نویسندگان، هدف تهران فرسوده‌کردن توان آمریکا، افزایش هزینه حضور منطقه‌ای آن و سلب اختیار واشنگتن در انتخاب میدان نبرد است؛ از تنگه هرمز و دریای سرخ تا کانال سوئز.
🔴
این راهبرد پرریسک است، اما یک پیام روشن دارد: جنگ دیگر فقط جایی رخ نمی‌دهد که آمریکا انتخاب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139317" target="_blank">📅 10:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139316">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
روبیو: ایران تحت فشار واشنگتن، بیش از هر زمان دیگری آماده توافق است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139316" target="_blank">📅 10:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139315">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
الجزیره: ایران یک پیشنهاد از سوی آمریکا دریافت کرده که می‌تواند به کاهش تنش‌های کنونی منجر شود و تهران با جدیت در حال بررسی آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139315" target="_blank">📅 10:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139314">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
روزنامه عبری هاآرتص: رئیس‌جمهور آمریکا به مهارت‌های خود در ساختن معاملات افتخار می‌کند اما در نهایت استاد لفاظی‌های توخالی است.
🔴
او مسائل را تا آخرین حد پیش می‌برد به این امید که ابتدا طرف مقابل عقب‌نشینی کند.
🔴
سپس پیروزی بزرگی را اعلام می‌کند و با اصرار سایر طرف‌ها به ایرانی‌ها فرصت دیگری می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139314" target="_blank">📅 10:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139313">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
یکی از نهادهای امنیتی هلند در گزارش جدید خود اسرائیل جزو طرف‌هایی که نگرانی‌های امنیتی برای هلند ایجاد می‌کنند، طبقه‌بندی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139313" target="_blank">📅 10:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139312">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf749ff64.mp4?token=KUMtivegGWefPc3eFW7c33ag2RtWnTsdRvA0rYhr5xPJbJbZikkaR1yabvnLBr2A1pC-Tf4qqlGmV6TDzHBFrzFIyxyy9qCEngk3SeTCgeEUOCdn_A-eNpqTZlbvGKwZC93wU2asVfrOiKiflSek8_jMFk18ykruz40E9vb9-ZO_Kb_S-a9sBi-1HjQVktaeXS6Nhty92IkuwdwDe4msMH-fsi0lda52yC81C91JK0JLIMrR1S3_etsuwOlWxx_AyHfA7N8ABGm6JbVWhEqi8xIZmg0e_a9yMjMcJFMBvkc117Dg-0XopsuBQDAa70zvDpiMnocHfiiNbYzXrI0mOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf749ff64.mp4?token=KUMtivegGWefPc3eFW7c33ag2RtWnTsdRvA0rYhr5xPJbJbZikkaR1yabvnLBr2A1pC-Tf4qqlGmV6TDzHBFrzFIyxyy9qCEngk3SeTCgeEUOCdn_A-eNpqTZlbvGKwZC93wU2asVfrOiKiflSek8_jMFk18ykruz40E9vb9-ZO_Kb_S-a9sBi-1HjQVktaeXS6Nhty92IkuwdwDe4msMH-fsi0lda52yC81C91JK0JLIMrR1S3_etsuwOlWxx_AyHfA7N8ABGm6JbVWhEqi8xIZmg0e_a9yMjMcJFMBvkc117Dg-0XopsuBQDAa70zvDpiMnocHfiiNbYzXrI0mOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: حکومت ایران باید تغییر کند؛ ممکن است سرنگونی رخ ندهد، اما خود حکومت باید تغییر کند؛ آنها می‌خواهند انقلاب را صادر کنند؛ این موضوع حتماً باید تغییر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139312" target="_blank">📅 10:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139311">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نیویورک تایمز: مقام‌ها و تحلیلگران غربی معتقدند که از دیدگاه متحدان آمریکا، جنگ با ایران ظاهرا به سمت شکستی راهبردی پیش می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139311" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139310">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
روزنامه نیویورک تایمز گزارش داد که هم‌پیمانان آمریکا نسبت به این موضوع که جنگ با ایران به سمت یک شکست راهبردی سوق پیدا کند نگران هستند.
🔴
هم‌پیمانان آمریکا می ترسند که ناتوانی در ایجاد تغییری پایدار در ایران، نقطه‌ ضعفی را آشکار کرده باشد که روسیه و چین از آن استقبال خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139310" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139309">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ایهود باراک، نخست وزیر اسبق اسرائیل:
توافق با حماس کاملاً اسرائیل را نادیده می‌گیرد و شامل خلع سلاح این گروه نمی‌شود
🔴
حقیقت تلخ این است که ترامپ به نتانیاهو توجهی نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139309" target="_blank">📅 09:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139308">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/302146c665.mp4?token=InaW20he6voybdPohebN05vbakGebFbI8OpCFn5YtAFWT1D11VojljSuxdLgi1i3kk1NZU057msiSM3pfyM0Wa7SrQPK4cVa5RL36LvbJN97dsqkVbEv8NbPX0audDvGefKPAwRIM8skfwzOfsdglTGbaHOUJkJC_xrumgbo102LcUtWiXaQzM9531EohfvZ2tJwZkMN6kvqYTMq30ymWkb8hgwOR_PM7DGoI9Cid1T2oEr-ML5p3M3iZu43AIhGJbsEAwt8Vny2lvg-RoYzOjXxtT76sNAENZPRyr6oo-bDCtP3HIbCldZkIcZ5NaLVMQjiUpOD5lf4eJ2EhIsgRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/302146c665.mp4?token=InaW20he6voybdPohebN05vbakGebFbI8OpCFn5YtAFWT1D11VojljSuxdLgi1i3kk1NZU057msiSM3pfyM0Wa7SrQPK4cVa5RL36LvbJN97dsqkVbEv8NbPX0audDvGefKPAwRIM8skfwzOfsdglTGbaHOUJkJC_xrumgbo102LcUtWiXaQzM9531EohfvZ2tJwZkMN6kvqYTMq30ymWkb8hgwOR_PM7DGoI9Cid1T2oEr-ML5p3M3iZu43AIhGJbsEAwt8Vny2lvg-RoYzOjXxtT76sNAENZPRyr6oo-bDCtP3HIbCldZkIcZ5NaLVMQjiUpOD5lf4eJ2EhIsgRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: ما تصمیماتی گرفتیم که به کشورمان آسیب زد؛ مثلا گفتیم «برای ما مهم نیست که کالاها کجا ساخته می‌شوند؛ بگذارید در کشور دیگری ساخته شود، مادامی که قیمت‌ها برای آمریکا ارزان‌تر باشد»
🔴
این کار به صنعت‌زدایی از کشورمان و از دست رفتن میلیون‌ها شغل انجامید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139308" target="_blank">📅 09:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139307">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سی‌ان‌ان‌: عربستان به عنوان یک متحد کلیدی آمریکا در خلیج فارس، نفوذ قابل توجهی بر ترامپ دارد
🔴
وابستگی دیپلماتیک واشنگتن به ریاض در خاورمیانه، تأثیر زیادی بر تصمیم ترامپ برای عدم حمله به ایران داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139307" target="_blank">📅 09:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139306">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a01601cdd0.mp4?token=Ms-B0LqIqDTlIOGDXrgrm1BNTT7P5HlaV41pLfsctOhKvSLvMEit5piYXJorNrJzoAfb8BpHHcEPEfrIMuAyzeFYWq5p5-aIjU1fDXz9Bso5SSp9ZwSK56ATfddNTb8JL-HCZusI35pQCmcZ8lYrud0gzw1F2GXA3pjVKJz-nfII_pEqTITF55p5c04jDvjMkKKdJ83W2t3e-2TxnZk4Jdh9_g7_LV74HITRZ9jfdPntvd3agx3OkFjkJMj9rYZRw5JU4NsItJ9Texjis2FYJDAadZVVM5mDRyYzCbCElvNu6MxDmOIpMvJeiHvy9AfGMmtiHIYo57k2M_N7RbK7TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a01601cdd0.mp4?token=Ms-B0LqIqDTlIOGDXrgrm1BNTT7P5HlaV41pLfsctOhKvSLvMEit5piYXJorNrJzoAfb8BpHHcEPEfrIMuAyzeFYWq5p5-aIjU1fDXz9Bso5SSp9ZwSK56ATfddNTb8JL-HCZusI35pQCmcZ8lYrud0gzw1F2GXA3pjVKJz-nfII_pEqTITF55p5c04jDvjMkKKdJ83W2t3e-2TxnZk4Jdh9_g7_LV74HITRZ9jfdPntvd3agx3OkFjkJMj9rYZRw5JU4NsItJ9Texjis2FYJDAadZVVM5mDRyYzCbCElvNu6MxDmOIpMvJeiHvy9AfGMmtiHIYo57k2M_N7RbK7TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط مرگبار هواپیمای گردشگری در پرو با ۱۳ کشته
🔴
در پی سقوط یک فروند هواپیمای گردشگری در جنوب پرو، دست‌کم ۱۳ نفر جان خود را از دست دادند.
🔴
این هواپیمای سبک که برای پرواز گردشگری بر فراز خطوط باستانی نازکا به پرواز درآمده بود، با ۱۳ سرنشین دچار سانحه شد و سقوط کرد.
🔴
تصاویر منتشرشده از محل حادثه، تلاش نیروهای آتش‌نشانی برای مهار آتش و خاموش کردن بقایای هواپیمای سقوط‌کرده را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/139306" target="_blank">📅 09:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139304">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0109ff6de4.mp4?token=Z3bFvAOTr3fyqXnZDVR1YDsWGwCr1aieQLKzd1xuR7dYYYAQXsQ1R0lnjwmL_wAzUoOFQywajCwmj5t6zFCFjN5KopHDG3JV9ouyPo27vcukmGC_rK0YbR2R24Qi_wFXRio-Dn4kr9NT5PJ3Hv_8ZC8xjm3VLlVJ8GKgZ_oPd-YLLOAaCOTtEV9qYpahIJHhOvSukGbf8eiKYaxJTMwGcuhl2SUB4PDmuR5ZObJ8DZkeECRL1D0ZNTnaHemmzGin-FJQpro7jERRBV9OsLeGiHrNSL3rl7BQoEZKLjpeXcjzCMOgWocBoRQuIuugkXK80DClcR1iHJ4hphOe_0o8xA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0109ff6de4.mp4?token=Z3bFvAOTr3fyqXnZDVR1YDsWGwCr1aieQLKzd1xuR7dYYYAQXsQ1R0lnjwmL_wAzUoOFQywajCwmj5t6zFCFjN5KopHDG3JV9ouyPo27vcukmGC_rK0YbR2R24Qi_wFXRio-Dn4kr9NT5PJ3Hv_8ZC8xjm3VLlVJ8GKgZ_oPd-YLLOAaCOTtEV9qYpahIJHhOvSukGbf8eiKYaxJTMwGcuhl2SUB4PDmuR5ZObJ8DZkeECRL1D0ZNTnaHemmzGin-FJQpro7jERRBV9OsLeGiHrNSL3rl7BQoEZKLjpeXcjzCMOgWocBoRQuIuugkXK80DClcR1iHJ4hphOe_0o8xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای حمله‌ای اوکراینی امروز صبح به یک مرکز توزیع دیگر Wildberries در نووسمئیکینو، منطقه سامارا حمله کردند و باعث ایجاد آتش‌سوزی بزرگ در این تأسیسات شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/139304" target="_blank">📅 09:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139303">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6667d80879.mp4?token=YXM8wTxcJQ1ygqhSzfuWN7sEc539_AWq2WBCQMRxf2a8QYhLLWBdqgVFrxBaiYA7zgrR3OTtzA56fQ5s53RwRfBilrfBo7WD1nZK_4PN_di6lp8dOUy-z3uv_q5u5U5ymNMjD3PbVb1ehfbivKXWduIgtRpui4MYSFFi3duC5UpB8QT_eXfHwSKUod1RMpegU1c00WPiUlKD1l9TCWxwYFqv3K9UhzGLx9K07yEAwusls5pKZawBkrcNt-7eorVAFC23oQg4DFCGqm9xsccGDV6qqbIcbB6X5y4pgUGNZaKnmyY_jxtSI4LHUqeCgYX026rLBgK290hoSnSl-gA6ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6667d80879.mp4?token=YXM8wTxcJQ1ygqhSzfuWN7sEc539_AWq2WBCQMRxf2a8QYhLLWBdqgVFrxBaiYA7zgrR3OTtzA56fQ5s53RwRfBilrfBo7WD1nZK_4PN_di6lp8dOUy-z3uv_q5u5U5ymNMjD3PbVb1ehfbivKXWduIgtRpui4MYSFFi3duC5UpB8QT_eXfHwSKUod1RMpegU1c00WPiUlKD1l9TCWxwYFqv3K9UhzGLx9K07yEAwusls5pKZawBkrcNt-7eorVAFC23oQg4DFCGqm9xsccGDV6qqbIcbB6X5y4pgUGNZaKnmyY_jxtSI4LHUqeCgYX026rLBgK290hoSnSl-gA6ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل شدید در شهر شی‌آن واقع در شمال چین
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/139303" target="_blank">📅 09:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139302">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزارت دفاع روسیه: از دیشب تا حالا ۶۳۵ پهپاد اوکراینی را بر فراز شهرهای مختلف روسیه سرنگون کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139302" target="_blank">📅 09:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139301">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWbLkPHBpfMmZZhXGmipSnZc0JiYfkaaj3nxYB9WwHONAN2VeD111lAMzJFhtSN_Bacgo-cfVkoJ7JHSVYvSvHw0tlI--ukR4D2TTd6yZE1RbGW0Al2LyGBdiAJjE4k02-3LIqA7DSpu7q3uOyXZUrNm-u-md8FqFgeG0IxVRWv91hOfFdWDE7DR9zReC7K61inDOdI89Val1EC5KWxcz9YtrxP4PaXdrywNvev4kiq89h5oaqhBMaK7WHBtRwgcFLqZJcOdwNbh3X4cU7Uj5Q2Kv02BvxnxfrCs1xxOd1MqMlF6iQxVtOgkhfzR6dV8xiruXnSXZcbBU6TXhh39UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی، مشاور تیم مذاکره‌کننده ، در واکنش به سخنان ترامپ گفت: همه می‌دانند که این یک خبر دروغ است، ترامپ عقب‌نشینی کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139301" target="_blank">📅 09:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139300">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
اکسیوس: محمد بن سلمان، ولیعهد عربستان، امروز پیشتر با ترامپ گفتگو کرد و از رئیس‌جمهور خواست تا تنش‌زدایی کند و از انجام حملات به ایران خودداری کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139300" target="_blank">📅 09:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139299">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ارتش کویت اعلام کرده چند پهپاد ایرانی را در شمال این کشور رهگیری و منهدم کرده و ترکش آن‌ها در جزیره بوبیان، نزدیک پایگاه‌های نظامی آمریکا، فرود آمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/139299" target="_blank">📅 09:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139295">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5b32c7f4d.mp4?token=OmqcOh8IKnc5CJlRAF_4q7yNwlWSMRkV_NQDd5EG0fVAz4FCMbBGZ-4YM8A1OTM0zn2naa-22fXQUm_ml5HdhO7Rs3lKG2VxsWwEtgL9SK0EqhlmCjmR-KiUWUzXWotL9lkzAOQaadC9eeo2p1FwEXS_LwxUws9uVawXwWK-wP4uhaXjfkUKJBC7SSP5xk-jn-UHIFSwtGbGZMiiPfXyfZOdu_V4K782npYNbeBHeRBy5ic5TZ8NPv4fcgn6M1r1joPypQh9FhrLm8AQBtsomnKOyiA4hwobosK0Y4_VBBtY7mYjdDJ6l6fNY6JXaorG04MGwIa-0xmkWLSboD8a9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5b32c7f4d.mp4?token=OmqcOh8IKnc5CJlRAF_4q7yNwlWSMRkV_NQDd5EG0fVAz4FCMbBGZ-4YM8A1OTM0zn2naa-22fXQUm_ml5HdhO7Rs3lKG2VxsWwEtgL9SK0EqhlmCjmR-KiUWUzXWotL9lkzAOQaadC9eeo2p1FwEXS_LwxUws9uVawXwWK-wP4uhaXjfkUKJBC7SSP5xk-jn-UHIFSwtGbGZMiiPfXyfZOdu_V4K782npYNbeBHeRBy5ic5TZ8NPv4fcgn6M1r1joPypQh9FhrLm8AQBtsomnKOyiA4hwobosK0Y4_VBBtY7mYjdDJ6l6fNY6JXaorG04MGwIa-0xmkWLSboD8a9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طوفان آتش در شرق واشنگتن؛ هشدار تخلیۀ فوری صادر شد
🔴
در میان وزش بادهای سهمگین با سرعت بیش از ۷۰ کیلومتر بر ساعت، آتش‌سوزی مهیبی شرق واشنگتن را درنوردید و هزاران نفر را مجبور به فرار از خانه‌هایشان کرد.
🔴
خبرگزاری آسوشیتدپرس گزارش کرد این آتش‌سوزی حوالی ظهر شنبه به وقت محلی آغاز شد و علف‌ها و بوته‌های یک محوطه باز را سوزاند اما به‌سرعت به‌سمت شمال و شرق و به‌ سوی مناطق مسکونی گسترش یافت.
🔴
مقامات محلی، با اعلام بالاترین سطح هشدار تخلیۀ فوری، خطوط اتوبوسرانی شهری را برای خارج کردن مردم فعال کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139295" target="_blank">📅 08:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139294">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
کیهان: دولت پزشکیان «آرایش جنگی» ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139294" target="_blank">📅 08:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139293">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: سال تحصیلی جدید، از ابتدای مهر و به صورت حضوری آغاز می‌شود
🔴
اگر اتفاق خاصی رخ دهد، متناسب با شرایط درباره آن تصمیم‌گیری خواهد شد
🔴
تصمیم‌گیری درباره زمان آغاز فعالیت دانشگاه‌ها در حوزه مسئولیت ما نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139293" target="_blank">📅 08:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139292">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
المیادین: تعلیق حمله آمریکا به ایران پس از تلاش‌های جی‌دی ونس، معاون رئیس‌جمهور، و رئیس ستاد ارتش آمریکا برای منصرف کردن ترامپ از این کار صورت گرفت
‏
🔴
موضوع کمبود ذخایر موشکی عامل کلیدی در تصمیم ترامپ برای تعلیق حمله به ایران بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139292" target="_blank">📅 08:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139291">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
روزنامه جمهوری اسلامی: برخلاف عده‌ای جنگ‌طلب، مردم و نیروهای مسلح دنبال صلح شرافتمندانه‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139291" target="_blank">📅 08:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139290">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6b-TnWfZYfukdRqnXovnehTNnqdPiveQUHoarFQV4Iq8dU63Af4zugxneNrUmdB1x10Ao18a9x_k-KIKYfJhgYFCtdQ7XdjGnQjWbh2omm72G78vJ6cccJ19vA7VAgbAHKbMHx749T-OhZlgK7k4-qt7bFKWdK2LC0VUbEiaUiH90f_kk8TWKKl4B0E1grCTxdnS4SYcZ0bKs5fDYGJQH7_SckBrQgLbdKxDPf_vf3U8jNesfqyYNq1xQuI_dIgN9U2MT56Hc6kqUJlJQqMuLfKvBgfCIpvD-zr-mxLiuylaP267VTtdzUPPR5RQLTU-P5FHFjBXzGfWePFxkl-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ پس از تهدیدهای مداوم: با لغو حمله به تهران موافقت کردم
‏
🔴
ایالات متحده آمریکا آماده و مجهز به سلاح است تا علیه جمهوری اسلامی ایران، در سطوحی از ترور نظامی، قدرت و صلابت که از زمان جنگ جهانی دوم دیده نشده است، اقدام کند.
‏
🔴
با وجود این، ایران و سایر کشورهای خاورمیانه از ما خواسته‌اند که هرگونه حمله‌ای را در چارچوب تعهداتی که مورد توافق قرار گرفته است، متوقف کنیم. این شامل بازگشایی فوری، کامل و بی‌قید و شرط تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران می‌شود.
‏
🔴
بر اساس این درخواست، من برای منافع آینده جهان و همچنین بقای یک ایران موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانم به سرعت به توافقنامه‌ای دست یابم. کشور اسرائیل در این تعهد به من می‌پیوندد. همه دست به کار شوید و آن را انجام دهید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/139290" target="_blank">📅 08:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139289">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60057c65fc.mp4?token=t2j8ZzWtTRRgI0QhjS3h_sKYL4kbMmrNOVSyEqCnZMQwDnjvJaZhDi-i4x790kIjy_t7VV1cmqsTtU8JYoRO6zn7-8qE_nsRRAlyx3XD4uYS20FSf7s53zDiBbA7CCfZb-dUT0N_A8tP8zWsOMSQ_uB98i0Ky3DOwO218ql6DV2zzxECW-eiKV4TXFussovwCM9r8hi2c-AvBqPaxUgfacApxI5zDu4xwwV5JYQxBtK9gWWQxYO2VMge1b_5ZzZ87yy-G7GgnlwkfyqA8zqfdM51TbFEy6MnodSMNW_ihopsY_NgQxc3wrh2Ol-ZStJMvnDUC3I7G_Eve-BOtPh_f3cCFih1ne1zN1YOizONXWLxnwVsPXO5FPySEI-Ck3_f5aIPkC_q-NJ_C8OevMz88IaOA-JkWnninPlPaVFeCfH99o1AITYaNsYa1ZETp3l22UMcx57qSXhyHne4OFwobI3XG2H9KkfGJNZnPn9DomPyq3rbTJu5q8AFygBwSppHoYABEcCNwVZUHjBS5BH3eJGSY1AZMhZfcunmA_xMFb2cRsochnZHzWSZ426VvqF3nK-X0VFOGWBiYh96E9KnlUSAFIfdqGTlbZ-BGE27xjmXwMyero4jXS3dO8OTdJN4ud9thm6l4a4Ledb1043REg2K4PK1Qv2jHraWfs5DgM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60057c65fc.mp4?token=t2j8ZzWtTRRgI0QhjS3h_sKYL4kbMmrNOVSyEqCnZMQwDnjvJaZhDi-i4x790kIjy_t7VV1cmqsTtU8JYoRO6zn7-8qE_nsRRAlyx3XD4uYS20FSf7s53zDiBbA7CCfZb-dUT0N_A8tP8zWsOMSQ_uB98i0Ky3DOwO218ql6DV2zzxECW-eiKV4TXFussovwCM9r8hi2c-AvBqPaxUgfacApxI5zDu4xwwV5JYQxBtK9gWWQxYO2VMge1b_5ZzZ87yy-G7GgnlwkfyqA8zqfdM51TbFEy6MnodSMNW_ihopsY_NgQxc3wrh2Ol-ZStJMvnDUC3I7G_Eve-BOtPh_f3cCFih1ne1zN1YOizONXWLxnwVsPXO5FPySEI-Ck3_f5aIPkC_q-NJ_C8OevMz88IaOA-JkWnninPlPaVFeCfH99o1AITYaNsYa1ZETp3l22UMcx57qSXhyHne4OFwobI3XG2H9KkfGJNZnPn9DomPyq3rbTJu5q8AFygBwSppHoYABEcCNwVZUHjBS5BH3eJGSY1AZMhZfcunmA_xMFb2cRsochnZHzWSZ426VvqF3nK-X0VFOGWBiYh96E9KnlUSAFIfdqGTlbZ-BGE27xjmXwMyero4jXS3dO8OTdJN4ud9thm6l4a4Ledb1043REg2K4PK1Qv2jHraWfs5DgM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اختراع عجیب یه گیمر ایرانی که وایرال شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/139289" target="_blank">📅 08:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139288">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrFAPJMpD0BkjV7jrjm8IHFgieB6QlgMo1tM7PF18Q_DvzGWGknTa7jOl8EAmSkOr2eaePwCZcnzYC1FEXjQPeFfjJJfX3S-xN3m4xRYvpfPHX0xIijyEZpupMf0DxKOalzZMxjYcGsSvE5a2zJz0R9yvoLSR-ds4qxPCaY8i0KPfJIAUPZA88ruXsENH7n4Dfsr5MkAObc7nWiAfTyrzsgqWF1qBTPr5IVfgC8Kx9gEHbBmfEmnxLw3tfeO-7sge0LqnDBSnSzp0gxmV3Ql-v1rwxA96rHwn7et1k48u1_SiZI8Ek7CLKsOSaty3w2VRTA-HDZgadmx_dBEdW6-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس
:
محمد بن سلمان، ولیعهد عربستان، درباره طرح ترامپ برای حملات گسترده به ایران ابراز نگرانی کرد!
🔴
بن سلمان در تماس تلفنی با ترامپ خواستار جزئیات بیشتر درباره این عملیات شد و از او خواست این حملات را آغاز نکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/139288" target="_blank">📅 07:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139287">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gokUSl47mFPUwRPbC_ICrbhiEZDd5Oo0jVIPjRVFv5EC3nXyWHZCiwIBLchGh0hCPyepmj8s-XzFE5MeePgiHGGI3sWqUAgCfUGP3cngbn2cDu7yfWyfc33QZCMWKu24kafxKlidSfl0ZURnBMEKKkZanGtKzWvsxsgP0IpYrrGH_Kk1nrX4VBt20hSfsmzFYLDDFfccyX8FeSI6DcLqh8bGAZ0m7_HlvhmtXag7kAbEYImb1uI5Fbp5ALg7Lzd6s-_2OCsAfj1a0ES-c7yzoAqoCb-uiYGe9oqBSiRQL27a3mHHo6GXXRfprE2tMFLC7DDa3Ib5ohbKAOr1omvsSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : حمله کنسله و مذاکره میکنیم
آمریکا مسلح و آماده حمله به جمهوری اسلامی ایرانه، با سطح وحشتناک نظامی، قدرت و زوری که از جنگ جهانی دوم به این طرف ندیدیم.
با این حال، ایران و چند تا کشور دیگه خاورمیانه ازمون خواستن حمله رو عقب بندازیم چون چارچوب یه توافق رو قبول کردن، این توافق شامل باز شدن فوری، کامل و تمام‌ و کمال تنگه هرمز میشه و تموم شدن تهدید هسته‌ای ایران.
بر اساس این درخواست، من موافقت کردم برای نفع آینده کل دنیا و همچنین بقای یه ایران موفق و آباد، حمله رو لغو کنم، به شرطی که بتونیم سریع یه معامله ببندیم. کشور اسرائیل هم تو این تعهد با من همراهه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/139287" target="_blank">📅 07:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbefa49090.mp4?token=GtK3oUbzdWGINx9UnM2nDBesk_3ZbdFi_FAmOtaUqCU1oR74em750CvyqB7c23moNgnRxkD6PPAwUtHCVTQS9nmuM3hjY45PiszicJX1UfjShtw73Rv36UlpAJqLX4yFv7xGnHyXvZAidSp6EaIwxLDozA-IFu6OgLkOkfxxVQgPOPCoCGlQE-Ea7_5WX3oHMfku53tcVd5Yl0JYuRiTx3G9sInit3O9NxJlISWE9KjHMqz_KNckmPd-QQZREnq3t7Wv-T3IDNlWwWqFs1W08JVU1ol-EMjElGgRZWhSrcip659YZc_lOg3Uc-mJ7OycnyMvLn5h9eG8FdSsvsV83Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbefa49090.mp4?token=GtK3oUbzdWGINx9UnM2nDBesk_3ZbdFi_FAmOtaUqCU1oR74em750CvyqB7c23moNgnRxkD6PPAwUtHCVTQS9nmuM3hjY45PiszicJX1UfjShtw73Rv36UlpAJqLX4yFv7xGnHyXvZAidSp6EaIwxLDozA-IFu6OgLkOkfxxVQgPOPCoCGlQE-Ea7_5WX3oHMfku53tcVd5Yl0JYuRiTx3G9sInit3O9NxJlISWE9KjHMqz_KNckmPd-QQZREnq3t7Wv-T3IDNlWwWqFs1W08JVU1ol-EMjElGgRZWhSrcip659YZc_lOg3Uc-mJ7OycnyMvLn5h9eG8FdSsvsV83Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت سیستم دفاع هوایی C-RAM در اربیل عراق برای مقابله با پهپاد های شلیک شده ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/alonews/139286" target="_blank">📅 03:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139284">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5db8baf5ba.mp4?token=LwN8T8sH6MhYIQ2XNfFNbcHMqNEfNaa46nvGG3q0FkoVWUWWB546nO_gcDQ0NqPqp6sANX9hS5kL7iuu-n3KptZjsMQx9gDlYrRMLC6r1QkktecRb3GS4Y4GK8iK3Ox7qzYXPGCoBjufXcOUF5TDs3-1MSnZOEMsT72wUMwMVcYJoSBVI4StAU-0njLBZgvTIFWbdG_Ny9Fwgr1-3SFLe2LcbmGjCQrNRlB9Cw6AkedN56p0DkTcbDLVvSGCXi9Sl4viGX2tfGxFoHi6NuLTOIlsqDNBtkVH0fuukAVxZVAPPn_96Iqv2K0XVzWSu2QpjTq0bIjgk5wE_t9lkonNyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5db8baf5ba.mp4?token=LwN8T8sH6MhYIQ2XNfFNbcHMqNEfNaa46nvGG3q0FkoVWUWWB546nO_gcDQ0NqPqp6sANX9hS5kL7iuu-n3KptZjsMQx9gDlYrRMLC6r1QkktecRb3GS4Y4GK8iK3Ox7qzYXPGCoBjufXcOUF5TDs3-1MSnZOEMsT72wUMwMVcYJoSBVI4StAU-0njLBZgvTIFWbdG_Ny9Fwgr1-3SFLe2LcbmGjCQrNRlB9Cw6AkedN56p0DkTcbDLVvSGCXi9Sl4viGX2tfGxFoHi6NuLTOIlsqDNBtkVH0fuukAVxZVAPPn_96Iqv2K0XVzWSu2QpjTq0bIjgk5wE_t9lkonNyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداقل سه نفر در پی یک حادثه تیراندازی جمعی در شهر Twin Falls ایالت آیداهو کشته شدند و دو نفر دیگر مجروح شدند. در حال حاضر، مظنون (یا مظنونین) این حادثه دستگیر نشده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/139284" target="_blank">📅 03:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139283">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
محجوب الزویری، کارشناس الجزیره و مدیر مرکز مطالعات خلیج فارس در دانشگاه قطر:
🔴
ایران یک پیشنهاد از سوی آمریکا دریافت کرده که می‌تواند به کاهش تنش‌های کنونی منجر شود و تهران با جدیت در حال بررسی آن است.
🔴
به نظر می‌رسد این موضوع با رایزنی‌ها و تماس‌های فشرده ایران با چندین طرف بی‌ارتباط نباشد؛ تماس‌هایی که بخشی از آن‌ها، از جمله با پاکستان و ترکیه، به‌صورت رسمی اعلام شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/alonews/139283" target="_blank">📅 02:50 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
