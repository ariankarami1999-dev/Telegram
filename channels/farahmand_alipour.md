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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 15:59:24</div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9J2WgJ5JE4bNwwdz7q3V2IrUVuUtOyCbKQMhCWopxKc1s6gix1hOSQOB24hmiOoqWoB5x08HGAydJYskEYx9uJ9fB7VnZeWF5pJJpDrJVOMnu_47qlJsqCRfP-HOpzs2qb0DYgznXUdQcIv9l1fZfBnSuOa2GGqlnj7f10NIymfektHzHhIgN_j39xmwWiE4ZQufHxDVJBCArVKFr2knX3wNxadbTNZDzc9agKT5UKobteysFOWA7d5CnI2vyGz9gYz5v9JuSejqwGuFbqIzFAPUn6061WK260Wq5q8Ifk9YPDRe2giW4GzW9wG7cma7pXSGwOOuYbHyQbhN_p5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFdFiG6Fo_21l3eI0g9gf5NGpCehHQROmy9gqjvXJpYJeTEPafgkUx7nkUKtMtjFP9wIeLMyJeCLfsclv0NiA-jEOkHOW_CEpgQ6_y8DF6v8l3r6VeLmhIvk_r3NCqjmuu18gMJpj9xRmp9ZZQxCwzTEqVTK4KLA_Fl-R7i_MS7BeJ8rqZCPWxPGw5fQ-zqyKEpNrHL2d2MktcW40qhVBwp2CPrCbKJVab5MSSLSKFMpulUQDNlhAT33DH8tamqPJNB-5RSGquoUGFYyPHa8ivRjt4VqG19a2mNwpC9ZlUClHNenuM5RQAb1z5EazGe_BeH7Qtjgg7ZKZ9yRI8U_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM4D2xqXw920j5I9-sKCvfDDKU6t5AhNKkYatnKcd7tyoYkmaeUhgO78sK7G85vU6MyfGE8BOIsXHDeg42fETgvtpANYSdeRfsCn8aIjovbtBuQR8HtHxM5dEojSpN1o7PitmBb4xcOCJXXvNqO9m7jeLwjdONM4vhunTUzrmb6AVzRy2LWWYluO7LsaHMTdPz0fo0KwC2S7WOUqEFZNdTS8J3oEZ7hivBhokMESqW5Cw--Hs8IzErse1J7aHJv56ywILUBFGPnDBXQdh2voFwCwnuB3rB2gKAA97q3tdMur7CkOT-kNgipH2PJCECq_RYmAuZaTgShqZ2Cq1OP1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=U0XYFEb8RKWLLwsMhqzQx6C2Y7QrZ3ewrFzFFqywQgi0fYG7bXsWKw3zACAka8z4of3-tU5fwa3K1tR9Gr_OKhusDRcRPhvW5MwMJY20V8EjSYM0M0BCw6fhZhwCkesv2mkE5ax1NEBkKjYY6qzgh_NxnSEUWwlWzcgT9yDaLXFxAEwuDaTin_TvtN2KIHZUDi7WwLu_yJ806xe9pdEWejsuEMTMN8ayhEUs_cPspEP6cwiibW6Oo5EnwXOsldvHr4e34CM-VER78ixik3sv_v1OFhiilCvGuZs6L7-t2q1MLbz3EOi8BTaR51karFkNREqWVfvndE1mNzrtukpsYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=U0XYFEb8RKWLLwsMhqzQx6C2Y7QrZ3ewrFzFFqywQgi0fYG7bXsWKw3zACAka8z4of3-tU5fwa3K1tR9Gr_OKhusDRcRPhvW5MwMJY20V8EjSYM0M0BCw6fhZhwCkesv2mkE5ax1NEBkKjYY6qzgh_NxnSEUWwlWzcgT9yDaLXFxAEwuDaTin_TvtN2KIHZUDi7WwLu_yJ806xe9pdEWejsuEMTMN8ayhEUs_cPspEP6cwiibW6Oo5EnwXOsldvHr4e34CM-VER78ixik3sv_v1OFhiilCvGuZs6L7-t2q1MLbz3EOi8BTaR51karFkNREqWVfvndE1mNzrtukpsYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/budDXemWSIQ7SkoDFzao16aXe1hInTtqIATa672agPsa9WF8EDsKLaGZV3l2WyzcdOnzy7lD-3AEzDARLU5DylmTGzy0xod2cYQUoVyaiEDygWz-aP4E3vtWkqMWNxQJMjnLh4M8a8tQhjNAa4Bv1ahYqY2UsYIJXOyQRJwyJ-kc9iYNaeAxPHkEf-9b9jhSA_aFjFd_9BNpDx0NOyB7h1peFf_j3XVoUfJM6YCCcfUQgKQ6TLuUAshceY4M24WeK_XLFURecglGtzjYh-FhsWLTeO-BGHNOc3_FHV_ke3Aq8JfdVy4vhfqBQWEuwqtDN5V_HvOy3tYY31T2d7gnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfxsnffrikp7UJJzega4j6SPWStfbcHHDUAnr4yFp3-taheqCZ4bgTlr9I3V3fiEq6MTPUlehPko9K7LSvFf2TFGc_Vl2EfNlRop78ui2eOLTGn5Z55D5DUpTySlpSMoluNkaHSWpvxBamWBbjsFrNePpVlCINd4JkgNtmQRZs-6AWy5ZLL6IdRV94EUJ2nCTGkTZTV7-e-gsJGOuM3r7q6iE2N0erWlvkfJJYOsNiwn7G1SbjuCwP9cNnBVCb7DwSb1-hcmYwHEJDJzjQZzjldIRWHVKiS1EvHEpQXAWl8Y8hUqvE38QxsBjWDYLyr316o1g6bU7kiwjnVTPMadNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CcWC1osg0H6kYI9L-mplmOcb2gHOPoYrHBorLvFI_F6NzGmUGHOIbQJwpue_fHeoUSNOM3pjxtn7J4AlzPIe_tBacjr86W-MW8YBhhF8Y2iJEiUNzYoXvfIedYcxk9HO1pZt5qRj_aOSfigwxDN1FXSyaIwtcuB6uvOmMMSD15PfLttCo5hgvbcd1hyQIMhSleSETkVqp2dO6rU9D6m714wib7NIAvKM_PMDqCQ79W8JewAWKeqaEByLVSBTTTgo5Wikevz5eGcUJuynjIIr4N6DZxRUzo0Liaa1WFdlDmyyOVRa6N_PLpeM5taY6Fvd8P7u1OJogHQ_ONn_f09L2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JoBwKgdwKgCt-1KRnLShK_ijQ9e1Ug3sTEkE2ts_AxqTwBmMir_BiQVqZNobBg6CIVexpQ7mFXY4WJTjWi1RCSTsIMJMhEkk40kN59yhDegAS7TlwTUcCXSrJXhoIW1WCMeT8v4lz0ZmWicBYodpVcAbLLhwfnOwS401818eTBehg8R9nDKUOuOq7cZYs3wv7ZRrUG6E7Hj6NcrSYL_GPz4sMY5pVDFD9uen2kgpTwsQrHcH9AAa-j8-nvbKvhbLcQ19zsMgfcw7SW59HtsvxeIXU8Au_NTk1l_pEkYXJ1AwFUFi-fhDPeAgvIcrZDS95LMhf7rPvL3X8PYgWZ2QtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnmc5BM_BATfxTXVABN7ZsU4BordS4eNQI6aaqyKbrjAug-1oqbJULpCSOPfYakPPn9IZ-6ilxl52zQpXke46Ly4mAhmQbWX1Z-k8r-YjEO5u98NFLcVnFff2kRgvZENkQp3Q8xpJFa2dMWI7VyX4iTJmhsmHCkQtgKwFSju7nd03Nj2PIswXOa_UUSqM0_82PRRv3-ahh0OTttH1aNBrl1m6_5DFaf0dRXXf850tcCHdoK48olS356kVX0TxVUsYSMYuzq1PArgATXEtYix8B3gPpmYgj1l3V0vn4w_UGUYBUHR2PpUbchJc90kbBcLfX7eYs7kIprTfShUcLr9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgDyKCIFEawQuKRuajP-DVDVTd1Ga_rSK6An4FYmu5tAxlv8-AM182xBy-1fvpLGrFjCGZX39Vo7QkyKvO30VeKd_jP7vthJv0lRXdNVVhyOaLyaR-qf03n5OxQDg0BnkhMPG_ExvuGqBr0AqR6ZLJ7PPXXYhIqlOaEtqa76UTwGmDHsoLmqho03aA3OksSX7YPHfJjA-3dAGodheWP_4wVpmOeQjI-0lV_0vmjOgko0kjmOcv8PiY5mHQ8zjhvpp4Kf4HlIcj4xwp1SqVgbXdSPimGzuTwkRdj5N_5y4u_8pKUnW69mkSrDfgKmci98brOZDqJb9luH274MhlwRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRlu6t01lrbzvI5UmprySByZRnC85AkdshR2zvMKBpSd5emMf-SiYwetqAJdbfAi75Piq04L-5z19ZN_cnw-NEWkicvTLdGA9KWnqVmugNhTl1WHg9fmiM9C_kv750SNQLeoqmL-lwosPWrfpCR3of6-ugY8xTO2z76yoZACaqJNVHzCqSzBlqLqM8SBcJ6hwtkyHLz8nUIMz68_knGeOjaWd_anAKnqTem1--vhcvnQMdtOcD2AtTzKmS3NQlaH4ywFq9Ou1yMBqt3k9hlpjX_QJpqqZ7UeS-65Wrh_tOptkvKC-UHKThXERz9i1AfjK-K6ZBMZJU0k6ZL_dC_4mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYzFfuzO0jId-eTEfc1EHyvwLtF1QgjCmCVamvOUr5U4MQ2dFurURiAPjXzi1l1KIOQo5NeRK2voZ2nioDNAV2iDWL0S82dZzdg3B-BXHo-ilkd3gskMqbN1ZBFEDnNQECD3eoouRJO7AQ6yiDdL6U15nY9l0B2k2o_VdSrCKajoFLYY67vjRkyb0Vgm2RuOHCVFCrgAZmMMGDMhV0fyfva_MIf3gp3F0-0lsTQjRBLE4A95nFTHYk8rNTmiSTtsh9N2QhQ6YTw8oVw5EFmGaZ5yn7yUcksMHwtG1tlRFJbhLZN6xT3n9GhhE2g6uwIUJAnQxt5kTsSu09jFlsnj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=W2x0jCcTJ8B0KSSMm1ARPGHFCUy83LE4GSUPtWH9AiYgHA4cCbKUgnYPTWgIYB4FHsvxo6YBrCbOCTRRbVposF--b7A6rRmgJ-D2PqzUQXFnMssC_0yFymMtTIL4U8IW31Fq288Bw_WoTGE0LTBhmY3kTIZwgPvHPELuJeSiyIr4xX_ts4DTMJuPFmDlYvg1OLF8fqXiRq2UFGSMK2D01or_PHOOAhEFncJP5JogijcYXvR1pDw5bvplSAX5AOvM9GRAMj1G3Sf8ruSxmBneDh6J3cieb_edgfJf_Yqvst6j3N5oxhOK36jobh22B3ZeuQRdqBkc3xz4A41zfxTrhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=W2x0jCcTJ8B0KSSMm1ARPGHFCUy83LE4GSUPtWH9AiYgHA4cCbKUgnYPTWgIYB4FHsvxo6YBrCbOCTRRbVposF--b7A6rRmgJ-D2PqzUQXFnMssC_0yFymMtTIL4U8IW31Fq288Bw_WoTGE0LTBhmY3kTIZwgPvHPELuJeSiyIr4xX_ts4DTMJuPFmDlYvg1OLF8fqXiRq2UFGSMK2D01or_PHOOAhEFncJP5JogijcYXvR1pDw5bvplSAX5AOvM9GRAMj1G3Sf8ruSxmBneDh6J3cieb_edgfJf_Yqvst6j3N5oxhOK36jobh22B3ZeuQRdqBkc3xz4A41zfxTrhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8OF14UZylzowWNic7lKP86S0zEZA4iZOfRPGEbSGVUUpOvYyFe4jMf3oFXuLTK2GekDGtFxdAg99Q-84gDUdROl2v9KiLXIZGdesE4tDEJqs9dOxVrHl9x4wYnxUwZF0DO7RORssE5IDOtur9QTUZz24arJfpV1wZyHurnP75VE8eHqZ3bM26mV8sO_LXFOO-Nde3VbUuCfx-F1g9iXA5v92eTVtT29mCJmbytqXnyyJhGYNPMCT_P_32oRquosaRcezvR_gLic9ydkxTZREI6b3Wcmy_aQ_31yNDgtqIEGiJGoGC1ra0uF72hcead2_QHSD-2jvzQttcBL6zYHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB3d79jVkUiloavjLIn-VnDNj27qEa_RQUm3wETFo6g6MZ09T2YhNFXfJ5mLalSE2wNZptZRELHGdXoA_xXSN8Qc0bdMZsEj7gW-Lzb92RbFPoY2ExEDxzY0yD9dWn8mPUDlGyChdocYVpEloRG9Stv_s4k1KO1e8isY6GGQcDy0il24xShZbWsklqyzlQm1bQR08JLk0EuztK6ouu-TrLZFTXnuKmf-cwpASd58U8lJC3pCr5meFZjcWznt7Yq5aFke5537emLBTOhNzECcEeskZkCgq6TzEXOBkcXGJY6rPJ-Ilj0gtoIfPfWkPw2OYfZTkTO9B0NdGAjszv6Y3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPnmVTwnWT9039Z2CRtPv6LoQgrtUVNya8EAXUXp-GEN1SrGh0ZSjHB-_yxlZcbZiXdKkegObfqTJ_jUBf5uKgK94IJhYKFqsNf4QP00kwp_CKNifShdg8p1KFJWeJqYAhG1PSj8WJi7X9dlY3Qj_8WU_ANP1LBZMtgwTZ6vbyKbyq8JGHKOkCQA8zPtqeqR6v9WPZHaSBPgYzudMnGjHjeLze21JGSUnbj2WmlPhkyi_HVqQFwx8XIUgKU6qNrzhvcrMU6_bWtrRcOVOrgfcVRKeuMh0K8S4SWl9YAw-euYGa4mjA7v2q13pseKZpwHCsLXnSq-xE6n1f-eKl_7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=YkPaFbxBPrdFS93NfIA_ExfN9jbWKTp-q3Khwv9wLWrPseJABHR7ovmDYKQYvWT-Zku6UvlbhWswqLZXKom03-Y5UWvns0_ZyHvNoXm0IfmdKwSeYTmYc07YgtWn1dfGjntCjI786vpCqed3qp4dqeaqVhQDMT3aEYr4Il6CsJN8PXWZrJiYMEnr7LwfevVCIMwwgJuyOIs00WtBlU5zSII7nnioYnk5bJo4oYGR5cCjVtcyJRGnYz_u6Y7DD1zC355Qn891GO9eM8oHLZJY_suDML5trXTDJvyuj6nVIXK0iZQPLUsILmT6EBJhHA1Z0PAV9LJ4v8ey2LdVPuZ_Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=YkPaFbxBPrdFS93NfIA_ExfN9jbWKTp-q3Khwv9wLWrPseJABHR7ovmDYKQYvWT-Zku6UvlbhWswqLZXKom03-Y5UWvns0_ZyHvNoXm0IfmdKwSeYTmYc07YgtWn1dfGjntCjI786vpCqed3qp4dqeaqVhQDMT3aEYr4Il6CsJN8PXWZrJiYMEnr7LwfevVCIMwwgJuyOIs00WtBlU5zSII7nnioYnk5bJo4oYGR5cCjVtcyJRGnYz_u6Y7DD1zC355Qn891GO9eM8oHLZJY_suDML5trXTDJvyuj6nVIXK0iZQPLUsILmT6EBJhHA1Z0PAV9LJ4v8ey2LdVPuZ_Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=eo_hWv4eRNU8aY5h7rAR89T5R577MpFNUIZsiYWKzTt3_wO5afE2ncSqp_NstpHZ7-5ZUqp7XMjTKxcE7oMZFOc1E5KG1irpw3zrkhI5ulRApaAAAaqHBaxgW2-em0Akepywbb4bMhBiOUAtnvQJobJRRymzcCwMYk_7NQm4WGfbiE-kabthDr5dLogUyciPzYk5ScbS39FU-4kQbyRkBAq9d43ZIbQecX6E0ZlcwTHIDc6jR4l_pkBBo22dtBy44rNZ8LXJe7Nwux79FXhk9zdI_ZN8txB6AUCWsSBiGsDTfloWnJh3muzY0Y9UJHaddkhiVn-_NekP8s3FuzXakg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=eo_hWv4eRNU8aY5h7rAR89T5R577MpFNUIZsiYWKzTt3_wO5afE2ncSqp_NstpHZ7-5ZUqp7XMjTKxcE7oMZFOc1E5KG1irpw3zrkhI5ulRApaAAAaqHBaxgW2-em0Akepywbb4bMhBiOUAtnvQJobJRRymzcCwMYk_7NQm4WGfbiE-kabthDr5dLogUyciPzYk5ScbS39FU-4kQbyRkBAq9d43ZIbQecX6E0ZlcwTHIDc6jR4l_pkBBo22dtBy44rNZ8LXJe7Nwux79FXhk9zdI_ZN8txB6AUCWsSBiGsDTfloWnJh3muzY0Y9UJHaddkhiVn-_NekP8s3FuzXakg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=WKOw1RL-EVjrJ6UYBePgCF87snE0OE2Tng5KN1xQBwr6M993I8nOG8o1P_-phs0m0khEIlJMMe6Zz4KHWi27tXPnD0w1ekbKNWTXhUZm7etCi_hMImlpHPhfKAndBIpivyaoCXZv82cqg3640MjPNnSq6OeLDlIYlwOmn357i6K6QxFG3VTMw239pTXO95914tzuZCEcmvYQuu7Ahmb9JZizZNDVuTklHKxsrYB14Gd7HDNLM4MuQOJUaub_DEM_-VtJLCmVuZy8DNUuBXa9ayrnNToAdKMkMf0iRDfhsPrLEOyF2UbtC00wqS31XQOe6PZcjUUF29ZFtv8FDUl3QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=WKOw1RL-EVjrJ6UYBePgCF87snE0OE2Tng5KN1xQBwr6M993I8nOG8o1P_-phs0m0khEIlJMMe6Zz4KHWi27tXPnD0w1ekbKNWTXhUZm7etCi_hMImlpHPhfKAndBIpivyaoCXZv82cqg3640MjPNnSq6OeLDlIYlwOmn357i6K6QxFG3VTMw239pTXO95914tzuZCEcmvYQuu7Ahmb9JZizZNDVuTklHKxsrYB14Gd7HDNLM4MuQOJUaub_DEM_-VtJLCmVuZy8DNUuBXa9ayrnNToAdKMkMf0iRDfhsPrLEOyF2UbtC00wqS31XQOe6PZcjUUF29ZFtv8FDUl3QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVRGT2Fg2ZofuqhlOh4Eyg3OXoAgMC3KmOeo84OzEHQPP-j-n404rjSTWOdt9UJ-IID4ycOTuxXmuzXLkcjx8ebb1skWKnB3qJOr2pw_sLLUqLBaT5690w0u0YGfIhEaihq2xQuZOx559Eo2BJXR375oX5ZVRG9v2_0fVi7JBmuVc-9PXQOXI8ZlAxvSP_JORUS1pdGYo5T-Hhbuc8w4Sus6WvII-GsnLrdmnGu-XhiuH15xz0M_cXBsT5qxT-DcO39lshimxcJzTT44Lo4I46KDyeKffZcYkiCikTHgMiqv1CKtreb3wGGP327Nopr1MpGBUCoQpZ5JSeNzOSSErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWL5AkZ4_mItYSq2vf_RaRDzrss7R9zxYYMFYkfVoWZ9SA5rJGXeapEtp2tF4OzpHf3EmPukz4TLagfXN5m6DELpg0V5VQX-yd_BgDPEBkLFK9bfbcDoem89ONII_K3Qbi4fpTS-RqJJIm7jebPfH1r0FKxvWuQ_o8VtzktSDGJY9hepsWCkzXUuEQRl-5brgzE82ScqTfPr8xSZ2E-MdOkQVRnElTT9sHhFhJHMgwNt4aeCQ1z-j6LO-yY97WZfAJDgJPLcAzduFu7MMQAicIEfT3jwB_8auLp0xnUbFuDOqtfad6RI0XYUl0y_gtA2B32aHJF7WX_c-gDH2AmtNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bb1XdiAVDgMyPP5YLVIT8i_hEkcGTsGmmfjJWNyLcrKqPa0DiAJX1llOBbrHiWyuGH-y_wsNn-2UCtpkdzZgmCnzGUX2gifLoxTAtsBZLLBAeQAWcjvc-J9rum6Wkiep5GxgELF9VuGw6ZeBSmQ0mHa2sPrDFkCEQPvjEERCaaVbjAeEyqYpcE7TJ87jnEfoM-tmwbyvczYKBAUyl5fcflL8IuGYTR8UAyOqojgT_kar1Ufwy-VFeI9vDaTCctkw1tli8fkztPcpL6U7AqJPk7eD3ijDsk9pOA7MbT5nBIOQ83UvLdabCVRjZ-rT0Q4rQvKTzdU8IRM_5pPERWEJDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vtTXD7y0aRrVbqciQSPopsgEkydkg4JB-kwU0hDjOpgNk-W5KFtA-f0m1na8hBE6e_juEUkbUGrG2zC0f0PoWvGg14Z1GSZt7-K20kFdwMIFQfoBzwEVpwKeayNOetVgFJtErn1vLrm2XzgQe3r3rKvUlQ-mqzCVS_0IVqZi7Kd4NcGLuYvvtwAbXPd7j2YZZKv58qmcKY4Af5z5JA32qyV8vOga-1LTSBTuwdZLxZszQVeKu9V9W_1yYd3crawumWHWi7Kfum4-jCS7EVzg7GS95WidkdBT9ebuLAvwmDjpB2_YsqZOt2AzLi--k0aDzaeWxdg_WSEwVtqiR1_lww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUYxYdWmjUVXt_Br8fwxEhX9wV0EN76tW5YuqNoP7yY-VzlgRtw2j0XpPUsgGfeakzgRreSXyAh6RnrmnmzeCJg_5-NN0NhxFUeUSWqJ2drqAKlo1Aeg0vOicmTTAtZzArRg04kfAuZlT0xaDiiDq_ue9tccbadJGaqFcEvL9VuX8V-Mi060KB5m0hywroyPIVl1AdCZguWZhUy8qHfQ-qTo_WrO5RvS3N3CM6o-FOp_H-NMFC2iS8zBme6f4U79yaXmr2t9ll3Dv0hXjFesdaQegq4HIy0cdJQLKrLK5QT-U8YPZIfs1Us1wBiaiO_RFaAhm7hD7-4SrCG203j8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/toIv83ahQf-W2ZcRp-yCYFglN0YtYJ2-6FqTExU5ie_Flrbezt7FGOEjw-ubh7BOKv2ONZS67QUR34a69FGWMcU3cOpYGLBtXk1N0goyX1H5RKD3BQGj1QgRlOJleIKflzJzeYi__upe8FAJRlltIsswSTQzW0AQTiTQQp5sfPQUXxZLS5M6OcR2nBk8i6pRMHjlA3NilwMPWMEVVDWjx2tnrNJW1QsK8Bpg2hkikCwjpJ3MvKqfrt4V6OISEFe3y-I0_jGPz8SZqItYj93o_d9OJ2Lq73GBlCOSzd_hsSGdPteSIaYLTeJ2LqgpNYi0bVizZHV97xkBgS4FD2lxJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZ-xUQK8DltfNjDvfZGjptqBD0edYxLHe9NRcbIejXyf9BE4IcDa0C3xtA0fHQgFoJXBzBtl-5rd0-3VoESQblUpJhicnpbZloNOxSZyJaAAWbv_9t6I_9so7e5g0skK2im88YEICcMbGuAURZWAxj8Qhw98t6eizg9gSuHLnbj4O8PxKUEIBB8m-EooZ6K9O82l8AQwq80vKecDXesSPjxVJ7G3tAYymAzLyNDEO5Lj-BBxG9bblHlZWJ5fbysTrz1CzrAu3gjX9e_hrQOSZiDjPQX8PcJoKYSRWHgaZ3v9SpSo2cvAn30eDJxFka3vnQ2FCqv41mKfyKrWkZH83g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIP3KcVr0TaAMuGF1NatLbA43t0sYxi-VRkucbCZsVt1YOTOLH6jOcDGH7VoRdlvjO-Bq0RDx9UzSeYbgLsJ6J9AMDdLpkixP8ZFXtIMWHLzNZSptv2IPw6oBTgzqo-6y7mQJkx2UV2v6MQ5dAHPISKbyzY36pf2HgJOKyPRhbU1XVAKBAvcrDptLJF-tx5QnSw4r2fpCUeB33__C8otoGtTDvxCUC6Evo64GSXh9gv0YoMqEHgb9QTQruYSiFV_AVbkCj3n7d4O2XlIxoNfq_0d-fM-bxjQCzUOuP73JPm1bUmKoHQo62qgHHsHtvWP6dP38cKWozfclnfMgpkQrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvjCs1W-eNK3eibSDu9fo7XgmUbggYK90T5cWIvaCsZRoaU0yAxyRkC-KIZSEZjK8BtTlUzdB1q6ztzc9eU8rkVK5I0Brneryi9QabRouCaqyUpCIHkU1MkqalAGnDfHkQm2PiRAD6eMXv4yA3esMWWsKEXgQ1F8_bheYwDBoLO5oIqGEnoXTLwjTsE0B6L4QOjpgzHZrnwzY4N70mytToeE3at9ytQcqpCKFWovSXQPOyVNmhkNn29Te5znwKhg95gC38jCTE8IL8RaE--_vp3lxh8RzqZfrpxjpKoWi0AHEL7fBmuaSgeBFpLXbAVeYxzW4WMHG675jrqiK5OP-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1847bOjyCeVDttMwYq2moU-IB00nKqIjlP_lLjFTmW9PEjwdLFN7OBLL9ugO4-m5XtNz-E0DRF696YwXTnEUnvTmNoNwKzBalEVYZkIclIip4YDYWdQd2JaIqB81mR-e-gEt77lQb1tzqkGvCeOikwDoYrL8h8yH4qR7yn-TiNOswcY0_c2q-1yPFTy9CrIbc9DDtlhkFn3dTeTDtSjKZlUJAop7y8upyCVPFIc9Cp2IlDznowQaDoPbdxAkwrKJQXf-WtvltsIZCZDuKx06X32KkCEOx_p-xdmg5Yfe7GRNc9gfXhpzcdWuaFMFEdq-c2FUV6ZqYVUkhhfIidiYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcqRvNCtwuzmx-bhli9Oef9Ird-uDlra8zJBi0pB7z_jJspMRw5Wgflw8m4RdG-cdRzLNcUcocpmgo6rzL1JFF-iObhCQdOxxKIRhv44bGxFj9jJzJzMEdw-Tug7GICCMpvu15HqZasdXFtn6MeCF93eoRc-7LycjGJMWhK92LvT1pycgyTg_9rvfWPFvXTnB6iWShHN--CdWLVqeEmt3XiC_8q9F_HVIsXE2dZ3bM3OaGMAWn7BWfwtHt-ijaLMJ7iz7irnZByzE4AX-i4hlOoDrpsyfJ_RHOXV5Du6r19mFNc67lNGZKX9txzBuOz52R9O-Af3Xzd2EIe_jk5i0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZkXNfu7OAc3evb__ET8csCEZtUVt1HOOAIm_DWhAiNQfhFt4uZTyHlY1dCikdlpYpK2NklX-jw8HSwwKrcuvuacKUTgh0bVbXIdh-wSTB0WQfusyj4P3MkCnlcn4tSikPDteA1UZ0YNbA5fdB8JhMT97JXzbw0YgI7pOO3tq3B14zwQp8PpR1KgH1Brzy9RnMCtnGJd-9KvsTrPCIehOM8mzUA7dmeWCVG2UopVSQWsDH_0iNineesJD1H1lTMZ7ZL4uN6Rk014CSfva2cqc2MA9os7_G30oSmKtHmORWGeKwyn8xAal8p0hq2K0SD4Emy1xGMMoBzhzHpd8M5qvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWBKHoUjvG9E2EtlFzfM53YPx9L3bLQKTLmryqaUkrKzV5xtvSFq0ix5FCULHIMXfU57lT6cC7LmVAJ8SueC2hWMEeOL3ma0Rt5gXZ2_XD8D-kmQbKxsP3ilsWmxyyFbsCwsS1fzr4TPCqbsTEkZMjs581OMecdxJbTAm65AnJ4BiZjbKRKkfjwVa7D9SKxn-5d18904x2PHP7U-DQXy4ySO6KhKjBEMQaLwoFJqxKjs7t_f7UtyaUBkHFLx2sp7UcvZCpTT5fn7kUVte3xe4y7uhLiItuia5ZwSzNUbInKxkFwbQ4vRPghFbk_IY1OZyB2iZmHKfkdTiblg9hEXTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXYcvP-zOGqSRv9-_j_JpKQXzFgwcGpd_fPomsJzJU3FRF1uEVjh8Ylh0-IhTHUS0tXKwniD40zKPvY6J9eEVhMHVQ3w2DfZo8ycTjxCDaonkjzjn1TI1xuv8iso5EIlalU2ArM2ty4ok5QIhaPhMaWXaFdM9vdJy2ijxCuyDJF7xMPk7Ut9sHiXtYv9dzbEB4I2O0qDo7CmrRYO0xn0q2Oq65IaLgPQiE8BBv2FHujBWf8R5x1nvqWmROmqkhqcymHS-UcoX8igb0vp_KJgNuBnBrdKwpPE2fy8wAjormOb_1rB5dQIP4mLievM-BOaCDL25V-83eazN-Cikb0VXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auxzO60xsTvwBfEsAkWkpZ6HiDqRyysOQHvaFpG_i_SBPZbHb33XZEuMrV5KgpRjuqkl_Ws_wndSdZBWPWcFpiEyHhZJ3TjufWKBly7CS10mZm43qHkqX7-QdGF6_FRdyppVBikNOcsX04hJqtzpI44ReGLO095rlhbQLHhPOokMUOsRDRMteeQMkZ8qZrhQkXvaeRNRXzFFGQ2RXr0txxdzQfek7ZNqMtuZJ9QKB7feQ7snfR0w7D-0XGluIml8_R5BltjjfMBQp3nnAjJUZfhiFsJV5BHpoTEp_2XrP8H4IhF7aOf4BgoOi3xP3YbiEZJLjSaDZYgEXL3ze4xvog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=nSPd23xLJLLAuYMscfw90dXqsqcCB7jxpLmk8hR2goTuXXKzROIgxi7APtKs5ImScgBGM1UQyY8ndkzWtP4OssZfSU-UmDT8hWZqRTV9Uy4DKGHQ7hOlW3iqIHe8CO7u7_JfiQAODrgkb9yoODD-sCZUD9Lu8xBMm-aHphWY8h7GlC8fTuGFW_coS-irJKDNWQHEOn025qPJm8-vBuEIveCOvnSGzHTft5yDsdNsOUQE9cfy_TZTvZK0bwaPr_VvFcFQ9y8iytg03cJsGyiOyp4bgn5sRNX8fOHCNdviJOCYYJxmaCv1U_uOX1T1Mpg_wMskW44Xir7MAr9rGEsnxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=nSPd23xLJLLAuYMscfw90dXqsqcCB7jxpLmk8hR2goTuXXKzROIgxi7APtKs5ImScgBGM1UQyY8ndkzWtP4OssZfSU-UmDT8hWZqRTV9Uy4DKGHQ7hOlW3iqIHe8CO7u7_JfiQAODrgkb9yoODD-sCZUD9Lu8xBMm-aHphWY8h7GlC8fTuGFW_coS-irJKDNWQHEOn025qPJm8-vBuEIveCOvnSGzHTft5yDsdNsOUQE9cfy_TZTvZK0bwaPr_VvFcFQ9y8iytg03cJsGyiOyp4bgn5sRNX8fOHCNdviJOCYYJxmaCv1U_uOX1T1Mpg_wMskW44Xir7MAr9rGEsnxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f04H8mCBm6qWghV9nWDL9HJdZ4tH13ffPOZeqZVywx_siY4iTGkuSwF1rEgTcA9gN7GzIbiVk-NStDwS_h3_nefUcCjbOPpojpptfN9df3FMxB391lvqRRaXXnAL2ZzpwDKsPmT1vGGBl8Biu6wzOffdE21qOBLgs0WE2f_WAqaOPIyv_juCDhFU5XL76wkZ5PvKmzJihrpCgvn49cV6pT-2gpxF27JkQKLaFI3YyrQXShMQ6Zfb5o1SMy9t7WDXqwLwW9G_453XXPUeRTc3UXHoCBxLg6808YFvxGpm572waf_uVbrIn31JyWHAyKuTggL0SWGnWJLwmMFyOXKK9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=ssKaDKX23YgrjJSIBmz0f1X5t01vJj_evme36txkWjMrR_Ct0YwmXwcjSA0iUQLCV57IaXXFMP74n7ept1pqEKqJD0FQst_pvpo3izBOYMd-QA70FtlM0fhNd2BJsFWf2Bkhsi1bkbqNalQMrJgmF35W9PdZAC_0ttFW_ek5BpOXLdW9Ai6w2RixYqgaQp2c1wzVNPe23KeNnFsODu_kiMOQ7wu6GodNmWkQAVqxbAkNCXndnZKJ_l2ifRyM6Y6csXsNzDgI7n5H17mHh2LTxNoPZn2nP58v61MsuIRguQI6EgOlHbm99-P2m_QmFvgL-YnWlbpWozTCHRe360lY1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=ssKaDKX23YgrjJSIBmz0f1X5t01vJj_evme36txkWjMrR_Ct0YwmXwcjSA0iUQLCV57IaXXFMP74n7ept1pqEKqJD0FQst_pvpo3izBOYMd-QA70FtlM0fhNd2BJsFWf2Bkhsi1bkbqNalQMrJgmF35W9PdZAC_0ttFW_ek5BpOXLdW9Ai6w2RixYqgaQp2c1wzVNPe23KeNnFsODu_kiMOQ7wu6GodNmWkQAVqxbAkNCXndnZKJ_l2ifRyM6Y6csXsNzDgI7n5H17mHh2LTxNoPZn2nP58v61MsuIRguQI6EgOlHbm99-P2m_QmFvgL-YnWlbpWozTCHRe360lY1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=ICJUYqB-oeGRjztXVnK47UPkFPn2MHtxX1aSmi_dmtcXBpb3qrXx6HXLzm9DrJP7CV2fyHU0X8W84RZeCId8tebPA5tx1kzioGl1VGNKrY1DbdIG6jmA2FBUGMpeSd3-Jjo8BilDMlbBqRhhaBelYT8qfimLTM87rnMLbg563TKHtIwdZnN7PvrRuVUd9T0Qy81woTJ42v4j5ZkA4AIXi6IZoa1hmIkFrYgBPOsNauv0N4xZk1b_Y517Um9PbpwDv0HozA4lutqZuhH-5Qw8YHaIk46fwkSq8dO32F49SVhLviI3UDRWByMrZ_F7HhVtPaLl956rGNXVJtgdo2CFxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=ICJUYqB-oeGRjztXVnK47UPkFPn2MHtxX1aSmi_dmtcXBpb3qrXx6HXLzm9DrJP7CV2fyHU0X8W84RZeCId8tebPA5tx1kzioGl1VGNKrY1DbdIG6jmA2FBUGMpeSd3-Jjo8BilDMlbBqRhhaBelYT8qfimLTM87rnMLbg563TKHtIwdZnN7PvrRuVUd9T0Qy81woTJ42v4j5ZkA4AIXi6IZoa1hmIkFrYgBPOsNauv0N4xZk1b_Y517Um9PbpwDv0HozA4lutqZuhH-5Qw8YHaIk46fwkSq8dO32F49SVhLviI3UDRWByMrZ_F7HhVtPaLl956rGNXVJtgdo2CFxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUaofaKEn5oso45pnC3c6uRK9pmLHfs6lZmH2wGlFnX_IwE0WrcJi93OPJrnH1RPz46VHkon1n0Xr3KiJB4DlVmpHsTgtCzaMpNHY1rJTxaYEAAzrSZWe7rJMIyFdC7Z8kuzTwgk3kZRVtxZEXr-LgOgpl9YKLiOLZODejHQsO8UZakWaeVyI5QzEPIolSHF2SM5gOK2csBTiNhyIQDNexhKs1hJBdnA4tCFYILw_8Xry5zhPbxR_VlqT9BItxln1dl2NedL3HwcVCmBGyGBSu8iT5L_WvIh43bSFMedgt1Hc60MIJzQtsylcaKdHZOQGiMHZwzC9w4qc6Lenr3hxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=jtTuyq9z71OjnEpq4gibGWbqh7nbDZ1wvvlbuwujOw6jgtDDmvsn4ZlSKC4o77LpWqsZVKKfscdtUMJjQ18ZfDG623Tloo2Wmo87GMjhqzUAIsNppTVz-xlgMyWKZzu-C741jpYdpGKjS9NMic_xzhEaUqxiAce-JEyrLrTmnPIV94juJY4Cl61aH3Nfd-aOvnzexYznu8EWAkHYEpm0AkfzU_f8rTmdKASgppxEPaaJY5sz1aRP1-sguG2IJpbL9-DNND7sSc7_fLX1s0C3WhfFIKeIR1Kb7FSPKOp9_f3vq6zp7KB12R-ItG7C0iRMYS_5dv6QpoBOFmacg_jlIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=jtTuyq9z71OjnEpq4gibGWbqh7nbDZ1wvvlbuwujOw6jgtDDmvsn4ZlSKC4o77LpWqsZVKKfscdtUMJjQ18ZfDG623Tloo2Wmo87GMjhqzUAIsNppTVz-xlgMyWKZzu-C741jpYdpGKjS9NMic_xzhEaUqxiAce-JEyrLrTmnPIV94juJY4Cl61aH3Nfd-aOvnzexYznu8EWAkHYEpm0AkfzU_f8rTmdKASgppxEPaaJY5sz1aRP1-sguG2IJpbL9-DNND7sSc7_fLX1s0C3WhfFIKeIR1Kb7FSPKOp9_f3vq6zp7KB12R-ItG7C0iRMYS_5dv6QpoBOFmacg_jlIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc_iNCmEatAmYIqrdS81bhUzdqVuOWqCPe34qi_TYXuYNknCY-et5r0SQqV6Y3WqhuijBz11gS8YqV2QYHphB0h3m2wyEy4tqpTR78TOD2XXQpMSk8mlTYC-Yq0OwPQUfZ4bzUZVokYjIHIqJeKQxCkBu99Ir5IScWouMjw_oPoJNxwOIaQLRCLhPKBCGBvNghryNlp_J8KwjjK5Xjv3Y3emkbGy5RDzUTU3nyI5xDB3XTgTjBAT5fmAUxnUD8NPozll5dZqiP_ek2glvo3Tya7Px7ePwGb2MT6I9xjGqfTupYChbgqY16pDFLXc354t1RgqHuqXDOSLFEJ6QxvbzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbPwdmHOINr9kBs-WsDVu_7fEJi-ZDbeT4Yprp09iBfWUKxj8GN6XkHwfJ3pSckCrEVnF95TubHXf_y6xH_jhBq1ntp_AeLRKdrOZajV02u-peojBHGZTz8ObS-XiweDwOoRk838qI9Sd8t9Kk2SjUtg1I2-nCblGW30rVowZdOIYIvn_zP52hw46bKjBtljp-vXFA1txF7SWo0WYNygxNNARUKDdN8dMChDIZeGGZujcEJbNY_n-lU0jCVC5hJPVu6i58sFsX4qB4WITgEv-3Hr000-0T7q-JcrorZgjY9ccaCozFSKqhdfv0tX5ZwxZWqnMewm5IWpJPRGbTswTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaCjftEwcsf0wIMvH0C5pZPoa-8GjWigYREfvHmIuUyvxZjMUB7sIG2Tbu0SgzlwSCuG0ZXvbfJOlGlECZAvOXHxNU9X-dR-Nb6VhyW1hfzdWr-099kOMY50fp5M_-Q68l5IMTY-hT_f6-NX60qHBycboU5Q5xs6OvaWTYNBz2NgNEVd3l03QH2IsjvQUQWtrlA4Bn1zFHMciyZMYncVYA_PNwgagfDuAsEHSiiXyaJZntHS-RJhyf_jAGSgqa8lF1NW94153-jU2QdsSA03RdvUQ6wspjrN4U-cfxIsypkrwmw2TPUfIBL-FIY9qFCeS6f5NZgLhwMvSlqTSf1WJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A49ItvEOgGn9u_YvtuWXikH6uOclRFq61QLpTqSn9L8quTMSklaqhZJuw9EelieXjA7GvxaxxF5Sy0LwKwV62rp6Le2oABHYsvYzzHvaqxUxcfmqxfkpNrXaPHPuWR8csU2bNVtN30c1vYMD4zTEetiLErCnpa7o8956NN6IVlRp72nv7cEQXMSWdnfxrJrfrLRpsF9KfpJw6qlTK0na6rPffD1nkskUwZsrjQfIPdz_XfEgRa2rKPyBAc-ZudLqAYH6x0KnpScBsRWURmCF16OKrfxrK1AdStsPPhuDq8euUdCjkPn_fXFSggBF2BmsY-nOuqPUl6sgSJaf2IPY7Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=NE2y8HWPCO1KMZORmvBpB_R2OsSwTvrhEbNkfYg396Le9P6muhBJ_FXmB-k9_xJ6mgMO9VXVXO-o3lhH0oWmgvRuSSN7pn9oG7G-nOP1iXFBpNsfYgJmMbIZY-T_wfJjJTvh3OBqcgp5lPU14imf6vrOPTZ-qdoEe-uKG0twMUKxmGzf4FXFpsEg3JaHSTuZUDjVA5WXX883TTscg7aLh6nrrtykK4MrXZjdI7a5cXs2gA-H08xzEL2VzCYUiC8kkn9S8VLGmpPWa_45dLOhvAX0EhwiAn1QGqY4OSI8GE8GK6WfywRcZvelz30_NwHkMjpOFYKSaHri8U-goD-09g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=NE2y8HWPCO1KMZORmvBpB_R2OsSwTvrhEbNkfYg396Le9P6muhBJ_FXmB-k9_xJ6mgMO9VXVXO-o3lhH0oWmgvRuSSN7pn9oG7G-nOP1iXFBpNsfYgJmMbIZY-T_wfJjJTvh3OBqcgp5lPU14imf6vrOPTZ-qdoEe-uKG0twMUKxmGzf4FXFpsEg3JaHSTuZUDjVA5WXX883TTscg7aLh6nrrtykK4MrXZjdI7a5cXs2gA-H08xzEL2VzCYUiC8kkn9S8VLGmpPWa_45dLOhvAX0EhwiAn1QGqY4OSI8GE8GK6WfywRcZvelz30_NwHkMjpOFYKSaHri8U-goD-09g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=SiEPTQ20Z7btYp-hzEmn5X7p5pcmGDH_y1i9T7JNtMEHnvvPBj-J05baT0lJ1kxlPgf5VU_vlDfesbDgKdBH7MbF3mIYzap82840MzfrcSUGG3uahuek5GJTBaa4jOWTv85_Ov8oLb1qGUaRZzeswpF0_tcf_HMgnziQNgoIbAPsg4z0KqWVMuDNrPNlqm55G2RspzDr4idI0iifOPYzPJm9i0EKKNriwfqg9swGgykxol-xA5MwXTFdJg2b7yse-_uCjqSqil9ztlDwtfh6oyAv-siZUG5odn8HVrmL6vtO9Ee8hO-DVxtaDtwyyQlBcFm2JCbfVzSh6BEIY2qqYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=SiEPTQ20Z7btYp-hzEmn5X7p5pcmGDH_y1i9T7JNtMEHnvvPBj-J05baT0lJ1kxlPgf5VU_vlDfesbDgKdBH7MbF3mIYzap82840MzfrcSUGG3uahuek5GJTBaa4jOWTv85_Ov8oLb1qGUaRZzeswpF0_tcf_HMgnziQNgoIbAPsg4z0KqWVMuDNrPNlqm55G2RspzDr4idI0iifOPYzPJm9i0EKKNriwfqg9swGgykxol-xA5MwXTFdJg2b7yse-_uCjqSqil9ztlDwtfh6oyAv-siZUG5odn8HVrmL6vtO9Ee8hO-DVxtaDtwyyQlBcFm2JCbfVzSh6BEIY2qqYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=c-6ms9Ac4WFvkgkn0FsM6Iy_FgsQWT-fEDzQiHI1kii0adQ0TJyseDFYD-kPcjwu-oMDxRZ3ZS7bf1Nyq-yedTcHBBWRoIq-JPV3y7oRl4rMhIz3DfY3xozOF59m7_0dDKyh8ltgXRYM-yv-KhxFB-g9tV2GDa_uTdhimGNfDhRi9L0nvBTpz-dK0TofwBjpkfMhrk21ZpPpW2Ptxb_MbYWxRzUiNov8bAm5308Vudi0rze_Bw5K6Dg0OxRP1mHmxb9s0wGIAERii6vt6wQmT-WaOT9fS6M2XE_rfkWwCkz_fnWFXX_uUT7PctvFFcnekJttl9DUK8u9harcOhnfpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=c-6ms9Ac4WFvkgkn0FsM6Iy_FgsQWT-fEDzQiHI1kii0adQ0TJyseDFYD-kPcjwu-oMDxRZ3ZS7bf1Nyq-yedTcHBBWRoIq-JPV3y7oRl4rMhIz3DfY3xozOF59m7_0dDKyh8ltgXRYM-yv-KhxFB-g9tV2GDa_uTdhimGNfDhRi9L0nvBTpz-dK0TofwBjpkfMhrk21ZpPpW2Ptxb_MbYWxRzUiNov8bAm5308Vudi0rze_Bw5K6Dg0OxRP1mHmxb9s0wGIAERii6vt6wQmT-WaOT9fS6M2XE_rfkWwCkz_fnWFXX_uUT7PctvFFcnekJttl9DUK8u9harcOhnfpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=qwrC-W2dRYEzbXUIeNfo7KfSDECv_xardCey52-okIQGicWI9kdWuTJIQE5A0OyzgbEETRZoRFDMm5SMwEeMvz3VmJ8e70xQ6bGZKiL2tX-TNQqWrVh4Kp7wFVRyOYG3JY2MUUbmrNSYpHuJqa_Y-eR9cfh4Zf83BXYoiYSSzFzhBQA7Sss4W1zWt3KP3YgkVQ1PK0KVSMAEyTbrLctBfU6vNscp8p6Kd3yW1qmH2OOFMCwAS55x-OjsiR3dnjYFdAXeL65QYk_iZ6n-rxshM5-OkywZHmphooPaDtFLVI86cO8oAMSCICl-DhcStoJPETYJ411y4Aa_AinBPZmpBCWE-b1b2uzLnYlr3RmdVR71m6nJusv0dBL_6W97iVNgawyQ194a3lHckRQqCFNHAD07I5EW_5QDicHCHtgUlwzX81dcLDjnmtd-_2f6_PZ6SGKlitM6v9w8jWWXOzEMDlYSauxbyvd2dFbw5-5O16Ua5BmUNY7vG8voXwzdotNwQFU83-2Gx4zRyuQst_DIXTNDIg3NmqWsLriURqXCRpcJD2e1K1HCdCA2d9OMtNn2RfAaw5Ctw7JBYqLsCjtpAZv3-yPi-kYKnCHu4jg1nJJhlGdU8TP8OdMa9UOKW4OUjohM3aZujCrL3qIvJurZjlfZnmTf3-Zg_S8iXA0BU0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=qwrC-W2dRYEzbXUIeNfo7KfSDECv_xardCey52-okIQGicWI9kdWuTJIQE5A0OyzgbEETRZoRFDMm5SMwEeMvz3VmJ8e70xQ6bGZKiL2tX-TNQqWrVh4Kp7wFVRyOYG3JY2MUUbmrNSYpHuJqa_Y-eR9cfh4Zf83BXYoiYSSzFzhBQA7Sss4W1zWt3KP3YgkVQ1PK0KVSMAEyTbrLctBfU6vNscp8p6Kd3yW1qmH2OOFMCwAS55x-OjsiR3dnjYFdAXeL65QYk_iZ6n-rxshM5-OkywZHmphooPaDtFLVI86cO8oAMSCICl-DhcStoJPETYJ411y4Aa_AinBPZmpBCWE-b1b2uzLnYlr3RmdVR71m6nJusv0dBL_6W97iVNgawyQ194a3lHckRQqCFNHAD07I5EW_5QDicHCHtgUlwzX81dcLDjnmtd-_2f6_PZ6SGKlitM6v9w8jWWXOzEMDlYSauxbyvd2dFbw5-5O16Ua5BmUNY7vG8voXwzdotNwQFU83-2Gx4zRyuQst_DIXTNDIg3NmqWsLriURqXCRpcJD2e1K1HCdCA2d9OMtNn2RfAaw5Ctw7JBYqLsCjtpAZv3-yPi-kYKnCHu4jg1nJJhlGdU8TP8OdMa9UOKW4OUjohM3aZujCrL3qIvJurZjlfZnmTf3-Zg_S8iXA0BU0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=BME0wuLqB4QD362O2cgzE47erdkh1rnxcQTdRmxHn5PwZTSy_5ZsLNw0I9sTdacsVlD5QIEiPLUAL9ysYf5FcaNP_un_EcKsr_nf9RIHRrzXQ0cwAIxbBpGGq4Lmpt9465EUQLwLuGvHJmE-Bil64FkLO6upqAoCX3Zclm_Oe0T_RwSjGEK7S7HywaCOvNslHX_Mx01OyGS98sUsOuZKuI79dmLRbRgmf_WhY1lXD_sj4tL6MTtAgcpu9ZI3JJ6-ovBAsEtm-ZEirhxU4-_3_r5ds9hpjgFuTQIcykh39G9fO6Qi0evTN7sWSP0CC2Oo_F-poIVmXLA8QPVdB83cXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=BME0wuLqB4QD362O2cgzE47erdkh1rnxcQTdRmxHn5PwZTSy_5ZsLNw0I9sTdacsVlD5QIEiPLUAL9ysYf5FcaNP_un_EcKsr_nf9RIHRrzXQ0cwAIxbBpGGq4Lmpt9465EUQLwLuGvHJmE-Bil64FkLO6upqAoCX3Zclm_Oe0T_RwSjGEK7S7HywaCOvNslHX_Mx01OyGS98sUsOuZKuI79dmLRbRgmf_WhY1lXD_sj4tL6MTtAgcpu9ZI3JJ6-ovBAsEtm-ZEirhxU4-_3_r5ds9hpjgFuTQIcykh39G9fO6Qi0evTN7sWSP0CC2Oo_F-poIVmXLA8QPVdB83cXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=IQrbvFvaHI2eQ1wtEtJiD3N9wNxISC7RSSBt1-ndhownlAtTmEFrzpkGiPV1fXT0eFVNyAgVwOO6jcvwiNo3bqpYcHhq8ID14w6y7Enf2xk1VvtgH9r2LI_qR6vTymP9UUITY1c8SIqJsfNwUUwWRteiWRhLBRKSDIis5-1yvSUZBX1-SQhTR3Q7qWjRJ30OVWZ2L9M6caLr4sTO9wuzdpBnvUzAVUMEp2a2zX-zB_JiXl26ikzWOTCO9N2BPDGNcpr4p_4P6rYyyYwlkqjAv2DfD5IfpjQh99BZKzReP1uJ04g2TdPW5tdSeKP28_jZM3KO6nkKbV5eRVs66mLxAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=IQrbvFvaHI2eQ1wtEtJiD3N9wNxISC7RSSBt1-ndhownlAtTmEFrzpkGiPV1fXT0eFVNyAgVwOO6jcvwiNo3bqpYcHhq8ID14w6y7Enf2xk1VvtgH9r2LI_qR6vTymP9UUITY1c8SIqJsfNwUUwWRteiWRhLBRKSDIis5-1yvSUZBX1-SQhTR3Q7qWjRJ30OVWZ2L9M6caLr4sTO9wuzdpBnvUzAVUMEp2a2zX-zB_JiXl26ikzWOTCO9N2BPDGNcpr4p_4P6rYyyYwlkqjAv2DfD5IfpjQh99BZKzReP1uJ04g2TdPW5tdSeKP28_jZM3KO6nkKbV5eRVs66mLxAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ9hq4n2o3rwt5uXQ35iIFyUUAnxJETK3QYquaxTqrdJLtOwwCd5NaUVjNBAHxuXzTIwzzrLEsOK8S9U04lp678h0RysqfkvEqHyfvCLW3ASv1F9uqb4h0BtYVNoOoaTdI2X2uVceWZDM1q7Bcnmwp69pLOJyXd1UD5vmPbYzRnJYjw--q5OrgRX1JxA2DSzn83pFdXV9juNb6V61lgGJM8TIVX-uyJBhUvlFuTjCffC0DL1G4qe62_Bo3u6F4O_VYSQ3zBsUGq09ISU6No-nGLmzW-Y9M0Us1lBCV2gD09a_dYNg3XVECuhXBo31C2w4I-JxTVTa9955FluqQsR5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=HJwACMjd35H6RCLWwTkj6LkcjPrc6QmoVre9RKY8GKM28MPUAysEPjHSULf55vQ6IvLCDoJEDYhmhH6KjZoJk9obX7wWTDP3jDW4AmliD5Yo7bF_W14JcvQAQ3nNj4pZ8Crip5mdy_Gw8TnBorMKUNG3-mriBxyRqb7fJ05RaEhvMKlsFvJEzTs5h09_RWH_xX0tcBXEe7ftTl2bjvoqfK5k4aTPZbisYaYszQq6bZyDaivMOoyXX6hnWYYUOeE6RFVLVlcGW9NGGL2Zs0xXiNU_kLDIT4ldon0rvQVUCdGl0qv8c83P2srOqx6zVNXDavbA3Ps6dnbt8g9oaZKc6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=HJwACMjd35H6RCLWwTkj6LkcjPrc6QmoVre9RKY8GKM28MPUAysEPjHSULf55vQ6IvLCDoJEDYhmhH6KjZoJk9obX7wWTDP3jDW4AmliD5Yo7bF_W14JcvQAQ3nNj4pZ8Crip5mdy_Gw8TnBorMKUNG3-mriBxyRqb7fJ05RaEhvMKlsFvJEzTs5h09_RWH_xX0tcBXEe7ftTl2bjvoqfK5k4aTPZbisYaYszQq6bZyDaivMOoyXX6hnWYYUOeE6RFVLVlcGW9NGGL2Zs0xXiNU_kLDIT4ldon0rvQVUCdGl0qv8c83P2srOqx6zVNXDavbA3Ps6dnbt8g9oaZKc6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_8pvfDrvBBF5bReYCkpBHirCV3gc8C3rZP-2sgUw2ecsSjKDFmHm83eQhUQ5OBSHR3w_6UdxBZIiT-JrPwIooldsjh6fANgTMqqSHhvbhHq-p6bK_P3zF1GZhO-23wMfskzCm3qzqR4E_Ap8osZxOX1R-ajS3FFsYzn-G6TkVeEdPGvgz8oNP9BR_z2D9UmuLT1mDuC5ZknO0wjj-8SytpyMEXg62YcfrJ8_7Ykne3JtqN4pBQSs43Kq-Ziy8kzax10rAsmM1DECpcNGG8-2VltnweKBReQzJEZlistfAIbzvdBHYtaRa6hIM76RYCEeWqskKoGTLbJPcDZhPG--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbRg-V2ITBbNs0NDYXXt5iuAEXA-3ETKiFNJm_YmSj8waqRBKruzLEc20Y2tblHSgni_0LEXmn-WRF9Uwwf-in6nqs0zrZjomr22VU64vyeNY5ejqs7vMiftNrTVCyTRS59mzkIcjnO0N25CC-0N6af1bOJFIBkSRdAKZBU8Gxf_1hlGQshGn2T6GSMEJIjivdlzBGvkWNJDRCTyYfJX7gN04lQAJSQUxrLwOj7dwOMyMh1T6goeYGmKbnQxfECPAkbA7A0brlfRJ7T4lCZd-sPEptcXJzdV8ryrA1FCbL1-7JC-ABPGVLocqgEmLB7anqqOfcqUYYY48tTVsekoag.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=bpYxcP2RE9_Bgb_gPYDNvauVFAAeiL4pjlpSIfoGZVGGzFpkV4UxLWUHudFRMWE2e5BCgQui8IcomuP1HVJdAmEdv8TsWj9A8QRGgiwDIjyrbaKlHjf0TZKppyefH-2dC2Qx9ywMocgp7392OMQihLEADcX9VFhiGQQDaEOuBfJdcFqi14Qg-RSX_Q53mVy_z5QOul6iE3FET20ICAQmmT6bwS4IAQJfjiJ9ZiH7aMLse-iRwlB99N1t9-vB0mgvwknqiWkCOJQl9T-4NwifppEVhBYl1Ym0ZzCFk3Hofgb9fbZ27dqnw995VNd8pzneo-4wH2FgpKFB8vFYpmTruQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=bpYxcP2RE9_Bgb_gPYDNvauVFAAeiL4pjlpSIfoGZVGGzFpkV4UxLWUHudFRMWE2e5BCgQui8IcomuP1HVJdAmEdv8TsWj9A8QRGgiwDIjyrbaKlHjf0TZKppyefH-2dC2Qx9ywMocgp7392OMQihLEADcX9VFhiGQQDaEOuBfJdcFqi14Qg-RSX_Q53mVy_z5QOul6iE3FET20ICAQmmT6bwS4IAQJfjiJ9ZiH7aMLse-iRwlB99N1t9-vB0mgvwknqiWkCOJQl9T-4NwifppEVhBYl1Ym0ZzCFk3Hofgb9fbZ27dqnw995VNd8pzneo-4wH2FgpKFB8vFYpmTruQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=oORwDi6QL-pNf3sstWN9ZyRRRmn5WEWRtYxUEkNqaBigrcsQiqUghn1xSwD3JFnYobcm-Latu5wmEYOA-aOxYnhZIpVEfKrNgqkG8ECr687vZzSlvTLgsRwJWdbJbUyQdKDtq_Qgh_1dzIVXgYKfBKvSDDMgnotdp3xZkY7cHfCeri7-ASM_Xy_BmGfZY3J5xRzyHqVkF46gmt_wroOElgch9k9JigR60bOtXOOOxSEN3zDl0ugmhNcl8bToD5HPmSw02j3fHgt6Bxvftn-KjtVGbV7Elg_U4ck2wq_5GYFUKe8ybGEk3Fs2sIzEbJEe-YYuuBllwEc7pZ3srxQJTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=oORwDi6QL-pNf3sstWN9ZyRRRmn5WEWRtYxUEkNqaBigrcsQiqUghn1xSwD3JFnYobcm-Latu5wmEYOA-aOxYnhZIpVEfKrNgqkG8ECr687vZzSlvTLgsRwJWdbJbUyQdKDtq_Qgh_1dzIVXgYKfBKvSDDMgnotdp3xZkY7cHfCeri7-ASM_Xy_BmGfZY3J5xRzyHqVkF46gmt_wroOElgch9k9JigR60bOtXOOOxSEN3zDl0ugmhNcl8bToD5HPmSw02j3fHgt6Bxvftn-KjtVGbV7Elg_U4ck2wq_5GYFUKe8ybGEk3Fs2sIzEbJEe-YYuuBllwEc7pZ3srxQJTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=W3OUaUdRZtTtAG5rPxGAgJJ_CQ8TKsT31Mlnv3ORo1h3cZpdY-51yr4p8z8ZRjb-Njg5VhcZSTOnbd2UQP1e641emyYZ8eEjPkMk0Lp7BK5WdPsAiv0pMsqdBoWZ9D1hV-cQcxxTXdy827yLh5so7RTwgOKClSloq9v0TT8YIi10DmuBNaCDST27jOaDoYspgK0tmut7x0v5xpTlpn8h4-yIBkjO_IfLyuM5T5OLtY-eGUJFKy8muX5-zEWQmiivyGh6WQBSohH_Bs9_qqpgclGXOzecgwCpDiz26JD0pk50yFBXQvDcC25tpptbVg_NrU_2647C9TwAle1AZOEf5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=W3OUaUdRZtTtAG5rPxGAgJJ_CQ8TKsT31Mlnv3ORo1h3cZpdY-51yr4p8z8ZRjb-Njg5VhcZSTOnbd2UQP1e641emyYZ8eEjPkMk0Lp7BK5WdPsAiv0pMsqdBoWZ9D1hV-cQcxxTXdy827yLh5so7RTwgOKClSloq9v0TT8YIi10DmuBNaCDST27jOaDoYspgK0tmut7x0v5xpTlpn8h4-yIBkjO_IfLyuM5T5OLtY-eGUJFKy8muX5-zEWQmiivyGh6WQBSohH_Bs9_qqpgclGXOzecgwCpDiz26JD0pk50yFBXQvDcC25tpptbVg_NrU_2647C9TwAle1AZOEf5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbI-MEtzuHrk2u_hrlf7v0gGpNbupl4soozBOYh0q4vYQQyToEJlvkO7MI7_k2dkGZe9AVvObMpcMVpodvu_csB6BdmwQ7C2mjB4K0DO7LouTeaDsmrjiZiUGuAzVA1YHCJ4yy6HS2cUa6D48mmSrxsfk66RMcgyfTbeadX8YMiiuXgI2gIHSdmL2sSiJFN_jCggyTzBMUZ0XfD3EJ4gSmwY9m5ym-QbvP3xZqj9jmL9V1UoinI1SDxH3Sl0Cn2shp4D7leCeccN6EDSLR0q6lLNW8HNj6_h9Yzgq5rxCDr4lTLucaNfKkvLK2mMSBIoiKfN2rqDIsVKcMaX2gBDhA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=pMGNSDnUXE85e3VWCEIGiAcvRdPeLxJOXgBcw5RUb0yh7qoZurByrwash3-MSvMLpLOGl4C0_OjOspvWRABTsi89FlR8a6fh51Da31_w1f3nuIZpBsoaHjgzD62UjotkhLuYEWuSJPhkcWnEPcNq817hj726FPPfT6NAPIgRwzkb1mAftyQZ5nYZveAVkslkXmA6sI4snWtYaO2favISoh2xyEDEXQAEYVavnPf_eQy69OjkqGF4NqLLT0rzFIf8GT73RZf8rM6JNP5YOPvsPOHo17RnwxGexcj7kMECFlbgcFnn190F3Z70xoh9FAWCo5KJ11yefVK9FYloyPAAwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=pMGNSDnUXE85e3VWCEIGiAcvRdPeLxJOXgBcw5RUb0yh7qoZurByrwash3-MSvMLpLOGl4C0_OjOspvWRABTsi89FlR8a6fh51Da31_w1f3nuIZpBsoaHjgzD62UjotkhLuYEWuSJPhkcWnEPcNq817hj726FPPfT6NAPIgRwzkb1mAftyQZ5nYZveAVkslkXmA6sI4snWtYaO2favISoh2xyEDEXQAEYVavnPf_eQy69OjkqGF4NqLLT0rzFIf8GT73RZf8rM6JNP5YOPvsPOHo17RnwxGexcj7kMECFlbgcFnn190F3Z70xoh9FAWCo5KJ11yefVK9FYloyPAAwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=baqxYgwFipr-1JLvFYjxQdwuKzDSVidtktHy_3wz9M_Rl2DqQ9iFRwSFLKkfrD9ww6oe6ihCHnLztFxd7NCr8ZPkP8uupuMEj5t95OehujkWQhOpcKuXs1Wv0K4i-xSixNDkbJ5RFMnKBkJtd1wRFK0UFAS8M23pdrY68XOA6QQn85rpk1WSh40K1p0__uIXQNrhlyyg8uz1p3p7zgne_pnwakwaKAzTIT_UoMAjCxRKCyt4A7VAF9GTPudaOL7GGNpkYM0mHvjpoeI_zsJ_ATbY2cRbQnqej0RnLREZbTUEQsV4GrXByO1FYt8xIP45GIl6VGqKbmKxeGthDE-D6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=baqxYgwFipr-1JLvFYjxQdwuKzDSVidtktHy_3wz9M_Rl2DqQ9iFRwSFLKkfrD9ww6oe6ihCHnLztFxd7NCr8ZPkP8uupuMEj5t95OehujkWQhOpcKuXs1Wv0K4i-xSixNDkbJ5RFMnKBkJtd1wRFK0UFAS8M23pdrY68XOA6QQn85rpk1WSh40K1p0__uIXQNrhlyyg8uz1p3p7zgne_pnwakwaKAzTIT_UoMAjCxRKCyt4A7VAF9GTPudaOL7GGNpkYM0mHvjpoeI_zsJ_ATbY2cRbQnqej0RnLREZbTUEQsV4GrXByO1FYt8xIP45GIl6VGqKbmKxeGthDE-D6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=W5d6_I3vlg1uBKtTLVokCTwMwmLtQdHmZ6Apl_QXvzoxeCpHSBoxD4yqHiUajOgZgWcpLHPoZPAWrBLVRWm9EZFLfhb5et9bo49d62rJS-hLIJNHXyLmsAbrG8KFaThiEMz6a5M_5TVuGf-rbhzHmAXug1jCXdscCUJCHZi_1xj5SwXC_8nbECD9vOrRbGb_kaJ9sbw0xNtfwt6p2wmU6JS9mJQzxAb0a4WJkAyQKN20AU0-PjHVNdKDs2b-FHu6atOeH-KE7h7vGwmThwFpPcdaWMf4kQkp78-YVfBX_e0cAo6DP5W0FmwauLjMf3IaTAUFU2HCKqoqATyL91GfSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=W5d6_I3vlg1uBKtTLVokCTwMwmLtQdHmZ6Apl_QXvzoxeCpHSBoxD4yqHiUajOgZgWcpLHPoZPAWrBLVRWm9EZFLfhb5et9bo49d62rJS-hLIJNHXyLmsAbrG8KFaThiEMz6a5M_5TVuGf-rbhzHmAXug1jCXdscCUJCHZi_1xj5SwXC_8nbECD9vOrRbGb_kaJ9sbw0xNtfwt6p2wmU6JS9mJQzxAb0a4WJkAyQKN20AU0-PjHVNdKDs2b-FHu6atOeH-KE7h7vGwmThwFpPcdaWMf4kQkp78-YVfBX_e0cAo6DP5W0FmwauLjMf3IaTAUFU2HCKqoqATyL91GfSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrRPj-uRukWpTeB-dAgaEID7miK45ee04P1rWSH8F-35OvV-FyJTTe7XUS2uJMQAZGCc1LDTBIi8lFw6Oki3YHW1wUeUlKZnbLHLW_8534PKBymHL8oRa8Cq4yB14dT_EIuETftfqqLYD11ljvufXlqWE4Xxcv5_nG8xIbLMZ-z9Da0XjX75P4hEpyASQpP_SYakaBfA_Jgv_D7rrwf9YOZDv_MoDtv-LaeU0WoPMLI7qusKBS2CuOUoZyGTHhHsmbHEjx8ekoimsg8lk97C06eCZzbJUoCtjs8dvT2GoH8dAkCQTd4PDI3kCbGma37DeFgFGbhZzkuGgP7sTxKt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=DcM1CfT5lBi2OVgLTXktNLbIgutrKi4TU1-DdYMRQnTjRXwP_J1YC-j_GsBQvKCxiCgUdcltKjSxqf3gPZtIfzEtHc93qTXD-ZcplCR-Nk8uErPqcJfhvKyg42Gz7YdBd7Ct8d_D_DTn_ylBMpd3WX8irph4UqpHj-g7HnogWWCSqitREBgFDup1qISeo9YTS1jYLGhuZO1rLpBWh0ipkTS640gAxho752QIe4LIAPwBl-IMM2AbiziFSUtmxgVASLj6xYj5Bgh_edYtGcUSOF4Spnp1FwGmgmx7QkRVPyVk7kVNZrJIOf4GjEk3j7eKGESlqtANN7zW_nuNSS3gvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=DcM1CfT5lBi2OVgLTXktNLbIgutrKi4TU1-DdYMRQnTjRXwP_J1YC-j_GsBQvKCxiCgUdcltKjSxqf3gPZtIfzEtHc93qTXD-ZcplCR-Nk8uErPqcJfhvKyg42Gz7YdBd7Ct8d_D_DTn_ylBMpd3WX8irph4UqpHj-g7HnogWWCSqitREBgFDup1qISeo9YTS1jYLGhuZO1rLpBWh0ipkTS640gAxho752QIe4LIAPwBl-IMM2AbiziFSUtmxgVASLj6xYj5Bgh_edYtGcUSOF4Spnp1FwGmgmx7QkRVPyVk7kVNZrJIOf4GjEk3j7eKGESlqtANN7zW_nuNSS3gvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNUK0fgKH1lYS4fwAeoT0_NBhIGKgfBuZDJM84IcFJozXc-vs0ohfLY-xYktI63DCZKHnGBLuiK383r9Kt-BouBDtgUG5GTxBbiqWnbQQmRs1h5wNL8Gp2lZP7OfwzdYu1OFR8prSR5SQWXV6aKcnGVy-yDBRxAkMHDSUuGeZkR_E9cRGbyeHuWBHpIaNFMhihRz3hY9GIDq3-Ja02X-DxxpWywykt_gRHZtSDOyO4jNmUHInVccjNbn9J1bGpf5oZtc5Tvqc6d7wHPHk_vR4QipUvlWCAZkhZIK8mL5l314ITU8fg_F9bi9fW7S8PAjg4VHs1t_DBJKW68Pc8iUIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=AbXC7vadxqaSLuyydwe35NcCloVN89jDexWAbHkEY4nnN8CV1-_wgysRk_ZyATnPLB4HiRk-YnvLmMW9EcYUc1sH8_ru6Y_klr7vtO3uXQ5VT8ofWkGDJbvAH7UM2XQkDBLu67Lhx-q4aSUpMyf_uQE5fiN6T80vXzprGG3bP0T_v7wNToGDv6DelnXYfa_wd1UuQzrwgMbOZCHMYgFVQoNhFdtC6mlbA3vlHbYREO7mBGgk2PTzDFdiF6nhTFtveE-v6eqbsQwfhCUcXQo3K117yz2vqFJ-4fWQ4ju4dFyaSpaxwwcXfENDxjE6AZhpQ_PXpXuOXUjutS5KoUjuMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=AbXC7vadxqaSLuyydwe35NcCloVN89jDexWAbHkEY4nnN8CV1-_wgysRk_ZyATnPLB4HiRk-YnvLmMW9EcYUc1sH8_ru6Y_klr7vtO3uXQ5VT8ofWkGDJbvAH7UM2XQkDBLu67Lhx-q4aSUpMyf_uQE5fiN6T80vXzprGG3bP0T_v7wNToGDv6DelnXYfa_wd1UuQzrwgMbOZCHMYgFVQoNhFdtC6mlbA3vlHbYREO7mBGgk2PTzDFdiF6nhTFtveE-v6eqbsQwfhCUcXQo3K117yz2vqFJ-4fWQ4ju4dFyaSpaxwwcXfENDxjE6AZhpQ_PXpXuOXUjutS5KoUjuMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m97Ma3EjlikGs6HokOtg2alb9fXIDHfuyOc8ut0ufpIx7fRnIlbbGvKgYt3NDEQVzppEEPuyDmPCF2218_-Kak3V0URu82aiDU8uC6Bgn8JfyUY19rPubn9T737WF-00UrpoBYeBUSragAuNqe9jxAno8nqXxPtBapM5oNHHel4tUS_qbg5VYkNizggeqi6fX3jqpvXP64sxzLSoi2oa9hzJ8ddr-Yq78CL0nNbHQ93agJjoGhGTeoFkO3Ok8UNR2rjfEr26z6S0WdpxzyzvltfLRn5tvXtVzXrmZIO0arMajkENtELux3Vmnc9jzyd7lGIXIvaYsaPduQkqFpUF2g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=lifdPw-YSfrqZQD_srJ9nJtA0lpXPl1rZNVbRqby_q-Q26SwTy4H5cj1OO_sAUDN7kKxRlOxE5ABPYdRFdMTVG8qjFuMkBMjYKtUMc6Rmzzc-pMVsswpQ2uyYCfnzzW6_vfASUNMJGoqMaWgI4cQfYvbt1ifcBrgtRgSZZ6WcV5ml08rgHcYOIjTdAatrKyv9pt0skPUk30-xtFbbuYFWPcGDjWipwRSHs5RZd0QeFzkBaaitil3FlU3OdVAW-yu-K7dliLIwwm139RZWEsi5S2XyZNYUGocMWqNNSuoxUWLtn4KVtROK8Slpum8T7fD2V8cKve68oPXuVUs41J8Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=lifdPw-YSfrqZQD_srJ9nJtA0lpXPl1rZNVbRqby_q-Q26SwTy4H5cj1OO_sAUDN7kKxRlOxE5ABPYdRFdMTVG8qjFuMkBMjYKtUMc6Rmzzc-pMVsswpQ2uyYCfnzzW6_vfASUNMJGoqMaWgI4cQfYvbt1ifcBrgtRgSZZ6WcV5ml08rgHcYOIjTdAatrKyv9pt0skPUk30-xtFbbuYFWPcGDjWipwRSHs5RZd0QeFzkBaaitil3FlU3OdVAW-yu-K7dliLIwwm139RZWEsi5S2XyZNYUGocMWqNNSuoxUWLtn4KVtROK8Slpum8T7fD2V8cKve68oPXuVUs41J8Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kzb1z-kdfJc7EAnEgeYdAE0bI5KpfePn-NfzoyE_UdEx8Tpz8c0Y7Jtd9LCMylSrehYLW431LWpt74invSpqF9hAf9eE6_sX-Je2lxfdrNCbZYna84GzAXiEVyPMsvFaASSYB5HV8q9vSenIQmB_u0R_zMKaQZJmviotBcRE1v_wrsrlzJoXWGQOWrwMBPmbCtgIxSZMc0uOMB4Qlf1KDTJyWr2Xf4IURll7aCNrRpPtOdN_EC19yJx1JVwz5aYzqHgI6kgmuW6i0dlzuorgp87EcTYFS1_tMaRo_Dy4szwdBXudlXwhl76_9HsbZCuB3Kxj9ccJjtY8Q5EA7D6hgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iamKu77dNgnRpWTKJG1U8K8yf0uAmcA58SBIKGBZQDzK2df6iww0GKo_q8vFV_bPP85Btv59G-VOvuKUAhGmyhyYAD18xdfqGFfUWtpN8XlraGZGALWZ6ksseHz-HG01QaIbQI0ezZdOMuv4ixI3JKvOqZQflxu1vYItJc9tW-SckST6PRl2QUV7PQgGDE3agsAyeqG0fxEGlwJ0PANFJEVZXJBQU4bGGXaQFebHBge14k-qH3puk9ThTsLzceTlWckLHqOSUVwX3sg1PhlcGATInpRUrPKyWdTTQIwAqNvKz9C9nZQFJOncNUyy6xRx6eittIVzSVjCo8C4Mq4iiw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=O25kM5Cjfr86BUwAjxPJ35yenM515jmB1oP0G9Xh_gS6xWZgQUcAPXIYDEhUyQSmX-yn9iQWS6683ei_ZRg_BRHVXFzIEc_RC-cornM9n7jMVqWaQ1K6OpBPgPZFsUP9qs8jLi5ogWPjUSG_CqUPgi8uj2oQGfkB02rfI7Mx_ulmewpCGYPbRGwnwaWUrtGAhI7fV_-EHbtUQPg5GnN8bHyd3DVTQnMms-WLf3zzkKcAD50Z5ahMaHSV18hi6A35cAM5Di-tpIu1ROiesg1iBnAmYAVCja1gPSEAgD9XOM2eOQCG0NxS_fZiMMMYuPqbW9uGMbO-UMxYvxINd-aZug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=O25kM5Cjfr86BUwAjxPJ35yenM515jmB1oP0G9Xh_gS6xWZgQUcAPXIYDEhUyQSmX-yn9iQWS6683ei_ZRg_BRHVXFzIEc_RC-cornM9n7jMVqWaQ1K6OpBPgPZFsUP9qs8jLi5ogWPjUSG_CqUPgi8uj2oQGfkB02rfI7Mx_ulmewpCGYPbRGwnwaWUrtGAhI7fV_-EHbtUQPg5GnN8bHyd3DVTQnMms-WLf3zzkKcAD50Z5ahMaHSV18hi6A35cAM5Di-tpIu1ROiesg1iBnAmYAVCja1gPSEAgD9XOM2eOQCG0NxS_fZiMMMYuPqbW9uGMbO-UMxYvxINd-aZug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2d9AFoScAOFouOHvcOxSOuV2Cwaw1rLRGM7HAHntEw0u1cYjTFZfAje5XXU8TM-a27w846cRY4M16ZKyXaPUlQ1PKKPl1aWgYd3xjvsgtl89t0earkNexhswntlvkpR4sQnzUiOmPj3LaflJjCDxvqVm0sEpVa6f3xygHwGvBMBUMJ9NWPdWfztWM9K7EiRvMm-rK2VOXf1e0iTQ2LZlQ8m7hfrUk1wAOT4BoIJ-E2kAXzsiJcMFXmXW7GT8QsUvGo-ui-X8I33mLHRY9yb3kz_MZMRB-8AfD0yvxtJh9lRHk-lqO3tDBG2wrSGtDJ9eH7x5RnzU2mWQabsFbaW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRb5wM7QPz-MXSkCqQ9YvVPVsiuej2TVZSYN0q8E-fywQUZRwQaGPTbH0nxuRfTMAqKMhUIx5fD42O9DdglaTdDKn_bUZvpN3eJ2sTGiOyNvHwvrSaWN_RFFcJYNORpIoUs6zTE1epsysZI0hfw6aM5mpHdgVxW8xVa2bFdvGskP0lCwY45DF5AyKdBARPXhKHfvPZ9ieftJHC4QwLC4dcs9AHSxFf4WMijC0zSYltA-Uil84S7nlZGldkdGnnPO1eGYpWyeozQU36W20IK5ZWuTLrgrel8ky3kb_OdAw-f5bytgNlKYLslj9I8WCkjb9MMjZcaw75Gy3yVY1JNUkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCI9HtSaCWvmASETJh8KzPyia_m_Jtbs-uwRslxq95blhVe44JFae5fkkMilipWEuqUyT1TeSVxsWAE8e0aSmGzD2xHnFPA9aSQFEN8cWuvex9ZaFwlzTgh5CZ9rt97Lt-CIHKc37VrT9isMh55DoZwYp8hNNtc64JCeoJuXhD7HXeplp_jOovZab45FA0qLjb_MmyXlgZ6nKmk6hZUK1gfxmruWSciTgDznUAam1QRsnb1tXak_5do1lQ6a-IN-NkXb6kfFNzLu7C6d1ZJw-q6xTf9MwwXlEyvnEZfKHe-UiHiiMIvbRrPdsFqYTHRdk0YUNFma-a4LPtwl8dObcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtpBBzthuVf-nKUEY1cNvVni4fLYQ8hNXahWdyLddWGDmKBwipDmor5XH_5WlPuCiLwpX-OpAgV5jC06Ul7hjvb3djNjoRHAoK5CpxN8ZUDW9Dh1w6PG9OGriFy_zRfocXSg1f4_mFMcsp4tfUkB-K41B6RFxZ6-9_fa5KiT5zAcw8WqhhJhjmLaP8d_2XIhRehC40YtU9Gu0lez-v3px_hsYAOJA3cgZRg5vKk5NG6GlIt9DS2aXmCAfp-YOIryEDYU9H-x4MQuhxDLU8bfFQDvHXBmv8StyMr0cQ4atXr4gj9RJV1k_VPCOFvuYqpITHN19FryPw8CCil8svLU9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZP1n1GUbAeSh8WyaeHqsf58Do9PxsBDLY6R8xIADUIJOu_GQv-aDIVvQG7PdW2KOaeQuWdYfewoU_NbDzV4v1plLAK4dkArYMVB9h7U7b7GFXEwEZ3CgeEb6lr0u3LXMZ8W88i2EQ4PpWzShldiWD8E8gE0ANxFicPogiI8EP7HRg6ySDSjRB3c6h7W8T3TnJkw_-VmXcq9y5wAQmESUIUDdtrBRoXZpDIEDoMkGmHwCcR__B6yIZX27sOyUJRfuMUT8LT17EZXQG4deLcNrrrHtOl5p7zdc24BSV-zuKLo37eGrUl6n6aTsxW_oIIsxO4rYEnqjjpMbbznDgvARsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=MPtZT3LwO6z60gRZHNdS3aJfrEFKOBXo0mugIVUxIc_Ey5H7464ADyWANkPXUxY5DpeG6F9t5IHeU-bnFM3PE6ASajx8zzvJmQ-H6iD8i7T-E3JEKfdNqBAYPg_0YMAW5br1z0p8lNZvSMrn9SJt-wv9TM4GGHPYp9hm3SUu-P7jCxGzQOVUFTGa9i_bC1xeWCT7-BpytQf9KOUec4lL0KphnvNak2DCpyiPq0viiPNTuGmGeN2nvBpnEd5XPXvshNK2Jeig1Hns0iHEd2-feggQ9jSbCNDHTiaGb-yV1UP1KPVmLreHO0X6Zt6t0HV5GlTlVHXNZbqN81svLxHcCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=MPtZT3LwO6z60gRZHNdS3aJfrEFKOBXo0mugIVUxIc_Ey5H7464ADyWANkPXUxY5DpeG6F9t5IHeU-bnFM3PE6ASajx8zzvJmQ-H6iD8i7T-E3JEKfdNqBAYPg_0YMAW5br1z0p8lNZvSMrn9SJt-wv9TM4GGHPYp9hm3SUu-P7jCxGzQOVUFTGa9i_bC1xeWCT7-BpytQf9KOUec4lL0KphnvNak2DCpyiPq0viiPNTuGmGeN2nvBpnEd5XPXvshNK2Jeig1Hns0iHEd2-feggQ9jSbCNDHTiaGb-yV1UP1KPVmLreHO0X6Zt6t0HV5GlTlVHXNZbqN81svLxHcCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=ULKg4AwagTJQp0_dAcaHzkVQQDrrHIYo2fL0u-hZPzOsmjb00rKmMQNtBSFVXWWDJa-lhw6xHfDEzUMysnVgKuw5LWcDAZ4j16GNYCMNrfUfywSIbg8G-VNytAF734rY6iGKHTnVJUbRU6sGgIprEUx2j90-t3Hv0EkocXezH8tObwkieylxlWpyc_bcTpt_OepEcXsWt_ecN-nzVPInzCiwAiePJqChb513qdX4-6vRQiOyYZtg4C3ni2T6-bfr81961BLljrEdd00ey1Edxfd369gr2HCPacgC8Hp2DKArr0Azu1kM9_7PHY_hAbFZrCD6fTJyK6EhFhxFpkgcEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=ULKg4AwagTJQp0_dAcaHzkVQQDrrHIYo2fL0u-hZPzOsmjb00rKmMQNtBSFVXWWDJa-lhw6xHfDEzUMysnVgKuw5LWcDAZ4j16GNYCMNrfUfywSIbg8G-VNytAF734rY6iGKHTnVJUbRU6sGgIprEUx2j90-t3Hv0EkocXezH8tObwkieylxlWpyc_bcTpt_OepEcXsWt_ecN-nzVPInzCiwAiePJqChb513qdX4-6vRQiOyYZtg4C3ni2T6-bfr81961BLljrEdd00ey1Edxfd369gr2HCPacgC8Hp2DKArr0Azu1kM9_7PHY_hAbFZrCD6fTJyK6EhFhxFpkgcEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=U5kwK0DZHAKYxlfoW1ErJ15Q0LJvFs8NJHgtS7FeX9Lf92hQWigE5Er8uF5F_jhCKzopXnpVUgwvfEZ4HSxtabq6q_Wpv_abkRLE4dJBUfE2Ffd5X9PKCaAFVrzR9w_A52hxxR0pUk0gNPY74rlBhvWUrugqHiAsq2lmB5z-FacgoEa-C5KmTouEEet9UQaR6adWAMu1VdDX8YJ7V4Bm1fw_2mdjj3yflKPkM6mLmPQHJyyBy9CHEmVOiNTTbQxeCqDFGPVfiTOAefmZSHhkuExZ1Y8NThexC92yTkIZ0yJRTDL3Uatn8iCw0I6wfm2TAbms3OftMgGnON6Ur4e0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=U5kwK0DZHAKYxlfoW1ErJ15Q0LJvFs8NJHgtS7FeX9Lf92hQWigE5Er8uF5F_jhCKzopXnpVUgwvfEZ4HSxtabq6q_Wpv_abkRLE4dJBUfE2Ffd5X9PKCaAFVrzR9w_A52hxxR0pUk0gNPY74rlBhvWUrugqHiAsq2lmB5z-FacgoEa-C5KmTouEEet9UQaR6adWAMu1VdDX8YJ7V4Bm1fw_2mdjj3yflKPkM6mLmPQHJyyBy9CHEmVOiNTTbQxeCqDFGPVfiTOAefmZSHhkuExZ1Y8NThexC92yTkIZ0yJRTDL3Uatn8iCw0I6wfm2TAbms3OftMgGnON6Ur4e0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=tU2sQxO6L94S6tKdDCkyfZEBUsvei4Rq9N3n1g-gKE5wz8-E_F6NY4OQfknfEwAwbnlorSrZRdkQVTSHJUoFfziLOmOm5S5o-iO4-2N2sGMJYv9rhBvfGDlulNloZx8w04QEoIQWSmHizl4DRhtN4KNeYpi3JrbpHRopC69aH7ddvyzxUriR1WfTX4lQFl89seRFqF_qiEN8J9Ua6xrOcxdh9ESjCpzHWS7P83xbvfoX5IZcD3x34rQ0fNp1s-UURUe_EwSJSUpvO6KW4-skAkBCJtY1XDHhGjul0VTs1dX-rlIuA2I3vU-71F-hxCDmeIXqdb4W8LT-XZSz1z_Vwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=tU2sQxO6L94S6tKdDCkyfZEBUsvei4Rq9N3n1g-gKE5wz8-E_F6NY4OQfknfEwAwbnlorSrZRdkQVTSHJUoFfziLOmOm5S5o-iO4-2N2sGMJYv9rhBvfGDlulNloZx8w04QEoIQWSmHizl4DRhtN4KNeYpi3JrbpHRopC69aH7ddvyzxUriR1WfTX4lQFl89seRFqF_qiEN8J9Ua6xrOcxdh9ESjCpzHWS7P83xbvfoX5IZcD3x34rQ0fNp1s-UURUe_EwSJSUpvO6KW4-skAkBCJtY1XDHhGjul0VTs1dX-rlIuA2I3vU-71F-hxCDmeIXqdb4W8LT-XZSz1z_Vwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QO-D1JWZGxLup2VPbB3P2FSwyQ5b5wCWBCXBhQm_NrIDUCDfb6NO5bZ-n_7GC0_WtbGY5wBguMOhgwzFt60-twO4J9aPivS7NqPnqD0U9pCmX694Gb-9RgMaeR_hCAMLjLcMoh4VOiqexCAy5byhWgVTgoE4BRIDDkScQ4DSKuRK2sttujrCkSQ582gJ1FngUKLPun1FMGRewqUXOgSlt91EQcv2399HOSwlBUKCqiZ8UXequZXWBgkyrfA_Qb5LWoEWWAKA4Nibd3qx3MNpFwAgn9nTW0wLihTfICGrbQhShAW9O4pVUjBtXkDrJj1PiAO5FQki5iSdY0jE1dh_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrOt0Mp_rAspsTTl22IpREa3-ezGddAQ8O8Qr9vhnAEtpvtAmdaluzybdeEey-U65Fc6CuxndPtafggQy0RnOdIMrdlT1LowX_Jb6rIsk2i_8cQsMpJvYFu3WMz-Gmty-ASNI-rvftN8bhIwCDjmteaiGanVgeCtQ4o0JNRalZZ1ydHxJ1VPGsiOsrVlFHgQ93IwHMROEpBPz199AcfPq7yiPjOv0_x9QuqSyXlWHkP2obRg_NT1o040ayC8kB8Ru8shGHXvq4zxjCL_A4DQvzLkhym0lyEqeoMJKAGhkOHP9QPQBJyhY3cq5hekonNv1ZL0-phHj1r7SQ-F_w9Seg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=pMtLVZ7wvA4oYMMt1Af1_r678SanmIP16VzIwpSQMACTVrhVN6yZCTrYZBdbCbd7KAkXm5MJpB21HMjVpLu4tqlizhjh0LLwVRO-AkDXXiTybhF2L23eO_xwCqeMPNL9_tcxXzWuId0RDIm9NaiqW7Ngw1naZB6DLOE8Tj6cz4hjuT-fPPosQR72o6KXwzxQWImsO8DNZl4sDz8cY7awk3i2QOvO-gedooY__On1xTyp3r_wYojsdtfVGndEcbwvPD6tvmU1WDlFW0mR-UM1JxKz1SdXza_1vsVPnHyi-LjmGXZFzdrifcxcG1RE8cI2sN0dJNuFTcw8OjFRlVmtDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=pMtLVZ7wvA4oYMMt1Af1_r678SanmIP16VzIwpSQMACTVrhVN6yZCTrYZBdbCbd7KAkXm5MJpB21HMjVpLu4tqlizhjh0LLwVRO-AkDXXiTybhF2L23eO_xwCqeMPNL9_tcxXzWuId0RDIm9NaiqW7Ngw1naZB6DLOE8Tj6cz4hjuT-fPPosQR72o6KXwzxQWImsO8DNZl4sDz8cY7awk3i2QOvO-gedooY__On1xTyp3r_wYojsdtfVGndEcbwvPD6tvmU1WDlFW0mR-UM1JxKz1SdXza_1vsVPnHyi-LjmGXZFzdrifcxcG1RE8cI2sN0dJNuFTcw8OjFRlVmtDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmiyVSPkWA6m3HvvUGDFbSzunAQQGqs3MRwvy9Yjz9kQNcimfQJPjk-Ms_Lq08RRa0ByPc-8gkBHveGPFHksRwBiUJFpx9fUZdRAdhHFMXVHtvkZtKVCF8nWxEUb834PeaA6LW4tRbwfk6g1azUQJUuXCOcL3ndCnbyIKphFvG2nqMRwC0gWLE4OThgnqxQdcLsmRoSzK5ClecxzGag9IOWn1KDtU2P53imUPjvGfqClzR0U_Zh3upBgYQ9gJ7yfCv4ZbW-OI4dEyKQLybPhcqUz6WRxInYC0ntRetLoRI0Kc-Q3yrTO8PodmfZAMCo8VCPSdvLiWFpJMnXjmwni5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=MhxHhEO8-h5S0PPz8rs5W2X1xEbtg1zHXeJN2c_O5SytVrjcQzBJ0fK03YnZol6myWLfRAD5YQ30DE_0ylmy2OMO9gFM9Q66wf_X0IBHEoJOiJhOhb33BO6T4MA6X08KOlJgSHmrHqqIpabxzFRByGKX05ivOPsqgl7zZtWlomnekTg9CvBFEKt5M_VHQH36SgUQV1AhmbsOv5M1e920JR92f9DYU_7CegViTBKscslc_TnSsZFgd9A-hnp5UTJSbbW-RKYFYp8QoVrcyCSA4V9JveogDkipt0ojdva_JUFcPC2iYNg6igSd6kniUV7RI-RWQEkZf49NxKIXeHahZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=MhxHhEO8-h5S0PPz8rs5W2X1xEbtg1zHXeJN2c_O5SytVrjcQzBJ0fK03YnZol6myWLfRAD5YQ30DE_0ylmy2OMO9gFM9Q66wf_X0IBHEoJOiJhOhb33BO6T4MA6X08KOlJgSHmrHqqIpabxzFRByGKX05ivOPsqgl7zZtWlomnekTg9CvBFEKt5M_VHQH36SgUQV1AhmbsOv5M1e920JR92f9DYU_7CegViTBKscslc_TnSsZFgd9A-hnp5UTJSbbW-RKYFYp8QoVrcyCSA4V9JveogDkipt0ojdva_JUFcPC2iYNg6igSd6kniUV7RI-RWQEkZf49NxKIXeHahZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RihmDOTjsGR12DyMbH3n6k6L3zlFMOm8eN_lhraXbzz018qSON75won0RYUUmEYIABGn_TPkGFjmDV6p6sm1Qi7hY2KQ3vOnDt7Ss-sbFK5SmisqJ-eYU9ye1bkTh2XMIHYgFolz6t-73WJbyRvQyxrTQhrYb0wAuAsBr2KYL1VFx3NOM1fuqjYoMhIaCTlNKnP4sZtYVPPdeV5gIYwQ6Aa0MWhCj_n3ptI15cF082phN-QPECRAku-Cz9nkBevE5xVr7QXOkZ9-BpUdaWqiG6VEWkYNt2bcvpvDr87PQqKflOsy0oUqDzZq67PenhWVZ8miWRMoH0esM0CWN0TzYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
