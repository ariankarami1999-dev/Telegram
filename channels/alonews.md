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
<p>@alonews • 👥 972K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 11:13:54</div>
<hr>

<div class="tg-post" id="msg-142185">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/alonews/142185" target="_blank">📅 11:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142184">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">با پایان آتش بس، محاصره تا کجا ادامه داره
⁉️
آیا جنگ قطعیه؟
تحلیل نوستراداموس ایرانی رو ببینید
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/alonews/142184" target="_blank">📅 11:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142183">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/142183" target="_blank">📅 11:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142182">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/142182" target="_blank">📅 11:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142181">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
آلن ایر: ترامپ حتی اگر بخواهد، نمی‌تواند از جنگ با ایران کنار بکشد
🔴
آلن ایر، دیپلمات ارشد سابق آمریکا و عضو تیم مذاکره‌کننده واشنگتن در توافق هسته‌ای ۲۰۱۵، می‌گوید ترامپ در برابر ایران در موقعیتی «غیرممکن» گرفتار شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/alonews/142181" target="_blank">📅 10:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142180">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
صداسیما: زمان شاه امید به زندگی ۵۰-۶۰ سال بود ولی الان شده ۸۰ سال
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/142180" target="_blank">📅 10:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142179">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0bkwGv1R4mze156g_77On05XjRzK4iA9h_l29l9H_-Xs6M1fOe6uzEStbDLqFJjzoIYyfdELM-9ARZuPDm1_PZOaYhjgvdYTCOpj504LhuWvxHAtj9IIQAtcMJQDV_m_GsYRg_aD7n0eJcBRq5SBb2hyvg37x9kNwVbf5aB8u9wlJxDzPvUWmYeJ0C7o4Q-6g1DDUtsTdOF5K5UVZW3zK17ayPyll6KES7AaH3SoO3EU8aEu-V4JxvBJsbvBY0qykV8xYs35DDdiY6zKEiH1-6CxvpxdCaMm-8LED8RQ7-Sy-fd7J_b_E3VaCKR9ijNmWNY7K5ng9srZM3RipP6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏
مسافران رفتند، قطعی برق چالوس بیشتر شد!
🔴
‏۶ ساعت خاموشی برنامه‌ریزی شده در چالوس طی ۲۴ ساعت، با وجود کاهش قطعی برق در زمان تعطیلات آخر هفته و حضور مسافران در این شهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/142179" target="_blank">📅 10:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142178">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
الجزیره: ترامپ برای ناتوانی در پیروزی در جنگ علیه ایران به دنبال «مقصر» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/142178" target="_blank">📅 10:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142177">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/142177" target="_blank">📅 10:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142176">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO2u6-ua8Ohrdbe3XvohPVJNfEYGlfk97HNeUjOCupWKSB2ZrKnAKP6rQL8x98CBbRnqiFDDMXvphfW4uN0r8lRS_vKrWk8nrj7wjsKzdTYExs03WwmGhJVlq1WEXwsiLeCgWXBgBY2PDYzEw2uFztC0AkSHVxSvux4iFUA-frc_UD7KsiIkkMBVKkLpcQSajO0_Hx-it21bKtXO92TbI6e1vlvWq0m92wAmXL80mx3Me91Qw4LzeFuA7nT9gzXGz3H6ggQh3QyTfYpQxGiMHSEPC9uDPymxZCY3dAgqfFY_nfwIzSVQFuRYI-_Tq3pvVreTjPn_7UZAMwIdZCVZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری که گروه آلفا گارد جاویدان منتشر کرد و نوشتند آماده ورود به ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/142176" target="_blank">📅 10:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142175">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
معاون سیاسی سپاه: تنگه هرمز زمانی باز می‌شود که آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد عمل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/142175" target="_blank">📅 10:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142174">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
جروزالیم پست:اطلاعات مربوط به تردد کشتی‌ها نشان‌دهنده کاهش چشمگیری در میزان عبور کشتی‌ها از تنگه هرمز است.با وجود احتمال عبور برخی از کشتی‌ها بدون ثبت، میزان تردد همچنان بسیار کمتر از حد معمول است، در حالی که پیش از جنگ، بیش از 130 کشتی به طور روزانه از این مسیر عبور می‌کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/142174" target="_blank">📅 10:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142173">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
روزنامه‌های بریتانیایی و آمریکایی:
تأثیر آشکار جنگ علیه ایران در [کاهش] توانایی آمریکا برای حفاظت از متحدان خود
🔴
ذخایر تسلیحاتی واشنگتن و متحدان آن دیگر به آسانی پاسخگوی یک جنگ طولانی یا دو درگیری هم‌زمان نیست
🔴
کشور‌های آسیایی متحد آمریکا، اکنون درباره توانایی این کشور برای دفاع از آن‌ها در صورت وقوع رویارویی با چین، پرسش‌هایی مطرح می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/142173" target="_blank">📅 10:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142172">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/142172" target="_blank">📅 10:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142171">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZhHtKnluFZmXAoSERe8eqGUY0StE_30OeNztlsFHlYjQfanX-wcTs8-FgvFY95H39jATmiriEI8ddfNR0H9DhXHmwseE-odrDEYEXhDTL-fTpC2XDufRpNv-mmSFlZrpwbLjBAjT_9B8QIOXYiGgl-4zIl83lcj6kg5n1M_YR5e6LmmH6o6a2eyhyCiamwTwXwFQk9r4F3eaSQ56KTieBOPordAkpNuyx5fcvZjqsCXk6BNMBM0KLzfJZ83x5Sch7tLm5aaNAR1jRoBTfHiO-t_5tIlCIqd97xl98W7RQerGqvFweM7HfB71-cklsragAViHSud7ZVr6BjuHgA9H1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده سابق ایالات متحده، مارگری تیلور گرین: آن‌ها در جلسات استراتژیک درباره استفاده از سلاح‌های هسته‌ای علیه ایران بحث می‌کنند.
🔴
بله، درست خواندید. این واقعیت دارد. من حدس نمی‌زنم، می‌دانم.
🔴
و این خالص شر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/142171" target="_blank">📅 10:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142170">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6lWeT4uJGYvaKqAKji3UXnrHokprsUcWaTk3_pjUJ7C_byJLjxvFT2UuE69saorUBdQkzq6O__oTIy5LXxNq31RPH6fk7-ZIPqG6_z4xheBVyw99deuBjso2Fs2wuoOJNwrCs2ZvDfkhKlQwAaIf8rqtdw_2K5SEMTqBNJoy3PAZDk9Go-Ww93k1nfGEq6eqXSOVRvqd_2532z0Sq7KnS7spBCKTFY9jBHjYnG_yCgNfPTyY8wMHweUwCfdLsTIqqBka0vETg50PKR11iKgmqfKJIEoUaKZSHiUzvf2vwNErDUXZvSpJ2aB9S_dAcSpUWHbYjIEIVt20IGrgYXdmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای تانکر سوخت‌رسان آمریکایی همچنان در نزدیکی تنگه هرمز فعال هستند، اما هیچ تاییدیه ای مبنی بر عبور ایمن کشتی‌ها یا وقوع حوادث امنیتی در این تنگه وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/142170" target="_blank">📅 10:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142169">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eR_2p6HQe1pkba_VgPQ8z6ofoYMke2h-iewY4StoTEnVaU5Kts4WdsxHDVexgzYbw4i8Im9HQtLxQOPNaXviM422b-ZgNxZeVE-ObuoDQnrxgxzllrLCbaWKujSymAOLL3n8UVdUsJzSBcBVnBSF-RN4zLmB0AAfVNnvAHazfmvYgdkkybSVeRgRkga02QOoXF2ng-bkw5l9bWvSU8eU-srVV3_gogbGzkgYYs9yMLcs5lbnH2Cr5fvB9YgHjt4OWamlEwTKLFMVRQo6rt7ZeBYAn2PLSjxTVh3syl4HaXlPauQXtlXYItxPpxlqJMlNFDQs5Edz0U-kfAesq5x0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دی‌وای‌اس‌جی، با استناد به مقامات ایرانی، گزارش می‌دهد که ایران در صورت از سرگیری درگیری‌ها، برنامه‌ریزی برای حملات تشدیدکننده بیشتر علیه کشورهای خلیج فارس دارد. گزینه‌ها شامل خرابکاری در کابل‌های اینترنتی در خلیج فارس، تحریک بی‌ثباتی میان شیعیان در کشورهای خلیج فارس و احتمالاً عملیات‌های زمینی علیه کویت است. دی‌وای‌اس‌جی همچنین به چندین بیانیه عمومی از سوی مقامات ایرانی که اخیراً صادر شده‌اند اشاره می‌کند که نشان می‌دهد ایران آخرین جنگ با ایالات متحده را به عنوان مقدمه‌ای برای یک رویارویی نهایی و قاطع‌تر می‌بیند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/142169" target="_blank">📅 09:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142168">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYMO2CekZ_P0xFRd0e851rRCRF-vdS1F7U5bGGniJXTljggCo-G3IQtsmvjntO9Zck2pvTRMU6d0kkPUYWMBURsanE8tHacblCJvy8Xdb0wuRwBlKGkBFJkIw7FFkBZIVooakLj1BPMHmvjV4Yzi8Vr0iHmnrR804myhR3bJx8xXvWZ7VTZKiB5pyBxDQ2zAMFotW7QhM5fjWXiHye4nKOaih6lcsjvvDMWPtB9k-OkABbjVBj7mA_3kwEjdM8aGJp42u8nAbhuG7g4oVAwM1u5_qbbaWv6gL6UBGY2k3bAhbqTwlCI4nKOFAQUJ1geSpnoBA4-OICx_KzNkeItqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ همچنان به شانون بریم از شبکه فاکس حمله می‌کند و او را «شیرین‌پسند» (Milktoast) خطاب کرده و برنامه فاکس نیوز ساندی را متهم به جانبداری علیه او، جنبش MAGA و جمهوری‌خواهان می‌کند، در حالی که برنامه او و شبکه را به دلیل نمایش تصاویر قدیمی از ساخت کاخ سفید و آنچه او «نظرسنجی‌های جعلی» می‌نامد، سرزنش می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/142168" target="_blank">📅 09:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142167">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/142167" target="_blank">📅 09:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142166">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwCBv26BwPHVBPjTWvpt-hriRcDONu4o8irHZ3gC1kIb4lmDYwwJYvMg-6ipIP_7kfJgc70wbsbcrFLSM445a5tXy_Shw0Z41T2-B_mE9WbJDduS7M1YaAVKqu67zClcDrbhH1mkphOtqQuenET5HnJ8Ofi0RTILDBu6yhkXkbVyTfhOmqXxe1VUnxIwAw0ntdvyO1kVYwfCW3CXtx1mQwk-nOrqKyd-54PouNNOsSq18TG793icNSAlVacQej3ai99GdIZA-bYjRASxgk5LmVN-h-Zx3eEca99pIjkBjddEXNCi-JsrrSZwPsWX-11UwSx7ioI1EH6AeAmJasVEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت، همزمان با انقضای تفاهم اسلام‌آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/142166" target="_blank">📅 09:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142165">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فایننشال تایمز: جنگ علیه ایران باعث شده که شرکت‌های بزرگ خودروسازی جهان، به سمت استفاده از ترکیبات جدید روغن موتور حرکت کنند تا با کمبود شدید روغن‌های پایه و باکیفیت مقابله کنند
🔴
موجودی روغن‌هایی که برای تولید روغن موتور‌های باکیفیت استفاده می‌شود، در آمریکا و اروپا رو به اتمام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142165" target="_blank">📅 09:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142164">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCfE-_8ArKZipoZ5m8zpyGzV6eSngzgnKJ0jhjSrfSmoMOYSpzO52FuGlYbr5Z1ponXn2QpFHjKnk2-8Ul7XWrhgEzLVarf0RBiZ9bp9IHMrIt58lzZ1MgfA0O1d8wg7ma_FJbbycIkxLRfdFE4kplEs1WZqm_kXVeB86Wu2buK9XPrdoRBPSear4lzFuLd8pIr0t6PTr4qfsCtxsnGo0v69jPnpj9nJbi81a-IuxvikMlZmEr6cNuD_mRF3uajj6dti7SUKNo_LaCHAPt_5-qEb-VCqWdmnnEJWqpOJDcIj-e5XC8-INZ0YDJYjvT-EJnBCVAxvyoTeXox36c3cMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمل و نقل از طریق تنگ هرمز در آخر هفته به دلیل حملات به نفت‌کش‌ها تقریباً متوقف شد، در حالی که داده‌های Kpler نشان می‌دهد که فقط پنج کشتی کالا در روز شنبه و هیچ کشتی‌ای در روز یکشنبه عبور کردند، در مقایسه با ۳۱ کشتی در آخر هفته گذشته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/142164" target="_blank">📅 09:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142163">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
هشدار هواشناسی/ گرمای ۵۰ درجه در خوزستان و بوشهر؛ رگبار در مازندران و گلستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/142163" target="_blank">📅 09:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142162">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات ایرانی: ایران در صورت از سرگیری جنگ، حملات تشدیدآمیز بیشتری علیه کشورهای حاشیه خلیج فارس برنامه‌ریزی کرده است.
🔴
گزینه‌های روی میز شامل خرابکاری در کابل‌های اینترنت خلیج فارس، تحریک ناآرامی میان شیعیان کشورهای خلیج و احتمال عملیات زمینی علیه کویت است. وال استریت ژورنال همچنین به اظهارات اخیر مقامات ایرانی اشاره کرده که نشان می‌دهد ایران جنگ قبلی با آمریکا را مقدمه‌ای برای یک رویارویی نهایی و قاطع‌تر می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/142162" target="_blank">📅 08:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142161">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/142161" target="_blank">📅 08:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142160">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/142160" target="_blank">📅 08:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142159">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT3am9ckmfpnM_7o2JhIQ2V0LGHd6EbIEcSdw2RcSkr-L5ifO0GWlaG3UFB73tZriUCj33GvtJqvUjeR1r6UECT32_j1hqZ1HNe-zXYOZYCQ_WRJvUn_wZmIzWNMgpnkgFtQw03jEZv41Y-uDjwdP74SPL5umQICZYmkSp1XRXJvS5RnSGZFjRMzgNaxrOa7_2OYHNcHNTtGYz8ALbbZH563Q4F7VreXemu5BRl1B-8vk8SIIwrkoT0xC73xaIhkCBcCU58Mk2qCLVuxfrIP9gT-8ZBkBPfim9hQDP_ixgmNHwfbXQekg387b18Tr47GXTzDUf5lc6KlP_C1TP3MZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پراید صفر فقط ۱ میلیارد و ۳۵۰ میلیون تومان
..
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/alonews/142159" target="_blank">📅 08:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142158">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/alonews/142158" target="_blank">📅 08:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142157">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/142157" target="_blank">📅 02:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142156">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ درباره ایران:
اتفاقات خوبی خیلی زود رخ خواهد داد
. در واقع، آنها همین حالا هم رخ داده‌اند، چون یک کاری هست که ما نمی‌توانیم اجازه دهیم انجام شود: ما نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/142156" target="_blank">📅 02:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142155">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTz1lmf6tDkik03TDu2xLLZssZjVHttiBQfY6hR9Z2-fxvrhDC3Z3WFZ-lO3otHH7WHV5ipTyC0dy8s9PlqEA1uI1awyL9BULst4yYdyMeHHVl6O-Cd-PWLKeyy5PeKzU3uqbcZMtw0hGYfuYQliLgPTTm4InLUaeiMQ90xcJR7qsurpIncahMMdbR9fcPaGUBY8j5i7fYgMGrYj3YjyNAAGWaRooDuHqg7ePtRsxWccfGql54D1O5QgKSFWG_ibLTqT6sQwPqThBw3iFgFGEHYVyG53fY5Gd0H-JLHDAM8QpJJapgKnWD1RCTAXoUVFweLdUoCnFJbIdDRLKs-aZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارجوری
تیلور گرین نماینده سابق مجلس آمریکا :
استفاده از بمب اتمی علیه ایران تو جلسات ترامپ مطرح شده
این یک طرح شیطانی هست جلوش باید سریعا گرفته بشه
مطلب رو اشتباه نخوندید درست خوندید یک فاجعه در راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/142155" target="_blank">📅 01:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142154">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/142154" target="_blank">📅 01:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142153">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رائفی پور: نابودی اسرائیل، تقدیر الهی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/142153" target="_blank">📅 01:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142152">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">با پایان آتش بس، محاصره تا کجا ادامه داره
⁉️
آیا جنگ قطعیه؟
تحلیل نوستراداموس ایرانی رو ببینید
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/142152" target="_blank">📅 01:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142151">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
نوید محمدزاده: از فلسطین حمایت می‌کنم چون با اسرائیل حال نمی‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/142151" target="_blank">📅 00:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142150">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzi1yvyIKFY7lJ8GMFHpLruTLzYUykXrj8OBKfTPPz9bMwsTLfFpiiIIFexGf5VTOg1RX1LGf4IVYyNKEpyke2a1GOY7e8IF5MruuFEBH--E9OSv9gEMHOrk8XTHeMsW5uRsd-DBTA_8EBKS5GdDhhcwf51DkdfV-4KQXRFXQMQUwjOhmqjDaoUgFK9a5AJ5ZOfWD3musI_WFSh2cAbKVvVAk5LGno20Ttw3BEnqqOasXkLYoa-8UdrgCr_nNIh6EniDzA4akAupgiJWJhDiRdmh1Tu2kjNez8EB8WtN4XkvaNEG9lDMMVlQZD2sQxInGAB12BM9_8SNAS3HmVFJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
بسیار خوشحالم که عربستان سعودی، ترکیه و پاکستان اخیراً و سرانجام، توافقنامه دفاعی مشترک مکه را امضا کردند.
🔴
این نشان می‌دهد که چگونه خاورمیانه در حال متحد شدن است و چگونه کشورها سرانجام می‌توانند به طور موثرتری از خود دفاع کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/142150" target="_blank">📅 00:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142149">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/142149" target="_blank">📅 00:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142148">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ:
اخیراً از رئیس جمهور کره جنوبی پرسیدم که آیا مایلند به ما در زمینه خلع سلاح هسته‌ای جمهوری اسلامی ایران بپیوندند، و آنها پاسخ دادند: "نه، متشکرم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/142148" target="_blank">📅 00:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142147">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
هواپیماهای جنگنده اسرائیلی مجددا وارد فضای هوایی جنوب لبنان شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/142147" target="_blank">📅 00:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142145">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-poll">
<h4>📊 وضع اینترنت و اتصالتون چطوره؟</h4>
<ul>
<li>✓ ضعیف</li>
<li>✓ قوی</li>
</ul>
</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/142145" target="_blank">📅 00:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142144">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
زمان آتش بس مندرج در تفاهم نامه رسما تمام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/142144" target="_blank">📅 00:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142143">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
۵دقیقه تا پایان زمان ۶۰روزه آتش بس</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/142143" target="_blank">📅 23:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142142">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/142142" target="_blank">📅 23:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142141">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
تایمز بریتانیا: ایران برای ارائه اطلاعات درباره سربازان آمریکایی، ۳۰ هزار دلار جایزه تعیین کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/142141" target="_blank">📅 23:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142140">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELGbIBWolXcUyWj-4H9g40gZrbfO9UvGVuzSQaH0yihs1D4u6WeKeyDHh9nEKbSZ1gITWVKKtOidRKshIpj-v7mZGM-LWdzU068FnI5w6dvzmA2QdTEQtenPd18ls3GkrzArV9OP47TwMhk7E_m_j5-FZ7Ga1yM2iF8uksC93kki4lzYXSxCnVwA1ZU01M9aIiVmOM_QY45gLNUonqEj1Y6ton06ZTvxP4VEUwvjV1MfiMQflM-FABctgN2r21uLOewHoZmcISE2e3lYueVHoO2EZhDd6yKbtaIxCNT1-KUuSoCAUnfTTn_Q-u7YH1yZUoojjv8evBU7LbOsb-u78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تابلو فرش دیده شده در بازار تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/142140" target="_blank">📅 23:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142138">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/142138" target="_blank">📅 23:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142137">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
داریوش خواننده مطرح ایرانی با انتشار ترانه توهم توطئیه و تیکه به رضا پهلوی مورد حمله طرفداران این اپوزیسیون قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/142137" target="_blank">📅 23:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142136">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/142136" target="_blank">📅 23:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142134">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏
👈
سپاه: پدافند هواییمون حتی ۱ پیچش هم خارجی نیست و ۱۰۰٪ داخلیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/142134" target="_blank">📅 23:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142133">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In3FzauHw7N1x3amQLJhbTbX8p1YqHJ2pEKMNeW_R-Xau6Yc0sRhv_DFbOB7kD1wetm-3qcuv9gZ9b49NETYhVIZ5_68cRybunSpLChS9tWOpiHWHngPtQPhoKI28eJv7C_lzOWT1NCHlV0VkB6IW-VD4WwUe1L-GP_X4bwOw7dLgWs-_V3IQtTkH1Q-6Tvlz2ZnMD3jUAUHEV6x4zDlB8cC9nmixKY6ts5UCQAz4enIJ46JjSd-jiW0DZS1Rkafymipq8nbWmFYTM_FWIVHfRCvr2ybBjB_wvBO_O-pGYciOM1-q5kAn543nSWYlLobxkl3ruecj33xRYH0wLMzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نظرسنجی سقاب اصفهانی در توییتر درمورد ۳ طرح بنزینی دولت
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/142133" target="_blank">📅 23:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142132">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7V5oEGCSeupZKCPl7PBNG_oOuS6ZJo2hhuCPKYkuZlXYiqjhaoyh8zAE6ia5pPjoXfH8mU20l8QbMutydtVQ-fJtCEPUH1dXSm6XJUNSTVFXV-38uzlzjfMmwf2x0lweH-2SLbFRyV5q4hHZjNT0xD6KPUPhdvXzLydfoSjfx5PJHPlBy1LzZ4JfDCJYweSAmXRGjghJBlnRa6yqHhjYzAf6-OnmaPEuRL2PgE9bhLmZK8SAoE4WeuZOhuoZxO7KAsKCtZg0Na7iQk-qKjj2SJWH69apZJtgUMNLSEOzZzYUrCoPzYOqXfEC4jJgbMkVVNchekgH1U_CYncEKie6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو با انتشار این پست در اینستاگرام رسما تایید کرد که مجتبی خامنه ای زنده ست و گفت اینا نمیخوان من تو انتخابات برنده بشم. نزارید اینا به خواستشون برسن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/142132" target="_blank">📅 22:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142131">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
قالیباف: ۹۰میلیون ایران حامی نظام هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/142131" target="_blank">📅 22:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142130">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/142130" target="_blank">📅 22:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142129">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/142129" target="_blank">📅 22:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142128">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/142128" target="_blank">📅 22:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142127">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
۲ساعت تا پایان آتش بس
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/142127" target="_blank">📅 22:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142126">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo1X7vKTw36wh0CD_C2-ZGW9ELFeV7d3lnqlAJoMZrSyDfma6O9vFe8QX74uX2mxGj_A35C8Xr5ZO7Yxd-VjwAi0pwFTT5mr_1Zq2gXJFREO2wgUsd9pNfkyMhB9_gTC2ZzbiWNxR7hwJZ70sm9mD3i_XiGzefDRS4Av8Q610WUHAFnOoJfBH7Oo6-VSPpP84kkFlgF9mEdqvycP3W5eSd8BGF94fQ_ND6emNtJ-8isaVRCFy9NFAaNsKJHkYCSnTnbAikeuhasbXkIg4UfMx_0c2QZneV84i8GNWRENMcFAK5MeoiJowVwMc7HuLQnjT7jh6wFLaAuOuG6YnXcdtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عامل آتش‌سوزی عمدی مراتع هویر دماوند متواری شد
‏
🔴
عصر امروز آتش در ارتفاعات حاشیه روستای هویر دماوند دیده شد؛ حریقی که به گفته رییس اداره حفاظت محیط زیست دماوند عمدی بود و عامل آن پیش از حضور نیروها از محل متواری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/142126" target="_blank">📅 22:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142125">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
جوئیل، بلاگر ایرانی آمریکایی: علاوه بر رامین رضاییان چندتا بازیکن دیگه هم اومدن دایرکت و شات گرفتم بزودی پخش میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/142125" target="_blank">📅 22:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142122">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PK3_0kR6ufxgqwjhx9p-jJwZDl8SvhRjrKFDVSjn5RYGlBM9D-4CfjRZAdAj0sSI_MjHJHvEyvHkwmseX4zKYF-ilq9bqIRyQ_msSR3hbSczwA2JJzUZlbrOsdLX7m0oQtF1vwaN515eShW4et4omNQv7_oJF2Q4dKFudLTuoJ8BI7q6lLwO6h44izM65_gmadTy3JILb8hjo_5ezZjosnUa6h5caXUQgjfpOZeb5xl6L_vhVAoJZFbb5ZjIfvcyV1i7cPL4dczC519eEdU-7zCbUzg_pkXnrJGmw4ETWBTwINSHGhBr668XxGG6oaW2VccMlK89UEYYHjF_S-hsOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جوئیل، بلاگر ایرانی آمریکایی: علاوه بر رامین رضاییان چندتا بازیکن دیگه هم اومدن دایرکت و شات گرفتم بزودی پخش میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/142122" target="_blank">📅 22:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142121">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
آکسیوس: جرد کوشنر، داماد ترامپ فردا با  نتانیاهو دیدار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/142121" target="_blank">📅 21:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142120">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoMVT9zY7wIMPqDc9t-8LrU92tE7nq-CAXabUiv9F3YknzqF7X42iHkbj6KyvSja57X39FC6Vi0QamNZZtcE8RmNfsklqfZCrlRYO6fbJ-nZbLcwjWAgWPLTnu5R3S7L-AHGhKuJ01u26ULyKGnfLVqYYw-CkzDfdRBY_bZGnLodqmgCVgSy7I6MZqp7ieEu8yjKIK4ecuiA0d4esDaVo85OJzlQ9tFiQekWJxfYYh-mQwViYew_ziVxVxm6pyTFH4uSLv55d6HB0AonioBCDnTIjQ9eBS73gwABzSWQ8MgUrBrAcF8fEVWamqmAXUVFbqxd-5brBkHCRg5ZeUVEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۴: «ثانیه‌ها به شماره افتاده‌اند.»
🔴
کمتر از ۲۴ ساعت تا پایان مهلت اولیه ۶۰ روزه برای صلح و مذاکره میان آمریکا و ایران که در تفاهم‌نامه ماه ژوئن تعیین شده بود، باقی مانده است.
🔴
این توافق موقت از ابتدا شکننده بوده و با مواردی از نقض توافق، افزایش تنش‌ها و ادعاهای پیشین هر دو طرف درباره پایان یا تعلیق آن همراه بوده است.
🔴
تاکنون نیز هیچ تمدیدی برای این توافق تأیید نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/142120" target="_blank">📅 21:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142119">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
به گزارش واشنگتن تایمز، اسکات بسنت، وزیر خزانه‌داری آمریکا، از اعمال تحریم‌های جدید علیه ایران با هدف افزایش انزوای اقتصادی این کشور خبر داد.
🔴
این اقدامات قرار است هم‌زمان با ادامه محاصره دریایی آمریکا در تنگه هرمز اجرا شود..
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/142119" target="_blank">📅 21:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142118">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نشانه‌های ادامه پسرفت اینترنت ایران: اختلال‌های تازه و نارضایتی کاربران
!
🔴
اینترنت ایران در هفته اخیر نشانه‌هایی از ناپایداری و پسرفت دوباره نشان داده است. داده‌های فنی از اختلال‌های منطقه‌ای خبر می‌دهند و هم‌زمان گزارش‌های کاربران از کندی، قطعی و دشواری دسترسی حکایت دارد.
🔴
بر اساس نظرسنجی دیجیاتو درباره کیفیت اینترنت که امروز، ۲۵ مرداد ۱۴۰۵، انجام شده است، ۷۹ درصد شرکت‌کنندگان گفته‌اند کیفیت اینترنتشان در طول یک هفته گذشته بدتر شده است. تا لحظه نگارش این گزارش، حدود ۳ هزار نفر در این نظرسنجی شرکت کرده‌اند.
🔴
آخرین گزارش فصلی Cloudflare نشان می‌دهد پس از بازگشت اینترنت در خردادماه، ترافیک HTTP ایران در مقطعی تا ۹۰ درصد سطح پیش از خاموشی بالا رفت، اما بعداً روی حدود ۵۹ درصد سطح پیش از خاموشی ۸۸روزه تثبیت شد. Cloudflare تأکید کرده این سطح بیشتر شبیه وضعیت پیش از خاموشی اخیر است اما به معنای بازگشت کامل اینترنت به شرایط عادی نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/142118" target="_blank">📅 21:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142117">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203d5aef6b.mp4?token=b8YLWyVpXD_c7rhN_rhixk1BZSfW19TcFus5dWtzvQ40h1yKktFRDtDZ9S0l14QK9_TLvBqX47bIeb2TSoPdmbHy_7S9KQP-MP0S_7hOAb0hY-HjYs-1g26uxOZQRIxoMriTwDDgXMt8eUqfwEVVtst8PaI_-LBh6Qglovmbpo-bb-TiA-QDViR9zosUffkzRicL0YbMGJmfI6rxDY-ppmi2c8cfSgrCiAD5m87bTEVImU04pt9yaK7QKjT3jqnVlW4gZW4Owy6dK1I-isyYtvmV96mrQzoy17cO4NfsMSpX63uwBU0_r1xqxGOnT614R4X-U1TbhcW3vU4Ojex_4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203d5aef6b.mp4?token=b8YLWyVpXD_c7rhN_rhixk1BZSfW19TcFus5dWtzvQ40h1yKktFRDtDZ9S0l14QK9_TLvBqX47bIeb2TSoPdmbHy_7S9KQP-MP0S_7hOAb0hY-HjYs-1g26uxOZQRIxoMriTwDDgXMt8eUqfwEVVtst8PaI_-LBh6Qglovmbpo-bb-TiA-QDViR9zosUffkzRicL0YbMGJmfI6rxDY-ppmi2c8cfSgrCiAD5m87bTEVImU04pt9yaK7QKjT3jqnVlW4gZW4Owy6dK1I-isyYtvmV96mrQzoy17cO4NfsMSpX63uwBU0_r1xqxGOnT614R4X-U1TbhcW3vU4Ojex_4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال خطاب به جورج واشنگتن سازنده کاخ سفید: از شما، جورج، برای برخی از ایده های درخشان شما در مورد این مجتمع نظامی/اتاق باله بزرگ متشکرم! پرزیدنت دی‌جی‌تی
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/142117" target="_blank">📅 21:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142116">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
به گزارش بلومبرگ، ۸۳ درصد از شهروندان چین معتقدند مزایای هوش مصنوعی از معایب آن بیشتر است؛ در حالی که تنها ۳۹ درصد از آمریکایی‌ها چنین دیدگاهی دارند.
🔴
این گزارش می‌گوید شکاف میان افکار عمومی دو کشور ممکن است بیش از آنکه به خود هوش مصنوعی مربوط باشد، نتیجه تجربه متفاوت چین و آمریکا از موج قبلی تحول فناوری باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/142116" target="_blank">📅 21:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142115">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
منابع دیپلماتیک به الجزیره گفتند که اسرائیل حملات اخیر خود به انصار و دیر الزهرانی را با بیان حضور مقام‌های حزب‌الله توجیه کرد و با ارائه عکس‌ها و اطلاعات به ایالات متحده، سبز کردن عملیات را به دست آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/142115" target="_blank">📅 21:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142114">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c241046bc.mp4?token=a2j8ph8YxaJxuFvUNYUbXEHAMEkcIQVAJO9eHmi7zRlpiUyFaZ3xF5ylyyt36eNuFS7QCT5xn1NBsPYonItUmvBMfO9b5YJm_VUjSe4AgBRH5Bjv2-eo1pcG1EVuCByOtkzyHggAHwqVr2rpFFAOgmSP_97zRPsSwsozuBXeivO11yyq1BO4Q8WCzuD4pc8SzCXvtMQnJ2XbO2fHnOXW4o7lev5IeeP4MnqoXK_ZCFucEKyTEsnHgh7uuGSOp7lFA8DVkbDlOiZ5Plv5coA14NXYZ2pRDqmTsdbGQI1VCqHDi-mE41Kt2QnwrSZ5Hn-AKb3gKtF91KgjTLtHuh7Oqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c241046bc.mp4?token=a2j8ph8YxaJxuFvUNYUbXEHAMEkcIQVAJO9eHmi7zRlpiUyFaZ3xF5ylyyt36eNuFS7QCT5xn1NBsPYonItUmvBMfO9b5YJm_VUjSe4AgBRH5Bjv2-eo1pcG1EVuCByOtkzyHggAHwqVr2rpFFAOgmSP_97zRPsSwsozuBXeivO11yyq1BO4Q8WCzuD4pc8SzCXvtMQnJ2XbO2fHnOXW4o7lev5IeeP4MnqoXK_ZCFucEKyTEsnHgh7uuGSOp7lFA8DVkbDlOiZ5Plv5coA14NXYZ2pRDqmTsdbGQI1VCqHDi-mE41Kt2QnwrSZ5Hn-AKb3gKtF91KgjTLtHuh7Oqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش ترامپ به استعفای سخنگوی کاخ سفید
🔴
ترامپ: من متوجه شدم که کارولین بچه‌هاش رو بیشتر از من دوست داره و من در این مورد خیلی نگران هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/142114" target="_blank">📅 21:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142113">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
بلومبرگ: انتقال مخفیانه نفت از تنگه توسط اعراب
!
🔴
‏بلومبرگ نوشت: به گفته افرادی که از این محموله‌ها اطلاع دارند، انتقال نفت از طریق تنگه هرمز به‌صورت مخفیانه و بدون شناسایی، و سپس انتقال محموله‌ها به نفتکش‌های دیگر در خلیج عمان، با حداکثر ظرفیت ادامه دارد؛ این روند حتی با وجود حملات اخیر به کشتی‌ها متوقف نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/142113" target="_blank">📅 21:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142112">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
امیر حاتمی،فرمانده ارتش: اخراج آمریکا انجام شده است و دیگر اجازه ورود به خلیج فارس، دریای عمان و تنگه هرمز را نخواهند داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/142112" target="_blank">📅 21:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142111">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
حماس دفترشو از قطر برد ترکیه و این کشور شد پایگاه اصلی حماس
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/142111" target="_blank">📅 20:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142110">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فرماندار شهرستان بندرلنگه: ۹ صیاد بندرلنگه‌ای پنج روز پیش با سه قایق جداگانه از اسکله بندرکنگ و اسکله گشه راهی دریا شده‌اند و تاکنون به خانه بازنگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/142110" target="_blank">📅 20:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142109">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ان‌بی‌سی نیوز : ناو یو‌اس‌اس جورج واشنگتن اقیانوس آرام را ترک کرد تا در بحبوحه جنگ با ایران، جایگزین ناو آبراهام لینکلن در خاورمیانه شود.
🔴
این اقدام موقتاً غرب اقیانوس آرام را بدون ناو هواپیمابر آمریکایی باقی می‌گذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/142109" target="_blank">📅 20:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142108">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
پزشکیان در جلسه هیات دولت: محسن رضایی پیش از این همکاری خوبی با دولت داشت و امیدواریم در مسئولیت جدید نیز هماهنگی، همکاری و انسجام به خوبی ادامه پیدا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/142108" target="_blank">📅 20:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142107">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db02877d6b.mp4?token=kY-l3XT4KV9vQ8VihQlqMYqkQR46fEpG1EtrtWRvCGJ495Dtb4iQ-9md0PP-Gvj9PJJ1MCZyPRl9UeliXNI8wPVkB72tmZ00kt9_hIa2fgty35bNS9yBt8sOd5XTlCJXRCGnhUfITOEB8SIhasAu4jq6MRzfHORj7PRZt0RK1miyHxjdg7pgtrDd6ts29K4JP2NnSspqoGwQojk206gjQuSEgJ8nrDxCaTw9Cy7RaDaiiiJlKcunQy1fF1t11kVNHw6AdBrg-DptP5fXLNbr1KgwUIaPjeJniJzqusjji1cu8Nua1_t-hxqtq1n_jRvuoToozhpMNPZUONtUQV282w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db02877d6b.mp4?token=kY-l3XT4KV9vQ8VihQlqMYqkQR46fEpG1EtrtWRvCGJ495Dtb4iQ-9md0PP-Gvj9PJJ1MCZyPRl9UeliXNI8wPVkB72tmZ00kt9_hIa2fgty35bNS9yBt8sOd5XTlCJXRCGnhUfITOEB8SIhasAu4jq6MRzfHORj7PRZt0RK1miyHxjdg7pgtrDd6ts29K4JP2NnSspqoGwQojk206gjQuSEgJ8nrDxCaTw9Cy7RaDaiiiJlKcunQy1fF1t11kVNHw6AdBrg-DptP5fXLNbr1KgwUIaPjeJniJzqusjji1cu8Nua1_t-hxqtq1n_jRvuoToozhpMNPZUONtUQV282w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دزدی خانوادگی یه خانواده از فروشگاه:از دختر بچه تا مادربزرگ، همه توی دزدی نقش دارن!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/142107" target="_blank">📅 20:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142106">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dndjrdd0v--OSrNqco4CjptlVIlRaqB35jbqeg5c_r0SPiUeys_xYsA-MCIsTO8pgATuGBJdxlW6p_RgCSYLxKwjFtCaL_RwsP4keA-maw4_XXg1Gg7Hj8q1Ez2etG2Z5QwEc4MvTCl3VIgyDDRd4NcLBruitUtjhkFo2XmM8575u8-7sFaLCAd_6jWmtvE693qtdKFDn0aH8OmllFu4JsLQtBThVU9rMf1ZFxK_vYUiyDGXT4UZYCEk6sMjI1_U3jcD3wauhnDHRPozQlhI-bCjBrxJjc8XmM6VwQ4os5BRvshbB9bfSVvnha6zD7shiZ1S2YsF5Css_CJnO7QIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پدر مهسا امینی:
کلماتی که اریایی‌نژاد(نماینده کثیف مجلس) برای مهسا استفاده کرده سزاوار خودش و خانوادشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/142106" target="_blank">📅 20:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142105">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
کارشناس صداسیما: مشکلات فعلی کشور، ریشه در سیاست‌های دوران پهلوی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/142105" target="_blank">📅 20:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142104">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b6a1f4993a.mp4?token=emti-oiTB7_rPZWazCvP6cl_i1fjIg72Ro-2ve5yyO9zm7Sg0eDMK5uavWIq4D9pdFQTc7pQQhC5yuCx04mqNjihcfgAx-E6Ecn4MxOylhwfIwtanibTFS6dEfFCMvufeo6Nko4cKPUESmLG-f07S71Wj9jM04LdLKzFUQn7WRHfJXUAhtB9hgwUvGGfaxKcIDM92njPXiAOtpaqmA-ooCygxu1HFiV7JNI71NIyk-jlJHV9srK-byZZcCuJXrfYbAnqNToe3kgV-SxNjS-aZqmf0diz_5GVW4AwJ5OfKfLThndnHnyXfCVna888N-wh4t6WystOor_a2zQD_fnXdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b6a1f4993a.mp4?token=emti-oiTB7_rPZWazCvP6cl_i1fjIg72Ro-2ve5yyO9zm7Sg0eDMK5uavWIq4D9pdFQTc7pQQhC5yuCx04mqNjihcfgAx-E6Ecn4MxOylhwfIwtanibTFS6dEfFCMvufeo6Nko4cKPUESmLG-f07S71Wj9jM04LdLKzFUQn7WRHfJXUAhtB9hgwUvGGfaxKcIDM92njPXiAOtpaqmA-ooCygxu1HFiV7JNI71NIyk-jlJHV9srK-byZZcCuJXrfYbAnqNToe3kgV-SxNjS-aZqmf0diz_5GVW4AwJ5OfKfLThndnHnyXfCVna888N-wh4t6WystOor_a2zQD_fnXdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام همین الان ویدئوی سوخت‌گیری یک فروند F-35A در آسمان خاورمیانه را
منتشر کرد
🔴
سنتکام: یک جت جنگنده مخفی F-35A نیروی هوایی ایالات متحده در حین گشت‌زنی در آب‌های منطقه‌ای بر فراز خاورمیانه توسط یک هواپیمای سوخت‌رسان KC-135 Stratotanker سوخت‌گیری می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/142104" target="_blank">📅 20:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142102">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
تام باراک، فرستاده ویژه آمریکا در منطقه: حزب الله 40هزار نیرو دارد که هر کدوم ماهانه 2200دلار حقوق میگیرند
🔴
پ.ن: اینجا هم ماهی 7دلار سهم هر ایرانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/142102" target="_blank">📅 20:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142101">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
2دلار یارانه دهک ۱ تا ۳ واریز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/142101" target="_blank">📅 20:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142100">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
یه سوال از دلواپسان
🔴
قِر دادن ۸الی ۱۰ شب مورد نداره؟ آخه هرشب شاهد رقص پرچم هستیم و من تحریک میشم والا
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/142100" target="_blank">📅 20:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142099">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
جرد کوشنر فردا با نتانیاهو دیدار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/142099" target="_blank">📅 20:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142098">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
پزشکیان: آن عده‌ای که نان خودشان را در دامن زدن به اختلاف، تهمت و دروغ می‌دانند، مطمئن باشند اختلاف فقط به نفع آمریکا و اسرائیل است
🔴
انتصابات مدیریتی باید بر مبنای شاخص‌های علمی و فارغ از ملاحظات سیاسی انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/142098" target="_blank">📅 20:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142096">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuIkF9vhFv0HTvDh5Xq7edQRr_g7DmAy1NIqjVPMll1msrE5o_tX-4nhUI1xluMRDj-bAmNw4AUXUrcaJ5Ps39LYIHNt7E7NRAYjgjW12xqwTr41aYRh4cwX17-8vwE5biJPWzbaRjoc_h9HnmJULbXU-7N0-pMeRpULFq0skWhvAZWN4rhtIRwB_rm-kou_tyCHg-5gt3sNfyEKix9NADAenNC6Ue38-C6MmtaMGqqDlaZ6lugI1K5Sa08Ii46GeZp_iy6-bfbtFEzd3YFt3Yo71hp0sXmJbFwJoHSVyOpT3CxJrlnLj829pJNnFbOfX0gA8AylwRISsYrLl_n_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجتبی خامنه‌ای به مجلس: هوای مردم رو داشته باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/142096" target="_blank">📅 20:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142095">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UupJRY_WhCfeozITmd_oUvVx68qoyh8FfZJDdh18yF7_ied-WRGUwlpMexq4_lKGp65BbJ7C-G15WVwswlsqg0r3tqfE1zjezHsx4oKvhGMgfPQ2GfIjy_LgyY84J2hgBJLp1HaDOuavp8-r8wZA3a3S5fR05o9ymxOVEe0K7wMdF5yGOBBxD80H47uDh_2TOzDeyBDzNbRKHOp4glfTXa4k6XdTgubK3fAPiD4B7ioDAdCWZWG2I-4PIGVktOgciJGZEujDtJrKyznSfjuh1OyksEs3bBBlqZONlT8o237XQapvoZFN8uJ-644hIIQMgtt2hR9WQ5-rfliia8pp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله توپخانه سنگین به بیت یحون، جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/142095" target="_blank">📅 20:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142094">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/269325e5d3.mp4?token=T1i1p9IxIhVBUED1mVaSyrNcwZGsKFZqVSVx7YReOm7RmFP-WOaNixKcGAAFkPdMcbAEFX3kEoP-8R52CuGo3HR6h3ksHtMYo5TavHQNqFSoFkfvJR2dj2vV2ACKT2PRxHuwEdeiuiYzj9z0XWQJW8bJM_oEIzKpdqkvOuZJK-Q__zGGtGIOkJApwLv4UGvS5msfaQwrwVd0OMkdx3fedey9CQgh2P-f0eB21Wolpl4zyjnuhevwn9mdpPMlK5zp9FlVbw-NmudLyfsBgHXuXh0U5NBhy8-ZB8w73fuKq_9HmB8uX8XAhAWffB44N8lNhu8ZbTRlMC_qx61Qxky01Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/269325e5d3.mp4?token=T1i1p9IxIhVBUED1mVaSyrNcwZGsKFZqVSVx7YReOm7RmFP-WOaNixKcGAAFkPdMcbAEFX3kEoP-8R52CuGo3HR6h3ksHtMYo5TavHQNqFSoFkfvJR2dj2vV2ACKT2PRxHuwEdeiuiYzj9z0XWQJW8bJM_oEIzKpdqkvOuZJK-Q__zGGtGIOkJApwLv4UGvS5msfaQwrwVd0OMkdx3fedey9CQgh2P-f0eB21Wolpl4zyjnuhevwn9mdpPMlK5zp9FlVbw-NmudLyfsBgHXuXh0U5NBhy8-ZB8w73fuKq_9HmB8uX8XAhAWffB44N8lNhu8ZbTRlMC_qx61Qxky01Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی پرچم‌های اسرائیل را در جاده ساحلی جنوب لبنان بین نقوره و صور نصب کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/142094" target="_blank">📅 19:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142093">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEw63_kBNUM84g_QXq43HtcEPLXjJ9y4PrWQ7rjomtDlG8XTLjiFV8GmyJ1-GwTX_5BiCOzGBPLcuxjbHmxsfy1SpMzSeOTQHAahOjrM0bDdQGblSILyqdFPOoMfQHxkbZ19TlJA64PIGtyTFJ9TFWkaEUGq-J76Zl0inENVGGC2D43V1MGk3cvAppQAuVSR02-2lmE7nwNsasS4K5Vsdhhx8yhJoPluTOFX9ZbbcuFjzB5aqGlomw11-UN15C6iEAkOn7yvwIrTSfhv2qE_3iW9E5bWovPZ_LI4XpnUgDK8MCmSYEAUY2P0TrAVt0o2oOPgFrtqx2CA81bRRSll1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند لحظه پیش، یک پهپاد اسرائیلی به منطقه "علی الطاهر" در جنوب لبنان حمله کرد.
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/142093" target="_blank">📅 19:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142092">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کانال ۱۴: توافق ایالات متحده و ایران با انقضای مهلت ۶۰ روزه فرو می‌ریزد
🔴
مهلت ۶۰ روزه توافق‌های میان ایالات متحده و ایران در روز یکشنبه بدون دستیابی به توافقی برای پایان جنگ یا رسیدگی به برنامه هسته‌ای به پایان رسید. درگیری اکنون به یک نبرد اقتصادی بر سر تنگه هرمز، تحریم‌ها و وجوه مسدود شده ایران تغییر جهت داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/142092" target="_blank">📅 19:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142090">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e64058ea.mp4?token=H62gVzwhpK7E1Wi3Z5c-vnCUSx5n4Vz90e0gHI0EtyQ164vZ7gVCZNZ3bby8S0ID3aPF1U797knorE3frdq408ujSVAaijFvIpJImCj-Va-aYTAXCs-pDRae-zqxBJVGx-7USU2lswSsjClvUmY_3wE0xZsOwhulKns8EeNoZ4J5mKFfMI-ARTk4X8kErLHfiYb89-uzdXapn-qnCph5NgMmSEtD6V-FrBBlG_WszNA3hzWRReFelgeFUptzB5unRqx4e7wI1ZjuYhtnz223qIF4Bumj0tJ_9EeSj4_OFmRzTGKQ3FUZ1Oq3o0hoCTzz3N1H_8YHJyzR6w273SBB7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e64058ea.mp4?token=H62gVzwhpK7E1Wi3Z5c-vnCUSx5n4Vz90e0gHI0EtyQ164vZ7gVCZNZ3bby8S0ID3aPF1U797knorE3frdq408ujSVAaijFvIpJImCj-Va-aYTAXCs-pDRae-zqxBJVGx-7USU2lswSsjClvUmY_3wE0xZsOwhulKns8EeNoZ4J5mKFfMI-ARTk4X8kErLHfiYb89-uzdXapn-qnCph5NgMmSEtD6V-FrBBlG_WszNA3hzWRReFelgeFUptzB5unRqx4e7wI1ZjuYhtnz223qIF4Bumj0tJ_9EeSj4_OFmRzTGKQ3FUZ1Oq3o0hoCTzz3N1H_8YHJyzR6w273SBB7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ریحانه قاسمی زاده مجری صداوسیما:
جنوب ایران، فدای جنوب لبنان، اینو یادتون باشه!!
🔴
پ.ن: ک...... تو جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/142090" target="_blank">📅 19:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142089">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رییس سازمان غذا و دارو:
هزینه حمل داروهای وارداتی که پیش‌تر با کشتی 3 هزار دلار بود، به دلیل محاصره دریایی، اکنون برای حمل هوایی به 30 هزار دلار رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/142089" target="_blank">📅 19:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142088">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزارت دفاع روسیه: یک تأسیسات اوکراینی تولید قایق‌های بدون سرنشین را در غرب اودسا هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/142088" target="_blank">📅 19:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142087">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
روزنامه واشنگتن‌پست در گزارشی فاش کرد کشورهای حاشیه خلیج‌فارس به دلیل بی‌اعتمادی به راهبرد جنگی دونالد ترامپ در قبال ایران، در حال بررسی درخواست برای تخلیه پایگاه‌های نظامی آمریکا از خاک خود هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/142087" target="_blank">📅 19:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142086">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBv1sOntsFutrBBC4WP45aqVDlqnJJ3X0xyRidUOJY7n78XMqEGkvMFGnZc9SUlMjAJrTP5uPR6xG3xzfLbHo70jQ96V3yNS4bkbdD8SYjeinFAdjHU1xFcuH_bnb53WS_ZQTE8PrWdJPPnwc-p3OlEBn52hIu0HDZTFM28xTclb_evJ4M-01CKVfr18Y9wVPsAPe4zTLyVAkFkKQTVmQgXBiE8iVe_6LLB7S8sgHt1fon6K_krOPXQAvQxo04HydHE_17tFMYQXfWK7HBF09BIR17RT3hro0g-H9zga46wAvQ9fzMIgQ5feu3laBJgF6lt9vbqs1lOIb0NJmyHLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
السیسی، رئیس جمهور مصر همراه با وزیر امور خارجه و وزیر اطلاعات این کشور با جرد کوشنر، مشاور ارشد ترامپ و داماد او دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/142086" target="_blank">📅 19:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142085">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIWg7KrpSglxvzsdPsc6ehxrzE8rcsR9UofTpaJedx99PFQTEpOOPlNZcYMC9k84DU7ieOnZZiaBvThOPJsWbiAR4r-Mxhpihjr9UoXpe17-SXQ0DMycDjr50BA8cqvarUQ9ByrH2ahqpKL4IzYq2ZX-a4ugmYH_p9DjeWc2TsmY__05JSZzfJPr7w19D3Mrs-2haVOYAMRREk3rLz4QHqV9djXJrW1o3RGulPx58mwYwgn0KWenPA2qomNLCWQFAq9m8o70CL48f3IVCXFuDIYy8JnksmRu5mNHJt0y2qyaIIuEAm07oia-8Li0LgvMF6u-SHANBtxJwhIyhnH5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تبلیغات انتخاباتی جدید نتانیاهو، مجتبی خامنه‌ای، زهران مامدانی، رجب طیب اردوغان و نعیم قاسم را گرد هم می‌آورد: «آنها می‌خواهند نتانیاهو شکست بخورد. اجازه ندهید آنها پیروز شوند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/142085" target="_blank">📅 18:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142084">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePM2hvcVlENHdZYvM1nA8TAfYxsDrj-Jnn3uCGX3uqcpRxJlNUtu8OblkLpgzM3Yl33CH4PKJugxlF000Jz3eA6MPUUO7mbQCacVsalrH9Bmv580t_k1tVtL6rP17cGROkEpGWO3oQHXCmxtZzbnFBsTstbdPnbglvdSR2Z7RrO2mADzR8n2_rbACO_ZzswefV8M0CKAfhVI933tkQbQAiqf4tVA-qOg0b5ycYQZDwyjIgBdk8SACfSGcKHCq1LQ2-OTOYHV-FEZwX1RcbEYSdO_MqVu1iVp3E3Txn_G_Ao4HtvzSVGQWxk3jF67QwwNTs0F7i0e0HXUa4ai3oDMlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کریستیانو رونالدو در گفت‌وگویی با مجله «ووگ» درباره آینده دوران حرفه‌ای خود صحبت کرد و گفت: «احتمالاً این آخرین سال فوتبالی من خواهد بود و می‌خواهم میراثی فوق‌العاده از خودم به جا بگذارم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/142084" target="_blank">📅 18:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142083">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
حدود ۴۰ دقیقه پیش، توپخانه انصارالله به مناطق روستایی ناحیه مقبانه در استان تعز غربی یمن، شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/142083" target="_blank">📅 18:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142082">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
پور محمدی: باید با تمام هوش و توان ملی از تفاهم‌نامه دفاع و آن را اجرا کنیم و طرف مقابل را تحت فشار سیاسی بگذاریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/142082" target="_blank">📅 18:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142081">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
فاکس نیوز: حملات یمنی‌ها در باب المندب ترس از ایجاد «هرمز دوم» را برانگیخته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142081" target="_blank">📅 18:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142080">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
الجزیره: ماجرای تعویض هواپیمای ترامپ بزرگ‌تر از یک تهدید امنیتی بود
🔴
الجزیره نوشته ماجرای انتقال ترامپ از هواپیمای خود در آنکارا، بخشی از یک پرونده بزرگ‌تر امنیتی بوده است.
🔴
اطلاعات مربوط به احتمال هدف قرار گرفتن هواپیمای رئیس‌جمهور آمریکا از سوی اسرائیل ارائه شده بود؛ اما دستگاه‌های اطلاعاتی آمریکا نسبت به آن تردید داشتند و ترکیه نیز نتوانست شواهدی برای تأییدش پیدا کند.
🔴
با وجود این تردیدها، سرویس مخفی آمریکا سطح حفاظت از ترامپ را به‌طور استثنایی افزایش داد و هواپیمای او را تغییر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/142080" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142079">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
به زودی جرد کوشنر داماد ترامپ با حضور میانجی گرانی از مصر، قطر و ترکیه، با نمایندگان حماس در قاهره دیدار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/142079" target="_blank">📅 18:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142077">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhwFRugiaTz5BLAoHeFjZKyaZbcLNY7KBmH8aNXypI6nleL1vFOMpqlPU28mecRDy1SWOv57kJIM5aKH94bI2R33SWU9uSBJQxfQKogcv1ToIyGpz7Cge7NQazFObP66W0Ef6vgXb1A_DhFLsvRY5LNkGO5wYrPOlHMNrouxKpxASltaqa5R2iKHDV9FziBNbNXhGQDm167LXqsTWt64AlrInAjmINwlhy52I0OshX4gNE0T8i8j0I2HqXt-kmig35ZgBKD22v5gIhqbw0KUcQsRsdaQp0wRtfu199Ukr4t-C0DA4YdTvv-T-0qq7YqrCmynP_D-eE1FhMVcVO62kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b2f47057.mp4?token=R221Y2eImMH21r6qdw_SW51Vu5oPNA9scvg6cfyLIJsoa6vNNDztqIfuZqhCHMfftaC1F-VMPHdueITDoX5S4I8N5QTEIYa8CFSheWalqjoHIjhgNfmruYTtQvlpFLSSMCKzeQcW0p2C2kdIxObTmFulgPM98dfJENONwe8mDMheYwR8smLsxv5IgiBW8KmsGh4P4TgCUv8CxhR_o5BGMra2gG31IafA7KjmzswhKyRGF78iwh5w4soAu599f7LBTofa-oVbKGzi2_UmcfiwcGQ6T1V2-vS1PwLymvErC5zZyiz-Bu74NkjunvGsPWyMNy17fcUjNPicl2EX5J4YTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b2f47057.mp4?token=R221Y2eImMH21r6qdw_SW51Vu5oPNA9scvg6cfyLIJsoa6vNNDztqIfuZqhCHMfftaC1F-VMPHdueITDoX5S4I8N5QTEIYa8CFSheWalqjoHIjhgNfmruYTtQvlpFLSSMCKzeQcW0p2C2kdIxObTmFulgPM98dfJENONwe8mDMheYwR8smLsxv5IgiBW8KmsGh4P4TgCUv8CxhR_o5BGMra2gG31IafA7KjmzswhKyRGF78iwh5w4soAu599f7LBTofa-oVbKGzi2_UmcfiwcGQ6T1V2-vS1PwLymvErC5zZyiz-Bu74NkjunvGsPWyMNy17fcUjNPicl2EX5J4YTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که 3 فروند هواپیمای آمریکایی تانکربندر سوخت در پایگاه هوایی العديد در قطر حضور دارند.
🔴
این هواپیماها به جای اینکه در کنار هم پارک شده باشند، در طول باند فرودگاه پراکنده شده‌اند، که این موضوع نشان می‌دهد آمریکا اقداماتی احتیاطی را به دلیل ترس از یک حمله احتمالی ایران اتخاذ کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/142077" target="_blank">📅 18:35 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
