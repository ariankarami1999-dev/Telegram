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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 20:29:14</div>
<hr>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9U_06HzaKfbF-jPj1fOEKxIuXGivRBEYRVVMg4ugNSmp-0ba9hVOw0Ze9l0yYmL_io5h9xSYmsD8hjQWZ61LKkX_yjNA28WSCZuab9y3nxT6AKFbqOiTpxRLh_DZhCIemIExqGmh5q1o8s0Wokiak9ETxH8eamuugEw-LXCwpBndY-bQuc57KgcWwoC2o8WQXjg1Zui_06cmN9R9yva7xYrTQTsJl1fPAtHXECoLQrpqNnxeaBi-XWyofUzBXo8Ocj37pO6Nf86jTH4UoEo5vw3TVIInpqT1rfd0btdEL0ZLxksO7HkHQvJdOuZIriNPducqvYDFA-yGWKX6-1zhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#نقل‌وانتقالات|ادعای اسپورت: آرن اسلات بعداز بر کناری از تیم لیورپول به گزینه اصلی هدایت باشگاه آث میلان تبدیل شده و مذاکرات بین این سر مربی و سران روسونری بزودی شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22839" target="_blank">📅 19:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BatfYXnhMi-JPzR743Hxk4PHT92oglrP_CCHJHIU0R0LNfE2XxuEwAVGdel6I3BhMreZKH9V-4StnbXkZdI2NwwZ4hatadMmbHHCt_qBTRbRq6yLU08PKxqzcMpQx7QxRcFO1drNugMGPRd1x6bPh-Ntm9tzsKVQKIKhWVT9xC7NNFwol-ZFj5GUiRx3vv3OpxcRHghQT2b0ajWJ9cPWPmg_ndTWrJt3lo74Ew-Zmo33vM79udINJXOXW4SKsXyb5S_nPsaph92T0WGuZIYmDcR7dpQ80KCca4Z9Zb6mpl75o4w_gLEN__AYvVLdlZb8xRcqRkQdyhNIsjhvUiOgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22838" target="_blank">📅 19:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1CxXafY90W-N-U6R5jwd5-Q0irGmLPceZHsQ9QAVMlPyO9xFRaLc6hizP9qzyn4h47StXYqi2k88EcVQvLlr2jowYuu0XeWcXwjGrwu0MzXZD6Ynvz1DG_HsDEG0prjvxD71OPwht5HQ8vTipTfIPrLdLkQd4-a1co6aguJ4W6a5Cpq_TEm-SyYYPZqSXBMr1WZdYhMlBK4eRDllMunCTfsV4mzXDEmrX0846dgkF_7U3Z793yuNnIFhLFuYltRqY3DTZ1B3POoVXuZnm2jgIBA-SLHwn9tAef_mitosLejyoPA7Nkpd5jZqafpJtAigxJRgjqWRkbPCC9eYCLiGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=VeDfgVLQwMNzSbSSa2lUPwsEW_eHGhpERZDCfr7Kh1HD5C2IplZ6Acd941eMlu1v52ZA2LY6NpHUW_q1IJ1We3hv8b4f5xzPJAAYmHCjzlvtY7wAfWt3bCy_e6ISeCmb3w1A0I-EmHetimONr_98u6jZECm1xoyL1IirvpHuXXQZdsjo5UQ2hWFoDj52NECTyFDEV7MaES7IGZgpuzjWPj3_jFs9vYcWH7JESwjPkVDtV5Qv-8ohogJWusELGGKuEXRwOQaLDZkz2E3q6deEd3Lz9_IcmXzoITr3X2iJAJK_fsdEZZcx_SEBeHcz8tUFQP3QOq4f-UhVpvGAFwUP1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=VeDfgVLQwMNzSbSSa2lUPwsEW_eHGhpERZDCfr7Kh1HD5C2IplZ6Acd941eMlu1v52ZA2LY6NpHUW_q1IJ1We3hv8b4f5xzPJAAYmHCjzlvtY7wAfWt3bCy_e6ISeCmb3w1A0I-EmHetimONr_98u6jZECm1xoyL1IirvpHuXXQZdsjo5UQ2hWFoDj52NECTyFDEV7MaES7IGZgpuzjWPj3_jFs9vYcWH7JESwjPkVDtV5Qv-8ohogJWusELGGKuEXRwOQaLDZkz2E3q6deEd3Lz9_IcmXzoITr3X2iJAJK_fsdEZZcx_SEBeHcz8tUFQP3QOq4f-UhVpvGAFwUP1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارلینگ هالند جدیدا تکثیر شده؛ نسخه هالند جونیور، نسخه هالند پیر، نسخه هالند دختر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22836" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_3AKvuSEttRpiW6ILxrhbz_tRQTdoAxFgqq9YUQh2_a3g_Uw8jHR2eKzbdpLgMFqp4cMJ4gg7kaNDWip3KEu31CN3Szgx_FOdBDauF4R4Man1FHlSWZbd5Jf4CqivvimKc-Cs71xqg1G1PxwCEEgMXn47BltbV-KOj1gmSVfikSdgIJGJQOX7zTTNqzIbek29XZ4RDT_LcT2DY4yAMuduxukM-0zU9T4vFfa9G5ezK2J5KBfEEGzDIc3ByXlG0FKcfjJTRSnno6FSj0DRQzl0vR_YDSjdeV8CqNkpGooEZiH1jSmylv21H1D5OWAXncyjjb5CU_JNHrz0rbiFY0pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22835" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22834">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYQR5m36ZCyUzi1CZ-jr3PnJvIxuj2IBbkZkFeL7tEGekPECUxNmXAJLvV1QlX0ZVPgSNKjibqx3Lx2PjUN7xWxsxDZEAfCRsDpK3IsBKR2Uk4xjy1ymckdlU8rEbPcrcubRsQ6oldmYsf4i2Hv6XKPf17V0nIQESDXn4830WWpqVssyWnHqBN_2LMcYxJXtTVgNmoR02HZpmLs5cru6aTJu6hDHSNbgXQo_RcogoIluVmyROhG3Op0t58BuQ2p2tacArh8Fp0KiD4q7cGe4cZqpq54l7YEl84hSl2YciIhAQl08qmvBdRYhLuqW1DKe9R6oOptT0qYzDUxvYdP7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
15
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/22834" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijoAa2n8dEFS2RLO7ClDU_n-ozNwtNhM6f4L1BYpey50RqkbztEmdiPGbt00sk4FELiJsD9WL5IJ8Mn2ijxXVTFZ6-ysdjIU8ckDY5f59dsy-l3ZmQ5NdMC6ppV96delNrZIiqCmkIW4l9xBcQm8X2JHyCzzhS6jMcytuLrWS3f7OacpcAxhuvCrmhViynqjZOzw2Oxg_SdpUsmSQ69N4ZEqQCRmcHdENzw-fO_JWYuPqwq1IvPxOy2_REvVz9lsstoJMr15z7ff2f_GxdaKjUEhswE_APDPMCpbd-WIZXjcfcDrqK-V-1DiyyO_F4jINXdAVodXTPzNj1XXAmDjIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا محمد دستیار تارتار در گل‌گهر: باشگاه پرسپولیس باتارتارمذاکره‌کرده واگر اوسمار برنگردد تارتار سرمربی می‌شود! او می‌تواند تیم پرسپولیس راقهرمان کند! باید چه کند تا سرمربی شود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/22833" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE3hFsPmyGp-nfrFVHJ8n1rHIqo6g5bq6nC_fGqJPWcdhpFIlN_ZBrO9aDB9ufAAAIlzS2U52y8DgIcftcxYn4UWB-qFg_231dj1wKNo7D-L4Rtd03nysVukYq9Thg2oVVJmiqzvyY_l0RPXI6uqP-YrkwkzZ1gTuqiBPoGjlm547Nju3Cc7gBzvH5xJBetNWN7qS5ufSM_kcl9cL6-yr8eDwbGpFiSKCZo19BFx-L3SNFIpJyrd4g5NuyZIhcyUsPlpy-HwQTqemTPiKc2ZPhclnztLyCNuZXQFGsygy5XlbZ0GtcsUsrgSG7i8RqSCV8OnKCx6YgePPpWfjm0xGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22832" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG9Wd7ulGCBm7wIvWZkHPQabOhkIizA7TfoSZatjXW2IV8C9x-941WKFTUldX-lDBwrP9XTXrTus3XdGIPnkEgx3YYtUXpnq3BIbHdwa-BKUOUTOtEzuBcr6pZGmLJAsJ7u1vz1xbbCzlnpOKvw5ZfT5zYVR_3Wl1XXlFennYza-dfbXQdmutKT_Jai5XRhA7LzZYM0tOzbl-kX3UH_xjJJuiB1ijZiIZrRMCWoIpexvWGEcnClAhw2eGUqsPZ96nvQ3UXxgeTdzQKsdTGlV1FGJK-YjvIkP2n2wkoT4LsMcYoWIPSLKgwEPXdLLyM_1dTRgy3ZFVNOcbizFSRfliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛‌خوزه‌فلیکس‌دیاز:طبق اطلاعاتی که بدست آورد مطمئن‌شدم‌که‌منظور فلورنتینو پرز همون مایکل اولیسه وینگر فرانسوی‌بایرن‌مونیخه و روز سه شنبه پیش رو آفر 150 میلیون یورویی خود را تقدیم سران باشگاه بایرن مونیخ خواهد کرد. خودِ اولیسه هم در جریانه که پرز میخواد…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/22831" target="_blank">📅 17:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNxtcBYlq-ELsdT731GzdXyPSIZe8Sc1CToVICoc9RDusXKIR-LDgV6OAm_ZBTnJQuGgKynmh9zg7gd8vie9ZdzzMN--wuIpMvNwA9LHTWoQCFsD0Rxw_pRa3WJV8cvuQvRqGE1Vl46IhQunyAh8Va-YExS80aVUwY_Fkk67LiKQwHOJE_0QVlrGwan7aWji572uIUMthCg4mvD6_RhPvyNY50nmv1jbF-tQYnxarLXyI9Xq9OGyEQaObeljgkZ4qDtC7Zzn8IertpuxCwsEp8F6lWkbg8zHHP4-HRIQ1AGcwM3DdnT4ZLJJBqPfGXxELo-1IMqXI6TQl88wXyNfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خوزه فلیکس دیاز: علی رغم تکذیبیه شب‌گذشته فلورنتینو پرز؛ باشگاه رئال مادرید بشدت علاقمند به پیوستن مایکل اولیسه به این تیم است و قطعا در این تابستان برای جذبش تلاش خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22830" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/22829" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6qkZaSKlI38vCC_C0TKps5yb5OqgxMFAuoSKzRXm2BUVE5r9GBuxMV9zv28wyHIqFQqLc85dgwjQa-7jtlJLHExiAg9KuDeCbY8J0GXWoooNIpcR3yNYT6fqB0I7DiSa-0g1e4-cznephyYGYwwOSbPqpdn9o2EDHYw_sRN-eqDi0DfKMDIpADcO9rUa75DTveIMnz1JEEbBppsRPyOPqLYdEiWPAUdfCA_SwB_vLpxo01f2hG2Y__sSYDivhkrBb3lvHEqVfSb3NR40wSoJ7cshi5aVUc_kp_qoNUdU9jkPjQY320yQPSkY2qo6EQMBF-kOveOmgyF4Q1B9JPd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/22828" target="_blank">📅 16:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBQoog96Hjsl6IhJqKM6bQ2Mw_zS_R9KeNpr4bMokawatBgHNaCBQ4Wnnloo5-9tgmBGQ_w32Ihw6RawqCCrqGPOy3l9D9mxyG5DWugo804FsiyaHcqa01Wa-dDjV-y1rEoUmM5bZHpz0avaPZWeYLmQdgC4hX0IrWj-vddptnUNg8DO3EJD3Ij8aX-MkKhxa4WpA--03I4080irtaSEdae_VlC7udZflu0vspqvx3Se6lIPzqRya2I0IfiLxVNGVINKlGBdRhdc55d7BSylyswEyA9qm7Mzbq79JD5q87T3BdQKTwDm3nEUve3wtIi2IhnEo2rLR-ru_FfvAcugzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/22827" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22826" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22825">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLkW_Ku4GGJRCN8ObjzFcJagdBOycFc8s-RPilrEotu-sInHI4CBH98gIQ42lEDO3mFJ1fvqx8s3dUE11yxzfWXfEIQjJj3vpQZKl2-aKLujT7mBf6k074-gVpsPPbUVg84XY__8X0I3UlJhTx8vV1TzjtCdCQCv8cXUBubB-Hz6Coa8NbOtjXOwDg3recsVkiFNoUT9-zZfki72Ssnl2wMuAHEQ-VbYvzH6euc6zNwTwiCLluTMCNhlfuMgW2ox-oQN4NmMzWZGfRaW1aWKGG4YUvzhO2sxw1PGkpP_FXzZK4J46GceGWAXbNyvaXpQc6dZauNJkf3MjJDZw9wlNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل هفته سوم رقابت‌های جام جهانی؛ از روز 3 تیرماه هفته سوم شروع میشه تا 7 تیرماه‌‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22825" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSXqovbSPHInvyr0AbfW6nlR9D5p9XWFrAB5TmHm84aOtZ2maA-xXks00vmwqqElGlkpk7V-CPkKZfL1udySzunGW0HktjbxOM0Tq5qwr86Xfg8BjaNS7g3I89onH3Gib-GveQYPBlZQYj8hjwkxOhVftX8Q3ywsO8vAmO3gEIK7dhZTJCOji9c-snGuI_RssdqxZSBZCyBF4hVA8fHbIZR6Mcdwq97IQ5I1USO50FSQjUFPH1nwb7QC1GZ-uy41NUDACO7_LwAxB8NnewtiTN4NtfkyhXibnOgMvUBB3aVKgS_noLhiyjSghXL2XfPhDwmkQnEiZUlgrR17LZFx9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نشریه‌ کوپه: رابطه فلورنتینو پرز و خورخه مندس ایجنت فوق‌ ستاره‌ها خوب شده و مندس به پرز گفته هر بازیکنی بخوای رو باشگاهش متقاعد میکنم. ایجنت ویتینا و نوس همین مندسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22824" target="_blank">📅 15:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUlTqLkCFsKe39hHDOGyFmLD-WvmYlYJoQaTxNehfrEhM9YsDlD3OAjNlxI4aZOxQZfJZpY51OKkb_iXNXKeXXkqe-4_HprEgVLAm7odJo3tIbJKuZqqokMJXxSXR2Mpt5gt6N0n__x9ANeKTHuB7fVaKnIca8KZut4FUXZvZpj-XNn1Ehk2MKCMMNNcjh3wJMbERKTImZtSCKAKjJ2DOawE_dtNXCF17P5G4c1FRH_gbP-SewmrPE4PqLJfGJBORLNntSHwHQVwqf8ljYTgqdt2HlVWLXGRxxGaz9amUfi9ukDutqk9bPVhvyF4aGvi-lA77sAa2w45swTVQdHfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22823" target="_blank">📅 14:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoxIbxpO63KOHbQ1lBw1gXafGYDzXfL8l7z-UyTH2ahSeoVBmy7k_uoaUfIauBQe3yYE_9c40xeVsj2Hhk33eAHf4PNVeAIUcbNOyhsBU3QO1i_TGDwsU1OZe1nR0XDEe0IOe8yDjVXFKZCS8IXgsPzbs_x0iE2srNARVrfc5hiyuPwGTahf2ob9yZecx9klIST79SdGt2YMGrBxzmZp0KskHWeIIisvIbNxUL89SVpaYBjiWUcJyhlfIY1dbUlKTo0K22XIuYV0-JfOb_hE3j9NKR2qka8gWY8jqm5qIurZ8NHInXKyu03NKdn_F2cLxCC4lwqSG3jyk4Dznh3svA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22822" target="_blank">📅 14:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22821" target="_blank">📅 14:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22820">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22820" target="_blank">📅 13:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpx5Ka55OW9YHQLCSKA2yWfYS86JGDwFjXhlgBPKgeZtu8Ttuwyeylhe5KM3vqzVRjIjphvAUNoSf2xCxf4VjnfKtz01ymEzBVAC7U9bHzb5FWBOUUGcPHFIZrZKH1b8z1cP8PO9-LBGO1z_VQUw3zIgIt0Hv0Y57TgyZryxokYy4zG98qy1RRY513jVzKLn0DrOD917pbkWguLDofoPfbFU8E_qgZEyDdZpOHQhGj3Xc3uR6g2rV8qCEAC_xuiDPBPosERErkWXu7YjZtbpXtL3Uha2ELRjAx_sR1jXJrd0BJ4Ss78aFUOmeFI-M-3PlDBYoqNRU6wY-wBgP2Vlzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
#تکمیلی؛ باشگاه پیکان قصد داره درصورت توافق‌ مالی باباشگاه‌روبین‌کازان، رضایت نامه کسری طاهری مهاجم19ساله و گلزن این‌باشگاه رو بگیره و درتابستان سال آینده با رقم بیشتری به سایر تیم‌های لیگ‌برتری‌بفروشه. رقم‌فعلی‌رضایت‌نامه کسری 800 هزار یورو از سوی باشگاه…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22819" target="_blank">📅 13:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22818" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGSe_yr7L8gtPF5O5UB8hiKzidkSEtP-rHAWxADSQsRf3RkRmpDGDbzmv7OA2m3TaauCY29ou79X31SKHDGeLLokViAvCoeboS7BklryKW657VLHWw1ZmAAZZeKAy8Y9oXLOUWfrl9JMexRnFhh3TqzvPpF8U5pLrPd0jT99sv0cSqsL1CI-zqWtoQwSoXCQefIuSZfjrlcIon-BP32aYbcrE-Qgd0HidSAURpow0eQVNSaFIT4YifK3brib49XONq4mDjNOGZ90g4E6uZw2zfyoJ_zx31ZNNcL_Pn635Uw3U_EPm7xR0JD-rMEKvDOze3c8-eIOEwolzaj_zxyLxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22817" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22815">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22815" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM8fKmQVyit-M49HFdlYRRdpqnfvrcM43-GEf-LrC8T-f1B8514NYQN0eVOeZKgXOfZILMJn2HMV9feLaLjt3bKccuKkp3Ro6leBq-9j41aASuix8L8AdfL6esTcNLVPkOAQGQ-geDgoYupHEKSilxLVweZpGrNVInOzifBLnqSa88hLfb9f-YxifNup1-L2fT47WF-KRWKHGGSOjLx0M6CCDZXN7Z7icpJ5BJnaYaHQPDndZJ3dIEiQlQn9NWjN7YHNglrFKBIuGLMM8aWnhOoMtCY-TEZgBQ3rUDBUlf8MWTuNkFG57hBFMULkAT8kWR08mYDB1dhn8jQfaRr-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22814" target="_blank">📅 11:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtK_YfCM9GsXk3BV42kPd-2YWk-TbUiz8GoQmjcs2jk7z3zVdA5XQK1szXPMWqkJinh9eZwDvx-BvWSfK0M-F1ZFgI6xV19c_CI11BEuYQN7dzUkQlN1EF7NRokr2uqZ0qiOZhH9I4WdMhXhWIHB2iOBDnMaCaiL0RrJQ7AjCK4tPZkgLiu98NFkiZhTF58eT5MR7hqvAFN1EfNvsQbuiSe4EATvx6nfHVEaS2XoleNlMrzHJznwEE51RGveu8kb-Hw8OFZmWWrpph70vjHSmdh4TW1k54ItYPIMqfPQvigEeA1nm7Gvv7-zDdgz1dXdlk3kTH4nAQd4dhjp8NtgDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت باز شدن پنجره نقل‌وانتقالاتی آبی‌ها؛ باشگاه استقلال برای فصل آتی رقابت‌ها برنامه‌ای برای تمدید قرارداد آنتونیوآدان گلر39 ساله‌خودندارند و سنگربان سابق رئال‌مادرید از جمع آبی پوشان جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22813" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THJbLlHRowettdNq3jQKR39M0u3SH4wMIBjp1-ECbIOGVYlnyLRiCXpWI1AsSJhdQZF1oZSm6Bt_jCntGRZTG55qvc9njZhYJUnLa7q84yYmql1UIaaGQTh9tJdDlXBxTtyO5V7AF7eSKXxwj_4nTVmO_NZg09F6HJxQygkk6sfndnwRaTD2ICB2AO80jlZc7l69VVy9ksS38FsKwAhB0tGJmFYySC_s7moU3vdt04wEp6R_B6U1tBgEQNwqJl1V_MaMxJG-9ts1AzGgNe7saprmSCymRl9zxru6iztCBD89P8o7wmfUuW4-UX2CnJXYGciKRLkcDOLmv3PmHNEDwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
👤
طبق شنیده‌های رسانه پرشیانا؛ سروش رفیعی هافبک 35 ساله‌تیم پرسپولیس که بازیکن آزاد بشمار می‌آید از دوباشگاه‌فولاد خوزستان و ذوب آهن اصفهان افر دریافت کرده. درصورت ماندن اوسمار در پرسپولیس قرارداد سروش با سرخ‌ها تمدید نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22812" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22811">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22811" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcmL1slTDAoSIQcOEA_BeN889ocNz4frm-twDHD0IlBc3Mkc52ozW3wsRFTLDuScPewjK_qAdfjRRrsymBTrjVAbGadXVzdRW7SxiIxlPxJnKadZE19jTxuUJQXKMnPawCcoAR4uu99t4qrlKlMhBXGZTA-GOKvB9bZYdJZLlgGv09m2PMHGH4kZX6B_9Bgud6tb9Pd37RW8AiazQU281tgTQOM6eBGEJPmABk4oFd6l4ucOudX1w0A_txC_us1721spEojV7-pXqu9rMiQChwyuftYFRON7fUJCXK3_l_PzASqeS2FUEDlx8cP8_0i14vR3AVjhSeGLzjAxSokaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22810" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD5mXfJhOfPlHVYJcBrno6qn9MLQPnVkAmAB9V3bMklPOp9WzcGb61Hn3LhqdzeocSCV8nnoFJ2euBopTrB7l9HCtiW-c4ES1Zg1uwC-WhYcg19-_bKHlqjf2I4e_ixmR74JPpAao0HWCKPW0ZBEsrK_CrWcXWJ5nML148Rj8vtFjuW1JIBFAXbF6UQza7h9C2beievijPron2WENiLW7IYeWRpgsEpT7TH7fDonMUkvId5oyQzJeXc5zflGjelmytTq3edUxzj8cdxXM9b_48TJCdsF41VF_PPVxeS2vDmvPFhSCrECEKs60VtaC8MPSJlE4vWadBOWt0-wGeBQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شماتیک ترکیب تیم منتخب فوق ستاره‌هایی که مفت جام جهانی 2026 آمریکا رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22809" target="_blank">📅 10:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22808">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uui6c-736e_R2K__bicd6yPoSkmNbxQNOskWLZQMSWxwKZiZnGZX-34MKK6JVFbU3sIj3_8CHxq-8yeowV9QgSJX_zNTuO7xb4FybIBF9ve-6QSB6lfcGkvlFSvogBm4bKFkYE9T9pxK0oQiXaMUkugcAX-IF_F94sMXMGyUZwGW16Di_o5APeMG5C0wSxvsw6X9uu_W7CwkOjQAvQr6s9h25Sl3l2K0BWg4hrluREDKLBC_sXH3oQphzXnk99ZemT7VRWaNiZxoEVCcFFdn8gYtVo54emhK-u7aQMSRid2UE7VqdiaCglfhYkpnb9Uu-2_0XT_Dh7GSGD5jSAMcFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22808" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1n-XJRAuopI_ppvWLDhKXCjYXG228IvBK0gsv-KiT0Tz9AgKQRNqgEevCT0mEaD4GWMQQFwFE4uJXl-IxzPdrnoZzBmoo8aYgmicw22rf3UTq98aslbcUesXgOMzsY67oVK6SMMBBn25zI6ZpPrPUqSo1wtVhIaRHwXllb_nq3eMYKk2Ghv-631H_e36OvmMjETwBhw2tgalizmqgZYveFgdCxr5nwzwuMjOGfBYA3EGhSOLN0alFeNOBQieLh-wPUPlvveyOMr9wxloW6vM6XCNdpLECU3qy-zeM6YuWEUn89HZYkHpoAbO2-HE1_Awru3iAubdKd0isMFOVFS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMbFNnOY13US0MfjIzLB7zS-y7MHt8TYpTeRzA2HaGS00IG1Dn6bd4T3-rpH3oL3HA5xQk1OVK__0lyPFf8HtaD85Df1RrboB2vVd_dlrgOfN_y8zheNo5kXCMgmABz722B-YFGq5l0tgPtAG_CAgiZXhGvk3LDfReQpAOlU2TN_UIIPLRE7wAQMOpe0e6aTE_KsXI6y4xX0cgIZ2EjzsjkfZAGf1OuLlKP4hp2O7IqGOlk6YTtqpJb3acYueAI91JZr1NsU1HLpNqhB-WlHOypOjp7iIt8P3QHZkh3qTHoOPk5ClUZ23_XcdcykYPPVeG21afyrOgPkLel5KiiSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo6tGIHDxDZQiOXSYa615zf-EcBUpgOUXisVB6aTyGIRUZ12XDDyh00ddMmGYov6iNP9qAf9nRuAjNgJwzwHFSlE-tFfnq_yHfhQ-wJ3syn15H1ap8J2Ezb1laMuSOJCkmXQhiNYR3ST6hAG2zNDViyj2rj2e0X6her6ucN2jJBjt8lBCHPxbh4iwt1TjykoPGzqcgNqvJq7nH3kKqNUDTt9Mn6b5CVqvTVcL89gqvbR1_IYiyHwPb-B0ThkP23bgSnOjapSeD_2uI2MvpFO8QCQrYNjJ-5KZvz5cw8RQ_rbv3-Ry6-yfDt7BXlnCdNl22vDTF2g-_vnWwBaSRki8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTfYhERNlQo_48JnGMB38Ym4LHr9uIRfnv2_GgTXVUsNL5WXgpojte5LPg-TcbXcz8Yu6bnddbBdU3YWAI6Oid1w7i8p-XRZiLv6oOTxlPUEVZXHRoDfFOPDARkOhTxKN71kXcX4XtgsdE3OLtJyAQkV0OlRuKilnTjH3Pgfm8RCsUzhK2V_D_sJmefa07HA5ffR2jFOLj5E3mNqpIaIoCX00-hPwBGlxlN0aqPzeWh4vg1XdEAV6Rn0K7Fux3y7ChtV9wmO-iA6pK5YMLQ1cjYckjsJHPq5KbyJwpJ0XX5gjSL3IpsIYXs3rChlSCuFttHSCJCr6kOZ8j2-fEpU1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgpAVBh-87OYR1chUbEVnFbpPZcRQFgEcE6CSWIaCIOUSPLRtefAUR-SvCVrt2wZ4_VtRSoyVQQJ1COeMi_DpfZloMeKEC0hWwMD3jUbEHnvIEO5Lmf3mmFWdvw1jnZeprgzPshO7eGGXsLDanrJey5Dl-hNs28GzSFyCQfJX-Ec6FXEmWZXoCtIHkaQYWWRGXNr12r0F0IhjBT73uMMLEGM1vepmk6jJg-JL4XaFzQOHo6vIZmVX4OSZnk-t87cIjseAvD4LiaGKhc9J8WrJdK3H5X5DphVXZhAbsgjarmsAAEcM6i_9D00u3ttWEtBF_EnL2-IKmSNSr2Wu5JSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22801">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnQhgOIEs9kyc3zI5SyHl48sK3nlHGBGDWXRE1TQZdBLEkiCM_T5MBYwPC9cvYy1GLntj1SE2v2jVzUL1aq9dXayWa10zdaYnSBoQUiThhX-iw3_qm4kWY6hoRfXqDvs2-Lfb0wZn0tAAsCUxjwcPe4ue4_mbSqN4xIaO2gbLEP7-8AMwrKJcKg-M66ANK3E6FzLOM_e2eHkYe7vRbI-ppcYGp_MlLCN5Z3LyqgGl8-z94ABAttZKMioakdF5DdiXxc9vAp5uXaWT4WASTn25uRY9lCCoom2CpZ9donpDSQfgCF4UtmzpUNp0AXbpS74ZBzhOY5tK8xY8SbUS3hCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینوپرز رئیس‌باشگاه‌رئال مادرید: روز سه شنبه برای‌خریدیک‌هافبک از یکی از تیم های لیگ قهرمانان‌اروپا پیشنهادی 150 میلیون‌یورویی خواهم دادم. کیفیت‌این بازیکن بشدت بالاست و بارها علاقه خود را برای پیوستن به رئال مادرید نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22801" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22800">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=cFxn4Ii_1mT15xZNemAg4DLQ-rr-0yIyHsgUfnwmBnZFj0De-xe8ZWhTMrcis4Q5wVM9eJ1exdadReNcBwNsSl8NH_McgMUrmLeGvTiXnH_IbJa5QHB8VM2q0LQLY6Z9sm_b2WhDVldfM8kccha2GaNOZR1OvYc5VsxRe8AES_FRBzXnD3pAkoAsVfArQ9SO6HMiPO69veRSwi8dnJVzYqu5usohMHcUaefors8D88j5yLJXwegyy-J_ImKRvkdScPPB0_lgS9ghcDUOY0QAq2hE9KbJSW5paekMUiDdn3IWtyl5Ce37_K_NxVEOWkSyebVKx9ygyyNNp4TLSstC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=cFxn4Ii_1mT15xZNemAg4DLQ-rr-0yIyHsgUfnwmBnZFj0De-xe8ZWhTMrcis4Q5wVM9eJ1exdadReNcBwNsSl8NH_McgMUrmLeGvTiXnH_IbJa5QHB8VM2q0LQLY6Z9sm_b2WhDVldfM8kccha2GaNOZR1OvYc5VsxRe8AES_FRBzXnD3pAkoAsVfArQ9SO6HMiPO69veRSwi8dnJVzYqu5usohMHcUaefors8D88j5yLJXwegyy-J_ImKRvkdScPPB0_lgS9ghcDUOY0QAq2hE9KbJSW5paekMUiDdn3IWtyl5Ce37_K_NxVEOWkSyebVKx9ygyyNNp4TLSstC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22800" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22799">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qx-QA1RzRd4sdWBTfFUeJY8_RMbVKIRma4MAuMml65MwC3QvcbjxTs4j28xVJ8LztI36pftYBdNTdoX4D1Pyge-539ZXsSoM_pvW9UR_PwQlqijECI2AOzVBiVBIG2ibNvrSRG6dQnHdXK6KGoB32Fe3d4dgfjEQjuSliJf4HfpEuMQ7aRq3y1Y19n-SgemdZQdmK0gR2KBbqQV239qEyPKgl7WECYYOac5-mjQX3t95jmgHknGFWU7hvOEi1PXvcandiAv4tY23Ice8Jls7uRZ9W_Bu-x1uKAFGCS6aed9Y5YrT5Ub5s7s6ZWhqS5oiJ5JKhcWovY7FNglbv1vonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برخی از خبرنگاران اسپانیایی مدعی هستن که نام‌بزرگی‌که‌فلورنتینو پرز قصد داره بعنوان خرید جدید کهکشانی ها از آن نام ببره انزو فرناندزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22799" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22798">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=dkhVsiHKwfrR5d_bSim0vVXEaRIaiX1EWX9-_rf2fQ1BwYT9atRVjOCuQfhf7Xk2sscnoILcL9pqWeydjtK00mnbkzuNFFfr-0XQpHOIv5xkpcWfuVtFJDkKG1gDt_GmM-q6aoo4x4lT4wlESRsv-0D00RgHKTwgmw-Wmd3XRzSdFSiU4ooKHotp0U9wWicfZX5KFOg3PWnvhSBlv6yvZz27Gxa4N138OlclE8WrI7-p6dTFv_Yd_C3PqWG00vvjoR_O7xQJ3QUp7ZAk-zv_VmC3EfGZnf_9BpOzGe0ldcm6SP44T7Wh-PLHIypMMWSkjw81RAM3r1xMS9gpk29auA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=dkhVsiHKwfrR5d_bSim0vVXEaRIaiX1EWX9-_rf2fQ1BwYT9atRVjOCuQfhf7Xk2sscnoILcL9pqWeydjtK00mnbkzuNFFfr-0XQpHOIv5xkpcWfuVtFJDkKG1gDt_GmM-q6aoo4x4lT4wlESRsv-0D00RgHKTwgmw-Wmd3XRzSdFSiU4ooKHotp0U9wWicfZX5KFOg3PWnvhSBlv6yvZz27Gxa4N138OlclE8WrI7-p6dTFv_Yd_C3PqWG00vvjoR_O7xQJ3QUp7ZAk-zv_VmC3EfGZnf_9BpOzGe0ldcm6SP44T7Wh-PLHIypMMWSkjw81RAM3r1xMS9gpk29auA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون‌کره‌شمالی‌بخشی‌ازدیدار کیم جونگ اون رهبر این کشور باتیم‌‌فوتبال زنان کره منتشر کرده‌اند. دراین ویدیو بازیکنان دوتیم‌فوتبال زنان نا‌گو‌هیانگ و تیم‌ملی زیر ۱۷ سال دیده میشوند که هنگام قدردانی رهبر کره شمالی شادی می‌کنند و اشک می‌ریزند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22798" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlJY8d_DP7MHgNcCHuwjqbQVOiX8HXSXqM1fAVgsG44edMFHNTpgwKh91aGixwL1Wa_4cZ8ANtfkAzpF937_6XcFtgySTGpksNXlsOlslwEt6AFkntJiOnjW9rXqJ9lKEtFJpVQ790vr-Y3DWAUWoPgpeOovKOj4Y52snnEvX_9A8zdSAwxgQTXs2ZgxK4yIZ2YAmd1v2LwdLwLz93UIL-HM4VXj69WVfwsFR5yDjHSR2je8LvxuROcpLVc5pxnsqWwvtW9HC94BiPV_hUDMlLx1aAjiNJJs3lcQFo39x2cg66UZ6LQ-WvJt1kMMBJ2sGQ0K98INEwzzI2P6YvSsiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ نشریه کوپه: امشب فلورنتینو پرز میخواد یک خبر بسیار بزرگ رو اعلام کنه و ممکنه بسیاری از هواداران رئال مادرید سورپرایز بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22795" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⚽️
تیزر فوق‌خفن نایکی به مناسبت نزدیک شدن جام جهانی با حضور ستاره‌های فوتبال و سلبریتی ها
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22794" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22793">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fN8plYQ8a6woYQgfINTCdg7TqmWLbD2B-3F5mk5PnVbjSagQdlIvxXDQmDKrrHbGyH_AaE4wiZSPOxZ7kx3FX7VNgyQF_jPrm6sZqgxxLKezp2Jw-O03jqagzqhlnr2p0zVN6Y5dGcqhY1wqA8nSyAHmZbmCJo6EPt9HpYOB1rqQ7rQ20jLK2GWfRdN2Jn3DzIsES40j_zsY_PI-yok0VEJAwVctJJsmNXgmF2Q4W5ZsipEbida7LuyUfo4Ac7pVLKIlWTtDZg_h2Kg8bIQjn19fwjS0Fo4daKAvmo6u1KWJzXpqTfyUruUEJ1s8AjPU7duPtdQ0tASgYoJMNtm0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
با اعلام ایجنت مونیر الحدادی؛ ستاره مراکشی استقلال فصل‌آینده نیز دراین تیم موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22793" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22792">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXDseIj64GxyCqtYAMygi7HbsTdjcXJyzgdP0zNoAZLgjp4x-i1hWxZ031HdfuHA_PAIqgSexEnvmQ36sos6hDv_ZB7rAc5XlpshhcWKfv7VhWTQiPRNURM508w_OLNLoRKaICMrE7WTwxXlIpm_X71rRVgDVR5CxUMU7xXRhYh-2v0IBgnRBU_cYRLy0krZfJHxljxBOr5hWwkirxdfHHrSs7YAAr7HH05vT1UZlqluuhr9RDfMMClRNsvjtutn1wqFZ41zp1ZLFLE7_VV-__j2Jt0oz1-l_pjxf3QkIfIaLG3NQQEI48JbtDgoSYZJzpBFrDxyiKO0pI9oJtdUdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22792" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6Vfed7dUD71uR78lW0KU2_BOrI5G4dSGtvHpK7Da9nI1K1h3jE53kKPEG6tkFCUyicnzGh1iGo7kziLLWD0Ayps37ZDTT_DTIi-ns-b4x2Y6t8KoHGgf9I56824r-NbBuTtmM1MYpiXkpJcpmoLwI9Hbf0kaF7UgYFGgNgcedPAZWG7-U9mTo1EB4R8xQY0kBcg4lKlew9iAGc_v9xa0E3zJrIgEaSl6134NLXhP7-G6MlRZAMJZWfHMszTzbQBsszP8fo6BAny4EOqHEI4LRBUrZ7uz7EJI7BCr97JpilaxepVCM0sH4VkRIMhSO_qNIGgN-C5Spz_diJdG36GZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین تیم‌ های تاریخ رقابت‌های جام جهانی؛
برزیل با اختلاف در صدر جدول تاریخ این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22791" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCHE5qv5ezEK0GU1gnTZqkbk77alBMkWjjAWGx8MPrW6MLd8qv17LExtoq3TcpiTCzuQ7anhrmDFwES41gKvATdafqYZKq2c7-8p1lUnKNPqtnBFzrTGtBxaMQ5Gt_rqLb6pDYOQKpqHtWldgqaRzPXY2eBChGR_muddmqhgoi3xrOFua9064GkX4wCU1dYOhezFA6pi28WfRev7Lt0P0BY0kt2Qsdb03yhqXJxVwv0I5LkHGK9r6CKbSblGcPfrh0rmbRVPJeAHNa7zzcwUnQNmC_zZa2BBNl6K77J8IYsmMLzfUcJuDvArdiO9xhwPGBf-ay2xcJ-t0qJy10NOOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLOMkGH_EqhnD7JVogEKTQQK1z6_s3eBSC2CSIGuHptE19343rekhHTPQblw4IwMNOrpSOWiVzKoR_5MgLVBk1vzVWhR7fa8omPgB5zkPN7AiWfB2On0Cf23urB8LKTPFGTGn-yHGeRStjmkY2HVDhg4GlrZXva2QVHMn9f1Cp0xl48KuZgacTAvC0RP3uMfDjgCmZy7q6DbkpfQLo0iBcrGBj94msL41LBzenJGGn27zmcJwIva7nUwb2PKHW9t9DWHVUy1N0pNH4VMCNJQQ86Yx2OK011t1dl3Hto7ZcQB11cSCaETFLYCXiX2XBmTeMiaXNMspDtgmyx7rdJ5Vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو: آندونی ایرائولا سرمربی 43 ساله اسپانیایی با عقد قراردادی 3 ساله رسما بعنوان سرمربی جدید باشگاه لیورپول انگلیس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22789" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22786">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_IUdfkSbzuiQp6C9z6JfZ3P88ctskpIiFbHA2YboB_a_kqjAZ7MWCMp9rTdCPpj0yDLlyI3udTChr2aajr5hDdaSY4PEYQ7MM6QvMLdYjI97ckL6gjlOoZai4nlbktFbLzZtuc41halvcMVNzp0f1V4--HBBLLk2vhBZ3cMD36VxOOADljBq-XYPWeauc7QAXBqOesJPi0vvLw7n5EllZiu7TVMFZczXZDCjMYD_NhHEnARxSx9hBnEcGgVHRppz2uZ6ExpTnJL7ggovuGjCYpWkRatLAnkmnGjSpyG4q1p6oNOMBX-g2mM0-VuFVinGkrrhCnIhqpZja21M6xmtLdbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_IUdfkSbzuiQp6C9z6JfZ3P88ctskpIiFbHA2YboB_a_kqjAZ7MWCMp9rTdCPpj0yDLlyI3udTChr2aajr5hDdaSY4PEYQ7MM6QvMLdYjI97ckL6gjlOoZai4nlbktFbLzZtuc41halvcMVNzp0f1V4--HBBLLk2vhBZ3cMD36VxOOADljBq-XYPWeauc7QAXBqOesJPi0vvLw7n5EllZiu7TVMFZczXZDCjMYD_NhHEnARxSx9hBnEcGgVHRppz2uZ6ExpTnJL7ggovuGjCYpWkRatLAnkmnGjSpyG4q1p6oNOMBX-g2mM0-VuFVinGkrrhCnIhqpZja21M6xmtLdbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بمناسبت شروع رقابت های جام جهانی؛
بخشی از صحبت‌های شکیرا خواننده مطرح این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22786" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22785">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=XqdVg3S7sXpgtBHvzzRpI4P8EaUmt6Pn0gUFbqZZ1EYE__zYitQhEm7twa4RbP_EkzycwzagGEx8rlMz65AiUXSnVbO16YP4ylB2xT-b6pyOWTBBly4mGC4rUysqQtFBHFIGSJGgCbdyYzWkncmyjlilBfrhJnNoRsN0ht3-c6Gr5LKykX9fcEWvlyIrOhDBtqiVpIMov3SOqTpGbeiWvPpq_b0C89qZmeoOg8xcNgdYi02QUGEVmD3JsZ9JSpaObB4aYZAMEfk2OKw1QsDcheQwounClOoO7IdamSz6rPUdrGu7aUP2IzrpK9afDo5cbkYxtvAHXenCIR7NEOEX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=XqdVg3S7sXpgtBHvzzRpI4P8EaUmt6Pn0gUFbqZZ1EYE__zYitQhEm7twa4RbP_EkzycwzagGEx8rlMz65AiUXSnVbO16YP4ylB2xT-b6pyOWTBBly4mGC4rUysqQtFBHFIGSJGgCbdyYzWkncmyjlilBfrhJnNoRsN0ht3-c6Gr5LKykX9fcEWvlyIrOhDBtqiVpIMov3SOqTpGbeiWvPpq_b0C89qZmeoOg8xcNgdYi02QUGEVmD3JsZ9JSpaObB4aYZAMEfk2OKw1QsDcheQwounClOoO7IdamSz6rPUdrGu7aUP2IzrpK9afDo5cbkYxtvAHXenCIR7NEOEX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
جمله‌ای که تمام راه‌های فرار رو بست؛
فکر کنم‌مهدی‌طارمی هم‌این‌ویدیو رو دیده بود که جوگیر شد و به میلاد محمدی گفت بره مقابل تیم ازبکستان پنالتی بزنه، که البته اون پنالتی‌اش رو خراب کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22785" target="_blank">📅 21:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAjsgiRH0ioFkK1gokrasBsXq6vXmh-uc5DAX84xc-GsQyPEQSlVdtDTQNnuxzmCtNKclrFbF_kWU9XiJxalBgGtwWxQJWSUE7uXq2VyqgM8Q28ynQ4e15PtG9UYIcBPLiJOWDYz6iyKs8rAAlUE09x43Cfvyw-a83pWTOMXKh53GN3aBb15IiIvBeUUorYn2fw4wmbHS30o3L9e01jb89B4Lrhhm02PJrdHK-xDw9q95V_zX4M4S2GL0InMaVbp2GXEUqHc9xiRlyZlhZGzTZW2y_LSnWJTljpZpkuLszQUpW5WFAFY2C5tKcMmKpGirxFaxnHBwcfAM1Q2D-PQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22784" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22782">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEixm9ztu4bx-Ue9fFnr8FpLeXV8C43dhIwQscxdfnHpmPUQbcpVUoOMczIfyhvz17lW-MIFEUabBGAZZcW4kZwutzw4aSHmGLxg9cZVjU-xP2MLsSKFY9bJgK4dC_SpP5KenYpXBANDZcZuef86xzDmr-7bCCGwhGUZ9NoiIpCt5b9gvIfnyuaO80Mp8CScc77cDdSqQROe9LiE8JTOwhmhRTOA_GfgPpG03moj5ZOjNTqEbcE661Lu-sku5S-ygDJFosPN-DJYkK19JilTr4YCbCq0ZVxBlSxXWHS4eaCi4FvQHNJ4oDR3BTO4SBTDzu2SeKW84b7gMMFmebsGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mgtgwyh30wajv-xypkWIMxkjii0W54jQl-HV0kpUxHTwBfLBQhSIG2wJ5sY_VQr_fCmAzYLBUtbUvCAK2SS4fR5lOZBmzfSanroqjE6v_7hIj8CKVn74TrAAzm3DAlhDG7vkXXUfQzAMskb586IevmmCQG7402db8_qPHTA_S3ZXkGCeIopD4SIadELjoDp9qJbTtQ2y2JOvvr6nc_7CgYRfp_1PWVqf_TJ2dgZ9H6GaX0gGIUmOzXwXY3Tb2w7JpvC6g6b2KK-hUUOys3Co3Q9QOIiydnkm57M4Na2YMVASCbOUs4soDBVwVZ5FWo222FFf63DELv1upHBarHtQzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22782" target="_blank">📅 21:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0eUgJgvgfKulGVAi_Nm86qJL1LXybNE2F48EnvKrljjYh7vdkRZ2OT5a_A5fhc2G17-_TE66tRx0oyeFQguAUXE7icHjfA_CsC1xD_u4Zb_l8sb9GG_s_15iO_V0XO4DZDP7cW_KUwqzj2KwhSjsjRKEmnmwDtwesmsHq3Lc3pxg8_qCual7w90pj87f1E4H3wM5f5qiDeFyD9Wy-uiUjx1-YadYL-s5v3QWWtLLkLnFYFzyzdS0-6wlSNMJAwkgOrge6fthU0wo_y2fAXAt7Kg9k00WeiKuh4L8BZ7107z_AUqPn4ioXYDY2DxtbAhdy55-JenhbLOE8g9A78sSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22781" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjZhAlsJ2vmYW-aooUhbVbvWDz3WYkZ0ijI84o-oUmK3UOdeK_r38LcCeNIxv1rQvgOgzIUi1c7effT6TywyRVA4tJpeBAqbcbAM1yLBkmqSmIEWuCWULQaaO2mer-R03hQFgXZWdczE4VEIYjRV2oao0Y7ZDMR8b_ft3v1gZfiX04GrlLonUsFxCYZBUf9sagwnSHP3kCwm1iMK4dETXihXm8RjO_-ohOvP3lh8omsFzUP7GLcPMI1kjJLp22rVseRXrkgVLoCFWYYg093Wd1oDv55tuTWnC3jnum7gMFZ2u_40cKK4zuEVikHVEQctEXf9hCesVeOalKMe7rMU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ ادرسون سیلوا هافبک برزیلی 26 ساله آتالانتا با عقد قراردادی چهار ساله رسما به منچستر یونایتد پیوست و جانشین کاسمیرو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22780" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚽️
اسپید با انتشار آهنگ جدیدش برای جام جهانی، هیجان بزرگ‌ترین رویداد فوتبالی را با انرژی همیشگی خودش ترکیب کرده. اسپید که سال‌هاست عشق خود به فوتبال را به نمایش گذاشته، حالا با این ترک تلاش کرده بخشی از فضای جام جهانی را برای میلیون‌ ها طرفدارش زنده‌کند. پیج‌رسمی جام جهانی هم اعلام کرده که این اهنگ در آلبوم جام‌جهانی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22779" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz1n2EBWxZyHZI6Pv2bXr82OIpNcOMg6qsrPTieTz_YG4SKeeWXGmVJje6p3eJOR4djDZKiCmyYT38agbx0hDUmcK0GW7zR8EEPDotgkt0qQGvot5iF1_DVrvSb3yq3-xU10BAoDLyNE-urvshcDdRLVFQEjRcsmjTCcK71NVaRCBA6UTarBE8dqG8WMve2isR9qmmQvElSFmkBLmwdCBware022tDgJEm57_jc10ACQrkG3lO2UekR70gifNg1g1cDsaAXkzsPQfKGrau3Jdxq2ceGHruLaauMc1h1_c8vtjIY0pLFkGCQkZsTijiZs7Ja-s57h8zySjjqsRHv8ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFA2HthtEBtXWzZABRmKwodHTrVNDP-_lg01O62WhoMd63mu2XswJyCcCXxs3i44OJnELgrvylt0tQzQQp1rNSRv2Vm8QMBhH6LZbl7Tg4NrIZ4QO41ZGPORSC5AsKqE8_8ujmamG5XH7jfWq0LoHPgy05_GGwaHmGkjZEdKdSejxdWOfJyWPHVl1l4U_v1UnF8L_I4ACgdAUTgrxzZ1egObGs-srBCBzeeACP6p452OyawlZ5YPpsC32mJ2ZnLCuD6H4A2PkR9_VYUP0yUvmgKyo0HTexBmaQVbf-SsvkfDN7dPmJNFo74YJVoEBD6OR-5jSNboABN8ebdRBQzrZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbT9HqceMrWggR7CbpIrfCCviGz0k51UTc4IUOHJms-c_XeXMsz6-QFk6EcwfFN9SLuLRDYSl7aPgKjZhSDO16h7pTQtVNnk6htjUhcv_Y0y26mLUcV4_eu2kYU_L5D2xE4u3vDURL2WEixQUjMIppwKYmTst0vWfDydquB2NZGggV5V2ASSnkjikNu7Whp06hbf1GNqA6jrpQNOEPMpuz-iOTmwImcxZUuIl-QtSr_pQRQ64sM2KuZSNFO91ZQPGRdqoF1sKFUaUwDlYtN91nnYlg9TCcxvfN2EkNTHg3IpMiKW1-JvUZiTr1PDAnh_sUnnHSFglC3bpDZrAZFNeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0HU2CUS3UNgZqznKfiTk5qYcUllDoTpjtUjPXQUrkJmlLe-sJg1ITFgWStM5x2PxJNYl02hHoQfDGm0Q-44z_PvNs3ubSRstorFSzdxuxy84W99ko3PNF2kQfnRih4OTKEgUB0m-fod3lA6_K8azUUMvQq-hNL3syWHMjYSWGPqb8CLk5V67oDfQ-y2xIKPhwXb3-vOGSAM93_Q7CwD5AKjeHUFgXYHA-C1dr7A_bn3QmZQ5AmOhh0SULAysqZsQDJXmBQTMkrlwH3zIleaoJvrZEEvkRGtdsC6--DswY0E4HkZDWCHt8Qu7n_MjKZkZrthkb5deRH2wxzB0qI2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD_DUEcJ7FI4oYOQJpUeQ3QSD9Na3HIrKGkhuoJEOElnM3mmnefvxOcGdkb55vZSi6S6ODb5iy9cq2DiZaxIe2V60XMPSGc8HDf3QMSfLv7HSAHt7Zirmmr1T-Krisd9C5g4urB-fNcjSgcEzQ3SParBXYLHnVAYrhZoiuvry5jCtBOKPKLt5hVyDBnoJ5WqCV7Qv1ds2uSzaMM4QwlLMH99nCtk4vAjWzciUhwP1RGAYUMrV5Z96kPQ_L60nnb4CInL2ILjcdLuFLGk7jAN_is7_2N3ubB16cjHc7GyQK-o6Fk-vgoG52-KkR8P6czhG1haE1Qvz5ipPyAZDWBZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c00997812.mp4?token=Mf94CqoHzd-o5KJ6erNJbKUom0QruB-6iPTEkxyn4N6TrU4GpsjkXPjJHBlmgzX_kPGnd6FFa5GYu_t0Ol9v5L9uFSnI-3b0KNzHTwQ5ViOExS5pjwWqZbVBrohoFXgwMOxzGWuYZPvvtB5l0_gyBAlFPheEGSyoDyT6nX-L8HhputHRyEcAJ7mkHU9sZmKAlaKGtyQCClsji3BWsXSmN5AAHIc-CKUPXit7H5EQSGx2yJzynj8brIPqcenyL_eQSt8p7jscl4XrPOjMXIltosp6YDp48mJEth9k42kJnS220K2-oIJwTDfvQr1O11ziwS5HlE2xP_DKe-cDIswK4iwNCbRCqGCD7oruaOPnpHROgXxwiSDrcFX9PpyMJnvO7TtHCGBQOZQeY20aZ7mMDMUpbsSBDLJ2uC5s_hcIadEU54YrIpdQaGxzHLukPpAtWhn4jxZQe3Ivt0D_iWDqY11djJZGTU0M4GzAYBIUeJNP1VlNGs0DVDO1jrjK-WnxQhKw7TVNqbGMjr1R-UYd-MYT3ihI2SeVhTOoNLrZ8a13sfvkVdYBDG9QNRrvoYgIDhkjOL-BooRMCLzP_F7XubdeObr8402tP0-rYkqofLVdPLBJza9EjY6cHxk1OvcLwEhBzh0oI6PIUW6Q7kIcSBXkQA0XlAU3aWoQ4k6CnHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c00997812.mp4?token=Mf94CqoHzd-o5KJ6erNJbKUom0QruB-6iPTEkxyn4N6TrU4GpsjkXPjJHBlmgzX_kPGnd6FFa5GYu_t0Ol9v5L9uFSnI-3b0KNzHTwQ5ViOExS5pjwWqZbVBrohoFXgwMOxzGWuYZPvvtB5l0_gyBAlFPheEGSyoDyT6nX-L8HhputHRyEcAJ7mkHU9sZmKAlaKGtyQCClsji3BWsXSmN5AAHIc-CKUPXit7H5EQSGx2yJzynj8brIPqcenyL_eQSt8p7jscl4XrPOjMXIltosp6YDp48mJEth9k42kJnS220K2-oIJwTDfvQr1O11ziwS5HlE2xP_DKe-cDIswK4iwNCbRCqGCD7oruaOPnpHROgXxwiSDrcFX9PpyMJnvO7TtHCGBQOZQeY20aZ7mMDMUpbsSBDLJ2uC5s_hcIadEU54YrIpdQaGxzHLukPpAtWhn4jxZQe3Ivt0D_iWDqY11djJZGTU0M4GzAYBIUeJNP1VlNGs0DVDO1jrjK-WnxQhKw7TVNqbGMjr1R-UYd-MYT3ihI2SeVhTOoNLrZ8a13sfvkVdYBDG9QNRrvoYgIDhkjOL-BooRMCLzP_F7XubdeObr8402tP0-rYkqofLVdPLBJza9EjY6cHxk1OvcLwEhBzh0oI6PIUW6Q7kIcSBXkQA0XlAU3aWoQ4k6CnHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ترکیه پس از ۲۴ سال بار دیگر به جام جهانی باز می‌گردد؛ تیمی‌که با تکیه بر نسل جدیدی از بازیکنان مستعد، از جمله نان ییلدیز یووه و آردا گولر، هافبک رئال مادرید و با خاطره شیرین صعود به نیمه‌نهایی جام جهانی ۲۰۰۲، وارد این رقابت‌ها می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tyar_0CYz3okmsp5BeitCWXzZZIqfywVKgf_sbDnWERM320R3aAmTAg2zmZ3wvENhhXRNb6OSXRSoowmy0bG0x-P5A7AzGba15rpK55cikONp81BaR3tZkQDnIlioKdYNUNwqz-0YLcIzg3-Hn_c67kKLdedpSR0fcY6hENRB_ZtE1spCE_VPieD4XAtn2JPQZKfUduDkmGuEnhOpp_cErMaNpSsQS7E9fMuXPYFhF9nlvuQ8byV98_jDZKgc8deXJAejgrAMy-ec7WwnaHcJAdXSzQLkSOYO6JEKjFv5jlLbMvPNdj3NAUpPinebaaVnkxDbqyC8tpNDMCVmx6iUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=Ra4aUlbLllCm1Aii6KZk-eMmUmKH7T9X0-h0nR0EmKkLjRrDKMf8ufch9o8Xlh6PP67e74pBalXO8OvL7BW6cltfgjPwCM3qX3JgrUToUpcB_ZRkK0KuitiU6Mq8IPO1hLAzq093m4sqdqrBjcGlm3mWXa_lrlW7PkvVecKXxXho4s4FoROyXAWgtDFK_CFvIsZh2EDYml_An_oHJhKIf7GQ7mD3JCxfe8nB0cNJs00u8PwmQfNKjCMhMwQ0cL9nvt9pfOv5tzCWJLkIwGgURPJbUwLOqBABHhy9t3G0SPxqo-N_9fHzMbZ7JjpSq4hC4ZlJdgLwyMMKC0QFcCwvTpNBjteiHEl5Fn1KbbYYqRqmUMQPinPpfrxoPTI3KLDlyNn8wadYuS7RQkeCLrTPpC2YJfud_FJuzWo5LtDbvhgq2us_xD2DTRBmBHoOnVy42ZeAGEnFmLzjc_JHItDXyZK14l9PLff_pazJVGDKSH_THvnWTsLyyPny_PxBwchUyqwSr6n7qIRRLDRDOCSO080at5PlNu2D7JtxRczOcQ3IBQ-xf3gVXhkAAiHWYad18eCH00_-gzgpHDFH3jQLPF_4nVyuwZIUUoV_J7NChSpnggA5RwFSCjf9Z3yNHnOm8lH_nAHheYLGB73iPIXTU0IHWTLECFd5UgHfBo_q1LE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=Ra4aUlbLllCm1Aii6KZk-eMmUmKH7T9X0-h0nR0EmKkLjRrDKMf8ufch9o8Xlh6PP67e74pBalXO8OvL7BW6cltfgjPwCM3qX3JgrUToUpcB_ZRkK0KuitiU6Mq8IPO1hLAzq093m4sqdqrBjcGlm3mWXa_lrlW7PkvVecKXxXho4s4FoROyXAWgtDFK_CFvIsZh2EDYml_An_oHJhKIf7GQ7mD3JCxfe8nB0cNJs00u8PwmQfNKjCMhMwQ0cL9nvt9pfOv5tzCWJLkIwGgURPJbUwLOqBABHhy9t3G0SPxqo-N_9fHzMbZ7JjpSq4hC4ZlJdgLwyMMKC0QFcCwvTpNBjteiHEl5Fn1KbbYYqRqmUMQPinPpfrxoPTI3KLDlyNn8wadYuS7RQkeCLrTPpC2YJfud_FJuzWo5LtDbvhgq2us_xD2DTRBmBHoOnVy42ZeAGEnFmLzjc_JHItDXyZK14l9PLff_pazJVGDKSH_THvnWTsLyyPny_PxBwchUyqwSr6n7qIRRLDRDOCSO080at5PlNu2D7JtxRczOcQ3IBQ-xf3gVXhkAAiHWYad18eCH00_-gzgpHDFH3jQLPF_4nVyuwZIUUoV_J7NChSpnggA5RwFSCjf9Z3yNHnOm8lH_nAHheYLGB73iPIXTU0IHWTLECFd5UgHfBo_q1LE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXnWq4H7zHRdcu2PkZBKwgzEgZk5hQj7KlWZ-VmaiEK9UzPhRFKB9wgYL7jtNdu0tsev5urae6ImsQKOcppv6ZfIDhCIURFqfwxs3G4y_5tEXfaLbexZeWII6eGSrVBArwhJo-HZaUuAn_CsNw-2TAMbnxcYlYWOrbzyYLyTZWxVsJBqHAc9fs8Szwe6c9RScSEUDbTWMgLy0hBT-tQdG_i30k4HK4qy_EVeAPtH5Dq4R-HO25tKqAvwZsO7KYNCmXKjSzQ_ueMI8UIqcacuN4UluSU4qFh7itnF5ANQuqey9gVaolblptCfq8RL4ruYEZUhaTLm_kTZrjEn8LwZ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVGATMpIxvHJyKPhx1PDBSTjAFoE-QkffqqrJmaQL_fsbAEiSU0aN6x9emT6YFgovzl3xIYYGcgWKJgg54M4cmgT7nj3auZKZRy1huNHy5hrJlmDLGi7FPgWf4bBITZanpOFaRJzMWJo64SqRuDByQm-34-gAQRwXW-nvP0QRKwAomlSanPe4p9ZAnucgXCJEvWbJB50cHI7ZEGzsaDDou-X1nZZH97mkjz774lsT0Ujp3qHD-xTARRsgrv0Kp2PRLV_G0yU1nEij9hga0gBlt3pB4mozTdg3fYIgTdEgFl6u8jdg5BIJrydb6Ezn7VkXmegnuOJ5BxAFNq-XB4S8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSD9DPdPSxheoGCNs1yuimUxg8Hs_VqQ7qRUNkCNmXCYkisQH8SvyRLSEw_-5lHbVthtvmkvl6tvRO6OiVHRKb24SE81ki9UtekQ6UVVVnthXG2uNrFO6Hy2C0JzMlnFJtjJxyJQa3kSoInfdVSBEV8TVO85dPmfDVN4cAQXam3t8KYzc81KARRos4rsSRuqlIvFznz1IWuHCiiJc7KaWaiA6zwMkhPPwPyn95NOikZfBbzdIXuG5oIDRDATV6gtlRxrqN71_XmVo9mFgJD6P8G9wNvYI3Lat3w3LLifx1tydLl5LjH088QUCn95mTW07_Jk-G4SWHcqJ9HKq6ZbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9iyidEQK3OpAfW2IyA8ypI53x7PmXzDOJ3d0EpiXNGdKuR-G6YV_mW1Da68o-uPQzBcm3WfNYhmHzQ5nSg8zEQ3cLyPW2iH7juezwhUcKv72xAvyJClKoAWheHr9-FXbcbKwSQH4SXlYQunvvOcbc_OwlxKzwg_vUN7ThXxV6HiAJHJVwvunggAm5HB6KP7Xeqe4DQTae9IrKsGMns5ooyXVS2VBPZj-N7gh4B20jhPQtE20IbvgDX8QCZT38dG7R0zC8ERcTlbua88lngolMeQKF_ramEwvE1ySwLMWn7d4Ks2KhrDIHthnJ-_5mcDJczThktFH6qT6TAXoBjWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE_Px8nf6ZS5P45uSpYmPrm1DV0DqKDbmTygL4U-kodNpJeb9r-aOgS5-plWMwS8V23f4sOYfBPoVwGK7nl2l1DI5HeY5KqDLIe1H0vC2r7xCq4nBzQWMVgWousRNhsU35N2h58N_hcOv1gwUFckw7OfxQcKiThgjY5X1YpXHqrcAZZVGQfPBZpL4LdNJ1b0RvFRx_lhZCXqTJ9vrwwCkkcEZS0Cm5_9_bVMedTCpbtBWAgcHQgkkyuvoj7vXwQsAFRuxJPxU26rPTETEoHFMtGrhqUhJjGe1TAlNBLelL74gxsjmOr693rUxxSi4KvQpyvbnqVR00PGZBhYvqTaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0rmDrlBU6T_Ew9hVYAEjC_QSbO0KaAbYCaP9nWPNniCoeAKaDtBSpNh9RULk_ICy_KB44lTPpo7x4HOAXZTEmdohS4ev2o4xQRZyqHZVpTSe7gz7SXRy4CQ1YIMxPG8e-BJgOQf5Lvk9MCxCMha-zLjdq6fMJ4YE8Fuwp82IL4I81PtE4dY2J27S3COUg-OB82O_iw1aCf3frUO2fwngc3nWz3PRX0FkGT3fQPULDr77-Uz2g6kS3E8Rh-Do89NB34zyGtCiZ1L1FlR3hrUp1gXhEZ39UWeIysY7BDqvGbhcPUclQy5yHtHY4H2RbcDxSvkAH-pxtkfS7QyNbQZeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjAWAPXPrgRvEBninrafQa2chilYwwg84ZJID1LplCmwEL9N46NmlwJuQEpH22Kp9RKzdM19Be2lYmUQtdez_ps2_CwsM5NKS7XG4UPTZ5ypW6jEUyjbI2l6zwRtAZxszemedtJM-WQvWT1UJkrIIO2AdAPBdkdh11zXYhw7DtRtZXoGpsr34TpI1lPQ2UNjFXJGRDqKASYs0WPwJBDIV0AA0MYwn9U27qBkh2dW5K06X06-UxP3Okvap3KQ3F_hDuf9MpH7TolD2mP5JU4MdXQvCISbuRar1SFQx_U7h7C1aL8IS52Ddkk3jazmpyKOw3HYCP3pa-uDUzNVIg0Cmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5y6gzo5GHw-F70o0WIUrOJod5wVj04sgxhpG0sLmTvZyr6Pp-XZvh8sikYI0qjlq7O4z3LGb_5z-Fi-U0_nIs_FbnGSoTOGqkiNHerOBH2o0Vo1kvmcYRIgHWXMt3RItugN8GS8XtPZ3JXcmO57uF2manIoCNvchfVT_ztcg5h6oQQ4DHH_ofXumJpg1LDAEe1m34TfWx6qWZOskSPbOajTKh3x9CmNFS9ZvGhJglOdGx7biDd7Ohs87iUrwAl_zgLbDFDxJ-8jXbg1_iIDL9qVcTy-WaDMc4ziInW8x37YMIz2jAkjMFmKwIGl77PcUq9UTwBWSWHUe6Bn2JwN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkrJ9xoXBotnW4MXl9FSQN8RQzosk51Z0a2eLfSeLeTNDLMG6z9ppS4tq7BqBZaoW3ytJdeHDHiDqongvF-CcOW2pMS_mlOhxudjDCLj7BFN5XonFwWkl-qJ60BfamD_5F6LanS_psNEI671fkXDZ21sRS_QrnUbMFpu3VyF69fF_XLj1jjSG-H8_EY8M7wBnBmsbz-msyko4og9FIqiEfPViuT0KFSDRW9UHNEFhB9T4tda-JbiDHcmxS7wWQPwY48BssvnX4eX-bDKmJ65MwEcXp1OJuoFW_WfT1xyeIzWP__bnedjKQbTZIylkCncUs2IJvJ-q2C0zhZx8SsYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTtinUjZe_4SDXB-3LSKbW8UKT0fKByLvE4ZsHwrGYfS5aRAA0ryKOBaAwaMPL_AwX3pj7lbyZ_AdAk0eXhgrPPnqgKyMWV5b8vOsQHioCHdnSDQ9rPK6npCc8e59KF9Ik7O1NzuLzH2N46fCfJ6QDZkdkNKnrvCbevhJkik08T-yX7Q0Mo760XLqanVDdotC-sgsE3K3TkhFpXx6pxUG8SfjNVKrjuo27FFa-lrY4nYQW8uzmvtH_TAu_vfqs2GlaJcP2DW11wtHA27l90OLd_uwJGKmtc0X2lkWj94Yo692lf_UjA1-aRsh9LYPpAzYoXRBoV03M5vPpbOCmji_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=lFmYmNECc8TrCUlBYLQjsvHxERM2lfK5INNGhd4dbeMmGNOgiP9L5Kchn4r4FTZVzstAhl2QLfj7JPqnfjy6ZUFHx_TucKU_0pNPO0s43M1GGSQqdL4bA3XnRwWf3rsKrgM6IpDM6ejSXYNp0O5-6uKzWYduCtya_qp264ojlfB2C4OaXdL5fjFGT_6TjkX8qzqKT78nNuD3Tvz7pEtB0EBuItlQ4M5EilVIEh_UwZRjPqOBJD3nfr4rDhOcy2MzZl-sPGB9HRyxbNEIAesB54t642LIz0zw-ipQhN0mYwFNDFJSKpRc0VmGbHO8Q4gTMXgxSfSvb0wRQ89Hr49Tww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=lFmYmNECc8TrCUlBYLQjsvHxERM2lfK5INNGhd4dbeMmGNOgiP9L5Kchn4r4FTZVzstAhl2QLfj7JPqnfjy6ZUFHx_TucKU_0pNPO0s43M1GGSQqdL4bA3XnRwWf3rsKrgM6IpDM6ejSXYNp0O5-6uKzWYduCtya_qp264ojlfB2C4OaXdL5fjFGT_6TjkX8qzqKT78nNuD3Tvz7pEtB0EBuItlQ4M5EilVIEh_UwZRjPqOBJD3nfr4rDhOcy2MzZl-sPGB9HRyxbNEIAesB54t642LIz0zw-ipQhN0mYwFNDFJSKpRc0VmGbHO8Q4gTMXgxSfSvb0wRQ89Hr49Tww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD_YDa9-vbXw8Qw5GWuodc7rDU4sjFFwtv4eojP1Ue3kCWlWiszr6EJvq5YIBDiiml2E10n9gOWMFRvUtJZ79Pp2wXyC3Qsp7vs30wPnxsJA8PEkTg1f8T9BWJM30Oi1AjSXcOjWboPyO-a6VlcUp958nD8WI-ARrviWTA7RmvcsogAuS_51CBXQLk1U9v2ZraWGysMN_pzhA5JAnhce2nInnr_HyXmhRNFO3PJhXQ3OspeAja1xaaHBT0XpIJuPqsPxIeDmslYfYOWjVlBr4K48x6XhIwK6BM2oMROGAFjfUWlycBQ-zH1qhs6IySqvtFzCtzA39bt2Rsf7rFVpwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zt9ncc-BN5DRlaSWgvvlz8_-RBVh4ybzzOwrZbQvwSLSb-jkSkzmThoADWKeb23sbvhvUu01h3o14n8QjqekTW6_FagGDoQ9T-TPmp1Is8swEGaK2BBnO3C94y53n1xa_nkecxZ1hkBzNaNtxcnlVKgWL5PQ3cOljTFxb3SmmohRB-37S5B_vDjxzCADkc4tsthPiuSEN6MI2MbihQFIEZv9iO-0o-QQh-JuNzocJUbgPW3VS3gJPwdOZkPU2vJQll3_3z7MtlWWYzhJLZLRqAAQzMg2ZJVCajvL53XvDyLwssoOeIBoM9R10UkbLNZlbxMDV-o_y_tfUvS3fhaUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8DbuiwpI6u67cSKZjgnRDWf1jpAPqcwul6UqAS9lDiUNkTjOPLJZQdq2Y9jptOzNxP9LxOT1JT0WXJRmm5nWMSMlx1s9liTJ-eBzvQeP-_vu6Ff67IkciZqAmSYPxmZC8lZPCy3Ga1HqaJICnBqM_1yz8s1v0UR6_7V80CqnWjoZmSn9HxvXFcy9J776HOh6u9J9zKs4Lu-xFDaDOWyPrKGSmWFnJ8bKwIR92HfVYd4jpD2XTu32z_lkST7DlU6z5NY8wGrm04dBhFQMhYT4AMDb4tivCfu2YH7c761yHss8w5RKKxOCFmcJ_vJJofl_wqmGA8VfkNbAVNftQMwEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=Vf6U2QsSfQ39WYWu2_GPlMrgYjabMfdnb-IUwSHPHOwMNTEnAlHsHW8Vaz-M6KmzOgYvO6Xyb2cwuaHYZI7cMmtwId_lrtDBEncaERxvJ4pfG7V3E6Ho_bL40GCvL5yGVaNehsLSNL-5zSCqfGNICREe3dxBO9DSfDVljtClsUNCgE6HP3OrjeWMqqonbEZz2oAMjnD_IUjSB8wVv1vlqndZOr7VUIKzw6AbPcDBHRbrQutEmtqQrqjuCSrPgzEG8FzkWndDoBbiOayVlLsS9f70-rLj62SbMRikZKNZm71ef6yKSPxo-BQOBkBxC58WuGQLXlPPQ0UhYwLmrAgN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=Vf6U2QsSfQ39WYWu2_GPlMrgYjabMfdnb-IUwSHPHOwMNTEnAlHsHW8Vaz-M6KmzOgYvO6Xyb2cwuaHYZI7cMmtwId_lrtDBEncaERxvJ4pfG7V3E6Ho_bL40GCvL5yGVaNehsLSNL-5zSCqfGNICREe3dxBO9DSfDVljtClsUNCgE6HP3OrjeWMqqonbEZz2oAMjnD_IUjSB8wVv1vlqndZOr7VUIKzw6AbPcDBHRbrQutEmtqQrqjuCSrPgzEG8FzkWndDoBbiOayVlLsS9f70-rLj62SbMRikZKNZm71ef6yKSPxo-BQOBkBxC58WuGQLXlPPQ0UhYwLmrAgN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkKHrpbJE20yQJvIWQYh3QDz787Q4wV0-pXGPeYBkLRX9fKchqwj8b8VwUQj02dzL3GOaGmFosFYEVKPwu32_EALfVE0Q3r8vzGA-rpMZi6RdY2di9BR2_HyN0ukVaSpOXz1xFG_9pnVQ6aaTTUXyRaww9QFrH6M7ypNausH2je5wdv5CQswsMWOZ589A_yu50LobODN9oWQYL4phe0Z5IE7-cOYXp3DkihtMo8cFmVHuCgAqf1j7grHT6g3E9F2BS98fKxCZXCEZCd39FmYWQvtTGMh_oyPhoYbk2Bj8pBLY4pbfGEcAapfjAWTbfJQmPE5izqQuzSos8P4awfrjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sndOaAUJvtwxIfv4NW6_tU52ljoBbtLZaMHs1UOpFhzo2DlPM1nEYwYCTqOhlhYtzry-XYrhPagCt4F6vOsC-mIWCesMoAR4gqhaPOnilYrM63Mg_CtfXBiYB46djlQgh3Z3z4iEy7mCHtzzjSK_ew_8ZcsK_JfxTT0W5KVrWbZy8GdMXEiqM02BA1255rwEmXOtQAQRpAxC5P69KJvN_PbL-4NJ41pl3Cq5IqcekrVzKxL-WRSylMwIa0KwcpEQ16QDVKh5fOO7VCDtAChy4cC2ny2lux1MbQ3vvaJ3DaEPzIMpoDVEclp09et4v2CHa1wcXiimAp-m5EVdYSccAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5StB1GYt_lxMJPCHlq3qY3S515j_UqdEdutr_6AsFGQKPMMWKPJyRPYcsHhGOiYnywSlOK25HjRKnMpQF6irHfeJhUMFyiL7pfTA5ty46kEp9FIKDeF55uvrdLWiAy-8I4BAtQzt9mBmvHcIRTee2wtm8SPs15Vbgz17TSscDCM_NIO9_z_pUDAK1fiTzUJ-5psjaE3WaVBl55S024UQO8_fm3DhKgjTSGC9q07f1r3T0yzgAzu-JHRT_dHTMjaV4rPSq1eEmfrW0Z-jvXNljmE47xqLLWc66vUqQidUO7wXWkdoY450vSQ9HIo9qIF5s_xSaUPxbD0xEt699gNbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bREWE84-Fus08xpYQ3RTThnIv0OKZ9r7rBFo8-XNgw1fGlBCmE8ra4VryVMagnxo5J-ZgL19AhIs4ZHYuNgl6nE50PNWMk4EF4JJyENw7yA8ijKnJsFHVzl_MWP6V8ZGVQhN9DYKwrqcAQQ1HNouM3D3xyg1rwbBKGOoj-GmmE2IS0hFQIQXhz7TIe-YY9Sx8bOTByDs37VQBipJm0nrI36uGpCGl9Zn5yetkLRiyvqPZZniyIsKKCQXqqBFlggfWLHi51bmAmYz4j6hrBsCb_TTZwIHbqWNdb39wTYVTEhRAXf47B6lfT4Rn8LO9PxqfUxRmnVVZUqHXzIwnjncQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRDgGqtPj2xorPrnt0SqhNa6Gwl8PVfFzBIneqSvM9t0_fJYJBz2QPmAWzWGlLO4FQ9Lxp6z7IL5PidGL-xRt0iFYKcwg_sww90Wb7W9SAphKUKy4G-VBbgyOu-6mJ-ulPfXUp12zsmF7l9BD46-DwJT13dUa8yt9aatVPAzmWx2L4xn_C1M2HBx2Mju5GrFgcMnopHRFv0Rn7ZvjwlE3x98pkr2PFhS5ykj7VrpM_t10gKg5V5-eeHBKxh1UzFR-Ivmi7IQCGpjuE054d_MCYysW5FkzWOrB2UsAKkXXeCIEmDKmvBL2ec5i7MapoMEBUnvSvtL7aUbrGKGltN7PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nslwwScsRRXr5tYjOtsFHtzFIK775netE__aoQTyarMx9WSxvnAVWGse-GZwm0hk44LL4EpRnDNZvPKJqveQpLWzUU5vyaGqVAn0QXajK5EKskqieDfK_mY2FjwttvEn3Uhvu-XFBusa8cCGBu-3q56K48R8UuRpkD9tNvGMX18UCBzAQs-QP3zD59JRenLWp-gO1u04TEGamnR9QpFynnbJCefxqRRnyse0HQqRz_jaQ9J-kQWQJhibs4i-huiRM2H6GSxDua0hq4vCuOG9y_lS1M80ZS_sAJaWCMYM0CIoCVLm4nlpvNE9JjCYTKqLZ3AWGiKTkf0msQL_CjCnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIAh3NVjHMVYcYVyDZOVjxbG9addCTnkRwZ_K68p4nlRANfMINHTdjp0gRFr_Y5ddeTFtST8RktRM1fsPI51KcuzN2OR62ViquVzO1obINWtjVHkwaNpNwFQ3R2ez9edvp5n2lZAyXFs7JInlTGlWVwwynChvzAcwUPUiJ_O1UK59X944VdkriWSl8pTzjhioXvIJXNSHdpONiNkIsd6SdbGfTsgoIh4Vmj2UKNtY0LYly4KBFw33Nq4ItT4b2NJX85eDRZIpwat_kLY55WeXQMfd8z6Yb_hz-CuF9RX0PYESRNRktxJtG4FY7lc3UzOThRFNKGFF1tnVrbtx0OsRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=DlRVrzp2E0g6drXB_w9R9UzYWnHEYCYzWWXu1lgaBLrltsbaQjP2Ds0IjclECUpRHejxYO8_ySEzGvn4y43BgGpHt6-e5YX-dRB743NgicUA7EM8yz7tHL21UfEDBfbIkj7ab4w26sSshEHmKpyDdfN6_u7_0ky9DRvtxiwPtZlMME1Zk3WN1Cq8lM4lB9NGmIk3efrWi1Beg3zXKXocsmIKmWCXCNNOr0MJP-ibNbLBVvVEFpR6di1YfZpfC-1PdjH1A1bMgG6XVAiKVeWMzFBxC0mBormFqXUGYCBLsVifNVB53LgNApx0duqEuyKTq_mfv3nJZ-C8BUQjhNe1JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=DlRVrzp2E0g6drXB_w9R9UzYWnHEYCYzWWXu1lgaBLrltsbaQjP2Ds0IjclECUpRHejxYO8_ySEzGvn4y43BgGpHt6-e5YX-dRB743NgicUA7EM8yz7tHL21UfEDBfbIkj7ab4w26sSshEHmKpyDdfN6_u7_0ky9DRvtxiwPtZlMME1Zk3WN1Cq8lM4lB9NGmIk3efrWi1Beg3zXKXocsmIKmWCXCNNOr0MJP-ibNbLBVvVEFpR6di1YfZpfC-1PdjH1A1bMgG6XVAiKVeWMzFBxC0mBormFqXUGYCBLsVifNVB53LgNApx0duqEuyKTq_mfv3nJZ-C8BUQjhNe1JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhBjBUyL033g_U92R9ISlcz21pIjqfvFyDiG2euhtyn8XvfDM79lOk9rwBZPjdI_Gh63RysoLTNmoLtSey8PLNMWHBwwHC752VmhsrcG_1xESkSrVRoKEf3nyfSZD6V8LaNpd-MpzYdnEzPJUBHoypyHRZQfXApnkOaKhtcsc5-3ZWmxmEInNHYWOYj-vYn6XZBq2MmxR_LHvz6ZlJOZBVkJ9UQ5CqWHzKjTg7xwnzDE0xL_P_s_okZ1c5jAvdYDrYIS3s-xl0R9qwmzzi2eLVwuQN9Cq0hdVTYnVfxMgP8nY1liqMIE2CTaMjd5kBzg2cJoxOV8PjaBtD2FKOMmYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmxTvze7egr0eb4TqNh-JXWvOoiHl7SxlVbjheocOQNXqZDZBy0Op4ppKQcm5kLKVOz_tVm2gSTL1AU9xECaK-25UxpqL5t2HOEc50nn3CuWgpXGR1fwd73aoibqO_frmr5Uq1hnGery4Z6ew-2VOLOZdP5dmK-HTK_VIazmSZKZE722Kjfu8-klricDQMHLBpMjGC88r_I03HTOTooX82g3EkAsWRQZ2UAnUmpewBwYSc5oj_ocaA7R_F6EjCp9d81P_dIyIvq8xH1YTtfq-FV_WJPx58s226I4EU99RBHQmXX9z4Y3CXsJgY9fJ6SvLSYww7ueV8cb8xJGE8T9Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7AApNfY8U62LEmx-ChJgd9v7_0uvWHKtWFfXt-E0iDF-VAMH8iy8LmDQ30LfZ3vzzSyf622U5oWMuBFKyFo_JGPm1Rv-vhLHlTUKRWlnxRK0t0jC1YQPTouNVuHG7KRvsiMCWocAC2a_DhLSv9ZnXvBEwQ_Ts-dkV_FU2El9dC3ojJu0Pc1-FNnhmRbGjaLVN6izUm-WqNZiuaF_x0T2dDJnyrVPSKc0ZIxXK8MJpDLuTkO1qFzv2Wz35-FMdXmrD5FJj0VsNCCLOzJhX8oMSKlWX4I4PGZUVQn2ajiD9YLhV_VpTrfOaSAMMn-DrYDjVfjl75ifIYR41HQytqc4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXP6-P6IZvv-vndtrzKE-62ZiRxiM274xGZ-AbYk0x1HcBghWFFTmUsdiq9NAAalIeKJkUgaiNoshXdE-sZ2gYzg1uWHjURMrxZ3zsYBSTY3FpNmtuna30xjrYIg4lwNQfoQE-tmKcloE40cG9QPvS9P4WVQtZ5CPyAVJeEisfYfdP8dSiR1mZ9FFt83Q7xk-dpMre9dlolRnys6M_uRxRrnhYBxyC5tV5Zy3HGnPlMKEq_OGiIq6YRCOqTaZ08QII4sSxUda2p-9kfBfZ60NTqccmmeQuyENDhdLEktvXZDPLfToQuYoxyHv5tU8G2fFNZ7bKr3LEgeFgpTle5Kqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsLEbmjYEou3Py5Kgp2IZ_Ecea-P-1mWDLCXBpdeXKz_7qeVy8Ed5WddEER4biW7syWp8g8L8QYdwIYpx9q_gWQ9D5D0FWDxiaELShYTTP0oeP8ugoaHMPQyWfyLTpLYjpHBEV2cTJ69pHut6CKOgV8LxPZPI0O1JqRAMm50Scq9OtmfUY7isY8MIhLmi8Rc_IUrjDZCN5FS8e9xkWxFDO8mjxWwfwnNomiJY_Ipmkmh1ANZIu0ifNRgQbdIzdfyHrPSeQhvgoS-WVdgc2snxD3WDdKJqKEOJSKuMwJ9nex8e9_vVfCTxiTcqTF7aJRi7ksp7dUVTBB8WwuHKnqw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5vhqUKz7SF-fYBvEEpGC_6PA2iCi0ed5O_bnlp9vWnrZrgCzd2nio9gXJX-DWFfs1mOJNN0b_r_G-OX3z-QnnqbCljYbxl68y4UVceiHrFnk3Ook1CnHxzqqJpd1uWmk3ck1hfVM-bJ4BBm3VjcIotZNgp7tNQj60SbH5mp2ubN1RKHTl1Nj_IYQ1Oz_YSY6uOabwofokqVx9eL0tJVGs3gaaSLU0aH_vRILxUaysXEURjAhb3p5wJtT_jiG-DYy7s48Q0jwetWqq_2KguL5dbXnJQ4gW0QSjOn6B0jR96XDKGhogvgN22bnKhSUAMMVrRRGDIcgVUbQAfxT4sVpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1314be179f.mp4?token=oNMcznI6ytUDNwQRBnaQQXrzJomX_8904rp6uSJJcHAWlnBWMGLrwqcxKuZ71G5oGUnHHJIyH6FqRnSw20tIWLjJ7nrCioy8xmb20cqG9tc-mYR7rIt_VoZQzpg_q3p__0BvV7ylAXvxq-sopiW7rvpMDE1OyggZLQafaEOnnrG0wcB9ns-x9n7zxuoUhu-0m1Tp-eSE4-GKkGWpITR-wT65fbfkZ7b-LESULBzP4Fvw_7P-hUghtLfZFOzV7qY3RY8XbMO2aw1t8cnAwMM-nMidI-aI1r8Y3edaQUCuoyL_BEpMWq7biqLzLFQ0zb9CUV5kr0qLe73fFFR9IsmZHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1314be179f.mp4?token=oNMcznI6ytUDNwQRBnaQQXrzJomX_8904rp6uSJJcHAWlnBWMGLrwqcxKuZ71G5oGUnHHJIyH6FqRnSw20tIWLjJ7nrCioy8xmb20cqG9tc-mYR7rIt_VoZQzpg_q3p__0BvV7ylAXvxq-sopiW7rvpMDE1OyggZLQafaEOnnrG0wcB9ns-x9n7zxuoUhu-0m1Tp-eSE4-GKkGWpITR-wT65fbfkZ7b-LESULBzP4Fvw_7P-hUghtLfZFOzV7qY3RY8XbMO2aw1t8cnAwMM-nMidI-aI1r8Y3edaQUCuoyL_BEpMWq7biqLzLFQ0zb9CUV5kr0qLe73fFFR9IsmZHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اسطوره‌آبی‌ها50ساله‌شد
؛فرهادمجیدی ستاره و سرمربی سابق‌استقلال وارد دهه 50 زندگی‌اش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=FywZAWyX7cUOqFzzMeIuZiU2mOs6yFtTQcmtPd3YGX2O4OvCdfVffESlbXIiOoR8GS83lGYO3mc_WjKQL5T54yThgzwWMGT3Bi237rAqSweg5wFYGaC3QkMPgDNHGQE--9EWLLsFPJ13jlWh-CNSghdHsU9BTN4WQ85nFyHlYV2elOOeU_FrEgVMDmZWH5BlcEg20KgmayfEC5ZxFCpDr_i8Ni033d8YNro2hct3ondfTj0G6z0fmBPyAlY89hED06zOEgIOEZ_tSLkzhu2k2A36IgksiLjt81bi3xjqKqdB80c6inL8md1MwZeNmohOFCSN23IJS4v98H03pN9jbIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=FywZAWyX7cUOqFzzMeIuZiU2mOs6yFtTQcmtPd3YGX2O4OvCdfVffESlbXIiOoR8GS83lGYO3mc_WjKQL5T54yThgzwWMGT3Bi237rAqSweg5wFYGaC3QkMPgDNHGQE--9EWLLsFPJ13jlWh-CNSghdHsU9BTN4WQ85nFyHlYV2elOOeU_FrEgVMDmZWH5BlcEg20KgmayfEC5ZxFCpDr_i8Ni033d8YNro2hct3ondfTj0G6z0fmBPyAlY89hED06zOEgIOEZ_tSLkzhu2k2A36IgksiLjt81bi3xjqKqdB80c6inL8md1MwZeNmohOFCSN23IJS4v98H03pN9jbIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروزقربانی سرمربی‌فجرسپاسی:
امیر تتلو یک اهنگ داره اول تااخرش فحشه ولی خیلی خوبه. قبل هر بازی مهمی اونو چند بار برای خودم پخش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdTnYPEqWOmomv1CZ5SwioExrfDr_2lzb0u0KrXJtcgh-ZhQnQT6iEaozQoqZKHkTM11D2XUfv94Vgz77RII-TPRrK4-YRBstXYwivxiA4St6-GiXdBWw9POouaiYi-rtwtLGVAwDFbl7GIX8uIEoCGBwws9wQzR7CC16_ES2-hbINxUwimX3ue74Ern0fZrogD7BwLlLKpANkPHp2pHJ09ZPR37nzKk30cxA8_NCMTDrvOsmHQ66MWEmIsHHXX5pNc3hUnyrOTLWrqkL-LJaUYxq3USL9MLh4YCpk_HLmjeNT-buDwoWsXooZeKG2xresYSgSUSRSv1f6itSRbRvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6sdhJS4K6Om-dpdSGxPXGmW2fg48BCAOSbHC0Miz7fRihSUQRbSRPmKHZ-qm9rhPmydKJ1yExWMVpFlChmAvfxrjUP57HD2pwx6xWWxsXHka_Tf4XQnGA8DtUgjnW6s9UmjhMFCgxhiInMVLEtegqqBYciL3feEM5-KGDPbrkxcas5EiAvtM6gdWwkfmkZ0sJcVh4rv1FF6GkROFfISY7jEQy3tNdDpptTtx5sJDp0B8k8-_yXX1C1hK1aP5PX6-F-tCa-IT4-v4sXFWHe9fFXk1qIufvKiCb3oH8niAqOC4Mqy4G7loe8bBdI1sEPW1cy_k4nvnZFbaPhgSOeZRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUPT5tdPGvNp-cOiYPlYfSFYFkt58jVlADUjUGr4cmgNFcfAy9RlfbP1wNmmWHpSmdxSUM2SEuO_s4HXi5IXjWAXDNCOFQBjJps_vQK0J94PB4BlajtkngvQgUvk5AgKFgP53cyts5LJGq9bgKY6qUjlvNYuHXpiVXKa0hY8T-9VT3VH6SBu8SGA26pyIFjrh8diOT5In0SFrEdiTF312ASgF5ZGOe6Ax-_syZ6bsX5DmXgWBfIv88uatNsSYj9BHVYl-pHeeUX_R_Q8KmeekaPsRZyeidTkdMuGLCSuXZSXsMnQpR0Wik7Hi4bcpbkthB0Izjz36b7DvcdL5z8ZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=Q83w461ErDlMP_iY52JKj6LBhAJaQBT00-yWI9d5tSGQhYbt_PtzarK4V-eST_pCGaoaU0k2mtph5aQI3EFxU94qjaWNTXcJoB9n0JzuZRPNKNCmqkOiIg_bFl7zJ8WfIJaueKR7dUCT26gJ2mNaf1FpYdtbTr_LR7fYyDpONVMiFJ0pvZ4riKQiWfslKDo4I34izZtejy0qmKizEN9fCoyncasHj7Xp2LknvhiN6j0Py265JTrtPq2EqCzczdHicACgWF-AxY6qTSfn-mwWEVuGMkui9v4NyqsyiYZZ3w3wEvMvK5TaKkPHJp8Z4moEXKrws2LHhVhkOl_zfZOY8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=Q83w461ErDlMP_iY52JKj6LBhAJaQBT00-yWI9d5tSGQhYbt_PtzarK4V-eST_pCGaoaU0k2mtph5aQI3EFxU94qjaWNTXcJoB9n0JzuZRPNKNCmqkOiIg_bFl7zJ8WfIJaueKR7dUCT26gJ2mNaf1FpYdtbTr_LR7fYyDpONVMiFJ0pvZ4riKQiWfslKDo4I34izZtejy0qmKizEN9fCoyncasHj7Xp2LknvhiN6j0Py265JTrtPq2EqCzczdHicACgWF-AxY6qTSfn-mwWEVuGMkui9v4NyqsyiYZZ3w3wEvMvK5TaKkPHJp8Z4moEXKrws2LHhVhkOl_zfZOY8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rr5eGKXfcO9lZaAQ3x7Mh3wN5qmxiKp_I6rAKL9dpdgdOzdEyfc-1vVV38B3sr5CXaEwFtkcXaNs4J7tHoynARFt8f4XudjKAd5exgNBYtRx2698GakF0VlM5EUkxBTBsbI65RWlgYhhaUW8jlpxVzZvBwoZqCSUJXX1Qjvfziej7v2J1AGK_6C2B7sMQtvR9RYWrBdgc9tJNB0WBVvFjrpei-7lsIGnqP79lzplQ-wNIzMMJMkSDSs-eoD-ujTUA6U6wcQLfjqi_pDjGIC_WlniFUuxwFJ1qVpKbbKTmIOwOXV9Qfwxj9E38v-p2ntbyht15tiviOOle_ctEBnmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAVeaPLzcLfGIdgMZYrGxM4ht1lQISDy3nEw-QyoftQl6c64FcGG4nnD44ctikZhFosM2TfWassCDOY6v5R5OxnIxdSfA4EWSsOG7uzBI-hZ8CJCVYxxyZxyyhWtaDZC757V9eSZOSaUDXv_K7N41WMUWeNNiCIwcVeOYFhWE4MJxDZeQ-Z-RdYbLWdb4CDQqwe7DWRoRGa-Borsuip6KtEwa9HRf7zzg0EHJy2MGlgX1WH-avpuaYv0YzvCZw0wYdrYapSbbdrNTSJK8ZCyILwm_l-fdFDQH8pq7asfLwYuShYj3517ts6GVW2G8JnKeuaLpSFtg-tyJizmkLWQ7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b71lg1n4q2GAIrCQzNyTZcAufvnc4iUuFJbmG1t5kY8s9VmuiBwbFP3PspuJfEP6n6cb4JqCEQXpKHZxKUH9gASOFWtGUHEnqjaSrWNaESBK0jQyoci_MohN0pNHgpD7YeAQegNxHIhuplU12P7tIL5ixwrCa9jkKugSIJphVy7i8gUkyjnb9HrVHDMhIvuQghNU34mxgaTryPaCEs5SUqHtwGOkF2qENcyStXTsCqkgStbZdwz9RcQAzrQZf10G5dj1vmVPdCNU2zWva9fjgLqkOzQ2ssjLXK-9-OhmT5rP3hPLYFbad3TGs6ihy-d-FIs4qfVsu4bLZIm93foAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsj40YOGCMaEwpxDrskn0Rd6dr46imR3PazF-CfleOByPl_vZJRl7k6SxiaTC52Hh-lGaAnyJqEEx8z-F7pBSNTEazuMfKyMemVv3kftCbB9JT4J9nN0o4dPEqvp04Zcv_R2ACEFwpxxZ6l7eCQFehQdVjUTXmery9K8i3zJM6lOZiPxfJilL5oR2YJxMtHTTwkxUGPrwBg0gmGu95RnTobzlYOqfLRe8foaci4kgqL_hHJo3W5SKwfRr7QdluSQh2sYVRc37KUTeMGergosbWC-wEJJpErNb98R2BoSgYCdxpOEagSbES7ch2m2iwlEfrgfnsmfoLmgzbGD_YC8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLO1Ir-nqa3X6IBli5m-VfsofC0TQsrQA2iFR-tZHLV3bG666EEZsuhcVbrzXgS9j-stFCERikg-NgO_K9reF298BIwbFsoSmueC4tlRpx4t1Fe2SleUouJejkyj5GMicfa2X8sUA3h9LMfYhATnGTuj0Z-cJdmWtIzEZyLcr0jxGZke7K5yAgF-HC808q-T6HXwpTrZM-0p-BMQtbWh7ljTVhNCkYtku5xX9Y6krPtF3MYv7w9OuO1QQda1mH63mLokyGQX4PmrThsy1BAWnelK3hywpw2oqfvFlchDG2bvFw7ccW92IXKwq1rHCBcoyQ7yWYC38gZSB8fg9MVxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
