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
<img src="https://cdn4.telesco.pe/file/t-ntRuMLm1TDik2h166rImzeEhnqVseHb8kNpeQG2Tqsf22YWyOZhmSBGMzBoTRtTDMAE3nJY0uxRP2XctEDIO5MCrCiZEwK5vFLh4isulif_Hh_bh-tynZirV-RFhe8rKljUNi7yJgmTyrsCG0ruO4ImiSgB-zVUWrfCYu_5jmcdfHrZqPwKeU2OSVJ1_DVHR-ICDt9ROO56XVQr27h9haOAIhlt_5rU3v44OEXtSn7r5iLqgwfo58uJQiB9ywpEWFyjQQc_VFVRGqg472E6qnWMwVurAXsv_SeQiCK4g1nF_TOXs32gDpKS7eod2vsIj03qKJ1aiXs9JMTBAjcjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 924K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 06:50:05</div>
<hr>

<div class="tg-post" id="msg-132959">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
یک مقام امریکایی در گفتگو با آکسیوس:
حملات اخیر ایران به کشتی‌های تجاری در تنگه هرمز، توسط گروه‌هایی در داخل ایران صورت گرفته است که با تفاهم نامه شدیدا مخالفت دارند و قصد دارند آن را تضعیف کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/alonews/132959" target="_blank">📅 03:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132958">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de4e6346b4.mp4?token=CiSuMFop-rs6yISSxM2QP6Ow7x0V36qrTNpUhMT35c_G1rlUkNd5Ycw1DKr4Q9Cmn9Khj8oCq2abvcxWqB321olG5UmumvhSaXSkPABi49Ikc_i63SswXUMEEns3CoJWLbZjS-gJKqHV2IUeRE7pTNt4ma1FiCBHYhAGYBRWcvwN2B4tpZA9GYXIZ_KGqMpVW2vC3q8re5P8utBxK7YuhGx15HCwg0ZxAKuWpWTdSsidPTD9S9dgrEwL8lQtvIh9lftGuRsmYoUUN5YEIKPGBPhr16XTAwglkaaXS3HhEFKbTI4XF314LGTDZTqm0U65uVyRXCwvU8XFsg4e4nCADw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de4e6346b4.mp4?token=CiSuMFop-rs6yISSxM2QP6Ow7x0V36qrTNpUhMT35c_G1rlUkNd5Ycw1DKr4Q9Cmn9Khj8oCq2abvcxWqB321olG5UmumvhSaXSkPABi49Ikc_i63SswXUMEEns3CoJWLbZjS-gJKqHV2IUeRE7pTNt4ma1FiCBHYhAGYBRWcvwN2B4tpZA9GYXIZ_KGqMpVW2vC3q8re5P8utBxK7YuhGx15HCwg0ZxAKuWpWTdSsidPTD9S9dgrEwL8lQtvIh9lftGuRsmYoUUN5YEIKPGBPhr16XTAwglkaaXS3HhEFKbTI4XF314LGTDZTqm0U65uVyRXCwvU8XFsg4e4nCADw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور مجتبی خامنه‌ای در مراسم
‼️
🔴
امشب، موقع برگزاری نماز میت برای علی خامنه‌ای تو مشهد، یه فرد با صورت پوشیده و ماسک، سمت راست تصویر و بین جمعیت دیده شد
🔴
اطراف این شخص هم چندین محافظ ایستاده بودن و همین موضوع باعث شد توجه خیلی از کاربران فضای مجازی بهش جلب بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132958" target="_blank">📅 03:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132957">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
قبلیه بنی اسد یمن علیه آمریکا اعلان جنگ کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/132957" target="_blank">📅 02:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132956">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmRq0kHgsfFuGS_b-wDLixui7MsPSCkYGJEcOy0Nf9YM0_Pt7-Tmwtm_SsKFYQIl-CXGktdMc5wSbIRiD3G80qo171zzU9ECh0EFn2OqXsAwgH3VDvaQLm-FybRxK_ZlCS6VaHO6-rVZ5H7XqgduOfpxYuj5-0_gTKCYMGuPvQMX0q0XXjWx2OlCzW0oE455w0lIyZ9IPrVblzJEFvgOm6MxOdJJebsLixawdcMOHjQzZpSmAfPLQwjIX7DXoSc0LUpUq9wpixnHgkX_SjF-EgSX9atWLydygZiaUDGyOVl-Ffv3EyNnzNVNoMEycmxGJNjdyhbnWs9A7tIVwIcPMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام:
🔴
ادعا: رسانه‌های دولتی ایران مدعی هستند که عبور از تنگه هرمز فقط از مسیرهایی که ایران تعیین کرده، مجاز است.
🔴
واقعیت: ایران کنترل تنگه هرمز رو در اختیار نداره. از اوایل ماه مه تاکنون، نیروهای آمریکا به عبور موفق بیش از 800 کشتی تجاری و انتقال 380 میلیون بشکه نفت خام از این گذرگاه حیاتی تجارت بین‌المللی کمک کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/132956" target="_blank">📅 02:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132955">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام آمریکایی در امور ایران: واشنگتن همچنان به یافتن راه حل متعهد است و مذاکرات فنی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/132955" target="_blank">📅 02:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132954">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c3af8da2d.mp4?token=n8gK0TaZTaA1bZzcqG1JnHcR0B1fbFgnqBxNHZvgfTypaDjD4pMOhlBsyQ5K6VRA5dTp3KaHH6TUwB_8HmsZlYaYZQ8KQ7vn78_hqI2RvH6dDtNgPeubtLxrhNxT00R60LCfHT9Ot_OkYV_u2AiqAuKmQsahseHH3lNyVCPi2tvFvkLqsl3ndIMqvKAxWvP1Cy4KoOmaeT3sHFrDoD5WoWMv8QDqyEDro4HlDGN571_i3ZNWigi7yjco9X_mvYVXxd25EZx4XGG8Ohp_t4kkHSHOk3zKiNMdyS8WO93URPfR9mBnKHWN9p37FpX9q7BCT-6L1UDlxc4XlSOE2vnTeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c3af8da2d.mp4?token=n8gK0TaZTaA1bZzcqG1JnHcR0B1fbFgnqBxNHZvgfTypaDjD4pMOhlBsyQ5K6VRA5dTp3KaHH6TUwB_8HmsZlYaYZQ8KQ7vn78_hqI2RvH6dDtNgPeubtLxrhNxT00R60LCfHT9Ot_OkYV_u2AiqAuKmQsahseHH3lNyVCPi2tvFvkLqsl3ndIMqvKAxWvP1Cy4KoOmaeT3sHFrDoD5WoWMv8QDqyEDro4HlDGN571_i3ZNWigi7yjco9X_mvYVXxd25EZx4XGG8Ohp_t4kkHSHOk3zKiNMdyS8WO93URPfR9mBnKHWN9p37FpX9q7BCT-6L1UDlxc4XlSOE2vnTeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردم غزه گوشت‌های ارسالی سازمان ملل رو به دلیل ذبح غیراسلامی ریختن‌کف خیابون
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/132954" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132953">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MXwIdhSsFFprI_Dmsmap8bbIn_HKRsyvjCnkoE1E9RYyBnAfsm5mgsGid5zCLKCYEyEyyBjiGEhX6SsqcKp7mSP0JOzInL8SrfnpQzjcqh-4T3g45KH8n_fWGjy94jgliwZLOaj-nOyQLw5KP9zn7jb-2YFM2_4WL9IX8Jpz7_j_-rfGdUlhsSGaMoi4Ts3500kRgKL-V9GzP7qp8qKcJRdzmYdr8db7sm27Pge-qo-USss3G88ur8nJ869b8dW56E_zRPRXnR-BoUie3Nt1JpGfQCaGQzp8jz2dD6HMnYE3fhFVopmr6KqJM9Vjmum-_PBBT4RsoFzVcrRcXBYztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون سید علی خامنه‌ای پس از ۱۳۱ روز، در مشهد، به خاک سپرده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/alonews/132953" target="_blank">📅 01:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132952">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9ef6e045.mp4?token=SrAC89yOUNZh5zdbL0jsLFr7fddM7eeP9DvSRWa26zanW66mtVAga6XbQlt9-ji5Yqdp8QxKZneao2L5OkZvYe94jdIskGngguZjMtOTXBIeozgegVq5WKFl_u40lm06oyhweCl4N1J7XYYjf-iahCBNi8DTYqclDJglyAHiylBSq2AtQj6kOGB8cTUl0-VhrbF2B2uABvWqCL7uNylaRPvVfOvqzWtyIHM8_sVu-dUZ6T_u_Sjx1UVKg8E_VYVOKbhtvkFi32cao7FyGvjWHqiSh3sLLJ446qQpdoxzm7XOUZh8bgHaDSvdZxyDhqiGasMvekQAN-ZUZdIqbS0pNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9ef6e045.mp4?token=SrAC89yOUNZh5zdbL0jsLFr7fddM7eeP9DvSRWa26zanW66mtVAga6XbQlt9-ji5Yqdp8QxKZneao2L5OkZvYe94jdIskGngguZjMtOTXBIeozgegVq5WKFl_u40lm06oyhweCl4N1J7XYYjf-iahCBNi8DTYqclDJglyAHiylBSq2AtQj6kOGB8cTUl0-VhrbF2B2uABvWqCL7uNylaRPvVfOvqzWtyIHM8_sVu-dUZ6T_u_Sjx1UVKg8E_VYVOKbhtvkFi32cao7FyGvjWHqiSh3sLLJ446qQpdoxzm7XOUZh8bgHaDSvdZxyDhqiGasMvekQAN-ZUZdIqbS0pNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مشهد به دار کشیده و سوزانده شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/132952" target="_blank">📅 01:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132950">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فووووری/نخستین تصویر از فرد تیرانداز
◀️
مشاهده عکس بدون سانسور</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/132950" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132949">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtV1PVl5rxL7iP17XVaoiduh3EuQUlMt0_YvytcX9OCEJEnL57g8aTtydr-NGF9QZvSC0XNXyk33D5Kj30CPMC9Kv8v-2cHbQj2OKAHC8rr-XbJ-TT5pJTlaN79mVbNO4T0w8NbUWXMd5roT6ihyVSTl_d4GYsfa4VksttIkCM1aHkZUus6crr0nOnnTwUtva1B4eMWFfeQUG5G9lqqOfOWxb56wNCC1YTwtrwZnTa8Wsu7G0j0TfNYkNUg2S60O_bgwMnOhV2p4FlDS8gXJ0XBxPwQsi6xe2bSMAaijUwK8MBf37cbeOUwjbyJSfEk-Gt2e8e6QjMhlHRFom0DFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/اولین تصاویر از پاسداران کشته شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/132949" target="_blank">📅 00:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132948">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
هم اکنون تماس تلفنی میان نتانیاهو و ترامپ.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/alonews/132948" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132946">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1a1QRi0Azl0RZqkYu0Z__fFW9zlsQT-QzU6rjHSm5PoFS5LIhWccLaKYpcGOfa8IdYCQdTFSv39-lJ4MJyG8g5p0VLhDFUN9X7uzzkzkBBnJv3pTioSCPIg91ShBVfnHmtutbzxGr1b5PXulRNqSvubx2OSVT5GLSdWh4oy0XHO0jGlKFqjxmsf7P7H3mBsA1K4A4XyxPIUhmRZ0_duxN5_NPhy6WA1jbbhZf_qip-fQuv8TwqHIpbpiNewn6VR1SLnnkCEPvsNoK4kvcv7VmKMtf4NuCo8IqOodYp3GaMAj_BOWM4SDD2UCPQW7Fl-fcj7OKv7vRS43w4WRYcMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ul-BweJvTceMtV_U6RPC2EQ1oKvFj5Tnp4YNdoK8DyIctIxs-gsO0sGPXmTC9QtbQD4DWhGN35JVA4HLPldr4-kISKeS_GrSDWDslOUdtLPj7dpFeHcduOowhJhzsLAMtNsaBJFvWQ3ODr9BUADQMRt82Kxl5sxNZCESZ695CxZdPrkxeGoYdKG-H24TyMZG8dzEftpdaiyWenSnvMvxzn8VFbOrtnfFSGIR_MJ2WQjFOpsaMObG4c2LvGZhD9lLtFj1KiXpFxH__WeSENwot_3miZ2KgNB6KlI2GkRfRoEKZWeAtXMBKSdNzhAIDMvSWj64XKRlntp5kRKwyG1PxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
فوری/اولین تصاویر از پاسداران کشته شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/alonews/132946" target="_blank">📅 00:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132945">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHzELXH6yWcyYDAz6K6LoqvhjMQAp4o5GBzA2CNFNQ5I1mDSe_Tnn17SUR4V07PPEAH2r1K-oR2OyqZZJJCtQSy7O7dsWvUlnmM3aGj5uREkuoW9RIHbk6XwjB0AeGZqyQ7_cfwrANaofmj1eEo3P1xJXhJSym3Q9_ZAz6GaXQhOHSBZ6yCxepGm0q_Og5woN9VfNCuWSFewspaizIVPN5gugkQNBhLyiunj_PXLY40-0FTDh7ooUFValB76mtaMoVBhrOo8rUdcmkZn1OUQqZhNyHu9Z7KV5qh4pOzK9NyOGN9TkMaDQ6Whx3MXrK1joKIlcIaHXbNYzXf5EO9vMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امجد طاها؛ روزنامه‌نگار معروف عرب ۳ساعت قبل توئیت زد که۳ ساعت دیگه اتفاقات جالبی میفته و واقعا هم افتاد
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/132945" target="_blank">📅 00:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132944">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
افرادی که امشب به ایست بازرسی مشهد حمله کردن لباس نظامی به تن داشتند و بعد از زدن نیروهای امنیتی فرار کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/132944" target="_blank">📅 00:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132943">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری/گزارش تایید نشده از کشته شدن حداقل 3 نیروی سپاه در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/132943" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132942">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری/تلفات بالا گزارش شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/132942" target="_blank">📅 00:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132941">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/یک فرد مسلح به کلاشینکف اعضای سپاه در یک ایست بازرسی در مشهد را به رگبار بست
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/132941" target="_blank">📅 00:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132940">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری/گزارشات تایید نشده از حمله به یک ایست بازرسی در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/132940" target="_blank">📅 00:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132939">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ادعای فارس: 45میلیون نفر به تشییع اومدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/132939" target="_blank">📅 00:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132938">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری/گزارشات تایید نشده از حمله به یک ایست بازرسی در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/132938" target="_blank">📅 00:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132937">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
آی۲۴ عبری:  عربستان سعودی در تلاش است تا اسرائیل را از پروژه کریدور اقتصادی هند -خاورمیانه-اروپا (IMEC) کنار گذاشته و مسیر آن را به سمت سوریه و ترکیه تغییر دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/132937" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132936">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
دفتر نتانیاهو: امروز یک تماس تلفنی بین نخست‌وزیر و رئیس‌جمهور ترامپ برقرار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/132936" target="_blank">📅 23:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132935">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پاسخ ایران به بیانیه ناتو: اتهامات مطرح‌شده درباره برنامه هسته‌ای صلح‌آمیز ایران و وضعیت کشتیرانی در تنگه هرمز را بی‌اساس، سیاسی و مردود دانست.
🔴
برنامه هسته‌ای ایران کاملاً صلح‌آمیز بوده و ایران به‌عنوان عضو معاهده منع گسترش سلاح‌های هسته‌ای (NPT)، بارها اعلام کرده سلاح هسته‌ای هیچ جایگاهی در دکترین دفاعی کشور ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/132935" target="_blank">📅 23:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132934">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsAxjhmHrL9apngOHUvzEwZuHXdljb8hFVYL8oCF05WhncLgWDFOj_dNoz75YjmCk5vplgxkDkf5fNUr-gSgQizGSFits2IvkOt9fHzcSqk1vGh2XHrPC1Y_kADX84y7Qa4ZAwH5FS2aAu5UvAlF9C2IsLjMBuI__HpAfapi6wPXhDM9d3P89ixPVGJGEMKZVj-p464D68oXtvCv7NXq1elWHgEmb7JA1-W3Lr1sp-6B9_hg0I6CvEqUxvunRhONWnyB8yECFxutr5gwH1pOvn0y-cN2VUi8juf1SSOqw8zealUoDnXLkkfOuVYsUenZlOzsYh9QzqW0T0hLH0QRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حجت الاسلام میرباقری: مشکلی نداره امام مجتبی(خامنه‌ای۲) هم مثل امام زمان به غیبت بره
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/alonews/132934" target="_blank">📅 23:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132933">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فرماندار کنارک: منطقه نظامی نیروی دریایی در دو مرحله هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/132933" target="_blank">📅 23:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132932">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=nLfWUFaKkgO91rVbgTczEabAsRGzIPp8ZYg0Hkat_zCnKnJiJBA6K_CRKJUemTG3cQ-K8AhSHXz-ORJ7ndgKYLoiPAt8z9RKw2RxxnTvBZyeWJFl2cJQB5utP97XR99ajE60nCXDDVDp5fR96Pdar9w9Ur_iN50X2wJDXALgybI1J70lXOy4p-X2-cPWEszQ6mU1oFfrXgiBdPQrQqtXgvo11TBKP3pfkcMJlW192mYmw2aTx8_8abdI86wn1aUf93y-uMFEPKBwr2MK3iBz0Ew7Xg0WVRz-4xJk6eQxx1sFhRe-H_899ey3znn794poYRBRnVD_xRGyzaLBlOLfaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=nLfWUFaKkgO91rVbgTczEabAsRGzIPp8ZYg0Hkat_zCnKnJiJBA6K_CRKJUemTG3cQ-K8AhSHXz-ORJ7ndgKYLoiPAt8z9RKw2RxxnTvBZyeWJFl2cJQB5utP97XR99ajE60nCXDDVDp5fR96Pdar9w9Ur_iN50X2wJDXALgybI1J70lXOy4p-X2-cPWEszQ6mU1oFfrXgiBdPQrQqtXgvo11TBKP3pfkcMJlW192mYmw2aTx8_8abdI86wn1aUf93y-uMFEPKBwr2MK3iBz0Ew7Xg0WVRz-4xJk6eQxx1sFhRe-H_899ey3znn794poYRBRnVD_xRGyzaLBlOLfaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امشب تو مراسم تشییع تو مشهد یکی اومد علیه قالیباف و پزشکیان شعار بده که گونی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/alonews/132932" target="_blank">📅 23:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132931">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
دفتر نتانیاهو : ترامپ، نتانیاهو رو در جریان اقدام‌ها و تحرکات آمریکا علیه ایران قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/alonews/132931" target="_blank">📅 23:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132930">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrYqPhcSnkfZuPiwJj2UU81ipe0YaIP3w9rHSlwcu_vXpOjvDDRwK8xV0A6N47P2nPEpmfP1-JjLa0f-LQ19p-HaKfeiafmToYpEZsQC-HlzKxsNKE4F4desibtfk1BZgCGPh4rqCYCiirKBZadtv6swhsUteMBFEi2Y3oikkqD292_X1wdlQ2H3A7q-fKSDQxXhTFf1Zdc8WhAgbFvhAx8rFcWdl0FTqc9FR4Dh4KDoWx9yy9tURUOnFgWt9kDGRZ0Tfwir7p1n-_fdM11LoFzNL2EXhVlKe7RNOQ6YmAjA9JZ1RijgxtnZl8rSLR7Fi1Ftf4C4JzfjTts8QgRQoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اختلال شدید GPS در سواحل عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/132930" target="_blank">📅 23:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132929">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mqcP_6su8oUrTaGKk9-y5jhApCJfU4cr3S_AqvmhWWWCG5hdpSGJB6MiHBGnv5TaMrtxaPARoG7Nm8E-DjlNPuOup1Y3AqZrguvR-Th5NJBP8BGJbUWdd_p5uD3tmM5ImaF5UatYTel7FI0NN6lgMRrsJUkvrUopS2-9JwRCZkWgVXEcatS8K9P9OMtMR5SvLegbQM4eYk4VhyiL9iRfrDj5lE_Ri02356OfGdNswO6NHZvOD7NGaYD1qQtvAgbua6bR1GPoeItlMCeIw16P2cPGErLwYYDvRKKBYePsy60N5xPLlL--rpSc_K_f4fusvQq5IrjUlpAgGLfnH4sOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رصد اتش سوزی در بندر عسلویه توسط ماهواره جاسوسی اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/alonews/132929" target="_blank">📅 23:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132928">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
خبرگزاری ایرنا :  یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/alonews/132928" target="_blank">📅 23:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132927">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6LuDmRgMyvnC4SNJMeFE2ufqOlwnfMLLT4bAgPP_syVOVPr9Ze0-KasmHCS5-vJS4svHF05FfSOZRjG2s2PAfVfHcuMVb3F0U2v6sfReh7AxRMJgJG46kT66JdWZPaaRy8IsZhOrmEBn6slTdjtUDCpqnbSMTLChLjP-pOolz_GOoPf19fiQpy5CPXq0HJZpzENB-EdZJRdqgNeQhx8w8Xh5byh2E1hJggG2pLNxadSSEBKX3PnZwRx_oqNw0gtoNxZsd75Gc82jktfMRVN5_yn5hyADQ23lm5hXC5TX8HcWIgObNPOyWN01pfHOMlBQnNJym3fpv4OFQw1DhSwvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اردوغان: من معتقدم که گفتگوهای سازنده و مثبتی که با رئیس‌جمهور ایالات متحده، دونالد ترامپ، داشتیم، به نتایج ملموسی منجر خواهد شد که انتظارات کشور ما را در صنعت دفاعی، به ویژه در رابطه با هواپیمای جنگنده ملی ما، "کان"، و برنامه "اف-35" برآورده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/alonews/132927" target="_blank">📅 23:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132926">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ایرنا: صدای انفجار شنیده شده در بوشهر متاثر از واکنش پدافند هوایی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/132926" target="_blank">📅 22:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132925">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
فیدان: آتش‌بس میان ایران و آمریکا پایان نیافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/alonews/132925" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132924">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">از بندرعباس فقط عباس مونده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/132924" target="_blank">📅 22:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132923">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">💢
فوووووووووری/پرواز جنگنده‌های اسرائیلی به مقصد نامعلوم
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/alonews/132923" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132922">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWNHInSj0Gr5ogGweoZdnyfhmknfTFrarXsaI3i3u-9OZ8GKYBQqfE9EPlR9nUMAnWyykRS9wtTcL9SRTEV_0hYVVPhZThBH79oOPvNPKl0IVQ3tmFJvWsE3XL_qVP_35i8W3UBo0ygV236FslFH3SpKCmrGxr7M7VzvB33Kgk2o6YcyYQY6RSX2vabdlAE0fWmjdTVmoNlBatgXt406hGH10lSCHi9RV_xQOdk3o_W3Gc_Hm9A-wtrTY5Ss50sY7QcndKFkCAYV1AOXtMNIPfymtHUhii625ZMkEpJrcFp12qUtuPSO_gdkAHcSNBbpp6FuaHaIowCCfPbxPvq8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از اتاق عملیات کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/alonews/132922" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132921">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری/شبکه ۱۱ عبری: کشورهای خلیج فارس (احتمالاً کویت و بحرین) یک عملیات مشترک نظامی محدود علیه ایران انجام داده‌اند.
🔴
بر اساس گزارش‌های شاهدان عینی، پرتاب موشک از خاک کویت مشاهده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/alonews/132921" target="_blank">📅 22:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132920">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
صداوسیما: امشب به بندرعباس، قشم، سیریک و جاسک حمله نشده و ما تکذیب میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/alonews/132920" target="_blank">📅 22:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132919">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/royq4u7cjeT8CeSM59jYnR0zye5YcuxqUpr01_kQ4NOcNfe46s4Wdq21YJ6H8KUZdCTYehw165FY-BQwFO4AqmK0qooyMhiNZh6V9J586v4vHPU4RoLS7V2_dBcd99RyS4XrP6lLLkJWso9KfG2eJ4_BEd-Mcju4TtldAUThyRalZcX0MBQ72u7Izho1pe-BvRA9T0rN-Qs5GIVBQkMvcxI3Dm7p-NZTVjaLuubZ0A_-TyENWJwkBrsEpxvrJ-ZiWSdjeImpSKLThX-JyNI8GuNToVgmqBJI60FC5KgELDPvczDaNeAVT4T7d3jsTEtdbCP5SS4Ep0xaRS3hjWjvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای عراقچی هم از تهران به سمت مقصدی نامعلوم پرواز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/alonews/132919" target="_blank">📅 22:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132918">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری/رسانه عربی نایا: احتمالا حملات امشب کار کویت و بحرین بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/alonews/132918" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132917">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری / آکسیوس به نقل از یک مقام آمریکایی: ما در حال حاضر هیچ ارتباطی با هیچ حمله‌ای به ایران نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/alonews/132917" target="_blank">📅 22:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132916">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری / آکسیوس به نقل از یک مقام آمریکایی: ما در حال حاضر هیچ ارتباطی با هیچ حمله‌ای به ایران نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/alonews/132916" target="_blank">📅 22:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132915">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری/ العربیه: ایالات متحده در حملات امشب به ایران نقشی ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/132915" target="_blank">📅 22:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132914">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری/ العربیه: ایالات متحده در حملات امشب به ایران نقشی ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/alonews/132914" target="_blank">📅 22:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132913">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadbf3e793.mp4?token=hq-JFq1Z96aM-L_kA577PrinGqMDIjGdAOmLJ_G_vCevaizl2sVEsOmJyXw8vBzd9j70hkYKHHZZacslgJZ6kFWfgQ7EonT-rIsDlz6MUz3wxt69exbyil4jghhJ9MidVFuYOlVu4tRSeII0SiVgNl1rXvM4YF9nXezzxtef6kucLpzXUId1XkNkTuoTUTps1PYa9ATGubvdf0UPe3kML_3k4nOfmQXEbUBrH-DWo7mx2d2Ahz3S5KqvKwR1SqrMKLJ_YFWZ8poDoUdQcpXjA8slFVBTCYBuP83IxiTmMn5FZlJGvZdZZWq1r3xal7U5NfBDff7tWLETXtnd-h-diQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadbf3e793.mp4?token=hq-JFq1Z96aM-L_kA577PrinGqMDIjGdAOmLJ_G_vCevaizl2sVEsOmJyXw8vBzd9j70hkYKHHZZacslgJZ6kFWfgQ7EonT-rIsDlz6MUz3wxt69exbyil4jghhJ9MidVFuYOlVu4tRSeII0SiVgNl1rXvM4YF9nXezzxtef6kucLpzXUId1XkNkTuoTUTps1PYa9ATGubvdf0UPe3kML_3k4nOfmQXEbUBrH-DWo7mx2d2Ahz3S5KqvKwR1SqrMKLJ_YFWZ8poDoUdQcpXjA8slFVBTCYBuP83IxiTmMn5FZlJGvZdZZWq1r3xal7U5NfBDff7tWLETXtnd-h-diQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چغادک بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/132913" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132912">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
برخی منابع مدعی شدند حملات به ایران از خاک کویت انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/132912" target="_blank">📅 22:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132911">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb578e14f.mp4?token=nkKdrOklRon-zd-7B1N0KHioFPhM8CJkHMkJ5fPhSKtOrPKEaoXN09JRc9dm5w9W4KtC06QX6j2fzV2hN_XhHp7Jm0PPvwY_jba2wIXUnj7g-BRcloQrQY7GI6jMPFEVmNXdsyXvJQX4qbY4CooN1YYP1OcygDLXwSFd3_4BA7w5IyPRkSa2KDOMmE72gDNM5JirxZ4WrX5Q6crffpFDUvz3XxlhjILkcDSCf0Bi8V8P8FY8B4eDyfImora8qNwsDCDUQU7MBNlOJmT3q4wHiynuCRfURJmof4tyqtkOa5IDWgKOrn4_E1oKGthkQDS_hF5Qd246VAGbfxHd0RnO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb578e14f.mp4?token=nkKdrOklRon-zd-7B1N0KHioFPhM8CJkHMkJ5fPhSKtOrPKEaoXN09JRc9dm5w9W4KtC06QX6j2fzV2hN_XhHp7Jm0PPvwY_jba2wIXUnj7g-BRcloQrQY7GI6jMPFEVmNXdsyXvJQX4qbY4CooN1YYP1OcygDLXwSFd3_4BA7w5IyPRkSa2KDOMmE72gDNM5JirxZ4WrX5Q6crffpFDUvz3XxlhjILkcDSCf0Bi8V8P8FY8B4eDyfImora8qNwsDCDUQU7MBNlOJmT3q4wHiynuCRfURJmof4tyqtkOa5IDWgKOrn4_E1oKGthkQDS_hF5Qd246VAGbfxHd0RnO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی که گویا
منتسب
به چابهار هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/132911" target="_blank">📅 22:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132910">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
آتش‌نشانی اهواز : انفجار امشب، ناشی از نشت گاز شهری در یک ساختمان مسکونی دوطبقه در منطقه حصیرآباد اهواز هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/alonews/132910" target="_blank">📅 22:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132909">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
چند انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/132909" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132908">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
مهر: تاکنون انفجاری در خارگ رخ نداده است
🔴
خبرهای منتشر شده در مورد صدای انفجار در خارگ صحت ندارد.
🔴
خبرهای منتشر شده در مورد صدای انفجار در خارگ تاکنون فاقد صحت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/132908" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132907">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
چندین انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/132907" target="_blank">📅 21:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132906">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
گزارش ها انفجار در اسکله چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/132906" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132905">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
حزب‌الله لبنان اعلام کرد که ایران را در رویارویی با ایالات متحده تنها نخواهند گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/132905" target="_blank">📅 21:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132904">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
انفجار مجدد در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/132904" target="_blank">📅 21:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132903">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9D6YNlDJ_Tx0tqS3lcgVfKaqre1Vh62ZKQGaAA0GFwdE_NmeOzdbfzRJsZlAQ11JQCSApoYMXBr5vDYRF6T8uopisnLNbYpCWz0reZN9NDb9edTz87eK0SmPalLUdcXfWqxbbQthhB8yN2XqVeX0vxQYXL6iYK3EYZfm5yI_ZTvXbmmgsgPeEm6NFQM_XhJ9WXrxP2EnBa8geUqKw4pewIBPdrsVc3b5BrIWaF0EjST9CNfLwiR1P8ibr8qxYC5JW-sPtoElZaoV5ABi8xKF8pRzvqgfTEfI_-5QFY4shMyVHwgOIAKAWs8046_Q5xrBBIH_bNK3RhEjq73QcpupQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون فعالیت هواگرد های ارتش ایالات متحده در جنوب ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/132903" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132902">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
۴ بار صدای انفجار در اهواز شنیده شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/132902" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132901">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
گزارش مردمی : 21:23  سه انفجار در چابهار شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/132901" target="_blank">📅 21:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132900">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
گزارشات از انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/132900" target="_blank">📅 21:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132899">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
گزارش هایی از شنیده شدن صدای انفجار در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/132899" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132898">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نخست‌وزیر بلژیک: جنگ با ایران باید متوقف شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/132898" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132897">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام آمریکایی:
ما به مرحله اجرای چارچوب مذاکرات لبنان و اسرائیل رسیده‌ایم.
🔴
کار برای نقشه برداری و شناسایی سایر مناطق آزمایشی در لبنان در حال انجام است.
🔴
اولین منطقه آزمایشی ظرف چند روز مشخص خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/132897" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132896">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
هم اکنون فعالیت پدافند در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/132896" target="_blank">📅 21:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132895">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02a761f84.mp4?token=Dw4sQ_EnqEq96OWngaxt_K2CZyo_fFxMQoPCVSaI7HlSRxcsAcdmfZQ0aQctXBi21iCvM91VnunU2ovfMYvM9yt9B-isBcJ1z18tbHqTRgIm3nBgMSRJpelm-YWr2thVchVYJZlQgRviEZEuhi5O6ma5I8uay-zcrBVvJZixoqWwaiC3CyzlX1tMnRVmnvQd_lb6r2ACZUimou_t9KT7G3sHURxYodjjmGQ-c_9Eeq9PpGLhmb6JNLxPsISQOY6aYRrOqjdMWGP8kmJor8yXbFohzt03jh-L98jxxs3VL6I8JnG819frd9seSt5yDCtQoMqEhsJ_8tjKWAbvytCYEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02a761f84.mp4?token=Dw4sQ_EnqEq96OWngaxt_K2CZyo_fFxMQoPCVSaI7HlSRxcsAcdmfZQ0aQctXBi21iCvM91VnunU2ovfMYvM9yt9B-isBcJ1z18tbHqTRgIm3nBgMSRJpelm-YWr2thVchVYJZlQgRviEZEuhi5O6ma5I8uay-zcrBVvJZixoqWwaiC3CyzlX1tMnRVmnvQd_lb6r2ACZUimou_t9KT7G3sHURxYodjjmGQ-c_9Eeq9PpGLhmb6JNLxPsISQOY6aYRrOqjdMWGP8kmJor8yXbFohzt03jh-L98jxxs3VL6I8JnG819frd9seSt5yDCtQoMqEhsJ_8tjKWAbvytCYEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شریعتمداری: باید یکی از خواسته‌هامون توی تفاهم‌نامه تحویل ترامپ باشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/132895" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132894">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری / گزارش های اولیه از انفجار در چابهار!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/132894" target="_blank">📅 21:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132893">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt0VH0xgmLw4SVNZh9mYtBkuZPaZZSGS5doh5lOt1Hisdc7FHAtCUytjLYeHX8mnjQvPqVc3F9m1R2NZrY9y-VtlcNFy3fc0lHPkzVwVw4_bq4HTsGZRjMG0Xg_OJqkXK1PYnY9df7YwmmXzpE0ziKcuFaifgUIfRxgIcUHqZ94Yx_Y5Z5ejEN-9O0TOEFKEmnjAAX9OAWClhmHfod9rASzQ_v6jWe49ObAczO6J6v3TUqsn1myCDcL_h85xy43ikKyFqz4JkB6AdsiuH7A_uDHqD-P4xK_7a7iUiA53eQQoD1VidvXm3Tk4NugJBoGoKZH0CwUjwhdBFalBaZVy0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هدیه خاص اردوغان به سران کشورهای ناتو که در اجلاس آنکارا شرکت کرده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/132893" target="_blank">📅 21:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132892">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
اسکای نیوز عربی: اگر درگیری بین ترکیه و اسرائیل در سوریه، به عنوان مثال، رخ دهد، آیا این موضوع ماده ۵ [توافق‌نامه ناتو] را فعال می‌کند؟
🔴
مارک روته، نماینده ناتو: آقای اردوغان یک رئیس‌جمهور بسیار خردمند هستند. ایشان سال‌هاست که در این سمت حضور دارند و از قرار گرفتن در موقعیتی که از کنترل خارج شود، اجتناب خواهند کرد.
🔴
اسکای نیوز عربی: اگر آقای نتانیاهو شرایطی را ایجاد کنند که درگیری اجتناب‌ناپذیر شود، چه؟
🔴
مارک روته: بیایید در مورد آنچه ممکن است اتفاق بیفتد، حدس و گمان نزنیم، زیرا در نهایت نباید فراموش کنیم که در ۷ اکتبر ۲۰۲۳ چه اتفاقی افتاد. حمله وحشتناک حماس به اسرائیل. این حمله از طرف اسرائیل آغاز نشد...
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/132892" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132890">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558eba4f88.mp4?token=OfyOzCRdEFkBq3W-RfZREvMdt7Ce_2GK1eTdfxLY0bXFE3waBetlaZ1lb9wssRc4vHMztdF2zxseiRxdIb1EKqB12c436ysbXpyJgzfHxQcRjxPiXOAlMbYX-WdP7DtdTe8aaHxuqR1w-lTU7ZLmc3wJnBWI9-_egxcPsO-HVU-gqkgwHUBprfIo0RKEXbx8UKozPUfkmRhU1kqB5vuKPWq8RnYijNx3I2h1kz5Gk_58tp2t_g7m2l7DJS_b9e0osTuhMo9uEoS5AqWiva8qjZCwou4D7yrC_EsOARwC51_Pzi1DBtRSoAZ-gL2HyDY0s2xvbSTKynXD6AzYZPVLJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558eba4f88.mp4?token=OfyOzCRdEFkBq3W-RfZREvMdt7Ce_2GK1eTdfxLY0bXFE3waBetlaZ1lb9wssRc4vHMztdF2zxseiRxdIb1EKqB12c436ysbXpyJgzfHxQcRjxPiXOAlMbYX-WdP7DtdTe8aaHxuqR1w-lTU7ZLmc3wJnBWI9-_egxcPsO-HVU-gqkgwHUBprfIo0RKEXbx8UKozPUfkmRhU1kqB5vuKPWq8RnYijNx3I2h1kz5Gk_58tp2t_g7m2l7DJS_b9e0osTuhMo9uEoS5AqWiva8qjZCwou4D7yrC_EsOARwC51_Pzi1DBtRSoAZ-gL2HyDY0s2xvbSTKynXD6AzYZPVLJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آنیتا آناند، وزیر امور خارجه کانادا:
به نظر می‌رسید که آن حملات اولیه (توسط اسرائیل و ایالات متحده) به طور آشکار ناقض قوانین بین‌المللی بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/132890" target="_blank">📅 21:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132889">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای خارجه ایران و عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/132889" target="_blank">📅 21:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132888">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
زمین لرزه‌ای به بزرگی ۳.۱ ریشتر ساعت ۲۰:۲۰ پنجشنبه ۱۸ تیرماه حوالی شهر استهبان از توابع استان فارس را لرزاند.
🔴
این زلزله در عمق ۱۰ کیلومتری زمین رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/132888" target="_blank">📅 20:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
به گزارش کان مقامات ارشد اسرائیلی خواهان دریافت مجوز از دونالد ترامپ برای انجام حملات مستقل از سوی اسرائیل شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/132887" target="_blank">📅 20:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132886">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
خبرنگار جروزالم‌پست به نقل از منابع دولتی اسرائیلی درباره احتمال درگیر شدن ارتش اسرائیلی در حملات علیه ایران خبر داده است
🔴
وی گفته که اسرائیل تنها در صورت حمله ایران به مواضع اسرائیلی یا درخواست آمریکا خواهد بود که اسرائیلی‌ها وارد درگیری خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/132886" target="_blank">📅 20:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سی‌ان‌ان‌: میانگین قیمت بنزین پس از شروع دوباره حملات آمریکا علیه ایران، امروز ۵ سنت در هر گالن افزایش یافت و به حدود ۳ دلار و ۸۵ سنت‌ رسید
🔴
این افزایش، بزرگ‌ترین رشد یک روزه از ۱۶ اردیبهشت تاکنون بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/132885" target="_blank">📅 20:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/708c587fac.mp4?token=ScLMFsRm2YaR4F97yNrD5F9KZWkepcYlNRbxj9zlvGWsGpSrPDJ6Z0xJBRMvIdp32iMCJe3nLGnuLi8Awwpd-t5RVC2_TcX5geyJcM0_MvxUQa-WVvfod9wFUic9zBof9vsbC0O9qyZkonYBW6laCkSRfPdpcYBe588Yx0DCS6JmLLaIoisO4V_KAe2sd_3a9MIlayGnKVSiEecYuPI4TC_tW3vOuwzgV-26ebouTcZ-lr9mX2EhIbbv3tThdy5dHH92setHDP-wniuS6sob-DXRhyPFFX25tLmDNqTAHkbAtN_nEBvLHY7oX9EPl8X-gyQx9B3t5wMAhkXfUrt55A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/708c587fac.mp4?token=ScLMFsRm2YaR4F97yNrD5F9KZWkepcYlNRbxj9zlvGWsGpSrPDJ6Z0xJBRMvIdp32iMCJe3nLGnuLi8Awwpd-t5RVC2_TcX5geyJcM0_MvxUQa-WVvfod9wFUic9zBof9vsbC0O9qyZkonYBW6laCkSRfPdpcYBe588Yx0DCS6JmLLaIoisO4V_KAe2sd_3a9MIlayGnKVSiEecYuPI4TC_tW3vOuwzgV-26ebouTcZ-lr9mX2EhIbbv3tThdy5dHH92setHDP-wniuS6sob-DXRhyPFFX25tLmDNqTAHkbAtN_nEBvLHY7oX9EPl8X-gyQx9B3t5wMAhkXfUrt55A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات مرز، صدراعظم آلمان: در حاشیه نشست ناتو در آنکارا، ما با دولت آمریکا به توافق رسیدیم که موشک‌های تاماهاوک آمریکایی توسط ما خریداری شده و در آلمان مستقر خواهند شد.
🔴
ما در حال پر کردن یک شکاف مهم استراتژیک در حوزه دفاعی خود هستیم، در حالی که همزمان برای توسعه سامانه‌های دفاعی اروپایی خود تلاش می‌کنیم و قصد داریم آن‌ها را در اروپا مستقر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/132884" target="_blank">📅 20:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فارس: برخی منابع خبری  مدعی شدند سوخت‌رسان‌های اماراتی در حملات بامداد چهارشنبه آمریکا به بنادر ایرانی کمک کرده‌اند/این هواپیماها توسط امارات متحده عربی اداره می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/132883" target="_blank">📅 20:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
روسیه و چین در نشست شورای سازمان بین‌المللی دریانوردی، سند پیشنهادی امارات درباره تنگه هرمز را رد کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/132882" target="_blank">📅 20:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری / حازم قاسم سخنگوی حماس در غزه ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/132881" target="_blank">📅 20:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-huQzQKViNYlFQ2yyX_i4jI-_sa5znxdPyZEctSVfyBu9pKCLUYKPzhHOBm5-Nm18je6fcOq3dp3R6nEMUXRlIwfAHnO1FzbBl9lYR171Xjx3Qa0ugfCQ94KYRKobhWmNrUufvomEo_tql12HDNy7t2Hms0T5d-q5Hf133eqjIqeFz3pNcHJmVVBiqwYC959qS-pbONWDvLRnud4zG27zOwnoFfcY0ccaGH4IJWgWmsbEgGMtUcisctTEEh072jKPFIzhLNqamuBGJ0BHqI7_Tvud0ObpmHO--oM6KI90lAfLQ-txl3aaJoQFya7fqsOgJ1MZ7Bxjp58CiJSPb0Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون جنوب لبنان هدف حمله شدید قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/132880" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: ضمیمه محرمانه توافق اسرائیل و لبنان، به تل‌آویو اجازه آزادی عمل علیه تهدیدات در داخل «خط زرد» را می‌دهد
🔴
این ضمیمه بنا به درخواست دولت لبنان، محرمانه مانده
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/132879" target="_blank">📅 20:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری / حازم قاسم سخنگوی حماس در غزه ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/132878" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رویترز: گزینه‌های ترامپ در برابر ایران «محدود و بد» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/132877" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، از مقامات ارشد بیش از 60 کشور دعوت کرده است تا هفته آینده در جلسه‌ای شرکت کنند که موضوع آن، به گفته دولت ترامپ، احیای تروریسم افراطی فرا ملی است. این موضوع، به ویژه، به گروه «آنتيفا» مربوط می‌شود، طبق گزارش واشنگتن پست.
🔴
این طرح، نگرانی‌هایی را در میان مقامات آمریکایی، متحدان اروپایی و کارشناسان تروریسم برانگیخته است. بسیاری از آن‌ها معتقدند که «آنتيفا» یک جنبش غیرمتمرکز است و نه یک سازمان تروریستی خارجی، و بنابراین، تهدید جدی بین‌المللی محسوب نمی‌شود.
🔴
سباستین گورکا، مشاور ضدتروریسم کاخ سفید، در مورد این موضوع بحث کرده است که آیا می‌توان از برچسب "سازمان تروریستی خارجی" برای هدف قرار دادن افرادی که ارتباطی با «آنتيفا» دارند، استفاده کرد. این اقدام، به گفته مقامات، می‌تواند ابزارهای تحقیقاتی بیشتری مانند نظارت را فراهم کند. برخی از مقامات دولت هشدار داده‌اند که ایجاد چنین رویه‌ای ممکن است در آینده توسط دولت‌های بعدی علیه فعالان محافظه‌کار مورد استفاده قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/132876" target="_blank">📅 20:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
تکذیب انفجار در زنجان
🔴
منشأ دود آتش‌سوزی سوله بازیافت بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/132875" target="_blank">📅 20:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
مدیرعامل راه‌آهن: با تلاش مهندسان شرکت راه‌آهن در کمتر از ۱۳ ساعت پس از حمله دشمن آمریکایی به خط راه‌آهن مشهد؛ یکی از خطوط بازسازی شد و به چرخه خدمات‌دهی بازگشت.
🔴
خط دوم نیز تا ساعاتی دیگر بازسازی خواهد شد.
🔴
هم‌اکنون تردد قطارها در خط بازسازی شده از سر گرفته شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/132874" target="_blank">📅 20:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
روسیه: رقیق‌سازی اورانیوم در خاک ایران یک گزینه کاملا عملی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/132873" target="_blank">📅 19:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_TUyxE-oD6OxaJkGSh-O55hDLvb8IWiIicLuVrGUX3GX04X7HzA7WNnUe5FXw0kvgxLd5qXdyk9hDnzRZ5YFaS6QxrUk3YnxwsmwEUFnZMlujgdSX6nAfxXKfVciH79xE4T1v8Icpe2pqkHcMm39B3WwIlzuOPw5WCdg4uaGzvtbu77WdEHzQUmw5U59oygxN3OZakq7en-fFZHbOjxhrYvhR2u7_ykf9dKhT4FGn6DO7aEYom33LLzYWVMagy2ChHE9WQtFXqWBG7PiuPLQ-LzRfcRHW_Si3LytLr2sGbOrBx3IDkKQNVPRnt0O4OaA5_IjfaPQxd-SAG4HkqtRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: چگونه «سلاح طلایی» ایران در تنگه هرمز به اولویتی بزرگتر از برنامه هسته‌ای آن که مدت‌ها مورد مناقشه بوده تبدیل شد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/132872" target="_blank">📅 19:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132871">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از منابع: قطر و پاکستان در تلاش هستند تا آمریکا و ایران را مجدداً به میز مذاکرات بازگردانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/132871" target="_blank">📅 19:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132870">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نتانیاهو: جنگ هنوز به پایان نرسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/132870" target="_blank">📅 19:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132869">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ندف ایال: منابع ارشد اسرائیلی معتقد هستند که جنگ دوباره در مقیاس کامل آغاز نخواهد شد، اما تنش کنونی ادامه پیدا می‌کند
🔴
آن‌ها هشدار می‌دهند که رفتار تهران بسیار غیر قابل پیش‌بینی شده
🔴
اسرائیلی‌ها می‌گفتند تفاهم‌نامه، مزیتی به ایران می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/132869" target="_blank">📅 19:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132868">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568e3cc6bd.mp4?token=BHncEXq0Q9HWGTn3Rt7VhS6e8m-yJe4j9SIPQPCCeNeFpXDbWk64BDSQDtu4BZOvjO5I_PyhMb2eWrX-NTco0MyJxuvbqrcMd3w-3A4qgGxzO3kRU3un7nahcVKAtL0UW51pGrPRC-LHoS2wdVF2wWcwwoVRFtwcN2Vw5oDQLoBwJFTBlgSEBEXReXVa37W2KglJSy8Ng_825ddRp1Pg4HOe-7v4TItL6khKrxyx1mWZNqP7531kqfK1m1NnSxnRkI7k4QCkRG1KkAvOwpHagjv_uotDc4jj2g9n-ORXVuMZceadBqiQZfsTl7dhT_mwC_oTSz5Y7NlxMc-wI4OzNBP0Ke2NsL00lWK2djcfXszgm7vIlAMpQ0VQHrgC0MbhTaZqAbL_qegyPerC7q9sVZkqlrk-fzrRLqX0wKFi98G-r1cvIeOv2Q13Wg-_IZtra9jPhrHOccaoJJPm7lCSqNABm10rNk3fmlxnVOLh_QCcfCp86_MUk3iJVgiocqtFtUCtOVKgs6Mea0CVSgNtUXlsyrTwC5mXKS48hjLxnIokoieYeJZ79MnnksUeRqruRGYzkmSUiuic-sJgTTWkIO9iONyDFrjtgVmsl_r8hhtZPhwSMPEruSYGzxynrv4IAs5gL-K5eQBW1SGDEJy7oMlr864ZrVlknTvi7DNeS3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568e3cc6bd.mp4?token=BHncEXq0Q9HWGTn3Rt7VhS6e8m-yJe4j9SIPQPCCeNeFpXDbWk64BDSQDtu4BZOvjO5I_PyhMb2eWrX-NTco0MyJxuvbqrcMd3w-3A4qgGxzO3kRU3un7nahcVKAtL0UW51pGrPRC-LHoS2wdVF2wWcwwoVRFtwcN2Vw5oDQLoBwJFTBlgSEBEXReXVa37W2KglJSy8Ng_825ddRp1Pg4HOe-7v4TItL6khKrxyx1mWZNqP7531kqfK1m1NnSxnRkI7k4QCkRG1KkAvOwpHagjv_uotDc4jj2g9n-ORXVuMZceadBqiQZfsTl7dhT_mwC_oTSz5Y7NlxMc-wI4OzNBP0Ke2NsL00lWK2djcfXszgm7vIlAMpQ0VQHrgC0MbhTaZqAbL_qegyPerC7q9sVZkqlrk-fzrRLqX0wKFi98G-r1cvIeOv2Q13Wg-_IZtra9jPhrHOccaoJJPm7lCSqNABm10rNk3fmlxnVOLh_QCcfCp86_MUk3iJVgiocqtFtUCtOVKgs6Mea0CVSgNtUXlsyrTwC5mXKS48hjLxnIokoieYeJZ79MnnksUeRqruRGYzkmSUiuic-sJgTTWkIO9iONyDFrjtgVmsl_r8hhtZPhwSMPEruSYGzxynrv4IAs5gL-K5eQBW1SGDEJy7oMlr864ZrVlknTvi7DNeS3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: من تصمیم گرفته‌ام که در طول ده سال آینده، 350 میلیارد شکل به بودجه دفاعی اضافه کنم. بخش بزرگی از این مبلغ به نیروی هوایی اختصاص خواهد یافت.
🔴
در راستای این تلاش، ما همچنین یک صنعت گسترده تولید مهمات، با استفاده از فناوری‌های اسرائیلی، ایجاد خواهیم کرد. این سلاح‌ها متعلق به خود ما خواهند بود و وابستگی ما به خرید از خارج را کاهش خواهند داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/132868" target="_blank">📅 19:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132867">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نتانیاهو: جنگ هنوز به پایان نرسیده است. در کنار چالش‌های قدیمی، چالش‌های جدیدی نیز در حال ظهور هستند. محورهای قدیمی در حال فروپاشی هستند و محورهای جدیدی در حال شکل‌گیری‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/132867" target="_blank">📅 19:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132866">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نتانیاهو: «حفظ برتری هوایی ما، یکی از ارکان اصلی امنیت ملی ما و کلیدی برای حفظ ثبات در خاورمیانه است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/132866" target="_blank">📅 19:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132865">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
قیمت نفت و گاز در معاملات امروز کاهش یافت. نفت برنت با افت ۰.۹۴ درصدی به ۷۷.۲۹ دلار، نفت WTI با کاهش ۱.۱۳ درصدی به ۷۲.۶۹ دلار و گاز طبیعی نیز با افت ۳.۵۲ درصدی به ۳.۰۹۹ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/132865" target="_blank">📅 19:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132864">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
بلومبرگ با استناد به داده‌های کشتیرانی: ایران در ۲۴ ساعت گذشته برای تخلیه نفتکش‌های حامل ۱۱ میلیون بشکه نفت خام عجله داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/132864" target="_blank">📅 19:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132863">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
شورای همکاری خلیج فارس: حملات ایران به کشتیرانی در تنگه هرمز، امنیت انرژی و تجارت جهانی را تهدید می‌کند
🔴
ما از شورای امنیت می‌خواهیم که موضع قاطعی برای تضمین آزادی دریانوردی در تنگه هرمز اتخاذ کند.
🔴
ما ایران را مسئول این حملات می‌دانیم و از آن می‌خواهیم که فوراً و بدون قید و شرط تمام اقدامات خصمانه خود را متوقف کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/132863" target="_blank">📅 19:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132862">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نتانیاهو : برای هر سناریویی آماده‌ایم
🔴
یه چیز رو هم خوب می‌دونیم؛ اینکه باید همیشه آماده و قوی باشیم
🔴
قبل از هر چیز، خودمون رو تغییر دادیم  جسارت به خرج دادیم
🔴
پیش‌قدم شدیم و حمله کردیم، ثابت کردیم دست بلند نیروی هوایی اسرائیل به هر جایی می‌رسه
🔴
از یمن تا ایران، وقتی هم از دست بلند اسرائیل حرف می‌زنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/132862" target="_blank">📅 19:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132861">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
کاتز: آماده‌ دور سوم درگیری با ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/132861" target="_blank">📅 19:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132860">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خبرگزاری تسنیم: بیشتر از ۱۰ میلیون نفر در مراسم تشییع در عراق شرکت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/132860" target="_blank">📅 19:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132859">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
منابع دولتی پاکستان به خبرگزاری آناتولی گفتند که پاکستان و قطر تماس‌های جدیدی با آمریکا و ایران برقرار کرده‌اند تا دو طرف حملات نظامی بیشتر را متوقف کرده و «طبق توافق» به مذاکرات بازگردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/132859" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132858">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
نتانیاهو: اگر ما اقدام نمی‌کردیم، ایران به سلاح هسته‌ای دست پیدا می‌کرد و جنگ هنوز تمام نشده است؛ چالش‌های جدیدی پیش روی ما در حال ظهور است.
🔴
ایران ضربه سختی خورده است و سیاست ما روشن است: ایران چه با توافق و چه بدون آن، سلاح هسته‌ای نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/132858" target="_blank">📅 18:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132857">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
اولیانوف: هیچ عوارضی برای عبور کشتی‌های روسیه از تنگه هرمز پرداخت نمی‌شود
🔴
میخائیل اولیانوف، نماینده دائم روسیه در سازمان‌های بین‌المللی مستقر در وین، گمانه‌زنی‌ها پیرامون پرداخت عوارض عبور از تنگه هرمز توسط کشتی‌های روسی را رد کرد.
🔴
اولیانوف تأکید کرد که هیچ‌گونه هزینه‌ای از سوی کشتی‌های روسیه برای تردد از تنگه هرمز به ایران پرداخت نمی‌شود.
🔴
وی در پاسخ به سؤالی درباره وضعیت کشتی‌هایی که با پرچم کشورهای دیگر از این مسیر عبور می‌کنند، اظهار داشت که ارزیابی دقیق درباره اینکه آیا ایران از آن‌ها عوارض دریافت می‌کند یا خیر، دشوار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/132857" target="_blank">📅 18:48 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
