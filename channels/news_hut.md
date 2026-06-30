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
<img src="https://cdn4.telesco.pe/file/FkoP_aIeIL4_-_inYPZro2KkX3opEAg21gfjMIaaHHMqWBonI0wH0NP7B1zMp9_tXARGNQLpQBLhpn8-vBOAwLZ1aGwwmFjStYdT7Ojt1pJias0tSQmw3qUZHuM6ax2iPaGj01C9cAX-3EdnCWYbkSH3AAoyKdgWRKdxJca61ijaFJtRyCvS83xET_e0hk0Jt_s4HmLIW99JH6RzpIrlJoF5KQM6TdfnzHjoUX5u7GqxpP8_E_ifu9k_w-Zv66zlX49xblAQJnVD_BxIABhHXMaUAvSxqSs77j0CHIjzii52kUIcOBZvE002_HJgdbEh8RIlT-NkM6M5WcmYOWfjEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 217K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 15:58:22</div>
<hr>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dahKW0wXjoBzb7IUGSl6dho8B8EINbXZ5cqTiluKu-RgEMCJgh4OtjX7EZnpfCjLPZVCrZkXjtbu6stT9hk70iQ-tLP07ME7ddplPCgkjCgekGydbLUSNzW2yv-rtRZ5LHPK13z9FwZVVT4XxVolhzWJ7pDct8Vx9IDSFuTiWDFM-e-JKYT1BxuYz0TL10vLyyGsWx76yedFUsmMV8i_IAxDjmykqGRzFUtvaDy_-vabsa6aj-4T0tQpL1pjhdPUo2Tu4cgtloCVDxyPboFHxc1Q7sBq0iyKV3fm-TtMgkZ1DfR0xFsMBofnlvI_e0fg10GcswhJxPg0zm_SZkmhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhdfZn1vh58UHrLm8lfZkD-_V63xgH9zFbwZcNC0IT3WwiMAY-AIJyX2Y1XjhYJiroY0hzg_ntpHK1FTJtZ91F4TlAV8ZGtTJEfeWRtuEbMKVa3LD_-TUgNWR3ZWb92l583-5eyQiCGxzAgLxhFbXhOD5Eg691yQBOd7PmA1Y0l-iUXJB4UPPVEon3AH83c5Ow9-bejISwD2ksN5yOTc1Y5TLtzt-pbm-xKeZlSm0mucpaAvVC9TuZNeCoyubLxQsEmqCEQqnyGLprpwq1bd_VEINLAhBBqfHL0gcG46ldTmNlkYn4OiptaqRUJ0QuYl-Mk3OBVoJ8x3uu59RG9Uew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=JDAf80GfVsqBGPCHQvvkoBPMrsQM2vVANTTcl5anBnyar9EW40HPCdd59eg6j7K4QTC3AQ5n5P2RsivFEgr0H5umkNy6TRLekCPfo1N69iB5tTxbwLNCa75W9AD4L__1Lws5_3UBzfnwQlFRJmH4Sx94k_RskQt2uC2709HyKRyEtHQwwRNA0rIas0eiWo9VcSukTP7awb7rnZY2CYWbT9iB8i55lf0YAI6HAOQ4xOKMzkjNECnwjgheQUiLWH-mxm78cftV5px0xCMllBZAOtAlWqKSkf6MYyLMZxt33f0BJhEu-f-8t21zsIE8IaCuqNcPxZ4z9UBdCkQn4TVt1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=JDAf80GfVsqBGPCHQvvkoBPMrsQM2vVANTTcl5anBnyar9EW40HPCdd59eg6j7K4QTC3AQ5n5P2RsivFEgr0H5umkNy6TRLekCPfo1N69iB5tTxbwLNCa75W9AD4L__1Lws5_3UBzfnwQlFRJmH4Sx94k_RskQt2uC2709HyKRyEtHQwwRNA0rIas0eiWo9VcSukTP7awb7rnZY2CYWbT9iB8i55lf0YAI6HAOQ4xOKMzkjNECnwjgheQUiLWH-mxm78cftV5px0xCMllBZAOtAlWqKSkf6MYyLMZxt33f0BJhEu-f-8t21zsIE8IaCuqNcPxZ4z9UBdCkQn4TVt1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0ogAm1VWZYxX8epuOvnSY3NOWIypcelOK-NJmhP_u0O7bEl7Wm1U5UWx5SnXR18g0jKUJMUu5NakQH8_sX2rVC26crNb3YjCUoqjRPz1QucG0bBSjFBtd5LBQhXUCcxcTTS6Dmt11vUAXY8x9vw9Yon6428QHN7GWsMRfPF8daBseiogJNJ7Q2zet8wReyLNin1-1DIvlayfTlcfZfAGq7ajW6Linn2SoCzPz4EVCTxx8qpBk4hMZbgTClTBJUTrGga3kjKwndpNj8mpFyI7AJbdc3UPjV2vWf1lBLIWYNT1IXVfz8O8rnQcKNGrCeSu8lNt0HqMSzDeTGZ94q-ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGjz_08JDImxL9NPtQQFdK44ksvR0v-G8W8I86TsP9zqZvNpJ3jYnm9ywi6MyeQQ3wftUjrBwnEaplhHDjDkepmS-SkFDIM8iB0-dZ8lvsVRjH4WNHLLrYWVUVwCwPzQG5A-tNX_UpBv1j76fZ6r2RWiSsG18_X5517l5NQYvDnc7fx9vp2aDgYl6n-Ya94w5BAZA9s68jshdrETwLCU58jAeyxsbL1WwPG67d2URLD-yrw19vM6Ax1jrlXmFoG9JBp4FdCGMKmWGnox1CZDGj7xhT4wFJvrpVfOWDCL2-XEZjNUzkqcN0ufQnCKcuZkge21QyyJz89WkE6vtZfMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfPZl_UIVpAaQwEYJwNw6-LzNC7GQT0JpRXMbRyEZl9d0Ivfwvo-iZrT06Cf26w-2eD0Fo1eZJKin2n31DO0jVyGZ3jRf8tk5Y-3d1nG6vy1V7r2udzCEUX_MUDfZoP8tX9Wz0oExpylTN4iB8H2UTNT_lTeFyMOvVQm3LFXmGlksTHyEIzdkFIOA8WRZBFdKaxjJmQm7yBgN6Ej6Ps0I_usympFlihZkS6Hx5UwTQ-U14NgCsygdIhQd83lPUNjalrZdl_fgDgtowD3do-FkKRYvMdcu-CbBsOjj1h2rgSYGguuT1Pxx2qn3dF8PeaP5sJ1QmQ0xRvK9tgPekTrFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQ33eMYPhGn7V2fuWMMMiNHHEi2Mvf17pCsqmpS-JrVq3YhhP_FnjvMdKncYXdR_79Zh3GMbKxlRbLoDxPuSDsnRQ1ZtNby0gmRQyWNmujc8aOZhZRLWvFrzUkR1IgeKmDKZIIMRIn-mawufUAT-jPsDYIKLkuqfiEqAyX4YSWxKb5--4vihMcCwndeRO84dkfC5oZwatpapIZRmjqHPMgHAnExdJRoGzIN1zzwxTYqi4dQeyG72GTGwtr7KhsvKTlTI7xbOVCYTA7Nf-ewjiEazOTvl4FhvEGXkTfRa2UzFnfZJV0tPDt5G-cAhBaw69Co5tTDu2gGUMs8Hs2hicw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EQOova1yluilZtP9JY-O4NIQ72SJek6f4QopdbXFLcHKl7vTeCNo5R_yKWQHytgGDEPjhnWj3MYlBPcZgyB-J0z6Oto5Yl4IKa0kEnONUkebDfJiPpX1_wipnf_ytad3Swo8RZTAG-NM36QI8NbS1lRu7mNIRPSiA-zw_IJrM8JwAW0UT01BSoaiUMaCt3BMW1fXnhuf25ApzJg5s69yXJsLVlnBUKmRY2Zv69ubnV626UoxCgcO6mL580T5TStS8Egk4CurMnTuW-08vJmIy5HyJh24v3VC-0lt8sHTM-pIeF8u7aY-a9Eph_9Kc3yLluzy6qmWQpUPSKAxcjqzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXykCPw51hgwYEx2VgnxXUjbBS2fMflF1QSsFLmVNh9IQmrAGg_zed9V__jc3gjM36Aor1QtTmzjt0qnpquEzR8faujxxiXQJHQoideh8DJz269Lolwp6VOBJJnsoQVf1NM3K_otZ2eDE2wJVr_AVBff_apqWf8aRwxtqTM205IRjmqswTs5KbHFEiMnSTMXeElXOytND4MGKr_Zpn1LIOfNau_Lidr9BDL9UiJ12sc4vNsm5DmZs9mOIUfp96qqZIQPZZdQ4_ogzRpyaeN_HyLFrOUyo1whMENkgjGIOtNoafX08mRbSBkXUd9ara1B2y2TymGCmKQ5wattIkOp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpC6vG6ECtlsHXyZtZ1Yd9kg49Uv4WQxPX6DC2zxW1qYZZV1TnE2prqJRYFU-hOVS_2q-2QdLjMlIbr1SJKj_6pGHU48lsCcqFx3vTO0fNZXfw6qIsMfK9AzLsq_qMsK_ZkFSOdcsBIUe1mCYUy0r2cmwxojGDgdHb9VyOyzqJa7j_xv_eV-o_b4IhbNuTK5gMIxlFlhqu41cLIBTKz8kUmcxfktl-XBvLbyPvjYsZRvuZOidD94s5hbaon0oL74CCVHXt8QxFz3zHbreA4FrVdpTqb1SMu3PqU9gbh3_RCs59cInc2X6YQZ_0KtgIgCjoDoNfNxJ2gbzTL85lEikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TlW_1A2pNQxcHJAzkIXQKlzSpMRv0beXQ9k3a0hrdmX6mODchd_zX982uzXskU6z7x5ONRgUDjtYzvZutg1ss1eCU7Fj5AZtb-53FhW122CII6mcqX6yFnA6Tjx2JGorenGec0fwKIx9dvbLnvaMjVG9vVaWZTlWEhU1xc-PAhK3hO784O_nDA8KmpAzxDojasXMSFl7H84VJuiO01atHqA2Z1eIR1Sn35oy1CsIxGEkbpD3AWWP8_tEtA1nkNDHRNKje2WSikT0CwT3vz2vfIQLxB3vaiACmV3jJOfZyzBE7mjwm-3WHSwaTHNWQjNJ_m5d3E2tkM8kvjG2X0MTWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uiYwciNxEnvqhgRat9x1JCKgf_XytWE9n5IxIHC5EN2pVNq7x9Kw0C9GKCcfzK56J6wVd2k1h-ufAOqbNXvrDEFRHoeuplm0F3wSVOa3SUeOCOZZkih3POAttIci40eTBtd-sJ0ZyaYCqkxP1WG1v7csu-JFRvxGv-ArZxhOtJLNpfw_dtxz_8nbl16bfJHN26zv85xlhjLsaSStr0isXom00ZM3t_IsMshhP0bOP7Yt2oEmrqmqhw_uBrI5gGE6lZHlW7KhYQWRNGCOTU7XUf4vlMFVhfff4YrEtQ-UR5kH-Y-87qYvBJSJT0GPovkHGOok3Zm6PU81vxO2kt2WHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BdXdpjBe8nwlQx7z3F_EGy1Jz6O_Z_NJWy6FhCho2NUm-1dFFkDjDqwo4hQSoYIQts_sphVZJkB3FALTTTg4GqKmsQfHB4ayH9FtqGMxrPDGQzCWTWBH1ZLInVu8PEEt7QpIFBKXbqlsihFaO1euW5y5fkKyaaJlN-n5IoIy7Dh65BfzObApCMCPns8v2cVjl9kdQDcpZFRtrHyolewcRt9Fml0QOf7tzpzjedNSl2t4NmujHfcGNXA0127QRIcZWa_cwHEorJ5XFPyyzZU5f3pOalmmS2toe3NlUQF139cIJEAZoShNt7n2BDE8A1rBs5_hApmAz6kD5Sum1i875A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmVIBmwq8cpCtRZWy2ZFfn9s6xAMjAWA51BioJ-Z5fNLgC1WBm1PXgIfB4IQwoKILPEjtGG5Vf38rC9J5CWnE5ql4CCQ8Uf8r-Y-oAXj2EDwIKmdNi3vwh_uaSezs1Q_XBpdemrzNEoykdQlTnKTZ6Xgvz9Rwj0atQQmEmUjCY8N5P0W1yKMgT1mlqBLHlwpXaMvPRUr0vE7F56YpCEzVBI4QXDES9CUaMSeIbWv1625BSFN_n_Ihrw_mI3txT3Avoh4Gtyb0H94tQPsKH7UN5wg3L3w1UWUPD9wdQWoD4axk9Z8Rqf-o8KMtccvoMFQSU3a63qjjXCsw0XPXpey_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=ptW60INbDxoPMQga3UFIKrQgbgO_YrXt6wo3f-Zxp1BrM5e2LKOpO_KAzxR9CdWnqUfBoncVcLYZ7A0lV7h9BWr-Rbso10rJgvkUekOHd873Lr-bFciApRJqRXCMO8BO5vI_E-WxG4Wt8fsTdEPjXmHj9D_Shnn4r6GGml-5yxrPF43bQa7V-JrOnECko58ORHEHDXd2Mg2CElx_sDTJLCS8j5Fm8zi0bUY1DXVWe5UB4Ji7QcBLG6VykbjOiSur-GBW7Zb6DkEMm9mLfYnMVfOGbAm9S0z_sy7jVwav4NO08TLlwpsmIlSfCjJLqc0jNCiu8wRwxeY2T62ARo70OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=ptW60INbDxoPMQga3UFIKrQgbgO_YrXt6wo3f-Zxp1BrM5e2LKOpO_KAzxR9CdWnqUfBoncVcLYZ7A0lV7h9BWr-Rbso10rJgvkUekOHd873Lr-bFciApRJqRXCMO8BO5vI_E-WxG4Wt8fsTdEPjXmHj9D_Shnn4r6GGml-5yxrPF43bQa7V-JrOnECko58ORHEHDXd2Mg2CElx_sDTJLCS8j5Fm8zi0bUY1DXVWe5UB4Ji7QcBLG6VykbjOiSur-GBW7Zb6DkEMm9mLfYnMVfOGbAm9S0z_sy7jVwav4NO08TLlwpsmIlSfCjJLqc0jNCiu8wRwxeY2T62ARo70OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=jgR65WWOJ9qzeBC24slhDzfjZGIxliCAIqBVrYJWkvASLr49PxC5dqTkWlL2gq-92VnI96QdgcN4Jk4cP3ByW1SFCQP1-RT62MUGNhfdCZKtVdTUtuQERmimRaRkdG5bljiRTH-2B2BiIk1DllEYy2PDjLgQjdCac-xLLACB3a0ykT87aAZNsMYK2K17XmRC-D3wY84TiVOnjuA0BTrpijZzbz1na9laVGHO55OOYJS0a4H1SeRGYbwTp7Lg6MspQXHgcuOzF9gwkn-_BsP0gzHghjjouCiYLnDZ1cNy_khgjOhSSQzZhMAmXGCiPe91vtUsCelbIXfk144BhWQxzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=jgR65WWOJ9qzeBC24slhDzfjZGIxliCAIqBVrYJWkvASLr49PxC5dqTkWlL2gq-92VnI96QdgcN4Jk4cP3ByW1SFCQP1-RT62MUGNhfdCZKtVdTUtuQERmimRaRkdG5bljiRTH-2B2BiIk1DllEYy2PDjLgQjdCac-xLLACB3a0ykT87aAZNsMYK2K17XmRC-D3wY84TiVOnjuA0BTrpijZzbz1na9laVGHO55OOYJS0a4H1SeRGYbwTp7Lg6MspQXHgcuOzF9gwkn-_BsP0gzHghjjouCiYLnDZ1cNy_khgjOhSSQzZhMAmXGCiPe91vtUsCelbIXfk144BhWQxzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=mgr64ty_WDCOi_JpVQRdPorvKkS7AZtdHYB5p8UFhqM4p8HAaqcTwDrvqJXZdqFtKxsI-5TDgribocmM3J04cxtDgSFH3hTDAKFuMJ_o3uScNmrsMDEd64UDfi0hKBTBHjKb1O4_4nrcdaqNF94QqG21bGalb0sXhuwHrygbwj9Xu1DsmCYC1ydO0eg7Crn66lNvtmX3J45wm-pSyEzjn0HOJMZxm1_wFpGD6aPgTyU1AlKvYfOD8wpa37tX6jaMDqZpKlurFdswlVftljxAYJB2h3dbr72VHvpqtws-kheHi7rKj3jD8JqIMKDrFTAk--imKT73Ajhzd7Z2NPy6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=mgr64ty_WDCOi_JpVQRdPorvKkS7AZtdHYB5p8UFhqM4p8HAaqcTwDrvqJXZdqFtKxsI-5TDgribocmM3J04cxtDgSFH3hTDAKFuMJ_o3uScNmrsMDEd64UDfi0hKBTBHjKb1O4_4nrcdaqNF94QqG21bGalb0sXhuwHrygbwj9Xu1DsmCYC1ydO0eg7Crn66lNvtmX3J45wm-pSyEzjn0HOJMZxm1_wFpGD6aPgTyU1AlKvYfOD8wpa37tX6jaMDqZpKlurFdswlVftljxAYJB2h3dbr72VHvpqtws-kheHi7rKj3jD8JqIMKDrFTAk--imKT73Ajhzd7Z2NPy6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=rVpaYKRm49M60F6Q5ECyJQCkdX94tuVzJ89yPWEt1ieS8MrRnLrde-SuGogRdOELUa2cj3bHc4aEm6YO2V8pYhk_8cyASyTGwTqOrod-tYkbzXwi5p9zva4olIEAhfhYCeQVus9TrRTzpmOK2Q3frGcSyTgZbJ6315qdm2DBNIqIZ-SY6rmxlospZsZ4ITHycSuvYcoSLm9Bx63bEMz5dgNfgW_YfsLw472r4CCwu8STLDOPIF_-zifIv0aGhiov4LlU5z_J3VC9Hv2AYBsMfkJfYHIezjPYAzwBoDw7JbwyUYXQAkb7QetiuN3VU0jB-nhR8FRUu4rNQhpaTBi3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=rVpaYKRm49M60F6Q5ECyJQCkdX94tuVzJ89yPWEt1ieS8MrRnLrde-SuGogRdOELUa2cj3bHc4aEm6YO2V8pYhk_8cyASyTGwTqOrod-tYkbzXwi5p9zva4olIEAhfhYCeQVus9TrRTzpmOK2Q3frGcSyTgZbJ6315qdm2DBNIqIZ-SY6rmxlospZsZ4ITHycSuvYcoSLm9Bx63bEMz5dgNfgW_YfsLw472r4CCwu8STLDOPIF_-zifIv0aGhiov4LlU5z_J3VC9Hv2AYBsMfkJfYHIezjPYAzwBoDw7JbwyUYXQAkb7QetiuN3VU0jB-nhR8FRUu4rNQhpaTBi3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nwE5adGO0A2e4t-WOKYdZvMgzGnpuhb6JSU6yE6EbzMcOIbuiHDYbDh4P1HSmt-P_yabtcpdAvCvzf_AXUkF0hfXj3yI23mBCpoHkX3eOS-AG4TQELepD8DDOa8eGy27rX4wGWmuDfhVarp6ctp7_bbL6THhXZVUyqoMILakcBkRrC9qTgIOP_-7s66Y-GiyFmNXF9neHRNw9FrguFAYHxRPnDgJLFidVrFA8_RxOuHHVA_t41IKOY-wBDXRJLbKbOhfb34hZ_icHJQLq-0XsJhQ6HSr7ScC9ReOMMUVK3nxXplCUJzMZBvkBPulagKP4oJC2leA1-xy-9CeatnHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuPm5O56Hc8vFKDluvi7WZbpUa-HQsqw5K6C_hAH90F9XRGhBA-QSaDf0Q4H4mwnZMuHWAQRmF5ntuM_wD4Kc3UIfbuYzjvF4mSnYEF31gHmYNWb93gLB9RRDJi3-IWd3eOTqdKS0xGdY_DbGXpsMQqvg0Xidv20WkcPckBW_feplOrjbUrLK5zmlkFp3owXs3fkQqyo2fJBVkpFsNPjcIGLIWoqEAVf7sen7ExulsDnOvSA3FcFo5LTCCcbw64OEGb8IYV5Tcd8EoSiAc0uHfQe0AfrlDtA_Y66ghWNlo55RgM28lDv--5ccc2mvqvgIEQ6O_OF76EQGgYGHRNHUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ch0pBvTO1JIoMNQWV2Eo8_x_Yak28MOC7z4ETVVWGdQViS9Te8HKT3Cjx_VK9y-J02L4--_wb_R1IsCr9VdKPgRTfCkZXWiyGFz-3uSEziLNq7yLdaG45mmSKJpcYTe5vw6lUCPdE5zvZLepbUX026QU0FoV_oOavKLFZMq7yFSSHCKSzy8kjEA3mJF-9G4QSxRyx8Jl2iXqXYEQPctw4mfRUW-TvVnEpoh4eP4u6jZy_2puS5YsfwBZiUA8f44QpKEZzpuCELaNLZc0iKnu4G-cnVL_o8uXb1VPIF8LjcXkQgVY-FgoqW-eFixGXj4fJpaTCAHGfIJARLGcVtZIjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=YmYANDidpyWG7Ybuo9dO1W8mmaBojoO5jSnx5Cxlyvr-2kZefkygjMfJ6wgQrQX4wr18CKGEGLJc0ZtoRq_CoZhdO6TytkrwGSoHtOMoVsvsdWz_kIOomcY6kVIThDCAaLAiHnf8otrFo3U1RBweChf7aELN_FvbzoHl1QeLaUwLg6A60U4JOexF2h2SvsX-3Nmss3cq4QozTRIJPqFT7TN7nON675qqjDSlmCKikC36kqyivbxovWUnzyvtuFq4wBRcJRFjT5bEwKXZipFQj8vXnMmZZXbHbUqJ1lUFeCp4jxRxQC0okSDhaQonRYljNsq4v2LM62dCmMN-QQyIZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=YmYANDidpyWG7Ybuo9dO1W8mmaBojoO5jSnx5Cxlyvr-2kZefkygjMfJ6wgQrQX4wr18CKGEGLJc0ZtoRq_CoZhdO6TytkrwGSoHtOMoVsvsdWz_kIOomcY6kVIThDCAaLAiHnf8otrFo3U1RBweChf7aELN_FvbzoHl1QeLaUwLg6A60U4JOexF2h2SvsX-3Nmss3cq4QozTRIJPqFT7TN7nON675qqjDSlmCKikC36kqyivbxovWUnzyvtuFq4wBRcJRFjT5bEwKXZipFQj8vXnMmZZXbHbUqJ1lUFeCp4jxRxQC0okSDhaQonRYljNsq4v2LM62dCmMN-QQyIZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrrihYG49Ck5hr8tPR-cY5j1YJMtbS0TDQWfhbpvf3wN468MtdAkcgrX61XYOLDYXHJvswkIi8ywewLHyfCwvwCEO0ySuzDTeInDbZiSGBJxdLVaXGN5ArU7wR6eTzxLhUlDrf2HKNuyfnhpcgBjoMtszsblD0G-eN3YawcQfO6sHoVueelxsghUs1Ou3FcXmcUjcVzg5Ir_6lWZr3h1scDe_7ukznlM7ORIoMYOqUrclkJn_dL-ZLXzMB_IMTSAGEfuZovmO_aXRt5_gUCTc0TlTDIF61qt0KtwFR0C_FZr_LCUAMhAI2LPGBW9-02mOKy0U7XGpFpxCgB9wJNNQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=ao3Q96S8gPg6ZLJqZrhvlMVBt8oWWFs9RkY017XfhAv5gzvo3ZLP18KrsQbI_LvI5VKi-WJi0Y8ZHoycjWYnZbLPB6ioMmSiiIBW45-uX68Z2s8-6fROqTV7eVOcxuV9wmXRuHZp9Xcn56p9ezdbIqURyJg9-Y5gIXkryJL1YMgqzcmHD82d_QoN1uzkQM8_y16751px-jU8WqmErKAlVSN8EFmK85lxhc8LJck41382o0buP5ok0SnMsfZFLC7PscpaDZEXDOpN7qHMZfA1LDfNIiUmFUj2AF2n5JHmNaPkhJYRJ-bETh0Uku3hk_yRQJPyvOzioT5_bjJzYl2rrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=ao3Q96S8gPg6ZLJqZrhvlMVBt8oWWFs9RkY017XfhAv5gzvo3ZLP18KrsQbI_LvI5VKi-WJi0Y8ZHoycjWYnZbLPB6ioMmSiiIBW45-uX68Z2s8-6fROqTV7eVOcxuV9wmXRuHZp9Xcn56p9ezdbIqURyJg9-Y5gIXkryJL1YMgqzcmHD82d_QoN1uzkQM8_y16751px-jU8WqmErKAlVSN8EFmK85lxhc8LJck41382o0buP5ok0SnMsfZFLC7PscpaDZEXDOpN7qHMZfA1LDfNIiUmFUj2AF2n5JHmNaPkhJYRJ-bETh0Uku3hk_yRQJPyvOzioT5_bjJzYl2rrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=JKzAjanDdNl2xJcvfvXyjFLMPYYukr9HY3FPW3eWiCEfiW8wmXORPAOm-sSn8QiKYSO8Z-S65RGagixxD8kdTwRBzfWdfrc6qEA28sh4IkA7jclpEUFzw8orCYW7_odXcrZzbNb6YAr7gBQSafxICeWJEs_eMRSv_pssDwZtDi-NkPB76EarRj7e7_1KGmzXXaz-zGkGNPbsVt0IWfHVRexOQnZM382tGelFwFoUIHToh-aflzVTxIhCr5dE1ehHQo3KJ8wXzLFe3eUjwSSWIFHiz_cO9OiOgMqMaCsEe8DxwhO-tIu1ahvEQdR2-vt7hQ9pZ9dohNuYFVjpQNKtSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=JKzAjanDdNl2xJcvfvXyjFLMPYYukr9HY3FPW3eWiCEfiW8wmXORPAOm-sSn8QiKYSO8Z-S65RGagixxD8kdTwRBzfWdfrc6qEA28sh4IkA7jclpEUFzw8orCYW7_odXcrZzbNb6YAr7gBQSafxICeWJEs_eMRSv_pssDwZtDi-NkPB76EarRj7e7_1KGmzXXaz-zGkGNPbsVt0IWfHVRexOQnZM382tGelFwFoUIHToh-aflzVTxIhCr5dE1ehHQo3KJ8wXzLFe3eUjwSSWIFHiz_cO9OiOgMqMaCsEe8DxwhO-tIu1ahvEQdR2-vt7hQ9pZ9dohNuYFVjpQNKtSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=u1e_LDWCEosfeJyEuimcox1Hllb-s7Pvv2ryhT45Er7-GWC3NsjyHmk_YzZbRukvU9E2cUjGu5bVmnD2qQNKQr8XvkQ_HkcKPxgUIVgakF-ICYqD7ZYOJpO3d7-Eu2ezH1CL3sceIGIXsxdUQWJPXkRiRt6waJehcpo_nqi1pa5O-VNoGz_993gp-ZLd0q0X1cutGrSEpdEhQmE43VU4XZPaKTvCb0TYwUl-AvE64p7i-z0fqjkJCRNr0gdnv5MRctqQ2UBqwidQ7Zzk2bA-o4Q_1Rct_7L8_pB5UTBwC-JeYNXM1uI9tny2UynGfNscW6dxhTzEU2KzuHeilDCAzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=u1e_LDWCEosfeJyEuimcox1Hllb-s7Pvv2ryhT45Er7-GWC3NsjyHmk_YzZbRukvU9E2cUjGu5bVmnD2qQNKQr8XvkQ_HkcKPxgUIVgakF-ICYqD7ZYOJpO3d7-Eu2ezH1CL3sceIGIXsxdUQWJPXkRiRt6waJehcpo_nqi1pa5O-VNoGz_993gp-ZLd0q0X1cutGrSEpdEhQmE43VU4XZPaKTvCb0TYwUl-AvE64p7i-z0fqjkJCRNr0gdnv5MRctqQ2UBqwidQ7Zzk2bA-o4Q_1Rct_7L8_pB5UTBwC-JeYNXM1uI9tny2UynGfNscW6dxhTzEU2KzuHeilDCAzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQ36tZDi33dxBjNEHBU8fpqDueSaepGLnKSvmgr_RRcJTKfOFvGoeyEoYHC3LMzlO5TFW3D-9qzXeXVCmjU_-QXMkWjiaCyJIMAEWCKDM_HHHBjE2VS4Q4H6M3txrtiRvNh-KF8nix6REEPg90ekky_iE00xVTDqZEThxZF7G2-FWLpfBHJvhi02sCtImfpljG_XpFZk0xKshjGeoIXBIfwyk3FqppZO6FWp9S6Fsj0b3KXd5JWq28BNFoxvTMtYMlGwUPP2d7AOVh9ZDHA4Aj-v-Dpi1Mw6n4yoJJ8P1CpUyy0fSEIGsmk0P0PsQ_i09lwsBrL5CaBpH_6ShPtdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=s8TuA7h6He5GBI_fQUl2euDWAVLExT7Wcbe_xgV2mz5MeK5ZoE3GjMCURvgCWpNoz9Gnj76veWrFprOy4flevYl9mT4cxY7mQhjpDloauIhF8ogJitRvcyLE9nyMweaYZ_FU3jS_9q0G-D-zTcu6Yj7-yHLIEFzENtxm0zhZeDgkr9kAGYqAzK-5EE6zjsO9AfyJikcCp1yJ8-qxaOtxl7R3-KK2MFXR_rdFWcBw3Zmk0duoYe6wfG9E01H1jxy25XWZEG6qbh_o0e_wrEpb74u-CrkwDhi4B4vqstKpMH7qXR7GifWLlVLcc8dGMhIJBRAx54sq-YeHZEeh_0NHbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=s8TuA7h6He5GBI_fQUl2euDWAVLExT7Wcbe_xgV2mz5MeK5ZoE3GjMCURvgCWpNoz9Gnj76veWrFprOy4flevYl9mT4cxY7mQhjpDloauIhF8ogJitRvcyLE9nyMweaYZ_FU3jS_9q0G-D-zTcu6Yj7-yHLIEFzENtxm0zhZeDgkr9kAGYqAzK-5EE6zjsO9AfyJikcCp1yJ8-qxaOtxl7R3-KK2MFXR_rdFWcBw3Zmk0duoYe6wfG9E01H1jxy25XWZEG6qbh_o0e_wrEpb74u-CrkwDhi4B4vqstKpMH7qXR7GifWLlVLcc8dGMhIJBRAx54sq-YeHZEeh_0NHbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=bun8Hrp60ciYvkIh5wD_HQOtyp8xGovtQs9QBS9bQ_YPl4ojFeJRpqc2Y3SEBAizi5Ze8B53XF476Haz2TKaC_K0xRszkh1XqiveacdHr1EDLUAQg3LMbO8nyP8kJiDyYLCQi55bIVa2AHuXvUxd-msRffbqG55MsaIjElYXe3CkSVOZzCpLaMBlJPICMXUxUSiWikFUnAmwPRH1h8xEGs3raoAk2pW_Q09kMUUk3-bUFN4-XPkNuLRIegohMZUBtefLMGO3xcNNzEKwgDYPOgSgYGiEaYqmFloU2DBhglZM19iI-MUeD_mmlMsF27d6nSWOvBxEkDX0_MpCq5z8CYheH93feFObTnUQsWrUTV1r9FjmjmkP0aASnJd04bL6NEa4OgEbKBghlKtT9OifpfAmlwlskVix_09Vi14GRBwf3jWrEPOHS8xXVf8YqufqSbhBDNIT8QQSYCNu3mvpWlkfj5KREOPwuTuI9nQF9iGLFknpzw4qXec6a0BvBuSOuFQHDbPDuNlhifKIxBssuM8GEPBdpw6rRux0qVUhR6t8GdjwGxEPPUg919dZCM2iXH2YZp72TZ-SHguIpVz-YAa9EHvD8DC7AJfyG4B2doJDpvekQNxD3QkPzTlT7d7M3RtEpzXJggmx1rm8zavyPGq7wr-5pbEEMfAE5IUu5ss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=bun8Hrp60ciYvkIh5wD_HQOtyp8xGovtQs9QBS9bQ_YPl4ojFeJRpqc2Y3SEBAizi5Ze8B53XF476Haz2TKaC_K0xRszkh1XqiveacdHr1EDLUAQg3LMbO8nyP8kJiDyYLCQi55bIVa2AHuXvUxd-msRffbqG55MsaIjElYXe3CkSVOZzCpLaMBlJPICMXUxUSiWikFUnAmwPRH1h8xEGs3raoAk2pW_Q09kMUUk3-bUFN4-XPkNuLRIegohMZUBtefLMGO3xcNNzEKwgDYPOgSgYGiEaYqmFloU2DBhglZM19iI-MUeD_mmlMsF27d6nSWOvBxEkDX0_MpCq5z8CYheH93feFObTnUQsWrUTV1r9FjmjmkP0aASnJd04bL6NEa4OgEbKBghlKtT9OifpfAmlwlskVix_09Vi14GRBwf3jWrEPOHS8xXVf8YqufqSbhBDNIT8QQSYCNu3mvpWlkfj5KREOPwuTuI9nQF9iGLFknpzw4qXec6a0BvBuSOuFQHDbPDuNlhifKIxBssuM8GEPBdpw6rRux0qVUhR6t8GdjwGxEPPUg919dZCM2iXH2YZp72TZ-SHguIpVz-YAa9EHvD8DC7AJfyG4B2doJDpvekQNxD3QkPzTlT7d7M3RtEpzXJggmx1rm8zavyPGq7wr-5pbEEMfAE5IUu5ss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSmNO7lzVBZazEoc6wY166XvDBt5tQpFIFURYy_XBMoM3rs3ahFJsQ08z6bG140UdaFzMBLbXCHi_LcmKr099W4RL-gFjOoEcelJOPgADU_Yj6MtvVF_Eh_duWSjh1i48iD2b-U9hEPPxFd5M8H1OKsaBT33mlHiWZHIktWDG0wB6QYIFdoo7rojHwL5Hh-8-KdHOCVugShafTOJOCvoeZXIQTB2VxPFZ-hrrk6ML1AbGsK4PCB57i1CufjapdGcCWHiaEWHaOgvFuC9xbdldCMrVmo7Xs2d61t8QrCcCs5wOTA1G9YLRgSMlF5oKsB3yxGUBbTeKZQGxIRwJT5PSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=h2uIP1VFcnIEDGBaZdNG78cMMd2c0NEPk4EkNUBY2aoFlATuP-8Hni8WlkLuwMdNwd0ArQLYOuetVBqpdpNw7CR1QtHmdDnBiVbIH428r4c0RdslbLtcXfo4Xw_4AIWsy1NlOytD4auphiV28nGOAgHS6lu8QBnrq9uRizteBp47U0L-cBmCHnvYgB94i8xPPy3PtupzBh38i98vF-nO9A_fEpJiRMeBreqAZm61VFPZfMfreO7qREd8pdvlpcI6gamUCoc2O8AUNuqnKkNxP4sgmoc0_fE6ebhOGIWWpavWT02hzrMKjPqFVLrGCjAi7YpIDAVgsL6XQ74wag7Fhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=h2uIP1VFcnIEDGBaZdNG78cMMd2c0NEPk4EkNUBY2aoFlATuP-8Hni8WlkLuwMdNwd0ArQLYOuetVBqpdpNw7CR1QtHmdDnBiVbIH428r4c0RdslbLtcXfo4Xw_4AIWsy1NlOytD4auphiV28nGOAgHS6lu8QBnrq9uRizteBp47U0L-cBmCHnvYgB94i8xPPy3PtupzBh38i98vF-nO9A_fEpJiRMeBreqAZm61VFPZfMfreO7qREd8pdvlpcI6gamUCoc2O8AUNuqnKkNxP4sgmoc0_fE6ebhOGIWWpavWT02hzrMKjPqFVLrGCjAi7YpIDAVgsL6XQ74wag7Fhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-EkrfLQR2_-JNXUKN7N2zUbI0YP8_nX8iAwweQLecfHAOlr1W5MnB_GUe_UkJKDfPDE1tTLewtn5ae02rp44ae2EPiJD2SjD3dOkLEjy6IktMfTC_v00IXziFEIT1UJzbVR4Wixdnl1rsc4JTPrAWuieXp7aJyw56cUtqc-3488FXFDsozkEzfEa0YP1wEcoGquitw-SWTVQ7BFRiLrU38zZdv-Mjnv87mcRMxGknrXfPvWLZ0AwoqixnGBit2-jre2p_2SyJGzR4pHsJE7RXSnvKeHOilgTxUcgsVW1TXx8HIYuxeVVDt_ibempEmtMVR67kFbHct2ELhjR3F5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=fnM0zPalE3rWjWkjn9iiIt0lsqtrKab4EmAmGiBXl3GD_77g38UmiQlXGIl_l4g4Z73qjCCp_jpnE4fnb0Ui1SFnDWtpaCoep9hoQccDHjFzYrEa22WzsWVy9ZZbHpdFrPH-NpPqUgFW9RMVDXMPLEBiVkG2jgcKQiIGFQLeR5TsKRyRM0h7xPy_t5OD-A5thohoNRUsQ0Fdflr_pTspbLTFOZjJWGVRs5KRp10xIbfL6C3iRvfV4BCoTft7kAjHBH3rNlOLl2oNFH2aVYOnpeXJCiCH7_C0u2FWgNDOCrQL4Sxfxhk5Sx6_uRYJWzDvto4x5PV49kLmEx8k0la_A4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=fnM0zPalE3rWjWkjn9iiIt0lsqtrKab4EmAmGiBXl3GD_77g38UmiQlXGIl_l4g4Z73qjCCp_jpnE4fnb0Ui1SFnDWtpaCoep9hoQccDHjFzYrEa22WzsWVy9ZZbHpdFrPH-NpPqUgFW9RMVDXMPLEBiVkG2jgcKQiIGFQLeR5TsKRyRM0h7xPy_t5OD-A5thohoNRUsQ0Fdflr_pTspbLTFOZjJWGVRs5KRp10xIbfL6C3iRvfV4BCoTft7kAjHBH3rNlOLl2oNFH2aVYOnpeXJCiCH7_C0u2FWgNDOCrQL4Sxfxhk5Sx6_uRYJWzDvto4x5PV49kLmEx8k0la_A4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=oYraTGSpyVd40tk1l-Z-Jt2h-hlTR0zKyOgHCYZYkxUWb2-y5DEOeurdZj17j1LiYrEq4JCxeyR1QPUoCS1rRxGnx0n45tAvkfGDW9qvcQ8QaRdTtW1XRUBUGfSlecO7ImPw6ei2xIBmIc55q48MT83pBPEiYXlV8MfdvMXZL_pA2QY6U7kNo3kjEhoqNLs6_dR9pvHIXI8ozF2YrbK80yyy24NKCQr0V-rmBT3vZWlLhbX5MQR_wUo8J82mYE8zu973rmJOL_NBeQTn4tlBpUjphtC8iNVFKZjh4PQaAGqDFqYEuY_xlXetmdJjhF2AFV4C18DoXwNBq9yCRI5A2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=oYraTGSpyVd40tk1l-Z-Jt2h-hlTR0zKyOgHCYZYkxUWb2-y5DEOeurdZj17j1LiYrEq4JCxeyR1QPUoCS1rRxGnx0n45tAvkfGDW9qvcQ8QaRdTtW1XRUBUGfSlecO7ImPw6ei2xIBmIc55q48MT83pBPEiYXlV8MfdvMXZL_pA2QY6U7kNo3kjEhoqNLs6_dR9pvHIXI8ozF2YrbK80yyy24NKCQr0V-rmBT3vZWlLhbX5MQR_wUo8J82mYE8zu973rmJOL_NBeQTn4tlBpUjphtC8iNVFKZjh4PQaAGqDFqYEuY_xlXetmdJjhF2AFV4C18DoXwNBq9yCRI5A2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=SRnKO23O4yBRI70mFvoKRVI1P0np_XhnjAs7abRmtXoSUTOupKPOooN3sPKKT2nS2Z43z4tr5yzgRwxDVzZX7WE-u9E94Yi-8awSRJDeo11uHGKzjB1uAiv-2VIJ1W_cPwYTpHjuaVj-wDqHdxcu4c7js5dT4asP9oQQb3FG6H100Sfu0vqKUhADkXXRSVmT9ZGPUeEmlfxadn1MK3x40QA7sl_gJ5nZSQGy8OXlAsdhJYXBTAw1M3H2VUc2h9wZjjLLlOsYfYhTcM4KzpBBVrVp4E8QygyQ4wee73CWSWX65ve1C1W1H8s-Kn05RosMAs81hi00XB-BbRzWN0yzPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=SRnKO23O4yBRI70mFvoKRVI1P0np_XhnjAs7abRmtXoSUTOupKPOooN3sPKKT2nS2Z43z4tr5yzgRwxDVzZX7WE-u9E94Yi-8awSRJDeo11uHGKzjB1uAiv-2VIJ1W_cPwYTpHjuaVj-wDqHdxcu4c7js5dT4asP9oQQb3FG6H100Sfu0vqKUhADkXXRSVmT9ZGPUeEmlfxadn1MK3x40QA7sl_gJ5nZSQGy8OXlAsdhJYXBTAw1M3H2VUc2h9wZjjLLlOsYfYhTcM4KzpBBVrVp4E8QygyQ4wee73CWSWX65ve1C1W1H8s-Kn05RosMAs81hi00XB-BbRzWN0yzPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=aKh5psVgLARa9lTQy4kIqiQWZHCQuprnqQ_ClegGhQbE5Pqzye1h3OjIKqkNmxjpkRE7txFMWLL7Cgm9KKAedzYruaAwFxM_WnjXOuTT2UtOxlz-HX6m2EAzupj6gUBCbe1RgVha4IlLpFm4Xrk3Qd2F7gvY-2nCMULTRHrnf0-ONX0SWWRM8Wks0nnShQQu5BxsUBRIRdJn6t4B3kjVmRIKRNLpwtF4vv-1MwPSnj8UB4gVSZSROydVRWwLoAaAYTfaFQZcX05NAFsZ_5oCZB_5uOkGZJsj6co9E3dQ6Y2eRLZrnO7WqbCNMmg0Z4hg-XPgu2nQDL7K1fbvIO3x8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=aKh5psVgLARa9lTQy4kIqiQWZHCQuprnqQ_ClegGhQbE5Pqzye1h3OjIKqkNmxjpkRE7txFMWLL7Cgm9KKAedzYruaAwFxM_WnjXOuTT2UtOxlz-HX6m2EAzupj6gUBCbe1RgVha4IlLpFm4Xrk3Qd2F7gvY-2nCMULTRHrnf0-ONX0SWWRM8Wks0nnShQQu5BxsUBRIRdJn6t4B3kjVmRIKRNLpwtF4vv-1MwPSnj8UB4gVSZSROydVRWwLoAaAYTfaFQZcX05NAFsZ_5oCZB_5uOkGZJsj6co9E3dQ6Y2eRLZrnO7WqbCNMmg0Z4hg-XPgu2nQDL7K1fbvIO3x8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=TfIl7OUIox6ySXslnlvreOYsg_j1TR37E3ooyuVqskHYeaHi79t9-UNSaU376LJ1JdyOymPV_6isvPioXl6Ib_96PL4cV1xegpV98sc2eXJvHYLzoiM7wNEmQFKgxWMgu8W3Ny0_qc8NxcMJXxzYhLkeZAIn8L1Fmzem4JCQP1_26-ywQbOqLIZXoyKVQ2Cszs3WV4ex-JMkE_1tFEhjMapF7lNBoymojdrNYZ9I07D-vRxz_bRe-PIT3EizV2u0xYFt1C-t_GlIqKm7Py5NUDxWZoKhD0mDR17Qtskw5A6Yw0dpUGxR5pIX7_nENY9ATRXFh7eeqnODBTBQHKztNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=TfIl7OUIox6ySXslnlvreOYsg_j1TR37E3ooyuVqskHYeaHi79t9-UNSaU376LJ1JdyOymPV_6isvPioXl6Ib_96PL4cV1xegpV98sc2eXJvHYLzoiM7wNEmQFKgxWMgu8W3Ny0_qc8NxcMJXxzYhLkeZAIn8L1Fmzem4JCQP1_26-ywQbOqLIZXoyKVQ2Cszs3WV4ex-JMkE_1tFEhjMapF7lNBoymojdrNYZ9I07D-vRxz_bRe-PIT3EizV2u0xYFt1C-t_GlIqKm7Py5NUDxWZoKhD0mDR17Qtskw5A6Yw0dpUGxR5pIX7_nENY9ATRXFh7eeqnODBTBQHKztNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=cnOjgINV7qFdivnTdpRU6-1FfCbRNKmx7ZO18K8b1KbSpU9p8N6KJSl4Esh6ZIWPzp3MQkEamsuwAsSUYriQU9gC6AmBIxUnEP1q_ZyI-7H-nd-n64TC-GJKyRr1Yi1CvT6qjjpEa_GMmK-UUlXUMO9vvWR9nwL2QK0tNdKXiuypvhPY37x3ThQEhaIWVOKXAAe0cn4SoOFWOK0jpGrlpBiAAl08zNjPB4IRod9-BdGGDphafblWO_aRCngzxdl8PE9dXwJ-1IGAbU4lGD5-WmlkMvkruiuVG1X_QQILnqwquPzOGcagYuxEIzOZr6T8sqhwJYQxM0nCK0GSHXe3dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=cnOjgINV7qFdivnTdpRU6-1FfCbRNKmx7ZO18K8b1KbSpU9p8N6KJSl4Esh6ZIWPzp3MQkEamsuwAsSUYriQU9gC6AmBIxUnEP1q_ZyI-7H-nd-n64TC-GJKyRr1Yi1CvT6qjjpEa_GMmK-UUlXUMO9vvWR9nwL2QK0tNdKXiuypvhPY37x3ThQEhaIWVOKXAAe0cn4SoOFWOK0jpGrlpBiAAl08zNjPB4IRod9-BdGGDphafblWO_aRCngzxdl8PE9dXwJ-1IGAbU4lGD5-WmlkMvkruiuVG1X_QQILnqwquPzOGcagYuxEIzOZr6T8sqhwJYQxM0nCK0GSHXe3dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=HB5sI-vdrRuUNwonI4CcIP7b7gZY0T3wndRo8YGs03xFDC4hO7nQNGLpuBlxTncgaJvv6k-y8324mhl6kS8psMJjJw6F11bcdR6Y4PAtvuheDb9JrSaQBQqjocW2OE8YUAwxn8KNzSrs5wfF09GpDgnM7r81hF59rXk4CO0IODF22PevvrNP0ZPf0GxGsT2LsJ_6QBWljIw_GUQLQjm0Joh-f1fdmYv13jAjAkvdKTvW-CDtVTbxfscboL3eTQ46CsiQS21DFLQkE9wQ-aNzGOT4D3gZegdU2BWoWEQZmuiEYxwJ5kSGy8odcsa1ip7__7JHlMoUPsBzDhG9PdSqNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=HB5sI-vdrRuUNwonI4CcIP7b7gZY0T3wndRo8YGs03xFDC4hO7nQNGLpuBlxTncgaJvv6k-y8324mhl6kS8psMJjJw6F11bcdR6Y4PAtvuheDb9JrSaQBQqjocW2OE8YUAwxn8KNzSrs5wfF09GpDgnM7r81hF59rXk4CO0IODF22PevvrNP0ZPf0GxGsT2LsJ_6QBWljIw_GUQLQjm0Joh-f1fdmYv13jAjAkvdKTvW-CDtVTbxfscboL3eTQ46CsiQS21DFLQkE9wQ-aNzGOT4D3gZegdU2BWoWEQZmuiEYxwJ5kSGy8odcsa1ip7__7JHlMoUPsBzDhG9PdSqNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLKVIOyDUfMTeiYGDcNonMoD28WiHkJdrDaqWt9NNEvUIOZuhvW6dK2dUdcIjaKYEHJo0wepsmPH429NhgWv1dlCAXgsgEFxi5tP4FQqZFR9w1GQaJTbjDaxiBt9-7DZkYBMpJvEORrllj4zSw1ai7u49eGXwTQB1NxRdIb6DE8Y2HSGYnhVY5X221grxRiVWnew2mKp-qSMzWHnXkQBrJoQsbYZ8Kb1GdX69vQSXhxfErTZzm0_FEYV9Zn02kBiX7Gm_TyAzku0z3epHL3lXmtf6EEFpGDWi8cscrRnnrESqqjpOEVQcRgjKcgnsf5JpeRgSbuuGuLsQBWr5U_Hbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8U_Go0khkrWSFbECYRp1kgQSRs65p2P9-N01haIHT2v-EXBrco9Bz317zOPORRkEA7dMhoatXKs6iP5KBxxecy8M50u8JtV52Wt05A6n7d8Prlmv9GG32tZjn5HHTv2iA7TNRFU_fjjXflNbEH6y-MDccrKJgasKbfwOoMrBerXhH5fw4bMVEt2eXZu4zV0o8PIYZVMvzBVaSATABYPw8JyJVsT_8f9nrkwmyIKrF5Pb1iKWC12WEJnAbj6tIpnGwosrQNMtwvcrzzaz7YmzfhzaHR-KP4s9TmmhOKb9So1BNk6vWAV3HiAl_xA5ebbGr_pyBvDlPcgn_J_gph3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYS8k8x0LjYS_a_9a4_7iGLb5TiRzeq5ttysTs4MdtY8G9De4Xycr5SSpfzdOF_-n6xSPY1BK91kDoef3QV7CX_qDGj_nESvM6RsyfGs8wljTa0rbTeZT7z8KNoRKZZJz0uU2VUiUibHk1QY04OBFLDQSqh-Wmu5-jO10AffIDpKEGteTBIkO5VSgraEoB2Dq0sLpDGZNkOkKzJ2yHsoXNlTUiDety4wzvysjeYfINjb5_KP2VSwWod3mMjxW8IomNZX7cHun17ALTvytnEuO92TJBmIqr2d2oe4l7QwDsnBESFaA_wq-jqCfv3qTiqGkgdl2B0GqzrvITqLQyW5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=WNjkvVV2poJlaGBuIsQ0BVhtaRQFex6jPXS71uYPBBIG0JmYalS4i95iz5fq5z9ZAKV-TtzlNHZDMT9d3GuNbGQwgSjNgjssrs6uzT6xfjyTKshREk9oswMVGInTjIdgMmCQd8tMdIJb6ZQ4pBs1CYASGpI99zz8Vh6h5hr7xE-PWby5VTjZIydHW_5S25rOkt2plKrNOYpraYtW36ZZ14Dq1yODXhR6F2r_JeEBJTSwQHgKGwyesNyoXyh68jltpHaIza8icqC2PptvyR-Aytb_QK55gGBmpy5Sqdo8t71t9xxkh3pP-ilUdv03g4SSBpBgXbNBGEouZVuoXYM6MzCeZud-pbGIYSk7xTCShzbH1pzD7OXZHUuzJSIxxTswno2OY4LI4PZEy7dcwZL5cBSwHCl7ijiChfNela0PijvUvjaPjnf72oKitXrPQFKvRa1brs2ISqH3ow0hXJtQW5hAZZRxSXRpymiQ04x--dQ12EyW4-gjFkNgGpu1FHJI8OZLnyPmcbQWkTJJXcuYwYCfOLpgzu1bTk9ossks70yM0lvSwPZoz-iW7XNdC6zlkUMl8EnSs15T4gWwu-M9htmpB8CTOkeG9qxfv9ss7EPrlOkBv0lrGPKNq_h_wMtoWACoLt9EvOiqIWwbtmCyR_s6F8p8oPSPSxR8RxZwIvM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=WNjkvVV2poJlaGBuIsQ0BVhtaRQFex6jPXS71uYPBBIG0JmYalS4i95iz5fq5z9ZAKV-TtzlNHZDMT9d3GuNbGQwgSjNgjssrs6uzT6xfjyTKshREk9oswMVGInTjIdgMmCQd8tMdIJb6ZQ4pBs1CYASGpI99zz8Vh6h5hr7xE-PWby5VTjZIydHW_5S25rOkt2plKrNOYpraYtW36ZZ14Dq1yODXhR6F2r_JeEBJTSwQHgKGwyesNyoXyh68jltpHaIza8icqC2PptvyR-Aytb_QK55gGBmpy5Sqdo8t71t9xxkh3pP-ilUdv03g4SSBpBgXbNBGEouZVuoXYM6MzCeZud-pbGIYSk7xTCShzbH1pzD7OXZHUuzJSIxxTswno2OY4LI4PZEy7dcwZL5cBSwHCl7ijiChfNela0PijvUvjaPjnf72oKitXrPQFKvRa1brs2ISqH3ow0hXJtQW5hAZZRxSXRpymiQ04x--dQ12EyW4-gjFkNgGpu1FHJI8OZLnyPmcbQWkTJJXcuYwYCfOLpgzu1bTk9ossks70yM0lvSwPZoz-iW7XNdC6zlkUMl8EnSs15T4gWwu-M9htmpB8CTOkeG9qxfv9ss7EPrlOkBv0lrGPKNq_h_wMtoWACoLt9EvOiqIWwbtmCyR_s6F8p8oPSPSxR8RxZwIvM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLTpyu_WcX2b5zrR40OFPaoQ3Oi4Fz8oLfLdhgtHW7q97N_ngtTDwBEWLb2_yQBkhRpNQpsM3nivFR37LYoPHWtKvszgOjFJJmR-aUg_nIsaN2SPjWkvOdVCt3PZ18Xfid9MOg3QWlNMBZ1CF4LA8BKjADyGZBsq9qBIcIO8GNVH_t3UEaORXXjV_68PtWlRBJN7P0QQKI1vdoPeEguX2lLjmuPGggg4saHtPoZGlB9rrmC4baR52r5gWpBahjewsQnocdlS-P64F3Ncyg8-pQaTLs-GYhp2I97SazScV8Ew4CALlb0DEoNSykWHnxhD-p4w4ycsNBl6PmlKNWR8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=s-8gU0asGd9FBs3qdBVt7xHtHbljf9xa5aOpDNpW4G5dADwPyPUHxqfr8IIxuqNqS_cVcNQOYeptwYvdvcT3M3oURoBtE_EE19RyCnGmNOnIsHmZeyq6rZTfiMGXKGnvKp1A9oM37bisP3FVK7CEnEmkxejQEukYcVnLGJlPS9QAbVUv0Ncb-fY4UkF65Mi6VoMRr2vYih5i734uCrX0B1i4sSAQfdp_24cdzHTQfg6VmPL_RjrR5UKDjzHYIn2-uSI86OIjhAN4MM8aEUOnsbPre0XmS8QLXN1EqbaQDmu5LMW2aLFNCFZiES7H8V2d667zVQUmiAGvBhoFcRhg3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=s-8gU0asGd9FBs3qdBVt7xHtHbljf9xa5aOpDNpW4G5dADwPyPUHxqfr8IIxuqNqS_cVcNQOYeptwYvdvcT3M3oURoBtE_EE19RyCnGmNOnIsHmZeyq6rZTfiMGXKGnvKp1A9oM37bisP3FVK7CEnEmkxejQEukYcVnLGJlPS9QAbVUv0Ncb-fY4UkF65Mi6VoMRr2vYih5i734uCrX0B1i4sSAQfdp_24cdzHTQfg6VmPL_RjrR5UKDjzHYIn2-uSI86OIjhAN4MM8aEUOnsbPre0XmS8QLXN1EqbaQDmu5LMW2aLFNCFZiES7H8V2d667zVQUmiAGvBhoFcRhg3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=rVTr1Yx-5KFy59J_QokwQKFDeDHxjA-5IcLnG51e5vozPiBVTyt69JBKqryc2polK8j7QXcRN4dqZQuv1EnrfFR0LV-4FQEhuu-MB3b_beVWAS4G44majHgMZtFWzCWtXoWJG80hBuOn14hB01-o5kAO-yRJ5HoN30201NC2SH_gNWuCsO3OqpEwVpJ8B2GSlS--dL8gTKyXyFhNpr19TfANF1_d1zcnHzyMBalkRFeI1zNaVacsjWWAtEkulw_paZy_xkRFh38VxBGFkL8VwKtj4IIIBZnITv3NmoEt0SXOtnEWUlILaFrbIURyMdY3F61ewYtsBZE21Nz1uexU0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=rVTr1Yx-5KFy59J_QokwQKFDeDHxjA-5IcLnG51e5vozPiBVTyt69JBKqryc2polK8j7QXcRN4dqZQuv1EnrfFR0LV-4FQEhuu-MB3b_beVWAS4G44majHgMZtFWzCWtXoWJG80hBuOn14hB01-o5kAO-yRJ5HoN30201NC2SH_gNWuCsO3OqpEwVpJ8B2GSlS--dL8gTKyXyFhNpr19TfANF1_d1zcnHzyMBalkRFeI1zNaVacsjWWAtEkulw_paZy_xkRFh38VxBGFkL8VwKtj4IIIBZnITv3NmoEt0SXOtnEWUlILaFrbIURyMdY3F61ewYtsBZE21Nz1uexU0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=NF7xGxFIUJVYcq3JERyGltNcWPGLgduLK292S8t2DRWdUHU094wKr6yJ3Yox81ZbLKdxjWgbBzQ66xC93v7aZ_0Dp5vGijcTnZs7QXaWQOdXatHNsLeZpKRTaCDBk0d8aQPts7FIwkIfTvpkvrqG_ZV2vSzqsYqk0v8Ej0hBQd_ubAgR2zTFloo3ruOYlJ-c8qoFy1Txws1VWUCFux2doCXKEQ-32wA8RmSfOqEsBNh7GHf_lQO-NuEv0_ZF1ACbM1ylllRPlYodBqYSuQhN3bHJ_WPNbIsMLLlMxVnmTT8ge-ci6zzUnJ9boT1TnpOOk07jsYUxaKDU1ZWEmrl2kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=NF7xGxFIUJVYcq3JERyGltNcWPGLgduLK292S8t2DRWdUHU094wKr6yJ3Yox81ZbLKdxjWgbBzQ66xC93v7aZ_0Dp5vGijcTnZs7QXaWQOdXatHNsLeZpKRTaCDBk0d8aQPts7FIwkIfTvpkvrqG_ZV2vSzqsYqk0v8Ej0hBQd_ubAgR2zTFloo3ruOYlJ-c8qoFy1Txws1VWUCFux2doCXKEQ-32wA8RmSfOqEsBNh7GHf_lQO-NuEv0_ZF1ACbM1ylllRPlYodBqYSuQhN3bHJ_WPNbIsMLLlMxVnmTT8ge-ci6zzUnJ9boT1TnpOOk07jsYUxaKDU1ZWEmrl2kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=NsuvBRPH0L2m96c5ItdpWabfPyYD58KN1Av4o_JI5sH6olv9Apoim_k_jdk_GtGPK4P_08Kpxbc7E-ss-o5R1KXLXQgeYW5EHIj1Vvf8XtXthHF35cS59fw-1eYDFHuDlA9JwZhXCKOKXzhJNonskczeD35bHko3Ax-Ycgc0Dw4STQkstHwojOTxJb53ssii1uyrxfqbHbNMIJ1QjEwD0yE7-_XsbYfweTHYAwD4KnecaxTpH57Rvo1aXjqCyTiUs3fMwzPLfB-tLza64ETHF7aZA4FBxaItzgoA-VfNvkY7ztIcvTVhxmbB7N8N3GmOym6lVY2w5bObbXESDQ8u7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=NsuvBRPH0L2m96c5ItdpWabfPyYD58KN1Av4o_JI5sH6olv9Apoim_k_jdk_GtGPK4P_08Kpxbc7E-ss-o5R1KXLXQgeYW5EHIj1Vvf8XtXthHF35cS59fw-1eYDFHuDlA9JwZhXCKOKXzhJNonskczeD35bHko3Ax-Ycgc0Dw4STQkstHwojOTxJb53ssii1uyrxfqbHbNMIJ1QjEwD0yE7-_XsbYfweTHYAwD4KnecaxTpH57Rvo1aXjqCyTiUs3fMwzPLfB-tLza64ETHF7aZA4FBxaItzgoA-VfNvkY7ztIcvTVhxmbB7N8N3GmOym6lVY2w5bObbXESDQ8u7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
🇮🇱
بنیامین نتانیاهو، و یسرائیل کاتس، وزیر دفاع اسرائیل با انتشار بیانیه‌ای مشترک از کشف و انهدام یک شبکه زیرزمینی در منطقه «مجدل زون» واقع در جنوب لبنان خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67023" target="_blank">📅 10:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67022">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtH5ZVoYsj5A8cnq6nOqiMhq3Uz_5lz52gdlBTWrqd9TFh_XAireyvcBwoc6RKaH0zBfg9rtivJ7ATavX5pEkdgDia_L1k5x00JhRw9qdoeesWMvPsJ66fJz7pNqYSICqaI-XEhqkBhRg0_dM-VdugsqPfp5D1EbK_ieZCd4T_iDr9yKjljQrEueMkdwYK5jE4WmNeONqzL-81XgXhvk33rFAOT510OwlRlUZPcqntpVkhbbUt4xT8Y-84L01KcWDBfBc7UAlV6Hg-y4G6J7UonEoM0dkZDp-5llAdkuxlvr8zwGcLN6nF-J9eRsV2ZfWyxtM4GYnpUg0-Wjd2ZHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی:
🔴
‏از ۴ تا ۹ ژوئیه (١٣ تا ١٨ تیر)، هم‌زمان با برنامه‌های تبلیغاتی و فریبکارانه رژیم برای دفن بقایای جنایاتکار اعظم، علی خامنه‌ای، و در ششمین ماه خیزش ملی شجاعانه ۱۸ و ۱۹ دی، ایرانیان مهین‌پرست و آزادیخواه در قالب هفته جهانی اقدام برای آزادی ایران، به خیابان‌های سراسر جهان می‌آیند، تا واقعیت ایران را به گوش جهانیان برسانند، و هم‌زمان یاد جاویدنامان انقلاب شیروخورشید ایران را در ششمین ماه کشتارشان گرامی بدارند.
🔴
این کارزار ملی با گردهمایی‌های روز ۴ ژوئیه (۱۳ تیر) در برابر سفارتخانه‌های ایالات متحده در پایتخت‌های جهان آغاز خواهد شد.
🔴
پیام ما به ملت و دولت آمریکا در سالروز استقلال این کشور مشخص است: با تروریست‌ها معامله نکنید! مردم ایران را انتخاب کنید.
🔴
۲۵۰ سال پیش، آمریکا آزادی را برگزید. امروز نیز مردم ایران برای آزادی مبارزه می‌کنند.
🔴
معامله با رژیم جنایتکار جمهوری اسلامی در تضاد با آرمان‌ها و ارزش‌های ایالات متحده و جهان آزاد است.
🔴
هم‌میهنان در داخل کشور نیز می‌توانند با حفظ امنیت و پنهان نگه داشتن هویت خود، از طریق ضبط ویدئو بر مزار جاویدنامان، دیوارنویسی و دیگر روش‌های خلاقانه، پیام‌های مشابهی را خطاب به ملت و دولت آمریکا منتشر کنند.
🔴
برنامه‌های دیگر هفته جهانی اقدام برای آزادی ایران به مرور به اطلاع خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vtmw77kcmeERdXIArjTpVTDJ_apqxr6Cbp5H7kMWLVMBd3iuu4GXyO4cevrUwUmeG3stQDIHltxELREqnYqt7N1arNP6Oydtp4cF-pVfwwh7J7hvAT_Vr0SLc4_xtWz20QzcbpkvRm1QG_RmXk-JUev3KsQYQWxOXSbE69VMXlwd91RiJDbvTsqtwCe8EXTJBpW2qzkYIVThFs33sZarGRhPgZW3Y8Af_TGLsxbHhPUNrkiVi-k625V3-7r7i8OrtS8cjUB-96RZHXzHGK6jShZ5Z6PqhOOzj6ehvLx3YX7F5MAPh9XekFE_c9CSip2yj9RPczmd8L1byu3SC8wtDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67017">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=Tu8G9rWk13n6L5kQAfQfOLczAD1uxtDHpDyDsAUUKttPIXzCynvorCmyQzEPyrBera7JN-Psu6jGJT2fLZqo_2eDFZtMu4zLhfPEqqOsG85xjC1zcTPD54Sy6MOz4hznJJj9_dYXsHedsT94EkwgZ2WJxa2uw2WLs05JQnr5yZKk-AJ3QFu1t0w3FrZp4m0GOP0F57VTJbz9hb9bptUelPZeiMQP4bKrzzKaRYuhI_TaatSe5FUnklgtyczkc9nqVKs6QQj6LfP5VZ80Ijd9ZOGhOJejmANolIWDHa3qiQgy4ifOoR-Q88PY-5Vy6DgY2LDijdgu7SHhvR27uSZM2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=Tu8G9rWk13n6L5kQAfQfOLczAD1uxtDHpDyDsAUUKttPIXzCynvorCmyQzEPyrBera7JN-Psu6jGJT2fLZqo_2eDFZtMu4zLhfPEqqOsG85xjC1zcTPD54Sy6MOz4hznJJj9_dYXsHedsT94EkwgZ2WJxa2uw2WLs05JQnr5yZKk-AJ3QFu1t0w3FrZp4m0GOP0F57VTJbz9hb9bptUelPZeiMQP4bKrzzKaRYuhI_TaatSe5FUnklgtyczkc9nqVKs6QQj6LfP5VZ80Ijd9ZOGhOJejmANolIWDHa3qiQgy4ifOoR-Q88PY-5Vy6DgY2LDijdgu7SHhvR27uSZM2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات هوایی پاکستان به ۳ نقطه در خاک افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67017" target="_blank">📅 01:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67016">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=EGCBRozIlulYYiSxFHmaAoh-Eyo1B7t0psytccE7dUQDrHdEMROokB0AOhPhSiPKrHJFPn637we8WrA_yLvMda3BwPVPw6Aglkqh--xgPRXx19V-83nAc6G2S-55M1VQ9_wojdMcVbZmaeuZHtO1L8egBRwnKaeoHGSkBu5ylTO3EzTMkjUkqhkPpFLlIY-Jwy4Yn1A5UYnGsS2BYFins7qtJrkn6kRvguIBSarhj5AgI04B9QiqFuGbppc2bAFOUwxs1X1SRig0ywmkVWYAsdcBzeskSRgyOEGXdQBcnjI7BALCN59r90ro-49Vo1GlZnHHu0yOMtOBQTSCUORJgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=EGCBRozIlulYYiSxFHmaAoh-Eyo1B7t0psytccE7dUQDrHdEMROokB0AOhPhSiPKrHJFPn637we8WrA_yLvMda3BwPVPw6Aglkqh--xgPRXx19V-83nAc6G2S-55M1VQ9_wojdMcVbZmaeuZHtO1L8egBRwnKaeoHGSkBu5ylTO3EzTMkjUkqhkPpFLlIY-Jwy4Yn1A5UYnGsS2BYFins7qtJrkn6kRvguIBSarhj5AgI04B9QiqFuGbppc2bAFOUwxs1X1SRig0ywmkVWYAsdcBzeskSRgyOEGXdQBcnjI7BALCN59r90ro-49Vo1GlZnHHu0yOMtOBQTSCUORJgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMj3Aygjpa2MDviDa1U6P_stKE-X_Uc5iJDCYD4nUJvqBmKRSZvKF3a56l_bHf8upsY4ytUNFuW2ZDkIwivvRoZdO1cG3LfEN3UXv2MWhNT9Ah1JMzzW5dpKygKrTlTNclMNUFXUgVFUrhPNTpslnKYa1KTE6MN1h86L_8G2SGf7kIefllGi5KIiHd5M-343eujJlPwHVYY8JKzyu1Ce9BEP6KjTArvqe8qw2kO5oa3UJ-C5GUDq3BRnTZxAtGiaqu-0U36rx8vUlCIyOXvm1YdoQGKra-lQhj2iYyLpkhhRMFedkgjKmY02yVLKLtK8ni5WT0vZzKTHDwl3-01JsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آکسیوس:
به گفته یک مقام ارشد آمریکایی، ایالات متحده و ایران توافق کردند که حمله به یکدیگر را متوقف کنند، در حالی که دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر برای حل اختلاف خود بر سر تنگه هرمز دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67015" target="_blank">📅 00:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67014">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=Iqn1QKMjYW3ewyNy86bu3V_hG6Z92rMW95IvZkgx4pCo_F0grJEuMxwVKjKNFM8SGerGTkc20dQeUAPQUqfdYb0vdwb2D41Cx3uabsW4K3Zhv2UwxM9wwXYD8FY8X6naGYeWCQ-lryS0KrOUkIW6GE0ty4dKMJiMCNJbHUIeM4JihRdxf0LIlTUuHuMg_PrJdMbre7uNwM7vVcKixFcCghlUCdz8w7VrndvtozOgpP4Fu-rjxb7P7I-DmJrtmg9JzSRDuyum8kZrn3MqTK7UmRoiJ2q7aQOp3Cg3IQd6jVYC8bV49rHxRWPCTIqTRDZk-AIITYP7ubyxvntyabbckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=Iqn1QKMjYW3ewyNy86bu3V_hG6Z92rMW95IvZkgx4pCo_F0grJEuMxwVKjKNFM8SGerGTkc20dQeUAPQUqfdYb0vdwb2D41Cx3uabsW4K3Zhv2UwxM9wwXYD8FY8X6naGYeWCQ-lryS0KrOUkIW6GE0ty4dKMJiMCNJbHUIeM4JihRdxf0LIlTUuHuMg_PrJdMbre7uNwM7vVcKixFcCghlUCdz8w7VrndvtozOgpP4Fu-rjxb7P7I-DmJrtmg9JzSRDuyum8kZrn3MqTK7UmRoiJ2q7aQOp3Cg3IQd6jVYC8bV49rHxRWPCTIqTRDZk-AIITYP7ubyxvntyabbckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دختره رفته پیش دکتر، یه تیکه نبات تو واژنش گیر کرده! دکتره میگه این چیه؟؟
میگه ما یه رسمی داریم، بعدِ عقد نبات میذاریم داخل واژن‌مون، بعدش میندازیم تو چایی که داماد بخوره. چون با اینکار زندگی شیرین میشه!
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67014" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67013">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=a26pnjacOUu4vzFSmMChNgUTEMWV5IyxBjoE480f2OuP6A9uqmQGuHZBJmpxXKJaNcxSsmUieQiyaHQqv7ZcHDUt9zP6zs7QjRqJLfCaqAGco96OPLSN191YI1YFeiUr98tau5n2tf5C1r7Ad4ob0rfrz21yLHlv7D9jFvKyFG3jGcZejaRqPd5Gh840nZqIh8p-B8xvcIaftwHtZwES6QQTWhiV9AT0sP1ZIuYV_kr7QJQKlGlyo1RAUgDCg6y2CdYme7-UsCtjk_O-taAFDhrLN4JlfAEfmaGr6WDfVoIkUvovs1UnitffJPJx5jnyUUY8SekTrqEbZYmSG3L4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=a26pnjacOUu4vzFSmMChNgUTEMWV5IyxBjoE480f2OuP6A9uqmQGuHZBJmpxXKJaNcxSsmUieQiyaHQqv7ZcHDUt9zP6zs7QjRqJLfCaqAGco96OPLSN191YI1YFeiUr98tau5n2tf5C1r7Ad4ob0rfrz21yLHlv7D9jFvKyFG3jGcZejaRqPd5Gh840nZqIh8p-B8xvcIaftwHtZwES6QQTWhiV9AT0sP1ZIuYV_kr7QJQKlGlyo1RAUgDCg6y2CdYme7-UsCtjk_O-taAFDhrLN4JlfAEfmaGr6WDfVoIkUvovs1UnitffJPJx5jnyUUY8SekTrqEbZYmSG3L4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDEJ3vjvRp-o52DaV5Y-FzC9Nx1ybRj7jP0BpUYd_WOypzEAsuQdgHluRkzmBVmuikbevbjKPfqyvJ67J3LwrzkPmekmQNjGBNmgSy3rVCDs9DYGqySVkhxtPEF758hQpJ-2EcVhgIZCClS3ahDjlmCYzb39xaM9h8eIUrTB22408xeUDacUJc07R4HDgyCqrA-DIe_t_EhOn4h_X6RzLslHcnJr_K808ACYQ2sm9xoUBrAMuxGQsSL1UEkH-sO2pYIKGl7B6UxoCPLfSOkbu-5NE6wVs5kjMyuifbywkg66AwktMexrL_qhn9k2IT0wqSmZUruFDbN5jGsmxApa5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGZpvTVX7vVeMwgZrKcwaGX48rzteE4ly8IBC52tOmcP9RFXbEru8i-DnIdOYTOtKh9RHj5jycWjEZOgJkH6XAMx22wY13Xc77qfrTWCckLBPpiOhqKJBCEcfKn-MZCAgIpq6TeQBEacljmPbk6j6rA7It_kXIAzvwVMqA8901xxAGSZFWTSnHJFLQHIu8-wp5_bsysfmwB6VOJ11oI8hC1cD894B5uAm8WM8wY2vrg0s2_W66cR2wce_Eesnr88tfFCbW0OLq0b63PniCbAG7UX0gJxw0OuvD-Jr0jkBZczjRzQVSakAb_e6D4Duvzv_e9uNc25udqbCRP53_Ua4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67009">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FSLeHBTqz9goYcZAfCu29rSzCT-IP6tx_Q0V5hnSMhLOPC9aV38GYZIHNNtvlyNtQ6K5HaORvgl-EiUKnfI7_Xss8TN-vnzO-eYhxBlpmxEd25NA1U2RTNQxBUbKleYAJykDQ67ckEcXMkIXUV0r8PDygF7pKjv0g9CqDjY098RP44p_rrdcyCvwu5S2eXPWEgew-G5FiiEFAm6dy-1h1t6izHGZpSoTnrcPSeaN9_i04nHfw9APpRiDj_1iyNHi4RG245kMVEaasQuPHr-3pyRBltH4OKusGtjUZQbK0cL_4u-j1i8kiMmvTE3Qe-2R12G2mkzZFn3PvauFynJf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=AA1_beLLudBUbbx24acrNBYvhs1FyHpC8SEIM9hIpQwmHK4w_fCpC8tZ5gj9P4LGUUgIL0JIVx68EFuXKr8WdW_vZUGUN4uUcnki-0PqZDmxIXSgLxkLzPl1hnbjYATPfF7_n4PFDeCu5NlTKRoF_o4lZIvH5iBIQc9Qb_2dsjQmS23BVpEUtbr0DnHZtRIgv1KhKOamYEXZ7b2vR7GIWI2IiW3TN3n6d0JN9AhUq2UB3Z3eJiXIz7m3GZoIlrLua8waoVzlibfGosbVji0q53TuNm1Vb0zTmQecVkFWw_QCr6aelcEBRON9WBqQ9F8npsNiIy5TRxb4gpnI5Mxrfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=AA1_beLLudBUbbx24acrNBYvhs1FyHpC8SEIM9hIpQwmHK4w_fCpC8tZ5gj9P4LGUUgIL0JIVx68EFuXKr8WdW_vZUGUN4uUcnki-0PqZDmxIXSgLxkLzPl1hnbjYATPfF7_n4PFDeCu5NlTKRoF_o4lZIvH5iBIQc9Qb_2dsjQmS23BVpEUtbr0DnHZtRIgv1KhKOamYEXZ7b2vR7GIWI2IiW3TN3n6d0JN9AhUq2UB3Z3eJiXIz7m3GZoIlrLua8waoVzlibfGosbVji0q53TuNm1Vb0zTmQecVkFWw_QCr6aelcEBRON9WBqQ9F8npsNiIy5TRxb4gpnI5Mxrfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری ندارم که حیوون خونگی این آقا مار کبراست! مشتی چطوری مار کبرارو قانع کردی چایی بخوره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67009" target="_blank">📅 22:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXHkTmTDvVQ5Ff5RBI7aTmm8DYFS_glCPCFhqNHkche7ttGo30pD6b9jHqfGfKu9YT2nwFqEpG-BmVQkUrf2ZPcHScdJOMMNfcOwG2uomjqLuIqidaABwrcRfzyxYexMTaMhv2ryq9USami9A2duo1PC6etnafgqqck9DUCeKO2TMixopLTKH_oXQ6pRKFlcrzgspJnoEGO_D-W3xvcvjOc3FFj1NMIFdraKta22vXijDh8sHf0Rl-h7_0UcMbppLQ2z6_Y-uxmViTC9azMthwCSYYGyYk0tz7Lz6ILTOyMFpJxlcLHyZopd-yZCmR5y6d-ujHfQXLg4I5_C16DNfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK7Nf34VmHSaAfG0lwqUBWiHW9U2mdfatiRtfKRhKggskjx4I9gyONvu3i5g8_cg39rt12brRR7GZS6vhTCCInK7xaRjAlYzEus7wqXRE77WLQNryVq7URi12Hv2UKI6uNINHJHWeYee-hFV8lukOH8uZ21-w6MsjNHKCKv4flaDBUwl-DFrw7xoXxlR1QflAdVfXSiPqBywZPW9OYBv57Pc1SeFks-injWIuIxGoefse5q8FBZWxh4Pws11QIKph40OovX1QS6v0bVZErAxmHfqiAD9xv2acJIv98dh_ol8TWVK1RyUNaE4nWuFh_cZL4oXFGes_Ep0zYiV6GaDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=n_jwuu9HmzQGDwqqDor08Kmqj1pZfIrTBZiN4BuT4D2aY83cq3JZ2tmYtwRftbU3py0et7QYAHZrs7FQpoqzYOYJhpe3BwdZ65mPiLEVlGoQyWXSfk-n_0uuxi9Jg55l4Nh1M0uF6_F7PZ57wF4PAsoWcfvCoMD4U4GTsx81rqGKMTYdj9bP8K5wRD1NIK75ohXnLUS3xwq3d6wYHFr63oCjXvHHxsP8GxEnpammJN5Td7pNfJhahGNkellH7T-Y99b0NH9bj8OL-eTVuYgMU4ktttmLqJKvGa2LUB1W02TQizKNWrRx1cU_95ST2TjaagvH6xivBNT9WXlJPMdh5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=n_jwuu9HmzQGDwqqDor08Kmqj1pZfIrTBZiN4BuT4D2aY83cq3JZ2tmYtwRftbU3py0et7QYAHZrs7FQpoqzYOYJhpe3BwdZ65mPiLEVlGoQyWXSfk-n_0uuxi9Jg55l4Nh1M0uF6_F7PZ57wF4PAsoWcfvCoMD4U4GTsx81rqGKMTYdj9bP8K5wRD1NIK75ohXnLUS3xwq3d6wYHFr63oCjXvHHxsP8GxEnpammJN5Td7pNfJhahGNkellH7T-Y99b0NH9bj8OL-eTVuYgMU4ktttmLqJKvGa2LUB1W02TQizKNWrRx1cU_95ST2TjaagvH6xivBNT9WXlJPMdh5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=ZvDSHiMJkMasltcDWnNLv1PcmhWQqEex8OIGnLuubkHcIzXQGDc0mcNjruRArKukAtGigeKLuxoJralIj73K-PBPqG_3Om-oHfEe0OZzHVIOWZrzCp6EOrE9EHe0r4YCJXaRZ6ax6EiAM_ZuIqmgSheEUQFS6qdXz0_cJ6Q9p75Tgdvc8D8-gOoPixddKT3noxCHhDQl6uXuTSPmm7BlIwK272QSl82KSsijIC7piNll3OgopF07w3kAZrnQ9Xd3_kHy2b1QiliImfbra9XtyyAQ9QIPcsdK9oCy5wT8yT8BS-RTg0bM8-2pzTYQ2-G0VhHsbrhe0oqWwUVRCx7p6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=ZvDSHiMJkMasltcDWnNLv1PcmhWQqEex8OIGnLuubkHcIzXQGDc0mcNjruRArKukAtGigeKLuxoJralIj73K-PBPqG_3Om-oHfEe0OZzHVIOWZrzCp6EOrE9EHe0r4YCJXaRZ6ax6EiAM_ZuIqmgSheEUQFS6qdXz0_cJ6Q9p75Tgdvc8D8-gOoPixddKT3noxCHhDQl6uXuTSPmm7BlIwK272QSl82KSsijIC7piNll3OgopF07w3kAZrnQ9Xd3_kHy2b1QiliImfbra9XtyyAQ9QIPcsdK9oCy5wT8yT8BS-RTg0bM8-2pzTYQ2-G0VhHsbrhe0oqWwUVRCx7p6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سنتکام:
ملوانان آمریکایی سوار بر ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش در حال انجام عملیات پروازی در حین عبور از دریای عرب هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=uGUFQKzPlYzX9TrlGgBh0IzfCx7ox_pRXkLWf3DXYenVHxvAQMnJRzTXFJkB-tngmdCM80u78nPKXq1zvb-M4hDqaYtCvD3S00eomtYJKxK2dN_-WBiwSmXinPeMHovFZuk5CJyGerSF4OWAKee8a5UX1aBGaf-Fxkeyqm5Jx3mRAqBEtdoq-LfIMxJZ5pzsEJ6CD0BYpoQRjENPGBzGAAPAHvJzGgrytCZ-wsVCuUX3nIQns91zrKPBlNVkJZS2nCiNu5SCKZg_z8sJX2JFD31rWgPNDwhF2UcH7DjsIwAdtb2bIXqB6xedRSuUs0MxoiUIS5Kyhk95pJWN5JHVEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=uGUFQKzPlYzX9TrlGgBh0IzfCx7ox_pRXkLWf3DXYenVHxvAQMnJRzTXFJkB-tngmdCM80u78nPKXq1zvb-M4hDqaYtCvD3S00eomtYJKxK2dN_-WBiwSmXinPeMHovFZuk5CJyGerSF4OWAKee8a5UX1aBGaf-Fxkeyqm5Jx3mRAqBEtdoq-LfIMxJZ5pzsEJ6CD0BYpoQRjENPGBzGAAPAHvJzGgrytCZ-wsVCuUX3nIQns91zrKPBlNVkJZS2nCiNu5SCKZg_z8sJX2JFD31rWgPNDwhF2UcH7DjsIwAdtb2bIXqB6xedRSuUs0MxoiUIS5Kyhk95pJWN5JHVEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=VDcyXfN0H6ADdyDTGbivYEX0qimCwSNVfX583fpntIVRUcLrOgT8D6JqGoZt7Z5z5epMH7Gvg1YKqXy5S3LyV9cTel6cLfK5npKrDAS0LR-DLIWJ8awH9BfaNhuo-vu0tDRsesysu9svwv4ql0_E4lExo17MVhjoNNWh9-rERVmsImWfc4dBPzoL-Asvo7cufpIU5yRHePUtAa56bDyjcFiaYmFzDRtAOpyKwZeMigQI47wNdGsWzHnOhHJpfvOw6fgwm5f7ebvlSsXhEsjbTITjaObnKUUyVN9q7bBrh0rFoBOgDepnd7pi7h22UIv_OdF4p66N3cTIvM_YSTsnwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=VDcyXfN0H6ADdyDTGbivYEX0qimCwSNVfX583fpntIVRUcLrOgT8D6JqGoZt7Z5z5epMH7Gvg1YKqXy5S3LyV9cTel6cLfK5npKrDAS0LR-DLIWJ8awH9BfaNhuo-vu0tDRsesysu9svwv4ql0_E4lExo17MVhjoNNWh9-rERVmsImWfc4dBPzoL-Asvo7cufpIU5yRHePUtAa56bDyjcFiaYmFzDRtAOpyKwZeMigQI47wNdGsWzHnOhHJpfvOw6fgwm5f7ebvlSsXhEsjbTITjaObnKUUyVN9q7bBrh0rFoBOgDepnd7pi7h22UIv_OdF4p66N3cTIvM_YSTsnwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTkbeMGKxNEyyh2lpEKa2MZ7NOo68ajA4f2Yk04v6F82DM2Ijnvv5_MaaGiWNt6iNtwWKArXv6MWd-5hIOQ55bIfcjR77ip2uhV4kDXT69T9oiZqFygmPgD4-q9ARl6HWB02qG_8hHHJSdbmAGzQ4wj-tmIV4AU_7msdcFmXoXsdS047wqaa_LkOhA3Bvj170RL2Ze4-oWI9qluK-3DJfVDePDCGd0XX-i7XC2AypdW4KHH6m_3MyYRgVKcZvp_OH2sQJV7_eEYQI6F923c1mkjQZj2PEiXfgXS-XC-FfTuoJuvP53p0HmslcW6AVxEbD2oS43EMxTJ-8Nb46ie7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=jOddNvHeZJ8WljQSIy-pLo0o8zQFnv5l62f-nE4r3ue98lnFy3gVk-Z6qwiBfwg0f-EUKL92g38bpcCB2PDMpt46nf8nf6HwPPxA1nTvsdJWxMsihVIEDNMTqoM96HP5YBzuHRAtmz1FYRjBVFuNujf-FSDpLj8FY4qBCR6HqzPBZxHePErft0r-SCrdJlYircLtKenCvR4SybdqbESwO7MKF6bBMDnemq5qfYVUQJtQQfLvC7GAYTVjqw4WTJsOZZGaWT_JKi_BV1XQjPwPGL5J8XGI9HGvfFshUqLADvHAiqyNFFeN4rYEz_yx5etlbFq5BJEL1o1XuIGDJEunxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=jOddNvHeZJ8WljQSIy-pLo0o8zQFnv5l62f-nE4r3ue98lnFy3gVk-Z6qwiBfwg0f-EUKL92g38bpcCB2PDMpt46nf8nf6HwPPxA1nTvsdJWxMsihVIEDNMTqoM96HP5YBzuHRAtmz1FYRjBVFuNujf-FSDpLj8FY4qBCR6HqzPBZxHePErft0r-SCrdJlYircLtKenCvR4SybdqbESwO7MKF6bBMDnemq5qfYVUQJtQQfLvC7GAYTVjqw4WTJsOZZGaWT_JKi_BV1XQjPwPGL5J8XGI9HGvfFshUqLADvHAiqyNFFeN4rYEz_yx5etlbFq5BJEL1o1XuIGDJEunxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:«بر اساس تفاهم‌نامه، تنگه هرمز ظرف ۳۰ روز و تحت سازوکار مدیریتی مورد تصویب ایران، پس از رفع موانع از سوی جمهوری اسلامی ایران، به ظرفیت عملیاتی پیش از جنگ بازخواهد گشت.
🔴
این ترتیبات هم‌اکنون در حال اجراست و مسئولیت کامل آن صرفاً بر عهده جمهوری اسلامی ایران است. هیچ نهاد یا کشور دیگری در این زمینه مسئولیتی ندارد.
🔴
مطابق تفاهم‌نامه امضاشده میان ایران و ایالات متحده، هرگونه مداخله در این موضوع یا هرگونه تلاش برای ایجاد سازوکارهای جدید یا جداگانه، غیر از ترتیباتی که اکنون از سوی جمهوری اسلامی ایران در حال اجراست، تنها موجب پیچیده‌تر شدن وضعیت، به تأخیر افتادن بازگشایی تنگه هرمز و افزایش تنش‌ها خواهد شد.
🔴
همان‌گونه که طی دو شب گذشته شاهد بودیم، رخدادهای تنگه هرمز از پیش به افزایش تنش‌ها و رویارویی‌ها دامن زده است.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز یا در ترتیباتی که جمهوری اسلامی ایران برای بازگشایی آن در حال اجرا دارد، مداخله نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=XkJeyzSRU0KBqU9ittZ6UZyRfRV3nFcRu-6U67M1dfJXedbEtWyosdluDac5y_Qi-05uNJQOfcNzl8uDfLTY0ODgtcv2sRqV7dY93DcsTMDfhr0sqzlHd_oTjAJihhc5xXLmGz1KddE1g-JIk-YqRrpS09LUhbOG6LByq2Z8DP7quYjG4iDXJGludhjWLa-fBxhOg6QqMpSNdU2ZT1BJzn46lFyg1fGYVMniyvQkNpwoqRjpIR5S_j5Jriq--7Fn0nfP5-3gUEBoZ8vsFIhLUPQiJDXiKIDLLoScqr7TVw6MrLQdoFR3zTA0fzoKZpgVhsAZ_bEBKjK1TYivJHlpgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=XkJeyzSRU0KBqU9ittZ6UZyRfRV3nFcRu-6U67M1dfJXedbEtWyosdluDac5y_Qi-05uNJQOfcNzl8uDfLTY0ODgtcv2sRqV7dY93DcsTMDfhr0sqzlHd_oTjAJihhc5xXLmGz1KddE1g-JIk-YqRrpS09LUhbOG6LByq2Z8DP7quYjG4iDXJGludhjWLa-fBxhOg6QqMpSNdU2ZT1BJzn46lFyg1fGYVMniyvQkNpwoqRjpIR5S_j5Jriq--7Fn0nfP5-3gUEBoZ8vsFIhLUPQiJDXiKIDLLoScqr7TVw6MrLQdoFR3zTA0fzoKZpgVhsAZ_bEBKjK1TYivJHlpgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو:
می‌خواهم به شما یادآوری کنم که در لبنان چه بود. حزب‌الله ۱۵۰٬۰۰۰ موشک و راکت داشت. و ما حدود ۹۰٪ از این انبار عظیم را از بین بردیم.
ما آنها را با بیپرها شوکه کردیم، نصرالله را از بین بردیم، فرماندهان نیروی رضوان را کشتیم.
فقط در دو هفته گذشته بیش از ۲۰۰ تروریست را کشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVz9aqnt2GyzVsY8C25AZTNRMwJIeDWXg1uGgNHA1atxMZlkLQlklJHLrlQwF0pyArnXDMHBJ4O-_yFAjmby0yICxgLqhhiL_9BnXSDYszEAJl89aWmQNvg1GiESzp7fLXG9J_Pb_RgBAUjgAqtJzECpTpphd-sKcpOTZ0vGVbvhtwfsKtVbf0vnHUVI6AqXdvJzIZrQ2JD1KBJhHu5QHGXRY_SUeLM9930K_pSKHqgcmNhnIuzdsh2-ApTHbMff_u9Oz3w0N0wVuKCRe7tamsgogen-x64gVfYCWE62UQClqtBs94VRORhnpAi8U4AoVoCpb-qZxMep87YxUIZReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MennO_-ZCJnegmSrHebDrXlbU3AVdXrQWOhxcsLJDaDRUel5aYTWUDk-vDhRtN_Ew27YqSwcqsGXYm98ITezHdMG7b2zp63Ks0QZFKAArNo-i3CxQ6efJQhYnYTGB_ewDqeYlaJ9aOb-EWlaAZ8Af0Tn8FX6G4q8eKklLZx5hEgdqzPeykLoWUdpXwFeOcoQXWfmpExavjMclrlNkcVJPdeSJJ6YWPEATuNbqUAOfpGAyb7xfdmcIQUEqfPSXSJZrQ2gktL8o3KyYikEwgEeaCER3fbHSTgdzs3ONSLz5Q4urKJ8seBlOzdk_5VEyfz3AdS-vknKEADp_0Wow1dJpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CyO47UpDnHDgKWoBX--Lm3TCaf5SRQKs9pBhPYEGyWOrqvfA3X__VibX1fIbF_ZMVr7OPe3rFWoMsH8A-Bc7sdtl9wuBSxeOKqIX06bUZwhTEpFkN6UkefoqSX5hGMGhwnuOQPNO8Y-dYteWTVHhXzZweisxS8xe5zttckBkhvD0bC2tXNdq8_Y-TaKadvMrXW4iK60cpBT7Pmuvj0Obf25iwPj2nyH9suXROfe6O8z9b4TXj0mAcBKDTCWRdbP-0hYVnt7mCUhpYKuQ610CBG7Qxriz5X5GrJv6UE1g8Qhgw8Hv421u83CHpbeHFaVo6Kr4WasN587bymCMz2uGUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=a6eNYIlxJYJEK0JfEHyUgP-0rUnwYtZVQ_kquDDXZ_egpiwqDU-qjiHknwxJvUWZtdVgK7azRICuEEHclfNL79THh3-cuT-7L5ojKEUbumaZwkLUMSVHLucBX9JIMNlhiN1-sz_wiEDsanJETyfGXJQg9tsPMzLP3CTfJbGWHTMV-fUtC2R2Ydz277DIT44ePUZI39HqZQiOmAy7HFFEklCxs_0j8WeM-wZHfC8-m0akB5i-SS2yiPDOGae5tDVIgTsFC8uD31VSFno_fFPPZCNeDAb3le4FPq3UMST36s_LNFtNgjDsumvoGTH6fHF-1TwGgEJzDWFDIpiNg4r20Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=a6eNYIlxJYJEK0JfEHyUgP-0rUnwYtZVQ_kquDDXZ_egpiwqDU-qjiHknwxJvUWZtdVgK7azRICuEEHclfNL79THh3-cuT-7L5ojKEUbumaZwkLUMSVHLucBX9JIMNlhiN1-sz_wiEDsanJETyfGXJQg9tsPMzLP3CTfJbGWHTMV-fUtC2R2Ydz277DIT44ePUZI39HqZQiOmAy7HFFEklCxs_0j8WeM-wZHfC8-m0akB5i-SS2yiPDOGae5tDVIgTsFC8uD31VSFno_fFPPZCNeDAb3le4FPq3UMST36s_LNFtNgjDsumvoGTH6fHF-1TwGgEJzDWFDIpiNg4r20Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیاین یه نگاهی بندازیم ببینیم چه بلایی سر تیم به‌ظاهر ملی اومد؛ قبلش بریم سراغ مصاحبه های بازیکنان این تیم تو تجمعات شبانه حکومتی‌ها:
شجاع خلیل زاده :
حسم نسبت به رهبر شهید ؟ افتخار ایران ؛ گل اگه زدم به رهبر و شهدا تقدیم میکنم
رهبر عزیزمون شهید شد همون چیزی که خودش میخواست بهش رسید
گل بزنم به  رهبر شهیدم تقدیم میکنم و ما فوتبالیست ها همه دوستش داشتیم ، افتخار نداشتم با رهبر دیدار داشته باشم و دوستش دارم
حسین کنعانی :
حسم نسبت به سید مجید نقطه زن ؟ بزن که خوب میزنی ،حسم نسبت به رهبر ؟ بزرگی
رامین رضاییان :
شهادت رهبر انقلاب رو تسلیت میگم تو تیم ملی به عنوان سرباز برای کشورم می جنگم
اتفاقات داخل ایران { دی ماه } به خودمون ربط داره و به خارجیا ربطی نداره
علیرضا بیرانوند:
چه بهتر که تو آمریکا بازی کنیم می‌تونیم تو اون کشور برای اولین بار در تاریخ فوتبال کشورمون به دور بعد جام  جهانی صعود کنیم
روزبه چشمی :
حسم به رهبر شهید ؟ بزرگ همه مردم ایران !
سعادت دیدار با رهبر عزیزمون نداشتیم ولی بزرگ همه مردم بودن و این راهی که مردم دارن میرن ادامه راه ایشونه
و بعد از این اظهار نظر ها بریم سراغ دیدن نتایج، تو بازی اول از ضعیف ترین تیم جام یعنی نیوزیلند دوبار عقب افتادن و در نهایت با سختی یک امتیاز کسب کردند، تو بازی دوم فقط چند سانتی‌متر از باسن مهدی طارمی تو آفساید بود و گلش مقابل بلژیک مردود شد، تو بازی سوم بازم همون طارمی پنالتی رو خراب کرد و در دقیقه ۹۳ شجاع خلیل‌زاده گل زد و خوشحالی‌ای کرد که در تمام جهان سوژه شد، ولی بعد از چند ثانیه کل دنیا روی سرش خراب شد چون فقط دستش ۵ سانتی‌متر تو آفساید بود، نکته جالب اینه که شجاع گفته بود گلم رو تقدیم به رهبر جمهوری اسلامی خواهم کرد
دقت کنید برای اولین بار در تاریخ این جام جهانی ۴۸ تیمی بود و ۳۲ تیم صعود می‌کنند، یعنی در واقع به اندازه‌ی همه‌ی تیم های حاضر در جام های جهانی قبلی، این بار تیم‌ها به دور بعد صعود می‌کردند (علاوه بر تیم های اول و دوم، هشت تیم سوم هم صعود می‌کنه) و بعد از مساوی با مصر، سه شرط برای صعود تیم به‌ظاهر ملی وجود داشت:
۱.بردغنا
۲.نباختن ازبکستان
۳.مساوی نشدن بازی الجزایر و اتریش
ولی در کمال تعجب یک معجزه رخ داد، غنا نبرد، ازبکستان باخت، و در دقیقه ۹۴ بازی الجزایر، ج.ا صعود کرد و در دقیقه ۹۵ با گل اتریش، ج.ا حذف شد، این واقعا یکی از بزرگترین تحقیر های تاریخ بود
...
می‌بینم یک سری افراد با توجیه های احمقانه می‌گن اینا مجبورن و فلان، نه عزیزان دارین اشباه می‌کنید، میانگین سنی این بازیکنا بالای سی ساله و عملا فوتبالشون تموم شده و رسیدن به آخر خط، اینا فقط دنبال باج حکومتی‌ان و حکومت به عنوان حق‌السکوت بهشون مجوز واردات خودروی لوکس می‌ده که می‌تونن ۱۰۰ میلیارد ازش سود کنن، یعنی عملا یک رانت ۵۷۰ هزار دلاری هر شخص بابت حق‌السکوت دریافت می‌کنه، جالبه که تیم های بزرگ جهان مثل آلمان و اسپانیا حتی اگه تیمشون قهرمان هم بشه مبلغ کمتری رو می‌دن به بازیکنا (۴۳۰ هزار دلار)، خلاصه که جام جهانی بزرگترین رویداد برای شنیدن صدای مردم مظلومه، همونطور که تو سال ۱۹۷۸ کاراسکوسا کاپیتان آرژانتین بخاطر جنایت های حکومتش از تیم ملی استعفا داد و...
ودرآخر، از اون ضربه‌ی تیر دقیقه ی ۱۲۰ جهانبخش تو جام ملت ها، تا پنالتی‌ای که طارمی خراب، تا پنج سانتی که شجاع تو آفساید بود، از پنج سانتی که بازیکن کنگو جلو ازبکستان تو آفساید نبود، از پرچم کرنر تو بازی الجزایر، از گل دقیقه ۹۴ الجزایر تا گل دقیقه ۹۵ اتریش، هیچکدوم اتفاقی نبود و همشون کارما بود، کارمای حرفایی که نباید می‌زدین و زدین، کارمای کارایی که نباید می‌کردین و کردین، اینا همه صداهای مردم و آه‌ناله هاشون تو گوشتونه، مردمی که دلشون باهاتون صاف نیست، حالا هی بیاین بگید تبانی بود، نه تبانی نبود، اون بالاسری خواست تا شما به عنوان بی‌غیرت ترین و بی‌شرف ترین نسل تاریخ ایران با حقارت‌آمیز ترین نحوه‌ی تاریخ از جام جهانی حذف بشید :)
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fw36zOpXYzSr-ombTxy-Rlv64Q1-M2my9J3900dFREiNmbtBheV12-BO9N9EW3iaDdHve9ZLqs7zBsjX4Oee9Z_L-ad_Qe8q0srSGCUc0nUFVSBU6qWWhfz5c42jfMspUHHgx89tfZ59XjT-1BVjWDxMqC0kqniX7J61hmbkRsHgww5eXPJqZrqnuHFEUHhm0cHYRVZcj2mCVi0NbUbP34SJHQFJRE5-W3kSAINZvzEobjQe4M1V1rIB7os6LEOLjJ_Cp4giySDKGt2a-3mQSg6WIWs6P9IUIHtVY6VlWPmcsTiYZepL8Ex3P_np_jcavedr5DBDIC5bixbswmCLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572c331047.mp4?token=LxKVTLoo4UWTsoA1cG5nKbCN2LDkabwqbWVuUkfrtHZRgspEOFriIb53ohFInG1HThWi334jxDeiUmmmNpK_3HLDKG0kP08Q0IHKV_SS-3IX5L5Rv0Dk_3uxmtFcSs57TJTf4DX3JNB3_Jo_81AhqTaTBm-VwNxEgMUJgq5AOvzOEJ5hPKtuuXHnC9EmfCo1HKBS-al5aAL5tmevvFlAg1kktO6NRi5dp4U62OacRvUTPPpYZleyxGpqhDzbIVKvKOWYbdsAFRmdFXIYuyEGLEGzU9P1FugtItwc7AC__RvwxHpIYsvL4pu5l4TO_QoqtQoY7MKtaSxIpp1GKuCImA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572c331047.mp4?token=LxKVTLoo4UWTsoA1cG5nKbCN2LDkabwqbWVuUkfrtHZRgspEOFriIb53ohFInG1HThWi334jxDeiUmmmNpK_3HLDKG0kP08Q0IHKV_SS-3IX5L5Rv0Dk_3uxmtFcSs57TJTf4DX3JNB3_Jo_81AhqTaTBm-VwNxEgMUJgq5AOvzOEJ5hPKtuuXHnC9EmfCo1HKBS-al5aAL5tmevvFlAg1kktO6NRi5dp4U62OacRvUTPPpYZleyxGpqhDzbIVKvKOWYbdsAFRmdFXIYuyEGLEGzU9P1FugtItwc7AC__RvwxHpIYsvL4pu5l4TO_QoqtQoY7MKtaSxIpp1GKuCImA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=S0oKJaDjFsLjZsmbvMZb43IT-ZzGzdlVYoZ4E9KPdnyPYp7RE9m5O8aMgHv1KJUTuOZiOqHQtsiS-lAoYq0U3c3QcqD5Y7wnT1RDkkieQLxhk1mJv09pQZ5UgiwBAlMX6MI0NvC7ln7lw-4nSlrRZzQpx3NzZNV06OogjYKN6MIDxndWFN0Bt8lRcKxU1g1AfDOipShnX8I-MexegUSjLCMeX2P8yHLTP4fxHVPTUOrPQSP6LdOm-V7vZXNVc3n7hCXsfvCob4TwMR9IcMcjyXZr1ZxHMkaimQe9T_4-NnlxY_PWIyc5L_ZFegUsBDTb0aWeoVLKLLbUALXH4Sn6FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=S0oKJaDjFsLjZsmbvMZb43IT-ZzGzdlVYoZ4E9KPdnyPYp7RE9m5O8aMgHv1KJUTuOZiOqHQtsiS-lAoYq0U3c3QcqD5Y7wnT1RDkkieQLxhk1mJv09pQZ5UgiwBAlMX6MI0NvC7ln7lw-4nSlrRZzQpx3NzZNV06OogjYKN6MIDxndWFN0Bt8lRcKxU1g1AfDOipShnX8I-MexegUSjLCMeX2P8yHLTP4fxHVPTUOrPQSP6LdOm-V7vZXNVc3n7hCXsfvCob4TwMR9IcMcjyXZr1ZxHMkaimQe9T_4-NnlxY_PWIyc5L_ZFegUsBDTb0aWeoVLKLLbUALXH4Sn6FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی دیشب:
ایران با این احتمالات قطعا صعود میکنه اگه هر ۳ تا بازی طوری رقم بخوره که ایران حذف بشه؛
فقط معنیش اینه که خدا خواسته این تیمو بزنه و تنبیه کنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=lrG1_ih8utrUuZ9XAdxGvp_0Blg-z---ds2CBbsHZIsKGQsHzIwdCoz6lRUddk33LXFEkyD2PfDx-VbfjJgxWFeHl1x-4n90m6gmy6JO3c4iKBohl1PCZiK8eMLiB4yT03icSETyMRBcD0bJeKlYF7zCLFyb5289Yi_nxRxqfEJtS-MSlm-JzE01BKGt7PGxW3SJEJk7p3W_o3FwtqQje5gmEfGL-Zc-X4Vy_0gre9YGdMcShPpLFYfEGaUJJKHuZm608gKeVlbGZPBErFYVXymM3iyPiwwROanklS1YBPDkt8_a0e94A8PEYaqNkDhwq99M12I-P255Fryz-U2HTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=lrG1_ih8utrUuZ9XAdxGvp_0Blg-z---ds2CBbsHZIsKGQsHzIwdCoz6lRUddk33LXFEkyD2PfDx-VbfjJgxWFeHl1x-4n90m6gmy6JO3c4iKBohl1PCZiK8eMLiB4yT03icSETyMRBcD0bJeKlYF7zCLFyb5289Yi_nxRxqfEJtS-MSlm-JzE01BKGt7PGxW3SJEJk7p3W_o3FwtqQje5gmEfGL-Zc-X4Vy_0gre9YGdMcShPpLFYfEGaUJJKHuZm608gKeVlbGZPBErFYVXymM3iyPiwwROanklS1YBPDkt8_a0e94A8PEYaqNkDhwq99M12I-P255Fryz-U2HTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی سپاه پاسداران:
«از اینکه دولت به سپاه نفت داده باشد، اطلاعی ندارم و بعید می دانم چنین موضوعی صحت داشته باشد.» او اضافه کرد: «سپاه برای تجهیز و پشتیبانی از یگان های مختلف خود به بودجه نیاز دارد و دولت موظف است این بودجه را تامین کند.»
مسعود پزشکیان، اخیرا در یک سخنرانی گفت: «اگر ما پشتیبانی نمی کردیم، رزمندگان نمی توانستند بجنگند و ما 20 میلیون بشکه نفتی که به دولت تعلق داشت، به هوافضای سپاه دادیم».
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=NbTFL118HQp1D4iCZllYs5jF2x2tsuieyEIUuGD8-JngS8HsLLt5Qz7wH2061BdblUvBS74cW0vvXQ6Cy3TKNo0IysSEFs21o0YUdPgbv4p1mtzYtof_vOmZHBButhEtGlHWEG3YbHPmsh2AAzGmZAfEUPt5b_955uEZyCKzEvMGa2_0WdmweDbpxeoK5PLs4cLAslZQiUM4T5h02hegksbAP8tIC-uUO24C5tVxSAINEB9dUa1CBzJ6My2J6SZ1av1bVohlGhyy1ovCnURdKfsoZAn-mquVL7TVB7shuNoq2OKD8k-kODCpeYdjAT_4wbzgNHRgTlMTNbLwFIOMNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=NbTFL118HQp1D4iCZllYs5jF2x2tsuieyEIUuGD8-JngS8HsLLt5Qz7wH2061BdblUvBS74cW0vvXQ6Cy3TKNo0IysSEFs21o0YUdPgbv4p1mtzYtof_vOmZHBButhEtGlHWEG3YbHPmsh2AAzGmZAfEUPt5b_955uEZyCKzEvMGa2_0WdmweDbpxeoK5PLs4cLAslZQiUM4T5h02hegksbAP8tIC-uUO24C5tVxSAINEB9dUa1CBzJ6My2J6SZ1av1bVohlGhyy1ovCnURdKfsoZAn-mquVL7TVB7shuNoq2OKD8k-kODCpeYdjAT_4wbzgNHRgTlMTNbLwFIOMNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-O_3xdDw-s6mIQB3w_0ofVdxcDgL4WFbuXHaktlOKbdpx-6Fpdn3tYKxd8gr1eWzagi2D1Ih0vrupNvFSnVjhJ0x-Veh7vXBKl24mG7lHWZsQD1CzMV6WX2BRtWT1vjZTXuLWjKJymakZw3cLbSlnW7nJN403VULRlWkvUY9Dgma7W-Jrj7l2vY42qcOz_c3L4X2bjJvfEBumM9hDJLLlDmX5RvULWLhOnBp71D58H3xeXeOOayXOc0D4PkB6zAbboRoXfe4piiL5Z4VBJdtxLuMBaDslg3GQbSdYE4Zmy738S3F-ru5eIKYDTTRwALXVdzlp879DNCkzyMKfvEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm-YNO4ktpMLwzKvnbjwIshzkXd2pV37wZQGXOTzqz8NY-SYqKGq8WA60F8SqHaWZVviAe8r5CDQe2IqMZfUg7iC6Enmf-2K1QjxqLzxBs46xrtqTxlSpvvB2F70aRsS9FYloYEC_rvhRV-wglqehzW5eY2f8zdaY9JkZ0O5PlRWERGyr2bV7koofd740mxqHK6oV1l2nV5Qfm1Uxv9tsrtFH5c5-edq0p4Lnj8Cy8WxwEhHUdjzpVuF_SRwalQEbr8_5IU-BL4ARxryC0jUSqO_rKDxdQLoNOCuGjEgrUQwTT1SFMmqX3uKn6t0faX5-3Nk95x77eqv62ndXqoLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=svTQiNKU6PufV2clWZSwc0Nn-Ql9Sb3TzN0bNkCipXLkPqtiREsHTgDSL_b5-81V7A4u6ZInuWrIIKKq3UDear82AOst35ANM6WHI1j4zvjn1wJxY2ai5rQgQbc2vVyou6MtFPHFcfu_GsFcRUO7d25j2ncz92I9JLXN2KmR5Oa6DAigN2gnGUwNTA2gSDNq04gtav0MCxk3Lc5EWA7FxhutTD4E10RjGpi02PCOmS2lzHePrzPbJCOSQnXcnZMNekLc7-Z4YUCjG6nt7Vr7QWqw6p_j3B-LB031jCDFv__tDxA1MejM3m6RxiSBfIZeH4zEX65EYQADjZ89fXUl8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=svTQiNKU6PufV2clWZSwc0Nn-Ql9Sb3TzN0bNkCipXLkPqtiREsHTgDSL_b5-81V7A4u6ZInuWrIIKKq3UDear82AOst35ANM6WHI1j4zvjn1wJxY2ai5rQgQbc2vVyou6MtFPHFcfu_GsFcRUO7d25j2ncz92I9JLXN2KmR5Oa6DAigN2gnGUwNTA2gSDNq04gtav0MCxk3Lc5EWA7FxhutTD4E10RjGpi02PCOmS2lzHePrzPbJCOSQnXcnZMNekLc7-Z4YUCjG6nt7Vr7QWqw6p_j3B-LB031jCDFv__tDxA1MejM3m6RxiSBfIZeH4zEX65EYQADjZ89fXUl8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سعید لیلاز: فکر می‌کنم آمریکا در بهمن یا اسفند دوباره به ایران حمله می‌کند، تفاهم‌نامه یک وقفه است
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66980">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‼️
مجلس خبرگان بیانیه‌ای در حمایت از مجتبی خامنه‌ای صادر کرد:
🔴
1. مذاکره‌کننده‌ها باید حواسشون جمع باشه و تحت هیچ شرایطی از خطوط قرمز رهبر عبور نکنن.
🔴
2. تأکید میکنیم که انتقام خون رهبر گرفته بشه و ترامپ و نتانیاهو به مجازات برسن.
🔴
3. اگر طرف مقابل توافق رو نقض کرد، باید سریع جواب داده بشه؛ همچنین باز کردن تنگه هرمز در شرایط فعلی اشتباه راهبردیه.
🔴
4. موضوع برنامه هسته‌ای ایران اصلاً نباید وارد مذاکرات بشه.
🔴
5. کنترل تنگه هرمز، گرفتن غرامت جنگ، آزاد شدن پول‌های بلوکه‌شده، لغو کامل تحریم‌ها و خروج آمریکا از منطقه باید حتماً دنبال بشه.
🔴
6. مسئولان نباید حرفی بزنن که دشمن احساس کنه ایران ضعیف شده.
🔴
7. در نهایت، حرف آخر با رهبره و هیچ مسئولی نباید برخلاف نظر ایشون عمل کنه.
🔴
8. گفته شده دشمن فقط دنبال خریدن زمانه و احتمال حمله دوباره وجود داره؛ برای همین نباید مذاکرات طولانی بشه.
🔴
9. از مردم میخوایم حضورشون رو در صحنه حفظ کنن، اتحادشون رو به هم نزنن و به حرف‌های تفرقه‌انگیز توجه نکنن.
🔴
10.  کنار رهبر و مردم می‌مونیم و در صورت نیاز به وظیفه خودمون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66980" target="_blank">📅 10:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66979">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=JIHyyb_k5U2GU8oj3t8o-ConIkSs_LT4yulFjN279MKVWEXEo7Mr8uujc1bxBfBwRKejT0wsExwnzL09AuRfDIxZ5VAhrO3lPnXNt3gvKNV5t0PLKRd5chQ191TmzX0bcOpxjIzyUjIMYSvvR5BCoscaQLOQf75hwRgjptLM-Nb89wiV93wDz2fpgfYqvyMklx7lMNOIeoYkXiRMBkvLE6LQyNVXMNFW8y6OQRFZ6f4SxVOOuFV8OYSnosK-OPCfvIqIcQuOYXkR0GrvxJytz3w4Tenj27iBbGQ1OlM0cZEMY5cGn7xj0ObVUDNzJY6OJ8KyEEZ0XATJ74fnaAZQbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=JIHyyb_k5U2GU8oj3t8o-ConIkSs_LT4yulFjN279MKVWEXEo7Mr8uujc1bxBfBwRKejT0wsExwnzL09AuRfDIxZ5VAhrO3lPnXNt3gvKNV5t0PLKRd5chQ191TmzX0bcOpxjIzyUjIMYSvvR5BCoscaQLOQf75hwRgjptLM-Nb89wiV93wDz2fpgfYqvyMklx7lMNOIeoYkXiRMBkvLE6LQyNVXMNFW8y6OQRFZ6f4SxVOOuFV8OYSnosK-OPCfvIqIcQuOYXkR0GrvxJytz3w4Tenj27iBbGQ1OlM0cZEMY5cGn7xj0ObVUDNzJY6OJ8KyEEZ0XATJ74fnaAZQbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سنتکام:
جت‌های جنگنده نیروی دریایی و هوایی ایالات متحده امشب به دنبال حمله پهپادی ایران به کشتی ام/تی کیکو، به ۱۰ هدف نظامی ایران در چندین مکان در داخل و نزدیکی تنگه هرمز حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66979" target="_blank">📅 10:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66978">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران
:
فرزندان شجاع شما در نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی، در یک عملیات مشترک موشکی و پهپادی در ساعت ۰۲:۰۰ تا ۰۳:۰۰ بامداد، هشت هدف مهم آمریکایی از جمله پایگاه هوایی علی السالم در کویت و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین را هدف قرار دادند.
دشمن متجاوز که خیانت و نقض معاهدات بخشی از ذات اوست، بامداد امروز تحت عنوان مقابله با نیروی دریایی سپاه، پنج نقطه ساحلی در ایران را مورد حمله قرار داد.
بر اساس تفاهم‌نامه اسلام‌آباد درباره تنظیم تردد در تنگه هرمز با جمهوری اسلامی، از این پس با کشتی‌های متخلف با قدرت بیشتری برخورد خواهد شد و هرگونه تجاوز احتمالی دشمن به هر بهانه‌ای، حتی مشابه حملات دیشب به اهداف کم‌اهمیت، با پاسخی ویرانگر مواجه خواهد شد.
دشمن باید بداند که نقض آتش‌بس برخلاف بند ۱ تفاهم‌نامه اسلام‌آباد است و منجر به توقف کامل مذاکرات خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66978" target="_blank">📅 09:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66977">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8-QfDV0T3n7XvfuAliBbzxyRZM4btJX50f4tBVKR7fZUj4rqGRiUwqZDELYmsXgB7pOkJ3BobS7tQx71ObvG29Y5nRwFnC4fTQNiD7yAReBMpYtw1bvuMET8eNcPoo1vYdj-D3P7Qy7EFUgsI_7qI2UBuOnez1jGMDcSf-VBnoSxrzHFo6PnPrdyE145qs8JomecjWM9c8MggOMAXJNUqKVtxdmqhLNL9I8RUXeaCe7YDRLBHWgzdIKAa_QBZxWxRwe-uU60AmFu4sInO-0m4N-j49CocWNHQYEWjfi3DHOPrp4JVD_8u2-fTXpodOgt1_A1ce0ks09ujomDkZWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هواپیماهای ایالات متحده به تازگی به دلیل نقض توافق آتش بس، به انبارهای موشک و پهپاد ایران و سایت‌های رادار ساحلی حمله کردند! بسیار محتمل است که آنها هرگز درس نگیرند! ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی باشیم و مجبور شویم کاری را که با موفقیت آغاز کرده‌ایم، به صورت نظامی تکمیل کنیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66977" target="_blank">📅 09:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66976">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حداقل تا اونجا رفتید صد کیلو از اون ذرتای ترامپو بیارید الکی نرفته باشید.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66976" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66975">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=WloJwCFABOw_EgDLAy_3FV_NlEyekZB9cE1Pi-JmF8QXfUvllX_aEgiEBj5OvGfBq_6ggnxUwbEg6fvW1KPVqDUwKEmzQrURxFzeLxEetYYFnVPc1r63VzcC-o5u1oT5s3fH-BABj7a-6cCIDoi6oI0J9PP9abAljfrMb61WLbd9kszrUU1ujHll7Prg38XW3dD060jkflXNeN3G6i3D7PV5NJ08vJXNj2JS8zqt5QBDutCeQO5HDiQ-Sg0vYILvUAnNYaf41Ux6cPrsJj-6i1G5ks6-LCAkMd6dM4goXcxh5utcKJeIyJp7-ydK96L20zh1ETeJesyBJtaz59th1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=WloJwCFABOw_EgDLAy_3FV_NlEyekZB9cE1Pi-JmF8QXfUvllX_aEgiEBj5OvGfBq_6ggnxUwbEg6fvW1KPVqDUwKEmzQrURxFzeLxEetYYFnVPc1r63VzcC-o5u1oT5s3fH-BABj7a-6cCIDoi6oI0J9PP9abAljfrMb61WLbd9kszrUU1ujHll7Prg38XW3dD060jkflXNeN3G6i3D7PV5NJ08vJXNj2JS8zqt5QBDutCeQO5HDiQ-Sg0vYILvUAnNYaf41Ux6cPrsJj-6i1G5ks6-LCAkMd6dM4goXcxh5utcKJeIyJp7-ydK96L20zh1ETeJesyBJtaz59th1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من دور خونه بعد از گل سوم اتریش:
#haa4m
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66975" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
