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
<img src="https://cdn4.telesco.pe/file/MDIU6T8CK08QS04VHiR5X31iLq652x4LxbOPRMTq2RpjQ8rYVUxvH0nxcZm0QfxnUVU6QXEoSjuYm9z458MmBPkq8kfIHuKq3Qx4O7qO-IaLA4mPovXLlff4O6fPLfWsQ7zpuF98vuTSE0Vekbhh-J4-iY2YY4A-UCXvKXLxa_pP6YUpeA5XhzyvBhTM36cfIsGOE4EVDc_GptHDjS3vTQE1xDWD-S04YwqeYMsqgqXkTVFrOhBMn0B3IHuJmdg2C5_ZNFTwuWsx-p8xbc7Taj7Rr4urrtHUzQVlY7uTJBEv9xmA_iDzVtRJYJKWXbvH4cucHoLRK-qGbpxR-AuVQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 23:45:45</div>
<hr>

<div class="tg-post" id="msg-451498">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
خليل الحيه رئیس‌دفتر سیاسی حماس شد
🔹
جنبش مقاومت اسلامی حماس از انتخاب خلیل الحیه به‌عنوان رئیس‌دفتر سیاسی این جنبش (عالی‌ترین مقام) و جانشین شهید یحیی السنوار خبر داد. @Farsna - Link</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/farsna/451498" target="_blank">📅 23:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451497">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امتحان نهایی یازدهم به‌جز هرمزگان در همۀ کشور طبق برنامه برگزار می‌شود؛ امتحان دوازدهم بدون تغییر
🔹
امتحانات نهایی پایۀ یازدهم تمامی رشته‌های تحصیلی، روز چهارشنبه در همه استان‌های کشور، بجز استان هرمزگان، مطابق برنامه ابلاغی برگزار خواهد شد.
🔹
امتحانات نهایی دوازدهم هم روز پنجشنبه در تمامی استان‌های کشور، از جمله در استان هرمزگان مطابق برنامه برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/farsna/451497" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451496">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727c844bb7.mp4?token=HOvSPiWPJY_zBJ3-t_QQbucsyTpBi8CevRaCcPhad_no6CdzLkC5KUDDonzG651PDyQLc6KBpUTME4zdPIjuvuliOaEQxOYGSFuPygwBJOzuNdrMKUEpHbNHuJC9V5LPZo-WbUcqP0CCGB0jQjcuNrYsIoR9A5MlpGf7k4QV_FSo-2aayWXKABTWpJk3jeyIVCYfibLRiiCHMuvlJH9Fn84p16M6356DC0KKPOxU4bIOJ5F3dfCVxWafjCGr0Kk72rppstrjkS4rirz4Pnk4_5HGP7gNpEYlpvmO3QT1br8I8erxIPYfVyN9udBlypXSYxP7jemP5Oujow_6fP5oPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727c844bb7.mp4?token=HOvSPiWPJY_zBJ3-t_QQbucsyTpBi8CevRaCcPhad_no6CdzLkC5KUDDonzG651PDyQLc6KBpUTME4zdPIjuvuliOaEQxOYGSFuPygwBJOzuNdrMKUEpHbNHuJC9V5LPZo-WbUcqP0CCGB0jQjcuNrYsIoR9A5MlpGf7k4QV_FSo-2aayWXKABTWpJk3jeyIVCYfibLRiiCHMuvlJH9Fn84p16M6356DC0KKPOxU4bIOJ5F3dfCVxWafjCGr0Kk72rppstrjkS4rirz4Pnk4_5HGP7gNpEYlpvmO3QT1br8I8erxIPYfVyN9udBlypXSYxP7jemP5Oujow_6fP5oPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان به دنبال طرح بنزینی جلیلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/farsna/451496" target="_blank">📅 23:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451495">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4d55e81f.mp4?token=MtpulGZ78r5IzXAYQFKFjzNzjCi54fVyMnbNp_hcbmQbVe8Q_5sI6l3Q8XTH_0gMoFBE5RMlIpym8GWtF-9Dp_rwZNY8q6Nn6HWQfw3Sy4WP9GmCcqtoCzlLl9e5tjNT1X4iiF5NSY40U6B_R_NZmQddC4DvD8znbrxPZ6cTsx3nnQh3lDu-TEow2Nu-F5iz8u4QYiTV4XeE0sARHnpj8wYF8I-VxWshBM5B3P8ZPoaLO_zJdaEUHjWyUW44kuP8uiHgO6aG8jTnuvfg2Mh5BGXVd031d6FnaoGtwIRpotCZ30hUgqTobdJs8pbkIZyNaA4inkMkQhORIgfrgPY4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4d55e81f.mp4?token=MtpulGZ78r5IzXAYQFKFjzNzjCi54fVyMnbNp_hcbmQbVe8Q_5sI6l3Q8XTH_0gMoFBE5RMlIpym8GWtF-9Dp_rwZNY8q6Nn6HWQfw3Sy4WP9GmCcqtoCzlLl9e5tjNT1X4iiF5NSY40U6B_R_NZmQddC4DvD8znbrxPZ6cTsx3nnQh3lDu-TEow2Nu-F5iz8u4QYiTV4XeE0sARHnpj8wYF8I-VxWshBM5B3P8ZPoaLO_zJdaEUHjWyUW44kuP8uiHgO6aG8jTnuvfg2Mh5BGXVd031d6FnaoGtwIRpotCZ30hUgqTobdJs8pbkIZyNaA4inkMkQhORIgfrgPY4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۴۳ عاشقی در گناباد؛ مردمی که پای عهد خود ایستاده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farsna/451495" target="_blank">📅 23:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451494">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
مقامات آمریکایی در گفت‌وگو با سی‌بی‌اس اعلام کردند که در حملات هوایی ایران به پایگاه‌های آمریکا در ماه اخیر، نزدیک به ۱۰۰ نظامی آمریکایی مجروح شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/451494" target="_blank">📅 23:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451493">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شنیده‌شدن صدای انفجار از حوالی سیریک
🔹
دقایقی پیش صدای چند انفجار از حوالی سیریک در شرق استان هرمزگان شنیده شد.
🔹
هنوز محل دقیق این انفجارها مشخص نیست‌.
🔹
در ساعات گذشته برخی منابع محلی از شنیده شدن انفجار از سمت دریا خبر داده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/451493" target="_blank">📅 23:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451486">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTveuxNOWzWAzDt8g1kWapdhkTfQcsJMoey1RV0-RLamT4cF5lm5wU6kgAOlzXGojq8IAelcDCMdYZuiWE4HxyR6sT_edglIe7ymFrk2FgkdszErRmGp9Ivc6_FdhxguQgdQzwcX1L0lM3sQ8yMRsAK9XoZuodzMKQTX34suFmTTkmPA2yJJD0yP20v8kCaYxPnvvB2xao8xeJyqAGP74Ey6OWHga4ljwJ8sNh4gvHqPLp54jrxWuJc4SpZRPqCjQ2pGmzIaQZlML28b86wGw_Yza21OErhrFhCQ4Ql5NFPDE9dx1-PanQpgi5EVKluGjnYwzT7oclZ7Z06hu_iKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mvZnerozIIqa8UA5WALnhT9e58wQ3ESkyVTyLlRKW0SHP6-H-agYv_heWvvQ0xvQr__rrtZrSeiSccIZ5c5y_IgnjTINVWied30BOwJkPFxQULXKGbdbzN7YFgIQFq2mIoX7rhhauZibmkX1CQDeNiVyNIetqKzAXunRt8PWoSUHhDjwnkGj6LuNioDTWu-tec43yiXPin_Ja937GFWbiU0MlE5kcIBaM9BMj0P3mETqsrCUogmrJHUmDPQE-OAl28_o5Grj9zxx1HQJ2Npnzw3t91BNv1e1wC0BU5YxbSMw0gS2zbYztq3yX3Yxo7M6xqfXauInztLoPBEr2fUitg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQuHvHnmcSN1QL_PUoLF5FJGVZi1pKfkiw0Azg7iJRPDSnkjjSTmJSbI4WNURemE7BfNft8ndbtlpKZmPN0540xa3d_HO7osqRwDhmXGEK_LBVt2G25TvSvH3AR5IhE4Al1mDw8R6M2sdOHbcjIQVAraO_L6PVHeRrgjQn8Jsl3Z4QPidHyjTfLSlXpHKFBnudRtzBa8Da19H0Eg0RvNIr3N2zjLsGbBBjOC7jDYjk5OnI1uRsa3lfgH0efbECoeNLntXjSUPCruYHpTPQNXqtgxg9JkhT8NTO5B0fPh0_EqznCKDn-IFz7R6bucEe9KW6xynfrTceP2i5eotSwNZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAmsu0AGeL3uEEHsUfzKMsWlFJtL8t7hlKHZkdi4rFArpWi_FXtlOJ-9byIWc7Xe006NwE_LAYmfrParQK1YyBRKQY5pKBvMRdKlgQff8IUdSIs1LIlOjGaDes0Smc1ZtEbYFGWBecyQpbIv3lDDfm9AQUKehn2LbazktSjYxy7Yb45UAJj_U0eknmiJmxm3AJZ-gxf7g1xw9zeJuPwvdGl1IvNYk4UFf9XWAAR5TsPb2hAzWuVRXXvcS7PNs2Brkxlp9n9KPb-GFTLK78d85v3Kmi8ypgoENCCDSwRm_Q4vurSt9WncWVX3L3CxY55KxaIvAuKdmu8NAk-crsrvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVGSS1zQPhB9FRc6BhGH0Z_wGvlZktI17yZigyvMZdrqqFCKOtFnBHYzbwznjxPGtT71PHbrcEaaxhHh5a1kPRJPMoc1MtLZpVf_iUkwqOy7ZxlF9Jec-PzmJmGpz0Ls2jAJKzwGdG5WiVE-do_TUL7S22xR1kxlAzWFRfgOJpJkYISBWr05EccXVvLTM8BgTr3tD_tzgRv5AGwWOO1JkMtZYc5YN9QJdJZrL8dz1BDp2pZD2C18wj7oC7ZW421dwKyPsLZXb3jojoYtlIhxtk66wKSpkMmNmvKk10htBqg-cgym7UXY-7z-giwhMPcoS_yxvwXCJnUkJ3Kug72ABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLFVYDWjXyZeZLUT0vtpZuyIzJJCJPefUIHd9FxavUrm8enpfd8MJyM6O9oWODLVFwSQ-MqnMIvkqwzFP-yvTAcoS2R5A6V4bonAohWsduGOw0IrVw_sJDjG34ZQhKyMO9LuTRBXHBv84-vFwcUAnyjpSl0A89Jkg_p6wjHyXh2TV5Xn9MQXfGBKly9jw7uTit1GzbPK4HOs2ay9EW6rAdBbzwO1wLT21pu0J9UjcMlTCBK8lK-SaEvgLaVw5_wmpxBr8-cG6RVXu0XH6G2uXApdOXPI95J2tVMMpgXrIoDUR9sjhLof7br0kRwHjCQBmCNLbc3OsBY-lCjUxyMmwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEWs3dkdkPybUuKHLpPvJzqFI5C59a7q-kaZq39d4vcIGHg42-vg7QUmL9uYWPEYI1d9L86s0-xlBH2xYtPd2_tdI1cPEEfqmHnNf0R7FN1AIxSDBT7fcYlQjcRQAGrGa8CMgQNeU2PPtCuYKvDUODEWBl4GodixdHEfm13n_zLnODmyGZWz9zuCJIS2mJ9pWMwWSOykldMiIYT56wjQZYNfuImg3Tx2BhmoRJVpISB9C5CSGIhxQR5FFOdWRFZnZGnScpHN0VvPrACpmYr_astytucyZTYEFa31CVika0GcuvD3rwu_iypTrlZC2xIciWy6Jn_j-Wd1bHK85cd71Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرواز رنگ‌ها؛ هنرنمایی بیماران پروانه‌ای در مترو تهران
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/451486" target="_blank">📅 23:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451485">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5895b61c08.mp4?token=SHoqYaJjVJPqY1-h96W0Z1Ae7nt8QNxVfjO8U6QbFjuwUMaxmj5RMuE_fizD_MPPlTQXDDkSRdIsE6MJrV83XWAcKUm9iLHKSXviKFTFofI6RZ5H2uGyGaYK_0I2k2yu7-dETS61E960ay7JOlLY1HFCBxAm0KpszHc09vwg93j9d7ixNqBN7yZQWwFLy7nHqRuvIPw84-dXcRz8HKp1dSl5PBAjp4ORe6uDnyCQbqNuMs32N4c3oWbKNVSth_8tDd0DiaxX_aOsv2zceofOwv5xLXYK6wYvDNbTs5wfB--AKnYGW5AHDo2m_M_UfewfNNMBkPbKoxSfBGBctoSqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5895b61c08.mp4?token=SHoqYaJjVJPqY1-h96W0Z1Ae7nt8QNxVfjO8U6QbFjuwUMaxmj5RMuE_fizD_MPPlTQXDDkSRdIsE6MJrV83XWAcKUm9iLHKSXviKFTFofI6RZ5H2uGyGaYK_0I2k2yu7-dETS61E960ay7JOlLY1HFCBxAm0KpszHc09vwg93j9d7ixNqBN7yZQWwFLy7nHqRuvIPw84-dXcRz8HKp1dSl5PBAjp4ORe6uDnyCQbqNuMs32N4c3oWbKNVSth_8tDd0DiaxX_aOsv2zceofOwv5xLXYK6wYvDNbTs5wfB--AKnYGW5AHDo2m_M_UfewfNNMBkPbKoxSfBGBctoSqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهپیمایی پرشکوه مردم بجنورد در میعادگاه ۱۴۲
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/451485" target="_blank">📅 23:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451484">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea6b80764.mp4?token=rR_TSvfkKPBTpCrfm59fX367Xo283fjV4mylUcvqzkLsPyEdq2D4-FX2Vtsis5OGucNjN1s8RbVw3oGL1kMoAMracFMk_KuCdEXJqGpWOaX7QroNMn-yb_MPVGiQQ2xcm04i5b6DXguwJFjm8pCGPHk719P2Tcg_8Mej5GPO7EqKl9Qihew_Ps-GmDIWyJMXu_2mAOz_vW6HeuJjsT3OAo7p-j4Eo0jDcizo2Pm86l85yMrQ6PWAjuplo8lK8LyYU_jhspBbqBZvPS8_zMPDc0CrwC_fJZ5B5jIPvCB_UAN0-40rS68MKUa6GDO1V21wC7ZeD2hxspna0yi5JnD2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea6b80764.mp4?token=rR_TSvfkKPBTpCrfm59fX367Xo283fjV4mylUcvqzkLsPyEdq2D4-FX2Vtsis5OGucNjN1s8RbVw3oGL1kMoAMracFMk_KuCdEXJqGpWOaX7QroNMn-yb_MPVGiQQ2xcm04i5b6DXguwJFjm8pCGPHk719P2Tcg_8Mej5GPO7EqKl9Qihew_Ps-GmDIWyJMXu_2mAOz_vW6HeuJjsT3OAo7p-j4Eo0jDcizo2Pm86l85yMrQ6PWAjuplo8lK8LyYU_jhspBbqBZvPS8_zMPDc0CrwC_fJZ5B5jIPvCB_UAN0-40rS68MKUa6GDO1V21wC7ZeD2hxspna0yi5JnD2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت ستوان‌دوم مهرداد پاشایی در حملۀ آمریکای جنایتکار به تبریز
🔹
پیکر شهید پاشایی عصر امروز با استقبال مردم وارد زادگاهش مراغه شد و فردا در این شهر تشییع و به خاک سپرده می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/451484" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451483">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d61070b2f.mp4?token=A60ln6-8kgzNzhcYpdbAxa22flptUq3lbfP6b0em6z-fVL2S_QW0IheI39QleTve9Ba5oOuYH7XA2ipjEi2hcJKbzXE1xHaQZZw2PNRw6tDd57hgokbn77ktboPsfaLd81esFwdbvA8qApylHIB7eecEXK39ETv3gSg26YYhVWGmtW0-5SlTB9tE2KGDDeip5zhfBv0w_POEnbuCBEp94QnbTsn4uFBLT7z1qZwLaeLOxEiQZnbeHIzzuC6xT8EiRWtw8B_08Y6g6QfAoaGExqpG886MXzUaPXu0GHh4f6WiCpB1lzRIcb6KN5MvYkge-aTrUk4r53KJRQSRAR8WOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d61070b2f.mp4?token=A60ln6-8kgzNzhcYpdbAxa22flptUq3lbfP6b0em6z-fVL2S_QW0IheI39QleTve9Ba5oOuYH7XA2ipjEi2hcJKbzXE1xHaQZZw2PNRw6tDd57hgokbn77ktboPsfaLd81esFwdbvA8qApylHIB7eecEXK39ETv3gSg26YYhVWGmtW0-5SlTB9tE2KGDDeip5zhfBv0w_POEnbuCBEp94QnbTsn4uFBLT7z1qZwLaeLOxEiQZnbeHIzzuC6xT8EiRWtw8B_08Y6g6QfAoaGExqpG886MXzUaPXu0GHh4f6WiCpB1lzRIcb6KN5MvYkge-aTrUk4r53KJRQSRAR8WOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها دربارۀ آزادسازی دارایی‌‌های ایران هم کاری انجام ندادند
🔹
نقض تفاهم‌نامه ازسوی آمریکایی‌ها فقط دربارۀ تنگه هرمز نبود. @Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/451483" target="_blank">📅 22:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451482">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تعطیلی ادارات منطقۀ سیستان و کاهش ساعت کاری در سایر نقاط استان
🔹
به‌دلیل تداوم گرمای شدید هوا و وقوع طوفان گرد و غبار، تمامی ادارات منطقۀ سیستان فردا تعطیل و ساعت پایان کار سایر دستگاه‌های اجرایی استان به ساعت ۱۱ محدود شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/451482" target="_blank">📅 22:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451475">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pB0aIXPsU9YqnrAOvA3LwPNISgHM7DTBabu0LgHRAGWFXQMGmujgriEht8shAzAoqsmQrTJGIwiQK-0KAdZ5FpPMkwx4w_FjlnRXuIPPVN7YMMP5DpJ8J-O7f5I92q1IJP5eFKbrygyknLuSTAl2uQFUWlqaUOs4o_BuJXFiqKn3l1sfGtVUIGh7RcdoTsAAl5MPyXmGwmEDMcw4IbZEfOeSFK65IEJwPYgrS2SFkIca1FRgQeCr2NQSdYn7ecTAe9e_QEbyh1CvaBp1zvD6e93CVbFTrdwkCyGp4t3DQlbgASRfoj6mv1m0Ils1FVvddyQkCMZmOHDU9MHQyeg-sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgAG2gxhKkUHwPRsbAY6u54r-6uqvkWzKFGYqNyg1GTs02BHMLf2hjjpUDOpGckOSOstHWekzP2DacoqRwxXlRBI2NSpPTkf9wHU3W8a_v40mTb8c6Nv0sjKmiUDTzXYvqjh8ThoOuZ27Ie03xQSel4k7u2eF8C64XZeuac5CEKeR8oy6lOtwjLW9B87dnqkYNBzkTAVVJgx6I4mxx8S483sd3j95jL5XAB51cvZ3XCJg9z6xrn4dn_qxuDBZxeqOZ-Ofiw5bfUjTlA_APdh3DzMqEH44fjfX_Tjy_c4CK9PaTNreiNkWNtNtdeKattIKEIAmZa97vWZ8fiouLN_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJAEsYRRnvZzz5Woyi-WqWLnW6MH3H3H7iGsAfOSujlsRmplmLLRJ36L15A67zja-A8ho0pQ0iRnewMnBgMS4ZYpXInc_Zaf8Iazazt7SF-R_ktQRddDMpKKXyQRXOUym-1maJxAaWDjW0dV5nPovVG5F-k94m_TnF3hqk2AgvX-SWs-MfnMf4oRY9jwAZdLLK8OsAnpE_vyi1smkjYKJ3wSPbHxuvBTqpNtKimGDO9dJ7TChUjO2W_-9Ds1ctfq954zTEtamV3pNBvU__Rd56k0KGhzRnD2l04gv9wR_qR75XkNFU1ymFBuIc_NEOCgyfcsYPvmPxGh8FCCJu20iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQuTtc710k0wdNLCLuCYC2Be61e9_UDQPBvyXGzSjWqYgwmDrW2jh0BR7k-voZ9Lks5vWXMC-0-Mxaj6s02LkQuqWV65URw5q3TiyODC7IZbsR00kTQSeXhXEwqN8wppFb4WTO0o0NSwhy1_NewczLTTyVxP4eE52mU5W3PZ_NEZmc2qju2R5WMsFiWRkWD_r3msb5pxwApf5XoUKaI5PQxbqpf6qoW6cYo_uEpTqMsTj--VPlNXJbQ5ViYQLT4HS4tynu0spcTm0rpHalWpUYD4Cyif2as08In4MU-scvr8DlszSTOWTVrqdBUJ9eijyEEFCozfIe3RX8EoDLXLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rSmWYnIKDVtwf18Duzu-s2IJuK31SqF-t_zKzi4WNtr4MCchK4bc7XK5o5y45RYPeuvfj6F_NPFI-zcrM04sWsN3ZZneAPJCWr_OnIHDVayrIzICgamYE0LdyynWTAjPnnJG-FMgXaXnn5MMvoyH_RrUyE1vv2MMHRtw74_yO1rOULvRaF63397oACeVLu9GDwaJayjh_vwFRfsVmyrtZtOWwoN1XjsZcJlW1UhEI-Yj84_c_2Vpnj8R1BbIMTbXhke1pPmunBkQbDMSgVOqAa_EHPStnz_NsEvttANq7bzZPqRwBD14tdNb0MMlYdT5u7CG3LXg7RPO9loCREP0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mddzZFleDVPTrkBXXHxZkxN-4T8QreI7e3WN_aKIx51QqYfCVGlfbHw5lZJp3WrjN0iymWnJmip_7gNcPir39H-vZDgWDIGJpau6eBoOIZegwmN0tr8d3T362SFLwUWrnq4NiZ5HIJqx32PPz76cbgQ5P6FH3r1y0FfYnWJN5RzpGz0zSDKdJ6xtXcHo57mmD_q7c_42ImvkNb4XPWl9O_Zo0XGpRpyhUucu5soA8cPcMYYL-CMIvogp84OVyVQA4MfUTTEDXLFYYvUg1QaxjD9-tgqizBKpzjzAcCq1wiXN-3BwhWutcjKzrJ9p_SqkhOp4hKr21umEh9cLqh0lJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UvJjoHsKIsd9CMt3D5OvSUo0mvuVaiFAHf8zqLGaoAw7ohMD4rJC2eX46YpnTVZJKptCByM7f-BAHs8KJHoHeM0fHeCFy7OJAuLoi0mfSVAQF-wfKcH0DeUvyKk5NlF6QtMaoulUhiP_cODp155OqtV1nPMInUgPsBKmko3nyfbxmNpQi7KvwCxO0ofgO21fmnHpyZEwx5VFFcUpM4QaLlRoOrXO0QJ1ej9fg8OBmxrAdYDpNhjRaDJyM82VxL7fXqOI9ayCj1pVc8NiiNRPxl1Zyc8DGTzVFeDc3IPRQXLAHZ67wEyi9k2kzxfc5eTWg43dkgA1TC1zzKW6WhhtTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زنجیرۀ انسانی هرمزگانی‌ها در کرانۀ خلیج همیشه فارس
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/451475" target="_blank">📅 22:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451474">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcae8d7d02.mp4?token=ZMZ6fB7PAVHHjK1oXJUtmj7gqKr1v2AFaQiAhrlx5POZ0EvpeWVvtO_VDCH0bvZquhBocEOvfuA5GqYHs3nfZ8x_EgupL-_CU6TRwOM6qzprWLRITmn_EEw4fW9qpJgNXQHS7YVeZHgknrTI4YsM4ZJ0XBA_0xmplemkzuk33aUFl7DU_L4PWYioPBR8ogC7y3gcG6NQXYx_Ejh3GZ1oZ7wADMGX2p8gaxeOEl-CLH8fzNy6e4hWUv62GilI0DeYo0pxojJXuHBZOaR6at5vSx60jCw1KerIYOT-ZWMF3qdd1Am54Ot9ao9RnlKf3FenplYP_gqv5fNewY-SQueasjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcae8d7d02.mp4?token=ZMZ6fB7PAVHHjK1oXJUtmj7gqKr1v2AFaQiAhrlx5POZ0EvpeWVvtO_VDCH0bvZquhBocEOvfuA5GqYHs3nfZ8x_EgupL-_CU6TRwOM6qzprWLRITmn_EEw4fW9qpJgNXQHS7YVeZHgknrTI4YsM4ZJ0XBA_0xmplemkzuk33aUFl7DU_L4PWYioPBR8ogC7y3gcG6NQXYx_Ejh3GZ1oZ7wADMGX2p8gaxeOEl-CLH8fzNy6e4hWUv62GilI0DeYo0pxojJXuHBZOaR6at5vSx60jCw1KerIYOT-ZWMF3qdd1Am54Ot9ao9RnlKf3FenplYP_gqv5fNewY-SQueasjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باقری، معاون دبیر شورای‌عالی امنیت ملی: ترامپ بچه‌سوسول نیویورکی است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/451474" target="_blank">📅 22:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451473">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6e659fab.mp4?token=W94fXHmj2o7TyD7ADB-_M8CJ9pCh-0dUWE9hdlV9BZjo1z64XtixZp2xtIEZTioccabOPFRsWPV150CK-mnfpiDy208NzyLN-SDbR8zNGvg-PTyD0X1zRWAqdzhkOm_pqqwzSddc_NE-DkQdOjix18VD4TbhvPeKvn7XRfGAO2ZgIb2l44M1nhBidb-VoObJznonlSM00sGwGskeozt3jETXs1XNIg5sUzPEpjvsJESH7lrmukSmS-rEr_CJj4dhzKkhqX4vtrtlUn5LzAi32F7zv4JkH5aVj_8vT3zsQ5MUF78nY-4fRcI_SvzXmL2VbdE_iEkfL3TXCVnShwdNgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6e659fab.mp4?token=W94fXHmj2o7TyD7ADB-_M8CJ9pCh-0dUWE9hdlV9BZjo1z64XtixZp2xtIEZTioccabOPFRsWPV150CK-mnfpiDy208NzyLN-SDbR8zNGvg-PTyD0X1zRWAqdzhkOm_pqqwzSddc_NE-DkQdOjix18VD4TbhvPeKvn7XRfGAO2ZgIb2l44M1nhBidb-VoObJznonlSM00sGwGskeozt3jETXs1XNIg5sUzPEpjvsJESH7lrmukSmS-rEr_CJj4dhzKkhqX4vtrtlUn5LzAi32F7zv4JkH5aVj_8vT3zsQ5MUF78nY-4fRcI_SvzXmL2VbdE_iEkfL3TXCVnShwdNgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهالی یافت‌آباد تهران امشب در میدان چه گفتند؟
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/451473" target="_blank">📅 22:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451472">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq99A1NduNsa-TGSGkDm7Ou75tcXODo6oW_5QVqzd7eq6QQeaNyfisRNx9MjPHSNw49mIAe6ZQTlRESyTaah-C5HESltCb58UrI99cDtHk-5sCpEs9Nr8Mj7PKQoqWDSA_u_wY7FQSgNw9zguz9xAb5Mfafj_SUWaBRN9sRCZLFspPj3OTww7Jeui1SyKh338n87BQ3AtLv50OpT6MuE5JF3UUWial_01R2bP4GjtazU7Zm12eAIC225qXnAt7HOf9txFaOdXcsUcx7yZxLl3fQqEw16PdxaxbPxQ7hWuQ4HieeLvDvUz2ljmUboX2mfAuIuYXsfBl8ALHZZ-WL4Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه استان کرمان: یک موشک کروز دشمن آمریکایی در آسمان رودبار جنوب رهگیری و منهدم شد
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451472" target="_blank">📅 22:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451471">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
منابع عربی از حملۀ پهپادی به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451471" target="_blank">📅 22:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451470">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaf299c7a5.mp4?token=iSVKVMT4MWTnwWwMKWCbNwUNvXKZPBKZ89SUQfMJREUD-BPjlitmkzIBHwXxISf7z8jeDUcutlJInJGo1rvigyHUweJ_WXkfSoWlCqrqlqcs_tmEwhMsjqVWnxNqPelOBgpP3TS_O8R1jDXSA9STZJTT6IHo3ZeP3CgFZJ-YEnG11W6jcIzrs8ZUhYnbOBftQJapBE2oAIs5qCeSF7i0IEUAkt-sD2l6fmlbTEoOSTVXRS81XGB4tARi5Gy6vUCuB7ZtBQLzArhGmBoi8JZ7F0jgScdFHTjZWsmkHVK07RGo_59YUy3ZgMiSXzAyuIqtFRUcJU2d1VS-9_Rg4nyqDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaf299c7a5.mp4?token=iSVKVMT4MWTnwWwMKWCbNwUNvXKZPBKZ89SUQfMJREUD-BPjlitmkzIBHwXxISf7z8jeDUcutlJInJGo1rvigyHUweJ_WXkfSoWlCqrqlqcs_tmEwhMsjqVWnxNqPelOBgpP3TS_O8R1jDXSA9STZJTT6IHo3ZeP3CgFZJ-YEnG11W6jcIzrs8ZUhYnbOBftQJapBE2oAIs5qCeSF7i0IEUAkt-sD2l6fmlbTEoOSTVXRS81XGB4tARi5Gy6vUCuB7ZtBQLzArhGmBoi8JZ7F0jgScdFHTjZWsmkHVK07RGo_59YUy3ZgMiSXzAyuIqtFRUcJU2d1VS-9_Rg4nyqDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگواری مردم تربت حیدریه در شهادت حضرت رقیه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451470" target="_blank">📅 22:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451469">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe2ecc4084.mp4?token=DnmHAf84g6Q21aXHcBkfbw_5Aa8vTsw51WU7g45aME6rllEehbUKHh7XnF2305XYFhOUtiyuf38FutiCr1PgOnq5dXqrN8G7UBdOR1UKgZGM3roU6RcWHEPbE8fpClMQ54DWEzvL01EqXpHAPe9_PK6sXizgxMYLZkAI5aI0NnGxvjJpEScUuofJ7eXkvMI1gMPlgLfc9GbnE9svGRWnLVWEOgl2nc8GqdVQoFspDzGtNFl5bWPqgZ_JFfR4I9TDExNhtEkq6nswIoMr1M_6SF9fDmgRWXm3zdsVfnv91ScnTQhjG8dxtG7Vl3aM4c9-fcSinJ4z3dy2bpHDVVaNIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe2ecc4084.mp4?token=DnmHAf84g6Q21aXHcBkfbw_5Aa8vTsw51WU7g45aME6rllEehbUKHh7XnF2305XYFhOUtiyuf38FutiCr1PgOnq5dXqrN8G7UBdOR1UKgZGM3roU6RcWHEPbE8fpClMQ54DWEzvL01EqXpHAPe9_PK6sXizgxMYLZkAI5aI0NnGxvjJpEScUuofJ7eXkvMI1gMPlgLfc9GbnE9svGRWnLVWEOgl2nc8GqdVQoFspDzGtNFl5bWPqgZ_JFfR4I9TDExNhtEkq6nswIoMr1M_6SF9fDmgRWXm3zdsVfnv91ScnTQhjG8dxtG7Vl3aM4c9-fcSinJ4z3dy2bpHDVVaNIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باقری، معاون دبیر شورای‌عالی امنیت ملی: ترامپ بچه‌سوسول نیویورکی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451469" target="_blank">📅 22:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-7eH-kHU0uKwfmFihi09u3HCNhQnv6o5SnScNrAJIxpiQp8qblZVfROhWbPvlvYW1cCH31KXSNb2miIBd-JKfkAKvIF5N1tp-7bdpa-XXJ4V3Jkn-8AieQo6ftG6YXQ1TF-JOxmE1t3nTTUc1rXw8k2f2NQTxcC8Hox3zetwRZ_Ro138zF_KGk2-05hJyfhhIIrwQe8zvokcgCCAIRx08sadkZSIuJUyaPvLqsCAmnRwxLg1UjsbZtYj_ylcxai1wN8chx6suLwUWPRaa_lcKi0dDQV5A6vtnL8rKC0veHbh0pG0J0Xadx0ublI3uB4ZsUFy8T_EAOi5YV3Wt5zdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFm0ZghKM5LOssKGgB8j6AmZP2L3uuHsmw1IYObwYua-XS_MQCYTeaFuHMXozSJ9mXWxZ4w6tb285YSTY-ZQ86BPVEL_Iv3Q9W7niG5RXlKVSaGdjhP7PTb_HJGVR1eBEY1xpxhTfp7o3PWxZlY1ytNvpTtyj0UOdgdpb6XVbfRq_b1g3ihHXQajp_gRCGpDa_VZDre7M-KmjzxatEu5eA1quGU5somQuG27qDuEGW4Q0arEangcm42EreGz01v2qvxVrpTkAtrP995Eo_KSH7hVzGZ_sdBMUT3obHwnRyPKeQZQ4l2FUokoRfL088VJwFWvMdXVJ-mA3llaBOZo7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFBluV5-4ytStd_cI7uMOjIn2pK6SqvYY14BeUs8L9ZAGTYokxHTcPJD2r6ZUtWX04ch99PuKOf94R5fed5imuJE0pV7pw2BOnY_ssR7ij__oTdetZ17RiSeQ5Iyw2R5BkQ-8t9BRpS6vs-VoXoCawnYKe7YFPpk8PY2FZ0KxijZhyK_YEilCsqb1cIIl3xmuYJT4SbsiKUQGt3H26n9QQWzaXXKPjuKWmNXmbrTzV6geU0gcRp4w1yMr1UZQCd3alJsR3MrUr5hFRFnnENjTqgQ8gTg0D1RtEZJOQ7gilc9SsKqMfidzfGTpg14x8ab0Fpon4H6RlXWR-ig7YWvQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHQMK_BcJLHLPwR-aU8Gbw1A6HiiAZL3M04lh1zZh2Cm9mdBqGEOG4-V7ksdp-mfBc307PtZ5pMqA2jCADapb9sBxeD--u7RQe4PTnrMdOTLXZnza3bV5LKxT1jZ7j-tMTN2jSDqSDNh7rVvmW6OaS4Pf1wixmuxCxqDHxVA_Arglcc3RFyD1xXYSEAnSSWwMqiFJ5VzjPhwNSjYgb4Spf_41s5pNbMaV3LwqhDsHHSOaatUfrgbqXBSDRFyPspCeYD69w0hyeBwDiOww9iudHdnXfw_SqSG-UVPy_Y0aP2Y33_g0WXO62r3001HG5k-OiKKJwcUfyQlZQ9laAPwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-onU2O2GVCkO5gYptr0B4IWVdMhJ96JCDdcnxpM11I4ZxH1RuDg1A-BfwWED-E2A8o2Mefz_kU-LCCNI83P3Zhk9obLA3qkRC6CNtWxCkgRn0-na9jnus5Iiph77wa90kk9JHWof_y5ruQtqSoXR6huz6NTMcVv3KQVoMKKD7qzfI5CnZ6o7UWWFJo1c1cj9XCtAwnJ0kLsApc45YdSWVsPHfkgKKghpFY4s_5rOMhk4dyuSrD30jfrhA-gAy-mfKhP_QqCX3KkFQ9EUiK_781PYITmE59QcM24g9-KZvFTClDEn1SQh1thmjIYDNSmnGiSvTAGFRrg7haifT3zXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ffhb8eCKLQU2GHPsa1PjSvE_QhioaHMcqmb_LiegppVFDKZPyk8LTRA5iumavd-8osX6n0jo_w8LCptbTjp4q7PxuprFp6vVRrLI1ILz9XUAAv1LJtvvgmLIQeV45vMpWeZZA9gHfiy9Wdp8TYle4HrrPrvjtzRwYra4dRvfxUVDYW26VO3ulgWy9P1EnEA8Hb4xqMqfFFn9A6TDxqwHRP6rHDUf4DBRpo_HW6FVYdkPExbCyZgfpuk1cpXqewiu8dEQ6DgZssoz7Ysu1CFurx4mU_WXuinARCLGm2JtKe4YaS54iiR4RBtrMhralG_pR83X7FL0lOefbQJPbwEBCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نصب پرچم عزای امام حسن مجتبی(ع) در ایوان طلای امیرالمؤمنین
🔹
برخی علمای شیعه هفتم ماه صفر را روز شهادت امام مجتبی(ع) می‌دانند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451463" target="_blank">📅 22:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgGlQjdgAUKwfXctNJPEG5RDy5BcYUIqZQS0hqMmG5U52f4Qak_vElv7niHCXH19SF7T407i9oo-4RtVJaRvzPcJBZ7aaSgak8aBJ14x_REEZN9hPJeF56B1MeON5qb77o3cVb93kWXquqB0B74dd8DP0uk26T-PwZC98bkF-hsu724QMLGoCyzl2D2ZMdcL8MnEKyIV2W4ATa_MYhkdcHJrwJfGI9g2tgVe3wHBKcdmrX1hcP_0Wud7pNhn_yi2cjUvZwcalI2Y8PFc7DwwSZ2hsmQec700xzDAN2DGJA0-UPeIN22ns9SSBlfbIBqD2FBlR90X1p9j6rdotCee5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
منابع عربی از شنیده‌شدن صدای انفجارهای پیاپی در سراسر اردن در نتیجه حملات موشکی ایران خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451462" target="_blank">📅 22:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvHJ-dV0LkppUn1WVBsNzbQKOIGpNY1QoUQIrR11eI1217nGs-Bvp4c-QF0syAt7f6eGwrVpb5DYmKmRG5rBe4XcuOhYkuZIgcWF9qH--wK-5w5Ul8tk5V_msQpuQ2kLcBM37Wg60Cq9e_ZgxdsFcaLs569-jkpyX8z7Ap27tnojSeIDmYeuPST9Bcglb6_15W1OI7ggdPY_kP9iDcg8D5KWtMpX7xPB4kkXsMdQB8-V0ANUOik2TRU0R12Lo4DKg2sbFZA2vRb1j2UiavT8k_3Vfg8QEFp5lP1StsbIN1p-i8EeVxUIkdOYg-GdPTg59H4DHBzZ2WbJWPaPx1ztgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر راه: سالن فرودگاه بوشهر در سریع‌ترین زمان بازسازی می‌شود
🔹
دیدن صحنه تخریب سالن مسافری این فرودگاه بسیار آزاردهنده است و بار دیگر نشان می‌دهد ادعای تفکیک مراکز نظامی و غیرنظامی ازسوی دشمن یک گزارۀ اشتباه بوده است.
🔹
با همکاری همه بخش‌ها، بازسازی سالن مسافری فرودگاه بوشهر در سریع‌ترین زمان ممکن آغاز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451461" target="_blank">📅 22:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
منابع رسانه‌ای از شنیده شدن صدای انفجارهایی در بندر عقبه اردن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451460" target="_blank">📅 21:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a39fa6d7.mp4?token=feZyaSrcHMIWhneDfP2dJx3NmzEwH9TBSueG-jsH7QonDKpJe4ol-w_-tbeedzqglQ8k4kQPNdu9XULTHTaau2MoTkBgInMJIUxWKKPqGkIR2fBPUruRI36wB_7VcWr3uY6IfQrNZ7A6JXx5uSWbo9yfLfuixxIp1UEvRYxhFbsYI_b96VedLrsifh90fz6ZtxXpcybzeuILO9m3ZjxdtoTRZAlwtwX6KsdIowbFPcpEKQbk4kWOrPea4bnn6Jo9aOYzpHXAtWbsu3JSM99YmMhUErAB3yVocTggnzGxf-p479B8py5n43EPKEF95kGwiOmJ1S5X18zRXUjS0qWWoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a39fa6d7.mp4?token=feZyaSrcHMIWhneDfP2dJx3NmzEwH9TBSueG-jsH7QonDKpJe4ol-w_-tbeedzqglQ8k4kQPNdu9XULTHTaau2MoTkBgInMJIUxWKKPqGkIR2fBPUruRI36wB_7VcWr3uY6IfQrNZ7A6JXx5uSWbo9yfLfuixxIp1UEvRYxhFbsYI_b96VedLrsifh90fz6ZtxXpcybzeuILO9m3ZjxdtoTRZAlwtwX6KsdIowbFPcpEKQbk4kWOrPea4bnn6Jo9aOYzpHXAtWbsu3JSM99YmMhUErAB3yVocTggnzGxf-p479B8py5n43EPKEF95kGwiOmJ1S5X18zRXUjS0qWWoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع رسانه‌ای از شنیده شدن صدای انفجارهایی در بندر عقبه اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451459" target="_blank">📅 21:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451458">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
منابع عربی از حملۀ پهپادی به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451458" target="_blank">📅 21:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451457">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/850e96d1ea.mp4?token=vdKUENOBc_JUoG2Pnp8IRPUUz_OGtnEgDvraCobqlvZDuAWDhiPK-IK_rXJ8WGsYYdrwNuVsadqFqPEYBw003l4hae8a0S5sINnR77gJ-L_MjhgQNzrppvywZFDxsH63NL9RVlUr3I_XMBPFg1SAX71wBfOWYEyql4TdXOcV2jy6MSXIDv9rVIJ7ngNJ5MhxNUptRsGsIF_EAE7H60NhdYdvJlrq-3uswGCL-RR5_-l5K66ekflzOtJX6o0egRdtuhfHVL488_n2RuikTyBhhTtl_4bZtTAt7uw1AYlal7ccSCxMQwdODYDvZc4IU2bY3E7UD_znGGf1BjF0aDkKJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/850e96d1ea.mp4?token=vdKUENOBc_JUoG2Pnp8IRPUUz_OGtnEgDvraCobqlvZDuAWDhiPK-IK_rXJ8WGsYYdrwNuVsadqFqPEYBw003l4hae8a0S5sINnR77gJ-L_MjhgQNzrppvywZFDxsH63NL9RVlUr3I_XMBPFg1SAX71wBfOWYEyql4TdXOcV2jy6MSXIDv9rVIJ7ngNJ5MhxNUptRsGsIF_EAE7H60NhdYdvJlrq-3uswGCL-RR5_-l5K66ekflzOtJX6o0egRdtuhfHVL488_n2RuikTyBhhTtl_4bZtTAt7uw1AYlal7ccSCxMQwdODYDvZc4IU2bY3E7UD_znGGf1BjF0aDkKJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرهنگ بازنشسته آمریکایی: اگر در کویت، بحرین، قطر، امارات یا عربستان هستید آماده [فرار] باشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451457" target="_blank">📅 21:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451456">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22b7a458.mp4?token=nP7Blj59k8S86pbh2VuyfAxYkrHnqShwV5PP_kwdnM7Lw6cqcsgSN_ZfN6D-2IRisBaow-B9Zc0aj9YtgQ3tXhSmVO0ekMft2czZ8KkomcnXLkBNSa581XLKUm6MP41738WHNPt43uhBPKUFX8B5LsiTavX8-5d66SI8z4g4tzj9LDHB3RxYivA8WaEyo6s0cIiBJqtOzdfUu446ME7oggPsca1LNGRiW-ODBDxGEf9VqQzncDHxs77ES2lCkQGv6Jq2eyjnMiwfiIOreZnHe3KnmN2x3x_XytKQbIYQgbLI9U7pB_y-An_7AfTkLfP_hbTrdSo7SmRvp99siJELMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22b7a458.mp4?token=nP7Blj59k8S86pbh2VuyfAxYkrHnqShwV5PP_kwdnM7Lw6cqcsgSN_ZfN6D-2IRisBaow-B9Zc0aj9YtgQ3tXhSmVO0ekMft2czZ8KkomcnXLkBNSa581XLKUm6MP41738WHNPt43uhBPKUFX8B5LsiTavX8-5d66SI8z4g4tzj9LDHB3RxYivA8WaEyo6s0cIiBJqtOzdfUu446ME7oggPsca1LNGRiW-ODBDxGEf9VqQzncDHxs77ES2lCkQGv6Jq2eyjnMiwfiIOreZnHe3KnmN2x3x_XytKQbIYQgbLI9U7pB_y-An_7AfTkLfP_hbTrdSo7SmRvp99siJELMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تطبیق تصاویر ماهواره‌ای سایبرالکترونیک سپاه و سایر تصاویر ماهواره‌ای
🔹
گفته می‌شود محل مورد هدف، یک مرکز داده C2 ​​و هوش مصنوعی ارتش آمریکاست.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451456" target="_blank">📅 21:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451455">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
با شنیدن نام‌های آبادان، بوشهر، چابهار، خارک و سیریک چه حسی پیدا می‌کنید؟
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451455" target="_blank">📅 21:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451454">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJuc8aohQ7SZmRL49SJN8V_XkrJt5s4lT-WB5XhHf6Jl3f0XVp2Ndi8rZFUD7PJjEuGTS9WupkLP4EpOnHi0T3ij9M857wU8kDgx9jjY9QauroAnOipF8z8eqhnRLQQw7-cnRNj7q91EG8V-_2YZZchY7Cnp_F1VIWMwfE8mhbJYEsgf1DuXfC-mh3msjnn4ge--M8YYAifgFQ8NT3foUu6KNBQJIpN5Hh5T6pXSwdnUZ11cP6e4ZT2KkCXPDurSqQSLBWbSVJY3D3VCHxOsWdK5xVDArlzjWqLRjoJJd9yymOIB63AcRpt7Y1-csxdHbXuyvoOYapmHQDki22j2KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آرزوی مرگی آرام را به‌گور خواهند برد
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451454" target="_blank">📅 21:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451453">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/981a8e6dcc.mp4?token=oKbZ_x3aXg6FHEDZO8rfyaHXIZJ13YOpykbCZFT8cniASdy-PK6V7dKlkO3uw-eAMckKdSv9ip1Jqf8DAY6V38fgnWmSF1lquFf54QnqbxLvYVDF9KnhVW5hqzssNzhwxONICxCoVgy6gPUtIY2BDZ_e-f6m4upsGqjrzQbkzdwgxnM1AdCZK5Guo49d8P8UyKrRWE4QgraepVBJFGYFbtszS0uVGtzOaxW7oFoADazXTMinSzORJltEKVgtsQUlMfV-7GxhrePmQA0F96HL3sIKtcQ7lMMSbZg83vSV800eYO3AI8OB5JSFYPcI0cavDFVv-_VaqR9rfhi2YG3Bjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/981a8e6dcc.mp4?token=oKbZ_x3aXg6FHEDZO8rfyaHXIZJ13YOpykbCZFT8cniASdy-PK6V7dKlkO3uw-eAMckKdSv9ip1Jqf8DAY6V38fgnWmSF1lquFf54QnqbxLvYVDF9KnhVW5hqzssNzhwxONICxCoVgy6gPUtIY2BDZ_e-f6m4upsGqjrzQbkzdwgxnM1AdCZK5Guo49d8P8UyKrRWE4QgraepVBJFGYFbtszS0uVGtzOaxW7oFoADazXTMinSzORJltEKVgtsQUlMfV-7GxhrePmQA0F96HL3sIKtcQ7lMMSbZg83vSV800eYO3AI8OB5JSFYPcI0cavDFVv-_VaqR9rfhi2YG3Bjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام‌جمعهٔ اهل‌سنت میرجاوهٔ سیستان‌وبلوچستان به شهادت رسید
🔹
سحرگاه امروز «محمد انور ریگی» امام‌جمعهٔ مسجد علی‌بن ابی‌طالب(ع) شهر میرجاوه در استان سیستان‌وبلوچستان توسط افراد ناشناس هدف سوءقصد قرار گرفت و به شهادت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451453" target="_blank">📅 21:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451452">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس از برخورد یک پرتابۀ ناشناس به یک کشتی در نزدیکی فجیرۀ امارات خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451452" target="_blank">📅 21:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451451">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d81f40dd.mp4?token=QnN9HbEtdSgG0kmLD9fz7k1eL6LQzQgKo8Z22WW-QosWxOxFZz0I-ClDgPzgtxJKYLXhRqOUw12G1h1jQ_GDeifcUtoYktxOtDH4zw5ERw7yP7spEVNkSXBwJRey6fznA2FYdZg0Jp27lIZXYIjICfhdiiEQqE8SA9oICT0eIGOHPCb5O-mYInHCDhbdCobyGlL1p2H6mTNgjw02Xqkz9fgWfg0MSw0Td0xpNJDHRV5319an-dc-mNaLHCu0_nNJPthuicWYKcRtz2EMYHrAbg7PAYLXqDzYMFlP0PhCs2QJCiLXFhP5KK9yIBqzPFrb_NqOZ7urHnQMvxBG6XvfDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d81f40dd.mp4?token=QnN9HbEtdSgG0kmLD9fz7k1eL6LQzQgKo8Z22WW-QosWxOxFZz0I-ClDgPzgtxJKYLXhRqOUw12G1h1jQ_GDeifcUtoYktxOtDH4zw5ERw7yP7spEVNkSXBwJRey6fznA2FYdZg0Jp27lIZXYIjICfhdiiEQqE8SA9oICT0eIGOHPCb5O-mYInHCDhbdCobyGlL1p2H6mTNgjw02Xqkz9fgWfg0MSw0Td0xpNJDHRV5319an-dc-mNaLHCu0_nNJPthuicWYKcRtz2EMYHrAbg7PAYLXqDzYMFlP0PhCs2QJCiLXFhP5KK9yIBqzPFrb_NqOZ7urHnQMvxBG6XvfDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشور وارد اسلام‌آباد شد
🔹
مومنی در رأس هیئتی متشکل از دستگاه‌های اجرایی کشور، برای تبادل نظر درباۀ راهکارهای توسعه همکاری‌های دوجانبه بین ایران و پاکستان به این کشور سفر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451451" target="_blank">📅 21:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451450">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOo-DnGDy1Dn_65UWBjpAOT3ExvwyOQBqPGQLBbx-7bfhxqAbSVA1KWOct1ezShJfNqTO52giYWqprGj0NkYtAfkb4RrMhULlEo63FhZqq3NRaULMcbIpjqCptHRDkmnyNKmZ7kllsFM8086x3788ZxwzKbkrzGQogbxKy8xnHupCG53884m3MF5pgfabN3ICYH9ZU13cFowgQ9bi5Cox06QzUR4_rIJ7EGzgO5uBUQMHEPl8a3KC3VEW9ed_wsRvHbsUrTvlFN5CHrkhTtMtcS6skQpxwSkVvPdUaNRa2MmaoURiwg8kCvlXl3JnjBlmdLaGFPjsj3aMukKR_CIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سازمان تروریستی سنتکام: بامداد امروز بقایای جسد ناشناسی را در محل حملهٔ موشکی ایران به اردن پیدا کردیم
🔹
در این حمله ۲ نیروهای نظامی آمریکا کشته‌ شدند و یک نفر مفقود شده است. @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451450" target="_blank">📅 20:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451449">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BR_P2Be_PkGURxKTSqgC4zN74kSTfEt9k9zG9DZG1kjjbqe98gUkmHiLJcCSA4rWtv22OmVQzywJEA71WrMQynkqYJz5EBrF3rRABDZIoENYFuAG8u9YR2_likXaz9J91TDzn_wvxm7uqYoN14EAQqRR1wR0-L11oyLb_oH_2bHglbxOXR620cE1ESPM8M5e1QjZNrKN0zBp-BNZUYKNLkimFovePpAuzGNq_uut5UQe9w8rnm9W5_m2mj4nAu5H1nqCW05bycnrv8uBfNpOdEA4Qopmg-MIYpJuFGX3iZlHq3AC0Xh7a7yDEhNLkud9v6j--nMj__fgol7xalj0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت سربازان آمریکایی باعث عصبانیت ترامپ شد
🔹
ترامپ: هربار که ایران یک سرباز آمریکایی را بکشد، بهای آن را چندین برابر خواهد پرداخت. @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451449" target="_blank">📅 20:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451448">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jcm49WXzAOsMTTz6IeWkBiCY6NMU1ZhNvwmluv6eObmqrvXEbQF1rSC8DAXlzaW451U39yeNqqiuTmEywLbmh9Z8nqsbM95UHepxm2UJ796GIwDzhAFS1XrPxM4bsUsX-PjPQoB4uY7YA5kdGEEM1VmnTnomX8TOIVnWnxnPTfLQVbYkhtgVMY1nJKXVcjhTDkzn10t4ohzUh3uPNjgbWfxhs2kI3zSWqOAwkwqGhDfSUt2w3Xso5PtytTEBmIY78hHxprGtgZgKyzncIimZG58fjbPHz3OdQNbvF36C9H9_FvJ4g06wRp_sZq_MSlgb9SyCiVEjF7m0eS9SwquS-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سازمان تروریستی سنتکام: بامداد امروز بقایای جسد ناشناسی را در محل حملهٔ موشکی ایران به اردن پیدا کردیم
🔹
در این حمله ۲ نیروهای نظامی آمریکا کشته‌ شدند و یک نفر مفقود شده است. @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451448" target="_blank">📅 20:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451447">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VT-RmYs9sqGn3jQo42FAn-FTWZAIDMF8Hp9tP0aK-LXp1WEUJ1t_as4eLc23pmtazH2EA_h9jeoR1U_lZeAEJKG-G9Abd9wVHEx7xt3XbbRVAYXMf-8gcd8Sw8JRZ6tkhxAZ8QhtPmLA4tVOGMP3eXNrkdN38YbjTG9FDpjw759_0MnauwzHis4EHe2VFA_7OCyvbSLqnLFm0TdAwtprk3hkpdGF2N_yeuvRwsnO7i8KuNiZ4GFCS5J-iAz5VkL-ovQllIyg1J8wFX8w59a4MNQqy4l_r0uM6Nawd2OklBtXn8LuyvNhxxeKkuhSridnceXIp_1Dzkq6iID4Xgw0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس از برخورد یک پرتابۀ ناشناس به یک کشتی در نزدیکی فجیرۀ امارات خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451447" target="_blank">📅 20:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451446">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf6QGbJQ8RN-LQl_PCOwAi-49h7F5qehQ9nf62zzY4Iwc4vCmNqdVHYm3yuF_fjUyzJ59nr6-yExsc5vzLWwHz1WIu5dHDHzyUq6nCtrqdcHVib-16KDr_JRBVjpz5UfUVS43JJ4oagQdvx_DtBZyfG9WRYdHXPcbtFa9hyBGsVtxBJAQ6LjVJssHXXXunixCZPG6PrD9JnkGdMv_aFCINIFFPHWgWsyJ9Yy8WLu-VkW9cI8Q2nCuG8Odl_ZePjZ_m6zJ0J14DisCzVQvN9WkfZwOjydJnq9frw4pVEAyJiLNxrlcrwIe9_Tw8hJh2gLBaN2vFXrAki_88pMuI9mgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تیم منتخب جام‌جهانی ۲۰۲۶ از نگاه تحریریه ورزشی خبرگزاری فارس
@Sportfars</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451446" target="_blank">📅 20:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451445">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حملۀ دشمن به یک واحد صنعتی در خمین
🔹
دقایقی پیش صدای انفجار در حومۀ شهر خمین شنیده شد و گزارش‌های اولیه از هدف قرار گرفتن یک نقطه در این شهر حکایت دارد.
🔹
معاون امنیتی استانداری مرکزی اعلام کرد در این حمله، یک واحد صنعتی هدف حملۀ موشکی دشمن آمریکایی قرار گرفته است.
🔹
تاکنون گزارشی از شهادت یا مجروح‌شدن شهروندان در این حمله مخابره نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/451445" target="_blank">📅 20:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451444">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd9cf5511.mp4?token=DJr4wNbuI0lHTWeLO90I0ZGonLgVgA2lUepiKoENN7yAZF-GQ4f98aZjwPuVu5ISBxHnDVYRb3iHrlzirLeFqYKPT0EyxbrEdZlETBfJ3P9kL9-o1p24UcUXNHUv6wPMZrKSVHXHSkl-1Ngg69fY0zSSxLdeilcVzNsdExrF88zUUK66VTLqZBx0nFkNGE85R9ELQjlMKoR0c8AqMPRtZbjgi1vs8IZ74RrOPb3jyGPATF1s56h2ZE507umrxE7trLPIFqUS_d7OjIcY0SQ_HdBXwG9_Hto_7ZWJPB94BFbBfrfu2GZIhaVtCbFjBTwzalDhdtLs7jNd2K7orjfwvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd9cf5511.mp4?token=DJr4wNbuI0lHTWeLO90I0ZGonLgVgA2lUepiKoENN7yAZF-GQ4f98aZjwPuVu5ISBxHnDVYRb3iHrlzirLeFqYKPT0EyxbrEdZlETBfJ3P9kL9-o1p24UcUXNHUv6wPMZrKSVHXHSkl-1Ngg69fY0zSSxLdeilcVzNsdExrF88zUUK66VTLqZBx0nFkNGE85R9ELQjlMKoR0c8AqMPRtZbjgi1vs8IZ74RrOPb3jyGPATF1s56h2ZE507umrxE7trLPIFqUS_d7OjIcY0SQ_HdBXwG9_Hto_7ZWJPB94BFbBfrfu2GZIhaVtCbFjBTwzalDhdtLs7jNd2K7orjfwvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی مرحوم مهدی آصفی در ویژه برنامۀ محرم خبرگزاری فارس
🔹
مهدی آصفی ادیب، شاعر، گردآورنده دیوان‌های شاعران قدیمی و خادم اهل‌بیت(ع) شب گذشته دار فانی را وداع گفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/451444" target="_blank">📅 19:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451443">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دولت لبنان پس از چندین دور مذاکرات مستقیم با اسرائیل، ساعاتی پیش اعلام کرد که بر سر اجرای طرح «مناطق آزمایشی» و ورود ارتش لبنان به دو روستا با صهیونیست‌ها به توافق رسیده است</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/451443" target="_blank">📅 19:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451442">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
آژیرهای هشدار در مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین به صدا درآمد. @farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/451442" target="_blank">📅 19:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451441">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQ_hvrSzyxel4SHzkwkU3Y65iUf8ep3V6t0XeHEFtqYMd035KKOSGvjG-GOD9HfR8h3-Sh9MuDnPpmRKYBUmzTWVW-i1Qprg3HVUCDzPPCVi5LlewvsGjdhaPUAH3-EU9_UCfijUwdKY8dGogjuh2chYbAWubZICqwigqo3op9xfUXhe4T2Bt3TacZd_WHjBDqiYo_-ccLk1z8bXJNY08Q_2pL1r3LDvU8d1b222r6szQrQOGtDqCWMOd5ohawgZvCyRHmJXsSC4zcgh5Ny7Ffh-XYsaceSXAJiH_R1iKW5fbF2EbOozlCzBEMpqxKZ05ExBPbG7Wu3CVTaQiZrV-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: ایران برای توسعۀ فناوری از کسی اجازه نمی‌گیرد
🔹
معاون اول رئیس‌جمهور: اقتدار دفاعی و امنیتی کشور بر پایۀ پیشرفت‌های علمی و فناوری است. ایران برای توسعۀ فناوری از کسی اجازه نمی‌گیرد اما دستاوردهای خود را در اختیار کشورهای دوست قرار می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/451441" target="_blank">📅 19:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451440">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07e737a76.mp4?token=GIKka0v5hMwVsGYE2Fhlb0uJdYpNLsLnc24GgSXFJ0z9BvRWvIxFx8xWOsMorIi_U08hM93nnHfRhpvO_LqRxmsUuD03yLFZcGGbpCzJucw4afkFYJMwEXEFMMDdrpLKVjXBwf7oB-FYaFRkmsh3onUUJW4mBVAup6tXWmHk5MpJ7g13-Mb7t3vbAefGw9B_dRKQCu_6_GO-fpA9iijMkADuZwr7HV_fFYpLHE7gNaBLKDK1U8_J1IBQqq0-KTysJJQJ-9nOdVn7BX-B3ayTjCjz61NhQzxYFWSitkTMYkLLjbtoOsgt0YHJr3H3yR8mVWdjkEEHy7ZiqB-v9O0_cTe3-k7QWwZbwSMQnp5yj3xwuETTC0umlzOU80SG-hZdhJOYh5wwI53NA3q0JZesHmRXRu_gtHQnw92WmIOT-Nskq9Gd9X2diqt_oFMrk7sue7Ij2qtNIOciS4ryBHjOGdV9HdWViF_i4H0bgqiKyTbMQ4tc3QMpwQldxFvjOcX1vG_g6KHQc27bzfi7C941xsnJr6W7fTm_pYXLS74njdjkC1QIdmKF_wqoy8Im7KetDZLo2VRbM3ksj96ZL0-xiibiELy29u_diEfdNU38ARI82E_ae8VdhhoZphqXORBeAjVHh9DBohJEpZKj-1-TIQ47F3uM9Rvcra_x0NXAgz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07e737a76.mp4?token=GIKka0v5hMwVsGYE2Fhlb0uJdYpNLsLnc24GgSXFJ0z9BvRWvIxFx8xWOsMorIi_U08hM93nnHfRhpvO_LqRxmsUuD03yLFZcGGbpCzJucw4afkFYJMwEXEFMMDdrpLKVjXBwf7oB-FYaFRkmsh3onUUJW4mBVAup6tXWmHk5MpJ7g13-Mb7t3vbAefGw9B_dRKQCu_6_GO-fpA9iijMkADuZwr7HV_fFYpLHE7gNaBLKDK1U8_J1IBQqq0-KTysJJQJ-9nOdVn7BX-B3ayTjCjz61NhQzxYFWSitkTMYkLLjbtoOsgt0YHJr3H3yR8mVWdjkEEHy7ZiqB-v9O0_cTe3-k7QWwZbwSMQnp5yj3xwuETTC0umlzOU80SG-hZdhJOYh5wwI53NA3q0JZesHmRXRu_gtHQnw92WmIOT-Nskq9Gd9X2diqt_oFMrk7sue7Ij2qtNIOciS4ryBHjOGdV9HdWViF_i4H0bgqiKyTbMQ4tc3QMpwQldxFvjOcX1vG_g6KHQc27bzfi7C941xsnJr6W7fTm_pYXLS74njdjkC1QIdmKF_wqoy8Im7KetDZLo2VRbM3ksj96ZL0-xiibiELy29u_diEfdNU38ARI82E_ae8VdhhoZphqXORBeAjVHh9DBohJEpZKj-1-TIQ47F3uM9Rvcra_x0NXAgz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متفاوت‌ترین موتورهای مسافرکش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451440" target="_blank">📅 18:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451439">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای چند انفجار در بحرین خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451439" target="_blank">📅 18:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451438">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای چند انفجار در بحرین خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451438" target="_blank">📅 18:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451437">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id90Zd-TZOg1cY_tLF7Xc0g0VIlw-gVufwTx-sMwvwvRdIbdCwYAlCyETCbiNQb251lCz02_u22NgK6YCA4MMnaCr41r5NQavGvqttMhO2o2TapINkgOnliHe_GXV7xsPHaXr1BhBSGhrwh7zCljtPPGFBvazk8OoWTTDlZVT2GybkD3NX5MDuybbscEZkANwm0Kga1YLle-Zlsk63zk8usS8QzS3bIo7K8w8a4lFS8UH_V9MFzbVurNQZT67r8VTC4D9F9ccVHpzLlaRkIkeZqnCRGN-Ey45XWG6GZsE6d9AZJkoCsLv-91RKa7EyESnPqh_NfzVCJoIbWK6VD5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مدیرکل مدیریت بحران استانداری آذربایجان‌شرقی: در حملات بامدادی دشمن آمریکایی به اطراف تبریز یک هموطن به شهادت رسید و چند نفر دیگر هم مجروح شدند.  @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/451437" target="_blank">📅 18:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451436">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">طرح دوبارۀ آتش‌بس چه هدفی را دنبال می‌کند؟
🔹
طرح مجدد آتش‌بس از طریق واسطه‌های قطری در حالی مجددا مطرح شده است که آمریکا هم‌زمان سیاست فشار و حمله به ایران را دنبال می‌کند. همین تناقض، این سؤال را ایجاد کرده که آیا هدف واشنگتن پایان جنگ است یا ایجاد فرصتی برای اجرای مرحله بعدی نقشه خود؟
🔹
محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در واکنش به این پیشنهاد نوشت: «آمریکایی‌ها روی هوش ما اندازه آی‌کیوی مختصر خودشان حساب کرده‌اند. ما در شناخت این آمریکایی‌بازی‌ها به مرحله استادی رسیده‌ایم.»
🔹
این جمله، پیام روشنی دارد؛ پس از تجربه‌های مکرر عهدشکنی آمریکا، بعید است در ایران کسی آن‌قدر ساده‌اندیش باشد که صرفاً با یک پیشنهاد آتش‌بس، دوباره به واشنگتن اعتماد کند.
آمریکا منتظر چه اتفاقی است؟
🔹
تحلیلگران معتقدند هدف اصلی این آتش‌بس، خرید زمان برای ایجاد یک فرصت داخلی است، نه پایان جنگ.
🔹
در هفته‌های اخیر، هم‌زمان با مطرح شدن برخی مباحث درباره مدیریت ناترازی سوخت و احتمال اصلاح قیمت بنزین، رسانه‌های معاند نیز تمرکز خود را بر تحریک افکار عمومی و دوقطبی‌سازی جامعه افزایش داده‌اند.
🔹
واقعیت این است که دولت با ناترازی جدی در حوزه بنزین روبه‌روست؛ ناترازی‌ای که بخشی از آن ناشی از رشد مصرف، محدودیت واردات و تغییر شرایط تأمین سوخت در پی تحولات منطقه‌ای و جنگ اوکراین است. طبیعی است که مدیریت این وضعیت نیازمند تصمیم‌های دشوار اقتصادی باشد.
🔹
تحلیل غالب این است که آمریکا امیدوار است اگر این تصمیمات به اعتراضات داخلی منجر شود، بتواند از این وضعیت به‌عنوان یک فرصت راهبردی استفاده کند؛ یعنی پس از شکل‌گیری التهاب داخلی، فشارها و حملات خود را از سر بگیرد تا ایران هم‌زمان در دو جبهه خارجی و داخلی درگیر شود.
🔹
اگر این تحلیل درست باشد، پیشنهاد آتش‌بس نه نشانۀ تغییر رفتار آمریکا، بلکه بخشی از همان «آمریکایی‌بازی» است که قالیباف از آن سخن گفت؛ تلاشی برای ایجاد اعتماد کاذب و انتظار برای مناسب‌ترین زمان جهت اعمال فشارهای بعدی.
🔹
ازاین منظر، مهم‌ترین راه خنثی کردن این سناریو، بی‌اعتمادی به وعده‌های آمریکا، مدیریت هوشمندانه مسائل اقتصادی، گفت‌وگوی شفاف دولت با مردم و ناکام گذاشتن هرگونه تلاش برای تبدیل مشکلات اقتصادی به آشوب اجتماعی است.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451436" target="_blank">📅 18:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451435">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سخنگوی دولت: برنامه‌ای برای افزایش قیمت بنزین نداریم
🔹
مهاجرانی: دولت هنوز برنامه‌ای برای افزایش قیمت بنزین یا اجرای نرخ سوم بنزین ندارد.
🔹
در صورتی که برنامه‌ای در این زمینه وجود داشته باشد، به صورت شفاف اطلاع‌رسانی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/451435" target="_blank">📅 17:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451434">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7vtZhP1NxPQtZVZPgA3myFbhuwub6cErcHIKF7Zbd-aNXZwg4Xq3bqcaEc8CgSX7TdaH5O9uNozfUIes1eeDVUN_nbvzexSXIGq8MAmdjNfIZv-a7Ypt2XviOTnXJpdw9NWOJtwNF4COLh3jEP2d1pgTUM38UemyxHro4xs94Wg01YIBbiiO8XwD6PaZDDfzRKUaSJI9O9W9gIenqbvDpjcMs1Dxy4nKt9djppouPSHf9o6HxqvjvWmDDhfh3wmeFldJMgWBaJ0xbupr8rGmMXyHWBmI37hIc1LC57Gymac7ZDh5y6Jrd7prEioKMAH5TYpsgGDVx6u_EYf3lLUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت هومن حاجی‌عبداللهی و جناب‌خان به آنتن تلویزیون
🔹
تهیه‌کنندۀ برنامه «قصه‌های هومن و جناب‌خان» در گفت‌وگو با فارس اعلام کرد این برنامه از شب اول ماه ربیع دوباره روی آنتن شبکۀ نسیم می‌رود.
🔹
این برنامه پیش از ماه محرم نیز در قالبی طنز پخش شده بود.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/451434" target="_blank">📅 17:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451433">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شنیده‌شدن صدای انفجار در شیراز
🔹
دقایقی پیش اهالی بخش‌هایی از شهر شیراز صدای انفجار از محدوده شمال غرب این شهر شنیدند.
🔹
خبرهای اولیه از حمله به یک نقطه در شهر در جریان این حملۀ هوایی دشمن حکایت دارد.
🔸
به گفته استانداری فارس، این حادثه هیچ گونه خسارت جانی درپی نداشته و تیم‌های ارزیاب در محل حادثه حضور یافته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/451433" target="_blank">📅 17:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451432">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c258107e1b.mp4?token=CL2Q_5d3FTmVzejXhyv6CXvaOZMk9HzgDHHL0O1XipVchZ8JFuFmYJgk2LXTwqNookD0xzL7IGXUtDb-SlDJWMHzf4F1CU4GQKw5ZGSQT2jgk2oOjm05i8HTt_jdgfnKDaldw_PSJmq9H37D_z6j3LJ6wn2YB-SJ8TIC3tA1uF9uiIRRBj-nQZRf33u9JpvqDVICyA4yUhjAP5_6d10dqU4fNJdnI_QxbyiqzNIY3XuwPeO-gyNcfrcs3b-U9rvd69OlPCl5qpdW_uRmXsGx8IXWpYSQHVn-DOoZT4Ja1X9XJLHqnU_VBlaZLW__6cu9lpvgmSjmc3WNIMWtHOBsXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c258107e1b.mp4?token=CL2Q_5d3FTmVzejXhyv6CXvaOZMk9HzgDHHL0O1XipVchZ8JFuFmYJgk2LXTwqNookD0xzL7IGXUtDb-SlDJWMHzf4F1CU4GQKw5ZGSQT2jgk2oOjm05i8HTt_jdgfnKDaldw_PSJmq9H37D_z6j3LJ6wn2YB-SJ8TIC3tA1uF9uiIRRBj-nQZRf33u9JpvqDVICyA4yUhjAP5_6d10dqU4fNJdnI_QxbyiqzNIY3XuwPeO-gyNcfrcs3b-U9rvd69OlPCl5qpdW_uRmXsGx8IXWpYSQHVn-DOoZT4Ja1X9XJLHqnU_VBlaZLW__6cu9lpvgmSjmc3WNIMWtHOBsXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش‌هایی از انفجار در شهر نیویورک آمریکا
🔹
رسانه‌های محلی از وقوع یک انفجار در نزدیکی یک ساختمان دولتی در شهر نیویورک آمریکا خبر می‌دهند.
🔹
طبق گزارش‌ها، صبح امروز به وقت محلی صدای تیراندازی و انفجار در شهر نیویورک آمریکا شنیده شده است. تصاویر منتشر شده از دستگیری یک مظنون حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/451432" target="_blank">📅 17:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0451456d.mp4?token=YVykqmOGxfvv6Mm3XfUgp9QSE_DvVLnMq5_Ntaxl6ZiyGfK1Rj8_v4KgbVWDqB8jecHePCHGqUrQqXX6d1jGyDg1J3M5szoxjfruw4zUSW-BIqwpBUBalzl-M_L0hnn2jfpuoAzHMEjCZiLNgOeSJCY4bjP_WICttZPA0en0LeO4LsoXDYYRXDP-Fr4Yxd4TYMP3JPcecFJzkXHXXg-z2JfpT7C4mTWg2d1tDwiQcP_46buer4hZ4DaOHfUAr6maYnAqPgiugs0MgkfetwwopSadIpp9qupyo9Fui6Xy47GlRqP_6At84bsMeGaYO0APdPTK3lPT5dcinf_PzBS1ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0451456d.mp4?token=YVykqmOGxfvv6Mm3XfUgp9QSE_DvVLnMq5_Ntaxl6ZiyGfK1Rj8_v4KgbVWDqB8jecHePCHGqUrQqXX6d1jGyDg1J3M5szoxjfruw4zUSW-BIqwpBUBalzl-M_L0hnn2jfpuoAzHMEjCZiLNgOeSJCY4bjP_WICttZPA0en0LeO4LsoXDYYRXDP-Fr4Yxd4TYMP3JPcecFJzkXHXXg-z2JfpT7C4mTWg2d1tDwiQcP_46buer4hZ4DaOHfUAr6maYnAqPgiugs0MgkfetwwopSadIpp9qupyo9Fui6Xy47GlRqP_6At84bsMeGaYO0APdPTK3lPT5dcinf_PzBS1ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی حسین طاهری برای مردم جنوب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/451431" target="_blank">📅 17:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451430">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960a5e081d.mp4?token=DT8YDRxVOg21MS6pU4WhtWaW1vsD45hham32L0ZBSQkhymSBSAyQf0aWNX_120O5OAOVmfco18e3IvQnYRzct55EnMCMvvSchT9nrv6frFTZAr1dph1f97RvsiYgyFSlED-aW2jHydzyPoP5CuMBDBrV8kaoCAXxVNB-n1g44cnt3PnYuCC7KaZtZ05fwWxLKOTFlT5i1qXOLBCivnyps_saqm2xJfSg7z6zckL074JP2ivU2x0U7NC-ZGGO-SdUOrLAMqqaHsuT-R_p4ElRPes3AGxBzw_VoTpyCkjLxxmwkC1cc4kJJZGzbKnxak7Sq6CzYVFRdTAQXbnBxDXsXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960a5e081d.mp4?token=DT8YDRxVOg21MS6pU4WhtWaW1vsD45hham32L0ZBSQkhymSBSAyQf0aWNX_120O5OAOVmfco18e3IvQnYRzct55EnMCMvvSchT9nrv6frFTZAr1dph1f97RvsiYgyFSlED-aW2jHydzyPoP5CuMBDBrV8kaoCAXxVNB-n1g44cnt3PnYuCC7KaZtZ05fwWxLKOTFlT5i1qXOLBCivnyps_saqm2xJfSg7z6zckL074JP2ivU2x0U7NC-ZGGO-SdUOrLAMqqaHsuT-R_p4ElRPes3AGxBzw_VoTpyCkjLxxmwkC1cc4kJJZGzbKnxak7Sq6CzYVFRdTAQXbnBxDXsXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجات معجزه‌آسای موتورسوار نوشهری از برخورد لاستیک سرگردان تریلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/451430" target="_blank">📅 17:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451429">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4ac0667a.mp4?token=d0h1JKq1AbFxbyFm-HE-fZ5cj-2A5JjQXdHnNAatTrhDRmGkqTT6Q9x10sr1egLWLEgGOTfcNxk72UE8Ffj3yqghDw0spewdsKMtcdr46CKjdCjpB6b4tmvlHSTEmOzMsDprw8HEkE8-FRyOSNvpMAIQ90lwuJlOrvVJIIYF0phiUbO33ZA4cT-wGLusgQMVI2sf3UwtNlLacdHcnM6MOrY4adn1refI-xPv2Ip7OKTUhamFNw8J9BvQD9ngMjAx96T48pKB81rSDiUsRXGEF3atwpHRDVTJs2UNvR8mf9K1765XndUWWs7HEy4-38nuEN9r-pnW4IHCPu1OAIefTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4ac0667a.mp4?token=d0h1JKq1AbFxbyFm-HE-fZ5cj-2A5JjQXdHnNAatTrhDRmGkqTT6Q9x10sr1egLWLEgGOTfcNxk72UE8Ffj3yqghDw0spewdsKMtcdr46CKjdCjpB6b4tmvlHSTEmOzMsDprw8HEkE8-FRyOSNvpMAIQ90lwuJlOrvVJIIYF0phiUbO33ZA4cT-wGLusgQMVI2sf3UwtNlLacdHcnM6MOrY4adn1refI-xPv2Ip7OKTUhamFNw8J9BvQD9ngMjAx96T48pKB81rSDiUsRXGEF3atwpHRDVTJs2UNvR8mf9K1765XndUWWs7HEy4-38nuEN9r-pnW4IHCPu1OAIefTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ضربات سنگین نیروی دریایی سپاه به ارتش کودک‌کش آمریکا با حمله همزمان در سه محور
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/451429" target="_blank">📅 17:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451428">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
وقوع چند انفجار در کویت
🔹
در حال حاضر، آژیرهای خطر در کویت فعال شده است، برخی منابع از حملات همزمان پهپادی و موشکی به مواضع آمریکا در کویت خبر می‌دهند.
🔹
ارتش کویت ضمن تأیید این حملات، ادعا کرد که موشک‌ها و پهپادهای شلیک شده را رهگیری کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451428" target="_blank">📅 17:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451426">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av4lxxwcfxqIKlRTJqC-TaWI9OZuVo2TtE75v9p6uYW2cl-IQBcjTYqGq8laPHp7gzX_HNVB2F3jyYXh83PuY7tC6K94Tn8IdbjvRLjsRp_BghI4p8vykpFUfMhLEcj_bWGkGaEeNrF3SQvp6x_lyTDQT6IV4czTRTk8zH3NOn1EWhuLR9IUr8qCcVO4Pml3spDywSCBFBLo4taTiWMAq9PD6xlntvmmooD3HCWo09eX8Q0GZ1E7k3apHf0anyFi_eIER3647OLpZ9L0vReJuH5aQwiTDh9y2Gn4RsyKL91UmW58w5uqojtJMyU6OLoTb7Q7PUtu9A-NOoh6AHSVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07f18e551.mp4?token=e-7Ij7flrW5YmuiYxpGPj3FcQ63hqzDk0Ya-ROPBWrXNIQgzPMuqGCMqjj6vJ2ONa9-2-GKeMkspMH3lZI9UDoyka7mLWKxbzTqss63C2tf84lJ2FC4YffeXBWG1f_OYJGuH7bwU7EL5G4c8oYbwAahSVyauDwIRjDuz7_9NJih2glKLQQc7maKHYYJUMF81d-x9gDw4uuf0BVmTHJzYVY9oAjpTRuqZqOFyzRr6HygEbIsRBDnoLjPMHaPC91J8ngunC4yVQdM0K7pDG1fTeyhOty-Yri6L6S9dFXOlNOEHOnkjBNQL1f_iP8Gppk39itAgpR_bJ-KWJDE08M-qZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07f18e551.mp4?token=e-7Ij7flrW5YmuiYxpGPj3FcQ63hqzDk0Ya-ROPBWrXNIQgzPMuqGCMqjj6vJ2ONa9-2-GKeMkspMH3lZI9UDoyka7mLWKxbzTqss63C2tf84lJ2FC4YffeXBWG1f_OYJGuH7bwU7EL5G4c8oYbwAahSVyauDwIRjDuz7_9NJih2glKLQQc7maKHYYJUMF81d-x9gDw4uuf0BVmTHJzYVY9oAjpTRuqZqOFyzRr6HygEbIsRBDnoLjPMHaPC91J8ngunC4yVQdM0K7pDG1fTeyhOty-Yri6L6S9dFXOlNOEHOnkjBNQL1f_iP8Gppk39itAgpR_bJ-KWJDE08M-qZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲ کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و ۲ کشتی دیگر از ادامه مسیر ناایمن منصرف شدند
🔹
نیروی دریایی سپاه: ساعاتی پیش ۴ فروند کشتی متخلف با شیطنت و حمایت تروریست‌های امریکایی و با خاموش نمودن سامانه‌های ناوبری و بی‌توجهی به اخطارهای پایگاه کنترل تنگه…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451426" target="_blank">📅 17:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451424">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ضربات سنگین دریادلان نیروی دریایی سپاه به ارتش کودک‌کش آمریکا با حمله همزمان در سه محور
🔹
ملت به پا خاسته و حماسه آفرین ایران اسلامی، با توکل به خدای متعال و دلگرم از حضور هوشمندانه شما مردم بصیر در صحنه، دریادلان نیروی دریایی سپاه با حمله همزمان در موج ۲۳ عملیات نصر۲ در سه مرحله با رمز مبارک یارقیه (س) ضربات سنگینی به نیروهای تروریستی آمریکا در منطقه وارد کردند.
🔸
مرحله یکم: حمله به سوله‌های نگهداری و تعمیرات پهپادی واحدهای آمریکایی مستقر در فرودگاه اَلصَّخیر بحرین که منجر به انهدام آنها شد.
🔸
مرحله دوم: حمله به سوله‌های آماده سازی شناورهای تی‌اف۵۹ در بندر سلمان بحرین که منجر به تخریب آن گردید و خسارات سنگینی به شناورها وارد آمد.
🔸
مرحله سوم: به آتش کشیده شدن سوله‌های محل استقرار و پشتیبانی و تجهیز نیروهای تکاور ویژه دریایی در پایگاه عریفجان کویت و منهدم شدن آن به صورت کامل.
🔹
حملات کوبنده رزمندگان اسلام با انبوه موشک‌ها و پهپادها در مقابله به مثل و پاسخ به تجاوزات ارتش کودکش آمریکا ادامه دارد.
🔹
رئیس جمهور بی‌خرد آمریکا که بارها به ناآگاهی و بی‌خردی خود از اوضاع عالم، اعتراف کرده و می‌گوید بدون اطلاع از عمق نفوذ امام شهید ما در مردم جهان و عشق و علاقه عمیق مردم ایران و سایر کشورها، ایشان را به شهادت رسانده و اینکه می‌گوید بی‌خبر از اهمیت تنگه هرمز در اقتصاد جهان در این منطقه، جنگ به راه انداخته است، شب گذشته باز هم بی‌خردی و ناآگاهی خود را آشکار کرد و اظهار داشت تعداد موشک ها و پهپادهای کمی برای ایران باقی مانده و رو به پایان است.
🔹
رئیس‌جمهور قاتل آمریکا بداند اگر این جنگ چند سال طول بکشد به اذن الله تعالی تا آخرین روز آن موشک ها و پهپادهایمان بر سر جنایتکاران آمریکایی خواهد بارید.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/451424" target="_blank">📅 16:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451423">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7Gb600dWlAN0GOWRUr3xiXsTCarpDR-t5cvdO-r7F6kJKRmTSEDPckBwVDHR72rvUMl_kpn6zFG73C1Vkakzs4Xizf8RO_Mxxr_pERQazVMdu5g-Bfm1WeX5BL1N7AFwgvXZ1pcMkLS6psSOy7ucVAbdgR1kt-i9hjVaujb4wdlDJV5b9ShgOFKMleRfgLlUSwvR9gSheDMuoJDEVdyz1Z-RwbE4Ljata9HCWAxrKOp0k0YtS81iUuZLcbs6NwY2U0YugE972pzKtHDdL7aU0aoPqG0u13Qgx0T2EIJnjtZAkRRdqUpSn304QUdok_TlJDSEurokZaSVcigksKjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور عازم پاکستان شد
🔹
وزیر کشور، در رأس هیئتی متشکل از دستگاه‌های اجرایی به دعوت همتای پاکستانی خود راهی اسلام‌آباد شد تا راهکارهای توسعه همکاری‌های دوجانبه را مورد بحث و تبادل نظر قرار دهد.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451423" target="_blank">📅 16:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451416">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tm-Aj9ZwO5M7-4F4C0BE6efvpoJkdVW6ZAKx8kLC8c-IDQQiU3VTzY4b31Vx5lDJS6R-WlFfkDhOCsZFiqmug8zfkJzFtpqRw4jXodsyd00YCtjQMDEj-FnHll-dGvqwQGjrAZALRD7ojfEhx2P7yD9z5tG1leI0b86KOtxZfuW1lCdfwvDI9O0OhMvO8yqkV1GjSUCtzU5D8BbMzEqQ6HjifXSxvHEqRUmg695470GdSIndpVpL9pWVC_3Y1PEZiMsj0mc6PBbpqTeEdhgciX3aAqXS6pkKu8fhUJL_ew_ivd_Ifw5dL3LKo9PNBOmbKNp0dZ7MF1rH7zonMfs_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzYRd35THDbE-MUi9xKBSOORpyfBynt3TyWBl4GXExAANVLB4J_AGuivHWiLqfFY70khVZvvd0EtrYR5vbyOeWY19EjOImQ1x84m8S39wN9CgAZb_LbAC3nd0N6VQPQVr-eMSScESndSHMgCj_QLtO_btnruWAnAHDxJoznP1Xr9IvumFwrcRWi0mFeg9oprv8ZxNc_7ziiRSxSTmDMJbhdLTtCrr8UBFv2cymjpFlyAoLliJIBxQfCof912WG97SzOet1YdRbJOaMr6OzA7tQqBjz6545_dabF0tedW21GIraqz8s04qTvMtOBofFKdhGZ4P1iuJljBjmrOhYICUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQeBOdugb9lW2DCX8GAe_zWOR37N8XU_G5Doj-YJOC6ZOxVo3gmIzgwlz8kf0Jl5pGO78llyAMbNPhnsB3bCBVtS5CVSaecFPuTNAytC36BxreXcI1uOj3t0GBoblZ-gKE-Az4ApBQJY6OLxgz8SLe32DOKhjP9ROLIzzDoqDenEje-H_3Q49Uhk8jgdqBih9DEBMynwtCDcEy_oB2VcdfkEfxTXjD1VbkZqPekfNAMgiMEgz7mNTK5dyTR5cj7KPdKR5Bvjzk3r3h7w0_NidLZV-4ZyCiaPi5lvL387JRI4morjIeIUvkVcsaKikoIoVIjBkgwKr3tPmV21df3uHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjJNEZm-D0KWk3QJ2q2jEXhorISeZO5BJuO8FAXtdq34CXYGfzfShyv9ssGdLOTp5uX1T6Ipt7SyUBrjcKZWH0NZw62kVciTI_PhHymfQSCep1VRY_dW9vzvmPF28rAo-Bvqml5Y54Ysa2BJ2HE9IWMvTn9dKfdKUZXjATM15Q7tLW-Ex9_C6Yv3JnXOm5kDF7xF7ir_gY6VYvvhgizg_FeOyo1Hr39PBRqqTAL37mgYAjfa6XO9yG3KWUnP_QktIRKKFHbPzwf_wyowLsRixOMjHu7E8YtaHf_NQbOsxD2SLK6h6tt7RHZu67HLVFl9e7fSZFYP9BdmS-c9t5g0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ThNMnzZ2qz6sM5P19CvnfK1FMpR6QrwMMyVytvF4azk3tmqpq0Ed-i6K8JiR8daHHQ2PIYlf2ThtBTJBXgfBTzqRPcX0EyKMg2XWwOnEpmfjOQcqeD9lmufI60raRloY2zm4HsRguTDk9UdoZutnpCEeU4bU0Opbso5Z7HPiIB-6A_nSJ0mW-llt7-51RfcWg1DPf5TYlrIel4Yh9BkWsjGL8vahpKAtwBxrtGdHLvMdcE35Pe7W_HpiowFWIUJeVLzMfGj-ujWYtt4pKupAf5aa8WyemPXAmZCRLmdnGZYalT55QfxkdR1ahdx2zxZq0R5U_NOeWnCVmGcwxS2_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlI-dQmyeEnrMzJhhpflMpFT099rLwPslnD10JIcvfSFJnsqiVvQB5aW7ofG-65SD9Oclruh94KCErfwOSmXwrN3XkalhH5Z92RDeZ-X6FhW6IT4dq6d7L88idhyjtobkw1eIXVhzKkSMjqDnc9SbsagS4szrSebrp0rtMZzqimwNnQYCM9sPxOglyjpOvxazC0_WM0Y36fBLC2BW_H8Rs3K3Z559pIaG1y24sXVEkqHyJhLJ_2o3ZC0PmPxCiXT18sw-y5qwLkFaqSwscleHU1lyxacoQXoar4dYVCcH2pmVDfgp2NfIPG0d1Jr0rz23wC8elNnvCMraDA2Kh8TGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WoU80MeGVRWk5tNse731aHvQmV3G0hCg182_TFRpgCOoVoBY8cAGSpaz0SOTbbCNYvUWq_PoDmbqV9OhzYVb5i35JWwj93Rv_W6CpBgaAZfAKkBTtb6uwgCBhDx0SxjHlIx4xyivvYweU6GcPaLlDOrXovrB5-B6zgeeGDmkGyTteP4A7re9CI9u7vV4pWNRSCOL5SAZEZvDG3UMWDU8bmALqWPwVT6xS0xsTtX7YWkf0o1MQCoe8ZLlNoagBO5tz8uCnywVV3fYHqdd1-TAiE7Li3sdXMSfANua1-uDh86ms5PSID86jNftJzml4x6HJVGaoO7-SR9DohColyf8dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سفر چهره‌های فرهنگی، هنری و ورزشی به جنوب کشور
عکس:‌
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451416" target="_blank">📅 16:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451415">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
وزارت کشور بحرین: هشدارهای حملهٔ هوایی فعال شده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451415" target="_blank">📅 16:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451414">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCIlXHvzVeQYH7OAtTugd31U4Tdkf1ktEItbK12Hk6YtMKO130ZMOhCSnrN1wStdF6RiUarddmoXxgNPBeEe6IgPAWY5Khkqk0PTYGrFiJBAkPVQVIj7yyLxBHao-YE1utRF-MRr5liMNTWyyvkvEGLEOD06d52BSnPfSygpcxFqr0LUqUhL1axoXYQVNtPe8yWZDYDh5xjKaYuEaT0Fwki3skHtJVYreNbOlYZ5MN0WMIbVwRpVa0IsnZ1Qt00TYZn_iasd1VMSyRZ8UAK1IvSaHtZ3526ntyvPCIBqvcUPXLqQCBRBz7kwEUVVVdZQ9234M7Q96I_jzwUL6JZuIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش دمای هوای پایتخت تا پایان هفته
🔹
هواشناسی استان تهران: کاهش دمای هوا از فردا آغاز شده و این روند تا روزهای پنج‌شنبه و جمعه در بیشتر مناطق استان ادامه خواهد داشت.
🔹
از روز جمعه به بعد، روند افزایش دما آغاز می‌شود و پیش‌بینی‌ها نشان می‌دهد این افزایش تا اواسط هفته آینده ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451414" target="_blank">📅 16:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451413">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE_3TDI05lY8Aaqc4Q_khK7QXoV-9L2XJj62spaIZMlIPSiZZ575kYN1r7vwevTuEXEpOPXVoFU9ajWjGtMMSV4GXtvG8hZOTgTN3Wv8Y9efie4_QJEwSDKwsI5j08CSEVghkTR52vJzlr9gGr6Ph7Doa-9qoR_5cgTupMNolxNnUaMfGKvRNYmCXV1hf8rBZ6U0cnn1utZ3mTpiftAGYXq1UugVPFs5Ccu58Hs3Yu66aKpLCRt561mwOKfHdwqQXFr9aUwjcpDcdlGGrlElOJ9XVAEHIXACHbeuhmA2QbIHzyNkyEqSzvJ0l_fWgIdgYNx1hChYhmrRkqW-Ge8Isg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با آغاز فروش بلیت قطارهای مرداد سامانه از دسترس خارج شد
🔹
طبق اعلام شرکت راه‌آهن پیش‌فروش بلیت در تمام مسیرهای ریلی از ساعت ۸:۳۰ امروز آغاز شده که در حال حاضر سامانهٔ فروش بلیت از دسترس خارج شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451413" target="_blank">📅 16:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451412">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4ZPJUbNI_Hl-3Ju7UaAfP8O2zrWEWD1folMUa9SGNu2r5Hp58EqPZiM-Ub02JxzOnt0JM-ClpVPL_yD7ZBs1rMyAAxnBueyJADdgf1RdUxPBJp-37RtGEdjhAoQrowseoAOkUQupKG2iZ42P8742u45MBeoQe3ktkWG__SwAnH7aRr8g0ZEZ8MC1UQSj5G9BuwV8i2VRNwZh8mBvVhQtg9O7hDLmNxjhGI1kPwnnHz_xKWGMoJeX7n3WEwDbuFlchFxjzAfN_jzYhAKGrSBGYidvqrBpmjtof2RJo9qXvqzKyBpUvPkXttwBZ3NPnQooLxXOChdizxbsj6cD7_yjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬅️
افتتاح باجه بانک شهر در زنجان؛ گامی تازه برای توسعه دسترسی شهروندان به خدمات نوین بانکی
👈
باجه بانک شهر در شهر زنجان با حضور دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر و جمعی از مسئولان استانی، به بهره‌برداری رسید تا با توسعه شبکه خدمت‌رسانی این بانک، زمینه دسترسی آسان‌تر شهروندان، فعالان اقتصادی و واحدهای تولیدی به خدمات و محصولات نوین بانکی فراهم شود.
⭐️
به گزارش روابط عمومی بانک شهر، دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر در مراسم افتتاح این باجه بر رویکرد توسعه‌ای بانک در گسترش خدمات‌رسانی به هموطنان تاکید کرد.
دکتر احمدی اظهار داشت: یکی از اولویت‌های اصلی بانک شهر در سال‌های اخیر، ارتقای کیفیت خدمت‌رسانی، افزایش رضایتمندی مشتریان و ایجاد دسترسی آسان‌تر، سریع‌تر و مطلوب‌تر مردم در سراسر کشور به خدمات متنوع بانکی بوده است.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/451412" target="_blank">📅 16:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451411">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYSpMQWL-fJBOnXYBsb2IKiXQ2HzMZMOWK17g70W4wLRsnfVVBHphJLOj5HBKg-8PFnkUkoz_mwvfe3quLWc03e6eH50ip8Em2wej78j1ECqSMhGtkiwSylr1z8AkHRqjN2DNhyfh_ov8dfO4-ZLKUYJaiIKfKi52nOiR2_3u8CcT2ECuGRyH0ClNnYuGitHcrP8BlXeQnkMj4nWJlJqm4b8z5Y29jZ957Ub-jPBNSdC8J7Z9VMvFqC0eOrs9KyjUF9DodzR3DepxUFA70qHz8qLPBcq_Iw-5mJNgThvYf_KmTcKJh0e1_fsIrFq3Md899vS00ZpFQ_x0rkm9kM7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/451411" target="_blank">📅 16:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451410">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/451410" target="_blank">📅 16:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451409">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فرماندهی کل سپاه: با همه وجود، هم‌صدا با ملت بزرگ ایران، فریاد «لبیک یا خامنه‌ای» را از ژرفای جان سر می‌دهیم
🔹
فرماندهی کل سپاه پاسداران انقلاب اسلامی در لبیک به پیام راهبردی فرمانده معظم کل قوا: ما سبزپوشان حریم ولایت در سپاه پاسداران انقلاب اسلامی، پیام حضرت‌عالی را فرمانی نافذ، میثاقی الهی و نقشه راهی روشن برای استمرار رسالت دفاع از عزت و استقلال کشور می‌دانیم و با همه وجود، هم‌صدا با ملت بزرگ ایران، فریاد «لبیک یا خامنه‌ای» را از ژرفای جان سر می‌دهیم.
🔹
میثاق می بندیم که پیوسته امنیت، استقلال، عزت و پیشرفت این ملت را ستون‌های ایمان، توکل، خوداتکایی، اقتدار ملی و تبعیت از ولایت پاسدار باشیم و هرگز سرنوشت این سرزمین را به وعده دشمنی کودک‌کش که کارنامه او آکنده از عهدشکنی، فریب و کینه با ملت ایران است، گره نزنیم. تجربه‌های بزرگ این ملت، ایمان ما را به این حقیقت راسخ‌تر ساخته است که راه عزت، از مسیر مقاومت، هوشیاری و اقتدار می‌گذرد.
🔹
فرمان حکیمانه حضرت‌عالی را نصب‌العین قرار داده‌ایم و اینک که آمریکای جنایتکار بار دیگر راه خطا، تجاوز و ماجراجویی را برگزیده است بر این میثاق استواریم که ، «درس فراموش‌نشدنی» را که نوید آن را فرمودید، با قدرت، قاطعیت، حکمت و اقتدار به او خواهیم آموخت؛ درسی که هر متجاوزی را از تکرار خطا بازدارد، هر طمع‌ورزی را در هم بشکند و حقیقت اراده شکست‌ناپذیر ملت ایران را در حافظه تاریخ و ثبت کند و مسیر حکومت جهانی مستضعفان را هموار سازد.
🔹
در اجرای تأکید حضرت‌عالی بر حفظ وحدت و انسجام ملی سپاه پاسداران انقلاب اسلامی در کنار سایر نیروهای مسلح، صیانت از همدلی ملت، استحکام جبهه داخلی، پاسداری از سرمایه اجتماعی انقلاب و جلوگیری از هرگونه رخنه دشمن در صفوف به‌هم‌پیوسته مردم و نظام اسلامی را از مهمترین وظایف در منشور پاسداری از انقلاب می‌شمارد و بر این باور است که اقتدار دفاعی، در پرتو وحدت ملی، استوار و نافذ خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451409" target="_blank">📅 16:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451408">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
🔴
یمن محاصرۀ دریایی بر عربستان اعمال کرد
🔹
سخنگوی نیروهای مسلح یمن از ممنوعیت کشتی‌رانی و محاصره دریایی بر عربستان براساس معادلۀ محاصره در برابر محاصره خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451408" target="_blank">📅 16:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451407">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8280446ccb.mp4?token=ZQmeVa9RZtdYSmXti3yWxpGBQnte6vT3rEkUWNkyte_RQ7E9aqnbw50Q0sQ08BhIaWUvzY90Vu-ujSqtGlrc8v9Z9CxBfPcEDG7mjoPzrCqL1aC8gPLxL17iYDyh6O_f6JLeYIO5YSnL7Ijh8531tPNv8RbM_Zgc59EqG3mIPxVI0h9sd-0TRGHTojcy15iVF5L7vBdp0-P4kjLscqRIIN7r09s_lgLCAFRvt0O5d87dt_Ee4cGO9_h6jXmXM9Rbp0MJo_HTs_zgnZgx_aIZri3cVWoIwv1HU7txkigrl49vlyoxoFvObvv45U50_GKoswEs0tpgxGmwe858uy1jFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8280446ccb.mp4?token=ZQmeVa9RZtdYSmXti3yWxpGBQnte6vT3rEkUWNkyte_RQ7E9aqnbw50Q0sQ08BhIaWUvzY90Vu-ujSqtGlrc8v9Z9CxBfPcEDG7mjoPzrCqL1aC8gPLxL17iYDyh6O_f6JLeYIO5YSnL7Ijh8531tPNv8RbM_Zgc59EqG3mIPxVI0h9sd-0TRGHTojcy15iVF5L7vBdp0-P4kjLscqRIIN7r09s_lgLCAFRvt0O5d87dt_Ee4cGO9_h6jXmXM9Rbp0MJo_HTs_zgnZgx_aIZri3cVWoIwv1HU7txkigrl49vlyoxoFvObvv45U50_GKoswEs0tpgxGmwe858uy1jFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ علیه ایران به روایت کارشناسان آمریکایی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451407" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451406">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c00107617.mp4?token=S2yjcs7hyKXvbNmLBW0KYaZVcgivsBhXlptMuZIc989JfHJU3GhQzAYIk72J95pNq4dn03U2ztObCip-EKUo7fGaDX0xUJSrnWEIsr7vpmhdKdfLCMmZz2wsHyKRWGD5mYZFXqSbsykQ7uRKHl_uyMtT75j5yMi3y2wXh_nHi7uOG6wigZ4e14v9Fl-ygu3_9irp8NPsoSxlD3qjUG_t7nFxSzVzEw1awaHYm1whm96y0vwos9MHZhayj6-nMd9hWgeFNA6nYjoBj51ZX-g6Gum9cIsDx8DAYqiK9KHRv7U9hTLqBlzbwbbCkzai7a2NWwrv1sOGQKwNAZuii0bsoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c00107617.mp4?token=S2yjcs7hyKXvbNmLBW0KYaZVcgivsBhXlptMuZIc989JfHJU3GhQzAYIk72J95pNq4dn03U2ztObCip-EKUo7fGaDX0xUJSrnWEIsr7vpmhdKdfLCMmZz2wsHyKRWGD5mYZFXqSbsykQ7uRKHl_uyMtT75j5yMi3y2wXh_nHi7uOG6wigZ4e14v9Fl-ygu3_9irp8NPsoSxlD3qjUG_t7nFxSzVzEw1awaHYm1whm96y0vwos9MHZhayj6-nMd9hWgeFNA6nYjoBj51ZX-g6Gum9cIsDx8DAYqiK9KHRv7U9hTLqBlzbwbbCkzai7a2NWwrv1sOGQKwNAZuii0bsoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: سامانۀ رادار اخطار اولیۀ دشمن آمریکایی، یک سوله تجهیزات و قطعات هوایی، و یک آشیانۀ پهپادهای MQ9 آمریکا مورد اصابت قرار گرفتند
🔹
نیروهای رزمندۀ شجاع ما در موج ۲۲ عملیات نصر۲  در پاسخ به تجاوزات مکرر آمریکایی‌ها به خاک ایران، طی حملۀ پهپادی، یک سامانۀ…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451406" target="_blank">📅 15:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451405">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رهبر انصارالله یمن: عربستان باید مجازات شود
🔹
نقش عربستان در همکاری با آمریکا، اسرائیل و بریتانیا برای ضربه زدن به هرگونه موضع واحد و یکپارچه امت، اکنون کاملاً آشکار و شناخته‌شده است.
🔹
تجاوز عربستان به یمن سال‌هاست که ادامه دارد، هیچ‌گونه توجیه قانونی ندارد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451405" target="_blank">📅 15:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451404">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47acd4d38.mp4?token=RsTpzgtNiOUVSf0GcrQeenRfhmaV76YgwsGonxCFBuIdddbiykNoN-fmiaBgw1-MnG7fecngoOxe1Hjt5x-oMGIlPIaXqJCvxlh0dBkIw6M_sOHoH7XEVEeBCv7rZ0KXrNAZ1_Bvkig1Bl9dht9nAsUmWkAyWoudFt0QO2un9GNFkBjnQ28nxIPlpM5JbSfoQR37GWkGVTBgkG-P5DGd_G9Y7a9Y-sif3lm_gBJOcwnchT0FtyZAl612wrIuF0P_HfnAQtNSRE5_I0H7ICBzoSXaWV68THdvhHpVq0VYaMRGWE_nQNmAjG4CbwWsYzUzaLY7sSzRGJF3_F4ymnxAKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47acd4d38.mp4?token=RsTpzgtNiOUVSf0GcrQeenRfhmaV76YgwsGonxCFBuIdddbiykNoN-fmiaBgw1-MnG7fecngoOxe1Hjt5x-oMGIlPIaXqJCvxlh0dBkIw6M_sOHoH7XEVEeBCv7rZ0KXrNAZ1_Bvkig1Bl9dht9nAsUmWkAyWoudFt0QO2un9GNFkBjnQ28nxIPlpM5JbSfoQR37GWkGVTBgkG-P5DGd_G9Y7a9Y-sif3lm_gBJOcwnchT0FtyZAl612wrIuF0P_HfnAQtNSRE5_I0H7ICBzoSXaWV68THdvhHpVq0VYaMRGWE_nQNmAjG4CbwWsYzUzaLY7sSzRGJF3_F4ymnxAKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از امشب دما در نیمۀ شمالی کشور کاهش می‌یابد و بارش‌ها‌ آغاز می‌شود
🔹
در تهران تا چند روز آینده دمای بالای ۴۰ درجه خبری نیست.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451404" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451403">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e596dbd9d.mp4?token=uXgxt6QhvQJ0OwCh2LG9OSDFKeP3GsspUr23I-rjir5CBvThOd2j9Cbu4u-RgCKM_m62nGAvnvG6j2r0iYofy3H7vh55FXhJ2iHnZEEiYXbcfmgNxzUsPDje70-UlU-4ptU1zruYzVo8JgX1ZSIryfjwwMKGatlkyIIEy3rUCkEg31z9oVVTOz4Tc1ffrJBR4PTdDMLvJznXT10p7yyGdo7Bugry8t7cOSq-RDajErvN9-EIZV2FQoP2D5B8kLNb1wr7qseTdf4mIlVFexLIAmZ1SQ26vwbcxCc-q2xWiR7AXq_HmVe6N7Vjko3a6T955fjYYEEWJw2cgXLq_thGbCtOn9JuJVaHLmzJuzOYTjYNrQZoQ-R0cTtQRtj-93Ji1RM1ssJCzoU2veuhIBFUu50OQ7-_cuuW659PIISrJd32dqMRCwuFCNsKarLqnvT2MDyHsWYumFlGHYIMDyWrEmn-Rn2q7HG44mjStlHbdMgw6KL72b2su3AAsY66kSR8QQgjb3i3sa1CA3GB-QJ7kTGHiw2bbViG4z8Dr3FAMcVs7kEryhOg7gKLyDQsXw-tEBUvYcKPVZv1TCZ6mtRq7d3HwB7dTPbXSpCBQxrs-fmBFKBH8OpPZCKg-FyjPCIVDamzaW2Vgl9_vmCcK5iljx4xhq2HePumi03ziMOpA_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e596dbd9d.mp4?token=uXgxt6QhvQJ0OwCh2LG9OSDFKeP3GsspUr23I-rjir5CBvThOd2j9Cbu4u-RgCKM_m62nGAvnvG6j2r0iYofy3H7vh55FXhJ2iHnZEEiYXbcfmgNxzUsPDje70-UlU-4ptU1zruYzVo8JgX1ZSIryfjwwMKGatlkyIIEy3rUCkEg31z9oVVTOz4Tc1ffrJBR4PTdDMLvJznXT10p7yyGdo7Bugry8t7cOSq-RDajErvN9-EIZV2FQoP2D5B8kLNb1wr7qseTdf4mIlVFexLIAmZ1SQ26vwbcxCc-q2xWiR7AXq_HmVe6N7Vjko3a6T955fjYYEEWJw2cgXLq_thGbCtOn9JuJVaHLmzJuzOYTjYNrQZoQ-R0cTtQRtj-93Ji1RM1ssJCzoU2veuhIBFUu50OQ7-_cuuW659PIISrJd32dqMRCwuFCNsKarLqnvT2MDyHsWYumFlGHYIMDyWrEmn-Rn2q7HG44mjStlHbdMgw6KL72b2su3AAsY66kSR8QQgjb3i3sa1CA3GB-QJ7kTGHiw2bbViG4z8Dr3FAMcVs7kEryhOg7gKLyDQsXw-tEBUvYcKPVZv1TCZ6mtRq7d3HwB7dTPbXSpCBQxrs-fmBFKBH8OpPZCKg-FyjPCIVDamzaW2Vgl9_vmCcK5iljx4xhq2HePumi03ziMOpA_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451403" target="_blank">📅 15:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451402">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc1570a063.mp4?token=hBeYbmkn_d4iGeDUa8Ak_9pLYKOOyig_wHRNtFcyGUy1Qvqu4k9uSNhC1d6L1SVO95sQC53gDCfvKDQA3hshScPIM4fiPewkVwyaX6n_WPZz8wy0dpnJ171LUP3X9iA3zqAC9ikNZMElldZCpGnNnVQ1yPYvKpzTpgx9WQ3VznFe4JXuFaFPfcV7pm26ASe6xAy5TRGktwztnt5FRJFoOpCaEO9CQ6QpJnat1LgUZsTb5Lfn4lRVHk9c9PnpIrljKrbzm6NihTgpnDMKtOYsDVTuXpUFAoyPuxsB4MWZijNK6mSivA6cmAK7tIHwlQ5OoB_V3bJbccLDR33D4J3CLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc1570a063.mp4?token=hBeYbmkn_d4iGeDUa8Ak_9pLYKOOyig_wHRNtFcyGUy1Qvqu4k9uSNhC1d6L1SVO95sQC53gDCfvKDQA3hshScPIM4fiPewkVwyaX6n_WPZz8wy0dpnJ171LUP3X9iA3zqAC9ikNZMElldZCpGnNnVQ1yPYvKpzTpgx9WQ3VznFe4JXuFaFPfcV7pm26ASe6xAy5TRGktwztnt5FRJFoOpCaEO9CQ6QpJnat1LgUZsTb5Lfn4lRVHk9c9PnpIrljKrbzm6NihTgpnDMKtOYsDVTuXpUFAoyPuxsB4MWZijNK6mSivA6cmAK7tIHwlQ5OoB_V3bJbccLDR33D4J3CLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زلزلهٔ ۵.۶ ریشتری در عمق ۱۰ کیلومتری در پرو دست‌کم جان ۶ نفر را گرفت و صدها نفر را آواره کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451402" target="_blank">📅 15:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451401">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuy8Evdy2QU6jJGs40lffL-hTZwvzv2fjsB-xhsWKk1nMPwHY79bEvloKQW3dUTDlQlD7HBG0sijLuAQN3fiLhkiCMX-Wxy5hfSUZUvD8w7GUfFRAk7EdbXaBTlzUcHCImiTdm4GceRDV0tJO57ei4ylGiMXu5sQeu8GO6tBihg50oMPi3EJkUqE3Xf2KgJuE9i0M7ft-WcWx1IPXrvoLUuXzhyOAGw5IrTAR_yw0B1mkD7dTsZD71CEqyqN9o3caIJht84PnP4UPVCJGWaxq_BG1dJtsd8D76QWT2mX4gBnDWzJ4jffDt_SwEPW1OWzAENJhdgqI6vseZ8q1ZNFRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام نخست وزیر جدید انگلیس می‌شود
🔹
اندی برنهام به‌عنوان رهبر جدید حزب کارگر بریتانیا انتخاب شده و قرار است روز دوشنبه رسماً سکان دولت را در دست بگیرد.
🔹
برنهام که پیش‌تر شهردار منچستر بزرگ بود، با حمایت نمایندگان پارلمان، اتحادیه‌های کارگری و شاخه‌های…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451401" target="_blank">📅 15:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451400">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/678a1a6d1b.mp4?token=vSTncFNjF387dtk8rR9qp_WxZMIQwNHH8884idqC73mi2LFuTG-WGHZvL0-zoIYbR7V1fPimr2PQMzcCZQrCDuS_0-zfLc2emgl7njX39nk8LPVeHl98nEzWezKUnjgarMFZDqs1x1g0laq6Xr9gpGU9lrKPhBfNmozUPMTeasJnKjQ12WogLPyhYllq-lnMWFxvaSHccNTNgFfF3GDMG9FiCRwEDCaut9dsKD80vSMdKuqkHd0zdM5QyiovOXHcgdGVw4KSfQw0c4BS-3L-veiZzv0gXK1-Dn43jLBUMHb9MKwXtwmz0BC-vXzRAEYTe3uWLjAkWzqVZ8CnRzMMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/678a1a6d1b.mp4?token=vSTncFNjF387dtk8rR9qp_WxZMIQwNHH8884idqC73mi2LFuTG-WGHZvL0-zoIYbR7V1fPimr2PQMzcCZQrCDuS_0-zfLc2emgl7njX39nk8LPVeHl98nEzWezKUnjgarMFZDqs1x1g0laq6Xr9gpGU9lrKPhBfNmozUPMTeasJnKjQ12WogLPyhYllq-lnMWFxvaSHccNTNgFfF3GDMG9FiCRwEDCaut9dsKD80vSMdKuqkHd0zdM5QyiovOXHcgdGVw4KSfQw0c4BS-3L-veiZzv0gXK1-Dn43jLBUMHb9MKwXtwmz0BC-vXzRAEYTe3uWLjAkWzqVZ8CnRzMMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هو شدن ترامپ در مراسم اعطای جام جهانی به اسپانیا
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451400" target="_blank">📅 15:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451399">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df42e9bf4.mp4?token=cYk2Tb9AQq5Cus5dUDn8jC6Sk5X3c-k9iuXkehMERB8i8fAkvME0GbSe5RykGel1rHKKOnbCFn-U3YJaqHm2t0mvHVEEwOy8w8Qy1vG2zcJyvCJBnTJdp9c2BTio3-j-GgJJ6CAyvre6LNOhe7ZtZ0qhymPWO-G9xonZprYn45oj1j9Jnc770PsG_FPk2e0KDJFb3ohr0Ri7alLiO1Ny1lX8w7T5LiMhU9NAYNQu_4johHqgPzNfExczVI5l06fdA_m5Fd-NGq2g5LZ7AG_iedvofq7fOLhNVaIxkDKWjQDK2HO_Y7nx1YQ-AddX4IdowjRFH72OQWPNfQMuRJMm8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df42e9bf4.mp4?token=cYk2Tb9AQq5Cus5dUDn8jC6Sk5X3c-k9iuXkehMERB8i8fAkvME0GbSe5RykGel1rHKKOnbCFn-U3YJaqHm2t0mvHVEEwOy8w8Qy1vG2zcJyvCJBnTJdp9c2BTio3-j-GgJJ6CAyvre6LNOhe7ZtZ0qhymPWO-G9xonZprYn45oj1j9Jnc770PsG_FPk2e0KDJFb3ohr0Ri7alLiO1Ny1lX8w7T5LiMhU9NAYNQu_4johHqgPzNfExczVI5l06fdA_m5Fd-NGq2g5LZ7AG_iedvofq7fOLhNVaIxkDKWjQDK2HO_Y7nx1YQ-AddX4IdowjRFH72OQWPNfQMuRJMm8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو: در هرمزگان خاموشی نداریم
🔹
در جریان حملات دشمن ۵ خط انتقال برق آسیب دید، اما این خطوط در کمتر از ۶ ساعت بازسازی و وارد مدار شدند؛ هم‌اکنون مطلقاً در منطقۀ هرمزگان خاموشی نداریم و همه مناطق درگیر کشور نیز در اولویت تأمین خدمات قرار دارند. @Farsna…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451399" target="_blank">📅 15:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451398">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
زندگی در چابهار، بندرعباس، اهواز و بوشهر مثل قبل در جریان است
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451398" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451397">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85dce6c68.mp4?token=JFk4sbmOpwV2-c4pHIr3jvDVl0ZAQxFPrbJAHVOvG8bdNXB25z1HbavKWKKFPcmkKjcHjHrw8ZGGmkiG08k0MPFY9emR9braR3ksQWrtJm6AEt7vHmujy6Rj4fMfuPaMxfOMjrNU4gdsfyRRMDgbM-usdqmVxW_vozcH3lIrDCe2C6o70SbQeAOdGg86aW3OlyroUVqOPzgDcUhwLxsBCW5qWm_HqgRwlTU3pjTfHbf-jqxFKqnyWG6XBZ_Tol7Ps9rCitKAIAWk7Py9_aHQCoQfNr0wx0GJ8ZSdmhj9Wmex-QPVerRirxDQcoRZ841OX8B0HnKlLF-2iFDfUsinmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85dce6c68.mp4?token=JFk4sbmOpwV2-c4pHIr3jvDVl0ZAQxFPrbJAHVOvG8bdNXB25z1HbavKWKKFPcmkKjcHjHrw8ZGGmkiG08k0MPFY9emR9braR3ksQWrtJm6AEt7vHmujy6Rj4fMfuPaMxfOMjrNU4gdsfyRRMDgbM-usdqmVxW_vozcH3lIrDCe2C6o70SbQeAOdGg86aW3OlyroUVqOPzgDcUhwLxsBCW5qWm_HqgRwlTU3pjTfHbf-jqxFKqnyWG6XBZ_Tol7Ps9rCitKAIAWk7Py9_aHQCoQfNr0wx0GJ8ZSdmhj9Wmex-QPVerRirxDQcoRZ841OX8B0HnKlLF-2iFDfUsinmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: به دستور آقای پزشکیان برای بررسی و ارزیابی آسیب‌های ناشی از جنگ به استان‌های جنوبی کشور آمده‌ایم.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451397" target="_blank">📅 14:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451396">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c184fefca.mp4?token=ihX_mBTIHSdBvo5u5XHbiM3WDHOoIBx9lyqf9lxOjseWjMLr550SkTxxyW7R-q3E_QRrftZCVIw9KAAhOwLBsCt8xq8gRMi6knmwADx414yzx1UORmL0M2is5Kd0VwdslwDLoFFiigMYKBu0fURY4tLuP1Ye8hevcvNGV-ywkMUMo7rhkiBqikpUbN83q4RZ2q2MWzcFjVtbkVqtridmlHMsXzulFm8fS4h0D6gboRIn0jLRgXQsloF8fVHe2AQtoIvDmAJZTQ9iutlA6oKED7epq3GNfgzcqtrnYFUH2nBE-5YUSUIuZTsl7QVc9iww6xx1rqessy7A51p4NcjukA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c184fefca.mp4?token=ihX_mBTIHSdBvo5u5XHbiM3WDHOoIBx9lyqf9lxOjseWjMLr550SkTxxyW7R-q3E_QRrftZCVIw9KAAhOwLBsCt8xq8gRMi6knmwADx414yzx1UORmL0M2is5Kd0VwdslwDLoFFiigMYKBu0fURY4tLuP1Ye8hevcvNGV-ywkMUMo7rhkiBqikpUbN83q4RZ2q2MWzcFjVtbkVqtridmlHMsXzulFm8fS4h0D6gboRIn0jLRgXQsloF8fVHe2AQtoIvDmAJZTQ9iutlA6oKED7epq3GNfgzcqtrnYFUH2nBE-5YUSUIuZTsl7QVc9iww6xx1rqessy7A51p4NcjukA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارگردان «قمارباز» جایزۀ فیلمش را به شهدای میناب تقدیم کرد
🔹
شبنم قربانی برای بازی در فیلم «قمارباز» موفق به دریافت جایزه بهترین بازیگر زن از جشنواره فیلم سازمان همکاری شانگهای شد.
🔹
محسن بهاری، کارگردان فیلم، این جایزه را به ۱۶۸ دانش‌آموز و معلم شهید میناب تقدیم کرد.
🔹
«قمارباز» تاکنون در جشنواره‌های بین‌المللی مقدونیه و قرقیزستان حضور داشته و دو جایزه بین‌المللی کسب کرده است.
@Farsnart</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451396" target="_blank">📅 14:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451395">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7b82dcd6.mp4?token=eS8qg9LHCkNQLS4BMoZ5fxuT_Sen1EJsK4AypTa093E4L95038bOe93UbVxmUmb4hQ9oBG2VxIKmf5D2EZsNhUtwY0dfuKXvDLI8WaGcOuK3alCu6bk8SA20PhL0UGTUf1jDbf78g76Hbj9NEAVHWcNtTEOAsoOgy3lznM1WxL197NEDRbW53J0K8IJ4Yna8QrTJg3SJX5FKt8v4W0CDl82F1OVG1pdodjUELJ6aLsbqHXmZF-vUtyLlciRoAJ9EygA0SbHy6otfTUhlBTk8ZjturIw1cdnTjVuYgFpORcOqrdXqi1fL-VvFqaPdctOREyM-J_oCLtMXrO0A16oZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7b82dcd6.mp4?token=eS8qg9LHCkNQLS4BMoZ5fxuT_Sen1EJsK4AypTa093E4L95038bOe93UbVxmUmb4hQ9oBG2VxIKmf5D2EZsNhUtwY0dfuKXvDLI8WaGcOuK3alCu6bk8SA20PhL0UGTUf1jDbf78g76Hbj9NEAVHWcNtTEOAsoOgy3lznM1WxL197NEDRbW53J0K8IJ4Yna8QrTJg3SJX5FKt8v4W0CDl82F1OVG1pdodjUELJ6aLsbqHXmZF-vUtyLlciRoAJ9EygA0SbHy6otfTUhlBTk8ZjturIw1cdnTjVuYgFpORcOqrdXqi1fL-VvFqaPdctOREyM-J_oCLtMXrO0A16oZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: هر کشوری که با آمریکایی‌ها همراهی کند، قطعاً کشتی‌هایش در عبور از تنگۀ هرمز با مشکل مواجه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451395" target="_blank">📅 14:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451394">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎥
سخنگوی سازمان مدیریت بحران: تاکنون خسارت قابل‌توجهی در زلزلهٔ کرمانشاه گزارش نشده
🔹
شبکه‌های آب، برق و گاز پایدار است و ۳ نفر بر اثر خروج از خانه هنگام وقوع زلزله دچار مصدومیت سطحی شده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/451394" target="_blank">📅 14:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451393">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a54248017.mp4?token=fu8Tob3Zhg47uPUIgOXohgaob0bQkZYS5yJyix8-j_GdYkHPg01jUdD9HEZSEmkdS2OP6QLzW8xJ5v8S2HCW0hHJdwJCLubvUPmOfqoqx8Rle9oOjt6OPG0nqnIoTOdgoi9KzHeTgm5gGs9_cJUQQM7bZsVS8g2RRCW3d6PlHSiLBQ913OfRriIFLGwcVXSg7m6Gz1_4msawVEPUe8I-GGzhRNDjEtIqDgDhPiRd_w8aiwvaVj5B-32vUQIljQuYpunD5G0rexgxx294anyLW04m36e6mv6Y200ZF_OzV6gtJGqQu2ALmpHhPeFPA3vtWpDZdSKXu70DLnX5s5QlTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a54248017.mp4?token=fu8Tob3Zhg47uPUIgOXohgaob0bQkZYS5yJyix8-j_GdYkHPg01jUdD9HEZSEmkdS2OP6QLzW8xJ5v8S2HCW0hHJdwJCLubvUPmOfqoqx8Rle9oOjt6OPG0nqnIoTOdgoi9KzHeTgm5gGs9_cJUQQM7bZsVS8g2RRCW3d6PlHSiLBQ913OfRriIFLGwcVXSg7m6Gz1_4msawVEPUe8I-GGzhRNDjEtIqDgDhPiRd_w8aiwvaVj5B-32vUQIljQuYpunD5G0rexgxx294anyLW04m36e6mv6Y200ZF_OzV6gtJGqQu2ALmpHhPeFPA3vtWpDZdSKXu70DLnX5s5QlTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربات کوبندۀ موشک‌های ایرانی به پایگاه‌ها و منافع آمریکا در منطقه
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451393" target="_blank">📅 14:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451392">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSS9Awd314S-fq8WQwW5JlIHQ9FLI9dbCqi5waPynDMRnhoagSxs6iVo9c6slfByp1lp50ZBIYnns1M4RXu70p1ubePbSH_c7JJShKFwI7XnrXzTCen1ZDJ7NAXcXtt2lQPfY7QXCw0q9mbIgM3jm9_XEQxEC3w1aIY7sXTbZJ5-zpEToJFNYXUrza-M0hUZtGlvr1LKCiZP5FmOAkb6D1qgGnn4FJZGf-r_g3_dsk4rnqG2M0MZtgrAf74oVW9b0i7gfqcONLQsioZR7Ul9iIU1VteXfHFlwFdsK4Sn-QTPzRo6tQ3DPqi8G6wio479OrnsvKzFnxxapOls2nI7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خليل الحيه رئیس‌دفتر سیاسی حماس شد
🔹
جنبش مقاومت اسلامی حماس از انتخاب خلیل الحیه به‌عنوان رئیس‌دفتر سیاسی این جنبش (عالی‌ترین مقام) و جانشین شهید یحیی السنوار خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451392" target="_blank">📅 14:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451391">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
قالیباف: آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگ‌اند
🔹
آمریکایی‌ها روی هوش ما اندازهٔ آی‌کیوی مختصر خودشان حساب کرده‌اند.
🔹
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451391" target="_blank">📅 14:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451384">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4imlSh_OKpuvOF2bMnCJGSKCLhSkwRzPaGuSaAIyywHyJgDUW0s1aOE3uZjpcBa3sR2ekyaAO-cyS8C31f6IoApnrVPzWnraH1NtLeJqS8OE_ZiG4OTAENlY_ZI2DeFisIq2HKpGXCAoWYFjjAteqgeYYddA7RlBeXAvrK79fgMm6Z5ySzXAgA4B3avmBZtZBB1K6WbPzjjt_ZZsO0AdhJBK66e6cMoFD0GpYU7aEcjIp4uTz7UmwhdkHwRnAXPfUxYZzTD2c_nbQnoaFcvDLGH-rYHE-Rsd7TOAtJpYUjI93m9Ho8Ws8U4GdSsNbKlieX9xec37G4yClbKRtADJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPgyeav9pyH_FnPf36zPUC7-GDOcK5SC6vOd35YDo-5TXLbloGyv6N_JFsibaAPaXPLg3nS6RHRaV9Ey5M9txT9TP52TJ-HfKIvuyukDKSN5wZ1znZEK9bNLou1JODwyFxFmaFXnazfGBaPEqlinGdyYDzJaS1IUbjVeAXZK4CaoQnahDhAO162ggMg_R4R4XHwodkmiz7uqon1IZFgsh5xIfIhSsa8xHr1A65M3LfcjbsjKXWkfnReOtKUOFGfev0XrhGpWy9P12h1Vb3R47R6zrk0sJKlPQAZKuI0yJ87RSzMjF5Utq9Kt7gUCq5QzBdb0TCF2sLiSQgoTu4sHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9AvmKaFRSKyiCIFLRLooYcjT0CmOzfPhb0jkWidjrwhWlbDLLUtrgZ9zWfFzCEkofEkn32i7cINFZdRh7SFRtSTfudNxQebhs6JukCEkLAHSIfSzAdptIWlODongaKve5BU63Oh75HaznaTYH4eKjtfAdNtoCYY3FSfJ-EaNdGY1ihpX7dHYblqBlywcxZbK8ll7S2PKe9W94zN1J3GtI3rNnOSq4EIWnGi1Cb9RbOWG6naYuxCiIO_-vBd2MBJUJWZMsoZIJhbrnHw8R-h5DvX3OW21yp-gG6tjQSh-uD4IB-CyaA6am13i1of9n7nvoZZ4E3kOL7FIzEd0rTmlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrzyybA3Xhh0ARbZmDKYIrEfy5JoqFZTIhRBXEY_cIuSp11kWJfhIpz6buts9x37kLz-U7sBLgLjihLNtoRNkm8HtNqPwz7WzhFAEspkPndQDofvbB4x8fmNO55M13pnZVBnElhlaPM57Tu4deIiItKG76sChW5H-ak-gQRwSyOnW2ZSM0_R60zoqdeu6SNjD_GJH7zWYSQaY9W68WlMSxsMk2L0cHPu5sJWDJXi8DZ6tPrpoUwEzE5NnDJxOfwKXgz4VjLAd8fVlNxJzKVf__iLcHm7-6XpN2GoJiR8hUrTejOJElle9vMWz6aH_bEg7GctpYqoK5fY8HyE3SRQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lR_4NHtYBSeKMnw3SJJ-8faQhftpcGTkifZLyARq15OkrDl72TJYMCgyNeSgPA5LpC6z_FIvK5FewWgOGzulJTowc0B_8BCqcJ4G6Cam5pC-4HRfDvRs2Cbx-vO5QQZXXOVW5ceFnI5OEjxhfPByi94KScQYc1Wcp7L5R_-z3k7LXoYS5X8HrndHjdVPnGiiTNNNsF1TYglV35EZw1BdZw_zJyz_jsMT7R0JvxKTl8tqwnRZH9pYrMKN0kZpFBTUL9cdHl-TUAyCkaZQsRnI7DBj-JPJDHTnRBe6me1VZOApxo4gxVB_cqPoiGTXk8XaFGHQb8w-IG1qLEFWOqhfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBxQe_aHkQDwBgikJSgv9tnUnRz2r5GrGblDm0ugI3_LI7vok0VpVZUK8R8gQlI302LNvetyEnjWRxoNEfwUvWLXhNeqOQWycurV402CtBUXkaLZTQMX58b4-1MEypIdIoUVYNlkiVffrLaak8gQ8Mwo3fpHT7e7y-CeC8PVWAu1pfzZaA3xM0VIRgUOZ_TBOhSqobsFL-sJ2JxQ4Ub9K8Y_ogB2wI06nERzZLyKfI0YT1lNvdEwWc90v0iW0NYOmDypwyt1eTC5cZUrkNscQrKyNPpewzqj5nl68DYm-VhWfyxjMrvQfM5XyGPNTP-X7FfkL97hqTsGwXr6IYSanQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qG9X48JdAWFU_bqwnATZcmVSkZBgD5c_AFHxp51gUwVMJmxDsZoj_SJAaDNsIJTPkhPO73LiiRfZMN8BfbY3pyfFIyjLZQmcH9KMiuGZozQ6XVN8uOAkZBtew67GI2K8HRTHu0nCWUr8xd4TgBXlHoF_EDX_UsTVc3eKxWW86zAazHFDSlnyijq-pVBLs8p8zILdoiIbHFuj-oW6r82EnVZAWiLsgjZojCxzIe3H-cnIDokzBeNCThULhdDR1FXZ1NHxe7Qt0UV0StSNDaurEUSlmg_gEWjYdDt2Pa3M0hEQM4KJJtE2CyW91ih7hH3Mg_QehnZh_7P-rD51_JkHIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
درمان موفق تومور مغزی بدخیم
عکس:
زینب حمزه‌لویی
@farsimages</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451384" target="_blank">📅 14:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451383">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tm4PWGNS5cWv_o5aQgskia0fBhiX06BEuZ-jy26isG527_e83UbkXaZuy65CcBaQPzKHNCNFQoomf3VFWNHgyM6Wtyxn6j-pr5zypSu5T57mgv0xiz4A4KJJD1oVp8gnXLzCf-xErOWV2IhMxMLRp2C7RUqgjewysQIvfWwtCCaQ6hAyB2zvMEw5cKWUy_VLFiTRh6AjMlu2GOf_y_Xt7MpPmb6Rbi7vr2ig1e0oAo51wD8dggQit1hFnxC-xKKj3vSDVbraggFDmBdkx_r4FU-KxQFsRurEAAMhliqhL93aSSoNtMYoK-h9maEXblu7WnqIryUUwIbeT3TPOFC0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پزشکیان: همۀ ارکان حاکمیت باید از سیاست‌های کلان کشور پشتیبانی کنند
🔹
تصمیمات و سیاست‌هایی که اتخاذ می‌شود باید به گونه‌ای باشد که حمایت و همراهی همه ارکان حاکمیت را به همراه داشته باشد، زیرا در صورت فقدان این هماهنگی، نه‌تنها دولت بلکه کل نظام با دشواری…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451383" target="_blank">📅 14:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451382">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پزشکیان: مهم‌ترین میدان نبرد امروز، عرصه اقتصاد و معیشت مردم است
🔹
واقعیت این است که امروز ایران درگیر یک جنگ تمام‌عیار است. جنگ امروز صرفاً جنگ موشک‌ها نیست؛ دشمن به این نتیجه رسیده که با حملات نظامی نمی‌تواند ملت ایران را به تسلیم وادارد.
🔹
در میدان نظامی،…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451382" target="_blank">📅 14:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451376">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNKB3vNEX26BNbPfOEDn1CW3M4LpqoubnLjX-q2OEf0qffCSh_nrdAKz1fq0Qkm5j1EPg1MAz74LtZHfneVgmS0SDrQgLIj3w0gELkekPJBP3Ke8Ry-ZynHcZlksg-RW91dPi1I_mlSSUnwkm1R1m_x2ohOKeA3dv4jG9n9ykTgE0qcImGbr5i5hFWynRwWjxZtc_0WCDopUfbXQuCWDSUApxTmFZtAPFllh-FX1sSENpg9IFGjcY6O94aDG2V1BBrnxtzExH4y3XNSR1pR2FC_O3i2bfBo8gHO5LQGvuKfzWq8UUbBizjA0gUYLYEyMq3uyPdQLSKbVzISgLGG7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGhE_BDFnlZYLqtEI_gfqG4X8wH5GU9RKfbQCE8lOXV451AlegJzzlpx7P_MkbSxHCm4Eq_RFhWDApD4XLFZOBo-92L1PzhxafEYFY4fTGJJJT_PIOmANaBcr6j2clxlorB1wp5gtb65IYr1yJjMNaP4Suf-WqtPsES7JTFUn643nismnG9SXf60Ra9UWRtgahuu884kg95k4C9_I_jS8szUpuE7pf5RyBHe_WOoi4vY0SlNCCEXpi7Rwl6iKGJpn5egk5RzKIPXvVp-Zhtw9rFoHuKsyq8TpfkRuJT79EDe4flyjPQGxln8pP_E-pqR4gmlch2QeDNu7JBHVDaayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJ3NDdk7mG9DJ5R-tgzZ8cb10oQX8-5o702F7prSfmmQSx3oV1-HPKY5dVB-bETpZsgA5bDcNUv9CFhjgS34SWTnGxtqTR9fPLiIyO7o_ltFgRNeX3lJ2GkGNGjEZLWctVLTOjyEZPR3Y5LPoWh1RBpJUWAEZ9mALRCVVT0dN52sy8N3q2di9bdt3802cMjkQ1EQhby892dx5idykQtUThikJCh54nvg1wayJDhRmqVrb9SvmV3pB-2lzoJM29xzrGkT0d-zoM3o2H0wion6NVAkbCF8v39Yu-9y-u8M0hapl76Is0xhIp-4-PjlDMIgx33N_ByMVeJGvD9BdMneuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuWMBecf_po9IVLbPZNHS6cx_1xvbpInWlWxYfCgPSiwf4bKrm3rh1J2aA5xafNUmXj0BYju0P4adRf6n_607L6Xv1GKFIV9wWoZXOeE5930HrcNeF6qckcIWQEfbCXqfl5vdpDSnA6aqzBpuZKVBANfA1jtiXbLQQz7s4nOL0A0-5D1CX4XaGxHXI9z6A53r2VVeN9rsSu9z0WkiXHe_0GcvXStWH443V7g7s1qbHTNMaH-zAcezamsSEUn81GIk0_Ul9GzxlJETm9Yrx7fzFKjopfeZEN_hyyWq_eN8zeFaqFuqu11SJhbm8k5AFX1Y-SMSi8g-O-DF_6HobqOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_gytnKD_yoGpoG4r6fCi-ZzHGfPMa81Lg03t79A6DCwJBvsKWJs56UvNT8gu6-c6g6m1q7aOBuvDwkRuMNdoqcgJOMm8yaxlQIoQWdF6wuiPjzJt_R8ZdcAvJTYUCZyLjpLOcke7f5QW7-rzI-bx669dfHQR5FfEX_bE2ta15JG2fKKZx1ydrTRpuvcsHpJEa8Cc2E_i1Dw1WxEqckzLgCHx_ntKgCRaMqtco6ZJS3pj-RJdyxH5XEeNS0knvPUT4q23bCbm8Y-NrcFfjB5-Y4-R39KNEtr3p6YP0RqulYiG-yaM-tIRwwzwJKxP6S9j7juKSav-MGdSEw-eV29eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTNu_gnNG4ED7PLhLGs1gEr8nDXDuMvzV3-ZqdVMXjhEjyeT1IqWQ1teUsIfXJ726zMWTnjKIWDSCACt50ZMq9iaSlmyZPAaDgEjXGaFP57vxmVVZbordIyhNFI90W-sYPKPpDCGYWpbyof5vmSL2EKb0uGx-we7CzYgr_voJRAcEvWNPBxeQ5j-Xpg-NI4dmaeYlqn-R6yTON__dhT0uGEgL832DamBekiTId_3-wUoNJdMXcu9SxK5KO19Kn8Aue6XRIdqfGjVCTBejpvdIL9HVvVlz1PpnGm-Z6C5BRgye0KQIH-plUY8e8wyMrQhEO2joSaJIYuH8aO5cSV3sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر جدید از خسارات ایران به دارایی‌های آمریکا در منطقه
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451376" target="_blank">📅 14:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451375">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پزشکیان: مهم‌ترین میدان نبرد امروز، عرصه اقتصاد و معیشت مردم است
🔹
واقعیت این است که امروز ایران درگیر یک جنگ تمام‌عیار است. جنگ امروز صرفاً جنگ موشک‌ها نیست؛ دشمن به این نتیجه رسیده که با حملات نظامی نمی‌تواند ملت ایران را به تسلیم وادارد.
🔹
در میدان نظامی، نیروهای مسلح با اقتدار از کشور دفاع می‌کنند، اما اگر فشارهای اقتصادی موجب شکل‌گیری نارضایتی‌های اجتماعی شود و این نارضایتی‌ها گسترش یابد، سرمایه عظیم اجتماعی که مردم در حمایت از نظام ایجاد کرده‌اند، ممکن است آسیب ببیند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/451375" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451374">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52f4bb1e8.mp4?token=XwK2domPm6xmqIk428pJcDPWxLjT3BLS_KEz10hsmYyvuXKDIMTkv2Oh5qBTCtSVREdcBt_IA3LSaETz-nj_0YrqM5pevKRHmU_hS3q1e6eYf1Jrdj2yb2sbnNP6Q68ueqg8aEQGmoZM2Nai9PJzWQZrEMZ2XdJURgsx3PGe1YeO4I4IqXmtRdK46nOHMPRETMiQFR_59Rv4DSx-II9bDzp_nBi-ZZUBL2VanKJQxYnAJnIrZN3ZTCcGLRmPJsKQLfwR1pV3gZF4o2pTPunZ8OMkOlGuqwsPAjlm8PNv515VMV2sO1vDVTF3NJlun40ebpbxHuRX8jlFJTkabhsbcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52f4bb1e8.mp4?token=XwK2domPm6xmqIk428pJcDPWxLjT3BLS_KEz10hsmYyvuXKDIMTkv2Oh5qBTCtSVREdcBt_IA3LSaETz-nj_0YrqM5pevKRHmU_hS3q1e6eYf1Jrdj2yb2sbnNP6Q68ueqg8aEQGmoZM2Nai9PJzWQZrEMZ2XdJURgsx3PGe1YeO4I4IqXmtRdK46nOHMPRETMiQFR_59Rv4DSx-II9bDzp_nBi-ZZUBL2VanKJQxYnAJnIrZN3ZTCcGLRmPJsKQLfwR1pV3gZF4o2pTPunZ8OMkOlGuqwsPAjlm8PNv515VMV2sO1vDVTF3NJlun40ebpbxHuRX8jlFJTkabhsbcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی: بخشی از افزایش نقدینگی در ماه‌های اخیر ناشی از افزایش ذخایر ارزی کشور است و این به معنای «نقدینگی باکیفیت» است
🔹
سیاست‌گذار برای افزایش تاب‌آوری اقتصادی کشور برنامه‌های متنوعی در دستورکار دارد و کالاهای اساسی و نیازهای مردم تأمین می‌شود.…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451374" target="_blank">📅 13:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451373">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70933c45cc.mp4?token=a5HNlSfigkxebeHQc2okBcuu5SYIvR6z2wafoyEPdWjcApQDjFnkBcy0_dD1KbBhIfcqBen14Bg48bwQC77Su2ToULOiSUEBK9mszA21kF15XCCj2l2cpViPT3K7bJ-LqkQ9-QS-0nLzNLmOGuiPN51_RNPA-w9LEKTEUACfbigmUBtfmxUxH7bMm-Hjb2PqgLbbxICOfZ97R2iOsdv4GD1FJW5_qcfrQ3cdka2bLGl3VD6AH48uf5vOgS76GfWUdKIdvxZF6KKnt2Ti06YiwmhHX2xIrukAgX934Zl3tBvE4BrSRcKCiu39nnV1UbKVunqKGfzLuwTjp1-HajJFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70933c45cc.mp4?token=a5HNlSfigkxebeHQc2okBcuu5SYIvR6z2wafoyEPdWjcApQDjFnkBcy0_dD1KbBhIfcqBen14Bg48bwQC77Su2ToULOiSUEBK9mszA21kF15XCCj2l2cpViPT3K7bJ-LqkQ9-QS-0nLzNLmOGuiPN51_RNPA-w9LEKTEUACfbigmUBtfmxUxH7bMm-Hjb2PqgLbbxICOfZ97R2iOsdv4GD1FJW5_qcfrQ3cdka2bLGl3VD6AH48uf5vOgS76GfWUdKIdvxZF6KKnt2Ti06YiwmhHX2xIrukAgX934Zl3tBvE4BrSRcKCiu39nnV1UbKVunqKGfzLuwTjp1-HajJFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی: ادامۀ فعالیت بانک‌های ناسالم و ناتراز را تحمل نمی‌کنیم
🔹
مهم‌ترین ماموریتی که برای همکارانم در بانک مرکزی تعریف کردم، کنترل ناترازی بانک‌هاست. @Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/451373" target="_blank">📅 13:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451372">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c95d9957.mp4?token=DqnVTzGzck8dJYoY9JrvSfPnOD93UTZAwFFtj891EWgimQvA0gU8cXqc71t9tlaOr_Ykrsqi14YYIMRqcJ8j3Vr9gQDwGOjz0zAkKjdzqfeqVOpdWjA_d_Skv9ZZpZjfj2Ic6qXRlQmx213mcWfTSuwktkyQ-Zgb0f50YfZDhQ4qyzA6ui7Um3L9A1516cNrup6wveQO_Szbah_DHmp3vUB4lh4pxjbo17wJy1iR7C2MnOCQlnVgxnCdz3VHMaCzQ2pLwL0_pi_nrebdMn8H7XLwiEdX9XAa_2Rv4NxXtisvN9AmCkKRJYVWpjnAK2d65tNw3gG0L7OqMrCo2w4Eag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c95d9957.mp4?token=DqnVTzGzck8dJYoY9JrvSfPnOD93UTZAwFFtj891EWgimQvA0gU8cXqc71t9tlaOr_Ykrsqi14YYIMRqcJ8j3Vr9gQDwGOjz0zAkKjdzqfeqVOpdWjA_d_Skv9ZZpZjfj2Ic6qXRlQmx213mcWfTSuwktkyQ-Zgb0f50YfZDhQ4qyzA6ui7Um3L9A1516cNrup6wveQO_Szbah_DHmp3vUB4lh4pxjbo17wJy1iR7C2MnOCQlnVgxnCdz3VHMaCzQ2pLwL0_pi_nrebdMn8H7XLwiEdX9XAa_2Rv4NxXtisvN9AmCkKRJYVWpjnAK2d65tNw3gG0L7OqMrCo2w4Eag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: بانک مرکزی منشأ تحریم، جنگ یا کاهش درآمدهای خارجی نیست اما این بانک مسئولیت دارد از تبدیل این شوک‌ها به بی‌ثباتی پایدار جلوگیری کند.  @Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/451372" target="_blank">📅 13:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451371">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c90d5c5af.mp4?token=oM6wNMAtu1ey2EVAnJsQ1IJSBYzbjm8mTPuSGp1AxAHuexcdZSfLNMCBlDQ6R2cgGm1BeUVkpZcHPgw-utswb_dZR8B9v3WB7GelaaWdKmR9hj3FwhfSmk73nxvLxClEvI7HFh9puHsBKTH-a707kUEiiUNabb-a_mRatz5V0Z-0XEhXSqBvIlLASRKKhoC0G57JRUrbhFCgeW24hJVzOC2LoNnMdmhwAEi8VcOjaX1gPnNAQz_dJh46jRQ6ah4ARCyeWW0CPkNxoU94KYnMnXFpBnDvJ2WLHLK-ZBtaLgERN7ziweY0v_zNfXELYeoWQYV8hj2b3Cmw885vP77TCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c90d5c5af.mp4?token=oM6wNMAtu1ey2EVAnJsQ1IJSBYzbjm8mTPuSGp1AxAHuexcdZSfLNMCBlDQ6R2cgGm1BeUVkpZcHPgw-utswb_dZR8B9v3WB7GelaaWdKmR9hj3FwhfSmk73nxvLxClEvI7HFh9puHsBKTH-a707kUEiiUNabb-a_mRatz5V0Z-0XEhXSqBvIlLASRKKhoC0G57JRUrbhFCgeW24hJVzOC2LoNnMdmhwAEi8VcOjaX1gPnNAQz_dJh46jRQ6ah4ARCyeWW0CPkNxoU94KYnMnXFpBnDvJ2WLHLK-ZBtaLgERN7ziweY0v_zNfXELYeoWQYV8hj2b3Cmw885vP77TCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: بانک مرکزی منشأ تحریم، جنگ یا کاهش درآمدهای خارجی نیست اما این بانک مسئولیت دارد از تبدیل این شوک‌ها به بی‌ثباتی پایدار جلوگیری کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/451371" target="_blank">📅 13:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451369">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjTLUH1_cGsdG1jz_SzzKI91pHAohS-f5fxjAstgIk_EI_TMfUfdldRpldWWQOReZhFyGDvjs8G7bXY09AP4IJsc3LEtbZwye7Q1faHv1ZyhqFBILhI7RKlZY8VEMRIXgGULNT0veU5R64wG0HFjFyyuOdODapdeV8RGk8bsuWAANIeBhvw9edAxb2bQReKa7NfiFaMgH_idEIBn0qB1_uHPC6sCi4lTph9ZKcb0Fc0ljweorwergSXE2fA74gGvbwEH5gZPeFi3icsWG86hDc7KZdnbGVy5SwxX6XkXlqGTaM6YtATq-xsIPtEmisgUG5wnzak8Hbbp82zJWOv1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LayDOjZ_irQCgMsbDsH-4_sT_wQhgFT0pCRTD0SlcRqLHkLUbMb5vi1HhYoE_vhV__lpcDW1KKFY0ThDZSsqUuqasFge8oHZXNyajB00kV5XvypetTbgNMbdJGEtwvI4gmkmn3i0VGTwVTm46LYLB4nlcStmEWc2mUh7f8Dcnnom8RXsEOM4_YzgpYwxfgX6PtpcwqREp-PPabWqEh-CUxJjjQfYC5Ya1MtShEMDPT2X2D_0VJu44dPakdxuxLgLujyYY68kS7OX3LHb3jCHydgZSu2wXxluQPFbNnbzQEPn7_aICNNf16diFulRGT-r4mkUI3lm1vqhyhEZ6h8m9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر فتوشاپی از عکس معروف مسی و یامال، پس از قهرمانی اسپانیا در جام جهانی ۲۰۲۶  @Sportfars</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451369" target="_blank">📅 13:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451368">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65616cf8d8.mp4?token=IGs09kotExFmKwUBFIo0fHLsBhzs0FkPwGNpDuFsMMvNVwwNiLOSnAy_ahHx5pPDHtbwWhaFyyCvao7DPqLHaqs38_CtgIEGazub6IOrHmh-fTgKWTIIpEOCdiYk4pya1iWTlGiCXYR32F6eHoFS7ibL-9yqkNKHkz_NlfM1Y13mfmHakSyzrcoYndanSx0YcMOFOch4A6CYbOPYbwVp0kk_FL2TGAmLGz7XuhC9qUtOhaZ43-PhIrergh13BcHPvaMeOCoL6Im9-MawKtjO-CaHKELHwCJhEtDRv-4q1BNEGnFJEQYWgT5c7G3ZSu8K3XliCV6XqDvDfKKBxZHiAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65616cf8d8.mp4?token=IGs09kotExFmKwUBFIo0fHLsBhzs0FkPwGNpDuFsMMvNVwwNiLOSnAy_ahHx5pPDHtbwWhaFyyCvao7DPqLHaqs38_CtgIEGazub6IOrHmh-fTgKWTIIpEOCdiYk4pya1iWTlGiCXYR32F6eHoFS7ibL-9yqkNKHkz_NlfM1Y13mfmHakSyzrcoYndanSx0YcMOFOch4A6CYbOPYbwVp0kk_FL2TGAmLGz7XuhC9qUtOhaZ43-PhIrergh13BcHPvaMeOCoL6Im9-MawKtjO-CaHKELHwCJhEtDRv-4q1BNEGnFJEQYWgT5c7G3ZSu8K3XliCV6XqDvDfKKBxZHiAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ اصابت موشک‌های ایرانی به اهداف آمریکایی در منطقۀ عقبۀ اردن  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/451368" target="_blank">📅 13:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451366">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt9L0yA_Yb-TdKxW38lsAGsZR5VUvaFSovwppRaER8XD89DNY9rja6KAKSv5wITEZ9qh5iXdX7f5UNiRcjn72mkCNrtozBGuK_FX3KhypAEsKtSEGJNv3ey1xt3ozmpdaMj0a2vzWlBDpHTt3CB4S6p8j2sLHOmO7qtWOkdbl1rMET1nArDymFNcWY-G0ERmpkkH6l6cTEVF6G940hOi5gCw15A57IciaKCGPU5RXKLvkXzzR2buW9P6-Kr1fmqTfNtOPSuJImXY8Ja2Sh_EO2wfgpBZ-d8-PFXqw-CMQUdEVCN_nDZk5ot7LAkRXaNuitSa0sw1HLms5ekyOOlTKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سابق دانشگاه شریف: ایجاد دوقطبی «جنگ و صلح» کمک به دشمن است
🔹
در شرایطی که ایران مورد تهاجم دشمن متجاوز قرار گرفته، انتشار بیانیه‌ای از سوی افراد و جریان‌هایی خاص که بدون هیچ اشاره‌ای به متجاوزین، جنایات بی‌پایان آمریکا و اسرائیل و محکومیت آن‌ها، صرفاً بر «صلح» تأکید کرده، واکنش‌های گسترده‌ای را برانگیخته است.
🔹
رسول جلیلی، رئیس سابق دانشگاه شریف در این مورد می‌گوید: در شرایط جنگی که ایران مورد تهاجم سوم قرار گرفته، انتشار چنین متن‌هایی نشان‌دهنده بلندکردن پرچم ذلت‌جویی است. کلماتی که در این بیانیه به‌کار رفته فقط کلمات ذلت‌بار است‌.
🔹
تعجب می‌کنم چرا این آقایان و خانم‌ها در این شرایط حساس که امروز شهرهای ما مورد هجوم قرار گرفته چنین متنی را منتشر کرده‌اند.
🔹
این متن به خواننده منتقل می‌کند که نکند ایران به آمریکا تهاجم کرده که توصیه می‌کنند دست از تهاجم بردارد؟
🔹
آیا انسان با شرافتی می‌پذیرد که وقتی مورد تهاجم قرار می‌گیرد، از خودش دفاع نکند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451366" target="_blank">📅 13:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451365">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">۲ مرز جدید به مسیر تردد زائران اربعین اضافه شد
🔹
رئیس ستاد مرکزی اربعین: امسال مرز سومار در کرمانشاه و چیلات در ایلام، در برخی ساعات و به‌صورت محدود برای تردد زائران استان‌های هم‌جوار فعال می‌شوند.
🔹
سال‌ها ۴ مرز مهران، شلمچه، چذابه و خسروی، مسیر اصلی بودند که در سال‌های گذشته تمرچین و باشماق نیز به این جمع اضافه شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451365" target="_blank">📅 13:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451364">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0D7uZCUFK8f28ojXiOykBmqGt3IDRDQ2H9G8957q0Y3idVsRQPsuSEpnUDg1A-JT3G5njj53-okdfHMb6Ff7Lnm3DwHUGMJH3Vp9I-z86dkHaOwkXnPu45iXJxRASFiXEPu5sImOTJXYZGHo1XSp95cPoPGcwlP8N9KKHGCfZFR-M2SeD2UgXBQwqG_jCjf5PtgX1MwAoMBzwchN7OEJEGGNI-51Wp7oxhs9TphfTl7IhevWSpjxU-Rd3UYJSJn_tZrHjPOM6xlIvQ0PwUBLZUJyz2KjctVN0SG69tWSp867epdR2LSFCbBlgPX_eXpQSq5AqS7SyjphTOcrT7FOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر الهامی: به‌روزرسانی توانمندی و آموزش پدافند هوایی ضروری است
🔹
فرمانده قرارگاه مشترک پدافند هوایی کشور: نیروی پدافند هوایی ارتش همگام با تحول مستمر تهدیدات هوایی و پیشرفت فناوری‌های نظامی، برنامه‌ریزی‌های لازم برای ارتقای توانمندی‌ها و تجهیزات و به‌روزرسانی آموزش‌ها را در دستور کار دارد تا افسران آینده بتوانند متناسب با شکل و شیوۀ تهدیدات آتی، از آسمان ایران حراست کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451364" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451363">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF1WCbFjsPEtZIRwYOXYkJJGlWXq7RS3GenbJ0JOVYGZS1xswbcafy-WDQyLwdNJMaYWjncwSoqyEk8wHITPDwk7aSYM4AeH8hWDLWZWpdBGtTNxsW20uJeSgCLWL5LlxkvaB3O6jniwS6Vn59N46IAqP6tOyygxlbHbvw8q1EdWjGHjJUofXlpK-Rules-s-WDhFS5Qr7rdLQ1YyxCVHEfg6TtjRqQLPvMdWU7hrNbspnrWnYuKQ0CkYWJSoge-0DLS3zuxuRRhKIMoLKq5zg4GcOk3SBJS-uxD5dIG6dO9_iMJC7LSW2Oe6mifoek-f4kmHz5is7SU-cqFQF4q2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به کانال ۴ میلیون و ۸۰۰ هزار برگشت
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۵۸ هزار واحدی به ۴ میلیون و ۸۱۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451363" target="_blank">📅 12:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451362">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7187234822.mp4?token=oiwVmhXrAI5Un41ZQcy0dva_qEZuRxejb8at_fZkwNpvFRaKsIsJoJIRkX1Mm4nbLQNvS6pikDTlgfAbZyH6yEDwqRQLlEMcnvI88yfrGCWI7UoknTEVjAFFXOgQfAhWJ5e1aM5z_L3P6GQXURxeBt_GmRGriWwJ_d9jFE8PJ8Kr40_oY6DtrltsXzS9p7EJhWR8wZeRQoJhSy_6cLI57A1aXTo5OMcAV4gQKBJ6O_6a804O8Zlg4e0R9iJyos1z_nBObFeBlYGMUCxCFLVpMhX5SxyegOGj_2n2aMF_TL5t5dbvu1mvyLKCHfy8MgcTHdhV-U9hTtLR0BvV4oFncA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7187234822.mp4?token=oiwVmhXrAI5Un41ZQcy0dva_qEZuRxejb8at_fZkwNpvFRaKsIsJoJIRkX1Mm4nbLQNvS6pikDTlgfAbZyH6yEDwqRQLlEMcnvI88yfrGCWI7UoknTEVjAFFXOgQfAhWJ5e1aM5z_L3P6GQXURxeBt_GmRGriWwJ_d9jFE8PJ8Kr40_oY6DtrltsXzS9p7EJhWR8wZeRQoJhSy_6cLI57A1aXTo5OMcAV4gQKBJ6O_6a804O8Zlg4e0R9iJyos1z_nBObFeBlYGMUCxCFLVpMhX5SxyegOGj_2n2aMF_TL5t5dbvu1mvyLKCHfy8MgcTHdhV-U9hTtLR0BvV4oFncA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: منافقان و نفوذی‌ها می‌خواهند مردم درگیر مسائل دست‌چندم بشوند
🔹
یک فرد نفوذی و منافق با تابلوی دشمن به‌میدان نمی‌آید؛ او با پوشش خودی در داخل صفوف ملت قرار می‌گیرد و تلاش می‌کند با نشر شایعات و طرح مسائل سست و بی‌پایه، مردم را به‌جان هم بیندازد و…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451362" target="_blank">📅 12:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451361">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4528a984.mp4?token=lpsiYXI-xxq3ivmDEBunerp10itt8qMf1xvOcpYI5r6GXueotdFNRHLk0zvOh1ln4vutGxY3KgNsKMp-FrAG1OITt8VKtRr0sdORhC54jx4eMBNvEYwFxZuUI6XEIgtj40vVBLlZjdNZ_mZWS0ShVQ4U-WgCPkUnDZ11EoJezL22E5HPXVnaLh4d80Bc-mPA3rAAQcIZir5bN4kSaSUV7HgohzgkjXfAM8xhiM7XBYy6WFJfe-MNdA6-5ugyQNQ9DqWd-hk_OX3hLbPyGmakdYlCjeWp7zuYk_gF3xDUONrjueCMYzi46gIix5LjZzYEIYlaQKMKYzXYbM-YfgKglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4528a984.mp4?token=lpsiYXI-xxq3ivmDEBunerp10itt8qMf1xvOcpYI5r6GXueotdFNRHLk0zvOh1ln4vutGxY3KgNsKMp-FrAG1OITt8VKtRr0sdORhC54jx4eMBNvEYwFxZuUI6XEIgtj40vVBLlZjdNZ_mZWS0ShVQ4U-WgCPkUnDZ11EoJezL22E5HPXVnaLh4d80Bc-mPA3rAAQcIZir5bN4kSaSUV7HgohzgkjXfAM8xhiM7XBYy6WFJfe-MNdA6-5ugyQNQ9DqWd-hk_OX3hLbPyGmakdYlCjeWp7zuYk_gF3xDUONrjueCMYzi46gIix5LjZzYEIYlaQKMKYzXYbM-YfgKglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: تصمیم‌گیری در زمان جنگ نباید با تأخیر انجام شود
🔹
بدیهی است که در زمان جنگ و شرایط اضطراری، تصمیم‌گیری در زمان مشخص مهم می‌شود و ممکن است اگر همان روز تصمیمی را نگیریم، دیگر فرصت نباشد.
🔹
باید همراه با نظارت، به مجریان قانون اختیاراتی داده شود تا…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451361" target="_blank">📅 12:30 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
