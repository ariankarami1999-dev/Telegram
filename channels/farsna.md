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
<img src="https://cdn4.telesco.pe/file/vKAhHmuKGiaJsIfz-tocpheCG9EviAs4TZaesIsvofgsBi_Atx7PyJLoeuHUjIURkatKMkz2_ODDBiPJQi5_DA35J1VW-Fua2dXsi3-mY7Q3sa7gBuZaJKEWPuv2Xtxhk7-a-MsFnX9d3994GKaNvTrH_fRznFUklKsrHW4OQPYG6ioft60RGK0bnvfPvnreDBkrXb3dck3mqJl4HF0f3J9wYUAPMA6JUxNOc54MIOtlCsqKUU_bsIo624v3lsWlbsEQsQJCagE3LAQmM73hLmK8d3hXnRoz3y3LKkxS9FaRsPOVZwKiseSPBf_qRz-u36Oz9dztKb5BbQlPGHiUqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 15:56:28</div>
<hr>

<div class="tg-post" id="msg-456769">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f8a1d4d4.mp4?token=oB7YE8lM9uNqdZyj7GVC8GfBxHPp2cm5jp7x-Zmf3YjmmZhihdxdNgcsLV0136jCzFbE0e93pveQh7kyb4ZV6K28LblHUwYuHVbq-myArnRVo9xxtn0MASN8ObtZfc8vBvfjPsmj9_5hes_9Ts_S6bmO4u08ucQgzj5VTAkcMATZRJYvse44EA5cXkkkIkxLfvd42OU89wMeJvl81BXWQJosdDIfVh1AhyKyoUiANUWIj5TNGEANg1GzLFX1nbupvFnUA4gF40T5BtXVlV8MH3Grp0WZ_HNmCoz6Abypk9FD8Y2g1xHvzQokoDmJIuKHyblAX5iwIeVBPsiwn_9DsS1lvuGwI3-Lyz0PBQiL6m6RpcWDJmvsLMBgE3WAR7_0R6gLI7kTBeow-_LICh2hfzLfOP-dPHejZH2-WWBJGDtEurJbkXbEBwFN9B5a7qNzKZfpOF3FqCtJMzVDsOjCxFcIHpjMDVWynuv2we-fSxpwviMFtAe4c7jH-j6ikrr7HTdDnKAPPX3fwCc6XjyiDBBqRnBxb25KRDkdjZzHNkN5AY9Qo7M-N62Jy-AoLMdOCJrU3pOCqgRUl3WCluIx4ENqk0unEWeDEWjnPGw0efWdlfkpPU8zGuP5DDYsq_STu1Zu6fxV7b15BlOyH1B_cf3BUQro9cpkOyGgNNMBg2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f8a1d4d4.mp4?token=oB7YE8lM9uNqdZyj7GVC8GfBxHPp2cm5jp7x-Zmf3YjmmZhihdxdNgcsLV0136jCzFbE0e93pveQh7kyb4ZV6K28LblHUwYuHVbq-myArnRVo9xxtn0MASN8ObtZfc8vBvfjPsmj9_5hes_9Ts_S6bmO4u08ucQgzj5VTAkcMATZRJYvse44EA5cXkkkIkxLfvd42OU89wMeJvl81BXWQJosdDIfVh1AhyKyoUiANUWIj5TNGEANg1GzLFX1nbupvFnUA4gF40T5BtXVlV8MH3Grp0WZ_HNmCoz6Abypk9FD8Y2g1xHvzQokoDmJIuKHyblAX5iwIeVBPsiwn_9DsS1lvuGwI3-Lyz0PBQiL6m6RpcWDJmvsLMBgE3WAR7_0R6gLI7kTBeow-_LICh2hfzLfOP-dPHejZH2-WWBJGDtEurJbkXbEBwFN9B5a7qNzKZfpOF3FqCtJMzVDsOjCxFcIHpjMDVWynuv2we-fSxpwviMFtAe4c7jH-j6ikrr7HTdDnKAPPX3fwCc6XjyiDBBqRnBxb25KRDkdjZzHNkN5AY9Qo7M-N62Jy-AoLMdOCJrU3pOCqgRUl3WCluIx4ENqk0unEWeDEWjnPGw0efWdlfkpPU8zGuP5DDYsq_STu1Zu6fxV7b15BlOyH1B_cf3BUQro9cpkOyGgNNMBg2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک دعوت غافل‌گیرانه
🔹
زائرانی که به خانۀ شخصی رهبر شهید در مشهد دعوت شدند.
@Farsna</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/farsna/456769" target="_blank">📅 15:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456768">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6G04P-z-eN7Ryd9y4kvYyWURdGYH0hNgS3DVhPXLUm8jf6mienMKciKgImlQ-CqfDbsJluICQQ5RngUiK5vPiMaPPw-bBrr4X1zrpIfnbjnHO4nPEYTfltxUtc9hmpcSoBqbAXM_RG4J-ZFtOvrVaIbUFy3a6F2wWpk5RbcJH8wc5F7ZQ96Ep4Uhz-SL6YdP733DKCtt3b2JFjD019qw5VfNJSUR1GeLa4GDLFqKUxDHemGU4m-rSPxknDsPErSQQKwrbjLKYi80AgCOWjK4c9LkcqdZGOvU5EtqAm03YpW3CzpS180VEr6MlGLnpy1JY1mRZJo38ba1tGuKBzylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارکنان اورژانس تهران صاحب‌خانه می‌شوند
🔹
رئیس اورژانس تهران: ساخت ۱۵۰ واحد مسکونی برای کارکنان اورژانس استان تهران در شهرستان ملارد آغاز شده و در پروژه‌های مشارکتی دیگر نیز هدف‌گذاری برای ساخت ۵۰۰ تا ۷۰۰ واحد انجام شده است.
🔹
در پرند نیز تأمین مسکن کارکنان درحال پیگیری است و تلاش می‌شود پروژه‌ها حدود ۱۵ ماهه به پایان برسند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 340 · <a href="https://t.me/farsna/456768" target="_blank">📅 15:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456767">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSGV_ZaMC8LVCdwPft70S6aYlkRTUieXCo5NfOXVcWO9Q2HCikamt4GbUp2KBkxwQn9VQ-eW3IRQKvCZ52Qdav7n-nUNT7BgyhCm-AW5ykTrDx4RNKvfH596-8SWMwtoJR-2YlQUnKwaGh1ofbCsgEHBlHAcX1ui3gvoge-ptkJ4pDYq6P_fY99XPXRTIlXGb8cShxqi02_IUacV9p3EcF-rAwFsXah6os5G3H9y0Mo5SAnaixnXknGh274WVEsc9bpxt_ITI3z5f5sHSjld6_4TNksFmEaAVKeLaPhXXS-ThgjYYMHGsE1txhnOumQ9HRwgwQRfrGXVutuM5Pi0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صلاحیت مدیرعامل پیشنهادی هلدینگ خلیج فارس احراز شد
🔹
براساس نامهٔ سازمان بورس و اوراق بهادار به مدیران هلدینگ خلیج فارس، صلاحیت حرفه‌ای حسن عباس‌زاده، مدیرعامل پیشنهادی جدید این هلدینگ، تأیید شده است.
🔸
پس‌از لغو مجمع قبلی این هلدینگ به‌دلیل غیبت نمایندگان…</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/456767" target="_blank">📅 15:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456766">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff225759e5.mp4?token=NpXrzrxM5KnmNYtiIK0FAN4vQaDuWnqjvAiHHJszfvLSbxxWeDpypg_09RkF7rYVh9lC0a4ojGKHk0Cdcd7FibaEWh-t6j5OocDIMaSqayRzbnmUlCCa45K96GKVwMcdMNMoS7BGaFcUa9C5mOvJThdSnNOH80wF-uZu3PJRtjYBK0f26oOekojxaygYpU955N_LhQaFsYQ-WlPom5aES2LWTixnhFV_igvjtn1Sal9BL8f61ZP-pSJ3zs0tiHSrzyNa6bBvcJUvKHiVIEwvvdFtJYN7ePK7prnamjXZQe-96m5nCypQrZnQmS72sKelTmBJ4_H-UyDHFbXQCmGlIFGk40Tn3QuETP6F6wtgBAb5L15Oj5U62Vew1pwo87CSw5iMwNl65qNr_Sd5KeQ9BmwpStpAhFoKy6W1v-K_H51LQWZdtDidbzZz1zLGLk6OpUQ1WvUcYfWcIF6FkSs-Ckgs4E73R7r0fq3iM-ICvcMjlvABIs9AGScu5XIUFi8OafG0PHFJtMV6heURntBp1p_tDuBedM8gyUGbnb2916XAgy1aGTs2X6zGKPOORCTDfhMk3ZXY1hq7xY8WbMREjq2qjXZjncGcgnb8-sWD07TOH_tNf5QNpcQkW8OOQPZaFR9bHWoyjtId11b7yCPWR1T1OFoXxsBXL24b7fwLJP0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff225759e5.mp4?token=NpXrzrxM5KnmNYtiIK0FAN4vQaDuWnqjvAiHHJszfvLSbxxWeDpypg_09RkF7rYVh9lC0a4ojGKHk0Cdcd7FibaEWh-t6j5OocDIMaSqayRzbnmUlCCa45K96GKVwMcdMNMoS7BGaFcUa9C5mOvJThdSnNOH80wF-uZu3PJRtjYBK0f26oOekojxaygYpU955N_LhQaFsYQ-WlPom5aES2LWTixnhFV_igvjtn1Sal9BL8f61ZP-pSJ3zs0tiHSrzyNa6bBvcJUvKHiVIEwvvdFtJYN7ePK7prnamjXZQe-96m5nCypQrZnQmS72sKelTmBJ4_H-UyDHFbXQCmGlIFGk40Tn3QuETP6F6wtgBAb5L15Oj5U62Vew1pwo87CSw5iMwNl65qNr_Sd5KeQ9BmwpStpAhFoKy6W1v-K_H51LQWZdtDidbzZz1zLGLk6OpUQ1WvUcYfWcIF6FkSs-Ckgs4E73R7r0fq3iM-ICvcMjlvABIs9AGScu5XIUFi8OafG0PHFJtMV6heURntBp1p_tDuBedM8gyUGbnb2916XAgy1aGTs2X6zGKPOORCTDfhMk3ZXY1hq7xY8WbMREjq2qjXZjncGcgnb8-sWD07TOH_tNf5QNpcQkW8OOQPZaFR9bHWoyjtId11b7yCPWR1T1OFoXxsBXL24b7fwLJP0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: حامی اصلی ما در مسیر مذاکرات، رئيس‌جمهور بود
🔹
وقتی آمریکایی‌ها درخواست مذاکره را مطرح کردند، پزشکیان معتقد بود باید از همین طریق راهی را برای پایان جنگ پیدا کنیم.
🔹
انتخاب قالیباف در تیم مذاکرات به‌پیشنهاد رئیس‌جمهور بود و حتی در صورت‌جلسه‌ای که تهیه شد پزشکیان اصرار داشت که «باید نام آقای قالیباف به‌عنوان مسئول مذاکرات نوشته شود تا من امضا کنم».
@Farsna</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/456766" target="_blank">📅 15:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456765">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05cb6edf7.mp4?token=LKoZ9r0YswGfZZ8PLQXimGovCdDIm0b2tFCy2tUWgR1N5jkhQRhqRX5IW-Z2f4PPvbb3becwcS64znQZwvPs0qt6Q7VXJqoDKlmAG4ZAgVUaPyXzJlS6wxJsf20h6mP9F1UOdDpGRSs4FBpC5ZWmp90xaKZrViGkDIKkOOtjCo4zJj65AWqA33UvfACeqW2vQQC5K8ubyMkZjEayi7VZyER29zkvL_i_ilRAVPYTmA1HmgUIa-VwVRPO5tF-XA-R9w-VdPcS4HYBKVXvr-byeINd2LOBPe5i4SC4UcKiri9boen1V-LqRu2r0g4vMNIv2C_UVZ2K1rtlZ8aQM2Z9_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05cb6edf7.mp4?token=LKoZ9r0YswGfZZ8PLQXimGovCdDIm0b2tFCy2tUWgR1N5jkhQRhqRX5IW-Z2f4PPvbb3becwcS64znQZwvPs0qt6Q7VXJqoDKlmAG4ZAgVUaPyXzJlS6wxJsf20h6mP9F1UOdDpGRSs4FBpC5ZWmp90xaKZrViGkDIKkOOtjCo4zJj65AWqA33UvfACeqW2vQQC5K8ubyMkZjEayi7VZyER29zkvL_i_ilRAVPYTmA1HmgUIa-VwVRPO5tF-XA-R9w-VdPcS4HYBKVXvr-byeINd2LOBPe5i4SC4UcKiri9boen1V-LqRu2r0g4vMNIv2C_UVZ2K1rtlZ8aQM2Z9_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میناب؛ جایی که یک تار مو، روایت یک غم شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/farsna/456765" target="_blank">📅 15:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456764">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DptkksoK5AYhNCgA-FcOeIAyq1Zt7UBeGm8NAuh3uHQeklvipJa0S88c1lX14O88CBc9-1IN_KVMgzshHvDD_FavACmlrAZWJyUoHFV1M823-3MD1oICQ_h7aPioHWsSOGDvgdpeJvcTLT_dTj0DVGTn1BgliIFNWwdsTlZ3fVIX_3Satl93t1HjDoukTi7NEkx4pAy2fj5hEpt5SNZxSoU8SzgjL0ix9pH9wtQezuqtgzup3gLxiKgWtnXeFt3rKQVe_BHizY9ickUeMqyz3SmK8EUmUYJgWYlHD5smiVD507ICRBApX6GKgVJkaPVXAlcqmoh2bdopJS1YF3iGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرایهٔ نفتکش‌ها در هرمز ۱۷ برابر شد
🔹
درحالی‌که هزینهٔ اجارهٔ نفتکش‌های غول‌پیکر در مسیر خلیج فارس به آسیا در شرایط عادی بین ۳۰ تا ۴۰ هزار دلار در روز بود، گزارش امروز بلومبرگ از ثبت رکورد تاریخی ۵۱۰ هزار دلاری حکایت دارد.
🔹
بلومبرگ دلیل این افزایش را نتیجهٔ مستقیم تشدید خطرات امنیتی ناشی از عبور از تنگهٔ هرمز اعلام کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/456764" target="_blank">📅 15:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456763">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r64t6Md8TuxjbVCNdP1Yt-E0rWceYTRPaXsN-v9SBIlaNjmJUc0sNfEWs6Ca6mzCQQCUTTPxP_LgvvJ9dzr8AhQb30bRFN4a3xNL2W2StGAXDWc1xOvZoBMEaKLGTJpnXvSYBejWKNKbxP47VdRT7eo9IYOtmYX8x_p65EDdxEQM22_5Dz92_8wCZaDM3DkHcKVRxZoGiUSXoC8aFwAfU8bfxlY58Qu_69OAgdW5KWWeWDaMoMoJpn-KLPMJ80MZzatzwcCPAva5pn0xav79xJj50-6dipmoc8xc-3R1Uf_6qRAb2crLAPdwTeV1esyup7GdwiDEuuNIueChWjwkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: کالاهای اساسی را ۲۵ درصد ارزان‌تر می‌فروشیم
🔹
براساس بررسی دانشگاه تربیت مدرس، حدود ۵۵ درصد خرید در حوزۀ مایحتاج عمومی از میادین انجام می‌شود. همچنین قیمت برخی کالاها در میادین حدود ۳۰ تا ۷۰ درصد پایین‌تر از قیمت پیرامون آن‌هاست.
🔹
در شرایط فعلی، گوشت عرضه‌شده از طریق میادین حدود ۵۰۰ هزار تومان زیر قیمت بازار است و هدف‌گذاری ما این است که این فاصله را به حدود ۶۵۰ هزار تومان برسانیم.
🔹
در کنار گوشت قرمز، در حوزۀ برنج، حبوبات، مرغ و تخم‌مرغ و سایر کالاهای اساسی نیز می‌خواهیم نقش‌آفرینی کنیم.
🔹
هدف‌گذاری ما این است که بتوانیم قیمت این کالاها را حدود ۲۰ تا ۲۵ درصد نسبت به شرایط موجودبه شرایط موجود کاهش دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/456763" target="_blank">📅 15:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456762">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
🔴
حملۀ دوباره جنگنده‌های اسرائیلی به فرودگاه نظامی ابوالظهور در سوریه
🔹
منابع عربی از حملۀ مجدد جنگنده‌های اسرائیلی به فرودگاه نظامی ابوالظهور در ۷۰ کیلومتری مرز سوریه در استان ادلب خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/456762" target="_blank">📅 15:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456761">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb764cc465.mp4?token=Ke767yPs3awYHSI-UuTKWtjicuOvjm_mkYfX6v2vQRq7uxJmlKrjf6QpRa6oH9wIsI-pfqreEZMSFjwSKcx2Ff-e9ZspaWtX_qErUeguz1es3UnQi1qoZww-vFnZ8NN2NqjxjCEBPS4Mw6rz25Wz692tsAT9d_ktTEt4Wr-KD3H15xVDcwxJUQGzcv_IXm7L9XXlZLyRzq0Ym5Own43VOON1C8vNTMarstFBdKjPwiU4xohSVAwa10ALP1k-2faNrUHNrheIfFfbdkeZf6g52yHKrNHvsvjNaSdUcV0DjO68nLw8Pw25IJxZxkU5TMMPLuvON3QSIBsGWl3dh_d0nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb764cc465.mp4?token=Ke767yPs3awYHSI-UuTKWtjicuOvjm_mkYfX6v2vQRq7uxJmlKrjf6QpRa6oH9wIsI-pfqreEZMSFjwSKcx2Ff-e9ZspaWtX_qErUeguz1es3UnQi1qoZww-vFnZ8NN2NqjxjCEBPS4Mw6rz25Wz692tsAT9d_ktTEt4Wr-KD3H15xVDcwxJUQGzcv_IXm7L9XXlZLyRzq0Ym5Own43VOON1C8vNTMarstFBdKjPwiU4xohSVAwa10ALP1k-2faNrUHNrheIfFfbdkeZf6g52yHKrNHvsvjNaSdUcV0DjO68nLw8Pw25IJxZxkU5TMMPLuvON3QSIBsGWl3dh_d0nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد خونین معترضان حامی فلسطین مقابل سفارت اسرائیل در واشنگتن
🔹
معترضان مقابل سفارت اسرائیل در واشنگتن تجمع کردند و با ریختن مایع خونین‌رنگ، قراردادن قبرهای نمادین با پرچم فلسطین و نمایش تصویری از نتانیاهو در حال رقص بر خون، خشم خود را از جنگ غزه فریاد زدند.
🔹
پلاکاردهایی با جملات اعتراضی مانند «اسرائیلی‌ها کودک‌کش هستند» و «اسرائیل! دنیا از تو متنفر است» هم میان جمعیت دیده می‌شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farsna/456761" target="_blank">📅 15:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456759">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXKo7fEp9mE6CeM2TR9WW6ohNpfwryrXyNBEehvHSJoP45ipWGWoP9iCcLfyQKaEMkyfmOEyMsLP1unpoDWDYstBDkSPx59uW4yAToZK1lGtehzm2NMhEI00VT-8oKG5LGjHCcteS0irzWI07yhOVB06VvpY7xz6fQxsdD46ibrRyOEsyLF6Wk3ZlIF5AT24_vC81eWQ9bf3lXwz-2H7mnpQkK2c4xTI3V0NX35rgXUhDHDVCFy0hUaS1Ebq8ELJnhRXLAJbqj_iObyrVAJLfjpZXo_KB47FcS4_MbQc9sz-MJvD1kRYhxWJUMTmU5EXwd_E6W7vipnBR4LA_p46LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ترامپ در ادامهٔ توهمات خود، تنگهٔ هرمز را قلمروی آمریکا خواند.  @Farsna</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/456759" target="_blank">📅 15:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456758">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4WthOmq2qD6dgGyITPbRXiBd0JTm8l9-fwaXp11hmB_w51UHrOYZ6YgEVf6TnXZxHqsnm-oKCkpcOnrxqGea-FkycPmCjg4r1eqDvZfkeWXRkaD6B8zgTBwq387Fci2oOMnYYAONRE5WzxVk1mWP8H25uU6AobpmAYTLmlvzgRDyiPznFqmdo-5pgNc0HdEqhsmzhQTVjNkvHHv-KoHhNFG4ooQLvPVi6R67-0Q3NcZIqHHMzVKhhEnxWY9IN2iLlkrWEV9F-ZOeH0Y9MXUQrHQHRB4leiHGGDRl3uuyImh8xYVNtNZL4yvLhp3SckAz2hwe3ff7QnZQVguw4DUAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: من از ایدهٔ اعلام تنگهٔ هرمز به‌عنوان قلمروی آمریکا استقبال می‌کنم.  @Farsna</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/456758" target="_blank">📅 15:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456756">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8126c9cfc.mp4?token=QQ8M2G6r1dFrd6YDpgj41tx81IDWNm09SloxyQxnVcLDNWSOtfQlchWBsBmjdwo2uJqnxIfRpdHHK57XsWB8Wk_09ucrZemwuf5eIjyvvhCGA1Q7Zzil4XQSovsg4CzgHiXU8sqkQau-TLO_zMNB8uo_X0sUSdJ0ax7fBu5Evno4c2DUHenxmQXcE7M537SOl0vDguy9sTT1k0KHL4Lg4Jl09XDIhh6ZCD0XV-zPw8i4pUkjPVS-IbQNmUM7tnBAUiGWj3OIhGfD9sRVP4FOxlQo20AGAeoQlVsaciCkTVD4bW2lAm8bthxf3P_DMuGmu-9U7TG9ueUhhrmX3RJUuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8126c9cfc.mp4?token=QQ8M2G6r1dFrd6YDpgj41tx81IDWNm09SloxyQxnVcLDNWSOtfQlchWBsBmjdwo2uJqnxIfRpdHHK57XsWB8Wk_09ucrZemwuf5eIjyvvhCGA1Q7Zzil4XQSovsg4CzgHiXU8sqkQau-TLO_zMNB8uo_X0sUSdJ0ax7fBu5Evno4c2DUHenxmQXcE7M537SOl0vDguy9sTT1k0KHL4Lg4Jl09XDIhh6ZCD0XV-zPw8i4pUkjPVS-IbQNmUM7tnBAUiGWj3OIhGfD9sRVP4FOxlQo20AGAeoQlVsaciCkTVD4bW2lAm8bthxf3P_DMuGmu-9U7TG9ueUhhrmX3RJUuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسفالت‌ریزی رودخانهٔ الیگودرز متوقف شد
🔹
مدیرعامل شرکت آب منطقه‌ای لرستان: عملیات آسفالت‌ریزی بستر رودخانۀ الیگودرز که بدون هماهنگی و دریافت مجوز انجام شده بود، تا تعیین‌تکلیف فنی متوقف شد.
🔸
شهرداری، دلیل آسفالت‌کردن رودخانه را تجمع لجن، زباله و ایجاد بوی نامطبوع اعلام کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/456756" target="_blank">📅 14:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4IrF16i8rt28_AoPAraXMWWQwzVtyhU8vbcbNdIw_8WjVN8r6f0O1gN0DZDy9jZ74sEhzMmI8nGqf2yJ3MSbm_YmEIz5ARUmD4rm0NCWftIpPc8ZPrTr5K7c98_c4ysK75vPiD0LC2bewZqe9846O02woEu-lGR9G-SwsyAT3YxaariAmiOfyWRgAvQ6ASjrjZk8u3bW_5p5wdpdhaxLCqoXFWORDCNJ0vDKfsJ9RYklyh47RyaAPAlhoiQURZGn390wC-zHFkSS0PXPpXlTRztykhsK-XZ2PYqkeRoqNTSfGzTMQxJO8srC3IdqKguqtwAGgXOw19EoTrpUTCZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjwP3risVGFvYIurCQrKEf34Qo5dqOZ692D4w9CH7sJZLnpDx8T9zFv3OUEcNADbXAPjG-Bm97drlih1RBvOj07eZPilO9jXNXtIJfQ5Ip5ZqdUxv2OykrzuQ0zeyZPYZVpv68BtokPHcJNgaO-lcuU6iQpZShiP30zEJgMWkXK1skczOlcm-3rqvnmrJiFJGv6d36DtJskgq4z9iB2a6VLr60WN8804Gr4RuVSGvhPFxow2ziEIVDX2ABmMdoQwZxm9HuJqdRFtt7pCK6hb765dNxhDAEUHYZFsIg7k8m77cn3f0wvoKY9lqw2kN4xhZSg0W2eKgKlrFPAh_E1L5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
حملات به فرودگاه نظامی سوریه؛ اسرائیل مظنون اصلی
🔹
برخی منابع سوری در خبری تائید نشده گزارش دادند که هواپیماهای رژیم صهیونیستی به باند فرودگاه نظامی ابوالظهور در استان ادلب حمله کردند.  @Farsna</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/456754" target="_blank">📅 14:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: تا زمانی که وضعیت خلبان‌های ما در قطر مشخص نشود، ما آن‌ها را اسیر می‌دانیم
🔹
ما از ۱۱ اسفند پیگیر سرنوشت این خلبان‌های شجاع هستیم و از ۲۵ اسفند با صلیب‌سرخ هم مکاتبه کرده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/456753" target="_blank">📅 14:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456752">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e58796c61.mp4?token=ElBW8zLnjaNLprVpx9xbRBN9Qfvn-a56cJvyp-dk1FpYh0po-TSOpN2XQ4LX_Enr-m5gui_jDJ5eeXPdyKPL4sIUqVzDnSaiy7c8qXCfhzlsUI4QKoeuU3ZlqGueDek4YsQ3riGfEFUxm_6WNJ5pkZPhRwCynJlOJRNR4MFxRnQvR7PKRY53mDXgwl2K02PbuC6lUYdMDtHcyONXv81xtQkl1-yq0Ij09M9rgsDkOLP-Tbr5C5znPInt7mv0iaCZBVOgko2eLZBp6ARAaMi2pBeYJhp5FH9zpeC_WZAGaMmw8TciYpVX5utdflma6_ksfirPlCW_VhH71Y-3sr8wxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e58796c61.mp4?token=ElBW8zLnjaNLprVpx9xbRBN9Qfvn-a56cJvyp-dk1FpYh0po-TSOpN2XQ4LX_Enr-m5gui_jDJ5eeXPdyKPL4sIUqVzDnSaiy7c8qXCfhzlsUI4QKoeuU3ZlqGueDek4YsQ3riGfEFUxm_6WNJ5pkZPhRwCynJlOJRNR4MFxRnQvR7PKRY53mDXgwl2K02PbuC6lUYdMDtHcyONXv81xtQkl1-yq0Ij09M9rgsDkOLP-Tbr5C5znPInt7mv0iaCZBVOgko2eLZBp6ARAaMi2pBeYJhp5FH9zpeC_WZAGaMmw8TciYpVX5utdflma6_ksfirPlCW_VhH71Y-3sr8wxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نجات یک بزغالهٔ وحشی از چنگال سگ‌های ولگرد
در سمنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/456752" target="_blank">📅 14:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71756005fa.mp4?token=dlASkjivlsA6I6-AK0bkJ_y9Fe25j5o3ST5MSe1eRXHlWRC1g583IoEHIPzbq8zhKWAT4fcaNl3glAL3oJtWNqkOOHAM3-cLsdk84Ym1oWrXbzFIRR54JFRbgtTddYj0JOd0kKK6I7Jh6M6CJtDt4yPa_p1OjmboHmJHTycIIheizJBqznjVkW7ZdMJFBuAVNdwOwVpX-bqEQqJ1mMPQ63TN-kbc-PfIv_h0W7BIMAzfVYzaqiKZgJGIyQdtDfCIAS6GTDcej7Q4kZ6g4eGqZX0uG1Dv9l1yotdOHyrPAmDGlrw94OvWPUKm-2CD9TRwPDJ7RoFzP_vPAEiJjeof6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71756005fa.mp4?token=dlASkjivlsA6I6-AK0bkJ_y9Fe25j5o3ST5MSe1eRXHlWRC1g583IoEHIPzbq8zhKWAT4fcaNl3glAL3oJtWNqkOOHAM3-cLsdk84Ym1oWrXbzFIRR54JFRbgtTddYj0JOd0kKK6I7Jh6M6CJtDt4yPa_p1OjmboHmJHTycIIheizJBqznjVkW7ZdMJFBuAVNdwOwVpX-bqEQqJ1mMPQ63TN-kbc-PfIv_h0W7BIMAzfVYzaqiKZgJGIyQdtDfCIAS6GTDcej7Q4kZ6g4eGqZX0uG1Dv9l1yotdOHyrPAmDGlrw94OvWPUKm-2CD9TRwPDJ7RoFzP_vPAEiJjeof6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تایم‌لپسی از حضور مردم بر سر مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/456751" target="_blank">📅 14:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456750">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/recuqXe_tcppeHw2q353Wng8aVGgdiOXRaNcma0IDWyUP3kgagP5wtFkXNX6snRbNHwVRKhIhcTgLQizxZdPMVgBtsaVKo4ES8QKvHxmVLgKXkJ3rmjM5_DrEb7tbegaEmGjVPVGYBjfSljDbvJycXQsr2Lst8mTfbhmCORIFK5Bkcl9qcChcEK_zRzfmI5xKdZltn5aFdXccq_0i4O3XxLcRlvvIZGjymbaWlYG7iwvExgVTDQFzVrNhAmhO-ntB0jxavpfwkhg019vyuMrBwvPUhzpX62u8mQPfQC64s7MTdUVgZtAaGeMY1l89jXcZaORnGGaxo68eCmSwvx5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
صندوق تضمین غیردولتی مهرگان دی شهر؛ گامی در مسیر توسعه تأمین مالی
🔺
مراسم رونمایی «صندوق تضمین غیردولتی مهرگان دی شهر» با حضور دکتر سیدمحمدمهدی احمدی، مدیرعامل بانک شهر، مدیرعامل گروه مالی شهر، مدیرعامل بیمه دی، برخی نمایندگان مجلس شورای اسلامی و جمعی از مدیران و فعالان نظام مالی کشور برگزار شد.
🔹
به گزارش روابط عمومی بانک شهر، این صندوق با هدف تسهیل تأمین مالی، کاهش ریسک اعتباری، کاهش وابستگی به تضامین سنتی و تقویت پیوند میان بانک، بازار سرمایه و صنعت بیمه فعالیت خود را آغاز کرده است.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/456750" target="_blank">📅 14:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456749">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نیروگاه خورشیدی ۱۲۰ مگاواتی منطقه آزاد ارس در آستانه افتتاح
عملیات اجرایی نیروگاه خورشیدی ۱۲۰ مگاواتی ارس تارلا امین در منطقه آزاد ارس که حدود یک سال قبل آغاز شد، این روزها به پایان رسیده و آماده بهره برداری و اتصال به شبکه است.
#روایت_توسعه_ارس
#منطقه_آزاد_ارس</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/456749" target="_blank">📅 14:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456748">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/456748" target="_blank">📅 14:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx2C3UNb1qF0wslAFnVGck4DnGqhME0Wwou-NUr7FkegZynQsPigIthFJyMDiInQd_H01JNcPof_s8cr1WtrNHhIfqWqN9PxYueKePQ76xqxtl7iSd9GSnDQs2b2ufrFF8ENIyRIXKYAFwV0CWGjv3MobLKwU7SxnSyHmyXc8DkyIskvT9c87QnxtApN6spnvNB8NQDYNq2EjRXIt4PdYIsCHsMnu5nz5e3KDbY65ElO-8rw1TfHIXQiUjEP8stZ7jqCv2ae2UFKiD_lO7djYadwy1Vg5Xcqt1RJIqNGtt7iHWPnaOcQsGuGaThfl1JdtEw7tLDJMU-BapgiY-XkYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارس جنوبی برای گاز زمستان سرپا شد
🔹
سرپرست پالایشگاه اول پارس جنوبی: تعمیرات اساسی پالایشگاه اول به‌پایان رسید و برای تولید و فرآورش پایدار گاز طبیعی در فصل سرد آماده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/456747" target="_blank">📅 14:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqgQAtHpM1sfFVDdB9My6TWUMzO5tqW0k-70Xnd2VdhbfC9WRvnB0fzEJvw0dhxj2-Sr4ZpH4u8oZhxYGCIQApYjblI3-U1CtprYUphUSbFWvt3bWxfwAm3flnbABmTCCDMU74BFwEynUKKfddfUy8MSEiCyiHKtMm5-q6YzIvBFCxTZlftzemA_a-W2Ic0--6oQXRbjN0y8WuyADaQwWxtF71eyJd0SAsXAxKHeLE5C5I2QqWbLnep_6tbzOQqZV6eiWZbhqipe6f7xkF6vZFpMbj-vDwlAjYWj79DmTp00qbp8X0_nAIyKkgZLzeZI2Qk6WbQEx6EJ_1rNcw44rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موافقت وزارت صمت با تخصیص سهمیهٔ واردات موبایل
🔹
درحال‌که واردات موبایل از ابتدای امسال متوقف شده بود، رئیس‌ گمرک امروز گفت که وزارت صمت روز گذشته با تخصیص سهمیهٔ واردات تلفن همراه موافقت کرد.
🔸
در ۵ ماه ابتدای امسال یک میلیون تلفن همراه به کشور وارد شد؛ اما در مدت مشابه سال قبل بیش‌از ۳ میلیون تلفن همراه وارد کشور شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/456746" target="_blank">📅 14:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06d1ee0268.mp4?token=GRPCa3rCNQgb_0g3xAiLH78nMdTNjqjvbG2emJfGTamzUmFRin7OewDy7QfwiHAtDKnOcUq3QbQBxqvxq1up5urWHK7izwN9AELC2UtXIYuhoBthB3xFkKWykGngp0pQVf95Z_PgeN5_SILB6ZA2HV4Sm8tNOOot5HU_I1jld52yNPxvP2slu_MW72RH7Yt8eQ2_vPTu6KpnhvpV5iXKVwM0J1SpHF429iL29X14WcCywwblfqVDYrfP_Zbg9J5IAaMBnspm6Ep1YZIsJlrdgPKAfsXYQpl8UJqHoQGkBmeNy3GsYji07pFrZoJmEPYkVLwBXpsYUQW1njlxXdFn_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06d1ee0268.mp4?token=GRPCa3rCNQgb_0g3xAiLH78nMdTNjqjvbG2emJfGTamzUmFRin7OewDy7QfwiHAtDKnOcUq3QbQBxqvxq1up5urWHK7izwN9AELC2UtXIYuhoBthB3xFkKWykGngp0pQVf95Z_PgeN5_SILB6ZA2HV4Sm8tNOOot5HU_I1jld52yNPxvP2slu_MW72RH7Yt8eQ2_vPTu6KpnhvpV5iXKVwM0J1SpHF429iL29X14WcCywwblfqVDYrfP_Zbg9J5IAaMBnspm6Ep1YZIsJlrdgPKAfsXYQpl8UJqHoQGkBmeNy3GsYji07pFrZoJmEPYkVLwBXpsYUQW1njlxXdFn_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز توزیع کارت کنکور ۱۴۰۵
🔹
داوطلبان کنکور تا چهارشنبه ۲۸ مرداد فرصت دارند کارت آزمون خود را از سایت سازمان سنجش دریافت کنند.
🔹
آزمون تجربی صبح، هنر و زبان‌های خارجی بعدازظهر پنجشنبه ۲۹ مرداد، ریاضی، فنی و انسانی صبح جمعه ۳۰ مرداد برگزار خواهد شد.  @Farsna…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/456745" target="_blank">📅 14:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456744">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1fc6ea396.mp4?token=MsvEerk9P2TWlPoU7u8zFw0gNlFA1htqSxfsJNxadDamMgcZbwj7OJHt7gkDPlHrAzjxqLJsj8uSEsCnRDulNlKQgENOwMhPUiHOohq05zw2r4j1FB9jI0aHW1jWOCF-Z9DQE8m1IDHH8wGzCx0A30B_KUoqwN1TbwTXEb4oRUkgAKbyV315WP4l1RmCT9OwcxARf74FVBd81Pyn4fpw-tRRPWnh5vxw85SUULtqRR0tRWjFwlfZnicilOHXD3s6OuHIbPOVdqBXQRk1pj1v0N0aE60bSOIGzmDGDTLxHk1ZUKPiafsgwyvQBwCdGTmVPg8dPvC8OXUX_hUYvtCAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1fc6ea396.mp4?token=MsvEerk9P2TWlPoU7u8zFw0gNlFA1htqSxfsJNxadDamMgcZbwj7OJHt7gkDPlHrAzjxqLJsj8uSEsCnRDulNlKQgENOwMhPUiHOohq05zw2r4j1FB9jI0aHW1jWOCF-Z9DQE8m1IDHH8wGzCx0A30B_KUoqwN1TbwTXEb4oRUkgAKbyV315WP4l1RmCT9OwcxARf74FVBd81Pyn4fpw-tRRPWnh5vxw85SUULtqRR0tRWjFwlfZnicilOHXD3s6OuHIbPOVdqBXQRk1pj1v0N0aE60bSOIGzmDGDTLxHk1ZUKPiafsgwyvQBwCdGTmVPg8dPvC8OXUX_hUYvtCAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی خواستار یک‌دهم ذخایر پدافندی آمریکا شد
🔹
رئیس‌جمهور اوکراین: کی‌یف امسال ۲.۵ برابر کمتر از سال گذشته موشک‌های رهگیر دریافت کرده. یک‌دهم از ذخیرهٔ فعلی ایالات متحده برای متوقف‌کردن حملات موشک‌های بالستیک روسیه کافی است اما ۵٪ برای گذراندن زمستان اوکراین…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/456744" target="_blank">📅 14:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bce769192c.mp4?token=A6JcKb3LIQ-RSFTQHkb2DTxtr-X1inrjApL0y9eJZiE3eh7L9UBAGTfbnDfLsrnCKmZmPSsU1ea2MAKZ7p04AIkQ_ysgrPtKxqEMQ5E3itzSuD7D6rM4xG-tzWu7AE0u2qVgtURPJjm_OxBZwF-sWUixfoYzD8c_kAIppE6ZOZRnAS7kDgDaUW8859TbV_2aWCFbDKJC9sdbJGCZeXcNm8le4sMdbCMim5cwKrNl78gH55yIGP-35sFIaQCHRLYMHplQZmd4fbojSZdJ4CowxZLfvd17b5wLvI0AdpoLljGV9IueYa6ZE45YBK3OWkeD2zW2r_kRxprIsn27HxTk0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bce769192c.mp4?token=A6JcKb3LIQ-RSFTQHkb2DTxtr-X1inrjApL0y9eJZiE3eh7L9UBAGTfbnDfLsrnCKmZmPSsU1ea2MAKZ7p04AIkQ_ysgrPtKxqEMQ5E3itzSuD7D6rM4xG-tzWu7AE0u2qVgtURPJjm_OxBZwF-sWUixfoYzD8c_kAIppE6ZOZRnAS7kDgDaUW8859TbV_2aWCFbDKJC9sdbJGCZeXcNm8le4sMdbCMim5cwKrNl78gH55yIGP-35sFIaQCHRLYMHplQZmd4fbojSZdJ4CowxZLfvd17b5wLvI0AdpoLljGV9IueYa6ZE45YBK3OWkeD2zW2r_kRxprIsn27HxTk0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سالتوی تماشایی فرنگی‌کار ایران
✔️
علیرضا محمدحسینی دارندۀ مدال طلای جوانان آسیا در وزن ۸۲ کیلو در نخستین مبارزۀ خود در رقابت‌های قهرمانی جوانان جهان با اجرای سالتو بارانداز موفق شد ۷ بر ۱ حریف خود را مغلوب کند.
@Sportfars</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/456743" target="_blank">📅 14:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4745022f5b.mp4?token=Vujwlcc34WmPdoGadsI26-cAZkVV1iJK3pdf-eHAAVSWzxfNs6bHeQZqgsQj6suYE8EWKUZAQbQ9-skedxNpNc3VKyfZoreiRUB82l_sXrCCJF8tGqQrQlcQSI0NaHFWxXPT42DYhYsKjxdtbcMuux6PFhNZoVl5xIQ4lq7ENz0MQVr4KHcMJiUtGwFI22OvnluIpIYpvl-SnSIT2s86FmqZPEEKDKelb0xR4WBa0ruAPSUSWPFd0mnqNbb9A2liqkYBYvj_nZWRirK4V5bBYp81r7le5GYS-HTHsBNs_3WbKpNf3hZWtUk5O2QP_AMKUd5tY89mpaPq3FjESCnCZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4745022f5b.mp4?token=Vujwlcc34WmPdoGadsI26-cAZkVV1iJK3pdf-eHAAVSWzxfNs6bHeQZqgsQj6suYE8EWKUZAQbQ9-skedxNpNc3VKyfZoreiRUB82l_sXrCCJF8tGqQrQlcQSI0NaHFWxXPT42DYhYsKjxdtbcMuux6PFhNZoVl5xIQ4lq7ENz0MQVr4KHcMJiUtGwFI22OvnluIpIYpvl-SnSIT2s86FmqZPEEKDKelb0xR4WBa0ruAPSUSWPFd0mnqNbb9A2liqkYBYvj_nZWRirK4V5bBYp81r7le5GYS-HTHsBNs_3WbKpNf3hZWtUk5O2QP_AMKUd5tY89mpaPq3FjESCnCZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: تغییر شیوۀ‌ کالابرگ یا افزایش اعتبار آن ضروری است و باید هرچه سریع‌تر اجرایی شود
🔹
هر فرد یا دستگاهی که با گفتار، رفتار یا تصمیمات خود، باعث نارضایتی مردم شود خواسته یا ناخواسته در زمین دشمن بازی می‌کند.
🔹
مهم‌ترین وظیفه‌ای که ما مسئولین کشور خصوصاً…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/456742" target="_blank">📅 14:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOfJvrMtB-cJOW9AoYrr3dmVU94pcg4oVKcgG6170xinSTkWr9yBUQjXPsqZuQ4ZL76DOOkrHYovlmNBqjVXb-5q4oJtX0pgXJgxTCTrZiG1drhLq1unrRN2w7xeCxnoSOu2RpzP5g2dqzsSJkvmS5NBSG4yNnVLLW-inA2f5WI7cBZkvHMp1AY-b25nzq5VKqfGd95rvSzAXstgrM5T4anJznRgjkNEZjgIznm_RTgos9bLfedzhXlaxHMj_kk28Xq_EDoIPa0apPWsnT3JPNbli2tephU_p2o6zxkYtHJisP1HYlZB7X_NCoyPiIUBMKwHy4KLrD_aAHK-c33QIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۳۴۸ کيلوگرم مواد مخدر در آذربایجان‌شرقی
🔹
فرمانده انتظامی مرند: در یک در روستاهای اطراف شهرستان، ۳۴۸ کیلوگرم انواع مواد مخدر کشف و ۲ نفر دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/456741" target="_blank">📅 14:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbDMd-dIp1HlR7pNE9sXPRsudxmUGcqbERAX5xhbLjQn_3WfydgPA8U4r0Lp7LRFal8NVKvl7Mco2lBOSpkoMc4y9BdjTdPHKgScB6GUMjZ54OQx4QbCg0CkrxkhqtzwrfzsV--5aSOE9Nj5AIMQVImDEJTL3wc3b5_EsPsWftFL7Fsc5N0SJfr4dEZVvlk65Exj9BaMsZuClnEZH7WgemzprnUeHE_nv7qYUJDjjJ2ynOW9_nAhAL8HNcn5_gyAjWx2ZmnmuNETDRUFSMaFGWe8lAhGV-mP-5pHn0x2Sx6HEh-8ls0qCmtkFYheqQTLoM6o8TNqATNiv9LqM6mr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلالی سابق در آستانه پوشیدن پیراهن سرخ
🔹
رامین رضاییان، مدافع فصل گذشته استقلال، مذاکرات خود را با باشگاه فولاد خوزستان آغاز کرده و طرفین در گفت‌وگوهای تلفنی به توافقات اولیه دست پیدا کرده‌اند.
⏺
قرار است رضاییان طی یکی دو‌ روز آینده راهی اهواز شود تا…</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/456740" target="_blank">📅 13:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456739">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f7848bf8.mp4?token=LCLzG9t_APTdr5k9bcAUFsWP5GmDKGkVQ5Iip5DVOVZ67xPOlephh0xC_8zq5UWXo6WccWY3UDFmAh4ofZhtHZIsC3sIi6SaPy35rVHEs-ux_LANJClZsURUOapQxgvetcqRHKonW3dcF8Wvd8VaM8GZJx0_3lrVXA6qLrmY3J2db0oIfywrmNpIUTtSEURsd3KXDEvZ0cO9SRIVyGNK2nviUTY0T9sxsbCaFZSjwfH4-m7dV9c40YUdW3DRHmEN07S8ACm9W9WukqKct0CogenQCILTiTRWfps51P0NSg-JrZl3naEgxPk-VpgkmJDBiuERg06Ryut0S5NuC1gLUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f7848bf8.mp4?token=LCLzG9t_APTdr5k9bcAUFsWP5GmDKGkVQ5Iip5DVOVZ67xPOlephh0xC_8zq5UWXo6WccWY3UDFmAh4ofZhtHZIsC3sIi6SaPy35rVHEs-ux_LANJClZsURUOapQxgvetcqRHKonW3dcF8Wvd8VaM8GZJx0_3lrVXA6qLrmY3J2db0oIfywrmNpIUTtSEURsd3KXDEvZ0cO9SRIVyGNK2nviUTY0T9sxsbCaFZSjwfH4-m7dV9c40YUdW3DRHmEN07S8ACm9W9WukqKct0CogenQCILTiTRWfps51P0NSg-JrZl3naEgxPk-VpgkmJDBiuERg06Ryut0S5NuC1gLUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ریزش بخشی‌از تونل شهید میرزایی بندرعباس
🔹
بخشی‌از تونل شهید میرزایی بندرعباس ریزش کرده اما این حادثه منجربه انسداد کامل این تونل نشده و تردد وسایل نقلیه همچنان برقرار است. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/456739" target="_blank">📅 13:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456738">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b3c131f0d.mp4?token=Dfs-vH7QfZ4VW5ikb51DzAabtD6reovyJqV37iveXSrWNmhOaVDALQybgkuu2G5ICcp3MoKZFN2hUXwg_rFaBdD8V_aEZDGKdFno236kdEnI6FiNwXq1dD5HLmiw6pDc8Zsb1VfrrhFuep7UCacll6CGz_uR0lFJu1jisWutK-m_NnXktBPeY2NktkHPYmhxzDXtQ2CJZ_IJFvYCX9DLAP8A3a9MFUUacmSxnsJ6k_qGZXaYA-N6u9LSAMsvpHJ98YbltRldMlAYpepICiRkhURbW9cr3ZzjcQa5ANv4jelRYV_8BUhqexJUm7WBgxsXOIK0_0DfoB64x9yYZk9iGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b3c131f0d.mp4?token=Dfs-vH7QfZ4VW5ikb51DzAabtD6reovyJqV37iveXSrWNmhOaVDALQybgkuu2G5ICcp3MoKZFN2hUXwg_rFaBdD8V_aEZDGKdFno236kdEnI6FiNwXq1dD5HLmiw6pDc8Zsb1VfrrhFuep7UCacll6CGz_uR0lFJu1jisWutK-m_NnXktBPeY2NktkHPYmhxzDXtQ2CJZ_IJFvYCX9DLAP8A3a9MFUUacmSxnsJ6k_qGZXaYA-N6u9LSAMsvpHJ98YbltRldMlAYpepICiRkhURbW9cr3ZzjcQa5ANv4jelRYV_8BUhqexJUm7WBgxsXOIK0_0DfoB64x9yYZk9iGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا رضا پهلوی حرف‌های خودش را انکار می‌کند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/456738" target="_blank">📅 13:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456737">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
یمن از حمله به پالایشگاه جیزان در عربستان خبر داد
🔹
یک منبع نظامی یمنی به خبرگزاری رسمی این کشور گفت: نیروهای مسلح یمن با تعدادی پهپاد پالایشگاه جیزان در جنوب‌غرب عربستان را هدف قرار داده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/456737" target="_blank">📅 13:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456736">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe3abc88b.mp4?token=phnsR42xURG_2hQwYig-WaKiH8oii2ozvw9lBHJoOXdrdBMa4JtWfpIskUQCjO7cnZEY4XzoKR0rPdZ-2BEMxSuBxKK0t1GuTgmLbi2Be-tle5c3IOcW_ZswNAbIJMi-XoZFDO2caqDC68TgPIlFRG4NsBI9155oJwAOvQUbnJuG0NH67JoeAzmUPdUZUKl91Mi1SoSgAHp48bq816zToJEHjYtAmWhHEJJy__kPc1UUlOVgDXVvU4QYoXXgran9mXx1u6zIgU5Z07ODdEUrIFGVhg9Zd-qlNyInuFcfykolADRXt3VkdLFfpyVPx-SEK9FoaaOnf1CGSv0K7_FviQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe3abc88b.mp4?token=phnsR42xURG_2hQwYig-WaKiH8oii2ozvw9lBHJoOXdrdBMa4JtWfpIskUQCjO7cnZEY4XzoKR0rPdZ-2BEMxSuBxKK0t1GuTgmLbi2Be-tle5c3IOcW_ZswNAbIJMi-XoZFDO2caqDC68TgPIlFRG4NsBI9155oJwAOvQUbnJuG0NH67JoeAzmUPdUZUKl91Mi1SoSgAHp48bq816zToJEHjYtAmWhHEJJy__kPc1UUlOVgDXVvU4QYoXXgran9mXx1u6zIgU5Z07ODdEUrIFGVhg9Zd-qlNyInuFcfykolADRXt3VkdLFfpyVPx-SEK9FoaaOnf1CGSv0K7_FviQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه رژیم جولانی برای بشار و ۲ اسد دیگر حکم اعدام صادر کرد
🔹
دادگاه جنایی دمشق امروز علیه ۳ نفر از مقامات حکومت سابق سوریه از جمله بشار اسد، ماهر اسد و عاطف نجیب(رئیس سابق شعبهٔ امنیت سیاسی استان درعا و پسرخالهٔ بشار اسد) حکم اعدام صادر کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/456736" target="_blank">📅 12:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456735">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr3tphHsSBNbv33IKtsPFbnM5uR-tm61Ex7WWVkEmJPJqYc1fk3XEdfEbNR0hLXI5bg0RYMHskz6H8pUNBmqNGfgGSSbiEYdp50VXmIN9RZEPNEAstyY7F5j5Lf95XI-vw2uvq--my9dzsSWsgBw6B4FykHIah-_NEKkisTVjWnuUOgDchKSgmRe_u0ZTtG5dqy7IZUOp6FYRNaZdWrbiSdUdmszczow3Jg9onOQiPBaYSWL1W2Fd_SnrT6jkE_Y306Q_2iiI70AidyDDphiFapIgVV2b7gQp7B_ZOdTLGja_VkifAi42pg2l40EyY3KBRcUaCghf0BsBStoFLGfSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس از ۵ میلیون و ۹۰۰ هزار هم عبور کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۵۰ هزار واحدی به ۵ میلیون و ۹۴۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/456735" target="_blank">📅 12:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456734">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a00827141.mp4?token=qNdEKDLS-jeMpN5OzNd9E-td_5sb059HqsYClhBNpoy6axcUbGfFyPrnUEexSgyk5GZGstKxh6Pq75nUq5YDUwcQLg4OFEn_Cx9Gq9UQqj6Ya5GE5rMBs-WmUaSmcmkAl3vrNM-xwDG5mJSBvCqoJEL4wmpSqqztrV_3VyntwFIX1QuEBq9Yyk56vNUnruaiC6LoNmjTUqdayqdvgtShzyTMLSIwv8uOmsLellP7CgcZKluN9QrppDWKpYn5GmtwEHO2Pwgj4Mb6yepooNGHcgwhVT_SmN2t9YiidA8nN3TqBejrNixjDtxRuiBXM5A-JjfvLCb73_d9vYGwxoL9O2pPWJP2c7KESpwGBvasOa46u4n4O-TXbVQR0HI5lFAvRRehmAPIGJ1bGrwdTSOP5LVMcvIZf40E5sZvuDL6UeDvMgLR5mUuTrJ6cBZ8iLtmXS_4meGEG3QcY8n_1J0hFJ_QUklxYRDvNR0PGqLi10oPoMlo3QoXQ8vgfhf79UqxKbYigqsA8QQUalsbwg5QUWds21mgp0Jv84idXWjWcWXtttQF7QD6Fg7Cbn1t3zjrGUgkU55C8gEUK922nNIDk0HtPh9w4gHZarw5pgMCh9ymuc2ZpO7OD7zs7pCIFTh0igpIaAeHmVhyJPd28WTWP3mKWAkV_8EATTNAkAE2JTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a00827141.mp4?token=qNdEKDLS-jeMpN5OzNd9E-td_5sb059HqsYClhBNpoy6axcUbGfFyPrnUEexSgyk5GZGstKxh6Pq75nUq5YDUwcQLg4OFEn_Cx9Gq9UQqj6Ya5GE5rMBs-WmUaSmcmkAl3vrNM-xwDG5mJSBvCqoJEL4wmpSqqztrV_3VyntwFIX1QuEBq9Yyk56vNUnruaiC6LoNmjTUqdayqdvgtShzyTMLSIwv8uOmsLellP7CgcZKluN9QrppDWKpYn5GmtwEHO2Pwgj4Mb6yepooNGHcgwhVT_SmN2t9YiidA8nN3TqBejrNixjDtxRuiBXM5A-JjfvLCb73_d9vYGwxoL9O2pPWJP2c7KESpwGBvasOa46u4n4O-TXbVQR0HI5lFAvRRehmAPIGJ1bGrwdTSOP5LVMcvIZf40E5sZvuDL6UeDvMgLR5mUuTrJ6cBZ8iLtmXS_4meGEG3QcY8n_1J0hFJ_QUklxYRDvNR0PGqLi10oPoMlo3QoXQ8vgfhf79UqxKbYigqsA8QQUalsbwg5QUWds21mgp0Jv84idXWjWcWXtttQF7QD6Fg7Cbn1t3zjrGUgkU55C8gEUK922nNIDk0HtPh9w4gHZarw5pgMCh9ymuc2ZpO7OD7zs7pCIFTh0igpIaAeHmVhyJPd28WTWP3mKWAkV_8EATTNAkAE2JTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاندوزی خطاب به غنی‌نژاد: تصمیم‌گیری‌ها باید برمبنای منافع ملی صورت بگیرد
🔹
وزیر سابق اقتصاد در پاسخ به موسی غنی‌نژاد، اقتصاددان، که در یادداشتی با عنوان «منافع ملی و حق مسلم» به دوگانه‌سازی میان مفهوم حق و منفعت پرداخته: ایشان سال‌ها مروج مکتب اتریشی در ایران بوده است.
🔹
این مکتب آن‌قدر از جهت سیاست‌های آزادی اقتصادی افراطی است که حتی در متن نظام سرمایه‌گذاری دنیا نیز دولت‌ها انگیزه‌ای ندارند به توصیه‌های این مکتب عمل کنند.
🔹
در عرصهٔ بین‌الملل، تصمیم‌گیری‌ها باید برمبنای پیگیری منافع ملی صورت گیرد و صرف تأکید بر «حق مسلم» نمی‌تواند مبنای سیاست‌گذاری باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/456734" target="_blank">📅 12:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456733">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ffaaa833.mp4?token=gx8LMhVGvlCUE44F1AvG3YANh8jKSsf8HAXdL6ADM7Xo56kzlaBX3I_MxVF7-5jqtNWqb4TUmUbgE6jLGfOC8Q5zh_TYccNGGeIblWPYr626GYi_mxBHC3ttbKaakq93D-xtFQ3Zn5hvbxP097m_PhhcFQT2IG2n-3ce_PSoPJ5dVPsjC8NsuHCY6mn8obggdpnxebBmfUb74xcHWqaOg2W9hYhlw6qzXw1GBKLCQOOjw6CUATtjQ2hZ64fj_zHyqrsQdLb1J63Gq1aStXBp78W6WREJ0Gg_76ZxGzjnSwlG3kgMLYcHXjnZN8hDNCqox7Lm0NDO0BbMpHflKQDxWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ffaaa833.mp4?token=gx8LMhVGvlCUE44F1AvG3YANh8jKSsf8HAXdL6ADM7Xo56kzlaBX3I_MxVF7-5jqtNWqb4TUmUbgE6jLGfOC8Q5zh_TYccNGGeIblWPYr626GYi_mxBHC3ttbKaakq93D-xtFQ3Zn5hvbxP097m_PhhcFQT2IG2n-3ce_PSoPJ5dVPsjC8NsuHCY6mn8obggdpnxebBmfUb74xcHWqaOg2W9hYhlw6qzXw1GBKLCQOOjw6CUATtjQ2hZ64fj_zHyqrsQdLb1J63Gq1aStXBp78W6WREJ0Gg_76ZxGzjnSwlG3kgMLYcHXjnZN8hDNCqox7Lm0NDO0BbMpHflKQDxWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: افزایش قیمت بنزین توسط دولت تدبیر حساب‌شده نیست
🔹
دشمن برای سوء‌استفاده از اقدامات دولت جهت کاهش مصرف بنزین برنامه‌ریزی کرده است.
🔹
کاهش مصرف باید با بیشترین عدالت و کمترین نارضایتی انجام شود.  @Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/456733" target="_blank">📅 12:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456732">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8c1b68c6.mp4?token=XW70M01ixLOlIpmrG8MbY2YJGvy9KhsQGb-YvTctT37Cxf2hodITJhqQPdibMVjkd2IFTSNeAC6MGWIKCodqPulTMpVZnHtIQ59HQ81SVxXi0DeusKbQhKqc1qDTE1IoOjb6BkYddimEFzllpizSoIG6UXe9QWhxYpImBAEtAA6BwGvV57BkjdpGNp3CCeFTZC565yatFtw0u-PRIrAynOGgXngBReXX8Yd4FFw5MqojnUi_ZgBHsJRB0KanpwpUxQDsMlf1n9u6vUwDqJGygNCnMZbuNuJ1OSgoGxyZZ56PJiEX-M5H1fV_4h7q9xGxOXP4aDCjfF2y6HzAjMQ9mnVnBBVP5IdrE4dPuNzbIMtj7p2NaFOWTnpQQzKeN_ylX0yk4vUOMGzJNsr10FrJKQacVCa_RY1m8hEM6aaugrygGiCmEnSZ9c2zwi7wZaOgrfBRf9AgDCLHAJykwaXMmewY4OiN0VdcsurezUn9OtgOkGltg6_nAuWrRrX0eEuX9YwqvO-J9Hpnmro-fQ3DTz951g5noz61J8j8PFger1H9fV27HpQGJnQqrHr40bvZRUrdlL7AxglhEwiSTLC69vIcglP2Q_UMa983zXrSacI9o6IPssqegqGXCjcAikX_SQSMmiLCs1TqNUwSL444_vpBphtIHd5P9q9_mlKeSG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8c1b68c6.mp4?token=XW70M01ixLOlIpmrG8MbY2YJGvy9KhsQGb-YvTctT37Cxf2hodITJhqQPdibMVjkd2IFTSNeAC6MGWIKCodqPulTMpVZnHtIQ59HQ81SVxXi0DeusKbQhKqc1qDTE1IoOjb6BkYddimEFzllpizSoIG6UXe9QWhxYpImBAEtAA6BwGvV57BkjdpGNp3CCeFTZC565yatFtw0u-PRIrAynOGgXngBReXX8Yd4FFw5MqojnUi_ZgBHsJRB0KanpwpUxQDsMlf1n9u6vUwDqJGygNCnMZbuNuJ1OSgoGxyZZ56PJiEX-M5H1fV_4h7q9xGxOXP4aDCjfF2y6HzAjMQ9mnVnBBVP5IdrE4dPuNzbIMtj7p2NaFOWTnpQQzKeN_ylX0yk4vUOMGzJNsr10FrJKQacVCa_RY1m8hEM6aaugrygGiCmEnSZ9c2zwi7wZaOgrfBRf9AgDCLHAJykwaXMmewY4OiN0VdcsurezUn9OtgOkGltg6_nAuWrRrX0eEuX9YwqvO-J9Hpnmro-fQ3DTz951g5noz61J8j8PFger1H9fV27HpQGJnQqrHr40bvZRUrdlL7AxglhEwiSTLC69vIcglP2Q_UMa983zXrSacI9o6IPssqegqGXCjcAikX_SQSMmiLCs1TqNUwSL444_vpBphtIHd5P9q9_mlKeSG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: گلایه‌های اقتصادی مردم را به‌حق می‌دانم
🔹
برای همۀ انتقادهای سیاسی و اجتماعی آنها احترام  قائلم ولی این ایام زمانی است که باید شب‌های پرشور میادین بار دیگر برای دشمن خودنمایی کند.
🔹
خیابان، محل میتینگ‌های انتخاباتی نیست بلکه میدان‌های اتحاد مقدسی…</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/456732" target="_blank">📅 12:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456731">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb64c3172.mp4?token=XAycPn5Fs4951ex2AzkW66ZopuS1c5wk4Tp4o7Hyn1RrpaR7e8OZ02UgCrJgA5zpZw86giLIenKdtgtsl-FHBkzIhjw2hVJ2XixZfFefFZPMFv_U-BHwU9gwdlolNYVPAA3oiRK_scCPTT-xFVuV0insXzSh6sNHWnvu7tJbg9QBM1ursn1h-zXQy4Wn2NReGRuM4Zf1qbStRQnKH4yfQJN4sstWn-a__SN8JHLftOWOzh20NGJ9HEypotZphrw_SYKeGa95hNm6gCybIyx5Rn426VgMOb6i_STOGSiMCRFCEU0ANVUTDul_3dawToEvIxyUkp0gMS2wJqGDLi1Y0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb64c3172.mp4?token=XAycPn5Fs4951ex2AzkW66ZopuS1c5wk4Tp4o7Hyn1RrpaR7e8OZ02UgCrJgA5zpZw86giLIenKdtgtsl-FHBkzIhjw2hVJ2XixZfFefFZPMFv_U-BHwU9gwdlolNYVPAA3oiRK_scCPTT-xFVuV0insXzSh6sNHWnvu7tJbg9QBM1ursn1h-zXQy4Wn2NReGRuM4Zf1qbStRQnKH4yfQJN4sstWn-a__SN8JHLftOWOzh20NGJ9HEypotZphrw_SYKeGa95hNm6gCybIyx5Rn426VgMOb6i_STOGSiMCRFCEU0ANVUTDul_3dawToEvIxyUkp0gMS2wJqGDLi1Y0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: تنگۀ هرمز تا تحقق شروط تفاهم‌نامه باز نخواهد شد
🔹
ایران تا زمان تحقق شروط مندرج در تفاهم‌نامه اسلام‌آباد، از جمله رفع محاصره، آزادی اموال بلوکه‌شده، رفع تحریم‌های نفتی و پایان تهدید و عملیات نظامی، تنگه هرمز را باز نخواهد کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/456731" target="_blank">📅 12:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456730">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d1e11ae4.mp4?token=ijlxVI9wE5CFn4Vu_O0qdBpmr1iCYhfHpsIcJGCv7rSTego8bO48W37HUn6WSSEfcGV15wxyn2lqSOivNhRGJjGdmJU8hFma23bJAzal2vCKsCBnFk4--GziJBWvKsuNyEy8zzqQU5W5yjciPS5_xWzCX7byS6kobZARz3B2GHMJZWRSRTmVtyKv6umn8RhB3RItoNKglEfgbRhyCPDDh3TkVXwEJsSB2HauGg4jUnQAV4f-Xd24UssoCLpjpy_SMOz7_9j03RGatCoogEfUHybfJ3QqkNIMhZs6iJoc5RKFkIN2LvcGhUby54gLV1SMCAunkU7vYuaALeLMBUf98w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d1e11ae4.mp4?token=ijlxVI9wE5CFn4Vu_O0qdBpmr1iCYhfHpsIcJGCv7rSTego8bO48W37HUn6WSSEfcGV15wxyn2lqSOivNhRGJjGdmJU8hFma23bJAzal2vCKsCBnFk4--GziJBWvKsuNyEy8zzqQU5W5yjciPS5_xWzCX7byS6kobZARz3B2GHMJZWRSRTmVtyKv6umn8RhB3RItoNKglEfgbRhyCPDDh3TkVXwEJsSB2HauGg4jUnQAV4f-Xd24UssoCLpjpy_SMOz7_9j03RGatCoogEfUHybfJ3QqkNIMhZs6iJoc5RKFkIN2LvcGhUby54gLV1SMCAunkU7vYuaALeLMBUf98w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: تغییر شیوۀ‌ کالابرگ یا افزایش اعتبار آن ضروری است و باید هرچه سریع‌تر اجرایی شود
🔹
هر فرد یا دستگاهی که با گفتار، رفتار یا تصمیمات خود، باعث نارضایتی مردم شود خواسته یا ناخواسته در زمین دشمن بازی می‌کند.
🔹
مهم‌ترین وظیفه‌ای که ما مسئولین کشور خصوصاً…</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/456730" target="_blank">📅 12:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456729">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVkcoMX4XgNtI-FTC1sNbRKE16PWCFa_o9mAi6j3-i4rs2Az3a0Az-e7sWXrs5hjWLz_AkwvNTK23Yi5tb_TQh8mcNvTca8eDAh78frEfNpgFmfqcZnbpJALiINimsGjNj-I1S7YfkJLFVtjrSzrF0AfiRaOsn0JJ75Eqeyowjy0UBn9_o6cDvmEegTgIp2lOaCli7bTD-4MBHwq9QvriDZ5NroU7St0EMKOd5kB7PQq-HOHTXInsKIJK3lEJZV9dvX6xA_4lbSpkBhjzyjYbzwY_ZcaNRFGN3mNwSfBin0xGXjRpPeD6dj-saeeqC9vnyecyITQ9c1ITfXxyMAcPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ باشگاه استقلال: عراق میزبان احتمالی تیم در مسابقات لیگ نخبگان است
🔹
این موضوع پس از انجام قرعه‌کشی و بررسی نهایی توسط فدراسیون فوتبال این کشور، قطعی خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/456729" target="_blank">📅 12:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456728">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44a8fa997.mp4?token=B54YxhltFUnX-61BS_uGOBmUbQNhr1xwVRBWqnRWQihkQ4u-uMKNhN2zeoAAGWFbtvpmtPFPAzJj-cZjzfaI9BfLXphTyXvu1nIwtZml_hCfhdGJcQtLBywcJys6ZWroHEKf46tPEFhpqs_3Cb67sxGBFc_6jCDcDnHayrSuyM2xFtzLchjC86YOF9g38RgnGfpE_Q0JSYRE5baHc2gH3lUwQ7ysX8k2TeUS08B8TK4QbAkee_7NW7qp_gqeOhsa8ZPlEhssup3b-soZnjXaL1mMTzuTOKF1D41TgjNTc5uDiHDRwGXhuK6OJbHAp5OkIYlJpFTeZ6mGpoqAK9Yh-DQBK5QwO2TDf8WCdDLM7SjfVljYNoTLqVcci-Kpm1aTV0Ij1jiseu9zvgY9HUkhKOa5K4fToop6KHxnchMH1kl_-WKbl4B7VCR6loy1lhGMNalPXDBDrLV87ZdOiQoNhvrC2mV-J-Bm0Smm2gA2EUKPDC_Au_YXGKg7luoJ9UX58Z-GWBcxIxoo-Jgxhi-vIdLltNG9sfe1C4FfeWt6VRz1zCHBaBA_q-JhODpD_iwfUziflSe6DI-fKpcMIPoapchF995ld7KRkWo7GvJEoEe1fYxvfYzXl_7lwo-0QILfToFrJ8xw9Jn6FajwrH1YGsH5Os3vSpbOoTl6wEfTl5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44a8fa997.mp4?token=B54YxhltFUnX-61BS_uGOBmUbQNhr1xwVRBWqnRWQihkQ4u-uMKNhN2zeoAAGWFbtvpmtPFPAzJj-cZjzfaI9BfLXphTyXvu1nIwtZml_hCfhdGJcQtLBywcJys6ZWroHEKf46tPEFhpqs_3Cb67sxGBFc_6jCDcDnHayrSuyM2xFtzLchjC86YOF9g38RgnGfpE_Q0JSYRE5baHc2gH3lUwQ7ysX8k2TeUS08B8TK4QbAkee_7NW7qp_gqeOhsa8ZPlEhssup3b-soZnjXaL1mMTzuTOKF1D41TgjNTc5uDiHDRwGXhuK6OJbHAp5OkIYlJpFTeZ6mGpoqAK9Yh-DQBK5QwO2TDf8WCdDLM7SjfVljYNoTLqVcci-Kpm1aTV0Ij1jiseu9zvgY9HUkhKOa5K4fToop6KHxnchMH1kl_-WKbl4B7VCR6loy1lhGMNalPXDBDrLV87ZdOiQoNhvrC2mV-J-Bm0Smm2gA2EUKPDC_Au_YXGKg7luoJ9UX58Z-GWBcxIxoo-Jgxhi-vIdLltNG9sfe1C4FfeWt6VRz1zCHBaBA_q-JhODpD_iwfUziflSe6DI-fKpcMIPoapchF995ld7KRkWo7GvJEoEe1fYxvfYzXl_7lwo-0QILfToFrJ8xw9Jn6FajwrH1YGsH5Os3vSpbOoTl6wEfTl5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: تغییر شیوۀ‌ کالابرگ یا افزایش اعتبار آن ضروری است و باید هرچه سریع‌تر اجرایی شود
🔹
هر فرد یا دستگاهی که با گفتار، رفتار یا تصمیمات خود، باعث نارضایتی مردم شود خواسته یا ناخواسته در زمین دشمن بازی می‌کند.
🔹
مهم‌ترین وظیفه‌ای که ما مسئولین کشور خصوصاً مدیران اجرایی دولت به‌عهده داریم این است که وسط میدان حل مشکلات اقتصادی و معیشتی مردم باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/456728" target="_blank">📅 11:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456727">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9nU58EKgWgl-ME3325xN40Is9sTAMnDw35acdTP-jDLeF5p-CnpjeuTb4NuyZ7fb-XWFKFflvqycvwPOiJDNSYi7T9bDhA8dAHTFklOoZ2C-us7X75BvkVCU4A8N2mRzcn2NQegTLL5IfV9POX4ffBD0_qvNgCw0Gk3FwWcoAvRV1zeaaX8ZGnWmTqh_eqMmA4GANa3J0RbnlENMh0YQvdhzDoLBa86oF378dSUYpmGh1o47PXzZDPZzXdKisNkp4TSiqeN3G_4BcTeJKUpkGqpRHj542DX_CQzFYEnj5Cp8AtIPNsLMzR-h_2iMxJioV3ERWs2tdP3L9lpXRjPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر ایزدی: تنگهٔ هرمز کاملا در اختیار فرزندان ایران است
🔹
جانشین فرمانده سپاه: دشمن به‌دنبال ایجاد براندازی و تجزیه در ایران بود و رئیس‌جمهور خبیث و شیطانی آنها بارها اعلام کرده بود می‌خواهم به نفت ایران تسلط پیدا کنم و تنگهٔ هرمز را در اختیار بگیرم.
🔹
او حتی گفت تمدن، صنعت هسته‌ای و حتی غبار ایران را می‌خواهم از بین ببرم.
🔹
نه‌تنها ایران اسلامی تجزیه نشد، بلکه قوی‌تر شده و فرماندهی امام شهید و رهبر حاضر ما شرایطی را به‌وجود آورده که دشمن مستاصل شده است.
🔹
در دنیا اتفاقات جدیدی و عجیبی رخ داده است؛ دلدادگان انقلاب می‌گویند شما نمی‌دانید چه‌کار کرده‌اید و باعث شدید ابر قدرت جهان افول کند.
🔹
دشمن نمی‌داند چه‌کار کند و تنگهٔ هرمزی که معادل یک انرژی هسته‌ای است و انرژی، کشاورزی، صنعت دنیا و.. را تحت تاثیر قرار داده، در اختیار فرزندان این مرزوبوم است.
🔹
امروز باید با مجاهدت بیشتر به پیش برویم و به‌فرمایش امام شهید ثمرهٔ پایداری دستیابی به نصرت موعود الهی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/456727" target="_blank">📅 11:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456726">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a953a64b2.mp4?token=vAWN06c789dFtsgMhwKnKcMRRXHYf9SgqubpeodnXOznpYbnDMb2e8hKLLA6pt0iDgUi9GMmbiBdqn2AEfvN1lf3VE4evKDDx5Tna2vudoGGvuxTOnvyO7oSSrI-w9hACOTwjjpBQVFacBKeDk8SggzUML_v7todJk4BvpUSaElTeh8pgrE-9wy-hM9VfBdrDjiOSKY9D6MXA8fmYxUOyb5zP2A-eTTN-ruebJQ_DNlEYTU4NoNwGDL7Mi-uPhWvACbLCI34r-iP45pGSJM48nZfWBbf4CCajE2VJKiDEhQaePQNIjU4go65i2U0lRpAJZOzDUOG9STxAIcB-hBIRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a953a64b2.mp4?token=vAWN06c789dFtsgMhwKnKcMRRXHYf9SgqubpeodnXOznpYbnDMb2e8hKLLA6pt0iDgUi9GMmbiBdqn2AEfvN1lf3VE4evKDDx5Tna2vudoGGvuxTOnvyO7oSSrI-w9hACOTwjjpBQVFacBKeDk8SggzUML_v7todJk4BvpUSaElTeh8pgrE-9wy-hM9VfBdrDjiOSKY9D6MXA8fmYxUOyb5zP2A-eTTN-ruebJQ_DNlEYTU4NoNwGDL7Mi-uPhWvACbLCI34r-iP45pGSJM48nZfWBbf4CCajE2VJKiDEhQaePQNIjU4go65i2U0lRpAJZOzDUOG9STxAIcB-hBIRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آغاز ثبت‌نام بدون کنکور دانشکده رسانه خبرگزاری فارس – ترم مهر ۱۴۰۵
🎙
ثبت‌نام در مرکز آموزش علمی کاربردی دانشکده خبرگزاری فارس برای ترم مهرماه ۱۴۰۵ آغاز شد! این دانشکده به‌عنوان یکی از مراکز تخصصی در رشته‌های:
📰
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
…</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/456726" target="_blank">📅 11:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456725">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAGlY9NfhSvhysPm39I4cQaSPWuCXd-Kzwwp5r5AjS8w9IR-Z5J1-PtQjyejA2RmvkB12JFK1E2g4ppquJ5c6GXwWCMgL-b6gBiOTu-DqfxaE7sg3LT5bWhzvhAid88cgSnlke11HYiWUemBbO5FDGEhT44hHZePqVEUwOK53263FYf6enoHhtec8lrEBr5Vampv3j3noyt3SMFYIs-HldwfGawW8HHrIC41Q4HgFMVoGrTqUg3Yxp6NSmYyjp2I_8kLileqXS9MNwlQFdx5yORKrw1pjkVM7jtyT4ztyN070K3BL2P1UStTHhqksDIHPWPxGK5eVrCjn_QPXRwjJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاریخ ثبت‌نام و برگزاری آزمون‌های دکتری و کارشناسی ارشد سال آینده اعلام شد
دکتری:
🔹
ثبت‌نام: ۳ تا ۹ آبان ۱۴۰۵
🔸
آزمون: ۱۶ بهمن ۱۴۰۵
کارشناسی ارشد:
🔹
ثبت‌نام: ۱۶ تا ۲۲ آذر ۱۴۰۵
🔸
آزمون: ۱۶ و ۱۷ اردیبهشت ۱۴۰۶
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/456725" target="_blank">📅 11:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456724">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQvw8ez-N9GJK1xNYfQXcS3gLvur4zImlyN_1B7tLXHaR2v2dQPkNxroAVp9_O08u6ADsuHxc1AVmGKwKrJUvR-z9gis-jefwXqupCfVRIKAg9gnWGUQ2JtQCUiJMMKZQ7U4Q40cMshx-weI1dDk_F1yDp37PcLwKb3zn9cfQj1EhstGiUgyoUDRRkmL4T0Dn0hDjgxoVC9M5uR2dHKK9L4X6R9DTZtZkHnvOuD-tSiZNdjSnqTSm9H6w14IdL3dLUmQyQ0TN7QgcjfrSELRZ_ajgrgSRxQxGyCHoz5FMmqahMlV5Iblpt5r30cBnr68fZoxG37TY1fykvPZVdX41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: دولت برنامه‌ای را دنبال می‌کند که طی ۵ سال، مشکلات معیشتی معلمان حل شود
🔹
رئیس‌جمهور در حوزۀ آموزش‌وپرورش تمام‌قد به میدان آمده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/456724" target="_blank">📅 11:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456723">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزارت دفاع: راه رهبر شهید برای ساخت قدرت دفاعی را پرقدرت ادامه می‌دهیم
🔹
بیانیۀ وزارت دفاع به‌مناسبت روز صنعت دفاعی و همزمانی با چهلم آقای شهید ایران: رهبر شهید در سال‌های مسئولیت و هدایت کشور، همواره توجه ویژه‌ای به تقویت بنیۀ دفاعی، خوداتکایی و پیشرفت صنعت دفاعی داشتند.
🔹
بخش مهمی از مسیر پیشرفت صنعت دفاعی کشور، با هدایت و حمایت‌های آن شهید بزرگوار طی شد؛ مسیری که از خودباوری آغاز شد و به شکل‌گیری ظرفیت‌های گسترده علمی، فناورانه و صنعتی در کشور انجامید.
🔹
راهی را که ایشان برای ساختن قدرت دفاعی کشور ترسیم کردند، با قدرت ادامه دهیم و آن را متناسب با نیازها و تهدیدهای جدید، پیشرفته‌تر و مستحکم‌تر کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/456723" target="_blank">📅 11:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456721">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دستگیری عامل ارسال اطلاعات حساس به دشمن در تهران
🔹
مرکز
اطلاع‌رسانی پلیس تهران از شناسایی و دستگیری فردی خبر داد که تصاویر و مختصات برخی نقاط راهبردی و امنیتی کشور را جمع‌آوری و برای گروه‌های مخالف جمهوری اسلامی ارسال می‌کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/456721" target="_blank">📅 11:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456720">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFdhOz6pwvHU-bt2yhMgDPKZveqVhzPSadA5r9HXeCJ_eAo77GN9yiev4E_fpetiIbgjpqeNs6oT6FxYl7KR3do4jRQX93EtW8gkmhXBye1iwv4vv1lgkG1wM_7x-Q6Yk1cg4GVNy4qQXA3045BbogbGT_as-aroy0RHRj446JprI_AvhkMAXWoRJVUFoJEg7NxQ4AFtc-Al422XN5niAIZ6m39WI1BuOwl5fjnm4i-A-RjNFz4HS1EuSkVOVevnVBehM9p9AQ9RM1Hu37nebpmCLH_KGKZfIWmYvTxAyBxIJKYVTRRTjKb9JYFLe0x9HqyyVvMIg15NcBJHGsOyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتایج آزمون دکتری اعلام شد
🔹
سازمان سنجش: اسامی پذیرفته‌شدگان نهایی آزمون ورودی مقطع دکتری «.Ph.D» نیمه‌متمرکز سال ۱۴۰۵ دانشگاه‌ها و مؤسسات آموزش عالی و دانشگاه آزاد اعلام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/456720" target="_blank">📅 11:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456719">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
یمن از حمله به پالایشگاه جیزان در عربستان خبر داد
🔹
یک منبع نظامی یمنی به خبرگزاری رسمی این کشور گفت: نیروهای مسلح یمن با تعدادی پهپاد پالایشگاه جیزان در جنوب‌غرب عربستان را هدف قرار داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/456719" target="_blank">📅 11:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456718">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حق انتخاب میزبان آسیایی از استقلال گرفته شد
🔹
کنفدراسیون فوتبال آسیا اعلام کرد که مهلت باشگاه استقلال برای معرفی ورزشگاه میزبانی در رقابت‌های لیگ نخبگان آسیا به پایان رسیده و AFC تکلیف استادیوم میزبان مسابقات آبی‌پوشان را روشن خواهد کرد.
🔹
باشگاه استقلال در…</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/456718" target="_blank">📅 11:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456717">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83bab004c.mp4?token=cTzay-tyL5D7Xvi-s39FeVjuzWyQskjq1FqsPZOHXW6iVfqbq_9C9rdN_vIFf2cGbQd6HGeYDIyJ3BaxmIeg3I2VOEksy9eM78gZ7tZ_XEvkluKWdhUnqE2QnKHFG4771ZONEahF4P_pjWdW7Z4QLrlYTpjeTH5Dhw41gqF0_PF_a3Q_4LORFwOqNrvRnpMU30q49r-DYFwVhpBmDCAmGB0zQfcdx0PQ5BjajcHoTqpiZmZ1g98sYokt-xwSim5VultYbSZbogVdhO3BgI0WUPubEKXS1YHTEpypGWWhrwcXy96aF9L9yT9MVtO9bwYmn55W9p6ewYKrwC1V0Y1LUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83bab004c.mp4?token=cTzay-tyL5D7Xvi-s39FeVjuzWyQskjq1FqsPZOHXW6iVfqbq_9C9rdN_vIFf2cGbQd6HGeYDIyJ3BaxmIeg3I2VOEksy9eM78gZ7tZ_XEvkluKWdhUnqE2QnKHFG4771ZONEahF4P_pjWdW7Z4QLrlYTpjeTH5Dhw41gqF0_PF_a3Q_4LORFwOqNrvRnpMU30q49r-DYFwVhpBmDCAmGB0zQfcdx0PQ5BjajcHoTqpiZmZ1g98sYokt-xwSim5VultYbSZbogVdhO3BgI0WUPubEKXS1YHTEpypGWWhrwcXy96aF9L9yT9MVtO9bwYmn55W9p6ewYKrwC1V0Y1LUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ریزش بخشی‌از تونل شهید میرزایی بندرعباس
🔹
بخشی‌از تونل شهید میرزایی بندرعباس ریزش کرده اما این حادثه منجربه انسداد کامل این تونل نشده و تردد وسایل نقلیه همچنان برقرار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/456717" target="_blank">📅 11:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456716">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7beb940822.mp4?token=pIQAkr86ZSQo7h9BvABoF3vlwT34wSdErGwIcONoXsp8-4M2filFukQGHtnMNWb1ZOHr8tTIyZtOQr0WeOxj7WZ9EPfNOqah0L0zT0reiqFxmjXmlZhShab-FNCO62hGeeMV1ELsP0DathkSrOxEjRgy2YNKfsLWhmoN1-hNn52D9geNpp9HyCdW7n2RbFwb6PF-KSDwdHDDDAzZ_8rnsN6CJZuBYHRz2X9Boo88U5UmpgEu8Q91AWY0p26RC2GRyS6Rr0DdelulNU1Biv4utcvvVTpKAybJdLnPXzZu8B8FrOqqnSPjkp69RVd41be-9CcZJgEAIQ7IRjZl_u5sXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7beb940822.mp4?token=pIQAkr86ZSQo7h9BvABoF3vlwT34wSdErGwIcONoXsp8-4M2filFukQGHtnMNWb1ZOHr8tTIyZtOQr0WeOxj7WZ9EPfNOqah0L0zT0reiqFxmjXmlZhShab-FNCO62hGeeMV1ELsP0DathkSrOxEjRgy2YNKfsLWhmoN1-hNn52D9geNpp9HyCdW7n2RbFwb6PF-KSDwdHDDDAzZ_8rnsN6CJZuBYHRz2X9Boo88U5UmpgEu8Q91AWY0p26RC2GRyS6Rr0DdelulNU1Biv4utcvvVTpKAybJdLnPXzZu8B8FrOqqnSPjkp69RVd41be-9CcZJgEAIQ7IRjZl_u5sXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همۀ‌ آنچه باید دربارۀ کنوانسیون خزر بدانید  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/456716" target="_blank">📅 10:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456715">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎥
روایتی از روزی که ایران با رهبرش خداحافظی کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/456715" target="_blank">📅 10:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456714">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0631fd666c.mp4?token=nr46-5mAHRrStrvy_pCa8Xnh3pSgnemmTCEQEF47WBQRL8ADpisYcuL8bq-eWGJKIEwKlPKJH8zinsjbuT56NEgD4IU1PTqtKJTsqucfhJdgIzl_TCMRiZJEKUv85NCkffKDoxHQs9RRO0dcagFlwZ-AqQYDuKW1MnDosiVhefRxSTgDdUtkb-P-lyz2-BHMlxxyed95WOMkV08NMLxx2FvljeGWc24V8zqkOiKbMcbKha5-23D6BEjVuAxygU9LCnMJAWr-FSq-qvjs2VmuCjNHL3A2xrHYqGR81I4yepH47TAwb3WEQrA9TK8XBxii1TVdbsSpot2NwXTVKLNcCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0631fd666c.mp4?token=nr46-5mAHRrStrvy_pCa8Xnh3pSgnemmTCEQEF47WBQRL8ADpisYcuL8bq-eWGJKIEwKlPKJH8zinsjbuT56NEgD4IU1PTqtKJTsqucfhJdgIzl_TCMRiZJEKUv85NCkffKDoxHQs9RRO0dcagFlwZ-AqQYDuKW1MnDosiVhefRxSTgDdUtkb-P-lyz2-BHMlxxyed95WOMkV08NMLxx2FvljeGWc24V8zqkOiKbMcbKha5-23D6BEjVuAxygU9LCnMJAWr-FSq-qvjs2VmuCjNHL3A2xrHYqGR81I4yepH47TAwb3WEQrA9TK8XBxii1TVdbsSpot2NwXTVKLNcCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درگیری ترامپ با خبرنگار سی‌ان‌ان؛ کاخ سفید ماجرا را خانوادگی کرد
🔹
در ادامهٔ سلسله‌حملات ترامپ به خبرنگاران زن، این بار درگیری او با خبرنگار سی‌ان‌ان به حملهٔ شخصی کاخ سفید و فرزندان این خبرنگار کشیده شد.
🔹
ماجرا از آنجا شروع شد که هولمز خواستار پاسخ ترامپ به انتقادات سناتور دموکرات شد و پرسید «جان اوساف گفته که شما ترجیح می‌دهید با دستیار خود، ناتالی هارپ، سفر کنید و سالن رقص بسازید تا اینکه به وظایف ریاست‌جمهوری خود عمل کنید».
🔹
ترامپ به‌جای پاسخ به سؤال هولمز، به این سناتور آمریکایی حمله کرد و بعد حساب «واکنش سریع» کاخ سفید وارد این درگیری شد و با انتشار ویدئویی کوتاه از این مشاجره، هولمز را «مایهٔ ننگ و شرمساری برای حرفه‌ای که ادعا می‌کند در آن فعالیت دارد» توصیف کرد.
🔹
کاخ سفید در پست دیگری، حمله‌ای شخصی‌تر را در پیش گرفت و نوشت «روزی فرزندان شما با سؤال نفرت‌انگیز و غیرانسانی‌تان مواجه خواهند شد. آن‌ها از اینکه یکی از والدینشان تا این حد سنگدل و کینه‌توز بوده، منزجر و شرمنده خواهند شد. این واقعاً نگران‌کننده است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/456714" target="_blank">📅 10:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456713">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌ پیش‌پرداخت ۳۰۰ میلیونی حج آینده
🔹
رئیس حج و زیارت: تا نرخ ارز مشخص نشود، رقم نهایی هزینۀ حج آینده قابل اعلام نیست. این درحالی است که بسیاری از زائران منتظر قیمت نهایی هستند که بدانند می‌توانند حاجی شوند یا نه.
🔹
متوسط هزینۀ حج گذشته حدود ۴۰۰ میلیون بود اما…</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/456713" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456712">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXE2M_-jlmpmryoUx7P2c5A4KbXQeRJPrfdJjaRtoKqgNZ1TB8_d8eqaCz1kWiZ-MTkcTH6wrn0FWGiZnWeLXXch5rjQAi1g13-SDelauxw0vNASlHDlnd0WVQpk7uLscaloSUY7sEe58CoXsDiJDTQNL19NpgLB3_SediufRvArO5tx_w0MQKCxCEjq6EZtQ0bdDPHhTUK29Z18hCzJZonvABYFmO_CVVcZlim-UkIwqqqZBcRnoYbAnXeOnxZ4Xkt37cEMnWmUsq4Q4CtLz2ncddd4ckcUhdodMfpaeXpHj4uu4qV5_R_0SH8DS_tfQ2RRWGwdxQuKFUrKS3SzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمران: متأسفانه فعلا جای مناسبی پیدا نکرده‌ایم که به‌نام رهبر شهید نامگذاری شود.
🔹
پیش‌تر بوستان ولایت و فرودگاه مهرآباد پیشنهاد شده بود اما باید معابر دیگر هم پیش‌بینی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/456712" target="_blank">📅 10:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456711">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کارت زرد مجلس به وزیر کشاورزی
🔹
گودرزی، سخنگوی هیئت‌رئیسۀ مجلس: در جلسۀ امروز صحن علنی، سوال عباس بیگدلی با موضوع مشکلات مربوط به دام‌ از وزیر کشاورزی مطرح شد که نمایندگان از پاسخ نوری قانع نشدند و به او کارت زرد دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/456711" target="_blank">📅 10:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456710">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWoZuwF3q5r1De-DXO5YM9rPin5euX0AmcL0Zk7-AJ-DIC537iT1W9eQASqfvYFksxLvNKVGpZjZUhoIpmIEEDyhA6SkjPs6k0Hum72b1eatQBX49a64Op1hPgF30TVMX3GdFIXxOEUBr5cc1y56kFMBstpWt64L8iZ6qbKOhDgxnEDEB7YAgZxAoDdwWz0s5SLiFPDtYHq0QlSZxqpD3jUNEaESenmtV4YkqE02DuPRTbtgrDkGDD2jMx0DTMRmdTWmOIta3rIPXmnaOwLRdqVdnTfGgdxCVPQCGhToH2isn6n0qR67x_u7c-b0Y4Ww-XBYQgEilylsKnFKBwS28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمران: کیفیت گازوئیل تهران پایین آمده است
🔹
رئیس شورای شهر تهران: پس‌از مشکلاتی که برای پالایشگاه تهران ایجاد شد، کیفیت سوخت تحویلی به شهرداری با کیفیت مورد انتظار فاصله دارد.
🔹
گازوئیلی که در اختیار ناوگان حمل‌ونقل عمومی قرار می‌گیرد باید از کیفیت مشخصی برخوردار باشد تا به خودروها آسیب وارد نکند. به مسئولان مربوطه توصیه کرده‌ام هرچه سریع‌تر گزارشی کتبی دربارهٔ این موضوع تهیه و برای شورا و شهردار تهران ارسال کنند تا موضوع کیفیت سوخت پیگیری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/456710" target="_blank">📅 10:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456709">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzrxCiKZKqG9susaD9Yw1Yh6zFA-H3boF58kra2oma2EqwUfvP2y_JBwP4RhqFcld-GI4mmz9tZ02NczqthZFThDt1KUjegNyF1NJ__EkqFW-qeF8rzqVuCYcu2fUnNqnDTOeHnmRFf2wA5BjNEI3VrepWWTkZo8uRClpVh8zuMUDOXXAWfGjH8eFHUDFgnvAA3-sS2nF9o_UlHumvqUvkZ-PrxmWHlevXPDipgDc3DwTjqgyr0PTQm-CQ4KhKjcoO2Fwiw1aU3DeYKSf_KtRq4G487k8Pm2zahsrOWKgqAKz2keFfu3QqKKQ-ety8OCGWqcJpvH_9fT1nTfPh7LpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف بیش‌از ۹ میلیون نخ سیگار قاچاق در اصفهان
🔹
فرمانده انتظامی اصفهان: ۹ میلیون و ۷۰۰ هزار نخ سیگار قاچاق به‌ارزش بیش‌از ۷۷ میلیارد تومان که قاچاقچیان سعی داشتن در پوشش تانکر حمل سوخت آن را جابه‌جا کنند، کشف شد.
🔹
خودروی موردنظر توقیف شده و متهمان برای سیر مراحل قانونی به مرجع قضایی معرفی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/456709" target="_blank">📅 10:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456708">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اداره‌های بوشهر فردا تعطیل شدند
🔹
استانداری بوشهر: به‌منظور مدیریت مصرف انرژی و گرمای هوا، اداره‌های استان به‌جز مراکز خدمات‌رسانی و امدادی فردا تعطیل هستند؛ نحوهٔ فعالیت‌ بانک‌ها اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/456708" target="_blank">📅 10:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456707">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuofDEi1AxfRu092qAUWUReU-MGvRVZnea8i58le-K8_E1XbbKrb07nqnGozAeGdmJ6yEG1xTomK293P8tSMTrQ2DrcTh8kFT8B7lQWvThlTBkGtmMIDYGKBkusR6tjqogDp8XB2zdmWquXm17QQ45uU5_SMEaWj_obiJQBMFSkUX6y-pl12oUoh7U0QYbzAQd5sCVQMszieK7ZxKQ_ZjuxagqY5j0seKfBazZEfZc_cZWJHf9PUkpDw4XeVCT7-F5QhaznzLKwayXmFmisSgxRr-SFL68NvS9bFTNzSaek7GIKCuVWq2jeIW784_QGNPgG6Q5_HS8FzRSR1t2GZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل‌گهر،</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/456707" target="_blank">📅 10:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456706">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5J6e0HaaU4lNDkLGOM5O9SPFfzWh5wYUT3zgKbIKCVue01eBW6r4j8xngFtoEqCkU5eRScLuPUxc9jsDpuv79Wgd582dhVAYCoOFMZfinAvUqHE1CJtc188IvRG0Fl_XxzdGSY9g35FhY8aa341uwXjWB2rboDnNdvdkwj-99-q-Epy_4xA_cI07eAE7sLtqeTAIK6XOv4vJzelxa2CgwRK7a5Bfg6VoMFutROhqq1aHc2BL3krFD_5dVb62uf7NcbEByXr9_N62npt6g-gRTK45sCT1CDsIdlZVLm46QiKDe76NefDttodxxEgy4hpzBYHBF6IWCCLvD0xwK86Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسیب
آنتی‌بیوتیک‌ها به سیستم ایمنی کودکان
🔹
مریم رستمیان، فوق تخصص عفونی کودکان: براساس آمارهای جهانی بیش از 50 درصد موارد استفاده از آنتی‌بیوتیک در فرزندان، موارد تجویز نادرست و نابه‌جاست، درحالی که شاید فرزند بیمار اصلاً نیازی به این داروها نداشته باشد.
🔹
آنتی‌بیوتیک‌ها داروهایی هستند که تنها برای اثرگذاری بر باکتری‌ها ساخته شده‌اند و هیچ اثری بر عوامل ویروسی ندارند. بنابراین اگر فرزندی دچار عفونت ویروسی شود، استفاده از انواع آنتی‌بیوتیک‌ها با هر دُز و هر مدت زمانی نیز تاثیری بر عامل ویروسی نخواهد داشت.
🔹
هر زمانی که فرزند دچار تب شد، خانواده‌ها می توانند از داروهایی مانند استامینوفن برای کنترل تب استفاده کنند اما اگر تب طول کشید یا با بدحالی همراه بود، حتما باید به پزشک مراجعه کرد.
🔹
استفادۀ نابه‌جا از آنتی‌بیوتیک‌ها می‌تواند میکروب‌های مفید بدن را که بر سیستم ایمنی تاثیر مثبت دارند از بین ببرد و باعث ضعیف شدن سیستم ایمنی فرزند شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/456706" target="_blank">📅 10:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456705">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOkcR9o_Vy7kqv8nAnweTluTYdQlmlQuXMgEmwUJotN9kZTUWBi6mv27Kzutex63FCDUHgYXXGrexCPjf5pJa_-X-b8o-HskVGgunV_vSbj5Si2vNxoXq2sFTUwoQPiiQ9-feXInxj4JxSf6TrBL8lHiif92Sk3RhqcXsn3C7TitMRHqo2HipHRZ6g6xP4IWCIC34HzrNLQvbt9jw0S_m6oELkKgse-DqzbafYhmXikYLz3BBPjgbEc40Xq5Ap7F0YGULgftJUJdLoe162j4xvnmgCAExRvaELf7pRKNOExKV0qbgs_Dw592q2YNK00bKYmIQzy8DgkzlXrS0XyCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان بورس: مجمع هلدینگ خلیج فارس فورا برگزار شود
🔹
سازمان بورس در نامه‌ای به مدیران هلدینگ خلیج فارس تاکید کرد، ظرف حداکثر ۳ روز کاری از تاریخ ۱۴ مرداد، تشریفات قانونی و دعوت سهام‌داران برای انتخاب اعضای هیئت‌مدیره را از طریق کدال را انجام دهد.
🔹
هلدینگ…</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/456705" target="_blank">📅 09:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456704">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خنثی‌سازی مهمات عمل‌نکرده در بوشهر
🔹
فرماندار بوشهر: خنثی‌سازی مهمات عمل‌نکرده در محدودهٔ پایگاه هوایی بوشهر تا ساعت ۱۲ امروز انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/456704" target="_blank">📅 09:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456703">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYn5Lycv2NIGmEkhOPmm1jOatzMBjzfLncrGYkmwjIiXYakg3HWCXt3IO9DaJfibtPy-cCjNW8p4C95na9GmHGdnCxqXENv6-AT1-L0yViRn8c1tcXjtk1ARX_CP4pIe0AYAFxLX-hZBopHrgD2qYNu0HWsQxFAkpRxe1CvBWkfPRVfAO0DHVKZYzdqgTvqiI1ZIStUh1G0gU0kimsuXrDnJ9KLenpiaqZPJQIGbS3mXmORy1jk0PtScz0V52-aw3awtR0rLd9jdmQDuR5CVNUunTAYk0OAg67ZZpgYgc1Huvs62XwSq_eV6QcAOnqh1p5KgaEt7KIluwKhsOSa16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچنان
بخشی از سود سهام عدالت ۱۴۰۳ پرداخت نشده است
🔹
براساس اعلام شرکت سپرده‌گذاری مرکزی، بخشی از سود عملکرد سال ۱۴۰۳ شرکت‌های سرمایه‌پذیر سهام عدالت هنوز به حساب این شرکت واریز نشده و در نتیجه پرداخت سود عملکرد ۱۴۰۴ نیز فعلا در دستور کار نیست.
🔹
شورای‌عالی بورس هنوز مصوبه‌ای برای جمع‌آوری سود سال ۱۴۰۴ صادر نکرده و شرکت‌ها نیز مبالغ قابل‌توجهی بابت این سود واریز نکرده‌اند.
🔸
این درحالی‌‎ست که برخی رسانه‌ها هفتهٔ قبل خبری به‌نقل از یک مقام اتاق بازرگانی منتشر کرده بودند که قرار است تا آخر شهریور قسمتی از سود سهام ۱۴۰۴ پرداخت شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/456703" target="_blank">📅 09:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456702">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c73f6e2b3.mp4?token=oWZ0VICJTMSxrmoA-pgV5ZjN7NGba0SjIuDS5TtdEi8KStuQX2BRHgZB4y-7EBaOfgFFOiM3GWPDAiX_h-yHvjOVQRrGslEyNlaND2p6a8WoDRZJ3iKdw3j8yA8eJ5jLjWLm7yGZ33g3hSATrZM4uZeVu6lgh1TvaWjftspjKDcAmu-Vu28aife3HEdr_ABbNdzqNoI4V7KljFoTyS-nUrViWeIn1iZfnwAtFmGVltYS-Qaf2X2PwLOXDNo6BfEOxwjJJGSsvmcR7Pkck4jo3TJDTcPojpdrdIOAXqWpvPwEGCWUaqChkfVarcMyD4iyq6ecHp4GSJhJLJCjjzcWew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c73f6e2b3.mp4?token=oWZ0VICJTMSxrmoA-pgV5ZjN7NGba0SjIuDS5TtdEi8KStuQX2BRHgZB4y-7EBaOfgFFOiM3GWPDAiX_h-yHvjOVQRrGslEyNlaND2p6a8WoDRZJ3iKdw3j8yA8eJ5jLjWLm7yGZ33g3hSATrZM4uZeVu6lgh1TvaWjftspjKDcAmu-Vu28aife3HEdr_ABbNdzqNoI4V7KljFoTyS-nUrViWeIn1iZfnwAtFmGVltYS-Qaf2X2PwLOXDNo6BfEOxwjJJGSsvmcR7Pkck4jo3TJDTcPojpdrdIOAXqWpvPwEGCWUaqChkfVarcMyD4iyq6ecHp4GSJhJLJCjjzcWew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاخت‌وتاز کَل و بزهای وحشی در ارتفاعات طارم قزوین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/456702" target="_blank">📅 09:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456701">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قالیباف فردا به عراق می‌رود
🔹
رئیس‌مجلس با هدف گفت‌وگو دربارۀ تحولات منطقه، تقویت همکاری‌های راهبردی تهران و بغداد و بررسی راهکارهای مشترک برای کمک به برقراری ثبات و امنیت در غرب آسیا صبح فردا عازم عراق خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/456701" target="_blank">📅 09:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456700">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
حملات به فرودگاه نظامی سوریه؛ اسرائیل مظنون اصلی
🔹
برخی منابع سوری در خبری تائید نشده گزارش دادند که هواپیماهای رژیم صهیونیستی به باند فرودگاه نظامی ابوالظهور در استان ادلب حمله کردند.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/456700" target="_blank">📅 08:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456699">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3d77bd4c8.mp4?token=M-V2GdhcEsMz5UI55F2aLl8ajaFcw7koHnKsRizV55C2I1oS505njydZQvySqEgCV4IcawVSCL_rxKeNjHNWIoOhANPaCzqiDPp4dgn3om0cmclJqJO7Ih0D534RbxhExiY6ii50oBoOosPR6WCYzkwjnFtfII8NsoHRfRIyV3goDt8mQ8g0H0V2XmDh549PDdap2UINcml-HXEP-8rwmQxHp5i0eNaKPyOiCcIUo-HZ5hhC93pfm7QUPiQQ81DOUPiXZK72Vesb7hHbfMqIXEfAL3WhwlNJnM8YS-ObiPkznpdeHkqB-JD5mzgto3CP6ykLZNRNQTYeDN7vr9Cc6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3d77bd4c8.mp4?token=M-V2GdhcEsMz5UI55F2aLl8ajaFcw7koHnKsRizV55C2I1oS505njydZQvySqEgCV4IcawVSCL_rxKeNjHNWIoOhANPaCzqiDPp4dgn3om0cmclJqJO7Ih0D534RbxhExiY6ii50oBoOosPR6WCYzkwjnFtfII8NsoHRfRIyV3goDt8mQ8g0H0V2XmDh549PDdap2UINcml-HXEP-8rwmQxHp5i0eNaKPyOiCcIUo-HZ5hhC93pfm7QUPiQQ81DOUPiXZK72Vesb7hHbfMqIXEfAL3WhwlNJnM8YS-ObiPkznpdeHkqB-JD5mzgto3CP6ykLZNRNQTYeDN7vr9Cc6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور وزیر علوم در خبرگزاری فارس  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/456699" target="_blank">📅 08:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456698">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQcSwVAvs7dBYn-C7ja1CA1SeyDNjrv-GK8nww3AftKnK9HZTHMCO2H5mQf8NqP0-MvCXYfD_kNKtadOlhWQLlEa3fBLayaO09dssOxzEjKc6v8QfagKLRh-cu9ECJNm3TxeTQkUzflvrgMhLBAmIWQ5wxA5ldjWgx7anhp_xeSL5OET8iei6-0isIRKsKhEhz-_i1Ey2iLN0VxuvK9payZ983G4n1zm725la2HV-ojbejbjoy1g1AqF-A2xmb1EWuzNWlic4uegIUvDG52KC53zMCSZWQNBqE8rm1fLOs5E6cV3vswP-RyYa8zT1ua-3F7yZovxNGeZWkqaN6rPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیۀ آمریکایی‌ها به ایران در جنگ ۴۰ روزه
!
🔹
در میان بقایای جنگندۀ F-15 آمریکایی سرنگون‌شده در جنگ تحمیلی ۴۰ روزه، یک قبضه سلاح ویژۀ GAU-5A به‌دست آمده است.
🔹
آمریکا این سلاح را برای یکی از سخت‌ترین لحظات زندگی خلبانانش طراحی کرده است؛ لحظه‌ای که جنگنده از دست رفته و خلبان باید پس از اجکت(خروج اضطراری)، در منطقۀ دشمن برای زنده ماندن منتظر رسیدن نیروهای نجات بماند.
🔹
اکنون اما یکی از همین سلاح‌ها، به جای آنکه در دست خلبان آمریکایی پس از اجکت قرار بگیرد، از لاشۀ همان پرنده متجاوز به‌دست ایران رسیده است.
🔹
ماجرای GAU-5A برای ایران فقط به غنیمت گرفتن یک قبضه سلاح آمریکایی ختم نمی‌شود؛ اهمیت واقعی آن از جایی آغاز می‌شود که یک غنیمت میدان نبرد می‌تواند به منبعی برای شناخت فناوری دشمن تبدیل شود.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456698" target="_blank">📅 07:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456697">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حادثه برای کشتی باری در خروجی تنگۀ هرمز
🔹
طبق گزارش مرکز عملیات تجارت دریایی انگلیس، یک کشتی باری هنگام خروج از تنگۀ هرمز مورد اصابت یک پرتابۀ ناشناس قرار گرفته است.
🔹
این حمله به موتورخانۀ کشتی خسارت وارد کرده و منجر به مصدومیت یکی از خدمه نیز شده است.
🔹
به کشتی‌های دیگر در حال تردد در این منطقه هشدار داده شده است که با نهایت احتیاط حرکت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456697" target="_blank">📅 07:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456696">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d51d793f29.mp4?token=t6lcfJDTLkYKYk6ZhKlTaMSxvJss3nP5YIJpT0biRxVg3xl1SUSbomS6Vso0--0UhSsXQ5oRFPFbYDLiIOxYBJXSkPBacVDfLqRMNrRRhjE7uvVtATGOqAiQUKpKilJpz8roMwxNBDwn_3YUV3OMwG9dnAN2zsEOy17vUGO_rhm1FR1lqF7csESVeic7ilA5Tt0FSyRbfj9a3rVfC5VoNowAy4zsESTRUE9xOaNlf92xDOgDkSNvdsGI0zEMyXHhR6JzKCrdtvFcHcFzYbKDYWwQau67faD_XNNlZzwnNzDE_XOGugO6Fwa9Bi284uW4kyC6ldsh4J_nT-TURUDoAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d51d793f29.mp4?token=t6lcfJDTLkYKYk6ZhKlTaMSxvJss3nP5YIJpT0biRxVg3xl1SUSbomS6Vso0--0UhSsXQ5oRFPFbYDLiIOxYBJXSkPBacVDfLqRMNrRRhjE7uvVtATGOqAiQUKpKilJpz8roMwxNBDwn_3YUV3OMwG9dnAN2zsEOy17vUGO_rhm1FR1lqF7csESVeic7ilA5Tt0FSyRbfj9a3rVfC5VoNowAy4zsESTRUE9xOaNlf92xDOgDkSNvdsGI0zEMyXHhR6JzKCrdtvFcHcFzYbKDYWwQau67faD_XNNlZzwnNzDE_XOGugO6Fwa9Bi284uW4kyC6ldsh4J_nT-TURUDoAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی دانش‌آموز کلاس هفتمی در فیلیپین، ۲ کشته و ۹ زخمی برجای گذاشت
🔹
تیراندازی در مدرسه‌ای در شهر زامبوانگای فیلیپین، ۲ کشته و ۹ زخمی بر جای گذاشت. شاهدان می‌گویند مظنون یک دانش‌آموز کلاس هفتمی بوده که در کلاس درس تیراندازی کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/456696" target="_blank">📅 06:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456695">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">عملکرد دولت در اجرای طرح کالابرگ، در جلسۀ امروز مجلس بررسی می‌شود
🔹
مجلس امروز صحن علنی برگزار خواهد کرد، و بررسی عملکرد دولت در اجرای طرح کالابرگ، و کیفیت حمایت از معیشت و حفظ قدرت اقتصادی خانوارها در دستور کار است.
🔹
در این جلسه معاون رئیس‌جمهور و رئیس سازمان برنامه و بودجه، وزیر رفاه و رئیس کل بانک مرکزی حضور دارند.
🔹
همچنین سوال عباس بیگدلی نمایندۀ تاکستان از غلامرضا نوری قزلجه وزیر جهاد کشاورزی هم در دستور کار صحن مجلس قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456695" target="_blank">📅 06:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456693">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4PUSxEzE1s-hKcFMX8CEhcfQdoCeG0YXtq-_Yc3ieDejYe9lSR12npnMJiqSA92pNY6bFBoqV8isk1JLvmMNF1qE1qsBAvORY3BTOVfPX2xexOA6ugdKomrqNOLQ1QyGso1lTLoIkNcrFxE-REV4MrUV5RYk-OTBzAVsKFdj-ZBDom43Ekv5fQXVuF_pyfL0OaLkLnElomXpO9bePyio-AmjqO-ZQRPPr9c1PdI2aNflyz1DE8T0SLZYAQg1YEyoFxfC4fY1pbbpUQHWIsJWYv3MhO0cCfBWc7E1Z7TDVn7xjIKH5YCcQxQxYjEXhsEEDtdEv2Ir-XtvIWpiayBFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SquSkySNvlov4IS1lmYgFKP6GYK52TUSYny_X6iufse2khWwjCrVy5K3YqeOVc9DMIyiqlvDCrm4mrmt7Cn54uU5esU6xkRlI0cPcbnIgYNDCdAKbasbI-TqNYD5VAxPnYg_dCG366thv6r9CEy9oHn1z6puUYmrMVQheXlUs-J-OQa5y2jdYJTc-B6WJLdA1L6Rup1T7bk6cwsgRbUbKJhToSGMGC2Df-GEXOFPGZ36sWgoqy2mGVCg7tdvm7Cb1G2dejp4UC6dQ5jaf5mBrZc1aVJtB7FfiWo6IWVKpE1xnKgYulljPJNqyg1LPZomtG9cCqJSoU5FVX0EW7U48A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان
🔹
دقایقی پیش، جنگنده‌های رژیم صهیونیستی مناطق المنصوری و دیرسریان در جنوب لبنان را هدف قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/456693" target="_blank">📅 05:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456692">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ: اگر عمان در خصوص تنگهٔ هرمز مانع‌تراشی کند، ما آن‌ها را به‌شدت بمباران خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/456692" target="_blank">📅 03:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456691">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0358a60431.mp4?token=nXMbIZPRLekYkdoMH5JzDCcjFcfOnqBoqOe77GP9xoRwW13ff-SZm5uNistSy54_6RKMYxuOVaJ_viXcqHX4AA51_C0KXDnPrj9q2nab1LtF1LHNDb--8ifNdLHJXpUJ1uyPbI08SDvuXCS8ml8Y4Gy2ZXNWUy7EuuCGsg6epaxsquXKnp-vlyEg592Y0E-DYTj_SRnVpUoS97O_W5ajl8AnkFJ7kXaRgdIPkch8NAcwyFv5r99HU89lN1OHEr8TpcNIQupm10vbnB_9czI5DjC7dmYZGQWMYalhNutN3-oIkYEYVKKR2QU3y_wUJR0gUBSyZ6lRjh97iGwk2QTOmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0358a60431.mp4?token=nXMbIZPRLekYkdoMH5JzDCcjFcfOnqBoqOe77GP9xoRwW13ff-SZm5uNistSy54_6RKMYxuOVaJ_viXcqHX4AA51_C0KXDnPrj9q2nab1LtF1LHNDb--8ifNdLHJXpUJ1uyPbI08SDvuXCS8ml8Y4Gy2ZXNWUy7EuuCGsg6epaxsquXKnp-vlyEg592Y0E-DYTj_SRnVpUoS97O_W5ajl8AnkFJ7kXaRgdIPkch8NAcwyFv5r99HU89lN1OHEr8TpcNIQupm10vbnB_9czI5DjC7dmYZGQWMYalhNutN3-oIkYEYVKKR2QU3y_wUJR0gUBSyZ6lRjh97iGwk2QTOmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ربات «سوپرمن» اینجاست!
🔹
یک شرکت چینی از ربات انسان‌نمای پرسرعت «سوپرمن» رونمایی کرده که می‌تواند ۲ متر به‌صورت ایستاده بپرد و به سرعت ۱۲.۶۶ متر بر ثانیه، معادل حدود ۴۵ کیلومتر بر ساعت، برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/456691" target="_blank">📅 03:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456690">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b94475dc.mp4?token=najKimPk3jyYx2rn_TrMI1Pu7on8_p58H5a1c4hOCns6zVJiulepntGtGNKdfUXm1ulTH3WQ9DADdd3Cp8M-GAWgK3dDvD4PgdaKhNFYFT--9-USb3xUm45fyQOtGC4MLV8M5XX66Kp3sKp2lnhDGSO2QfK-jzo8G4dqwBeo81w6mxHcxVofAgaMoiWgwGY2fIIshmedqmJltq2JMIVNQXjrrVKXwcWXZCqsXZkAAp5G_a4SvDBFU-K7zxuIVysF3Hec8-ZKWuDKQVtTYlOws82nC48Ui7NepVQqIDhbkDqW7nTwRVVmXJ6jfOxdCHnpiPVgT9WBSWWx-qW40uGXYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b94475dc.mp4?token=najKimPk3jyYx2rn_TrMI1Pu7on8_p58H5a1c4hOCns6zVJiulepntGtGNKdfUXm1ulTH3WQ9DADdd3Cp8M-GAWgK3dDvD4PgdaKhNFYFT--9-USb3xUm45fyQOtGC4MLV8M5XX66Kp3sKp2lnhDGSO2QfK-jzo8G4dqwBeo81w6mxHcxVofAgaMoiWgwGY2fIIshmedqmJltq2JMIVNQXjrrVKXwcWXZCqsXZkAAp5G_a4SvDBFU-K7zxuIVysF3Hec8-ZKWuDKQVtTYlOws82nC48Ui7NepVQqIDhbkDqW7nTwRVVmXJ6jfOxdCHnpiPVgT9WBSWWx-qW40uGXYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای خودت با یک شوخی بی‌جا شر درست نکن
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/456690" target="_blank">📅 02:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456689">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qey2LlM6f-Eeh1jtS4Y7O1xhUKo2tJvxfEm7NMtLaTspdS4kw1Y-UYHX1ENvGvnliE94twTyGfDb4iGsYqkL-6HoaXs302LOjwDKXNxcXKaqtQfk0ErWFUmNamRogcZSR_urp2w37AxKyi6alOB04vQDv5qJv7XGzbKd0b2n09CMACfl4S1CqwF1rQ45hZc-8hKjqzg5wv91uYEaFis1cbBlVsHqakUU9Nxqvn5a7Qp3aMHovvF-IFGDeRKUU0da-8zhFqQN2ffWc0DAbNogL24eDU1sugC-RbxSgx9kyJQZeosmLhHbYhcI6hn3b6atCfZMhac0DppdlK-6b9_EpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط کتائب حزب‌الله برای همکاری با دولت عراق
🔹
مسئول امنیتی گروه مقاومت کتائب حزب‌الله عراق ۴ شرط برای هرگونه تعامل با دولت بغداد تعیین کرد:
🔸
خروج نیروهای اشغالگر آمریکایی از عراق و تضمین عدم بازگشت آن‌ها
🔹
رهایی تصمیم‌گیری‌های سیاسی و اقتصادی از سلطۀ آمریکا
🔸
خروج نیروهای ترکیه از شمال عراق
🔹
انحلال نیروهای پیشمرگ منطقۀ کردستان
🔹
این مقام حزب‌الله، نخست‌وزیر عراق را تهدید کرد که در صورت ادامۀ اقدامات خصمانه علیه این گروه مقاومت، اقدامات تلافی‌جویانه انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/456689" target="_blank">📅 01:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456688">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3ae134ef8.mp4?token=MO_0YG3vGPllWP5SAETou90XQ9fZyAizXJPuc83G4WXFRJozniCkWwMxDH40JYA1g5ampjFMfrW9gkG003Ym3FYCXPfkrN22dKUHs-WBshTAWcFPmdSAY4c_JfuP8puA5hc-F7WOKSasAFOUFhc18SrDZdnewzD39JFwg5S0_g_I60mw-PoKtzK4_iUmIa9wh8vuK0KHWEWrT_yzX9vXDUpvUOxqacZQE_ppWmoRaS7W5VoS5K38aDi93pSTRt4xMwjaBEYHTzCIxK4DhB3qirx1_T6ABFR3eLUNo4wFlOvzkS8oMr1J4RRgen6FnjT-m9wKelvZBgs0uJFVjB8WYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3ae134ef8.mp4?token=MO_0YG3vGPllWP5SAETou90XQ9fZyAizXJPuc83G4WXFRJozniCkWwMxDH40JYA1g5ampjFMfrW9gkG003Ym3FYCXPfkrN22dKUHs-WBshTAWcFPmdSAY4c_JfuP8puA5hc-F7WOKSasAFOUFhc18SrDZdnewzD39JFwg5S0_g_I60mw-PoKtzK4_iUmIa9wh8vuK0KHWEWrT_yzX9vXDUpvUOxqacZQE_ppWmoRaS7W5VoS5K38aDi93pSTRt4xMwjaBEYHTzCIxK4DhB3qirx1_T6ABFR3eLUNo4wFlOvzkS8oMr1J4RRgen6FnjT-m9wKelvZBgs0uJFVjB8WYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار مخزن سوخت در کردستان عراق
🔹
منابع محلی از آتش‌سوزی و انفجار یک مخزن سوخت در سلیمانیۀ عراق گزارش می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456688" target="_blank">📅 01:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456687">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">گفت‌وگوی اردوغان و ترامپ دربارۀ ایران
🔹
رئیس‌جمهور ترکیه بامداد سه‌شنبه در تماس تلفنی با همتای آمریکایی، ضمن تاکید بر اهمیت ادامۀ مذاکرات با ایران، آمادگی آنکارا برای مشارکت در این روند را اعلام کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456687" target="_blank">📅 01:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456682">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfa0dlubhJuk3SbwASLHxg4cABuSAFRxt9cVZzsH6X5jWJ5g4A_LpW-0jz8X0tiW82mnycqZtpfiyTxNH0ULJlrpLnZlYzPalCMLSzjX9nrVMUQGQc4GevrWhIESWTtcXXw0hyZ1BKKhbw6AiJprTVeNov6LnXnF8nqwU-DGPy_xxLtcc1VZBpGxWHMRUT7Ho_OGDNfHRZFiBnbgguDYE0Xju1VBpGs2omFCtS_QSWZdYP2eZYiZr_Bf_iTC_FMr8t__C8jqaLRqrvDdk0X2GmL4_-qf-cKvcXJmvbUIM9kmVs3ZJ6CnvmlCK7UZQaNMzKPL1myk_jSmxts9a0Hlyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZvD0hQ4vM5cvXiAvA0J_GA3Q-e8pif9F7-jyMs_Cde6t8D24zO10zuD59A45-e3ISyp5ImDrVwva2Cc3FnsCTUpGfg8gCS0rR0W2INjpvATKgNaqyIDGrDJzswO9yH3PwoOPDsrGDrVk4pTwq5C0OzuF3e6VZIQbRe-lcuyqAqMV4UzsBdiYnbgc73-UmjEdZ_OZUoBnXv0q7QZIJy0FTTWGeSxklL95f3HfrmiLni0GmMAG2woq7HmBRkdNYoE3UTjgfOy6Vyb5iPSxzK113fV6ZGIsDfdbURhMVISioqf-JT7hL0PsioLoiGhWFivAiLeOs65jmSlwHGg3j-yFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F464te7C1LPN3mDFu5-N6c64pTl2zDlTs8TtwmDxWiXdiX5my4RUgRZvHz_n22H5T7_PkD3FqivcHzgbDlFlRnS_ygVFh330evQyYFJ7Nv1d4rvUwXjKJ73JtLvZ50kDEveyZvfs9_DY5GQTbwzfcZSB-wMt-bonWEfXY_XyH863e5AkQGqZoj6ZZ-g-HXJQkjwUe2oVgaZQshLuMR-nTPQh4dVYatd-c-xoDFz6Y5zGkXhuHJ0zfCujP_83cAooVca1hBly1M0LjYNt2K1oLtPUegOpp5AQeCeZkFST9ZN7ZFMsqcZL2IevRHZcuGog5djP1SSX1yaGIqQg0zABRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EeLLmfY8A0cCPL-1WSuR7urfD9AUhHEwWUOV94Zuvz52cIqckrvO7X16P3ghgsnd47u9W2yTlLyF85q7kZfgJp6Ooc4sIMsNL6ByYBcY0xRxeVZrIkt1CrgVVS_Tt1WDbw5Pi6fSYcq--bpvmK5ii2TesTmPjwGr22blU_C-nG5XOLoNW9Zxp4x40vZGZDJXH1ws2FN0AfaNAj0pBABs447pedmtGex__ARa_X5w2JGfRiGpQrqSND8rR3RSnUJ2ODTByzEM3v5juhuBTL6dAME571AA1se8-qNaA7m0Fao98gSDYVuWlTZU8-L3plDPPP9psRRDH00eUSwyYTHrEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvtbNmSRB0Ma-PyjXDcQTSBkgBmy03pg56T6SwaPA-QQfcXa6eoTlblWcrMSX_UfQo_hASBqwUZGAUWUat9Od4Fue6Zm_i1Kxq4Eq4aBBUIzDKiGFGJptrFU2R66ynZzhnPQaLHQuyMUnZS4qeDLUmxYtY9YyHpbvKkIXMnlYaJ8n8z74jdoJsiYdCnGBGGeZe9yHCC66fwvEDolWhKsX8CXZz8iFhTa0Dwl9EEr_WGss_bkfb4fNMIBGf48Q7j_3H8jRpgGWl78pxQ8ciBWgYl6AnqpvG1IhhaMFO5WXxmVGEeS8YGHHMxDEk2mOx58_W993xYQDwkkJhqIQcS65Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
آغاز محفل اربعین قرآنی‌ترین رهبر جهان اسلام در مشهد  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/456682" target="_blank">📅 01:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456681">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجار مخزن سوخت در کردستان عراق
🔹
منابع محلی از آتش‌سوزی و انفجار یک مخزن سوخت در سلیمانیۀ عراق گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456681" target="_blank">📅 01:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456680">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhOJNcXKLdg-xH__ToUZ6ogin-KTWSdN6VvTZDC0Lyh7c5P4dKCKOvkwuGl4uhJbwsoa4uwQ_K9wUQsL6fTBrJ_y-baQCE0pTwvF4utImn-ARLFf6_l8CdrjUf4A-34CbJdNh-VFYMl0bltqxeOfbC5bjar8tLB0oVBWIGcN9smGNA87JVb7pWR-XKenSjcECTzPSkYExvhRiSSWusYhgcUibnqrPuUz3EiB0esw6CkLbaX9XULQ5NZPSLJzZIHpIfy02DTfQEmQjZ69CfkmGeC_5355nxFN0uIHSjwHrt6ivXHx2o_wacO81ykUDAbW_zagSbW_HreFaAo_HmWnSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی حامل سلاح عربستان در باب‌المندب منفجر شد
🔹
یک فروند کشتی باری با پرچم اندونزی در منطقۀ راهبردی باب‌المندب، واقع در جنوب یمن مورد حمله قرار گرفت.
🔹
این حمله در حالی رخ داد که کشتی مذکور در همان اسکله‌ای پهلو گرفته بود که پیشتر نیز هدف حملات مشابه یمنی‌ها قرار گرفته بود.
🔹
یمن اعلام کرد این شناور حامل تجهیزات و محموله‌های نظامی متعلق به عربستان سعودی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/456680" target="_blank">📅 01:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456675">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7Q1FZo1FT8JTTL9J6-d-G3GX8Jgwq6MavTi0CXbdbgFURqWEpqJMQLoU0UvjjVRLa5EQFd7MCphInzWil8GkoCw15BxykQpqEzDEUDNPIqKU2A00HDQKh4aQVcEQX7Z49GumGaDmyf2l7XM9j4tW55uwwDIdOGWyZ_wx8sB5hqdSuct24uJh-_H5bnaIOIbz5DXQIuMMiZgC0ZWjIGXjaW67Zj9q61s6iJx1yQ_IB3rh4UEtXP2XsQpEWrmcTzIyFFmhWMBjOdgnaNxcTix_FNondEnYQ5L9jKMLMEvb2Llhmx9vZF-ZgAurrj4VRfO_49IV0Vtc8K4uyfai33ujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RUjWcxbmVkcHtY8yli2Fv1g4ePOgruARdwjx5DgqWhmmxY5zXmmeHIxAVIlhyiKJ6g09quJapQi_3Wd4YLEpt-XEXe6_GhqUFgA8-488Pw4rz-qPRlSoRimGj0SIUH9lgZv7uXwdEPoHdFvFB80rNdkjTmHcW3V1FXunNP4rpP2PaaPtuwHClO64x4Dqym0TrtYXs65ObUtzZY5-mpUdaMSLvwApCbLrxMaNIGJogC9WzCVGBnVCrqCH7NctbdSoZw3sc2USqNJRmKLZ2IFhLjzGJdCLq1cuEIatOKubWQ8h7W5pfHLSUZbTYMj3oS4YGH-1Mx_GSVQ9wh9S9aFSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdhdOcbM8xCFaZSb51f_qYm6yRy8XiW4Eyo9Bhr2asaDrtJcVOuDhIDnWQPld3IbbCsE7XkzfopwUUtyln512dzlvhT9tim2AvJthyG7l2FbvuCiMSBna2cTOcgwQhxaNkdfZoqxXYWyYzmitz8pYXqLteXNhXyMhq4xM41ivza5A8E-rxy1NRwkXQolkbEuFyvSRuxFN3JwZ0l9K3YapFBj7McrowJTt5Uk0Z1ckTtGlQ5ysM3nSiZfByAriZOJsZfgVGYNMlgsK9xA77c5aHjFsraa-toal-kOUBwQPgRo1EERF-ZsjxHQUyBZuTdNlTYpiVJfs2zFxtA4GWWHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OP5iGXou0cu6bEhQoa_Yv2SAE-vEZ5TM-8mFkjbTl4VVAL3LtupTF0t6hqmZO6v9sPinzQNvnkkv4IfdqIwTCdxYSjIsgLNYTNjDt8OQedWv7OqMX_3KLlTUF0qzTCLFRlLMuuYK1G61Kd5rdMBzxu5ycPN9yp35Rt5w-NYqzVbCkCEMjkdKPwBcxD4kPpJBMS8go5LEUJ7jHezOwuvrS7B5Iem0jFwaKFSBoBhp9qfdKk9pZG6-LgiodmeUrmNNXZjbk6cgBiGnFLjgvjpOnqZozHLlT-_wURtbSNzzQQXm-bdRA8VAfr_hbRTiaz_JKb4zRtnY76n_Syx-50sHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8ZLJzrsMVNGJena4ua7DJkB0Lv6L-ZM5G7f2uclYic4QkP-oWjqAs9jEQDwtteXgGMQp8ipNbBH9ZSsKfwpsAskkG2WIeuPFtF6e5OF22XsQkE5pePHEGci8838bno5p5Z75weY1emelvHT21z-LA2Lb-bQ-TeLx4peF-XvX7c0dRk1Dtsm1w10RKcacxTc9Z4MY9PgI5jBDxq8Lcz0wdGXnP96elVxl3wMVaePH118yUU3iu5BgMa9xuVfpz70DQ4CUlWEm9alEC4mqOPlm8o7LISoCITY706NV-cHiBNwAUq2YSqgAymr1P55Ib-r9a9HN0L_5WXNJ0MosqP6mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۲۷ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456675" target="_blank">📅 00:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456665">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNsqZ7XVUU6AzjHzaw1PEihKZcHca24YvTxcZVh9XmK8irLz00DYnKl6ljPje-vW6HjPIAEt61JckQcZ7ZOXcV-KiEYFWLqUYdoN7OlT74cS8J8YirhR0i2UzRdjFIZFP9FsOT4o1sYfe9f_X9hoCeiJH-8_yGHQINrodtiwi5aJVqnljAn12wd2_PgGybh6juRGmtm3zAkNkNKK2qghhBNnCGcBhEZXUaUHlt8_WJmquutqoiju24ZSSL1l-XHDNAtduNoAYSIQLArXRCV6R_fd8y4r2QBpm5RZQ1RYtahbwY-fNDDzmKQw4wgPGTZOzizxfROMMpRC4VqvEL7c4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0txoe5uP5FM9XQXR1ajKJ8v4_UUCEuvmm0uv-P-ZxeFC4_z4MDcT8ko7u4sbO5ZoTlY55WOUsuI9WdNGLJlRYsqVGPX0CwgnzVCRTxZcNzHRqtxxBu-GhV2NmXrj7qXGug6kWocQQacfkJGIF3bbI-a3QL8JiQd0oBuuc-SrAeIcApzbcRo-0Z5bU0a4d5YtxO_ySa-qFW0TbTO0Vnnz1q2SdveySeycBTyHXVR6f8h23pn-d_tbpmQ_bTNa6xUQMnrdvV1WHN8-WdRKKFYgRcCdYyvni1uoI0t_ue7rOC5m1wni7R-WErnretLOiduzDr7M4Cs73PFCnJlabTDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FURurWQ4PKesmRap_Fsni_8RS1Xi2b3lA-hryzgNBHB9h8m36OreEUTD6LKwFEcfs8UsUrEZc0HkpGUhgEuhD_i8Vcw6Esjk3iSht38SY_0CaETMHWzbdakMOVL7SC6EAeRs-93D37MNGmrwGEgw9qPgltiLSHHYdp0JhmUl3YlIU8sti-qemFcWtsjGG64-TNBpWkZUXEvttFzh5VVMViuE8HuIPlIvi7tDpIVpxyZGFHa4GQsDpfHP8govqGK0oxGRAy3IpLfY3ghyWtNtmlZDe7JUv1NuMfDlpDyuSQwJcdKeHzICnnER5r7f99aXgN5nTGF8NE4A36NfOK4u2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxwWLPUOEJeMfUStlBjco8AwZpYsOHDMGKS0zDm915V1ZSC2prQPvm91aqkIjWeO5mYaPoGK-gAhhK2Ox7FNQa67U9L0YHXFK1eQrg9KudahY26na4r1I2xBOkYcZHI3Ew_cwQRuR775k8DZI9IrAMPzscjlugGP9bad8BSN9CmhIYYe4LWOgbbqVMbkGVZ1Muf1lzcjY93bcyFnHLOqywUtoY0AMYVmgL8wEUq2f9GO2DlK1jP1bayUMBqGd1PQuCBRvcQWlnQTj6THaP57lYAYP8DwdNPrRE_h73Xfif5rWwUucX4YQRR40ak3eafa346FkyY9cIihIGWuGA565A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/biIm8pnIgWrAILv98h_1QEIavbzxPwZ_8LJQPf5oF2RR6I2C4rjcYfElbTBrgHHdhBy0nig48t7eHAwLnDuIETzzjqo_bf36ZmPXqxZQjxlkUKois1B9eAx7-J5_0OfE1vSKZF42QUoNAS-zbK90Cazoeiv4F9uO2gvfe1LBDb7DByRFS3iv3aZU4ZfZq7MHI493IScD0KjPLVBGxso0R7tqVjHYloMXV36eoDttFAOuGls2YPt0UjkHMNrJPvRItuLPvM3NjA-uU4KpO5pgllYgvWVjLFaN8vKD1117kehgI61Y4Z0QKwgNcniJBNFdxqYxlEf-Fc1nqhSUEd7Jtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6uiE0kstXYCVNYxEIGjyZG5vqeQ9Ymr-xOlTzFm59ZN-g7dvsM-IkpfECxmKuZkFiatr-WitOpRioExxQufcF8Vn0XCdxPM_ExInEJAAKPZKaTZbwOOsJLecfbFfqZgg6gDGqWtcN_-VfBls4HmqocxyrO1i_xwMlorj6FW7ZZ_9NmwrSdZxTFr5Vpq9HSls1dlm5EZp4xgnNpwbV4d4nxXgUbTAdnmkFUaikXh6K_xX8yj7TmxowboETg-etdvfozWJ7jwd_Tc0eUtB1n659kgIVsoSo4Zp7gpnMZUzLwu0rs_1p-GevBh0iIEGOalz_ilnaAlJTYG8iAGSUAdCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTeXflu3BX8b5XuE6JwE9safTOeGE83GkC9LDLPQBf0PtVe-DxCyXyhlF80bOGgKhtN6v2-RcYcn-5VS7PfNgp8b6dO6ETwvE4ybWw1Z9PH4XoH9llOYxG0Ue5VUwMDa71QnR4Vlxw3gijpfzbaz1aJovyRUL_jVqyRAoUva2IevUlPRnXNuQdRZuVXoxOS-fHIita_992z598l4WJ91n-_5WJvVMwmxkh4WKfiGgrJw8Q4fPKY-aRar-dZkz65D5vvLgEw7V4FQhCEeAvSDaKDvkzi0hEZP4S_aDXihchDwWpWrlge9KUgzEH8DBSj5Zqzgy6kjU0X0sVhBtTcA_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RDB9guajub_A-WqYKz3mUnmO5SsTBWeqyksbtPVzkCGF62CIcADow1HKBLtMgJ5gyHvCDigvbHdVXENd5oFsJ-QqcDyaQDL0oE_nt8QbptNPX9_bVkZA89cyQv3EEmWv1cCxBS0y47yspchn39UXNMAH0v69I7qgSEJ6GMzJnpdHe5cCYsyVRrOTGme24MagBD_mW_EvjztI3rKsirW_G-9iiWsoJVldIclQm4QZtd_rSlC7D6Fe05WfsGzwyeaCXGVdfdf2Xdw2bK28G2-YH2R-4mV-P16gYatSgLLRuZxePXHBaVbXd4hErX5Db8ytQTPylIl_xVOmPy1qoiITlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijT4k8cnhVlAMRlM4XH-fW1c5psP6ui-2cbj2mMHGw1YmMcjSpLGXk8HKRCMSCe_ROs65hTThxRSK4gVyjmW78mJKIUPvX0LVR_dRXqweyZyeGrSTWf0-hfZjRxC9agtB0SI2q6O_PbdpfdO2JUUJyI-xGWrpsyhtpT2B9oEkjB4wSzZzdVCrwaa4YiG1s8I4RDCc6QhV08FO_As6BVEsW_I3nNKwYu06HwWnMT6-XztrGlr2FfIy1dRPXfxQ4jn8owngyMci6HZmnWHHovY5Dn-wCpA8Vb5Qj_iEzoeIvNwSO_KvbYw-9Xhn-u-lt6yXMUAhXFcwm8k4FcraRDN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inVBO7iTgwOEoT7p5SN0diWltfJ7FxnTcrr6ytlbGjXfiPw03uSaTJryUsVKut78BFZ8nmwysZDE40lEbuTO9HkYPPZxUOzhB9ow_m3rv9J9QVot4Hj8dVge5Ay3P9DZY29yjHkNu1gZbR40DsEvXTps5d8ztqPwaNIZTPDr2-BQjfhQ3Wt-g0lzeHznRU6IJPtijsAOVvVamm4pIfIjq9mhxeeoODaTA3QiqqVdqi29lrs3ises7hacMhoSTczo_Cl4OLBnen-t0WSeq1atHg_LkmPn8LsURedUcwTg-xdGj1b4ct4ve_qXwDLneHw_xlbTCCevHhsC7OIlFixRQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456665" target="_blank">📅 00:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456664">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حق انتخاب میزبان آسیایی از استقلال گرفته شد
🔹
کنفدراسیون فوتبال آسیا اعلام کرد که مهلت باشگاه استقلال برای معرفی ورزشگاه میزبانی در رقابت‌های لیگ نخبگان آسیا به پایان رسیده و AFC تکلیف استادیوم میزبان مسابقات آبی‌پوشان را روشن خواهد کرد.
🔹
باشگاه استقلال در نظر داشت ورزشگاه بصره را به عنوان میزبان رقابت‌های خود معرفی کند و انتخاب گزینۀ ازبکستان را نیز در صورت منتقی شدن عراق، در دستور کار قرار داده بود. با این حال نه فدراسیون عراق و نه ازبکستان تایید نهایی لازم برای میزبانی استقلال را در مهلت مقرر ندادند.
🔹
گفتنی است تراکتور، کشور عمان و گل‌گهر، تاجیکستان را به عنوان کشور ثالث برای میزبانی مسابقات آسیایی خود معرفی کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/456664" target="_blank">📅 00:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456663">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87ecf94de.mp4?token=FBgzMVKb_HMB4NyR5TeLtlfpPZu-5HPnoInzropynSO33CFbDf_kHeN2ayhAQAVOsEIZCx1EtHJlTAL-rykJlQQ0ld541j1oOXZW4Pw3vQabRsmySdWRsGeFEksmk9RelHk8uXIxNRTA63_JQ8rx8r1Qd4lHtwWgZkWV1_A7MvvRA4pLoPE9ZO1eSHmmjduD-bwmR4OGuLxX9dtmr8XgWGPkop1dv2lp6FkZUU-H3S2e9YOgyWKEEHGHa4ZY0PZI3pATK7EE3s3SqgwbfKlPMyMYKSxz0ccpA85KJMiVcsrs7BsdaIyhxtlz0y4QfjY571GtEr2cyAeyzWoGt1n26BZZ2LarorqP2CXj6dYc5hjf49n1-xOcz76zj92DiaGl4e9KoNmlvlmKq6UvALGi28ypSVQ57vlMD6UkmV_EHZNOSxpqtL1oBOKmXEpudVlTP6P2Ow9Z92QUAopjgyLsMa9zH6d41VvE8HKGQ-LRXZOl47kMacQihtC2qmTNYIrZvHXplptCGdh9S-KjTkLv-JvU6ObWHZSO1zkiqcrmFc3b1LHp_q4QO0gx1Qde2i2iW-ieabfhBwZmC9Pd3l6pTXslET7L8XeaiX6oTRWmZWkRV3ezQCm25fQ1ZC5wy0WB2pMDb3ujfMlKre2t4Kd2LlbwByrSI9x9P4zt46EFCjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87ecf94de.mp4?token=FBgzMVKb_HMB4NyR5TeLtlfpPZu-5HPnoInzropynSO33CFbDf_kHeN2ayhAQAVOsEIZCx1EtHJlTAL-rykJlQQ0ld541j1oOXZW4Pw3vQabRsmySdWRsGeFEksmk9RelHk8uXIxNRTA63_JQ8rx8r1Qd4lHtwWgZkWV1_A7MvvRA4pLoPE9ZO1eSHmmjduD-bwmR4OGuLxX9dtmr8XgWGPkop1dv2lp6FkZUU-H3S2e9YOgyWKEEHGHa4ZY0PZI3pATK7EE3s3SqgwbfKlPMyMYKSxz0ccpA85KJMiVcsrs7BsdaIyhxtlz0y4QfjY571GtEr2cyAeyzWoGt1n26BZZ2LarorqP2CXj6dYc5hjf49n1-xOcz76zj92DiaGl4e9KoNmlvlmKq6UvALGi28ypSVQ57vlMD6UkmV_EHZNOSxpqtL1oBOKmXEpudVlTP6P2Ow9Z92QUAopjgyLsMa9zH6d41VvE8HKGQ-LRXZOl47kMacQihtC2qmTNYIrZvHXplptCGdh9S-KjTkLv-JvU6ObWHZSO1zkiqcrmFc3b1LHp_q4QO0gx1Qde2i2iW-ieabfhBwZmC9Pd3l6pTXslET7L8XeaiX6oTRWmZWkRV3ezQCm25fQ1ZC5wy0WB2pMDb3ujfMlKre2t4Kd2LlbwByrSI9x9P4zt46EFCjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ تشکیل پروندهٔ قضایی برای آتش‌سوزی مغازه‌های میدان شهرداری گرگان
🔹
رئیس دادگستری گلستان: طبق بررسی‌های اولیه، علت احتمالی آتش‌سوزی در مغازه‌های قدیمی اطراف میدان شهرداری، اتصالات برق است.
🔹
با تشکیل پروندهٔ قضایی، علت دقیق آتش‌سوزی و مسئولیت احتمالی افراد…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456663" target="_blank">📅 00:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456662">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4504351748.mp4?token=D7ndEpQUF6KsUSwEv1KY2mBaBuitnWz0HLHR1V1j_eZoGuIJSHXya8jCoit3vhl5yUIwuuHLPXf-Pe9M0JMekeTimG8Xsw0xWhG5sdt4_MN7tdqbDVj2WbGZYKEkxWuGT8exnl2VWiGp_Alu6mm6xDu3_t4f6HPr24ui2TizqnxZ2J_z99Hm2mA6PcaObK6wK9_RGCoGiDmibjI0PkolH4WAW1G1shKNPB1cpwDxEqbhVgVDaqf1bAzHgjBpyapvf1l4W80mxHiTXY-6gKqYcTDLdUOoPeYbwQq45QfnFqlzOgjiDjE96qchJyq4a7Yddw-xzlObcGDeS1wMjjvp-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4504351748.mp4?token=D7ndEpQUF6KsUSwEv1KY2mBaBuitnWz0HLHR1V1j_eZoGuIJSHXya8jCoit3vhl5yUIwuuHLPXf-Pe9M0JMekeTimG8Xsw0xWhG5sdt4_MN7tdqbDVj2WbGZYKEkxWuGT8exnl2VWiGp_Alu6mm6xDu3_t4f6HPr24ui2TizqnxZ2J_z99Hm2mA6PcaObK6wK9_RGCoGiDmibjI0PkolH4WAW1G1shKNPB1cpwDxEqbhVgVDaqf1bAzHgjBpyapvf1l4W80mxHiTXY-6gKqYcTDLdUOoPeYbwQq45QfnFqlzOgjiDjE96qchJyq4a7Yddw-xzlObcGDeS1wMjjvp-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم دامغان: خیابان به خیابان می‌مانیم کف میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/456662" target="_blank">📅 23:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456661">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c893b286e.mp4?token=iyKWoWpLVMd_YJXi6r240QBw9b_Vi7i5EjJL8fEkhV31nQWTnvlPS0TSuL5jX4qAQuWUvW3acyB_XIgRfe72Dr8paloVB0CNj8dwCgTo0532dqZCltWmtc8hd1USLEDmg1hlBUW8q03gvcE-2rL40pOmZC1tfr3pqteYOl6J7RwZenLJ7FP-XyF_p1UXN0Rx4hYJz6sIb8Mz005SgaVpvLywplm-vaS4VY7_2IqvQXhvTgMI6YNhoFd96adk-vk6aGNMZlbXAFDYnX49WQyBS7SstbtIJSn_MQkYg_5XAsWeEhbNbKkOBXBOcfHo6cshaDJHMOlKou044J2YzwLUig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c893b286e.mp4?token=iyKWoWpLVMd_YJXi6r240QBw9b_Vi7i5EjJL8fEkhV31nQWTnvlPS0TSuL5jX4qAQuWUvW3acyB_XIgRfe72Dr8paloVB0CNj8dwCgTo0532dqZCltWmtc8hd1USLEDmg1hlBUW8q03gvcE-2rL40pOmZC1tfr3pqteYOl6J7RwZenLJ7FP-XyF_p1UXN0Rx4hYJz6sIb8Mz005SgaVpvLywplm-vaS4VY7_2IqvQXhvTgMI6YNhoFd96adk-vk6aGNMZlbXAFDYnX49WQyBS7SstbtIJSn_MQkYg_5XAsWeEhbNbKkOBXBOcfHo6cshaDJHMOlKou044J2YzwLUig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: ما خون‌خواه آقای شهید هستیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/456661" target="_blank">📅 23:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456659">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWrBzfwxPQ8Zzyax7u1SyjD_zoyLfpDYmhpnZQCforubkw_4w-Ht3UOseZYk9yZUpLbQxb4cZQwrs6cG3k6BvIEdpTlixs-B_6d6g1vVXOK47d0eAOtW4obJ7gktHg-0gk2Tlix1VFVBu6xuBO5d5dGc8tecPqaJM-LJf3ThOF7MsUWHbFeBCSgenKKTmESjhQyHWpAN9JNFrqBn42br6p76U10vu9isZYN0Qn1XqjeitiqtDb4heGYV11pKCRfVpUqEG1BtkqFLsEWpXw2SvHoK-ZnfOF1njrwIknNR1G-VrYbCAMXzyGCq-0bI1X9M54wuq6KaQHVgYTV8t78fOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b26d336c1.mp4?token=WvQ5kgtdVVFJz1PX98Brr7E_Y3G5kVepsyjUNVYZ1X9jiLSO9s7kZ5HwyWwmLXWt3Tm1Dp__Xi9W6u5ciH-iqr3qDPsoPtEqVYt8gv8xa6wB1upKdMf0bFhmSziHFe5pJj6Eca3Dh0x9NFyO-4QHYwgVK47Cw_KaRx_XqIxdCQrqB4cbbo7dsTjLLZYWhhBWAxX4Z6o9eAAcrT1r7hRGtvvVYxx8qQb-7FjgW2ppQq8g9IZcJsmmSPpHo-LeHrN5uy-W5MgrVS9FhLqgZAzECiteSFtehzMqpzxZiAw1kEI5qJBHYvlB9QKUfCc1iQidvhTdQWCS8cyeJy_CbvRogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b26d336c1.mp4?token=WvQ5kgtdVVFJz1PX98Brr7E_Y3G5kVepsyjUNVYZ1X9jiLSO9s7kZ5HwyWwmLXWt3Tm1Dp__Xi9W6u5ciH-iqr3qDPsoPtEqVYt8gv8xa6wB1upKdMf0bFhmSziHFe5pJj6Eca3Dh0x9NFyO-4QHYwgVK47Cw_KaRx_XqIxdCQrqB4cbbo7dsTjLLZYWhhBWAxX4Z6o9eAAcrT1r7hRGtvvVYxx8qQb-7FjgW2ppQq8g9IZcJsmmSPpHo-LeHrN5uy-W5MgrVS9FhLqgZAzECiteSFtehzMqpzxZiAw1kEI5qJBHYvlB9QKUfCc1iQidvhTdQWCS8cyeJy_CbvRogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از دست‌خط رهبر شهید بر صفحۀ اول قرآنی که هدیه داده بود
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456659" target="_blank">📅 23:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456658">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc3fd79f9.mp4?token=HQ0eo6wcWco5q0aO0wFN5vJTkEP3-K4N2zPGp5Luo0RPlLHUzwGMLTX-55iu2B4BjvoAAgaRQ6T9hWVKlv1ihuG_iQk3rkwNjYsKsCdYHzqa7KFcMcsmt5BSdzluDoaG2vxTsV81azWddmFgf47DXpfKgU_UQFey_KxqngMW99Z_ZVcd7EU4FsXiSem7XSgZ5Kj7Yld7TfkeWU96I5BMVUKvUYFd6iVLD7NdaVaZHuXF98_UQ-geD9WaZfBQnqbUeqC_AmISrvZ3S-rm5734H6hALjszoEhl74yG4CbMHxdkvPNvK9EJTWB9sSQ2VkoqUGAvRzJ7mf18Uzl4K3bEXjRTgobk8_32MOt30xt8x3Ufe_RdENr3g3bLMlXP6G-cHJRNosvW3KkzAzV1YRz1M215wffWhLwqdlmvjznieitbiPQZ4OQKPINrKzyYOsIUvWaurt9RCRqnNzgTwyRBF3S65piF-PCXGIvJOMbtAiWzcznyKKT6Ysp3Hb-3IobfrhsxU3_qwX21nvr7IT_cpWHLOtfeksZvQmxPKqykfaQ-d3sLD4IElzBMNy-lo21pKe4E3eKCXyV_qDJ4nkAUGpTqNjWrV0J0JKh7_2gKIFsa5usW5Tb4ipkupwL5t456ngb6GuDY6QGY_uZgzsEYPNZMUY02PXDlDDFepxRxIl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc3fd79f9.mp4?token=HQ0eo6wcWco5q0aO0wFN5vJTkEP3-K4N2zPGp5Luo0RPlLHUzwGMLTX-55iu2B4BjvoAAgaRQ6T9hWVKlv1ihuG_iQk3rkwNjYsKsCdYHzqa7KFcMcsmt5BSdzluDoaG2vxTsV81azWddmFgf47DXpfKgU_UQFey_KxqngMW99Z_ZVcd7EU4FsXiSem7XSgZ5Kj7Yld7TfkeWU96I5BMVUKvUYFd6iVLD7NdaVaZHuXF98_UQ-geD9WaZfBQnqbUeqC_AmISrvZ3S-rm5734H6hALjszoEhl74yG4CbMHxdkvPNvK9EJTWB9sSQ2VkoqUGAvRzJ7mf18Uzl4K3bEXjRTgobk8_32MOt30xt8x3Ufe_RdENr3g3bLMlXP6G-cHJRNosvW3KkzAzV1YRz1M215wffWhLwqdlmvjznieitbiPQZ4OQKPINrKzyYOsIUvWaurt9RCRqnNzgTwyRBF3S65piF-PCXGIvJOMbtAiWzcznyKKT6Ysp3Hb-3IobfrhsxU3_qwX21nvr7IT_cpWHLOtfeksZvQmxPKqykfaQ-d3sLD4IElzBMNy-lo21pKe4E3eKCXyV_qDJ4nkAUGpTqNjWrV0J0JKh7_2gKIFsa5usW5Tb4ipkupwL5t456ngb6GuDY6QGY_uZgzsEYPNZMUY02PXDlDDFepxRxIl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
ماجرای خادم امام رضا(ع) شدن عباس جدیدی با عنایت رهبر شهید انقلاب
@rahbari_plus</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456658" target="_blank">📅 23:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456657">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
کاشمری‌ها در ۱۷۰ شب ایستادگی، همچنان پای کار ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456657" target="_blank">📅 23:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456656">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e524f8bac.mp4?token=hsvAq7OdPgHAKV-6jZ2nL8tnLmlzAE8AipFyyOE8vuDfJAnmZjoW1BUcDKA4ZYjx058E8l5DdfUZjZ9cetrKnc4Hq2jgYT7Foyj9PVJmXmob9VsaJEeQIB_f_k9qShB-Q4waJ4np3WgwzI4hlaGloppxY3WiwvP34N4jKUlMztQYzIVV1_nfhsIwa5W563wTRPhKKKlQMfLPcLQws1HBCKqzwX3LBK9n5wg2DLJVE4hA-n-38E2sz_kEjkq1PtRSMYsIlPCdhNm-BC-5sGtOV7hKnP_viVr_lm7cKybiL55lyUif2hblh5l2Tnthr7_seWFPvXAVlmaM4zjOSkf9Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e524f8bac.mp4?token=hsvAq7OdPgHAKV-6jZ2nL8tnLmlzAE8AipFyyOE8vuDfJAnmZjoW1BUcDKA4ZYjx058E8l5DdfUZjZ9cetrKnc4Hq2jgYT7Foyj9PVJmXmob9VsaJEeQIB_f_k9qShB-Q4waJ4np3WgwzI4hlaGloppxY3WiwvP34N4jKUlMztQYzIVV1_nfhsIwa5W563wTRPhKKKlQMfLPcLQws1HBCKqzwX3LBK9n5wg2DLJVE4hA-n-38E2sz_kEjkq1PtRSMYsIlPCdhNm-BC-5sGtOV7hKnP_viVr_lm7cKybiL55lyUif2hblh5l2Tnthr7_seWFPvXAVlmaM4zjOSkf9Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای این روزهای بازار ماهی‌فروشان بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456656" target="_blank">📅 23:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456654">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06507043fc.mp4?token=uwKM3az9r46sNZPUoveVX56sM51oLG1kM4lAZMMYkGJdCi-DjTn1wftTylM9sNruZE1fonGaJ1-PfKZ-a1TR5iycfkc1uJRNf7qA7IIDbEFKvoPLs-gnpTsItwWXaullYy1P1lIXp9NMcgbAhL0vfgXqfQxR9CTKY2vw5Sv8lIyu6AvdDOztKHTlVZOn0SZ2qGwrMpV3j40F6N_lDH7by8UAjGGx16yImhdUysJ--a_eKNrxjeH1hdhsOgbe5r9qZwGr2hhJKdFP7UGfeDLm7lBP37dpr6IZMhuwWWJi8eJRhS7XgpSfhmuiL10WZyeNP1llnyFpX1-88XwsTmkvPXwFmn4RQ7qUZ925oz7kOoZBWlRJ8vwSFxlf3AFaTMXFYL_jIFmUrMAn-mgPamSmfkSaBs_ImUtcNPMDQaJBCYuQeoH7bUOkZjW24Tj4QW0tUrOvnM3SmdUupQYOsiKgY0Ix7bmViZWiQtiux1QdzRYZ8yQWgFkljFzE_e6n2A5YhILM9JPKRyNVg_RWCukCmBJTxXQrY5s6IHu_a_gUAF1Rqnfo-98yYejhvZOFJ0EyCYNB3yFjERt-O0T8ZF_Asj44lFaEQK-QxytrvWPgadPU8ee4IxUx5flGUaVfPw1iV_4U17yiBpBkOX8bDrLYiArbDJCw7Ikum0tekeJa3aU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06507043fc.mp4?token=uwKM3az9r46sNZPUoveVX56sM51oLG1kM4lAZMMYkGJdCi-DjTn1wftTylM9sNruZE1fonGaJ1-PfKZ-a1TR5iycfkc1uJRNf7qA7IIDbEFKvoPLs-gnpTsItwWXaullYy1P1lIXp9NMcgbAhL0vfgXqfQxR9CTKY2vw5Sv8lIyu6AvdDOztKHTlVZOn0SZ2qGwrMpV3j40F6N_lDH7by8UAjGGx16yImhdUysJ--a_eKNrxjeH1hdhsOgbe5r9qZwGr2hhJKdFP7UGfeDLm7lBP37dpr6IZMhuwWWJi8eJRhS7XgpSfhmuiL10WZyeNP1llnyFpX1-88XwsTmkvPXwFmn4RQ7qUZ925oz7kOoZBWlRJ8vwSFxlf3AFaTMXFYL_jIFmUrMAn-mgPamSmfkSaBs_ImUtcNPMDQaJBCYuQeoH7bUOkZjW24Tj4QW0tUrOvnM3SmdUupQYOsiKgY0Ix7bmViZWiQtiux1QdzRYZ8yQWgFkljFzE_e6n2A5YhILM9JPKRyNVg_RWCukCmBJTxXQrY5s6IHu_a_gUAF1Rqnfo-98yYejhvZOFJ0EyCYNB3yFjERt-O0T8ZF_Asj44lFaEQK-QxytrvWPgadPU8ee4IxUx5flGUaVfPw1iV_4U17yiBpBkOX8bDrLYiArbDJCw7Ikum0tekeJa3aU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات شنیدنی از هدف قرارگرفتن یک پهپاد MQ1 و ۲ پهپاد MQ9 در عملیات نجات خلبان آمریکایی   @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456654" target="_blank">📅 23:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456652">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71102e9aa6.mp4?token=pPETTkw2_-V1otVS-V6APV1tXanRkhE3NeiXGOtP3h7dODtupsnPW8_npJXuiJ9znSOAwIak39U_dUUKvTSLwlIbwlmjqSTV7kZai8bfdIeenZVFVE2uCR6iUfT1oa1CnvSg3ppfab-do8XCj8PO8lPIQeJGVOS_uZBtICrjyY4Lvxdn3zJhyWFGhwHaozd-qjy5WMsJV4CSolvp1KwNlI9qR6rg0Rci7Wh2B1dMN0MKk5XY4OWyhWtfrjgJGvC4OXtLBT4dio1uH6xhDvCd85-1KF5AcJTIahoN6bH65UflEwCnyXCeKyUy_99HCoZwq9N63rPCQSB8s9s4ZP3zFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71102e9aa6.mp4?token=pPETTkw2_-V1otVS-V6APV1tXanRkhE3NeiXGOtP3h7dODtupsnPW8_npJXuiJ9znSOAwIak39U_dUUKvTSLwlIbwlmjqSTV7kZai8bfdIeenZVFVE2uCR6iUfT1oa1CnvSg3ppfab-do8XCj8PO8lPIQeJGVOS_uZBtICrjyY4Lvxdn3zJhyWFGhwHaozd-qjy5WMsJV4CSolvp1KwNlI9qR6rg0Rci7Wh2B1dMN0MKk5XY4OWyhWtfrjgJGvC4OXtLBT4dio1uH6xhDvCd85-1KF5AcJTIahoN6bH65UflEwCnyXCeKyUy_99HCoZwq9N63rPCQSB8s9s4ZP3zFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر نزدیک از لاشه‌های موشک آمریکایی تاماهاوک
🔸
جزئیات شنیدنی از نحوه هدف قرار گرفتن موشک‌ها در آسمان ایران از زبان کارشناس پدافند هوایی سپاه پاسداران @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456652" target="_blank">📅 23:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456651">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48608c55e0.mp4?token=THCuzfczW1kF_T0P988xPV5IZufljtUwWJvzHeC9yUzntWQVr2j2zx2yUKWMfBbaRekp44m19DdB8BAOO0VTo7O_5ZOE4tBQIe6mucvto0x9dptuMRYcTEmorz3J7AVE8txIDyNcbIGAVuoXZ32hu4gWpNHU91Hv61ISThUHt6NlH_qNt4e5rVRmMVrsp8wgHrdjkQlDSY-v5sO2EWTMVcloqaz-I1yUrGfUG3EY59QJUVFCCtrs7d9Jo6wsDreLTBHKQx20kecTvPSLvsagd6Lw8pCkEPgEQDHoDxsFOVuWsLNImXB7jA4wE3tWCXcabd_Au8Nr0ocrw8NgFFdJBGmapW1OQlnYtf45J6vf7IeOrJc4gXvND5eCcPubJgGpYBpisYoB5oUcEjQza-H_e8tj36zLa2bQ9ZnsVorU9MUiv-v558k-Pzr_zZVYZvYSpm3_8_oLjFQszdos9uMofoziDRAOM7SWyH2TYwd0aIIctE-7T5gymnHANXeagvEcfqzdiJjH4K6xz3Gh9UaLeQdwk56nEfaTEKQRYAWzSZX15oI243nWw1MpofMESNJp8eUCOoo7Xpg7RgE1MFx3zOe7As8OpDM87wKM4EiKo4MSS34Ek7e5H6SmK0BY1vxBAr5cF82nxc6LSM4kFCvO8D36g0uaMEsTiz57msOFh-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48608c55e0.mp4?token=THCuzfczW1kF_T0P988xPV5IZufljtUwWJvzHeC9yUzntWQVr2j2zx2yUKWMfBbaRekp44m19DdB8BAOO0VTo7O_5ZOE4tBQIe6mucvto0x9dptuMRYcTEmorz3J7AVE8txIDyNcbIGAVuoXZ32hu4gWpNHU91Hv61ISThUHt6NlH_qNt4e5rVRmMVrsp8wgHrdjkQlDSY-v5sO2EWTMVcloqaz-I1yUrGfUG3EY59QJUVFCCtrs7d9Jo6wsDreLTBHKQx20kecTvPSLvsagd6Lw8pCkEPgEQDHoDxsFOVuWsLNImXB7jA4wE3tWCXcabd_Au8Nr0ocrw8NgFFdJBGmapW1OQlnYtf45J6vf7IeOrJc4gXvND5eCcPubJgGpYBpisYoB5oUcEjQza-H_e8tj36zLa2bQ9ZnsVorU9MUiv-v558k-Pzr_zZVYZvYSpm3_8_oLjFQszdos9uMofoziDRAOM7SWyH2TYwd0aIIctE-7T5gymnHANXeagvEcfqzdiJjH4K6xz3Gh9UaLeQdwk56nEfaTEKQRYAWzSZX15oI243nWw1MpofMESNJp8eUCOoo7Xpg7RgE1MFx3zOe7As8OpDM87wKM4EiKo4MSS34Ek7e5H6SmK0BY1vxBAr5cF82nxc6LSM4kFCvO8D36g0uaMEsTiz57msOFh-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها و حماسهٔ ۱۷۰ شب حضور در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456651" target="_blank">📅 23:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456650">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aad7677a8.mp4?token=AZYMqNC091DXIX9_qjQUIanB-dJB0A8IH2gxvobxHXzWRFA3c-dwDy1gcOgvYYoWzgCDKN6vfQS-erwgRoH-i-vXGsfEJWyXp8aIoD4_-CmMXTyjgI9SYVZctmcAmgtgjy_Bs1lgruPpOOQ6JLqithnNwm93M9itsuUS6oD07JfiwWGmyX-lw8AUKrW9UaP_vx0mBTL0Z2Pn3D9PMfaFaod2T_IydinyW2gpYQYRLXUqwD3l0PiX-1FDPng9gEP8fwo9bIVkPuUF8MJm0DljoNwYcquxltqk6AAAoiz-2xEFoDMsHENH5GzkeRsa8UKzv-C-ZeXbmboPvKF7X6ZLQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aad7677a8.mp4?token=AZYMqNC091DXIX9_qjQUIanB-dJB0A8IH2gxvobxHXzWRFA3c-dwDy1gcOgvYYoWzgCDKN6vfQS-erwgRoH-i-vXGsfEJWyXp8aIoD4_-CmMXTyjgI9SYVZctmcAmgtgjy_Bs1lgruPpOOQ6JLqithnNwm93M9itsuUS6oD07JfiwWGmyX-lw8AUKrW9UaP_vx0mBTL0Z2Pn3D9PMfaFaod2T_IydinyW2gpYQYRLXUqwD3l0PiX-1FDPng9gEP8fwo9bIVkPuUF8MJm0DljoNwYcquxltqk6AAAoiz-2xEFoDMsHENH5GzkeRsa8UKzv-C-ZeXbmboPvKF7X6ZLQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: کره‌جنوبی گفت که برای مقابله با ایران به آمریکا کمک نمی‌کند
🔹
وقتی با رئیس‌جمهور کره‌جنوبی تماس گرفتم به او گفتم: «آیا تمایل دارید در رابطه با ایران کمکی به ما بکنید؟» او گفت: «نه، متشکرم.»
🔹
من گفتم: «یک لحظه صبر کن. ما ۳۹ هزار سرباز در آنجا داریم…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456650" target="_blank">📅 23:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456649">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f49232e6.mp4?token=dV8Au2DcWQ34CgcUwkxK9XpuCB6ZF8dvC6evj6INDNQALiRahAMeSEjusFyjI5DQiopkpKPNOw8enkcK73lco3k1LwNUcWGIjSEHufnUvzCnphPXm8lO0Ha1FY8JbqfuI0jdpn-i_87KUEgZ8_Y5H0Egbz0XyS5zgDC_1R7VDza4DYCI-WG6o7pC4QVTM7Y_DPMr1KqajKDpES63IzF_EM34GQLVleJZy4TdZXXu7k05JauhGJKB3k4dQAX4ULd5PSYvFSw3v-0FT_b6idqoGh0JRmVC6-Z1rsfu-0V2ZlTb2yQkQsAhB0V_F9JonfFxNZ37wW4afKjmoUvXYyh3Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f49232e6.mp4?token=dV8Au2DcWQ34CgcUwkxK9XpuCB6ZF8dvC6evj6INDNQALiRahAMeSEjusFyjI5DQiopkpKPNOw8enkcK73lco3k1LwNUcWGIjSEHufnUvzCnphPXm8lO0Ha1FY8JbqfuI0jdpn-i_87KUEgZ8_Y5H0Egbz0XyS5zgDC_1R7VDza4DYCI-WG6o7pC4QVTM7Y_DPMr1KqajKDpES63IzF_EM34GQLVleJZy4TdZXXu7k05JauhGJKB3k4dQAX4ULd5PSYvFSw3v-0FT_b6idqoGh0JRmVC6-Z1rsfu-0V2ZlTb2yQkQsAhB0V_F9JonfFxNZ37wW4afKjmoUvXYyh3Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم چهارمحال‌و‌بختیاری: به کوری چشم ترامپ؛ در خیابان می‌مانیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456649" target="_blank">📅 22:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456648">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89ac0b8d5f.mp4?token=g4BgSvTFNGw-ZGx9_h7oOWF8Xw8tMQukx_t45_n_TNTBvGL1vcfI_68K_AMb8-Zt-8fpAArTvnNJFKJDpMoM0IkyTKrcUGkO600qaaFtYPeeUt1P6f6QpytXi1E4j8mt6Rr7qQkZiEd3BhouuJFC3vzcB6hcCZ_AhuGCk3HL3C5EAviFFezTv71aK0x2QTCEi99F9-vn8QEV8YZdvWkLzPgYjOMxtOdGhvPWYmha_HRnu1EYExNf6O06Y9wRJ9vJuQWEENp5kllQKDqt9pGaHBfwP7ft3lmWvUYoMemNm-PtTyBLUcXSazJZBemLBb0Y8rMIyKagQDWYUpZDgsstq09RQzOTYdRqbTfupphjW1nk_aloFYyfq8rteiZeXaWS-VhAzKxXcAgTwNlVW7t50rklv0jcSQ2ZMZGiRQfm4CGmDeHNcCZ7HwgeudmMzG5bfesZ_11FGnf_iA5x2niJpx2Ny4gNP90EuoWrngfvSbhHU9-nZy43M5sdDTnNyMyfeoTY8anC5PiSGouX4WiYKJcOOfWMnxxN6_7lNMsRIO4CKgCczSmLefdI22U34fh41E8uRD1oS4cw7ECHzgsoXF_NkWkESWM1qPYfrV6qqcYOH7aOds08ngx70BIl7WZ-fF0dFxc3dKZNtzR-oitMw13I5ZLoQPNrkIsGHNwRJqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89ac0b8d5f.mp4?token=g4BgSvTFNGw-ZGx9_h7oOWF8Xw8tMQukx_t45_n_TNTBvGL1vcfI_68K_AMb8-Zt-8fpAArTvnNJFKJDpMoM0IkyTKrcUGkO600qaaFtYPeeUt1P6f6QpytXi1E4j8mt6Rr7qQkZiEd3BhouuJFC3vzcB6hcCZ_AhuGCk3HL3C5EAviFFezTv71aK0x2QTCEi99F9-vn8QEV8YZdvWkLzPgYjOMxtOdGhvPWYmha_HRnu1EYExNf6O06Y9wRJ9vJuQWEENp5kllQKDqt9pGaHBfwP7ft3lmWvUYoMemNm-PtTyBLUcXSazJZBemLBb0Y8rMIyKagQDWYUpZDgsstq09RQzOTYdRqbTfupphjW1nk_aloFYyfq8rteiZeXaWS-VhAzKxXcAgTwNlVW7t50rklv0jcSQ2ZMZGiRQfm4CGmDeHNcCZ7HwgeudmMzG5bfesZ_11FGnf_iA5x2niJpx2Ny4gNP90EuoWrngfvSbhHU9-nZy43M5sdDTnNyMyfeoTY8anC5PiSGouX4WiYKJcOOfWMnxxN6_7lNMsRIO4CKgCczSmLefdI22U34fh41E8uRD1oS4cw7ECHzgsoXF_NkWkESWM1qPYfrV6qqcYOH7aOds08ngx70BIl7WZ-fF0dFxc3dKZNtzR-oitMw13I5ZLoQPNrkIsGHNwRJqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهپیمایی مردم شاهرود در شب ۱۷۰ بعثت مردم ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456648" target="_blank">📅 22:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456647">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ntfu_7ID0WNfUybLYG3eq_bZaR4fuT8QeCyHeOvKMa_n0jhV4RfPmhJ7JzJBA8wyH_XE1V7fp7mJh0KZ5SJngkfrf4jhRaCYTTlRp7FsDZuyappGLMId9Z1iCeP9RLslce5HWltdz7t7OW0oIQveH4zgZ7YL8nnfpqg6z4Eg-3lzSs5q2A1MYWE_aifu27SWWbgF_248wAAP7zYHy4t8m6s6lSwutOFmmpvZHg71gyFYNKLktxQOvyseFOLNe8YAWJ79EhH0_dQwFRIxjDXRZ4ZbY8aYU7ONUXw0X4uS0QQUh34TwjG7WPFH6Lj7k10eSJwfJV4-s8nDPdyOOVvzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: صبر و همبستگی کلید ایستادگی در مقابل فشارهای خارجی است
🔹
آن‎چه بر آزادگان ما در سال‌های اسارت گذشت، فقط بخشی از تاریخ جنگ نیست؛ روایت ایستادگی مردانی است که رنج را تحمل کردند اما عزت ایران را وانگذاشتند.
🔹
صبر، همبستگی و امید کلید ایستادگی ایران در مقابل فشار و تهدید‌های روز افزون خارجی است.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456647" target="_blank">📅 22:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456646">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f019a57166.mp4?token=nvYtxw3euM_3uziT1RfZyPqGHp8YarD1iGq_I0vuUeGxRKXWLyESGNCzbzCAYuoIdZJF6a6bb92412wFp0St4D6hYuZAs7t_Y_28T1wcnpyyAuSYPFW3OjvOriyxqUOTzS-MSujgchzNcuMKNOgY1baz62HRrUatKyua66zZgFKSKM49mSk4SwzOgVYVbL11QUU4rpcvnWcNcMKkPA9_3gvmMjI_w0M4An5vnC9S_cjxDYZL9a_daaO0TF5JjSy5sSsSi518f_Bkdl0LE2dpMS80qE_naXruofOHyFGV4X9mDbl3aH0_Sujg19yCC4rYmhJBTh2mx1jvw4y3K7XtpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f019a57166.mp4?token=nvYtxw3euM_3uziT1RfZyPqGHp8YarD1iGq_I0vuUeGxRKXWLyESGNCzbzCAYuoIdZJF6a6bb92412wFp0St4D6hYuZAs7t_Y_28T1wcnpyyAuSYPFW3OjvOriyxqUOTzS-MSujgchzNcuMKNOgY1baz62HRrUatKyua66zZgFKSKM49mSk4SwzOgVYVbL11QUU4rpcvnWcNcMKkPA9_3gvmMjI_w0M4An5vnC9S_cjxDYZL9a_daaO0TF5JjSy5sSsSi518f_Bkdl0LE2dpMS80qE_naXruofOHyFGV4X9mDbl3aH0_Sujg19yCC4rYmhJBTh2mx1jvw4y3K7XtpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم چهلمین روزِ تدفین رهبر شهید در حرم مطهر رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/456646" target="_blank">📅 22:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456645">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e8a8752e.mp4?token=jWb_N-WRXqXHmvShcKT1tlgQY5hzgtC1PJkHto_faQpbLoVlcRa2hxCPmzh8QOzNofC9BS_jlnFiAxukn9ThZTIHcQhewv_OIUtg4Houc8QyTZQtYz0q6OxKIUu0VJpEXkwBPmRiiTuHy18KaQEdH4RD_RALo6gkCoGpAY2XOIIKhC851StwzgHlfvMg5FzMkIgFGM9CaA0iCHEndV44p7R9wwHMyPIft-gioKIe5-mOor8Xy_7ZxsRzT5aI2mWHjA0uGueLL-gvTgiKiajlt5HgI-nQK0JG9qhsP9pF1OLKCd_eciNwLe9mq8qd8l3kyHpjMO2LTLa9UOF4op2H5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e8a8752e.mp4?token=jWb_N-WRXqXHmvShcKT1tlgQY5hzgtC1PJkHto_faQpbLoVlcRa2hxCPmzh8QOzNofC9BS_jlnFiAxukn9ThZTIHcQhewv_OIUtg4Houc8QyTZQtYz0q6OxKIUu0VJpEXkwBPmRiiTuHy18KaQEdH4RD_RALo6gkCoGpAY2XOIIKhC851StwzgHlfvMg5FzMkIgFGM9CaA0iCHEndV44p7R9wwHMyPIft-gioKIe5-mOor8Xy_7ZxsRzT5aI2mWHjA0uGueLL-gvTgiKiajlt5HgI-nQK0JG9qhsP9pF1OLKCd_eciNwLe9mq8qd8l3kyHpjMO2LTLa9UOF4op2H5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحنه‌های ماندگار از میدان‌داری مردم لارستان فارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/456645" target="_blank">📅 22:32 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
