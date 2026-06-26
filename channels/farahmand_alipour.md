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
<img src="https://cdn4.telesco.pe/file/uUxJ9gGeZ6LX1HvvPAm-cTD4AeK0qKxyah096SCivWFYVswq2vylJd3BaXnSxD7GAEMn1hGbzsLnj8FriXrpdSOpGpIkMeB_cXchHZG3WXrLb7loe7dfy_dg5KLVmkGcyHI-vq65mBnuTeDkdupxdaL19x0PqA-EFiTHnfsYNwOIywaqCcb3EwUY67p97iBulgTQ8zTKuSgy3VKS3-EPn4vBfzyZ1ZPenPKn4EstVQ-Xwuh-oaZK4bQmPlJYHtFcq36x3Tkn1fw6kRePIM_mz7U2nasa9SIrOn99mmEVtKe7Ygtzy2vC5IQBz_6jhUXGcYfkAtBfTV-lTW732rpryQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 13:45:33</div>
<hr>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qvv0oNieOKpjDD__S1oAM2RVzTuTnqVUIA5s65IBoptVQW67DBJvE-LvZSPzcaDgfLTor8bTn8HnzG46jbxuwYDjW73OcSgno5soLgqYPMW1xwYtmfn-NUEnsMpgjIa27LCJGSOA2guHFl-vxZy_nN-S6MpIQ3m_L8Pn4FcJi5Z5HpyVTNwQjJnMzDr6wYGutaPpcGLntFhJedDiyAgjZ7RN10K-2L8BIJSTb29K1a-vfjTfZ_mKlwKQAFqWOS9E5uup5Mt05_j25GTQiajTTRwODucgPumxji87EupCR-5GsZ02xisFy0zb18_stGn_oG6-H7wKT-N5-UsvP6hGMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9J2WgJ5JE4bNwwdz7q3V2IrUVuUtOyCbKQMhCWopxKc1s6gix1hOSQOB24hmiOoqWoB5x08HGAydJYskEYx9uJ9fB7VnZeWF5pJJpDrJVOMnu_47qlJsqCRfP-HOpzs2qb0DYgznXUdQcIv9l1fZfBnSuOa2GGqlnj7f10NIymfektHzHhIgN_j39xmwWiE4ZQufHxDVJBCArVKFr2knX3wNxadbTNZDzc9agKT5UKobteysFOWA7d5CnI2vyGz9gYz5v9JuSejqwGuFbqIzFAPUn6061WK260Wq5q8Ifk9YPDRe2giW4GzW9wG7cma7pXSGwOOuYbHyQbhN_p5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFdFiG6Fo_21l3eI0g9gf5NGpCehHQROmy9gqjvXJpYJeTEPafgkUx7nkUKtMtjFP9wIeLMyJeCLfsclv0NiA-jEOkHOW_CEpgQ6_y8DF6v8l3r6VeLmhIvk_r3NCqjmuu18gMJpj9xRmp9ZZQxCwzTEqVTK4KLA_Fl-R7i_MS7BeJ8rqZCPWxPGw5fQ-zqyKEpNrHL2d2MktcW40qhVBwp2CPrCbKJVab5MSSLSKFMpulUQDNlhAT33DH8tamqPJNB-5RSGquoUGFYyPHa8ivRjt4VqG19a2mNwpC9ZlUClHNenuM5RQAb1z5EazGe_BeH7Qtjgg7ZKZ9yRI8U_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6jRmf0ba--mShtp3pjmojRkhZCp-yUBEnp6GPKvFtb3MMpcG_cIQzwaod3z_JK_RX0WcI43aGl1PG8XmYwzcaGgQ7dZllPn7bL_tAMkqu-e8pnolZdB-Q-a6S4t4t_MRQdvzC9tEcOt7r153fqzATAH8LYRxtoTYUlgM0XHwMTIqMH_IdvxcS2oe0cyQ02n1aEQvjki0NWaxnrRN5V256yS5ch6xnrJnJo1ycvk2uS2MEvUjvXYooNISJULVTX_0ILL0iz-jyHamKmAPPmPccXw6i0CkTHoLu9aZhHWnUtG1tZkcqsayXmxDu17jTsRr3B5DD6yTk1vufypS2cbFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=FV5QME_MxtPvyGnvdYt6lEapBQUZq-XpE48FOaWhF5CPwJ18KBnoCoA08VDezzVUpcsIRT2spFlfBHzAHYsCq6jBYhE4-Cn_FCkreWenalal0dy_arzkVBbT8R6NSZDpf0dPmtiN0RPzUAwCiXwpufgkhgaItW21a-1R6TPVljX47IriqzOIi-cIyBt9fkuTn2g21C8CwMiQEYeGJBEGCmyCNiAROgKZmbmMeD-8qSB2l626lilRnm2a-sWD1XHhSj1agjxz2S2uBlI_6iuY8YMGIfRvXDVwA-AGZD7homXqlyuS6LRZ0Ha-brwJD9A4--yT5zyEj9QdzX2VlRFjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=FV5QME_MxtPvyGnvdYt6lEapBQUZq-XpE48FOaWhF5CPwJ18KBnoCoA08VDezzVUpcsIRT2spFlfBHzAHYsCq6jBYhE4-Cn_FCkreWenalal0dy_arzkVBbT8R6NSZDpf0dPmtiN0RPzUAwCiXwpufgkhgaItW21a-1R6TPVljX47IriqzOIi-cIyBt9fkuTn2g21C8CwMiQEYeGJBEGCmyCNiAROgKZmbmMeD-8qSB2l626lilRnm2a-sWD1XHhSj1agjxz2S2uBlI_6iuY8YMGIfRvXDVwA-AGZD7homXqlyuS6LRZ0Ha-brwJD9A4--yT5zyEj9QdzX2VlRFjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=iF2srjxcL4ZBsJCQ_7iGRxyRMVNN1_PZd42nPcbn3iJFyxQRyIxU3xYnN8x9-e9mSE3cJuw-KHn0cM6qoaoCDYByTpW6NRc1Btl0vsdKkfkmMGQpb_-E7uAd0Ct5cI7FFJfrJi8-FCCyoxVf6HJlV801rqZZp5-HvFRbJpDWnN_JW_HRz7uTkaOE9OfqYw3NyKF3Qi0CeG13GG1OE2X7fiXIGQ11U8VDptU7jtSOWweN0YD6rU-CmeYha0wop3LY6Ue91FitP_jZw9ULFwsS1BgaM6Yl1V8aIgLPqhRhGlZFtD6eXTOc90CaJwQmwX_ojzzvUWuiEjw7WJacY0YSGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=iF2srjxcL4ZBsJCQ_7iGRxyRMVNN1_PZd42nPcbn3iJFyxQRyIxU3xYnN8x9-e9mSE3cJuw-KHn0cM6qoaoCDYByTpW6NRc1Btl0vsdKkfkmMGQpb_-E7uAd0Ct5cI7FFJfrJi8-FCCyoxVf6HJlV801rqZZp5-HvFRbJpDWnN_JW_HRz7uTkaOE9OfqYw3NyKF3Qi0CeG13GG1OE2X7fiXIGQ11U8VDptU7jtSOWweN0YD6rU-CmeYha0wop3LY6Ue91FitP_jZw9ULFwsS1BgaM6Yl1V8aIgLPqhRhGlZFtD6eXTOc90CaJwQmwX_ojzzvUWuiEjw7WJacY0YSGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf2U9OciURkkQQ4zhMA1HRxOYDfxslMk65LuYdzQ7-vVQIZOFyrZSIIiWgawnK9Vke5r2sGIEgwqsApX195Z0L70wc8L8AOfDfkbGQP1cVGAemytizh-yFFAv85cdw6d4vAo0jTtdMwfCbYgJA6Dkq_bwj6cwPIyCR2ww8zc34h6ZPg_zt-f4Et9rG-q6zlo6N4py_EuGkVhIjesN1DXbR1S5pvCujsm27167NF11oTjoUnhL0l2x-23kOQolPMqucMug1jvuILZmz_6Qvohpl68WCbepyk3ypttZns1xwPBvBWg7gvHiAjdB9LW5PZTy7rzAHLcgm_8MCaZqHOt_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/budDXemWSIQ7SkoDFzao16aXe1hInTtqIATa672agPsa9WF8EDsKLaGZV3l2WyzcdOnzy7lD-3AEzDARLU5DylmTGzy0xod2cYQUoVyaiEDygWz-aP4E3vtWkqMWNxQJMjnLh4M8a8tQhjNAa4Bv1ahYqY2UsYIJXOyQRJwyJ-kc9iYNaeAxPHkEf-9b9jhSA_aFjFd_9BNpDx0NOyB7h1peFf_j3XVoUfJM6YCCcfUQgKQ6TLuUAshceY4M24WeK_XLFURecglGtzjYh-FhsWLTeO-BGHNOc3_FHV_ke3Aq8JfdVy4vhfqBQWEuwqtDN5V_HvOy3tYY31T2d7gnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=c0tT7NJILZpPvsY9Qa_MG0_zT8zZvgFkUhOG4DHutGP_Fx04jwA1XvhCAzzfrXbA1WPCkVG-bhBDhplXaxoVWsHR3amGwXtlul4FVaWKh0xwTKj8dfhZJqajiwl0Bv8zFpSg9npH8C-BQBY8RWdCG0aMiwK1jTVLlc2TtxxqDRGk3PANTHcaVL0X3OpmDAy2TFUnuhH9FJRDGM0yL1xEYouTP0KKWAQIrrOcLtcKeLpbbIoT_4S8W1mrjP9HRfkaPv27oBCckaXIBFkGVemRBXiYK40lvgrPltQ0WZ1ncfr9OfeFEx3x8iCR_skQNb1dKmNfbNA_54gZ_VTFYSJixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=c0tT7NJILZpPvsY9Qa_MG0_zT8zZvgFkUhOG4DHutGP_Fx04jwA1XvhCAzzfrXbA1WPCkVG-bhBDhplXaxoVWsHR3amGwXtlul4FVaWKh0xwTKj8dfhZJqajiwl0Bv8zFpSg9npH8C-BQBY8RWdCG0aMiwK1jTVLlc2TtxxqDRGk3PANTHcaVL0X3OpmDAy2TFUnuhH9FJRDGM0yL1xEYouTP0KKWAQIrrOcLtcKeLpbbIoT_4S8W1mrjP9HRfkaPv27oBCckaXIBFkGVemRBXiYK40lvgrPltQ0WZ1ncfr9OfeFEx3x8iCR_skQNb1dKmNfbNA_54gZ_VTFYSJixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=OPq3cR3Qo6hhZnA544SqRW1zTB4Nc7i-pxNq6PjN4uhFo-_0wZTHtg-dfM7qan4ntEVLD1WuLx7zl4RzsQBcqfOHiF03_1QHFlLKvVzGwPIJVwi-p6qQ8NIutEXCXPBBndmLWEekyj8ld8uhibLR3TEV92LFVBtzuvjteIA4wDhXKduMmbu4RAkeDixWC4Dva9fREoYIASDk2qsAbgq2ENcoNCsfwTedn__GB8i-9KpYglj2M6TwHWX6IdeDs1plcYTF3Mdghowt-a_liRTVvPHYxlNV8nUTOXWf1Tk3cjlhqvaufI1ZzvR4HSrURn57Pm-0gBleuhi_atNz3OtzRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=OPq3cR3Qo6hhZnA544SqRW1zTB4Nc7i-pxNq6PjN4uhFo-_0wZTHtg-dfM7qan4ntEVLD1WuLx7zl4RzsQBcqfOHiF03_1QHFlLKvVzGwPIJVwi-p6qQ8NIutEXCXPBBndmLWEekyj8ld8uhibLR3TEV92LFVBtzuvjteIA4wDhXKduMmbu4RAkeDixWC4Dva9fREoYIASDk2qsAbgq2ENcoNCsfwTedn__GB8i-9KpYglj2M6TwHWX6IdeDs1plcYTF3Mdghowt-a_liRTVvPHYxlNV8nUTOXWf1Tk3cjlhqvaufI1ZzvR4HSrURn57Pm-0gBleuhi_atNz3OtzRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqBOGD9bIpG6m3swORo2sMF5Lx6KDH8xfA999sxYGEII6v-fjjGKp--GL_f4qAcVszv8ApCF4F65IUGpdHCal-e5FxCSWsPl3GOC3VHDkSex63rM90reMlygfG_emTF1jAJBuN2Y-rPR5a03_BnHxk8ezYC0FlaknBm_ZOYQEB2cdSwZoFickXaRob3dQH1rSgkSL4ZNdFj_-33NqgKD_RAbgiR69012XHoQiLRLhKDuWbipGMKUzZchd4KaXTOQMqA_Mu2bPiTshkujmg-tC4fSAwT4LKKSMYODPSqV-d1c1rZvv6D6a9lURLWwVoyCPP4k6Nu39-OPJdS1aAwD-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqT13RyNpxvUyZxQNFhVYfQBzIKdeLIX-Wx3tewxuP5oCuimFJi1Y5a4guXAEES5e8XGvOKKLIw6w2W8sxvWzUSm5sgZb3CV8xBuEDUFtVGBC3aJbm5RpA5rbTftS0PZVXW4nKbJ6L9AUlmHbvEORdos0O3eW-Nfzafm_GNZ9Zcda1j34Kw79jObwWkAc3s9iE-X3J8S8mAPJbf8eKKGzkPWaMau4hePQz85wBuhjEi5wb1F61e75ikqXinmHFmfe2Y2IR3XR3V5HrAwU2rrfCqvW12n_87wCDI-Jzb022Fh9lnpve7BsPj6WTy2uSRtmxHaYXGebIsa4ghxxdVVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXER_l-LBMLiXUNB33fB_pVLho1N5j5geqD5iwZNSCRZeRaXcPR7rODAX_LnE_Szi2zKRCO1dAeb4GSYNlF3ZuMKP9cIRsGMs8d2c5GDwFlyL0NqOO1s6CBbPzwRGKpBL8VALtX01MDiZ9uC0mw_7aNYkVfOFsbc5DANIYPbEomTjZs29DVOQXCRKvXTLxn5HkMMkcvfugzA4UzisZck7ljHcJr0AnO-3h8jTuHpVBd8qqP2r3UZYsqzqfsRbZqv82noRdl9bdBw-jZEky-ZpfyQuJew0FLLrHYpMZVyFdf9MAtj1nOVqLTSKvZXIDACEBt5TJcrjxRta6sgm1PiOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=s2OqxLCUisCRNVZmsyQ_bjVdbS2gYV765ecd-Eh3w-Eq4C0rBwDbtBKNXlcEHaXcXmGj1bd2fRMhOTEyQRRw5moOQIcR21dfPJD_JZoRmOcDJPI0Fc0JNjyhvXBjX46zmoaibH6RZPqAklEUcdi606TVoT5Rr2mVIncp-4NC0Iuw78llpIeLRrHlOUKi12W2i-FkCPrlJVwAznvv6fHDR7NUT_cp_9_JVWJ4zurDvVtVQ8Rep6s7QmwVd2s0Sl8H2JQyQ1enqDZlz0Z2crxcFZvGr-GfeeTicXaWq0F8sfm5N6QKvHMG7Wxy-nQWFASSxT-7G1QrgRVNQFev7nRV6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=s2OqxLCUisCRNVZmsyQ_bjVdbS2gYV765ecd-Eh3w-Eq4C0rBwDbtBKNXlcEHaXcXmGj1bd2fRMhOTEyQRRw5moOQIcR21dfPJD_JZoRmOcDJPI0Fc0JNjyhvXBjX46zmoaibH6RZPqAklEUcdi606TVoT5Rr2mVIncp-4NC0Iuw78llpIeLRrHlOUKi12W2i-FkCPrlJVwAznvv6fHDR7NUT_cp_9_JVWJ4zurDvVtVQ8Rep6s7QmwVd2s0Sl8H2JQyQ1enqDZlz0Z2crxcFZvGr-GfeeTicXaWq0F8sfm5N6QKvHMG7Wxy-nQWFASSxT-7G1QrgRVNQFev7nRV6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnmc5BM_BATfxTXVABN7ZsU4BordS4eNQI6aaqyKbrjAug-1oqbJULpCSOPfYakPPn9IZ-6ilxl52zQpXke46Ly4mAhmQbWX1Z-k8r-YjEO5u98NFLcVnFff2kRgvZENkQp3Q8xpJFa2dMWI7VyX4iTJmhsmHCkQtgKwFSju7nd03Nj2PIswXOa_UUSqM0_82PRRv3-ahh0OTttH1aNBrl1m6_5DFaf0dRXXf850tcCHdoK48olS356kVX0TxVUsYSMYuzq1PArgATXEtYix8B3gPpmYgj1l3V0vn4w_UGUYBUHR2PpUbchJc90kbBcLfX7eYs7kIprTfShUcLr9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgDyKCIFEawQuKRuajP-DVDVTd1Ga_rSK6An4FYmu5tAxlv8-AM182xBy-1fvpLGrFjCGZX39Vo7QkyKvO30VeKd_jP7vthJv0lRXdNVVhyOaLyaR-qf03n5OxQDg0BnkhMPG_ExvuGqBr0AqR6ZLJ7PPXXYhIqlOaEtqa76UTwGmDHsoLmqho03aA3OksSX7YPHfJjA-3dAGodheWP_4wVpmOeQjI-0lV_0vmjOgko0kjmOcv8PiY5mHQ8zjhvpp4Kf4HlIcj4xwp1SqVgbXdSPimGzuTwkRdj5N_5y4u_8pKUnW69mkSrDfgKmci98brOZDqJb9luH274MhlwRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2I7LxVCiuQsyON6hFXWz1obidKWtlBbejOp7OX43lgWpqFxyiotQSd0MyjI8IBczNl2sRqxAEfTw9YETwoF_GUrsjILRV65w-0xRxDBQBSuFR1GCsghWc0R3r1JYns2xIB-mTM4KxjQcP74_N5BzMAexlKOodxS4VR1F6DhVA5W9CabGXtBW_TVKUdBlMnQBU-0AfflmtAcOKlo3ATXwuvlv7kIHWwkLJ12Vhb6Hkm0rpmf7Qxg4Fmv9tzTswRQ1ZVU9w4iiU4bKCjvA0iz851mP2aP9TMBtJ392Fp2jdw3jA1WHtgYv-q_Zg5JtnN8-yf36LgB_w-p2MA_UuvHQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-MZjbQAGTLZoPp2lPfEhFRgVvkteQJX1p2W_eD1cV_mkT1dsS0wEjoXmcqxwIpE7wM4HfwXF1uDFYNLkeIFRMSM0VWSU2GSfYqldhhhrCh2DOyNXbggiePm9A0dOPwauFUyXsDLxxVJh43bdteOyBJ3ufzGXQbQifOjom7QCXYfApWN8RxSdj9iJpIQOAGSNzTq_wf0oMthkTS5_qMoBTcplZUrL-BxxTmPA-hUJ8Dn2kt1j9vDiEsedb7pSyYG57DPsO8yL6Y2fvv2HNRBhvf1A_p7pJ6Nym3gzF_b4nF07tEAFyCHRZxWeJrqH2E7Jee1nN64W6GDu5sfuP09ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=WXp105lSMa2OqCE7MI38y3GGs0evRgMo6pFHnX8B7eq-bdBVKYdiaNwy2aA0XigbULN1XvEllqWPiBIOVOWK6nLkSqnF1CbLe3p71RcW-qaTWQCKf5PvrKvsbo_XcCyXQPVm3gmOk-Fh3i1c-qfYCDD9xOiL3ARr9sQkJNH9mMM-kjjV0H8l_FT4tawJzha0HFd8wTrigwWNDfCwwFH0yUJDfj4HrSyJLLAFQlSWiiXxcMKojUoZNikc_Zo6k30l6E0gFnL2D_HJTwLItkMhYrk21qne_HcuE2EI2Fku-3-v2OtAW3oNY7zftukOqWxnzWBK2rubxByeXVcvt_aehg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=WXp105lSMa2OqCE7MI38y3GGs0evRgMo6pFHnX8B7eq-bdBVKYdiaNwy2aA0XigbULN1XvEllqWPiBIOVOWK6nLkSqnF1CbLe3p71RcW-qaTWQCKf5PvrKvsbo_XcCyXQPVm3gmOk-Fh3i1c-qfYCDD9xOiL3ARr9sQkJNH9mMM-kjjV0H8l_FT4tawJzha0HFd8wTrigwWNDfCwwFH0yUJDfj4HrSyJLLAFQlSWiiXxcMKojUoZNikc_Zo6k30l6E0gFnL2D_HJTwLItkMhYrk21qne_HcuE2EI2Fku-3-v2OtAW3oNY7zftukOqWxnzWBK2rubxByeXVcvt_aehg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNxjnxS8dAUsYsPlsNloekarLclcBrdbpv7T0TxzkTobwfHyD6G-RceuKlSqZwtpN2p6D__flWIjndg_GOCHKRsiisn-bF-WMk2Yiv22osVuHLg2jpPHMWYa4IxhvS2I5gytr4OTfZKto7KCbX-DRD7Qje9gcWi1MSGTmtH_T1eCEmwp2bGBt7_3IJ7NQeORzVH1FsQqgqz_sGYWitFOxFU6Mauc84Pe5ity9ZJtrz2C78f11BozEW57ZM6KSgNPV1yd4tWqkuDpY34UnMDJiNeMQGO9Y13qZBhW5qQp2KVPoLs5AYxNRnD1aOsyZKXcpwUKA2etw1XPwwrN-aRmhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaTjB_UEppG63WKnyC44e1Q9tKdbwvA5NyvvsGaDP2luJSkiv0BTdx-NqeQ_wsFi8wcF6aQ-2uhBOm9hRCUGYazGtHYc6iYvJ6S-GVDSIVs5OhwpJZlnlf_EM6lIqsnfeCrCX-OBV7VRMdbbrPhuwOzsAeqo-7bSvOL1foKSO0p6w9MJ3g8iBVndKHWk5j1Ng44e7FsgirpE2EaCut-288r27C1q71pPmb8OqYUW7kRPEfUYSUxGBZfo-WwSkwWiPVJK3g51I0vWjbgUuqAuuNngNJCw8MEiEgxSjvhTS72BWenX6kRX6DgXyJA4dWEMrehLlzN8gJ0ojzBqx0OX1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ4eWAE8lgOp58RY3HAHr_zgZJQwUx9uSfGWfgv5S84GDtoI1W7h9qU1cfQyd67rwoehqO326Kc-rVk09YiCE0UB9Azpgb9pF-NFYiZyjgJm7emHJ6OH1nFaI_rMgRJfnodbWxPBuC_vto9aPyvisfbjwl1ElOxvv7WIo-VZItt3jvx6bA_7H_-3NezTeqNSRIw4NvPUDFpXOFr_RCrjEJG8bmf5-XtLZKYdoCrYI38S0Ujs8gJbtFv9r9NL4vKSA8bi6DsaGE_B4tU7CXk9fXwygVqcxJZ_YOxJJdmPDDB0GVgpmPjC3QahfjhiUJRIwab2Hx6iK7nwb8q61aH6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=OMALeNtp9fMzzWiDjI73UECMq7uxxq2Vi-eYmS2aSxxIKI804mMHXc5_iW2TLcfR1vYeN6axgjujkyU9r32PjeVjeg_NkOwUlqmTJiGaZTW3hpD1eRmjNATVDPp2SFMwcOu8yLE-yZy_yMzQtNZvuqHtNNTHm-Fs_G_C9MZI42s3I7hFDg_Bg26euhXO-me6jHbADZHKtfYtWsGQW9wx7zHItqziWR3RdciOpiDebiX0g9IWxwZ3lDqx_tCenoDqdhD9vrmK9akSGkE040zf1Xi6rMYS-AxtNpps4Q1RU1x72_ueC_SZz9po4KKg4_MCyfQG41AQOlzp282kV08Rpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=OMALeNtp9fMzzWiDjI73UECMq7uxxq2Vi-eYmS2aSxxIKI804mMHXc5_iW2TLcfR1vYeN6axgjujkyU9r32PjeVjeg_NkOwUlqmTJiGaZTW3hpD1eRmjNATVDPp2SFMwcOu8yLE-yZy_yMzQtNZvuqHtNNTHm-Fs_G_C9MZI42s3I7hFDg_Bg26euhXO-me6jHbADZHKtfYtWsGQW9wx7zHItqziWR3RdciOpiDebiX0g9IWxwZ3lDqx_tCenoDqdhD9vrmK9akSGkE040zf1Xi6rMYS-AxtNpps4Q1RU1x72_ueC_SZz9po4KKg4_MCyfQG41AQOlzp282kV08Rpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=hfWjqZ1DALHdkLMlvvpaYerVoIZpt_vmb6on1aD0eyVmwZuR8zcon7yYm657V1vKm2CdL527tn5mkGvVylL6Fj_EXUmdwdQDIJ3MfaKUdgebXMgBNaVt93xSxyQHis-8bchLBuycIfDIK4R2FdLB0jsE_OtTPmJRhmE75gxlo2OIuDpTwRS6kkTFPGxKIpcDn3NQa_EKq2F1jESS-2whtdOrFIlbFptTPqSHKRrnezDXtn9Mcr7_iVEjmWiL5rBNMu0CtB9vxmR0_FcO5rr34G-NfpaH4e61JBCL7GLGYNsPSuhgDguigiCY9YJMeUB9yQAB6pmueRHLDCakxHsp7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=hfWjqZ1DALHdkLMlvvpaYerVoIZpt_vmb6on1aD0eyVmwZuR8zcon7yYm657V1vKm2CdL527tn5mkGvVylL6Fj_EXUmdwdQDIJ3MfaKUdgebXMgBNaVt93xSxyQHis-8bchLBuycIfDIK4R2FdLB0jsE_OtTPmJRhmE75gxlo2OIuDpTwRS6kkTFPGxKIpcDn3NQa_EKq2F1jESS-2whtdOrFIlbFptTPqSHKRrnezDXtn9Mcr7_iVEjmWiL5rBNMu0CtB9vxmR0_FcO5rr34G-NfpaH4e61JBCL7GLGYNsPSuhgDguigiCY9YJMeUB9yQAB6pmueRHLDCakxHsp7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=Gj_Ryk1rlDPRowbfaTakHRJ0PTErVJlWUaOyr93uCKbqOPiT9alwZmmhbuGIRoMb_RKLhtalnfxyZ94U-H7eaee0KwuOPIKBzW0m2z0GqBE0v2eOplD14HRX4ES-yLlG2eCIJjAGrHusgQkX_v1GiW1nuaTjXz4dr3cS2cbs-tHlr9kVa9auDEF6P5GuI3O569nbiHSoS7qnqZ9MkSEQ6WZyfq2OXT8IB30d_D2C5f0ok9eQ__FKMUQkMS0tQKJuyxYJ4CjFz-vBWj18R5i-dJYjQfmVZL9RM1HcEVwkaJpEHCa66rqfxCQLltodPs4NGulmlZ4tc_4z6udoknb1vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=Gj_Ryk1rlDPRowbfaTakHRJ0PTErVJlWUaOyr93uCKbqOPiT9alwZmmhbuGIRoMb_RKLhtalnfxyZ94U-H7eaee0KwuOPIKBzW0m2z0GqBE0v2eOplD14HRX4ES-yLlG2eCIJjAGrHusgQkX_v1GiW1nuaTjXz4dr3cS2cbs-tHlr9kVa9auDEF6P5GuI3O569nbiHSoS7qnqZ9MkSEQ6WZyfq2OXT8IB30d_D2C5f0ok9eQ__FKMUQkMS0tQKJuyxYJ4CjFz-vBWj18R5i-dJYjQfmVZL9RM1HcEVwkaJpEHCa66rqfxCQLltodPs4NGulmlZ4tc_4z6udoknb1vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kotJtVYsdLSPnm62jXWLFe7NkPkhwJTIEBNibUXSXLl1XfQJofe4yxTwSe1CaKJlWfOfOxovIQKFPMU28GCTopcZzvJS3BGgYKJJqpTZy3QEGD7mb-lztmj8XaPOkjupUGHTZTDvLjQmcPitcwNqCi4CyQeflzZaokK3tn2a-1fphLAjims4jZ28oiis8vtBPD06CixyddKvmns8qaBryC7s_Ho7-PBsp1z3eiwxcmOkJZI00cOHor-QPp54T_xHDABwN6zKaAStUh5KSvk1LyjUb_nGUv35AjOGN55dyPQddinXz0Li0NYC6j6SmPSowBNo-JdXUGZtIuP52nUlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg8uC06JWrdingxilJwCQJg8j51jT2sLVIhVj5P89-zj3olggWYBTQTIR_cNt6BGCWkBbbzWXUL8JGwrnz_ajeznLmrUouOj55UJXFMBAorLeMky7p09MfMNN50EAULN1revBI5iPbtOwOzbiITE0wSE_Z5j5edBL7FWLmpeUJu-DgyuMMyYDL45NhYuWQdOKlX6Qa9O1TVIGXEZjOvkHigd2nlGalFoJdsZmo8amEY6glLscpIi4kk3c39_z6_zucRQnEQ4xpUmLLhnOr-66ScShDEoSx9zzbqcljqzhnnGiF8ysfaQOvYOs8K4TBtA7CeUq2Pk86-_49bslRdMJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DsLGLmDwwJyOOrrZckoDqK_HiCYcE94cv2f963D-c90fDhGdoCkwl_Lx-p-TblfBNioUyP0UeT4rPvdcnwHwPC0q_rPxQpW393debZbyJLR-Jgx-NEXvaLsiZR7DAYk9w8xzS4lwRhy4-QLGplXb1lpxR1cR2p2HMHQfVN_AFfJKzJI131lOHbpiHeDDyR-LUMm_QeJ3bciqKoFJVJeJ5QailcAcUzLkS3vkR6B2WkzeZKuwhWvm4d07XFrd2D-9iShhYIgtDPYgbQdJZhI2HmmoT_l8Z3fpQP76_887us2E7BicTwnEjKJHel6GC1d6rxbvHS48hOa5bR0Fv3GUcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBqFYMaZElBXKhgTv9JhSrs-CjjhWfwwJ6gddTaAoKMuMBwH_Txuqt3d7qd0p8YD-i_lGLwO9OtvgZbhFIFOjUbLokg2IrpxWlApE4Src3Vyqw67QeklnCZ0mwoNod7t27Hxrhx3AcpxGGc9fqovXwivWqvn4s3oE29ygbcGQXjRg3cZJaxtU1EpzquLvznXz4V4nrKQ_uca9EsdOzAdFwPiNmjwBPEK64kVPzPh_Lj3WfkPN_mHjsi5RWBxpVr-K8vFdX2Kq9gM4kSNG2eOxDK-Q8mUr-ZD6qv_JX1SslHB7k6kHqSPyj3qyd3e8KMzANuMMOERNWzHSJ7TIetNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIr9p3h7-o_bBzYrEkIxdHcAw4fZZtLn3lOWLP_smdXOPW6BYXnxoUSnW4YK-7fTJ4CFcDXLDPNVplTyeE2Wj-hh6aWj22l3Bk2E75YVrYha_zYtEmrg-GJwtdakpF0AySZWIZYSkRN51DQaVoCOmUZk13w53SxwDomKwMaWyHVnkntfCfe5xhpWLdSv5esvjwnLOxhZjLe8Ms9Fp4C6s-T8KH8Ya8SrQHjssU4lcJC2BBK9b2OuI8L2-3rZyVha2b63TZSfGXIPJJT-rvRsGPbQ_SucXbNeMcfvCUuWNr_ZwbQNiwuWRKOg2JzOP1eBETDjVnTNr6jvubfSknRKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swkrt-VeMPnilnKCb22hmxwoPZlLI5OMYrbdtN8gfsAzsC5kc44VpMl4j-0Jm1DTBO9DBaNUgKFoQT3ZTQ_blsdYAXBBkdGxbj2ontNrvkTss1HuFyyQuZ7OO0zsU566Fc6625D58qKFf0KOqe2ZUx2v12uDNo1yfTlbt7584SqHU1hYlh1bPBUUDVGHjUEYlmFeEeWDED6-VZjozRa2Q0bAQVVNpOzdh6CwFBlcwJKaHLZOhpVxZjYmnmwMRYykyXxRiOeNNV31jKKUssf1coGEJDAK8eJhdog81ZFZCMSOiiNjtVZRoUudKQuy3mtT3_Q4G8gR2Q-wXuwuq2Nhyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r44DJD96leSE6SnpHJ7aq3wvaXIOUcDSZmbo76ucMiJsKkRu5GKm0qVCxOUvRAKvEsKpSzG8akj3-nP5H-JJ1uqHMmWrdcvqy-njzcnAtJZyWm-kx_IUmuFv76hw9rd88iv7M1AWS9bGVVn0eXfsoFhzvRiM6rKNnlqjsBI0spQpWQ_AqA7bfrY6uEDiKBF4CKrHmYwuI4nDzGRx4KO4GTjQlAnY2mGaUHQ_CBTDBzH6DIS-AZ0dsjkF4KceFFEV2KXuk0f7WSvRiwN-D5MvtDSc4ErJt8FUzqeeT_L5GyxtzWK0tx5BcglN7yUKfxbKlYaG3n1loWGfgYNo7yrqzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8MTFELjHXU5k98Qmh0bULXycQ3lFIX98jHSP3dSd0vFQctmZ37Aaaolzv76qmRbOp0iodzKVBwJkdMhNm0GZCGU3tLMxagdJYAVQtAXFPvMF4zOYruZOVu1vxyhyOIcXk6IsDlfd7ZVcuMUKuMfbHhk-TQmsPjzmTmF8nUEwheN1Nh1-hsVqVs_UWWO_3mVFI8x0Bi30v2bSrpJte20d5j834d1EStEB8hvVQMtxqi9ujWBE-jtX8_joA6y-kYhDKs67tehpyKJLwiV2cb2USCqy2Zsx0s0WBHVcAmU5LjyNi3qkrbuGvOGfW2LUKxXI6iVeZIHFRf-LEKPeaJFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7uVHgIY293DYfDE7JgLSlPvvfZmudtCvkP40ZU3EmqH-KiFQSOjKmMHzllB0bYzb6D8tbKSGUAu9DqsMLDfmC2qK4Ux42c9G9_LJIvtQSEMHtTVk7-NXBfdp6oKg-p-DBcFcHrlDwZ0NWojsx3qQc-XHdn2gekhb4u-hH4hD0gTEnfcMLZB3GWRm15D72UfoxfXcfnM81yCr-hhd8pfHLlpI-UwodfKMNOszC7cHFuOpkC3P0tSMffJ3iIFCq1t0ntPQEGX6jJpR6zSBKoZN_rmr_RJWQ4VzsfFruQHxnwSf-dHdKUnQrvfY8QrnDepOy1nBNOcbbHxEsAc5Jakfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op7ZOQGZ9FBLBPejSmlhPQ3OepaOQ6exuIP96g_StD5jrQYJXR1L-LqS7MCCtfFSrzrhsftIkyVz6Ek-qZGykGaWVDA3Fpr3zYB_9fAXh6ZwLOyosy22B6UjMcRwZpyH0OzRrBLI2RGvhE34WV3PKsFp9qEmDxR6PoWpFQ9jCP6X7XjqBcLvjVtBiZHoQ6wLbLKSTl4XMB1jty6m129umNyL--tVHHkh9U8snAfwADoiBSDLnj4RLvROyciiFN2fY44B685eNZdi16fqqu02TUnwtD0kQ5uXC0fMUemjqis4NyGyxBNzFy7-uQKcUv-2gk4ZK31T6gwyWHsjtlNUTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOCWMS6q1JIu5uRFHEpNphIRCyFbYFgO2ZKEXvGL14_mlHjHQ3kdeiu_LZ-jQymFjQT55RgeWVKEXvsrFiJ4w_fOvGdkZIpCT8Jp_c8DEQJRIE09zDDSippBzHi2eqExGn4QZ8uo6K0WJ6jYaUotr9pHPVKH5EaDSV8PHalC-d_AScBDEwPhNfqh_Kk_6FzRI0d27EtASaT4cL-faT-nnu1BSDLI6radEbPAuSFkb41lX2b5NUS59_C5NaDo04DWgRmde5lzsoQzgVZS7Q3yhOszybC5CX12szgqekcCCbtaOIdlGUcj30AOUXAwJGN3HIYfd48CDywMksidEgc_NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7ZzEVbLXWthAJVKNeYvAzM864kK3pGVmm2KZqHJI_6cPWSs80SQv8etdZE5CV5cr8wN7lO3KGyXRHhcGH0wWsCXWx3bCbeJ2Tlfm7SFlddI_jw2Qvaf0cdDcE5DVnFWdDlzFymm4zgI5UE_nI4Npwy6QsZGzEt_IxVlKcw4Aw-zd4RumI4fcTOMvQRnn2a0NvFXKupYoX7aQSM0jzDO4K_OKM98-QtCJpLciVtsuVOfJOqfpE0M0pWohwWtCE8hB_ZiEl3I2cP3ZnWMtxoCiQZdB2HU9Ga9NqKaHPW5_amNjSe31T7ox45-HFVGPIEMt6hvETmHwAyoqA38pBcfUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY37RIEsCgPiKgfHDxg-FSTLbV9gdDLwKiGXCqoFYPEYKZbNmn7MN7th4cd_fnQxErk0O9uN1Mg3WzfsA3-oaOiZYbe3B6HVrWDPoQ1Xq6WoV7FrO4hJzr-TpJicopTC43NV7ziRFHk2kD0-tleBHiz2SjNVMorJlvmX42exTjTrpUtW9HwsSXa3PiQ3wSrutpWwQz5mAG_AojDYyn0suyxtIYPwaQu69SZ57RKflEWvYgj2IftXwUyqUfAy151_QCMcbJD_RIxeMSYk1dXsQFGR9TWe2PuDr2bb8U2w_-Rk6_h-uf9X5lYOnKKvG-48lgcdLvFfvKmOaxPDKAi3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZDFV3dVfJE_8fCzSjhn-HyLJSoo3yr7V9jviwPBmCzGqQhwGoMi7ayH0wZiFNVrf89gUvoeYLL5-3xgdSiLZgZCusMOXrd7uuhUIDax13YHJFuwwuS95QUl-ggJea5IyzFdJ1yAtYrpN1wEd6EfLaou33eZGQxHx5b7kZpWdjZdiv1VfOdITaeOIDqlLGlYFmUqg0hAQyPxSItKEeFlnaa_9GG-J2IWMsUMelNPxl5Aa7-YsjWXCtAMMOvqv57vGZGIEc0OvQW9oMaTxZiVdYbcrlZxdPNbg2XCKXlEwqwEguGmArSGLrTTwu_i1jSgFQN6oJey2uIXRHp_ykJgJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viOdlo2eCkGrHA9fTdvoZTWMfdc9t43tihY0YOJP1XSTV04Aqhgj5GGZC1tnODKfcSFJJpwlvVnfIH-tErbaac1WN7kh79uuQHpINxxt76-HlaCkx1ixY7aYo5LxrFtv0RfDq_ZWorj85-Qa9B7DFLPyx27AGp1h454FPyiZlx-vTSF0h1Q4NDvS3i1oYCJAbRdivmGmcNwfA22YjCEQQeW2PpPKMVsCMzzGMrgWu36ZyZo1lZkQJfQVQleZjvwDyrF_bg59rwYXZRa6jpyzkpU227jSoxZWgpJYQfgBtqD2c8ij5zNT_HL94-yfnJEEg9ogMcAjtCniDS_CYmE0cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=Mpt9fNhY2XaApHvr2SzI9DSOSe-z3QOBWuKv-r7rQW9EgO2xRPD-4VakOXXJq2-8woducmIDyKX8ZK4zRm0iMHCj5Qoj7jtOjsQpMvMFWGSPOR5EMxLINHxYD2e-73tjKjJwi-snpkYXo9ok0GdvKjnf5FRiJaFhCF1R44u57F-H8my7x3mX3GCSNS8sW0p9wG9uem0QaLJKdCeYWo1kcL7GOVL8r6GC6RAiuhRnEWDcQg5Rq3_NXAGD4krU9JtK107kXvjERBqlaEG71eqWegt3OpvkTn9_Y3ncmSqYGKgmfRp37RutKBTDemwo2oYg0Yb9WHkO7B1IemtSdot8kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=Mpt9fNhY2XaApHvr2SzI9DSOSe-z3QOBWuKv-r7rQW9EgO2xRPD-4VakOXXJq2-8woducmIDyKX8ZK4zRm0iMHCj5Qoj7jtOjsQpMvMFWGSPOR5EMxLINHxYD2e-73tjKjJwi-snpkYXo9ok0GdvKjnf5FRiJaFhCF1R44u57F-H8my7x3mX3GCSNS8sW0p9wG9uem0QaLJKdCeYWo1kcL7GOVL8r6GC6RAiuhRnEWDcQg5Rq3_NXAGD4krU9JtK107kXvjERBqlaEG71eqWegt3OpvkTn9_Y3ncmSqYGKgmfRp37RutKBTDemwo2oYg0Yb9WHkO7B1IemtSdot8kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBZvRr-w_GjI7cj4_iJjXdt25I1ZEpiE2_D-9gofJD3hxmKy5Os9vpTmepzu3rZ7HIrW-FWHAq44xneAQoFogwvhNO45W4N0SI60pBsoFIO2d0KseUMvQqYZL2tycqHdtp87sBqcRnMHUUI6-JxA_2wkHcJbW0RI7TS5LuVjAOVZEucci_guf5t-AqbIoMz9v5EkwWGE_eVU1bgMmarh63ku1KoZ3owoV2snY2IsbfhkWa3PEW3OkADyHkby8UAC4UzrhMi3u1zXiIkVZSy5Rn3XIMiaHuRtPFPXkri6AW0xkblJjyTTgy-VU2THz0UkMVVOkWvbaAjT0SYxEiCJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=BhJhVKJyvzXCnx4U0SNqWKAL_BbODCjo6nuZLBMaHTO_1u6PVGIyayDr_DTk0YE-4iWyC7RQ_wR4DLVgGIfz8mZuaqdolsHjZgMSxrcNweD3VlqqhKJkS6EBHGHVbaqJnZ4gHC3hXJDE0_TO9yO-0XUFZVlfzFnuVyURtmbCiC4ZHBBxaGXuLnNV7ZJIvyyCgagl3GGWfAO-UcCRvzAJ-Ijgs5YTMGA6D0Lylud525nJqTvTzdSNQq2dEog-BcD6Q0F6p8sRhhZybUeP_SBLScA3N8kWPlMLbXy1bWpIOPzjJ8_fDYWbmm9SDx2MhM1c1V19Nu79u1uiwwGKO8PynA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=BhJhVKJyvzXCnx4U0SNqWKAL_BbODCjo6nuZLBMaHTO_1u6PVGIyayDr_DTk0YE-4iWyC7RQ_wR4DLVgGIfz8mZuaqdolsHjZgMSxrcNweD3VlqqhKJkS6EBHGHVbaqJnZ4gHC3hXJDE0_TO9yO-0XUFZVlfzFnuVyURtmbCiC4ZHBBxaGXuLnNV7ZJIvyyCgagl3GGWfAO-UcCRvzAJ-Ijgs5YTMGA6D0Lylud525nJqTvTzdSNQq2dEog-BcD6Q0F6p8sRhhZybUeP_SBLScA3N8kWPlMLbXy1bWpIOPzjJ8_fDYWbmm9SDx2MhM1c1V19Nu79u1uiwwGKO8PynA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=o9W-2d2L4SQUnelfi_y5ddVb_3G9ITaXDa2JRnFAIRMFmvLRPKwnrFwdUFnImZnzWiXZ9m98WndYhG0czRAkuChC9rQTevoF_QhKHCARlx63lZO496foohLzvjfQ1Zc3Vo1Kcq_Drzznmz_K5-y9ch3HYC_0HqCmQHLOa0IAlufrtMfHbxgiORaes2-Bfe4kFsQDP7jleiOD_e0xW_u4qWzPm3DvD9SKM3Z3tcIvjyJ_5NVLDO0gCn97_9a02zURYx-TCSbkdYpQBWL-QeQENdhYTbyN4YIGPXb3Bz2VaTT4N6nWJK5IkN5rQiMrwnqA_nmVzp7Of-HiGka7mRewSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=o9W-2d2L4SQUnelfi_y5ddVb_3G9ITaXDa2JRnFAIRMFmvLRPKwnrFwdUFnImZnzWiXZ9m98WndYhG0czRAkuChC9rQTevoF_QhKHCARlx63lZO496foohLzvjfQ1Zc3Vo1Kcq_Drzznmz_K5-y9ch3HYC_0HqCmQHLOa0IAlufrtMfHbxgiORaes2-Bfe4kFsQDP7jleiOD_e0xW_u4qWzPm3DvD9SKM3Z3tcIvjyJ_5NVLDO0gCn97_9a02zURYx-TCSbkdYpQBWL-QeQENdhYTbyN4YIGPXb3Bz2VaTT4N6nWJK5IkN5rQiMrwnqA_nmVzp7Of-HiGka7mRewSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpwQVEcVtVitYGb0mOcdq1BmGP9xxBnxKmx0hV02ly6c9YREYnk-pvXZ9mitxjYwUVthY0ILZvBVv6xDwT289LeKlzQHihj5WChJBjZkmZqkhgdeUuAotNQ2WHV5c-x6kSTvhurtqOgksjzKUI5_0VFH_SjIUj6r0qKbdSuTsfZowVZ-wb76nbz7ElkysdfaL8eCUVEEfTVW5b-df_42ustbOCbGffnu6vq_W8fNl0Vup24mzxhhwldYzxc_YDUaVVKzkvocQKdh7xtiMaAkMLLGxY8-zWHdpXSmjDBREEtjbVSI5UVIN-IMWEL5jTYQGK063bYQODsQ7W3SUVMrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=b9YQK6fOj1z4M-RrhRxISBENzJ_NWpiBP8Vhr-wb3CeTHsgIq9H_vWRPbQAu5kjoRxdux-5ysVDvcB3N1NUZVfEEbrpBqYXIVh6gH4ZteYSklJD_eX322snfU5exfbV3dBmDA3k5DHqEwohYROuVmHWT_qlea90BS5aUYcDPHlObK7upk8JozhmaWybl6DmfHhx5-lReSpAATLnJeKowql49-vkgAxNikotYVgUMz_AqfFLOZXwXOFAZ7IWKQetKmrwvLQlfTENFHLMGV3ZHjFyos5samW8qfIDqLc5kJo5oxqVuxORsWsKMOkCohkaw-5KIPXPal1qhQ1zWGDI-Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=b9YQK6fOj1z4M-RrhRxISBENzJ_NWpiBP8Vhr-wb3CeTHsgIq9H_vWRPbQAu5kjoRxdux-5ysVDvcB3N1NUZVfEEbrpBqYXIVh6gH4ZteYSklJD_eX322snfU5exfbV3dBmDA3k5DHqEwohYROuVmHWT_qlea90BS5aUYcDPHlObK7upk8JozhmaWybl6DmfHhx5-lReSpAATLnJeKowql49-vkgAxNikotYVgUMz_AqfFLOZXwXOFAZ7IWKQetKmrwvLQlfTENFHLMGV3ZHjFyos5samW8qfIDqLc5kJo5oxqVuxORsWsKMOkCohkaw-5KIPXPal1qhQ1zWGDI-Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hvnx-exjSLKiQG3lrIR4NPTY_CHnyGXP_naCs9shTwY8rcturg5-j52Oh0S6pF7viIhhX8WsDDrkwNJe1-bvFS_gSkIqGWJaGmrnkyxAIA8WZ_6Jk-bHn-tdJaXn57rK_9J5rUe-BgskYLDbAWznkwUy0uWPOup_75FD66reoldUJLi6jXebzciV9OKw0CzcGKBOO1r6LHVqWyJ9BkgguO6kxmptJHTpkCmVDVAfhQF_bz87r1ptb19uieD_IrBCKmQlt0xHuKmm-zE3PmiFani9ZIgN-G0pgDk4YwlidvZ_fWSDVc8OAFGKMt-H5fLHG_UFPyhvJbpySXiVqmaj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEQe7aqVKfsj28h8VZp8h0o8uVURip84jqwvYU6rRfWGnyqWIV4Y3NfGCfI2loIgIiLN19Dd1kd5CrSNxKZvop9LDm2Rv3zVXd0b-1NN97HzMisSCU9XZtew4KvD3bemsGC54WIICsp-Pr0bHHTZwq53GdHKVS1gva-HG0teUOFmo-zocSqY7TR-i80yAqlEiJ4hdaUL0Lk9Nbbkcuq5sYV87piPGN2m4lQ5Ubaw-DwMyRe0dy11bSULcbaSy9JnFTytEPf_86s5hLXXbakHwwks7sB3nN-yKooWrWbR9CSPlQH2Yir80uX8xJ-c5gppbXfUC01vfk8u7-nypEPCBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oj4nqPH3MK43kEGCWDELeTy310EqWkYzio_ln2gIqU3nB9mX2vk8Y1O1KIx4225URoiWE-KbK85lgH12KeSmVVRaUxf0j_cTYov8z3yJ7hO-8Rf3kOZTY1leEjVWn54yHwZZF13Uucaank1HhKxqTK2liIR4-x3JYGK3u6QRjEvSd9alWYvyl6L2qBB0P0YF6WHIUM2HaIbWjm-43WNqLuEBxSIROMzlRoWuga3a_B6-zFy7QQCIxBWwm7yBdxsYK7XSlegByCkq3ltheD7HBp7Ftqo43at1A5HixltKGCTRnZ6Jsypn12rV5s4SYDoAybhDOu8sRzumRxU5Zme4zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzWeZJzD4atynay8CnOvShD47v97snpS7Wp7Tz-aJBzigaQpuW09_TcU1OkMgz7-HYvfuMOTc2v9u2TVg8WYCkMQd9HBnjAYKTLgq0SI6lf6HVmCMR8Zlqjm668wAJzR4wn-K5AyVgl4thJ8VNXrYnxT-7yav3jH5eckPewdD0NenLuR9xTxD_txT-wliZG_UIQNOyROVnM6JwfO8F7JoeFPpQq6lNPJo2peIu_9_VV17Q1FEWqoPB1ghcaJTzlp18RLdVCx7iNuMZ8pOD8dWZfHO72ircPLhFwAQqRdPe_CyfS3C57Y-b9yu3whceTwKpTzF8PjvBfyDhWNEYO_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=FDI9Kg-bpZuuaGsyMML7De1Yl_h4jqqQGiKX4ETus8Qk8sJT48NwwOd-5E0R4NZKhucSdFL1Z-DCLvpZ00BgM4y_LWqE2SJyFwJG6Iw6KVisZP-vNBFedaZv1WovVfURTWbKFCR4NqdNE5OOMSCHa-mGkzrPUyK4VDF8-3rhw4vE1dpLkSnxn_tYYOn1SIiOETrPuQsWjNYdyJewwheOVWtkNKmfxVs-PlnW-4zviFOq5LtQcswHyDVWXRsquyXjCRHLVlrWE36pUzDEs5yHBZCrtpmSk6747gyP6STP-whW-LUkzi6KXKM80jxFkdfKM9j5ThiPgxPvoCEXPIeuAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=FDI9Kg-bpZuuaGsyMML7De1Yl_h4jqqQGiKX4ETus8Qk8sJT48NwwOd-5E0R4NZKhucSdFL1Z-DCLvpZ00BgM4y_LWqE2SJyFwJG6Iw6KVisZP-vNBFedaZv1WovVfURTWbKFCR4NqdNE5OOMSCHa-mGkzrPUyK4VDF8-3rhw4vE1dpLkSnxn_tYYOn1SIiOETrPuQsWjNYdyJewwheOVWtkNKmfxVs-PlnW-4zviFOq5LtQcswHyDVWXRsquyXjCRHLVlrWE36pUzDEs5yHBZCrtpmSk6747gyP6STP-whW-LUkzi6KXKM80jxFkdfKM9j5ThiPgxPvoCEXPIeuAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=okSR5u2nd-ydWdS7zwxpEmTrh8rfi2LiHQmzA69BQKC6xSrSqvZUzhD0fYubuF5wLKojEZS4mBuKNVFlvDcBsm3IXpzZ-7q0G_LGtB5eih7-110fgHL_YFbUnwrk7d4S2UX9AuZ16JIpRhh9DCEj0He-_GDerWjv_7hvKRmMPaMwgJ2IEesm26HOTlVCeX8pt20NgpDOEs01DMy7Ae-Ls38tJATQd5YiADAjlU4MKUorQ1erNwKTCEqtHW6TkGlE2bvIGzd4jmBRtDNVCbHQ6jrM8vkdWaE1-ADid2ufE-WRxfGpLxPaRT7-UohTOa7cmIq9yfvJ1IKMzMsSB01EuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=okSR5u2nd-ydWdS7zwxpEmTrh8rfi2LiHQmzA69BQKC6xSrSqvZUzhD0fYubuF5wLKojEZS4mBuKNVFlvDcBsm3IXpzZ-7q0G_LGtB5eih7-110fgHL_YFbUnwrk7d4S2UX9AuZ16JIpRhh9DCEj0He-_GDerWjv_7hvKRmMPaMwgJ2IEesm26HOTlVCeX8pt20NgpDOEs01DMy7Ae-Ls38tJATQd5YiADAjlU4MKUorQ1erNwKTCEqtHW6TkGlE2bvIGzd4jmBRtDNVCbHQ6jrM8vkdWaE1-ADid2ufE-WRxfGpLxPaRT7-UohTOa7cmIq9yfvJ1IKMzMsSB01EuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=dcYbq3vNwtcxrznt9bcXGPfiUttritoXZhiBs1_bYeu8kQ8FRKj2Hj_k1JrT-CNLY1q6HS822Qk_CXsoZ_VPQvR3CKpXp6oERTwaYuN25dKr-ILeBDJud5gZCSvFFOOwEFZDj1Z1njRvb7cNtVzzEublezO9wZIbOg1HLl_QpLNJvTLIVDVbJk2iOXAdxtiSjRrNzOVmQ8xcTyQNvQLRTLbEgqP7MGNpiQO19poyFqEW_DHbWTvgwLynRXU6KyzeC52DC-E2BrKiC1ggT02lFLSGwGZCahBEg5K4_EQJiivAs_J5vAkoQLyHf0dgFMuYbHFvE7Q45wz6vT3JuZyt6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=dcYbq3vNwtcxrznt9bcXGPfiUttritoXZhiBs1_bYeu8kQ8FRKj2Hj_k1JrT-CNLY1q6HS822Qk_CXsoZ_VPQvR3CKpXp6oERTwaYuN25dKr-ILeBDJud5gZCSvFFOOwEFZDj1Z1njRvb7cNtVzzEublezO9wZIbOg1HLl_QpLNJvTLIVDVbJk2iOXAdxtiSjRrNzOVmQ8xcTyQNvQLRTLbEgqP7MGNpiQO19poyFqEW_DHbWTvgwLynRXU6KyzeC52DC-E2BrKiC1ggT02lFLSGwGZCahBEg5K4_EQJiivAs_J5vAkoQLyHf0dgFMuYbHFvE7Q45wz6vT3JuZyt6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=RLcdbqh9uXvPpAzStS5dk7o5OZxB5DpgWqacZg7XcHQy4uYVL-7XRRqqqw7Yidv41tb_b6WFH0nZCzvW1fEZ6QAtuTi_zXxGbApQ-bqFqFs6vFiLcniGB5sJMteZArXQQrK5XvvBab0bkrYrewyQ06ezirG3EMvpz9aUUQUq7DkE7sY6AQbwXky6kxZXqWi8Z0oJ07Y4W9RKwJqp4WeDX9SWUb4fk-_bmNDVCXusS6KwzdT3LBfttWazrCGyuMvpxRjZOOW6Kule_QS9CUd1Gf-psC-BYJCKriNc6923W0A4zjnVex1u9OjhLVQILInD0mj_ICdPi5Y_9QTRCVoN2ayDNISf001mCrUyhwp5NwTEj5-9qYNOV3s3b7j-SeZDEIh63quNqMkh-zU57Tp8ELDQaP-StTsTBtGQD9nP4eiW-OgKw1lnPBE0BDYmudisMq-WmAUUdklCmspmLdT1xxciByNMvIdcuGUnSsbqD9ZmoLAjW-pQehFZkVIHCyHXpe5fLh8n4zYAhD4qi7-wZ4lZ6pmqJGBj5zY3LDQQKdSmVctstxXnSnx56xx5TbE3XrVuNaoByTgO4u5m1EKRo5O-vkd-oQALtvHYnFcQNN1rSBmX-zeJXyHC4q77bwsGN5OZ6k8xZyRn_fQcSFH8-L4WjCuAQQyy9Nt5hr9yMfs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=RLcdbqh9uXvPpAzStS5dk7o5OZxB5DpgWqacZg7XcHQy4uYVL-7XRRqqqw7Yidv41tb_b6WFH0nZCzvW1fEZ6QAtuTi_zXxGbApQ-bqFqFs6vFiLcniGB5sJMteZArXQQrK5XvvBab0bkrYrewyQ06ezirG3EMvpz9aUUQUq7DkE7sY6AQbwXky6kxZXqWi8Z0oJ07Y4W9RKwJqp4WeDX9SWUb4fk-_bmNDVCXusS6KwzdT3LBfttWazrCGyuMvpxRjZOOW6Kule_QS9CUd1Gf-psC-BYJCKriNc6923W0A4zjnVex1u9OjhLVQILInD0mj_ICdPi5Y_9QTRCVoN2ayDNISf001mCrUyhwp5NwTEj5-9qYNOV3s3b7j-SeZDEIh63quNqMkh-zU57Tp8ELDQaP-StTsTBtGQD9nP4eiW-OgKw1lnPBE0BDYmudisMq-WmAUUdklCmspmLdT1xxciByNMvIdcuGUnSsbqD9ZmoLAjW-pQehFZkVIHCyHXpe5fLh8n4zYAhD4qi7-wZ4lZ6pmqJGBj5zY3LDQQKdSmVctstxXnSnx56xx5TbE3XrVuNaoByTgO4u5m1EKRo5O-vkd-oQALtvHYnFcQNN1rSBmX-zeJXyHC4q77bwsGN5OZ6k8xZyRn_fQcSFH8-L4WjCuAQQyy9Nt5hr9yMfs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=NnVGP6l4iMq0sTU4FUi_9fy3-jb6UUtvrjHyO3HqlblDJAmIYhw8PdeiY3fyGSL5qKIvL_0XCQ8ZSoMVKwpJPI9rH2FswLBqNPb_iuGT8VNxx0DPDBa5gydfx3ioO96tz0okbxZW1y9zO89jGLQaTk3knCsaxaLqmRtVOm1Uidq-OKOmNV0mUbnzq0PjUu-v-MgfB4T6s7wd2g-uK3cOsaIZWH4GPASneG-a15MwV1b7Thqme1BKv6G1YVGTHTLxS3hoyPPQWvy5K2yQl-K68Rbl47SdJ5rDJgQvahuUJPQiMFs8d9qTduosxAcE262Zwq5wtuScugGUSIK0yjh6dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=NnVGP6l4iMq0sTU4FUi_9fy3-jb6UUtvrjHyO3HqlblDJAmIYhw8PdeiY3fyGSL5qKIvL_0XCQ8ZSoMVKwpJPI9rH2FswLBqNPb_iuGT8VNxx0DPDBa5gydfx3ioO96tz0okbxZW1y9zO89jGLQaTk3knCsaxaLqmRtVOm1Uidq-OKOmNV0mUbnzq0PjUu-v-MgfB4T6s7wd2g-uK3cOsaIZWH4GPASneG-a15MwV1b7Thqme1BKv6G1YVGTHTLxS3hoyPPQWvy5K2yQl-K68Rbl47SdJ5rDJgQvahuUJPQiMFs8d9qTduosxAcE262Zwq5wtuScugGUSIK0yjh6dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=L42KUwiEaT44oUyNHlNJwjad88VvIiHva7jcRHWt2lmKhtwZl_LS0DQfzBzt8GE942QBJLaO9nzp5c3fxVmsBHRS-pY6wEDLTZr_DIexFUfU9t_bC_mR7xKC9GZkWFYLS0LqHRslUSSPrCEhA-02t7AgHvUru5e4bTBTN6Ohv_nZ_c2mTYLhQOpgmHb2SAPwsXcQPolpnUvPs1hBYNZqckVP7IVEyrW4y0HgPJyfDexAPfrVoZ3MDzuEuIJfQtc9ajqydKatcUW2DIbx34n9mfnZmP3Ed-D3AWbq800IVca_w8WHLM8_BvCWZ3I8kVBzDo1hlTiltkpdv_bWchcRmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=L42KUwiEaT44oUyNHlNJwjad88VvIiHva7jcRHWt2lmKhtwZl_LS0DQfzBzt8GE942QBJLaO9nzp5c3fxVmsBHRS-pY6wEDLTZr_DIexFUfU9t_bC_mR7xKC9GZkWFYLS0LqHRslUSSPrCEhA-02t7AgHvUru5e4bTBTN6Ohv_nZ_c2mTYLhQOpgmHb2SAPwsXcQPolpnUvPs1hBYNZqckVP7IVEyrW4y0HgPJyfDexAPfrVoZ3MDzuEuIJfQtc9ajqydKatcUW2DIbx34n9mfnZmP3Ed-D3AWbq800IVca_w8WHLM8_BvCWZ3I8kVBzDo1hlTiltkpdv_bWchcRmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6sidjFhCtgKG5lIARJPzk2NwGDVfF6b1-L6h5R5g30RYh9gl1X0hzm8UQrtaM8XDQ1Q9UfSfmCE5BtSA6QKiz3tvQak6-q9F8OqrcnO3N8Y0o5mpcTBk-Rhe6bEBcBTDRqJTETpF01Q2Mu-pAxECbKZBHPImGOtC1fAoLJIRR85AUz1Y-7_6KMLDxXfrr-v5Tu5mAJoSlL3c5k-ycA8lZR7SH9qB-NKzCkmzr1k84Xaduwu4_tY7DaFJg-e3kVy828Wsx3tNiRFX6v0exWvlrypcFx-qb7EwvMMDfryLEWXhyE1ihlSWkCrhAl7eoYIx90xP_PHFq4kJfOMrNH0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=kBeoYTAUe45-WJ9nxiNAoWpXciernyq3YQ-MTL6ZiauRn3Z-BLi1QyUesez5nRj3CzIBKIkFKAM_vUPnWNEq9L_OwPr599cr-K0uA6zWowKShBr-rMPJi-3Xl04JNJjdxoVjD5g5ryIIoD8eIJvC4iIothax9PKBte1PlEw-lYf5RiNwDNy4CruAn4EBShavEBHqTTKCC62JIXK1YwIv-IeNov3QnXf56fvkuEv0xnSP3HTnbiIEQ6E6XHlLoqTIWeY6aWFW62O_pY0oyC2O7BxBXdqVglxFD9txIDswdE3MW6Z1b26WXpiqwd__waPqK3kCm6Pzu6IQt5qtXQMiJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=kBeoYTAUe45-WJ9nxiNAoWpXciernyq3YQ-MTL6ZiauRn3Z-BLi1QyUesez5nRj3CzIBKIkFKAM_vUPnWNEq9L_OwPr599cr-K0uA6zWowKShBr-rMPJi-3Xl04JNJjdxoVjD5g5ryIIoD8eIJvC4iIothax9PKBte1PlEw-lYf5RiNwDNy4CruAn4EBShavEBHqTTKCC62JIXK1YwIv-IeNov3QnXf56fvkuEv0xnSP3HTnbiIEQ6E6XHlLoqTIWeY6aWFW62O_pY0oyC2O7BxBXdqVglxFD9txIDswdE3MW6Z1b26WXpiqwd__waPqK3kCm6Pzu6IQt5qtXQMiJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsgitDIJbnSQCqdL95XDtMvgHz8Q8jFTzkpi_Vv67qDsBW2rntIei3Orba6j-I68CknYbeCogdMd_lwJnOt6B6KNkscE8myb5QXLsnQW4-0bF2cQ6GKAnIHLwI7PvggTcrXsf3FPSKwwtebVawG0kT-UycvHJ7XWvvqwBJf08x6KAtEuM-8_kZeyg_a4Q5tFjA8JQCD34s0X95x3q2r-TKpd9aDQuriKJ2R4U1DA-2YP8R-gs9KfcQKKzcrSKq6wk-lWt6IFQlwDhnQhYtxiT90cgBkqUFGS0dN2DaFOEULt_CKf483RV5KzJZHzULEeHX5psoARDgPnuaVtKnLAkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5L7-HGaF6b3gXpEhR99T0AVnhkk8eHLy7kMme2_TAaLqgasBePFtOy6YWwizP3tQT0c5dwj1zH9B3NDIg301nXpTLnikOhFRBh3ZfDCBh7L7-XO_vafDyzmp3px6xDhpMs2q71aBVgiyEvvblo9A8CR15K1EFsMb7l8jRDUysGQRh0sRFhyIZcuBJAye3K1XsYY6g6WU_LsqUXDLEY79Ddm2l3BJe92wZ4rKVlltv-3YyAhLzZOxvi9dFJF5VAvSxC-Z_zzQ1XADPU40vJGitvpR3nnDUrR48dZl6FwJK-GIDXNJNMW8IUuU9hxOnGZACOS5X2oqk5eXmD3E6We0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=MiKmHOzkwUBlLyFsKW-M7W4h19uFIkANzF6XAEp9Ogx5eMHgqOnAZy4bCGgCENYm01JoHNttwJyyh_iMXUM-XC2rK_kvbQajeQfGB2JxG0Xzn9sSvtOwHFB1LiGlVbNRkhFPzcvEMRL3wEzG523QwOJEXN_2tKm0q9sYtUro44O2o_cRSaXOnW4-mNxO0myCkJaFAMydUMbqoNqZShuHuyu8yFpBQ8VbTA3nQYdAqZNTTZU2CYgC6GS-0j0NeS6Vv29mirOkII0-8PycJC9WgVLeFDwE71_uCXp31joJzRTIH-6EmsSU8j8jO0gvK4Y5CzOEyh6rEPRio-EXH2Mkrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=MiKmHOzkwUBlLyFsKW-M7W4h19uFIkANzF6XAEp9Ogx5eMHgqOnAZy4bCGgCENYm01JoHNttwJyyh_iMXUM-XC2rK_kvbQajeQfGB2JxG0Xzn9sSvtOwHFB1LiGlVbNRkhFPzcvEMRL3wEzG523QwOJEXN_2tKm0q9sYtUro44O2o_cRSaXOnW4-mNxO0myCkJaFAMydUMbqoNqZShuHuyu8yFpBQ8VbTA3nQYdAqZNTTZU2CYgC6GS-0j0NeS6Vv29mirOkII0-8PycJC9WgVLeFDwE71_uCXp31joJzRTIH-6EmsSU8j8jO0gvK4Y5CzOEyh6rEPRio-EXH2Mkrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=QId60VRR-d-PNMuV4p1DRvccgLBWao14SYQgJ5fr_YEwDeusPrZGaRoRmpyWFByFnx8O_gmuHOQdENFL-NgOAmsJpwJpAGia2v5ujrUV6LXgWXHIzCzE2LBkY-KoCxKSHEB0hwYwEbpXGMBmtc6eELMgFoXKV4JFIiGxNKlfrBycHwwyKViqyyWY_7h_TbvssDYfl8MNb1WlqMe17w4F3N48O8Pji5lAv39oPUvo_p4v0lpNC4Brz1T4xWJu-FQZ5V8x44UFazwRjGK9z1_aVphRrjaO6_36OQ4qBpUJf7as7AWVLQv6mMHXFOE_caPq7rI8a8akNhbz9-_BctALSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=QId60VRR-d-PNMuV4p1DRvccgLBWao14SYQgJ5fr_YEwDeusPrZGaRoRmpyWFByFnx8O_gmuHOQdENFL-NgOAmsJpwJpAGia2v5ujrUV6LXgWXHIzCzE2LBkY-KoCxKSHEB0hwYwEbpXGMBmtc6eELMgFoXKV4JFIiGxNKlfrBycHwwyKViqyyWY_7h_TbvssDYfl8MNb1WlqMe17w4F3N48O8Pji5lAv39oPUvo_p4v0lpNC4Brz1T4xWJu-FQZ5V8x44UFazwRjGK9z1_aVphRrjaO6_36OQ4qBpUJf7as7AWVLQv6mMHXFOE_caPq7rI8a8akNhbz9-_BctALSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=gjYe2fEpjMAfPw174nKBa7mdrY8ZrLclLuWQbxg8LNMbTqt0mkd39KCFZTZIc9VryAnOSlUOKg6_DCwrBhQKM_UxgKVLX0e-64xrxqU2qUPO6CHMoWqPuf4YtEjgMAakg3wRsdOr25QnRrO5mmbP9it1j5LiU5UFEHhO1O4TzyKyfXT9vfjHT9ZorlTUVFimnIywHZ99MfYVDxft6p6UJ05z3TIIyfLfAHJSD8cwgfGSE6oKwzo-ih5Jr0SyTfOMSDeGdY9zwYw9K7JbttH5b6emY1W2N_4kii9KVpaqRnknR2S-SecdvxnLHAZuSuPIGo_ijpFui72phxWtqKl61Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=gjYe2fEpjMAfPw174nKBa7mdrY8ZrLclLuWQbxg8LNMbTqt0mkd39KCFZTZIc9VryAnOSlUOKg6_DCwrBhQKM_UxgKVLX0e-64xrxqU2qUPO6CHMoWqPuf4YtEjgMAakg3wRsdOr25QnRrO5mmbP9it1j5LiU5UFEHhO1O4TzyKyfXT9vfjHT9ZorlTUVFimnIywHZ99MfYVDxft6p6UJ05z3TIIyfLfAHJSD8cwgfGSE6oKwzo-ih5Jr0SyTfOMSDeGdY9zwYw9K7JbttH5b6emY1W2N_4kii9KVpaqRnknR2S-SecdvxnLHAZuSuPIGo_ijpFui72phxWtqKl61Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlpP5z3EaQ2FI6s71aCyv5CPLFAVLIGSCXIPNa0jhQ730QSTi4VIZL40blwHlYHa_v10Doov0SVbWR4XOq4LD0raPd1YZ7XKN_A1gz0afKLBmJ4ZNLeyanjG4xvx_kddgnhpKaILVcqxBDcpGlSiiFd6fTEIAyc-TDjMcqiXwzoQp5etiHOBaP72MU4B0aKlJS52IOqQ3TZ2z3yiXbYkHyKhowurjXxSaIwYFmOQVMMQ1Fx_Wkm8XabNrS7dsOBRzqs2t9OUFMDAK7nCzB2OkBE2_E7sUNSX3uHi85WsI75tBnINeUVqMdMwihxxOTeInmq2QZHiboo4x9ZQjAa5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=nAwvXRusl31Lyd_qtb55KF-rz_cq0bWlObjcIjQSVXSpJlXXykTKd-zRPe0dbGGV16Omb6dZ8HzTGhmMk9CCwq0yUMSzvXjOM5oY0rESvfEtiROqVWj1WF26A2p5628th0QzzWd9m5DSnyOWhd_OWrjk61bH84FqZnL4auL3gcnMoeAp76VbkXtAVHSSAMcfcZlrPRv-hb6VWXiLCy_r1AdbrwmqzG6MVuEknhZcKwPNpWsm_tczINfDbFUO1dHnwVN_FlBA0qA0i6XBVlEf8AxaZPgApUi7gemnisQ-XlYGmg4ejNLpVhzgoBQz5ZHLoeTVwObkBIK1o5UHZFXm4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=nAwvXRusl31Lyd_qtb55KF-rz_cq0bWlObjcIjQSVXSpJlXXykTKd-zRPe0dbGGV16Omb6dZ8HzTGhmMk9CCwq0yUMSzvXjOM5oY0rESvfEtiROqVWj1WF26A2p5628th0QzzWd9m5DSnyOWhd_OWrjk61bH84FqZnL4auL3gcnMoeAp76VbkXtAVHSSAMcfcZlrPRv-hb6VWXiLCy_r1AdbrwmqzG6MVuEknhZcKwPNpWsm_tczINfDbFUO1dHnwVN_FlBA0qA0i6XBVlEf8AxaZPgApUi7gemnisQ-XlYGmg4ejNLpVhzgoBQz5ZHLoeTVwObkBIK1o5UHZFXm4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=CL_JFgMSgAtAykFSO-hNBuNHxliQLEvkcoQFR8mbosJn-eitv39OLdUKVIsWCSmhvdN3jd47MK2hXm9HEPd1a7RhiSNprJ0WUqc06AiwsYsORwQ9_nkN8GfUPAfAkanUFgGy3Bigx2swLSIoTK-IX0_aHpfSxKh8UUIUzKFYyoGY7F-GyOCrRP9jV9CEeZ1ZZlf__vmsiWfHwTC9-RMnVc7hqZdsygMYcQcLPG9uByucf09CLCYbGqw6nxGUerSnBfPbUKx49eOK-QQv5bAUItoaAJoFplOJq68GxVNcwVRZHhKQ3Xh8LWh9dWLkCrcYcQfRy1WzyqbTAsaXLJLyLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=CL_JFgMSgAtAykFSO-hNBuNHxliQLEvkcoQFR8mbosJn-eitv39OLdUKVIsWCSmhvdN3jd47MK2hXm9HEPd1a7RhiSNprJ0WUqc06AiwsYsORwQ9_nkN8GfUPAfAkanUFgGy3Bigx2swLSIoTK-IX0_aHpfSxKh8UUIUzKFYyoGY7F-GyOCrRP9jV9CEeZ1ZZlf__vmsiWfHwTC9-RMnVc7hqZdsygMYcQcLPG9uByucf09CLCYbGqw6nxGUerSnBfPbUKx49eOK-QQv5bAUItoaAJoFplOJq68GxVNcwVRZHhKQ3Xh8LWh9dWLkCrcYcQfRy1WzyqbTAsaXLJLyLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=g8ZxSJhk6OrC3IkqQlqly8JCm8l88cNWlTPy5Tcq0yj0zzggkNBQUhva6rgFxcS1yZblNMvP5vKx_9SP14zZefxqIGZGYfOHDIv1yMVOcMRKcVVFcJfNlKExr_GLujWzNuof3z__ZJCTR2VhWH7gftjcFSSZlQVosPNByo8S3A3AJFjlm09jXNFh-O3BJ7wNHOQ6D3ynaf3hRKpXh_u40GxKPkLdopG48R3A-tqB-SiqZUHD-ifzK6Q4LgTYgU9FA3OhQKVV_5XegGReIYNFpfV10td-RwlOKAN5XppKYFxh0drVSR-SF4urwLj8NrLB6d7DMzm-ED2CdT5neySc0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=g8ZxSJhk6OrC3IkqQlqly8JCm8l88cNWlTPy5Tcq0yj0zzggkNBQUhva6rgFxcS1yZblNMvP5vKx_9SP14zZefxqIGZGYfOHDIv1yMVOcMRKcVVFcJfNlKExr_GLujWzNuof3z__ZJCTR2VhWH7gftjcFSSZlQVosPNByo8S3A3AJFjlm09jXNFh-O3BJ7wNHOQ6D3ynaf3hRKpXh_u40GxKPkLdopG48R3A-tqB-SiqZUHD-ifzK6Q4LgTYgU9FA3OhQKVV_5XegGReIYNFpfV10td-RwlOKAN5XppKYFxh0drVSR-SF4urwLj8NrLB6d7DMzm-ED2CdT5neySc0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_8XaqE7VUR4HGCRofLl2jFsXseaVjTYhblknZfz37FZzkGsSZvhApBCRKc_YV9n0cPRl6gV-UG56RLEPESYjM8aPHp7XBOnSaBHMB9hbd1qcWDJ0LX9kWvRKLcOdUcJzNDH9CXTKK68JRuHAe1m-sWIg4g8qBf3Q33pBIkpzZp1sOPyORjE_GnruEjJYM07nBpYUJPkksUIANQ1MKHkvYMeZYi2Vfvb2IFDEgaWE9JzhBRk1aFB0Xy13bfOVk6Mp1RsYmvrk8taMyeNR-gY-HXRVrO3ESE0Yy4qXFbhFdatTOiV7F19_uhSJ4K98NmsUk1RmuzHCChq8gqj8Hj6FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=v9MwcD-g_sPrO3yOPAlvY4FIgju5Xirp2d1tKipA1sFXC3o91BTIaXzYWrY7Qap7vusPg0zl2KNwWaKkZuHjEvfvSRFtWFVx9qMWeDHtYzX8X6hh4XP0NQgDbw4JDYBWxJMUnUFVBPij8wJTSPJwwtr8L92KXvxaU0CbGGt6ZqZM5SFD22G_GrDDczKQR7yn9_mCQ52T88QxtywQfcKMKAD8zXVZ5JUYTuhko1Krjl3I9OybBJXCbyx2V14v1SO1OlphDcTLsRH8GZgzE5XMmQeM-1zV02My1Az8NPBKMaR0LeHR-pGpR7kL-UCMrdZUda0bDiOh-z0ytspHhGKYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=v9MwcD-g_sPrO3yOPAlvY4FIgju5Xirp2d1tKipA1sFXC3o91BTIaXzYWrY7Qap7vusPg0zl2KNwWaKkZuHjEvfvSRFtWFVx9qMWeDHtYzX8X6hh4XP0NQgDbw4JDYBWxJMUnUFVBPij8wJTSPJwwtr8L92KXvxaU0CbGGt6ZqZM5SFD22G_GrDDczKQR7yn9_mCQ52T88QxtywQfcKMKAD8zXVZ5JUYTuhko1Krjl3I9OybBJXCbyx2V14v1SO1OlphDcTLsRH8GZgzE5XMmQeM-1zV02My1Az8NPBKMaR0LeHR-pGpR7kL-UCMrdZUda0bDiOh-z0ytspHhGKYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN83q5dJENWN-oSccKf3bhBNTRto0BHQwO8r5WIgBroZXaksmq3Na4WegYQn6skP0RWFzAwdSsbfcJNBdbVgShIlWSuGekJB4jdE_9EypCecOqVtJah19ZB7jY7cIZ1HyNqmsV1VDM0aNXRkpf3B5ZKNZvW540J9dbKUnVVN04WUCdYoxm9x9La2be9Qqj4VaCHrsEqWt9_Y48QRPxAt4BykdPfLIFCjl9wtObM_daUlhNQYn5BOqzXQWbWjiT75eweuFmucM_v49aM0uTTgyfnT3m6Uwh2vAebJZyz40nUht9EPSxgSqpNIk5qElV2_fXSAEHXe-kOVWw7ch2DNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=brOZ-V5xUbq9yTQ-wMP1Shb5dBH0VwzlF8Ob5QPKHRB14O5me4-NnaMsD_nXq70mDW5sJ0WP6LdvT7PdjLR7nWXYF7CHuY5JXkYKBQLSV15PQDGbBRp5Gque4I0s3xP-Ee0-fpUtpvH59ZLh3CrKehPnvGrrtZItVGIktMDN39sR3WCkA3Jup_26nEkWIMAttVx8n3rM10ioi2Gb_A-8zaAkEnjVrH_oulyKtuolE16D7Q514hz8hkZ8IZcP_uU2G3jBrVCGO3EURwzEDpVKFmPaHc0Z2xdhdKQB-FpTwaUbILhPzOke81RAod0TDKVTd5Auh2j4frh_biTRgIJyuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=brOZ-V5xUbq9yTQ-wMP1Shb5dBH0VwzlF8Ob5QPKHRB14O5me4-NnaMsD_nXq70mDW5sJ0WP6LdvT7PdjLR7nWXYF7CHuY5JXkYKBQLSV15PQDGbBRp5Gque4I0s3xP-Ee0-fpUtpvH59ZLh3CrKehPnvGrrtZItVGIktMDN39sR3WCkA3Jup_26nEkWIMAttVx8n3rM10ioi2Gb_A-8zaAkEnjVrH_oulyKtuolE16D7Q514hz8hkZ8IZcP_uU2G3jBrVCGO3EURwzEDpVKFmPaHc0Z2xdhdKQB-FpTwaUbILhPzOke81RAod0TDKVTd5Auh2j4frh_biTRgIJyuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/henBJNLFOqSWwzleCv6FBElUhCs8Z__ZXkJzMkcnX8sHpMW2lvejgw3X2NL__K8BMUeIPIG8IAA3VJ_ApfS335gLQgetFW0gEXZfzxV8U9RjbVzjbWIL2VdAdNv2LbuSrlRC7Spejok9FC_3zrZsycxswfPinqQkhoS9kIVn4hs2izuc_0HFn3Q-ffrRZJWVrVpgea32PfNyLEBwgY7LlwtQuZcKOhXs6g7yy8X9B2HZ5zO-COF3thoBFBFYgDVlGgPdxO8wnn9jMy9e2H6P-i2800UV94ih2xq-vaAbUCWxWzeU3Jlsi6r0V0W1jDnKprpXueDnMmLPQUa9mM6dIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=ikRvNhOAadSyAymheUwVISN3iqolxlGUKlFL6BfdqiGFJX7Qw1D7Dz7W3BfshaWMFWGm3WPNe_0txgNOu3QXGYNy2qmm-5oSE7qu8WcotlRFpP-el3YWJH0Suw-k6Zo9LeCRY7JAtoS013pO8hJj809OxW_p4Hb9hAx1o5fnvGlogsakuhKZhLZ_WSANSO8b6YriKZ_GXLSLWXalyKWz2Ztkw_b5Y6sdCIiQ6L1ny-2cVRUvLJUWLDZqQScPCU1cG27itMyKixsg3Fz73iMlFenK9NVB2iKhKF-ACcqssvWfJramtsTRVYUax1i9Y8vnbg518pjThA9mcv4tLaZLSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=ikRvNhOAadSyAymheUwVISN3iqolxlGUKlFL6BfdqiGFJX7Qw1D7Dz7W3BfshaWMFWGm3WPNe_0txgNOu3QXGYNy2qmm-5oSE7qu8WcotlRFpP-el3YWJH0Suw-k6Zo9LeCRY7JAtoS013pO8hJj809OxW_p4Hb9hAx1o5fnvGlogsakuhKZhLZ_WSANSO8b6YriKZ_GXLSLWXalyKWz2Ztkw_b5Y6sdCIiQ6L1ny-2cVRUvLJUWLDZqQScPCU1cG27itMyKixsg3Fz73iMlFenK9NVB2iKhKF-ACcqssvWfJramtsTRVYUax1i9Y8vnbg518pjThA9mcv4tLaZLSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzjIL98zfz3wDa-LkoyFO2i2VSgJTXOtAVmhbLcyZae0ZSKX-vABjgYOh_j-a3sjg9hGGQlC9b5YVzpkMCgsZoRtaGpUZmuS3TJ3bE1e1bXN0mDPdnl_YlKYgQnqu8NdiLAue7KgKLYhxuHZjJVkBmtZVgESJ5eAX13M1iqtN34OA_baUYI7dA9-EYlGn_crAAKIBDxA0XIb69ULN4giCUNmks1nYt4m9jzmrICK3jJXRM0dMj2_MbHmAuRjL3LEvlDKGKaE53US2gx8WCRbXuJXHo1t3kB9NUhWiFtvkU035JxkZ5EbONeKcH1Ij1ZC9HwMFm1oKWW5y723ftHdrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dGPei3wnuFCgndz5cl8fZkMmC45tHtq3QH73lS43R4sB6vEFdumYP4zTmDbKHW1n2RrvzauUNP5kF-fObtuuk_C_wa8-3SYpDylFxZE3ljcDwp4Yi6YJVVQpTzL1quW0uQlYehVeob3qZilMXRNuSwBrOHEo1uXj3MhsQhXYiGmpdj8P6g23oL8Vp5ZPKuGPOI4PP37aKqgETM7Fb7DpHEy94dxpk33Ouo4QSskKcgcBzB8RBYTK06uC29pgOLtMRt2B0_-TFWLIW1IW3R33hPUjqNqIvKkx5Im2NXGTHrwgbxdwdDcUQiiqZ1oHfVZd2kfZbPIiT6TO7-taE1Avnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=a1rw2ib02-__aTChblTf_QDzDXWoeek-daE0FXvxSdekPZfJ4OLfuy2AcJGB8BGWVMlWmjIZv5dMHq4F0HOVa1LYqfvD3BGtPPed1NwdrHMBPYZXwMSQihHQaYtT0n0wKfQy3dL1zf01GF18RAikdDErZjHntjAh6E6AZlUFbAnnwFex-jAgAFjrtRSlvmMObaEWFxtK3aK85GP29ppPbC__nK0B1qLg4MCwmqJ7j1OaItMMBD37cW2Y1w_pAkIntAYUhnbU9mbG4bqL_dV696ymbgJWfVFsjCkT_ymELrYWrd1eNQchPDoP1T35Aap-I6DmLnZfsta2tGvFreTxMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=a1rw2ib02-__aTChblTf_QDzDXWoeek-daE0FXvxSdekPZfJ4OLfuy2AcJGB8BGWVMlWmjIZv5dMHq4F0HOVa1LYqfvD3BGtPPed1NwdrHMBPYZXwMSQihHQaYtT0n0wKfQy3dL1zf01GF18RAikdDErZjHntjAh6E6AZlUFbAnnwFex-jAgAFjrtRSlvmMObaEWFxtK3aK85GP29ppPbC__nK0B1qLg4MCwmqJ7j1OaItMMBD37cW2Y1w_pAkIntAYUhnbU9mbG4bqL_dV696ymbgJWfVFsjCkT_ymELrYWrd1eNQchPDoP1T35Aap-I6DmLnZfsta2tGvFreTxMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrUoho8BREcIQyeaC-X5v0mi8ON8EKeiERCMaFLHXu_TngkGYkMR5AD3xAHateP7LRb4Gvx5ceBGPff-zqIF73voPUO4Vw31AkOEuSfvIWfT-GhBidpXRlWIL-HK-YEDCcphDnhJKV8Ij6nsuhEYPjEKjRhyIF597HXbrCBOQAqTklWkV0uu5t-_tlH9ixKLEic7BOUnS6Th2dWkBHVK-wACauWgL2k6uZD-n2z3QYulVLQG8PKB1OYFugFvUukJfo6T_MPsEY07CsKV4zMFOShBRHd8fiSyx-cG6UUKTPESBAyxYU2NIYtTt-OsAKVTe9SpgPFLeZndGw-0cebJsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bq-rfKfJLK2HAPDOcgXxHJhFus8euwH374DABWvMhC9sffcfv4_GwF5BZrRzsTGxa-nsNVhMw0hfSHuZYT5MFuGT1bxfx0Fd75mXrNLgDZ9zNEPhQC5LifZAvffMDSuS4M9-rOWKqgXxZxVPXZf4SNWBlwAY8hIwYh9JYVeRFgBgLwx1iWejJJIMkogmAdMfIrhMZCtvV2OiKmAmJ7oSxGH49yfeG-tFAtnDYuFv590Psx7VTeTudUcAo1Vnv0F3XfZKFqFKMBlexcrRzxdZxmBHPfs8YjHepXwTNiW9yKA7eZEokruUA2fsSgKSlZwlq21kofXQu6nY5Wu8FXMBvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqyFZuPTyTktODlo7gokhfhKZW3-Jvwl9f5AWkL67WekfC198Apj9G0Gg6g9-qam4vEws-y06EIAtUbl6BoL0a9mFKWOLJb70UIuVV6p7jIhoVfsIe_dUkDe8BDSOdvqJ-MCh6RUZHWX6wvjnnHYS165zcqzamvUhgliDVWmYg26Kwzmd7twSPsA3V_A-UoRYqP3a-9RF6rbN5F5PSI57uydPf_KbC0bs6KU-QWWlJi_P9zuffAf-jqv2_pRUlcwy63p0mYuYxPsF12hmxp9cG4ciInihgZbLISCwVVT1da8shg_PFQSvuSXshvKxFcjStynJoRlsvCv7RdFlsTMbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-y6VkZwLbAnGsT158KRx_VPiX8DNS0N4Lq5zt2Pqh7nu0H7vaDk9gl1vT_vZO2yG0Y6G2q38R_HVprzwEHK_K9LgydzH5dWGMPwTHfKFmhUtSwFvK1Fb2uIC2NbuCUzqok-nVF-Cx04FWU__yERy4oa05XRczAKI78UF1Ll0G9i9XNknWOmkOmibe5hO-NJEAyJ_kl3PNH_UDXCHIzLMQ3qIqFKdtMMLEopoy6nAvO4etZKQ6ekCM-DghfAQRbUG-EIFN3WZqQe8kobbnMoSUosthsG_6a9VdRCibeQYRkIWXQ7x2Q_b68dHDPWZWfgMZ0LAy0arAwOFIT817NM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVvCDncWEzUHa0JNVCV2lAbKzwueT60JCEyQi7qOWOD9uQg1uAsCr2LDgqgEB57PT6n_4GOZEKsoPfFc5nkrlpz77q1avv3JPJt_3oOrvF4Ai_MI84p7yhhTQRa4m4OycbSnp5AGX3BNQOWN32DE4gZO48CYMyQbC2avwi96HPzxr-zspabqCOqCmjVGAg55S-mMCASD2dhzAqBtHu99IopjwU5z0ISO1kyA6wByPHteszYNPDdnBzhODrmetEec8Czf5LvnmkJTjYN3TKRyfEnEcpAskoENFoO27n1jG8S99YEvf5ooH-6OMc_Ngd4rGOsy8S0fx7ZaM-jAMnQe_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=fmDVX_i8mn1wFtRkf-ML8zWh-Q1g0uBrPPvpVjiSEae7NTv8GmjUtzHbECy-p_zImgETUAhcJRBiOZHS2QHGeD0Y0KNV9oCfGDY6_jUCtIX85Qgal2z-DehxppPf1qg9RqtV4Ju8DsSgLD_8fIaT9hn0ZsxIAlG3jal0zs7pS1ujveG5Fb-1Q4NiH2fg5HdQ9-kYhULdPKpkSHUNBqGtUYF_4iTEaYgAEUMrLje_-6Hck_a9syP-BsJu9XyM48ayIfRgqv9Dw7VXkPxpZFDClbwVJmSp8mboMfrV4eUr5NjCieWk9g8aJDOqUzqJl23NgyDfdDAgYjXwa0ISSIRhXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=fmDVX_i8mn1wFtRkf-ML8zWh-Q1g0uBrPPvpVjiSEae7NTv8GmjUtzHbECy-p_zImgETUAhcJRBiOZHS2QHGeD0Y0KNV9oCfGDY6_jUCtIX85Qgal2z-DehxppPf1qg9RqtV4Ju8DsSgLD_8fIaT9hn0ZsxIAlG3jal0zs7pS1ujveG5Fb-1Q4NiH2fg5HdQ9-kYhULdPKpkSHUNBqGtUYF_4iTEaYgAEUMrLje_-6Hck_a9syP-BsJu9XyM48ayIfRgqv9Dw7VXkPxpZFDClbwVJmSp8mboMfrV4eUr5NjCieWk9g8aJDOqUzqJl23NgyDfdDAgYjXwa0ISSIRhXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=mx4P1kwSeU6CeaBqZsKqsO55bqtvS_1S_5PoYxSazcF8WROlgErhg-O1T6wNnrfyTQxw2U7-k9YHGR1jCHqxKkMsj53CgNfk16yzZrKZNM6RR_bSvc2ZvLSWMyzBDglx3Tq_XkMGT4sYMt83OMwLn4RX-CkksFk4NsvmlrG4wH3Sm9pQ3pggTUsiEocbd8xPNYQ7iRRfNgDhZ9th3U4-nIJb-5W-cOEzD3guiBozLFhqVd-NLAoTYXsZ5KE1fd8ji4Kq7-6X7CnHYGFXB0pP_uk98KDaeKYFehFpZUlkUHB5rwiut4sm70cL_zKfKvOmjxtG2Ne_I2nSMysvd2usYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=mx4P1kwSeU6CeaBqZsKqsO55bqtvS_1S_5PoYxSazcF8WROlgErhg-O1T6wNnrfyTQxw2U7-k9YHGR1jCHqxKkMsj53CgNfk16yzZrKZNM6RR_bSvc2ZvLSWMyzBDglx3Tq_XkMGT4sYMt83OMwLn4RX-CkksFk4NsvmlrG4wH3Sm9pQ3pggTUsiEocbd8xPNYQ7iRRfNgDhZ9th3U4-nIJb-5W-cOEzD3guiBozLFhqVd-NLAoTYXsZ5KE1fd8ji4Kq7-6X7CnHYGFXB0pP_uk98KDaeKYFehFpZUlkUHB5rwiut4sm70cL_zKfKvOmjxtG2Ne_I2nSMysvd2usYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=oMmYeJb5bjJ5ByppALH_5OrhA23O07ekSMTfduUdPx6IsMQRsXP89q99FQqS1qwMsb_vcVf2D4DKQuf_b8HVj2XFL1oEpuRXdncScH9JXDynC8iuMfEIedPlpmaBynj10TnUlE6vVLY5RQfHB7qAKA_zBQhCdqdupYWllEpo7Z5PTEkU_Ssk6awF7nEeAWu48tybPz59_ks8lPOPK-IRcQOYQiIVIsHGdwZbO2pcqfN2auG3nnRtJISyDq1GwAwWWq_Z6gkxrimbjF8BfdHwuj_8eSCYKBtPeLaUUEmmXSwR9qm59HmSsZWKI3hxra8CUjWDHX0Tm1a-5Drmv5ahFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=oMmYeJb5bjJ5ByppALH_5OrhA23O07ekSMTfduUdPx6IsMQRsXP89q99FQqS1qwMsb_vcVf2D4DKQuf_b8HVj2XFL1oEpuRXdncScH9JXDynC8iuMfEIedPlpmaBynj10TnUlE6vVLY5RQfHB7qAKA_zBQhCdqdupYWllEpo7Z5PTEkU_Ssk6awF7nEeAWu48tybPz59_ks8lPOPK-IRcQOYQiIVIsHGdwZbO2pcqfN2auG3nnRtJISyDq1GwAwWWq_Z6gkxrimbjF8BfdHwuj_8eSCYKBtPeLaUUEmmXSwR9qm59HmSsZWKI3hxra8CUjWDHX0Tm1a-5Drmv5ahFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=K98UUP7yKl8_Rdhc2QwfJLpU-QygULkF-CKBa20MnFlFIJUcDG6ZAkC15g3nf04tgSalw7UJ87lrXU9R-Yct6Sv_cN0gIh2xN3EOzAmWUoufv8Ezhs_4_V8KOFwgO82EdwTQpQ0wrYKWN4cT_i0PsWjuLEK-JUGaQAPOJQcQ6E0aRUHaHZ8Gn2vvEweSYg3f6cE2-8a2LQUkb_xkWgUpYULBR5rRkWWWZ8Vp_fQGPwr5LetWQ5z2IqG8xhFJkzdIJKMHDD4IfGqYp0aYNiIZWqtipE1ONM8r31XW00qWmLWPCRFsWMQzU2qMjM8mkMvZx0ej_XZaFfozMT0UYt8R7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=K98UUP7yKl8_Rdhc2QwfJLpU-QygULkF-CKBa20MnFlFIJUcDG6ZAkC15g3nf04tgSalw7UJ87lrXU9R-Yct6Sv_cN0gIh2xN3EOzAmWUoufv8Ezhs_4_V8KOFwgO82EdwTQpQ0wrYKWN4cT_i0PsWjuLEK-JUGaQAPOJQcQ6E0aRUHaHZ8Gn2vvEweSYg3f6cE2-8a2LQUkb_xkWgUpYULBR5rRkWWWZ8Vp_fQGPwr5LetWQ5z2IqG8xhFJkzdIJKMHDD4IfGqYp0aYNiIZWqtipE1ONM8r31XW00qWmLWPCRFsWMQzU2qMjM8mkMvZx0ej_XZaFfozMT0UYt8R7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvcnvKDmGjaIAyCBacpmaMlJlb2SSXZnkRQcytgwFImHmlpOjeUQZzbFANJusrkM0evcRAJ0zH3SZT23ly0f9FvYj0ORmsKM_Aq5Eg166H9GAcdFH218EuuNkf404HYpvxrLTCD4ZqawyeotR9Y6S24TMQ40j-efQpKmVCfLfcQEGOwmuwRWoxNUIKgBiOoT0liw2ovq3HZ7ufGWabQ79iYUwolImx2hdLJ3dZ2GDVE-vfFgec8BC-tUZDAf9rKRk1r9NogVPTpvqilHy8opRaau508zO_S86m0FAMYRNY5iyZDEkE-qS_2BEQJvJUdpnmn_xtrfjxbRpw04Ropwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XC3pU1clr6PFfISY-HahfPf_LDNoflFFw65GKd4zgQ-sOQYlNSn8BFIcaui4eYFuHSYtaBDJqjlq1mPl9KnHtEuiUAN6Eezqtvwkyj55oIcqhTyZ41niKJCA_61tB4xIRCMRkrpd3GgfiQru3fAhNvGsvBQ_W6Xp7x03uUPWKdcWG0NlEmIPG4-dt6oLaZOAMO96Pq9gJE60FJNfNSArJh4ZsnI-pJOOdBc2zTaEeGZHoC0DD2isr5tzkak7mEie7kbP4aUJKNblTmCZsIpuDn8v4RDJq676X8yRboUylvBnHbgEHRI7e61BXWf7yxGsIM-pSB91Ew7hXBQNIiexAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=v0elzgMCKUUyNIOdBpXt6jazLM3zviRcwPSSWnuKkudK5qkPpdZzjzFKmQL4vLUMkq8Eklkyd2M9SIdSj7uonArK23QswhrdptF6qT0ExOU4LqfO46XdXaZMvvmW7fD2mIbX0vmnxDmhQglVgieVI2AH2MTV5nEmEcZ9mqhvb094pNb09Iwshm22x_NApKSL0w-BY1WNNEypEiw9CDVtrmCjpSmM28eL7XxCSBQCuGWnwM2Np7SySWG_upplaLLsfuOcYiiid-7BzLHiSBA9k30vx70Pwr20CY_WN9FRhgU5uN5Jq9AvsWFOhHLtknmS9TOH4fN_7m5i_EcHSerVDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=v0elzgMCKUUyNIOdBpXt6jazLM3zviRcwPSSWnuKkudK5qkPpdZzjzFKmQL4vLUMkq8Eklkyd2M9SIdSj7uonArK23QswhrdptF6qT0ExOU4LqfO46XdXaZMvvmW7fD2mIbX0vmnxDmhQglVgieVI2AH2MTV5nEmEcZ9mqhvb094pNb09Iwshm22x_NApKSL0w-BY1WNNEypEiw9CDVtrmCjpSmM28eL7XxCSBQCuGWnwM2Np7SySWG_upplaLLsfuOcYiiid-7BzLHiSBA9k30vx70Pwr20CY_WN9FRhgU5uN5Jq9AvsWFOhHLtknmS9TOH4fN_7m5i_EcHSerVDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk_Qd_mZFQNza13N3Z95KwpoNleXHj5bIdxqK4cU8jCBFg5Z9O8bmugjLdJFAAEbYT80IdbpCppPhY4hDTovWXThNDCWDZtnIHlw7ZHLxF4PIUzxn4UXD16387m4cvgi8do5tNWS_-27zGEtSdLbA_BQ9s0YRkB2LGS8oYuoetaaBS5znRZKepEXto85tjMmjdC5Lfe539_VAxMn12dMBdXh8S9EMnXMtuWcaH2Xlvz7tfw3Lh8f-azU4zz9t9-gQuENldIX8LPWC_FNHm0m4LObyEHmqw0s1cOC2iD-0kp4ds3TxzPBYeLq3C1CkNjZ1ReIi9Q2nAwKU16Egqmcvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=qT5TFNNaeBc8lBh8lN646MCiDkZn3-J-JpEpcG3vMhI4uln7-2E8pjesD7MHmE-nDHbzuqk8W8sF4_OTEyyQQVgoHEU2dpOTX4ZFFrYZKpMGwxUOOp_tyueFGTnB1AWMt-rREsi1sjYUhblrZ4GIYAkLXB2CC1KgxtkupW1L1W_UArLzN6f3AV0R71uj2fgIwi1pKY6T7TyJ8veSJvj50RZub7FFKYOm_OZMsUqAN7Da2Y5r_Shj2jMtq-rdARMs7fBqpVDZPcljgHk70-EahPzBz4x238vk_ac1cPXFYVR8rXd-wZLV44zX3zCiQTWxYguABUec3_tTbIDRXid3Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=qT5TFNNaeBc8lBh8lN646MCiDkZn3-J-JpEpcG3vMhI4uln7-2E8pjesD7MHmE-nDHbzuqk8W8sF4_OTEyyQQVgoHEU2dpOTX4ZFFrYZKpMGwxUOOp_tyueFGTnB1AWMt-rREsi1sjYUhblrZ4GIYAkLXB2CC1KgxtkupW1L1W_UArLzN6f3AV0R71uj2fgIwi1pKY6T7TyJ8veSJvj50RZub7FFKYOm_OZMsUqAN7Da2Y5r_Shj2jMtq-rdARMs7fBqpVDZPcljgHk70-EahPzBz4x238vk_ac1cPXFYVR8rXd-wZLV44zX3zCiQTWxYguABUec3_tTbIDRXid3Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0Sa0dDd34W3Cxr2bxU2SxKY66c5LmLN2mHLs7m-2XeCLBnI7jwfTtKd9DU0q0LUe3fP57f3Lt5Mhxtn0ieUICiIFKCZx-P5pjXVgjGMUxK2Sm3ox23bOFn9yw0XR2si5vFBfn2drAsqUmIQIuNXcw0pKGEPbsv1FWUDMFPQFLQvGyvp-cmbIb9U2zHwzulqSsNJqzOLcYtWV7DAJtvSAwIabkrI6pcePIS25vlQ_mmDHSCgtSlRJuY5orb-32dRRNExfuzqsyeCfXrfmreFhUtatHX3q0P407-ItjRyGwsrYr9DNSCFmUt-vA1KbfZTzfwCADMX48elGUtL3hWrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
