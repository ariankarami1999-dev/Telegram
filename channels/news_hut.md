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
<img src="https://cdn4.telesco.pe/file/PH5jacSICzZKzBiPDv2r0mlDQ_Y_904WdWPvpCREQnv073_t-ocS4bMwqbqjvecaYtxToqbU5usJHXP3Le0nythdvwkQUwdFrH5k2UvsRq-mqaDWiDL-CdOq3CWVkJ2kSdqBrJe9NGc_wsky-GA_B3yq-RiSpjYcrOkxZM-AMzg5ZVVgi-ulG_MKjD1RP7veQen3JNrPN-0PN_piGvxa8TzXwA8_ZcbSAr8ZJa0ryjr_P6Jjtt7aXXN76_z5jEwysvnRF4cb56DHh0Dno61WrA4c79PzW21OaYu5vJLFsXCyKg1aPw_G01hpgVV5hzo2ZwmWz6uHaNrpBKNP9hyAxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 17:07:57</div>
<hr>

<div class="tg-post" id="msg-71095">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=HoY2VmkIu7bG-56WzyeG92oSLVvbPgvoKiw6eziJT6tub2ly-QPG9k7mHrho3DyznwPS7zLfEQSZnoolaM5arn9LGNih7vzD_d49jFc3QHM8Rb8mgrOEbOiLmyMcyaUt0P-8zznu09h4MwCt-wtDoSNA0N21LQH5S6yOq5BrxVhNqelx0d1kmgFq1raE_hwt3BtKKoLqC2Cj0zCxLdaV8qfSQB2aeLJMfa0k6psXzSYG5c9coi1Ah8CaWxmId1Rt76lJkSkKCjpS3lefW4QlbNL3kJlclKP5iSv7XDUQZiGcISGB-jZwPu6BxnIT3SBRkxXrhO0-AZEHvViWJnN7ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=HoY2VmkIu7bG-56WzyeG92oSLVvbPgvoKiw6eziJT6tub2ly-QPG9k7mHrho3DyznwPS7zLfEQSZnoolaM5arn9LGNih7vzD_d49jFc3QHM8Rb8mgrOEbOiLmyMcyaUt0P-8zznu09h4MwCt-wtDoSNA0N21LQH5S6yOq5BrxVhNqelx0d1kmgFq1raE_hwt3BtKKoLqC2Cj0zCxLdaV8qfSQB2aeLJMfa0k6psXzSYG5c9coi1Ah8CaWxmId1Rt76lJkSkKCjpS3lefW4QlbNL3kJlclKP5iSv7XDUQZiGcISGB-jZwPu6BxnIT3SBRkxXrhO0-AZEHvViWJnN7ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ببینید از خانمی که داره از تجربیات رفتن خودش به تور کویر میگه...
@News_Hut</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/news_hut/71095" target="_blank">📅 17:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71094">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=ZljWjFMjZJgEB1fKBQqhh7qJjfScYvg1j0WJYWj9pDimo2XaWRoH5Hk0rgm9RFX6z7u_cDWGxuPUJYihTIfIC5gU_rmNpQQJUyA6yhAIYy9PxJSeQYrKv_zwl8l6q0bs2pmgHniqp6goDy9zSPb5YB2Mu447wMuCWsETuI1ngC1dzW90KtHryLnJITtG3M-EKRwRx9f-XAQ3DQsjZLXA3uMUEHsUOe80ZRq9TbRwpOuy6c5h0YBA0FT5xzukZr52SD7syV0ItzgLGEkX0ZPabhDsuXI6Us1X0lgXV4zRDFJIuz7jk14LSRkWh0hyJfRSrrrDLBVEAbwu_uJXQUpmVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=ZljWjFMjZJgEB1fKBQqhh7qJjfScYvg1j0WJYWj9pDimo2XaWRoH5Hk0rgm9RFX6z7u_cDWGxuPUJYihTIfIC5gU_rmNpQQJUyA6yhAIYy9PxJSeQYrKv_zwl8l6q0bs2pmgHniqp6goDy9zSPb5YB2Mu447wMuCWsETuI1ngC1dzW90KtHryLnJITtG3M-EKRwRx9f-XAQ3DQsjZLXA3uMUEHsUOe80ZRq9TbRwpOuy6c5h0YBA0FT5xzukZr52SD7syV0ItzgLGEkX0ZPabhDsuXI6Us1X0lgXV4zRDFJIuz7jk14LSRkWh0hyJfRSrrrDLBVEAbwu_uJXQUpmVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سامسونگ A17 که یکی از ضعیف‌ترین و تخمی‌ترین‌ گوشی‌های بازار به حساب میاد، قیمتش به 100 میلیون تومن رسیده.
البته این قیمت واسه دیروزه و امروز احتمالا گرونتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/news_hut/71094" target="_blank">📅 16:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71093">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=m3JaoJQg5pj53Jl9vuL-S9_ZuZgnDO6i09BqBP6K5aaOYej5ejNDl3fHhbOkLv2TkEpR--1W4o7F0yEbu1qkGiG1sqYXUZZaOFZQI1VfZFRDQX0rykG1A7ls4UKsABppU7N0R2lU46lYOahtzwo3VxV4ASut-p0yG4_MTKtCtBi8iyHNX4owoa8eVd4q2TMspD5QGlvaAg1odwrbKVRNIpGGZSirovD-UnE6gz4MBE09Y6FVKTrTTwvvapVsPGd2fboHd3C56yeV60BrLMr8z0jXUjEUznbqEuB3AreRn2DQPe8yd2esP7f6bDCtspNuH289s3EmQn4RzN628kgSCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=m3JaoJQg5pj53Jl9vuL-S9_ZuZgnDO6i09BqBP6K5aaOYej5ejNDl3fHhbOkLv2TkEpR--1W4o7F0yEbu1qkGiG1sqYXUZZaOFZQI1VfZFRDQX0rykG1A7ls4UKsABppU7N0R2lU46lYOahtzwo3VxV4ASut-p0yG4_MTKtCtBi8iyHNX4owoa8eVd4q2TMspD5QGlvaAg1odwrbKVRNIpGGZSirovD-UnE6gz4MBE09Y6FVKTrTTwvvapVsPGd2fboHd3C56yeV60BrLMr8z0jXUjEUznbqEuB3AreRn2DQPe8yd2esP7f6bDCtspNuH289s3EmQn4RzN628kgSCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک راننده کامیون:
الان کنار مرز پاکستان هستیم میخوایم رد بشیم اجازه نمیدن.
رفتیم پیش رئیس گمرک میگه طرف پاکستانی اجازه ورود نمیده.
پاکستان گفته به ازای هر ماشین باید دو میلیارد تعرفه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/71093" target="_blank">📅 16:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71092">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=Zto5xFimVJtZRFIH3Jo07xOAktW3e839kBIz_TrKSvYv9uIWC4rTObIEPSiYznpqR8OaIpcLGmO3am3smgmq1gZntfLpPT-RS0VeWeg4O6H4vVaO-ek-MF-VFAK4tlYsZiBgoi2puLC68AHXvfeuWpZ8Oa-lfKKhmiFZraFn1zAaX78rMtRvWwyNjQLC7f4ndTBxgbdwizDNsvMFUCcVKC5VrpgwEZ5qItJHjJI3WdgApVl1cPSmvrzqb61qkv2KktyS3RwBgJh1DxL8rl4qBtmXBpX5iobqOSvhBpMRpU66fPqUAsaLfzIxYl83-IfzTbPKleoey8ayvcq5o9GOsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=Zto5xFimVJtZRFIH3Jo07xOAktW3e839kBIz_TrKSvYv9uIWC4rTObIEPSiYznpqR8OaIpcLGmO3am3smgmq1gZntfLpPT-RS0VeWeg4O6H4vVaO-ek-MF-VFAK4tlYsZiBgoi2puLC68AHXvfeuWpZ8Oa-lfKKhmiFZraFn1zAaX78rMtRvWwyNjQLC7f4ndTBxgbdwizDNsvMFUCcVKC5VrpgwEZ5qItJHjJI3WdgApVl1cPSmvrzqb61qkv2KktyS3RwBgJh1DxL8rl4qBtmXBpX5iobqOSvhBpMRpU66fPqUAsaLfzIxYl83-IfzTbPKleoey8ayvcq5o9GOsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
فک کردین اومدم از قیمت دلار آه و ناله کنم؟ نه اومدم پاره‌اش کنم!
رزق و روزی دست خداست نه آمریکا، دلار قیمتش عوض شده، خدای ما که عوض نشده.
قیمت دلار هر چقدرم بشه، باز روزی مارو خدا می‌رسونه، منم اعتراض دارم ولی ناامیدی تزریق نمی کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/news_hut/71092" target="_blank">📅 15:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71091">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=Mcqm1BY8A87LAm3G3VfkJJxUu7rhFnHYZlLcOJDxtQYbMfLTxuS7FAtbBAmcNhZX-Xo8Nec0kTAkNwPaD2RgTB-riL5Y0KG_MDak9pBwLWmL7Hg4TceB9ofJHGWd0Uq4nYIF4xqOv7fx-_w0ijbcM3iti7b-obUZxHcPRlC8hVK1TjxgBBa0-ZkKx3bCmvIjCNSRIpR0JuVl8M166zk96PDGarjpmlc6JcEu4goRDimeVvVvsMBNtp_JvYg4GEeIxrcoYNaV5d69QMIqf5BhwtNH2YS5j9GAL9Ikg7T2ZColY7Megp37lvW9nzTT2N-lge-i23jzNQb9BOGSG6ep8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=Mcqm1BY8A87LAm3G3VfkJJxUu7rhFnHYZlLcOJDxtQYbMfLTxuS7FAtbBAmcNhZX-Xo8Nec0kTAkNwPaD2RgTB-riL5Y0KG_MDak9pBwLWmL7Hg4TceB9ofJHGWd0Uq4nYIF4xqOv7fx-_w0ijbcM3iti7b-obUZxHcPRlC8hVK1TjxgBBa0-ZkKx3bCmvIjCNSRIpR0JuVl8M166zk96PDGarjpmlc6JcEu4goRDimeVvVvsMBNtp_JvYg4GEeIxrcoYNaV5d69QMIqf5BhwtNH2YS5j9GAL9Ikg7T2ZColY7Megp37lvW9nzTT2N-lge-i23jzNQb9BOGSG6ep8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
🇰🇼
روز گذشته، یک پهپاد انتحاری که توسط ارتش جمهوری اسلامی پرتاب شده بود، یکی از واحدهای برج مسکونی الدیره در شهر کویت را هدف قرار داد. این اصابت باعث آتش‌ سوزی و تخریب کامل آن واحد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/71091" target="_blank">📅 14:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71090">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=aSr_drfDtyuX4YbN1fewDea1kIx1Nko6BD_rT4GCN6Fw5B_FviBkvWHCR7kcWg9HkCuxp-DlYEdUWWNFZTUuerIAycrmD_2Z0k5l_mBTyxEyPZUXgUPOLTBGbQGxOhkszlPrh7c6xEXVK9UcE32SNXjKJF5buZcjMfuy3a3nT2uigQb-BU7akKqbaA7H4c-K3BNKrjqYCxsMCX2qIb-hJe0kIZMn8aklDFckJWKVYu2u_xeOOiXdtsK1ni6T46c_VhRNWekyEZlThqyqi53c3T2dtSLJRXAkMlRzK3pw6q_1QLQEt4vhUxExxgfd5nmyAGHCw4R_eltR0moAVX10Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=aSr_drfDtyuX4YbN1fewDea1kIx1Nko6BD_rT4GCN6Fw5B_FviBkvWHCR7kcWg9HkCuxp-DlYEdUWWNFZTUuerIAycrmD_2Z0k5l_mBTyxEyPZUXgUPOLTBGbQGxOhkszlPrh7c6xEXVK9UcE32SNXjKJF5buZcjMfuy3a3nT2uigQb-BU7akKqbaA7H4c-K3BNKrjqYCxsMCX2qIb-hJe0kIZMn8aklDFckJWKVYu2u_xeOOiXdtsK1ni6T46c_VhRNWekyEZlThqyqi53c3T2dtSLJRXAkMlRzK3pw6q_1QLQEt4vhUxExxgfd5nmyAGHCw4R_eltR0moAVX10Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
🇦🇪
با افزایش تحریم‌های آمریکا تجار و بازرگانان می‌گویند امارات از بارگیری لنج‌های ایرانی خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/71090" target="_blank">📅 14:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71089">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=b0x04bmp4m8Z1eqhqZYkbUaNml6Mxl55jzZrCyRt1RP_pjgnPSUxZ9bNM4w9MDzC8AfSHyb4TniEjAxJbmTMxRrKRI7xFaGLhNHdTcfrl3WSGUYA-yM7y47Bx4jPxg77gazXhMJxpft1fzV0ihH8eV_V54tG3xpt1vghQnnorvv9qOJW6n3u806fofjt1ROfqSxLx1xy1Xhuzwmde8Sdl0sUQ-GmRBvwoGceiod6i02jHAxeHvRTGpV0cPqaxo5qOPy7DJU7ew2vfva8qiAA2IT3r1cMrglc1nBraQ7ehdnu52N98WguVDA5kXv9Hr_-Bpe1WNDwy_6qxGILHIX1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=b0x04bmp4m8Z1eqhqZYkbUaNml6Mxl55jzZrCyRt1RP_pjgnPSUxZ9bNM4w9MDzC8AfSHyb4TniEjAxJbmTMxRrKRI7xFaGLhNHdTcfrl3WSGUYA-yM7y47Bx4jPxg77gazXhMJxpft1fzV0ihH8eV_V54tG3xpt1vghQnnorvv9qOJW6n3u806fofjt1ROfqSxLx1xy1Xhuzwmde8Sdl0sUQ-GmRBvwoGceiod6i02jHAxeHvRTGpV0cPqaxo5qOPy7DJU7ew2vfva8qiAA2IT3r1cMrglc1nBraQ7ehdnu52N98WguVDA5kXv9Hr_-Bpe1WNDwy_6qxGILHIX1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
🚂
برخورد قطار با یک کامیون در گذرگاه راه‌آهن در گدانسک لهستان.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/71089" target="_blank">📅 13:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71088">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=jLYEMFsMuse95PU43lQhJctRszPYbIeAJIq5wzj9_hzZwriRA5-K1Gx6xXjrlzKB6f66QpLpIccWqM7N7nZLgkh5TDPWTmW8hmOK4sxOb4eLDcpl0TwAPktqLmjSHrUev_5I1TlikQFfyc3iYkx3t7FR_J0Oy9mVIV-KcBGljXFpMOgwnWj33vHQPJ4i3qT1HnIf0s-Xc5cxQFUCL7cpXNdChdqe3gTNIyFzqoD_VVl_i7JgHL-GMG9N5R-eJ9U8Sat-w4_vWBBZg4fsr5vdG1bV0s_OEJaYsNv7Dj8aBG9cqa5dq6jv-rIq9a2AAmKeQ75d01l8FT8JB-AGgWwVFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=jLYEMFsMuse95PU43lQhJctRszPYbIeAJIq5wzj9_hzZwriRA5-K1Gx6xXjrlzKB6f66QpLpIccWqM7N7nZLgkh5TDPWTmW8hmOK4sxOb4eLDcpl0TwAPktqLmjSHrUev_5I1TlikQFfyc3iYkx3t7FR_J0Oy9mVIV-KcBGljXFpMOgwnWj33vHQPJ4i3qT1HnIf0s-Xc5cxQFUCL7cpXNdChdqe3gTNIyFzqoD_VVl_i7JgHL-GMG9N5R-eJ9U8Sat-w4_vWBBZg4fsr5vdG1bV0s_OEJaYsNv7Dj8aBG9cqa5dq6jv-rIq9a2AAmKeQ75d01l8FT8JB-AGgWwVFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با رفیقش رفته دور دور الهیه و به یه دختره شماره دادن،
و حالا اولین پیامی که دختره براشون فرستاده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/71088" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71087">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71087" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71087" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71086">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFwY3ftK1H_R5d8xSc3Em0s24auOwrNDq44QapJ4zHZLw-7HyECbXB-uSMWFZUNL89kgf5kvWgE6Baa7xLXv9POBRHXK0pSs6OABLgpM10mIgDjDJ2r5vjA025Jx0qSJy-3TX-KZJt2LTE79MgOVmcHw5xQW9g_thncOywjYCBK7rz_EZ6nZnxipfH-VdZaCOkr1kH1uuJZPsTLOKFwDNrvh6jc6E8SKVfYbqQoTxcjy6rdeJRxPDhrm3E1HRsjSJBB54_RU4qo6H8FaLMz5Ew7mhHRZ1o_x1hvnZvBwDuaODP1xhk5bu0nXRmX0jkIlx2HpHv_Dc8OWe0iaARy9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب رئال بتیس
🆚
رئال مادرید را در سایت بین المللی
TrexBet
پیش بینی کنید
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر
رئال بتیس: ۲ برد، ۱ تساوی، ۲ شکست در ۵ بازی
رئال مادرید: ۵ برد در ۵ بازی اخیر
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/71086" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71085">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4843999275.mp4?token=Gr902Y1AKpgY9KOgzrW_FnCMx-KMjftGOzSCy-8ih2RD36mS5RrmOpd896T4H_9yfKApowpKHnoVTpVmzWAxg9RhVcotW5qUlfhOcqaa6XUh7Kqt0qtmkxXLfojVkshlNIh08niaEFo5R7aG3IHmRJUyEBtjztBGbYyh1X-yrPkzJz5Lyh4JCKHrRh2H5TvFbaCLPFjR2mz9UAwiRqcJ84jReG9QbqI67qx1fXGmWXskeg-nteIhO0VPZQ33hwHTnXpj2dKBq0uiYN_SzdbKLLzHUiQ0KLODUWzW9ZP5XiZlFmpvVKA8ZdlYrvr3pZQBbfNGQVYdJPxu6FI-v2mpuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4843999275.mp4?token=Gr902Y1AKpgY9KOgzrW_FnCMx-KMjftGOzSCy-8ih2RD36mS5RrmOpd896T4H_9yfKApowpKHnoVTpVmzWAxg9RhVcotW5qUlfhOcqaa6XUh7Kqt0qtmkxXLfojVkshlNIh08niaEFo5R7aG3IHmRJUyEBtjztBGbYyh1X-yrPkzJz5Lyh4JCKHrRh2H5TvFbaCLPFjR2mz9UAwiRqcJ84jReG9QbqI67qx1fXGmWXskeg-nteIhO0VPZQ33hwHTnXpj2dKBq0uiYN_SzdbKLLzHUiQ0KLODUWzW9ZP5XiZlFmpvVKA8ZdlYrvr3pZQBbfNGQVYdJPxu6FI-v2mpuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پرزیدنت ترامپ در رسانه‌های اجتماعی پرسید: «مردم ایران کی قیام می‌کنند و می‌جنگند؟» آیا دولت در حال بررسی مسلح کردن یا ارائه، سایر حمایت‌های مستقیم از مخالفان ایرانی است؟
🇺🇸
ونس:
ها ها ها... مگر پیتر دوسی امروز صبح این سوال را در فاکس نیوز نپرسید؟
سوال خیلی خوبی است.
و چیزی که رئیس جمهور گفت(درجواب به این سوال) دقیقاً همان چیزی است که من می‌خواهم بگویم.
قرار نیست درمورد این سوال صحبت کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71085" target="_blank">📅 13:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71084">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IQ6y9Co5kf_pkFfLMf4KyGoOs3JGbh0YGo1vR3IRHG1w8X8cRXvXtkcQQITt-vjDYwLMYZjuLHgQ90Z6Aea3_OghsZWGeFIYoWt_o1jSNVTncfBturrfabeUKhVCtdH6kA3u3rFFI5uS9rdk4o3zco4IEz0R6GODRqnM5bIxLAYYbIDpwCIXvwLDipn2tjFya9TwNIJYUD7mJjfnYy2Sr0MunHzCnq1wuMgrC0BmNYfUvzfsH9aJgteZ4cAycqq_nebOnuXuvtWGxorA8qfiY1G6_LEkLKUb0oe49sFfh0WHMLPDM0opPpQ_dZGxmMpd2SxCFa29LfCoAoanM1yY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی با این پست به شدت میسوزه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/71084" target="_blank">📅 12:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71083">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=n4IQYkMJFhjFZmo5TQP8lhyqnxA_k3tWVihR46gJX-6hVWwJJ6RJ-yT_V8m8XwB1vDLty_vjDtGYkcS3XcpRCcJR_EjtS8CrsZa6PQV93CNCnKmn-XzUdxjXkKxb0HknpSjwN89kprOFt654jwdGd5yB8TWmHuevbJ57NRSeVlNJid1fPnqUTyracfOP2vGjsB7sBz2886bnqAGWy3Ao6PnkjwZut29fqc-qiHIcxFWmHl06Or2PhgK3Py8-pUb90rW6UIEGhGB2AIsOZyJG5UjzdDE6K3d68rfhngepVMnlGrhr_yIie5jDoEoRDDnsLUxKhVgRyU62usw-Qo4XNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=n4IQYkMJFhjFZmo5TQP8lhyqnxA_k3tWVihR46gJX-6hVWwJJ6RJ-yT_V8m8XwB1vDLty_vjDtGYkcS3XcpRCcJR_EjtS8CrsZa6PQV93CNCnKmn-XzUdxjXkKxb0HknpSjwN89kprOFt654jwdGd5yB8TWmHuevbJ57NRSeVlNJid1fPnqUTyracfOP2vGjsB7sBz2886bnqAGWy3Ao6PnkjwZut29fqc-qiHIcxFWmHl06Or2PhgK3Py8-pUb90rW6UIEGhGB2AIsOZyJG5UjzdDE6K3d68rfhngepVMnlGrhr_yIie5jDoEoRDDnsLUxKhVgRyU62usw-Qo4XNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از طرفدار حکومت
🎙
خبرنگار:
از قیمت دلار خبر داری ؟
🇮🇷
طرفدار حکومت:
بله شده 200 و خورده ای
🎙
خبرنگار:
با این قیمت پس چرا اومدی اجتماعات ؟
🇮🇷
طرفدار حکومت:
دیگه باید قدرت تفکیک داشته باشید تو ذهنتون و قیمت دلار یه چیزه و بیرون اومدن یه چیز
اصلا اگه امنیت ما نباشه شما میتونید راجب قیمت دلار فکر بکنید؟ نه نمیتونید!
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71083" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71082">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⏺
ویدیو وایرال شده از اعتراض یه زن کارتون خواب:
به عنوان یک کارتون خواب که 20 ساله دارم این زندگی تجربه میکنم!
شما مسئولین که مردان خدا هستید شما دیگه چرا؟
تو دانشگاه رشته حقوق خوندم
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71082" target="_blank">📅 11:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71081">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=FaaPxyaAk3FRBRUI2o3kXWTYxiDrqwXV1UJMuzLxXXrfqpazC31wm1CLUHI2Mhn3gnpgDTqx0SMriF5I0t18AXb7pQltpuZAU1MxNmWzooTpNTSbMigkOMCvzaydg8TqbsKz9urgx_6sxAF8bS7uaonoIWX2IfSt7ZUFvNd-wAmrkFh12JqHtZNRCPOu-U1bK86wlfA8IByF-G6RxUWijxR-MWRrJEV-yycdSauzDi9hW1eRoYkOpZ27zM77NfqH1HZrSXXd9R3VukiD3LHriCvcM2_oSnOnQhpQuT_58HtwE6bpcmwKf4odOfgs58tS9Evk_KJRHpCpuGLlDt1N5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=FaaPxyaAk3FRBRUI2o3kXWTYxiDrqwXV1UJMuzLxXXrfqpazC31wm1CLUHI2Mhn3gnpgDTqx0SMriF5I0t18AXb7pQltpuZAU1MxNmWzooTpNTSbMigkOMCvzaydg8TqbsKz9urgx_6sxAF8bS7uaonoIWX2IfSt7ZUFvNd-wAmrkFh12JqHtZNRCPOu-U1bK86wlfA8IByF-G6RxUWijxR-MWRrJEV-yycdSauzDi9hW1eRoYkOpZ27zM77NfqH1HZrSXXd9R3VukiD3LHriCvcM2_oSnOnQhpQuT_58HtwE6bpcmwKf4odOfgs58tS9Evk_KJRHpCpuGLlDt1N5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسره دوست دخترشو برده تو کوچه پس کوچه ها بهش رانندگی یاد بده
آخرش هردو غافلگیر شدن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71081" target="_blank">📅 11:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71078">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=YyoVO1P2GtH24jESJVaaIy_eP9tnr3CWrCOWCDK9PuzaZebUFpInYS5VGe6PgAe6IbySFK4eFRYDP2hd4q-vOf3QKMM-JD9sBBpP_GTYphCLsB9cctUv7Hm2sRW3wzS_kiqyeIudzFBXVKXn7H2Kzzk7LzLURewQe6p5CjwrVxP5V1qPsk4zeTO7UH0KY-CHYtKuXD-o-ufQx0rjQeHXRSBvmQ-8qZSROzvVGC0CuVCmhKRlHpeAKTAIo-ekGCcGYJkU8WaF2K72ul00gdYpZLqxVhvV7xkfuBZjbN5YJhlDm-_e2YsFt8SUAZ5wH5CXxj2T820Wxs3o50m5tK_N-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=YyoVO1P2GtH24jESJVaaIy_eP9tnr3CWrCOWCDK9PuzaZebUFpInYS5VGe6PgAe6IbySFK4eFRYDP2hd4q-vOf3QKMM-JD9sBBpP_GTYphCLsB9cctUv7Hm2sRW3wzS_kiqyeIudzFBXVKXn7H2Kzzk7LzLURewQe6p5CjwrVxP5V1qPsk4zeTO7UH0KY-CHYtKuXD-o-ufQx0rjQeHXRSBvmQ-8qZSROzvVGC0CuVCmhKRlHpeAKTAIo-ekGCcGYJkU8WaF2K72ul00gdYpZLqxVhvV7xkfuBZjbN5YJhlDm-_e2YsFt8SUAZ5wH5CXxj2T820Wxs3o50m5tK_N-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی دزفول چند تا دزد میرن توی یه خونه مجهز به وسایل ضد سرقت و 3 کیلو طلایی که توی اون خونه بوده و قاحب‌خونه قصد داشته باهاش طلا فروشی بزنه رو میدزدن!
صاحب خونه شب قبلش توی اینستاگرام گفته بوده که میخواد طلا فروشی راه بندازه که این حرفا رسیده به گوش دزدا ؛
فردای همون روزی که این حرف رو زده وقتی صاحب خونه خانومش که باردار بوده رو وقتی میبره بیرون یه هوایی بخوره دزدا میریزن تو خونه و طلا ها رو میبرن.
حالا صاحب خونه گفته که هرکسی هر سرنخی از این دزدا داشته باشه و بهم بده ، 10 میلیارد تومن بهش پاداش میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71078" target="_blank">📅 10:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71077">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0def551e36.mp4?token=V6RnHP5wpked8QWEnvRCkCkkA8FBcHianBdLu53zX3gZS5woaP0WQmAsEPRyN_zvLiAupQMctJAO6vYTAVCKBD6r_EXsRoEUJolCpa4hBvp7ksiPC3BpvJuXLHdGRybJv8_ksSVuxI8Btp46jKUjKDb1iKCqKkaiNuN3Wz8IzTp9KcMaMshkAJGjDs7JC6I4fu4OTFleG1MCoG3le5EbasPNKUmyphcrkBw0YlN_-ktaMcvvPpxPg2f4dSqWimRaO3FQ5feWkiJj4ZkJLtaBVToul3xU22ApOvnrD5wbIdgNLU5KDhyIe2Gg3c4GaD8SrZgfe0OSio7OoGjFq5BhHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0def551e36.mp4?token=V6RnHP5wpked8QWEnvRCkCkkA8FBcHianBdLu53zX3gZS5woaP0WQmAsEPRyN_zvLiAupQMctJAO6vYTAVCKBD6r_EXsRoEUJolCpa4hBvp7ksiPC3BpvJuXLHdGRybJv8_ksSVuxI8Btp46jKUjKDb1iKCqKkaiNuN3Wz8IzTp9KcMaMshkAJGjDs7JC6I4fu4OTFleG1MCoG3le5EbasPNKUmyphcrkBw0YlN_-ktaMcvvPpxPg2f4dSqWimRaO3FQ5feWkiJj4ZkJLtaBVToul3xU22ApOvnrD5wbIdgNLU5KDhyIe2Gg3c4GaD8SrZgfe0OSio7OoGjFq5BhHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه دختره داشت تو قزوين واسه خودش قدم میزد؛
که یهو یه پیرمرده خواست مزاحمش بشه ولی بعد که فهمید طرف پسر نیست، عذرخواهی کرد و رفت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71077" target="_blank">📅 10:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71076">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=CByrzygJ4u5E7SiR6f-o36EE0OqYiK2wwHfwif7aXmG-O4J2EXTiCl1D4SCuO3bHm3669w4oxBhxxKvN8HwOKYEn3sCnbKr3EPEfHUyEccXqmZSDEFlFexA9NhqlgXC2EhnxMH8WiNF5i1LfF2wn5pCuI7OSCrwCSBEz7pOagz0rH7_CIN_kN6IGNuBAFt_iu1hGqqs7bDP3TRQwDOm_aLS1dpzaSyKMby8DVnwUBYJUYSB9owuTVdI3FJbgU8wuUVHVNwAc8YaDxOOGWN3hqGN2HKi7PA3bOo6X41R4LoqoZqHt84z5dSMUsFhNwy72-dFZVjfoJeplFi11S9xykA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=CByrzygJ4u5E7SiR6f-o36EE0OqYiK2wwHfwif7aXmG-O4J2EXTiCl1D4SCuO3bHm3669w4oxBhxxKvN8HwOKYEn3sCnbKr3EPEfHUyEccXqmZSDEFlFexA9NhqlgXC2EhnxMH8WiNF5i1LfF2wn5pCuI7OSCrwCSBEz7pOagz0rH7_CIN_kN6IGNuBAFt_iu1hGqqs7bDP3TRQwDOm_aLS1dpzaSyKMby8DVnwUBYJUYSB9owuTVdI3FJbgU8wuUVHVNwAc8YaDxOOGWN3hqGN2HKi7PA3bOo6X41R4LoqoZqHt84z5dSMUsFhNwy72-dFZVjfoJeplFi11S9xykA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه دستگیری یه قاتل فراری در ایرانه
:
قاتل با چاقو مامورا رو میزنه و داشت فرار میکرد که یکی از مامورا عین راموس تکل زد و طرف افتاد.
بعدش یکی دیگه از مامورا ویلچر برداشت و میکوبید تو سر و بدن قاتل تا بیفته زمین، هر لحظه این فیلم عجیب‌تر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71076" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71075">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L229KRy5cpPbotHr68bBeJhKkdJbdTUq4uO4EiPuU21HrKC1Qgae9C1Nrj3J5tbt8_Nh34dO_JVx_g9LD-doX8GzfkA5EJuBuQqsoW6U-ukMRWic5gZx-Trby7NtagwhwSH2D4L60a0y0iYAcZf4O3FCt0vhJyNskQic1zRpUHLpXpREGuNrl6nYSeekaIC-RA-dzFUIwJulHH4b2RfWjok9-iIwvELHsa6xtOdV78hJVeunvJorAu2QpHt9IBWgOuxnb2VSNWZ0rZktBLLrF843uYEXqBadNQVOG6IJE883jC1fu9HO41qnTv4zFrvns9EAqh4IO4sUjA4pFplROg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
⭕️
#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
اتحادیه اروپا رسماً به «عملیات طرد اقتصادی» (Operation Economic Outcast) پیوسته است و ما از موضع قاطع و زودهنگام آن‌ها قدردانی می‌کنیم.
ایالات متحده در کنار متحدان خود قاطعانه ایستاده است تا اطمینان حاصل کند که رژیم جنایتکار ایران نمی‌تواند از سیستم مالی جهانی برای تأمین مالی جاه‌طلبی‌های هسته‌ای، برنامه‌های تسلیحاتی و نیروهای نیابتی تروریستی خود بهره‌برداری کند.
جهان پیام روشنی به رژیم ایران می‌فرستد: ما تا زمانی که آخرین شریان حیاتی مالی باقی‌مانده قطع نشود، از تلاش دست نخواهیم کشید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71075" target="_blank">📅 09:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71074">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71074" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71074" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71073">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuGU0xv4iee-utA3CjLyCILacar9pXg4B-rTPLdwq-41eU7JvhcyrhRv6GI52IkeD3NBzN3JnMqXMPvbZXBS4J1-pP4TCOslgSTnoLGv6TdopciNdP545fGfh4SjAer176mwTMwh1rBrPVjA1neRp4ZSfnqkhRLhQ1Z7INkRmzw0mHV-FyKVBTdgepgi4vBG99LDwZTbNssuU5awj75_J7PoIUCrTQx4dJtRihbru3F5kKHV7ebmKDH3pBC35SPz7iyPoLNTvjA3NKwbe_4Cd8WVgRgqxhCOZd-3yPpi0A-OEF7NGtpm9aSwKHrWxmQFhlHCuFxeXm7v7oh81eM2zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71073" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71072">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🇮🇷
نایا:ایران چندین موشک به سمت کشتی ها در تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71072" target="_blank">📅 01:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71071">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c46c090035.mp4?token=LSJero3CKIeNm5fA_N95-6dvX4d9GkbTeIS-DU45VBdtXTHBOiXH04KLF9gYb6yoeAjPlZvXNJpx-jFZeGUWiiIV7j3NXaAh9CwDNDJV-ILLmXS6mmU1DP9dPE_cOAv25iORShAFGqZBbZgolyIaMY_HkhTJA2RSKxhbeBN7Fw2-13olhog70FQi123YEmIP51dd-5cE5SaUVqjdctCE5ywpI_IisIQzfsO9tmqrEvPg4pF9xgahIL4YCb4xb99GdoRQZ5DcL6chTDeC8BzOFHY-qdj2Tr-vDWT6nr5LH6iEHuN4Sy8DkB9-xujvHhmSLjDIkIN7Teik_BCGhrpKKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c46c090035.mp4?token=LSJero3CKIeNm5fA_N95-6dvX4d9GkbTeIS-DU45VBdtXTHBOiXH04KLF9gYb6yoeAjPlZvXNJpx-jFZeGUWiiIV7j3NXaAh9CwDNDJV-ILLmXS6mmU1DP9dPE_cOAv25iORShAFGqZBbZgolyIaMY_HkhTJA2RSKxhbeBN7Fw2-13olhog70FQi123YEmIP51dd-5cE5SaUVqjdctCE5ywpI_IisIQzfsO9tmqrEvPg4pF9xgahIL4YCb4xb99GdoRQZ5DcL6chTDeC8BzOFHY-qdj2Tr-vDWT6nr5LH6iEHuN4Sy8DkB9-xujvHhmSLjDIkIN7Teik_BCGhrpKKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پورمحمدی:
انسداد تنگه هرمز، برنامه‌ریزی شهید پاکپور بود.
شهید پاکپور پیش‌بینی کرده بود که جنگ با ترور او شروع می‌شود.
شهید پاکپور برنامه‌ریزی کرده بود که اگر جنگ آغاز شد و او دستوری صادر نکرد، فرماندهان ۲۰ دقیقه بعد شلیک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71071" target="_blank">📅 00:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71070">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46300e7107.mp4?token=cZm6DIdrnwEiiQttWi5390cFNTMjU7hUVnblRHwTqK7xph8FKd8kbtwi4nRjYaPzPjMFnIFqghYQqWq6647re4dwJuXt8uyxEtllUuBdprWxmiEbFzdIReJ_ejkXWNz_sTqRjAKhfMOfnt-R8PzEJstoNe_5imwnDv-mdQL9990j3rBYFxYAvAhpsHwoY1XkXqVe0rMaNXBBJ41X39zv62ZaMEXyq03uHFbsiorGHNjFulLjTthiu7B-OXiGOzT6CpeibgGG0-R3hw_SEbTaDWnlctgpRjrUpLJbv_hDWhPLDBP5yEqOznK2bE1Lxwkt08CpVtwiNiWatDWISCjvNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46300e7107.mp4?token=cZm6DIdrnwEiiQttWi5390cFNTMjU7hUVnblRHwTqK7xph8FKd8kbtwi4nRjYaPzPjMFnIFqghYQqWq6647re4dwJuXt8uyxEtllUuBdprWxmiEbFzdIReJ_ejkXWNz_sTqRjAKhfMOfnt-R8PzEJstoNe_5imwnDv-mdQL9990j3rBYFxYAvAhpsHwoY1XkXqVe0rMaNXBBJ41X39zv62ZaMEXyq03uHFbsiorGHNjFulLjTthiu7B-OXiGOzT6CpeibgGG0-R3hw_SEbTaDWnlctgpRjrUpLJbv_hDWhPLDBP5yEqOznK2bE1Lxwkt08CpVtwiNiWatDWISCjvNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چندشب پیش تو شیراز یه دعوای عجیب رخ داد؛
دوتا دختر با ماشین میزنن به ماشینِ دوتا پسر؛ بعد گفتن ما مقصر نيستيم و داشتن فرار میکردن!
پسرها هم گفتن چون بی‌ادبی کردی، باید بمونی خسارت بدی، بخاطر همین پریدن رو کاپوت ماشینِ دختره که فرار نکنه!
این وسط یه پیرمرده هم خیلی بی‌دلیل از دختره کتک خورد...
تهشم دختره گفت دیگه این موضوع واسم مهم نیست چون زنگ زدم شوهرم سروان شهریزی، الان میاد کون همه‌تون رو پاره میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71070" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71069">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876466a913.mp4?token=ZT8ApHwRyvtfU29pJoW3FuZGmHWHMKrxR0ufYqlq3T2Kx3hUBFVstJF3nwwR5QVZHOtHkKjoc9R_IEkpdkWtvkxsVP-b9WiVnbgfgqCf9ZqzT4GjQdGL05Y72pWgArZJEgipV5t5VrDkHX7tzxHDd-NCkPKBNWTSQasdOCYrIhUi4uFoe0u-nzkH6M6Vkje7wFqpo081u67IjJiEonUuSRA3I4YiBoZ3sSU0B1g7sw8DepWqWkVjEfKkOvCwk4vxzBPqJa3LUJzei1MLlRDTGSahQTlwGxjmLIuMSz-zbqdIrHsLRiyhD2KmvGhtRtkTgTY6crS07xOjW6L7Hl4hvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876466a913.mp4?token=ZT8ApHwRyvtfU29pJoW3FuZGmHWHMKrxR0ufYqlq3T2Kx3hUBFVstJF3nwwR5QVZHOtHkKjoc9R_IEkpdkWtvkxsVP-b9WiVnbgfgqCf9ZqzT4GjQdGL05Y72pWgArZJEgipV5t5VrDkHX7tzxHDd-NCkPKBNWTSQasdOCYrIhUi4uFoe0u-nzkH6M6Vkje7wFqpo081u67IjJiEonUuSRA3I4YiBoZ3sSU0B1g7sw8DepWqWkVjEfKkOvCwk4vxzBPqJa3LUJzei1MLlRDTGSahQTlwGxjmLIuMSz-zbqdIrHsLRiyhD2KmvGhtRtkTgTY6crS07xOjW6L7Hl4hvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق گفته خانم دکتر؛ دیگه خوردن واژن خانم‌ها نه تنها دیگه نباید باعث خجالت شما بشه بلکه پر ازخاصیت و فواید زیادیه که تاحالا درجریان نبودیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71069" target="_blank">📅 23:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71068">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYJSeRUVM7xx6lwcnNceBB6ma-suY0s9-ZAlPMfTnnBRf51XG0gAwSAysjgEkEAIDRtbgpGFN-BfTchmkCloVKhuUEQz4y2qWa9Xay6dJl-6aVNcOjMKNXAGxuWlPHyPywUA-q-c6Ixy1jTBgYgCerYzUH8S2qAodrfx_wp63VN_zXj_aqsGtaasX2HPbtp_pqA0TJEU-3EP8kGVmdc4Q1mlX9nmflw6I0eOLfRibOXxPhxhFrBKHS-b7rxmhGqbpWrdAVTbF3IMw6PHvIBpQRlch40fuYttFNsNDV-M6nFuKlqj3KG2VcnRgV7hatY10G3BMqy-sr8FWGKJwjNKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیبافِ:
قهرمان، محکم‌تر «شورت» (Short) کن؛ طوری که انگار آینده‌ی شغلی‌ات به آن بستگی دارد (چون واقعاً هم همین‌طور است).
یا اینکه سطح ذخایر را به زیر «منطقه خطر» برسان و فرو ریختنِ آن حفره‌های عظیم (و البته نابودیِ شغل خودت) را تماشا کن.
یا هم به درگاه خدایانِ نمکِ «برایان ماوند» (Bryan Mound) دعا کن.
دنیا که از همین حالا بساط پاپ‌کورنش را آماده کرده است :)
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71068" target="_blank">📅 22:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71067">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=PpOSKbTYi3Y-vbvE9AwqpYnXsB3uTyOBasQ0J8z0SL8gUYIdPyJXhF2E0OwzI8V70h48B3OPV0M4Wqr6nADQLtfD_bCXA3IKleewEahHW12dyS0lamf-cFY268XSxONYkQyIVNXf4zh8i1xIvkGdXiMutp7t8fsh3H-QVKFAYM4tln9QnLN9QSKFf6VwxP-RVfVDdG5GrL1iJclBfk0gm8XJM2luLIoHq0bYeQnI0BzKdk-1zggr-h1U2K2gW6cXCWUNkp0pHXHwuJtqdNyNz3peD_GtzrTueWYU4yra3okGG_vJiwuUXaE8NJ0thRpcogFFY7u_ltWI3Rxi9wY8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=PpOSKbTYi3Y-vbvE9AwqpYnXsB3uTyOBasQ0J8z0SL8gUYIdPyJXhF2E0OwzI8V70h48B3OPV0M4Wqr6nADQLtfD_bCXA3IKleewEahHW12dyS0lamf-cFY268XSxONYkQyIVNXf4zh8i1xIvkGdXiMutp7t8fsh3H-QVKFAYM4tln9QnLN9QSKFf6VwxP-RVfVDdG5GrL1iJclBfk0gm8XJM2luLIoHq0bYeQnI0BzKdk-1zggr-h1U2K2gW6cXCWUNkp0pHXHwuJtqdNyNz3peD_GtzrTueWYU4yra3okGG_vJiwuUXaE8NJ0thRpcogFFY7u_ltWI3Rxi9wY8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ارتش اسرائیل تپه علی طاهر در جنوب لبنان را فتح کرد و کنترل آن را در دست گرفت.
ارتش اسرائیل پاکسازی دو مسیر تونل زیرزمینی حزب‌الله در رشته‌کوه علی طاهر در جنوب لبنان را به پایان رسانده و در تلاش برای خنثی‌سازی آنهاست.
لشکر ۳۶ کنترل عملیاتی رشته‌کوه را در بالا و پایین زمین به دست گرفت و آن را از وجود شبه‌نظامیان پاکسازی کرد. برخی کشته و برخی دیگر فرار کردند. خنثی‌سازی زیرساخت‌های پاکسازی‌شده در حال انجام است.
در داخل، نیروها مراکز فرماندهی، اتاق‌های تسلیحات، اتاق‌های ژنراتور، محل‌های زندگی، دوش‌ها و یک آشپزخانه را یافتند -- که به شبه‌نظامیان اجازه می‌داد عملیات جنگی را انجام دهند و برای مدت طولانی در زیر زمین بمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71067" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71066">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWKrALVaXLGcJ82N5Ca4MeGhx9bfxSLsBJCt3Y-EVilINnYmahIZxN3PSpPiHHPo2AgdUD00XPawXSFn-FPux8d_ufbexh6T5JvEtLeRrmvj3mCUxAUU3yDSQKnQsnl78xr9_bZgWDuVVZqkzSYdQ1Zj5uuJZbbcGhUjlRreYQZ6m8SnBeuOVXEmsa1yHqlkJxuQA7SkCdzV5qdQz0LUIdaC8jpgwMH0WFDzbxT2eRzBFSHLpJzknHzur8cdzLqu7BKYopAEv0DG3CX1ug1NXxvDMYpEAD4lT4yN1tmKEoNFQ7u6FLCTdFb9te_yYeaBQdb2-SrjKR3fPqYkfTHA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید حضوری با اسنپ‌پی، یه خرید معمولی نیست؛ شانس بردن BMW داره!
😎
🚗
با اسنپ‌پی می‌تونی از بیش از ۲۰ هزار فروشگاه حضوری خرید کنی و هزینه‌اش رو ۴ قسطه و بدون سود و کارمزد پرداخت کنی.
🎉
🥳
همه‌اش همین نیست؛
۵ هفته، ۵ برنده، ۵ جایزه در هر هفته هم در انتظارته:
🏆
۵ گرم طلا
📱
گوشی Galaxy S25FE
📱
گوشی iPhone 17
💻
لپ‌تاپ MacBook Air M4
🎮
کنسول PS5
این شهریور، حضوری خرید کن و شانس بردنت رو بیشتر کن:
👇
👇
👇
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71066" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71065">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=thHqyNxX_uioUg1bhj7SVTmKdWpO59zuHeiqf0_ecM2nAyYf5EdHCi-cjbB_6brs90Ax9l1utU83tObUUVpKTBMuFv2NvKwDpOp1A_A1xOE4xZ8PZT_efct4Ed3BRyBTyWnci1EQSrEtk9d2bKuwE19l7DmNINYQZw5X9kz8_4CHY7Y2zlS7mVdkkHw6RJjLwGAyqX5wuk_diyziQcqxM9eCEJt-DP7J7iYUWnQBBRP6M3utcMdIchtbWSdyVBDrPAI2GidLoPrAlbdHUdpjBpS3NXyrDFoKJ2Ui5fKxD8fEiWy4q56soT6znSCDS61NcAi32-r0NUVrnagYxme4LJABt9C9zrrhWjmdqI22WwBHG6Ul2BKwC-gGz6sQAA6iYdL3EwlfDpwEzOHpHApoPGQdgEJUw1Ox8yPNlTO3HPKrKL-kQG8RMEwpKhp1tttHW1rMDgknBpIOsvJzci7hM6KNfSlyuggCtD2qIQYiEfv9yWdU5PdXM_JJTG0Rtfza81mbTqnJh2rgMLAkr1s_VQ98mYRaAME00JaBcV6HFlcj-rEJht1de1oP1uYYsdX_tX7jO8VvtCG_Jzs3u2IO4jWaFNMDAwHkfxFoi9gLcv2AJ0YRPOvFx7odMr_Z65v0aSiNBycLU8PGDpFnu5xh6Yk9rNVjnnml1qe8mfMjHis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=thHqyNxX_uioUg1bhj7SVTmKdWpO59zuHeiqf0_ecM2nAyYf5EdHCi-cjbB_6brs90Ax9l1utU83tObUUVpKTBMuFv2NvKwDpOp1A_A1xOE4xZ8PZT_efct4Ed3BRyBTyWnci1EQSrEtk9d2bKuwE19l7DmNINYQZw5X9kz8_4CHY7Y2zlS7mVdkkHw6RJjLwGAyqX5wuk_diyziQcqxM9eCEJt-DP7J7iYUWnQBBRP6M3utcMdIchtbWSdyVBDrPAI2GidLoPrAlbdHUdpjBpS3NXyrDFoKJ2Ui5fKxD8fEiWy4q56soT6znSCDS61NcAi32-r0NUVrnagYxme4LJABt9C9zrrhWjmdqI22WwBHG6Ul2BKwC-gGz6sQAA6iYdL3EwlfDpwEzOHpHApoPGQdgEJUw1Ox8yPNlTO3HPKrKL-kQG8RMEwpKhp1tttHW1rMDgknBpIOsvJzci7hM6KNfSlyuggCtD2qIQYiEfv9yWdU5PdXM_JJTG0Rtfza81mbTqnJh2rgMLAkr1s_VQ98mYRaAME00JaBcV6HFlcj-rEJht1de1oP1uYYsdX_tX7jO8VvtCG_Jzs3u2IO4jWaFNMDAwHkfxFoi9gLcv2AJ0YRPOvFx7odMr_Z65v0aSiNBycLU8PGDpFnu5xh6Yk9rNVjnnml1qe8mfMjHis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ترامپ هم اومد به بازار
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71065" target="_blank">📅 21:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71064">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=bySGzUU-aQ9ANWaRchy0RIuWWkYVqYRfTwL9d0icxI14gwLDyTIns5xIviDFOdcMpGlHKfPx3WKNpfjWFyqvKX96uU0Ii8d93bsu4UJolDzpLLd4KKY4xRvfB3007nM1PjcML1-4CPo_oXntD4cAJCFqUZqN_8vrDG1M3U9xGWhkCJkFh0rF32xcC3HUBcZjjZVrau_JokJJUHlebRcpNU95hZBTILvTUj9d-y_THI4hjZG4mXEzS2h4G1R9LUfnXheeNV8SVA6EhGqOhu6IhIMhHtCTblXAdUncAc7hY9RCpQl7jaLHbI4XjbdgBkLBtcH5a9nIi7VXW9pCUmnZfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=bySGzUU-aQ9ANWaRchy0RIuWWkYVqYRfTwL9d0icxI14gwLDyTIns5xIviDFOdcMpGlHKfPx3WKNpfjWFyqvKX96uU0Ii8d93bsu4UJolDzpLLd4KKY4xRvfB3007nM1PjcML1-4CPo_oXntD4cAJCFqUZqN_8vrDG1M3U9xGWhkCJkFh0rF32xcC3HUBcZjjZVrau_JokJJUHlebRcpNU95hZBTILvTUj9d-y_THI4hjZG4mXEzS2h4G1R9LUfnXheeNV8SVA6EhGqOhu6IhIMhHtCTblXAdUncAc7hY9RCpQl7jaLHbI4XjbdgBkLBtcH5a9nIi7VXW9pCUmnZfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
رقص عجیب «حسن حسین خانی» مداح نزدیک به حکومت  در حالی عجیب  و  با شلوارک! تو یک  ویلا با آهنگ شماعی زاده
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71064" target="_blank">📅 20:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71063">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=XXaRxiB0kADk10ZUznd7JqUc4yIm2YUzc0jCb9lmFItHkuKgaswafUKkjQJudFbzXuIxLoZ9NWq2f_D-8CaAL6zV2sSvpWj3c-C3I1gybeE69LE3RVqg2wLbsh-m_Pcldarv0tkc340LjfBkC7LX3IHTm88_dTYZd0vKw9kKaK3RmIeJ9C2nbuZEjbgB9ECbpN3XWcLIkJsGGZ25wkjNfTmdWWu_RmGj_dGpziEEwGTAeoNFiTrBR8tMBQRocCGh_hKfBCtHXW4WzyRXS9H4I4KlEorCdbXuDynVyFd_sw6m2ncDtpev9N8AR5iZaQYlwQzU3oe-xIUJeZSbqLcD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=XXaRxiB0kADk10ZUznd7JqUc4yIm2YUzc0jCb9lmFItHkuKgaswafUKkjQJudFbzXuIxLoZ9NWq2f_D-8CaAL6zV2sSvpWj3c-C3I1gybeE69LE3RVqg2wLbsh-m_Pcldarv0tkc340LjfBkC7LX3IHTm88_dTYZd0vKw9kKaK3RmIeJ9C2nbuZEjbgB9ECbpN3XWcLIkJsGGZ25wkjNfTmdWWu_RmGj_dGpziEEwGTAeoNFiTrBR8tMBQRocCGh_hKfBCtHXW4WzyRXS9H4I4KlEorCdbXuDynVyFd_sw6m2ncDtpev9N8AR5iZaQYlwQzU3oe-xIUJeZSbqLcD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
من به توانایی‌مان برای از میان برداشتنِ یک‌بار برای همیشهٔ این تهدید ــ یعنی سرنگونی این رژیم ــ اطمینان کامل دارم.
این همان مأموریت اصلی است که همچنان پیشِ رو داریم، اما به تحقق آن نزدیک شده‌ایم. این کار غیرممکن نیست؛ بلکه کاملاً دست‌یافتنی است.
آن‌ها بی‌دلیل از حمله به ما پرهیز نمی‌کنند؛ آن‌ها به همه حمله می‌کنند، جز ما. آن‌ها از قدرت ما، توان بازوی ما و عزم راسخ ما آگاهند.
من خطاب به دشمنانمان به‌طور کلی می‌گویم: با ما درنیفتید. اگر درسی گرفته‌اید، بدانید که نباید با ما دربیفتید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71063" target="_blank">📅 19:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71062">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
شلیک موشک/پهباد از سیریک به سمت کشتی ها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71062" target="_blank">📅 19:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71061">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6xAI2GzfLzlWJy7RHSJvxPBUPRpaCxrD7VBjhwQofDAlAmr81MBRcjcoDKh7K3hge8OEphhQQh_SmPyUFppg8hh1YDUwvOxZU8qZuCe0pcrS4sK2gEsf-AQS2eeZIRXXjYulLEmRdZawZDpvcNhkXtgWEfJjId6Zpz-ehGveqDConplQAF8Nqgh_RoFfM3UTwie9YlqwiqJTjeslMVHrts6RRRf3COwbYIpP6pSOJrSQnoeVuRkWQPh56-RHBW7iUAf7lKtX3BEL-hzUeiBauDw_zepBfGOOKEtmxutvkx0qvPC6RW8Tw2KkKt9pCpaqGzj1-xXuOgq-OCY7pgi3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
برای آن مشتی خائنِ پست‌فطرت که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کنند، باید بگویم که ما ذخایر تقریباً نامحدودی از مهمات با کیفیت متوسط تا عالی در اختیار داریم؛ بسیار فراتر از آنچه ممکن است برای این عملیات یا هر جنگ احتمالی دیگری (که وقوع آن بسیار بعید است!) نیاز داشته باشیم.
علاوه بر این، ما در حال تولید مهمات با حجمی بی‌سابقه هستیم. ما در حال انباشت و آماده‌سازی برای مقابله با هرگونه وضعیت پیش‌بینی‌نشده‌ای هستیم که ممکن است رخ دهد.
ما این مهمات را برای خودمان — یعنی ایالات متحده — نگه می‌داریم و فعلاً به دیگران نمی‌فروشیم، هرچند فروش به متحدان به‌زودی از سر گرفته خواهد شد.
همچنین، لازم است بدانید که دولت بایدن حجم بسیار بیشتری از مهمات را — بدون دریافت هیچ‌گونه هزینه‌ای — به اوکراین واگذار کرد، که این مقدار بسیار فراتر از مهماتی است که ما در ایران به کار گرفته‌ایم.
صدها میلیارد دلار کمک رایگان به اوکراین و ناتو اعطا شد؛ هزینه‌هایی که اگر از اروپایی‌ها خواسته می‌شد، خودشان آن را می‌پرداختند.
با این حال، ما آن پول را مطالبه خواهیم کرد، هرچند با کمی تأخیر!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71061" target="_blank">📅 18:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71060">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=RrVx6eYDM55RBPVrBG_TaB89Ehlh3xTjhNBaQDSDukZspShnLHCMNvtBKG6H5KE-osbdxj8tfDkFBEwUzZbTy4nLyDPb5AetDcnxI4UtVV3X8I32Gt0SWzvuzjb-dj4mjsQm5POmNNL9IuhsINm4H2xW8zOXQ_sCEwr_ROwvVLmPumMA3RXklhWbidYFeyqgWR5yAwWyfa8AV_wsNyOKJJ4-QbOSXr8KSKBSEpfyJhzEX2Z-5FAKr95HIdNSzadXoyulHIzgR_DbI00N81K3xmHM2SiS2toi1jmxbrZ4idP_PH6FBvxZEm05xG3wAi5Zv6Phw7vjMEP-40eYJewlwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=RrVx6eYDM55RBPVrBG_TaB89Ehlh3xTjhNBaQDSDukZspShnLHCMNvtBKG6H5KE-osbdxj8tfDkFBEwUzZbTy4nLyDPb5AetDcnxI4UtVV3X8I32Gt0SWzvuzjb-dj4mjsQm5POmNNL9IuhsINm4H2xW8zOXQ_sCEwr_ROwvVLmPumMA3RXklhWbidYFeyqgWR5yAwWyfa8AV_wsNyOKJJ4-QbOSXr8KSKBSEpfyJhzEX2Z-5FAKr95HIdNSzadXoyulHIzgR_DbI00N81K3xmHM2SiS2toi1jmxbrZ4idP_PH6FBvxZEm05xG3wAi5Zv6Phw7vjMEP-40eYJewlwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
کسانی که دوستتان دارند، شما را فردی خوش‌برخورد، شوخ‌طبع، سخاوتمند و بذله‌گو می‌دانند؛ اما دیگران می‌گویند که شما سخت‌گیر، متکبر، مغرور و حتی بی‌رحم هستید. به نظر شما، کدام‌یک از این توصیفات درست است و کدام نادرست؟
❤️
شاهنشاه آریامهر:
بی‌رحم؟ گمان نمی‌کنم.
متکبر؟ قطعاً نه.
مغرور؟ شاید کمی. اما در مورد کشورم—و آنچه به دست آمده است
نمی‌توانم شخصاً دچار غرور شوم، چرا که انسانی مؤمن هستم. من عمیقاً به خدا ایمان دارم و اهل عرفانم؛ پس چگونه ممکن است مغرور باشم؟
انسان در پیشگاه ذات ازلی، هیچ است؛ مطلقاً هیچ؛ گویی اصلاً وجود ندارد.
البته با نگاهی به دستاوردهای این کشور، قطعاً دلیلی برای احساس غرور و سربلندی وجود دارد.
اما بی‌رحمی؟ این ویژگی من نیست؛ این نهادهای حکومتی هستند که باید عمل کنند.
وظیفه آن‌هاست که کسانی را که قصد آسیب رساندن به این کشور را دارند شناسایی و خنثی کنند. اگر نام این کار بی‌رحمی است... خب، در آن صورت باید بپذیریم که در این مورد با هم اختلاف‌نظر داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71060" target="_blank">📅 18:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71059">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259e330a05.mp4?token=aVMExSXhPKqxLWa7gtHfFkRFsKUKnmCpiTVipPykT4W9KOA_eMg8gTrdKNuSb-WJQj83YkdrfDy42lQzShzNVXBEZz9KF0IHyQ_NH74qb2I8I-61V-FZQzB7UDfRMX2EvZe3nJSY2m1MzTKj5vsrsTdrdxS3fd-BdS2begsztrZAGSZ_Fpa1_EpoNukgq6dFKAqk52GNT7x8L1fhulTklTYYukg1WBiXkSGPipSfcgUO0s9dxOPLIdORlrLs5SsXs0Sdez1iGZUFoCrVguCnQQqA6QjKlPl9VlTkm2hoFw-XrwW3XqtByBRxss6nVSGLOi8bZioSlnfADUQylb6DUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259e330a05.mp4?token=aVMExSXhPKqxLWa7gtHfFkRFsKUKnmCpiTVipPykT4W9KOA_eMg8gTrdKNuSb-WJQj83YkdrfDy42lQzShzNVXBEZz9KF0IHyQ_NH74qb2I8I-61V-FZQzB7UDfRMX2EvZe3nJSY2m1MzTKj5vsrsTdrdxS3fd-BdS2begsztrZAGSZ_Fpa1_EpoNukgq6dFKAqk52GNT7x8L1fhulTklTYYukg1WBiXkSGPipSfcgUO0s9dxOPLIdORlrLs5SsXs0Sdez1iGZUFoCrVguCnQQqA6QjKlPl9VlTkm2hoFw-XrwW3XqtByBRxss6nVSGLOi8bZioSlnfADUQylb6DUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های این پسر درباره‌ی اونایی که میگن کسایی که ریش ندارن کونی هستن رو با هم ببینیم:
کدوم مادرجنده‌ای اینو باب کرده که هر کی که ریش‌وسیبیل نمیذاره، کونه؟
شما برو فیلم سوپرا رو نگاه کن، عمو جانی کونش هم یدونه مو نداره، چه برسه به صورتش.
ریشو کسایی میذارن که ترس از کون‌شون دارن، اونایی که عقده دارن و بچگی کون‌شون گذاشن، ریش میذارن.
خیلیا ریش دارن ولی صد مرتبه از کونیا بدتر هستن
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71059" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71058">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71058" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71057">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJHDJrvM0uY_OAfvdv8zSG47LgSFiVg2_-rAISf22_mgZXBm3r0lMU5D1Ft6n1Gg1K-HbDAzjmVfPeqvKWZ0ajGjvFaF9I-MfOIEmRNgcxHos_uU-zVW5PMxNniCGV6Elbglv7nlMy8kR7SklDpVlBY7GIs4VzZbpV4yPTUmF4BBSVthVVpuNkWNJRQnUuWnvNOwWGtTGUaSasOOyypYoTY_cC4GV5vmTcKHjDbL_NCovCBs6g9WsonNGDidJE1TquLvsNis7zPa6BLmLw1sUkInGJVhRIwgDOFkFv_2_4y8XfS3WY--0_cb7q7j1Zb1wEH_hA6lsj8Ibkwo8ZS01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71057" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71055">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAsZnDtw0R0NDTTpXT6hrPcI97ul6ugfHoLAnxOwrO1Zq_WKuuCFWtof1riZzTw1Mow37tUjwKVr96NoB9Y4NmoZD9IvL45LiJBCqq5KSwuuPSaopwGCPFOBTQL_1H0luYHAkqce_4UUrPdk4LggEHeVQGJDuxDDE7JMk_7rnMBffQinqZ_deOy_gyvbxTlRhaTKdYcK6_paX0uLQNGETlnZXexo9YJxzxtlf17-3gB4WZRlPbMUT0uDRwKmYhXKDIS1ukICTyU2R0ATgyKLvsUyPJIcETYHwzsSY73PHAHx7jvz4rLXvW-_fzWYHv2oWgLpAYfD8ldb50P5Wmrcgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
💬
🙂
پست جدید تلگرام در پلتفرم ایکس:
حس و حال بامزه‌ای دارم، شاید بعداً عکس‌های نودم رو منتشر کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71055" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71054">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_f526ww5iq2iSbVzFao6VrCt1q7AiX5y8Rd_gktGzq47M6z2uYME9-HG1-Xb1RIfe4cVb19mcSPmKH9Zzfwbi_CESsrh1BPeicpm_ClYELjUYTFe8N6UBSVnJGErNGFN-nJyURnuNqo0L8o7o31dIdyrnkTlYxzk1JSkWNH1vjCUOxUyNheSL0JvRwM-u5pmyg1Z69pFYDRq5AS6xuL5KjoYTrtPHV5aLhq9DSB-KnD9R3B4rNC0ufeltu37Tny6oHaMzC0xPtW3kMlAnHOhLOYHJpvC79ikCHX139iziZGALYfYp6G6dGXFSDCVe86KP3RLqk178spIN4mKMX_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
جمهوری اسلامی کشته شدن سه خلبان نظامی در حملات آمریکا در دو شب گذشته را تأیید کرد.
اسامی: مجتبی باقری و حامد اوکاتی (خلبانان هوانیروز/هواپیمایی نیروی دریایی) و حسین مهدویان (خلبان نیروی هوایی).
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71054" target="_blank">📅 16:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71053">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=Htx1A80X7AsZxa5wtV3GIr3j_iRKyuJC6UyMZ18k3CpswxskyFjC5adLABB_gzfUy98lKS1XvUh2NLWAuSlcHUKWKsQgGKjJHNSKFrMIY_B6OPoc8ch2b-Widqt6HlQMirA6r7rYbTTplJ08y08YvaHPraM3lO35G4agkIBwo9mAelXa5RZfHyU1KWYcHBUTlo14WI-3HDotrKltWMqXW0CqgiU8xMrbPMHjVnNYpknIisBxsyGgySb5pbQlpdXflwvfDWr4H2H4ynyHSSnnp_WP7JlvU2LdsZkkfNMCBMJTTnm80phEpj-k11FFdVmORXK9y9KIs_BO7Opq2UF7sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=Htx1A80X7AsZxa5wtV3GIr3j_iRKyuJC6UyMZ18k3CpswxskyFjC5adLABB_gzfUy98lKS1XvUh2NLWAuSlcHUKWKsQgGKjJHNSKFrMIY_B6OPoc8ch2b-Widqt6HlQMirA6r7rYbTTplJ08y08YvaHPraM3lO35G4agkIBwo9mAelXa5RZfHyU1KWYcHBUTlo14WI-3HDotrKltWMqXW0CqgiU8xMrbPMHjVnNYpknIisBxsyGgySb5pbQlpdXflwvfDWr4H2H4ynyHSSnnp_WP7JlvU2LdsZkkfNMCBMJTTnm80phEpj-k11FFdVmORXK9y9KIs_BO7Opq2UF7sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو ایتا و روبیکا با انتشار این فیلم نوشتن سامانه پدافند لیزری جدید اومده و همه موشکا و پهپادای آمریکا رو با لیزر زده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71053" target="_blank">📅 16:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71051">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=V_zEx3t502k9xVOOSuj2GWNnE3fjOifl3TBNW5D2AZL7r3poefNesn0kga4MRfcOqfKJTosGoQhe8TKS4NaeheoUxUE0-dYAV2ZlNOvX-p7J9m13FTt8GUpx4BNa3dverd1jdjnwAJQ5fuUQt7QzA8eCYL52FOcvD-mph7AnIx7xFi7YHRcRn9glihxQLgYIayxpeijKjB86HiR3w3H87pqtia95g1-KtcgYcRhVySVUKrJGpCwTjYz206sitly2RvoA0oX5bLnjJ4UUv57Q9S2XPCdzUySt0fZVGF7v2L2J-wc-s51PF0IeNol8mdUtO0JqS0pRq8dr2SCwmU2LQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=V_zEx3t502k9xVOOSuj2GWNnE3fjOifl3TBNW5D2AZL7r3poefNesn0kga4MRfcOqfKJTosGoQhe8TKS4NaeheoUxUE0-dYAV2ZlNOvX-p7J9m13FTt8GUpx4BNa3dverd1jdjnwAJQ5fuUQt7QzA8eCYL52FOcvD-mph7AnIx7xFi7YHRcRn9glihxQLgYIayxpeijKjB86HiR3w3H87pqtia95g1-KtcgYcRhVySVUKrJGpCwTjYz206sitly2RvoA0oX5bLnjJ4UUv57Q9S2XPCdzUySt0fZVGF7v2L2J-wc-s51PF0IeNol8mdUtO0JqS0pRq8dr2SCwmU2LQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ از یه دختره که سر سفره عقد، آقای داماد رو سورپرایز کرد و گفت من مهریه نمی‌خوام و فقط 14 شاخه گل بنویسید
؛
هیچی دیگه پسره دیروز طلاقش داد و اونم با 14 شاخه گل رز طبیعی قرمز  یک جلد قرآن برگشت خونه باباش...
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71051" target="_blank">📅 16:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71049">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01429c982d.mp4?token=t6MgLx7837Qsu3LrYFktbZRkdHvRXiWIg9KJJmKhWt6IDmgdoIWYhU9WE2vXtjosJJz_uYcTfqraWY3D1eO3jOJSo7fmu6tRzO_TeGBNmYQVshRgi8k-5ngfcbWAD3OXpV116frkx11lu1LY_M0YnhAawVTH_h70d5grkse5ymT7KLLYuLvtYmme38oZzrfCXZY4tw7mjW4k4f5d4pHEfN3GIrtE3TTF4SZ_0_rK4p69axJqWCIhHYygvnLTwfdc-AXSbX0rDPYQsRbkxnzV3_iEqLcpmkqQK8QgDXtzWBAHVKBnjbD5sHf4EMSUt2akgDhGITREoRjJwqM8seV4eg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01429c982d.mp4?token=t6MgLx7837Qsu3LrYFktbZRkdHvRXiWIg9KJJmKhWt6IDmgdoIWYhU9WE2vXtjosJJz_uYcTfqraWY3D1eO3jOJSo7fmu6tRzO_TeGBNmYQVshRgi8k-5ngfcbWAD3OXpV116frkx11lu1LY_M0YnhAawVTH_h70d5grkse5ymT7KLLYuLvtYmme38oZzrfCXZY4tw7mjW4k4f5d4pHEfN3GIrtE3TTF4SZ_0_rK4p69axJqWCIhHYygvnLTwfdc-AXSbX0rDPYQsRbkxnzV3_iEqLcpmkqQK8QgDXtzWBAHVKBnjbD5sHf4EMSUt2akgDhGITREoRjJwqM8seV4eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز، اولین ایونت مد و فشن توی تبریز برگزار شد و حسابی غوغا کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71049" target="_blank">📅 15:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71048">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=d_hSHx4fz9GUFpLoxIS2moGdT5sfCCA5ICwrvcG3sVOLvflgRH3z-m2DF-g_nXVKCYoen6EaUd9kXVaQxzIMftFMu7Rs40nXMF1mIfn_hCGA-2uj-5DPqqNKDejvL2fR9unbJqivpPHAIIeDUt3BdkTOfYcfAAMJ2bzxqkXuAVMih0ep-Q8kM5Df1DcIjDv1T4S2_3yEKkrRW6h1a3wNEivRrXq-7RptoA2EjwhhUjU8HQW3MfWel_HvpK7OrV99ctERp-4T9N-l8RLcc_RI2GpFOXu3zJAQMF4YaJFMgYrdSdx7wKpceBga7Vi8zsoAzCmOlzpqaMsFelv5GpAJiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=d_hSHx4fz9GUFpLoxIS2moGdT5sfCCA5ICwrvcG3sVOLvflgRH3z-m2DF-g_nXVKCYoen6EaUd9kXVaQxzIMftFMu7Rs40nXMF1mIfn_hCGA-2uj-5DPqqNKDejvL2fR9unbJqivpPHAIIeDUt3BdkTOfYcfAAMJ2bzxqkXuAVMih0ep-Q8kM5Df1DcIjDv1T4S2_3yEKkrRW6h1a3wNEivRrXq-7RptoA2EjwhhUjU8HQW3MfWel_HvpK7OrV99ctERp-4T9N-l8RLcc_RI2GpFOXu3zJAQMF4YaJFMgYrdSdx7wKpceBga7Vi8zsoAzCmOlzpqaMsFelv5GpAJiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ در مورد پسرای زیر ۳۵ سال که موهاشون سفید شده، در حال وایرال شدنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71048" target="_blank">📅 15:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71047">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK8jPnd21VGkWv9HToIAOUiZizKDndtxTLOz9MTZoa3OWnOeC3UsLOptuf3yw-8WLK5HlywanqHqCCAlwn_07YJ8JdYmmG0ffs3TMZ9o9BuPmSJSpEzCbtrc7TiLz0mrSYgGLvXkhOxAeQcs11HZ5KPJcU7j1_Q_J8aC_LMnmGFzeRKPpMWMA_rgcr5hGuHLgCBTc1Qu_qnuHDjFoP7cCJh1vX7PICmafSSJJ3d7zzUMkeJYmHKO4EE9kIIUL3MjmstEe4zCO36g1-ClMc55Pn-rlakf-8Tq4T62K7T343tBEt5k67Bw15XVyMPEGBgJ4ur-eA-QQ5Ge1QvT5o8O2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
خبرگزاری میزان وابسته به قوه قضاییه، روز پنجشنبه ۱۲ شهریور ماه اعلام کرد حکم پرونده صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، در دیوان عالی کشور تایید شده و او به ۱۲ سال و ۶ ماه و یک روز حبس تعزیری، مصادره کلیه اموال منقول و غیرمنقول و محرومیت از اشتغال به شغل کافه‌داری محکوم شده است.
مرکز رسانه قوه قضاییه این پرونده را مرتبط با اعتراضات سراسری ۱۸ و ۱۹ دی سال گذشته دانسته و مدعی شده است که متهم در «تحریک اعتراضات و ورود خسارت به اماکن و اموال عمومی در استان قم» نقش داشته است.
صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، کارآفرین و نیکوکار ایرانی است. محمدعلی و صادق ساعدی‌نیا در جریان انقلاب ملی ایرانیان در دی ماه گذشته دستگیر و اموال هزاران میلیاردی آنان مصادره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71047" target="_blank">📅 14:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71046">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:  اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت. ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71046" target="_blank">📅 13:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71045">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=fxoxXNsabstYlG15a48kW42aFANM70ZlZPaDNFgwLEbZlUN5vL1OQN7RCqwFcEB3VErqPYsdjRxjfGAZsLKdIi-ealkGwF2KwxglsKcDcxs62g_q3AvJuRHTNwogpr4Cr2llhFhI-4EMaE_HPBIhMjt-fHwgnbqjSbVB9DOkX6rdZ1lIM_IzxsEBOiE_MFxd79B2Yz7hSVlJsY9SaS7csvI54CDLYursPHGRmVNpJn9MmVDRG2qwjKNCtTH405693nTAHava4h1MTjqzGOVN8Viktb1k0X11U_4cfgGiPs3jU5mhKgEF3wNQUCTCj7qI0EuX7HRr8OYPXDiUPQLetg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=fxoxXNsabstYlG15a48kW42aFANM70ZlZPaDNFgwLEbZlUN5vL1OQN7RCqwFcEB3VErqPYsdjRxjfGAZsLKdIi-ealkGwF2KwxglsKcDcxs62g_q3AvJuRHTNwogpr4Cr2llhFhI-4EMaE_HPBIhMjt-fHwgnbqjSbVB9DOkX6rdZ1lIM_IzxsEBOiE_MFxd79B2Yz7hSVlJsY9SaS7csvI54CDLYursPHGRmVNpJn9MmVDRG2qwjKNCtTH405693nTAHava4h1MTjqzGOVN8Viktb1k0X11U_4cfgGiPs3jU5mhKgEF3wNQUCTCj7qI0EuX7HRr8OYPXDiUPQLetg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت.
ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران را به اعماق دوران حجر و تاریکی بازخواهیم گرداند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71045" target="_blank">📅 13:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71044">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=BvNDXMlt6SQNYPRnqARfvj74WgJsOzHGYSWceQt0G8wM4YQ55Lh3edH1UPEECjTq2ko5P4EJ-X-q37rYr_anGEjzyIBSdbC6YMlaZnSV1JCNw23W3yqKlbXLiDrlJlzvUez692695qfgllxR8IqeBqQV33qoXuE1l8lKe7KCv4M-5OeQSkrJUNQofDC5MNWVqnrwF2JMTiIPB74itdrAKug_4IYrkiQpitbsxNR01WfLxft3eXhc5NyKgoGnqK1-3aE9z1dG40IBtUIajB_UV_XoNk3sF4ERfzXJUFMo3GB4GzafXSUORyAj521VhS3-yiAPGaZhgN9zvlq_1cdf7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=BvNDXMlt6SQNYPRnqARfvj74WgJsOzHGYSWceQt0G8wM4YQ55Lh3edH1UPEECjTq2ko5P4EJ-X-q37rYr_anGEjzyIBSdbC6YMlaZnSV1JCNw23W3yqKlbXLiDrlJlzvUez692695qfgllxR8IqeBqQV33qoXuE1l8lKe7KCv4M-5OeQSkrJUNQofDC5MNWVqnrwF2JMTiIPB74itdrAKug_4IYrkiQpitbsxNR01WfLxft3eXhc5NyKgoGnqK1-3aE9z1dG40IBtUIajB_UV_XoNk3sF4ERfzXJUFMo3GB4GzafXSUORyAj521VhS3-yiAPGaZhgN9zvlq_1cdf7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
جنگنده میگ-۲۹ام‌یو۱ اوکراینی یک موشک اس۸۰۰۰ «باندرول» روسی را در ارتفاع پایین با یک موشک آر-۶۰ منهدم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71044" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71043">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162568634d.mp4?token=mxfDgpRDjbsEBIXsyl1zPrm_Zoqv7JWnlx_xvzgv1XV336ZTJ0J9meENXmi6IG4-ytn_JQUGeoLEKP3-9A9o0kMO9GyVBVxqzU9WLtJZCfI5ee7RGHguzg5GHLG2Dnni3eNK39SZJJMwRI8fVaqtphYq6AY8rAkozT3WdOL3PRsUYpNcrKNjND6a8ICb3abNqAwJRjVPJGf2ykr-JdrXtfPttbWe9Njml_YV_k-Bjo08issAXdEuBXGz5BxB1vPq1IeE8MJvIB6j6N1H_EiS-S38KdcPpjeKoj28cf0tyRW2lSD6nuQdzkEXjHFKbhs7hElUY4H2bPjDZ9XOVfLtWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162568634d.mp4?token=mxfDgpRDjbsEBIXsyl1zPrm_Zoqv7JWnlx_xvzgv1XV336ZTJ0J9meENXmi6IG4-ytn_JQUGeoLEKP3-9A9o0kMO9GyVBVxqzU9WLtJZCfI5ee7RGHguzg5GHLG2Dnni3eNK39SZJJMwRI8fVaqtphYq6AY8rAkozT3WdOL3PRsUYpNcrKNjND6a8ICb3abNqAwJRjVPJGf2ykr-JdrXtfPttbWe9Njml_YV_k-Bjo08issAXdEuBXGz5BxB1vPq1IeE8MJvIB6j6N1H_EiS-S38KdcPpjeKoj28cf0tyRW2lSD6nuQdzkEXjHFKbhs7hElUY4H2bPjDZ9XOVfLtWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
روابط عمومی ارتش:
در ادامه سلسله عملیات‌های صاعقه و در مرحله سی و یکم،  در انتقام خون پاک مردم بی‌گناه و دلاورمردان نیروهای مسلح، بامداد امروز، ارتش جمهوری اسلامی ایران، «سامانه‌های ارتباطات ماهواره‌ای»، «انبارهای تجهیزات» و «آشیانه هواپیماهای جنگنده» ارتش تروریستی آمریکا در پایگاه احمد الجابر کویت را با موشک‌ها‌ و پهپادهای انهدامی، مورد اصابت قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71043" target="_blank">📅 13:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71042">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71042" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71041">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgY7L1xnNgrXnwokp-4ApVgCC58SgBUKlTcMtRATl8YMqq39Jx3xrGD0JuyxXitRVeIPVVWakwo0ZiwQ8whAEFFvalGlNAS_mDP72ZeT2o00bKmKaMv-qjteaZK5YBPwWF3jlBUf9TDV27x27SvHqCzmQQfB2TFUB0rtF7Pt5YSrztES247ox_3Y9l4EIh0x4u0mNAcKUesUrG6QBPI48IK_JNny1hSaaSPqj6vIw9mP0SsVf5zl_d3uCrocjBRSFGU-PHlgZDZUGdgAXljkWEiRvAzGZDV7BbSdsoD9a0PkDsNElb7k4kw6cLA0ulLvpccpB3-9G1kdydhMhMnPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71041" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71040">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=AtEW3vHz8tBibTB4nhdI83DyU5FZb1X_sVrYzwyfXsh9YWt-ZLk5SAxHA3-WkiCXtxf-jW8ChTEqaO5cAJXev5xmmslNhuyLohoU0VIIy7o3yN2puLJvHYcvDvVBTi9xK_s8_cTixxBMk3uczqtGEN4Qbu3e96s2egtEPrdB10wqe6lO_kGg9mx4wjst4qnxCkW0j7XRjZU1OwXmFyFmB0Qv28L6vl2Sdd8fOgJO4CZ6oasyGQnHYwiMt__I-Q9hJjlBfWpGNxff29MQwTotltAMu12Vnn85-mEEu4VY8uC9g0ERkR3YzCYT8yOfaC1sQh9KqzjNQn9HHUF-jzHFqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=AtEW3vHz8tBibTB4nhdI83DyU5FZb1X_sVrYzwyfXsh9YWt-ZLk5SAxHA3-WkiCXtxf-jW8ChTEqaO5cAJXev5xmmslNhuyLohoU0VIIy7o3yN2puLJvHYcvDvVBTi9xK_s8_cTixxBMk3uczqtGEN4Qbu3e96s2egtEPrdB10wqe6lO_kGg9mx4wjst4qnxCkW0j7XRjZU1OwXmFyFmB0Qv28L6vl2Sdd8fOgJO4CZ6oasyGQnHYwiMt__I-Q9hJjlBfWpGNxff29MQwTotltAMu12Vnn85-mEEu4VY8uC9g0ERkR3YzCYT8yOfaC1sQh9KqzjNQn9HHUF-jzHFqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تو میدون تایمز نیویورکِ آمریکا، یه خانمِ چاقو بدست بعد از اینکه یه مرد و یه زن رو از ناحیه شکم زخمی کرد، بعد از اخطارِ پلیس‌ها به سمتشون حمله‌ور شد و به این شکل بهش شلیک کردن و کشتنش.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71040" target="_blank">📅 12:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71039">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=fFNrpk3GCNe-I_s5m_dhQ9xYKfd1zlvx86rqPEVTT6CzawTT7KwMcJ1bu2FNfIsvAZkbzP71ovFz0XG05-VxXMv7z9LqLsOSITSp3NJdHrCZF1GdHOtSGeA3qACcqAwZLZsAIs5N7Kk5IDv_D55_Zz1eUdO-Uxww9ZW16JciL3hHIIlcK_fz9XC4m0YVThjg_7TRJOYJiHqdRT9UVQnTFvLtNs0VnXQo5-BypedwxPCmbQcrCa2kQpxyhx2rYjodguuNWMAvhKj3tRhfw3h5cwOlw6coxZFLekJZ2HJ6KPd6Aq0ywldFVX_c6RJMABdBDRTpzAxUHtffha9Kp269hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=fFNrpk3GCNe-I_s5m_dhQ9xYKfd1zlvx86rqPEVTT6CzawTT7KwMcJ1bu2FNfIsvAZkbzP71ovFz0XG05-VxXMv7z9LqLsOSITSp3NJdHrCZF1GdHOtSGeA3qACcqAwZLZsAIs5N7Kk5IDv_D55_Zz1eUdO-Uxww9ZW16JciL3hHIIlcK_fz9XC4m0YVThjg_7TRJOYJiHqdRT9UVQnTFvLtNs0VnXQo5-BypedwxPCmbQcrCa2kQpxyhx2rYjodguuNWMAvhKj3tRhfw3h5cwOlw6coxZFLekJZ2HJ6KPd6Aq0ywldFVX_c6RJMABdBDRTpzAxUHtffha9Kp269hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سایپا تو ماشینی جدیدی که زده ماشین با اینکه راه نمیره ولی براش کیلومتر حساب میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71039" target="_blank">📅 12:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71038">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmUUwGIh-cEBZr7V9xb1kRKS--DPaWwTZnx9dc5sThgNYEwrhUtEPIroFPSEnfJZGJYaNXPzPruLkthAWnbHzP_zpsLYufYgqYs2N0zC8y-TbwQLBkar0XFQtqXyisRuh5gR8P_ukMAKRn4PHjMLt-M2S09g7o4gysYdiV6ZifqwVls2W0ZvZPGkTAAEadHR9uRoAPNJKYQdxrRj_t3V6yhpVnAMq95boLxULL1XH1jpHlIvQpi8FAOfa27Jb-6W9AtS9kFYYBBsgaW7bIlb9i_2qyerVCEskGMj3vkiNxGNcph5IpjMra_T1Ucu312jLi-FLyt3OPjHzWtEhWUQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس:استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته در ساردینیا با شیخ طحنون بن زاید آل نهیان، مشاور امنیت ملی امارات متحده عربی، درباره ایران دیدار و گفتگو کرد.
این دو مقام درباره گام‌های احتمالی آتی بحث و تبادل نظر کردند؛ چرا که دولت ترامپ در پی بازگشایی تنگه هرمز و هم‌زمان افزایش فشار اقتصادی بر تهران است.
امارات نقش کلیدی در تلاش‌های تحت رهبری آمریکا برای عبور نفت‌کش‌ها از این تنگه ایفا کرده و در راهبرد تحریمی واشنگتن، کشوری مهم محسوب می‌شود.
مقامات اماراتی به دولت آمریکا اعلام کرده‌اند که هرگونه کارزار مؤثر فشار اقتصادی باید شامل تمامی کشورهای عمده‌ای باشد که همچنان به تجارت با ایران ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71038" target="_blank">📅 11:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71037">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به بندر سوچی در روسیه حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71037" target="_blank">📅 10:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71036">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef77017317.mp4?token=DOZMs76zVXyNsnHMJJ7qiXxiUjVnE4ONDyrjbfTr9-CgqpIhEYOpCO8oB-PcpMTbzcoy6aWxPQBNh9bWkBvx-QY4E-ZDBAzBI5K3AwX5Be43r0Z2h3DpcZKXkDjZNFg7NIlhoNssRJtTt3Z3xDLTWLAQLTDzzbsge3ymtyfU_tHjBNLOwakI3HEFnq9NZgQ4zW-3GPb3cjk3condTLknICI44kpnp-rTBkXzDqp6L5H8k5mnNHKB4c2aGfO6JX6mKzdAoHzed1fNJ39_n1xHBPxQma4QHpDln9D0cWiS5Z0dvwwuxyIAvMm9RLGMyYIo07Relbiptec8BUeaTnhtIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef77017317.mp4?token=DOZMs76zVXyNsnHMJJ7qiXxiUjVnE4ONDyrjbfTr9-CgqpIhEYOpCO8oB-PcpMTbzcoy6aWxPQBNh9bWkBvx-QY4E-ZDBAzBI5K3AwX5Be43r0Z2h3DpcZKXkDjZNFg7NIlhoNssRJtTt3Z3xDLTWLAQLTDzzbsge3ymtyfU_tHjBNLOwakI3HEFnq9NZgQ4zW-3GPb3cjk3condTLknICI44kpnp-rTBkXzDqp6L5H8k5mnNHKB4c2aGfO6JX6mKzdAoHzed1fNJ39_n1xHBPxQma4QHpDln9D0cWiS5Z0dvwwuxyIAvMm9RLGMyYIo07Relbiptec8BUeaTnhtIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی وایرال شده از پسری که چالش گرفت که تو خیابونای شهر از مردم درخواست پول کنه(نفری ۱۰۰تومن) و اکثرا قبول کردن و در آخر هم پولی که جمع شد رو رفت به نیازمندا کمک کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71036" target="_blank">📅 10:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71035">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=VEtU1PO39ER6mWLx0eYczs-RuHqCBGMpeJ136MCXzHZAa4LKZE0eluxvJyUNMMPzFGgCBkKD7a92__zerIQzSYOvW_1TV-H3_Yci0mbykcNctm7NLFGCcMHuEf2sBjZa6UX_A5q0k8iiHOK14h3vazULdL546eMFUHkTCFzd2X_El7h3z-5dG3zY2Bt3rdXgfqa_2qZp6dC3LZ16ipBZhPmaPO5pTdm3r_DnYOY5FOuqIFzH0NfTdQ_Q07MfravpWKcOLDPnu8T9pfgO14bH3-Ay4vhxeAoYcp2U2ph8KB_JTLRypUrm0DyFgB31ZN7E9ECBEM3hUk2hopoUDvpMlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=VEtU1PO39ER6mWLx0eYczs-RuHqCBGMpeJ136MCXzHZAa4LKZE0eluxvJyUNMMPzFGgCBkKD7a92__zerIQzSYOvW_1TV-H3_Yci0mbykcNctm7NLFGCcMHuEf2sBjZa6UX_A5q0k8iiHOK14h3vazULdL546eMFUHkTCFzd2X_El7h3z-5dG3zY2Bt3rdXgfqa_2qZp6dC3LZ16ipBZhPmaPO5pTdm3r_DnYOY5FOuqIFzH0NfTdQ_Q07MfravpWKcOLDPnu8T9pfgO14bH3-Ay4vhxeAoYcp2U2ph8KB_JTLRypUrm0DyFgB31ZN7E9ECBEM3hUk2hopoUDvpMlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ویدئو جدید از پرواز هواپیمای HC-130 Combat King II آمریکا در ارتفاع پایین در عمق کشور به دنبال خلبان آمریکایی جنگنده F-15E
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71035" target="_blank">📅 10:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71034">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=HGZ4EQnidUa-IPRaosj18KkrQmR0RwwGDdK8k2o6A7-OMjbRypiXVdVwtZsEB6oA-LLlUgaRyy07oDqstfqkKimdt_FqlJd2lDXXjliNQ7_4szxVk8jDWvnaH2XueuPkTRjLeSPqVZF_QgQGinkGlLjm8rJA6OQ5WgRX24fTmOtwQAdnhuLENmfp3nnJG-Kz7on2RCQ65k765G6gPgJCrt5k88ttguz_KXjT-U_QmK_as6IkZuLXq9iVaQ27Laut9QSoHREkv3QQOgC-MhLXB3sjCcMXLler1OmxjD9za8NmFbf9vhdyz2jQc5z5umCsnouWs3riAs7HKXK5tfyiVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=HGZ4EQnidUa-IPRaosj18KkrQmR0RwwGDdK8k2o6A7-OMjbRypiXVdVwtZsEB6oA-LLlUgaRyy07oDqstfqkKimdt_FqlJd2lDXXjliNQ7_4szxVk8jDWvnaH2XueuPkTRjLeSPqVZF_QgQGinkGlLjm8rJA6OQ5WgRX24fTmOtwQAdnhuLENmfp3nnJG-Kz7on2RCQ65k765G6gPgJCrt5k88ttguz_KXjT-U_QmK_as6IkZuLXq9iVaQ27Laut9QSoHREkv3QQOgC-MhLXB3sjCcMXLler1OmxjD9za8NmFbf9vhdyz2jQc5z5umCsnouWs3riAs7HKXK5tfyiVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تو یه فروشگاه تکنولوژی تو روسیه، یه ربات بعد از اینکه مشتری هلش داد، شروع به دعوا با مشتری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71034" target="_blank">📅 09:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71033">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=MX7Bc0S-LybSu5ey1II6YbM3s0IEewCPfO3qbVxOElRzh0ksPCWDZ6qsBtdTmQd6KsB5OwAyHxCqkKmRN5tmIGaKZIyrIiV5CtMbosReLN5iFa_MzUAfK-T5kY1_fDXSlmPAKJOFatpfaq5g93Ty5I9CZlFnyNf0ivKXHAOPv_XG2fURrcepdEBiIyvWW2nNWIHZatfFnQLYG5tsBxlTLYZf7MIl_HVdJiDz05doRW_0nmaVlzGt5h6Tk9t3_Ap8eDVEQZ-8QU2tczfPLUGBjRPP9nupI8_aPgrXPN1cZUMPTjkRBc6f1SF0-PUGwrXBe3jkofX2MjnzTexNYKfZGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=MX7Bc0S-LybSu5ey1II6YbM3s0IEewCPfO3qbVxOElRzh0ksPCWDZ6qsBtdTmQd6KsB5OwAyHxCqkKmRN5tmIGaKZIyrIiV5CtMbosReLN5iFa_MzUAfK-T5kY1_fDXSlmPAKJOFatpfaq5g93Ty5I9CZlFnyNf0ivKXHAOPv_XG2fURrcepdEBiIyvWW2nNWIHZatfFnQLYG5tsBxlTLYZf7MIl_HVdJiDz05doRW_0nmaVlzGt5h6Tk9t3_Ap8eDVEQZ-8QU2tczfPLUGBjRPP9nupI8_aPgrXPN1cZUMPTjkRBc6f1SF0-PUGwrXBe3jkofX2MjnzTexNYKfZGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیح عباس حیدرزاده مداح درباره‌ی وضعیت مجتبی خامنه‌ای :
تولیت آستان قدس رضوی گفت که شب دفن رهبر؛ مجتبی خامنه ای ساعت ۱۲ شب اومد حرم برای دفن پدرش و تا ۷ صبح اونجا بوده.
وضعیت جسمانی ایشون هم عالیه، هم از لحاظ ظاهری و هم از لحاظ جسمی؛ حتی مسئولین هم پشت سر ایشون نماز خوندن.
همچنین ایشون نیم ساعت کنار قبر پدرش دو زانو نشسته بودن و گریه میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71033" target="_blank">📅 09:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71032">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71032" target="_blank">📅 01:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71031">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CARDswdKciFnbrSgRkk9cF7E_vJ0mMr4X11yC8V093ub7t9wERCvysLu_mY4OVIi3t9VeAjyGtox-NeBPJhPiTBBzidba2FZH-rZBYA0ae9IQak7gFOmofeHNxoUL7wpX8k-VeaYkpRFNtruIxysqPVNziyMMsNHZZJD1Dkn36NT0Yyyt2hd56lit9ieBM9Ifa9XuB6q5fNC6_0YfmqlJf8AblP9v6xqHecO0GrbqTvmjivrdhbdHSvCztTVb6SwBiiNiN6ees4thZ0cVmLvCoRX-LRID8aGettxmsWCaUOqjDMa-6ztXLpAvHD9Eslr1e1oIU4NT8ffL2mN55e-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71031" target="_blank">📅 01:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71030">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
⭕️
فوووووری/ همین الان با شروع مجدد جنگ دلار و ارز منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+S5Mn2k3LOf0wNjJk
https://t.me/+S5Mn2k3LOf0wNjJk
فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71030" target="_blank">📅 00:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71029">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=auE2UyBDwpVwTqnku4lsIUdUir-eQahzmSgAEu_23kYTidbRm-FHNL_LNj3H12sR2ea17sW1c8k2oTw8ruuu9rfdZ8AlqU-2IVecxmtiVBlEtpkGsBCAssFqHAhLbZAXdzpieNQz-QmM_AS1jHucg9tuLqDHY0ESqvL5XXIEnLQ403v0nNvy0qfLL22p-YaY3GuWMCBiHhPNJrGm89Qk4WqY9EnEBPCAN9rlPNLpzGDvo329sY6tsJKGS3RijqzxfKHgCD8ECrZBslbXvDonQakeX7L1P8OnqsAs1PH2-WvkPSowA3-V0Ru7sJPOohLGrv7JlFCroj-NE2N-ZT40AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=auE2UyBDwpVwTqnku4lsIUdUir-eQahzmSgAEu_23kYTidbRm-FHNL_LNj3H12sR2ea17sW1c8k2oTw8ruuu9rfdZ8AlqU-2IVecxmtiVBlEtpkGsBCAssFqHAhLbZAXdzpieNQz-QmM_AS1jHucg9tuLqDHY0ESqvL5XXIEnLQ403v0nNvy0qfLL22p-YaY3GuWMCBiHhPNJrGm89Qk4WqY9EnEBPCAN9rlPNLpzGDvo329sY6tsJKGS3RijqzxfKHgCD8ECrZBslbXvDonQakeX7L1P8OnqsAs1PH2-WvkPSowA3-V0Ru7sJPOohLGrv7JlFCroj-NE2N-ZT40AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇹🇭
ناو آبراهام لینکلن تو پاتایا - تایلند پهلو گرفت و ملوانان و اعضای این ناو برای یه استراحت  کوتاه مدت پیاده شدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/71029" target="_blank">📅 23:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71028">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=oNgfYj5XD0yCjH6XhdjuMLdSY2InIk3LmZTfr-_M8XGIsj5MOiazGj4ydjhVloK_NypBTgtMdkVhT6P7M5QWnLz-U-fBKRfH65IGdPqddd-BahgvfPlcmS4e6Lilxs6EGJDZPQTbDW297XRA63Nw7Tn7-dwO06yIG2JIvjuNkWgg-T8abe-CIjGIvrG1M9QCMqbfBTP7cZoAlqeoPGYQQgH-3RbsBKok07VdkIGdan4eBoxMjIR3qDjRDlVLIebQVueQDIdVyJVqUzLbnm7R4AsvZTrc5cQoSfhd59Rhem1zQWfo9ZyDf0OGkFl57joUm2x5Sd8vu9zVzkTktzd0bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=oNgfYj5XD0yCjH6XhdjuMLdSY2InIk3LmZTfr-_M8XGIsj5MOiazGj4ydjhVloK_NypBTgtMdkVhT6P7M5QWnLz-U-fBKRfH65IGdPqddd-BahgvfPlcmS4e6Lilxs6EGJDZPQTbDW297XRA63Nw7Tn7-dwO06yIG2JIvjuNkWgg-T8abe-CIjGIvrG1M9QCMqbfBTP7cZoAlqeoPGYQQgH-3RbsBKok07VdkIGdan4eBoxMjIR3qDjRDlVLIebQVueQDIdVyJVqUzLbnm7R4AsvZTrc5cQoSfhd59Rhem1zQWfo9ZyDf0OGkFl57joUm2x5Sd8vu9zVzkTktzd0bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
ملت ما با قدرت جلوشون ایستاد و اگه بخوان این مسیر رو ادامه بدن، بازم با قدرت مقابلشون می‌ایسته.
ما تو اون تفاهم‌نامه چیزی بیشتر از حقوق کشورمون نخواستیم و الان هم فقط دنبال همون حقوق هستیم.
ما همچنان به تفاهم‌نامه‌ای که امضا کردیم پایبندیم. اگه آمریکا هم به همون تفاهم‌نامه برگرده، ما هم طبق همون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71028" target="_blank">📅 23:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71027">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=iteVzSqF1YBsfjuLRk_POTysdeVRJcy28zjathrgOPPyhzO22YhKkV-n_DQvVWH5MUB9fQXolr2hoFkBWC7qCpwdtjRgZVmtO1Byct6_5UweqIVnnPe4cCPDbMeyLtd8fFs4ckne_cMJblmwLq0TvfqdtvWOaBZ4pqTKKXz5gvMH3_pXuqVKWLb431S54SfIO3WCaDj1kBZYSgweSk_EtH2chKSKx-PJIvW8hLKDNGXVqK1k_pZf6LNG9i8BehU0kbr_eunzNRpOJidQrS2EnGiT6zerJEPTOKSm8pEcu9ptj5CqmYgfRxIMlMnou2yCd8vpdT3Byc0KTJFgD-uzqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=iteVzSqF1YBsfjuLRk_POTysdeVRJcy28zjathrgOPPyhzO22YhKkV-n_DQvVWH5MUB9fQXolr2hoFkBWC7qCpwdtjRgZVmtO1Byct6_5UweqIVnnPe4cCPDbMeyLtd8fFs4ckne_cMJblmwLq0TvfqdtvWOaBZ4pqTKKXz5gvMH3_pXuqVKWLb431S54SfIO3WCaDj1kBZYSgweSk_EtH2chKSKx-PJIvW8hLKDNGXVqK1k_pZf6LNG9i8BehU0kbr_eunzNRpOJidQrS2EnGiT6zerJEPTOKSm8pEcu9ptj5CqmYgfRxIMlMnou2yCd8vpdT3Byc0KTJFgD-uzqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره انتخابات:
من تحت تأثیر انتخابات نیستم. خودم نامزد انتخابات نیستم؛ حزب من در انتخابات حضور دارد.
به گمانم حزبم به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران به سلاح هسته‌ای دست یابد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71027" target="_blank">📅 22:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71026">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=R6_KwVx3lZQ_4bVwK_D68u0HU2OYZpMTcdKBgXohYAGLfe9TpGOiE8ZRpU9K6Rad8bQJ5UTNg7yHW7JMEFmGPyE2EmnkuZbnx1VOzkiWOXISJRNSsWXWVSLO1xAXlVZwkSoMhER4S_9FkHoLNCK2KoCafTuWMIMSi8BO6OC9AR4O3-9uw81GZg5x1jP8iWEmhu4FeN3uz0qGyfkmn_HaZ82edcN7fxIkBXlW8EeC7bCxOw6Pl2baSmkWIY3UhcyYJ3XSqEMM9g4LPA892xGH9rPx09dEAXOdxElSO81BjEHZMEM920CSTyfTdMtCt2D7tNWAPvXy2HnRuBtbd6Hiew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=R6_KwVx3lZQ_4bVwK_D68u0HU2OYZpMTcdKBgXohYAGLfe9TpGOiE8ZRpU9K6Rad8bQJ5UTNg7yHW7JMEFmGPyE2EmnkuZbnx1VOzkiWOXISJRNSsWXWVSLO1xAXlVZwkSoMhER4S_9FkHoLNCK2KoCafTuWMIMSi8BO6OC9AR4O3-9uw81GZg5x1jP8iWEmhu4FeN3uz0qGyfkmn_HaZ82edcN7fxIkBXlW8EeC7bCxOw6Pl2baSmkWIY3UhcyYJ3XSqEMM9g4LPA892xGH9rPx09dEAXOdxElSO81BjEHZMEM920CSTyfTdMtCt2D7tNWAPvXy2HnRuBtbd6Hiew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
دیشب حمله بسیار سنگینی صورت گرفت و ما آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71026" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71025">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=NTVAZ3fYx-6yuaeoMOWJYcz_jlgzZQrQ5_JFzHuztfDB2nJ-8DZ3hdQ8CsdTHK5n_ktIe3SPttD1UX6yh_HdM-0Ip6nXHw_YXRuCrhSOMqklcrs2Gvc3lPMOdaRlaLaKovmmVdVV4yw5io_VhFHlcVPX76kty5cxuDc16OePZI7XDLzc4KzAl5iFGr9ccMKM17ylx6DeiuXfx12iuoH_5pVTAohGgM0dPDy_osxQEeNkfXT6o59BVgGNN578Puw1ELQtEIFzv4LvzME460xJbcnoyUXogE5_z8Dvi7XhYwxRvWe_SWbrL3uEB30nTsJ2oNEvzVvuc8xk-Dd5YZVdSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=NTVAZ3fYx-6yuaeoMOWJYcz_jlgzZQrQ5_JFzHuztfDB2nJ-8DZ3hdQ8CsdTHK5n_ktIe3SPttD1UX6yh_HdM-0Ip6nXHw_YXRuCrhSOMqklcrs2Gvc3lPMOdaRlaLaKovmmVdVV4yw5io_VhFHlcVPX76kty5cxuDc16OePZI7XDLzc4KzAl5iFGr9ccMKM17ylx6DeiuXfx12iuoH_5pVTAohGgM0dPDy_osxQEeNkfXT6o59BVgGNN578Puw1ELQtEIFzv4LvzME460xJbcnoyUXogE5_z8Dvi7XhYwxRvWe_SWbrL3uEB30nTsJ2oNEvzVvuc8xk-Dd5YZVdSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
یک ضربه کوچک بود، اما دیشب ضربه بسیار سختی به آن‌ها زدیم.
ما تمام تجهیزات جدیدی را که سعی داشتند در امتداد تنگه هرمز مستقر کنند، از بین بردیم؛ تجهیزاتی که برخی جنبه تدافعی و برخی جنبه تهاجمی داشتند.
آن‌ها تلاش می‌کردند موقعیت کشتی‌ها را رصد کنند — چون همان‌طور که می‌دانید، قادر به دیدن کشتی‌ها نیستند؛
ما تعداد زیادی از کشتی‌هایشان را نابود کرده‌ایم
آن‌ها نمی‌توانند کشتی‌ها را ببینند چون راداری در اختیار ندارند؛ چرا که ما رادارهایشان را منهدم کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71025" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71024">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=ZAdW5JFtQ650RKHlvON0DuQzFK09jjapJyo22EfUgX0zv71wqZiWxp1t3z3l0UH9igzKzqGvYj2JNe89oieGeKBWurIU-V3il4LbrYenF8g_ukOIyVi61mdqEtRsdFk_4CZf6LY_tN3u-0xdHGQmKNEJ7ZWY2jgIUW1LeT8juH4pvd4K_5U-k-MqQJCnJlrkl8NPCgDYZI_KTNQ62tO4lQWkX_koocQde4GwVW5rViAu8gHEtjgR5YqzwniKmN7x-dNXt1glX-Fk033bAm-VIKsw65oagrd0aHy2BHdMtTHmQsZr6TW4xYHxAQIBqHY6DRPh4oSQSexHREkfCteTUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=ZAdW5JFtQ650RKHlvON0DuQzFK09jjapJyo22EfUgX0zv71wqZiWxp1t3z3l0UH9igzKzqGvYj2JNe89oieGeKBWurIU-V3il4LbrYenF8g_ukOIyVi61mdqEtRsdFk_4CZf6LY_tN3u-0xdHGQmKNEJ7ZWY2jgIUW1LeT8juH4pvd4K_5U-k-MqQJCnJlrkl8NPCgDYZI_KTNQ62tO4lQWkX_koocQde4GwVW5rViAu8gHEtjgR5YqzwniKmN7x-dNXt1glX-Fk033bAm-VIKsw65oagrd0aHy2BHdMtTHmQsZr6TW4xYHxAQIBqHY6DRPh4oSQSexHREkfCteTUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ما هر کاری که آن‌ها انجام می‌دهند را می‌بینیم.
آن‌ها حتی نمی‌توانند به دستشویی بروند بدون اینکه ما متوجه شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71024" target="_blank">📅 21:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71023">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/504db2064f.mp4?token=nx1PasgjmrOjqu2ANVxkcYRhtE9pLe_lmx7Ro_y6S6K351p9ke7IU8SzXAJlktwg9-W67AL7VHmkkKdZmWk4tJN_4meppDmHJVxqC6NriLZNXbv_5LaQs0sdF4125a0gu0skyLYywa8MYdmXXpWJPyaqszPWwmFAmthOtvhTpS3JC8g-RVudmvgX89E5SQNcoFzcNq7VazUrqetu1qGguFpStKfVCPFTHTJ4c4DV3PA29LK-M4SmWpp9cpq2KaXX_A0I4sUnQyVxfPCkAnapMmVGjvfhW5tCxGXwaBSDHXYDqfEG-urJ07nf4YYi38WJDPFJkuDDuGCFawgYaSQjJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/504db2064f.mp4?token=nx1PasgjmrOjqu2ANVxkcYRhtE9pLe_lmx7Ro_y6S6K351p9ke7IU8SzXAJlktwg9-W67AL7VHmkkKdZmWk4tJN_4meppDmHJVxqC6NriLZNXbv_5LaQs0sdF4125a0gu0skyLYywa8MYdmXXpWJPyaqszPWwmFAmthOtvhTpS3JC8g-RVudmvgX89E5SQNcoFzcNq7VazUrqetu1qGguFpStKfVCPFTHTJ4c4DV3PA29LK-M4SmWpp9cpq2KaXX_A0I4sUnQyVxfPCkAnapMmVGjvfhW5tCxGXwaBSDHXYDqfEG-urJ07nf4YYi38WJDPFJkuDDuGCFawgYaSQjJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
بیشتر مردم نمی‌توانند به این شکل آدم‌های خودشان را بکشند.
بیشتر مردم سعی می‌کنند منطقی رفتار کنند، گفتگو می‌کنند و بعد شاید کار به سرنگونی بکشد.
اما در ایران، آن‌ها مردم را می‌کشند.
وقتی مردم برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند؛ درست وسط پیشانی‌شان شلیک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71023" target="_blank">📅 21:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71022">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=gUIlzPfc8Hlevk6Oo_N8_Hdrj8mZ6F6fxC9U34GVAx0oMCEP0SlQM6Hqu0PPF2L8lVhn7ngZomH8jO0C-lQ7hlGa_padl7_A3vlgdtaWTRFhLzf-ZEwh52cNIeEFgbM_wSgxcpQmgg2UyUAlO6hNXa4lW8_IuQx7JXfsUggK1eX7pw1LwUbBBqg2DOFzYoqWwEyubiWJHkeXphEyajmtDbvI4WzQmEFO_2SmO3zj4YHjxp-MwM1Rxe_zjQHkaYjLkMHEhCDC5ppLc9i-pHbXeOA0qwXhU8-qft_m6elqbSSExkkQXvpTUKdvw2bqioXMzB_O4j5iBPmWrsIeIIsQlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=gUIlzPfc8Hlevk6Oo_N8_Hdrj8mZ6F6fxC9U34GVAx0oMCEP0SlQM6Hqu0PPF2L8lVhn7ngZomH8jO0C-lQ7hlGa_padl7_A3vlgdtaWTRFhLzf-ZEwh52cNIeEFgbM_wSgxcpQmgg2UyUAlO6hNXa4lW8_IuQx7JXfsUggK1eX7pw1LwUbBBqg2DOFzYoqWwEyubiWJHkeXphEyajmtDbvI4WzQmEFO_2SmO3zj4YHjxp-MwM1Rxe_zjQHkaYjLkMHEhCDC5ppLc9i-pHbXeOA0qwXhU8-qft_m6elqbSSExkkQXvpTUKdvw2bqioXMzB_O4j5iBPmWrsIeIIsQlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
تا سه ماه پیش، پنجاه‌ودو هزار نفر از معترضان کشته شده بودند؛ می‌توانید چنین چیزی را تصور کنید؟
و حالا شنیده‌ام که احتمالاً بیست تا بیست‌وپنج هزار نفر دیگر هم به این آمار اضافه شده است؛
یعنی شمار معترضان کشته‌شده به حدود شصت‌وپنج هزار نفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71022" target="_blank">📅 21:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71021">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=aU8UTpmPMEZyuxQCndvEmL7fAd0XYibIBa6wMZ8tSXci2flxyv2MXlELdUGv79mkrD7eYkCKybsTm16tUteeGN1vaYX4brHlUsMW-7ELvJqXNjb6X7uRf3Ro2FRNwgNc24oiGaoaQfaYP2k0QnX1cOXdrrnbMto2Dimy0ra672wf18YskWL7vY8EMIimaAVesszEXsFELVU3PKYPYA0VznOLM9yWU-t6XR3cZ_eiE_Cb5b9RJCO0_Z70wQbELGeo6lSwcE_IJrmdnxCUhcsi4QZ3nQPY1fA9yExhBvm9sQzassK1pAl2cI9wtOLcnzob1Xz5P2kAWybnIaqOPwIVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=aU8UTpmPMEZyuxQCndvEmL7fAd0XYibIBa6wMZ8tSXci2flxyv2MXlELdUGv79mkrD7eYkCKybsTm16tUteeGN1vaYX4brHlUsMW-7ELvJqXNjb6X7uRf3Ro2FRNwgNc24oiGaoaQfaYP2k0QnX1cOXdrrnbMto2Dimy0ra672wf18YskWL7vY8EMIimaAVesszEXsFELVU3PKYPYA0VznOLM9yWU-t6XR3cZ_eiE_Cb5b9RJCO0_Z70wQbELGeo6lSwcE_IJrmdnxCUhcsi4QZ3nQPY1fA9yExhBvm9sQzassK1pAl2cI9wtOLcnzob1Xz5P2kAWybnIaqOPwIVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما امروز در «تروث سوشال» (Truth Social) نوشتید: «مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟» خب... اگر... اگر این چیزی است که شما می‌خواهید، آیا سیا (CIA) را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟
⏺
🇺🇸
ترامپ:
خب، پیتر، من نمی‌خواهم چنین چیزی به شما بگویم. خیلی دوست دارم این را به شما بگویم، اما... اما گفتنش مناسب نیست.
ولی... منظورم این است که من وضعیت دشوار آن‌ها را درک می‌کنم؛ آن‌ها هدف شلیک گلوله قرار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71021" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71020">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):   گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.   @News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71020" target="_blank">📅 21:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71019">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=X0CnoflQ9XDemwr4_bBjKYEGUMTzeq9257zPOd2un-PFR_JVYPFogBQyLOU83gwC4-5rwBW-H4xsS076Coaq6Ytz5G6b9hcH5XE231-eyxLFY9t20Qrh13u9mbXGKpL2i0iduoiiKR3W8A5FAR6SlAofyfP8iwcU5cbBG-cryDumOzWwH3Dc3mYJA38GPY-BvDpvtRkmF2RVBRwl6RGEArFxrX8YMblZaHLT5vwD2ZYKnMpwqEyUenvRxiuDkBTB7jbEwTruHAd6iQYkZxz-nY7dwBm-ceXszRgv_Ev4Cqm3uX2DujILKWcypWMS73oyrIB_GWXeRKQIaJb4WAwBnAUcLGWqiW5SW_kR5AdqOQhvFZwPeFhgoMOm59QzgTAdwd3I9lE-sQQOK-_3vudbZZvAHrlEk72zTZ4XfNLRjZfCkOTGGsYBXFahbdko2CJfjW8YfhFk7o0irRPXle-nhLqm_AOuPVqCW_oCUKvJ1zV5lrqQKIFROLzyhyojbtMVjYRpwZiwhdhhX5Jbm3OAy4vSCb-CTCEN-pxEslsEHwP2-rLPuR-sPj2btLbhpNQRGGi0_DSzRIZEzyajsw5OWE4PXOxdhT8RI5dxWuts3XOxYJFyAWEOV7pcXr74w6GSyMoGa06ZxyLQja04i7CCa0ji603eyujo28KM05xwoXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=X0CnoflQ9XDemwr4_bBjKYEGUMTzeq9257zPOd2un-PFR_JVYPFogBQyLOU83gwC4-5rwBW-H4xsS076Coaq6Ytz5G6b9hcH5XE231-eyxLFY9t20Qrh13u9mbXGKpL2i0iduoiiKR3W8A5FAR6SlAofyfP8iwcU5cbBG-cryDumOzWwH3Dc3mYJA38GPY-BvDpvtRkmF2RVBRwl6RGEArFxrX8YMblZaHLT5vwD2ZYKnMpwqEyUenvRxiuDkBTB7jbEwTruHAd6iQYkZxz-nY7dwBm-ceXszRgv_Ev4Cqm3uX2DujILKWcypWMS73oyrIB_GWXeRKQIaJb4WAwBnAUcLGWqiW5SW_kR5AdqOQhvFZwPeFhgoMOm59QzgTAdwd3I9lE-sQQOK-_3vudbZZvAHrlEk72zTZ4XfNLRjZfCkOTGGsYBXFahbdko2CJfjW8YfhFk7o0irRPXle-nhLqm_AOuPVqCW_oCUKvJ1zV5lrqQKIFROLzyhyojbtMVjYRpwZiwhdhhX5Jbm3OAy4vSCb-CTCEN-pxEslsEHwP2-rLPuR-sPj2btLbhpNQRGGi0_DSzRIZEzyajsw5OWE4PXOxdhT8RI5dxWuts3XOxYJFyAWEOV7pcXr74w6GSyMoGa06ZxyLQja04i7CCa0ji603eyujo28KM05xwoXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نتانیاهو درباره ایران:ما رژیم ایران را سرنگون خواهیم کرد.
ما این رژیم را شکست خواهیم داد.
🎙
مجری؛
«شکست» چه معنایی دارد؟ آیا سقوط خواهد کرد؟
🇮🇱
نتانیاهو:
سقوط خواهد کرد. ما آن را سرنگون خواهیم کرد. این رژیم به هر حال در آستانه فروپاشی است.
🎙
مجری:
آیا رئیس موساد، رون گوفمن، برای سرنگونی رژیم ایران تلاش می‌کند؟
🇮🇱
نتانیاهو:
تمام نهادهای ما، تحت هدایت من، برای سرنگونی این رژیم و شکست دادن آن تلاش می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71019" target="_blank">📅 20:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71018">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=DqUV5NmS8AahmjutXr7YeOq6bCQiUk1xd0UFPMFHDky9muMgE82uPe6YRZNxXZSbKA8dkFOWSmlau-NnUhQh54to6UvohHUfNr5vv7Mqf6YAezVhLLI5N3H2Vhe3riyQ_aKA0DZDeyJQq8boK1uFznr-HES5PNXrZ-xg8wz02eqqQSKUEUPxOMqf-NgT0XKzD8JUf6q9fWWQhUOmCCTftAXnsvao1fDwFLdzPmKTyuEmCyHG4C06vgmax22sXN-CkrbxUnk9vpz18iC6J66eu-5x7nBDd-x3-24z-BauZ0k2AHbS6WaHulCyA-da4tpFchhFj4Kyn56jqXfMj92Kgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=DqUV5NmS8AahmjutXr7YeOq6bCQiUk1xd0UFPMFHDky9muMgE82uPe6YRZNxXZSbKA8dkFOWSmlau-NnUhQh54to6UvohHUfNr5vv7Mqf6YAezVhLLI5N3H2Vhe3riyQ_aKA0DZDeyJQq8boK1uFznr-HES5PNXrZ-xg8wz02eqqQSKUEUPxOMqf-NgT0XKzD8JUf6q9fWWQhUOmCCTftAXnsvao1fDwFLdzPmKTyuEmCyHG4C06vgmax22sXN-CkrbxUnk9vpz18iC6J66eu-5x7nBDd-x3-24z-BauZ0k2AHbS6WaHulCyA-da4tpFchhFj4Kyn56jqXfMj92Kgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از دیدار محسن نامجو با مجتبی خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71018" target="_blank">📅 20:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71013">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ib3LBrbvR81GyAqOxhVYQdU8v7_uNUQ0wPZn8xLdD919EGm3BosvZeDh27hki8DfdVgfcJRij6NMArovkkTkxPVN0KyXmtWl7xGH8vJzkAhwWMRYD2gec5S6w5PAcXV9f_zTePYAPOeJN1stu5HqL9sZgg69oj9b1FU2qKfZOxA-fSRtiarU8z9wu1ZOEjT-Qu0EK47OS_Yhc-Crak6u4xm5l3ofyQOgByJ8spxA1dnIUK0cUkKwT95GthdvRfDiUay6n1_Q3Yquj5mAsQ53qtLyF81KF3WMdOHJCDqNwmEinWCCU2hz_JtnFujmE8mKnY0y9f-54cEBvIVILAidaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRuP7rvOLG6IAyprVJpe_PHR5c7hCLlv8W-dJBUiSWapVRY197sq-g8E1ZkaccuTkn4Ur-Yt9DU5ROwTL_Hz29Je37ltfCeVO9aJf_X4jKI2_1k18rT92FsgNiQcMjBgKqsxJ-ITOR7v-uIvSvFhDRm07Blhj2i9tndRwSFzUp-bD-PURCzwbQqdsLQKqVZCPDOY-MMM4pnePVcgULka37U3ms8HzCqcGrMglvLr1-Ox8C1qpNxcaQUqPSGOIFFS9EMWty2L4C2BGZ7URLZ9uouYmsy5hx5V31pf8BRaqovp1fl_yKfilBqvfiOZtxVv-XlzeA4aLwGhHuFxL1KZcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21e8023466.mp4?token=URKDQUnhPxKG-XNSdbM9HjlagSnxAgrqNTKqAcL7QTuGfDq06XdMcI9cTDqBvR7-XYeqeaxiQ7eMD4QIdXPyZtV5-VLfV87-33OAJ_xze03ePeF9nXcQSua00bMzAE722KxI85T3LK1vcf7iiTgANTC1SExPsPrfXBgGydfL6lpVrTIH6HclPAobmIzrMCkCesBDcbpH1JVTnz5kOeLgCDeFGk83zAgtZMCR0K0RZR7LEwNSQ5z-kxD1HKoRcRD2VznXN1DYRPEEMYzs1X7hT9Q1cLPYmyv59OrC41tCQV6ORLzq1-Uzb8nbY4IjofcCTT67KAPaTx93DvjPmPhVKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21e8023466.mp4?token=URKDQUnhPxKG-XNSdbM9HjlagSnxAgrqNTKqAcL7QTuGfDq06XdMcI9cTDqBvR7-XYeqeaxiQ7eMD4QIdXPyZtV5-VLfV87-33OAJ_xze03ePeF9nXcQSua00bMzAE722KxI85T3LK1vcf7iiTgANTC1SExPsPrfXBgGydfL6lpVrTIH6HclPAobmIzrMCkCesBDcbpH1JVTnz5kOeLgCDeFGk83zAgtZMCR0K0RZR7LEwNSQ5z-kxD1HKoRcRD2VznXN1DYRPEEMYzs1X7hT9Q1cLPYmyv59OrC41tCQV6ORLzq1-Uzb8nbY4IjofcCTT67KAPaTx93DvjPmPhVKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حملات جنگنده های اسرائیلی به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71013" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71012">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=AlEUeCIdhUaxlcV-lG3jIdfZu2mVTHGRg0njmqBDoRqV_uYV1RVT1B6rNxwSBA4bp4mzwdmpF5wtunkwsi9_DYVyNTQHbjFR1ULAHeXanaU-o3L0jx4SCWEiDzk-OUJwn7WWonj3TIk8h41hrHjzj5m4AieLDfv_VcR0pFC7H_jAvf60VFjvMXltWctZau7XTvli2cLuwVtPn9BDc2o1Tefe5dsvatpi67B29lASWh5sAcw264xbQkJDJHKhwz7CU4LWQBQVKNLIhqoSQyU_pWW07XotDbafPdQ3H2u3xQQJND78xwBY_k_trqGzuq7XWz_Kgdkbm5dO1bBJ-wcnig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=AlEUeCIdhUaxlcV-lG3jIdfZu2mVTHGRg0njmqBDoRqV_uYV1RVT1B6rNxwSBA4bp4mzwdmpF5wtunkwsi9_DYVyNTQHbjFR1ULAHeXanaU-o3L0jx4SCWEiDzk-OUJwn7WWonj3TIk8h41hrHjzj5m4AieLDfv_VcR0pFC7H_jAvf60VFjvMXltWctZau7XTvli2cLuwVtPn9BDc2o1Tefe5dsvatpi67B29lASWh5sAcw264xbQkJDJHKhwz7CU4LWQBQVKNLIhqoSQyU_pWW07XotDbafPdQ3H2u3xQQJND78xwBY_k_trqGzuq7XWz_Kgdkbm5dO1bBJ-wcnig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مردی در نیویورک آمریکا پس از برخورد مستقیم صاعقه به پایش جان سالم به در برد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71012" target="_blank">📅 19:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71011">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn5iGOG_1XPLAB6Pa-jftcW29FqT5EGsK3Wv71tBpl_iaqNbK1W-ddLcgDXNrPRWwvW6fUWo_uYOkDSX-2Tfz8M_XS0vm7cX7RP6NRUurpzzlrjL1AMnxHYES6yt_CZdZychKB_rFiu0flEjtfjcAtyI5znqY_nLRhcdTaSwoEqSZFy3blRaBI8YunlBi7KdA9E-TH-e_PnWqjozj6gWMXVQjx9Dje_KANnHnAyqT5sAJEZiJ3n9X6nWXstAtgBPG1s1wdGxFULjKUGkU6nU4QRF1OJgo66tSIQImn1MfkVik5smf8jD1_ICDjeOji3gni63lICkfDecr4Hd9UzqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
حالا که تنگه هرمز تحت کنترل ایالات متحده است، آیا باید نام آن را به «تنگه ترامپ» تغییر دهیم؟ این تنگه هم درست مثل خودِ آمریکا، «داغ‌تر» از هر زمان دیگری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71011" target="_blank">📅 18:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71010">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71010" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71009">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=hEW3ohw2wBLJOsMpDEbpeMh6oBXpVeJBv07Oq2tV7f0Y6PpliQsiUtr7rfv6jfky08dNzhpyJrHhxAgdF8oOYj7qIIhmeNvgR66aATKjE_-kbpIFYrldDgDyaYWT_VcXoucU6KNjL2RRguVHwMA6yf1ivn8RRST-H4dbapZ9b069UVjAyeFErPMBOAFpeb4pZRFz1P9Chyslc4lY7crq8NT9A2KBoK2fuHAEB0SijW0CCClRL0wze82sl3K97nKCm6mUFIrWKiRsjzbjRPNZpdNBb6oE_4b27n6mMb7qedV3nKAljVmm9J1l9_Gh64vnptQgOGMuzIB2-0YLDQkSnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=hEW3ohw2wBLJOsMpDEbpeMh6oBXpVeJBv07Oq2tV7f0Y6PpliQsiUtr7rfv6jfky08dNzhpyJrHhxAgdF8oOYj7qIIhmeNvgR66aATKjE_-kbpIFYrldDgDyaYWT_VcXoucU6KNjL2RRguVHwMA6yf1ivn8RRST-H4dbapZ9b069UVjAyeFErPMBOAFpeb4pZRFz1P9Chyslc4lY7crq8NT9A2KBoK2fuHAEB0SijW0CCClRL0wze82sl3K97nKCm6mUFIrWKiRsjzbjRPNZpdNBb6oE_4b27n6mMb7qedV3nKAljVmm9J1l9_Gh64vnptQgOGMuzIB2-0YLDQkSnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما اکنون کنترل تنگه هرمز را در دست داریم. ما آن را کنترل می‌کنیم.
دیشب ۲۸ قایق و کشتی را از کار انداختیم. ما کنترل آن را در اختیار داریم، آن‌ها هیچ‌چیز به دست نمی‌آورند و ما آن کشتی‌ها را نابود کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71009" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71008">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=eURfxp_W9PVr3umtQaxC0M2iCXZ107q-GqHBt2_guXfS8iiICpRC7owm6v7_FsN7wd3PFrQ6k9laS2dqu1lnQ43KFqBWJisch03CWGdemnxWIw2p78f58adSmQmWgj2tZxT5Enpn6dO7af_c6VcAyTAOO4gQrKeAe6_b_w4ZlqUPrwN-FDoEaI7NrrMwRLPhp04WhTUyYSHdgap0cFunW5AdY74HFIm87ghnlufz3mKovSbeK_MzSa94tWjfy32nj_Zrf-ob9BBsoOQnatqQf0zGUfbsAd1xrRq0Esm8aqG-B-LyZ5DhhdQWvR3x4kiPwLDbLiOcLQ3LBvF_Dx7iVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=eURfxp_W9PVr3umtQaxC0M2iCXZ107q-GqHBt2_guXfS8iiICpRC7owm6v7_FsN7wd3PFrQ6k9laS2dqu1lnQ43KFqBWJisch03CWGdemnxWIw2p78f58adSmQmWgj2tZxT5Enpn6dO7af_c6VcAyTAOO4gQrKeAe6_b_w4ZlqUPrwN-FDoEaI7NrrMwRLPhp04WhTUyYSHdgap0cFunW5AdY74HFIm87ghnlufz3mKovSbeK_MzSa94tWjfy32nj_Zrf-ob9BBsoOQnatqQf0zGUfbsAd1xrRq0Esm8aqG-B-LyZ5DhhdQWvR3x4kiPwLDbLiOcLQ3LBvF_Dx7iVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇧🇭
لحظه اصابت پهپاد شاهد-۱۳۶  به مقر ناوگان پنجم نیروی دریایی آمریکا در منامه، بحرین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71008" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71007">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnOCGHokFMkvFtxPSIHqUujDbU4tUSQD-InaGNUpcu9szo07jfh-x0YD1CpJYMypadgm4fBaMJgB6BDEyM1LWhpVFcrFy-lzHvKFIEpS4f9e_7E3g2iaCiBbEMjgrU4JdbyBlwOQxBLJa6XF9Dio0fX12po7VCHhjznvpXp2MfGT1NdqhVCxnKOi9Cgu9v5Is0CYFMHqeDCTpD3onRpsazcPmMq8B1Grn-30XAiMhnJgdOQxelfpS7Z0ybSITSEd3IdaX38EJP22GIWfCGn3BnPpor0WiFFYYRZnrz3c4CS6damVIqejiUIochW7IgYaBuhRfB45KN-bXdN31U5wmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه:
ایالات متحده به هدف قرار دادن ایران به دلیل حملات به کشتی‌ها ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71007" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71006">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71006" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71006" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71005">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc46TLpeuFwIMO8BAd2pcUhq-4PbQrzSSSAFAOd49IFkOVI2yuQ7SwyxEw9lYiLQNxHYecUZfXBHPqgMK5KsdJpqU3JpKZpOpFvnVHJ7AIvA0aDgti0aUbIGBcMRDkqQSqs91mvj4rIayURuGfGfvxvbEsjqgqiKXWKQCw9gMOcD8iVUpuonm2muGIt2609Zp9v9h9gzg11z90qC25ADYUxWEUD5EMafsY8fJRm7YWEC_XCVKnP2L1KHwDr3Tlz9ALllEfB27HGUn5TzbzMhlCROZzaeERUR9YeDDsza1ACXg9eqzhrXChjYGTUebb5EnFudtl0ZcigCTfqyWmQ8lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
استقلال
🆚
پرسپولیس
⚽️
پیش‌بینی دربی رو در
TrexBet
از دست نده!
📉
نگاهی به 5 دربی اخیر:
2 برد پرسپولیس | 0 برد استقلال | 3 مساوی
4 گل پرسپولیس | 2 گل استقلال
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71005" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71004">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26734edca1.mp4?token=s0migv0nNaClAyEfR4XU78k_x1pBwf7NzGaCgNAnZqhTJKH8XIonVVf6PPKA6t-yfgBvdMeSylrQO0dVz0rLR9AXrnVkuYT5RxW75EWhk8bybBz1aMQVaSUR7xkWktasHFbL0nlB68RDl0MbFCNAPfco_HN45_udGBc6SpX_4XXIqm2zwLDWucaLb24ZSWVBRgiMTORvNnjkRzSQuAhOW7jhjb2E2fDI2J90OfBO-eNaJOePjD_NZ47tfmtwnol5rV-sSAIqyUPK-I7P5HwFPe91IKUY7OShXNQSdB1lF1GKOJ9LjH-PKAhQSk0Vy4f9HjlW6yrRoT62wH9inu9qaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26734edca1.mp4?token=s0migv0nNaClAyEfR4XU78k_x1pBwf7NzGaCgNAnZqhTJKH8XIonVVf6PPKA6t-yfgBvdMeSylrQO0dVz0rLR9AXrnVkuYT5RxW75EWhk8bybBz1aMQVaSUR7xkWktasHFbL0nlB68RDl0MbFCNAPfco_HN45_udGBc6SpX_4XXIqm2zwLDWucaLb24ZSWVBRgiMTORvNnjkRzSQuAhOW7jhjb2E2fDI2J90OfBO-eNaJOePjD_NZ47tfmtwnol5rV-sSAIqyUPK-I7P5HwFPe91IKUY7OShXNQSdB1lF1GKOJ9LjH-PKAhQSk0Vy4f9HjlW6yrRoT62wH9inu9qaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
اینترنشنال:
⁉️
🇺🇸
🇮🇱
از شهروندان پرسیدیم پاسخ شما به پرسش ترامپ درباره زمان قیام مردم ایران چیست؟
یک شهروند با ارسال پیام صوتی به ایران‌اینترنشنال خطاب به دونالد ترامپ می‌گوید: «چه تضمینی وجود دارد که ما بیرون بیاییم و تو بعدش مذاکره نکنی؟ ترامپ، کار را به نتانیاهو بسپار که او بلد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71004" target="_blank">📅 18:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71003">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=g8CPHcuFG6v4gtOFOtuUxQcXOAtoFgMErnGCTFZaz-um0lz22XuRfizpRxDy6jy5rKlrxUaGnK9Ye9mYfj1lCwUDPRh6bnjcpeD4VwK2JpmLasqVNTSP5tYJ2SRp0Qc_o2S6VLtCX38W1HCpJXawiaSirY7UBC1IuVouEokarcEfuVC9a9glXt33h_mWUIUHd7JovBRTmFhrGcTF3Mc_0nqDRl79t04pyiyC5_0N-jvsPsa3vItunN-IaVSXz90nSTgCu8ACV370Tut0NAFihg_SWVNga1Ir02fFJeLXNpkj5QdNxfStocIwa88yMrmqPNrOs4iLElsv68u5hTn4sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=g8CPHcuFG6v4gtOFOtuUxQcXOAtoFgMErnGCTFZaz-um0lz22XuRfizpRxDy6jy5rKlrxUaGnK9Ye9mYfj1lCwUDPRh6bnjcpeD4VwK2JpmLasqVNTSP5tYJ2SRp0Qc_o2S6VLtCX38W1HCpJXawiaSirY7UBC1IuVouEokarcEfuVC9a9glXt33h_mWUIUHd7JovBRTmFhrGcTF3Mc_0nqDRl79t04pyiyC5_0N-jvsPsa3vItunN-IaVSXz90nSTgCu8ACV370Tut0NAFihg_SWVNga1Ir02fFJeLXNpkj5QdNxfStocIwa88yMrmqPNrOs4iLElsv68u5hTn4sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
فردوسی پور:تاج و دوستاش نزدیک ۲۰ میلیارد از پول بیت المال رو گذاشتن تو جیبشون.
چند وقت پیش تیم ملی جوانان ایران واسه برگزاری یه اردو قبل بازی‌های آسیایی، به ترکیه سفر می‌کنه.
تو آنکارا، هزینه هتل‌شون طبق سند خودِ فدراسیون، 116,160 یورو شده.
بعد برنامه ۳۶۰ زنگ زده به همون هتل گفتن که قیمت‌ها اصلا این نیست و انگار مسئولین فدراسیون قیمت‌ها رو الکی بالا بردن! و هزینه ای که کردن چیزی حدود ۳۶ هزار یورو بوده.
خلاصه تاج شیرین نزدیک ۷۰ هزار یورو کرده تو جیب خودش و دوستاش
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71003" target="_blank">📅 17:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71002">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=bWq2Q4-t_VFOI9NxIOWlp3QEQXTycDqzpgXsojqVOcTnjPFwrK9JrfZtKsQcbPhs0bEMShabCJw6A006lV-GT8KhjSGlHL5MLWC3j_waS3oLvjFUnfsPXG7fSjDk3buSVNJ7ovmZ-ZeEnWz_P2tMaDyQUkVirET3fVLZVDTv5AW74rODhH-X0U2OcNrzZthTlUuj9GtkMRRKHVPlVALj_AaO5hPheiNG5XDvlPqiAwvOQSh_3bHHtcNgZHItR2JnV5D0iu4igOmAJjXaog6692PvRpRcbqoTP2_drg0C2KhU9GN996yCFXhkOStD94Vo7cbqaclcklbnbrF9A6yZQkE8Vto3TInl2AFmpxktWxDPbajv1pufFPSfR1uKgD5TKrfoY-_eZIwg5j9JsysG751RpM2oZCt0r1JtiAuQitzVL2XqNyKjEJwMXStmBhnRJNKYILZkGSttgFcxbGRootvbWKqAxtDwguPTz-rbldOyFjNlHahpJE3JnpN_ao9nMEHnY1gVMETaKxU_1iJNpxzCvecirbcOlJC2pTxizRdkMQo7NW47U8VRebdDSQA3rLz6j4odp3Qont6mWSZee9KbZuznitiyL9-dfhkNl7V8ZmMXZoArn4hrovXOMm28xhxx9jEqRzQS1XIxfsH22bUtr1RGyhYqV94PCuFF3l8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=bWq2Q4-t_VFOI9NxIOWlp3QEQXTycDqzpgXsojqVOcTnjPFwrK9JrfZtKsQcbPhs0bEMShabCJw6A006lV-GT8KhjSGlHL5MLWC3j_waS3oLvjFUnfsPXG7fSjDk3buSVNJ7ovmZ-ZeEnWz_P2tMaDyQUkVirET3fVLZVDTv5AW74rODhH-X0U2OcNrzZthTlUuj9GtkMRRKHVPlVALj_AaO5hPheiNG5XDvlPqiAwvOQSh_3bHHtcNgZHItR2JnV5D0iu4igOmAJjXaog6692PvRpRcbqoTP2_drg0C2KhU9GN996yCFXhkOStD94Vo7cbqaclcklbnbrF9A6yZQkE8Vto3TInl2AFmpxktWxDPbajv1pufFPSfR1uKgD5TKrfoY-_eZIwg5j9JsysG751RpM2oZCt0r1JtiAuQitzVL2XqNyKjEJwMXStmBhnRJNKYILZkGSttgFcxbGRootvbWKqAxtDwguPTz-rbldOyFjNlHahpJE3JnpN_ao9nMEHnY1gVMETaKxU_1iJNpxzCvecirbcOlJC2pTxizRdkMQo7NW47U8VRebdDSQA3rLz6j4odp3Qont6mWSZee9KbZuznitiyL9-dfhkNl7V8ZmMXZoArn4hrovXOMm28xhxx9jEqRzQS1XIxfsH22bUtr1RGyhYqV94PCuFF3l8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طراح ارشد موتور (بمب‌افکنB1-Lancer) متولد سیرجانه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71002" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71001">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618f407212.mp4?token=dUaebrg_U3mgKRO8HLNw9bmxLlyRYcIkhDT9xjSItW7xCV30Bwlb9RQN59UMohcQ5j_hBgQ9UOLoUpyLbJCLRdu3RVjplCad2zIDNN-e8sz533Zys7rK05OFG50LWOgmJdsj0rz3RXhW8_Q1ryPg7j39psZtAu0UBR63slOSjdIOWckyl3JcO6DHKsquhYF2uf00WzqGxx7YOElTGDAZVbmPcF-t_ln3ChRd591mhskyktM_GyCtqzQ_0AMoMEa7V8tRF8WR9q95DcIf0Z0X8jbAluXpiNn4hatsHUjmtGUpSiesohLasm3GnQ1UhGu4vE34Py8Z2KH7xS1cRci_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618f407212.mp4?token=dUaebrg_U3mgKRO8HLNw9bmxLlyRYcIkhDT9xjSItW7xCV30Bwlb9RQN59UMohcQ5j_hBgQ9UOLoUpyLbJCLRdu3RVjplCad2zIDNN-e8sz533Zys7rK05OFG50LWOgmJdsj0rz3RXhW8_Q1ryPg7j39psZtAu0UBR63slOSjdIOWckyl3JcO6DHKsquhYF2uf00WzqGxx7YOElTGDAZVbmPcF-t_ln3ChRd591mhskyktM_GyCtqzQ_0AMoMEa7V8tRF8WR9q95DcIf0Z0X8jbAluXpiNn4hatsHUjmtGUpSiesohLasm3GnQ1UhGu4vE34Py8Z2KH7xS1cRci_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بررسی قیمت چند داروی پرمصرف از شهریور ۱۴۰۴ تا شهریور ۱۴۰۵:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71001" target="_blank">📅 16:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71000">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=Myv5-sp8ecN4NILAK53N5JLiWSXyT8naRcX1YPfnC1vqAej6Mr1EcUGXqLF2eWkTKaSu2movRqqldeSk3LtRdc7CKiiekCmV7muljJk3ztajENjjbv_Qf-o0_I3BpAQOYM8LaUbCnS85_4bYsVdodqHEuivV9hyGSJu2OKpkdQEx4iJLdRaEqfdMaA2apS5TJTWADO3p3BuZy8xZ8Syv-ImHdS5NG5r2wE6B3C-PuD3WDGbnV8nOERczsMxv5qC_G3G46mT2XnnZANjAJHdno-_eIIIY5FBK29h_WlJ20HJjtyUSenzZu168azvZ0uokVVIc4ZFX3xJLuBEG4TAZfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=Myv5-sp8ecN4NILAK53N5JLiWSXyT8naRcX1YPfnC1vqAej6Mr1EcUGXqLF2eWkTKaSu2movRqqldeSk3LtRdc7CKiiekCmV7muljJk3ztajENjjbv_Qf-o0_I3BpAQOYM8LaUbCnS85_4bYsVdodqHEuivV9hyGSJu2OKpkdQEx4iJLdRaEqfdMaA2apS5TJTWADO3p3BuZy8xZ8Syv-ImHdS5NG5r2wE6B3C-PuD3WDGbnV8nOERczsMxv5qC_G3G46mT2XnnZANjAJHdno-_eIIIY5FBK29h_WlJ20HJjtyUSenzZu168azvZ0uokVVIc4ZFX3xJLuBEG4TAZfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرت زدن وزیر ورزش و معاون وزیر خارجه و تمیز کردن دندان توسط وزیر خارجه هنگام سخنرانی پزشکیان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71000" target="_blank">📅 15:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70999">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JN9yxE_JzrmbITUs4nCSxlhxdjQIQxOviAKPhKpM2zKQeyby8DCFXJD8bQSUtZu2Cb-XwfbdHO1yXOSi9L2jlMJhTIe5t5sUkpVXmZkX5wHRodXQ5qB7Thn_FkQBR7ORXnNXwtLQ4QrZ2N5H5idLUyi4aF48N8Lkg8KNVhUNa1JdIeKxFPwr3TJT18dIUJjCwZKSMkNX3oVZPCrXbVdpII6J4fRKXak49i4yxagxeHzrOwgswK5gJH9hZAt0B8RAW9Y7TNA5ihHFekcKivJv1XJSSQ8jijaimFbuD6NahRzBrWRbJOrXu49dLefBknXXug5gtXdtTMfT-j8qxHqWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70999" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70998">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM-kXnwDlYYI_DcQPbzJuMq18eo5gFZleO2syICQWpmIEVHpMdeStO5eUDYzZW1szQEC95xB1Rax875UVilOeDT5Pe3w_8wvl9VZSYQrXmTr9fLWeImGn3FEnBKDZlqdWa9b-YJPLnj6pvrN3rczsGpuihLIwi3CiPr155vE3npHRCxV4sjowO6TDmpQmAzL3W7c6-NDc-SB8667J9wwKGc-jG2Wyq5p_-OntrGG5wVJsfcFkp1zMWSz53ZvVb2-fVykOC2L5zaQ18J8B60RonIXzSRnUnrt-hgPxrQ4kzYDxXESwCPeX5d3pg2vpbenPKwSbJapxOHRlcFAW3SLSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
فیلد مارشال محسن رضایی:
با این دست‌وپازدن‌ها، نه تنها در بیرون آمدن از آن ورطه هولناکی که برای خود رقم زده‌اید ناکام خواهید ماند، بلکه به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، بنیان‌های شما را درهم خواهد کوبید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70998" target="_blank">📅 14:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70997">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13235e9918.mp4?token=FngCKgc4rStWn8VtJKtlT1-_LKEF_FO3pNUPNmpVICw3H2a6UI3m_J-4Cajv1JhSJc9qjymH_7m8F57qEf7qvYX1fiKGusp20SMwQ1LMQkQs4i5z0LZ8qVHEtEPYI_2jkqU_Ga7WI8mskg-J5fg231Pmc0euQG0sWlztS8NU3w2gU56f62zK5VtvykgN9XmxwJ7qSD6qyXqXStxjbP2s5hjpUpORZcF_rTd-GvuYN-13xPtrxYgvwyRjTVhJJCtVnGV6eICdYP25Zc35AHo32i-XuQKNUEy_6_PtCTaiB43VZhAhBImArj8Vng0rESWqbgkoBS6xoRO5bWNx_3OOOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13235e9918.mp4?token=FngCKgc4rStWn8VtJKtlT1-_LKEF_FO3pNUPNmpVICw3H2a6UI3m_J-4Cajv1JhSJc9qjymH_7m8F57qEf7qvYX1fiKGusp20SMwQ1LMQkQs4i5z0LZ8qVHEtEPYI_2jkqU_Ga7WI8mskg-J5fg231Pmc0euQG0sWlztS8NU3w2gU56f62zK5VtvykgN9XmxwJ7qSD6qyXqXStxjbP2s5hjpUpORZcF_rTd-GvuYN-13xPtrxYgvwyRjTVhJJCtVnGV6eICdYP25Zc35AHo32i-XuQKNUEy_6_PtCTaiB43VZhAhBImArj8Vng0rESWqbgkoBS6xoRO5bWNx_3OOOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
پوتین خطاب به پزشکیان:
تو این شرایط سخت، داریم سعی می‌کنیم هر کمکی که لازم دارید، بهتون برسونیم
.
قبلاً هم دربارش با هم صحبت کردیم و داریم کالاها و اقلام موردنیازتون رو تأمین می‌کنیم.
با وجود شرایط نظامی و سیاسی فعلی، همکاری‌های تجاری و اقتصادی‌مون رو با همون روند و قدرت سال گذشته ادامه می‌دیم.
همون‌طور که بارها گفتم، ما تو روسیه کنار مردم ایران هستیم و باهاشون اعلام همبستگی می‌کنیم. شجاعت و مقاومت شما واسه دفاع از منافع ملی‌تون واقعاً قابل تحسینه.
لطفاً سلام من و حمایت صمیمانه‌ام رو هم به رهبر جمهوری اسلامی، مجتبی خامنه‌ای برسونید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70997" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70996">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">1
💵
= 200.000
💸
🔼
یک دلار آمریکا=دویست هزارتومان   @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70996" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70994">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=bR7WqzdSlIWIm_rE4FznE_VVCi-581MfDQ-f3i_CeboGPo5OKHSx8Da3i884LsvQ91JVcVNnJwCeJF_zSh5M_fLjOJOJwfUgUkbbYoJGuy9qaH5g-EcHZH4SfaWv7AvE4TZs89SWmv9UyG-DW0LuaDsKyzeXW04QyMqyx16bKq8Jt-WupgvEjOAXarNAQKGjRKJV2OKlehKgzOyo_ltYMKjzMjSBfyHr74U6oISWGW1Z_Lup67V3mgWvUqCvFSdPDpvg2K8RDHHRoU5S8MemdhDjjytT5rzLd-GjbJdOOnHLDCax7D8spbLbMi73l6gvn5u3LpMlcVZnVeOu0ui2oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=bR7WqzdSlIWIm_rE4FznE_VVCi-581MfDQ-f3i_CeboGPo5OKHSx8Da3i884LsvQ91JVcVNnJwCeJF_zSh5M_fLjOJOJwfUgUkbbYoJGuy9qaH5g-EcHZH4SfaWv7AvE4TZs89SWmv9UyG-DW0LuaDsKyzeXW04QyMqyx16bKq8Jt-WupgvEjOAXarNAQKGjRKJV2OKlehKgzOyo_ltYMKjzMjSBfyHr74U6oISWGW1Z_Lup67V3mgWvUqCvFSdPDpvg2K8RDHHRoU5S8MemdhDjjytT5rzLd-GjbJdOOnHLDCax7D8spbLbMi73l6gvn5u3LpMlcVZnVeOu0ui2oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
ناو «یو‌اس‌اس آبراهام لینکلن» در تاریخ ۲ سپتامبر و پس از ۲۸۶ روز حضور بی‌وقفه در دریا — که رکوردی مدرن برای نیروی دریایی ایالات متحده محسوب می‌شود — وارد بندر «لائم چابانگ» تایلند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70994" target="_blank">📅 13:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70993">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل درباره ایران:
هم‌زمان با افزایش فشارها بر آن‌ها، تشدید تنش‌ها و تنگ‌تر شدن حلقه محاصره — آن فشار اقتصادی خفقان‌آوری که رژیم افراطی بر مردم خود تحمیل کرده است — احتمال دارد که آن‌ها واقعاً دست به حمله بزنند.
چرا؟ زیرا ممکن است برای رهایی از دوراهیِ میان «خفقان» و «جنگ»، گزینه دوم را انتخاب کنند. ما از نظر دفاعی برای چنین وضعیتی آمادگی داریم.
اکنون در ایام تعطیلات هستیم و آن‌ها معمولاً در تعطیلات یهودیان دست به حمله می‌زنند؛ هرچه باشد، آن‌ها از یهودیان بیزارند.
اما ما — هم در حوزه دفاعی و هم تهاجمی — و با هماهنگی ایالات متحده در این جبهه آماده‌ایم. بله، در همین جبهه.
با این وجود، سناریوهایی وجود دارد — مانند حمله به اسرائیل — که ما به هیچ وجه آن‌ را تحمل نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70993" target="_blank">📅 13:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70992">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=TAhfn4LctZwn1E5FddihNAGf5tC-4Sq8_TJXFU-reTryKDvFVZ8OljuOvOK0jZfPUCmOoBoB9k-oPxVMUj96ZJUp-E3xWw7pvLELE67RXEGGtabgiZQad7_inWmk0HJ340moEdtCAa1M5adk1RxTusdxiqqIsNOkNWSozxhs1njpE3orIoBqc8LMvTOEZefiCokei-IAr6_hWIRzWD3aNY-TYSdIqJvKvVLKCRaHL4tByFPoAVH3MbXnZs1RQ4T5DHIn8Nz4Ofa9L6o8s6BusSp52I4xZdLTn7CwTtBNi12wAw1kdWNpuu-v2JL1JbkQPJg5wN_fJZ3JGm8G5GPzZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=TAhfn4LctZwn1E5FddihNAGf5tC-4Sq8_TJXFU-reTryKDvFVZ8OljuOvOK0jZfPUCmOoBoB9k-oPxVMUj96ZJUp-E3xWw7pvLELE67RXEGGtabgiZQad7_inWmk0HJ340moEdtCAa1M5adk1RxTusdxiqqIsNOkNWSozxhs1njpE3orIoBqc8LMvTOEZefiCokei-IAr6_hWIRzWD3aNY-TYSdIqJvKvVLKCRaHL4tByFPoAVH3MbXnZs1RQ4T5DHIn8Nz4Ofa9L6o8s6BusSp52I4xZdLTn7CwTtBNi12wAw1kdWNpuu-v2JL1JbkQPJg5wN_fJZ3JGm8G5GPzZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از فروش طلا، به دلایل کاملا نامعلومی بیش از 5 میلیون بازدید داشته!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70992" target="_blank">📅 13:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70991">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70991" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70991" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70990">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cueqwX5btFlz5WVbHlQiA2wUgiPKvOQZQqhe0lDdcB3OpmIFx_ILx7g1e3CbNOShZjU3h-jGrfr4ABwkPge9bO4zTAoeaAauCw6t4FNjvIJ8hKLvnh7AFBr78CYiLfkJu65CgkowYQGGF4S3Vqo7np6fLUiikPkCQr0MT7F8L3YuPCTyeTvV3MaLyP7meE1RDe48YtRDRGQSZQaY0ATMbg-P19m5UZVSafJS49WywggY204XK4GCP4NI6yKZecmZAfoPuZZouJYWTTkeaoCIhvU5RNoBeE3W4wUdGIn763pnexL0bSVM3URgyYq_ohcIEqZiVDcqECrd-qepcqMIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70990" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70989">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1829295007.mp4?token=gg6u7_1tflk0mr3IsdH6kdBjMym1GgVwO3ua95eAvVbhQrGr7OQU49tBWXbv96fa6Vmwsozc5nuHGL_Wlrs9Lyv5E8ORetrW9Ss-Ltz4V4MECHxRgltEWyKqM2qVmUEAWgZ1n0P1IridZ4Z6xxDTS9BY_XLWBQDS3bntTgK3yIIAyqrog5iH30FdErJqduKOT_mTlBTh1ugb0PObp923S6Bg9AblqxOje8Wtsz1lgM1oJqaqVVTbeh-NjeePFb6fh8yN6wHzABa2A0DhEu1Xs9M1hGiukmtjwuupFPUpjS0WMJBF7qCjniJIcdnKMTrDeEseaxj6ukqJyh6pj1Jhgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1829295007.mp4?token=gg6u7_1tflk0mr3IsdH6kdBjMym1GgVwO3ua95eAvVbhQrGr7OQU49tBWXbv96fa6Vmwsozc5nuHGL_Wlrs9Lyv5E8ORetrW9Ss-Ltz4V4MECHxRgltEWyKqM2qVmUEAWgZ1n0P1IridZ4Z6xxDTS9BY_XLWBQDS3bntTgK3yIIAyqrog5iH30FdErJqduKOT_mTlBTh1ugb0PObp923S6Bg9AblqxOje8Wtsz1lgM1oJqaqVVTbeh-NjeePFb6fh8yN6wHzABa2A0DhEu1Xs9M1hGiukmtjwuupFPUpjS0WMJBF7qCjniJIcdnKMTrDeEseaxj6ukqJyh6pj1Jhgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇨🇳
⭕️
حسین مرعشی دبیرکل حزب کارگزاران:
🍆
چین سفر قالیباف به چین (و گسترش روابط تهران-پکن) را مشروط به موارد زیر کرده است:
۱- باز کردن تنگه توسط ایران
۲- دریافت نکردن هیچ‌گونه عوارضی
۳- پایان دادن به اختلافات خود با عربستان
۴- پایان دادن به اختلافات خود با آمریکا!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70989" target="_blank">📅 12:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70988">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعاتی پیش دو فروند کشتی نفتکش که با تحریک ارتش آمریکا خدمۀ خود را پیاده کرده و برای گذر از مسیر غیرقانونی در اختیار عوامل آمریکا قرار گرفته بودند، با رفتن روی مین منفجر و متوقف شدند و در آتش می سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70988" target="_blank">📅 11:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70987">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0gD3_rxSpVI454rERUki8mb6YnuOwjpE9hSEM-m1XpulabgosHo0wf5MKFm7limm0zdkQxaOw4jMcu8oKl3zp839QbsVG9zyAYK4D802dbtfADkvKfLdAjkRc_m1q5lV7OXPrAyunC6rYAbn2iwLOh6fAZyauAEYJ0AGitiGHD6WuSdQtwhbApjcbtD1Jl0M6A8TNGu7SwHgxeCYiJfk0Ke2d84v41JwefEVyQ0r8r7sGLQmUbSS95D6UxdpzeXSLZi1Ixdz3UGQogAt9b14eYbx6b8ZnnAOyh9-Wj7bCBi4gASHCFqXtD9rY0rBigIoXL4iCwVelDEn6V5RU2PwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
من برخلاف گزارش «ای‌بی‌سی نیوز» (که اخبار جعلی منتشر می‌کند)، سعی ندارم ایران را به پای میز مذاکره بکشانم. برایم کوچک‌ترین اهمیتی ندارد که آن‌ها توافقی را امضا کنند که از نظر خودشان بی‌ارزش است.
وضعیت فعلی ما را بسیار بیشتر می‌پسندم؛ چرا که تقریباً کنترل کامل تنگه هرمز را در دست داریم و اقتصاد آن‌ها نیز در حال فروپاشی کامل است. آن‌ها صرفاً دارند زمان را سپری می‌کنند تا با سرنوشت اجتناب‌ناپذیر خود روبرو شوند.
مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70987" target="_blank">📅 11:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70986">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=XgnWHwX2WS4ElNVLLCFP050FOEvpEXzJmLOYsf-WTsO_EXreWnrm9P75ZnhaNbsLBi6zeLzrCaU-PXkQ4iNhfLoRTsVVWn4ydlA2IiQQyw7N-oKr70HwL2bSsmRBqt5FJY9mzR017wRdEWdmCNjC1R9aLn3_if7Nw0J6KJkuRFiwQ4zVDivPSieMDQd8kes9iv5i6iwUxKA6LeFpecjjfiaqrXkJdLWtsS2vDukal7ggu2HDAbp16RMJYnTtddjyLc2eoU337gwfw0Y3mW29oOKECznHlLBYQBhrwW7d_ffca-jIilKdF_TkbNdHdDqXp8I1lbC4WLxj_8zczS2_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=XgnWHwX2WS4ElNVLLCFP050FOEvpEXzJmLOYsf-WTsO_EXreWnrm9P75ZnhaNbsLBi6zeLzrCaU-PXkQ4iNhfLoRTsVVWn4ydlA2IiQQyw7N-oKr70HwL2bSsmRBqt5FJY9mzR017wRdEWdmCNjC1R9aLn3_if7Nw0J6KJkuRFiwQ4zVDivPSieMDQd8kes9iv5i6iwUxKA6LeFpecjjfiaqrXkJdLWtsS2vDukal7ggu2HDAbp16RMJYnTtddjyLc2eoU337gwfw0Y3mW29oOKECznHlLBYQBhrwW7d_ffca-jIilKdF_TkbNdHdDqXp8I1lbC4WLxj_8zczS2_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عطریانفر، عضو شورای اطلاع‌رسانی دولت:
پزشکیان اول توسط شورای نگهبان برای شرکت تو انتخابات ریاست‌جمهوری رد صلاحیت شد ولی شخص علی خامنه‌ای صلاحیتش رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70986" target="_blank">📅 11:01 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
