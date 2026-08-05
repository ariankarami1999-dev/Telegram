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
<img src="https://cdn5.telesco.pe/file/iTBzodE_UCx794G3vGbEbUCKZIZSVFLA0j0AHhZq8l4mOts-zDCa-Qq1pMB_hKWwAmIswISzzkha4X57htRvf3lyytkH4UgnZQDXkDEml35A9JrfHtem5bM5vIX33sAw67DSHSO1CHlXCxC0Y-JSTVmThfvC5O8G5gjRgc__W_iDL1irWry24y7L6va47caScFBjUnoX4sGnsP228kTK7P5AlCrbT5uqgF7MNgiZR9AHdMLtzo1F4U5ByUG1hSZVHJMRMy8kdv0QFy7l6NzxLuKkIOhIkVFbQHO-r_QvZs321DES5hX0dxPSfrpUHT1kcOvPTYBMr0m_67uD13Tq1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 493K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 19:56:33</div>
<hr>

<div class="tg-post" id="msg-102800">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn4MYVcUer6hFSA_1APDFjTYj_8Co2gpgkxmtLast69jAO7vYPTQ5EEDA8eoQ1b0cva6innlF6d4QH-M160-_idYf1GVuNOpNaKl0UBl175HCjgYl7jk2nCh2RQ0bl1-RnA48s7G1L3q0NuiFxqRV9dlQjKENplPfHc4j8VctFrsemEFGhk771YSvcAE9mtQ2ltKtcXqXO0nAdpg-p0VGrAjKnfgjTuFj42AKdPU_liG_GF5RXTrUSPSs_NjIoSGNPhtD04jOxQb0KQMwFZbqioS-0XL2Oab667foX5FIhcNrLvWu0UgIWf0ejc8JHu2H1cf4Bd-vCtwCZJkxl2hJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
استوری جدید رونالدو در حال صفا و آرامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/102800" target="_blank">📅 19:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102799">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b7936557.mp4?token=d0tXlzlg626kMjmQr6NNks0AwX8mKn78H0XJJiRskiadlBcVh83LVQiYMrqa_sozVFKdS_hqZyUOPG4APlFwdM2GVzbE2EuAZtMZSAb3BFzKhFpkD7QiCY8CsEMnIAnHOlmVH8k6WIEHXnkQUQIirNk0JbDIGH59LCsVBCZumz7--K3-WPgMN9A0IaxESboz6BZYXC8me21EtrfDeOXUQSjLFFDEsk_jvy3fWem-IwHrjzqulpeTqly47Gt6zr6RCmEBQnVNuDdHrUtN03_AdVRYa9XyBDLTod6fFOzvY9ahMp0jhp9Dn3B8aID66bb1ZOLfAb1YeD45X4QAtxMNZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b7936557.mp4?token=d0tXlzlg626kMjmQr6NNks0AwX8mKn78H0XJJiRskiadlBcVh83LVQiYMrqa_sozVFKdS_hqZyUOPG4APlFwdM2GVzbE2EuAZtMZSAb3BFzKhFpkD7QiCY8CsEMnIAnHOlmVH8k6WIEHXnkQUQIirNk0JbDIGH59LCsVBCZumz7--K3-WPgMN9A0IaxESboz6BZYXC8me21EtrfDeOXUQSjLFFDEsk_jvy3fWem-IwHrjzqulpeTqly47Gt6zr6RCmEBQnVNuDdHrUtN03_AdVRYa9XyBDLTod6fFOzvY9ahMp0jhp9Dn3B8aID66bb1ZOLfAb1YeD45X4QAtxMNZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادمین صفحه رئال‌مادرید بازیکناشو اسکل کرده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/102799" target="_blank">📅 19:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102798">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKLs9OnZx1-hGG0Gi9cWge_F7mLqLhDSH34ra37a0_6sc5jbz3U18ZzkxMHhROW3teYDg4ZlyDvydga-omGAMVN1_QIOCMCchrVNGlJRoeYsaF81G5aiYL0M-6dGG3IG95R-mOJL54yCNJYFAPZt8E11uATQMAdjtd83-yL3E-mFPg12gqgJfEP2_Nh_ACsxmeyL5OXg42OV7MYuwhkZ3iBnkUaMcS8BXYpt_4PZgo0c-a1B6RoxNxduRAEj2TnSfpp7VhvREVvCO4DiWmXTh-ZPLpOhmaZDvqR_J756q7pO7811mmcdAHzFwTKULLkjJlJvsPealLD8bIguhJSPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🗞
با اعلام رومانو، مولینا مدافع راست اتلتیکومادرید راهی آا‌س‌رم شد
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/102798" target="_blank">📅 19:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102797">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a21bec45c.mp4?token=I-c9M_mbZiz4l5ZXmATRig-FucPPXPxXK3xrcRXjeQBQwKa5sz09UWuXI2cyvgGJjI6T_wBrVh5Ya_C8S4QxzPmL9l0aPtT9AEYwpymfZ8cBoKs4_TpJuorTpqHUkSmvbajQpgPZ1mrEwWirS55Xj3bPE-_zUDQt6BlV1iaVlIX-vJ7l2OEjbg_N2QjSo4_puQU-qA-810Ri5txXivGphI2R2D18vwCumtKW4DSwTneBcHhuVgUEkpvVScK8iuXa2tkgZVAgMYXIvNtRw-UORGjorKWGbp7zDIRxXdQk_qA697Y6NmNkv2eAkQaIpeahMosjfxPzzRPtaySGEnDkAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a21bec45c.mp4?token=I-c9M_mbZiz4l5ZXmATRig-FucPPXPxXK3xrcRXjeQBQwKa5sz09UWuXI2cyvgGJjI6T_wBrVh5Ya_C8S4QxzPmL9l0aPtT9AEYwpymfZ8cBoKs4_TpJuorTpqHUkSmvbajQpgPZ1mrEwWirS55Xj3bPE-_zUDQt6BlV1iaVlIX-vJ7l2OEjbg_N2QjSo4_puQU-qA-810Ri5txXivGphI2R2D18vwCumtKW4DSwTneBcHhuVgUEkpvVScK8iuXa2tkgZVAgMYXIvNtRw-UORGjorKWGbp7zDIRxXdQk_qA697Y6NmNkv2eAkQaIpeahMosjfxPzzRPtaySGEnDkAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚠️
هشدار، ویدیو حاوی صحنه دلخراش می باشد: صاعقه یک بازیکن فوتبال را در حین مسابقه در تایلند کشت
❌
تلاش‌ها برای احیای او در زمین بی‌نتیجه ماند. به گزارش رسانه‌های محلی، ۱۲ نفر دیگر نیز مجروح شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/102797" target="_blank">📅 19:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102796">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq00Y6IF7KhBN2VSulcgs4wYTapBmIo7CqNG6K-gYBNNfWTAjfQ5jEgRNbcHudWa6mdZvnZemrEa5QHU8MZXpw9wm-GtzculHX8eB6NLwqtrhIaeDPDLaG-PJyRg08HhxeYa2j2NvQB797GtO2R2XI8gXlMqG4mAQRw6b8C6z3JBi6Q2sMD1QWPGc9dY0l3ZFP8borr1RiwmKJ56dmJ0iQlEufdfprR5r3gz28bxzJ3HBOcv24no9cLKOgQFzesMvgrov36TlEWpMPLPhN5WWpV33rk7vnhPW9PoR_DZnjClB-rCoavz87VhXJQdzkv2J2xkmgoTHRVxlGCOcJp0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
💥
جزئیات انتقال دیومانده از لایپزیگ به رئال‌مادرید به نقل از فلوریان پلتنبرگ:
🥶
مبلغ اصلی ۱۲۵ میلیون یورو
🫣
مبلغ اصلی با آپشن حدود ۱۳۵ میلیون یورو
✅
۵ درصد از حق فروش به لگانس‌اسپانیا تعلق داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/102796" target="_blank">📅 19:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102795">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFYs7hntxT2LOPMUDH7MTtMnW-XjzmGtIx3v3p6Ql7VTx3QZMAkghtaNjGpGcXIWe2uM_HsIRmTXPOziq-J0NjRKoPWNFAf4SN7NzmWIkRC2sqgQsej_Adi3nVysntEPhdAtTHpkxI7iNMuZDRYxxdt_zKLWi0VPWcrYi30T0mdSzYZSDE38csxaArFcVZk4ghB4QNI4Np6qy5SVJvY0ZEvAWyy16fFnBlVdmX9sPLwRiAHJY-D6lIRfivqd78LQC__5Ro0uLZahAAVvju_u2KagYbmVSYYz_Lc5CvI-pX0hDFn71JafPeV_FaV4wYsAtEdWtkBI5SnR3Id3DW0RZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
#فوووووری
از اسکای‌اسپورت: وینیسیوس جونیور پس از مذاکرات امروز با رئال‌مادرید شانس بسیار زیادی برای تمدید قراردادش دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/Futball180TV/102795" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102794">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833c1a2554.mp4?token=CVGPqgRGiz66P2WQcD6g8I9CyGBB1o0rXQ5dVn0sC_8x55BtfLCyicDdRM_jypx8tlLyTYzM9Ck6-aIg_urFzjMv86XKqot-7EOGyPHdGVcXoFLIZmu3GBRWd5BUeb3x5xMcDjr4Y24ublMTRv8Am6jXTIF-UmU0O10YpgVnFOikqOr2Ubs5bNWaPFFA166onUTcCK16xfj2D734SytKiiCG_jf1cjT0vZ-XAinPFso0drECoWNiyye1G33Lw5N6VbHX2p1iStqIZqRGT0qA8UPm7DW9-_aht_K4BxvPuoItD68AGeHXFfEc_Zztka9fBnpIWLZy1XYJrW4k9c1idQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833c1a2554.mp4?token=CVGPqgRGiz66P2WQcD6g8I9CyGBB1o0rXQ5dVn0sC_8x55BtfLCyicDdRM_jypx8tlLyTYzM9Ck6-aIg_urFzjMv86XKqot-7EOGyPHdGVcXoFLIZmu3GBRWd5BUeb3x5xMcDjr4Y24ublMTRv8Am6jXTIF-UmU0O10YpgVnFOikqOr2Ubs5bNWaPFFA166onUTcCK16xfj2D734SytKiiCG_jf1cjT0vZ-XAinPFso0drECoWNiyye1G33Lw5N6VbHX2p1iStqIZqRGT0qA8UPm7DW9-_aht_K4BxvPuoItD68AGeHXFfEc_Zztka9fBnpIWLZy1XYJrW4k9c1idQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
وینیسیوس گذشته خودشو فراموش کرده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/Futball180TV/102794" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102793">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خفن ترین تیپستر های ایران با هم جمع شدن و TRUST BET رو تشکیل دادن
👍
هیچ سایت بتی دوست نداره شما این کانال رو پیدا کنین
رایگان بهترین شرط هارو براتون میذاره
حتی هزار تومن هم دریافت نمیکنه
سریع از این لینک جوین بدین کانالشون
👇
(این پست پاک میشه)
g14
https://t.me/+cBQ8n7zLQiUzN2U0
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/102793" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102792">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX450VxPkNwhbNqhA9xvNBzkJQ9Epz1hfFQfmgKbhuXgsIuIMaUe_r7VT3rvKWQmtG1UXQEuafS6JJlwys6ZdN4Gg3OhIBc7ZS9Xh3i9o3IiUKbvZJZKkGm-bAnP-mbVUPl9-u39jgowWUoKwNiPnlw6wZnoQwrjyN8rUSCuuzlWdps_y-qH5i9sGeYIpQMhOe6S5E2PFQK73tqL3ZWYIVrCY0EGpTpOtGmD0z240AvsIs9lxp33AnLmi4ucBS6LDy_jpcwTbfTotiVdJNwKPYgOz5kP2WAxaCJ6mvMQj_-zRCnW6vdad72_4EI9qtr2MT4U3h-3niY7hyg9PLufIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 میلیون تومن برداشت روزانه ی کانال تراست بت
🎁
پول دراوردن از بت تجربه و استراتژی میخواد نه ادعا
برایند ماه تیر توی کانال تراست بت: 78 درصد رشد سرمایه بود
✅
40 بازی اخیر 34 برد
📊
💠
https://t.me/+cBQ8n7zLQiUzN2U0
g14
💠
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/102792" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102791">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a91c5460c.mp4?token=qbGiWhw6uI9k3D6bdFzvJWJinWBVydL7uyDCsoXvP8HjIWRkvd0MuXE3ekGIJQyJnxFYd964rKgRdSqwB0dHsf0BQV9WIRBujmKD3gw_cHG1vWmXxjVBXlLRg1-EkgM0M-MfXNRh6JSVCR3b1WWdo1UIQ36_JfY8cd0yORAjJ26TjkIbC_06hmFQkLAfj-62l2JNsoqnC4zgmaku3URFbJM8HlGf4xFbsrvC6frcyyJB3MomLNCQAEiaESIW36_9HbNBaEgW98kpsVe_0vO2Tu2ByRxnB2zxfiJUcEnAKH6WAvjXP9PxmsEpmyaSXHeALfobP3ooW9kddj83hSIAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a91c5460c.mp4?token=qbGiWhw6uI9k3D6bdFzvJWJinWBVydL7uyDCsoXvP8HjIWRkvd0MuXE3ekGIJQyJnxFYd964rKgRdSqwB0dHsf0BQV9WIRBujmKD3gw_cHG1vWmXxjVBXlLRg1-EkgM0M-MfXNRh6JSVCR3b1WWdo1UIQ36_JfY8cd0yORAjJ26TjkIbC_06hmFQkLAfj-62l2JNsoqnC4zgmaku3URFbJM8HlGf4xFbsrvC6frcyyJB3MomLNCQAEiaESIW36_9HbNBaEgW98kpsVe_0vO2Tu2ByRxnB2zxfiJUcEnAKH6WAvjXP9PxmsEpmyaSXHeALfobP3ooW9kddj83hSIAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚽️
برادر گارناچو که فوتبال‌بازی‌کردن یادش رفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/Futball180TV/102791" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102790">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59768147dc.mp4?token=P6ueERHNiFolUajE3UxcKd4UA8neDCB5TpMmikuFVUuQVGgwEPNlWoKLrWds4DrroZcgisR4otA06pbEMtd7X4WjtGRz2kfLo01k5EDQXQZJQo0E9yMa5I0R9vWnoA275VNn6tUBhhFPGtSbd7aO5DcdDGQBu7Wgex1MK6b4Llr1Zn3GR3IwOZis9bFNgk2flipyhKngehuUoKttr63Qp85aKV2UEv0LYiANJdKpHWmJ2wpouuFSSlxCgJ0kdFTFpeUjGUlqZJzr2SdVslOtAvwhBZmGO8jawGsEf79AVRrQeCQKoYiyPxmegdLQZyGUCJbmnjqlkLVdZCWhRQyvZyoTau1Eli_F5i0uqQlSui9DDZ_tRvGMRdqTQU05wQLZuqxxlaiBxw-X2Bk6GvDjtIlj7jCthUVZBJ8JNcjDMNa4dKi8IuzGKuvMm6PSwnRilmKTCszmkp8ZAZvX6lkVaz1xZa-3TJiFP_ZdksuAHQ2ZckMktPorXLx7PTodBm6YANZ09XrwE1Pn_Pnqvm1IC4wyOqfI2uhrufB49BWxpsSQw_ps7QbdnpJ92WR_v0wlW9x-nbKlHlCs33jjPADo7cBUU7HwzJUPFp3sXfoaGwJsOl6ktqLWLMGf1RVDU6PIs3GONysXA5Tk_edU_HJXyZ6RiAn57ycyGQTpdm7pq8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59768147dc.mp4?token=P6ueERHNiFolUajE3UxcKd4UA8neDCB5TpMmikuFVUuQVGgwEPNlWoKLrWds4DrroZcgisR4otA06pbEMtd7X4WjtGRz2kfLo01k5EDQXQZJQo0E9yMa5I0R9vWnoA275VNn6tUBhhFPGtSbd7aO5DcdDGQBu7Wgex1MK6b4Llr1Zn3GR3IwOZis9bFNgk2flipyhKngehuUoKttr63Qp85aKV2UEv0LYiANJdKpHWmJ2wpouuFSSlxCgJ0kdFTFpeUjGUlqZJzr2SdVslOtAvwhBZmGO8jawGsEf79AVRrQeCQKoYiyPxmegdLQZyGUCJbmnjqlkLVdZCWhRQyvZyoTau1Eli_F5i0uqQlSui9DDZ_tRvGMRdqTQU05wQLZuqxxlaiBxw-X2Bk6GvDjtIlj7jCthUVZBJ8JNcjDMNa4dKi8IuzGKuvMm6PSwnRilmKTCszmkp8ZAZvX6lkVaz1xZa-3TJiFP_ZdksuAHQ2ZckMktPorXLx7PTodBm6YANZ09XrwE1Pn_Pnqvm1IC4wyOqfI2uhrufB49BWxpsSQw_ps7QbdnpJ92WR_v0wlW9x-nbKlHlCs33jjPADo7cBUU7HwzJUPFp3sXfoaGwJsOl6ktqLWLMGf1RVDU6PIs3GONysXA5Tk_edU_HJXyZ6RiAn57ycyGQTpdm7pq8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایتی شنیدنی و جذاب از لوکا مودریچ افسانه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/102790" target="_blank">📅 18:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102789">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
⚪️
دیوید اورنشتین:
🔹
وینیسیوس جونیور برای موندن تو رئال مادرید 28 میلیون یورو درخواست کرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/Futball180TV/102789" target="_blank">📅 18:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102788">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bL0D1clbb_8mHOrPH0a8ohuknTdJNyHGJc5WAoZd7Gl_sF8i0fVRtKDLPqppK-qSyt85z4EGXmcWJRT9VYH1SdQVdrRJ_HRgJDWZJkT9I8nYNvFkMytaejOub25eScTrIAg2cobSW2ezmd39DFGveZ1X1A9Y1RwWhfddxRnmEaZuUox2rAfzFxfawapNz8vpjdi3T_FQhIpv8XlQHbgb_VGmU_VUxu45m2BDumwyMl2nywTmOWnOgzdMoASv7AghCnLAqQSHibuPJ6YNGUACdmM1cfub-cYzBYa04Mht3xciCPzF6Y3i-I2IJ0U4plDYKpRfLZrJ13X2Vo2Nr-Jn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
دیوید اورنشتین:
🔹
وینیسیوس جونیور برای موندن تو رئال مادرید 28 میلیون یورو درخواست کرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/102788" target="_blank">📅 18:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102787">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UehO3pRaWzYnUFLetJs0EJu1aaDR1q-tIV_DcmKw-vT1wwl259uDXM1yVa3oKs_VSi94wPWj9alBJkfaT8EUulLFeRVMNvJGYEnX5VeX5SCPBYnMN_bMoxlKDnqhsIq8hlQy39kDWTE6vB6YG_no4dj1eJISU_8HdkhL0Nf-d70w2y7jWCArCSHVr0NraH2EQigkHgMdXbDuIip2GkZgGflFYWoKzuxO98dAhcFqe5IjN-D0iHaM0ocay9t8M2m62gSUL5SmyLNjqhQMCZ642QIlHavr2MJMT13kOmCXq1Hi8XbUBKv5bl3ZD7YseDRKE8s9_zsiKILlNn871_RCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیس فیگو:
اینفانتینو همین الان باید کنار بره! رفتار او پست‌ترین، فریبکارانه‌ترین و خودخواهانه‌ترین رفتاریه که تا بحال دیدم، او برای خوشحال کردن رفقاش از هیچ کاری دریغ نمیکنه. ما باید شرافتمندانه زندگی کنیم و به یک قانون متعهد باشیم، فیفا هزاران مشکل داره، اما فقط یه راه‌ برای حلش وجود داره اونم رفتن اینفانتینوعه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/Futball180TV/102787" target="_blank">📅 18:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102786">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d841566422.mp4?token=dcEgxIzsYM39LHvINabosAk2x3UYAHY07mL03X46zuflDm8bdNokBb2Gc5znRuNuWDsKBXEzVluDKFkMAQWKzpZ_3cTPSRZ_-4R5m3kJ3Uam4A8DctE0oaEjFm1RG9_qe7deRAjCG3VYHn5qfG6MdiNfNFHGTtTDizANe3kN3JnfHETCVVOLmJD8ixS9RBPPUs_V8IT3u-DdrqZMmL8ksYSBy18OlTw1HRNtu_H_hlK06wg2xSP49TURGZH6ucFMsYd5nfp-ctzO5DVE5W3A5SZ5T_ndCYR8e5SI1yQgmJ_8gkGrqoeJMAmQkYrKXhu3Lf6tKwtd8RD7mRK-SFhz-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d841566422.mp4?token=dcEgxIzsYM39LHvINabosAk2x3UYAHY07mL03X46zuflDm8bdNokBb2Gc5znRuNuWDsKBXEzVluDKFkMAQWKzpZ_3cTPSRZ_-4R5m3kJ3Uam4A8DctE0oaEjFm1RG9_qe7deRAjCG3VYHn5qfG6MdiNfNFHGTtTDizANe3kN3JnfHETCVVOLmJD8ixS9RBPPUs_V8IT3u-DdrqZMmL8ksYSBy18OlTw1HRNtu_H_hlK06wg2xSP49TURGZH6ucFMsYd5nfp-ctzO5DVE5W3A5SZ5T_ndCYR8e5SI1yQgmJ_8gkGrqoeJMAmQkYrKXhu3Lf6tKwtd8RD7mRK-SFhz-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سکانس‌های تاریخی ورزش ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/Futball180TV/102786" target="_blank">📅 18:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102785">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1Nq2JxWHixCXK2aNhfB92lLbGvy9kW2euu1pt0Lhb-0qCzTJ0UID_yqVLazE8GHumyqeMCm_Ff1fH0OFLTPgoIOX6YKY6TwhpeD_rTonyc0Ji_JPvfXFlimzBu0glq3eMcJiIW8Mn19GrLsCe3LfqctWymCxTNg10Hy-zOx2JPbEfZovk4mSZeKv86T_q-tsdbCPkd0Io5q61d8qWa3d0V5M9kKRPRLWjGqTcFdZCTTbasLV0hODontadOQZNsFhKJxzIXR-EWZtcflWq7DxpHBupfz8NzZ0xwrcjblqlPByF42e-nYzy9IcyyXyZyuEk45Q_PnndQhmlmyWy5bBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرسنالی اینو داشته باش فعلا تا ببینیم چی پیش میاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/102785" target="_blank">📅 18:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102784">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
وزارت خزانه‌داری آمریکا: تحریم‌های ۳ نهاد مرتبط با ایران لغو شد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/102784" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102783">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa7464e72.mp4?token=D5a5cgqBko1V6mi-T3Lq3kJwBqfLyx-6U006DlA-MKLkWljQGFggpED-dl2FPvpoEjilPEH_JrG8w5O_v4uzVpMobH1rug1Z3VlwILJe1g8eFpBwiiquNheb482yOzd7fHmzo4YPFBVLMEhekuwgz3KAX7L_L7pQ3PT_y7E4TAApR8zEfw_5TAIFDmG19V7phqIKN80KRXOahvx6H3Ms-FTF6wPZfVgmjX-Xw9DumCFTz953QbyAE9-4_bFJtnzU28yBSqP9DHu62E8WmXQzqvJVQZI0BPsc8teO9193mJiMSRUY3Q5CvFeCOO6hPcclbRSphGA_qwTYmcqBfOGQmwBNyWPG0gdZfEX9k8iGHFL44QkNWfPOWcZLBOdGncs8b1aXogAOGtB9SgT0WEjonpTjkptUTyIOuXAuL5bM8M6BEy_nvtIN09IT5Hj_Oocb3TkejLuOS-c4bBuXqc-EycUrwMMaHgRgn_Wl8h6JSr86NgujY1roimrkghq3emy5m7JvZLJwQuWLj4IPNaneqb3xDmgYVRo_aYy6h1mRwXIPKPBqjeQChBnow8H7ROeZXb9FQAEruxIuXO3SiwgXjvzq6zhq-0bD_GUaHONUyu3isO78SEDWEJFDdwbOVohEVXLdqF7hb1YaOaqWKyOV1A_eXFbVv6fZcVwFUKU6blI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa7464e72.mp4?token=D5a5cgqBko1V6mi-T3Lq3kJwBqfLyx-6U006DlA-MKLkWljQGFggpED-dl2FPvpoEjilPEH_JrG8w5O_v4uzVpMobH1rug1Z3VlwILJe1g8eFpBwiiquNheb482yOzd7fHmzo4YPFBVLMEhekuwgz3KAX7L_L7pQ3PT_y7E4TAApR8zEfw_5TAIFDmG19V7phqIKN80KRXOahvx6H3Ms-FTF6wPZfVgmjX-Xw9DumCFTz953QbyAE9-4_bFJtnzU28yBSqP9DHu62E8WmXQzqvJVQZI0BPsc8teO9193mJiMSRUY3Q5CvFeCOO6hPcclbRSphGA_qwTYmcqBfOGQmwBNyWPG0gdZfEX9k8iGHFL44QkNWfPOWcZLBOdGncs8b1aXogAOGtB9SgT0WEjonpTjkptUTyIOuXAuL5bM8M6BEy_nvtIN09IT5Hj_Oocb3TkejLuOS-c4bBuXqc-EycUrwMMaHgRgn_Wl8h6JSr86NgujY1roimrkghq3emy5m7JvZLJwQuWLj4IPNaneqb3xDmgYVRo_aYy6h1mRwXIPKPBqjeQChBnow8H7ROeZXb9FQAEruxIuXO3SiwgXjvzq6zhq-0bD_GUaHONUyu3isO78SEDWEJFDdwbOVohEVXLdqF7hb1YaOaqWKyOV1A_eXFbVv6fZcVwFUKU6blI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکات فری استایل یه دختر خانوم با توپ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/102783" target="_blank">📅 17:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102782">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDYuZCrUU4iVRNhEVRVUiL2_LNpsjScPb2HM_8Lsc2EJliZYQvaqzxAkS-w2uQbPNigajFk_nPJloAT0YWZfF5du1qZuDgC87FcXKja3AQPKpNwgNfuzUFtHGFAfNdlQBP-PgL8ln4Dl9Nkzj4hry5P7lEBp9RIfJfR-GD0mh5zWbRJDeQjwg_EkWKPl--NMAoX_GXeN_ckOg6prkLjNXzv3ESVf38IDr3EmY_U-nwIP9H6H3hFuHR62BA-OJB-W3HO1UsmS1WTzzkWtqncgf15zuUi4FzKzVMDmGT_fSWY5H13XYHb0XGPgWFb-MN-KDwI-iPAW_yFRQ8A1t3HsMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وندا جان دیگه کار از کار گذشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102782" target="_blank">📅 17:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102781">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_7hsfd60WLtcePNY16yOa5vnMSGMHQJ1xUmz-kLd3JUwQ5t98xbAXaNcESatnRRCmIOIpjGQMMlCWqt2y4PRUTphpYJE6U5Ejt0X4PnA_4vCm_pff9LZz2PsQ8ZZVwLKFvueCm7qGs540DJn5nyw-eEIYR4T39Ugz6JqqT01qWqXD8htnvZL_I2zlRRXO_GYLwU7PZcp5pqPYDoyD-izz6FgP48fVVS97e-EcPyEbjhYlGwkB2cGKdWY67TGrwPP4bUvZnphSjMMnUlfCZntCAFThB8AuNbu0VcQZQMqNODM1htq7a7BwFNlkhe9HXXczrsp6DZ7TPmF-tVrTKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار در بارسا
🆚
پاری‌سن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/102781" target="_blank">📅 17:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102780">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvaHtjwurhXGqWimkoaxscL5dWTNHbJpPgIO654ErvthSZrq3CmkDBYDekg5an7uux4WUjTY-gOJIFcqdQ8kg2UYQ7GrP8VW899UBobJqORC_tMAcWMl6mKHcVxHKaBzB4UgV8SPO3SS7NQ0S_l-I1z5gti1o5zRCYaFdhqPMUtUNjk-FtCLEQrelXnwofqMpk8UK1Gzqdk6R_UTQXyUW-cFfW2ATkvyiwgeqIHsT5cfh-yRrXlRXHTC-eOF7KtGGaRVOcSF1muMHf0EVpv17LunOVTzjN9AReYDuwlOmwI8S0ctdrczXZ207uqK01cqeKSPo8jtLSlXa7D7sxp2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
بازیکنای مطرح حاضر در این فصل سوپرلیگ ترکیه:
🇹🇷
ترابزون اسپور: صلاح و اونانا
🇹🇷
بشیکتاش: تروسارد و نوبل
🇹🇷
گالاتاسرای: اوسیمن، گوندوغان و سانه
🇹🇷
فنرباغچه: گرینوود، کانته، آسنسیو، تالیسکا، آکه، اشکرینیار، سمدو، ادرسون و لیواکوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/102780" target="_blank">📅 17:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102779">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtSsVisNQdef9zeXkWJa60MBEXmd2XZijj4nIaL4Ewca3XLxC1uydieRVfOtEE9TcnkgrDkhWB4x9ikdlAhegiVctcvAT8A4GeAcnMjAtn6IeIPtnTrDdu8cKD-yIz-VkW8mXDm6pxn6m45TFCADTKxUgVUblvuqtyOP7LmZ0mOjtiWwhmqFfiIZQq7j7po0qwOaHcqnbV5KqYG_VND-Y6h8DN6xogDHBT_XX57RbD4wXgzKV8I0z4Ge3b9FDcG1kXKTW1wi5fS3xtpDR4USg5vyW2hRmX_rxI5pO4AYgt7bjFA_dl3pcm-X9ZoHX-l-zKkKMN1ypgzSGrsuGL338w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
چلسی بازم تو بازی دوستانه باخت؛ این بار مقابل یوونتوس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102779" target="_blank">📅 17:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102778">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHjNRJwm8wCM4a1SFwjRK-XmEMTTgwaVwff-JAnb_zQ_zj4bwvK5OnG-wgWuJbMquJZtCWZiRU81tL84elnKLQt45ZGq_Jp79JILnpa7Vy7D-MJ1InlImCtUY04o0_tpW0N9A2pnnq2pgXHmZaRsw1Xb9yqGWBX7U4fB6HOrZIaWFKorP5D35d4mIv9eA7CX3TCNusz2ch15kImIxj-KAs7_zoU-vhO3b0XzBeilcUe7wCXGb7e_3vgnfzrbtdahnuTXnM-gdljoHnvvzM52USghUFav-6f9KueMyzxJYB1lQJbz6xZrSfnTg0GxA6xJXt5mydsODPw6NXXc3Zmwcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
چهار خرید رویایی رئال مادرید در سال 2009
:
🇵🇹
کریستیانو رونالدو (94 میلیون یورو)
🇧🇷
ریکاردو کاکا (67 میلیون یورو)
🇪🇸
ژابی آلونسو (40 میلیون یورو)
🇫🇷
کریم بنزما (35 میلیون یورو)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102778" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102777">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyVN60snFb_QYS57y-66RMqaoVe1BOOBg9MKvbyOhGZd7lLbZUXNzw2gVuoPgKeryjpqCZlHMmND5B2O9agNhb0S06kiQwDTGE3WIk3_Ey9r6Q48o_aQQighTAkg6pFn2VccYE2VydAuF6o4zAy2KK_KWiaBXk2tYh3zHAkORjjLbRACViaIzLM4UZzZIHAlY9L_vn4DMdUj-peX0zcFWUHdYTznT1kjPM-VWJkfN1ur0BhGEMYKsxGfH4ol4TcyspK2mt0k0YETM-EeA1Rv0QKnbi1mql0XX3eSjFclxwdnbA_uYb_y4lpLo0_Lo1PmZLQ2UAp7Erl2NUlzwuhsbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
بارسلونا قرار است بزودی رقم ۱۳۰ میلیون یورو برای آلوارز به اتلتیکو پیشنهاد دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/102777" target="_blank">📅 16:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102776">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb91a96282.mp4?token=rhGFTFNDxI0Li3XU6aaZ3zriq6nzLuXZ5bgw01f6dJwZuVdtBSg9i2lZoiXPp-a87O6TX20oN-3F9RoUj6SBtGNBzTNV4RrbHdwj2AyAoqvZUuQ3Mu4v6jJ8H0h5nz_iq23SR0CtmjMPa8D-A6D0sCGQysh-aWjH43Eye5EL6WX7lR3OQPzFXTUhh4HWKuYZFJlectlbwzDzxb5di0j3B-pmCdP0xqROY3u-S_f8MIUZh2wI6Sg9QY1zdCJMuVh9rAnF2ibcW1ExQNIFRxLklz1BU5trUuUvf5httBQTX7zoRKyv68g5lBEYz9Pr6GFjanP4VysiLiR_frlxj7Tg_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb91a96282.mp4?token=rhGFTFNDxI0Li3XU6aaZ3zriq6nzLuXZ5bgw01f6dJwZuVdtBSg9i2lZoiXPp-a87O6TX20oN-3F9RoUj6SBtGNBzTNV4RrbHdwj2AyAoqvZUuQ3Mu4v6jJ8H0h5nz_iq23SR0CtmjMPa8D-A6D0sCGQysh-aWjH43Eye5EL6WX7lR3OQPzFXTUhh4HWKuYZFJlectlbwzDzxb5di0j3B-pmCdP0xqROY3u-S_f8MIUZh2wI6Sg9QY1zdCJMuVh9rAnF2ibcW1ExQNIFRxLklz1BU5trUuUvf5httBQTX7zoRKyv68g5lBEYz9Pr6GFjanP4VysiLiR_frlxj7Tg_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🔥
🔥
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/102776" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102773">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stidUZnm1IMoLxbxrGUf3hUlGi8RcJlyl5bTWHoc5w1iWbS1tkASh_QYXzybCiT9j-vZcAEW2frK6Zjv3Ed_spsyEHERlpD2HVb3JObySvXKbSDz2xYgWCAAz-54HfNKI9VKTtX-GlG4A5l23EH-vJMqzqOVq9RjMuf2JE8h1kqx3qMKDaqICC-nl4GRX074XVexX0g5X5Zlgk8hfQkEGufap116PViTIsTFRXIoPu1d85xVUuWeKDZ6aglEzMuBN-ek9WMC5ipvoH3yVWlMJK7ntaTJG0AC80kNWsGDzfUNNottTq3o-OT6DR2Jb0QG6YJ_V0u3zmtYu9ZS9BtoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VmycOOThZA7XZUqjvHPknI_fZPpgixbF3QuSWBz_98fkh0As54ouXauAtyE8U8RCHjaNHIQ25JFUkE1gIC5ONK1hj7Zec0SClTGt2e1aCqFmQFmXD-TAdjwJz81j1gRyX-xiaafvmQT5_YsjU2reC-Btx4iUNSi-YX9uGeu_TlMgMtyRR_BhV1ajumk71oED6QWNRo0SjCGXDXxsd5hYEMLufs-B2TmHrqeKvmqAPiP01NlcOEC58i5TFpqkkoDZD9taBGG5XuPFF0ZP5SoVNmTvBGfhrGCs-8yZBnJuGf2vWkHlFM7q6MBY_LwnA8e6QTQKee7kEwphn4myg0pLHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqIggQhirsAcpT-oJ_IEsxm0ZVrGczqN7kCylhi1RaUXVF2Lesbvr5d9yJZKgwky_umOPbab7mHSgCu_0p0jejH8k4YcgXAixbqggHRQeXz1qVrfl4ZKsQSzzE41HFeHjFd17dpBZUq6QVF71LN1jh8RrrzlqwgPksM5nnIx6vwkzE9W6EYW09HloMn1pziM3x3p6YzeeMiZBfLcObcPYdyFQ2c5jv4mMzpACYhV86UAS92qi38RlgMpwCmomwLEC8wZq0Rja8pF97mto6McZGSz6bzPRWp-R_OiXrIVpDPproEQJei0VEnoLc_bH2a2xCUhGBxjCJ9sGlgJmHhUAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم «کومو» یکی از قشنگ‌ترین تیم‌های دنیاست.
لباسشون، شهرشون، استادیومشون و جوری که مرحله به مرحله و از سطح پایین‌تر ایتالیا رسیدن به سری آ و گرفتن سهمیه اروپا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102773" target="_blank">📅 16:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102772">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba5d6f365.mp4?token=uxVuwyiSgmVNKw67AtNNLmCtgYKmk1S2-OrhrWbcfBBP9DG6fqvPZus4dc5oqGyD2M0eps3BL_KxQiZqQxHFWhd0WoLSyj-Wd2iagkaP27C7hmZDwZmWrJwevFl60IFbiKPnmUcUXcuYO8GfABJS1mTlD6ILpBb-hWmY7I15YSFBtG0ve9QMZUkPvkAFG0cZNodls0wnc9Mp7kxU5KLmcIUas8wkn44J70hxiN7ufOuWI9nyJW1ZF7idkFnsb8zDlrY4QFksLVVvTeIDvlL4gj-vrGo8_SvDC4bkLxROpNNTOOXRukS3QSEFBNN6tbB4A0sMAg80mY1EbsFig08Qsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba5d6f365.mp4?token=uxVuwyiSgmVNKw67AtNNLmCtgYKmk1S2-OrhrWbcfBBP9DG6fqvPZus4dc5oqGyD2M0eps3BL_KxQiZqQxHFWhd0WoLSyj-Wd2iagkaP27C7hmZDwZmWrJwevFl60IFbiKPnmUcUXcuYO8GfABJS1mTlD6ILpBb-hWmY7I15YSFBtG0ve9QMZUkPvkAFG0cZNodls0wnc9Mp7kxU5KLmcIUas8wkn44J70hxiN7ufOuWI9nyJW1ZF7idkFnsb8zDlrY4QFksLVVvTeIDvlL4gj-vrGo8_SvDC4bkLxROpNNTOOXRukS3QSEFBNN6tbB4A0sMAg80mY1EbsFig08Qsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
روزی روزگاری رئال مادرید در بازیای پیش فصل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102772" target="_blank">📅 16:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102771">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk0Ht8wM6WfATOrXKeCpJZgllY0nKBsd_p4-UvAjZfaIioq1II1DrQQvvJGN2ZACVcLdSGX3bi3z_O_9Wnrho2S6OiEasAuNzgIGLVRTCQH4xyAir9u5LVQ383PwEy6IkTXn3lqJMy79QQ7JVNydMWbY6f0WnbK4tSCS67KZzJmLVu9Sfd1ZJw5vJD-2aFlXlLsYCvOV7KG6lcJb7vpgEqhWvL4o9dBXOZDad72mkmeVDgrpd1dKMZb2FVnISe1BJ3T5Ksqe85fHO_NpYzaTf5za-6yDzYjMEXeBoNtVySz8AUxU7yTtdmUCkz6PM88-GMx5BLfDeIxCc3HqaN6tsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس در واکنش به هوادارای رئال که فریاد می‌زدن: "وینی، بمون"، با علامت
👍
بهشون پاسخ داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102771" target="_blank">📅 15:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102770">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0143fadc66.mp4?token=kA4ArFnMQ1xjcTINk57J1f6I8-1ruL9vGicxBNXSwQppyemjlQCEs0noT6zTY13s9bApnC5U0xl9FrlQgMqjg1HKdGAjaQJK7RSXwuZQ-TLtsNQAub_pTBDpXy8N1aHXqRVEXx6dvaofGiNSfGfMt2SyNG7GBYTmvm0iy1tOcIJj3yh0yBFKfD2KjHHoBjfMolXfwaqMZzgoX4j9XEWdnLyEBFzndTiMgPWRWUw3A-BcDZ_yQYS47RTfC4ea2ss6Bvb4yss3D45rsCQkyWxLMc6OszOuK-1JigNnzf1mqylGyP7T6-YQH_G0pF8sIBsBFNNEDOq1Jc5C34XKg8QL8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0143fadc66.mp4?token=kA4ArFnMQ1xjcTINk57J1f6I8-1ruL9vGicxBNXSwQppyemjlQCEs0noT6zTY13s9bApnC5U0xl9FrlQgMqjg1HKdGAjaQJK7RSXwuZQ-TLtsNQAub_pTBDpXy8N1aHXqRVEXx6dvaofGiNSfGfMt2SyNG7GBYTmvm0iy1tOcIJj3yh0yBFKfD2KjHHoBjfMolXfwaqMZzgoX4j9XEWdnLyEBFzndTiMgPWRWUw3A-BcDZ_yQYS47RTfC4ea2ss6Bvb4yss3D45rsCQkyWxLMc6OszOuK-1JigNnzf1mqylGyP7T6-YQH_G0pF8sIBsBFNNEDOq1Jc5C34XKg8QL8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی نیازی به تست دی‌ان‌ای نیست:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102770" target="_blank">📅 15:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102769">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7f8280c0.mp4?token=ecpluie9P2qKaIjbPJUJiMeq9WLsJay04m7qlMZUHNAmJyfnJ10LkkjsFzuoNc5DstvYducJXVnOAMe2hAUu3c6pctm3OLLJSzMLX6EOYD23kq6oBI6da4cDsoFPq8wQd_Qr9Lw8hwx96c6avyA0ojB5iGoixKcwwb3qAs9APp9XYaUPLWIyrhNek6fwuT6aw2IDy1E01YFM5D4gumk6L5foJCxeNg8At2Z5kR7Kfn2ozdPnBx0lCc0SX8d4sTsi3Fgy7r-TNyBmkjWNeZHBdnMYIYD4W2-Sm23mHBMfwEjvAPiwiykL2FXbq5EJD1XK8Tljn2pnFF-FEd-5ilYsrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7f8280c0.mp4?token=ecpluie9P2qKaIjbPJUJiMeq9WLsJay04m7qlMZUHNAmJyfnJ10LkkjsFzuoNc5DstvYducJXVnOAMe2hAUu3c6pctm3OLLJSzMLX6EOYD23kq6oBI6da4cDsoFPq8wQd_Qr9Lw8hwx96c6avyA0ojB5iGoixKcwwb3qAs9APp9XYaUPLWIyrhNek6fwuT6aw2IDy1E01YFM5D4gumk6L5foJCxeNg8At2Z5kR7Kfn2ozdPnBx0lCc0SX8d4sTsi3Fgy7r-TNyBmkjWNeZHBdnMYIYD4W2-Sm23mHBMfwEjvAPiwiykL2FXbq5EJD1XK8Tljn2pnFF-FEd-5ilYsrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ياسين‌چوکو بادیگارد لیونل‌مسی این‌روزها علاوه بر بدنسازی به تمرینات دروازه‌بانی مشغوله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102769" target="_blank">📅 15:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102768">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8597e812.mp4?token=k3CGNPUeck5vDil5gIQkr29ypV5JJsN33jfbFYsvaezIxORGUYVZucYhitGLe9mhW9uDcVbQcFtgiWKvnyBP6f6aS3ymX2O4DlYKPlklqjnGsyaK9XqKi5XFZZMLcbE0fGbBQErKojtVb-WKJLnnLrS4KPMXDV1QzJf2WrQUoOe6y7mgFE5xOnPT6CWI5AH-NMo2GtEpCHdh11rzHTxQK0chRPfQll3YTyF4B-b1J47HoE7Ns0GtxUju5JASi0qLri7KZDu4ic8JzdPrYirprh6Wz2kXdwB6YB8pZZKh64NOZ8oDdm01CfKanBgjaU0nMZ9eiwOUI8yZc_fqEwW-wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8597e812.mp4?token=k3CGNPUeck5vDil5gIQkr29ypV5JJsN33jfbFYsvaezIxORGUYVZucYhitGLe9mhW9uDcVbQcFtgiWKvnyBP6f6aS3ymX2O4DlYKPlklqjnGsyaK9XqKi5XFZZMLcbE0fGbBQErKojtVb-WKJLnnLrS4KPMXDV1QzJf2WrQUoOe6y7mgFE5xOnPT6CWI5AH-NMo2GtEpCHdh11rzHTxQK0chRPfQll3YTyF4B-b1J47HoE7Ns0GtxUju5JASi0qLri7KZDu4ic8JzdPrYirprh6Wz2kXdwB6YB8pZZKh64NOZ8oDdm01CfKanBgjaU0nMZ9eiwOUI8yZc_fqEwW-wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
▶️
#نوستالژی
؛ مروری بر آخرین تیم قهرمان پریمیرلیگ انگلیس لسترسیتی دوست‌داشتنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102768" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102767">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e70775585.mp4?token=WZVXZHT_eKpg6G_BIa1-75MwQbAaqj01ftioMIsXCXLNL5JKWQv2b9RMfUjXEbkQIhm8yP-hjLekigUdjf8Nc58iZt7-rDazq-YQBJ714yTeqHNKzMOAMM8yhJG31Djrc302fhGmaOheZzAqj34r0hBRbTj-xZbJ36L_jKJdImZaYDLNvo-cg1BYyIr3o9LgQf452gnFj8j-0BHwirHOgxLDtY7KyzNYA0tl5I3eENa00tFWKUgU5GGlVofgFYRljMYHAKhXiYb43VfTpUEyV1KQCE4TV2mok0Nye6ogRFr50iXeHpZdc_VWY4JAeSzC764laSQLW7bYDcOyTBu3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e70775585.mp4?token=WZVXZHT_eKpg6G_BIa1-75MwQbAaqj01ftioMIsXCXLNL5JKWQv2b9RMfUjXEbkQIhm8yP-hjLekigUdjf8Nc58iZt7-rDazq-YQBJ714yTeqHNKzMOAMM8yhJG31Djrc302fhGmaOheZzAqj34r0hBRbTj-xZbJ36L_jKJdImZaYDLNvo-cg1BYyIr3o9LgQf452gnFj8j-0BHwirHOgxLDtY7KyzNYA0tl5I3eENa00tFWKUgU5GGlVofgFYRljMYHAKhXiYb43VfTpUEyV1KQCE4TV2mok0Nye6ogRFr50iXeHpZdc_VWY4JAeSzC764laSQLW7bYDcOyTBu3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
خیلی از بازیکنای جوون دنبال اینن که سریع‌تر بدَوَن یا تکنیک بیشتری داشته باشن، ولی فوتبال سطح بالا بیشتر از هر چیزی به فکر کردن و تصمیم درست گرفتن توی زمان درست وابسته‌ست.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102767" target="_blank">📅 14:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102766">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ddc5f55ee.mp4?token=mhbbmVJ3yaiT2mbPoUa_Sp8Vf4tGmZHxvm6AxLonaqD_2geVFycbqs248xdQZoxujCuLoJwnSsyQucIlZBbeNWJ0OXBfakdTMNCHYETh4cQuhJxgkIDOL-QrcN2MmZuNieNVJ5v3uaRkkEvXAMp38D2yW4r6BOUR-KfaIMIFBz7nDO5EJY8dxx2TE3a4bwGVDHtRbX_y2mJl4FWLK4mIE1KxWkdAYLoC8I_sq6HaAeavHQLsahZflHYA_7W5VXQF_1Op8q8-iaZy6ZSqo152s3kvIaFdwifAdxDWhqZVVSHnrCes4M3sX41PyWTF-zDMNT9NKgV_h3UkN7cgX2k5Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ddc5f55ee.mp4?token=mhbbmVJ3yaiT2mbPoUa_Sp8Vf4tGmZHxvm6AxLonaqD_2geVFycbqs248xdQZoxujCuLoJwnSsyQucIlZBbeNWJ0OXBfakdTMNCHYETh4cQuhJxgkIDOL-QrcN2MmZuNieNVJ5v3uaRkkEvXAMp38D2yW4r6BOUR-KfaIMIFBz7nDO5EJY8dxx2TE3a4bwGVDHtRbX_y2mJl4FWLK4mIE1KxWkdAYLoC8I_sq6HaAeavHQLsahZflHYA_7W5VXQF_1Op8q8-iaZy6ZSqo152s3kvIaFdwifAdxDWhqZVVSHnrCes4M3sX41PyWTF-zDMNT9NKgV_h3UkN7cgX2k5Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
وقتی میراث فرگوسن نابود می‌شود :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102766" target="_blank">📅 14:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102765">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWLVSjpY8R-fTH6MeBdDzPG-8uswfQGLKQ8Z0e7TooU3YRSZ1t_Z70XRwZMrdA81nsWn5J3362sgaNHM0dtW1Cv2lH2b3nqg2jAYq1sxCQddG54v1D8y_jlOvzk5L-f8DHYTMbFxbF648C0fZo1oo_XY6jJ7ivIx2xCDx43i8lWDRbxSin-iwp_M_VeUUoVW_O0UokA1TMemUXsnS4k-wicT2CZxfTrin9dDkzUlauX9DCXsIKfhuBBi8o4fvND4HffCQW8RpRuzmCpMLYu8_WTrohFU-nNrT_6kpETk_WmPFFlGBAsiQZ0HmQ9nLda9mhRVoYPbU6LkAUPwimmOLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔴
7 سال پیش تو چنین روزی کینگ هری مگوایر اسطوره فوتبال انگلیس با 80 میلیون پوند به منچستریونایتد پیوست و تبدیل به گرون قیمت ترین مدافع تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102765" target="_blank">📅 13:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102764">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctDVQIuEVBf9PpBHSqIwcXZzfdnb5XndiO59QEDaryP165XTkxldn7AlccIjhYiittBsVGpkybOWV6FI2RaswmlSLLaaHVISCRG8eOmf9hnQJtSLLtoM0BwJ9rPiEnJExbzOGAj7vkqhQnVk8qmmIoQvbnmCSkK0Ed9BLOlL9uPWzVWyaC9xu9hDGNnC6_hW51twvfTtaNRKqn8vZPSqXuZgcpJrccjrIk3t46DL_Lis_zuctiVnFayXMQnfqZlfx6Svv13PNSoti_8B52Pi8bzUq97SSX-KkZoQneenbfjk_jT6b5sfhYnmyYJHfURKqAOZBHOpUWepRWWsqllxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102764" target="_blank">📅 13:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102762">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0EFZeN3xeLeUGJdDzn8tLmoMj1drgpK-Kmu-HXgg6wOePobzMGQhQeuGTNLQEs7J9ksuQB59Nuc8w09uMvCncWDprDvlHI2nKb5v1EQtAYJqa8npeG042epiMzkKiMDxlfSMzOMeW2Xz6eLH7MIUyRLUivA16GFEjkeK3jet328IVExHga83WhzPSb8-nc1xtGKIcyJflf6PgwZDFsHbQygvW7SRoAKsIAFJDoDmBMwIQ1G3VHd-Gy9p4-5G2Xxlpa1do0f27CyTvzBQm6qcrONC1kYubeT_07-8CGSPqirQX61kO7DjO0fi84NNHErIpR8lngkdeQMv0WEhcjT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه که بدونید فصل گذشته
فران تورس لورد بزرگ ۱۵ بازی پیاپی رو بدون گلزنی پشت سر گذاشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102762" target="_blank">📅 13:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102761">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=giqdvrCi45rWauSNLB2Z_AVztO6T0_kov6ve_pr1QvBkwoIpTV4UvgnAZed79y7KgXG8FPmrTwaR_Xdlwz0Es3HVr4tQNEdPMDLvAV85E8Hw8wbkyvDkadPKj_eulK5I-MPorwhT4TC2ZJva7e6be-d0GHp9O_kdDmy0sTwoLIsguLkimgRMEDWlhAva6bzEhof-ht9JkveQ4lFEPslavDUrLVuH_XSn-G3RxzezFpEEQCNeRxwzvxa5hknpeGIH4yKnqQyAInTTIsRXJv2R-qp2XI-xNHMwsy5mKzzu9XkxG9-UsIx9o6TehAS88BMuVLE0MdE6E3LpK1WF8u3vuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=giqdvrCi45rWauSNLB2Z_AVztO6T0_kov6ve_pr1QvBkwoIpTV4UvgnAZed79y7KgXG8FPmrTwaR_Xdlwz0Es3HVr4tQNEdPMDLvAV85E8Hw8wbkyvDkadPKj_eulK5I-MPorwhT4TC2ZJva7e6be-d0GHp9O_kdDmy0sTwoLIsguLkimgRMEDWlhAva6bzEhof-ht9JkveQ4lFEPslavDUrLVuH_XSn-G3RxzezFpEEQCNeRxwzvxa5hknpeGIH4yKnqQyAInTTIsRXJv2R-qp2XI-xNHMwsy5mKzzu9XkxG9-UsIx9o6TehAS88BMuVLE0MdE6E3LpK1WF8u3vuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
😐
⚠️
ارتش‌روسیه دیروز با پهپاد یه سبزی‌فروش اوکراینی‌رو تار و مار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102761" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102760">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkYjwiq0J5LPSPOdGRTa26jMTjxNR4AEasVyFHPu5FkvzG0QyhTgaAx0c5y3TiRGi--GIMyy4DcOm7tOrrNMfJzwsFjQntfpWLzF0d0cc4TRfi51cIaxoBevwVWM9G-orfDGvo_GamIxiDkby-hHcT2E98N2eKX9OAsqanW9zwBUhDyUnknzfibflz58WAiDgz6a_owDBcxQrGp-_GzZpvity7wSK-sl3Ai9BFJs02guUSfRShtukk9PtNejvljHXAz2peBawFBGmt8gDlQ9rNSc8kVAz5EHryipIoqnXYEQpuVPqVdXxWQTyEJuWYou_XEeBS7k7xSrW7pFLbgjMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102760" target="_blank">📅 13:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102759">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPujSNbe-ZyZYG-4f6FMpP9RbMWS4xCOXtY_-_pOr6OTJ4iFLyUFPb7vBF1alcX6plDOzA6XfRuAH8qIfrKFgNyEBhrObeCpytarQZOg7y5yKgYS4Svu1OqflenYGLRpqGPQeEMxW1XIq5PUt9YFjgLNtPBqwamVw207kepcWsvS8kXk5H10KHJqVGKG5k3xu82L-LFOIhAjYfFNfDEngWh3QIswAAnsGLnmz1W7kmZVxavxXo0QkTi2dnO_wpvnkXc4ge7bjuZRzoR351SU_8Mc4QVUMULTXCXX3BmLB_nT4zQSGjSeyF20bTy-5ekvk_UUKDPzXZhWXWWesqv_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
بازی‌دوستانه؛ ترکیب منچسترسیتی مقابل منتخب ستارگان لیگ‌کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102759" target="_blank">📅 13:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102758">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfQTDFqT15Iab5cY22cCWv8Rqz39gGqEniLvnsQwiTH5ZJlV4jEpnlfBxaL8lKrrYVOu7gEc-5h6y71mHYYSGOe3yC6KhtSL7rugBm1oylQ4MdsLglMjjhyco3V5Y5sGYE_F3a1gWA3lwu9mnw69WPWjUb20gN0lQi6Ideinl1cYiJNR2tURQj5Lu6yM9OXfIyeRa5m8HhM9EJqVt4d2mp8iyhSmP8d-HVuo3CWvZikqNwSNNvdDEdl56wa01VNtMEL4pznMpVuGpNKePEjIs6I3twpTSAOo6VbN9h8zjJKro8A9iy5IIPSboLSKOfaNbEX-O5nLm8JFILVvNAGcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
متئو مورتو: جاشوآ زیرکزی بازیکن شیاطین‌سرخ در آستانه انتقال به یوونتوس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102758" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102757">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=jiM9kaKS-SbMZj-YuhZDE-qu1qWRANrkYKDgDqOmNWZXleGVTB33ClS8zR0RwnSHyTamMt2QXHH7lz__ZXYOCO2tCQaX2Umg11i8aG3631cI3M7BJndotBUNs-UbAxxAyTXnUehaHqWZ4mIspAfaJzwvQRR0tFmtuoqXfZK_pxGVJq6b8sCCEsQOyh1HDDFFGy04ORozAPnWbCI3epQ3wzkaJLZ_5v1aRXg8Z-WNxZ-8xEeSdDok8uy3L9U0Pstp9Q1N-jB7gWSepR9VwjsrAgKmXDydaDry5PsOjRl3-BflDzZ7NNGl76TKR4F8GnzH06qw7HSAwYIOusZG3nQcEZyGm3TrQ8cxylB72ir_FiaN7AzNAEG9CiwtgR2MELUNLPPS6xdeki3EHM2vZ759-I7s1KFFHmv5bLxa8QbzO53KZ3br5QbS-KxOZ5yk3mRIjJvMCeDxeuuR11m7EMpwujwxvvfxseUhJE_2SzS8hLUEb8xxVDBTM_mcrXLr4pe44OFjsU-fvleoO2U7JMz3geUT6X0Y_EsiD7UR8j0fD0yYh867E2eNxdYJGkLy5Gz15a-ZfPdlWW9cMKJ-dm6ccwUBY0ArJ9ecJIA-eM6FrEnA9R4c72W3XDx9VnUTsWl097DHxAWJ8rfk7AUmOKFo9alE_e0jxD7TQbAapgQeLic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=jiM9kaKS-SbMZj-YuhZDE-qu1qWRANrkYKDgDqOmNWZXleGVTB33ClS8zR0RwnSHyTamMt2QXHH7lz__ZXYOCO2tCQaX2Umg11i8aG3631cI3M7BJndotBUNs-UbAxxAyTXnUehaHqWZ4mIspAfaJzwvQRR0tFmtuoqXfZK_pxGVJq6b8sCCEsQOyh1HDDFFGy04ORozAPnWbCI3epQ3wzkaJLZ_5v1aRXg8Z-WNxZ-8xEeSdDok8uy3L9U0Pstp9Q1N-jB7gWSepR9VwjsrAgKmXDydaDry5PsOjRl3-BflDzZ7NNGl76TKR4F8GnzH06qw7HSAwYIOusZG3nQcEZyGm3TrQ8cxylB72ir_FiaN7AzNAEG9CiwtgR2MELUNLPPS6xdeki3EHM2vZ759-I7s1KFFHmv5bLxa8QbzO53KZ3br5QbS-KxOZ5yk3mRIjJvMCeDxeuuR11m7EMpwujwxvvfxseUhJE_2SzS8hLUEb8xxVDBTM_mcrXLr4pe44OFjsU-fvleoO2U7JMz3geUT6X0Y_EsiD7UR8j0fD0yYh867E2eNxdYJGkLy5Gz15a-ZfPdlWW9cMKJ-dm6ccwUBY0ArJ9ecJIA-eM6FrEnA9R4c72W3XDx9VnUTsWl097DHxAWJ8rfk7AUmOKFo9alE_e0jxD7TQbAapgQeLic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚽️
روایتی از تحقیرآمیز‌ترین گل‌تاریخ‌فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102757" target="_blank">📅 13:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102756">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=EU59GdjGxsj8YiGPmTaukec9NMvYTIqXchca_VBsd10Clc_YeKRn20DWUbl8u0vyPCo3xVEg5UtnDxhkEIgPxBK2HuKV97kQtj05sN6ocdArrx6AaPGw1efyH2o8vGzh5U6FgkDMMavV7xSCKnZfjDcXVTLWNXsMtyj5pOKUE4xZPeuXf37EF-iNhfDU5YRRPW2FOsWyTPW_UcdWdvcVSTSftRy0sibZw45sXx3xXttcgLZnevy4hrYqaFqAh0u4AvM_Bdf3ShejWc-Ti76065JKrfpVJX_Vz70IgB-KCx_AR__KaPIU25McoPc7alPLZ-iy7FcEDqzNseQNUkYX3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=EU59GdjGxsj8YiGPmTaukec9NMvYTIqXchca_VBsd10Clc_YeKRn20DWUbl8u0vyPCo3xVEg5UtnDxhkEIgPxBK2HuKV97kQtj05sN6ocdArrx6AaPGw1efyH2o8vGzh5U6FgkDMMavV7xSCKnZfjDcXVTLWNXsMtyj5pOKUE4xZPeuXf37EF-iNhfDU5YRRPW2FOsWyTPW_UcdWdvcVSTSftRy0sibZw45sXx3xXttcgLZnevy4hrYqaFqAh0u4AvM_Bdf3ShejWc-Ti76065JKrfpVJX_Vz70IgB-KCx_AR__KaPIU25McoPc7alPLZ-iy7FcEDqzNseQNUkYX3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
تحول تاکتیکی تماشایی انریکه در پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102756" target="_blank">📅 12:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102755">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=IXhTjpL7yQhDIZI7tkgvpYM_DbKkwKOWYXWPO0-y2pkwruWf9oDlKSmC5ztB48c7NQouqPpPBmFPb_3SQy5ax-E9Us213SCiqxlivYpT1_KypTN9k7l1awwmUHVZg6nx63wjqiFGhYc68UQrozlDp5Bz5M_Zzkoxpop_A9qvrd7SUyW79nKOtP33fFxhTb0sNLrPZqq72oI2Yy4314H9yTXrV2AJBeiNOQuvuTJ-Dvzs3bxYKNbYoGiVR30MA1g52WmD6x_I2-x3Dr7dnmGUJbCJaMjIbMFhJDEmKLQNQHC1rvSsGczV8Uyh6wM_6nO3AndQOCyRs6B4Ccm7Mt0-vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=IXhTjpL7yQhDIZI7tkgvpYM_DbKkwKOWYXWPO0-y2pkwruWf9oDlKSmC5ztB48c7NQouqPpPBmFPb_3SQy5ax-E9Us213SCiqxlivYpT1_KypTN9k7l1awwmUHVZg6nx63wjqiFGhYc68UQrozlDp5Bz5M_Zzkoxpop_A9qvrd7SUyW79nKOtP33fFxhTb0sNLrPZqq72oI2Yy4314H9yTXrV2AJBeiNOQuvuTJ-Dvzs3bxYKNbYoGiVR30MA1g52WmD6x_I2-x3Dr7dnmGUJbCJaMjIbMFhJDEmKLQNQHC1rvSsGczV8Uyh6wM_6nO3AndQOCyRs6B4Ccm7Mt0-vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇺🇦
آردا توران در تمرینات شاختار اوکراین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102755" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102754">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960818b54d.mp4?token=QAJnwp2NXYb4Roii-d1xrjck8tRPiNTXihun35cQfnnpK7ED7FuRsYYeOL1YRnHTNGwKIY56n3IlCsdm0dpvgElJ_wcKZ5xI7gwSwEwC8dUr3ivx8EMPGArem-QbfzRoMYJSF8_eW31p4DY1gydMpHkxtH7FUjj0Z2Cplhj-m0D8OlV2fkvMwQTgnvtj20PBqWeUywMcOCz21ZTLpDzn9pntRRF3KkNcdGJ6qWRn1QNKSCBeBjAeO15mlEmXVjeBDYYo6udnl67go6gJuPfeOFs5-k8OWSD7bEhXvE4QZwaS3gbB5WbpA6VLMan97mXqvwRaFklWYjOM22aRk1WW1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960818b54d.mp4?token=QAJnwp2NXYb4Roii-d1xrjck8tRPiNTXihun35cQfnnpK7ED7FuRsYYeOL1YRnHTNGwKIY56n3IlCsdm0dpvgElJ_wcKZ5xI7gwSwEwC8dUr3ivx8EMPGArem-QbfzRoMYJSF8_eW31p4DY1gydMpHkxtH7FUjj0Z2Cplhj-m0D8OlV2fkvMwQTgnvtj20PBqWeUywMcOCz21ZTLpDzn9pntRRF3KkNcdGJ6qWRn1QNKSCBeBjAeO15mlEmXVjeBDYYo6udnl67go6gJuPfeOFs5-k8OWSD7bEhXvE4QZwaS3gbB5WbpA6VLMan97mXqvwRaFklWYjOM22aRk1WW1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بنده خدا احسان علیخانی خوب مچ میثاقی رو گرفت قبل اینکه بخواد علیه عادل کودتا کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102754" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102753">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpSa68N18Ni385jC-I9XFsK93hsPVoO9mwOxYwsCdsJC-MSeoQzGi8MIem5yOqlMEo2zTb9daJhEJlQizfQriG22oadLWFh_NbVH39c4i_1AtDeEGMj7lT8_GEbUCIEEfNvjHyCFAgzmQ9kyqfO7l3IzsaynTnHPschNzFFnXkfwP6Pg65ppqpnwqyteBPjQKvIHzrc6AkfSaSUn-uya96pldEhvvapbFkrYdWHxL8vEHwt1lWNK2eFtksyhH_JYZXAuPFkq3GEStZ7j7r-AubdgyfHBq_tM2bVoGEC5jLS8nBWk_LKD6ydRbwn9Z1xu1XPeVRhww730xaFMB142Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
بازگشت دیومانده به کمپ‌تمرینی لایپزیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102753" target="_blank">📅 12:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102752">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF7jA_Dri-rABMwaaREtZH4-i-TRJsArb1LcAyrVemQi4VgQ4KDS50D7w2j9gx7DY7avEUd2MRpE-c3Hway-S5ze4O6fydr1pxP4wB-JrM43KXzPiR1E-QvIHlAQD3yx913LLzNlnUURN5NVIi5nl7DQKNvLYwl0xmapMb8SP-GMn1tbUvp3IebrX_oqyQPBwbM92MXihY_VDK6-IhlQ7L8HkGIOFWvNeMpzLsMx3_LBUigR6qLUzCIFhdJme1Y6wFXcnanrZTH6fLZARbuoP5FHvlmHXH86iC2UASshp36_ZXIFbUjEyD3MHVVbL0DJf8dFA_tPtHP7VJddOukMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
با اعلام رومانو، ماستانتانو بازیکن رئال‌مادرید با قراردادی قرضی راهی فیورنتینا شد
Here We Go
✅
✅
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102752" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102751">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co_13zn0NENMR1Tj6xFSFyuZkzkUpot-bkeZ23kZtOhp9MtXEMgp54oeeJlQ4sZ6zOi__3VmDdazlCLs3Upmlai01t95wjswAIg4UlOid2SSm6OYXqJTuTqjl81G6XOl6mkkEdED07DpeJwyw75WQ5aa61MHyPLw-RqoRa1qDxafCqmLpCB3j2cgpPDs7fAVwc58AAUPyjboiiyuyvKiew5GCK2kDD-eH5pPAmSg8mmkZ-SqBvbts0GM7vsgJcsVHIOXxhbTURegxNBicxP8FcwltOi753tHN9FNuwGvzMO4XyB6wsKq7dwd8ZhBg-ijJoCdx9eRAGgQZnxW1U7qvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامین رضاییان رسما از استقلال جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102751" target="_blank">📅 12:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102747">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YL5lan6UvaTHgo1s148G7UJZ7HeUmuYA1tNlT3maxCmQRAdrWE46EN-pVroSzxc9LZQ_0UAvvQ13zaqHMlDBGhnRu5nO3SfqigM2Dnf5eTc2iUV5MhIWR0HqdBQh5Rn8ttbwTGqLrIT_B7u9xA2PnHCjZU0yT83KEHbz4In3-ulORI_jcUAcQW83GS50lITXPlwXP9562lTp3J9V3VMimmaBcHUZVdQ-FBQW5EJ92sN5-P-Hy19W-JDT6BgJgE8dFcA6TOy0r0G1mIQQpKjY-4SUcsaGXxw-kLmreS9pl2bvPxGYdYACUuEMdSWVZiFrb0SI9qFm509fkQ_qkHb7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sii5pMjVrHeo5GNFhB8BXbgQ6gcAdOzMLgquI9_fm4vPxkQB_yRTVfupEcBqHIMxRFkTco0KhhlCnzUc4Bn2-CV-WY6yZQdy4zhz4KO7pwOS-Fd15MBCZWrX8uC7QPtqdqT46U5TmFwExdIAU-SEjiIwhBK3qxVBFpbmvXGLtE2Asb5SM9ECujExdjirIvZ69YfpkDjgnE6h0SQR4nXqHm5g1JCMpZUR-xeJqMJjeaVvUHI6YYgZLO7prYhsrkqiWULVcqVN3wBwKPRKP-k5awzjLxPvntgbTEgtY4KduYWbCuqRFrBxAFXzjkEKaizXI9QmyQR9q6EL3vIQkRVJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqYmCAp5ni6ukfeB-94lFL-lnX6QhMIwFY-bcI16UIkweNo42cNc8mlkBbIIeH6oOpuy4OHDYL6r80g0ry2pF8PHvBdbU5Igh0R-z-_24c6yjfbp-FOuYehX8qTi3bnWP9fUFd9939YPmBkvUtV92hCWqGYSmTJIVkXvhJv82N2i3flDzfAX0_9B_bgX6Cnwo69O9Sdi4NX0viu7eqHGe4gXG7HncWkZhBEcVpe1uxPY1ow0jDVGthd6UxO5bHdBbR1V7KtMyWTvlO--vM6HOeb-fGLzc-2yQFX2XvX29by-ZTddef79_OMeqV1OLqnEClS3vBpRiwd74nA1uTdP-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d56wTIX-rWPEewTFbPyxpsXA19ff3_qgosvS5lpmWG9f1WXAXQVdZUJcb4U6wFczREpvJsafVki_7iZRdtWCD1vSfMx467BdEWyLSeY9EmcrnhG1bB4GDFwaIg-PgKTEOu6hZINTZKM8Ob2-VhF-cNLqaknloK4u9f_5Nhs00iexiqzZHTyCdWgDnyvaRF-7h7Kr298Bv3PkPhbEZdcVmO7JyvIE4Fj6Uxc_exQueOxPX_CHIny4pdTHoYwytgtWMEXrdFsXyhT4J4ul4hxwmoNQFcslkntsWN-IFhNN0pIp_we7SnDkBCklt1uziqAP0KYpSVN2qsQLioirpXvKdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔺
تیم کومو 7 سال پیش تو دسته چهارم فوتبال ایتالیا بازی میکرد و حالا به لطف نتایج درخشان با سرمربیگری سسک فابرگاس اونا فصل آینده یکی از تیم‌های حاضر تو چمپیونزلیگ هستن.
🔺
جالبه بدونید مجموع ارزش کومو تو ترانسفر مارکت تو فصل 2019/2020، 2.4 میلیون یورو بود و الان به 489 میلیون یورو افزایش یافته
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102747" target="_blank">📅 12:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102746">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c832d40c29.mp4?token=CdPZtuUiHtjcU0Se74MsqTFrN_9wuE4mO240e-zy4xj0o7sm3nF-FR6x5kw73Vdwa59VILu53U8cFbOlsxBlMdWr_J5JXJl0WraqYGRm0nvUMAXj4dZm9W6TrKaarthux-KS-OU17qwjxY1qY7ZFY2QPHz_Hcgs53sb9T7JbGRFF5S31NIo0W9sSTgThIdLL3U2RJ2Q68YabJrmCVph3IM5gZV9eq-Wi74FL5gQIfIa0JXiTXkS9jR8MZzsh4vtECL68poDmRNjg5FGVFdYGMz76onfwbMnfHttkN1RfTiLaW7Bw2v6x6GogAVXWwAzNI6bICSVgBDU25Keng0tdYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c832d40c29.mp4?token=CdPZtuUiHtjcU0Se74MsqTFrN_9wuE4mO240e-zy4xj0o7sm3nF-FR6x5kw73Vdwa59VILu53U8cFbOlsxBlMdWr_J5JXJl0WraqYGRm0nvUMAXj4dZm9W6TrKaarthux-KS-OU17qwjxY1qY7ZFY2QPHz_Hcgs53sb9T7JbGRFF5S31NIo0W9sSTgThIdLL3U2RJ2Q68YabJrmCVph3IM5gZV9eq-Wi74FL5gQIfIa0JXiTXkS9jR8MZzsh4vtECL68poDmRNjg5FGVFdYGMz76onfwbMnfHttkN1RfTiLaW7Bw2v6x6GogAVXWwAzNI6bICSVgBDU25Keng0tdYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
✅
رونمایی رسمی باشگاه ترابزون‌اسپور از صلاح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102746" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102745">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ace4b7d7.mp4?token=VanuIwCO30UHezWf-xQQrwbejrr9ei77rH_Ee3Ilgy12RBHi0gKUlBSb8MT9pkPbwuLxpckt9vjW4YV7p3x-cuZWkUOV_M0Ko6HNdZIvB7UodnzPXz-rEuUxeMBmJt5riQzMDQUEdulGadEb6fr_C648fIof2BOYbUHS5xuJlMXZL5F3hQD5KdHYncUz5sfQT2gutGs09iVruVCV48vMWsuLMFzX9oMmhjLo6PT_FA7D6cgR70IMItuM9DtArEycT-1rRAlk86QHPm5WcwYTDOhrcoUMozYJMkbydSwTK1PgOWh4UBZKx9DBA_-OSJrGghsjxysk7LHqioQkd9i-tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ace4b7d7.mp4?token=VanuIwCO30UHezWf-xQQrwbejrr9ei77rH_Ee3Ilgy12RBHi0gKUlBSb8MT9pkPbwuLxpckt9vjW4YV7p3x-cuZWkUOV_M0Ko6HNdZIvB7UodnzPXz-rEuUxeMBmJt5riQzMDQUEdulGadEb6fr_C648fIof2BOYbUHS5xuJlMXZL5F3hQD5KdHYncUz5sfQT2gutGs09iVruVCV48vMWsuLMFzX9oMmhjLo6PT_FA7D6cgR70IMItuM9DtArEycT-1rRAlk86QHPm5WcwYTDOhrcoUMozYJMkbydSwTK1PgOWh4UBZKx9DBA_-OSJrGghsjxysk7LHqioQkd9i-tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با این وزن و هیکلش یه حرکتی کرد که واسه نصف بازیکنای لیگ مملکت قفله:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102745" target="_blank">📅 11:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102744">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c80f4ab4.mp4?token=rLtkbUrakU4AZKNshZ5f3RpnB6nArGXUM6FvnzKywDPEctWZXRCRrxBonM_oUCe6GVoqIShNL_2MSYyw7Gdeu8e4sfRmjlMQ6LNXcXHgmYddcwFTN1fe1_a4UT1ProB3-08ej8V-aVCkkw6NDi81WpjdI_kj2uPrScOvEXn_wHvwSoimB83_m1RhMtqeZ9VLqN15L5vIhWbh_d0KiuQIHev83CxN4C85e9HjlrGDMPIsZEApiIyAE7lxN-HCvNDyWfrm6zcrTUNuAYTAfWsouYuzt61PP0rk5nlYG8XqbR54YLHyjfpQZD0TDn8408JKsR4Si1eBucwHe0rhAocWcgxfao7r5GzxsxAyi5UWkDSCwxBiPv_X3E4l3kFu10a4GoSHk8weGy0tGyjCCecCWoC2KaiaqohqKN2NYwiIUEvACPbwHHJhKQmJiaFreTSHSD2b1QEpXMLAqv4nvGPe2QqetSQcZpiS5or2Hkv5pykn_NuWcVf4bgRnmAd_v31pNDNp-uaLzFZzi5YmYmfFC6A2C1ymke6xo-MtjBc8O98jNkYH4oteuuDkCMDr9zgErJQJPsgHp-43xt-6Yhl4Hd9TKn_g0RbndtWH79uxsN9MEcVLJdg76RMGS6C6M_XKJdPuSclEyXe_3muzUyPjrrU5k1owFo0TSCZCKknzQos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c80f4ab4.mp4?token=rLtkbUrakU4AZKNshZ5f3RpnB6nArGXUM6FvnzKywDPEctWZXRCRrxBonM_oUCe6GVoqIShNL_2MSYyw7Gdeu8e4sfRmjlMQ6LNXcXHgmYddcwFTN1fe1_a4UT1ProB3-08ej8V-aVCkkw6NDi81WpjdI_kj2uPrScOvEXn_wHvwSoimB83_m1RhMtqeZ9VLqN15L5vIhWbh_d0KiuQIHev83CxN4C85e9HjlrGDMPIsZEApiIyAE7lxN-HCvNDyWfrm6zcrTUNuAYTAfWsouYuzt61PP0rk5nlYG8XqbR54YLHyjfpQZD0TDn8408JKsR4Si1eBucwHe0rhAocWcgxfao7r5GzxsxAyi5UWkDSCwxBiPv_X3E4l3kFu10a4GoSHk8weGy0tGyjCCecCWoC2KaiaqohqKN2NYwiIUEvACPbwHHJhKQmJiaFreTSHSD2b1QEpXMLAqv4nvGPe2QqetSQcZpiS5or2Hkv5pykn_NuWcVf4bgRnmAd_v31pNDNp-uaLzFZzi5YmYmfFC6A2C1ymke6xo-MtjBc8O98jNkYH4oteuuDkCMDr9zgErJQJPsgHp-43xt-6Yhl4Hd9TKn_g0RbndtWH79uxsN9MEcVLJdg76RMGS6C6M_XKJdPuSclEyXe_3muzUyPjrrU5k1owFo0TSCZCKknzQos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚽️
⚽️
روزی که لیونل‌مسی به مورینیو در الکلاسیکو درس فوتبال یاد داد و پاسخ تمسخر سرمربی رئال‌مادرید رو با درخشش فوق‌العاده‌ داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102744" target="_blank">📅 11:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102743">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از رومانو: برونو گیمارش با عقد قراردادی راهی آرسنال شد   HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102743" target="_blank">📅 10:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102742">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5hCqh6hweY2ROIYdQKKh60oRPP5qxThc56eESm1INiJgq3tYeD7oLFTzYVJGD17ihtxZKER3UsUQDHj1IZAwtXJ5U_sxTbg26vdVRS2FaW6hVDYM9s0lQnyw1I2sDJ2vNWFAfEqpgMRLsgMzYKRB3xgKab_OkZU9BuUps-HA17CaWebSQ_s7vo089re3ZnlFmfEKhaVtINzePm-ZfGAqnSEDAZSk_9fadWfB4Gga7aIHT9V6GdItEFEC5FP_XqKG8r5DojRU3SN0lZqmDVsFjGPhKMahiAFNHQbvSl5ZoQnZTgeBq-zqOuntylB_OabGD61_qrubLmMCH7_enpDqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: برونو گیمارش با عقد قراردادی راهی آرسنال شد
HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102742" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102741">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2e64a450.mp4?token=mxXnIw23c4QuXeQy4QSL5SdI-5ChX4SWg5wKNFq00haNrAZVwk4N5l5LvYWXrLNfZNrhAYoToUh_AXYz9r7Qp3avRCYs2aIP7lgVsaQkv4ToGG3ernEdSySxFM3-reCp1dx5DIdnYSIdCxcb8_G341cFWIuNkAGwNNbDRhnIs4K2PohstYwjaR2yCoY48wmO5jPbT_L2vmkC0XOQBaKQolG8p-HPdtsYIZKmn0AR7yUfmasykNjfFqkWeQQAcHlF8lcf1MSbkSZEnd6juGp3GnY3hQd2Uz8F8bC3ZQqmCHBYy8sdNLmEmmwH1xHfAZ-5sbHC7m3B_23Rsr2ZPTckCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2e64a450.mp4?token=mxXnIw23c4QuXeQy4QSL5SdI-5ChX4SWg5wKNFq00haNrAZVwk4N5l5LvYWXrLNfZNrhAYoToUh_AXYz9r7Qp3avRCYs2aIP7lgVsaQkv4ToGG3ernEdSySxFM3-reCp1dx5DIdnYSIdCxcb8_G341cFWIuNkAGwNNbDRhnIs4K2PohstYwjaR2yCoY48wmO5jPbT_L2vmkC0XOQBaKQolG8p-HPdtsYIZKmn0AR7yUfmasykNjfFqkWeQQAcHlF8lcf1MSbkSZEnd6juGp3GnY3hQd2Uz8F8bC3ZQqmCHBYy8sdNLmEmmwH1xHfAZ-5sbHC7m3B_23Rsr2ZPTckCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
▶️
تیزر دیدنی ترابوزان‌اسپور برای محمدصلاح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102741" target="_blank">📅 10:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102740">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op_TosdOOSN4vP8WV__uBjUE-z96cT7J-uZpgKa9_X87Sm2ekc-bYL_0n-SO9fmwIUZHmhzV4dM-blHh7RUm4ecAA1l468z3-ZandS5FrvXCY35Q7s4yWMU-qq_txT7CEwQ0FrGJHvYsEjBHgUkB_Fz4i0GJiZvhnmZJ85FwKe0abe2TKNT6t7hYn3B9bIiXv11ZNd3qNgFV_tEc1WPBLRPOKTGPppxZ1nPMhKrUyQ7jqHYA4dmiizUJdz5K6MQ1T_hzAqmvyr-NCPQFcAUXKCisoKPbcglosVYFBbzBsuS2ER2ndw8lliF0LjH6h1lklQMaDiimnivKUsMKGmKdIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ وینیسیوس و وکلاش برای مذاکره با رئال‌مادرید وارد کمپ این تیم شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102740" target="_blank">📅 10:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102739">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d431d3ca7.mp4?token=gJVLkwOhndoFKZnDa_5Mve5NGebeH_RFb7Zs80fBUBAt6ZZzdoTnyGfOE3mdMUVQSG8Gy8zYMusxoNSZPvxdU4IkPK67bebTWTZ3HbUrhQHODDkGml83YoBySL9Ir1e69a5bWkvTxFyQmONlaa-2lxkVJHtAGIO8D93LjwMo9VhNjCRn9Y5gHlWFf3lCPKhad9QdxifvxuWev_zKjP4cZPE47BT02lefRdXaThtSu5jNHaf6jvGlMeRNuvWBwpJV1Q9UUvuHEanFrgOrPKlSs2atD_cMKHd6XVONKAU7Q3rcS4e4-bwrgbsN5KQL7TNd1_AUugf3CLL1Cj9se3f0c6AXZ-im2fcfja2midlPlXRqQxjuZBfr_CDOBY6Do8bH8UrrrriEBoDj0-evHx1jQHTnW6G0t0z1iN61cd5OzbbcQUqI8RdkxLXiiNp-s6On-3tbT1FuRlgK31lG2IslTuiwp-un2ZoUbYxvNsRu9y8UOqhJFP7Eih7k4MII7ZICjmNvnlJ1XOVLXcGXGco2P2QM1mOSOF1GyACkbWF6sQnABHopmeyu_OUVA2DEXGSRJJkJymRu2hBifKn90y2MQXZ6gi7Avmkk5WoT7OIyfz8PfKo1lmLrFUQNP6jJRa-Nx9YWHUm_ZPrBbr4v7fZLt16T1Exlxz03bzzqzfLkbnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d431d3ca7.mp4?token=gJVLkwOhndoFKZnDa_5Mve5NGebeH_RFb7Zs80fBUBAt6ZZzdoTnyGfOE3mdMUVQSG8Gy8zYMusxoNSZPvxdU4IkPK67bebTWTZ3HbUrhQHODDkGml83YoBySL9Ir1e69a5bWkvTxFyQmONlaa-2lxkVJHtAGIO8D93LjwMo9VhNjCRn9Y5gHlWFf3lCPKhad9QdxifvxuWev_zKjP4cZPE47BT02lefRdXaThtSu5jNHaf6jvGlMeRNuvWBwpJV1Q9UUvuHEanFrgOrPKlSs2atD_cMKHd6XVONKAU7Q3rcS4e4-bwrgbsN5KQL7TNd1_AUugf3CLL1Cj9se3f0c6AXZ-im2fcfja2midlPlXRqQxjuZBfr_CDOBY6Do8bH8UrrrriEBoDj0-evHx1jQHTnW6G0t0z1iN61cd5OzbbcQUqI8RdkxLXiiNp-s6On-3tbT1FuRlgK31lG2IslTuiwp-un2ZoUbYxvNsRu9y8UOqhJFP7Eih7k4MII7ZICjmNvnlJ1XOVLXcGXGco2P2QM1mOSOF1GyACkbWF6sQnABHopmeyu_OUVA2DEXGSRJJkJymRu2hBifKn90y2MQXZ6gi7Avmkk5WoT7OIyfz8PfKo1lmLrFUQNP6jJRa-Nx9YWHUm_ZPrBbr4v7fZLt16T1Exlxz03bzzqzfLkbnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
نیمار دیشب اینجوری بعد برد تیمش برای هواداران رقیب کری خوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102739" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102738">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/102738" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
R14
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102738" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102737">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiIFWRS_ucmlZTnd_BK3z6FkYViJ0tpPApsAEQOdQIlB9olxF71xhRFp5rRmXPNGgOEdwF5I-Sp1zLCGC-29dFGi2FUnIa1reYcRAJsq-kY1qpcuIqU3uA_05Bm858YSkLBOIFtyzxv2q_pltzLHFDGOtLkp8IIgjSbK1X21XNvijAq7Aww7hmY6FzWQ6MtL9iQvm-0WgtEmEXia67h9NT3jm77dZ0zm9sSTdY5hRTEeDKjxj85fLdOLGX7qYtnBeAIfzUXyKqBYiCI3F5hTOnu8khIhFXKbpNWMhMaUbRvpknUarKqlMGokbow1kvBljqN9_UzeXVKVbRrXoRs8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r14
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102737" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102736">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6bf58ac0.mp4?token=f9Z97pxi2IRzkSA5GZwTg4nOz05FsNl-AIWEdcigzVRtaPUwXi_ZUubQVPaUS2sDpKF0dVfMP1Qzt2tEV2JZN26QhjzA_4I5XzhHURzLDS7JEkYcrVnHs3xn52QrH6DOkJrzHyLGhK_hj7XWbGRfJTy8AsNQFHsdBK-mspHuwuSBD6gFzMhZ7NnmkHWM6uLXwImw9r8UjJSGl1xLpQJ99UZdC7arK0Sn3LuH_Z99XKD9qgJXcTgE8M_aoa-CKGcvFmcJPTJLEUQvTiBbef7fdIjVHiqiWA3JqIcR61sjJKR8S_WcNJA05BgYRgrGP8LWVFdV8ptqR63UoFQQhxkCJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6bf58ac0.mp4?token=f9Z97pxi2IRzkSA5GZwTg4nOz05FsNl-AIWEdcigzVRtaPUwXi_ZUubQVPaUS2sDpKF0dVfMP1Qzt2tEV2JZN26QhjzA_4I5XzhHURzLDS7JEkYcrVnHs3xn52QrH6DOkJrzHyLGhK_hj7XWbGRfJTy8AsNQFHsdBK-mspHuwuSBD6gFzMhZ7NnmkHWM6uLXwImw9r8UjJSGl1xLpQJ99UZdC7arK0Sn3LuH_Z99XKD9qgJXcTgE8M_aoa-CKGcvFmcJPTJLEUQvTiBbef7fdIjVHiqiWA3JqIcR61sjJKR8S_WcNJA05BgYRgrGP8LWVFdV8ptqR63UoFQQhxkCJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪄
🔥
نیمار در بازی دیشب سانتوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102736" target="_blank">📅 10:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102735">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45508d652.mp4?token=H4l2AAGwvkbDYgv-u9qAb611oRD-TrU2OFCr-AAX6iNPIgx0jBAhn57NAOj1pR6_DXq5lTf4w_T9_7WWo0n678ifrMyJ5kZyro0Ec_mUwOz9aQ7Rh0_bWuX-_uhNIXJYIhO-gElMdLmZjJ6_2H7f29Yjpwrd_awQ2sMEiiY0qm4wAV_njPDT5dJS32rWmYg_9wOau3axahw08rChpixPKkyjEjcd-a1XacdNSUlbjAiMOUpICDByKrSowWHpenbzLG3Yx-PTAmbWtKmT-y7BM_nVC13aRDeJ6ovC0SK0F-4357yLyv3yun1Yu6aKoi6IIjNgUrzP6XQGwHHc8mfxMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45508d652.mp4?token=H4l2AAGwvkbDYgv-u9qAb611oRD-TrU2OFCr-AAX6iNPIgx0jBAhn57NAOj1pR6_DXq5lTf4w_T9_7WWo0n678ifrMyJ5kZyro0Ec_mUwOz9aQ7Rh0_bWuX-_uhNIXJYIhO-gElMdLmZjJ6_2H7f29Yjpwrd_awQ2sMEiiY0qm4wAV_njPDT5dJS32rWmYg_9wOau3axahw08rChpixPKkyjEjcd-a1XacdNSUlbjAiMOUpICDByKrSowWHpenbzLG3Yx-PTAmbWtKmT-y7BM_nVC13aRDeJ6ovC0SK0F-4357yLyv3yun1Yu6aKoi6IIjNgUrzP6XQGwHHc8mfxMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل مدنظر شما چیه؟
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102735" target="_blank">📅 09:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102734">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNQeJHdyp9muzkZy1Zp2Q0xGhyZDbSpIU0BZZ-7GIAvU3m3dygSECzaOVtkow_2ovT0juHckrr8Uaf-DjA7Mm9zuSFHVE-cQ9TPI49GVry98cLRY37-f5uHZ6udu_rEgyL9GTP8cVxm9sQHMJqdVbp0cnu9Tj6mAnzISWYe9Ndw3cyxm-Uw9P1DggbMn3C1hHesk54GXM9FGChA3VRaufVVDzfIe4dArc_HRr1popCQI7X2P4yZr83omF68ugW1Pql2moTOtuU1bG7IVagqI0kbjcIFgB2IHC1ehNc9XKeRY7mV7QmuBw9L0S8a-t2Vc_PM29zcyDn5VaksT8g_SdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🗓
روزشمار آغاز رقابت‌های فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102734" target="_blank">📅 09:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102733">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We2VHkbWPbPomLXdpthdLemoHycfiqL8nZkScy-6q9yXv-b9PEmNyfl1SpPZbXJDdWSoTC6m4FyeeeFTWjkaOybH98tLjB-Rnf58m719LUymANVfVaSN024e9FvgUEHhngUApNlt70EyUqfn1Snk-blv_tbiz0VU2IDwO2hSMPrQVRmZiUR31YU1Jk4I9iU_oWaxdwd3RSf50pjsX7Ex8--LaAMR76l3qo9lL8EuyXafMz0Go9RYfoubUgX6-xlNY7Oq-fOYXaxCdtfyHsWzQUrQBTkUjElUAXQpI1qvMNPIbtjybsoCTNHDkAu5xNlIRX_G9B2DbIMAPc80hjqzmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیم اگه تا الان مونده بود کنار هم شاید یه لسترسیتی پرومکس میشد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102733" target="_blank">📅 09:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102732">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663702a362.mp4?token=nhFFO6n64Tyns4GC_vIs3re06ySMt0gVPtJj84vx46Kx7HwnzSdZc8Kvl5ciEl2-ERhBEvCEsexpkTJobWEOdiKUFIt2C3zixYpKuJHMBsyqIUYC1nvJ7E7hipSUovDWDE0QPLbBi1_EQMI4YUlJd_QBFZarcdxnRu8sKjNUvQqGdsKX28S9hA16GLBD-g1FU_x2TyJcuBVf3F_OhMS2AR95Gx_zmgD_GnuvcssrygSrIKsdoOgqibrS-ANmtEQqdh79q8xk7VZaVn2pZP3ZtbYRM-p5N4WgdPYFaEJcVLwV5zbhLFenwDf9StX-omo88rgT0rR4YlVcLF1ByWCHqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663702a362.mp4?token=nhFFO6n64Tyns4GC_vIs3re06ySMt0gVPtJj84vx46Kx7HwnzSdZc8Kvl5ciEl2-ERhBEvCEsexpkTJobWEOdiKUFIt2C3zixYpKuJHMBsyqIUYC1nvJ7E7hipSUovDWDE0QPLbBi1_EQMI4YUlJd_QBFZarcdxnRu8sKjNUvQqGdsKX28S9hA16GLBD-g1FU_x2TyJcuBVf3F_OhMS2AR95Gx_zmgD_GnuvcssrygSrIKsdoOgqibrS-ANmtEQqdh79q8xk7VZaVn2pZP3ZtbYRM-p5N4WgdPYFaEJcVLwV5zbhLFenwDf9StX-omo88rgT0rR4YlVcLF1ByWCHqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
دیماریا: دربی روساریو با حضور مسی خیلی سخت میشه، چون ما همه آدمیم اما اون از یه سیاره دیگه است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102732" target="_blank">📅 09:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102731">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZBQ0UvPjeSkAIM5XXQ05YZY0GM-uJoIobbeZkM-j09BjKf1kzh2FzAP0IsTzNEFBWHEbg0P6JPhcpEtjNvnA_TguQjRZs6_33zay_bPCly3f5oR9y7dKKNApxvQ5C8fkhCv_EJbrxZFdlgOExRZO3NDuugY0UyTn9HNxT4qZFW-O-I1OW3RYfWJG9foN44wJS3xHy8LaYoY5oLQav3f4CqCukR_JL7vZ7drWwF1XJJ2L-OZFPQUyrQM-iutuIdzRHfNr6uEXRFJFn9EvLfk2RPYtqf1CFDNpovvBvZOL7tPiBGupvuuAzX9w88PiCiORVvXkq43GaFAgle3v58npA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
✅
💔
#رسمیییییی
؛ اتحادیه فوتبال اروپا، تعداد کارت‌های زردی که منجر به محرومیت می‌شود را در لیگ قهرمانان اروپا از 3 به 4 افزایش داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102731" target="_blank">📅 01:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102730">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYxRQ_qsTry8zeXsnrjWUic4g9S7IonhTZ9SMBdFeZyyGWbcnovX6wqVQScVOXcWeSEiSecOmYThrKlexzKQT1PXSeamZZ23Ih0C0Af70cWodBLSj6A051F7rWmi8MZ3od8_ALuZ3zLajpGS49qiXo5ZCjZthYhbQQ7UUqfC4E3ISzX9kWxfbfyBaLF0QrYxLm90KUMCXGAarunLPliYMVfRmzoctfvejiTPNNDKQC6pK_zBohjCbRSUq623Fl9GqfURtn4ZfJa4xNHs6UGDlxX9oGLmChIfvKB2znJyiUuxTizIeeM3VaLHOXCwbAeDQz4QbmeMFrOcfYGIN9fs9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ به نقل از روزنامه SER، جلسه سرنوشت‌ساز رئال‌مادرید با نمایندگان وینیسیوس جونیور فردا چهارشنبه برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102730" target="_blank">📅 01:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102729">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffk7-L3npFGMy0Flq_mWoy05F2RMmpl-LHSR0RJWoflP20YmUAPYzQRKUNCSuWJ_JeHhaSFDiF49inpzxv3sLlMrXQBVfz-7TScOYriOZm7Md33feTKsgJwIlkJcL_EmoSpCkfqp-ioBHl-Ux_NaQIiIj2QeFA7QBBTfl5s1OvEFGw9-1gZyDJ44-1-ReUZhc7T7pPqhBi4Lp8eakJPWw1__O7OWY24Ssq4cryHwGTFwED0w3-CksCDpRdkP_1tTib-HN3zBIhwI7QfmyDaMV8GwrZHn4SDXLbpEXLxCjAINbtWgORa9VqXSkyTswJvcDi2RsOwGGFJI5yEhhSsmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
👤
جوادحسین‌نژاد در مراسم رونمایی از کیت‌جدید تیم ماخاچ‌قلعه روسیه حضور یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102729" target="_blank">📅 01:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102728">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0hnk9ShkY1fzA7xMKcKzetk9dIdI2Vcd6ByScyE9BlBNfVR92_MAz9qmljanHcauAm3DurxUFxuPAzYG5m4tFfeCONJhlK6WLIE865hd0ORP5NoD0pumO66Wn1rDKirnYqJ9UzmYbM_-Fm7Yw5AqCQRlp2R9vetq1m-jyvhPlDcm8X8UNK66Wa40_x-29q3dTQ5IpgJU61HU2Q01JZZpym3WjbYkWgN-CHx6uAhNqZCl4kKgUOPHwCfZUA4CEJOYu6dilPqbRevUxr3PxmiAaVE6aGY8LyfyG8-ovX6iwdjgUg76kurVtjqynS_XoaGgF6WVtGs8zo5RP4OpteEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت انگشتهای دیدا در مراسم تشییع بارزی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102728" target="_blank">📅 01:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102726">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c707c5bf8.mp4?token=E14PUGz4yIVFO2LAAoORoo8injMsEWdIfNQ8NBbuOaTV_QUXKSdaH5C-GxEpImIHH9JLDec0Ur5aeHpDoQ2IXgQg85q4dEHcxxJ71XLgv0t83-_uRfILyaurE0xYUrtkaB5v7CC9c5HA3HEWg-IkJt-PV39Ffqg-6dSrzhfyL9Lh_EFrz4jUuECTD2XUur1X9SuQGwlfnwiAQJKNrmFOBpqVoPpdAJZXdrm8wTONeGaI8sWTuQCmQMYlk0F6eCeIVcRm91Z2dh7HNd-R1jyTIfaYPsRaDReRJ9vR0TmqKbduyEq2utY9BN5jUao6qAeoBYgptXbYBoyg_2oYIrzDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c707c5bf8.mp4?token=E14PUGz4yIVFO2LAAoORoo8injMsEWdIfNQ8NBbuOaTV_QUXKSdaH5C-GxEpImIHH9JLDec0Ur5aeHpDoQ2IXgQg85q4dEHcxxJ71XLgv0t83-_uRfILyaurE0xYUrtkaB5v7CC9c5HA3HEWg-IkJt-PV39Ffqg-6dSrzhfyL9Lh_EFrz4jUuECTD2XUur1X9SuQGwlfnwiAQJKNrmFOBpqVoPpdAJZXdrm8wTONeGaI8sWTuQCmQMYlk0F6eCeIVcRm91Z2dh7HNd-R1jyTIfaYPsRaDReRJ9vR0TmqKbduyEq2utY9BN5jUao6qAeoBYgptXbYBoyg_2oYIrzDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
فریادهای مجری کشمیری تلویزیون جمهوری اسلامی درباره تنگه هرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102726" target="_blank">📅 01:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102725">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5XIXA2DSq7M6FhIrJJSlyrKhvzzQqP4W58NrGobspwdImmBDpanBv25uZk0CsDeUbxI1BIL89QLqUDt_i5aHhawsQg5OunaSHI1N-3FsnXCNEUZljlThfCrDCoAMBXGwfCW-jzBIGwFEEjdTQCLAkis3o0kKwtJ_Dd-b3rsqwrVNFx5WcDnYTT6P0UByaQS3K1IRtxxwF9h4eKPCGwuVw5HzWAAkrJimY9iywgj0UlXcbVRLxWpa2l8cmVtHTycdjei2y0Ejz3Ta_GkwcFpwUFOG-apN8RCUS2Ec42ZG3kOq5ANl_C7ZnvY8NyTzTei6mgL3iQONrRCx3lOfKA6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
باشگاه لیورپول درحال تلاش برای جذب ابراهیم امبایه‌ بازیکن PSG است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102725" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102724">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
بازگشت ستاره سابق استقلال در آستانه بازگشت دوباره قرار گرررررررفت
💣
💣
💣
💣
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102724" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102723">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EWzoBA9AOpOnhR925zQO4REiTLZ5Ley0zXG9VA2BiSfPnv34dTQrnho4zQOfEbqKsmKbLpiD3fYErkttoDAg29xlmZ3eSrDmXILxhzHIhFTetzvRNlqsIzKsiM_6gF7dRsMP__jO9KL1nnjdYnFMeF9vWLblaJPRJbjJpmS-Ea7w64lN-5idIJ-HIXGsnpcQgUY8u-HkkiU-OrDG9X3EA0JUhbXASpV0RLnwptNDzjbNCVv4MhyY-NhcsEU2lkC3AH2PWq1aL9v_UQB1XuG7PsHGoYAa5k-BZ2hLmN238iw2iX55dorzXOalIM9CPYp_6NDWT78hBYjFL3UNCmzB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازیکن را به استقلال پیشنهاد داده است</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102723" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102720">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WJJqKecGVEawSijOl-ZwM6WOVP0MvL07eMUO86k_RmLAUijUs1K70YBVJH3LHLzq_rtsslTZn6PSHrebRCDjOh-mqOqI-P6KzM6Z_UxO0mjwVGxozPSUmMUyua5AlnSUAQVvecpncRiZFEmmXWldTUuLXMEjQP7p-u_SvOuePkUgYTiDs0rkxTz4jZ5xLqV4ziOsJN4tMjv0M2YiKYCXh-06eJEqat1aIw4fJgIIoIl6WUdUc6XKOKj1CdxcwZIrPmRKTusRGYP5Aojxs0aAvXrvi02S90I7OK15CnnTw1zokwfBgJwTRiGxJQ8QpptzrRJtY_DwJubq7uH1_PGnag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWcZLOa9Er7LqIXKfTDWcxAaM_OWDT0AKsDbzMLGtxLb9IXMFFdjjG7Nd7f_Ob_TbF921xdAcPO-C4LmZ1uN5syKfX2GjpO2A9stmYTknUFVBOAfrQKfLzUePD9lft5y6M0AH6FiGJ_02UQ79vJR83Vq11H2szVfLE0At1ZvRm5HEpcfHzqBvl2zRylzJR-7sJ0fOxWSEIQV-OlOBPZtRpUR9UTjUz8H1ZyS8MpIvlGRIMlgpcApdAmpH9MV-gbinSACNG464dso5m1rEYoxXlt8Xz8oS-gpxwwjaQg16QGS5yJZUKbk69e8LLBpT9loYZdnnONVgaQH3QqFykNSVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVAttv6SGcv6gM24EnyfsglmNuo-FT53ktZhc_uGNFx5c7C2P4LCPc83PlCFHqAWbmbHQv8WonSA8RMb5GWFDNFpxD83kOYQ-1wDJrt6CMY0HHBYvxKZBgcMndg9KyIPmPFQz4FspFfYh0U1DvsmhkaUhywnv9KQpVYAEbGnAS95ex4BPGQIup2I4C_4NGbpUweOfYVNWInKpA_o6W_J8KKinH2UFsh7dkUJyxnjIC4HuftBrLHVqCg9whw2kJuuqbVVQCuImu-wuXgZfWxz8QweDrKFnmtajkDyDciDLO1gObmmjeMHKXw80TSnx5mQxmYpHfaHXc5RKqBmgY375Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو اینا رو با کپشن: « اسباب بازی های من » پست کرده
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102720" target="_blank">📅 00:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102719">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw08FgVyh66ANTTCq6nPywIR8qQrfR1b67Ql50utnPHIyYyxM0whxUEXBt2vFuV_X6M-ayeAxY7Opc5I1b4P6c28fZhAg3MiOTmnsoIfzMv0OXOB-sTd0sYMcg72gr_BcRyKa38A6chW6kThRT4vOPteXpLd75-qAqZLBQm8ldxzRfM3Y4JuuHoNu0Sdrtc8ylpHX43IQGcDzD5cUXw40t3oOnw7o7evb4Ayobop0j6PDgfjSUFZhEgo_D3OwbAlz7hVeu0bU062Sx10Y5dBZYCjRuwZRybNjrWSk-qDSAVx8_pV8gytD4Do4puPzSZahHQQcSP_J4ozoQzM2aFyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔵
۵ سال پیش در چنین روزی؛ لیونل‌مسی اسطوره بارسلونا پس از سال‌ها درخشش بدلیل مشکلات مالی کاتالان‌ها از این تیم جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102719" target="_blank">📅 00:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102718">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKVdcfb4wAr0E54_Kg2blgvl09Z8mA0iwamBWLxlC0Gk8ueCM8x18OVwM_PQRLEbDF1B3FfoYtKI_lEPWdqoz85eEBmYJIUbAJnvYzlqQRrBw69pJftr_prdZv0bX6J-goeo162po56npw5b_-qqGHBR1BIvBYQ_9Pw_w4lZi5ysGUPBDJLLmv5HjREcHocDRvH4jHFMICRUcnXn39R-Agyrei74BCc9OU0OE2h5COioJxqWzPY8jFWdYDxdISRfYBXZJB24nNz72zBCm0MABnsgIVIhgbaWJVs94zyVtUzUV8yFjoSRKQMiKMSjQzyNMTURNm6utVK4vPgVOb4lIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
فنرباغچه ترکیه بدنبال جذب پاولیدیس مهاجم بنفیکا هست و برای این انتقال باید رقمی بیش از ۵۰ میلیون یورو پیشنهاد بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102718" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102717">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUtRPp7JgdMqCLE-Q1vAr_moMy3guofBXrnu8QJ10bUGVldJS7G46nCW0DRJYf8r8B-_aIe-Sg15SSoncj3x-xXbJXlGabKCJPTGQWxZ7e9RKWyM9kAp8otb0CouX-zkiKr8yV2QQLXPKfOUZTpuVAVCS9yTlTXl4g579EpQYw5PjKrTYfJs4Plq8g0WOWi23s-538-QxWtaT32wPxA5yv5lFR4toKp5YIFv0JneFzMrcx_v1iu6Buio-BswIwgYZEnzhAsX31cHz0bHkdgIfUlvlZmriJ9TA397F49gWkrFeo7p5w8E9bSqje1mu3LNgUpiqbzhBL0jOVUAAFrSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102717" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102716">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UyYJAuhfZQlsOv3SktpkLuSmkclFa-7B7YQC-3IVmCAi34WuU6PSmEJkfgvgOS6tA9Dh6B8Q0EltBXg6MpgJ3QKwSo0N2PtUzHwpODMgT_wkdUx34L_iN1PEnnmLL8MAe8rqNl7SYBPJ_J-9m7uN0CzxTUdVPZLNutn0-x28gL1dtpVAWKJZMOZuB1aEHqyG9jiqFoWn0lrJCQvJZHDvynLiDJrExmFUdB6yJgCUkXu6LtfS_VpDT7McG91Mq8CH9Yt8iFs-cCtUHwdhmirnF31eFPQCk7tmU9E6GyUBN4IfhCCkJ1uF6oTuXC3c8MXdLPThzgr6k3bJOGdZE6OC6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
جرارد رومرو خبرنگار نزدیک به بارسلونا: امروز تو مادرید دکو با ایجنت آلوارز دیدار داشته. طرفین میخوان هرکاری برای نهایی شدن این قرارداد انجام بدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102716" target="_blank">📅 23:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102715">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EluGQj9aGujZRjmmV02newd3xxAF0-z426jqnLrCccK5XJqueJMHSr2geEEaeGLDyN-NW0pRopRtYbAkmhlMTXGMn3tyC9CnrdoU9_DUX22cE1WNjXGaWZCoDy4Qu_4H69A2FpP9_AHk3GgQx9RlTorZOGTxj9B2UEEHPTrM9etwAa_PcnguSSXKW5PVk1F8TlfMQhnm-K9qz7kS8znJWAfdlVQotgZF6Mb7XIVVwJnazA4jESm5tjTVbhjuwwb48T-EilqZjGL5h9bop45VDkLfY4-hhx_5VLxv4cCCbLtDTYoXyxd43m5P-E3lBSii31I5O_Xbb4FHpY3oEDU0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو و پوستکوگلو تو تمرینات النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102715" target="_blank">📅 22:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102714">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4oV2zy-bhCALjUz_h6llZLiZR7G8de4iLrQYUw470JtnvOEjGi46E-NjDonM8N8E1z2ZatYbPxIFMQKoFD9zZTYPDQoDMZpvMLoA6nQld163ygjjSxnxrMuMfPaDvBzucB2TU4WAqP4DEEmsKxQ9jsGvBVxq-U3pu-zxeiGa5IBWMA53w7Nn0yNwMVf-NUNaVTuOv3AWq3tTmHgyYtJTvr4cm-cuBtTpXoVUN5DqfKsI0rIJceB8TmjlQLl76dAqYoQT3x5TRsYNoK0mPoG_BEw16DZ0LE8kB0OIIh4e3q0gc6oUky2mjSX1WE_vOS3Bjd1tjYzyFpvcQ2U8WNkKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102714" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102713">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=qm4fkk8UflRfbXBs8nAlc109KRTgI92bWNMnlY7DrPNfOGjkDrgDwa__rA5VrVj3jNx8Rh0O4jKga542zLPKUw8RNAHAcVhSDMYzZ2rZv5spRagEk1cPIhz8NbGaNjnmumW0BqtpNJfFWnIr71FugbRPj0ugR_9lQvvhtZtNfWXDtRprX97FeV2RC5qeu0sLojqdo15YYmGukH9LjyKuqim7bFYiYt6jkvnaTk7brHN2-JzL2_GtBJPbgh74YCp7Z1m4yU1eLQUQIwt47G9NH2bOogINFMSmQOueBS27nLihFtZKDKuCwmwI3fidH53uTar-uzPKuXywKrJWbM5BgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=qm4fkk8UflRfbXBs8nAlc109KRTgI92bWNMnlY7DrPNfOGjkDrgDwa__rA5VrVj3jNx8Rh0O4jKga542zLPKUw8RNAHAcVhSDMYzZ2rZv5spRagEk1cPIhz8NbGaNjnmumW0BqtpNJfFWnIr71FugbRPj0ugR_9lQvvhtZtNfWXDtRprX97FeV2RC5qeu0sLojqdo15YYmGukH9LjyKuqim7bFYiYt6jkvnaTk7brHN2-JzL2_GtBJPbgh74YCp7Z1m4yU1eLQUQIwt47G9NH2bOogINFMSmQOueBS27nLihFtZKDKuCwmwI3fidH53uTar-uzPKuXywKrJWbM5BgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…..
❌
تصاویر مناسب دیدن برای همه نیست.....
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102713" target="_blank">📅 21:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102712">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBBn1MpzAjTgPIgmTBDcBGDqXsDZtcNbOyysHIejm9avOWzRlK21cL3yh5GMwmXUmDV4UKBc4Qzwj84R08vUVkf-PIg6iGafQiO2Lileg1O_haEFYrzuQ6o_LHp-NXUq4o_0B3yrxMKOBE2RkwYdhccxdL7mm0T_uUhld81URt-w34Owty2Fyifzdl7j_0HwvnmmoLujA4wz_J9HaXgwHpc84DMeA2yma8y4Nu4fy8S4OL0ImnbctCEbK16hMba6mXWpvTGSnNGMgznOQwCbq2QOI7kuXDk0mhaNXnsuLr03jmRFkKTW7bdS0AZ6Ij-ztSiajVEqjaI-h7LrfFgUYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدری از پسر تبدیل به مرد شد
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102712" target="_blank">📅 21:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102711">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9rXDWJ3JNPDXRJ36-Xo5SC8V3ZSLci9Fyq8q9Sk7PzV7_B5T033jCHCWoPicQeLXoy0EPJ8mt0go6U_4NEoM7EcF54cAZ9FrqJaDo_sC1sh2DwSa5VnwIJzP_yLsLCK2kj2N7P9y22PyFCVFg9QTIGGW5am2me2T2dyiqhtSj6knSCySDjZMcJNVRVc4Pq2RQwM8155uPFMhparT22KC9LlEBpgZiDwVdRWOtPBZ3CpVMuEjFLXFbe8UCI1c-n3VYWujLHIpFDQp6JEVSIHuASiy2VS2ScHF1FFKazoO2ozZ0Br7qAlzybU6NDW9u2G3XeB4ykxaxySRKmjR8R77g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل زده در 10 فصل اخیر 5 لیگ معتبر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102711" target="_blank">📅 21:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102710">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_qxDjnsyBRvpKODREF74QF1a4X_EArOXX_lgpVnh9aziZXE2Ii936ddFnc3sM9ICxGDAMzXIuwc26Xf00_snI4LgeTI0d_7Fq-6LOQNKl7rwzHD0ClHIkomWTzQ0srgAQSzCTab6Ta7p5wJ3bw5Dg93t2bSU20dETSoq9iSJfsPpNkq5xzL9r6EFA0QH8GoIAOinBMB00G2dGcF7Ajb4dqZ_nrRVe-xj5p-YlKlXrRZNKHArK3gLezOdAjgKLjVGw0hr9huU0m7PbvVH3upJqN6RUN2aY_GZzsCEbdO8ZMKtRz1kjcI_4ZSQpaKcPnG7OyXOakRCFKdk9XtT338Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
رامین‌رضاییان خطاب به مدیران استقلال: دست از اینکه منو بذارید جلو هوادار بردارید. من حرفامو تو زمین میزنم نه فضای مجازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102710" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102709">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBxmhs82n7YUVlTJYENfQ6nM31B8nrEeXBmRuEo4pymzmUkftMTwqz_vg1E7C5x0yAnja6PW-GCg0SRNQmR9zRu9AmFSUpbzzR29-e5c0GdPxhYNy8hk89tfZApoyMLLaM_udE875iqtH1-1ergaobAEtQrIAjA-2Cp8YWXTMhqkgk3hYfXQjEwaN5-40HZMS8-H-GYzv43A3JGEOEpog2ijlBugJptFfT_6F4ZJ-f4xv7RAMZNUFdB4xsdDA9ObZM1M4CKkhymk-oedG5cl-AHclsUYqr_fxNzQD0_LFYEahozWBtcqn-kcBeI0kzm8F14H5DtTY52d8YDHFxOgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری
؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102709" target="_blank">📅 20:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102707">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyyTONgy6okUnT4-ejYqEFrfU9zV-x4t9ukRO3G-8Zf8__AZkM6HT40G8_nJCeFIj3b3P5eWnjTDxjqebJGPYeBg0--gjfsvOGqLict9f0namX77rPI5F98gaV2jCGtdjBTV01FYJCqgGKWg_0ESLv0j7bCCHjkhbPl4bjdOlr-AWiFsJ26flGL0q31GLUw7Qu76Ml4n4CBslxvFaqH2QruolbQXop20SZnoyKqS-AcEwuu7_JDuQQuAAEVvaJgmxruixtqXDZoJKxzj8ILs4ZY_bmo3LatZRiADx4fioUzpmlhRYpDbmgJnvbihnEDUhsiIjJfM58NnHjdDHt50IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WzPi8NKfmL2DpGcyLklKDs9NpTYEnAyKsUfIHRzETftkAMyy37ZXRQZt_9iZKJzxbk486MDfZ_T5RaJYWvC52UypGGLFIW_mXFS6Yq_HERLOLBSRmY9mxnTUkcYRyJ1Dtu0zeo-cD64j-vyG7PGZdehpGG7D9Sv8Q7OJ_WHFYH_Bv9DogsaXq0x9bFTZin-j5ieCIY3BXAgxiXNBJX3Xkp07GzGRrU13K3ndwj-OOzUitO-0w2hxEuDb5Cohv4rddb7AtGUGEB6MWpvp3sL7qResEoOC-h-_inWYW_g2-lxlRg-wkx3CCpwuuQRXne2K2ECpTSAyBcVf_f9TgRVr1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
ویریجینیا:
من اصلا حسودی نمی‌کنم. به نظرم وینی جونیور خیلی هات و سکسیه؛ اتفاقا باید همین‌جوری عکسای بدون پیرهنش رو بذاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102707" target="_blank">📅 20:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102706">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5JqzkwACWe7zMbiKjltU_-vy_nINpC4m6cEjQcSO4CCmeIRCQS5tNMv8TZD0z9Iu4lIoqPoNM4UReNqYYlSzOpPONlmFArpNtfMl4PnF_v4UOysyMNW6tVhXDYwxCQJi3kaIi3byX3UwJF2S85UzABUbBz0BC8yvopHEEzaCkKJ_FxLZU2tC_lAaO3UFvpgwJZfCQ0l6yKsplpGMV5PD2YdpPMLxJr8Sfmt3IBVFvRmM7TLTm9vTXzlLWy7qkOtAVtQHQqDhpoy7iuZw-DJO774lQZOk54Aq-e-T-iMOFctWascHxB46Ruc9uQTFFY02llcDajRtqVqwp391GaZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
فووووری از فابریزیو رومانو؛ سیتی به دنبال جذب پدرو نتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102706" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102705">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=r42vW4IXht9zHq8uVWm1MQDCcDbl6SAml4DQkpDzgwik5DEJ80q84yXUicVNGNNIXVOv8yYc73g23W6V7f3DZcVTvwdcqlOlBKKXFzo_YqzZDgD1WybFNfdbOjZUj8AtEP1DqTU_wg0EkVCo9nhcYRQv7i-gVN-RJSzdDSv9cnBf3pr79hvZqJ30AxAlonEyiMQeuXPOtvp7fwCMO1kKDSsSA2EKrLwQY3ajynTSXMk_00XQ611SeLyJ19i9SFp5OckwmMN-rqky1eRfRmVhFZguZ-8XZJhCfzGx89O9ab1rrHthr7tQXWniF5TKvGKv0iWyNyx2eKtBbZfOe5EefA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=r42vW4IXht9zHq8uVWm1MQDCcDbl6SAml4DQkpDzgwik5DEJ80q84yXUicVNGNNIXVOv8yYc73g23W6V7f3DZcVTvwdcqlOlBKKXFzo_YqzZDgD1WybFNfdbOjZUj8AtEP1DqTU_wg0EkVCo9nhcYRQv7i-gVN-RJSzdDSv9cnBf3pr79hvZqJ30AxAlonEyiMQeuXPOtvp7fwCMO1kKDSsSA2EKrLwQY3ajynTSXMk_00XQ611SeLyJ19i9SFp5OckwmMN-rqky1eRfRmVhFZguZ-8XZJhCfzGx89O9ab1rrHthr7tQXWniF5TKvGKv0iWyNyx2eKtBbZfOe5EefA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚽️
#فوووووری
و
#رسمیییییی
: تریلر جهانباز FC 27 منتشششششر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102705" target="_blank">📅 19:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102704">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yd6taY68x0HnHynXcADmFP_VGJqGi-GFErybx7gEsNYrbRzaNNVFUlRN15XCXTMFBJp9ZGVfvkrc8dNYmqBGJRvuW2-h2UqCxrxUW_xI6ikDqzMJivXUGk5e9qCqJuHX-YICNBe2pzRfLNYfTwrH9rNUvLNKNPRSKWHAvwwpBHpk4UBFHFpS-yszT3mAWyCUjOwINfQ5nEfdnScG-0vO0WPfV1VMidab3k5mWL035k5wD9FDK6toLTmCRPtuJLXf-P27ivKauXFh0LUyLnReugfY_1F0wxMxsqhOs18PrwcloFUsFtHsybO2Neyc6KgxMR5gpAzMbXPDZRf9oil7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👤
پست جدید خاله جورجینا در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102704" target="_blank">📅 19:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102702">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fkz8Yd3HbYC7ZlXoIpq9V62waWmj3jtnpofzVWQ7aGeciUxIvkTndACe1PzN3s1vCQ3s9AsgdBpXbX7V88gKpgYlmiDppoGJNFE9QCVrIURcbviOO533SxS03QAIGbb-gDhmhsi-CMxaWgr7iCAN7JK8yChNz7Zb5d0WjRBi0YhcHBjy-ErQV7fDCgxEeMqwSiRoT6-SYilXHn4iZJd4gzy2ptVf9-NRyRnIf0Uky_xi5vm3h_4lG42DisSXwt2hX_-Ge-pUsFhiqLgYEytMqDxMDXtCW9jJeLpPkZCLnZD6X40WBNoOF7_RXJpBmpsMrVs34C_ld03VWqOQRZZjKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sf7hjUCeTJUJo-CmPIYOc7J3SvDcYoMWlxSEiyAds0JvAGCrWM7KpTxgVgBQ3Vi0PupmLCUz-nmix0kHWwUgJXOdbU5Foz4NL0VsXQvEYDUOQGhdJIBKMF5oPfLZmOLU3PdlpN21qOk4H53s0vra0MBHnKkrHn9y2HoB8ocl9LBVjkjMYrZ-6KNNS02DVBUOgcTtMWRO4KaKIQpi-eBpoHluFwaVrvy7RX12MeIUnLWtIlfrgAwD5X-eJE-f1g3UcGH7ydXJKexQK-KTP3fonM3-aXEhbo0QX5hh5dLnt7LISSMVh4SKO690E9Pzv0LuPYQOTJWEZbsaj9l2FR2TDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
رونمایی موناکو از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102702" target="_blank">📅 19:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102700">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=Hm4hRhb7pB8SCefp0TV_B7PtAOR8edtKZNq7m6KQqdy5iq07HdxnkFDCz4Svr1dtj1xsfAXU5ltHmsYp7y7cQnnkI0bex7TmkzycwGipfp9kR3X-9ZRHx0vXFC9wh6rBbrwN843upEt-yzllqZDp0l7Siq5qwTXXF1iCqUmTF_W2lXPG7akAc00bF6FgIk-GRMP_H458jWf5LOEgGEzG4TeuJGlx-TNSlVJXVeGG7WFK9SqR6ho6nlLTZVAkKF5N226LsLYIi9WNP5zGeLJKluGCAYWBOeH2y0IYZEabTU0k1OmxFW9iWuFmJA06qg1uJJpseM1ai0RbvFil5r_UWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=Hm4hRhb7pB8SCefp0TV_B7PtAOR8edtKZNq7m6KQqdy5iq07HdxnkFDCz4Svr1dtj1xsfAXU5ltHmsYp7y7cQnnkI0bex7TmkzycwGipfp9kR3X-9ZRHx0vXFC9wh6rBbrwN843upEt-yzllqZDp0l7Siq5qwTXXF1iCqUmTF_W2lXPG7akAc00bF6FgIk-GRMP_H458jWf5LOEgGEzG4TeuJGlx-TNSlVJXVeGG7WFK9SqR6ho6nlLTZVAkKF5N226LsLYIi9WNP5zGeLJKluGCAYWBOeH2y0IYZEabTU0k1OmxFW9iWuFmJA06qg1uJJpseM1ai0RbvFil5r_UWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
مطمئنم شکیرا ومپایره مگه میشه آخه تو 50 سالگی اینجوری باشی و با 30 سالگیت فرقی نکنی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102700" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102699">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=KBiEVuE4LY2hAYkf468MEVZK_l4RclIPkvMQ0I4LJfeSCPIz4LNhH0bD3eY1DArY6yrxnJ4lYIbJvB1DecmiQKmXH9oPYNIwRCG7zchJM0dDnMwHgvsVON_o6oLO4HeiXPTzHRfAK8pGfydLx3YcKABu1A3i342HYIaMnMJSpM3ziPjNcfbhJtucmDZlNDE--9ITVPupj7BbXU0n2OA7f2VBtdAI0lk4fXV5VRUwTiyl6Tb-cWYPfMOI901wA1sXzwjIcadtwmzQLzeeTRJmjCTmfuHHcHEsrKNr6Bdrd7M4UsDv_aXkj2EOwW1hWFr_hDEnEIG9jDMYpAsJb6gXqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=KBiEVuE4LY2hAYkf468MEVZK_l4RclIPkvMQ0I4LJfeSCPIz4LNhH0bD3eY1DArY6yrxnJ4lYIbJvB1DecmiQKmXH9oPYNIwRCG7zchJM0dDnMwHgvsVON_o6oLO4HeiXPTzHRfAK8pGfydLx3YcKABu1A3i342HYIaMnMJSpM3ziPjNcfbhJtucmDZlNDE--9ITVPupj7BbXU0n2OA7f2VBtdAI0lk4fXV5VRUwTiyl6Tb-cWYPfMOI901wA1sXzwjIcadtwmzQLzeeTRJmjCTmfuHHcHEsrKNr6Bdrd7M4UsDv_aXkj2EOwW1hWFr_hDEnEIG9jDMYpAsJb6gXqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره خنده دار پیمان حسینی از عکس گرفتن با دخترهای بلاروسی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102699" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102698">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cL8iyWC2w0nMQjOYHNWUGa2sR3qXpkQL5Auvec3mVhvZYsoo_v8-YCjD304lzvrzQ4_2Xcm2xvicbaNcivD2oqag6zFiN0NfQ1NLvJanF-e3chhfai40ZbFh7yMMPEp4uj88Oo51eh1xm7eAqyKi2gfeXcTW1Migk81nSaF3r9hm9RCz38gVm3HEeSSGeMWL9UI65jcKjYcZqKoxgbROAWUvsj7qwUlNSKAJBYOmZW3wm3lWLf19BYJPKs235OBVmPyhGgpm7wWq7WWNj8JpArGSIbJ4VJWYoZRYyTRw_EUH7n5ZpeElKVjNdYwG-AmP_1DVhnbFNjk1py0r109Rsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102698" target="_blank">📅 19:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102697">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYqLd8KUCFI692GhZqR8_kct5RUgHpuVpmb2y3jIfLk3LHe1YJ0IElZoxRod8U8LLYJ4VHk6v4UAUCIdPQIC-afSGJlmSAU5fl_6U2zKKbbmmt2E2BxoPlX9Ct2PnJ7bDTGl_o1IwMzdgZH4uFE3mmXZiuYqCtyonKBXAcrmJAJsz1iY_5DQqHjQJ_ekXRakBldI6eoyEI1xHGWhnLsrA11n65bX-O9U9Hl0mzSLKHuo3OTavsKHnCXITCclI8kBwDulJAPxfI6WJn2khHdW3i61TJUyRdWBf6nL7iehb4KcR8fpbhGjKAaH-DBJPaiSHu_3mwEG8YVCJo9NexUXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
#فوووووری
از رومانو: ترابوزان‌اسپور ترکیه اولین پیشنهاد رسمی خود به مدت دو فصل را به محمد صلاح ارائه کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102697" target="_blank">📅 19:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102696">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoDw9a9YPUrRO-oJO_CXJrCVr-m4Mywlw5vXlpsAuCwPEmuq7yBux2nlA31xK_CF0zFqG6nPcDnUJ6N1fVS-R3ZdRaSfZyGt3DA-aFAXTvrAb1Vy7g0cv_f-r8wEowfeTTt4ABtUvvX_ySndmBlj3Ztosny3xr0pvTDE-rXpjtb30Htr11FjR-GccCsfz09mxNHjPNDAw8UfVYTwxTIMRgn9TceociKiWwBJPkZRj75Zauxm1e8S38MpSQrrOjMS4sH1kIFXOcF6bLJPnHxOKe3I28gFqBp6jQ8XZBr7y-rH-9Ucgxt3hcQJbmEn-C83Qi3mRgbY7aBuBjrjeNilTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#رسمیییییی
؛ علی‌نعمتی با عقد قراردادی به تیم لوسیل قطر پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102696" target="_blank">📅 19:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102695">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b46370582.mp4?token=OF1kHlVNGxZr-sQRaBPBS0TNV8P4wggHgTd88yA5qtKsAfVvtQxC20yaqsmpJXYQ7ouCnIad_AB5UsMz9bgvoKna1h58KS0OuEEnCa0VppuMppMiK1FYbcT-PA3pO-TP3kV5AVKZ-Op_5tmm7i9aENVDnwa1CkKMIWo_f1HzAPPvuIWLpLM629-RqdXTJJMwGObd8Szcth5VP24-8s92Ep47Ga3unLg16M-ut_EsZvlmkscRs-3msapeNWmgLfNUw8ihQF_xchLqcdPtJRRLEaldUgTRaE0BLDxbgzkZypetIOkx1qyLGXlL9uSJdYSdX3e-MaHFFsoYYq-H1-FJFWUdcKvytx5-jdIDCYQjBbXL25jyf0gC9sbObLHKfZufN-Ba3QRab-ig4L4a2BQ5OC_vQpCqGxD1Ju5X_lcsCTl6NwYANDB1bXO2XiMISYkbzjKw_rS7JPTlNlXp2LdSt_aLnzmaFE4MYTapvPRKbJnWQbhleHFa2osJCzWNvJz9_vcXe6SixaIxdu4sNr05T09nd4yW6Np4jLRI24slHxNNUfXk5af0dC8W-mReP15MiXARo4hfMYYgGK5LxUdRzKLFwSWdOv7zXRUZnWK-VDO1dOd0iBBSJZjf5IS4KzzP4zLCI4gldvX7lxePA6JRfJCHstluXg7dDKGSV11DIEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b46370582.mp4?token=OF1kHlVNGxZr-sQRaBPBS0TNV8P4wggHgTd88yA5qtKsAfVvtQxC20yaqsmpJXYQ7ouCnIad_AB5UsMz9bgvoKna1h58KS0OuEEnCa0VppuMppMiK1FYbcT-PA3pO-TP3kV5AVKZ-Op_5tmm7i9aENVDnwa1CkKMIWo_f1HzAPPvuIWLpLM629-RqdXTJJMwGObd8Szcth5VP24-8s92Ep47Ga3unLg16M-ut_EsZvlmkscRs-3msapeNWmgLfNUw8ihQF_xchLqcdPtJRRLEaldUgTRaE0BLDxbgzkZypetIOkx1qyLGXlL9uSJdYSdX3e-MaHFFsoYYq-H1-FJFWUdcKvytx5-jdIDCYQjBbXL25jyf0gC9sbObLHKfZufN-Ba3QRab-ig4L4a2BQ5OC_vQpCqGxD1Ju5X_lcsCTl6NwYANDB1bXO2XiMISYkbzjKw_rS7JPTlNlXp2LdSt_aLnzmaFE4MYTapvPRKbJnWQbhleHFa2osJCzWNvJz9_vcXe6SixaIxdu4sNr05T09nd4yW6Np4jLRI24slHxNNUfXk5af0dC8W-mReP15MiXARo4hfMYYgGK5LxUdRzKLFwSWdOv7zXRUZnWK-VDO1dOd0iBBSJZjf5IS4KzzP4zLCI4gldvX7lxePA6JRfJCHstluXg7dDKGSV11DIEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این خانم باتجربه نکات خوبی رو در مورد دفاع شخصی به خانم ها میگه، حتما ببینید :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102695" target="_blank">📅 19:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102694">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqq9GpjCOfJ8zI0kmMHXBmc4ir65OBr9Nx6CdGR3hzjPPn28ELnK0fsbinjvt0KCwgajXT4e9gCzRD7s--Op6PgMZRDa7ZEMM2viJEaLQWB9I3gSux78GBz1fZ9sM-sBC_1xhJgo-Tlw6iNul5YTPd0WuV8lP7iJ-I0Iig1ms5OjWXSSK10bpaubZ7v8clsa00R1aRYX6_eN3C42OmPBLVjJn6Kd9fTVuG1uQzJTbpv9rSgmZ207GdEd7rdZOB4LEyF2wbtRutWgVU5WBh9pLDOdMoGZHUT4vg7XNtA-f9cOdtn2BSC9SNbfQ8hIUjcbPZBA7D495hZCRLbpBSy-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی برای حمایت از بازسازی مناطق آسیب‌ دیده در سیرا اوئیسته مادرید، 80 هزار یورو کمک کرد.
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102694" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102693">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vkl7xplfnnU4vEh-usfymiwDjk1ajHh4xpOUhX2eQ4clYOoCk4pj8ObP44DCIfB3PUf5swqZmKg203MgV1ZwEuCWlqAy0n076ZGwyUWXd6lLHSoVY4YCf1kWl11ae0Cu1622JXY0WPedG_8BdUl22drTyOlYowlD_n6nv-jlQlQFd_DAML0o36Wgd759cYpGLui3jY4QE8YZty3laAF2h6lRZx3sCE7H7i_9BekkDfGA1EHU1DWA4rcWskdywmH11fPWKsruT5trhgCatSHQ__a97BN87sj4kkk-ntxJ1JUAqqMxj2d3YtJPwM1uWt-Sizc5mxprDBh-IzV36gHM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
هروه‌رنار سرمربی تیم‌ملی ساحل‌عاج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102693" target="_blank">📅 18:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102692">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=goBBM5eLIKiybcsYKa8RA5UgzeQ9IA9EeKyydSgJGqsGgXtkPLIVwZJxlIgGHqudtIkXH8pR6NN9Whyqywo8va9j37NciJvbYVpi-UdfdeK1Lujs0n43SPUvd0bJy2W37Y2iTx6VKgMD0IE2b9UqAkgtZXfb24ggJ2TWZstDdHqxNzpOF3pU9_lspM3tvn5ZRFP7xV_4hs5ysuSYA0LKxcwn1ibk_-v8gGBlNpQDXsryizPc1giIqyAtDTX_X2vJa0xF4ZTSZoYHvf2i8MQN6RzgqSlAKTgsuN1IGJ3IurXLmliSJiUk9U6kYG3XOnl_XgBUyvJs4OaTeGQBi-ts9iDC9GKG-kHy1nz9ac-c6KoNVviOmP294nNXwz8k7aOThWb9cIMGyJIb2KCxesO1kCpmfyyhC3Kqir06gHfQVeUtKT7oj0WUD-hiv1td8KVcYElKvJADfJKgPTOGt2Re0y7HLnnBZly-typKbV_mpa0CuJ45Aiws9z5NnR7J-4HbvHSTr0TKaEs9a4L-3lV0OEuNDrr5xMcDt9dq6qY4sQpY0btQsWK9d9gJzuaFb1b2EJeM6aJ-sOlJC-K4QLKbJimSpkNXCsSskjYhKJoKswRIo7eeg2Ho9gYW0EIKGmpX9Z4CiVj-7CDeCXhKkhdsG93sfDTRGu1VOWH1AaWyUjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=goBBM5eLIKiybcsYKa8RA5UgzeQ9IA9EeKyydSgJGqsGgXtkPLIVwZJxlIgGHqudtIkXH8pR6NN9Whyqywo8va9j37NciJvbYVpi-UdfdeK1Lujs0n43SPUvd0bJy2W37Y2iTx6VKgMD0IE2b9UqAkgtZXfb24ggJ2TWZstDdHqxNzpOF3pU9_lspM3tvn5ZRFP7xV_4hs5ysuSYA0LKxcwn1ibk_-v8gGBlNpQDXsryizPc1giIqyAtDTX_X2vJa0xF4ZTSZoYHvf2i8MQN6RzgqSlAKTgsuN1IGJ3IurXLmliSJiUk9U6kYG3XOnl_XgBUyvJs4OaTeGQBi-ts9iDC9GKG-kHy1nz9ac-c6KoNVviOmP294nNXwz8k7aOThWb9cIMGyJIb2KCxesO1kCpmfyyhC3Kqir06gHfQVeUtKT7oj0WUD-hiv1td8KVcYElKvJADfJKgPTOGt2Re0y7HLnnBZly-typKbV_mpa0CuJ45Aiws9z5NnR7J-4HbvHSTr0TKaEs9a4L-3lV0OEuNDrr5xMcDt9dq6qY4sQpY0btQsWK9d9gJzuaFb1b2EJeM6aJ-sOlJC-K4QLKbJimSpkNXCsSskjYhKJoKswRIo7eeg2Ho9gYW0EIKGmpX9Z4CiVj-7CDeCXhKkhdsG93sfDTRGu1VOWH1AaWyUjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📅
شش سال پیش در همچین روزی ایکر کاسیاس از فوتبال حرفه‌ای خداحافظی کرد.
"عده ای برای پر کردن زمین می‌آیند٬ عده ای برای تاریخ"
⚪️
🔺
ایکر کاسیاس از دسته ی دومی هاست٬ خیابان ها هرگز ایکر مقدس٬ یکی از بهترین گلر های تمام دوران رو فراموش نخواهند کرد :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102692" target="_blank">📅 18:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102691">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5e14ddfd.mp4?token=u8PdoRKu1vlB2ksvixwfetuGqsKE0bkcyTmIELhqquwVzqqhp99BM3AYREPyKa2T1WZCa0u2GoshLjrnISL0ogkD-hgfzOW3wG2C0vCA3jXnv7ifb37HtmCqlQFxwBtYGMdzqHQw_QKLnDewrpx1_iqbn5_kBQE-MKbAZcJZzHYeZDR1s0dQyTxVs3nZKhf7pvdv6c_dO5bwYBtbBFqBuzuTpdfdb099yNt2vmdtVPKatkNnHkHei4fETe33FfRNuBQWO2QgoQeEiAPuIo0Ue9AQy2wMG96PHhhm7C6-JVmWmAPsYdmpKfHM0m_OhIJjwG1T8LPO0C4G7Yw66D-BlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5e14ddfd.mp4?token=u8PdoRKu1vlB2ksvixwfetuGqsKE0bkcyTmIELhqquwVzqqhp99BM3AYREPyKa2T1WZCa0u2GoshLjrnISL0ogkD-hgfzOW3wG2C0vCA3jXnv7ifb37HtmCqlQFxwBtYGMdzqHQw_QKLnDewrpx1_iqbn5_kBQE-MKbAZcJZzHYeZDR1s0dQyTxVs3nZKhf7pvdv6c_dO5bwYBtbBFqBuzuTpdfdb099yNt2vmdtVPKatkNnHkHei4fETe33FfRNuBQWO2QgoQeEiAPuIo0Ue9AQy2wMG96PHhhm7C6-JVmWmAPsYdmpKfHM0m_OhIJjwG1T8LPO0C4G7Yw66D-BlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
#نوستالژی
؛ دیدار فرزند رونالدو با مسی فوق ستاره فوتبال جهان در حاشیه مراسم توپ‌طلا سال ۲۰۱۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102691" target="_blank">📅 18:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102690">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W33MTJXRHHERU0_DdsseIAtkNnsUmTRBKrt_xS09zvoz28Gbbww3btmyo0QD4SJb4Tm5OSmk9p7WJFLnMjbSsbg5xVjS8jFxMiQ2GbKOHJ9IftHq5aQ8vMYetes2_KNCH7KcuHdcnY4ZSnfm3APWMmjcYdXRKgC26YoKSIa7W1OTaDY7tKOzMr-Pdxf_Ap1w7kZLR-8HhccFovQJi4h357tmc4G3TW2yhKNwzKwUPimW8_i8iINdP7cbcvtKkgKlhb1ymsJZXOwojVeGpz0Eym-JNOK_Aq0jvvtVAHgXcT2NEiDY1_ZGdAzukMfz-maplAMn_TYPATbcJt5PTgFPzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بازیکن سال 2003 آفریقا: ساموئل اتوئو
🟢
بازیکن سال 2004 آفریقا: ساموئل اتوئو
🟢
بازیکن سال 2005 آفریقا: ساموئلاتوئو
🟠
بازیکن سال 2006 آفریقا: دیدیه دروگبا
🟠
بازیکن سال 2009 آفریقا: دیدیه دروگبا
🟢
بازیکن سال 2010 آفریقا: ساموئل اتوئو
🟢
بهترین گلزن ساحل عاج: دیدیه دروگبا.
🟠
بهترین گلزن کامرون: ساموئل اتوئو.
✨
بزرگترین مهاجمان تاریخ آفریقا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102690" target="_blank">📅 17:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102689">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
⭕️
🇺🇸
روبیو وزیر خارجه آمریکا: مذاکرات بسیار خوبی برای بازگشایی تنگه هرمز در جریان است و احتمالا امشب یا فردا یک بیانیه مشترک صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102689" target="_blank">📅 17:35 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
