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
<img src="https://cdn4.telesco.pe/file/cbU3eORFKmYNVSaWUlIQMdEaNUhjNftOgBwQ1h5nHZ397Szdl2nKaEWa2E3WS0-f5klnTNxrnEtX6ckcMQJ_mlvM5exD7qdh9ILCj8PgAZD8xcT3e2a4BewtfomKlz9maQQ8N5hsJ67-cOHiMZkEw_-1f12kU4f8OllskMgvBPTouWNppR1eDfpIuOG1jr3yYpSqBjySfmHIhdUOjZ5M-k08rUcUq6GHZ2UFgrbnplzhFKqyNkCbj-PEDdbAjH__6FZfCWZGoM1GW5hxcatieEb-AAHpFq6mIYMVoyZptkXZlPY3AjvTVZ-LvjSeAD4U86Unv89fLJ1N6Kf9m9nQAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 10:24:21</div>
<hr>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=EQDqqUnmmainNW4tviUqMqoTQmCtCnAcytNt7YAFLSWRrA1ORHLYBc1GNW9hBgsIyYLMTR5IBxu6PXQciTqnEBnx147Lce8ij6qdUPeM9sOWsPJO-p4bYpFIRZDirBGhlXUVwU5CuxNkLWPVcaPFCB46Bc4evjZtNBH-OLdEk_nm_MxYANz3pkxKur017LU_7r8Lv3vIuS3tGrg0sLGq2zfrqQFh1FLI7LQ1p1nEeRSTYyjGMGatLTIhjn-05X7a9XC4vQGszGAzH6Q8R09tuFBnT5BWVY8TBvVRaHitBP6Py9AkDQ3lbek3qXjPuCTR7jwKl6vovs6XVlzNEI2rYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=EQDqqUnmmainNW4tviUqMqoTQmCtCnAcytNt7YAFLSWRrA1ORHLYBc1GNW9hBgsIyYLMTR5IBxu6PXQciTqnEBnx147Lce8ij6qdUPeM9sOWsPJO-p4bYpFIRZDirBGhlXUVwU5CuxNkLWPVcaPFCB46Bc4evjZtNBH-OLdEk_nm_MxYANz3pkxKur017LU_7r8Lv3vIuS3tGrg0sLGq2zfrqQFh1FLI7LQ1p1nEeRSTYyjGMGatLTIhjn-05X7a9XC4vQGszGAzH6Q8R09tuFBnT5BWVY8TBvVRaHitBP6Py9AkDQ3lbek3qXjPuCTR7jwKl6vovs6XVlzNEI2rYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7U6VgsmWc6M0-vWa9P2SnAMmQ9Gp16g3XE_5UurUNL4IlTlKSRx-pA0V2WLJXDvF1OQQbYl0Fv6lL6vOjD_knC2Qm8xTG7d4EK2qW9viZqtLaUEsk-a3hRKaHsOoGZaiNt-sq2QeEwGRYlUGzG2JVLb9e_0ITB_ZUsBUDyfcOujpvBUAeOAwDAXKbaN-_0Khaqt-tzTRyevu3MxYUL79MaOA3o5d5tJGRGpeg5vSv_T1tZW2EYVVpUTpWzPcMtVrZqMIlODJNbm4A0EBvxRHor3Xrbhn4wpJnO6EARVCApNvIoR3cn0NDKeNBRQtHx-iRTESFnpMVSQBxVvTtBmuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwIKd6DytcskgrREZ8hwA8c0pD0sZgM_-vgLSFSuppsLWvo4lKHUdnYamvU6KTJ0ZIwie4YA-P8WvlGHSSsdL1Tqj1EqYmTBJtXSZZJjRFO3ivP5mNbMPqYPVtPXuQk9OJ3aio7IybF7LKje0fKB21QUwTvctk4viQjjQTVEGzMXgeQYKOZ-JI-ojiPVYjQYGeBhs_G-zPRglqIgT0eNEBsIyy61lsLPDIe3zNaTwlZG02u33BI7OSk33P83sDXz49KXOUPsyBV0Igb4hJ2yXW5ne1QUNBSUjH4NSib_WEtNlf3eOJo1lKyP202mi84jZO9uilhtDq90cEmta9cboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!
این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.
🔺
ارتش آمریکا همچنین دیشب به چند پل دیگر در شمال بندرعباس حمله کرد تا ارتباط زمینی بندرعباس با بقیه مناطق کشور دچار اختلال شدید بشه.
🔺
بین ۸۵ تا ۹۰٪ واردات کانتینری کشور از بندرعباس (بندر رجایی) صورت میگیره. ماشین‌آلات، قطعات خوردو، تجهیزات الکترونیکی (لپ تاپ، گوشی و…) مواد شیمیایی، مواد و تجهیزات بیمارستانی و… همه از این بندر وارد ایران میشه.
🚨
کالاهایی چون گندم و روغن، برنج ، ذرت و…عمدتا از بندر خمینی (شاهپور) وارد می‌شوند.</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=XvbzOqCHC6WprXv2z7mdMkC-4iWEHIkbpZYqa3PVxCjR459d3FR2VYqZx93Oux4K-tAVg_pjtdcreqeEfXlF99UsDcJkfWLwJf8LNe1uuBFZB-jv6oJSegjPTNugft3XVuubVuTykDpyZb-lGSVIjrsCd4gzv2h7BvnqU1Llrq6jdqYh2tMQjgYryMP_CUkZcVxJh6pnbRjehtC4zRkuIZzajjKh7DN7OYGYzAnfS2DjFoxI1cl7oeEQweqE_33qj_os53X5njkrodDZYAUidogCtyi9WAST-5Sw_tcTVKO-6zmiLmbbG_34375LHHoEruunshCKDoxV_JPmK764WCP6wsZOSsW-gnGjMdTuyV3-Z9aoyyuc0OV3Zi-7hGQxldeJj2MIklCUxjnDxGGUQ4BP071Am6HviihHg6sVc_5iJ8ceL6PzF2WyY1kmvg3UngFBeMsgvqX41LF6RR6OSnVvzy6Gol3b-IaYqDvt48MlqRK4A3p6LsahP_z05zhUUE377f2B4W5mYdJCYMimxsMjMV2FDW4zXap3me9PlZJhWltiEkNYY6b22kno8x0Ap32hsBDDqOdERnr_PmFPEkcK9iqilKNgDsZNGvSBT75MGPvrmbjqbovD7rBOHH8L_jc3DB5HKQ25XSMBT8WojH2aeazv3q_FCBJ3BIhw-eY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=XvbzOqCHC6WprXv2z7mdMkC-4iWEHIkbpZYqa3PVxCjR459d3FR2VYqZx93Oux4K-tAVg_pjtdcreqeEfXlF99UsDcJkfWLwJf8LNe1uuBFZB-jv6oJSegjPTNugft3XVuubVuTykDpyZb-lGSVIjrsCd4gzv2h7BvnqU1Llrq6jdqYh2tMQjgYryMP_CUkZcVxJh6pnbRjehtC4zRkuIZzajjKh7DN7OYGYzAnfS2DjFoxI1cl7oeEQweqE_33qj_os53X5njkrodDZYAUidogCtyi9WAST-5Sw_tcTVKO-6zmiLmbbG_34375LHHoEruunshCKDoxV_JPmK764WCP6wsZOSsW-gnGjMdTuyV3-Z9aoyyuc0OV3Zi-7hGQxldeJj2MIklCUxjnDxGGUQ4BP071Am6HviihHg6sVc_5iJ8ceL6PzF2WyY1kmvg3UngFBeMsgvqX41LF6RR6OSnVvzy6Gol3b-IaYqDvt48MlqRK4A3p6LsahP_z05zhUUE377f2B4W5mYdJCYMimxsMjMV2FDW4zXap3me9PlZJhWltiEkNYY6b22kno8x0Ap32hsBDDqOdERnr_PmFPEkcK9iqilKNgDsZNGvSBT75MGPvrmbjqbovD7rBOHH8L_jc3DB5HKQ25XSMBT8WojH2aeazv3q_FCBJ3BIhw-eY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=FRJB6a2DWt6nOid-BClhhjow_-KrFCMvrZ8ntDleTUI4kPj5xLmah5CK-XhLIDEEjcJQV0MFH5kOqkRisK2BV0HG3adSVr9MN6qkGIIbTuDO0C9uGBMTUJphzoJec8_wWJ3DbjWmteOhTnv_ltUA7ZIEZENaeWRU3i2PtgLPH1nESxKceg_tl0D-e_XDG1LqJhkbwRDkABJ2YlWhCl0blYcmE_gxnyt_dCsIkULSZF3knbr1ptjS2yS4ftSznN-AgVy72UYNTeANy_WkcrciErfDabJUsEtsz34umBU3w3tcSHxQPP6gk_MUAamA7qBZ3lhDt0DPnFJ1NfjlMjWE3WBUrDGCS3hAXLA0sNFqOqHbgm47Gp9fpmOVHN-9WofqPIMPi3k_HsHmCEX_am_ipYOlW1egvF6kGtUxn107Q3pQV7xhxwde6SIMJMa8pq_ZNTDxltSS3YYIL9_WFcSX4tE7ur6-OXbsY4DpKhoaP5lY9dy_ZXo5DJFLUQDTtWGLOOnahLteGMUKlIC7oFKIsGfUH8Pa6SvDf4VlLUaY4O0ykaoNYz8_vH1IlFN2DIiNtapZli-bqlBGVt2JB6qdanbHV6ytIf277AB0VpcHsLLUJgGd6q2e0H637Vg0XuUo2AXzUgdsm3g6V0aE1sjrXzncNO2ZLHEcPqpX49vL4to" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=FRJB6a2DWt6nOid-BClhhjow_-KrFCMvrZ8ntDleTUI4kPj5xLmah5CK-XhLIDEEjcJQV0MFH5kOqkRisK2BV0HG3adSVr9MN6qkGIIbTuDO0C9uGBMTUJphzoJec8_wWJ3DbjWmteOhTnv_ltUA7ZIEZENaeWRU3i2PtgLPH1nESxKceg_tl0D-e_XDG1LqJhkbwRDkABJ2YlWhCl0blYcmE_gxnyt_dCsIkULSZF3knbr1ptjS2yS4ftSznN-AgVy72UYNTeANy_WkcrciErfDabJUsEtsz34umBU3w3tcSHxQPP6gk_MUAamA7qBZ3lhDt0DPnFJ1NfjlMjWE3WBUrDGCS3hAXLA0sNFqOqHbgm47Gp9fpmOVHN-9WofqPIMPi3k_HsHmCEX_am_ipYOlW1egvF6kGtUxn107Q3pQV7xhxwde6SIMJMa8pq_ZNTDxltSS3YYIL9_WFcSX4tE7ur6-OXbsY4DpKhoaP5lY9dy_ZXo5DJFLUQDTtWGLOOnahLteGMUKlIC7oFKIsGfUH8Pa6SvDf4VlLUaY4O0ykaoNYz8_vH1IlFN2DIiNtapZli-bqlBGVt2JB6qdanbHV6ytIf277AB0VpcHsLLUJgGd6q2e0H637Vg0XuUo2AXzUgdsm3g6V0aE1sjrXzncNO2ZLHEcPqpX49vL4to" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا قبل از جمهوری اسلامی
ایران همین جغرافیا رو داشت، همین تمدن همین مردم و همین نسبت جمعیتی،
اسرائیل باهاش دوست بود و آمریکا پیشرفته ترین  سلاح‌ها و تکنولوژی
رو بهش میداد و اسرائیل برای کشاورزی
و آبیاری به ایران کمک می‌کرد.
شما اومدید شعار محو دادید و پول و سلاح ریختید توی لبنان و فلسطین و…….
🔺
همون روز ۲۲ بهمن به دفتر اسرائیل در تهران حمله کردید !
🔺
اردیبهشت ۵۸ رابطه با مصر رو به خاطر فلسطین قطع کردید!
🔺
دو ماه بعدش روز قدس رو راه انداختید!
اینها کم آوردن ، میخوان مردم رو فریب بدن و بگن «مسئله ایرانه و تاریخ و تمدنشه»!
نه خیر! مشکل جمهوری اسلامیه</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=dfaAKyRCDXSJtwQ2Kp52tYSddR5rfJwsp1vtElLD50iMuuTJHcgi3NmSjdk934oFPpGpNOgF8qO_F6ueFJydedzHuoV4wGOcU70-jzt1wHpNkKzJHa1xwctgxRHgyxjvfOI7m4amCW-X2zvd33lr97jN1WfiiRFJG1OwO3WEPaCusBlLrXl6cTHewG_Q3u7KYUihDB9q6VHpGmnLSdqyxaM0dERSom19dUYN6QyBpXDa53zXYbIen8-IaoirW65W86yUhkxyzYl_RDYV19dJ7s-WaMeEFL49spKu2DpJh4f7nMbhT8VLDFISKTMlDMIGBHYAQXxb74TifeYkg6ADWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=dfaAKyRCDXSJtwQ2Kp52tYSddR5rfJwsp1vtElLD50iMuuTJHcgi3NmSjdk934oFPpGpNOgF8qO_F6ueFJydedzHuoV4wGOcU70-jzt1wHpNkKzJHa1xwctgxRHgyxjvfOI7m4amCW-X2zvd33lr97jN1WfiiRFJG1OwO3WEPaCusBlLrXl6cTHewG_Q3u7KYUihDB9q6VHpGmnLSdqyxaM0dERSom19dUYN6QyBpXDa53zXYbIen8-IaoirW65W86yUhkxyzYl_RDYV19dJ7s-WaMeEFL49spKu2DpJh4f7nMbhT8VLDFISKTMlDMIGBHYAQXxb74TifeYkg6ADWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbBppC3kE4yiqvn1rPHo5LlwHBLSmaHvizSpBZGLNUz4gRKpxGzCOHkieTXV_mtXVmjA8iUFweBq2r_sO6aWBrzIUP04nKaaLvtIlzuYj_T33P6VB477eSUrzcfNbex07FxYKIvTm923ZWUCjQ_93cESQVKHSjPIcG6ZLG-uy4SVEsWn3jzpKo3FLv5GoPxQIZGWWxZHS6HAf_q0wNHP5j4C6Zk_B-wARPr6-kGZkylyPopWt8eL_7fO_hX5d873A1jCUqrPWjsA-ZQqOHlAJq5d_A6PJ4mb-Sd6oeHtXvna7lWiOQq52OF4-22STGgayexXHILpktMYVIw1eh-bVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=G_Ar6iRCUc11R-46msXg1j-h30ffm98JIWUM_SzpGtvGP2VSkiH6v26FzQLGoQY19KhOYidUnba8ufzYCyub_qzKLU_VhhDWvLbzOtRSLaYy-oWiReFzdJnQQMIb0TWkK1-PQgH6MOujJtIB58jmQNUtAp6ptaHJ_0XIkwPaWjEzzOjbWWYy2t1mBkNtFBCflgIu8CmJa2q2UlzV7VapKHbxNU-dQOz5_gMR6WptDNsw5asRpCNsXTlh-OcMLpCvpFWhP1fWA1_HzotEvuN9vfYrg5NHY4i9IEj_A8PMgUMv3MgM4UbrK6UmYpiFSOPwwWC6ekRm8mAZcKArcqP6YLd4RXvOh05J8a6kZIWNJJsVMeLY07jgEWShJl21f7IZLKp3D-6D0vJk-MW5LK87cryhTE8YTqL8przbAL2ZzG1sFF_HQuP-ABDoMvbXgS0d8_dGZphfJdUVjYmS1UjCrPgUELzEPEfzUPupwyzMRaA_LzFCtb5KJV1w3PPSwmqAW8pMuYrig_MN8XItauN08_2sCoQ03OKrQnv2aUstJkNH87yYWd6uezQRyi4jqjmmpzvRbklmTyNBVe_RgDiOJ__flx_kb1NAh45LnFFfvgx63ieag599La85voJ5hef5Ogw60Jyx3rdAf3YVfXqULA9NN3Z__PFGyg5QlxNbMQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=G_Ar6iRCUc11R-46msXg1j-h30ffm98JIWUM_SzpGtvGP2VSkiH6v26FzQLGoQY19KhOYidUnba8ufzYCyub_qzKLU_VhhDWvLbzOtRSLaYy-oWiReFzdJnQQMIb0TWkK1-PQgH6MOujJtIB58jmQNUtAp6ptaHJ_0XIkwPaWjEzzOjbWWYy2t1mBkNtFBCflgIu8CmJa2q2UlzV7VapKHbxNU-dQOz5_gMR6WptDNsw5asRpCNsXTlh-OcMLpCvpFWhP1fWA1_HzotEvuN9vfYrg5NHY4i9IEj_A8PMgUMv3MgM4UbrK6UmYpiFSOPwwWC6ekRm8mAZcKArcqP6YLd4RXvOh05J8a6kZIWNJJsVMeLY07jgEWShJl21f7IZLKp3D-6D0vJk-MW5LK87cryhTE8YTqL8przbAL2ZzG1sFF_HQuP-ABDoMvbXgS0d8_dGZphfJdUVjYmS1UjCrPgUELzEPEfzUPupwyzMRaA_LzFCtb5KJV1w3PPSwmqAW8pMuYrig_MN8XItauN08_2sCoQ03OKrQnv2aUstJkNH87yYWd6uezQRyi4jqjmmpzvRbklmTyNBVe_RgDiOJ__flx_kb1NAh45LnFFfvgx63ieag599La85voJ5hef5Ogw60Jyx3rdAf3YVfXqULA9NN3Z__PFGyg5QlxNbMQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=BYNnG-pdOr6bHjKx0USJi0hTO3AIs5zo4_QOAjigxDJ7gG6C0jzVbhUY_SbasafwINjNw4fqVnxaYM9PmK5FpxA-ZDg4OjR0MWuIh6dCvTpnU33XgxvNRTcGMoZawBf9YBuCvIPLmn15ORWcu1943N550l0hH828CV7hw5QzulNcmVUPbHxexXf7Wn3v2kvBNdvqwEMM155nQpu3x35OPIcgvJMC6nYlIAIRP0KSdcINoIydKeslQjx5uOxacmYrKKAYYK-2DA--qeIWG4SrdsAOx8potK-7uWFknXzXDcu8n9dipPtGU7DV_ZpwnduuBGsi-ulCNDaM1VLMz0NjZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=BYNnG-pdOr6bHjKx0USJi0hTO3AIs5zo4_QOAjigxDJ7gG6C0jzVbhUY_SbasafwINjNw4fqVnxaYM9PmK5FpxA-ZDg4OjR0MWuIh6dCvTpnU33XgxvNRTcGMoZawBf9YBuCvIPLmn15ORWcu1943N550l0hH828CV7hw5QzulNcmVUPbHxexXf7Wn3v2kvBNdvqwEMM155nQpu3x35OPIcgvJMC6nYlIAIRP0KSdcINoIydKeslQjx5uOxacmYrKKAYYK-2DA--qeIWG4SrdsAOx8potK-7uWFknXzXDcu8n9dipPtGU7DV_ZpwnduuBGsi-ulCNDaM1VLMz0NjZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvDYAVxq_VcbEn0jaAtD5W0oDdCv3M8dmdxBphtzQ5ZwVVirnEuae7sQDY784gBK6BpZHGygBOPw0ePCzEjP8oa-y21b_C8vFWf_neLyAqf_Wbd7azZZUTfH89ug8shTlr8FOJfiyueNVS0BNi_E9sxOtFj-Zr9WdrRH6t2Mx6NALQBEyBifA83N9-w67rDqsQ-p0ZkWtPrVIBSdzYdbAZQSA8jNCx7-m0U0c5ubeMLRs6Ek-tOMEEqhg4k1z2U1vhP8aJsrJfW_zhBQbml2fRWDupFkGydVYyYxuDsrZrSNuy8hEr_6_uBv2KdiOOzC0chxlBOYOHNbuxHcbjYmzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o23JcAiz3J-Icg3U2M2NzvMMdb40oPmFoaBYdlEUwYBjyhuN5b7h2IyB8XgQrGu_Dq7InpDe7TcU2ZambOI_wXSGPPLisXRqSm0xPvHzpWORotmFzWGypHPDRcs28w5fgyeAPgPX9tmcEit4U8j9ZNBkqD25XpgTKaBzyczAQNroCMUmhkA_u6H04mdQtYeTzyX2ghvNenOWyuC42uvE645ZfSEQuwM6bftXXPSROfKTqucxUJy8Aa9k8LJWwmH-QDEjrouQMl89LJ258sbqW6S1tVKp-PMIp46gh9b6vqZvF-z-Z8kH5YlZDHes4FG4ujPhCMiuflxA-C9mAuAtDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj5r17LvhYKZPKH_z4Yr62thpiFHiUk8LiH26S0LqfbzRr4anLt-I4ZlHGmLLLokjaV7l3yCbMbH_sSwpzpoZRl_bN13-AuNvNRSDhRXn_0pWfAMFXI4j00iMQrdXOrrZlNW__UkxJ6YAYYDdIKuzjK2jXSON60UJVXKLGpSiLQs7ewG1M34omN483pt1bgKdxYdtLJ4MBnsrZGMgPCBlKZyeS0uSstBfzav_2qmMuBExOvZT22uS2fGMWylDiqDPF-rg6O1gBmACv9_Vtg-0tRr1_lFJMPu0svI6UoBFTlaJtH_Ay8aPYXXW4r5GwjOUXuhxMzY67FHpPB16lEb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JiqJqye3zdqbbRe61tMDRcNRd1HRUc8lwStEdbQx3VVCEWyoVq17TPi-MSLx_37Wk7962pQr0S4OxJ2-XvASxtp7NIqc-E7JezT6ns4DQnxD5uhBsTg0bVd7RW3am31cclvv04Dt2y4WnbYhwSsDG-AX6qNaIcFxcydkS7L40vrePM66G5ChtNGeybD5D7xlld9u0XZP7w3ZHcv6SEa7zjHlu2EWCtEA6mxikm7Ux77QHLAfxeZN4bmdoalyYF1j902Dt_OaFkQay4ODUaKCofw0gLn0U2ls930_94RLVk95vfPBB50OdPHPiRglhSM_HTEwMZ3i0PQTxJjXc_4dd-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JiqJqye3zdqbbRe61tMDRcNRd1HRUc8lwStEdbQx3VVCEWyoVq17TPi-MSLx_37Wk7962pQr0S4OxJ2-XvASxtp7NIqc-E7JezT6ns4DQnxD5uhBsTg0bVd7RW3am31cclvv04Dt2y4WnbYhwSsDG-AX6qNaIcFxcydkS7L40vrePM66G5ChtNGeybD5D7xlld9u0XZP7w3ZHcv6SEa7zjHlu2EWCtEA6mxikm7Ux77QHLAfxeZN4bmdoalyYF1j902Dt_OaFkQay4ODUaKCofw0gLn0U2ls930_94RLVk95vfPBB50OdPHPiRglhSM_HTEwMZ3i0PQTxJjXc_4dd-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijt5NRK3bltsYCoHkEWDkhrcfi5qZ--8GXUF5P3-8IK0TPqriYcGaj_rju2tJ7vUgwYsS5u9HmUMtsvwofBpwQIY_G8VauO1lhDEPE79BAXOnZcWgApkjZp8GP76Nxi2zQQ9wVFiPyWCkbhC-9yvd0w_1ZnHvvy65JIPelk236nzSTkWZJOOo82ttchl91wf8Wqd9mCD7pIa5mPzdbLXD1iNMUNym65cPe24AyUPfo20PC1xb_MnWNYdf5MmiJ0HfjfWiWjCciXf3-nfQwoVq71WQBin3R_7y7TWbh_DZcycgfxnLxzhmpI6d4g18W17wla0suaespRUpAdDgjiyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=JYCCchxyPd6A7ilQkz80EaXyVs2eEsT0foYs0LNA-hNCrlVX8uDIyd-GqnSj5S2pA-NoJCWDs722GN6rh_Ulp8FaQ0otBJuAQbmpJQ708RODUIsw74MXBXvtq7PL43Lw1-UcXriz7sjhxUJ_-S4b-ut0y0jgQ6bDNuTeQqHPL1cMhNAvReGvM30SDFNiUAhxndwwJO1AJzo07_DC2-7eu59ijUkCzJoG_7SBCDpUqnnqNyZzxS9d3tfNka8FoWGidqeZPqX2Fe-VYDqyVPpf4atEFBFm_dWFHWLR04c2eYcB5XOY4r0ClYFla4O8NDsMZLeR8uv-naHUfuY0s1njVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=dWf6EZTzIZf3kpUPVPuf_cAJQ7CVsy6iOkabI1WMmPrMCmbCdf3PBOIlPELF9sFx9gbVeQWwfNcuLeUa4QU_BBCUd3gKmjlXvyZUZ08cBKj3nLAez_ENdXELSOpAIVZNTLgqL16rT199nbBMNVKcJtyIotZqRlVoIcu0OJ2cyfO-uznwRfHpz7MgJ0Ev7WFyG5nN24g6UmpbBqC-UR53wUpaTiq6S-XtObe077k_wLYzVjMumFAoJYCYg8FtdIrvQhkOV08qxdLb2Cq1z9Yq7_76v-YqTZSTTzJ8rXLZpwhRM6DHhgnsdNY7VKNLW7A-zQz65nNpv_7d9A2R3dhG9r3d8jVanJfe4kBsbvUeUUR7S09TeXOpP19Qu6UGBuaR30Q-QlCY9gEkKekSkEPOr2HoD88xfGyvODaPdd1H3ST_xupUfTkWFVxEadR6oOCxUqDjRLuBWsWsL3BaJu485qR-vQSJ96eaZRLdYqQ3y6phGUXEiLeVznHmfk8YdUlva7JDYRhAT8trRdobzd1OmEmQNlPP5HA1bTaz1-lNy6vBCFiuoLOOm93exEiOngC1zSziUSD6IXr0gqueGss_N3oTBj9jJliavg04_hkOhQ670MislNdEwnWkCsRPdvpyK2nPZfHcWtg7S039SnHp7EUjodPYTS1LKZRiu5vjTFM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=dWf6EZTzIZf3kpUPVPuf_cAJQ7CVsy6iOkabI1WMmPrMCmbCdf3PBOIlPELF9sFx9gbVeQWwfNcuLeUa4QU_BBCUd3gKmjlXvyZUZ08cBKj3nLAez_ENdXELSOpAIVZNTLgqL16rT199nbBMNVKcJtyIotZqRlVoIcu0OJ2cyfO-uznwRfHpz7MgJ0Ev7WFyG5nN24g6UmpbBqC-UR53wUpaTiq6S-XtObe077k_wLYzVjMumFAoJYCYg8FtdIrvQhkOV08qxdLb2Cq1z9Yq7_76v-YqTZSTTzJ8rXLZpwhRM6DHhgnsdNY7VKNLW7A-zQz65nNpv_7d9A2R3dhG9r3d8jVanJfe4kBsbvUeUUR7S09TeXOpP19Qu6UGBuaR30Q-QlCY9gEkKekSkEPOr2HoD88xfGyvODaPdd1H3ST_xupUfTkWFVxEadR6oOCxUqDjRLuBWsWsL3BaJu485qR-vQSJ96eaZRLdYqQ3y6phGUXEiLeVznHmfk8YdUlva7JDYRhAT8trRdobzd1OmEmQNlPP5HA1bTaz1-lNy6vBCFiuoLOOm93exEiOngC1zSziUSD6IXr0gqueGss_N3oTBj9jJliavg04_hkOhQ670MislNdEwnWkCsRPdvpyK2nPZfHcWtg7S039SnHp7EUjodPYTS1LKZRiu5vjTFM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!
ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟
به خاطرش حتی موشک به اسرائیل نزدید؟
(که اونهم اومد در پاسخ ماهشهر رو زد؟)
خب جنگیدید و شکست خوردید!!!
هم در لبنان،
هم ‌در سوریه هم در غزه به مردم گوش ندادید
جنگیدید و شکست خوردید!
۲- اتفاقا چون رفتید توی لبنان و غزه و…… دنبال کشیدن «دیوارهای آتشین» علیه اسرائیل و نابودی اسرائیل بودید، و افتخار میکردید که  بهشون
موشک میدید، از طرف دیگه دنبال اتم
و هسته‌ای بودید، اومدن و ایران رو زدن!
هم اونجا شکست خوردید و شهرهاشون نابود شدند
هم ایران داره نابود میشه!
نتیجه ۴۷ سال اسرائیل و آمریکا ستیزی شما!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=BMKZk7d4TR23meNbWRX1PGkNu2Mn9teJhV2hIIhgRKy1SYX3rYHnGJAe8gGLd8D-PtWThWt7VYClK57lxResftgq0XPtbYAL56vh_8i4GGHrZ7vk8jjA2rUykCAgxcHGOepVtRIBP1_AiCyL2QWAh5RUq-gz76N9Ndey5V3ubO5EskhcL07BziIP2yR5LeDRGNyBaCzLtY-WCf5mKaFPfxjjjm6MuKqHWf2uTCUwTD16N2PKWvztZIOSq7HKJWcB3ap0DVc5AfCgq7ymGNbcbJLKYgFlYuTVmrLWccrNTcyYjrVRnu5bzy8Q9reFPl7XebH7z-qOncChdI-sImZ6Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=BMKZk7d4TR23meNbWRX1PGkNu2Mn9teJhV2hIIhgRKy1SYX3rYHnGJAe8gGLd8D-PtWThWt7VYClK57lxResftgq0XPtbYAL56vh_8i4GGHrZ7vk8jjA2rUykCAgxcHGOepVtRIBP1_AiCyL2QWAh5RUq-gz76N9Ndey5V3ubO5EskhcL07BziIP2yR5LeDRGNyBaCzLtY-WCf5mKaFPfxjjjm6MuKqHWf2uTCUwTD16N2PKWvztZIOSq7HKJWcB3ap0DVc5AfCgq7ymGNbcbJLKYgFlYuTVmrLWccrNTcyYjrVRnu5bzy8Q9reFPl7XebH7z-qOncChdI-sImZ6Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdWJgw0PLVMOxf50UHNevQWUOdCA1CdoPX_0z9iz-k6WtSxMwBr-aofRD7f9ll804XH6DaZJ1ELPMlMpuhOQnPKs8JyErM6SWhuaCnSujCteOBMVuvkNkNqsxjOXPXySGGOdgs5Wed63LZG86_J18AVtM37nK8R9JL2eln5jndKb_Z2F0Mk6GRCcGBIBmjQI3MHl6PmdvkwKaEc1wqoPtN2NrIi7CnCROH_ihPKlNdTdlLFiPa-EfnTyD2FmHRdh3vsEarEd2154QrYQ6vziE-pVQ7MiObpIamq4JpHZvvkfnLFujZqg-RUS6KcumrSZuy2CxkqlN2y7LDvTImj9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=K6kHelteDclK8BnEQlM_1IPcZ58kRldQI2bYNTnLSdsoHa5BfIRYhD0ANQFt5zIO5UgewOKS9c_-nIOQFco46fgGHsPvs_g3wQQYQFCV0e-25m99-bg0dDryufhSw4ikN2kon8cDaO7xfPa-Cumr830ZY1j3yii8yzK5AJPTQgoEEvQINVj4kDxQo8yi2OzI17QVORvIkLNnwX5OkEDJOimXhSFeY1dZ3VjlKLwNKiAsqXeZHvi6Os2wUAWujsgf8AyYdhuLJ3RXlUxy4VM3Xk_L1R97stMbdEhfshlf41l3UnZHLyqR6p5qnsxCiZKIkWMknYPU71kbqBthtdRO5yWFL2HABCnhOzTIZQGhS6G8jiJUDqu5DoWpMHNRuY8zJ1FpTsZ_l6cmPKG0zicWC70IOJCTO5DEdpQZbzjtC__5z5QvGUmIG8HDAuF4oDuv5cW_CChZv6XxCb94ewoRaHFFKDWv3r-mrDnle_JjHj23NxTMDpLRU9RRkVTxKBuLWsO61KJ4TBH7-5dtf7pNDQVH0nUf6LAdsdK_nvYU8V2j69mJLcPfuT-fXM6RQSn8pB8wNQShJvC4sfz9bsAmTh-jRnB5DuQmheH_QRaKiswX6ajMEPkEhlgSDVOWo4BrAlju_KxlPribOLeLkYl3k_HVsHP2-3E0mVHHzKRu83A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=K6kHelteDclK8BnEQlM_1IPcZ58kRldQI2bYNTnLSdsoHa5BfIRYhD0ANQFt5zIO5UgewOKS9c_-nIOQFco46fgGHsPvs_g3wQQYQFCV0e-25m99-bg0dDryufhSw4ikN2kon8cDaO7xfPa-Cumr830ZY1j3yii8yzK5AJPTQgoEEvQINVj4kDxQo8yi2OzI17QVORvIkLNnwX5OkEDJOimXhSFeY1dZ3VjlKLwNKiAsqXeZHvi6Os2wUAWujsgf8AyYdhuLJ3RXlUxy4VM3Xk_L1R97stMbdEhfshlf41l3UnZHLyqR6p5qnsxCiZKIkWMknYPU71kbqBthtdRO5yWFL2HABCnhOzTIZQGhS6G8jiJUDqu5DoWpMHNRuY8zJ1FpTsZ_l6cmPKG0zicWC70IOJCTO5DEdpQZbzjtC__5z5QvGUmIG8HDAuF4oDuv5cW_CChZv6XxCb94ewoRaHFFKDWv3r-mrDnle_JjHj23NxTMDpLRU9RRkVTxKBuLWsO61KJ4TBH7-5dtf7pNDQVH0nUf6LAdsdK_nvYU8V2j69mJLcPfuT-fXM6RQSn8pB8wNQShJvC4sfz9bsAmTh-jRnB5DuQmheH_QRaKiswX6ajMEPkEhlgSDVOWo4BrAlju_KxlPribOLeLkYl3k_HVsHP2-3E0mVHHzKRu83A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=o_Q082q6AbDG5JzD9YXqIwVEBF3CnBu9x9pQ7TY1VkxZlgH1DzashjMokZCO8a9A32amclsoHTU8_d6SSGnURlwHzCuGRyWAgthZnQCNWL0H-Le_-Rh94cb5LuLL7_V8_U-TpZaCjh-GiLEJ8VyVEjJ_Lyqc5eD8rOt8bJwcivns-6ZqA0ePBi5oXw1--h8CzdRV52bjbTHL7NCFVHIDk96Lr75tIZZJwXQxOjjBKJnDDu0Ut8Cy8G-L0ACv6_79kNpjDW572Ju6tIfop8iV94T4YmAk583z8yVrbn1JogfJX3mBWz8sLlU_CaF7bmXW6xKCBOk_v6gGkiRi1CZBHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=o_Q082q6AbDG5JzD9YXqIwVEBF3CnBu9x9pQ7TY1VkxZlgH1DzashjMokZCO8a9A32amclsoHTU8_d6SSGnURlwHzCuGRyWAgthZnQCNWL0H-Le_-Rh94cb5LuLL7_V8_U-TpZaCjh-GiLEJ8VyVEjJ_Lyqc5eD8rOt8bJwcivns-6ZqA0ePBi5oXw1--h8CzdRV52bjbTHL7NCFVHIDk96Lr75tIZZJwXQxOjjBKJnDDu0Ut8Cy8G-L0ACv6_79kNpjDW572Ju6tIfop8iV94T4YmAk583z8yVrbn1JogfJX3mBWz8sLlU_CaF7bmXW6xKCBOk_v6gGkiRi1CZBHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=Afv26odM7cLxGkFwFP2eXTMNbbXXXwkW7pfXSe2sUNJ2sSLE8VNlytz3sE7SzwVXmlbFwkLfFvcadCivvxBJqjpz2PIGAvLrBhYGjjD_kjx9CfdUBdvHTxNdiGBILgDfo8MPqZL8aI_0K8z-rXsKIaFvHENDyyErl2ttTMGH-24TqVOZoO7F5pF6z62p2b5XqNzLjGaTvROIGtN4-oxLFFQFV1Vm292FFEY5eGcGf3ceZUaSjH5QDDAtB0nTkdScDVh9vrmTAx09oI9MyaemqJToMJVEJCm8_bkom3Lb2ulmMHIJYCBCDn9OjTYV88patIy8OjIP2Weuzm2GfjsIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=Afv26odM7cLxGkFwFP2eXTMNbbXXXwkW7pfXSe2sUNJ2sSLE8VNlytz3sE7SzwVXmlbFwkLfFvcadCivvxBJqjpz2PIGAvLrBhYGjjD_kjx9CfdUBdvHTxNdiGBILgDfo8MPqZL8aI_0K8z-rXsKIaFvHENDyyErl2ttTMGH-24TqVOZoO7F5pF6z62p2b5XqNzLjGaTvROIGtN4-oxLFFQFV1Vm292FFEY5eGcGf3ceZUaSjH5QDDAtB0nTkdScDVh9vrmTAx09oI9MyaemqJToMJVEJCm8_bkom3Lb2ulmMHIJYCBCDn9OjTYV88patIy8OjIP2Weuzm2GfjsIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNbKOspmmndox0vbKjIKvOC1XZ5ShEMQB3kN4IIU0RcheAxVHxGDQgsdDtZpY8CaPHzY7AgWXuMefW2UhUU_m5zHnQwPcA5wML5gYhUaJT6wQP1Lm83y0OeIw1c6CQ8ia1xTsc-1KqYdmKTsxL4pq24LWPZ5K96_fs9CU5lnKXIXfvhOZXLBxocQKUVTyQi8DvzvH4OYDIHi_BrwhsnN0l_lW8pFFd5qrlYzjCl2j-f9YOkj00P-B8ZY-KhujlSXmmpMXF8JK1o-30iQww1M9NVGzjtctJhS_lkSMMEe36mZ9mrOtw6Dt7bJq6tf6wPkT1Dd6_nIbs-dX7q-FpU1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=XpBiLnfUjpyUonQrj87tJR6me_hKmc4t1Rn9laehi5Iw2XKuqLGdtoxDXSSbgcLCihO2DvAlpNcUUsNALmmoXoMhVOn2ttByyCNPhUUdrya0rCc_tUOjWdYLofIlUebC8AcORRcCZirUKnnp_tuA_4ZxR4xBHlg0Eyg_rMdnCFO8m8pB6kQnaJsJ4wPVA_EDWnvgX_sOXNX1FHN2Qi2YKvQT5kepAPIfnUVTIbzJvSZ8a3sXRAB49WxnPgD_U9eFw7TUaCPpNLE7VkCiHOnVQ0PhvwpeFrG2w9RQkjKKZKDQ4He2pm-4dsWiaJvd8eFuhYXTV2BrOqZ1aFeUWk90Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=XpBiLnfUjpyUonQrj87tJR6me_hKmc4t1Rn9laehi5Iw2XKuqLGdtoxDXSSbgcLCihO2DvAlpNcUUsNALmmoXoMhVOn2ttByyCNPhUUdrya0rCc_tUOjWdYLofIlUebC8AcORRcCZirUKnnp_tuA_4ZxR4xBHlg0Eyg_rMdnCFO8m8pB6kQnaJsJ4wPVA_EDWnvgX_sOXNX1FHN2Qi2YKvQT5kepAPIfnUVTIbzJvSZ8a3sXRAB49WxnPgD_U9eFw7TUaCPpNLE7VkCiHOnVQ0PhvwpeFrG2w9RQkjKKZKDQ4He2pm-4dsWiaJvd8eFuhYXTV2BrOqZ1aFeUWk90Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnrm30qJQkqF5qApZqNl9CvmFw6K4JQ8XNs_z-bM1_fVJIMVFvEmHU0mx5SYUyFvfOZpHGknRL0P5IWPaI1sbP3Xho6XqYTHgi11vVqJfZ38Q4JoFL2tq7m2AI-CAucaOPr5Li9toCgi0m7xkXexCpPCwwooDqUbSk6xKNX48EhbK5q-vDvoqs5yIdYPbOUeioDfjVhwNAZYeTldcu1Zz7eKYhUtdt46Ucx0_9vcRNnZ8wrWOuLE8RnQOUkYcu2h6jHgH7f1vT3cxDdMck3k8zntTdpStJr4o0XogD-ibZOJIDQdLazntsAXJl1mIU6NmA2v8TUvdF6jhWFJFDeSLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=sqNtSr3PmY7yJoVOHhaYlXRzRRN7bm4JiwtwdD4k0nMoe39ZyWD5VF_RMELJWy5h7f6iRRhwjvmBDdAPlL-V_csj-Bi-FEJPn7Cfham3JKUg2G6hH8uHrkpBFUCIOiRgYRLU-ld-0qxjmbt5Fq7fwNSccF155syWBcRsnWivoV1RgxRfEkR48MQMiI03n9xMvQO7HPUHAUwt-BPR5oeD6qkT9Ivxe7ba5s4b0zvctzdFpwNgZYsQ0aplVxtAka8QKssatOGsCoe-lu_-AlICaatCocizWBYaNDYhgNi-IsKwETIx37YLVo9iXU7TqyZITgqr53E4wd5LIvnEYJ6hBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=sqNtSr3PmY7yJoVOHhaYlXRzRRN7bm4JiwtwdD4k0nMoe39ZyWD5VF_RMELJWy5h7f6iRRhwjvmBDdAPlL-V_csj-Bi-FEJPn7Cfham3JKUg2G6hH8uHrkpBFUCIOiRgYRLU-ld-0qxjmbt5Fq7fwNSccF155syWBcRsnWivoV1RgxRfEkR48MQMiI03n9xMvQO7HPUHAUwt-BPR5oeD6qkT9Ivxe7ba5s4b0zvctzdFpwNgZYsQ0aplVxtAka8QKssatOGsCoe-lu_-AlICaatCocizWBYaNDYhgNi-IsKwETIx37YLVo9iXU7TqyZITgqr53E4wd5LIvnEYJ6hBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnqzGf11pGJOqmXQtwWc6PSkNb2mAuBAiCg3OPT34Ce42CplUs4Xb1lId52ruzWJfeLWMWbzW3QkiwLLFUd56h7c61NurtHNc6ZDlS6LgMOpPOrb_izFi45R8aw09HPJKwcCSXt874GR8zuOGpNEnNhkG--yAGmTwzYUvnv7cjlRp5STXr-z7rs5bFcxcsJo2j3ONhOfGa04QSEx5yOGln6OuLoMdQAiG0d7-5w1CMqE2-6ZhPB_UxDr9bAgFhdH7PUwFslInRRrwNzRc97DAvZ7qcd37Y-oLW6IP_1-QA3ynC1tYqdFZIqxPMvADnBr9rqUK9lxHLhMsQ2I6X1PTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اهواز تحت حمله شدید
حداقل پنج انفجار مهیب در اهواز
🔺
انفجارهای مجدد در بندرعباس  و قشم
🔺
انفجار در بهبهان
🔺
انفجار در بوشهر</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=mhjMzcT4Q7SLJpy1LgOSvWs4ZBbMff3FrWWBhwidnel5uRK1TzxX0Pa0mig6gU-rWhEnRQqC1oDzz2X-HphbLycAm2qhBrFDQekGWWjz2HLFBDJzSSyU4Sfpxj1wMC3as6f9hdvZZvMTC4vpOUQ5TFRoHPX2a64HF6Acq8D861YgSmcXdnifMquhYV6PGdZVy1E3Px_1K6CSQguugV02BTqP_hJ-OAXlcYhA0XcXRO_kTjPaV_Oq5f-a1Pi9HimStEfP-yCeyG6rhJMCwaSen_Fh6TN9VhH6sTeqeGT9IxBgGn4t_XSIF0-w7GUW7BUfEmGDpAUVwws5N9kdqLguSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=mhjMzcT4Q7SLJpy1LgOSvWs4ZBbMff3FrWWBhwidnel5uRK1TzxX0Pa0mig6gU-rWhEnRQqC1oDzz2X-HphbLycAm2qhBrFDQekGWWjz2HLFBDJzSSyU4Sfpxj1wMC3as6f9hdvZZvMTC4vpOUQ5TFRoHPX2a64HF6Acq8D861YgSmcXdnifMquhYV6PGdZVy1E3Px_1K6CSQguugV02BTqP_hJ-OAXlcYhA0XcXRO_kTjPaV_Oq5f-a1Pi9HimStEfP-yCeyG6rhJMCwaSen_Fh6TN9VhH6sTeqeGT9IxBgGn4t_XSIF0-w7GUW7BUfEmGDpAUVwws5N9kdqLguSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=vhHMd2ZtnRZd17-tgJbWp7eAxsPA5sCtsIXTLZlNSOHNVEHCjTLOWxhbSVfyK24Gu2XrVzcqth0rPNc9zCvbWYiEcpAv1Rtvb3QHxC2gdxbeH6Q0K0AyvlcYhYOIFM7adN9Po6RtfcrmC5B5Uwbqh8FV6wUVg_aoc1GgOnzHgPqFcXLgr7-H_AH6Cb08NjKTW7FSoyaYocb407UVetbxqwaob9mXhw9X5USvwIKllNEH83GW7hhZ6GymUSonSZ7YJXXnMptCFk9oDhElT7EB442rjlRy_s4QyhwbmVqMNJGEhDCQe6-V0zZK6gAZfD0U_NUSBwJUm7MNevWcUl4oew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=vhHMd2ZtnRZd17-tgJbWp7eAxsPA5sCtsIXTLZlNSOHNVEHCjTLOWxhbSVfyK24Gu2XrVzcqth0rPNc9zCvbWYiEcpAv1Rtvb3QHxC2gdxbeH6Q0K0AyvlcYhYOIFM7adN9Po6RtfcrmC5B5Uwbqh8FV6wUVg_aoc1GgOnzHgPqFcXLgr7-H_AH6Cb08NjKTW7FSoyaYocb407UVetbxqwaob9mXhw9X5USvwIKllNEH83GW7hhZ6GymUSonSZ7YJXXnMptCFk9oDhElT7EB442rjlRy_s4QyhwbmVqMNJGEhDCQe6-V0zZK6gAZfD0U_NUSBwJUm7MNevWcUl4oew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDyfd2wGA7AqBk7Nu5ggVRSdpafDEKtxNF8Wnu83RgoUVtJu_PZoaqJhhqd9pJgMPLVH6azDB7DsOmzqtpnNbGWIms_Blv8JpX5WrHwDU40l799cfAEj14Xy_cH77oxnGZCGtXzHZCtSUK-ChXvQQgmnZEYva35cw9YlsWoHSyNFtkAKSEtOPjzBAdC5N3lkbfsDM0oUb4WjmF-XraggF2lIvoZXkOdZdvhQB6RBwK9etqXSFQk_YDPgdfg9aiaBu2TJrEf1GRIgbHkERmgfHmyb2uOCVUDFnOFqCaqUjE4YUIyUnHjomNa5biJXo9YsfWGnXi_dPnLRqZvqi12I7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-14nmkxUSimJBA3ZhFbTL95xqqAi0ohZK6qzJWr2ZPAvlBLqI7uOu9N8sgP-gK8fTPDRZMtt8n1rQ-wXSHiu-_Cl7oYKuPnIP3THZ7ydTavD0sbc3gymxiDYXwUY2HL-OUV3nTZWJerdhdmyZvRwuFeLGTbiuMF8NTxqVUJz4jfHVxT1ViiV2rZAyveMOBIPSea6PO_Wr6uiH8Tz72iJrlg2XqLf-qU6DimtC7cXYSryzlSqiqar8l3E1oI4vjAiZNzcwbzqMCbvk8m_h1Hk64kEqPUvNQapZswahww0aKYTjp_sKQR2wxCpDC1kVpRoz9HtAlMCEvb7-y-SxGfeANY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-14nmkxUSimJBA3ZhFbTL95xqqAi0ohZK6qzJWr2ZPAvlBLqI7uOu9N8sgP-gK8fTPDRZMtt8n1rQ-wXSHiu-_Cl7oYKuPnIP3THZ7ydTavD0sbc3gymxiDYXwUY2HL-OUV3nTZWJerdhdmyZvRwuFeLGTbiuMF8NTxqVUJz4jfHVxT1ViiV2rZAyveMOBIPSea6PO_Wr6uiH8Tz72iJrlg2XqLf-qU6DimtC7cXYSryzlSqiqar8l3E1oI4vjAiZNzcwbzqMCbvk8m_h1Hk64kEqPUvNQapZswahww0aKYTjp_sKQR2wxCpDC1kVpRoz9HtAlMCEvb7-y-SxGfeANY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=WBGpaK1xKVn2n-l6Z2zBdTSsf7gyWSHWqBhhlx2hUacDEOqbMEW_5Hj5N1kHeYxQldKuLmijersBNWU7JtHrV08iNEcxDzJ9UpilISADqCYZRnN7ei2PlpAIE6sZCrW1nOvLwoVFtwobgDsO4qkztCR_bnx-viwIHcaXwZVYgKd18Fja7UnAYXyEPKzyCPf80bzJTu3QEjBW_rCk13d-GVMfJGPfEG_k5-WmhMyRoXxqvckUzZGTjGIfZtDIiEELJ-5piG1JdkL6ru9JA1R4-NwYbb6VIcYJZ8hJPnnGkyPHtkmUBkD3cpXHkBa7GEQEQ9mdOSYeZmpLoNnqhvPRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=WBGpaK1xKVn2n-l6Z2zBdTSsf7gyWSHWqBhhlx2hUacDEOqbMEW_5Hj5N1kHeYxQldKuLmijersBNWU7JtHrV08iNEcxDzJ9UpilISADqCYZRnN7ei2PlpAIE6sZCrW1nOvLwoVFtwobgDsO4qkztCR_bnx-viwIHcaXwZVYgKd18Fja7UnAYXyEPKzyCPf80bzJTu3QEjBW_rCk13d-GVMfJGPfEG_k5-WmhMyRoXxqvckUzZGTjGIfZtDIiEELJ-5piG1JdkL6ru9JA1R4-NwYbb6VIcYJZ8hJPnnGkyPHtkmUBkD3cpXHkBa7GEQEQ9mdOSYeZmpLoNnqhvPRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=hUZKpCt4NWScpT6K7QIOxkWGF3GTZrE5fNlEYwTsKmi77D7U3AClxKdB91LZF87bbJ1M3wCWPVvk1CMOphe-FxsJaQ-IIA33MafE0CDSWu_lOHZ5Otv5wD3g25t0u0PbT4Qa8vtieWcBoTFzGtTcLlDGFGCcpY4fWkbWbHqxWQX68617rBIFx_x2mXk6-_TGjbJHbGlifhZsiBNx2SrVDwLPfZYQsCeMZUW54nBCyhFchrbUJ-Y0OmkZrPIooUVvbZBzMh7Gpir-ZwW6qy-D-8kY3Em1Ab_Bq_qDCz5f_ZJEZOhXDHeFhELjzMqT8vpnHqNUCXKVF3aCekC2Akh2xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=hUZKpCt4NWScpT6K7QIOxkWGF3GTZrE5fNlEYwTsKmi77D7U3AClxKdB91LZF87bbJ1M3wCWPVvk1CMOphe-FxsJaQ-IIA33MafE0CDSWu_lOHZ5Otv5wD3g25t0u0PbT4Qa8vtieWcBoTFzGtTcLlDGFGCcpY4fWkbWbHqxWQX68617rBIFx_x2mXk6-_TGjbJHbGlifhZsiBNx2SrVDwLPfZYQsCeMZUW54nBCyhFchrbUJ-Y0OmkZrPIooUVvbZBzMh7Gpir-ZwW6qy-D-8kY3Em1Ab_Bq_qDCz5f_ZJEZOhXDHeFhELjzMqT8vpnHqNUCXKVF3aCekC2Akh2xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8cNq3Y8rhuO2KOKQ7nf7VStRsAENys4W_lnuYaeuDfxpMdUvE4be6q4Ph8ldKk7naZQBCbRsqjhL1Al41xM1iPJ8wg7Q7fjlBUTPdnmCVRT258keEBh_eHSuxz-SBk7Aj35lNLRgH-_1VG32L-F7TYtBH-JovUE5if2yOOHYdvEbXE5989rY1gonRshtWJvXzWkSF8PlAVWnbCOlM1D2GwcUePNShZK9eTbkQg24O9ZjknOHb4obQ_Uk-6DPB9NcwfGB5NfL4zRE6W4yP3t58nNiO-tEpqYJHGLRO3IZn5f3Bfpy72U1TdwmAQOZZUY52XUFLpadI27b3OLBhzgjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=NB4hqsFmkKSTlPQ8m6hG_B8O89st9FRvC5K3h9OT54_rZtCCnienBX1ZXNmbxBpjZQyxlt1_M_bQqorhgvd5vTFLFitQkRBOgfmi8EiqY8-KxCKblkcByzOpcEHU-1V58JkNTOFoe-I-OSrWmZ_FxOkin_pR5l0izz0VHssauJtLtIhpUnFH4ZtapndWBQQFn-0oX4miCV1MTCkjpmOG24I3y7FlkZ3fqAStJHvkPE6iDkpAd11AM0Tu3PiaPQKD9GhMQMlXwlz6n3-GvuaFYSAAEuETR5NZ5uPjvzn69L3Us1EM5zsVWpmSaSS7LXuejWkTZnJA6WffZbMhzWEYzSZWl33j2jiya18HSQ5iephrmxapE7rdtkFxP9OUwtqlCtuKXMt1UEGt55sjJws4qc9MdTC4xt-xlK6iFXD5MsKKkmTXNUssyuGfcEii-0vdc_6trKrUgxhHaDro7lABd8-cPJ268NEqJjGvedrO09QrfIDjaHRaQfzcco8BxS1MVKCOFB-M4OOsdtKdguepvOs3YU5Hnj6-ElJBVcKmufLuYXlwcI0mm6nmm6PZZfzURi5fgc_3o0p-vZF7QlEJ4dSg3NqvhrHQ1ccXKSU-MSWqPbNykgmpLaMfYZnCidx0ehro0aoLffErklQQanpwWgskKeKfpJdO9Py8mGlyxC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=NB4hqsFmkKSTlPQ8m6hG_B8O89st9FRvC5K3h9OT54_rZtCCnienBX1ZXNmbxBpjZQyxlt1_M_bQqorhgvd5vTFLFitQkRBOgfmi8EiqY8-KxCKblkcByzOpcEHU-1V58JkNTOFoe-I-OSrWmZ_FxOkin_pR5l0izz0VHssauJtLtIhpUnFH4ZtapndWBQQFn-0oX4miCV1MTCkjpmOG24I3y7FlkZ3fqAStJHvkPE6iDkpAd11AM0Tu3PiaPQKD9GhMQMlXwlz6n3-GvuaFYSAAEuETR5NZ5uPjvzn69L3Us1EM5zsVWpmSaSS7LXuejWkTZnJA6WffZbMhzWEYzSZWl33j2jiya18HSQ5iephrmxapE7rdtkFxP9OUwtqlCtuKXMt1UEGt55sjJws4qc9MdTC4xt-xlK6iFXD5MsKKkmTXNUssyuGfcEii-0vdc_6trKrUgxhHaDro7lABd8-cPJ268NEqJjGvedrO09QrfIDjaHRaQfzcco8BxS1MVKCOFB-M4OOsdtKdguepvOs3YU5Hnj6-ElJBVcKmufLuYXlwcI0mm6nmm6PZZfzURi5fgc_3o0p-vZF7QlEJ4dSg3NqvhrHQ1ccXKSU-MSWqPbNykgmpLaMfYZnCidx0ehro0aoLffErklQQanpwWgskKeKfpJdO9Py8mGlyxC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwgnFPCYL4jydudpAMSjTr1JkIPSMGM3QRMAKJA80t2guqrETZYOMs9XY6NUrkWBIhWG8XngMNxTaLW19HmJBfqaPT62UBriwBeSkk-vGe0eM8VDoFkJ2xNdglfYodew60z4EyEy-tWAT5gXY6-bSE9CO9KcFNrl3Qszo3GoIAyyD_0slhjjRJnlg9Biafb9RikAvivdQtJjtdxcwHzW18p_H3LQ7X1XYIrK2npivH5znF5kzEZOC8vd9VFlCi10AKZCiU_cjxL6EtAZ5lBQ38nGILwgHdgvoVsxsFOYqJ1ZRP9E4Iz3Bfkz59kNEnAs1N045dSxatTFQw5feozNRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=koq_GSyuS7_aTn-zsvrcFB3hFV77KhwJZk0wpIqdh7GnFOgA2yvDaKu09E24sCG-dCEPtu1xPSWq2RA7Pxyit3mBAK8O5LdLLz26fu3OGdhWBDPrRP1jhxvi7K6GRrS1rFaZwFeCG4QUkHYyDRi1cHt7sTpTychgdq9KYPRXTGsoE6jYU5WuKVsZFH7dhmBopMH0tjFqHGohr8oVza2ZkNao001nWBAF6j0OpjqxDo1ed0JFHz8I1CP4LxsL-iL7XcHg67_drNP9s-kVRF3DyIZqQ2pe32BmMFz3xP_YQ8dIzYer0UBbvCgEGqarSc9QflTiJvzdOHU5YXp0epj5Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=koq_GSyuS7_aTn-zsvrcFB3hFV77KhwJZk0wpIqdh7GnFOgA2yvDaKu09E24sCG-dCEPtu1xPSWq2RA7Pxyit3mBAK8O5LdLLz26fu3OGdhWBDPrRP1jhxvi7K6GRrS1rFaZwFeCG4QUkHYyDRi1cHt7sTpTychgdq9KYPRXTGsoE6jYU5WuKVsZFH7dhmBopMH0tjFqHGohr8oVza2ZkNao001nWBAF6j0OpjqxDo1ed0JFHz8I1CP4LxsL-iL7XcHg67_drNP9s-kVRF3DyIZqQ2pe32BmMFz3xP_YQ8dIzYer0UBbvCgEGqarSc9QflTiJvzdOHU5YXp0epj5Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..
سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند.
و از مرگ متاثر میشن!
تمام هستی اینها :
مبارزه، جنگ، کشتن،  کشته شدن و….. است!
زندگی براشون چیزی نیست جز
«مبارزه  برای عقیده».
و خوشحال میشن اگه زندگی رو به خاطر اون عقیده نابود کنن! زندگی نیمی از مردم جهان هم نابود بشه براشون مهم نیست!
چون «برای یک هدف بزرگ‌تر»! مبارزه میکنن!
پس چرا مثلا روی مدرسه میناب مانور میدن؟
چون میخوان شما رو بیارن توی صف مبارزه خودشون
برای اون هدف بزرگ‌تر !
برای جنگ‌های بی پایان تا رسیدن به هدف بزرگ‌تر!
اینها نمیجنگن تا در این دنیا آرامشی باشه
و صلح بلکه میجنگن برای آخرت!
برای اون دنیای دیگه مبارزه میکنن!
از این زندگی و این جهان متنفرن!
این زندگی رو فقط یک پل می‌بینن! یک فرصت برای مبارزه و کشتن و کشته شدن و….. که بعد توی اون جهان به آرامش برسن! این زندگی فقط عرصه و میدان جنگه براشون!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rv16-t8RBwqyrtJ04xhRM2NruFPa45tZFG99WitZJjRLR-RsVLm2bceWsO1gVfe2-oQgB50SAoa7ydRZC7rU17_oJZ-syaO0Bgg0ej9dT8siDA-mZy6eb3Jm58xX5WekNg9ydzQfW9gOsHtzxQqPtYXolYZLZmO4hOFXjO8Fi7qIf5d5X5hoa5A6ga1mPNH-Oaz0a8LaevhPbzMnGwxO8itjAz79Z0QWHOJn4e_wu1qnI3Gpecu3Befm0IsEyWBIaF7s4mSSxf1thsg-LvdQqtL2cXemwiwxQpKG6WJsWEt0mt4NbbdY1CNApmcjVWW3ZROKw2ZuBA-SkGMC1syNZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
حملات دیشب به استان‌های خوزستان، سمنان، مرکزی و لرستان
🔺
دیشب تعداد زیادی انفجار در اهواز شنیده شد. برخی‌ها تا ۹ انفجار و برخی تعداد انفجارها را بیشتر تخمین زدند.
🔺
گزارش‌ها حکایت از آن دارد که یکی از موشک‌ها در اهواز و در نزدیکی یک بیمارستان (بقایی) اصابت کرده.
🔺
دیشب همچنین به چند نقطه از استان لرستان حمله شد، برخی گزارش‌های تایید نشده از حمله به پایگاه موشکی امام علی در لرستان خبر می‌دهند.
🔺
استاندار سمنان نیز گفته که به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.
🔺
استاندار مرکزی: شب گذشته به دو نقطه در اطراف شهر خنداب حمله شد. این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقاً مشخص می‌کند چه اهدافی را زده و نه ج.ا می‌گوید به کجاها حمله شده.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7X6YQlLU-KBrRuIYyyzJ1jzhmCCiURiWypqCt5w018ONCKymCaGmJrzg3nwibhau3vzz4y9JIE7i_ueDqp2CVBiyXfO9YUkoSmIOw1c3s0ph8Jug1vkaG6nkRE5L6oQtXHzmIGLNa7s4QTfNBT7Dip1cKZAsM8vJx2uat4RGuoKDz6-U3z3u1u6SiquNdzZRdwtwuJbhGkJNkSaRCmxwGFWlJl_mtLAlZjDFwLHC9709S_BOTdzVb07UzX6m0iJvBSCbWwxgRNRy-SXs5HFO5TmAHqWR5tEfGaTd-qLx_JNGw3pOQbh8S78SpyuQ_tcCEIYvOtsO9V9fzBp_FXjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFbBNEqaCukIXyujKzcZ8ZLXM52V04fb_HdN5XuxFJLHE3cnG_u558FdQpd2o1MhKZ8bVufyjf3BBHXRZZH2eDc0S9rIUaVGG2VtiwmgTn6jRSlPO8AmSKW7i-rg6_DTHWzzZRV8zY68Y5ULyFHd3dGVA9mAM5c81-IPM_Du82kaabtKhJHN0wUNdNskqIHo3ojX2QHsSuUXx4w78_MB5HAlRDbZu1JQk4hJlaMw1b2iCTHxu1oOzapppby2kqkmuvtBqAlpYm9DI-HbGwJONBa5NQcpW-hMgbQ0LQYoEn_y467tHwt1GuWfGtWzqs7bhdDLhyGDHCV5z5S69D5O0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=TxV4G9jewZ4X1rPALCdYWqYbxnqCxUbs7735aIRWbvLfbMPTgWHA0IcJ_FkXO1YdX8XByyT7wTa9BtkJ-IORPlx29SQYtFxyHimRiYnYgWAJ-FNZcEm1yYv6w0oiBFhLC8v5d30SrmU7dz92jD-RrngW7T0mRv_mxtsuSP_MnaBQfNRV_xdd7BS5IZHrZyArtcZYYHiRkwHgOcsfCyaVgxF6F06ClkARbDX2cvFahPE54gRwi_nS6tg8gjGYVlfxY_8KJrDBktipvo3Dajd7Uvbw0ZFgWwh4V8GNzZGxXiEqNrBiHSqwtP545WCBXKO6esARMng4fFvWGo68TczJyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=TxV4G9jewZ4X1rPALCdYWqYbxnqCxUbs7735aIRWbvLfbMPTgWHA0IcJ_FkXO1YdX8XByyT7wTa9BtkJ-IORPlx29SQYtFxyHimRiYnYgWAJ-FNZcEm1yYv6w0oiBFhLC8v5d30SrmU7dz92jD-RrngW7T0mRv_mxtsuSP_MnaBQfNRV_xdd7BS5IZHrZyArtcZYYHiRkwHgOcsfCyaVgxF6F06ClkARbDX2cvFahPE54gRwi_nS6tg8gjGYVlfxY_8KJrDBktipvo3Dajd7Uvbw0ZFgWwh4V8GNzZGxXiEqNrBiHSqwtP545WCBXKO6esARMng4fFvWGo68TczJyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=v26D7KNNOtyhpTJYS8qYWgLjI42Og1Slfh8orf3ipKzZSiWgirEHiLC1LHq62UXcuWIWRT1tHx19ZgG3TeTQF3lrLHwLo1Uk6wqzBfQVavIBtlUYVvGmYJfxwCixN0Iiox5g5rwPL7k5-Yftz03WmPOwfRg5TqVrzcUjwkFhCFlV6wnka3nXdzs29p-47ElEdHeKYIRFYa1Nec27mXyJtEdqF7egtG_9XJYhWuip1LrKqdEesll0Xbwfb4Ien9YMY7swUnuTNWnDj4kpQpDgy3XdsLA97Uh6StXR5_3KxpB6DvFHPfyUhvLae88TtLVMhHpAqEpC1iXpCk7IukxzdYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=v26D7KNNOtyhpTJYS8qYWgLjI42Og1Slfh8orf3ipKzZSiWgirEHiLC1LHq62UXcuWIWRT1tHx19ZgG3TeTQF3lrLHwLo1Uk6wqzBfQVavIBtlUYVvGmYJfxwCixN0Iiox5g5rwPL7k5-Yftz03WmPOwfRg5TqVrzcUjwkFhCFlV6wnka3nXdzs29p-47ElEdHeKYIRFYa1Nec27mXyJtEdqF7egtG_9XJYhWuip1LrKqdEesll0Xbwfb4Ien9YMY7swUnuTNWnDj4kpQpDgy3XdsLA97Uh6StXR5_3KxpB6DvFHPfyUhvLae88TtLVMhHpAqEpC1iXpCk7IukxzdYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf1FPGDGccU9sv4XNl_17D40iuhtauhFiPJ0siggSK3w5x8m91vxwTj29ZLl30firclWwNG-CyOFhEYhk5lh42Y-nicuLwPy_ODws4P9-76m0Ml1CYJi5k-dPHZFD4gyn1C2vye9_qYK6udtt-wt22jztgdC5g3F4ibLtqj15qLkonozchfKzc9-kfxnNjxKts8u2ed0gVBgs1dr6-sGfiIJ_sqMKLkFEF4A1MATtmbtas_TMH3cO5ym5uNLyViJvY1lenWIgW8Tuqs8nStQu9rNzDFHTb0XxtZMBpLBZtGtZLF3ztYIZbRv8Q0-GdYfPWHBReOH6NzNom_FcS6ejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKVGNhhPVcsvCp0jV8pitnsvFuC0qnY5JzHiQh_Aoc1ndrbe11dZ-O0mw4HgFPvkwUQ11Cm01UV6Bls0Q2LlOOOSRkZGh-LLj1CX82zziTWwsnqKe46j7IO8r08aE71-2LQI1thdaasNcVtugQMt08NUDBldpt5A5wPFcIWxCknEMPbvwg534-qXnWYTI__tN6Ni3wjfjUKE-HdLeQ8FXFkhD3w81N642w9_jybZJHEbgnRJnR5O189QKx081Lbkd1XI1R8qwvWaArlMRtu8S64ShYXH0HdBToMHU3NMwjwRr9ExfoMfxvLviHzEETXxeyf1thxNfzaJTA2EQn2XUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=UFKTXvg1B5dbK6M2TwhMsytZMzKUXl0kqcVbhJ6OQkZfPQK_mGMVxJ066nRLeGSaD-jOWODqtfgEExNc_qYavCBEbYrpfjSLxpo02a8WNZUXh6YgYZJ61SwhqH7q6wtJ9D_T95MwYN-mr260audo0QxstOGOIT-f1gNbSGCKWIA7J3GE3_PZw8H518yGa-_WlEmNhsyvmIh_ZTDo-VOT_uMegT3e1R6pqml7ZJKhDIe1YEfjuqPqSXqW1MqfzwLwZMaLPdw_Kz1zaUeGUummDjZ_nyJEkBIiOJ25zNw_kDBXHTbe_a13EXYcXe-HC6O0mVSk2HcTrpPETn7AwnNMRRJx3fQYLkBkizf_ivvdYOtsMpqDdXF9SxsaHThY-pF6QSvcMOQjxaSLskNy0dlmInL011u_7TsxU6EaV7JtJxa8ndjPNTzB1qWl529FuIoyv6GIpezU8bQd8UkttxYYKuH2PMftubUnriThQzjHpiGbZdq0loYJDUvbJ9tx0XJ8dzOC1hg-E11aXVg3GQJI1LtYIq40tum4_nLjuwWHMkkEwc_be-It2r0fVZXNi_QHRlr_2RoDEiwE7_J_a9Rr5eTXM5Sq-goT3W4Z5QnkObBfT343M1JhG72n_zP5ODvT7X3ca7o67UvHpJKieMuYEs3-VZjZZ8EOrUkVCiQ_tXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=UFKTXvg1B5dbK6M2TwhMsytZMzKUXl0kqcVbhJ6OQkZfPQK_mGMVxJ066nRLeGSaD-jOWODqtfgEExNc_qYavCBEbYrpfjSLxpo02a8WNZUXh6YgYZJ61SwhqH7q6wtJ9D_T95MwYN-mr260audo0QxstOGOIT-f1gNbSGCKWIA7J3GE3_PZw8H518yGa-_WlEmNhsyvmIh_ZTDo-VOT_uMegT3e1R6pqml7ZJKhDIe1YEfjuqPqSXqW1MqfzwLwZMaLPdw_Kz1zaUeGUummDjZ_nyJEkBIiOJ25zNw_kDBXHTbe_a13EXYcXe-HC6O0mVSk2HcTrpPETn7AwnNMRRJx3fQYLkBkizf_ivvdYOtsMpqDdXF9SxsaHThY-pF6QSvcMOQjxaSLskNy0dlmInL011u_7TsxU6EaV7JtJxa8ndjPNTzB1qWl529FuIoyv6GIpezU8bQd8UkttxYYKuH2PMftubUnriThQzjHpiGbZdq0loYJDUvbJ9tx0XJ8dzOC1hg-E11aXVg3GQJI1LtYIq40tum4_nLjuwWHMkkEwc_be-It2r0fVZXNi_QHRlr_2RoDEiwE7_J_a9Rr5eTXM5Sq-goT3W4Z5QnkObBfT343M1JhG72n_zP5ODvT7X3ca7o67UvHpJKieMuYEs3-VZjZZ8EOrUkVCiQ_tXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGn9elZ2oywSrwnj_OaJKVzweSVI7xgiUT_4d9KCi3rbRiDDxt_p3u6tfswuKSjJFOj8TFjR9pq8teztxFCjQze4nnmRlBJkxZgtNg2qtOuBzD9i3gltAZ-_Q0rZFViFXO4ncp4bOmpURoi2cLzJ3t8HFmFre0Uuh2iTGVnlF_wHomv7nU70MxQqoyngzPAr8bB1DKF6X9T_DFWqfB9cnCGHKz7fXIhRdp0963cPlKmkBDH_1xH1jkAsloJi0jvqkYXfUx64AMTW1pNs0JhfMZ5yip-0ejYb7x32XUVlK5sPeSQTJgid0m0_v_aqvJiI2OdGOTuh0ofNhE8p6FgerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlTrUd7n6kB0iQbCCOsB_MGlqFAvUHJQK-0XMC-fQntUveUcatKkdH-uaKi0F9RSqKpL_Yt7tXMG_anxilb7rtFzvR-B2WyZwVb4ncukIaeK8fJEy7_QEHVsNc8BMq1Sg9AKb3Ap6LqTwG8aDGWZ7Y6IxDr2VaGGjqfdv6AR_YZ20plIfUc3JbpBPUnODMhjYrILxpXpsxuJ5RX_NwhfOdYmkw4l4tway45Zy4CtQkpMu3fzUmXov20OvmRf1vMurysNtpWcUVqMQIQjxyR5hOU70lQAjdwX_V3boHnS5WGZL9ifesBSwiCiRxlhfxBI6he_o2t9yKopbnG1ZlEPs0jM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlTrUd7n6kB0iQbCCOsB_MGlqFAvUHJQK-0XMC-fQntUveUcatKkdH-uaKi0F9RSqKpL_Yt7tXMG_anxilb7rtFzvR-B2WyZwVb4ncukIaeK8fJEy7_QEHVsNc8BMq1Sg9AKb3Ap6LqTwG8aDGWZ7Y6IxDr2VaGGjqfdv6AR_YZ20plIfUc3JbpBPUnODMhjYrILxpXpsxuJ5RX_NwhfOdYmkw4l4tway45Zy4CtQkpMu3fzUmXov20OvmRf1vMurysNtpWcUVqMQIQjxyR5hOU70lQAjdwX_V3boHnS5WGZL9ifesBSwiCiRxlhfxBI6he_o2t9yKopbnG1ZlEPs0jM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=eB4VRvF4gKAig2mdx4ss18v5TkiPTrBlQtGqewnfFrz8Mf8bkUI0nTSvL_Kdl9lFMHJwMtkjdPGQPvcAGpGK-YbIiBYVls97-uKM_l598Bc46Fwfv2Jo2tjmi9zdcvpXcyXb7wbd46o9ubTjMz6rYCh40RDszwj6frTbuClEAN_DUUEIdyRWB0OgCka4SJC61WqtX_63hSX3BX78FNyBWbBWosvRfcFZbK-7t063l5CAk_hCwEtBIkOchS5wMo1382hUozRt5HiGCUSjqyPTNncR0LfYR9VJVbVX4N3Wb2TFPdYVXOhemxB386-NVIWWZmXFZo7kXBMxonO3rgGH-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=eB4VRvF4gKAig2mdx4ss18v5TkiPTrBlQtGqewnfFrz8Mf8bkUI0nTSvL_Kdl9lFMHJwMtkjdPGQPvcAGpGK-YbIiBYVls97-uKM_l598Bc46Fwfv2Jo2tjmi9zdcvpXcyXb7wbd46o9ubTjMz6rYCh40RDszwj6frTbuClEAN_DUUEIdyRWB0OgCka4SJC61WqtX_63hSX3BX78FNyBWbBWosvRfcFZbK-7t063l5CAk_hCwEtBIkOchS5wMo1382hUozRt5HiGCUSjqyPTNncR0LfYR9VJVbVX4N3Wb2TFPdYVXOhemxB386-NVIWWZmXFZo7kXBMxonO3rgGH-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=jgRYkhQd37fhFl2aCUSsgb-_kLZ4pHBvr4a8RTZp0ibbz5FucsihNdTu76ASD5OuBT8I75IOok8yjub3qu-krRYED86Y8JBjZkVCTNOzYOH3y037zYH-xP0E28PoHXMondY07QQebl71YVQiE17lYsin4PrnyDRr9qx5xBEjqLOIlyrP-_147Bz4o0OwZTjabWVoBL9pTFJGb6hj_pg01-vwgcywQCp2Bj46qzqsI7piVF1Zake71B_w6Ibtce1NiJZpBcrLOuIAcMAXm4e4mZ5ljb_caLtpFz-UZRWUpFtww5eLF6mvJeJc_cT5sOmfmMLXNIfo81LXt5Q24SP-5pxnIDHfhCIrwNJFHhsqsagvoV-nlsaT7Ycx8yA0EvfwbcxoiExylBWFuoJ9XQGwXS-lYR-eQvsyoJtE05tDIlU23z5Tz7s60TVcseTfjGqn6uXejZBmVF_m3MfCLeo-fqkxMqAswrh23cyDfAAH32nFe6Ujwf_mQd-AIVg7rcqZcCxkeRMPQUtX0H93j-qXI1Koq8gTjUut6cS1aDJ9w3hSxtfHHiwXfsHWykemnUnrc1SVqpkkOYWW27ZqOP8pflfOHwOHnc1fueUeUcJe2oJz-cGWvPNBdmMIRBqla4chDPG-60m2CI95yeg52_qS5Ju7m0Qd89mQO8UZSOr6OdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=jgRYkhQd37fhFl2aCUSsgb-_kLZ4pHBvr4a8RTZp0ibbz5FucsihNdTu76ASD5OuBT8I75IOok8yjub3qu-krRYED86Y8JBjZkVCTNOzYOH3y037zYH-xP0E28PoHXMondY07QQebl71YVQiE17lYsin4PrnyDRr9qx5xBEjqLOIlyrP-_147Bz4o0OwZTjabWVoBL9pTFJGb6hj_pg01-vwgcywQCp2Bj46qzqsI7piVF1Zake71B_w6Ibtce1NiJZpBcrLOuIAcMAXm4e4mZ5ljb_caLtpFz-UZRWUpFtww5eLF6mvJeJc_cT5sOmfmMLXNIfo81LXt5Q24SP-5pxnIDHfhCIrwNJFHhsqsagvoV-nlsaT7Ycx8yA0EvfwbcxoiExylBWFuoJ9XQGwXS-lYR-eQvsyoJtE05tDIlU23z5Tz7s60TVcseTfjGqn6uXejZBmVF_m3MfCLeo-fqkxMqAswrh23cyDfAAH32nFe6Ujwf_mQd-AIVg7rcqZcCxkeRMPQUtX0H93j-qXI1Koq8gTjUut6cS1aDJ9w3hSxtfHHiwXfsHWykemnUnrc1SVqpkkOYWW27ZqOP8pflfOHwOHnc1fueUeUcJe2oJz-cGWvPNBdmMIRBqla4chDPG-60m2CI95yeg52_qS5Ju7m0Qd89mQO8UZSOr6OdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6ko0-7z8bOtdm1o5WcTQL5QQtZK7e3NQfXZizPUpYjM2C3yoz7FOV6EWLqA7WZbKX2A9a3RrDeCBG7AYzvKas72RspenzTHcnY7v140n4RMFTQKBnA_CHDxEUg3kLXAwSy6Nb-kbvM_JvXn0M9e2Pi4LOhRKHLH-e3iOQMEdCzqqWCzKQzAwIVYtpCavvvV4ioMa006vgXMpb9SuWxBJQlXLSe-OPLeO48AGR3TpkUe7RPE1EARy87ltZtz_VG6e_dW8WJVQJmSjmhQEtD8zZ1lajZhsUPZZbHagsGvxHOOv9M2maAZZXGr09u1yMBA3qRPZzHVrzazyGYVfASkQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMcZV4V-eUIfW97oIL58ZDV9Oy5ijRpnuYBzB5oXDvEC9BfGMBNiaGZBCll7Pm_v1aeWmkOs9ltAKdX9TV2sgfaHzF_SZvQwhH1kMIwD-0i6LBQfl9SvTjbk-UvHp6fdcdtufiD_vrB8ZTKdhBb6VG5M_aJUj4eLG9XAZQzwGwFEPow0pamiG4iKhakfd3xlXiZ_cEM4Dx_kKj6t68m-Ta4tLICCuiAUrDEdAGse_g9MKClSXvBh-4UxfPiJUgEDK8H_M4oNZkzKN-thRnHJxAqB2nVlHab2hZD31mf4CzHbsyFw3ovE87_epsWPled3WuyMyCac3hdAHFdembECNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=ghcqBm8j1RWvN7GglmkZTPrlw6xdZtoUynWuw3ECbMZTgVWnf55HS080GjDXlTY1of7q1hx4MpiVkSsxIy3e2pcpgi-RpZQNYVm2g3sL1XN7M9eAkj9ehDlNXNlA7oWoxDYyXAQX3BmEgF9qNEdVqp3K3uyuC-YHqQkzTOlYeQ-I7AzF-BRLEWOIZt4o5YRYMhWrUjIzJP9_NZc2wuEBexfy1MsqF7fZCaJVbDL0tkPFXMidIglpJ9v9T7btlJY8zgSBowWIbDTwHblPGGgDYAd3vC97eNDNXSNmogE0hXybO9l0reJuuBlvbuLlN2CMDuf8e4GUdyJ99G6fS_XupQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=ghcqBm8j1RWvN7GglmkZTPrlw6xdZtoUynWuw3ECbMZTgVWnf55HS080GjDXlTY1of7q1hx4MpiVkSsxIy3e2pcpgi-RpZQNYVm2g3sL1XN7M9eAkj9ehDlNXNlA7oWoxDYyXAQX3BmEgF9qNEdVqp3K3uyuC-YHqQkzTOlYeQ-I7AzF-BRLEWOIZt4o5YRYMhWrUjIzJP9_NZc2wuEBexfy1MsqF7fZCaJVbDL0tkPFXMidIglpJ9v9T7btlJY8zgSBowWIbDTwHblPGGgDYAd3vC97eNDNXSNmogE0hXybO9l0reJuuBlvbuLlN2CMDuf8e4GUdyJ99G6fS_XupQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=HNPVsFyaJ1OsR7-r9OWwnMiEhri4_pJRIH0e7xdaplcFUnDvnaO02-Hey-w_LOS0Nnwmg-k2Y_b_RMRqSy8brxgvorHNm6IyD16f-t-nbKMOoqg6UUKFHLrJxQNNRn10an65r7oidk5qyNvn4x6CUkAVYBAoWmAF3Vls_sL745iO0nj_-2oSKoPkZKkT4zjSEFCZeL69XbZ5Gv7Fw3uZxTixeIYyKKKJU5a_UM8_w0e2T8OvU5k7TrTm7JLR4a6wj7j2m1-LUIx9Jc1mAzg8w4Z_MOt-IwaO7BNkIsm610nScng3gykhr5zKQPDIZ7GgcSqHG4OUAbCR_8SrJsgVSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=HNPVsFyaJ1OsR7-r9OWwnMiEhri4_pJRIH0e7xdaplcFUnDvnaO02-Hey-w_LOS0Nnwmg-k2Y_b_RMRqSy8brxgvorHNm6IyD16f-t-nbKMOoqg6UUKFHLrJxQNNRn10an65r7oidk5qyNvn4x6CUkAVYBAoWmAF3Vls_sL745iO0nj_-2oSKoPkZKkT4zjSEFCZeL69XbZ5Gv7Fw3uZxTixeIYyKKKJU5a_UM8_w0e2T8OvU5k7TrTm7JLR4a6wj7j2m1-LUIx9Jc1mAzg8w4Z_MOt-IwaO7BNkIsm610nScng3gykhr5zKQPDIZ7GgcSqHG4OUAbCR_8SrJsgVSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=sGGBbv6KCtR7DLr15i-JFLL8Qnd36lyDJ_BHnJA7iSeusrwjC9fA4cb3CR4cmv2lPHEACrlUxCPuU6U9uWCf15mUBrEIIqIQ8vGQqdYOVQaDRFXhFKznz8iRurm-tmxZ9erdAp1UCImWnjcXX5tdyp_Nhoxthuw6Qz02j09x5BrhNrYgmztqushkyMu5WNST4xTWnG-t0kbArp4PjtKu8R7jktWLMe_GmxfcJgfO5kT2YrNrtcox1TlOIVBtKzjHFRNZfvdA0U3MjtwOMx5ETFmCgGF-ufiSH1cW9ICMch6PDEUJR99qpC0DJ1udh1ixVldNisR2CzL_9JLv4NkKcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=sGGBbv6KCtR7DLr15i-JFLL8Qnd36lyDJ_BHnJA7iSeusrwjC9fA4cb3CR4cmv2lPHEACrlUxCPuU6U9uWCf15mUBrEIIqIQ8vGQqdYOVQaDRFXhFKznz8iRurm-tmxZ9erdAp1UCImWnjcXX5tdyp_Nhoxthuw6Qz02j09x5BrhNrYgmztqushkyMu5WNST4xTWnG-t0kbArp4PjtKu8R7jktWLMe_GmxfcJgfO5kT2YrNrtcox1TlOIVBtKzjHFRNZfvdA0U3MjtwOMx5ETFmCgGF-ufiSH1cW9ICMch6PDEUJR99qpC0DJ1udh1ixVldNisR2CzL_9JLv4NkKcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=cz4PjCveRt2PzJIvsFmY3QUY01v2enMEQNCULFGigazAoT3jd5ccOCvQ4XA7V-tTV6E6qh8D3uqVrdXrd_wBzmXpBF1v8FqhuxRp2GK94PX7yH1jL_YcJnXtN93sTNw1sEqlFkVksW-OhcXqdRjsy1N8oHZZLdlNS5kEfIe1knxbdsyxKWc8x4Nsw1oBOa4IssldfeiUO5Fc8TRkQokvyrv9Iv04uA8GnvITMsTzEkfbJl8pZhKOZRm9hHxzPrLfPwonSImO77ltbyoP1JAsTHJGDV0EpNTjWX1RvNiEszKYghYiPqxxEpE2ODA2TSA70mAHlq_vmXHTetw6bi9npQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=cz4PjCveRt2PzJIvsFmY3QUY01v2enMEQNCULFGigazAoT3jd5ccOCvQ4XA7V-tTV6E6qh8D3uqVrdXrd_wBzmXpBF1v8FqhuxRp2GK94PX7yH1jL_YcJnXtN93sTNw1sEqlFkVksW-OhcXqdRjsy1N8oHZZLdlNS5kEfIe1knxbdsyxKWc8x4Nsw1oBOa4IssldfeiUO5Fc8TRkQokvyrv9Iv04uA8GnvITMsTzEkfbJl8pZhKOZRm9hHxzPrLfPwonSImO77ltbyoP1JAsTHJGDV0EpNTjWX1RvNiEszKYghYiPqxxEpE2ODA2TSA70mAHlq_vmXHTetw6bi9npQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eteFPHliWBYUhm-IghKmGBdP7Dg5UUjnsQRAF2ryJh4uzUHGTTASimeUd_BPLBgbdVyEiA-2FQYaPQAoM-DqMy65CvTCwbPkju1jBQpOCvOT2TaMP7pKLq4HPirbKUR0CoyWuWFqWfF3PYFZQJBACI3A97AAyHyvPZABJYoyn9ZJCTHPyl7nFEN-gCbFbinvjPJMydMsNSVNdqlTQjLjmLVC7WQWc4Fmy61iKupwlAUiDxtJSzMKRU43Atq-C6Lxh6E_Q9cNCepagqUtUnjBmPA3PObpm615yDeuxZ7p0sjW6jhaBoIH9EvCY4bxuOY-Qzq7oL9a3nHjccf50vxvrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDOgxgHNtJZvNAJl60GPdd3p-_70hIWPr2YjISf0WVE0TJYeU8foFf0lpC2O8sMhATUnDupCab1HqiPHhnraJeXr-b6zWxUXUoM3YC-jXjzawqYEVoSpZqP8KtOK4C22HR-zyNKfbDGFPaYImJnkVEXi1rq3M6zcQCEWykj_jARp8RrGWDFgAe0IkUc1oKY7Q9Wkikda4JXoYg8cMz1cuRqQIBwR_XjQ_TcgA9m8ODRm2_BobUgxPUi08XU0EmWz5-1o_bSzloNOirrHN971Ec4qMOV0HBorM2CIlz2wJE6wIYMQO14_vIK1pBcjAOhHHgOQSeUgRhWOzLd32CMBIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=LfzYM93BJK--HXFJcGVXclLG1IZkr4p4YWrFwZJnzbl3gnNzGVOLUMOe_-h9hioICdy2mWIaZs71Zjp1ZWZqbaQJqamwdIl5e2Wl8GKg_zuU44HTZnirUa32m7LGqmgXavoopGIwZi8wpPvdDXQxx3T7lmIjTaHSE81e6sHyZDrqm4SwyhoXlDbSXN0qaJ2fROd5n2rkdPqufac213mDromBSZ9cuBppeXvlTTXgXQO-X2laTC15pftOTP7ziejqk39xqOrJn6A8L1R1vcBCVNwK4laET24uZs7eE-qvfLS0XLS_Dk4eJu8kkRJfg2SX7ryWN_6gmogdVlvnI-MteA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=LfzYM93BJK--HXFJcGVXclLG1IZkr4p4YWrFwZJnzbl3gnNzGVOLUMOe_-h9hioICdy2mWIaZs71Zjp1ZWZqbaQJqamwdIl5e2Wl8GKg_zuU44HTZnirUa32m7LGqmgXavoopGIwZi8wpPvdDXQxx3T7lmIjTaHSE81e6sHyZDrqm4SwyhoXlDbSXN0qaJ2fROd5n2rkdPqufac213mDromBSZ9cuBppeXvlTTXgXQO-X2laTC15pftOTP7ziejqk39xqOrJn6A8L1R1vcBCVNwK4laET24uZs7eE-qvfLS0XLS_Dk4eJu8kkRJfg2SX7ryWN_6gmogdVlvnI-MteA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=mcZHYH2T4AT83lI4HIO159Th_u2aU86dxpFXy0X7cc3dnvkXgjHP3nUDpuoTETlsJyn5fiykVl6OyAy4tHDY1il84rB6L0QcUplC3z5ngme8zFzMcQ1XUSFogD8asyD6Tfu4_WH4_-179RzzWghedjXy7n2kELnjP_Q-T3ATmSkGywfYXnTMCXzqh__K6AmYi7O6IwiN84KjG_Qsi_GhuoJyb-fUss576HXhQTOzNp0c3WwlaOdpO25oipjW2ZzjaPkveqpHNGcNbw96thEwk4X-XtEbLeCG4bULkiYG7jYweTb_7LRHJaqt8W0qQ6ZONRziO34pJ0wmEb1vuNyp8ijz6TFLHE4x0rOyIh3NgFsTZIMKp-jLCOD10xmTqBOX2T6Tb75q-v59oK5bKEjRAirqKuwA-1mweldy7aD0i8Np6fOG5tWy9SzN0fiXRjAexEv9BdoiCFDvITdQHJRCZyR3z9K9YwOOGz4t3s19hUEYj5GGlmk408lOVHX4KICzg62VQsOzo5msjf9LwC9R62GTdczATMYRbATIw-I5tMx0KeRZf_OPTWlWYxj5nS5lVOC4zghj-2kBTjXXHEn3pYmFnRQXQ-nNv9D6CCHXfmEjRCJKeaN2WwIBs2MQoc-ZeAM2h3GCSf9_d0xxJbY3fSCsKL9HT6gI18awyaa3udg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=mcZHYH2T4AT83lI4HIO159Th_u2aU86dxpFXy0X7cc3dnvkXgjHP3nUDpuoTETlsJyn5fiykVl6OyAy4tHDY1il84rB6L0QcUplC3z5ngme8zFzMcQ1XUSFogD8asyD6Tfu4_WH4_-179RzzWghedjXy7n2kELnjP_Q-T3ATmSkGywfYXnTMCXzqh__K6AmYi7O6IwiN84KjG_Qsi_GhuoJyb-fUss576HXhQTOzNp0c3WwlaOdpO25oipjW2ZzjaPkveqpHNGcNbw96thEwk4X-XtEbLeCG4bULkiYG7jYweTb_7LRHJaqt8W0qQ6ZONRziO34pJ0wmEb1vuNyp8ijz6TFLHE4x0rOyIh3NgFsTZIMKp-jLCOD10xmTqBOX2T6Tb75q-v59oK5bKEjRAirqKuwA-1mweldy7aD0i8Np6fOG5tWy9SzN0fiXRjAexEv9BdoiCFDvITdQHJRCZyR3z9K9YwOOGz4t3s19hUEYj5GGlmk408lOVHX4KICzg62VQsOzo5msjf9LwC9R62GTdczATMYRbATIw-I5tMx0KeRZf_OPTWlWYxj5nS5lVOC4zghj-2kBTjXXHEn3pYmFnRQXQ-nNv9D6CCHXfmEjRCJKeaN2WwIBs2MQoc-ZeAM2h3GCSf9_d0xxJbY3fSCsKL9HT6gI18awyaa3udg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=lcygEXRMKer3NwfpOdgM4pM-NQUGQnRagujiymwInNcajATi1fFwjPUQP_G-liVdNOsCuF9n9-guejEtnx_i11RgGv3ygJ4ACwLccIGH5-P7omv2aahFsbZOWigHErH5nBztBh5rpGY_xcup-LS-pwX0QzUSHkMzqCBHcWwucHdYGaDzUGdf9Y8joxciChvs0jsCgrIl8RKL3JZme0kqPjboO6nSLTTP-Z1kRbBUJlMG-vq7Iz4z9tDzlNXPLcUS_1OYKc-jhTJjRK5MNm3L19YCtC48M5iGKEy19Ap9qgjTSjPmHFNcskbVfHc_lMpxQiHwZb6bgq2slwM9uaCgtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=lcygEXRMKer3NwfpOdgM4pM-NQUGQnRagujiymwInNcajATi1fFwjPUQP_G-liVdNOsCuF9n9-guejEtnx_i11RgGv3ygJ4ACwLccIGH5-P7omv2aahFsbZOWigHErH5nBztBh5rpGY_xcup-LS-pwX0QzUSHkMzqCBHcWwucHdYGaDzUGdf9Y8joxciChvs0jsCgrIl8RKL3JZme0kqPjboO6nSLTTP-Z1kRbBUJlMG-vq7Iz4z9tDzlNXPLcUS_1OYKc-jhTJjRK5MNm3L19YCtC48M5iGKEy19Ap9qgjTSjPmHFNcskbVfHc_lMpxQiHwZb6bgq2slwM9uaCgtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
