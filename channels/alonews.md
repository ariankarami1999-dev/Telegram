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
<img src="https://cdn4.telesco.pe/file/jW8HgcMaa6S0DbXrCVgQtF4GWovb6N9K4yTh2LyIHiukXoU8HuQ4r-27uq988k649K0mJx6w_GaM1u-Lcau_9aTKr0IJJ9UGJfi-MVDdo0l-r8bS3YFG_je8Rm3wfKnIiRTTYUL_Lkncg0SfNX49vwYDJ2pwzVG6OjK2ynDqBr8t_m9OCic-66W0-gYi0AFyTyBX_VS8Lx_XxDEiQm_Qs-3kAbRwtiYF0mpeAvQSagsfTmjeGXUYjNlrvSkFFleFA8dVg0i5DqI6yy50rkqa1u3qgG1Ng5Hg0L-Dtf7znqvfnB3_zDaCpwMdlHjfhVj3Hjp-oiJNRjf6O3NtJkLxZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 973K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 15:17:21</div>
<hr>

<div class="tg-post" id="msg-142229">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کلش ریپورت: رهبران حماس در دیدار مستقیم با جرد کوشنر، فرستاده آمریکا در مصر، تعهد خود را برای خلع سلاح کامل و غیرنظامی‌سازی نوار غزه مجدداً تأیید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/alonews/142229" target="_blank">📅 15:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142228">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f72ceb115.mp4?token=ufso8jh92W77f1ouv96_S2dt25sKy-1_qMf32ZYgFP0Jn_8EoyDVDno8CiwiEHoefxEyIrfEOrZt3nyhiSfsv_1IfMt1YWUveppXua-zmaJmwuy_z5dWsW0WK-bMDb24bwd00rvrxjKIIBsA_lkflRPBmecCev3h41GHO4KqmOw1WsrchpWidhds_Z2wZS64scYC8rrs7B4dIe7-XV4NTDB05FlMsFM2JGBUuUBKr4gNoim947iHmgYrvEjVjygGit9LUVHn8bmfYpvD4v_4zDYFSkUDAlEAerhVmPtxecgMDS6m-86gPZagdfn2hTe_ebkQSOPQxKcNoaHH4Mlz4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f72ceb115.mp4?token=ufso8jh92W77f1ouv96_S2dt25sKy-1_qMf32ZYgFP0Jn_8EoyDVDno8CiwiEHoefxEyIrfEOrZt3nyhiSfsv_1IfMt1YWUveppXua-zmaJmwuy_z5dWsW0WK-bMDb24bwd00rvrxjKIIBsA_lkflRPBmecCev3h41GHO4KqmOw1WsrchpWidhds_Z2wZS64scYC8rrs7B4dIe7-XV4NTDB05FlMsFM2JGBUuUBKr4gNoim947iHmgYrvEjVjygGit9LUVHn8bmfYpvD4v_4zDYFSkUDAlEAerhVmPtxecgMDS6m-86gPZagdfn2hTe_ebkQSOPQxKcNoaHH4Mlz4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: به نظر من، مناسب‌ترین کار این است که من از دخالت در انتخابات اسرائیل خودداری کنم، اما ممکن است از یکی از نامزدها حمایت کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/142228" target="_blank">📅 14:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142227">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aea77c36c6.mp4?token=QOVDUkr9wVUubsEwvJgKBR1EzjR6owDRUn8UbvjD1ONWOYgwG9rD8GwMJ9JxhZWt7LKZ7ZryrBvrSNEEUjfBjiPiRliUSRLCbOM3mqG0BTLdrSC4UvS2rXsIdRkPBS3Wo58ajhGB3Fwe2_5Zz8-cPNjWDl9h4eE23FFAWWYzYrF-McBuDmtmfylg0VED9FGqG38AG7xWPMljiwABX2-rv-gny90SjMWTPD5RJaXZo_54Q4edPdMkGA_UbFAG02AhZ9bdtxLrpU0kFnT-uIzr-l8UkPHuItMU9NkXnMsvgrnQ_NuMbCY--LZKowoa3X-xjJqcMFPFcikXMWE-HDcv3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aea77c36c6.mp4?token=QOVDUkr9wVUubsEwvJgKBR1EzjR6owDRUn8UbvjD1ONWOYgwG9rD8GwMJ9JxhZWt7LKZ7ZryrBvrSNEEUjfBjiPiRliUSRLCbOM3mqG0BTLdrSC4UvS2rXsIdRkPBS3Wo58ajhGB3Fwe2_5Zz8-cPNjWDl9h4eE23FFAWWYzYrF-McBuDmtmfylg0VED9FGqG38AG7xWPMljiwABX2-rv-gny90SjMWTPD5RJaXZo_54Q4edPdMkGA_UbFAG02AhZ9bdtxLrpU0kFnT-uIzr-l8UkPHuItMU9NkXnMsvgrnQ_NuMbCY--LZKowoa3X-xjJqcMFPFcikXMWE-HDcv3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد حماس: ما یک کانال ارتباطی متفاوت با حماس داریم و در نهایت آن‌ها سلاح‌های خود را زمین می‌گذارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/142227" target="_blank">📅 14:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142226">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ : اسرائیلی‌ها نباید در غزه حمله کنند، زیرا حماس موافقت کرده است که سلاح‌های خود را زمین بگذارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/142226" target="_blank">📅 14:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142225">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9189453b.mp4?token=gRWY6Z_K1ddPuR6GcxcOsbeinuWmoaWkOAzmujK1IRtlxVsooGky4kIgAQDSMHwrrhFM3JAWitHF8hwjdpjz_1SMnEJflyC7z5MpctvbjO4r35ZoBLrdHlDECnHmg30r665U4ZjdNMGxYrZva9rkYRssMJ0gYyt2r0-eY7XltVDGII8DrYiJ-wI1tBeLY7EBb6N69Q1HBcfBIvxePZU-46dTzO5ByMY-sRPpXd5vMjfBhTX8miPKQ9gYAitc4P9KdwkGbrrvCHYqrFBpWwCGw1SwBvta9tuWmI668K4V2l5Gc4JDDBr6Ouxq4x7F99QhWdtQ-aqcuqX2kZcURllJsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9189453b.mp4?token=gRWY6Z_K1ddPuR6GcxcOsbeinuWmoaWkOAzmujK1IRtlxVsooGky4kIgAQDSMHwrrhFM3JAWitHF8hwjdpjz_1SMnEJflyC7z5MpctvbjO4r35ZoBLrdHlDECnHmg30r665U4ZjdNMGxYrZva9rkYRssMJ0gYyt2r0-eY7XltVDGII8DrYiJ-wI1tBeLY7EBb6N69Q1HBcfBIvxePZU-46dTzO5ByMY-sRPpXd5vMjfBhTX8miPKQ9gYAitc4P9KdwkGbrrvCHYqrFBpWwCGw1SwBvta9tuWmI668K4V2l5Gc4JDDBr6Ouxq4x7F99QhWdtQ-aqcuqX2kZcURllJsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما یک کانال ارتباطی مخفی با سپاه پاسداران داریم
🔴
ما مستقیماً با مقامات سپاه پاسداران در ایران در ارتباط هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/142225" target="_blank">📅 14:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142224">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ: ایران باید پرچم سفید تسلیم را بالا ببرد
🔴
آنها در بازی پوکر خوب هستند، اما در حال نابودی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/142224" target="_blank">📅 14:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142223">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95373bc7de.mp4?token=MKZ1NF4prJhJESCfVzgY8mEEcVq4LFJImLqZ1vFNoPpJW86z31F8pVxcywD8EyfMVD6vlQCCxvnct4hLC9b3gAC-k5JqULOxpOvNOLo3cq1_YBjCqYL8Hok09rdo_XxYzpwB5v3_NEBPsCgoO0ZTT0qrEuUcX99fgvZdbTf8eX-bZ8gKHGEF882kmmPHUpwKYcDNy3HVBUb-ed66dSen3MbYEaBt_bikvsT0hBGgjZ8XOc7j7N9zj94CbkpcOWh_WIoFd8B-mhqVzCvb_p3R4erkqcS5dBqn-LTX_L8xRgJ8av_hwwF5KaSbHbfE-w51ZBPrNzMd5Gh6r28U2pEh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95373bc7de.mp4?token=MKZ1NF4prJhJESCfVzgY8mEEcVq4LFJImLqZ1vFNoPpJW86z31F8pVxcywD8EyfMVD6vlQCCxvnct4hLC9b3gAC-k5JqULOxpOvNOLo3cq1_YBjCqYL8Hok09rdo_XxYzpwB5v3_NEBPsCgoO0ZTT0qrEuUcX99fgvZdbTf8eX-bZ8gKHGEF882kmmPHUpwKYcDNy3HVBUb-ed66dSen3MbYEaBt_bikvsT0hBGgjZ8XOc7j7N9zj94CbkpcOWh_WIoFd8B-mhqVzCvb_p3R4erkqcS5dBqn-LTX_L8xRgJ8av_hwwF5KaSbHbfE-w51ZBPrNzMd5Gh6r28U2pEh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آنچه تاکنون از آن (مهمات) استفاده کرده‌ایم، در مقایسه با کل ظرفیت، بسیار ناچیز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/142223" target="_blank">📅 14:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142222">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / ترامپ: اگر عمان سر راه ما قرار بگیرد، آن‌ها را حسابی بمباران خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/142222" target="_blank">📅 14:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142221">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
الحدث» به نقل از منابع آگاه: گزارش‌هایی درباره موافقت با تمدید مهلت ۶۰ روزه آتش‌بس میان ایران و آمریکا وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/142221" target="_blank">📅 14:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142220">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abT_h91lcY9v7c4gzY48Lxyn8ORn9iNkLT1Yi_thkcWjPPNr693LO6MoQX87uhk0bRnFQ4nRRWlshdW1NcBGIiM0MiKp44g2m0Pw1ubF6qzhhT8ThdAAH8OUW4owXaqpQv3tUBym1IkgXIcsS7UFAbvON9P06_LiKALhB929EmOBm6L_8w7JmreP39nE9c6cGo3PdZexNzbtWWe6q5upCI6SJ0wg9v5mubrHXaUW9xNK7lwN2trY8qZjzRID_AhU4M0_s-VFoyxa92GAtOTzuWrnaOAZXct2FSJtydMZD6k-7jSr68j4dn2ljsR4WZygTYZ8iET1fUe9twaYs_32lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیرکل انجمن کشتیرانی و خدمات وابسته به ایران: منشا آلودگی نفتی سواحل جزیره قشم برای ما مشخص نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/142220" target="_blank">📅 14:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142219">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پلیس راهور فراجا: حتی یک خودروی تولید داخل در مرکز آزمون تصادف تست نشده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/142219" target="_blank">📅 14:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142218">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0a5896144.mp4?token=IuVKOAmyKzLbSUBDvlH1iTUfHXBDPz-2glF1f1WjAI0JSzjWzbzOjEmIxCSdaQ-Dxv3TJBu3JUKISGd4KwKdeEUbW4bZlv_e9625ccIOhpFFo53HEkP737K_gSRlyuk9JGUQTsAjF5dB2hlbFiJsGNTP22i-o8ulEj9PsaiDg68xBxeFdKsq5N2vM2ibWR4pkE0BrWhcFbfExutBL996FaRYm1G_JBo8XZKn3hz9AVEMQCrwhjiWyjOKDKYWuM3SYF-Xz4JOL5zX6cjhAig6Gj2oDKCVq4Kj9vVV4lZ2euqYsd8V2-poYPmw0zxvHYjGZJJh8IP-UWQcRYNYTkVN9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0a5896144.mp4?token=IuVKOAmyKzLbSUBDvlH1iTUfHXBDPz-2glF1f1WjAI0JSzjWzbzOjEmIxCSdaQ-Dxv3TJBu3JUKISGd4KwKdeEUbW4bZlv_e9625ccIOhpFFo53HEkP737K_gSRlyuk9JGUQTsAjF5dB2hlbFiJsGNTP22i-o8ulEj9PsaiDg68xBxeFdKsq5N2vM2ibWR4pkE0BrWhcFbfExutBL996FaRYm1G_JBo8XZKn3hz9AVEMQCrwhjiWyjOKDKYWuM3SYF-Xz4JOL5zX6cjhAig6Gj2oDKCVq4Kj9vVV4lZ2euqYsd8V2-poYPmw0zxvHYjGZJJh8IP-UWQcRYNYTkVN9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حمله هوایی اسرائیل به شهر المنصوری، در جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142218" target="_blank">📅 14:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142217">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری/ العربیه: گزارش‌ها حاکی از آن است که با تمدید دوره ۶۰ روزه بین ایران و آمریکا موافقت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142217" target="_blank">📅 14:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142216">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90cb7364d7.mp4?token=WyeBy5XyPtNi3lTB6w3PHZHUsnHzoe74d_O7jR3rPzsPtu1avwhFng6qW8okKnFOgClN6M7YgTXn8eh_kg1spib0Mezt-htxnJIV-Czj8QsAekx4cyubjblsNUQYzLRnFzoUg0ewHGAwKQC11x38PNdabbOqQINgnD5mDvBzPmMhKYgSb1wG1K4tFRcQx7DN9yoiJuOGETtNRMUe1_P9aNJmP8XUWb5AOr-ScprjoHrXZXduDx6u8WdiR3cDLpHvKYDjdWY1d0XNM9eN7ViB0KZyWcv7-UMRcuuT95WSVabhEumVsimOHuGrSAF_emUjgxOcEQ9B9PTUs2ivvgJj2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90cb7364d7.mp4?token=WyeBy5XyPtNi3lTB6w3PHZHUsnHzoe74d_O7jR3rPzsPtu1avwhFng6qW8okKnFOgClN6M7YgTXn8eh_kg1spib0Mezt-htxnJIV-Czj8QsAekx4cyubjblsNUQYzLRnFzoUg0ewHGAwKQC11x38PNdabbOqQINgnD5mDvBzPmMhKYgSb1wG1K4tFRcQx7DN9yoiJuOGETtNRMUe1_P9aNJmP8XUWb5AOr-ScprjoHrXZXduDx6u8WdiR3cDLpHvKYDjdWY1d0XNM9eN7ViB0KZyWcv7-UMRcuuT95WSVabhEumVsimOHuGrSAF_emUjgxOcEQ9B9PTUs2ivvgJj2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی اتوبان بابایی تهران، یه پسر جوون داشت با پشت پژو پارس سرعت میرفت، که این شکلی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142216" target="_blank">📅 14:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142215">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSL7m6J4OYmenOw135ju0xO2YRzbAeHfl0Al37LAafSQCF-4VY0tR6BgStklciSN6iCILXXqPOTXf0_9BURHAe0L1W8KXvFMHcK9eZXYFnFnqB16nXGYeOyyZHZPwmRL03jTRGIb2oMaK6YbL_euLs3L_qXFwHUFgSKuhV4WFW7pxFm2AsRw7VL_bjbptU1lNCJxG9x3Ylxogn92uA-hOVmEkdXhG_E2VdGfEJJ-2qMp2idFthX-Ty9kR3BTZikKVZuWiPMXnORVX8ZRHRBSIowHdL4Z41S-2yh0IR6fFUF82DssIfVd-dbJ5chwBq8QySAaxytSRSZ-5fLvGPRL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ هم اکنون: هدف اول این هست و خواهد بود که ایران به هیچ راه و شکل و فرمی به سلاح هسته‌ای نداشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142215" target="_blank">📅 13:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142211">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIiyhvLpMErpSco13ZSiOw4e73RWz2LtB25qs-vBqH8iGrgtuTG9q0eICM7huvkoSxSfUuVCk0cUeBRLStXj_5_X5S8_WI6G4bHN08W-A5g_BsLrXCuBnh9YDzQdjmteLRfZdd5-toYMPc7QVTdQxEfCJ7GP_OGEfUVoX7tknAR8LU0niEb2MYIRuMpGQuVid0m60ycGGgZO_2q5r-nhywn-zXhr1NHI2mU8CPY6FYJmQ3yHtfzNc5z1VhQj4C3ze2EXx8rQ5ZtsyYRBPMrkYECidKs__M2X11ubd8x4vzI61iBF-Eas4qLvqj6RIMdI3z2XPsMqeL_ZQYF8ltn_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lmpiqvSZnj1BV3OVXCi1RdNe6E82aj4BzhTJ9Xrgpk9bG-4qGhOla-FngINookNwDMrkp-4HpKCG8Ymo3RC5CxXoTQo9u5uBFDIUkvGpHpycQ4xtZtW13NNg63yoIP0SfAsEqqAysXpYM9EIoMQzeuW1haSuHG8fxeTqT3SaSDDD69LJa1oD2v88VDzW-dhQFPInKkfmenP6XFHasjTBwqmqg53z3uUZvN8ZXe7VnBoPGSQW0B4BVM5pyBrybawSk43ZgbJIITThTZ6iGW-_MDmo49H1ayRHALdciSTioyK8BvTmeGgF6q9HzvsvifuIBI8vLXZsJ_F0j-JGM3hLMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f157f1c6c4.mp4?token=SDZQJWDt3pukY6mWy7Z1x6ekTXwGeAvm1mKTtXoDSNhyBVPALPGTFIx7j8vHlYeLl9qotspsSWRgiugNNJRLJXJHkG8SzWSWTpOdxw_TJ6vCBqnTa_E9jMJP-FUzhLVCMRA7x0L00BuwPki69Tm8VCKZdalzkgt71I7FhysFMJO4bVAIv-tevWnP3IXC5lwfHN-VJnDMBCskDcYakvartWCqWZGhVCwClCKJSJUXdNE5SMpdgHtrMCfgZ7Dj6LpONeG-0Zj6s9BPgYZPmKC0fBXJVsh9SkiNVE5HE2HRsw2JqBxUDyUdq85ZZ4wECLx2Z8iHLNBRf98nUq12FlFgjU4cqeJYOXxxn24qO6hAKDc0d0O6tGU3-PBG1aFqEM5uVeuT4cpS5MSD3gBYbXuR_V0mRo8GFUwSABZ_4xr9zi5ucNbFcZp20mKZgVXe5oweBoL1Lp8QQluie3yu1d9w_nI6db5lWr4jvZ5nS1tXAatHGttE5Q4cfDnZroBSxlCaFi59HSGspa1aiW1kyZ8mgGy1WNfG7bEgdUJdevhuMZyj530RIel8CnbysDlAAAQ1m5F9szv3Hcsy0hLuoopQjWuxGdJtM9TGIQAOeEGi8wsUghRZcngAd9dEVy01h8BD4CdmlMGje6vlMxr9Cq5b-sBKIPzoWZTctD4Mtxfhrds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f157f1c6c4.mp4?token=SDZQJWDt3pukY6mWy7Z1x6ekTXwGeAvm1mKTtXoDSNhyBVPALPGTFIx7j8vHlYeLl9qotspsSWRgiugNNJRLJXJHkG8SzWSWTpOdxw_TJ6vCBqnTa_E9jMJP-FUzhLVCMRA7x0L00BuwPki69Tm8VCKZdalzkgt71I7FhysFMJO4bVAIv-tevWnP3IXC5lwfHN-VJnDMBCskDcYakvartWCqWZGhVCwClCKJSJUXdNE5SMpdgHtrMCfgZ7Dj6LpONeG-0Zj6s9BPgYZPmKC0fBXJVsh9SkiNVE5HE2HRsw2JqBxUDyUdq85ZZ4wECLx2Z8iHLNBRf98nUq12FlFgjU4cqeJYOXxxn24qO6hAKDc0d0O6tGU3-PBG1aFqEM5uVeuT4cpS5MSD3gBYbXuR_V0mRo8GFUwSABZ_4xr9zi5ucNbFcZp20mKZgVXe5oweBoL1Lp8QQluie3yu1d9w_nI6db5lWr4jvZ5nS1tXAatHGttE5Q4cfDnZroBSxlCaFi59HSGspa1aiW1kyZ8mgGy1WNfG7bEgdUJdevhuMZyj530RIel8CnbysDlAAAQ1m5F9szv3Hcsy0hLuoopQjWuxGdJtM9TGIQAOeEGi8wsUghRZcngAd9dEVy01h8BD4CdmlMGje6vlMxr9Cq5b-sBKIPzoWZTctD4Mtxfhrds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جمعه خان فاتح، فرمانده شورشیان طالبان و نیروهایش پس از رسیدن نیروهای کمکی به منطقه بندخسان، تسلیم نیروهای ارتش افغانستان به رهبری طالبان شدند.
🔴
پس از تسلیم شدن، فاتح با یک هلیکوپتر دولتی در مسیر کابل اسکورت شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142211" target="_blank">📅 13:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142210">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سپاه اصفهان:احتمال شنیدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142210" target="_blank">📅 13:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142209">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
بی‌بی‌سی: یک کشتی کانتینربر چینی با اجتناب از کشتیرانی در آب‌های خاورمیانه، از مسیری تازه به مقصد اروپا در حرکت است
🔴
کشتی مذکور از مسیر قطب شمال عبور به اروپا می‌رسد و بدین ترتیب خاورمیانه را دور می‌زند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142209" target="_blank">📅 13:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142208">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت خارجه : مذاکرات با عمان همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142208" target="_blank">📅 13:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142207">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رسانه‌های یمنی همسو با عربستان سعودی:حوثی‌ها یک کشتی را در تنگه باب‌المندب هدف قرار دادند و مالک آن فردی به نام "امیر خان" است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142207" target="_blank">📅 13:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142206">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزیر جهادکشاورزی: ۸.۲ میلیون تن گندم از کشاورزان خریداری شده و امسال وضعیت تولید خوب است
🔴
همچنین از مجموع ۴۰۰ همت طلب گندمکاران، ۲۱۸.۵ همت پرداخت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142206" target="_blank">📅 12:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142205">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNRmsHa_HRMExSpQdIDgVyOsnaFh9GUQl3wn8OMdaXbLswtgbqAKVy_3wAQGe7JJijZWlF36Bi-a735Aj0ltsvs32zJbw41Q2BbtsvTVPQtoP2XXkB8NfKtOzAAW1q9HavWO6MBvdiBL0oDiEMORlzKtQB27KFu6tgpM14ZFUcdxYDgDX75pYsrPZH_Trx7fVKDK3E9lXu91peyI2_xp-TKHDPaD0x_n_53l7m4L7KgKRD3HL1cHh_hzV9LVKJxu6T-f809gpmE7O1VzEF4o62393_DvOfwZOON5jvxbW9fNZw4TaPyX0kAnDNI-SzDnUwi5qWd_QyKrFnqsSCZifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار حوادث : ملیکا همت زاده دختر ۱۳ ساله اهل روستای دسک تو سیستان و بلوچستان عقرب نیشش میزنه بعد میبرنش بیمارستان تو بیمارستان ۷ ساعت منتظر پادزهر میمونن اما به دلیل نبود امکانات تشنج میکنه و جونشو از دست میده...
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142205" target="_blank">📅 12:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142204">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
باشگاه استقلال اعلام کرد که استان بصره عراق را برای میزبانی مسابقات لیگ قهرمانان آسیا انتخاب کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142204" target="_blank">📅 12:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142203">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99f102f9aa.mp4?token=DVCa2yalEr-6JG8EJViUsazgadk3bVDh09bIq8p1fAuvjV7CWjENUb34oXSszTHZDeZTBdvhamDh5QVexsR68BPEsTOGkg4ujXuuopJ0S5Nqs3Av5TMfYWOSpATQhHEsgD5H-P1zDjydXZHy0udJXyJ5q26PgR_iCq6Ldazu3SlciDuS08bRfz3lOMma_rIJeUH2o_KHYVA7aPcKFZY0DYpOxA63LgNGrSj80y2DZlrhFcbZvCyMAQoMBdoP6f_zDqBwDFc4s19TmToFrSzDetI-ofqgrRKc-EiKDvoxEZAKoz8QXOCh5jLHoZ8YQR2U65nGzqAljD-Q2MtMB7zJNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99f102f9aa.mp4?token=DVCa2yalEr-6JG8EJViUsazgadk3bVDh09bIq8p1fAuvjV7CWjENUb34oXSszTHZDeZTBdvhamDh5QVexsR68BPEsTOGkg4ujXuuopJ0S5Nqs3Av5TMfYWOSpATQhHEsgD5H-P1zDjydXZHy0udJXyJ5q26PgR_iCq6Ldazu3SlciDuS08bRfz3lOMma_rIJeUH2o_KHYVA7aPcKFZY0DYpOxA63LgNGrSj80y2DZlrhFcbZvCyMAQoMBdoP6f_zDqBwDFc4s19TmToFrSzDetI-ofqgrRKc-EiKDvoxEZAKoz8QXOCh5jLHoZ8YQR2U65nGzqAljD-Q2MtMB7zJNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خودروهای نظامی اسرائیلی در حال پیشروی به شهر بنی حیان در جنوب لبنان مشاهده شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142203" target="_blank">📅 12:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142202">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزارت خارجه : تلاش‌های میانجی‌گران پاکستان و قطر، برای کاهش تنش ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142202" target="_blank">📅 12:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142201">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه در مورد سخنان جی‌دی ونس که گفته اولویت اول آمریکا اکنون کاهش قیمت سوخت است و برنامه هسته‌ای ایران در جایگاه دوم قرار می‌گیرد گفت: این نشانه تداوم سردرگمی و اثبات این واقعیت است که از ابتدا این جنگ تحمیلی هیچ مبنا و دلیلی نداشت جز ارضای مطامع یک رژیم اشغالگر در منطقه ما.
🔴
از ابتدا، دلیل آغاز این جنگ تحمیلی را مقابله با خطر قریب‌الوقوع ایران اعلام کردند؛ خطری که بلافاصله از طرف پنتاگون رد شد و اعلام کردند که چنین چیزی اساساً وجود ندارد. در مقطعی اشاره کردند به خطر بمب هسته‌ای ایران؛ بمبی که ۳۰ سال است در مورد آن صحبت می‌کنند؛ یک دروغ بزرگ.
🔴
خود را در یک باتلاقی گیر انداختند و الان برای توجیه شکست‌ها مجبور می‌شوند که هر بار اهدافشان را تغییر بدهند یا اهداف جدیدی را تعریف کنند.
🔴
الان دغدغه‌ آنها بازگشایی تنگه‌ای است که اساساً قبل از ۹ اسفند باز بود و تجاوز نظامی آنها باعث شد که منطقه ما گرفتار این ناامنی بشود و جهان از تبعات این وضعیت آسیب ببیند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142201" target="_blank">📅 12:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142199">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/niJYc3iPJSNF-alcwcwmFhOWJLNSQAJWSf9UXCQfWK_oiDTDo01Cuw3oyUnUJqllG6viFqwRaK3FfMquWnOGHxYtkBbc1ZJfPTo1gOvVFMb1ZaS0Qgsv_x_EakMk4j_j4gBDkG7EWq7lCyr7qObLfzyucPSRnPBMqvwIo75khWyABnqsbudKbm1wq6vQqRYuQx81LMmb95vi9xCg4s8VZ3dwzT1OD9EG98QC1ztG57WGcXnXi-HLHChpULZPptYzw7lkt_10kyKTDP3tldx600a7bm2MmONp_k0foHkTPy0L2Wp1Es6X9cDJaTtU3JSkqCYKmo0zqJ0DQIhmmNjh6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xb9BPSggW_u1aqhtLeV2uwPi4Eo71ALdOPNPb_fMk6Tm2vU_eJQjf5-CG5dTsbsROccO-q0VEHJHm_3SyJ4wx8WUUnZYzDWpMTkFX1E-NIE6PGK5rrAJ43Hx_TCBS13NRMNYPKa4aIkf4fXvD9Vh3JsJwd3h9Shl2XmisKdNDdybFbZhDHM3ahD6zXt-X0RmPmC_-eTyuUhlrqK6934lWqUTetJaiUOSMBj7GpeOxgUmRo8BVcoRwe92vnIPB6H50n40GUjHIM_9R-hS_XKqo4eFWKbS-NnEtpxueyIqLmNjfk33kBE-yW520TYkpzFg3_rElta7OvPydJSC0s26Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
"قلعه" دکتر مصطفی حمزه  نیروی حزب‌الله در روستای رمان، واقع در تپه‌ای روبروی رشته‌کوه علی‌الطاهر - قبل و بعد از حمله اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142199" target="_blank">📅 12:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142198">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
5 موشک بالستیک به سمت کشتی‌هایی که در تنگه باب‌المندب شلیک شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142198" target="_blank">📅 12:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142197">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ewgmp2-F6XzP13s1VYKnutts_5vR0tKXe_o4Jqyqx-ookA43c4IwEogUgzBhVw7ZIRmqDs2OKdCuk5Vi6Kq0gZ3yOMK4SxbOtMCNi5MenwTs6XYczp4zwf7cZ3ojhcC3Ope6XEJmXNrhQfCAI8EB90thxYOGOz7FVh9UbBOGX5nksgBOGenI-2maXhdtb5Tzux4wa4FN3E5fBS4HlDLHM0hftXaPyw_tXiaCXIeqUb5v9TDyQRmKc9NLgi3k6V3z2MOrkUuM4Zo0-lvS_M4agr05hDCPxql4LnPj68yOjYsIQV4L2yTALbhgD-D25Mg9FIvwjBCpuP0AuXFkgP_vWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / وقوع چندین انفجار شدید در نزدیکی دفتر مسرور بارزانی در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142197" target="_blank">📅 12:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142196">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
چمران: انبار نفت شهران نباید در این محل باشد و پیگیری‌ها برای انتقال آن به خارج از شهر ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/142196" target="_blank">📅 12:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142195">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه درباره ادعای یک رسانه آمریکایی مبنی بر ارتباط غیررسمی واشنگتن با سپاه پاسداران از طریق اقلیم کردستان عراق جهت اطمینان از حمایت نیروهای مسلح از روند مذاکرات، و صحت‌وسقم خبر برگزاری نشست محرمانه میان ایران و آمریکا در اربیل:
🔴
خبر برگزاری نشست محرمانه میان ایران و آمریکا در اربیل کاملاً ساختگی است.
🔴
خبری که اشاره شد از شگردهای رسانه‌ای و عملیات روانی برای ایجاد اختلاف میان ارکان تصمیم‌گیری در جمهوری اسلامی ایران است و تردید نکنید که چنین رفتارهایی از روی استیصال انجام می‌شود.
🔴
انسجام و همدلی میان بخش‌های ذی‌صلاح در جمهوری اسلامی ایران در ارتباط با موضوع صلح و جنگ بی‌سابقه است.
🔴
هیئت مذاکره‌کننده الحمدالله مورد اعتماد کامل همه ارکان نظام، از جمله بخش‌های دفاعی کشور قرار دارد و از این بابت خدا را شاکریم.
🔴
قطعاً هر تصمیمی که اتخاذ شود، از جمله در رابطه با مذاکره و گفتگو، حتماً با لحاظ دیدگاه‌ها و ملاحظات تمامی بخش‌های نظام صورت می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142195" target="_blank">📅 12:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142194">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / وقوع چندین انفجار شدید در نزدیکی دفتر مسرور بارزانی در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142194" target="_blank">📅 11:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142193">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffbdcb628a.mp4?token=VZdVKF1DRjNh8GG6OQQ4BGPO3U1vuKz0RE0qB3iEoBYf5vlpRy9IS-ESPTHssyFn10ygyt1mxmIn5tVXTipatWzuXYLSYRWpP66udgZFu2Hod4kmN_FwdEzUsh-8U_M_DG-8gBOvoISVlFVTIofLRZjg_qbJ1fX0-w3-hYcSIAq_G5Fj5LEYBdixMgFfQRxIz3yrQG5NxcF9RurME4Q4YyAqXAFwJivFL70yVeVHG1LuFsnCOBVYEPqHpVlGovr8KQ930r59AJh362Bb-naAK06VnyQizShMo2qygInABXETDKmUlvK6QDlG2VRqO3ShH9gx8CK149gRX2Wn6kbwQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffbdcb628a.mp4?token=VZdVKF1DRjNh8GG6OQQ4BGPO3U1vuKz0RE0qB3iEoBYf5vlpRy9IS-ESPTHssyFn10ygyt1mxmIn5tVXTipatWzuXYLSYRWpP66udgZFu2Hod4kmN_FwdEzUsh-8U_M_DG-8gBOvoISVlFVTIofLRZjg_qbJ1fX0-w3-hYcSIAq_G5Fj5LEYBdixMgFfQRxIz3yrQG5NxcF9RurME4Q4YyAqXAFwJivFL70yVeVHG1LuFsnCOBVYEPqHpVlGovr8KQ930r59AJh362Bb-naAK06VnyQizShMo2qygInABXETDKmUlvK6QDlG2VRqO3ShH9gx8CK149gRX2Wn6kbwQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: هیات مذاکره‌کننده مورد اعتماد کامل همه ارکان نظام از جمله بخش‌های دفاعی کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/142193" target="_blank">📅 11:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142192">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
بقایی: میانجی‌گری اروپا میان ایران و آمریکا صحت ندارد/ مسئله آمریکا بحث میانجی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142192" target="_blank">📅 11:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142191">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ad40293d.mp4?token=J0ETBftxjhSIgKWmUAykxMADdnUkh3kNWeq0MErUH9cAlo9IClYCPz5aZhORZ1AC_BRFD1d9Gk55mAWJ28Vlmp6h1Nh3ye58s1W3kZmRfg13y6Xs9YwgqTUx87cPijskIhXRbFbaI9qIs_1S15J4QRpH4k4ISejW9RbKBF2HIlOsARbDK0GDNLkEziyQ2BAT3KrZOdktEdKAKEpJgI3YIWh_zn2DYtqHYK1y0IfBIKp7qKpB3vpx7Z8C6PMYDRKXolmDtOyTF_oZ4E8zdPYbgL27epLadZPLgb-MCKF60wlURSr9fl1hshWoGTKnzdPH41N_rsMKkkxHaclrU_SzaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ad40293d.mp4?token=J0ETBftxjhSIgKWmUAykxMADdnUkh3kNWeq0MErUH9cAlo9IClYCPz5aZhORZ1AC_BRFD1d9Gk55mAWJ28Vlmp6h1Nh3ye58s1W3kZmRfg13y6Xs9YwgqTUx87cPijskIhXRbFbaI9qIs_1S15J4QRpH4k4ISejW9RbKBF2HIlOsARbDK0GDNLkEziyQ2BAT3KrZOdktEdKAKEpJgI3YIWh_zn2DYtqHYK1y0IfBIKp7qKpB3vpx7Z8C6PMYDRKXolmDtOyTF_oZ4E8zdPYbgL27epLadZPLgb-MCKF60wlURSr9fl1hshWoGTKnzdPH41N_rsMKkkxHaclrU_SzaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: تحریم‌های آمریکا هیچ تاثیری بر موضع ایران نخواهد داشت جز انباشت کینه و دشمنی بین دو طرف
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142191" target="_blank">📅 11:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142190">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر کشاورزی: قیمت اغلب کالاهای اساسی و مواد غذایی نسبت به هفتهٔ گذشته و نسبت به ماه گذشته رو به پایین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142190" target="_blank">📅 11:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142189">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a019ec7.mp4?token=vZbunRb4kThuaARHWGZ6jvvgWI5Fjb-_K6xL-h8RZST7zS34m6tRHIXeTRc64-a5rUkJWMa4WgXPFNWAlDUerntKHcgNflrI1vxXDuskGw1mJEyII93YZgc6p1m0fAY0get2DaeC5UnLhm_iapoCsutkSbWODTBJCEm1B5_h58pQO6olpbchK0F7Pnu1jVHgeCEjVT5vAypD1J5Fr2oofb3Wje6qfYRMpWTXaHWbeU9hB0y1WoPeon2WLpOo_UGu8faIv8gU2iN_V0JctwZKnCHOWrXiLd2wyYqsD8rAqe5LmpPIHK8emvrfSZv6zq5_3aYcEEZlmlBMmpveQK_HfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a019ec7.mp4?token=vZbunRb4kThuaARHWGZ6jvvgWI5Fjb-_K6xL-h8RZST7zS34m6tRHIXeTRc64-a5rUkJWMa4WgXPFNWAlDUerntKHcgNflrI1vxXDuskGw1mJEyII93YZgc6p1m0fAY0get2DaeC5UnLhm_iapoCsutkSbWODTBJCEm1B5_h58pQO6olpbchK0F7Pnu1jVHgeCEjVT5vAypD1J5Fr2oofb3Wje6qfYRMpWTXaHWbeU9hB0y1WoPeon2WLpOo_UGu8faIv8gU2iN_V0JctwZKnCHOWrXiLd2wyYqsD8rAqe5LmpPIHK8emvrfSZv6zq5_3aYcEEZlmlBMmpveQK_HfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تا زمانی که وضعیت خلبان‌های ما در قطر مشخص نشود، ما آن‌ها را اسیر می‌دانیم
🔴
ما از ۱۱ اسفند پیگیر سرنوشت این خلبان‌های شجاع هستیم و از ۲۵ اسفند با صلیب‌سرخ هم مکاتبه کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142189" target="_blank">📅 11:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142188">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه : تفاهم‌نامه‌ای که با طرف آمریکایی امضا کردیم، هیچ مهلت ۶۰ روزه‌ای را تعیین نکرده است.  آمریکا چند هفته پس از امضای تفاهم‌نامه، مفاد آن را نقض کرد.
🔴
گفتگوها با عمان به دلیل پیچیدگی موضوع، دخالت بازیگران متعدد و کشورهایی که به دنبال تضعیف این روند هستند، مدت زیادی است که به تعویق افتاده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142188" target="_blank">📅 11:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142187">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: نامه ای با منشاء وزارت امور خارجه خطاب به مجلس برای مسکوت گذاشتن طرح اعمال مدیریت ایران بر تنگه هرمز وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142187" target="_blank">📅 11:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142186">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏
👈
وال استریت ژورنال به نقل از مقامات ارشد ایرانی و عرب:
ایران در حال آماده کردن نیرو های نیابتی خود در سراسر منطقه برای گسترش قریب‌الوقوع جنگ می‌باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142186" target="_blank">📅 11:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142185">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7902ce9fb9.mp4?token=WzQb1M2ThiBgFfqTl9Eyfo71fSUHKeLUR_qZQvL1NujVyn7_ceznsDTYc-iD0Vi7FPxO0qG9qSpvKEwR_9k4QKzUOd1G06Ukblt0yNcb2zL7jOWCJUvnuTpW_pvo8LlG_R1AgFS6v-Tswzppj13e5FyPl3VobjhtWb84GC87ZsVydH3salrKQkyab4mrzQitC0i8raUH9bSWsiGeqvW6GYTK0Cmn6RfAS-giSayijI62yRS2T-UDMBLejN4JlyRwEHM2COrCmvZ9BBQpYguBoB0S4hgW_cUQQnzuShXrLejOu78JDDG54N-mIyiWwmOH6i0vFypDZq9IhVTKEtKWKLeFVeavgAHNq1xQGBESwf9PXpCdNJ2A3Ho_o80uUcS49QP3UtX8jkWaL9jW5ERJPnBdZarQRDTYlx4qLBvNchWhBDmMIQaCe3l4zv1ytfH5uFCdWezFGTe4ZaXjW_mGeFM77RSuIvQGJGT6r0BmRSNEdJOCrFT1q_dgPCtpBPElqq6T1ieOgTLYo148WH3PiQfDrlw_ueDYPcbX5HJwcqThg4oEnLsLyYoeuYQVyqXDbvhAAiRpIhXYIsdvPJyLZzGFkooSV6DnMBtL0X5C4kKTCGdOKf5-UDvFG6XQJH8oIsDLiOw26RyO2ZNZ2SfJTqiEmpLaQV2UycfUy4mLrzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7902ce9fb9.mp4?token=WzQb1M2ThiBgFfqTl9Eyfo71fSUHKeLUR_qZQvL1NujVyn7_ceznsDTYc-iD0Vi7FPxO0qG9qSpvKEwR_9k4QKzUOd1G06Ukblt0yNcb2zL7jOWCJUvnuTpW_pvo8LlG_R1AgFS6v-Tswzppj13e5FyPl3VobjhtWb84GC87ZsVydH3salrKQkyab4mrzQitC0i8raUH9bSWsiGeqvW6GYTK0Cmn6RfAS-giSayijI62yRS2T-UDMBLejN4JlyRwEHM2COrCmvZ9BBQpYguBoB0S4hgW_cUQQnzuShXrLejOu78JDDG54N-mIyiWwmOH6i0vFypDZq9IhVTKEtKWKLeFVeavgAHNq1xQGBESwf9PXpCdNJ2A3Ho_o80uUcS49QP3UtX8jkWaL9jW5ERJPnBdZarQRDTYlx4qLBvNchWhBDmMIQaCe3l4zv1ytfH5uFCdWezFGTe4ZaXjW_mGeFM77RSuIvQGJGT6r0BmRSNEdJOCrFT1q_dgPCtpBPElqq6T1ieOgTLYo148WH3PiQfDrlw_ueDYPcbX5HJwcqThg4oEnLsLyYoeuYQVyqXDbvhAAiRpIhXYIsdvPJyLZzGFkooSV6DnMBtL0X5C4kKTCGdOKf5-UDvFG6XQJH8oIsDLiOw26RyO2ZNZ2SfJTqiEmpLaQV2UycfUy4mLrzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سخنگوی وزارت خارجه: ایران وضعیت خلبانان ارتش را از مجاری دیپلماتیک پیگیری می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/142185" target="_blank">📅 11:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142184">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">با پایان آتش بس، محاصره تا کجا ادامه داره
⁉️
آیا جنگ قطعیه؟
تحلیل نوستراداموس ایرانی رو ببینید
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/142184" target="_blank">📅 11:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142183">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏
👈
آیا آمریکا به دنبال تدوین چارچوب جدیدی برای مذاکرات با ایران است؟
‏
🔴
احمد الرهید، خبرنگار الجزیره در واشنگتن، گفت آمریکا در آستانه اعلام اقدامات جدید برای تشدید تحریم‌های ایران است.
‏
🔴
به گفته او، لحن تهدیدهای نظامی واشنگتن در روزهای اخیر کاهش یافته و تمرکز بر تحریم‌های اقتصادی برای بازگرداندن تهران به مذاکرات افزایش یافته است.
‏
🔴
همچنین ادامه استقرار نیروهای آمریکایی در منطقه می‌تواند اهرم فشاری علیه ایران، به‌ویژه درباره تردد دریایی در تنگه هرمز و پرونده هسته‌ای، باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142183" target="_blank">📅 11:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142182">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74072ea52.mp4?token=ZedfxaBOVR7bc27FM6NNoS_tvOLpoPmcH4JBy6aB7qPq4jyMjIXHdFwzoXNWQO1JXqLKFAmgjTm-o2P5TTDolBrIkEymL5hZdIYlyCi2jkDVCf4JwAe-kch7xE6VOUKqzMmR3NeQ1I1OZv0uV82OB27MrAorMWpAPlYem-TPnjO2C7UVeN14DQ0jiciZZZ483EL_Um8akZ_MN-6HUeC3EH1HyNhhb8jCoOavr61YJ8UskjyALPZIN5BzeYKWJmMzygufa3t-TC0TNTqkN6-RPVM88smJTz44zWjMTTH75uuFprsj1cfM8X29q2Z6fAmmMfkMDJoBBqWdhI3hhB5jww37TRiA34WQNm5lzrq11yRz-NXWe9oE7Aw7VvoBIjC2qNUVFWDdSwIypq3tpZA2sncZsSOZUEA5VIYR_5Evf8TYo9OQClV8jzu9gjxC8dkQ6Fs-CwWifUff3aJrz05VL1k6L4fQYv_4IISUwb2d1ujRZC5tikovXisMuo5NMwFIxR4A_w39xqf-pDgB-2NMKwpNxlbrBGbx-CnsEdg4ZaMQWu5bIeK8CAvm1Z3yK1TGcKHeizTOZagXa5JUAG8_rsnx1yCTfpwgTPDchEm1lQiVe6oyJzTZPUhn_5Chespz4sfVr0fYshYsr6Z0NyqLBK60ndtkTR4jVThz3QHgAAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74072ea52.mp4?token=ZedfxaBOVR7bc27FM6NNoS_tvOLpoPmcH4JBy6aB7qPq4jyMjIXHdFwzoXNWQO1JXqLKFAmgjTm-o2P5TTDolBrIkEymL5hZdIYlyCi2jkDVCf4JwAe-kch7xE6VOUKqzMmR3NeQ1I1OZv0uV82OB27MrAorMWpAPlYem-TPnjO2C7UVeN14DQ0jiciZZZ483EL_Um8akZ_MN-6HUeC3EH1HyNhhb8jCoOavr61YJ8UskjyALPZIN5BzeYKWJmMzygufa3t-TC0TNTqkN6-RPVM88smJTz44zWjMTTH75uuFprsj1cfM8X29q2Z6fAmmMfkMDJoBBqWdhI3hhB5jww37TRiA34WQNm5lzrq11yRz-NXWe9oE7Aw7VvoBIjC2qNUVFWDdSwIypq3tpZA2sncZsSOZUEA5VIYR_5Evf8TYo9OQClV8jzu9gjxC8dkQ6Fs-CwWifUff3aJrz05VL1k6L4fQYv_4IISUwb2d1ujRZC5tikovXisMuo5NMwFIxR4A_w39xqf-pDgB-2NMKwpNxlbrBGbx-CnsEdg4ZaMQWu5bIeK8CAvm1Z3yK1TGcKHeizTOZagXa5JUAG8_rsnx1yCTfpwgTPDchEm1lQiVe6oyJzTZPUhn_5Chespz4sfVr0fYshYsr6Z0NyqLBK60ndtkTR4jVThz3QHgAAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رقص و پارتی طرفداران جمهوری اسلامی اسلامی در کانادا در یک قایق بصورت نیمه عریان
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142182" target="_blank">📅 11:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142181">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
آلن ایر: ترامپ حتی اگر بخواهد، نمی‌تواند از جنگ با ایران کنار بکشد
🔴
آلن ایر، دیپلمات ارشد سابق آمریکا و عضو تیم مذاکره‌کننده واشنگتن در توافق هسته‌ای ۲۰۱۵، می‌گوید ترامپ در برابر ایران در موقعیتی «غیرممکن» گرفتار شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142181" target="_blank">📅 10:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142180">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
صداسیما: زمان شاه امید به زندگی ۵۰-۶۰ سال بود ولی الان شده ۸۰ سال
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142180" target="_blank">📅 10:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142179">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0bkwGv1R4mze156g_77On05XjRzK4iA9h_l29l9H_-Xs6M1fOe6uzEStbDLqFJjzoIYyfdELM-9ARZuPDm1_PZOaYhjgvdYTCOpj504LhuWvxHAtj9IIQAtcMJQDV_m_GsYRg_aD7n0eJcBRq5SBb2hyvg37x9kNwVbf5aB8u9wlJxDzPvUWmYeJ0C7o4Q-6g1DDUtsTdOF5K5UVZW3zK17ayPyll6KES7AaH3SoO3EU8aEu-V4JxvBJsbvBY0qykV8xYs35DDdiY6zKEiH1-6CxvpxdCaMm-8LED8RQ7-Sy-fd7J_b_E3VaCKR9ijNmWNY7K5ng9srZM3RipP6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏
مسافران رفتند، قطعی برق چالوس بیشتر شد!
🔴
‏۶ ساعت خاموشی برنامه‌ریزی شده در چالوس طی ۲۴ ساعت، با وجود کاهش قطعی برق در زمان تعطیلات آخر هفته و حضور مسافران در این شهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/142179" target="_blank">📅 10:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142178">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
الجزیره: ترامپ برای ناتوانی در پیروزی در جنگ علیه ایران به دنبال «مقصر» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142178" target="_blank">📅 10:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142177">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622e7971cb.mp4?token=JJAi8rAEm5gGFlJFav4BWzuR1Xia3jgEwh63WCAhVuIDffgf_wMWEUvP6nHb2k-t8tFiMO23P446hFAho0m-9_EIzCkUQafOaSJB_5QnSryYDLBXe48dM1KAdWpyttroMuHTZfLri066pXrtVuy7VHuxLB9_0BKU97PO5AT6bSrRx51apU4n9c2pGyDqwCTXof4penkmDg5X3ovaH4zkaTKgA8b_lWJW6DLRE1Awdr5RUkcZUgQn73xFJWuKFYLUw8lZXpdFfgxA1SJpjmUaEJaCdPzrhlxxylM6LRD8Dk2AJy9CR_5wqEThORiHQ9hFRQRnqANgtJmyIUuBo_uLNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622e7971cb.mp4?token=JJAi8rAEm5gGFlJFav4BWzuR1Xia3jgEwh63WCAhVuIDffgf_wMWEUvP6nHb2k-t8tFiMO23P446hFAho0m-9_EIzCkUQafOaSJB_5QnSryYDLBXe48dM1KAdWpyttroMuHTZfLri066pXrtVuy7VHuxLB9_0BKU97PO5AT6bSrRx51apU4n9c2pGyDqwCTXof4penkmDg5X3ovaH4zkaTKgA8b_lWJW6DLRE1Awdr5RUkcZUgQn73xFJWuKFYLUw8lZXpdFfgxA1SJpjmUaEJaCdPzrhlxxylM6LRD8Dk2AJy9CR_5wqEThORiHQ9hFRQRnqANgtJmyIUuBo_uLNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیویت بچه‌هایش را بیشتر از من دوست داشت
🔴
دونالد ترامپ: «متوجه شدم که کارولین لیویت بچه‌هایش را بیشتر از ترامپ دوست دارد. این موضوع خیلی نگرانم کرده...»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142177" target="_blank">📅 10:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142176">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO2u6-ua8Ohrdbe3XvohPVJNfEYGlfk97HNeUjOCupWKSB2ZrKnAKP6rQL8x98CBbRnqiFDDMXvphfW4uN0r8lRS_vKrWk8nrj7wjsKzdTYExs03WwmGhJVlq1WEXwsiLeCgWXBgBY2PDYzEw2uFztC0AkSHVxSvux4iFUA-frc_UD7KsiIkkMBVKkLpcQSajO0_Hx-it21bKtXO92TbI6e1vlvWq0m92wAmXL80mx3Me91Qw4LzeFuA7nT9gzXGz3H6ggQh3QyTfYpQxGiMHSEPC9uDPymxZCY3dAgqfFY_nfwIzSVQFuRYI-_Tq3pvVreTjPn_7UZAMwIdZCVZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری که گروه آلفا گارد جاویدان منتشر کرد و نوشتند آماده ورود به ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142176" target="_blank">📅 10:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142175">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
معاون سیاسی سپاه: تنگه هرمز زمانی باز می‌شود که آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد عمل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142175" target="_blank">📅 10:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142174">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
جروزالیم پست:اطلاعات مربوط به تردد کشتی‌ها نشان‌دهنده کاهش چشمگیری در میزان عبور کشتی‌ها از تنگه هرمز است.با وجود احتمال عبور برخی از کشتی‌ها بدون ثبت، میزان تردد همچنان بسیار کمتر از حد معمول است، در حالی که پیش از جنگ، بیش از 130 کشتی به طور روزانه از این مسیر عبور می‌کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142174" target="_blank">📅 10:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142173">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
روزنامه‌های بریتانیایی و آمریکایی:
تأثیر آشکار جنگ علیه ایران در [کاهش] توانایی آمریکا برای حفاظت از متحدان خود
🔴
ذخایر تسلیحاتی واشنگتن و متحدان آن دیگر به آسانی پاسخگوی یک جنگ طولانی یا دو درگیری هم‌زمان نیست
🔴
کشور‌های آسیایی متحد آمریکا، اکنون درباره توانایی این کشور برای دفاع از آن‌ها در صورت وقوع رویارویی با چین، پرسش‌هایی مطرح می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142173" target="_blank">📅 10:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142172">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc22d90c2.mp4?token=dJqm28LjgXUr5dhCQJ5O0cTUfNt1oYeJxM3qCBs_l4YnGD4bqvIBWCRilpRQlST-auSZ9LPKfklNCDzlE6ULAbuhY3ikQcXyighChsFAQvXoG8I5c0eSPc7aWBPgQH8u2cwd6JQoi17ya8nTYVnwb5NDX6Z164nA7b7aVeY4sSFyfdJf90ghOD8G8xDG7WDhZ5JMCZq407D-yJWv6sdnfwKUdHJHkbiLeY3mMHylwoiYeca4Fcl89YS84ksLLJmW0gmhwxd46tevy-rAZKDk6YDxJuDWnEa0iiSJJEd982UQudMa8uLGv6HeX4I38rzgPMyOsFJCjNFLgYOEkeGV7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc22d90c2.mp4?token=dJqm28LjgXUr5dhCQJ5O0cTUfNt1oYeJxM3qCBs_l4YnGD4bqvIBWCRilpRQlST-auSZ9LPKfklNCDzlE6ULAbuhY3ikQcXyighChsFAQvXoG8I5c0eSPc7aWBPgQH8u2cwd6JQoi17ya8nTYVnwb5NDX6Z164nA7b7aVeY4sSFyfdJf90ghOD8G8xDG7WDhZ5JMCZq407D-yJWv6sdnfwKUdHJHkbiLeY3mMHylwoiYeca4Fcl89YS84ksLLJmW0gmhwxd46tevy-rAZKDk6YDxJuDWnEa0iiSJJEd982UQudMa8uLGv6HeX4I38rzgPMyOsFJCjNFLgYOEkeGV7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ونزوئلا عالی بوده و ما به خوبی باهاشون همکاری می‌کنیم! ما اکنون نیز همین کار روانجام می‌دهیم - البته در مقیاس بزرگتر - اما ما در حال انجام یک کار بزرگ در مورد ایران هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142172" target="_blank">📅 10:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142171">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZhHtKnluFZmXAoSERe8eqGUY0StE_30OeNztlsFHlYjQfanX-wcTs8-FgvFY95H39jATmiriEI8ddfNR0H9DhXHmwseE-odrDEYEXhDTL-fTpC2XDufRpNv-mmSFlZrpwbLjBAjT_9B8QIOXYiGgl-4zIl83lcj6kg5n1M_YR5e6LmmH6o6a2eyhyCiamwTwXwFQk9r4F3eaSQ56KTieBOPordAkpNuyx5fcvZjqsCXk6BNMBM0KLzfJZ83x5Sch7tLm5aaNAR1jRoBTfHiO-t_5tIlCIqd97xl98W7RQerGqvFweM7HfB71-cklsragAViHSud7ZVr6BjuHgA9H1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده سابق ایالات متحده، مارگری تیلور گرین: آن‌ها در جلسات استراتژیک درباره استفاده از سلاح‌های هسته‌ای علیه ایران بحث می‌کنند.
🔴
بله، درست خواندید. این واقعیت دارد. من حدس نمی‌زنم، می‌دانم.
🔴
و این خالص شر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142171" target="_blank">📅 10:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142170">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6lWeT4uJGYvaKqAKji3UXnrHokprsUcWaTk3_pjUJ7C_byJLjxvFT2UuE69saorUBdQkzq6O__oTIy5LXxNq31RPH6fk7-ZIPqG6_z4xheBVyw99deuBjso2Fs2wuoOJNwrCs2ZvDfkhKlQwAaIf8rqtdw_2K5SEMTqBNJoy3PAZDk9Go-Ww93k1nfGEq6eqXSOVRvqd_2532z0Sq7KnS7spBCKTFY9jBHjYnG_yCgNfPTyY8wMHweUwCfdLsTIqqBka0vETg50PKR11iKgmqfKJIEoUaKZSHiUzvf2vwNErDUXZvSpJ2aB9S_dAcSpUWHbYjIEIVt20IGrgYXdmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای تانکر سوخت‌رسان آمریکایی همچنان در نزدیکی تنگه هرمز فعال هستند، اما هیچ تاییدیه ای مبنی بر عبور ایمن کشتی‌ها یا وقوع حوادث امنیتی در این تنگه وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142170" target="_blank">📅 10:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142169">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eR_2p6HQe1pkba_VgPQ8z6ofoYMke2h-iewY4StoTEnVaU5Kts4WdsxHDVexgzYbw4i8Im9HQtLxQOPNaXviM422b-ZgNxZeVE-ObuoDQnrxgxzllrLCbaWKujSymAOLL3n8UVdUsJzSBcBVnBSF-RN4zLmB0AAfVNnvAHazfmvYgdkkybSVeRgRkga02QOoXF2ng-bkw5l9bWvSU8eU-srVV3_gogbGzkgYYs9yMLcs5lbnH2Cr5fvB9YgHjt4OWamlEwTKLFMVRQo6rt7ZeBYAn2PLSjxTVh3syl4HaXlPauQXtlXYItxPpxlqJMlNFDQs5Edz0U-kfAesq5x0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دی‌وای‌اس‌جی، با استناد به مقامات ایرانی، گزارش می‌دهد که ایران در صورت از سرگیری درگیری‌ها، برنامه‌ریزی برای حملات تشدیدکننده بیشتر علیه کشورهای خلیج فارس دارد. گزینه‌ها شامل خرابکاری در کابل‌های اینترنتی در خلیج فارس، تحریک بی‌ثباتی میان شیعیان در کشورهای خلیج فارس و احتمالاً عملیات‌های زمینی علیه کویت است. دی‌وای‌اس‌جی همچنین به چندین بیانیه عمومی از سوی مقامات ایرانی که اخیراً صادر شده‌اند اشاره می‌کند که نشان می‌دهد ایران آخرین جنگ با ایالات متحده را به عنوان مقدمه‌ای برای یک رویارویی نهایی و قاطع‌تر می‌بیند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142169" target="_blank">📅 09:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142168">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYMO2CekZ_P0xFRd0e851rRCRF-vdS1F7U5bGGniJXTljggCo-G3IQtsmvjntO9Zck2pvTRMU6d0kkPUYWMBURsanE8tHacblCJvy8Xdb0wuRwBlKGkBFJkIw7FFkBZIVooakLj1BPMHmvjV4Yzi8Vr0iHmnrR804myhR3bJx8xXvWZ7VTZKiB5pyBxDQ2zAMFotW7QhM5fjWXiHye4nKOaih6lcsjvvDMWPtB9k-OkABbjVBj7mA_3kwEjdM8aGJp42u8nAbhuG7g4oVAwM1u5_qbbaWv6gL6UBGY2k3bAhbqTwlCI4nKOFAQUJ1geSpnoBA4-OICx_KzNkeItqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ همچنان به شانون بریم از شبکه فاکس حمله می‌کند و او را «شیرین‌پسند» (Milktoast) خطاب کرده و برنامه فاکس نیوز ساندی را متهم به جانبداری علیه او، جنبش MAGA و جمهوری‌خواهان می‌کند، در حالی که برنامه او و شبکه را به دلیل نمایش تصاویر قدیمی از ساخت کاخ سفید و آنچه او «نظرسنجی‌های جعلی» می‌نامد، سرزنش می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/142168" target="_blank">📅 09:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142167">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
گزارشگر
:
آیا جلسه‌ای داشتید؟
🔴
ترامپ
:
جلسات زیادی.
🔴
گزارشگر
:
جلسه‌ای درباره ایران؟ پیشرفتی؟
🔴
ترامپ
:
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/142167" target="_blank">📅 09:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142166">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwCBv26BwPHVBPjTWvpt-hriRcDONu4o8irHZ3gC1kIb4lmDYwwJYvMg-6ipIP_7kfJgc70wbsbcrFLSM445a5tXy_Shw0Z41T2-B_mE9WbJDduS7M1YaAVKqu67zClcDrbhH1mkphOtqQuenET5HnJ8Ofi0RTILDBu6yhkXkbVyTfhOmqXxe1VUnxIwAw0ntdvyO1kVYwfCW3CXtx1mQwk-nOrqKyd-54PouNNOsSq18TG793icNSAlVacQej3ai99GdIZA-bYjRASxgk5LmVN-h-Zx3eEca99pIjkBjddEXNCi-JsrrSZwPsWX-11UwSx7ioI1EH6AeAmJasVEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت، همزمان با انقضای تفاهم اسلام‌آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142166" target="_blank">📅 09:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142165">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فایننشال تایمز: جنگ علیه ایران باعث شده که شرکت‌های بزرگ خودروسازی جهان، به سمت استفاده از ترکیبات جدید روغن موتور حرکت کنند تا با کمبود شدید روغن‌های پایه و باکیفیت مقابله کنند
🔴
موجودی روغن‌هایی که برای تولید روغن موتور‌های باکیفیت استفاده می‌شود، در آمریکا و اروپا رو به اتمام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142165" target="_blank">📅 09:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142164">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCfE-_8ArKZipoZ5m8zpyGzV6eSngzgnKJ0jhjSrfSmoMOYSpzO52FuGlYbr5Z1ponXn2QpFHjKnk2-8Ul7XWrhgEzLVarf0RBiZ9bp9IHMrIt58lzZ1MgfA0O1d8wg7ma_FJbbycIkxLRfdFE4kplEs1WZqm_kXVeB86Wu2buK9XPrdoRBPSear4lzFuLd8pIr0t6PTr4qfsCtxsnGo0v69jPnpj9nJbi81a-IuxvikMlZmEr6cNuD_mRF3uajj6dti7SUKNo_LaCHAPt_5-qEb-VCqWdmnnEJWqpOJDcIj-e5XC8-INZ0YDJYjvT-EJnBCVAxvyoTeXox36c3cMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمل و نقل از طریق تنگ هرمز در آخر هفته به دلیل حملات به نفت‌کش‌ها تقریباً متوقف شد، در حالی که داده‌های Kpler نشان می‌دهد که فقط پنج کشتی کالا در روز شنبه و هیچ کشتی‌ای در روز یکشنبه عبور کردند، در مقایسه با ۳۱ کشتی در آخر هفته گذشته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142164" target="_blank">📅 09:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142163">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
هشدار هواشناسی/ گرمای ۵۰ درجه در خوزستان و بوشهر؛ رگبار در مازندران و گلستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142163" target="_blank">📅 09:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142162">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات ایرانی: ایران در صورت از سرگیری جنگ، حملات تشدیدآمیز بیشتری علیه کشورهای حاشیه خلیج فارس برنامه‌ریزی کرده است.
🔴
گزینه‌های روی میز شامل خرابکاری در کابل‌های اینترنت خلیج فارس، تحریک ناآرامی میان شیعیان کشورهای خلیج و احتمال عملیات زمینی علیه کویت است. وال استریت ژورنال همچنین به اظهارات اخیر مقامات ایرانی اشاره کرده که نشان می‌دهد ایران جنگ قبلی با آمریکا را مقدمه‌ای برای یک رویارویی نهایی و قاطع‌تر می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/142162" target="_blank">📅 08:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142161">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f073a154.mp4?token=DvSur3UPlZaT2N3gH4rF8gHB3A_jqWR2btoWLgs-_tFXan6wexiDNSA555D_A1iTm0vPadDFuqbAZgK8NXdWzhVe66WYCNkUlgikamZ_ARyxLwB_PojLO1WbD0oOfJ_Rolnvhu03IKe3eNF4C5iVjXPw54qhkYjGD7WtP-Ijlq0f1ilzX5RlTlywhrFDg3LIHfzDD88FbCPA-eGhJ-Tf2wB-iXNtRF1B_O2JzNqdzyUyFdbl9nOjJS2GRr_mIIuctqXdQ_Q7DfWhkWLxPy16gdMKLZVlQ050WSDdhGTmYIj5IHQo0toFbfiCJErWG0QoYBLzt_52OvfPFBtP-P1JeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f073a154.mp4?token=DvSur3UPlZaT2N3gH4rF8gHB3A_jqWR2btoWLgs-_tFXan6wexiDNSA555D_A1iTm0vPadDFuqbAZgK8NXdWzhVe66WYCNkUlgikamZ_ARyxLwB_PojLO1WbD0oOfJ_Rolnvhu03IKe3eNF4C5iVjXPw54qhkYjGD7WtP-Ijlq0f1ilzX5RlTlywhrFDg3LIHfzDD88FbCPA-eGhJ-Tf2wB-iXNtRF1B_O2JzNqdzyUyFdbl9nOjJS2GRr_mIIuctqXdQ_Q7DfWhkWLxPy16gdMKLZVlQ050WSDdhGTmYIj5IHQo0toFbfiCJErWG0QoYBLzt_52OvfPFBtP-P1JeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: در به در دنبال یکی میگردم مشکلات مردمو حل کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/142161" target="_blank">📅 08:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142160">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e806ec45ed.mp4?token=mVfFYWOLONtoxIpgvPr6mMk9NLxuLVTxULn7hDNn2MNc4Bnmmr7SRqYC9ev3bA0I29l--_oQ68Ij2e_6DKMbYkzL_FdIAqIHIPwbJNcTbeGYwCt4ffpV1eNczCX-1lbWIbMbZKvgrPwfRDWURkk5Ryd-pyrPa8oOjaWem_ojvmzI1NJAaJemGB3Aw7yYKYr8bJOIuzfn4xztGR-_w9K3-Z4hhVhDZlZwTf6i5902YWZKF8t0fQyrwlHIb3iGnqS2vP0Ltv0vIreDziaEQNScuVn4kUqSCzgxNNXaeVWw50csbXdHE_POtlC_PJ3B7zYTw_gQ4pUQKBYyhegDMHi-YF366UpxRKiQJ11ggGxgx--gZfFu3d-uy2tbuWbIKaZSVqBCMfq2b1l0ahjdPX0GB7_y9l9NvA_hx1JdM6-RFqiCmy9Z9_ULrFHKHsMq73Hb26S3w09W7-9laSOIqFTLkQs8v1Z3_AW9xxwKWQUMJSat8hU8TrFnWCMpKk2uTdxiNQAFfxkZ3wZTAcaKfnsh9p5kgSIGXIVZq_b2lwxqi2p3nelFeYYc4dH7i9XUhlEbuj7-6mJsVF3vymJfkIiZg_GdQL-AC0z_tljjxJwaKV4Qal9Ifh0khKzFDflQojMeUfAIecwXOhj5wWcsTT2v_t0b3Pa_7nT0NgFPqlUQZWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e806ec45ed.mp4?token=mVfFYWOLONtoxIpgvPr6mMk9NLxuLVTxULn7hDNn2MNc4Bnmmr7SRqYC9ev3bA0I29l--_oQ68Ij2e_6DKMbYkzL_FdIAqIHIPwbJNcTbeGYwCt4ffpV1eNczCX-1lbWIbMbZKvgrPwfRDWURkk5Ryd-pyrPa8oOjaWem_ojvmzI1NJAaJemGB3Aw7yYKYr8bJOIuzfn4xztGR-_w9K3-Z4hhVhDZlZwTf6i5902YWZKF8t0fQyrwlHIb3iGnqS2vP0Ltv0vIreDziaEQNScuVn4kUqSCzgxNNXaeVWw50csbXdHE_POtlC_PJ3B7zYTw_gQ4pUQKBYyhegDMHi-YF366UpxRKiQJ11ggGxgx--gZfFu3d-uy2tbuWbIKaZSVqBCMfq2b1l0ahjdPX0GB7_y9l9NvA_hx1JdM6-RFqiCmy9Z9_ULrFHKHsMq73Hb26S3w09W7-9laSOIqFTLkQs8v1Z3_AW9xxwKWQUMJSat8hU8TrFnWCMpKk2uTdxiNQAFfxkZ3wZTAcaKfnsh9p5kgSIGXIVZq_b2lwxqi2p3nelFeYYc4dH7i9XUhlEbuj7-6mJsVF3vymJfkIiZg_GdQL-AC0z_tljjxJwaKV4Qal9Ifh0khKzFDflQojMeUfAIecwXOhj5wWcsTT2v_t0b3Pa_7nT0NgFPqlUQZWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان: پیمان مکه مشابه ماده ۵ ناتو است؛ حمله به یکی، حمله به هر سه ما تلقی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/142160" target="_blank">📅 08:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142159">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT3am9ckmfpnM_7o2JhIQ2V0LGHd6EbIEcSdw2RcSkr-L5ifO0GWlaG3UFB73tZriUCj33GvtJqvUjeR1r6UECT32_j1hqZ1HNe-zXYOZYCQ_WRJvUn_wZmIzWNMgpnkgFtQw03jEZv41Y-uDjwdP74SPL5umQICZYmkSp1XRXJvS5RnSGZFjRMzgNaxrOa7_2OYHNcHNTtGYz8ALbbZH563Q4F7VreXemu5BRl1B-8vk8SIIwrkoT0xC73xaIhkCBcCU58Mk2qCLVuxfrIP9gT-8ZBkBPfim9hQDP_ixgmNHwfbXQekg387b18Tr47GXTzDUf5lc6KlP_C1TP3MZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پراید صفر فقط ۱ میلیارد و ۳۵۰ میلیون تومان
..
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/142159" target="_blank">📅 08:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142158">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzjPGq4LQspnVQPpIuqH5BmFpaXtS4IltXKgDSsh-Zj_miTBnOnpsqR5Cfae63R7gKLq_mrlpb9YEQsgKsFYdv-yiVbxJ3XMTLLF07MzVRV1fQE-lnwX79kG668kSSHqmDoZ10e_wJWB4dtcOtTilU7Bf42kjdfku_aP5qp90MTHehyzngmHjVMf2uFMsMKYV7AnmgjY0LrrFe8gikPMZZF-Le5DmhDQvan8Mbe6d3g6iIsdNGSyRaaRjMfFonlt4nEyh1zLy7NwR8wFlTGOTAvxTCVUQU-aDd-ZF2RJZuHuzmHpVwFmXtW6lOXkx-ZhZkQTJKBL_omteI8EVY_X5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ترامپ: از پاسخ منفی کره جنوبی درباره ایران ناراحت شدم/ رزمایش‌های نظامی مشترک با کره جنوبی کاهش می‌یابد
‏
🔴
دونالد ترامپ نوشت: با توجه به روابط بسیار خوبم با کیم جونگ اون، رهبر کره شمالی، از این واقعیت که ایالات متحده مدت‌ها پیش موافقت کرده است در رزمایش‌های نظامی مشترک با کره جنوبی شرکت کند، راضی نیستم. این رزمایش‌ها نه تنها پرهزینه هستند، که بخش زیادی از این هزینه‌ها توسط ایالات متحده آمریکا (طبق معمول!) پرداخت می‌شود، بلکه پیامی کاملا نامناسب و خصمانه به کشوری می‌فرستند که تا زمانی که دونالد ترامپ رئیس جمهور بوده، غیرتهدیدآمیز و محترمانه رفتار کرده است.
‏
🔴
بنابراین، و با توجه به اینکه برای لغو خیلی دیر شده است، به وزیر جنگ، پیت هگست، دستور داده‌ام که رزمایش‌های نظامی مشترک را به میزان قابل توجهی کا
هش دهد! اگرچه تا حدودی نامربوط (؟)، اما اخیرا از رئیس جمهوری کره جنوبی پرسیدم که آیا مایلند در خلع سلاح هسته‌ای جمهوری اسلامی ایران به ما بپیوندند و آنها گفتند: "نه
ممنون!" از توجه شما به این موضوع متشکرم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/142158" target="_blank">📅 08:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142157">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d98c512fcd.mp4?token=bu7Iy8OFaTkW-ZW_l9SEYjnePxkqu2SzSFZJXC9oFNBiQIann8ETsSTxM0UHSfcRSiJSI7KW2v0OqucdM7SL37Ol50p0k09s3npc1AiAVqW1NJHoCUBZOpHmnNVIXb5yhl8XX8KqW8ISdI-0UP8eHxdPALBYSXioT2Mp7-ewz2XfSt-1bH8byCdjDs2LUMzXX0oHOwlPiK1ShGItu8qLpEnfwDk5M40nmOfF_53ciKdA-eop-o45KustDrCugvKm4uFQEwz3taZObYATwLLpPra-bmVhXev19ki0fcVASPfg4ieFgw0j_Qh2h-pn9d-cncmUqd39okUdixpRWK6arQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d98c512fcd.mp4?token=bu7Iy8OFaTkW-ZW_l9SEYjnePxkqu2SzSFZJXC9oFNBiQIann8ETsSTxM0UHSfcRSiJSI7KW2v0OqucdM7SL37Ol50p0k09s3npc1AiAVqW1NJHoCUBZOpHmnNVIXb5yhl8XX8KqW8ISdI-0UP8eHxdPALBYSXioT2Mp7-ewz2XfSt-1bH8byCdjDs2LUMzXX0oHOwlPiK1ShGItu8qLpEnfwDk5M40nmOfF_53ciKdA-eop-o45KustDrCugvKm4uFQEwz3taZObYATwLLpPra-bmVhXev19ki0fcVASPfg4ieFgw0j_Qh2h-pn9d-cncmUqd39okUdixpRWK6arQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
اونا پولشون بی ارزشه، ارتششون داغونه، نیروی دریاییشون و 159 تا کشتی‌شون غرق شدن و ته دریا دارن استراحت میکنن. رادارشون و تکنولوژی‌شون از بین رفته، تورم 350 درصدی دارن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/142157" target="_blank">📅 02:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142156">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ درباره ایران:
اتفاقات خوبی خیلی زود رخ خواهد داد
. در واقع، آنها همین حالا هم رخ داده‌اند، چون یک کاری هست که ما نمی‌توانیم اجازه دهیم انجام شود: ما نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/142156" target="_blank">📅 02:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142155">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTz1lmf6tDkik03TDu2xLLZssZjVHttiBQfY6hR9Z2-fxvrhDC3Z3WFZ-lO3otHH7WHV5ipTyC0dy8s9PlqEA1uI1awyL9BULst4yYdyMeHHVl6O-Cd-PWLKeyy5PeKzU3uqbcZMtw0hGYfuYQliLgPTTm4InLUaeiMQ90xcJR7qsurpIncahMMdbR9fcPaGUBY8j5i7fYgMGrYj3YjyNAAGWaRooDuHqg7ePtRsxWccfGql54D1O5QgKSFWG_ibLTqT6sQwPqThBw3iFgFGEHYVyG53fY5Gd0H-JLHDAM8QpJJapgKnWD1RCTAXoUVFweLdUoCnFJbIdDRLKs-aZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارجوری
تیلور گرین نماینده سابق مجلس آمریکا :
استفاده از بمب اتمی علیه ایران تو جلسات ترامپ مطرح شده
این یک طرح شیطانی هست جلوش باید سریعا گرفته بشه
مطلب رو اشتباه نخوندید درست خوندید یک فاجعه در راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/142155" target="_blank">📅 01:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142154">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d47bd844.mp4?token=rL711Ix1RatPY0xX-hI9n_hvjkfSilXGU-z6bPM9flWpzT-f8_xCS69v-mUwQo3F0phIvAn1w9NxgBOa5TTcIH5N48smjWjA7M07STEvVaa7Y2Tr5XBW9VEX6Jh-laRcT9xtxHdibmuy7ViBMcdqnPB7FpJ7F8X7myoQgUTYBb7mefcWlZk-tcxJmQLmgBGHiT90DL6BuLGDFt9Y-g6dlTtYTCPgBTAbjhfqFxkpMMLHIkbUA2GHDBg7gBZ6Dqqt_zkZkd9L15QbjId7-kjghEQOjgcmMbOf-XkZqWScbneePSJzwBLM_F_ewkpwtDeoa7VyU_gq_hUpfc7-Tp0AZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d47bd844.mp4?token=rL711Ix1RatPY0xX-hI9n_hvjkfSilXGU-z6bPM9flWpzT-f8_xCS69v-mUwQo3F0phIvAn1w9NxgBOa5TTcIH5N48smjWjA7M07STEvVaa7Y2Tr5XBW9VEX6Jh-laRcT9xtxHdibmuy7ViBMcdqnPB7FpJ7F8X7myoQgUTYBb7mefcWlZk-tcxJmQLmgBGHiT90DL6BuLGDFt9Y-g6dlTtYTCPgBTAbjhfqFxkpMMLHIkbUA2GHDBg7gBZ6Dqqt_zkZkd9L15QbjId7-kjghEQOjgcmMbOf-XkZqWScbneePSJzwBLM_F_ewkpwtDeoa7VyU_gq_hUpfc7-Tp0AZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیمت‌ها رو تو سال 84 ببینید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/142154" target="_blank">📅 01:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142153">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رائفی پور: نابودی اسرائیل، تقدیر الهی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/142153" target="_blank">📅 01:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142152">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">با پایان آتش بس، محاصره تا کجا ادامه داره
⁉️
آیا جنگ قطعیه؟
تحلیل نوستراداموس ایرانی رو ببینید
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/142152" target="_blank">📅 01:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142151">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نوید محمدزاده: از فلسطین حمایت می‌کنم چون با اسرائیل حال نمی‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/142151" target="_blank">📅 00:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142150">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzi1yvyIKFY7lJ8GMFHpLruTLzYUykXrj8OBKfTPPz9bMwsTLfFpiiIIFexGf5VTOg1RX1LGf4IVYyNKEpyke2a1GOY7e8IF5MruuFEBH--E9OSv9gEMHOrk8XTHeMsW5uRsd-DBTA_8EBKS5GdDhhcwf51DkdfV-4KQXRFXQMQUwjOhmqjDaoUgFK9a5AJ5ZOfWD3musI_WFSh2cAbKVvVAk5LGno20Ttw3BEnqqOasXkLYoa-8UdrgCr_nNIh6EniDzA4akAupgiJWJhDiRdmh1Tu2kjNez8EB8WtN4XkvaNEG9lDMMVlQZD2sQxInGAB12BM9_8SNAS3HmVFJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
بسیار خوشحالم که عربستان سعودی، ترکیه و پاکستان اخیراً و سرانجام، توافقنامه دفاعی مشترک مکه را امضا کردند.
🔴
این نشان می‌دهد که چگونه خاورمیانه در حال متحد شدن است و چگونه کشورها سرانجام می‌توانند به طور موثرتری از خود دفاع کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/142150" target="_blank">📅 00:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142149">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf270f369e.mp4?token=RR4H4xwTq6smACUCnjs7_fyXO3ENvTB1VNexrujknzW5JGdwmyi9NfF48GVYwTU6o4yJYE3g4YB5yi86p62kNRymH-WATdrvy9QEjpXh2ZZCNj5cwj_81AakKG_e3zzatuIyKWlkysl6F2p1JmTwlVRndQE9H4O3hIiXr_RMqvv26U4EdUQmFnBeRT1j45tErkn7yMt2nb6ICOf4110ZPQf_D9P_JK5yp4oSMlaBonpIbX4rplGdw565vgqXe9HzTk1FRazdEZz3STVNcJDAtL0wHU7QLOHQDyfyuCddq4ZCyubMHz6HIMiuLO9laSJH8_vhh0EN6-R_f0eekpT-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf270f369e.mp4?token=RR4H4xwTq6smACUCnjs7_fyXO3ENvTB1VNexrujknzW5JGdwmyi9NfF48GVYwTU6o4yJYE3g4YB5yi86p62kNRymH-WATdrvy9QEjpXh2ZZCNj5cwj_81AakKG_e3zzatuIyKWlkysl6F2p1JmTwlVRndQE9H4O3hIiXr_RMqvv26U4EdUQmFnBeRT1j45tErkn7yMt2nb6ICOf4110ZPQf_D9P_JK5yp4oSMlaBonpIbX4rplGdw565vgqXe9HzTk1FRazdEZz3STVNcJDAtL0wHU7QLOHQDyfyuCddq4ZCyubMHz6HIMiuLO9laSJH8_vhh0EN6-R_f0eekpT-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه جوان رو به علت اینکه زیر پست مسئولین کامنت فحش گذاشته بازداشت کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/142149" target="_blank">📅 00:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142148">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ:
اخیراً از رئیس جمهور کره جنوبی پرسیدم که آیا مایلند به ما در زمینه خلع سلاح هسته‌ای جمهوری اسلامی ایران بپیوندند، و آنها پاسخ دادند: "نه، متشکرم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/142148" target="_blank">📅 00:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142147">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
هواپیماهای جنگنده اسرائیلی مجددا وارد فضای هوایی جنوب لبنان شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/142147" target="_blank">📅 00:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142145">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-poll">
<h4>📊 وضع اینترنت و اتصالتون چطوره؟</h4>
<ul>
<li>✓ ضعیف</li>
<li>✓ قوی</li>
</ul>
</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/142145" target="_blank">📅 00:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142144">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
زمان آتش بس مندرج در تفاهم نامه رسما تمام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/142144" target="_blank">📅 00:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142143">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
۵دقیقه تا پایان زمان ۶۰روزه آتش بس</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/142143" target="_blank">📅 23:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142142">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21dc2ca760.mp4?token=BVTyZy4Jpc07hf8zAQ1MX7Zg8IFImmc11fpuCr1tjl9sLCJJn6bodPj_BDNcXTqonz4wDdJ0oF6bJwdij7PMxXrhzgRGtNZ08hM9qhowmIYHkta_o_OAnGk9s8rjk5eQLQRkksUPZGEe7anDdZZ219YvrW7POmiEVd7pa6TKRgftp0NZzv449nw8D7P4Rm1moM3xRQJtEy9nL4l0nr0Jd1re9FtVVJcLlxZ6nJnH6dTfC9ZRRDCCqWOna_jY1g0CYBCrE46hwZnOljtAYqpek8_0J0yUFEJgcX8SdEegWpYa7NuNOVfA4vol7IMvObq-LE4Vo3MwIwgxv0-PPvXr8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21dc2ca760.mp4?token=BVTyZy4Jpc07hf8zAQ1MX7Zg8IFImmc11fpuCr1tjl9sLCJJn6bodPj_BDNcXTqonz4wDdJ0oF6bJwdij7PMxXrhzgRGtNZ08hM9qhowmIYHkta_o_OAnGk9s8rjk5eQLQRkksUPZGEe7anDdZZ219YvrW7POmiEVd7pa6TKRgftp0NZzv449nw8D7P4Rm1moM3xRQJtEy9nL4l0nr0Jd1re9FtVVJcLlxZ6nJnH6dTfC9ZRRDCCqWOna_jY1g0CYBCrE46hwZnOljtAYqpek8_0J0yUFEJgcX8SdEegWpYa7NuNOVfA4vol7IMvObq-LE4Vo3MwIwgxv0-PPvXr8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه، اردوغان، در مورد احتمال وقوع جنگ با اسرائیل:
ما در مورد جنگ صحبت نمی‌کنیم، بلکه در مورد صلح صحبت می‌کنیم.
اما اگر کسی بخواهد ترکیه را به خاطر جنگ، نه صلح، مورد حمله قرار دهد، ترکیه در مبارزه با آن جنگ تردید نخواهد کرد و از آن فرار نخواهد کرد.
من این را با وضوح و صراحت کامل می‌گویم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/142142" target="_blank">📅 23:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142141">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
تایمز بریتانیا: ایران برای ارائه اطلاعات درباره سربازان آمریکایی، ۳۰ هزار دلار جایزه تعیین کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/142141" target="_blank">📅 23:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142140">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELGbIBWolXcUyWj-4H9g40gZrbfO9UvGVuzSQaH0yihs1D4u6WeKeyDHh9nEKbSZ1gITWVKKtOidRKshIpj-v7mZGM-LWdzU068FnI5w6dvzmA2QdTEQtenPd18ls3GkrzArV9OP47TwMhk7E_m_j5-FZ7Ga1yM2iF8uksC93kki4lzYXSxCnVwA1ZU01M9aIiVmOM_QY45gLNUonqEj1Y6ton06ZTvxP4VEUwvjV1MfiMQflM-FABctgN2r21uLOewHoZmcISE2e3lYueVHoO2EZhDd6yKbtaIxCNT1-KUuSoCAUnfTTn_Q-u7YH1yZUoojjv8evBU7LbOsb-u78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تابلو فرش دیده شده در بازار تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/142140" target="_blank">📅 23:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142138">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
قالیباف: برای جوانان برنامه ویژه داریم
🐸
🕺
🐸
👯‍♀️
🥸
🍆
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/142138" target="_blank">📅 23:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142137">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
داریوش خواننده مطرح ایرانی با انتشار ترانه توهم توطئیه و تیکه به رضا پهلوی مورد حمله طرفداران این اپوزیسیون قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/142137" target="_blank">📅 23:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142136">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏
👈
قتل جوان در جشن تولد با یک متلک؛ قاتل فراری به قصاص محکوم شد
‏
🔴
خانواده جوانی که در جریان برگزاری جشن تولد در یک پارک، با ضربه چاقو به قتل رسید، پس از دستگیر نشدن قاتل برای دریافت دیه از بیت‌المال به اجرای احکام مراجعه کردند.
‏
🔴
این پرونده به بهار سال ۱۴۰۲ بازمی‌گردد؛ زمانی که خانواده‌ای برای برگزاری جشن تولد به یکی از پارک‌ها رفته بودند. در همان محل، جوانی به همراه تعدادی از دوستانش حضور داشت.
‏
🔴
در جریان حضور دو گروه در پارک، بر سر متلک‌پرانی و حرف‌هایی که میان آنها رد و بدل شد، درگیری لفظی شکل گرفت. این اختلاف که ابتدا در حد مشاجره و جر و بحث بود، خیلی زود بالا گرفت و به درگیری فیزیکی منجر شد.
‏
🔴
در ادامه این درگیری، جوانی با ضربه چاقو به قتل رسید و قاتل پس از ارتکاب جنایت متواری شد.
‏
🔴
با توجه به فراری بودن متهم و دستگیر نشدن او، خانواده مقتول برای دریافت دیه از بیت‌المال به اجرای احکام مراجعه کردند. با این حال، متهم در نهایت در این پرونده به قصاص محکوم شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/142136" target="_blank">📅 23:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142134">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏
👈
سپاه: پدافند هواییمون حتی ۱ پیچش هم خارجی نیست و ۱۰۰٪ داخلیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/142134" target="_blank">📅 23:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142133">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In3FzauHw7N1x3amQLJhbTbX8p1YqHJ2pEKMNeW_R-Xau6Yc0sRhv_DFbOB7kD1wetm-3qcuv9gZ9b49NETYhVIZ5_68cRybunSpLChS9tWOpiHWHngPtQPhoKI28eJv7C_lzOWT1NCHlV0VkB6IW-VD4WwUe1L-GP_X4bwOw7dLgWs-_V3IQtTkH1Q-6Tvlz2ZnMD3jUAUHEV6x4zDlB8cC9nmixKY6ts5UCQAz4enIJ46JjSd-jiW0DZS1Rkafymipq8nbWmFYTM_FWIVHfRCvr2ybBjB_wvBO_O-pGYciOM1-q5kAn543nSWYlLobxkl3ruecj33xRYH0wLMzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نظرسنجی سقاب اصفهانی در توییتر درمورد ۳ طرح بنزینی دولت
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/142133" target="_blank">📅 23:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142132">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7V5oEGCSeupZKCPl7PBNG_oOuS6ZJo2hhuCPKYkuZlXYiqjhaoyh8zAE6ia5pPjoXfH8mU20l8QbMutydtVQ-fJtCEPUH1dXSm6XJUNSTVFXV-38uzlzjfMmwf2x0lweH-2SLbFRyV5q4hHZjNT0xD6KPUPhdvXzLydfoSjfx5PJHPlBy1LzZ4JfDCJYweSAmXRGjghJBlnRa6yqHhjYzAf6-OnmaPEuRL2PgE9bhLmZK8SAoE4WeuZOhuoZxO7KAsKCtZg0Na7iQk-qKjj2SJWH69apZJtgUMNLSEOzZzYUrCoPzYOqXfEC4jJgbMkVVNchekgH1U_CYncEKie6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو با انتشار این پست در اینستاگرام رسما تایید کرد که مجتبی خامنه ای زنده ست و گفت اینا نمیخوان من تو انتخابات برنده بشم. نزارید اینا به خواستشون برسن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/142132" target="_blank">📅 22:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142131">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
قالیباف: ۹۰میلیون ایران حامی نظام هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/142131" target="_blank">📅 22:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142130">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f93f0bed1.mp4?token=IN0b_IIbxWtqQMWy6X4QGdX5ASkRRtwclESC1EriqsMP9Co1UbjW8Kf2Wh_yaBWw_yBAfP4MBHuMbVF3VNppzhopYwf1cViQTNK2jdbf5tad5Br-_VxqWbVyGuVP22IZuZYTATc9TTZ7ZLnuUJ9L55u5VBbAvjQ9Nph8YznsAgvqkiBsqU_N_jxnFogD80hfMeTePmuIBiA0oc87p804eI3jkLMkrNDScyC1fyHxRoD-e0viJ9XMV6gtNOqzqy1HTI94RshJr0IJof2V7m3uxfpv0uWDntjvRnvqu696ehfADtm2F1EVeI3pNrug0a7hhKEI_TeBh9KJqkG4g8SOnVGDM6EcpI6-kGJKTJgYIgUBrEWhbQkDbBNgIhbwXzytSpZbn4UrBBu2vUmGuvF7IXQ3oaruGfVGB62XcHBvrtKenI9v71o8JfyDU0AHvLQ7HKj9AClJiRyGSXrt04bN9jmTQKLYlTDPIyj8W2sGXazeDUDOVBAQYsau0xSOSBC9LNwiPV7dA0HIJ_o6XsdJ21wBU-6We9qP8JVhx5RyaX6DfJwCXucMgJ7OuJJBH5_FvD0ZHloaPI_qyy814WBLpqYdhTgTwOLgnOdQ9NCtbaFD_LdFyCdAdjSCW_cM56KltrlVCxBTdecRXaVoQJ7LeqhEUB5llUNQVu1RcuP7Mb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f93f0bed1.mp4?token=IN0b_IIbxWtqQMWy6X4QGdX5ASkRRtwclESC1EriqsMP9Co1UbjW8Kf2Wh_yaBWw_yBAfP4MBHuMbVF3VNppzhopYwf1cViQTNK2jdbf5tad5Br-_VxqWbVyGuVP22IZuZYTATc9TTZ7ZLnuUJ9L55u5VBbAvjQ9Nph8YznsAgvqkiBsqU_N_jxnFogD80hfMeTePmuIBiA0oc87p804eI3jkLMkrNDScyC1fyHxRoD-e0viJ9XMV6gtNOqzqy1HTI94RshJr0IJof2V7m3uxfpv0uWDntjvRnvqu696ehfADtm2F1EVeI3pNrug0a7hhKEI_TeBh9KJqkG4g8SOnVGDM6EcpI6-kGJKTJgYIgUBrEWhbQkDbBNgIhbwXzytSpZbn4UrBBu2vUmGuvF7IXQ3oaruGfVGB62XcHBvrtKenI9v71o8JfyDU0AHvLQ7HKj9AClJiRyGSXrt04bN9jmTQKLYlTDPIyj8W2sGXazeDUDOVBAQYsau0xSOSBC9LNwiPV7dA0HIJ_o6XsdJ21wBU-6We9qP8JVhx5RyaX6DfJwCXucMgJ7OuJJBH5_FvD0ZHloaPI_qyy814WBLpqYdhTgTwOLgnOdQ9NCtbaFD_LdFyCdAdjSCW_cM56KltrlVCxBTdecRXaVoQJ7LeqhEUB5llUNQVu1RcuP7Mb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تنها رهبری که میشه گفت هرچی بگه همونه، مابقی هیچ
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/142130" target="_blank">📅 22:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142129">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18fb8279c6.mp4?token=JDFQhHua79GB61QQ57BcoldDmiX4kamsIS6EPL5GdszQ906ggqRwxxtwEIOqW4B0IG3ROWMjcXBLGD3kCkg-FMt90zUI3CEM8j4PbyTD_Fre7lD80S4rRM4KWbWNsI-_XG7ZGlVVxuRFoleuDnlC8vu2HtcNe6lJnIYjsBHQryhaMycorS521Ey4fNoCSt5cmACcgo2xeUF0OZQW-dC1uI1YrNCiBPB2jbhQd1dDeJyHx_nGOwEyvpZPdCZvK4MNQ0VtJy1N4Oz0M8Q9FeR8xTCGo6bSInVLjZWYiY6ph0lM5h2-eO4UtEMFKfp8h6HHz2dtkl0MkQZKQC7YKjoSuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18fb8279c6.mp4?token=JDFQhHua79GB61QQ57BcoldDmiX4kamsIS6EPL5GdszQ906ggqRwxxtwEIOqW4B0IG3ROWMjcXBLGD3kCkg-FMt90zUI3CEM8j4PbyTD_Fre7lD80S4rRM4KWbWNsI-_XG7ZGlVVxuRFoleuDnlC8vu2HtcNe6lJnIYjsBHQryhaMycorS521Ey4fNoCSt5cmACcgo2xeUF0OZQW-dC1uI1YrNCiBPB2jbhQd1dDeJyHx_nGOwEyvpZPdCZvK4MNQ0VtJy1N4Oz0M8Q9FeR8xTCGo6bSInVLjZWYiY6ph0lM5h2-eO4UtEMFKfp8h6HHz2dtkl0MkQZKQC7YKjoSuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف(ممد سامتینگ): مردم حس پیروزی را آن‌گونه که باید، حس نکردند
🔴
پ.ن: حس که چه عرض کنم اما این پیروزی خیالی تا ۳۰سانت به مردم فرو شده فعلا، البته شماها سیر هستید و متوجه نمیشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/142129" target="_blank">📅 22:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142128">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ef704c6a9.mp4?token=ZlxNaGD_MpFGWvYOnYl8kYumQ1EI3T_sNJoPiVhz6iELrNDczRsM7m1bTQXmdq9PvEYseQHs_Y9aodgflVw3jRInNFim8MrhvS3s8DQqJLpjMO3GhlHQjJ8nufwWsScKRoMR-Kq8OmwY-3R3kxb2K5mpEA4_J8364Z0XDUh3jJoYFXX1QFGLZlKMeCWgn3mYAwF98es9uCersvWnHQyOTOesa5x4wBFyL8-Zf_DHF-InqX4YbPRiqzpB7XgIHoybXgI2QduNw_bNgiVv-_fptFmdmc3kcvyzlYadWt3Vzl0PewRAVZd6_Tidpo7Mk78cQf5Pnpef7AQjXaM98zKB6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ef704c6a9.mp4?token=ZlxNaGD_MpFGWvYOnYl8kYumQ1EI3T_sNJoPiVhz6iELrNDczRsM7m1bTQXmdq9PvEYseQHs_Y9aodgflVw3jRInNFim8MrhvS3s8DQqJLpjMO3GhlHQjJ8nufwWsScKRoMR-Kq8OmwY-3R3kxb2K5mpEA4_J8364Z0XDUh3jJoYFXX1QFGLZlKMeCWgn3mYAwF98es9uCersvWnHQyOTOesa5x4wBFyL8-Zf_DHF-InqX4YbPRiqzpB7XgIHoybXgI2QduNw_bNgiVv-_fptFmdmc3kcvyzlYadWt3Vzl0PewRAVZd6_Tidpo7Mk78cQf5Pnpef7AQjXaM98zKB6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی: تو نمازهاتون شاه رو حتما دعا کنید چون هرکاری کرد اما با دین مردم بازی نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/142128" target="_blank">📅 22:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142127">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
۲ساعت تا پایان آتش بس
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/142127" target="_blank">📅 22:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142126">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo1X7vKTw36wh0CD_C2-ZGW9ELFeV7d3lnqlAJoMZrSyDfma6O9vFe8QX74uX2mxGj_A35C8Xr5ZO7Yxd-VjwAi0pwFTT5mr_1Zq2gXJFREO2wgUsd9pNfkyMhB9_gTC2ZzbiWNxR7hwJZ70sm9mD3i_XiGzefDRS4Av8Q610WUHAFnOoJfBH7Oo6-VSPpP84kkFlgF9mEdqvycP3W5eSd8BGF94fQ_ND6emNtJ-8isaVRCFy9NFAaNsKJHkYCSnTnbAikeuhasbXkIg4UfMx_0c2QZneV84i8GNWRENMcFAK5MeoiJowVwMc7HuLQnjT7jh6wFLaAuOuG6YnXcdtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عامل آتش‌سوزی عمدی مراتع هویر دماوند متواری شد
‏
🔴
عصر امروز آتش در ارتفاعات حاشیه روستای هویر دماوند دیده شد؛ حریقی که به گفته رییس اداره حفاظت محیط زیست دماوند عمدی بود و عامل آن پیش از حضور نیروها از محل متواری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/142126" target="_blank">📅 22:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142125">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
جوئیل، بلاگر ایرانی آمریکایی: علاوه بر رامین رضاییان چندتا بازیکن دیگه هم اومدن دایرکت و شات گرفتم بزودی پخش میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/142125" target="_blank">📅 22:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142122">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PK3_0kR6ufxgqwjhx9p-jJwZDl8SvhRjrKFDVSjn5RYGlBM9D-4CfjRZAdAj0sSI_MjHJHvEyvHkwmseX4zKYF-ilq9bqIRyQ_msSR3hbSczwA2JJzUZlbrOsdLX7m0oQtF1vwaN515eShW4et4omNQv7_oJF2Q4dKFudLTuoJ8BI7q6lLwO6h44izM65_gmadTy3JILb8hjo_5ezZjosnUa6h5caXUQgjfpOZeb5xl6L_vhVAoJZFbb5ZjIfvcyV1i7cPL4dczC519eEdU-7zCbUzg_pkXnrJGmw4ETWBTwINSHGhBr668XxGG6oaW2VccMlK89UEYYHjF_S-hsOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جوئیل، بلاگر ایرانی آمریکایی: علاوه بر رامین رضاییان چندتا بازیکن دیگه هم اومدن دایرکت و شات گرفتم بزودی پخش میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/142122" target="_blank">📅 22:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142121">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
آکسیوس: جرد کوشنر، داماد ترامپ فردا با  نتانیاهو دیدار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/142121" target="_blank">📅 21:58 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
