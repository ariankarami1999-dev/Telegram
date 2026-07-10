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
<img src="https://cdn4.telesco.pe/file/KGnE1t2xKdokcPy29rEPDZdGCJn6q0-XFabDxpFG2aC6HQqM3vCFGSXfwkza5tbNNxQG2nRFEcFscpWwkNqWVc7w1YPbb3xseiIZfsjCaxXwOJCc_BCg_7ozW62QhibYWMm7eR9HmjX6odoOA_oGagmTV4P_qVO3PJf5s2cVmxzqP6vokwDtfhauWvDVSMV_ePJQ40nbuPnVotSTYS1kMJpXl--OjAs4E6T3PXuqByGqKfy1dD9dbI8_75UZQUwSxHAeib8S29UpBcxnr0yljHEOezaEusCaDT1uUGFreSd78QuA1o7lfeZNeKEQd8p8eZhHVFp8G6wF_h6y_-53nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 186K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 23:45:05</div>
<hr>

<div class="tg-post" id="msg-67753">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjWXpJrfEIYdzjudKjnBAw3XwumH2Jx-6Yh9BRDYf1g7QnfcPtN3aG0_YB2lgxyaaAt4jULCnpqppQFc2S1FHz5J-AjC6mvD4xLGdY2faO5GZ5WqMC9hiOGIKt6jzlaqPXgnA8YC7W05eRlJ2SqPMvcbOW3IsZk87RU4Byr8wmQ0gFmF4VdEvoVY3ERazBhWQ_tqV4V1_OQB_bavjjJki2L-Oy9L_tMQXPOvbu9t8n_Gw5XolhOVVXkRqkdNedOA5NaC6AVPVAQBxG9TZOCD0er-XV2RHfBW7Y9dJKNXCDntCEMXImfEs2AtC1IMfYjjkVu9Ot95KoPZzBAJQxRK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhHvZwXvtcW6rKnbVk8xW5gdzzZGV2uxGSkNCC4vgMevqm9cdgYLM8PRKCEn9mTI7GMVJI6Jo-kLAByELHzeMHmM85cdJxPtGl00PskrP5tJ00JUlp1W97YMZIWFyfoo0-J5FeDHXAOtIjD1XQPFIdsKn9pdTZfQLGe9nnGJwLL9cEw78ucccum6fSui9WfD3Ya2-me_7hOXCQ53szt8JdvndhQ2_x9qhnGnjvdsfzDiBnFb2Jg-sujLqTJpI0hPl3xYmdwBLvjLyB7ceo5DdL6hxN_Jyezy28AuiOZBucrDdaluIums6WhdYZe4xzg8TJQuLIsn_QummbBZdBM-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONhfIFY-F4rSHol8RkawhITl7MiOpP3Lven9H7aTJdE9qDbTiOZ7Yfw_jeMfFRzGePMQ7y6O4GSuZXfc8aKn7tm06UG3ncWiaCy7f7yOKGs7c6C-ELadh96qMMOyn2hZ4BFna5aV8-W-XdkxGg-5NE3AopIJLWsTHWt96KpJLo_94O4BPQ1qZpvNtJ9YSH3EGwJg54FVS9fPXwT-Pqc0NkdeAxJXm_QI-sUYk4B8MnVhiYUG6ChRjFA4J_2HhqtpMco7p5JYyUk-mE8IssjVcIq2XaFLiZjjB3KdHkwEmcAcoTvwDGOE3mL08LKSzKgS4kJz1i16G1V7JdIst-nd8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
شبکه خبری CNN تصاویر ماهواره ای  ادعایی را منتشر کرده که نشان می‌دهد ایران در تلاش است تا تاسیسات هسته‌ای واقع در پارکچین را بازسازی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/news_hut/67753" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67752">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e999307d.mp4?token=GAQNZFEO3exKfwA3IFl5Lj9bZh4JV1_iv5bxg_aougOqPBefCT78sp8aYfJBxpRD0LTQcucLSJkqB3ID0TRBVw5VQQwmSYiTWdXSM92i2oVxADfA3YdmJ3FfmPVcm7u0dw-OmcHpIz_QYXFlL72x1ZVzfAW1Wtuu3sLG6A8y0XtmxdEABiqzZ2lLrVedn7rOW7gkltq0uOwzHnj0rLsDUDSjPmQ8NXX5M9IScxlFfJvUiutIPqZonQqfrY69r-_DAbzXQBnZp4rhfeSYsjXUhNCvzRmIMAW_8JIee5HSX2Rix9RtbfCNDse4mZX_6bb5QOb2Cf6A_jt1vnJgRqBQiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e999307d.mp4?token=GAQNZFEO3exKfwA3IFl5Lj9bZh4JV1_iv5bxg_aougOqPBefCT78sp8aYfJBxpRD0LTQcucLSJkqB3ID0TRBVw5VQQwmSYiTWdXSM92i2oVxADfA3YdmJ3FfmPVcm7u0dw-OmcHpIz_QYXFlL72x1ZVzfAW1Wtuu3sLG6A8y0XtmxdEABiqzZ2lLrVedn7rOW7gkltq0uOwzHnj0rLsDUDSjPmQ8NXX5M9IScxlFfJvUiutIPqZonQqfrY69r-_DAbzXQBnZp4rhfeSYsjXUhNCvzRmIMAW_8JIee5HSX2Rix9RtbfCNDse4mZX_6bb5QOb2Cf6A_jt1vnJgRqBQiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب ترامپ رو تو مشهد دار زدن بعدشم ماکتشو سوزوندن
گفتن خودشو که نمیتونیم بکشیم حداقل ماکتشو بکشیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/news_hut/67752" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67751">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtNa-OaHDVneW-ap5qGJ_0cE_rLc-1YWUY3cGMB-eMbfwBqOWtowJlpP1wWnbQn7m0ruQLq4mkF3HN9NYgkZ56Ljvq4XKEsbCQy68enGHO2fgQDfuYmC81qYXwOzmlVRwJ6WLPkOsKnh0vzfvCeXzCANWHz0j953z9AsyYXlFADjXtnaXCJbPY7XLPeMwSjjniSFEZv776L26nuWkH6XyMwrOo4_I0d-M4o5MSr9JBUbJIh8Sfrxl7Mgw0QWEm2gSzygGcMb_4a2WyDEOa8sh7WsmdrbFSA047sf6HchxdzcxpEfWzGSExeqxOpb4de3k5MqpHAq3_OaIVWoXqpskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
در جریان مذاکرات، به معاون رئیس‌جمهور آمریکا توضیح دادم که ما به شما اصلاً اعتماد نداریم.
به نظر من، تنها کسانی می‌توانند با ایالات متحده مذاکره کنند که برای جنگ آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/news_hut/67751" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67750">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.  @bet_maxxx @bet_maxxx @bdt_maxxx</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/news_hut/67750" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67749">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnegin</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAEiGawFGl7_cmbtzT2t9OdiKGks9L2_bEyp76OZSz_eAL5_X1o89IwLZ7BS9gelKsS1ph9FTZWISJCj_KMB66FFcX2c777m242SGXpouF2MFEGfT9AZbM4wTx2YOIm-mK5gsLRWCVEcNkZyB813odPoKCe4QxFTCXeF-tPrrcALMwcvD5vi1976ZXTCUxWu3pykYfhtM-V3X5MzoZQmHmw_722stBA37N_idq2j-b6KXKraL_Axmfb2HOi8vbYJMb2D3WXATAGmiU4oLEyADtu8fLoHlYJBQ50uN6x_Z6cqPV66UKkNXyD26pA3xPoWFXddECjyvIchcCjq3X-ZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال
اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی
همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.
@bet_maxxx
@bet_maxxx
@bdt_maxxx</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/news_hut/67749" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67748">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=U2IoC9J0w9VYyIMvBqheL51JrUCgnvtX5sYvyhUJSE63SQxkrToN8zb0KJiK41zIjNDBwnxUNRa17qxDmmWZv7HJwF6QQRR4PYORe3dFH5RJGt0833Fj6OUEBFbCCWRwtDxbW8bbu6aBtImj40uzMGBQyuJqDVSjXvf8SbWgpGHXmdtHRdHb58LtdDeiNcUeEOY-QKDhGdr0neWamPiIRN5aRF73lWmyT5kCYseinl2iLhq7C1OTBWINgN-R63gb4P3PqSooc6vayra73B3PIzBm0apmELCG6rSQSBSa9Ujm0mRH4J6djdK0M3WGvKrSbLuMRNv6X2OT95_AVw7rzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=U2IoC9J0w9VYyIMvBqheL51JrUCgnvtX5sYvyhUJSE63SQxkrToN8zb0KJiK41zIjNDBwnxUNRa17qxDmmWZv7HJwF6QQRR4PYORe3dFH5RJGt0833Fj6OUEBFbCCWRwtDxbW8bbu6aBtImj40uzMGBQyuJqDVSjXvf8SbWgpGHXmdtHRdHb58LtdDeiNcUeEOY-QKDhGdr0neWamPiIRN5aRF73lWmyT5kCYseinl2iLhq7C1OTBWINgN-R63gb4P3PqSooc6vayra73B3PIzBm0apmELCG6rSQSBSa9Ujm0mRH4J6djdK0M3WGvKrSbLuMRNv6X2OT95_AVw7rzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالد ریگان چهلمین رئیس جمهور ایالات متحده آمریکا:
در این سخنرانی، ریگان با یک روایت طنزآمیز، دیدگاه خود درباره نقش دولت و مسئولیت فردی را بیان می‌کند؛ روایتی که سال‌هاست در مباحث سیاسی از آن یاد می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67748" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67747">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXb6QQGwU4YyxWrG_0PGLFXwU1i1QqgwksNtCStxLs-nE88Nw2wFxC3DE8UFMJNQGN__Xo7mhSTmfSLh-OvNFVuJUm4U2W7NZQRINMPVRR-FEYkuAWC7-WGEYRy51ZFEB_zjwaZX_Ampl3jza5YbjkwTDo2QfwqR1_AY8t6qcxmSHWS9V1_NM0qedeMn8z2szRa1XBKn54XUeV3bIyVkBwbhm7fOrsJOP7GmNU8Vm61WirsWQDQpBFhdpM6sNQN76nvMDyY_CicuNIR64gIQ7ngMa7_BC13xQ1irQ44-6lSl-n4C2OrTe0mBwi8kF-NEt4AQTqPZd7pht4AopZx3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل هیوم: آمریکا و اسرائیل گزینه‌های براندازی جمهوری اسلامی را بررسی می‌کنند
روزنامه اسرائیل هیوم در گزارشی به نقل از منابع دیپلماتیک منطقه‌ای و غربی مدعی شد که ایالات متحده، اسرائیل و برخی کشورهای منطقه در حال بررسی راهکارهایی برای تضعیف و در نهایت براندازی جمهوری اسلامی هستند.
این گزارش همچنین ادعا می‌کند که در پی تشدید اختلافات داخلی در ایران، مسعود پزشکیان، رئیس‌جمهور، و عباس عراقچی، وزیر امور خارجه، با فشار فزاینده جریان‌های تندرو و فرماندهان سپاه پاسداران روبه‌رو شده‌اند و حتی احتمال کنار گذاشته شدن دولت پزشکیان مطرح شده است.
اسرائیل هیوم به نقل از منابع خود مدعی شده است که عباس عراقچی در تماس با میانجی‌ها اعلام کرده دولت ایران نتوانسته موافقت سپاه با مفاد تفاهم با آمریکا و توقف حملات به کشتی‌ها در تنگه هرمز را جلب کند.
این روزنامه همچنین مدعی است که یکی از گزینه‌های مورد بررسی واشینگتن و تل‌آویو، تشدید دوباره فشارهای اقتصادی و بازگرداندن کامل تحریم‌ها با هدف افزایش فشار بر رژیم ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67747" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67746">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7q2YCcxvNz_Y7KJ48KJNysT7jB8z-GVSDxsaj-W6wO65DG58YifBhEKCoFhFBsE2yzSFGPNkWi-WAWA0iNPnPAo1NJP6YqmCfzjl3-SkofS_8wVPoBWMmzyeGWE-KOTK5NRSO_txYn-itZ31paHafTNeLe-K1ChXVR9KMdr27OkLiAKvNjS2PPoXQ2CRYPHsz0Jic1vGdRkhBAzLqube6Hu5vtogB3Z9R0vX-0Kd76ij__OawxgsWgX81EHX3rhynyf5BtXcxj5NCY6_RGvYhrFLkoZ2K5gPFkXKCe4kYLzeXYHS5jEcSrudhexgxbT2TsiQvFkpgsYymHqXDD3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باراک راوید:
بر اساس گفته‌های یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده، به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و تلاش کنند تا تنش‌ها را کاهش داده و شرایط را برای از سرگیری مذاکرات فراهم کنند.
این دیپلمات گفت که جلسات بین مقامات قطری و ایرانی در تهران همچنان در حال برگزاری است، "اما واضح است که هر دو طرف تمایل دارند به توافق‌نامه اولیه بازگردند."
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67746" target="_blank">📅 20:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67745">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS_TQaagjmgZ74AAKxBmXwXBOY_B9XsQSxFT-UjW4FPtLHToOLfKZFewi-1ZCEuHfpR0UHhFeAb9CJ-Hp8GLUGin_Wibbtqy1Tl6euJhzXNnDUV2vJ_YBpdENhXkXO8MES0W1E9Y89z0ocipwMHelmy77xBBs2xzxFcy3hP33m8SRyoaALyoSZE9hQsxINzar551KJafFvz9PwHVSkGjiGqDNxtzG9pqOcLXbeaIWc-zE_888v_jQbCV8fr7GGErTVbuaUc_6w5yhDcGVle4K76hQxShcpEn1mhoRO4Ltun92_VIjP7mWxdJKs30dpM0sfDXOOkvHJJF8TEOxeopUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به «نیویورک پست» گفت که دستوراتی صادر کرده است مبنی بر اینکه اگر ایران در ترور او موفق شود، ایالات متحده باید «به‌معنای واقعی کلمه، آن‌ها را چنان بمباران کند که هرگز پیش از این ندیده باشند.» او افزود که «مدت‌هاست» نفر اولِ فهرست ترور ایران بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67745" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67744">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdFEqDwNTxZs2Ii58BzB9q8svz6SgVxULERrn4RA2OTpE8kVst5OljdjfBTAKBu2e1dRED9lLpX27iJDZNH1JpZUCn-KrhTVpr2dR-eJ-zTk9gPDwcJeBPWgelB2PPE_syc2Nmp2gkLcAhVeff212XLJguME0kiao6Xy53Na7pmBGBEziwBdkgCR5z40HY_qbskEFpSon698QroammssZv9ukNCIm50_pEuaX5BRchBEeY7smvDTHf7MasjPyVcYLrotSZGa3QwEU4tccN7y-B1HvB00k_8akO6Hf05xSY_dFbyL2YTBlOt5HfWnuznBMkEPgrdUhh1YskUfvdox6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
ترامپ و خبرگزاری آکسیوس را نادیده بگیرید. هیچ مذاکره‌ای تا زمانی که دولت ترامپ به تعهدات خود عمل نکند، صورت نخواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67744" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67743">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
آکسیوس:
پیش‌بینی می‌شود که ایالات متحده و ایران هفته آینده دور دیگری از مذاکرات را برگزار کنند، احتمالاً در سوئیس.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67743" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67742">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=ZpuYXEKszUxizkN-WWYbzHue7hbIX2lXU3GAQmpu2IQMiPOlSf1442tKMsmS3ZA6GJS1F0HYzw2DE31D5j6ynCTkRdS8HqojREnCJHNuLjAik7-j1eQysAbdvz_tZRZ1DP6HyxNzEYRZ3XkTY0GTfpRn2xUx9Q-znnmSl7iEDfuegT1m6nwoNgS9tzUeGnjNjlHZkEInVCPDtn5RZL_pBTmc_eQSgcHNjvcO-wCn4grwaPNvSSVQygjqzefZoBi9ndwUoNdA76s_I20vCxrkElsArwdERISnTCNNPSSycOufcHRY8QWRwp5angQblej-y5gDqc4NN7EGxNk8X12brg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=ZpuYXEKszUxizkN-WWYbzHue7hbIX2lXU3GAQmpu2IQMiPOlSf1442tKMsmS3ZA6GJS1F0HYzw2DE31D5j6ynCTkRdS8HqojREnCJHNuLjAik7-j1eQysAbdvz_tZRZ1DP6HyxNzEYRZ3XkTY0GTfpRn2xUx9Q-znnmSl7iEDfuegT1m6nwoNgS9tzUeGnjNjlHZkEInVCPDtn5RZL_pBTmc_eQSgcHNjvcO-wCn4grwaPNvSSVQygjqzefZoBi9ndwUoNdA76s_I20vCxrkElsArwdERISnTCNNPSSycOufcHRY8QWRwp5angQblej-y5gDqc4NN7EGxNk8X12brg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش‌سوزی گسترده در مجموعه اکسین پلدختر در استان لرستان
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67742" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67741">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuHU0bQPTXx84WC3vxRpgMZHTs6woLF85PuswU3Hxo4pF-IFY9AcyPPQHaqfMU6HckEGoKHKS5VsRfwvhl-Vf81agxvmuUdAoGeKvOqqFn5FXwHV5wrVj8luNBFt7nxEMBzTlHsiDmhPMaEsvM4eebYL7NO1twLcM1lHV9Q3t_NDARYDBymOrxNlX4E9Ez0-tlf_n5ghRPzwUvwwNcHtBfqORvSn5iX0ZXQp5iVGZIa4CvfKWQ3RmCjcIGV2gGX0Ne98h9NncHOec9H1EbCYE_kByY2eridc_HxjW3oLATs5zHnSMkl30rARMlowxYFprStnX1FIrzaVFcIu27BKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انفجار در پالایشگاه نفت پلدختر در استان لرستان.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67741" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67740">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUsjWXQG5QPbV5o-yPfic5CkmmhYvqUjOvvNramn5dh6wnzC0nLbrvfysb6qPv3lqXdyStrCgIz0FwR2fHRSnl3H399iTYbmD9LaIuMeM3o8PvGrB9Fz6DuLVE-XujUpeUGZMAFuJ8ZjB64M0IKXf_HoyFUTCrv2Zloe1SvVWK0w24aee3yCCK5-gBD17SqmOL6NFMp37YzZ0i2tOo4C9tkg1slQvA1F0uV2Mv8Eu5y_yplWWHVdmbyPyaSeLXlNJKyQBjj55yChmRdhAe-PRTy_wMXCgyoeKXR2NQg5wo4InipSJadSGnzfUC2l_fUpcVbxukxcFth-hjLDE_CSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بلند شدن دود در کنارک پس از وقوع دو انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67740" target="_blank">📅 19:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67739">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=hFngk352zfmB2YNVoROthRcEMGbEoWLxBO6lxyCv3JCKWHoO3lfpSZ_VCyb6wuq7SJAgdooHay15MC-Jf9K8HriygFT1yhlx-OEVAEFU_ZqFLTMgs3fwDrTrkj8hf8EwhI7ge5rrE9DVphHug2Im_GTSGLbwBoh3rPqSez29jScZJbkw-NRMFQTKggNnWrbuEzFVry3EwJTcpF66zf3mULUs2UDGnxJ5Y0yRnUcJcEGPJdBphkI58JMGU0t-e5MTozVO9eTRjK22FdCzq_YM1qOwEjpfWUOn5gfThX9DvW99_mkAClzRBJuL9Djxj35guBeIquSGXcLGJyUPAp77RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=hFngk352zfmB2YNVoROthRcEMGbEoWLxBO6lxyCv3JCKWHoO3lfpSZ_VCyb6wuq7SJAgdooHay15MC-Jf9K8HriygFT1yhlx-OEVAEFU_ZqFLTMgs3fwDrTrkj8hf8EwhI7ge5rrE9DVphHug2Im_GTSGLbwBoh3rPqSez29jScZJbkw-NRMFQTKggNnWrbuEzFVry3EwJTcpF66zf3mULUs2UDGnxJ5Y0yRnUcJcEGPJdBphkI58JMGU0t-e5MTozVO9eTRjK22FdCzq_YM1qOwEjpfWUOn5gfThX9DvW99_mkAClzRBJuL9Djxj35guBeIquSGXcLGJyUPAp77RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صداسیما:
اگه خمینی و خامنه‌ای، زمان امام‌ها بودن، امام حسین شهید نمیشد، امام علی حاکم میشد و امام حسن هم صلح نمی‌کرد.
پیامبر خودش گفته؛ من مشتاق دیدن اینا بودم و حسرت دیدار اینارو داشتم
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67739" target="_blank">📅 18:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67738">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arjnpsJ5xnsaeMh8VZUga0qPWjna1lZNgCGA3KteIt383c0K0UIJ468YE6bjuCi1sxV8-wuhe-W3IJRSSZTuJl8WDExrcaY7UKQf7W4vkzzyFW1PUsg3z3kQvGjxDd5hjvzDwLkHbgzH3uDvkQO8DIgnCithsrwpjxtDQFfW0R9YxpHw8AZRKcERDYm-pJmnVZQktNmF_Pgt7wOReHdPCZxplea_ppnICoSUYWQICK_DYCt3CLz750uNc0kkDgWnm6ckugaSxhDsgDWLAe7NJjKtJBQ7EmtIb9FcZS87aGVxpGC3VkW9VFj3q5SrjHsA9FkTWYQTizxlrcLuV_AjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران با ما تماس گرفت و خواستار ادامه "مذاکرات" شد. ما به این درخواست موافقت کردیم، اما ایالات متحده به طور واضح به آنها اعلام کرد که آتش‌بس به پایان رسیده است. از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67738" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67737">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU9Sctj167KWL5BeATIl-nk7KxxONOc1wIu5Oev-J3wArbgw7XHrar8bg4kzNYUhKFRV5onWtVYYJcfMlAx-CZiHdA3ty9P_rsZKU2rq8sUbA1wUPzg-TN66JvCOCfnyhIXq4Hwby9Bcnf9S6Jg1-PTZVn9yWa3LF1k7Cac94n8kmuEv4YxX6E8uRN1DfhaJyFkMcKnrGO_lH98agkztuaZ1FvXMconYlpgYLAAnfkmzUnEIabPM3eKTEU0h6wvKRAGwd3wPfqPCyjlFg2SPz3gqaUfARiTnkXfB8z3QoH7v3IncCX8vtvyD9TlYbH2tBGB4yISCul1ayCwzmY_oQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی ایالات متحده امروز حضور قابل توجهی در خلیج عمان دارد. یک ناو هواپیمابر و اسکورت آن (حداقل 3 ناو جنگی و یک تانکر سوخت) امروز در فاصله کمتر از 300 کیلومتر از سواحل ایران مشاهده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67737" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67736">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=kEv1J_Iq_XvCiUvR9CWkN4JEXvbkxCZo7LgICvKLa-DEZ3BdhiLupYDSkEavvQ77HjPEKXbnhzIE6arKHOIRzuZyE5RPQiUG8V2VLApgiOgWLvpoVXgPeEuICvp9WWdcSp0sZBMyJYMN8kzLVkgs8yA55v59V_R87yFt6OKHSjr0gKnDkTcUjbHBfqMrhaOPqUNYLVhe22Nm57dzzbTa33rAq10WtpB2HAY2xkriRX9aM37X3rCK_zgnbbhRAHejTlvqCw_CJMTf2t8J_3tzV1Hwx9xerm0qnSk7zT0wilOOq-kBCO-zmnULhkbynrSr7ihLiSfy0VTRiGI_uesRTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=kEv1J_Iq_XvCiUvR9CWkN4JEXvbkxCZo7LgICvKLa-DEZ3BdhiLupYDSkEavvQ77HjPEKXbnhzIE6arKHOIRzuZyE5RPQiUG8V2VLApgiOgWLvpoVXgPeEuICvp9WWdcSp0sZBMyJYMN8kzLVkgs8yA55v59V_R87yFt6OKHSjr0gKnDkTcUjbHBfqMrhaOPqUNYLVhe22Nm57dzzbTa33rAq10WtpB2HAY2xkriRX9aM37X3rCK_zgnbbhRAHejTlvqCw_CJMTf2t8J_3tzV1Hwx9xerm0qnSk7zT0wilOOq-kBCO-zmnULhkbynrSr7ihLiSfy0VTRiGI_uesRTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو‌ ای از صحبت های چند روز اخیر ترامپ که در حال وایرال شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67736" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67735">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67735" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67734">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LobtDc_3YShnkjUz0Zp-1Hz_gxTikobKfg8bpdfkdlkzwhHaBF-2S7SlU0Ci8Xbjmld_PzsFTSVmewOXBBqsoTtHulgZrMQwmJEzdbau8VHuYC-Nx0-KOeEfvWdOJZ8tZtJ6CT2ybk3tPNh92pVl-eWLaaBeem9V8NbpyzeJHPIUa7Jyedj0keEesKNd3Obxg8Kj3If5jDjwhiC6JM88GQqnJ4pr-boWAqBwMcI5hBL5MqdliBcW82sbkuTTmhFOnxbn03amBg4iVQq5Pv-eTphJY5PSUG6tZearYQjaV3IE8pmAhi9ZMiKKBR0gH6EIHmcLLmjj-rryi589k4ArKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67734" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67733">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=cIYW5qFJ7vC-F0n3c9Tx12DobABqlS2B-LctiiH_TY2Ls-3J_i2qA2N73-BDwro92DHCuMOEAl_oHQRKfkyBAR-g2K3bb5j5VkRKAXgxcRQIyzjWF80jNc8OUrO740Eh-mPUkAOzL_Ym18o0WOZrQvu7IYGtx28eOFsZzdUIZSv_qxW0C17shGSdBbxqX2gQpRA5URubh_HdYrp8D4jPNOXygHZMBwTeZt2FKwTfSQt76rKuv60x-h7ddFvXUXqEc1n7nOwhVFfr7OEaEWQMxqoBdWAFnq189OceT_g63c3YV7FPRVN67JIEARMCvJPVKN8XpM4lqNK6rWZVC7Gmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=cIYW5qFJ7vC-F0n3c9Tx12DobABqlS2B-LctiiH_TY2Ls-3J_i2qA2N73-BDwro92DHCuMOEAl_oHQRKfkyBAR-g2K3bb5j5VkRKAXgxcRQIyzjWF80jNc8OUrO740Eh-mPUkAOzL_Ym18o0WOZrQvu7IYGtx28eOFsZzdUIZSv_qxW0C17shGSdBbxqX2gQpRA5URubh_HdYrp8D4jPNOXygHZMBwTeZt2FKwTfSQt76rKuv60x-h7ddFvXUXqEc1n7nOwhVFfr7OEaEWQMxqoBdWAFnq189OceT_g63c3YV7FPRVN67JIEARMCvJPVKN8XpM4lqNK6rWZVC7Gmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇷
علی خامنه‌ای،22مرداد1397:
به طور خلاصه در دو کلمه به ملت ایران
بگویم: جنگ نخواهد شد و مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67733" target="_blank">📅 17:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67732">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiFDIx6SIWVbqqTWdPlEuWDK1EgV9eIIKw5LqkDp1l4UoE0vmb06414c4JIwNcqYOzEu0IEtEiZKyISeI0Ti6qwoDzlI7XhN6Hh_UfrHmGofkqYsVcHdCtSjfAl1fVGZNZ1vxq88BKbDiXhPOmoOfStHm2TIILRtvYOB3GVD7dQuVcfknJf6DoCrZJQ7jFOauv9dfuTFlX6ktm-9nA8QecvsVzVHn9ywBmpZIsRw3ryjUH8ZFlncEG01Hh3JMyvP5fR8G2RVFhryBqtrpe4o7iihLeCjKFOsNuFcUVPGKBNxhPEgHo-a7qVy6f9GczmB5CGuiMQu1dHgX36v63GHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کارولین لیویت سخنگوی کاخ سفید :
جوون‌های نسل زِد که از وضعیت اقتصادی و زندگی در آمریکا گلایه دارن رو بفرستید ایران خیلی زود قدر آمریکا رو میدونن و زود برمیگردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67732" target="_blank">📅 16:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67730">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY1i3-zYKbvImSsuNGFBGq8AKs_W3ir6QzGRuRbBdHImZghylSoat-5jMd7IIb7sRnOeqK5nt5sy7MiJjpnYHHEZt5NuvHDkoqpo7Y-7EDSgsMzzn478Pq2VQzv-Uc4soIIvRPuNtxg55Jcag5z4bWtBzu1uaKbgHGdtJ7-h5AR0KBV4XRFWL6H5DhSgBbB1XGvbldcKLNoXEZa-daIueYZf-XJa_c1iwh7hAcD_hgLotEXMsJgg-SDTsrShKBIcEICbNICejQo1ad2hVi3AIcEo587kNv9hxoZm3X8VAWmOD7X4NwFI8BGnFQ6A50i3muXQungJKNB3vcsmkJpBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1372691bce.mp4?token=faGyJtVr2kcNS31pCeGOZMazyTj4e3AUvVIorbcc_iQ5rJNjOxrzvF5XxMbhj6FghfidHCMgWzBg86KXYpjJP6wji2_ozuL2p71E2aG_sF0s_s77Qd4Wmj62JBlt6Gelw4sTTu30BZ6lrLhyVVi7p3B0ZVw1_EcXN4x5zNmI6-s5i2fyvGJRqvrMUhsRRl87Atu9zPRh_JhRKoVCjL3u2JIXczN6SuMMfsRi_xZusfIu3Uh6CnfAZy_o7AiMoThfRdMWitlRiONu64XiM6amh7sEAAIowIUDcum6yZFi5pZQJmZo1pz0-fSLgFreVZGLPfXRladVNVnx66XACVuScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1372691bce.mp4?token=faGyJtVr2kcNS31pCeGOZMazyTj4e3AUvVIorbcc_iQ5rJNjOxrzvF5XxMbhj6FghfidHCMgWzBg86KXYpjJP6wji2_ozuL2p71E2aG_sF0s_s77Qd4Wmj62JBlt6Gelw4sTTu30BZ6lrLhyVVi7p3B0ZVw1_EcXN4x5zNmI6-s5i2fyvGJRqvrMUhsRRl87Atu9zPRh_JhRKoVCjL3u2JIXczN6SuMMfsRi_xZusfIu3Uh6CnfAZy_o7AiMoThfRdMWitlRiONu64XiM6amh7sEAAIowIUDcum6yZFi5pZQJmZo1pz0-fSLgFreVZGLPfXRladVNVnx66XACVuScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دیشب تندرو ها داشتن بر علیه تیم مذاکره‌کننده شعار«مذاکره با دشمن، خیانت است به میهن» میدادن که مهدی رسولی مداح حکومتی صداشون رو قطع میکنه و میگه بگید«حیدر،حیدر».
این حرکتش باعث واکنش تندرو ها توی فضای مجازی شده و گرفتن روش
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67730" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67729">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4niFslqZE0AoBZJ-dmltWAWiO_SCAmrBELRcjebG9bGaF0oA6OXrYPFo-CNaN78SNNUV8c84axNMDp8PdUqqIlUpaq8INLezNLXwJBFw_ohvxcsTnpeaq6l2ptEIG-ZbSrZR73fovMYw0TDb-GdIFxLbqSwgCbhhmAsgVqglFUT6790J0kwhS7nakj9QQRevpdvLWmogh4_W-q3xJ4A6w-ztFWjF6_wXWv72lcE4Vcf15UfRetSzPWYzfXMFGGyq46nRXJL2CRNxgyxv6-1o-L5LPE-v0CcmASgrQfFaRTihQ2NK36FSRRW6SJ9tBCNyCrsOBxqew5BX8wrwnWzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده(سنتکام):
❌
ادعا: رسانه‌های دولتی ایران ادعا می‌کنند که عبور از تنگه هرمز تنها از طریق مسیرهایی که توسط ایران تعیین شده‌اند، مجاز است.
✅
واقعیت: ایران کنترل تنگه هرمز را در دست ندارد. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از 800 کشتی تجاری و 380 میلیون بشکه نفت خام از طریق این مسیر حیاتی تجاری بین‌المللی کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67729" target="_blank">📅 14:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67728">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GSINzXHWjiXBv9HILfg3vtgiwshkCcL90_R-gn5gS-vQije_M05oDf8vW25PoIQh-CyVJS709L-rusGHbyKOmdeKI3ttAyv8245QQ9LH52NR7DewseTjEf81RP1Qw3TbVMMR1uLlpwT0QEBn2SgqXDXhtocFQVPvOQ1exNWiNc7IbpeE0OnJCGjVJJgRnGKcRONjyhQD_5DB-0zgI_X19Exwe7cMlBM0_BdIC7OKZU4wE6Wr2BP62ZsAaU_3ZHR9-eZj4HqVOFeIUNDAnZB6yrdVky7pr3dNNRDHXO9I4j3_r96yhrhx08u01a51JazoueI4-MVfMwdnbW7n1LffDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام سازمان سنجش، رسما و شرعا امتحانات دانش آموزا، بدون هیچگونه تغییری و طبق برنامه، از ۲۱ تیر ماه آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67728" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=XKMS7n3RBy0Ia0qIvarDvVVE4EtT2BmqgT3vR15ZgdaM3ma2NmgiBSQRjHCdMYD2E29hRbzYR0dBKRH1tryjkL2czX9QquWDfbLyKtYAgBFkYP9ElJgKhnHJhStLas3Ax1Z3hNwc4LmR3sYQNUq7-rqZTNS0Jvos1-a-Hbj953ltIhfMtuQ7wAK4sYHYNk8dfIlZGdG4Yh7HqEDdYjeZLAPp2tT6UERl5f3v_o3d7ugLU0bBUiORmhGvKsMCWCQM-7LwcTpfyX3qDqUKYIYXNqXbkQIGAuikjWHoL2utkKfx2K29tMLfexvkOu0TszePONxJj_1wTQWbqffo6Qq1Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=XKMS7n3RBy0Ia0qIvarDvVVE4EtT2BmqgT3vR15ZgdaM3ma2NmgiBSQRjHCdMYD2E29hRbzYR0dBKRH1tryjkL2czX9QquWDfbLyKtYAgBFkYP9ElJgKhnHJhStLas3Ax1Z3hNwc4LmR3sYQNUq7-rqZTNS0Jvos1-a-Hbj953ltIhfMtuQ7wAK4sYHYNk8dfIlZGdG4Yh7HqEDdYjeZLAPp2tT6UERl5f3v_o3d7ugLU0bBUiORmhGvKsMCWCQM-7LwcTpfyX3qDqUKYIYXNqXbkQIGAuikjWHoL2utkKfx2K29tMLfexvkOu0TszePONxJj_1wTQWbqffo6Qq1Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسِ تتلو تو زگیل ابدی با یکی دعواش شد؛
پسره هم وسط برنامه خیلی جدی بهش گفت "
برو بابا یه ملت روت شاشیدن
..."
+ ستاره همون دختریه که تتلو تو ترکیه روش شاشید!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67727" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FG5AouYG2vXMKMf7vor40dyfy-QAZxnqTo9KF-xFxQa8tvLHQxmtgUF80b47rdj7cZJEGnEgA72YjOf2oB3r74UnsGcZ5NscRMxOyPc598dKYnL2Hh8dOyeVMHj_2xp9CR6TLRd6wt06iE8Tj-RdBNZ_yTrS2dW06HdV8x2FOVATIoNWQvNIaFu-FKpyyGupbSmOqnUzmXBmRr72Eeapwh0XK7RACwj2Z-TZq7ILw-NClNuWjCGZZf2fafOzYpRFn5rl1_xjl9uY4TouGMdd_rBP4DNZUsEtmybUEelpNd_aTGAcGMFHVm5Si8hHPUSLYRzE9T9OEbfW9R9GumHIEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606bce162e.mp4?token=MjMF8fACwKSr7-7xnwtjYzrcMhBATpXruoJrOFEsxvijebijVWyuNKXg8eCOwHFvvGJKf2DM226XS-KB3Nf6g-JMq9OtjhcnOAc1fesDS4N1UCo93RWXevC5rnOL6ea7RHZ9zpiTj7acNpuohf7BpURkcAdTFxwA6SdyJ-6tBbRIpEDSQU5gxKp6LNBgHTOWFSuOQ7IqUVzjuWb0Uh9JfJNys6bgnhQ4jzgB1Dhbkn1OL_69V7KabBBTdbI5ud8x_TgQY_TWET2-STXAR56_ShRiqbQ4JR2uUeIcV0kB5uNtnY6XYmtsSyjPCsSLG0bP46jmxWOs9uZ4WEPWTczjNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606bce162e.mp4?token=MjMF8fACwKSr7-7xnwtjYzrcMhBATpXruoJrOFEsxvijebijVWyuNKXg8eCOwHFvvGJKf2DM226XS-KB3Nf6g-JMq9OtjhcnOAc1fesDS4N1UCo93RWXevC5rnOL6ea7RHZ9zpiTj7acNpuohf7BpURkcAdTFxwA6SdyJ-6tBbRIpEDSQU5gxKp6LNBgHTOWFSuOQ7IqUVzjuWb0Uh9JfJNys6bgnhQ4jzgB1Dhbkn1OL_69V7KabBBTdbI5ud8x_TgQY_TWET2-STXAR56_ShRiqbQ4JR2uUeIcV0kB5uNtnY6XYmtsSyjPCsSLG0bP46jmxWOs9uZ4WEPWTczjNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی مجری‌ صداوسیما برای ترور ترامپ؛
نگوزی‌ داداش.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67725" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67724">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
تماشا کنید: پهپادهای اوکراینی شب گذشته به ۱۴ شناور در دریای آزوف حمله کردند، که شامل ۱۲ تانکر، یک کشتی باری و یک یدک‌کش بود.
از جمله اهداف مورد حمله، تانکرهای روسی به نام‌های Chelsi-6، Aura، Sana-1، Ilya Repin، Venus-3 و Penelope، همچنین کشتی Mercury، تانکر Galasar Kamal که پرچم پاناما داشته و تحت تحریم قرار دارد، و یدک‌کش روسی به نام Alfeo به همراه بارج Aphrodite بودند. جزئیات مربوط به پنج شناور دیگر هنوز مشخص نشده است.
در طول ۹۶ ساعت گذشته، پهپادهای اوکراینی به ۳۵ شناوری که به "ناوگان سایه" روسیه مرتبط هستند، حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67722" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I8GVgR-PkEaS2n0XV3T9bPfzcI6VgdvWANya3Wp1NhCNepDuAxS3trn2fQtixXr-rLwPl93WpI1WYfEN7GvrFK-cuJWhHetjAyUpzYZnhG3Yu16mqqw1Hhcx6Xrd46R59UTLMYJ4gOM997GNGsjXNw-XGHqU-5tc_UFgasNt_VbUR8fnjYktuJfCHSZ0BpN3wLmS9UsbWcmpxHlTXWnnahrEd3fXp8a6noB6lFoBB9jXsZvWAy3AdDsHX4tyYIItzh58zgCwqE1Sbftnue2bXcR8zvURvRRKrRaK9uaZsr0WXbH2nUQrVSHN8GQSm4pPYh0BqYytSB1F25eOE1zLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_8SC6uohVWcQ4BfqYY0KC3P0dWU0t-qbUCSY1A3rBVgU1wYp2fDOktn8KAsJ8XKD5v-zCRd9JAEj1Bq55iYyqM7jvZsvbqKxpkrnlGSrPHM85pRFXJKiGbU_DUZ0yThB3wyr_KtAR73_0h9UQqITMZljAFqQRLZjh1pclXTEyc1yC9Ywn_i1aCTdY2R9Y1HnL3FUdTfosA9JanBWv7AVrLDhMimJPHVvW3ivWyX3gDdjaYJNZ76D6rxZp8zmwEWQk7qfT_IEBm4prUaC7BV2vjdrt88E4Z3VFTvLyWF_ovzhASojSIs9OZCzjSVktsTuFfsIr_xoVrt4ieeJcOYRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EVGtCgpxzyPQ4VzZ6aYaJOeF6I24wDTKYxsqLe2Aim7WiqlWauC4SdSxpLZLczT-8SmPAirK-gC0Jxkh79ajLLIUisNZ2J4BLe4xwA_F5_BK2-PL8KbP-TIr9R0MBI2oMeWIMNzspdpInEhx6cN5DwqvKaNuo-efNCA4z5iPIbqa6_HpEzv0ROlXJ48hX2wXiBs2antLBXjm8uIr4D4dvGH4j929gmaq40qt2T8pj4i4whrP0ISy3AATnmJUOsx84nNDEETr_1y2sYYffksnOIysPfH8UE-x3GIyubmqrAY-cTnAU3Qn6-nF5N38gb7-8Rj3KZTBWEcEjASirN-w8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xz-HJF3Kat5cPYpmEV_D_NluR2fPVXwoIz-LJwAnFonKNcj9287vITLZLZifKju0w3IESroWTYQg9hYLbK0OWTbBzfhCywsE9Js6B_pQ_RSw50UAdZSSqjiX7rSdxbXKqubvguwzecLOiOtA6XfgwvQxQS5rdOpydwZpJrB5QPEufeL9rZT_FtixihP9VE0br2GObbvekIvU9hg97ATCE4UTCWYKIbfuSKHSulApLYeCXOvKwYIyF8vDn-tLKXEm4NU8qRR-bcEWi46hyRmN4ngy3RfYbQmJgAAyMpinO02CvtIcoBYXcFjIZkGKOXfQvWoIZJpwGWGobTaPB03bcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6lW_dzFTIhNnZbpwf_kjnkBEokIZjpkF8ryGzUqsBoA_93tlH2f4rth169lgaeg_YTpb3Pp_QhSE8RtE8Hd9L4JVfrD75Dm-LM-pAYgLWSoSgCy5o__YwqtEGbNKnF3IK3j1rsoL9jvZ7DC4mqOtY-ITxTtZqj2qPNHTvoesrR80JO8-AaRP6FNuw9A21AS9dyT6z-z6Agh0DSrSQegdtSu8FUxo15g8VG7poCTR9HpVOm2M2sqm4E4OBkEJWp9UUzFpJ48B6Zk7KzEbO43ddzFmO3KDpwNF8cVBqVVpQFypy5iWCZ35Sk6xX-GH2UP2wtnd0NMjHgNLd9-WeMB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-GVM_YuRvDrf41BnfN9ksO_DmCiO8gyEDicR75UOLyfAOPMMM6PWov46iVnSRmGmbKsYr7o5O6JxS3kWoB_Z0eEPIRU1-J5BDxtkWB_ATKj1_gknl6uAhlAeBKMlzGY42SzqY-QcH0tHRXVj6paKyQ_flVigvm6QEXlUziX9aSqF_8srRpjXd93GEG8quB0BWAqu8C3lP7MWdfaG-iuBU6CXw98qilZP9-akKT5VCGeYtWybijbircoIalziLuacSOxpiuu7SgiHtymc2qvNGaBcuzTv-AWxMTEPLqAQFMW-KECAFl3aVamhQJPbMFV_j-PadXMYbMTYKJOj-JMVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=P_aKc9wibbkxg17jYQvijlcXXiCEya0C_CdOeDt1tUASNyshNDL15qzuqfAk1uicVpdriGDoO_IdUwfHbbotjjIr4-DEtXpqNGBkavB56iMx_A72scU2ruMF0tOC5q0TYRi1xkLp9WlgBr5aTxsl1-zFov_O9c_2defzl6Hau6JD4i5C6qyeKKCXvCCSE6B8AcUmu4Qm8mFj2cBtZdtxyQG1hKhOY7A1r2p2WbvBIgfPvkvYC1RaogtNJDYT3REkp7zw7dXR2Yh9J-y8cgkI_ip-5O2LWksiX8HVw86-c9rqz-jAiHF9okKdUAU19hsJRFhUFHRET1rohpltcmdvmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=P_aKc9wibbkxg17jYQvijlcXXiCEya0C_CdOeDt1tUASNyshNDL15qzuqfAk1uicVpdriGDoO_IdUwfHbbotjjIr4-DEtXpqNGBkavB56iMx_A72scU2ruMF0tOC5q0TYRi1xkLp9WlgBr5aTxsl1-zFov_O9c_2defzl6Hau6JD4i5C6qyeKKCXvCCSE6B8AcUmu4Qm8mFj2cBtZdtxyQG1hKhOY7A1r2p2WbvBIgfPvkvYC1RaogtNJDYT3REkp7zw7dXR2Yh9J-y8cgkI_ip-5O2LWksiX8HVw86-c9rqz-jAiHF9okKdUAU19hsJRFhUFHRET1rohpltcmdvmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPkuuDFIATKSWoDSBNGkooghSwxWsPaEAMBZpYp_xVL8eL39xEgZCFqzVQJyjLUaFSyhSrTLFreuClE3o85ASRPz5uOeZ8BB5f-jvg3g_40AqMU7y-SijfB2OTFLQq6E84aLHDikg7S_l1Br-owKiDwcfQkPLc-_RYj8TB1XgmxC25sJ68h80cOUcpERt8w7Ms1OamcuQ2BoU58uIaOT6ajCzBpz0PpRouOE4v5PkKyfx3qQ7DIiG---SU4eL75u6miQheykIBrmfV8q5MZQZwq6-UlvTEc1oFUCTwna3coTjMFFlcdZlmODOt-fzQ4UFyXh-KC6DVh9K9aZRKuyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون درخواست زیاد بود دایرکت رو خالی کردم تو ربات ۳ تا پک شد، کلیک کنید
💦
😁
🔞
🔗
دانلود پک اول
🔞
🔗
دانلود پک دوم
🔞
🔗
دانلود پک سوم  @News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA9m83joKt8V1wZpw1JrFB9pkJjgoSyxpMMywMS-LPtJm8zMKOUCVAZQTokYiEUdaV8cjaVmO3HjwnJIPkTgRwxu3tQFyglIZfdBAm4ACd5HwiW3T15oceU-UV9YeYSuwxpwzHDbZzpw0Ega4YbBr0bzTlYYNONltNQtGCq6bjMLollVR-QJDeHkITTN1Q1nqWu3s53l8nNiWk_P86UeBPpe9Z6p1dglkq3eLlEpv5kzDRFzrxsH_Ke8JCH_UGuq00K6jtwqFD4RQBHmxq675kky5sX56n-FCak_H-OUYqli6gVNBhyC6fslU535I8HY4hfWI0vGDZIA5fuzM1Latw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/immYsMPbL28WVOUClRZAb5-9Lmfkontn9M0RcMrYxi50OyZuNy0tmJY2jPgBsqbukjiy0_0XRKnxF7E6nxzWYNJDDOoVFP6b0Z92yWSp6ColIjv590tQLX366kANNqzuLgP-CwsI_YcGKXzDobTi-oDEkgzUc2-jaoUSkbFHpB9R8yhLBYMqPMtmpZNE_Q6mkuJBfodQAMXgu13LpUnrxiBrIhdKVCiti2L4Sy6dGZ5iWGDLVKXslgoZN3lz3LcS1IH7Xq4LCqgk1J7Z7jsLs8CDw1OcFkLa9nR7SD9Up0_yTq6x6gfP3LtwpWNTr6kTxLzyhOTayF1uCicWHwEDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzEHodKj_vxpO5UN8BTki_LCZEoj1TKdNoZop11LA9xmeN9mfzoTXjHBevjvRsGL1EB0k0_cpudy_uiLw93Rgt8qQZMicBGB-T81k5CSOIMuE9Ye4gsedDdNlXD2uiiDNty9v_rg0c1Ot6uQrqp0ANk372pqNeW-ZAqAeHu6tXSBqQUz9mFSGuSTfXBU8WKpeBEe9NcmYZ1Mh-6LaJv0TUp9o5_dPrqWz9IgwtiYRpNdU9YpbZyOJoHju3EA2q2-CDIoGLCZnq8f3_hLD3pD9yzr3BnLrT18Ooio9tXwC4Mrc1aDReHkUN07Y7NPnFz0od-AxTSrQPwL5eOS1QXGCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=KAkUnUOMHEvWKZzTUpqdycEe0sjwathXBBovm5w21Uc-mEGryI7hvT3FyNB3EOa1vvzlV9_XbwkAOeFZFKXFofU0EnHZKpnK8cC1Ei43-vswH4LqA3HPpBHKS2i4KEfObruiF--WyLtnEWYu0YkSdBY1z1EsPjToZF5KJcwYvfUVec2FGQVPzr8XGQ_3zzfrLBP7tzQxvfN16BLfpFfLTyKpYuEp8zupu1TEvDa7BqHCXAzqjF9rR6IHyXgWFjqe65RWNA_T-iqeQtdqLl7xZ1mbkwb3Bw0SU1wMeEcthGpmJv3bwdGqK2MVFFpkWn1LGQfYtcCK6gU3n0Rz28lIDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=KAkUnUOMHEvWKZzTUpqdycEe0sjwathXBBovm5w21Uc-mEGryI7hvT3FyNB3EOa1vvzlV9_XbwkAOeFZFKXFofU0EnHZKpnK8cC1Ei43-vswH4LqA3HPpBHKS2i4KEfObruiF--WyLtnEWYu0YkSdBY1z1EsPjToZF5KJcwYvfUVec2FGQVPzr8XGQ_3zzfrLBP7tzQxvfN16BLfpFfLTyKpYuEp8zupu1TEvDa7BqHCXAzqjF9rR6IHyXgWFjqe65RWNA_T-iqeQtdqLl7xZ1mbkwb3Bw0SU1wMeEcthGpmJv3bwdGqK2MVFFpkWn1LGQfYtcCK6gU3n0Rz28lIDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=ejZJBVNec4Xq8NXEcGEB76J4ByGIo90HBdUwuKohy-rhiUwKaoRrb9gLs5vpJYKahUKvcJpx-NtO10Qcv1NPH6xo_l2Qw1Sm14vltzStOh4L6E6RWJw1eipVv8a-QFnO7Z23l39gP0cts9WyK8nuT4vsQj48I2rXTKQo9gEvc_gqvD582gWD0YJ204BVko8xOixGpWIzY1V3Eb292tuafEwFH54SjOsRfVgkyTzyw8kkP2rwLV4F9TSlRgoBUm6-mQee66MLM_HC3xIW4UZaqmpuQIVr8gcJ9Iykm0iIiPQ6BJ5XGSyLgWgV23A7P4atIKUU3ciYDIrFlR_Smb0sBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=ejZJBVNec4Xq8NXEcGEB76J4ByGIo90HBdUwuKohy-rhiUwKaoRrb9gLs5vpJYKahUKvcJpx-NtO10Qcv1NPH6xo_l2Qw1Sm14vltzStOh4L6E6RWJw1eipVv8a-QFnO7Z23l39gP0cts9WyK8nuT4vsQj48I2rXTKQo9gEvc_gqvD582gWD0YJ204BVko8xOixGpWIzY1V3Eb292tuafEwFH54SjOsRfVgkyTzyw8kkP2rwLV4F9TSlRgoBUm6-mQee66MLM_HC3xIW4UZaqmpuQIVr8gcJ9Iykm0iIiPQ6BJ5XGSyLgWgV23A7P4atIKUU3ciYDIrFlR_Smb0sBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=rfmgL9IbGEim3UHhQepk5gpz0peHB61TFAQARWZc9Pii_3TK934FDTltC_jgZpHsy4n1HDfemym2JRbB9w8nWRv4MgyjfI2wHoMw0ixnxWXW2veyxNo8xKEGQzhQnledtlFiZnXUScrXNKpqdmxZzDg9k4Sd6XCcsQXjH_4pZOu69EPmCS-HT5vzDrzJ9B2kyPQWKX-uGOKsOz8vo1VjxMdiaR-acuaV2bPR51mQ8XvUazYGoMCN5zWhuUGdPIOJkEE2Zh1Kj6opfYE4hhesnHcFAFnReElVJ5SECrj16UCdnJT7greW8lAHbVbzeOIQ4xpExHCDNQoKPC9iSyyHfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=rfmgL9IbGEim3UHhQepk5gpz0peHB61TFAQARWZc9Pii_3TK934FDTltC_jgZpHsy4n1HDfemym2JRbB9w8nWRv4MgyjfI2wHoMw0ixnxWXW2veyxNo8xKEGQzhQnledtlFiZnXUScrXNKpqdmxZzDg9k4Sd6XCcsQXjH_4pZOu69EPmCS-HT5vzDrzJ9B2kyPQWKX-uGOKsOz8vo1VjxMdiaR-acuaV2bPR51mQ8XvUazYGoMCN5zWhuUGdPIOJkEE2Zh1Kj6opfYE4hhesnHcFAFnReElVJ5SECrj16UCdnJT7greW8lAHbVbzeOIQ4xpExHCDNQoKPC9iSyyHfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5amEZG2DYCPk4XuhaGt5PjOwQnS1Rze7bsdNlfDlbmWEQK-FZH4TlB9v0D3LCAD30CFrdS8NiwpHQsBAfsbi2jo9ns5Zi6o-oWtmt5qxsfkvOs47qCO7KbodBqPlXhfbSW0kV9X8Ao-sLIC73sU71cDv3uotxU3y892_EjvRJ8ZZdQY7AvwTc_HdwZoVAYlkbNRze5xQuNGKK6sg9uJz3PZnYEehtZuWUtsOjSOj9L_x9KVncPdSLBPGeAYZ6T8raK8SZH6MpTCPTtePP9Tb2CqPgb6PrW-oqzWWhxOkOYGvufoeQiGSTHI_47J-lKrCCxFNqSkhlR0AZ_axnfDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoUeXdHwJWy0DbxL-JIu4MYb5OHY7UStMlTwfRx-_dDWfKoWiN4emDV5iq6EcnIuoGF7KW8GjLuuNtx6NTHNEJeIbKyNRhfcqnPS1UYtjpLb--XHgx1OhzRkuv_aSm-UJr3_9dZHo_ENOn3AsnhtCElIqVwri5058vttqymbp2jziw03dzuDAPaCLYupqgwubA8IOrb5PyO-IdyBb4nycuXDMT-lkkO_fFUBgRsFlDITGNLtoEO1XVdSgz2hgbFL8m9mSnJ3DmsEUy2kjthDlf9dNQO2bDkDb_OrEod2q7XUV59-GkKvlw3ifXdfvkttE26ocZcGTvTn6xskA4dx-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=hUifwp9P0JlJf-91nFfPh3btv5uklYl7M69wJFfflB4mcqcjALqzQ35Pupa1mdAbebiUR6e7HY8tb20FyOPGYrAFgMcH4z_MI5oaiYofWJXA9f79DfcsgNPLATMF475lIVNqrtxOXPjR_dRSPaMHl9mlY39DGtK002ccMmSYlNOnwv7nxigNNm7vuRfGTTTWQ2EVySr0PxegxixXK4MrO4mk_dyv7KcL0Gk_4aO4RZWtccSUX_QFPeFdHLquLsHyBXldGL7D1BqsWzXK_TG9hhN1fR7teRblWVmMqBXjdf4o_O7C-6o1mPLry-V2KaLpyyiVwZV_h-5x6PqF-LjbwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=hUifwp9P0JlJf-91nFfPh3btv5uklYl7M69wJFfflB4mcqcjALqzQ35Pupa1mdAbebiUR6e7HY8tb20FyOPGYrAFgMcH4z_MI5oaiYofWJXA9f79DfcsgNPLATMF475lIVNqrtxOXPjR_dRSPaMHl9mlY39DGtK002ccMmSYlNOnwv7nxigNNm7vuRfGTTTWQ2EVySr0PxegxixXK4MrO4mk_dyv7KcL0Gk_4aO4RZWtccSUX_QFPeFdHLquLsHyBXldGL7D1BqsWzXK_TG9hhN1fR7teRblWVmMqBXjdf4o_O7C-6o1mPLry-V2KaLpyyiVwZV_h-5x6PqF-LjbwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67683">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=kTQuSR0_U_ZxpT3yW53t82E5yLb4FdSrmVeOp7A_TiekCnOiiU1w7MEPCbO-XDgMfrDpMVxxqgm6G0HWI0r6S0DxJJyJ8j4iSiTvoDSLblsApwWlv8kEqzrrzHUgcS8BheBjhTKCEP1bZzze4uhFxThxRKqFpApb2am6g-1POAk5dY8PUfV9wfuqj0Mj8P-m3ew858CEtD_9z5JFOLcNHCaBbEe7gIJvA9JemkGpohkSXGG0AkNIUdgObXuTC8RBHj5QwDod11XNEEwZSPhl1yoiWh46p04Tx1u1bMsyIQPGkIHnQYOXIxyiO-IIj8-6hTuKUS61PT52UY4wG0X4kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=kTQuSR0_U_ZxpT3yW53t82E5yLb4FdSrmVeOp7A_TiekCnOiiU1w7MEPCbO-XDgMfrDpMVxxqgm6G0HWI0r6S0DxJJyJ8j4iSiTvoDSLblsApwWlv8kEqzrrzHUgcS8BheBjhTKCEP1bZzze4uhFxThxRKqFpApb2am6g-1POAk5dY8PUfV9wfuqj0Mj8P-m3ew858CEtD_9z5JFOLcNHCaBbEe7gIJvA9JemkGpohkSXGG0AkNIUdgObXuTC8RBHj5QwDod11XNEEwZSPhl1yoiWh46p04Tx1u1bMsyIQPGkIHnQYOXIxyiO-IIj8-6hTuKUS61PT52UY4wG0X4kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر اسرائیل، نتانیاهو، درباره ایران:
ما به ایران آسیب زده‌ایم و این تهدید هسته‌ای را از بین برده‌ایم.
این مثل این است که سرطان را از بدن خودتان خارج می‌کنید. اگر سرطان را خارج نکنید، خواهید مرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5oPO48jW5JHsnKx4g4BTmrb76Hz0hAoRqmWQla3P-96HynnLEq45NLhRSH3tcT4Mfq5Kba8jvDrW2wQ0iFYE5MSCb8-uw7b84g5sbr2qq8z3VyMw5h5pQvCqdPMAzTKm2QouoFDi7aH0BqPgPOSaHMjQa2p_sXlXyqQtYkOxUyc6r3CNEm2xcTZowIGxNEA6W0esZKXCONCtSRN3ZPGWUcbqZvS3uOf7fykb7UvgbcU77iNACjhKEwWkWuBgzvagdGoolZGY4_gxZqcWGdhjUrgGi2P7UGz8TgK7ZnwNEyxDl_Uxe7SoonkvZmaYW-iyD-lr3hB8MWHiSv3v0Z1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So8t7UtA6RpVa2rOqV47Vi0HoUAvFtqAOfG_xnBw2yHKja6-VVFTZVu9bqJuWatI3fN2skzXMYssl3IYyKaeqohrZI0vjgoNsztK97yNfTDCQ1dRshY-iznXPrGHdvO92jbab7ifXfgwRWXOueZlMoyzv7eGH0Vz2LmAkxaqJoXmh4OViZojA_vgZbIftPqNUc-Z1_Ur51JKkDfd0bD4L4u0C-9C3wXCT2wJH1RRVPkFoltLQdhvRsltxBqi0-EUuAMhXVRIrflzVSx9NEyLcvtXnrUS0ugSbjAoVZLw_MY0Y72hM6V04gt64B99dy2PY3tWoEzhw7W8CX4RSHHtKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-kxMGI990ED4Edz2rc4ZWZgwZ4GhISvGaoW2yr7ifP1bNnJiUKvfEFYaCPgzgMT0wPyB6SrqR5953IinHQQKR1ciFXXEUGWiVGfzZ38yJ40jCgXnpuwW7O8XLA4XelS0z-s7gyr3h475n8Ee66FSaaxS7-gtRLfl_WNB03UGsCn-81WktqZa_OnHKveK1SY0_LcTMUg_YCI4Ldd0s4UFcoD_Ym37grUnAwHPgRffG8d2Wi6xO1NB1D3QSPPyZpr-uyJRq6dRernOLp9GrVfMuBHUiMKQZ5aasV-OgF-7BCPtGvS5UMwt9BcR_4-V5R4zwdq9CzjQlXFzCJPv3wC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=ejMjhj5DM0fUKovAoV25mwlpKagXe6-nKWMxFoTqlWXzi8ynhVLJxt6r2EPbacuYwlVbLz4t6I-e8EKpoy245cFk9TC2xCtgGYmTC2ki3aQI9aSgE-nkn7y9wakPcdxJNia3mSrs18u_rY1WXtds7y1aWJ3a9smEZjeON5iLaBxK1lZrvR0ujVlBZS1lxCG8E0X9whu-S4SdlGWgv6WKO1Zlq1tB6mFe1tg67MS4RJMzXTHEk87RyF-FdF8SX7oDrjbVxd4pgG_Iwy6-yV07vgwwb1qCM-rv0T2WWV9TS1VX6kahV--Ue3pU-_pVwTAz-r94ltB_QkOu7y-L09ZLNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=ejMjhj5DM0fUKovAoV25mwlpKagXe6-nKWMxFoTqlWXzi8ynhVLJxt6r2EPbacuYwlVbLz4t6I-e8EKpoy245cFk9TC2xCtgGYmTC2ki3aQI9aSgE-nkn7y9wakPcdxJNia3mSrs18u_rY1WXtds7y1aWJ3a9smEZjeON5iLaBxK1lZrvR0ujVlBZS1lxCG8E0X9whu-S4SdlGWgv6WKO1Zlq1tB6mFe1tg67MS4RJMzXTHEk87RyF-FdF8SX7oDrjbVxd4pgG_Iwy6-yV07vgwwb1qCM-rv0T2WWV9TS1VX6kahV--Ue3pU-_pVwTAz-r94ltB_QkOu7y-L09ZLNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
علی خامنه‌ای در حسینیه امام خمینی، پیش از بمباران توسط آمریکا و اسرائیل:
آمریکا هیچ غلطی نمی‌تواند بکند (23 اردیبهشت 1393)
اسرائیل هیچ غلطی نمی‌تواند بکند (18 خرداد 1395)
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=RRrXuBo92P0T3Za9Jr9755OhzsYAIN3bcb27JFqItH1Hf_jj16HmJlFXU0eOw9NZaeq40N8lUQw9l2Hr95ngBb8_O_u8DNYaA70sO-50pA_CPHlNEozN616lMmv36LNxIDViuQHVqmBDGDqYz8AnjtdL1pZ2XsyNvtdLrs8Suxx71S3ta9rtXiTrSGdhhvoz4BFjugyJ3uvbJJo-Kr4Mp7iqlVGl23-NQuwqs7XmAeTxh1HiMtS0KWMwPYXoM3oMG8dmHQlmsfp6jKOa3D_rAnsswn8m0naQq2gMw1VjQS3qXI3AoB8qI7KWsIKehuwAQvwObid5va05-Kc88VDyoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=RRrXuBo92P0T3Za9Jr9755OhzsYAIN3bcb27JFqItH1Hf_jj16HmJlFXU0eOw9NZaeq40N8lUQw9l2Hr95ngBb8_O_u8DNYaA70sO-50pA_CPHlNEozN616lMmv36LNxIDViuQHVqmBDGDqYz8AnjtdL1pZ2XsyNvtdLrs8Suxx71S3ta9rtXiTrSGdhhvoz4BFjugyJ3uvbJJo-Kr4Mp7iqlVGl23-NQuwqs7XmAeTxh1HiMtS0KWMwPYXoM3oMG8dmHQlmsfp6jKOa3D_rAnsswn8m0naQq2gMw1VjQS3qXI3AoB8qI7KWsIKehuwAQvwObid5va05-Kc88VDyoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=CM34iVdst7f0hFx7bO7VXQCgtfGXA4N9ToVbxPUXIl2_sjHCNL0psYUWyJ96Yizi0lC7AAkkhSZfnT8nNVjTpVtDSHG3leWqf7l8wwKekBU15gGGXhgp4EtVbezPnqvX6gau61c_VSySauLzwCRECcKq8m4nbrlJf5ZMzJLT9yGPbdDkGiC2CbRGScqaED1oyCteLhzHdanbRb1N8zOzSKOghOuvCae-p8AtGSZAj_1Eu7_SQ3uYJt7MZeJL8pSyp7a3RMppmJPW5c7iMKNXEG1cQNRLD6I-SDrvoco3_OVsBle2ckvt-duifIIJJWxT0cH0BBb9gfTl0uGrw3rxKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=CM34iVdst7f0hFx7bO7VXQCgtfGXA4N9ToVbxPUXIl2_sjHCNL0psYUWyJ96Yizi0lC7AAkkhSZfnT8nNVjTpVtDSHG3leWqf7l8wwKekBU15gGGXhgp4EtVbezPnqvX6gau61c_VSySauLzwCRECcKq8m4nbrlJf5ZMzJLT9yGPbdDkGiC2CbRGScqaED1oyCteLhzHdanbRb1N8zOzSKOghOuvCae-p8AtGSZAj_1Eu7_SQ3uYJt7MZeJL8pSyp7a3RMppmJPW5c7iMKNXEG1cQNRLD6I-SDrvoco3_OVsBle2ckvt-duifIIJJWxT0cH0BBb9gfTl0uGrw3rxKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=fkOwJk1BnAUF-JJxaFr9owU3qcC1P8qZKsA3kWzYFyoQXtS35r9b-tqEUAmqOBT0HOVn_YBQEtGdl7SdDUat-Wcy_66rmfq_DhAP7OU66NxVDL1pAU_ZAGPLwSqmCVYMhHPfZNXD5vVPDo9MYz5ubS2XZEcmeH1Rky5LcspzkSFt8SRpB_PE4ilNQrcGtDktHbyMSdInsvCdYUfK4xmHHQHjLkOMT-nDbVIYAl6MAbQ8vTEaoyCMHN35jdFCeU77qfh7emtGpHxR3Ae9CrEVDukqHY8LUxAZ1mQPUqc4cSN9ycK_WER42_Hudx0M_r0mSOZ-QQBpg82fxamdBeT7xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=fkOwJk1BnAUF-JJxaFr9owU3qcC1P8qZKsA3kWzYFyoQXtS35r9b-tqEUAmqOBT0HOVn_YBQEtGdl7SdDUat-Wcy_66rmfq_DhAP7OU66NxVDL1pAU_ZAGPLwSqmCVYMhHPfZNXD5vVPDo9MYz5ubS2XZEcmeH1Rky5LcspzkSFt8SRpB_PE4ilNQrcGtDktHbyMSdInsvCdYUfK4xmHHQHjLkOMT-nDbVIYAl6MAbQ8vTEaoyCMHN35jdFCeU77qfh7emtGpHxR3Ae9CrEVDukqHY8LUxAZ1mQPUqc4cSN9ycK_WER42_Hudx0M_r0mSOZ-QQBpg82fxamdBeT7xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUhYDGtxUWZpBeOvXx92iN2kPlUm1HRQgt3BZlDBoWfZQ-p8oPBsWzrXZmo1K_xMp1DRXwPnvVBzNXTjHAnU2Chuq3FQu5HZu8uaf_94N45z7iUTlqs0TtsmYGwE46iTMHFJlUT5HeFC7VPTzwjWkj0pzcN_afIfB_BEC3GL-qb61WduYV6q3vZ9H8mrrpwfACbMyPEdA5fd-zx3XZxV2llavMqIpcOls1cCmijBdY4k4yt6NZLDbAWrDN3j5n2wJHhjt_AJoMoc5p8Qvj4Um_QfVOKlO4rhd1Gc9JDQttZ8oMJBY3lHPjTgRFyK43N8Y9Boe5bj8Jhpo9D1gd7ZUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=cIoHYjCi1H9kiQpuAH45sW-AUVoFBHXlxW3pzm_O33KUzjpNycE7_3UrZBMXk1ZYjUnWAaCyV8x5wJ5btIj95PW2shjbBVIwNUS2S4DN0euuHAJ25xsv9c08FWAroFLawTQCX4QBkrxDmpqoW5VAH5JIB7aP6RGV2YCstmnUaZHSLDjV1yUDMBqJ0NsYRyYf4Py6tklbyqEZCJMPDP_LX5H2W4G9AAAe4L0kr_bW-jnkERF_xu1c-TVuXAjSjklHPs1NQBsFso6oyRXspFNLmKLO-Jq1976PyNN6CnKacqtRK-pIRRDUkq_yEc47MNcLhuWjqbX4Fo5cvqLsETv_xDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=cIoHYjCi1H9kiQpuAH45sW-AUVoFBHXlxW3pzm_O33KUzjpNycE7_3UrZBMXk1ZYjUnWAaCyV8x5wJ5btIj95PW2shjbBVIwNUS2S4DN0euuHAJ25xsv9c08FWAroFLawTQCX4QBkrxDmpqoW5VAH5JIB7aP6RGV2YCstmnUaZHSLDjV1yUDMBqJ0NsYRyYf4Py6tklbyqEZCJMPDP_LX5H2W4G9AAAe4L0kr_bW-jnkERF_xu1c-TVuXAjSjklHPs1NQBsFso6oyRXspFNLmKLO-Jq1976PyNN6CnKacqtRK-pIRRDUkq_yEc47MNcLhuWjqbX4Fo5cvqLsETv_xDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XobGqYF-wA7clWpfRpvKYd22KCC_wCcg9EmqyrGpg8rmFTThCyT8KzJEpwIp1M9rLwNR3rV7KJPi2FJABle60qkLvaUFkm0qt5rBMgxaTYyKY_qXrLyRKnJiENiKpRhUVjtAOjQom3EqSl-b0u0CiGGUUG6csrmkOptVcT-FNrBnfC_wFbQfE-jlLTcQLlmybjkNr21JUzCNO-RAo0cCl2ez1ODMClY7tWKgjuHN115nn1YrqY8tM0cENh4hMdZdf_jz7An0GEATgKdRyBSLvFpcd3k_-Vt5BPpVCiTZEeCRoT0sLwx9y3osaH9eBeATp9nC2kQGfS6JO_t9B4whfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCDlvi9XOcbCYpBI9RD_3S3Wsxxn_jfTx31qhXkrT1P-A6RjgxG_-kZbxFHfB8JOAfsHoNCludZZxOu3f8g-kwN_NGvS214qjL6qsz11r0_7QfqJ8SReYAGcBXP8z-OyeA2i9euUVwjaJF5VWWCWAkRhStJ_j8aXaw5yQ-FWA4VjR80NYkbW5p1Tkja8IDCCBOrtKjcApuEacS0QK3rR9lduUnbii7eVFe2WZIMf5PJUGcRXQS1b830DyMhWtSA-L9KqyoUZO6ihrjML00nTvmI67s0djg0dDa-cA9kZr1hljP9sRSk4a4y18YRC58EmkvgWaQqMySrr6bmVjQwFtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1_MfSCi8GjYS6rEw9OQB9DYXQuDbsjsApTYScN0jFNyms5_7vx64eBsoBZq_roCOAH5RSv3wSa-XWJjCc7o49wLGpmgJNZFqnEULl7aY0OkWgb0RLAw3rUP_1srqUFZgHJbHZrN91QgHr3FRHLaV1-RGhUSgeKjIjIbGaWY8ZjEFA3Y9ZN8C8JQ1k38HdcoWAJAvhdhMskOLykZ8Etb70_zzIhvdI9U8u14gk-STJMzwHlPLb-mW_dznHMZB9eWEWD22Bv_PIGgfFC8hOWskdo1kwYcaUkpQJhomQQyHFkLnQAmsQnStGs-Vq8Y6db7MexdHmxw-F2H7lMa1zfMdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-B7qZ9KArnM6iDgaojl6cNiFXiofgDvrl5gqZE5cZ2ZPOEuF6r_H2bJRe1EpPqQdxV8_bRqi5Ut2Sq5QsxU-0RiP1kikn9N6g12BXaZ77JvRY6ZonFd0xO3cslbD3hNxmTlnG_7Q-m4ULhymrotWKPd1VoGKelBZHB12Jw6WCVFrxTPnXKuat_vPIltPPOH2zS5LXHDTxW93yUPVr6hvkbsLc2oAxg1ickhf4GaYUB1n8bLpX8S_Y-VgkzkCENGt6IRotvoGYh4mMJCRjC6y3skQcRmaEIANyTrxy-PLOjYxxj8_iLgVvmdZkGgRauiajcLN3EjQX_5FDankkFEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=Jc0xq99GYwxQqLoIhwEYYC5TV1iyOgvuaHy_5GVirWKxLBp264l6bYclGbdXST0biAb6eZsH7ZcOuzHbeVC_KWaG0odthstNvnPyCSV3b6prl9epsQbgL1i-Q809lOYUkM9xFHea1leGD4EuJOLlJRXHDjjrR_CTLAECK-D72xsIYVYAyR24rjZYb-hVvJYnWr27BmOJpG83Eh3PrnBqchw5391wMBQ4Gg2YMeffQ4-rL6YwHBuDzhslS3ExILjTD-2qa754PURRaJ8QzCb5FL1jpaoWJcwSnA3fHE8GvBCtTFkxH3cTnH2aDy1lbbw_EebGZfWmfWe27eVDbd6rIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=Jc0xq99GYwxQqLoIhwEYYC5TV1iyOgvuaHy_5GVirWKxLBp264l6bYclGbdXST0biAb6eZsH7ZcOuzHbeVC_KWaG0odthstNvnPyCSV3b6prl9epsQbgL1i-Q809lOYUkM9xFHea1leGD4EuJOLlJRXHDjjrR_CTLAECK-D72xsIYVYAyR24rjZYb-hVvJYnWr27BmOJpG83Eh3PrnBqchw5391wMBQ4Gg2YMeffQ4-rL6YwHBuDzhslS3ExILjTD-2qa754PURRaJ8QzCb5FL1jpaoWJcwSnA3fHE8GvBCtTFkxH3cTnH2aDy1lbbw_EebGZfWmfWe27eVDbd6rIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=SfyM-I4yOnSrU_ZPGC0j79d5U7CJhheU1zNngvxuc1EdEyWAGj7W3uPdcc2iXsdnymw87gacx3bxGEx_Macm_OPNhthnGCx1DKnVexRLpjuuJ2dDgrurr8T7IpevVoxmsFsCz6D2AcogvudpnOPP0TsjBSEkzvxA092mFbygp9J3jX8abmVm_kQAa1Z3r0Vbrbl7_u7-ZqKr9MmVx1Jny8liEDPOA_89xWV1q4Yl5uKwn1FtSCZVMZj5hSUpSIGOJfAT2T37-e2aQ8gkTcFTdVSts3_vMTUf43E_6YYtL47O1aJuqE1pS_MjvStLgtKDSfwRyZQbgIjqNfQlTYzxpyyr_yic8F5VpEGtrPvzjypTQppez_fyjukL5OxM2qvDhsJ_Pnr7HJwVlt_E8sqTZKvpQbCxZnF5uj3JychbqlJTwaYur8XT-cJ5EiJjidF7lkAe6e6oZ2MiIrlBEsicPEbBTiVAOqtFFrsmuBKUu2a-1cR_0mwP3uUK19JwDfwWXsQA4pf1XBoUo2nj0OVzcSkhSB3-YjGsHMMm1S8gdLkESXRvDYsDvN1Wb0JEUE132D_5sDkWa3EMDqt7iF4DA6WiMwkRJ90MXxKu3goaHEOkGs2mdYncq_Jx765dhgm4RtKyXJpilzPEb8LnaHFCWWufTGexAdG3oZiR9thsmYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=SfyM-I4yOnSrU_ZPGC0j79d5U7CJhheU1zNngvxuc1EdEyWAGj7W3uPdcc2iXsdnymw87gacx3bxGEx_Macm_OPNhthnGCx1DKnVexRLpjuuJ2dDgrurr8T7IpevVoxmsFsCz6D2AcogvudpnOPP0TsjBSEkzvxA092mFbygp9J3jX8abmVm_kQAa1Z3r0Vbrbl7_u7-ZqKr9MmVx1Jny8liEDPOA_89xWV1q4Yl5uKwn1FtSCZVMZj5hSUpSIGOJfAT2T37-e2aQ8gkTcFTdVSts3_vMTUf43E_6YYtL47O1aJuqE1pS_MjvStLgtKDSfwRyZQbgIjqNfQlTYzxpyyr_yic8F5VpEGtrPvzjypTQppez_fyjukL5OxM2qvDhsJ_Pnr7HJwVlt_E8sqTZKvpQbCxZnF5uj3JychbqlJTwaYur8XT-cJ5EiJjidF7lkAe6e6oZ2MiIrlBEsicPEbBTiVAOqtFFrsmuBKUu2a-1cR_0mwP3uUK19JwDfwWXsQA4pf1XBoUo2nj0OVzcSkhSB3-YjGsHMMm1S8gdLkESXRvDYsDvN1Wb0JEUE132D_5sDkWa3EMDqt7iF4DA6WiMwkRJ90MXxKu3goaHEOkGs2mdYncq_Jx765dhgm4RtKyXJpilzPEb8LnaHFCWWufTGexAdG3oZiR9thsmYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=Jj62hnGHRsM3-13xOziFZROd4rmrf5aOYFBYVlCNdz80qlKcJluEbGS53Y7EYCx5GKsC4I-Nr3zEwugJC6-BHqlXomOWs1GZH9PFY-EspYE4HWYT4r1gqFAHFdef3wxDX_ISaLZGQdIz_uCJufRQk3Sia8x8ikwPwqEVIc47_qgcglFc9rS0Myb6t3YupLw2Dg1K3rDxKR0TqEhrGpTjpD_5zkdDkU5woYcE4Apk4XlJkXdisl1McnDNrvdjr-Ik-hQpSdE3D2_opTBjusfwYzfguuKfxaZyj-bjVHNbLMKZw3lwOFjQD1KyoGSGyEmdxXrwbPHUm7jgAz8VUz35Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=Jj62hnGHRsM3-13xOziFZROd4rmrf5aOYFBYVlCNdz80qlKcJluEbGS53Y7EYCx5GKsC4I-Nr3zEwugJC6-BHqlXomOWs1GZH9PFY-EspYE4HWYT4r1gqFAHFdef3wxDX_ISaLZGQdIz_uCJufRQk3Sia8x8ikwPwqEVIc47_qgcglFc9rS0Myb6t3YupLw2Dg1K3rDxKR0TqEhrGpTjpD_5zkdDkU5woYcE4Apk4XlJkXdisl1McnDNrvdjr-Ik-hQpSdE3D2_opTBjusfwYzfguuKfxaZyj-bjVHNbLMKZw3lwOFjQD1KyoGSGyEmdxXrwbPHUm7jgAz8VUz35Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=SIBhNPr14OtVQ8Jbw5a1bEaFx_NbhHzHTqOMYCKwWx6gX6t-gDd_tZRBix7BUsYaYP8vtstyxOR_JzM4iLEatVOjcOFaZJ99DeuhDlLD1c_5_IXhtRMRpUYd_5EvoFeDFxronnouhc68r0yqA7Y1MI5V65IICW8rNtj-Q4nsejZ9OapOHm3sYMbc2e6rZu7yVCzSNns7NE6MfhdMvY49W76t2p-tKoJI2r2QeSDPxDrugZzKlGdX1PEEaq-FjghBjT3hIl98JHyyX4E95iT2Vdzy6V9d7RAjJXwhFmX14yMpxWQQJniqfRD8jdCpI8oTqCOOKa8Lz-c1KcHK6wBYlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=SIBhNPr14OtVQ8Jbw5a1bEaFx_NbhHzHTqOMYCKwWx6gX6t-gDd_tZRBix7BUsYaYP8vtstyxOR_JzM4iLEatVOjcOFaZJ99DeuhDlLD1c_5_IXhtRMRpUYd_5EvoFeDFxronnouhc68r0yqA7Y1MI5V65IICW8rNtj-Q4nsejZ9OapOHm3sYMbc2e6rZu7yVCzSNns7NE6MfhdMvY49W76t2p-tKoJI2r2QeSDPxDrugZzKlGdX1PEEaq-FjghBjT3hIl98JHyyX4E95iT2Vdzy6V9d7RAjJXwhFmX14yMpxWQQJniqfRD8jdCpI8oTqCOOKa8Lz-c1KcHK6wBYlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPa151ldns3zQ85bZdUM3lzsAhVar5VEDB0tQDOOYprBSJUg1aQeRmW8EaL5Ubk-zWjT_k7aOH-nIX7EyYr0uM0Y8W6lQspl_poztWEJ4Rd9xUR5n6pfrlUfryjkEEoxg63yps0ZZjJEonBM42gcXfSdKe830RPwQpne-qGrGDNVyw2vJdd0Mum0_8LHab0yVjLfRyeNvk75vbFmV2fOeD3R1xqfxTgWKA3SiB4CBSceI6D_DqCbocjlkU4wUHrSvZrExyUsWfh9K9Tn02ccQ8xToY_Ezl8vaFTxmGC0N2xQ5_7NqdXzmfv1p6LW4McIoL49RY_hAq20TLTcVu3OvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uhp74o54aroA5Fhvv75c22eW97H_GycSareb_sXWwWF2Wws3pJ4PNx2rqXRio216kRZNC6xAsQQ5sKMzWW48kCLXOX46LWXQ82lxVUEOy1r90R8YJh4FmcZCtWeHDhMTlImAwXqJdDA4_QWWaOhrfo9e0WpAUPe_Ym5wIbjD3ls_JCfYXc6-bf7ImX3aPAPQn2mYroWlOBaTZ5d45B71sqMLFONIEMEL-CYJSOgnmolwIVvIUoCbYqlPnTYLL7ZZkLy3tdQRHaGBAiiSMafKJoXqELbHm9BgFMe6-4Z_sS9bC0Y3KaTCo2TAVPurTCwLuyar2D43oC6mymxZWjv0iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVA7MCEkPUM-uSXkkOA8KLfYWR3UFoL6uvY-F02vDJGeRcyiCT5ODfn8Rvb5x0Yomb9YCpv02q47JYxhz0Rf3lGRBBpNanv_1xx1vi8mQ0GpsFxRAxWyRW8vCpUWS492W-frgoYrutJuSbmDiFzOzXEs_coG31MIXuPlN-tBAbqits_1LkYrxa37fm4xIMSKyLmiz3TBTsfMA3xPTiVY2fqkfZeiiTm1prkXeYhgAiBQqS6tqHifsTsNC30L3U_DF8Y1Z6RQ6h2s_1ZzURRToQst4TZH5YPZNpO2Rtm8fkvxFEcHW9p6202S4rjND6hdA6_6TewwOr6NgDWnsX4K7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNf4wpvtLSsPb-C8R27LOpoZ-WwfnG3ZvPPZJN978HJ8EqBME2yfDL_LWFR8cAiJV1KbEQ9tKIsyXJjpOOOVReSXEpmYNzyT-HI2vYVhrIJ0vs2WHUVO4FMKQhz7KWuuSL3_BHyrB8J4QH5L9yxVFFD80sq-MdTst9VU9lnP37Aygg1Z9OcF1cmAe4jWL_K87LNQmvJq1LOk_mwRPsKj6UffjI4qk3BXxxTjTRmS3q8IOfAQJ02oFf27Nih0cepsSM0yuSxCRJvfwFpcdJAjeJ3QvALXiDkCwbN-r-CaEAsFV09r04hL-YYAYI4gtVLZaYFY6AVq4KfdAyfLg3mVSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1os1N7pwsjsjGnB2Oa0k4_k41-fbQxKiXWxeD6nVknBU_AS58pqLVsmdr1-ev3vnoAKyaL88spuPDMM5nDNMcMD_Fj678KNNLfQ4arrExG1Li8wjAco5Q3LmWD906atRmWt-9EgEtjl-KvBgTXbGlfR1vXRk8svOvY-JZTvhRe0bG49bSM8cWlDlGoMlX8I45rYCWmbQEkJmdK3l4YFWFmN_0Eq6mz2P_yjZXdxRIZVN5798Jr8-R9X4nz-O5Oj_PAGpT7NUokRtt13wATv_xnFBQz-ybUP0UdWkeI6A-Spi_SwCESjFzfaPMTc34M39dYrNU8CCwzaxaTQGpaGJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N01H-zDIwl_JU7ewcbRNCvG6S8OpXP_sPxdv0jPnUWG1o4qAkkw4zqUZ25Zr-8pJbarccXMe5jXdFIC3i7SbqkOzMjA6Cw74Wm88NLTtLsIEVYgogGo3vHR7YZ6HXrD1cDyErjIh-kPMv9i_-Gc2MrWkenjFHficHVwBpXuuSNoKEkMM4XYUd8LQ0Zc1CAblHPhW5-rmMOfwAr4ym3x-qICG65ADrn53n7ECyrNNYODxqDIfdfPpbUxtS2t_LeLj_nMwR-e3ntr_okplr3WhVmeH-EGDFex8WugJXjwvwtSDx3slRh3P2qoFtbOKtWRVL5SXzh-Lo0W2rcuYN9-Thw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
