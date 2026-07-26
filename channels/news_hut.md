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
<img src="https://cdn4.telesco.pe/file/PYvkd-GTfp9RNpmKWmsuepLgvDaLAPwRDvz7YXofKsG_C-LMOf7PppC9eW_AR1JjDu1K_zN3hSYYsV9ZmGs0Yvd9t9vJtqDQ2kyyeehLKb3SxEHnC2DC1ZTBOhWV31OlZ2_VOJObeSwD7RND4WcFRmHN-6gImuHzvbII2IVMA4DCYaneKJmq-OCEsQ8rB9lZ77kIVRFKR3aBTMjCWrpe6RkuDQ9_D03xAY7anW1INRYqyVoWhQt-8sjCmR_XioTG0M8xRlyi6QyQhaxWppCN4PquuF7D9L3iiRnocQRSCwcc72X2cDpSFRp02KffArMwGsL_Si4hIyiD1LZatzbH-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 149K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 11:00:43</div>
<hr>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuT63B1GKxsVNAKqRniCAOCIUaGABCPKioWq0veF0wpQxRwTHMm6yPBV0vdUTlHocifarYQ8ElQsUtVhu63bzxKlG-Z_7mfp5OgN5AaJ54_h4u7Cupl9rgFSjPAZxU6QtIbvb2mfwj_K6_9x7ZHcilwXNxuYBtTpvJk7gFPr5ACnYCP2drwcV-bDDfAIPEH7pdzpi5a_2GHx0NRlHcYJtVTJJ6gm7QejECQ6My_r1932nS6XVRD1g47NZH-n-SodnHdVZVy92kFiUtnGbm-BHW8VsX5aGGx3GdLnkB5aIoNtq4e4NRlpwcY32lGxZ3XcbMW7bLH0j9J8wN2RinIZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt8n_TpB0cFjFBi2s1PaMRRl7PeUTtpqBFH-tTkq0ukwrlfIKpSJxcmGN8y-huDKaIl8z1c6C81fUyKW8TVDbL0wRwS2GvXHXXPojazRy2RjXhMUYgpwUuZqg0OlzsAHF4YLDAR-I5IbhwIP8rZfNty-kmGKl9aYX_vlFNLMEilg7YouudwY9vBCPnHHdGClvdeWc61AjJwwY5IO-y2QAsL0mDL5-1NDDcijEN4vxhcQgmeEGeWt89siWnFBvwgMRCHWPUfWRmUEdat0O24bLGL2pfRSIYHWhWlw3PwNKr7T6BvBRu3F3BcwDVOBYnZ3wVV85UeV0FIWuubvnIQmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_grE6OHQBPvQvezozuJenYYGsYRXjuQknrzZPEc9mW5gvXTELXK_aSk-YtmRDlCjPIsst2tPyrdAJbInR1JWlIB3UvcdiKT8wUGxsA09eBBV-XHRhZyehHMmjUDfYlqQEQJKG_KsdC9Qb8ufsn4KCdU2EuVTn_KdEq8pmmSoUqv8U4ujFPyKYku8IKjEii_lBaFJvgfJ0p9aAWSJUjY0vi9Z2rcvjaNYOYTGmpRh09VE2543mmK4fnwnoiesIjP4TR5rjWdQuc6mALXba7Kgcq2d8wV0HjNT_vdDNCy_J5bWpw_VqKYtZzHBWfi5foN-eOGT8fP3E2Dvj7DsUcJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=EqniXM4m6OMvdVX7nYhd37oSTOtnhjylTQz6K0iXvzlVTVz2QFVAjtZX-WAl79IaswW6c4iGHePJCKMSozZnk7xkFTz--Fkuoa4jVj3Leodf23bFlQsfY3F8idnhHcEikkTycY3HPsW95z_Obdx21euLYZFC6XpJKxSR58UX2MQICBYggEtOw2GTyCT2bhfymbctoyFFUGdFzl_v_B-Xkaqn0PZ8Mg62FnJAOfih4fm5SV3RLjohUktBNWtWJBQeGxRGIGKatOr6oFvekW-FoS7_FrAZLgyKS_CJvYxPzKc6AYAKJV9tS79B6xhtE3ZBX_L2Yl3oIGS8ma8InFjC2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=EqniXM4m6OMvdVX7nYhd37oSTOtnhjylTQz6K0iXvzlVTVz2QFVAjtZX-WAl79IaswW6c4iGHePJCKMSozZnk7xkFTz--Fkuoa4jVj3Leodf23bFlQsfY3F8idnhHcEikkTycY3HPsW95z_Obdx21euLYZFC6XpJKxSR58UX2MQICBYggEtOw2GTyCT2bhfymbctoyFFUGdFzl_v_B-Xkaqn0PZ8Mg62FnJAOfih4fm5SV3RLjohUktBNWtWJBQeGxRGIGKatOr6oFvekW-FoS7_FrAZLgyKS_CJvYxPzKc6AYAKJV9tS79B6xhtE3ZBX_L2Yl3oIGS8ma8InFjC2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1C3-VgQcfcryqgOkebK_uQ365IIOulvJo-pLPGzmcngvq6gxp1Ex58Hfgta2j1xmSjLUHa_-E09v8344vGZhO2k5rDxbCwPLHG7lJ7aQqNZXYElPU-Lk0YA9GcJYyq8xMmN39iGmoEnE_tsIO1flK473XF3cPR-jqEERP3r7f2RaPP1-JejBJXklxqXGIa5eWLkMzzhJo9J9AE3xkElaN__iOA4Viec5x0uGRWfqGTP-JE8awT5hpXZ7pBrRUmpZdETrcqSmTZGuaJn13x6uWxiA-F_5SoeVuAp3SMnBSHp0lxNf4_LbSi39qte2zIazTLnqamE5MYVlB9VbEnb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUc1DqU0SAG3Uh48ed3v2uA0KRGQPwuHqVSNTxRri1oMwOgi8CNC6Ys20fKWryVrVCt1JGDJc2eXDvxQB3CiOIn5_qmiArDnVI0o3uN3db95SDRnjv0V_J3aO9B18yltNBgTNsz6syH56RvvFsmmWZiSJtZNTFAj5QhNdDPpZ9AN86vurG6ELLncSPKVcs8iy_sMabdUuSgjzeDQqvj79Pd5WO0hkhKkDu3w02m65vozczk0xQs4vay7TtG85eK3iI43-Gfx1fkzGmR1z1jWuy9ATegvdJPqZXEpzTl-xFu0TTVVk0gO4IyLsfmG1xvCBfHjRSuwsdzjJtOOwz3pOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT066vbXZVvUEEXkVWveOlNR1CjcIztnenLL73Jx_5aqK9L1rwJNA1QcvH6n-l5hugcFT1gwlAwM1I3pb_6RxXJaKr1IVErss292kWz2MBzw74qPDH3k2M7srEgKixJxCsiKQGbVkp65zkJQJUChV6Ri62ULHgC3oRoFJxPro0v2XCGp8ljK0hSCVRk04HUVmM_xiVPLaELvWEO7AD1wO5MQ6K50ER3wEuuUL6I9DzygDTR8AK6ZPhgQ0vQN__E51A7jn8pqF6BC11cZGpAeRhSBDKUbgAtq0hmtLHUEr9bM9TKGo449D0cQuXa0oYuWa8xxHoMQWLP2nB7eCi055Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=fV0cqwTaJGmTCtq7WR-KbgLmXp9cGNPn-TLr7L_PXnekZvkMT4T4tsrFPFxNhFBrOzS7MdrKJiE9sYnXMCf-M9rI_XY5zTS9lz6ofB0GfB9AxRldAp1Y1_NvkcTfB4Ytye8y8rlw3NKdTs1xe5M91oatpCLIW8pb_XoZUKDkRDHmJ_Gu3Q1-DbuQ2xK_K8vY59JkCb5iEiVAXpEE9uaZnzSRycuDqxZwMEbCEvRAMXsha3t7YmVgCHtRHKDjefLEIKCohjxEAKCzhArLvVwQeZq5PmlRENHRpBL-Uc3q7G0dCVB0BqxqazTdqwEVyFyA6h1QblotuwrzQ3_dyRbVww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=fV0cqwTaJGmTCtq7WR-KbgLmXp9cGNPn-TLr7L_PXnekZvkMT4T4tsrFPFxNhFBrOzS7MdrKJiE9sYnXMCf-M9rI_XY5zTS9lz6ofB0GfB9AxRldAp1Y1_NvkcTfB4Ytye8y8rlw3NKdTs1xe5M91oatpCLIW8pb_XoZUKDkRDHmJ_Gu3Q1-DbuQ2xK_K8vY59JkCb5iEiVAXpEE9uaZnzSRycuDqxZwMEbCEvRAMXsha3t7YmVgCHtRHKDjefLEIKCohjxEAKCzhArLvVwQeZq5PmlRENHRpBL-Uc3q7G0dCVB0BqxqazTdqwEVyFyA6h1QblotuwrzQ3_dyRbVww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxxS86Te4H1EutF0Ly8bwwYyp-gHoOPdqka1mKR9IAfq0gVvtFtqW6J_0Kp-4zMyLlhRvZRs1mZcvBYm-l1-rgSKq5UGs0FhZ30MDxSq_tYG9H1c7AIWSZkjiMltjhdZy8hbgt3m1bAmll1QOC_lhQ9dEZ04UdeX00IUM10sxUQX-CwioiIcTrNXSUsflvDcHPwcS0pVtgH-UaH7cx2xgxJFk_7EowM00WSpNi5d7fygb-D5YguuYtKTYcFA0pYqCXNwA915GM-ue0o80mb6zDh-LGMFOOGKdIVbgLzXk-Mi5h0pZwFsAs-Jweui1kEaZoVc9f_XXdrBnHXMr-KJjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=aIetjiKWkgaC8-jnSBmbD-Tq_rdUPveNXTafUpyJQ2foNQbD1wtgeMbx-p8n_W881ZfSMTSiUe_gMUlvTaPGnTltUQuUx4VCcz_6aLscxjLjgo9pf8QB2f8pFgHNgy6u3nQIoCUI_sBmPEBhGKdjz75yX_bqdZlhVzWgHJ4izCU3_moP8yVGZ0wlh64yyG56KGD9jBjt9jvoHWFX5FvM4Tbw0pWsyaQVPCm_i2JkGU2JAObisqmiq94jc2prRoSKrdj-AYM4niQ6v160jXbYxEHY7eQt27JMGpBta_GETS9XstgxJdbFKQvHdEyBIqu5Rv3U6lJkFQCHUyDe7NL3Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=aIetjiKWkgaC8-jnSBmbD-Tq_rdUPveNXTafUpyJQ2foNQbD1wtgeMbx-p8n_W881ZfSMTSiUe_gMUlvTaPGnTltUQuUx4VCcz_6aLscxjLjgo9pf8QB2f8pFgHNgy6u3nQIoCUI_sBmPEBhGKdjz75yX_bqdZlhVzWgHJ4izCU3_moP8yVGZ0wlh64yyG56KGD9jBjt9jvoHWFX5FvM4Tbw0pWsyaQVPCm_i2JkGU2JAObisqmiq94jc2prRoSKrdj-AYM4niQ6v160jXbYxEHY7eQt27JMGpBta_GETS9XstgxJdbFKQvHdEyBIqu5Rv3U6lJkFQCHUyDe7NL3Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=PZv80O7blq0JmBQMBCnU0HAXoPp3RHXUsUgVEdNA7CJczfchTEXaFbeDnXCy425Bqf9Dd6U_5XjPJ1LPjdi8Ys49ANHPUPkjE557hmYpouIlAoblTv9pV4yKngbxkAp3I2uew26RwFex3GykuWfIEhaynI1IFjj4u4btYJBPBmvrw8hFczgpoR3yvqBOdtpSNal8BmOTOuHMtZf8JqLQCGjvPcT477oykHMKR-Oe06UFkU1Hr5ewiIvvoVms3xJfsPn0O_bBR-GBkA3Yn-gXqypIp62ZvgLD4ArVraySfVMJc_iVaKCUlQJQYnwqv-HTo0h4UKsfOTj2I1qKzfFiaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=PZv80O7blq0JmBQMBCnU0HAXoPp3RHXUsUgVEdNA7CJczfchTEXaFbeDnXCy425Bqf9Dd6U_5XjPJ1LPjdi8Ys49ANHPUPkjE557hmYpouIlAoblTv9pV4yKngbxkAp3I2uew26RwFex3GykuWfIEhaynI1IFjj4u4btYJBPBmvrw8hFczgpoR3yvqBOdtpSNal8BmOTOuHMtZf8JqLQCGjvPcT477oykHMKR-Oe06UFkU1Hr5ewiIvvoVms3xJfsPn0O_bBR-GBkA3Yn-gXqypIp62ZvgLD4ArVraySfVMJc_iVaKCUlQJQYnwqv-HTo0h4UKsfOTj2I1qKzfFiaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSh0BmAI8gCgZd5aEPST_cvNOcTmi6Za82EDj4YQqcn1easmc7RPhbnzmSFe_ZeRnCOpBhQm27OPP7JXKFckTHBOsAk5i_jj31LvWhBVcnm_DiN52fFbDlXcn0f0GLgRYcMeiYpq9JeVHdiNMyzv4rjbTz2FDXo_afAIQ3o6aEDJN5QdnddwnJMJExQlSag8udZsA3avOYFM7m9fdl0dyPpZB5yQwpRTE8MHWzOzpu3KNj-acpX3jfidwTs7yXyemTEeWbOc_cc7XwBKVh7MiVUqthZ_Mfnltzpb2sSKpxNQPkrViDlcee9alSlq_uOPT5JtIARiMa2lMPDnmB9_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=AtdxHqrf877s56EwzUUnAMCYKIv7_7FDFDcpZNy8mdixRFPir92PFuE57vRKH5tzup55zkEqXvihyqABRiXr00sRJpL2OzBlaQ4BfHrvAokehEtoduMygaL2ht_hx0cgwUP9kN5SqGQGVuuKQ3WcyBE0zhgK0byGC_fOhHO_XLJGeU9eMlGvrTzFqODrFRptbZAXo25d0o6AAntjj-gRJY12EPYxfEtFIt4Ua1vLK3op2axI8wrbVUtVr8MLarJYcbRyVrArqBcD4N-A7yyYl3xLdq9hJaLYPRq0Yvcw-jn6q7bd-KY1LbhT18hMeO1g2z0u98inCgoIO8SUt_G6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=AtdxHqrf877s56EwzUUnAMCYKIv7_7FDFDcpZNy8mdixRFPir92PFuE57vRKH5tzup55zkEqXvihyqABRiXr00sRJpL2OzBlaQ4BfHrvAokehEtoduMygaL2ht_hx0cgwUP9kN5SqGQGVuuKQ3WcyBE0zhgK0byGC_fOhHO_XLJGeU9eMlGvrTzFqODrFRptbZAXo25d0o6AAntjj-gRJY12EPYxfEtFIt4Ua1vLK3op2axI8wrbVUtVr8MLarJYcbRyVrArqBcD4N-A7yyYl3xLdq9hJaLYPRq0Yvcw-jn6q7bd-KY1LbhT18hMeO1g2z0u98inCgoIO8SUt_G6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=X752QPq-qz4qweM4B4DrJG152XOPG3Y9aJQDc0fZWx7RneZJ_epGNZ1T1IaVgvYQS3zHekseaweXNicD2FCBtRzmna2SU9kRvxPm1UAdlC-3h5FZIxGHtcTgwuZezUZcqevsIpN7eZpDDelG9CKpECv5vmRRpXiD_AEwbC5ayAXmKiL8XgEPqmWeVQLP0RqJYDlcNJQndgeYbMB0maiYnjtaAsonsDlu_tBVw7F3sTHcCyUAsCB6ABr_qu4FhdzBxHdYDpb3Pg77DS8VuYq4S7QO7MQChfYPz05379J3iehgyyqtydjTBxrw3OlS8k2se54opPLxIOiUmqQC3nhHaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=X752QPq-qz4qweM4B4DrJG152XOPG3Y9aJQDc0fZWx7RneZJ_epGNZ1T1IaVgvYQS3zHekseaweXNicD2FCBtRzmna2SU9kRvxPm1UAdlC-3h5FZIxGHtcTgwuZezUZcqevsIpN7eZpDDelG9CKpECv5vmRRpXiD_AEwbC5ayAXmKiL8XgEPqmWeVQLP0RqJYDlcNJQndgeYbMB0maiYnjtaAsonsDlu_tBVw7F3sTHcCyUAsCB6ABr_qu4FhdzBxHdYDpb3Pg77DS8VuYq4S7QO7MQChfYPz05379J3iehgyyqtydjTBxrw3OlS8k2se54opPLxIOiUmqQC3nhHaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=A4i_UImjuSp181oxlxaqRUVpZdAQogr9s9ko9fPAg2WWkr_PWtsbkD1uOqAYFCUplvEJ8VtgO62_dOad4SMiFHotMrz-gRsJgwGY0nMAIS6Ijkjyet_gTqiHOPvVbwAqgWQSg2Gs3CuPXnNFqYQmG-wbdDioaaW6-cBe0s3mDZnjKJ7MfOdfssXgwdQRwXh4UEGrdtnm1TudjW2GLgDE3EnoEBWlm3wLhKnOPg2TkiHz4JhCWJCK_yNczuf_3xtWBfdkw19A5V1fod_V0aRRXiYQlW0imKTiTYAa903M0DrQKIRbuEJfMvMUeCBLxD9Z3PvCKzYVRsgeZMzx0nQsOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=A4i_UImjuSp181oxlxaqRUVpZdAQogr9s9ko9fPAg2WWkr_PWtsbkD1uOqAYFCUplvEJ8VtgO62_dOad4SMiFHotMrz-gRsJgwGY0nMAIS6Ijkjyet_gTqiHOPvVbwAqgWQSg2Gs3CuPXnNFqYQmG-wbdDioaaW6-cBe0s3mDZnjKJ7MfOdfssXgwdQRwXh4UEGrdtnm1TudjW2GLgDE3EnoEBWlm3wLhKnOPg2TkiHz4JhCWJCK_yNczuf_3xtWBfdkw19A5V1fod_V0aRRXiYQlW0imKTiTYAa903M0DrQKIRbuEJfMvMUeCBLxD9Z3PvCKzYVRsgeZMzx0nQsOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fJbFRZFCCgYNwIRWjjhlHCr4kSu9UH7fEXbZE5G0wK5cmW3ukOZej7PkdStqlDdZdUKK6m4QkdWTwr3GcyHP5mg90iQWq10SWQ0FevDtcPR21ARorOjtPV9ob8HJt3xE7S3IjXN-GMk3bzwHamBPbb3ZCdsaza5Nh6GNnoKXCN7I5-mC1gaXv8-4RrwmB33mdSL13i4lhJ6XF2M0sBh6RvqG_tKRcCY0UYGjROrgpD1VtozQf3x97qf2kGrzCdZZzEJ2LXFhF63JBGGYPrGwhDrEc8uAfEAVGgirw_88-3aI1y8uePMdX7hXbCqGnH74LUs6UM--ETYZ-GaLziXSug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fJbFRZFCCgYNwIRWjjhlHCr4kSu9UH7fEXbZE5G0wK5cmW3ukOZej7PkdStqlDdZdUKK6m4QkdWTwr3GcyHP5mg90iQWq10SWQ0FevDtcPR21ARorOjtPV9ob8HJt3xE7S3IjXN-GMk3bzwHamBPbb3ZCdsaza5Nh6GNnoKXCN7I5-mC1gaXv8-4RrwmB33mdSL13i4lhJ6XF2M0sBh6RvqG_tKRcCY0UYGjROrgpD1VtozQf3x97qf2kGrzCdZZzEJ2LXFhF63JBGGYPrGwhDrEc8uAfEAVGgirw_88-3aI1y8uePMdX7hXbCqGnH74LUs6UM--ETYZ-GaLziXSug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=MHnevhGAXkWupFc21c9wSAQtHC8R_eqLaK45ptVQ5PwV1nu0cICrIAWD0U_92ALZr8k8VBvgdLv23a27lal0C4h2WHsMsOPQwDM1OkvBwza63aJmgNnAb_RU9sYh4rtD9m48JlMVkRDswjufV6v8KL_ELow-dtJ4YXOxpILwzq_zTSCxJAmtZi0EafgU2YwGJlcGqwg3efdTRM9ZSVEnDon_4GFU60TC4VR4Ylu_jr1cc4xCCCk4suYbmmcdBs8k6sWhwaaQKZdDBOzLgibQJq_dKDAunKVXUTRpVsQZIVzxvQKYjI5O1_m-lRaq3Wzd-u2VC4JJx1feqaovx0stjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=MHnevhGAXkWupFc21c9wSAQtHC8R_eqLaK45ptVQ5PwV1nu0cICrIAWD0U_92ALZr8k8VBvgdLv23a27lal0C4h2WHsMsOPQwDM1OkvBwza63aJmgNnAb_RU9sYh4rtD9m48JlMVkRDswjufV6v8KL_ELow-dtJ4YXOxpILwzq_zTSCxJAmtZi0EafgU2YwGJlcGqwg3efdTRM9ZSVEnDon_4GFU60TC4VR4Ylu_jr1cc4xCCCk4suYbmmcdBs8k6sWhwaaQKZdDBOzLgibQJq_dKDAunKVXUTRpVsQZIVzxvQKYjI5O1_m-lRaq3Wzd-u2VC4JJx1feqaovx0stjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlaHPhx4-xCMeKVcpbu59G1NJ3OklrZv48iCBFj9Mf_i6BznpNgJX_hQyyUR-wq4rrx6qq1ebRPLm0IeXHeeXYvrAw6UMjF0zsfgls2MHhFtABSQZ-tyXHvKpj4AVU44rOnv8W-kzOaKBELt4LcbHciMWgJKEqGk6Ifb7us2ukizxFfDqDSWlnKnMGOqI9iuUALs1h-q7g8OpyiqC_G1XCzTtJMavgYnI0dbehOERq3veXJ5eTmTe8zIyhNh7sj5a9I2RCaEBC5ri3pLDo_ojF0zSL83ZmM_e456Udpc3kCWdeRGRM_7d-9c3Xh-vPeE9SCSuTzd8egwMv3gZjw5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=phHuMXE_dxpNg2ViGJ1xbpbRGeqdbdgEKFBxI9tYbZqQAKG7Bt9RN37QHn-ZxEv2WikYVBEalUITjaf8h3--Br6hU8J1ezmfG5fNAB8PuPkuCKLWn7Ja_Wauk9e_Y8vNIXUqbCmMGB-_nqXp4XFnQ2iiVwIKD0Vk3NhqvhMdDqSkXRHqqkymVe6BbMp5dTq5hBR51sxRxPf5JhZlfQUUCcUVKnGPYKror8h4ho3IQvDDmDvnbBNgYn5t67IIBVVZYBEdd9sbLTUc5yhwnlwGrZf9W25QXhY0E9FS8zWF2n5bmb-Zg3FBs59LzDHXrq6029_4zSSYPADI9aOaLHSVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=phHuMXE_dxpNg2ViGJ1xbpbRGeqdbdgEKFBxI9tYbZqQAKG7Bt9RN37QHn-ZxEv2WikYVBEalUITjaf8h3--Br6hU8J1ezmfG5fNAB8PuPkuCKLWn7Ja_Wauk9e_Y8vNIXUqbCmMGB-_nqXp4XFnQ2iiVwIKD0Vk3NhqvhMdDqSkXRHqqkymVe6BbMp5dTq5hBR51sxRxPf5JhZlfQUUCcUVKnGPYKror8h4ho3IQvDDmDvnbBNgYn5t67IIBVVZYBEdd9sbLTUc5yhwnlwGrZf9W25QXhY0E9FS8zWF2n5bmb-Zg3FBs59LzDHXrq6029_4zSSYPADI9aOaLHSVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvGz0K7XpgvaQxFRyCyWXWQ3UDmF4h2gMS8A1As14glMxi16DFJt6PIRBq07ue1q3VjRslbu2mlMxi7ekco8ErKa36ZqnY_TN9OXJkfPs-3sYr6dttFrR4GgD-EJDpWnXvoSVQAP1RCEyoFH3Uml-QaipD0ZxUXvLaTBXKpG_jyWQlMuceOvFrdxYVzYdJaWKg4Lt5AHxCXLx1YqC4cf3Xr8BGrgll2QIWAckzpbGZ66V6MRJeAYCU3NshkCzFB0Hi0saPb_TtZ884Gd2il1a9vKkIMNB9QqBAp8-J4MYj-Mcz-3V0lM1ctisfPr3fcS4NDlwpY1pnId4X-CVltUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=bmC2q_r9iy6MgP0ZnQOUUwtZwrn-TMIV-TOiUovlLoSqu6w25SbqEl9VusRpqMLRCgyoqvsFTMMascGkKXyrz3aTWB0WAfZkpRZQA_1IS-JGZDkI2k6C0-MGNl2JNkZhEVAXoosnjBq9aH9pkfZWLP_R6M6fqBHBmJt0CzrMOZ4W5aWzG9kaz6SVSk3r2AShSO2VOzckQLtqRi0were9ZBeVgQBds9eRE_8dbyqu3XIhb2R_dTWL1HF9qlwnrrz8VGXaeTEuyGj-K7EE3PLTHaz4kLQ0FyD8WB6YhKo2Bi4gFsgkjJ1LYQXhiXR0KJYYukwQmq9Q53iT-MlYE_AA3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=bmC2q_r9iy6MgP0ZnQOUUwtZwrn-TMIV-TOiUovlLoSqu6w25SbqEl9VusRpqMLRCgyoqvsFTMMascGkKXyrz3aTWB0WAfZkpRZQA_1IS-JGZDkI2k6C0-MGNl2JNkZhEVAXoosnjBq9aH9pkfZWLP_R6M6fqBHBmJt0CzrMOZ4W5aWzG9kaz6SVSk3r2AShSO2VOzckQLtqRi0were9ZBeVgQBds9eRE_8dbyqu3XIhb2R_dTWL1HF9qlwnrrz8VGXaeTEuyGj-K7EE3PLTHaz4kLQ0FyD8WB6YhKo2Bi4gFsgkjJ1LYQXhiXR0KJYYukwQmq9Q53iT-MlYE_AA3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=R5UYwch4VIC1YoaGXjWulgJSCRQz-ZG2QzE30W9VZzHyOGwIZAwNmA3OasBwzT9QP1aH41mWiMJ3ZheLlHIpN7qfK6bambDq3E2wKplMuaBv9sTVpGk4GTIiRAIQRUER8_EOatxKMofha6ADtxZGkkmJU2yUz4FW43K7rrcO2qvN9gAzJLs9ON6g6_rZktovwtmfEBDOxcs4l377-mnmQAeF8BEVliGpuQvm4zRpHkeTvjSHjdl-_3LunyUIZg1vRYnzYQgyEiCRpdYc8XQ0KXBlC6SioFE2iqQaXcTb8rZVc1TJ4r7R16FIScgGsvjL2_CckT2NSMK7icGiu7VTtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=R5UYwch4VIC1YoaGXjWulgJSCRQz-ZG2QzE30W9VZzHyOGwIZAwNmA3OasBwzT9QP1aH41mWiMJ3ZheLlHIpN7qfK6bambDq3E2wKplMuaBv9sTVpGk4GTIiRAIQRUER8_EOatxKMofha6ADtxZGkkmJU2yUz4FW43K7rrcO2qvN9gAzJLs9ON6g6_rZktovwtmfEBDOxcs4l377-mnmQAeF8BEVliGpuQvm4zRpHkeTvjSHjdl-_3LunyUIZg1vRYnzYQgyEiCRpdYc8XQ0KXBlC6SioFE2iqQaXcTb8rZVc1TJ4r7R16FIScgGsvjL2_CckT2NSMK7icGiu7VTtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=m7VitNqjBo712Q9NUqZQO7xH1CArjvp97X-dzD6X-JwOv8RtuUpLZtybqnmC96yMlnpNBNHsGDP5-_5lbpZPNJdl--Da-bPNlC2zI_Fbhi0S-KshM8nlAwwTDMdrzZgB4BH-VFm1wruxejc0W2fsRWo418ZohuTxvSb-FePsj02NIMURK73L2tT9grNij2mfQ4F2xO2tZccYh_S9b-UepM7vV95Oko4SberWiRPqxlvJJPADaxhDCUXfpk3DpEo4AZjoA2-EY_ph4Rca9hnSe6c01zGNVqIQhp0kILdHJPV6_jgMKBbUmT-tAnl5QtnVbW034_9R6Xqfj2uSNzsNXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=m7VitNqjBo712Q9NUqZQO7xH1CArjvp97X-dzD6X-JwOv8RtuUpLZtybqnmC96yMlnpNBNHsGDP5-_5lbpZPNJdl--Da-bPNlC2zI_Fbhi0S-KshM8nlAwwTDMdrzZgB4BH-VFm1wruxejc0W2fsRWo418ZohuTxvSb-FePsj02NIMURK73L2tT9grNij2mfQ4F2xO2tZccYh_S9b-UepM7vV95Oko4SberWiRPqxlvJJPADaxhDCUXfpk3DpEo4AZjoA2-EY_ph4Rca9hnSe6c01zGNVqIQhp0kILdHJPV6_jgMKBbUmT-tAnl5QtnVbW034_9R6Xqfj2uSNzsNXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=YTEhKylgi61zrfl5PZmq-AwoKZ3LRWv-FwACbdGA2JvS1KM0YtOBfRrQKLVeBBRnXFOC_558uE2c4r4YCajS-PbyqqqfhDZ6KAyY0CnnO2HD7o-zTmEhCArcZU3IMvw7wjfTWkBhRneOu0CvRbjkoRwQVi_rsjZESym_Rj76lP81OQCa6JF1Yk0QTIxXXT5SvT6ZZZC-otiwWTsdpe1hZEuZjxvKxlbT6AFFP5ZxBy8IFig5JoxnF4eDz15ZAzPjGA40-4BtXzQM2b6jw7Ahm8eYj6DO2IwwPxQ7g4Y8Z5Av7Mvjpj-G3TYR_cxkl4S-kMPJPoBhk7MWkeQ_IdZ6TQC_2AZZqTu8dqpsjQX0UUSTG1A5wMMelA_w10efFiEM2ti5xDI5FGfQbAMxVY5WjsIfZVWBmd_fSY-TGvy2lQAz6ypkG7YgX9TbU_gFdN81VK0oM6CuwXujr1LScUXkcsY5YWTe0QxRAFIsXBx1d8xbYmiy3nggXgXcz7lr8mYnhBfjH9GBOdkkMr8DUAtReS_i5LzX_gKZ24oItvf995j_s96az9Fqd_kpl4znbsalezgNOZ2sQoC68tmAVCwnnpAO_WW4oNMN2lrXBWRA038pTr2deAhfMz3HAIr3N-YKTMOUoZl9RcAuje1vGlRfg_oWcuFZClv8RkcX0A7V57A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=YTEhKylgi61zrfl5PZmq-AwoKZ3LRWv-FwACbdGA2JvS1KM0YtOBfRrQKLVeBBRnXFOC_558uE2c4r4YCajS-PbyqqqfhDZ6KAyY0CnnO2HD7o-zTmEhCArcZU3IMvw7wjfTWkBhRneOu0CvRbjkoRwQVi_rsjZESym_Rj76lP81OQCa6JF1Yk0QTIxXXT5SvT6ZZZC-otiwWTsdpe1hZEuZjxvKxlbT6AFFP5ZxBy8IFig5JoxnF4eDz15ZAzPjGA40-4BtXzQM2b6jw7Ahm8eYj6DO2IwwPxQ7g4Y8Z5Av7Mvjpj-G3TYR_cxkl4S-kMPJPoBhk7MWkeQ_IdZ6TQC_2AZZqTu8dqpsjQX0UUSTG1A5wMMelA_w10efFiEM2ti5xDI5FGfQbAMxVY5WjsIfZVWBmd_fSY-TGvy2lQAz6ypkG7YgX9TbU_gFdN81VK0oM6CuwXujr1LScUXkcsY5YWTe0QxRAFIsXBx1d8xbYmiy3nggXgXcz7lr8mYnhBfjH9GBOdkkMr8DUAtReS_i5LzX_gKZ24oItvf995j_s96az9Fqd_kpl4znbsalezgNOZ2sQoC68tmAVCwnnpAO_WW4oNMN2lrXBWRA038pTr2deAhfMz3HAIr3N-YKTMOUoZl9RcAuje1vGlRfg_oWcuFZClv8RkcX0A7V57A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCNmMo2NAFs11gxNjSuZqPGyTJaTQGWO_Zap180JPzO6NxJXFTKJtlT0seyvuxeRB5VHleo8pL109xEwwOu21Ql401qoRYPPhOyj_Xu7QT18S0-72kYcqFWt9PAyXz26wNq5aooRtrzJpTxbiMxZcUwDrgHawnieusAYjxIc2n_Gqf7ilmtTQNV85RSQMrYOOAN3hTfU_fxNc9L8QptwQT4tsdYlkXWKBOhYNNI3GyLpKKmJL6DOyRWDOI74561moVKvCN7JIpzBFomF8VY7KhSDGGWVjNe6uTbT_mrImZ8PwfC-PIneS9OLHaONo8Yd_umih9fTv4uT_ZiPZoezEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=paf-KsEEsOfGK0NTuXTgy2bnEQ2wHWfct0bFXam05nBXBNDDI3Jnd3ZYQuL0jSWziWms2lTYlQKHUgtxf0pxBi_MfmwZ4eWvBLnmt4whJEFnF0BexHdApJWFYDAtU2pq1sGM1KubvGbbqCY06vGBsspWRB7-IQy1fSTMwYPCuaR92x30VVjD7u_VrCAFIJHln5JPTY0e3_52V89yuAwVfH6Xa88c6VsIiQXV_S-xZqJS08oXMzfgbEbN0Nq_VzaL0vyR3gBUU_YGVwOPGcN5d4wE-G5M990aLQIF1o1xg-1OLrb-xrNcICsC2kGM1R_wJO0v7fZmoa-J4u1i5hw5Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=paf-KsEEsOfGK0NTuXTgy2bnEQ2wHWfct0bFXam05nBXBNDDI3Jnd3ZYQuL0jSWziWms2lTYlQKHUgtxf0pxBi_MfmwZ4eWvBLnmt4whJEFnF0BexHdApJWFYDAtU2pq1sGM1KubvGbbqCY06vGBsspWRB7-IQy1fSTMwYPCuaR92x30VVjD7u_VrCAFIJHln5JPTY0e3_52V89yuAwVfH6Xa88c6VsIiQXV_S-xZqJS08oXMzfgbEbN0Nq_VzaL0vyR3gBUU_YGVwOPGcN5d4wE-G5M990aLQIF1o1xg-1OLrb-xrNcICsC2kGM1R_wJO0v7fZmoa-J4u1i5hw5Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByKFsJ6Q-fA7hXFjU7Pl1pYC76xlG-Gx6DrkMt0Jbh-agmNetaK29RUqZ74I1nt0IDgNPRpcVnR5o__3kq5YS2TBjevLyexPDTqQhDxjargNIwZEqlbg2zRxdCf4EWaC5OMoYDoIBhxyJed2SC9cTZmETJCmJVtFy8ofRN9Oo9aCglsEgNkdGhA7NCjQzh8X17cebgv-lsJzYHkferD1NVt8u6MIta2h9c7WUxVTaIfPeoJFsnODd7MbL708Hd-TCEzFGOQ4aIHvHdHgZtV2sSS8gml57SrtWXFza4bszGlt2DdlGj9oKAEKEXoW-L1JS0g1z2A9BCokKqYyYBxcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KX2wkNnsNTY_AYHFV-s0LnJo6VUmsv94s0i_YZ0UY8pV2_yoSts6uorHHh6GA9yIryhOCdOhVP4h032io6MwB0FdvqgxgdimwTPrZJ2szTLy-QHr-e0_-OMk_L0bCc_j377gokwkhkWezX8mBFsXtgQvODpVQilNu_7pLlg9E9RrZQBYrOTgUYUXXChtXjkWbyc-o6mLQejMSFq2O2nrm3yWtOIuuUJPvMWTtscYDMLjBIMxxP5-7hz7M4_3VEP1mCjxllov5AblNmgm9U1jmcp7hhhewAgRCCvXo9cdl6onG-Bt7hdpN6WqvOuE0e6Ms5vnQmLRpmMvYpLCcSK6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJKxgxibXg70LARwbarUj0dDgiAs7rwg-F9J2h5bkV4-lXItYYiQdnR__VdCvcP1Y0jtOz4dZfIsOQgVdFCqmJ09V5yuKc2AzdF8DrSTvtHDIZzG7YwKczNrMwTxRrqWNDy6EWlb7sYe3MXnvbaHDQC2oiUBXDlkG5FQLstAaNo__4oG4t4Sly4dS761OXzYDTrbDe6zveJiZcRBnfsjwz1fy53f8vWsrbCFgIlVTyJBMAhKwR0iFJnvgUdKaG64E1KqMgqvDBHhNdBIUfGI0Bs_SLGeptouY3M7i4XMPhOdP4bHl3LBD3julC8pS2GLHmXCwuFUo8UOvyj-jeKQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBvPdB1WKReOtidITfRMYxY0rRSbhXauVLKTrmTjKlY3sLSjqHzeeF3Hnjg1t7W5wEqXAsDyDpezPDkmnIow4StuJLBhd1hBFdf5rkfy7CwRsephZnEGkduNWGXx4UDtnMd1vGHQhqJIzfKxcYjnM9Nb0ewoMl6G4IsgVO2Qo0uO6oGtGIs6e79y_F9OaicnNMLpF6w4ESRoOF3geSVi-_R05y3DX_UX8Cn2ufFGNLE7pJEArnKzsfRKM7lhXpsD8tIj-IJsOHR3NIAe2AxuSFE4GY_PAhASNhUme_Dzcz4lvBe3gwo6GjNXMI5Mb3npGOFtbayGSfGRX2LTFUFBIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHCO1Yw4pf2TfM_c93Of5akgJu3KJfxMW7Au7mBnZiyD775DszbCl6Dj8HOfeB_D8_c2N3QlKgwxScW_O0lbvF-zA86UfZPHUdWJc9eETXOteC7_RDEdv1BtSsecvBLMoVWMgzsG9EQNdxdd4x1kiil9rNrDvD4au2biOWkQ1M-KDDcRBfYoal0CWoXRhgfugLySPDu3gSB7N3C0WzF6nVfwLzHQiaoEZnFd2HjMhiUB8VUdoVAEJGs6LlZzSfHbu0VVEACI9kHqxOB8LQwwYx9mzkVhAMXZlOftyx_4pVpl7gdLcpWh6FJiROfsWJs6pB2xAe-yv5cJDrzoeN3DCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYJJjixXXr8PTHXGOV76i9r1bjMxeA1Lmdc5MJepnvrSJAv8wXHi_Sfl5-wzHzyk-k-l44yVoGWcQJK6aGPkkbBKssI61w42ufWO2Bt2ph2iofNOlCSI3YVhHCjc9FZJSh2hou2mwSCRqd9kQjgfPqvsG1qiC1FDjo2LgL13A0NV8B4wItRHEOQ5YcUcS36XtnUJmqRLsto1m3PyHof3GNELaC3_xs7oe4A5sM6j7qLg_3C9D34bHsjjFDoJPL0CRPAUSbrZ-fIlkP0L8QV8qk3AIvNo6ykYrEQbwEwB-g2hiogznkLCfdi7lQMMu0JN2QnIPzGR79czY4MEDSDnFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=Ps4tU-gy9A4yPA7QPqH_YByd8fOzJ07LI0v9WU_XhZVNcrC-IcyVIgEPPve1vWMO7GUa24yRDcbLg87xZzheo3RgJBmLoepDsFYpx403DuvdTioGd7j2ediAik6WTUKstFqRhXaM8RxQYgBQA3HbQAR0x4S7JUpDSQa0ON6tWqtsaFmNs_0Z7cVOZnbI36whhK_gKJ_Tv2zS6mcOTle58PQn-EiNYXNvKc8htRHXR0xFCXnw07CF4I2qVdFg_Kzv_X8UaOX3aVZ4PQTnxJj9qwMsU7N21D--QvzJLHh5RPFCLmfQLjX174OaPdnzVa7EBiBQdMpE0z1T_FP8QdnzwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=Ps4tU-gy9A4yPA7QPqH_YByd8fOzJ07LI0v9WU_XhZVNcrC-IcyVIgEPPve1vWMO7GUa24yRDcbLg87xZzheo3RgJBmLoepDsFYpx403DuvdTioGd7j2ediAik6WTUKstFqRhXaM8RxQYgBQA3HbQAR0x4S7JUpDSQa0ON6tWqtsaFmNs_0Z7cVOZnbI36whhK_gKJ_Tv2zS6mcOTle58PQn-EiNYXNvKc8htRHXR0xFCXnw07CF4I2qVdFg_Kzv_X8UaOX3aVZ4PQTnxJj9qwMsU7N21D--QvzJLHh5RPFCLmfQLjX174OaPdnzVa7EBiBQdMpE0z1T_FP8QdnzwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=ro0g4LT9KJGtJyqu-orYab2UlfFKlFXUrqIpRJP4hipJpWc2OJ48q0l4F9TyzOqm8dX2dTCl5FC2d4g9DTjrM2dQyL9LSyEG-TuhgYS7yXhP4pYGpQWefx4gLwsfSrahAzEuSfLVW2K_M4Z7P1vU3WL114MqtY_G-UuEwqZ05Dtk79C0wIyH54eQxArJH9tMrPwM2kbQPh6m8z7s1PQz26SHaHHFYPN4Vm3EEt11KUVJrrETcZX4zQIR1ROjJDT38i_FQGxIiipzaakc2quhbfA858GitIeQLW_LSZMitrkEborHsnJxk7THsLP84VE6BS3CSZG4_3xfrCbC5DZNbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=ro0g4LT9KJGtJyqu-orYab2UlfFKlFXUrqIpRJP4hipJpWc2OJ48q0l4F9TyzOqm8dX2dTCl5FC2d4g9DTjrM2dQyL9LSyEG-TuhgYS7yXhP4pYGpQWefx4gLwsfSrahAzEuSfLVW2K_M4Z7P1vU3WL114MqtY_G-UuEwqZ05Dtk79C0wIyH54eQxArJH9tMrPwM2kbQPh6m8z7s1PQz26SHaHHFYPN4Vm3EEt11KUVJrrETcZX4zQIR1ROjJDT38i_FQGxIiipzaakc2quhbfA858GitIeQLW_LSZMitrkEborHsnJxk7THsLP84VE6BS3CSZG4_3xfrCbC5DZNbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=v2q490e8LyXu6Ae210RtXxrjujX_eOnRJf8ANlYpyOFULTtetNCLSxFakUw7AHDwIQepPOcJk2SPOZxO256vz5_Wg26W-0ogsWGbiP5CClNSb0ruA3CW5zHdgxa_j22fc71tzjMQWY1WKOr6W9VWZDoiqq8HupJT8JergqtPIJMFwVtM4zLTOMFg2R1HxwoQG0neTjgUtWvzLBkrJS2wqO-bXF-_UoP2GjYawl5oONcMkB9Epa16uPjazUstfGGIp7dlRzfg9VhLIhr_KWmC4yw0ampUcM8Xq2hZuwjGfGZXJ7EVIF9_Qpe_g4f4bT6zDTlyNM_ZAJkvt5AJGG5PcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=v2q490e8LyXu6Ae210RtXxrjujX_eOnRJf8ANlYpyOFULTtetNCLSxFakUw7AHDwIQepPOcJk2SPOZxO256vz5_Wg26W-0ogsWGbiP5CClNSb0ruA3CW5zHdgxa_j22fc71tzjMQWY1WKOr6W9VWZDoiqq8HupJT8JergqtPIJMFwVtM4zLTOMFg2R1HxwoQG0neTjgUtWvzLBkrJS2wqO-bXF-_UoP2GjYawl5oONcMkB9Epa16uPjazUstfGGIp7dlRzfg9VhLIhr_KWmC4yw0ampUcM8Xq2hZuwjGfGZXJ7EVIF9_Qpe_g4f4bT6zDTlyNM_ZAJkvt5AJGG5PcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=T7LDc70A15tZWGYifr017twJsqopeTSoZe9_p0G_eWJV02C-PPKQ-G89btzM2iZSPKCe8sl8F5DpFpsynTD8YdwcQaIAizb46wIRrWAm6xAYLjLJzgsoqNae2jFKhJ7pgwxpqTk0hYArQO3gCkE62MJ4yh8RYpDJOFhssw8R4NkhZ1yV8q82IZua07a9PNIpXfYoUeutQkHxbEUaKsxrTcbfzDlV9JKs-rjpz8pAWzgMNi9pAqmJa8l8XuOhcrYmKdL6PIHKMoAUg1Ek8_ve333dwqEBXlcyV03nWMS41G2NijfWrH2DT7cvw2oQS0-_soQqui-94vEIuqg3Mzh9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=T7LDc70A15tZWGYifr017twJsqopeTSoZe9_p0G_eWJV02C-PPKQ-G89btzM2iZSPKCe8sl8F5DpFpsynTD8YdwcQaIAizb46wIRrWAm6xAYLjLJzgsoqNae2jFKhJ7pgwxpqTk0hYArQO3gCkE62MJ4yh8RYpDJOFhssw8R4NkhZ1yV8q82IZua07a9PNIpXfYoUeutQkHxbEUaKsxrTcbfzDlV9JKs-rjpz8pAWzgMNi9pAqmJa8l8XuOhcrYmKdL6PIHKMoAUg1Ek8_ve333dwqEBXlcyV03nWMS41G2NijfWrH2DT7cvw2oQS0-_soQqui-94vEIuqg3Mzh9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=nVGfL3W8S6mgGQgXtI089J45Z42OvHyPoIXZM8EGUmXLo1JhVRqH10XtEUSdYou9iyaC5y5ivEHT18iri0cSUqSyEAQxQGK0PO21JCd3VfQ-N7mSAwCZqzsYiQWbrqBo4v2KXDT4r4l2QhALzWzzQd4mLv1HK_BMOqQZb8TSzlKUH4rwAA6i4I4jnrNL-WcZRWV599pE1xJ9yUlBaXqaF4nI-EMzA0ebGM-cv48_qwaqUg38Bzew1Bo36HY81Mf8Pf-OT1AdAizwwcK6EmxzJUR7o7JMC_d8bar_ieG1CjoIT8Kec6NjZ19QQpDsSLSZg5GNxhOJOCvsPiA_uP4qHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=nVGfL3W8S6mgGQgXtI089J45Z42OvHyPoIXZM8EGUmXLo1JhVRqH10XtEUSdYou9iyaC5y5ivEHT18iri0cSUqSyEAQxQGK0PO21JCd3VfQ-N7mSAwCZqzsYiQWbrqBo4v2KXDT4r4l2QhALzWzzQd4mLv1HK_BMOqQZb8TSzlKUH4rwAA6i4I4jnrNL-WcZRWV599pE1xJ9yUlBaXqaF4nI-EMzA0ebGM-cv48_qwaqUg38Bzew1Bo36HY81Mf8Pf-OT1AdAizwwcK6EmxzJUR7o7JMC_d8bar_ieG1CjoIT8Kec6NjZ19QQpDsSLSZg5GNxhOJOCvsPiA_uP4qHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=EGEHXv4DmZ5yA2EMRe6lSnW5Ca9qpSu9M0-bAMUeBUknVM0zCUR_JTf3p86Fk53U5kMQ8LOQD5jX3nF1QpaZlZhdAwo7qcdRJ89ebtufzpOg74lG92Ttgj8Erd1YLRBOKsACX7vTXQxOLON0nOH7t0SvElFuOiO0lArQXxZdPFLFUafEonNkk2D39Zz9V5U6dIe-wcBp86HulE0NRTUWt5CGRXinoahvbLCf4WzyHtSLNB6cKmdHxm9XXoOvixTk9Qs2xCm1XCoeWawH3jQ5elS19sf_sk7hDOHXIWsbf6fKJ83H4qdB8BJntS0hh8LsmUcbZtv_rHcSlzbkxwVDmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=EGEHXv4DmZ5yA2EMRe6lSnW5Ca9qpSu9M0-bAMUeBUknVM0zCUR_JTf3p86Fk53U5kMQ8LOQD5jX3nF1QpaZlZhdAwo7qcdRJ89ebtufzpOg74lG92Ttgj8Erd1YLRBOKsACX7vTXQxOLON0nOH7t0SvElFuOiO0lArQXxZdPFLFUafEonNkk2D39Zz9V5U6dIe-wcBp86HulE0NRTUWt5CGRXinoahvbLCf4WzyHtSLNB6cKmdHxm9XXoOvixTk9Qs2xCm1XCoeWawH3jQ5elS19sf_sk7hDOHXIWsbf6fKJ83H4qdB8BJntS0hh8LsmUcbZtv_rHcSlzbkxwVDmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuVWIKAeRjdcR3_fF3UVOnbGRVcYZ5l35yp4mKFfxrLEWQIc_vn3MqDVcc17N9Rpk4djonWunRlOOtvi-m3HA4BQ3Hb5NbwRVIBVQzy4Fgf-y8-vQA-7Z0ZGD8NpYutQWWRblJrodjVvHdJSEkbgA3JOy3RUk1QoYJZ5z5NkSr0PgEiQVGMbxXFm-FADmM4k7bRaL0oYyDo-wc-Om3R4i6fyfagWqYPCACCLHd-_VxB8RGL0RqQEf7XkcpRR9AiHMaTnKa0Utv4GRS9wAdc975MfdxXC6g4CfWdHfzR3XA-gZCGlUDYls8r2xdDHmZNxnkt7L4Te4t_3V0NHLLQfuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4yDeJgxBCC97CibQzERQcN3xtEkIPX_tWdw49L3yK9Mozl18OYu3_HnP3id1iSqmSZ5Oeuid6k8htsXVcNvwSh-Bz7NjbYaS_VrFQjIgzT3gp7e5KRz8Dm0MGloQ73sm1IImKALAzsnmeJig7427N5e3YEiltXYx5Dj2IeAqE6-cKBJ5EgkPIfmdLBrby58lTLAHYadOqu0N1kYmKZrLPSvqxb9YkOJampAPYR3kPJ03dPnJgypUq6H_CyISjrOZEMk5SBUwzL7dX9Pc1vYkBfp-nV4ji3gTw5d7gNbLbW7q3jRyZWDBvBkHHxYrUApp7-pDylEZhc_GwqkBdBJxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4FfO3SbfyMKLoKXzJtg9d32enakc4TklqSi4o8fJ-G6P1ZdN6AbyyPcOPZj2Ca90AcdmeK8HhUrbYTaenW1tmQsd8Kgc-7oTL14nwKC5za3SwSJOqYZ7uZoGgMGBOMp3e96SNbHkW4PY971lY72Uaa02FxTRKQXGQZd0qA4TTxfaWmgIFC9XF1p9bGasYm4bvZiSBAaNiISzoOd30WVtzoR5uKwuoY3nPGK8-_0zlJ7w8diT8F2qZR5zDi-mQ-73VxDh5kepOCdb1w78SjvvM4MyUrlNaJVvJlS9H4QL2rG34N3_0s1qpS8fU5HHcYJbVWa5Jt4PNkHWMdaNCVzdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=r7MYpnNCdckMtC1u9XG2_Up_WY-qyYPWjtUMgkKgYe89H3QCl834qoexs3deYzfMrQFhKkRz0xa_3QMqh4DliWG1Abp-pDYOTqZMUMaXthL0aaFWXCzDGJqtLxqcehK2eVzOYnMN-JqnFQZoJsmptnnAf5g-C8jrFnHM5e6589yAeGnM4GpwhT_09GqeDd5tERFe0OwmV61fObUp8w3_H-pAitg61YGPjRxX39xl8SYC0nKegPGpMc7rbUOM8ccZJplOxlowFaypkPzK9aqHekdG6siuLCcTaTq-lr6fQEgN17TWEMS9JAEzI7DakyHUomqrtjfxO5_O8vXXRj-82g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=r7MYpnNCdckMtC1u9XG2_Up_WY-qyYPWjtUMgkKgYe89H3QCl834qoexs3deYzfMrQFhKkRz0xa_3QMqh4DliWG1Abp-pDYOTqZMUMaXthL0aaFWXCzDGJqtLxqcehK2eVzOYnMN-JqnFQZoJsmptnnAf5g-C8jrFnHM5e6589yAeGnM4GpwhT_09GqeDd5tERFe0OwmV61fObUp8w3_H-pAitg61YGPjRxX39xl8SYC0nKegPGpMc7rbUOM8ccZJplOxlowFaypkPzK9aqHekdG6siuLCcTaTq-lr6fQEgN17TWEMS9JAEzI7DakyHUomqrtjfxO5_O8vXXRj-82g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f24zlKvi14h6kLhmxEJ1HbkyYjO2SvMPEqa2NOvQXBFW5WStzAj_OE6jH2eFUjGDV5wO99P73H-GSRODZtOJzioVjZ2O5u3IbsuE4RX2fZbHhTe0kF1LXKHhw4MyOMZvWJszsO8ASy8OymuBjT2lAPAZ3nASjMdfdvzqZb3iI7B8Jb6qL4m9GLFTE_H7WkUg1O2DkHqyTtuyqezQawNOf2fCSVVTNUi16Lg6AbvW_cvdiffPe8aXZRYLFm90VJhgbATzN_uKy5l9roWkxZY74V9TttyF6fmMQhAkqaWqE-hUOg4JP2-t6LkUbSW-LXHLyk965MnzQESo3c2_JHzetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVxV1xwjfKIbJR7XQr4eQcL_VNIEHBsG06aF9KIWC0Hz76x41cHrWy9gwLAPNt5_cGo4DaZnK3gitH_rDcywpK-HjZ8P8ebPXNfZESo5lWBYmSVuOl4JJwHBITNw77RMCjA8LX9PJonL4QW6RBZRxp8fMTXrh-M1qNDXcso7NHj--gPCUJT5s9yUZ73kjt03Gf7Cs7l0ll6exz6fZup1cZhG1-kly2Bv4zZq0opPd8ZGOI2Fc_JF1_58Qw6FMp0hOO556wXaBQ-HYiRPmBjmjFDMDayAxhGL04qxUmjAh77m5ydujrFgDOqmPg53tI0FK8oLEkA081mlo1F-y1uMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=ZaE92mN9jB2Zc08gjb0pzrFA0cw0P3uqtCSVV-Ib6bn3kqieLRtd1X_yE9nDxZWnh7sEYZtcjQvxTkeFUvF5J6IqBlLjm8WzHiWNoTd8KbdLV8TmA0JNy-evwKlBI10bPYMIqc24v7305NUysm0g5xcrGzYGhMvkh0hHZomHJDFruuwbxTQrVTHIqO_vHRCEOXZPgNq_sUIif8Ame4aWwvBuH8m7I94Y6ga3LfWBG5WlsG_QRy9xjh4aLeB5X0qwKqZ-nrJ2JvY5rnuFHF5jUPzhwoEjwfsHqHlEtzGgQhIazBEgmcchm9dRP46H54mNGQu3uVbGKtpY7j0aXY9fhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=ZaE92mN9jB2Zc08gjb0pzrFA0cw0P3uqtCSVV-Ib6bn3kqieLRtd1X_yE9nDxZWnh7sEYZtcjQvxTkeFUvF5J6IqBlLjm8WzHiWNoTd8KbdLV8TmA0JNy-evwKlBI10bPYMIqc24v7305NUysm0g5xcrGzYGhMvkh0hHZomHJDFruuwbxTQrVTHIqO_vHRCEOXZPgNq_sUIif8Ame4aWwvBuH8m7I94Y6ga3LfWBG5WlsG_QRy9xjh4aLeB5X0qwKqZ-nrJ2JvY5rnuFHF5jUPzhwoEjwfsHqHlEtzGgQhIazBEgmcchm9dRP46H54mNGQu3uVbGKtpY7j0aXY9fhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr8bCDZ13l2_wf0OzD6069-K0MSMDKCu912K0D76-nA_qMLfN5DiHXs5YViz1RA6KKpHVCzYSTAHiYMA40jj0Hq4-8TX9YhwwHz7Z8s5I8gtOaLrGl7wOupn-9EbyCOETYaIAWWbU3LRXzcDqX6HaPvlDY9rWuaw6MluxjpBP6-HlwmzE5s4ZuxP4s02LfZUgeIlYGS2kBEvEI3Vuabwc_KPwpM7WiMmmog-noXAz55kSWMi88yYI_CEetc4n6z3eEhzdzYBkNzdVyIdj3ddeENo30tV_7tBKaZRKXoXsTGUCpA6bJDHr2ct-Drhcfbup_75m12iphwpDAvf7MymrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LM5Srjxz_swrDsN_-IAUmekFD2QxrZJ_5uBVXbpupcACkwfGAaA5KnrC3gIgoFqjDSnBPfvwdY24GJ3u2tkdkdTS6HBnkdseUYjfa_iDipOOnH-lX5WfVWIjbwtZR9B_J2vWYSYGqhPFpL9iqHpPKx09wVNMZF6MSqlCMa-jI9rwbq8CBh3pPoHsdlqxMYrExs8NrdLgrOmS4PaBiUaBz9pqJkIQt3B6O8o5qMebjy72Q9rcdqMBxbm4TzBvKwI1085PLGxFTgFUE3mZZC0BNzhYNiBvjRHSrX5ZN2CanJEoMnEFYk0f0GLGMZxFiS_m5h7L-JZImRtSqH951icY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qElkS6e4MWYihDtUF2EKn2mRNEXN7xpH3wvVbvZWZAIRiKCJI_Yr6yhlHNaVS60Q5SUubl1m1yubTiWkGWT89c4gHTyWSvEVVdv2cAp1oVhxEAosQodmWptGoHInqH-XjhFzlPTpuK-tEQXETu_qpcBEXP3GRRiAve6I4OhzEABvQSCrUduYtTr4MdutJ-TGotQog-4Ha7WXshHbylyLvR07cE1uxzua8CwORfhRUWXVxLpk8ptiVSMTAP3vxP3fL2lR1Vhd2JF-j1EffqG3xJEG18TqGwtHZi_OJ5awBcEr8CljVcGZIb5tSQcUmpQbA9iv_j6bsZhIP2zKUrOezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgqKao_zbC73jHIgtmaQC_JsyU9Xu6gqUz17xY1IXlvLKSku6zxEPCDaeqVocksFYU_9YpcwT82jZBRWbi-zUk9gQAkG57Dsl3N2ZqztEFeKlR1xD9CEBscNm685f0f9k84V0Lv3GgCk7e9q85zQTkGKBpMcXtzCIXC1DIQAVHz8jTPNwu8iwxKvsMpazeSYGLJV7ncBwiwuouiBTrXqDUT2ro7EyEVfRU7_2rfIXYW8umWv7TW_VaoGcXbg4jP-7ibV-0FcN3HNbMDBkWJnmU0KsUqpPyq2JJSOaExh9t1fbh9iqVm3bRmpIb6WDI2cpsLHu5LtlluQeNr4hCUlSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=AVRdfK5MI8zWk7Rr-NfMHaFceeqqQW_k8DnsUWb7QkMvXW9IpBrcssf9Bi3o9Vvx2y0AeT8aKU3jDnIT3powxUFLBkMiA3GR2i8U4E8XYxcsfj_wLMHkEF_Cz1RMUYhX_R8MzppGX70r2cGvEbG4XNx0o2UHMAPvIaWcC5NZeOcj2jf2BZGQPoG5ZPp7uO8G5fTMy2WmBI9A-00u8rC594Mm5Pp5jIBak6p2YADqJpiGjmqVBmQw7sv977dVRvpcVTT_Jf0xLixTDpKgZG1SX-EZpDGUK3AFdM_FZn7olajWNJ1cZ9YxpwMnGVqebsNcwKBoSxKJiZzHxgO8iC2OlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=AVRdfK5MI8zWk7Rr-NfMHaFceeqqQW_k8DnsUWb7QkMvXW9IpBrcssf9Bi3o9Vvx2y0AeT8aKU3jDnIT3powxUFLBkMiA3GR2i8U4E8XYxcsfj_wLMHkEF_Cz1RMUYhX_R8MzppGX70r2cGvEbG4XNx0o2UHMAPvIaWcC5NZeOcj2jf2BZGQPoG5ZPp7uO8G5fTMy2WmBI9A-00u8rC594Mm5Pp5jIBak6p2YADqJpiGjmqVBmQw7sv977dVRvpcVTT_Jf0xLixTDpKgZG1SX-EZpDGUK3AFdM_FZn7olajWNJ1cZ9YxpwMnGVqebsNcwKBoSxKJiZzHxgO8iC2OlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=IFn0BWKZGHx5bfsdv4otlrCikKw6BUnlJTvQwG4dp62AWVEZgGpCW_QvKKv3FHaErwwN5Wt0VAoN1xTflzqqhVsepB7OKvt1DoyYhT788bzLvS_LD24oLxDblo9YP7PGw8zO6mfg6lieDb9tf1_KQadZYb9-QH0m-UqhudfYGhZ3xqq5jsA7rFTsEF6-n9KrtSlaS_2xF17kbSb4ReTeIHLQhzZE15_Dr_BEF_q3LyZVXCftmRdQCVEwST9MQYFavKA-mTsePC3ndSXIALfSa0XsBzAqOtHf2bKzEQEnIH4G9UQcwnXqd-lvqDDIjRcUfAcy79AsXZkbuVGc8E528Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=IFn0BWKZGHx5bfsdv4otlrCikKw6BUnlJTvQwG4dp62AWVEZgGpCW_QvKKv3FHaErwwN5Wt0VAoN1xTflzqqhVsepB7OKvt1DoyYhT788bzLvS_LD24oLxDblo9YP7PGw8zO6mfg6lieDb9tf1_KQadZYb9-QH0m-UqhudfYGhZ3xqq5jsA7rFTsEF6-n9KrtSlaS_2xF17kbSb4ReTeIHLQhzZE15_Dr_BEF_q3LyZVXCftmRdQCVEwST9MQYFavKA-mTsePC3ndSXIALfSa0XsBzAqOtHf2bKzEQEnIH4G9UQcwnXqd-lvqDDIjRcUfAcy79AsXZkbuVGc8E528Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmiKOxOsmdNVae80e-CR7EFuPnRl7Bxd-DohZgO6clZdbU-zMquqMJKwHYTuA_uKUu1dDRZCVg64kath1HnjYVl40rZ2jxXGL8GRuBTKZ5bF8MRfgh1zc_CGHKfbVIjsNzOtjoSetxex2RbNN81axke_cHKUJQdfTt7PFyxjTS8fZ_JtHjI_rVn2W0cQUX3hIL6dulGpgJKpyfR46Qrs_ISs3mVKZN8PSNRT24x10n6UdSSoHXuejZYoGHboXcir-vRNUxdXU2nWKkgRtqOBIwiG4YvSTEURBvvWYb6PxZtFN9v4-plKZFfl11_tTLc_0P9hLBszluj7fXKOHtTusQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=QEfw7bHtthhkiIs9q4tTLx5pN8QV8tREqVaETdHFDxXzbef3UiXJdNKzIXje_uMsLtcCLI-jStrCnHRX3QvaoRxjejuoeOV2mgNhMnE34-11lfkYP8ErKbVvn5fnWQbYA_ekPALOvfJ4EOdfJUQNwyIZYSyjkAbsbPeeLVQ_2Oz4qXrUEWkZG1RDF2kfocTVTu4ozwIMvVwS_Z8LrM-sIWJBs_n7IdDlpPzMYMxgWAnEj-Fahcl9IaEmOHT9i7pC1aIIWPG5rQAAJLER2_ZJLCNrZGQB6tg5GKpb7wK9CTf0Bt9Ht0Ll2nHF4a7aKiTUvgUyAj9oFCRASbZHry8eWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=QEfw7bHtthhkiIs9q4tTLx5pN8QV8tREqVaETdHFDxXzbef3UiXJdNKzIXje_uMsLtcCLI-jStrCnHRX3QvaoRxjejuoeOV2mgNhMnE34-11lfkYP8ErKbVvn5fnWQbYA_ekPALOvfJ4EOdfJUQNwyIZYSyjkAbsbPeeLVQ_2Oz4qXrUEWkZG1RDF2kfocTVTu4ozwIMvVwS_Z8LrM-sIWJBs_n7IdDlpPzMYMxgWAnEj-Fahcl9IaEmOHT9i7pC1aIIWPG5rQAAJLER2_ZJLCNrZGQB6tg5GKpb7wK9CTf0Bt9Ht0Ll2nHF4a7aKiTUvgUyAj9oFCRASbZHry8eWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=UfkGrG25CM8Ig6V4sb6tKodvUYx2L5w2OgyLYzyw_I1gxv-TK4arR8Yo3ElU3RkvtYJNjrtuxXqWrSk0VcfwTSrzyT54oOxsZO4LaI2riL64i_5NwXwCk0nwH49J9LaCQyt-9QxH67LbGonqlldY34WWwHb6doJu5Aoci2qeB4j7PkE0_LuIdgkjtroiDxqu8nIQp-snq-jIQryIlDyNqKYSE_TD4Ox4kgvrMkXLepJxEG8q3mTyq_UZ6y6q6qiT1p5LDFV3-iuSoZ4aaoWlPqbc5Z-eR4kz47cgU7mDThHHusI_7mtbN02XY9mj6g4Nk_zxo5T-ZSN5crOwrn6IDy4K8an_Lnav_1Bpx55R2sbgGBzsSv2fal8vcsIR60mxG2GC9kLoPOJITn73GeeVSxewPseHUTZWia64guOzLpHvS6ge72Jyr5bv6CnSJa5rtSYhG7OLC79QlqgqpI6DbDsLowaT3ai2Din6IsUmHnLeKr4xkGLx5LdlLVUyPs8g-5raCz8vNjpuPrRZ2lwW1j8KvW7Dj9LH5D17l8q7bDS0xvgE5ZGIS0vM6XLH6yNoXlSeSstLBr7sE_eQKPJJ74n237Hn7uCkkZFblS8jTbr4ZnL9g5hrizUUIgGpVlF7nUAgqFjSoI-oE3RKBlSx93pFCeE96-qaj0xOtiOapjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=UfkGrG25CM8Ig6V4sb6tKodvUYx2L5w2OgyLYzyw_I1gxv-TK4arR8Yo3ElU3RkvtYJNjrtuxXqWrSk0VcfwTSrzyT54oOxsZO4LaI2riL64i_5NwXwCk0nwH49J9LaCQyt-9QxH67LbGonqlldY34WWwHb6doJu5Aoci2qeB4j7PkE0_LuIdgkjtroiDxqu8nIQp-snq-jIQryIlDyNqKYSE_TD4Ox4kgvrMkXLepJxEG8q3mTyq_UZ6y6q6qiT1p5LDFV3-iuSoZ4aaoWlPqbc5Z-eR4kz47cgU7mDThHHusI_7mtbN02XY9mj6g4Nk_zxo5T-ZSN5crOwrn6IDy4K8an_Lnav_1Bpx55R2sbgGBzsSv2fal8vcsIR60mxG2GC9kLoPOJITn73GeeVSxewPseHUTZWia64guOzLpHvS6ge72Jyr5bv6CnSJa5rtSYhG7OLC79QlqgqpI6DbDsLowaT3ai2Din6IsUmHnLeKr4xkGLx5LdlLVUyPs8g-5raCz8vNjpuPrRZ2lwW1j8KvW7Dj9LH5D17l8q7bDS0xvgE5ZGIS0vM6XLH6yNoXlSeSstLBr7sE_eQKPJJ74n237Hn7uCkkZFblS8jTbr4ZnL9g5hrizUUIgGpVlF7nUAgqFjSoI-oE3RKBlSx93pFCeE96-qaj0xOtiOapjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRJ2jjI7SnoE2zuZs0V9K4Vm3NTIoO6VFaVLwITlxRhCjYa6uPyAW7YbD1QRM8wnOWQ67nXF8Lv3y9OdVDTg4QsFoeiU3l2-5V4F3CF9I4rhsjm9T8eUH5On1-hjzDt0fpN5QiFMfLr4LKuhChliLoq9I7NabF_bv7LdYATiTxKqsLGIUZ6wK1e6YxmtP5wmxZ-8uHkMHSGGj0q9WrK2PRrtE8BMeeKTNeioYQ59OPoCgKj5Bic0wYxHFFDwsDoYscmBXBt2bpvpawniWDwKuVg_7i9f1lTVq8eaxwTs_iFtQp0zcQCYakiN69EmenMex-v3-2DI4Ng74iaiBzCJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ3B8mgMXtGvBxELl13RQxtG-fDzWxwBtU-2N86wZDQ63b3qinVvHWw5gafVF6_fOoAjEhJlbsFMBkRIqonhrbkZq5_hrbySc8qoPrg80Bwp9d7shWa79sWpoVHUvEhPovVHsQJfin4FWrH6s__gye2ZXAHiz65HCwN3QzW4vqO3HOqdslRQ_51odEn20PCKkCs7dH93bXoy7wHZ6wCoKTlo77gCuvoC4020yJTvOEz-unxFDw1Xe6FXy21dyiPV-YNUau-iIl5IJsznMzfA8XabOcOzJxmtPTEyTpcBt5YgDpEqUjOEi3Yt8va8VPz1s7HUAe-8084lXmGokFS8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wg7uKykdBbOyywAagTbRW5Pdv9CpuC4minGvAzFU1Otf0anF2s4CQZZdje1-zMTZy_IPZ7XGAiP-62Q-AVlbyiebwZ1KKsT0hNZ5oV7z1lHRN8-PoBKB6xCxAd6_7yWYPSUr7LXZuFpBN6cL_fpVeEu4a_fXjloN2DttmJSonQKkMVEAhBmvcSjNer7m5sN7Yg-xGIpjC-sSxMr4-mQvUigNgsRLdW1y-xM0VF7blsquqAfz0ATTbKjgIkkOs93KqGRvBtxv6VyTbUJKbRoL_BJKbrkW3GzG4Nhs3YpIzjrp4_QqXnoCWuMGqb3_ZSpPkp2ggqssM8Lmc6ddAnW1Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mT9UH0N5IzqMIwUl8CGkW3Y0NneBze2mUbrL33qJ_jtk_Cmu5Yg63wuqw43Qh3BzPUH28lb8FvkIHED3X-QA1gxHTuMNzkTyqGUOpZBVqb9xSqen8vUUmpLcBEPF6A2W452hCmoRaKJHgjIMMpSLtWI9oCbRcdIa1mttofycOJ5xvcdyZvn1zG4iCN7b5OwjnM2yQxuJmCDZUMnKF9QmgfTHKro22IE5ZNeONBW0szowThbqc_GRm3Rg_eVV-lVLIF_5IfayS-0J6wItYmoN4T23zCUbh05HmCstDivWZpervd4DOc4865RsOMwtd4WWSVofert327wPFIq47qO7dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=u2i179Es6239cltiorFcqr3i3HlDxxeZ-fot6YBY6jjLTYeyZ1aCUkJrv9ZVBczkww1LpDpqlWGDjl-BSB1IPuxyscb2ntuzcdKci0ur5h37AnZg1IytGOfUYZrFvqxhfOz7VZUrLalE9oDXXC-Z5nfaICjuMe_R_qkkOtFQTxmoM9YvFuDRwrac-QKTEdF6pNHBDAMZNZsbIFfWWtKZlnRoJIU1tI3uB0p1cYc8tn7Wft6Rh_yyNt6Gkkvutotq4VAUPOnKIv0thDMXdfeNPdl9d02_pY2zgRilEV7vt8kb5OWah7uLVjaaGX4rZrcR0v405SbX2Sc3Nten7TOubQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=u2i179Es6239cltiorFcqr3i3HlDxxeZ-fot6YBY6jjLTYeyZ1aCUkJrv9ZVBczkww1LpDpqlWGDjl-BSB1IPuxyscb2ntuzcdKci0ur5h37AnZg1IytGOfUYZrFvqxhfOz7VZUrLalE9oDXXC-Z5nfaICjuMe_R_qkkOtFQTxmoM9YvFuDRwrac-QKTEdF6pNHBDAMZNZsbIFfWWtKZlnRoJIU1tI3uB0p1cYc8tn7Wft6Rh_yyNt6Gkkvutotq4VAUPOnKIv0thDMXdfeNPdl9d02_pY2zgRilEV7vt8kb5OWah7uLVjaaGX4rZrcR0v405SbX2Sc3Nten7TOubQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmA7cZLAhRsdltJxfQzGm0o390gMu0UF9soMpOe9FGpfpPayjprlRYPne9GPYHcB9tGUv6KKzoaFiZ1O3SNXlOTg5cXAuMfUlh0C8kHVZCQpYyV0hmxVGNtg_5oo2_0MVDMLmG7YbXMZGSKUuHcN7FKeNB8fh-q0bd7DwP-P7u7h7_zJxRq6pqIBQ9oWY_oQOlsvTcBVQnBDJ7kWbqUtdCBR0cc6D8KVlM3BhzZXdh2ZKt7qFM7rONI_QoaLmYsvXxp3JjI9MMs_8xX6U9drxp19DWmTnPSqcpu7Rw0mPy40e67EUtQAgY2heHKtMVY0DG_087wjdpgKaThaDwn_gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNfr88yrj9VRTEfSyyGQ8PiSS5PCISrKVq40BmOOO00_2voR7mGO9BPBgX5LFQ79mmeanLfkeyt6XLNLoMbOHC8a5n4OiXoLR1ySd2qKuJoiwFzfYpYDky-dcrAS5-3Ti6RJPAEUZMK3lOJagL2T8HhwuYvOQCvXowrz0kOWtvDovbKu_yAfbL5UXM2sbEnzSaBI3yegNCB3ghyN4l-6HPVNSkCpfnsTYSvvz31NgXpawz8PkjVau_rrsyI49ZecagMM4tKqFXnnByoV6sbIsUu1m_PF2e2W9xAnkib61kgH4OZxbsqzqBxJNw2qCEk9X9gr5TfA8GwNQ9X1g6ArSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=vSZjCVx1WREBUvJI7Y8WRB9N3J0bG2eNCIMvxQdAK6bDRLbjAcCeWFyXVbzU64a4h5Ly6IHtWeokSbm8nZfLS6Pi0liXrc5aEmzsRgj6EdLzCFcE5GY7DHaho0IhsAepKpWLeZlmuxBv2LAOxbTVXkXkg8fBsKi53g_k5rUcSlp6xuU5JxwoFGfr5jY8RZ3py6SYhHnw2_T5eNDd0YNf81aHGop-Atzh2fcwWpqPreto3kPjcCu8CotEu98aWhbR_xFDYYmKbSQFlnwa-BlJDglept-6AxIwvE2slemsavEB2rKWOkppQs1AY31NLeEmKqTeDJy1yciHmFspQo1_NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=vSZjCVx1WREBUvJI7Y8WRB9N3J0bG2eNCIMvxQdAK6bDRLbjAcCeWFyXVbzU64a4h5Ly6IHtWeokSbm8nZfLS6Pi0liXrc5aEmzsRgj6EdLzCFcE5GY7DHaho0IhsAepKpWLeZlmuxBv2LAOxbTVXkXkg8fBsKi53g_k5rUcSlp6xuU5JxwoFGfr5jY8RZ3py6SYhHnw2_T5eNDd0YNf81aHGop-Atzh2fcwWpqPreto3kPjcCu8CotEu98aWhbR_xFDYYmKbSQFlnwa-BlJDglept-6AxIwvE2slemsavEB2rKWOkppQs1AY31NLeEmKqTeDJy1yciHmFspQo1_NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=qTpukHXKltf0qvapMD-klQ5jbLryZkKMvt96hE2E_7y2aUqeDM4OxK6pNAxnGMoiUg8_C6xetjQw7fIbHl6hNgipXDNvBwq7oI4NF30agEAB4K4VLQWWpo296gN9PNyTsKqngnDZM2otCshHsV-vDB3b-IsGv5OlL2kB_8JuMTRVozSMCWZ04tkQOHcmOZxMebEeeyrJfnDHVQbJN0gN9GNRjc_HYqHraekzUC6w_dyLCErESc8cV16dEYCLgd3OgkjrkxGWXlQnbT4_UJJuu2qMNvjr_Np3gJ04LyRJ8j53akxdY1R4RoqBMiaW3gimIvIakflXqx3AnCOuTw5jIA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=qTpukHXKltf0qvapMD-klQ5jbLryZkKMvt96hE2E_7y2aUqeDM4OxK6pNAxnGMoiUg8_C6xetjQw7fIbHl6hNgipXDNvBwq7oI4NF30agEAB4K4VLQWWpo296gN9PNyTsKqngnDZM2otCshHsV-vDB3b-IsGv5OlL2kB_8JuMTRVozSMCWZ04tkQOHcmOZxMebEeeyrJfnDHVQbJN0gN9GNRjc_HYqHraekzUC6w_dyLCErESc8cV16dEYCLgd3OgkjrkxGWXlQnbT4_UJJuu2qMNvjr_Np3gJ04LyRJ8j53akxdY1R4RoqBMiaW3gimIvIakflXqx3AnCOuTw5jIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=aqMsw04fzGfVpN0sy05Uen9ehjK_9EnwXkTUZbratRwaHnVREZIdCmN_jwJKcD28dd3VUZN5Nb6ojt-NQ6T1nMjO5IXXJ6SC8i-whsG5A-3P4YW3N3MzEK-EQNjBd6W4Gezg60Rz8cgp5pZbNcZeSGdC_2W-nswAWwIDy9CKGBF_DqJM-BFpel5iPnrd38uKhPNtXP5oSr9zlBa94sOgnxIt43kD7Ax-STBNv4FzbdUi9cravFR5I-RSvLhrfMD1WDWCms8TBnjYfazxkAPff8uu3qUD5IjpZpMAni0HFJK76olqlATz1b89TZjBfAcqi4OSQqvnGDz5zrPcU9cQODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=aqMsw04fzGfVpN0sy05Uen9ehjK_9EnwXkTUZbratRwaHnVREZIdCmN_jwJKcD28dd3VUZN5Nb6ojt-NQ6T1nMjO5IXXJ6SC8i-whsG5A-3P4YW3N3MzEK-EQNjBd6W4Gezg60Rz8cgp5pZbNcZeSGdC_2W-nswAWwIDy9CKGBF_DqJM-BFpel5iPnrd38uKhPNtXP5oSr9zlBa94sOgnxIt43kD7Ax-STBNv4FzbdUi9cravFR5I-RSvLhrfMD1WDWCms8TBnjYfazxkAPff8uu3qUD5IjpZpMAni0HFJK76olqlATz1b89TZjBfAcqi4OSQqvnGDz5zrPcU9cQODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=XEmtBsUyUQwKT_HXLokTMJEYZgd7TQvdxPrTKo0xFnix35IztPdxkbRoUImkEo8daY3WoRz6ve1dB4BKWrTiLHsfkeJ7seTCs7quB4uYfgCzlIfC6HqAGMru05TYggHg7Gb2q1v6z_fY5804d_Ls_n38QOOi1rEbTjlBLrJIemIpSkMFwAMwWagEjPp6v1XGKLHlqk0s8n2qi_lTWFvowLq_vkArAZDkLdICQYfFRT2jIrpNbgoSiIZB2_DQs2VCg6oHiBLXAyowcNRGIm2Vwy5-S9sUH0mcVB8gnhmjSaOFL9IlDevK0_DKhCFG0271ttwqi7AFK8_qtKoH2oCxHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=XEmtBsUyUQwKT_HXLokTMJEYZgd7TQvdxPrTKo0xFnix35IztPdxkbRoUImkEo8daY3WoRz6ve1dB4BKWrTiLHsfkeJ7seTCs7quB4uYfgCzlIfC6HqAGMru05TYggHg7Gb2q1v6z_fY5804d_Ls_n38QOOi1rEbTjlBLrJIemIpSkMFwAMwWagEjPp6v1XGKLHlqk0s8n2qi_lTWFvowLq_vkArAZDkLdICQYfFRT2jIrpNbgoSiIZB2_DQs2VCg6oHiBLXAyowcNRGIm2Vwy5-S9sUH0mcVB8gnhmjSaOFL9IlDevK0_DKhCFG0271ttwqi7AFK8_qtKoH2oCxHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=WEgpwIuTzX6ZJ77Z5ex-Hddn6EtmokUrA9hYBjJN1N0z_d8VRouELq9X-BuhSPaIhEwqdj2sDF1QSRvlRno89ji21fs90jV3UglEXsvLb7Uj_fHqkww23Sy-dMzxkrLaEwKALj73O70Xzat7cXLRxCR28DqfsBgcsqnuS4_cW0oVk4BkasmAyxm7VD2_NkHuhnx1w24_hI1bRL_IWYhXovpGFSc9BPU76iqHDDB2BZ-DLv8xWQBbyTSEHph9Aut22QuVbMtLJWvwklyQz2iJqkRODhrlmYGYJo4bRfR49f07wRNwT6YWhJ6mhzhMjn8JWFwA79vKXUXoWAMKQKIk4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=WEgpwIuTzX6ZJ77Z5ex-Hddn6EtmokUrA9hYBjJN1N0z_d8VRouELq9X-BuhSPaIhEwqdj2sDF1QSRvlRno89ji21fs90jV3UglEXsvLb7Uj_fHqkww23Sy-dMzxkrLaEwKALj73O70Xzat7cXLRxCR28DqfsBgcsqnuS4_cW0oVk4BkasmAyxm7VD2_NkHuhnx1w24_hI1bRL_IWYhXovpGFSc9BPU76iqHDDB2BZ-DLv8xWQBbyTSEHph9Aut22QuVbMtLJWvwklyQz2iJqkRODhrlmYGYJo4bRfR49f07wRNwT6YWhJ6mhzhMjn8JWFwA79vKXUXoWAMKQKIk4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=qqD9Z0e8jM27D2jAkCn9DKDjE9aHTzFliGYRnyqxnJtkki7X1K-O7Jqh5aYzGf5jvU-r3jVWReuYsCLgDK7ROpnAkas1rEdD8-YzfIRQZbCihTANjvlKGt25GypGdUiynRD-dGwDahpuOBZB-XEvuW-yX6soBqyG25Y7RgnPIu8TsngsZecp_HaMJXy-M15W_hNMwXel2465EKLRNyMXnH7tfEpxXUx8gcs1pGPMnzeHrV1JjPm7kbTpImr_0n-4V3xfI0xqBSAgZkVGvpZMUL9l1R4OZf8cweKYwwuN4Z5TXnDHkIN2ywq60DajowpUxpbR_hoNQ-bFe-JsJYentQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=qqD9Z0e8jM27D2jAkCn9DKDjE9aHTzFliGYRnyqxnJtkki7X1K-O7Jqh5aYzGf5jvU-r3jVWReuYsCLgDK7ROpnAkas1rEdD8-YzfIRQZbCihTANjvlKGt25GypGdUiynRD-dGwDahpuOBZB-XEvuW-yX6soBqyG25Y7RgnPIu8TsngsZecp_HaMJXy-M15W_hNMwXel2465EKLRNyMXnH7tfEpxXUx8gcs1pGPMnzeHrV1JjPm7kbTpImr_0n-4V3xfI0xqBSAgZkVGvpZMUL9l1R4OZf8cweKYwwuN4Z5TXnDHkIN2ywq60DajowpUxpbR_hoNQ-bFe-JsJYentQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifVn_fKOZql_3gJH81NT2hPM0BJiGpZQgsiAzMC8wTrWy0Ho8-auiQ7oQlsRj_YGg3y0Ystss4YNZLkYOXMUJapO-HJ_QyyvkMKrD4AQrUlnTVNNGhlxKHzaV55PmgxPQxaRq4YeNjHTl5Mii-4W6U9WRBY_fJnJPQqP7hEzgRs61kYCCvIAZaYo-G4QeWQga40klLRkQzne2TWdCVYz4ZmpecCW1MbEz0X8VGe3TjC_JEe2vZHR5FOK2eeQNnL62g1Z0idm-jggLNAIQqn1Zouj-Sta6s_O3UBXeWFV06WY5V-_12_rxskRwqXS55cG5aX3omqnixCUnsP2sGOf0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUK9-ObdL19WbRgH-BTGaI6tULMHzR-43p5X9Qmgyj4euM4CPUrs8sHjwnxu0smGtdTJZp0NEKdQUA_zKBh0_tLFMrLHu86lUeAYPE19xULltrIRLwW0-t8y6OHirxGrMSAosJVcRZt1fkww-NK-XCK8mCEve3Mv4YZM-ifG-jngHS5DYRHFQYo0RDjFc5S8ZHHcbQs3t4wGOakRK7zdxa9sZx-vTF9S6PMl79li4rxZD_XPtmJDDATGst7bl0_ljNvIxKFADZxJj6azrVnp2mSOMh4JX_Iarv4WpgnnnWDy4EBFSSOAulp4REcxPcVRseXCvDr5Dmx_tsJVM1JRrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMtWzTG0kGtiuRmeBZcDcSfFD4T2PFua0_Mr8tFLSH7pM6gTvWVFxmKcbcFW4QsWMFFFHijP3d5J8bLmN8XGppiGYBLesb4ZMQDaI8gfV8FV3qWSEIboofPjiezP7ofIi5wXAPkh40SLXAoMPUF07MsbR3_1dgFUXoxLBqTF21vPylE--1B4F7hMZy5Vn-YeD9yLChvQDBQvXYHZH5n0Fa0uHWNV-KNTjXJHsRfouuAWC7gVSCzHDnWxgFZY6a9fQg1_HsIs36V9zcbqO2NJq-bnToZdXDAnd1Kz2BxYez3FrBDS1NKBO8eVtyb00kPiXjfEnrDcgGzBFrw7ClEWmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=F564VKNBHLNsxPOmrKZOIsTGzFwqgn9y8lFHeT54FnAy7rcflzm8ftEBScuGd-GMHKx2YpdHwzyupmiXiaV60m-hoCKHRU1ltrkESIW_4TbBv4PSuIDlEO70j-Moig0jVSA_LoEp-IiESIBafKS6Zyyk2U-mYCJshxpr0OuA4lHkjbs5DSEOGYqcqytzle-YcLmQ25v_UtJbzO-IyWsaO1_cLaqTKHZY2hKddV41nGRQMVLO1z5Txp6AEfQrvXhUZDxpdH78kKJaPjLiLNMduvq8XZiyZgYKR3WXoOF8r5PQVSgNuVLzYnXDf8lI9nr-yMCcprYprFnWUv-nWGZpng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=F564VKNBHLNsxPOmrKZOIsTGzFwqgn9y8lFHeT54FnAy7rcflzm8ftEBScuGd-GMHKx2YpdHwzyupmiXiaV60m-hoCKHRU1ltrkESIW_4TbBv4PSuIDlEO70j-Moig0jVSA_LoEp-IiESIBafKS6Zyyk2U-mYCJshxpr0OuA4lHkjbs5DSEOGYqcqytzle-YcLmQ25v_UtJbzO-IyWsaO1_cLaqTKHZY2hKddV41nGRQMVLO1z5Txp6AEfQrvXhUZDxpdH78kKJaPjLiLNMduvq8XZiyZgYKR3WXoOF8r5PQVSgNuVLzYnXDf8lI9nr-yMCcprYprFnWUv-nWGZpng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=iIn64-a9PWLPjhoIgxUlqdVALCPr53bfAjVKt22WUBTqAZr_uuPlypkVlblUJ-aOgWSE-xsoGRsLK-YJ2I5jrPLxVSbt1H-Q4uxGd52nbdVIYdvBkcG8D6vptfkn3cEDAzBYlKtPQFCf-LrpG24xumpES8pkVpWfazGWA1bBVqjC4_qvI4X0JogmYikXAxrPuPy8ZK51S-A8WFffPR8cUc064hKHRQ1S5gLspwO6Km3QtCifXLkrvVth2C-i-x0RqH_GqgSwbrWpSMBHGqLUdGjmbMRLzPrYiMljlis3X-qkte8W4HdIi-FoX0C3M2MxpOvLXQNDYLT8nXLgfRaHng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=iIn64-a9PWLPjhoIgxUlqdVALCPr53bfAjVKt22WUBTqAZr_uuPlypkVlblUJ-aOgWSE-xsoGRsLK-YJ2I5jrPLxVSbt1H-Q4uxGd52nbdVIYdvBkcG8D6vptfkn3cEDAzBYlKtPQFCf-LrpG24xumpES8pkVpWfazGWA1bBVqjC4_qvI4X0JogmYikXAxrPuPy8ZK51S-A8WFffPR8cUc064hKHRQ1S5gLspwO6Km3QtCifXLkrvVth2C-i-x0RqH_GqgSwbrWpSMBHGqLUdGjmbMRLzPrYiMljlis3X-qkte8W4HdIi-FoX0C3M2MxpOvLXQNDYLT8nXLgfRaHng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=NiR_OTs20HoPqv5QJXDXvFBgHvtF7B-f6UO9xAdPsr0xBuAtTFMjRMPxOh9Y865P24h22mdzdy7dqQ9ATlF31OkBSLJpvz3lKcy-Wv41Sf1j8_Ob4_kZ2un4ZAC921BVyFQ16ORiu8wwwyaRYNuQ2VU3PB7zpX4q6vSnnrRoAu0RiTKhekYKvzU4CJmKlFRbrLGaYp-7p68nhnp45t7Srf2lvbJTKBHNpX7exj9TXSBLth83iWNc0gLVNXzN6XZwX-X4v1RFWSJJPiINPCBTLltFWMgm-3L__uQSMjxBs4H-fIqIrf9iRtx7WbYy2l3MV1TVmIZugvXhGfvgAh6hrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=NiR_OTs20HoPqv5QJXDXvFBgHvtF7B-f6UO9xAdPsr0xBuAtTFMjRMPxOh9Y865P24h22mdzdy7dqQ9ATlF31OkBSLJpvz3lKcy-Wv41Sf1j8_Ob4_kZ2un4ZAC921BVyFQ16ORiu8wwwyaRYNuQ2VU3PB7zpX4q6vSnnrRoAu0RiTKhekYKvzU4CJmKlFRbrLGaYp-7p68nhnp45t7Srf2lvbJTKBHNpX7exj9TXSBLth83iWNc0gLVNXzN6XZwX-X4v1RFWSJJPiINPCBTLltFWMgm-3L__uQSMjxBs4H-fIqIrf9iRtx7WbYy2l3MV1TVmIZugvXhGfvgAh6hrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOdbN_n28XJklysUSvOwkGZjwJMOjQ-1ow4fgkJ3L2Bb4etkJvZeQBzB2YzSqDAinPGewRFHiQrRyo_NwrmDkpDUUhPrSpSU87ycGjExLaxwGiX_kZeIl4n5D8rHNT3uwqroevfos40swFS4DbSxTfkhBCKMGzKkDDcBZrp16EfGCq9MHQZEdZHy8OlcnQ_ofP_dED68aDNbVYjlvGizgUUtYLcwze0hzdcVbfc6cXNFLQ_1DQ1IcCd68UDRFjKkY-afMlIQN-xqAbNGUJlSw8gCXQ9vyU2k09ZMEAwJsLos80EskrZazJpCHwDrA4PlT9PS9WOkQ0w0T43CtEgdCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=URC_8zHze6uoF9ukHZoOxiU_wYa4vubQw7LyshjFw5p08xdbhZgPOdxvF0ktCAfj_ryhnS_fcaUtlaRjsWE4s-idyobPXxm5QYEEFdjTusPyMrfvyEb36h0wpUqsCNIEmPKTV7k7GSFDu-x_69rGXFu20qFKble61kFRErMJH4Txi8Lty1ZRzV80V7RnGvpo8tGlaP5dqAZWH1yEFZdjSxZCPCYfUALGwBwWmJmapwbF8CdjIq4JHrQrqW_M-UYUeT49n1rzqT8_CNeA_WD_q2KxivqTJifiN4CHqyKGCVWk7rEshvcxOl47NhNT-amsZqiDQgsYLElJfh8o_wpl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=URC_8zHze6uoF9ukHZoOxiU_wYa4vubQw7LyshjFw5p08xdbhZgPOdxvF0ktCAfj_ryhnS_fcaUtlaRjsWE4s-idyobPXxm5QYEEFdjTusPyMrfvyEb36h0wpUqsCNIEmPKTV7k7GSFDu-x_69rGXFu20qFKble61kFRErMJH4Txi8Lty1ZRzV80V7RnGvpo8tGlaP5dqAZWH1yEFZdjSxZCPCYfUALGwBwWmJmapwbF8CdjIq4JHrQrqW_M-UYUeT49n1rzqT8_CNeA_WD_q2KxivqTJifiN4CHqyKGCVWk7rEshvcxOl47NhNT-amsZqiDQgsYLElJfh8o_wpl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=hDr1Do9dVjHXnIQa-H4Q_GCa-9bd_WF_Ri7T268G8cQPdLQxqS60yvVuxR7_jvQl0JnYTTHbMpXmR1pyrsl5qSMhWHWriFTgPtifs-9pOqZA--FcxNHdSus4DdATwJBLbdvNql3GPLSQhKX7-YiqtH_VvtHEfbkXBOvhaVysfD9ewM81fQLGv_yWnndXfY8B4mA_Ljylrl_9_J9M0-r19JELGDP94bLjo8XJWJiteVyOBIuuAftOQSS7xyzUZsZkrCw8y8bI1pSVlO5PL5WlnJXcVVioy8726uzLputmtcSWndf9hCL2cfKwPiPH00pbmyf8p5S1r4ZGNR24AiDGgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=hDr1Do9dVjHXnIQa-H4Q_GCa-9bd_WF_Ri7T268G8cQPdLQxqS60yvVuxR7_jvQl0JnYTTHbMpXmR1pyrsl5qSMhWHWriFTgPtifs-9pOqZA--FcxNHdSus4DdATwJBLbdvNql3GPLSQhKX7-YiqtH_VvtHEfbkXBOvhaVysfD9ewM81fQLGv_yWnndXfY8B4mA_Ljylrl_9_J9M0-r19JELGDP94bLjo8XJWJiteVyOBIuuAftOQSS7xyzUZsZkrCw8y8bI1pSVlO5PL5WlnJXcVVioy8726uzLputmtcSWndf9hCL2cfKwPiPH00pbmyf8p5S1r4ZGNR24AiDGgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwgVwH-Rb3astbWiQAbV1aGHpqNUGxqW_eeUOc4GZPLF3tlvX57anzntgtjd5nC-YKGv5bdVNooRJOASKJpA2xO83ZsFbcgYyx7eGvUewpfeOTTrZUQHrm5ah5S1Ntw3-T5oGXe85eAtG6YY86PMuoOWVkzizDq_VYDsgOgm3FWeWJY9iTa84kY8_Wszf038tu7Ip11P1_gjjVEpc9eIFTtOhn3EOmEHrn0woF1EDnunP2WLFPUwS38w7BlSqHyc2_oHzy5PIoj1s8mMvwB9y2dLBqZkiXtuJj3QNWj2BYqJ4ZQgMfaPbI_JDFVLOfNYighCAWHzPF03v73DxqdiHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=dV4xK2bRENW_n_9VjMOrk851cKQlBqbwJtnR9yIBSFIXKLmrmInE1sqJ_b1QfoOzDmRmfApPMfhoOEEGbKZa8itGWeAfntD5pBe-5GwM-QfJRRSpceY9uOW4U6-FAdqQvKewUGmhLC8HZ9v7sAz2Gj8vSVLBRkoKH8gajOv1vacQ9UnWP8CKbFSsN5Ggup1f2Xj34z6-ordzrIE0IcMOTQ9InHa6kjGrM8FSyIUFhAB6ah8hQymVNc7xRu03qh6ktlobJi3MPABsLH8ZRfCCRD2bQIkUVfpQ9yuk78-Dal6_bBGwkb3Ue4j0yeKbBXpaQIBvozozuabYgDnZ20id1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=dV4xK2bRENW_n_9VjMOrk851cKQlBqbwJtnR9yIBSFIXKLmrmInE1sqJ_b1QfoOzDmRmfApPMfhoOEEGbKZa8itGWeAfntD5pBe-5GwM-QfJRRSpceY9uOW4U6-FAdqQvKewUGmhLC8HZ9v7sAz2Gj8vSVLBRkoKH8gajOv1vacQ9UnWP8CKbFSsN5Ggup1f2Xj34z6-ordzrIE0IcMOTQ9InHa6kjGrM8FSyIUFhAB6ah8hQymVNc7xRu03qh6ktlobJi3MPABsLH8ZRfCCRD2bQIkUVfpQ9yuk78-Dal6_bBGwkb3Ue4j0yeKbBXpaQIBvozozuabYgDnZ20id1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=LuYlFw8D081DTcGwTqW0sfxl1kheldxBIzlOm8ijNzltN0TqPwVi_YA4v7rUX_qg7Ctg-pHa8OE5Rz_VDe9JcIau1jkh89Wp4uif58G1KeAp3E31XL8NFNJdcbizE3_4ugaF18te83MeQiwwHmtMniHzmKMJaSJy31U6nGPyvdplbxrgdepYeNCc0h2K35uTrNuUdCWaeWUafmV3VLZ9lj-UIh1IxlMDB0p2dTpk-y5ZTWzR3YaD7kpqxxeDhUsOscr8zCNv131S_HEoqR53VhkXBFp9RMnoALSKQ6r6_-S9twyEsfoXHn-HwUkZmwRDSdW1_R1cfyQ0Khro_590Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=LuYlFw8D081DTcGwTqW0sfxl1kheldxBIzlOm8ijNzltN0TqPwVi_YA4v7rUX_qg7Ctg-pHa8OE5Rz_VDe9JcIau1jkh89Wp4uif58G1KeAp3E31XL8NFNJdcbizE3_4ugaF18te83MeQiwwHmtMniHzmKMJaSJy31U6nGPyvdplbxrgdepYeNCc0h2K35uTrNuUdCWaeWUafmV3VLZ9lj-UIh1IxlMDB0p2dTpk-y5ZTWzR3YaD7kpqxxeDhUsOscr8zCNv131S_HEoqR53VhkXBFp9RMnoALSKQ6r6_-S9twyEsfoXHn-HwUkZmwRDSdW1_R1cfyQ0Khro_590Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=Do5FPyBB5TwZY9Xfsl-WcFEeTtWDJ2pq96ajJ5c4RS1CJyoqjYg4KCrayMYTezLJpdmeEFlXxbkcv43_0or0WyO55R_QLvPStF7jqDv0dD3hP93q_AAMSDu0uw8JHHn19-X-a3KWJiC0DvcO53x-wPZ32pEJkO08VYKYf1Y_2NoO9zZ9D21oMQgvYJsZ3fws-1_lA5AqoeesT2HbQqGg1R1p0uxKLXRpE15FtjiPykHzSs0HPxzJqXIUHmTJ7_HnM1SerN9He2AZfr56mMIX2n-c6LzqnJmjGZu2v21-Yn2TQpn736xJ8BrEeivHfi77d9LTMPbgiiRnjslvqRiXTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=Do5FPyBB5TwZY9Xfsl-WcFEeTtWDJ2pq96ajJ5c4RS1CJyoqjYg4KCrayMYTezLJpdmeEFlXxbkcv43_0or0WyO55R_QLvPStF7jqDv0dD3hP93q_AAMSDu0uw8JHHn19-X-a3KWJiC0DvcO53x-wPZ32pEJkO08VYKYf1Y_2NoO9zZ9D21oMQgvYJsZ3fws-1_lA5AqoeesT2HbQqGg1R1p0uxKLXRpE15FtjiPykHzSs0HPxzJqXIUHmTJ7_HnM1SerN9He2AZfr56mMIX2n-c6LzqnJmjGZu2v21-Yn2TQpn736xJ8BrEeivHfi77d9LTMPbgiiRnjslvqRiXTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
