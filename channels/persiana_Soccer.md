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
<img src="https://cdn4.telesco.pe/file/iIZgDxNvE0QYsCsbx9tvvJPpU8TjLLmiPtTHZWVOwkTatOxDce8exvwbEUWYnDi-q-idtG-4i5sDIT2j-zg1zMqEYv0WTvUPD2s354qdK22Rl1whXjBpSkHHirSmOvEuCicjlFTMMYuMbR1ENXK9KlSxN45IApbJelZx18fCPE1zIiwOPnxDKoo5s7IndSVvRUh5kNNfVU46e74ustR9rqBDBGGEq7DrfU4VxyIWjSZH9DE5ukwW8j56zehYYsRMM1Yzr6Ml3sdfi5jK1rHOfw5YTv2X7tJzDCzPjLHqRsowcb8mDTs1kh-YsfeD0b2xZmlfw1HjyyaOheq_8jSd1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 634K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 19:03:51</div>
<hr>

<div class="tg-post" id="msg-27408">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ66F1HykJfbgV67AZkfZrNY5z5p_adUZRGNIJF9WyehRdme53gR01hq1FFwAheu8FzkPJxNUHJK2y7c5Z2aOGWiq95PyZexd1S8TKoVtg01pbPTb-ZH7nq_SG_Gk_gPOe0u5C2mga_EVduKDFCScaWqNCDKrb5jD06jEqkApnoNr3oAlxDBu7VwTTZnbyMCXm2MvZe4afSHGaBz7W0pRH-6bwM99kAK7nBwFrymwwuWFC20IRzfo1JRQFZK45RNjviyZcn5Cs-gE_4hUYWjzV-JN99cn1-MtClwfxYlaq7mbR-ZTfNEc084Q7cYHDpmvKkpKnZmM7eCC1yR0ztP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/persiana_Soccer/27408" target="_blank">📅 18:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27407">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faz1PoZ1hZsEBBIshlZbr6b2Mpthw7Wr0IRE8P5V0PeKuCkDPHpVMXAbiFD5-VNQCty34-_g9tPMljmBHfWB0_BA5CogjHWPi_YJDSSCw7Na4TflUJY3er9-Aegf8QBe95uB27m3946xUbWzpj6_X1p0YtjtScAx8xWOJ5Z7KAtTvZna3jJP1D0TfZECyvZT9i5OOI1SNhaJFREir59SZnHukSlhY7cyIFBVi18CA0-zEFunl0-T0PtEUtTZRL_YMigRtmowySxiJZuQn_i95C4QMySyQqz536ags00rwJ_eoXE435tmKQZRx4DhS6Y_MQO2gPAPxAASyXnTASFDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فصلی فاجعه در انتظار روسونری؛ آث میلان در اولین بازیش تحت‌نظر آقای روبن‌آموریم این فاجعه رو بار آورد. حدود یک ماه که با تیم تمرین میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/27407" target="_blank">📅 18:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27406">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9154dc0f9c.mp4?token=ARQUYkx6QmXv2l2GMWH6Uc3s4Vy6PPE2irhvRD92m3jMjVD2-Zf9kGv_QMkMqGwKtxKTEHeXCASvYQkyozdZPKIHxK6c2KTREhgy-qramdXyq5jkJDGiE0qAQrpu0F9g-SlxDz99omhKTJ_5Y5ypbJHDLC2g5tmdg3pt7jU347wQcJc-8IWyqxHN3dSL7MEl6CntslQtlBZwvu8FPj4RHR42oH4gla34gmyPFUGQrY2LG_AxRVQjAZ80ssAU_tfKU_KjbFDyNSjzRhO89xp-gsZR8RNB3-harOu1ItmhRgDe-RvKmuRtRA8lFtzrMMijOnY8B5fnJahAuDRJMnf4Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9154dc0f9c.mp4?token=ARQUYkx6QmXv2l2GMWH6Uc3s4Vy6PPE2irhvRD92m3jMjVD2-Zf9kGv_QMkMqGwKtxKTEHeXCASvYQkyozdZPKIHxK6c2KTREhgy-qramdXyq5jkJDGiE0qAQrpu0F9g-SlxDz99omhKTJ_5Y5ypbJHDLC2g5tmdg3pt7jU347wQcJc-8IWyqxHN3dSL7MEl6CntslQtlBZwvu8FPj4RHR42oH4gla34gmyPFUGQrY2LG_AxRVQjAZ80ssAU_tfKU_KjbFDyNSjzRhO89xp-gsZR8RNB3-harOu1ItmhRgDe-RvKmuRtRA8lFtzrMMijOnY8B5fnJahAuDRJMnf4Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت سوزی عجیب شهاب زاهدی در موقعیت تک‌به‌تک با گلر چلسی؛ تو یه لحظه هم رگ غیرتش باد کرد یهویی با پنج شش بازیکن چلسی درگیر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/27406" target="_blank">📅 18:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27405">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1-FxjVUdoB_PRT5GyejznBchl2qbiZNqyxHqgc6b3t17cBUYTR5B-rUAaWB0SSaRn3W-b9TY3oDtnmrkbrMrctiOZ88_0vx9hTSXUfD2c0AnnfKDlNGMlgVF_dUrrIrcYJzCw_h1BWG_D1HJUmwiOsEpikGShq9wKHQdgUsJJSX23m1Q9dIcOxzqEEe9Acjt3CeRIprQl8huc677CXQG92cx6SB9ohJ8U5laNAQzcgn_mv9jPHALOMtq37bLeTqwOeahe_6NrbgzKij-Uw7c62jCIUpcXVchvQfj46NKz67QCKpsQH4QmzCfm2nXlRf_nN08ti_P5RRIrpOF2VdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیرو خبرریپلای شده؛ ماخاچ‌قلعه‌روسیه‌امروز تو لیگشون‌بازی‌ داره و حسین نژاد طبق معمول بازی‌های قبل روی نیمکته چون کادر فنی جدید این تیم تمایلی بهش نداره و به باشگاه گفته این بازیکن رو بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/27405" target="_blank">📅 17:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27404">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKRqu1jL3C8H3hcaUKYBNVajR3imaKV6TzO0U5yHV20H7UVqT7QhsOQ2uJn4kGZkji_al9jk5vccG3oVjWYFYfXdXJXBgwQUgi_Qra-FpwZ9QA3hdEnAI2LwWFSieYB3IrRQ1Ab0OwEbV4IswIiv6r75aV5eRzRry3_Am5BVAMa1YDVkFrHIyGhwulZU1K7BsxBDAuSXSlxw8OI2Pk1FxFcIykzwfA0gf8yiRNMp9g8WLA9rRshwzwUJvNGaElzPB5Gre3i8dTe9Vw71axaCFyhziBZRIW27Oo2IeQO61FMFRryX6dsJu6dDjJZxa3-KadmI53G8HyFy0PzkeBFVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
ایرانی بس کن؛ یه بار دیگه ثابت شد که تو مسخره بازی رتبه ۱ دنیا هستیم بااختلاف کهکشانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/27404" target="_blank">📅 17:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27403">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8dde9dbf8.mp4?token=Z5YprtN463_J44F1frWt3ZOc99eTo6X2wED2UDhHw9njAre8lHCGul7u46KYBv_Ooj-kR3OL-PRDM25mGCzYTO8HrQ6XfqqJ_MFsXUbrnwMEN-2sTjjChcXac0qZsCNSE_uRhLMxfKqz1PHnjOL1V-l7P8XjrKfS-AyVY2-txD46R_X1lelSozEnmiMZBEh19HGMDeB9uKcahtkgBwbKAheOEG6cOd5GkcBnwg0OTvVB7s0qMyR6fveyAbZct69YDQ_AS2aHZt3Ktg_Yp79tniBHeF1sUSQUYo2B4_4jFt9q0Ih0q5oxs-3xi6qHCDj8cPO3XZ6EAC1ZBO-LEiLKXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8dde9dbf8.mp4?token=Z5YprtN463_J44F1frWt3ZOc99eTo6X2wED2UDhHw9njAre8lHCGul7u46KYBv_Ooj-kR3OL-PRDM25mGCzYTO8HrQ6XfqqJ_MFsXUbrnwMEN-2sTjjChcXac0qZsCNSE_uRhLMxfKqz1PHnjOL1V-l7P8XjrKfS-AyVY2-txD46R_X1lelSozEnmiMZBEh19HGMDeB9uKcahtkgBwbKAheOEG6cOd5GkcBnwg0OTvVB7s0qMyR6fveyAbZct69YDQ_AS2aHZt3Ktg_Yp79tniBHeF1sUSQUYo2B4_4jFt9q0Ih0q5oxs-3xi6qHCDj8cPO3XZ6EAC1ZBO-LEiLKXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیانا؛ درصورت موافقت مهدی هاشمی نسب، مربی سابق استقلال به کادر فنی جواد نکونام درتراکتور اضافه خواهد شد تا مثلث خطرناک‌ جواد نکونام، خداداد و هاشمی‌نسب تشکیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/27403" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27402">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atZHoxRxo-Jnhq7jocfh7Z3fGcsVc9p8IM_yK2zxHX0fbBC4rvU4tDPylv6uyCE1GXeYDmBHlCt2VKBBoyxEgys7VqgdLy-8U7UvmxQICsDBTis7eoowDVns1dPRJTjbEtI3OBQOt_tfRGS1zTBzDXmeYKHE3vIrkvTspP2aCURUb9FZ2hYBcKylqd1ox2KbiloNyjsEHvGfFC9fjo4dSR92MVMd8aH6h2rKOWu78vbGr0uPRffLhXWjYzl7LYZcKDVFMCUIZyqBKtCfr2vTKu4-ueEAGKefgfH3cH8IHyxVAn_MVMOvTaWEEP12QrOmh3DReLikdQvKNxSW61Y59A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/27402" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27401">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGkyjWSJrW1GMH9tDE5ex9wIaOPPOONMHXM-C0ZjuRJgN8NeN-6jsjvXnfzueD2CxgIpNhJf6esXsrrWming6SKfKj87xnaErR6IygaOOClgwM0nyBJALwBDRuJzxkld80Q_fQbIhkr6x1bn0Ea64QGOJ9UGNcZKK23U0TVHBI7uB6liuY07LAxaWMvYa9Kaso6qd7KIRjVCRYuWNkZObBhNcJ4GNEDydI-6LxG-gLVfbxco_VJPkfgqi77vULrv-siIbRsx6-EDDFYIG6wmwgfpOdfKcq4Ys9fkvnMTd8d0jsrSRbJBUlTZ1nRsaxSQ0D6mmoWN-i5ZgDsjK8wSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥃
خسرو خان هستم و با همکاری مافیای روس، از شرط‌بندی و پیش‌بینی درآمد دارم
⭕️
بامن‌همراه‌باش تابتونی روزانه بالای ۵۰ دلار درآمد ثابت داشته باشی
🔥
💵
با عمو خسرو، آروم آروم به آرزوهات برس
🔗
آدرس عضویت کانال vip:
https://t.me/+J_q7c-COftQzOGM0
https://t.me/+J_q7c-COftQzOGM0</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/27401" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27400">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b7307f5c.mp4?token=Il_sJb8U7uyVKbNm7n62GBg78ykvN_Imcr0n1Gy2ME5vqbwH6vdF8vrGZOW4leb-wNMyo84-i6PDg-euuGsIT785nhFFuk9jZjGLrQwP_r8uSyv2ht9eBlITVco6BgJtGQ7W_r-41jc-jtrExcHwpDqy-aH7PTcdQNvUCBWgMypoU0MtKJen5ZzyzlycLWXPOnRhEDSfBezBmTiWUf8JsXfDA0ekRBWFBDag0oN83flbB48-cadz0H8llDy64c1dAWdS4IC8DWcM3x43tfKWgJFZRR_Zex3qVTrF9RJnGccjPZ6-2Nyewdo7TwtoHrUjOAFwLGikTvojnxGcYgS0pk3D5xBC7-jrEyBNuQacUftE8bKQNcSl_CifzNC3hKIzs7vIEABrS89WXaxsyUgbag5CCatRgiu-_S7CPWGNRn4hJaXChVZ3riMQWhqI8BtJuMMKtjHtiMI5_4QZlep4xp7fa_b3iOrFTw4Deld37uzEuAbt0Okp1ZybfKtrCDk1-f7fnTQb2B5HHAhwNzaqli9ysRjSlxQhkYq52RTgmLV-5NEr2MHxJM4SjF3OufX6a61Nmv8tK74hCJ_uCaXld5itFw2pEAYxhMfRor5ao3mjj2axJS-lxXxqBoRxGjWYcUl4gbWgrwYSk6fTc9fir8eomr-7IbzkmqtRIrV7ENI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b7307f5c.mp4?token=Il_sJb8U7uyVKbNm7n62GBg78ykvN_Imcr0n1Gy2ME5vqbwH6vdF8vrGZOW4leb-wNMyo84-i6PDg-euuGsIT785nhFFuk9jZjGLrQwP_r8uSyv2ht9eBlITVco6BgJtGQ7W_r-41jc-jtrExcHwpDqy-aH7PTcdQNvUCBWgMypoU0MtKJen5ZzyzlycLWXPOnRhEDSfBezBmTiWUf8JsXfDA0ekRBWFBDag0oN83flbB48-cadz0H8llDy64c1dAWdS4IC8DWcM3x43tfKWgJFZRR_Zex3qVTrF9RJnGccjPZ6-2Nyewdo7TwtoHrUjOAFwLGikTvojnxGcYgS0pk3D5xBC7-jrEyBNuQacUftE8bKQNcSl_CifzNC3hKIzs7vIEABrS89WXaxsyUgbag5CCatRgiu-_S7CPWGNRn4hJaXChVZ3riMQWhqI8BtJuMMKtjHtiMI5_4QZlep4xp7fa_b3iOrFTw4Deld37uzEuAbt0Okp1ZybfKtrCDk1-f7fnTQb2B5HHAhwNzaqli9ysRjSlxQhkYq52RTgmLV-5NEr2MHxJM4SjF3OufX6a61Nmv8tK74hCJ_uCaXld5itFw2pEAYxhMfRor5ao3mjj2axJS-lxXxqBoRxGjWYcUl4gbWgrwYSk6fTc9fir8eomr-7IbzkmqtRIrV7ENI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی عارف آیمن ستاره 25 ساله مالزیایی جور دارالتعظیم در بازی دوستانه امروز مقابل چلسی بعد از دوری شش ماه او از میادین به دلیل پارگی رباط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/27400" target="_blank">📅 16:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27399">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsstT4zozxuCY6pjwFD5CPDqOSeucfFnTxevnlVSmx2fiMEEAaYT7Rhhg5ElgEUxpLImRH0-jPAf4XD95oq80mwBIjODAvAKt7LUSPjA0SqLQIvfHaU7OVeO1vpkwCxayUoexl6OqmAx2RMPXMjeAs2al2e7QnpmR0zyUtFYBOmTbVVS6OueQrSN9cbgeTREGRQlLkaOqbZTfodLgIdGBGW8YfUSi64rR6jM-0RqBbUsvFdG4kRF3ILdkBGguBI6xv4O56zugt6nAH56NfwpiJJjkjYdM8KhBgKmyDSFb5Kig-RV-czx_f6r5S1ucHrxRvW32_CvutmkL5v9LYIwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/27399" target="_blank">📅 16:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27398">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIIU15RMpbEWqUAs6wybwB1z__8wh_tgHVxf_M3KnHi5Ccvn4XKoOeXwGjGVawC--94yRGtRooOUPlvIPuQD8CAor4Imxlv-lO2-vfbjOxMmbj1MYRul8PZe_JDOmQ7vjGfJiQg6zLh4DRiy6I6rsYxN0bypwOm-t7Q33SNmYVCsTCLMicjghoEcd3FQ3LRYyOInIKUTbsjd9_K9WYJsM46aTuBOGN2lxxn5mHVe1FOS901Z8Aq1hUtkg83746oQbkkZ4tro4TMnje0uBp4ppkjp0MPAfOg_4Wf4Hhg-B93NDs36FEGVHSX_ZrE1ARKEFrSoHIE7chcy1zZ7VgKxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
جوادنکونام‌سرمربی‌جدیدتراکتور: تیم خیلی خوبی دادیم. چهار بازیکن تاپ فوتبال ایران مدنظرمه که نامشون‌رو به‌مدیریت محترم باشگاه تراکتور دادم تا اقدامات لازم رو برای جذبشون انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/27398" target="_blank">📅 16:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27397">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0eb7a5bc.mp4?token=qxCQV5W2DIIbBhUTPQbRVOvUiaUdPzYuaNmKfFaR8O2ej9R7SNF7kSka1OfVccWi1QoXTLOgwLBcAXKvu4m_mHio8xfgk7hxXgROeEPRUu3U2f9taCEgjV0A9jRDJzYfKovyjHF-N28s0vmpQg0133mqJA1vM6O95nU_kCUAzWaqHS9QhtY7uTaeoqfow_4arTu4fdQuaGG_KNUGLwhmRuR2ksBEMI9gfN0rAxW49OQ6M_o30GeOtF2M2vK7cPtcKM_4hf7TqntPTKfW7TvuvFrX1RMuLx2rTeyI0-vCuyTZlno1qa7UcKzagGc9adsWCb_fKfgJ_Qe7NOBC330QbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0eb7a5bc.mp4?token=qxCQV5W2DIIbBhUTPQbRVOvUiaUdPzYuaNmKfFaR8O2ej9R7SNF7kSka1OfVccWi1QoXTLOgwLBcAXKvu4m_mHio8xfgk7hxXgROeEPRUu3U2f9taCEgjV0A9jRDJzYfKovyjHF-N28s0vmpQg0133mqJA1vM6O95nU_kCUAzWaqHS9QhtY7uTaeoqfow_4arTu4fdQuaGG_KNUGLwhmRuR2ksBEMI9gfN0rAxW49OQ6M_o30GeOtF2M2vK7cPtcKM_4hf7TqntPTKfW7TvuvFrX1RMuLx2rTeyI0-vCuyTZlno1qa7UcKzagGc9adsWCb_fKfgJ_Qe7NOBC330QbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
ایرانی بس کن؛
یه بار دیگه ثابت شد که تو مسخره بازی رتبه ۱ دنیا هستیم بااختلاف کهکشانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/27397" target="_blank">📅 15:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27396">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ca826d21.mp4?token=Eal-RBuBmdAhGhO1xgfT08pLNWrpeTiXPeA3hHga2blSXjdb9Eua4qTSG-9OhNmH7v6rJmg9rXghNFSkGLxH6zo3F7na43I8x7HiTL5zzvDD1r0QuzjCvTVyqo1-ObRa3R7KBg5PHxC2hvkItJrSqFrhNJLBhKeyeY5xB76MDV25YYroOLqv58Ajkvmj3IB3ttiDw5s05RdcPBIazq4lcZPIDJIV7UcYYRAnC45r5NgUmNSWdi17dJqgDW1Ecrj3WZc5xYafdwZ4zarVll-mIlN_KbGtjssyzIVQD-v_JgPUGW2oGMmWqYgouHuPtlnXS6uEV-6KH4dSiU725fA51w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ca826d21.mp4?token=Eal-RBuBmdAhGhO1xgfT08pLNWrpeTiXPeA3hHga2blSXjdb9Eua4qTSG-9OhNmH7v6rJmg9rXghNFSkGLxH6zo3F7na43I8x7HiTL5zzvDD1r0QuzjCvTVyqo1-ObRa3R7KBg5PHxC2hvkItJrSqFrhNJLBhKeyeY5xB76MDV25YYroOLqv58Ajkvmj3IB3ttiDw5s05RdcPBIazq4lcZPIDJIV7UcYYRAnC45r5NgUmNSWdi17dJqgDW1Ecrj3WZc5xYafdwZ4zarVll-mIlN_KbGtjssyzIVQD-v_JgPUGW2oGMmWqYgouHuPtlnXS6uEV-6KH4dSiU725fA51w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/27396" target="_blank">📅 15:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27395">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0574804636.mp4?token=kLhlBe4qLhv6xNOL-NvtKEgY3zSonJmYK72iAKxfkqly_CLNbMaSsl2ZgU4IbsZgXCOZlYAxLHNCfiSWEpjqEwXlmZVvBRGvmRZ56GHiCY1ClPHC-kIVW8NG51H7giDKlXdXqvz1sTwiBIm2B_C2hqcm1v4vqhq8u_qOUWll2ncGPWwjlejQ0X19tw4iP5QMyIYonQXxdH7V5x8TrZ9lcKeSfhjMEFTaKVufwUDhnZaXRxg0od5pTr2vcAYB9KzklifBWcogiAifXXOl8t9tNjp7j6JEpf54fL7yYopUATOwX5Pcd9EjHA4AdMRFEaQL-290gO-nBULl25DJ_NdVyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0574804636.mp4?token=kLhlBe4qLhv6xNOL-NvtKEgY3zSonJmYK72iAKxfkqly_CLNbMaSsl2ZgU4IbsZgXCOZlYAxLHNCfiSWEpjqEwXlmZVvBRGvmRZ56GHiCY1ClPHC-kIVW8NG51H7giDKlXdXqvz1sTwiBIm2B_C2hqcm1v4vqhq8u_qOUWll2ncGPWwjlejQ0X19tw4iP5QMyIYonQXxdH7V5x8TrZ9lcKeSfhjMEFTaKVufwUDhnZaXRxg0od5pTr2vcAYB9KzklifBWcogiAifXXOl8t9tNjp7j6JEpf54fL7yYopUATOwX5Pcd9EjHA4AdMRFEaQL-290gO-nBULl25DJ_NdVyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دی‌جونای‌کارینگتون فوق‌‌ستاره سیاه پوست لیگ‌ زنان NAB پس‌از اخراج‌بدلیل خطای شدیدی که روی سوفی کانینگهام انجام داد، در توییتی این اخراج رو‌ «امتیاز ویژه برای سفیدپوستان» دانست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/27395" target="_blank">📅 15:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27394">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifiiJr6VZt1kMBR8ieUFJ6oQhurgKsMTJrw-I1KI_eCcRhMVmD7hyTvZpWHykAeJr7xKQTjSNVXVNbJQoGQ9fVsRCz5_Rwkl9GZjueVpjvPjYuj3GPcdsW_Iw2sgLcVEvW9OZztbqw0F6zyBRPi7R5PGmDiJ1UpsSMJGBetzQfooFODMxUkn64mngOeF_4hQu4P5ExJxT7d1lFrzPVGt-TUV58R6d7CPIGRlnCJR6ky9vOTAmjrujxVQwS_CdeveDjDYgGoDLmyq1eO3prJzIZZG7QAbBWHtFxJv3Dv7v0OUHnu41BphK1yuRTTNqX8s0D6svss_cPntPKW7XFqELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ حسین ابرقویی مدافع پرسپولیس: از باشگاه‌سپاهان‌پیشنهاد دارم و مذاکراتی‌هم بین دوتیم انجام شده. ظرف‌چند روزآینده‌تکلیفم مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/27394" target="_blank">📅 15:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27393">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnRTCtiPWfDkKgG8Kvxwag5IruUSRNIqSOkBSrGWcjiKxKO9PR6nUOp3_l4sUq5_OaE5k6GEk2NUlZXkenvkCUsBRrNNcxLj5tlsQ-R7GhixA_w_UULKIJK4Q-k_dQlcyfG0F8SzO0KbbM2OtG-v1czA3PEUrudTZ3nt0TUG3RNdECr1pN7AIr4AqVhqcZa87nPhW_4_iS8KS4r2WgfC2kBu386XIWIwm618bHeBORlTPZMhF0Ctoc8ZpZ8nmLui1lpp1OZHTrYBmyYG4bL8EAcVDGV1iilkSLHHDd7sIS26r_ibQLMhryn69JZl1ZazFiF2BvbSAoQF-4hUX22q1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/27393" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27392">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arIF4RXup1lIb-dSBkvPNm1UTuL_zXHCOWwhjYFDD9xO_khXfByOOoTPc9y4gkRiEWdpyyAZ2HeyuhN8gub9MGhnZbAvYy0okEorNFOxLJ99pMsF71bxju2O_GtJfaBEoxCeMbGgHps1N1hBBWQZl8y7pPQHXm0LxycgHvAYNPYYT38OHfPjD6uZLF3g9x5TaTQ-SHsAAFiwwW2UkgnR_VJ4mO5IKWyD0HMWWDznhBDBiL_b3V1DA_TSCYQtcQ-upKUv8pWfNxlTWQT7mz3RPdJMnncVeFxlUlHKh-UNsNtqqOwuqANrhk1NzWDJZ7PXun2wbRx3FRy7puepzPiJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
جوادنکونام‌سرمربی‌جدیدتراکتور: تیم خیلی خوبی دادیم. چهار بازیکن تاپ فوتبال ایران مدنظرمه که نامشون‌رو به‌مدیریت محترم باشگاه تراکتور دادم تا اقدامات لازم رو برای جذبشون انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/27392" target="_blank">📅 14:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27391">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4ZX825WWsT6oQkjn04eT7A2U0iwwWSPz708AUsaciKsIYe8TJ5qu98lgc-D8-BshNenG3-ueCafjahdXV3dn6JkYM5BbGNPy5rv_1rVsNVGpmifSAehPOitPJOpFe-TSpryL9qmFe-3JlOj-gMIRmAsN3K5BJ07LrbSwxQ2emeapf9wnCHeIVccvFnpsP-4xcf190o-6IUFu1kzziNCvVQV-Y1HUTtX6pjrjUUgw7gQoFjC9ci25TeW4bwPLiQB12WbtZqTxWmtT9KoQ5AQYpCKyM0ZabJ_H1aARSAUiigsZHMU7o3wiVYuoSFm2rWqhTRT4j55D5vLRTCgeGod3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ احتمال داره جواد نکونام از بین صادق محرمی و مهدی‌شیری‌یکی‌رو درلیست خروج تراکتور قرار بدهد و درخواست جذب رامین رضاییان بدهد. محرمی رو مهدی تارتار برای پرسپولیس میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/27391" target="_blank">📅 14:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27390">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3mC6JNE7nNbk8fUCYXUZdN-TcVCm1_rR6U9sSNBxDoIs7TvYLJ1SC7-UDvZbBo43jeDR2hZ2u_hPgWuNjDisJ-bSMAlKN1OaZ3lEzlAJKXqJiqZ7cdqNstJ0A0A7xXSK6ky-RHUOUD4nzz7EJ70kBZRo_prY6n8Ik1hkvVeXFNvuw-DTJwOpFeWQ3Stg21Da_JJfJYOvuQt81JbupiJ5w4WzHadxSHDWslOWLO7KgGALc9pkE_HOl48K51mlMVwnrrHTy89FbLfcRmydfRkjxOijpgr_0-vFl4zM0WGUmZ-xtebJV9TcPMj2IgTxdrG-eyoL_MgxtqWJjTo8rtXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/27390" target="_blank">📅 13:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27389">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpQdV3vvTm5h-fu987fA-5_kVOWo2rTLzeTkYXT9os8qGRcXvjcF9tz3ICcqz4GKsms8HP_UYnYb6fYaBO8URQxQUJQSIhM2mZKkvQiFS_ZUE986W4Na2BsfUz6bjrOEXgeaBkUPFCQQbSrWhunFmvKeBhTtmEAUX59fLHNw7TtfCVolXgwhY_iM-KF1aUDwnQ2a2wbqqI_W7L-zNjEGLMemqnXmlozmdBC8FdVc6PXyrtBpu2VKn0VY3Dxzo3jD79qQI8mNM3PXoT7vY91hksshgj4Ayz8qwfgeMjukjJDVVSWoawFhYuM9MkzhkeiOrmgVblkx_JA5sreKsLXFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/27389" target="_blank">📅 13:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27388">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0gKfpW59HnbdY3EKzBQZS102mfRJHX6QQLuJ17kjPOamGyp_EgPebRvy9XPUVF9wwD7Ve1Yb7GTY96o3reSSMcF68BmvErIADNtjDbHIwnYTrrzcEuRKjmKZY1B5zvOywJssLHHWAI9RGr2LiGsOd9sgipDWYQMkSEhDkE2tz7fL6ktKg2Od4JP3Sq8x3yV9jW8anIX7vVXkRkeJhyxu02CXqa8xlRfwjalHvRBkw648caUiuK6-lXFFPeVsVcaet43wVDSn4KcfAXX0EK5VEZayQWygTWtyYTQ45GC-XjdUwKjoRezuY-bNiGpYkYms1dLYVBmy8ttQ853DkcKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 28 روز پیش پرشیانا
🔴
شهریار مغانلو مهاجم سابق‌تیم اتحادکلبا با عقد قرار دادی به مدت 2+2 سال به تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27388" target="_blank">📅 12:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27387">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f7c35af.mp4?token=mAQ7DUWws6fLFJHKiPGj-SO5SWY9naiRCRRWzQkaWUzSCD6v-K0GKCW459umL6UC2P5IWMnR9g3-Cjr0y9b2VvH-B-KGhCNJq_zGRBNaRY6Xw0izovGjKoX9h15FJQon1ldN7QdMPXdBFAGhsbrR1slbZhUPU8uZGfl0vPtmINem2ERHWRvi1UC5uRLj4EX5I-CGUAJtKucSL5rFNdEMXv5wMEysYATRZU21acFoGC2HcT2Kw6MC1y5Q3AHVvK1SkdnJZ0It-KHyptP0Vg5igCQljmiZQbxzvc6A5DsYhvV3LECLddoFV-ECdRy2U9NTYyMqghnSPpWLuHhlM53O_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f7c35af.mp4?token=mAQ7DUWws6fLFJHKiPGj-SO5SWY9naiRCRRWzQkaWUzSCD6v-K0GKCW459umL6UC2P5IWMnR9g3-Cjr0y9b2VvH-B-KGhCNJq_zGRBNaRY6Xw0izovGjKoX9h15FJQon1ldN7QdMPXdBFAGhsbrR1slbZhUPU8uZGfl0vPtmINem2ERHWRvi1UC5uRLj4EX5I-CGUAJtKucSL5rFNdEMXv5wMEysYATRZU21acFoGC2HcT2Kw6MC1y5Q3AHVvK1SkdnJZ0It-KHyptP0Vg5igCQljmiZQbxzvc6A5DsYhvV3LECLddoFV-ECdRy2U9NTYyMqghnSPpWLuHhlM53O_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برگ‌های‌ریخته‌شده گزارشگر بازی امشب سپاهان و ذوب‌آهن‌ازپرتاب‌های‌بلند نادر محمدی؛ واقعا قابلیت خوبیه بشرطیکه‌درست ازش استفاده بشه نه اینکه از هرکجای‌زمین توپ رو بهش بدن بی هدف پرتاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27387" target="_blank">📅 12:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27386">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH9lJnnE546qOYtBupFPqz1-jgKLrjRYO5O6wz-wp5uwM1vnXpkbDJ6MOpLE51vE6vYxY2J7nAdp2HP7_y2keeEVyPb7ctryOC6q3n2l72zNHWXifZPollWtdxMytIdxn3ldc-IHNdNkzN0nZoduTEUIMWUfduHZfoZHXyfoP6QBbrqjzXY6CvmPhUl6o5So4ZuZlfFm1Gjl7C4W70YzHoLSZGrTaYQ71g79-n7_iIlJ5SRUmkxn5mXwHmkXfKh-AdKnLzNuxvVbWPDZDxQ5RHzp786ozrEEEMdteYz9YQda55hIUpZ3vbp_0hwmLkWFNnZCE9vi_dHYU2Eji7SN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛ مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27386" target="_blank">📅 12:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27385">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuIwxSD7EkRn8SBRG6vqu10OhGdCD1c86QiJbIIdtQKLOEqf9W8DVOIr5JSWqq2UMdEIh9GxWCrrrFPHi2YQcmhbb_QhFAKFuL2eMj6zeGsEP9Vc3uO471n9UQU34l8vqTNPRqlqKe8IdVFaAf0YRTKqRnSCDI6eGbOn7Ps2FhfDGBA6wrQ4gJv-rK20Y66h2Kq6qlnk_i_M_Y947OpJJ8XyjWLWP47VTXInTCiRCgnQ6J8elwRemJbBfTzQGZOzfgVPH6PiL_N87lh_6a3-aFxjZ1yb1dydUoIZo96AFl8lpDPK2xXYcvmGdLnTW-Kr3M9jNCTyfan_ten_BqfsuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/27385" target="_blank">📅 11:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27384">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSib_VRNfGGXXvefXrrNqCkPasMz8oGcxbGK3y3Y2pwdpyzRTof56N78P6oSZV2EH9uyUa1Cg9U1AQYdcPPV7X4FOTYDZfZX42zUkliThd3Z7oPhmLJ2pa_GEEHxp8vyvWmSxP-dYqJETY_FhlWZYFfmRtN2U547e33LJq_lrMkWZTyfEkwirsli82BKjZdNSnqmTJ_6M9_miXmnmW8EDpQIv0CqceVNpFJXochUv5pTRujjHkVVNpALIP_9kfyeCxek3TNgQCNt4Kj3yQj3YjN3BtvklIG71MYvHRLpJk-TzadH63BH48Go_7O1UXmrHrGz28IRZCdzoyx_f8B34A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عجیب‌اما واقعی؛ رامین رضاییان تنها باپرداخت 100 میلیون‌تومان قراردادش رو با باشگاه استقلال فسخ کرده است. در واقعا زمانیکه نیم فصل باشگاه استقلال قرارداد رضاییان رو تمدید میکنه بند فسخ 100 میلیون‌تومانی‌درقرارداد رضاییان میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27384" target="_blank">📅 11:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27383">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLQPcxRwTbL-NA2GJMdJRpMk-LIMw2GSDueaJe0pqpKqfKD5_QNjtnDBwW8mYboD5DAF1nWVWG8S9yZcBF1BGtfS16CGUif8kJeECQUUDQ_CrMOlLgrcWw9JoupB9mzAfeKdKOHQOEYsQ7qLxHDnRBrMLm03VUZEYqtnu97YYdyXDTLJl7hvilDaLCqzDb67ptaiOAHk4Tt2fTUrM8VebtWFlftn3RECxAeDB7bEJw4jbeh1JLx8XevsZBNlZCxaTNE8QOw8sTEGKiWBQFcAhc0w1vIdF_3dN3HrRsW9HEmsYc_OQfMRBiQl8pMQhmt3R8avf3JVyRhA1-AxLUZLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌رسمی‌باشگاه‌تراکتور؛ جواد نکونام با قراردادی سه ساله بعنوان سرمربی جدید این باشگاه انتخاب شد و جانشین محمد ربیعی شد. محمودرضا بابایی چندروزپیش گفته بود اگه بزارم جواد نکونام در لیگ برتر فعالیت کنه بی ناموس عالم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/27383" target="_blank">📅 11:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27382">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr8Bmt7Vn169m395jP-Ui4CsQ4GGSG3R5VLzN4obGEve8LQpHfI7OKzByu7-IEduflFHx8_PmoMTy_4RDJUUBrg0nAqOR_43Z3YSj5BpaCczBH7jNNfmFVj8G61ohdLjGYue9sjY4S4suR5JNAQnaJkpFSFAREAdNhKmlWB6lpZmONCGHB5R7IxA7_vu2s3Jb7am4vfRkfdeSNU_-1bjCBQZenFLGODj54nzgRzDPvULFuM_L_jGKNKO_Z_0KSgmikYn4E11NPtXUjjvAPzmTsed1VRiegMdquFJvmbCMrpCb8YPZ_XHs6H5drslj-pItIg2U15DExjsk3afrlhycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/27382" target="_blank">📅 11:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27381">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtPz8lTzq6Q2tFdJTqYdqbKKnIS38Wkoym-y8jBRX4jTVBUkGh6VnBivh3r5sQpX7YqPejN9loefFZY5ENnPUXjzke1tnuUxcHXUmfKsahDrRktvb0wOP323R3GUj7IMljC3rDLORmtRjhU3FawuOILUYOXsVX0d5vQsfempd2hGZP7XEsK9_CqjB-dfPoY1ch_NqHd_VtmGzK8egbGOs9G3_kbnb6X_IlioZz0mi_iNNqv8pYMpZ7WaGbfgkFY337hLCihAhdiKXOqTPEItdaVwygglUnK-FTlxjo9zcgN3bkcF-Ws081rPXCI5flbbJO0X_KQD4j6fQ8nUXzceXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌رسمی‌باشگاه‌تراکتور؛ جواد نکونام با قراردادی سه ساله بعنوان سرمربی جدید این باشگاه انتخاب شد و جانشین محمد ربیعی شد. محمودرضا بابایی چندروزپیش گفته بود اگه بزارم جواد نکونام در لیگ برتر فعالیت کنه بی ناموس عالم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27381" target="_blank">📅 11:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27380">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L40STQrru7Oe8WUnHo7NHTuDg1ifueeRTKlyZaye2a5P-7OkdkdRb-_019D5khUa4UtLDwFdoSEkWWEYVHZL2chM0f26M1GpEfJBIwy9RLxDtHbQs0T_sM21SagSwA1gQdbHv1pWGR7gPprEt5Y6v33XTealleAMwsitOtJxitOLwU6P991tSp-kBH7MTXPYIvWvDWadjkSVfuWujTx4g-i2U9krI-rJueVs3_9LtaRMVjjEJeKg6GNqlN47BICV9HTAUxXKelcAdO7NvbpWvq6OnwXkHzccTW7o3kLn65BLbFxdVO0dSArpQelHEpOhepjvI7kJCiILPaXM23KEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/27380" target="_blank">📅 11:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27379">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvWWUFD2JWPwOIJhVzP-3xyNRGzRLYQDjRUgUtskHQ2kV-Zhmia2zFZrj2_ySXE6rzbo1-Ooy-iX6OIHEFdz8MO_mpqlF1bNct_QoL5hzOolCx6RI8CrHiZ_jIlmY5ImDdoq3_ManlF6n1zbL4uivF3oDkmC3JXuOv1_1vRgRe8OfvwpQCPACN4knLli0kWWTncWoBenXF8U5x20gXE0Y_98g41IMkZ9ERQYVQ6yIQIwbF4FBZXqnSkK0Nks7tffyShs4gAOkxORj8DCJOx9Xgg77lF2K46XduZbVW5OlGCqyLhjIS55GWyez2BmpJ2g_W0ePagwk__OS7wqswyN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ امیرحسین‌طاهری‌مدافع 22 ساله نیرو زمینی باقراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/27379" target="_blank">📅 10:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27378">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkmgmYf1ry8DuDRMUCsBD7jgOAR-TTDynqSEyme9J1otYu1GlXDFS0rOctrcJbJaWMjOlvGyCLHkxluVQT3Dyq7Hb3C1bpcHz5vh0k43gZacMaC-qaCk9ImcJ_qHCi_J75_oj8MPlntbUMplYUj-39JFdS9C9EyaN_ENEt2UQ2oyKip3P658GVrHxAM22MrwD9x0Yo14pAEkUT6e5fgdqZPtUqG6zqXZVuAhX_KCVZh-VamHpkECNhkb_Oc1aJnsLxmh1XdsF0GId0OBmeFACETDBlSBS5ukisITGndbnedM5EIsraTX6Upr2lGLGFDgCoXerrYHUt-u6x6ahK9taQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق اطلاعات ما؛ علی کریمی از تراکتور نیز آفر بالایی دریافت‌کرده</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/27378" target="_blank">📅 10:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27377">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkN5FfQ2ZAn0kCo3xpkuFkqn3uGjp3CIRHAr0c10MuKZwq6BKBKKmPeVX13YDPoohaA_wN1D2ETRkPnY6JIJ_YQW1gwDowzOE1Bwvb0U8OhQe4Ew-xdsDdg4WN1MH4r_uijhlaHGOlYE21bNisRmtzJLCFrd1TphjLDJlDm01dEnmKZm2Sa1SeBS25uqbeaZCEtv8g2Mgkla2Kb7BymIA7ijTgb7_e-M_kO8xy2oAS8CDtEeujWev-ArAddSfjCbKRhmUfVQ-a0jN0YipjRSrLUtCIGasgt510AienvOBfRwH46o7BfgIX-1q619k6iQnR0h2i0zxHbph_SjFvp6jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/27377" target="_blank">📅 10:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27376">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vejud2YuWx2bk3QFHwO5GbgBUhi-MxwHyUmRMrWd8jR8Zpt9OcgXWkvgefsqB02-JNDA9RbnhPaM4zFoWavAEcyZn3STCEjvh1pBvdyyv0OooBS7dYLbUQBqhRI92K-nTeSlXF6cYsimJ3-ojfIVKydS45Ob9R_HKaLNCc9DHVH4DVIJcJEPRvNBk1aR1jMYtjlPt8MzicuE29xZrBv-QKQgGYoAjM9AmMjgBrNfM_VGh8I_m9qR3RmfbidHdPNFzWpmojXTNPNHAgBgtYuhziSSbVS6nD9zWxCNho8QROun1RLsw9pAnyLeGSTnKq7T6-jfj7ISZbGv2KWI9mFV3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27376" target="_blank">📅 09:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27375">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4RmvV4GRihLa_OKyn24zxZQ5Zb7eatQ1-D_ohwtu8lR5oCWuBULk5FxlO7P7WiNa5CNbza5joW8TJverIYmmCXTLQOiuQHs7NcLHRJJ92s8rwRF-sYNkDbKH9SOGlw6XRcbulN2rSRb8vIS38kwvs37_Z1IEGUG2IzsGiZ9AKT8Of6btFQNcKbouEj6N9QGscFeGIPqEMp9i8eIfFBGux5TILsb_yaujHYR05KlagnfbwnrRDNamuiHbv6Oj-nOVptDQMSw_VWz8sNzdwhscyzUdA13HdbHt3TawoA7iujtXZzHVyzbdTVUvUtI7k9_89SjYgDXfZ4h4P4D6yvVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری
؛ در آستانه شروع فصل جدید لیگ برتر؛
حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27375" target="_blank">📅 09:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27374">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rga2m_hiRxR6JjJPieiqymKSD-7f8pny8Ua8dbyx_Tohuo-6uOpa9woP-dNBIw1sZiV5K_aqWeiARS-xzQEGjhQJz-9z6BWsPEL2uDx1WsUuryUYsO3vCKbJYnQDrbSWoIQGSo8OfWjNCOvw10KvcrjKEpeCZk8LsKzSxFKnggvLWmPIMXxN-iiT8h6zOzIVHnWFoec-7ugdky1yYSS_pboR30Olf4dpXLMlLIEHzbHpTQd4TZ_SgsYe5xw1p-TU8Z5h-v_RnOlDcb6CAohtPWpU3YUWo0aK1HtyTR3RBpi28U7OljJlDhCpO5Vkb4sZhQw4PiV_PbOM64iQVJ65hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌شروع فصل جدید لیگ‌برتر؛ 10 رکورد تاریخی باشگاه‌ها در تاریخ لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27374" target="_blank">📅 09:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27373">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-Q1medUUtwYp_bGuAMTdoron1uVmx7kPVI4FdANjAkW2HS8i2R0lcFtgFy-CCl6981nc_JKw4wzVzSScEsG06qsdJJK7jy2JWVfufWEVdb7tde65nMK1kjEbEzlriO7V2hBVUMRQ_BwBwX8PE_yZ-0MgMpG4cD-GYvaIesKGtQwuFN9wwqrXKbEGYT5mPFMzn-05kL6Ms_09ih9N47OKnc3C0uqUrbVGJ_lhit0rG2bGdcFwYISEP5GE53-6OUfJNpO0o2-zUmNGuk8HbDgu88UyXyrRGdMCSTbsAZspRFqrlG8ayNUIpimg4io7IRctvPpHwTL0bks92yOJewdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه‌فقط پدرمسی‌نبود؛ ایجنت، مشاور، رهبر خانواده و... هم بود. موقعی‌که مسی تو رده‌های پایه "نیوولز اولد بویز" بازی می‌کرد، دکترها متوجه شدن این بچه مشکل هورمونی داره و باید درمان بشه. خورخه‌که‌از پس هزینه‌هاش برنمیومد، این هزینه رو از نیوولز و ریور پلاته…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27373" target="_blank">📅 01:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27371">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQfJMxwzxus9X0hnzgENBIy6nwF2t-HJL5GlYrziVj3WA90X0NaPRch53VqvGpUgHTy88ltiFWffzEYXmv-wrYZLLudemVv4DcVxIyQXr752_AIU9J8crMdIr-0rSBattpuejk0mebcvVpkm6ED3Za_5_h0dKMuW5eSx7YWgnSREc5pKrQbYXhu-HlDd9EauElAaLv4O5e17zBj2pGDpHMZoYez4ZEw5GLIJnr9aV8FHVxnEdlKucln-HJETFvFm445QsnNPoCUC7WQZ0MnHe675ZWIdxbdoDFlxs9e-u4_byNHyH25M9qUoTmDx8UNVexSMrVLloTyJB0F3e7QJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از دوئل شاگردان مارسکا و سیمئونه تاتقابل توپچی‌ها با دورتموند در امارات‌کاپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27371" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27370">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEjV4YOIOAZOhTgaSSe2GbvJlDAV54bueRp0s58qw1JwhYJJeMUWwlWuJIFf6UCqGyehKqba_bnb1pLSYHqPS37HHQXzZwtr2iWSiTSMRPqNBxlqMQGv16jNDACxXoZDTjWgH3CpiilmDlrHD9ymsjcp1XAsUOyv0fgoagakskEwffrWy_isvoPzATc0oVzTZFequBm0uuY76QtuSzaOJxecs3jHvtU2Qf3jebrudfqhZfqeYXPw_XLcpPVn0rlhRz-lriEHD4cs0ZSQscRrE4MIkkWXo5zA1QCsmPhz66JPnnbIzabxEbyuaOAskyyOV-4B7pE8u0olRuMk6p6L8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
شکست شاگردان آموریم مقابل چلسی و تساوی در دوئل پاریس و یونایتد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27370" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27368">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWZJ__ooERljQtUc0qjbiV6yGsDLGxl4IlPOfOo3amYGQR_7E0e0n8ZxVzB4jzUl-TDtNBej7xWMcm6ICslhqWymJ_goYGg4h_er5xCxuR47rrmrMiBfHTRypDrzFjtthHLgXa8NQmvFDf-lJmpvNjQqsyuCT6fpeGl7tYgdvn-NYsN7uAUS9iGDFqa-n8qhJoaYc8ZXzvM40J1Qkc_u4qhGj_S1KD05Lh2-Nh3TdSsAuJzGIuJQe0biXOMl60Op9AdAI9199BQsaxvOQ9lpTjYFyyfckcj_xBFBekqe3G4nISoz6z5WvgrZexc8HqI7jKdbDP7l_D4eK3sGhImIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری جدید خدابیامرز دیگو مارادونا افسانه‌ای برای درگذشت پدر لیونل مسی که آمادگی‌اش رو برای پذیرش مهمون جدید تو اون دنیا اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27368" target="_blank">📅 00:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27367">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCjNB_mJ-sYFAqt_ALeEmzVa4E7XqsF8nU2uZL8UI3MZsk42lFr1ZmV72CIPYmGMfRPIj5qkDYZmpmfBRvrIBe00BRM7EXU9pfws5oKHxxb4jzIB9JGmTsUR4O0-aHJAt69B6oh9OtjCwGNkcwNCTnYmOgziJr80RUppTdnM9REWvumoDIQzUNjFWWTApjttzGASSYVBvcgZN94EhqfWW2HiaB3MDOgxNe7S5dzzSKk-mLQETJFR_yPhENtJNWKiV0LL3b3RWQRMmMYd7PT0FlXTnKqYotto0NXv2Ctqxp5ecWxN2nunOFg2MYLmpFI63fd8eUdH_QW9HKT9_AZKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
از پنج قولی که پنج ستاره تیم ملی اسپانیا درجام‌جهانی 2026 دادند؛ دو تاش فعلا عملی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27367" target="_blank">📅 00:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27366">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV0uafUj4FmdgZzFJgvVOOAOZlEHKpq1IHv-_mwVJDM3AN62yr_ggsHg5VBirMqnyEIdiJ6h9URu5axKkkAHlMTfp0ckCuDC9TRRrvwP43cp0y24nYAZYqnpsd585ged8uB2tU9xr4OZUPe6iLHJilLK3_znn7RqBRBVJM6o5Cuti421A5qWS1LBaYaueqlh_iJ8OPnhVX7Khsw9CsH8pLNpalAxEEKFn65HZo99eB4DOYb-ktNB6CC3nuwAd2mSq4gFq5UKwLdyx-9SrqSTvZbIV8y4qOhJrfFS3grnelsOM4ietTmRNHwxbfqEh-zKGR_FnhqO9FevflVzw5UpFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛ درصورتی که محمدرضا آزادی مهاجم‌استقلال قراردادش رو با تیم استقلال فسخ کنه احتمال این که راهی سپاهان بشه وجود‌داره‌. ایجنتش با مدیریت‌سپاهان مذاکره کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27366" target="_blank">📅 00:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27365">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-cfVUAcfrdwzNDEKXodHcjCkpTLTZzyLq616rw_cwA3euM5zy0tsujsskurHLylFhSsSvLn0Tbm4ELtXXHxgbv7M46wKr5Es7cE6585NlIWVi5_UNHL-HNxp10WJ3A-Xs22kb_SdllurY1il4w4oN9v5DABVKGdt0pX-hOiRT6V3eA4ndDftFe09nfvO-Pmuwc85WTQ5B0v8NthoRyrv42QjNYJgH63IvwuY0sgTIWVPhg5UkMG-oga--yci6YFEhBZcFStURWxsCtwHpDM1ZolGgW86HKOOzXcdlH0ewEe-rt8V0hbtyYPNsh8QrQOYhxy8pQV36hocTcnszqy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27365" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27364">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhiIFW-scrXNUTZVpNYs3OU7vCdRX3k9TztDvFJDv6vdahmUF_dxx2tGiwnExBiNQA1Nk8SVzJa-uPgD5FhSZzMqNZR9wculDNTTXQec2CS1-htMfFRU4KOBHCtGqad4mp1HbZpMitjfe_aUXzb26Q5ar9Y_EaugQ2NDTC0pOkdt_ne6gS_SxJ7TM-Ge9jsnKS4lFRmCG8XoDdnN5CFGSmg09MOMBSpYeIPWLw6j9FFJPYOuCIFegxIDKjHFyZ8c6wrHKxKbqbiJL1jkeLG90apmbNw_UwVbAWz1Gd03ztXbIwha0mMmWzghgXbsO_5kOxsLsi980z1l4E-Uy8dZpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27364" target="_blank">📅 00:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27363">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap6rONI6qB2E1DorMampU_2EpJ0Lo6xNkmCBjJa-SRX9HagD_Iu50x8xUnNBIAn89JFuBfmJ1dk9sZF5ADAAUhS9Ue7-VPi2ujcWRsvrGEpwrrDuyMkoGg0s_aIBJ-3uIEAXZJLg2F1k8DT0QFXsBnwpTTS6_Jbi3RMPovjB2ncUUYK3FLTmqIre1r7KGjSt3SD8_G6mPmkhkOeWRus_PtA3bXJgHGmFxydg7zIk3S63W7khnMyXEpMKDC88i9CNqnIuzOLKELrwFansw6obnJhzZWPMaxuxn3JRkNkRbjP509XP8f2T5i_YM8RCb4koR0YNldk_qAcjYGBfyTVtPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه‌فقط پدرمسی‌نبود؛ ایجنت، مشاور، رهبر خانواده و... هم بود. موقعی‌که مسی تو رده‌های پایه "نیوولز اولد بویز" بازی می‌کرد، دکترها متوجه شدن این بچه مشکل هورمونی داره و باید درمان بشه. خورخه‌که‌از پس هزینه‌هاش برنمیومد، این هزینه رو از نیوولز و ریور پلاته…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27363" target="_blank">📅 23:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27362">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50f562360.mp4?token=EcD5FHmnB6uO9g7PEPP08DTRuGAOmnKeu3KhbeqWvZ4BIaeh2wb1T-ozp5WcjiYCll1MncTH-k-enpa4U_FeC5BbfnKnO8zKnLtEOqPWwmAZlR-MVdhhASdIgaOH_xZ9mdwrMzh5NDtbzbvQaBpOq_7ItHVvPQ_NdFsFmxcrCbL_2IpPLuihl25v2FI4wY2yhWTb1VBQ819XiU6zWU6aD9YlKGzSDySKcQyBXZVEx8MsHWCpeCYbMhCtKp3GVKPGIJ5kLtpAU8nYNGIq_r6RD9uCrRWG8EvcPl_0JU8aZB_Pa9HeegLvHuFmOYvRJTdBc3TsSWniX0XWZu49ARUiXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50f562360.mp4?token=EcD5FHmnB6uO9g7PEPP08DTRuGAOmnKeu3KhbeqWvZ4BIaeh2wb1T-ozp5WcjiYCll1MncTH-k-enpa4U_FeC5BbfnKnO8zKnLtEOqPWwmAZlR-MVdhhASdIgaOH_xZ9mdwrMzh5NDtbzbvQaBpOq_7ItHVvPQ_NdFsFmxcrCbL_2IpPLuihl25v2FI4wY2yhWTb1VBQ819XiU6zWU6aD9YlKGzSDySKcQyBXZVEx8MsHWCpeCYbMhCtKp3GVKPGIJ5kLtpAU8nYNGIq_r6RD9uCrRWG8EvcPl_0JU8aZB_Pa9HeegLvHuFmOYvRJTdBc3TsSWniX0XWZu49ARUiXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
هایلایتی کوتاه و خاطره انگیز از عملکرد خییره کننده الکسیس‌سانچزستاره‌شیلیایی در دوران حضور در آرسنال؛ یکی از بهترین وینگر های تاریخ و یکی از دست‌کم گرفته شده‌ترین بازیکن‌تاریخ فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27362" target="_blank">📅 23:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27361">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOgazvf0QhUJqsSTjtmQwr1PXogn-Vjpkc1sTb6oTCd7aQkbwxhBCkUHCHcPaqeV54Zjhm6ffuE_74GEOY30tOdA_fltv87lWw2h6fEfpiKSiuHvuAJGo-2xKvkVH7o8iY1YlX6wQmuQV9bK1csPrG43hlsJH7cF5k-AY8sbFnUsyXghQ7YHqtUU24Zb1p5ePXjWOSwLD4bq3FIho0m-4rJGtaqfhvEzYWdBZnBWJjKWEWkGcUcbjsEui6oOsLMyFkLEoBiRE2Zw7dwbvZFmjiQXOrUoiTTpMDKHDrEWoN6mQYdleoeHM_HceoFcBDbrve8peIJed8HlSf8ltDVGCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه «عراق اکسترا» مدعی شده انتقال مرتضی پورعلی‌ گنجی، مدافع‌ ایرانی‌به‌باشگاه الطلبه عراق در آستانه منتفی‌شدن‌قرارگرفته است. این رسانه نوشت: دلیل اصلی این اتفاق مخالفت شدید خانواده مرتضی پورعلی‌ گنجی با اقامت و زندگی در عراق است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27361" target="_blank">📅 23:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27359">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg-inFxZ_zcXO3KzaXDtTebP9s028tzfmPJi1MFmJJWCaWfAYr9YmIY4ffv8SthJx_ziY64F83Rv8dlMRNuoAMJ2kBP-4HWgHDoIyPf2eNHP8TUnhxSFXA6XfeI4ciP34_sptVm3jj-QTkAHVVtluSiLCzPrTO7WzlmZCdkSKyGV3WxRuSlT6K483oOkBxaZQ8MbivSqPWJtczS3mxeswsrDKYufTnfC9kuRkNjkrE1bCQo_dQkG2OZdftfL0u2FCLh2uKm45zCJO8qDG70tuQlzAWCb_y2ejWmeeM4qsBXiBXk_Wg5_U4YxINbi3ZwPAvakeAgmNtQR6WsiYOE0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار امشب‌باردیگر به پیمان حدادی اعلام کرده اولویت اصلی او برای پست دفاع میانی دانیال ایریه. باشگاه‌نساجی هم اعلام‌کردیم که منتظر است‌که‌باشگاه پرسپولیس 120 میلیارد تومان بابت رضایت‌نامه‌دانیال‌ایری پرداخت‌کند تا این انتقال نهایی شود. فردا…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27359" target="_blank">📅 23:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27358">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgRHoQFxQNqc8Pgzzwf0GjzkPuiLbC098yleLDUN07apMXAbLqOs4VfDINtUK7UJWJdY9A_4hN6rlkw09M6oRrJ6qvpxbJqgz2xvuaRzzSFJMVjV9Z7V1UFWlmfBxNo3CZ_sdF3X1dyr-fcZMkNAqPInUZT0DG7335i9KOLgAM0GDaByPhAcIDaVu0WB9ZV4O0PN3tIvVPxe1ZOaI3FK4gj7XXnt-HGoTS9X71sZYjhrnAm_4wJEfvokHbpFECRffV4Q7qKmMWtYTVDVA5RCuU_ZZwSM3lE2e1u8UInTNJdz4CUFDIu8eaJ-gA0xaYGsyE1whcxFfZZ9weCtIxAibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
🇪🇸
#تکمیلی؛ پیغام فران تورس به باشگاه بارسلونا: دنبال‌جانشین باشید. من با PSG به توافق رسیدم و فصل آینده در این باشگاه خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27358" target="_blank">📅 22:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27357">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN_C5D_-cB0dU_qpKYhwig5a8fVK-VaQQIazYxw7KUHZzrl7L2DPASB0seskHT7do-QDh1t42s2URTWtQtEh0vkVqRssySsCWBtttU6o8UrL-UuX-Atkzhu_b9Ny_C7Vx-QW4tupQrI7TEW9nSoaBIvyyTgyxOVrakFdNBMk0Sam5coMoGM-S67rfIOd6goX6vh48srxr_DhkYz3HIpriZLjssxYf7aZiD3uPO2_WRva9c4dvys4PZlVDWGPQQ6tWsinin-mA-1wwkG3JKgn0BWiVHIsogvdsNKznMn5o7rJBX5lPhP5fTypKCximPPHSoLGPrR8HYaa9jrYKhQnQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار دوستانه امشب؛
توفف شیاطین سرخ مقابل شاگردان‌لوئیزانریکه و برتری رئال مادرید در شب گلزنی ستاره جوان و تازه وارد کهکشانی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27357" target="_blank">📅 22:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27355">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDs3KWFFNg8sbDXX1YUqg7cdlG8drVhort7bqdJYZrLlfwwUcXji2h8oPeyP76rkV45mpRwBmK-_zJNnF3k7mxqvtoPYOY_xkNTXoFbMY1Q-IC0bHNYoAEaSImc57j8vdWnus-sv1XAmI5SWSqaIe288lPwW8J0z9vRHzRstyyKGGRWA1d0OYQP8y-5AJp_qKffVOuemJW_ObkJu-r5NyM32TF8LIHHur5wiMjtyYOaiULu-HxEgUKBCQBiW72dEFnZM3956SewXKg_os9riEL_SMvOKW6UStpQ68zuWa1-_rX26monn7U3NXrA2-1vcpelisUCbkNQoEDCIxgX9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgO8gM236y7hKXU7g-d_VZQY3kYFFuTyhuxa3udaK9K68_cF8jdzgBkjesZn-zW3SaFc3ryV5eMNacN_7Em3lJfdxZpN3gbM3ka_zfS7lvIXiphabDxk2NgA1a9qwZRBRGr63afmHOc69wm70_dqH4A8NT-359e0w9phZpkyNixXUkj7m46YsmAcSkxb3NWs241dG4YCRXCNEeSO04Y2MHw_OykBr9BwsgzC74-VCjGYzDLfKLmAX3zKwAvVh7trlHVAOUW9K_bqVC-H703RKcX9mtcyx26OGAneDF3uSqPK8jCewN1yyJEZc08Chne5jhP2x3RGzz5Ykh0ed7KrMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
دو ویدیو زیبا از فوق ستاره‌های تیم ملی والیبال بانوان ترکیه با کاپیتانی و رهبری زهرا گونش که اخیر قهرمان لیگ ملت‌ها هم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27355" target="_blank">📅 22:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27354">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYU_RovxaqKiBzZAf3rXqviNI_2Rok_o_I-ySPmWc3VHYpxlyaPMIeY3rtdrJRpruJnKom0HZL-IqvlUPAaHz8JXUqow0gHyaytyFvw1l8f3gSlRZkhTqSEketvWA0177Qs2RZPxJc4fgU4-cWruaQ8SQOYnySVVYsqh8mAjS34prejFB-OXJ9XDqI1qpwfphCagVWK37zkodco-yjMQ-T4QRdEUtmNSDcdJrv8wwULVsxAOIchx50mKvjAwjSVCIgJmtmKeT1D0SmUgBLPUWuA1MfH00FXGT9Ja8fSPRzTIOwb5fRJ-2wC1ypDIAoIMc7jxZiuffZAEZnRoeKYk4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
بعدِ توافق با مدیریت برای تمدید قراردادش؛ جلال‌ الدین‌ ماشاریپوف‌ از امروز به تمرینات‌ آبی‌‌ها اضافه شد. ماشاریپوف به باشگاه گفته تا تکلیف رضاییان مشخص نشود شماره 10 نمیپوشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27354" target="_blank">📅 21:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27353">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f51b1028.mp4?token=V3SqbWeOJJuOilzjHQ8NAyQOLMVAtpfZDzRCOBTyRLmGrW4hU0tP9a1HoJ1rylBx5920-anY3KOTuELrPxYQfywLv6d6sDaplZ5ZRNyshksNq5UnkfWrDBjOa-D7TM4JVsfnBnkM3f4Vwl__P8p03mcEYqhMQaToGges1kQvn-bFccHCf5zJI3PZ-GUCmUIsNRzcT6-wXRfXuuCDagLYPj60qIUfeWuNlMv7N2I1FGlff1dhqbrbMpTlnWBD09NSeKajTbC-W0ybVSqoJi_ZQl-E1AkaAvvJQaB2Zp9cMRgqJj4TS7u1Gvi917ZbA_ouVWi6gfwCp4mA3mGVx31YkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f51b1028.mp4?token=V3SqbWeOJJuOilzjHQ8NAyQOLMVAtpfZDzRCOBTyRLmGrW4hU0tP9a1HoJ1rylBx5920-anY3KOTuELrPxYQfywLv6d6sDaplZ5ZRNyshksNq5UnkfWrDBjOa-D7TM4JVsfnBnkM3f4Vwl__P8p03mcEYqhMQaToGges1kQvn-bFccHCf5zJI3PZ-GUCmUIsNRzcT6-wXRfXuuCDagLYPj60qIUfeWuNlMv7N2I1FGlff1dhqbrbMpTlnWBD09NSeKajTbC-W0ybVSqoJi_ZQl-E1AkaAvvJQaB2Zp9cMRgqJj4TS7u1Gvi917ZbA_ouVWi6gfwCp4mA3mGVx31YkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گلزنی دنیس درگاهی دربازی‌امشب استاندارد لیژ مقابل  سرکل‌بروخه درسوپرلیگ بلژیک؛ قلعه نویی تو جام جهانی 2026 میخ کوبش کرده بود رو نیمکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27353" target="_blank">📅 21:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27352">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ4MTxxR5OAAG-bniiuRcWKVoV9ZRIejvmoFGuJAfDh9i0FAFCatwrbIYMiic6GvB-w_ox9vIb-SGmFkjzO3QJvBb66psKEGBmE_ta4NpjJxRIO8uESo3G64RYZ1_han9WAVxxpCIm1-rDdJCrk8dowv8K2QY8C6AOniew5jfRRHxRVtyi1HQC-VI3XN9wljCZdOpXdsTSA-HNM0j-LyblTUjfK4OO2AUuEA2v2nsR_rm8uApv5VZ4ByRMPgOqwb_6eKoRPhXY0WbXGOwxXtAcQFJprn54NjO1CwFVWG-aG5ueo6svGU7nmpK4Gssrv_KBSk8F7AMo1hXHe6KTb9Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تراکتوری‌ها با پیروزی 2 بر 1 مقابل شمس آذر در دیداری دوستانه به استقبال لیگ برتر رفتند. شاگردان ربیعی در هفته اول به مصاف پیکان خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27352" target="_blank">📅 21:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27351">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyVSLbt8xy6rzaZAYhvB3N6qjru6rvyycQ74wlNTvG-irw795snrcUSpIvgx3EBhBMdg1foB2pgZLACTKngPBJvjPANU2_zfND_m1JQseV2QdUOMpJiBDfL-Vg6GG38lMhH1btNnKRr8d6o4gaGioMoP4w8BjGH83uGKQtYw5EKcjexGrGacPdLVMxgydjNd4OFJVSh3BKSvlAZn4uNPZzg9rR-VFcnqopjMyAVueDPkPxdhVuYyYYp8Cv8sxWkkRDJyth8zojTxhK6Zj_Xue_7mA1vqxN1c29S6RKUaNR0cWnjme3wpBbhxoJaxeBBe4d-_ro5hRYOEtOkDD38tkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بعد از جذب کوروش اژدهاکش؛ امیرحسین طاهری مدافع‌ میانی22ساله فصل قبل نیرو زمینی که عملکرد درخشانی داشت در لیگ یک برای قراردادی 4 ساله بامدیریت تیم پرسپولیس به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27351" target="_blank">📅 21:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27350">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24945e30c7.mp4?token=DHaqdJIHpfBJFWUjV4zAajiDcNhJqLjIkjY3JhY3b1JZqbfTwQ3HArMsQJ1h96J4j3FNvqgWIIMQn8Pq69i2-d-r-w93YPyaWoVyC8Ad686DWcR4-Qc9yFQ27hwxy6wc5JvAnT-bNXQyUHdYotCLEcU53Ju1DNoLGtj3TLQzLcohxOq-Pzc3d8wcsdMQJKArwtBjtiprl3FM5qNBhWweyl6CeBprYaTP-a_peq-JNSmuQOp8D0-xzXD07XqqKEElm7MIXbAtiOinGxHSqqootu7tq5Qk6_8Ao2RNoV9jK8srga9IhUfmtlRpxXMz5hYpACiaqDkbytf7XSqv3Vp13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24945e30c7.mp4?token=DHaqdJIHpfBJFWUjV4zAajiDcNhJqLjIkjY3JhY3b1JZqbfTwQ3HArMsQJ1h96J4j3FNvqgWIIMQn8Pq69i2-d-r-w93YPyaWoVyC8Ad686DWcR4-Qc9yFQ27hwxy6wc5JvAnT-bNXQyUHdYotCLEcU53Ju1DNoLGtj3TLQzLcohxOq-Pzc3d8wcsdMQJKArwtBjtiprl3FM5qNBhWweyl6CeBprYaTP-a_peq-JNSmuQOp8D0-xzXD07XqqKEElm7MIXbAtiOinGxHSqqootu7tq5Qk6_8Ao2RNoV9jK8srga9IhUfmtlRpxXMz5hYpACiaqDkbytf7XSqv3Vp13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇪🇸
🇦🇷
ویدیویی‌زیبا که فن پیج‌های باشگاه رئال مادرید به مناسبت فوت پدر لیونل مسی ساخته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27350" target="_blank">📅 21:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27349">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe423c6dd.mp4?token=pPlNQX-h71p2oZoIuELX1XQnRKT67H-o-wohF0Y5jNVGBLGvtDD96fejQ2oZ2AFbmvgBQ8ubVEcLoSev6i61NRT7UzLhGUAFR7Ni7sfzTkhGaYRhYV6RjaipvVzrzKeAlx1-6a6A3b9HzVooxfMk2qdaUOOjbEwqz3JS7NY6_LCbyk2ytGdFQCTtye_x-bmRw2f6CId7b6XfgYjIG250Edq_whIT19UxEZ187zS7mbt8Rw9-L3UcEwDjaVRXSHiWHXWSE7pRyByjrjRomdapRE89vkniviQelVu7O22x_zwz_cz-IXCyKKvnm0Bp0CADzpT9UEf3SVCvGwloXi2aFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe423c6dd.mp4?token=pPlNQX-h71p2oZoIuELX1XQnRKT67H-o-wohF0Y5jNVGBLGvtDD96fejQ2oZ2AFbmvgBQ8ubVEcLoSev6i61NRT7UzLhGUAFR7Ni7sfzTkhGaYRhYV6RjaipvVzrzKeAlx1-6a6A3b9HzVooxfMk2qdaUOOjbEwqz3JS7NY6_LCbyk2ytGdFQCTtye_x-bmRw2f6CId7b6XfgYjIG250Edq_whIT19UxEZ187zS7mbt8Rw9-L3UcEwDjaVRXSHiWHXWSE7pRyByjrjRomdapRE89vkniviQelVu7O22x_zwz_cz-IXCyKKvnm0Bp0CADzpT9UEf3SVCvGwloXi2aFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
واکنس ابوطالب به صحبت‌های اخیر مجری‌ های صداوسیما درباره آناهیتا درگاهی عمه دنیس اکرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27349" target="_blank">📅 21:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27348">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTCdEtPgLjU09kNQ5nEt1rvnEQqxX3eFyOJtA33Q4mZ04zoKaeh3pTLo7xKtSUbHuE7sp_eHn3jBEYPETkYbccSlYWpzdATTOnzvNjcGVBDQdoT5z_sS3ab4Eo-1btzkdm4yCzs7aJB2CQhoPsy_6MnzFgnFPdQESazhpY55_llTfTojkZJ6hlmch9Ivn_aL72D0-PY81qstV-BEqg6eDcduig6Dzrxii1NOD59x1FeACOqg6_fcbrw6tJ205BCw2IdT9uziqw-Bsb7T2OiaBznIuB5pjdt_IEHayVqUpchrQW3ZdA05j-qhphPax_4Q4hqyxkFFxVygcqvuTKttRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27348" target="_blank">📅 20:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27347">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7Sic5D_BL9ZCZSwpID-_lJJpYeARYduoSL4rM8ZorWrFGaKhg22nNSaa0x1q2EfKln-i-pWG1-V8w4OT93xPKHSDf5NoERZY_TO_Jjt0vkKr0GIoZmaeNcvlJqH6FEDAmT1z0cA6u24kpIo8w-Ap7OPV8lPKp4EEge0Sn6DX_r2y7-r-aTXFpX7hVQqs5FHvht9mlJ6oIKfbi3szo6C1-fSuDFJUO6Rj4jbPQ9wGhRp48AAKXV6YLnmxSFLLNKMzL7uG16qZblUGCHSQ0P6j4_doJymhTtzDGq55Od1FgfLW7UkC2lGcLwxqbyLgMDh57HeXRWNbLgON-_zTZtlHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس برای‌ جذب کوروش اژدهاکش مهاجم 18 ساله آلومینیوم اراک 150 هزار دلار بابت رضایت نامه او پرداخت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27347" target="_blank">📅 20:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27346">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8cuZ4bTB85IGiT3pKYrFxKcAy-uy5G6FJ262tpDN1ezeFYTrHkS-4YLZOrNdmDgXQ6fJnvboRxzMZWTRwZ2n_GAP2sYs3mp_Ndb8JvYguL_Lfq5j3C_3AIz4L9Sl6E2MJc3dTuyUejL54e2Mjm0bKLhnP85xxSz6gIPNy7C7OaCkVXte-XA3hXHZpPzeFB1gxjYJWoGYaWq4jevpdnlay_-IsxQhHn0i7aROyyC5_3HnH2UjqElpHqyJCE136c1emviyQJTfLn34CWbsHAtve_9GytQjzExEiGrrohp7pZaZdytqCUZl_sKTR9eZMd4qpFRd4n1IXE9nesHxHlJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در فاصله دوازدهم روز تا آغاز لیگ برتر؛ تراکتور امروز در دیداری‌دوستانه بمصاف مسی‌های شهر بابک رفت و به زحمت دو بر یک این تیم تازه لیگ برتری رو شکست داد. شهریار مغانلو و هادی حبیبی نژاد دو گل پر شور هارو به ثمر رسوندند. هیچ تیمی در این فصل بردنش راحت نیست…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27346" target="_blank">📅 20:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27345">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_n7pl1LHkV5XB3QWs5Ly9gDyOkDN_T0m07spdiY_RYbg2wJ0DVeW--8zz6dnqPw3oBRWWipf-BDMQTLZGOXk_QLFoQOfyxslyrhZRTHpJrO91iirDjFw5__xFtPH9-PR2oDjVQPjVzW8lrXICF4IXtHZfCM-VI_apDK8pdfWt1Q2DXrm4EA9quNzihvX02pgkJZFJihBVkDfYjbP-I7lQCub0WIRVRiTCGGoPX51GBvbOArNAXTzIb1FUzlFdJL8SnZ8ILo5JTvd9HseRcS2Lp_Nh1wCRo8qj6wkZEHOJpzTuXvY1kfzBw1eiJ4_5UW14PScwreq9JVP05aU2-j6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
#تکمیلی؛ خورخه مسی پدر لئو مسی که همچین اسطوره‌ای رو بزرگ کرد مدت‌زیادی‌بود که با بیماری دست و پنجه نرم میکرد و دربیمارستان بستری بود. دلیل اشک‌های لئو بعد از گلزنی به الجزایر تو اولین بازی آرژانتین در جام جهانیم همین بود. در نهایت، خورخه صبح امروز تو یه…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27345" target="_blank">📅 20:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27344">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWfx4obWyaMyshEqmr_rLINKGCWlVMSo6A3l5aTEEdljRjqQnxGT_G3l5duo3zvPPv95pAWVKvHgqWLGumCceCBImRlvO_saJiRhaYfH0V5EDqRwlCr9iVlmi715WXMCFFtGFoInjClOrE3Mukbt1cPkoE_Nkfo69dGDoex1FXwhCD88v4Vo8a6YRF_d3KEuNRVFMYZkutDm-QsVlPVuXnp9RH0ii-xyI7UwhPnT1U0dHe9nYe4iS_VM3GBFcKLsJgdLY97F_9jwDUcLAqY5Lb1-vdqmkATGbaE07XSFbpvWd-8FDgUn3pJFGsxGZGTFmg6Uk8YmGxeTLdoq5k56fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
رضاشکاری مهاجم‌سابق‌سپاهان و پرسپولیس برای‌ عقد قراردادی یک‌ساله با باشگاه پیکان به توافق رسیده و به احتمال فراوان راهی این‌تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27344" target="_blank">📅 19:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27343">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw4KRKUSkl70YCE9fKMNChRZIeJJhRzXVxGMhHgzWncPzAXda9ZltwYiI_AXAvSInO9RMdE0kKPaBCqOf5ci8J0KlD6n2KMIXz7DkkkuiD6FKRNlumWmEmzPErWttQrFrVu3sC_8L1FdnOYTSXxPjaxdgoFDR3quQ2wCgLKO-eg4ps0-AbMjG8LQCYKdxyqsvnWkmqwc-YSJkwNIGk22LQZqTt-EzOJ2tDKSdq1dHupmNOnVT7NUwQuu8PuDE08bRNtBkeSKXFG4hP7ZBHd6RTkDIemz8WF_5R_g6fZLQ9OsnK70F_vSaqOw7KNkXSFU0OT8v6xdQgRnUuyRwbfHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله ماخاچ قلعه علاوه بر آفر از سوی سرخابی‌های پایتخت؛ از دو لیگ پرتغال و لهستان نیز آفررسمی دریافت‌کرده. یکی‌ازشروط مهم حسین نژاد برای پاسخ‌دادن به آفرباشگاه‌های‌خارجی اینه که رقم رضایت نامه او بیشتر…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27343" target="_blank">📅 19:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27342">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehL7H7UbWy_EOjeeLnSaiZq5maIXLN3h-hdLkfRTFB-pHitWffOm71PeKyxJu-2ozDeirZiK48lqIamxm7p8RfrFNFwswZZbJdk7QwgxwUaJJbLGucdq86rR3nadLjLYyisnhkLa9276zEIMRd-SFJHcH5WS3e-Sj1ktaz8yhBufGao7VmpAGUzFn09CIHoVxMIiDLmzHbS32waYt58LsuRGVzPwt2F9-UlQyea6ShMCYC2rqEbjsrsd_5KhDgI7eMWr1FNBJFcgi9vTfvPzyjJIaFxBlLbh_lzsivQRKgMcHFNRBRr4As8fMMWca7f88teOVXLl9xo43Nn9sndx_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌سازمان‌لیگ؛ دوتیم استقلال و پرسپولیس فصل جدید رو هم در قلعه حسن خان شروع خواهند کرد و فعلا تا هفته ششم هیچ خبری از آزادی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27342" target="_blank">📅 19:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27341">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDG0QRbytL3UFBcc5o9oCSgCdxAQKkkXcrKEHniKVzSXAzVeoKbgFRqXQNYA3ahR3I4534bkt4Mff2JAu5ITy41YV1a1sDThOz6OoFkST5pVrDQ9iDtGPVRiQuE0k9laHvH49HB9tg9dGJpfSHcgsdQrdzdvLfP-2SAFjw0enxaFA8NnaR_kGFIeqwE7OabtFIl56CKXuGbLWdIH_ulrQ-1_QKeAetzcYO0ywCzw0I64eVUaGU2bzZxou7cmD6TJmPbiPxEHFmhI3z2fL9eTjF-xY9yVkXWvOIJJXToF9EXyqCLFjgu2qCUhYaR8DrH7DPdDqHP0JXRP8caWN2c8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
باشگاه رئال مادرید دربیانیه‌ای درگذشت پدر لیونل مسی فوق ستاره آرژانتینی رو تسلیت گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27341" target="_blank">📅 19:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27340">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrZXMsk2GOg8y4Xa3SB3r0KlZAIgt8dKpHXRhtz0LSKEQjiMpA-KfHR8k1oOzvaTwj6y39cVB7qYeqdQbBzm3c0E-LkSMSBLey3PFSKUowKBimibEvoy8MANRGNs_obs_xUYNe0NrY3WpQZ_TlDytaFNnYqlnyX55rwQLdNhINU1hdM2SeTU5E2xc6UbT_V63ILTKa8zK-Prtvnrih_A4DiFi1djIdjp1KqOLBcsdGmi2G6SsC0o3Y0f-zWcHShaZ5rDb3ivIhq165s3ZpUyhPCWJoNFaXalTVNEz22u4s2csYr5eNtfZqFAF7DVwTXpfyIaouvOnarDtiql9nYNHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
#تکمیلی؛ خورخه مسی پدر لئو مسی که همچین اسطوره‌ای رو بزرگ کرد مدت‌زیادی‌بود که با بیماری دست و پنجه نرم میکرد و دربیمارستان بستری بود. دلیل اشک‌های لئو بعد از گلزنی به الجزایر تو اولین بازی آرژانتین در جام جهانیم همین بود. در نهایت، خورخه صبح امروز تو یه…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/27340" target="_blank">📅 18:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27338">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIB3i_HE7SQ4Z0jK5wXU0vQzj1WmU_BlSuyKrSv92eBNcZT_2NJ3EVcODojN94iA_ELWAf2tZ5P8s_V6_0I4n12jp39DN5wIA5CgXCCKD9vTf_0IDBQ4-WbLkq3Yo0jE2Clru34j7nrsYZP_UVgc9Bhbe69fkxtYpDpGioYd7YpQ-aQgH018ugvboUr7p_UB_DUA9QyULEz6RdfNZIOGKdOJyGwEPkpLY7Z_Nb4VTPjWRz_e3PX8qVFwTg3V1JfsxnbEkAQws50Ao6cS0Pq5rgOKTSp_3jkOLlNPH4Rx4PlAyd4oHaiX2f9BhJUkDWXZgfgTfg7eCqd3bg5fKILpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وزینیا دروازه‌بان‌کیپ‌ورد درباره‌پیشنهادات متعدد باشگاهی بعداز عملکردش در جام جهانی: من میخوام جایی برم که منو واقعا برای ترکیب تیم و مسائل فنی بخوان. نه فقط برای مسائل رسانه‌ای و تبلیغاتی چون الان یه پیج دارم که 30 میلیون فالور واقعی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/27338" target="_blank">📅 18:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27336">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca7c42226.mp4?token=B04wZ0XII6CMI8i_t1AC_3Vsqcwgu84dhyugQttc_Y-x2x3PBtMFE_tSn38IiJ52eWi6MFwjvSbVVx-9WPWjFSqO4QuW-g5oa4gW9gXIqGHfAzokvERptjkML7ljNAPYXP41hxKDKan1mrBE_cQ3iqchVuw_aMkFque8xOPiy7Ba8igrSU-F7WjeMB_Mnf1lxe9MnNsmnZaWpDP1LvmKisNrJnFmueTRV74857fGZWeS9etAMaDpTwXTmMkO2MteAy_9eZPd4XYraiKy_tewVAJhvJ_D1UvT55kJKS8qR7HrI8tO8TP6U4BD_wfeEOO3S0_N98tx1SzZznJ-pa50ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca7c42226.mp4?token=B04wZ0XII6CMI8i_t1AC_3Vsqcwgu84dhyugQttc_Y-x2x3PBtMFE_tSn38IiJ52eWi6MFwjvSbVVx-9WPWjFSqO4QuW-g5oa4gW9gXIqGHfAzokvERptjkML7ljNAPYXP41hxKDKan1mrBE_cQ3iqchVuw_aMkFque8xOPiy7Ba8igrSU-F7WjeMB_Mnf1lxe9MnNsmnZaWpDP1LvmKisNrJnFmueTRV74857fGZWeS9etAMaDpTwXTmMkO2MteAy_9eZPd4XYraiKy_tewVAJhvJ_D1UvT55kJKS8qR7HrI8tO8TP6U4BD_wfeEOO3S0_N98tx1SzZznJ-pa50ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مرگ درپخش‌زنده‌ی تیک‌تاک؛
یک تیک تاکر وقتی داشت لایو برگزار میکرد داخل‌مخزن آب پرید و چون فضای‌کافی‌برای‌چرخیدن‌وجود نداشت تو پخش زنده غرق شد و خیلی مفت جونش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27336" target="_blank">📅 18:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27335">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbV4H0axGqGPv5vw-Gl7FR0fRy3JC7e7nYt8FOrwU2Xys1m1mWYmoIuELl4FyDQqkrGCZelNMHiJdjK_h212KtxvW2oSVghz3uVoO5ivfqYzZLi7fyUab2pcV5cco_aynZDATCmJNONrefQsXO4jhIk333hF8Td3EFzOTZ_TpuemLvkG32gD0DSu-leoVXQyEERpp4vQrrIByGbGC1ua8hm4rgPy2JEwfps5GWNjXzSZ3jBKgoQS_Isqe1Do3ViM5KvS4b-9MZt4ltGdJd1x-EoEjv-H_eKTCqDoxBOd-bjuQH2QLC0Sd3cx8Kse7GhYCfjXb4VgN5ieV0Fk2UIH1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27335" target="_blank">📅 18:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27334">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9v0CLMkmEcH8MxQcRDmLb6FYhWxZGQpmG-dDJOHmbYFfDFM795ar9CppTlFWDDdaEL_4iS7mehuTDGI1whX324qP3lmMraeQa57OOaz6JJ8J5qeBYaYSO21vLA6aUsIRufMkBzkGsmrLP9VKTwDGwePYW_V3KqXoGc65mW2qLy1bthBr4WVS7g-u-h_hXIanscv2T2uFd-Zz44SGMSdSB3mlhxC2kdj-T9YCfqiT8V5cGjSMujRNb17EnI0IXxH3jDomMUpiZaOSY8U77brIPNdBvLzDtqqElM4vVfNHwWXfhD_hqx0_KihF5zLSuGOhZjo3wSQuDmk5JjIDcdbPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27334" target="_blank">📅 18:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27333">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU-IEInOH0xrvrzpJOmOt37ScO977Im28NH2g-5y9fTguUSrpDkKGX53JqqEkkWIgacHn-jKmdEB7qZBWIuPwaygZNYWahRplJWYWc8yfI2uAWstkQeHo5rMo8przAomR30xkElSIJ-HO4jSIFd4FExkkJdYVvbfaxfakUncSE4tbZA8t1jIgw4TCKNmfldDjc5qNhVE4Urie_v8UXTqQwfe--dtuVzQ0HFyEwdD2rrY4FMAjzXB8JgpYmmQsq9zRAE8UL1PGruMy2rpe91rDlyLZBfkY-vk_Uln3gz2p7PHhSAmtGUdWt_AF27ZY8PMrXT3OhYRcgOxy_nYHd9SxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌ امروز؛ از مصاف روسونری با آبی‌ های لندن دراندونزی تاتقابل دوستانه یونایتد و PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27333" target="_blank">📅 17:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27332">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZXP4imYwz-Q9lU58ha2543TTemeliTs1XdoeSqz3QYC0CSdyTUZ0cyc46wIQpPJRTV4NDWHUnCNiTQZZprAM9RZ-FBdxWzm9naldrYI50EQDilwEBZE8p_ydl--M_wHMOGQlNTotfqAtGv94RDDeB17F9kaztjP_J1jVhl_pfFmsvPrJGCD7GFhW1w8m0odjLUqAAb18JCEqMElJQGLPXwpGQy4q-9Jt1KGtrETmugOi9FAi39KVvMUl1Cv5pEaV6eLKGtNdcno_lf8KWz3Uqb0VEUOTH0OdYPk94DK6FbhVBDqbYLrYkctpLZXb4JytmI9pmIalk8KzrWZXwG0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
#تکمیلی؛ خورخه مسی پدر لئو مسی که همچین اسطوره‌ای رو بزرگ کرد مدت‌زیادی‌بود که با بیماری دست و پنجه نرم میکرد و دربیمارستان بستری بود. دلیل اشک‌های لئو بعد از گلزنی به الجزایر تو اولین بازی آرژانتین در جام جهانیم همین بود. در نهایت، خورخه صبح امروز تو یه…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27332" target="_blank">📅 17:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27331">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnFnRhove-Rpne2GTUqbdgU0TR2uXDhNMrlOYhe67SF9sy27_7plpscsZO0TdkggXFf2-mBc5VfWcVLUC1zUAADdcirFgjzKuLaHj1GifwafNhKN3fXD7753-wQcNwNsk_dW23jvBbgGqXy1TLRfiQgE5LxoBrN8RFJmYptm3kOaLvXemidZF_K2WZLQCLjHSRiKCDuhUVz4UDxD3fqFbF8MRfooPVwM6V_rO2IM50aRVXxgUg0uO-HKlkUp6Wzi_MJOsuxzt07ocbwJ84EIZfwbA3eppo8SPWNvcEIiBtcCyApkjb9L61t9vUxWDqTo3CilGXhno3zaIebnv0IULg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوباشگاه‌استقلال و آلومینیوم برای‌حضور قرضی شش ماهه محمد خلیفه در آلومینیوم اراک با توجه به بسته‌ بودن‌ پنجره‌ آبی‌ها به‌توافق‌ رسیدند. درصورتیکه تا روز سه‌ شنبه پیش‌رو پنجره باز نشود خلیفه تا نیم فصل راهی ایرالکو میشود. سه شنبه آخرین فرصت باشگاه استقلال…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27331" target="_blank">📅 17:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27330">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XK8nmZgScBtshO4uxoVYcqao-G43IHZQN1ERp0KOxED4r2eiDc2Xj9irczehM7Tsm27QRd4tBGsZVSGSnuiBcAgeiFI5Qs9nyagLbT55SJ1U5FoI1YCV_LKF_7rx-h8OwP3hjrj6iN08h7H8neQACa7RUaT3c6MnZUyTlKvgsfm3yhaHJNFMS7PC2VkQqE45c3vgsx2TZfJz2BXi5xAfv6f8Zdyo8QOu94cW8GfccduZCG-12XVIvbYHg_oNZNQmLaTGFia11Rikr-PRf2fVOqDMABxacdS4xR08Xgs-TbvGIfc6HJ1XAGhIEmm7KVQ_oKvFZsckEZhovJuRUaNZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیورونمایی‌تیم‌پانایتولیکوس یونان از موسی جنپو وینگر جدید خود؛ طبق گفته رسانه‌های یونانی قرارداد جنپو دو ساله و به ارزش 800 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27330" target="_blank">📅 16:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27329">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATFsK-JuW7y8J_qo70eSen-710oTEx4anM9Bv-a78D4Xu8qe3I7PY3WJ2ep1soadtCNiM9QxLvlRTToTHNsOh6I8qYQRGFIMwZDhhTxkPCsm4lRbB7ACHuN4StdOU1DjgW51eb9HPNLkJ05OGrn5pjUroLMBYfypbGae2rlfeZDpM5TqmUfMEX-h3_NAvfivgBZNL8iacb8vmlFm07r5FAFShIjE9z0Wbi2YR9iLHjkDTY7n_AUjQ6UXdDJFnwQPbbzuKjo9siJLBIXwGGa4KfIvw0vWiGQFr-V-LW3oiussckR3ZVn0Ro6JgG1B7dOWrSwmajQ11UKlEXwOFUxkPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27329" target="_blank">📅 15:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27328">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDBbCG23b0rNpzWXfDPVqnzkdXknnAGGu2aEyFpWF6gsnAuCTZ21BMgDzx1fkhlLO3rUYj2W9HI6Rw0l-GGqH1XeVLge-chGx9IaV-b67sFVBevCXrlfxIDtYopqkxg5zqMY9VmUn_zUYh1x3PPlfjStNKqss8dv9umnzHnQPN2WLK7y96QSaXllshy2KT2Pef_LJalJqywyOgbYusMaf3yDkKP0n9lT4ve_MWy9oFUT6ihiXI5ePZNwFzWEMhSOWbVITWz_gLnINeslmXRHxWwy63kV-ByhcnJkiTxIDYH7NKXv2Ks3tp5G9F19FCGrS2sGTEqmaFbrXevH6amXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پیغام باشگاه بارسلونا به سران پاری‌سن ژرمن: فران تورس رومیخواید؟حله 55 میلیون یورو بدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27328" target="_blank">📅 15:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27327">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C50Ff2Kt35-TNYgKohY4tXI_J5CIzpy-NWeGDcYN54bwAhcq6yw91HTsfCFKNeJJM-mkQLDO9T5QbZew1l8dRH1mUsxQAZGDEqGx5X_abeAL6iJcDfJjTKOjGVKXJ1ha4AzcAYTh8iivhjmQR4RsB3fp0f7Bta8o33Ec7rQnA7k1UrXBbFaq5N_4niUtU-XhkITMyRaOHESxWmxRYbW19-8HxxWp2aZ6M-OiCv2IRhIrlb7mVZeqlADakRh9ZqoWNP2lkOKhysvaswKIE7SEqfi92Ukz0gXh1BEjnZQMGMJPZrZe9qqPT654W2mProA5AUmok1pj2WLd48TXOxDCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ سران‌بارسا قصد دارند بعداز نهایی کردن‌قرارداد رودری برای‌جذب‌کریستین‌رومرو مدافع میانی 28 ساله تاتنهام و تیم‌ملی آرژانتین اقدام کنند. رومرو برای پیوستن به بارسا چراغ سبز نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27327" target="_blank">📅 15:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27326">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNbjYIzfisD1AbtzywU2i5SEybSMBLPvQZ_A6Eal1NGudHdn-v0Y9S3Kzk7i5Ni5A4YplCCGtWHdTQ5k4qiAHjaSW4uTe7pc4-XavK5dEEj8lH-_WNUHwIY2koH_TNoVzIiYbt7fWnkdmRiYtWMVtZh0oMHOZ2O1ut52mT8ZJTUV6DmHV0SM2cfOwUsibXrQ_UlkPJRCr-FPpBLDvn8hIQJmTDSA_0ZDV-t3qRFx8EYg2fYjszHfTxi0L3S6oauKcONuJq2VD2g4ZxZxJVKR9N-EJMTQim6_yWyi2Zz41GjFTR__Hmc3T1ab-9mXJqtpJ7Fb3bEiSb8dEOXBdUAb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27326" target="_blank">📅 15:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27325">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsamqxMbKOsPGqITmO7MuNOnYddvVJVGPzebZwGrsjitDR3t1WRxUj8zE93WdzgTrhqtX7wfaSA8HD0LjCkMlZMrnY4YmXBfRHLK0ZUDTB8aL99E5hVHkA6jyETAoZqF90p4rnjKdxnwbev07g5AK0hkvE7gIOF7JgFIFwdTCPGYNkoCTrnrEe_kjZWb1EQhRzVY57yZJrgAhCHgF1C7Zv2ccJbISJu9-6k6_pxYpkhULuofwtfDZRexMH34CWZwriTn4gV4YAO5bYjNcJNs9upmZ5pgD2CT3sF0XwTOiLmbuCybDKWZwgervJYo1y9mRh5GcNAfP1MFBGNWF2lsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی؛ هفته آینده مراسم عروسی کریس رونالدوعه که اتفاقا لیونل مسی هم دعوت شده بود. حالا با توجه به این ضایعه بسیار تلخ باید ببینیم لئو مسی دراین مراسم حاضرمیشود یاخیر. البته ممکنه که کریس رونالدو مراسم عروسی رو عقب بندازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27325" target="_blank">📅 14:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27323">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6yjVBwDas9Yl5s8c-tgCMyilHVqB64dgEUSWVvPiugGPolVuk2A-oLJV0GgCAwdoR3YWSnEiD5oaKPkXrSRuWLqgmjxYyezDpQeJHgefdnJwZjGeNsCREJU_BvKvolLK370e_1tpLOSq_BhsPvRtZu_MVTQ7ab1HExM6KZm_hhRTIV4DUhMfCxoxduuh5YoKv0pOxv2Dr8mzoxKQFOQEdiy00PURyYROuRJXS0wZIyJJMAzQ6qIKascmhTSxz9sfVs9ZkYhf0gQP-I45rn3zj-iu4teuP2ivH_EbD3I_JyfLkvWy4C0Ya4Dz200e68Hs7-ezfHex-Q-dwSFEfbrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRqhOsYA_uvYlH6eXQKCiXStBQqMSM_G0osWr9vcAOus8IZe7LoLyErc3qpWDWCilnIsnXzPUhdrANBplDqkE0coiOKxXTE5r2q7oDLh6D_aY7PMBNzCa72Y99uCVBwvrBSz5NPTbssqlklyK78gRJqfuhY1UcXkod_VV6HlGjCVlTvZlV3F246Ng1-P1zS3gP0T5aWzaF7aS0xsXT0oqfIXBzOKIHRFTWdvMVzHNO4GuyM4rTfX-WynWTkLanizO30hmE8rOq5tYRiCQhI_ObiFcGBhl7dJuNiAMLu2dRiV-y3P7EOAX5l74tABWe7di8YS6b1OgLPCUvKlsWpAmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
🔴
🇧🇷
رومانو هم تایید کرد؛ باشگاه آرسنال 75 میلیون پوند به باشگاه‌نیوکاسل پرداخت کرد و برونو گیمارش ستاره برزیلی کلاغ ها رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27323" target="_blank">📅 14:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27322">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI9ENzlPE2OvLBoM42FDEhgmcKF_GFHLHbm8I5D0pNDCLCYg5OrlPZtR6UZ8JrfmovNX7EItigj9LTcOaF7msdp7AUw2gd40b3EpmRw0eA-fJMH29x0KGh7F50PqBfm7Uehyj-smKQ0TjVBLAALs0kSVEFRgJpepoDzAyGkWXgRMggNBbGkQN9vl2y0jlhQqt4oDkJP6L72WJIloP_H1hvbQN0848F8pP3VdfIFIbf5xFAyfhburkZq2Y3LnAq0-EK92Owvlm2xILYDOCJJbUdkxg6fNWNTIUDq4JCZFCANXBtEidtBJs1BcXg0FIPGCPjv-WnzMrs5cMEkU_dDJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پدر لئو مسی فوق ستاره آرژانتینی فوتبال جهان ساعتی پیش در بیمارستانی در آرژانتین درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27322" target="_blank">📅 14:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27321">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC7n9QGq9N8cVyyWnmdHLIi8NKNvJIVD07iew-AEHW9VJ4It1iD32zJndsINZEvDVvaEMzflXPwz-8j3HSeKEZv4ZXQ37M_mj9bL1OaNgxmGuDd9uC-Tc5f-SU6qvtIdGc-UkLIMJl0-xVxDmlW_YFT0YcubCjJsMXa6AEnsgGcNqKqdrtX_PZTxumvRj0fO2bchiNlJ4gHqqWBjj9_a3Oev9m87orMOVJ9o6-ssahFMlXMm6lq0xRE1VFkMHbNcqIArPgLlgigNFxENv6uVUbsIyYbCEjlQDEBdG8OtqDiN0xR_BgwtiRxWVb4bUgKt8jcjxDQoJ-DDcjExXW1vYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پدر لئو مسی فوق ستاره آرژانتینی فوتبال جهان ساعتی پیش در بیمارستانی در آرژانتین درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27321" target="_blank">📅 14:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27320">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euzZT1mSvXBd5WUdy_NJZ_z4vP5kcQwd84jUblF7O5Yg4AUMoNfcJGNcAM6jvn-a2RmNLS8y2AfZSjoUQunV1nlQp0XI315E_lAVFeQvGPyR_FVkpj47glPZgkdMzEB2NNOB8GkGI0e6Rr2tdJTxLc4elWO8sOiNvBTaHObwk8jeDcbuVfAuTwkUmzy7qTqNwnX-adJtINrDlBO4yPpLyqw71inyurAB6aYaRGNKYdepSE7nhS2jrED4YwGGYJHkD20etiUlPmjzbhQNiecrmcY4x2k3XXBTyfDktN-16IR-M5iHUSVYrrA9eJCnuXC2Y0bYbjoGRYaou9-mJYW7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27320" target="_blank">📅 13:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27319">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fa190d851.mp4?token=Fajo63S97JBS7aICF7I5DvK9ik8lF3rBk-mH6NorEczMuN80czHQMddwSy5lxe5QsJ814FlYcJgxOUbW-7mtFYz13cbQ8lUUO8GNPJDCnwDycpUborr2j3xYi5Nrj6Wp1cuK5Y5X2a623Fco91KlqjnfEKW6Mbdo1TORTKcQxkcX8w1NNT3GDuykNWw1zTYsBSHPtL6vvGp0ZH2Gur8vO-m0ZxDJ2c0Qq5mkwdIUR7SjVhKfXmGTOiZzFajHr7he4tIMsXgvTLHEdkydtFSu63EBsrlVcsc1piNid0R5EaqditLT2vqt4vW1gDnm32lb_UZ6JVAh7SGgCcw2gy1rOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fa190d851.mp4?token=Fajo63S97JBS7aICF7I5DvK9ik8lF3rBk-mH6NorEczMuN80czHQMddwSy5lxe5QsJ814FlYcJgxOUbW-7mtFYz13cbQ8lUUO8GNPJDCnwDycpUborr2j3xYi5Nrj6Wp1cuK5Y5X2a623Fco91KlqjnfEKW6Mbdo1TORTKcQxkcX8w1NNT3GDuykNWw1zTYsBSHPtL6vvGp0ZH2Gur8vO-m0ZxDJ2c0Qq5mkwdIUR7SjVhKfXmGTOiZzFajHr7he4tIMsXgvTLHEdkydtFSu63EBsrlVcsc1piNid0R5EaqditLT2vqt4vW1gDnm32lb_UZ6JVAh7SGgCcw2gy1rOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
ویدیویی‌ از خداحافظی چندفوق‌ستاره از رقابت های لیگ‌جزیره؛از محمدصلاح رودری‌هم رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27319" target="_blank">📅 13:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27318">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgpZrHbqmhJyNfk2P4E_09iP26650hCHrGteCv9CyFjf9MmzOSBpKDKK8OxMkDdvvdHVlTFzTrdrPksbjaKmE4FfmnN_76hUjjoD92v9-3B7hVf4vezboTwarvY4zcgWeBCenDDXZIOJ_GN3DODo-3O-ynxe7kvcG6HIcDnVuasRqVnuyu-hhHn1HyXk1jHkvADLxy1yz6moyj3afFpD9O9abhv3XQ81EUMvz7_y2U4kDqkiP8w5u8RmVlBCoDAtoqY0cN5wiwofcrCvrFwd9WLUDBJBK3EAxjfHBnmBHKOlC68iRvdNKFUvTbCSgZcouDJ265YG4_dthWW8ULiG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27318" target="_blank">📅 13:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27317">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎙
زلاتان ابراهیموویچ: وقتی 20 سالم بود با یکی رفتم توی رابطه، الان دوتاپسر ازش‌دارم، توی این 25 سال حاضر نشدم باهاش ازدواج کنم چون میترسیدم اگه بعدا طلاق بگیریم نصف دارایی و اموالم رو ببره. بعدازحدود25 سال یه شب کلی تدارک دیدم و فضای رومانتیک درست کردم و از…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27317" target="_blank">📅 12:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27316">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUXoXklC8P_5LemnqTBXlwxvHMHOgs6YKVS9yXjaUlZkv440KpUVJVhE6NztctiEf0MTmPyBjhWlDLyO-7YkCQK1D45mGLA4jeUMEF3-QBHXaB0SGIx6FZKBS0uBaG1ALCtxaOBJQ3kVWAzQ8e-CJuZ0XHHYXOaZb8w_CETvICVAKDSGzscrQ82_VsZpV3tqwGW7b6AFy-j6mvJIJwm_ltj2NFA6tvIPRlUACIiYNj5Mf3fNdEIrKucQoo8HfOOtFmc1ox08uuouUvK0O-8EBp9M-KI1zQ0CKJRY1UiHPgcsSeOp_DQWIYLgyfMJOxTwHT8dVXLt2oFwT5iahdJYkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:
رئال مادرید و بارسا به احتمال زیاد در الکلاسیکو رفت‌لالیگا که روزیکشنبه سوم آبان ماه برگزار خواهد شد با این ترکیب بازی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27316" target="_blank">📅 12:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27315">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGBvwfK_OO1zNNBT-xbXopcvHHXMrMv46MZZ5JbNoBD3rE5SXSTSQF6zCY5iRTR8o0RXG6-WQozgjO7y8CUAJ3Tlq-e0fr2wCvS-aHxWdV_Si3Xb2UWCGcyXV6IB75xaqtiOiD91Qqc185XS8bkjWUPYPPRUWjYDrIJ6sPZs0gCqv7uPPvQFY6wBYxUEPczLqgoAvtQMKbPGu0ISV-opSRloh27RGxCTaAjOIzeTMw7Py2xp9UqtYh-Kc191ihnNrMavYDN1mN3nVkELBCCsBNW6P1N5dDdrNT54yXIzj7S7XqxOJYLoisrJT8ORM-jhk8BqmRy_GY00fgUR-xS6gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
⚪️
#افشاگری؛محسن خلیلی بدون هماهنگی با مهدی‌تارتار با امیرضا افسرده مدافع میانی 25 ساله ملوان‌مذاکراتی‌داشته و قصد داره تارتار رو راضی کنه که بجای ایری این مدافع رو جذب کنند. مدیر برنامه افسرده همون ایجنتیه که با مستر خلیلی داداشیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27315" target="_blank">📅 11:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27314">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQmv06BttAITpkv0zxPoihktEYdGOB14uGQbHpRo-hunUOkWnPiauCAluX8CFTFhWQMTbxSjqrLU9VV7DcFYE6wCmEabDHJWQNsH7bQUQ4n3ojyFJpeQgxhuuMZB9lMcqKUG8mWnNZTFYC4ZU-2SOq2wD8sklFB2bFoDyrwVPHQnGieE2aQxwlX2eaVJTVGp2s1L8jCMwtbI1oFSuVs-kcYuynFDEuActjz2kjE9f95ZnykLAdlZTzWnWFk9l7mdWNlZG2A59Usbh7Se3slU_T1hrD-zR0KAP6ZOBKmjuP8DC0rwR6tElcgAIW0TWUbdEjaIIkmeuWEBVCPJRdntRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27314" target="_blank">📅 11:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27312">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX8OAzXYopWWMbcLBLAlVeJCzJdbZhi3kSaqmd_Qhf1qm0buBSh2mwGDxziTCilWgT_QQ8aBIBWcLthTI0xgac1jsJjE3ZBa7VTsBw5VPprgWkGG8PxynM7aVa8y8acqGU1Sam48DDUNLbzHnh3efvy7MV7WmY_2x1lNbUOeELKYNzJoaTpdUDtLnFgQlEdjRDc-KJS7iT0CyHQkNLa2J5w3tCl-6WJ-hQtRGjvQqeJ7AmCimCpSX4E_5l_G5KuzEVvEjfuhK8I6T-1sAGmGBJSe4-sAwuZ1Ucc_tko4WRx9VnYjoqBoHDSzsYo1NCx3ergADUJjZUgM9FBs1WdZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا؛ احسان پهلوان هافبک تهاجمی33ساله‌سابق پرسپولیس، ذوب آهن و فولادخوزستان‌مذاکراتی‌باباشگاه فجرسپاسی داشته تا درصورت توافق نهایی شاگرد رسول خطیبی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27312" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27311">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoL4JKMqc8ZLJIMC_BzPYrFxXLwidXO3gGX6VVPgKwZ-am899wlaGUYmGCIWHGK-04llZGu7aUSqwjW8ZXTlsKtKA__VxYdfeqUHk0VD8YckmHgJeBQ6u3biwAKLj9IzcPvHuhRxAN9ei0sXRyEkDQ05Mtb7AIeiXySKjkjBaqRz67fc8cBG97LqyxJ6cwG8ONYFkWt_PusU735gkYt0xiQxTPTDLE_Rouo8tchA7U3jCpbMvdDqtBilW92MVCgqD_0lU-yboysL70DrVEy00NiDf6QUvcbA6Cvg1naspblqDgnMLiOWKAFFX4U959hl57SCQcxOBj2VV6PWCep4ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27311" target="_blank">📅 11:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27310">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a095528f2.mp4?token=MJHsEH31ii73Mprg_JqNPa0jA3hzMtouYVOR1whAHN1XBvcXxuS5H3o0wO3fU_C0svFd3aAYSon9sEVvMz8bYxmQTCHtA4cW2EbbQDF84oEX0YI12XBhf_JnjlfSI3gLuutMWBXm1LN_LmeR7SL7S47eXqMuZb4tpkfg10EnBXPaQwL7UaG7yq9ENEavWppGpdD8a_sSG7EeDSD2sy5ZeCq8QnlkU5f_iaZGirp9A5mjYojxyi2bMhIOgUKtDoiBHE76wRpc4pNPSQ9AIdzyrAv9dhnX3LFBG9wdpawdhW6dyNzw0AeXn7YW0oJ15nj4wjpgBko2QkH43W7jKk56Drfht8vAX-KU_27KL84_9f2nC2gkD5SGgxy3GVlE8SyGZ2I8Pe19OEZ7v4qG0-_Mysb4KFi4hVJr9sm1cRUVZyLWbezJPZ0w0tNTxOazrlOKM66CMCobTdzkYL5vwqk4wcDu_rHWn8VzKem3ccRhPSw23xIb4Evc7kz2LNqIZhRob-qFKreC7ibuOwGLuHpBYV-42t8_qNxQwxtcJC4okWj1oZFWZlRhL2CBV2-TdpqSXo51xOc8TZB-5voS6SKN9V-xs_abL6P3OFnPGCWKCEMsPkkZtYtCA_B3l4D74xrRa6HV_gIoe6oEcfCnSRdiuQTNooQdejw1a8uSB6M8te8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a095528f2.mp4?token=MJHsEH31ii73Mprg_JqNPa0jA3hzMtouYVOR1whAHN1XBvcXxuS5H3o0wO3fU_C0svFd3aAYSon9sEVvMz8bYxmQTCHtA4cW2EbbQDF84oEX0YI12XBhf_JnjlfSI3gLuutMWBXm1LN_LmeR7SL7S47eXqMuZb4tpkfg10EnBXPaQwL7UaG7yq9ENEavWppGpdD8a_sSG7EeDSD2sy5ZeCq8QnlkU5f_iaZGirp9A5mjYojxyi2bMhIOgUKtDoiBHE76wRpc4pNPSQ9AIdzyrAv9dhnX3LFBG9wdpawdhW6dyNzw0AeXn7YW0oJ15nj4wjpgBko2QkH43W7jKk56Drfht8vAX-KU_27KL84_9f2nC2gkD5SGgxy3GVlE8SyGZ2I8Pe19OEZ7v4qG0-_Mysb4KFi4hVJr9sm1cRUVZyLWbezJPZ0w0tNTxOazrlOKM66CMCobTdzkYL5vwqk4wcDu_rHWn8VzKem3ccRhPSw23xIb4Evc7kz2LNqIZhRob-qFKreC7ibuOwGLuHpBYV-42t8_qNxQwxtcJC4okWj1oZFWZlRhL2CBV2-TdpqSXo51xOc8TZB-5voS6SKN9V-xs_abL6P3OFnPGCWKCEMsPkkZtYtCA_B3l4D74xrRa6HV_gIoe6oEcfCnSRdiuQTNooQdejw1a8uSB6M8te8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
ویدیویی از عملکرد خیره کننده و تماشایی زوج لیونل مسی
🆚
کیلیان امباپه درپاری سن ژرمن؛ تیمی همه چیش تکمیل بود بجز داشتن یه کادر فنی خوب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27310" target="_blank">📅 10:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27309">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🔴
بعد از جذب کوروش اژدهاکش؛ امیرحسین طاهری مدافع‌ میانی22ساله فصل قبل نیرو زمینی که عملکرد درخشانی داشت در لیگ یک برای قراردادی 4 ساله بامدیریت تیم پرسپولیس به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27309" target="_blank">📅 10:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27308">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqkVpg4vH1j2su9pWRL3uIGLtJgbqn3-hovpWglycmpLWWnPnW6B3dVw9bzrmWrTm6KFVMmI5xpW1HEQNH3c-FrSLSCBRRfCgOArfNJm4fsG4cv77MwJLBENqpk_IQGOSW6nOaHLjsbR01IRBsOqcjs2LrEaJ44YtM5tAIYXM87PpbRUFmNXUiduFMEUOZsEyYCnPQ0kvxRuP013uuScrxLi2LccmymlferKWnsfcM7aUO96_yx5f3uTNaddpnoqF690gxqdXMAsmYudflD2Km0qlJ8pEr6GJZG00a5LjIjgbe8xYc68q3TIRlC2uE9RgEYro4qAF0MnpvLH9z8cLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
کوروش اژدهاکش ستاره 18 ساله فصل گذشته آلومینیوم اراک برای‌ عقدقراردادی پنج ساله با باشگاه‌پرسپولیس‌به‌توافق‌نهایی رسیده و سرخپوشان بزودی از پدیده فصل قبل رونمایی خواهند کرد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27308" target="_blank">📅 10:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27307">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E49ym7q23kLfsed5oOQayN1IGNsdGFZ4SM2Y_AaCCm-YKJnX4dN31xeBp12qHT6zbD1EPPzbNhy9uGT_BwUGcDliNLZ7_JypnDrYoQAHpS00yIjoaUbTlFf9JcRk6w_XtLLIOWiH7dllZyFXBbd-g57t4UuiyzeyutBYHLjFBIroLpTGYjJOaVy46iIRATMG1dCRS0wxkJ4Sr7wypw2He6N-YQ-psqCN-PTeDiGKJrH_6is19luJpxfj6UPONrVq33KE2anq5MCuhrwL2vX4s3l8HPfRIZKLCyszhHPClU-OhZUMjmDAyCnblQaJrgOcQLeOlGfXFxIDmC9eA6P2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27307" target="_blank">📅 10:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27305">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM7yCK3RYRObcxYftTJAk6cd79i9pN-Y_QfqOrtPuyp3cz9IJ2iBztiK66pL-L4KExzEUlvaQIqpC29d45cdllzpc2PlLUIa4wNW-VpZOEA3PhDusiBGgIHCwdhlqlg6xCTQDtn0yN1ivAg7I_bAkcCvj_WklMVxpv5xxPi9iDVv8nYRfW6-ctPpUlpkKTy4hzWurFYt_79RWVNzXBF_-k3drB9Av4xv3XJfstdBGcuVs2U9_nyx1W_lwy3S3Vt9SDS5lVQjMAGZhLJoIekbrrsd1dF3KsY9ox6aL5VfKXnmA78IxKsIRfiDQCJJSKye11oSvh80SHvhFF_OEUwP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
با اعلام باشگاه فنرباغچه؛ اسماعیل کارتال با عقد قرار دادی دو ساله رسما سرمربی این باشگاه شد. ارزش قرار داد دوساله کارتال پنج میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27305" target="_blank">📅 01:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27304">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7GEys4qE5aYjRsxw7_wm9qOPnSpOBZ6yCduUA7dV-z_ZzFR6heFnbXLSIjdcDUMfRLvpiE6-SoU_5LDZGOmg4W39dizsbtl9jan541wt-sVrv-eTGHm_pQBEetKgreZIyEuYcwkNb-Of3_ydh3aJvzDKHgE8lI1k8qGqfc-QXRfXqAc9002EmDLbEV7NknNtOSpeolX05z8ZPWfKCbCvE9HyGkDTLUnBy4qCcb5QUMuntDPRaORR8le-0NSh66WBbR_F-Idw6fYvjmfDgj5Qa4seFg-oJWEFfuZQ8YLy7yA0HEQQGqI5HMviFF2HA2pJ7r9lUc-qdkoxPEgxRxz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
کوروش اژدهاکش ستاره 18 ساله فصل گذشته آلومینیوم اراک برای‌ عقدقراردادی پنج ساله با باشگاه‌پرسپولیس‌به‌توافق‌نهایی رسیده و سرخپوشان بزودی از پدیده فصل قبل رونمایی خواهند کرد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27304" target="_blank">📅 01:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27303">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc07f33275.mp4?token=U6geduRT6KcWvu659qrgDWiU6dogQJpUvKwPX3Un2eXf7Eun5uQ4XDI7y4h3tEIpRDXBOUhpKqedYOAPv4WCKcJ66haiCMYZ1ZwRzGq3hWlZkiq0sKB0QZdpD-zCmrAFu0qfUxBe2nksox8Rw2rFukmhbnfmqdZjrHI_EyQoUPKMRGGKtG6GU51y-4WMsO_EQbkHanP_59xfiab49JZFE7E3OnjazKxw8etByKtNpfdy4BXVXoxdpEE6Ygq4bV3gW5r748wsXTaD6mn8OHCLfm2NUas-JioudYLx0WRD_TxHhcW4SiT3vt0Aad1ogJlp58diFrK83DoSvtUY8dwupDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc07f33275.mp4?token=U6geduRT6KcWvu659qrgDWiU6dogQJpUvKwPX3Un2eXf7Eun5uQ4XDI7y4h3tEIpRDXBOUhpKqedYOAPv4WCKcJ66haiCMYZ1ZwRzGq3hWlZkiq0sKB0QZdpD-zCmrAFu0qfUxBe2nksox8Rw2rFukmhbnfmqdZjrHI_EyQoUPKMRGGKtG6GU51y-4WMsO_EQbkHanP_59xfiab49JZFE7E3OnjazKxw8etByKtNpfdy4BXVXoxdpEE6Ygq4bV3gW5r748wsXTaD6mn8OHCLfm2NUas-JioudYLx0WRD_TxHhcW4SiT3vt0Aad1ogJlp58diFrK83DoSvtUY8dwupDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی‌خاطره‌انگیز از تکنیک‌ومهارت‌های خارق العاده لوئیز نانی ستاره‌پرتغالی‌سابق منچستریونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27303" target="_blank">📅 01:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27301">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3IP_Kue9RnuXtwDEXZR3sv-BLHwAXfC4IoVm14S1WAerfa7MdGYhk9KytZWqxP2eGWFIRwsG1m_hrMzgKR7ASm5QKNDaqGLwB0xKRFc56ofzwBjF2iKZzZVCgOXIlbMEBY-nw1CKHY1RmhUgT7wGWgMm2NkFkM2kyMqYKQcNG7kra3zxnPeBrIXfhriTkDt46hUMiCPdigm_-efbRaJ-L3urOMzuJyq0GVKlFLW5YZjZiMmvNZIHIW1euq_CD7kQcwY67bRQPYCYfdZDcVQ3SRaRl3ZE2twy_mh9ORQh_hW58E4ipHBHzg-_kWqyLQ-wR1zQvkQNoH0hw2LWjhEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛
لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27301" target="_blank">📅 01:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27300">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reor2gnv7W0t2zn6e4QpY9AAvwZ8RCNptzZqkFRGOTUGOp_4Dis0QsZS0gOzxNkMK0sv5bSwnTDD895T-9fTnSmoD-EgV2fH_N-enyTH6O9-77kb_qRxV_YVl6X_r6Qe9pom_i-MtZxkP_jw8PhC9jCAXqNOuf3bM5tPjncMsC5cM4rZ5_SDtcEnRNbVZYTixy0rEjWPeAAGnO05oAZySELZzjk61k-qmwTTDuYyesgQuJOypvR-0mKVgvlNzEnXHZVsI4dgh1ZuP8y6_bAT_PfgNhT7zPc717o56-fi_3UGwRTA-uW8Q7woRg0Knd93-egojiqA-H_NW9d70LQv5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار امشب‌باردیگر به پیمان حدادی اعلام کرده اولویت اصلی او برای پست دفاع میانی دانیال ایریه. باشگاه‌نساجی هم اعلام‌کردیم که منتظر است‌که‌باشگاه پرسپولیس 120 میلیارد تومان بابت رضایت‌نامه‌دانیال‌ایری پرداخت‌کند تا این انتقال نهایی شود. فردا…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27300" target="_blank">📅 01:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27299">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leSkvpqOVIemhyl8JN2sU8dvGXVq1mMUhTdnXAkTxadyd_exekaQ1Pp6Cz-in8DScLlVg5EAOLf3wVFTmhD5XDW5wjttzx3cJXlgqraizMXYtM6Cj459wJbCg34FKS8OttRPTmYbzYkAdKylE5EZcSh1oUuTGrgz5VNouhqKvMsurOrczsmAZR5ceyn23y_42kv2U7vp2xCk-vKxgJ-HJVM7sTHiqTr9VtYLeEG1VWdrxyWlePFiuMe535dqqeMWn4qdHD_0pxgCh2_FupOq4zBLYGtFyNnsdhKjAhEuz5I-KLFi4aUfNaODS6-PMwFOmlWfJlPHAo2EcuncTiN34g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
⚪️
#افشاگری؛محسن خلیلی بدون هماهنگی با مهدی‌تارتار با امیرضا افسرده مدافع میانی 25 ساله ملوان‌مذاکراتی‌داشته و قصد داره تارتار رو راضی کنه که بجای ایری این مدافع رو جذب کنند. مدیر برنامه افسرده همون ایجنتیه که با مستر خلیلی داداشیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27299" target="_blank">📅 00:46 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
