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
<img src="https://cdn4.telesco.pe/file/rseRqp8ULYMRQ0XxW9xjCcamxCZz1gT9EF1dXN51FWiw3jZuBxSn3KGtcC9vRnOsLHfjVAl3i4PJD-vFzpbfEeKINU0B1ZnLlyMuaJWHxwKG_iIIs3yii6SBsqlRA1_iynGnEll5OUoQB5WypdUlATV0GEorTYNHcB1GGMnnGltmySGM857Zjsm009v2EfNIzNE4NDL3qHv0HZxe99AhUUfytI-Ssl9GcxqjeLU8xSI4lNVjx64g8pgzMiHB7wnIXy_MrsNxROjnCjsh38pb66wczkSUsCGH-wuDNEI7BcIcksvVQArHgAsq2f0O9UlrBiOa3yl1RTw6C6SbtqxGZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 11:42:18</div>
<hr>

<div class="tg-post" id="msg-467246">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBHz4A4fN0LpcgugVTVaoE9bSj9w_G3SEtlUVyAvu9Kc_0tOUL3ug_IJHg6mgrXLUTZvE0YHYILMCszjm6Mashri0aI9GGHmUQ2XwScP895NUegOwIPrxGnIbyLiw6u609wx_GHbXn975JG-k_Y23SZ_rIT7L8PX3HZNTzyMVSMSLAZUill0kq8BszOkOqcAZ6tFHu4j2nhNIfp67jaVhQUiLgPPKq5QG741KhFqJlAKxJ6Ce10LOI8wS0DQycxwPyKt_boUgrg8acPhF-sFqL8huAjRTpYFnXJdhj0W5auqtYf4L_XADwmcsjvKGy1bQ4bn1mN6-PhDgmigAJZKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوومیدانی‌کاران ناشنوای ایران نایب قهرمان آسیا شدند
🔹
تیم ملی دوومیدانی ناشنوایان کشورمان موفق به کسب پنج مدال طلا،‌ ۳ نقره و چهار برنز شد و با ۱۲ مدال به کار خود در این مسابقات پایان داد.
🔹
براین اساس تیم ملی دوومیدانی ناشنوایان کشورمان در رده‌بندی نهایی مسابقات بعد از ژاپن و بالاتر از هند به رتبه دوم رسید.
@Sportfars</div>
<div class="tg-footer">👁️ 419 · <a href="https://t.me/farsna/467246" target="_blank">📅 11:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467244">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44855256e8.mp4?token=jZZwAWpe2tBMrbw2Wg3M7UiKLB33M338xm9HEWT-VjKeEUL2KqXnOH_5SJMUdD56plmCW3Ll3VyTuUMOB5cre8f8Q3Bmh5owUcphgS9RAMwOMzsRef4iJoRlZCaNy_NY63xhAokI418gae-0deIr__6dmfd1qYDdQ-niZb-alJRHc0svQzb5I6mdBnaiDwNTJCad9nciOwh72wLpxA7tzENHZIu69_xYvPabFk6NfC4HTvzLduxtgbJxVocS3PHSrZaaERE-hN8TwtpyB5G_9mkmxmADYvslMOOB8NC3I1DKbExghxnm-CXPuCp2WsaJGr6IkPC3yQuuP8xZIKM48g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44855256e8.mp4?token=jZZwAWpe2tBMrbw2Wg3M7UiKLB33M338xm9HEWT-VjKeEUL2KqXnOH_5SJMUdD56plmCW3Ll3VyTuUMOB5cre8f8Q3Bmh5owUcphgS9RAMwOMzsRef4iJoRlZCaNy_NY63xhAokI418gae-0deIr__6dmfd1qYDdQ-niZb-alJRHc0svQzb5I6mdBnaiDwNTJCad9nciOwh72wLpxA7tzENHZIu69_xYvPabFk6NfC4HTvzLduxtgbJxVocS3PHSrZaaERE-hN8TwtpyB5G_9mkmxmADYvslMOOB8NC3I1DKbExghxnm-CXPuCp2WsaJGr6IkPC3yQuuP8xZIKM48g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آنچه در سفر وزیر نیرو به کابل گذشت
@Farsna</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/farsna/467244" target="_blank">📅 11:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467243">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
از هامبورگ تا دارالذکر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/farsna/467243" target="_blank">📅 11:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467242">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba130634c.mp4?token=TzpL-6MfkwEXkX7cl_GOgTwy_qmMD6koOwMsg19ARCq7rMrsDFi4YxDob4jUcmBICn3xdabYrGScs9gASKak1HfkVM_vyFU0wDYALFNuUbU5AcSlF6qtKhhnanHBkfWtDlJhZtuyZtCMe9_l_Gs6zmQ0CpOG5War96Y6oKRYk5QcNSxZaJq7MGpvCeKUlqV8WIYUwrVuZdgcA4VWqciVHH0ehS3QArw1G8WGXlYOvIzp27tRBqiubRHYIGm-KsThcZomgii-ByvA-O-j6MsK0ab3wxWovuE3pLw0YZSB8TDpUg9LWdKw1ggNwdrOODVM6gDrTdI19qMTSs5ol8Vjmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba130634c.mp4?token=TzpL-6MfkwEXkX7cl_GOgTwy_qmMD6koOwMsg19ARCq7rMrsDFi4YxDob4jUcmBICn3xdabYrGScs9gASKak1HfkVM_vyFU0wDYALFNuUbU5AcSlF6qtKhhnanHBkfWtDlJhZtuyZtCMe9_l_Gs6zmQ0CpOG5War96Y6oKRYk5QcNSxZaJq7MGpvCeKUlqV8WIYUwrVuZdgcA4VWqciVHH0ehS3QArw1G8WGXlYOvIzp27tRBqiubRHYIGm-KsThcZomgii-ByvA-O-j6MsK0ab3wxWovuE3pLw0YZSB8TDpUg9LWdKw1ggNwdrOODVM6gDrTdI19qMTSs5ol8Vjmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندگان مجلس برای حل مشکلات مردم خارگ قول مساعد دادند
@Farsna</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/467242" target="_blank">📅 11:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467241">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e8b2b99a.mp4?token=KkRQCb8Uvd4fsWFE4FtTz6cmWCQk8TlzsJWMl3T1jQcJBli-KQOySObnSj0nXHBYIGhyVJn8He8JQLgpNs5fIXZqJMnUMp8UY1g1lJwDrKgLirBQh0A1wYYIUlge_hI148ytUzLcqR0FJFqRpU8fcEt67M4oN2sH0yZ-sImOj5RIYQC_NZ0IQpOf6gtorgftpou7pYqo6WcWBQyW7JoGmxXQ0n6bjxCUXxGHOH7t6WrF1hkEp2_QOouoyNKAksk98p27Aul7EQcjqLQs5YY1VsAerl5ycwhXCfNK4sDYQwh33CM0Tp7qenPZ-FcW2x7ats8SOrmmT9IFdxVUSwrYTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e8b2b99a.mp4?token=KkRQCb8Uvd4fsWFE4FtTz6cmWCQk8TlzsJWMl3T1jQcJBli-KQOySObnSj0nXHBYIGhyVJn8He8JQLgpNs5fIXZqJMnUMp8UY1g1lJwDrKgLirBQh0A1wYYIUlge_hI148ytUzLcqR0FJFqRpU8fcEt67M4oN2sH0yZ-sImOj5RIYQC_NZ0IQpOf6gtorgftpou7pYqo6WcWBQyW7JoGmxXQ0n6bjxCUXxGHOH7t6WrF1hkEp2_QOouoyNKAksk98p27Aul7EQcjqLQs5YY1VsAerl5ycwhXCfNK4sDYQwh33CM0Tp7qenPZ-FcW2x7ats8SOrmmT9IFdxVUSwrYTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس فتای فراجا: تجارت وام در فضای مجازی ممنوع است؛ به وعده‌های وامی در این فضا اعتماد نکنید
@Farsna</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/467241" target="_blank">📅 11:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467239">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86db71c63.mp4?token=WuB7GcGD2tEwYhTtcmtz77CD-nM-0ANo4hIEaZ_8w7_ty9SU_qlOPZhEqV8kQyoODmG-fzCYJLMXMgFHa61y2qLK7eohjuqsBbOmEk78w_4Mv-IURoyWV_Fj2tY4EY1-lSuldlnRstMssSvsg_9Cjp7DTBpeq5PQoU0Cd79BQJ8tXUCh_EtTBAc_3fkAJhc-WmTWWBe0oTeQPdmo2UOp2UWhfRvXXagEP01a6kNdIdJo2FNan0T_U-c9WMXd2Q86pzD1ky-snJM58je89W2-Qis9ReJyvymBALbEnLluZHH3dG99NGjJuvxHGK19QihyH_Pfe2oGu7sXiZWMjnRRFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86db71c63.mp4?token=WuB7GcGD2tEwYhTtcmtz77CD-nM-0ANo4hIEaZ_8w7_ty9SU_qlOPZhEqV8kQyoODmG-fzCYJLMXMgFHa61y2qLK7eohjuqsBbOmEk78w_4Mv-IURoyWV_Fj2tY4EY1-lSuldlnRstMssSvsg_9Cjp7DTBpeq5PQoU0Cd79BQJ8tXUCh_EtTBAc_3fkAJhc-WmTWWBe0oTeQPdmo2UOp2UWhfRvXXagEP01a6kNdIdJo2FNan0T_U-c9WMXd2Q86pzD1ky-snJM58je89W2-Qis9ReJyvymBALbEnLluZHH3dG99NGjJuvxHGK19QihyH_Pfe2oGu7sXiZWMjnRRFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مأموران مهاجرت آمریکا باز هم به یک نفر تیراندازی کردند
🔹
یک مأمور ادارهٔ مهاجرت و گمرک آمریکا در جریان عملیات بازداشت در شهر نیویورک به سوی مردی تیراندازی کرد و او را زخمی کرد.
🔹
این حادثه‌ در پی چندین مورد تیراندازی مأموران مهاجرت به افراد در ماه‌های اخیر، بار دیگر شیوهٔ برخورد این نیروها با شهروندان و مهاجران را در کانون توجه قرار داده است.
🔸
زهران ممدانی، شهردار نیویورک در واکنش به این حادثه گفت: «دولت ترامپ فضای رعب و وحشت ایجاد کرده است» و خواستار توقف عملیات این نهاد فدرال در نیویورک شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/467239" target="_blank">📅 10:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467238">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎥
گلباران مردم توسط هوانیروز
🔸
مهمان نوازی هوانیروز کرمان در روز افتتاحیه بزرگترین پل جنوب شرق ایران که مزین شده به نام شهدای خلبان  @Farsna</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/467238" target="_blank">📅 10:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467237">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cI8JVH7WJtcAtjWWH6BmA-vwlZhdb5-y6ByJIXsGDt2TPtUBXMcABER78nhDL5y9r0MCSOkJ6hQFyCUT_bx5Qjp6wUjOtijHurCy4ZhtjEL76vYB_kqMW23VL8vSJhhrhhQhtnHbAbAvrmoflTvc0F4koI1WChclRf7NGvy7cBa81ITRkAygCwYFEQ1yV1Wlps0pNnn6Kh4AOGj-1F4ZQ-iEbgC0uCMgV7X_8z_C3BxMbjxD2sCAMR0NLpPuWAPkVXDcfVk5KL-Nl4JVU_Chk2IzyscYvXN-jXbN80fifF4_G9OGunUmd2OAbGOb5e5snLvkj2SBenQF3T9MvuwNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامزد سنا: اسرائیل قوانین جنگ و حقوق بین‌الملل را نقض کرده است
🔹
جان اوساف، سناتور دموکرات ایالت جورجیا، اعلام کرد نیروهای اسرائیلی در نوار غزه قوانین مخاصمات مسلحانه و حقوق بین‌الملل بشردوستانه را نقض کرده‌اند.
🔹
اوساف که برای انتخاب مجدد به سنای آمریکا رقابت می‌کند، روز پنجشنبه در جریان مناظره انتخاباتی درباره احتمال ارتکاب نسل‌کشی در غزه گفت که این موضوع باید از سوی دیوان کیفری بین‌المللی بررسی شود.
🔹
این سناتور دموکرات در ادامه، از مایک کالینز، رقیب جمهوری‌خواه خود و نماینده کنگره، به دلیل حمایت از اعمال تحریم علیه دیوان کیفری بین‌المللی و قطع بودجه آن انتقاد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/467237" target="_blank">📅 10:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467236">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE8ILNbmvnhAECtYB1ra0czeCdcmxc5Ed6C1CXZOxcfW3PZ9Wi2UfhrjS_kYL_LVDo13rkUsFtIrsriG-Xw6IrOckvprSaYRz-WII5amKMD-2S4wgSnAtn5p_A0dQ54--hBJJMzfoqBAjJROx89JMOXVblZzmu7ahBbrBxSuQF-8YiHjxJ7wFxuKgaCY2SPXaIt5V9ucY_s9_JzkTjCTnqp-McKpS3hTBpF-MH1mWCDKqL2H1GZrifWLx2MjjP-6IEozf6F4d42jSzJZuciakhT_hHlX_1peNeixmARtmOpcIH_C-C55xCoGh7szgBfbsB7sh_piqjlvNovUSXEmFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ میلیارد دلار ارزی که از جیب اقتصاد کشور خارج شد
🔹
در یک سال و نیم گذشته، معادل ۲۱ میلیارد دلار از ارزهای حاصل از صادرات به چرخه اقتصاد بازنگشته است؛  رقمی که ۸ میلیارد دلار آن مستقیماً به معضل استفاده از کارت‌های بازرگانی اجاره‌ای گره خورده است.
🔹
باتوجه به حجم کل صادرات غیرنفتی که حدود ۵۰ میلیارد دلار برآورد می‌شود، عدم بازگشت این رقم نشان می‌دهد نزدیک به ۴۰ درصد از کل منابع ارزی حاصل از صادرات وارد چرخهٔ رسمی کشور نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/467236" target="_blank">📅 10:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467235">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تلاش ناتو برای آرام‌کردن روسیه پیش از رزمایش اتمی در ایتالیا
🔹
پالتیکو: ناتو به دنبال اطمینان دادن به روسیه است مبنی بر اینکه رزمایش‌های نیروهای هسته‌ای در ایتالیا هیچ تهدیدی برای این کشور ایجاد نمی‌کند.
🔹
مدیر سیاست هسته‌ای ناتو ادعا می‌کند که هیچ دلیلی برای نگرانی روسیه و سایر کشورها درباره رزمایش اتمی در ایتالیا وجود ندارد.
🔸
رزمایش سالیانه «روز استوار» از ۱۳ تا ۲۳ اکتبر در ایتالیا برگزار می‌شود که برای حفظ آمادگی نیروهای هسته‌ای و تمرین رویه‌های لازم برای بازدارندگی و دفاع ناتو طراحی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/467235" target="_blank">📅 10:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467234">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74322aaf3.mp4?token=uQI1_T0WQZjGI4jaXeXzRl_9NgzuYM6i8sT64Sedo-PMi3OBYm1HArUA8qne8TCobcCELm-bvuNAjPxbTtUPaFSxnm1k1w356_cnz62JCMLJmsj0VkA0C4SM8jU76Wdb_Rn7Wkff0Vb825-feJpGSeraC5v15LDLyOysP2a7TLDLW33wzLi54qnGeS-EWp1vPFwAvX2ljTmbTZk2mWLWpcS70ckfPGl46i0tJfUfIvjUh63GCQZ3rEDI26NtvN_4dI2F6BZV9i41lqJQNym44-0pV-C8Ci0eI0o0Z_VP5CFp2NhB-tisNnP8sUMZgYhCjjO7pBX2TW_lCzbLpxm4Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74322aaf3.mp4?token=uQI1_T0WQZjGI4jaXeXzRl_9NgzuYM6i8sT64Sedo-PMi3OBYm1HArUA8qne8TCobcCELm-bvuNAjPxbTtUPaFSxnm1k1w356_cnz62JCMLJmsj0VkA0C4SM8jU76Wdb_Rn7Wkff0Vb825-feJpGSeraC5v15LDLyOysP2a7TLDLW33wzLi54qnGeS-EWp1vPFwAvX2ljTmbTZk2mWLWpcS70ckfPGl46i0tJfUfIvjUh63GCQZ3rEDI26NtvN_4dI2F6BZV9i41lqJQNym44-0pV-C8Ci0eI0o0Z_VP5CFp2NhB-tisNnP8sUMZgYhCjjO7pBX2TW_lCzbLpxm4Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور ۲۳۰ هزار نفری در پیاده‌رویِ خانوادگی کرمان  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/467234" target="_blank">📅 09:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467233">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e4c1d123.mov?token=tg1o4QD8x-qHrZj8Tq0WcxHPpFFVTFO5zu1z6WcOtFh2aS3jeEr2UclMLURQe-GWRI0CYwpU-O35lHiJH6iEHXItiTepbJnfKQJNcoGFC-xzzHzOSqGcRIFa1Q-tnzPwVQUIJIvSmcSnkZ6bFOq1s6DwCdF8NNPa4RD3LnnetggxhpEbpmbwL03i-W7MflM3bzlabp2yKFExAEvF_bdEzyVKXc2QJL4_ZlEiC_VTIuVhV3npWTw8KiZ5sZSxUNGFRhwgPDusuufDiCZrtbRPeME3cwhZTtgbGLvOPJiNbcxxCoUjn05caK4popGIVQRgCfDlW2xVmXZGCCvw_aOPaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e4c1d123.mov?token=tg1o4QD8x-qHrZj8Tq0WcxHPpFFVTFO5zu1z6WcOtFh2aS3jeEr2UclMLURQe-GWRI0CYwpU-O35lHiJH6iEHXItiTepbJnfKQJNcoGFC-xzzHzOSqGcRIFa1Q-tnzPwVQUIJIvSmcSnkZ6bFOq1s6DwCdF8NNPa4RD3LnnetggxhpEbpmbwL03i-W7MflM3bzlabp2yKFExAEvF_bdEzyVKXc2QJL4_ZlEiC_VTIuVhV3npWTw8KiZ5sZSxUNGFRhwgPDusuufDiCZrtbRPeME3cwhZTtgbGLvOPJiNbcxxCoUjn05caK4popGIVQRgCfDlW2xVmXZGCCvw_aOPaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس‌جمهور به عنوان «مهمان ویژه» در مراسم عکس یادگاری نشست سران کشورهای مشترک‌المنافع  @Farsna</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/467233" target="_blank">📅 09:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467232">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">۶ کشته و زخمی در حملات پهپادی اوکراین به روسیه
🔹
وزارت دفاع روسیه: ارتش اوکراین در شب گذشته با ۵۰۵ پهپاد به مناطق مختلف روسیه حمله کرد که در پی این حملات پهپادی به منطقه بلگورود، ۲ نفر کشته و ۴ نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/467232" target="_blank">📅 09:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467231">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQpVj8rW4G0Rnj2wKTrTL0ecLrBVKHyWgQHLVpfJk0fS291YnZlZgjZ0nbjSCmrbGiRxIY7fOL9nIyzKVAJbBTokLd6H6K1FDTKP8f8FW1_ap3nQdk7dWHMuqJ2BvKrUcyF9_KANqRhnpKCyY56HetBiAHhz08ue_5VPi_189-17uMAltbBj9Q2aaxN1c1rwG9iYofTuyjx8GwcoODT5liNZjtoESuTDIrC1C-mwuI-yYgQzdcTB9EQuk0DDTXWZzee4XzThOmWdBCNpxjochIOJlWNcWriv3XNNXrAFsKVHUvKLJnL3srhVrXaQVH2oSyTzvDnnI1YPeGCzu-e2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس تا ۱۵ مهرماه تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا۱۵ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/farsna/467231" target="_blank">📅 09:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467230">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/175419dd2b.mp4?token=Rui9g0q8PUvckRcPSMBG_eT5HL2z7xJ89b-Gq97MbC_ml_hO9ZLZu4YFDbqC_dhEvEwLQNgDRL-JZCI_Op6o-1esCmfyrRgsh9RxE70tcy80cSc7tqQpCV9lAGpE81gktkMBBosYK1wOU8s5ZRcEFwo4e3B3OUQ1QywZz7SqZqRPh6hfmkCs75DAcxw5A_HDRT5EevLB_oJufv_hcySxnKxm6vNnJRXh8icQvPrieAnfkHZyZjLJ0KH3AEliAsZZTjpZZ1xc-lU4nFY6goSSp-4zCVXF6Ixm5MWhZG6GHXiSzLLd0H31_EkVO44Uj-o5lw4lVGff5C_yktVP-VFZfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/175419dd2b.mp4?token=Rui9g0q8PUvckRcPSMBG_eT5HL2z7xJ89b-Gq97MbC_ml_hO9ZLZu4YFDbqC_dhEvEwLQNgDRL-JZCI_Op6o-1esCmfyrRgsh9RxE70tcy80cSc7tqQpCV9lAGpE81gktkMBBosYK1wOU8s5ZRcEFwo4e3B3OUQ1QywZz7SqZqRPh6hfmkCs75DAcxw5A_HDRT5EevLB_oJufv_hcySxnKxm6vNnJRXh8icQvPrieAnfkHZyZjLJ0KH3AEliAsZZTjpZZ1xc-lU4nFY6goSSp-4zCVXF6Ixm5MWhZG6GHXiSzLLd0H31_EkVO44Uj-o5lw4lVGff5C_yktVP-VFZfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور ۲۳۰ هزار نفری در پیاده‌رویِ خانوادگی کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/467230" target="_blank">📅 09:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467229">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7eb764da2.mp4?token=qzILZebz_95Rk9JyM0YOP9viU7G_Ol5qrO6n3HGCvl1D0KA88r1SFAzUkWUkur29cLD4YFanIRNkqrIG1444qVp56ZKtL8xWRffBD1O3kuOV_bdVRIKoy8wZBBoKrtdFgdd8ARwjv04puRL2FGdrwAUZFZDDPmSIc-t95Thy3W2fqaZ0W6lF2oMDN4QcUi8bxMQRWuYlusG6SWNsh4l3YpH0RQnEuXM-Hiaj6hdbQua-8TSZb1eBx46Lia3kaw5i-KFXpmc8yzj1QD-chmVb6JjmJsE7tCaTskHVPQG13oY8GcJ-Snu6jhgjmwZgIiiGsJMisCEEXLFlbQwjAJhDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7eb764da2.mp4?token=qzILZebz_95Rk9JyM0YOP9viU7G_Ol5qrO6n3HGCvl1D0KA88r1SFAzUkWUkur29cLD4YFanIRNkqrIG1444qVp56ZKtL8xWRffBD1O3kuOV_bdVRIKoy8wZBBoKrtdFgdd8ARwjv04puRL2FGdrwAUZFZDDPmSIc-t95Thy3W2fqaZ0W6lF2oMDN4QcUi8bxMQRWuYlusG6SWNsh4l3YpH0RQnEuXM-Hiaj6hdbQua-8TSZb1eBx46Lia3kaw5i-KFXpmc8yzj1QD-chmVb6JjmJsE7tCaTskHVPQG13oY8GcJ-Snu6jhgjmwZgIiiGsJMisCEEXLFlbQwjAJhDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان برای شرکت در نشست سران کشورهای مشترک‌المنافع وارد سالن اجلاس شد  @Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/467229" target="_blank">📅 09:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467228">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efdbdbe8b0.mp4?token=qJXUDbv4HpzVTxMU39uB59NbvULdGoWS4zsSuISIa-I1bEjfZphyd0miRvo49HiiXS77sP2u5Sm7iy_k59M2ajGCWVnhzR_bkRbSTwRa6UUXbSMm4A0uglv5O35w8s5ByE0dyQ6DQWSk2n4hcq6EuUXWLNVwWXRnFfD6BMhhi5Ny7ih-Uc4wPcrK-MfAXiK9MRPb5y-1aHbeMz73ntcMounVxgVhfKaphXIv8Tfm22fKDPxLSo28lhSzJw_1Osi61lE_ifnnwTIFtNv_EZBWF5ixiDH29J05gxYAEuDg62y48NDJ1As7u0KBdITN89AXAWhgGBgN001-SoM9b3wbEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efdbdbe8b0.mp4?token=qJXUDbv4HpzVTxMU39uB59NbvULdGoWS4zsSuISIa-I1bEjfZphyd0miRvo49HiiXS77sP2u5Sm7iy_k59M2ajGCWVnhzR_bkRbSTwRa6UUXbSMm4A0uglv5O35w8s5ByE0dyQ6DQWSk2n4hcq6EuUXWLNVwWXRnFfD6BMhhi5Ny7ih-Uc4wPcrK-MfAXiK9MRPb5y-1aHbeMz73ntcMounVxgVhfKaphXIv8Tfm22fKDPxLSo28lhSzJw_1Osi61lE_ifnnwTIFtNv_EZBWF5ixiDH29J05gxYAEuDg62y48NDJ1As7u0KBdITN89AXAWhgGBgN001-SoM9b3wbEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان برای شرکت در نشست سران کشورهای مشترک‌المنافع وارد سالن اجلاس شد
@Farsna</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/467228" target="_blank">📅 09:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467227">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_I0onw3ExHixRRHVR4gkaY-JaE9BAo2dyXEQ77--CuME_UFqFVAl7oTA01lJVRr-b78vBaOL_8w1wkRPXqTweyPabEsXx5JBD0xvUCdMmpZFmyvDAXoBSsghXAQKyXOtwwtpttY6OGY4V6ar3rck0H8hTDReyFaEVLLkQugxaHlQfa0OVaGVEb6H2ASOmqElc5NhUokd0dSMx0LcHl5Jayljs4EuJK_MIct5KjmYnhIkgrf15UHkNgMFt0RSEzNdXHBvi1rKzo7Q35N3tA113PVPqyuHgFfqZ3J0yp07we2ymeXqRSixJlntwsJTW4K853o5piVBTYjJ_t_M_gevw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت‌های دریایی در دریای مازندران موقتاً متوقف شد
🔹
هواشناسی مازندران از وزش بادهای شدید و مواج شدن دریا خبر داد و با تأکید بر خطر غرق‌شدگی، فعالیت‌های شنا، قایقرانی و صیادی را در سواحل استان محدود کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/467227" target="_blank">📅 09:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467226">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
ماجرای اولین سفر با کشتی از تهران تا بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/467226" target="_blank">📅 08:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467225">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a90f4363.mp4?token=MoAUKnIk9Ppy7UPwN1-VPM9hruekC4dtSfJOY3aLJDjxr6yzDoGsAGiP3CDlucQuihPh_SI1WfWVtO_Ug58KtWzl1fHnmTnlNp_4cA9hbVhLRgBMzVSPup5739U0W0n0ZcRFbNQ1qgPB4yXFy-JX13wYxyTTju6gY-8AetNuhllgXIa_U58dDa1_Np1xD8gh1ubehP1sLFGGe-3M8UlMMz4qFX0LKgYBhEUNNHqrp5negOycJta19LtU8PAPo0Rneefo_sDMgCgAotTRydoXkZDXkkjJ2fL6xycuZJ2Q6mVlRDG-SZpS5Hu34ccLJp8l8tc2pKnNw8utWf9DEh5jsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a90f4363.mp4?token=MoAUKnIk9Ppy7UPwN1-VPM9hruekC4dtSfJOY3aLJDjxr6yzDoGsAGiP3CDlucQuihPh_SI1WfWVtO_Ug58KtWzl1fHnmTnlNp_4cA9hbVhLRgBMzVSPup5739U0W0n0ZcRFbNQ1qgPB4yXFy-JX13wYxyTTju6gY-8AetNuhllgXIa_U58dDa1_Np1xD8gh1ubehP1sLFGGe-3M8UlMMz4qFX0LKgYBhEUNNHqrp5negOycJta19LtU8PAPo0Rneefo_sDMgCgAotTRydoXkZDXkkjJ2fL6xycuZJ2Q6mVlRDG-SZpS5Hu34ccLJp8l8tc2pKnNw8utWf9DEh5jsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: در ساعات بعدازظهر، بارش پراکنده و ضعیف همراه با رگبار و رعدوبرق در مناطقی از البرز، قزوین و تهران رخ می‌دهد
@Farsna</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/467225" target="_blank">📅 08:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467224">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQJDU6OvSdMp9hGF-47DwrIf2jtqd9lxm5pSZTjj7Vae_a_et1Z2Rjd0HrHWQLMXDZIXviad-wbICTduUTseApxZcj_74rHdjPEASgwQSKkBnEhEjcSuywJixGD2t4i3rkl1vfWKMDlmNP49xH_f4WMEseeFHAzyfiiZKOBA9mWccbWdQW88kd-U4w6sAxAZudl4hC6efOW1mvdcUNJ1M83GbCNU0IarJKv0QJlg1cARopY4BCo1raeHk02ROewoVUILCuE2HVPm-zbhSrbKT_BTQ69ysngkwJZ4PzlHJ0k1Ml8fGe1H5vZ0IAOI3sxbxj4YAUCqvMpv8Mv1KX31RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در حاشیهٔ اجلاس سران کشورهای مستقل مشترک‌المنافع و اجلاس محیط زیستی دریای خزر در ترکمنستان، با نخست‌وزیر ارمنستان، دیدار و گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/467224" target="_blank">📅 08:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467223">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
سلام بر تو ای وعدهٔ تخلف‌ناپذیر خداوند
!
@Farsna</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/467223" target="_blank">📅 08:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467222">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هوای تهران «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۷۷، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/467222" target="_blank">📅 07:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467216">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRYjaKiyiUsBchbTmhBuig8X69gDwWTnCgcnf6E2u7sAlOY4j-g-9V3veMF2B3UXiNXaVGRTENT4_xnfHhNHBH-TnA9A28JielCAXOQ-2Wsc5KFIVdkrW8nMP-GyrefHbF4LTyZiULWWHO4wyppgsE8bLRUW58CWDAc-8wsi-ad9WDZBjCPDVwrANro_l3wPjx8V1yWDOLXWMklQt1A-BquwDbhCyuidV8PNQfIXSmfS2PrU5qLlNm1i971gfREM-CJCR7Gwev78E7yNpzLwDL5h9Nhox8b2HOxe8vNyeem_3ZqDza5ZJKAQl4lpDUgUQ-kG3pa7Ss7Qxh4ZeTienQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7qneZVLNwtTFcQTrfEEeBzmfHTDA-dGyFXnNUDEpPLQv5LGOYKfOHrf7wMd048uAPglWlxcqh6W7nblIbrN7ZP_ANztUrowqxt4YjFJ-OHILcraQ8e3oEpN9C1bSq7mt-QDO5c_I_e1ayTiq1SD1bBQWaFCdxyUxOEbvtoWhAvl7jQPrOA10StlcRnL8_O1yTt2MZI0hbLsHC2u_u4n_qHD6ghTzB4__Qdt7VnxY42WPsNjTYUt7aumWo5sct0_08_bApKTvAWM8jnsFlvO_J0cEGi0hiZe3ClTUZUJnOIqtyd_Y_8RblPLSq3pW48sI5OWt737J1t7jhazRd54OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJMjrCFsaDZkiGsacmPewb09g_xIp6XPtSw85A0VA902EJCkqv8jmXOGAuiUsq6ijBwcdyy4s7xJz-BbVAHsF26YGx7uLuG0NHjWGnyQ9mme_jqQwXb9zIEQSUBjhA1j0QyHuO2V1d8FeVC6JccSn8TqY3l4dTe-f4AQaYvxE-4HZHSHkaCCB5KXME7sMrBRxIaChN0PR9X3N47ReetXwmMskkIk_nWbNakxIVu-6SUkVO2nHkg4KBKgf_2R2XdrxP7FYTvAAYbdoNVg-RHB7mt1bfYLtv344IgM7BqlYg4v4TYWUDPURnGiXQQViZIz6g75Kc-GTWxy56kROjTWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZ97aO8vEKBAao2pdpb3qGNxHffCeRgJPMnJyYo_S5ZZ9UiYspgRM7eP0zZdjpxtNjwc3wshac94F3neIAV6dzyOrs4ZcY0TQEXtu9mq4QzzzSvWWd6YBk4FFjy5ABdC6SrmPkJsy8wz0vkw_gsu3UwjkzYrOKBHwFzRdKkMtedbKH2d86zIJ2Y4M3W5bZf_HKKcn33ueIWnzD8EtBB8XKlaA1RzocTv0sMq4wvFS4cDeM8U71yYkoI_E4wlJ1jrIhE2Pj7hOJDXV8Pl6CAoNMnbzGVkrjdtUIGKxDqQnHIfqL60sqqIxbZHDN_fnuHEglJhrh85tpXim8111LswLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mhZa0dHlnxKxSToY4AxYKV20dsGrnrqDLkjJ_c4LMJeXhukRNjHmLJupIw3oeV5xQJ313IzmR8qjw4X11j4-C5dJt_bTdw_i-3c-fJgAtzDvSyZy_ieM_31BHR5lMm3lJMr00EVQe__6p13ERkn8yeOxGzTxmHzd9_fRjFSHiTFhudExHLDRV_kJQ1DOz9xoEBS9jpU6X2GjNVxwOjNcyOF68FmD4TCjIWH1d4o_LYcyxU_suW5L2F68lYgC6t6MxktcFwWzDq6ObSHVMxcsMqZUbWzRwGNiY5JIqD-71nar9d8EmHqvzdPzKdLwYOBd4ehxApgTuyfoYePlsy_HPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن روز ملی کودک در ساحل بندرعباس
عکس:
معصومه کمالی
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/467216" target="_blank">📅 07:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467206">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بازداشت دو نفر در انگلیس بعد از ورود به یک پایگاه آمریکا
🔹
پلیس انگلیس اعلام کرد دو مرد اهل لتونی پس از ورود به یک پایگاه هوایی مورد استفادهٔ نیروهای آمریکایی در شرق انگلیس بازداشت شده‌اند و تحقیقات دربارهٔ این حادثه ادامه دارد.
🔹
بازداشت این دو نفر چند هفته بعد از آن صورت می‌گیرد که پلیس انگلیس مدعی شد طرحی برای حمله به یکی دیگر از پایگاه‌های آمریکا در آن کشور را خنثی کرده است.
🔹
پلیس اعلام کرد تاکنون هیچ مدرکی به دست نیامده است که نشان دهد حادثهٔ پایگاه هوایی «مولزورث» در شرق انگلیس با طرح مشکوک علیه پایگاه «فررفورد» در غرب این کشور ارتباط دارد.
🔹
پایگاه هوایی مولزورث مورد استفاده نیروهای آمریکایی است و محل استقرار واحدهای تحلیل اطلاعاتی، مراکز فرماندهی و یک مرکز اطلاعاتی ناتو به شمار می‌رود. این پایگاه برای عملیات پروازی استفاده نمی‌شود.
🔹
ماه گذشته نیز انگلیس مدعی شد چند مرد را در ارتباط با طرحی مشکوک برای حمله به پایگاه هوایی فرفورد بازداشت کرده است. این پایگاه در حدود ۱۴۵ کیلومتری غرب لندن قرار دارد.
🔹
این حادثه نگرانی‌ها دربارهٔ امنیت پایگاه‌های نظامی بریتانیا، به‌ویژه تأسیساتی را که نیروهای آمریکایی از آنها استفاده می‌کنند، افزایش داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/467206" target="_blank">📅 07:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467205">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🎥
شعرخوانی محمد رسولی در رواق دارالذکر، مزار رهبر شهید انقلاب
◾️
کسی که کُشت امام مارا، چرا نکُشیم؟!
◾️
که ننگ ماست، اگر قاتل تو را نکُشیم
@Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/467205" target="_blank">📅 07:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">طوفان تهران ۱۰ پایتخت‌نشین را مصدوم کرد
🔹
اورژانس تهران: در پی حوادث جوی عصر روز گذشته ۱۰ نفر مصدوم شدند  پنج نفر به صورت سرپایی در محل درمان شدند، و پنج نفر دیگر برای ادامهٔ روند درمان به بیمارستان منتقل شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/467204" target="_blank">📅 06:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467203">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc21dfb31b.mp4?token=FdkVC_XDxCDwcpvBtifujkTZmrfrGVlf2JNa35DkwQDSU1qqef0v7O8FV7IoSbPtMJRFVKTEYcojt6c4O26-yqYM658dJiaUPgiTmxV_e8euU8QTrF__dpdwKbMvSfciePOEdtrA34tSYm5mcbR0WdvDlek8NmvVfLDHvmPI-Q4X754d9t5QLr1gLPx6bLCAnTVoXjna8MkDV7-flqKV6aorW352VbIvpPz5sAj6AwMP6KqUE1ICYGth0chhAjUpzD6S86Lk6srshHwJvQY0nV9rEWOKqBZGA6UC5vFebkyF-zrdafCPRplDBRrVim0lVVV5UEK-Q_dQmzCYFCoUrnCk7soMw8rOjvO3SV9DvJeWsrLNNrIH5Y0pmpZUQGBPquNpCTTJcXtsAzp5SgHc6-8VQsvNUTzQ10vbdeev91fw9w0ilodQ3T12KC0jAnCQB-oQBDyrC2XtfGUeQMXsqS4jOrAqpELyHFTcik9dpg0ho10242gRHebg0qREQHVDTIO1bBsnQPPRKk7MCLyT77kBCxpR7ozmyIc4Bxz_VUoos1qFZ63KCzVbWsDSxTqMqcAzD7RSKsb156U6RjTsh6lHU9roQ8pSwvXlSWp5-tIN373z4d7V5tWN-r932lahqfgI9kSdjkxggU4EWIJiR_aH9b62iwpLQYhnY97o5Zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc21dfb31b.mp4?token=FdkVC_XDxCDwcpvBtifujkTZmrfrGVlf2JNa35DkwQDSU1qqef0v7O8FV7IoSbPtMJRFVKTEYcojt6c4O26-yqYM658dJiaUPgiTmxV_e8euU8QTrF__dpdwKbMvSfciePOEdtrA34tSYm5mcbR0WdvDlek8NmvVfLDHvmPI-Q4X754d9t5QLr1gLPx6bLCAnTVoXjna8MkDV7-flqKV6aorW352VbIvpPz5sAj6AwMP6KqUE1ICYGth0chhAjUpzD6S86Lk6srshHwJvQY0nV9rEWOKqBZGA6UC5vFebkyF-zrdafCPRplDBRrVim0lVVV5UEK-Q_dQmzCYFCoUrnCk7soMw8rOjvO3SV9DvJeWsrLNNrIH5Y0pmpZUQGBPquNpCTTJcXtsAzp5SgHc6-8VQsvNUTzQ10vbdeev91fw9w0ilodQ3T12KC0jAnCQB-oQBDyrC2XtfGUeQMXsqS4jOrAqpELyHFTcik9dpg0ho10242gRHebg0qREQHVDTIO1bBsnQPPRKk7MCLyT77kBCxpR7ozmyIc4Bxz_VUoos1qFZ63KCzVbWsDSxTqMqcAzD7RSKsb156U6RjTsh6lHU9roQ8pSwvXlSWp5-tIN373z4d7V5tWN-r932lahqfgI9kSdjkxggU4EWIJiR_aH9b62iwpLQYhnY97o5Zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون نیروی دریایی سپاه: شناورهای متخلف در تنگهٔ هرمز هر شب تنبیه می‌شوند
🔹
نیروی دریایی سپاه از شب نخست جنگ تاکنون با اشراف کامل بر تنگهٔ هرمز، برای حفظ منافع ملت ایران عملیات انجام داده و این روند ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/467203" target="_blank">📅 06:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467197">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/liIPQBKiFiKT1-j-tV86jwmM4-05gnsYqfR49QqDW6Oi4otIJRIH9wN4awSAT3NUrrDFGeKMDmRDFyO2iB4a9AVcUurLonYIgpnE9bqvBTQVrjAwckHJjk_0RnBhLpdS8PhJOy1L5phbqkDdIYNDFCfPX26pNxLOIOLfywopowV_0zpQzb3vDQpruc-WtY8JgwE-EhFCg1dwPHelFZ7Rg73RoTb7tjVuvTqLgCSRgxKLOutat0REYFr4rjcVbgG6e6ovBQSBtlIvaqNXmfU2Jktn6JtMVCHM1_qWVlc_rRiHF5YLLZEavqcjrEdYvYHmTQ9b4YoP49GdaWw5mV5Y_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JmAebVG21zlnZYqSWVqnjrhWpkO_RZTxlZEEQjyvk2-vd8TkF-Xr8N7f-nW-_81jukP6GAkLmDBv4vp90SgDxe5JfGhM2pro1rTM2Sz3TtcPnQHmNSGkm_wyObUKK1sKM84xdISJO4Ho-RwQlQfv_Gf4NpeIzN7ogS1jj5hFSz3SnL1dxkvgpJ0GRnoOH7C3RxTAP7xt_AIh5wP_SBPxLsDX2DrGvuXNM1_3PwexVRzNEP0JzM5vEMrBU4YeDaQzhW_ppTzUaCPro_oCOLuxF7qsY1KqT2b2eHIw-icSwyDGZNKbDwcRNXZLSLJANk-yzmCEFtmQ2N9QrP8X5bd-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NONF3lbNDnT82gHGJLxg2xP79d7ql3dc2U4cpmnPPTzcCWJdagpZdl6IA1pNANtMTEmMgnfh2rRAbOrp5UNRuw-4slItifmjAZrG_PoBeAmve0R2TNKSQqkE2IW4uq_Iee6iwwvOHIBGwEzcCd5ieuK3aT1oWcJtG6h2jgE-kK4bJsPXBIbhiZpydTDQG7WeYJTZzFe6cz9VfeYw0RZT9jd0pxcqJA-D_7BlfbgTzuuCV89TZszC0TC326gJeUaIIW8SoN5XKbXoDfjhRQDXO79pRfnCjqGPJLUbyTMq-fkx4PH4LMLYFCSmV7KEhV2_jxaqb0WQdW3HbsLYDa0T_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/acXSbetXoVRVPB92EMYqlfA5eY0u56An_uw8or1p_tDNachaYSp_H9mzgCDBCtQt8S5kP-WJzldDKRxoecHDyqkSB18UmhRCEC-po4g9a_QG0P8GJ0ljx6gU8QxjLHEvpIFuopj_4ARd8shWfbRmpSp5sIHnvmXOgJZ8b7kLDE7xE3lMOYbs4hBfe26kS_6Ego0J6awW2ndBNFRIid5NV4k1vSAa7pmMYM3KvqM4FcU2w-X2IhYFvN9YKxlmUwditJg-6wZXemTfgSniWUGJR3jOs3wrx_Dky2qn_o3yzjddRl3c2DjWACbvtwThX9Wtps6khYPqNT-eU3l1m5PBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nmyx7Lxo0OsLqLpz22QDi-7wsaNpZuIQGU9VNURowjt1UAC3bknItcf3jsPI9384qJ3uvzhP-wvxvvketldp0EBpLaycxignHFCyPe_YAFlYqzXbASQIeaIktCei5JOpHyNQyPY8jYcGYyLerGD2t9Prp7MnhbzvloqrHhSeGkkNayeIIUtqeHaWXykoCzDJjcNJ0XMTxIy68ppRPjRBW4UXW0p32ztO-z14riUvKgYMWypoHwMVYn5uGScg6tYu0raWGSs6T3Tl764pLb68Y_4fb2OzohjyT6_YnZsFZ9TCXLfpeUI9Cx20eWd5ohAeqv15dDkhy1G01woGoUGUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIaRcDDAl6NN74C_Qcf-fkcQk4Bf6eJXR1Y_ZWjyDl9qe0I3898cWagFjBiNr4-la3nBlFIQUhTRqWtubMSMT-Avzmv0omeV8neUjk6P-x1dDbzFD4-SqP0_qLkcDE5bf0wruLLS0qfp75KXGN02svUifksEUDZmTgtZEoQ9qGfCXNdzZ10_lRZ7lzQ76VLfzkBpnQ0N39bCaFL10fuh2aKBAnsOAAQ5tefvWYxaj5Y6_lFbMNBzI3zI2MuRDbUpH1JnwsiFqRGFZ25Sezfc08GcR0su-DZL1vF8JikJLP6ocgZpgOwefd4zzd4bRZ_oAIOu-bCl3fxUJVudKjqJ7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن شکوفه‌های میناب در گلزار شهدای این شهر برگزار شد
عکاس:
عماد یگانه‌دوست
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/467197" target="_blank">📅 06:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467196">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آموزش‌وپرورش برگزاری آزمون‌های «ماز» را تعلیق کرد
🔹
رئیس سازمان مدارس و مراکز غیردولتی: داشتن مجوز به معنای فعالیت بدون قید و شرط نیست و اگر تخلف مؤسسه «ماز» ادامه داشته باشد، پروندهٔ آن در شورای نظارت بررسی، و تصمیم نهایی دربارهٔ ادامهٔ فعالیتش اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/467196" target="_blank">📅 06:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467195">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🖼
تصاویری از هواپیمای منهدم‌شده عربستان در حملات یمن
🔹
درحالی‌که عربستان مدعی رهگیری موشک‌های یمنی است، تصاویر جدید انهدام یک فروند هواپیما در فرودگاه ملک‌خالد ریاض را نشان می‌دهد.
🔹
رویترز می‌گوید که این هوایپما در حملهٔ موشکی نیروهای مسلح یمن به فرودگاه…</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/467195" target="_blank">📅 05:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467194">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هشدار استرالیا به شهروندانش در عربستان: از تأسیسات انرژی دور بمانید
🔹
استرالیا از شهروندان خود در عربستان سعودی خواست از پایگاه‌های نظامی و تأسیسات انرژی این کشور دور بمانند، و به آن‌ها دربارهٔ احتمال بسته شدن حریم هوایی و لغو پروازها هشدار داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/467194" target="_blank">📅 04:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467193">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwQyD-dWbDwB6uWwIz-PiSnhjz4EbMVW9BqqUifpsJEqDvEcpvGiSxjNEXqNunOtWhGcl0qlxV_RJTJ06nTCQEBfbMyBpCPB64w-zo4ijgwFjBxqvE6R-C9eG55eQfdtYfgVJB6FHzm_Z4MxbVI9IUOzNSibwunmunNX_wPFcG1nhWVNOU0py6mG_a6jEVB0SjWrM9S83D5a2kX8ljFABi3lQJ1nNW6eLyefUHwCNmFfUIoaHGstjvsCAawOW_IUiz99UbdaGESrMoUj4_CH-sMdPAhajDdVk_ZWi2HuUc63L_wwODHCG9hSY2Z7Ihs-a6VMSw-Tb4V8qKODAhcryA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهرانی‌ها برای خرید از طرح «تورم صفر»، در سامانهٔ شهرزاد احراز هویت کنند
🔹
شهرداری تهران: شهروندان پس از ثبت‌نام و احراز هویت در سامانهٔ شهرزاد می‌توانند خرید و پرداخت خود را انجام دهند و کد رهگیری دریافت کنند. خریدها با پیک یا به‌صورت حضوری از میادین منتخب تحویل می‌شود.
🔹
همچنین امکان خرید حضوری از غرفه‌های متصل به شهرزاد با کد ملی سرپرست خانوار وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467193" target="_blank">📅 03:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467192">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0567dd374.mp4?token=lf0OANGaeqbbTnTeIrNRNh7oNWRolxYmwsakA-wgBnzkyZzkVkwjRnr7IbZ-wA4naWM9hYHU2am5Kl5WcM3hSHcfstblhw_x4N6mtJtW713nzcEVfMwbiPIpen4FqLBqBxvFd3BfhPudRGwX7Wdrx_T79DycyvCtHAMJTTgsO90cFB4qNr3UMnb2EToiAuuC8vnUQzm88YwOEGP-2RVLp_n5mp104aLPJckxMO5eC8IGcXUXRFknYYDetu--b4juwt-k8Sxn0ZjIsC39Cxng7VWZbvLeEIYav8h9KaYAkMVEyL4TdY2MMSsJSRPivW2EnuD1WNRRwiABX4FRUKBlCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0567dd374.mp4?token=lf0OANGaeqbbTnTeIrNRNh7oNWRolxYmwsakA-wgBnzkyZzkVkwjRnr7IbZ-wA4naWM9hYHU2am5Kl5WcM3hSHcfstblhw_x4N6mtJtW713nzcEVfMwbiPIpen4FqLBqBxvFd3BfhPudRGwX7Wdrx_T79DycyvCtHAMJTTgsO90cFB4qNr3UMnb2EToiAuuC8vnUQzm88YwOEGP-2RVLp_n5mp104aLPJckxMO5eC8IGcXUXRFknYYDetu--b4juwt-k8Sxn0ZjIsC39Cxng7VWZbvLeEIYav8h9KaYAkMVEyL4TdY2MMSsJSRPivW2EnuD1WNRRwiABX4FRUKBlCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این‌طور به فرزندت نماز را بیاموز
🎙
آیت‌الله مجتبی تهرانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/467192" target="_blank">📅 03:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467191">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حملات هوایی عربستان به دو کارخانه در صنعا
🔹
شبکهٔ المیادین به‌نقل از منابع یمنی از حملات هوایی عربستان سعودی به دو کارخانه در شمال و شمال‌غرب صنعا، پایتخت یمن، خبر داد.
🔹
به گزارش رسانه‌های یمنی، یکی از حملات کارخانهٔ تولید اسفنج در شمال‌غرب صنعا را هدف قرار داد.
🔹
حملهٔ دیگری نیز یک کارخانهٔ فعال در زمینهٔ تولید مصالح ساختمانی و تجهیزات برق در شمال صنعا را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/467191" target="_blank">📅 03:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467190">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhjNwJ7m-v9K2s0zECZmCOfBvJkD96fAj2gZgJW_odEinsjnJe_wLIIn0-YXYruPBx4Y3xC1Mjc-qohDd7ug1A6KP6Dn4uX_WXJFmxMcU3nf0ZTJ1D8LyxnxpsgGX0uhzZWkDTpBs3p3EnOR-OuKjsbBVMV8FxYqLQwOJcx9wL0wrtG7tDxMnNUMHmaKupoppdsIlUkgAVmoKExdS2oW6ndtDtqB5VsyPkAx5bk76w7b-NZ0AY2kQlmtAwesKVAf6EsxLPdurfFsC537nmWR33QnzeJ0W8Q3-qUP01j12dUn-HWQQuBE8PqlHbL7B00qZcEAVooGZEnJessuH_A6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنهان‌کاری جنگی آمریکا؛ وزارت جنگ آمریکا کریس مورفی را به العدید راه نداد
🔹
کریس مورفی، سناتور دموکرات آمریکایی گفت وزارت دفاع آمریکا در جریان سفرش به خاورمیانه مانع دسترسی او به یکی از پایگاه‌های مهم نظامی آمریکا در قطر شده است.
🔹
او این اقدام را بخشی از…</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/467190" target="_blank">📅 02:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467189">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sip44mWBuXlFwGJkTbC05UrJFcrJw1EbF_fxDgQDXl1qStWoKU6IIY41picJuThenzIl9DX8cuXzvPjXesudvvYVe0-qblfi9tjlBzrrS0TahAEroIXAz9ybjoaf6_VRbEEUDnDvxLfgK427I_YQnjnOnUcsUGm3b51yEqGBzY4xA7P5Ro7veHWZA4nqG7M-Hm4BXP8PEalDC_TrDBv9wjKQxQhMGFvq4dkSmGLhQxTbAliCNin_UiH-aIsznI7DlOSBE5BXas5SSINMTLPffRIX68_jkxUzmyKOU0LJ1HJ10sRcsGVVxM-HT5iqGL7zBbRv4qA7y6URuU-vmFRQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع: به فرودگاه‌های عربستان حمله کردیم
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد شامگاه امروز پنجشنبه فرودگاه ملک خالد در ریاض با دو موشک کروز و فرودگاه نجران و پایگاه هوایی خمیس مشیط هم با موشک‌های بالستیک مورد اصابت دقیق و مستقیم قرار گرفت.…</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/467189" target="_blank">📅 02:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467188">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/830f231c18.mp4?token=F3LPXmqAX2f0n0G79iO1ChZv9KCmc6Gg2hY9VSlQtg-JFLzL_7cmAkoCMqeZ8cghfbIHB4d9Jg16sWssv1I_Y6PMLe9Pk-ScFwZSGa2G3cscXsuWqYdseASOMOiDZHXOcfmL7BiNssNkmREGn8WKZ6QMClz0l6MSrmMJkRZhH9qUCdz3Qi9oP4QWpOnE3AL0aSPHVQ6AqSyAwkjDW75ZPdyVpXTOtgwTI9_573HkmdRZt78ylCXzCA4c9W3dLzCuPkSnnXzlL_1O24r4ltqqpSPbtjBzWwayp40OiT1eJlVpIDzgXaKzABhh_gj4_A_5XAN3FWG7qg2ftcQ7AkMjq7KwB1DpH_GPJGRYZPbMtyhFcvXwP5oAkszOf44nCIBGsNPAx2bSUg6z0pStFqLbmEkubqgkl17tP2rjPaGFFTe0TKQT84Kr3kxmZEYCm0EolFZtPJcUPxDkztpJDyBsFeg_VG0oZ-EkCaHMjEsRP7V3_gO4nndzIt5SGNk2PFRLbBzafhPPLV0rN_wBCZs1wyHrRRiUWSgzolKxnp7hBWak8lTu15BYt8FWYu-FPr9feDOHRABhiqSpD8txXml11cU2Bjpq-yeOQZEzgjUc8fz_ciXbZ5XypRhjvuuT-Wh2oA7qAiDrWjlQ6LxFER1ZbYS3kF7SeA0N1RsoqfDl8cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/830f231c18.mp4?token=F3LPXmqAX2f0n0G79iO1ChZv9KCmc6Gg2hY9VSlQtg-JFLzL_7cmAkoCMqeZ8cghfbIHB4d9Jg16sWssv1I_Y6PMLe9Pk-ScFwZSGa2G3cscXsuWqYdseASOMOiDZHXOcfmL7BiNssNkmREGn8WKZ6QMClz0l6MSrmMJkRZhH9qUCdz3Qi9oP4QWpOnE3AL0aSPHVQ6AqSyAwkjDW75ZPdyVpXTOtgwTI9_573HkmdRZt78ylCXzCA4c9W3dLzCuPkSnnXzlL_1O24r4ltqqpSPbtjBzWwayp40OiT1eJlVpIDzgXaKzABhh_gj4_A_5XAN3FWG7qg2ftcQ7AkMjq7KwB1DpH_GPJGRYZPbMtyhFcvXwP5oAkszOf44nCIBGsNPAx2bSUg6z0pStFqLbmEkubqgkl17tP2rjPaGFFTe0TKQT84Kr3kxmZEYCm0EolFZtPJcUPxDkztpJDyBsFeg_VG0oZ-EkCaHMjEsRP7V3_gO4nndzIt5SGNk2PFRLbBzafhPPLV0rN_wBCZs1wyHrRRiUWSgzolKxnp7hBWak8lTu15BYt8FWYu-FPr9feDOHRABhiqSpD8txXml11cU2Bjpq-yeOQZEzgjUc8fz_ciXbZ5XypRhjvuuT-Wh2oA7qAiDrWjlQ6LxFER1ZbYS3kF7SeA0N1RsoqfDl8cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عربستان برای جبران شکست‌های خود، به دروغ‌های رسانه‌ای رو آورد
🔹
سلطان سدح، خبرنگار جبههٔ مقاومت در یمن: عربستان برای جبران شکست‌های خود در برابر انصارالله، به‌دنبال رسیدن به پیروزی در رسانه‌هاست.
🔹
العربیه و الجزیره به‌طور گسترده دروغ‌های عربستان را پوشش…</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/467188" target="_blank">📅 02:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467187">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Arzsu_3C88dvLLjwQb_zEuwlEZg9mFd0r-FcrJQ3IwDQdKWHrE4MkcQxIFqYf0TnIDp_kfKuT7Orz_YJ2SzRwOshReswzUePr9UFFu8cLOovmxXuAveINEKoUm1H5sVUN1Md8vmPWU60kajhrcLvVSmAdTnGr0JVc37NjE0WpeiUwhRo8IqS7eYn9Ye4aYKPes82VTmL228f0hW5WtJvmHbhutyGhobnYLn6gtW7sTMxkB4w6AcbHdJaoLIdN0ywajGhmzEp6XY0NzpiseYtbnkYjV2-P-QoUDkDDxJH6rUmFAXOhXI7rNN5FNeU2SCz8OUCHKBmyGDKtf-yszGTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرانوند قبل خسته‌نباشید به هم تیمی‌هایش، به سمت بازیکنان استقلال رفته و خسته‌نباشید گفته</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/467187" target="_blank">📅 02:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467186">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veaNtkeyxet6-a0WW6RNW4OK1XoRN8Ibrl9hFRe5mayyt6OB7gkdLS3JEW3n78q9Bo9dB7MIkFBjQkDVZnCZFHnMjKu5oqhk60bJznV6DzYFYrRe8Unx1-4TiORGlg6B3coYXrGojOFfqL-AqrypS_i5RU-4QfQ6RKyTLjAwZ6KTyvK1AHKdBs8hx9oEPEFk-POtjVPiTek62y6R1QUN67W7otDRevqMVTA8EnHsYruLCaNHbNn9uJ3QuLpJ0rMygmN8WPSp_qcQTMoH8kQcEWZgdpokOMAouHOeLxcbPfTAgbRm-N143gvBcVFy-iETNpx42AdP8ORw7_6t9IQFFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرباران افسر سابق ارتش آمریکا پخش مستقیم می‌شود
🔹
پیت هگزث وزیر جنگ آمریکا روز پنجشنبه گفت قصد دارد امکان تماشای عمومی اعدام افسر سابق ارتش این کشور را فراهم کند.
🔹
این افسر به‌دلیل کشتن ۱۳ نفر و زخمی کردن بیش از ۳۰ نفر در پایگاه فورت هود در ایالت تگزاس به اعدام محکوم شده است.
🔹
هگزث در گفت‌وگو با رسانه‌های آمریکا گفت: «مطمئن می‌شویم که مردم بتوانند این اعدام را تماشا کنند؛ این مجازات باید علنی باشد.»
🔹
یکی از مقام‌های وزارت دفاع آمریکا نیز اعلام کرد: «این اعدام به‌صورت زنده پخش خواهد شد و جزئیات بعداً اعلام می‌شود.»
🔹
نضال حسن، سرگرد ارتش آمریکا و روان‌پزشک، بعدازظهر پنجم نوامبر ۲۰۰۹ در مرکز آمادگی و پردازش سربازان در پایگاه فورت هود تیراندازی کرد.
🔹
او در سال ۲۰۱۳ در دادگاه نظامی مجرم شناخته و به اعدام محکوم شد. او اکنون ۵۶ سال دارد و از ناحیه کمر به پایین فلج است.
🔹
بر اساس یادداشتی از آدام تِل، سرپرست وزارت ارتش آمریکا قرار است او ساعت یک بعدازظهر سوم دسامبر در پایگاه فورت هود با جوخهٔ تیرباران اعدام شود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467186" target="_blank">📅 02:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467185">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">استقلال: بیرانوند به رختکن ما نیامد
🔹
باشگاه استقلال به اظهارات مدیرعامل باشگاه تراکتور که گفته بود «بیرانوند قبل خسته‌نباشید به هم تیمی‌هایش، به سمت بازیکنان استقلال رفته و خسته‌نباشید گفته»، واکنش نشان داد.
🔹
استقلال در اطلاعیه‌ای گفت: ادعایی مبنی بر حضور آقای علیرضا بیرانوند در رختکن استقلال مطرح شد که صراحتاً اعلام می‌کنیم چنین اتفاقی رخ نداده است. تعدادی از بازیکنان تراکتور در اقدامی محترمانه و در چارچوب اخلاق ورزشی، برای گفتن خسته‌نباشید و خداقوت نزد بازیکنان استقلال آمدند که از این رفتار شایستهٔ آنان تشکر می‌کنیم؛ اما آقای بیرانوند در میان آنان حضور نداشت.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467185" target="_blank">📅 01:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467184">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_WXr2exFZXMUk3lU3UusL-TSq8FCubC_c6tJoahhJOMqxjugnl0TQRrAn15zubCZ02X5xVdwo3I_qewP4VR_obmAInk_sIsuE_L5S-l9ERCfEdOxjcSb0r_BDM1iDzSTGyRxYkUXvaQXVgG-bFMyc2rK32rzBrsgyDWZ9z-Nxu8mTdIbp2cef9NxNvH60fcdLA4lbQsTIEhhH5oWax1r2Onw083lH-uAfF2t8XN9QIQ38nLcCtsvLiWiHrpuvmY2f3bnPyshKVTfoyr8MrGQs7qjOJRCtYkwOZpkLEV5_LF2ZQNg70k_mNuQdiAljH-gSiMybxE-FTH8lUKS72ikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر تاکتیک ایران در تنگهٔ هرمز
🔹
سازمان تجارت دریایی انگلیس اعلام کرد که از ۲۸ سپتامبر تا ۸ اکتبر، دست‌کم ۱۵ نفتکش هدف گرفته شده است.
🔹
برت اریکسون تحلیل‌گر حوزهٔ حمل‌ونقل و امنیت انرژی می‌گوید این الگویی‌ست که در بیش از نیمی از گزارش‌های منتشرشده طی دو هفته گذشته دیده‌ایم.
🔹
به گفتۀ او ایران چنان با سرعت و شدت بالایی کشتی‌ها را هدف قرار می‌دهد که به‌وضوح به نظر می‌رسد آمریکا و مرکز عملیات تجارت دریایی انگلیس مجبور شده‌اند انتشار گزارش‌های مربوط به حملات به کشتی‌ها را با فاصلهٔ زمانی انجام دهند؛ چون تعداد بالای کشتی‌های هدف قرارگرفته در چنین بازهٔ کوتاهی، از نظر رسانه‌ای و عملیاتی تبعات بسیار سنگینی دارد.
🔹
اریکسون توضیح می‌دهد، ایران با چنان سرعتی کشتی‌ها را هدف قرار می‌دهد که حتی پیگیری این حملات هم دشوار شده است؛ اما در عین حال، دامنهٔ حملات نیز در حال گسترش است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/467184" target="_blank">📅 01:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467183">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نیویورک‌تایمز: شرکت‌های چینی برای عبور از تنگهٔ هرمز به ایران هزینه پرداخت کرده‌اند
🔹
ترامپ روز پنجشنبه نوشت که هیچ نفتی که از تنگهٔ هرمز عبور می‌کند، متعلق به ایران نیست.
🔹
با این حال نیویورک‌تایمز به نقل از افراد مطلع از گزارش‌های اطلاعاتی این ادعا را قابل…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/467183" target="_blank">📅 01:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467182">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEXIvPqik5biOtuVqNgL8QdCHwh-IEpPAkFZcoDvR2ruT-yYhe08RO2PKb7OZ42_z4HUYA-X3jUrdO83uK1FmUE8KqGfXKva8IuWDFtRe6yfxeRLtufv7NtXG2k09SE1SSTR4ESginnjRuBoqvSp7xxN4wYQ2E1By47_ReoNQ2D6x7LbCfm53Q1vg58d8pRNUeMuiXuw0HONx4NPIMNvtYNM6ruR2ffnj_bk5FDUf9k5u8-rTVmjWojcUkdWCCDEYwdRuKxQo7zl6rfkmh2P4rXV7OEyqy6UxwAdt0gskEnqWXeu8y5TfaSlzkfZ6zDBJJPl5txAwwp9WWoSNfjWxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروغ ترامپ دربارهٔ «مذاکره با ایران» هم نتوانست بازار نفت را آرام کند
🔹
وعدهٔ دونالد ترامپ، رئیس‌جمهور تروریست آمریکا مبنی‌بر اینکه ایالات متحده پیش از انتخابات میان‌دوره‌ای حملات هوایی علیه ایران را از سر نخواهد گرفت، نتوانست از جهش شدید قیمت نفت جلوگیری کند.
🔹
همچنین ترامپ در شبکهٔ اجتماعی خود نوشته بود «گفت‌وگوهای سازنده با جمهوری اسلامی ایران» درحال است.
🔹
بااین‌حال، روز پنجشنبه بازار نفت پس از کاهش کوتاه‌مدت قیمت‌ها به سخنان ترامپ واکنش چندانی نشان نداد.
🔹
قیمت نفت خام برنت که در مقطعی به نزدیک ۱۰۶ دلار در هر بشکه رسیده بود، در پایان معاملات با ۴ درصد افزایش، روی ۱۰۴.۲۸ دلار بسته شد.
🔹
نفت خام آمریکا نیز معاملات روز را با ۳.۶ درصد افزایش و در قیمت ۹۱.۴۹ دلار به پایان رساند؛ این شاخص پیش‌تر تا نزدیکی ۹۳ دلار نیز افزایش یافته بود.
🔹
سایر قیمت‌های مهم انرژی نیز از پیام ترامپ تأثیر چندانی نگرفتند. معاملات آتی گازوئیل در بازار اروپا ۶ درصد جهش کرد و قیمت نفت گرمایشی که به‌عنوان شاخصی برای قیمت سوخت جت نیز مورد استفاده قرار می‌گیرد، بیش از ۵ درصد افزایش یافت.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/467182" target="_blank">📅 01:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467179">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTEXKi-NKYfhYrxl0lL15HapCuH2jLLVPKbKRSo-quSvzB_nyfCzcumaiDTHmQuwHc7b9pW9aZdIyVDK6r-4ddjv93T4WnNgl_DlMmVkHDYxXvIhI9iXdiiauqcFXf-YgC_vqjP7SZmY87hL677K74UGoBXnptF7LYG2DWTyRG6H-j6ld7eBEi_OwZkCSLAHJ8JWPugAFokYvaPQuu9dqppYCX45VePawaDfIeqxwMlzoHXpG1rLajogRdY_X24e4GJmZJpDes2fwJz1erkf_Y2i-o4V6vfKASmZ7M4jEwkjY5StgTP5DHtmLEfIlS_yOG8ra3iRBjOhROeM8s1qdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NE8QzdAcav_WDJ4CBkCreMyNDWPDBoDdrJogDauhPzGDP24CesbXznH5mmQOQXqhle5WKDBhLmk2_TrdPAAreH1JVEi45PTEm4qOjcIk_fMoiAwJKcxMyi5xQvlxutw9D7FoXVViTlEr3jBsRfuPecs_DznwsNYgkjy6QbM1T7eiGmsyUS93C8t8u55y3KRgC4RwkFRWlFz1l7E64iUxeb2Gpxa_74y4-qvWRFFB6Ig5aYmp9_nvhxjltWWJFl0tAswTfpFiQO8000d8OQEv-sf9uasElVY_JMcGbY0YjfIjofvzeTnz96HenrGHW_JeC45NAWaxNO809U383fY_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frLoPoLamPrre75JWtKInY65LQMADv89ucUHgN5ZTmScMLOi396ok6tAkq9d39nxuZYfSkTU_CM4TYAIqyaYsXnrpxFWei0O2QVvjftx7TdwgL9GIAGq40wdw0yANFN8p5Bnt5i8u6Vdu_3BTncBt3vxbjE7v_jjTAdXyv1BKJVzqIUZu_BwrC1bbPaYvtS9qUZLl25ZKVb0R76PyQWCzosE0uXUK8w3UkpJDxF48Qw8juPmKGGsym3W5qcod4P6HW0blcL24KcLorCenMDLZ61rlXJb-yN95xJzcDvGwkhk-elEw9MBgA5aJ5eiGU-A7D5fgVPnyriz8y-cox1qTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
۱۰ خبر امیدآفرین در حوزه‌های اقتصادی، فرهنگی، علم و فناوری و زیرساخت‌های کشور
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467179" target="_blank">📅 00:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467178">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نیویورک‌تایمز: شرکت‌های چینی برای عبور از تنگهٔ هرمز به ایران هزینه پرداخت کرده‌اند
🔹
ترامپ روز پنجشنبه نوشت که هیچ نفتی که از تنگهٔ هرمز عبور می‌کند، متعلق به ایران نیست.
🔹
با این حال نیویورک‌تایمز به نقل از افراد مطلع از گزارش‌های اطلاعاتی این ادعا را قابل بحث دانسته است.
🔹
این روزنامه نوشته ایران به برخی کشتی‌ها که هزینهٔ عبور پرداخت کرده‌اند یا احتمالاً حامل بخشی از نفت ایران هستند، اجازهٔ عبور می‌دهد.
🔹
مقام‌های فعلی و سابق آمریکایی همچنین می‌گویند ایران ناوگان نفتکش‌های موسوم به «ناوگان سایه» خود را در اختیار دارد.
🔹
طبق ادعای این روزنامهٔ آمریکایی، شرکت‌های چینی برای عبور از تنگهٔ هرمز به ایران هزینه پرداخت کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/467178" target="_blank">📅 00:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467177">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5bdb68dc1.mp4?token=PH6rJHiR7ce6PCYdIMTA3vVhTGVKsreLDDY9hwSNgSPBl3-3Zv6X0_zFxcU-5oIXfes9mxU_Fqb3MYKtOM-9Qk3_Zbo6hPJErSHcE1G78aPuJtlUb2GPcz1kwx3w9_TVSA6GzKHc7jYlozceYR-UB_EeS8JDjb2WKLEorvi5iOM1YT99fGfYEkXsj6SSm3Oxn_2iAuz-v5RdiS-U1bOHOQUbJq_b54FYHGrpJlVbYw8eXtpbdSaXg9qHltOUysP6re3_s07JlZOtV_uWwiM9kHPyRTWAIvR2LxmgO6H7OUqRF9V_9MbkkTS0S860zG4BCHImyoJUxDoqypyGQjkPSwp5HnFeEyBioNTMSitMHdjJ8kFQaSp28QS58Fhxq9rAAU1aOubhtpW7NR6c1K8uLW31R3p8MCUdEketXT7ZDgNyi_C28ldDnfhawfRx-wKw8qJfKRuzKn31zdYHkk8-xdDecOSOd6mazDd5mzHP_PMX_GC6qYb-aa3Juxz9dw9m-SJe7YtMvKu3QJ7gE97oAgUUoreGVGtJvJd3NRG_ZlxO_QWwAxhTvURCkmAAb6AlN7piMOikbIq16KGc2PGCGEMp4beXBkUOdeYleGYSDdFKVW5HKAG2tqsKSRY8CzSHom5RDO2cd1YhTEeTEsEmvbfLGSTe5dFq2IkIwHAteC8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5bdb68dc1.mp4?token=PH6rJHiR7ce6PCYdIMTA3vVhTGVKsreLDDY9hwSNgSPBl3-3Zv6X0_zFxcU-5oIXfes9mxU_Fqb3MYKtOM-9Qk3_Zbo6hPJErSHcE1G78aPuJtlUb2GPcz1kwx3w9_TVSA6GzKHc7jYlozceYR-UB_EeS8JDjb2WKLEorvi5iOM1YT99fGfYEkXsj6SSm3Oxn_2iAuz-v5RdiS-U1bOHOQUbJq_b54FYHGrpJlVbYw8eXtpbdSaXg9qHltOUysP6re3_s07JlZOtV_uWwiM9kHPyRTWAIvR2LxmgO6H7OUqRF9V_9MbkkTS0S860zG4BCHImyoJUxDoqypyGQjkPSwp5HnFeEyBioNTMSitMHdjJ8kFQaSp28QS58Fhxq9rAAU1aOubhtpW7NR6c1K8uLW31R3p8MCUdEketXT7ZDgNyi_C28ldDnfhawfRx-wKw8qJfKRuzKn31zdYHkk8-xdDecOSOd6mazDd5mzHP_PMX_GC6qYb-aa3Juxz9dw9m-SJe7YtMvKu3QJ7gE97oAgUUoreGVGtJvJd3NRG_ZlxO_QWwAxhTvURCkmAAb6AlN7piMOikbIq16KGc2PGCGEMp4beXBkUOdeYleGYSDdFKVW5HKAG2tqsKSRY8CzSHom5RDO2cd1YhTEeTEsEmvbfLGSTe5dFq2IkIwHAteC8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عربستان برای جبران شکست‌های خود، به دروغ‌های رسانه‌ای رو آورد
🔹
سلطان سدح، خبرنگار جبههٔ مقاومت در یمن: عربستان برای جبران شکست‌های خود در برابر انصارالله، به‌دنبال رسیدن به پیروزی در رسانه‌هاست.
🔹
العربیه و الجزیره به‌طور گسترده دروغ‌های عربستان را پوشش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/467177" target="_blank">📅 00:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467176">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud94cgEwqHievbCOXutS-eCyhgL0DnRHs4wVHEM55pC8RKz4yRqXlGpH7JFkjJGW-uZih0Ye8Q1Ut7q_9b0tptithflpc1M15uVTMJmPsA5_av_ymdyKPh8AP1QWgBG3VgU6BB44QGUkkR39qArNNZ_PeMv5WtPThM3d8-qH_bpB5TBCmS4btDXq0noeDGAW2X1GvKvSDeZ7hi7ZGh6Y2OUXF6C1gfOvqZUO3yVWSlv1b62EqZYrZRPUil15cISXfLA1rrDgjTm9zAMIRkddZRe8-sQJUd9FZdn4n8bDZREnr00iOqFLtdN_q0wwkkMN4XVeuUCGR4bGrU7TcHJLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/467176" target="_blank">📅 00:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467168">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkFjOI_y1329ZFAAZWq9R59TkCNNJ_UMByDtGOfq2HLaiE5Nn4MggJoRmA0ggFcUpHELqMU-lfXv2qSV1DJs7XaGqPL2iX31vtdpNfa2jQX5g-MjtKtHqEwSdBBUNBO_pAOUD6UsTa3VFja5h1P4h_0sNp4r9d5lTvMi6ww7VTMC1BoRAaBWch9LSQYDkL2xeKaztjD9clK0Goyv0MM8S5Eu9tK1hgGyNBOXsjqae3bOHydU0q0gxveJJv9xW8piuZCkf_MhlOqDkWGkoPGkaNQWo558CoSwMhslT2Hsb-zftbhIu0TqOJrcLgJIPsD40fSfXFz2O1k50abWk71jbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyEKcLYDEE3aV-XGo8JosYcHJ6o_H08wvHMEAfA0EFPhEaCnX9oi5R4Wfr9wOutCEx6HW9vGRrT39rel81kXGBkgT3yllO2DIwCqG1Ys0nXdY9Ay-laLqQQf5BnXzU5UUJnd-TWyWN1KddU6p3ZpflLzu2j_FG0ghr5GfA8wI9eMkmC5qLhuCLctNv6AmiH-7o3K2iZccMJM8xLCr3aeNnNhv0myLazDiwoKrx04xq0i-8lsqqxPnvHQ6up03WUC_4vXs8Zrc6Gb69byBVpIeJRmv9RKdf_KVxgxoxMg4ZiUx0j2jdeeneJx5J83N7aUlunuPiKAo8wOg-yd3EiuXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lso_BI_f62ukq1m2LWP9pnGPwNqyOHkjDnHzb0iKhEWEkb7uOaRDRU-JsT3SyZPO4neT6uvtTO7PF-UI3Jq0JOx1d-ohNKSQEFxx-BMNpGA08KSrzg0P__O0ulrT4aF9M6gTt7N8ciktjJsBGg237zQ1Q47zcLG6_CZzbPOhG7rpA9qyNIhpZh0rQP28vt0JClOBalszEIBfawVrxC2C42wduV6c5I33aiCGcirSxo5j-4bZgYH8pJiIV5b-0kPiBdWf5qZwTtDRevBhppi5P2SH4KPsr_v2hexPDca1_dE1S5OVOILSjEgVJJz0tQN5MEsGy19XA-7r9qXTwCJNuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/euebMo3VQVmOfsrI-xEt-y-TDxDlYZuNynlqdce_qRadtGEfrK-36SDYJizN9WJIswP15MO6LHJYjF8uPCge61FIwcTm3I14wTtTOzENtJ1l2nEnk1i2pMIrnHU9nKiUC4Pgvm783hh01eOTd1W8LErwDT1npuyLKdxVJiI-f-rhbDAv4ZKTjtO0PijQteFt28BtpuOoZtNJ1McfBldSaUOAoG8vvPFMD6MtTwwaXQ-uBDTy6_TSNCUynwB6gYvUtxpz6m09MyUeqDmVTw9dOer-VwIHatBsPyhsaRguT_GHst6_xGTJrKUOeFCj-C9SvvVo5l34FjlQbvFiEKaQpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_G1o8DHh5xfB0Cd8xqEPeL2C-PIyRyZo21au1Bdjs2st9gjRoROLV9yx1jeRRX9Uz1S5dM-06Z1QVXAX_uRslxWrqbM5G-Kc91OSJOqvz-hojgzTCPGILLi1KILNFcScvYvq6mqMT8RlYNlX92OfEyTF0k__4BTcF65d0n4xQV4Hd67wr0sobPeIB5mlLzkOav11iFMvCIz_YnUBTtyAL6VxYpyR6LrXjA22UNFyV0kkGFidMAMNCzCLknmsd6MU87REbW6KBU0wTA_6WFiz71l16-yTIGT5ifhHHL7u78gcdDB1pKTyLQoQjZs8HHRlY3e2ZWqvgK6rLh-GAbSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLEUXUODzufpZxki6hQUauroEezVUcUpQkff2lcrX61fE_Sh07mHfSCuX3kxRb0Qu2mQDlxYgjmR41-oSMqt8xyuZ9OkyrX-1D3z3hMswBRXwL1NGVh592z9KAZi27vMSkGT8t8krOM00fjXPIVXAqCbSf2-ioIVzll4mm3X7rT0TXj50qHMZheRIcTwFkcKGlZ-cmULcwJlRkkVPcAE-2VfPKkShEWFwVEl70S-_Ll-lm3ZPGJ7tNXwzcxTdGA0A6RwSuKNfn8Hu3zeRNDw9D8R-iPCYh8gkYg4vs6Q5B1WyKIOi4y5wWrlSn7mY6jYQbekYR-_sIbJI4DrHVS7BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMSp62xyAVHPTWCDoDMJjMCy_O7PP5c_t56AT1A7qBZZehAy0cnw-FPPsxo5xJs4vmivy0mui31WroC4PtimSik83C2dg90DvTF0t0FM1MpifHIZ70xBN7tofjVxiRFEjdu2fflRE_bPya-2tW7uasnFhxI40oZVplerMYETVkh6fOXI7b2g95xAzKCxUW_by2BgckNeVWUT0ybtEQ5ox8cvOL8PDaFN5DC2L63ePGYavIGPVaqfN299STBCOmW_nqVq6b0nLJDayJlD4ITurmc3LniTiMjid7-aDiB_5oVNsfOzf174Q8U7_legSiEmx0ImbqieHWXjMwvY1nmaPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GClfqqgXy4nlrszThD4FEQSjc45HPNMJPVv-Zu-LSxMx5TGwc9DMkvOOvGuwbS37kz-PnNxnNnwZHN5q4606IKVCxKurP3ei8ufLOA1HZjNdkuRw8ONTepAInClsBy7pAzIx7kxTVXnIvkUeHrUF_2qO2-Jse8XcJLEyEmAaLbNapv74iPXSslJsPHFOT5JIrqlRUN-8cIxCa_T--zPP0QQF-m7G0hSnCpqe4hgc_Y-E6PpwmK1jpHy3QRfGpmK7FR5fVKvAwRzNZztvXaaR8edXRxudu8JVd-5TdwjLtr2X1A3zA00vUNBmEdvt8Cckf54gh7kFk_7SEgzaLTMlkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جانفدایان میهن در همدان حضور خود را به رخ کشیدند
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/467168" target="_blank">📅 23:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467167">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de6b8ec4e.mp4?token=R_LO9MlyNyeFE5Oclmgw0b9U9Xs_fIuLRzLijKCFxgYq601XxxzLA4jN-WQgZMGjG2aDmLKnzYIFlziqtdBmUkC_XQ8Edq7x-uP7a4fs4aTdpnABYI0ogdLes8U03iWwDKa71pU82sV7UkLXu2F9rKvBJmIoWv0k7GoXMuqgr2_WUI1joojqlxDGyN-kthOomW3kMGnk0-9e35xIrZOk4CGpCqU3cgvJE6zPqWjWvw5t3QcdKqjEl0IL6Xj5FB1W09zR1qhbdYB1yuR9j3wrvxiY7xU9FFjb9SgX2iAeVdzBC2vfjGxySCauMb0YO3NpmMHVpRhnQ9E1n4N0PuLr20Ao0EXlTTxvfh_tIyx06i11XCK--9HFAonsJcjuzZzZFkymaWderKDuhjY2yoV369umeyaKympYIMB3VTKJI73wn9fOERNm6DuwGcpvVYy0cdIbT7CdmU17krP63Ors3hNboEslW3AfIYqjOMzT0RULeeqp0Hy713vbQuMjJxxzvM6ToZrlSKqCHD_oj9zq7alwRPC7NK71_ujwIM1WloJy61HvVFB6M8v8Y49qYk-3pCvyMi55FrLAyTwTY8k6TcJfPdk3yvRsDX7XtRcW--4LXU0q2vK8RnuSLTRRa-LLBVNPynaShHcGzQWiu0cnMmsT1I_f27al8jGrvsvE5sI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de6b8ec4e.mp4?token=R_LO9MlyNyeFE5Oclmgw0b9U9Xs_fIuLRzLijKCFxgYq601XxxzLA4jN-WQgZMGjG2aDmLKnzYIFlziqtdBmUkC_XQ8Edq7x-uP7a4fs4aTdpnABYI0ogdLes8U03iWwDKa71pU82sV7UkLXu2F9rKvBJmIoWv0k7GoXMuqgr2_WUI1joojqlxDGyN-kthOomW3kMGnk0-9e35xIrZOk4CGpCqU3cgvJE6zPqWjWvw5t3QcdKqjEl0IL6Xj5FB1W09zR1qhbdYB1yuR9j3wrvxiY7xU9FFjb9SgX2iAeVdzBC2vfjGxySCauMb0YO3NpmMHVpRhnQ9E1n4N0PuLr20Ao0EXlTTxvfh_tIyx06i11XCK--9HFAonsJcjuzZzZFkymaWderKDuhjY2yoV369umeyaKympYIMB3VTKJI73wn9fOERNm6DuwGcpvVYy0cdIbT7CdmU17krP63Ors3hNboEslW3AfIYqjOMzT0RULeeqp0Hy713vbQuMjJxxzvM6ToZrlSKqCHD_oj9zq7alwRPC7NK71_ujwIM1WloJy61HvVFB6M8v8Y49qYk-3pCvyMi55FrLAyTwTY8k6TcJfPdk3yvRsDX7XtRcW--4LXU0q2vK8RnuSLTRRa-LLBVNPynaShHcGzQWiu0cnMmsT1I_f27al8jGrvsvE5sI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«جانفدایان ترکمن» سوار بر اسب به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/467167" target="_blank">📅 23:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467166">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3acb54a5c3.mp4?token=e9ImvktiiWpqFa4tUoQAtm7OwAKpICMMuzskNJ8ZdLCPj25luuVPEwiVqZ1tBOE_69FcYJ31HZnSsrilscRwajtFT3Rvd1Gt4SsiDMND1z3FUUrL3hMAfevRH4usgS5ylHjA23TDj5XLqwx5D5wV8UOY7Ixg2tw9O2H9KTP09OqfODoHSe7uq0tFBrK8W6YoN5Lx6PqhzEEc5Qx5QVqhKCbOaOxGBhN07q9ocZM4I4gxV8IXvohWCqEjy80_580amfJcBcdzBsoKxUFo15qcuTe2lPzKw4xRKGwEyWqCWBUDh0Bm9_uFUvlJJ57O0th_dE-0Ei8uaMKC6ol3mrePYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3acb54a5c3.mp4?token=e9ImvktiiWpqFa4tUoQAtm7OwAKpICMMuzskNJ8ZdLCPj25luuVPEwiVqZ1tBOE_69FcYJ31HZnSsrilscRwajtFT3Rvd1Gt4SsiDMND1z3FUUrL3hMAfevRH4usgS5ylHjA23TDj5XLqwx5D5wV8UOY7Ixg2tw9O2H9KTP09OqfODoHSe7uq0tFBrK8W6YoN5Lx6PqhzEEc5Qx5QVqhKCbOaOxGBhN07q9ocZM4I4gxV8IXvohWCqEjy80_580amfJcBcdzBsoKxUFo15qcuTe2lPzKw4xRKGwEyWqCWBUDh0Bm9_uFUvlJJ57O0th_dE-0Ei8uaMKC6ol3mrePYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امشب موج ۲۲۲ میدان‌داری مردم باغیرت ایران بود
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/467166" target="_blank">📅 23:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467165">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807406b7e2.mp4?token=BUcHnB5HwEbNcHjP0bP8-ZmlAnjaK8L4Jd-latdSl_viIcQVtpk2b-577DmGdWyx88KcL4Rc3GlYIKBWo1wQNs_Y2epLoy90zUOMZPBaQui2k2XuhqzDkDfj9vTxFvqVS_6qUqU7rYuC2VQKiz9MuRlwmVGhko6BcbFPBvElvKHjzDNxFvJIV0iTDRB0u0AY3VQhs-uQN9iU2KCbP1Gj3PFgwGN1gyQXqbtfGSagRL2FjC_w1SDQ26BZWdJTqRq65YV42aBT1lAZSudDln_lMjZM8ivIyDv8MiLup8M5ZTXirjCaMP98Jn8QgX0ryS7fpHnDD4itHBChc6sNxHmj9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807406b7e2.mp4?token=BUcHnB5HwEbNcHjP0bP8-ZmlAnjaK8L4Jd-latdSl_viIcQVtpk2b-577DmGdWyx88KcL4Rc3GlYIKBWo1wQNs_Y2epLoy90zUOMZPBaQui2k2XuhqzDkDfj9vTxFvqVS_6qUqU7rYuC2VQKiz9MuRlwmVGhko6BcbFPBvElvKHjzDNxFvJIV0iTDRB0u0AY3VQhs-uQN9iU2KCbP1Gj3PFgwGN1gyQXqbtfGSagRL2FjC_w1SDQ26BZWdJTqRq65YV42aBT1lAZSudDln_lMjZM8ivIyDv8MiLup8M5ZTXirjCaMP98Jn8QgX0ryS7fpHnDD4itHBChc6sNxHmj9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان در دیدار با پوتین: با ادامۀ یک‌جانبه‌گرایی آمریکا دسترسی به صلح غیرممکن است
🔹
ما از شما به‌دلیل موضع‌تان در مورد وضعیت منطقه تشکر می‌کنیم.
🔹
روابط ایران و روسیه در تمام زمینه‌ها درحال گسترش است. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/467165" target="_blank">📅 23:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467164">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
نفتکش‌های متخلف روی مین‌های تنگۀ هرمز منفجر شدند
🔹
پیگیری خبرنگار امنیتی و دفاعی فارس از منابع موثق نظامی نشان می‌دهد دقایقی پیش چند انفجار سنگین در معبر جنوبی تنگه هرمز رخ داد که ناشی از اصابت نفتکش‌های متخلف با مین‌های منتشره در منطقه از دریا می‌باشد.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/467164" target="_blank">📅 23:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467156">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSBHNhbdADV-TpiwE_qUBjh_yTX6onjQLHVTWKsrpHFK5cz0NsmbquUVEBzscyV9PnzbZzm0kKIta_77g5jd8CeAhQ_5yeruA8P7jKj0xz2aZ-w8hOE5CKYpFz_rW8gm5sdTaLBEYJJzsvARkJ7DK56stIS_h3OEgodd3Mkn0AvT9-Mo8wzBxztEj0nbDr1BsjdjQXrS2rhvJBQyVvQufk-Ik_859wareFV-W1fj7GznZis8B_BoUQmK5UpRoFiR6YLy6xBFJEzXnfs-FtjdSs0GppFvegndGSM5bFZrluSZvdpBU6_2qzDCuwq58T5udczh5dz4heFMLPsz8AQrPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3_otSk1GThD_X9j29IyyJlSYpMIP4X_Ci0-DaZKiHfz2u8H9zL5lkP3cVxQCkOv6vdgHSAhyFS8P8o1fsje57DUto2Ih5Ush0v_38y5rLml28kpvWFOQQbFPItL0jHeVN2YH1b-xeT9Pkn6rtAt1UNR7N8dU4srkIMivj6ma2MJPafCSY093YYArPpMCsWwxzu8aOFF4-KmiXmi_NbfnUVOMs98X0bRSNumaX3gFKSLj8sI4UBUq8DmBoR0gaTZjYozAlVqYVq_juLQDujQjtuTCVdw_faFl3DJ2rYy0b7cjiShkH_HtN_kuL5g0rou_3DBvYgQOIPew4gNRW9eCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8Jy74SPheB5ERqfVZWMw5jCLm9mgyvRNblT5aCUASXTlrDOv4fr4a_oj_C9FcVlSS2OdRt24DBmjsgUgAOeaHx_v8HuFo-T_HykRAsYk9IvffEF9E2EPVfhYKRJMoIdIHHxWUyb73f6ZpLEaQq6RpbOM7PmgVqIArJISsmx1y7yjvR-jfTt0QOuqCIUQR5vsANtxc6aJbbwEUa19FA_tKRvpD8gU_XTFeBTCXNAGU1MRcGnosp5-JKWOIwIMs5B4b5aVnVDN7uEv1g9NHl9rpb6v8CW7T3j26RQhsefo8_Gt7QwQtPaUIazvbRFuOgdK1NLeoAeag-fQ_aducpayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vqll832NV1WPylJVQEuCeRJr47eJHFufDKGEqd2t_cquyRXDUkL7qgA0TgvwgFCzYVFucMqWMA_gRj5fCOhT-OzaFhsP1oLx7dBaWY9ZJ_hBYHrjhHasQ3W39ILKt10WX6D4r06GbI2EPdAm01j1cxPxzzHfLHYzhjH46nHIVWGX00j4dAFTJPylnTXlOD-VTgZRqykqescp-NPDYFJAOd-G9KNgAkDzstv_JbFXJCKFBY_ljhiysSdtiFyuzuCvLyKEsh2-AzwKgoal2cNmzy-P7U5sM32cOH-bLFdlt9IHxVSPtFkZmKZgVbWEIGrRAmb4NbFgfO0VxRrqu5zGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gf26qXIaFC8SLLPpYdk3fdLmXzuQ-wcToJkas2kGLhUD76ZZbEmjen0koVefUZeOzaxX2WdDOUiq3ZtN1AA_A-Pv_wl168v_QnaD6pK3OZaXiwk4QjylN2T_L03oiY1xW9QETCU6h5d8OrqfQXhIL2cWJq34W8_G612nGsr0eJwM_OrFVkcKwdDBQQZHIFHyZkvRJG7zGHjZIKu8Sj0tx_YB0UYLZbXNG-VHkhYQKwunXLT-3p192mRWGqJDBZsduDI5mES4Jk7Kl7fWws1cFY0yzmbaJKxoW0g4iauCZzhH85RId3FfftU8TfhbIHrMEpSAZPYFrlBPdf1cmf710A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RULsaaB3M_FPaN5oQHmfT5e-V9CIAkralk6-zGy0rW29OvEwUJW3Q0QmEsQxAHs3K6QIAMAAxvYXODRjPhnMRkYFdClKoxFOUEFUtaPswL7jGhPUTIaBRmvjDCavkg3mhu3vKMzgTzexKlE8oDsdnei5zPRpHpt9DDA050YA-79ysLHh9A097_qtq8g2PqS2uBxz0REYx6fSruiJESVc1SNHfx1OGkdUnIDgxgcp95MHkMRW_-56dpKHZ5KJbaPEQde7Q9031u9_a2nriCy16PqSP3xosW9AnhOwCT4CJCnJ73pkB_ShMWdBBEsT9bFp_B9rvUrqjcZ7DS6Cjs_9Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWDotosqG8RJeSTeJ0axdsci__4UFIPFsh7EXYfcqgacvL6aiVLhpGET1bnrT4yvLMVuRQGTKSnPfHxqq3xJhNxRqxwr4_A43po_LT56bLEy_aquAbbD6YD8b2oY4MRF3Husfs_WMcdV2xwakdjVphEShNUZGKeFKYq3YZxISNyxVGlpKWMDz2Ye88tPtblfblsU1hMIh1WdpLQhm_GGWaBApc9m4XuexfRaAvoTWBZaeWb7_8oYFwTfjmtH1AnxW9sKFLUl36N7hfNI-H52xgbbEYVW8lu5rL7r5nRBlL1y9dN7LIHhisqUGtrO_XVA1CjZ_BF8xzZABO47Q3yEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VNwVtj6tWhuJwfckTI6dcklodhDWMgoDYhy2YVvfEyyXWhzdqrDYje3qFjnYV4HPxtB2GxkxTqQHqrhKjwtuED3YhYR3_x6tMK9orF7JgbuKHFER6tpZTA92S4aGAdV_ebymIh7vPVa0OIPO4oOCU4bpY8n-E6Hm3kI8SjgaeWcjIesP89paG5ETlpCUj1Z3iT0UgaOrTLlrLZ7JVsnLFq_LPw0KsQ22PMgNQtWNePBzX5hwlRXkjF5j9IWSmOJM7hfAkWu3bHIYMN7khjeVr-jWQy4LYBC5hnJR6idVyaiWQsOav4P2IcYdZkUSK6pl6nFMBis_KTNUnlGEoJH75g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نبرد استقلال و تراکتور به نفع پرسپولیس تمام شد!
⚽️
تراکتور ۱ - ۱ استقلال @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/467156" target="_blank">📅 23:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467155">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f79235cc3.mp4?token=WuTgLo-PbsU-OsijxOOQJUSElAuLHW6e4m8C-qq5Vr8xdnDpF0Kcbg9oS7yy7-Dc_zZLb7v1DS4GhPeS9jw6gyWTEParVWGVPU6iO3AAZwegmJToUaM0bf0iW0-o4MtW2mYNAQLROgNRHjgflp8YxJyTS8IxFvAIM5iOmvg95vEbI3JsBzDiR-f3DZwwG9Q1gFGXJnQRAxDD9aERNsgQ1qrDcdGLWfbFBMISBel6fplwT5aDGqRo4LC8lx8iJU49iy8pVrpxcLaaA7s9YgCvIkA3srj8VdMMOj5nTEXOBZXL0B26XuZm0ffM0UMVkpWXXvaBCbJ1faynME6GWczovJAuN_bSeoPjKdNmgk-EJLPo6LVjA7cq9dcGsReiu_CfML2uCqVEAyF3Y0kfB6S2cltlZPNtunjtmERSAP8DQN4QTCLNreqlTZsaKy8qX4dc2eYX6EEoF_UXvJ-ku5gjRdAjLHrbLvWorXwPBCUmz0upHn9jl-aazpAadqsdEPlcaQkqnveCvRuWzBjcZySAcmt-7d351uFpB7GbwYpXHbWWiJ-QTK-zjpGQsbkOZJJrytyWHp_Yoi0N9q-0dhTG0AGgKiURVRuNwfl_bSgKCH_rINDUIIPYMr4ZLoILeVuBT4FRPBqF84I2ZDSwNE1HHEIBjQ13uaNz0BwGdtoTSf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f79235cc3.mp4?token=WuTgLo-PbsU-OsijxOOQJUSElAuLHW6e4m8C-qq5Vr8xdnDpF0Kcbg9oS7yy7-Dc_zZLb7v1DS4GhPeS9jw6gyWTEParVWGVPU6iO3AAZwegmJToUaM0bf0iW0-o4MtW2mYNAQLROgNRHjgflp8YxJyTS8IxFvAIM5iOmvg95vEbI3JsBzDiR-f3DZwwG9Q1gFGXJnQRAxDD9aERNsgQ1qrDcdGLWfbFBMISBel6fplwT5aDGqRo4LC8lx8iJU49iy8pVrpxcLaaA7s9YgCvIkA3srj8VdMMOj5nTEXOBZXL0B26XuZm0ffM0UMVkpWXXvaBCbJ1faynME6GWczovJAuN_bSeoPjKdNmgk-EJLPo6LVjA7cq9dcGsReiu_CfML2uCqVEAyF3Y0kfB6S2cltlZPNtunjtmERSAP8DQN4QTCLNreqlTZsaKy8qX4dc2eYX6EEoF_UXvJ-ku5gjRdAjLHrbLvWorXwPBCUmz0upHn9jl-aazpAadqsdEPlcaQkqnveCvRuWzBjcZySAcmt-7d351uFpB7GbwYpXHbWWiJ-QTK-zjpGQsbkOZJJrytyWHp_Yoi0N9q-0dhTG0AGgKiURVRuNwfl_bSgKCH_rINDUIIPYMr4ZLoILeVuBT4FRPBqF84I2ZDSwNE1HHEIBjQ13uaNz0BwGdtoTSf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکاوران نیروی زمینی سپاه در مرزهای غربی خطاب به دشمن: پا در این خاک بگذارید، خاکسترتان را به باد خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/467155" target="_blank">📅 23:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467154">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/684171b317.mp4?token=DS9Ol2ZjPRP-1BHKBWt251MdHF6urVKoptMHcxWBHfs1Rj5VxzsePwjnYM43vulmHDRtcfbBQWR16hqIRgFIjQxfaswd__ouiFXpOeweOYheL6uFt65vi2LIN6TdwiS2edluvE5pgG5Z_Tf7dB0sX5YsyEBjQ6A45-yAw-QWvAJ2pYS_TDQfg4o7M9dCtyV-IibUYuC4iBBmXwGcaL31U0tL3tFY6hbnEpVi4v6Gl0BDShA5MnbtLSWYqEHhLU-xYphNAi5hSdIto_BiORaWhv-6xLConQ0azklLDyQWXdNIJQt4GSgZJK5JqZ9HVweQ6VMw7AgF8Jlu4Q5MajO6mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/684171b317.mp4?token=DS9Ol2ZjPRP-1BHKBWt251MdHF6urVKoptMHcxWBHfs1Rj5VxzsePwjnYM43vulmHDRtcfbBQWR16hqIRgFIjQxfaswd__ouiFXpOeweOYheL6uFt65vi2LIN6TdwiS2edluvE5pgG5Z_Tf7dB0sX5YsyEBjQ6A45-yAw-QWvAJ2pYS_TDQfg4o7M9dCtyV-IibUYuC4iBBmXwGcaL31U0tL3tFY6hbnEpVi4v6Gl0BDShA5MnbtLSWYqEHhLU-xYphNAi5hSdIto_BiORaWhv-6xLConQ0azklLDyQWXdNIJQt4GSgZJK5JqZ9HVweQ6VMw7AgF8Jlu4Q5MajO6mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از شنیده‌شدن صدای انفجار در مقر گروهک‌های تروریستی در اربیل خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/467154" target="_blank">📅 23:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467153">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
منابع عراقی از شنیده‌شدن صدای انفجار در مقر گروهک‌های تروریستی در اربیل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/467153" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467152">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6A1r5XtMZhD-JC6pBZSerGo_bxriC11pSIZCCUnXPG0TCKrLjty5_i5e5KK4GL8VyGRerzo2NfW12FGJqM4undeBTIsINvOUpkI17CM_H2kZSOKFOWLI2PCk0qo4MGWCJBH3Z_md48q8QQUGqpLNZ_q47M3d2_DktZ0dbQCM8fL5x_98fUKzKRd6uWNXpxx949H-oTVuIQ-pdB2SoM1PdVL7gTMml-b25Ym1-IzM4ofrR8hAP8tWk8LgOCr-EC3YTtF2vngJV1NHmAwWNBxYGQnJM2Q2F0VBYqjMH-u6aJjax96A37kGiTYEObZfgYbasUQolVDmmJFBBEC6UPvRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخالفت عراق با تحویل ۴ هزار داعشی سوری به الجولانی
🔹
مشاور امنیت ملی عراق: با درخواست دولت الجولانی برای تحویل حدود ۴ هزار زندانی داعشی که تابعیت سوری دارند، مخالفت کردیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/467152" target="_blank">📅 22:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467151">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شهادت مامور فراجا در حملۀ تروریستی در فاریاب کرمان
🔹
سرگرد مهدی جمشیدی، از کارکنان نیروی انتظامی، دقایقی پیش درپی تیراندازی افراد مسلح ناشناس در مرکز شهر فاریاب، به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/467151" target="_blank">📅 22:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467150">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9547fda8b2.mp4?token=DO_0myEsxpf7AIbzpf4h6b0RRTeoof7H6uMhL8ghEr64XwwDGDgapGIAALvuCuSGchWm_e-poBoCn36ybp8uwIds_bPxfam_ELOJ5b7VWxuBhTRWrN4ZdoRfUCEQz-nLEpHSoEGwKBOAwsYyWpOsZVA0cletH5f0HdXuuwYPW29BbGKhouJDSzFK4r6ysl3GvggcR32nmlabeIMgQR6m0KUvXXfXaY6QJu5j_MLNIboFAE5DoNrqUNVEIK9htwh5p0mNrhmiIOcVUr3jxfulY0TJb0iK3wDLDZ7OAHue_3pbcXaoX2hyn1YJ2byq2K4SeWofVPzv1WlIO_hije3Ukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9547fda8b2.mp4?token=DO_0myEsxpf7AIbzpf4h6b0RRTeoof7H6uMhL8ghEr64XwwDGDgapGIAALvuCuSGchWm_e-poBoCn36ybp8uwIds_bPxfam_ELOJ5b7VWxuBhTRWrN4ZdoRfUCEQz-nLEpHSoEGwKBOAwsYyWpOsZVA0cletH5f0HdXuuwYPW29BbGKhouJDSzFK4r6ysl3GvggcR32nmlabeIMgQR6m0KUvXXfXaY6QJu5j_MLNIboFAE5DoNrqUNVEIK9htwh5p0mNrhmiIOcVUr3jxfulY0TJb0iK3wDLDZ7OAHue_3pbcXaoX2hyn1YJ2byq2K4SeWofVPzv1WlIO_hije3Ukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین در دیدار با پزشکیان: بهترین آرزوها را ازطرف من به آیت‌الله مجتبی خامنه‌ای منتقل کنید
🔹
روابط مسکو و تهران در مسیری مثبت درحال توسعه است و روسیه آماده است هر کاری انجام دهد تا به ایران در بهبود وضعیت فعلی در خاورمیانه کمک کند. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/467150" target="_blank">📅 22:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467149">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/333dc748c5.mp4?token=jEPDn8wZXUST1_TT05gF-Hbao_YtNFVqW7WMJ80VsX0-05fJgawsv8rcaY5Tm2g7dsos13nxIs6j5lOMpy_6EfI0TsRNNTPwg1hPR8sGo0FiEjzlpQeFPIqEBm9rDI_XXlqX5IT6dLPNwv2XbEjYPrlWTBqUNhBfQw76eezHAMXcceQpQX5vCmsXckZ5UBAKLKkwFyqpTFmO7gE9WawyV98KOLHPkg6LLKcO9aPlyJmoQ7X-ziulOz8m7okXNfdLJ6NH38hA61c2ox3GxgDRn5SNbwt6RAcSIui_0qK_5g8PWJBFHxlNdodlB1rYaRhceTNe4KXoKf0VPM8WwcL_Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/333dc748c5.mp4?token=jEPDn8wZXUST1_TT05gF-Hbao_YtNFVqW7WMJ80VsX0-05fJgawsv8rcaY5Tm2g7dsos13nxIs6j5lOMpy_6EfI0TsRNNTPwg1hPR8sGo0FiEjzlpQeFPIqEBm9rDI_XXlqX5IT6dLPNwv2XbEjYPrlWTBqUNhBfQw76eezHAMXcceQpQX5vCmsXckZ5UBAKLKkwFyqpTFmO7gE9WawyV98KOLHPkg6LLKcO9aPlyJmoQ7X-ziulOz8m7okXNfdLJ6NH38hA61c2ox3GxgDRn5SNbwt6RAcSIui_0qK_5g8PWJBFHxlNdodlB1rYaRhceTNe4KXoKf0VPM8WwcL_Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: تولید تسلیحات ما در طول جنگ ۲.۵ برابر قبل جنگ شد
🔹
ما از قبل جایگزین‌های امن برای مکان‌های تولید را درنظر گرفته بودیم و حتی یک روز هم تجهیز و تولید برای نیروهای مسلح قطع نشد. @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/467149" target="_blank">📅 22:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467148">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff8ba101e.mp4?token=A_tSSalKIusDoZYkA9GPHLvGUlmoYJtaIIHhl6YUCHnHUWYozdN7m-402f2M7_-2QRh1y9jKAwaAvp56YUnGiUlAxaolbPM1rs0oxkdansjmbv2QkB2cez6ESM_DQva0ThSnjzgqbZzSr0ztR9JTsRGuIgqlXXf1pU7HW37apFqcao3qV1Mw_6w5_JnM_VZckxnFymN9m96edTBqwCMnb8XTd2OWbPLasaHHE013m5yWJ8xqkIUxPc0YSP8RHFcEXRBSJ_3yTcvKh2p_E2x1HxVbXK1QkBLT9FXwDGdTMnzczLRlZua0HLIOcwxjhLwdyrzY1ALM8pnGlI0xVpOGqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff8ba101e.mp4?token=A_tSSalKIusDoZYkA9GPHLvGUlmoYJtaIIHhl6YUCHnHUWYozdN7m-402f2M7_-2QRh1y9jKAwaAvp56YUnGiUlAxaolbPM1rs0oxkdansjmbv2QkB2cez6ESM_DQva0ThSnjzgqbZzSr0ztR9JTsRGuIgqlXXf1pU7HW37apFqcao3qV1Mw_6w5_JnM_VZckxnFymN9m96edTBqwCMnb8XTd2OWbPLasaHHE013m5yWJ8xqkIUxPc0YSP8RHFcEXRBSJ_3yTcvKh2p_E2x1HxVbXK1QkBLT9FXwDGdTMnzczLRlZua0HLIOcwxjhLwdyrzY1ALM8pnGlI0xVpOGqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: تولید تسلیحات ما در طول جنگ ۲.۵ برابر قبل جنگ شد
🔹
ما از قبل جایگزین‌های امن برای مکان‌های تولید را درنظر گرفته بودیم و حتی یک روز هم تجهیز و تولید برای نیروهای مسلح قطع نشد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/467148" target="_blank">📅 22:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467147">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63730388b2.mp4?token=aFdMx4fAYyjY7baRfKFMcvm-nbCY_jH-j4wJ5ZW0oNyR1SEzKsl-hQfhqTJsBb_lMmLkzLW5ZoOVx0yRrBgS0qmXczzayzogNLPztlJJTir5-LuWuqvikIOOE0JCTYE3ehLbF8Iok06U7f1wWZZO4t9eBtxxkob2QcvWo7RO4bwoBqWNDUURR7J5wriC9Sz1sHTMsprz-0Rdmf5RUv3qZc1dBmdrDGHusjNJKunD2EI-GkuM0pk_A6q1kei3k68zKvRm2qEhuyThbV9wUY_L3BEOhMweyvIpxLrH9wrWt7hd-Q_-XwMr9rcWDTXFn57jXCBuDvOXSRSIVy4TFa2y2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63730388b2.mp4?token=aFdMx4fAYyjY7baRfKFMcvm-nbCY_jH-j4wJ5ZW0oNyR1SEzKsl-hQfhqTJsBb_lMmLkzLW5ZoOVx0yRrBgS0qmXczzayzogNLPztlJJTir5-LuWuqvikIOOE0JCTYE3ehLbF8Iok06U7f1wWZZO4t9eBtxxkob2QcvWo7RO4bwoBqWNDUURR7J5wriC9Sz1sHTMsprz-0Rdmf5RUv3qZc1dBmdrDGHusjNJKunD2EI-GkuM0pk_A6q1kei3k68zKvRm2qEhuyThbV9wUY_L3BEOhMweyvIpxLrH9wrWt7hd-Q_-XwMr9rcWDTXFn57jXCBuDvOXSRSIVy4TFa2y2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرۀ سعید جلیلی از جلسات با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/467147" target="_blank">📅 22:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467146">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa2e248cde.mp4?token=CN-v2euw4EYMxvC_eX8t93Yw-0etq6CdKHMEms9op1QzZbUX4abLsAc4CTm6UkS9ocqgLP4e2rW_j3EWFVWTXPoZWBtoMUa_DAjGNuLaC9aMHff_H8nxsUE586IC0gmOP86KhDFZdlQs1mLcHyeTULBJEZbw3JXYg66VRqg8n5wLd1mFelC3tkHXrKXQFBtCjc5QVmrJe3vAEw8dXzTJ5i3OTLtLAFo9fngTzaQEUnlQ8y-lCMsA06Ytl-VpgP3yXFv-_FSNh0vuIBdaTs0Mvz-L2sztb1-0MPpm9VJyWqC9y6r_ocV1Y_40UrqcDIKEVBlbBXmoUtKKfLY8gHrVWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa2e248cde.mp4?token=CN-v2euw4EYMxvC_eX8t93Yw-0etq6CdKHMEms9op1QzZbUX4abLsAc4CTm6UkS9ocqgLP4e2rW_j3EWFVWTXPoZWBtoMUa_DAjGNuLaC9aMHff_H8nxsUE586IC0gmOP86KhDFZdlQs1mLcHyeTULBJEZbw3JXYg66VRqg8n5wLd1mFelC3tkHXrKXQFBtCjc5QVmrJe3vAEw8dXzTJ5i3OTLtLAFo9fngTzaQEUnlQ8y-lCMsA06Ytl-VpgP3yXFv-_FSNh0vuIBdaTs0Mvz-L2sztb1-0MPpm9VJyWqC9y6r_ocV1Y_40UrqcDIKEVBlbBXmoUtKKfLY8gHrVWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمن تصاویری از درگیری‌های زمینی با مزدوران سعودی منتشر کرد
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/467146" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467145">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حملهٔ مسلحانه به مینی‌بوس حامل کارکنان نزاجا در نیکشهر
🔹
روابط‌عمومی لشکر ۸۸ زرهی نزاجا: ساعتی قبل مینی‌بوس حامل کارکنان لشکر مستقر در سواحل مکران که برای تعویض شیفت در مسیر بودند، مورد حملهٔ مسلحانه قرار گرفت.
🔹
در این درگیری یک نفر به‌نام محمدرضا اوکاتی…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/467145" target="_blank">📅 22:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467144">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNNOnWBfu1yWaAACI158Jr37Kvmq3iQyT3KdHIdXXW_tW_OayJEE3H_hDjUnoJA-sQr4WJSd_Eij_xztqTs6YmS2ew9gQq8gdgDB389Ulx0fg4XsaZEyZMluVGwDY7eh2BBHA8xRI3WcVUfObyHTGUtTFw2Gm-C1QZ5WGgnRYyDJDlT76ZzUO01HXSd-3f2wDxedBi-dokmfO33m3X5a-4PtFbO61pRbT3exiy4ikOW7jlGdHfJYBKWvyQVZBC7CWxYNHaPbJTjrEULprgYvbB9GuJCqZMyJC004iJ2UPT3Pn5gAvNwekIIX4ARM8dTSGSp628f2pV-Zpsuubaw7ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پزشکیان و پوتین در ترکمنستان باهم دیدار کردند  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/467144" target="_blank">📅 21:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467143">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqMP6K6UmaEseDohALcbHp3qN1nslnx6vSv_PSziSiQ87McxAfJAUVwmYuLdaP7YEk8R08UMU3OxPznbF5u04GFfDyHNLpQElDi81FtOkxZM8UGCrsuhU7aO2vm9LyzwgfZDVv26dE_XiloQD4ZxtjLxWYY69eKpwJyItQ61R7oJr3tW3InV5mwR2lLLzr5wE13evsxmhnU5dlYcL2sBjAvC3sawGQpiUoLW5tx4WubnoDvpwyEOoLTUAwAcizir147dq15RSIYW3-zIY-hTDVWsWf--3A-6JB-6MOrspYZCk-VD3wZCBH698CsC9ir_hlPIJIYrIn4iZO9IIIERsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرانوند از تراکتور اخراج شد!
⚽️
با اعلام باشگاه تراکتور بیرانوند به دلیل مصاحبه علیه زنوزی، مدیرعامل این باشگاه بعد از بازی با استقلال از این تیم کنار گذاشته شد.
🔸
بیرانوند در مصاحبۀ خود پس‌از بازی با استقلال گفته بود: از مدیرعامل تراکتور می‌خواهم به‌جای حاشيه سازی برای دیگران، اول داخل تیم خودمان را درست کند و حقوق بازیکنان را پرداخت کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/467143" target="_blank">📅 21:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467142">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXFGJ0BsPcoFaKdwPe0meUzm03oIOpV5-_S9738hey-BNLZzKWB6ABjDF8zUgb-9grxrnwyo9fQhoB8oZse3hERk7L7AnmM4SYtiW6RliYB4yEMN5UKOIc1dTrEfIlFiPowzq89GdY3_V4K2cpjnmaH22c3c9tfwJyZ2pCp5GenK13HpLRsf8nnpTmfxLxhYvJEdFAAAbyZDsYzRUdlkvhoyB_ZRX9lyWkHsig2ShPyLjQaSMZ4PL1iS8Ugoq3_vhC3RAquzW5TiDuDyClWnV7Yaa54054bPDh-0xyfs_MTSdmK-6ZlOWv2KYd3-clakegRNBaDaedMLK8wKG7irHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتین با پزشکیان دیدار می‌کند
🔹
دستیار رئیس‌جمهور روسیه: ولادیمیر پوتین در جریان سفر خود به ترکمنستان در ۹ اکتبر با رئیس‌جمهور ایران، دیدار خواهد کرد. @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/467142" target="_blank">📅 21:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467141">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57bd1e81bb.mp4?token=PprmEj2dp9Yhj-gYaIbdDV7jtI_AIn4-B4Fs4aDQTRAwkCHiyHpMvYTKTei5zDRsD-W29JBy6AN4SXR_ZqIXv3QaWPrk5UHdufNakrgOjNCjrIlJ_F7k8v1caN60B1sG-dZr4DhRdD82ht7BdL2mIJ-qXcNBfVvPNFicy5kW6N4fyBKmfyy5LTS8_RhAi20BT0R1HwEuZ7vcjzYmxnCkMqOHSwEGb0XIF5hVs1EC6uxFGVOuED8CyCe7cvp_-WuIQ2ahgvapnEsaCVAdoqW7awDc0qt4QqmQ3lpud2WTtvWgVI_oFdvqIX1GYWeyvSc0Btjydjg5BHYQikjFHlFayip2NSCU8ErvDAP6VFh0xzsNfgjOus4LxmgALHFVEl1r_-G-iUdth2DQSIeRbK6_YceYyhDPXffuxuTfcorBZTF6mbPs42nyIpIJLI17ZRBSHMdItbT_bYUI1XpzYMAaMV50ntPKzn6oQab0XGB6Q4VG445kcBhKqa20b1aBSdp-Uv3WD6RPqyC23RGtmEvkz4nEiT1RKXdKIwsOSTriQnfZX3b4I-bhL9iEsAbBCWpwFVD0WwOHPCD6lCSQ3etOVKWC6bevBTmVO86kZvfs2M4rJeoAI8iwQaW4xtRzWzHA3qwXxRzPtID0HejvgbollobhjPXa-6CyoxPXS7Wqw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57bd1e81bb.mp4?token=PprmEj2dp9Yhj-gYaIbdDV7jtI_AIn4-B4Fs4aDQTRAwkCHiyHpMvYTKTei5zDRsD-W29JBy6AN4SXR_ZqIXv3QaWPrk5UHdufNakrgOjNCjrIlJ_F7k8v1caN60B1sG-dZr4DhRdD82ht7BdL2mIJ-qXcNBfVvPNFicy5kW6N4fyBKmfyy5LTS8_RhAi20BT0R1HwEuZ7vcjzYmxnCkMqOHSwEGb0XIF5hVs1EC6uxFGVOuED8CyCe7cvp_-WuIQ2ahgvapnEsaCVAdoqW7awDc0qt4QqmQ3lpud2WTtvWgVI_oFdvqIX1GYWeyvSc0Btjydjg5BHYQikjFHlFayip2NSCU8ErvDAP6VFh0xzsNfgjOus4LxmgALHFVEl1r_-G-iUdth2DQSIeRbK6_YceYyhDPXffuxuTfcorBZTF6mbPs42nyIpIJLI17ZRBSHMdItbT_bYUI1XpzYMAaMV50ntPKzn6oQab0XGB6Q4VG445kcBhKqa20b1aBSdp-Uv3WD6RPqyC23RGtmEvkz4nEiT1RKXdKIwsOSTriQnfZX3b4I-bhL9iEsAbBCWpwFVD0WwOHPCD6lCSQ3etOVKWC6bevBTmVO86kZvfs2M4rJeoAI8iwQaW4xtRzWzHA3qwXxRzPtID0HejvgbollobhjPXa-6CyoxPXS7Wqw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
ورود پزشکیان به ترکمنستان
🔹
رئیس‌جمهور به منظور شرکت در ۲ اجلاس سران کشورهای مشترک‌المنافع و اجلاس محیطی زیستی دریای خزر، به ترکمنستان سفر کرده است. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/467141" target="_blank">📅 21:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467140">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBHW6Ayic2Ilj7nMV88iiU-g1Q-D6H6_ybeOLB9-BVJX5fOwOELE2P7qUryATowcufoZd-wzAWWwQOc59sGREn6HOVXWLR56rrh48FT1SjPr3vYWoWWFTvzrvCXrmlgHxuYHu5myJTNgGmsWA9W8aCzcTDZ6e9gpXyqfVhbPm47U_MpwVNKZsJhu-6Y1xc8QKLmb78Wubao8X4VsmVCDQ8R4PZfr_J-aqJBIxsLRqJkN7opXAWfa7voI83NiPzEfV2X4jl3bVqu7G-Q84HlK0kC_-lF0zuP23MWJxaHO4yqm8KPH3FP-nAKZ-Xn_JjTNZdlG0V-3aj2PymvY17k-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر ایزدی: رزمندگان سپاه و ارتش برای دفاع از تنگه هرمز آمادگی کامل دارند
🔹
جانشین فرمانده‌کل سپاه: تنگه هرمز متعلق به ملت ایران است و فرزندان این آب‌وخاک در نیروی زمینی، نیروی دریایی و نیروی هوافضای سپاه، در کنار برادران خود در ارتش جمهوری اسلامی ایران،…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/467140" target="_blank">📅 21:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467139">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b81e58d9f.mp4?token=dfBwuPvLagby6MGk71dytB9m8HQYTabf0TPyFQSEH8wNQvOU6kaJEyB0TPIt3rv8C6KTXlnhuy6b-lSGiAdyVGbqlxYnTmio4INOrf-j-aiEBadF_KOvabgeRiDlXeIxj4Mmi4fmyetRM8TXgXvhtDS0PMXJzwTD98jaLczYDxo8OUwp600jSwYtxySZv_x4W0iL1jYzP_SyNerCkjzw5X7LbJkYFVCFe8k8lW3TjzvIyjLwfVCNpZehMVa6wIDb17yylUXzANvC-_l3BWMQveAaUcN6GFcQsu501Uc_pVeuB7gj0s8UpTmvPyaFiNECeGtnUQDO3Af2Kb2LU9JqKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b81e58d9f.mp4?token=dfBwuPvLagby6MGk71dytB9m8HQYTabf0TPyFQSEH8wNQvOU6kaJEyB0TPIt3rv8C6KTXlnhuy6b-lSGiAdyVGbqlxYnTmio4INOrf-j-aiEBadF_KOvabgeRiDlXeIxj4Mmi4fmyetRM8TXgXvhtDS0PMXJzwTD98jaLczYDxo8OUwp600jSwYtxySZv_x4W0iL1jYzP_SyNerCkjzw5X7LbJkYFVCFe8k8lW3TjzvIyjLwfVCNpZehMVa6wIDb17yylUXzANvC-_l3BWMQveAaUcN6GFcQsu501Uc_pVeuB7gj0s8UpTmvPyaFiNECeGtnUQDO3Af2Kb2LU9JqKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جولانی دورترین گل لیگ را زد
⚽️
امیرحسین جولانی بازیکن تیم فولاد، در جریان بازی امروز تیمش از فاصله‌ای از زمین خودی توپ را وارد دروازۀ مس شهربابک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/467139" target="_blank">📅 21:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467138">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌ رهبر انقلاب: استفاده از فناوری‌ها و هوش‌مصنوعی نقش مهمّی در کیفیت مأموریّت‌های فراجا دارد
🔹
تقویّت همه‌جانبۀ نیروهای حافظ امنیّت از جنبه‌های مختلف انسانی، سخت‌افزاری و نرم‌افزاری خصوصاً ارتقاء فنّاوری‌ها از جمله استفادۀ هدفمند از هوش مصنوعی در تحلیل داده‌ها…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/467138" target="_blank">📅 21:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467137">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌ رهبر انقلاب: ممکن است خیلی از اوقات زحمات و فداکاری‌های حافظان امنیّت، نزدِ برخی افراد عادّی‌انگاری شود و همین مظلومیّت و گمنامی است که اجر آنان را در پیشگاه الهی افزون می‌سازد.  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/467137" target="_blank">📅 20:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467136">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌ رهبر انقلاب: نیروهای فراجا با رفتار اعتمادآفرین خود می‌توانند اعتماد مردم را به این نهاد ارزشمند ارتقاء ببخشند
🔹
ملّت مظلوم و مقتدر ایران، قدردان زحمات و تلاش‌های بی‌وقفة خدمتگزاران به امنیّت کشور هستند و متقابلاً نیروهای فراجا که همانند ارتش و سپاه از عمق…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/467136" target="_blank">📅 20:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467135">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌‌ ‌رهبر انقلاب: امنیت کشور، مرهون رشادت و شجاعت نیروهای فداکار فراجا است
🔹
امنیّت، از مهمترین نعمات الهی است و برقراری آن در نقاط مختلف ایران عزیز، از شهرهای بزرگ تا جزئی‌ترین واحدهای جمعیّتی در روستاها و محلّه‌ها، از مرزبانی‌های سخت در شرایط دشوار آب و هوایی…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/467135" target="_blank">📅 20:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467134">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رهبر انقلاب: نشانه‌های تأثیر پررنگ فراجا در جنگ‌های اخیر آشکارتر شد
🔹
نقش پررنگ فراجا در سطوح مختلف از رده‌های فرماندهی و ستادی تا کلانتری‌ها و پاسگاه‌ها برای تأمین امنیّت در سال‌های اخیر برجستگی بیشتری یافته است و نشانه‌های این تأثیر در جنگ‌های تحمیلی دوّم…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/467134" target="_blank">📅 20:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467133">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رهبر انقلاب: نشانه‌های تأثیر پررنگ فراجا در جنگ‌های اخیر آشکارتر شد
🔹
نقش پررنگ فراجا در سطوح مختلف از رده‌های فرماندهی و ستادی تا کلانتری‌ها و پاسگاه‌ها برای تأمین امنیّت در سال‌های اخیر برجستگی بیشتری یافته است و نشانه‌های این تأثیر در جنگ‌های تحمیلی دوّم و سوّم آشکار‌تر شد.
🔹
تمرکز و اصرار دشمن جنایتکار امریکایی-صهیونی برای ضربه زدن به رده‌های مختلف فراجا از بالاترین سطوح تا سرپنجه‌های آن نیز اهمیّت این نهاد را بیش از پیش عیان نمود. امّا این تلاش مذبوحانه و ضربات خباثت‌آلود به ارکان نظم و امنیّت جامعه که مشابهی برای آن در طول تاریخ موجود نیست، باعث نشد تا نیروهای شجاع فراجا ذرّه‌ای از مأموریت خود کوتاه بیایند و حتّی در خیابان‌ها و خودروها، همان نقش و وظایفی که در اَمکنه و مقرهای خود ایفا می‌کردند را به انجام رساندند.
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/467133" target="_blank">📅 20:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467132">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قطعی برق برخی مناطق تهران درپی وزش باد شدید
🔹
درپی وزش باد شدید و وقوع طوفان در شهر تهران، برق برخی مناطق پایتخت قطع شد.
🔹
عملیات رفع خاموشی در مناطق آسیب‌دیده درحال انجام است. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/467132" target="_blank">📅 20:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467131">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgoOp0wE9uI3RjgkddOjAnSbgcelL_TW2b8M3YPMgYCcKPd9Q70fH-6p9knXAdduhbPUIO0Ku8C7SO4MkWHngA2Kve488FfwAx0WUKYb3QCt2ZgYuRAH0TGg2Hfc-OHFKflJu3ZddpVUmcm9FKQA6KK38lVEHD2yWASO5Iv-L2jCLoFJFSiR7ioygGLmpJ-Uq_YUrIF2POARYbmYqc3_dPlNqJh6WgS-uZ20UHLX7NMvVF0Xq-ChTNhZ5OQ7Ui31dKjEW429QHm-_hYdpEnYd-FtpRYO7djMoG-E9Jh6xm5wncmmNbJa-kh1W4jm8qOxcmOqA9sW9Sx5Ym4v46ottg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر ایزدی: رزمندگان سپاه و ارتش برای دفاع از تنگه هرمز آمادگی کامل دارند
🔹
جانشین فرمانده‌کل سپاه: تنگه هرمز متعلق به ملت ایران است و فرزندان این آب‌وخاک در نیروی زمینی، نیروی دریایی و نیروی هوافضای سپاه، در کنار برادران خود در ارتش جمهوری اسلامی ایران، همچون ید واحد وظیفه حراست و دفاع از این منطقه را بر عهده دارند.
🔹
تلفیق توانمندی‌های رزمندگان در جزایر و آب‌های خلیج فارس و تنگه هرمز، شرایط اطمینان‌بخشی را ایجاد کرده است و امیدواریم این آمادگی‌ها روزبه‌روز تقویت شود و صیانت مقتدرانه از منافع و حقوق ملت ایران در این منطقه تداوم داشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/467131" target="_blank">📅 20:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467130">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frombankmellat | بانک ملت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRwHTUmJT8hPRwSKHF-FyHW8Mq73BGQXc_ALsBn30HXPUtGxaVIbMhaBC3pDhr6gsXbH9b4CXMO7hFSTt7Mca7U1DwKKYLr-ZPMglDTS6D-Cf5HP_4s-1FYY4NtDiuwwHlSiDVKyT32-U9EgIZa9Spk7SmD4HXMnzo_abLBVcSgyhyTiWg9zb0WYQQXHyv7X1flztXskV8gf_DhMjVFiZA_2QN_wf5Q9D9AV04FqBfugbrMWVKcQjRuXqmHpfFHH7VfeEUwlaT9AuLEmcarMv4osV0GMo9Q8oeUerw94z9V4kiAA1Yw-VWX9E2iSR7aA4IQ8dE0ee4GLZSSujWmQlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌روز رسانی سامانه های بانك ملت و قطعی موقت خدمات غیرحضوری از ساعت ۲۳ پنج شنبه ۱۶ مهرماه
🔹
در راستای اجرای به‌روز رسانی های فنی با هدف افزایش کیفیت سرویس های بانکی، خدمات غیرحضوری بانک ملت، از ساعت ۲۳:۰۰ روز پنج شنبه ۱۴۰۵/۰۷/۱۶ تا حداکثر ۸ بامداد روز جمعه ۱۴۰۵/۰۷/۱۷ موقتاً غیرفعال خواهد بود.
🔹
در بازه زمانی اعلام شده تا اجرای عملیات به‌روز رسانی، خدمات کارت، همراه بانک، بانکداری اینترنتی، بانکداری باز، دیما و دیگر خدمات غیرحضوری غیرفعال است.
🔹
بانک ملت از صبر و شکیبائی مشتریان گرامی در زمان اعلام شده تا برقراری کامل خدمات قدردانی می نماید.
@mellatbankiran</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/467130" target="_blank">📅 20:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467129">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSSHarSjGG8iJRz8fuF0miCJFZgSIRnkLczsRORNnPg8wexlh0WIoCFawV7pHVLJreqj_uDu-zZZkFJSGEOtMQonjbPBippxgEGxEbaFo_GjdFfS1MnNKeQc6rnlbh5KdbueVKWe4TSeizH85WMbdmA1arBe5GU_DFEjS08m9h8wUzU3zqPWMjJjZ04DnnvlhPdZy6n7QTC8QTdYxpmyBet53lZv864w-JIqOTSihZxyc0KSnhGgOT2t0HQEH-d2w7XcuOwrGes5sueDOQQV3Ns3E71CJHrNIUAbSN2DVutcQ8rg-cseRSp4NQvViQtW7i5BY0xba0AXMbHrbeEFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
برندگان کمپین خرید کارت هدیه بانک شهر معرفی شدند
⬅️
کمپین خرید کارت هدیه بانک شهر با استقبال گسترده مخاطبان به پایان رسید و برندگان این کمپین معرفی شدند.
⬅️
به گزارش روابط عمومی بانک شهر، در این کمپین، امکان خرید کارت هدیه از طریق شعب و پیشخوان‌های شهرنت بانک و همچنین خرید کارت هدیه دیجیتال از طریق برنامک آپ برای شهروندان و مشتریان شبکه بانکی فراهم شده بود.
⬅️
در پایان این کمپین، ۱۰۰۰ جایزه نقدی ۳۰ میلیون ریالی به خریداران کارت هدیه از تمامی بسترهای حضوری و غیرحضوری بانک، ۴۰۰ جایزه نقدی ۱۰۰ میلیون ریالی و همچنین ۵ دستگاه تلفن همراه پرچمدار به خریداران کارت هدیه دیجیتال از طریق برنامک «آپ» اختصاص یافت.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/467129" target="_blank">📅 20:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467128">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/467128" target="_blank">📅 20:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467127">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا نام ۶ فرد، ۲۷ شرکت و ۲۲ کشتی را در فهرست تحریم‌های ضدایرانی قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/467127" target="_blank">📅 20:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467125">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAJ4ar12sTU-UCV7AsEydDlQNoGctZXH2mXz--2Ln32r0P_qd9kFK-XTNsVxtfoXB6a-l5WTf5VhUGE76s-urAF4GTxIE_uKuCjmxcgg-xbSrPV0hAgz4fFkbt6yP9awXrxkC4kqcHAd12xQDCy2I_rIyFJorvKa_WiqSERm090EAI38TmOKa82VbHcVKwV7VPes0BfdU3s1IDIXDvGLE-7Wo3dnIqm-FY-rnByLHsp_WTHfyXMX1lgil2XqNssnt2H-VZFwwVUTEuGSyAqJA9POmVmpRhdW_rrw7QUmChr_aAFsuxwccHhyujK9WDz6EWIFVzaNn464GsTaT2wFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TcTVH-oBWwmu82fWSrQDSIDUEzlAmPorWBAiojc6iHA3KROx8xmmlbnWLqkLn3lI5FxMbnprfSm25r5C-ktdFyJ3S6HABaiqUDRbi-dlhhJ7rcfGUQo3VcG2lcJw8YtB1ntPEL2KFr8_L8fKUGj1JrN19Gn6idc2RQ6oSmjqU9-8_bfAqKR0TH1St5W-ynyFhGeW5eskaUw5U11TXJbFgFbbknQhqcc3ocy-8jE1yQNR9KIUrMKtocJ7c92fH8PHZd8aRNR3g_XAonfNV_TfocWk2JKDkeEZ3BzKm2Comfc8rMyDY2esFXbqg_KrAE-eORd7a8a2nF7pbS-dt8Zcmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شادی پس‌از گل ستارۀ سپاهان با یاد امام رضا(ع)
⚽️
مهدی لیموچی وینگر سپاهان پس‌از گلزنی در دیدار امروز مقابل فجر سپاسی، ذکر «یا امام رضا(ع)» را روی پیراهن خود به نمایش گذاشت.
⚽️
این دیدار با برتری ۶ بر ۱ سپاهان به پایان رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/467125" target="_blank">📅 20:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467124">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mONzxtaWt1eCVVIyl6hUJwTxnnT2gFeFOUK3VGRpljeighOhRTM7ymzTvwFPitBINKCUDFC89DxfpyddGEl0rxhcImJYFWiqRwQBwu1AcQ0Soiz6sku-Xb0cmg9eAUHxXtBB0BXNmlWrkQpwCfvpmnn7cvrpX48OvuVrJul-lEozlqeIDZ95L8CpwUS_hsisZWx3VGtccQTMgtG03TGO_a6B6TKS1pI9osX_4Q8VQ3TLFkDvOWQipk_vJat2JLPo2NATDddhLE7k3NpBI0mcWpep5HNGqJm6mpsfdE-mTGX-zwyAW6oHrdO7zO_W9FEMJbu8k0TPROtEcfFgNMrAbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست جدید وزارت نفت: تلاش می‌کنیم به مطلوب‌ترین شیوه نفت صادر کنیم
🔹
حمید بورد در گفت‌وگو با فارس: صنعت نفت در حال حاضر در یک جنگ تمام عیار اقتصادی است و تلاش می‌کنیم، مسیرهای پیروزی در این جنگ را مشابه گذشته ادامه دهیم.
🔹
تمام ساختار نفت پای کار است تا…</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/467124" target="_blank">📅 20:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467123">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSnUFsfu0QEWrqRQf3Aboi6f4ibBwbM0QDyTmlfsbxWxJWZ6OTY8MAfek8jWlr_Fa2SE3LVgi1a9Aq3TBbpS-5SmoatHFqw4TlXT12RfRcxsdNwrSOi55ySVLxgsrFgP9ZJKReB2AbmuzQ5yvgDcFAluo6TMI8JjT5iRk050HjjkzodPN8aujHMjK3mc5WaSg9wiID54floWCujs--d2zaEWx8uvwVfiFLG6QqPz2dzEdGaSiA2UjJWr1kipU1s1tyBs1pAS27VtKIEUCfzWCY1EQJNZMCFtNgf_1BCU_nqMr0UZya_bpbvic6ONe03HKiTEph-UWLy34rg46raI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نبرد استقلال و تراکتور به نفع پرسپولیس تمام شد!
⚽️
تراکتور ۱ - ۱ استقلال @Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/467123" target="_blank">📅 20:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467121">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
پیام فرمانده معظّم کل قوا به‌ مناسبت هفته نیروی انتظامی تا دقایقی دیگر منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467121" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467119">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXE9EXgZH0aWL6AvbYf2O3QnL5RDqremx8W2A5nrZN9eZ1KuSEjwvOfh2bsLRiUf0k7QtXwKHSBDu2w7pLB7jqk31q1t5qD3eShmApOr76-IPZN87HKbUXVOAh2KGTVc06hu9WH7w1WYwTZiZlSWAvNnApDlV2YgHm6SMht_9oDqFAodWsp9y4jjLrJm2oIgibqg7dnCY7QTILipTq0153IB7n82DU2W_5uq0iPiWVK2XcKXryEjK6MJzyC24Cma_YyDaZBrlJ2m3BOlCCEsT6dzNKkiAgnuCV9DAesN0T8ry5vr9PrSxarohVNfsZixF9ychzD6askmezrjJ8xICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: همه باید به‌جای «هوش مصنوعی» بگویند «هوش برتر»
🔹
از این به بعد، در همه اسناد آمریکا و امیدوارم در اسناد سراسر جهان، به‌جای واژه «هوش مصنوعی» (AI) از واژه بسیار دقیق‌تر «هوش برتر» (SI) استفاده خواهد شد. ببینیم این اصطلاح جا می‌افتد یا نه؛ خیلی بهتر…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/467119" target="_blank">📅 20:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467118">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سلطان شکنجۀ ایران
🔹
داستان پرویز ثابتی از آنجا شروع شد که دنبال کار می‌گشت و افکار ناجوری هم داشت. سال ۱۳۳۵ که ساواک تأسیس شد و او از عده‌ای از اطرافیانش درباره یک سری کارهای مخفی شنید و ۲ سال بعد فهمید که دلش می‌خواهد ساواکی شود تا بتواند کارهای متفاوت انجام…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/467118" target="_blank">📅 19:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467117">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">قطعی برق برخی مناطق تهران درپی وزش باد شدید
🔹
درپی وزش باد شدید و وقوع طوفان در شهر تهران، برق برخی مناطق پایتخت قطع شد.
🔹
عملیات رفع خاموشی در مناطق آسیب‌دیده درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/467117" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467116">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6L5AvSiEp9Lg8rOtnWvVEP7YPyQ-MsNXVf7QBDQrtPg4MAltZfCcOwfCuvh1vsfuL6LRVezSxBTBMjUyRGVFX7KjHaRp1CgGeRhl-ptIMi0Xc_0qtztXXbSSrkKN7NwF5yFjCZZ4IDnNIB82XEoPDq135jY5AjGqXcStKPhfsq5iUNOkRlE7cXxnNeWOvSPd-ZzU7hZSrZ3-gHbWSOrS5qkHTAPXvvn0vquBnRRa4fBNSpVU3W_N6GKdqd3EuH4mbfdgL13yfmRdW3mq-ZzU8zb8vfY2c3hhiQ-Lh6GPAw6Kw7oyTJsrYzHIphiUD8t_t_VFhYNic8ADcJqWpJdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع: به فرودگاه‌های عربستان حمله کردیم
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد شامگاه امروز پنجشنبه فرودگاه ملک خالد در ریاض با دو موشک کروز و فرودگاه نجران و پایگاه هوایی خمیس مشیط هم با موشک‌های بالستیک مورد اصابت دقیق و مستقیم قرار گرفت.
🔸
سرتیپ سریع تصریح کرد که در نتیجه این حملات موشکی، پروازها در دو فرودگاه مذکور متوقف شد و خسارت‌هایی به پایگاه خمیس مشیط وارد آمد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467116" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467113">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmrlQt5xHQ-G3qN7bwAlhd36Y1YGTIv6b93YO3fFSrnE27F-x7KFJOmMkL941XUptVyQQLkfrIQMz8T9xQPVlJhQyWrZZfDEuk81DFf2YaP44Q2TmAF6zGu-ShiC1rv8E7PImrZ5ZOI0nhFoSlLiCBSkL-u3iWxNLcEoTRA_0ryN-pz3CaZllViOO3JNAWdwKKHIsUwC_e_UPFCD23lljaKCPMiZ1uJUi_bC7NyqhCxtiKVtNdY5Y2f5r13IOuRDSbQ7r0K0D0I4rT3-QyqyyVLaMS2mJaGAZG9VeKTwzUQNQN_zbq11AouLvf0LeKAW7RKBJKJWkHpdzeu5AUoPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXoXm6nTnfNvlIwbkD-g6Zkyyn8s4mHl8ZKpFW48Xgt8gNFXZSSUHYusmDUOUaQ9XBud5jayZT8ZFAQSdiIH5cf7nWnwkln2TZvDsjRZZPN2YbwjiRHM4Dw8z78M6MTY7Ckune4osvYdXwMx5eH1fVDmm_hrxxjjcIrNjySIasdiP3poC3JLCXGl6v_322YEUEk1t9fpcTytAylwYl2GMWqj5k4OjXwAuEdRcK7wTNrA5Nsg0Uo8Fr477B3efN7f89o9eH7WqA5hAXFm-viIx9dIbaihtfGxuxVUpqC0JjcjeqMbETtyPvqruXJbqqnCnQ5aDrPBhc0Fr2qck4ojTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IW8km67MTBwM9yHz9ObXQUz3tY9N7VlSgeZmRhrIab4g8a8LVcMzchRa8dI_6Z0L2rJ8MedBW-_8JEMV3dLByrjAITHbMk5uGAHem5X-rw5OKtRQplP-rpwQr9EpEFUA1rHRxuGQIy0_jary8n47fZh-OiNynUJikrZmTWxSJkU-bProAjk68noEkkEhdiWOeKSuXKjDVRQ1nSxIz-Hfy_pIC-hLGNkQ3S4K2QC_H45qeS9vcJlZz4h4DLV-yqxYQOT2QcGjemKDT-Hin6QIB8q-J9XVcQnVVY22jhetcwc4FTxMRHZ8Pdj38ZIqlclXvqkNkunryaW55f5WVPFsXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: در سفر به ترکمنستان با سران کشورها دربارهٔ مسئلهٔ خزر که با خطر مواجه است، گفت‌وگو خواهیم کرد.
🔹
‌رئیس‌جمهور پیش‌از سفر به ترکمنستان: خزر سرمایه‌ای برای نسل‌های آینده و محیط زیست ماست که اگر از بین برود، مشکلات بسیار زیادی برای همه کشورهایی که در…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/467113" target="_blank">📅 19:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467112">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فرمانده‌کل سپاه:  تنگه هرمز، خط قرمز راهبردی ایران است
🔹
هیچ قدرت فرامنطقه‌ای حق تهدید، حضور سلطه‌گرانه و دخالت در تنگه هرمز و خلیج فارس را ندارد. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467112" target="_blank">📅 19:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467111">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJy3SnkqIjF_DVILuB6qbHchlnwhJpUwxqq0H4frh5FG8ZIkHX5hUkEP3BhfA7z1ODzme2WroXE1Kvb-mqgbHuCaSal-BNOY_NebvSmD7-YrXrwgq0F10tZNEy3hF9C5Oiyap9w4k-wZyhZtyRfBv1BXDssqQ5VT3dYAn_RiOiHZLzwXMWohdIKLmvPX-3pqeeocJIwOCc-un4fnFSA87GjBOurVRWnG8agee8O5AdNAnYj6nUIGrAyIt2SzO83dNjH9Tr_eyFvldNjHzo-vEoFiEEi7nG9s-JBMqBYuc7Rf74ZCu-vFfVdkpFppU3dlgWVE7TU1bOh3yaW4XOJgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرمانده‌کل سپاه:  تنگه هرمز، خط قرمز راهبردی ایران است
🔹
هیچ قدرت فرامنطقه‌ای حق تهدید، حضور سلطه‌گرانه و دخالت در تنگه هرمز و خلیج فارس را ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467111" target="_blank">📅 19:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467108">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7262159e9.mp4?token=tzdKgOd4ammatsgrQ1y8GDQw16g_4LmVXi7X4MRorF07GzxjxbVT-ZRwVTesGgisBYUiypKp3tpwccUxXI2KL4lvIbGiy-zKIRCSHlqhFg5fYgzjmCC2aN6OpqVmnQkyywABkZmFTuCn1ttVQjH-63OTN9qC5bcEdStNFF4yqYI9EWOFcE3YwX8H2TyRj_ZB8uOAv0S5_KFMixBxmmwnpeYYzkSfaR4GO6CVxGXhsyB6H3i3QTwz7nQVcNRdATUgxMSzTzJm9T_IUnS89m9iGYN7p_HkchkQayZHvlll3qW6GuN3Fd9-igxzBGyl9krPbicy7Nj5RhDoYqq4VWFNTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7262159e9.mp4?token=tzdKgOd4ammatsgrQ1y8GDQw16g_4LmVXi7X4MRorF07GzxjxbVT-ZRwVTesGgisBYUiypKp3tpwccUxXI2KL4lvIbGiy-zKIRCSHlqhFg5fYgzjmCC2aN6OpqVmnQkyywABkZmFTuCn1ttVQjH-63OTN9qC5bcEdStNFF4yqYI9EWOFcE3YwX8H2TyRj_ZB8uOAv0S5_KFMixBxmmwnpeYYzkSfaR4GO6CVxGXhsyB6H3i3QTwz7nQVcNRdATUgxMSzTzJm9T_IUnS89m9iGYN7p_HkchkQayZHvlll3qW6GuN3Fd9-igxzBGyl9krPbicy7Nj5RhDoYqq4VWFNTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درگیری شدید بین شهرک‌نشینان صهیونیست و نیروهای امنیتی اسرائیل در قدس اشغالی
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/467108" target="_blank">📅 19:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467107">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805fc7f33c.mp4?token=Mk8wdZ8_A8HN42DgQevWCHycVVSt4IiGm2tlM_rHez6mO7-oh3d7KYdfNQboubZjshs7danIZMvmEJRoN4y3o-yYf_Ad91h6uxImDavyv0uZkna_tSEF4s5UKsrOoZiCXa9FI71JvvInk7no6_Dnj1MqJ0ou5kltWF7djjXLc3dgbVCc6vxOdXblh1TFNu7jx9ZE1CgQBME3ywBRv5XMjPK3JPjWDbFm5KgbCt8hwnHsnVyLe6CGgVtB7pEXKUaKLwm_57Al-5xFqHqFGZxIopjwoKAk-m-ifSZn2MOORkd8lF0UfIgYqlyQQNsJAhTamtUUTPMiRcKBBy3Ke-fLzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805fc7f33c.mp4?token=Mk8wdZ8_A8HN42DgQevWCHycVVSt4IiGm2tlM_rHez6mO7-oh3d7KYdfNQboubZjshs7danIZMvmEJRoN4y3o-yYf_Ad91h6uxImDavyv0uZkna_tSEF4s5UKsrOoZiCXa9FI71JvvInk7no6_Dnj1MqJ0ou5kltWF7djjXLc3dgbVCc6vxOdXblh1TFNu7jx9ZE1CgQBME3ywBRv5XMjPK3JPjWDbFm5KgbCt8hwnHsnVyLe6CGgVtB7pEXKUaKLwm_57Al-5xFqHqFGZxIopjwoKAk-m-ifSZn2MOORkd8lF0UfIgYqlyQQNsJAhTamtUUTPMiRcKBBy3Ke-fLzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ستون  دود در فرودگاه ملک‌خالد عربستان پس‌از حملات یمنی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/467107" target="_blank">📅 19:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467106">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrzpXv17wcJHvsoMymkv9IRCnTe7IO5oq9IqD5RrG__jCroBk0uTdocZdiFp0E1Nm6MgUleRvSRXKobqeoeeeYZsRvqQetfv5Bek0igxbrqTm2heNCBYmA98KZk2UsRYCJgocvpyn3k7e6Fb97425xxQCB-V8j0xDSA2KZPXe0PmwaWEAkill721iG9-SpzjXwWfXFzQz2miFs36Q-nDWzYEp9jNgB_SoUgZ7r8hDfwufT_l6-fH1LHgCufScAhzFLAUO2Kun4EBrbEFMd5EG_GON2JQJ2BiV_8uqnr4RvO0PZET07h8J7v9Gz44p03ugUeFz17aa0UieGy5yJo7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل مساوی تراکتوربه استقلال توسط حسینی
⚽️
تراکتور ۱ - ۱ استقلال @Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/467106" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467105">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616c846f9.mp4?token=MuEIc_CgIrHaQTEjObAcHz8Fau35oB611SW-eWSKnUpJjHv0kFXS9VkbgkkwzTzW_H1-QU_0-aSQY1DZ-NRKyZtWU_teKbNAWRWcti0lnL7OUf86_rA_WgN_hiLXJ2AxlK1fVxvzlNu0k4Q0xukrNcgwnACgKlkl9QZD5NabyWsFKKcPUcrcXvRazn_XxKWBSEex6QSkMyYZJ_27_LE3RKcU9tQoc5Iq8xjAeS0U42bkzqnUu8mOelw8TvtxmoKoiLQfVysymVODoyizyCCAUt2hYzJvv0mhxbARO840ofUvc4k1q1B2wW6ibcjmhn7LaUNlkaANimzskEuqAt31LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616c846f9.mp4?token=MuEIc_CgIrHaQTEjObAcHz8Fau35oB611SW-eWSKnUpJjHv0kFXS9VkbgkkwzTzW_H1-QU_0-aSQY1DZ-NRKyZtWU_teKbNAWRWcti0lnL7OUf86_rA_WgN_hiLXJ2AxlK1fVxvzlNu0k4Q0xukrNcgwnACgKlkl9QZD5NabyWsFKKcPUcrcXvRazn_XxKWBSEex6QSkMyYZJ_27_LE3RKcU9tQoc5Iq8xjAeS0U42bkzqnUu8mOelw8TvtxmoKoiLQfVysymVODoyizyCCAUt2hYzJvv0mhxbARO840ofUvc4k1q1B2wW6ibcjmhn7LaUNlkaANimzskEuqAt31LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل تراکتور به استقلال که توسط داور مردود اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/467105" target="_blank">📅 18:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467104">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d32a4cdc.mp4?token=fzA2Z6IbXNZL-Y8w4GC7a720J3quApNiyd67FVWpiyHyYd0SKTaWqzlqcbxOzh-lauGhZFUwY4QtPaEPzxzKkjD3o-YyFyXHjJYxCfOvPEXoa8akGiRKF9WZ1crwqUv66GW0Tnhr-Uu0YoRjwReh5McryQ-DHzJYy-HbJxnfvTiYBqMcLqWKEQfQwwpaHh4tstyLugFY-a9xrHn-7q94LNnfSbYoWMdvIrsTiu8on3GOLe52pd4NlaGDjb7rCaZj3sWhd4dFA8WnkcGD7XYoI_9NatdgiUIwqXpKOh5ShLCcGbFhyOCL41ycVs49cbI-GsD9uBMJMXNleCVDlgDPEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d32a4cdc.mp4?token=fzA2Z6IbXNZL-Y8w4GC7a720J3quApNiyd67FVWpiyHyYd0SKTaWqzlqcbxOzh-lauGhZFUwY4QtPaEPzxzKkjD3o-YyFyXHjJYxCfOvPEXoa8akGiRKF9WZ1crwqUv66GW0Tnhr-Uu0YoRjwReh5McryQ-DHzJYy-HbJxnfvTiYBqMcLqWKEQfQwwpaHh4tstyLugFY-a9xrHn-7q94LNnfSbYoWMdvIrsTiu8on3GOLe52pd4NlaGDjb7rCaZj3sWhd4dFA8WnkcGD7XYoI_9NatdgiUIwqXpKOh5ShLCcGbFhyOCL41ycVs49cbI-GsD9uBMJMXNleCVDlgDPEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به تراکتور توسط سحرخیزان در دقیقۀ ۲۸
⚽️
تراکتور ۰ - ۱ استقلال @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/467104" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467096">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzFco-7KP4VNkXQ0vlT7yIiZC0Lj8wfbtzAVldq2rE6Xl-aM-8P46FCNyWu4XoP6htvxtsupiuYL5UEG4UlCkyt2-Zt6uW2fzCxFtN7Lq3dVK8KXuKoQGIASlt5Hr8i0iwgifQXEGD_EemB5dFn__P4epQ3wfwz-hX2pFN0wvnhPFOy5819LYsPC1cN1v8jkYC1vK6vhqB55uVx60xQI_JAMb08oQj5sBp98-pT_ZABz_eTX5ugwOAAAcGK1MKRxHYIrbG_S41w-8cfNA0TwZ0lbbFfg7sK2RVfqCQ3dxjz3oIcZrFJQb32BUzjUoqHcneqOGYhiv2K6iLW_ughdaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PrGd-ZlOaU0cc9UnbL7UtosGpeP1-6dicaKjxXW2mP1IXw2AhbwDItpXZCZR5WBfOqoCQ5PvFtBY7qWMMuP4tWKlVjXTcHbtSEgoa8K-hBQs4N9BslovkpsQfNhizBG3FDSVT7NQcs7fP5hc9CUYX-SOb-c23wA3ceHAMh5uE7ntP_S3MPIqJsh8yDzChQOFii2mlMzvTVi1F9Vi07XmQU4gy5e7mzlyRailZNlyrvypa5vYrTS8AfWN2GZlj0PC_EnQdkuHtq_B3R5PKJo5fllPK4dokQqYEPJdrIcez2BZeheLQOJZibb4iEPG0L96HOm-v9fvrNY87wrAUSIWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LyxZzsWRWoARs0JOTmj-unUueiUNZ-twyUV2BRG9IHvFeHqE7r0nVc-r-Mk3aq6Hrzbj6NIN8J84WffOscdLpfGeba_ekF4ESU9-kBb6zK8VwQdPdU_70ZPzDd6PCtwT15M0Occ2D9sWeYilsleQio14qnvKKc1uf1jO2GJAc_F8n1RaI9KbGpSQ7FMwtfcu6rpp5Wm8gZQ7X7QCublmNh8wz6AAZ1QxWw0o_s1c0pThTDmivz1N1BDsDwdWs95DEIwpWuDVnAXttABLaC7GmKdMAGwa4Lw3_p9H0zSjU0Nq9jriUsZXGnKzytcoeh_hOJMWE-jp3b-rdhYDFuqrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWWpjMpwn6QCf3BmDkJpu_jM5qMIOz2LccyG9ThNVaTtsESJ6X8hYIl41MI9r26TWwHQrZ6XDfRw-YNEfKqUjRkGDx1F89br4JrGR1u3zQ3NvEgDEYqvvM3_mlneBSyLxVUrztARnrr_w8gNNsvy-qRq1SIfKtnVO5U-c9yVqismLk3V-SR_EgThL600W5LhQff8hy7TX2Izs6X0F1MKV4k03GY0q4BERAOeAHpGGsNEN1clqTM3BAuD_4JXCUuJrOaIjqj3E25zVh7UH4WLLbkURcZufXK5T0TUUz92_ggOiLMWdAeH-XRl3J4ilX0Zq93Yz0hWGxUu578Ku8ULOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6cvihBQIsVug1F7iCPo4cFxDfBn4NPQwVTwvkwCpdFU_tSAUvpSjq8cp4kyQjtC6UaHJjAMtPgjoZfcWqB25CfD4x_sBQN-Y_6SPwCPRUsLAoYT5vkyHUQZEkTf27jRSvKoCLgJRxlkYiKpb-TK2wQtWxfF0yjVGNfnIvJQ6Np6ztGVCjkx_4QKKG4_3z1EXihMARQhpiLtWb2SSRnlswmKK3GzEg98EPnXUwxBm2rMg9yuxheRBzDg_ITavW2Cl2iM2qVFfVq1FVY3XKUnuhJZJLblp3jhmCsA87DzpRrzK_5FcSjqINao6cUMAkP29uRdECcdu1iCjbU0pGqA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vtJY_KzA3kt2UNx7g9y4Fpf_nzYpSiggVGUeRHWdAGTtIkbetvF4rr6Hp80TFYCvXjQyXZcvj4ED7sTyafUFxtOvLWW97WyF1dRUnOl6OKZ8rFWe_FEszwNO4aQGyiW-O7U9k4SIHr_EABgl-Ldyv0yOKXdyRsjpnbdp52hm-0C95k1dJKUioV2pgqRqPBPauqjGw60oKFqjd91lHAI_qWmlFjkwfo9XU594xleSBOp8sS_ZtILZn7LAAUTfTbFRSyYn3vMAjAb34w0w9Y6AAXi2g3kLcDyFBg8q-U-wFPq6bttn0Rt4GvnQtsRgE_YAduvc1HNuRTKrwjNKTJ4dFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rk0EXEXoy_WdM1IArJ-1f4cX_TTDC1N0gitkEa04dNM4jVtDjOABvdKKYDL5kllg2dgUEYSyYK_s_lDlp3Xgz98ywSUGDu8noUrwkMDBdi6mu1_mzIHFr4ECU0pKrGxOC_Tai8qm3BIXxavzTtTr_G3dPYiwpwL_44xhT9GHxn7TnL3nr50YWaWL3_5f1cDZ3uTkhEkpWRRf-3A0_ftvFUuFT0ROfDo_VWRSDFjQ2Hk1UbDPAlfdu59nA4smE01jr7EUkhHgap5n84vwVjKpgAuvHCcL7VU7c-jazCznc-xUj0i0h9vx4phkIn9uiBZ6FFFbhDmH3s45afv4bnafvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBDNpqxQyH3R4o22fuk7WzjCqi-VLxbXwgPtOug7zaSwLNmY-iXQepIpfJoxOgfkireW_oq1H2SpLO013wSf7wmRHQCZXiFU4q6u4rI_F_RxiUx-kzgTg7HeGfYBDGh9_toOno34BL-gPPAUw2fLF_yCGJSTXSagxsMZLvyzHNXTPF6G7tSJZACW88fNu-xzrtJeR8lfa7ej-CDg-ohxRoUPl0HfyMPsjz-SzKZ4rh-oA62bQYWgiT1kuiu7ifSnHQvIAZzktN89Xm4imvg7n9azl1gKqge4Brk7_pvE6LJ0wI38sIysO__h-XQ7R-ESmsbcGejCONfmjfrZml5B6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رزمایش جان‌فدایان وطن در گلستان
عکس:
علی دهقان
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/467096" target="_blank">📅 18:10 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
