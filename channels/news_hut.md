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
<img src="https://cdn4.telesco.pe/file/gJQfLE1ObTYugu6coPDEtmI4T1wK2lBUZ2fCCR0nfpWzrVIID7RAWMTxZaIVfAUzFXGTjeAi_PVDYTfST4MzvAuA5Y4eA061t7PcWUOAacqYLx1WB-bdpgfN53anaD6stYg-JGLk0wI43ly0Tm7CVlxLHCwo2BHjyjJ3Yaoa4HFM2OZUn2MZnJFvZ2-w4BDUgVlGDWoDxI5UjV3AhUhQMMtv4EjetPDAfPfgGFNNX60yn9Rq9LbNouwRBg_3_1dNJCWAuGJoU7mfDPaUC644Er_YPdxbFkWOcWLNi2RHXwqcyvyVmEgI7RUoKZA-ZgdmB_gPIM8dwGqHaOIPffyCUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 196K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 17:00:45</div>
<hr>

<div class="tg-post" id="msg-67422">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=N-2OTgl8xcbYnexWj5VfzqZVAFINe-VdCoQXgR2vnk9NNaJnwWHLp3eeqD3ecM35O0878-1rTiq4XmcZuXa0TJW79gQxZLzXmlAPsZrcSxUrwaT07otxAp3GcfB5IiC8z_-4Os1tLIOV4HYpWvmeeMWP0wuqLM_D-lU1B0L0Bvru93c-fRQhTJoiZcjv5snyYbZjgzZlUnR4ZZIiPSLyqh-izLyYAgfsn68XKRRhK4kt2hQ5XQxs-nPcczXL7k9inKzgk94890p_29LqE8IECwszT4ZZE5yjR0MbSoq7BcM5m26xCKOPTXt8nWmDwnMrOPyL2aWN4UnY68fx-f7HbzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=N-2OTgl8xcbYnexWj5VfzqZVAFINe-VdCoQXgR2vnk9NNaJnwWHLp3eeqD3ecM35O0878-1rTiq4XmcZuXa0TJW79gQxZLzXmlAPsZrcSxUrwaT07otxAp3GcfB5IiC8z_-4Os1tLIOV4HYpWvmeeMWP0wuqLM_D-lU1B0L0Bvru93c-fRQhTJoiZcjv5snyYbZjgzZlUnR4ZZIiPSLyqh-izLyYAgfsn68XKRRhK4kt2hQ5XQxs-nPcczXL7k9inKzgk94890p_29LqE8IECwszT4ZZE5yjR0MbSoq7BcM5m26xCKOPTXt8nWmDwnMrOPyL2aWN4UnY68fx-f7HbzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توضیحات واعظ موسوی فردی که تصویرش به اشتباه به اسم مجتبی خامنه‌ای در فضای مجازی وایرال شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/news_hut/67422" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67421">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=VfMMQmohHgUdruhzRgg7XuyMHAV-Mjmj3oIZwbysknfMAh3TCHUjK5ZXvOaqz02aWBzdlmyweEDeVvjP6MDX2twLyeUXfBZqbinEblWHM0Xs7ge4JUrcbs-uEjVx_U-fYhv4d4I-97S-2ekG7iTyBmoVPmKhuD-97gbVUnL9HzSbG0zA1rmRo5uQV7ck5hsOTqX8A2KJ-BHuYmC6leJ8jwsKMs8pC4mD4m1pdnFEazfsBzsAbr5hiPfK8SsClef3GGcDOh6Ksg_ldrX5NTgMji2bpllRYXQU6NSJdgAF4uqb1EzoIPXjTsOH-_uY5PabJtZ5W7gsLzu7WoJGC0syiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=VfMMQmohHgUdruhzRgg7XuyMHAV-Mjmj3oIZwbysknfMAh3TCHUjK5ZXvOaqz02aWBzdlmyweEDeVvjP6MDX2twLyeUXfBZqbinEblWHM0Xs7ge4JUrcbs-uEjVx_U-fYhv4d4I-97S-2ekG7iTyBmoVPmKhuD-97gbVUnL9HzSbG0zA1rmRo5uQV7ck5hsOTqX8A2KJ-BHuYmC6leJ8jwsKMs8pC4mD4m1pdnFEazfsBzsAbr5hiPfK8SsClef3GGcDOh6Ksg_ldrX5NTgMji2bpllRYXQU6NSJdgAF4uqb1EzoIPXjTsOH-_uY5PabJtZ5W7gsLzu7WoJGC0syiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های اخیر علیرضا فغانی از ظلم‌هایی که فدراسیون فوتبال در حق او انجام داده.
@News_Hut</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/news_hut/67421" target="_blank">📅 16:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67420">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLAXqWArnxmMdoLI8Fl8jf_6XaNbwcgmocPEEvBrDIBPt-0PypG0BDgPjr8i_ZEtys3myqXSeUHgAmKYyJNyT_DHJG-GAXJ17mswryhXtHxkDSGQlSFA-9mS7OZqy8iWCOIWhmVD2qPP_rBrlTwSzf1nMZ080sCkNWT51H6XYu0wLvg8P4d12CdtJe1jVoKvMEcfjYE8vSA6W6MgdMamE8hOfPhJfTk6h6UITD788vXgk5ws6OjZj0Z30xVChAP5iXDJ43TrTeqZR8HrIyA2ZJfAxzj6cz70_ILNbyz45J09yL09LKsZDHogvg75O48RmCDYIqkzck9GRThpXg9khA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری
CBS:
علیرضا فغانی قضاوت فینال جام جهانی 2026را بر عهده خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/67420" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67419">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=SCCFwtMj_NuQKa19AV5__Q9ezOq8jUHi7hCyJADhftFiGbL8SbOSUeAOzC25wNfeXZ7EMk98Fhhrzzbf8tdZpRYsGPOPLOsEVRnSiXv7LWUfiIrno4fqKcEBwPT-IWaYHeW7MIm0wDnr8vDxNRQ0isDHKOrbI9cENk0uZ2FkPmfukgPxqqEpumyc8Flln1ncipx3qTbWeiVEz-bxbxHjn3XRtuCvjfZMpoDUac6-t8XPO_AF3zH1FJH2JH-v6f7MwEjzKy3J7sF4iXGoqj0Q_dRs-lSZxZzt30pgGfKh0fAShpgW90VcN3sNd0rDICZJlyFcK-KiRlhNEJXJwzxvNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=SCCFwtMj_NuQKa19AV5__Q9ezOq8jUHi7hCyJADhftFiGbL8SbOSUeAOzC25wNfeXZ7EMk98Fhhrzzbf8tdZpRYsGPOPLOsEVRnSiXv7LWUfiIrno4fqKcEBwPT-IWaYHeW7MIm0wDnr8vDxNRQ0isDHKOrbI9cENk0uZ2FkPmfukgPxqqEpumyc8Flln1ncipx3qTbWeiVEz-bxbxHjn3XRtuCvjfZMpoDUac6-t8XPO_AF3zH1FJH2JH-v6f7MwEjzKy3J7sF4iXGoqj0Q_dRs-lSZxZzt30pgGfKh0fAShpgW90VcN3sNd0rDICZJlyFcK-KiRlhNEJXJwzxvNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ برای شرکت در نشست ناتو وارد آنکارا پایتخت ترکیه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/67419" target="_blank">📅 14:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67418">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FufM9s0BnbhzEk_jQm9Q0Yl9GCV6tV1GCMCTG-VTMkGOfUR5RV8Ej4dF_9TfN9OYUuwvZJ3TxNH6hUZ8WQvriA-ma8hgvJtk25sYC1r9nepws5BkrvjKBKImA7pE7-6Sg-Xo7cUXCfjsskgAj5XFxceJ_X-cgvLJLseEbc0NsMuMfKtMBecyPWtzWae8tsjOavMAoWcnNYaddiII0BSH_hTi1SYb2KEJs_Zyb2Yzi3UrSud-NLwFmviw7bkFyxjj8sNTzWQFgK64r4jwC-m4WQHNNPyPRjqznIgHNg03Vw6K5ah9-mJiTPiHzAkwZCc5JWO7oF0UU_8khlOZ8FkNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری رویترز به نقل از چهار منبع آگاه گزارش داد نفتکش حامل گاز طبیعی مایع «الرکیات» متعلق به قطر، هنگام عبور از بخش عمانی تنگه هرمز هدف قرار گرفت و آسیب جدی دید.
🔴
به گفته این منابع، این حادثه پس از گزارش‌هایی درباره شلیک موشک از سوی سپاه پاسداران به کشتی‌های تجاری در حال عبور از این آبراه رخ داده است.
🔴
بر اساس این گزارش، پس از اصابت به سمت چپ کشتی، موتورخانه آن دچار آتش‌سوزی شد و دود غلیظ امکان ارزیابی بیشتر خسارت را از خدمه گرفت، اما همه اعضای خدمه سالم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/67418" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67415">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la-EsNavPi8ioUicveS8bGTT8T1lU6Nt4ggs0j0yiQkyfXQxAsQ2KImlW1iTMmJ-BnFeTccdvqwRmOQdA3jDL5gURBh64aVwhOAw3zs7XAk3XQP8zKfv1rE6b0_xwGsY11-4kUp-oSzWpoYIL_hz9kFMyNro2kl_GvYqpWmPHH1nlxvNEbjPRWlH563nHsQLUbAsYNGwm-yKvBwWJShIsKqcC6XOjkIpX6clhRYFbElvzUi5JZWXPxtAZu1aF0hGhEy5YDMZvw7ug7-dz9nG-4z6LPgC6SK6maz4QpxlDg5yCxom3MmTlK4cMuuM4ZXcBMmff11Xuk4m8S2I_Wi_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=f-LHuAXtuItTRBOF1J36KFVybI0sS6BG_XFRXJI8sQOLA8QNP2mKHlzjg6y--JwkD5g9p8e1u6ViHFia7xQ9z_L1Rm-GY4TB-P7dAK0ZrnSlOGSWe9cjzNdovsde4TTDsKGKlGVGI4p2wiNoSm2ha7_mbDitSKi4ZoEaCuPRMAm2oZXTXnDKsBJ9kBWAMGiFMURY8aY0xigfVtfbbN6t3ogGfeVIh7dsXMfqTN7djetuXUOVV6ovXxPtN0IDiMFNtSDVV8G2fvXEsUNTPinMOp-0BT1JYkyBR_l61v-k8uUOU-M-TxSSdND0Nbg-veYOUH3bAv1v1kMYPZ17Wk7DMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=f-LHuAXtuItTRBOF1J36KFVybI0sS6BG_XFRXJI8sQOLA8QNP2mKHlzjg6y--JwkD5g9p8e1u6ViHFia7xQ9z_L1Rm-GY4TB-P7dAK0ZrnSlOGSWe9cjzNdovsde4TTDsKGKlGVGI4p2wiNoSm2ha7_mbDitSKi4ZoEaCuPRMAm2oZXTXnDKsBJ9kBWAMGiFMURY8aY0xigfVtfbbN6t3ogGfeVIh7dsXMfqTN7djetuXUOVV6ovXxPtN0IDiMFNtSDVV8G2fvXEsUNTPinMOp-0BT1JYkyBR_l61v-k8uUOU-M-TxSSdND0Nbg-veYOUH3bAv1v1kMYPZ17Wk7DMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رویترز:
تصاویر ماهواره‌ای نشان می‌دهند که هزاران ایرانی برای مراسم تشییع پیکر علی خامنه‌ای، در پایتخت گرد هم آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67415" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67414">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=v_ndpivhsS0hVLt3YBn0H8aQ0sZLrNebi4gbchlpEyMdKBKetgt-dt3q-KX28wfR2ffNDBjOQ7B-gipL_Sq-zM1OTAVuHJ9u0sAhIo02s9J7OzdpZFQYqs0c2Gx-n6L056QG6VOVH2hyHVlLwiCRwC3_6g1uBj-7ge3xXpGHMrlw6RQZU31OMysaQ8txef3Fo50rZcLuGMrpnqBbEASQjTmwJB9UDA4DuGoyXxAOv9pagmFMnpFmDjAnat789YD1yuh41QARo2lks06zRfxZHA361MfdzDA9KrZGDWUm6v9ZSSMp36yLATUgHQtEt45xtwL_734i400TJywHuMknqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=v_ndpivhsS0hVLt3YBn0H8aQ0sZLrNebi4gbchlpEyMdKBKetgt-dt3q-KX28wfR2ffNDBjOQ7B-gipL_Sq-zM1OTAVuHJ9u0sAhIo02s9J7OzdpZFQYqs0c2Gx-n6L056QG6VOVH2hyHVlLwiCRwC3_6g1uBj-7ge3xXpGHMrlw6RQZU31OMysaQ8txef3Fo50rZcLuGMrpnqBbEASQjTmwJB9UDA4DuGoyXxAOv9pagmFMnpFmDjAnat789YD1yuh41QARo2lks06zRfxZHA361MfdzDA9KrZGDWUm6v9ZSSMp36yLATUgHQtEt45xtwL_734i400TJywHuMknqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جکسون هینکل فعال‌رسانه‌ای آمریکایی رو بردن میدان انقلاب و خودش داره شعار«مرگ‌بر‌آمریکا» میده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67414" target="_blank">📅 12:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67413">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=UWcRJN8H0x0swhDwITLP-VWgZmcGBaD-Z6rcT17yq_kNU6Xl4iPPGbV9z-wwvlSrdtrEP0EKI70dRk5Q08Oz38BkTIikde4DauaOJhGKJC9s2E7SQXq6zQb7x_3L8y1EJHSoJiFjhVpyQruAzueKbbypNjmpgQDArBdbIxBLnWzIoh1-1DpkDLhFhaGvRWV_YkJYS1w-Rng04tC8T4rRTd5AKkaSZ_LS9k-t3W_14w1dMXpzHeKNestjQz-2J3HjVLONGC2wyXT-1K1f4uXBWP79CsXnq4oBIQZxTf1ek1ZuEdLzURAFkQBDEdLwmOr95mUCzhcol-deMZxNgrv6pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=UWcRJN8H0x0swhDwITLP-VWgZmcGBaD-Z6rcT17yq_kNU6Xl4iPPGbV9z-wwvlSrdtrEP0EKI70dRk5Q08Oz38BkTIikde4DauaOJhGKJC9s2E7SQXq6zQb7x_3L8y1EJHSoJiFjhVpyQruAzueKbbypNjmpgQDArBdbIxBLnWzIoh1-1DpkDLhFhaGvRWV_YkJYS1w-Rng04tC8T4rRTd5AKkaSZ_LS9k-t3W_14w1dMXpzHeKNestjQz-2J3HjVLONGC2wyXT-1K1f4uXBWP79CsXnq4oBIQZxTf1ek1ZuEdLzURAFkQBDEdLwmOr95mUCzhcol-deMZxNgrv6pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در حال دادن شعار «مرگ‌برآمریکا» (12بهمن 1404)
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67413" target="_blank">📅 12:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67412">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIA5PEyeosPnqgWlH5qmCrtBek7hBza7JBiTAu4_GyrZwrBXTUaSKOfmJUiBeeHXBW6Mca9trsyQL4uSSHUEsI8bxSU2oEgIT6MVf1ceBJwmiXrds0844OfRqLH9ee67hGmUtsq9vIhJWPWEYHkYOls4ZAHD_u2iAptwaQFuQKSDlqtriyE3CskKEq92-ot68rQfbJnacXD7RUmrlCNntpNr92Wq4zeWrFXTT4VXa7cN6ah0byNsiTzW7WQR_0iYI6QfMVcDMlINUF6BocIm3x8oqhRtYhBoVHht6r1dwmI-gCV1G-Xpa6SgeMl-h21kt9O9jB7EdzCv6X-tiZPKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس:
دو مقام آمریکایی به «اکسیوس» گفتند که ارتش ایران دوشنبه‌شب دست‌کم دو موشک به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است و دو کشتی مورد اصابت قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67412" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67411">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
احتمالاً نباید این را فاش کنم، اما ما دو تا از بهترین نیروهایمان را برای محافظت از قاآنی در مراسم خاکسپاری فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67411" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67410">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64666ae825.mp4?token=InoN07M2isUWRtnChPAxmn_FaS2se88-MnBwMqg2x9gSDgxksSuSymrt4SQMkNK4plajGqwkhg3wzS7ku4yNBwO-uqwNgY9Ms4i0yuQ1Rw1nhMDk1Yfn6oKB_Jh7vT6xqQVvzaLShVLCPaqaG2XmAkW3ULZ5bk0vU2w83bTUgjmaDpYhyN5QGU83QiZnUi1PORmFNzE0P11JKoJUtrSC5fHMC8d85fXfczures1k-hRvtrq6ZDjfBAoJUYxDl-bTajCI0Ow_pNiwP4upztD6Jmi9wtpABWT3Rc5Fjg73zMZy61zLlFsR2lMjjqhodB78xEyVuhqlQyT8nvYhZgWUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64666ae825.mp4?token=InoN07M2isUWRtnChPAxmn_FaS2se88-MnBwMqg2x9gSDgxksSuSymrt4SQMkNK4plajGqwkhg3wzS7ku4yNBwO-uqwNgY9Ms4i0yuQ1Rw1nhMDk1Yfn6oKB_Jh7vT6xqQVvzaLShVLCPaqaG2XmAkW3ULZ5bk0vU2w83bTUgjmaDpYhyN5QGU83QiZnUi1PORmFNzE0P11JKoJUtrSC5fHMC8d85fXfczures1k-hRvtrq6ZDjfBAoJUYxDl-bTajCI0Ow_pNiwP4upztD6Jmi9wtpABWT3Rc5Fjg73zMZy61zLlFsR2lMjjqhodB78xEyVuhqlQyT8nvYhZgWUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته میشه این شعارها علیه عباس عراقچی توسط تندرو ها داده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67410" target="_blank">📅 10:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67409">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=J1uE3oupNr9E0v4jfY_casFy3B9zoCrjxbV6gSFOmNuCtT8c4kgvlbAWTMrTpTbr4amGYz8H0ih12U4gyEGyQ8gQpv5vhv7CC9pwoiS7688E77IrTgZsWF8MjE0n-PH4rQtftEF7YEOp9bdD-C4dmi6P7C2O0cdv6hn2OHg7HeiFMv5zQsEFg0RmiSgLneEXcMbUbQAz5r2UbI2oliTrwXtsvOyhG4_JBUaOJ0WnRu5mf8SPXJku-4bDUi_iWn3IMEzy3jl_LmP8_rkdZwWXgDcCsHt55bjtEwLzGW5NyUO3oyMlrgwc0A3tQ1fgU6aBYE5kinrDttyJ21aio6-yTiMJaINge3LIK7J5R97eOPcXrxscUc1HlVWYYDFPYDlOqNGxiu_ndic6X4h1b3ycEtN0cie_1XqL-4Ssp4KxUZlX1iDRAlQiTCyvFJ3i9-0R0kzkKG4nj4iAo9xXhLV6YUUbUm8zXesRa2Z384b6swuprWlM8dmdaQ8sqd_mh1O70gS0epLqhSdoSxlroZqFLAVmhA6fyg7B3XvSM0NGUf4EcbyIEu1h-pfKUU1fm7GgpsTZUwhpZZayulbl_ZkuB3kl3O72L0yz76lHkGlittYJNH4pUazo_2RdHXO4rR1mGru19XEVn5CPWN8FY2MS6ifaB8WbnIm3DlpVzkbqE1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=J1uE3oupNr9E0v4jfY_casFy3B9zoCrjxbV6gSFOmNuCtT8c4kgvlbAWTMrTpTbr4amGYz8H0ih12U4gyEGyQ8gQpv5vhv7CC9pwoiS7688E77IrTgZsWF8MjE0n-PH4rQtftEF7YEOp9bdD-C4dmi6P7C2O0cdv6hn2OHg7HeiFMv5zQsEFg0RmiSgLneEXcMbUbQAz5r2UbI2oliTrwXtsvOyhG4_JBUaOJ0WnRu5mf8SPXJku-4bDUi_iWn3IMEzy3jl_LmP8_rkdZwWXgDcCsHt55bjtEwLzGW5NyUO3oyMlrgwc0A3tQ1fgU6aBYE5kinrDttyJ21aio6-yTiMJaINge3LIK7J5R97eOPcXrxscUc1HlVWYYDFPYDlOqNGxiu_ndic6X4h1b3ycEtN0cie_1XqL-4Ssp4KxUZlX1iDRAlQiTCyvFJ3i9-0R0kzkKG4nj4iAo9xXhLV6YUUbUm8zXesRa2Z384b6swuprWlM8dmdaQ8sqd_mh1O70gS0epLqhSdoSxlroZqFLAVmhA6fyg7B3XvSM0NGUf4EcbyIEu1h-pfKUU1fm7GgpsTZUwhpZZayulbl_ZkuB3kl3O72L0yz76lHkGlittYJNH4pUazo_2RdHXO4rR1mGru19XEVn5CPWN8FY2MS6ifaB8WbnIm3DlpVzkbqE1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، کارشناس مسائل فوق استراتژیک:
باید هزینه بالایی برای خون خواهی امام شهید ایجاد کنیم. کانال ۱۴ اسرائیل می‌گوید رهبرشان را شهید کردیم و هزینه‌اش فقط ۴۰ روز جنگ بود و دوباره می‌توانیم این کار را کنیم. این بار آقا مجتبی توانستند جایگزین پدر شوند، اگر باز رهبر ما را شهید کنند چه کار کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67409" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67408">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=qF05nh8tcTnLZwYpjmWt_twS5nYNN5d8Is59v0wffqp7vA9OkadxxSo-5-_dFBhSdX3QFEVo-EV4oVjSivyYB2Hl7Sa03m7sniiQq9rItnZuw51NezcOieTQz2z3vB_O16p2_GqevFL4O1KmbMYJ24IfJrXWWT9Gwz86OsdxCJjaOYUJvHqc6KdBcY5D4Tjocce2fRgRDNz8NNto1HEVhugehwJ1fM3AUU9DtEmkISGUrwgGr8gnGeC2_j0JZBSIHXJxmqFRzp3XdCc4_fBy29jWe0t7rLVxHo52GrTfNLOovtVobPDZIu61jBMDyNH68k0NhTd0QEnbkpL3aH31Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=qF05nh8tcTnLZwYpjmWt_twS5nYNN5d8Is59v0wffqp7vA9OkadxxSo-5-_dFBhSdX3QFEVo-EV4oVjSivyYB2Hl7Sa03m7sniiQq9rItnZuw51NezcOieTQz2z3vB_O16p2_GqevFL4O1KmbMYJ24IfJrXWWT9Gwz86OsdxCJjaOYUJvHqc6KdBcY5D4Tjocce2fRgRDNz8NNto1HEVhugehwJ1fM3AUU9DtEmkISGUrwgGr8gnGeC2_j0JZBSIHXJxmqFRzp3XdCc4_fBy29jWe0t7rLVxHo52GrTfNLOovtVobPDZIu61jBMDyNH68k0NhTd0QEnbkpL3aH31Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب یک مازندرانی به حضور سعید جلیلی در مراسم تشییع علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67408" target="_blank">📅 09:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67407">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcgPScQ9Kw0-gIVNE0tm2LQs_1-3T2ZSsW5JvC3lBLcvPUTnyI8EY-8LJ1Mbtqaq7UuW-yl74brixxvknrqxvdUPSa3-VnsdsBmiiDMDiDZliSOaVPubSkt1ixBfOQnqqcm1GwlaA3BeIveiVZM0uiDoo8DP9hqT75sRoy8ruMLxw6WxDbhazdZTCcNT4WxndWpHwgT2omrsdWaBpu2jqdwDGwydKyNdgEOZuZjeDF14NHQvzALVgpPSMppdKfTwVMiWFeR_7bxP4RBQsLGq5aEq6-WfX5ORbY8YM3G3LDMzWeF9wEDp8pkCqsZc1E4kETav_AXGAB-8mpQZWULBxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
مرکز عملیات تجاری دریایی بریتانیا:
یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
بنا بر اعلام UKMTO، این حمله باعث آتش‌سوزی در سمت چپ کشتی (port side) شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67407" target="_blank">📅 09:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67406">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67406" target="_blank">📅 03:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67404">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cBtE8Oq7qdCNA_z8-N74SdgSUpYRZaWHJ9U89xZhuS2Qn-J8KLKKiF6sXB387TtRi9no_g-rLioy5yHRlgEWd3jeQPEDL0jgYW5CqF4sgP82OFkTPVRhM826m-KAZmbIRW2ZKoI2Tc-rcsy5CAkGehLi8aMiiRN5vSAg3dmKxwlHLzmcifLHoLIzslUVGMSmwBqV7QFJ-onD_tFvfUtyTl8b9N5ZVp6vaYuVX8dy9h-paasujLfrclUyzCpahmz2EwlHti9zntRha2ATLMACUcm414eiP_iyvwpd4lwNprss1Bwsc7Afh-EOE1kdxYz1_6-dh87x8fllmc75hkcfFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67404" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67403">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmeGBYTX-1t_vob9flAPg1dBIEIxR5Wncg1UU5XfqBgXKr6CE9Y4NpCX88a0aKpIdf_52PO45-w1uPTkw5VxuilUXpwyDy72Tjg_1ZuOYbqE-XRv6M9iwjBekDa3U3exwdCfYyqsjz21yPcV6DkQJQmohrkF51N0_xmhzGyV_KyEBWc7jPX7YxUoOVDw7uQznYlZtyWBUWOWddt16JulzHVVdWLL62B7NU60LVFjNeZnhkrp4tu86KjeX7PccXP-R7fNlOw7AzqaxpO3oKQ6mrlhzKSrBW6MTwQM6SIDU7aZoLdyd40fVbrJ2RXOE8h98Ros2uHiMUtdP8-6OouSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026
| حذف کریستیانو رونالدو و یاران با شکست مقابل اسپانیا در دقایق پایانی
💔
🇵🇹
پرتغال 0-1 اسپانیا
🇪🇸
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67403" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67402">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9EPOMo_EwGK5TWXy-w27uzWFe30iPPNfNcZmXyKj7oWeXNgMaTfH1i2faLYmketlENwqqYYsPzpFfQOrutPzZhxTnWwRnU8zNeDWyZl1Vk7mTbeivjxelxmytsZFjAxZhzLNwXQX0VK9PZ3VX_4F35GuJdCDHcc5ePoJDBeUreNNqM5BWLgPpxiMNMANnZMNy02pxlAic90AgYlMo946Sol-qHfOWcbo98VlDkiv-hMBg9IlRzd7ZG4CO43BhcK4bWIatHeDUq_4FET2l94bDF9aBvZ1c8QqrEtlnNKMX9lQFEMsGrGs-j-txxdIQ5R4QOLOD3LrXdTHWA1f9fH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ادعای کانال 14 اسرائیل:مجتبی خامنه‌ای در مراسم پدرش حاضر بوده.
🔴
حضور مجتبی در مراسم تشییع تأیید شد
🔴
مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
🔴
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از دانش‌آموزانِ حاضر در جمعیت، تلاش کرد از ردیابی بیومتریک بگریزد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67402" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67401">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=gv7vtphSTaY52hmHj5eFLxwd5MwEwdaBvoiq38fxkdmzB4LG5URQpHGo4x5qJH-butoo_MTM30QwyaFNryf55-2H7Ifi6XPxtc5-_WyPtTFIuajXIrNpc1YCxQthYiugBTmNxtrbw7xdeXfjgACJAiZH5BF3lH2Ef5oWIr6qPySaZhS40T-z8jOLBcQMK9qN_TAXSz8cFCp8xtYwBDSUpZCvH8nTJahvAfXnR8jSVaDju3Z6YW1tIxOG-KCZLiD6gdlbrD8xLE1o9ixaWKlxomRUUWFk9Ovm1siHGXdVY8VF80AxqlbEGwQsLeB4huSBplORKDqN_UGBD5YMco8Tjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=gv7vtphSTaY52hmHj5eFLxwd5MwEwdaBvoiq38fxkdmzB4LG5URQpHGo4x5qJH-butoo_MTM30QwyaFNryf55-2H7Ifi6XPxtc5-_WyPtTFIuajXIrNpc1YCxQthYiugBTmNxtrbw7xdeXfjgACJAiZH5BF3lH2Ef5oWIr6qPySaZhS40T-z8jOLBcQMK9qN_TAXSz8cFCp8xtYwBDSUpZCvH8nTJahvAfXnR8jSVaDju3Z6YW1tIxOG-KCZLiD6gdlbrD8xLE1o9ixaWKlxomRUUWFk9Ovm1siHGXdVY8VF80AxqlbEGwQsLeB4huSBplORKDqN_UGBD5YMco8Tjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارها برعلیه پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67401" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67400">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتلوبیون اسپرت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT0SrnmGJJrvFyDQk04ksgojZ-BWkm1irBlfzd3gzz5vbtOPkpxo8i6ZeZ0dHaQSpxJILhTl4KpEtMdY-ftcpL6c1YtAOslnx_7UEvWKhYokxiXitCmkpPeVRxFSCJ0M8MB3XCRNZBx2KRInKtgDxgifVRBtN193l6abmgSACLxIODzUuaSNqTr9iCrkh7EgHETQzfEe9Ap2-EKTK1j-sfRw3rngsB_syO2JUd-gopaXjMqaVXELLYOnv31xjgT7DVynTNcTjDiaH9gF5-W-GpfvoCaiW85tAdso59mtFP71ELXze7nWFnw21QSN6sJJmPtNnvj2T7TIS-WHMhfQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
اسپانیا یا پرتغال؟ انتخاب با توئه؛ تا از رقیب عقب نیافتادی از تیمت حمایت کن و پلی‌استیشن ببر!
🏆
👇
👇
👇
👇
🔗
همین حالا حمایتت رو از رونالدو یا یامال در لینک زیر اعلام کن و با بازی کردن پلی استیشن برنده شو!
👉
Https://tcup26.com
👉
Https://tcup26.com
📢
این پیام رو برای دوستات بفرست و به این چالش بزرگ دعوتشون کن!
🤩
@telewebionsport</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67400" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67399">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e727650.mp4?token=crH_ZBmmMjbHk6ZeCPhCAVAj0P3giHM01Y2jQnF6xWYi8CDvBhFBYBDgR-bOuEUTsg0u2Al9JEkweu58QD-mUsN2xjOB6gHoneZfrMzySJcUYgT-UWWx8YWNsceNBdk-MfHpMum003qDqaxhso9vahPkISSmdEzz99bk736ect0cCpPsSW-uCZjLNlrfOESbkbrVL7KHhz9eG-NJGOup7my2J0ppm9SMI94ry2oe8pYZaUqAkmF1VWvJbUbJXNJPq1EpZ7adXY17ID4mdNneA68JdFGnep0IM_GVJTF9P2JGbAS2mv2cY_FhSK-IR6-elSmy7zHKF4eqbCUi_EvXEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e727650.mp4?token=crH_ZBmmMjbHk6ZeCPhCAVAj0P3giHM01Y2jQnF6xWYi8CDvBhFBYBDgR-bOuEUTsg0u2Al9JEkweu58QD-mUsN2xjOB6gHoneZfrMzySJcUYgT-UWWx8YWNsceNBdk-MfHpMum003qDqaxhso9vahPkISSmdEzz99bk736ect0cCpPsSW-uCZjLNlrfOESbkbrVL7KHhz9eG-NJGOup7my2J0ppm9SMI94ry2oe8pYZaUqAkmF1VWvJbUbJXNJPq1EpZ7adXY17ID4mdNneA68JdFGnep0IM_GVJTF9P2JGbAS2mv2cY_FhSK-IR6-elSmy7zHKF4eqbCUi_EvXEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
عجیب‌ترین چیزی که امروز میتونید ببینید:
نیسانی که با یک چرخ جلو بدون مشکل داره حرکت می‌کنه و سگی که داره راننده رو قانع می‌کنه تا دست از رفتار‌های کصخلانه خودش برداره
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67399" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67398">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad6611348.mp4?token=Jdgotm308lj4ID9_cegzyhOhu0DVrefvROUXOI9edm2mZeN4QRcsTp6CiZKoM5Nt6uVL-hRw6Eu55yfXYgCziBQMWhhcTq8oDHkD30ELYEhpb2UEW5NdfiJqviZq921Hx6zGsfrdbF-4j4wtSzZDLw5wv-staOz3tNR5hKhfDQTsP67Euq-u2Xh94GFp7DbzSBs-vhIRPksAecCzscq8qk_jYyL1X2WXwKw-XsrRnJmmoElYgidR2bClIllCI5uAjAdfphmI7p3DqZX1iVK2m2DuVKNeGhEGh5zjRlTxhStwrKO_0UH5bZgrjUV7q9AXtro0X_RS8_xk2qdcpKIGJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad6611348.mp4?token=Jdgotm308lj4ID9_cegzyhOhu0DVrefvROUXOI9edm2mZeN4QRcsTp6CiZKoM5Nt6uVL-hRw6Eu55yfXYgCziBQMWhhcTq8oDHkD30ELYEhpb2UEW5NdfiJqviZq921Hx6zGsfrdbF-4j4wtSzZDLw5wv-staOz3tNR5hKhfDQTsP67Euq-u2Xh94GFp7DbzSBs-vhIRPksAecCzscq8qk_jYyL1X2WXwKw-XsrRnJmmoElYgidR2bClIllCI5uAjAdfphmI7p3DqZX1iVK2m2DuVKNeGhEGh5zjRlTxhStwrKO_0UH5bZgrjUV7q9AXtro0X_RS8_xk2qdcpKIGJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فحاشی وحید خزایی به خامنه ای
رادان کلاهتو بزار بالاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67398" target="_blank">📅 22:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67395">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUL-pgtVBXfXs8Yf11YfvWh2HpQ_InGAH4uUxeOV-_tofoQT-_QbAZcM4si8pQAmOg18zsAewruH8yBkbGPxFm7fXML69R9yblLG2WxJLNsRv2LgCKVtWrqZQSFfhxMohbYRdSN7mL9U6NmL2FHURNLKbd3XmSuIM1tbs7vvOPXyu2EE7WX0wpLUu6HR9gC1UYJJai9Gu2Hkg4kc40sksHM-1Ln_uwvOA0Q6elAuctufdnWAs5Kp0qnM_YlDJt-wuW75pUBOEc7ppUaeUvNBB-0_rgIR5RAwD04F-V3otM5QlblGe03ZecplagaVR6a_zyS3vYsaPnv8TJXtkJpWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v0oYCAPnDED5uglPRrgpLQDTrWDxjswvolXQ1f4fjBuVqJtrO6t4Kp_lBx7sLO-ReMyyNNohzUx5ia43cwwiRRJNPPoTx7OSSLhYZzMZN5ZeLWeyUbJ146Qh_CX-lC-Oo03E_i1TZeIYGaduoMlBQ8U7KfamnpygejdiHVMZeTMTny1sDv1m-wKASe2UHN4SdedJ0Q6n9rrtBF3yzE8eO8DN2HSqJT-n5D5hKMeJsiZlvQ_9_YCoSfSaEl9AXLFddLoGeN1g2p36D_1jsKdoK973IsWHHtTk1LMEAuYoL1lPj45_JGVdiGbnFQ_5bZd4eRgbI7Y_z8cMGYVKjUiz5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=OjOESOyUCCVYnzr6e-6nyckpjIl5oRM7CKSEnJVeBybTgZYc-4TuW8iUg2Wg4lSkjSShtt_65HUrbYbI5sCyPK7YE_9laK_8S7H1b_DPiUnZ0Hwzr7GHdE4aMRjJSF4U7V9fUnLPYEH7_hN6g_maDJCivzpDWonsGfHYqCGaOBnQlLCv7BibPx9ZdVww8bM5z-RMRhEmUgdTfqlOwRg-HuVLQQB4CqwlT-0x2WXeXvmxekH_rHgQmUI1RKFhDrrr3RWQ4ZLlDYjDlLw5_ezX94QondgL67qOvT50BpK_u2LqA4eXBfBESd5dJ6uN2VMa99MhT3s5iokxtUkAtT3VRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=OjOESOyUCCVYnzr6e-6nyckpjIl5oRM7CKSEnJVeBybTgZYc-4TuW8iUg2Wg4lSkjSShtt_65HUrbYbI5sCyPK7YE_9laK_8S7H1b_DPiUnZ0Hwzr7GHdE4aMRjJSF4U7V9fUnLPYEH7_hN6g_maDJCivzpDWonsGfHYqCGaOBnQlLCv7BibPx9ZdVww8bM5z-RMRhEmUgdTfqlOwRg-HuVLQQB4CqwlT-0x2WXeXvmxekH_rHgQmUI1RKFhDrrr3RWQ4ZLlDYjDlLw5_ezX94QondgL67qOvT50BpK_u2LqA4eXBfBESd5dJ6uN2VMa99MhT3s5iokxtUkAtT3VRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم اول تصویر کوچکی از جمعیت یک میلیون و هفتصدهزار حجاج است که امسال برای حج به مکه رفته بودند
مقایسه کنید با:
🔴
فیلم دوم جمعیتی که روز شنبه ۱۳ تیرماه، با وجود واردات عوامل جیره‌خور نظام از ده‌ها کشور در مصلی جمع کرده‌اند
آن هم در تهران با جمعیت ۱۵ میلیون نفری!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67395" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67394">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=qlFVnnteFEyXPJbAKHbFlanh4BVl3j_oyqaOjrx29mcBk5PgsBqxbzezOKBoSJkgpqAw1pttfwR6rGsI3Ec5U6hrs6XnxoBPqm6MLulSN8DdFnuiw12qCcF6GSjsXOQo-SoPMLsPELi0xBEHmZX0eFKHqqkh_bFFU29pbF96mrxmE7q3O7v_R9A-FsQLDe9VhbH1PayLFWkKo0yo80yyfeAuFxWcfHtPadTz3KDmWpOMcGThrXU8OVUDxdhoc2TuZqbMD_YE_ZBt79a-Mpm0a0KClQ7gBbGNhbBp7z88xc5o5oDP5Mx1IE0S_uwXX5dQa_n0Oz6f04S89rHgrCogEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=qlFVnnteFEyXPJbAKHbFlanh4BVl3j_oyqaOjrx29mcBk5PgsBqxbzezOKBoSJkgpqAw1pttfwR6rGsI3Ec5U6hrs6XnxoBPqm6MLulSN8DdFnuiw12qCcF6GSjsXOQo-SoPMLsPELi0xBEHmZX0eFKHqqkh_bFFU29pbF96mrxmE7q3O7v_R9A-FsQLDe9VhbH1PayLFWkKo0yo80yyfeAuFxWcfHtPadTz3KDmWpOMcGThrXU8OVUDxdhoc2TuZqbMD_YE_ZBt79a-Mpm0a0KClQ7gBbGNhbBp7z88xc5o5oDP5Mx1IE0S_uwXX5dQa_n0Oz6f04S89rHgrCogEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره مقامات تهران:
ما بسیار خوب پیش می‌رویم.
می‌شنوم آنها میگویند که«بسیار خوب پیش می‌روند.» آن‌ها اصلاً خوب پیش نمی‌روند.
آن‌ها آن‌قدر شدیداً می‌خواهند که یک توافق انجام دهند. آن‌ها باید توافق درست را انجام دهند.
آن‌ها با بسیاری از چیزهایی که بسیاری از افراد گفتند با آن‌ها توافق نخواهند کرد، توافق کرده‌اند.
ما به یک روش یا روش دیگر پیروز می‌شویم: روش مهربانانه یا روش غیرمهربانانه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67394" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67393">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=gY6ymwtutRwkwjn_ZXCQkE4SIc7VKyoCiPtg_l5cygSdIohJJTlWGnX2yX_MOPzix9zOmdmHphAqf-GgwMEzhwPTeTrjEMhHIvkfMcxRndj1PLzfBwkfhEA4gWLSGdJwoMtSCvZXM_t000NnVXS-6xuH4svkfFU15zs6soTySi4CV5nhbSf7p9sibhmVkzdnbPtUi7C6ZtfEuWgaCKrNORx1WVDfQ9Q-vNZyKUP5m8Yh7YQ0SEEtfPhtQxR1K811ICpm78jvCyiZ6dvVRdl1VUH2pVpsWymYfzz889w6Y_VKXkf0vnhZyrW9Fm8doluWoiZhrKzKdvA2P8iQ6HIqFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=gY6ymwtutRwkwjn_ZXCQkE4SIc7VKyoCiPtg_l5cygSdIohJJTlWGnX2yX_MOPzix9zOmdmHphAqf-GgwMEzhwPTeTrjEMhHIvkfMcxRndj1PLzfBwkfhEA4gWLSGdJwoMtSCvZXM_t000NnVXS-6xuH4svkfFU15zs6soTySi4CV5nhbSf7p9sibhmVkzdnbPtUi7C6ZtfEuWgaCKrNORx1WVDfQ9Q-vNZyKUP5m8Yh7YQ0SEEtfPhtQxR1K811ICpm78jvCyiZ6dvVRdl1VUH2pVpsWymYfzz889w6Y_VKXkf0vnhZyrW9Fm8doluWoiZhrKzKdvA2P8iQ6HIqFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح عقل عرزشی رو ببین
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67393" target="_blank">📅 20:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67390">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9CaGumpSRKgCthPwysjc2JtPdKU8OoC0tG7ixeAvwOn4LFzclJbv1pfFGyT5rY2lKK4i1xVq5sTo9vBSwMjq5W8phprBR7WPWqpxRMkaQr0Mc6LBJP1HcpnXWlsemkis4XGDkjqy3CHoUJDYnmX-f4GdjTEVY70VBXJ-twp128c1TE_Kk-7X0q2LhtzdGxPBq2bdy_a71azdMPyuoxZvgrqNdWvm02relprA15tWd6XHbFVF90em0HpqFAtS-9ddpEH4LcG50iESgvYQYxAm9iFmSYYYSUFbYSNFZaCB97okVS9uWrW-cRulrS0Ll0aSgIeFsJwGC3YnPo5VW97vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4sVeZijSkTBNTvpAhFBo_4FiNGCcpZmaxGtAcDn6xBD8oW77qUEyrlUQDVwVgIgLgp-OWVkz3KLeWDV091EagL97Tl0cfWcmLOiiUOgfyJaIp6BthXWgulAfuN9Ljr20JFPsP0Ozc1kXR5t1lsiwqd_YVY2NQRjgHh1N1F-jadRWlZLsl4pKwOsTQadqTReAi-HjVjFMnun_KHqDpq8CbHwV0QfnohW40mzgCVALf7UBFwNlvBj10ECaSqtFVTj36MD6NCdWgna_y8tWB4MbZJ7Wc4su1NDu1fJA8eNJofMJW7-lyfi-UK03Y6jitwPSPdh2CoAczRzpGadKCSK9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=JkYqDUKUiFY9Mh3LybSi1k2J-hABzwu-r-6GBt8EKVyNqMarn6NyZB9bsi_ztfl1D7RAH9UGw2EQar4mEmYVVmDWBP6p8JHxCjD57qcYGkZ2BJ9mBpDfjZ6_GLGfZRDt5yBvxiCbehNxRNpNmVVvFlRqvOLbVIUurvP8zmp_YIrNCyfBckyGxFiXrJWCq7BiH-P0vBhMR7oVpozzlW5k7Ac48vZp8USQ285UmldYmMZAiWt2NJEJ4ldVPxJv5D4egwE1J9tab0HKWPD2Ybg6kY09E7eTRFbv8fer9ylkKP1-PTBEsWasL3F4TqJBLhI__SvfnpF8rwsj3BbpcdPceA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=JkYqDUKUiFY9Mh3LybSi1k2J-hABzwu-r-6GBt8EKVyNqMarn6NyZB9bsi_ztfl1D7RAH9UGw2EQar4mEmYVVmDWBP6p8JHxCjD57qcYGkZ2BJ9mBpDfjZ6_GLGfZRDt5yBvxiCbehNxRNpNmVVvFlRqvOLbVIUurvP8zmp_YIrNCyfBckyGxFiXrJWCq7BiH-P0vBhMR7oVpozzlW5k7Ac48vZp8USQ285UmldYmMZAiWt2NJEJ4ldVPxJv5D4egwE1J9tab0HKWPD2Ybg6kY09E7eTRFbv8fer9ylkKP1-PTBEsWasL3F4TqJBLhI__SvfnpF8rwsj3BbpcdPceA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
پهپادهای اوکراینی اوایل امروز به پالایشگاه نفت اومسک، بزرگترین پالایشگاه روسیه، حمله کردند.
این پالایشگاه در فاصله ۲۷۰۰ کیلومتری از خاک اوکراین واقع شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67390" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=u7AKKjC5aenFDvihiyt6S4yu43zV-j07IVTALnnEGUz1kWxie513_xUfWnJAK3AXv3vU_D5FiX0qpY-7ix8ECULxm07m4Kba30KYfBG56D83MFNV6sYRAGThTiKyCyIIpUiGmmDq1AkYyQymB6I06ZFmC2jYbxyEZ_4i8rGf-_2uAvR5UnpU2A1qt2Jtxi0cNzp7-qnoT-Ie7kL0ejJAhcVK4SAI3nvo3A1rDOc-p6lwGmkGKYKzYYtK7yUYEoSDAvmRYJLMjNpr6prQszE0Olpu7YdOPH0jyOPoP9kcXb-ZqU7fkIK9V-VfWgCjRPB1loVXBIB2c1Qya73vJ02wpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=u7AKKjC5aenFDvihiyt6S4yu43zV-j07IVTALnnEGUz1kWxie513_xUfWnJAK3AXv3vU_D5FiX0qpY-7ix8ECULxm07m4Kba30KYfBG56D83MFNV6sYRAGThTiKyCyIIpUiGmmDq1AkYyQymB6I06ZFmC2jYbxyEZ_4i8rGf-_2uAvR5UnpU2A1qt2Jtxi0cNzp7-qnoT-Ie7kL0ejJAhcVK4SAI3nvo3A1rDOc-p6lwGmkGKYKzYYtK7yUYEoSDAvmRYJLMjNpr6prQszE0Olpu7YdOPH0jyOPoP9kcXb-ZqU7fkIK9V-VfWgCjRPB1loVXBIB2c1Qya73vJ02wpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد جنگ پهپادی:
چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند. شگفت‌انگیز است. شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد. و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=S9ScMuUmI8Kuwyh7yLYkNo5o50UWcsvg6PHpzRGQVULtcUJzdVT8U4MFegc_Sd2BoDGGkPgapINP8TuyV7DbK5X3mFee8ltWUumNas0mNYtC_QIREQMxH-FBr6Fm_rLTIavO-EMkKbxtlGW9CQkUj_AQYVyMddrrr1lE-qa8ZejB56ouMVzl-3L-EVx7TLHYaF4T8lEzAmwM4CD6gsJRiLuZJzqzhJRYr71EAKnu8w6L585BNSpkgAaIEm5oXl5-eM7AHA2vQH_MHEfNkdkvqIW2ugaJ4C2M8Ml0NZaZmg2LH2irRQINdcjKhY2kZIa_gK1jM93sw_UQCdESXUQmEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=S9ScMuUmI8Kuwyh7yLYkNo5o50UWcsvg6PHpzRGQVULtcUJzdVT8U4MFegc_Sd2BoDGGkPgapINP8TuyV7DbK5X3mFee8ltWUumNas0mNYtC_QIREQMxH-FBr6Fm_rLTIavO-EMkKbxtlGW9CQkUj_AQYVyMddrrr1lE-qa8ZejB56ouMVzl-3L-EVx7TLHYaF4T8lEzAmwM4CD6gsJRiLuZJzqzhJRYr71EAKnu8w6L585BNSpkgAaIEm5oXl5-eM7AHA2vQH_MHEfNkdkvqIW2ugaJ4C2M8Ml0NZaZmg2LH2irRQINdcjKhY2kZIa_gK1jM93sw_UQCdESXUQmEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره کارت قرمز بالوگان:
من درخواست بازبینی کردم چون فکر نمی‌کردم این یک خطا باشد.
این یک نفر نبود که به صورت کسی مشت بزند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=CV8mlvt1EQlBT6_WbOf4B0dv9ZcBfiZ4mJYm_zB3IdlHzfyJxSrlMa3mpvv8OYatTNbsqTabwW05pQDx-6K1Yi6FFumdb2dkoApiw9r3RRJeFmt5OYkDSm2Nkgk9D86-iqIpfiGZYqr1OHXsQatkNUvclg193dXl-uHz9ztXD4Jaq7cXW4TR8qftWX0jabdQSzwAsCSdgcM4M9c0M3vNNqj3fn9oPJvT8WZ1gxxO2CP3bPhayc0Pn17YxX9Mlckq-_gOtMfsp6TGYEMeJDcBMd9iWyoY4PFilnQp4P107y0UvTe2cJ53RYhgiZZghZl3iVnqBvXggP5BOsRrF4iBDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=CV8mlvt1EQlBT6_WbOf4B0dv9ZcBfiZ4mJYm_zB3IdlHzfyJxSrlMa3mpvv8OYatTNbsqTabwW05pQDx-6K1Yi6FFumdb2dkoApiw9r3RRJeFmt5OYkDSm2Nkgk9D86-iqIpfiGZYqr1OHXsQatkNUvclg193dXl-uHz9ztXD4Jaq7cXW4TR8qftWX0jabdQSzwAsCSdgcM4M9c0M3vNNqj3fn9oPJvT8WZ1gxxO2CP3bPhayc0Pn17YxX9Mlckq-_gOtMfsp6TGYEMeJDcBMd9iWyoY4PFilnQp4P107y0UvTe2cJ53RYhgiZZghZl3iVnqBvXggP5BOsRrF4iBDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره بالوگان بازیکن تیم فوتبال آمریکا:
بالوگان بهترین بازیکن ماست. او کارت قرمز گرفت. من نمی‌دانستم این چه معنایی دارد، اما بعد شنیدم که به این معنی است که شما نمی‌توانید در بازی بعدی بازی کنید. این بسیار ناعادلانه است. چگونه او را برای بازی‌ای که هنوز بازی نشده است جریمه می‌کنید؟ من درخواست بازبینی توسط فیفا را دادم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=UNijXBbANqyBwou9mEDR4Shfvax89dOGgukFnkiI-lgydyTOd6i_7C3qEzagapMJfsXmMVusDRrN30hBvRTTGYP_tlTZjGx1XUCpzVlOSH_dnln1MulO0_ZBWLf0tRnQSeeJnccxvwhvoRXKZwYb1BVAVa4pkQg20Bk2Cdd91Cksk8R6rylJiqU52QRYoZe-JCWx7dK3tww8xD-5pQ--2cUAYJZt2H-7Y2TZFDsC6Q5ET782uNJfqQ2OFV9r1_5hu-2Dzp1eFsM-r4_M8GHb3VuE5f0hDRo4ZwcPfPJ6XjnKxrGbmRmUdNSIq4luqLsZhw0k1e0mAdwnCGMn8NSFCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=UNijXBbANqyBwou9mEDR4Shfvax89dOGgukFnkiI-lgydyTOd6i_7C3qEzagapMJfsXmMVusDRrN30hBvRTTGYP_tlTZjGx1XUCpzVlOSH_dnln1MulO0_ZBWLf0tRnQSeeJnccxvwhvoRXKZwYb1BVAVa4pkQg20Bk2Cdd91Cksk8R6rylJiqU52QRYoZe-JCWx7dK3tww8xD-5pQ--2cUAYJZt2H-7Y2TZFDsC6Q5ET782uNJfqQ2OFV9r1_5hu-2Dzp1eFsM-r4_M8GHb3VuE5f0hDRo4ZwcPfPJ6XjnKxrGbmRmUdNSIq4luqLsZhw0k1e0mAdwnCGMn8NSFCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
یا قرار است توافق کنیم، یا قرار است کار را تمام کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود. ترجیح می‌دهم توافق کنم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم. می‌توانیم تأمین انرژی آن‌ها را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، بزرگ، زیبا و مدرن. آن‌ها اکنون هیچ پولی ندارند. ما به آن‌ها پولی نداده‌ایم. می‌توانیم کارخانه‌های تولید برق آن‌ها را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر کارخانه‌ای از بین خواهد رفت و آن‌ها این را می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f387513a36.mp4?token=tNnkqJJ1JEu00Hq5mYmVHVa2WH_pvCHcxQ9Rg753Tf72m_5yMtWNhdF3KoKSft2vVR-H8LAefOfKTzW6g-_-Wnu3MN5_3id45tN1wS0ODCiDKOBpB3uAdqyAdnYfSeobLmiRjXUI3XSBycL29aLVVzOJvRQ8jX1U5IWlzAT4qSND2M2lL9HWbYc1Enq2V4WVPGPOJSUg-KkJiVacE34PyP2XdnKRdcsomhrxG8KPY-AQGX-WEREYIT9WzQjeAda6ZoUh_Z_0GCMr8cK-seyY-8NFlBjIgGlkt5I43thaS0Vc_Vdx7G_lW6HWaks_bQF9CKgiZaF5MUIKfmSzNCXVLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f387513a36.mp4?token=tNnkqJJ1JEu00Hq5mYmVHVa2WH_pvCHcxQ9Rg753Tf72m_5yMtWNhdF3KoKSft2vVR-H8LAefOfKTzW6g-_-Wnu3MN5_3id45tN1wS0ODCiDKOBpB3uAdqyAdnYfSeobLmiRjXUI3XSBycL29aLVVzOJvRQ8jX1U5IWlzAT4qSND2M2lL9HWbYc1Enq2V4WVPGPOJSUg-KkJiVacE34PyP2XdnKRdcsomhrxG8KPY-AQGX-WEREYIT9WzQjeAda6ZoUh_Z_0GCMr8cK-seyY-8NFlBjIgGlkt5I43thaS0Vc_Vdx7G_lW6HWaks_bQF9CKgiZaF5MUIKfmSzNCXVLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
تنگه هرمزِ معروف؛ هیچ‌کس تا حالا اسمش را نشنیده بود، اما عجب ماشین پول‌سازی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67384">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=oMp9yUhf-7Bso2pdbrVKtnBGAgaJ1JtXEacBA5mMiR1ozasaQtCM8Umgej6woFgEA-KemMpCHY1Ms5Sxsh_z8RET92FuVKv2vVFxl-6qSxDFgKmPzBcqpGcWNiuvNciw64eHiNmGmUH240XunPqD5cHijsRZygGNFET1v6YqGWlR5P-5lh28dcOxPOl74EJnSdtPfE1Ga9yCKFVlcK4Kno84hYIeZ6CkmjoIq9lVnMvm4MUsdFwmDvmkUxcYG3PT-SKGAGvA5bkpFKKkj7BmFzCEnb4g46KfjW0cmRxmdoI7Ij4Ro7pzaHsk7Xln9jt2ACigouOhBx_Of5bj-4Etbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=oMp9yUhf-7Bso2pdbrVKtnBGAgaJ1JtXEacBA5mMiR1ozasaQtCM8Umgej6woFgEA-KemMpCHY1Ms5Sxsh_z8RET92FuVKv2vVFxl-6qSxDFgKmPzBcqpGcWNiuvNciw64eHiNmGmUH240XunPqD5cHijsRZygGNFET1v6YqGWlR5P-5lh28dcOxPOl74EJnSdtPfE1Ga9yCKFVlcK4Kno84hYIeZ6CkmjoIq9lVnMvm4MUsdFwmDvmkUxcYG3PT-SKGAGvA5bkpFKKkj7BmFzCEnb4g46KfjW0cmRxmdoI7Ij4Ro7pzaHsk7Xln9jt2ACigouOhBx_Of5bj-4Etbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
من به دنبال تغییر رژیم نیستم، اگرچه این تغییر رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67384" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67383">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=gZSWsOt4SQfN1u3juryT1ngSo0jK6ewlNZRP1HVpw-Tkwwpfm2OLSYH76m18YojhQMW8cSVZYqTSRGdd3c0xa2dHhSfMri6tggwgEv8d6bGI536rXpX0pZIAetWfHg1cJ8XkmgEX_CS6wzcqZXZ94o_QibCjWzBE4jb8WzuGqNl0ALdE2hD6RO17KpnFrDAlo8jWynJ93W0MKHolKwUoqkOc_SKEZcAJZWG1013UmDeOB-gB6NdgyEDMZSpe-eDy7K1EIM_B9d2kd4BxV1q-1AKo0Tg9XDeGk_WuxFdbK63EdczBD-z-3UpAoQWKFJ7798GvgW8gIfDdxDijVWpQXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=gZSWsOt4SQfN1u3juryT1ngSo0jK6ewlNZRP1HVpw-Tkwwpfm2OLSYH76m18YojhQMW8cSVZYqTSRGdd3c0xa2dHhSfMri6tggwgEv8d6bGI536rXpX0pZIAetWfHg1cJ8XkmgEX_CS6wzcqZXZ94o_QibCjWzBE4jb8WzuGqNl0ALdE2hD6RO17KpnFrDAlo8jWynJ93W0MKHolKwUoqkOc_SKEZcAJZWG1013UmDeOB-gB6NdgyEDMZSpe-eDy7K1EIM_B9d2kd4BxV1q-1AKo0Tg9XDeGk_WuxFdbK63EdczBD-z-3UpAoQWKFJ7798GvgW8gIfDdxDijVWpQXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
مقایسه اجرای سحر امامی، مجری تلویزیون جمهوری اسلامی، بعد از مرگ علی خامنه‌ای (10 تیر 1405)
و اجرای ری چون‌هی، مجری تلویزیون کره شمالی، بعد از مرگ کیم جونگ ایل (28 آذر1390)
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67383" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67382">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237168e66.mp4?token=glcPmHuR05DECDh5ytdPZdj1OSC8iKwKNqMicfP1gBkSRusMhTgwpgidzo5PFsJ5i-rBRgi_sDXI_znorrUvG13sMomEnf7Zmu6fvnIDOq4ss6jOLXG1mq7-vfmHsT6MJddFEhdDto2o-35oEG6oQPHWhHWf_amZFqmpg3rsVyZjRpVWgV8fJ-ZXSecBbPGP0Yd9UQSH8RWX_QoNp4KWGZVqhH9IoNSfFDtcSRabGFInAydFXJlfGZCLhXCN76uIchges8JWVyij07X3pdzEqan-VHvK6Racd9l9ML71GR4q28L79CvOhclR_oyKIswE7OjoQxfL78tCQYanCapM8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237168e66.mp4?token=glcPmHuR05DECDh5ytdPZdj1OSC8iKwKNqMicfP1gBkSRusMhTgwpgidzo5PFsJ5i-rBRgi_sDXI_znorrUvG13sMomEnf7Zmu6fvnIDOq4ss6jOLXG1mq7-vfmHsT6MJddFEhdDto2o-35oEG6oQPHWhHWf_amZFqmpg3rsVyZjRpVWgV8fJ-ZXSecBbPGP0Yd9UQSH8RWX_QoNp4KWGZVqhH9IoNSfFDtcSRabGFInAydFXJlfGZCLhXCN76uIchges8JWVyij07X3pdzEqan-VHvK6Racd9l9ML71GR4q28L79CvOhclR_oyKIswE7OjoQxfL78tCQYanCapM8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مارکو روبیو: سوسیال دموکراسی همان کمونیسم با ظاهری آراسته است.
مارکو روبیو، وزیر خارجه آمریکا، با انتقاد از سوسیالیسم و کمونیسم گفت تنها کسانی که کمونیسم را از نزدیک تجربه کرده‌اند، درک می‌کنند که سوسیال دموکراسی در واقع همان کمونیسم با ظاهری آراسته است و پشت این ظاهر، همان ایدئولوژی خطرناک و ویرانگر کمونیسم قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67382" target="_blank">📅 17:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67381">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=RbmEnmuQOsZmUk6IxciHa38ARknru9lpgISri5DutoTIH0Q7MnG6wp5S2TcIn1fYaaZYehbCOUNteeIybHibbVRAqUZFDLNLNe-Q0xN0mst-WBMSdTocad9j3ZQCsrhLeIJ5DZXRe1iL5sOw4RtQlAqNfWXHes4VjT3YEMLKBFvPofoXUUrn77iCMY4hYuHc3Rzu1ICWkpeUNuooRJHhRZRhdJEPXflOMXktH1rz7gVPYIA7cdiDjxqk1pFS_Edkv7dPiFRIaBWCUpNZ4kDLvubg7xDn5d0-ZZh4K9UuWYic9GvnTNbuamvRAnZw89y2l4RVrZ3ltPvtHE81hJn_yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=RbmEnmuQOsZmUk6IxciHa38ARknru9lpgISri5DutoTIH0Q7MnG6wp5S2TcIn1fYaaZYehbCOUNteeIybHibbVRAqUZFDLNLNe-Q0xN0mst-WBMSdTocad9j3ZQCsrhLeIJ5DZXRe1iL5sOw4RtQlAqNfWXHes4VjT3YEMLKBFvPofoXUUrn77iCMY4hYuHc3Rzu1ICWkpeUNuooRJHhRZRhdJEPXflOMXktH1rz7gVPYIA7cdiDjxqk1pFS_Edkv7dPiFRIaBWCUpNZ4kDLvubg7xDn5d0-ZZh4K9UuWYic9GvnTNbuamvRAnZw89y2l4RVrZ3ltPvtHE81hJn_yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در برنامه ای در صداوسیما حدود بیست دقیقه کارشناس برنامه اسامی سران و مقامات جمهوری اسلامی که توسط آمریکا و اسرائیل ترور شدن رو خوند
بعدش مجری به کارشناس گیر داد که الان بیست دقیقه وقت برنامه رو گرفتی که اینها رو لیست کنید و در ادامه میگه به جای اینکه به مسولان و مردم دلگرمی بدی داری دلشون رو خالی می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67381" target="_blank">📅 16:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67380">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=qsmaavs76elzC6IyH3BNsfyWVNZyLlWxsBLFcAT9Z796RHsrl1HKHQS04vig41k3Eg6_PfnXQ_A3eEkB3wbU4uTG4Rk1uOc2WXILkHIelW8echSqyThNhiuJkdvy0kOxUeqFX1HLX4tQRIkJu3UAU_ypXQPBj_-ZxVMvuC3WmkPoGLZhJ8WS5ePCzJXYSsu3MqzrKdMcFtu6Mkg3JDQT1GhegCwHy5JN570dPinY6Fpx0O5mH294A2uFXkNDp7TBrXxu_0MguWU45H7OSet1y1JvJix9uHAx0Ar7d7ZOGo5rDJYLpBFFeWz8QCixqORKlBsfB3APvbOn2qdLsijaSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=qsmaavs76elzC6IyH3BNsfyWVNZyLlWxsBLFcAT9Z796RHsrl1HKHQS04vig41k3Eg6_PfnXQ_A3eEkB3wbU4uTG4Rk1uOc2WXILkHIelW8echSqyThNhiuJkdvy0kOxUeqFX1HLX4tQRIkJu3UAU_ypXQPBj_-ZxVMvuC3WmkPoGLZhJ8WS5ePCzJXYSsu3MqzrKdMcFtu6Mkg3JDQT1GhegCwHy5JN570dPinY6Fpx0O5mH294A2uFXkNDp7TBrXxu_0MguWU45H7OSet1y1JvJix9uHAx0Ar7d7ZOGo5rDJYLpBFFeWz8QCixqORKlBsfB3APvbOn2qdLsijaSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو در گفتگو با فاکس نیوز:
ایران کشوری با حدود ۹۰ میلیون نفر جمعیت است و حدود ۸۰ درصد مردم آن از این رژیم متنفرند. اقلیتی که شعار «مرگ بر ترامپ» و البته «مرگ بر من» سر می‌دهند نماینده مردم ایران نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67380" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67379">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=pL1xIxQeuRB5XuJR62vPveNtad1C01GZ8mBPdFInhWycLvYkrf7A4zNYr1jKqMBee5QMDBogoIYx0bMTVsm7CKMBw17wcam5ZAuOdzErHCvaBQDWauyyqQOUhN5ZBI6PlUDkq34SnkfjQ1Jv3oZq6UYO0gtkeLhK8QKi-Dq54G9S5exyIrCykhgovgJr7hF6aVlD2A14WAXtmm2vy5bTxuePvafv6LfgZ9PW32eDp6VbuFVKZLmIQHKGzGTKSHtn3th0qM1xK2cjy224MWXbcOgmWAUKONmT6DMbUoXU0e3yeQ2357q-HaT8aj47V4qsbWSUfMdKzWHwPpp2DOBZRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=pL1xIxQeuRB5XuJR62vPveNtad1C01GZ8mBPdFInhWycLvYkrf7A4zNYr1jKqMBee5QMDBogoIYx0bMTVsm7CKMBw17wcam5ZAuOdzErHCvaBQDWauyyqQOUhN5ZBI6PlUDkq34SnkfjQ1Jv3oZq6UYO0gtkeLhK8QKi-Dq54G9S5exyIrCykhgovgJr7hF6aVlD2A14WAXtmm2vy5bTxuePvafv6LfgZ9PW32eDp6VbuFVKZLmIQHKGzGTKSHtn3th0qM1xK2cjy224MWXbcOgmWAUKONmT6DMbUoXU0e3yeQ2357q-HaT8aj47V4qsbWSUfMdKzWHwPpp2DOBZRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری:چرا آن دولت هنوز در ایران پابرجاست؟
🔴
نتانیاهو: زیرا چند صد هزار مزدور دارد که در روشنایی روز می‌کشند و قتل‌عام می‌کنند و در شب مردم خودشان را می‌کشند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67379" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSaY-zEPNelucQJlwGlW6Msz-lPVpKIn5dPsh1oivhEk2EnFRLmHBlE7ro9gj3GYcn3sG8MTQ_9Lbd_6Wq_wqY0LmNg3OD7TFezQBGs1lSUdQSFhTPUaCxa8TKVX_Z3jGKXaiHIp7YUqjDdku7NUquUsEyMdu0pto4IrduBukvzWXDjV6wys0CqiXPQmP-7kjGpORmLbgu376eduZf6c2OoxwFg_q8acmgff0gJiYfjEkpcSJVDg_6M0Rr5WPG3uwpHoeB1CuGPeu-NVYvsttxniHyM5Sg-22fBUFHWHxUhSzLFEtAOxqP-PqP41bo8ZYIeS-uFqnofZz41Wifb3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAgwqVjDQxRbIpL0Uy2oUTo_-_OSe829hDRIhKzzNCuQ64cCb2eG9C1uh6ffAdCrEtPCSDX62CV40TGV_F5co6vlZjJeE5uOcCf3-rfYWUH1B6dUUE-CKUbf2dhQNdVZHCQAkQCUJPR3upcdcSO48njKJvlk9dd8x--bGdNFei9LkR1REgsFaPFhWSA_uCZuaTxjIC3_lRjJp4eRWat0Kt4AckroYksqONgIfPXAZ1ZkVxFYQB1qYCXWBvzD8k8VF3DnuM8A4CvsE1xMMTnf3Ysj41CLElsFO91KGqWyRhb0BHeXbl8W06nox_9AOrbQWkzHhlXN2tvRg_gbth8adQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIZ_7MknV29aqT0WieDQBpcOnhFdPR4MvTPyabpAkHJpiljd4vBtqpMGF9HkckXY2l7aXHp_b7ZwKNWb19Sn6-TXOKT7kYH_Iys-fstDJIX68-MeYBQpLcbqzhkCO5_skbGTa9XFdlsYUS2Ks11V1UUomOaQW-F9gfpsGGhoZJ1dtsgBXF-o_UvjT3W-UofLD_HM0qIz_Bz1FXI-v_qcuHBG2KUHnZj7nr9VaVurhx5F_Rbh-zNeaZrO1DWKPbmANIFmlUy4KNPnMzzfGLzYRW8lOItR23KN3790LwXWOAh8kLn0bdybyNXmx4cHcWopXiJzplEVtvInIHolpx9JvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67375">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2uLp-KHHVXX6mh8atgiMFdCMvd6HN0AnTSIpw73DwuLbuU9buNG26yQiJJLpKZiB_tAnFeKBwCYmZLkGnwe5h0I5xrUqlBKikJL-lDn8zYH-Whm2HDJDMy2pqTbkZdSo824DGposK0Az-iHBvVsu9QcU0Zs_rs0RTopV-VnSGdL5efhmLoPvA0-fnur3HtY9GfiD5fGbAYXc_YDX0VKiYy5H1Cp6UdlD0lngG_zv1HKSTjPWpluJefvM-4nAhZXnt5QzagqjX5dD2ekrdCLUL1XBnfr7VkO589dkkh53WtmvjDSyTYsVOweVzdbpHg6YOA0lN6EON0FpwNgcs0VgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک بنر در مراسم:
دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67375" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67374">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOPecufA8DHrnCyV2zQqRH3R_t15hoFeLyr8lNqZ73ZxHK993eANywRQUsmiBGoSqqg4wx--Bj-ppN9-ykUu6NqnAj4a3r6m5XQUvqQLnJVw6PBwEb9svp2pUUmY7jfrpWJwoFswKg3A3ggHZXX_Cb5KGyfxfgvMbyrmWnARTw0MNNW8-483RulsdUjyx0mbkiU8Hrk7TUalIonS9YklWc2ULdFIo-v5eqtINkkUGQLDvDYe8NVtHVFNE-2kEZLdCc6Qf8IzjC4_fhPTCi0yDVjVR4MkLTRSj4gHc2kkSjD6Rl6h-5aspyaWZfny5_1G5doYrA0aUyiB6oroZELbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ادعای
نجاح محمد علی کارشناس عراقی مسائل خاورمیانه و از حامیان نظام جمهوری اسلامی:
در مراسم تشییع امام سید خامنه‌ای رضوان‌الله‌علیه در تهران، فرزند ایشان، بقیةُالسَّیف، آیت‌الله سید مجتبی نیز حضور داشت. او پنهان نشده بود، بلکه در جایگاهی قرار گرفته بود که کمتر به چشم می‌آمد.
هماهنگی بسیار خوبی با نیروهای ویژهٔ امنیتی و فرماندهان ارشد سپاه پاسداران انجام شده بود…
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67374" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67373">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pweg6sumT8prhv4nKIFIz8b__MT6d-RrWNS0qn4iNxVty9_pM9DZ5hpeIw5YnE-ngF7XkCUvVaif0kN_x1bapNNC9qfns6d9wrFUKe-SlwUHWHrz-IEun1BGmqnbqbDBvWycONttkFnBV3R2MWKkOx6eOtmdcquEBs3_HwfZVyCH-MtzB1MguBBpCqoHcPQsLDX3SGyZggCL-vshNad_8FAs7pfEg7jE-HqzBL7twDVdKeerRhM3svk3MAvGbHSuJstVSRnQ-EwgWwK4vu8ncWzwj52qxCIpkJQLHEaC0zEK7HZnGhpWR-Wwq2-AH9KirHMsKRfIy_H70Omsowjgdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
«آیت‌الله خامنه‌ای که مراسم خاکسپاری‌اش هم‌اکنون در حال برگزاری است، توسط اسرائیل حذف شد. هر رهبر ایرانی دیگری که برای پیشبرد طرح‌های نابودی اسرائیل تلاش کند و اسرائیل را تهدید کند نیز حذف خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67373" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67372">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=RhxUfg_gZchzljwErp-NCdqrgfsPzyGnHDBAud-8NvxcJOzM3TVJueekUj6Sq4y2wHcycbOz-eEJfFcAv-skaem0OsfI6AarA_W-oNxH9ZCAybjt8NZwdsGXh1d4HwkKn0O_GBLPM1PiYsZ0F-Ad0f6ebR255ZKj7RSI28KdFnwqLn-HYQPsIV_Uo5ifGvrbp6uvQ4DnXDXok5g2xGKXWtJM4OocsnRP2J2Z-o6myunPYRPKgpswwiAmsgOcrs6l_XoXObszfLHv1sIteYECjbbpXmVeYeDaCBj-6UOKA8NJe4ELWnWm9bSKNPbnHfbg3YAphdXyeJd0mR47qFvAFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=RhxUfg_gZchzljwErp-NCdqrgfsPzyGnHDBAud-8NvxcJOzM3TVJueekUj6Sq4y2wHcycbOz-eEJfFcAv-skaem0OsfI6AarA_W-oNxH9ZCAybjt8NZwdsGXh1d4HwkKn0O_GBLPM1PiYsZ0F-Ad0f6ebR255ZKj7RSI28KdFnwqLn-HYQPsIV_Uo5ifGvrbp6uvQ4DnXDXok5g2xGKXWtJM4OocsnRP2J2Z-o6myunPYRPKgpswwiAmsgOcrs6l_XoXObszfLHv1sIteYECjbbpXmVeYeDaCBj-6UOKA8NJe4ELWnWm9bSKNPbnHfbg3YAphdXyeJd0mR47qFvAFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور احمد جنتی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67372" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67371">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=pLMg5CBBS1CLg4OAiLcNURK3vAA_vAURZt4_kHk9MwXhFm6ZPfofemI2XRkX2wNmbfvX0oqyFp90EwDkpCow4C9XWxLTud4zDBGO_nUq8AO0wMfIzHCIthfzc3iez085BvpEvsOWuGezSHOuzu_qz3ZvImlSLIs00lXQ93TtwvxKI1HfwxrzZ349EDcT-anrckNvIWK80W6qrsp0O_fCU3RWHlT4LSxTtmn-WuYbq-5mvU7Oe3ijHzu4qkI2VFRFi8mKOR_As9gHSk5d0g0Ieln5lphIc-ZAsjXMsmar24RgcQ7U1DBBqIQaL0YSCBTstwN25mlLG8UZbhNWm1GCTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=pLMg5CBBS1CLg4OAiLcNURK3vAA_vAURZt4_kHk9MwXhFm6ZPfofemI2XRkX2wNmbfvX0oqyFp90EwDkpCow4C9XWxLTud4zDBGO_nUq8AO0wMfIzHCIthfzc3iez085BvpEvsOWuGezSHOuzu_qz3ZvImlSLIs00lXQ93TtwvxKI1HfwxrzZ349EDcT-anrckNvIWK80W6qrsp0O_fCU3RWHlT4LSxTtmn-WuYbq-5mvU7Oe3ijHzu4qkI2VFRFi8mKOR_As9gHSk5d0g0Ieln5lphIc-ZAsjXMsmar24RgcQ7U1DBBqIQaL0YSCBTstwN25mlLG8UZbhNWm1GCTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی عجیب منتشر شده از وحید خزایی شاخ اینستاگرام با سردار رادان که میگه کار دارم با وطن فروشای لاشی،ترامپ گفته گوه خوردم
من سلطان دختربازی ایرانم ،حتی سردارچندبارمچ منو روی کار بادخترخالم گرفت ! اماخداشاهده آنقدرمهربونه،هیچ کاری باهام نداشت و ولم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67371" target="_blank">📅 12:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=MEIuPJ-hAV2eFlThU4vWTi8i8sDFxFdNFaOODRYkb2nRYZ4yYAn_yXOZiqDPIMCZnqS6xEmaF953wpolyJmiFFoGGK_5kYlciZ4owORA4kUdZI1Mqj4nN7q1lCO-FovsbWoPZa2xSF18Uzo-YJh9sAJmA8crcp1Zl2FkdymFG23OLZ7hxYTs1jMovs4rlX9etJ0ztGpuqA2eOMuJAUmz1X44UEXNPAESFNXCxYgI9lzYHalflhzWP-CivkvmYfuWwOs28XU5JObv60CDY2DP8wrInANImyMM5WRA26nuLIjHv5suRGOs4yEF3kzBwDaGF7RhZTR2zZ311j-4fbCLVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=MEIuPJ-hAV2eFlThU4vWTi8i8sDFxFdNFaOODRYkb2nRYZ4yYAn_yXOZiqDPIMCZnqS6xEmaF953wpolyJmiFFoGGK_5kYlciZ4owORA4kUdZI1Mqj4nN7q1lCO-FovsbWoPZa2xSF18Uzo-YJh9sAJmA8crcp1Zl2FkdymFG23OLZ7hxYTs1jMovs4rlX9etJ0ztGpuqA2eOMuJAUmz1X44UEXNPAESFNXCxYgI9lzYHalflhzWP-CivkvmYfuWwOs28XU5JObv60CDY2DP8wrInANImyMM5WRA26nuLIjHv5suRGOs4yEF3kzBwDaGF7RhZTR2zZ311j-4fbCLVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=B7GIGudOeWPCSNTm-yHA23dbs-kC6pwLcXTLO4s1YFHDhXLAhHPm3lsR4OpIThOy6tZBi6upxqETEbhRztcOiXc6JLFJ83eKL22mlPNIriv4St_5Yv6Dq51yrZJq9fTpEDeKX1vm1HkcB-mQqh1ZRQzfcjGCAbKxWhpinZi61CKcGOz8-yhaF3_Yk8uMdnOvrkXTYuc8F2XCl4q4-14o5w1Acg-n9vK1ZQt6xrGUv3Pe-SABLzqsEDkx8gNJ2KyTcMpXWqht6542ukiszbeFQiPh6lKvtYJkp5ZS21qUreooKl5sKh5D0kqCYnScTqcpDF9z-YRJ3FHCJm7hnsIiEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=B7GIGudOeWPCSNTm-yHA23dbs-kC6pwLcXTLO4s1YFHDhXLAhHPm3lsR4OpIThOy6tZBi6upxqETEbhRztcOiXc6JLFJ83eKL22mlPNIriv4St_5Yv6Dq51yrZJq9fTpEDeKX1vm1HkcB-mQqh1ZRQzfcjGCAbKxWhpinZi61CKcGOz8-yhaF3_Yk8uMdnOvrkXTYuc8F2XCl4q4-14o5w1Acg-n9vK1ZQt6xrGUv3Pe-SABLzqsEDkx8gNJ2KyTcMpXWqht6542ukiszbeFQiPh6lKvtYJkp5ZS21qUreooKl5sKh5D0kqCYnScTqcpDF9z-YRJ3FHCJm7hnsIiEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عباس موزون، مجری صداوسیما:
چند بار [روح علی خامنه‌ای] از بدنش جدا شده بود و تا ارتفاعی بالا رفته بود.
«اصلا بعید نیست آنهایی که علیه بشریت عمل می‌کنند، از نیروهای شیطانی کمک گرفته باشند.»
چی میگه این
😢
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67369" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67368">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg1XzhkcSz3JbPg1NishYkP2E50rk1ibgGm4WZJNIfUADGvvFFz6P_7B5NfkDk2U2m9cXvYjJ1D6DxmfFpi4rLA7dUbkUfbUFg7D6FNSfxWkUmVxfGOlMwkneD8zIzcgrAX1zwwjCjvIIT32mPfVzV4JAX5YYDHYunpASeSS7yvrevDSP6Bxk_ALOLIIBC-cXIKd5-P2bIELWq-29oD_NRxYa2c6EO491CRAEXBSXYP2EO_eQDqHHzA1s26ipnEVuyjDqSr5lOb6nDY_yBZhfNZo82AlEO_bE02elwiesrgv-1cTjcuXFRWg6XYRmFvzjszZ1haa_zrUSkHMnMuzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67367">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=KysYO4LzXwoi0zEUqmJyo_4pjKUUAZc705WxJ1eODL_5cE8cKroEWXj1Kof6TBqgxAL_UHEfOzkIQAu81rX0NPMYeDDh3zLRXAxnyUBSyRHDT7lW0q9uSkuUSMrqZAxqjsH9t_lQlXCQYTIPOmj-_-sIB8KWfCQJOBeCDvQkiURM29qR0PvQ7uMrBVXeM2ceJJw5e4c1oG8KC1YdrFzDjsmsrRrBZ-j1K6-z_OQg16AmdXH4NxV5qbsAeZ05xibfgZfN_XSrOTsoEs2Wnf4j9rm_qsGmoW3riHtLdywYoi4fXOJq2tnmkx0rsXwqYwoucPKrIP-o3Pm50eyiG9v2YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=KysYO4LzXwoi0zEUqmJyo_4pjKUUAZc705WxJ1eODL_5cE8cKroEWXj1Kof6TBqgxAL_UHEfOzkIQAu81rX0NPMYeDDh3zLRXAxnyUBSyRHDT7lW0q9uSkuUSMrqZAxqjsH9t_lQlXCQYTIPOmj-_-sIB8KWfCQJOBeCDvQkiURM29qR0PvQ7uMrBVXeM2ceJJw5e4c1oG8KC1YdrFzDjsmsrRrBZ-j1K6-z_OQg16AmdXH4NxV5qbsAeZ05xibfgZfN_XSrOTsoEs2Wnf4j9rm_qsGmoW3riHtLdywYoi4fXOJq2tnmkx0rsXwqYwoucPKrIP-o3Pm50eyiG9v2YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
خرافات پدر ایران رو در آورده.
آینده ایران در یک جمله است؛رنسانس.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67367" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67366">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=t1P-uHD6e10Yu3-ngtVkIDShiWcrWTgv0WM4BhMkNtjsIly75t7DBTIQm42OFUer3H_dQrRkP9-zTxEZZgCZluv7iIrnnQUT4kembpUjTiS1Ga-94FJ4bSBWfqtmSYSJmt-TMJRaYNGx3TM9Pgl-cTns29IrDlNdOzgc7a_FDOA1IsNrHlEF1ZQ5waGENw1l8uSGoz9Muh0TLAyLRr6EM7oru5gACNWImXBzABpwbaOp6lUT7zOSl4eeDC79eSo5jLK4pBIg8Nm8IjWvO8hNsICH4fpM3qrYN3tRkWC8frkPg7jxP2Yn_wBZApEUKbSNmmRd24dzP69hIUhMzheFhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=t1P-uHD6e10Yu3-ngtVkIDShiWcrWTgv0WM4BhMkNtjsIly75t7DBTIQm42OFUer3H_dQrRkP9-zTxEZZgCZluv7iIrnnQUT4kembpUjTiS1Ga-94FJ4bSBWfqtmSYSJmt-TMJRaYNGx3TM9Pgl-cTns29IrDlNdOzgc7a_FDOA1IsNrHlEF1ZQ5waGENw1l8uSGoz9Muh0TLAyLRr6EM7oru5gACNWImXBzABpwbaOp6lUT7zOSl4eeDC79eSo5jLK4pBIg8Nm8IjWvO8hNsICH4fpM3qrYN3tRkWC8frkPg7jxP2Yn_wBZApEUKbSNmmRd24dzP69hIUhMzheFhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم وداع با جنازه علی خامنه‌ای، وقتی نوه‌های خمینی میرن جلوی تابوت سید علی خامنه ای، قاری این آیه از سوره نساء رو به کنایه می‌خونه:
آن گروه از مؤمنانی که بدون بیماری جسمی در خانه نشسته‌ان، با مجاهدانی که در راه خدا با اموال و جان‌هایشان جهاد کردند، برابر نیستند.
اونا هم برمی‌خوره بهشون وسط آیه ول میکنن میرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67366" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67365">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfllXsB2ux5hGOYLlvxOmHnqe0Ls0ZrjeUAPs32fLwM8gJICJJczzfjsJa0EzoW5MgUIxLDw21SpzVQ7wdM18oiTv9YsYtJhoCxeL2MpmZaGiiXkCvz6I1Iv1F7ILuHow_Bz1EGZJWcDDC3oquaD88g6ejF1vrFIWEp5ue2_0cUvCAsAC37fYSLzFW4ylgiAx6SA46qkWVTX14aXBZS-Ean-lO5qOzPNpKPudTTR6A1x8P_Q1H62lbYMANxH9C-EwlEHpgmQg7XeMQPjL7Ssf2ey74r2eQBqhQPS9IKX28Va77V56G8Cw30Zgz2jh0eGW__bqz8h1KPnTyWw-_qToQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
قالیباف در گفتگو با محمد درویش، رئیس شورای حماس:صلحی با آمریکا وجود ندارد و اسرائیل را به رسمیت نمی‌شناسیم!
🔴
دیپلماسی باید در خدمت حفظ و تثبیت دستاوردهای نظامی باشد.
🔴
مذاکره زمانی موفق خواهد بود که کشور همزمان آمادگی دفاعی خود را حفظ کند.
🔴
ایران بر حفظ تمامیت ارضی کشورهای منطقه و پایان جنگ علیه متحدان خود در محور مقاومت تأکید کرده است.
🔴
جمهوری اسلامی صلحی با آمریکا ندارد و اسرائیل را به رسمیت نمی‌شناسد و حمایت از جبهه مقاومت را در قالب‌های مختلف ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67365" target="_blank">📅 09:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67364">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67364" target="_blank">📅 03:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PGNUHmZBXAi9Cv4I60X5vAqbNZQn95bVdmm06Nc7OhKtoBUC2j-p_7aclIazy6cZSGy98mx5Z34qY5WUJUD8T8Rk9PJ1dS11psPQwWFKOg0KTpI5nqm9KzBTlVMF8yRJtfBs7LW1UyWkxl8a60ygmqsksClKdYHxAFh8qJl8ROp19JzOhqjUYVVLdB2kN7QHrv2x7eGpwNcmqDKDGLTlT5ekPZNr4Kac0LtSX8cTuVIN13RDzqq-2D8ASxEPNQrTsVxb5FiEztexrZLWW0a16OkEjZIkdRUvMR0nCBMySN6G1pjOAWSdT4O1Ed_me9fv22R7XNvpTVHC8bY3zL__Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=PrEN1CVWMtGcSDC5IRUZkxIHNDYBYAcYRHitGcI9AbYlVMJrYvre4YqyPNl2hQsVqYWV7RLWG3WvCKOc1QnIIIdzS9yFzjBuNr_K5JZlzvgjsEjXBe_EdmgC8Qr0plbw3XNoNnWI7ju7ate-jFSd61PM0Fuvjc-iHGvZNIprL_hnn5JVPiqO_icJ-NQnot_s85p3Hysz6cv2s4jm5tTCTccgfGI3mdwmWSrf5GFR7v4LRpG3d_BJbL44TsWHt0YWbV6JDWmpkTLImbZeocz--fPjiJAmDo8kbkBdxhNmUEuuXt6lP0ibU36wio_gH6xalnWr2lnxZQRky1OaajFmBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=PrEN1CVWMtGcSDC5IRUZkxIHNDYBYAcYRHitGcI9AbYlVMJrYvre4YqyPNl2hQsVqYWV7RLWG3WvCKOc1QnIIIdzS9yFzjBuNr_K5JZlzvgjsEjXBe_EdmgC8Qr0plbw3XNoNnWI7ju7ate-jFSd61PM0Fuvjc-iHGvZNIprL_hnn5JVPiqO_icJ-NQnot_s85p3Hysz6cv2s4jm5tTCTccgfGI3mdwmWSrf5GFR7v4LRpG3d_BJbL44TsWHt0YWbV6JDWmpkTLImbZeocz--fPjiJAmDo8kbkBdxhNmUEuuXt6lP0ibU36wio_gH6xalnWr2lnxZQRky1OaajFmBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ارتش دفاعی اسرائیل:
پس از فعالیت در نزدیکی نیروها: ارتش اسرائیل یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را در منطقه العقیده هدف حمله قرار داد
امروز (یکشنبه)، نیروهای تیپ کماندو یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را که با موتورسیکلت در منطقه العقیده، در نزدیکی منطقه امنیتی محل فعالیت نیروهای ارتش اسرائیل، در حال فعالیت بود شناسایی کردند.
فعالیت این تروریست‌ها تهدیدی برای نیروهای ما محسوب می‌شد.
پس از شناسایی، ارتش اسرائیل در یک حمله دقیق، این تروریست‌ها را با هدف رفع تهدید هدف قرار داد.
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود ادامه خواهد داد و به سازمان تروریستی حزب‌الله اجازه نخواهد داد به شهروندان اسرائیل و نیروهای ارتش اسرائیل آسیب برساند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yi52Aye8S0FX8lBZ74mtwAasZ_WvrdoXSPc5d3c9lf64PEuR9ofnQrzSZAnPnlD-jdkrbIosTkoGa7Q3t_SC7w9IMtr3CtF-QYStULOSKuex0mV_GtjIcoBPpM7ftcpAGvs0eRbUwG_CWnh12ST3ha_fTJejQSyuEWJTEVCwQFrnjlW4l1AaVvu31wuTfjh5nSq6yc6ioPx_WpmiOufJoT1elJiX46SGy6C5tERC3Fln8pzQ-P_9BWHvq1N_A-TJ9eFinJAqFkX8u0x1SZfU8PfAUpLco2AMkkiBCiFwdQY8tH6v5eJHgbtYPRO09kbN1fAfarM80YScR5BNYAsnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=lINeNOyjCrL9sbFihL67KyWaw0x_4PZsJVL4gySWjHKrEMEJ523B2q4_hvs0mxjP_uady90RFt0N1cavPruuv47vOiJfuYpY4e9Ky5M2VFcNBXNLRjHctdVI0tU485SVxAMUHMLalPYzQsBBnbbQn7incsKSXydt54krcR7_qOviSGhLRTNZiX7rTMMCXOeA_QJKJDvXsU02NilH2lHbYyUQ3L_MKtPYXLt0OSC-UHtDD9cqF5wJZPLKs3FgYkpm7rr1iu_No4ioN572gV8TD4UXyVVcgTNasg_jKHu3Vk7cGGnTOM_8w3-BIp6GsRSb44Qow5kzsgL-eTTLp4WiQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=lINeNOyjCrL9sbFihL67KyWaw0x_4PZsJVL4gySWjHKrEMEJ523B2q4_hvs0mxjP_uady90RFt0N1cavPruuv47vOiJfuYpY4e9Ky5M2VFcNBXNLRjHctdVI0tU485SVxAMUHMLalPYzQsBBnbbQn7incsKSXydt54krcR7_qOviSGhLRTNZiX7rTMMCXOeA_QJKJDvXsU02NilH2lHbYyUQ3L_MKtPYXLt0OSC-UHtDD9cqF5wJZPLKs3FgYkpm7rr1iu_No4ioN572gV8TD4UXyVVcgTNasg_jKHu3Vk7cGGnTOM_8w3-BIp6GsRSb44Qow5kzsgL-eTTLp4WiQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=k6RF3oufIEtgCVRURn3MIni3NWlMHeCDdl2Uo5Va9LNndmEr83zDUYy8sVF6eO3YR1ugrASRLeqHgwdSEi-YADvgk6Iq7-3HtV9uE8iIFY29kulupvob6YRavl9VH9U01mSp0TTKWmSdBQ2Wm_QQZZaOuA9TRvbjQzw9Xuj4ytbe8WD7YVUp3v2i5IQCCgFlEqrU3tSwbcqb0fisfji5vqAKE1hg4Jib9Hs3NREuHv0S7xu4UrnBfYoXFNBi5oemxqI5Ms6uKU2CxWdHzkqnwat-Bo5MkblFdXwYHqIw9CMLIwmDHipGehCyOsH_4gqPtGOpfbR-O7gEkwhmg3AWWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=k6RF3oufIEtgCVRURn3MIni3NWlMHeCDdl2Uo5Va9LNndmEr83zDUYy8sVF6eO3YR1ugrASRLeqHgwdSEi-YADvgk6Iq7-3HtV9uE8iIFY29kulupvob6YRavl9VH9U01mSp0TTKWmSdBQ2Wm_QQZZaOuA9TRvbjQzw9Xuj4ytbe8WD7YVUp3v2i5IQCCgFlEqrU3tSwbcqb0fisfji5vqAKE1hg4Jib9Hs3NREuHv0S7xu4UrnBfYoXFNBi5oemxqI5Ms6uKU2CxWdHzkqnwat-Bo5MkblFdXwYHqIw9CMLIwmDHipGehCyOsH_4gqPtGOpfbR-O7gEkwhmg3AWWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0W9k83XrG_S039IG5mTAbjLap-_SnbKtGQZOvpDe48jSa8RjjYHrYrODGUD6uH1af_DO8iixNIe6dK8_0l9HbBh3u1c0TLtiZRorRDF3CcvI8vaCSe7FshLw_pws-lG3SBeccbv7zY4XmV7N8j5K1xtJrR4SajgyRKU4eUW6C1hWq93Qcinjcad8yRUj35f3YfAe66d9ckqu75x0AwSFOzazjEDKX_ON01WYZg9kF65SMrZLWaK325E7SOEwY15FXDdsK3j31LuJiIH_yHwjIAGCIOfpYH009N8Tugz3WRQVYsisqdd48vY5tdRaXc_ikbq88GKfh9qkaCTtf5UKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=Od0d-sWd5yk6QS4WQFhSqiS_fkqQ4whxkW3cSiLhYNaWSz9IoMH4hXf3cUEgWxM03ynjX6o_eZd01-6YXpbnOri0fHBOj713Dwkn4Mxmpw5SEZXkvNQ9UMNcJSZzcu8uG3xnCivkygE93sVGU1CVAKv02fileYk59e09plbRanZqoHFav_5jUTeBpkFv2GsoiYQgcoKGbBqez9JTVP94yBBzHTbH3QsiAeDFANoMgCD2pAR9tJ0W-QPaTZs5KMdkfcbjqX9rhGm3SIWFU4dNK-UJ60nxp6runRBu0cv293ybFoglfYPAlqDp9YcMPWXVhJ7iok7TttHe_1mvgc-f7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=Od0d-sWd5yk6QS4WQFhSqiS_fkqQ4whxkW3cSiLhYNaWSz9IoMH4hXf3cUEgWxM03ynjX6o_eZd01-6YXpbnOri0fHBOj713Dwkn4Mxmpw5SEZXkvNQ9UMNcJSZzcu8uG3xnCivkygE93sVGU1CVAKv02fileYk59e09plbRanZqoHFav_5jUTeBpkFv2GsoiYQgcoKGbBqez9JTVP94yBBzHTbH3QsiAeDFANoMgCD2pAR9tJ0W-QPaTZs5KMdkfcbjqX9rhGm3SIWFU4dNK-UJ60nxp6runRBu0cv293ybFoglfYPAlqDp9YcMPWXVhJ7iok7TttHe_1mvgc-f7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1jKKtIcDO4CPYladPzEa0hbKLOUr2JpTeesbAIZ2TpX9-Q6-3_6N6MvWqoJW4KV5D_VX8wjXUh7FR1t9CT5cwc1f-yK15BPcNE-sS1loZWAr53lyOYGNmfM0bu8hGhpAK8uDwpkQmxwDV7Sp7h6NS37sd3GvLBgky08m333cijX4kgCynTbmuVBcESCSeq9DmPoC5PuGBsm9PnBEcfnSZwVND4LyoCuoVocyV5TGlekUroU9TOJWiCte-VanikF0XRvGqdYqEHOdAV3qloSOzjt6hEy5f8b9-xeqCsxpGKdeo8TOoP564aLerAenuYdxILlTL2z5FJoUJQy8AUJTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=EvJiqpH4E8R3BO9XpyWT5LjQ3704NbWhHHPmfDXSbe4K9yFG0da0eTCBJVvLRSmUBFVWFq3jDuAOBa0IKJ2RCr6UPApJML7nuYD0iZIe8oiBcPfZ60MCBoNP4aMvraFkewUHrED4W53sZvDkDy5eoXoikWor6jnwt_ikjMG5_bftvLgKp_-qx_vnMfNTWjICR1-rIYblf7sfJ9pBPE998mkx6VThXA4u-mzjNkwZsNKRcDjdNIvetYGYMVLVKJqWTZljUPaP0UQeEUzcyJPLbNsd_xt7yIQzQVbwidbAg0QFd5L3U52vJz2g4PTKWNJNQ_LFU5aa-Dys9VGIbWHKlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=EvJiqpH4E8R3BO9XpyWT5LjQ3704NbWhHHPmfDXSbe4K9yFG0da0eTCBJVvLRSmUBFVWFq3jDuAOBa0IKJ2RCr6UPApJML7nuYD0iZIe8oiBcPfZ60MCBoNP4aMvraFkewUHrED4W53sZvDkDy5eoXoikWor6jnwt_ikjMG5_bftvLgKp_-qx_vnMfNTWjICR1-rIYblf7sfJ9pBPE998mkx6VThXA4u-mzjNkwZsNKRcDjdNIvetYGYMVLVKJqWTZljUPaP0UQeEUzcyJPLbNsd_xt7yIQzQVbwidbAg0QFd5L3U52vJz2g4PTKWNJNQ_LFU5aa-Dys9VGIbWHKlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVFsGMJH9zlsbXonr1y4U6bTPsd1LqgKxvLFOKZexCbCBKTREV8DaedJgSAwsIctKjecDinZwZTvi_PL6NMrNGtEFopbbotBqwM6LeOmzPgz7JRITaUPLhaY8NGqbdt7ecCA7nsrHvEKcfyiNnIKRx3eV1Ozg_f1RznmI7mIJl4TjAGX0wagbAthlT275Z1EcuzcbR04V_EcO5KOE66zkydk8se6pG8DbLlNO88XI9FQ_Vwef0BqgRUYrQ-oLfk4SCD5VTFGNOJG_zmycNH3heYiJSL-VMFZJjeyNaJp2aa5BoZMUVwF5tb7eScAD5SgcBxbhRWeQuqhfUdLkP8CFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=OuTaMHlc7mnWoPZGw5qV1SnQE-YvoXwTYtnjaGBVjZQnBWhIsVYf5Z6icb5vjB-KnbTW1BY_djcq40Hkj_Eqq8-iGHTCPhILozB-tcj31IoNEjnj_G0WDaNsT09_8O6jIAoJil4NVC2BjwR-3fqfahISU_AxqWrcFahX8O10ehqdHgrRdoJ5yV8nY5N-mCEVLUWOv1v6jIBDgK7XYIs0YDr-5D_k4tPMeftkfDGD2As05tSJTJ5oYcUw4vy-8dtrZLJr0vjkUxKcitNZRQ-NuiI-b0CY-vhvZL4ygRtBeFQzgZIm0BF5E1ktnME_LAMeSZcyg1xFQx4h7iAS_CWvtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=OuTaMHlc7mnWoPZGw5qV1SnQE-YvoXwTYtnjaGBVjZQnBWhIsVYf5Z6icb5vjB-KnbTW1BY_djcq40Hkj_Eqq8-iGHTCPhILozB-tcj31IoNEjnj_G0WDaNsT09_8O6jIAoJil4NVC2BjwR-3fqfahISU_AxqWrcFahX8O10ehqdHgrRdoJ5yV8nY5N-mCEVLUWOv1v6jIBDgK7XYIs0YDr-5D_k4tPMeftkfDGD2As05tSJTJ5oYcUw4vy-8dtrZLJr0vjkUxKcitNZRQ-NuiI-b0CY-vhvZL4ygRtBeFQzgZIm0BF5E1ktnME_LAMeSZcyg1xFQx4h7iAS_CWvtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=QwBdIIobeDAILuXUKLZaMhfaFSxDrn8ojiesQp4UhV98o3WUtYEWCA3Q5tsMiB8vmDbK5yI-oEfMHqveJPhFoUvmZUiMowbiX7M7pIiq6PykMugXp6oqX-yE6nXOBijdJB6dboJM0iMH6wMUopVh328_7K7DoaYwSlA7NBKeXDOt9rqWLjvMlZ-H4gwp9m4F61hPrzSWPfGUdZpMd68i6uFr6p43p4r27LsmEej0g0x3kdT-Q9h0PE-RBwlRt-yjjXFG9jLVZ_nYcGEszUzxSmjxOpyLQ0iUgo8cfQBxF4ZEDX-sanMNgg8x-rPsPekzr_ZUN9MZNnTJoS8LrBnOEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=QwBdIIobeDAILuXUKLZaMhfaFSxDrn8ojiesQp4UhV98o3WUtYEWCA3Q5tsMiB8vmDbK5yI-oEfMHqveJPhFoUvmZUiMowbiX7M7pIiq6PykMugXp6oqX-yE6nXOBijdJB6dboJM0iMH6wMUopVh328_7K7DoaYwSlA7NBKeXDOt9rqWLjvMlZ-H4gwp9m4F61hPrzSWPfGUdZpMd68i6uFr6p43p4r27LsmEej0g0x3kdT-Q9h0PE-RBwlRt-yjjXFG9jLVZ_nYcGEszUzxSmjxOpyLQ0iUgo8cfQBxF4ZEDX-sanMNgg8x-rPsPekzr_ZUN9MZNnTJoS8LrBnOEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2qVphAQK_QJ7x8lCVyC4-gHHWtQAuENmSUYUmHis_L3wt0uxN14XmK5fAlhAo35nTf6c5WbXXJzaKySYObXFtcTS01vylhtQ6XGZYfXf7bmWLoo9j7ijYY50XP-xkR3xBszmj6Zd20I5xmWx88cGssrn4a_l7BwHDD4jYjGkvoKy6JZsVZv0iuAF0OHTjstNyMfsngdvbS8e2kbw8EEWsJmc73xEPBqhMBaLdeFQgHL7LTKOgysu4mmZPQRl7whos4kKWJYQa506BXsmexY2ER1Faucr406XJEutYWQDazjfacyEkVfbNPNI5Gqb1f1WPqg4m6REEIRLQ4tstNKDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPv4c6baUgseXj40JOO2xuUvZbIxEqJNHXnt7nHZ_IMv-Yy4yVsxeTnuWchajdwzhbRMXH0H7-oREiAwHJX0EzO6ohscOAX6uSCd3_gygjDhW9z2sNoXokKMKSCb1aFPIidka-vJAIleG94MQnkDBEI_XWHRlmI4IRocnNMzVp5NlQ426Il4CJnNYvYlRzK0tVxhhIe0J5_aHmBWjMuFqqiggL-i20iZltW0kOm7dgvmKHp-YSGampDgHJTEIezWVLz_cWX3jaPnCUgnDMs7OWuuXs0Sglj7d7U0WnmkwMOgTRQ13C2vgXZd6I3j0GyxtEB1qa6uh5LKcrwfoNS0dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=n6o3w7yTAjxZIbkpkevGfr4hrTkFoigYul8zXcaLq8z2y9erMPzbAPMBL5DUlici-zj8uOkAVKAP-aDSMe4LQdpUZe-abhZBl5klXWp2WvVZ1TLrtwxiD80OmVwuMjPRmdQKLhlOwZpFL5ZE5XliJ2eHO7eAVSNBnyig3BT-KnpqzI6ZGPIUl-xLl3Y4jxwh3DzJsr6pFHZxdwEW311IcucxSe2wVX_dRQ7C7Sq-BSZ-8KdxcUCb1lPQO3qVOjB7zwKk1_TBlJQwqHJad239LVj8pCwbI5E7pbRJIP_630h0D04Kzz_INYYmPeBRS51I_oPESKJGko7PcBvYWbcRbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=n6o3w7yTAjxZIbkpkevGfr4hrTkFoigYul8zXcaLq8z2y9erMPzbAPMBL5DUlici-zj8uOkAVKAP-aDSMe4LQdpUZe-abhZBl5klXWp2WvVZ1TLrtwxiD80OmVwuMjPRmdQKLhlOwZpFL5ZE5XliJ2eHO7eAVSNBnyig3BT-KnpqzI6ZGPIUl-xLl3Y4jxwh3DzJsr6pFHZxdwEW311IcucxSe2wVX_dRQ7C7Sq-BSZ-8KdxcUCb1lPQO3qVOjB7zwKk1_TBlJQwqHJad239LVj8pCwbI5E7pbRJIP_630h0D04Kzz_INYYmPeBRS51I_oPESKJGko7PcBvYWbcRbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=vCdNdRsGdV-33kAhCtp6fBCaM30xCtGekojqxSz6aGMUNnBr84lCT2f-JS2CTQbBU46jywCi4CR-yZXx4mqBFI6-VEgpxsK65yQb8U3i2-6JBvFtohhI6IgPsm9vcYVs_2ZSvIthJnX_bIElyjlL6fYA5sXXMe-LBi33o-4kBgvRW2tKNomYm4PqO8D6FOl-Uarshyr3nrJvt_Kp-davSoaBodLMM2PchJkzTiwghK4yj1J3S3qgJoNCkLbUgHOPjWUIPglG4kh_aYFa_7VuhkhScvg2SKkhzldEttNkfUfccf2pIdA93xEzxrxf0HjJDcuFNDhWFlARdaYBOmugDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=vCdNdRsGdV-33kAhCtp6fBCaM30xCtGekojqxSz6aGMUNnBr84lCT2f-JS2CTQbBU46jywCi4CR-yZXx4mqBFI6-VEgpxsK65yQb8U3i2-6JBvFtohhI6IgPsm9vcYVs_2ZSvIthJnX_bIElyjlL6fYA5sXXMe-LBi33o-4kBgvRW2tKNomYm4PqO8D6FOl-Uarshyr3nrJvt_Kp-davSoaBodLMM2PchJkzTiwghK4yj1J3S3qgJoNCkLbUgHOPjWUIPglG4kh_aYFa_7VuhkhScvg2SKkhzldEttNkfUfccf2pIdA93xEzxrxf0HjJDcuFNDhWFlARdaYBOmugDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما در وضعیت دائمی جنگ نیستیم.
من خودم، به همراه رئیس‌جمهور ترامپ، چهار توافق صلح را به پیش بردیم.
تنها مسیحیان لبنان نیستند که از ما درخواست حفاظت می‌کنند.
دروزی‌ها هستند، مسلمانان هستند، مسلمانان سنی هستند و حتی تعدادی از مسلمانان شیعه نیز همین‌طور.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=E0IYx-8C-7PEJAHpJOGSCdAlGwheHOMWO6OAOhPKnHbYTVU_Z4DQHk5XUBMXILYlqR0nLGvaXkgbg3x9RIie3QrxdOB_W_R6M8nAVIsTequlFrOws3I2Wi4QvqOY5KLF62blxyNqlpjBgUTvju7OkVocvSkIpU9qarvO6CNwSLEmVDnqEyqBjFajBgFAroCooTbccUgTXwdftXx9BQNot4SY77AMHLsw_d92L1se66ZlxQ4vZNTD5EPLQkI2lXxmwW8j-ebghIqhwFncZlvE_it7VsSu6wLf7TZB91oP8Bq3gATk4IJwGKrNJBBGZmdcjwhiz8rbkgOEPewmQW1m-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=E0IYx-8C-7PEJAHpJOGSCdAlGwheHOMWO6OAOhPKnHbYTVU_Z4DQHk5XUBMXILYlqR0nLGvaXkgbg3x9RIie3QrxdOB_W_R6M8nAVIsTequlFrOws3I2Wi4QvqOY5KLF62blxyNqlpjBgUTvju7OkVocvSkIpU9qarvO6CNwSLEmVDnqEyqBjFajBgFAroCooTbccUgTXwdftXx9BQNot4SY77AMHLsw_d92L1se66ZlxQ4vZNTD5EPLQkI2lXxmwW8j-ebghIqhwFncZlvE_it7VsSu6wLf7TZB91oP8Bq3gATk4IJwGKrNJBBGZmdcjwhiz8rbkgOEPewmQW1m-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
روستاهای مسیحی در لبنان...
برخی از آن‌ها در واقع درخواست الحاق به اسرائیل را داده‌اند زیرا ما آن‌ها را در برابر حزب‌الله محافظت می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=VkZelXPhq59h5YgpyHC-7RM27gcdUBMkUcOsieMRj3905qEoMWxd4Mu9lf7hO3G0vpRFyNFAeS1mvxc_F1VasXAEDui-ZqxufIkrPnkZ80GFm0zEAOK6uqcRrPPjC5XEFCsE1LLGdCBIsvE5Lm4o-uEP6h-80jgBbkMyqu8ZGK1yPNEm-1mTQMbe0qanAAKQtCG-gmOpzAoN__ir3Epo6-YrTdpCOg9-mFY-0XziaQpmWkatetrKgHDUV8itUVHVu_PnXcgVlmAjLsL8FreJo-R1X1uaxUmbOhqUsQVnNcqRAO-wzxHroi-_HVdrtr7XoWuLwaeKTJztlxHkwVVPmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=VkZelXPhq59h5YgpyHC-7RM27gcdUBMkUcOsieMRj3905qEoMWxd4Mu9lf7hO3G0vpRFyNFAeS1mvxc_F1VasXAEDui-ZqxufIkrPnkZ80GFm0zEAOK6uqcRrPPjC5XEFCsE1LLGdCBIsvE5Lm4o-uEP6h-80jgBbkMyqu8ZGK1yPNEm-1mTQMbe0qanAAKQtCG-gmOpzAoN__ir3Epo6-YrTdpCOg9-mFY-0XziaQpmWkatetrKgHDUV8itUVHVu_PnXcgVlmAjLsL8FreJo-R1X1uaxUmbOhqUsQVnNcqRAO-wzxHroi-_HVdrtr7XoWuLwaeKTJztlxHkwVVPmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=VfLraD_SR7-jGMf9TcEzjifvLSRLj8siD4h4BrffQd7RcIZpx87Kj9KDmaDIXzfMiso5KViBe_mT68wWzb_4M74IhfcjRTxLKFPDS_t_9MUuohG69SPNNGgJtvkCKolCb8-3Gkpb87UI_5UYGdC1RNlpM0TVroTjwA6qar53UQSh9SpxlgdpqIbb08n6Sg5HBTRVi6G4QeuA2K8fOwYWudi9DsBbOicxkUm9hTZ2UHAs57ld-DfPPXvJnR3WrqO6l28NJgl3xBS-m4e6RovatyCCRKXmsiyqet20Dz9p0cuUN1vOlGB_wj_tAl3TNw_NNM0H0RstE2sONTGGBFhcCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=VfLraD_SR7-jGMf9TcEzjifvLSRLj8siD4h4BrffQd7RcIZpx87Kj9KDmaDIXzfMiso5KViBe_mT68wWzb_4M74IhfcjRTxLKFPDS_t_9MUuohG69SPNNGgJtvkCKolCb8-3Gkpb87UI_5UYGdC1RNlpM0TVroTjwA6qar53UQSh9SpxlgdpqIbb08n6Sg5HBTRVi6G4QeuA2K8fOwYWudi9DsBbOicxkUm9hTZ2UHAs57ld-DfPPXvJnR3WrqO6l28NJgl3xBS-m4e6RovatyCCRKXmsiyqet20Dz9p0cuUN1vOlGB_wj_tAl3TNw_NNM0H0RstE2sONTGGBFhcCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwMh1_WbgqB1gw3TU5nzMBYJ7mpqGHNDg6g7fX3RPbAj0puZPlFaDdbAsL_8yK6fHLQ56SwV4q3Wc2DhX7AP0XRWM5VONGK1QPDuQNiYMm8IVjY6gFS6vo30laMagn3r427cjd13A6x0bhPypkWK1-conzpjoMFFNs18HRwiRWQFcXiNxMClAkp0ylFOecfWIMusGICrUxWF0cWjS02myBvzOkECRKq519WZcxYAA2PkClrBKiRBQ_9gTmcZpy8Phm0-Mvb1cYYIosS0vO3Sej0O_RhNmkULf8hhBf3Y6VvAHUcnfLZB5B1HwJrp1OXKNUs5woBl8cBKgPaj4n9nBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=s5URqSvWLeb95oVFap1MkLuDhMSDNIT7jFQeXe2BSr-nn5MjVMPQXfIt3f-8fVY4p1Z6hZIgIQDN9IOPIFdpl8V-eJidA-UHuovytSoUecVnZ4avfafv02snnlNlqHWxOx4XgZCwCpAfzQJi3Lgt0k0MtckWRKMzzUPoJaNSEi1ZWYpwhT2gwQ5jGs3gME_qb3pfgoid_omXZ0R9BLVHa8eYrPBBurTIG4m0FPHGWbs2Jdf7vXBcrRYX__jls8w2Xn4RN8cX4c3K6_8VKRkrNID_QpjgGYiMwdsCrE0EukVVE76FsqscIHqveH9EW_pEmZ-43uBmjbQz39U0w9VwUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=s5URqSvWLeb95oVFap1MkLuDhMSDNIT7jFQeXe2BSr-nn5MjVMPQXfIt3f-8fVY4p1Z6hZIgIQDN9IOPIFdpl8V-eJidA-UHuovytSoUecVnZ4avfafv02snnlNlqHWxOx4XgZCwCpAfzQJi3Lgt0k0MtckWRKMzzUPoJaNSEi1ZWYpwhT2gwQ5jGs3gME_qb3pfgoid_omXZ0R9BLVHa8eYrPBBurTIG4m0FPHGWbs2Jdf7vXBcrRYX__jls8w2Xn4RN8cX4c3K6_8VKRkrNID_QpjgGYiMwdsCrE0EukVVE76FsqscIHqveH9EW_pEmZ-43uBmjbQz39U0w9VwUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jErpUSBoxAz2G0pUbYj0F8haNxiMmyxeBe_TLl0pEy-ljwMF8-a71Vz0Kk_xbOJwJvKbqkkgrtrIyT2vSfqUlxqrBF_tU628yqTlKeRp39x4eZ7fH5pXN3eAbEcwQ0klkOhRQnIHnkzK8BoM9nIyGpA02aQhi6-EDjQjCOab37gjXCnm7HtLAxvw06jolSVVaYLdgBmZvkZ8cxGtDM--Z-S0sy9T0BaH8d7WwAgyxeuFvCEsykRKHk1eyoFDxZYWw674TAhXDEXW-vSuJ7NE6apB1wcP2HnHqyytnUy042y4fiEbXP7pCQwTLUOF6qR0wIxX3fcEkETy4ADqO7z3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=MPK27DLaziAU9-I8RtwInVlFPbKkftueQrnRK4w4XRnZcvNpArTZ3542LrdYG43TbMrbdfPRQGUKKGLSNnwvfXeFFM8X7gSAuBZjsT07_2q8RVzBbFCt6ZMRNLT5pk8hkuTxJuTHQ3H68lFIJObxhX8D0xm8tCd75ip1qtCsP-rRCdooR_xyQp8rAF-QovaM0oT0RLAHQtglBdiW-L_yEPLTznqbZ2SqycnxzJSt9BXKWzCaM_DYNSMJ-Qfh4MssrvtpmK9Syb9loyXZXz5EfnFpPBH0JtPTfObfDI7z7IwuAl-l1VVCURNGcY4eNMOFrwLwYZzl72sS4AWSLFyTSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=MPK27DLaziAU9-I8RtwInVlFPbKkftueQrnRK4w4XRnZcvNpArTZ3542LrdYG43TbMrbdfPRQGUKKGLSNnwvfXeFFM8X7gSAuBZjsT07_2q8RVzBbFCt6ZMRNLT5pk8hkuTxJuTHQ3H68lFIJObxhX8D0xm8tCd75ip1qtCsP-rRCdooR_xyQp8rAF-QovaM0oT0RLAHQtglBdiW-L_yEPLTznqbZ2SqycnxzJSt9BXKWzCaM_DYNSMJ-Qfh4MssrvtpmK9Syb9loyXZXz5EfnFpPBH0JtPTfObfDI7z7IwuAl-l1VVCURNGcY4eNMOFrwLwYZzl72sS4AWSLFyTSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4KArCFXt_cqM8LDsLSrsv7vTlAB9rG5opKgpT_yuYNHSdNxXiEXSD59NcbJa_chBujijvUV1s2uVTpcOeJEwO0QRwBZqWvnUnapGM8RqL-rYn-NdE3MjcMdLDLgcLwcK7A3zuP60CDMXDMfo5xcPxBNmMh4raIqztruR2INA08S2os1l5qyc7N5U6k0J4JeQEvF4eWHz-H6oCAhfCHKYJAWXM1WDFqlbpZXPLTa7XgTFhQfhDBI62LA0c_1MRdgs4zas79Vkl9LJDcbGiz9tZ0jz96O-GVAEEfgsIitDrHws9NI6-HSBIbOtSpy6V8JEYh9pFnlSgyehgd2gC3PAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqmu-L5pCeH_xMb4CoXVQ2ZOyFkdkNLvy3UeF5oPxbG5-Yfork_8fBHidjzeRxefFs2YBMUTHVJI68BEZKjbeMJ4dikHs6W2kGh9gK07HrxOY6ZMztNPXmBipHEjIUimta2ieWqLRXNgOMZenQ0iimDhI4prZloVNfhPfyoqWMq88Sl_hGaoAqVLJVREqedA4jJ03H9XNWyvmRrQ0hqwJdZBFQicdtV7vOp8ISHfVKikzwwuVyQmUrjG9WIejcfPkc-DLanncc2w8KCXRhwa6cuIkSkMcX0cGLzSWdjvaqHG74JoP_4i8bUqoCv23YuRshcPpsK1pko5EhfhxV-iPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYnA7Cwec9T-5vIXYdsSoQZqL842iMstHEV40M8hieObCNn2DJLK_eYkYpzfTYh7NPc0InN3TIFT7nlVCSN_f4yGxmQ6-MMIRuy-skDcWNbiV1P2rmguF6UUqTC__ui9npWQ8YZCFLrudrR6BXNdfUWJCFnOKAXyXRNg-3ZdnF4XqxiY8-1SwjUSbEi1NQy-9Q-wVIRXP2K6qUIjl3mmTgxSLZD8KYZRe85NKJokcqOnc9WvSJyw6nRTTb551Hj6y8D7StEq3orDh6Qltz_Ar0LvCWJH_9OqdfoeVPfakZlqKkt7oiXhRaX1NvzjYNEzYlvAHr7k9GBZ6I3_Xvt6wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHzeVX4cjxCCmcDXRh77cwL4MgDpEchMqSCmzKVeTs9-WitEx4Dgj4MgBw60-B8t2B8AaBrx8cr1mIRYjJT7-uXbcJXOSSb7UedMEwKe7c13Xi8KXnSYNC3VkX35l39R9hY2sw1QAPK6ltZrIX3kqItCcY-R83rhvnsmUQ0FYi18dxUWJvKbqQ2vDCMpIPk_56HnQbmZkTFkyM_Ai3bltC83I6X83TDBk4WlGXwY654FxHhUaUAK1ask28NL_TiNN9XdJQl-FcFxu2n0KF4_npK5nB2g_-B6lNspzgXV50gFJshyDymKji-xOjyvMUrWYsuQ4q_P51MQf2PrP5-KNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=K0vlLPm-XlNXyMSpYUfw4_IV5qhu-9n0KosWWzKPvJ8rrNEOzBM2D6XpRaJ4n76bTTaH25BNuI527JBGL9ojV1YjjlHSP025wSPyndVVSu15gOB3yuhyoOrtgflWO-39y8_IMqHw-KDyvGm0HtdBJ_lavS10-Rjc7zSkejRRx8epXGGlgcdBia8Q97IvocGEu_3KRHAg_GHPt5oVuewPCMhoMwjlLQYB_7P_LeD00kx5j9yLdQgUzb54jshNRJsR-58tdsFGLYzG-KnGl9zrIpx0Km2JjGPQRZGUDyIFVHXbXRf_2tUBwMl_CU5gk3v9j3BP7jxxB7htdsfpwxgPCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=K0vlLPm-XlNXyMSpYUfw4_IV5qhu-9n0KosWWzKPvJ8rrNEOzBM2D6XpRaJ4n76bTTaH25BNuI527JBGL9ojV1YjjlHSP025wSPyndVVSu15gOB3yuhyoOrtgflWO-39y8_IMqHw-KDyvGm0HtdBJ_lavS10-Rjc7zSkejRRx8epXGGlgcdBia8Q97IvocGEu_3KRHAg_GHPt5oVuewPCMhoMwjlLQYB_7P_LeD00kx5j9yLdQgUzb54jshNRJsR-58tdsFGLYzG-KnGl9zrIpx0Km2JjGPQRZGUDyIFVHXbXRf_2tUBwMl_CU5gk3v9j3BP7jxxB7htdsfpwxgPCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=ID329Eqz_lVzCu4ccklGiPSKq99r1t1zhzKyDpZsxXIWxtgxgDZyt_ML4adXtbroUXPUVql9FGqzq9qdscc4gCHzvyGa11lMcjK13rsHSrbG2tLK2ZcaqVNqSZ4hq7U5UTJSUnB7hPvTtoAcFmTZBNYlsJTf-2pMK2E1OSFrVaw4fGgrh4wWSX5ckEXPZyuhmPdbF01SCXxFCUMWRdCovIGObrQoFoKwtUn1LQZMMCtg9y-kuuxDagSliSJSedipGWK-Zl9l7GGk6mlDqJQkvvcKUUTAkjALHgwmxC8MjnaSN28br0mZWjFi9-xEdmYhm_g94YLS7-Mff5wKxj9vTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=ID329Eqz_lVzCu4ccklGiPSKq99r1t1zhzKyDpZsxXIWxtgxgDZyt_ML4adXtbroUXPUVql9FGqzq9qdscc4gCHzvyGa11lMcjK13rsHSrbG2tLK2ZcaqVNqSZ4hq7U5UTJSUnB7hPvTtoAcFmTZBNYlsJTf-2pMK2E1OSFrVaw4fGgrh4wWSX5ckEXPZyuhmPdbF01SCXxFCUMWRdCovIGObrQoFoKwtUn1LQZMMCtg9y-kuuxDagSliSJSedipGWK-Zl9l7GGk6mlDqJQkvvcKUUTAkjALHgwmxC8MjnaSN28br0mZWjFi9-xEdmYhm_g94YLS7-Mff5wKxj9vTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTbfyxsXt8tQKG_DLSCyryt1OIiLfuukPF8wN_YVL6X8TimMR9sPBZiR9nBCEdftAyduwJBhWFuW6H_c-JEytaSsuzDA7frnq6hU6GGzq4bgzQTuf_biJ9-8ordvzDGkX6oWLCTXuuz5yYdH8St_Pyx0xufJvwz_dRIRs0fY15ZEznk0yt7Ou8K8AWonXU-PJyVLa4GK3gF6jLDAwDcAqQ22HBfE3BYmHh05VeXZy0LKE5uWEfiFhGVKCl_J7JLcdknXOBU13cocgXBh-ZJ77cFT7Rz3F7O_mxAU_P014BkjKonmMsz8Q53XNVkIvEM8vY6jsqbJJ9kB-J25gLb-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktmpg22PGCxBkqq5-g73MJjp-rIG96BvMUMql5kjOVJK8ToZBTZH9F_mVtBrZMCpq3FRC5ScJxb03j_IE3dMXaEGtGtnUBXECXEZ-UvlET41xUP2PAAKFdglPebsaTopLLFyhpwDrdAUY82Ks1m3zHnJYIiGQvAS7-eMPmgxiwFYqzAZTMeUkc1f8HHU6RxPws2MYXFPFhEWSMeN7zkgSOUpQsbaT016hcmO3apucXUqK-J1FoMzo4YOvIXa_5fmqX8VSeLD9nwPaCSgBE8BPEZnxkhXMyz25B8NviQ_cyATGSb4MHJeQFPukr705z90jPDQ-yM-xQQhs9o6mt_zVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=Y2X_WaxT3y2MtYjV5YH0ueIncT8KXNXkKIdLhwtzWxceXvf10mz4XbPh-CghyzxeERbyMxKCkSRaLBZzx2w2m7vQz_X3q9JpMiG4bjF54U-VYbOUTwZ__SfKft77JssFilk2d6_Mbah-YMHqglwwADmb6SmpjYj2Eeb5QPcEFUAdJlYbbB0wgvhxeddYjqGcHi56uYzHYNdTp_EGIH30QgTQu_RNUymFfymhMDMXCiHBMhbLo3MoySA57Xw6cr8Bm8ORQgULmL33QWVReqHbLRSSBW9cp1YOTyK32cEQ_V562S8GdKnkxMM8l4qwjOZpYM6T72zzCj3kBycEH5Fdkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=Y2X_WaxT3y2MtYjV5YH0ueIncT8KXNXkKIdLhwtzWxceXvf10mz4XbPh-CghyzxeERbyMxKCkSRaLBZzx2w2m7vQz_X3q9JpMiG4bjF54U-VYbOUTwZ__SfKft77JssFilk2d6_Mbah-YMHqglwwADmb6SmpjYj2Eeb5QPcEFUAdJlYbbB0wgvhxeddYjqGcHi56uYzHYNdTp_EGIH30QgTQu_RNUymFfymhMDMXCiHBMhbLo3MoySA57Xw6cr8Bm8ORQgULmL33QWVReqHbLRSSBW9cp1YOTyK32cEQ_V562S8GdKnkxMM8l4qwjOZpYM6T72zzCj3kBycEH5Fdkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=PEdpRcnnZqGABLNgYgZUS1UL4L1j7Uv7afZLmSI0QEzqJDaO831h_cY3qbY2eIaNuY90Kb2quHBEPArFqWlSGKLb7g2ashtQR7SWKu9kOjJF36XgpmWZ6BEMiGOC6uCzf0NQM4b13TuzFnebLdBfWKxXm8p5tBSB65ilchm4TOtgggvgsIMH98QHunTdKyASrOyEK2hxQumYoe8XEhkbdr4eziAC_SH2ixtdx4PskbT7MCKNBSa00yZRRcfRrs2BKz0vOoG7BYq7sSWer4nQCX1NUjYsnD4eTdQqWio_7ht31DlpIUXOiKI4XC6HPAMqRJqnpN4jcpzSVMNSIU7weA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=PEdpRcnnZqGABLNgYgZUS1UL4L1j7Uv7afZLmSI0QEzqJDaO831h_cY3qbY2eIaNuY90Kb2quHBEPArFqWlSGKLb7g2ashtQR7SWKu9kOjJF36XgpmWZ6BEMiGOC6uCzf0NQM4b13TuzFnebLdBfWKxXm8p5tBSB65ilchm4TOtgggvgsIMH98QHunTdKyASrOyEK2hxQumYoe8XEhkbdr4eziAC_SH2ixtdx4PskbT7MCKNBSa00yZRRcfRrs2BKz0vOoG7BYq7sSWer4nQCX1NUjYsnD4eTdQqWio_7ht31DlpIUXOiKI4XC6HPAMqRJqnpN4jcpzSVMNSIU7weA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=cWjUderzvAm9CB-apKGgmSP4JvTESQ4Ej-cgQpdO1-v4KyZi85UBmTRlQmEhArE64AeLg1ILqWkqPRrlolt95AYtOKdeOt4ApIkiWENhW-VxwVCwKfgpdcT3gKgeR_iJuhSdZmHETmOh0-7XdP1NsLPYY2M3bOzQgtDktOuwsZsKLL5ovxqsrqqM5t5OkemhoU-VUq--zlo76KBWzJ-LrhWMJxkf6MBMM-hBM_tjwkSeL0cCZokUBERcRIy8wU4k-a0fykmZjrrl6CwQOXnD7pmFCDVsg83xg2sSsVDuRI1NBASXTZeyLRd6xJmwWpL3p6V6DuZjjyrkU4_xnGDqxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=cWjUderzvAm9CB-apKGgmSP4JvTESQ4Ej-cgQpdO1-v4KyZi85UBmTRlQmEhArE64AeLg1ILqWkqPRrlolt95AYtOKdeOt4ApIkiWENhW-VxwVCwKfgpdcT3gKgeR_iJuhSdZmHETmOh0-7XdP1NsLPYY2M3bOzQgtDktOuwsZsKLL5ovxqsrqqM5t5OkemhoU-VUq--zlo76KBWzJ-LrhWMJxkf6MBMM-hBM_tjwkSeL0cCZokUBERcRIy8wU4k-a0fykmZjrrl6CwQOXnD7pmFCDVsg83xg2sSsVDuRI1NBASXTZeyLRd6xJmwWpL3p6V6DuZjjyrkU4_xnGDqxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=PVtf_Uc-hW0sAJTPETGDzPo3M1Ds363C234MgxZwKDyWcU6TtfRQEud_A0eEyNc5Z8enK_iIMwU32N-JwL4Ig9uI1e7oQtrOToqekaxbbOkXGkHTqGH79OCSwSSlogkQX-HUNQAG2mPwwOx3SlTEhcmk-503Yr1_-RIdhrEZNIaCMy6HnhbLiRLQOE13Zvz_Jnyarwih3ry2KdvFn3JYLGUmWqv6IxMf5-LcGxrY7HR0HAl1ldrdzk8RonjmSLVJdi9mUtaMaLfcCxK90F0EYiun0BqZU-VV5IEE1306A5iLrtRB9C-gxCb8Y1jTu6Sd8GWgjD-wxdxoKwSLBYbPhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=PVtf_Uc-hW0sAJTPETGDzPo3M1Ds363C234MgxZwKDyWcU6TtfRQEud_A0eEyNc5Z8enK_iIMwU32N-JwL4Ig9uI1e7oQtrOToqekaxbbOkXGkHTqGH79OCSwSSlogkQX-HUNQAG2mPwwOx3SlTEhcmk-503Yr1_-RIdhrEZNIaCMy6HnhbLiRLQOE13Zvz_Jnyarwih3ry2KdvFn3JYLGUmWqv6IxMf5-LcGxrY7HR0HAl1ldrdzk8RonjmSLVJdi9mUtaMaLfcCxK90F0EYiun0BqZU-VV5IEE1306A5iLrtRB9C-gxCb8Y1jTu6Sd8GWgjD-wxdxoKwSLBYbPhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=f0bKvfCjDJuwSYHKpP_tL2ZdbjjGCDPizSRcgOKUGU0YBBTGqrCYt_nHN4o51Y5WOcP8tBv9mNN2Th6Hb3GERBarNZ44NSUuMPlw0EUyPzYOd_aR1P8RHmHljF4JwCs_j5DJxrLRkJjH7icog-Ydjd64YI6IJ0ZjcPI44PQpahaa4PdeYjHOGcpN8eFcI7E7zi3Pc_ZDFZttBGziixR552o5fJUMZsnE0biouAXJ-WrG1RUH9EnAyRWBN5ZA8_o9KqVDjAuCzyOo6pS8WIpyEt7ZHCmNiTE5MHKd2kR_whUIkuTyGNh2k29TUSioAfBFdW0MlRIN6CixhY0IA3Awug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=f0bKvfCjDJuwSYHKpP_tL2ZdbjjGCDPizSRcgOKUGU0YBBTGqrCYt_nHN4o51Y5WOcP8tBv9mNN2Th6Hb3GERBarNZ44NSUuMPlw0EUyPzYOd_aR1P8RHmHljF4JwCs_j5DJxrLRkJjH7icog-Ydjd64YI6IJ0ZjcPI44PQpahaa4PdeYjHOGcpN8eFcI7E7zi3Pc_ZDFZttBGziixR552o5fJUMZsnE0biouAXJ-WrG1RUH9EnAyRWBN5ZA8_o9KqVDjAuCzyOo6pS8WIpyEt7ZHCmNiTE5MHKd2kR_whUIkuTyGNh2k29TUSioAfBFdW0MlRIN6CixhY0IA3Awug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=FJyhtythMgyLwDxF3htqtUHW4pSJ6MSB1wsVJis89mXkOcJAhLfbrP-mt_34vZOTJyfrMHXuN4Ti_htAMVCbIbA_KuIYt9i2WdVpbGzX6W226E0unXcBcYrBBSdft5SgoS4L5SqsXP-h33_y3bLDWBqDbuGd2RW6v-tMuFTpyFlNEWHVbyPaVXT6Wl1sNNG3wmjIacFyC1tSyyTropR7ZGFSqRxE923GffjK_hTmjRqxIbmYD5F6dYFP00Up2nHVHqd0NFvmyZNKmix4QV-_KdljGLuNwKKLRJ39iU38WljRzI6lygfNGIn5qb1vA04by9TpMtymGhspjTbsderc6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=FJyhtythMgyLwDxF3htqtUHW4pSJ6MSB1wsVJis89mXkOcJAhLfbrP-mt_34vZOTJyfrMHXuN4Ti_htAMVCbIbA_KuIYt9i2WdVpbGzX6W226E0unXcBcYrBBSdft5SgoS4L5SqsXP-h33_y3bLDWBqDbuGd2RW6v-tMuFTpyFlNEWHVbyPaVXT6Wl1sNNG3wmjIacFyC1tSyyTropR7ZGFSqRxE923GffjK_hTmjRqxIbmYD5F6dYFP00Up2nHVHqd0NFvmyZNKmix4QV-_KdljGLuNwKKLRJ39iU38WljRzI6lygfNGIn5qb1vA04by9TpMtymGhspjTbsderc6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkqekH6ofrqlgnYHiQ4rlyYCusmVVsb9PnyLMAoLySz5ceh7Vu19YC3wDw5CL_yjRoNMCd7DFb0Y_pIshX0_QiaLzG3LZAUA23fbApROyhWT2fyz2vonvpTpAARxNVgk700XrPFBkudFfGkbxZyJm8Mntod6dbVL5NKotof6ElSNpHSSmVmh-DhORgqlJDyUz8ReNLfOlxzWTK4rC3X26HP7Xdsets9MxbllCkzsdtzxIovxRVAns2vwEvEgY8TJ7LZW7saxC31-IR53EnjTLiX5LuFMENsIQDwgy6vYIkXygjrZB6EXHlF1mNn2Xmi0V_eUUJqOrr9ysxBZMESFiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aUnRV_dJvXAe6n72SK0qEw3E0LpHtrVgtNQWuB2hqOPsACXk6IFIgccrXY1u72djSSjUIN_tr4QgIh3UbU-eaW68MJRsm_0ut-BwfciIZb4G7kHovkkRN1QwafxKt6eP7EERZlKmR5knV68gMVk-oT3E4FL-BmciKVkPku6JF3sZm8wDZBlaDGSWZgUJ2vGk0oD6zChLCQEuexZi-uGYU1ZjZzQOeUPsOTtP_K41_dKU7teUJPqB4kgYYVkj2kVfJmc9MRFHFwx6BfKb3O086qgIUFBxbUcAsq2MIrArYN8n5VA343YFMiUmvtED7QFgkkHVhIp0RMve9f5X9_FfqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXpiq51CujyXjUyBHg09k9n3ztwogszGf-Oim_fxD0yFHvnqSa3_jM-F_AyWgxE6lQ3XaktU-B_zByL0n2hN5AeK0nD9OLIlVrdhQfXx8xQAqFPOpRSJakv2homFYCU1X7PXB_LqKxKZ9_AgiQLsgOrq9p1HaW3aYsi6kV8EBGQH1QevrmX5hudWTAikz30wvsF8Rgaqhj0GND4GzQKAa-71baZO7VDQt34avPeIKCeSjHst8gU0CWZ_DLb4iQ2Yx0hkcX1x-ef9drrbc12aVOexawIj8n9A1hhjD6LtMrao1cA3RHSsyXG4uY0Jz65PkCWPxKd5FLLuLEcjOKDrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=IGGP8e7X6IKqKkul99PMCLhavf-tMTxV1eEV3N2IjtSmTyTCcb2Y37vnXQPDZZvPEumZbTe6YGPYv-vEv7Tafj51w85ivbW37iOcZIew8mTTJheEc0fcQyry46yo7Oe0xkhm9Bae1lwWkYsIKUqBFcmotD6ZZZ9PcF-IBVU8szMhmRZ5RazRZmmP3dMAOWyYbo5f_hxiQ7-UPDhSc9U_jfUn1I8H65phGECueakSuIef-dtLH8kGqLb5sA1qIPo3cZAvfQacLVjWVxQMELefURyEkHLEaYtdmqggLoxX0Quoh-UdyOxBs3gYMxiVHstZD1qjr0QjV9G9q_mZHJjrGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=IGGP8e7X6IKqKkul99PMCLhavf-tMTxV1eEV3N2IjtSmTyTCcb2Y37vnXQPDZZvPEumZbTe6YGPYv-vEv7Tafj51w85ivbW37iOcZIew8mTTJheEc0fcQyry46yo7Oe0xkhm9Bae1lwWkYsIKUqBFcmotD6ZZZ9PcF-IBVU8szMhmRZ5RazRZmmP3dMAOWyYbo5f_hxiQ7-UPDhSc9U_jfUn1I8H65phGECueakSuIef-dtLH8kGqLb5sA1qIPo3cZAvfQacLVjWVxQMELefURyEkHLEaYtdmqggLoxX0Quoh-UdyOxBs3gYMxiVHstZD1qjr0QjV9G9q_mZHJjrGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Poax5aigbDPvUeRIH70VkOVkif80waxnv9jAdYwMke7A0ndEEF1SXSYuUmFwRfXr6Q32XwZX5GbpKQT32QTInw37k470h6AI_g_lUrgj7dWnzOo1AdPHfaYHIiH6nI_IsQO6CL19I8ffm3b3dKg6oKPXhawvrMrVNlcAwVXwHg6crydkbQ8LWWs1rvjZkHNKgRCpAwF3ic-sE28lbn8is9fsWU-_JmeStypfOP_cvTa7Pr1PCdmg2ekxjt2w73ijN1LXo2LdxrsJGu6PMUH1B1H5kKMHXU7HT43d_X5MeZ2Kz6xr5XV_FcilI59Sr4GnyIlCnfnDJDmGR6OBhbRWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=ZTWGy2p_RYop9I1eZUv7GRWWfc-iqgrE4g-kj-g3Ew5PSgXFDeX-qWP0zLhVcfBq9B9kLDh3TJMFlfcXOWV6Lf6x3AOSqXUG85wqegCc1UbLeDACwBJeKcJrWuPY5ztLXyy1REwPoYGyIFFxi-FxSJ_QrxrAn8iCHWFy-Lqrsvxmph0-H8PktDh5kwmeChPUSyVKM1rknABSjIR6JVt6yQA1er-WwD450k1d5-EQacu9Pfy3HLBVkda_4oxfcVrqoacTNcA-_-5EvDGqArnibEHxJmhxM78s2XZ2MI477AWY_3HeNQtQJj8JyCb2gEOnVSjdQrTRVGZNqdfxkA7vjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=ZTWGy2p_RYop9I1eZUv7GRWWfc-iqgrE4g-kj-g3Ew5PSgXFDeX-qWP0zLhVcfBq9B9kLDh3TJMFlfcXOWV6Lf6x3AOSqXUG85wqegCc1UbLeDACwBJeKcJrWuPY5ztLXyy1REwPoYGyIFFxi-FxSJ_QrxrAn8iCHWFy-Lqrsvxmph0-H8PktDh5kwmeChPUSyVKM1rknABSjIR6JVt6yQA1er-WwD450k1d5-EQacu9Pfy3HLBVkda_4oxfcVrqoacTNcA-_-5EvDGqArnibEHxJmhxM78s2XZ2MI477AWY_3HeNQtQJj8JyCb2gEOnVSjdQrTRVGZNqdfxkA7vjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CcvbSuSVyuafmtW14ZYGjVjosZ5q01HQrDzqStnnnVXDv2MFrh7WxttUu7KqMxntLIo-FW7Fe5y4Wr7fFpI9bKTFfLU2FTREGyYsRciyAFvg0NPrpO93QsneE4ljU5aLZYvInR3i_07i_UBsuuYi94D13sbwNk2mCdPC2uODado32AvKM-lCC3Qsr65uS866ats0LteylsudDUXawsBri5dCs4yxMnq9io0yyykrGjP2nxvGh2ONez5wHSYmVVvRWfRw8yflnWPFMnyNHzqu4f_XOhQYuubWEJn9iSOdKTQvy87xbLkorYdOf4UhfLSDXQtAjANuXpt-L7pEgjhcFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
