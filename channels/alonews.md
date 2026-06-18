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
<img src="https://cdn4.telesco.pe/file/ZtlW37VfZnXBGn-pDwlfbQ-QbkcxYOJrrZO8qIVSPbMekE_Mkmaz6TFb_Bk7NrtTmQBssp5kAoKY3iTAw1LvbMbtVv74rIk2GpZ7DFJmVKMZiI3hwsFiB5gVG-FThpN67aZZeqQs438s_qm-rtaQRaW9SRJ9Ukrj0VbKclcAzEbYfCJbNEomI-EuV7zduPiSOy1dTFm7_KCzL8kf8pK1Qa3VnMght3UQK58_PiVn63vdcRQ9lM-j_1A1X_BaSQtSQ-td8TUwwNwHfTlCPLQO6aSs42qk81A8vOQCWLWKZqTmB__Mvkd5UYvyn9mBbp48SW6ut3UkPCSKipNMHMd1Dw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 17:57:40</div>
<hr>

<div class="tg-post" id="msg-128929">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
الجزیره به نقل از یک منبع در دفتر نخست‌وزیری:
معاون وزارت امور خارجه نماینده پاکستان در نشست سوئیس خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/alonews/128929" target="_blank">📅 17:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128928">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ به کانال ۱۱ عبری: آماده دیدار با نتانیاهو هستم
🔴
او باید منطقی‌تر باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/alonews/128928" target="_blank">📅 17:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128927">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4IAAJXC_xVWhGkQdMHe6CeeiubMzgzKHjX4EIshFYyRsgVVXbR6zn5ZQFs9kqggH_qlyu5mcCE0fbkO8wIU2HgRotWxGzlkBG70Frz55cuU4qfmXenlN6zay28MiPpBXEcs8_lMkZHvIKLHTqss5yceFPnOEaGh8zU_QKLMvsdaP33tolBqWogpFXXSegdSak8A1FK63m5pkx737iM0jmJSzsbGo_lCfFhvosKX3TkYzKaPz8UC4XYX6gHb1y7vuBO3E36m8omemRl6oqk-Wx3gmFEu0hme2g4znrKwpSwcF7-fCo2J-Y6AHs9qU6KqxNxqf1OeRmvWUZaeWWBnDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ به کان نیوز:
من به احتمال زیاد در انتخابات پیش رو از نتانیاهو حمایت خواهم کرد، اما باید ببینم چه کسانی نامزد شده‌اند.
ما رابطه خوبی داریم، اما او باید منطقی‌تر باشد. من آماده‌ام با او دیدار کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/128927" target="_blank">📅 17:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128926">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ:
هیچ ملت و فرد عاقلی نمیگه بمبارون رو ادامه بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/128926" target="_blank">📅 17:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128925">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMtWc7bp1e938hL98mwXAtokT9V6sgFiFuLxNmCVVtsl503kFD9GLSG_PJKNDxVN2RudVlET2cnFyh3PxPKVHTMB-PUIevI_fQZIODDKzadbZEwtB2h1mksh2y2jga309CDYx0F9wfdHdQl2LFbcHt9uQrvRKl0Z2sfxqhGuWytuGtBDvXxZo4ZbTuY6YE-AE6XLP_puntKThivAPVQWjIbc53GEjw2d4j5U8gWf0m3FNPYnJwJFjBZbJh_IlXdHG2H45DY0APdfbMLvn0bWBJ-ut1CWUI59sTtkaEqKRXjyuVALHEb_eE1dZFKwrfabQwDYN82Fqpm8FO8gE1q0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: نفت در حال جریان است ، ایران هرگز نمی تواند سلاح هسته ای داشته باشد (جهان در امان خواهد بود!), بازار سهام در حال رشد است ، شغل در رکورد است ، و قیمت ها در حال کاهش است (قیمت مناسب!).
🔴
کشور ما قوی ، امن و محترم است مثل هیچ وقت پیش. خواهش میکنم!‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/128925" target="_blank">📅 17:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128924">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ایرنا: ایران به پاکستان اطلاع داده است دیگر نیازی به برگزاری جلسه حضوری در سوئیس نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/128924" target="_blank">📅 17:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128923">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
تلویزیون پاکستان:  سفر برنامه‌ریزی شده نخست وزیر شهباز شریف به سوئیس بدون ذکر دلیل لغو شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/128923" target="_blank">📅 17:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128922">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f05f75b6.mp4?token=ba_qMjILiDP7naB7vjwV0FwDohbpG8_6XOXY0Mh_pwX4orDpMa7_jJDPSFY8ZQK2Ej1A5Fa3hsDW0yknCjNsV3VEJ3yhYAdjAzXv-LgOke_f0Z9i9lLXkTwWgPwTzwAd18YMorGJbABY7L5FeU2p2OUogwtHcSIJUJJCz_e9pT-v-0Mu9-WVPHhzJvt9_pyBF56dTICPm3QYmB_q9UkbhO4Y2JNnOMsdLA8Jlt0xJlgSbUuBcYX3XyfL1EK3eNGsuZ0GcTROLuNLEniLByagyNp3mdePS_RkTp68AP-lrALnQmZPMEMIkhWNx3UkHtDtosHOXUhWCThrw0InjVBb0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f05f75b6.mp4?token=ba_qMjILiDP7naB7vjwV0FwDohbpG8_6XOXY0Mh_pwX4orDpMa7_jJDPSFY8ZQK2Ej1A5Fa3hsDW0yknCjNsV3VEJ3yhYAdjAzXv-LgOke_f0Z9i9lLXkTwWgPwTzwAd18YMorGJbABY7L5FeU2p2OUogwtHcSIJUJJCz_e9pT-v-0Mu9-WVPHhzJvt9_pyBF56dTICPm3QYmB_q9UkbhO4Y2JNnOMsdLA8Jlt0xJlgSbUuBcYX3XyfL1EK3eNGsuZ0GcTROLuNLEniLByagyNp3mdePS_RkTp68AP-lrALnQmZPMEMIkhWNx3UkHtDtosHOXUhWCThrw0InjVBb0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رویترز تأیید کرد که محاصره دریایی ایالات متحده بعد از ۱۰۰ روز لغو شده و کشتی‌ها بدون دردسر از تنگه هرمز عبور کردن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/128922" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128921">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
تلویزیون پاکستان:
سفر برنامه‌ریزی شده نخست وزیر شهباز شریف به سوئیس بدون ذکر دلیل لغو شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/128921" target="_blank">📅 17:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128920">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8cD3dUf7F3k1embW72nYgk6ZcjlWGSecu_YaDlhFG8FBk0AuMBp98XZ6QzfupJ1bOBoPMzp1u64D5IulsYqoeFQaKggg_4o0qTAZsvb24dbWuxG1A71r13HQenhBK6cBZtHxpeWMT22K03f7Tnwp9hHViaqKBdDrHV6Jjh1BRzW6vL0ift7SD7cLnnQ0AHuvP6RK1IRqApOQla4OC_JrU0T8IdxweSN8RUmPK9X92fkyPmPxVTycJ1oN_ELCKVZeqHkJix5k_BB-L1EUmjp8Hu9rVCZ3RflJ5Hv_O0e4B-p8AYqzo0pzYr-LqrRI0Ro3-7sBPJ4ilFXZDFZWM21DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این عکس رو هم آمریکایی‌ها خیلی زیر پستهای جمهوری‌خواهان و جنبش MAGA دارن میذارن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/128920" target="_blank">📅 17:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128919">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIF8scEGc1q2tRc2mIQQwz324_-xvWmgb2G4SXPV-vWfxapXwAsREO_yqJxOQleI7mqfeI9ZP5svCZ8GyoUaLvaXiPQnMpHUJG1NVuolgMfdOV_CF5Hyorxlt2-ukIekcHNNvJKwOzVcNq1Pd0l-AEsNGtDoSjfBth59TUmi6RKwAJryNcnf9xiUG7K98FY5SfhSXfWzA16BolQk6R5bI6ZSnqqYeTlqVyfuKvI9u_Sd5eWLeOJ6RIhIZEot3Ak6FwPVzR8gu5PG0uB_rlKDRTM_sgkElGI_KFvF2KpmQgfE7Bp900MKflr5OVkrTcZhvqLu-YLsSo89WaTFdsFKeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: هنوز تصمیم قطعی برای رفتن به ژنو در تهران گرفته نشده است اما در صورت رفتن ریاست هیات ایرانی با قالیباف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/128919" target="_blank">📅 17:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128918">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9FIy0kJ_B4MJqmPRk08kQYkjLvqo7iwCGy--XzP5XTQjUuzwaMsStzshxWnQrI_b04M9PVrljqYdXPzBH3HPqNJgt5sf7bsLdtKzyQX19xiJ0khKBtr2mBCNxyKXSPuWzvy0vfLC7ow9BCY79Z5c88GdWBiKqB5RtbqZt_iEruDHkIY4vV5hLaQreZ-XAcRi8HR9oIz1KuLtwIQoss6AEvRBrvDM5iCvkxzuCMyGUSfKJMp2gIF8ogTryEJPJfS46eSU37Z9bBqCpDnCio7dMOPy1D5Bqiaxpq_Q9VO3BskCUKeS2TM8A4O-xC3XcWFgoIcmb3myeLPS0_PscDuwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مِی ثاقی:
یه مشت وطن فروش به برنامه ما هِیت میدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128918" target="_blank">📅 17:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128917">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هنوزم آتش زرتشت ز سینه پرتو افشان است
هنوزم فره‌ی یزدان به ایرانشهر تابان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/128917" target="_blank">📅 17:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128916">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/128916" target="_blank">📅 17:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128915">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نتانیاهو: ما امنیت را به شمال باز خواهیم گرداند و این مستلزم حفظ منطقه امنیتی در لبنان است. ما نباید از آنجا عقب‌نشینی کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128915" target="_blank">📅 17:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128913">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pF720fGwB-OxHCuEZT3RQbeRDbDoYFEwTKtEv0S0AVLjQiAPcFl-_TiD6L1GrXq2vMfmCjB6RXkgr4gU4NvKYr_gIrXDGfCIneWjghpAhfoTLxfg6-3cEtFeX293J95M7_wp6RNrU0dOMXAa_YlR73hfFX_F2WlknBEhaF_dfQzQPWm9orfTHK1qKT7fqd5pnVl5N_STTJmTntTGoXISXLlmP5Z19llqQunUodsouoSjfowK1DeJBPjNZLRAt9_vE26tZ-bcj6RYjelNdBhI3D-uyHYUUpiNImRxpI0e-LmVBmm__7LRjrcad9esZbWaFdwxt0NuZrCQFd_cgX4bTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxPbNNQftdXliPx37-Sje_SsIzlGcrzXtoy5OjnnAJKU7pL2dhR8CpuiSZ0IGLeUgXVsgLapQP8CNn2HAGQNEhDxBLAIMguz5ok2MJMNqGf_PCQlfmstl7tU9TzdfCh8sWb2nvIbt5MWZiDL_uqambq4veqLGcOK2aJ9j-2DB11gBn2pxNEvCQMzX0PZUNl0X2AjJBjnukjtP5g1hwj3X169ghB6KDc01OC5ndZZFBgSvWcc1NhM2W9-EhIFZSlkuyi-yWfkxPpCxLU_9FXogDJN6lZkurplK3t0c60cb0bqHoN-7jPJoQEzICa0duKjHVWYIxk-9mB777S6JuJEXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128913" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128912">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7be62b11.mp4?token=gIDYi91SKBLUuOtlPZrNIs5JypjU3RZj4KTI6CQikGrWwgKAhWLnfF07XYaVX7FKLibTuS6TNdCCogiL9NTrDJUgeaAEy0ItouzPXkdUJF1yqxOgN3BbBHt_PpfhifROK0076-RFl8tAM6LmJxsybnH_Tb_NEDHAhuROOVSrB1WcZcoJkzaaL81Wiyz80TvvdxlQmFcD0WNiL-o_HWYeWf63XPx-GzHuVP_v9Pn81ldI0BA6lmSjzjB_xzkkFBLjlGuP3ASen1rnKxHwmX6aV6bxVRIeVhRd3NHW_CCePqCatUmXa-l1hjd_iCl7GwVhR-zydj1Hx3GD7wBdubLOiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7be62b11.mp4?token=gIDYi91SKBLUuOtlPZrNIs5JypjU3RZj4KTI6CQikGrWwgKAhWLnfF07XYaVX7FKLibTuS6TNdCCogiL9NTrDJUgeaAEy0ItouzPXkdUJF1yqxOgN3BbBHt_PpfhifROK0076-RFl8tAM6LmJxsybnH_Tb_NEDHAhuROOVSrB1WcZcoJkzaaL81Wiyz80TvvdxlQmFcD0WNiL-o_HWYeWf63XPx-GzHuVP_v9Pn81ldI0BA6lmSjzjB_xzkkFBLjlGuP3ASen1rnKxHwmX6aV6bxVRIeVhRd3NHW_CCePqCatUmXa-l1hjd_iCl7GwVhR-zydj1Hx3GD7wBdubLOiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیکه سنگین حاج فتل به میثاقی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/128912" target="_blank">📅 16:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128911">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پولتیکو: ترامپ به وضوح از تماشای عکس‌های سوختن کلیسای جامع دورمیشن کی‌یف که زلنسکی به او نشان داد، تحت تأثیر قرار گرفت
🔴
این فشار نهایی باعث شد که او از یک بیانیه مشترک سخت‌گیرانه‌تر درباره اوکراین حمایت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/128911" target="_blank">📅 16:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFT-xgPYr4jwqUmRaSsLv06BSCAEnQeAP91XbTdT7PKyhAe2XTIoHDpTKuDLde2PAHd5cYnlvW-n6Y3FSXmgl233w1RBt2yspoDVHJwaNJPARGCwIfyq21SRPG0-4xIpZ9h_GVQaKuoL_3fbzIw3fs92YXFBhi9H5bbHFyuCqowTvHV4CJFVj8aXt59_wCQGVzhJnIjAwcJtP8XEuC1PuYM-CRBvaT-F37YC26eKMVvQL2Y0zDCfNMtjLerAaAiSgmRFrUpXIpFFApF6MzQkD4ZRPADLV0WM-vJnUYY2u_Uxt41-hyGHqL_dRA4Ochl2gVGaZTK7EH_lvvnpN4xrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از تأیید پاپ لئو بر توافقش با ایران خوشحال است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128910" target="_blank">📅 16:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128909">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90181d0fb1.mp4?token=ItFX16sBCas8TEIH5nGxV3PEz2lAdPEc5N3EEb7oDYQfCAY--kAAXOkG8cbnSuu2nuOOzMPnK-Pz6JpvEjGXyXRphSMfFCPSqCViB90wGwAdDLCvucKiJ96tjrOoi5Rmc6UpDBxol6elnm9R0XnzQcW3e8kb3-9rKCQ40FPR7fQb1SP4puYNb2OO9DiNi48T2qJGer2JVWNfdsxT5iK5floQcdfL68VxL3HwsA-RHVuoAxqrhz9LCmz-2H0sb1HPhCPziR2oPm9k-8fdJcunXTrpdZC4FZUMpRVNtOCdjDtkfdLukrjCkP9bghraBL5IYMIcmPRPrGsPADf1bXsnHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90181d0fb1.mp4?token=ItFX16sBCas8TEIH5nGxV3PEz2lAdPEc5N3EEb7oDYQfCAY--kAAXOkG8cbnSuu2nuOOzMPnK-Pz6JpvEjGXyXRphSMfFCPSqCViB90wGwAdDLCvucKiJ96tjrOoi5Rmc6UpDBxol6elnm9R0XnzQcW3e8kb3-9rKCQ40FPR7fQb1SP4puYNb2OO9DiNi48T2qJGer2JVWNfdsxT5iK5floQcdfL68VxL3HwsA-RHVuoAxqrhz9LCmz-2H0sb1HPhCPziR2oPm9k-8fdJcunXTrpdZC4FZUMpRVNtOCdjDtkfdLukrjCkP9bghraBL5IYMIcmPRPrGsPADf1bXsnHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی آب و فاضلاب کشور: رقابت های جام جهانی مصرف آب را در کشور افزایش داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/128909" target="_blank">📅 16:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128908">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ارتش اسرائیل: بنا به نیازهای عملیاتی، نیروهای ما در منطقه امنیتی ۱۰ کیلومتری عمق خاک لبنان مستقر شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/128908" target="_blank">📅 16:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128907">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
صداوسیما: ۱۱ فروند کشتی از محاصره آمریکایی‌ها عبور کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128907" target="_blank">📅 16:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128906">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: نخست وزیر و وزیر امور خارجه در تماسی با وزیر امور خارجه عربستان سعودی درباره توافق واشنگتن و تهران گفتگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/128906" target="_blank">📅 16:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128904">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UW2uFvej3JGm6nlzuTkWGTb4lZNctHiHueqyR9FoE9IfcWNFGRwBvEQS7TWyFpgplT9sReUOYhJYwrMpNSkfKRUCOSjckbRHxzCo72jFjQaW4o1-yvpO8kiqh3DB7uh7oweFiRIg3UuJo_3DEKNnFBHpzFkwiqMl1g0W9ZKXuwgOheckXlx_k91uwaI5mC1wyIowmMD-zFbZgnPyurHW-kYpWhJ4tIBtO5_LQgUPZRcdCs0HRK9PNAJSZifqoywJL3w36w2qbz5q1WO9a_3GsI7Eeu4-ZDs8qSkChUrLHkZUQHaHQB_2RN9h60q33v8GKgh7IY80P8PYU0CTcMKHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/me5s6ZoNnY9eNXUWfVASeIyk5a80ttOUdnocDhl1kv7Dvf_knk2Ee7hoBSVNcrp2X9-7SNdmNEAdhGEN82p2MWeEBJ9HNnhbwosuI7PnIe7T5ob01E8qOFDO0BAnU76AkD_qtS_uG3GaLBdbfMHbA4zDBeJFlHJDT3jk_ibBItfjN-KaGafCQjBUzoXvOuPYQtjtsAsHw7Kd2V3q6i2Je2dp60-Z0AIr6e6c0yw8QBczbXPZzWJAgtGE2-Y0Rtf4fzU0SDk4nUTH6c_bBW0GaWhmO8MWGCsODNq8g077q30cJiR2sB7n55k3YEbqdlnPsvNt4YWC5fjkfF2f2DC_aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
فوری / رئیس جمهور پزشکیان متن اصلی تفاهم‌نامه بین جمهوری اسلامی و آمریکا رو منتشر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128904" target="_blank">📅 16:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128903">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سی‌ان‌ان‌: نتانیاهو در تلاش است که بر توافق نهایی ایران و آمریکا، از طریق سناتور‌های حامی اسرائیل تأثیر بگذارد و بر ترامپ فشار وارد کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/128903" target="_blank">📅 15:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128902">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
یک منبع اسرائیلی به سی‌ان‌ان گفت:
نتانیاهو معتقد است ایران با محدودیت‌هایی بر برنامه هسته‌ای خود موافقت نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128902" target="_blank">📅 15:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: کشور‌هایی که از تنگه هرمز بهره‌مند می‌شوند، برای باز نگه داشتن آن اقدام کنند؛ ما به این گذرگاه وابسته نیستیم
🔴
مذاکرات با ایران، حول موضوع عدم دستیابی به سلاح هسته‌ای خواهد بود
🔴
حضور ما در خاورمیانه به میزان پایبندی تهران به یادداشت تفاهم بستگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128901" target="_blank">📅 15:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128900">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
توقیف کشتی حامل ۶۶۰ هزار لیتر گازوئیل قاچاق در خلیج فارس
🔴
محکومیت متهمان به ۴۲ میلیارد جزای نقدی و حبس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128900" target="_blank">📅 15:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری/طبق گزارش CNN: نتانیاهو به ترامپ اطلاع داده است که اسرائیل خود را متعهد به یادداشت تفاهم آمریکا و ایران نمی‌داند، همچنین جنگ در لبنان را نیز متوقف نخواهد کرد و نیرو های ارتش اسرائیل از جنوب لبنان عقب نشینی نخواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128899" target="_blank">📅 15:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
شبکه کان اسرائیل: موضوع عقب‌نشینی از لبنان هفته آینده با هیئت لبنانی در واشنگتن مورد بررسی قرار خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128898" target="_blank">📅 15:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128897">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فرهیختگان: گفتن اینکه توافق با مهر تأیید رهبر است و یا تحمیل توافق به رهبر؛ هر دو خطاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128897" target="_blank">📅 15:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128896">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
امارات متحده عربی با تصویب قانونی جدید، حداقل سن مجاز برای فعالیت در شبکه‌های اجتماعی را به ۱۵ سال افزایش داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/128896" target="_blank">📅 14:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128895">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
بقایی: بازگشایی تنگه هرمز صراحتاً بر عهده ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128895" target="_blank">📅 14:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128894">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مدنی‌زاده، وزیر اقتصاد مملکت: قرار نیست توافق با آمریکا، اقتصاد ایران رو به شرایط کاملا عادی برگردونه.
🔴
حتی اگر جنگ هم نمی‌شد، با چند صد هزار میلیارد تومان کسری بودجه روبه‌رو بودیم؛ الان شرایط سخت‌تر هم شده.
🔴
دولت چهاردهم بعد از جنگ ۱۰۰ هزار میلیارد تومان از بانک مرکزی گرفته و آثار تورمی اون در ماه‌های آینده نمایان می‌شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/128894" target="_blank">📅 14:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128893">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سخنگوی وزارت صمت: ر اعلام قیمت از سوی شرکت ایران‌خودرو، نسبت به آنچه که توسط سازمان حمایت محاسبه شده، اختلافی وجود دارد و ایران‌خودرو رقم بیشتری را اعلام کرده است که آن را هم اصلاح می‌کند و اصلاح‌شده آن را قریب‌الوقوع و امروز به بورس اعلام خواهد کرد.
🔴
دیروز چهارشنبه شرکت ایران‌خودرو بین ۳۰ تا ۵۰ درصد قیمت محصولاتش را گران کرد.  این خودروساز از پارسال تاکنون ۴ بار قیمت محصولاتش را افزایش داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/128893" target="_blank">📅 14:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128892">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d006ba55fd.mp4?token=Y45z9fADNhS_gd5QObLIGtZuVXd3R7JfZhlcb6cyBf4ZboDpf_o47AZ9R4JlwXN1RYJhR81iKc2DJllrZiSdiGfQVl8PKJX4DS4UiQhF7YRrkqX62ItG3mqp44Dwk55A2oFTz7hXyIZ38dQwY0MHrYOgH5jRUqX24n8dQWfUpRrQJ5oSqQ84ZWAvPSNPY6eKt3chssotlmAtstTAjNyKHt80FaXD-K-aHaUo4nncIhCoOGJzmBfLDvTrPRO60AZyNgY6jlpfYIdvEmVoOe-YsM3CX5hkQiCeo-vDH8NvvlhhmNh-QX53hC-In-uTfLtOYV6mvGhJ2oQKmwzdzpnyTRaqTi9NhiI1AjySJ5Q0LAtZMWSYL5VAjciUwAHruVpHTBnRKR9I3IR7eBIjdl6ml0ALcycdNIgFNFozNS6U99RMO7hOcIfVGI2wKdJCVofiSTGAB-HRE3-1SsP1PTXDV3mx6Mq654ef0zmphyr1XoQyBw2U0QCrYzC5eTqYQfjV6QLxd3I1M_P72O36KOPVcucs9jezoZyl4TOjcPspFg207RymnckXUAtaeqLLi055mVtROItXBhbFKYLUsF71jXwI2_fMcNAbRtgCyCvnoOxrTaiIMBLn0cf_lQJrazgzsu-aqag-p_nEZsXQbeld0HXa98SK8CWYiAzjxZw-FPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d006ba55fd.mp4?token=Y45z9fADNhS_gd5QObLIGtZuVXd3R7JfZhlcb6cyBf4ZboDpf_o47AZ9R4JlwXN1RYJhR81iKc2DJllrZiSdiGfQVl8PKJX4DS4UiQhF7YRrkqX62ItG3mqp44Dwk55A2oFTz7hXyIZ38dQwY0MHrYOgH5jRUqX24n8dQWfUpRrQJ5oSqQ84ZWAvPSNPY6eKt3chssotlmAtstTAjNyKHt80FaXD-K-aHaUo4nncIhCoOGJzmBfLDvTrPRO60AZyNgY6jlpfYIdvEmVoOe-YsM3CX5hkQiCeo-vDH8NvvlhhmNh-QX53hC-In-uTfLtOYV6mvGhJ2oQKmwzdzpnyTRaqTi9NhiI1AjySJ5Q0LAtZMWSYL5VAjciUwAHruVpHTBnRKR9I3IR7eBIjdl6ml0ALcycdNIgFNFozNS6U99RMO7hOcIfVGI2wKdJCVofiSTGAB-HRE3-1SsP1PTXDV3mx6Mq654ef0zmphyr1XoQyBw2U0QCrYzC5eTqYQfjV6QLxd3I1M_P72O36KOPVcucs9jezoZyl4TOjcPspFg207RymnckXUAtaeqLLi055mVtROItXBhbFKYLUsF71jXwI2_fMcNAbRtgCyCvnoOxrTaiIMBLn0cf_lQJrazgzsu-aqag-p_nEZsXQbeld0HXa98SK8CWYiAzjxZw-FPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت امور خارجه چین درباره روسیه و اوکراین: ما حتی یک قطعه سلاح کشنده به هیچ یک از طرف‌های درگیر ارائه نکرده‌ایم و کنترل سختگیرانه‌ای بر کالاهای دو منظوره اعمال کرده‌ایم.
🔴
زمان آن رسیده است که ناتو برداشت نادرست خود از چین را اصلاح کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/128892" target="_blank">📅 14:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128891">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
میانگین قیمت بنزین در آمریکا برای نخستین بار از ۳۰ مارس (۱۰ فروردین) به زیر ۴ دلار در هر گالن کاهش یافت؛ موضوعی که همزمان با افت قیمت نفت و تحولات اخیر در بازارهای انرژی با امضای تفاهم‌نامه میان ایران و آمریکا رخ داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128891" target="_blank">📅 14:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128890">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsMlr-FKueE46RXqadjlgOBYAqphTwDy3MrxAMZeDO3LBRh0v_Ah0V4MNXSuoRfNnit5j2hU7j58IqVsNDUQynfHS9x6z_mBVGV6H3VXHYkDpCNbq06yyLlmxc7TajgJ_W5YQzbyj9G26UKvoXoiu2nO6PPknUP-gfBxv5cQTnsYnwyZelJKSQTBqpkWe4WBoPLVPv42rXX2WckWFI5icOXClnrZFmBmNV5OX0JzJaxZdHHu0tRROL6J82VW0qgpbzYoMr9Mit9yaUfxh715TeIp1aRusbWXej8svYu7HJ5N5zaB4L0mzd71hCa2r_N27MBhT5c36gyDyA47SURAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: به گفته چهار مقام آگاه، وزارت دادگستری ایالات متحده در حال تحقیق در مورد چگونگی ایجاد یک سبد سرمایه‌گذاری جهانی گسترده توسط مجتبی خامنه‌ای، رهبر جمهوری اسلامی، با اتکا به بانک‌های وال استریت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/128890" target="_blank">📅 14:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128889">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_MZUMiwdT6qH5nF-hzfV0tzrU1zRLotKBfWWqUsjbn853rGZDHfzHeknAiP93n9nXxomiA8Pwg04bBPXaYkQIwDN0piuJE9w-jljiDo57s1NwLttJJECKL9wL8dlCBxc8YoSgZL_T2v4DBZK0UEdmO_6ikrzgK4nWKTmQ_2Ra6Be6MhaOYPdt_I6gwaQqIM7seq4QRlwfr14bCj7bUsAAQQbfqcoD9O9Fm1e59Ai37BHE2RIuxyOdeY48zDLGIJSHDpupLfBTVOip-K28ypjKjeHbpLbe_TlCPUPplNFuXvn8E2QxUaoU6o4ZKbBj5qdC-xZr3w6sIUm_x2A50jKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: این یک سند تاریخی و پیامی از ایران مقتدر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128889" target="_blank">📅 14:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128888">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5nOL3JTkUnqTi7ttPEQUHKruyzPvOymHcHvcdQNbjq_qIb1EIYr9I_f_Vcrna6PDBCC0NA5pVBWkD1pmJislhOlV9qC2oNDwPcqHbyPKJ2CEsgBbKb5_xXGtXLkR8BhvLFcL4WKxC5THuC6dZxVmqWb0bU-PC2GrPLK8XzsD_Jw7ZJssSwXfma0M4j8lXpv7TKNE278ETICNY6tGHlNV6D58fBdjdl1EVwtAF6CoxVGY5_0F_nl1Jh18ze_x5PLW7YIX6aFel8oXlFISsBdZlKRL0f1bNhRxk9tOd1KDSwrdQEmvxWBXJ-lK6NVQCBDl6EKE5VgR9XlzoRkJlXJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بهرام پارسائی نماینده سابق مجلس:اگر کشور بی در و پیکر نبود این حرام خوارها بی کیفیت ترین خودروهای جهان را ناگهانی ۵۰ درصد گران نمی کردند اگر آنقدر که برای مذاکره دست و پا می زنید و با هم رقابت می کنید کمی به حقوق ملت اهمیت می دادید در این کارخانه های غارتگر مال و جان و عزت مردم را تخته می کردید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/128888" target="_blank">📅 14:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128887">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
به نقل از المیادین، یک تحلیلگر اسرائیلی در مقاله‌ای در روزنامه «یدیعوت آحارانوت» از آنچه «شکست راهبردی ایالات متحده» در نتیجه توافق با ایران برای پایان دادن به جنگ خواند، سخن گفت و مدعی شد: «این توافق، جایگاه ایران و حزب‌الله را تقویت می‌کند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128887" target="_blank">📅 14:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128886">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
زلنسکی: اگر اوکراین بسوزد، مسکو هم خواهد سوخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128886" target="_blank">📅 14:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128885">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فیصل بن فرحان آل سعود، وزیر خارجه عربستان: «حمله ایران به پادشاهی و کشورهای شورای همکاری خلیج فارس، اعتماد متقابل را سلب کرد. پس از تفاهم پکن و آغاز روند عادی‌سازی روابط، ما در آستانه گشایش همکاری‌های اقتصادی بودیم، اما اکنون عقب‌نشینی کرده‌ایم.
🔴
پیش از هر بحثی درباره سرمایه‌گذاری یا همکاری، باید درباره بازسازی اعتماد و رابطه گفتگو کنیم؛ این مسئله برای بسیاری از کشورهای شورای همکاری نیز صادق است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128885" target="_blank">📅 14:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128884">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAP-8k8uhrzJmEhDsLNs-CeBeEmCibCQq4SVAaNZIj97qx97FnfR-PxudavLQijkV_CqUveZIJDINe-gcgg2j4ZZQc8Z2FCDXXM1ttmDOQwZKfX-6zd5Vql6rpbX7hOFIWn8MUzzUywv2fgyMylO3eqtFUJvMr4To-Rht3ewqUS_pyhoUbVyVvA_Sh38Gr42OiMmTP2Q54mL3I_Mwa9VYWpiwSdO4p9lwwTOm51P0uZcx7YHSNOSd_6qTayBskMk4XtasiKFJgGToBTYPKYiTJgWUF9FZawAA9_iOnWxo0vcsmPjFpGAbRPTmwefy8mfdaB-xP1KvXWHV6tE329XVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان نخستین رئیس‌جمهور، جمهوری اسلامیست که امضایش کنار رئیس‌جمهور آمریکا برای پایان یک جنگ قرار می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128884" target="_blank">📅 13:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128883">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: به طرف ایرانی اعتماد نداریم و آماده هستیم در صورت لزوم حملات علیه ایران را از سر بگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128883" target="_blank">📅 13:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128882">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رشیدی کوچی، نماینده پیشین مجلس: متن تفاهم‌نامه ایران و آمریکا بیرون آمد؛ آقایان پر مدعا؛ دقیقا کجای این متن ما را مستعمره آمریکا می‌کند؟
🔴
آقایان فحاش؛ کدام بند مغایر با منافع کشور بود که اتهام جاسوسی به مردان میدان دیپلماسی زدید؟
🔴
شرم بر شما که این‌گونه به خاطر بغض‌ها و کینه‌های سیاسی، امنیت ملی را به بازی گرفتید؛ رو سیاهان تاریخ شدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128882" target="_blank">📅 13:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128881">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزیر دفاع آمریکا: تنگه هرمز یک آبراه بین المللی و برای بسیاری از کشورهای جهان حیاتی است، اما ما به آن متکی نیستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128881" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128880">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3g9oJPRvwhafhc-atA1zBWMINXHBmzGS-NgVQH7MmqRkRey7lm7NXu3BX4-_sMgvi_iPIjhCWjYMawK_SrF2xjY_AB2LKydcgxYyLQpctJgDD1yEVtGnAdtxeSVQiKfWJZ9sXfTC3ncMk0KKDDIpi9qL4AZV8KZKfU2JUG9KmXQLsT312G-zPy1eWl-IKzYamEGwRC8mdmwUpjuGXecwqAuN1sEPt-vuG9_AvjKcG--yhxHJ433F71n42rqRYyEaR5YjBL9HVbGuY-jx3L2FaOWCZQro3I0tmuZ83Bp2nlB-8oMwfF0hjq0vioHBVtStW702QQAMLPdv_jYp290dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات هوایی ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128880" target="_blank">📅 13:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128879">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1nMWaOPBAvFyZlxbvQEpQNADi1YF809uuPXRASMsUae3neRYue8nHDn80QvQnQKcVXR0JxMkZo5oGfseECsy64bQGk5UzK3G-DC4_H6Qh8e3kVd21gEEz31z_-1J57wsjTf5FwK07qrwEKwqjclRIRkANOMXE12_iNgsUZp2s1xJOD5kor0IKkTRD54ficdsPbR2QsKbMfk5QUg43u90l8n1R8OPipqT50VRh9sSIYE18Ah-FPWDFRjmIhK_Md6EqL38_aNCmaThVHtt5nalDDZ6Doo08uS59giw0gwoLum9VMwvu8O9PS57vY7j6jqt8OUmHcujB6YOCRx2NuEog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور خارجه  اسرائیل اعلام کرد: پس از آنکه کایا کالاس، اسرائیل را با رژیم آپارتاید مقایسه کرد، روابط خود را با او قطع خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128879" target="_blank">📅 13:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128878">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
دار و دسته رائفی پور بُت سوزوندن
😐
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128878" target="_blank">📅 13:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128877">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js_omgd2e3s759hJSKNUazAiSFFqNfGOnP7B3dFhJpwqSuM4z_ZPXpCKXT0etmJmGk7nMxr65_Jl7bpGve-ev1g5oCV1C3Z94_6_zqIT9wmVJAraQAAWXoFnI8a_do7RpwTbfHKwc__d0UbOi-GvTJvMWsy1L56lm6UKg_VyVXUAzArICdG56Tu3JaJii7jx5br_fpxKwlEAEDcf7SWQSnQMpeOrNQc__pxSASOTA3F7DKMXmRPLECRVIgkLoAxQYoREMDevgYEpBJuv4R6jbKpqGOad7hm-sQa09YhakV_aIsK2-oHZkqx7GFf7W9EbUS1Iq6VedIusztga6Fp3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار وال استریت ژورنال: چه عکس جالبی. امانوئل مکرون که کاملاً اروپایی‌ها را در مورد ایران نادیده گرفته و مخالفت آنها با جنگش را سرزنش کرده بود، موفق شد دونالد ترامپ را وادار به امضای تفاهم‌نامه در ورسای کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/128877" target="_blank">📅 13:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128876">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شبکه المنار اعلام کرد که حملات اسرائیل به شهرکهای کفرتبنیت و حداثا در جنوب لبنان همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128876" target="_blank">📅 12:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128875">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTCmGC7cMgk5S-62lI2pSn_QP49E-FG0IDjTAA7tWLG6Uz9d_vVvM1YU7tnp88vN_laq32CVRtKzBfFgS95rFszDb4AsziVDd_mW_tUEAPV6AS3aTYcmHGVSaCmFPr1j87QuH5A59V0Mg-6rYvBzh8O5eVQqJhHrBkAuIwUHG-28igpAbUcUAuHXnfXh6Rztxb3lCjUNG237BY5YhTHGRcBh3H1Zz6l9B3UniaVtU1aVutjSeRbQ2CZLOZ09CKLULw4X-9M0UNzDHRdtSlCbbfqNVMu_JJMXEzQIsCB-SFBxzVRTo7-SOTgh5F_3AiZcNoIm18cSlRjjWQPpjW1gQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دانش آموزها دایرکت سوراخ کردن که اینو بزاریم، ماهم گذاشتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/128875" target="_blank">📅 12:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128874">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی اعلام کرد:
در حال حاضر، سطح تماس‌ها و ارتباطات با ایران در پایین‌ترین حد خود قرار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/128874" target="_blank">📅 12:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anHbsEk5vCBZU7j4MUAhw9HKH2_LtHaGF0CcsjHDtuimEjrXevitRqyEwkZpLL8sdhbNmzCT_WYpwLoJe3oulMBTxzc_Mb3wDPNXmU0qPNpfj5JS31JFH-j7PApOQ93dCyJOF2MuHdjJauQdeYrA7hgKYzU28A8Oxw7T3TpiMNgi7XeaAeLaf5eRkrl1KNv1FtSAR4sGFKTAbonuCqAuGN3ouS1b3UVD7j63A8mmwG7a5DadkUwXN-2AAAA6L3CtusFo5PA3Oc34hqDsAqeMCY1WSYgBTl0KJztcveIkzcOttqbO-CjtGpB0WjlADKwbAAFlMJYeis02Y9i9aBesgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، هنگ‌کنگ در راستای تلاش‌های پکن برای بین‌المللی کردن یوان و جذب سرمایه‌های خارجی، آماده راه‌اندازی معاملات آتی (Futures) اوراق قرضه دولتی چین می‌شود. این اقدام گام مهمی برای تقویت جایگاه پول ملی چین در بازارهای مالی جهان و تسهیل ورود سرمایه‌گذاران بین‌المللی به بازار بدهی این کشور محسوب می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128873" target="_blank">📅 12:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128872">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfpjvdtDQEyHc1xX58BJMmtotq6s9H15ye5bNR-HipfjD4op7IIQj6vsin2zdFa97zwvpKF_E8ZxI99_BC88yjhbdC5UDYGDAU_I8Kg-rcFDljmxvs2kyQivXzg7SbKBK7T3pCo50ZcLnriWuPxWiYWlNNlGbNIcFKShmZ2Cn45siOVOMf1SzsPTkKUqcywtyx26O8ae7MihArei8vFrGzBRKhn32tDDROxs5EUAW3aupq2GCrUeooOBhZsONOESmXD7Pg8jx5hESPB1cmbvmTlliXIXKwvocgBvDBJJ1XjEIPB2t3m0-n4wTGnz0uSmLrq4qcibyozVEfYuADXHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: انتقام آقا رو، امام زمان میگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128872" target="_blank">📅 12:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128871">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
شهباز شریف نخست وزیر پاکستان به عنوان میانجی، یادداشت تفاهم اسلام‌آباد را امضا کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128871" target="_blank">📅 12:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128870">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
منابع العربیه گزارش دادند «نخستین دور از مذاکرات فنی مستقیم واشینگتن و تهران فردا در زوریخ سوئیس برگزار می‌شود.»
🔴
به گفته منابع این مذاکرات فنی میان ایران و آمریکا شامل جنبه‌های حقوقی و قانونی مربوط به رفع تحریم‌ها علیه ایران خواهد بود.
🔴
منابع العربیه خاطرنشان کردند گفت‌وگوهای فنی ایران و آمریکا پرونده دارایی‌ها و وجوه مسدودشده ایران در قطر و همچنین پرونده هسته‌ای ایران را در بر می‌گیرد.
🔴
قرار است در نشست‌های مذاکراتی غیرعلنی و اعلام‌نشده، پرونده‌های مرتبط با لبنان و حزب‌الله نیز مورد بحث و بررسی قرار گیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/128870" target="_blank">📅 12:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128869">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وال‌استریت ژورنال: اپل تایید کرد ، قیمت آیفون افزایش می‌یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128869" target="_blank">📅 12:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128868">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTAQzr5_pfiyUz1yH07mZTbbT0i5H5p5nR5tTNQ-rXEiFiRtM9HX3ZsZJgz7wBX_DhA4JSWNGZ1DN1Vr2WWki2b9qpsxYy_o4WxbKztsL3ce-jEbBdVXJ8GJ6FhSZH_f_xFy1YSO_2v1x2ZwDy5wgMTcaF4pPi2mR5Psl2syb4XwjRsb62MbQ02kyWvKYSzJppvdwafdaqWbGE1Y9Dyv9PFbtL7b6TPc_-CDULbi-27gJXfstc0Mzf8QXWHj8It3bR0Q1O-5aHa8h7i_sO_gae-1xZcQMaQ5wr_kFS_6kPontdQsKoJaXmKP-zMKOvO-osfPlp6_D6NmlsciVyoHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:  این احمق‌ها که فکر می‌کنند من در قبال ایران به اندازه کافی سختگیر نبودم، در حالی که بازار سهام به تازگی به بالاترین حد خود رسیده و قیمت نفت «به سرعت در حال سقوط» است، یا حسودند، آدم‌های بد یا احمق. آمریکا را دوباره بزرگ خواهیم کرد!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/128868" target="_blank">📅 12:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128867">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38821025b7.mp4?token=ifBz6Y1C7tzv4MfjnjvjTHFZRQIdfRwMm2exI8K8YEH26O2vhinNPVR7giZlHQgvm7KhnyYvol2Zhdi0b7Gw6KqvywvG0YRlCGHV9Z3EwfkkrYrc0PIdaCAtISy8nf7MQILVeZb8UpAVjbkp5nWuECIpug7dfuMTtKj3usDCsFyQw1rLicHcsdATdHe6jOSnsW6MSrM-EOUUqkZEnM5X6qXOwOO3WPMWtP1sx5Zmi6-QnNhfsYsjiEeOlybqhsYGuvpe2m3XQUspS62uGrKn-xKrs62bvh-bfAchHkx1iO9oN_3mh_HINe6EBUcUKIDnq7M5a5GBKJf-WOAAWfzjQT6TT1op4MCtsInv9x18L6rOE4U__Kv1qSEFUEXaASJFdDBVCvfL-6H9Yrgckora9SpNR8aS1Q4C1weLptWT0TGuiDZOqj2dksKl3RYDld0AhhlSEgQtjwz7EmEzvrGjG3yPudjJCNQjaCKkDzE7We1t2XEL_usFAeHyYC2zdXZA0tcmds7G8i5kGSnsWHhnuDI1SUqyxvaDtTHWfqhMoUqOA2vkHFXBocL4lTph5xFp-18jjcs8wRsrzmFAanahsw5aOPE6n4_9FM1LdfvRaLPiCmpq8AZcAkd6jD6DWb6j2JfC4gcZnb-ybnwl135g2yiHFsfjqCfIcNyBRIGRrd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38821025b7.mp4?token=ifBz6Y1C7tzv4MfjnjvjTHFZRQIdfRwMm2exI8K8YEH26O2vhinNPVR7giZlHQgvm7KhnyYvol2Zhdi0b7Gw6KqvywvG0YRlCGHV9Z3EwfkkrYrc0PIdaCAtISy8nf7MQILVeZb8UpAVjbkp5nWuECIpug7dfuMTtKj3usDCsFyQw1rLicHcsdATdHe6jOSnsW6MSrM-EOUUqkZEnM5X6qXOwOO3WPMWtP1sx5Zmi6-QnNhfsYsjiEeOlybqhsYGuvpe2m3XQUspS62uGrKn-xKrs62bvh-bfAchHkx1iO9oN_3mh_HINe6EBUcUKIDnq7M5a5GBKJf-WOAAWfzjQT6TT1op4MCtsInv9x18L6rOE4U__Kv1qSEFUEXaASJFdDBVCvfL-6H9Yrgckora9SpNR8aS1Q4C1weLptWT0TGuiDZOqj2dksKl3RYDld0AhhlSEgQtjwz7EmEzvrGjG3yPudjJCNQjaCKkDzE7We1t2XEL_usFAeHyYC2zdXZA0tcmds7G8i5kGSnsWHhnuDI1SUqyxvaDtTHWfqhMoUqOA2vkHFXBocL4lTph5xFp-18jjcs8wRsrzmFAanahsw5aOPE6n4_9FM1LdfvRaLPiCmpq8AZcAkd6jD6DWb6j2JfC4gcZnb-ybnwl135g2yiHFsfjqCfIcNyBRIGRrd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره مسلح کردن معترضان ایرانی: در واقع کمی دشوار است. می‌دانید، نمی‌توان فقط سلاح‌ها را از آسمان رها کرد. واقعاً زیرساختی برای رساندن سلاح به قلب مردم ایران وجود ندارد.
🔴
یکی از چیزهایی که رئیس‌جمهور را بسیار ناراحت کرده بود، همه این معترضان بی‌گناهی بود که چند ماه پیش توسط کسانی که در قدرت بودند به قتل می‌رسیدند.
🔴
آن افراد اکنون رفته‌اند. اما خواهیم دید: آیا این رهبران جدید با مردم رفتار متفاوتی دارند؟ قطعاً امیدواریم چنین باشد.
🔴
و اگر چنین نباشد، وقتی رفتارشان را ببینیم، می‌توانیم بفهمیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/128867" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128866">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پیت هگست: حق عضویت سالانه ما در ناتو منوط به این خواهد بود که سایر کشورها به اهداف هزینه‌های دفاعی خود عمل کنند.
🔴
در جایی که سایر متحدان با فوریت هزینه نکنند، سهم ما از حق عضویت کاهش خواهد یافت.ناتو یک خیابان دو طرفه خواهد بود.
🔴
من امروز یک بررسی شش ماهه وزارت جنگ را اعلام می‌کنم که وضعیت نیروها و پایگاه‌های آمریکا در اروپا را بررسی خواهد کرد. تا شش ماه - می‌تواند کمتر باشد.بیایید آن را بررسی ناتو ۳.۰ بنامیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128866" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128865">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام اسرائیلی نزدیک به بنیامین نتانیاهو، نخست وزیر اسرائیل، گزارش داد: اسرائیل در حال انجام مذاکرات پیچیده‌ای با واشنگتن در مورد حضورش در جنوب لبنان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128865" target="_blank">📅 11:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128864">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06953ba6ec.mp4?token=bu4-Y9YhIU5Lzb6jk4p-ni7Es7_EIm0CjNI6xrB7-DUchH2csLVLreeZacHQ7_hjPQEHs2dgy_IPL5vc9GrjQ-Qt1S3MkOpnqGxbnQB-OHQeT8hzZb5m06VfQL3WuLbfDEDoplBIISGdSaYGgfJ4vZA15tYI5acaep4Np421H5fiQfY6oFKiOBolqkG4pHl7HvMBGJaIsCRMgsJLYfgBrOt32wPZurTHk3tUbGWlFead_8ltmf1CAXxlfCZnRaVYwOhGUo7PObz73QV0K03kG6WSowYgp5oiUke31Zqvv46t9lwsXNqlPpLtMtdqK6X5PAGZb1rKPngwhMk59SssZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06953ba6ec.mp4?token=bu4-Y9YhIU5Lzb6jk4p-ni7Es7_EIm0CjNI6xrB7-DUchH2csLVLreeZacHQ7_hjPQEHs2dgy_IPL5vc9GrjQ-Qt1S3MkOpnqGxbnQB-OHQeT8hzZb5m06VfQL3WuLbfDEDoplBIISGdSaYGgfJ4vZA15tYI5acaep4Np421H5fiQfY6oFKiOBolqkG4pHl7HvMBGJaIsCRMgsJLYfgBrOt32wPZurTHk3tUbGWlFead_8ltmf1CAXxlfCZnRaVYwOhGUo7PObz73QV0K03kG6WSowYgp5oiUke31Zqvv46t9lwsXNqlPpLtMtdqK6X5PAGZb1rKPngwhMk59SssZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست وزیر جنگ آمریکا: برای مدت طولانی، ناتو یک ببر کاغذی و یک خیابان یک طرفه بوده است.دیگر نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128864" target="_blank">📅 11:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128863">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3xihItxLpMiSfdCzqPRA3Or13zFrMhKej2Egw71n2nRcOWT98t1XOdwqiIeoWOU1-V2Bcz-ZxcxQAzo72_9kcLDXzflKbz82LHEWUUJWOSUIHDWsMdZh3Zx-F2lPhN1FuoKGcrpUw3RUJxtQA2Fp-YbAfStyeIhTMD-fAzvrfZ34CB-xqQ36qchnUUUczlqDjOM7jKiCi--6vLoF5mk8RwM3vSeRfn8wWOz3u61WVHol98CtAeGVu1azOPZlaEEDhmZM2OHmD4IeRMX0sfv4Jxx6oYWzExddjbcxWwUD61QS04LVVSlH8ql070tjkxKyKid3ohDsTDYx4rlAULk7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار ارشد آکسیوس:
ترامپ به توافقی با ایران رضایت داده که بسیار کمتر از چیزی است که در ابتدا امیدوار بود به آن دست یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128863" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMmRIxinDwYIg93rvnQP9Q7Hseo_4esM0oQ-0lU8nx2AvodWkq-jhMIv3O_tbH4UmkuYVyjvMA1NgI8Zf-Dp7aFdqQc_GeNywKxwE73kKsgnEow_Bl-sXht59LjKswkIsB6is8xv2aGofCrmOOxJUDgoL5piJOn062YVr361Ep5g9MLroXP4dXOvF59quwU6FqYQ2c4VpmtA4CGGEM2cWFpReZh2uGafjWFp8agNqV2AGbLMiqECIQE3j5gubDi2MgMxAKIPONT08fk6KWqVcdM0_irc8WanSttAGJUEeinVap_6prqU3k2s4SLvEADfG00x3sGkTTA9MLoGZNTiLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ اعلام کرد پروژه ساخت سالن جدید کاخ سفید با سرعت مطلوب در حال اجراست و برخلاف پروژه ساختمان فدرال رزرو، هم طبق زمان‌بندی و هم با هزینه‌ای کمتر از بودجه پیش می‌رود.
🔴
او همچنین گفت این پروژه شامل زیرساخت‌های امنیتی و نظامی مختلف از جمله یک «درون‌پورت» (محل استقرار و عملیات پهپادها) خواهد بود و آن را برای امنیت ملی آمریکا ضروری دانست.
ترامپ در ادامه از شکایت حقوقی مطرح‌شده علیه این پروژه انتقاد کرد و مدعی شد شاکی هیچ جایگاه قانونی برای طرح این پرونده ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128862" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
️سناتور جمهوری خواه بیل کسیدی در مورد تفاهم نامه ترامپ: ریگان در قبر در حال لرزیدن به خود است....این بدترین سیاست خارجه آمریکا در چندین دهه اخیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128861" target="_blank">📅 11:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128860">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf672333e.mp4?token=LHwioOpP2CaIQG1hfJFfImU0o2CUd_JDxwUfp2ccMO0ozxtnA0tSxkYFxxD598ZuMYcghVuRMcqpRj3iy-AexC3qPk1p3C5tpCH7MjHvSlm_7saz9MoCYAqXWmkAzEjgXeMLYWWP-thVmH0V5mohR6I8IAauYik-zpxrZjcy2W6Cn8YQbmjFj58mJk5mRWygEhPIX7uQ2b6zRbODmbceQkA3jmBclqoBtEU4zEXKLhSwgMx1CnvkzS7r0LgVK3ViYO-5jnaLUS8vecRDOmvrpQhiqtB4nqFY4SeFNTJJa_vJvpmGc78GjwxurFqkv-DT7QHJRmPIttsP_moK95LIsjCun46t-D2L2N7NuwbZ0pb3madJ6TSbj7zQ519zsrCTjZ0f7uNwWr-mMAV07YFy4y1LEIdJERvr9fGUEAg3LN1p9MPWVUh7wBYiTQajI-N27OS3tHeZ-qpBDnmB395qwKeIJ001_R7Pei5Ng_wyw_0FhbDGzFOb5eMn8vKU3aN4ULwjhu0CU6MlnV9LsNVXBXyqx4vPMjYg60NXXngPAMolCG4G_XeYdmz26bM_NBOsW-FafwpyR6u5SNQBQvZPI1ThP9WRuPR2Vmvw-wphuqNTdIWf7RbS6XMJwaUHU_klVndJ1zfWFDCSJpWa2xgVjP7_Q4ONea2iWs4Yi3-73bY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf672333e.mp4?token=LHwioOpP2CaIQG1hfJFfImU0o2CUd_JDxwUfp2ccMO0ozxtnA0tSxkYFxxD598ZuMYcghVuRMcqpRj3iy-AexC3qPk1p3C5tpCH7MjHvSlm_7saz9MoCYAqXWmkAzEjgXeMLYWWP-thVmH0V5mohR6I8IAauYik-zpxrZjcy2W6Cn8YQbmjFj58mJk5mRWygEhPIX7uQ2b6zRbODmbceQkA3jmBclqoBtEU4zEXKLhSwgMx1CnvkzS7r0LgVK3ViYO-5jnaLUS8vecRDOmvrpQhiqtB4nqFY4SeFNTJJa_vJvpmGc78GjwxurFqkv-DT7QHJRmPIttsP_moK95LIsjCun46t-D2L2N7NuwbZ0pb3madJ6TSbj7zQ519zsrCTjZ0f7uNwWr-mMAV07YFy4y1LEIdJERvr9fGUEAg3LN1p9MPWVUh7wBYiTQajI-N27OS3tHeZ-qpBDnmB395qwKeIJ001_R7Pei5Ng_wyw_0FhbDGzFOb5eMn8vKU3aN4ULwjhu0CU6MlnV9LsNVXBXyqx4vPMjYg60NXXngPAMolCG4G_XeYdmz26bM_NBOsW-FafwpyR6u5SNQBQvZPI1ThP9WRuPR2Vmvw-wphuqNTdIWf7RbS6XMJwaUHU_klVndJ1zfWFDCSJpWa2xgVjP7_Q4ONea2iWs4Yi3-73bY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه سی‌ان‌بی‌سی: فدرال رزرو آمریکا ارسال محموله های ماهانه ۱ تا ۲ میلیارد دلاری نقد به بغداد را تا تشکیل دولت جدید و قطع دسترسی گروه‌ های تحت تحریم به ارز متوقف کرده است.
🔴
بر اساس سازوکار مالی پس از ۲۰۰۳، درآمدهای نفتی عراق مستقیماً به حسابی در نیویورک واریز می‌شود و دولت آمریکا کنترل توزیع نقدینگی آن را در دست دارد.
🔴
با توجه به اینکه نفت ۹۰ درصد بودجه عراق را تأمین می‌کند، این تعلیق بازار ارز را با بحران مواجه کرده و پرداخت حقوق ۷ میلیون کارمند و بازنشسته عراقی را در معرض خطر جدی قرار می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128860" target="_blank">📅 11:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128859">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8UqP3s-zH6I3b05PBV9DhHqb6kPHURWaivPGFUxt7ncrhRZUk2a05A0vurDUG0FYhwj_xVChG1DBqeKBn6G_IeYZ7-uFK066iDIFIAMkM817mqckXoBVZxD0hmIyNi20i4OtE4aA5Ev-iLil9aNj95raNiEuQR6zzFljyO1i0cFAcUyY9FlLFkNwZPXnfCAEvYeOxX9vd0QNTYr-3jJThxo92lqAjOo26DyzaEDZUQ50VBUu93YdM7kiS0eeZGoge7UIKWwqHrF_c9x8ly4i3TfR83nm3M0Qg03qG-NyyKTCrOal0bjlLbesFm077T7funIj49AJ_pzOYsIg5MBgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی عضو تیم مذاکره کننده ایرانی: استاد خوش‌چشم درست می‌گوید؛ ترامپ کوتاه آمد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128859" target="_blank">📅 11:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128858">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وال‌استریت ژورنال: به نظر می‌رسد رابطه ترامپ و نتانیاهو به طور فزاینده‌ای تیره شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128858" target="_blank">📅 11:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128857">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
پیام حسن روحانی پس از امضای یادداشت تفاهم ایران و آمریکا: باید از دستاورد تفاهم اولیه، حراست کرد
🔴
باید نسبت به توطئه و عهدشکنی دشمن هوشیار بود
🔴
امروز هر ایرانی در هر گوشه دنیا، به ایرانی بودن خود می‌بالد
🔴
رهبری نظام با صلابت و درایت و حکمت، انسجام ملت و نظام را مدیریت نمود
🔴
نیروهای مسلح جان برکف حسرت پیروزی نظامی را بر دل دشمنان گذاشتند
🔴
دولت خدمتگزار لحظه‌ای میدان خدمت به مردم را ترک نکرد
🔴
همسایگان ما می‌توانند با مشارکت و تضمین این توافق، از ثمرات امنیت و توسعه مشترک منطقه بهره‌مند شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/128857" target="_blank">📅 11:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128856">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
گروسی: در مذاکرات سوئیس شرکت خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128856" target="_blank">📅 11:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128855">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
جی‌دی ونس درباره اسرائیل: اسرائیل حق دفاع از خود را دارد. هیچ‌کس نمی‌تواند به دولت دیگری بگوید که اجازه ندارد از مردم خود دفاع کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128855" target="_blank">📅 11:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128854">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری / نتانیاهو: اسرائیل به بند لبنان در توافق ایران و آمریکا پایبند نیست!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128854" target="_blank">📅 11:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128853">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری / گزارشات از پیشروی ارتش اسرائیل به سمت ورودی علی الطاهر در لبنان
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128853" target="_blank">📅 11:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128852">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e98533ee.mp4?token=tQhvgnvb899T_HP9AZyz0_QpCEHTOLdY0MoJ94fnf7aB4-kYs7jU24Vbr_BmYE-5wBiZna2-qSiwMjk1RGK2i-AxHp5LyIX9YAx3vOXNAvQxY2At_YFehuRcd2nTceUyiwbgDW2vrBX7I0zWnp8m9dxqwqClR4kRyUHZf4BmrU8KsBtsuQHzD4zof4BuqFj13uAP99IzSacecO0lkOtH66Xr1oy1dU7-REh3hv0Nad250WkFFcI6QZkvB4uPKwpbWRfXKlVqfor9mziq_vrgzYmZbIRl8D1HrkS_a1ZClA72VzTX4c4ywYt-YnzCyP6c0vHGmdR5vtZg3jrT1u_5TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e98533ee.mp4?token=tQhvgnvb899T_HP9AZyz0_QpCEHTOLdY0MoJ94fnf7aB4-kYs7jU24Vbr_BmYE-5wBiZna2-qSiwMjk1RGK2i-AxHp5LyIX9YAx3vOXNAvQxY2At_YFehuRcd2nTceUyiwbgDW2vrBX7I0zWnp8m9dxqwqClR4kRyUHZf4BmrU8KsBtsuQHzD4zof4BuqFj13uAP99IzSacecO0lkOtH66Xr1oy1dU7-REh3hv0Nad250WkFFcI6QZkvB4uPKwpbWRfXKlVqfor9mziq_vrgzYmZbIRl8D1HrkS_a1ZClA72VzTX4c4ywYt-YnzCyP6c0vHGmdR5vtZg3jrT1u_5TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی آقازاده‌ها میفهمن بعد توافق قراره پول بیاد به کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128852" target="_blank">📅 11:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128851">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری / گزارشات از پیشروی ارتش اسرائیل به سمت ورودی علی الطاهر در لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/128851" target="_blank">📅 10:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128850">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
آکسیوس: رسانه‌های نزدیک به نتانیاهو به دلیل توافق با ایران، حمله به دولت ترامپ را آغاز کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128850" target="_blank">📅 10:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128849">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ناتو: توافق ایران گامی مثبت به سوی ثبات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128849" target="_blank">📅 10:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128848">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سازمان هواپیمایی: یک میلیون بلیت پرواز در ایام جنگ لغو شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/128848" target="_blank">📅 10:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128847">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcba069447.mp4?token=R9yUBO9WhaRq0ldPilD6N5B2zdMqJbJ4CNq35gxjtx_z6f07hQryqt4X45jAzvYIspJCnzSJEydf4DmACjLVprBQkByLMdrihYc0zweobm8G40KGeoogpCIp-2S_JHimzR39AAi4girdiVvTLLSBaLH9tMnyf5v0yWLwD9t8RLemgSls97owfv4rhzlb39zqfvvQdAUNUXmdi3XNJcshPxhRp7zfF7qgrb4lQ8nXhxgqKVhJswGPyyoV6Ixx0EyDOP90LAtWZXAjZNjE1vtkN5DA6R03hgHyUgXQ8c9rwd_LnqMVKHihuXYZcx-rdVoK7r3shUTqv7FAb-sj7lz7oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcba069447.mp4?token=R9yUBO9WhaRq0ldPilD6N5B2zdMqJbJ4CNq35gxjtx_z6f07hQryqt4X45jAzvYIspJCnzSJEydf4DmACjLVprBQkByLMdrihYc0zweobm8G40KGeoogpCIp-2S_JHimzR39AAi4girdiVvTLLSBaLH9tMnyf5v0yWLwD9t8RLemgSls97owfv4rhzlb39zqfvvQdAUNUXmdi3XNJcshPxhRp7zfF7qgrb4lQ8nXhxgqKVhJswGPyyoV6Ixx0EyDOP90LAtWZXAjZNjE1vtkN5DA6R03hgHyUgXQ8c9rwd_LnqMVKHihuXYZcx-rdVoK7r3shUTqv7FAb-sj7lz7oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ بعد از امضای توافقنامه با انگشت اشاره می کنه و میگه: نفت پایین، بورس بالا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/128847" target="_blank">📅 10:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128846">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر دفاع بلژیک: ما یک کشتی مین‌روب داریم که آماده است به محض فراهم شدن شرایط، در عملیات پاکسازی مین در تنگه هرمز شرکت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128846" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128845">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
بقایی: اسقاط تحریم نفتی ایران از امروز آغاز می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128845" target="_blank">📅 10:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128844">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
آکسیوس: رسانه‌های نزدیک به نتانیاهو به دلیل توافق با ایران، حمله به دولت ترامپ را آغاز کردند
🔴
مجری شبکه ۱۴ اسرائیل: ویتکاف و کوشنر یهودستیز هستند و اسرائیل را فروخته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128844" target="_blank">📅 10:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128843">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
اسرائیل به حومهٔ شهرک کفرتبنیت از توابع النطبیه در جنوب لبنان حملهٔ پهپادی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128843" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128841">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29f737682a.mp4?token=TxjjrcmTZ5J0bbic1-xIwgGo_ENLrqlsyOdceBgy_F2me_DiTljYAyoP5rT31uCTQFgqoDNyeGEVUQYyTO1LYi9rEvS7o4Ev-GFXxXuS_hw8j-sZC11-avYUBPTMrG4RvNyW_V9BFVprs2ANIEW0qE7Z_FWqWqTtD-FblxlG4CkH2LVCv9i0MUp8hx-TcwE96swYyji6FetpU8oVuwUXGlTLgDDl9mQE7MEkHMQ7LNqsuuHiIHaV-mvK0XofmGIpQgJwDquIVmuunhPGOwfDyMT1m7-mQ0MX_uqgRtpG65pHzSYXlP-TMubKR0yogCHpPUEXaiSVWAoXIZcskwMJYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29f737682a.mp4?token=TxjjrcmTZ5J0bbic1-xIwgGo_ENLrqlsyOdceBgy_F2me_DiTljYAyoP5rT31uCTQFgqoDNyeGEVUQYyTO1LYi9rEvS7o4Ev-GFXxXuS_hw8j-sZC11-avYUBPTMrG4RvNyW_V9BFVprs2ANIEW0qE7Z_FWqWqTtD-FblxlG4CkH2LVCv9i0MUp8hx-TcwE96swYyji6FetpU8oVuwUXGlTLgDDl9mQE7MEkHMQ7LNqsuuHiIHaV-mvK0XofmGIpQgJwDquIVmuunhPGOwfDyMT1m7-mQ0MX_uqgRtpG65pHzSYXlP-TMubKR0yogCHpPUEXaiSVWAoXIZcskwMJYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسکو در دود و آتش
🔴
حمله پهپادی وسیع اوکراین به پالایشگاه مسکو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/128841" target="_blank">📅 10:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128840">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnsDwYWhKTDaG2q4kr__azc7u9bA9FzaPd6b9aKIf7Clq9ghRMbtHhkbVu0Q5wg_iXnTQLfOGyqMwssf19y0kM2Tb9iSN8rKr6QJA5tqBZvfWCEhtMTP6vRZKMRIYtgU1j9ANpuvjI70bMKNEayUrTHWNg1pqaVLf94wCCbLApTHb61svMARpvosP4XFLmy8G6zwo8IyfEaaPEI16fdoWet5Nk2EA46g6SB0Jv-6QaZud0b7LngISuOraC3TCXIxvvdzLJPrDVG2Pp_DtidcFHqqPmD804rzs3xMUJCDHmcj5HaOO8bNSmEYi075a529IeFPkVUY-wTskUMDGsJ4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ در حال از دست دادن تندروهایی است که زمانی از جنگ ایران دفاع می‌کردند
🔴
بسیاری از محافظه‌کارانی که از رئیس جمهور حمایت می‌کردند، نگرانند که توافق صلح به اندازه کافی برای بازدارندگی ایران کافی نباشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128840" target="_blank">📅 10:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128839">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
دولت سوئیس اعلام کرد که روز جمعه نشستی با حضور نمایندگان آمریکا، ایران، پاکستان، قطر و دیگر کشورهای مرتبط برگزار خواهد شد تا مذاکرات مقدماتی انجام شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/128839" target="_blank">📅 09:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128838">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVEG8YWzDf-iKcYko94aFOGJoKAUwqdbff0xr3-iO5QDbLbKSB7YujbtSA2t8kY8VXtyVSxbl450sCivdzXG5L6pjdxBMCZt3-K8a3_9uINb-rX8iPRMl8GN7Pm20WP_on4VMwRIbM73E2df78AllFz--BlRf51IO6MqUS8pvCygSXPmUXFkN9N5sliPWkuZ54NNBHjzo6-tnt7pefL2H4MlSUOFo27m9LlUjJo-dRQPeAZAqBtXJKImSdqyAy0CPQCUYNIs-Rdh8dNIkVpnCMXpUGR3kTSl29AGf5Py8A-KGCqQ13BRTjOAXs-kgjPt5pQnOE96K7QW9KQJqQdp4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور بلومنتال: سنا قطعا توافق با ایران را تصویب نمی‌کند
🔴
محکومیت دو حزبی برای یک توافق ننگین عجیب نیست که شبیه «تسلیم بی‌قید و شرط» است، نه توسط ایران، آنطور که ترامپ خواسته بود، بلکه توسط آمریکا.
🔴
بیش از ۳۰۰ میلیارد دلار ثروت بادآورده، لغو تحریم‌ها، فروش نامحدود نفت، عدم بازرسی یا تأیید کامل. همه اینها به خاطر وعده‌های مبهم و غیرقابل اجرا در مورد تسلیحات هسته‌ای است که ادعای ایران برای پیروزی در برابر شیطان بزرگ را تقویت می‌کند.
🔴
هر چیزی شبیه به این توافق به محض ورود به سنا از بین خواهد رفت. برای اینکه اثر اجرایی داشته باشد، باید در اینجا تصویب شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/128838" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128837">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCo9ACtRy0aAHQjbE8rnmoAThQuGU0YJpe5djTIGyuL-RxeWZ1KpovffbBwrqtopBWE1JxabHqZKfjKGIgx__kCpNnBM0ArYjRGX9mU3VuhgxyS5F-VxL94rLx5qnxNHMaRW8aveqVj6Za-V9Ukq-E5syS15D1JMSsl-LwzJs8abvcGSsjz9spYrvq_Q-e4YxQBF6TqKGxTcAfYen_pIKVfIHO4lOYbQXVkPsPoT1bz_3gY9JZTFRUnjXYgo8twDZjRZiFGsTEoI5Uv68IZkF4z-oIfpySg2d5NgIYADIlHHpdQurSt8l5wUoH3G_GXQ9tySUoPzaPWTj2ZbrdlfoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری متفاوت از ترامپ و مکرون در ورسای
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/128837" target="_blank">📅 09:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128836">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
روزنامه خراسان: مراقب باشید در مذاکرات ژنو، ترامپ یا ونس با مقامات ایرانی عکس یادگاری نگیرن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/128836" target="_blank">📅 09:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128835">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
فاکس نیوز به نقل از یک مقام کاخ سفید:
امضای رسمی که قرار بود در ژنو انجام شود، پس از امضا در ورسای لغو شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/128835" target="_blank">📅 09:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128834">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
تاکر کارلسون: توافق ایران به امپراطوری آمریکا پایان داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/128834" target="_blank">📅 09:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128833">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ارتش اسرائیل: کشته شدن یک سرباز اسرائیلی در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/128833" target="_blank">📅 09:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128832">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
الجزیره: موجی از خشم سیاسی واشنگتن را بر سر توافق با ایران فرا گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/128832" target="_blank">📅 09:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128831">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مذاکرات جمعه ایران و آمریکا در سوئیس قطعی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/128831" target="_blank">📅 09:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128830">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
نفت خام برنت ۷۸ دلار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/128830" target="_blank">📅 09:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128829">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کانال ۱۲ عبری: افزایش نارضایتی‌ها از نتانیاهو در دولت ترامپ
🔴
برخی از اعضای کاخ سفید می‌پرسند آیا نتانیاهو خواستار طولانی‌تر شدن جنگ با ایران بوده تا موقعیت سیاسی خود را تقویت کند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/128829" target="_blank">📅 09:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128828">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ :  در گفت‌وگو با وال‌استریت ژورنال: بنیامین نتانیاهو فردی فوق‌العاده است، اما گاهی بیش از اندازه شتاب‌زده عمل می‌کند.
🔴
در برخی جنبه‌های جنگ، نتانیاهو اهداف متفاوتی را دنبال می‌کرد و اسرائیل به ایران نزدیک‌تر است و به همین دلیل در برخی ابعاد این جنگ، اهداف و ملاحظات متفاوتی داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/128828" target="_blank">📅 08:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128827">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ: ممکن است رسیدن به توافق نهایی با ایران بیشتر از ۶۰ روز طول بکشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/128827" target="_blank">📅 08:54 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
