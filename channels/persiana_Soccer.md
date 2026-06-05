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
<img src="https://cdn4.telesco.pe/file/Lsv8vrJmWs7dCo4aRLyxfGyVD5RW8iMEp4i_borQ2Ow2SZBPiVGjf1v7ohb_dH81uHeMt0nH5ED9BoHADVlz68eo6Zdn5-sTrmRgUZ5qwQSn8iN5Qo0rxCaVYWC2Ass1mlWo1wAV_on2AE9gpmdl0KhtnjZQZBQUeKOSSTfAk_cTenZLT-Lu7BwfLxYO_heU9D0s6xt_EGcVSTuZIdWJyxhpSuLZrMFB1_bSpQBf5sMeODEfQCoKW7OphKUkzuy4kyCL58NJAonai93wkfIp1RAayTmb-3re09CV3uprefRQHlI2ZP-yJONn1KZdkmJXSXM0NK6EXKWhuXBFJajCqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 174K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 17:57:44</div>
<hr>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE3hFsPmyGp-nfrFVHJ8n1rHIqo6g5bq6nC_fGqJPWcdhpFIlN_ZBrO9aDB9ufAAAIlzS2U52y8DgIcftcxYn4UWB-qFg_231dj1wKNo7D-L4Rtd03nysVukYq9Thg2oVVJmiqzvyY_l0RPXI6uqP-YrkwkzZ1gTuqiBPoGjlm547Nju3Cc7gBzvH5xJBetNWN7qS5ufSM_kcl9cL6-yr8eDwbGpFiSKCZo19BFx-L3SNFIpJyrd4g5NuyZIhcyUsPlpy-HwQTqemTPiKc2ZPhclnztLyCNuZXQFGsygy5XlbZ0GtcsUsrgSG7i8RqSCV8OnKCx6YgePPpWfjm0xGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/22832" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG9Wd7ulGCBm7wIvWZkHPQabOhkIizA7TfoSZatjXW2IV8C9x-941WKFTUldX-lDBwrP9XTXrTus3XdGIPnkEgx3YYtUXpnq3BIbHdwa-BKUOUTOtEzuBcr6pZGmLJAsJ7u1vz1xbbCzlnpOKvw5ZfT5zYVR_3Wl1XXlFennYza-dfbXQdmutKT_Jai5XRhA7LzZYM0tOzbl-kX3UH_xjJJuiB1ijZiIZrRMCWoIpexvWGEcnClAhw2eGUqsPZ96nvQ3UXxgeTdzQKsdTGlV1FGJK-YjvIkP2n2wkoT4LsMcYoWIPSLKgwEPXdLLyM_1dTRgy3ZFVNOcbizFSRfliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛‌خوزه‌فلیکس‌دیاز:طبق اطلاعاتی که بدست آورد مطمئن‌شدم‌که‌منظور فلورنتینو پرز همون مایکل اولیسه وینگر فرانسوی‌بایرن‌مونیخه و روز سه شنبه پیش رو آفر 150 میلیون یورویی خود را تقدیم سران باشگاه بایرن مونیخ خواهد کرد. خودِ اولیسه هم در جریانه که پرز میخواد…</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/persiana_Soccer/22831" target="_blank">📅 17:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNxtcBYlq-ELsdT731GzdXyPSIZe8Sc1CToVICoc9RDusXKIR-LDgV6OAm_ZBTnJQuGgKynmh9zg7gd8vie9ZdzzMN--wuIpMvNwA9LHTWoQCFsD0Rxw_pRa3WJV8cvuQvRqGE1Vl46IhQunyAh8Va-YExS80aVUwY_Fkk67LiKQwHOJE_0QVlrGwan7aWji572uIUMthCg4mvD6_RhPvyNY50nmv1jbF-tQYnxarLXyI9Xq9OGyEQaObeljgkZ4qDtC7Zzn8IertpuxCwsEp8F6lWkbg8zHHP4-HRIQ1AGcwM3DdnT4ZLJJBqPfGXxELo-1IMqXI6TQl88wXyNfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خوزه فلیکس دیاز: علی رغم تکذیبیه شب‌گذشته فلورنتینو پرز؛ باشگاه رئال مادرید بشدت علاقمند به پیوستن مایکل اولیسه به این تیم است و قطعا در این تابستان برای جذبش تلاش خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22830" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976cd07773.mp4?token=UnB11S1O74pUpV2B_0zqC3MS2DqBt24wWSy9KgbVBMJxz11eNIpMrjGldFGUn3QQ3q8HtWe3ozaOnC-6f_9peQ2ptSdE5HWW6HXi06dTrvBRwr1yBMoHbWFTWrql4_GXhcm-d94jHBs8jCl6XSjqMpxuYvi9UKDSpGAu22G7xxlvlKjuf1AvuIW3xQM9ly0gzyi7TbMAGNHl87WjQC1x89L82ywzZbsnt4ef8s957Ml_tBFYfCgOy-ifxZ-7GW1Onwr9JE6M8rpRODLTW1vJOSSl6eGVPHzN4wNmto5vuRQY9ccipiDuTlThZP8TwmyJeSVAyZVcuGAVuhrJQ_drNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976cd07773.mp4?token=UnB11S1O74pUpV2B_0zqC3MS2DqBt24wWSy9KgbVBMJxz11eNIpMrjGldFGUn3QQ3q8HtWe3ozaOnC-6f_9peQ2ptSdE5HWW6HXi06dTrvBRwr1yBMoHbWFTWrql4_GXhcm-d94jHBs8jCl6XSjqMpxuYvi9UKDSpGAu22G7xxlvlKjuf1AvuIW3xQM9ly0gzyi7TbMAGNHl87WjQC1x89L82ywzZbsnt4ef8s957Ml_tBFYfCgOy-ifxZ-7GW1Onwr9JE6M8rpRODLTW1vJOSSl6eGVPHzN4wNmto5vuRQY9ccipiDuTlThZP8TwmyJeSVAyZVcuGAVuhrJQ_drNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ابوطالب‌به‌تیم قلعه نویی:
شک نکنید این تیم قلعه نویی تا فینال جام جهانی میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22829" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6qkZaSKlI38vCC_C0TKps5yb5OqgxMFAuoSKzRXm2BUVE5r9GBuxMV9zv28wyHIqFQqLc85dgwjQa-7jtlJLHExiAg9KuDeCbY8J0GXWoooNIpcR3yNYT6fqB0I7DiSa-0g1e4-cznephyYGYwwOSbPqpdn9o2EDHYw_sRN-eqDi0DfKMDIpADcO9rUa75DTveIMnz1JEEbBppsRPyOPqLYdEiWPAUdfCA_SwB_vLpxo01f2hG2Y__sSYDivhkrBb3lvHEqVfSb3NR40wSoJ7cshi5aVUc_kp_qoNUdU9jkPjQY320yQPSkY2qo6EQMBF-kOveOmgyF4Q1B9JPd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22828" target="_blank">📅 16:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBQoog96Hjsl6IhJqKM6bQ2Mw_zS_R9KeNpr4bMokawatBgHNaCBQ4Wnnloo5-9tgmBGQ_w32Ihw6RawqCCrqGPOy3l9D9mxyG5DWugo804FsiyaHcqa01Wa-dDjV-y1rEoUmM5bZHpz0avaPZWeYLmQdgC4hX0IrWj-vddptnUNg8DO3EJD3Ij8aX-MkKhxa4WpA--03I4080irtaSEdae_VlC7udZflu0vspqvx3Se6lIPzqRya2I0IfiLxVNGVINKlGBdRhdc55d7BSylyswEyA9qm7Mzbq79JD5q87T3BdQKTwDm3nEUve3wtIi2IhnEo2rLR-ru_FfvAcugzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/22827" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=qicaGmDZe6lQdRpwaD_Co10vFRYdUAWYpwHsLMvRA_QYHi0oAzudJQUtLBCFexi5IQi-IZSldQUE6DT-_Shx0dol9ZWzdzW5h13j3WNz0nBEuJmbu5JahIMrrI9cQu2zcmCT4VZIFrQKkrLdq7C9KBnHARM-VtIWOcNs3ETz6K5jtiuUh0Ns2L-jh3Tv8PwhCvtxO0iLpLToTwAUKqQcK7SPoD1ROBwDQuL58dAf8Qrt1LTr8E2_0PctWgeK-hgBMNZsHkrty1Oj5rQ-eXOZrmhZMeXMrDEcH3bbrPftcsn6v8pPFllGYCukme9xu0TLNmM8XPdWA0jOFrFn-QHPoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=qicaGmDZe6lQdRpwaD_Co10vFRYdUAWYpwHsLMvRA_QYHi0oAzudJQUtLBCFexi5IQi-IZSldQUE6DT-_Shx0dol9ZWzdzW5h13j3WNz0nBEuJmbu5JahIMrrI9cQu2zcmCT4VZIFrQKkrLdq7C9KBnHARM-VtIWOcNs3ETz6K5jtiuUh0Ns2L-jh3Tv8PwhCvtxO0iLpLToTwAUKqQcK7SPoD1ROBwDQuL58dAf8Qrt1LTr8E2_0PctWgeK-hgBMNZsHkrty1Oj5rQ-eXOZrmhZMeXMrDEcH3bbrPftcsn6v8pPFllGYCukme9xu0TLNmM8XPdWA0jOFrFn-QHPoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22826" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22825">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLkW_Ku4GGJRCN8ObjzFcJagdBOycFc8s-RPilrEotu-sInHI4CBH98gIQ42lEDO3mFJ1fvqx8s3dUE11yxzfWXfEIQjJj3vpQZKl2-aKLujT7mBf6k074-gVpsPPbUVg84XY__8X0I3UlJhTx8vV1TzjtCdCQCv8cXUBubB-Hz6Coa8NbOtjXOwDg3recsVkiFNoUT9-zZfki72Ssnl2wMuAHEQ-VbYvzH6euc6zNwTwiCLluTMCNhlfuMgW2ox-oQN4NmMzWZGfRaW1aWKGG4YUvzhO2sxw1PGkpP_FXzZK4J46GceGWAXbNyvaXpQc6dZauNJkf3MjJDZw9wlNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل هفته سوم رقابت‌های جام جهانی؛ از روز 3 تیرماه هفته سوم شروع میشه تا 7 تیرماه‌‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/persiana_Soccer/22825" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSXqovbSPHInvyr0AbfW6nlR9D5p9XWFrAB5TmHm84aOtZ2maA-xXks00vmwqqElGlkpk7V-CPkKZfL1udySzunGW0HktjbxOM0Tq5qwr86Xfg8BjaNS7g3I89onH3Gib-GveQYPBlZQYj8hjwkxOhVftX8Q3ywsO8vAmO3gEIK7dhZTJCOji9c-snGuI_RssdqxZSBZCyBF4hVA8fHbIZR6Mcdwq97IQ5I1USO50FSQjUFPH1nwb7QC1GZ-uy41NUDACO7_LwAxB8NnewtiTN4NtfkyhXibnOgMvUBB3aVKgS_noLhiyjSghXL2XfPhDwmkQnEiZUlgrR17LZFx9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نشریه‌ کوپه: رابطه فلورنتینو پرز و خورخه مندس ایجنت فوق‌ ستاره‌ها خوب شده و مندس به پرز گفته هر بازیکنی بخوای رو باشگاهش متقاعد میکنم. ایجنت ویتینا و نوس همین مندسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/22824" target="_blank">📅 15:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUlTqLkCFsKe39hHDOGyFmLD-WvmYlYJoQaTxNehfrEhM9YsDlD3OAjNlxI4aZOxQZfJZpY51OKkb_iXNXKeXXkqe-4_HprEgVLAm7odJo3tIbJKuZqqokMJXxSXR2Mpt5gt6N0n__x9ANeKTHuB7fVaKnIca8KZut4FUXZvZpj-XNn1Ehk2MKCMMNNcjh3wJMbERKTImZtSCKAKjJ2DOawE_dtNXCF17P5G4c1FRH_gbP-SewmrPE4PqLJfGJBORLNntSHwHQVwqf8ljYTgqdt2HlVWLXGRxxGaz9amUfi9ukDutqk9bPVhvyF4aGvi-lA77sAa2w45swTVQdHfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22823" target="_blank">📅 14:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoxIbxpO63KOHbQ1lBw1gXafGYDzXfL8l7z-UyTH2ahSeoVBmy7k_uoaUfIauBQe3yYE_9c40xeVsj2Hhk33eAHf4PNVeAIUcbNOyhsBU3QO1i_TGDwsU1OZe1nR0XDEe0IOe8yDjVXFKZCS8IXgsPzbs_x0iE2srNARVrfc5hiyuPwGTahf2ob9yZecx9klIST79SdGt2YMGrBxzmZp0KskHWeIIisvIbNxUL89SVpaYBjiWUcJyhlfIY1dbUlKTo0K22XIuYV0-JfOb_hE3j9NKR2qka8gWY8jqm5qIurZ8NHInXKyu03NKdn_F2cLxCC4lwqSG3jyk4Dznh3svA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/22822" target="_blank">📅 14:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVGcYPkLYw4OJiSfSr4_1jNl4rJ6_VvSksr_zTnYxj7MRr46g7x9SwZyd4Ei_kAGWeBHQ33Zooaui195LH0jKnnSThtPj3NL4CA-ZxG4pMyNzZWdG_PahNfKiIx5yLbC5927v1Ork76odKAdcM7HTLX5N5QTcjhQfypy1gXPrEsCWiqmRQSJIqxT-ORyFc1TngtKh3hWn-c49eBFDtvtawij-ForHERG2IrTJkPRB_13Rf9brKxzHV-9rNGDtNczMsXHVIHFJ8we7xlsczLKoU1EHl5p94Q6PYMMRLb_1opyJX_MvV0TmR2cJ4faRyoyq1lJOrt67bfEhlArcJSxHihk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVGcYPkLYw4OJiSfSr4_1jNl4rJ6_VvSksr_zTnYxj7MRr46g7x9SwZyd4Ei_kAGWeBHQ33Zooaui195LH0jKnnSThtPj3NL4CA-ZxG4pMyNzZWdG_PahNfKiIx5yLbC5927v1Ork76odKAdcM7HTLX5N5QTcjhQfypy1gXPrEsCWiqmRQSJIqxT-ORyFc1TngtKh3hWn-c49eBFDtvtawij-ForHERG2IrTJkPRB_13Rf9brKxzHV-9rNGDtNczMsXHVIHFJ8we7xlsczLKoU1EHl5p94Q6PYMMRLb_1opyJX_MvV0TmR2cJ4faRyoyq1lJOrt67bfEhlArcJSxHihk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی‌از عملکرد خیره‌کننده لامین یامال ستاره 18 ساله بارسلونا در رقابت‌های فصل گذشته لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/22821" target="_blank">📅 14:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22820">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhCfUhG8IoNHkSTziJvhAVr6rCQjBQeRZ29bQJlDa00btF49NO9x_XKCswhFybbA1V6YX7Src6eWZ0h3iTI06OhTTSG10-UCClFa_U6Q2jFDsgXoayr9EEv6KRHoUj_ltSzLBUgoxhojU6BZ0cTEm6g5Q1p_YEGP7LNgvc-4fyz4XSKyoe2ot22gbvE0HfSEhrPmNfm4-JcuyixGk6rGgPScOneQSThrF8qGyNG7lOqq8RG8nmC-dsNKz3EbL-2svsFiG-DV5IpUyXr0K7mtwwkVGNYez0pZkGaz0lNyr_fPZiXBXbyOd3twcP_DJ-hHp_2LR2DT60TeEH50U6LqrzLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhCfUhG8IoNHkSTziJvhAVr6rCQjBQeRZ29bQJlDa00btF49NO9x_XKCswhFybbA1V6YX7Src6eWZ0h3iTI06OhTTSG10-UCClFa_U6Q2jFDsgXoayr9EEv6KRHoUj_ltSzLBUgoxhojU6BZ0cTEm6g5Q1p_YEGP7LNgvc-4fyz4XSKyoe2ot22gbvE0HfSEhrPmNfm4-JcuyixGk6rGgPScOneQSThrF8qGyNG7lOqq8RG8nmC-dsNKz3EbL-2svsFiG-DV5IpUyXr0K7mtwwkVGNYez0pZkGaz0lNyr_fPZiXBXbyOd3twcP_DJ-hHp_2LR2DT60TeEH50U6LqrzLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
من خرافاتی نیستم ولی شما این بازی ۲ سال پیش پاری سن ژرمن با حضور امباپه مقابل دورتموند رو ببینید؛ واقعا انگار طلسم شده بنده خدا
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22820" target="_blank">📅 13:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpx5Ka55OW9YHQLCSKA2yWfYS86JGDwFjXhlgBPKgeZtu8Ttuwyeylhe5KM3vqzVRjIjphvAUNoSf2xCxf4VjnfKtz01ymEzBVAC7U9bHzb5FWBOUUGcPHFIZrZKH1b8z1cP8PO9-LBGO1z_VQUw3zIgIt0Hv0Y57TgyZryxokYy4zG98qy1RRY513jVzKLn0DrOD917pbkWguLDofoPfbFU8E_qgZEyDdZpOHQhGj3Xc3uR6g2rV8qCEAC_xuiDPBPosERErkWXu7YjZtbpXtL3Uha2ELRjAx_sR1jXJrd0BJ4Ss78aFUOmeFI-M-3PlDBYoqNRU6wY-wBgP2Vlzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
#تکمیلی؛ باشگاه پیکان قصد داره درصورت توافق‌ مالی باباشگاه‌روبین‌کازان، رضایت نامه کسری طاهری مهاجم19ساله و گلزن این‌باشگاه رو بگیره و درتابستان سال آینده با رقم بیشتری به سایر تیم‌های لیگ‌برتری‌بفروشه. رقم‌فعلی‌رضایت‌نامه کسری 800 هزار یورو از سوی باشگاه…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22819" target="_blank">📅 13:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=C0G_EIxuFbyz8j2DRT1YTHuVWwpPaRBEaKylG_AjYG0ngjs5fE7iWr4uJh5TWZ4n-86xDJ_Qn7Zs7BLvINIJptQZqSnaSUhywFL-xa9a6pbRTqZhIfmbqqCxMJCOpssjjehmxkdYI_zF92mMOTm8sCSXmFzT1IzOz0qlVK3qMZPj58f1XJsqa8NqYnf0iJDl_h8ctDcigvp3gzCqvz2ShYacVTHJ7mi2otgdszxQhZfcdDXAMXny8fXVLx_EvyPtzGdPs_gsPWV5yVF1GrGyWQC5LNY5vSb_1HN4B0KAb5CPNR1bBA4izQIaFcXKWUAZhMzTi4GacGNE1w4q8hUj4FNDcJ64qMuHVWAmF_K-Uk-S5ZOIkpVebXSgUllARW3Nv61d7Xi1oaVh7Ocbi22pPu1Gkhb2TVbJxUYG1lcUUr1ijm0mA0diGZUFVBknw1ZXwrLlHI0cbDr9AFCbfHEcEoU0EB4BSJZkSgnOZrofip1f1TjrCBvP-CHKocMd1OAFU4oQ3b7OQSgkehwFkRvi6-trVWrGUQ8_xHow9w20N7jif_4Os25hKKFlL-tX6IBoc-7FE5RQXHyWV2A4PSjwUyo3ptkQVxQ-j0qQKlJvjy1VSVlrdZe5nLlroCekOOHlTYqSWTYDX8tniVB8GrCXUEPuaKt7dW0Eq9udSJkoEO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=C0G_EIxuFbyz8j2DRT1YTHuVWwpPaRBEaKylG_AjYG0ngjs5fE7iWr4uJh5TWZ4n-86xDJ_Qn7Zs7BLvINIJptQZqSnaSUhywFL-xa9a6pbRTqZhIfmbqqCxMJCOpssjjehmxkdYI_zF92mMOTm8sCSXmFzT1IzOz0qlVK3qMZPj58f1XJsqa8NqYnf0iJDl_h8ctDcigvp3gzCqvz2ShYacVTHJ7mi2otgdszxQhZfcdDXAMXny8fXVLx_EvyPtzGdPs_gsPWV5yVF1GrGyWQC5LNY5vSb_1HN4B0KAb5CPNR1bBA4izQIaFcXKWUAZhMzTi4GacGNE1w4q8hUj4FNDcJ64qMuHVWAmF_K-Uk-S5ZOIkpVebXSgUllARW3Nv61d7Xi1oaVh7Ocbi22pPu1Gkhb2TVbJxUYG1lcUUr1ijm0mA0diGZUFVBknw1ZXwrLlHI0cbDr9AFCbfHEcEoU0EB4BSJZkSgnOZrofip1f1TjrCBvP-CHKocMd1OAFU4oQ3b7OQSgkehwFkRvi6-trVWrGUQ8_xHow9w20N7jif_4Os25hKKFlL-tX6IBoc-7FE5RQXHyWV2A4PSjwUyo3ptkQVxQ-j0qQKlJvjy1VSVlrdZe5nLlroCekOOHlTYqSWTYDX8tniVB8GrCXUEPuaKt7dW0Eq9udSJkoEO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازلحظات خاص و بامزه پپ گواردیولا سرمربی سابق بارسا، بایرن‌مونیخ و منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22818" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGSe_yr7L8gtPF5O5UB8hiKzidkSEtP-rHAWxADSQsRf3RkRmpDGDbzmv7OA2m3TaauCY29ou79X31SKHDGeLLokViAvCoeboS7BklryKW657VLHWw1ZmAAZZeKAy8Y9oXLOUWfrl9JMexRnFhh3TqzvPpF8U5pLrPd0jT99sv0cSqsL1CI-zqWtoQwSoXCQefIuSZfjrlcIon-BP32aYbcrE-Qgd0HidSAURpow0eQVNSaFIT4YifK3brib49XONq4mDjNOGZ90g4E6uZw2zfyoJ_zx31ZNNcL_Pn635Uw3U_EPm7xR0JD-rMEKvDOze3c8-eIOEwolzaj_zxyLxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22817" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22815">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=KkOFlYed8om7B5G_NKLAPxvuSy1DbuTNrH3hWp8OJbtT3dLBvNxtIuRC_PAsfW-rSYqzTSacsaQJpNZ6k2e1uAdTSgmZwguM4Dy2JzuAEejw_Act8tSn_2YOmmogiApk7etgaq_p4uuacBMCu0IxH_PQSkaDJuTiE7KxYxcpnJixVIil0tZpYBTSW72qAsrENSJaTMbqJvzqWeWGfyX0lrfuD8iDxcnqD9RQbLp_Lbyc1Bhjujb09V3GzK1XJQeC1y8VJVxtck1k5IFIDZpWpYcrSVOA_GyCv2oKpTuy2rX-_g8nTFH5fkt2SHgckBvxq0OGTuLv3y6xJmOnHwSodku3MWXKCd6hwiG8x9AHDkxxIf8XFBPLYN5uNuG6UW7vz1juxkWkr9nseNtCILIpz9rFUVXg29fZwUEcv3t8jVfcR1LTZAZk4iQNh4ZVazdW6ZY2crdypgVxQ4D12aEnE5l24KpVaMBTwf4GkfVDd5Lj9EK8-9-mKqu67dnSbLpg6EN32Tfx5Yjm8onFEB9B0dLkyttFVAEY2wVR0lSRnp0O9h9H-EL4lm1_gdM16R_OP3YeSrXFUolBrsj5hfeyV4esD6xQHWeQsF4li-mm8U8u1hZFSC-t74ImHR2RIZEl0_lHOMXKy7h991-YEebgYXg095DqIvziVahONaeP6hI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=KkOFlYed8om7B5G_NKLAPxvuSy1DbuTNrH3hWp8OJbtT3dLBvNxtIuRC_PAsfW-rSYqzTSacsaQJpNZ6k2e1uAdTSgmZwguM4Dy2JzuAEejw_Act8tSn_2YOmmogiApk7etgaq_p4uuacBMCu0IxH_PQSkaDJuTiE7KxYxcpnJixVIil0tZpYBTSW72qAsrENSJaTMbqJvzqWeWGfyX0lrfuD8iDxcnqD9RQbLp_Lbyc1Bhjujb09V3GzK1XJQeC1y8VJVxtck1k5IFIDZpWpYcrSVOA_GyCv2oKpTuy2rX-_g8nTFH5fkt2SHgckBvxq0OGTuLv3y6xJmOnHwSodku3MWXKCd6hwiG8x9AHDkxxIf8XFBPLYN5uNuG6UW7vz1juxkWkr9nseNtCILIpz9rFUVXg29fZwUEcv3t8jVfcR1LTZAZk4iQNh4ZVazdW6ZY2crdypgVxQ4D12aEnE5l24KpVaMBTwf4GkfVDd5Lj9EK8-9-mKqu67dnSbLpg6EN32Tfx5Yjm8onFEB9B0dLkyttFVAEY2wVR0lSRnp0O9h9H-EL4lm1_gdM16R_OP3YeSrXFUolBrsj5hfeyV4esD6xQHWeQsF4li-mm8U8u1hZFSC-t74ImHR2RIZEl0_lHOMXKy7h991-YEebgYXg095DqIvziVahONaeP6hI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محبوبیت بسیار ارزشمند علی آقا دایی اسطوره مردم ایران و فوتبال آسیا در بین مردمان کشورش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22815" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM8fKmQVyit-M49HFdlYRRdpqnfvrcM43-GEf-LrC8T-f1B8514NYQN0eVOeZKgXOfZILMJn2HMV9feLaLjt3bKccuKkp3Ro6leBq-9j41aASuix8L8AdfL6esTcNLVPkOAQGQ-geDgoYupHEKSilxLVweZpGrNVInOzifBLnqSa88hLfb9f-YxifNup1-L2fT47WF-KRWKHGGSOjLx0M6CCDZXN7Z7icpJ5BJnaYaHQPDndZJ3dIEiQlQn9NWjN7YHNglrFKBIuGLMM8aWnhOoMtCY-TEZgBQ3rUDBUlf8MWTuNkFG57hBFMULkAT8kWR08mYDB1dhn8jQfaRr-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22814" target="_blank">📅 11:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtK_YfCM9GsXk3BV42kPd-2YWk-TbUiz8GoQmjcs2jk7z3zVdA5XQK1szXPMWqkJinh9eZwDvx-BvWSfK0M-F1ZFgI6xV19c_CI11BEuYQN7dzUkQlN1EF7NRokr2uqZ0qiOZhH9I4WdMhXhWIHB2iOBDnMaCaiL0RrJQ7AjCK4tPZkgLiu98NFkiZhTF58eT5MR7hqvAFN1EfNvsQbuiSe4EATvx6nfHVEaS2XoleNlMrzHJznwEE51RGveu8kb-Hw8OFZmWWrpph70vjHSmdh4TW1k54ItYPIMqfPQvigEeA1nm7Gvv7-zDdgz1dXdlk3kTH4nAQd4dhjp8NtgDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت باز شدن پنجره نقل‌وانتقالاتی آبی‌ها؛ باشگاه استقلال برای فصل آتی رقابت‌ها برنامه‌ای برای تمدید قرارداد آنتونیوآدان گلر39 ساله‌خودندارند و سنگربان سابق رئال‌مادرید از جمع آبی پوشان جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22813" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRMy5A_GqT_9cC8wQEWbp1UObmCC0Ige5bi0ndUJQFs3Hfy5C5vi3SNa2BdZK-F459oVuIKVhbGzrYuQYZh1YudhUMvsaaajE2hmAQJzepgiLnlHNbs6zzzlo89Q_gq6WfxtBb4OpjgliZlom2M-EaRvjS2jWUJcsEAsG3yC9gF2bTMu9AXcGApxpnhfzFtIvuNbREeR9MdlJXn_laz_4NG9dubIyyEtkLlOM2-l-gMi8qG3yTs0n58gmI4A2OFxBciewtOVYAuyqoanN_mgPwQCLXfPaBpn_m7tEL5U7iGpMDGiFC8JBqbdp48U5hsBCfrxG-IcmFqrvNXVI0bjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
👤
طبق شنیده‌های رسانه پرشیانا؛ سروش رفیعی هافبک 35 ساله‌تیم پرسپولیس که بازیکن آزاد بشمار می‌آید از دوباشگاه‌فولاد خوزستان و ذوب آهن اصفهان افر دریافت کرده. درصورت ماندن اوسمار در پرسپولیس قرارداد سروش با سرخ‌ها تمدید نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22812" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22811">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚠️
خیلیانمیدونن‌که‌اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس‌خوش‌آمدگویی‌تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22811" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcmL1slTDAoSIQcOEA_BeN889ocNz4frm-twDHD0IlBc3Mkc52ozW3wsRFTLDuScPewjK_qAdfjRRrsymBTrjVAbGadXVzdRW7SxiIxlPxJnKadZE19jTxuUJQXKMnPawCcoAR4uu99t4qrlKlMhBXGZTA-GOKvB9bZYdJZLlgGv09m2PMHGH4kZX6B_9Bgud6tb9Pd37RW8AiazQU281tgTQOM6eBGEJPmABk4oFd6l4ucOudX1w0A_txC_us1721spEojV7-pXqu9rMiQChwyuftYFRON7fUJCXK3_l_PzASqeS2FUEDlx8cP8_0i14vR3AVjhSeGLzjAxSokaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22810" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcmpzYsLJUBYrcGvfACiXG6ZL6xGcKGdmYNA5PBjcb4pqRKfuKFNnBAmg_Y7CB8HLyGzJE3ULFO0gOIIBUF_6aFYIrofwHViuK2Wk_htCFmHs_DgyjoCMS1ZDvGPvcAauEaJk5uGSSFRH0wf-FBzw7b_Bt8Mg9ayg62SH_-0-YwdMelKEAyu9hpqyPOphYdtm_XNBN6C2LqSH2nHDS85XyRVixtFnqsJ2trIqF3FnBPQp0l9g3DMnrlKe47b9J5jb9ofn53WnGIw_xWQjU9R4uYtnKD52gVSUDtLKDxwTV1GN_TJDvcwXMUmheP8T0XLJYk4zhMf9hbDSk4h0Cq5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شماتیک ترکیب تیم منتخب فوق ستاره‌هایی که مفت جام جهانی 2026 آمریکا رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22809" target="_blank">📅 10:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22808">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHw6CB8TEP17boMyUP2JuWXauXs8UaQtvRF6ktfTsQ9cQSB8s0QFqfhfifOqoiWkH-8gpup_VBjHRXGkMdzBlqy8MrHhXnS5m2Pfm0aInbeqgBEd50j6Q7LujDAwdf_0l8VngiOHiR3Qvl9KYz__p4CcpbokqHG0wpib-qpwMlOWD8NaUudpW90YaDir2x6Vk2bT865EYyB9MHmpU07qQbgdoOpgwB1PjmaNiyz9GnUfm56scI1thRUh4EyPpr7Ks2Tf3qjxorxhYXaAMdzWTyL9PejmpiyV1DFK4dGuoEF1iJBhlvFUvHPd-F0qTvhhtG4jVYFbxtM0POAjapVDTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22808" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1n-XJRAuopI_ppvWLDhKXCjYXG228IvBK0gsv-KiT0Tz9AgKQRNqgEevCT0mEaD4GWMQQFwFE4uJXl-IxzPdrnoZzBmoo8aYgmicw22rf3UTq98aslbcUesXgOMzsY67oVK6SMMBBn25zI6ZpPrPUqSo1wtVhIaRHwXllb_nq3eMYKk2Ghv-631H_e36OvmMjETwBhw2tgalizmqgZYveFgdCxr5nwzwuMjOGfBYA3EGhSOLN0alFeNOBQieLh-wPUPlvveyOMr9wxloW6vM6XCNdpLECU3qy-zeM6YuWEUn89HZYkHpoAbO2-HE1_Awru3iAubdKd0isMFOVFS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMbFNnOY13US0MfjIzLB7zS-y7MHt8TYpTeRzA2HaGS00IG1Dn6bd4T3-rpH3oL3HA5xQk1OVK__0lyPFf8HtaD85Df1RrboB2vVd_dlrgOfN_y8zheNo5kXCMgmABz722B-YFGq5l0tgPtAG_CAgiZXhGvk3LDfReQpAOlU2TN_UIIPLRE7wAQMOpe0e6aTE_KsXI6y4xX0cgIZ2EjzsjkfZAGf1OuLlKP4hp2O7IqGOlk6YTtqpJb3acYueAI91JZr1NsU1HLpNqhB-WlHOypOjp7iIt8P3QHZkh3qTHoOPk5ClUZ23_XcdcykYPPVeG21afyrOgPkLel5KiiSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo6tGIHDxDZQiOXSYa615zf-EcBUpgOUXisVB6aTyGIRUZ12XDDyh00ddMmGYov6iNP9qAf9nRuAjNgJwzwHFSlE-tFfnq_yHfhQ-wJ3syn15H1ap8J2Ezb1laMuSOJCkmXQhiNYR3ST6hAG2zNDViyj2rj2e0X6her6ucN2jJBjt8lBCHPxbh4iwt1TjykoPGzqcgNqvJq7nH3kKqNUDTt9Mn6b5CVqvTVcL89gqvbR1_IYiyHwPb-B0ThkP23bgSnOjapSeD_2uI2MvpFO8QCQrYNjJ-5KZvz5cw8RQ_rbv3-Ry6-yfDt7BXlnCdNl22vDTF2g-_vnWwBaSRki8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTfYhERNlQo_48JnGMB38Ym4LHr9uIRfnv2_GgTXVUsNL5WXgpojte5LPg-TcbXcz8Yu6bnddbBdU3YWAI6Oid1w7i8p-XRZiLv6oOTxlPUEVZXHRoDfFOPDARkOhTxKN71kXcX4XtgsdE3OLtJyAQkV0OlRuKilnTjH3Pgfm8RCsUzhK2V_D_sJmefa07HA5ffR2jFOLj5E3mNqpIaIoCX00-hPwBGlxlN0aqPzeWh4vg1XdEAV6Rn0K7Fux3y7ChtV9wmO-iA6pK5YMLQ1cjYckjsJHPq5KbyJwpJ0XX5gjSL3IpsIYXs3rChlSCuFttHSCJCr6kOZ8j2-fEpU1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgpAVBh-87OYR1chUbEVnFbpPZcRQFgEcE6CSWIaCIOUSPLRtefAUR-SvCVrt2wZ4_VtRSoyVQQJ1COeMi_DpfZloMeKEC0hWwMD3jUbEHnvIEO5Lmf3mmFWdvw1jnZeprgzPshO7eGGXsLDanrJey5Dl-hNs28GzSFyCQfJX-Ec6FXEmWZXoCtIHkaQYWWRGXNr12r0F0IhjBT73uMMLEGM1vepmk6jJg-JL4XaFzQOHo6vIZmVX4OSZnk-t87cIjseAvD4LiaGKhc9J8WrJdK3H5X5DphVXZhAbsgjarmsAAEcM6i_9D00u3ttWEtBF_EnL2-IKmSNSr2Wu5JSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22801">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGl8ew9Rk4J5Lx_WTE1-mu6oUbto7fYiyLkrhaVNmSLUeeVVNFG_b9z3R62PNw_DPlicmpW5srvAnxjP3rhEQE_EEV0RbBAp6Deo9P1mHzTpzGDoaMAuNWUFBcCWe5Oq8kqiuA2vJeYPkpZsFlkhgFa5dKBlXzQPY9Wra_ZdzbBfj5SJaVrNBtF_IEEUuCILUoz3TO393ASw8VngQ6LwjQBQVPvA6GXmexw4JJRTVJgFQpq-W3pQ8XT2WsvOaGwBEByjsAoYjvHiDmc5Bh-WrT04hXnYWGr_Rd5-Ii0g404e56awWO5SskJ6T-Uu11gQde4L1-QkvPuPVcvvlgY8MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینوپرز رئیس‌باشگاه‌رئال مادرید: روز سه شنبه برای‌خریدیک‌هافبک از یکی از تیم های لیگ قهرمانان‌اروپا پیشنهادی 150 میلیون‌یورویی خواهم دادم. کیفیت‌این بازیکن بشدت بالاست و بارها علاقه خود را برای پیوستن به رئال مادرید نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22801" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22800">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=vz3L8TZn1NFpnkg-KXd_fxQtS7jM5pYm9epHSkJPvcYvaM_Lu3kE253ndb-z9LXuhuBl7gi-mBl0ngT3e6mWfPzXxTpUF4fDDrqgJWyYcKv7cgGST9_JbWFxox85v7NKi_5lGxOXRtk0u2bxZTdRCKIxxCn26kK-QRWCZ8abbBQO67_OyaP2UmGjOI-7Uq64uG_QqFjFQh5eB7WqrfnfS7HODc0AGB_JqoPeNacgJFf1Q-zSlWeyrrmRFtgOn1MmSQCZgmAPakL6U71TUrzU6nK6PfhLcxLrmJMkQVymk7KuF70Cx0Mqs0brUhchECF7gn0DCTT3RySCYg49rEaTTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=vz3L8TZn1NFpnkg-KXd_fxQtS7jM5pYm9epHSkJPvcYvaM_Lu3kE253ndb-z9LXuhuBl7gi-mBl0ngT3e6mWfPzXxTpUF4fDDrqgJWyYcKv7cgGST9_JbWFxox85v7NKi_5lGxOXRtk0u2bxZTdRCKIxxCn26kK-QRWCZ8abbBQO67_OyaP2UmGjOI-7Uq64uG_QqFjFQh5eB7WqrfnfS7HODc0AGB_JqoPeNacgJFf1Q-zSlWeyrrmRFtgOn1MmSQCZgmAPakL6U71TUrzU6nK6PfhLcxLrmJMkQVymk7KuF70Cx0Mqs0brUhchECF7gn0DCTT3RySCYg49rEaTTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22800" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22799">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qx-QA1RzRd4sdWBTfFUeJY8_RMbVKIRma4MAuMml65MwC3QvcbjxTs4j28xVJ8LztI36pftYBdNTdoX4D1Pyge-539ZXsSoM_pvW9UR_PwQlqijECI2AOzVBiVBIG2ibNvrSRG6dQnHdXK6KGoB32Fe3d4dgfjEQjuSliJf4HfpEuMQ7aRq3y1Y19n-SgemdZQdmK0gR2KBbqQV239qEyPKgl7WECYYOac5-mjQX3t95jmgHknGFWU7hvOEi1PXvcandiAv4tY23Ice8Jls7uRZ9W_Bu-x1uKAFGCS6aed9Y5YrT5Ub5s7s6ZWhqS5oiJ5JKhcWovY7FNglbv1vonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برخی از خبرنگاران اسپانیایی مدعی هستن که نام‌بزرگی‌که‌فلورنتینو پرز قصد داره بعنوان خرید جدید کهکشانی ها از آن نام ببره انزو فرناندزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22799" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22798">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=h25VnbofPXMHdoLQIrzf4i_UiFi63p8qZqqnb-xzCGzDY1S89zGpBJXvJXlbCFdYCMPmQ76Lri1SJwHUdGQyedAuEb9yvl-YRf8LdT_2-StzEjQMbrcu0caBhmPzvKQpW2Ygi6aXnyM82aWHtuQUaZeYzAyWZHRwKmQWXn9OkI7MLuAuj-O9YG99RG_KBeL4266VVBVaBNCybq099B3UeSD9AU0_mTX5SPnL6yNATosqUF9i6sDcw9Zy3gxmr-hJ5F9EIP6xzOLzaxTNefAALJV9IMr7GPQy01AUPJbLUxTl7zutSnEYjvvLbp9ysXdr4TtkCoCX1Jwub521RpnTeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=h25VnbofPXMHdoLQIrzf4i_UiFi63p8qZqqnb-xzCGzDY1S89zGpBJXvJXlbCFdYCMPmQ76Lri1SJwHUdGQyedAuEb9yvl-YRf8LdT_2-StzEjQMbrcu0caBhmPzvKQpW2Ygi6aXnyM82aWHtuQUaZeYzAyWZHRwKmQWXn9OkI7MLuAuj-O9YG99RG_KBeL4266VVBVaBNCybq099B3UeSD9AU0_mTX5SPnL6yNATosqUF9i6sDcw9Zy3gxmr-hJ5F9EIP6xzOLzaxTNefAALJV9IMr7GPQy01AUPJbLUxTl7zutSnEYjvvLbp9ysXdr4TtkCoCX1Jwub521RpnTeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون‌کره‌شمالی‌بخشی‌ازدیدار کیم جونگ اون رهبر این کشور باتیم‌‌فوتبال زنان کره منتشر کرده‌اند. دراین ویدیو بازیکنان دوتیم‌فوتبال زنان نا‌گو‌هیانگ و تیم‌ملی زیر ۱۷ سال دیده میشوند که هنگام قدردانی رهبر کره شمالی شادی می‌کنند و اشک می‌ریزند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22798" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7ZjZYd8vcGxJuEk-TSpJEP5efLuiw-mAFh5NHV85rknKCspWQI4hDzNQBM93_H-5Zv1CdJhaWOF6xtwKg7a-K02Pl5KzFNcqHz1twmgPZEbQuUnfjAgM-hwUL3dA4wG8MFK9DWWL4vbM7MLCcfo_f4MwpiLDILfo1cMUMioMUECGYzSArp9c9YDQWAIQV1S4USlVYwGZ02eZS9J6VZwsT2jkDwf-W2pPn_-O9urFYe_oiBUZulCcD1nZZVwJmdrcFqU5uLa8RAv9UKb6gPat9Mi13f2tLBO2YcgKcXQ60bOfl-pEQfYWJ0KuCIJBzOfPCFyW_Uih9QEO8ON4NMNaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ نشریه کوپه: امشب فلورنتینو پرز میخواد یک خبر بسیار بزرگ رو اعلام کنه و ممکنه بسیاری از هواداران رئال مادرید سورپرایز بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22795" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⚽️
تیزر فوق‌خفن نایکی به مناسبت نزدیک شدن جام جهانی با حضور ستاره‌های فوتبال و سلبریتی ها
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22794" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22793">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUlU1bgPRjS-yrg0WBB55zvIZ2lH1O--B-_4ruZj1jMfzY-Ong-xkXH5Qraa-RHi6jSI6eIS4RwBQHBUfbywVvRcHsRfblsDVE8QaqFkql_NDXL3maj2_U8EVTo3TrY7P7HFEpH6Y4XoFIqi6SJz5z1aw2Ms3Enff-E2ZxL3wGZPGo-ySNZnaKkAH_ZSL9rIiqlKlqUlJNbkTgaVejgBndAG__T5RIi4_ZsAptz8Sbt5xLdaU7XZrBHaL1NbytGFv_WBLHMVSF9guDEmiMKo1ISwZmbwRwdVLrAY2gw71Pb1uc_cV3RHiaxQMRpmwh7cfraguOhcQzArg_sBKSZn-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
با اعلام ایجنت مونیر الحدادی؛ ستاره مراکشی استقلال فصل‌آینده نیز دراین تیم موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22793" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22792">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtseKqVpYRZH0G5IiwIccleucSs6ucRwak_PawnkdqdztsRkPnKpoeEVZGFP-48-N74sFMda8DIlYagczrcBztMbVuBppbdK8VPxcXsEi6YniR-ILWQaVauy7cm3hiozgY4Ysgzi1cANGXNEfonPjbTx0Pw5Lwds6_7oVqfWTY_tzZtxwDj7lqIxnDtGUWZOAKDNcf-JNjVSjHgFQ5dvKZz77hho0HhYe7bfHC8kbFaccpTJccDMZV816gItB-LQxRFDNvjoWy9zPCmq6_Vx3K2Memz7QaCiZvWdfrBzBXJHnkWZ2AwuWPDQFguO9XDmFqCrFTfSHWgBJTDqOH-4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22792" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPfovjBLJR6-dBfzj8tBc0URlBc7wev1n7DEC_1zPbDfy5Uw-yr9KkilTv6uCoiwB0QFUPufkbiXdDrWJumBJ2t_vwh0tqESMHngciGKKd1sttITf0D4G-1t4nkjS-BcARwe11O_hWSqNihZvdgBYJqSBqEJYqpKNHCNf-Jim94bkQDNKkIyCGOkbsC79ep3IBIrhmXvyMeKm0hQIfXxf0VyUfSZ4GPHYX3JttlFYZdBtyc18jkAaLkXH_JIY3UrpOlWxIPoq8ASj8ObwyVjp5u8EbcSKdTaPSbKShgVZUVocCEHxW2Fg-GYPjRUTKN1Q8uQovGQidfWOTTurGReEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین تیم‌ های تاریخ رقابت‌های جام جهانی؛
برزیل با اختلاف در صدر جدول تاریخ این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22791" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22789">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHvBUYw2CYBkH9dODRAI2dNZ3nVTAg7mFnAEU1BTeVtq3-IZKZ2lWNyt6YJ6af7dtEUyONALFbpH2Sp8rIsT1ClnoSerq138y0HlKZeQCL9LA6oL14ZwVtEyymgum61pw_tF7XJbe7ySsIQ0z_MR33NDHNxeFvSr9wYwGIAoUddmQQ68Ixn-VNgDIn9scbbCjhJnSd0wWSQ-A--Fz1uJCDHj3kWqIThkLjQuiJPK5HsCBzLUzsbGXFI8TKKSmXceMQEJlVNJbHejSZmNCQTzJ3AdrIjeWBROhA5SO9GaSd0rJWB4pGBGQk30xCGFsTxY2LqoAxaQeucGEG6uB7-1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQl9X0R2aaISSJuBrMtd0FKYt7NzxAoHZuP9h7xOQw4pSzsSHm8oeEqVPd8MRJid0lgQvmz-3veF_kcZg1mUgZtUc-nHcOcB0a-qbqrec4nqTHf5pFWp-TA10qXhIcJCa9xml5Db-0zrPz6ccwaO5FmwvleFWdYvrB7PuC_GMXbEHoqjrlYrxf_hjFbtucwpQ0cGu1MkVIjLhdBA6xwrS15_IdSnZvCg1hF9nNmW3QQpjy7t7tLOFEvRyAySOd8P0myEsJIdMaoCBuDsnKD781tRsOp6owNiX0n5Dy5kiwt1dOvQI9D9Ruvgop46YnHdvrcblnHyfxIbrGdZX2Q5Vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو: آندونی ایرائولا سرمربی 43 ساله اسپانیایی با عقد قراردادی 3 ساله رسما بعنوان سرمربی جدید باشگاه لیورپول انگلیس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22789" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22786">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_IR7cTUN0nX0dbhzEY6iPxm9ovc9hmm-Ad7_CGKpMz3gkz4JZMdPWfy3CMhWWm0WnL69IPCeec4vCsw7rdaY99r15efeXjy94XW7CZu_bRW1Qn6PPOB7RqnwrWu04vZMZFON_swAl06ro1eLfLs1qYjyk7Je2Hpg_MRrfNVeo8TphG1X3kPBqDmw9Q52rKYQkMT3S0lzw9XYTSy_eTfi5Vw_EU4L0FKU6ymvUBHdR2yLr0l2Uoim9YXwSXgVWLIAWUBMtuFFLcfBnCCS2Jkb--YIJkwKBgg7tbeMintMo9mO8OOhsaw9eXL9YIE8WmZLozunwp3TXTDPYwlKrsnQKnf8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_IR7cTUN0nX0dbhzEY6iPxm9ovc9hmm-Ad7_CGKpMz3gkz4JZMdPWfy3CMhWWm0WnL69IPCeec4vCsw7rdaY99r15efeXjy94XW7CZu_bRW1Qn6PPOB7RqnwrWu04vZMZFON_swAl06ro1eLfLs1qYjyk7Je2Hpg_MRrfNVeo8TphG1X3kPBqDmw9Q52rKYQkMT3S0lzw9XYTSy_eTfi5Vw_EU4L0FKU6ymvUBHdR2yLr0l2Uoim9YXwSXgVWLIAWUBMtuFFLcfBnCCS2Jkb--YIJkwKBgg7tbeMintMo9mO8OOhsaw9eXL9YIE8WmZLozunwp3TXTDPYwlKrsnQKnf8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بمناسبت شروع رقابت های جام جهانی؛
بخشی از صحبت‌های شکیرا خواننده مطرح این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22786" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22785">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=mcDxUS9VmcBMI2NCabO29ZJpQ_186VGdgYNHBmb1lXvNkw29iwkLpehov9L-Jjx2HNgsU8_FJVvm6OA3W7Vs52gnxEKXoJnXiZP18lhXzbcYiJcmK1GTS22UXHemVEoZgLkG3VUqWyYETVyjNU3Ss5C0ysL1-E_-YivMCsEfLrj4wnc8nGNSDoZ5Uf73EaCMjRwV9rZBB682vJ292gc0Yy3gUfteOwurAYEaj7uW6FUW-UlFII4KY-LbRjdAA9VEFcJKhz4crqSZMtNwwzHICq0_ZA9_etbA3YhF1NuA_YCY-5bVgFYo7Kgm7a4GY2Ey-IYlJXH_s_BJA9ZqOYOsUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=mcDxUS9VmcBMI2NCabO29ZJpQ_186VGdgYNHBmb1lXvNkw29iwkLpehov9L-Jjx2HNgsU8_FJVvm6OA3W7Vs52gnxEKXoJnXiZP18lhXzbcYiJcmK1GTS22UXHemVEoZgLkG3VUqWyYETVyjNU3Ss5C0ysL1-E_-YivMCsEfLrj4wnc8nGNSDoZ5Uf73EaCMjRwV9rZBB682vJ292gc0Yy3gUfteOwurAYEaj7uW6FUW-UlFII4KY-LbRjdAA9VEFcJKhz4crqSZMtNwwzHICq0_ZA9_etbA3YhF1NuA_YCY-5bVgFYo7Kgm7a4GY2Ey-IYlJXH_s_BJA9ZqOYOsUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
جمله‌ای که تمام راه‌های فرار رو بست؛
فکر کنم‌مهدی‌طارمی هم‌این‌ویدیو رو دیده بود که جوگیر شد و به میلاد محمدی گفت بره مقابل تیم ازبکستان پنالتی بزنه، که البته اون پنالتی‌اش رو خراب کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22785" target="_blank">📅 21:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYH0ZtY0HJVgTjPSjSgbiaBetCzzzcGaTyYSZkR5U8hThMn84Onai4Om9OiMXIDZadxX1wTVShwWswHq2L471Fbe6Bzh_qlQSvHuxC_hZy0x_xJK1LAlFd2QE0y0ZVX9tdt0r5ymADutDNxnSXJa_TY3SxHbXluWuOx2wg4hzkE3jpaitZ6OUZ0dg6XbvY-0x5vR6R---_nPgERTt42Qttk3ZHNSMPe10UiHb4lg-6-QYMqN016iLU5Ea8-Z5UTo8OJyIJFoNIFygUxOPpdMu-IbhK1z7IzFX9XeGz67NzkM5rNlvcAqD6JjnA90nzwOr5Qrte8XLHaVEGp6u_qlCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22784" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22782">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mW-QbAj3midvd-7Bu1M6i7J8hiuN7bcAKOJBvdxOw3I4NIaMTGQwIuEziu7hi8U8jsnJtwMchSHsi2Rs4q_V2B-YdsH04uoTQLzQgYFIZ3Ny9ulHlTAmq2fBCMBw0RvRGmu4iEpIacF10hWDVahVPtQualCfwd5vfISvDl_np9VhznTR7Gxz91GjV0OZno8-RImey0x6tJKkm5Sp0SOwTQo63_r5kUzaPBQgCITS5gO-jhBBzxLBLfe2oiqYN2moF2ugIt7D7y0EKIfgyRs0LswWx27xVZcVUiOxu96p4amOeGeR0HW7hlSayAuZnKC9TllTVCvqlfsGNUU2iZzLeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdR098J30fM8N023ojrBuaTjs5TmL5Q5NevaMyJ9s6L_gHr2c1lkUWBHcOnhz1uiGrUJhvMHtkBT6cUkdya6EAf_A0I0ehdZHIc_pzeO8qOprw7djPIDgPURGRNDpNC4G5tOKg3UH0hC6FYfc7dYy4HQyzs0isGdy-ogQXcYZ68ymHOoD3kaP3eRFXXFxgnombJdfIYpRmr1ycs0Q0gdqfN7FzbySq2JMVCg-De9SaSLSM3fOBndGazhrqqZlLkGzbCcNZTsKbN-2YjHsv1dlyFylgmtN3Nxm5wqwiuCe5Vl2wwHnS0MjdCepIAgn-OoVeplYx2_NjZKG7JAjzxvKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22782" target="_blank">📅 21:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_niwseyiICqU5LkOxLoi_zPA9fSs47Pdb0uc4QW6hCrm--NIzRaOhVycgpXz0ccfMhpAnBA65ReVr0Stz8AKQDdAQmtKIApcLsOxhWhrFNbpBWXCT3eN3_RlzVBO6U7vdIOLkVH4CarRDhIQh28uiGMHdxKdVLYPg25rh73HeOc6IOXy6Hk3RdyAXsTY7ZMAnD_DLlqkIFWW-rpx6BdIWUWv2O2q6rlK8ruJXBmlc1tYZmc07BsK91p0m5ch7bhWJZG8W9WLzSb6jriymlcg-71rZXnYH-2GCnIirgZ6bcevsOXwx9sk-wcmMTIP2jFu0uiCTKAyR0rsP4LrMoYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22781" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7vPkevkOWVFcKxFxGGu48GaJPFGJlCx-aOoKZS4X5QW7Dzl247gH9NjzTRpWOye5-uIeB4f-a0yLVvDfsz2e8Fp7RIam1bk1L6PBAsazrCeJanrtLMpXe4CaWpSXxWS3e00PLhbKRMM9npwo1NoasQeABoi_3-SoPEZmqbykKHSxFDuPjxzmfZRFyuKJIL9JyzLaaOhvH9aOtvf-FfyWwvJiDIfsxsmGLa-as4ru1FxxuV023G58N3CgG1151IhnlXUUGTT6EZdTZmY2PuPiycm7HOZHfXrK2ab_HEXBeY3V20ApqPr6-1AT9USo0CUiv69h_Whkli3BFSF3c51-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ ادرسون سیلوا هافبک برزیلی 26 ساله آتالانتا با عقد قراردادی چهار ساله رسما به منچستر یونایتد پیوست و جانشین کاسمیرو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22780" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚽️
اسپید با انتشار آهنگ جدیدش برای جام جهانی، هیجان بزرگ‌ترین رویداد فوتبالی را با انرژی همیشگی خودش ترکیب کرده. اسپید که سال‌هاست عشق خود به فوتبال را به نمایش گذاشته، حالا با این ترک تلاش کرده بخشی از فضای جام جهانی را برای میلیون‌ ها طرفدارش زنده‌کند. پیج‌رسمی جام جهانی هم اعلام کرده که این اهنگ در آلبوم جام‌جهانی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22779" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyQNXbldVoB_9k0_QMLmpRoG-gSbN72DUkzV0e93SJSBNylCZrkj99GKe8Yw3imiJvSkGy6MjRPDzUEQ60c7h9qwUqcN5_ubdUtqGl1b0iCHwPo791_g_AZ_RiK5X_whC6bqKrodWy5rGYkUK27fVdbKYA67sBo2Pg7iPf8QLJBnAOUZAtls5qKqyTVnS8ycR8VrF6F-1_xYfpkzB7DhKdQWP7tZQKdgMC8LT_OLqyEggpEzZeNECuJuII4BLtynhBpygB5K8CRLR6eq1rXllCPIH1D5aks3XAFOxXqS2JdCMpSsVR0uvfWNOVUkMBtbVcezqMovlJEmSgIF9yUERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqtZ2_7vNjX8vSwN0AhwQaR3Uk2qvnbdXeVw_NMRJWtRDZsJREZeho26i_OULr2lZ2UeXqRSXNvQCW7J-OQXoNo4GJNGpr6yIcQ0OVB5gHRAf7YVE6bXHP9z2LwItqdKQbA7CtXPNglqBuQOrr5TgtLuZdxmFHGzr3Wwjb5QQ_oXUo1hTVVl4Vh64ORT0YVIVEl91nknXdWQc0hpjvdcUbbeEKKjsr1vpJIWx4C7qK3jrQHm9vdceZ5YOhbLswl7gbB358zbcdspuds79oHHnqCmyqSth8RxTLKEhIYsv6AD8b7keb9gAR-zRGOPBCEyMLoL0D6O_Lvhm2EW9PygwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijvAT9h83kE0n7PDmgtda27IZ0Wz-uE5O1cn6hx4XVfL9CRPW-BP-sIgad02-X2WyV7a31P24puh2LhVGrxkuTb9IwTxcJ1cyxfYQnQlu1_HP-Nq4q0CVr4_v-lIlnYnI8LjHW7MhbwOgHz3ZNvm0l3huXYA8s69s4o0kpQHgl751Kx5n_jAdn5qo-gsVZ_n9Mcr7z-FU4KQAj-SpLTfH066DSw1fVp1FRaqDJMwdPgcNDbMoVkjRKvRP790GiIgA4tvsovF5UKsf0cYbL9TiRtl7XLLMlKnreZDuhqMh670El4N0Fom1ZwStXzp9juitYWEtMLHUOFF9OwOpqywXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGZSrzvJB9M2_OJEmSpugfRwCscJdExuXH-TRWAjsvs4F_gV6oehJN9bjOWwQX4Egj4xaJtrCZ8xnxmdRpkKd9N1GoEC1NlGd-w16Ph9Dasq-wa6fWJnKx_6CnLrpKz4JNpRdt3kEpEUGPYnoe5Z1cgVL8CRKsZitttAXf-HQCIJUxFr9cHkqf7oQE_swfJpDwCSPXWudymKY61f6AiPMicgbpkoF7Qk1xxQitizHSFeXXOBzerZaX5aozEn5F8WNup0haLvS-6QwKEtUlV6HBVkt946x4STnGt-0UASeb1LAsPO1cZdTK2xIlH0r-iFsUyh7J4OPKktTyqspOF0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa_mQDtEyq9UR28A5UoLYRnCsuzYeNVUgJw-gdcGCUjjWZo1TccMZZRabSa2cYEwAISwX6Q7Of4ZyzO1ujJUQPFMNWcBAuBCBCcuBHry19LKwCs7pX2tGhXcK2qjzGNcr85WHoVOIoIaRDmTnQIC1OFo5-NyQF0hm34UfYxfwWfZj8pwb3tkV89DqqNtfxmErXEmOY9mCgx_7h8jmoVzsESECMbz_55AzJLnGsSKDhaGGQ5LpA9mNL8nm114BzeSAOnibbHu4jk8VKNeP_5QI2jq912Li3bkxNVtDtJdmtX9bIugRVq3xWGTB4T1LInlf77mCyEWc6P_jw5udTZaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c00997812.mp4?token=EfT3oUmzDHZu2CbIY7rMhH6teEfjZ5cqjmfYEhUUi97Vh0IMbZP4aaWMcYl0fBap0z3LOlUEb-GGGp96_JSM_I9x7i8TPhs3D9DzJNHe8PQ5Q9oCyJmfer1ZQdnxZZls8NvZ-du7wkSpOmJjH5lopKBj1UdJL-JMZXeSWSw-a_MVy7io8yb8rArkzO_A5rvCjIUI693V3inXUhTV1oV6qoQE4gfLG8hbS1FobunJgKH_Yo3n9zmfL6TEXjQcIaCwQ8Pb2PAPJRO_biYGcBzFLDrpItcpnCl8XjAuO1v3r7e8PryQq9T9gNwrACK-hL2gMVEdVB7rDUfHictCGsg2X3_EcPwae2UTM0ZT_mR2VayY4ILPGMdCaANDkDrD8DI_jRYmaaVaenfovdVpVoXKPDhWj25xLqMRZ1bjUZah3EGaXW35rgtIe8ybv4OL7Xi-731cfVKuib1_U1vSnyBnAe2U0lN-pyH4-z-6XuSg_o7rsDVEhbf0lhRrSbFQdzTLNi3HbF1hCpUpGsFki30ruJyAVw7eFxE7dgsjwMLB_Zjwxzi0TMPYYAi9uaKxbytqKqW8GH-E0lgRpV1BB0j4cJ8C-NXQmBBWTJ15507wEk2T3P5jFGCnEV8-rFcJog6kp_OiED6O7DcSTzxyFamd1a2KEjoXOgWFzlrjKcGzatA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c00997812.mp4?token=EfT3oUmzDHZu2CbIY7rMhH6teEfjZ5cqjmfYEhUUi97Vh0IMbZP4aaWMcYl0fBap0z3LOlUEb-GGGp96_JSM_I9x7i8TPhs3D9DzJNHe8PQ5Q9oCyJmfer1ZQdnxZZls8NvZ-du7wkSpOmJjH5lopKBj1UdJL-JMZXeSWSw-a_MVy7io8yb8rArkzO_A5rvCjIUI693V3inXUhTV1oV6qoQE4gfLG8hbS1FobunJgKH_Yo3n9zmfL6TEXjQcIaCwQ8Pb2PAPJRO_biYGcBzFLDrpItcpnCl8XjAuO1v3r7e8PryQq9T9gNwrACK-hL2gMVEdVB7rDUfHictCGsg2X3_EcPwae2UTM0ZT_mR2VayY4ILPGMdCaANDkDrD8DI_jRYmaaVaenfovdVpVoXKPDhWj25xLqMRZ1bjUZah3EGaXW35rgtIe8ybv4OL7Xi-731cfVKuib1_U1vSnyBnAe2U0lN-pyH4-z-6XuSg_o7rsDVEhbf0lhRrSbFQdzTLNi3HbF1hCpUpGsFki30ruJyAVw7eFxE7dgsjwMLB_Zjwxzi0TMPYYAi9uaKxbytqKqW8GH-E0lgRpV1BB0j4cJ8C-NXQmBBWTJ15507wEk2T3P5jFGCnEV8-rFcJog6kp_OiED6O7DcSTzxyFamd1a2KEjoXOgWFzlrjKcGzatA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ترکیه پس از ۲۴ سال بار دیگر به جام جهانی باز می‌گردد؛ تیمی‌که با تکیه بر نسل جدیدی از بازیکنان مستعد، از جمله نان ییلدیز یووه و آردا گولر، هافبک رئال مادرید و با خاطره شیرین صعود به نیمه‌نهایی جام جهانی ۲۰۰۲، وارد این رقابت‌ها می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm7536O2TQ_8OufupAGrc7I95gMpmRPLA6YXx36K_HwKgXqp_MBOQ3jWSjPiTfyCMhZLwvfxk5cAM-8R4qvuwvtltLSI-Db30snOBSdb_83utCAYXKRXYdL87pOH6swdqkceMiT2sJvuj1IrfQHWDTs7KD4D_hOwH6DACsetVAnJViHXrsjZl9ZfTvAz82EHMAm5rAxHxVZeLthSetRy06JtOnJyKbZ-d27sJv-3yPV4YjtkXVYGglKyEqkDustbxKsyKlSmkt6fMuHI9Kw-NXUXDU-DWBZ728kPZ9gt8HcJoZKIkZjyLIFfpiVDg1R8WFVdDbuNttTXLMXA5KtGUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=a4syn5-wGYHTMBI81Z2FWQErCVIaDhoCNoPmnK3zzJGhs_O3KAD9JPW7y85gG_4vieJ3T96D_h1Ob6tYRWCGqNLxlzCJPtKbewNGTUgMJisnLf66TtQxEIf3AkssOKtIqnZ9JIMJUVZbJd78XiUPMHviRqx0wdWaIK0f3aYh6GrlpQcLg45xiayld56B3DY0ImWyIxVlZtW-soWvYA2tv1lP-VPpa0eSVMibW2qSdyF2hOwD-fOWJ860C6MrohmOlmOlABIN9ttgMTnbM0F2FiicJGz2EW1VaQhetaDMhmBhnLXPqWI_N1nWygUD-q8ddp47iuyXoEyO2YlCFEJLxpiPYmFWa0Itq_-nRl4BK0FQ_wIAfkfNwER0tXLAyO6SdukAQUJJ6A_exWDUvqm8GidhlSabWZxUJsNxBfMin9v8Fpqn1jzXn5v9fpYb16pOq730XmjHQG6D5xgSDFaVvoo5oqmrH_DTDH5KZTrC5XZgu6sDaG9q1zGgn9yHf4NuOW8I0yezmyuM6did0Ye4HNwpB9TQKN-kEj6BW_AGlZmZ6EdeugxVl4bx1sDjfZ0XITBh0bmSMgSA0d1MoLiLxhslorfnsuOBXAm34ZdGkLO2eJ86For27sKD12UjW99SIZnUa2y8YJshEBNNxxsFrqp7hMR6BU8J8seNCOHVILg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=a4syn5-wGYHTMBI81Z2FWQErCVIaDhoCNoPmnK3zzJGhs_O3KAD9JPW7y85gG_4vieJ3T96D_h1Ob6tYRWCGqNLxlzCJPtKbewNGTUgMJisnLf66TtQxEIf3AkssOKtIqnZ9JIMJUVZbJd78XiUPMHviRqx0wdWaIK0f3aYh6GrlpQcLg45xiayld56B3DY0ImWyIxVlZtW-soWvYA2tv1lP-VPpa0eSVMibW2qSdyF2hOwD-fOWJ860C6MrohmOlmOlABIN9ttgMTnbM0F2FiicJGz2EW1VaQhetaDMhmBhnLXPqWI_N1nWygUD-q8ddp47iuyXoEyO2YlCFEJLxpiPYmFWa0Itq_-nRl4BK0FQ_wIAfkfNwER0tXLAyO6SdukAQUJJ6A_exWDUvqm8GidhlSabWZxUJsNxBfMin9v8Fpqn1jzXn5v9fpYb16pOq730XmjHQG6D5xgSDFaVvoo5oqmrH_DTDH5KZTrC5XZgu6sDaG9q1zGgn9yHf4NuOW8I0yezmyuM6did0Ye4HNwpB9TQKN-kEj6BW_AGlZmZ6EdeugxVl4bx1sDjfZ0XITBh0bmSMgSA0d1MoLiLxhslorfnsuOBXAm34ZdGkLO2eJ86For27sKD12UjW99SIZnUa2y8YJshEBNNxxsFrqp7hMR6BU8J8seNCOHVILg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebkH_67WMU20KxQli4IR3hNt1H-aoYqfCsvuDgXS6_OTfgCCNQ_j1CG53GCim2uuZ9BMbPLeQNqOyvDsEREfG3Eh1PRSz54ky0AZI987nlk_zLiDPj2uXRFOGFTE2spfZKKdBg32ue5xFcqf3ASqEytr3jAFJEBI_LHJ_0m1J7GSGuJqjNjCX8kB1O1LNcZgwopftIdFJWIX2gCMJx5930G2koTeNLTgh28P16gEwVz_wFX-ruKj-1IZex_S_3jPXjsEZ86V6ZTkX1mDE9h_Ump5Y4PyhrpeAQaQ60rcdOLv9JpGld8SDxMmMOm1ELNmXrPzLk_H6VY1hAPlsG8VLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNp-OnQWaXXfNxhKcK0kSSUhfJVrG7qG71BrwUWCSd7z70v0u2QKPKyDRGCaBFsufHXjT_cIfPYw5DdgN7PXX4-fEpDT81cZO5iBQNdbbmHQ-4JRZt38oUiSOzcZ0WMrvbSJ5w4S3ySWcgYzUidjUz3s-vspRne4IMb_mzvrAuqIj1zgmRp-YuIk7rCcWZw1vkOfsShOiVy_0mIjhrbys-3NC1vnTVepa2tt388W1swBQMnH1SkabE_HceFRaWuLnc7ov-QtKMvO7_mwi5QcBCBfa5djGTaqYVqF5XzwKomWlyrfvNr9Iw9uLm7CSR8tFvke6L_-jr7RBUE81-VuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J34c4GlsNC2WSjAjtClZyNW4YndFGSObQdZ-eS572hJcKtBNuNbUbJaHXiuMPzpF-HCIv8QWJayB8BfMJay1v6p51VC8zaTfzvqDigALQACraJMDZ-KC1Ci3EBm9FNNORv1vEaDxiA2q-lrWnMCCDV--i-VpYnW4VGaEqp9Z2a98789wmIGwsLt3LVzotN2Q9dnLVq1Gc9mfpzU0osvomXRULlIrD0nOpNMB9L3YejdQv-4GaWClTR8Nebi-B1CsylEQifqHlhjil1C3W-Pe5ss58gfk2cVyudpH3cQV_7LpbETmYwh2rPeQpAN6xV-GRr6GsJ3h9-3Mx0-_G1pbhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKhqjYS70eWrQpkNmN2yYqAUPuHmcVlrEP0rQwMnU6vcVbdD7gEfRUOLgtg346_9BK12V35NI5bHM1BWAlUit9Mmk3xHTaz6eHe7NqTG-jkO1TMZJryw9oJcGatiqOOTAxDZzRbIfrCRJwjPD6f08jvLmfRC8x8eoCtd_8bBzTD8mG-Da3mXH7oQkOFo48R0CkIUpq8amV8H2AmLsMYSL7zkRmY2kecfeoJTl-CqtMYn8F9hAxwaIpCGdKVj0fXw21vlMNB61UDMvBOE1m7a9nR7Zsr46o3fujKzEVLPCMnNySk0JUTh1eDrfMiCPFZi8tBHmlQPro1xUWl6xMBiOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gECzuH0wDVTWgCVt0cnSJQ1ow3OwRC3SBtJl3OHBTZiSm15TOSDZ0Mt1C6Rh2Jqc_nQJPk3DH__0-k12R-kdqJ4r_wDkJYTRHvlVRpE8Tn2QKDtmBuUpkRkclvdvGJ_AjmtpZDvrMDXC2_CcK8NvprQNV1oY8u97EFe63_0sS7mTqtDiV8WV2g9qjsZ4PUqHOq1asDIXxh60TdUbEM6msk2JMoWpZa7Wiu5r6lNw7mHBKbvcEsR9SzOGGNVwKntsvpTO1FTEyFJca1LzhTDyJDrtXmegSr9hhERiEF4PBvLanq7kJrHnNrK-Be9jjVn9vOQp24WtBNs1nFFRusN1bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLiSMqo7mABEaAx81cfvpKoEj7vL_ByArNB8fi0rz5H_7DxStL4RUGUsRN-vbCRYs2mQiduBCBmWbHuEWAAE7GcY-78ScaDCjhNAmkao5uC6YCxEamhgnQg9BkkjgpknBP8hKFQ3nzdEuZnaNHNRe1B7phMr5OHhDnIgLhR3NwqhYT_53OCJ-wxVeNen5FKnmuELqJH5pAcxcPRgYW-60_yy5iVHxWVVPUIwpPpPhjSAT214w4lbSPDLOwpg0KV97ksPHgINjKl6OwZmvklEVg7ilpQNUfS75Lhn4VcsqXCqewMtEEVKLbF5UvPG4iao9QFCLIbhDI6e5K__ULVLSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMAswW9K2atDcMnu9WWqAKa0i3aLYjZnz87Wl4kzsrvvfMczlghZaQrR3UsYzcIoMvmcbKvI9j2MvDRGl-sjsLldsiOFcCM43xmAR2GJ9ZYl28PcX3Si-3qNEip_RhmumBJTm7WMgQ5fJEXWe1LqTrAh0XEdfokYD4l-IdPXSsaUGPybmbpgaoIse6XIhf3h74dFdl6SRyA2XW_S18MBYlhPeveb2NsiE-jEYq8JUfeZvCBv4j4LFGwuJOVWKtxw-keXRWrR4r-IJTUL4X0zKeG2LdLAODECzuycpxvBN8AAIIQOX_1NGLaQ_Myhck1tCtGav_1EJmtyoyPxhtEzbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWv-HfR6wXhlQG5BQJFWSVKrR0yKna3dSlmb9k8Z07H7ZJk4QWO7S1AfHiA2LAjVd3IKkJgEtLQZQExOQs1aQJrtpmGUQeNLgu0mwXDwYIY7kElIuTlj7fzuB97d6iuL57l1Ksr-nhL-oLCEU39wj4WlCQRvX9cnPhH1mCRfMqX64yFfO6VOcdX7C_5jEBgNBcniR9BWdBVSm4RgS0PGuzLYM3LfzOEKVthOQ6jQlfaZNDIg9m1fQe1_DEQHL7-Ck663DhJGv3ZocsZGHfECCITB8w4BtcfQsaBXgaxQkBcXX6nJqf-zZRyMMvCfcTq1jy9hWfBnrrZTippNAK961g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBJUf2N1cjMuWjI79Dw4ZkqLIRlngz1lfpIgHvA9eYgpvHiIHUnvQ9B-xg_aflNYwfi8u7gOHzvK72gf4GlXVKy13zUn6-LdvsYRn3aTCM1T76ATo2nSev0qoMiU2FS1mE64JXOe-RTcxm5ASp0bpeLnxI3YZOVgaUUQpEmaoVTymgH0ltx6vw9htm4mdK3TiVYe2nFZBfief_WiBL73Jz6zAFvs2aBVrMjr5hun2Jl5gZ4JbMd4I8kq-xEwm9BoA3-uCyUYvSpGXqpYkANu6aYhO_1xq3lCCyRGpJ1EFFyZUd-CVtjDEC3VKdwH0edJe0opML0sQjy3RMBPgy4A9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRI_JdHbA775WZwbnbJH31ae_q7gAI0ww4P3zLyb1hFC9hUFjQJz3IVHhuijgdce855tU_wfrvDl6GObgYQ3hVGwXy0xbaSJFFesvtjLCIhJDlUUzN6scQKqpX-7Y8J-kRLEfSMzNJsmi1LROh2mBeahbR4eJCz61eQRpxRZm6G-14hj7nEVOIPWBJqd5BKNPO5v7u5Hc57taUF1TZjfnyQRxLoyGFhM3uVVKLvnKYTQu7Q9_34bR21C_7wc8m1jG0vMu5pU_uis3d0U0UyA-D9hiFzoA9BcuNAnV5HZUbm_IRAxzsFV6MNCwzuhM5yexFjaWqTaZTJlDrbPFRLC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=VhVNuAhP029LIZpYmZfFz4ybsvJr_Mg25HmFDD9peCysqOm2NLCssu8RVan5s8tgK9xOgGnWnYwKctc8PTXO3oWsH4QbYgdzzQTqh1awgKKq3Tl4G6Q66ZVj65g-daeZHQKxroLU8CA37DZDav2sECE4KrBG6VWBh4yt80tTOSGeOw5lOC1QIcPcSoDR1cmF5aOPUaeq0RCAbhV-_Ahb5HGzVLoXLpNwufrFPnIww-ijsG0pSsWVwnFEfb8jhuZez1-0aKzY0ppB6d-bHTVvCNZoibe4sTppgPYlNXXzLC-IEZ2h55-Ci1ZLzlgU3lHW9v6TXimQgvtdkcLWFYitOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=VhVNuAhP029LIZpYmZfFz4ybsvJr_Mg25HmFDD9peCysqOm2NLCssu8RVan5s8tgK9xOgGnWnYwKctc8PTXO3oWsH4QbYgdzzQTqh1awgKKq3Tl4G6Q66ZVj65g-daeZHQKxroLU8CA37DZDav2sECE4KrBG6VWBh4yt80tTOSGeOw5lOC1QIcPcSoDR1cmF5aOPUaeq0RCAbhV-_Ahb5HGzVLoXLpNwufrFPnIww-ijsG0pSsWVwnFEfb8jhuZez1-0aKzY0ppB6d-bHTVvCNZoibe4sTppgPYlNXXzLC-IEZ2h55-Ci1ZLzlgU3lHW9v6TXimQgvtdkcLWFYitOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBj9iQvC_ZUNJLNSvNpQOpzoZborJmhmvp2QMAMX7zwM_aWyaugCa-X4YVyJB6YBzPbkFvMQrh5sDN1Lnm-VS-x7vjImgEXBF8E38Q2sV2x68sFR_kdLxwNoggcRuUpmOYNnuAbVl3rMzqmwdIXgA0AUnsZp5di4ZUS37AiASEp_KWgPRP8SqTx7lXSrk8j-_TCDyAQJf6zjFwC6zbdPmwhd9kFUzVPs7QtjNoUHcN1Zw_cPG0S6ZGfq4TAMnsiZEHv89yiqo_VaF1ajwTNILQfcyReI1RsLhAsIZ7YI0O35YZ0CHQnmHlGhxnsd2rtao1Q52QkSMd1F0wYQTcsr8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2nDIGIJ2uEsXTl8yhv0rDTcRBFTDJJ5KoByoWp65dMguSEw-9RKnn6wwQfqT3pp-Eo719y97OkIWG6c5zRLAY9u996E91ru1-6pxP2e3n1JCZbrnPMCvjhcwxWY9DetKcnwWPzV6FwGUK-ZFjUGY0kBmIaXwz4pgk77JNt_RXDvABjvVzdb_tdAOn66zYe7qpeHW8NezVbnRtnTyCjFMTgx1Q12RNT8uihhp5i6vLTrkmmHZD1K9dPXdvQiOI7vMzOpUoZFUkWg4WQqRyxv0JwMTWeHmEcG7HD3ltupZMuGr-3yUJpIY2jXz5z24YPZUMvgX7y9VxSjnPMsSWwFCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3GKJbcaaGx5GDLtm1JWbguaTUXFVMjmrTnpbpCnt7jj6MfNyHWBVTfv5PKyBP2XVlCEcq2dSD6xiBHX22JKpspUCUtGP3QrdT4WoJwNgAqa0twkjCJAp5_olBNFq5HAbU4HkV5VIZojcQrroH_8ap1mJN00NiYWzUQNGdPEZsfxloOywugeF7HbtlOHAfhcqUK53PYqiT6KCqKIHMUHNN1saJlPME2BjOqLlh2-OGeLZcl4HPBVAZgZWdZ8-c6pLoNWb40Gj1NHG952L5a6YV2Y39GIszC9qFv10K2WP-CJqC0-PahKkMSx2HX-4-_bOejyvAriDTTJZhSW2G6Icw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=bQMfrc0ZygN1eWdQetJ7oXfszNtiiy3HQcvJOz8azDTlQhh9fo1KF-WGZIHdq7sRRhCEULPjdLQTB-SM_2x1i4fprXCJed1ge7hpe0kPZRIQJ88oetgnvuCseckY3kmpZgjDBqp_mjRoE4uNgh43n_DYxqq4Dd5PJ5un7E-GPl9xoqyzvmJIoQhE-IZeJx-hcs8lBe_5PUgcopxswJWly7iB4J523Xq8vVPQsXZ8jhW_U7iE5neyZq0pyHGp7xNAmf1qTaCjGScQ_w0CPbYsSqbp1RaXbRN0Ar2IxM7CRMaAXKwTxtx9XIpbcR3zpZOAS1oLOqxnU9-4RpcXzl3Dwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=bQMfrc0ZygN1eWdQetJ7oXfszNtiiy3HQcvJOz8azDTlQhh9fo1KF-WGZIHdq7sRRhCEULPjdLQTB-SM_2x1i4fprXCJed1ge7hpe0kPZRIQJ88oetgnvuCseckY3kmpZgjDBqp_mjRoE4uNgh43n_DYxqq4Dd5PJ5un7E-GPl9xoqyzvmJIoQhE-IZeJx-hcs8lBe_5PUgcopxswJWly7iB4J523Xq8vVPQsXZ8jhW_U7iE5neyZq0pyHGp7xNAmf1qTaCjGScQ_w0CPbYsSqbp1RaXbRN0Ar2IxM7CRMaAXKwTxtx9XIpbcR3zpZOAS1oLOqxnU9-4RpcXzl3Dwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQpWwK8CeYyjSY3UA-FEb2xigs-1dyrYfYjAmIxypnmu8-PRD09gQOffTMA9GvNbxvnjD-r8u7gNdWw-aKkCcsAtnMxodBiVAiY5wZ0yBe7twLUGmsva9O5YKw19Z0m265qtbePMCKLcmCDQKAXTd97jmhNuMAu2kyZSYMO7i0mHySYlwT73zs7IlzlgdSpCPDZ1a0pX6IC-1LkhHO4vqsgb74VZrNhfZvzzRj-uulf-ad_yG2jLr-_aEyoNQe7VPMgJ_xMeTPTPeFdFFKLdIh9Shp1SghkBrsfegk8dkSUTqrwImaRRAYpUKgHVJ_nyTFXkZ6vPlgin2aD_ALfIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kudUSALQa1Yrv6Cc7bV6f0mZVcS1XBSyhjdgDSGMtpCVCxsMYYkJAsY8pgZ5wVKHJmPN7J6wk4GauLIPnj7yBh7Ij75vNm95MEKHo_R9NoPbC-GkGHIgOIh2_lF6BHeHDURUCb7s7MHdYvSRTFwRhgm6EOeXLI9dtzndT5Tj2AqU8dwVZrvvssWclhZHA8gzbooDc81mM_C4IeDvaaXqSBtHnDpxaMqVh4_gAwOKq7itah_iaFcbsyuQ7ivLjDGP0nhuVRg1pSuUeQGGUnDy2IUDQhccDT0QJyfYq5f5YbJlszIgKoAK4uSR73DoeqUa6yvBtqRAMRav8--f-MyJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q67601jjDUWeRCjQga5kEsuahu_IGd8NI6cusIHm7vIDWC_iqxT7X9OaVCaubI-xmlf5p1xAyQlF0CNUxKLhxS9MZjcnaef3KBEx31MFPX09KxtFS6N5-y-CwVTmUFKJ-o8gbsorrH-BW20aONbVe1gm95mknY5i52b_xlKOpWh4-qCSlJjmepcs42P23KV75YclNMJ6dsc_m2VQFKQ4I3HM92i8bAhTaM5EaPRxozSdMkiy--0e4wBim6tE4m2caNgwe3I2ryE7fZcdLV9seZ_hAJea0nRLFEGUI1TF8cXhBsQ7AdWC3ZPwoyc4e6UdFhCZT-ca7B8aTHGyg3QjaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoYOJa2QsAxOBECeaaPBXBlserE2NM7UYLakAq_Emk5X3ui9gMRkw0-Luv2uzF8vgUeyiVsjPXjDsHqB0p8xp8paxkjYsEhqJatnlhgQd89cXoTgVRrwQb_iHZThMJ6iXOebwusW8Vnev2RsABn59qC0w06uQV-0NZFNSAJ3lmSQGLY6SDou9h9uzdf27Ozb6Agkp0O32dew_qiIpVrFO9E85ar151s7q0lY7HRfAC_LVsGOr8WajgJhKPNPTY-oSupq_zuXfRABRHPkfNCKoygem5sIx27TYbmN1A8wnJWgRtUAIrjhZtrrciKZOyNLVe1cmrrDtyB7zQ6UwtTgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItJKUm93rQC8GM-B1zllIQnfQYTgmTrDNBXNarNCHeB0Yh1loTMWSZyLdEYfApSGXAqTALQ4L2XQ5QkM0EPzqjpEZe9a9GwadCIpsfMCzccAXQdu6jo4S9v738r1Lwj65b0m9ljr5cWAuEYBSCbU7ib5DU96_YsiqTQWGFAruW8A6xyMli4f8oqgfEbo-vnV7GdVQx-YUfrsLIV_Cjhsaz1uXLfqOKENwdK5M4nCD_OQHly3-92P1C6oDWNeTnrvFrUlvaHx_JgcsN0sTlQvQZIINm1J_XpPUlWjU6eDFIevYLtXYoqENwOj0KM_Pj7-Xsn6IYcwl57RlAQ4_SwtCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCpfB3J35LUcsB4yrCp8KqzXI-orkBGtXxGwPoA_-T_gkCS7xAmRJoaLNcmUymbrrtWwoIhjZarSV-HfOPj_iCpG8fTuzM3QTxyin7e9nVOGPE1WqtBdJWvMmpYc1sQgGThulqrt_rMo0hqQ9gVXb3nPAvmwS3Nw_z18D8bSD8DpZaDhjwrSPIjYUli52AnDT2iQRon9UHtKgKfat5X9LXGKspvm2u4cafyyDFalx4HGAgpqYENfj7atGPCYNxoLC_JVNHKkzW-hY-KqcfbPnK8r5Lurh6fcdP8q7xgGzzqHNznjthJs-ZFwc5yTZd-JMS8bGJJjYNuTNmLZXzD8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTfAC7UXCA4a8TrWY9Zzfuu0XPHSJggq-p3Y-aQLr5U-MjrfazRmsQrkjHVdr8kSps4t9AgJtXAKldh43MYvABjKqCZ8pdlLbZAPAbx0Zc6d18_ChDwO0nP8cBVHZP6lDw9GNKzDYo0I7wuJSsmBOm_FCdU9ntqlNySvbTZOQs6RjHjiF2TW2NZEyQpGCS68-RPgtTfnluyteTaHHbUdYWgEJFDOT20x5TkHPpICzsMwJ_ab4rx9DlK3k5RR2q4_zTv9JkZ3Hp2ijFIz5twV5Z9QeZH_ZLIwbmBp7DzB32gOlwfJdn8EZYzPsPlf-kjghi3jdMGSuSPMMH1Krn426Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=tC5PDeXaoOX06WNXRzsIUgMbnLbnSxRr0vO08qbebmC-ZCZx22BViLy2g99xehtYWvdEB7bPSj4Je29xFXzNqET7Yx3h5zfMYo2XtrDgRjEpnhoUxVMLhVz3goCVKatyapajAOjOB8uDhdJjqBOaGfwXOBQmufPUujyWdJrZr5F99JkWiKdeOBNmEBa7OBagmaNh-MwoYXADxwRxvHkYTnAHWvPtla7Lb_sc-sF1XnEnhtAKJ83vKt87O6E4SvX_PBlwZL5tj60tmrB2OvCL5LOBmn8JAUyEv5TJKjGPFJtpjCGOcDMOVqCEpyWwm-3p-K-xTOrzIGrr4Npx-0NtmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=tC5PDeXaoOX06WNXRzsIUgMbnLbnSxRr0vO08qbebmC-ZCZx22BViLy2g99xehtYWvdEB7bPSj4Je29xFXzNqET7Yx3h5zfMYo2XtrDgRjEpnhoUxVMLhVz3goCVKatyapajAOjOB8uDhdJjqBOaGfwXOBQmufPUujyWdJrZr5F99JkWiKdeOBNmEBa7OBagmaNh-MwoYXADxwRxvHkYTnAHWvPtla7Lb_sc-sF1XnEnhtAKJ83vKt87O6E4SvX_PBlwZL5tj60tmrB2OvCL5LOBmn8JAUyEv5TJKjGPFJtpjCGOcDMOVqCEpyWwm-3p-K-xTOrzIGrr4Npx-0NtmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YunAB92bwNF-2Hm-zkJj2jhhnOmno-ttbtrBQ7wSuBh3PV7WVFKYL7RFkgBCw_hxdK68ELQi_Prs7F7mVVuh2lPJ34gO8cgHXUirl4FF9-9LhFdnIRq9v_62isijOKFws_4t0PCUjye89pVICdanvfheieXWP7QHhOdCPJ3Yv8gVValg6Qwx1a_5aeezUhN80ur2scGanwSrN6vQq7w0iQzW4vP7MxpnglK63magc9KnLg2Ls2F5XNoiMnOsKY_VFoWJ7IViESn6pbFbneDP1_OVdNhybxmBhaH3Q0S8S-9Fz3q9O_P-8c7OvJLqI-8qItTPumjuRI43vs2LRML92w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlpxT8F_TyFwo-6m_lIFzJEAlrsFJrtwjGir2j2fU2KWu0GHzYd2SLCw_rT4_sL6a0KLL5kGpilj0IR50GTFt7TX5hLhTXz4d0COhohruJvHgPkH6yL0omVkFXAb7VpJAcVO78S_OOHEMa--bvw5zQyPvYlMkRFiqglVby9odI3PN3QV2FonM1INmCX5567ak5Ld0IMnPIbfvKKJeETAdWvd3idaH3tsAwUVXgWnh1kMCQjlMNwnXyMHvlzrsMe_5Lr64AMfzPgT0cGx-TFI-87B2vU2AwMxehJOYqxDNxsrE-POdPT7GmxiCayNUMpJCgnOOH_kMRzOMcHxKi6gpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5H2ksIV3TUXtIazEEZyx-RdgDHUJd9JbeccpAyLVpI-Bq6E-DQnp3sSOOvHUcVSEEbt22zviYDRSCwTmPyuv1y9Eoujl9_MpBQ1JmVlHOq7ZAKSs3KBl_bEaqgxJsANeUh4MEo1F1H091120rhxuOywntbeq3wFLhN-uu7970I1phA4D9rhjBbI0R9lRoGQqverPRhoe-JST12MZsLphri9l5cvmdU6ApkxIva3187JaTvgPw8Yv5HI9uz_bXC-fNESEDc3E0zL8MKQiRowqjl87ii7t55rhOy8DY70AE8uatEfzZiXp9BkpOEFn1VRV7QEEFkoSRbgS-WPJEx_8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUUtoqbQs3jxd18mpgjWUVf-pmVDsDs2-NYV_KW6shvLhh6axx8qyLebAOWoxSYXo0AFiVFqvJpEeqFMQecDFn7EFMXfyrAExedHbQHeguFvUHLqlQLwSl0fvRJLUD097v9i5D-hOr8ancvL-ZLf3r5xSTMqE7Bn8lmjg3qlFmHrrW6j7gr2HN0Z7BlN9bIYXDc0V4ryOiyAH4Mwf2NIr89fIg7D9xR595Z-uVXCBg2P1z6UoLnrfF9d1KSVo_DIxxLOIPYN0b6CAVnQ3QNnQJOQzVw9ShOq6i0V_hgZxwGz6ZqkacuJCSKI84DKW_Pbk6NMwE5JqfNoDcBVSe1a4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvZcsbP8D3Fw5o-Y14JgFTaDCT0MoZCcTOypb2S7EfcUHfGrcva3fJU-xS7g3QRg5dpWsEiEk2Cwx5VQU7DWUmVsu0-__SFwYIvniogr8dfVErDpMAFhcaoio5Wr0ocsdQiLeQZjKaCnq8XgTySu9Obyxej7-aOkYq7Nk3EXUzos5E1fgEMHQMiGjemHO7QT4xbvCDhEHkKsHn0tLbgSod6-KWsbsyBeLkqPeng8Ih2fZmLSf4sEc6WLc-q_XfejY3FA3bxc9vnkT_TpYDJoi3eLhHF6WmgtIYHLuSpGmYq7uCaiRbo_hT0xHp6jaGAsGHan0GI-STdZ9HbM1oqVAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_xUaVK9LApuVoiW7OmyoVfgzqbKaev4itB1HEVU2BgN0kPnD4LoPLf7wGBSQhc3NX1OUoO4oOQWS28KrC3FH0h82Z84xPtDFMhWrP7cHWx7ZwObPaw1cU65XokONQ3T8fbRBPniTZBYMofloHMLhZ0tHe8dixU5VdhUvMXTfjC4GBLrznrc5Cs5mnBMpDeogpnIB2IFA_zNzJgLpgC3s7--kxr6HRX20dV3iedvf_VYqb5u6ZHxj7nLgFtacFBXkPdRtmaJc5G4AHZZTesIjFFYhCG_48p5kBbaUm4zyKPfK0Mivd-EU3EgGAF39hDyxniVgAIvR4jyxXL9qJLnqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1314be179f.mp4?token=WEdulESEd_ZNCk7BnQCbiQk3lOtsDECsw_0h_-KDw8b3LFBEO7fb0q8Xt6g4d2qGOVPg9nIqK9c1_f_rdnpx95pLNlMugupJILkTxAorUsMw9_nvwrOwRthNecmXkJLgaZNj4S6cgfRjCSSxJsyRcNssJDuLbq37rFvXVNBfRaxZOdHFE-ydnDt8rox1qAs8mLbdVz2oAZxSO-RuF-GnqXhebXO7-YhGBF65r72Sr79Jv9VGdxwzkWAZJT54PqX1dCPN_XAUdO23sJ2mX30bS1HkTgyDpiGsOoVVsiNwCouVvlYOPyeVLXEKFBhxXZENB2re9i_utH-WT2r7f9vmbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1314be179f.mp4?token=WEdulESEd_ZNCk7BnQCbiQk3lOtsDECsw_0h_-KDw8b3LFBEO7fb0q8Xt6g4d2qGOVPg9nIqK9c1_f_rdnpx95pLNlMugupJILkTxAorUsMw9_nvwrOwRthNecmXkJLgaZNj4S6cgfRjCSSxJsyRcNssJDuLbq37rFvXVNBfRaxZOdHFE-ydnDt8rox1qAs8mLbdVz2oAZxSO-RuF-GnqXhebXO7-YhGBF65r72Sr79Jv9VGdxwzkWAZJT54PqX1dCPN_XAUdO23sJ2mX30bS1HkTgyDpiGsOoVVsiNwCouVvlYOPyeVLXEKFBhxXZENB2re9i_utH-WT2r7f9vmbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اسطوره‌آبی‌ها50ساله‌شد
؛فرهادمجیدی ستاره و سرمربی سابق‌استقلال وارد دهه 50 زندگی‌اش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=vYhFo3hHxTgAsZikNU9fwNPy-xeH_Nho-sydCh7UhQjysqE79XTXVlT0MHauE6jwmqM91AGlpet5RmMpgzvdNriht4wsUhXCIqC2gpcjuMgzHDBOT_nsEWJslpZlC9aUVp6K3r46NRd_zWQcjm0Y-JLjZDI0-44chVexTtSwT3ZRvNE2H44pVNyGe0YbamYUyIQ_rErrcY22iGNgzYv-7zLDpQ8GpbDtNokx1ptSwgKNMbjbK2gx1HvuAz480Xp6e__c4pKJaPDffOfiIb7xwN8Jx8_0jX4PJqJEZa7dG-Vgd-mS_pVlT5hLOx__cHXG7-QMuTIEsGCrDEZrj9hxfIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=vYhFo3hHxTgAsZikNU9fwNPy-xeH_Nho-sydCh7UhQjysqE79XTXVlT0MHauE6jwmqM91AGlpet5RmMpgzvdNriht4wsUhXCIqC2gpcjuMgzHDBOT_nsEWJslpZlC9aUVp6K3r46NRd_zWQcjm0Y-JLjZDI0-44chVexTtSwT3ZRvNE2H44pVNyGe0YbamYUyIQ_rErrcY22iGNgzYv-7zLDpQ8GpbDtNokx1ptSwgKNMbjbK2gx1HvuAz480Xp6e__c4pKJaPDffOfiIb7xwN8Jx8_0jX4PJqJEZa7dG-Vgd-mS_pVlT5hLOx__cHXG7-QMuTIEsGCrDEZrj9hxfIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروزقربانی سرمربی‌فجرسپاسی:
امیر تتلو یک اهنگ داره اول تااخرش فحشه ولی خیلی خوبه. قبل هر بازی مهمی اونو چند بار برای خودم پخش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCe3ix0H_nMmFgIC5qEq0HRtNTzt13txnLCZ1gXW1O-WEJBw9e7VVitcL6fDJzowmqEjx5UeLlHDzvW5TI5T5VEkyrHrtuKrSV8IS3bXTPFuXhIAmf5DbfUIujurdWdXB9Xbg7-vQacZZdFnbpavM-mwQSVvyihbJDabnAYPq8lWPC3GRaAjjqsuCZ2NOCWZELWGmuSOvFkPUccPZi9oTtTBzvfQYeajktrbD67-FDL8O6a-5uOks2z9Qwp1ihbup-NXe_QvDNGDWgj6MN9DFb8wjl1SG9br1tr8OjlcPqRg5RDxGeD2Vg5YyryxYJtua_hdozlo2ILY4GtDJGubTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فکت‌های جالب از جام جهانی 2026:
1️⃣
۲۲ قهرمان جام‌ دراین دوره حضور دارند. حضور ۴۴۹ تیم‌مختلف‌از ۷۱ کشور جهان. ۳۵۷ بازیکن حداقل در یک دوره از جام جهانی‌های گذشته بازی کرده‌اند.
2️⃣
۸۹۱ بازیکن برای اولین بار حضور در جام جهانی را تجربه می‌کنند.»جوان‌ترین‌بازیکن: خیلبرتو مورا از مکزیک با ۱۷سال و ۲۴۰ روز سن.»«مسن‌ترین بازیکن: کریگ گوردون از اسکاتلند با ۴۳ سال و ۱۶۲ روز سن.
3️⃣
کشورهای کیپ‌ورد، جمهوری دموکراتیک کنگو، ساحل‌عاج،کوراسائو،سنگال و اروگوئه هیچ بازیکنی ازلیگ داخلی‌شان دعوت نشده است.» «۷ بازیکن با سن ۴۰ سال یا بالاتر.» «۲۲ بازیکن زیر ۲۰ سال.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nStZrrebLV0qv1xng1rzJqFC5gNNC3_1vi5NZruLF4D-OwHgKj6ONRBQvBtj13fXS4gzGHVXf15uzhjYeejQOCx0K_B2fIo_D5OqV3yhlyWDoUiy8SuZzVFxkPAsIpYooA78WApe6cYa2KbbGEPF5GGh3ZFBV8lN7AlK6KDk3Y4v-3-DGkalu9IpHv5pBWq148b5hh-AvP7T9hpHnSMC3jC8OfdQrrZG9XwnxvGCJD3qJ4b1VgSNWL1DrC1Zu0vsac-tjeI_Y3H09qcIGMgwttb8Mr5jwsV3pfuMbh4E72nowlFWMR2iPtJpUIN8ZBYxCQOolM-PiVH1Ocdy_TcU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abowvUeHKWuvAsuRuNZCNVn2SsJO0hdifApJzT66yKEDuSyLYQe_ihBpEaJZwZS5xD15XJoaxP7FJCaSC-yUP6LLHrc9b5LgnBbqfXqSjG_dL9dd_8-rU55j3KFxQJnIep0MbX8E2krl-n5DW3vMSdQ4r7A66sQoNs5LzvoK7S69n-4gz1yHyhIx6RM2EYSSYyp3gbn5EuUfPSvrkbV6riIvvnSCTN27vrWgq84ziLdKyB7E_QZgKlQpMXzNgUYb4E-lhev07K-88ffUj24rAT8Kvtr-txRD1GBGBdUvjXf81QgCK5wrpd7bqmymeNy-RfRwUWp8svGLHzfO11brgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=jyCGFFTKwV_0Lq7UO7IvsUj79vNxUIHGOxsC0MUAChDVyVPu00MSYHjTu33eNYXui2dl34nZF03BbCK60wM0j_4y8sNTa7zNS0EU2Zyl-QyHOUVTfsPMXFYJ0D9Qz9IhnSD5tRVAMFs-i5ZoD5NQ8yidrV9gW_vZzRHib5u6C4PEBEO7nZ6uY1k9HvWRqmdu7B63Xp321LrnYw3oGhfZ79rrMTrZLnW2V5cHQ1bvQG-OYKYSjZgTsIcs19kr06RIuTQIOu3UbtIipVfivV60pOChL2gcK4ENzoP985zjVyX02-wYeiG6Paix9jL8RpxNr03Hd2K7htKK-JWWNh4IfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=jyCGFFTKwV_0Lq7UO7IvsUj79vNxUIHGOxsC0MUAChDVyVPu00MSYHjTu33eNYXui2dl34nZF03BbCK60wM0j_4y8sNTa7zNS0EU2Zyl-QyHOUVTfsPMXFYJ0D9Qz9IhnSD5tRVAMFs-i5ZoD5NQ8yidrV9gW_vZzRHib5u6C4PEBEO7nZ6uY1k9HvWRqmdu7B63Xp321LrnYw3oGhfZ79rrMTrZLnW2V5cHQ1bvQG-OYKYSjZgTsIcs19kr06RIuTQIOu3UbtIipVfivV60pOChL2gcK4ENzoP985zjVyX02-wYeiG6Paix9jL8RpxNr03Hd2K7htKK-JWWNh4IfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi0urSh2O1BEbeO2BKBaIuOH-bTddXpmZFt15ZrhqwFhA-KuS6H_Bm0-s0cAYQUmb-2RAAZo9t2AqnPJWno95eMBEzDu3CZfv3PNRrHOUG_Ul9bXYPML3MxoBMLal0-tOoHDfFgYWuJUEun3HNeZGk9jP3WY56rfWyqwassSjVe_xSi9yUQk7Ail_PrBHnb78aZzQMwJ1lHAg8EvIjvZmRLecJFM5fkOG5wKyNKn7s05O5HQKFAN3vO0Oo4b6iC84M75HWTmEBq9VPTGAMpxs5YdKllMv0EYf0Qyi-icQUvbTHGqf_jiTKW3k2tTJ8SPiV5QvwNAAHmCqW3arD79dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0L2HeGrHo6NT9NnmBqCNmGY0cylcm1vsSTH5Pio8lMZic9K6Gf---qc-4CxBA8rpL9RmxbsSEoi0k1BAOpJEHbZuEstkmTQoqEvi2TJZf340IJPVv87vZcyJhLTM8iS4uI639jw4zWIos_KlABs31mcSF-Ez64u0QPMzNYblonoAPZK1d3_OtUyi-jGEVOiRlQPdGNB_Vr-1wwyUuT0G1XLD2FOi1ryBjKmrclPXYGeXbi2x5CLmi5gXJOhKyfwb6FPjHB8HiNfD1oBirFYNelR8Jc1FScRbxdblaHIFmcMnEvDt123NXV4721vhcooZeO8-iJkoJBY1WMpbIdKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برسی دوپیشنهاد برناردو سیلوا ستاره پرتغالی:
🇪🇸
اتلتیکومادرید: تا سال 2029؛ سالانه 18M€
🇪🇸
بارسلونا: تا سال 2028؛ سالانه 8M€
‼️
ستاره تیم‌ملی پرتغال آفر بارسلونا رو قبول کرده و بزودی این انتقال به شکل رسمی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcTLiwrxKAuVHl3CqE_iWBmc2xP7hS0MspcxVIkQDMysyTadV95yNPKDx2Jv0mfcDARK1EJ00PWrt6hhZ-n4sSMlRvGBk9NPc3rsDcKc7SZUa1snyBmHRXhVR8TphQgqVMCCKrMWXo1oWCR96HlHaKHB-So6yu9aGsigaWc3Pc_ZefnIp24G-V2RaLdKmI8kB6tYKDi1-FsGThzUycVC5pedVaFe_wH65hj3zEiKX43G_VtnBTrytKhg4ElP1ZTCkBZbH_XDnkxw40BmBd8YNCTcVB9-MW4xVwCc5xxK0pTMPeYMjQwiVBmRNPCIB9T1C8LyXcK9j-eFtFHdfJffjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6dTKg_m51VwAShtDOLFW49IyjEY6nK6w1qeSnxgG_hj1BK7cLFIbBkgs3Y4WmW5bt9Z2x77EIGKEKCM5_12ioW7johPkhdOEMDK3SBY5GVBdPHIgHlwbbZ475vInfgU3AYHszKsYUovPJB6dnlEBAh082qRUq608A5kJcIMftvJiTF8UyHo8O-FbkCX-reuy_OrO8ziBKNpa1nBdOVxnImYjvJqm4-8SVWjK7Ahm2qXk4ClUyJJIQU37qL7yA6qYPG--vgiGi5znUhywYc9AtmJ1alMKjZbgKp4SiO1yuWf1QMy3fsrExJJQk1acGmltLEdTKOqRd00RT9E11rxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFHQ3nlzFo6foIrHpUOYUiLxUEmPBQIxAWvW0djSJw4BTGJpriV2WhN27KoEQZ-_vGm3UtQ7R2BM8QF82N6UYwBV6fTn5eTEe8-7ruJhNFECAPTtSIZouzLsd91HeQPfHgs8IO7awAAOHbRQtrPK85kMDt5usGoMoiGAtbuEUqEhavqzfYL6OOjmYBWXHfbYpwPV_SGSygkQwjEnTS5_tKFNDqKdGgSk0vh3wUuJnl-2LJzAE_zyW8juqaREvBWTYHYXZuR3I9qDKenUVibtUnQNU8w9_u8zzQujuFbx-GpPCv8O7c3tlLdT5oVsMxcVBfYijIdwKLqGF4JJ_bNWxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">توپ ترایوندا آدیداس یکی از پیشرفته‌ترین توپ‌های دنیاست که فیفا برای جام جهانی ۲۰۲۶ انتخاب کرده. این توپ میتواند در هر ثانیه ۵۰۰ بار سرعت، جهت و چرخش توپ رامحاسبه‌کند و داده‌های خود را با اتاق VAR به اشتراک بگذارد.آدیداس‌معتقداست این توپ می‌تواند بادقت میلی‌متری و زودتراز داوران آفساید را تشخیص دهد و به سیستم تشخیص آفساید نیمه خودکار کمک شایانی کند. این توپ بدون سنسور در فروشگاه آدیداس با قیمت ۱۵۰ دلار بفروش میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22724" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azH0i_O4hbw0mDe4HxbBJJdDdVTj90CkxdJrvCdcTtTjcxkHfyNojNMtDzQjS7JDJH1tMnQOkU2ty5TeEH1MZigFPFOmoBmxeE4yM8Izk3Nx6xSAv2TSS8VlchHSgOyFbolFB9OnQiqay-SK2IbCcXGftBzTT08Kou7FVQaBFnM8hOUIX-f7gXuu_D9zyd1icjx90rkOuzfBA9O4FQip5NIo2Pg-UGJ-FDHEypvDvXSWOYTsoFTQZssPcasXZeNldKoMNT7JKezoF94fMmpifSyuXzDR9tMdt6xK9q1fUFfz3KNdQOihpibKn5UzHrqmKypEx56hrDoGwUXLPw8WXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmHBF5zRuiBCLM9BFVWUdzzlR8IIoOCKm0fjoQjZGFxY5v3E1njVwitng0_OoKhYzo6st5ViHXdD29Vm7lS2xBgBlyXHI41LK0g0ibWcEVHgkILt9x0ww4Vq_-Tm8ikcJMENbIcVuqXfM26pcMyukVSGr8SkxQmZsCpmptOP_rvhAiJ5nRrR8ks1nHDyGb1kGbVkNrdEYekNEA-7kqnCQMM0ltLV3c0TQsjElFSSQzWaPBDJU0n93xsnmbKg_1oXqNPfKHFhsG4J08CztOW3TElRY_y2uConzHwO1TwoUeU3nnbMzloUYikXWbvQftllPMqNQl_PNXD1Klf9vgrTQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByfCjjKkf8iN06mwPeqINzWjDKdmmHa_W3akOpJNers6NbVdbKt4_FT_yptUKXI5GQQR7g3gX9NlithARePzr8hAjRAydNNb1CEEMS9ImuCkTMaSB_N5UFE6AE1rmo8xRj_NT2_V7Mrt50RJvGlLXG0vlWbCE96-PU8-mBI11xhKBJPNFZBSZ8d95xTTrCrMOzhM2_4YCSqsYHG6bjKvcTiBoIxFHHQW2aDNUqdWDDHkm1hjXL6_4oNcT58WJ3-Y2IrtH4nilH7PAvsyqPOFjjPexbvDfEUx-z8k2o8dUmUrjvYYN_IaGKTfrV0ijzHCYvQOFQREZVBgcgrmRSsxIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mb65jIkKTUNkjLPlg15o7ZvDQJ4ZJJCBmoFpTVoPoBu1c1cVi8WDvD0lSD3oFDrl9CmAZveDZHdVq2O70-gauF7-N3UcKmGb42Gb2UV4vWbEGjkOCrEWgEYVepg8McCv5Oqn1IEuGrf_yPCDfxEUpSIyW3HU5g0ols8EN_j-Ruo0gEzQin9YVsUn0g9p9uPu6_U6W6-qCrLboaisUJRukIVhzMjNLv2n5lrMDUGljhHC8ff1zFJISZB9WJ2YySYqV0Vb9aTEcpdl_ixqTWF-kFymhFObiWnbmzTG8h3ms8FtxWqPeRiKnn-y0V5Ggdn9Ypm4iNSUiy4C_Tl-f0nJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFNE2wI-qjWOyE-iccUD4skaVzuoZplYntX9n0jVKb_GOT7-ADVR2qKRQ8Y-5XtC05IPPpAc-V4SVHpdiyBrItBOmBJ0n7JZ3mljyV39Uq1LY0dNaXRw9RX8jN2wfBD-ttQBY1am6lqoQmBg09CiFVelav9XmgSgE8m5OdWCV4HJG44quXOnoFrDOVsFMG9KdUplkp7bS9ufsi_n_UR3w-q5E_c0D6IcP4FOB4sZkjMYZNxWH9X85ksXdf_Y1ANjA_4VzC-1nGlfGixEsuDKIN-JPIZqX3hfijSEgXLgIXIpc8SD57MjghrQsimjQLlNIUUIKimXCISbXVSfDlSA6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
