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
<img src="https://cdn4.telesco.pe/file/A7T-A-rN4FjCOsiK2q5g2jjVdYUh8gKrbIg7EkhcwRuVn449tgbDPToGiYYXRCc8FQNOeztntzN4ye9nJkMU_Tc_gLcUtWf6HSFCkOQ67t9OZRBthTRNspFKmMh9SKteK5yyqYazfSNDZeMiZ8vFAzD-KI0vZe4nC-vtUL0zloDrT-5eEK5j9xaBq1RJ5__85zr685LxXAIEts9htrYiguPynkqot-Uk3380SU-1LHYQMKwjYOCMCR8zNjU_SIHH68a__9DGTPUxEHUNGKEgO6UJwuQn0kv3okfkFu6PSvPqCJ6kz13l5pFpYi-zXN4bcMzowcj9KQY10yl4i9jCKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 420K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
<hr>

<div class="tg-post" id="msg-30914">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_dEsuExqTADbOsfir7HQLGoEeXCiw0Tl6p_PWZj8Kqwi7Ibfnb7O4y6S2ulF0NZNxjNgkfgR6B9lxGYhydczs7oObETLHdOfw1Su-_2Z8DJtjBpjMi6UPjQOinhrFLFfs6HqcflTArOpZFznEx4lV4NMJcW_to0AETlclsN1YC9xzinthvTOTvi_Mg5-k6iZxo6BpCIVNgP5MY5QY7_9JY_91xa26jHZWlYDKDz_g2LnZ8Uf-V4qsa5zak5wfsLqnkoNkOGD0kyvsllBVmz7pSkeX6ae6Y-qEbtZow83nLgRZrwAXYI_6B0nBP7KNkjbcTG3xxg47GyxJNDrGTQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دنیس اکرت مهاجم 28 ساله تیم ملی ایران از طریق مدیر برنامه‌ ایرانی خود علاقه‌اش رو برای عقدقرارداد با استقلال در نیم فصل اعلام کرده و درصورت تاییدیه سهراب بختیاری‌زاده احتمال آبی پوش شدن این مهاجم ایرانی الاصل بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/persiana_Soccer/30914" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30913">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETI8vOQ-R7fA-_lqCPr0plthxD6mh8nblXfdGue19gQ6iwTrV2vvja75hIqoQGZLT80ijFP4CUyRzlFTlTmdFKr48TMaVZqfzPy3OcMZE66sm_3NWllMp4ZWbH2FRr_9nPTC6j55smCZFNhpy7lG957U7kNHy_e54iSk8w1OW9BkqhJwCccg2ZHINa1G6pAfs6wgue-3WaflkaZO2PinK8FXj2OH-DdukFS3G4ezhlN6k93YUd__xL7OJTa71oNeqdMxECP-vh7DtlNw3upQROA3yn3CT5yKV-FzRPTafZ5nqs0kyq67Vyh271_ud9j_viaWRFetEobsVDZhbLfLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه فلش بزنیم به این صحبت‌های تلخ ابوطالب حسینی درخصوص قیمت دلار در آذر 1404 یعنی کمتر از یکسال پیش + دیس به امیر مهدی ژوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/persiana_Soccer/30913" target="_blank">📅 17:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30912">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyK4QxKNzE8ifPKcPdBZ_A76_CN1X0r--amyfRlJBWFvYliW8m951GhMjbTZy7dUk_LzKntMygjLYDtyeZ2dS796WjNHBJ7QJUycxLnmLLTLwVAqqWIL0CcauS7j7PPQ41wwsQ0ToCW57fikJSrjjpgvUC-mcG4jWrkcyO97tE7ySMnl0Z1BamM0fW2OdmhNboSYXWVGOWZTz_4y2MlCuhmhosurCKEKwDBpUJPPHwUstdsBatOWEuOQjDuUie1TtN2qj383UADF-r-WrwyfMNDc2CBg_7vIbmlVMApzu4KjWLmEpRuN-AuwfD61nXiyeP-uWE4qotCyqRyo3Nu55A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هر ۳ جام‌جهانی‌که مسی فینالیست شده تو گل، پاس‌گل، دریبل، خلق‌موقعیت و پاس کلیدی نفر اول تیمش بوده.‌ توتاریخ فوتبال حتی یک بارش رو هم کسی نتونسته انجام بده چه برسه به سه بار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/30912" target="_blank">📅 17:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30911">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfXsLfL7swFE1mVgn08Gf4pNkTzhjOgvPIIgDlDtE-KJTa1RyIqT6yTussmEcF7z7ni_juMqd9xYqlekYhiC0DOc-VSKR5lM5UiXRy5iKTA5k3tSsIIoRiC6lkpmo8KGF15z3ifA-7xN9FoAHTQpOFzR_GBshALON7sbQdtdid1P6q1HtZbf7pHyYIiVmYfUjTvhz5OsZVtKQlapl3ieArdUy9FvxzMYgzG4TFBWQb4MCEGx-gDuxoIMt72crayDsEV9XZGJVRV9J8DQTd20W5pTcmfG3JuaCq1cGfz753pkJZZtZfAk0Q-KE7was56veIJptXLizoEyK7Pxv7wYSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
انتقام قهرمانی آسیایی از ژاپن گرفته شد! تیم ملی والیبال ایران امروز بابرتری سه بر یک مقابل تیم ملی ژاپن قهرمان بازی‌های آسیا شد و نوزدهمین مدال طلای کاروان ایران روبدست آوردند. البته گفتی است ژاپن با تیم دوم خود به این مسابقات اومده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/30911" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30910">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=jVQxuro4WasO7H1qynQupDlULkMOCTC-X4x14P13Vf_8BiwC54iy6lTt6F1N8oF3pAgA6LwZhAEdoQIXrNQ62B4iGyowgCjgMueqPjLcs9g9ERs-PzJSIGU1BXgfyuPAW8_cV15Vk3O-S6lptfVbUpHu1Jb-2uItlx7yz6CB049IzHNybf8xoB-YOp1Ulfwz9E_HT5V_0rDVJ5JfNavbOPAbULN2KQx2EAO7alduQZvDa7TyFFkt4xT0yj-ReBWelKvb4pPbHfAycVjYd1UkHYphkEutNRRgP4VvuLjgJW-CVa2Cl36DlDBS8jhiWcJ28ymifTj8CTDcXxNkKmvpPBMNa8zEQrA8ynR0Q5JDq8EegZ-3AV1Ug3gQWUt0ki4vIvAhk7Rc_u9G4AA-VjxOaXz-pHGrXj9FXLOG_WFVNk4Ob-jxQbK6JY9AVwNZDyNTfFuzuzJSBMuSJOwKvn_rS1fW5BmOXzRTEysDHsJNf5KVtsO08MjERbBjknBqLlFcwYAYkJqx5NiKVbxQJHAYd3gflHq-tUpegqtwZtNBA6-gd2aW5Fq3itGmXSpXtE6do2NWEvvkHyRrPut_wRTsWNegJbTtT40hSLy1CZoyS4RyO3iAymUYhN8FxveIfpSwFVtI5gaPROfOAKuI7eFMT-6-k1xha4EsSQJ0OET-H4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=jVQxuro4WasO7H1qynQupDlULkMOCTC-X4x14P13Vf_8BiwC54iy6lTt6F1N8oF3pAgA6LwZhAEdoQIXrNQ62B4iGyowgCjgMueqPjLcs9g9ERs-PzJSIGU1BXgfyuPAW8_cV15Vk3O-S6lptfVbUpHu1Jb-2uItlx7yz6CB049IzHNybf8xoB-YOp1Ulfwz9E_HT5V_0rDVJ5JfNavbOPAbULN2KQx2EAO7alduQZvDa7TyFFkt4xT0yj-ReBWelKvb4pPbHfAycVjYd1UkHYphkEutNRRgP4VvuLjgJW-CVa2Cl36DlDBS8jhiWcJ28ymifTj8CTDcXxNkKmvpPBMNa8zEQrA8ynR0Q5JDq8EegZ-3AV1Ug3gQWUt0ki4vIvAhk7Rc_u9G4AA-VjxOaXz-pHGrXj9FXLOG_WFVNk4Ob-jxQbK6JY9AVwNZDyNTfFuzuzJSBMuSJOwKvn_rS1fW5BmOXzRTEysDHsJNf5KVtsO08MjERbBjknBqLlFcwYAYkJqx5NiKVbxQJHAYd3gflHq-tUpegqtwZtNBA6-gd2aW5Fq3itGmXSpXtE6do2NWEvvkHyRrPut_wRTsWNegJbTtT40hSLy1CZoyS4RyO3iAymUYhN8FxveIfpSwFVtI5gaPROfOAKuI7eFMT-6-k1xha4EsSQJ0OET-H4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ امیر قلعه نویی به فدراسیون فوتبال تاکیدکرده که افشین‌قطبی بعنوان سرمربی تیم امید انتخاب بشه. درحالیکه جایگاه خودِقلعه‌نویی محکم نیست و ممکنه هر لحظه کودتا علیه او آغاز شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/30910" target="_blank">📅 16:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30909">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=gMalPQaWLG1TjUmlENadyZXgxqwJZRe2xEo3cOIUxZYOP5W9rg43UIzEMPyY3pKdmBtpX7E_bDzCbGr2SaoYZ9KVg8LFUvyjuP-S0vwmA8v6L_ae_h4q9sx8EusU9OG2Yi7F7JFr5onjzM330hfKWzUcRJWdNmaAqS2embwLoM4hRoDRfX0J0rwIUEbbVQE3jeX4SSet12rSdUzuI52yPD4ARRTKuhLcRVBYrrgtYTWoBaQbUouOp1m_xtOUfraunOvZQCd7Q0-Pv-A_2WUUd0CDZs_8pbUKlDrcofq6WplftbyhchNhR_XDrHi2Ul2w2bQtTuLLZyNmgPXU1deQsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=gMalPQaWLG1TjUmlENadyZXgxqwJZRe2xEo3cOIUxZYOP5W9rg43UIzEMPyY3pKdmBtpX7E_bDzCbGr2SaoYZ9KVg8LFUvyjuP-S0vwmA8v6L_ae_h4q9sx8EusU9OG2Yi7F7JFr5onjzM330hfKWzUcRJWdNmaAqS2embwLoM4hRoDRfX0J0rwIUEbbVQE3jeX4SSet12rSdUzuI52yPD4ARRTKuhLcRVBYrrgtYTWoBaQbUouOp1m_xtOUfraunOvZQCd7Q0-Pv-A_2WUUd0CDZs_8pbUKlDrcofq6WplftbyhchNhR_XDrHi2Ul2w2bQtTuLLZyNmgPXU1deQsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/30909" target="_blank">📅 15:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30908">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5YK9UsCTHIXfV70VqYNgvnXybzf2CRosT7JzESqerVEG2Qbdzwi9Jm4XijLKFR2IBmRCXgNR9CVCZwCo2DZryppctnaPGlICoq2xxO9IKjsIPQ865kHq90HuhcytS34uQ5_mncclfwrgSISB7SzciNA3_Cmh8uzAkfUcuX4MobNqc90Kt-CvxUuLlVZBaL4QmdwXiKlTaT6Xdo4uducoz-fcbF5un8jxQ3eNTt4TKu6FNaKFrvfCropQwASpEL84P7RHWtKfR59tVy3tgc0Y2aWwymhhw8Q5iSl9MTP0ng8e89-VnzthkOBmJfv_M296zzPVSvMg6otAx1LOtKU0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/30908" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30907">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhBdqkxEEktanFJLiQOlnWWHRL_Yh3PFj0h8YorS8_4AvGkW9DaojxG9QWNmutkoEggyCpR35qnno0HGm1LfVEM7u4vONDiq0d_1dEn8tvJ0i-26iPa-Agm8YfHeUJoJoMGe5yfklEIW-GncVmNOvZlmGlKMMKWWx5MVqlMTgCs3d9zreew57aoTvCWUvnVdaw0unpEiMmBp2y2OAHjAfXk2vr3PTfyagNL78ikI3Y1Z1Upa-jKvuYBGaD5FXWvujHIRes_c-xEAzDSbPMhTjtTvWq3Lx9u_lz9QndGXV-A3UjbrAoOAFhaavmCCtXUVi9YPi5T2mIo4FGQT_vVVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/30907" target="_blank">📅 15:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30906">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyLmh0U6-uQBQMRbOBXg8_fQu602c564UaJEJpHtmXCLPIxifMM7RDhDcQ7-boGvvfiDBrrexXyuyVuKmNKgOy-gG3Dz15jy7cgxwxWMx8UaDqKnG-j8ex5ZkuHGIyUFpbsMH3Jeosj1NloESzsdrZkO_K1PXuGmquiHmrHE96YZ-u1q8VUlzfJZ-bXXiE8lFzA4QJ9FatpNjvz_ZdWdGQD95c_ZobAQPhG-VpYiCV6PTz_earQRrXT4zKROhaLm3ViAk98tJIT8abH4V7TSaO0t6aNnIxpYF7w8FQWvbWvzE7LADzu2QvLtYuxX74BiGL4zhMVfMbrH7svSkyQ3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ 10 گلزن برتر تاریخ مسابقات ملی؛ کریس‌رونالدو و لئومسی اول و دوم، علی‌آقا سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/30906" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30905">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=nGDob89lVWZpX_DgQRcxSUxXsFqv6V4i-oESO3mUCR_3eXe6wmAAmPTiJndXBm_rO4pDOdDSNboOWjM5NwYrEEf0NTEs6WIbnVEc_y6j-nY2Bo26Ik8REEhGWVpC_VHE4rfj8XbXmNn6q0B0hJHsLU9yPWjXHqCGeTl8y3DTqa7PM-ApjtoebaOdnBkVlBecp5-VI7FkYQLLbhqBwPbIXw3Bd-cnoAUdHgMXdH3qZ_cZbPBp85m40mVaFEezz8_id5ojSYivV9R1uB0czQMS_ad1i0SvlVs-IEs0UDdhJHNQb6FBklRUl9uasRftuQV6SGj_TL6OQ6yK4KxLXU0IJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=nGDob89lVWZpX_DgQRcxSUxXsFqv6V4i-oESO3mUCR_3eXe6wmAAmPTiJndXBm_rO4pDOdDSNboOWjM5NwYrEEf0NTEs6WIbnVEc_y6j-nY2Bo26Ik8REEhGWVpC_VHE4rfj8XbXmNn6q0B0hJHsLU9yPWjXHqCGeTl8y3DTqa7PM-ApjtoebaOdnBkVlBecp5-VI7FkYQLLbhqBwPbIXw3Bd-cnoAUdHgMXdH3qZ_cZbPBp85m40mVaFEezz8_id5ojSYivV9R1uB0czQMS_ad1i0SvlVs-IEs0UDdhJHNQb6FBklRUl9uasRftuQV6SGj_TL6OQ6yK4KxLXU0IJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح بعد از پیروزی مهم آذر پیرا مقابل یوشیدا از ژاپن‌هادی‌عامل‌حواسش‌نبود میکروفونش بازه و گفت: ببین یوشیدا با همین خستگیش حسن یزدانی رو چیکار بکنه تو جهانی اگه بخوره بهش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/30905" target="_blank">📅 14:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30903">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha7oBP8K5SDvBUZdNYjPoVTxCOWfFW_bCAh8GsJWFd2xKO-YmxxL_sOEv_UBqVW4V7doMCySjhfYQ3t9q1V54KzDhLxp9YQ_uVgpq5Kk2u4CRGvFF7L2s62e0VjqPZ8eJjzQ125SzDugsMf6zdQ5-GeUIpvH9qoUbAhOLuPp1ZPCy7uXgU2EzPLsU0ESZWz688OR_7u-4CE0CBZZS_mSCOyPFfhBxLbDm-j_jSHSQPhnCZ2ML_o-qUvsCz7ZWV4wazcoaNn3vuW43FnUKHHvzK0MV_oYvqFUvp3MTfaXRWVCqpmm8d2jZe5Fm1yRDr_tuokNoKjABzjaFfNykfcNHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌‌های خارجی معتبر پنج گلزن تاریخ رقابت‌ های ملی رو اعلام کرده‌اند که علی آقا دایی اسطوره فوتبال ایران در رتبه‌سوم این لیست قرار داره و تنها کریس رونالدو و لئو مسی بالاتر از او قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/30903" target="_blank">📅 14:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30902">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS5Gi6LssqBmcnW-p90Z3pYEkblT1IqlxQprYYhXAcSNXaMmb-ZG7yhLK2DTClaB8GNPaaW7ISaB1nwCp_TvuJ50KnIzjQiZXDx41ZHtbw4BY3VYMrCWp36yYh1c4Xsd16e1i3GOT18S5lvi8F0EUC7_XSVz0ee3UWI4d8Q7AbD77--OIeXzb087qMsxJedp9yDsoeBNpX7-8gG0KMp5H2qa-X-9HIHPHDtGtpoAGzhnlbwFqj_3HrVGaSkjOKx0AFIwqOaahC2s6NerC1fzCUwFsC8BtbC0448wgQ2S4PxUxTVS6-jHwGATTYuBJUjhwu7ruhdfZwOxWWOa7oiXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلای آرین پایان تکواندو ایران در ناگویا؛ سلیمی در فینال وزن 80+ کیلوگرم تکواندو بازی‌‌های آسیایی ناگویا طی‌دو راندمقابل‌مارات ماولونوف از ازبکستان به پیروزی رسید و مدال طلا را بر گردن آویخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/30902" target="_blank">📅 13:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30901">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEjGmIUUKq8sdg5NEIHaoPf6kLDgxeEewMOX_i3CG1FnCtTCD2F5TzY9-pfd_xwcxo9Ueb-gFsLLRT8ClUVMrdcZhzyb8BMa-BklhdP5taxqp7pm3EITaisbUTqtOKgpoAJ3dnkDSMHXrMpRjewxvEK2rCsPwmjCFqcTrwSutagIRX5qUO5m99flfCJSg0xjGS99k3dBqLZGd46JqK3TrCfde0pqAG-tuWp1sxjHamMpAJpPTkt8V8wS9KXgPF1mJJAhdBRWpabWgoAKASCh3c-hLnp9wA4PL2975wUVC7Z5kpwDR7fr5dDyoutSeTHwms_uxRrSzpD1kMWU6Sff2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال سرمربیگری تیم ملی امید رو به افشین قطبی سرمربی سابق پرسپولیس و فولاد خوزستان پیشنهاد داده و درصورت موافقت قطبی ایشان بعدِ سال‌ها دوباره به ایران باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/30901" target="_blank">📅 13:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30900">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G05_PvMWLLLMttJMaried3IvgJ56AcFjrU5AMrmUPhfPBJ52RfpuUfo9v-XbMdqXv3w-X5GIRy47WCJYtx0h67N3vLgUPWW0TU0p6ON8qm4piiR9-MQWcrzxYWe77OrfIfcAcuwbki-5SiCnhtwApToU5xz0CE-7BYJ3Kgfl74zJkBioAUQCKCg6DmR5gv_3v30YjHdL6_kSVafMLR8iJmS3qrvrZWXKs8bU8Rdig3PdmBddoCuvU1U-uhCoLahamrIhfC2OWf7IJx0pyuSf8_f_-xGKmGKTJJJ8T5UBtED5dsfVL4_OS72T2NC5bOKd6_Y-7ND4S2Mi1LcHL2EJWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قیمت‌پلی‌استیشن‌پنج پرو تو دیجیکالا به 345 میلیون تومن ناقابل رسید. خرید یه کنسول بازی هم برای خیلی از جوانان ایرانی آرزو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/30900" target="_blank">📅 12:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30899">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNOEM_zpiwRhZL3oRz6RZrxyvudr7lrhjacB9DFCBmnTnMs91PfIuBSzvpN0x2tvrZEAP9IdkSouXH4ouqAfEiH3LuG5fPCrO2-tRLyqlR85TJ0_CVVuAF2FXFOQyGWSfZmweJg7M5BdOcIjiM2LMuWUExvVVyKPVq2jG5aBhnen6cNMpUV-Jl2YlORJd0UtT0M4rtz9px0Kjh5qwwW5lKSppj_3BRC5eTXkrWRnbtS6dicz34cDh6WM3CXHY9oePRyqK3WtVbsohnSHbowoRYwqehghEgyWu3XpfM9aC_qbbZ9auxlQjOPakLE8udN3TJZVBAHTKjc1pYIeeKhpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/30899" target="_blank">📅 12:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30897">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
حسین ابرقویی نژاد بازیکن جدید پرسپولیس: باعث‌افتخارم‌است که هم در لیست کارتال بودم و هم هاشمیان. تلاش میکنم بهترین عماکردم را نشان دهد.
🔴
از بچگی پرسپولیسی بودم. مثل آرین سلیمی که همه اهدافش را نوشته بود سال 98 تمام آرزوهایم را نوشتم که آخرینش پوشیدن پیراهن…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/30897" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30896">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plSgy1NKUpJWHTAS4TVgJq-km8KGTEh8dnWWrMBrVuwk4i98ZQYX2o49bYrUeXsZyKF8cjk6stwIRGEZN5hULe9uPVmpAfKP1IbUbz8xqXXjeOb4325UNOJO673BmvjytczwrGYKjG7G00TBDWLUN1uOo0dgwCa11Ub43NIq8Pcy_JQOZpGvZRm364qcp6P-dorsZy8sjgT13Z3Ho7any47cV_VoAAl_YqLIWaBsn0QdWCOggspVEX4GFTi5lZ_eOt62oFjKRqd-hneltG3VgmJJL_dZu1yqrTe73yx71yW1K8xftZh6eS2eaFK2D6ZSb9ZyXTq2hiP-WxVbAlrjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیرعامل باشگاه تراکتورتبریز عصرامروز با علی‌ کریمی برای‌پیوستن به این تیم جلسه خواهد داشت تا درصورت توافق نهایی هافبک سابق سپاهان و استقلال شاگرد نکونام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30896" target="_blank">📅 11:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30895">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=GV9j8yapR1iBpovWvV4bW1BxORAtTMEwH30EeX_q5izJpi1JmagElt-UVz1B9XglAbLArwL0pUkDdjNEq69O79udIXi1M9IKqLBcLVCGF1LieIpuf8SkxvbFM7DjNKdPqSD9Y5RKSwVmkqLVIBEYzes8e2f_npQ5m6siWiK04C73mxLQvZAjkDKL7hJuNwcwQsHbUoATwYLCtkbU6-U50cs5DV9HxFCdHg-dEfcpatV4G6MbkE3Otz3hrLgZRmGvRi-6dWo503PyTJEEfgCwV_MBRPrHMx0fOnuMWNW1-JS2CCI7AwDWTBpHe9Z7HdWb-2L-RF5gSqER78S3hCEkQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=GV9j8yapR1iBpovWvV4bW1BxORAtTMEwH30EeX_q5izJpi1JmagElt-UVz1B9XglAbLArwL0pUkDdjNEq69O79udIXi1M9IKqLBcLVCGF1LieIpuf8SkxvbFM7DjNKdPqSD9Y5RKSwVmkqLVIBEYzes8e2f_npQ5m6siWiK04C73mxLQvZAjkDKL7hJuNwcwQsHbUoATwYLCtkbU6-U50cs5DV9HxFCdHg-dEfcpatV4G6MbkE3Otz3hrLgZRmGvRi-6dWo503PyTJEEfgCwV_MBRPrHMx0fOnuMWNW1-JS2CCI7AwDWTBpHe9Z7HdWb-2L-RF5gSqER78S3hCEkQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ درواکنش به‌خروج کریستیانو رونالدو از اردوی تیم‌ملی‌پرتغال از رفتار او انتقاد کرد و گفت: نباید میراثی را که ساخته‌ای با غرورت خراب کنی. اینکه بدون صحبت با هم‌تیمی‌هایت اردوی تیم ملی پرتغال را ترک کنی، بی‌احترامی بزرگ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/30895" target="_blank">📅 10:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30894">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tj7ZR8urhqJIBqvIkvgjdlwUnbH1Z7GMxYlNgdizmLkpvudj4qq_zg4D77D0IKTgrwbdiruDTW-hCY400xyTzk5uz9U37cd0u_ZQLoJoDfjOfFyExNchVm02Gyy5qh-fK379AH9alQl5l3aeHejJIeTinF__x_Y0bNS9MrUdvPjZHJaRcjNpQrXEO43XRZskofz34850t3CzEkWSXZkCFxlIYOJqwJztrgDjxlyHFta7Iko4w_R7zvzXFfkTG8yZbLZDUg3SLZwxSac34VKgbjY9gIY1VYKGGpm5k5DtNjpya0jXL-lkt3e2Dt3U3XnZaWV-UFjGdvaA31om0CHoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/30894" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30893">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPdUePSa76PLoRYKAnZ2r6olvCfVKMjfSWzfb0S6ar4RQDSaik623urC-EKV3wFH1HXHsqladCYBCmDNhmqjqmYnF36LNnvEF62m8gJSADCdBPsOrIZCisbPP_C3kSs7Iwk608CsF7oBPPDfyVQ8iBrU34VVzawTYtSVag4_tSvGdgBwDHBZAIhi17hdZNcpIJq2wv5xLIZ0D6Y7TyAHgDcv8Vzr-c-DKJYFjAjdyUmTlRetvh1iGw8KHNgsnqk6otL2M7bbO9P1c2qDp3TCWWdMIEe9xQ01Fn-VNhF0gTrgQ-MhJfzym8CUpCLn5v7kqMeI3AeNKaDgP9RPfWnqDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه
آاس:
رئال مادرید توگزارش شکایت‌اش از بارسا به یوفاگفته بایدتمام جام هاشون از سال 2001 تا 2018 ازشون گرفته بشه. بارسا تواین‌مدت 9 لالیگا برده که تو همشون‌رئال دوم‌شده و اگه این پرونده به نتیجه برسه 9 قهرمانی لیگ به رئال اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30893" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from؛</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzw8hIOT9Ep58yubgyZFlhlRIHxba5mLNpBFRf45j7LtLge5p0_ULetbn_BviJzX2QYQpPQhckTVidzksDR0oRgBRIkv8Wsnzgtt9km9so70jaITXIJ5AyVUtNKPrfszuLTDMET1PzalH4QyPWeCdSsWRoOJ2Cf2vabbyy-uqGaR0hiPopW6AwMktljdvQj8krU77rkcXLf00FzvCiz7z_EczV0wS_mP0VTSpdphEmTpjDm3InoZJ3Ff8G4iy7nVvE1Uh9Dsp3oCN5VtlfjyUfOo-v0bDbmyKvqKjWeqvRLmO44OfTfSGEu3Hiz0APcjXEgoJNCubJQwJOMoAiUfYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو ضریب 2.0 دیشب که به راحتی برد شد
✔️
✈️
@best_form</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/persiana_Soccer/30892" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30891">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGIryV_sEVhNsCHf77YseEVz0gRk1k8mqFNKrhzyVeCgiuH2TWw-nzbYqGQhkFkMFCZXKSiIIrZ_mqigS8LZWJ7VQLq_Eks_lZzf80gyY5FKfFilQKlmg33Jfr56ONM9th9a-JJUWafDCa1YAmUi7IDr9O8Ory2FPsK7C8wNQjwTxx4vvWWBL1kRdwQZBnomw0P80pb26IzM2nHukexznlvW0Rpd0MfcY8Hf1Shng0I4EdejmjIswwDxSfp_fFZQT879d6wSZUFkAtLR6NpOJWPvja9Ii81r1lhNuEMPhwil3FLus37eu6kBpwM0LQtHxa387LYi4T6mJGYmkZsIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
10 بازیکن‌ایرانیکه سابقه بیشترین تعداد بازی در تیم ملی ایران رو در کارنامه خود دارند؛ احسان حاج صفی شب گذشته در صدر این رکورد قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/30891" target="_blank">📅 10:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30890">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcxsyBETL0mEoMjBQprUZULpumImowcAfaM8Oq7obMqWEV9cUrR7GWLmz9XAnvxWpiEivhcH7S3rheIcV-7_BH7pA5iTQBiMi7JQe9kftpW2w5ZmY2m4JDqRYjrgc3JjIFKX10M-7BVb_fx7JWGty3jgG__rqoh7NWO1xtqcsH9on47yuwqq91umUOuSsse1Fy_93QkkMbTqU-41xdsYa2YoxR8MHzTO5pib9RP6kxEJ2mgqvc0HwkTP4yiruu-8XGhlgX6iiuvyWe_uMhAuDaSOnE6flXRwGHNqd7UucdJgFOamrHine1XszdGJXF7zm_jrjP4kvVhse0jslhQEQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ترکیب‌منتخب‌فوق‌ستاره‌هایی که تا به امروز با هییچ باشگاهی قرارداد امضا نکرده‌ اند و در مارکت‌بازیکن آزادند. محرز یه مدت با باشگاه الوصل در حال انجام مذاکره بود اما به توافق مالی نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/30890" target="_blank">📅 09:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30889">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMJBW_90Fv2tF1Vz89wRJYHsQ-YTAzNxjzqSkzrPHG9zNCMWaIrRnVmAXGQWhxWak1cE8jsJYF9YnDjGd-dbWjQLjPxvvXy2014_ARATupuuBnm8BMKOasMqyr4XUQ0hjB9sHZUKO-Rg4Ar1zsAWawgjc4RjLPkVZxhHCgOwXCmNd1wfNQPfnui2UmRnt2Am6-z8Z3wYHJP-w_fNQc0Z6VNxdy8n5We4BePa9FlGyjwzbHX2QHlGIDsdcGeauO7uOd43_rOQ6qrYtwnk-_cKoce2RkPPosge2_z2NjJvaOmBVccn72s6FlwqfwCp83vgLAylzymJzOgHA7z7HbEk6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان که‌چندروزپیش در اردوی تیم ملی جوانان گفته‌بود که من اونقدر حرفه‌ای تمرین کردم که هیچوقت مصدوم نشدم تو بازی با روسیه مصدوم شد و ممکن است که چند هفته‌ای دور از میادین باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30889" target="_blank">📅 09:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30888">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=e5wObYDSAw1ETXAa6iwQt8rAiT9kkzxHcCxV1h_E_aC2YQdo9ssNrqnlaVVp1eLZo111cAzL1ao0D3oyuSURrJVwRT44NRBgODlKqP43fuyXX3juoZbWfa1zn31JSb_LUUiLXrF4d8m04b6wUSZk79aoyfOPIwuzy0dEMPqSvNn3ySVjPAL-ibpo4HnCqVBL5Jnt7CUfn-ISJhzlr2yULBJbdyK5bxl_Z1Ql3hkVUHs_PUGkbkKHpItnq2XvwWOp2jJv_SXqL-wXZBvu3K9kTmGjbfnAU74HH9b4BruSEaURuSlRRWtIcGhW6SZKJtL89GRicTKHTqS8VH6umQbE0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=e5wObYDSAw1ETXAa6iwQt8rAiT9kkzxHcCxV1h_E_aC2YQdo9ssNrqnlaVVp1eLZo111cAzL1ao0D3oyuSURrJVwRT44NRBgODlKqP43fuyXX3juoZbWfa1zn31JSb_LUUiLXrF4d8m04b6wUSZk79aoyfOPIwuzy0dEMPqSvNn3ySVjPAL-ibpo4HnCqVBL5Jnt7CUfn-ISJhzlr2yULBJbdyK5bxl_Z1Ql3hkVUHs_PUGkbkKHpItnq2XvwWOp2jJv_SXqL-wXZBvu3K9kTmGjbfnAU74HH9b4BruSEaURuSlRRWtIcGhW6SZKJtL89GRicTKHTqS8VH6umQbE0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
صحبت‌های جالب عادل فردوسی پور درباره مدل ماشین اونای‌سیمون دروازه‌بان تیم‌ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/30888" target="_blank">📅 09:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30887">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huK9GteZsE6Fv618sQk4P3rTJS1XigIB10ZtTUYG41q3db3BJXy8gCkcu1qkK8CUZ38jBkzn9tfaE71_khxCWZIeQeM7gzI_HipcGbQDEI5ze82aHtuDQ-B1Bhx1NyapqZedV-Hd8DweeXdU_K0R8M7WimD_KDd0gi6K82fF_RP3pgYREjugZA9buxe--7_X_SZ3KBVrqqGE8icsEJ26aQyFcqMlmeLCRVp4bHiZppCf5gNRv_PPdVqwjKT7AlcWXATD83K9Uk0OWo7H2WZA2oNjOWyqHDVLxMVyYgRKz53Waq2p8RnjjcmvDyilcWWyoh1G18oF8q4iM8hrpVt_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ولی کریس رونالدو با خدافظی از تیم پرتغال درس خیلی خوبی به‌ما هم داد؛ جایی که نخواستنت نمان؛ حتی اگر تمام خواستنت هم همان جا باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30887" target="_blank">📅 08:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30886">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxbRBb4KSRZSHLrP-xr_ILJz_PL0xd8Eoj9mEmDGLa1KJ7C_Y8DPgspuarpKYrZZHrzibgrpnD0qGyZBhN5dUzW7hqAD3sTK1f_-0HLifkp_RrHjauSFoRL9jST9d0caMBsa6ZLuXFKE8MiJCjkVvofgJYp54HOQ9V9fqNBF3gjJVzJEufxUy7wne879zfx7L-D2AwlKAJFVg3zuGTeJ2eb4VzxSBSuTWTQpWEqxcllZ5-nRTjjOlxYiagearbRPrEcp07sY9ImV0y6WUSTGqFcqRMRsPik9UP2CbTKfjGarNS9UGap90v8XBmkUUeIUWDKPzvfpC-paX0yU5OB6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
🔴
معین توی کنسرت آخرش اجازه ورود پرچم شیر و خورشید رو نداده؛ وقتی تماشاگر شعار دادن وسطش آهنگ خونه، ترانه «بی‌بی گل» رو هم اجرا نکرده.
🔺
این اقدامات زمزمه برگشتنش به ایران رو جدی‌تر کرده و احتمالاً خواننده بعدی که باید تو ایران منتظرش باشیم معین.
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30886" target="_blank">📅 01:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30885">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇧🇪
🇧🇪
ویدیویی‌زیبااز دوسوپرگل استثنایی و محشر کوین دیبروینه 35 ساله در مسابقه امشب تیم بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30885" target="_blank">📅 01:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30883">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHc1inUpZW6jUN6OILPsor3LLNPMNwVU42XvI6yxJhZ44o55EOrZm_DE8FwKl0XMfyeXGTkdpMeEt4eaX0qeOgI79qD3BY-MyI9EzM9JTCynwVQCMBqH3cfeDp5m1dBpsJbeM64W5-kb4uEboHIqqcVcNT8r4MVlCU7etdaMNX9l_2zgLhJ1fNCsGunpOJvoLK3fHw9b6fOk9ahK6lJuxN3m6Jt-oh2wUI2ZsGLrVdSRA7VlmYbHIlufQmJCj8DYkC62BCeGuZ1s8bPS47nAhbWtwb6Gr0JmPQDtagT7ukvIY5J6sId7Q9ppxVsnN14KWFvpJRMyqRaii4bCQZ0EPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30883" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30882">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSxZw2VZK-6by2a5mvhrq5aHMhsz3-vbgqM2xtyJb9zCFqdo-rtYWCGfqHTjlj8NpJdPvNdG73j3mjF4t6-3JkyS2QtViW0VaWAaA5sQ5BeX-Di1JnN7lzGqdksDAq8UBmbudT6u_T-2EMk1A8Kf_iJI1dRtDC6zfUP87nxfdsqAIKran1Vgel_yH9Ed8jSZrMD6jvOTLfSguwAPKzdqSY0KhqJFn0s6GRng1IsrD37g_csSQIr8WsrGuLwXgE28QVnr1xMykb99ycy0fSnGRnVAX8h5G2QHtTYckA_AD39fQcgVWi5yaJkssDcGZOO2sp5w1x8ApoYiZdx499A5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
توقف‌ خانگی‌ فرانسه ده‌ نفره‌ برابر آتزوری در شب درخشش جی‌جی دوناروما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30882" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30880">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب ایتالیا - فرانسه، بلژیک - ترکیه و هتریک دیدنی رابرت لواندوفسکی؛ لوا با این هتریک در تاریخ مسابقات ملی 92 گله شد. گل‌هارو اصلا از دست ندید فوق العاده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30880" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30879">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvKAVR1PdYTJxrrHpDd07xQ7wVgDb2A8Cn7Qe8hs8uD3MFprjWPE-V_G25AbpHgj8gX_S4lknjMQjm7-5YjH6VuZM9jNqeLOQgr9pVNXasbYDnoQ3Rw2lhXKRPhDLnngkw3I1tKv1J_vegBJ4tGQOsVTRFe-BNYeQVjeXjBiZwCFMt6Bq4r2XUoLO2re3jmBnVsO5WfkHZwGRi6MTV2cTIHgZyEqoRjVySIVVsKAV8s_Jeegqm0aG3LSJZJG95Nv9SrNFC3o9g1YENoHajsPHny2PB0EDI0ZChVfMxXQRJGid34ICoN2ipzi5VOorNHcgp9blwImxJEPGR8sn6riWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔴
پوستر رسمی باشگاه پرسپولیس برای زهرا خواجوی گلرسرخ‌ها: 2 بازی، 2 کلین شیت، 8 سیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30879" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30876">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr7fUemmq15U5w-GX2DhEwfLC6McYrIuVzomXodCjBm5kfJrTzwrQVGwlZtM8yotbrJs2p_FY4pEG1T7oT_3S7js7yZZ4yhLUpvmm568fLiknFQsPYMsTcWmp87W4wOJOLf4Xxj4IwbAROLL4yPapUaLLMEzKfx3WD2iGYIJkhQx1vRAvfmKKNXDu-x8qseSgbo1JjLTG5dMxmMYaS5pTJhpO_a1KRShrDt2anSrnQttUM2N2wkoN2V_R3kZqMiN5huCjvQRZSIDmTktkZdg1IYXM0zTfJpDxK5JMCsvgHnG-ijwgpJukvs_D10zwLDjMmGsPQg6EUOMOIkDaWceoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه A لیگ ملت‌های اروپا در پایان دیدار های امشب هفته سوم؛ فرانسه با ایتالیا مساوی کرد. بلژیک سه بر صفر یاران آردا گولر رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30876" target="_blank">📅 00:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30875">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnlBIyfVwHYBBGlSGWD_31VL9PlKEwxQOxx1M3cASUXBQ7gORuSqfbVu_iL4lHtTOapWr1_lwEowbcUo85-Yq4HiMEjmr8j_POqwfUtFp2TSMG25dbPG7sVfPRkWVfaXeEB8M2-zaB2Sbsdl0gEuRRc9R00G3RM44cSdp6Wd8aqkS6mlGGxlgMtUVjukPTdkplpFPWMY8G1DZhaa4jdQ2dgeL397OGoI6ooqNOo0lcKbxMfgSFx1Vqh-8Ez8ndxS67e6yXnCpvmyr6izj0BqZEXuaiwECtAnelsCqCK2fzWRuNvkVxZ5bODWqY-hd4K8kFwOgINQFNrDTt-Z4J35gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30875" target="_blank">📅 00:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30874">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeoqCMRx4DoOT2njIHUuuqvxFR2Q9LIFzd2T4eIuayumm168yHUiecG9znZlFv2Vc1RX11LzyfyEKnB3JpIjLIBh5RYMdy1HKGY7NNyE3NCWaO1ZyF4_TN_Xqg69B9VgJoQLej1cEzbZkCN3YSxEnA5wzxKSEjQ0toMD7j3act2K8-nc1ia7MKDmYn3bHDp_pk4zEzh7-hV0TG_4UjPJylUMw0VXQZCHH_y59cmkzDeQMV7JqVBNmW3Z1FLApDj92uaav5bMc8m7w5Y6KbkittFWw5SwoKQ1Op6hBqFwMi4NzB54zQ-hVx7uqfIrc4bi_NgadvB_es-xeJ5O110q9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30874" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30873">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gftuXqSn2k59sBoBo7_0BFVRKcpO9H4UjL0a6Hiulwzd8SoR3Bn0XZ-x_4IvXpoU4TFMuYoLEyaH8oAvdIXJziZYroo6rKGLJJCZxLBwmwhlCYRtQs3vJwInVlaTsQfGmWD1w1cmZ9PUvnylwvJ8cOLD020tQ4szAn4KMHlJzd6QdUZISpWS9xWem1rTAZLEN9qEUw9hIvE2o6tJfkMZrBlUOKR2RMeEVr06Aj-W8M8q6RM9PdIicg_lhztvxF4IAxZ1K_bFo7h71TXeq8uF4fVVlYY2YMva3kRKKBm6zuSu9y5fnPTYZGcoZQLxjFAVP6y3MNbFNkhWh1Y54DDgaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال فوق ستاره تیم ملی اسپانیا برای دومین هفته‌پیاپی بعنوان بهترین باریکن لیگ ملت‌های اروپا انتخاب شد. اسپانیا در دو هفته ابتدایی تونست بادرخشش یامال انگلیس و کرواسی رو شکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30873" target="_blank">📅 23:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30872">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9yiegzRVr9fs9hGSq1P5hjNM48wHvjD0bPj1hwIdC3vjfswQiqbQRN231cog8OBBBpYPUupMvOGd0X84E7J1lyUL3ZEFua-lejuuac1XdrgXBmSDaazDK_kRoysXKPzS4gLr1vF6OXMg6yo_fG1dmcwu7Obvt6EMa6UydWC5YAOgFkIENKmb9BX1xNf1_ooPoDvsCf7c0XYtnqoDLWrhWfKnq0FYj_DSgENOxInBbYV0Oz9gLbT7EDvLfh9RUFp4AJ_46Vrn4xHsu8cKovaH1aAoGQlCUhMmTtkjZfAGDaMkNwquBSaO5X1-qZi2WHkgP9ymcJFArSgduH_wzLVIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30872" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30871">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojlSm16WSDgJAQLWnTQxRCcJFS8P9fQOs_eHB1MJoTX4lWx5qLlWL_aD1COxWmtEJojToEZ7uxEf9ghgV3OHPN9RDwkOJldcV5SXgjUBXHhXgwR59TuvU5Z6bX_EB77Sz7kQHTXU0bB7sMXQ7oM_haKHJeL8joCrwzxcAofO1vGGNFvRhrfuM1vvIQfnJ9YasET-p9PzpfUuyqWAr4eDZekfV3iSouUI7JgvvW30w6FvaFgP1C0Sl2uvGXzH6aQYzlP0RE-yZBc5baVQYQEafJ-CsBodkvAzhCax0yvSROEVJMnPdZRsvwbjPUk1neBxGjWChv_Mrx9X_08S6ELRFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30871" target="_blank">📅 23:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30869">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1dSPT1T0Kq1BQg7cIgQKJYyfvJOfG2ntH1iakrm1NKp8asz64jscOoN8_FgRcMbwTHBxZYZ4MUXTXLlssyelfWYlO6f_byUCp6fKMznZ4cmyN0N1xf7M2qlJ2qZb-1ihJQmaIrhPK96loVtoO79OWg5iU45irjEUq_Pz9j-6ivp-uKXlIMmRVW8Cl-VFL6ydSNbo-dPb5sUvSyeFOCR_n_paEIJnug-06Dvn_2Wm3_WlekuXCijGgO7kCZdWuuhnGX-Baevt1DpA893XGkhY77BWfyGHYKVU2hUwsZtoAC4hHX_Atufz-_QwxEdaIhGNYDwi7utz2VDEZNxWwrxwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/acPQwh5ZbTJXyoPrnwLgKwpVgkVX1kOz2zOZZ9WAl0prd0Fx7K3A6YW1ZDXZDwVXGFVK3U5muxO0UgaG_LrTJiK7TYNbkA6vAIffWBzSwTCUDFHoYiJJt20YqFbejM-gvjD8oE-I0Vr5rgKJnl7E3qAmIoRRkzo8cxB9Os9Kb060vnLaiusZ6nIKYK0dYHLk2F5bFuxyWJMtN1_UvkDC-YRaUELzmDh4rVUv23nDghc2NvBFW_yilwB_VJPaLiiB3v-wSVn91A0jMj4c9LYNntt1MWJfv9orzigWDURREYGNcgTwfH3rH_r1GkEdOfEcf6Xpq9pFsswV-EUEdRmd9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تعطیلی مطلق استقلالِ سهراب بختیاری زاده درفیفادی؛ ۱۷ تیم بازی‌کردند استقلال تمرین کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30869" target="_blank">📅 22:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30868">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=p00oQQ90gO57hDlpYJ8pWXG1n0Ncc3nugszXfRvB0WI-VuR0FJzZdj_jkIRZkcuHbVT8jUspIc3DZ4FEowEtlRij7ovN6KbC9HfAW4YAZuzBMa8toAOyqMbBe6-0ioAhB_NdtLQ7KfTtUGVgyBwyt-yI5IHmF1ZAR-CvsJ3UtBrCsYJU9BINb42oeigbFgQ8k-IQhxYrQtJITMPeNz-uDG9P00L0gUxfbGPOyzMEA6PByZeUr8h-EJU0CFk-x_X_upPnsDyfB07yYywmBw-mV9oDf0AmzSTmmfWPLw9c5yJjSSMe3_MAjPmdsxIZLoWklWVC_5aA7T1PaCVa-Igo5FaFlBZ9o7UW9t5685Tt_nCrrE4MDxFqMiAqZDNm9vwRFByzDHzDJGtxlut9FCaIkELqF6Yzj3n41jC_8TLDi6OxuLrNa3by-CD72GtpCze8Q8popev70S_TwmoEgpp7OYDqvTkIednMSXe4Y1vh6zqcNB4hfbs7SfS0ybxmQlXmLe3x96wQMUtTKKzBRm6HxdjUDmqlmjnE7Bj3U9Fe1xGdSMJbCiLaPRvELVvxb16T8RgVUPmejz8xhjsRqIEI2zh4h8-E5ZBx6T3tJQuhz7viUyss4CZoRfziZmlDeKAnHfTzr87SrFfl8vhRzNA1n0sgLvTn_L4zqPkKWHc2uhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=p00oQQ90gO57hDlpYJ8pWXG1n0Ncc3nugszXfRvB0WI-VuR0FJzZdj_jkIRZkcuHbVT8jUspIc3DZ4FEowEtlRij7ovN6KbC9HfAW4YAZuzBMa8toAOyqMbBe6-0ioAhB_NdtLQ7KfTtUGVgyBwyt-yI5IHmF1ZAR-CvsJ3UtBrCsYJU9BINb42oeigbFgQ8k-IQhxYrQtJITMPeNz-uDG9P00L0gUxfbGPOyzMEA6PByZeUr8h-EJU0CFk-x_X_upPnsDyfB07yYywmBw-mV9oDf0AmzSTmmfWPLw9c5yJjSSMe3_MAjPmdsxIZLoWklWVC_5aA7T1PaCVa-Igo5FaFlBZ9o7UW9t5685Tt_nCrrE4MDxFqMiAqZDNm9vwRFByzDHzDJGtxlut9FCaIkELqF6Yzj3n41jC_8TLDi6OxuLrNa3by-CD72GtpCze8Q8popev70S_TwmoEgpp7OYDqvTkIednMSXe4Y1vh6zqcNB4hfbs7SfS0ybxmQlXmLe3x96wQMUtTKKzBRm6HxdjUDmqlmjnE7Bj3U9Fe1xGdSMJbCiLaPRvELVvxb16T8RgVUPmejz8xhjsRqIEI2zh4h8-E5ZBx6T3tJQuhz7viUyss4CZoRfziZmlDeKAnHfTzr87SrFfl8vhRzNA1n0sgLvTn_L4zqPkKWHc2uhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ صحبت‌های جنجالی و عجیب و غریب حسن‌روشن‌پیشکسوت‌آبی‌ها درباره ریکاردو ساپینتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30868" target="_blank">📅 22:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30867">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzOyHcHehOe4yFUze5_WlSlFhUKC7qP6sD0e95CYnA-MVVRuaUzomoGIQ2ox6L0ZZ8eZ0y6cDW8PD7D50kVICR9BTKYI__wkSbKCg4bPH8NTdPPxotwLyGTN9BYEDZslbqgE2oloiudCjCLOnrTYrvNiE8jWKLo7po1wzjGD_9gjArLNxZN1NFXjlU4o8-QYpkRMz0T7DB56WyJBrQlCKped-psgaJLakHh6qUuEESU_fXcvaYSEs9D3-bHAxKxV1HxCxD9zAXt6uwPSUjMRt2mmadv5Ppg7T7T8kbat8KBrjEVEnGgkwCg2WazVCDJKo5ygXX6LcsGsgjvwh_STqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30867" target="_blank">📅 22:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30866">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afJSQgl8ofaFQa7uaheHuP2AGduUsTctut3BYy3eJuQK-4JZ0EUegU7uo5c9ZkBHUraW-y4IW9p1iCA89VbEIZsbVOu7UAB69UNPEaxjbDKkTHsb-lrGVhVe8v_r550x-SCCu0k-dXCC6p_yeY7he0ROT2IUnsh0x66dTkDz9rToAHam1MU3vfiyGcEYGpeobPAMskFeK1Q_87Ym9vYhK-nBDuFLeDwR4N1klUgDHU1Gx3T5Qx2PysvCsuImf2oVahWZbgsn4egqIlqN39G1WEgku1toZ4G0xIuKCCN1MjAhyyKEgGuo4AzH2TrgruYiftp82BL4pXcov3Z4NcBvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30866" target="_blank">📅 22:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30865">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBhpnOw8eP8Mcwk_M6bORiXVxLVymxvGxJRsqkBSARf7ceRAZ5QMD00qahd6cTm34bxOCNK5Kkz0giG9cVN6VhNtvvWWX8BwriQ-1QQLDJgcDHIJiGUfSxiERK7xZWpj8jUGzLDEH8udl7tDUMRUytiouU2asLvLCQPQpIHt4B70pkiEKXtZwCGVWiDBypA8wyujWAQpHo1xZatJcxR1gGZNpj9qF6hLwrTHsFJ3leJDSxJ82mmDHO3-b6oHv9iU5DEcwcVlkcBnmtUU9Gf6egFmMki9OW96URnIEL-ywJ-HE-3bQ4wPzYzZ4nt2JLD6kVz6gSkHU6VVYnfF5Rn_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ به‌احتمال‌زیاد رقابت‌های این فصل جام حذفی بانام یادواره شهدای میناب برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30865" target="_blank">📅 21:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30864">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRN90GiThrq0afvfXvo7pACmhL6NUuzDKQUJ56PW5X91nEXbCOSywxWrAD908_xq8yJpS9TJXtprPVeJOp4kQWXgerJsiwcnuxFShw88qEh4MlYktYtyChXQdqqUN1sUo8G2ZpJjmua68e1C4UvWmfIaLr4rqOWMiPxhxl4iuP1Tz5Z9DJX_q0Li-AbzH_xxXlnc73fuhV8-i1OQsqwe5lhRq6LeGDoOZi1jsuVQlkPdzHV--ihc32WSqUfK0wi9Da22DmkCeX58TpGvArfHAPS_cDBMIvx7HSxdvv4QZR9A_iCys5_WIrEa9tT4vvrpapCec5nYhOkS6Ac6oqrBMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔵
#تکمیلی؛ درصورتی که حکم نهایی منجر به محکومیت منچستر سینی بشود؛ ارلینگ هالند، انزو فرناندز، رایان‌چرکی، دوناروما و دوکو بازیکنان‌مهم این تیم از جمع شاگردان انزو مارسکا جدا میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30864" target="_blank">📅 21:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30863">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrDqOONRArK2nxBZKOpBF8H_mjsnclqpNo_p_xHCCem0OMGOUfqas_3v3iKgTLfjIVQIzqMd6qJvUwCKdI4hDAcjkSAKnMXMr7ewFrEc8nOJWkfUrj75MBn8GjjaQqSSVMdRiTeLyXao2_M_Zvgoqi9w5vYjSrlmYrkSAzLgo51TbotpjNBXKLoDB8xtr6c6l5LlY4476S_l2XAOuJKdUIhzGRzUppfqKp-kIt6iVzCY0AHm2r_B0ptlwrqPJ5e2uYNzL4W76H9iVssBCCDmo3-V0ALsCuAAJqkMGMD_QDT2QANL-vr5nRcsFxYcysbyC04ovIK2jWQvvfAW5A2YIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین و خفن ترین ترکیب منتخب تاریخ فوتبال از نگاه دنی کارواخال کاپیتان سابق تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30863" target="_blank">📅 20:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30862">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb6GuTScVer_bfxfH_cJ7OaQlpimgMX2rI2tbCdJ6Pw8tPjv_GhP-xbVyeMH8SW2VUaUlgynlf_TaHqnEGEIx-iLTZ8RTJ2SUiElO3045yxgQ_YBPPtxlnBQmd9pCUJhpa07ARsW7PoGgQlLgoK-A10UWvPUbIqNERKZfcA1d3A9j0OzCls2NRQ9OtMLCBkqu4SZqhagBlNg6zHQLneLiiI1U04DdMZ_LRBjZczd1weD9fDM5C4vy3x3k42_M56Fj1ozQApAgaAkHP63CboDFTCjMrYGN_BqnqYAmNpji7cFMhTXSnz0F8tSwTrlF1U3pyZLB0vE5P_AT7MDqTka1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30862" target="_blank">📅 20:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30861">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msCbuW5w-YXuwBKrPY1lwGuBP5r7KILe-EYanaeKLhUfB8YpSv7w-ACdMCg7yYDe415GRtFGxlR_sPUUjPy6ShkZvgYLUBwqFI2s7Liklowwt00Clql9wznJBPnjP3g0x2d2MeIh9kPY3SSCIlqIX93DGKC2iypKr4WhdAdFpC4Re5pGMFUa7h9YeyWAyKBpAm1q0_nuNezr5EWvSqeXmL5Zly16xdbfQUl6tIyyoUHbla4VnTqQ2ssjwxGZC94QEOtM8HvTQN_Iq4O7oKmWpM8a90v_ZPgtFOdqkZiOSWPqu_4D0bFjZpHNTbWp1caRwYwUHL84CnU-3tEjTszp_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30861" target="_blank">📅 20:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30860">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHBW6PRrthdCm4ecQ4V3sRt91XLeRYuR6FKOVI2XNsmwKuKEAkRNL85yLa5zk90dA3BRbmeBw2kuYf-Qq_3eKQ5zvkS74O6qxyui1PhkcBW4u5QcpbQochV1htIJ3SlgamQenuSBTMM4PqoM4AMzIBrY9bXdiradyAaYLMDnEjzhlZQsD3mSHutt_hugTsp40s1pgvwh1_WHHJ7BR7XtDQg1iRVZtK4IH4l9uKpAbmd7UDNVAQvWWrgr5IDBvw-91J22WLIYHusIK_FgQ6sL2u-t7TwpFfGIC14N-NYz7M598dC_Lu7yQmd4ze8H-o3SfYNLOhYBCpRNwaooFAh-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30860" target="_blank">📅 20:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30858">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=bT5EuEi1N5yi4_PvEeMG56lMS_P6L9vG-F4ibR65SJ16ybLejR1MfO-CGjb6stBO2uWATgu0zwqSIfa0lrAyCY3rAZy_JQXHu3zygadX9RLiYJFAOws0d1xDYIEFaJ72lWnnzdBwWvvsVS1UjqlNKPA6NNqVVvFWFVSDxqFn_ZPXn8HyIcN_Pgx-hxz67JoCjMEOKLayFyXmpsg3Glu8Yr-UKgs1IgHwY5zVHkstraAxDjdVQYI47ubXldZUb8arB5vW4MdsKNLO5vgH29iZV3X2_Jg5_LTyrkoJGy6ItC8-Sgc-lWXsbnkNwdfp5hsAUbr-XMaZLtFqzrunRQU6bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=bT5EuEi1N5yi4_PvEeMG56lMS_P6L9vG-F4ibR65SJ16ybLejR1MfO-CGjb6stBO2uWATgu0zwqSIfa0lrAyCY3rAZy_JQXHu3zygadX9RLiYJFAOws0d1xDYIEFaJ72lWnnzdBwWvvsVS1UjqlNKPA6NNqVVvFWFVSDxqFn_ZPXn8HyIcN_Pgx-hxz67JoCjMEOKLayFyXmpsg3Glu8Yr-UKgs1IgHwY5zVHkstraAxDjdVQYI47ubXldZUb8arB5vW4MdsKNLO5vgH29iZV3X2_Jg5_LTyrkoJGy6ItC8-Sgc-lWXsbnkNwdfp5hsAUbr-XMaZLtFqzrunRQU6bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
حسن روشن پیشکسوت باشگاه استقلال: ریکاردو ساپینتو تو اردوی کیش هر شب دختر میاورد تو هتل و ترتیبشون رومیداد. تو سعادت آباد هم خونه گرفته بود مکان کرده بود. بعد از تمرینات میاورد تو خونه و شب رو تا خودِ صبح با اونا سر میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30858" target="_blank">📅 19:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30857">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oikQq5m5Wmj8USyWi1UNiNDJ27xrbJBiyHiwqTzvK9x693_QQcnr1aaWmRLgvPQVEyYpphG6ncu6c38YakmDA2xstrZA6tMNTHY_q-LUseTosvxHptp8uvAs0ah_3S2g1MkL4RxLYu6Zv1gax1G2L1ZnsVlNKRO6fldnXidzy1YjuRops77LONidB_ezbqfY4dqVXqH-Mzbk6Gx4SdbEeEySFjmnf6LKDAGI8qZ6wA89rZ8AS1hOXIf9ljLQ-YQawTnnb0HTOc4qzve5dxjuWDesB2Wtd6NJhyYGCpJYWigz1Sjxitpjgl2TlUum36Fv9o13yMT7pwAY1Lz5b_qiSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30857" target="_blank">📅 19:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30856">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKVVY73PSdLjUG2qsl4eQQw30FXREDgZa4LLVa4XbokLldsjo9NRZFr88OlrYSVfv34imSy4h_S1PqIyeP3-WgYHvdhowB0OCkGgt42st4zu1T2QeikWdaz5g2F_60_t-wuPL7dYhVUHgE3Cg10Nq32agNq0kO9WLoghnTrlC5MgZ6U3mxhsyafR7Wr39O_cLEl0arPu1-kjdL-bxSwyt23pnhtPKBa-gMBSlORIKe4WMZISvFTKf5C3zoNPtI50hiu3yufeShwrfCxnAbhLMuUbadDCidWBnafQlPGK4N7g_-GBZdrT3uZEtnzLlUXFKEeZBXwUP1no-0A0OJcPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رضایت‌نامه ابوالفضل‌رزاق‌پور و یوسف مزرعه رو هم300میلیاردتومان خواهد بود که باشگاه فولاد خوزستان درنیم‌فصل با فروش این دو این رقم برگ ریزون و سنگین رو به جیب خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30856" target="_blank">📅 18:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30855">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZymhwGUnNC1rS3_N0XJjJjOoMIoOjpEHV6q_pL4_74HUoWodZFC4n3Epl3uzOf9CPTXCfbxF64oIN-2rm3ytepHRVuR1bcXn_kdcx3uK0NncHMq2zCTLIc7QcB4TbUNpdrxRzlRLTxWKn0MHj_s63GWfw-DR4CYk1E95i-fmPYFg6uNJy4bP-0sByg7wFuulv7s59BiYTC8-Hu4hg5SmAw-S4eVVVa4vLyhFRjJfKh4iY68c4ogeTbe0QtG74Ywcw1a9mDtPCVsyidX21ClRKHat-p9BmGq32UVEMvMnu8DjzU7C6WfZy6CrNxmFcdAenb4KEAHE6a6PmxguVJwszg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
هانگ کانگ در شمال نروژ، با جمعیت 2484 نفر، جایی که خیلی سرده و یک زمین فوتبال زیبا داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30855" target="_blank">📅 18:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30854">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6l6Y00QxcR9kB5M0I3H4GBNr7LuWK_4UUmCcxV95ECPvN0PZtbA-rcVzhrqGpReCSQoT8vWongkObMfPkaN15pSLq5F7IEeklpwZ0JYSJKq2Xhuo7N-M0BhTulV5LhWa2b8KGa2zvK99xmTg5efe0YyOY6TU9T-UCo-n6nI73keTeh4Ji0Q6ZKq1EKBAQ1oPf-ZN2lA5vJygWYPVOP41xNBGRGeEqp_kMEr9jagbRnkshxzkyPolictPXzl-xNG_BvJ7pzMAf60sVQPgma-LTMYcbO7YZTS80-695UMr4e0zvQ1k788KiMBPqCbetNPJSPZRAbpCNaTXP0PQTT_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30854" target="_blank">📅 17:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30853">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T72U9GIR9VwqfRAtNqi-2jZxqDwy-sCaRoazr96kP1tIYhoecJ9b7q-KEkxZPa0dgHwmh6CXZEG6gKdiglbiYeKc6n0uqnbswtF6NOZVnxxiNoroEDl09cxW1YTGqCJw2HcsISSkPDkBPWK-K6YDnqqgKPLujE5KpbC_Hbc626p_Jk6zD1_V5i2SLBFS_DSnNJsStL6nzHVSgEU5cexYPcreILiTKPdAODhAg4SiWH663LKrtQfr9yDW5vDl8awFrusvwz8FYcdk36GvSgn3sNEAN7uiM6MXSQDVmY-IpsdTXPupYsMRN4fpbNnh0eg7Y9anx5WjLpFIIC-QmAwAig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30853" target="_blank">📅 17:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30852">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRICsvo0pRyqdhdX3v6PK4SSA_EHvUH9txmM6JgErV4cnF0X-43MUFLdqMvlmMPzGunF4Y4XXwBV6AcbpYUJnJADWGjGavk8QcwAkHILwlbYDxGz6KoZdA0RxKibCbnvWs3SozR7kmoG95ItU8unSbA1GLr2dow9eKPs0EIZCA5JczDY6qd8znujoZOK5wMv5VfNlXuc0OGpQ_3o7Tjn_nwRYpkYmPBpptchu3JpesbXTQQbzOfrM0WCclWTfDTIun6IJJyEuMlIavk-tgfGr-mW836Ob_Wd7vmzjRcNEdWNAQF0Z8pimBtsfiU3TCEzre8LUaX6ehRclFu6DUJHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌مولر درباره‌بازی‌معروف ۷-۱ برابر برزیل:
بین دونیمه تورختکن‌ما به هم نگاه میکردیم میگفتیم چی شد اصلا؟ یواخیم لو بهمون گفت نیمه‌دوم کارای عجیب و غریب نکنین. نه برگردون نه دریبلای اضافی نه هیچی. باید به حریف احترام زیادی بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30852" target="_blank">📅 16:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30851">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8nxtt3jpwcSQeEy7OusLx5C5zbppnsEcniOkH8dvvomJdAWW7bzcUUVO_xjZln1qOHCl-APxOa4ZetcmGA6Unk6vnzqnwMv8yaW8TBKk_4QeQFbO6rg9-fFXPeXd9_rE58U7vdgecXLXMJr80HrHc3NIyKrZvI4XJ_mN5W0FrXGtx-ktsIlOQShdq9eGLfaPMQdDP6HdXE4SO3N_wPPeOuWSkTI70unlmvxslwzrCk9_tLnfS3XnxQYEkK0t8cKXei0NmBsQcMPZcfCh9jNMLCpfFbjtkFRALio933znpV3m10E5H43RI_T4bX82qP2RgGAtQ7FFeL4eJtT3J_gkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی که گفته میشد خورخه ژسوس در پایان بازی‌امشب‌برابر دانمارک درباره کریس رونالدو خواهد گفت و از او بابت‌ این‌همه‌سال حضور دراین تیم تشکر خواهد کرد اما او از هر سوالی راجب‌ این فوق ستاره پرتغالی طفره میره و جوابی به خبرنگاران نمیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30851" target="_blank">📅 16:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30850">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDJCoT8phme450r4BaTuNCGpKlcJRzn3IwI02g9U9BAUINsjV-ky3nWgDKyUgzZXUxQQiV2n2ZrWHzWDRR0RTkefGQeDsxelxfvGy1hqFcW4MCfjzYXDvPKGibwhL1XHWW-p_xOyqhLUzL6wt5jWGwIRLa3STgWyXKsHA4fF3zxMp1SfayBaL5t7oaXujeEgPMadJ79hiyMxl_qrUCjLS392i7a9whfTCcS9kT5b322QPTOwKO2tZ_fuLgEk2eUkum26uA4eJjh9yfY4WKzxK-Pjj7S1WAOdwUdRhInCM5PUhnesd1c41rVqzhW2BZZ8ACwNnxtdTlJphb80UoWZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت‌ جدید ایلان‌ماسک:
اینستاگرام فقط واسه دختراست اگه‌پسرید بایداینستاگرامتون رو پاک کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30850" target="_blank">📅 16:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30849">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUVlufbfeYb_89oPlHzQc83zH5w7KARtHlC-Oh1onA5jEoYk_MS2CUtzozzTSA5keaZd3CWWqjO76ERPq1rPPiY4CvgUNBzZcWvfhVZ4UVQCQSYnkAG3MLHdcCY1zc91LY6fzqiosmruDOWoIydmnwUPdhyZbGRTyAo0GxbyTi71uJOtY-5T3rRfZBDOpQBupFXl9I_5aHDxVDxwMuO9_K_a2d39BtGzHhJKkDnJGViS18vOf1syP5Rjj3guLTu4WxoAVacBqWMvm2FfKzNsYH41vzWKtsHCLsQUrsa1P5J0QfucjwbIpubTBxKr5dOlm3Wp-FzKtTPKi6AlWyULPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30849" target="_blank">📅 15:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30848">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XecZ2PRSxQ_JbYnYCBCOJwz_lKAWrfpqsIO-Yv3XmzaFtHCXVsXUk6549YL7j21e3fGbg7KMd_K2XPSGIeKpHqEOhhL6aMBwRJeli7H6jX8UApozD2llPv1thS1EPFL9b7VmIsOysMqagASMK9PRkWo0cZhNBYTy0B1RY3nKnq5PH-djTjVTrC-f42Th9aW9AEkLAjU1XrsQzwt0NnXUj_0NLNcK4wdH4PvGHYZxNCVY8Kj0qtecU__wVYJdppb6JM_ANT78zwqr3k7za9oqeeXlkK-Ss67XgRjJJleWtuoygnI67S0pouoNn3VlUpU9Tjnn8cy4zxN-HPe_exc9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇭
روزنامه AS: باشگاه‌رئال‌مادرید گرگور کوبل دروازه‌بان 28 ساله تیم بورسیا دورتموند رو به ژوزه مورینیو برای جانشینی تیبو کورتوا پیشنهاد داده‌اند. درصورتیه ژوزه نظرش مثبت باشد فلورنتینو پرز با دروازه‌بان سوئیسی دورتموند قرارداد امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30848" target="_blank">📅 15:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30847">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdOX4qCHme_TRT-tkW8Rs6lRNMtYGCkw-NLSyuhFlKMgsJ9KJi6lHZVP2C9g78MPaI-0z5y2QR3qUow1HBW7UV9UJP-p25TAeyanKW2M4j5dgoupa4Lldlck1PWdiMAc4v6sIiq5a5Xw-_tByVnNSUQ6oqebWvEdF2JNEH0cIDBMyv9czS3VtUdv_W1zUh2M7y2yNo3SaCOIZIqVqLzVfcjoCNvR6FYGB20sj2fLbvahgnL-MjDzkLLqW4gYX3EbkFvUDJTy6oZbd1aVa3EReQ7NOWHtkPwramVV9OMBzIfrabhloIgI0pw0ckXNhmlaET1FfKcBj4sbsIkOWUqaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دانیال ایری مدافع‌میانی پرسپولیس به دلیل مصدومیت از ناحیه‌کشاله ران در بازی اخیر تیم ملی امید سه هفته دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30847" target="_blank">📅 15:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30846">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qj-q0W-2wfMj1K2Mkzu_gZ_wJtwPB9vaIUkHwr7mwHraH58nTtb6an4wC4MTs55iq-NfiAcY6xpdhudK5oYHMYt7__ZTeQJk9nnQyqJZg1KEFIVReE83fHE0Y2oJp9VPUEUH4Tl-QoeCIdBvvmCDzvi4SASl85PySn6XoNRyXaDX2ghNvo07iPKE-r_DKyFbX_GLbDb94ceDs9ReMHChrHgU2ebx_IBSKMWsbxCTtmC61Rit07CDviyk9Knrp94L1AgfU8fBqGAb8FdlFay-Aa3MZ3h6D4jNz2d2U4Fy-a8hlVb2qxgC8YKPsQoLLdFUlBTRd1Rb4QOkPSAGjj-eBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو: پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم.…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30846" target="_blank">📅 14:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30845">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1505PCgDJdpE3YmhIGi6UoyoiOZx3iXAabUw9ihzz97zZPWs0noRiFtrjVEGI3uM2Sx6OtgR__5C67EqtisNF57d_zlv20XRd6Ls-I_7Lx0nSLCeuviBTYD8gW0pNlYsSgVHSEjtx0c009U7S_mL8JQGsSXAn9BStg3W8MVLTBKLPy0bw8hLNkzZ3tUstk-yMUwf8KQ1vZAlJRyYhItgSVzo5M0JvGGq_2wQ1JdKBLfNtvd3n740urj73-P0pkPA1STw-F9opEmBfKzBLl7sjYY0OKGXsS-K_hUSauBB37_DIoRZ6xNObmTH9gh4pv4RIMLOBJ6YsNGlTv9NrC51A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه پرسپولیس؛ دانیال ایری مدافع جوان سرخ‌ها در اردوی تیم امید دچار مصدومیت از ناحیه کشاله ران شده و چند هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30845" target="_blank">📅 14:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30844">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=h0Ee-nn8DwhKPLlYeSscdihmKE6tekRWRO2fcY5fuPmMqr5Tt1YTz3btYf-9H0Kybl8ZbQ4kmVwpmnmvhyu9TeB2_DlWY0JpHeBmSi_X1cDd8nW8uMKEGCYiS0eN-k32B47AL8RAhlAPElSyr4BSKV9iHPESJO_Bf12Kg3auWE6GKTbthyuFfaL9EHU0L8M1X2W64GdR1duPsDn1GoH4jHLW5u6_hMcE0LGs3mGLSWr31xse0NJKQcjHXg-buEAkOsYi_EPin28RlIX7OzR8egmCMmiZ7ilTG72-zxNliCoIBuMUIiIns7BvNLBBsRFzrpSAKDPT2JVkEdCTNqjzFxANZ7ncIFcBND2jiqsF6Nj75tzfJK6sST4CNmfjdQg1sUzMGEWz2r21xfluSeTjeZR3stGe79Jks65A7OEhn5Lwi5FB6Vd82TSdAyZnPdvw_78VCFltpJO_FfydVbfvqwtnMZAz6tRnyCetqrDwb9Y9o19_-T5quyB3LIrQcmTYSxLVMlXViDGZh4PoCeo3BLAbfz-Naocsa5GLwIX3LjQYsiBgJ4DTpG_pWRzgWjOMxkQ2avun6XRXN1nHPf07w_NIMO8zPkGNJ_cS4gAY6xDoFz712thptduVgvN5p2kRhT66EO2sy9C28U-PeTg_o-vpOiT8HteS8b3Rq2BRTsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=h0Ee-nn8DwhKPLlYeSscdihmKE6tekRWRO2fcY5fuPmMqr5Tt1YTz3btYf-9H0Kybl8ZbQ4kmVwpmnmvhyu9TeB2_DlWY0JpHeBmSi_X1cDd8nW8uMKEGCYiS0eN-k32B47AL8RAhlAPElSyr4BSKV9iHPESJO_Bf12Kg3auWE6GKTbthyuFfaL9EHU0L8M1X2W64GdR1duPsDn1GoH4jHLW5u6_hMcE0LGs3mGLSWr31xse0NJKQcjHXg-buEAkOsYi_EPin28RlIX7OzR8egmCMmiZ7ilTG72-zxNliCoIBuMUIiIns7BvNLBBsRFzrpSAKDPT2JVkEdCTNqjzFxANZ7ncIFcBND2jiqsF6Nj75tzfJK6sST4CNmfjdQg1sUzMGEWz2r21xfluSeTjeZR3stGe79Jks65A7OEhn5Lwi5FB6Vd82TSdAyZnPdvw_78VCFltpJO_FfydVbfvqwtnMZAz6tRnyCetqrDwb9Y9o19_-T5quyB3LIrQcmTYSxLVMlXViDGZh4PoCeo3BLAbfz-Naocsa5GLwIX3LjQYsiBgJ4DTpG_pWRzgWjOMxkQ2avun6XRXN1nHPf07w_NIMO8zPkGNJ_cS4gAY6xDoFz712thptduVgvN5p2kRhT66EO2sy9C28U-PeTg_o-vpOiT8HteS8b3Rq2BRTsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30844" target="_blank">📅 14:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30843">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTgd9jULLgqY0b511WKQL_-4UJebapuVt7Xapzi3AsD3JtMrbH1ri7r88kaf_-ynRNPUuVLu4SoqwIkCkFUEXBRD10FLBIW-fMEqk1YqGuJF2ToAL8eP4dsGMILitEduGoNCyzKFBwvTakBHvvfDuwk04RqlDyImpXMApa_SLC1WIymDKvcgnXbo77qN7A3VFV72rrQ8BEpbPChLuyRhFNDHp3RVKGLvp23BMjJt1E0X2rlMcG2dDugS4dNMv_rZeh3DUdRUmepfBE_NLt2kFuEl3TFm4uw7xH9UchUCgE2OHJXTZ-JnppOaNw44WJm4JCGtI11b9WLMFPMT5sIvhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نرخ‌امروزمدل‌های‌مختلف‌ کنسول پلی‌استیشن 5؛ قیمت PS5 Pro درعرض‌تنها کمتر از یک سال از 40 میلیون تومان به 315 میلیون تومان ناقابل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30843" target="_blank">📅 13:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30842">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9S1rbHyNz8xLvITFiF9feUG_LFZx1_YyPyt5qae0cIDZGGszpUebN9qZkeB1aVcObTYvuU-1g3liiReJ71CPP5xAuaRihtZJRtAL0Nw1vFF08JsKuuXkJ2FJ0zxqp4_qQ-jVLk5QP05NSVhvLS9GSIn9EO3-mXVuTuju-V8_Y91tXd3fp9xAi-pXgjZA5dVevhwz3f7XrWJTJc2EIPrVstjVVRGAqThisXU5XZKGkbomaGI08YbRGYDfp0HDWWRKY-IPM7i_qlgFavbMXUYZjksHnf93aGWul0ZoEzVxRoVj5-58imc87lwUNma9dqGfF6NAyvbTkoPEiiItwwQDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو:
پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم. از این پیروزی خوشحالم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30842" target="_blank">📅 13:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30841">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwgjuRp9wgAbhk4jYmxv8ekJdY9g2MkJLD4_SFG_awxosDfmzYjnMX4qD6U5lREHG5m7yTTYRmqX5OJEZUbKSYfHgRqrlxZXyty1_cvAeOLMUme8lURcd95_RqTqLYc3xh7RtThOUX9UKUK48VGSDRp_Z8O82upEVeiqNAzHjzfM_a36_qEG0_URZYxpE_0onOSbKVg_72ZqvrfamhM-IuJY4budbg-svwMP4lOtoa7rZVXc-jJ1_pPQnB-C3A4pht9OzcHDyqoYbDUaxf9ECf8WdKW6kJXvOJUGfmt9jEDWUcwAXB9CSvHfw0FDjanQMQ4PRhgI9iWMZi2ctJfBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین‌شماره‌هفت،هشت، نُه و ده تاریخ مستطیل سبز با اختلاف بسیار زیاد این چهار نفر هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30841" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30840">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lliYCqslYjPeIpvlIOj072se7MKNXOnQ1pxjbUCyx86-pF81LZN68v6pNu9VsHKsHFSL4N5OPh_2RC66fRIlzu1gDJNDgzftAsLacWe4tVGLjtjktmOrol-uGiJazgKaFiM6KMh50mXUTt0hKUgvKZjI4Qy98oKK5xgfYrGLENp370TaQfeW2WpKGT-RaV0PE2sqYUYe_GA-YVbxxmFEy-V1ufHIvYlP5Llnb5pMUOE2XXPpBPvE7mjUXN0s_oLS8fEUypHeGrUs2zrBwpNnB8sN_xCBaIa2ADR8v6-ovWSR3DZ116_lijaM-wcp1Z-7eEUGt_N7k6t0P7hBh-M9NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات لیونل مسی، کریم بنزما، نیمار جونیور، کیلیان امباپه و وینیسیوس جونیور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30840" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30838">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgkwfGD2_fn6x5ea6JgL2LJFCPyGsM6z-xmFTQ_TsW9idECKQE5oNZe082uHcFupICM1gibkODmrlXB3ccuSEkx0qWP57aKMT3hKVaKB3ps9wSbnYIMz8Q7gZ_3k7FW24cfIKf6NgliTl4N_cnewbJXYTpuSf1kf5VBwN4E2m4nv6O3gmgYFRrpyswnnUQCBG-LFDadvtCMGtuT1yQeQx1gh2008JMRCyh0xfgOWcmFBdl_Mpj8o5Bl4mqV9cpXfH1LcU8DQ0Q3SQ9tXnXLoFq9S-gAIrdubMP3uM3VznNAuLrRTqOoQZPSTNapgwyqEB0g2Ny7e-QBp9vhPzscNEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه بیلد: سران بایرن مونیخ از موندن مایکل اولیسه دراین تیم مطمئن نیستن به همین خاطر دارن تلاش میکنن که فلورین ویرتز ستاره آلمانی لیورپول رو جذب کنند و جانشین اولیسه در این تیم بکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30838" target="_blank">📅 12:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30837">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMVvD8Ht3_QWtQjD2naXHP1qHTcgXTM-HwqPh185mMf-Fdqn9C-7kfVS2KSGdGXw7Kfuu2KH7sLa1SXlzgvd1AmIfGRpwTLoTZTCsospdyQjUCvbAjfTLf-RvZlh6epK10kgrUF8aW4FAiIxbH5rzlMYZx38g3K8UY6OerGl7XliSCX4_PWPexH2_m_syzjEDNRip-JNOCtY_cwGOng14Flg1x-s4qGspaxBqbE_NKhjD1P3KMAGa2-V-mtj8X6foFIeh6tkgU5sY10VYCkz0l5X4bb1b7-9UYzU05UTeEOTPMUlB71o87X8NkMsp_N0y2EOWEpr_msHHQ3LFP_uWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30837" target="_blank">📅 12:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30836">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=NqTTYVB3DP-ZeUeDe6gMUsOSd--2YjLYD9A-2j0eZs_uy50VV6bErhhD2WH5iHEGojR_mDBLS6ovrRGlCotZL4gFPQgRdHAvDjgxyEu_RDAno6_EFGf8BcOJAttR3hPeEwck9QIWFPP4X0IwIpHCF8uJB7scqlaPfNxMiu2G7TZLQjkzOoyT06ERrNIfaw_abrp5Zcxxrab29hinUIMDqeHTRX7QhK2-oSYsUH1_2-WyNkT2xP5Kvy4oIcvdDEWaBL5VzfLl9co9Rj_M3LboaDJC2gf3FWoaoJxtgjFrL3Zpf4J-qckILDcN899v68DKbqTeWGXJuhAG2GiBpepI6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=NqTTYVB3DP-ZeUeDe6gMUsOSd--2YjLYD9A-2j0eZs_uy50VV6bErhhD2WH5iHEGojR_mDBLS6ovrRGlCotZL4gFPQgRdHAvDjgxyEu_RDAno6_EFGf8BcOJAttR3hPeEwck9QIWFPP4X0IwIpHCF8uJB7scqlaPfNxMiu2G7TZLQjkzOoyT06ERrNIfaw_abrp5Zcxxrab29hinUIMDqeHTRX7QhK2-oSYsUH1_2-WyNkT2xP5Kvy4oIcvdDEWaBL5VzfLl9co9Rj_M3LboaDJC2gf3FWoaoJxtgjFrL3Zpf4J-qckILDcN899v68DKbqTeWGXJuhAG2GiBpepI6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طوریکه‌قراره‌علیرضابیرانوند دروازه‌بان ملی پوش تراکتور بعداز اتمام‌معافیت‌اش به خدمت سربازی بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30836" target="_blank">📅 11:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30835">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/30835" target="_blank">📅 11:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30834">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=kqlvfP9XHPgitEWmDwShv6cInjZm_ubN6ysYDGDPqbQcay5_xLsJPrNScXqao0WzeGzRo-qJ9WG7zqI0ZGAvZlTzdjROnVqKZlV4A7OoDuLwddHB4PteBFPbeqmHSo3Z32rTwbV5Nx95yxyx_K5ovt4thJUAAqN3PP05t3FLlRk0ITfiCyaadZ3oc-lcaufkpxvUoXsgarwTw1NdxODheVMpHL5tpad7vvH_q10oO727UH4FkoErI21LhpNhHOthf87Jwr8Ifu7PxKBLV99rdco3ZxV_k-y4wf1I8kpml14x20m7WEYS7rG1a2F1x2dcw0sQa8pkaVm_KYKsIPL6zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=kqlvfP9XHPgitEWmDwShv6cInjZm_ubN6ysYDGDPqbQcay5_xLsJPrNScXqao0WzeGzRo-qJ9WG7zqI0ZGAvZlTzdjROnVqKZlV4A7OoDuLwddHB4PteBFPbeqmHSo3Z32rTwbV5Nx95yxyx_K5ovt4thJUAAqN3PP05t3FLlRk0ITfiCyaadZ3oc-lcaufkpxvUoXsgarwTw1NdxODheVMpHL5tpad7vvH_q10oO727UH4FkoErI21LhpNhHOthf87Jwr8Ifu7PxKBLV99rdco3ZxV_k-y4wf1I8kpml14x20m7WEYS7rG1a2F1x2dcw0sQa8pkaVm_KYKsIPL6zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30834" target="_blank">📅 10:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30833">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqX7Hp3iGnlu57ATGq0LaYlv9fDOBlp-X8DaaVwe7XWT9poRtyThQ-M20uaSNnyDjf2PUdW-YrUpbCL98dWo6W9VWQfsMXPMCGHMXFk6DCtLCMrnYE6ifkxaM30Jp-L0u-7vm9LsBcM6129RIcBHk5OET5-V4DMHw8nPtBB57hUkyLW0QgbDW2tBPJZEOFPO-dsjcVJ1ztQ6JYVmUhXId22Wwdcij8UAfpbIYhm96w_teuBKx9ARyH8fRHiPEO_qpOtEbNrZ_qmY-NMSuuKbuRU2kV9AffxNrYhU98g0ek8NtgpamDXR7i_Rfi3yudAjUe3Hc5d9hl5F2HIxLwP3xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
👤
#تکمیلی؛ مدیرعامل باشگاه ماخاچ قلعه روسیه رسما مبلغ فروش محمد جواد حسین نژاد در نیم‌فصل رو به رسانه‌ها اعلام کرد: یک میلیون دلار با 15 درصد از انتقال بعدی محمد جواد حسین نژاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30833" target="_blank">📅 09:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30831">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPXf7N3MlQO60Wb3HoIYw74niCLBFrEy50aDrs5pfPlDP5G9rL70amePW7Uyv5fjFdi4OBPv3bgD-o4EJmb8GvfhuS1Z7u_JRTWJIqpLyBKAzuo1ghJHFtMYNSzATuUXeAbHhBgWL-tL5H50R8YWrKluQv1p60Bx9sP1iNM61NwxtkXm28Zq1WYuhLKzR7brVItOVqsdRxQ3pAvsnlmLUmpvfoCSCzhsDxnOaWzZauBxBAZO7tWqy334tFdWsmnHbmiRLo_Vc7QyNDoPOwq9lpMQpDJrloZK74aypFm0x233If1eWpAnjdl5TH-dx7N02jj7UmCSsXH5IvcpeiFxw-f4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPXf7N3MlQO60Wb3HoIYw74niCLBFrEy50aDrs5pfPlDP5G9rL70amePW7Uyv5fjFdi4OBPv3bgD-o4EJmb8GvfhuS1Z7u_JRTWJIqpLyBKAzuo1ghJHFtMYNSzATuUXeAbHhBgWL-tL5H50R8YWrKluQv1p60Bx9sP1iNM61NwxtkXm28Zq1WYuhLKzR7brVItOVqsdRxQ3pAvsnlmLUmpvfoCSCzhsDxnOaWzZauBxBAZO7tWqy334tFdWsmnHbmiRLo_Vc7QyNDoPOwq9lpMQpDJrloZK74aypFm0x233If1eWpAnjdl5TH-dx7N02jj7UmCSsXH5IvcpeiFxw-f4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/30831" target="_blank">📅 09:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30830">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_3oApWQHKqwMSlVL8K5jOLYlKvNcpNpT3ddgCB07iSNxQ5sJJ4DwThanENQgviIO2cTjhnqrchi9CkPBV62VJKwXLlUd_xdPYEeyn8Gp1h4GXlkGlFuuQAM1UGSXUJBaclQUo821CZXzMGVmge3bJjRlaF8ycLNgoCt3Q-ZfYiWlCVM-lInleeU8lvKpg6ucwvhC6JVQ8bUvxFgKSggoz8TYXpRdSBD_aXu-9chzasD8RH_pEA0Ody6t049i-j6W36qY44fiXbh_E9jwS1K3KZ4kFdZg7Coacwed2XuqMG21790WxA2pQ77tobsCUHoLmpvNqYmO9gI5Tbtnakzww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/30830" target="_blank">📅 09:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30829">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGKGq2X8KnszZ0poPC1Ozbvz1EdGcfy7vvgMNKEAEbqZnfeOwSrPTzmwsPS7yR5fXIuNHczAKMYF-gfyEWyPneOPDmG36MuPErkUZnKDkqMU78tH7ADZEfMRNzvTMzo0fgGRB_nGKood2I34iDiDHQEWl85EuwHlBVXZQ30fE4R-0HVJll_W8_2R0RNkrnQvbKoNVuTiFpbcbIDQFpRaOEkbto-1rgaSy2NweQxl7urmUb_Ri1hIAGEhIovMQxODXjV3lPT6x_HiDnVFrb1VI0hpMpRGNViAC43vRTbqmOgK_me5QxDGp4u1_2-MfBmDqUSTs9DBVZDu338uaf1Onw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌خورخه‌ژسوس‌سرمربی‌تیم‌ملی پرتغال؛ کریس رونالدو فوق ستاره 41 ساله این تیم در بازی فردا شب مقابل دانمارک بازی نخواهد کرد. ژسوس اعلام کرد مشکلی با کریستیانو رونالدو نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/30829" target="_blank">📅 01:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30827">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2t516-mCiBvXW9EQHwyq9K_JuzWxbFGHrtGS8gdYrQ7sthNaupW9XvGgU8YJfTcPSlGw6r6VuocvuFcbCcrwqkrbjuhSaOQCBCsSN_U8qhaA1v78Vrm63nx54xVcc6TnmwfM8rSheQvLKpLJaFculycRaROqZM7pgXgjBHT8m9rjtV0wECIKA2jGRRifx9QYavaExJgk-vRJSZ7425aS81vBb0h9z1sZQt52Y3Qy9OSknFQASyNM3LNjOdnz62fY5HJgZ7QG-cgGrhehLyEhxwI5RMPWFJeH8H5vk4WhDA8wmc50ObxTkaQ0yPTihXa94oAa0MyQq6ew7bwVqnNVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/30827" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30826">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InAffDjyS9xWAfsBlgixg5lmdibaU0xlLqsjVrfI2aGjg8WEiMrA6slE9lZ6v4O4d70TEV5car61sTcVzf8IIJgGKuQOF9Z2cOKIUtf7YgSL2zJ6m3UULJrh68GEUbpe0buJekNnLqWA7oGMUGlOLHA_YwRBao8IBOFrs7OHlHudPb27qwjG_z_WzMHyXWD95dN9GGXH0EhW-TLF53uA88TEbQe16GARMVbP7ro7bl2A9keodXTctuQo5Gw7h2uZenMv8KdEz_ZvjyALas0r9_bbf6A2d1jHZdTHovKb3fq3iBS3YOFzL-zy7M7d0J74JMaE-g3Aa7H6TV68rwQTCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
از اولین طعم برد ژرمن‌ها باکلوپ تا سومین برد پیاپی شاگردان ژرژ ژسوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30826" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30824">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzS_PMtOjDPN31RssY-OT8j4I6FcY_tx_XhIoDrdgvA-b3-ZcpTZ2eX82e6RK-t2I5uv6wESEr4WfowzBNRk4cdl7m2u5w6OJc6iG4eSp-Q5zXdtDC0Y5m85yheSbKebdOGqDUxoRIJWc3l_qrRP-OM7ahfz4xANVY1EY7mnnq6VQH8VFg0cSl8uw_IR4w52wjrWDtHpHcLMlID4gRJXO0w_2w7DV7Z0BNxBrNcAFlXQPzBGArZXRTurQeRhphyzriXN4XfTbENjLRX5skj8_K_Tzz-isB5W4Rml6YgjIJIg8A9RDKdMZf_8MND54oPPCIZsIcpRzTHmQ_91YD6-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رکورداران بیشترین تعداد گل زده در بازی‌ های ملی؛ کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30824" target="_blank">📅 00:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30823">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUjzoggiEQ8wbssgKmaT3vDjsO6RDDvmLSeELT54Y6HzUM5aO5WxAVmbFDIZ8J3t3IkfUb3m-Mlw7vKhgP6fuQm9ZdbcERWzFxxzrU1UutjBwiCKfKFpyxHYTCODKO8Pecb605Q5XN9-jZXqZaMoNHo7xybFGrTNVFXTOQE7syJEZq_J4E5x-fmk7OaIHZ54BGP2VyoyxD9fEqADlfwdtD1P6jVL8h8l8vCD_e5wuqTez8vfeCbINntJrPSt2w-NHDv-XqLWU7CGmf_eKEeZwBM7cY0FvfhYSSXS1DmJ9YdW2OQd5Mogm0WXm0dw-WbmDqQXqEvh0kPawHtGJKtfpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ابوالفضل رزاق‌پور و یوسف مزرعه دو ستاره 29 و 21 ساله تیم فولاد خوزستان به احتمال قریب به یقین در پنجره نیم‌فصل به ترتیب راهی دو باشگاه پرسپولیس و استقلال خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30823" target="_blank">📅 00:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30822">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kE7fWchzgb1dhtv4ntY9yFbKkW_60I-Fjgpt4ra6yKE6Gnii3OXMoj9LELmmUR76Vs0VsDqGEFTaTukQ0nFfHNb4s7vCNJwxmsa2JXEqSzmZTLBqUGd583i1s2EP_Ga6ERX9IM9q70GZMEjHiGQHd3YVZWDcqSKIUaDetfu45HsSBgborj1yf4_-Kcp2P8J0kBKeHVmTDnII0GxZKYfc7PXXs2-7BkyalJQn_E2dKz__W_V0ipp-dLhcEqrrbXJ9CcPQNnoBmH1Infd4SVe139qTG8tYkCKzfFCxelmRD9pWM75wqPOMexuoQGQCDOemElDl82Y2JG4UfJaByWJ1zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ برخلاف پیش فصل؛ حمید مطهری موافقتش رابافروش‌ابوالفضل رزاق پور به پرسپولیس در نیم‌فصل بادریافت 150 میلیارد تومان به مدیریت فولاد اعلام کرده. بدین ترتیب با پرداخت این رقم از سوی بانک شهر رزاق پور پرسپولیسی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30822" target="_blank">📅 23:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30821">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYa7FmKcsi3jaKdBuu0PR089_LK6BlUeKqn913xB0X12yU5soNbegnWE_n5Y91rk8LhJyzQWXhrYaZZcaJVPUUNhXLORnjR3Ss1t2YruXCC-nf9y0RQjJvqu58ho8d6KfKOr3mdzaxce_qWtVO2vo8hfA32dH7MDiUINpDDEbgfHugifrIiOECOXk4MgizqPR8l3VW2v-MPIVZTzOcICxxMRv3jwBjd2uRV3Msf5-aH5wFaV14iLDrI06_6Rah6pJmfcsr1ztvWfSg2eDDcCQDhxHFXaK7PYThw3Sd7AgB1MZi0EqZHYldY3MkxNdapJWlLRv8C-C8JRo2WLV1sPeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30821" target="_blank">📅 23:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30820">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeY3H6Tlq-AQ4EU1K1j8oEuK5e5EVe5inSjUo4ZwcVAnJ2hy9i5U6OpfWAtse1fPeNqAGmiynsh3HV5Fk7hLUR7Knq5ss84oImyGnUxB8ISiwHQ8n9KlZsx9TXYebxy1ksSV5Flccds9LQf_fZoTX65tJUgXjWmAlKS4x7bU8lOFqI7Rz6D4rryA8p5OnKNnAfhDEGzlKZ71bgFolDd8dR7aoXTAeabTgpX3jbVUmUWsTkrbQTKRy31L9JcNFCzSvBKnpYwQgwYtsD3dlBXWYix9edxYYs8ueJTRn4LJ4I4VfDL0q4F-snQ2IQa2dwILBGywrjynfBxDMGzC7-ugLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛طبق‌اخبار دریافتی پرشیانا؛ باشگاه استاندارد لیژ و دنیس اکرت برای جدایی توافقی در ژانویه به توافق‌رسیده‌اند و این بازیکن درنیم‌فصل به احتمال‌فراوان بعنوان بازیکن آزاد به لیگ برتر خواهد آمد. استقلال مقصد احتمالی این بازیکن خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30820" target="_blank">📅 23:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30819">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi80y7V8rijhdURU35T2cZEEqU7eDzje65Mky7UsrbvTO6PNa-Epwj5ZVx7tdHdI3yLW9AqIN_NsNvDT85CxxGZ-nr3PGIfyTgl8kuQ8BZAmcfLPms8xnVFHIi4HXFWPP8-Desk7bn9CusWxjBszCR2h3ID0YgumKHmMpOwxT2SI1It8Xof54-5j8-ajy47p5KLpbTah7ASbmh4SfUQ35tWQGFsDq2Pufc_-y3Sbcvl3gXqpUpKAdET0mHG3IKPwnsGGe7J0W-a1YjI_vkAgAmv73-Ma_RfYsBmRini9UOZE8cgqH9dZD2JM6ey9fzkcqpTnuQZZmu2clgu2y5upbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30819" target="_blank">📅 22:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30818">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RT2YSaxJ1hMChP7C6W4FCSBG_Iy7UsZP6V8d7M-Gq1KJqc9bi-G3qi2k1MdmHskrgtpahrNCN6DKW-ZtOIdxSC5_oFfF9RDTpDde3YKFNk1BoAr13NzeRyssK3pUJz6ZSxeEbP2kCwWWAGStrkD_JI8Q54rnQQWwnOvSH-QA_AfXBh_4vj5E6PikvYCHbuObrZVxp6bTjOMAVQpeC92Qd3muw2JAXcunBC20DOUuQUnTt4vqYB8-v-HE-QDoK1FaX5kdtF_JfmIaXCaT1DH_teQl7nyyczJicfuzng9zO2cvRQfhXa_gl3Lw5UlZDa_vyfCk5XbvmaKNecok3-9d7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک 146 گل کریس رونالدو در بازی‌های ملی برای تیم‌ ملی پرتغال به همراه تیم‌های ملی که بیشترین‌تعدادگل‌رو ازCR7دریافت کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30818" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30817">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukTSql-fHJgqRSqWNRdN2cQG_9emkwg9_fnfBfIKY32XLj96UNy5L3KT4ED-n-gZ7AHqLl63aYLfo7HVyB5ckUGa0R1f4Fs3fWZOLPJH8YXz6jdliZyVMHIpVFPejrSTz5GMzXS_PmHiKvVS7Vq7UpFmzJEOLI_3ElSCDbLXzrz7qPnHssb2kXMUQ3BT2olly753rrpq7NrK59Y97kx1D1f8ySlUCU8JEAZYqY2I8uBK-mFa4LVi1brM6UC4UVp-T0o7hlJI5AJpJclPeu0kuFe_lMIIxCXzyVZODDsgSwO-3Sxb5RfBUNlqrtU0AWwHsRc3tmibn1_4BQUle32NFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رکوردزنی‌تاریخی‌حاج‌صفی!احسان حاج‌صفی با حضور مقابل روسیه به ۱۵۰ بازی ملی رسید و با عبور از رکورد نکونام، به رکورددار بازی ملی تبدیل شد.
‼️
جالبه بدونید اصلی‌ ترین دلیل دعوت حاج صفی توسط قلعه نویی؛ این‌بودکه احسان رکورد بیشترین تعداد بازی علی آقا دایی و جواد…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30817" target="_blank">📅 22:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30816">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prw9ltcXtxfMnKGLl8SQWSi3X6tmDJjTsgqyi4RW16q091PW_yxZ9leHjztrk0qB6qlmEHHxiMZAf5jYCVYEtJTaFLyvExaGrO0gO_v5IvhdX6tQlArpD4ZvjF7pGgbHq80y3lsUBZlAR_lBXpIyGKCU8_gA6ebAtPQbA_lzwl4H1qIUtOz4Z9MRteStGOtBwCrO39mEn2_dloYJgXD_ZjPKtEPFlQJEqjFKePSfjDVFoYIzm57YEgXD1INCTrFaU713I6HM_RpqnJHxwvO9iBhpSDhTLh__KmX1Al08ydW6v3b1J6iMR9N8DHGJOqyPeRV3TEcgHHBkAHm62_dj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جنجالی و عجیب و غریب حسم روشن درخصوص ریکاردو ساپینتو و کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30816" target="_blank">📅 21:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30815">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veqrcPjI2X1OL7rHlVfLFwkQRXr9j8wxCDgWgY_t2zMNK9hfkZ_MgTYScKeflO3tJLbcUeBmFJxbH7IhSMvDinEQLP__OKw17AHZtisHhA_P62h4COpYYHkaMkwQiWr24wmDeJ2c4de0Def0PH49Hf0ghIQ5qafZiYpap8BE_57z_yrV6Nb__WTzmBuPIL7_2IPvhUga_G09oH-HLRHiZc6aoyiDiHAs34gQi4WAKKnwJug0J9sW20WQEe06WXcjv4W_C73QjO05pTXpSISm0TuO7Nyj_a8o_DoN8RvvVeuiXuQY9242Rsq30987LojsxB6Dlg4FHYQHitF-t-r2nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
در فاصله 48 ساعت بعد از خرید سهام باشگاه آلمریا اسپانیا توسط رونالدو تعداد فالورهای باشگاه رشد چشمگیری داشته و از 500K به 3M رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30815" target="_blank">📅 21:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30814">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfS5q5giu7yiVBZseRY4FyDU4eJb432zVLqaQv2x3zMMbsxRu5K-8zcdJLY1-ZeZJXc1LvooaGvkRJ4AbjAnZCSbo-C1r0Ms9sUEODxIxgsaf8T7fN5duwiQizYwygyAUHsbqxAKZShX1wmfDc-sORN7iOkxq_ZUzDBvza0GuNKoD0TWqJjDML6utFtGLtsLdnhEGoRxTMA3RJ_X9ZyqE2DARprDPPgxAvMI6W56iEFdNZou8rM_ppshUbhfFujs644MxqSEs8IEWlmAEJBvopYvdRAtmsOEI0S6l-XjBskTvjH8JevKHOdJfhuwjDYhgicgqzLFjUDnhQGGeDS95A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولیویه ژیرو:
روزی‌که من به میلان رسیدم زلاتان اومد پیشم و باهام‌دست و داد انتظار داشتم خوشامد بگه ولی نخستین‌جمله‌‌ای که گفت: خوشحالم اینجایی ولی شهر میلان یه پادشاه داره اونم منم فهمیدی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30814" target="_blank">📅 21:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30813">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93919f9336.mp4?token=molNT_Fjrc11dCY1BYPTTSpx4v2J7ge7twXsh3JQZgl_LSYRKUnystvREWR54URNpwKKEihuHbHxJBO2tRL71trgtaAdWm7VD-gchnxHcHZX9bP1bfXtzFJr2GTRocjA5nAQCekbIearHq8hHvuzZACYzNv6eRMgXxw_veHYv2qfrp4Mq1C2sL1_5FjTEJ0tbvdCkZuFDKh9P6_AUb93nToO70yUF5PcjRgdFx9wZ-qOkpT_1MZVCIGf7Uf_Z6xCAu21YFgYOxJBtMSO2dDoqz74MEIfErJYvufghwIKr3olek0Cit5Hymp5VEL3JA2VSy173J28-TO-H57XGATPXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93919f9336.mp4?token=molNT_Fjrc11dCY1BYPTTSpx4v2J7ge7twXsh3JQZgl_LSYRKUnystvREWR54URNpwKKEihuHbHxJBO2tRL71trgtaAdWm7VD-gchnxHcHZX9bP1bfXtzFJr2GTRocjA5nAQCekbIearHq8hHvuzZACYzNv6eRMgXxw_veHYv2qfrp4Mq1C2sL1_5FjTEJ0tbvdCkZuFDKh9P6_AUb93nToO70yUF5PcjRgdFx9wZ-qOkpT_1MZVCIGf7Uf_Z6xCAu21YFgYOxJBtMSO2dDoqz74MEIfErJYvufghwIKr3olek0Cit5Hymp5VEL3JA2VSy173J28-TO-H57XGATPXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌پسره‌امیرمحمد‌خواننده سنی نردن گوردوم رو بردن تلویزیون ترکیه تااینجااوکی. بهش میگن بخونه، اینم میخونه. اول همه تشویقش میکنن ولی آخرش بهش میخندن. پسر متوقف شو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30813" target="_blank">📅 20:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30811">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADeJNX-DjaN1FkeF-FVFrm323YIuxkgJ4E74f76zuWXCGvOiURcnNJq7FLJlIfFOYtYATTTiqkyMQX2izzZDY211CTNFIdwRtCFeNC32g0Q4ZgaKC90lOBv8f6JPHOhlv434j5Ee3Se96_uF99gcM5QzphwdE2t_4zmX0hphbK0MfetASfAqXvg6tn9W7jbCaOxszgjqGxrENDuZ_X5o72jSpAvSgRLvi_ictS_CQg2LW277vVV3fEZ9C07qMKqI2ZrneIePn8RDoCfBoH10MccpjrnqKmpzKTdDe7ieBefcwIIYeoJMrnJqq345Z4IdDJ_bdGIpXRwuWEHwSPE0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijFOvLqBl15NMTyy3giPxNPfp2PDgEMyycDi2Q9yYtIGcfrIoNu2yVoaMbdAKVZyWkVQIdCKbd6yEWZNrBLQHad9HmusddZRi4MQt2ed0W4nm2Ye1w55QwomJEH-4UBLjQ9yrhsguwGCJ4VB8NmOPqVPu2DOuq6OKKXK4oVJGnkHeZIspwds0mdXaEDAXpdYhzrlVrkYTvB-0rDue-Mq53WjLRCPV0BykUSwK5OKuRdB77j_6ERc6ZhaEMad0NT4LLY1Ehnif_lMywz0tPkV297PeKcmr7x3iBmZ-1S5qrJCCTwL1V_Q6XNERiog2zdiFyYKmd3wSnmP8HKx0_k6qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30811" target="_blank">📅 20:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30810">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubbNCeOvnfTEetYnxq6Cgqaqa-xEQq0dZlCHzi09satzrJXnBluZVqbRBo5MsqrH4rNf31vryvbzpyIlvDreU41pihHNdeXB7fjGmLO9MXimdR0XK_j0FkCgoWoBasTBIaRMng2t6lJz5qSUhAG_uNkaxJvBgvwjViRUux30HGYDRJWO53_nivR35suvAglB34UZULmjvGlflkfrXT6GyYUOQyKI4sldI1L-SFz_ryZSW6Z5KX_v71A6zg0vMIOxvVQDYqzJMfaxOMb95SAxu1dNCp06FZqHs_HGWuDS7Rtsh17cyGkwUbGb0g_K3K_ulaP1tURdtpVSswTHckiUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال ستاره 19 ساله تیم ملی اسپانیا که شب‌گذشته‌نمایش‌درخشانی مقابل انگلیس بعنوان بهترین‌بازیکن‌هفته‌اول لیگ‌ملت‌های‌اروپا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30810" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30809">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ5WhnAHbDkU8sQwHQKtnPptcjm8MGBBI-6pJczqvM-x8EjyJuisZBebCMmMPXkrZRsC_SSH2VwG16NavhMcH47JZxA39I5q9CSOLJPGFdV9k7XGVKicUEbH1OMcen-aYys5qnZQbl2Vwpumyp8k7IwvX4F_LGm8hyp-kA5viGDuZBSu1aYn82nCOVw_znzaCXTkPwp9ryvXXWofqAGd_Mf-d9J9ZQ9gtcrHU0vTBeH0EoS_wtVGRu0fOQKqIRLxTse6cgiMerNJaXgQSHFV3FzITGvME4azgdMVz3kfnBSkk6WSihcXfUxKyme15B4UfgrF8gNGco2JkCUUo9X_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
نگاهی به‌شماره هفت‌های تیم ملی پرتغال از سال 2002 تاکنون؛ رافائل لیائو وارث جدید شماره CR7.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30809" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30808">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐇𝐚𝐉 | 𝐅𝐢𝐱𝐞𝐝</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czKtcd1KpsrVG12i5m8wpYk3EqS8M0nuKJ2HJt-wB0DDa0yRePb17Ikc3LEzDnLY4eiAjiLTAmaaZU7810mTG5Y2KGduJ0zjWyqgJy5wVD-LP0DkTqoLC_QG5308dJhpRrnkx7TSscDJdS7j6tN83h3BxRnNhpFXe6ReHAlv75nR8sqrl-D85GoSluor6n0Sq2vhkiyt2IUX-Br72T5DEu0HjV89tTLkG2jSaev08w4QwuCFXoKQLZPDRBrmmnP37rn6nTdlTncx2QqHVIDu5tJF311YPm0HCJPO2CIxVeQJjrZRKjJZVrD3JdGah7jQa8tA48Jr3UTDW45dWMYUTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30808" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30807">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMj8DqgqXnDRFzbHs6vZLtLzeG0xZDVVy1agEJ3zz3TmZBwmru--jguvobrzfAbZxQdALt9PqhOckoxLD3TVxtYHe2sm0fUudJzH_GiVf__W1WoVBmuZVPmRUb2PA42VhiU5fbBxkRhE-fhQMgrH3ivLz039YkSEGxXqslCOb1fiBXPGz2WKHvLUgUFqAE6OYygbH6kXrxpWaje_7Jkp0qztc5mJDxlDJZ6dsi5p5arXynhd4BgwMOsdfwsCvLY0fyFzyY0CnZrvSXqk7mklBzgSsuL-5JN5UzTF8H5L7DxGXkcfwl4WNY0puEsx6Ox_JXz2eHsAnRrRMV7TX908Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥈
نقره‌سنگ‌‌نوردی‌ناگویا بر گردن رضا علیپور؛ رضا علیپور در فینال فوق العاده حساس سنگ‌ نوردی بازی‌ های آسیایی ۲۰۲۶ آیچی-ناگویا با ثبت زمان ۵.۳۶ به مدال نقره بازی‌های آسیایی ناگویا دست یافت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30807" target="_blank">📅 19:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30806">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwDr2wfAcMx20FrQZ7RON-9KaShqHksKPR6FspAaQlrF4lo_xh7wLV1gvRpREgIb1jprSB_4MFsYRUtixJtBJZeeMdzCzVHVeXFa0xFhB8S2MWw7Z3RsZCNoRI0uVNsY4zkwOlW5L_p4C-6a3VbSAE0TfWcm6UhPv-afswCeIVfY2ymZXFCfGTEvBPf_6fVBcDEdTf7_PSgjzl1JYeIsO9D14c3-eCueseKHOyDNG0b8MldC1xwV2LwPWmjsN3HD_K56hliEIOyYrkLqqvjofYirPUk40sjjOjFJJQ2IzmcGNMntnPzB-oWXD574UZn1ihy2GhT8DVkUInTHICyVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فران‌‌تورس‌‌ستاره26سالهPSG
: باخدافظی مسی و رونالدو خیلی ناراحت شدم، ولی طرفدارای فوتبال باید با خداحافظی بزرگان فوتبال کنار بیان چون یه روزی هم قراره من از دنیای فوتبال خدافظی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30806" target="_blank">📅 19:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30805">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5nD42YDhCtTYvwuEUFdSwYBZanD_oY5FMWxNfwfppD0_HZwqTv-11noA9q9hb0o0N0cGrXpFmNfyvRfZV1gp9FlDr_Pa0vNNp3b-59IBF8dXExB8eCn2UBN56g92_LdAM2Z24aWdQlChOy1gnSKLADaZc5LX1sQwGjiUJD-47bNkzNoAQPhw_7-eiEFMJYT4q1pLajw4XqZCxcLwdeZD8i-6-hUAt0C2vO-gevAK27MX1NYjnKjUs9fNQLBHlt2kwpOXJwGv56Isolv7C7vAV_1WGnaixRUvblp5P0WMohADSbetMywRKiIq8aUxgdc6dYHGCBwrQKER_spQ4-xVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30805" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30804">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx1xOX9AK4-5OQbJ_kMS_vxGx7y30uWE282E6GLt3hSKWBcnPJ-DWNrXncEe4DjZ-7JZ6tWC41xsnzRPWrnsPhuynQCaCIdpx_zPcFsiZ95-4hXUvNDKOF9PE1D_7uzHGJfbgSDuVRK8CbClGnSF_VndGo5YI_bQEf6W4MHxYo5o74BUhfJKiIgbp8cH77uLbYmHSHOYg9UxcbSCGiQCXa4OViXgrMzwaZsdGjJFSpTRYiB-0WjZvfRxO1Z6D8jrYqrtOOa6_-EMcLW04p8VDq-YRtCKNlpPTI9rg3-VK7b2GEzPt9g_5-m-7y1Lt4Aj-DJC61VFrDwaLpQKW-MpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30804" target="_blank">📅 18:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30803">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4QdRLLGSKe1H5-UGi-QwPvGgJVt0dQ4P8LocVlHncWfFnZesWudYMivkRaoFg0YJKzhMV8cQhqfWOWrJfhUYuWXG3Sme327V67Yd6mjHO-nIehU5PDUDD8c4GwGImpU_aJRhFmlmL3q32RX0S8CiAgJfLD9kjuHqA0Rh7Ocs4mIuouzrlkqAt7CD70iD_pYQOlcpeMGAgLokpaH0fCcnUdX8MhE9F6yFsElh7T0g_hQTV3d2FmfNzQ-eD9KqhNJJ40VLaRgt2OmD6t059HKTT6E35_GknwAq3_H-KFeHAn-PLC57DqbGPi3TUI0c9CJNRV5Ny_WOD33i3vTIOnrcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30803" target="_blank">📅 17:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30802">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJhjO0CyxHPVgFQINJEhbMLJNk5XeJk4MWXVAXhCxMR2CGkT0fW0kWJIyEcik_oqn6vIP54NGnx_fPbDPJO15vOTeiFHFaljB2a3I_uKVwwUIr6E3bSVVvcniOTnv_ua1r2JqZPTnBCfUCkt81KMJASY6PYWSVFlzu7ZpkTL-og2RyEc1dSqZVnT9TPDr5VVjSzgthT6ga8xBJ-FMTk4ymqwN8RZ9u5ABceQzVAH9Qoaqz-Oq3SzsXu-ZvDgrOTwrMcBeb5lq31f2M4mOxvU82JtvL-q9uCpB9Y_9PRT0UgtDJoj0nkdipZeoJxWIbT1dDxhZuBNg2I0t080P3kG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30802" target="_blank">📅 17:37 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
