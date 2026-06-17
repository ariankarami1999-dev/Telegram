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
<img src="https://cdn4.telesco.pe/file/clmfUNAIiZFN6c_UxsrBsPu8z_6scjlgBKSprpmbDi5lXHyvjAu_7f8YX21QA-vU4JxtUx73OaLrF_R9cMRLZo7kKnTwDxa9ZVC9tTyV_09hgGjavAkBOAXqkZkilzlDQ-jw-8SS77noNyWNuaqQdZKFY4yI5sIAvkzQL0UF8wRckI1PHZVvNH0f75ncug-Dy10gKIir5e0EzJsiUfaV1xKNrgj_gWN2hovCK2f1yUyCQXoMN6N6qDkOP-jo4hV2L-Mal_rxmb1IHn8CKJwNNf0Pu131jfvjMdhn3Ruq03sNTyLAATLDRnK_Hzpo05TyX83MtxGq0B0XxALmtlcLAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 20:57:42</div>
<hr>

<div class="tg-post" id="msg-442839">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfed1494b7.mp4?token=opErP0_774y9BcXqtANmYirM2w1pAwOI-zmPVeT8UHYkYqkAVQnu763TzU1m1dV0PvXSAyG6wo989vT8tWS9WOhKLqRwgjxuWV2LIfvV0eR_c2EbBMYAyCr1uXQCGN2Dbrnc6DO9D4lFABEvgDWMAI8_Rb149f0uFeUV8QqSa4G_DVyBT4JKCVXxIsp0FIl7D_ogjoT1PYcck-278i7BA4pIvefNytDrSya7gKdt98JPDH5u5DG9Gp4KupBCG2wb9SD8EcWbfRPieew4d0RTB_qPzwaujreTYP_OZGvaZ2aY8cx8bRztx8wx6OCzsDD364h-QKp_IkTtR5GjxVmglVd7PJvA0NaD91WdsMRECL6wANgY_y4Tn4ZZo2aDy2QjQoN8xrk4SYMf-xLEuDMPzSuU30tQwcct49HQYYml1GtkQPTTowizeCfwSG_PaT3n3MioetPOAti8UHv01x7KSTRXKvdRTN0VAcWfcWoE3IM7dbSv1CFuCtqI20DevnNd0MyyHOC7R6VwQOzMk3CYBH0nFpqSskgKXVFVaI59PrNSwQjAtaiXdkWBGkOWvGUpshUhGPXkQiwts2Fo4lKDr289ffBWSRIBem9gZQwooavlqkOwm4GC7tIrE4MD76cTNbvBsKgOfKsRhaMMkRt5BXjCN9NDwruIKSlSwcUbul4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfed1494b7.mp4?token=opErP0_774y9BcXqtANmYirM2w1pAwOI-zmPVeT8UHYkYqkAVQnu763TzU1m1dV0PvXSAyG6wo989vT8tWS9WOhKLqRwgjxuWV2LIfvV0eR_c2EbBMYAyCr1uXQCGN2Dbrnc6DO9D4lFABEvgDWMAI8_Rb149f0uFeUV8QqSa4G_DVyBT4JKCVXxIsp0FIl7D_ogjoT1PYcck-278i7BA4pIvefNytDrSya7gKdt98JPDH5u5DG9Gp4KupBCG2wb9SD8EcWbfRPieew4d0RTB_qPzwaujreTYP_OZGvaZ2aY8cx8bRztx8wx6OCzsDD364h-QKp_IkTtR5GjxVmglVd7PJvA0NaD91WdsMRECL6wANgY_y4Tn4ZZo2aDy2QjQoN8xrk4SYMf-xLEuDMPzSuU30tQwcct49HQYYml1GtkQPTTowizeCfwSG_PaT3n3MioetPOAti8UHv01x7KSTRXKvdRTN0VAcWfcWoE3IM7dbSv1CFuCtqI20DevnNd0MyyHOC7R6VwQOzMk3CYBH0nFpqSskgKXVFVaI59PrNSwQjAtaiXdkWBGkOWvGUpshUhGPXkQiwts2Fo4lKDr289ffBWSRIBem9gZQwooavlqkOwm4GC7tIrE4MD76cTNbvBsKgOfKsRhaMMkRt5BXjCN9NDwruIKSlSwcUbul4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ مردم به منتقدان: تجمعات، مشق کربلاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/442839" target="_blank">📅 20:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442838">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a2c30169.mp4?token=e9WZhEhdMR4GOVqHzP-ixi53tzrOd-rag6DAopzkHNywjMyo8D1tVvXBEWiYhmb5ZgXdypqco4c5D38o56IxC1POMU56zwIfK4kHWmvKwQ0e369VR2gdlCIYO7Sh_pAgedOWP4kStccNaw5jNabSRiepvPUH6JjaYwI_03pFXoRiMPgUxBO9DcZKSHo2hLqUKqkMzcNJIFIh3M6v4VhnLvZ35c-DJ46ZKNTV235cMDSLqdhfcYzmDBV9bvtnoaKUVjlgSUtodlw3yv9djUGnE0dTiojL6mCxIgLhbLT_TnU_XYXYfHUogrPG23FJgME-jE8GdOjmqv-7GJphEtyKpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a2c30169.mp4?token=e9WZhEhdMR4GOVqHzP-ixi53tzrOd-rag6DAopzkHNywjMyo8D1tVvXBEWiYhmb5ZgXdypqco4c5D38o56IxC1POMU56zwIfK4kHWmvKwQ0e369VR2gdlCIYO7Sh_pAgedOWP4kStccNaw5jNabSRiepvPUH6JjaYwI_03pFXoRiMPgUxBO9DcZKSHo2hLqUKqkMzcNJIFIh3M6v4VhnLvZ35c-DJ46ZKNTV235cMDSLqdhfcYzmDBV9bvtnoaKUVjlgSUtodlw3yv9djUGnE0dTiojL6mCxIgLhbLT_TnU_XYXYfHUogrPG23FJgME-jE8GdOjmqv-7GJphEtyKpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: در ۲ روزِ آخر جنگ بمب‌هایی به ارزش ۲۰۰ میلیون دلار روی ایران ریختیم.  @Farsna</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/farsna/442838" target="_blank">📅 20:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442836">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3se_wt1slmLjCJmjamI8tsQpmGFc_SsiSN26IsNN194cXCDALkboydqfkn9izcMf2cvgOAbSKEsuSDuluzukrNcFea7bt_9I9v9r16h9Utpvn07yACp5AhgZNzBSPFJGXUSvTD2W4q-d4HFVbzsvnM0YzAW0B9gfAn_Yrn3Dd8m6WdAxxcZN690CDQTU8hxggJ_c6Qur8FRCbWrr33KKFSqFRBJrJ7-bDSNxOIMScPozHk-1f3dRZREce9FADPgBCBTr_JSQang3PxqUu9nB7sELVMVST5nzTKrMQKh1vKe-J3PGHSDLtkNJXoU34Dkn1lGKGCqkvUMcntSy_Z32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر پول ایران را پس ندهیم، هیچ‌کس در دلار سرمایه‌گذاری نخواهد کرد
🔹
ما مقدار زیادی از پول آن‌ها را گرفته‌ایم، پول آن‌ها را از آن‌ها گرفته‌ایم.
🔹
این پول ما نیست، پول آن‌هاست و ما آن را مسدود کردیم.
🔹
در یک مقطع زمانی خاص فکر می‌کنم باید آن را پس بدهیم.
🔹
اگر آن را پس ندهیم، هیچ کس دیگر هرگز در دلار سرمایه‌گذاری نخواهد کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/farsna/442836" target="_blank">📅 20:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc8405859.mp4?token=jzmlUgVNsKE_AV5Xkoz_VKV8Do0mFkuSbCi7rOacFpOVKbf-EGKPsy0ipdXIJkg9VwMJDWFn7pH5dj0ahKSUMq1tcM5T8Xfw2XCGxoLOPqvV-mOvBMx7iuHQsSPijxY-NLs2_EIynXqdpz4j7W5vL5LDtc8KxZubMzYTmeA1Q_xve_6eio42UROKl3_dlFcZPa3GdQZmUh7qEx2lqBxaG9TxRILf7BjaJ3QKmTf8rkM5O7heUszvN2zx5lvsWmgi3CbM9foRFQdiQvvecV8PQ6nV1QFXXIGS6Mc-yEDrFqsi4OC7M9ktLvxhUn1y37CupX1IkCAn7vMidSguziRDCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc8405859.mp4?token=jzmlUgVNsKE_AV5Xkoz_VKV8Do0mFkuSbCi7rOacFpOVKbf-EGKPsy0ipdXIJkg9VwMJDWFn7pH5dj0ahKSUMq1tcM5T8Xfw2XCGxoLOPqvV-mOvBMx7iuHQsSPijxY-NLs2_EIynXqdpz4j7W5vL5LDtc8KxZubMzYTmeA1Q_xve_6eio42UROKl3_dlFcZPa3GdQZmUh7qEx2lqBxaG9TxRILf7BjaJ3QKmTf8rkM5O7heUszvN2zx5lvsWmgi3CbM9foRFQdiQvvecV8PQ6nV1QFXXIGS6Mc-yEDrFqsi4OC7M9ktLvxhUn1y37CupX1IkCAn7vMidSguziRDCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: وقتی [سربازان] جوان‌ آمریکایی را می‌بینید که‌ بدون دست و پا حرکت می‌کنند، یا صورتشان بر اثر انفجار متلاشی شده است، بدانید ۹۵ درصد این موارد کار [قاسم] سلیمانی است
🔹
او همه‌کارهٔ ایران بود و مورد احترام قرار داشت. او یک نابغه بود. از قضا اهل ایران…</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/442835" target="_blank">📅 20:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442834">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj7Uz5nKwXiEX7ThpcowciAtbdCHNRojJT5HpGsE0XaxbptRG0SdwDEWJZCKash27BX86ESlIa72H4no1U3KkaGKbMjU1JDrq7ac-hhfN1uYj7FARFtJaWyAKBku49DyXyZgJK2LkHxW3TM7x1H1LcnMhgO2JRWZaZQrLgwBYvA1kEhtXEv0razY4lYSEuj0rNKdmdkP_tftZII2hTl0KPxdbb-h3nhGhDRI6yysLxefN8wvgK_eUrJluN6jSrxfxJOmmh6WTdvR411m1G3tRyTlfbsXA2bEpXCC8wu1ueoJxpxfaZIVOEM-jQR5aaInr2oORLdB7LzLaL1dSl0fYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس برای مهار گوگل دست به کار شد
🔹
نهاد ناظر رقابت انگلیس مجموعه‌ای از قوانین جدید را برای گوگل اعلام کرد و از این شرکت خواست شفافیت بیشتری درباره نحوه رتبه‌بندی نتایج جست‌وجو ارائه دهد.
🔹
بر اساس این مقررات، گوگل باید نتایج جست‌وجوی غیرتبلیغاتی را بر اساس معیارهای مشخص و عینی رتبه‌بندی کند، اطلاعات بیشتری درباره نحوه عملکرد سیستم رتبه‌بندی خود منتشر کند، فرایندهای شفاف‌تری برای ثبت شکایت در اختیار کسب‌وکارها قرار دهد و همچنین امکان انتقال داده‌های جست‌وجوی کاربران به سرویس‌های ثالث مجاز را فراهم کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/442834" target="_blank">📅 20:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442833">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e6db6afa.mp4?token=pi5A6zW56ZMSWFWwmAFNkLlSrLM_gmq8dZWpcH3mT6x6qXD7oGCM3EuXcQNnX6C4NAfHM5S2F09lIf5gIvGudFd943leUl5P9Y70YPj8rkaCDBVgwoQ4drjhmBronFdN8Ile4qP6n0yAEeHCt3L4Ml2DPRSoN6bbTUui_kCLG2V-QBjfV8b9pG5_L-ZbFvbMpVjebBiTjgbky8ObsjvEjRQ99mMfmVAOJNKKJ3VZOVg82SwE52-dpmUei24_sElw1JwVbiBACp-qHi7JJNcJV4X46DXstVCKT5_7Z4wXLdV39NdLVUy7SoDncX7-bMut1YnxoSBAYzTvTaZUl6cbkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e6db6afa.mp4?token=pi5A6zW56ZMSWFWwmAFNkLlSrLM_gmq8dZWpcH3mT6x6qXD7oGCM3EuXcQNnX6C4NAfHM5S2F09lIf5gIvGudFd943leUl5P9Y70YPj8rkaCDBVgwoQ4drjhmBronFdN8Ile4qP6n0yAEeHCt3L4Ml2DPRSoN6bbTUui_kCLG2V-QBjfV8b9pG5_L-ZbFvbMpVjebBiTjgbky8ObsjvEjRQ99mMfmVAOJNKKJ3VZOVg82SwE52-dpmUei24_sElw1JwVbiBACp-qHi7JJNcJV4X46DXstVCKT5_7Z4wXLdV39NdLVUy7SoDncX7-bMut1YnxoSBAYzTvTaZUl6cbkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
🔹
ما روی یک تلاش موازی با کشورهای حوزه‌ی خلیج [فارس] کار خواهیم کرد تا به مسائل غیرهسته‌ای، مانند موشک‌های بالستیک متعارف که درباره‌شان صحبت خواهیم کرد، و حمایت‌ها بپردازیم.
🔹
کسی می‌گفت:…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/farsna/442833" target="_blank">📅 20:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442832">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1c2256de.mp4?token=mNx0iYtgjrNLMrA7CBGFyoyHTRMcdUTUGdGDw5A5cw2v3ZB2FWPsEnyYJhSiP8kNjn__oHSRYrZJN0fnaF6g1jGYLl6-wclAhPu4x3vKnOwRjHePX3bY24T1OpRH5uRCpoPB8qE_SNlXfslwBaJIuOLWl5NQkW-FZq2lCd7s2I4G29RypdYL7oyP3-B3yvXGTtO7ppbLukpjjP8-cSQv6otIdrFw1dPseEKH2U0hXxj-UfiU9TdHYOhrEYyzVd3hM2ieoVRzHdG0oU5mm_hybiWD9khoQkusL0QOEGGrLHRm4Bmm8gxGTSvzjQXQlbvIbtd1fX8gFDpL1StN5du6IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1c2256de.mp4?token=mNx0iYtgjrNLMrA7CBGFyoyHTRMcdUTUGdGDw5A5cw2v3ZB2FWPsEnyYJhSiP8kNjn__oHSRYrZJN0fnaF6g1jGYLl6-wclAhPu4x3vKnOwRjHePX3bY24T1OpRH5uRCpoPB8qE_SNlXfslwBaJIuOLWl5NQkW-FZq2lCd7s2I4G29RypdYL7oyP3-B3yvXGTtO7ppbLukpjjP8-cSQv6otIdrFw1dPseEKH2U0hXxj-UfiU9TdHYOhrEYyzVd3hM2ieoVRzHdG0oU5mm_hybiWD9khoQkusL0QOEGGrLHRm4Bmm8gxGTSvzjQXQlbvIbtd1fX8gFDpL1StN5du6IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
🔹
ما روی یک تلاش موازی با کشورهای حوزه‌ی خلیج [فارس] کار خواهیم کرد تا به مسائل غیرهسته‌ای، مانند موشک‌های بالستیک متعارف که درباره‌شان صحبت خواهیم کرد، و حمایت‌ها بپردازیم.
🔹
کسی می‌گفت:…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/442832" target="_blank">📅 20:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442831">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05235cdc5c.mp4?token=FttkstVUS6y7vSCBPxzzzmzYdPKPGqcxZfYjeQu7bfo2KZGRg7ECdbqZEFq_MlR9kMaoc6i6Cx8qdbdjgr_Bl5GNwOFLQeJYR43PDyWPDmrys7dp_SmV0ct4t0WqdPo9FArtRRGm3nXxGOOIUkwzQKzCYc9izSMcfjqHL7IL8boUEn800o4FlNSt5MOtKk3LT8Aetpy7R4e8LTBmWtKRU2C0F1ziCs8tv-VzISuaxct7myzhh4TvyI27sLRFdYBm8pK3eLP2mvjPmmVw9jmnrF8qYF1Uub-9jCpP-rq0hKysQ_kyENLH13ikb6c92WBGch4LUzumG7n50ZdWKKlltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05235cdc5c.mp4?token=FttkstVUS6y7vSCBPxzzzmzYdPKPGqcxZfYjeQu7bfo2KZGRg7ECdbqZEFq_MlR9kMaoc6i6Cx8qdbdjgr_Bl5GNwOFLQeJYR43PDyWPDmrys7dp_SmV0ct4t0WqdPo9FArtRRGm3nXxGOOIUkwzQKzCYc9izSMcfjqHL7IL8boUEn800o4FlNSt5MOtKk3LT8Aetpy7R4e8LTBmWtKRU2C0F1ziCs8tv-VzISuaxct7myzhh4TvyI27sLRFdYBm8pK3eLP2mvjPmmVw9jmnrF8qYF1Uub-9jCpP-rq0hKysQ_kyENLH13ikb6c92WBGch4LUzumG7n50ZdWKKlltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
🔹
ما روی یک تلاش موازی با کشورهای حوزه‌ی خلیج [فارس] کار خواهیم کرد تا به مسائل غیرهسته‌ای، مانند موشک‌های بالستیک متعارف که درباره‌شان صحبت خواهیم کرد، و حمایت‌ها بپردازیم.
🔹
کسی می‌گفت:…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/442831" target="_blank">📅 20:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442830">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8915264142.mp4?token=CbzwvKihfoxbX_kEOzixHZ-X-AwiF5tVB0z4ax9RjDCyUU-qtJ9ijyImF7sQSWQsHPlJOOR1kfd2aN-dxo4Ts8_5DKq0I0Jd3TPMuZ1mc9Z_P7Thp41oa7zf69TA_T53o-al_gegSVndqX2T4NRsWbjbgkOvJiw8BGPalRwu4zLqVcK4UggFsJd0s0DJ-uB4ThSXl0prUxmCpj0vOXUG-YM3ylmQbmUlaD_q-wy92m8wF0nA-kxQfLPEsrhmsUp4hmJZKU1RLtCGJyGe9LpZU0zzSmYMU5Rsu9AM1oLQE33o2uOkWlXweVVLGlNXdit3sHI51ySsVasF2QuysIKXIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8915264142.mp4?token=CbzwvKihfoxbX_kEOzixHZ-X-AwiF5tVB0z4ax9RjDCyUU-qtJ9ijyImF7sQSWQsHPlJOOR1kfd2aN-dxo4Ts8_5DKq0I0Jd3TPMuZ1mc9Z_P7Thp41oa7zf69TA_T53o-al_gegSVndqX2T4NRsWbjbgkOvJiw8BGPalRwu4zLqVcK4UggFsJd0s0DJ-uB4ThSXl0prUxmCpj0vOXUG-YM3ylmQbmUlaD_q-wy92m8wF0nA-kxQfLPEsrhmsUp4hmJZKU1RLtCGJyGe9LpZU0zzSmYMU5Rsu9AM1oLQE33o2uOkWlXweVVLGlNXdit3sHI51ySsVasF2QuysIKXIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: پل B1 ایران، معادل پل جرج واشنگتن بود و ما بمبارانش کردیم
🔹
مردم از من می‌خواهند که پل‌ها را بمباران کنم. چرا بمباران نکنم؟ من پیش از این هم چنین کاری کرده‌ام؛ چون می‌دانید، آن‌ها زیر یکی از وعده‌های خود زدند و من بزرگ‌ترین پل آن‌ها را بمباران کردم.…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/442830" target="_blank">📅 20:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442829">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e4a2d661.mp4?token=C0lkHnJha9Yt28yaw02j83cDm0uoNKFF46hvfH-Bi51xPReBXof3r8m2XODoHVKN-hTZHxwIZWTwIpjLo-cxzNk-CtaOHeXLa_EBzfmeSxxFzF-ahUwEDdOGQT7uS_9kKhZN3mQ2fcWCZasox3lRInoTvYhlOEGjA8QKlFJTQL0arHkCKLngRYbzdVgDpbhr9qUqKwNjjiB4rfUI5W4oEXavkNTGMIaT2h8lZpFJGtzZfrvoz5Q_ce8UtwlcNTHCrLUMq-B9OoHAJPiSMIcPAPhx9aiaUceiY7l3J27IVLQTS1AfqIkUlCmMRHXWE6P0Njc44SYm-qmLsoNTW_WOAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e4a2d661.mp4?token=C0lkHnJha9Yt28yaw02j83cDm0uoNKFF46hvfH-Bi51xPReBXof3r8m2XODoHVKN-hTZHxwIZWTwIpjLo-cxzNk-CtaOHeXLa_EBzfmeSxxFzF-ahUwEDdOGQT7uS_9kKhZN3mQ2fcWCZasox3lRInoTvYhlOEGjA8QKlFJTQL0arHkCKLngRYbzdVgDpbhr9qUqKwNjjiB4rfUI5W4oEXavkNTGMIaT2h8lZpFJGtzZfrvoz5Q_ce8UtwlcNTHCrLUMq-B9OoHAJPiSMIcPAPhx9aiaUceiY7l3J27IVLQTS1AfqIkUlCmMRHXWE6P0Njc44SYm-qmLsoNTW_WOAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: با نتانیاهو اختلاف‌نظر کوچکی بر سر لبنان داریم
🔹
او مرد خوبی است و گاهی کمی هیجان‌زده می‌شود. من می‌گویم: «بی‌بی، می‌توانی کمی نرم‌تر برخورد کنی؛ نیازی نیست هربار که فردی از حزب‌الله وارد ساختمانی می‌شود، آن ساختمان را با خاک یکسان کنی.» @Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/442829" target="_blank">📅 20:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442828">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b66ebd12a.mp4?token=vErD-Gzp7CNmVe7QYF_oi280080KrjCg7YP-n6tP0NPdX6vyUO3G3uQPAEpSMXQbzEZjHsXMnbxr5NVf04Hi8uEmjotxWucNHaNrw2dt3RY2x1S8BEskmpBsRhuHwN7BFp4CeCPyvwHKEZQr0KcTonZOj58FrIgSkSf5DiDxDWIamZzUdykE5c0GhXgi_HqdpGumNUZ4m3cGIKqhVcfVC26fLg3bqsCaV3BjpUHivl2Rc79h-F2CAwBeDBvcx2Sq_10wChzZ9W3hgemfWj_z0lpX61cw7rqYS6URQlk40OlddhU1B7e0NosxX4d4ARhG1hd-mpvrqYwYd1rXy-RYvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b66ebd12a.mp4?token=vErD-Gzp7CNmVe7QYF_oi280080KrjCg7YP-n6tP0NPdX6vyUO3G3uQPAEpSMXQbzEZjHsXMnbxr5NVf04Hi8uEmjotxWucNHaNrw2dt3RY2x1S8BEskmpBsRhuHwN7BFp4CeCPyvwHKEZQr0KcTonZOj58FrIgSkSf5DiDxDWIamZzUdykE5c0GhXgi_HqdpGumNUZ4m3cGIKqhVcfVC26fLg3bqsCaV3BjpUHivl2Rc79h-F2CAwBeDBvcx2Sq_10wChzZ9W3hgemfWj_z0lpX61cw7rqYS6URQlk40OlddhU1B7e0NosxX4d4ARhG1hd-mpvrqYwYd1rXy-RYvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: با ایران فقط تفاهم‌نامه داریم و اگر موضوع ظرف ۶۰ روز به سرانجام نرسد، ایرادی ندارد؛ ما دوباره به بمباران برمی‌گردیم.
🔹
آن‌ها توافق کرده‌اند که سلاح هسته‌ای نسازند و شما این موضوع را به وضوح در متن توافق‌نامه خواهید دید. @Farsna</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/442828" target="_blank">📅 20:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442827">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07d944cd88.mp4?token=FZxFpFosyo2W83eowXRh8TrIiEGF6GfzPnqjTJi2VcT908i4TSzyFaWmnZ-vQQDHceCMByHqxgnaUWtsrsGku1-yrQEDFOEOM_lXkNe7gL6zfxIqRtVf9zDSgdo-nA9wB4TguoPVVw1UzjTbgakO4ZHWtkiu9pW6yE7FNkyefZOQ-jDaHwzDY1au348G7gl6t4g8r_RQVTEIgA6lTTO7ze2Ltd5VHki3IfrhTYK4YiH6Smq2d6JzxHtZynoMpDhRSfJuNEkY7kOMbx6FiE4BMv3D4vi8OG3C7EWupHiF0tE-HgPAsx2x2KFnOJ_10hOQ2OBA74ME0VbzKeZtCzFk7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07d944cd88.mp4?token=FZxFpFosyo2W83eowXRh8TrIiEGF6GfzPnqjTJi2VcT908i4TSzyFaWmnZ-vQQDHceCMByHqxgnaUWtsrsGku1-yrQEDFOEOM_lXkNe7gL6zfxIqRtVf9zDSgdo-nA9wB4TguoPVVw1UzjTbgakO4ZHWtkiu9pW6yE7FNkyefZOQ-jDaHwzDY1au348G7gl6t4g8r_RQVTEIgA6lTTO7ze2Ltd5VHki3IfrhTYK4YiH6Smq2d6JzxHtZynoMpDhRSfJuNEkY7kOMbx6FiE4BMv3D4vi8OG3C7EWupHiF0tE-HgPAsx2x2KFnOJ_10hOQ2OBA74ME0VbzKeZtCzFk7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی متفاوت از حضور خانوادهٔ شهدای میناب در حرم امام علی (ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/442827" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442826">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77331e7d9f.mp4?token=jGSBTgAyWZmxOz5IdsOx3FTAS0V4IV_6Woo6p44iPsi7VNUMtpOt-KsTzPsat414vYphOxBAi8Lp2jFSWjI5uuWoVbajrBqEb4u5Ubey8sV1gBvWt-S24OLIezdCSEeKgzAmmn99pxcpaANBGBw9wMwrFzagKzpye2eJ-MTKPKZsteCFg92oCDgc14Lh1QVw3KK6gv2rFCTTLyCt7zCdO9Tv2cuHqU3jx6jT7nKpFW8kbgYrkN-_rWbEaAMbwXrOqGNn0ihr_e5VIR3BmttcKc8dFcERIoUNyXvu8K0HOx67D0FtNZY2cgz9g0FoW18zCoYEIPvOWJA2pgC-VxTJPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77331e7d9f.mp4?token=jGSBTgAyWZmxOz5IdsOx3FTAS0V4IV_6Woo6p44iPsi7VNUMtpOt-KsTzPsat414vYphOxBAi8Lp2jFSWjI5uuWoVbajrBqEb4u5Ubey8sV1gBvWt-S24OLIezdCSEeKgzAmmn99pxcpaANBGBw9wMwrFzagKzpye2eJ-MTKPKZsteCFg92oCDgc14Lh1QVw3KK6gv2rFCTTLyCt7zCdO9Tv2cuHqU3jx6jT7nKpFW8kbgYrkN-_rWbEaAMbwXrOqGNn0ihr_e5VIR3BmttcKc8dFcERIoUNyXvu8K0HOx67D0FtNZY2cgz9g0FoW18zCoYEIPvOWJA2pgC-VxTJPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما فردی به‌نام سلیمانی را از میان برداشتیم. فکر می‌کنید اگر او زنده بود، اتفاقات فعلی [برای ایران] رخ می‌داد؟
🔹
او یک نابغه بود. مردم این را فراموش می‌کنند. من در دورهٔ اول ریاست‌جمهوری‌ام سلیمانی را از میان برداشتم. بدون آن کار، احتمالاً ما در موقعیت…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/442826" target="_blank">📅 19:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442824">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc2d4a638.mp4?token=PuB0rX9s7U-iSTb6X5wU0n9KuunKNM9XVNPbM_G8VpeysqWjuOX5qru2ghbd-q0tv-6wTGWntWiMRpzFd7s_RVflngM23UX7wedTitB-ZAwMsyeQXYjmPeCLiOjfUMk-Z2MqqAi4DxHtu_7Rga40ALzilqc54M3oMcRvzDCobxIlLg68VEBsgNvzJhNEN_SsCpnhA7XUZMqgZ_Kcu1Jr29Mn84zvFc6rZPT3ULmD8-NQHeb1fN7lRbFFztpp57uZ-S_ajmbW1-ZRA_o2yT8z-AsAFpQJQ9NTxkDaOt2VK3aIbDXJ0SmQ9IhGLRpNQuKVMQGNsO8NTBc9sPpT40UKKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc2d4a638.mp4?token=PuB0rX9s7U-iSTb6X5wU0n9KuunKNM9XVNPbM_G8VpeysqWjuOX5qru2ghbd-q0tv-6wTGWntWiMRpzFd7s_RVflngM23UX7wedTitB-ZAwMsyeQXYjmPeCLiOjfUMk-Z2MqqAi4DxHtu_7Rga40ALzilqc54M3oMcRvzDCobxIlLg68VEBsgNvzJhNEN_SsCpnhA7XUZMqgZ_Kcu1Jr29Mn84zvFc6rZPT3ULmD8-NQHeb1fN7lRbFFztpp57uZ-S_ajmbW1-ZRA_o2yT8z-AsAFpQJQ9NTxkDaOt2VK3aIbDXJ0SmQ9IhGLRpNQuKVMQGNsO8NTBc9sPpT40UKKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما فردی به‌نام سلیمانی را از میان برداشتیم. فکر می‌کنید اگر او زنده بود، اتفاقات فعلی [برای ایران] رخ می‌داد؟
🔹
او یک نابغه بود. مردم این را فراموش می‌کنند. من در دورهٔ اول ریاست‌جمهوری‌ام سلیمانی را از میان برداشتم. بدون آن کار، احتمالاً ما در موقعیت…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/442824" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442823">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d7e262eaf.mp4?token=vedgw3Sljm5YHhMKoF7R7gsGQdqFPwYC9bECELLvDkXQppOGuPCaQ-Evwxe6dl-9G52y3MmxlAMztFIGT4DAEKYFiwOif8EQRFRX1T7gUmhme62ZGShLGl7WCZ-sZucQ9yLiRg14g2xCdQ62HIZo1OE_GhvadAISfm2OoXzkSKl1R3iuT8uV2mki8GdmNtkRGST3uL-ZXmjNvomk9cjmuHxn12virW5rOm1BVY2AHHTgkWmf0I4ig83FV-POs22RR6mRryFJs-lFbruOlzlYLn9lsf3yjBYM7zIpXMHElbZiHM61Pn8Y7bjR1Ls2rY_k8fhMowDtjOtQZDvsLTFCV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d7e262eaf.mp4?token=vedgw3Sljm5YHhMKoF7R7gsGQdqFPwYC9bECELLvDkXQppOGuPCaQ-Evwxe6dl-9G52y3MmxlAMztFIGT4DAEKYFiwOif8EQRFRX1T7gUmhme62ZGShLGl7WCZ-sZucQ9yLiRg14g2xCdQ62HIZo1OE_GhvadAISfm2OoXzkSKl1R3iuT8uV2mki8GdmNtkRGST3uL-ZXmjNvomk9cjmuHxn12virW5rOm1BVY2AHHTgkWmf0I4ig83FV-POs22RR6mRryFJs-lFbruOlzlYLn9lsf3yjBYM7zIpXMHElbZiHM61Pn8Y7bjR1Ls2rY_k8fhMowDtjOtQZDvsLTFCV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: رابطۀ ایران با چین رابطه یک مشتری یا همتای تجاری نیست بلکه به معنای واقعی کلمه باید شریک باشیم
🔹
نمایندۀ ویژۀ ایران در امور چین: در هر ائتلاف منطقه‌ای که شکل بگیرد، ایران و چین حضور خواهند داشت و من با قدرت در این مسیر حرکت می‌کنم.
🔹
ما صرفاً یک…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/442823" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442822">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دبیرکل حزب‌الله: پیروزی ایران موازنۀ قدرت منطقه را تغییر می‌دهد
🔹
نباید ابعاد جنگی علیه ایران را دست‌کم گرفت؛ زیرا هدف آن نابودی نظام ایران و پایان دادن به زندگی عزتمندانه و مستقل مردم این کشور بود، اما این هدف محقق نشد و روند تحولات تغییر کرد.
🔹
دبیرکل حزب‌الله…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/442822" target="_blank">📅 19:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442821">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfuxlrIRsg4oJMIm21DLdbflWWPDqZM4WNrUP_-3unaCdgbj1vkEhTuRCyCJPuPX2PaQ_m6uJtc5pL_Q1CIJlkTJ8PHsIaXi_NnUGoQsKm_LlCPMw_p-ylRKALNgHisBcMW7008fAoQeUtXPILyebAOgnoeToNwaxDQzgOMGQwRKjdf1pEKDsenIpFblj6jOPg6S3nu8bpG2UDFvNWvyXjQsAtjK2-uD_uAgDDLFrO4nwq2RNG4esVHTRsFoXUIsShh73XKIVpF0E4_oQLP_aD2J8NPwEotstlwTPqDuT5MgzpjNlUy38v_cKISFETx5x-B_db56x_PbwIvo572LQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله: پیروزی ایران موازنۀ قدرت منطقه را تغییر می‌دهد
🔹
نباید ابعاد جنگی علیه ایران را دست‌کم گرفت؛ زیرا هدف آن نابودی نظام ایران و پایان دادن به زندگی عزتمندانه و مستقل مردم این کشور بود، اما این هدف محقق نشد و روند تحولات تغییر کرد.
🔹
دبیرکل حزب‌الله لبنان با اشاره به پیامدهای این تحولات گفت: موازنۀ قدرت در منطقه تغییر خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/442821" target="_blank">📅 19:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442820">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tw0bLgL4CTrC6wVbfqXMj-HdcxyYEC8iRN37hdzKt80t2N83IXvX18W5tgcvsRJNhBUx7J8ovV8pfyvJUHLUprgbLWjGVhtN3HMa3LhHsLNoxXf2f85E__9p1oA9lyMzQKAdbtA509ehlkUVrKQPQxVGrpJJBB58usX3hFz7Z7M2D1fLyTBouHZIynCABNIFfcxMJb5z_wZEzSSF7NN6iC3B-f8ArQc2EUotliWXC8r4MdELElP306dwipyaIxaJllY4z6TLtpv17VASR0WwBhUIDLmc5xX_5aSG_PxcUOWAOFLtxfY91BPSQxNQ1hFWy2MEjekgfMGUfdw-IiXFRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین دیدگاه‌های موافقان و مخالفان مفاد تفاهم‌نامه و مذاکرات با آمریکا را در فارس تعاملی بخوانید  تازه‌ترین مطالب و یادداشت‌های:
🔸
محمدجواد لاریجانی
🔸
آیت‌الله میرباقری
🔸
سعیدرضا عاملی
🔸
یدالله جوانی
🔸
حسین شریعتمداری و... را می‌توانید در صفحۀ اختصاصی هر یک از…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/442820" target="_blank">📅 19:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442819">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWcccgqwGCehd_Xa2lUeZzuyNXLyoBSW2I42kqW3ahKmjlLpwNDQzJZgz5MNKTzlXna6UYEmAGjaO0G7w5scBDGr5g0w8hwZFnSNEiT-9t0pGwbctQ_Qa_LAXDrwsIAhr4UxTucVUDD_I6ve2TOQR9VR9DxwoC9KVu0A3_aKyZ4-0FnyyG7kRtRYgallhLyHSq2nwUono06w1Ra1DMDIZmt2UnlUorCUyHx43FCtFaPCS-LdqFvFWCGLBmJ-18-Fv4jfJD54RL9RgdgKw0Ty0HaYh-vvAXQoyIk-G4NvhZMOBc150vwmqOg8eD11YyMtZXLpE0UHhoZ2uBlRPAuvrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور فرانسه: به دنبال جایگزینی برای تنگۀ هرمز هستیم
🔹
در چارچوب نشست گروه ۷ بر آن هستیم که همۀ اقدامات لازم برای کاهش وابستگی‌مان به تنگۀ هرمز را انجام دهیم. این امر به معنای یافتن راه‌های جایگزین و ایجاد زیرساخت‌های جدید است.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/442819" target="_blank">📅 19:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442818">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e61ab4c46.mp4?token=F--btpDDcAgkkBdVs-qkpQEkaJ_DZETFY6pfuo67aenHjvQkeTAmHlhj9fCtS_TTRttc4w_vnSOinnU1DbsXYfkC0EnxvxyUJ4KkH0pqi-Q6DRZBxU1lAeNgDM6g4HD6OAAaaKBpVc7ZuctM6d7UJQw7vDAlYlfNu_qI24BFg-uyRYlDieeZmNLtI34cB2N666ZmtA8zrbJkMLetKte8YBqYP09b5Q9ZQoCkNTYSc9T-ALutZKkP1wg3ONheh_ROmgIt13_gko16iVNH4pQaeye7TmfrX05yMqytDqrd0d2SyD1V9BzT6YI4RJKwU-BcW6Gs9Q28RDXq8VdPoKkRig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e61ab4c46.mp4?token=F--btpDDcAgkkBdVs-qkpQEkaJ_DZETFY6pfuo67aenHjvQkeTAmHlhj9fCtS_TTRttc4w_vnSOinnU1DbsXYfkC0EnxvxyUJ4KkH0pqi-Q6DRZBxU1lAeNgDM6g4HD6OAAaaKBpVc7ZuctM6d7UJQw7vDAlYlfNu_qI24BFg-uyRYlDieeZmNLtI34cB2N666ZmtA8zrbJkMLetKte8YBqYP09b5Q9ZQoCkNTYSc9T-ALutZKkP1wg3ONheh_ROmgIt13_gko16iVNH4pQaeye7TmfrX05yMqytDqrd0d2SyD1V9BzT6YI4RJKwU-BcW6Gs9Q28RDXq8VdPoKkRig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ توپخانه‌ای رژیم صهیونیستی در شهر النبطیه در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/442818" target="_blank">📅 18:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442817">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863bcd819c.mp4?token=tq51289KSAiUNbnm5Nd_q35coBExlTI158xR9kISPMX5jV4r5NSj1Qd1kq9qSu6UNCYvVPYjMfUiB2uSdmuacK5RNCoBmj_F7Dmfl8oY4vu8l4_SA8h59QxnY3Q2xHz2-OidOqR40BmKW2Gw6k8PhYXHhaBM64dvZDRrZ7hGauNurkdatrwl-AYaAAGT4LcXq7L_lN35kUfhZuEB5-8utp_L2l_zWADVEH8Zt01IBN3bcdglv1aYTpAsCKXOG1-GvMdO_cOR6Wy9PRE2NYl_FmjHPbmEXV1GikXqwI0IGaUOH9gBe0pCl6CODSN-1-8PkyBcIRo9u67eMpwlQqNxfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863bcd819c.mp4?token=tq51289KSAiUNbnm5Nd_q35coBExlTI158xR9kISPMX5jV4r5NSj1Qd1kq9qSu6UNCYvVPYjMfUiB2uSdmuacK5RNCoBmj_F7Dmfl8oY4vu8l4_SA8h59QxnY3Q2xHz2-OidOqR40BmKW2Gw6k8PhYXHhaBM64dvZDRrZ7hGauNurkdatrwl-AYaAAGT4LcXq7L_lN35kUfhZuEB5-8utp_L2l_zWADVEH8Zt01IBN3bcdglv1aYTpAsCKXOG1-GvMdO_cOR6Wy9PRE2NYl_FmjHPbmEXV1GikXqwI0IGaUOH9gBe0pCl6CODSN-1-8PkyBcIRo9u67eMpwlQqNxfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دست دادن ترامپ با مکرون سوژه شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/442817" target="_blank">📅 18:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442816">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2559d8c5cb.mp4?token=ufICn1LryupnNEl7ziVa4nF_2EaDBZOhIiGBRmfLY6qO8tVOzKL6c9n6fj9O_y7scE2okqb4Tqrs_6L_PHEVo3sDb2szfM3wwTAd7XDjovUdW3rfKTzIUCL-5VLagtDN8DlaZWTWjqQUvu2phEXbggjWrbiLJQQSOU95SbJXZ09rFUfQ7gdcWbeQ7rcgOOIRIKRyFATaN4yIKDycxYOqIdjFZ0C9KTYDguzhRJYTIhlC_W_iYsyw4UWW-4eFTRFbrHGdd2aQJ6ksl0ZnRTC9P9RstYjb4kj7tltsG8m2b-J6Y6SsFwNI2yUzHlZQP-vSixQjt4mrw2ZY39Dd1brEIHmLGn8qerfgJKU1PkHobGmzqjnDcUZuwvMHm-M4CuZafMrIb-uvHLIA-jFgj7Q7LyY5Mq3EAGBzIVOpaKNwLPCkvd447dZtwdAMzNIkzzqF60FddhYrBLLFUepMM-tQ5nqNtAMyDT53PeEaEjqGaSKG7rtFPTmqn2zODNpeFiiF6Kp8fM-1QYwRgnvEaLF3Y4brbv3fk6uovXNH_2r-dhL-HNrXA-k0dRH23M79o4U3IstX6mVyRm6GkS4hrW1tiwxLgymBhUtK4qreES3QYPU_gN38fHlvEFCGLt0BDJbKQ7-4Cs-PxDnTeYFSULGIV_zEjHnJlPXI68VcrY4mylo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2559d8c5cb.mp4?token=ufICn1LryupnNEl7ziVa4nF_2EaDBZOhIiGBRmfLY6qO8tVOzKL6c9n6fj9O_y7scE2okqb4Tqrs_6L_PHEVo3sDb2szfM3wwTAd7XDjovUdW3rfKTzIUCL-5VLagtDN8DlaZWTWjqQUvu2phEXbggjWrbiLJQQSOU95SbJXZ09rFUfQ7gdcWbeQ7rcgOOIRIKRyFATaN4yIKDycxYOqIdjFZ0C9KTYDguzhRJYTIhlC_W_iYsyw4UWW-4eFTRFbrHGdd2aQJ6ksl0ZnRTC9P9RstYjb4kj7tltsG8m2b-J6Y6SsFwNI2yUzHlZQP-vSixQjt4mrw2ZY39Dd1brEIHmLGn8qerfgJKU1PkHobGmzqjnDcUZuwvMHm-M4CuZafMrIb-uvHLIA-jFgj7Q7LyY5Mq3EAGBzIVOpaKNwLPCkvd447dZtwdAMzNIkzzqF60FddhYrBLLFUepMM-tQ5nqNtAMyDT53PeEaEjqGaSKG7rtFPTmqn2zODNpeFiiF6Kp8fM-1QYwRgnvEaLF3Y4brbv3fk6uovXNH_2r-dhL-HNrXA-k0dRH23M79o4U3IstX6mVyRm6GkS4hrW1tiwxLgymBhUtK4qreES3QYPU_gN38fHlvEFCGLt0BDJbKQ7-4Cs-PxDnTeYFSULGIV_zEjHnJlPXI68VcrY4mylo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیین عزاداری خاص و دیدنی نخل‌گردانی مردم آیسک خراسان‌جنوبی در حسینیه معلی شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/442816" target="_blank">📅 18:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442815">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
منبع آگاه: سفر تیم مذاکره‌کننده به سوئیس تاکنون لغو نشده است
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده در گفت‌وگو با خبرنگار فارس، دربارۀ برخی گمانه‌زنی‌ها پیرامون لغو سفر هیئت مذاکره‌کننده به سوئیس اظهار داشت: تا لحظه تنظیم این خبر، سفر هیئت مذاکره‌کننده به سوئیس لغو نشده است.
🔹
او همچنین درباره روند مذاکرات و اسناد مورد بحث میان طرفین افزود: جزئیات مربوط به امضای یادداشت تفاهم همچنان درحال بحث، بررسی و رایزنی میان طرف‌های ذی‌ربط است و هنوز تصمیم نهایی در این خصوص گرفته نشده است.
🔹
این منبع آگاه تأکید کرد که رایزنی‌ها در سطوح مختلف ادامه دارد و هرگونه تصمیم نهایی دربارۀ امضای یادداشت تفاهم یا برنامه‌های مرتبط، اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/442815" target="_blank">📅 18:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442814">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90912aaa23.mp4?token=Ga2TTBA5KkWqZQ6D0AJJlvYtpVCwxVivCsstqdcXE6ezC2Q2ucKZyQC-0z_1SbpiyU9Fca5bcCLKZy5-R6InKsSQZh3VzPol5EjVcAGs4PJjfuqblF9d-owWdrhhSIX3tGpKaboIrTEZT_RXNP1Z7h-mx197asdH3l2Gd9rJqmXfgXSaXNr87qji_lNxZQvLQo6FtlmPa0FKv7E37bOiQ5Wefa2Q3Sf-n4en2waHkmktsksV5SBhu7IApkQWAaZ9_YLrak04DSQh02sHPo9SDJ93RPQ8U2wFgtXFlnuEEMcBiawLiLwL85iXBa4hsy3Ok6Oq3JR4FYjIP4cwEc03qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90912aaa23.mp4?token=Ga2TTBA5KkWqZQ6D0AJJlvYtpVCwxVivCsstqdcXE6ezC2Q2ucKZyQC-0z_1SbpiyU9Fca5bcCLKZy5-R6InKsSQZh3VzPol5EjVcAGs4PJjfuqblF9d-owWdrhhSIX3tGpKaboIrTEZT_RXNP1Z7h-mx197asdH3l2Gd9rJqmXfgXSaXNr87qji_lNxZQvLQo6FtlmPa0FKv7E37bOiQ5Wefa2Q3Sf-n4en2waHkmktsksV5SBhu7IApkQWAaZ9_YLrak04DSQh02sHPo9SDJ93RPQ8U2wFgtXFlnuEEMcBiawLiLwL85iXBa4hsy3Ok6Oq3JR4FYjIP4cwEc03qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توله‌های گمشده هلیا پیدا شدند
🔹
سازمان محیط‌زیست: هویت دو توله یوزپلنگ هلیا در پناهگاه حیات وحش میاندشت جاجرم به‌صورت قطعی شناسایی و تأیید شد.
🔹
رفتار طبیعی شکار در این دو توله نشان‌دهنده سلامت کامل، دسترسی مناسب به طعمه و امنیت زیستگاه میاندشت است. @Farsna…</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/442814" target="_blank">📅 18:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442813">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b36a0cd3b.mp4?token=WSgOy2Am5SuDLhhn9V1Wsor8D8cVSrKXw8UXyDnyyp9jOshOGHNC_3pUyVkPHwMSb8szbX7e8jHlckDPaRv4kedr5uJv0_p2rd5cTVgQcUvjeAmyPC-oTkmHrXJs-dHZ70ngiKuLcZssVwN1KeF_p5y1BcmZ9mkHH4I0Dpi4Opmy88R-sXDEU00qboXqeVQWKalcDGvyvI34WkTsyT0SYtMT46F63WBtarp37mWtJA9KrXLAU9F2l6h9r-7fg6W7JXdRgeLbdEC_dnXVRmpBfPBNwjXt-AXkp1vmDFOUN-AMhu_rxzzB3xKyyEmB67IWYBqsGtEfmx1BBv-7LesaEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b36a0cd3b.mp4?token=WSgOy2Am5SuDLhhn9V1Wsor8D8cVSrKXw8UXyDnyyp9jOshOGHNC_3pUyVkPHwMSb8szbX7e8jHlckDPaRv4kedr5uJv0_p2rd5cTVgQcUvjeAmyPC-oTkmHrXJs-dHZ70ngiKuLcZssVwN1KeF_p5y1BcmZ9mkHH4I0Dpi4Opmy88R-sXDEU00qboXqeVQWKalcDGvyvI34WkTsyT0SYtMT46F63WBtarp37mWtJA9KrXLAU9F2l6h9r-7fg6W7JXdRgeLbdEC_dnXVRmpBfPBNwjXt-AXkp1vmDFOUN-AMhu_rxzzB3xKyyEmB67IWYBqsGtEfmx1BBv-7LesaEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اروپایی‌ها به این نتیجه رسیده‌اند که حق با من است
🔹
خبرنگار: ما در این اجلاس شاهد برخورد بسیار گرم رهبران اروپایی با شما بودیم. آیا فکر می‌کنید آن‌ها دارند با جهان‌بینی شما همسو می‌شوند؟
🔸
ترامپ: خب، فکر می‌کنم آن‌ها به این نتیجه رسیده‌اند که حق با…</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/442813" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442812">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f0c784c6.mp4?token=YqyeO-jWN1OArDlUot9Cvfqvd2tau-rUX0gIp8BVhWfY6G1ZLf-0LrlhqCNK-_96LGjqMciqgDg15d8K9kmZHJU4lqWa9yB1Lhnv8Qha8a2AJ6oX-ZIFqNhP8T_mwbuKCt-Xswi_ZnbINq4NobhJsm9UNR_9i_Vown7gFI874W0f9rIhyEKfLGg5IgT7qzwr_NlodEIEpI0Ci62mcoRgS6gCU54m7eJOlqHN4jx3Jp1Ze8tchI6ln0TYuuVRUtYSmP5ctGwW8ytMD87977n-w-knTVKaGH-jrWRPTM9pLfl4wIkUV16aBGhNZOZm0Gdluqn5Np_yELmPirycp0QSmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f0c784c6.mp4?token=YqyeO-jWN1OArDlUot9Cvfqvd2tau-rUX0gIp8BVhWfY6G1ZLf-0LrlhqCNK-_96LGjqMciqgDg15d8K9kmZHJU4lqWa9yB1Lhnv8Qha8a2AJ6oX-ZIFqNhP8T_mwbuKCt-Xswi_ZnbINq4NobhJsm9UNR_9i_Vown7gFI874W0f9rIhyEKfLGg5IgT7qzwr_NlodEIEpI0Ci62mcoRgS6gCU54m7eJOlqHN4jx3Jp1Ze8tchI6ln0TYuuVRUtYSmP5ctGwW8ytMD87977n-w-knTVKaGH-jrWRPTM9pLfl4wIkUV16aBGhNZOZm0Gdluqn5Np_yELmPirycp0QSmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: آدم هیچ‌وقت نمی‌داند توافق‌ها چه می‌شود
🔹
ترامپ در دیدار با نخست‌وزیر هند نارندرا مودی درباره امضای یادداشت تفاهم با ایران در روز جمعه گفت: آدم هیچ‌وقت نمی‌داند توافق‌ها چه می‌شود، اما خیلی زود خواهیم می‌فهمید. فکر می‌کنم انجام شود.
🔹
آن‌ها می‌خواهند…</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/442812" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442811">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2MT3FmC-CraToPBYKsY9AZ8EUqwHbsEO51sfTem-uOq6xIAB9aVQsjgx3-NmjMUzR3x3dcVLvsJ0OP6QHB1dNxTG5jZjaBm3nzztpgSCAGe2fhyL-c8GB2behGrCdXzmvIAWv6Eo9t4hG1OMhAxnsEl1Tho4zq6WhCRde6anK8_NCU8aPNpU9adVV-N4aRMXRYybe6nKnkpq_VoZfC7qu62HVOm4msHbEKiwKuODjIGchbtZoih5v8IFTV9DM-hast5Z7zT8HuAkDtDeB_yMeEaob55Vt_qY_d3ElQtPb-Jm7VV8T3VTvc9XkL7XvgtmcOobaVB11PHVEJ3EIwTlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جراحت ۵ نظامی صهیونیست در ضربات حزب‌الله
🔹
سخنگوی ارتش رژیم صهیونیستی از جراحت ۵ نظامی این رژیم در حملات پهپادی حزب‌الله در جنوب لبنان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/442811" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442810">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f35d9ebf38.mp4?token=F8F82JEHYiTm4EeL8z6icwngbpNd2WbM-_dPTTDwPEF_JFMj092Gz-mb0PYvG-Imv91VNWZ64hOlmVfJxWTm6m_EmPb4up7LM7k6Ra3o2cZnELAQsK-2JfiluiguTV9wo5f-5G0pQt1qYkIE55QxGKjyaplBfotG0EN55vBlW_yLiQAmrtEALxL-BsK1AgUWpD72OYOC2_ScsfpVPthS-K07vTAfi9K3nzjWojlf3Z1XoFkAftSRbXlc626Uq-Y4FBxT9O6fHLEUQ8f_gSvr1pMkdjZs7afZXJnWJ5CsMRQtYuBhtKACzBnQdsG9MxlmOOyh_SGcxwAnmiFLgwiVxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f35d9ebf38.mp4?token=F8F82JEHYiTm4EeL8z6icwngbpNd2WbM-_dPTTDwPEF_JFMj092Gz-mb0PYvG-Imv91VNWZ64hOlmVfJxWTm6m_EmPb4up7LM7k6Ra3o2cZnELAQsK-2JfiluiguTV9wo5f-5G0pQt1qYkIE55QxGKjyaplBfotG0EN55vBlW_yLiQAmrtEALxL-BsK1AgUWpD72OYOC2_ScsfpVPthS-K07vTAfi9K3nzjWojlf3Z1XoFkAftSRbXlc626Uq-Y4FBxT9O6fHLEUQ8f_gSvr1pMkdjZs7afZXJnWJ5CsMRQtYuBhtKACzBnQdsG9MxlmOOyh_SGcxwAnmiFLgwiVxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: آدم هیچ‌وقت نمی‌داند توافق‌ها چه می‌شود
🔹
ترامپ در دیدار با نخست‌وزیر هند نارندرا مودی درباره امضای یادداشت تفاهم با ایران در روز جمعه گفت: آدم هیچ‌وقت نمی‌داند توافق‌ها چه می‌شود، اما خیلی زود خواهیم می‌فهمید. فکر می‌کنم انجام شود.
🔹
آن‌ها می‌خواهند…</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/442810" target="_blank">📅 18:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442808">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16837806b6.mp4?token=JS7O2CMbHvlub8jkjf6B3JR3ZYCXskEDV3VG-AfyxAE7IS3Hj-UDweBEf0kcL2W9g14ymQl022v4ydIsFbvZKh96cYp4Q_SmcAXCi7FR0vhI17DlRGHo6kHuCCvk_Ey10f7-T8IsVJqbazhxWafjicUsJTtVEi0JOAMILFYTi65k8nYy8IGUEal19wK0GxLwOmA2khh14Oh9el8ly3kL-UaQz9o1itY4qNALp8-e5Gj8pnEIV_QzBb-GBRppg98tX7OlNBxk8wtvl8-kwt-Jes9880V9miOI13Bizee-C1jvtOeBYTfvGhSF3fHUFNK01ZXboQTEX_8ZEI1xaP-hqUOCPxgF5ti1btAixyOiQnpBcgw15E2jdWrMo4GaoWND7BSAwQ0CsZoMRuk9SvK4oxSLofQUyXl_f1lLnH-aEbDSQkKixN1eRSwckbnXz0C3fI43VRhKEXkPqiQtolmJcMDilPripvMhA9exOH3-xugPFhno7mmzwH3rZlEMfD8mV8SQCwqEhsBBd4OJbYIVb2LE3JfakXtZSkugIQ9hZtAjZrdO5dBwi3cpHgeAxJKpr6FKSf796JffUlobb2tB0JAtYFUNUWyqtYssqcWLL4s7B6_5pTJQkw_c9HAbgI1WzhrLn6hAqEVubJM7BOVdAv51ZkcdJO690izWgDG1Mw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16837806b6.mp4?token=JS7O2CMbHvlub8jkjf6B3JR3ZYCXskEDV3VG-AfyxAE7IS3Hj-UDweBEf0kcL2W9g14ymQl022v4ydIsFbvZKh96cYp4Q_SmcAXCi7FR0vhI17DlRGHo6kHuCCvk_Ey10f7-T8IsVJqbazhxWafjicUsJTtVEi0JOAMILFYTi65k8nYy8IGUEal19wK0GxLwOmA2khh14Oh9el8ly3kL-UaQz9o1itY4qNALp8-e5Gj8pnEIV_QzBb-GBRppg98tX7OlNBxk8wtvl8-kwt-Jes9880V9miOI13Bizee-C1jvtOeBYTfvGhSF3fHUFNK01ZXboQTEX_8ZEI1xaP-hqUOCPxgF5ti1btAixyOiQnpBcgw15E2jdWrMo4GaoWND7BSAwQ0CsZoMRuk9SvK4oxSLofQUyXl_f1lLnH-aEbDSQkKixN1eRSwckbnXz0C3fI43VRhKEXkPqiQtolmJcMDilPripvMhA9exOH3-xugPFhno7mmzwH3rZlEMfD8mV8SQCwqEhsBBd4OJbYIVb2LE3JfakXtZSkugIQ9hZtAjZrdO5dBwi3cpHgeAxJKpr6FKSf796JffUlobb2tB0JAtYFUNUWyqtYssqcWLL4s7B6_5pTJQkw_c9HAbgI1WzhrLn6hAqEVubJM7BOVdAv51ZkcdJO690izWgDG1Mw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: آدم هیچ‌وقت نمی‌داند توافق‌ها چه می‌شود
🔹
ترامپ در دیدار با نخست‌وزیر هند نارندرا مودی درباره امضای یادداشت تفاهم با ایران در روز جمعه گفت: آدم هیچ‌وقت نمی‌داند توافق‌ها چه می‌شود، اما خیلی زود خواهیم می‌فهمید. فکر می‌کنم انجام شود.
🔹
آن‌ها می‌خواهند امضا کنند، می‌خواهند به زندگی عادی برگردند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/442808" target="_blank">📅 18:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442804">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97253ade57.mp4?token=i2TvY8jUeHPL3_FfA-gnge7HdzzZMf4uY5LiJGEvnyOSA39Pss3UlPvGh5EdF6-eZQC7ivBWinhOQHIxIdBiGgz8uiT9mfi4dmyiQRHh8YCXXjHU48sZkNAdjdablq8O7rGAbhe1cTsF8qRh64cRGfTE2v3EVUWb8HZojq2h6kvCsunggykx3mxhVO3T0cc6u6RcHJhE2gMec_R0zVv-Rgh4DZe78cpxcsprsSmC9T2cI0HsCf495YqAfQlFd_28nNJ9EUNSVijhqOp_r4GBrAqD7QvxW_vHR7Z2myG5JSyZsrkO7Gj6HM0-KEZx_62sbtF4K9k3ORkd7tPaYicBCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97253ade57.mp4?token=i2TvY8jUeHPL3_FfA-gnge7HdzzZMf4uY5LiJGEvnyOSA39Pss3UlPvGh5EdF6-eZQC7ivBWinhOQHIxIdBiGgz8uiT9mfi4dmyiQRHh8YCXXjHU48sZkNAdjdablq8O7rGAbhe1cTsF8qRh64cRGfTE2v3EVUWb8HZojq2h6kvCsunggykx3mxhVO3T0cc6u6RcHJhE2gMec_R0zVv-Rgh4DZe78cpxcsprsSmC9T2cI0HsCf495YqAfQlFd_28nNJ9EUNSVijhqOp_r4GBrAqD7QvxW_vHR7Z2myG5JSyZsrkO7Gj6HM0-KEZx_62sbtF4K9k3ORkd7tPaYicBCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان و باران شدید در مشهد  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/442804" target="_blank">📅 17:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442803">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e04f904f47.mp4?token=ILscbkNL7R8lQyorWInaT20fcUUa-CapeIxlXjbq5CnCXUaiHyGvugYa-77lucT52h494R2nb_1rdmr6VMUHFTavX2GTplqbyuhFkPy45nxZGsCzg_AvOBQ_RA7KoGD0ihpWek5P3_oVqM5oBJ6YAPisT8CPCNQI1teS2EKjRu5AfaVNKUCebB9l1M5afXnUeUWooxlvNAFdGNL-sRapeWqVoTPNti1MrpdzHPLYMAaskrLB4-tU4LHecr9pW7YvbWolFz3vQ9dKWuJiih6wFcdlAwXCedFZaiE2a4FXCpJT2s2O0ElxFrqfOiEEaDWduRNQ7gxNbRzUAeaJoSM6BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e04f904f47.mp4?token=ILscbkNL7R8lQyorWInaT20fcUUa-CapeIxlXjbq5CnCXUaiHyGvugYa-77lucT52h494R2nb_1rdmr6VMUHFTavX2GTplqbyuhFkPy45nxZGsCzg_AvOBQ_RA7KoGD0ihpWek5P3_oVqM5oBJ6YAPisT8CPCNQI1teS2EKjRu5AfaVNKUCebB9l1M5afXnUeUWooxlvNAFdGNL-sRapeWqVoTPNti1MrpdzHPLYMAaskrLB4-tU4LHecr9pW7YvbWolFz3vQ9dKWuJiih6wFcdlAwXCedFZaiE2a4FXCpJT2s2O0ElxFrqfOiEEaDWduRNQ7gxNbRzUAeaJoSM6BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان و باران شدید در مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/442803" target="_blank">📅 17:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442802">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAHA-8pA_ZHrGbQDeGUY3s5az9yRtdgavUn-Lj1n-n8FnbcKjd0fXNre60MFlLZHmBgKvuYI12NvQZYjwPDDhu5X3lQoXDaItGAJubdzt7wXjxrSotudX-WUZ5S8zXMATqUWxHZJ_AyEcMgm0j_WtGnCsxq68zHz28y7JRFhFJIvHSZtAeSOhKiN_-roh8VR9FYoo_BvPKLGeX2hT6VAIBQxHOOLRxMenmlP0JNEOKgVICKJztLyYYB1HFTBr5ruglYt5hP6VxEocEZ06qsoMuDBaxaYgxxyw690WHv8sLmwy32gegNFe8seAgnPj4wi4VA2uRYyKCab7MZPESi0BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاسوسی پهپادی از تمرین کره
🔹
رسانه‌های کره جنوبی اعلام کردند، تمرین خصوصی تیم ملی کره جنوبی پیش از دیدار حساس مقابل مکزیک در جام جهانی با ورود یک پهپاد ناشناس به حریم هوایی محل تمرین مختل شد.
🔹
طبق اعلام فدراسیون کره جنوبی در زمان مشاهده پهپاد، بازیکنان تنها مشغول انجام حرکات گرم کردن بودند و هنوز تمرینات تاکتیکی آغاز نشده بود. به همین دلیل هیچ‌یک از برنامه‌های فنی تیم فاش نشد.
🔹
پس از شناسایی این پهپاد توسط نیروهای امنیتی، موضوع به نظامیان مکزیکی مستقر در محل اطلاع داده شد. آن‌ها با استفاده از تجهیزات، کنترل پهپاد را مختل کرده و آن را سرنگون کردند.
🔹
بااین‌حال، زمانی که مأموران امنیتی، پلیس محلی و نیروهای ارتش برای ضبط پهپاد به محل سقوط رسیدند، دو مرد ناشناس که مظنون به هدایت آن بودند، دستگاه را برداشته و از صحنه گریختند.
@sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/442802" target="_blank">📅 17:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442801">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f04cc8635.mp4?token=J6UQ6Idyh9V1JKJdLPQZP66TuKAhFes8z09E-6pYFCWXKk_zx-05OHPsS4diFC-Tsh40MQq0cf5Dxl_v9gNGBa73g9rIQbmiq87NwQqvdpECElZS1myxbzOWv8jikYydd4wNM00LhoxXP_6wU-USqhbeF6B_qMozWHzB6MbRJo-otKUo6e6Ux2F9PzkrDsbdIZL8262Vtk-8PWYojVZCPgWC0twmNlgZ2t2zRDooMEuB4eHd5G72744M00PHOpB6qsM4yaD-T__cGc_M-0_uojnbKAKBTOYKPzoCU2zv_IXb6AsqZYWNk9ayhr8956GPMxhR9edyCCsOecoyoBc5IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f04cc8635.mp4?token=J6UQ6Idyh9V1JKJdLPQZP66TuKAhFes8z09E-6pYFCWXKk_zx-05OHPsS4diFC-Tsh40MQq0cf5Dxl_v9gNGBa73g9rIQbmiq87NwQqvdpECElZS1myxbzOWv8jikYydd4wNM00LhoxXP_6wU-USqhbeF6B_qMozWHzB6MbRJo-otKUo6e6Ux2F9PzkrDsbdIZL8262Vtk-8PWYojVZCPgWC0twmNlgZ2t2zRDooMEuB4eHd5G72744M00PHOpB6qsM4yaD-T__cGc_M-0_uojnbKAKBTOYKPzoCU2zv_IXb6AsqZYWNk9ayhr8956GPMxhR9edyCCsOecoyoBc5IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از سرکوب شیعیان بحرین؛ از بازداشت تا محدودکردن عزاداری
🔹
رئیس جریان الوفاء اسلامی بحرین: حکومت بحرین با بازداشت صدها نفر به اتهام همدردی با ایران، صدور احکام سنگین قضایی، سلب تابعیت، محدودسازی مراسم عاشورا و اعمال فضای شدید امنیتی، موج تازه‌ای از سرکوب را در این کشور به راه انداخته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/442801" target="_blank">📅 17:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442800">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syMo3mjzsHWIy7xfRmkNjKZm5vNXMO7_qhM0xgJFfTZyIcS56TNJRIu4pv5YYgGDBJMpVnZJOVFjSAUus3UsrXppTAjv-gBBtFzKTYDWjKGe8QdsL4bgukn6gIyBhypE9STzhle5pW2O6K92N6bwAQmzYMu_H1FDWDQ_H3ZFLqLWDNfP5xjsTWRds6lpM26ibMv_Nm02Dcq_0rmDnWL8gY05Sv0OH_Np4bPrlXz_K4POJoA_M2g_zHx4IpGsxfHv7Cnaokn2sw9yz7hXpZzlSVmyQEtoxOwhimzP4KLyxfxcGo3akyQmu33p3I3nQLX14CESkx-EApRpPcAqCmO5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قیمت جدید محصولات ایران‌خودرو اعلام شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/442800" target="_blank">📅 17:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442799">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184068c2d7.mp4?token=pVDwbLXWJTk_NDGd21NVNZ3NLp66OoMX-wENh-PQwlqvJPb_wXkAk66CqUMQAMuC8bpimRiJwU9KwRlBdv5It8nNvvadgaxNXWcUV181sOb5I53BzjWJLLtBOLdMi323vTafpbgnvZKY9_sJQM9Arj1Q8fGcJuYpYyjTEZOwwRZb-6dJf5qLvPZiaWb3xdsx4Jz90o666riwc1j7gbHiY7jCD80Z_-PMASP-JtO4YvHJlPLuNRZ28j1WAgcUpYNXOnwHw3taaj9kLvYHE4yKZQkr9Ew5jSI-hTMHJ8pX3Q1Dye9WC0W7tg29IolTpGzpydsQljsspP7KbK2SheSS2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184068c2d7.mp4?token=pVDwbLXWJTk_NDGd21NVNZ3NLp66OoMX-wENh-PQwlqvJPb_wXkAk66CqUMQAMuC8bpimRiJwU9KwRlBdv5It8nNvvadgaxNXWcUV181sOb5I53BzjWJLLtBOLdMi323vTafpbgnvZKY9_sJQM9Arj1Q8fGcJuYpYyjTEZOwwRZb-6dJf5qLvPZiaWb3xdsx4Jz90o666riwc1j7gbHiY7jCD80Z_-PMASP-JtO4YvHJlPLuNRZ28j1WAgcUpYNXOnwHw3taaj9kLvYHE4yKZQkr9Ew5jSI-hTMHJ8pX3Q1Dye9WC0W7tg29IolTpGzpydsQljsspP7KbK2SheSS2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش‌ سیل‌آسای باران و تگرگ در نیشابور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/442799" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442798">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5KqQQuL7LaEnc_GPjaKmdVbbsiESftIirCPa8Gt-UQwUAEME_CCPWCjq_tMnVSuIz3cxYQkCHeIvLZBpCeI_NM8I4wk5hjchVFlIUDwU2Yfs9MHhEYMMKveqH1kqTnd3gfYLb-u4RG-7dbAZh0ZU2-sZZ4Kdj1ZTyyQ40XaHumPX6V3wnFSaEmYyuLjAGmjeIpqj36q5F0RKcufpgR392e3m6PeDqYS3y9unnE1-HrBn1ilOVa6JXDUXNQsMTg62e9Fzh67coayugyHpjyj7ZOMwRiFcNoQ9IwkgCom3QoPchUIRIv241tvD7y1IN-j2-UhEUS0g3WEU2bNOcLwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنوشت قطارهای پرسرعت ایران و چین در ۲۰ سال
🔹
چین با ۴۰٬۴۹۳ کیلومتر راه‌آهن پرسرعت، بزرگ‌ترین شبکهٔ ریلی سریع‌السیر جهان را در اختیار دارد؛ رقمی که از مجموع خطوط پرسرعت بسیاری از کشورهای دیگر بیشتر است.
🔹
توسعهٔ این شبکه از اواخر دههٔ ۲۰۰۰ آغاز شد و شهرهای مهم چین را به یکدیگر متصل کرد و تحول بزرگی در حمل‌ونقل داخلی این کشور به‌وجود آورد.
🔹
در همان دوره، پروژهٔ راه‌آهن سریع‌السیر تهران–قم–اصفهان در ایران آغاز شد، اما پس از حدود دو دهه هنوز به بهره‌برداری کامل نرسیده و بخش‌هایی از آن تکمیل نشده است.
🔹
در اروپا، اسپانیا با حدود ۳٬۹۹۳ کیلومتر خط پرسرعت، پس از چین در رتبه دوم قرار دارد. فرانسه با ۲٬۷۳۵ کیلومتر، آلمان با ۱٬۶۳۱ کیلومتر و ترکیه با ۱٬۲۳۲ کیلومتر در رده‌های بعدی هستند.
🔹
فناوری قطارهای پرسرعت عمدتا در آسیا و اروپا توسعه یافته است. در آفریقا فقط مراکش شبکهٔ محدودی دارد و در قارهٔ آمریکا نیز توسعهٔ این خطوط محدود بوده است.
🔹
آمریکا با حدود ۷۳۵ کیلومتر خط پرسرعت، جایگاه پایین‌تری دارد و برخی پروژه‌های مهم آن، مانند پروژهٔ کالیفرنیا، هنوز به پایان نرسیده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442798" target="_blank">📅 16:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442797">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNeBubtJ9sSoxGfqMw05KX7mxuSG-d8F6hJrZlQyyipMcq1AP6fB9ZPgCWeSV_CKoSl_hYcxtVo97snA-KB6AcwnfWasTok46vK6eol74rqq2EMxN2EllOM69ZM2zvTdarjeaKyTqdVm2PAm8JI9XbVK2WBm1r3n41p0HLMyn3s2CRuXSDA0TyAjdiJOzgM6MR12TEjHz9D5zYqP_L9kRs-eRbN_9-db36wAfKoD0BM5w7U5xyLeTD49xnRzlglKJo6BRT-6QWVllKLH6iyXKiUuVL2WtecyHFrW917NJo1E0jKU03zeKR5GBvhIO-pLVto-t58v5LrJMl_b6K4n2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنوشت ۲ بچه یوز ایرانی چه شد
🔹
در آخرین پایش از یوزپلنگ مادهٔ «هلیا» در پناهگاه حیات‌وحش میاندشت خراسان‌شمالی، ۲ توله از این خانواده مشاهده نشده‌اند؛ موضوعی که نگرانی‌هایی دربارهٔ سرنوشت آن‌ها ایجاد کرده است.
🔹
نظامی، مدیر ملی پروژه حفاظت از یوز آسیایی، به…</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/442797" target="_blank">📅 16:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442796">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1916ddc8ec.mp4?token=Lmko6014oQSyVyjUX_n1X51GcuvcN1yNYXnl984LYjJ20bC8UIQI4yOermvYPBRHK07UA7n-NoTYMszrk5YWI7k4qVvEAHrGuhYxsFQTqIBQQCUQ9vMlHu0aByprQYZCrVsXjZPqUQs9K81hYbBwW2jjZT_49cjTWfkl5Yxf76f5yMgUHQmbHiTPxap3nVmtxcCYdtO-oPvBOq74y4WKU85eUgImJI3wbin2tmAHbgJqRY8GzoUSBnQmf__Ve0B1YP6qwpFS7J6rdeHgllXuZZCmemsdf8W6sTc4Y_IFza1fgMql3kn72UwmRGgH9lmFSKyEmlHqNN6eyrg_0zGc2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1916ddc8ec.mp4?token=Lmko6014oQSyVyjUX_n1X51GcuvcN1yNYXnl984LYjJ20bC8UIQI4yOermvYPBRHK07UA7n-NoTYMszrk5YWI7k4qVvEAHrGuhYxsFQTqIBQQCUQ9vMlHu0aByprQYZCrVsXjZPqUQs9K81hYbBwW2jjZT_49cjTWfkl5Yxf76f5yMgUHQmbHiTPxap3nVmtxcCYdtO-oPvBOq74y4WKU85eUgImJI3wbin2tmAHbgJqRY8GzoUSBnQmf__Ve0B1YP6qwpFS7J6rdeHgllXuZZCmemsdf8W6sTc4Y_IFza1fgMql3kn72UwmRGgH9lmFSKyEmlHqNN6eyrg_0zGc2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ خطاب به اعضای گروه هفت: من رئیسم
🔹
رئیس‌جمهور آمریکا که برای شرکت در نشست گروه هفت در فرانسه حضور دارد، به هنگام شرکت در یکی از این جلسات، رو به مقامات ارشد سایر کشورها گفت: من رئیس هستم.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/442796" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442795">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buNXaNKOwwCiig_BMh3tWea78l9bOIvZ1DeIDSCZqupp6X8-rXJHOn0R-0osSalYpp7WVsFLVWNyDIAzYPcr4XYEJ9rh19Ne3nKrLn3NR6o4mr9lKEzKNweuc0U4ITRxzzy6N7Q-hbPS689zYCUpsUiMNeUHWf7XxKoKbnCj6Tb1w2eOOP51bvcPJj48O9k4wW83F9-4ovIEykdwVdgko1dkEWglv_FDj4xBQ8ypoa5KSCVYm2UfYb8Ene69oIB4s9aivwrNNbH_3z6mmgEujLWfEOoAh81uSIJ3qZfDATdYi98_Ka10LHkLLrPhAZBuex-vPwr_Cnwd4TUHfeeYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور بازداشت خانگی ترامپ برزیلی
🔹
دیوان عالی برزیل دستور بازداشت خانگی دوست نزدیک رئیس‌جمهور آمریکا، ژائیر بولسونارو را صادر کرد.
🔹
بولسونارو متهم به دست‌داشتن در کودتای نافرجام بر سر انتخابات ۲۰۲۲ است.
🔹
همچنین دوباره قاضی پرونده بولسونارو را به استفاده…</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/442795" target="_blank">📅 16:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442788">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItFN6BxDrZR8tbyZK5t62ygNfodpyKc038O_N11Pqk4iEQti891pW0WpgqmndY2rQ3nec9yIn6oo_AVgN6L9C45gnlWOF3SVPmzXFPFor4SaUPJ8bm634VvSwJYIQt2VxPvCAclLG-xHVDALFnErRklqzOovgnf6kqttxDsnUy1ogq9LB-MLKgEi4ap0U1S0UI4toe2vv4boaAiJJVEwRJCPNJVU13tKlC0I96z8RP5TJZHn5kY100sJeuMZ_-z9FncviymYpJ74WwhxbWDT_qlhIWhL8E0CVkwTtcaL6KRXyzyMOHi8FsvUXRCm0717CO2itHFtiyLYUQU4bxqU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOdxUG5loOr7WlivXC-mBMaqPCEB4433mryfo624iE6Qwai_bYE99bVY1vfWkWx7qkWKSI1TayKn3HdL-laIOwr6v562gLpYYWb3AvZIlv2k4XGdfo0u0KOKJ0_KzzyReJA9aMnM7k9clhe1gwa8Dj4JVc_xrTbzSKlQT-3XKyZz4XZp638sJ9kfQYD4netEZZ9AzdvUjQY6KcF3RxAQCGuqo9YZox4i0gai5b9EBu2KGDL5rgrluxAlBEBkf2e6FpY2zouirg4X6L3bJskPlw3F4XLFIo35X51XsiM5XlRHPretjEByw4enwshRwHs-NVvf8e0UWn79z3RNugb7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxyZ9MRPrF5EMNVXeFGJImNa_DAX5N4GcdNnMP0h5632z4tPqwaZEqE03WyQMVoo28SYbvRmJue7H6DFcGSuBScBYFDOeL5Zyw3673vvb78WMRGD1w6DoriQoTFvWzUtp1I2avYipSR0-BEq49RNQ4-cbWGXfbZSYrQS1XqZlAYMIv371DhR5TY14HCjHpFGCsXjfezYtZ92dDsj7ZmC3I0ZSvhBBLFoydNdA34xPp9diKRSCvRDu5iS5bfBEewR-dJjQeHVOLj8R_M2RiAtfEKG5BshDpPgXcvaynDCSXGCAGguvEwzFW_5mzVGkK_2EOqbRFhMR_ODFlwVx2jOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HG7OPNlKHEuhmMKB_dLmoHW2LcO-eqR3dxHLN9iqmHaIZwszuIPMyk3h8MFRpeXNWl58cwhV9Do8k6OlI_UnBzBeDPZU2GDaHsmYLMSiYFcZnPsdz000dFQhDdKHa87HA3pjuiVyUNSiryOyBvTpfMIrHGYDU6CKsn4foaWAwPR9VPdDXS2xDNH-CIPmDwi6OBJmq3WV3ET8BPHtErT6l3I8HTGkA0ywmUFr8QHL41BK0obZawwi2A1SjWJcGwsCYPNHZaXv1iNQOrVrvAdAgmEt1UxpY0fE9-GecHnx0NUGyzxXY_bo9IIUPsU0p1KzUKeD4BqHjrwoIlfgVip4uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-1EbEyCNrmbkb4RmphtoXWoaHJmecwgKkriB-kpBUoZ3mYSWyPugUEDqPYMbICFcsOE0k-sOPppQUwnn-bGisUxzuHvm6PJzp02jqnN0dkcI9kGjalQSNXvTh72BplQuUyK2pul8u-PMz8oJwSykyKWSVRxdYA3oJcidneXj_eUwxQeIKgeci9r0f6LfSVPSLr3c9Sc2gwnhDoXFNQj8Sst3OHS3RE18KFyoAyhfM35xiQ_KFcvypBS1xfoST9K_32QBealZFVOOshLtzje2-17kaD7jjZFAHDVRBtdKXq8C2l9ajQFUzyMe_uw0gXXfT3Q9a1mHfHJYikurXEdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4pJD-J3U2oM2ZWqoRIsV8a8AIMbU4PoxTWKa90Hy7h6sb5DHM6dXXT3bOqoUn2sR1xwar8E9j6hhr4NH9K7mC3rLrzFXhZiNxEfRd4VkAl7dBanUXhQc8FnrADz_MqRwgz9_q7MLQo2M34mlLmMDCRT2WMx1iJdYsAMV11ikHer1-ic9zFvm8QZnzRt9ilMQ5mKvsOtS8vayfA13E3uAXZ5vPAbx1lMOuTvwPdEenhx4d_Ca0bigsEcskUHTSul0_T4eYcY3EXKYliodNXW_b9ZqRbyuCAwNV7xHKIrHvEp1OxoHqdQSpyIviy2I9apzhjXRJmIKmUcnt7OQxEPkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aO5v5OWN_fbJGMF37Z09JnxrGZypRchwgFMbpDmqEkrp3EJ1TjL6kLxylTS3uEWiIPxNtR00-o1efn1Vq013uLmksraW2qiOD7Ru22t2jmmR5i4X-eXdGwFzWyrCI4U_vNEaFd5PhrMD4-4pPXXnWMNjo7z_CMS7tx3OOQEouJs8HkXEsjvPtqD9W-_lo-g_YbONllhtgAsqn9-DDy2-Qrzi2wUcVN8_k0XBV7Ys69Gh5RF2iVSl2wjdOZEWggMGIus8R_HlMdSmfhwEHIKSZmZWzqUQOH97JvtgLruPbfjnKhwhGioqDAyf04bNCqc4AEj-BbU2nWnVIOYjWE280A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کارگاه دوخت لباس شیرخوارگان حسینی در حرم امام رضا(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/442788" target="_blank">📅 16:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442787">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrOOpupEyQWNqEGXfyOzS2bDT2a_VkIY3Oy83bGE77rRXuBNEH59nA3vcj6mKdKXf24Te-wHJzT-UfwGMCr6QdOQrp5I99z4mPB1kU20og7hkMk9Wh7LKOtOTo1QqhEduBtFMhqvrJS3FqhbUC1jCFv32trb5PW7dembYi4mvRzQXsA8e34ROaW4sYAqAl7wC0TFZy-l5YPJrZJN0FC_PMHN0QMiU1X9N0vXU7dP5sDz9rtANg0bzDUCxEoNdZzbCOLnmbpcLJjHCal7lCK_p9WuAnoAdOX1bu1Y04Cm1zI5kpSiNAi65wkQ8Eg2alJ4-_BxdDpJOR2NrEURUVYLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۴۸۹ ماينر غيرمجاز در خوزستان
🔹
فرماندهی انتظامی خوزستان: در بازرسی تعدادی از کارگاه‌های متخلف توسط پليس امنيت اقتصادی تعداد ۴۸۹ دستگاه استخراج غیرمجاز رمز ارز کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/442787" target="_blank">📅 16:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442786">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cf13e6f9a.mp4?token=PKXG_wOaPO218Ya3CzOZQj3kneiNm7FKbjWZA5gl9SEREMCS5cxr_sTJDdBtZKyGkU8EKSYyFi_vx4ES5q-dtzP-UFSK1bRozxDP-4xiJJKRtasj59EjyGggBrJbqx3cFjEHcayoTQA-0X_cLbt8XPhuUeyTbOQ3gJDGNN-gX6YSyRTQRn6Gq-FCPBIIzSCokqr7H3XTU4LKBZKNdlrjuq-XxUX8aIlRsRKUVCcl1HkQgZsI9hoTiOoxeQFpYVLP4Why_17M4xdQBfRGCjFTIdM8-6jVv325ZlAcCctDh6LF8pUobTnSKtR2W8sKUY1Ww28X0A_JruxjapL6RY3CrgM4yat_6RJy7oFSLEuqauVUgpcl3oGiaPdLu3D217Z7801uOziVN5lmyaskSbUFG_ty2ROHvrdEQdmSF6tu2-m-_1hzhkYbkdNLKB8oMAV1g2Gm26Zl0-qa-hz-0CLeB0IAGc-VmYF2GaWajQbXD8xmEsm9o9_pyNOiCqk5KeG__PWXoyHQqObMs_CVSPisonwe1Fj_r5DClxlkPiQoM9V5Ken16u6JWcWuCLHwm9YUGtaOjzK1usjWP_D46mHwP-LeLZaNi30XOZGE8Yk26kpiLGOqTa-C4lPQ3Vzn-VDjzcbNvfUat7Gxcveyfkc5PiVHPY0gJsJ9P4jBDs49yD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cf13e6f9a.mp4?token=PKXG_wOaPO218Ya3CzOZQj3kneiNm7FKbjWZA5gl9SEREMCS5cxr_sTJDdBtZKyGkU8EKSYyFi_vx4ES5q-dtzP-UFSK1bRozxDP-4xiJJKRtasj59EjyGggBrJbqx3cFjEHcayoTQA-0X_cLbt8XPhuUeyTbOQ3gJDGNN-gX6YSyRTQRn6Gq-FCPBIIzSCokqr7H3XTU4LKBZKNdlrjuq-XxUX8aIlRsRKUVCcl1HkQgZsI9hoTiOoxeQFpYVLP4Why_17M4xdQBfRGCjFTIdM8-6jVv325ZlAcCctDh6LF8pUobTnSKtR2W8sKUY1Ww28X0A_JruxjapL6RY3CrgM4yat_6RJy7oFSLEuqauVUgpcl3oGiaPdLu3D217Z7801uOziVN5lmyaskSbUFG_ty2ROHvrdEQdmSF6tu2-m-_1hzhkYbkdNLKB8oMAV1g2Gm26Zl0-qa-hz-0CLeB0IAGc-VmYF2GaWajQbXD8xmEsm9o9_pyNOiCqk5KeG__PWXoyHQqObMs_CVSPisonwe1Fj_r5DClxlkPiQoM9V5Ken16u6JWcWuCLHwm9YUGtaOjzK1usjWP_D46mHwP-LeLZaNi30XOZGE8Yk26kpiLGOqTa-C4lPQ3Vzn-VDjzcbNvfUat7Gxcveyfkc5PiVHPY0gJsJ9P4jBDs49yD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداح بحرینی مهمان هیئت محمود کریمی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/442786" target="_blank">📅 15:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442785">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a22235fe5.mp4?token=Y7uXPts-OJRmQvPwRBVTrSqCMFovO9XhtWx83ecxHCb-c8Wd-wDvWu4VJkqvJXJ14iAWU7mQUmMeUT16zgBE9TKpC2ZPNzYCSCHPJq7BfPXcS3wKbKNYHNklCjDOiBE5DVuI7tuCergiVTiD2EjlpVbFPgDbB5ew7sUtI5wyNaAYE4jTo1mYSI4kRciRDDI7q0m-3oZ9gjA9_5XEZbh5wLY2pmr2W2wX59dUhmO5_jojhzXkPuzl9IkMrwYxs1LxzZNTQ77HEx0i-3nKYuuxCDxGmgLU7FGWlz1v-00rz24UcUJua_aS2mhgKLnF6sj6R6dAFySKiCT5sIAYhs5Dyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a22235fe5.mp4?token=Y7uXPts-OJRmQvPwRBVTrSqCMFovO9XhtWx83ecxHCb-c8Wd-wDvWu4VJkqvJXJ14iAWU7mQUmMeUT16zgBE9TKpC2ZPNzYCSCHPJq7BfPXcS3wKbKNYHNklCjDOiBE5DVuI7tuCergiVTiD2EjlpVbFPgDbB5ew7sUtI5wyNaAYE4jTo1mYSI4kRciRDDI7q0m-3oZ9gjA9_5XEZbh5wLY2pmr2W2wX59dUhmO5_jojhzXkPuzl9IkMrwYxs1LxzZNTQ77HEx0i-3nKYuuxCDxGmgLU7FGWlz1v-00rz24UcUJua_aS2mhgKLnF6sj6R6dAFySKiCT5sIAYhs5Dyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سازمان مدیریت بحران: ۱۸۴ نفر از ابتدای سال بر اثر غرق‌شدگی جان باخته‌اند
🔹
بیشترین آمار فوتی مربوط به استان‌های فارس، چهارمحال‌وبختیاری، خراسان رضوی و خوزستان بوده است؛ درحالی‌که ۳ استان نخست دسترسی به دریا ندارند.
🔹
حدود ۳۰ درصد غرق‌شدگی‌ها به‌دلیل ورود افراد به رودخانه‌ها و کانال‌های آبی رخ می‌دهد و آب‌های راکد، کانال‌های کشاورزی و تأسیسات انتقال آب در بسیاری موارد خطرناک‌تر از موج دریا هستند و قربانیان بیشتری می‌گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/442785" target="_blank">📅 15:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442784">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee06ce13e2.mp4?token=Gs0NW4l9sSHjvP6oBFOvmHArRARm3QItSVIleoVPMGZRgBj6vWtsQTZUvw6DEAv0DBLNCFIyxo8uDy7e38KSjpRIs0UbpfUPhSqYV3BcHs6ddBpN47fZMfmdPdVjPHibM0Fl5HIbz33msssOo5-YzuLAfs8QCsjr0pN3zRATNZ-zw0RSZHkTkK0QvhOgni8vpMYz3wpuL1IPW6Sht5AH1dAsl8A1fyZ4U3Mfe9uMYjomBR1SRxLncJTa67udMdASqm4UAk-LIBawTJDfYiuxlZ6BUA-iCwdtvSCtJWy3D1KJXFApSe95UGdHdyMjyTv0IvHIz3_vP940Bz8DlAPI7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee06ce13e2.mp4?token=Gs0NW4l9sSHjvP6oBFOvmHArRARm3QItSVIleoVPMGZRgBj6vWtsQTZUvw6DEAv0DBLNCFIyxo8uDy7e38KSjpRIs0UbpfUPhSqYV3BcHs6ddBpN47fZMfmdPdVjPHibM0Fl5HIbz33msssOo5-YzuLAfs8QCsjr0pN3zRATNZ-zw0RSZHkTkK0QvhOgni8vpMYz3wpuL1IPW6Sht5AH1dAsl8A1fyZ4U3Mfe9uMYjomBR1SRxLncJTa67udMdASqm4UAk-LIBawTJDfYiuxlZ6BUA-iCwdtvSCtJWy3D1KJXFApSe95UGdHdyMjyTv0IvHIz3_vP940Bz8DlAPI7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: توافق با ایران بسیار قوی است؛ هیچ‌کس نمی‌داند [جزئیات] آن چیست، اما بسیار قوی است.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442784" target="_blank">📅 15:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442783">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d9391399f.mp4?token=Zjd_ZidbVUUU7J1f3qeWf00UswUAvBj_NwkyP3cVBt8GMc8yqX5IDbxL_C_w4Ky8VZeUQm9lVdsfxGADFfQNjL5BFvUrzbPV4lp--QeALjnX2I9iYsM1YW2r6pKmm4QPFU3_mVk48efRydSuIS9jRe7XQaCMl2tCSEoRIgs1XrDybOKrlGFG6EekuwFlQePcyqRjJlADXTB-62v-hgBazMu62aGkzkRMYN6-3QGc6qfS9WSzlJQaDFvSCleRzm2oqsKyNmWO0CgNqD34Yi2Mk7KDasavysuva0V9W-z0pTufLaDpP71xBAx2zpny6jF629IDcFSH9LrJ2anTr3BQBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d9391399f.mp4?token=Zjd_ZidbVUUU7J1f3qeWf00UswUAvBj_NwkyP3cVBt8GMc8yqX5IDbxL_C_w4Ky8VZeUQm9lVdsfxGADFfQNjL5BFvUrzbPV4lp--QeALjnX2I9iYsM1YW2r6pKmm4QPFU3_mVk48efRydSuIS9jRe7XQaCMl2tCSEoRIgs1XrDybOKrlGFG6EekuwFlQePcyqRjJlADXTB-62v-hgBazMu62aGkzkRMYN6-3QGc6qfS9WSzlJQaDFvSCleRzm2oqsKyNmWO0CgNqD34Yi2Mk7KDasavysuva0V9W-z0pTufLaDpP71xBAx2zpny6jF629IDcFSH9LrJ2anTr3BQBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردی که در ایست‌بازرسی‌ها ترومپت می‌نوازد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/442783" target="_blank">📅 15:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442782">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80926d0a5.mp4?token=fB7YMTNNHDg_Cqf9qKztKYvEbWX93KEpip7Mg5P9MfaxDpxU-sCBGw5sQ67_d-cmR4VWs1-8UH2AyzQGGTTi2g7pEMrzbr9_w5vFMl0bcH-QZe4YMsLs1_GzypYkBZWypYTQVCwHEaSI0pVHBsbTEgk7SQZw_5V1QB1KZt0_UhO5XhME-uUHorsjcxzUN0HKy9dRXSB8fUjropB1MkgQzgivU_SUSekJ7-1bGr6HKxi1d6rhd5iHKY9MwN07ZpSB2a_eTeQiiQMZFIS9GbCm9jq6NOseok6AOWaGEAbOZFC9AcIRB02iO-i9KHIBfo0DzJQclmFMgTlSY-_omoqW8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80926d0a5.mp4?token=fB7YMTNNHDg_Cqf9qKztKYvEbWX93KEpip7Mg5P9MfaxDpxU-sCBGw5sQ67_d-cmR4VWs1-8UH2AyzQGGTTi2g7pEMrzbr9_w5vFMl0bcH-QZe4YMsLs1_GzypYkBZWypYTQVCwHEaSI0pVHBsbTEgk7SQZw_5V1QB1KZt0_UhO5XhME-uUHorsjcxzUN0HKy9dRXSB8fUjropB1MkgQzgivU_SUSekJ7-1bGr6HKxi1d6rhd5iHKY9MwN07ZpSB2a_eTeQiiQMZFIS9GbCm9jq6NOseok6AOWaGEAbOZFC9AcIRB02iO-i9KHIBfo0DzJQclmFMgTlSY-_omoqW8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما در ایران سرمایه‌گذاری نمی‌کنیم
🔹
ادعای ایجاد صندوق سرمایه‌گذاری ۳۰۰ میلیارد دلاری در ایران دروغ است. من درخواست ایجاد این صندوق را از کشورهای حوزهٔ خلیج فارس نمی‌کنم.
🔹
البته اگر آن‌ها این کار را انجام دهند، مشکلی نیست؛ اما من می‌گویم آن‌ها تا…</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/442782" target="_blank">📅 15:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442781">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344ae8b55a.mp4?token=MV5buhjLDD0_6E5uBaB-mNi46uROxRCSpd8gJMqzNAlevL2coF-bqPHqN9byE5pT1g1rqWsVN7ZC8QbXSJ37zsUu7aHAlfKJOeSgG-eZfOfdwLCpiRdYCHqeUNpzjMV1bD1AKjdac0ouuQkj_0O0CsDMntCc1VIPt-xtnYmTwFdTSGb3SjTh_aaf9ReflLWHYlzdJumk7UcfuSP2qAF10ALmfluc_xps2wroy4e0CzlJ7kDad0NURllS5Y9rHIJieCjy-WA6X6Ouyh-MTS4cCwmGYtmewEUXOzM5Wxm_iZ2FiqDZHksLofGKXJLRy1yZL_Z8JIpT9Suw7raxlQ84Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344ae8b55a.mp4?token=MV5buhjLDD0_6E5uBaB-mNi46uROxRCSpd8gJMqzNAlevL2coF-bqPHqN9byE5pT1g1rqWsVN7ZC8QbXSJ37zsUu7aHAlfKJOeSgG-eZfOfdwLCpiRdYCHqeUNpzjMV1bD1AKjdac0ouuQkj_0O0CsDMntCc1VIPt-xtnYmTwFdTSGb3SjTh_aaf9ReflLWHYlzdJumk7UcfuSP2qAF10ALmfluc_xps2wroy4e0CzlJ7kDad0NURllS5Y9rHIJieCjy-WA6X6Ouyh-MTS4cCwmGYtmewEUXOzM5Wxm_iZ2FiqDZHksLofGKXJLRy1yZL_Z8JIpT9Suw7raxlQ84Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ما باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442781" target="_blank">📅 15:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442780">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f32d523736.mp4?token=uppaJxj3B0TlMrJjRdzbwY0kYKfi24NraCIdLJX6Pt-lVGULcUc-b5KU710yuqXL3FCWEp0wlPKAM0BeLd-PEiiPtoQ8YkWUfMKO2W1Mx6uZ1xX55_1wQj5v5aoNJSLxJiLGt5SMKJmXt6fPYjYd21lslzoWBm_ALJW9AhgKgyBA6wJrMjQS-gS7Fv2rzL_6pQX8xs8Rb9KOH3fzntV2-cK0-fIMYNc7fUpxRamnVjw8PaIxJjGEjBiJrmFRdGImOqutaUwulvi6djvm09MVU0SgW03kembU1SamjexAq8Q3WRRkKUxTMt4GFB8x77GWAwPoQZYX61Y27qE3jcSwCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f32d523736.mp4?token=uppaJxj3B0TlMrJjRdzbwY0kYKfi24NraCIdLJX6Pt-lVGULcUc-b5KU710yuqXL3FCWEp0wlPKAM0BeLd-PEiiPtoQ8YkWUfMKO2W1Mx6uZ1xX55_1wQj5v5aoNJSLxJiLGt5SMKJmXt6fPYjYd21lslzoWBm_ALJW9AhgKgyBA6wJrMjQS-gS7Fv2rzL_6pQX8xs8Rb9KOH3fzntV2-cK0-fIMYNc7fUpxRamnVjw8PaIxJjGEjBiJrmFRdGImOqutaUwulvi6djvm09MVU0SgW03kembU1SamjexAq8Q3WRRkKUxTMt4GFB8x77GWAwPoQZYX61Y27qE3jcSwCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیمت‌های جدید لبنیات اعلام شد  دبیر انجمن صنایع لبنی از افزایش قیمت ۴ قلم پرمصرف لبنی خبر داد:
🔸
شیر نایلونی: ۸۴ هزار تومان
🔸
شیر بطری: ۹۸ هزار تومان
🔸
پنیر یواف ۴۰۰ گرمی: ۲۰۳ هزار تومان
🔸
ماست دبه‌ای ۲ کیلویی: ۲۲۸ هزار و ۷۰۰ تومان
🔹
هفتهٔ گذشته نیز قیمت شیر خام…</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/442780" target="_blank">📅 15:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442779">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3c9c4c0d.mp4?token=dHrBC1YNfThxopy1YUfSB5sOB8TVt2FQbhmolT9uJhIxMfPlq0W12qIZFgSKZ3AXspoO0Ay_EEZl2DgBC5rwSw13rBX5WI-a2p1cmrQRr8PnIEWT4pVwimB2212B1i-DlPSr2wuug7aRFXObldEtejcNMfWRs0iD5WB85O3Dd5J0-q2BkrazANo-rpUNFptv91stid9bvSQKBJOn6cBz_BL8UC5J-636HKuQ1D3_NGvLLv9P6WIg1lBP7C6ycNZVxZ96R1CJEwCdqKYHUxYXIi30Zsx0j4gexiEnbJcXOAJIgDRgYZb6NOvR2_wfqP72MJkjSdiyd5Sn9UEyZEZHTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3c9c4c0d.mp4?token=dHrBC1YNfThxopy1YUfSB5sOB8TVt2FQbhmolT9uJhIxMfPlq0W12qIZFgSKZ3AXspoO0Ay_EEZl2DgBC5rwSw13rBX5WI-a2p1cmrQRr8PnIEWT4pVwimB2212B1i-DlPSr2wuug7aRFXObldEtejcNMfWRs0iD5WB85O3Dd5J0-q2BkrazANo-rpUNFptv91stid9bvSQKBJOn6cBz_BL8UC5J-636HKuQ1D3_NGvLLv9P6WIg1lBP7C6ycNZVxZ96R1CJEwCdqKYHUxYXIi30Zsx0j4gexiEnbJcXOAJIgDRgYZb6NOvR2_wfqP72MJkjSdiyd5Sn9UEyZEZHTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: با ایران یادداشت تفاهم امضا کردیم نه توافق نهایی؛ اگر از آن رضایت نداشته باشم، دوباره بر سرشان بمب می‌ریزیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/442779" target="_blank">📅 15:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442778">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUiOhqaviu2_P7FOypWsYbjS8ucTifgK3YD_g1z870C7xqKmNLmexR1nI8pxbK47VVjNP4SrDMm0jIrxya4F9FJQjkYnmVPqyvOQk1byOq9gZ6DDwKJ1ZXTkT3uzvG228ArYSZexnQDXsmpLYROD-kVd63QaWUk0Nqj-b60vyucaleikJs6dsjluMkjQLIMPabQhoubp7TqH8orpTwuOcOLQwuT_NkAAGVnJhlgbMg8u7b5tQE7SBNj87XZI_cE9vswMMzVkI9Zm5KH2TuqqlKuokOquVe5sRqHsdMGT83sgmfFiUkAagPkSj-csgRttOEo8AuCddjsbdufNFMluYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید این نکته درمورد دور موتور هواپیما باورتان نشود
🔹
برخلاف تصور رایج، موتور جت هواپیماهای مسافربری با دورهای بسیار نجومی نمی‌چرخد و سرعت چرخش آن چندان بیشتر از خودروهای اسپرت نیست.
موتورهای توربوفن مدرن از ۲ بخش اصلی تشکیل شده‌اند:
🔹
توربین پرفشار: حداکثر حدود ۱۵ هزار دور در دقیقه
🔹
توربین کم‌فشار: حدود ۵ هزار و ۴۰۰ دور در دقیقه
🔹
دور توربین پرفشار تقریباً برابر با دور موتور خودروهای مسابقات فرمول یک است، درحالی‌که توربین کم‌فشار در محدودهٔ دور موتور خودروهای معمولی قرار می‌گیرد.
🔹
با وجود این شباهت در سرعت چرخش، موتورهای جت نیروی رانش بسیار بیشتری تولید می‌کنند؛ به‌عنوان مثال، یک موتور جت می‌تواند نیرویی معادل ۱۲۱ هزار نیوتن ایجاد کند و هواپیما را با سرعتی بیش از ۸۰۰ کیلومتر بر ساعت به‌حرکت درآورد.
🔹
دلیل اصلی این قدرت بالا، سرعت چرخش قطعات نیست؛ بلکه حجم عظیم هوایی است که موتور به‌سمت عقب پرتاب می‌کند و همین موضوع نیروی رانش لازم برای پرواز را فراهم می‌کند.
🔹
در نتیجه موتور هواپیما برخلاف تصور عمومی با دورهای فوق‌العاده بالا کار نمی‌کند؛ راز قدرت آن در طراحی آیرودینامیکی و جابه‌جایی حجم بسیار زیاد هواست، نه صرفاً تعداد دور موتور.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/442778" target="_blank">📅 15:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442777">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246216472e.mp4?token=SiEfZJz-8RCI12H4hnFwqMTDMEAhwkwGUiggG2-UL-2FNrHnMYxcSGJud7DvhIhMECChcSCsPQ-fqyZWOmKZYhYAuxJyDjxctSCBDZjt-cb9edxHggIOiKDoLDIAqrHw52H2P_OUZwQZneOO9UftRhC_BEkyhAGWjQAU_wMN4_c9RUBmJVQxlxMgp1Ui_HkB3LVaBVjTwto32LeV2UkdNLxP98_lilfi_pU-0T7ivlS9TjYkGexcGKrrtRUGsyDoL2VG9HtmQB7dIOAx52baCq-C5A_Uhq0d9OZXiB985kMyJ5DRUuyubzARIvV7N-C-WT7y3c8rqeasLf3-3GGo2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246216472e.mp4?token=SiEfZJz-8RCI12H4hnFwqMTDMEAhwkwGUiggG2-UL-2FNrHnMYxcSGJud7DvhIhMECChcSCsPQ-fqyZWOmKZYhYAuxJyDjxctSCBDZjt-cb9edxHggIOiKDoLDIAqrHw52H2P_OUZwQZneOO9UftRhC_BEkyhAGWjQAU_wMN4_c9RUBmJVQxlxMgp1Ui_HkB3LVaBVjTwto32LeV2UkdNLxP98_lilfi_pU-0T7ivlS9TjYkGexcGKrrtRUGsyDoL2VG9HtmQB7dIOAx52baCq-C5A_Uhq0d9OZXiB985kMyJ5DRUuyubzARIvV7N-C-WT7y3c8rqeasLf3-3GGo2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگۀ هرمز همچنان در مشت ایران
🔹
با فروپاشی محاصره دریایی آمریکا ۳ نفتکش ایرانی با ظرفیت ۵ میلیون بشکه نفت خام از تنگه هرمز عبور کردند.
🔹
کشتی‌ها برای عبور از تنگه همچنان منتظر اجازۀ نیروی دریایی سپاه هستند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442777" target="_blank">📅 14:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442776">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f55cc49105.mp4?token=HRo58hJxHV7T_7Otezh5AYf7lplTwT6wDI22JILEMd2KamuaEiEDJRh3Y89w0pAIBC5gFAP9vfQ4mnflE5mxlpmEWpZLyvcAsIa7CN6ttuQ2jWhiMITUsGVOuiJ7-VOBstcgY4P-UJVkUKUrfo2YTQdm8ZPRMkuOF3yMwpUtiT-b1FoTJfFYhP_xiqHp8QaQ_GrUdwUKsd12nwV7Jfa9ocPd1GFcDTCQjsXNsc_F7_J3fkn5RfU96v2vhzOjBEScwj01BgM0Y7ulIjMUJ9wHm6sWHjqB_WprfPkxOyy9TO-zSeewnFMwAa7aahCTUp_VB__qSl76QOw5OIipXpv5TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f55cc49105.mp4?token=HRo58hJxHV7T_7Otezh5AYf7lplTwT6wDI22JILEMd2KamuaEiEDJRh3Y89w0pAIBC5gFAP9vfQ4mnflE5mxlpmEWpZLyvcAsIa7CN6ttuQ2jWhiMITUsGVOuiJ7-VOBstcgY4P-UJVkUKUrfo2YTQdm8ZPRMkuOF3yMwpUtiT-b1FoTJfFYhP_xiqHp8QaQ_GrUdwUKsd12nwV7Jfa9ocPd1GFcDTCQjsXNsc_F7_J3fkn5RfU96v2vhzOjBEScwj01BgM0Y7ulIjMUJ9wHm6sWHjqB_WprfPkxOyy9TO-zSeewnFMwAa7aahCTUp_VB__qSl76QOw5OIipXpv5TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: با ایران یادداشت تفاهم امضا کردیم نه توافق نهایی؛ اگر از آن رضایت نداشته باشم، دوباره بر سرشان بمب می‌ریزیم.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/442776" target="_blank">📅 14:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442775">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786c67eb77.mp4?token=aABzbSJ8Qe0L6VhPUg398hVkFD-rcvVJWrP-P3Y-_WttPQD62gNhuhCRdap-bxCHmof-XaiDCVGkn2Gnj7d6pLS3KsHoQmDwyNd6sNAawx5CY339tj_O2mEXUqoH2dq2yVZz1oLM-_Kp6uC-3emiYD7maoCnCKj66JrHxSJGg9X1p1f8H-xSpda0P8o1Wr-7t8JWJZgW8rMVDplt2eQZ0h2fZz4v7bq-KISyS1uW6ZVoi7oa2cPS13Kotnqm35TS2G8nb8F3TynoIzAFayKgKylfG8E525LjZpB1afoYbS2MW6OE2uVQO_MJIf7pMrGXnpZTFQHsJpVltrt4QAUZWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786c67eb77.mp4?token=aABzbSJ8Qe0L6VhPUg398hVkFD-rcvVJWrP-P3Y-_WttPQD62gNhuhCRdap-bxCHmof-XaiDCVGkn2Gnj7d6pLS3KsHoQmDwyNd6sNAawx5CY339tj_O2mEXUqoH2dq2yVZz1oLM-_Kp6uC-3emiYD7maoCnCKj66JrHxSJGg9X1p1f8H-xSpda0P8o1Wr-7t8JWJZgW8rMVDplt2eQZ0h2fZz4v7bq-KISyS1uW6ZVoi7oa2cPS13Kotnqm35TS2G8nb8F3TynoIzAFayKgKylfG8E525LjZpB1afoYbS2MW6OE2uVQO_MJIf7pMrGXnpZTFQHsJpVltrt4QAUZWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست هم‌فکری قالیباف با اتاق بازرگانی
🔹
نشست هم‌فکری نمایندۀ ویژۀ ایران در امور چین با اتاق بازرگانی، با هدف ارتقای همکاری پایدار اقتصادی تهران  و پکن برگزار شد.
🔹
پس از جلسۀ دو هفتۀ پیش وزرای اقتصادی دولت با نمایندۀ ویژۀ کشورمان در امور چین، نشست امروز دومین…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/442775" target="_blank">📅 14:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442774">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6074564280.mp4?token=uOJumqvBr-KFyjJdpwF5KVOez1tbWbYV5oo4rgqJ-yX7KM0QYZBwFsEj4bnvY4GBBi7B2FmbRkjf6rt8xVTAAkWhbSFYV17_ZS1bCLOFLnrukDuY1iKkGScOhRSMhjL75UcgCd_pFE7s07Kd2ibDsngGZShY4raz-pyvMkdufVM5OpBKN-Dfvj_fAal0uy29qdL7ooZ_o5riE26N54S5fF_UHbdyXeIZtvHQXTMgchye511Y5Li0J7uSk4jHatDPM4VHL5K0uKyxNBlmigmrFggp6iORBxnnuJa5om-hErhRSXr7ynw2Elc42Fx3xlYewT2I8YvLvl9joTbLCP6X-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6074564280.mp4?token=uOJumqvBr-KFyjJdpwF5KVOez1tbWbYV5oo4rgqJ-yX7KM0QYZBwFsEj4bnvY4GBBi7B2FmbRkjf6rt8xVTAAkWhbSFYV17_ZS1bCLOFLnrukDuY1iKkGScOhRSMhjL75UcgCd_pFE7s07Kd2ibDsngGZShY4raz-pyvMkdufVM5OpBKN-Dfvj_fAal0uy29qdL7ooZ_o5riE26N54S5fF_UHbdyXeIZtvHQXTMgchye511Y5Li0J7uSk4jHatDPM4VHL5K0uKyxNBlmigmrFggp6iORBxnnuJa5om-hErhRSXr7ynw2Elc42Fx3xlYewT2I8YvLvl9joTbLCP6X-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین صوت اذان در شهرک مجدل‌سلم در جنوب لبنان پس‌از بمباران‌های رژیم صهیونیستی
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/442774" target="_blank">📅 14:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442772">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e2e712e72.mp4?token=eGF1qtbmGsbJyT8FQRmY7hTNvzkaOHWTxpQ9aRgH_gTzDreRi1Wf5qtZAEEN4Beb7oV4Eh7dUq_wYo8m_MKkuD3lV5qEAcIV5-rLXp31O6TOl6iVzYVUcIkBv5TzcJyER0joqPpoC0MEx_0Irvsx3sxIDXxgmjjlM5p4G3ofrg2P7x18mTW-VWra7sD9dKL8tk9b_n2sCQEXCzlCsVHhMp0FXW8-9VvYUmSrODTbREUplL0JzOYHyWPnYgvbbXPC5MZ8blDYuW2IxIYeoF6V46pE3Ow23I3GPNKa6E-Gq85svD-stiSAcIhCyW0Z7VFFkWM-RhddhSPEpujgXg1N2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e2e712e72.mp4?token=eGF1qtbmGsbJyT8FQRmY7hTNvzkaOHWTxpQ9aRgH_gTzDreRi1Wf5qtZAEEN4Beb7oV4Eh7dUq_wYo8m_MKkuD3lV5qEAcIV5-rLXp31O6TOl6iVzYVUcIkBv5TzcJyER0joqPpoC0MEx_0Irvsx3sxIDXxgmjjlM5p4G3ofrg2P7x18mTW-VWra7sD9dKL8tk9b_n2sCQEXCzlCsVHhMp0FXW8-9VvYUmSrODTbREUplL0JzOYHyWPnYgvbbXPC5MZ8blDYuW2IxIYeoF6V46pE3Ow23I3GPNKa6E-Gq85svD-stiSAcIhCyW0Z7VFFkWM-RhddhSPEpujgXg1N2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تولد یک مرال در پناهگاه حیات‌وحش آستارا
🔹
نخستین گوسالۀ گوزن قرمز (مرال) امسال در سایت احیا و تکثیر پناهگاه حیات‌وحش لوندویل آستارا متولد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442772" target="_blank">📅 14:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442771">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cfca5325.mp4?token=J4DChtldqS_cESdbQYj5TUFXn6qK6xXXiQx07eqBDivNBvRbiZInKqGmNJexEOzZeejjj-v5Lne2Qa5kLV71jv_pDwOg1ermMIeegqr4433mF6XmENimV1rXSog9Fx3T58mxJ1RgeuACQpZahuaAl_Wm0jSANl3MbY5W6YPmELO1FePY_-FtCrlZde_Oz4hmgtbLrK6iLTnWgSKgpRkVxM9W-EVF5CCWQ-Ts2SfJIxkgk3vFO1LmBVqWkwW343pq19-92But3qgNzYJOi8BrcNRlt2lwGvlf04DFYr5FvHYZCo6JF6iz4G4oZmg12CgViTcNDFjpv2lZpLP8usiIVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cfca5325.mp4?token=J4DChtldqS_cESdbQYj5TUFXn6qK6xXXiQx07eqBDivNBvRbiZInKqGmNJexEOzZeejjj-v5Lne2Qa5kLV71jv_pDwOg1ermMIeegqr4433mF6XmENimV1rXSog9Fx3T58mxJ1RgeuACQpZahuaAl_Wm0jSANl3MbY5W6YPmELO1FePY_-FtCrlZde_Oz4hmgtbLrK6iLTnWgSKgpRkVxM9W-EVF5CCWQ-Ts2SfJIxkgk3vFO1LmBVqWkwW343pq19-92But3qgNzYJOi8BrcNRlt2lwGvlf04DFYr5FvHYZCo6JF6iz4G4oZmg12CgViTcNDFjpv2lZpLP8usiIVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاتک کره‌شمالی به فیفا در جام جهانی
🔹
درحالی‌که فیفا میلیون‌ها دلار از کشورها برای پخش مسابقات جام جهانی دریافت می‌کند اما طبق گزارش سایت Alerta Mundial کره‌شمالی بدون پرداخت حتی یک دلار بازی‌ها را در کشورش پخش می‌کند.
🔹
براساس گزارش رسانۀ اسپانیایی، کره‌شمالی سیگنال ماهواره‌های کشورهای همسایه مانند چین را هک کرده است.
🔸
پیش از این چین و هند به‌عنوان ۲ کشور پرجمعیت دنیا برای کمتر پرداخت کردن حق پخش با فیفا چانه‌زنی کردند ولی در نهایت چین حاضر شد ۶۰ میلیون دلار پرداخت کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442771" target="_blank">📅 13:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442770">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2c2769de.mp4?token=ZJ8enJfocikj3B0igbqgK8uxhZR4sP3SlnqRaSlSlG0WUASysU93dhd56czWM57gaJ7YpQ7Wu2saCUg1oTip6r3u-5cQFaJhraeraZNYq_oS-V-LjIMLdDtAjld5nM27lU-DGZpm4If0D8d4kvohIEnAuv4sKzsU_wIDoHZsdiuy_0_If6JJJ2F8CmJyKU4F6OZmkRX6snoDV4m423Q86_zrq6mNP2_uJVd-xcKnEVLxNkXf3OEH5kpnoaYKAqgzpeoyAK-MF57cvRTISKfsVsiZDhzYS0cu9sblmTew7aFY08Vqe3mt5ZQJ0phm9_Nn7CIUnxu5I5PbwLUgVKkDeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2c2769de.mp4?token=ZJ8enJfocikj3B0igbqgK8uxhZR4sP3SlnqRaSlSlG0WUASysU93dhd56czWM57gaJ7YpQ7Wu2saCUg1oTip6r3u-5cQFaJhraeraZNYq_oS-V-LjIMLdDtAjld5nM27lU-DGZpm4If0D8d4kvohIEnAuv4sKzsU_wIDoHZsdiuy_0_If6JJJ2F8CmJyKU4F6OZmkRX6snoDV4m423Q86_zrq6mNP2_uJVd-xcKnEVLxNkXf3OEH5kpnoaYKAqgzpeoyAK-MF57cvRTISKfsVsiZDhzYS0cu9sblmTew7aFY08Vqe3mt5ZQJ0phm9_Nn7CIUnxu5I5PbwLUgVKkDeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله تصاویری از انهدام خودروی زرهی ارتش صهیونیستی در جنوب لبنان را منتشر کرد
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442770" target="_blank">📅 13:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442769">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9mfGnvAlAMRVRNtKH_NN0vV0-0vVV_LuMOfeFac1tB0zA8gpa4fgYGOgQl9bN0HFTcUunCoRxzxMsSIeX9JYL4AXF-UzpnyJ9qxIZK_FUQjVJwfZnrzLZRt-eP9dfxejBQVBuW1HnNrGQDyAt_oVEJNm7g7NkEaTPVtikaoh2ujhhB7AGvvmNfcXlcKKV9VFgHp-KcDmjOx189ncULMajUHyHIuz_Jej6_3NYoKi-2sUsQMCebT_YqbGCUePAWDs2Kf24y4FdRVZzRmbKNhF8I61NLYT_Nwanhn5ipcF30JZ3pQ8dBkBxMJKKqO63ZqmpFe1gpljprzc8OyOwKsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدارهای حملهٔ پهپادی در زرعیت در شمال فلسطین اشغالی فعال شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442769" target="_blank">📅 13:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442768">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8m9IBK3JW5MYNrj7ggBnSlc_sqa0KwBLFmly9msalBp117khVUSxctdCkJ6Kdyw2_g36BjEMZC6mP9EQ8h6JHWO0SzpG7Mj8MSUPNMri6yS-0sIHtDmqURKRjAnKA8axcP3ZBuycKMBtjl8MVR5UCY8Bu0Zi2jmOWUUjKoBsX7Pdffi2m_jslV-ABBeIMflnX8caVH1XteJ_En1d4dPZ4ym0uG9w08Ki9ygt4I8ujIxmS5r4qzTCk3RtioAtQPjrKF27Q96EveWy-rUi4zuCVwNjsyrnNbHXhOJsWpQP5rGqLtYswKCrrcF6U18Tl-V60FG8VlBs8rCGWIOCn68Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معتمدیان رئیس ستاد برگزاری مراسم تشییع رهبر شهید انقلاب در تهران شد
🔹
معتمدیان، استاندار تهران، با دریافت حکمی از سوی معاون‌اول رئیس‌جمهور، رسماً به‌عنوان «رئیس ستاد برگزاری مراسم وداع و تشییع رهبر شهید انقلاب اسلامی در استان تهران» منصوب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/442768" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442767">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/035963a43e.mp4?token=k0EAmGOpMM8KNWWinUWc9MlpnFAvCQmlY9O1tL8o7AlTd_IVnz2Q03_MVIpM8G9WrdO-w_VQcRzKpY76Io8Ys8eoWTCwx2YRed1tn6YTUzVDcvBohEOPupmL3pzmmIa-sp4UyqSPDJmBdVOhvTLTXF9KSh4k3NqUQpoUZFq1Mf6UapqIDnr_n1jvWT-kIlpj5jFpkeQxi-T3ZANxzNqCo0t9igOOJQIzaVgdXQe5kHrLpDLDzpB5L577RzaTBr_w4nuPDfjvyHb-N4fj27xmHZflCCE7dtgPyFq2DYDFo95eU4Ad1N8sOarbn-nH5gIvGpUCguiG7bUFLcAaGioO9lP14AhTpOMzDsCZxeoRb8NDdLt6s59r6jcWWc037bATukHYwhU8zORP_AQLIt__tbGiS5udOGuoQfJz58bKMvGQ-iZ76UpPaZj3EAFK-HdCzI8SncdMUYNhIFgvKXtrS_f0zS0EOMm3ysVwcN0twNc6Sc3ty8p3rz_BZkOBssYfNMjc3dx-lHLNf_Yv_jQQ2t2fp2pmqr5YvH2yzU0wXR94m5ClBs-hYQhR3qW8cagOy2CfqdvBbWvrusWUxLdz4P3dS5nqO-HnANFh5TnS8KUpwAzaVPefzUVU9wbZ25W3I230p1VYocR_U-Z8jTnmBPO3lWCHQtbvV-GWO7xkKg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/035963a43e.mp4?token=k0EAmGOpMM8KNWWinUWc9MlpnFAvCQmlY9O1tL8o7AlTd_IVnz2Q03_MVIpM8G9WrdO-w_VQcRzKpY76Io8Ys8eoWTCwx2YRed1tn6YTUzVDcvBohEOPupmL3pzmmIa-sp4UyqSPDJmBdVOhvTLTXF9KSh4k3NqUQpoUZFq1Mf6UapqIDnr_n1jvWT-kIlpj5jFpkeQxi-T3ZANxzNqCo0t9igOOJQIzaVgdXQe5kHrLpDLDzpB5L577RzaTBr_w4nuPDfjvyHb-N4fj27xmHZflCCE7dtgPyFq2DYDFo95eU4Ad1N8sOarbn-nH5gIvGpUCguiG7bUFLcAaGioO9lP14AhTpOMzDsCZxeoRb8NDdLt6s59r6jcWWc037bATukHYwhU8zORP_AQLIt__tbGiS5udOGuoQfJz58bKMvGQ-iZ76UpPaZj3EAFK-HdCzI8SncdMUYNhIFgvKXtrS_f0zS0EOMm3ysVwcN0twNc6Sc3ty8p3rz_BZkOBssYfNMjc3dx-lHLNf_Yv_jQQ2t2fp2pmqr5YvH2yzU0wXR94m5ClBs-hYQhR3qW8cagOy2CfqdvBbWvrusWUxLdz4P3dS5nqO-HnANFh5TnS8KUpwAzaVPefzUVU9wbZ25W3I230p1VYocR_U-Z8jTnmBPO3lWCHQtbvV-GWO7xkKg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از تسلیم ایران می‌گفتند اما حالا از قدرت ایران حرف می‌زنند!
🔹
پروفسور جفری ساکس، اقتصاددان و تحليلگر سیاسی آمریکایی: آمریکا نتوانست ارادۀ خودش را به ایران تحمیل کند چون ایران دارای ظرفیت نظامی قوی و پیشرفته است.
🔹
پروفسور رابرت پیپ، استاد علوم سیاسی دانشگاه شیکاگو: ایران در مسیری قرار گرفته که به‌دنبال افزایش قدرت خود است و آنها به گرفتن پول یا موارد دیگر راضی نمی‌شوند و به‌دنبال حذف نیروهای آمریکایی از منطقه هستند.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442767" target="_blank">📅 13:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442766">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oG9lSoZWfHtXekqaAHjyVxBTVmpyagjeWoY6M7b9Gp9lYMyw_6GK6Z068wdnlEroSHO1gBRY0K_C4Vopg5hnJxhJXmg4j1ntbElr0afp55TxIbJj7ju6HOcVyHuYIQdwVFd-guc4kTFh_scAMCwXowqG9VgUZwGgpoPeoF-Qgh9H8bniJb2SNbEU9VnROwtd8ZbsKaB5I4iBhX80evyhdI-M-7Z_jd3z2pAsO92iUWRHbFJ7NKZ4yuxC_hkmmvAQXhJE2Zl43IffOUvx48GHVFeuKNM-Z0IbrCQKJurNdOu3HInKakdBkprOnQf4fJy0_zkDFUwERkYupRk0mjyZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۵۱ هزار واحدی به ۵ میلیون و ۱۵۱ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/442766" target="_blank">📅 12:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442765">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d005037a59.mp4?token=SAnsuAJ411dNP6NEpANNcLFQln6sZxxQQF9Nw-N5PLdgn9KMhypCf9fWbwjhxplCvwbgy-3jGG1YE_KX2oru0-oNMWPmxgW16HpkAtk4NNZ8-LQiz4912f2Hw4hiw9Espq-Ev1SWpKPAkq_JVJdBlsdd7iM4sHNbMKX-0dYysZzStzmJ6Tsp6iY-X3vHBtV1ulYtfeIJ4UUiyWe2HWWRGWEFvvCYk-tWOfK9JasSwGV_Rrw2Sxi-9EGHZITp4tY0SX69xmYy8L76cxT4MRZBX-vg-KzerZ1BSJbZE2O-AhErkmbXbFMdV6LcBN9dPs93puIwK_-1YOHflvaQjeh8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d005037a59.mp4?token=SAnsuAJ411dNP6NEpANNcLFQln6sZxxQQF9Nw-N5PLdgn9KMhypCf9fWbwjhxplCvwbgy-3jGG1YE_KX2oru0-oNMWPmxgW16HpkAtk4NNZ8-LQiz4912f2Hw4hiw9Espq-Ev1SWpKPAkq_JVJdBlsdd7iM4sHNbMKX-0dYysZzStzmJ6Tsp6iY-X3vHBtV1ulYtfeIJ4UUiyWe2HWWRGWEFvvCYk-tWOfK9JasSwGV_Rrw2Sxi-9EGHZITp4tY0SX69xmYy8L76cxT4MRZBX-vg-KzerZ1BSJbZE2O-AhErkmbXbFMdV6LcBN9dPs93puIwK_-1YOHflvaQjeh8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیدحسن خمینی: جنگ رمضان جهاد اصغر بود؛ از امروز جهاد اکبر شروع می‌شود
🔹
واقعا باید از نزاع‌های بی‌حاصل که نتیجۀ منیت‌هاست دست بکشیم.
🔹
برای حفظ پیروزی باید جهاد اکبر را از درون خودمان شروع کنیم. در برابر مردم باید افتاده‌تر شویم.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442765" target="_blank">📅 12:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442764">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPhczQrMWwvge13BLsFB26NCkczvquMIEhrarXOelLU7yZtjuWWINtCuYW_aM6Cu6cX1ytWMecj9QLfBanlmeA3vjwHc2lbXFPUlOFpm7ZpNxOYD6kh9zB3LzPJzH2H1DC4t7xDeSJpVphuZps2PPYC-KQK9hfrqOkssHGdMzFw40JiBa2Gvy-Rvcn0pZIPUe50eaAP_gs8nE6fBDgNY72dAOZwhc729a-7DcCgFP2e2zte307c3uaRtzJW7vV5dje-YQr8PM6-mjAj0ptfb9skvjBUFKzqyjf6ihfJ_p8ssobQlWhmLyz1SzQowaSj2tKP3kPaxHVCglZVMJrtiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجوز اتحادیهٔ اروپا به داروی ایرانی
🔹
رئیس سازمان غذا و دارو: یکی از شرکت‌های دارویی کشور موفق شده مجوز فروش دارو در اتحادیهٔ اروپا را دریافت کند که دستاوردی بسیار ارزشمند و حاصل عبور از یکی از سختگیرانه‌ترین نظام‌های نظارتی جهان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442764" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442763">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6f319AkOQ_j2j5sOtGVW1FB6fD9DPUdioUIXRAX649JOIGzTPxgUeAvc2VFwfckCcB9aGihBvy2KpOWx_FBxR0mDoNljXabTMBOTHo0nCzRRIgGNTLvAiv7DIwEeci-4f-7EWkhh1fFl3swJo5nzh4fOz7G6-wzk6z2_yS_HC8JRmXwDai-vqRj5M5gbSgoQAuetx6ujIggFRwpe5bAGkCRfQ4Yy3IWxG8Hs1wJKEedcz812QsxUuAtn17ZJKyW7aEL4sMVtY-30yeqaM9jGDN6-j5pkMdZ9mz3rAwt4zOgrStcIJHdWGqDC4MoP-k90ufOGa6yBwVwDDiRuApeFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ روسیه: ایران حق غنی‌سازی صلح‌آمیز را دارد
🔹
مسئله نیروگاه هسته‌ای بوشهر فقط به روسیه و ایران مربوط می‌شود و هیچ طرف دیگری به آن مربوط نیست. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/442763" target="_blank">📅 12:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442762">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e94aa310.mp4?token=RI5EY_IJxTawv4WOtNIqTtHvxXT31eIsIsk8esTuH-C-GXtnq3mXyyYlfaeqKKcimrddcFOdJR6LoENzfw8Qh-08tqSiA93BkbeB9qyL2Dx2vqt4zXe290bbGS3om3t2w7Ze4pBrsanznTz0CIBMEwTOUtF0EdewQsVwkFofVr6rI2_0m4W_C7JTN3kDPKDxdvYDh8CYD-Ge04wuU07lOzWy1qzZuXAA_GJeMdZbD1FkBtYdHztMsDUTYad6CWx92QHkLav_k9baJmtwT3PtfB9HuMPD8gsgZBDxpNumb3GtCLFG0O9fJrSj0bHiQO_ZOUbTGXBg4LC_ovkaHcK_9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e94aa310.mp4?token=RI5EY_IJxTawv4WOtNIqTtHvxXT31eIsIsk8esTuH-C-GXtnq3mXyyYlfaeqKKcimrddcFOdJR6LoENzfw8Qh-08tqSiA93BkbeB9qyL2Dx2vqt4zXe290bbGS3om3t2w7Ze4pBrsanznTz0CIBMEwTOUtF0EdewQsVwkFofVr6rI2_0m4W_C7JTN3kDPKDxdvYDh8CYD-Ge04wuU07lOzWy1qzZuXAA_GJeMdZbD1FkBtYdHztMsDUTYad6CWx92QHkLav_k9baJmtwT3PtfB9HuMPD8gsgZBDxpNumb3GtCLFG0O9fJrSj0bHiQO_ZOUbTGXBg4LC_ovkaHcK_9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میان کاروان تو ندیدم غیر زیبایی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/442762" target="_blank">📅 12:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442761">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfYo1jypo_-DwqMzNuf2d_l34zIvsFRVYXsmmKzGoJ1oT4ueb8ohVeA2eNePiRdutnjNBIAA39CMN05x2Y22OLZnYSKp6vgRt3CTSEhLZYh4xkMqegGSPSLnSCik8FKTPDD239nk0DlQ5y3r393SYHP89aSpe5wFK8S7pHJM3jTPVpKdky1QNCPA9QnxIhS29Q7qCRZHizpXa0IXMpGUutgsShCnQuhFBpP5eawE66phKlUqtUn-rF-eKUhuLNrV6FOtkjHxi3N9TuK_y5lZTzNRpyUnb87y_OPkwzjgLc2J4Cwt0PuInmFqDLY8pnfaPYGYWvTOqWJWOPZpcUVSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با بازگشت آخرین کاروان حجاج ایرانی به کشور، پروندۀ حج تمتع ۱۴۰۵ بسته شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/442761" target="_blank">📅 11:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442760">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کشف یکی از بزرگ‌ترین پرونده‌های زمین‌خواری کشور در تهران
🔹
با اقدامات قضایی و پیگیری دادستانی تهران، یکی از بزرگ‌ترین و پیچیده‌ترین پرونده‌های زمین‌خواری در غرب پایتخت کشف و در دستور کار رسیدگی قضایی قرار گرفته است.
🔹
در این پرونده با جعل وقف‌نامه، اسناد رسمی…</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/442760" target="_blank">📅 11:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442759">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8844b0c69.mp4?token=tkb4ZO455RodbbYKZZ0zgblAyWD2wYp3374LKpXrVjSBBKT_Yxn16QX26B_qlbZa8qYmFjJYFOvrCrQglmxLw6V0O165YFc0EK8z_3JTSSuRGFYZcVx9o9TkeQti4itAhYzsUiupJL1EpK7TNIuHTD89vbOXbz-_PvMCWEeg673wSpjZCz-fURpBNXBSPdsVXguQV2TYpLGWTVaK1yykF1zvpP5HWosghwU7jhXPOcDHNYCwSEmMI3i8yqDmmtKcazLVnY5w4aapBt-pFk17vq6DQG6eQDxZnMJwfqxzrnJ-hv5uvyarGFEZ-5jmTcjXn9z673eHLEnXtEqZ8hVE_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8844b0c69.mp4?token=tkb4ZO455RodbbYKZZ0zgblAyWD2wYp3374LKpXrVjSBBKT_Yxn16QX26B_qlbZa8qYmFjJYFOvrCrQglmxLw6V0O165YFc0EK8z_3JTSSuRGFYZcVx9o9TkeQti4itAhYzsUiupJL1EpK7TNIuHTD89vbOXbz-_PvMCWEeg673wSpjZCz-fURpBNXBSPdsVXguQV2TYpLGWTVaK1yykF1zvpP5HWosghwU7jhXPOcDHNYCwSEmMI3i8yqDmmtKcazLVnY5w4aapBt-pFk17vq6DQG6eQDxZnMJwfqxzrnJ-hv5uvyarGFEZ-5jmTcjXn9z673eHLEnXtEqZ8hVE_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ پیدا کردن پیکر نوزاد ۲۰ روزه در جنگ رمضان
⚠️
هشدار تصویر دردناک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/442759" target="_blank">📅 11:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442758">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEmba0MYz32QDDIzlpIXgHh6hWFO10Wm4Tbrty5zWlUHgHFNMYZgN_jNkTp9CYBvkNm2HJIB0JdHlQGE7V7ZB2-Ujdg_r8N4PhC3EOiHhcDKqnLgA25qPQYLtaytRVPvQmisJ4g225JT3AmfteZqNRrx7BouZRvfSaxlfaGZe52-uLP1RrOxb9wll5OAROpHwn86YlB_M3K2yuETMWZ0vRPYG1dPM5AFR5HS1SgVgGrBfn5ScVHm7cEQN_snl-gXHpIOEiBE-RetaNPfXZ1Scg_PTZZxA8-bQ-waogX3B5CWVJNPcw4mDkVDZP9BViuf9bwgcMtHYO_mjXMh0MO0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه‌های ماهواره‌‌ای ایران در سال ۱۴۰۴
🔹
سازمان فضایی ایران برای سال جدید برنامه‌های گسترده‌ای دارد؛ از طراحی و ساخت «راد ۲» و «راد ۱» و «پارس ۳» و پرتاب ماهواره «پارس ۲»
🔹
ماهواره‌های راد ۱ و ۲ قابلیت تصویربرداری با دقت ۵۰ و ۲۰ متر و کاربرد مدیریت منابع…</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/442758" target="_blank">📅 11:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442757">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj7EXV59GmB05U32wF9KcUEiZaeIhwk0w_AyDENZVQX2elo1HhpbXTrcy8CNzZlB6NMg21zAbQhUcjDgVuyY272K8_LaBVXSUfEyxhOLvcx_VedZALzGxjb0rs_TaO-xQoOJ3UZ18s1ulM4XlsOI6YQcSJnaSEsAWYxXoiqIOA8AaGFuO7axmccu4RWXUbjBMpgx2HYBJjzaqojzQJRfS_vmXotipFrp7LQtjbKqbqqCmqw-J2aB4TP-NM_1sUEv3FCGLr39xmzFmy4q5q33VrQ9eTojBMue8QLHspSBCS1zvUDUdDeLEDULBLigIVxpMVmM7eB1LY_alqOQvTYPFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کف بازار ارز و طلا کجاست؟
🔹
بازار ارز و طلا در روزهای اخیر به‌دلیل کاهش بخشی از ریسک‌های سیاسی و اقتصادی و همچنین افت قیمت جهانی طلا  وارد فاز اصلاحی شده و قیمت‌ها کاهش یافته‌اند.
🔹
با وجود کاهش قیمت‌ها، بسیاری از کارشناسان معتقدند این افت به معنای تغییر روند بلندمدت نیست؛ زیرا عواملی مانند رشد نقدینگی، افزایش پایهٔ پولی، تورم بالا و کسری بودجه همچنان پابرجاست.
دلار
🔹
برخی تحلیلگران محدودهٔ ۱۴۵ تا ۱۵۵ هزار تومان را حمایت مهم دلار می‌دانند و معتقدند در صورت رسیدن قیمت به این ناحیه، احتمال افزایش تقاضا وجود دارد.
طلای ۱۸ عیار
🔹
از دید برخی کارشناسان، محدودهٔ ۱۴ تا ۱۵ میلیون تومان کف مهم قیمت محسوب می‌شود و در سناریوی بدبینانه امکان کاهش تا حدود ۱۴.۲ میلیون تومان نیز مطرح شده است.
سکهٔ امامی
🔹
محدودهٔ ۱۵۵ میلیون تومان به‌عنوان سطح حمایتی مهم معرفی شده و گفته می‌شود حباب سکه نسبت به گذشته کاهش یافته است.
🔹
دربارهٔ نیمهٔ دوم سال نیز این دیدگاه مطرح شده که به‌دلیل افزایش تقاضای ارزی، اثر نقدینگی و کسری بودجه، احتمال شکل‌گیری موج جدید رشد در بازارهای ارز و طلا وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/442757" target="_blank">📅 11:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442756">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSPexPipTl2awoE8MM_06fkO_TXHc2Dsrlrcu0aPwKWcXPlB_h4tVUW1f7jCpyrkPoOAiRbzI6wckVquoZrWEMlCPvvIVLFWuEWjIJI6qL1eJDTO7iURlg2wxBBs4TESqdo8NH_wSqzlQ68_iVlToT2Ur_oYErm7186vrd6g-fbNP5_1Z7uaTL6CbOfUxJ68XGNcPY0hTMDLPoKYZfXbA034FntFjZuPeA_CCmWNOH2jbW99JdK79PIaECabxkQUNVJkn55Y9M_w-fv22KfWsjD9n4ifjSzqJenstfdAT5fGEtOQY4e6yn0aVuiOo-UN1auvYBblEUG2QnpejoC5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد تلویزیون در جام‌جهانی ۲۰۲۶
🔹
براساس نتایج نظرسنجی مرکز «متا» تلویزیون با ۴۸.۳ درصد همچنان اصلی‌ترین رسانه برای دنبال‌کردن مسابقات جام جهانی ۲۰۲۶ است.
🔹
در مقابل، شبکه‌های ماهواره‌ای فارسی‌زبان و خارجی ۱۳.۵ درصد، شبکه‌های اجتماعی ۱۱.۸ درصد و سایت‌ها و خبرگزاری‌های ورزشی ۸.۴ درصد مخاطب دارند. همچنین پلتفرم‌های اینترنتی داخلی ۷.۵ درصد سهم دارند.
🔹
نکته قابل توجه این است که برنامهٔ ۳۶۰ عادل فردوسی‌پور که در بخش «پلتفرم‌ها و برنامه‌های اینترنتی داخلی» قرار می‌گیرد، تنها توسط ۷.۵ درصد از پاسخ‌دهندگان دنبال می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/442756" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442755">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpTfnYP9zTC4b0WQsrBchBozdSToJ5e9miFKeBC6shmYGdynL1L21LPXUvNz23v9OH_xFKxVr_drotsz-Jo8-symYgMEkgABqEyQiIkMFEc-PskTexBLkle4auuqChBdZ1wT_id2X7zsya3K-9lhxYRhx1XQZNxSZOYRo9SXzeBAKfIQF-IVZ3rCk-QZQOIiHcORhtx9pj2QiFbZ_D-oaWLfA80o4kmX1G_Q7gFZXQOYR3_A4QT_5oC9M4RXWJCgDzS6nwRYXxoVBXCz8EiHgrm8aU4U9PglgOmcCDEUQHqwOZ8A0OBK7HTJcJe6Tl0eZ8jM98uckZ6QyT4wa1NAGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: محدودیت منابع، ارادۀ دولت برای خدمت‌رسانی به مردم را متوقف نخواهد کرد
🔹
دولت چهاردهم به‌رغم محدودیت‌های مالی، پیگیری مأموریت‌های خود در حوزۀ سلامت را متوقف نخواهد کرد و با بهره‌گیری از راهکارهای نوآورانه، از جمله جلب مشارکت‌های مردمی و ظرفیت نهادهای…</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/442755" target="_blank">📅 11:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442754">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b576779d05.mp4?token=YxCsA_MC55tu89mYqqxoI013bGbMHqdgDRBZiaKyYzJfaTRK-_-wJ2m6d5Y6lMH8dpS40QaaRvQaeV7mqfBHmhEi9u2zAqBcpt1abFPFnsKYf_2-WwOWZivIxRBj_is35z1DIA5SR8twV--iSLQ4TZJlW99N2H5rN_x7pzjIADcH2BwCK3ejIQOxwOk2oMbJgEBeOG6n1OFx2VL_N07VLU5USEnbI-UW-fPixykIA7DSocV_mVl7IaE34MYEsHT-tvZeANvI5p5V-76Ehf8RAgA3xpufOWmLMKLwD9C2D2z7aASnQaBWr8uYR5BSsguluolWjjRl2MpZBTY_uEAuvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b576779d05.mp4?token=YxCsA_MC55tu89mYqqxoI013bGbMHqdgDRBZiaKyYzJfaTRK-_-wJ2m6d5Y6lMH8dpS40QaaRvQaeV7mqfBHmhEi9u2zAqBcpt1abFPFnsKYf_2-WwOWZivIxRBj_is35z1DIA5SR8twV--iSLQ4TZJlW99N2H5rN_x7pzjIADcH2BwCK3ejIQOxwOk2oMbJgEBeOG6n1OFx2VL_N07VLU5USEnbI-UW-fPixykIA7DSocV_mVl7IaE34MYEsHT-tvZeANvI5p5V-76Ehf8RAgA3xpufOWmLMKLwD9C2D2z7aASnQaBWr8uYR5BSsguluolWjjRl2MpZBTY_uEAuvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کودکان حسینیه از آرزوهای محرم گفتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/442754" target="_blank">📅 11:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442753">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhG6G3jNfCXr9Qo0d1tZ1bX3qkrefN0KQxpWtF4IrmFpAcyeK-5HnAjRSnZWl6-JlpouZzzN5o4xwgipBpfNOLL-_jKr-Z9vOFpqXCfkFl_aaChP0_CxF8jZbQT1KhD6az-SICa2j8k0bWtlbGSYB52lppmBi8yt2v74ohzAZCj7-z3hQ8dVGCEwsHJ37yuidXVZovEr4sewrFz_9V5YWevU8kEriy8q2n5VJ6egyFgFDPNLKqcX0mS7P5hYtsnGb0WGYVl3HtJKAb5LvYYnn39bROGazQoksw1WPHHziJEvLrrrbR3EfVS5QvjLsBq_SL_3FwLchnfqUZROezF6lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ایران باز هم از محاصرهٔ آمریکا خارج شد
🔹
تنکرترکرز براساس پایش سامانهٔ ردیابی کشتی‌ها که با تصاویر ماهواره‌ای هم تایید شده است، می‌گوید «حدود ۳.۸ میلیون بشکه نفت خام ایران از محاصرهٔ آمریکا عبور کرده است.»
🔸
پیش از این ترامپ گفته بود محاصرهٔ دریایی ایران از روز جمعه بعد از امضای تفاهم‌نامه لغو خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/442753" target="_blank">📅 11:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442752">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
حملات هوایی و توپخانه‌ای رژیم صهیونیستی به النبطیه
🔹
المنار لبنان گزارش کرد که دشمن اسرائیلی حملات خود به جنوب لبنان را تشدید کرده و اطراف النبطیه، کفر تبنیت، تپه علی الطاهر، جبل الرفیع، کفرجوز و حاشیه شهر النبطیه را با گلوله‌باران توپخانه‌ای هدف قرار داد. همزمان ۲ حملهٔ هوایی هم اطراف کفر تبنیت و شهرک النبطیه الفوقا را هدف گرفت.
🔹
در همین حال، نیروهای متجاوز صهیونیستی به سمت شهرک حداثا پیشروی کرده و هم‌اکنون در مرکز این شهرک مستقر هستند که این اقدام همزمان با شلیک رگبارهای پراکنده مسلسل صورت گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/442752" target="_blank">📅 11:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442751">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ex0K9V_dQ9unRO-maHiDoBVPyEUVrzTCJhcufpfw1izryyFP0IBtHbDC7i3FIxKCoqnbiZgkFGairI2ZiuPo_I8x0cSSlwRaPJwXB82GLfOr5thSomrkBodCgzNqUcNf3VBCw7y7gmfGu5HJhYSA_WS9lfLpuxVHf3e2_rhrF5lkbCDonFG4XYXYR8cZh8gDZOl_n8Nkl7AV9PiKXm8znJLDqHJuan56OhhMefquXXoyhTxoxQQsjxjqHpEsI49nzSOIJ9m5IDNqRuUVpEB94DeGE7-mOQ6t_wZqetl2WJxLb3czORwGLRh_za5uqkCD1EMmRpwGpt1rztp7Trz5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۳۳ هواپیما از زیر موشک‌ها نجات پیدا کردند
🔹
سازمان هواپیمایی کشور: در جریان جنگ اخیر ۱۳۳ جابه‌جایی هواپیما از فرودگاه‌های امام خمینی(ره) و مهرآباد به فرودگاه‌های امن‌تر انجام شد.
🔹
همچنین ۳۶ مجوز انتقال و گسترش استقرار هواپیماها در فرودگاه‌های خارجی صادر شد که بخشی از آن با موفقیت اجرایی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/442751" target="_blank">📅 11:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442750">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLLMsN-E58VF1EcJDGKfIpshhhAY6r0HaOviOtrUdEz49_5nejSBLcAvTqf1mjB8_rAZcuNmTImfDGgzRGHPbNbQvDV-OYnC22aiwTh9A9cV2xx6v_A7p4eb5ZT8PVeP2Ssa2BuxHreB1A_eJ_i7i0OAfmCyjExD1tnlvO89nQvV9MLPZtenjhs9WTKX6peVx6jJbia73n-sSv-HdfKQQyn9dbj4RdOXcxZCLN_TSIOZnRjjbn5fwlSgzjksmhmGG11bbvAzTqflwCq2PLvdxcb99GY47t9bZDQ8CDMnJl_CmwbLgn7KEAGI9PvwzcPhiIgyJl6u8Q1dqBdquyDuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: محدودیت منابع، ارادۀ دولت برای خدمت‌رسانی به مردم را متوقف نخواهد کرد
🔹
دولت چهاردهم به‌رغم محدودیت‌های مالی، پیگیری مأموریت‌های خود در حوزۀ سلامت را متوقف نخواهد کرد و با بهره‌گیری از راهکارهای نوآورانه، از جمله جلب مشارکت‌های مردمی و ظرفیت نهادهای اجتماعی در سطح محلات، مسیر تحقق عدالت در سلامت را دنبال خواهد کرد.
🔹
در مقاطعی، سیاست‌گذاری‌های حوزه بهداشت و درمان بیش از آنکه مبتنی‌بر عدالت در سلامت و پاسخ‌گویی به نیازهای اقشار آسیب‌پذیر باشد، بر شاخص‌های رشد متمرکز بوده است.
🔹
پیامد چنین رویکردی، افزایش فشار بر گروه‌های محروم و کم‌برخوردار جامعه بود که در بسیاری موارد از دسترسی عادلانه به خدمات سلامت محروم ماندند.
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/442750" target="_blank">📅 11:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442743">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqg2L8Eeiznr52uCo7T-gcRkeoK5ZPqDxgEtv6GaOIA8_B-8l7Z10TC5QidIOtIfmx_hmWxMdhlHkj3t3ZTZRHsKne-Me0UXLsNZsrJKltLBBxyHj1ABReQLlZuGEVjvMzRfcsCjbNk4CKwYvMi2nslfsuwS5qllAeWPTaTKzyzEg0Agu-ahYpoEFCfgr95SrdtsC3QWJdiOMPtVZA2BTObmemUy6P5j0ZhEAUHs0qu6rM2wRXdZpPF1W7xPvjyfbAdGK8EMLZQ0MtF1bZiWGOWSNl1D27VVF5XSD3p5hZR7KtMvnFI1M8Mhrtb_tuE_q9N7JqqaOA8aeNqoqlakTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMGpNbcrVTwp6tl8BiypgkFtKXdJcqsmdsD_kImQeXcIZap4uKd-tvvpP_EccuXbBqbS9dONJIwXG01k1L2YIM_iEf68n9Klh8MPa0lOSvT5DcSyjpnhN1RiIkuOWDoCxTysdCcitkwMdB1u010ZZLOHbWHuOgzj4VEOP-G5RVGHS1YbfzXbHVbesbKrtov4bSomI51kst64UNyMvqLOeHp32z1z9SL71S8ZrZhaJDDxt3k6YMBdy5KFiDLrrewPUXk0bsULCvAF9UFlkv0uBLP4b6PVm0ExlafxUQuCiRDGM2_zIiRjZ7y5ZVK5DodSXZWYQFbRbYCDZ1bEJz7bkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZWcFT9mm6HAXyVCwc8_PcYVhd06q_TahyydZ8NZBR8FKVHYs3R3Ip2M0vZKDjZ7oozFSlqmD8fmX_cpkXnQm9lX7PCezEqs8hJH2PdCipu9L7UNdiWVPQmwja-6JvOk5dlM0RVAxLPCbuKY_8lXRAGb7f16Prljwcmrb_q3g5SwcPGOQHfTFS_vC6vN2GKNYPNYvfKVZYXLyd8B13HTgxk_xrzKjvoKhe32FNk_52z5TUM5QyfddG9iNs1lErGiy-dRFAxWzasTa7TAuJjBv88HhWoSohNUYszFoDS9KVWGlbqCdbJrDBFi39kKHNJi2_c1F1src1vNKleX-xqR_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xb5dUapqDbWmzCLZ8mZAnC4oQD6yPidUS5UkJLrOoMchBxWIqLsWOJFsx97zSYe3gsbpbX9x--q3qx4QCU5mjrZsyqSpqzHd-x0COKb6aP6-O5DKzp9I529DXkHQZOaszOXQgg50oh05Bpx9N4sINBjpKHRlj7pixQbMKE-S9wyZmu4cJzSha6AruKpCyExzIcj1wOqNbXvklfKuYOQjo8_pEO8CieQ6eh_w5YZKCaCXTerOtPYJLdRFa4QzqCecfLWBh0wPSn-E-P_0PZBQINuPiD0gI4vWaiUOiJBYxodTnWqU4kOa9_3DqhvPIV4n8RyZrzI6kQTPUHHAESB0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWsljf0eJb2StvD_v0CxjBNo2O7wQz_C19xtgzWfIa9gUluFKDPBvzJsxymUsNY5ub3Z0mVujowLAagJggzeDbEg7S54M0QiNB-JIsvfaKmEB_6QaVjsyTNyo2HscWAOvc0U17vJW4pO_KkWD-aQOpwvQAH6g30hrBtgBl-za74QTv_XyRB4-eRe8tiNfnnubcu8aFve-0R63S8KGifreAYamPU0vi7cYp2Cb3_LZ62b2DAldFvVZXcYHXvuRazn2cOHM5yTDQIKO86jtdAf8IaW9M-yrMvbPQ9Bk23a6b68kp2ZtQ5DJ4hkomjHu13q0gxQRuPI6zjCflxxaNXsaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UnupWM1vVZ7CNBcrsFkYoZXGbe9iF6F1ffMWBBc_uB2vbDZ9dL_tqvgA69MzBWbzWCrwGNBHUV6-Bb0IxOsIlFSZLk0eWYMND46rjgVoCe4EQZ8qAajRLlbIgBOkjjXdwlg4Uks5xKTl5Lo6FmO1r7bi2IYRI1XoZXXt3doWSRpTdeLDD68SOjI-rvQzAASxDuU5GsgVZI_sIend_vGoec1B0RSYssibhH5H31j6q0lJ-lFEKiz-O18MZU8qK6bkyvKq2puCgKLolZavd_TLCbss3NIBG0Vqz7jlUdDKXl9vQa1w7-GJyEM8qlp9XdKkA7ZkjNjrRg4iu3b13Lt__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufi8mIZWJ1K38huwCHPXZ0BxwXAjGkXvIMPfPN_H-gbkV220UnhYzzBbKGK40jbL-YsrEAjrZiocKtzhmhUMUhC3Rlvtc0SMcZXpQ9CtHuPIH_LSGkpFdakUC0xF4nNV0i-9dgWU2xbbk7N9H2I7uNlkD-HSqDBDVTfiwx_pqzPoCxA1NVWj2fBqYTEvrz58RbvZ9odW6gZN8K41KKxvnR5TlBrH0DSkd1DEY6_EOic1K7rIlPbCZos2wXqxoES2WOqWjkEfvWVjAvIdOidHu2-s1L1Ffw3Jcz78fA2RM430dfKj_p7I_05h6kzFN08QZOH8PxBBF6heggzCHiZ7yQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هیئت آیین حسینی در میدان ونک
تهران
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/442743" target="_blank">📅 11:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442742">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تداوم انفجارهای کنترل‌شده در شرق و جنوب اصفهان
🔹
مدیریت بحران استانداری اصفهان: انفجارهای کنترل شده مرتبط با مهمات عمل‌نکرده در جنگ رمضان در محدوده صفه، شرق و نیز جنوب شهر اصفهان و بهارستان امروز تا ساعت ۱۴ انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/442742" target="_blank">📅 11:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442741">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a719775f79.mp4?token=dRPa2SDZC19wVa07z-KPLDtREl6DSfqU2y1wZbWBYwc4omg0E34OUn5hDVdIVygt0-Q9Mr-HOMk1W0QM-ksMEQQyAnhZqOPIqaj6ghKQm-iflNHz7CX1Pbfky6XhRDsaVHAI-BIm4uqA75M3yqInkXBz6gG8AHNiYJrX9gIMPRn6HLGTOFU1xx-MTIwKsZlgJPb4uLmZoHVIUL9xQDqkP23vuH0-LBmVn7SxzGwckFqyhIQRmav8Lvk8sbr3v5zCM2mzBDWRHY2eD2EWOXjgE-vN2DySqBRiYAxRzFXMfU5AB5HNIrSwWUOd1ohPHiOeyXYfdU2jS_alx9W8ngrhrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a719775f79.mp4?token=dRPa2SDZC19wVa07z-KPLDtREl6DSfqU2y1wZbWBYwc4omg0E34OUn5hDVdIVygt0-Q9Mr-HOMk1W0QM-ksMEQQyAnhZqOPIqaj6ghKQm-iflNHz7CX1Pbfky6XhRDsaVHAI-BIm4uqA75M3yqInkXBz6gG8AHNiYJrX9gIMPRn6HLGTOFU1xx-MTIwKsZlgJPb4uLmZoHVIUL9xQDqkP23vuH0-LBmVn7SxzGwckFqyhIQRmav8Lvk8sbr3v5zCM2mzBDWRHY2eD2EWOXjgE-vN2DySqBRiYAxRzFXMfU5AB5HNIrSwWUOd1ohPHiOeyXYfdU2jS_alx9W8ngrhrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرۀ آهنگران از واسطه‌گری رهبر شهید برای یک ازدواج در جنگ ۸ ساله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/442741" target="_blank">📅 11:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442740">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axyI1tCN7QBl5QSIN_pCXPOxOHKBjwuPT44J4KSQto5Eg0tq6v35O4poNnNe6kjfKQdzM0P5x8Z_e1NCmIEh2YyMEqiWC36ORfQwIj70Gs6IXNl9tjMGmYFmBgDfXuOdbJMXhttTceEBlsDTEOcGonie9J1VABeMNodlvy6DSR5cmbmnRyKJeU7NdYZXvO0lqv17jeKCtwCJxaUWpyCrBTwLJCOaze0bc-iWZwP0OrNddk6-JiUdJH2dbWbCssGWyofse7l74l_DwsocvKKAZCvb3ZJRI1_M1FiAsVkv8fm4ncXY4SGSrVd2oHW_cREDztyqKdPN-5swAKxkp_laGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رحمتی سرمربی خیبر شد  سید مهدی رحمتی سرمربی فصل گذشته تیم فوتبال شمس‌آذر قزوین، پس از جلسه با مسعود عبدی، به عنوان سرمربی تیم فوتبال خیبر خرم‌آباد انتخاب شد. @Sportfars</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/442740" target="_blank">📅 11:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442738">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77e1c26547.mp4?token=rYylkbqcWnizMMrFLYgFLm1eK2yjtDvXwvYW--g6sU9cemfKM0epRcHTVnnYheU5b0cx6040EC83AoY3QRbDPkizD4MzkBk88i2CERohBoqw78IbMCPvXh2E6_8w2m5qAK1PEX_rfN3ycyd3praisODtw2uMgvj_gKLsa6rPL6yGPLBOfRw6luMTg3apgUmARjly-sHZ99ZaEPtjWXDmR7vzcc6bGm-1GwN6bEXlUkeUwVSrcz4m4lpUg1WfJuPjF8gK1meEVV-rnZWlUwyINph9zU1LQnb9QDPjcApxvPvLftS9UYyF5NOFisFkESgDD5QMeWieEuAPwXHZbxxDhJhpqtEkbW_Q6sFax5XjJkfYVbte5FcEBRDk1oQ2JUrOawP7ExwqjdFakg1KB8PJ04n8A93k1WJi3NbVs6ZAbrGT7oLXkMjybojRVaJEOShrUdhCOclAiR-TB42r-nv1BbQm1uUI16RZnH__OL3HgqzoqJiheu6NZm9nVwYh0fSluZuvv2ss12G8TWxME1gi4URLcyJHwnsM3cYDhNO7SSB-4PJmMy9Y5ZLUVFyzmF1YaXPZ_HbQXQnhmKXETU1Hei-Ws5eC1S4v9d2wgFvocGaCenwViDLtJQ7dpG1LQ6fZxzhbyfF-Bd8DRPfTEE2Dg0Oq5h6M0mZhxo-HnCyQyKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77e1c26547.mp4?token=rYylkbqcWnizMMrFLYgFLm1eK2yjtDvXwvYW--g6sU9cemfKM0epRcHTVnnYheU5b0cx6040EC83AoY3QRbDPkizD4MzkBk88i2CERohBoqw78IbMCPvXh2E6_8w2m5qAK1PEX_rfN3ycyd3praisODtw2uMgvj_gKLsa6rPL6yGPLBOfRw6luMTg3apgUmARjly-sHZ99ZaEPtjWXDmR7vzcc6bGm-1GwN6bEXlUkeUwVSrcz4m4lpUg1WfJuPjF8gK1meEVV-rnZWlUwyINph9zU1LQnb9QDPjcApxvPvLftS9UYyF5NOFisFkESgDD5QMeWieEuAPwXHZbxxDhJhpqtEkbW_Q6sFax5XjJkfYVbte5FcEBRDk1oQ2JUrOawP7ExwqjdFakg1KB8PJ04n8A93k1WJi3NbVs6ZAbrGT7oLXkMjybojRVaJEOShrUdhCOclAiR-TB42r-nv1BbQm1uUI16RZnH__OL3HgqzoqJiheu6NZm9nVwYh0fSluZuvv2ss12G8TWxME1gi4URLcyJHwnsM3cYDhNO7SSB-4PJmMy9Y5ZLUVFyzmF1YaXPZ_HbQXQnhmKXETU1Hei-Ws5eC1S4v9d2wgFvocGaCenwViDLtJQ7dpG1LQ6fZxzhbyfF-Bd8DRPfTEE2Dg0Oq5h6M0mZhxo-HnCyQyKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراف به شکست از قلب تلویزیون موساد
🔹
مهدوی‌آزاد: ترامپ مجبور شد امتیازات زیادی به جمهوری اسلامی بدهد؛ یعنی کمپین فشار حداکثری، تحریم و... کشک!
🔹
نوری‌زاده: ترامپ بدتر از کارتر در برابر ایران زانو زد؛ او خیانت کرد!
@Farsna</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/442738" target="_blank">📅 11:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442737">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311cd4ff7d.mp4?token=Ix9_Xz4UYRQLjOiDLBHnJYPb3ra4d57kSZM4Rp2FoL257rUCxFD-s3S7hIC8t8xCeDmSdMS3c-FFhkBSfwfcD3ravi8f6pSeuxa80gVWlF_wFt3Dfb1yCkLD9ZR2tAPatMpdWMJgqGxrvb-4rKZF56S4Qa2lS4VsF4CApAXCwIqYEy18QEQ7_4dnyCDQKKwToLRwjPw9og8TmfFufedDTUWM56b61XEIQaAkbJwMnPpFFS5uUOxHV7xe9Ap1Nu5mF3p3KxjyHztOflIvi5e1HfLFrJIVp26lPJcD431qA88JlwAiorLkhQicjyJ2Mkca1o3gS8Wu_yS9PDe62OFNjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311cd4ff7d.mp4?token=Ix9_Xz4UYRQLjOiDLBHnJYPb3ra4d57kSZM4Rp2FoL257rUCxFD-s3S7hIC8t8xCeDmSdMS3c-FFhkBSfwfcD3ravi8f6pSeuxa80gVWlF_wFt3Dfb1yCkLD9ZR2tAPatMpdWMJgqGxrvb-4rKZF56S4Qa2lS4VsF4CApAXCwIqYEy18QEQ7_4dnyCDQKKwToLRwjPw9og8TmfFufedDTUWM56b61XEIQaAkbJwMnPpFFS5uUOxHV7xe9Ap1Nu5mF3p3KxjyHztOflIvi5e1HfLFrJIVp26lPJcD431qA88JlwAiorLkhQicjyJ2Mkca1o3gS8Wu_yS9PDe62OFNjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قهرمان‌ها همیشه شنل ندارند؛
بعضی وقت‌ها فقط با چند انتخاب درست، مسیر بهتری برای آینده می‌سازند.
این انیمیشن جذاب را ببینید و با مدیریت مصرف بنزین، همراه حرکت به سوی فردایی بهتر باشید.
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/442737" target="_blank">📅 11:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442736">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgrWESihkexDx2OL4zWfoiYmXZMDpoNq1WuB-7BnFk9PBDQvZkor7KRbcEprqdUcdkbHVpt9tM-r2K67ou1EYJX95541s5E7c-zXV1D1J6EXRFMMWDTgupP_vk1rHSiUfowgTChUo-o71jd9b6gnAiYb8pS-zxGpBU4bxYpDLmpKcJkN3XcpiiY-9W3XNSX3qKbxLxIp4gVBU94xXiuUZqrebcEmZmIPahIL5ai2ufjlLmBEsKHly5B63ZYbHsC72KQvv44fCXmWMRM5cuAFKKhRmwaYqu_IJEn5iufyqdhbCBOauEuQiWTUTT_dS93IgjiYqZLil0KgWKRhbFnpjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
بالمیل‌های ۷۳۰ تنی تغلیظ مس به سونگون رسیدند
🔰
مس ایران در مسیر جهش بزرگ تولیدی
🔻
پوسته بالمیل‌های طرح توسعه‌ای فاز۳ تغلیظ مجتمع مس سونگون با مجموع وزن ۷۳۰ تن، پس از طی بیش از ۱۹۰۰ کیلومتر از بندرعباس تا آذربایجان شرقی، به محل اجرای پروژه منتقل شد.
🔹
این عملیات پیچیده در شرایط ویژه کشور که طی ۴۸ روز و با استفاده از ۱۰ دستگاه کشنده فوق‌سنگین انجام شد، به‌دلیل ابعاد و وزن قابل‌توجه تجهیزات، ازجمله جابه‌جایی‌های کم‌سابقه بارهای فوق‌سنگین در کشور به‌شمار می‌رود.
🔹
بالمیل‌های فاز۳ تغلیظ سونگون از تجهیزات راهبردی مدار خردایش هستند که هریک با توان ۲۱ مگاوات، پس از نصب و راه‌اندازی به بزرگ‌ترین بالمیل‌های مورد استفاده در کارخانه‌های تغلیظ کشور تبدیل خواهند شد.
⬅️
ادامه خبر در مس‌پرس
https://mespress.ir/x6R8
⬅️
فیلم انتقال بالمیل‌های ۷۳۰ تنی مجتمع مس سونگون را در لینک زیر ببینید:
https://mespress.ir/x6R7
@mespress_ir</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/442736" target="_blank">📅 10:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442735">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/442735" target="_blank">📅 10:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442733">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7R3YMPI9x7xj1nGTUvnuFI4318oDc2W8m8w2nuoAf-0eaUmPdK-YfshjtgIoMq11TF731xj4p2tu4Gi1zwPaf6cyY_o2m-v4EVR0RTf5UB0m3B1crdiEW7tMgIeJteyHZK1mAzCITm9qtz5KFPmw-UKjf-sZxlzSkCqpT1hnyIxI2vi2D2y-_vJ-dK3YgGQmolM4VLjDnUxQSw79SpKZQpLd5deLxSNEcd49nygwxyiG6aDAph3CX9XpshJuS1HxlHm4VJ3zjBLDuTxlJKNocNoOXvslXO-XkS5KsyTNOOhNXMsegglU2ngbbUO78qF9GR16XnE1Zg2fawtFUd6Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umjo2AJUGvC_R-4IVfgacWHC43L1UDXXMJAWzAxq7tAYvWFZaPuNSKl10e4Q_IwngC1Ub6oV_6r2Obhao42YFVVOQ6mAdRoySDKMIhSMbA0IyiPHvYSuDo216j_d3KVHLR6_iEcH17J-ZVtufVexpM5yamBxtobA4EYuUDAVGO7koJ7Qbk6dDhib3EvHbnU3axW0XjEIEFD92sThZ3IBd0LXErLBaupZXtuqLYFejV7FkAXse83_f9IjDFBEL9QbZZxjfEgQKyLmOL7E6Jpw77kQrMmwu0bG1qQ3HaG0ITMCz7tG6nWbHKuu7g84rZTcfRSAduH5k7CQXON7abwYCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نشست هم‌فکری قالیباف با اتاق بازرگانی
🔹
نشست هم‌فکری نمایندۀ ویژۀ ایران در امور چین با اتاق بازرگانی، با هدف ارتقای همکاری پایدار اقتصادی تهران  و پکن برگزار شد.
🔹
پس از جلسۀ دو هفتۀ پیش وزرای اقتصادی دولت با نمایندۀ ویژۀ کشورمان در امور چین، نشست امروز دومین دیدار قالیباف در حوزۀ مسائل مرتبط با ارتقای روابط تهران و پکن است.
🔹
در این نشست  راهکارهای ایجاد و ارتقای همکاری‌های پایدار اقتصادی، دستیابی به نتایج ملموس و عینی در روابط دو کشور، نقش‌آفرینی ایران در ابتکار «کمربند-جاده» و مسائل مرتبط مورد بحث قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442733" target="_blank">📅 10:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442732">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f22e9fd16c.mp4?token=oTDVpxQ8Hb7svXCddVAajnzf2WfDbs9rmNonafm5BSQoViO1lRBR1I0IRFTJInB0fyEoYxof9VppUjzs5sXc_S56_RxLt-jELGJdSBNnvRUmLW81Q5fykvHrXHIDCCns4s00ZdjxaHuGJZpvgPCtImRWRdIM7vI67xjrYtRt-RFZerUv5HO6nEDathXw3Mde1h3RZx9PUS_ITB_FF84C3_eUNOq6gf5jaTZ-2xMg8e-a8ZFiawvmW90-6WE4Y2AYQq1_K5a_UJNHAuPHAfuGMCAT_jOvxTgJJlxuamp-KIUF_0IJN7iYkAjHSiqZr4QzKg3kGjo6U4dpmzVSd9p3SIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f22e9fd16c.mp4?token=oTDVpxQ8Hb7svXCddVAajnzf2WfDbs9rmNonafm5BSQoViO1lRBR1I0IRFTJInB0fyEoYxof9VppUjzs5sXc_S56_RxLt-jELGJdSBNnvRUmLW81Q5fykvHrXHIDCCns4s00ZdjxaHuGJZpvgPCtImRWRdIM7vI67xjrYtRt-RFZerUv5HO6nEDathXw3Mde1h3RZx9PUS_ITB_FF84C3_eUNOq6gf5jaTZ-2xMg8e-a8ZFiawvmW90-6WE4Y2AYQq1_K5a_UJNHAuPHAfuGMCAT_jOvxTgJJlxuamp-KIUF_0IJN7iYkAjHSiqZr4QzKg3kGjo6U4dpmzVSd9p3SIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تظاهرات مجدد حریدی‌ها علیه خدمت نظامی
🔹
رسانه‌های صهیونیستی از تظاهرات، بستن مسیرها و ایجاد آشوب توسط حریدی‌ها خبر دادند. شبکهٔ ۱۲ رژیم صهیونیستی گزارش کرده که تظاهرکنندگان حریدی در اعتراض به بازداشت یکی از حریدی‌ها بعداز فرار از خدمت نظامی دست به تظاهرات زده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/442732" target="_blank">📅 10:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442731">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1NY1hPUZHS_vxsBrQqL8h95P6pI2UZRFvyfah2WmOEn4xs9x_mh1d0xtmLonbsZ-OHVgREkSgyrTLa9BQBqdbDX5O5H3rnKBUiadLR6w60AtO1-wAZQbb_lOc0unfN8vr6rEHlW2-sW1WnxxQaLCjzWw_0qSvB7TQFDWvnw78SaXNNA6DltQFYv-ngkeMgBIEk7q7x05PlnnEAffRIylDCFpYaC6HYJs6-gFIeddi1hrJBPhnTZMVQ-hEIVY27Uxn3p_LXHseBbw-ZimhUA3vZiePt9YziUtfW9U4X1rsk140kUD5UguGghBtUWZuh1QG_-TfEqCZp9u2KudpuS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط‌ونشان مدافع قهرمانی برای رقبا مسی را دارید؟ غم ندارید هت‌تریک در ۳۹ سالگی جاودانگی در ۲۰۲۶  آرژانتین ۳ - ۰ الجزایر @Sportfars</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442731" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442729">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3734eadb8c.mp4?token=n5qAShr3fUBoIX9HECFDT19bNx_5jxrmzcyUwGSxkeOfodpG1n3XRncpSD61EB876EgVfyXH0pJfZUzsfqoN1Sqtbv5Ze5DzORkJBmbAfMAAwHpuOcDDI2F3kwA0FIWs0ICp03r_IoiS0t23iRmpHpG2gp2fDGbH0mCcS1fMHJkt5FjO7fpqADGlTPOgpq9OrQQ2-bAn8D38qC-1JbHAnEDN_rA3ARSJi9kjloPLXs3XMJO1huOvQqDFkHkD1AfOTDqxaub7tkX12eIHEq5AuJPugZTVPM_7pVIO5mSBSZqmxorTSxhEz0EyWi60FQuFNhwzXdqq8FPAlZBUuYn5ZLgY5OdG4fMZFzrYDxdqe_uxj7Ohv3hnPjKkzy8XZsArngmf0ya4mDI8tiB1olKYM-VMrbw4ff7vP9Q9TQk8c8yxxFgP4DsEh5zHNeOVdSOyY1IgCAUt1x1xc5STQQNZEtzLK9sDOLP3S_4Mw2CVzOeJFzY4c1EnFO6POVppY_uQpChLxQJ0qqVbyMQbvahmJODzsnZy373R-pacs3xIkPbvFSS8KEvfH1-nJ_zVuV8vtgYoesAdNexxlvMYSAKjP0elDYRLtdKur3IfahWclziQm9NIyiH89f8TzMQkt5GzTfiZG42Jcl1kbDJkMwzt4-C-VPLhw8iBgDo6oukHWmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3734eadb8c.mp4?token=n5qAShr3fUBoIX9HECFDT19bNx_5jxrmzcyUwGSxkeOfodpG1n3XRncpSD61EB876EgVfyXH0pJfZUzsfqoN1Sqtbv5Ze5DzORkJBmbAfMAAwHpuOcDDI2F3kwA0FIWs0ICp03r_IoiS0t23iRmpHpG2gp2fDGbH0mCcS1fMHJkt5FjO7fpqADGlTPOgpq9OrQQ2-bAn8D38qC-1JbHAnEDN_rA3ARSJi9kjloPLXs3XMJO1huOvQqDFkHkD1AfOTDqxaub7tkX12eIHEq5AuJPugZTVPM_7pVIO5mSBSZqmxorTSxhEz0EyWi60FQuFNhwzXdqq8FPAlZBUuYn5ZLgY5OdG4fMZFzrYDxdqe_uxj7Ohv3hnPjKkzy8XZsArngmf0ya4mDI8tiB1olKYM-VMrbw4ff7vP9Q9TQk8c8yxxFgP4DsEh5zHNeOVdSOyY1IgCAUt1x1xc5STQQNZEtzLK9sDOLP3S_4Mw2CVzOeJFzY4c1EnFO6POVppY_uQpChLxQJ0qqVbyMQbvahmJODzsnZy373R-pacs3xIkPbvFSS8KEvfH1-nJ_zVuV8vtgYoesAdNexxlvMYSAKjP0elDYRLtdKur3IfahWclziQm9NIyiH89f8TzMQkt5GzTfiZG42Jcl1kbDJkMwzt4-C-VPLhw8iBgDo6oukHWmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار مهیب جت شخصی در تگزاس با دست‌کم یک کشته
🔹
یک هواپیمای شخصی دقایقی پس‌از ورود به تگزاس آمریکا دچار انفجار مهیب شد که علت آن مشخص نیست و دست‌کم یک نفر در این انفجار کشته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/442729" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442726">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127290f528.mp4?token=ZV32K1nBwYBCvvONRJGOP54yamTrT8-k-mIAtstwcYjyalQwjnr0Ea3De20b7CEU8uR-SgIAS2mD8NqY4Ul8iHoQrnuer4fnXeq9mVTdChPpJohPtC4sSFbfK54SrF_Td-KsH-8ZUT6GfBQ_wY12tMSuoW1FZSc4GQLn_Wm_mLLOhh88pv65X_G6U95dxAmfbd5sXmA05mLcW1qWyodm0WcOO9jNuZauuhp9tw3iVnyUXA_YUoS4TBLXpy5hKxtd3gmtHDj21j0q2MLsslmASpLSxPDYsOS3hBFK5UvVYTk18RN5tmLu5hn9rqgdmD5BbkS2M7nxx_ivLrcsfDdwVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127290f528.mp4?token=ZV32K1nBwYBCvvONRJGOP54yamTrT8-k-mIAtstwcYjyalQwjnr0Ea3De20b7CEU8uR-SgIAS2mD8NqY4Ul8iHoQrnuer4fnXeq9mVTdChPpJohPtC4sSFbfK54SrF_Td-KsH-8ZUT6GfBQ_wY12tMSuoW1FZSc4GQLn_Wm_mLLOhh88pv65X_G6U95dxAmfbd5sXmA05mLcW1qWyodm0WcOO9jNuZauuhp9tw3iVnyUXA_YUoS4TBLXpy5hKxtd3gmtHDj21j0q2MLsslmASpLSxPDYsOS3hBFK5UvVYTk18RN5tmLu5hn9rqgdmD5BbkS2M7nxx_ivLrcsfDdwVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم گنبد حرم امام حسین (ع) تعویض شد
🔹
شب گذشته هم‌زمان با شب اول محرم در کربلا، پرچم حرم امام حسین و حضرت عباس علیهم‌السلام تعویض شد.
🔹
علاوه‌بر تغییر رنگ چراغ‌های حرم کربلا از سبز به رنگ خون، چراغ‌های بین‌الحرمین هم برای عزاداری سیدالشهدا قرمز شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/442726" target="_blank">📅 09:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442725">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آغاز فروش بلیت قطارهای تیرماه
🔹
فروش بلیت تمامی قطار برای سفرهای تیرماه در سامانهٔ
raja.ir
و سکوهای مجاز فروش آغاز شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442725" target="_blank">📅 08:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442724">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
تداوم حملات رژیم صهیونیستی به جنوب لبنان
🔹
منابع عربی: رژیم صهیونیستی حومۀ شهرک نبطیه‌الفوقا در جنوب لبنان را هدف حملات قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442724" target="_blank">📅 08:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442723">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUB-3YfSxLxz12zB-qjTTY4vGqhZ43ubaOkNrdDE74dXAuUd-Zkg08rItHvzoOYUS65syB6U5ouFDngMETgHyaK-d0tmo2OqcSWa2ARpXF7v1WlzrDPZwaqHNs05MDoQWE7mVUE2YYbYlL3prLqEYl44bNv5jVDmBpTUUw4YypPGGejVgsSjfX5TwKonXv57vMq1NYXZ7iVr2PyPnvq2bw9MhAbAPKds7zuA8mGGbJJrSw_oDAuxIPkVvEZCHH3_fQG8IHKKXnhZlJaDHZ6wp3EBqJo7kJC_issmmBvS4d3sO3ikZu7pqFCjhQWv3CFNzjESIa4y_DAQDeOzVyyaxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح تکثیر یوز در اسارت؛ یک دهه انتظار بی‌نتیجه
🔹
طرح تکثیر یوزپلنگ ایرانی در اسارت از سال ۱۳۹۴ با انتقال «کوشکی» و «دلبر» به پارک پردیسان آغاز شد. هدف این برنامه جلوگیری از کاهش جمعیت یوز آسیایی و افزایش تعداد این گونه در معرض انقراض بود.
🔹
با وجود چند سال تلاش، برنامه در مراحل نخست به نتیجه مشخصی نرسید و تکثیر این دو یوز در اسارت موفقیت‌آمیز نبود.
🔹
۷ سال پس از آغاز پروژه، سه توله یوز در قالب این طرح متولد شدند؛ رخدادی که امیدها برای احیای جمعیت یوز ایرانی را افزایش داد.
🔹
اما این موفقیت کوتاه‌مدت بود و هر سه توله تلف شدند؛ موضوعی که انتقادها نسبت به نحوه اجرای پروژه را تشدید کرد.
🔹
ظهرابی، معاون سازمان حفاظت محیط‌زیست به فارس اعلام کرده کمبود تجربه، ضعف امکانات، مشکلات فرایند زایمان و نبود آمادگی کافی از عوامل اصلی تلف شدن این توله‌ها بودند.
🔹
این نخستین‌بار نبود که مسئولان سازمان حفاظت محیط زیست به وجود کاستی‌ها در اجرای پروژه اشاره می‌کردند.
🔹
یکی از مسئولان پیشین سازمان حفاظت محیط‌زیست با انتقاد از سیاست تکثیر یوزپلنگ آسیایی در اسارت، این رویکرد را برای شرایط فعلی ایران ناکارآمد دانست و به فارس گفت که چنین برنامه‌ای در نهایت کمکی به احیای جمعیت یوزپلنگ در طبیعت نخواهد کرد.
🔹
اکنون و پس از گذشت نزدیک به یک دهه از آغاز طرح تکثیر یوز در اسارت، ارزیابی نتایج نشان می‌دهد که این پروژه هنوز به هدف اصلی خود یعنی ایجاد یک جمعیت پایدار از یوزهای متولدشده در اسارت دست پیدا نکرده است. با توجه به نتایج به‌دست‌آمده، به نظر می‌رسد ادامه پروژه تکثیر یوز در اسارت نیازمند بازنگری جدی و اتخاذ رویکردی تازه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/442723" target="_blank">📅 07:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442722">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رگبار باران و رعدوبرق در ۸ استان نیمۀ شمالی کشور
🔹
هواشناسی: امروز چهارشنبه در شمال استان‌های آذربایجان‌غربی، آذربایجان‌شرقی، اردبیل، گیلان، مازندران، ارتفاعات البرز مرکزی، خراسان‌رضوی، شرق و شمال خراسان‌شمالی و برخی نقاط خراسان جنوبی، رگبار و رعدوبرق، وزش‌باد شدید، خیزش گردوخاک و در مناطق مستعد تگرگ پیش‌بینی می‌شود.
🔹
همچنین آسمان تهران صاف، و در برخی ساعت‌ها احتمال افزایش وزش‌باد و گردوخاک پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442722" target="_blank">📅 07:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442721">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6789100e6.mp4?token=Yw3RGD4Aa4bI1VyJXIdJFxuMI2tkMzSF7aFxTT-vjqcmNPNRLQuk6dikkBVk8KEhqdlTlHdsELPPle2_-yULkwwz5lYz3XyIBSFHQ2sYjxhALaKduPO44C0pwbFRrNZFBI88C8wxAn7JM-WnLnkA5AC4UkaljfDcXiHGmVrqVzjS856iEIOBsKNNkZgEDH-PmOFSizvV0Z5LMPkBCvYmgtktVtOkbR_qquVIUEQAx7ii0vO_ytGS6cD6xngpqDh6ZJ0mX3C8VozfRFJK2EVRutEtDnJJvhe152h6w3F7pAzPsYuWKzgiCCL5MX5kT7l8YB6LoFJ5B_f7fvTDx5kHsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6789100e6.mp4?token=Yw3RGD4Aa4bI1VyJXIdJFxuMI2tkMzSF7aFxTT-vjqcmNPNRLQuk6dikkBVk8KEhqdlTlHdsELPPle2_-yULkwwz5lYz3XyIBSFHQ2sYjxhALaKduPO44C0pwbFRrNZFBI88C8wxAn7JM-WnLnkA5AC4UkaljfDcXiHGmVrqVzjS856iEIOBsKNNkZgEDH-PmOFSizvV0Z5LMPkBCvYmgtktVtOkbR_qquVIUEQAx7ii0vO_ytGS6cD6xngpqDh6ZJ0mX3C8VozfRFJK2EVRutEtDnJJvhe152h6w3F7pAzPsYuWKzgiCCL5MX5kT7l8YB6LoFJ5B_f7fvTDx5kHsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ مرگبار آمریکا به یک قایق دیگر در شرق اقیانوس آرام
🔹
فرماندهی جنوبی ارتش آمریکا از حملۀ مرگبار به یک شناور در آب‌های شرق اقیانوس آرام خبر داد؛ اقدامی که در ادامۀ سیاست بهانه‌جویانۀ «جنگ با مواد مخدر»، جان یک سرنشین را گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442721" target="_blank">📅 07:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442720">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c7af5c063.mp4?token=G0mSk4o8XtcR6ZVtja86ayfHVJ-1Jy7k_aKbAcieqlxx6zU72DPg93GtYyV2a85-_EAgaBi-rS2ffxvq1TTHdzYn6qAELWwTVOgnd2PLm2PmcLpfdVy29TBOzcXCkI30YyH1NQTIlFez1EPzPkTK5tkpbp-nLLz9EcMiGE4kXQ21wknpe6k1TPQTFtE6D3uigcZ7F2_Jw7qbGNvHSpcecAjTLRfowzl5O_1dnWyslwT8z4tpLUzvzQofJyrePIw-g-_yxUNZ2kM9-ItKMAH35ZmMa1cOf7KXOinPDasLOBis8guhOUdFoiQ9ca0jJi_eWyplH8uRxIPusoRk-R2BvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c7af5c063.mp4?token=G0mSk4o8XtcR6ZVtja86ayfHVJ-1Jy7k_aKbAcieqlxx6zU72DPg93GtYyV2a85-_EAgaBi-rS2ffxvq1TTHdzYn6qAELWwTVOgnd2PLm2PmcLpfdVy29TBOzcXCkI30YyH1NQTIlFez1EPzPkTK5tkpbp-nLLz9EcMiGE4kXQ21wknpe6k1TPQTFtE6D3uigcZ7F2_Jw7qbGNvHSpcecAjTLRfowzl5O_1dnWyslwT8z4tpLUzvzQofJyrePIw-g-_yxUNZ2kM9-ItKMAH35ZmMa1cOf7KXOinPDasLOBis8guhOUdFoiQ9ca0jJi_eWyplH8uRxIPusoRk-R2BvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاهده ۵ عضو جدید خانوادهٔ گورخرهای ایرانی در پارک ملی کویر استان سمنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442720" target="_blank">📅 07:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442719">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADRKu4GZ4A9AohhnrQIb_rRHt36mDIq4JHBY9zavcuHUPqKtO3DgA0eCERDc7_wCUNpEauDiIREzNaE10cGHAHNTQLQE3oY_CyqckZ6cE13NzbX67d7El0kBhlDO86uzcG1HYXCCst8pg_bmmBFwGfo7MJntfDZOY0luB29ImGwylZBfqYOSJGyQzuZzD3s6YAi4_K4aB1Rj70mrA6taV95hfbzil0Pa-DSQKv_CjpUx8YcWOFY7wybXVb_R39EK721GK8PCCiOPxFM2qAYQbHKFnI8dFwBQ5M1WsQfQ4UVyksc-7rx5Cl9bUpkKCD7KgE5pf2-OMQbi3No6BM6wYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط‌ونشان مدافع قهرمانی برای رقبا
مسی را دارید؟ غم ندارید
هت‌تریک در ۳۹ سالگی
جاودانگی در ۲۰۲۶
آرژانتین ۳ - ۰ الجزایر
@Sportfars</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/442719" target="_blank">📅 06:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442718">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0b2908cb.mp4?token=rK0bq4Q9nydqPrd3TA-yBW99ee8ZXUlu6EtlIS6Wvk_t1W5kj4svCqybM5cdpNsTEXBZNgNJbh_JVyCaUNnNShvJr4cQCPPz8iqXgwftrD51GxY-ANiASZfCwzxdjpadnZMzdHnPk7FQ91uwtgmEf_Fy9VJiKY8tTPyFeHQ34HWmGGFnG48xHNon5gUSh6IkefoVa0JQCzUnBDWi7yHKr5G_lCN_kwvsCqPnOFJWUjUHn8ULzUGH5eYeLR3sp1L_l3ftoOVTJE9XwLRnT7Q8f6w3QICdL0cpjjl6_3rLhoSF5gNCYI1tGcsJfCZMjf25yZT_dfvHttS1XumXrQ-uug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0b2908cb.mp4?token=rK0bq4Q9nydqPrd3TA-yBW99ee8ZXUlu6EtlIS6Wvk_t1W5kj4svCqybM5cdpNsTEXBZNgNJbh_JVyCaUNnNShvJr4cQCPPz8iqXgwftrD51GxY-ANiASZfCwzxdjpadnZMzdHnPk7FQ91uwtgmEf_Fy9VJiKY8tTPyFeHQ34HWmGGFnG48xHNon5gUSh6IkefoVa0JQCzUnBDWi7yHKr5G_lCN_kwvsCqPnOFJWUjUHn8ULzUGH5eYeLR3sp1L_l3ftoOVTJE9XwLRnT7Q8f6w3QICdL0cpjjl6_3rLhoSF5gNCYI1tGcsJfCZMjf25yZT_dfvHttS1XumXrQ-uug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم مسی به الجزایر
⚽️
آرژانتین ۳ - ۰ الجزایر
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442718" target="_blank">📅 06:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442717">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe038a8e7.mp4?token=T4nc1BGnCiBZCWl1eEY43O3ZGvxxTH0UXQnJjK0Ic2_9lcXQ_KUueyeBVd7MRiQHzA_jcXAZqqxNl_pOaueXVfOSfhTZMSnBEiXmEodzujhVCATolPv0L1hFw6G_qzYqEs-SSY1tKcHtymtyBKUhWYFJpN8GqBtPGb9nUmiwSi999eVNxMsvixcjy4pH2WjwTbTNOjpHMXdzTjy65g4GuMj6gGQfVUM9m1RiadtDOz936iQPPzVJ63lxKajn-wOeuEwnIXFfa_EtvxF30zbJjOdGsgUqgZ_Irq99bAiOpDxwEntDrCbaU2gCLbImdrfZwV1bAyocZRKNf8RoKVWurg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe038a8e7.mp4?token=T4nc1BGnCiBZCWl1eEY43O3ZGvxxTH0UXQnJjK0Ic2_9lcXQ_KUueyeBVd7MRiQHzA_jcXAZqqxNl_pOaueXVfOSfhTZMSnBEiXmEodzujhVCATolPv0L1hFw6G_qzYqEs-SSY1tKcHtymtyBKUhWYFJpN8GqBtPGb9nUmiwSi999eVNxMsvixcjy4pH2WjwTbTNOjpHMXdzTjy65g4GuMj6gGQfVUM9m1RiadtDOz936iQPPzVJ63lxKajn-wOeuEwnIXFfa_EtvxF30zbJjOdGsgUqgZ_Irq99bAiOpDxwEntDrCbaU2gCLbImdrfZwV1bAyocZRKNf8RoKVWurg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول آرژانتین به الجزایر توسط لیونل مسی در دقیقۀ ۱۷
⚽️
آرژانتین ۱ - ۰ الجزایر @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442717" target="_blank">📅 06:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442716">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEmbQvEaXRXwzN4e7b10bxr90gSqknVbPYL5yTMHDqG2VN1KkeI8IFe62CIvmUNaDZ0NvX7CDFY99vBFEz67dJaFzMOdrFzCYZkCYfvuIJQjfTPrM1rt5KtomvIdQamfUyVev6nI8Cc-YMRTkl1IQWeRpkYgpELgPEOJP32UjoW7RvmUkfTGb8C1kV8VOwo0EgKJccUhgSkM0KzKt64Naez4aF40k21LjatOJSfTsCYoYhk5wciIy7aq-Kzm7QQb3VbGTUR0XUMYgtXiNKIwWuUa0L8FuqIMPQrOLIzX7RtN6eIKrUR14ja-L6lpow7srkvdxImIgCnJwPDENAUF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم آمد و افق خونین نزدیک شد
🔹
سال ۶۱ هجری قمری چند هفته از خروج امام حسین بن علی از مکه می‌گذشت. کاروانی که از مدینه راه افتاده بود، اکنون در سرزمین عراق پیش می‌رفت؛ سرزمینی که هزاران نامه از آن رسیده و نویسندگانش از امام خواسته بودند به کوفه بیاید و رهبری…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/442716" target="_blank">📅 06:00 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
