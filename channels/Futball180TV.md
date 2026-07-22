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
<img src="https://cdn5.telesco.pe/file/YDgGIKeUES_mT1P4WbRXqIWyVu2jye9MQxJXLTgqJkjohUcaDUc4z1Bghr96k_6trDA9IWW6tq4nYtIy2_0s7579sc4j0aI1vds7jbHKg0AM1eEtEGZKHdTsgZk6aUSSafK6pJKtiA76qG0wSP3NOF8nFiWSo1gCUDFU5ImKjpiZPVcAC8UQGjnPEy2OEReTvd6wZWXvXJerl7sTpqP-1jwHXjgENYE_8fao6po0pzRneDXkdxwofxVHfCskWG9fDgbd165C7fxLXXoe_RVVzlfsOQCaHrBG8kiXGVYp-EMY1mKcC0w46on4BrcjjCMkXmTtGPNkTHgoobanHdzhLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 544K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 11:22:12</div>
<hr>

<div class="tg-post" id="msg-101538">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovxvhk8mIgsyqcCjDLmAjwJj_1-nWdK-5RT5PcW9vGEejH1GC_-cjxDM-JT3zaJxgtbTMr6CD0W5Dsp4Kg7vEy4fjCB6grPnFGZuLfSv0E83AU2RFs2v5YCbrCN9V92ph7GXyjgUvXc1ESwruZ9HUWDCaYWZ8IQbEblA8sC5gDJbdirhxUNVYfgQTWx7JbufdLzAVzJIEF3l3z4iVlS9R-mrP0k1lpsAu7Jyt5ZW9SrfoSy-pagUnbq0QclepUDPh07844gfj5M8tcwx2bDsYDG7Yo7-JMqhYIq7i92Z3B0YF4zot4i-N9h8cR_Q08cKqAIrLn5o4XQI-oOsAeJx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حمایت یحیی گل‌محمدی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 456 · <a href="https://t.me/Futball180TV/101538" target="_blank">📅 11:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101536">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330d45af26.mp4?token=mjzm0YVkWQMM_lz9FWMn0eTxdyIwNg2XcsBbYzJXC0G_Nq3wm7q3vHPeaaq2OECsJwqfbuUZX7PMuFqJeJzjTNjLIL5KVV484ZPOuslctsAvkid3wF5ODjQy9fbbNu2IB0WqkdF3j6FfZ4UMziO9MvevlxryvtIU3RBZKPZWvkmzz0DB5oh8FODDWpB-o6ag3gMG74Gl1OMI3iAQwYqTzcYejR4NrgnEatp4sr9lyFDvonN7tPh_uzDSKOk3ZEhKXzdy2HVGxvirjyOc89F6qII0ceGfdoqaKh4_2MME9lshJXtrsuZ1DHYuR8cUBTvBRedYXgh4PEYOHXCTBYUDMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330d45af26.mp4?token=mjzm0YVkWQMM_lz9FWMn0eTxdyIwNg2XcsBbYzJXC0G_Nq3wm7q3vHPeaaq2OECsJwqfbuUZX7PMuFqJeJzjTNjLIL5KVV484ZPOuslctsAvkid3wF5ODjQy9fbbNu2IB0WqkdF3j6FfZ4UMziO9MvevlxryvtIU3RBZKPZWvkmzz0DB5oh8FODDWpB-o6ag3gMG74Gl1OMI3iAQwYqTzcYejR4NrgnEatp4sr9lyFDvonN7tPh_uzDSKOk3ZEhKXzdy2HVGxvirjyOc89F6qII0ceGfdoqaKh4_2MME9lshJXtrsuZ1DHYuR8cUBTvBRedYXgh4PEYOHXCTBYUDMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تمامی قهرمانان جام‌جهانی در یک ویدیو جالب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/101536" target="_blank">📅 11:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101535">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=NMHbetrcKCoi9EAla8litVSh3F-vaLZi1mPW4SbBL01KE7kS7SxjXJdxddXrQlXcbJWyLXgyEkEr59yv2mG03-6Nspd0azaKFsrsIwL1aV_gsOdWL43oQ-jftcHKP8k0IBO1OiyFNXT_nkpH7m9ntdnsfH7t4kwwhzk7qtk-EDd2Fs3HNx4smdgWUoMxkzbkA9LgBMnyahFDDNo5hXdGqURGipQf7I3SwoKKtKJLya_ILrd1798vvnRHEuReIg1-qomLHvLI_lhWOp2runLybmjbGOCkwtrcSGpCEZqnxm3Tbv46hhuQzNN7cCsdodI2o9TAr1DqUEEhJffMWizAQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=NMHbetrcKCoi9EAla8litVSh3F-vaLZi1mPW4SbBL01KE7kS7SxjXJdxddXrQlXcbJWyLXgyEkEr59yv2mG03-6Nspd0azaKFsrsIwL1aV_gsOdWL43oQ-jftcHKP8k0IBO1OiyFNXT_nkpH7m9ntdnsfH7t4kwwhzk7qtk-EDd2Fs3HNx4smdgWUoMxkzbkA9LgBMnyahFDDNo5hXdGqURGipQf7I3SwoKKtKJLya_ILrd1798vvnRHEuReIg1-qomLHvLI_lhWOp2runLybmjbGOCkwtrcSGpCEZqnxm3Tbv46hhuQzNN7cCsdodI2o9TAr1DqUEEhJffMWizAQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی پول نظرتو عوض می‌کنه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/101535" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101533">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=XfC-U8aJ0d2lc_VFjAY4wSS7-T8lQcUmaLUBq3mpm2QnQ0rHpYV3kwFYSwG9Yqh6RAs-d9x5-6F7bwASp5C8R_Mx86MCK2FUb5ybPNOgU2LiY2_O2hQmIcdt0ZVqMbJD3L5FB50unpUhdt0UQmdv3eJy9J1V-fkuL0IUFF1iTy6uWkWBCsH9EfJpc3LrcWXO82KXal0JEgRSkb-1PCC5tS8b41NLWhLxmm7cqpRwI3w4Xb9B1ML7WmBiGkejOl7Dj0His3pGNznzD0q0yiz9pCgfEYLao2U8L5KmV2n6qb4YD2pqgfwkrFTOlpuplrOUzJX9cljjH969pjx0sFusZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=XfC-U8aJ0d2lc_VFjAY4wSS7-T8lQcUmaLUBq3mpm2QnQ0rHpYV3kwFYSwG9Yqh6RAs-d9x5-6F7bwASp5C8R_Mx86MCK2FUb5ybPNOgU2LiY2_O2hQmIcdt0ZVqMbJD3L5FB50unpUhdt0UQmdv3eJy9J1V-fkuL0IUFF1iTy6uWkWBCsH9EfJpc3LrcWXO82KXal0JEgRSkb-1PCC5tS8b41NLWhLxmm7cqpRwI3w4Xb9B1ML7WmBiGkejOl7Dj0His3pGNznzD0q0yiz9pCgfEYLao2U8L5KmV2n6qb4YD2pqgfwkrFTOlpuplrOUzJX9cljjH969pjx0sFusZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یه سری ویدیو قدیمی از قبل آشنایی یامال با اینس گارسیا دوست دختر فعلیش داره پخش میشه که توش اینس وقتی یامال با نیکی نیکول بود تو لایو گفته:
‼️
🔻
اگه یامال یه میلیونر یا یک فوتبالیست نبود، نیکی نیکول حتی دو بار به اون نگاه نمیکرد!
﻿
‼️
🔻
همچنین ازش پرسیدن: «لمینه یامال یا امباپه؟»... گفت: «بلینگهام»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/Futball180TV/101533" target="_blank">📅 10:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101532">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">😂
😂
😂
تفریحات جدید اسپید بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/Futball180TV/101532" target="_blank">📅 10:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101531">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=e4v4-hdaBfoBDmgAiCht7mImT2WuFJFEwgtZC_TKl68I_TvPSoYclVyOHWFYqN06RzxHDnga-A6qe01Yeh2ktW9iR92mQZ0G3iPopfmiZCkQLP7HIDaxb_Stiv4PT4Jpuy5oYqBBy3we1HgMFmzzyyvJV1RqCrjnsNrYYrICmSa78DLx6s-RsKZkWtWiS4EvdWen-Oj4wLVmb44H3TNwBOUO_VnAQAKkqP27-x8Zn8Btd0kjrnqb-gdslNUopAp3ywpDahh78RSGNjujX9PjtmRDBI3MES_BhE84cvjm_MLHGXaNVRb0AsVLvC2iBiLFTa7WVX8h1XW5I9VkvzDXXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=e4v4-hdaBfoBDmgAiCht7mImT2WuFJFEwgtZC_TKl68I_TvPSoYclVyOHWFYqN06RzxHDnga-A6qe01Yeh2ktW9iR92mQZ0G3iPopfmiZCkQLP7HIDaxb_Stiv4PT4Jpuy5oYqBBy3we1HgMFmzzyyvJV1RqCrjnsNrYYrICmSa78DLx6s-RsKZkWtWiS4EvdWen-Oj4wLVmb44H3TNwBOUO_VnAQAKkqP27-x8Zn8Btd0kjrnqb-gdslNUopAp3ywpDahh78RSGNjujX9PjtmRDBI3MES_BhE84cvjm_MLHGXaNVRb0AsVLvC2iBiLFTa7WVX8h1XW5I9VkvzDXXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یادی‌کنیم از سوال خبرنگار صداوسیما از لیونل‌مسی که بنده‌خدا اصلا ایران رو‌ نمیشناخت :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/Futball180TV/101531" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101530">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sukY0xtcSdDJMI0rMPE9mGB9MN3DcVd_dkQi4tjZlJEbW210JXg5bBozPTiwzSYV97lFiezuVLrtcO3UQq_FlR-AgFI9-2_WN8q3sD6uHJTubz4tYrA1ln-IlKovfv9DmQqDNXIiCCvgtzapKOOcKCAo4uU1bQUh0eUAt4VdVZB67tBPABapDSdRB0ON1jcgZqKsGhH9XHTVNBzwaUS8ViC5v1Dc1KQDQmJssisGCzOwwM1Dx896X_PVUWBbwUUObP_-sb8p0r-4aHjsArQ2dQHvr_sQHPJakSkLKnj3RsOuLX4cYP4fP-ltaCtBV8gX60z-t6hICsNBb59ciEPn3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📅
🏆
شش سال پیش، در همچین روزی لیورپول برای اولین بار پس از 30 سال قهرمان لیگ برتر انگلیس شد.
🎙
یورگن کلوپ: "این دستاورد بسیار فراتر از آن چیزی است که من تصور می‌کردم باشد."
🎙
جوردن هندرسون: "من بسیار خوشحالم که این عنوان را برای استیون (جرارد) به دست آوردم."
🎙
اندی رابرتسون: "ما 13 هفته منتظر ماندیم، اما هواداران ما 30 سال صبر کردند. این مدت کوتاهی در مقایسه با زمانی است که آن‌ها تحمل کردند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/Futball180TV/101530" target="_blank">📅 09:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101529">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLDUadm019G0v8bPTwmKxi9HD-5z_XSDKxCAIlXq-MDRA2aeSwBHM47TEqmWd3IvHBtdiMC5vEfdJFSg19XBfb4FSDLwVc1mHQel_V0hhLYswI0Og28VpFiu8uSgqrP1naXYRPX00oXh3Z3hotVzYKTCLph_uKB9_duL1Q_DfZeqAmdjLnaqTMZCjjxoUWOm__VhJPnQz6bL-PzFXNMvOJRVNpjYVMHmGpe5PiFa0mNJuuKYh70UcorIFmRhhh0YAqs4n5Sgfbe1vKMw_-iqe2vjOuzDwcpSsSUYbTof-UJWbW5uCvCViIqqpBRGqrM_FRjfGfjReVDza3-YSZ5rnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🇧🇪
🔻
مارک فان بومل به عنوان سرمربی تیم ملی بلژیک انتخاب شد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/101529" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101528">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=gBTpHTlMJdqEGs8sgtSSUACShtakjkmQac-ClUfj16zBy0Odi7YGinVkraasYBSaBCV7cizfjBtK42hc8Vn9G-0CgZh7bPNJEF0o-kVJa1uqR9s9VyPK8dDGo9fxIEW8Bzy6G5fsp-rDa_oqpea-rhZJu4daj6ig3ktCUfFcqPskQNGXHOt-g7RDe789v1wX_kXXZxbSU3m9qSocslpGsSD3YEYvBg5D__RrWJskQCCv-s3ZpYXlecdFn2pvb7-34FsDzrE0hNQCDxZ7cjTdGvLgOZt2gVYOVXCSlVPzxAzeSEDS0KaJn1U3acmXG6s_n7sss2_9llxTNyHVudfTrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=gBTpHTlMJdqEGs8sgtSSUACShtakjkmQac-ClUfj16zBy0Odi7YGinVkraasYBSaBCV7cizfjBtK42hc8Vn9G-0CgZh7bPNJEF0o-kVJa1uqR9s9VyPK8dDGo9fxIEW8Bzy6G5fsp-rDa_oqpea-rhZJu4daj6ig3ktCUfFcqPskQNGXHOt-g7RDe789v1wX_kXXZxbSU3m9qSocslpGsSD3YEYvBg5D__RrWJskQCCv-s3ZpYXlecdFn2pvb7-34FsDzrE0hNQCDxZ7cjTdGvLgOZt2gVYOVXCSlVPzxAzeSEDS0KaJn1U3acmXG6s_n7sss2_9llxTNyHVudfTrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
فینال‌باز واقعی آرژانتین در کنار لیونل‌مسی فقط یکی بود اونم دیماریا که واقعا نبودش امسال حس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/101528" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101527">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=siybEc3rtSTdlw39L0hC2iL_dvJlnQLwOp-C6uRC6C0M8dlpv67bYPoaOm14f-zin8HfBKBs7g0gM5YKSpTbOuFCmvAtLI-xgyeZmLS2j-dU0VJoEIn33zuMJTDtk8jezvy1LCVYZEr2Hc_g2nA6TQmcy30vsHn7QjjID18SXWHHKH86wMKHv4Ayb5U72tXtc53sy62kmmCxwWUG5cfrmeHKtPxQFoCsVFyUyi6bIga3_6OTm6XqcPWgrpsC_Skdo5SBuk4ZKdcVOGs3__6HuAll-sT3D25kRQmQZED4pSBJWfytDR7wc0qZPxxsL1EAEEvnyr5cLnEtInRP4NAsQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=siybEc3rtSTdlw39L0hC2iL_dvJlnQLwOp-C6uRC6C0M8dlpv67bYPoaOm14f-zin8HfBKBs7g0gM5YKSpTbOuFCmvAtLI-xgyeZmLS2j-dU0VJoEIn33zuMJTDtk8jezvy1LCVYZEr2Hc_g2nA6TQmcy30vsHn7QjjID18SXWHHKH86wMKHv4Ayb5U72tXtc53sy62kmmCxwWUG5cfrmeHKtPxQFoCsVFyUyi6bIga3_6OTm6XqcPWgrpsC_Skdo5SBuk4ZKdcVOGs3__6HuAll-sT3D25kRQmQZED4pSBJWfytDR7wc0qZPxxsL1EAEEvnyr5cLnEtInRP4NAsQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😔
پیام استاد وحید قلیچ به دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/101527" target="_blank">📅 09:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101526">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMiEgM-d7vxL0Vz5mnzRELU7AQ5lLDLtGTz27JeMjzJoUdj0og6vxg_uwtqUxLN3cbHu80RNCGuJzAdn2mdT6dZutJyoCLGETy92W5DcLTaAYOEO8xNI0URoTQ3nb7JnB97wfNZWtu9nbDG0IJ6V9gjwKcRd9wfR5MvZsz5NoqTXF6-nkDknX4bMfORWC5iMvV2pJV_PSZBOLq1sT2GWd20CNjz-WeP-Y-TFXDNeS5P773kAchg7qdPKE67beLA4_-gRlkmRbosk0o_rf-E91-qvgxOVAoC5NEvmXbMAphow4_taMMi9O7o7rmlnmD9X2yoGoMiNpC1tFCMXuPqZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مارک کلینمن:
🔻
جف بزوس، بنیانگذار آمازون و چهارمین فرد ثروتمند جهان، برای پیوستن به ائتلافی به رهبری آمیت بهاتیا دعوت شده است؛ این ائتلاف در حال مذاکره برای خرید بخشی از باشگاه لیورپول است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/101526" target="_blank">📅 09:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101525">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=EZoQg13Mk29sHWEmIlF8SISgWXs14LfAdZIOYRLfzJwFXZ4VNs3-yG-aJaQqCMZNB5oQaUO90JYX7mKmjsegxJ-S8kzKiW1OYaRFhuJjwJdYwxyJiWuSje6ZfaIuzC1kqByWR_8bA4nu-NLgasHnlcuJ_DmGHWhNoZnBCYe04RmXp9gMazGuAE2RA9MChwHWPSDN2vLgLIGNjhy99Qo4IIWb3I_IelWMEt96o21atPVlymRB-ckQSmJppMRMxtSaXhzcsyHvJ6Ey_OaMBz-A3WS3N8bZHEM6De0gL10hJ-RwSIIfY4Qi8sVHM_ITYG-IZaB6lI11yfGS7QM-Kkl5qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=EZoQg13Mk29sHWEmIlF8SISgWXs14LfAdZIOYRLfzJwFXZ4VNs3-yG-aJaQqCMZNB5oQaUO90JYX7mKmjsegxJ-S8kzKiW1OYaRFhuJjwJdYwxyJiWuSje6ZfaIuzC1kqByWR_8bA4nu-NLgasHnlcuJ_DmGHWhNoZnBCYe04RmXp9gMazGuAE2RA9MChwHWPSDN2vLgLIGNjhy99Qo4IIWb3I_IelWMEt96o21atPVlymRB-ckQSmJppMRMxtSaXhzcsyHvJ6Ey_OaMBz-A3WS3N8bZHEM6De0gL10hJ-RwSIIfY4Qi8sVHM_ITYG-IZaB6lI11yfGS7QM-Kkl5qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
روایت امیر قلعه‌نویی از دیدار با یک آیت‌الله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/101525" target="_blank">📅 09:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101524">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-vkBnVhWthaXyJqWTwvCxDUEhi3IxoVFeNUhfc1b2duF1HtkDeMi_dYBH_uSAiqTCD6My_HwI4zYTuDvaSBTdoVaA-3YfHwIDv1JOcKOhm49I5dd7tA8JxbU937oCTr3B5DOmaWEPx_ZYA-B0t-KY9MIpU742yPW3fksoa1GBuQSJP_FMH3Dj7rxhwXXpaC-YpuB8LfPrCURNHVRNeyv2dqgV95WMYSRPKBSYKgsHewwLad6JfH93zcgoIrfKi-oB9QxNxiISFQxBg_0Iya9xEklcfhHqxBpEIAK32gVfqcURP54aSc8uNtc1_3vkzhx_VVamxbqmS6FZGGU46MCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش هم داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/101524" target="_blank">📅 08:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101523">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obim39LVcCFd3Nr2BfyRK6W-Inhbbryl_67rMFSXm8EwqUD-l3a52i213tIFU-sMnlL7i67DPtryPvXrzeSoOsabe6P8yQZhZ9aUg5o-JdNSQ8DXNdKu0pxcPxH5p8bQJKCrYwZpCcWRZmLUmo3tUSRmD6-9j37JgZ1ybmLwUvaa9L0UGFQpNjeT9qa_wHcrJVjIO2P2zyWKGgAME-_VCm3nDK13aVVFj8qxmehXntj5K1ESUWavrzCOf1Ftm812BMAOqjEKKdtxPottOREXXT9qq3C_maOaQ7PQXL_Ucr9rk-F_QuyAWqoMYMAu-WIuQODkkmYoS3ZI6TzLbbDsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
👏
دیگه قرار نیست بعد دیدنش بفهمیم که 4 سال از زندگی گذشته و اوچوای دوست داشتنی بالاخره از فوتبال خداحافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101523" target="_blank">📅 08:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101522">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMZ5cfgwCf940Ov2GZHLynfGwQ-b3tLNSYFs6rvFht-58ELx9Rz2Qh_tWD6kzSXGK7nLDKA4jr-0r5BIzXiIAS7Md3U3bxaQF-GD7yWzzt01MAWdtHTtZiu0KVNZU9VwHoBbJePcnvoDOe5VYAq7Q0G5utaGBKzEFIqc8vksiklL2oOmF3r9h9VU-V3Nc6iHIq0yOrTggfYHCxPhxb0mR-XUqPhEyIw0MX-BzL1DQMSe8bRA_uc_wCo9YC2mi9N4fricZAs8ZgZ1nyvfldGp110NNBD1IXoydX-OJaOz4WKD1KrXVGRdg0Rik5HOOZ95BDfHW_qpebOC4nJ-QdELzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">-EURO 2024
-2025 Champions League
-2026 Champions League
-2026 World Cup
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101522" target="_blank">📅 08:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101521">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
⚽️
ماريو كورتگانا:
🤩
🤩
- رئال مادرید در صورت ارائه پیشنهادی مناسب آماده فروش کاماوینگا و رائول آسنسیو است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101521" target="_blank">📅 02:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101520">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mklh6hrbvi3GEronsTOpq6TS5rYqwmaq7Zx5ntdWLitYMPEH7g6S2wu3v_orUkeFciXFtHNsGO4sIj_IWOBSWcROJ_B12ra9q0RtByZDvVo7pSWYplQw6lhn0Ayxt8Q-y4AMBhCk_tBQr0eleod9D3ftWf_XzXUM4hj2SLfFlCARe1sQaJbjI6tfH8FtFo_HZ7H4bL9LiUd5hvYP7PVi2cvpzgFcj0XGgvL8Fi7awQ3GV8hd2kfOotGR0vffFgkDxsU2aJicTxVM5cfGIJhv8vjpUgKpivnvS-PH3scbvWBmFVT0z9TzTqL7qasMLiKTTHB75CQGoCnrhIZMKK5ISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇳
دونالد ترامپ در یک جمع خصوصی به اینفانتینو پیشنهاد داده که در صورت عدم انتخاب مجدد به عنوان رئیس فیفا، نامزد پست دبیرکلی سازمان‌ملل شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101520" target="_blank">📅 01:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101519">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZoQC2h_yE4ZcWE_WVu1trKwz4A4apEz4euGFNSSgRHui64lkTPcvsmWRbwdHRXUm7KeRiMxN8TIPLxpAq-T8jx7fbbZaX7l4mKiufC_m3zrN-FBP_j668TsE2F9w-FV_K-CCC71542jm-XrdAxGB6VTEtqFW1JpsWHIr01uS6AxiMaPPtXR6YyceTDAlSOpgInR7CYAGL_ND9a-2f2z2XXhAD2tHNBlMc6aGPFOjU8hKhkKVYA5hR-iHfBzFWKvsLvU_I_t9EZxIVjVxi8Da0tjajqva0t-GQDZr-U5iSw0w1pYhkNy_19b0HShmStLD958AIADXnTvSmGn_q1b2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین جذب فالور از جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101519" target="_blank">📅 01:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101518">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fL6znC1FgLjM6QpaCD2zoDcgZqHanLSScDqle32zIq361VeXZQXwV64JDavWO0yymYBvWv9IrdS1zxl21a_GtyEFyOMaW9SzaaQwcD3eZpo-LTEAqr-1vjl_7lJ00w_8LigUv1PAdy2lCdF-ss2zu2IG40IXhPtau9tqanAWw4gozarb4VyMF38Ss1X2VrWDqX-bEDxRTM4NnFFV5qlskqO23X_BTmQz9WxpJV3OdB3qz5FNKlxoTeSwrmEZmC0U1gy_9yXiHl8_S0ubo9EjCQf1g2jjh2WzLg_97Vyy-wU_E7_vI9tuvr6q6qG0eUqyuzbvXBZmO7mBiLHBRQSN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییییییی از متئو مورتو:
– فلورنتینو پِرز اکنون بیشتر از قبل، تمایل به تکمیل انتقال رودری دارد. توافق بر سر شرایط شخصی، به زودی حاصل خواهد شد.
💣
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101518" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101517">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101517" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101516">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWIK2oQe5MF1shfjF1DWHxa9bC_rHMSEjMgpXbzm5JoXMSHDU-SmqxzfF_H44Lr9CJ3ltXm3FzEohQAseXQvGBFv3NUYkl5tt02hOy8gvhas6kKaYFRPqsElKV_b8jRzLLFJs9TZu2ox56nimCekAM-J4HvTMr42TRlleZCsAJEmrOdg_5y2FCt0utJ9Tw0aHrgv6p0cX6ZCFT6zvxaVoDxqbaBsd1GDGiEN3ljLDTixK1MX04xXuXsc1OfmAePFDkdcPIg0Ithnil6Vq8yrJKU0ghdpO6cZH28oPcjCvviyRMvOEC1FTI8FBu0XYuVwHvWLnyTJLlwiNaOd9TvPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101516" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101515">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgEvpbfwwkWI-ZSMgldNS5hnxOKY8tPF2XIv8X6Oj-bG7stb1qQgW_4ye11EaVtApo_mqNHkxx_uZnO8s4xSnsCuZeDIotk7TgKKv3ApACTMFKudztqAgPFkVRbdyUxrszIOoKwX5RMPIeSAmHpQ405hVETR1rA-vIAnde3c5u0WTv-1HIMrMCFSXKUxnggvyp-R3TxJFKuTORZXr5wRzb4EiZd_UF5QPig3UZDkM4K50qZP-vbb59FQbdJXnOcJ8Gp5HViN9QwkgHpQHKjak1oMv0gIXtUSfgdQSN9GttzavtWS1j1cSJsJJIXQUMoEvLJc1jktzDsWte8my8Pdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جدیدترین مصاحبه رودری و باز هم خایمالیش برای رئال مادرید:
🔹
رئال مادرید بزرگ‌ترین باشگاه دنیاست و واقعاً دلم می‌خواد برای این تیم بازی کنم. من و خانواده‌ام دوست داریم به اسپانیا برگردیم. اگر لازم باشه بدون لحظه‌ای تردید قراردادم رو با رئال امضا می‌کنم.
🔹
مدیر برنامه‌هام با رئال مادرید در ارتباطه اما بهش گفتم تا وقتی مسابقات تموم نشده، حواسم رو پرت نکنه. حالا می‌رم تعطیلات رو کنار خانواده‌ام بگذرونم و امیدوارم مدیر برنامه‌هام به‌زودی با یه خبر خوب باهام تماس بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101515" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101514">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=MVFTo7Qy-drtEOhZjCpXj85D7iD2uSIfmUBaIPrJqzOh-dxg85tK3tWFRS5OLm5s9u6744L8XGJKhh3D-wZ40NJrz40HUuAEHgC58XA55oGGtpMnlxY8upN2V6Tk68wu92yAx-vXJUXks9qp-wNUJSuTbzdm8yqIssF8tPKT8o3_WgYO5BvrAwiNvLXXep_AY5-guDJOL0vj8YO7CJkbWeJS_mHj4zfDcWQk7q33EBjXD2QnlI1hsDStT4_QvFi8ton5wLrnRI6DbimDfrd89yyEi3L7X80oiaI6S9v5TrqCXBGVZ9Pn2WNPETo9pBl62uY_s5yUgeUc657xqHER8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=MVFTo7Qy-drtEOhZjCpXj85D7iD2uSIfmUBaIPrJqzOh-dxg85tK3tWFRS5OLm5s9u6744L8XGJKhh3D-wZ40NJrz40HUuAEHgC58XA55oGGtpMnlxY8upN2V6Tk68wu92yAx-vXJUXks9qp-wNUJSuTbzdm8yqIssF8tPKT8o3_WgYO5BvrAwiNvLXXep_AY5-guDJOL0vj8YO7CJkbWeJS_mHj4zfDcWQk7q33EBjXD2QnlI1hsDStT4_QvFi8ton5wLrnRI6DbimDfrd89yyEi3L7X80oiaI6S9v5TrqCXBGVZ9Pn2WNPETo9pBl62uY_s5yUgeUc657xqHER8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاوی و فابیان رویز که اهل شهر لوس پالاسیوس استان سویا هستن بعد از قهرمانی با تیم ملی اسپانیا در جام جهانی، وقتی به شهر محل تولدشون رفتن، بردنشون روی ترازو و اندازه وزن بدنشون بهشون گوجه دادن
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101514" target="_blank">📅 01:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101513">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO1LvhIZihDB1ShY30R_oczXqc2pZNECK0Kb6inSzvehjycsubEZbfQ_Ty3hNf1OX1K8nUeW-r2xd_FdwdxiKsu5S31xvimugj0LtTzEjycdFGKX4HUL8tuK40K8JN2pAJOHrlqSbX5MSqUBy5_ueCeSRvnPJzuqTEA01_OL8qGlrd_OZuoZNezI_qDy8UC-yqdIVmmSR_LEj_scOIs1TBq6AuHhUjjA7_bQBSorwzvjsSKUjLA3xC58T7PuZhtzVgyaSivSnUBlSxQi2IwR2PYo3Z-gkQsfUQvafg6dXTkrxE62X13tpJ813mGhB1pbcH1XnjqeZcPqiUqlOvWIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۵۰ بازیکن برتر جام‌جهانی از نگاه the Athletic
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101513" target="_blank">📅 01:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101512">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q3M84O6JqK7eVXl78_6QA-ZomQRpkrLmkkTxgMDaE9ZIJgioUCTDahgysNe0hCcLU0ioQfKtrOl-M1hWcHYkHXLYdI2h_WQ4ixl55C-ht2WU7tpXnS4UtXYoCQzN900DWoq1_haRBgj4F-k97uRVT-aexMnzYPM3iO2n-UsMaRt8TwW9nGH4S6_wifTHLhD3AZ6yu3v0Q4Y2Fxew1qYJ4eR1ptpJr5iWuEB7ECAU9hhLl2f8f2_bMA5DO91YiB-GGAlbNBHcu67MqVIHsBSACdDP4KRMzPx8Hq2T2hFxDYJP1vhsCQQKeksy8c8p2nerZrS8YWRemM4xa7cigUI0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
از رامون‌آلوارز: دیدگاه رئال‌مادرید نسبت به جذب رودری عوض شده و احتمال عقد قرارداد با ستاره تیم‌ملی اسپانیا افزایش یافته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101512" target="_blank">📅 00:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101511">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
قرارگاه مرکزی خاتم‌الانبیا: تهدید حملات آمریکا به مراکز هسته‌ای ایران جدی است و اگر چنین اتفاقی رخ بدهد تمامی کشورهای منطقه آماج موشک‌های سهمگین قرار خواهند گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101511" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101509">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EuweMksr9dQjH1dOUybDigkRZnOzy5q5WBpr2ogziLVryEbOorrPys1o0JB37rCzA_w6GYtuU9mlf7dEQd-_rPsrsX2DV_akgNtqLJZeA-v6f4PuVZiftzPOW7jU93-sA6rvRWAQ5I5wa-UMb4MIaTcmzjbS3xXGj_CCT8RDoZV4cy4x_3v0AUFJzYiTAvOUPMNmVlcP0tmxewnRetUmSQAT4D1BgAVDqCJ8ROTOGMetJEdY_p8YXgwF-YG7OCxBnZ2i-WSupWoi0P19EEg6W_qwLetQyil7Xseuhps0QCuHgbVKD4KnmocaXx-d40u6xiNVMu6WLY1zOHK8l3rNww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvryqQ3tAq-ex7rKZhRlKtGruYRbcagknVC4RDjUZx8N3r5BUDNTVzhDVeH__2FU7mYNmymPL7hyhokp-_Pg3PJCBRJv0nOWLZtec7j8cJw7vHMWAuZ0-Jti7fchRPmrWwOBqTMpOXmO1gVkOAcK4_MzLo_EYnxS-hnsbgMmTShNrmZ8GU-PV39RNsGyl_IIyuNGZs_A5zM_LblIT-D_XKIxOmyOW8tAIE-gvl9m5Sh_JzKnMH2oyprMwDSo8jZgiICROebRDCLZvyQEmU-zhXZ5QE_zWNDU_mT6JwsrM2w7-a5F5hqiEDiUWY1yjJjGpOQVEKQxAnjjMLN8tIBI1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101509" target="_blank">📅 00:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101508">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNTGBL0sP3AoiGK1qoEIWJPvIthZH5DlaL54Y_XyrMEX4PfDgEXyd1L162m8m-UvrIf_a6PJbDu727Ovoikx_1FdaWXRD2FMjTzeCsbu-kleDT52Qdw4kFdHoX37uW5lBiZlpCK-B7mCw-2i4lnbKPR5nmig4UK128y4OAlrAWDhFeyBopehzdDUtURPKekn2FVdaHu04cPxT5_1k4iJrTLMcNGHnFZFoeKxb8rLM8HhnDeiV7o27yMOPyOnKXk-5IonkmYr3mP0hWqMm4ZdjeAACIsccMIa9DXxUfVKB4_q4D-l4XwAoNbv0zm4MT4Hc-HWvkXFolaMceh1os24AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101508" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101507">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esC-wQZi9on3W2Ct_9rMpsEMf5VZ7RKxbmh_u1dXWMrYuSAaDBzAnJPxTSmbMd1Vv_MCMAIIo44IDwVIQGonkwjg2_9bv5dzoQVmzJJsvV7nXQMsBYyUkrRwXNQ2cYJ__5uj2RInrmZeVXIIve5G-r4mVdnzrqxYcglZ71w5ZCZ2obtn6MH4Yd5wzc1NRNsy3AjEbv7q56Fa0OlqFZj94nKKTzGBXncGFLL_X8uu07K5hcyvsQQzIA1WYB-DRuzW_6k1k2-sU9s8hc21NnhiFSZoHjo2o3VJf4b84siRldBDJFkgyJN0YDKaBijfKqkxw260Q0Sl1vVVr_8eYYv5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگی که شباهت عجیبی به مارک کوکوریا داره و حسابی وایرال شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101507" target="_blank">📅 00:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101506">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm6eKwMBmOd_JX09xZchL5zFu29n-mfzfJ7SHwxVVUP6Muvfl5h3opT4DKa45rE9211tC4mFyac0KlKSqWBrToEHqaUi_772p8DVOWpfjuQalm0ttR28WPYqDTJYTv28bgHqGht-WwlKiNqpG_ttMNAYNIYlrQ0AwgG1nayh9U1m5JLTTcCPAVFmcfYq3AGst-7dquiNuP7e-qbz-AGqmh2PZjpF_RpFSzF8zwANiaIOaMMI-Tnj7HGQ6xoqS7hvRoqh4pEs90ihPozhAbZY-Zefazh-8eFyYF5uJLjdtI7K8bkTRoA6QyEad2UI6JqOZHYLlAGRrrwX9EoHayh7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101506" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101505">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">راجب پنجره
🔵
🚨
⚽️
امشب باز هم از علی تاجرنیا پرسیدم و ایشون خیلی با اطمینان جواب دادند که پنجره باز میشه و بر این حساب هم دارن بازیکنان خارجی رو مازاد می‌کنند و مذاکرات و میبرن جلو، بنابراین امشب دوباره تاجرنیا اعلام کرد که بهتون بگیم پنجره استقلال قطعا باز…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101505" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101504">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTLY3EhRyMaOlNekbt2A6jn0d_2W9FUaXDcCLiRP2XeJx5eDwFsxjZWjOB1MIEaAUiq2SU0CxNbpQshhg6KhWsxZQR_hlvDxRz80aLh0usp27Kr53QsKe9c7OMSNgsMSu8xhKT_rrBfCcFNVqO8wDqzYbO3kPZXIt-ReDeZ9zS7luEmxsYEsaYeHTnermfjN0JWefSxXoUm0mW7P_kaIIFDaat4vahq0r_Rrs3v-YBzkgBZjlcgDvaSXpwdaohBj7p629czWjdZuGsGcKx3rCWZWs18EyQeWSBRPkpyiK9huwVgKezCZ1WP_9Bq1XglCTz9aAIZVjxpTWgu_qUuRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان:
پارادس خیلی خوش شانسه که من تو زمین نبودم! وگرنه یه جوری با سر میزدم تو سرش که کارت قرمز بگیرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101504" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101503">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuDdECLz2pj18UmoZMHbOO2UR76N4_G0WeYsXlVZppre222s4W1A_9ytIebsUL_lQDh2pYF33oveqLnWZ0J-gov6-UTiQnEZHEGtUofq6THgJzxusNTN56ssv_34PjzzUpH2jr1L747DCxuDsuYB3dh34DY477mcwqflBXEfzkls9PimIbc7sTlZA3TKctV_cmFI1iceqzLmiMo0YHfH1FPVoiJPWcWnOmmONV8F9ykLwrGpuWQ_KtpRBGJEWcxmdbtjHhmxeOuURiL9FocclJHQmL1z47metLJdB6w64VL5E2UzvBed6xM44DEoqEZ793e9LH6kXOvvRw1JaMTpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا بازیکنان آرژانتینی که پس از پایان مسابقه رفتارهای خشونت‌آمیزی داشتند، باید مجازات شوند؟
🎙
گاوی:
به نظر من نباید آن‌ها را محروم کنند. میدانم که این رفتار تصویری مناسب برای کودکان ارائه نمی‌دهد، اما این بخشی از ذات فوتبال است، و گاهی اوقات خشونت نیز در آن وجود دارد. در نهایت، همه این‌ها بخشی از فوتبال است و باید همیشه به همین منوال باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101503" target="_blank">📅 23:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101502">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd187695c.mp4?token=iM1y829gr-Pd2hVsdT-E6UcHAxddYBytHOWxjHd3s9I-BbihTmTKxebGrfJu0s7l-YCE4hTgtTRAzpflFTJBgL8w2VKJ7UTDrduzeItHViG9w6xMcXz3RvcGiL9C04dxq-OeIC_HH5TJVwL54BYX29ZhNqTz8g5zlUK6TUB8VOQumEh596sq_zgiALEROmzbF_bAlgQ-pgi_wzlydgGMi-Bfq_Eh6z8txjan-efAAJrY1TFNNLnzzex4EhP1E7ci0neqgDX5chvhXUsOUxAH_KAsWS2EEBNLB2amXAGaQWnUKYo2sdsR0MEEKSHcUPIaPYEtYBwvNGSRk0ZbYBP7Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd187695c.mp4?token=iM1y829gr-Pd2hVsdT-E6UcHAxddYBytHOWxjHd3s9I-BbihTmTKxebGrfJu0s7l-YCE4hTgtTRAzpflFTJBgL8w2VKJ7UTDrduzeItHViG9w6xMcXz3RvcGiL9C04dxq-OeIC_HH5TJVwL54BYX29ZhNqTz8g5zlUK6TUB8VOQumEh596sq_zgiALEROmzbF_bAlgQ-pgi_wzlydgGMi-Bfq_Eh6z8txjan-efAAJrY1TFNNLnzzex4EhP1E7ci0neqgDX5chvhXUsOUxAH_KAsWS2EEBNLB2amXAGaQWnUKYo2sdsR0MEEKSHcUPIaPYEtYBwvNGSRk0ZbYBP7Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپی که از مقایسه اونای سیمون و مارتینز بعد گرفتن دستکش طلایی وایرال شده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101502" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101501">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DE1AcP4x4vP6VVyWJhi2Mp0AXAOQo-O0cb9RYyDYfJV62QAL3NE2CqnScjc130N4VKqzuCcrM864TJHKrSK3Ra-S1QwCKD93o9AorEaQPVsQI-fiQo50_sb-FG7ae5KFPv5Fe1pcxfbPzaR4hjWraEPyX5MgyT3C-Gw7s7bb_Cvz7YsNq7AqvvXGdmNa7RjcEkr1L_h2QwcI4IVImCspMv2W76UtFMq4MKwovDX3ZyhmfF0BPygWOvflcgBXQHF8i3Gwoaf1EKgGBeFoFFpOBwgl5TGJoJg7pukneNS0WucRRmhsN3mNZMjOM5LuVkWnQY9ovJKmTM62lpylDycLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
توییت جدید امباپه: من برگشتم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101501" target="_blank">📅 22:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101500">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9116787106.mp4?token=CiBZrsnS8uwXAlB_xublcCAkFWi0HxAMMHnO-KtcOcwBQOHapzsH4vSjwlWTjp9WlI7w3CPz-zOehVMoth53GWEWQ8HZXYeBwEvMWIHiwG--wdt9S_O4_jljfXUBOf_Jso0rHoOitQEWByUsytIdbFLBIBIfFxPP4imWX95-ELIAmUwSS4jcQ1enQj9O2Gi9T1jDBXDOdCEH3S_cq0Tau_851b1zmrtuBja9vNi-1Mu-EemP9ev7atWOTtCUoejKTY4fxpeaBnCiHbZbjQfThr9pju91awx0l4grNij2X5gkdv5MeI-Xuij-tfSut1_m8k5_RBtZ_YqeDWKYnnNef4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9116787106.mp4?token=CiBZrsnS8uwXAlB_xublcCAkFWi0HxAMMHnO-KtcOcwBQOHapzsH4vSjwlWTjp9WlI7w3CPz-zOehVMoth53GWEWQ8HZXYeBwEvMWIHiwG--wdt9S_O4_jljfXUBOf_Jso0rHoOitQEWByUsytIdbFLBIBIfFxPP4imWX95-ELIAmUwSS4jcQ1enQj9O2Gi9T1jDBXDOdCEH3S_cq0Tau_851b1zmrtuBja9vNi-1Mu-EemP9ev7atWOTtCUoejKTY4fxpeaBnCiHbZbjQfThr9pju91awx0l4grNij2X5gkdv5MeI-Xuij-tfSut1_m8k5_RBtZ_YqeDWKYnnNef4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👀
خداداد عزیزی اومد یه خاطره از اولین سینما رفتنش بگه دیگه جواد خیابانی ولش نکرد و دونه به دونه اسم فیلمارو میگه و اشک عزیزی رو در میاره؛ خداداد عزیزی میگه من ۴۰ شبه از دستت چی میکشم آقا جواد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101500" target="_blank">📅 22:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101499">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OX_F8fvDeIN40DCmlMQ1jNsoEX-CpX1gbjYuhEtmGx7XbP9I25TzE2UJ6-RZEh_R-w549cqZ4d3ZAjaoyg0f8lcufxFMerEM7rcGXd59aOyEDnPdbNC818VF1ESHxy7hO7sEBPus_AONyCPJ0adSm2e_rKwi8SgLDvAwtIWgA8Y8gAKi9jCXPyn9HTAeQ5FfDuCN4yuqEdOmMwcQEXmNB-PwNWhSDpBi5q8uEYIaYhYiS9OSjQNNlCszR0RCm36Ds1-xNmBcoFazRGdSkUX0DWhFYGOLAQtaC-2S9lP5SSGyPysaJFm_P-CuJJxxNMAVTFD4Wu_LfcgK84JEDvgxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🥂
استوری جدید راموس در کنار لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101499" target="_blank">📅 22:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101498">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a3469819.mp4?token=njHCEZsNGDfyFvkYAw6bXa6ftulMa2pXnz2QIE-mm_eW4uKYC4ySmFRnYl5wkmmIP9Oa6MSyqXD8Vc7KpNdC3EQSvSnzV66wXeTbV3_KOMdyI639_vHLWzC-iREc7k1UfwiffmjI3DVX3DF8J4U2QwDgUfa-zs9OPRnbKBjF6otzr2AGjdJWwLm5Vv0egjyvHFAyf1_nnytWxPYh1Z_uuTSLII556VM_FNSIKxBebQIfDlZxt8v34eRccblZc51gDlfoH3dW0cvRZXZfCFFQswlxjNuJVA0Y_ESEQbjZ04P6qFxNODRrJsSZredJvmfEVS8CfneVT4IZGgycBU7Q3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a3469819.mp4?token=njHCEZsNGDfyFvkYAw6bXa6ftulMa2pXnz2QIE-mm_eW4uKYC4ySmFRnYl5wkmmIP9Oa6MSyqXD8Vc7KpNdC3EQSvSnzV66wXeTbV3_KOMdyI639_vHLWzC-iREc7k1UfwiffmjI3DVX3DF8J4U2QwDgUfa-zs9OPRnbKBjF6otzr2AGjdJWwLm5Vv0egjyvHFAyf1_nnytWxPYh1Z_uuTSLII556VM_FNSIKxBebQIfDlZxt8v34eRccblZc51gDlfoH3dW0cvRZXZfCFFQswlxjNuJVA0Y_ESEQbjZ04P6qFxNODRrJsSZredJvmfEVS8CfneVT4IZGgycBU7Q3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا حتی سطلای زبالشونم شادترین سطلای دنیا هستن
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101498" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101497">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGWcHyMV-CqVtoKDT43MhP4CMzimdu8qFfCkPVIZtwhp2wyfYPrqJ8mDnyEOQkFatPj4ss4diUqDQVoc6JL1cp6AAwuj1RlGdKJpJ4ebZs41zc_NAbyv7_1Xh85GemoGoiaTXipfhUf2hAj_7OmISsgjRFGaQ6LqL_N_pozlM5IzgT6g0KXJ0wXgTxZj7ztWQxt8pZYC9Jv6jvFBcZHXPu2xBigP-0fWJhYGF3ybNblRsGjFYJCcamMv08Z89fR-FLTFEdkTybKnLsBZKgzucx_v4sceC2-YqegMrrw28ztmhiZSSMZ0Bf8MAM4lvR_QF8TCKbHSec72FHLn6U1H2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاویه فکو که داری داداشششششش؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101497" target="_blank">📅 22:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101492">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UL1S5orZlB5sMP7ACv0S9IHN3orxbpVlGnBxOm4PTNpgJ-SGYi5RquiphuieZLSGvuOtzP662D6HFFlVYWd2cWc37cF1evAL2iJpqIAexfxRLlyxobiaQV-XocwNokygJJwzTztDHwrh6Moo-8YNXJRwiPIuAPD9tkoDlcN8X5dSRKXqwe1UUxcZdVfQpva6_8Kb1ytj9xqwpzD82Pks4r5ISYVnJFWZGr76dAqjxcJIslT70UD62gch7X9juc6rcp1rTLvSGk155NAF16fcrreiwav0RdWayMNiNxv521oahZ13I_k4BEDyi6chyMl77qcG49Hqiz2zG_aHPJOwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UeZqS-pTFMysKdZqheWR_3Jb6y57n7XBzDEP9Jmkb03eib4WKmznB7_NQfIbZgkfCQi86fUPKWYjTmaW9FeWRrFBYgsU_H8rfpQA6XgfkZR7l4A0A5f1JxmHEBtFOSijtzVK6GtVExaDSKGM84KGoz8qC-TW9v2fkYsgcLliMkuMEt79jiCysuU_kaN7OnsKGfAB2cyufe1LJlLo9mLevLrtxG1dsEoF_V_l3vrgbkKbO-NeqTVOujx3hprHhKCalVMeigXH0x3ubsZw2prUC2Lipe_qP-MwY8an1FtwgqiVuxdqFYr_vaxEqLgzALpCpBVZozeoL-JdvBYh7s-63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ds_iaW3R4-1vxrNgPzst3Z3Nb7DKlHSK-ullDn32gTmw9MCMJmWepXSA-lqOWVOf1An0kvydGYhqUltnbRskkzihn9x9vk7iypg4Bns3byRWSb3fns5nMYWY1IzxOjHCtf58pSbtZwP9tnMN1LMjgtpVLNAAIbfHo0sOJBOI5rG_CkokztgdRNhGR4VXKShCxX0Y8sKnkI8mGAwacdF2xmxgzuOJLAaa1VTa00kKt5Nw21VkapctcFeiCBcCIMv3BOreueT5UKRJr8cROr7Q0MJnEouAJ_wzy30z_BuyDcXNPsokgf0lif_tD7myfTzw_qLpxK0qM1o6o6sglFO_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbJxy90h3z7K5b6VR2N5m6FBi3Vamb83Rz_US1lNFtbMysxM5YAqlwpIymsEFJGar85FyHiN92-B8X6Tswd88Oyry2Ikn0xsLLv1bFFF-fTQDq7GS4daX4CpcOdL0jDHocWKZGTtroEBu2OgRJsraEovM7p9h8dZX09DIqYyKXeOdR-ZTPWNW0BMwr18FZY8ZRuykpUAuMz-NVnd0Dh1SbSBQh4AoCNCrkP3J04wQEY-km9IiEkIRlsWbF1CW5EOsBaRMEFOOGeS9NTa7FISr2OKFSyoD7p0tc0FNrV1vDea35jGYhlJgKWZYj_zobNHR13Q8id1E3Wr5VrfekLLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgDVfbi_kZc9EMzeowZ_qjuBacuQzMUnEZrgdTqr-BR1qLwAIV9pR09rOMVKfmbpTM58OBcdu8kQNcT1WFT-jwr257jUIJUYIpq64eSg3qpj8ns9Rd2fVkuMjZOoN5M-5mkB0QEPB3RaDJKfFTF9FU-bKNCh8x-QxsVuSNk-VViQCvcCma5fUl9vk2_JGoZOuOZoV4Kf7AcyFYrdPy1Ih4tpJuVgNNHkXh25g7dOoPJVYnXEmFfHvzHt3VZfxm3zCTufop5WFLdpWaltFFAxMTTY7yFAXLVtAmF1fS5G2FAN9hit8By1jicWkD6DQtqUqaq1HGcAYYbzly8PPBHzpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
تعطیلات تابستونی وینیسیوس و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101492" target="_blank">📅 22:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101491">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2aa4c289.mp4?token=PYa7nR_vVdXm0f0Vt9yp43Jm1za2AUzkxuxRaZ9-OPDIbMVYlAE_i7Ul-0qZT0MrFGQ8h2C0hMaXsG_z17KqEe5SsYnByBT68DT0M0V6WKjdcpLbinZz8JV6q6AD5v4KVAoP2fonASvDbh-ChiGFCRq2_EmkqClEqovoTOmOtfLmIzJwyb12zJt5oERpYgswclO-SvnEcy7NajFKQG7zNOlzoMaftrkbFF0ubwPvW9CSJEgYWVExOrMynofdQ35AoIEi-0ODpReCT-A4U9qE9BenYNfkH8gJ2tD7OOMHy2a3fCNaM8-3JmsaS40eUTLC80z9DJM9g5gk9YnxWTNyzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2aa4c289.mp4?token=PYa7nR_vVdXm0f0Vt9yp43Jm1za2AUzkxuxRaZ9-OPDIbMVYlAE_i7Ul-0qZT0MrFGQ8h2C0hMaXsG_z17KqEe5SsYnByBT68DT0M0V6WKjdcpLbinZz8JV6q6AD5v4KVAoP2fonASvDbh-ChiGFCRq2_EmkqClEqovoTOmOtfLmIzJwyb12zJt5oERpYgswclO-SvnEcy7NajFKQG7zNOlzoMaftrkbFF0ubwPvW9CSJEgYWVExOrMynofdQ35AoIEi-0ODpReCT-A4U9qE9BenYNfkH8gJ2tD7OOMHy2a3fCNaM8-3JmsaS40eUTLC80z9DJM9g5gk9YnxWTNyzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"اصالت یعنی به ثروت برسی، اما حاضر باشی هزینه کنی برای کسانی که سال‌ها از آرزوهاشون گذشتن تا تو به آرزوهات برسی.
بعضی‌ها با ثروتشون دنبال دیده شدن هستن ولی بعضی‌ها دنبال جبران سال‌هایی هستن که پدر و مادرشون بی‌صدا از خودشون گذشتن.
شاید ارزش واقعی ثروت، به چیزهایی نباشه که برای خودت می‌خری؛ به لبخندی باشه که به روی لب ها میشونی و حمایت ودلگرمی ای که به دیگران میبخشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101491" target="_blank">📅 21:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101490">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbXO0T5AnZiJHN2EWV3cMV4klhLXw6Lz67aa6eWnyjPrIrGDRU6vdeWLCb1HFKZOe80A_MRVrsBvCFcMEglwOS8xX3Vz3fsspe16Zju5wBTOAtnFkgtvI-GaCmyG5jjfo6acdmPNDEXBDvW28PNvaYi5lX_yj9owdmOgTcaw_jMab-5ev3_cm05wfi0xYWes7drJgMQt7_CP4P6V6mQfPVXTcMRVLQs4JJENV076boEy5Z3E8gG1sKwtCSQ_SFqIT87YsUr2OHPU5yr2eScmaC5EgD7QdPC00goFVm4TmSVZOWEiiePLg_PdO4HDqvPCbmYYq8BB5dIf9CWyB5QMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
تیم منتخب بدترین بازیکنان جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101490" target="_blank">📅 21:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101489">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II4kIKQvIPvvlbbnN-r67njtU2yH2RB-vVHvFXMqzpxw5RbXdwDghDXZWj3yxlkKIOqXkPA7lgfCQJ1AQ2SMinYt3sFjlY8zOjmSwQN-QqvbPuECcIKi_fSP_cr0vGmpVk5xFWKWeqnJKAj9ZX7J4GiwS19kzFtgI0SkK7utN0s_XBiAemg6X5BNqR7qFNaBiMMNbZEAL-jwd1uXKLrG6DU0ElVMkWVJRa5oZqwd6uYAB-MJQ_fwked7t-ljqUq2zgj-J4sMloGkJhX80lpY6xPp52RuIgAa40OzqgCV2Hm-DpyUoBlN2xnKljwThLcQoJ8DNr7UzfTL43Hqt4VCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید وینی با چونه جدیدش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101489" target="_blank">📅 21:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101487">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBIaTxQF8eSQ6A1If0iIn3X_SlEA_fXUQRQnBnoMKmPknkOVnDQ7CWzEwfbMRqAuoy7V27VBACZ1fyQb1tqHHDQv637v8fEA6NOYeNgnM680QLGdqMRL_RujlKme7s2TvYtMF2qt3Q3pmkWWsOD719ZAwhhfpL8Nwi0LSh6qekx67_Jt2N_NRqh28rrr4--gE9z1Sw7cgss6pXXvYcgg41J8iAZ7O_Aht1HXgOlL1PPSvuJ7P_fV8qzIQX07_umraJWIuVcsYUabHtJt2itzHOQFHet3gHXhMGLuPPws5ocp8ou0FypYkd83esDdWcZPrk2d5aUQ5CNAO7SUZGKjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان فصل 2025/26 در میان باشگاه‌ها و تیم‌های ملی در پنج لیگ برتر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101487" target="_blank">📅 21:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101486">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_5yl7FA0srvQT0tyyYeDw38w5m2bzB94gocn3Vvwug4EnZ1j9qJRDpUvy9S2-RGewvKb2QsBIXvcnViRggLlD8xnzINa4LXuQGMQxyo2FQ3ubp4YjgYsSZxpIEHPlMuT9upHUP0hHHB6iq29LtJq5O3ike01j0ZiR295r6YZaHKDrvBgg07fd8ceCzJRm9iTnpqK52h8Q-6v56Yx_t1wVmMNH_wrlh7rf7lwKGFBdhDZZKOvf00rjch82A-Dy-2NGMXPfw-MpZdxvgHr7j6AsXLHvZBcHwHmUDnWeO2-hrGMhWUtuQItX73MoqdkPb_LvGxhVyQRU0cFL7-0kVTdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رادیو کاتالونیا:
🔵
🔺
🔻
لاپورت جدیدترین بازیکنی است که خود را به بارسلونا پیشنهاد داده است. عوامل مربوط به بازیکن با لاپورتا در دالاس ملاقات کردند و ایده حضور در بارسلونا را مطرح کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101486" target="_blank">📅 21:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101484">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cw9U6kUGhWgjva6VbITAAKxtNKKKoC-Wnfj3-mOfVDWgrWr3r5OfS5iIUUxEpdbp7wRQc9kmvEG5xTmdHNLbU4T8aHEuif6eXDqsg_20saLPmkhuidrniOvx9zrLWcJTKPKPZ2viDcVRXVqYyoHnolquYxeSdUMy4m5jahAbin9NpFVvsiOUw73nwMQokqNi3AueahBPmDoVokMVSKop6AYTO5ddB1r6qxIQs5LijToHM-_IJoQOf1eHamIl0Vx-LXMTEvxoYZlyodS47EFJHSDrK-Lvhud6t8gCU4I_rTtL5hsL-wdyXfnIQpDdEiXd1ZDfoAKlDo9NEyf8bUs0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjuqrsqqZwMUoeXV-n9jx9EDaa7iv87gRFI4ehmPqTzU77HTgJIAgCZulvygqfVRuE9IyoNtzQYRauS62Fv7kCp1-6u7zy3AujHuLV7s7dvB5bwDjg0ZuyI9MvWb7ENo0kgo1WWmbTA-p2jWp07jy3CyyHkFZ3W6uwY6hEHAdURGWXVbLiVV4rxLvjgk26rVXLOl6xGEsNaNJ3h9gBz6AZ5Of0tHxXoibDqSuH3upsSHQiI864atj2tOilTYbs5ggU_JEtMdyUBPlCEd0HAcdwOAzxH18eMK9Wqmr8Z9logh62j-mOYwH8RKWKvXWIH_ZiEeHccqprwwjwjxUby-Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😁
زیر بغل شکیرا از آینده‌مون تو ایران روشن‌تره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101484" target="_blank">📅 20:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101483">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etbgO4iRto9b3nKI_K4PII1qsAgMKi67GEvZRQaXpDrBxhwc-bmg-aZLYNT-IxMLiQCzrZjRL2sc_HeS3aemZTfxtulRe535eP7DJEAUesXx4xXYfbMuk7TNPZ_64m2k4cwP8NY8fk4pA9D5isda2C1VG2onwEtaKDeZMmv3UABu5VBBqzhGnJFbYBXxeoVYDZ3y3eyz4qHB5N0bUvLUA3XuPHn0LfQvEtyP_UwOENjhIJKxKy9LtzV8tAMY5FJF5B2pHQRHkxkSkVyLM7fDbvxom2sur-d6ut2dBCeVS3wDQMshJiPQdGjI0H0eDi7pw7oW4yGN2ZbzavTcOsYNpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
فوری از فابریزیو رومانو:
🔻
لوکا مودریچ قراردادشو یک فصل دیگه با میلان تمدید کرد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101483" target="_blank">📅 20:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101482">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0k-iEzgLLaQuujkA5ktVXspo9aCKm67CzWA9Ck1F-G33qgs9L_xjhmYaucMr9FD_yo-tV1V6x63XqfGD1JJyMAuxhq0R16IXlogULJMZJ1ty-QqFrEzl-h2pAm1Lixok40XM0bvZEh7zptKSA0v-OtGfv3hv_hbelbWO7_X-AsitniznfHq25els0UAwuLjmUlCb7NJm-ANljrSia4peslHT1tNeHry7XK7EtvgDf-DaQVyyV9OgxO1F0HbIIcdgZ-p9OPkC4eK2CC4AN6TUR87QMdcyzM52yYOBwj_SZ3R7nJZ1OMdANKgpdLmrP8AjS2lxZhQ9modxvsUrjst6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
||
بازیکنان جوان با بیشترین تعداد دریبل‌ موفق در تاریخ جام جهانی:
◉ 27 - لامینه یامال (2026)
👑
◎ 22 -
کیلیان امباپه (2018)
◎ 19 - جمال موسیالا (2022)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101482" target="_blank">📅 20:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101481">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NElHHe_92X0AQVCEC-ueuywXjpUHL_2L4ps4FDjuzMG_ky6oMqIX2qWoXX4wJBmlkQpXVHd81DuKcoHQLwQN6sPpJV1xsE3w4ojNRQgE_M906qcM78Xko-OLjA2WFzZN2ST6QSGpA-4I55zJyBVPkIUhDwzU15Lp0wdY_J1U9yt6ulnec-HalpSwRZwca3SXXhLdhVBWC3Svgfv9MxnL7MkEIjCha_mpppr_838NGaPdpDa-_xLJkA_hx-y6A8xYKA86lfleCq7Yuji28xkz9b5W9fFoc6E_v4tiFmg8yERLTcOZBAZezcXTc9Yug0efAY-LxzXbwZQP8sb2WeSMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه کاور EA FC27
نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰هزارتومنی برای خرید این بازی خرج کنه. تازه اگه فقط بخواد آفلاین بازیش کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101481" target="_blank">📅 20:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101480">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGPErkBsnx2WFjy3GmwNDmzbwQHr-1SUdgSEp5nv24GSAmjnGsecEakZYFgobspz2oUkJLEM50z1W4AtefBpEYTj91jukt25WOP1g6cy5-_fF4HLfvMYZ5O2A6Xw9MWlRRbNm_BVgTJGiM4LYnqf3nG_BH-wNWNVp1iZLSenNxbNKd_dc3IB2fKVODivHA8_y1ELUNUdgvqj8g_ns-JerxNRTznmksgNRI3FefPZ14vUHxTO5LCrfS3_3uNuEl9QiyAydZdnb8yOeHPBb9eUTu7cPl3QZPmlKWVb5mFrbZ737SxruyJRFXKF6SyunZ5bjjukoOXKEhsAeIK2aQf6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
گلوبو برزیل
🇧🇷
:
🇧🇷
• نیمار تا ماه دسامبر در باشگاه سانتوس باقی خواهد ماند تا قرارداد خود را به پایان برساند.
‏• در پایان سال، یا به یک باشگاه جدید خواهد پیوست (اگر پیشنهادی دریافت کند) یا ممکن است از فوتبال کناره‌گیری کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101480" target="_blank">📅 20:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101479">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ffcc2a6a.mp4?token=ObssKk_DRKRGyppZNhDEuUnCXONiclmBO5oaxy3ewUplvTjqjkdrluvJy6r1u2mKaPv5d_n1wsmS5OOIhDej84gZtXyidCiTXMVLXs-iPFO2785vMLtlsNRSC7QQZ2LTMgT63JyZUO82Xrdecfr8CpUuGpTBPdkvcVWNpbJtQr9X5qG4QKUugKar50poBjNHdaO2DKheIm7FILfyZ05KXu85eeaDbHFbcRkThdG7PsIeHG-ind_FWay8LWM3mq2nujIzlYQs6HkijwfLqz9kRafk7LMWcVvQXDFP2_589RjBwOtD0etRS-ZUWvdvv3vIvYS0CyoZWIE3FIARTBBcWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ffcc2a6a.mp4?token=ObssKk_DRKRGyppZNhDEuUnCXONiclmBO5oaxy3ewUplvTjqjkdrluvJy6r1u2mKaPv5d_n1wsmS5OOIhDej84gZtXyidCiTXMVLXs-iPFO2785vMLtlsNRSC7QQZ2LTMgT63JyZUO82Xrdecfr8CpUuGpTBPdkvcVWNpbJtQr9X5qG4QKUugKar50poBjNHdaO2DKheIm7FILfyZ05KXu85eeaDbHFbcRkThdG7PsIeHG-ind_FWay8LWM3mq2nujIzlYQs6HkijwfLqz9kRafk7LMWcVvQXDFP2_589RjBwOtD0etRS-ZUWvdvv3vIvYS0CyoZWIE3FIARTBBcWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
شیرین‌کاری لامین‌یامال در جشن دیشب اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101479" target="_blank">📅 20:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101477">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1111b268.mp4?token=UVgSV_9zR1hY3Djy51P9iIBoE5AarLrLwpUwAWLPmXrHBFDqjP5KSHZ7v-GYz9IRUz0fjfqi0JpfWc1qiKif50yIfuwICcZ91lb0eS67mXPGDDGuHcQeZC-SI5Jf6MZYgezt8Fu1jMFYslAGo1EdK3YWR5vxurEL_z0Yada7PSfZrEErA5OxwnGOSu38s10z924dD145w4VG2WKqlfeARy1sbWujjLWF052VN06gu4WV0JZoZxnaN2-tNGWE-J6sYo3y8uZ2QH506OhL88-K5R4cZIp4eZy9Q2C-QFYYrl0Up5TAMH6PHj2wKcTW-ffuxO-kFtk9lDU3ksca1Q680w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1111b268.mp4?token=UVgSV_9zR1hY3Djy51P9iIBoE5AarLrLwpUwAWLPmXrHBFDqjP5KSHZ7v-GYz9IRUz0fjfqi0JpfWc1qiKif50yIfuwICcZ91lb0eS67mXPGDDGuHcQeZC-SI5Jf6MZYgezt8Fu1jMFYslAGo1EdK3YWR5vxurEL_z0Yada7PSfZrEErA5OxwnGOSu38s10z924dD145w4VG2WKqlfeARy1sbWujjLWF052VN06gu4WV0JZoZxnaN2-tNGWE-J6sYo3y8uZ2QH506OhL88-K5R4cZIp4eZy9Q2C-QFYYrl0Up5TAMH6PHj2wKcTW-ffuxO-kFtk9lDU3ksca1Q680w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تایید دریافت پاداش میلیاردی از سوی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101477" target="_blank">📅 20:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101476">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfWkbDbzGc6dzUpvbmH-64OZMS2jeqKcV3J3W40PFrd4XTWvWil1haXl72fnVeHIHUvG_xM3pql9IoOfptyvcW-awwEfBpg2ROedFFuxniBvOd5kSyKlf7Q6FnJ52p1RYjH5gH2M7QMPazKf0nv0Z0ZG9v9namSZ6yLpDv8RtWbHnq3zVOqRLllFSZdLfn_WXgHnXY19hWg0IacBCpGGIRKiJS7Qm1EepvZAjhQBsrUTYqaZmJ-aBH66uvPxD5cH9Q0nyVhGgSakdr42yzn45xzAN-JXYxEtMmWhPr7pmMXzfLfwLCEjKt6J8pygD0oCeOossJDnwtLwPwOGKmHxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بازی های پیش فصل چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101476" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101475">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=NMl1HEJzmToYVGG8loGkOY-D9_-qVOXlAXpfUHk96bZaqJ4W8zg8deFCgJuiwtG0BJYtfRm53uRHoNlpw3pwd2SES1j0Gr7QeLvJM3aO4Cxl-yY9NE7nrQkFTnoQhOPyIqIKVvSQKJb3cMcCK3zD1UfHxkdkZRYI7J0NWUYOFidxNBfxqyqu1dhdYRWw1m58DSNbV5-W-MDHsNqbaJaZ3uQ-Caqf4xsqWkcuDv6Ob-q3Z7WbqV_6jYDviaP4sEyVQn2Y5pYMqR7IHLDUJRY4nr3-z7eqJ8wB-NiXj4g_KbemSrp9D7SFGmkTLA3M5STUqHevitaLPZyqOJ1W4BRvjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=NMl1HEJzmToYVGG8loGkOY-D9_-qVOXlAXpfUHk96bZaqJ4W8zg8deFCgJuiwtG0BJYtfRm53uRHoNlpw3pwd2SES1j0Gr7QeLvJM3aO4Cxl-yY9NE7nrQkFTnoQhOPyIqIKVvSQKJb3cMcCK3zD1UfHxkdkZRYI7J0NWUYOFidxNBfxqyqu1dhdYRWw1m58DSNbV5-W-MDHsNqbaJaZ3uQ-Caqf4xsqWkcuDv6Ob-q3Z7WbqV_6jYDviaP4sEyVQn2Y5pYMqR7IHLDUJRY4nr3-z7eqJ8wB-NiXj4g_KbemSrp9D7SFGmkTLA3M5STUqHevitaLPZyqOJ1W4BRvjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفتم قبلا یه جایی دیده بودمش‌ها!
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101475" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101474">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101474" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101473">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moV7tDilBjtXyFEqvhPj032xToY3T30izzsjrRxMIPDYbxqmmEz6JqQMzS8zXVtdlfFHjnQFMQwavudCWvRqDav7fLLzZ8CvclRTAHPyJukdsOpFEMk_qp8gyta5Q496JRUnrmkufRs7A-Dc1AvJNXSiBxta8idTPXejCsORYMR_i0TEBBdmgGZ8Hut45A-bLeokUDmzj7-n83ofdH7IEG2MUkvjnMq2k_Zy0F6iHG7kCQ1z5NiNy8e7pdTc0n2BAmELLcmDcCxjoRLVFFBgOfMS_bXYpW0yaiqBYdUdWXrG_C1_QCtiFcKz4ag4pizVaaYyIEyupAYMztzEhGPsdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101473" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101472">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=MnIGa9tJS1FdsYzkYhWd2J8eQn0oQuk3KnCFjA_mtKYG9-x9j3iFOmqEb-72nH2-4y-dh-Pak9fhkRhk70jDi6E3rCEaHCwk5DoAEi81fPtDnVeH90x7thzfkXkvdizyqNprfRrZyJDcb_aytYTWYCp49oqxrNvY7Z-izGjF7LOThYMXl8arAp_1LT3MYCW2fb-w1xf6J6rUJ0iKeV3Bi2StUkMvO9DbLU0RsrjEcd8lNGshJEVlqNNSgvQOTCmlb8zZmSJDiADF82AmcG16KYjWFkFnOY_90So9raiy1GmSqG4BVwefULJE5Cd99qSvBOUtRofEpFHuaeHxZbf6tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=MnIGa9tJS1FdsYzkYhWd2J8eQn0oQuk3KnCFjA_mtKYG9-x9j3iFOmqEb-72nH2-4y-dh-Pak9fhkRhk70jDi6E3rCEaHCwk5DoAEi81fPtDnVeH90x7thzfkXkvdizyqNprfRrZyJDcb_aytYTWYCp49oqxrNvY7Z-izGjF7LOThYMXl8arAp_1LT3MYCW2fb-w1xf6J6rUJ0iKeV3Bi2StUkMvO9DbLU0RsrjEcd8lNGshJEVlqNNSgvQOTCmlb8zZmSJDiADF82AmcG16KYjWFkFnOY_90So9raiy1GmSqG4BVwefULJE5Cd99qSvBOUtRofEpFHuaeHxZbf6tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
👍
حمایت رودری از فران تورس در جشن قهرمانی تیم ملی اسپانیا: "شاید بازیکنی که بارها و بارها، ناعادلانه ازش انتقاد شد، ولی امروز... امروز بخشی از تاریخ فوتبال اسپانیاست!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101472" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101471">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=DyoBS-wb2zwPnxwcwGZ5NxNjBkGXcwnR2MJKXrSQknMItlIxAH85gP7Ro5--QwjBrASoTCKMh_K_1Fhn-5V_vfsnP4_KAbDzPuaQbgKr-4jTYZktrcluwDwXAB2JRDZqk7pUC2gxSBAK6JGBSHAktn8TQJNNAl-s_9OCI_yHYKkU3GeFDxxGYAYtRmzy-AfCzOOdKn2513COCNY_DTaNwvA4oZgwuJTNju8o5yD9pAwqAd0dVal9TZn3wpi8hkIb8gwHAf59xZjlFPdOzvdsaUXScPGsEpagjugmaZiv1v350d6CqwvQuAOEarhlRtluyOR8xXCTnnP_gVeperyZQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=DyoBS-wb2zwPnxwcwGZ5NxNjBkGXcwnR2MJKXrSQknMItlIxAH85gP7Ro5--QwjBrASoTCKMh_K_1Fhn-5V_vfsnP4_KAbDzPuaQbgKr-4jTYZktrcluwDwXAB2JRDZqk7pUC2gxSBAK6JGBSHAktn8TQJNNAl-s_9OCI_yHYKkU3GeFDxxGYAYtRmzy-AfCzOOdKn2513COCNY_DTaNwvA4oZgwuJTNju8o5yD9pAwqAd0dVal9TZn3wpi8hkIb8gwHAf59xZjlFPdOzvdsaUXScPGsEpagjugmaZiv1v350d6CqwvQuAOEarhlRtluyOR8xXCTnnP_gVeperyZQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
امباپه و اکسپوزیتو در میامی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101471" target="_blank">📅 19:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101470">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8OQS7ukpDrP8Sb3BWRBDLX7FBgWWepwSvqt4EDJkn0kduTsR624_ULf4WqGEDQucMk6Z6QzCr9sqWBvztyrPeyRnJipkN3OCmWxKGMvoP67OhG5si1CPa60QSRUzoO_Mc5IqvL4EXWJ4qQqY5-7zHqgClma3HZm16ALbWvfc1q8mLSiWzs-s5QK_duJsa1J7p8VbhYqcb_JLeTxHqzbkeCf4CioITBX8jWvWRFejy-8IyPN0LiBqchXOxbyOmWwdJ0nUD-btkIG9GhnNGoptQtdTt5eQSZNcOZqD8JGlnl3-hDq0XN0Sgmkum-gX9GCABwP3JywzOkIzP0mdCHhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه حدود دو سال پیش با دختری به اسم فاطمه وارد رابطه شد، اما بعد از جدایی، فاطمه باردار شد. اولیسه اول پدر بودنش رو رد کرد، اما بعد از تست DNA مشخص شد بچه متعلق به اونه. با این حال، گفته میشه هنوز مسئولیت پدری رو نپذیرفته و فقط از طریق وکیلش پرداخت نفقه رو قبول کرده. فاطمه هم پیگیر حق و حقوق خودشه و این ماجرا باعث موجی از انتقادها علیه اولیسه شده؛ تا جایی که کامنت‌های صفحش رو بسته.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101470" target="_blank">📅 18:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101469">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=nk17FJuh7vLpfNmDnyVnsJZqOaihIeFV84OHpKI8zM4G3owQURXz3Xfp5LBywuuO6jvYIm8ox3Ci9BHKsqI5w6oqcxzfkvwnpPmO7IjbLwFX_3wVwThOMXHyk_EC-WpW1qt4c9FIox4q6I5I45LDDL7wt89XB1COGXXSidIJ30mnR7CAKnliQNXf-h7gyZemgaM3lLMZJ8JPxacCCKwl1rid4kmF3bvuJqRl9ecwmLnK4TCCn74e_Vsg1sieAPDCVcbSMFVpAlM6bb6NjPt6x_aeRnFqCgB-jfba5nKTaLOzYwra-IIGcaTT379G5qrHCr1Ili_7M5_WcjEA3OHF8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=nk17FJuh7vLpfNmDnyVnsJZqOaihIeFV84OHpKI8zM4G3owQURXz3Xfp5LBywuuO6jvYIm8ox3Ci9BHKsqI5w6oqcxzfkvwnpPmO7IjbLwFX_3wVwThOMXHyk_EC-WpW1qt4c9FIox4q6I5I45LDDL7wt89XB1COGXXSidIJ30mnR7CAKnliQNXf-h7gyZemgaM3lLMZJ8JPxacCCKwl1rid4kmF3bvuJqRl9ecwmLnK4TCCn74e_Vsg1sieAPDCVcbSMFVpAlM6bb6NjPt6x_aeRnFqCgB-jfba5nKTaLOzYwra-IIGcaTT379G5qrHCr1Ili_7M5_WcjEA3OHF8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کنایه‌ریز دیشب رضا جاودانی و عادل فردوسی‌پور به محمدحسین میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101469" target="_blank">📅 18:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101468">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqBxJ_l64eIKeCCGB6NF-se4qoLH2ZfPa--RJKD2Cc0CgA_vmnZ_JYBZITJBfZc-cTycd7Zk6zzSWnB9f6QKsscEJ2QoijjOJShNEz8b58D55jmulPQi0fKL7iELkmw9-cpxDPxLiKdOCNHEAYRwLwqKYkdMpurfaqkggb7yRJz955vz0qzXjWvOHGtvtqbQ8JG37ZnZcMf1Qnzmua3e20nW_PgpWbKOWpmA66T9rAWZYq4oeWQZAfrUVIqehf4CwO6lcRVEOgrWlB6XnixGaUCbTbrrwpHOTaKsSCD4OrzPNWUb6oVn2mvNlOS7ahMVOuwaT61ID1aYgy-8BqkFxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه روی جلد FIFA 2027
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101468" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101467">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1o6a_Ek2wS4nlf2I3cR9XOLI3-huJBnrMZnX2Ab88IA8nJ7L54OowccI1lpiEUCgIB3z4SBA5Em9ES0YEQOfVRSRnFl_LY7GlU1UdSB_WlMIMeLt7idgcY6LisjSF5lTZsHlZpe1_ghPCz1HrzLG5_tvf6q-pRTzZzuQhU56XUjyRAWW5Fibqa6lc15Nm5IJmTC9xqIlh2RDiHlIvLPXGAgXfCmSmE07sNb2GgaK65ZNxnH2dIqxVKwSFRQTrg3JWWdTCYklnnzPZ016vIFSt91-JQiJjXb9MdgLeXlrfh68rfdgF5q4VJByfetSgGI47VFm1bLyUeUJXPtEo3RTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتونی تیلور، داور انگلیسی بازنشستگی خود را از داوری اعلام کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101467" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101466">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDs8azirM_BCutyTi_zHU8Q3qMSomLZyn2gx0cYecP-oeopm0lvxkJm70d3sD4jsWgA2A-hqo_msaIg4kwTacQWQSMWTjOikJQacawDZ5HryiPJdlf4v-3UVi0HECilXvL924jujbAbOu9D1BvdQl25nZRYgSAKnTAnwI2mQuhQ7hrDQa_EcrlRtgZigWyyrL-fYa2JtNuDdAGNaWvrlzpDELGJxl6aIsMrm-41RLVZmGjzimY9a8-Tl-IWNGK0yEjmkBkeUypdNPWimLc-xPeS2-4MPsTcF8dYdlKPwAtkqqQw5GATeJhj5ZuD0HmEiHFdAyw-PsxupITEDxFE2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ماتئو مورتو:
الهلال در شرف تکمیل قرارداد سامرویل است.
الهلال معتقد است که پیشنهاد بی نظیری ارائه کرده است و امیدوار است در ساعات آینده همه چیز را به پایان برساند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101466" target="_blank">📅 18:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101465">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcvmSb1yBYbWBu5EiwtMOu6k72Om8-ys1KoREHpawa0bvGMNb5u6zx1rr2RgCn4owyQYFV-2YKQeQIRU7DQEfndZcoviUMCoENjsP_W4OhjJw3rhwZSFD1Sy8o4ULSY_zoUdWAjvSA1UUchjEAElz0_oryeU0G1UKnTEWcUm3NkzuefaHnmDL2eUAmyVMatR_vRR4FZkcCe0cWAuTmNpAUHDk3HYrALNHu_YHk12yZx0jKFk9inlNnpGAsbZkQ_SlpxNGZQ7XAfXU9Ti75uqFdtSjPu5JqBrDJW2jx9WcgLgmF5m0-9Bfk8lsgslpEd4I14amQHJZ7i34cIF57elLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
تیم‌قلعه‌نویی پس از درخشش در جام‌جهانی با دو رتبه سقوط در جایگاه ۲۲ جهان و دوم آسیا قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101465" target="_blank">📅 18:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101464">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21557090e.mp4?token=XPLP-VlZm6qddldGHbGpPVQ8NsbDvMjZOYPdpvJSTQnkpoVzb4-NzRAfHlV0Ezv6uo8c54NKSLhKDoQpsAunQFHPFV3ATO4tdhouJI-EGtX9je7ntKfmR7g-VDOKDia2uNmJw0uAKMDk0Vx5-vZ_OiH_2VMU_xIxLgTEAb6aTBugqKHG89cxbkYCGYhJiolcgVDei_egnbprtGCFDTRoR-kVD2H8QR1kGzkKBYUWIXM85I-k0_68IwFWcKftyLtqZ-egmRjNTooh_FjyBzjzxFOmbBLZvyIz5xEgT1RfT6kYlSUkwF4QDv1Kge1rL0_huN52tWcviOfANAw_33AFFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21557090e.mp4?token=XPLP-VlZm6qddldGHbGpPVQ8NsbDvMjZOYPdpvJSTQnkpoVzb4-NzRAfHlV0Ezv6uo8c54NKSLhKDoQpsAunQFHPFV3ATO4tdhouJI-EGtX9je7ntKfmR7g-VDOKDia2uNmJw0uAKMDk0Vx5-vZ_OiH_2VMU_xIxLgTEAb6aTBugqKHG89cxbkYCGYhJiolcgVDei_egnbprtGCFDTRoR-kVD2H8QR1kGzkKBYUWIXM85I-k0_68IwFWcKftyLtqZ-egmRjNTooh_FjyBzjzxFOmbBLZvyIz5xEgT1RfT6kYlSUkwF4QDv1Kge1rL0_huN52tWcviOfANAw_33AFFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماممممم چه حرفایی علیه مسی و آرژانتین میگن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101464" target="_blank">📅 18:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101463">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">😢
تمامی سفرهای استاد اینفانتینو در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101463" target="_blank">📅 17:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4ba1VhD2iGzdlO0CD2YXypc_nsdiiCJkbqjPBecIb8SqS7tOpEuJPTnp3wgX65BSqQ27s6tfe5i6GOlNniG0pCuVgegRWvWV3pfzXTqiEgU66ULRTSSCh9j6uowFPlbmGJj0c3f0KyVDcvhqzQP2VQjmmfLoEK-ZOjbBPHQYK-790a745viBQXxwiqjol6PiL6pGtGfPVRx4pODBUd8O-fQjJPdBae-Q07nfe60mxdJLF5Cbn4yHs5dAIxZVHngWSL9c14UTsYw6GFOcJEanoekqeD06oy4iQXs1IfQ2ButBirZhuJX8T3zFPB9Orheo9_ch0wf2Me4bd1OsPDhRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: استون‌ویلا با ارائه پیشنهادی به چلسی خواستار جذب قرضی گارناچو با گزینه خرید در آینده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101462" target="_blank">📅 17:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101460">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgSp448z427zscdpzedKR3IqhMerLIvl7Aht8iRXBtREVMVP12p74ccGo_j1JoC4Lz64-TCEBTVFeNhXoDmltp8GbcqkH_qfd4cNIMZzGfB3l6BDVnwgkpJ8QHF1xb8YHub6EDpEN-SnxrYJeBZwMaZJpeJkiG6du5y3PsFd4rv6uPdGx3q_75_fPrzjsS-lHIv4LHn42h9CvpGDnQRYQyJgpRIZFR3N_qQunN7Lx6zcQrJjUu91wDRjQFERkbRfRq9gdSpm0sxtRyRJlH8OIGp7FLMpbvOkIJygtwSE9sv1c5HreDdRUkMBlEm14lxG6ZGKwW5aS7GkL9P5bBj9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPRwcjqapTMwaJPAV6cdXWvGcm3krQEsRCBDp7s1nEKyA3de_uiVpBQAT8WRODSpgY-O0GkJDHbbBy_lJ-WfyIikF_z-_92DrbeQ_5FMZ6RQv2Fo7B5ijII6yq_UhiyBOPsanSBDq_Rwl-6w2Mqbne0kS7MWEjOdjKMjFXAoOYpHnLPPy-7byT6pDnkDSVlGAIi1hXgrx7xMEscFILrHtp-XeyBr9KljVwrBsZEfgEHnTwFtcPxKWP-g0Obuij3LwIBJwtRgNv8CRmSEHd_GClI-otuSL6G8XcSb0-di8TWb5VQU9omhn7jOwGGXPuPjF0_PNkMNRoKTzSV8nWGV7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصور کن ۵ سال کنار یه نفر زندگی کردی و خاطره ساختی، برای آینده‌تون نقشه کشیدی. بعد یه فوتبالیست با ۵۰ میلیون فالوئر، شهرت جهانی و حساب بانکی چندصد میلیون دلاری وارد زندگیتون میشه. فقط دو هفته طول میکشه تا اسمت از روی صفحه چتش حذف بشه و جای تو رو یه نفر دیگه بگیره. چند ماه بعد، تو از پشت تلویزیون داری جام جهانی رو میبینی و اون، کنار همون ستاره، تو جام جهانی از کنار زمین لبخند میزنه. اونجاست که میفهمی پول واقعا همه چیزه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101460" target="_blank">📅 17:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101459">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=ppMApLt28cdh8rlLM9NUIrADdSTNZwK5f6xzeRcXc87MDWe7_eWB9CTm3Sr1SW73uaujuI6_lzlCYRhK5MTp_vCs_G9Cw44YAUdD3eq2H9RAsPjQ9dMUo2alAfZUJHNjZTt8g5WJ9CmA06YZpxEuQsAFFPkgjLU5YIwDtXDpGq3Didb6Czp7pgz3ow88aEvy0rTw6HjIcvwKDGDaUbtCHL_FArk78ZYvr4q9_plKXnMTqIzK57Z695ZioaZZr9MteZgVCJuLzA6b-4FGrOLp_JEKd74yRX2eoISdedfS9ZCCtUAs0Zt2box3lRbuigjfzzz1dtfByMkvHWYoKoJzXnQ854bBKt0GKe_d7Ij1DMW1HIo3EnJjSzWATjfMwCgCCJpH-vFZ-b2PDGz-rSCo8kVDUhLQFdDZ_YXZbLWm_hlVn6hezLbbQwxiYbBvmne8_gbcXZRBMT0McYP67BtV-yZ3hkvPEj8NC8x5q5JCZ1CvY06WcBXPmRw_ds8uaGSmEkG5FhTZOjXuLeZll1KukIK9eYthFGi1bnwxzBf-rNb4sQoSLLZM0EkMNSbl3pdXRd6G7X44QF_iA0-t3t2BAonw3DbvyfLKqlmMpBZkuas6mxk9eedAlBeQ_Er-o86DiUhn79RBqM6ylS0OFoiBvrxvNKi078Oj6nwdUIAfvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=ppMApLt28cdh8rlLM9NUIrADdSTNZwK5f6xzeRcXc87MDWe7_eWB9CTm3Sr1SW73uaujuI6_lzlCYRhK5MTp_vCs_G9Cw44YAUdD3eq2H9RAsPjQ9dMUo2alAfZUJHNjZTt8g5WJ9CmA06YZpxEuQsAFFPkgjLU5YIwDtXDpGq3Didb6Czp7pgz3ow88aEvy0rTw6HjIcvwKDGDaUbtCHL_FArk78ZYvr4q9_plKXnMTqIzK57Z695ZioaZZr9MteZgVCJuLzA6b-4FGrOLp_JEKd74yRX2eoISdedfS9ZCCtUAs0Zt2box3lRbuigjfzzz1dtfByMkvHWYoKoJzXnQ854bBKt0GKe_d7Ij1DMW1HIo3EnJjSzWATjfMwCgCCJpH-vFZ-b2PDGz-rSCo8kVDUhLQFdDZ_YXZbLWm_hlVn6hezLbbQwxiYbBvmne8_gbcXZRBMT0McYP67BtV-yZ3hkvPEj8NC8x5q5JCZ1CvY06WcBXPmRw_ds8uaGSmEkG5FhTZOjXuLeZll1KukIK9eYthFGi1bnwxzBf-rNb4sQoSLLZM0EkMNSbl3pdXRd6G7X44QF_iA0-t3t2BAonw3DbvyfLKqlmMpBZkuas6mxk9eedAlBeQ_Er-o86DiUhn79RBqM6ylS0OFoiBvrxvNKi078Oj6nwdUIAfvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
نیکبخت‌واحدی: ۵ ساله پارتی نرفتم و الان دیگه با وجود هزینه ها نمیصرفه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101459" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101458">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=pKfFL_RkIonJ_9EEH13DMjBoBzRSEHh0TlXhwhYJBRkJAuc4vIjo64wufvOCNZn0swJukx2GdAGxMt2ARECcQn3f3Kfa7BBk4Ij50XTfALlaA0atnahWjzZ7UKsdsISTyxs8qTtM8X9_nheVXGegntySpEz3BP-EyPeUtZgKdGWBtZ7KSFAldoTx48JkKOxJJ5HRCXLsw5VIkEeMlb4WCrdXoyKZgQM-wy3R_OhOdOpa_zRHS-FuLvBxkJNGDeYEVgHooWfjt-OrbzMFIF8XD4tJxU77RnRNCyOe7qbnQF6gOzDGLoq7y9BGIIxe-6s8cC3kRvZYIIHTzKN89FlkHY6QJSldcBe7jENyYD7P3ssrUj4WvSQ7MlVJcaiZWxz7j7jonK7gN9B_6z0wxDhV8q_57I2iTxoHPS2b1kqz2MLnH_cX7CcQiBCio6BG_VL0wqCwkxoEXkvm7FwSNkhxquCPmMPtq9WsUduzJBBegMI4vwSJnCpizkqchWgM7-xeW7N-zrziZDESl8EPNAFQ93bNucjn4mv_nUD_w-5HBWaIT7V0ptF7BRFpd3BP1ERKGUm6NSUD7bGQoueR7LsGyjd97hCtttffdeh9Mp0JpwRj49DnWScBycovgSaB8SmA5sN2dAnZm77AFLJp6I8ZCIhnGRWJ-eKYLL0qsShX0gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=pKfFL_RkIonJ_9EEH13DMjBoBzRSEHh0TlXhwhYJBRkJAuc4vIjo64wufvOCNZn0swJukx2GdAGxMt2ARECcQn3f3Kfa7BBk4Ij50XTfALlaA0atnahWjzZ7UKsdsISTyxs8qTtM8X9_nheVXGegntySpEz3BP-EyPeUtZgKdGWBtZ7KSFAldoTx48JkKOxJJ5HRCXLsw5VIkEeMlb4WCrdXoyKZgQM-wy3R_OhOdOpa_zRHS-FuLvBxkJNGDeYEVgHooWfjt-OrbzMFIF8XD4tJxU77RnRNCyOe7qbnQF6gOzDGLoq7y9BGIIxe-6s8cC3kRvZYIIHTzKN89FlkHY6QJSldcBe7jENyYD7P3ssrUj4WvSQ7MlVJcaiZWxz7j7jonK7gN9B_6z0wxDhV8q_57I2iTxoHPS2b1kqz2MLnH_cX7CcQiBCio6BG_VL0wqCwkxoEXkvm7FwSNkhxquCPmMPtq9WsUduzJBBegMI4vwSJnCpizkqchWgM7-xeW7N-zrziZDESl8EPNAFQ93bNucjn4mv_nUD_w-5HBWaIT7V0ptF7BRFpd3BP1ERKGUm6NSUD7bGQoueR7LsGyjd97hCtttffdeh9Mp0JpwRj49DnWScBycovgSaB8SmA5sN2dAnZm77AFLJp6I8ZCIhnGRWJ-eKYLL0qsShX0gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🔵
محمد خلیفه سنگربان جوان تیم‌ملی با عقد قراردادی به استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101458" target="_blank">📅 17:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101457">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=JufxWzflcLxuixyWoffme4B90eZnBCgyUPy6ZQAzwBLRvbPvKtoVcus9gUPZw15QCE1lqOxTCSD0g09OjJIZ2GtWsgOxpk_KvsXdNIn3WD91bigpQqnrg7HoALwUqYGjgQnB5dH6qn_hez_w9NJ8xbKFuqWw1q80zvgkAUoCB2c-4_tjFNRxfimdQyCY47Rc6gEw9oLAoT6_Pue959bYlv11VKw50cZnWtvceGiPVOpchJkjIxGoDik47yqcMhk2AIb2FI0SinjtpVvl0GnHw-RwyqXzfR6A7pf2CSr7eZecNpXKio3tD163kqgPdno_5HOOhV3GVKLW4xO7NghgEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=JufxWzflcLxuixyWoffme4B90eZnBCgyUPy6ZQAzwBLRvbPvKtoVcus9gUPZw15QCE1lqOxTCSD0g09OjJIZ2GtWsgOxpk_KvsXdNIn3WD91bigpQqnrg7HoALwUqYGjgQnB5dH6qn_hez_w9NJ8xbKFuqWw1q80zvgkAUoCB2c-4_tjFNRxfimdQyCY47Rc6gEw9oLAoT6_Pue959bYlv11VKw50cZnWtvceGiPVOpchJkjIxGoDik47yqcMhk2AIb2FI0SinjtpVvl0GnHw-RwyqXzfR6A7pf2CSr7eZecNpXKio3tD163kqgPdno_5HOOhV3GVKLW4xO7NghgEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
اسطوره وینیسیوس بعد عمل زیبایی در برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101457" target="_blank">📅 17:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101456">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=F0djRg2HKcscm-ex3X6DiUf354hZ6Oh_37G7vFG5wq_XqWIc3QKu4xzfqJb3MPwBp6pijoHMAIEK8a9Aa4F4bUG2cr89VzcbIsUQ1Orx4jChrmqiSwYwWd3IU8VT0EYvOO018Z65iHvadZt_x5eVhCCZ2zaXoC_prPuUQhKzTRK0vgLIquq7Hczujr22yJopq4hwnOlErPeBIYxDry9wG8ziO6lydhECMUwvFTEd2YRCmY-UUhJJzB2b5D-7cFT2xSOVzv20KmZwZQX5O3G_hixLlmJtyfLHuxdngg1YzVH-E-qhy-kZTAAgO1iZSmYJ0Lyh7CeIkqZ6xVv1UIYBsn4TxLPhT_JgKgxbgx1Gm_hemVYHIlIhnR88u0PIUDTUBTUglTr0JdSCz2bu0wqHrydGs1JIovGwBjFWfamXFxOgob3Rv_k57lTUvBQ_gde03kjC2xGjJWJmA1j38qOSzUjMz1toksqVwX5tBOslpnS_UhfhQWp1KHeW7xJbm2Fvx1YNSGpSnfdPZ16p8GDSvl8JqlXOOrI-w8LxNRVmvrs_YhIlxGIECsiNWmywrXzACBR1tfQ51r9bBgI0b6bYpFWILDIOsdCn8tUH9gj_ZIqXjBNxguByRZrmRYbbybrvVP3_-u7ENPjWnbSdr7oyqeD6VD_Di8C-AhmyalliF3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=F0djRg2HKcscm-ex3X6DiUf354hZ6Oh_37G7vFG5wq_XqWIc3QKu4xzfqJb3MPwBp6pijoHMAIEK8a9Aa4F4bUG2cr89VzcbIsUQ1Orx4jChrmqiSwYwWd3IU8VT0EYvOO018Z65iHvadZt_x5eVhCCZ2zaXoC_prPuUQhKzTRK0vgLIquq7Hczujr22yJopq4hwnOlErPeBIYxDry9wG8ziO6lydhECMUwvFTEd2YRCmY-UUhJJzB2b5D-7cFT2xSOVzv20KmZwZQX5O3G_hixLlmJtyfLHuxdngg1YzVH-E-qhy-kZTAAgO1iZSmYJ0Lyh7CeIkqZ6xVv1UIYBsn4TxLPhT_JgKgxbgx1Gm_hemVYHIlIhnR88u0PIUDTUBTUglTr0JdSCz2bu0wqHrydGs1JIovGwBjFWfamXFxOgob3Rv_k57lTUvBQ_gde03kjC2xGjJWJmA1j38qOSzUjMz1toksqVwX5tBOslpnS_UhfhQWp1KHeW7xJbm2Fvx1YNSGpSnfdPZ16p8GDSvl8JqlXOOrI-w8LxNRVmvrs_YhIlxGIECsiNWmywrXzACBR1tfQ51r9bBgI0b6bYpFWILDIOsdCn8tUH9gj_ZIqXjBNxguByRZrmRYbbybrvVP3_-u7ENPjWnbSdr7oyqeD6VD_Di8C-AhmyalliF3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
زد و خورد شدید مردم بنگلادش پس از پایان فینال جام‌جهانی
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101456" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101455">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=EdWZPzK7vv2oFjoh9dMd2tcTFM6Qm07ITLktC9oLitvwyYwy2itmRsltbkN8tYC56jG5djcpcbCO-o0ri3_vZ6wmC54ASWKHwjRDMSzFfHwTQh43_1Qf4C0R7OKGcR58RfQ4uz9J90mzTWPh0GofgLWCoaQnZRXLfM2zpPS-XQK_Qude9pCJ7nU0j4p_U4avmR-g05PFv4Fn4dqr7rLWyrXJf6cPq1pm33MFe9rWDkZ1P3DdHrU8dLvMK7QEgIhbob1_Of4UQVI5CwR0vtgE_OBt0L15JGTi6n83lgM8cDG7tRuvBRcIl3TVyvwD0D7eDPTuQ1WUoVzV-4BsCmQogw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=EdWZPzK7vv2oFjoh9dMd2tcTFM6Qm07ITLktC9oLitvwyYwy2itmRsltbkN8tYC56jG5djcpcbCO-o0ri3_vZ6wmC54ASWKHwjRDMSzFfHwTQh43_1Qf4C0R7OKGcR58RfQ4uz9J90mzTWPh0GofgLWCoaQnZRXLfM2zpPS-XQK_Qude9pCJ7nU0j4p_U4avmR-g05PFv4Fn4dqr7rLWyrXJf6cPq1pm33MFe9rWDkZ1P3DdHrU8dLvMK7QEgIhbob1_Of4UQVI5CwR0vtgE_OBt0L15JGTi6n83lgM8cDG7tRuvBRcIl3TVyvwD0D7eDPTuQ1WUoVzV-4BsCmQogw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
سرگرمی برادر لامین‌یامال با نیکو ویلیامز در جشن قهرمانی اسپانیا بعد فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101455" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101454">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=g02TMm8pMFhKgSMZonTVhs5F0cwFgcjSeciv9D6RuUBcgVLf3ubc3idcS5MKAp_RrTwfK9zzjeOP2T9PgFXIW6bRC84agALAC82BLe3DLcwzlEjOAal37F2i7rXc2Eh5tLESEkjlK-WuOfcPoxDi-3PGSRd4cx2NOU_j8FXfyX0xg9NWFKEX7TwoaACcMtSuovjq8WJ4fQumqZg1r8WmTHoNIcA_8Z-SxAXcazlQZ2aX-UTDzLHv5oTnBEO-gkHubNPBtFn5oqbnHzAc367DZgJYWQlBJNOA-P5xtNhiMs-e-6II9l-evVJ4J3KYr71lH-g22phRjIALKINHHhFXDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=g02TMm8pMFhKgSMZonTVhs5F0cwFgcjSeciv9D6RuUBcgVLf3ubc3idcS5MKAp_RrTwfK9zzjeOP2T9PgFXIW6bRC84agALAC82BLe3DLcwzlEjOAal37F2i7rXc2Eh5tLESEkjlK-WuOfcPoxDi-3PGSRd4cx2NOU_j8FXfyX0xg9NWFKEX7TwoaACcMtSuovjq8WJ4fQumqZg1r8WmTHoNIcA_8Z-SxAXcazlQZ2aX-UTDzLHv5oTnBEO-gkHubNPBtFn5oqbnHzAc367DZgJYWQlBJNOA-P5xtNhiMs-e-6II9l-evVJ4J3KYr71lH-g22phRjIALKINHHhFXDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی‌کریمی بازیکن سابق استقلال: استراماچونی در حق ما استقلالی‌ها ظلم کرد. نباید تیم را ول می‌کرد و ناگهانی از تیم جدا می‌شد…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101454" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101453">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9k58lLcpVLY-Wlp3wabiira0GvQ06KIttNhZwPfK1J5ipfvJZ4VGXYJiGvrBqZhZj_0z5r50o7FjQw_TcdG-LINpHBoNUnitUaHgz5iI2eyOv10ZMjzGsCGFAO5P0N5VUiSN5GyXxz0XZWux0GZOioZqb3gqlsV8MhSDvrGslR_NB8FsciUO_qUQYZUQz9_zrLZIOv32oPtO_ZyKnT-Xnklj2Fh9jafDfLqsjNDLLef6qROfObDTTVSsFgL0xCUOdbtJSlSVNjeqthqEo21tHJuTajcVqgv717hFw9TufXw2Yz264RsHLkubS-y4u4owf-QcVPUdC5JCgRXao2HMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بند فسخ قرارداد آیمریک‌لاپورت با بیلبائو ۱۵ میلیون یورو است و اگر بارسا برای جذب وی اقدام کند، به راحتی موفق به امضای قرارداد خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101453" target="_blank">📅 16:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101452">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Q94UFBBxud0pkgI_bAFkB0IIgJ9Kgb4t7iO-WWduhPdXlxmW5fqTQ9KVM6IcK-t0il32Jq_WJHaGE3ephEbJ7Ndgw00He-Jb3QW76LwHSbT6Kbw5q5snI3F3U7BDG2U7Jr7IohL88NaYprQosF4VfaZ5xqCVhMfbtGwoFk5I5ZtCkAElspdelh2zE6P2U9kUs2kGhngxy21oUjucl7BCNB0ODkdVZkreJtAglzSrRPQI7IXuzTFYjpzR-6wZjJOIjqS6kADIaP5yGJ21mEsPWe2Or4qrg8aq1lah3SM1GJn5ryCIYPXayH3og_iavahASjIHqK3i66nTXa6E2lPABhPqUeqpBq6FitSz8nmCS9C7IIuJPIEVZtn1sIUOhqSEUcHtDYDBUWxO-9wf6a-f0rZgiXR9FP8EaJU_M296F38y2tg7mhD_VURRbgIJK-sCezFGO3s0TESEWwyg75n3sbkMCjPxyUqufzWCBtr1Xcmjd-sx_2mHUqXdMWJcNISIE5D3hRgWuk7jxbstMZwlr22XZd67Ua9kg4D_5aq64-ek-zDttgR_VH_8K6PtXrLuPJIqE_9y26C3MLUi88DXpqzXb5Rv62wZzx1Xl-XA6bpc3n_ZAvr4ZZUM2bFpzhk2AIih-i9matsSRU_e4dLI3-8EUDU2lJQarPKfIorDVXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Q94UFBBxud0pkgI_bAFkB0IIgJ9Kgb4t7iO-WWduhPdXlxmW5fqTQ9KVM6IcK-t0il32Jq_WJHaGE3ephEbJ7Ndgw00He-Jb3QW76LwHSbT6Kbw5q5snI3F3U7BDG2U7Jr7IohL88NaYprQosF4VfaZ5xqCVhMfbtGwoFk5I5ZtCkAElspdelh2zE6P2U9kUs2kGhngxy21oUjucl7BCNB0ODkdVZkreJtAglzSrRPQI7IXuzTFYjpzR-6wZjJOIjqS6kADIaP5yGJ21mEsPWe2Or4qrg8aq1lah3SM1GJn5ryCIYPXayH3og_iavahASjIHqK3i66nTXa6E2lPABhPqUeqpBq6FitSz8nmCS9C7IIuJPIEVZtn1sIUOhqSEUcHtDYDBUWxO-9wf6a-f0rZgiXR9FP8EaJU_M296F38y2tg7mhD_VURRbgIJK-sCezFGO3s0TESEWwyg75n3sbkMCjPxyUqufzWCBtr1Xcmjd-sx_2mHUqXdMWJcNISIE5D3hRgWuk7jxbstMZwlr22XZd67Ua9kg4D_5aq64-ek-zDttgR_VH_8K6PtXrLuPJIqE_9y26C3MLUi88DXpqzXb5Rv62wZzx1Xl-XA6bpc3n_ZAvr4ZZUM2bFpzhk2AIih-i9matsSRU_e4dLI3-8EUDU2lJQarPKfIorDVXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ایمان صفا بازیگر سینما: با کری خوانی‌ام دل خیلی از استقلالی‌ها رو شکوندم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101452" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101451">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101451" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101450">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H86kFiioeIqhm7498LdaVKhgSDFagUfY9q3hQAxtjm1blofZQ1OGNh1ybDznOZeVU-vwXW3SfUzfVhKuDPKfpCFWodu3N52g13hikLDA-U1AcwviP_FctXKRknTZlDWsVJI1_Ax8ntbsBbIs473GfVhuUyckbeXlo4rOgLadOGV5w41mBmmmgLU3OQQ1CTjX-onQFBa_9urz9VdWWZpec9BIrmdAhHBNSS07EXBcKDaVue22mYMPU0nuWpH3s7nEmC70CiJA2d1JYx6SVO8sWAcJhFOKFgY7ZS9qYw8YMIMUT2EIsBNnuMAyO8-nLtr1nrKG-2UeqspXq2SNufzakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101450" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101448">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=fDukOKbHHW4CBg-5r0lLzAYgdNOldzrBOB2_4EW0kw-3m5jCv0yG3ZyNNf-FRnyrOuGG1SOYwvihOryRGawI5mMVxk1-g_n_4HU1i_nnOk54sT9CWgk6a6_4fTdzD5Y_L9mZnKRf3ohhTTg6AMSlVBPPMYXPBrCv9VnrxtrbGSQ640v2Uro5upVM852xekKX-s_J4sjDt0WmAyLSnSaUYeDA1-7QkMsz1OftRWuDQikNDu4bac4obNi5pjkKSBuX0ceJ78jbcyEk3tRxYHNx9iDcb7gv0NaS9QpaxqiwE791sruhzHBlc1j5nygZtDRs3W7oPfogsIHzJ602AYvxtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=fDukOKbHHW4CBg-5r0lLzAYgdNOldzrBOB2_4EW0kw-3m5jCv0yG3ZyNNf-FRnyrOuGG1SOYwvihOryRGawI5mMVxk1-g_n_4HU1i_nnOk54sT9CWgk6a6_4fTdzD5Y_L9mZnKRf3ohhTTg6AMSlVBPPMYXPBrCv9VnrxtrbGSQ640v2Uro5upVM852xekKX-s_J4sjDt0WmAyLSnSaUYeDA1-7QkMsz1OftRWuDQikNDu4bac4obNi5pjkKSBuX0ceJ78jbcyEk3tRxYHNx9iDcb7gv0NaS9QpaxqiwE791sruhzHBlc1j5nygZtDRs3W7oPfogsIHzJ602AYvxtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🙂
خاطره علی کریمی بازیکن سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101448" target="_blank">📅 15:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101447">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53a9000335.mp4?token=e1BJINIjDLvaBC7QxqGB7bpwz_8AOpxQ0Q3mrJRz2cjDITYF2Kdl_GtBJ1fH7F4CaLLBnZTid_C62A_jC9OE18xeG64LS_dIVfeNDjoywzKa8AyGuDmWL3uoTY9CsQZ1Ga1vXD1bQDROTR7l1zgp375MnnSibZhqMF4e58FfABQfgxyWgaS4T0hilJV1IQThNZsAatFYZdo8DUIJDCk2e44E-C7KP1MWi9yxdl9HKgv-JGj0FjJaxzbnncpE7IXB-XBKpooGYZqotPAsKn1zBtEX6IMvmYuVkCp574A9UjfkA7lDRJ5_WzuYhBQBdzLeM4jRuCCxxI77tQmTvvyCu2qc1VQtoyoYqe8CP7oZ-CXTr1ULPe03CPVA3B7WmjDL8lskjsw_c1Q9bxdZpXqVrbM7T8g6pLAJh62a8S6mgYUBzX1MantdYbjeiS9Eort7ztGI2FcAmkpvz_XFXMwrCCukTJUmm2SjX0D9Uhdv9aDwa24d7znsscJbfVq54xbYkju5DyxCVTSmd9L87ZOO07D5Qz_K3HzZX7QXqNs6MbtDlLVyOpD0lBf0xBCxloHP9bIzy8SDkQhVVvcaKjHn-MNazv8aMPh5qqF7BNvwGFQTTW-xtK69rvGfM3txuzP9kIAb863WRD_O-pf_2Dani3_XL5T0ZrFjDIIBuq69qfo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53a9000335.mp4?token=e1BJINIjDLvaBC7QxqGB7bpwz_8AOpxQ0Q3mrJRz2cjDITYF2Kdl_GtBJ1fH7F4CaLLBnZTid_C62A_jC9OE18xeG64LS_dIVfeNDjoywzKa8AyGuDmWL3uoTY9CsQZ1Ga1vXD1bQDROTR7l1zgp375MnnSibZhqMF4e58FfABQfgxyWgaS4T0hilJV1IQThNZsAatFYZdo8DUIJDCk2e44E-C7KP1MWi9yxdl9HKgv-JGj0FjJaxzbnncpE7IXB-XBKpooGYZqotPAsKn1zBtEX6IMvmYuVkCp574A9UjfkA7lDRJ5_WzuYhBQBdzLeM4jRuCCxxI77tQmTvvyCu2qc1VQtoyoYqe8CP7oZ-CXTr1ULPe03CPVA3B7WmjDL8lskjsw_c1Q9bxdZpXqVrbM7T8g6pLAJh62a8S6mgYUBzX1MantdYbjeiS9Eort7ztGI2FcAmkpvz_XFXMwrCCukTJUmm2SjX0D9Uhdv9aDwa24d7znsscJbfVq54xbYkju5DyxCVTSmd9L87ZOO07D5Qz_K3HzZX7QXqNs6MbtDlLVyOpD0lBf0xBCxloHP9bIzy8SDkQhVVvcaKjHn-MNazv8aMPh5qqF7BNvwGFQTTW-xtK69rvGfM3txuzP9kIAb863WRD_O-pf_2Dani3_XL5T0ZrFjDIIBuq69qfo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا جهانبخش: در مکزیک زیاد بهمون بد نگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101447" target="_blank">📅 15:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101446">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=MEJ7exygErkyjO2cPn-LMnU6oa3goN6hu3J7cnTZ2A2Iutw4TrU-voFqeFXDY4yIjECoTWQJgP9_o_UyHgvK6JkU6ztFriUqVSd7xKn3EHVZQdJSCFqxOgRKOodv7EKg5tmHCfP8DSBa5XkZ384bm9WEwEQw96M6xsqhbkgAV1_EaYNGbFEkBPr4WVB_rmDpB7LXSrRGYze123yWpC3W5jEsMh2wHFZ8ZX_JMouOWzAxjYMEA11I8mu9Gh82XxMVZcYjqwZdxdJS1dCIYM6w-sSHsTld8bWor3SG1HqO1oWGuVBehc_08bfpPj9k4G7C5t7DR3-ku5jBgdlA78O8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=MEJ7exygErkyjO2cPn-LMnU6oa3goN6hu3J7cnTZ2A2Iutw4TrU-voFqeFXDY4yIjECoTWQJgP9_o_UyHgvK6JkU6ztFriUqVSd7xKn3EHVZQdJSCFqxOgRKOodv7EKg5tmHCfP8DSBa5XkZ384bm9WEwEQw96M6xsqhbkgAV1_EaYNGbFEkBPr4WVB_rmDpB7LXSrRGYze123yWpC3W5jEsMh2wHFZ8ZX_JMouOWzAxjYMEA11I8mu9Gh82XxMVZcYjqwZdxdJS1dCIYM6w-sSHsTld8bWor3SG1HqO1oWGuVBehc_08bfpPj9k4G7C5t7DR3-ku5jBgdlA78O8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👤
محبوبیت خریدنی نیست...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101446" target="_blank">📅 15:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101444">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItpffsBFCZ31xKwOASRU7f3QHeK0reUvXoqq-druTu2hUpvtj__eNXoweTFM5iPIwxksTOf8FuLQVxafe-0oHVDjLXhg8PnuIAtKACQIZ_NoyheR38sbfnVaXk2Ol70KrAQM9TlG0VrRT9cH2UPOS7Q6flWb40gnWzTCfzza89fbCPN8nKD1QjLPuN6-yVQKIPr6MT-DEqzxXwATP0wWpZTS_thGPgdjecjoy6v9rmNv0oNBiZWx_aLfYDgbXOUvFPxx2wcB8Kcfk48jLSUxAWAUnK7IY5aLbwZ01rtcOMU3U4SoD0ID8SQSkLWToPA0RHpQvb0Fb0caLWJKD8Jzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
علیرضا کوشکی دقایقی‌پیش قرارداد خود را با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101444" target="_blank">📅 14:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101443">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=DMgX8Uh7p-HIhQUdyi81aHCn_4joQi01d_ss9iaBOxHQ30_jYtPihIGXC2XQw3fpgg1MDMYstEAZ5K6oGZ7-QGfmPKAyMfdih3cWDeCfM19OTLhAz3HsNYSzniI9AqmFo-3gUsQ_CvsqVzfbXsNEWdtNep_WHihlYYHXf2naojQH5BxhicDU4F2_-oCHPpnBisVMNF1aDjkT70QHvvLYU3rR-zw3PAFhNjtUxDajVTKy-_JK2-uHYwfC5h5KZxsUIifTpDj-nspvN5p0Y9xFIjm_JdXGYHsaj05Br4w8JZBiQOQZtT9HXHFQsfmPtGnhSlXXLS_l1yq8PHB4afMT0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=DMgX8Uh7p-HIhQUdyi81aHCn_4joQi01d_ss9iaBOxHQ30_jYtPihIGXC2XQw3fpgg1MDMYstEAZ5K6oGZ7-QGfmPKAyMfdih3cWDeCfM19OTLhAz3HsNYSzniI9AqmFo-3gUsQ_CvsqVzfbXsNEWdtNep_WHihlYYHXf2naojQH5BxhicDU4F2_-oCHPpnBisVMNF1aDjkT70QHvvLYU3rR-zw3PAFhNjtUxDajVTKy-_JK2-uHYwfC5h5KZxsUIifTpDj-nspvN5p0Y9xFIjm_JdXGYHsaj05Br4w8JZBiQOQZtT9HXHFQsfmPtGnhSlXXLS_l1yq8PHB4afMT0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عکس یامال روی پهپاد انتحاری شاهد قبل از شلیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101443" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101442">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i22rOpTZsXGT8fJxVnaAQWaVIPlF7_rLppgt41yaWAqV149C-jVayl3LvDZVc8FNRnpIojUJ-LkopAYrjhEBSzkKVyIdx3Mx8R5JUTJoDJmESp-F2YjOEaVlorjjBsZGxnwbPtUpP5FeW8DkXLNKlERRP8mYHxSBH3LBcYMln6o348ZX-t3piDpE3zEf4attKdb6cvy-MmPHXl64lVqd8yWBuqqILXzYO81_8tzmvJQoQHCJgfEbl6rtaKzXyrMxhmqYyk6XXFBnQykibtWyLL3X2IlVUwlppkr5eKulb3mS-nf_i6wvxXo0iVBkATHd979vGzSG1v9Hq0D9f4xeCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رامین‌رضاییان با انتشار این استوری تقریبا جدایی خودش از استقلال رو اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101442" target="_blank">📅 14:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101441">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqQJTnZUf-LcO9fuL6MPCpUL4q5LTXkgdbME1B8brTHNhMQj_bwgNshoni6rq40r7q3PdLTH4AZhrnefyzh92xXbtTv-gOjaUvzirzd0khGnzZfp4dF9d8ZXThDzWQFWYz_VnziZzx-ZSCtSDbnh5PlKQhj7VRTtipSG1Lrzo5hlQsM-h9r2hmmNbUJNx5dMn3hDOtZlMizLdd67NTmGv0biYl8D31LzHPvmm35-92Yeg0Gf1cG6XvRIPSNBz2eAdrS_a5QEKcqPs8OfF913cfoguVAxQo0SRf9H3Z8vNJ7Aele6uClGEBI12aB9C96tMDndEKYgpaSj8j7O7JA1ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🔥
لیگ‌های بزرگ اروپایی چه زمانی آغاز می‌شوند؟
🏴󠁧󠁢󠁥󠁮󠁧󠁿
[31] روز تا بازگشت لیگ برتر انگلیس باقی مانده است.
🇪🇸
[25] روز تا بازگشت لیگ اسپانیا باقی مانده است.
🇫🇷
[33] روز تا بازگشت لیگ فرانسه باقی مانده است.
🇩🇪
[38] روز تا بازگشت بوندسلیگا آلمان باقی مانده است.
🇮🇹
[33] روز تا بازگشت سری آ ایتالیا باقی مانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101441" target="_blank">📅 14:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101440">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=Fj0jrvmMZcWJlJ8klqqC5AMEPNxNymhhszfknSaVqKY3P1DRFm-xp2Qb75AEQYfa4iR1AVzNmOds2g22lF7pWXODvLoSfkiYneKvvfHPXXXoyQgdyn_4ILk-7RbmDj3TQDaCm558r05gr04h8S5wYG_U63PPLA5np6T4pNwNQF9OtsUlDDvjzz0RsNBLaL2pZoHGru-SqKxmPIPEq7PWsYU3jJAJRQDko5IdLia65psuBrlDvwlztv5gLJqSoEh4PUwNoRdpx7AaGhxCmzAz3s0VZnMBaPVLWtf0Sg1FU81wl_j70aFw7-3fGkZi7P-HrdWxa9rm1tH26jTfMIw-uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=Fj0jrvmMZcWJlJ8klqqC5AMEPNxNymhhszfknSaVqKY3P1DRFm-xp2Qb75AEQYfa4iR1AVzNmOds2g22lF7pWXODvLoSfkiYneKvvfHPXXXoyQgdyn_4ILk-7RbmDj3TQDaCm558r05gr04h8S5wYG_U63PPLA5np6T4pNwNQF9OtsUlDDvjzz0RsNBLaL2pZoHGru-SqKxmPIPEq7PWsYU3jJAJRQDko5IdLia65psuBrlDvwlztv5gLJqSoEh4PUwNoRdpx7AaGhxCmzAz3s0VZnMBaPVLWtf0Sg1FU81wl_j70aFw7-3fGkZi7P-HrdWxa9rm1tH26jTfMIw-uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
خانواده سلطنتی اسپانیا در مراسم استقبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101440" target="_blank">📅 14:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101439">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101439" target="_blank">📅 13:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101438">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e455125710.mp4?token=hb62PYEit5lMAUziNPOqADrVVmnRnI-i0OW207qkkn9R2cj4IflpVFVYcoxocjjIiylSbb7_G4ZrcWILuS-v2AbXZVE_wVWCNGzxL10rHr0jJxWI0Su-ZTOM0mXaexCVzY7CLh2JTzNodEhtYNmcXx42zK-Jg_zlwrk1JNBCVXhQHABVHixh62Y5WQ5Id8ui23ZK9jYS52OETHGmqIo_PeFKj-VO5Gy7WrGtyTCGd_39IA__sC5B0Qyh3dsF8kxieC5oOj6o9PfKlABJhA6Zmvi8k2hUnd9WbMkljCDowGQDFj0vjxfokaAX2cH7BzpN0EfyilUfjFCOriVhYRJZbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e455125710.mp4?token=hb62PYEit5lMAUziNPOqADrVVmnRnI-i0OW207qkkn9R2cj4IflpVFVYcoxocjjIiylSbb7_G4ZrcWILuS-v2AbXZVE_wVWCNGzxL10rHr0jJxWI0Su-ZTOM0mXaexCVzY7CLh2JTzNodEhtYNmcXx42zK-Jg_zlwrk1JNBCVXhQHABVHixh62Y5WQ5Id8ui23ZK9jYS52OETHGmqIo_PeFKj-VO5Gy7WrGtyTCGd_39IA__sC5B0Qyh3dsF8kxieC5oOj6o9PfKlABJhA6Zmvi8k2hUnd9WbMkljCDowGQDFj0vjxfokaAX2cH7BzpN0EfyilUfjFCOriVhYRJZbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
دیس فوق سنگین ابوطالب به قلعه نویی: ما تو غار کنار عادل فردوسی‌پور هستیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101438" target="_blank">📅 13:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101437">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKbckhtL_yzQZ_OPUIV13FoJSOijOhDED7PGtsGdo3l2vswqFQu0hGTRamcY3hhT3UCBFXfFLoo07k2rnp7oX0EIUpCySQAxlsYdEMMIBR7esrNXVlcJ948y9io1k0UMRYvHZshsVQWGKHKvqEPDmrYhh4n5QVk-wrOJXlX-Knzq3XprzFWLZy6fvQPUK68qXd844pwo1DcmSuwEw2G5vqxJmuail8jvqdFtJ4ut__iyRIeUPJHk4hH32PFQWLJshY3M_b7AwLcA0B2BvipTvUUeTv_NGV8Vqi42JfBGONzp9mMrLkSkc8UW_tqzkh3C_VMKtxu2u5bAQ9whIxEk-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101437" target="_blank">📅 13:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101436">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj8pK3Stww_YrPUM3iwUr7fpdGpqcuBmqBRGEtladbmOxsPgjKQwYXrjFzgeLxzviUzJVdlr-5pm1-oTTzZqG5CNEVuRfYL4d1fr8NTrKYfmjmZQDYiP6uV7AyTVXhXUnKCy7UyHgZ9ABRV1LErt-d8hf4V4EjHFtopfpQ1wIvxwg7biCQp3VMaJ4AlbvzyTyZOUC0j1JBEG0u1UXINn1jsCKoL4YymyaMpJXwQbt3H8s0ogGBMnhU_O9-p_nf3HJA-3ejo-men-lIR71uE_RCDhSlh1aqEdrokPuKzunnlg6WCptbchxmDyM4exHUxPpbfPcbSI0kx5wxfRTVKVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
جسی‌بسو بازیکن جوان تیم کلوب‌ بروژ بلژیک به باشگاه بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101436" target="_blank">📅 13:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101435">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101435" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101434">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5cbab8fd.mp4?token=VSRsO1WpEoqJ7hTxJgXfDf7919QmqCHqQpct49MVyJPpx6wEZu45IVniWoWpyO51BaF8x8jarVBP8BuY2koYynN1ASkxz2enRJeE7sWTfV6zXxnZsapR6M4Xlcjy9m_g2Q5r5yEcOWpqJzFfAsKhwmxBYwAl70m75m0T8z5SA8skojL5l3Be1XLDyjrStQkRx8dtvNGmmbOx4s63jYu4AFfUeSYivZRt7sHHgi9ASXfft_2gI_5wFbQveqkd6Axfqs4oUPr9Sd7tG9jgTmO4hR1B5KdnCqE8LlAj4eh3a0ThywmjgS1tATjWd6QFmgUMYqyo2sNRzc8utpW_I5yE2i_z94ZhjgNOZ9Hqd5CvmezoV9GUsOMO2-dWSgRwnKqr2SKB_eVlJIo7EXL61V56Q_kGml1Y699Z6MmN7v6i7Cp66reJnPvJiAUwA6HBSxH0Vnf5B5wSbhHt6XKSgSvbAKf-a2lkyHxfOr2w8wWCXGnhIwXTp0b9leOh9hnpdNWe-mopnGvUkziwtnQ9JhAv6MaSCXXGrK3FjbDoAddl5jWoST9mwGnrqEBlEZ8x4aS-Or_CFx5QSGlAykCAUcWO-t9v0o-nEh7v2EKA9yIq_sD7ouOviwAL6T7QprH0ETLbpMZZDvwiCHtdOOMrR2DxEysw_xCv8qcxxRnLI95HpjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5cbab8fd.mp4?token=VSRsO1WpEoqJ7hTxJgXfDf7919QmqCHqQpct49MVyJPpx6wEZu45IVniWoWpyO51BaF8x8jarVBP8BuY2koYynN1ASkxz2enRJeE7sWTfV6zXxnZsapR6M4Xlcjy9m_g2Q5r5yEcOWpqJzFfAsKhwmxBYwAl70m75m0T8z5SA8skojL5l3Be1XLDyjrStQkRx8dtvNGmmbOx4s63jYu4AFfUeSYivZRt7sHHgi9ASXfft_2gI_5wFbQveqkd6Axfqs4oUPr9Sd7tG9jgTmO4hR1B5KdnCqE8LlAj4eh3a0ThywmjgS1tATjWd6QFmgUMYqyo2sNRzc8utpW_I5yE2i_z94ZhjgNOZ9Hqd5CvmezoV9GUsOMO2-dWSgRwnKqr2SKB_eVlJIo7EXL61V56Q_kGml1Y699Z6MmN7v6i7Cp66reJnPvJiAUwA6HBSxH0Vnf5B5wSbhHt6XKSgSvbAKf-a2lkyHxfOr2w8wWCXGnhIwXTp0b9leOh9hnpdNWe-mopnGvUkziwtnQ9JhAv6MaSCXXGrK3FjbDoAddl5jWoST9mwGnrqEBlEZ8x4aS-Or_CFx5QSGlAykCAUcWO-t9v0o-nEh7v2EKA9yIq_sD7ouOviwAL6T7QprH0ETLbpMZZDvwiCHtdOOMrR2DxEysw_xCv8qcxxRnLI95HpjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🔵
باشگاه استقلال با انتشار این ویدیو نوشت: برای بعدی آماده‌اید؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101434" target="_blank">📅 13:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101433">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALZXaFfU6Lj7uiurzK-2ZJZ8oFXIaO6uxCakCXFzQCPuYpzuyDA-K2rmxWJ0tOUwhVjBSLm4VX9RGAnCaJMtU3WWNsV60Vr1jMpuBNikQiroQO9DQB4U1rSjbJBlr-z2UKvlabSS8tgXbtyXtnmnC31i-Ajz9Hap14Brhon2wTAUaqUpZeHq0NUrGDdaMTE00mnKi6apJ4cIUMnkvY8xG0PXQEQR0vl8k1Dp-HqufiUOWegdN7geEG9jQlrD3BiZv-XAX5ANSm_lNvUu73HkT7AjTppuxDq6CNWttwHhPFdSMV5uAdsZxm9yGH6aVC_N_BssaMgC55PEe0z2-fU0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
🚨
نشریه(L’Équipe): رئال‌مادرید بدنبال عقد قرارداد با فران‌تورس ستاره بارسا رفته
کاملا جدی این خبر رو زده
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101433" target="_blank">📅 13:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101432">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7351cc80a0.mp4?token=vjxkIGaipM50-M1w8C3RuV8onLLJ2DaEK64bBW929JsfegQP0t6DRj7-4F6VGq9YTC7WImn9-FahNMyDDY0uOJ0th_MH3Mb9hjgI5cD49VY8o7PRIcsWMhamC_AbE7Bo7ioo-8BWDdFz0Fcl0EKLexbwaQfNYvNKYrsV-dTZc8TA44Ww3VovhkX0Po_Y-2AawcP_ePfL9Ktql1eUCGGG9vyp4PIPZbxw4E2UA4Vbwh6SXKTfu3TepS164VpiZG3e_ul2lCDfOb1feioq_0wKjM-YE15hxYjWwVtKvDfEyfP9O_KG8kp2GbPAynhld4jqKl7qHhd5VXWIXujU1PXGvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7351cc80a0.mp4?token=vjxkIGaipM50-M1w8C3RuV8onLLJ2DaEK64bBW929JsfegQP0t6DRj7-4F6VGq9YTC7WImn9-FahNMyDDY0uOJ0th_MH3Mb9hjgI5cD49VY8o7PRIcsWMhamC_AbE7Bo7ioo-8BWDdFz0Fcl0EKLexbwaQfNYvNKYrsV-dTZc8TA44Ww3VovhkX0Po_Y-2AawcP_ePfL9Ktql1eUCGGG9vyp4PIPZbxw4E2UA4Vbwh6SXKTfu3TepS164VpiZG3e_ul2lCDfOb1feioq_0wKjM-YE15hxYjWwVtKvDfEyfP9O_KG8kp2GbPAynhld4jqKl7qHhd5VXWIXujU1PXGvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه نیکبخت‌واحدی به ممدحسین‌میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101432" target="_blank">📅 13:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101431">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edf1184b.mp4?token=QtBybyaS6lvBr2jtg5ZvlYK667nKeRZRDkmomZ9jjHxxxQ5u8BsKlm6fYEOrvgCRRemrmjcmgALuP4J27xle0QLnPRfuSsAQD6burC5dHZklEOx6DOiq7qJd02UP7HiKiWASwMDNIlBtSvShOsJccEOADNheGqJi_T3kWd6UwO2HhX_jsr5yBrVVUBGlcbR203Im3RyhvztdPjoOkVuzPvR9VA38hquy3dBB9YTSRNXTy-aEkGlAwMfHgdxAGGJ89Z2JHYFKCOBr34Eummcgsp9QSvpjoBmQkcXGFcLKzdEnqT5Mh-P5gpJaMppkGri54mZD3mgIyAphvcW3ODMzzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edf1184b.mp4?token=QtBybyaS6lvBr2jtg5ZvlYK667nKeRZRDkmomZ9jjHxxxQ5u8BsKlm6fYEOrvgCRRemrmjcmgALuP4J27xle0QLnPRfuSsAQD6burC5dHZklEOx6DOiq7qJd02UP7HiKiWASwMDNIlBtSvShOsJccEOADNheGqJi_T3kWd6UwO2HhX_jsr5yBrVVUBGlcbR203Im3RyhvztdPjoOkVuzPvR9VA38hquy3dBB9YTSRNXTy-aEkGlAwMfHgdxAGGJ89Z2JHYFKCOBr34Eummcgsp9QSvpjoBmQkcXGFcLKzdEnqT5Mh-P5gpJaMppkGri54mZD3mgIyAphvcW3ODMzzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
داغ‌عشق پرنسس لئونور به گاوی دیروز تازه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101431" target="_blank">📅 12:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101430">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556a03bf67.mp4?token=nouxMWfW5aUxN341-Cfrm-34yRXq4fEwvtUfhho2YB3HoXJCp7hLxaigktCvq92JcLLmgx30WixtmvO2soE_CcIH4mRyPzhCZ305u7jflr0AFOG8vWT5aeafEyLMRsGIBpPumbflzNKBJTSNaoc1IXteDYfRikWiHeot5ovuWXHaKx7HhNPrGVb3H1qwW9Qa-bzIVcJkW4mHHZp57MUxrpw2rT2S16y5i1rME_PEvEHqfZiV9rv1ffuxaxqDcUULO--rF-ZMUA0-Yl_15uYoRv2vqWfRVsErta6iZ7bC66K4zYtjAoe8FUrcBl7QgoyDwpJ5hivph2W3Qr1q-ISL-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556a03bf67.mp4?token=nouxMWfW5aUxN341-Cfrm-34yRXq4fEwvtUfhho2YB3HoXJCp7hLxaigktCvq92JcLLmgx30WixtmvO2soE_CcIH4mRyPzhCZ305u7jflr0AFOG8vWT5aeafEyLMRsGIBpPumbflzNKBJTSNaoc1IXteDYfRikWiHeot5ovuWXHaKx7HhNPrGVb3H1qwW9Qa-bzIVcJkW4mHHZp57MUxrpw2rT2S16y5i1rME_PEvEHqfZiV9rv1ffuxaxqDcUULO--rF-ZMUA0-Yl_15uYoRv2vqWfRVsErta6iZ7bC66K4zYtjAoe8FUrcBl7QgoyDwpJ5hivph2W3Qr1q-ISL-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇦🇷
استقبال مردم آرژانتین از اعضای تیمشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101430" target="_blank">📅 12:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101429">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44603a4d54.mp4?token=juiN9fHPCfV9B7NoFoo9NmzUFDNGXRQ9EEmwJhME_6XHkIxD4HJTmpF-8YEhFPcyOPiEbpsfWiy6fGfiZY2ffD9uuwhWIC3r5cJBCiJM3NBjUjFlvWASxi67rwZW-uhy4jFIngIJYZof9-Kqng2Fj9YBFhiFFEp-bv4QvGK1HjKatkvaooOh9GmyCHBLEMgiFpGm4brWFr3StPRJGXjHANqvuKtrJU5ep_YEUr0C4C9DJGkUOPrUIq141TwPV-38kK8JPsxwbX6b3wGSg8rlSFWvIP-Y9VV8HNdZPvHS1dLGh-_ATvk7sFfZQ-6QRcvBPbbZ844FTCPfnH9Mzpgn6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44603a4d54.mp4?token=juiN9fHPCfV9B7NoFoo9NmzUFDNGXRQ9EEmwJhME_6XHkIxD4HJTmpF-8YEhFPcyOPiEbpsfWiy6fGfiZY2ffD9uuwhWIC3r5cJBCiJM3NBjUjFlvWASxi67rwZW-uhy4jFIngIJYZof9-Kqng2Fj9YBFhiFFEp-bv4QvGK1HjKatkvaooOh9GmyCHBLEMgiFpGm4brWFr3StPRJGXjHANqvuKtrJU5ep_YEUr0C4C9DJGkUOPrUIq141TwPV-38kK8JPsxwbX6b3wGSg8rlSFWvIP-Y9VV8HNdZPvHS1dLGh-_ATvk7sFfZQ-6QRcvBPbbZ844FTCPfnH9Mzpgn6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حضور ترامپ در فینال جام جهانی، ورزشگاه را به یکی از امن‌ترین نقاط تبدیل کرد! از بالگردهای امنیتی و نیروهای ویژه تا تدابیر حفاظتی چندلایه؛ همه‌چیز برای حفاظت از ترامپ در بالاترین سطح آماده شده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101429" target="_blank">📅 12:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101425">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/layqfVQirbi_lx2UczZdvaVQ9D4lSeHIZKnDuhB5jdThra1IrgQLo52z1uXwyvh7iF4CBI2D536ABcjbRv-PXNKGxUhlO5-4AE2qSSxISmtnsd_UDWRVlkZpwCa2KpsDG9NhTVvxtehmAUtBE8GzWbH3W75lILvKQNp2vQxojsxkPmfCuYvkgPS1MRHAlX4_kFzmq7uvAV-7Ecwy69agWJAcdfZAudti5cMyX0eXoKSElmP_kf6WCS9FfAoldSSiXdqD-YyGIn6uhwIDSXjB9Rj4QJVX7PyECCp1zC_O0CLWCNZFz1b-P8zxrwX-glXypQvrhhOK8ZxU0tc7ZkMo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTYCx6mWtIiny2ysl79HcenmN5ANp-DwXZDZIDJsJ5G2L-NvgjsJLTam7rxAsZYajOUnWaPFhpOIAIzLcTRPYNA4em0HgjSEb6mSXcs6d24V_GSeno5x4J9Hr5I3fLwGieR5TY5Or11_Yl7w4UyJzJDsCKYhD5kTwlLGpvG7gGs_ankcHSwAZodUGuxwBBk5q1SFIEinukeN_LWV4W_AmF6G4xSPgohIgJigo2kvjAFPJpuMvW4kWOIJen6iovKn3RI61V2WncDGVH-JEPilw1fLDoSY1ReXHpqUTO3-tcdAldiYX_lNADzgp0Zd1W6cqwxFIcNJ1OfpOXC0XUq_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOst6huoQo8DiZ83xM3D635lNLMRkDrdoxYxYSPpG46RlVj1C7qAXbSPLIn0UHwI0ym2V-lalHZKcijdJYgYmnmBRcWx-0yfZnIy31Mi8FTHtgdjHZQvsPVOSQJG01QTp1kCSQQXMs-JF-R0MesWmRsDY7C6pqxYchULC5oIpEtbWOf-1E7Z6a6-Il8N1BMEFi9nmBq57c3k_mtqWVyF0-a08B9vABG5CXdXMfgrpyc4129Z2GZM4B_fH3rLZ9_md0aYNcsOb5Sh0AdTuSawlh5V7_SoUSKpI7MKBM17sj4PaGdwRO3LAhWkePsM4lUbfbDBnCUr9WQA8nJ1hAGnfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcKw5U-jYvB2IuHlxWq1WDNBdOzWi0NVY_tT4gQiK1f0u9aIe7lW6K1s3fQgSZqHsGoFyQjky8aRyrfKuzlqnD52T_pR68doYMglrerkZpgE9EZIQn9TWt-GIbDry0sT0rfca0rse006lQmR4vQI1NtFL-N9trP9p-YrCS9ODO7BIgDo_Yl9OQg4JcssJNeTT56nVbLLT2fixk8YrmDnOuZgHW7nukZJkkII5ESV0qd4sXCTxEKNHYqGckwTrXf9-tmsEZzBjuRY1tZ2htxT8c2ltXlrjRnXj4sZbwvqdcaK3yJbvYXgBcT1F-VOUFswHcPz2bmY6i2hxxGWhsmHRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رونمایی باشگاه‌میلان از کیت‌دومش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101425" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101424">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZK88Q6aZvSmqcB2W-cCtC9B2064gZ_kUUO1SsfKsGhq2G9NMTDg8zy613BIGNJw3dCxpoinXGVkflWEtO0sLb_rLuns96y1U7Xwu2WRL6UGXAafXKB1O50EV4xkR6pxvFiNQlc7U9Cu3QisimHpksBct9xWAshXE9KtrZknAvJnEH7as2WVLUXnT8nFTenPyBDeJ3M6SOmvxg4tMzzP0CaMlijYnX2PDlgExGzG9WhTe1y-AVVyhEP2X-c611K2fKEqsJcJV4K8sNLgaXL0mbaOURRBWgg84UJVvIoVYH-swNkp8rj86eaqVB1K-GxSxyzz946yfITJ3g0bz1JiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
بهرام‌گودرزی مدافع چپ جوان آلومینیوم اراک با عقد قراردادی ۵ ساله به استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101424" target="_blank">📅 11:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101420">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vGIuba3TROPWZSy_Hx7ZjYyU63IxdOTNpkm5Bq-n2C9U2W-JTyOWMTfQeKwI3eCi5o6rukAaSkvlgYwi70mMMhjSZECH4T21XLnplBr9EvJ92y3bfDm5DjYtVrL5mROYsSPm_3vX1k2Qdg5z0SFdzAiQHjpR8LZ9rc1r9hP2SsNCvYnJ2RXQIo5muwyrvlWbjDV5F1bcfGFfhtKEFG9_hPHhEsFaMtU5ykiIJLCREJI8iFoioK06FvBvLyBAhUDappS6v_vyV1fzGp17u_Wd6EKW0rerklbMEkEUPsx1EfoYMdXSDQ0ZRk633lfHs7u-2W0DS73mBdWTDihr_yQqvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_86CYREHJilR-R6g7YBXIHwvoPzk_1VNP42LA-OBa4yaTUnpPvv31E2Opj8nI8NOEUY3CdcFhEqfLXDnS4CbQ6cxlC0Rys21BTgvQ3nhu1WEFzLFXJNfeXk5djd1_6-AIIdr0n9zjjeXH6gL8NbMqzOEqeMQlRqAZDX0x5ktyid6Nzq_dK8ogB1aZuL-CW3BQPN0ak8UcNVp0eaiFl7GP39n4rMhZp62MKRSCXy90Kvus5WowwgtJpwuHTUGCv-E-VqTnD6hW_1cnIKi7lZKc_YXVDt0JhgwqCdHcBca8_6QHwtT_z2cXT4b8X8PSE-Gm83FFU2e6ovyTnFTmi0EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5LdZDl4blTXgzOJFENuDSeVl21PI_awK5V5NRr1d-hdlP5pb2ECDPXF15JYboglJDQfYnMEjittCnnWP0sNoI_gDt7FcRtomo_-8jQrDOWHSWa9JVkpUHxG6NolMs1cBTL_tN5Ft09yBRt5ar7-HRxeEBH3nBXKgYtzjvNYM9yb4Jq6ekduW8xgo5i8rKlkTUGH4OukErvTyoq0x2QYa45-h545BdSdn2_advCkQ_3C7bCl6XrhDMS7BNtoJAlh-SngV0JfzVBST4Me2y5NNiP63iwU-CjQq7wq3vi8gtyyA1JG4wBvNsnqydqMXN8_okY1ERljaHomQMkJ1Bv-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MspoVQcF1wqkVJ1yINFJjXWFbGd5aQ7QzOSvHXqwM2W7TJ6tIQgnq0RIfxRwGaPqaDCuwY_p02fpLrhYpL6k9KIeSU1qt9NOdY2FL0tBoujuWqG1WW5YPchEI2MMPUbY9kl9HCI_Y5B5GiPLd97N7-meCRiFxU-06AAD7qhIuClLFF9u_P2QwzWGCScgp6LjEWrls2yamIiOG4ZQSAJ6fkoED_BEdcoU8C7LugxfzakkkkfmkGQiRi02nDML37R1cEzjlYBb69R0zSAaV4Xm2e-si4RVJoLfiAPEHnifqE8aoyngdtQ_-YIyVX5ftbeW376s-gqN0XDZHrrnEF1LDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
رونمایی باشگاه یوونتوس از کیت‌صورتی رنگ دوم خود در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101420" target="_blank">📅 11:48 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
