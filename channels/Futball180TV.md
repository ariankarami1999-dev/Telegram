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
<img src="https://cdn5.telesco.pe/file/CH1tcVEJret5meoBP-vGYlqORPKg7tV7eRGo4e48DFhlV0SOS_OnuaK7y2Ji0TzslvxCtA3Z8mJodGOXqxai-QQhqhq64yDrvvZ2-BdMZKaieE4xDT1-fc67mOiEIdV_D5EH3ngQoaZJVGJ2xb178UfSmNLGRoS57E7nkF_gu_fXLWQOdDrASiiieC6wSZsNlSMxMqfoC8zNSR2fz-EkO5C25D1UeCWwI-sG0X71vUCgFDCkTc07C9MYKF2KGgFtywwZLzrrZCxNNbxStRMHeJAZro_MqhFrsifixFO09fAcSUnsnB39xPdooZzbXcblnLD1-A5WfCYb826UTzyVBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 216K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 22:15:48</div>
<hr>

<div class="tg-post" id="msg-91222">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csMLWUt7LvlO6Ne67vsWIcuDJQ024zwXHW4X20U2DMvzJtBl6Vv1M0IDTghFbff7gzFB4snp6ZqlfbkSpFWbQU83fpVXUQ5Y8nQ91n0c8tVH3TzxlHcorniJqwiWa6EIntluJLsDZ9tVfY5IvFqO0xL3fkarR6kEJcEZ7BpUXmIa3puBZJHq5sbMalvwZqRzOFNbGmtCkpbQO1XXa9z1hbwr74LrTPBunxzKAlXMD4IFzhaurpPZUqSaHj2XO70lM-Zp0k3Zg6q00mSKcbOm3Tgo_K13M5dNLNj5WyhXb0o_QTn1KJBmiUrXmrY88oAUIYi-pDDgyDTXnpdFRll9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
درگیری عجیب تو بازی دوستانه پرتغال و شیلی که منجر به اخراج مستقیم لیائو و رومان از دو تیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/Futball180TV/91222" target="_blank">📅 22:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91221">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc619ece3.mp4?token=MOOK2RaduRIeymXPX4O5An5qtMSolYHDPEugIhLzyLTrLKffEfVZ4jiIofoaTJHrHxNvFwZSQ1BSIa34iPmZGpCz62fYY7evXRH0GkWIS7yomWczW0Mc5oE9kNZ-X2xNDzZOSXBQclIR2f6HDJZ9n7wctT1OryH5FaLwBjcFL0TizM9G_XKuDp4EXn741LOdLslV4LXpKBDKwt3iuKRpgiU1OAug--kqh_EGydzkZK5WopuJbSalkt8_GOvyrdEFID8s_Y5vMbRMHBbK1dfytFHQng3Id5Vdx6ZVrMMXdn5NB5Jj_GWLdghjmvACb8MNnf_G6RFEUMFCnm_rn01sLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc619ece3.mp4?token=MOOK2RaduRIeymXPX4O5An5qtMSolYHDPEugIhLzyLTrLKffEfVZ4jiIofoaTJHrHxNvFwZSQ1BSIa34iPmZGpCz62fYY7evXRH0GkWIS7yomWczW0Mc5oE9kNZ-X2xNDzZOSXBQclIR2f6HDJZ9n7wctT1OryH5FaLwBjcFL0TizM9G_XKuDp4EXn741LOdLslV4LXpKBDKwt3iuKRpgiU1OAug--kqh_EGydzkZK5WopuJbSalkt8_GOvyrdEFID8s_Y5vMbRMHBbK1dfytFHQng3Id5Vdx6ZVrMMXdn5NB5Jj_GWLdghjmvACb8MNnf_G6RFEUMFCnm_rn01sLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درگیری عجیب تو بازی دوستانه پرتغال و شیلی که منجر به اخراج مستقیم لیائو و رومان از دو تیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/Futball180TV/91221" target="_blank">📅 22:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91220">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiMUORr6HWfoo0UvwQhLGBS6bVKhemtKrEV4DJ23S4eIKjAqfY2a6u6VjZccG7obsSYr6K5iqKaUJEuztpVGaYruCLmMbX9DiC8lgNakqs-KzNzclEEjq-Kz7Eo1lsPddAQYB-OsPqX9_rqhHd1UJ3z2wSdVkIYcRCIsI7XHVpaEAixoVZR4KGk-afnNZD2H_kWpYPRi78SAJVXEBwSHllDCv-RmI_2uDXnieiLpHEAXjHSFPq74ftH2RHBnRN9LEpAG2bugKC45hG2bwo1EhCaRO5KkLFHi6f2lVftDvSACXE5Zd638MKHAF7HvEwP0CEoEh_cAyV062czPcVIiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکاس تیم ملی عراق به جرم همکاری با حشد الشعبی پس از ورود کاروان این تیم به آمریکا برای جام جهانی، ۱۳ ساعت در بازداشت بود و در نهایت دیپورت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/91220" target="_blank">📅 22:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91219">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3LRoosjYGd76dVlwcGaSiZGy4rUtpciyYTjtwoKQ8QAZ1JfdABEBKLJ0seoWz_kgQddlBtozZGMykFP6jBpaOqTE-ij9_ra2emHK9BLppkNY9eOp98ptJzO2fb-VJhJg_kJB_fPVn5S5LfuVoPff9XTpnyoZy1RpoOQqO6b5mKxYvyWhSTkfERaYQY1aAI3-yLG4S4bwuUw0e_W60Nj5N69Ydtmay5mpI598njgM5AR8NU4qJMsTHyokRUDYELXGSPsZFwpsAXMCmzLjXflamYFPJvjY9EaRj6eRTMEpL2dtJBIFrQtQH6_XCwzM1zPuQ1dRj2ke29mTh-kmiyLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال 1998 مجله بزرگ FourFourTwo⁩ پیش‌بینی کرد که دلتونو خوش نکنید چون دیوید بکهام سال 2020 این شکلی میشه اما تو 50 سالگی این شکلی شد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/91219" target="_blank">📅 22:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91218">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuykF0YnpAu1c9uFZTjEcI2-HMkMM0yHT5T328Hd24iop8IUoIaBzFgXHNwzd_ke9stRZd_IkYuCCGBvUUHf7jqgjikq_fN3tbrk3zcrnSx-aHcvb2KnJnXUCDXgd2R8KeLBvyJCk9t-2FIA6j4cik1aJk19rPzpO64oZgC7vXFJN07cRpcdVqmFMJdgunQuQFhxe7yK-rb4KQ_Hg7ScOwV0z2FqEO8Qym7RMSGIk7FUiVeSlMzhZ679Mw6nklpCHsBqoXv7ToOjLqjGNjXHdnp_EKz2gX5mehG-Z9S4ZPXpOH9Z7-HMOru3WjrkJUJnKbHG3HHqO9VIhCSY2-jf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناخودآگاه یاد اون عکس افتادم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/91218" target="_blank">📅 21:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91217">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUzsxuMKKUVHcha-cg6kQuffn9G010sLwgcZ-pKB0ClOjGZ4ZwD_rPoMyEZ5hBJbKRIwM8_Xvg7fQ04Kufyr6M7eW8UYbK61jsXuuTnjkzcaI3io-dYgDajXO7i7cE7uuek71DZgYjQiMV6sAWS99_2zLp1fFYCJ0D2ckUvtmpI-KHEnJ6UP4ELLixaQTf2kTMCZPfFRUTItUQG0nKJL0vQEFmQ9CgyUhn8LkUnqqLGmKUdzJ2qv14-Q6yks_p4ey56iS8niUITaZBNDY38m-UkSH1hAEdxoKMVuKzY0LzbswXYeLRvyoK8asR0KE5eYF_Qthd2D_dJfr3Uc-7RjbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید لاشی چه دافی مخ کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/91217" target="_blank">📅 21:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91216">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm0F_tnZEjK_pxrU2lSZaBJ3KtF5NstRi2d5AGI7FpBsdleEcS1I5uXSAUDDoGzLqY2SfRQ2TW4B4MRjqIdvqF5xcHHzxcqlUF0y5on8c9ksyT3Vza2EWz8Il7K6OXiQzE3VN53ZP647lvQJhjDOIoJAbgEpyr5NhSGBRkXaryldXT32yjX3Eqqj9PNPpP5zVhRQ6j0u8hbuAARr8iLvRkmgeNJimTgPCQ7He1QCWtcj0QLlFbqaIeyYqap42-0wrf5ijt0CzB2iKxITOdAgwySocjMGxNbjHlMLCxhGinAchDBKFXtu6DGVmtDPsq99dw3o8yHOuSxcTY5p98-WYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اولین جلسه تمرینی تیم ملی اسپانیا در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/91216" target="_blank">📅 21:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91215">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vH7Lq4578wQeR4KeMAt6YkcdAw38ZT2_78pFdAqAaxsywhnzfVXRX1dwa6YsOM2nIpa1ZfljYuJvt288Jod46KTzTzxhTy9YWm7U5gfVqhQNvSbyhg0gWkbWvpaLUS3Ah3aFLACjQ9Jab9VSW0ObsLg5z0xPny6yO7NJwT5iyzHt0hjG-TblGo2fwLalek34-0gcMc2nz7PJ3uly9zB1r4Ts7TEdxFxeqGpA_QUeC3Ci1uKgfcMcH-DT3F9A1zOhySjfk6Q4PdsW_kvytjqBH-FnT5JACsg6FALU_mtrl_V5Aldmx9vXapvZk2afG4PZsRajD55A07hoCzaDHXewig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنری کویل یا علی ضیا؟ مسئله این است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/91215" target="_blank">📅 21:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91214">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYJsi2CxE2zXrK9_7SJy8LsY55lPzxSycIpX96-BvVmFLHJzzX_gkyE7WRpoehPLAEQd2iCseO07tZHcvLTP6K3Hgs654icvFLPx3RK41ecJShaGdOWePtQDkhBWbYF1NuZy8-mAihnr_nsHCql9JuD7YpBCWalNjEOnxriJrHS4b2Dw5fx42D3j8kaHXNXDyHSXqP6Es9L-Ytx_a9LWOVsHM4AlMLCbkoi3gUiMaMz4rBE9QPHW1HUZWdPTg5BKy2b9RXHidMWfLY2AGnhoHHW6v8kIQcx57B0LE8L6uqYLz_aDbbU2d-7L1MZEqPFevbvabE5i8nr6nPRNJaA1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
الرياضية عربستان: الهلال رسما برای جذب عثمان دمبله به پاریسن ژرمن آفر فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/91214" target="_blank">📅 21:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91212">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwdYMldv3mySnsJkxfIEK7r_lka9fa5XveecbjzuSufFJJbq_T5oxKuHl6dB1z8uYzyxrIK773_SP9poFgSUfTxkyYLQvHCBLA88pU8m9sSG7pHctSWshghQH2Zj81qKfmJgQJphItUbq3iPoqg8WolyitgJM42YxNDfl5ekDwe5NFFUP3Lj4Pq_tIX5mCT-gRtCLqf5S3frPA1qvb76CHB9f78bILdYBy7C204mQhemOPBbDDgrsAO9xb7lDBd5LA27COeeuP5z-xb1dshDz1qhZOCGB3bOuU58e7GoK14CO57DuBbxkG0AHdjQXhgnW04kODHzk8Wa5oxaT5EgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZSia1NRDIM80WACqy17X0MtYfTeTdBmgp5bgxnRS5MiBBgrsVHm5XQA9aPdTxcTvT4PASF6yvf61xeSEy0mGJ7BDjCEV9Ixgnr-WvaGDwmhfnZzsLmjU-NbMXeEdJ3lEfhtZdld7Dk78NgKoOR6HWtzediWF-pX5kCht1Ut767vBjgGEZLNtDgDpSIcn1RL8HiGRktF3xK3Tv8fewEs88LpqpHK1j9K6wUC7VupeFtQOfVIoMIgsZadMDfUukTx64ENyf0kvl9e-ilygrUjtElDjt8gW1NRa-p5z1xY8yWdZee6pM9RP0RSsO9obS2VXlcnnqkGJEsoWCmqJLr7Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم‌های اروپایی در جام جهانی 2026 و تعداد بازیکنان با اصالت آفریقایی آن‌ها:
🇹🇷
ترکیه: 0
🇧🇦
بوسنی: 0
🇭🇷
کرواسی: 0
🇨🇿
جمهوری چک: 0
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند: 1
🇪🇸
اسپانیا: 2
🇳🇴
نروژ: 2
🇦🇹
اتریش: 4
🇵🇹
پرتغال: 4
🇸🇪
سوئد: 6
🇩🇪
آلمان: 9
🇧🇪
بلژیک: 9
🇨🇭
سوئیس: 11
🇳🇱
هلند: 14
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلستان: 15
🇫🇷
فرانسه: 21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/91212" target="_blank">📅 21:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap1dnTkTXsFon0fjv88_waGno111j2Nh8P86fIbRGL_9K5SEACoIm7b_ZQHj6RpcW_0yW0cuulMt-KqdG-Vp2Yx1hjkDKp7IngWuRAu5ZEiOLHNGTKT0nRpe8uFekkngyTtyhqO50JIr31Fc0xpPnboD2JgYAEBBYTKooFMniSA8cPyFhlIO5q9rj-vL_OobgKM4CtTUCsG1hQSwBMUYgkcDcYADAQP0gssWTmkfREdNJ_CGlm9qrBvWGoW2ihM4p7v3XnxxZXCEe3kL7d0vdEvaXdo5Sinf4qzHgwjcQpf6UfV0ZdUMgyPY30Abg2BS_dfYLB54o3rS0Nyx_9ouRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سون تو جام جهانی های اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/91211" target="_blank">📅 21:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEJGa62i2MyUGM6H7__7KoO_RPTTttgMRVOXXmuANs7yvGA2ufqPy_3g8ngOQFs84uDS3T4niFXc3gT9uHo7uNFSuASROni8jkwH9YCiVZ3mflWegvCFh5syM7BdM5hKdPLQ-U49O5qqws2qnr2IjdJ9-mR1Mk63DJ3pE5v6b9ehObx8A9pAg-F8iwJ9TCT-9u4DhmmkkeIS_PRPV0uNGtU9qIUPNIK0SDvm8ePHRlhBCXup0lV7W9x_fNeBDc6EABdWJQxLpCoHZp0v2ihdUA49c1d1UKve0TeTqKKFu6S2NUfT4gxAnN9Kb6bazN8Hnb4-JiRyR-d7E6QVgWJC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب تیم‌ملی آلمان مقابل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/91210" target="_blank">📅 20:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91208">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZzAMV2M9okJqQJAzAA-HSvok5oBuWdKdOqJwjpXmJFow11-IY4F60MGOPrTMSO09fHqOj554t7_0x7HjxeSTM2tnOBEwseNSqyrkGwIGLkabX7c12Z51eowEAMSVQZTwGMb6Z3wfjLo0QkmkL0LWuzXgZ4Bfd4luX2UQypEtx7AiHT7TsYVjJcK3Ldij4l-f57JnDW2FdXWoK_UUfBh2Rt13h5FFC6Vg2tGNBkZz9VgW-PicF2OttKgNc98EGE-hYeJPGGrfUWUs3c8pFcdmhCUOTbrGn7ijRRfIgK9WKvHbQib8FSDOHAXz1JXVxW5ec8e8AmBu_uhqwuuVmoQeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب آرژانتین مقابل هندوراس در غیاب لیونل‌مسی در ترکیب اصلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91208" target="_blank">📅 20:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91204">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0PvR0BjFWfCjANfYsfu2zWQsqpBzAyehW6h4I16viPXiCeBx0fqa5RMKNaUJ-BJ2t8zHPSLsxe0V6COlteEmTOfBODRi6BC6e23K_cs4--xm5naplASsihEQKJJmuM89sQwicaXX1PgkD9J0A6cvarTMKrqjjQ-oZmVOifXNEaaac_3cPzwAKAv4lZInLuSLn56_Suf3uz6tYSHaZhy-qBJA5oxa8BDOolJgO6VWARJbFK_4nGpBnZkfDu4bjhqvo0aBDrgXclzU91oQTKNKwe9DM3zy9dDlTyIKpKw1dQaQRzdx6qJJa_cFD8X_RyA1LqoHc-XKTtq7VX-jBM5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGVYEmBKhfhtgL0UNsBLyisCNJhprD_qDab9zenLmcU18PmpXh_OBt5dhbspCj5n2oKFhTTeyJnn4jrUuSz64CJOO9AQRFfqHAkud6hT-oKx8ugqrlm0PTRLtOiyxIK0_YSqLzuQmDDgG7Nh47MKNVoJVQSJ7WeveNyARfo8I4JqfbOgxm5E5VXmE0qEex0ikSL_GdoUCgO-Kd_nPfaI53-mK37_2zd9OnpLBRpnioAn2wDRZOE7geiY1pouvRin5qJyE3N7MI3sbVgoNVppXPsmHIBF9n-fmwFxQ4XshTyZ2JP02Lp1sxKDkVt28K2_Bzcx1nYk4Xh2MZ6xUAD5cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/veQJ72ZKNYu1QmmSRH5mqdotwwcsXRHTn8hlml47tvRp14vwEU0eF4Yyly5urUfNcTXUwQOpzCtRIl4DRWKsOvxSTPIDcgRNydXmPrjn8uiGplOhInWuX4_XR-nF-gcWw9QUwKGftAHR1wlOHTJZD8miriPxEiJtY2hY_twiydZ_sXxE4JKzzjhikffcJNoU1IPufbRTlYE4q7Msll6C1YA3jsIiwXixDSr692Lcvk5xvvLvLZBCHA4I2Fa33KCaLC9yst6JwU4Gh-MyvyHN3u9MFoeqZCx7ZyFcIrMF3NxR4t1044fYPMsEi4nx5RQBySmkW0ko2hyA-_XMeqK2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sg_MfaiIy9RY8KybuaQHExDeet9lM3tyECZbti3nUJZhgEdnRC-PR0MnmAufWuqHteVnY02990uvzBhOBbVTj5x0ENb1wAJxVsP_ycYkkwG0XfKJnzykRdgmyxOVAD0ucnq1YWGMLgyeY3a_NaBAATbFJGEcrf-i_lrjlu_QVfPt4kxCABrbKPGqPwzZv-AfX5FV15MZocwxxoSORly_5aAuP2ObVjNfqhLgYz0DW6dn-ItQbZSl8N7f2TBgxeaSJOCDjWFKqsfn24TBgzVY_6VWbtghNZcf-gi0z_5nWDw3sAsNirvJjsXPP35YlAIk9a1aK1K9NWg_CCpjVJIq8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکم زیبایی از ورزش شریف والیبال بانوان ببینید تا خستگیتون در بره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/91204" target="_blank">📅 20:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91203">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye5y02TQk3fpjeNrDTNRERwlWfGHxCMRIIm2B8kMm3Ml02iykUmHEbvmdbdDbGgGmWUm9oaI3EHZf9rjWqsKYR9-k613WQzFjiCscNCnm3ExQ0d_SQZ65bQNj72ST1_BtTuu7yiwYJj-Rv-gHmQ4OHKOHw1r_kAe4QTba7OFpIQGdFUB3pMkHK0u_L3AFj21BuephScIJS9R_DkYWaRSXVgH184UQSaOTMBijHTSMsmljscwFT1PAbsFNWo_GdPcHCF2ZPwkAojiUV4iRvvKTpGNJn2GnaT5kvK36wdSncUbr_c481il1gN1kLOGNH21apSbLdZKjnvrh9ewvCFpDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ترکیب پرتغال مقابل شیلی با حضور کریستیانو رونالدو
؛ ساعت ۲۱:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/91203" target="_blank">📅 20:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91202">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D06zl9z2fKC8uzHMBS41g-W5zVnPis_QtKAPR6iUz1zkJ8995r8Iw-6yLNxsIRnIGzBP4m23WghN6oINtxfj3H1QcWh4F7ZKxweRn7yJlEADFstzSKybiyN4swofjrs78N4ig0u9iRSBSYdc4WF8qUCBG_j4ChzoiQ44MEklKa2GyB99FVY8EcMI_yMI9_uxrlnyjEcc2_HoRTI4Iw2SJyIk2bz3_Xcs0OCOTM-rm7ZrW9Y_fp34G9Y-GZBFpYS3tfZ58LxGuuPxvZVqQ9RFEKz2p-IKzWSJ_ihs5ouKzJgTw6wq4zVvFeqkzhg5wTwahdb62NW2tduKffR1JgH1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان رو نبینید برای آلوارز 150 میلیون یورو باید هزینه کنی، یه‌زمانی با 50/60 میلیون یورو میتونستید اینارو داشته باشید :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/91202" target="_blank">📅 20:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91200">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VU1-mIo_21j0jkjHWue0VuvG-Qeuyr-chSF6Pww9qVJPNnirUMI5_W5BzP-COo2ggJetN4cNyB85rw_1wHM7cGNfjo-TZs7jTnDoyaG2YySiGjqVCeSTcMxHA2SMZGCh8ahZ6a4c_f20rdovoFyotwHH488qgQT3MRvVespxK_U0l2W56oMKH46UFq99A3Mhkq04tHPVMRysq7dWR_jWlvU-kXoREhSepSMK35_0TCMoSk4J_fgt2vPFtaHBBQcIeuqE3Vp-FMynYwLNDOvZ-K4lM6oXzPJ1S_ad2FH5cOeH3c54UQfaC3E9XZzQgjicJqX-fLRuebgO7fVY2FvMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btkrSah-t9-6Kbn9x-e7JbnWCAZi1Ti-UR8XxVRXLY7rsE8fWMMssT1K0E3l5sf_ExhsWS0UMhAKgBaCpWxiPxIqvxuQeL5aes4naozp3KNRAfvSIlfDuUQme2ABCflAGKQRPoFVqm73aFIBqmfDn7qUx65o0RAxRg0ATNDLoE_K6o7gfo_SLBhSE_zeYGLUMwfhrVqEZWLVhA-VmPozPjIHvaewYRdBKGkElb8BhXJowrL8XwYQfydq2kpV2HO47SxbjujjRwIoxy18WE91W5L6xm6ez1Qhm_KHfK2Y8mCvA3FYw_vc3Ss1hbdkmeKWEK16BkwR6y1dGuUkFI1Nng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🤯
💵
طبق اعلام مجله فوربس، ثروت رونالدو به عنوان اولین ورزشکار تاریخ به بیش از 2 میلیارد دلار رسیده. ثروت لیونل مسی نیز از 1.1 میلیارد دلار عبور کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/91200" target="_blank">📅 19:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91199">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffdd5cda06.mp4?token=Oeq8dswyE6gUCSOqOhP8_EM81SSr9NBIXclxRdJIpcANfgk6IFIiUbSsXZfnxepmno7TUumtaPG3T9tQiNujAFxTOVAbAJX0o-Iossiz1iGKurJOV_vPhpcHuqko86CylQwGJH-lZ5iA4gnamLJ1LSz3oxMkYeUF405FKNGFx1hLDqjh84fjHvbMiAJn3B-TtlOQFhTUT57JR-RW6HToZpjR3kpGJIFRDCK0zHLhkCk5IKO0SuErlYoynJIccA2F2pWwpe6un9XXOCGk0IpL4Lcq58If9Hx6gi2oAr6LxkVonL3FWCvOyap-p8R9QGcLjZJUQJPtwh6JBOtrJd_hkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffdd5cda06.mp4?token=Oeq8dswyE6gUCSOqOhP8_EM81SSr9NBIXclxRdJIpcANfgk6IFIiUbSsXZfnxepmno7TUumtaPG3T9tQiNujAFxTOVAbAJX0o-Iossiz1iGKurJOV_vPhpcHuqko86CylQwGJH-lZ5iA4gnamLJ1LSz3oxMkYeUF405FKNGFx1hLDqjh84fjHvbMiAJn3B-TtlOQFhTUT57JR-RW6HToZpjR3kpGJIFRDCK0zHLhkCk5IKO0SuErlYoynJIccA2F2pWwpe6un9XXOCGk0IpL4Lcq58If9Hx6gi2oAr6LxkVonL3FWCvOyap-p8R9QGcLjZJUQJPtwh6JBOtrJd_hkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شما شاهد عادی ترین زنگ ورزش کلاس نهم هستید( همه تو دوران اوج )
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91199" target="_blank">📅 19:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91198">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cylms2QIEEhrWowzeOfNhKft_NEPPpuwGSoH4idbZnA1Czc0OgAxZk5SmcBO8IaKZA8NbZc9Sf4GJagPHm0R5gceQ54h0JKvIBDkvJDT4kGG4Pyj6Q6Nei85zBV3AZCwhPUwrq-BWCAJxagCFxtrtisyZyY_6lAbrLVkvBJDu0jpeWCuq2kCS_TgHnO6q2ZyJv-V5i5egYqo8t76VQMmxSp1kgzxmkNhj5vmjiqcXLRK28iOfkgUBpesJVrN4NzJTLA5-huF2DVsgvtv0PEQIn5afTh8XqOj04J3a3x0oIGPwwg2wcuXg4Zy2YhFx829JxvCRcrmg1dZhS7fVO-81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ساليبا:
اون زمانی که ما فوتبال زیبایی ارائه میدادیم و لیگ رو با رده دوم تموم میکردیم همه به ما میخندیدن ولی حالا دیگه نمیتونن به ما بخندن و سکوت کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/91198" target="_blank">📅 19:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91197">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtfqcT5F_Pf_uXv8WlnlO95caJ7NXUARNt7QW_79H4kSlcxPTgKOOJkhktU-5IdL4MpM_Tuu2wBxI8kDlUnhjQXEG9G9hwJ4QOxFGw-OQ8GUnhh4jQMUyfK3jh1yNoJ_u4FUY1fUpsUHtDIFsglTQlNlvBTRFpGtN94mFG68iLL4d9aTx5r_AZ6whFqiwJVQy5DTxbnISkjWR-OG8qINJxl1mWSR5-h2U00POkaaaUsPiaGAF0Bq45ZqW9_H93t7uyzk-ppIpnk0bpmvDCcHH_era-7nKSAohslTiEIIK2beS3WuLtMB-Vu9mOzt98kmr6v4tK8MgwThikH7OTMv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
🇳🇱
ناکام و بدشانس بزرگ جام جهانی هلند؛ این کشور سه بار درسال های ۱۹۷۴, ۱۹۷۸, ۲۰۱۰ نایب قهرمان جام جهانی و درسال ۲۰۱۴و ۱۹۹۸ سوم و چهارم جام جهانی شد
✨
اسطوره های هلند: کرایوف ( جز پنج تا تاریخ)، فان باستن، رایکارد، رود گولیت، کومان، سیدروف، کلایورت، داویدز، برکمپ، نیستلروی، روبن، فن پرسی
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/91197" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91196">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYudx2_QyoU0EZwfRIIuBe4xoG4Af8FoKKZuRxP3cOO9Z8_d9S9zz6-JNkVbXgK5a2png9z53-iUOLl6HzJAL5uZop7Mr9MEO5kLrpfA3s-WuzkwpNmfywhdaE1emmr6y3Ov1twAOYc2xNQ7bYjCbUJ2yeafj7ec_yg5PizSLiHNm2dvgXZ2dayYADmJsh-znTle3gosZxyrK0GPHPcvA0_mYfIOtk31eYtsJq7N3y9zbQLqnMScZnxNuxHD3GGwF_sV5r3I8xZSRe5pMPSK8eCgv6raE4hkypqZULURfSF-NoIY5yKsTgVs8R-I0gOue0athIzx3Du6N_1lt-8qbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
الرياضية عربستان: الهلال رسما برای جذب عثمان دمبله به پاریسن ژرمن آفر فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/Futball180TV/91196" target="_blank">📅 19:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91195">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nperU1tBOzcyCWfROGIO2tfL6zdboELNnYzHpo0RwQe2L4NMIufuSFi6ybNiQ2MfrdTt2Q_AzmlOcbABV2yaHY79dykn_ZSGQKb1NhFtXQ0hQNRlEGHukIFjOeUtftQ0iGbrgtw4Ok5L0bsglE3AxOaqsy-dqNuIafv3-jbLH56xfEkhYZA7rEEpPyTjLetb5CRM-_MJzf9-8XyUl6aB5jG9De-UAyCQTqRZehXDKVdF8O1aVqv9gdp2xvM-z03IN-zAeFKbhX7aQkTpkwhsYzOfjzTWIsDrD2TsvcP4Qs1r22uucGHWceXk-U6K9_m6LZRRA4f6byr1szTgzVgZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه نیوکاسل چربش کن
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/91195" target="_blank">📅 19:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91194">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10990086be.mp4?token=I1ENTcc8kn6w0_4-zdwRj48FcRdEMGeU5w47lheG4q2AVrs5NZX6aN-WxMFn_aSuOgBwNxNsrV943WugX1XI4-TwBeMJ1CYQfIBMqsYepoW_-KnrrJZY9Bn3K0_5CTr7wBUVzyTPMCI5AiE0vafaLLBIV-TOib_eA-2hKB2_ua_TRuz1l9rVx-g5R1PWDQs6pfvB0YWOfQgApbdr_FVw5A5wxS2c62NbGnC7FqeUOCeVQzdvZKiy0kso2KUhr-94Ze62tpegDBRdCuvfj6fOby_nTXz4oe_zBrkjHXfXAGlSEuTApKMy6rMdctbP0OazOgb6z1Lq_Y_O1UJCAzeTcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10990086be.mp4?token=I1ENTcc8kn6w0_4-zdwRj48FcRdEMGeU5w47lheG4q2AVrs5NZX6aN-WxMFn_aSuOgBwNxNsrV943WugX1XI4-TwBeMJ1CYQfIBMqsYepoW_-KnrrJZY9Bn3K0_5CTr7wBUVzyTPMCI5AiE0vafaLLBIV-TOib_eA-2hKB2_ua_TRuz1l9rVx-g5R1PWDQs6pfvB0YWOfQgApbdr_FVw5A5wxS2c62NbGnC7FqeUOCeVQzdvZKiy0kso2KUhr-94Ze62tpegDBRdCuvfj6fOby_nTXz4oe_zBrkjHXfXAGlSEuTApKMy6rMdctbP0OazOgb6z1Lq_Y_O1UJCAzeTcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🙂
چیشد چیشد ازگل؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/91194" target="_blank">📅 19:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91193">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
الرياضية عربستان: الهلال رسما برای جذب عثمان دمبله به پاریسن ژرمن آفر فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91193" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91192">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fab7e29.mp4?token=VILca6qm2gr7v7hNukGoqYpIsi2sVjPj-JoQbRKFUJUmkgQTTI_blDfIAOtZe9e1IS2CQwLzkeCcz4OZBDStKdPQ9vZhuiMmYVk7SpdQbQNAOGi0I8a99BgOt7IjRxMnt3hzgZe5Vc9zxTFKXMrZvmEgfg1Fu74n8u2ooO9K7P4IOm768CzeFaHIeUQ8LyIqimt5qzjhS164FxLY-c-6Kkhr5pkideuRfjLnOlb9SGGvWJk-k1PKbaKn07MXcXgN76buZHcUswoQ3T5biEhLgfLk4MG7SIuZki4-6ojW3WQ1_W_NIeaZ5s6mo-Qs3QcQTFX8njOs4roJQAnE081aZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fab7e29.mp4?token=VILca6qm2gr7v7hNukGoqYpIsi2sVjPj-JoQbRKFUJUmkgQTTI_blDfIAOtZe9e1IS2CQwLzkeCcz4OZBDStKdPQ9vZhuiMmYVk7SpdQbQNAOGi0I8a99BgOt7IjRxMnt3hzgZe5Vc9zxTFKXMrZvmEgfg1Fu74n8u2ooO9K7P4IOm768CzeFaHIeUQ8LyIqimt5qzjhS164FxLY-c-6Kkhr5pkideuRfjLnOlb9SGGvWJk-k1PKbaKn07MXcXgN76buZHcUswoQ3T5biEhLgfLk4MG7SIuZki4-6ojW3WQ1_W_NIeaZ5s6mo-Qs3QcQTFX8njOs4roJQAnE081aZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
اعتراف نیکبخت به تبانی استقلال و پرسپولیس در دربی!
‼️
😐
نیکبخت: اومدند گفت چون جو استادیوم بهم ریخته است بازی باید مساوی تمام شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/91192" target="_blank">📅 18:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91191">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tavvniJVoYpYUTjFq9885uX261S3BlX9HOUMxbQdBBkhdLWw8REHhYcnUH7rNsfBFn91pSECKHddL7psMdc8n1zL2Y7hA2JG5lGKcADhbBYo-qEdK-5gqs2Y4wxnWNSxCdrmYrK-9vzs8iqFCUey0UbjPzvT_kyvUc-_zlYtsSlUCPe0o50rTXqLigqlLq65TpyCUEJggrh4dk7sIUd5SCLLS1kUwhkelXKMufiZnW6sK5DmQm2z_pHwXFuPaXjqdJ0yz-l2F7aW7nB8f_i6Q4ZY9O_gL8TctHPzLgs8tx9xZZmQk4ZWca354c4d5sYImdktiDafDbeTDND5fxhozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع خیلی خیطه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91191" target="_blank">📅 18:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91190">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یحیی گل‌محمدی لژیونر جدید فوتبال مملکت:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91190" target="_blank">📅 18:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91189">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnsZ0G9YnifIfawEQkt5sOQxP7da35yT_rLafmTb-4WsBn65AmDY7qf7QMr-TbjEacTmwrKgGWkpUt1faY52Vp7pegnpV2zkqqq23Zqkx4zZGQuerL9DWUHeKZ135kI-C4sh6HbGaf1zLFCT-M71ifvdQusneZdVRkdFg4s4XEUIUUacXxKPqSAEL1iRLUMkxj5Ok-s7ox4RDz7KP119mtXrevJx5JFSwRFcgKTNsc3sNgyGgoR9_7DtW0JJAhDqZJ8kEkqSYw2d2ZBrOWWM3r8c16iuQwjDat4i1DUgAEK90i0MzBh1Y5o1pvGjM3vAnnRfCQMiXckO-6to0QSb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع خیلی خیطه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91189" target="_blank">📅 18:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91188">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3kwhqAr6Q68ltTL7-HgJxw4n2AM_vdN_jGg60Ix9KJrJTTj7OMNM_ztg573JecpjGbjXGoZ8hSmim0iViDtUkQi_RqqMYqrKGb6fhiaaeEj-36cz2xEOe-9wgzG35bFkmHKq1lqFleyUli_RUSoAQCgRONEOmWVvTwtf_zgm0jOxAptYwS_op4lbYGa_qKEy9ukcY6x8spn9dBl4kghk7xbbVYzJCHIYyKtp_Cwd_pwhg0YIMRC1pH3jUBSC2x1W55l70gzyAU8hLkq8Latwpi_W6xr7p9LkqEa8G7l4w5HdmHHbaO-EiUz6sAOLDj2ytJyJzkcF-8tuwb2kEz39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
به برکت میانجی‌گری(همون خایه‌مالی) برای جمهوری اسلامی، اینترنت جمهوری اسلامی پاکستان هم دچار اختلال شده
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91188" target="_blank">📅 18:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91186">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzodrfXq9K2uEAqck-oe9IWlVPWHLFjyARqwus6tOy6GdDIEHs5WdLuVpsveRWlKGV6xb_b5DEAgWJJrz5c5JV748_hYXte1LRm2e7DN1hxYot_IPx3jAFSZSTJeRS-KidiQ6-avqERwpPEO6ZsDvsTKO7ieK2MGZgMZTsjQlFAhDF6qkBMZ_A7tpoVWmgAVZPedrKd_b3u7Okpbtl6As11ukTwf-H4ASXLy-0IAMkE2vcjIgMb4eFMHAoXrC9bACXdQS6PseVoA-9lHd8KzqBl4EUsa8yqXScCd0elpOQ-apf1QzJz67ynyW0Y4ZbYnFRQVjK0EWtzI7Vr-wfb5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلث های سه نفره خط هافبک اسپانیا برای هر جام جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/91186" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91185">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niVv6pxQ0GH_Av_2qnECyvpVGomw2GpdwIrUMmuk1KHd955QxM3ok3QvCPhHykp796YTUzFU9EgsuKqS6vSRcCLXY-nyVDdxG3wPofP2TT_RGSxMiTryDWRCusaj5cAJ4jXLAMqhYltrgKBIXHaYXXimSBx7SF60H76Ktlo1TOFfpgzoqoiWnnfM8tPBOlKVLDrzX-woX_ADyukR0m32jFXWgLn_oC9b2JXsk0CjtCEVk2Zb29aaXQLQ_nJOvLPVn7DUAkrGdlng6BokEZ0H0u6NZdpZmVK8_d6VhcwbRPMvue7VlTEuMCOwdfwdE8b6jAiRTLLXAvjqpHlG9IEqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇷
❌
#فوووووری؛ لئوناردو بالردی مدافع آرژانتین روز گذشته در تمرینات دچار مصدومیت شدید شده و نمیتونه در جام‌جهانی حضور پیدا کنه. بزودی آرژانتین نفر دیگه‌ای رو جایگزین این بازیکن میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91185" target="_blank">📅 18:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91184">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d61c1cf6.mp4?token=aLUO8msBLUauVmxSADwspkcpLSxzfGK0Qc4I3dfwnyLT4so0Ejth0PNQR5HGCBlFZHFco5xDZTd1Mtuu16yvxcSxojksCtivATbqbJyyEO74pPbq1rDL912HGrS7SMNqCfNCElUo1eQ4T6CbP1VtCVXOLIK1Ag1zLgYAIXhKt-At47xh-bqWPc6VKYRsXIgv11eMjosXpSNJHG6lTbaFaJvkLlazVtZ08VtaHzPp0QQZrWJqF85qT5OpdkM1EpHb4UWbQr8KRsz_Hxzm7akMDeEmbWqx7L2gkghqxRnfOwr3NPtYhEZhib1Y_vSNH00BTIL-lX3pcfmBmzRnDQHFIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d61c1cf6.mp4?token=aLUO8msBLUauVmxSADwspkcpLSxzfGK0Qc4I3dfwnyLT4so0Ejth0PNQR5HGCBlFZHFco5xDZTd1Mtuu16yvxcSxojksCtivATbqbJyyEO74pPbq1rDL912HGrS7SMNqCfNCElUo1eQ4T6CbP1VtCVXOLIK1Ag1zLgYAIXhKt-At47xh-bqWPc6VKYRsXIgv11eMjosXpSNJHG6lTbaFaJvkLlazVtZ08VtaHzPp0QQZrWJqF85qT5OpdkM1EpHb4UWbQr8KRsz_Hxzm7akMDeEmbWqx7L2gkghqxRnfOwr3NPtYhEZhib1Y_vSNH00BTIL-lX3pcfmBmzRnDQHFIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
🇪🇸
خبرنگار
: رئال مادرید یا بارسلونا؟
👀
پاپ لئو
: پاپ برای همه تیم‌هاست، اما پرِووست برای رئال مادرید است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91184" target="_blank">📅 17:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91183">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇮🇶
🇺🇸
#فوووری؛ آیمن‌حسین ستاره عراق دیشب در بدو ورود به آمریکا حدود ۷ ساعت در بازداشت اداره تحقیقات و مهاجرت این کشور بوده. اتهامات این بازیکن ارتباطاتی با گروه حشدالشعبی بوده و مورد بازجویی قرار گرفته و سپس پس از ۷ ساعت آزاد شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91183" target="_blank">📅 17:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91182">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eda27170e.mp4?token=s1fguAUaFCc91Ga6Lazh7rUCB0ssxayVxqN2qcnPmOEfM1wZgGl2mn3YOWDjg_QK-0P7pMwVUa3M3ci3Bzoa5dIhAe_xAqKkIiCShsdgzhkfQX8YzE7AdUJg4-V3aQH1NVQWyFbZWOYrRQ3Zk1SEaeR-Sc9wy-AiK-O5_rbnqSQIC4Prt131R78CNSJc37X-1HI7H2ukkAk2CMWwvzQdPxvGlLgE8RHMl3EXhWXnBzpebW7BXCeC3YLsyF7AEz5d0o6LooZDuesNXQSoznmeDRu20MfGdBCdPAE_0Ob_7YVk6XYoUleeG1_cOV9ElrJm8fXg2IqBtRYYo3Fwp-xCAGQq-IG6m6pPEdFLClw3WjEdvy7cqO1ooNX-d99QHcMuPSsCEm3-zk2t9hLbhpnsrA_RXE-D3UP1rOCSbTd0zD_Ihm0bP61kUncpYWHpc4LO2mxToxILWDUesL7_Am56KlpJUPBPTUYuRMpOClwiw0vQkHEWf-8sAMXP_T5zYn-jTtGO7kCiMpWwQPMvS2DOgi6a-wSRgAaQP5ERwOMYzhRFf5GYSHhNdHplaBcPz9eivvkzSbNp9aXJBNLDg10Lf0_IKWh4nE1MoWRCzXeR5QaLo6cdjqnON8E9p6a9IXXF-uGcSJvD3gMkYnGkmRGgEXzPhZnhaTfCx-ZuI-VhWjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eda27170e.mp4?token=s1fguAUaFCc91Ga6Lazh7rUCB0ssxayVxqN2qcnPmOEfM1wZgGl2mn3YOWDjg_QK-0P7pMwVUa3M3ci3Bzoa5dIhAe_xAqKkIiCShsdgzhkfQX8YzE7AdUJg4-V3aQH1NVQWyFbZWOYrRQ3Zk1SEaeR-Sc9wy-AiK-O5_rbnqSQIC4Prt131R78CNSJc37X-1HI7H2ukkAk2CMWwvzQdPxvGlLgE8RHMl3EXhWXnBzpebW7BXCeC3YLsyF7AEz5d0o6LooZDuesNXQSoznmeDRu20MfGdBCdPAE_0Ob_7YVk6XYoUleeG1_cOV9ElrJm8fXg2IqBtRYYo3Fwp-xCAGQq-IG6m6pPEdFLClw3WjEdvy7cqO1ooNX-d99QHcMuPSsCEm3-zk2t9hLbhpnsrA_RXE-D3UP1rOCSbTd0zD_Ihm0bP61kUncpYWHpc4LO2mxToxILWDUesL7_Am56KlpJUPBPTUYuRMpOClwiw0vQkHEWf-8sAMXP_T5zYn-jTtGO7kCiMpWwQPMvS2DOgi6a-wSRgAaQP5ERwOMYzhRFf5GYSHhNdHplaBcPz9eivvkzSbNp9aXJBNLDg10Lf0_IKWh4nE1MoWRCzXeR5QaLo6cdjqnON8E9p6a9IXXF-uGcSJvD3gMkYnGkmRGgEXzPhZnhaTfCx-ZuI-VhWjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
🇮🇹
نظریه محبوب:
جام جهانی بدون ایتالیا اونجوری که باید نمیچسبه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91182" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91181">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtAhMJK_b_kRXss01GVdsB15BpqzMKAFRfFUHvEiyWgD0iMqDF9f1Hh31xxOrYySv10XNAcLdZZb8OfQ6T1ZRqaUqTejhtGRpJB1sTNqg8t8frl_ipxqBe7eWFH7TNqdovC5VF54wcigvjszlWsXHC4uSlmXU646sDXx4ZJsjSg-8_8j83IInYyu2VBTZZ4kaJgtzyXnN1lilXdT5DkMFcyYHCvoNa0je6BRvJZnf_ZSSjd0UqsAGgqDaMs-idmJqVzshBSWUICUdKyZl2KQUpwvhlj29D1XSpU0OutZJs_qm-LmznMuTAIaRsHnKPh_10QPeoKICw3lsP0NPepCMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙️
پاتریس اورا: «نسخه پرایم من در مقابل لامین یامال؟ من او را زنده زنده می‌خوردم. متأسفم لامین. دوستت دارم اما از کریستیانو بپرس، از مسی بپرس، از بازیکنان دیگر بپرس که موقع روبرو شدن با من در بازی اصلا دوست خوبی نیستم".
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91181" target="_blank">📅 17:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91180">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4803f256d5.mp4?token=pUbv8IpFGP8nNMxqtJGmh-xiJBalLw1QVeNuNQgEryQE57QWICBktheQT606UWN2L6-3067Wgy0pUOLsWnbKH_UoFF7JaRut9cLRQrtd8frXxs2pVt9yfofBnhF371UnUiAOAEjnTlumJgSf3dcgk_0niUrhcjug8J1qlIseQJB6-ISKFWwLyfubZy9nvmzcXhMCCr9cSQOF-lLylZpVJmn4KCk8Skgq4Qn0SuZMLhRdfb2ahhUlI0zmxH-Gn-Qu0sPGykeyPO0_fVQMTSgE8Kn8Lb7aNDJT686BtFOnphBrjLmLpCD1eCxHJpO_NO6MrFkotwZxgMHMofM-rlwuog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4803f256d5.mp4?token=pUbv8IpFGP8nNMxqtJGmh-xiJBalLw1QVeNuNQgEryQE57QWICBktheQT606UWN2L6-3067Wgy0pUOLsWnbKH_UoFF7JaRut9cLRQrtd8frXxs2pVt9yfofBnhF371UnUiAOAEjnTlumJgSf3dcgk_0niUrhcjug8J1qlIseQJB6-ISKFWwLyfubZy9nvmzcXhMCCr9cSQOF-lLylZpVJmn4KCk8Skgq4Qn0SuZMLhRdfb2ahhUlI0zmxH-Gn-Qu0sPGykeyPO0_fVQMTSgE8Kn8Lb7aNDJT686BtFOnphBrjLmLpCD1eCxHJpO_NO6MrFkotwZxgMHMofM-rlwuog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
تفاوت قیمت خودروهای خارجی در ۱۲ سال اخیر
اینجا هم قیمت فرغون تو یک سال از ۴ میلیون به ۴۵ میلیون رسید =))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/91180" target="_blank">📅 17:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91179">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa0DbPYTmuxiy1803XSQkptsmAWFK_KABhyygWqgkKVZArLuyEbCdRawQVa0zOFHTtZWge0clnXHbZgPJvGGFofTCTS3X90eGZgjAMR02Y4Eclg3Ju_DMdxLsHj9x5LnhWZ0Ftx54SHywpPmm0pAHq-J7-wj2uYIpL6dMWq4RNPX5J5LUfhb2-cUxaXWQ_2CA740JT0vQn72HJBYTDs5eodDbN64ZrHCwet1XJnhNVL7H_KocoKUw35K7yrwtWsRbiWr3_qU5GsZKmXHW9T8OQh1TwUJ-6NAGrpTjuNp4lQFfaGuVxLx-WQHCS_gkSSAJR1ztczVUFLTS-h7NxSy6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه این دوره هیچ‌ تیمی تصمیم به شگفتی‌سازی نگیره و ضدحال نزنه یک چهارم‌نهایی احتمالی این شکلیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91179" target="_blank">📅 17:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91178">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecfebd678d.mp4?token=rWjpFJk581PcAhvINH_N-4XaCKgsL-gqEEyexsOHWLVRYP_yGxZlOc3jOr947h3yuf3vMHUvgh8KadcG5YkOBTll1l-uoGciVtQGHPFemuLHehvq42or7auGCkpreh3rbPu94AuL5-9TQIrDndey8k0eANCHrQaOEB06XA0eoZGWIn6RvrulACrVWMRXuBDLBWkbnfUjg8btanjfNnmtcUPcMzx9rE_zMnKevf255ljsYBZnLAw-ABL1hOnytMxX4Vb3t9ueF_Pu78ECU1hlrxrLnuA8kcHeIuzt1Hu-j1Z29-9srnL7FB_DVeM3SzQL6lbB_TAi7_ng0WwSVSRkZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecfebd678d.mp4?token=rWjpFJk581PcAhvINH_N-4XaCKgsL-gqEEyexsOHWLVRYP_yGxZlOc3jOr947h3yuf3vMHUvgh8KadcG5YkOBTll1l-uoGciVtQGHPFemuLHehvq42or7auGCkpreh3rbPu94AuL5-9TQIrDndey8k0eANCHrQaOEB06XA0eoZGWIn6RvrulACrVWMRXuBDLBWkbnfUjg8btanjfNnmtcUPcMzx9rE_zMnKevf255ljsYBZnLAw-ABL1hOnytMxX4Vb3t9ueF_Pu78ECU1hlrxrLnuA8kcHeIuzt1Hu-j1Z29-9srnL7FB_DVeM3SzQL6lbB_TAi7_ng0WwSVSRkZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دم جام جهانی یادی کنیم از بزرگترین غایب پرتغال
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91178" target="_blank">📅 17:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91177">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09753bd04.mp4?token=FDojfLiWFx1uTgjnaWg698HjfkxqTvYk6j11ZEdrHXMQJozf5qOvsnUYm_N_m24xTYNa4vo711J9nAHV6P1BRLWa_r-DAm6eEDSl_jRG-q6aDPDvodIxnNQ_ltUIanZI7k6rOAYtK0zuqWjpNM9Tmyd_Ho6zR7RaMMwPB2EBhiSHY4_cPcU7q1RzpqQBIS1ByBkbSl2zjnVeVopxSjQUX-cegnQDtk1UCti_9jJlNca1nJgpugH3ty2w8p9yM3BxOZwSrusWXtGks_aJj4FPwg3Ng3FHYIkTJI7JsU4mS8NO46fkP8YRafrb2c7dHx1EJhLhqNZbG8Oclip2ZzYNGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09753bd04.mp4?token=FDojfLiWFx1uTgjnaWg698HjfkxqTvYk6j11ZEdrHXMQJozf5qOvsnUYm_N_m24xTYNa4vo711J9nAHV6P1BRLWa_r-DAm6eEDSl_jRG-q6aDPDvodIxnNQ_ltUIanZI7k6rOAYtK0zuqWjpNM9Tmyd_Ho6zR7RaMMwPB2EBhiSHY4_cPcU7q1RzpqQBIS1ByBkbSl2zjnVeVopxSjQUX-cegnQDtk1UCti_9jJlNca1nJgpugH3ty2w8p9yM3BxOZwSrusWXtGks_aJj4FPwg3Ng3FHYIkTJI7JsU4mS8NO46fkP8YRafrb2c7dHx1EJhLhqNZbG8Oclip2ZzYNGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
پرنسس لئونور دختر پادشاه اسپانیا که آقای گاوی زحمت کشید بهش پا نداد، بلند شده رفته سربازی و اینجوری داره فشاری روانی از دست دادن گاوی رو خالی میکنه
😂
😂
😂
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91177" target="_blank">📅 17:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91176">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH9yMoz5DGsLtTXHz37BErYCGv0-H8dQltC9Oga7eUCtsoIJGEBrVcQoMa1A6JMjVGM4jTuA2fRQ2VdeiVziRGtUPAO4UnaY8RrDdTl5sgCzRt8ivxHaZLePrUFAJwNBoJSxlM_LgZxwk2XGnHCLiEoaQb3aNwmiPw-4LZS9adYIkEeZiYaFwT13lDO9Ui5Bpzx4l_SHpJka23zh2mELdOSy5NZEq8a2h6_7A6xobk9NDxZBm6s62Mjq2fp63vUKNVu-R2EQPHweHOeNMYI4WmGfCbNCnKsKZRFENz2CncAmM8dXU4dWIrzxCfuhbLrUbVoavOvHB-pAweyfITGC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
از مایکل اولیسه خواسته شد تا بهترین بازیکن فعلی شش کشور مختلف را انتخاب کند
🔵
مایکل اولیسه:
🇩🇪
آلمان: جاشوا کیمیچ
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلستان: هری کین
🇪🇸
اسپانیا: لمینه یامال
🇧🇷
برزیل: نمیدانم
🇵🇹
پرتغال: برونو فرناندز
🇦🇷
آرژانتین: لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91176" target="_blank">📅 17:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91175">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c576d4593.mp4?token=MjYADQQfGq0Hm5dzwaC3gpH84FxbvB-IBR0dGdbFPLtqZdShrRzMS8bA7Ql1nFvpVhaedQgMt4imr1peFnlh8mcwzP7f-FkHLlIqK1ssvuC7h28tuaNjtqapu6X79P0tGFfoecKIWtvX11af2jbSwdQK5urvYv2O-ij4razgBJqyDihbPyyPHBJukwuK8dGeSm4C2NW9WVRtHUrY1-vPoi9xDibZ7YBGWvWICMZ4End9XRJq591vhfZNzPhTbg9qYgym1XBnAk2usLkOlcYcdqUwn4brfKT1WJzAddUyVSBJMGB2JJYt3mqLbztcz2U-WWqQKcGF0kkw-i7q54n7CIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c576d4593.mp4?token=MjYADQQfGq0Hm5dzwaC3gpH84FxbvB-IBR0dGdbFPLtqZdShrRzMS8bA7Ql1nFvpVhaedQgMt4imr1peFnlh8mcwzP7f-FkHLlIqK1ssvuC7h28tuaNjtqapu6X79P0tGFfoecKIWtvX11af2jbSwdQK5urvYv2O-ij4razgBJqyDihbPyyPHBJukwuK8dGeSm4C2NW9WVRtHUrY1-vPoi9xDibZ7YBGWvWICMZ4End9XRJq591vhfZNzPhTbg9qYgym1XBnAk2usLkOlcYcdqUwn4brfKT1WJzAddUyVSBJMGB2JJYt3mqLbztcz2U-WWqQKcGF0kkw-i7q54n7CIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
روایت چلنگر مترجم سابق برانکو از تجربه همبازی شدن با بهرام افشاری در مرد عینکی: بهرام از شدت گرمای هوا، نزدیک بود بیهوش بشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91175" target="_blank">📅 17:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91174">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
#
فووووووری
🔴
حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/91174" target="_blank">📅 16:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91173">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZy6rnjtkFjnXXyBtDggwE8uHAl7Uzg5w9pf3Z3N-dBjd90y7xGBghJLCenXyS5f0I7S97zzODdXLlMzCgpzeKZQ-n7LYyeYbLr07UNTqUnCSQPpcL0tL-VsIbKiP9QyzL2wxG4NeCEKUXl9tIr0XlLY1GWBeejL18swA-jyNp533IE2HQmBEbx6DpEvdm-u5B4el_wFWNQABOy2WbMHxk7EZzEg8BT6eYRAmhH5j2rbeZeN_9KFKs9kJCBQq1B_EQiPcAspFUt0iQhpSgFLm4S0hhIBP5PyRzlHC4DNIiMtvKyY1zZ7HO6kt_C-S4FiqWH_LLz408jMWWwZ5nnpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
طبق گزارش امروز لكيپ:
❌
تقریباً تمام بازی‌های جام جهانی (۱۰۴ بازی) ممکن است به دلیل شرایط نامساعد جوی، در حین بازی به طور موقت متوقف شوند!!!
❗️
احتمال وقوع رعد و برق، تگرگ و حتی گردبادهای قیفی شکل (تورنادو) در مناطق مرکزی ایالات متحده مانند کانزاس سیتی، آتلانتا و دالاس وجود دارد.
‼️
همچنین خطر گرما و رطوبت شدید در شهرهای ساحلی مانند میامی و هیوستون وجود دارد. در حالی که مونتری ممکن است دمای بسیار بالایی را تجربه کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/91173" target="_blank">📅 16:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91172">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAq90tZ2rNVUTsMmcf6gv0owP1F-ZX4_V0OTO-He1Ifwmtlb0txzUSOZFMMscdsIaOt0VK1X0k0Fb5ozVbyVswkE29dazb_Xj1SpxlysMQPv-IAzqgNKh43cUhi1Wn_hKHLDVYag6u_fC1LZCfi3T-JAfIqkFRmqwmK-lVRpkbz3w3pV0XsWjA3HlDzpTy-eE2vhzhrUpH4BGp16qBKPhXe0k9qHo7wGfaR6umho5O6K1OS_5YZYxeGwGy3D-GkM17REx2yeEjRecl6dG9YCgROA5d37t605VPqYdR6L3XbQUet8frpVtk8PMzjXt79MU3L6XuoSk0i9o-BGxygI1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
معرفی‌مختصر تیم‌های گروه B جام‌جهانی
🇨🇦
کانادا
:
لقب:
Les Rouges (قرمزها) / تپل لیفز (The Maple Leafs)
ستاره‌های اصلی:
آلفونسو دیویس (ستاره بایرن مونیخ) و جاناتان دیوید (مهاجم یوونتوس)
سرمربی: جسی مارش( انگلیسی )
تعداد حضور: ۳ دوره (۱۹۸۶، ۲۰۲۲ و ۲۰۲۶)
بهترین مقام: حضور در مرحله گروهی (تا به حال موفق به صعود از گروه یا کسب پیروزی در جام جهانی نشده‌اند و به دنبال شکستن این طلسم هستند).
دوره قبل (۲۰۲۲): با وجود بازی‌های خوب، با ۳ شکست در مرحله گروهی حذف شدند.
نحوه صعود: به عنوان یکی از سه میزبان مشترک این دوره از رقابت‌ها، بدون حضور در مسابقات انتخابی کونکاکاف، مستقیماً وارد جدول مسابقات شد.
﻿
🇨🇭
سوئیس
:
لقب: Nati (تیم ملی) / شیک‌پوشان قرمز
ستاره اصلی: گرانیت ژاکا، آکانجی، زکریا
سرمربی: یاکین
تعداد حضور: ۱۳ دوره (یکی از منظم‌ترین تیم‌های اروپایی در حضورهای اخیر)
بهترین مقام: صعود به یک‌چهارم نهایی (در سال‌های ۱۹۳۴، ۱۹۳۸ و ۱۹۵۴)
دوره قبل (۲۰۲۲): صعود از گروه و شکست مقابل پرتغال در مرحله یک‌هشتم نهایی.
نحوه صعود: صعود مقتدرانه به عنوان تیم اول گروه خود در انتخابی قاره اروپا (UEFA).
﻿
🇧🇦
بوسنی و هرزگوین
:
لقب: Zmajevi (اژدهایان)
سرمربی: سرجی باربارز
ستاره اصلی: ادین ژکو (مهاجم کهنه‌کار و گلزن تاریخ‌ساز) و ساد کولاسیناچ (مدافع باتجربه)
تعداد حضور: ۲ دوره (آن‌ها برای اولین بار در سال ۲۰۱۴ برزیل حاضر شدند و این دومین حضور تاریخ کشور مستقل بوسنی است).
بهترین مقام: حضور در مرحله گروهی (جام جهانی ۲۰۱۴).
دوره قبل (۲۰۲۲): غایب بودند.
نحوه صعود: آن‌ها با خلق یک شگفتی بزرگ و حذف/شکست تیم‌های قدرتمندی مثل ایتالیا در پلی‌آف سخت قاره اروپا (UEFA) توانستند بلیت خود را برای سفر به آمریکای شمالی رزرو کنند.
🇶🇦
قطر
:
لقب: العنابی (عنابی‌پوشان)
سرمربی: جولیان لوپتگی
ستاره اصلی: اکرم عفیف (ستاره تکنیکی و آقای گل جام ملت‌های آسیا) و المعز علی
تعداد حضور: ۲ دوره.
بهترین مقام: حضور در مرحله گروهی (۲۰۲۲).
دوره قبل (۲۰۲۲): به عنوان میزبان مسابقات حضور داشتند اما با عملکردی ضعیف و سه شکست پیاپی در همان مرحله گروهی حذف شدند.
نحوه صعود: صعود مستقیم و مقتدرانه از مرحله سوم انتخابی قاره آسیا (AFC) به عنوان یکی از تیم‌های برتر قاره که با پشتوانه دو قهرمانی پیاپی در جام ملت‌های آسیا، با اعتماد به نفس بالایی صعود کردند.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/91172" target="_blank">📅 16:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91171">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eze874oKvzeeV6rZsu8UimAKgaQs9CUNoyt5RLeLivrQdUBRv3fVCE9p4ogxodSuS5zlhySnT8pSLbEdua1NAMeQ-avcz_cD7sTSNf13IH7i6TKZyUefZMACE9H6smN_tTU7tbvHjR9BscibUQ5PjljJLoIT9QsJmXlJ0bEW4sBf3u22zPDAyH_qJrTdKclWE3ieywNvgvZWqjRjf4qmXyVsAC4bk-8nHRoTuJlvnFhJ2kx0VusV4ZY8irWrIKeIG5k8c6vSUd7mj3FXRmtOsZp14s3yueUuu3mpAI7fXtTlckR6gKetTJw1PJGtoMQwBiGlKcA4_nrfJcyWeVhRmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس‌تیمی تیم قدرتمند اردشیر قبل سفر به مکزیک
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91171" target="_blank">📅 16:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91170">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG20bGYtOsMAmI6NJC60K7xINxjJU1H2-xOT5sKUCsFEhEpWZituejSUX-lndouwaDJYNsNopW-aVKKHINJnlCoe0OdRJTP-lRHe6ZWk5kS5X-J8D60DYeLm3T-O69pbPXTE-9JPgo-pCtto7MFPtVS1Vn_ffW0KIfN13UjLI2VZeKK0XA52MSFbzUYnsH6XQtnTV_P-LRya9vgtNKfutpbxvEA7lxYsbGvwJMwIC8ugawYK_Gi0-VMzIdGucAoPchgAGqgH_MhjvcnnzdKQx-cFHGiRsNY3TMADSgA8MVgscVwKrtZO-qT0IksLvpfNZdhCfAZ-tUk_q2CwTH1A4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامان قدوس تو عکس رسمی تیم قلعه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91170" target="_blank">📅 16:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91169">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mNrOl_xbyN2sAqTRvpWPzg3rPLPDwgsfRpTGKYtNDgG5q0ZmlXtmlk_WdfULtEpQHgGgAZdrzkoDK3Ae8hCijpfAwTdSfoCDBS8gpGF1ViNbjU7LBMso3WrPwI6FJKy_SQ-Evc77TmF3bD0tICEQUa2RTsBpyWS3xwJeONSR0v2vEBX-0Zq9_buMTFHLzqFukDjdWfx3PX3ZPdcrjGV91BA1UUydC2vHYtPQixdFSE91OFDLnkEKHmousAaoHjDn8GJ3CYmoyGkgTGi_5HDtWdAdNA_mkY4UKUaL7XwjfqMWNmS1DuZOSq0LXb2RToz65Uvtq-Rlj9uLesvatnTDhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
؛ به نقل از موندو، دو تیم سیتی و یونایتد خواهان جذب بالده از بارسلونا شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/91169" target="_blank">📅 16:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91168">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a405dfd62.mp4?token=vKp76OEagXc-Zsuxbi7i8i-BRqSQlm-jhuGME3GFmt9UMO3rArhcmkP9G4WZ_8uK9NZnfnLzcorY0RJ36-GtiE9_DMq6_Ca85UcdGVW0sHS-cY1HQAJGBmZp_H9VAyvdLbyZCisIHpbzJ6XtVN4laD9bMQJbP9BPsJOsQ7akV64ubVpMQsRWRK-nkRgeUihonqvhM_X_0mNjQlu30Hg0-gQXR2tmzvSBipmCXZOU6xiktfCcxz_Q611Li1ndJjbyAp7HFHr9yhNAgryc6oVa3hrKB-B0NsFUg0ZsEwFyNaGB7P1r45i1nxmkCEFMmiojbp57hrUKp9PTAaMhUAbYaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a405dfd62.mp4?token=vKp76OEagXc-Zsuxbi7i8i-BRqSQlm-jhuGME3GFmt9UMO3rArhcmkP9G4WZ_8uK9NZnfnLzcorY0RJ36-GtiE9_DMq6_Ca85UcdGVW0sHS-cY1HQAJGBmZp_H9VAyvdLbyZCisIHpbzJ6XtVN4laD9bMQJbP9BPsJOsQ7akV64ubVpMQsRWRK-nkRgeUihonqvhM_X_0mNjQlu30Hg0-gQXR2tmzvSBipmCXZOU6xiktfCcxz_Q611Li1ndJjbyAp7HFHr9yhNAgryc6oVa3hrKB-B0NsFUg0ZsEwFyNaGB7P1r45i1nxmkCEFMmiojbp57hrUKp9PTAaMhUAbYaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
وایرال شدن عجیب و غریب موزیک شکیرا برای جام‌جهانی در سراسر دنیا؛ واقعا محشره و همه نسل Z باهاش ویدیو ساختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/91168" target="_blank">📅 16:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91167">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGybo2KC-z6uGfMMNxMyqYLNl79Mv2oSIV0y_K--wVvMTGsoma2_yxlcShbhSkWTJT2R-xzBm828ZGpro96_rFMRScjOPBT3daw4sTi-i9a00YtmaJIGz4LCv5dHx2ksM9UAeBjHS-O5clyrr2YLWkRJb3-xw0USU6aPhsC2_nCb1BYgP8Z2KQTXH8I8j4uCs4TYHeoVb4_gcyfauASfu2sxOqyKPFX-X38Yepg-g3ebTRqE1mi4r8YG2WJvQAJ5Y09Rosu_7a0NgXpSd3g8OBPViOoY9EiPRkcXfzwknJJ3KjdQjWNLKum7ZT6N4Mpjdi3Z12u9k3oBKxZEwYTtOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇸
🇪🇸
فلورنتینو پرز: عمرا بیخیال ماجرای نگریرا بشم. انگار بعضیا حافظه‌شون خیلی کوتاهه. این بزرگترین فساد تاریخ ورزشه و من تا آخرش میرم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/91167" target="_blank">📅 16:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91166">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5532e9c9d8.mp4?token=NDsX7J9MeFAwUYuuXZD5Xs59P6sEqhyEixoSsDskKAPxEnkmR3W8FKTPL_B_tQaBDmtqB8jRNd8-lDmmZMesATD7pVlwQXd3DFx7niC_cm17dFcaeazhEhLynfpbQ9QkauqvvGIthqeM89ExQY8Fa97zdfUlizx_QWx8ChuNqjogg_ySsoGL1MNL-ZSXZEgOuik-19lgbny5W3tr9eW0vSfs8NajGZ0dgm8Qw8DTko1KHnz4DBHWhW6DbGNhcU1UguD_YsiwRjCL4NJaCAXWsXM94L3dsb3thrMvSUpGiYNUJ-eLq9HHhr96K1SMTEzc3wSh256pUu-QWJtHWYFiSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5532e9c9d8.mp4?token=NDsX7J9MeFAwUYuuXZD5Xs59P6sEqhyEixoSsDskKAPxEnkmR3W8FKTPL_B_tQaBDmtqB8jRNd8-lDmmZMesATD7pVlwQXd3DFx7niC_cm17dFcaeazhEhLynfpbQ9QkauqvvGIthqeM89ExQY8Fa97zdfUlizx_QWx8ChuNqjogg_ySsoGL1MNL-ZSXZEgOuik-19lgbny5W3tr9eW0vSfs8NajGZ0dgm8Qw8DTko1KHnz4DBHWhW6DbGNhcU1UguD_YsiwRjCL4NJaCAXWsXM94L3dsb3thrMvSUpGiYNUJ-eLq9HHhr96K1SMTEzc3wSh256pUu-QWJtHWYFiSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پارت سوم ورزش در خانه؛ حتما استفاده کنید و واسه‌ دوستای گشادتون بفرستید
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/91166" target="_blank">📅 16:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91165">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea44f33918.mp4?token=u4Lo5qNLCIn2MkovK1gaZSIWp3juR4wqZpkPHEMIghb78UEtoBzGJDUAjr23vPr-vx-TEz38_ibOpd12ZaXJx_egHXzS_GKfvkpdgFGRwCCEw_mZ1__7SkjcpsRGtQdNjfyQyWm5QX09weIDNEVxubQDWDNauYTBpysAhzSjkioE46b7G8hFzSR7xCKVFJP158qobV13fMvqtA5r_QdS_lSRtv6dT9-UH5M1SVqHUbQTuAqVXzGOD3gA4gYMnnYAKCc1youpn6RtBBXBajwaQ6DcAMgpKioRfQaPKy0OyrA1eFYdoRHtZ1f6sPGpb_WmnV46Tjvx2V52_jQeFlnKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea44f33918.mp4?token=u4Lo5qNLCIn2MkovK1gaZSIWp3juR4wqZpkPHEMIghb78UEtoBzGJDUAjr23vPr-vx-TEz38_ibOpd12ZaXJx_egHXzS_GKfvkpdgFGRwCCEw_mZ1__7SkjcpsRGtQdNjfyQyWm5QX09weIDNEVxubQDWDNauYTBpysAhzSjkioE46b7G8hFzSR7xCKVFJP158qobV13fMvqtA5r_QdS_lSRtv6dT9-UH5M1SVqHUbQTuAqVXzGOD3gA4gYMnnYAKCc1youpn6RtBBXBajwaQ6DcAMgpKioRfQaPKy0OyrA1eFYdoRHtZ1f6sPGpb_WmnV46Tjvx2V52_jQeFlnKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇲🇽
در آستانه جام‌جهانی، معترضان در مکزیک، تندیس‌ بازیکنای جا‌جهانی رو در جریان تظاهراتی برای افزایش حقوق‌ها از جا کندن و لخت کردن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91165" target="_blank">📅 15:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91164">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e51373c01.mp4?token=Z43sxIliNHGS_Z-Ek2adgIJwjIDN8lAiffuSjFpekhNV304oGjzE9OJO6vs0WkIBWz0_1YCwQGL8UDRpwB1OmU6MCb8jmjH7f85gn1u_oFipPb5nKE3ISa64d3XspwHExDyXV4T5gK6Z_AsOapFQFrPfv2em4ALlvcEOg7D2u_kQmLVZw4ZDCsMt-ZGeFnXhgQ6xYjjBzPUZliszC7v7vVchrieubB-SXtfLs8AvO7yyC-j1FT5BU8LUtj34tes51XCHN2rh0g-uKLrTLrQN6fhBf-6YTsX08eh2x1nWARuqMLf01qiwo-fX48bPjm6UAApVhbYjE5ET3w-eBkmhXXtyFVikXO6y81mEjlbNGL4rVLrBTxd9rM_pC37eqTcp8EisUKYcatEeROfw53iNtfxZ54wQmeDMyiHhWoR_SVloeO6_sDCJtN07t0oGP7_zBgRZgq8e2woGze_xUteGlNZ_nm28WQ8N5wa5A1ZQYxGRx4Sy7Vfy8xiyjO8RQ1g69aNPdKdp3p1uCke0WXjZKwS76rwOoFtPh96bJeVfR9xwM7pIpXpJCb6gG-X4g8UFN1wJxm7MDq7ON8LbjSC0trT8IVaa3cZdOZt8jd0VZfnytK1hU3MnRlQkXzt4CMqmSAXQOdsRP6C0nE10ERYjO0FOoN_vNOC-w6kPMbhUADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e51373c01.mp4?token=Z43sxIliNHGS_Z-Ek2adgIJwjIDN8lAiffuSjFpekhNV304oGjzE9OJO6vs0WkIBWz0_1YCwQGL8UDRpwB1OmU6MCb8jmjH7f85gn1u_oFipPb5nKE3ISa64d3XspwHExDyXV4T5gK6Z_AsOapFQFrPfv2em4ALlvcEOg7D2u_kQmLVZw4ZDCsMt-ZGeFnXhgQ6xYjjBzPUZliszC7v7vVchrieubB-SXtfLs8AvO7yyC-j1FT5BU8LUtj34tes51XCHN2rh0g-uKLrTLrQN6fhBf-6YTsX08eh2x1nWARuqMLf01qiwo-fX48bPjm6UAApVhbYjE5ET3w-eBkmhXXtyFVikXO6y81mEjlbNGL4rVLrBTxd9rM_pC37eqTcp8EisUKYcatEeROfw53iNtfxZ54wQmeDMyiHhWoR_SVloeO6_sDCJtN07t0oGP7_zBgRZgq8e2woGze_xUteGlNZ_nm28WQ8N5wa5A1ZQYxGRx4Sy7Vfy8xiyjO8RQ1g69aNPdKdp3p1uCke0WXjZKwS76rwOoFtPh96bJeVfR9xwM7pIpXpJCb6gG-X4g8UFN1wJxm7MDq7ON8LbjSC0trT8IVaa3cZdOZt8jd0VZfnytK1hU3MnRlQkXzt4CMqmSAXQOdsRP6C0nE10ERYjO0FOoN_vNOC-w6kPMbhUADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
یه ویدیو از بازیکنای پاری‌سن‌ژرمن موقع ضربه پنالتی بازی با آرسنال منتشر شده که نشون از زرنگی شاگردان انریکه برای گول زدن بازیکنای آرتتا داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91164" target="_blank">📅 15:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91163">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c5176bab.mp4?token=Q0avA-sA4HWDGlUI7OY-r_7Q_WrtEbPMjEgzHd_K2WOPJOO7jo0redSVLHWIa3pGme6uNzdjL_-1auaOalCCJ65pG7meeTieu1Q1KR99fki7RHBuuvwCci7xtSygBkXM4uzgiLZ_UWxTMQty25rxrB8kxiyNTSPaBxO3sAWUusbxIcKnhKRBmmll30YuG7u2dbT_v-8RqtgIVFFK4CF5w6Gkuy1EBnDBOuhfIsMxoeRGAVSdXXMwvUohhRjwAvids6M06tnpXWJFcBzgPtUNxbDygiDyfzxyEQkFaqnsABX3zgbrZ6s3iZxTwCVC2K3MXlApGvo98ZjwU1GOiV-4ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c5176bab.mp4?token=Q0avA-sA4HWDGlUI7OY-r_7Q_WrtEbPMjEgzHd_K2WOPJOO7jo0redSVLHWIa3pGme6uNzdjL_-1auaOalCCJ65pG7meeTieu1Q1KR99fki7RHBuuvwCci7xtSygBkXM4uzgiLZ_UWxTMQty25rxrB8kxiyNTSPaBxO3sAWUusbxIcKnhKRBmmll30YuG7u2dbT_v-8RqtgIVFFK4CF5w6Gkuy1EBnDBOuhfIsMxoeRGAVSdXXMwvUohhRjwAvids6M06tnpXWJFcBzgPtUNxbDygiDyfzxyEQkFaqnsABX3zgbrZ6s3iZxTwCVC2K3MXlApGvo98ZjwU1GOiV-4ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
💥
رونالدینیو به یامال: این راهی که تو شروع کردی رو من آسفالت کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91163" target="_blank">📅 15:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91162">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBPKey0AWKWG7hadyn5G9nKtnSwj0xd0yoyi2kC63ZS1QKJTZ-S-uLvbnLyWUEL7jo1ZMb4S6xkrO_dP7fBhVdn5z3YiU63Xndw7pvSI7QftWkiATDcaTYZB4_EWknKAl25RocIOdI5BmKJbQKtahhhJMFGuMZBbDMRDP1xIF5_Wg9LgKGxmgYHsOmW945nZ2MjAgp2fd5DyBaXqjDvpLwwm-322AeVAzFC03RfTohrBMoSAOUDDjSnZT8w9vEXr9QQIXdE7rjkoAVbQJJitNZKLg6UNxuRtuXUnaTMasdoCZUsk3-1lZWJq2F_AkOzxVR2kPoArYmEoGjNp5r8iXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇫🇷
عکس‌رسمی تیم‌ملی فرانسه پیش از اعزام به جام‌جهانی و سفر به کشور آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91162" target="_blank">📅 15:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91161">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc14c7273.mp4?token=LCd9Uoj_w3mVU2k8xuFljV0msvbhc8O-QdqCyl4EbPNqGywKhhwikQWpjRr2WCc40fB6nkyfkfggTbtUVd14WCtaV6tSFA58UjC2sYe68KeVRVrcd_c9KMPBqp15Mo7NA0mX3kjQOMC2lP-Dzjvv4qCswqlrAYku_2rEuUcK9EDX9kOhzSjiSMUEbnL-1XQtMFLrinYKb-e4PYuU0g4bJzTyiZIEiVSOOaTF1-MKwRRuohi7tHN2WHs8LizQsTyp4WeQzifgre4R7gGR1ag9crxtcYREwusXNYxraSDXHK0Kf2ZUW5xravSIHPu2lTNfJwfdcamla8zAQMRdjDHLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc14c7273.mp4?token=LCd9Uoj_w3mVU2k8xuFljV0msvbhc8O-QdqCyl4EbPNqGywKhhwikQWpjRr2WCc40fB6nkyfkfggTbtUVd14WCtaV6tSFA58UjC2sYe68KeVRVrcd_c9KMPBqp15Mo7NA0mX3kjQOMC2lP-Dzjvv4qCswqlrAYku_2rEuUcK9EDX9kOhzSjiSMUEbnL-1XQtMFLrinYKb-e4PYuU0g4bJzTyiZIEiVSOOaTF1-MKwRRuohi7tHN2WHs8LizQsTyp4WeQzifgre4R7gGR1ag9crxtcYREwusXNYxraSDXHK0Kf2ZUW5xravSIHPu2lTNfJwfdcamla8zAQMRdjDHLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇵🇹
یه سری از دوستان نمایشگاهی ایرانی از بیکاری اومدن برا پرتغالی‌ها چالش جام‌جهانی رفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91161" target="_blank">📅 14:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91160">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🎙️
زلاتان ابراهیموویچ:  صحبت درباره قراردادهای رئال مادرید در این تابستان خیلی خنده‌دار است. فصل گذشته قرارداد بستند، هزینه کردند، جشن گرفتند، صفحات اجتماعی را پر از طراحی‌ کردند. سپس فصل با ویترین خالی به پایان رسید.  و حالا فکر می‌کنند بعضی نام‌های جدید…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/91160" target="_blank">📅 14:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91159">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucRu9PiUlbXc0-ziElXKWzG6Rw5Lak-ZgABv1CuQGDrjXD99sYOnIGwoKhiVPiINT_Yld0EpaGa0ch_9-U8adADm_i46HkKOwjXuhIGd8OgkLLGupe-hKPqatJm2tk3iWcggfAv0ccVVEyRFuZyv9Ha11P77nXUSLmAbVaJ5BNj0HccgEqY-blgG_D2w4JPTZvM8h-GayvOx6vbBvNXkpzdD_BGbUPufwU29KOtqXoQznLHE6tjU85IFIDakm6_bM8wWG-8gE7hGaj9Uwgn92Qiis-otuBCbisJaekuVJtj0otR14U-1ZLk-bCvBG8Wq8NyW4rupP9LhSFiMMf-9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
زلاتان ابراهیموویچ:
صحبت درباره قراردادهای رئال مادرید در این تابستان خیلی خنده‌دار است. فصل گذشته قرارداد بستند، هزینه کردند، جشن گرفتند، صفحات اجتماعی را پر از طراحی‌ کردند. سپس فصل با ویترین خالی به پایان رسید.
و حالا فکر می‌کنند بعضی نام‌های جدید ناگهان آن‌ها را قادر می‌سازد تا با بارسلونا مقابله کنند؟ حتی اگر ژوزه مورینیو خودش برگردد، مشکل خیلی عمیق‌تر از این‌هاست.
اگر بارسلونا پروژه‌اش را کامل کند و بازیکنانی که واقعاً نیاز دارد را بیاورد، رقابت بسیار سخت‌تر از آن چیزی خواهد شد که بعضی‌ها تصور می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91159" target="_blank">📅 14:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91158">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80803a67.mp4?token=bAEsUD2YedeMXk1kyQkO6QlmhOnfP9-sq1KfBYCvWldKBFNsyXfmL0pUH8Ze0d_ya2_lgEx8SRlmYJbixq_si1B-tqLON3w4bL2odwXKx_Oa3GM3J5XYWgkixG6W0v9Ipx2CLj_xI8Imj3C2lBWqcLqSV4Q5IFfW5aOBqm-JG6dSHKY-vhGzoy5GOu36GJh_dEufhkVnWQqhl0njLCZ20m6FxJ2UWWwYW5ZCwloZEk4hhHjVFKS-ovK5Vd6xrRevevIkBQ2SKG8jPM_CgiLLje1396AINCApRlahfxKs6K0BJCFOkYzJtyJBjvNUMcF18NzLHDEpbuHVDcXh-UpJNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80803a67.mp4?token=bAEsUD2YedeMXk1kyQkO6QlmhOnfP9-sq1KfBYCvWldKBFNsyXfmL0pUH8Ze0d_ya2_lgEx8SRlmYJbixq_si1B-tqLON3w4bL2odwXKx_Oa3GM3J5XYWgkixG6W0v9Ipx2CLj_xI8Imj3C2lBWqcLqSV4Q5IFfW5aOBqm-JG6dSHKY-vhGzoy5GOu36GJh_dEufhkVnWQqhl0njLCZ20m6FxJ2UWWwYW5ZCwloZEk4hhHjVFKS-ovK5Vd6xrRevevIkBQ2SKG8jPM_CgiLLje1396AINCApRlahfxKs6K0BJCFOkYzJtyJBjvNUMcF18NzLHDEpbuHVDcXh-UpJNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇾
تیم ملی پاراگوئه هم به این شکل سکسی بدرقه شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91158" target="_blank">📅 14:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91157">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gweyh3Z90BKMXbTKR67bd1RhtU5h1rNmRbVd-ZpVa-ITykvYjV5eqhiA-QkGfKiEnkB-wZGqyz69EC3-TDo6751PTV5XdNcJEtB8y7r6sZ38EmC3hfBzGx0v4cbQrmUKd0aBiWmEfpww9nAwI7jSMTvaQ5z_EdWSm9WcqyI1SZL-GHc4sg-_MIhKKmcJzPCK23Ju2ePzI1G5jSqqTKPsikyp-_waqFKzjJ1am_jvGYf34WaGcRysC70bQFfi8IbojgJcztubYFwqDjCZhGPOF8lTI8g-IEnnX370_fB-EL-UeH8f93SBDu0-L9FIE1ilTpz7did4IErvftKrf5fBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دلیتا تو جام جهانی مجری خواهد بود
🍆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/91157" target="_blank">📅 14:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91156">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJtYwfClyNmiwoTtxPI6dZvr-xa2Sod1IszwQ2bqzLA_men7X-UOWKq6eRmB3PrAKS1urSCOBCmv2CPDVibdMOR3hJePalSBnp2C7rSmacAc5fmxSGM_M3mdBplmqYQ4Mu7gb20VuoPGhvdwMdbgL5yQKAwSavOGXW-Hgp4gq6VSf4XYRn_ZLT0Dpy_CDSOvZJ7kgaaiWCAVSHxp6OnPElF_xbsxFCAGosKpw4v-S_h0tH3u383Uq0S9tWWp5iRq5iOJYAMO8_Jifa40HkqIKmPIu08bpaCiyP4UW5yQSD4OPYTmFztpAylDR5x43wnRlsoiJTRlNpC-mMt3yGRIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">11 سال مثل برق و باد گذشت..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91156" target="_blank">📅 13:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91152">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdGE1EeWGNck2qT6dCx8Wb7r2NFchTNSD_hFn2BpbWXsNGyy-k_uC_U6pDxjVvdeQuxL0W8aMJcA8vALVtJCiZ1Er4ZXeLKap8q4tuEG1AvH5JgyXBQ7Ih0mSqWUsPREcbWKVDR0DmwqNGLw8yQNySET3sYb9fcBtECKyf25iEPaqaZzOI80JiVO8nJuwLuGeRHI8qbO7CoBHxWodRfn3Xarr0UpUaLAMuY0hj885NzfVbIAaglmij2PbAK5-onj6D0c1b8GhE4zFbWaxNqcI7kXwA6ktuPLYBa0cMmUwDQmQe90JVokQVWbz2CW8f0q7D2QzVUGnRBU0_YHViU7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYVW3ryfu07r8xL8OjLcQJkK89BLE9dAUram6keVba9k2Pd1cNeegqmJUZTpNPHn5SJNhhqgFsfu47qQ3ZNVIjM0ZcVMP3q47pfcrtTSGrvqkfW59-cFz-3lMkpfk7QD_eejtaH4A9Hre7GXDziJaRBGAAbqrgCJohcSUJmJ3ZsBCnaXfp3xP6WtrNZoyuduLUhJT8Dveh3i_YC5wJFdSAt1SlPLWb-zd-JEm2gW6nBe1Kw-5STbkmV-nYM3uUTTnodtXmHeRXUKGTIMA6iOfrZJIwoZrDC-8m31JuQ_edTQn3XUIHtk80XI55CCH-b2nkcc6ijwk6fOFxdzVq9Y_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZImLL07aXPRlUhilaMQJNN5EfpsBtH1UH483p3OKj8L-F2HluR9bplFcPjEjQTCpb3as4uGUFc2bGd_Fvw8urE4n1GJvOg11LsLm1cKn0GcOi4nW36QZ0Ak3PMuvSv96wN1b4n3yHXE9HJsUMQ4YwigUVz1Ywr6FQiZebsrmFVQU5c40-nkJ591BCpHvcIcGHyJgpB67nPLjfvjXSjoY8mZsY2cLE-VSPSudkG0vRMSVsxbdBLoRSzQ4yaLPqo0ZFRWCCZo6gdojR43X1qr1mVkuuOjvL4KBe-blWOPEtKgomEx_NGvES9ufvO8Z8bwBnP-opFNe7tjXqFb62qGbew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDAIOHYnCcuDGA8ZWc7w85Y84ReJoo7VKfAWM056aeFrZD0J7hXZGevHBcJW5JVCFv26Zc940csCzePng9blq8WIjK_UDap-JwXw43H5MEyGi23eZy-a_Rn5UgQqROG3u9XbMWSGdlrZq_0aTIrlRaNyihb3GPYgdmoDCp2TTqRb9MQ29Wm-fLrsTIXCb22z3BGWuSbVwx-5RzsOJtEJpCVHs2IlCLrU0N1b1FsY27QaFU1hHfmKOa0RhFmd0-XsSLlaqWq9xzA-H0KQrhUcqvBkalKtpa5rSpE7l84FHZMUWtRYzBQo3KJzKHcxQx1cwyWu_WD-a_Hs8Nx1rmh0cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🤯
مادلین رایت هستن که بعد از خداحافظی از فوتبال تو سال ۲۰۲۲، به طور کلی وارد OnlyFans شد و درآمد سالانش از حدود ۷۰۰۰ دلار به ۱ میلیون دلار رسیده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/91152" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91151">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_ePsXRWeo0WxxqsLN3Umh3mJ35cEh5zF6XJEhA37nmqHh9ElzqOHo64kIIpo32LNSGUA55gI3NPUT-wqoL1GuGt6_spa1OuT9akWj-TUiEYVkThb71pbYjdivs2kZFkQ5F2-kNqmaG-XLu4SKiVUX61ofMoEwIBuAiLwX4GsttV9OI2SwO2Q6fHXOp4xmHMhluYyxK0BloDRFUyUTBEVe_1DeCwsqQrNuvh_jSlnu9YPBsDO2K6H-rUrbFG2QD3V2X1mbc_C-Nxin1-VpilexOiG7EsTBksFvL6kGVQj5do4TUCHSm1F8uTIYggxdSWYOiq1lejZayFywxzYdT3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇫🇷
عکس‌رسمی تیم‌ملی فرانسه پیش از اعزام به جام‌جهانی و سفر به کشور آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91151" target="_blank">📅 13:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91150">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
‼️
موسی‌جنپو بازیکن استقلال قراردادش رو فسخ کرد و یه پرونده جدید به لطف علی تاجرنیا برای این‌تیم در فیفا باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91150" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91149">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICm5TPgvjH3jrsT8Juh2rLySAx-MsF-tzPY72W_DOVMiRLRsiyQpL495ebYCxpLqxTCd-2avsM_OHa_1B4XRA7V7jlMCIbZn3RgSteV7Sx1Ror5sRTq_Ca8OkxRcB1er4YpbEv7yJLh2WmT9QTlCmFgGZwr8SxeVwEOo26Az3DeVhWl8G5WvTlHE8myUhZbEQ094wa6czEc5F4UpAKs21Nvgw_XotnTIB7ibVlJwklShXJ_Sh0ZshZbegyEIW2H6m1ZN3uAsXfdIJk6wAHPRKIMf-i8aUo8aTaFgt1DBDwhr-ifCeFzlLUfTDgEopppsKWmh8nk1rgL_czW6K-X7DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از ترانسفرمارکت، یامال و هالند با ۲۰۰ میلیون یورو باارزش‌ترین بازیکنان جهان هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91149" target="_blank">📅 13:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91148">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
#فووووووری
#اختصاصی_فوتبال‌180
؛
🔵
ابوالفضل جلالی در لیست خروج باشگاه استقلال قرار گرفت و فصل‌آینده جایی در آبی‌پوشان نخواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91148" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91147">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz_YlX0IugYmGrSoqXYWVhkhOp4U2tctipMNeIMPnag_tYNkblg2AlaDntvu47SrsuUXm_f5lR6-lCz9NDUdrli4Vk_0TEPDIbo-YacGdvIoWzzWMvzVHF2G0O5mXdtO8CBiyl8h9wYIvZV5DQY4SGv0is5siT1bnUqyH5mMD1ssBaVw0mo8GWzHgDwVeBo13U2aab9D9uIJcWZDdLWRuMu98mByeGcXqBpAOekpkz_kL3eFuudNhKfAl8uiDSynUkrAYUnTZ63xOEwIZE6td3c__R6Qy8vU9Vurz16CW6YijD10Rj1UsvWsEjTphyxfynUQWsM3-TzGWUBxaVTb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇩🇪
اولیور کان مدیر تیم‌فوتبال بایرن‌مونیخ:
🎙
اولیسه باید از خودش بپرسد چه می‌خواهد، رئال مادرید او را در گذشته غرق می‌کند و به بهانه اینکه ما در گذشته بهتر بودیم فریبش می‌دهد، مجموعه‌ای از افتخارات و جام‌های قدیمی، اما بایرن مونیخ آینده را به او می‌دهد.
🎙
رئال مادرید باید دست از زندگی کردن بر اساس افتخارات قدیمی بردارد و تلاش کند در آینده پیروز شود. در گذشته نام رئال مادرید بزرگ‌ترین بازیکنان فوتبال جهان را جذب می‌کرد، اما اکنون اینطور نیست و آنها هر تابستان باید بنشینند و بازیکنی را برای پیوستن به تیم قانع کنند، ما گذشته آنها را نداریم و آنها آینده ما را ندارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91147" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91146">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
وزارت خارجه آمریکا:
فقط برای افراد ضروری از جمله بازیکنان و کادرفنی تیم ملی ایران ویزا صادر کردیم و افراد اضافی جایی در آمریکا ندارند و نباید از امکانات ما استفاده کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91146" target="_blank">📅 13:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91145">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIFrHd39cNHxoSkpnCvT4aphjsw-3PV2kl_AxiqUtYBeFW95phbh9TQF19TIjYTWEm0pUUIBHUetiYP20bTe8acgxYM1gDWLeayekL5TlgYaqJTTnQh995u8GWcc7NofiK4xezpNoxe8WvJa58RpYAT2YeGvoEAkIOm6LoiefaOPAgt-WvctAW2cXerdvcyC-sm47vH0JyrhB1X4LzXtNu8kqB79ISwLJK0reAPDhZGXvbiE2okIn3xrejOIfYZ6QefUSg1pxYEu9HG2izBEllsoQ1oq0DUEjvTfcJU9fWQFIBgD38SQsV576bdrroGjZQbX9rnYLsGa57NxihcnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
معرفی مختصر تیم‌های گروه A جام‌جهانی
🇲🇽
مکزیک:
لقب: El Tri (سه رنگ)
سرمربی: خاویر آگیره
ستاره اصلی: سانتیاگو خیمنز (مهاجم میلان)
تعداد حضور: ۱۸ دوره (یکی از باقوام‌ترین تیم‌های تاریخ مسابقات)
بهترین مقام: صعود به یک‌چهارم نهایی در سال‌های ۱۹۷۰ و ۱۹۸۶ (هر دو بار در زمان میزبانی خودشان)
دوره قبل (۲۰۲۲): حذف تلخ در مرحله گروهی (پایان رکوردی که ۷ دوره متوالی از گروه صعود می‌کردند)
نحوه صعود: به عنوان یکی از سه میزبان مشترک مسابقات (در کنار آمریکا و کانادا)، بدون شرکت در بازی‌های انتخابی به صورت مستقیم صعود کرد.
وضعیت فعلی: آن‌ها بعد از تغییرات پیاپی روی نیمکت، دوباره به خاویر آگیره باسابقه اعتماد کرده‌اند. با داشتن امتیاز میزبانی و بازی در ورزشگاه مخوف «آزتکا»، فشار و البته پتانسیل زیادی برای صدرنشینی در این گروه دارند.
﻿
🇰🇷
کره‌جنوبی
لقب: جنگجویان تائه‌گوک / تایگرهای آسیا
سرمربی: میونگ-بو هونگ
ستاره اصلی: سون هیونگ-مین (کاپیتان و ستاره سابق تاتنهام) و لی کانگ-این (ستاره پاری‌سن‌ژرمن)
تعداد حضور: ۱۲ دوره (رکورددار بیشترین حضور در میان تیم‌های آسیایی)
بهترین مقام: مقام چهارم جهان در جام جهانی ۲۰۰۲ (به عنوان میزبان مشترک)
دوره قبل (۲۰۲۲): صعود دراماتیک از گروه و حذف در مرحله یک‌هشتم نهایی مقابل برزیل.
نحوه صعود: صعود مقتدرانه به عنوان تیم اول گروه خود در مرحله سوم انتخابی جام جهانی در قاره آسیا
وضعیت فعلی: کره جنوبی ترکیبی از با تجربه‌های باکیفیت در اروپا (مثل کیم مین-جائه در بایرن مونیخ) و جوانان نسل جدید دارد. آن‌ها به نظم تاکتیکی شدید و سرعت بالا در انتقال توپ معروف هستند و مدعی جدی صعود از این گروه به شمار می‌روند.
🇨🇿
جمهوری چک
سرمربی: میروسلاو کوبک
ستاره اصلی: توماس سوچک (هافبک و رهبر وستهم) و پاتریک شیک (مهاجم لورکوزن)
تعداد حضور: ۱۰ دوره (با احتساب دوران چکسلواکی سابق) / این دومین حضور آن‌ها به عنوان کشور مستقل «جمهوری چک» پس از سال ۲۰۰۶ است.
بهترین مقام: دو عنوان نایب‌قهرمانی جهان در سال‌های ۱۹۳۴ و ۱۹۶۲ (در دوران چکسلواکی).
دوره قبل (۲۰۲۲): غایب بودند (نتوانستند جواز حضور را کسب کنند).
نحوه صعود: پس از ناکامی در صعود مستقیم، از طریق مسیر سخت پلی‌آف اروپا (UEFA) موفق شدند بلیت حضور در این جام جهانی را رزرو کنند.
🇿🇦
﻿آفریقای‌جنوبی
لقب: Bafana Bafana (پسران)
سرمربی: هوگو بروس(مربی باسابقه بلژیکی)
ستاره اصلی: لایل فاستر (مهاجم باشگاه برنلی انگلیس)
تعداد حضور: ۴ دوره (پیش از این در سال‌های ۱۹۹۸، ۲۰۰۲ و ۲۰۱۰ حضور داشتند).
بهترین مقام: حضور در مرحله گروهی (آن‌ها تا به حال موفق به صعود از گروه خود نشده‌اند).
دوره قبل (۲۰۲۲): غایب بودند.
نحوه صعود: صعود به عنوان یکی از تیم‌های برتر منطقه آفریقا (CAF) پس از یک ماراتن انتخابی فشرده در قاره سیاه.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91145" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91144">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNI1G0JZc4aHMq2Mg1pbO7y65sAsB1s3iwUyRqxDWzUxNTZmDvs2MC2B5SaKwecJcdr2XBvl138vKq24c9IYZvJrqPctgyb9mnaevv_ppIrYiEiY9MKK8oYHzcvII35DNSsBEqAbk6O5XUZSf8DtKkEm01Cn9J6hilfo81qBu5MM4tOs2OsxSNupArNiJNtvjATazkL682vUflYlytdWd1G2215CJLrJM_JWUEFwGbQSL4y8DfToL81lgB9mfstMKWpGJVBM62ZCLt3CWitE5IjjgLRQ7SPJWWtUjrGTJ1ubTJUgmHKGUsOZep67ispUUkhuA5ONc0RrXz1X1CyYtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاکا: «من علاقه‌ای ندارم که فرزندانم بدونن که روزی بهترین بازیکن جهان بوده‌ام. فقط می‌خواهم مرا بهترین پدر جهان بدانند»
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91144" target="_blank">📅 12:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91143">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR2tknDsG5e1AaAzAIgbWU6h2-qthOrZwb3aloJvtcu_sq2J7CDJSYp2G5skk2b72K-xn9kZtawoAk9n8wNVXhhY0i5rjMfbsOW4Hp90ZafCbifzkHNUw35YsBUs565YqUoTCdDssW4_y6YqIvPq9fVxcfMvd2X4RWfA1D6bEtKiY-CEYsFf-oNnvZKG810dcB_5I2FUtL4WoutyfDorZ33jdbr_DNAPmiUWW-OBycOnQQlQxMdEItgEBPMul07DLHjMNZERraJ4_ibxG71Um8QHOhHcFmthB-KF2jLDZy6jT3PN4-zc3WUZ1aKBeJAib8j5NETnOI6Z0YHLBYCfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
#فوووووووری
؛ بردلی بارکولا برای تمدید قرارداد با پاری‌سن‌ژرمن به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91143" target="_blank">📅 12:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91142">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c06a46347a.mp4?token=hElCjNp_lCUMttjFAwTJMoNAW-UQy4WVFTO4RQCnZ4sITt9oCvdWBmonzqRo0HKQ9i3QSw2WMoL7kl-lQ1oGRy4Lf2WikMReG8Zw5yWjdyARN50gragsrINkLe74-UHHnfB9f-6JIsCpJrEQx8YbIeQLgfUiSy4qoBwy7zROlHjwd7czPaSEBdijLItmPkDioIVzC7Ognkh7Ol2qDR51obP7lgvaZse-zik8i-FSW2cgeX2inDGaWwTJtFMTjHm_bTsq8l76p-u1JL6ucAYQisGvC6MmFy8d0ARIC7rfSpvBZRYh52xlFSwit8bDG9dk26cfqMRfN_-MWs3xKcJmOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c06a46347a.mp4?token=hElCjNp_lCUMttjFAwTJMoNAW-UQy4WVFTO4RQCnZ4sITt9oCvdWBmonzqRo0HKQ9i3QSw2WMoL7kl-lQ1oGRy4Lf2WikMReG8Zw5yWjdyARN50gragsrINkLe74-UHHnfB9f-6JIsCpJrEQx8YbIeQLgfUiSy4qoBwy7zROlHjwd7czPaSEBdijLItmPkDioIVzC7Ognkh7Ol2qDR51obP7lgvaZse-zik8i-FSW2cgeX2inDGaWwTJtFMTjHm_bTsq8l76p-u1JL6ucAYQisGvC6MmFy8d0ARIC7rfSpvBZRYh52xlFSwit8bDG9dk26cfqMRfN_-MWs3xKcJmOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتینی ها از الان تو آمریکا کولاک به پا کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91142" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91139">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=asyisFJpU0uS49VgtxBNAjiGwAvvZ7K7kasvNUfIsg3CKtxcriN9Jam-doM4bRZDlRwrIcMuuNsad5Pl47A-fk8OE4Yo39AuVnRFsQP-EXHovcTztBZ9cm5U3aFgLwmL2ul4TkDSXgQh-C7iRxZn-8zNcS8TfJynjxIPLEmI2RbEO4yuqYc238s3hhVSQhXfXRaWx0zk_W41aCX78i7LXP7ijxjTRvoEdqWjPMr0YvX1FiZUc4BX736cRu81YEYSlfSreSv3nP_YrzggVdqfWrcnT-q1lEbCC2-W2luEHfnwryoSRwReuIGL3do4JamxDbA4r0FeOAJe18oMHlnBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=asyisFJpU0uS49VgtxBNAjiGwAvvZ7K7kasvNUfIsg3CKtxcriN9Jam-doM4bRZDlRwrIcMuuNsad5Pl47A-fk8OE4Yo39AuVnRFsQP-EXHovcTztBZ9cm5U3aFgLwmL2ul4TkDSXgQh-C7iRxZn-8zNcS8TfJynjxIPLEmI2RbEO4yuqYc238s3hhVSQhXfXRaWx0zk_W41aCX78i7LXP7ijxjTRvoEdqWjPMr0YvX1FiZUc4BX736cRu81YEYSlfSreSv3nP_YrzggVdqfWrcnT-q1lEbCC2-W2luEHfnwryoSRwReuIGL3do4JamxDbA4r0FeOAJe18oMHlnBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امروز در کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن
«خسرو پناه حیا کن، کنکوریو رها کن»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91139" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91138">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773ec48db.mp4?token=A0Gtr-__nuWUzUw_oVdWKDWDWrZhp1hwkD3rOrqOLeg00ft-zigMyIN29_uY4fMvLOHKM9cp1B9aTiH09vJZfOltNE0AOFfsfMqLrcR56iIOT94C0BnbB7U63s-I0HpE0khbr-ZlO7tgfeqTkoSZeIUTIkg1gptNCQ98T3vT5j0MY6jl0e_dqwhwLW9cWBlKOKzHU6rw9w6IXqVx3IBdUpj9es8uVNA_2ZPig0jyupuJXzHZnqwA1B9LNKVO-EhoklxQyuPFRV9O2jFBX81FfluTLy0JOkM1nSz-tAIlCM_CQAVPRA5zPQqabGp58rlrmUQHesmH7Lo6i-V6hPy6FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773ec48db.mp4?token=A0Gtr-__nuWUzUw_oVdWKDWDWrZhp1hwkD3rOrqOLeg00ft-zigMyIN29_uY4fMvLOHKM9cp1B9aTiH09vJZfOltNE0AOFfsfMqLrcR56iIOT94C0BnbB7U63s-I0HpE0khbr-ZlO7tgfeqTkoSZeIUTIkg1gptNCQ98T3vT5j0MY6jl0e_dqwhwLW9cWBlKOKzHU6rw9w6IXqVx3IBdUpj9es8uVNA_2ZPig0jyupuJXzHZnqwA1B9LNKVO-EhoklxQyuPFRV9O2jFBX81FfluTLy0JOkM1nSz-tAIlCM_CQAVPRA5zPQqabGp58rlrmUQHesmH7Lo6i-V6hPy6FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه قهرمانی تیم ام سی الجزایر تو لیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91138" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91137">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-e4yDA_cPSsig_65DdXqlTpHsZQgFnWBTWRwn-Fdl1Z6gxnXWhdGOS9MloSUwbqMOo2EBt_X9qVE2LNPLK1776xWGA4fHaFTwmyfNdIRfI41UE9K21UpTcgg41M5qWYhT_3NnPv8dJucTHXWMVUGUzbDROSh8t9-JA_f1rWIjRyWN7UVPxZMMBFVPZYcOMzjNol8FKbd2TQkCWRhopd6EeoXm7KAab8srpxJpKZarPKJc9dCiNcxsIyte-i_W_ndXmq7POQj1i6nracO--vfxIX59IK9HaaRafhskO4r07WbYgTc6lcKGWOKuDabnSLtG-5iga5RISrE_gQzq-LVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
لیگ‌هایی که بیشترین نماینده رو تو جام‌جهانی دارن؛
انگلیس با 165 بازیکن با اختلاف در صدر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91137" target="_blank">📅 12:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91136">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be064ede1a.mp4?token=s5SPjNgcgngpQk6RTnqB-n6Z3G6Ze2rm8hxt8P_uCRVY-TUlMlb9IB5cZirqoF8II4AuVAlgk2A9zuyQ2d0kh7h4Gs9TD89H8IgQYsLyY62f08LiQkyziXEPt_JK5sWVAMOmLKDFExHid0H7JazXGceaU05sDs-Tv6lU84-yZiPhojPvDaZLNumJ6BhYKL7LycbWr8ZivIEVTNmqYNO_PwxCysFf0cZ_4iX5VdzoTeN0TjQr7RqFGqcasAjd-C2AtohMMW8Xv76WGbNV0-mepvXZ8wxnFsPwrQgrCsG4UB64v-sdxNxcad3hlLf7-XgDAT15IUxj0E0-4gztji5r0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be064ede1a.mp4?token=s5SPjNgcgngpQk6RTnqB-n6Z3G6Ze2rm8hxt8P_uCRVY-TUlMlb9IB5cZirqoF8II4AuVAlgk2A9zuyQ2d0kh7h4Gs9TD89H8IgQYsLyY62f08LiQkyziXEPt_JK5sWVAMOmLKDFExHid0H7JazXGceaU05sDs-Tv6lU84-yZiPhojPvDaZLNumJ6BhYKL7LycbWr8ZivIEVTNmqYNO_PwxCysFf0cZ_4iX5VdzoTeN0TjQr7RqFGqcasAjd-C2AtohMMW8Xv76WGbNV0-mepvXZ8wxnFsPwrQgrCsG4UB64v-sdxNxcad3hlLf7-XgDAT15IUxj0E0-4gztji5r0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرکی به ایشون گل بزنه با من طرفه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91136" target="_blank">📅 11:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91134">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7pDwI8WWoPYCEEQIBGE3Iq2haXU_JHWMCWHkDh2MbY8I2n08al61wVmOfhSPVtWiTtHCyAxWUpgxBvw7-dIt74k8hjzydW1g_vE2KmIlK-6QYDQySIV7XpNyCDE3uVrF49prlWP96VnP5rC_oc5vxLgJH43ONv2aeLKZiAY2UR4PlSd8IwYMkcJ-yXtjvTquCDow600X32WuFScwVfixwaBt2bQ_VYFmXy-MYwyudHYAJFZTQo2UH4AkM9Jm4JOsrJJMO7JHuPotwT8Qn3HZ2TsvmdsPz5FxZAC5BL9cjGXdXwpQUWhrS6XMldu5vumVw9hlRMZCNtVdPSHqNuPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7UJLu7vL_BVfqH5u3qACaIFrA6czAH4glnu1bj9QJUZ0YS3cnFy99ZzqTZnBjxb8ps5qhFNWy-1bt_pO8H4ne8-ZypxjCH2yw1KKWSL8okhuYS71LzMB-bsC1yZWHRXz7mbbClH2u9XG734eJPPNvM3GlKm6_yfh8DswPcu9yP0qVXVGcthGhfTZZB_Ip1W5K_U9-iUZLOZj2KDCJ61uHeD9IV2WBQxuJNkYkvB4fVPnIhRcKPh80KYqujgZ7z84H12BeNvZzvOcivAnBlTAiYxkZP7BpUx8yaspCsk-jcZX0s8uZGwjPfOdsE2fYw3q-wJQAWf-MYWEllEw_Shpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
این‌چهره که مشاهده می‌کنید صدف طاهریان بازیگر اسبق تلویزیون و‌ سینما چند سال پس از مهاجرت و کشف حجاب، روز گذشته با انتشار استوری اعلام کرد که به ایران برگشته و خبرگزاری‌های داخلی هم تایید کردن
🙂
🙂
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91134" target="_blank">📅 11:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91133">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc3fc13c7.mp4?token=shP2sMX1vx4EQYXltmiaMhbfIi0VlhLQLdnyUB-slReG7PztT9oXdYwu2IhM_9gyqNzcN4Z3zStBdXz-lp13OX1pv-rvW7TC54RKWQM1r3I-TGM4-oFMvyU-jsH4Pclar0VJ8X0XJnzdTw-9RONz_dm9lq1UjI1IhHq50yUy8uM5NKckBMk229ymro--pD09D4wiIjQSrj_DVUAklzt_e0Xy8EKw6Rhbklj00fflXo94ZncPpIXo2l0eFpX2L50C9iRkAeWhm2uGBNx7hpAEuqL_yaDhMw7Hw9IPxKVDWBFlcHB3RRi-xpOuatAkwjjXrs_95yp2VILfJIrwxHX_tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc3fc13c7.mp4?token=shP2sMX1vx4EQYXltmiaMhbfIi0VlhLQLdnyUB-slReG7PztT9oXdYwu2IhM_9gyqNzcN4Z3zStBdXz-lp13OX1pv-rvW7TC54RKWQM1r3I-TGM4-oFMvyU-jsH4Pclar0VJ8X0XJnzdTw-9RONz_dm9lq1UjI1IhHq50yUy8uM5NKckBMk229ymro--pD09D4wiIjQSrj_DVUAklzt_e0Xy8EKw6Rhbklj00fflXo94ZncPpIXo2l0eFpX2L50C9iRkAeWhm2uGBNx7hpAEuqL_yaDhMw7Hw9IPxKVDWBFlcHB3RRi-xpOuatAkwjjXrs_95yp2VILfJIrwxHX_tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوستان حکومت اومدن یه سری تینیجر رو دورهم جمع کردن تا با بساز و برقص از تیم قلعه‌نویی در آستانه جام‌جهانی حمایت کنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91133" target="_blank">📅 11:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91132">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112d86fcd1.mp4?token=sDqKHFjruIogVTTeb2YYcy4yMiB5g3ZaiqlmkkoUrCok48DmtFGZ-ehkKIKrMTJ_rJEJAMa5fmsrL7ZkML_Zy1STuLVpn8yijS2ZgI63RqrpSKZukvgICkPM_NSaIzOtBL-y3xqpgUWJKL7O9Svpc53uQaAUkGl1EfjxkO6KKg72Yff4BZds65Y9ICs3P2_tM-yHaJ7ZUf2CxMkTaFqn26--Ey43Y-Zg9gNgu1qEesAzO4hScvpkibJRsq-iPCoKd8zAwLge-U5o9zAEP7kgiSRLEOrIlGVapVje7_QPXZIwsRXMzdJEsp9Vrzdr2GFFaqmKbNQsjlOvTa5GYAqb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112d86fcd1.mp4?token=sDqKHFjruIogVTTeb2YYcy4yMiB5g3ZaiqlmkkoUrCok48DmtFGZ-ehkKIKrMTJ_rJEJAMa5fmsrL7ZkML_Zy1STuLVpn8yijS2ZgI63RqrpSKZukvgICkPM_NSaIzOtBL-y3xqpgUWJKL7O9Svpc53uQaAUkGl1EfjxkO6KKg72Yff4BZds65Y9ICs3P2_tM-yHaJ7ZUf2CxMkTaFqn26--Ey43Y-Zg9gNgu1qEesAzO4hScvpkibJRsq-iPCoKd8zAwLge-U5o9zAEP7kgiSRLEOrIlGVapVje7_QPXZIwsRXMzdJEsp9Vrzdr2GFFaqmKbNQsjlOvTa5GYAqb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت لیگ پایه استان اصفهان: پیشنهاد میشه اگر افسردگی شدید دارید و مدتیه نخدیدید این ویدیو رو تماشا کنین
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91132" target="_blank">📅 11:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91131">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=IDMO0JY3nx_i_W8vM3_Cdxy5hSG7RemxlESZ8T7d0cLfqQCfO7pOj1bbCdVh3441GQS6wTtOehzsu0IkcfvrmTKujlQ8mJAVfSTVbHiNo0Wo2h5HUgjfwghJo_VWFl5A0JGWBX4eD5b0oeo2CXY0sjp2GPDJHqPmZ9Wn_6XgU-YaPt2ektirSuVbZQFNb6X4CRDJNGErMvvm7vk61tiYn6G0pgnQ1u4O-BQmQXH8Wtt1bgr_Cgo6mBs-QKh6BroSxnyfPzUQr1kJffWB7zPQd96GYCV_pBCiJhk-Y3nrkj5QTfBxAvi7TEnrGxJJv4Cuxz3cr6USUdsFdPbntl0xhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=IDMO0JY3nx_i_W8vM3_Cdxy5hSG7RemxlESZ8T7d0cLfqQCfO7pOj1bbCdVh3441GQS6wTtOehzsu0IkcfvrmTKujlQ8mJAVfSTVbHiNo0Wo2h5HUgjfwghJo_VWFl5A0JGWBX4eD5b0oeo2CXY0sjp2GPDJHqPmZ9Wn_6XgU-YaPt2ektirSuVbZQFNb6X4CRDJNGErMvvm7vk61tiYn6G0pgnQ1u4O-BQmQXH8Wtt1bgr_Cgo6mBs-QKh6BroSxnyfPzUQr1kJffWB7zPQd96GYCV_pBCiJhk-Y3nrkj5QTfBxAvi7TEnrGxJJv4Cuxz3cr6USUdsFdPbntl0xhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمعی از هوادارای پرسپولیس صبح شنبه رفتن جلو فدراسیون و از مهدی‌تاج میخوان این تیم رو به آسیا بفرسته
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91131" target="_blank">📅 10:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91130">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nn0BXD-xp1B-n3TAnhWVwp5eE0zUZMnRXz_HF5YLUEYOOpiTqMcRRKJd25ebxBd2rTjUQI_LD5yYjxxJ7W5GxW17_9IkFMnV4rNXOFNVGq33LvO6rpGyWymREeWm8ZlPTyFBRO-xnMSoC9oen41ao8Gg9YNmXem0OmBQDIH_kfpw1i7lkqMk81mEuAYw0M5q22LGS0Jbm9PUHc-hKZcsB8hUfKwtuAqcPMQFXhzwK59H5kfzzGzO6BblwqA_DdDEUzZwt-kro8fWbkZQqvZq1E2D0FZku9y3-SqBrA5MggzIj0UsxbjbT2xCRnvuMkiQMVUGaqTUFUgIrVllqBhRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇷
❌
#فوووووری
؛ لئوناردو بالردی مدافع آرژانتین روز گذشته در تمرینات دچار مصدومیت شدید شده و نمیتونه در جام‌جهانی حضور پیدا کنه. بزودی آرژانتین نفر دیگه‌ای رو جایگزین این بازیکن میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91130" target="_blank">📅 10:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91129">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🇺🇸
مهدی‌تاج: آمریکا شیطان صفت درخواست ویزای منو رد کرده. از این موضوع بسیار عصبی و ناراحتم اما کاری از دستم برنمیاد
🐸
🐸
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91129" target="_blank">📅 10:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91128">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss6T0DR7HiJ8fWqTqeqdvlWXnwzZlf5oAsPlgYMOFHtylEYStfYwD_dduJgY0SgIM5ruustZkQkUG5_ogICLtNy1QP2vCFyRkBUGB4SSSyWwogayPrTgqRn7HmryBbSsemN3rSN2ZF2TkgKAakoZolI_1a5PcaRnAGuCvz74L9NqbpkocLnfAe0ahwEn_cs64W0CPXi6W9MOe14iyOq7M5BGtU19bM44kxH4hIdf0FG_GVu7bZ6qzg8-7vwwU7ASfoKlrIEOIYLZvd65MPHIJgJ_5CJLHEZp_0ITEoyGUmEH5Y-jdgZGPMqgQk_8MuUaMt7G4QQsVc5PMI6H6K-gTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇮🇶
🇺🇸
#فوووری
؛ آیمن‌حسین ستاره عراق دیشب در بدو ورود به آمریکا حدود ۷ ساعت در بازداشت اداره تحقیقات و مهاجرت این کشور بوده. اتهامات این بازیکن ارتباطاتی با گروه حشدالشعبی بوده و مورد بازجویی قرار گرفته و سپس پس از ۷ ساعت آزاد شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91128" target="_blank">📅 10:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91127">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🇺🇸
مهدی‌تاج: آمریکا شیطان صفت درخواست ویزای منو رد کرده. از این موضوع بسیار عصبی و ناراحتم اما کاری از دستم برنمیاد
🐸
🐸
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91127" target="_blank">📅 10:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91126">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/728bdf34c7.mp4?token=jjBO5X6oo1Z6i5pfmkPGhySMofQxSetL6UkI4-DAMPUXAW4hpcJl_GpQfxTX0244DxgfirvGpHpdWZ5fMAQFF7FZqX6vVeQOAti71r-rE9TmgsS-XtRb98SMRNT3cQL8PaLv8ulGDhuOkEIHSeNRn_1uO9Foz1TN_kXSoIs79aC32FwzUw_n6qDVKw7L2N47TMVU8zAVlsiyN9tePO6gLBHIKFzchEKfvOlXSwfRycvPSTdVXy_vpQ1m6Naiak4hBC41YUE4MoekUwpK3LH4h0D2afRzYcNtqE_PhcCGVHK-O8RC7YCkx--By1JEfjrymtj52f3r_rfzva5d6jxZmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/728bdf34c7.mp4?token=jjBO5X6oo1Z6i5pfmkPGhySMofQxSetL6UkI4-DAMPUXAW4hpcJl_GpQfxTX0244DxgfirvGpHpdWZ5fMAQFF7FZqX6vVeQOAti71r-rE9TmgsS-XtRb98SMRNT3cQL8PaLv8ulGDhuOkEIHSeNRn_1uO9Foz1TN_kXSoIs79aC32FwzUw_n6qDVKw7L2N47TMVU8zAVlsiyN9tePO6gLBHIKFzchEKfvOlXSwfRycvPSTdVXy_vpQ1m6Naiak4hBC41YUE4MoekUwpK3LH4h0D2afRzYcNtqE_PhcCGVHK-O8RC7YCkx--By1JEfjrymtj52f3r_rfzva5d6jxZmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زور این دوست عزیزمون از هالک ایرانی بیشتره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91126" target="_blank">📅 10:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91125">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
‼️
پشت پرده اخراج شبانه و غیرقانونی علی دایی و دادکان توسط محمود احمدی‌نژاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91125" target="_blank">📅 09:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91124">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06eeae197.mp4?token=dMu1OamEKfTNa5E29ZfRsY2iqfE3o46rPQVVaRI5vt3lBAwcuWSMIrKhC8VTlgtsb_BYrI5ISEzZ9DBlVmo8sy2nE45nn8sIScZD6v-V5vBJTUkKXHkY0ib_MGSEPWf2AMhC7ZOHvi2q0hOjidyGDisEYljYKNexBMhV3932Ekwp1yEMtdQCsWLDaVHm3AoLwzsq_8byl4oauJiNqXUWWKoTqQft796V5AiOqPJ55IuJU9hknUYv0yJsVEhrOE2YDGVwSVfPo91NY6_KmkIOl6oGrnCNApzSB8bLju4VlvlsKWmKdlLQhgsi1I8qOpDCu3BoiDUEn3OmRClIndSvjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06eeae197.mp4?token=dMu1OamEKfTNa5E29ZfRsY2iqfE3o46rPQVVaRI5vt3lBAwcuWSMIrKhC8VTlgtsb_BYrI5ISEzZ9DBlVmo8sy2nE45nn8sIScZD6v-V5vBJTUkKXHkY0ib_MGSEPWf2AMhC7ZOHvi2q0hOjidyGDisEYljYKNexBMhV3932Ekwp1yEMtdQCsWLDaVHm3AoLwzsq_8byl4oauJiNqXUWWKoTqQft796V5AiOqPJ55IuJU9hknUYv0yJsVEhrOE2YDGVwSVfPo91NY6_KmkIOl6oGrnCNApzSB8bLju4VlvlsKWmKdlLQhgsi1I8qOpDCu3BoiDUEn3OmRClIndSvjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
👀
خنده‌های نیکی‌نیکول زید سابق یامال به رابطه جدید ستاره بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91124" target="_blank">📅 09:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91123">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/806ce63d62.mp4?token=OmdJLl82YZub6ek8gkx22PHRwexpBtQRUl2sT5NlW0xeJW7IJrnyGbHCahpr9vkVBcwT9qirBb5XGK-0CCSM5dHH6Z41xk7yEaQPN10Pit8Eb3hWZta7oypfnuvKzA2Nsy3IPZC_1rP5_i9NuIJYFcowCm3_7IURUfRBwgPoCXcLpCc0qqPPKSWtCoyF3MV2vlsUiezpyelkvKZsmvB9E46zmiLYYiwW1F3rA03whiFCk1uKADyZhhDkaQk0x9T19orWtXkv4e3r3B7gbzHodUJt9VJr-mQBVT-VrUi42H56430_X66gbde7BVkLZvfH-f_n5Wtwg0-AC2UnA6q-Lxi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/806ce63d62.mp4?token=OmdJLl82YZub6ek8gkx22PHRwexpBtQRUl2sT5NlW0xeJW7IJrnyGbHCahpr9vkVBcwT9qirBb5XGK-0CCSM5dHH6Z41xk7yEaQPN10Pit8Eb3hWZta7oypfnuvKzA2Nsy3IPZC_1rP5_i9NuIJYFcowCm3_7IURUfRBwgPoCXcLpCc0qqPPKSWtCoyF3MV2vlsUiezpyelkvKZsmvB9E46zmiLYYiwW1F3rA03whiFCk1uKADyZhhDkaQk0x9T19orWtXkv4e3r3B7gbzHodUJt9VJr-mQBVT-VrUi42H56430_X66gbde7BVkLZvfH-f_n5Wtwg0-AC2UnA6q-Lxi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇲🇽
هنرمند مکزیکی با آهنگ جام‌جهانی این ویدیو تماشایی رو ساخته
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91123" target="_blank">📅 09:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91121">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GDNbRnfv_rbd8Jhf9C0NPN2qobRhccslCf5Mn3dp0hqq-303f19PsgixP7V7XXD2ON-iaJxit9nHohsDg7f3RJJ2S-75DoDNK2NAdXGM-lx-IdxKwkXl5Hr3Q7BOR39rTVERHOBUhbuomj8FZziTiRzOSFDcErPGuoq36J6P1qI7rB591bsMl0T3qm5clCqvknOJGbV1v6zCDwl0ichVh5PYdAlbwCXNtq49dHLLEa-iJ2fmp0YGdCJ0dscVL832XpWvskk3J6bPLy6g1aWmwbX6a1XGZcNzavmNvVzOlKUSeteGAEIVSrmTas7HSSeDHZOvqzopPTA1FGfD-ReICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gawLXhG5CKwqksBKCHiOZmQp8sIUlrH3vQWem06fbgvkcjb2_v0wA6RGFD_HEjCSBll45IIv1GX4tOSZf7PF2mnITOOwX3LTTiarGnSKv6kC69JixrVESRcBqN1wU2sdCB82L830BiXnQu2v95hiY_inady1i3KEvzJ38pYr40wYUzaoqP5-z-otckOGdyuL_4-OA6sDfTnPJJCW5mGYq22gL2bD-NpNPBHHZVuDMn8k-r_-D3kV2oLXETPGYNZAUeHwBr_VE2gBA36AwBEtyirZxrw0TonkHTeCREAcfTMzTmvnz98L9d-j6gqV5qLwQ_YBuxIhQuJiuruzoWUNug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
امباپه: به جز هواداران بارسلونا، همه قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/91121" target="_blank">📅 02:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91118">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇪🇸
ورود کاروان اسپانیا به خاک آمریکا برای WC
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/91118" target="_blank">📅 02:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91117">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: پرز عاشق و دیوانه اولیسه هست و برای جذبش هرکاری میکنه. پرز گفته این بازیکن منو یاد اوزیل میندازه و شدیدا میخوامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/91117" target="_blank">📅 02:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91116">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdfMUQnCDB2ioRtTvVtTpwXfvB52b8tRHGUbF1oojW0OGJSKS9SWSPN3pGNDElawTFLlSaxeleCn3bAAWUbRxcsYdnJnZCJYHnEvX1MejvHzg95rW9S8_-BOJUxqKI_NrivDhEJVSk2xJdZ-zmOV0Q5pTDUD68wHeC9r-HEiicklV9c2ZJ8s7ifCSL35pPTq3JKdPCfAZ1ONz3lxTt6m5L5qUYzelfaY4Zaz_VGoAW54PSz_c5OSW9oGJpWjf7zaqAAwPSR9VBFEypaX3d8k87IKjXQaxGbYTgxnq2iOiuzgk4txtxwkJVLIcZcciPwG0mluEK-hQNcoKHC-als-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فوووووری
؛ فلورین پلتنبرگ خبرنگار آلمانی از علاقه بایرن‌مونیخ برای جذب مارتینلی ستاره آرسنال خبر داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/91116" target="_blank">📅 02:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91115">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: پرز عاشق و دیوانه اولیسه هست و برای جذبش هرکاری میکنه. پرز گفته این بازیکن منو یاد اوزیل میندازه و شدیدا میخوامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91115" target="_blank">📅 02:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91114">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91114" target="_blank">📅 01:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91113">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91113" target="_blank">📅 01:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91112">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4IlFwb5E9M_bDLscxTh6uDKHjicnG1Haxdi8yj10E36QPdRpaXfQDRnvN2w5F4SpQ0KY1y1I5_luA3lN2ilOlK8eAGCgAJJoQ37aHIGDmba4P-RN9COPZGet295lCBxmmpWrw3xccQ_z9IL6IeXuKC0UlYJ8aWhk6CZsDaSlseXa0oi02q3s3PHzwvMRflForG-Ydw0zdxOUbgUjoSG7sgrunmajZ8qtl0Y4mVoyF8tsAt_iwiYDs7LG-8Mq5kHZUf_-tEKQgA-Bca2z5KSywZigg0VdKx0BJgK3bmTqEMYrgN_RrCZT9NjgSSQ6Rl7rfsGSuVI-wbiRRXwpnRfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری
؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/91112" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91111">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ME1ZPtkAaDA0eGbNGj-VYWk1NSJT402TxtZgUglPzoyuTLj6eZIHVO-uxgQq4ikjCH1M3ULfExbHk3GXHw4KJDmcs9UqnKeS8wBnsVL6DkmHtEKoXCkwZYpG5RzNMJzgYoUOs9NN65IdIoYOyK3egXzLIOV6Yac3vPEsEKjo9h5UiFQwFyPQ0sW8hCIG_lZQCOSDoNi0rgWoftwLOuCr_WnlEyr0FZr3ChutcNGgvL-uVx81n0ovZZ2Jx_H_p7AZkRP-o870vTzstQSCjW8hwtpOCnKdJ8I6BTtChPD5-xM0VE5c-DQEwy198i2X1Kcl7flP_j305zQvdhnwRJoOvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛
✔️
تیم ملی والیبال تحت هدایت پیاتزا دومین تیم جوان لیگ ملت‌ها
❌
تیم ملی فوتبال تحت هدایت قلعه نویی دومین تیم پیر جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91111" target="_blank">📅 01:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91110">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqRmnSnvljh_Vso2kyr___rgrSkN34ob-1Sq5qDk-wmI0-PhrOevpQDYJ3LfRHzDfqExJY3D-tiuN54nti2pX_JjGoVNZo_07jqQo_F5J-xs4L66Qm-yke6yznXGYVPYfDuYCBk2OJtycY5IiI-4nJF3UGHdgCP6KarRPntcDTf9feZ1b0ft3U9XxjNJUyONFoJ5D7mJ-gPFW176TQhvg6DDqRJnwS2oAr1Jy1Lk2lESXFXH6mrFz6ScW7B80L3W_HaTUkzMHU8O5apuFsGMiytKovu9agdGFU-2AXJwgNM9HPaAEPAKxPUNW-mtogOXAyUQFRoBiSR2acyGa15Vwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🏆
هر سری جام جهانی میشه یادم میوفته تتلو میخواست جام جهانی ۲۰۱۸ کاپیتان ایران باشه با شماره هشت و ایران رو قهرمان کنه. بعد پاشد رفت تمرین استقلال که منصوریان راهش نداد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91110" target="_blank">📅 01:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91109">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91109" target="_blank">📅 01:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91108">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iF639NgyTGGVo-GT2zSFldh3LIt0qZDQHrfMVlqN2VjcjqMHpJe0Rp-sops4-dAQ9qmHIR2OMZQZp1_ghBmmaGnZAoFa76w4oV_la80BMjivYGBlxCH2Qljm1WhdCf3CWUcdL9YzxGrufhtifayhQiE2BbSNk5JJrt2cIBJYvkERyiVmG8mML57ctZXWg-smuYkkAlXf-4LX34c0bDrircpTj0d02hx4mwNVoDRqBJX3XkaySpQzk44ZnoOc_HNzhwcu0pf9gIT0YsCtB1I2CFB2k5BhHvNgzNlUHwtEqN22L6Hx2Oa1bHK9Ols5oQTAjU7KVxjcAcUUvZWbLwtmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ یورگن کلوپ اعلام کرده که در سیرک انتخاباتی ریکلمه هیچ نقشی نداره و الکی اسمش آورده شده
❌
هرچند رائول به عنوان نماینده ریکلمه مدعی شده که اگر دوشنبه رای بیارن، مذاکرات جدی با این سرمربی آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91108" target="_blank">📅 01:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91107">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
#فووووووری
؛ شنیده شده بخاطر توافق خرکی و خیالی، پدافند خارگ فعال شده و سپاه داره موشک میزنه سمت تنگه هرمز
🚬
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91107" target="_blank">📅 01:21 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
