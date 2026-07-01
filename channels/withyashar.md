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
<img src="https://cdn4.telesco.pe/file/Sh_oQ_zrKPH5aEEo_UHIkHmH4ohkX1KR4MgYFCYvn9QlX2PzCYPFnD-d4MYSKlo7ZtpWkjqFnbK54kWzJIGARLUdef5dkc1zBOhNl-1dEi9SWtogSSxxpDYbUrnn_C6Y8qwMG1d8Auofk5yJawccRL29wVE0zGv9qyC3_6hfWBgaMkoH-TGadSadhCVWHiuwJhAKuAvFMVkxs5xqfkF2lM9AyiK7QN1fnOKY3mGG0LKITp9gKq5FOG4btqrwhRpDC0VE9keN-QkilQ351WFaKDAtQ2F1Ern5snhIU0Tz6Apv9bacXS3OP73D_kK9wt_GhAKpqTR0z4Xwl0QBu69vvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 333K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 22:25:15</div>
<hr>

<div class="tg-post" id="msg-16291">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تحقیق جدید نیویورک تایمز : بیش از دو میلیون سرباز روس و اوکراینی از ابتدای جنگ بین این دو کشور کشته یا زخمی شده‌اند. روسیه بیش از ۱.۴ میلیون سرباز از دست داده است که در میان آن‌ها حدود ۴۵۰ هزار کشته وجود دارد. اوکراین بین ۵۲۵ تا ۶۲۵ هزار سرباز از دست داده است که در میان آن‌ها ۱۲۵ تا ۱۵۰ هزار کشته وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/withyashar/16291" target="_blank">📅 22:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16290">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK5dnKO3u-4kQoJhlt3OMx40t7DSbNfCA5LxkCvd8vFepqKlzVrVVRWOTpoDQB6YTv_OX-OFdGt1UiUaG_RSYumw7WNXUAaVbOsYlyhALKSipSadgLlcvsSW0w_HB__A3xqTHah0ikn4laIT2BKK7QbkM3bkOtXgrsUSVAUWzCfaN_IunHtl6e-VvP6qhFCJZh6vFm3bdiAlKbTSWIDzjDIEROH31Zkn2lKQ7sEv2Ez4ph19epkh0uvEJbc4KHvqu33zTNxKkfEIcrCahqfe6pMNQ3UG_SuExlFmQnqsVRVJ9lDjsgTdHUktuvJgURKNRiS6DGmPaCuAXtOWU5swOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو گروه از کشتی‌های نفتکش/کانتینربر تحت اسکورت هوایی و دریایی ایالات متحده از تنگه هرمز عبور می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/withyashar/16290" target="_blank">📅 22:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16289">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سفیر آمریکا: «رابطه واشنگتن و تل‌آویو شبیه یک ازدواج ایده‌آل است که در آن جایی برای طلاق وجود ندارد»
@withyashar</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/withyashar/16289" target="_blank">📅 22:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16288">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78447e35bd.mp4?token=A1jr8XALskPXIP_avJnB9xTXYazJ4fy8kaeNKMz8fglRxI-C6O8NYnWwv9uWAz0cu3nKnBS8EOaLqb6FCtQGJ34-EoOOgDy05abGwJ6SSD6K2XWZ7hsA9XuX-fL5KK0AYMYozmpQfeM571bA2oO0YfQ_Y4m1Jzztaaa-UOBCnoiCi4VHd0Fc86T-Bpr7aW0wIIFoC0cKddJxYeGXzLqqZFwvHtw2F2xZPKQUs3Ep6EzJGUimb1cpJINgKVP6uu68hyBZPvcwrJThuc0FFQRmioT6HmdVHns9fIw0S5MQQYt8E7yL-U7Q0_nufeTctsbtdMCw6GRvGDqFH12BO2D6Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78447e35bd.mp4?token=A1jr8XALskPXIP_avJnB9xTXYazJ4fy8kaeNKMz8fglRxI-C6O8NYnWwv9uWAz0cu3nKnBS8EOaLqb6FCtQGJ34-EoOOgDy05abGwJ6SSD6K2XWZ7hsA9XuX-fL5KK0AYMYozmpQfeM571bA2oO0YfQ_Y4m1Jzztaaa-UOBCnoiCi4VHd0Fc86T-Bpr7aW0wIIFoC0cKddJxYeGXzLqqZFwvHtw2F2xZPKQUs3Ep6EzJGUimb1cpJINgKVP6uu68hyBZPvcwrJThuc0FFQRmioT6HmdVHns9fIw0S5MQQYt8E7yL-U7Q0_nufeTctsbtdMCw6GRvGDqFH12BO2D6Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان پرزیدنت ترامپ توسط سوارکاران خشن (Rough Riders) تا کتابخانه ریاست‌جمهوری تئودور روزولت همراهی شد.
@withyashar</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/withyashar/16288" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16287">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5fcb8e951.mp4?token=JwzTY9f0f1Lq8DDoFvADTBaUQkgecX8YHM-1d00s3Qe3r1wweqrLaf6rw7uDfJXQYX5KPPgai1PmUIzMs__WuedplAGx2YA6z-dJGqzi9oN87NcuNiAMeAWGnn33EFpRy6bT-chp-WUcPUkofU-BQg5ATG18TjCvhz8C5rl7UQrYudPxcdAV3-g_8pGzhwV56aIUHbLWqRqkkeDcOpcS0PYV6XRnS4YXlVYdaj99FiZjwmCCNddJCtVt10R_8jjzlbeRGLtPNh0aG4SsmmRSM2zkRutpNbLjUqKt5B_Mdy8sPXoYT_edCwtFAXv25G0LJpNt17c9mObegLMN4O0t0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5fcb8e951.mp4?token=JwzTY9f0f1Lq8DDoFvADTBaUQkgecX8YHM-1d00s3Qe3r1wweqrLaf6rw7uDfJXQYX5KPPgai1PmUIzMs__WuedplAGx2YA6z-dJGqzi9oN87NcuNiAMeAWGnn33EFpRy6bT-chp-WUcPUkofU-BQg5ATG18TjCvhz8C5rl7UQrYudPxcdAV3-g_8pGzhwV56aIUHbLWqRqkkeDcOpcS0PYV6XRnS4YXlVYdaj99FiZjwmCCNddJCtVt10R_8jjzlbeRGLtPNh0aG4SsmmRSM2zkRutpNbLjUqKt5B_Mdy8sPXoYT_edCwtFAXv25G0LJpNt17c9mObegLMN4O0t0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیروز کریمی روی آنتن زنده صداوسیما: قلعه نویی 5 سانت و 10 سانت رو تحمل کرد ولی 30 سانت رو میخواد کجاش بذاره؟!
@withyashar</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/withyashar/16287" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16286">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8VtvNrKhstWxkp8e4QynIAW3gr9Dy6zlgq27dH8KL5OtTuq7AFe0p0L7O_VIJWIRrdODJmtnvtVRgsyP4PjBuJQz0unxI40ezQCznagI-_dOUPOlYpy3E3chniLc4eisX-t0q7GBkxHsStD_yhNPfrdoW2SuQ6fpzjfL197R8Lpa0iVd-Mzxje10fTcJpVntyd3dgwlbcr7JGp262J2NCbcFjHV1ES595CQRHdnxklvZBvFP7o9GotD-ORBcM9YBV217Q4cvZ5MJUjd_Du6AeQ8cvAL20DP4vmhPyiUcgCdSnHAKBqvTECaFt4V0c8pv0zhWkfrc72kfCHqiIsP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو ۳پا از به گل نشستن کشتی متخلف «خطر شب‌ ادراری
😂
⚠️
» @withyashar</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/withyashar/16286" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16285">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">جی دی ونس: نمی توانم متعهد شوم که در طول ۶۰ روز به ایران حمله نکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/withyashar/16285" target="_blank">📅 21:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16284">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOrvBE_9BlVjiZtWiaHXQkLvhQLg1e3N8X8m7nLtlkTn4gaQ59OOI37aLso2OWRBLZ7FD1n8rRaUbIBUz4YD4tTvuXIY3oIRqZJG7DDQNc_R1cJb4pL8qSr6fASEBNrweBLMM_O-KvWfAzd02wscJ_F72EmrXMt7RwsAu4ikjP32LG7CCRqOhQ-nQ15IDjIrzSYOWkYz20LRoqz_wOM_D407W0xOBWZA1JNjHG4Gsm9NrTdnX0nbtgCQN9HKXyaWMZ4FXx3ZS6JMnl3OXkNb8-4FdsHI94HmXambstBjE4vhkJFe8L1JA6I0YVR8KpwFY5WhyX7qVb0e3NGhmC8ggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با رسیدن ناو آبی خاکی باکسر به محدوده فرماندهی سنتکام استعداد نیروی‌دریایی امریکا در خاورمیانه افزایش می‌یابد.
استقرار ناو آبی خاکی باکسر احتمال حمله زمینی امریکا به جزایر ایرانی و حتی نوار جنوبی کشور را چند برابر می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/withyashar/16284" target="_blank">📅 21:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16283">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fcb1fe97.mp4?token=LrBvxTqAkL6gMDa_BZIOVpooSGhdfPNxywlIFNgSMkJM6akD_Db4IfD7zaxUDzHfHtfZVaowvAoVcDplPV5KxjrwR1cM0a0vt-QMPY7ANyVOoR6pgUXSKooqfp6C0ByoCvwfoUOBw96cPnJWzuHwLrA78YX8-M0K4U2cAHt0ORynMBgNr5ZabaeDvESmFerLiAoeiLgbjfJcdeeUlkZ04WZ7Wi2DS2TFe0s_FlBM0l2edhXvDnk6dyz78eBXQNYLubJWohSXc3nKXURw2gNOQuSYLiYHOO-9AXvthMXtumCW4BPpOF8vqkgR_nr4BYRh3z49cB28n5aKdZHh5nL7LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fcb1fe97.mp4?token=LrBvxTqAkL6gMDa_BZIOVpooSGhdfPNxywlIFNgSMkJM6akD_Db4IfD7zaxUDzHfHtfZVaowvAoVcDplPV5KxjrwR1cM0a0vt-QMPY7ANyVOoR6pgUXSKooqfp6C0ByoCvwfoUOBw96cPnJWzuHwLrA78YX8-M0K4U2cAHt0ORynMBgNr5ZabaeDvESmFerLiAoeiLgbjfJcdeeUlkZ04WZ7Wi2DS2TFe0s_FlBM0l2edhXvDnk6dyz78eBXQNYLubJWohSXc3nKXURw2gNOQuSYLiYHOO-9AXvthMXtumCW4BPpOF8vqkgR_nr4BYRh3z49cB28n5aKdZHh5nL7LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ۳پا از به گل نشستن کشتی متخلف «خطر شب‌ ادراری
😂
⚠️
»
@withyashar</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/withyashar/16283" target="_blank">📅 21:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16282">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گفت‌وگوها با واسطه‌های پاکستانی و قطری در دوحه به پایان رسید، سازوکاری برای جلوگیری از تنش‌ها بین دو کشور ایجاد خواهد شد. تصمیم گرفته شد که بخشی از ۶ میلیارد دلار دارایی‌های مسدود شده برای خرید کالا بر اساس نیازهای ایران استفاده شود
@withyashar</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/withyashar/16282" target="_blank">📅 20:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16281">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/withyashar/16281" target="_blank">📅 20:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16280">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارش ها از وقوع انفجار های شدید و تیراندازی گسترده میان ارتش اسرائیل و نیرو های حزب الله در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/16280" target="_blank">📅 20:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16279">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وال استریت ژورنال: آمریکا در حال بررسی خروج نیروهای خود از عربستان است
@withyashar</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/16279" target="_blank">📅 20:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16278">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رسانه‌های سعودی درباره نشست دوحه:
ایران خواستار اجرای ۵ بند از یادداشت تفاهم قبل از پرداختن به پرونده‌های دیگر شد
ایران اسرائیل را به مانع‌تراشی در اجرای یادداشت تفاهم با ماندن در جنوب لبنان متهم کرد
ایران بر حاکمیت خود و عمان بر تنگه هرمز تأکید کرد و هرگونه مسیر حمل‌ونقل دریایی در تنگه هرمز بدون اجازه خود را رد کرد
ایران بر اجرای بندهای «دارایی‌های مسدود شده» تمرکز کرد
@withyashar</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/16278" target="_blank">📅 20:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16277">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ارتش آمریکا:
امروز ، ساعت ۳:۳۰ بامداد به وقت شرق آمریکا، خدمه یک بالگرد MH-60S Sea Hawk متعلق به ناو هواپیمابر USS George H.W. Bush در دریای عرب فرود اضطراری انجام دادند.
هیچ نشانه‌ای وجود ندارد که این حادثه ناشی از اقدام خصمانه بوده باشد.
سه نفر از چهار خدمه نجات یافته‌اند و در وضعیت پایدار روی عرشه ناو USS George H.W. Bush قرار دارند.
یگان‌های نیروی دریایی آمریکا در منطقه همچنان در حال جست‌وجو برای یافتن عضو مفقود باقی‌مانده هستند و علت حادثه در حال بررسی است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/16277" target="_blank">📅 20:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16276">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اتاق جنگ با یاشار : در سیزن ۹ اپیزود ۵ کارتون سیپسون ها پخش در سال ۱۹۹۷ پیشبینی شده فینال یک جام جهانی بین مکزیک و پرتقال برگزار خواهد شد ! همه نظرشون اینه که این پیشبینی برای همین جام جهانی است !
@withyashar</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/16276" target="_blank">📅 19:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16275">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یک مقام آمریکایی به i24NEWS درباره ادعای آزادسازی ۳ میلیارد دلار از دارایی‌های ایران:
هیچ دارایی منجمد شده‌ای آزاد نشده است و هیچ دارایی‌ای آزاد نخواهد شد مگر اینکه ایران شرایط مندرج در یادداشت تفاهم را برآورده کند.
هر دارایی آزاد شده باید به تأیید آمریکا برسد و برای خرید محصولات کشاورزی آمریکایی برای مردم ایران استفاده شود.
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/16275" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16274">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">واشنگتن پست : وزارت جنگ آمریکا در حال آماده‌سازی برای اعزام نیروهای زمینی آمریکا به لبنان است.
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/16274" target="_blank">📅 19:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16273">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اینترنشنال: مجتبی خامنه‌ای میخواد اژه‌ای رو بعد از پایان دوره پنج ساله از ریاست قوه‌قضاییه کنار بذاره. @withyashar ( البته تجربه ثابت کرده هر چیزی که ترامپ و اینترنشنال بگن، جمهوری اسلامی لج میکنه و بدتر انجام نمیده.)</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/16273" target="_blank">📅 18:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16272">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عراق به گروه‌های مسلح طرفدار ایران دستور داد تا ۳۰ سپتامبر خلع سلاح شوند
دولت عراق به گروه‌های مسلح طرفدار ایران دستور داده است تا ۳۰ سپتامبر، همزمان با پایان ماموریت ائتلاف ضد داعش به رهبری ایالات متحده، به طور کامل خلع سلاح شوند.
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/16272" target="_blank">📅 18:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16271">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190c38d298.mp4?token=d7oYc-5DMyLNrGwpTM_2mC-6fZisXy-4RScJoAlAH24WjoX3VVuGfKn7_Rx1oan1LLuxbRw4kiu2Su2aQeBjEDoey5bVknqAmVmjUYTKErE5XCzLKTt9Dl01tp9Ej_QKCgvHYMuQ87_Sn3MQ1I4lAcydzR9r_LKL8U0fmKNj8lT3gjHvkly5O0ckGt9D1Qt6dfLelouYJZF-9SSROUA5xOY9hBN9qAAft-DWCHrKpDX3CVdCDr870EvtGxUSa2OKRLgKixz60vm4LSJw6KZsMj9HK0R_y0845gsoD2n4tHY9Qh66ZGdkNkH7j-On_EskA9L-SiHOsigvq6fUsdta7LL49XieWZcJH3Lvq9_YsVVYhrlOiHG5WTKfXUPYnHoCuwFrrZgQc3BHLujpteVXnXAwmxNzKMRKnhuFFcahNdb93ODuXaX2_NRfMw-_8MKegfZP3bhgFPK0L3TpKmNOoXxMwRNrtNkq0--og2u9ECY1aBVMUdw6chX1Yr9tZUx5AdURevxD2jy6erXXeXbfma6Rx8bo1TW6sP2Bw2SJdz_3mO25xTu2_SC-CnOoOr6dzCiQ-MO-1ssxxQJ3ADMNKTq_MTCksYX0CeOw-EEssSB0L8QhgMEc19jWjWWqmNYsXR-xoKpX3Yll3JoLXgpCFvCs6-k5Nxd9z2U4Ahtr2p8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190c38d298.mp4?token=d7oYc-5DMyLNrGwpTM_2mC-6fZisXy-4RScJoAlAH24WjoX3VVuGfKn7_Rx1oan1LLuxbRw4kiu2Su2aQeBjEDoey5bVknqAmVmjUYTKErE5XCzLKTt9Dl01tp9Ej_QKCgvHYMuQ87_Sn3MQ1I4lAcydzR9r_LKL8U0fmKNj8lT3gjHvkly5O0ckGt9D1Qt6dfLelouYJZF-9SSROUA5xOY9hBN9qAAft-DWCHrKpDX3CVdCDr870EvtGxUSa2OKRLgKixz60vm4LSJw6KZsMj9HK0R_y0845gsoD2n4tHY9Qh66ZGdkNkH7j-On_EskA9L-SiHOsigvq6fUsdta7LL49XieWZcJH3Lvq9_YsVVYhrlOiHG5WTKfXUPYnHoCuwFrrZgQc3BHLujpteVXnXAwmxNzKMRKnhuFFcahNdb93ODuXaX2_NRfMw-_8MKegfZP3bhgFPK0L3TpKmNOoXxMwRNrtNkq0--og2u9ECY1aBVMUdw6chX1Yr9tZUx5AdURevxD2jy6erXXeXbfma6Rx8bo1TW6sP2Bw2SJdz_3mO25xTu2_SC-CnOoOr6dzCiQ-MO-1ssxxQJ3ADMNKTq_MTCksYX0CeOw-EEssSB0L8QhgMEc19jWjWWqmNYsXR-xoKpX3Yll3JoLXgpCFvCs6-k5Nxd9z2U4Ahtr2p8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : «لوفت‌وافه» وارد میشود
@withyashar</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/16271" target="_blank">📅 17:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16270">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">«جان رتکلیف» مدیر سازمان اطلاعات مرکزی آمریکا (سیا) ادعا کرد که جنگ آمریکا و اسرائیل علیه ایران اکنون جنگ فناوری است و گفت: «کشوری که بهتر بتواند از قدرت فناوری استفاده کند، آینده جهان را تعیین خواهد کرد.»
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/16270" target="_blank">📅 16:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16269">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جی دی ونس: ترامپ به ما گفت با توافق با ایران فعلا تنگه هرمز رو باز کنیم و ذخایر انرژی جهان رو فول کنیم تا بعد ببینیم چی میشه‌.
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/16269" target="_blank">📅 16:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16268">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202c2c732d.mp4?token=dn2RzTg16pHWG8_henJd6CKEmWWljV1Ha8jYF-H8W6rivX6sYYbF3qHPPKougcP1qhl2WZHK-hZDCaAvWdvXpmL8F0UQ8YWMYJhLBqETLsbxjOAyg_iGJyrMuyPG-sqhs48mBiwPgOPy6uvlZ7SLiilBhHPVj12w4S4_0xJOdp8Lknu1IJVwTd8mu8RSzJmsCXihuqnwarWOtXCy6pt_4r6x8SNRzGWGS8qXexs0V78YJGuxFK7Vee0lrtxoEPBfcpP2PoZdOMdnWnEgLl4mWY947_YRDrIYn8n6GPP1iDQtR-sOF-pDfV95eMbl4GdWkx6EETuyHFp0fork1DgTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202c2c732d.mp4?token=dn2RzTg16pHWG8_henJd6CKEmWWljV1Ha8jYF-H8W6rivX6sYYbF3qHPPKougcP1qhl2WZHK-hZDCaAvWdvXpmL8F0UQ8YWMYJhLBqETLsbxjOAyg_iGJyrMuyPG-sqhs48mBiwPgOPy6uvlZ7SLiilBhHPVj12w4S4_0xJOdp8Lknu1IJVwTd8mu8RSzJmsCXihuqnwarWOtXCy6pt_4r6x8SNRzGWGS8qXexs0V78YJGuxFK7Vee0lrtxoEPBfcpP2PoZdOMdnWnEgLl4mWY947_YRDrIYn8n6GPP1iDQtR-sOF-pDfV95eMbl4GdWkx6EETuyHFp0fork1DgTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: منتقدان شما می‌گویند که از ریاست‌جمهوری سود می‌برید.
ترامپ: من سود می‌برم چون بازار بورس در حال رشد است. همه‌ی ما داریم سود می‌بریم.
وضعیت حساب بازنشستگی 401(k) شما چطور است؟ ۸۵ درصد رشد کرده. «متشکرم، رئیس‌جمهور ترامپ!»
من سود می‌برم چون پول زیادی دارم.
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/16268" target="_blank">📅 16:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16267">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ درباره ایران:
ما سه شب آنها را به شدت هدف قرار دادیم، اما اکنون رابطه ما بسیار خوب است.
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/16267" target="_blank">📅 16:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16266">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وال‌استریت ژورنال: یک کشمکش قدرت در داخل تهران، مذاکرات صلح آمریکا و ایران را به خطر انداخته است
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/16266" target="_blank">📅 15:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16265">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پوتین: به دلیل کمبود گسترده سوخت در روسیه،صادرات هرگونه سوخت ممنوع می‌شود،قابل توجه است که ایران از روسیه بنزین وارد می‌کند و صادرات سوخت به ایران نیز متوقف می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/16265" target="_blank">📅 14:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16264">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">غریب‌آبادی‌(کاظم دست کج)در راس هیئتی متشکل از وزارت خارجه، بانک مرکزی و وزارت کشاورزی به قطر سفر کرده است، صبح امروز با شیخ «محمد بن عبدالرحمن آل ثانی» وزیر امور خارجه دولت قطر، دیدار و گفت‌وگو کرد
پس از این دیدار،
نشست سه جانبه مذاکره کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای یادداشت تفاهم برگزار شد
@withyashar</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/16264" target="_blank">📅 14:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16263">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/untiPDhkPz02LTDniS_l06qPZe-mudXRRT2wusS48C3ELyfyiLaF01_K_pZvkNVOeXtI6CT-psYWfilJFR2l6vPoPNjaxSEI6tOujOGH-hfG_wCx0Z06k3U2DzUtgnuuvJJAzK65CidSIB2r64vikd6EsN7qO0qsi-DGf_BKWegwBKrhqBMNLExcYsCdmPMOYne7BwKO2uXcqgM9iHfC7WAGPMIC1vbcgnGtmkijC53kblkHM-tGj1SDnKYHIiB5EXBh4_HbJ0fQrf0uCuH9BD0erfQxg88kTyFzuraiQ_eSBOnpzGgxbR7ZYzFSyyJakDuKvIFHJYHp_GygiwaK1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این بین، جمهوری اسلامی هم بیکار ننشسته، یک هواپیمای ایلیوشین روسی تجهیزات را دیشب به تهران آورده و اکنون در حال برگشت است این در حالی است که خبرگزاری‌های عبری امروز صبح گفته بودند که ترامپ در پی یک حمله تمام عیار است
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/16263" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16262">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8M-QQsEkXfGNBBM8-P6t1ogKbU2nU0-D5HsNDQ6WURD9bQTcW0R57H7yNTdWZz6ctiuK-k0ObyXafZF6AuHF2zt13Vr1rIoYzdeADg6Fypr8k34QdNvH2KYyyG-XFX2aWLSxlYPH7VAWW6D_ebp2Ta6pgu-ePJg7Tuu8G5Q4OzpqzvvgvZvLqMAmtJTEOzRVSczi3YmZblzyumNkmc0DX5nJU-LZlhthm9cHhqb99ij7YTg9rUGwx5YmddnwkbuLK8oyxPjpnyN6UFnMcKU3y1J_pNAswxY7SJNAtCZL-h2SrbsTTUNcOz4s8VrlWJZ9anOrGtO82bG2fINM_Z0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا جهانی دوباره پایین زده و اومد زیر ۴۰۰۰ دلار
دلیل اصلیش اینه که پیش‌بینی‌ها از افزایش نرخ بهره آمریکا دوباره بالا رفته
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/16262" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16261">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jr76KORnnL18JKTeGHziyjGkimCmzANHwCwDGXc2rffFPyOEXz-mJe4EnSExkO_Jiq0jteqtYXNZIuUH9drOIOE7AZ_WV499ZEaHQZLreTnmJdfSpkoUqwZxMDrBrJ8BiUNl7FKVS2GlZDLZgYsMudObid8l2e-wCIaMLRIPhzK4rPUu43t2T-5dJTHNGezINhGQEhJJAQFqTvQCBMNi-LpK95LbH8ERNcWBhuw0s9myW7ShEj06vJA3j1monxsXaRD4-S6RwMsGAv93md-6soOLg5Pp6iKnl_1FHnqooGHnlRbxRaxiusvLWXOqAcRL5zrXITdOXh2kxe9UQ6ceWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق داده‌های CryptoQuant، موجودی نهنگ‌های بیت‌کوین بزرگ‌ترین جهش تاریخش رو ثبت کرده و تا الان بیشتر از ۲۷۰ هزار بیت‌کوین (حدود ۱۶ میلیارد دلار) حوالی قیمت ۵۹ هزار دلار خریداری شده
و
در حال جمع کردن بیت‌کوین هستن
این به معنی رشد فوری قیمت نیست، اما ، نشونه مثبتی برای روند میان‌مدت و بلندمدت بازار محسوب میشه
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/16261" target="_blank">📅 13:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16260">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60dd03797.mp4?token=NeqiYFaWDHNXl9h43f4vk77D6PI1vXIZH2oeq-1XYtZNMwaFnQMNLe-_vgpalGvwhQSn66DPwGpX15R-XWDKyQj7QGLdHhZ5eQqVAcUMyG3nMq1Bpkf5-Oa4kFVHsImKc4IkEd_659FY35lu5nXbKXeJ5Te_N8ozEiUKQCumOX4YQ8BqPv7tts-aA9njaWhOaRk0M4Yf-deRHIi9a3Y0NuYlqKAqU0Of4QMtmqGlMaRxuRJHaFxehRkTriYyd7fDpUA2JJkxGEXNKFOPK3imSwBidJrQEG6xQ5yXx_1ufbs-OtwOKP7SQfo6Eb_QZIxU-rb6VlfSc2JGRIgsgFBMc7D7RnR4HqH0XV80MF_g8sui6wnAGF8N4yWrP7KYWdxmO-6StG1sBMnI5zHnK7MTLEk7n0q5ZLBkvbA-5TvuydvwceQHEHWBFsx7QATtWTWNKfwpIqE75srpbVzrJ3tA3-azpGm-yJ64FFi7BkdP831tcXVmVsqA1ISWMwPJJ5OpTcNIUmBcp8axrUuORmIaLsQCknF69l7H2LqeRxp333Gil_B2a-QiR_dmX4jgzGtNZSdSQ-cNnGlPr38gi_kPN7ynhvo7Fnkxzkr5EfHAkuDxIwXlpTyuwcjX_bZltxcI44or8uMiPbdpB3NmxdPaoxMqE7Cbqh9OBcpUes6ICwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60dd03797.mp4?token=NeqiYFaWDHNXl9h43f4vk77D6PI1vXIZH2oeq-1XYtZNMwaFnQMNLe-_vgpalGvwhQSn66DPwGpX15R-XWDKyQj7QGLdHhZ5eQqVAcUMyG3nMq1Bpkf5-Oa4kFVHsImKc4IkEd_659FY35lu5nXbKXeJ5Te_N8ozEiUKQCumOX4YQ8BqPv7tts-aA9njaWhOaRk0M4Yf-deRHIi9a3Y0NuYlqKAqU0Of4QMtmqGlMaRxuRJHaFxehRkTriYyd7fDpUA2JJkxGEXNKFOPK3imSwBidJrQEG6xQ5yXx_1ufbs-OtwOKP7SQfo6Eb_QZIxU-rb6VlfSc2JGRIgsgFBMc7D7RnR4HqH0XV80MF_g8sui6wnAGF8N4yWrP7KYWdxmO-6StG1sBMnI5zHnK7MTLEk7n0q5ZLBkvbA-5TvuydvwceQHEHWBFsx7QATtWTWNKfwpIqE75srpbVzrJ3tA3-azpGm-yJ64FFi7BkdP831tcXVmVsqA1ISWMwPJJ5OpTcNIUmBcp8axrUuORmIaLsQCknF69l7H2LqeRxp333Gil_B2a-QiR_dmX4jgzGtNZSdSQ-cNnGlPr38gi_kPN7ynhvo7Fnkxzkr5EfHAkuDxIwXlpTyuwcjX_bZltxcI44or8uMiPbdpB3NmxdPaoxMqE7Cbqh9OBcpUes6ICwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکورت و جابجایی دیدنی بی بی نتانیاهو
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/16260" target="_blank">📅 13:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16259">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkqxtZRrSy9--sKJr8DMW-p1IjgYgRlTw6I49APJEk_-YyWPAoPFb45INX_i0cKWx7KVnzRjn-4OHPfY8YP1GqzeBb5f-T6O6yfpynxtLyHP7VXUBiG2YfHg2VTkfX9b0JGwUoSKA7rmGV8xbP8bCIlAm1fJQr1m0aPv6pKVvYebpPMXcTqXkF66WA43v9iMDdw4zA_1Ti7utnfnZ9CN_4L1q9p5FRJmCzz6BMVQ4Iipnei6ZfBSSPI541SCBuOJHup-8GLz1x-NIbMBaGbkUf-9wRYw6cs6iuLMU80Z9g5PIGDQ9p1LyFrhHX808ovQGTKVPogzucdNtugETOnyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت خدمات دریایی انگلیس:
یک حادثه دریایی در ۷۶ مایل دریایی جنوب بلحاف در یمن رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/16259" target="_blank">📅 12:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16258">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رویترز: مذاکرات فنی غیر مستقیم ایران و آمریکا، در دوحه با حضور مذاکره‌کنندگان ارشد و تیم‌های تخصصی در حال برگزاری است
ویتکاف و کوشنر، چارچوب و مبانی این مذاکرات را پایه‌گذاری کردند
@withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/16258" target="_blank">📅 12:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16257">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانال ۱۴ اسرائیل : رئیس جمهور ترامپ برنامه‌های عملیات نظامی گسترده علیه ایران را متوقف کرده است تا مذاکرات دیپلماتیک با هدف محدود کردن برنامه هسته‌ای این کشور را در اولویت قرار دهد در‌ عوض از حملات تلافی‌جویانه هدفمند برای حفظ اهرم فشار استفاده می‌کند تا از بی‌ثباتی منطقه‌ای جلوگیری کند.
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/16257" target="_blank">📅 12:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16256">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فارس : استان هرمزگان بیشترین آسیب را از آلودگی نفتی ناشی از حمله آمریکا متحمل شده است. این آلودگی بخش‌هایی از سواحل بندرعباس، قشم، جاسک، سیریک، بندرلنگه، لاوان، بوموسی و تنب‌بزرگ را در بر گرفته و تاکنون بیش از ۲۵۰ کیلومتر از خط ساحلی این استان تحت تأثیر قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/16256" target="_blank">📅 12:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16255">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">1$ Tether = 175,000 Toman
📈
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/16255" target="_blank">📅 11:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16254">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIPnEhYv6wPYzlyleIXGlbFfGVgRiBuNU1R43W1l_R0MYgEQB-2LltZalrOJ5FrPfYbL-GrjPzNPIwRlbSqrrKfOSpTiHfQUys9HvRuKy90JgZZdsBhd_-Qfg9KpwZyWIMu1iQeQY_lwi_rZ94JW4VIcTmQwYhHPiwQ6JfxeIr1MHq48bJ9nDVP46ROVFKYThKZLGCd5tera60Q3Iiic-1RMyYM1X3cda_Eirb4WILL_4NzuVrSh_wuykJs9muAhRhqVd6vRGpUpyLhAzRn5S6dCcNWSzcsl94miTItgszAlFINdcreoLuJ-g6hE9SeAPecsD5Xlg7sPtIIbD2HjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون شیراز نابودسازی از پیش اعلام شده مهمات عمل نکرده.
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/16254" target="_blank">📅 11:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16253">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlX5Wf-q4bWnaQiTQaiHHEGYOx4fef8wkkJqSOlEGttdn8ffAh1gMaLtlGEdRU_bprThW60R-PDKD2_b5ISa26-CO75P_NFhxQl05ndre3d6GCWZX_eGcAg9g1NpGNt-pqM8fbrdxZ8P2_RAaJdroMMgsxjWLgFqcNkNMkof9Vx07JPdJRl_dh11JEF6GjXQg97-HISXjClyA7gyMeaY-MDnZ38M76nWQuNpz5mU0JwF5AdAoEoSqv-gNGhGnA8bDOo8YNU8hJm5VXUwwcfAWCwLZiFKINSYy1dybOrIx-XpYIau-PsU8gSEq7KFA-jVfqe6vtob6rdnOCaaReLleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند کشتی باری که از مسیری غیر از مسیر تعیین شده ایران در تنگه هرمز، تردد می‌کرد به علت خطای ناوبری و آبخور، به گل نشست
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/16253" target="_blank">📅 11:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16252">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرگزاری های رژیم :
خبر تدفین رهبر انقلاب در نزدیکی ضریح امام رضا علیه السلام کذب است
به تازگی، برخی صفحات در فضای مجازی ادعا کرده‌اند که پیکر مطهر رهبر شهید انقلاب در روضه رضوان و در جوار ضریح ملکوتی امام رضا(ع) به خاک سپرده خواهد شد. این شایعه در پی آن مطرح شده که بخشی از روضه رضوان به دلیل مرمت سنگ‌فرش‌ها، داربست‌ کشی و با پارچه پوشیده شده است.
لازم به تأکید است که نظر و تأکید رهبر معظم انقلاب بر این بوده که مکان خاکسپاری پیکر رهبر شهید، به‌گونه‌ای انتخاب شود که خللی در زیارت حضرت ثامن‌ الحجج(ع) ایجاد نگردد؛ ازاین‌رو، پیکر مطهر ایشان در نزدیکی ضریح مطهر دفن نخواهد شد.
@withyashar
یاشار : امام رضا هم جواب کرد
😂</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/16252" target="_blank">📅 11:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16251">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سخنگوی ارتش فرانسه: ناو هواپیمابر «شارل دوگل» در خلیج عدن مستقر شد
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/16251" target="_blank">📅 11:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16250">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شرکت‌کنندگان مراسم تشییع از ساعت ۶ صبح روز ۱۲ تیر تا یک ساعت پس از تدفین، بیمه شدند
@withyashar
سه‌شنبه ۱۶ تیر نیز تهران تعطیل شد</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/16250" target="_blank">📅 10:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16249">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بی‌بی‌سی: ترامپ در سال گذشته بیش از یک میلیارد دلار از فعالیت‌های تجاری، به‌ویژه در حوزه رمزارزها، درآمد کسب کرده است
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16249" target="_blank">📅 10:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16248">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وال‌استریت ژورنال: عربستان ابتدا دسترسی نظامی آمریکا به پایگاه‌ها و حریم هوایی خود را برای عملیات امنیت تنگه هرمز محدود کرد که با تهدید واشنگتن به تعلیق تحویل سامانه‌های دفاع هوایی همراه شد.
هرچند ریاض بعداً موضع خود را تعدیل کرد، اما این اختلافات و تنش‌های دیپلماتیک اخیر باعث شده آمریکا به کاهش حضور نظامی خود در عربستان فکر کند.
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/16248" target="_blank">📅 09:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16247">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وال استریت ژورنال به نقل از مقامات آمریکایی:
ترامپ در حال بحث درباره احتمال تجدید حملات نظامی گسترده به ایران با وزیر جنگ و رئیس ستاد مشترک ارتش است ، اما تصمیم گرفته است که مذاکرات دیپلماتیک را در حال حاضر ادامه دهد.
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/16247" target="_blank">📅 09:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16246">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=JYtvmu5ZeavaTP_-FAz_EddnmRbcg4tQfletQit0KKCQ6DnloNGAq4q88fbNH-L5-p9Fsu0QVD_R3-6KlvNwhiNiyaIb_kbCXKIYKxh4wS6A_ISkZBFHZs-fK2Nuwi95vakz8jeC3mS1n-VvOHGBuf7XOJTK5JzROAcflLb0iS6IuTsAV3UlpYZw_XobMhlXF6Eo_KEW4H8zO4TWCB_GBe0PTtU83v0S-v7Zq9pWYK5Cl7T83E4RlcYzEY65-rJbnuMOabGPirXBzMUuOG2bCNnmmk-hRj1wcjoZJjDhaYnHXVOlO2YpbIColwNlp8dmbGFR1z2gvDbzAuuSf5wEKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=JYtvmu5ZeavaTP_-FAz_EddnmRbcg4tQfletQit0KKCQ6DnloNGAq4q88fbNH-L5-p9Fsu0QVD_R3-6KlvNwhiNiyaIb_kbCXKIYKxh4wS6A_ISkZBFHZs-fK2Nuwi95vakz8jeC3mS1n-VvOHGBuf7XOJTK5JzROAcflLb0iS6IuTsAV3UlpYZw_XobMhlXF6Eo_KEW4H8zO4TWCB_GBe0PTtU83v0S-v7Zq9pWYK5Cl7T83E4RlcYzEY65-rJbnuMOabGPirXBzMUuOG2bCNnmmk-hRj1wcjoZJjDhaYnHXVOlO2YpbIColwNlp8dmbGFR1z2gvDbzAuuSf5wEKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها) , سپاه پاسداران که بیضه های این ارتش هم نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/16246" target="_blank">📅 02:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16245">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رویترز : مقام‌های فرانسوی تجمع بزرگ شورای ملی مقاومت ایران (مستقر در پاریس) را پس از آن ممنوع کردند که نهادهای امنیتی نسبت به افزایش تهدید از سوی فعالان سلطنت‌طلب رقیب هشدار دادند.
پلیس پاریس این تجمع را که قرار بود در ۲۰ ژوئن برگزار شود، تنها چند ساعت پیش از آغاز لغو کرد و دلیل آن را فضای به‌شدت متشنج داخلی و بین‌المللی و خطر بروز خشونت اعلام کرد.
تجمع‌های پیشین شورای ملی مقاومت ایران، که توسط بازوی سیاسی سازمان مجاهدین خلق ایران سازماندهی می‌شود و شرکت‌کنندگانی از سراسر اروپا و جهان را جذب می‌کند، معمولاً بدون حادثه برگزار شده است.
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16245" target="_blank">📅 02:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16244">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJgGcqn_sYe-kgpuVV1Jub9GIuHCgqPWsmWm1zxfXACg0qGQjn-BXwRyOiStt1q5jX6Jx6xapKb18Q3NvQZ1ubSO_ismXXBOLQHZEigfhou-aXnLmnaxWEt3RxYZLwXgNpEPB4r6vkwa-t_nrvehOSl3wuGzz_PNFDApgqByZHssfOtmyJg1ZyC89DjQR4WmDV5wiwmzOYZHnMcra9X5dWJ28KxM9Ee_KDXbFPjz8z9tnX0qj89hp05ks_yBRAsc81RssPcmZEAiPfYPUXb17MZq-QoG2g1gAsm6WO7Sm1Vsh-0mmil9Skg5FTSb9-yhyj5HVapU1eRxsEvIWby0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است.
از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد تهران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/16244" target="_blank">📅 01:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16243">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو:
حزب‌الله چیزی شبیه به «پنتاگون» را در زیر زمین احداث کرده است
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/16243" target="_blank">📅 01:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16242">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAPczXbouH0iRB6vtbXE-deZnlOaJsBt-wguYppppiOM8bO7G75Q43a42GCrD3nL-iFKMFfCNfuHwnRDKi2q7-taZwRknaZQNxx-iEVYyzpkWrihmDJdrvXbDK6kBRarEFEcu-Zrl9CrQgonlPqu0sS1I6ikkPg6IRqwkMFrf4qyH79FriUUJT5uGW_yqlXfl68a3AQvw6isn48BGBHcBexpf0zPbBdi9kzDObHHi3VwNC6YP8_TnZtfa1TErDW1CzR5X_Ev91ENESDAPsdZfBFKJbndg7vqk3kBkUakSoxZL-X6BGWJnMW5dfU6NjdqnNweXOTRIVuutohNdhnNaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبی خاکی باکسر داره میاد ! ۴ ناو ۱ آرایش رو به جلو و آماده به سمت خاورمیانه  یو اس اس باکسر، یو اس اس پورتلند، یو اس اس جان ال. کنلی و یو اس ان اس پیلیلائو در آرایش جنگی در اقیانوس هند حرکت می‌کنند و تحرک و پایداری آبی-خاکی را در دریا…</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/16242" target="_blank">📅 01:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16241">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رسانه رسمی قالیباف بعد از اینکه صداوسیما مصاحبه‌ رو قطع کرد، اعلام کرد بخشیهایی که پخش نشد درباره این موضوعات بوده؛
پاسخ به ادعای بازرسی آژانس از سایت‌های ایران.
جزئیات پیگیری آزاد شدن پول‌های بلوکه‌شده ایران.
توضیح درباره اعتبار 300 میلیارد دلاری برای بازسازی که تو متن تفاهم اومده.
پاسخ به ادعاها و حرف‌های ترامپ.
توضیح درباره پیام راهبردی رهبر جمهوری اسلامی تو 28 خرداد.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/16241" target="_blank">📅 01:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16239">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8ZpMJ6dmykjOZUOfuNETcqaFbCY6nE5sPcAo5id6xLfvPdXoQVTQI9xyrH92uaUSP50jHjIIEQ2OHkQVMMNMKiXhjcHqKrIrnhpV38V2INJ-xQrui0PITB5rZaF7j1VFIAvWQ5L7LUCNmw6C9jMG9Gfsi8x2Yo_dR32wLWbb0P7kczus8-BVT-JcolkQFKNZN0nnImTQKAlssjy-6XZH1X09dXUyAb71YDjrCmhT3usj3QX7dACfPUJGnioBSD9ISpIWlHf80mRXEPy8AIym7It9p-S88vKZXloumTQICRmb9Sb5vCemXTKwICwvPEhtWlV81YjQtQOd_o_Tn6XrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9663206797.mp4?token=i1JY02z303sWER2mVNUYVmOXQpPAWla_KQgt3WC55_mPtxRmCLGkcfN8-mIX0n5CiOeRUE8i_NFNKhGPxIa5j9rE7SQ0en_DjKw9Antssb9EPfGKsmnkaT6kJP0fCB2hlBorEHxT_xfv8WmwDUiJC1Q-oPx-ioVB76WWj8dnpZRcXS7T-vquY3hLDshPwFliPYqeX0c0oXM7ddrxchIdgNsLedHSFR1n3TU9l-DMKonuLT-4antDhOSUWZGZX_fK9dhJLH8P1osLZCaKW04ItAHm0bBJIRzBkrgF42HGUh2YiM-OylApCbuqX3JBoW3SFgAPZbjSwo2eyV4FCG765g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9663206797.mp4?token=i1JY02z303sWER2mVNUYVmOXQpPAWla_KQgt3WC55_mPtxRmCLGkcfN8-mIX0n5CiOeRUE8i_NFNKhGPxIa5j9rE7SQ0en_DjKw9Antssb9EPfGKsmnkaT6kJP0fCB2hlBorEHxT_xfv8WmwDUiJC1Q-oPx-ioVB76WWj8dnpZRcXS7T-vquY3hLDshPwFliPYqeX0c0oXM7ddrxchIdgNsLedHSFR1n3TU9l-DMKonuLT-4antDhOSUWZGZX_fK9dhJLH8P1osLZCaKW04ItAHm0bBJIRzBkrgF42HGUh2YiM-OylApCbuqX3JBoW3SFgAPZbjSwo2eyV4FCG765g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای افغان به مناطقی در بلوچستان پاکستان حمله کردند و درگیری‌های مرزی آغاز شد.
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/16239" target="_blank">📅 01:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16238">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMgQFsRonRqEHqBlj_MceYWU1cgpQjQvpoGabgUE_MVwkhLVp1Su3xtrDD4gKDuEUPrXw_Abag7fb-DFN_WX2bwC1sb69M9nxWDFc-6G6n7HrbZe8Jmw8kZRgOCJBZ9w4pwJB16zeblC6KyilO1Yo88slD1cU2kpoh9H2mSZFYgYCoYC3awBxPZRey6HfKlkM1dnYZQzDAk8CuR8h6kHGMJk_S_89heRhm_bmw_s_1pEPF8B4EU6ujCQ0h62a29ReO9Nqh-LoDlX3Y-NUZM_Uv68fgHRGOW1Rloau1xNc4_GytVg1SSgYyjDP2K_U-IxQsSD75_p3nRIott9AIRuFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاروان‌های کامیونی پر از تابوت جدید از تروریست‌های حزب‌الله که توسط اسرائیل نابود شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/16238" target="_blank">📅 00:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16237">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وال استریت ژورنال: سپاه پاسداران این پیام را به واسطه‌های قطری منتقل کرد که اگر تضمینی مبنی بر کنترل انحصاری تنگه هرمز توسط ایران دریافت نکنند و اگر ایالات متحده و کشورهای غربی از برنامه‌های خود برای دریانوردی از مسیر جنوبی در این تنگه در نزدیکی سواحل عمان دست نکشند، دوباره تنگه هرمز را خواهند بست.
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/16237" target="_blank">📅 00:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16236">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg5bFXv4KT2mGJvUYpWdL3pePxdct7PD5HECxKouX0FmJJX0RT2uRrcpG2dZcgYIQlOLo_yjXt-pnF9DHGf61StxJw6sJy5ySmIoiRuJG0F7k7NEDeyzqeFpKuLXGYkEqP3h6s9zVDsOzAg_FbIYsw3pvlKCvvfgkbKxXTm67c9ELoTzvWP75qnTvxZJPhsNiggDmg0wFri74M40-BN4hs8u62dZrogFRwrY1YuzXL0_AmjB2dDjIIkF06xMpDdlZNYnt-pgfu-s5y1KGn_E_dWHP99HTWmv7QmwBtRxrfiWtNch54z5w6_mnBsfM7iqOhK0TSyBaP_WkSzIzkiEkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین لرزه ای به بزرگی ۶.۲ ریشتر خلیج کالیفرنیا در سواحل مکزیک را لرزاند.
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16236" target="_blank">📅 00:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16235">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جی‌دی ونس: ایرانی ها یه تاکتیک عجیب برای مذاکره دارن. توی رسانه ها میگن مذاکره نمیکنیم ولی وقتی به ما زنگ میزنن برای مذاکره خواهش میکنن. خب این یعنی چی؟!
ترامپ مایل است بمب‌ها را رها کند، اما فقط اگر هدفی را پیش ببرد.
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/16235" target="_blank">📅 00:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16234">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتاق جنگ با یاشار : چک افسری ! این ویدیو نکات ریز مهمی داره حتما دقت کنید! https://www.instagram.com/reel/DaOSvJUxDdL/?igsh=aGRkbWQyN2ozeTNs  کلیک کنید و کار های اداریشو انجام بدید</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16234" target="_blank">📅 00:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16233">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16233" target="_blank">📅 00:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16232">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اینترنشنال: مجتبی خامنه‌ای میخواد اژه‌ای رو بعد از پایان دوره پنج ساله از ریاست قوه‌قضاییه کنار بذاره.
@withyashar
( البته تجربه ثابت کرده هر چیزی که ترامپ و اینترنشنال بگن، جمهوری اسلامی لج میکنه و بدتر انجام نمیده.)</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/16232" target="_blank">📅 23:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16231">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY1nkeWifMCI8smB1c9qS_0uxbHgGFpRBukcwK-VnG62vz5rf67iPf3sd-aF3Nm76B-krUM9ABGrTbbRRuFlgPXm13pKhPZPTgZLtjoXQXuDnOAK34yqAXmimOcov4mMsjcnAmpvxlat_mAygCge8nE42-MoEZpUb8RYHIdRyBppACBBjaOd3WlHuwFpqeQaKGChy79ygPJ4pSu27UUd_6Nm4VvrNbnm_25IYZe9yqIXpyyaSQxfG-nyKvVga8S7JXvDuWMbg-Hw50tE5pGUbmpCf3uSOA4erwPuIlTk4bbHRM2fflSjs3pO69nMx_bRPwnrAcnaJQVyX95IvN9AVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/16231" target="_blank">📅 23:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16230">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=sfxvrcWKmNjvsngknyErPUGRjJnzD_QeP1id_kA8TUrTmCvMKVZ_bhd2S98D2_yy1BOxmPLLgfFCSaGHBZaGjYwXcWcpyzUZw38wyfrrNfK7jJlzoziQN7zwl_UjkMpvvkZdedL0QyfABtXcJ41j3yO1Cb-SlCJauRZwRKfxRjZ3CGqcDxtYSYPKnld0L_rodcllqDEOsrY57z9ZEBHM4bMv00iI7k7oDuH_WYSCSYUT1Jka35aGIilcpzEhjYjzNEnHlZYdFQ5-JOYpnJnOVNmfNoANzLpFbPCv-lZh8umBOAhRfZEfLdCP1UiFU6BHCaml4ybRa5Uh-fwfLlMDSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=sfxvrcWKmNjvsngknyErPUGRjJnzD_QeP1id_kA8TUrTmCvMKVZ_bhd2S98D2_yy1BOxmPLLgfFCSaGHBZaGjYwXcWcpyzUZw38wyfrrNfK7jJlzoziQN7zwl_UjkMpvvkZdedL0QyfABtXcJ41j3yO1Cb-SlCJauRZwRKfxRjZ3CGqcDxtYSYPKnld0L_rodcllqDEOsrY57z9ZEBHM4bMv00iI7k7oDuH_WYSCSYUT1Jka35aGIilcpzEhjYjzNEnHlZYdFQ5-JOYpnJnOVNmfNoANzLpFbPCv-lZh8umBOAhRfZEfLdCP1UiFU6BHCaml4ybRa5Uh-fwfLlMDSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : اگه لازم باشه، برای بار سوم به ایران حمله میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/16230" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16229">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16229" target="_blank">📅 23:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16228">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سی‌ان‌ان: آمریکا و کشورهای خلیج فارس نهادها و مقامات مالی حزب‌الله رو تحریم کردن.
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/16228" target="_blank">📅 22:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16227">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbpNvW4spfdPpFYF-gfu7EIlD33QbGLGvroDxDebq2NkMVJB6z9LDHLNeRZlNDJUhHaod429PnVgWVLtz2Mw6UeGbt5YFLlEJxWfh6iB7e9RqtPNXnyQpuVLJfWyEa94gLSygQ4tZXzDJjrCiR--qRD6YRwpUsJoSbODTStU4JHC3n4XSbVoUYTBcp8Mz5YjjrX_1RuXpN3F8snMeeAsXScZXm0BsraodYWTUPIwFbHvrHhDth0bNpmQsBqJc8M8WxQpbgG9PEEoJtIGunLqvXBUhXWoadrRhGPFhiDijlXSKdu0S55xLiUlqdviDwV-aQhZiNpqWA7P3JKGAiwiIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تابوت های آماده شده برای خامنه ای و خانواده اش
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/16227" target="_blank">📅 22:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16226">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔸
فرمانده سپاه تهران : خودروی حمل اجزای خامنه ای به شکل ضریح حرم امام رضا طراحی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16226" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16225">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ در تروث : مایلم به رئیس جمهور شی و کشور بزرگ چین به خاطر پیروزی بزرگشان در قانون شهروندی از طریق تولد تبریک بگویم!
@withyashar
یاشار: ترامپ در آغاز دوره جدیدش فرمان اجرایی‌ای امضا کرد که می‌خواست اعطای خودکار شهروندی به بعضی نوزادان متولد آمریکا را محدود کند(پدر خودش با همین قانون آمریکایی شد چون پدر بزرگش آلمانی بود)، اما دادگاه‌های فدرال دوباره آن را متوقف کردند الانم  عصبی شده داره به چین تبریک میگه
😂</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/16225" target="_blank">📅 21:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16224">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتانیاهو در خط مقدم جنوب لبنان:
«حزب الله زمانی قوی‌ترین ستون محور منطقه‌ای ایران بود، با تقریباً ۱۵۰ هزار راکت و موشک که به سمت اسرائیل نشانه رفته بود. امروز، تنها حدود ۸ درصد باقی مانده است. اگر تهدیدی برای امنیت یا سربازان خود شناسایی کردید، فوراً اقدام کنید. منتظر نمانید.»
پیام ما به ایران و حزب الله ساده است: شما اینجا جایی ندارید. آینده لبنان باید توسط لبنان و اسرائیل تعیین شود، نه توسط تهران یا نیروهای نیابتی آن. هدف ما امنیت و رفاه پایدار برای هر دو طرف مرز است.
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/16224" target="_blank">📅 21:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16223">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزیر خزانه داری آمریکا : فقط چین نفت ایران را خرید
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/16223" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16222">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رژیم چنج ؟! محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی استعفا داد @withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/16222" target="_blank">📅 20:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16221">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رژیم چنج ؟! محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی استعفا داد
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/16221" target="_blank">📅 19:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16220">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=EfYL-WyRmH3whX3ou42dEII_H4YeMyjnU3wF5PDyHVYzHTeSXrMU_Ef9DHQXrcMhWbbmxemXxwbuM2Pal2KlIi5Xv6YuC-sYFs1eNzGsjNIpMwJVbM7UCn487YdudfsX_Q9J3dGOsZceDj39MzPyQCjmR3ScBV-53FaZD-XqJvUF4Ri99so4STMSKDpnSQSuLLpwOjfQXnPePP96w1d-RePChjSnsOG80Xlnzz1DpuaUZRjE1CrMBN7PqJvUqwMNS0oBYc0qhueNmA20peC1AfZMLd8Qtoo_A4w0-WHNf1pGmGOw8K34Dsa4gnKkw0Ozw6sZdZ7E91HWobSHYBakfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=EfYL-WyRmH3whX3ou42dEII_H4YeMyjnU3wF5PDyHVYzHTeSXrMU_Ef9DHQXrcMhWbbmxemXxwbuM2Pal2KlIi5Xv6YuC-sYFs1eNzGsjNIpMwJVbM7UCn487YdudfsX_Q9J3dGOsZceDj39MzPyQCjmR3ScBV-53FaZD-XqJvUF4Ri99so4STMSKDpnSQSuLLpwOjfQXnPePP96w1d-RePChjSnsOG80Xlnzz1DpuaUZRjE1CrMBN7PqJvUqwMNS0oBYc0qhueNmA20peC1AfZMLd8Qtoo_A4w0-WHNf1pGmGOw8K34Dsa4gnKkw0Ozw6sZdZ7E91HWobSHYBakfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خالد مشعل از رهبران حماس مرگ مجتبی خامنه ای را لو داد
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16220" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16217">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خالد مشعل از رهبران حماس: مجتبی خامنه ای کشته شده
@withyashar
🚨</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/16217" target="_blank">📅 19:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16216">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتانیاهو: اسرائیل و لبنان دو کشور دارای حاکمیت هستند و حزب‌الله باید از بین برود.
هدف از مناطق امنیتی در جنوب لبنان دور ساختن خطر از شمال اسرائیل است. ظرف هفته‌های اخیر 9000 عضو مسلح حزب‌الله حذف شدند.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/16216" target="_blank">📅 19:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16215">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsIupb-SinL-GeaiPA6ZD3KBkDablZUO5bhGpbkanbxfU1YjdnybJ7Z7rlpIV7LiYqdDpkB6Ym08pun_TULP0BMsuCf2tbO3sxlpsF1iZfd5mlc3a-kZd9ArxbuEyfnqOQq3Dl_0LSrRqRNstWnqkm1dGipYT8uVyJK_4KGdsovHvRb2sAEut57D7Cxm24oBr9HbXdrmG43lUCKh3RcX95v0xYFOCg7T_sbhFGFd-k3W0BLr6DqF-wnerj9A1Ety-Z-Z0WVYZdW6hx5t4aFyvYNpCwECdRerJ345_T0bonDmzc-tnm38V1azrTzpZeHnYhI1JtsnoXyT1i6jhI9Uig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: اولین آیفون تاشوی اپل هم معرفی می‌شود
iPhone ULTRA
اپل احتمالاً در ۸ سپتامبر ۲۰۲۶ از آیفون ۱۸ پرو، آیفون ۱۸ پرو مکس و نخستین آیفون تاشوی خود رونمایی خواهد کرد. به گفته مارک گورمن از بلومبرگ، این تاریخ محتمل‌ترین زمان برگزاری رویداد معرفی محصولات جدید اپل است و در صورت تغییر، مراسم ممکن است یک روز بعد برگزار شود.
آیفون تاشوی اپل، که به‌طور غیررسمی
«آیفون اولترا» نامیده می‌شود، گران‌ترین گوشی تاریخ این شرکت باشد.
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/16215" target="_blank">📅 18:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16214">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N75m5OrUGQeLYIGPPFDHYvi2F_aS8OA71xWPL-LtDQcxB8cxFxyp0jNgcFRzE0CxuuVb8ieTIhjR11TtVgz8qxjkEyxEqg_GdsBcroXhDBNRemR0NIMriSB2sIF_vUWIxjCrAQVVOhNiI42KQjtkCB6JTa1wsqW6iuFwjVAI86V5Fx8bRbzYFHsUdrFMdTZim7mYopnHKE7dQtD83dGlxw-I2RZwNJKpe5oREIYign_9VuZCe9Cz1eJb-D8NKnOBYc_NJhglGZcCZJwn1N8wzSLDjVI_63KRhwLhlvSMQOmTwD5A99HXwMZMqqHlRE1--7NSZdIQHr3fo9sAmbeVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
"پیروزی بزرگ: دیوان عالی ایالات متحده همین حالا علیه حضور مردان در ورزش زنان رای داد و این رای، آن وضعیت مضحک را کلاً منتفی میکند."
@withyashar
یاشار : منظورش مردان تغییر جنسیت داده هست</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16214" target="_blank">📅 18:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16213">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-5lMG3pKn420Y5JcUGluYkfUcpV5dzRuCWkLbSCtk1lqXRChGBJFNIPW1NzwAv79kLy9co5CMiYS2NQ5K8w200XXzUvtyLnTqfvK2io49jwPaLcagoDvORzgBpjBpKit-wQx7NS9Mqw4RxRiMWA5MtIfT5Zd6G3vzDRWiau3LbByqJt1PAVQa08Pdgpk7aRS6W8gJ4GKERiuuF4vHxZenp-khKO8atqfPlEseyrxtDLKxMzOYvrpqvxFxXf1BpRttmQBQUo7S2-cskKwac1QDQlrNfUOOrsrAdAlGDeY5d7xpIYhSnI7ylM9aB2fV2OE3NJ2AS3SiM5CsU2cy6xrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/16213" target="_blank">📅 18:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16212">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رسانه‌های عبری : «پلیس و سرویس امنیت عمومی اسرائیل (شین بت) یک شهروند آمریکایی را به ظن جاسوسی برای ایران دستگیر کردند.»
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16212" target="_blank">📅 18:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16211">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
📩
درخواست همکاری  اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:  نام یا لقب نوع فعالیت / حوزه کاری: سابقه کاری: آدرس لینکدین: (خیلی خوبه باشه) آدرس اینستاگرام: (اختیاری) آیدی…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/16211" target="_blank">📅 17:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16210">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وای نت عبری : یک هواپیمای مسافربری شرکت هواپیمایی الکترا ایرویز که با نام تجاری لات به سمت اسرائیل در حرکت بود، پس از آنکه دو جت جنگنده نیروی هوایی به سمت آن شلیک کردند، در هوا چرخید. طبق گزارش‌ها، خلبان دکمه‌ای را فشار داده که هشدار ربودن هواپیما را می‌داد. این هواپیما از ورشو پرواز کرد و در آسمان ترکیه نسبت به ربودن هواپیما هشدار داد. پس از آن، بر فراز قبرس پرواز کرد و پس از عدم دریافت اجازه فرود در قبرس، برگشت و مسیر خود را تغییر داد. مقامات ارشد صنعت هوانوردی این حادثه را بسیار غیرمعمول و خطرناک می‌دانند و تحقیقات فوری در این زمینه آغاز خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16210" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16209">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آتاانتیک : اسناد منتشرشده نشان می‌دهد با وجود هشدار قبلی ترامپ درباره عدم استفاده از سیگنال پس از یک افشای جنجالی، مقام‌های ارشد دولت او همچنان از این پیام‌رسان برای هماهنگی‌های حساس استفاده کرده‌اند. طبق اسناد FOIA، دست‌کم ۱۳ گروه گفت‌وگوی سیگنال در نیمه اول ۲۰۲۵ فعال بوده که یکی از آن‌ها با عنوان «Iran/Ukraine Planning» به بحث درباره ایران و اوکراین اختصاص داشته است.
این گروه‌ها با حضور مقام‌های سطح بالا مانند مارکو روبیو (وزیر خارجه)، پیت هگزث (وزیر دفاع) و دن کین (رئیس ستاد مشترک) اداره می‌شدند و برخی چت‌ها دارای حذف خودکار پیام‌ها (۸ ساعت تا یک هفته) بودند؛ موضوعی که نگرانی‌هایی درباره نقض قانون نگهداری اسناد فدرال ایجاد کرده است.
در حالی که کاخ سفید استفاده محدود از سیگنال روی گوشی‌های دولتی را تأیید کرده، این اپ برای تبادل اطلاعات طبقه‌بندی‌شده مجاز نیست. با این حال، وجود چنین گروه‌هایی به‌ویژه درباره ایران نشان می‌دهد این پرونده همچنان در بالاترین سطوح تصمیم‌گیری آمریکا به‌طور فعال در حال بررسی و هماهنگی بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/16209" target="_blank">📅 17:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16208">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyTljAGg4EYiWKaB8O58N2ag95IQxu3bosFm-SDeDJ5CBV6o-EowB_T9WkPSAkhON9oT5Phf6Ll86r1AzpUnUagxhPSoEDPRJnD3QegRoLS8v-3TjNPyymcfJEwQZUvNlGjXFZhtbqjBpYOxTnEjnEcnzEV7AdcQGf1XmmNmwMmUbVag-Ap8ssOC1f6Vy-RVYAaEydg2XwuhXDXricmgwlJux5YwAmcc7UdMhXmu0OFiuieSF2MEGoN63ZTnat8K8iws_lCOtLpFvmsNQWUPOaJjwu3j6R_4e2rpdWgdQAiKtq1IwTIiELdPMWXB2uelJ_FNrHqd2UaoF0P0hwA_ugXQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyTljAGg4EYiWKaB8O58N2ag95IQxu3bosFm-SDeDJ5CBV6o-EowB_T9WkPSAkhON9oT5Phf6Ll86r1AzpUnUagxhPSoEDPRJnD3QegRoLS8v-3TjNPyymcfJEwQZUvNlGjXFZhtbqjBpYOxTnEjnEcnzEV7AdcQGf1XmmNmwMmUbVag-Ap8ssOC1f6Vy-RVYAaEydg2XwuhXDXricmgwlJux5YwAmcc7UdMhXmu0OFiuieSF2MEGoN63ZTnat8K8iws_lCOtLpFvmsNQWUPOaJjwu3j6R_4e2rpdWgdQAiKtq1IwTIiELdPMWXB2uelJ_FNrHqd2UaoF0P0hwA_ugXQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت دفاع اسرائیل و شرکت رافائل در بیانیه‌ای اعلام کردند با توجه به تجربیات دو جنگ اخیر با ایران، سامانه‌های پدافندی گنبد آهنین و پرتوی آهنین را برای مقابله بهتر با پهپاد‌ها،راکت‌ها و موشک‌های کروز ارتقا داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/16208" target="_blank">📅 17:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16207">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">روزنامه لبنانی المدن گزارش داد:
توافق‌نامه امضاشده میان اسرائیل و لبنان در پایان هفته گذشته به
قطع روابط دیپلماتیک ایران و دولت لبنان منجر شد‌ و عباس عراقچی در پی امضای این توافق‌نامه، سفرش به بیروت را لغو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/16207" target="_blank">📅 16:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16206">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از خبر تشکیل نشدن جلسه جمهوری اسلامی و آمریکا تتر شد ۱۷۲،۵۰۰+ و بیتکوین به زیر ۶۰،۰۰۰$ و همکنون ۵۸،۵۰۰- اومد و نفت برنت +۷۴$ شد
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16206" target="_blank">📅 16:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16205">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الحدث: منابع می‌گویند ایران تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16205" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ستاد مراسم دفن خامنه‌ای: مردم برای نزدیک شدن به جنازه علی خامنه‌ای اصرار نکنن.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16204" target="_blank">📅 15:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16203">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سخنگوی وزارت امور خارجه:  فردا در دوحه با قطری‌ها «دارایی‌های مسدود شده» مذاکره خواهیم کرد. @withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/16203" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16202">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjWbAM6WRyZ62-_w7XpRR-j5c8CzmmMwgvaHRzJSdw62g_zwFc0h6Cq_g2Iuw-cg7ajzEm7ZycOLCX5uNTDggXRcSNYyjvuPcScTUgNeXmTu0D1xENU6URU7tWXhQtG4WJT7N6oTsclgiufW2zrdinyQVoVr2Kv-axZJX3npHPPKtMOdItY1_Pubr1YlkCJRWB1BHkzdHhhXOF-rpFKXq20w_GPo8YGDhsXdy_D0z6Knx3hH92_NY3pE7Bvt08R7Dk9hKfth4iCX9U52UWHvMTZX0qGlqS9nX8PTOZhY8dyvGJb2Al8-ekOWgVW0PapswAeI45T9jSWIFfQ8mzFrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانا کوآکو بونسام، جادوگر مشهور غنایی :
کیپ‌ورد آرژانتین رو حذف میکنه
،
من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/16202" target="_blank">📅 15:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16201">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سخنگوی وزارت خارجه:  آمریکا صراحتاً دربارهٔ پایان جنگ در لبنان تعهد داده و باید به تعهدش عمل کند. @withyashar
😂</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16201" target="_blank">📅 15:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16200">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سخنگوی وزارت خارجه:
آمریکا صراحتاً دربارهٔ پایان جنگ در لبنان تعهد داده و باید به تعهدش عمل کند.
@withyashar
😂</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16200" target="_blank">📅 15:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16199">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhjMwy9LeYPF6EmsIFqVfhpB2Lcuw_qx6D7e67AFTWQo2-KBAAfNNIA7jXBgZb8nxeLRJTGTLbWp6UPwzKMEUfgNgWl5stQmtT6UlRuqpljrnnmzYv71Asmkw1aqXGD1RJwyU_pxtyZmI5Xl9Vh-8dcDGkaLlNrwRlrL2LctjZW413iMDlZCLvuHF31_8lv0EHmo4TyAa7M_Py36NtjIhEYP9TSPd7H7WzKs4PeAQuZDiiXYWjaG--oGtimjETIZU_vjMw43BC1DuHtTtGFePa14TfpXVbliMqTQs6Bdf8mngsuIoxONRVUycuuB7dNfy_3-0GwE_6sccDD9cwgFbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر وایرال شده از تعزیه محرم
قیافه بعل یه جوریه که داره میگه خب عاشورا من چه کاره‌ بودم
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/16199" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16198">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دبیر ستاد تشییع جنازه خامنه‌ای :
مجتبی بخاطر تهدیدات دشمن نمیتونه تو نماز میت پدرش شرکت بکنه و باید مخفی بمونه
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16198" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16197">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فاکس نیوز : ویتکاف و کوشنر به سمت قطر حرکت کردند  @withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16197" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16196">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر : هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/16196" target="_blank">📅 14:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16195">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_mxwTOdfsGSpgdxSBq-LSQkmlBAwR3mwiSs2RqbhbXcIjsOh7hZ48hBrxc7xMVAuqjBojVtod8GquM7JULIpHbbIQWvl4pS5wUmiqRKfDZf1sHmFiu2RExiI7XneO4eh1QuAM2nR3v2I3sByrkCzkUdkBn7mAAIxRVK-5J2oy05vk2Hnb-0fGtl_Qm0E54G8ItDBtbOxxLDmvs_ee93VARrq3U7N6JXeXgwNFkaNzEXF-S8Tkf-vLdwQ4Ia4THImnn27N_EHP_HKWEyVLlgcim8Fa-YxrPoVR7JeG1zTZN_RGz-p0JTCO9I-scF956bcUO08Hm5MYJKS13Gka12Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی هوایی آمریکا موشک ضدکشتی LRASM را با بمب‌افکن پنهانکار B-2 عملیاتی کرده و در رزمایش Valiant Shield 2026 با آن یک شناور آبی‌خاکی بازنشسته را غرق کرده است.
در حالی که B-1B از قبل این موشک را حمل می‌کرد، تلاش برای افزودن آن به B-52 و P-8 ادامه دارد، اما B-2 فعلاً تنها پلتفرم برد بلند پنهانکار برای شلیک آن محسوب می‌شود.
ترکیب برد بلند LRASM با پنهانکاری و سنسورهای B-2، توان حمله دقیق و دورایستا را افزایش داده و تهدیدی جدی‌تر برای ناوگان‌های دریایی، به‌ویژه در اقیانوس آرام، ایجاد می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16195" target="_blank">📅 12:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16194">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر امنیت داخلی آمریکا:
پس از حذف ایران از جام جهانی رقصیدم
روزنامه نیویورک تایمز گزارش داد، مارک‌وین مولین، وزیر امنیت داخلی ایالات متحده اعلام کرد که پس از حذف تیم ملی ایران از مرحله گروهی جام جهانی ۲۰۲۶، «رقص شادی» کرده و حتی «چند آهنگ» خوانده است.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/16194" target="_blank">📅 12:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16193">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک منبع آگاه غربی:
ممکن است اسرائیل ابتدا در هفته های آینده وارد جنگ با جمهوری اسلامی شود سپس ایالات متحده آمریکا به اسرائیل ملحق خواهد شد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/16193" target="_blank">📅 11:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16192">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وال‌استریت ژورنال گزارش داد که مارکو روبیو، وزیر امور خارجه ایالات متحده، توانسته است دونالد ترامپ را متقاعد کند که اسرائیل باید حضور خود در لبنان را حفظ کرده و علیه ایران اقدام نظامی انجام دهد.
در همین حال، جی‌دی ونس، معاون رئیس‌جمهور، ناچار به عقب‌نشینی از موضع خود شد و در نهایت اعلام کرد که از توافقی که با محوریت اسرائیل شکل گرفته حمایت می‌کند، نه از ابتکار عمل ایالات متحده.
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/16192" target="_blank">📅 11:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16191">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIrfhUvpwzZsgr-FdqRXOB0cwKOAbmSGAq5_tIPm9jKxeY8WmIpYs5wugLfsjre50R4q5rNFGoYkusJ2-uP1SSwlMndEJGxgJ_1SBpe3Az76r9KI52d-Ofx_C9vgnUMayvPQpt3jdXT-q8xYc-yFDbQrAV3NskD12cnhNm0fHe-QvFCrnyQ5P7nHhL7LMMTzpoztbVEaF-SlbZjXAAvXM5cHBMWSzsxbRhS9rY-S4U6yEbsGNRwj-DW0HvFeOsB1io57Da-nVvM4vvdicOG5D1f9CodHtwQi2a6MhUBknATikkejn3Kbx84I3oWlr6SEoJw-WcM6UaeWVEw_DiM-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین تصویر ثبت شده از محمد اکبرزاده قبل از تصادف و مرگش
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/16191" target="_blank">📅 11:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16190">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajhaWGdGzszeAo5aeCi4tsG7zVn_r_bXmOooKMejYoQFwxi4NYwVsGSllq6yqN1sL3gXy6wDkBTD6qZDhh7EVo_mKI41NAVMnLu1mpK43FfKo57YoAN_Ll2CmnSrNgp27G50Ebu_lLl2l-kOhpr7heWxek69mS1qSVlEvyS05IZ2iALeDmVNN06DgRqWvsir9UT9RioPUioeqZXyKq4Kf0KxL_sGXnT1N9pYc_mlcHtUXfjmKBLYTeTpeYjzaJu273MQKybVsSigplHnGSh40nK3exchPg21bRl-DqoBBfHAi0RmnOV6Lt8N6XhyEmB7YLDff6uF3Ng1ivKqeSQhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان انفجار مهیب و برخواستن دود از سمت فرودگاه شیراز
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16190" target="_blank">📅 11:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16189">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اسرائیل در حال آماده شدن برای شروع مجدد جنگ تمام‌عیار علیه ایران
بر اساس اطلاعات موجود، اسرائیل در حال آماده‌سازی یک کمپین مستقل برای آغاز دوباره جنگ تمام‌عیار علیه ایران است. این تحرکات نشان می‌دهد تل‌آویو مسیر جداگانه‌ای از آمریکا در پیش گرفته و انتظار می‌رود در آینده بسیار نزدیک وارد فاز عملیاتی جدیدی شود.
در همین حال، فعالیت موساد در داخل ایران به‌طور محسوسی افزایش یافته و شتاب ناگهانی این تحرکات، از تسریع آماده‌سازی‌ها هم‌زمان با عملیات مستقل اسرائیل حکایت دارد. هم‌زمان، انتظار می‌رود در روزهای آینده موارد بیشتری از انفجارهای مرموز، آتش‌سوزی‌های صنعتی و حوادث مشکوک در داخل ایران رخ دهد؛ رخدادهایی که با الگوهای تاریخی خرابکاری و عملیات پنهانی موساد هم‌خوانی دارد.
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16189" target="_blank">📅 11:05 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
