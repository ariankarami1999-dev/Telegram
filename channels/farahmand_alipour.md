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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 18:41:18</div>
<hr>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K86q9Pgkmf-I0BvRjkhFAAeLnuBPT4wEALZQG9gRi2mIKotW_LU9oUFhz13Yg9wjUD67gGD-bXHrZ9cuLM6r9RUd6Y7wGSq-te_T0nixa-QyAPkCcQnARSM9irxQBQGR0k4FyxXamoTIpHDdvIQwI7TSLMxTnjCzTEVFe1sjW1hlJH2tTuCuTp4eMvr8cIcE1FjDF9VNNoQua8vcNToDKWvH0ZZihpe0AZZeIiuhwEmS94oNE9zYOBCIXPrGwMgWRqA9mGOtG-6_rRhUtwlRXQrmqPlC-lcGRDJdW9d4XU6oJ1oYKI7RJZ17n35LbMzsA5c5YIlrNzYacJ9dN4m9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9J2WgJ5JE4bNwwdz7q3V2IrUVuUtOyCbKQMhCWopxKc1s6gix1hOSQOB24hmiOoqWoB5x08HGAydJYskEYx9uJ9fB7VnZeWF5pJJpDrJVOMnu_47qlJsqCRfP-HOpzs2qb0DYgznXUdQcIv9l1fZfBnSuOa2GGqlnj7f10NIymfektHzHhIgN_j39xmwWiE4ZQufHxDVJBCArVKFr2knX3wNxadbTNZDzc9agKT5UKobteysFOWA7d5CnI2vyGz9gYz5v9JuSejqwGuFbqIzFAPUn6061WK260Wq5q8Ifk9YPDRe2giW4GzW9wG7cma7pXSGwOOuYbHyQbhN_p5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCbooH_h5rMr1jsmM99DYAG-HBv-xaw2c_9FRrELw__GaqzJrc1YnkKG5VuDUm6P5ChZ-V9zIiklEDwImH_QQbDB0rlw3WwCpHBb4woLC7E3eyxIVfFRJS_tWqzJvrv8FBpoCuMxZmQywnPuKU3fUju_LNRmDslASKsde8z1slhFXxNS_QkBFUCiFl84J36JOXFXAKsKYQiqGXF_GqfhTjmRlBUPze-DN_Tmkkn0KOWLBtimGXpJcd9_nPqyyf2qXD5UC_mlWyIgqHGnnmgQ1OKHxJiMZXUwPSTtC1ofldrgb5yRhwgswZafE6Y0Ag9mnWkZltelSh3rDEUgroy1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM4D2xqXw920j5I9-sKCvfDDKU6t5AhNKkYatnKcd7tyoYkmaeUhgO78sK7G85vU6MyfGE8BOIsXHDeg42fETgvtpANYSdeRfsCn8aIjovbtBuQR8HtHxM5dEojSpN1o7PitmBb4xcOCJXXvNqO9m7jeLwjdONM4vhunTUzrmb6AVzRy2LWWYluO7LsaHMTdPz0fo0KwC2S7WOUqEFZNdTS8J3oEZ7hivBhokMESqW5Cw--Hs8IzErse1J7aHJv56ywILUBFGPnDBXQdh2voFwCwnuB3rB2gKAA97q3tdMur7CkOT-kNgipH2PJCECq_RYmAuZaTgShqZ2Cq1OP1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=U0XYFEb8RKWLLwsMhqzQx6C2Y7QrZ3ewrFzFFqywQgi0fYG7bXsWKw3zACAka8z4of3-tU5fwa3K1tR9Gr_OKhusDRcRPhvW5MwMJY20V8EjSYM0M0BCw6fhZhwCkesv2mkE5ax1NEBkKjYY6qzgh_NxnSEUWwlWzcgT9yDaLXFxAEwuDaTin_TvtN2KIHZUDi7WwLu_yJ806xe9pdEWejsuEMTMN8ayhEUs_cPspEP6cwiibW6Oo5EnwXOsldvHr4e34CM-VER78ixik3sv_v1OFhiilCvGuZs6L7-t2q1MLbz3EOi8BTaR51karFkNREqWVfvndE1mNzrtukpsYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=U0XYFEb8RKWLLwsMhqzQx6C2Y7QrZ3ewrFzFFqywQgi0fYG7bXsWKw3zACAka8z4of3-tU5fwa3K1tR9Gr_OKhusDRcRPhvW5MwMJY20V8EjSYM0M0BCw6fhZhwCkesv2mkE5ax1NEBkKjYY6qzgh_NxnSEUWwlWzcgT9yDaLXFxAEwuDaTin_TvtN2KIHZUDi7WwLu_yJ806xe9pdEWejsuEMTMN8ayhEUs_cPspEP6cwiibW6Oo5EnwXOsldvHr4e34CM-VER78ixik3sv_v1OFhiilCvGuZs6L7-t2q1MLbz3EOi8BTaR51karFkNREqWVfvndE1mNzrtukpsYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=iF2srjxcL4ZBsJCQ_7iGRxyRMVNN1_PZd42nPcbn3iJFyxQRyIxU3xYnN8x9-e9mSE3cJuw-KHn0cM6qoaoCDYByTpW6NRc1Btl0vsdKkfkmMGQpb_-E7uAd0Ct5cI7FFJfrJi8-FCCyoxVf6HJlV801rqZZp5-HvFRbJpDWnN_JW_HRz7uTkaOE9OfqYw3NyKF3Qi0CeG13GG1OE2X7fiXIGQ11U8VDptU7jtSOWweN0YD6rU-CmeYha0wop3LY6Ue91FitP_jZw9ULFwsS1BgaM6Yl1V8aIgLPqhRhGlZFtD6eXTOc90CaJwQmwX_ojzzvUWuiEjw7WJacY0YSGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=iF2srjxcL4ZBsJCQ_7iGRxyRMVNN1_PZd42nPcbn3iJFyxQRyIxU3xYnN8x9-e9mSE3cJuw-KHn0cM6qoaoCDYByTpW6NRc1Btl0vsdKkfkmMGQpb_-E7uAd0Ct5cI7FFJfrJi8-FCCyoxVf6HJlV801rqZZp5-HvFRbJpDWnN_JW_HRz7uTkaOE9OfqYw3NyKF3Qi0CeG13GG1OE2X7fiXIGQ11U8VDptU7jtSOWweN0YD6rU-CmeYha0wop3LY6Ue91FitP_jZw9ULFwsS1BgaM6Yl1V8aIgLPqhRhGlZFtD6eXTOc90CaJwQmwX_ojzzvUWuiEjw7WJacY0YSGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/budDXemWSIQ7SkoDFzao16aXe1hInTtqIATa672agPsa9WF8EDsKLaGZV3l2WyzcdOnzy7lD-3AEzDARLU5DylmTGzy0xod2cYQUoVyaiEDygWz-aP4E3vtWkqMWNxQJMjnLh4M8a8tQhjNAa4Bv1ahYqY2UsYIJXOyQRJwyJ-kc9iYNaeAxPHkEf-9b9jhSA_aFjFd_9BNpDx0NOyB7h1peFf_j3XVoUfJM6YCCcfUQgKQ6TLuUAshceY4M24WeK_XLFURecglGtzjYh-FhsWLTeO-BGHNOc3_FHV_ke3Aq8JfdVy4vhfqBQWEuwqtDN5V_HvOy3tYY31T2d7gnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=OPq3cR3Qo6hhZnA544SqRW1zTB4Nc7i-pxNq6PjN4uhFo-_0wZTHtg-dfM7qan4ntEVLD1WuLx7zl4RzsQBcqfOHiF03_1QHFlLKvVzGwPIJVwi-p6qQ8NIutEXCXPBBndmLWEekyj8ld8uhibLR3TEV92LFVBtzuvjteIA4wDhXKduMmbu4RAkeDixWC4Dva9fREoYIASDk2qsAbgq2ENcoNCsfwTedn__GB8i-9KpYglj2M6TwHWX6IdeDs1plcYTF3Mdghowt-a_liRTVvPHYxlNV8nUTOXWf1Tk3cjlhqvaufI1ZzvR4HSrURn57Pm-0gBleuhi_atNz3OtzRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=OPq3cR3Qo6hhZnA544SqRW1zTB4Nc7i-pxNq6PjN4uhFo-_0wZTHtg-dfM7qan4ntEVLD1WuLx7zl4RzsQBcqfOHiF03_1QHFlLKvVzGwPIJVwi-p6qQ8NIutEXCXPBBndmLWEekyj8ld8uhibLR3TEV92LFVBtzuvjteIA4wDhXKduMmbu4RAkeDixWC4Dva9fREoYIASDk2qsAbgq2ENcoNCsfwTedn__GB8i-9KpYglj2M6TwHWX6IdeDs1plcYTF3Mdghowt-a_liRTVvPHYxlNV8nUTOXWf1Tk3cjlhqvaufI1ZzvR4HSrURn57Pm-0gBleuhi_atNz3OtzRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CcWC1osg0H6kYI9L-mplmOcb2gHOPoYrHBorLvFI_F6NzGmUGHOIbQJwpue_fHeoUSNOM3pjxtn7J4AlzPIe_tBacjr86W-MW8YBhhF8Y2iJEiUNzYoXvfIedYcxk9HO1pZt5qRj_aOSfigwxDN1FXSyaIwtcuB6uvOmMMSD15PfLttCo5hgvbcd1hyQIMhSleSETkVqp2dO6rU9D6m714wib7NIAvKM_PMDqCQ79W8JewAWKeqaEByLVSBTTTgo5Wikevz5eGcUJuynjIIr4N6DZxRUzo0Liaa1WFdlDmyyOVRa6N_PLpeM5taY6Fvd8P7u1OJogHQ_ONn_f09L2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JoBwKgdwKgCt-1KRnLShK_ijQ9e1Ug3sTEkE2ts_AxqTwBmMir_BiQVqZNobBg6CIVexpQ7mFXY4WJTjWi1RCSTsIMJMhEkk40kN59yhDegAS7TlwTUcCXSrJXhoIW1WCMeT8v4lz0ZmWicBYodpVcAbLLhwfnOwS401818eTBehg8R9nDKUOuOq7cZYs3wv7ZRrUG6E7Hj6NcrSYL_GPz4sMY5pVDFD9uen2kgpTwsQrHcH9AAa-j8-nvbKvhbLcQ19zsMgfcw7SW59HtsvxeIXU8Au_NTk1l_pEkYXJ1AwFUFi-fhDPeAgvIcrZDS95LMhf7rPvL3X8PYgWZ2QtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=s2OqxLCUisCRNVZmsyQ_bjVdbS2gYV765ecd-Eh3w-Eq4C0rBwDbtBKNXlcEHaXcXmGj1bd2fRMhOTEyQRRw5moOQIcR21dfPJD_JZoRmOcDJPI0Fc0JNjyhvXBjX46zmoaibH6RZPqAklEUcdi606TVoT5Rr2mVIncp-4NC0Iuw78llpIeLRrHlOUKi12W2i-FkCPrlJVwAznvv6fHDR7NUT_cp_9_JVWJ4zurDvVtVQ8Rep6s7QmwVd2s0Sl8H2JQyQ1enqDZlz0Z2crxcFZvGr-GfeeTicXaWq0F8sfm5N6QKvHMG7Wxy-nQWFASSxT-7G1QrgRVNQFev7nRV6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=s2OqxLCUisCRNVZmsyQ_bjVdbS2gYV765ecd-Eh3w-Eq4C0rBwDbtBKNXlcEHaXcXmGj1bd2fRMhOTEyQRRw5moOQIcR21dfPJD_JZoRmOcDJPI0Fc0JNjyhvXBjX46zmoaibH6RZPqAklEUcdi606TVoT5Rr2mVIncp-4NC0Iuw78llpIeLRrHlOUKi12W2i-FkCPrlJVwAznvv6fHDR7NUT_cp_9_JVWJ4zurDvVtVQ8Rep6s7QmwVd2s0Sl8H2JQyQ1enqDZlz0Z2crxcFZvGr-GfeeTicXaWq0F8sfm5N6QKvHMG7Wxy-nQWFASSxT-7G1QrgRVNQFev7nRV6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZEzpka9qunum3cqZWbfGYJUif4w0FLpsdABo6PkOS7_H-m7oAz-_Dmc65l-bLZXmdnO382lu0Agqfhqa4ztNCco1Iy6SpOTk8nJ3vTwH373lCr6-ySGmdrFC5h7hYG6-l9tm-RDAG17VamWV4cFTvNBUo_PQ6robhaO-z5UVuTEui_LBRh2leM3XGRyXDUC24jDpPc5kCgxZq3hpOWRid9EkSExB9P-JlmZSFzfif5051m6E3DdxLazLQd1NOV4ISVBZxZHj-yByICbt2U1bX9JnVpxk-5XknA9TXPpFTpt8r4fddy8dxiPLEuDpmSdJGQE2n7u_nntF3FoZQOMqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVp4LSAsxuCOqDyCUbFcgNxGkfwm--hUbe77PjWs8q_xxDdFjQi-PffXRKCm8XDm2dzibwlR-rjm57L_B2_eCnHH9kEGf_l-c66DEbB0g_ii3ph9jf7tL3QCGvKOEww9gM6hW2s0nojKjdmh47bps3OYFmq99mz1lX-3CaRx88xlYZP_wClqRN2WCP1Q-l4UCJGxU71-cpTnsehAVsvEXY4B-hXkQwAN3wC8wzakEvXK-9M3QIKEhw3laJlke7LIiRDyi5UX6Zd85mK11u7xphVe0ciX8zigggDLBTfKrJ0J_hL-UUFcjxI-FIHDe5Gq02kaykAhXtUEZqJU3WjLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iniCr-VnCc4WnwLozJlxNUvqoXocTG6EXYf7L69v7NW2wxTuvtFhsvjBrcX26d1RJ3AhRoPQPSlI0KT1x_VXl0y_pubV788e-oq4FBgTY-p5csRyhXGOGqe-h18eSymDiOQ2cduDE2bVOtLFt7otPpGvDVHU-Bjr_rQdbeVwIn-Zho4fYbFDPpqXnojEa8NlBhZ2_N9YVFG9fV7b9Nafe7Ist09FxWB-BDCksuN86VUQfTy-ArBbe473ESGTx0qw8Ol6GW_xme7WfhtIBAoxHVpK8oxO0k125EYt6KyxlglxynhgPD2OrPRoEWN6R5_YK37D3YUWA8AWeb3E-ZSTpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWqxA8E0LEeiK1TOdaOdux4gxIMQ00rIpGTsKX7Ub_k-D2GelGbv8vQFCtDRLRh8La7TGvOVUtbZbSVx8Hs3rIA1dHi8oJ3MF3n4bPYX-GozVUh-Os8zW-mRatvKJAt7IaqU31Yu9bVv6AwMqeuN_zLgiIZXfUFJIkSU6qZ5MHY5q03G6PvGCAxf1E8j_epeEvDzUtgW3ESrH9LHD4In2ido4nT2TneSmyjQnLdjKV3DNEZUM4-u9oQE42zABucYi85Pdkmbi-CG_GlQACZ7XCEahVReTkcN0527ngRvSXJSdi6u3IMcfW73YGGznZR-E1iuTeFZmYu4CEvhL_ywWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=iS-HTTqf3DWbmXgrCtuQULqkhU7Q1CsgJIgWUsxiXCckhcxSywWombnUAYM1TJ00TF0oUhket1Xbf9tYe7Vh0xGn93Zf25G5yx9PYSmNK3qiyB0yueWE1KIW6Kb8E70VEmpVRU9sWE2sA4HvEAxGnhYLtUQ5X0rgpGj0Mu72ProdK_sk1QjZ0HAN4mVh-k4h1PLusaVaD2jMaUXR_NYwOFgm0-ILLRMhKz12ndmDcppwm6HYrVdgbZf__BakbPZtJek8YUaH1X3Pq4AtooLR2gmXlBodI6Rl1QPw4zHxsalMNyAb69eLdEDYZC91y2I-uURpVSOCs1W0A2uU3ghE5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=iS-HTTqf3DWbmXgrCtuQULqkhU7Q1CsgJIgWUsxiXCckhcxSywWombnUAYM1TJ00TF0oUhket1Xbf9tYe7Vh0xGn93Zf25G5yx9PYSmNK3qiyB0yueWE1KIW6Kb8E70VEmpVRU9sWE2sA4HvEAxGnhYLtUQ5X0rgpGj0Mu72ProdK_sk1QjZ0HAN4mVh-k4h1PLusaVaD2jMaUXR_NYwOFgm0-ILLRMhKz12ndmDcppwm6HYrVdgbZf__BakbPZtJek8YUaH1X3Pq4AtooLR2gmXlBodI6Rl1QPw4zHxsalMNyAb69eLdEDYZC91y2I-uURpVSOCs1W0A2uU3ghE5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7WtCcNV90OAPc6FXYEa1viVUFbcsmg7VatJscgz4-9hUwOwxShqY3FhRqn_kv6zjptzUwE6CbY9pjVXgtJF_mzj6iqohbtKWxwsMKygqxDUP4r8U9j3vLSuDtpx1CV5pNcg_jCOmKL-fTv7nhxp7Zffyjda0219hy2oy2oQGhDip5-sFjDrA-JWZwreiPs14RrCfNeYUL_Uwr30UUj4aKxAZPG5MHDnIkDEM9cRLQFrRmLY8rfwZNWihBev2PuCtxG9OKYwGD0diJ3HfDQFCxSFjEFqH-svkf4khqgkN1I0s5IIwMRhnvphZsqsm9UXjd_YlcKkmuC8aiN5aOwOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arVIqMhPHnHQpgKw3as8IdVWXGJxe6NThh8LM_ZYAI0XV87PlohZCFt9JSpQxayi8U4dHKUPoPJS9J_wn6xxCOZF-aK-PaD5vn209oIAQH5lq9ZpvZSk1wBvgXzBTsD2lH--UKDNFAFwsQFzHjRSpaegI05E32BTtb2jl6GV3XU3ZmhS4argxUe3ea8vuuJSMq1s-Na0HKTcbb-f5UrLRPs6iwCkqlyG1WvYDOZ-l9trMdAtuYQGzj0_uoSfl-5mbSmziM14YeP7oZ4UwEiVAmeJLlmCZb_Ids2OKetPWCPLaYGztBsZDeQEW3EV4aqbXp_zpHgWd7tBgVBP_zvXvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOijeT0mrbPWrIzgZ9sodgMBs_64QtQKLHiy4Sk60eD5Pvy8I6Qfe6PW-SGOrG8rn1aHYoQVdsddg30DDMNkBZtuOyoI2wl2nNJ-1Pxm5Q1h2NVYcVAnur75A2Bk9Bh08irF2ehmn7JQvnodcEF76nmV00c4HJNOEMokdA9rwHOBdzRHlnLKRa8Xf5ss1bFcD81bMHYnxmoJdeWxsXnQpd5cNs6ulX1MFkust6dSWL7qnFK98X9faMANX6cd-aHxr2ZIcABS2nAKsB2S_DxsMx9X30gA7OVtYj6E0qMBfXBmevGvFjOMT1dY1pt-pmQTcdOhX8NL8hiTtntkNJhHbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=c07c88ZWfFW7RNa6A_AYF5N_q-cJj3_hBHv05HyPuGTOe7MJ3kw73ZmI72Ucic-yS3Q9IzhsrSYZtRhW0_pb2IYao0Wk3jOrVCWq2RqBxyo4nXOZWFsOz6uTU56cc-N1rBXRC69ACA6Lyrw3xeAcjz-aQrkwfM02FwtJWWDAEnXNTuqdya3uNz7TP-in4t7VBUHNaV7g0rTjWvFi-a1NJN6u0BRDT8pRRfF1bfel8v3TjVBo9SeSZOsWwPMHTwZDCAbDihuT__4aWGJg2gXmo2XBTLs7hiT8JKLapvZqcAcyZ3PJqyK4w3qmHV7KmdBr0I9HAUJzltwi-Rx5Ac3mbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=c07c88ZWfFW7RNa6A_AYF5N_q-cJj3_hBHv05HyPuGTOe7MJ3kw73ZmI72Ucic-yS3Q9IzhsrSYZtRhW0_pb2IYao0Wk3jOrVCWq2RqBxyo4nXOZWFsOz6uTU56cc-N1rBXRC69ACA6Lyrw3xeAcjz-aQrkwfM02FwtJWWDAEnXNTuqdya3uNz7TP-in4t7VBUHNaV7g0rTjWvFi-a1NJN6u0BRDT8pRRfF1bfel8v3TjVBo9SeSZOsWwPMHTwZDCAbDihuT__4aWGJg2gXmo2XBTLs7hiT8JKLapvZqcAcyZ3PJqyK4w3qmHV7KmdBr0I9HAUJzltwi-Rx5Ac3mbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=eo_hWv4eRNU8aY5h7rAR89T5R577MpFNUIZsiYWKzTt3_wO5afE2ncSqp_NstpHZ7-5ZUqp7XMjTKxcE7oMZFOc1E5KG1irpw3zrkhI5ulRApaAAAaqHBaxgW2-em0Akepywbb4bMhBiOUAtnvQJobJRRymzcCwMYk_7NQm4WGfbiE-kabthDr5dLogUyciPzYk5ScbS39FU-4kQbyRkBAq9d43ZIbQecX6E0ZlcwTHIDc6jR4l_pkBBo22dtBy44rNZ8LXJe7Nwux79FXhk9zdI_ZN8txB6AUCWsSBiGsDTfloWnJh3muzY0Y9UJHaddkhiVn-_NekP8s3FuzXakg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=eo_hWv4eRNU8aY5h7rAR89T5R577MpFNUIZsiYWKzTt3_wO5afE2ncSqp_NstpHZ7-5ZUqp7XMjTKxcE7oMZFOc1E5KG1irpw3zrkhI5ulRApaAAAaqHBaxgW2-em0Akepywbb4bMhBiOUAtnvQJobJRRymzcCwMYk_7NQm4WGfbiE-kabthDr5dLogUyciPzYk5ScbS39FU-4kQbyRkBAq9d43ZIbQecX6E0ZlcwTHIDc6jR4l_pkBBo22dtBy44rNZ8LXJe7Nwux79FXhk9zdI_ZN8txB6AUCWsSBiGsDTfloWnJh3muzY0Y9UJHaddkhiVn-_NekP8s3FuzXakg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc7scNaL_CBFsvncK6NKTIHtldXxnrNpnP1aC44xgsfoKsZDHfcyApcAgRZ1_u4-0lxtzba9hvGa2evVW2OdbXZb9yxEyqUQEDj_bB6kFnwIeM5TKJ8zhvmNOc-lq3fikRSAu_-QhEiyV2XVpY6gsm5Fjeb9MOnEWfxGOZR8kz492GIVz_UhbSVB5Ry3vn9-KZqGb3Ob_5jUsYLY7SnQuMq7wyGsamGfLIWL9hAWzbmI-IZSqh3jAk964BauTxcITtPqpx3TcgYqAjqXyGQ23ixAU5ZTGAMBKq22F9WSg5rwpGEZdxeh2CBEPcPMwJ9coEgjhckKom9QL9sJEJKu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol-CeDnYiTesCNMyxEQDNfF5lJHCM61XGiSOdoDGxVCj0klthvl4u8bZJ0jyLiAPpzN7IBOP92UbYsjA9UoSwwRY-F1f8UaDgkUdMB3aWQYNBPqyxwC9gz-X7e0UETlTdHcpORk28egq-6p26nPoCAMaQbNK-73q6Q-9bhukACxDNsIGoB_ohIBU2xH-XxD5iOqOhC1pOvlLyXIWV7LQPcmhcccJ1FzzzZcGVxts4wFG2PJ9cL-_WUpjjbOXNqsQVpQAOui-8mjJENoYsSiCC_IW42EKEGuHR4yUcIRA7tKmcteynSmdLomH_x8Zj3RbjeW5HxcaC1XEEHZ-goALbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oe2yJY3J_xDzEWImG0XpXIPTga-5lIm4Cqr3WRl_56SlbC6_ehBEzTEk79_I6s_Sn-mfokOJQHiHsf4fKE8ezcsFY81iOztySJUaUWKRcNRxDHC3tmc3WO2ZpRl-HDvUAbbC4BhG19EBh5s5bunoKTkiDFZFXjDPuU3p5sXeiwWO4f7MM1xXrVsNzBnDlfc0KS9sGr6JuaCdN3j8kc0mUsjolhBXBFHnBMWAAj_QjRAR-ZqIhMJLS2tyqbuQh4R3OYmgoTka8Pr3pMKaFExKmDvheitUOmt5LK-qUcMVW4KGp8iKpDCWUUQPnojAVgG_IL4zq3iRpzS5qyCcK3QlEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fBTGE9kC36DPEGQbCSPQRLriyTsaAFOxMgHleklEs5xteYX9bJhwuSv6IZ9Aj8ZK3bX1Us4C-Y93bSvmhm4ykOd-DKFjrwSxxeeHvsNbR9fNGTceVw2Ez-AKSq4QXD-jqL6T5t3WI9WTxQ52OJBw4jPYwa9pTX5e8jJbIVRskcSEAFrUhTXfTdhhhoCQzPivoHF0cIkDX4cZs7z4sDtuKKXMSHJ7v7yzPW6R42Hz4F--caVeK7z0QdX9HRQs5yhUm-G9O5ov2v6gaqV7J9RH1-t4qM0JDM26j-2DWdpUC1mIseZjrG2U_DDCiKCG5pdPIiodzp4_ACa3SPSDciflJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMJtUSXkfr9XxwyP7r_gMlDSrP1LajZeu9TXw2irAtHOmmzAv77D5OJb1EtveJN5xga1K96Z3YESdfAjjkcPxeW_xnMHl3O9or164Z64kyuOIJzTK3uHzpxVv7SFM8c1sPqQf8K9OrlLtRNi1ihAN4NaS2sdWtMjhte32n3vJ1_RKl_KDrF887dpvIr1yQGsIOpcOwa6A03niDHrrGbGqSSbLhSLvY3eZxzjJgobe9OnqZ8CL0eGbnSlWhYTXFaflqVq26t6qzLlM_ofSlQILildS0dr2J4u28XsYXaTyUkUJTIAgDvpjRGrXHB-NdGJzjFrANdwytk-tO1YJvzXhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SomjC_LpfabZewaoWJ1bv5ArVh-8nbQ3M2C63xpbRR8fChn-QZEFEwc9Z9_jdpaxRNEQF807byprTf4QJnwYDsPEWOwrdAD7ZEHFrDTpg_O_RleLfyGTIsaAB_0qqDvwEZXHS-JambV1PBgODWKXiefIgF8ySyJO9jbBypRYOTl-mwHhqk_N7BI74Pb9DS5mJajgSUVTX6VUalVx7JgOJxZXtCDflNZBurxBSlFe9ptjAV1O7errD_R6u5oGz_hFzLeTixPplxIfSRYq3BHopw37nehkrWVwJGvmsLM_OtTHqxmrBIC76mcrtuKRhuAAr8CpvXc-o8QeuujS1PRbxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvKuJ1q-qETMrBt2CstUu1j5nbkj2U-lpELMjKIuavY4wz7uAVEUzW4r_ZcqIFXTIHvZ2ekalYxs7XyJdEqNEGK-4qjgpRxS4zr2rtCj1bTbZOM8adTUjphGlJxRBoMA4Z-Xe3N41X3DeYNGmlbHv2GKEv-Gt_RwUZDps0gaOfs2UrJtKk8vXWxNUqsg2LX-TX--IRyfV1kGfyAGaaQ7kGBpRbuoOQQwSF1sBY2O6KnSpDFnn6mB7UWne97_4eWa9Hhyyi3oaMIiAURgFQfoQvrNKZj7caEidLvv3t0f2SN-YAzVs42qj9jTvWuZZUTGrXbJ0pySR-HNwDtUobK2Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swnPUSyQAUJJIN_QwKErJZ3VzxYu4H1IsFoyzXkWiB5hCRb8JNq4gFrATqKroA7a8jAIfUB6XS2r5-sIc_sv7P6VxfAeGPU8Z8gxjLAo2yZZDLnkN1C-3wer-B9LJfKnUFV5U2aChkTJeoj6Vu_qZnfyG_rJYJWXVBC_PckSfLpsHMCle47QTk8qnNmn8wiUYi30aE-X_YJnOkaeDMdZOJA2Vo28fJN6FgCSiJDWWozvr0624aVbxT9kgGhO-ufDNgZRpLDgPIT8G3SLWyK58Q9Thp69OIaBfQhwOA0lzo-seUeHcV3zz-LnkVbaaqbvUzupXi-t2R86vXSr4LGCgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID6FVTinqqZCAUe2rPk1yMLtRWPjytMT6QdfvInNtmwU3-yLllNsuK1GWTsHAMrAgkpCo2VbW1sIk9jJtxAnjCXFfasTzCj4VoaBgJMmEdULJTMiJY8iOFh6YMdon9XgSk-Qd1mTMp_FENeI7BgQc9P7HxGJtYCDZidshdh9YlQc7mi1Sqs1WJZ6m3nDu2VsxDx6_zC6xhVW1B_7cbDbY0pyPFKx7UhSnuaxDbvfCBjowqkFUc3SXXkGs8lkCMwyNG-dubAy2vZD0PFchGrREEUk11O1ojiAG9RKJwDpJhJ9KTJKYiydP-HI5FrUOoUZwBFnZ0Dphgou565I52m9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uimxxDI-wEMoAxoxy6-ZWPkj0IIRZuMGsNUbQveZ0njW8RbVR7khbR2Zie4YckneQI_IrwF-OWrS7nXNO8p-lpswxMs5iT-J96LdKrvkJU0KPlbXI-nIF_W5KfOsP7PhWsgDFRqt8YHExQI6mHg1k8v7UpN468214M_rG-1UJ4Ptp3M24Y05a-pNuMO5GBi1cFkmVGMDN8NMXWH9YGfDMLXMxsEFI2nuNFgxJ00HK-GERLMYKzMcixGrEcgVYoKhTfFPXkom1nIkslJrYd-pvSWBYdrf44E8J8njiZI3J0dNEY4tHbJwp8uA_unD2HTYZNNMcJyLDzpsGlSmcY6y7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOm8rxYYSCE8eF-Sn7-INxmQ3bHdnR0d4Bgblth5q-QCYHx-PNmTFPmG5uVFcxcdn9DNX31pJcjBRTOvnFBOB2s9Yet5VeDeuiv2NKnFS-ub8ORUIcJ7G5ZY-uRis2NVnwqilSw-29tGeL7YAoLjViw3-rCn0K2PniCA_MNw_Eh5GHYnVun2vXV5jnGPZhc2_izg_a_f42VuMLfQCkwJOlJN2gYXncoIjOz9dCHMHB3zSYH7KceeAqPe4bIai7rKw95m7vJ6mNfhXseS0AOm19YRvudQ9B4tbayZS8A9cAdFEiLrBJkFDIrburf7TsM4HNtvJtUt60K1pIAkWtuoMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_dwRQ2qmIoXG3iILjKiHy19IlHHVafzSIk8e6KQ7V2p2S7r59qYxrvnRBkc6KaIXrsrZlEpqfy6-LGpkVOmpZFNv12mLcmbJ3YdI0PSQYV71fOBiFMnyZGP2rDu8pbIEquiXnyi9GWbVwGlkTs51haBH8KIYVapblqGBVXOz89VFplsxjNEcovruKSvmW_6LXthvZx0RDvlKlhuHqM58tV1lNr_75ba9jAsYl01wCvjNuEtlu2A_Bn7bhx9-HHc_VwnlVOxdxr7WhLkzWtNo_fkoiXejWgPhKOdEH2Z6C6yM10Xk0XWgSu6KmUo3QSL2iJ2mlWVNA_C7WvdyUAzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i57p8HWhRz9Bbch8UU8GGTuHaKZpu7UGVdezBkq0vkDG-Z2-uqvazm7axl3MpCTwbbW2bFv6zRuNfT-x7b89osJ6rxqUTYGgzx0dTFGVFOebeHWYw3gwsL4E3Vx1_nN3C4XhaaYdXawaiR55TI84GleZBBBSlnDUDofhKOh8egm9gy1UT0GWs89e9KTY1ND0ZVt1N_4g5MLxxIr4hES7hvwGQGko6P6irOBNpJYXvvYmiMDyvsTBlz8JKUgkiGYHp4HPERs8jOH4Qrr8o84amXK2C5WwvczYRjZRjqHg3K4TFk-bUbNerSwXVkkTyfwGlOvnbvjsVi5I3iX2V0hsNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_PzDn6p1RN6CybGvQJiPOmhN_hvz_MLRruavkinElSX2_vmoN-YTKQmSXoEZNB9dEakd9mb8Ljn8ot9usfnoRVyVXHCERaQcXmESV-ZNsJmB-fDSE1n8WeIRLJnhOYbpOQbNpbAtxWBKfArvsd76ZiycyeOOd7Q7TgpJsjMIUz7xX-Bw7-uCy9SOA8X_HkFn-U0nZ_uguJsUY_tqK0_NKLdG6_9HCoP1zM7tXF1aRf4yEBCGXrSoXKLH7u5beJDqMfRTceodbSVQMX9BioAM2LUDPEAuJ-kyUXUQJMaaIq2753Kv4e7hEzNMSreeWxKb274CBOw-xvYzYl_9JebjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV6uZ8khDPXJFRvuzWjT-vmrww8vgPdMeAwl11CB9UEDRkYej7KI1wwIUBG6dl3F8lWEFY_66P4j72vQb2RgaBx1-Jo8Olf-ZlC4HEgU0hpY18XTPF154s2Q50rhA9D0MlX8QHNwkGAmKkXCc47dcxCqWFAc6B_tyWz3MzkbONCfHsyEwqdGd3i0YW-gfAAfS8kXKj2_-llefH_rucMpcJZcZGnZEuFAnh6NVi5YE1h3fDhCWG7SGN97302DEDiNyk-qBnRx8kjeFIfADXeUHyYxVUcIi2zWnB_xia0fo12mT6vdjM57ChH39kw-o7cRLTyZL6GDG5bYp-TEECjOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=gT0y8WUc73hX5ROLkbaTgO2bMjF-jXmjCzIS-rcSs3zBAFKbOJlXwWuZw3W8Z2ZqRDvP6SZickkdRrtNrRRPD_DF9KSJulWG_w1_g6BEwJW0nM3K_wWfdh1CuOVa53KMoPU-wrUIXH9sR0F9mu6BrU8WXLUyIzJ_h1pFYj8ixb9PhZ7FBgcQXxiv7Tvh85A6LhbUZlyJiOwaw1_PLeCHse34FTtMOjxxAxY3JKpJkjdet-CaOP6RIeWCEdaqt3cADqWwVi0w1VFLxPOcaExBwFiV1_-krnQ6_hFj6SY1AW91VW18oG4r3KlWT7zpD1FXEa99wIfRgDzAcFjDNGdZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=gT0y8WUc73hX5ROLkbaTgO2bMjF-jXmjCzIS-rcSs3zBAFKbOJlXwWuZw3W8Z2ZqRDvP6SZickkdRrtNrRRPD_DF9KSJulWG_w1_g6BEwJW0nM3K_wWfdh1CuOVa53KMoPU-wrUIXH9sR0F9mu6BrU8WXLUyIzJ_h1pFYj8ixb9PhZ7FBgcQXxiv7Tvh85A6LhbUZlyJiOwaw1_PLeCHse34FTtMOjxxAxY3JKpJkjdet-CaOP6RIeWCEdaqt3cADqWwVi0w1VFLxPOcaExBwFiV1_-krnQ6_hFj6SY1AW91VW18oG4r3KlWT7zpD1FXEa99wIfRgDzAcFjDNGdZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBUi-VNlApT9DoICfFky-ByayaIt6asBGsTPwkeU3a4oUWKEmo-3u4vapQC7AsdlpxmcFMhw0PI0CoaW8uXvxF05VlwwjZDtHDph63nPxdOQOEN68tzMWSARC5Xm3ji-DbsUpaLaTzg0EKQCshe-TAqjb0CLDbc592v05gCSg318W6EbF1l4TizCzLruaToFjj1rL2lbCPLXvHTIx78ZMi2nsIoIs_oLQJ3ET28ocggxR-5khCmdlsYOsUhZ4867gUx_-sNXcEfn4A3crsdWwTmAb0X9X8eOBRRURJx02x7rOueIQbqWfRLh3_IMxrvC-BMewghN4Hr3N2GqithJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=ATCzVoZ0u5QU8kJsQZs7WWBCbneK5_FhUo4qZNjiZFzhN5-2LIlA9k9IjTTxHKoM7_GLBbDen3VeZHgJ6QAFMSwi6r-eDlpxTnhpvH3sol0hiqKe5FjcEQ6TDX2FrFz-1uFKknL8mfL_19dhmeRTWNM4LlBt7tvdjbMjsQof6wJZdLkLHRX2NcvPF54sG2efh1TGQI1tcMGSY7DQnYkJzUGkM1rWzudaE2bUEK-aJrd4CwAwXdYXsi0smmvTJkzaANCBAfpuNdgd6aMye_8WRYDUElcS_B5IX4cFy6C78cpArKm0in-PHgw1rqx8EjVqQpjJ2MesvkT4UJQR5UeSmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=ATCzVoZ0u5QU8kJsQZs7WWBCbneK5_FhUo4qZNjiZFzhN5-2LIlA9k9IjTTxHKoM7_GLBbDen3VeZHgJ6QAFMSwi6r-eDlpxTnhpvH3sol0hiqKe5FjcEQ6TDX2FrFz-1uFKknL8mfL_19dhmeRTWNM4LlBt7tvdjbMjsQof6wJZdLkLHRX2NcvPF54sG2efh1TGQI1tcMGSY7DQnYkJzUGkM1rWzudaE2bUEK-aJrd4CwAwXdYXsi0smmvTJkzaANCBAfpuNdgd6aMye_8WRYDUElcS_B5IX4cFy6C78cpArKm0in-PHgw1rqx8EjVqQpjJ2MesvkT4UJQR5UeSmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=pbVGi2Rtt93ZQ2xzgh1d5OHmnN5qd8oN1fA3HF1eFQ0ZAQuRNpuVU_Taeby3adFa9_HvwOfl9yFuFLmmuVSaBuzI465k9alwUkBFh4WPUFPeXwmbfbChzgS_851n-6_7Ykdzk_XteF7UqfuyUs_IuSljeC6-G1nfeHt3s1SmFp2uj5KcvHNnmSFgptKk-BDTir9C_mGwExIoz9Y-kSxTMH-1T3-iPCYk0g3tOaOcWFHf3jFg0mJmQPT4gk1CV_rQJKyI9TVYlyzn43k9nwN-gow5azYNdjDo-7FD391m00XpveD21hbTk2jZ-urIBuE4z1Wqld3c7beKQKRKSKu80g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=pbVGi2Rtt93ZQ2xzgh1d5OHmnN5qd8oN1fA3HF1eFQ0ZAQuRNpuVU_Taeby3adFa9_HvwOfl9yFuFLmmuVSaBuzI465k9alwUkBFh4WPUFPeXwmbfbChzgS_851n-6_7Ykdzk_XteF7UqfuyUs_IuSljeC6-G1nfeHt3s1SmFp2uj5KcvHNnmSFgptKk-BDTir9C_mGwExIoz9Y-kSxTMH-1T3-iPCYk0g3tOaOcWFHf3jFg0mJmQPT4gk1CV_rQJKyI9TVYlyzn43k9nwN-gow5azYNdjDo-7FD391m00XpveD21hbTk2jZ-urIBuE4z1Wqld3c7beKQKRKSKu80g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFelk_gaMgz2rSHIdskaAE29E43rWfSXBeqN9BJVu-xDDKFf2De8ozuuE2bWqu8f4GiI481wBjCT96VmddDi53SlySq5bK5wGS0f6p2PNBsN0HghqzgFYQshPzns3kZXmTIFGPWIo8LTCbN0quUs6wQ5wBx80YVMkAhQ3DiUqGG5pK7z35dclaPOhd4a-TfEACR1rbvxvd7jzZkHHbuoS6sZp8m2C5tSZPg1oEIzn2Dp3S9MbAxB2eiD1csVBaJ6rxnn4MAp8DjdRgrouU3-e1EX40ZoQaxdi3r9w_3pNGrMAj48hh75sheQLQGCt5TNm_7F1HzvdYCYbqdrzgTp5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=m6K9wVPb1hjN5-A7T7GMgQGPOUivrcKKtuZqRGuAe8pFMf8MTUFKkobjyGbBXPUVdO3NZbulh8ZpNnFudK2Qz1-suGfpT341Af3qov2beCMOT-qccfEuzt1PCKasN_m3xQESg8Iwq64R77Q5UGGbXU0yg6MFbldHjBJGfXdfjK_pASYDy0f2TjXYF-mhK8k_N9RwggM-Ghn5AAwXL-sJhBiS3dmf9_3dl0eiqJ56ujebKMNg2CO_2CUMhm3AhbIVSYHnB0qjk06Vp0_OPfpvnjYrYGGAxNDoqyc_vgBFT-UqlLrChONBVJlaPZtEhx9vRjwtVhBJ1rvP-K3vicjKUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=m6K9wVPb1hjN5-A7T7GMgQGPOUivrcKKtuZqRGuAe8pFMf8MTUFKkobjyGbBXPUVdO3NZbulh8ZpNnFudK2Qz1-suGfpT341Af3qov2beCMOT-qccfEuzt1PCKasN_m3xQESg8Iwq64R77Q5UGGbXU0yg6MFbldHjBJGfXdfjK_pASYDy0f2TjXYF-mhK8k_N9RwggM-Ghn5AAwXL-sJhBiS3dmf9_3dl0eiqJ56ujebKMNg2CO_2CUMhm3AhbIVSYHnB0qjk06Vp0_OPfpvnjYrYGGAxNDoqyc_vgBFT-UqlLrChONBVJlaPZtEhx9vRjwtVhBJ1rvP-K3vicjKUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9P3iYggYf3SCQZqixra2OOIFGlirNg8GSFANJyB_iQF4Li_71mZd_sCFL7TWdgEhWmPbGUvLJw0gwxaRLNqGVgYwMT2NU3Y2mbvh-1ZRzhwHMX38U-kj4CIp0cfn0LoWGcjzdm2E9BPBJLYpTwfmtklJGZeFkj3zq5usnOZfYkBabxEPhm-TYFrO3UTO9Zy1VMq853Y7uqGltYuUG0mZOakb4SUvF83X4K6RQ4Gg2R_7ygIbeb2f-_LUzvCaUvo4iP8AHGcs2n51kcU5sdrR9hF4T6KTvW8QIJxrml6O0lziHeV41yuCM3CJoAl6dk0FhifeenF-Gi2CQ05UecXAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdaJYhA9GcqQUYCiPXwtbWG_WEPphOjyzbW4i3FU47tRJtR9EpCov4Ti2uBRiL2L8dmB0XMUZbRKo6IvQ1MiJfUe0p7cHoOwCt5E3y0BkGxFuASTAEoXQI7McUh1BwkouKh2fGluwGQuEf8AGqWO0YD1O4F78EiEuhGqUNRqSl3gxcjBkih4SWayOmNAF6-UYfDA0hZ9Wwk5ashIkF_iP49xF5NsfnADB9lPmZgUSlVKPMRPYHxmB6MJxe3K7zcCxujnZ3YSD1fK27pswTKDW-pHFKBqErbbZgLDXhsaid63k_drGqF4rh1a7n1IUvmr2fYblKNlVS6D92b3MVMFcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oE-JOvlUd01cgzb7yYqKp-mvRKnlKHkYRAYmPznHQvILBMTiDQzYzkc6OxVSfINYrNH5LxJFRQbV4iwqtzw_bmagmx9qx6b55gtmO7CZbuBAMOf5CnjxDPrAMd9Yv32k6H-ugr_vIq1ahBfZseDda2PZn3R5lW_2Q-ZwL0pkzIkodEZ_AP8Zgoe9rRjTIqmjyerf9WzwJRXHNfvlJOvDu0IuAX34_N3nHYJyHfkxx1eA1EcwkljLf5P99_UXaeI8Lw1qT8VXIlDR0WQ7X7zASKR2Y_b5Iw2E-N_DeX_df199stHZdY2C3-aZXP7AwvMqPhdAiZWPZpnYWLwF02_DZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXiu45NcBVjsJpeUDsTD-AVjm9Vzjx2oCs1F3o4YsH3I2iz2uh4o30gN2A0Y8VvndsZJC-2VVSwoWnbd5SYB_qlqhL2yUlDJE9WQgEf8FW2DU6VbuKCpoSZFjwGone7ERDGji-Wzg9Rz8GVY5Wgq2BHR9FzIN4X1eQbgZKVFiscXQxRQ2j267oK7xMtYOHFfUB1U6nsxoLoz-Dx401Ppd5FmtCm7akHM9_DBcUWIKk4_Uh9ducpU5ycjFEtGJHFq2g4HIrGdyFgCy_aZTP12oz3ninWuiUXL9eA-fh0gd4KjUicVTrxFwhIr5qgFj8V1t1IpUcbZgp_A6-wIMF04Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=ENQlM0XK8bqExuXr5wv7vS6skBttBQTNv0AdaHxEOecRln8c_P_18C5LbEE6ebzSRgKvTw4qg7osa0I_OTa7iGxH6GlhH31mNUT2R0frnjODE060Bkw2ZtR8LaxzokXogpfBVBhtNNTlHtmhCjuvevYB6SsZUN3vZwRGaVXr1v_bUW98R7_iZSE_60RudrFENcQ4CHYdzy8_q3s9w1qexfUpMi7UJwASqwjDWhtQOU14P7v3w9d4_Dl2-gxCsqy_jL_p9OTw7xWukSuSRC3k8W5poy8AKQERreFLZbblZMpvKmZjaeJw0VaKpRA5FigsWLkr1IT2-vsA1wguY0NICQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=ENQlM0XK8bqExuXr5wv7vS6skBttBQTNv0AdaHxEOecRln8c_P_18C5LbEE6ebzSRgKvTw4qg7osa0I_OTa7iGxH6GlhH31mNUT2R0frnjODE060Bkw2ZtR8LaxzokXogpfBVBhtNNTlHtmhCjuvevYB6SsZUN3vZwRGaVXr1v_bUW98R7_iZSE_60RudrFENcQ4CHYdzy8_q3s9w1qexfUpMi7UJwASqwjDWhtQOU14P7v3w9d4_Dl2-gxCsqy_jL_p9OTw7xWukSuSRC3k8W5poy8AKQERreFLZbblZMpvKmZjaeJw0VaKpRA5FigsWLkr1IT2-vsA1wguY0NICQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=h31Nl3ep-WpBITtaHa3x_Uo_NJCZENCNCd3TbgwDrbN-AV6xS-NyAPaqYXWaQtvnjK0bkQF-0AqPeIfHKUbg3IbNzZExrzZBG29DygK0edEsUPdSKfR0ENgBwEX9npXCVZqHFhEcfsmyJwaLHV-J-P-R3abRRcxqOZV_esvPznlHzlT8sp1946GqE2rJCKFITv-PJViVV0QZ3xpsyrOUG2mO4J2RROCmEyerUkAovQZgsS7CJObwm47HN0biJFY1VE2cM9BASd3kbPfaHZok8bGmtjLAePJuUCZxWMKZg0WYbAWwA6xQe5zsY5hp5xg77w0GPOSabR8jG0NQgxOuyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=h31Nl3ep-WpBITtaHa3x_Uo_NJCZENCNCd3TbgwDrbN-AV6xS-NyAPaqYXWaQtvnjK0bkQF-0AqPeIfHKUbg3IbNzZExrzZBG29DygK0edEsUPdSKfR0ENgBwEX9npXCVZqHFhEcfsmyJwaLHV-J-P-R3abRRcxqOZV_esvPznlHzlT8sp1946GqE2rJCKFITv-PJViVV0QZ3xpsyrOUG2mO4J2RROCmEyerUkAovQZgsS7CJObwm47HN0biJFY1VE2cM9BASd3kbPfaHZok8bGmtjLAePJuUCZxWMKZg0WYbAWwA6xQe5zsY5hp5xg77w0GPOSabR8jG0NQgxOuyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=jv_lbTlRDxAntWpG0T0DBz_iW3GleMzCeR3ncKrxm5Br9dUl6QV6x12FJ4xDUjkZHdU39fVYJd2jo4n9naheeCzDYVExJjiYDaKtyvZfr3nCzwwALkjWPPKI26UgAqYPN554WLFq5sqlbI4jql0p6QDrRWhj6lj3PjPO7F2J_uYKYIzByLQzgUX7l9tVXfdJfmvOc8GwwD74EtbSNAzYR2SjB0-EWDpmkhKTzWoRPwzMiXS78i6Cf1ILCXIVB60MarxncBqxjMKo1_TuIGJCvr7S1D1_zenB7WlRcUbjqMuoRCR1Pl0LmzOCA2PHYaKUzmiC16IGv5oVh-rv3RTZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=jv_lbTlRDxAntWpG0T0DBz_iW3GleMzCeR3ncKrxm5Br9dUl6QV6x12FJ4xDUjkZHdU39fVYJd2jo4n9naheeCzDYVExJjiYDaKtyvZfr3nCzwwALkjWPPKI26UgAqYPN554WLFq5sqlbI4jql0p6QDrRWhj6lj3PjPO7F2J_uYKYIzByLQzgUX7l9tVXfdJfmvOc8GwwD74EtbSNAzYR2SjB0-EWDpmkhKTzWoRPwzMiXS78i6Cf1ILCXIVB60MarxncBqxjMKo1_TuIGJCvr7S1D1_zenB7WlRcUbjqMuoRCR1Pl0LmzOCA2PHYaKUzmiC16IGv5oVh-rv3RTZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=M-nF_9LQcv2R1BfzoWiidEipsrZ7yBIJnLsCY4a7Av1-dVJbJRQUG9j0ONCXfLbW_rU-ndIbr9sWYys03j4zdtPpRBwOTlsj4lP_d6cMyVpy20tWtsUsdCRkURg12TRrahVweSbKsSUOFxSDdNxd5ijzqFF-j8sOFY72kcQoArBILLNGcgf2buz-iazN5sPYFaFomR-dXTxWEk8Wn-evEEym1rN6MZvprPRm2OyeenSdYEKoJI5L-P68PJInOzjERnyUFGMkbVyFYVoqs6kpoFRRa7NP1KIEWZjkovv98sTLhtFYQI5ODqf6GYjPyb_7NH71RPcoDp1O7GJJ-KS1TkXKGhE15T-h_nLogOollOf0X4507MogT-pTAyVep8H3tel_jXljio5z3pFRI_dZ_Nuhy4WIDgYRjHGHgxScSMtcbGnVUSLDjECCSy_TD1v-7nMerMKmbnZwiV3ULlEbInA6tjPFmaD7SwDPYzc5aC8KGArSlXf8reKEWgrsqKNaVJLXXjbM8XZHKiM7fiFCmP4kQAMVk9QcKIGTX7tpfvrfwk-qZ7goQkS4l08kijBqmrvksK2w79YhtVgirifK-bSXpObzzQUZf1qWI00UarP1U6Twn4oemAJSsRR-W56eaz1RDJfpbuVnWAF5p3SS47n80HiXhJb2HfWf-HSIGc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=M-nF_9LQcv2R1BfzoWiidEipsrZ7yBIJnLsCY4a7Av1-dVJbJRQUG9j0ONCXfLbW_rU-ndIbr9sWYys03j4zdtPpRBwOTlsj4lP_d6cMyVpy20tWtsUsdCRkURg12TRrahVweSbKsSUOFxSDdNxd5ijzqFF-j8sOFY72kcQoArBILLNGcgf2buz-iazN5sPYFaFomR-dXTxWEk8Wn-evEEym1rN6MZvprPRm2OyeenSdYEKoJI5L-P68PJInOzjERnyUFGMkbVyFYVoqs6kpoFRRa7NP1KIEWZjkovv98sTLhtFYQI5ODqf6GYjPyb_7NH71RPcoDp1O7GJJ-KS1TkXKGhE15T-h_nLogOollOf0X4507MogT-pTAyVep8H3tel_jXljio5z3pFRI_dZ_Nuhy4WIDgYRjHGHgxScSMtcbGnVUSLDjECCSy_TD1v-7nMerMKmbnZwiV3ULlEbInA6tjPFmaD7SwDPYzc5aC8KGArSlXf8reKEWgrsqKNaVJLXXjbM8XZHKiM7fiFCmP4kQAMVk9QcKIGTX7tpfvrfwk-qZ7goQkS4l08kijBqmrvksK2w79YhtVgirifK-bSXpObzzQUZf1qWI00UarP1U6Twn4oemAJSsRR-W56eaz1RDJfpbuVnWAF5p3SS47n80HiXhJb2HfWf-HSIGc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=dzR0QifgJ9cGiW0hKDtUHswlCNV-Dnv-Fk443rkjENzsqvkIYkjWApk3CmxEh4NoIl1rYXU-Lcc18ZJwPFn7aetcI0vb-CoH11VYm1_FpzxmW2OTaNdvly3vVl5QYY8sAkUZDrIaSl3r8LSDZk5JkSjNjOKSvzxskUYjIldBDpo2tPy5Qd-z_tttvu7Zcbi6Ka8QwOcrzatB3JisBvlJpf4qjHRJxlITd5DaeihUi8AU5yipupAhEJUUP4ptoQ1yI3831KCJqLcA9bWQ5s6p8n6hk1mZhx5nzMAUm-CwV2dUObdb-QU9llKweGN21EFB7o2EpU5vnEPv9UpgjgVxrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=dzR0QifgJ9cGiW0hKDtUHswlCNV-Dnv-Fk443rkjENzsqvkIYkjWApk3CmxEh4NoIl1rYXU-Lcc18ZJwPFn7aetcI0vb-CoH11VYm1_FpzxmW2OTaNdvly3vVl5QYY8sAkUZDrIaSl3r8LSDZk5JkSjNjOKSvzxskUYjIldBDpo2tPy5Qd-z_tttvu7Zcbi6Ka8QwOcrzatB3JisBvlJpf4qjHRJxlITd5DaeihUi8AU5yipupAhEJUUP4ptoQ1yI3831KCJqLcA9bWQ5s6p8n6hk1mZhx5nzMAUm-CwV2dUObdb-QU9llKweGN21EFB7o2EpU5vnEPv9UpgjgVxrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=shF7V-1hOoIob4cKmBuZmKFdTwvuPCvCL_1uk7w5OhfI8blx63UWQZTXY2XQfio_TWf25egMRdrTIgijWPid4ACrhJNJjeJrMhJh6AZXBlg5cc93rzmqofO0iMnowSZePdgyu6GY1y3ZTcvqr0SAW5Ek7nSPPBRfBZLD_LltqDGn2C3-WcorIvapPlo6CXb_CqCY55d-PBQcSOJrUklPibMo6zSTmYq59FwOTTTM1e8UqGuT_dIfhyjdrpO2X-j-IwJK2p8ycUnZHc2EuY7KpqK3WpK5Lwfw0jPOtRD_w0_TXLAQpxjLrZjRLPdx2AgJ7w1DxxvlBLhPL-C9piGE6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=shF7V-1hOoIob4cKmBuZmKFdTwvuPCvCL_1uk7w5OhfI8blx63UWQZTXY2XQfio_TWf25egMRdrTIgijWPid4ACrhJNJjeJrMhJh6AZXBlg5cc93rzmqofO0iMnowSZePdgyu6GY1y3ZTcvqr0SAW5Ek7nSPPBRfBZLD_LltqDGn2C3-WcorIvapPlo6CXb_CqCY55d-PBQcSOJrUklPibMo6zSTmYq59FwOTTTM1e8UqGuT_dIfhyjdrpO2X-j-IwJK2p8ycUnZHc2EuY7KpqK3WpK5Lwfw0jPOtRD_w0_TXLAQpxjLrZjRLPdx2AgJ7w1DxxvlBLhPL-C9piGE6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5wB6TPGS242wvxNPgde72JBbvvU9vGo5MuQJlFw84zypm8X9y7NPk9gBz17ndG6G5ttNQ-3isefALzuR0mfmb7U5Y8RZiaYgOcnVxsQzlaO_fPOuZQHTu6DDBWAxlMKKGcD9L2IL5CjXxvkQj-6KqMe7Rg0JniDejXWczwd3nHSUFfUe8GA7uY-VErM9zf_jGk-UhC0Kb2Rg7hlp85Rwa994KYNai5qy_HEiUV1jv-i4ukuBTS6RuUUz8FwSJBqCL8nRXbJMVshHvKMkisVm3oYSpYxZlZLDSiAWxKMPFHlL-63ko05RWZZK4iinkQu_S0A3mSkxYb-1oDnrZ7UdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=l8nZK2PX4eQl9_1FZ_ur-xgPm3XESqxAr25lRe42ev1-KxPiHmfOKQofg32IrRCrSlpgVHBMfO81V-D_Uq6AuEkEhH9Bi2v2j-opb6wv-VcurzduatKdKj9qCiwWgtfsuO9D2m7DC2GSG-hTeFeJgpoWAy_CkNwE_8IDm9vQwMBCrkXU4sSrcZT3-pakY8Wtg5Fl6KmSbm5tIdYAaqMdVswRCFg3AUb7O_BsBfV-sSZo8qlmcZXFLylgsumQZCYZULa3OhovxbkaGDP3mZp_krjdatLCrzLDPa_lmXgemGaOfYrGDXq9IMtdfevaQRJ9X0KDetjM0HIOxPgru06V8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=l8nZK2PX4eQl9_1FZ_ur-xgPm3XESqxAr25lRe42ev1-KxPiHmfOKQofg32IrRCrSlpgVHBMfO81V-D_Uq6AuEkEhH9Bi2v2j-opb6wv-VcurzduatKdKj9qCiwWgtfsuO9D2m7DC2GSG-hTeFeJgpoWAy_CkNwE_8IDm9vQwMBCrkXU4sSrcZT3-pakY8Wtg5Fl6KmSbm5tIdYAaqMdVswRCFg3AUb7O_BsBfV-sSZo8qlmcZXFLylgsumQZCYZULa3OhovxbkaGDP3mZp_krjdatLCrzLDPa_lmXgemGaOfYrGDXq9IMtdfevaQRJ9X0KDetjM0HIOxPgru06V8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftw4qCYAfd9X8YJsStSpD97D0D_z0XMGRO6n3vVIOPPZaO-Y0n1Ge7LUwHNITIyBqcmhfc0RTcGOqVnrWniKfLdn0W9zl-a9oEwe4RFDe1aLQcCW_rGlOCcUX4Q2kdKKsn5e4atJXGA3KrO5dnLJp8JcHddPmnouo9QqlU2b9KVd1SvaY1X0I-K03LJq3XcY2t_cM1JCv8cuLQcUhSd26mk5_5BvJ2drfTzjVN4gs8dRhju5AXs9Tit2Uqd5boUfyZ7hwXyP2lssWrCRc2qfoccz2wEZquqvE9FwY5DiR90AAyAcRtavaVzki5YTW2kUFZZ4kMNOmmd78IOe-CEYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGTkvQZ6EhyYLznqaqqFsTx5IyUGB1zjyNAfQo9SeiDDZk7pHSifRnZe4pY98ghkn1KffmY1gRxV-WGqf8VC81VkDh3yiGkUDZwleofQPJ8dFCC8amlokgpVJtEAECY5N8uQQFfhVoZC4aEeMYUR9heFTM5AfaaEQzW185fD9WYTiFzU2fokChSO86qZmaUPhLwG7JVuY6a7_DmopJvK6Nt0rm_V_a-1ZyyrAFeF2VPWIdbScdVkupbkzZs3ftYoSn79_hPJSyvcKq0W2AWBZG6QV8Eaxf3fETPoh3gOr1zJbudCNb_xTdT3jSE8uGy2q6qe9C3kvlgp1lTFILvv5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=VKAIqiyV2oncQJkRZ0pLFCn5dcx2oiNswx_rCywcO9kRWOBC_p0WTZGbGbRvYa8O3NeYeTjPpPR3cWG6HziMaQZlNn1XhELqT2cPZBAuEPV9_lIQRVYdDeSwCCDEROoNLv-jRFakg_tJzzBmoJe5cCWWRaCFG5qYwzHa8YSmpSkWWkjMMCMYkqgtheKgmNtRbd-NeRsoMl60Eem0jpJ4LToK-pXYT7Lh0VwKLkfa50VXUWRUJVFHXEzYtosOLCOORJWDVMDMhfTD8dFYViMpGOr0y2AZeFRRS7keyaFro2zMI9KQs2Y15xvCPQhDTU_cvwG0J2iYEqW2rzdQobsIEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=VKAIqiyV2oncQJkRZ0pLFCn5dcx2oiNswx_rCywcO9kRWOBC_p0WTZGbGbRvYa8O3NeYeTjPpPR3cWG6HziMaQZlNn1XhELqT2cPZBAuEPV9_lIQRVYdDeSwCCDEROoNLv-jRFakg_tJzzBmoJe5cCWWRaCFG5qYwzHa8YSmpSkWWkjMMCMYkqgtheKgmNtRbd-NeRsoMl60Eem0jpJ4LToK-pXYT7Lh0VwKLkfa50VXUWRUJVFHXEzYtosOLCOORJWDVMDMhfTD8dFYViMpGOr0y2AZeFRRS7keyaFro2zMI9KQs2Y15xvCPQhDTU_cvwG0J2iYEqW2rzdQobsIEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=nG_4YgM76GSBbrfTPyJA3pX4RT2yKV0asmGEgePryycsmXS_Y837xUFmS5F8E0s0radFwPiAQOE8cbXHddM9_P6qTnqsdtgYZnV05IRJ4BiHfiNRTibc7cSPZjU441n1WGNdOjlfE203mZv1Kf4SXoE2sjNxQOeyv221HeKK7LLaWouM6NKetcgDQ8-7Rep7FVuDRWSAXRheud_YUhA9V8G8JD3OQJow5OrZ-ceo2TlmZtEG8YBDsWOFfR0HgsQBYXaNe_EX0coYXtHqOX9cgkfY7yw9bCjWWUav9rT-2wrqcHl3EfK2MSs6kq_I1Se1aRsijJhGHH48sxgdf6De3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=nG_4YgM76GSBbrfTPyJA3pX4RT2yKV0asmGEgePryycsmXS_Y837xUFmS5F8E0s0radFwPiAQOE8cbXHddM9_P6qTnqsdtgYZnV05IRJ4BiHfiNRTibc7cSPZjU441n1WGNdOjlfE203mZv1Kf4SXoE2sjNxQOeyv221HeKK7LLaWouM6NKetcgDQ8-7Rep7FVuDRWSAXRheud_YUhA9V8G8JD3OQJow5OrZ-ceo2TlmZtEG8YBDsWOFfR0HgsQBYXaNe_EX0coYXtHqOX9cgkfY7yw9bCjWWUav9rT-2wrqcHl3EfK2MSs6kq_I1Se1aRsijJhGHH48sxgdf6De3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=ePeoxLLTqTzIqTJpuAuKKKmzolMpmlzw7CVxlg3Ft8_OpVC30ZH7ndRN5Q0mzxlbmqwav7GwMgR2H2nsVnJNmrFG2DM9xOPT4Uk0SyBRxcdKrxDHvQOGDdob3-DufcPcFzgxMEjdxp_kauIb_D3d0P6QSMYxCNseYd1VfSIyOlzSQ33h8M0ThAd-THq2EwO91VVUmU_AIQ7m6CREEKN8m-2JOJCpauO0tNh3rLxn3EtH-N-2PXZS_CxxqJEBbx6S3MGaBYhK654aiH3QdqIHh9nVPm31OTOXUIDd83xfnV1ytI4wEVVMgwnyqrfjWuQ7XPAVD3zxpoh54ZnzWoMpsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=ePeoxLLTqTzIqTJpuAuKKKmzolMpmlzw7CVxlg3Ft8_OpVC30ZH7ndRN5Q0mzxlbmqwav7GwMgR2H2nsVnJNmrFG2DM9xOPT4Uk0SyBRxcdKrxDHvQOGDdob3-DufcPcFzgxMEjdxp_kauIb_D3d0P6QSMYxCNseYd1VfSIyOlzSQ33h8M0ThAd-THq2EwO91VVUmU_AIQ7m6CREEKN8m-2JOJCpauO0tNh3rLxn3EtH-N-2PXZS_CxxqJEBbx6S3MGaBYhK654aiH3QdqIHh9nVPm31OTOXUIDd83xfnV1ytI4wEVVMgwnyqrfjWuQ7XPAVD3zxpoh54ZnzWoMpsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjqE5I9WhIEpJPPBgzPEtr0INg27anKE1H7zfo2XHXkdqrgTIU51f0rNxwTqFiA1So3RsEAE0_6SLn6SifgRF_WjDXuxwwGN5oJiUjoCb73oNJxXHLcOilwP18slz2bzZeEfHXDC-60hMsdMtRUeqDITfUe3sKy-EGinQ-k6uQekNbcD8a7QPta3iSz8ccqCb31pFUdKPZmvkCDTqWMIx3UyHK3vCo35kbSpM2GjZ61f92O_Wc7XtyhecFZ5oCVj5S7FpIvG9cZr3cDAku9HsBcoMssixF2ONibtQ37uuMv-jzSyZHikY-kAZ2BIhoMyUBhLCuIm42RNTHNNOs_3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=XvU0x6jkyKkryvAaYFKT_Hm37o6J0eEXKJQZ7K28_NmBwIm3DJ5BLGj4kSvSqRN43_nc47lAy9V6sVr5mlpbieH5-P0w3xs_QTbOeFzaHQ3CEL_UFYCJZAyosdKIEUofMAClJ1daolshA_3yq6D8mSeud7x0Onqn_5ILjlfEo2BeLMrQjKoMHeYM-1r0p63a5JOQJxp0Wvx22fmKRf3F_p7Y445T4UKSDpxg-F_ED3MnCvLS6f6E5CKX0T-qd_ejFPvr17ZqH0wqdMLUmHQyYLHK8SAS-Pvnzuio4QBSYHKnoheVIlPDBtgL-6orGMD-UhrNe8etvuwG-n25SeFsgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=XvU0x6jkyKkryvAaYFKT_Hm37o6J0eEXKJQZ7K28_NmBwIm3DJ5BLGj4kSvSqRN43_nc47lAy9V6sVr5mlpbieH5-P0w3xs_QTbOeFzaHQ3CEL_UFYCJZAyosdKIEUofMAClJ1daolshA_3yq6D8mSeud7x0Onqn_5ILjlfEo2BeLMrQjKoMHeYM-1r0p63a5JOQJxp0Wvx22fmKRf3F_p7Y445T4UKSDpxg-F_ED3MnCvLS6f6E5CKX0T-qd_ejFPvr17ZqH0wqdMLUmHQyYLHK8SAS-Pvnzuio4QBSYHKnoheVIlPDBtgL-6orGMD-UhrNe8etvuwG-n25SeFsgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=HZBlybMZ0k0POzFNC7KZOUUQuPR2e-_yrj62Lz3unFc1xgNw1Hyzrg5L7vc_vrwZtgjVSnl_2eC_bXVi8WYQ7VyCV5PdjbfG7LvomajHShSommOaMfzEp0aDDcs_afOCX7F54UIe1JN_rbaTig4Ju-1bg1fn8bqZ_HnAH1h6nb9JTXisDtz_QBmWXHigP33qDbrchSLHIaFM-53LaMmmsvtNpMFAWWB3X1Ju26HWZytqAMoojkC9lVLLVw4yPJhxwoAGVGualKRPdlsttVJuLk_P181q0HJptLR81DXb0EGHdcthe4NwQL_-MDCW4UElLBWRJ4BwYSzwYQbSoR74ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=HZBlybMZ0k0POzFNC7KZOUUQuPR2e-_yrj62Lz3unFc1xgNw1Hyzrg5L7vc_vrwZtgjVSnl_2eC_bXVi8WYQ7VyCV5PdjbfG7LvomajHShSommOaMfzEp0aDDcs_afOCX7F54UIe1JN_rbaTig4Ju-1bg1fn8bqZ_HnAH1h6nb9JTXisDtz_QBmWXHigP33qDbrchSLHIaFM-53LaMmmsvtNpMFAWWB3X1Ju26HWZytqAMoojkC9lVLLVw4yPJhxwoAGVGualKRPdlsttVJuLk_P181q0HJptLR81DXb0EGHdcthe4NwQL_-MDCW4UElLBWRJ4BwYSzwYQbSoR74ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=ZgsfBPv_GRwBQjCH4rLJTl5DqEi-DwJv2w291UIQi0xyN2BizDB7hwQRmgniHyqZkP-ZF3T-ubk5KWEiksPRtRjo4nJJqDLCKH2Cy8zBgbfdkJyZohAWDN4VZV8VbkIwSMRb0G8dA9Bhr4Fmd0HTc1KseYpG_hs3h13HMjVf9EunqVe6fklCMi2zSd3PkRY_oX9wQalnH3agAP9RtINH_1CSbPO3f_TxJJutt4_gBFwNJnT-frrTuxhY1yX_bVmm8wBVBzSJO50gh0-FXSCeN0g6Udrc6t-WSzhTTm7gei92s1A3Zi0hrsY06fAK14NBW0OKwtFFK2pL5CJMf2eldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=ZgsfBPv_GRwBQjCH4rLJTl5DqEi-DwJv2w291UIQi0xyN2BizDB7hwQRmgniHyqZkP-ZF3T-ubk5KWEiksPRtRjo4nJJqDLCKH2Cy8zBgbfdkJyZohAWDN4VZV8VbkIwSMRb0G8dA9Bhr4Fmd0HTc1KseYpG_hs3h13HMjVf9EunqVe6fklCMi2zSd3PkRY_oX9wQalnH3agAP9RtINH_1CSbPO3f_TxJJutt4_gBFwNJnT-frrTuxhY1yX_bVmm8wBVBzSJO50gh0-FXSCeN0g6Udrc6t-WSzhTTm7gei92s1A3Zi0hrsY06fAK14NBW0OKwtFFK2pL5CJMf2eldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAdjElYWYJRITY_dJC6aAdo8UFzpX1SOrxeh-SExUTgcaZSLwbfp4BwyXL4OJ5NFwiaBD4WQjAyAtF6zCclVrn7XIN5niL4vFTIncX-vHd-qU3Gv0gnXl7K3Rj29kmQnoTxVDbaENgBEcrmKQ0M32zX5ZWCEfrb-COv1I5rbvY-nMRLuXf-MupPJw4mPwVw4PICn3hCvZMeCL6xW6_oytateBAEsGALAaOL1AVPXcsNLx8uh0E2tfIfIYjBWGvUMY207mLT2R4ZYNhQ7-S4XIjIrVzYz8bL0UEKpIfKBGDy-cBWj3xIqrmX6Fpy27tcbXO5xkVsFeY3Kwg_ALpNkhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=bdWhpRhY-dA9O91hb18QNM_jco6amRWTPTCGrDdQ2vQmXna3ur5a9S7x4jOA26DfCOaf955adLqCMkokVIhziRTGh_UqRrsIPElM7lxJsmse5k1jY0ZVjfGEHeFsrBzafsI8U0lK9pFFx0IzYTqPPMx-3r3_yZqW7uI_1rZZZbKbBJe8-QJWys9pagzy6JPCcyUsRT3Xyoy-9iSMZCr78rv5CQCR3itgXoyzKJgXULYavaOMx4Dn216CnHfYJbspxToB-8_vMPpr5c3s62nPceScgVR1iqoh-RfQsByGiFyF9Gu5DP-BbAqQpDzKcMjDd9nnYxhuhtxsIgEGDhnyiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=bdWhpRhY-dA9O91hb18QNM_jco6amRWTPTCGrDdQ2vQmXna3ur5a9S7x4jOA26DfCOaf955adLqCMkokVIhziRTGh_UqRrsIPElM7lxJsmse5k1jY0ZVjfGEHeFsrBzafsI8U0lK9pFFx0IzYTqPPMx-3r3_yZqW7uI_1rZZZbKbBJe8-QJWys9pagzy6JPCcyUsRT3Xyoy-9iSMZCr78rv5CQCR3itgXoyzKJgXULYavaOMx4Dn216CnHfYJbspxToB-8_vMPpr5c3s62nPceScgVR1iqoh-RfQsByGiFyF9Gu5DP-BbAqQpDzKcMjDd9nnYxhuhtxsIgEGDhnyiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oirk0qbvz4-31VEnhsYaRjMCoTYqybzYdcsQZLbzWePcs7IvZZO2e03O0Hb0K1qFbzAvA4X2EYSPgUOa1JFKsSP1S-wehHmSWtbTrHznXQwJoFq4Qt6IcJUAnJg6vPZgQq50nStbwSdYsUCCNKYK8uXtO4X5yBHRWFv9CmRMoNJ37wuP4Nb86vbCE95jZ8lzkIDMe4zH2pXgrU3DwOpfWPvLI88md-52GYgGOhDyUPRO_difPWgxvK8jnhfVq2GWEMFg888k20dZ4irONVHuhJTtLMOuscYJzz5I__quGtaml0zd6I5TvRYjisS4Tb-eZ6ArapysE6vJHdAM6hc1Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=eGlOjnaErnoNxr9UvdPgp4t87kL63ciEF6rrJj9OicRBcXyzQC6hPimOp9DpwjOZl60mjfhZDL4pKUlkOibFxepkR9Vxwn4UNZAzMB163qPEw5hZlTrqqfNzc8WIQiFW4zn-ba9xwRHmA3r2rRuoCeEIDowyvNubZzZBh_XHOrsp5bK4-BTKv4ehLIT0JyFPGRFTlwCPatl5hLFoi_SCowJ7ab4M4iCQNoyLhZ1V4EuA4sXBNgLqhYehdylpCrdTHf9l4vLMUoI6fC6xEWZFkzrfb0GzyrI_kdV1HnHm6l8bnZzAVVbV9Wsrd0KJo8RcpQuGk5Y6-Ly4jrc2iz_PiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=eGlOjnaErnoNxr9UvdPgp4t87kL63ciEF6rrJj9OicRBcXyzQC6hPimOp9DpwjOZl60mjfhZDL4pKUlkOibFxepkR9Vxwn4UNZAzMB163qPEw5hZlTrqqfNzc8WIQiFW4zn-ba9xwRHmA3r2rRuoCeEIDowyvNubZzZBh_XHOrsp5bK4-BTKv4ehLIT0JyFPGRFTlwCPatl5hLFoi_SCowJ7ab4M4iCQNoyLhZ1V4EuA4sXBNgLqhYehdylpCrdTHf9l4vLMUoI6fC6xEWZFkzrfb0GzyrI_kdV1HnHm6l8bnZzAVVbV9Wsrd0KJo8RcpQuGk5Y6-Ly4jrc2iz_PiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMy2u1lWDsEQRiOfu9k8DiM-o_HmQn1XwHNu8Kz-1vVTC8zCFwqvPPClj5gwSaDkNGNVQa3kr2H0Up00rPj8ihGXFbAK3uqWSnV94ecT4mFCqNZNGghaK5XRQnXSsOh2Gbn2_tP1WNc4plV4VPRbhZ3qH1p86eJmML_SUxTB19nRsWi4IcgNymB-QL5B6wxV4y2ug52WqGY1rNqv85cSOalpI-ivuxMJLktDsyCokIGG2cOwA8b2QJeeOJ2BiCW59xNpw3DIVJONo48FETYTRbSMglBiOxJjh3fFswynBnqz3On2zmA_VHejhFMSGI1RjqiPFVKYdDinUMvfForivw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=gRod4flfNDJSQMhxH_wlOl2T6N5KeeK3fdjLYfXGK8guCZp1AMvqG8OkUefq8E9T3Jq0kEi6gfUE0GO-RsGOSWvxfYSP16yRM4eFTvUQuIQS1Zu3E23NyCBHA0WnPhqsEbw5mTeWpc4M2ahWMqMCXxmVhpKbJyqnsg07crORZpZEYAnJofByqTSPjiFH9AMn-W1KsdbIP8Tlf7z5qEm0MJOifTFJsNaWCKimQMahcqfMtXEiFfMLuo3Apis8i8eytsEyrUj3WnhQiPSj18ew1dUCeXooXw6MmSO_e5V6LUxV6JYYThREpnS23-EgfZ_tMFVp9J727QPlaoaiPvBwdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=gRod4flfNDJSQMhxH_wlOl2T6N5KeeK3fdjLYfXGK8guCZp1AMvqG8OkUefq8E9T3Jq0kEi6gfUE0GO-RsGOSWvxfYSP16yRM4eFTvUQuIQS1Zu3E23NyCBHA0WnPhqsEbw5mTeWpc4M2ahWMqMCXxmVhpKbJyqnsg07crORZpZEYAnJofByqTSPjiFH9AMn-W1KsdbIP8Tlf7z5qEm0MJOifTFJsNaWCKimQMahcqfMtXEiFfMLuo3Apis8i8eytsEyrUj3WnhQiPSj18ew1dUCeXooXw6MmSO_e5V6LUxV6JYYThREpnS23-EgfZ_tMFVp9J727QPlaoaiPvBwdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGqpDILQNlLgp0MdPrAIo1rDSO_TqojUFVN1PvlJ1-2i8lmZblQG-rlsm_3Ri3T0Ek_t7Ka_qEY614WUbJUMvofYhC90vHy6UNBB8CB0zFbbIEvZ1TsVChU4XImHlGSh62DtweSQ3vtrGzmkFnc7Zs1gNE1jwHKG8DWqD1PhWBaBTu6QuOEhaNmzlZNdZjJ4MzdqiLVNroosVWbbUZCZXlINyJ4IVK4ftdsp5tMquCKm2qXfxXq6WtrKC_tNmx7AfWiuGI7e_kbNkMJlXFtJDXJ2u1vBclk0BS1YEghIQVq9KMOCfB1x8QAAEp7Q-PoeB2UIT-NrbCUQeSc41keP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F6wHkMKx7m6GcJet2bKLDRBCpr9ZWu0M0hQz6ayqeH01D-4e6NDHV-gpqEt-cefiSJPa8NXJj5018u8ImWl5kLFSjmjZC8g4ul1OO45LEdlldsuAgdQ1xREIT3OqL4TRX8IxZunvMK1ZpY_qctgLAd7y7CTQDpSTmYZzSonlL6uKDVvSYewFYTPmR8swUiX4MB5SAfBDs9w0cytRHbttP_buvHjeTqz7OYXft5K7kanTuCblsmBIfGcT8NPWKIU5ke6MBbXGvvBLVK-wf7FG1SGA6k4MijQn--RPJMMhoKrTrbF4aRxJfjnrfZ1NUU1f2DEqeDv9I7MwWWgf0WNO_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=fyjUvol-56N5KuvxVXs6XCez2J4av6oAled12A2hDso8ClihcEwcGzqQR_ReVb8Un6uYokC2SG1655l6wlCjYKe7DPSeo3IgfoQLO6-Lzo7lKYq_vpQR_PKQPQ1VooEyXvJyIFXWvK1B2eteZg8oTJMNMCTJRiuGVL4iGF2z7PFw_ftuYERBsEXo2YI-iV0jLksrdpBOKEK45-RSuZx161dHHrbzepaXgejWKTy5Eox2EW7wem8TBv6AE5ZMnwyltc8vO7anagb_vMsr3PTkaa6VgbU9JUMUVWtjZuQ4JDunlz-HUvA62ChA6Jip-JWVjGdOc_d8PtvbzynWfQvmCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=fyjUvol-56N5KuvxVXs6XCez2J4av6oAled12A2hDso8ClihcEwcGzqQR_ReVb8Un6uYokC2SG1655l6wlCjYKe7DPSeo3IgfoQLO6-Lzo7lKYq_vpQR_PKQPQ1VooEyXvJyIFXWvK1B2eteZg8oTJMNMCTJRiuGVL4iGF2z7PFw_ftuYERBsEXo2YI-iV0jLksrdpBOKEK45-RSuZx161dHHrbzepaXgejWKTy5Eox2EW7wem8TBv6AE5ZMnwyltc8vO7anagb_vMsr3PTkaa6VgbU9JUMUVWtjZuQ4JDunlz-HUvA62ChA6Jip-JWVjGdOc_d8PtvbzynWfQvmCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeXjLsNwqeQqDRYqHbfuVEZS_XEh3e1ZwdCe8JAiKPQ3olSk6IajoYvYpIW88t6qL8JznxvNPLg34KzTeIoLNEqVMIooFbuFhT7lPvacLlRBDJTnWBG5YrSX6RvqzAHhJXzoYSNMs5vfZmEz9nK_EZtDORtNpy4qk5jfEuzTKo33dgiSaAQX-oOqSza3--3nhXVixayRU59vZCjG9ANnjPr3gNPRuLv5JaoOMLOIY1afvuH8MrS4-Zy0qr2b9WG5Z6jdfbU7GaTwHLqpahZAulV_ITlyIdeTpcVNfsDEFnxQqInJJTdAeZbieDijcuQNDHDOYWKttW0sTLARS_NUBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK9gXAbqSvl138y0H9-XGNGZP0jy2WxaZYoAichtxreu7V59_8CYHUnxGctBgeydJr4JB-aE_U8LjmXG6WqnRU-AMIW-JKIDxV4gFnhPFUAvJGN4f-c5V2XY0a3jAYAqBcc0AWI8449fFl_mkAqQiClVQFJOuH6lbFq-lOTb2z2UfFf2BCsnefVTr_HXTLHqy8eHHqqdYb4XpEIXYsNgVee8E1enGnh-Xzblzu_f4x-HDfd79CjC47FMeN67vsKYQ0n_VCcyq-2AHTzArZeuPROVtlzcMZ94m2JyyOXANThOAtifc_Ac2_fO2xpuTt7F-fhXdk-7Udw7-lecmjyn9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpM1BMEsZ0gy2izzxQNMINTm4kxJkuMfEwNDe5tnkm2vtB7fAJnnZymrQOjvmJVmEu39vnqi0nCpFjQt5iWSpJxTEaH_pozvaCsqASd7NFgSdsz43a8wF2gUeSoBLZYqiL6M9oXT9-A807Elu5GK2XEolx2tt7jcMd_rFivSnBY5O1UNQyXAm4tLujWUfZiyxbhHTYZUju9t567RXX6FDDr8xkL6KMoEqJarFPHSjTJ67TarDwJZCy6LVCBE0GK1AfSH225AsSr9jPikPQt9P3asz_wZtB-lZDjE0fQd3F2mvV29Y6aDeL2gNqzbSrlanqpgfTRM_3CLqoad2-qrFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpIDzXzDbdVug2XgsGYtI30lx9lxIlaHO8mQsN1TJ2l8nXvHGFeX_9pws0XmW62zUK84rkCEpu_4tiMwTgMzT1NAhh9w60CoUjZfe09CPo1jZfAKrKKufRXMC8HCk1aB0q2rV9alYaF_v5D-5NNNMhbJWX5DHtuq1vymVXr6VztV4Qkz35f9d-FMBRz2Muhd--CFB0FHXSS6scqwRxWeMeCIt-oEmvnesi8Qw8UdplGeMSE8yFr5Nmqix8XQz6FeH3Yc5LD6EKNFMdNTOWjlS-0c2M5FH2xhf1BGS3R18u80K-lDYsCin-JPfccIu2zUXvUhSdrgELq3yt-EHfa4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bah3hfRfI41s2p2AgEhGohGZ4YiWGqzFtDR1YUXqRW08UPLpWhkAPHTyGhONdR3gm35EneedsbA16yh6-OPZ3XvvOuC5HAx3qxTNIWNkhl83g9Duo4gJBOZMkbZLgV38i5ZImcfhDpYcBX3HAUloLEaVPrdc2Ulyl70ydqUIcSMZZjXcBgM6Nn5ly2T_NDz-Z3NReXn2Spw-yFAZUx6wB14utsTCJYJ86sxGhdS5wK6aEG4kYlvBcsRrfZ5Nvi-DHrbk6s96ZhZx8Seryq6Au8XQXwkcmnGLbxrP3W4_-EY0DNqrWzYZ3OY1Efqo5gebGhbKg8k_g_bl-EkTG1iOhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=CYeRYuN_QOzxrizBdR-y82NbwjI5Vuf1imTdC8j3A3LBssnUg19XwMG-77elrUWv2SEFcjN9YI-meFxduUt705BSnA-kW-VG1TlWY0SIAvZBZn4Yu_dVJSSxwAdrp8JICOksFWwc2SNPKLfQ1d6PR7-5bHQoi1AVD3hHGcmkx96_wsLdIyY46FghoschuJoPrEdPc4SP-eAKvhC_a2kLO6igjOBNSzl6T4sDBc7NMJgnrYT22tOpQBcQOoXCneZKE7gLh3BIKwjJQttIxJlelWQJxryWsKiyfAF1IGl_HoPXBqHWtJblXCb_2Aaxz0_xEdLSh2oPvBJoogJGeT_iPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=CYeRYuN_QOzxrizBdR-y82NbwjI5Vuf1imTdC8j3A3LBssnUg19XwMG-77elrUWv2SEFcjN9YI-meFxduUt705BSnA-kW-VG1TlWY0SIAvZBZn4Yu_dVJSSxwAdrp8JICOksFWwc2SNPKLfQ1d6PR7-5bHQoi1AVD3hHGcmkx96_wsLdIyY46FghoschuJoPrEdPc4SP-eAKvhC_a2kLO6igjOBNSzl6T4sDBc7NMJgnrYT22tOpQBcQOoXCneZKE7gLh3BIKwjJQttIxJlelWQJxryWsKiyfAF1IGl_HoPXBqHWtJblXCb_2Aaxz0_xEdLSh2oPvBJoogJGeT_iPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=lEnhSxbYJf0DF-i8dRDti9jUM_P6teNF5AFoeQPq7XUT8c27HAwIAsVEVlu9LOd2W83XXXN0jTdN9enHvXskzu58VzCuDrFyDX3rSct9Ytw4lazFVuO-TSId5Lm0G-RyUtXNQ65Ec1kB4B8VCiXb0DJFQMT1-31K6TwUtvffZ1bndWv5VVJKfcoIoXozUylPeZwLPqJSeLsYClYQfB4MI04CUOhpjA1v-CqAzxmSktbGbP4bZNJdN4PQ23Al8VuotM-mDIiuRqXQmDetTy4SDg8mTa3kU2-0amZrOhFdKoYcy_JPx5pPC6mkiOIdrpUEk_ThN2XOHrCys9WL2P5JZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=lEnhSxbYJf0DF-i8dRDti9jUM_P6teNF5AFoeQPq7XUT8c27HAwIAsVEVlu9LOd2W83XXXN0jTdN9enHvXskzu58VzCuDrFyDX3rSct9Ytw4lazFVuO-TSId5Lm0G-RyUtXNQ65Ec1kB4B8VCiXb0DJFQMT1-31K6TwUtvffZ1bndWv5VVJKfcoIoXozUylPeZwLPqJSeLsYClYQfB4MI04CUOhpjA1v-CqAzxmSktbGbP4bZNJdN4PQ23Al8VuotM-mDIiuRqXQmDetTy4SDg8mTa3kU2-0amZrOhFdKoYcy_JPx5pPC6mkiOIdrpUEk_ThN2XOHrCys9WL2P5JZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=Hj69EDgMtl292HucwOSAOWgNXVXBzNcPP2q1v-76_a75gcaTkkdbUtmaamq0m9eT4Ecp7FBqIU2vAAU_NRfBAdG_ZjUlS2CTYWGJVeDzhgAgjLgRZdXkr88awkUOpZ77ewhxW8GLOmnfvNM6ybQ7FTI-GH-y0CxPdBJ-KmTLSfz1Nv85NGTJUm4sAkjsYRA3ILKo9zw4Rzlv9ORAzPmJfmanNEc_Fp-atYxHANRMEsy5OhZhEUzXUSFL31drO-NkMN3zCpGCKvqF6J6j28CkclH0OBG0FQW1bSCmXbQuvoYIWfNu3akZc0onZApObDIhfRuKbFCwPVtqN150yIQuAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=Hj69EDgMtl292HucwOSAOWgNXVXBzNcPP2q1v-76_a75gcaTkkdbUtmaamq0m9eT4Ecp7FBqIU2vAAU_NRfBAdG_ZjUlS2CTYWGJVeDzhgAgjLgRZdXkr88awkUOpZ77ewhxW8GLOmnfvNM6ybQ7FTI-GH-y0CxPdBJ-KmTLSfz1Nv85NGTJUm4sAkjsYRA3ILKo9zw4Rzlv9ORAzPmJfmanNEc_Fp-atYxHANRMEsy5OhZhEUzXUSFL31drO-NkMN3zCpGCKvqF6J6j28CkclH0OBG0FQW1bSCmXbQuvoYIWfNu3akZc0onZApObDIhfRuKbFCwPVtqN150yIQuAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=FpydNrPcgK9U0eiE3hADufE4SMOGdhQyIReRr14xeSJphGDBWmOhg4HueOrOd_G_Fg79VIzZ9U2DGSJ8kEotMrBFnKjoQYGOHTuTfzOevqm125NTAHg8-C4iE7-Ge-JSkd6CTvpb3eCkstF2LN7OS_wof3v3fL_yN4_KFyu4WLnEqnYVocjhTRMiIzg7QhZbehb6oUjy75etcfNHzR5QUN3wuIJ0ye5aw4RHHtsFh2_VO4sCiqOtpXmrs-vHPjqoY7fUuctf3qdC176kK2gnozhNt8qSYC47KoNC7NyuBRtWk0JFivB-e_xhqMGN-Cjqiwcm3agVwK0FoD2ysRxwAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=FpydNrPcgK9U0eiE3hADufE4SMOGdhQyIReRr14xeSJphGDBWmOhg4HueOrOd_G_Fg79VIzZ9U2DGSJ8kEotMrBFnKjoQYGOHTuTfzOevqm125NTAHg8-C4iE7-Ge-JSkd6CTvpb3eCkstF2LN7OS_wof3v3fL_yN4_KFyu4WLnEqnYVocjhTRMiIzg7QhZbehb6oUjy75etcfNHzR5QUN3wuIJ0ye5aw4RHHtsFh2_VO4sCiqOtpXmrs-vHPjqoY7fUuctf3qdC176kK2gnozhNt8qSYC47KoNC7NyuBRtWk0JFivB-e_xhqMGN-Cjqiwcm3agVwK0FoD2ysRxwAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8VYHCOGPkDH4Wpa_1dsEFqYqIQ7EnRVDsh9kx70qtLAbY6QXOlxOaezxaLQkg80jqxbSogZtJMmZQjnvzmeS3dBvTwnyqcaVkAyZNRBj2aka9OX3na7TjSOxKjNRz7ZD4QlbznTBEdnJ8E4mvWUFs7hPrj24gFCv9RGfTVtj_khrJdbMYcgeDd2N09vPund_CXpvyiM1R_8K-fvudJNV5W104EKC3p0qqhCQCPG9sHG5phc2Tj8OEbPZXs5lnNI0RF_2j6yVowdo8iEoGkgLecu0QwagBqZ3yPkpmNrIykaE5_8EmNEwPSW03hJDhlcKyem3Q-RR3EJDcjMyigKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV-E6Z0MDWDmr4Xp3wx7GiyloPtiMkAoE4N7IwBfF4ZQG1QSy_BuF1XO8HktfA-fDRbFmseGBQVLRjblGu5lDbIClASd59WZSElux1GC-lI1nOMTInC1ILH3jQNZjhr2aUqJtexS-1rDLXcjqsLXfVTlxes2LZgIiZO-g7L4rIbqf2hlyMuNOoxyVKbu8bQg2_d4gLo9tTnf60OolNWhKUNBWsEO1-C-6T9XRyR0HwEYP17iiu65oJradFJeHAqR4Bf4bzvGMNAXx1HgbjoZJpQBUK_9CzVMj-oaTEeABi8TbzEnwLPNyvYHIy1rG6m-e_4aztt2oItNCcOc-x9RaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=ibcdPSDaSvx42gOEi4V4EH09ohNSj3aWYViveCzZJ4pJpseD-BDGgS3MEOrqZL5llXR5EyhinfDRAi4SceaDNfXvqyavGzHCuG8psZjd6UgWOzyNNIKAbdyEPFV0EDCcNCHJsb3XlUAW4A7d5v6QyvRxbxkBJi6XQ2l0O7toghsyi48ZrXwa2K8OROtXlJKzg6hm_9QxL6ckrIjVF8bXJkfAXW941De9rXTMB9viwhN5Ln2WwcmvnLRGuPgzlZyVcHbZblM1CUi5eX5yUcadMc_EGc3Ao6SQD16OIdTTBS1kKnChFUyw0mSSj013yLeWqF3yLJsF-rqEvnM3PCF6Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=ibcdPSDaSvx42gOEi4V4EH09ohNSj3aWYViveCzZJ4pJpseD-BDGgS3MEOrqZL5llXR5EyhinfDRAi4SceaDNfXvqyavGzHCuG8psZjd6UgWOzyNNIKAbdyEPFV0EDCcNCHJsb3XlUAW4A7d5v6QyvRxbxkBJi6XQ2l0O7toghsyi48ZrXwa2K8OROtXlJKzg6hm_9QxL6ckrIjVF8bXJkfAXW941De9rXTMB9viwhN5Ln2WwcmvnLRGuPgzlZyVcHbZblM1CUi5eX5yUcadMc_EGc3Ao6SQD16OIdTTBS1kKnChFUyw0mSSj013yLeWqF3yLJsF-rqEvnM3PCF6Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3PwyMzdDAU-HX731jHMUaL3zYjY0TuKcnqfWy2tueF32gkyffTw043XmhJinUk5dVr-SNp_bHDtxs83n0c03BkGJpER6LEo4W2msO3DK_sshwkXfYAmIRtU1ywhIa6a7hx4jgzjyCTJiYOHY63GthhAeXC-tV7PHoGqwxGAqbGzPl8SskNoYVtnemnwGx-_f9loG-N5euFg6e1ivfnt1KqxM4buZabXEujmIzWHphk6_y00AWi6RmsSKErwgEZwO8WtDNkCl6tEBJP1M_7gRHj_HaUKuGI9tgwnjG0CHh4sFR1Ffx5LrPNRcfBhEh1ebGGQ_TaKElhBwjv6JWLu5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
