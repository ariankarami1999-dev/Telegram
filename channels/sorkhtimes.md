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
<img src="https://cdn4.telesco.pe/file/nGVx4LkmBo_UM-gDYgiwuhgkItDgdngJbDaswq5LlYo2490oL5q32vi-JzSq622pBhaw59McSQaeXd9EYDRBMl0YmEl04_iZ1cq0xP-qblB-FKAcAfDaP_wj60pTvjagjkbWzmQ7lItVJZqiOdbx5lU3uUVsRGadGwm3UU0-NlReK-zKDg0_tiVgN83VanoglODNt9exlbXt8R0kufsekDN_EAgrAQy7SA03qpROyKOdSxrdAMux83sX-btySnXQHWrcWnsQPQTqLZl0nG_AypEqPjdReYc5becSlj-kcVz9n2JkRMAxUDDdrrWx8hRn3bITCbmblQWBCxUR0ALT1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 11:32:41</div>
<hr>

<div class="tg-post" id="msg-138650">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5M-g4IZ1yD5qfNFEJYIKT0AkoCLrhg8P2HT2o3PVy67jMNQ6YddEh4us1lQBcVIh3raDoa54x24AZAIJmNTdtlBNqkRFA4hNl02iNE-YWtRdP9U_1WcQRAXZJmvF9VQXK3G1aSNQbIEpGAIih6x4a0n2j5zHMso57AjoG7fWiDXwNT7Fs-teRVxPVwnMRrZxgL3NjRNjtKYTmnoYutLNHDoN0OaebIKXi7xOVRuXCvfbt_YnpyZ-UogE43z8Zoah_zS02t_5ESIkinvlyxVukTu8xrSL0GKOKOVsFqxeYwB-XX0ZXjeQ2Z2YNjZhMiFrc-4b4iKu2ioLZ_qui8TvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
❤️
برخلاف برخی شایعات مطرح‌شده، اوستون اورونوف در جشن پیروزی کنار هواداران حضور داشت و در شادی آن‌ها سهیم شد؛ او پس از پایان جشن، راهی رختکن شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SorkhTimes/138650" target="_blank">📅 10:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138649">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWDOB0-OaVjIEf-8_4jV5bDCyJRCjRvrKUYaNJ_Y7roDOsVkIahczVJ7mrL8auLSBjq2sWVOQ1lnrww-uTepJi6_b6ey87zrReS6yoqs-kRnrRy4BVV97k23uLsDcfXstWqQ5IBEIaK5qM37IPqWt3msKfKC94swrLRpXNNyVq-OFIpfZPknywRmsYtve8UjRudy_fdEAD_WFV2TGJFy5W9xRytBj7fhiApuAVn0o31fDKlJX_Xz1CiCK7EI9z5ull5QENYMmRx7XKcE-iA0cQM8wcD40GIAZUclxnAWOD8d2RX20bCzm2inZl-M_3sVE2D4JsPCYSAFlpQdsUJ9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
هفته‌سوم لیگ‌برتر فوتبال
✔️
پرسپولیس
🆚
تراکتور
✔️
🗓
تاریخ دوشنبه ۲ شهریور
⏰
ساعت ۱۸:۳۰
🏟
میزبان ورزشگاه تبریز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/138649" target="_blank">📅 10:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138648">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚽️
🔻
بازگشا: شیر ما برگرفته از هخامنشیان و نماد باشگاه ماست، اما شیر استقلال و نمی‌دونم از کجا اومده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/138648" target="_blank">📅 10:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138647">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
علی علیپور با دو پاس گل و یک گل بهترین بازیکن بازی امشب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/138647" target="_blank">📅 09:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138646">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhsiyEEBKstvgTJytQNBFxtekcUgh4jXEiAZwiLPKNf9BVhQ8J3PpSTdDQjLeA1nT9GkLsYJ7iDKFXmepgyp3ZM3o08Ns4yCz6Cnik3K2A1XfF01-jAKk1ZGf0vQgZ3w66HGHCa8D1If3YQONGKDxw0i9FXf3eH_tkd15k4tTMuqTqsWO2Dir0rk8bqhYwF90GsevsbBLrueIJJHFk56aS0tBjIuHISsYLj3rMc5OnE-exBksd3QQU4oQJAEJHe3BLIvPcGMNxpivhxCp08issgM1HjVnBwmGIlC0rHO0OVOFbgdtrRXzPSv8CQgJZAve_t77y1gEu-KFP3eesn2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارک کلاتنبرگ: گل استقلال خوزستان به پرسپولیس صددرصد آفساید بود چون مهاجم جلوی دفع توپ مدافع از روی خط رو گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/138646" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138645">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
حسن اکرمی داور بازی پرسپولیس و استقلال خوزستان شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/138645" target="_blank">📅 09:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138644">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3h5WN7vmQP6qVZVN34bvp1msjW6oy6qAQf1dQ2ZcZrtw3o9-yNcDbjqS52Gxu2eangPLaCpH_eNVuMkZ_Jm-nQMPo1ceF_rCg4j7ohXBejumvkyS10bvfFd82ZNbsOn20Uq3nrKetda2kz_U_vFTv7p1kay5CFbLRxERPLTQ3B36p17xrJ0aVhO2Cdnlcug5_B1KociF2WovUdJjQbLhahXjP7kAr4wvSScW4LO6iEdtRLW8ts080cQxoCJNS3yWa1I7u2teBjK8fJHl1DM_bHMB-3Wu2XfYAMq-M6uNT1h0e9SrS5_hfKr_taN8rE8nSN_ybgJqiuKpy-ZJFPLSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇺🇸
ترامپ: از این لحظه شدیدترین فشار اقتصادی تاریخ که تا به حال علیه یک کشور بوده، علیه جمهوری اسلامی اجرا می‌شود و‌ «هر کشوری» هرگونه کمکی از جمله اقتصادی، نفتی، صرافی و بیزنسی به ایران بکند را شدید‌ا مجازات می‌کنیم. این دیوانه‌ها گرفتار شدند و به آخر خط رسیدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/138644" target="_blank">📅 08:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138643">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
صبحی که تیم محبوبمون توی ی بازی جذاب و دیدنی بازی و برده بخیر.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/138643" target="_blank">📅 08:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138642">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">➕
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
➕
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
🔗
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/138642" target="_blank">📅 03:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138641">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8ef11ffd0a.mp4?token=srRhDDqpqTTXR02gLRMufgy8uRndPGRbsKNDuBhXV-Qb7Vug3DiXBh6tbcQRiR1HsClC5rxD1bNwKUktCL4piNJm5lhoTgpM4Aw2ImCJqgIoS6U8tlxOBigH95ESm_Uczj3_HfSTbkCx2Yc4r9JZ6QpDSA5dA8cf3boK6MF3RUc1Oj2KoII0xWjOkX1b-hbgCVH3j69VSX48f4QS3ZUCgHmGWb_V7hdQagXxbmVA82ToOPCpJCAC0SwgDWYg_Mf-hqKKXX9ztEuAdayqTN9QJKXGTtn5Dzr0E1SnIB3n5EWpaKoa8ZaiCvoEVo6lo1OCRWKT_USsvBNyb3PvJj_P_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8ef11ffd0a.mp4?token=srRhDDqpqTTXR02gLRMufgy8uRndPGRbsKNDuBhXV-Qb7Vug3DiXBh6tbcQRiR1HsClC5rxD1bNwKUktCL4piNJm5lhoTgpM4Aw2ImCJqgIoS6U8tlxOBigH95ESm_Uczj3_HfSTbkCx2Yc4r9JZ6QpDSA5dA8cf3boK6MF3RUc1Oj2KoII0xWjOkX1b-hbgCVH3j69VSX48f4QS3ZUCgHmGWb_V7hdQagXxbmVA82ToOPCpJCAC0SwgDWYg_Mf-hqKKXX9ztEuAdayqTN9QJKXGTtn5Dzr0E1SnIB3n5EWpaKoa8ZaiCvoEVo6lo1OCRWKT_USsvBNyb3PvJj_P_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس در پایان بازی با نظافت سکوهای ورزشگاه، کار قابل تحسینی انجام دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/138641" target="_blank">📅 00:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138640">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tysEP-QQSEq-a1KzBt93-mVSRYVtxyW1V5eRuyiZBU5Mb3xq6me8BH57rGsGQsGHD2uzdB3ScfS3kpdFVAlG0TLJ0hJm-ZX-u5urXmG-uNz9lv80cZyuOGpPUmx5VUbG-3W7nOG16JQpIihdRJS_Oasc7VJH8fw4BCpL3vAPBifl85fyJGCu5zS2fhGaPKVElvDNEiGPpiDN_F-Tn4t-JN1vbu0Hzl9Dyxiu9kB6VlnIVwov80NF3W6dirKHswJbJazYQwRJyGpkxk1jHblc3SScm5mfIkQBKgcxSSyMqUKBaz40FF5_RdoNkxooXJbKOdwBhD0Z-dchiAZMh2cBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💯
میانگین سنی بازیکنان تیم(ترکیب اصلی و تعویضی) در بازی امشب 27٫81 بوده!
✅
تیوی بیفوما با 34 سال مسن ترین و پوریا شهرآبادی با 20 سال سن جوان ترین بازیکن امشب پرسپولیس بودند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/138640" target="_blank">📅 00:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138639">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
✅
دردسر شیرین تارتار؛ ۴ مدافع برای ۲ جایگاه
‼️
⬇
⬇
⬇
با اضافه شدن دانیال ایری، تارتار حالا کنعانی، زارع، ابرقویی و ایری را برای قلب دفاع در اختیار دارد. زوج کنعانی و زارع در هفته اول خوب ظاهر شدند، اما حالا رقابت برای ترکیب اصلی جدی‌تر می‌شود؛ مخصوصاً با توجه…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/138639" target="_blank">📅 00:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138638">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
#فووری
❌
طبق شنیده ها, حمیدرضا گرشاسبی برای صدور رضایت نامه ابوالفضل رزاق پور با مبلغ 120 میلیارد تومن رضایت داده و تنها موافقت حمید مطهری مانده تا این بازیکن پرسپولیسی شود
❌
❌
البته بعید است مطهری راضی شود مگر آنکه....
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/138638" target="_blank">📅 00:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138637">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvrQIex4ChPe_MQvFQhOHCmb3Jhlty1Mw-WE89mnLiBTzGWyyEE7tMkLLrf91fb4i5J9LPP8yCrg4N6DkUx1V70RTEeYq3f0bEbf3vDyZq7L2svCutLaZ2cLBA-FqE51fNotn44zI-WlpQEyep0a1gxGrNqfZ3w627F9ZfyQoLUhi-Jn0jPvr3F7TaxDPq45fRRFdTJixYC_1BkgPbknhAxxNX287byydLkJwz2I1Bm74rBneDCBKL5baIG5BOT9OuvJ577D9Krl_NUfMhycGzBqBiv4v1KO4UcZyPgskxfDeHoL8qOtIUb9N1BTwOprJCOOReoJVVS3clj-WmZbIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صحنه‌ای که کرک و پر ابوالفضل جلالی از پرش محمدمهدی زارع بعداز گل محمد خدا بنده‌لو ریخت
😂
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/138637" target="_blank">📅 00:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138636">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
📱
استوری محمودی کنار بیفوما  بیفوما: عشق منی محموش ؛ فدا بازی
😂
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/138636" target="_blank">📅 00:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138635">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384e0a5eb3.mp4?token=lizYXPB7XezQ5tEFqsfqm9kdyK1Y65bSvoy4w9Mc5O4RExqMNx4Y0tB8Wr3RfXxhTt9fZWWLFygg0jJLEOYF4QM4Rg52xQoW_uWMyPumRe9zTWfg6_-wEsuLatN76a-kbQViQ1iruBORnbNIJr6EJzbuQ1rrRmmPGYuu5NB-t8mlM5QODB_nj_VGmcqExOA43KotYVLyGDMUTENOOXEK5LF1GirtRmv3RQf3UR0AAyauBY8h-7urmoqwpgbTqx-huGr4qpY50LF41WApnARigJj9rFdrirZsI0i7ce3HcaQTgrUxEa_6UNO7wEcCOv4reUxk50BpQ5kJy-dscqXbvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384e0a5eb3.mp4?token=lizYXPB7XezQ5tEFqsfqm9kdyK1Y65bSvoy4w9Mc5O4RExqMNx4Y0tB8Wr3RfXxhTt9fZWWLFygg0jJLEOYF4QM4Rg52xQoW_uWMyPumRe9zTWfg6_-wEsuLatN76a-kbQViQ1iruBORnbNIJr6EJzbuQ1rrRmmPGYuu5NB-t8mlM5QODB_nj_VGmcqExOA43KotYVLyGDMUTENOOXEK5LF1GirtRmv3RQf3UR0AAyauBY8h-7urmoqwpgbTqx-huGr4qpY50LF41WApnARigJj9rFdrirZsI0i7ce3HcaQTgrUxEa_6UNO7wEcCOv4reUxk50BpQ5kJy-dscqXbvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
📱
استوری محمودی کنار بیفوما
بیفوما: عشق منی محموش ؛ فدا بازی
😂
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138635" target="_blank">📅 00:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138634">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
در یک پست باید تقویت شویم
❌
از مدیریت باشگاه تشکر می کنم و از آنها می خواهم در پستی که مشکل داریم بازیکن جذب کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/138634" target="_blank">📅 00:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138633">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpaFWV18R_GqQOGbZ2wHs-5yQ1XJYzBJjzG1J2ZBnSzR89AMRroGq63grgdK6E-RiuUcrRPLg082J0dOUruC_tQmCSjPIyZIqy9ctPkIaUlRbpipYzjs7IH0kVMyaDrs_LB7J5D71fGSP0DvZHzknroGfZ9OmzII5lbZhpIvXmIFZ9xr2NODsi7bhCe9a4sN6DwDoO3Kl1tdWFG0v68ngzK7PBzipWuT4IF5VtKP4dO2Kd9ot1huWvDbXuDo-5tZR-7eaxEDiVjTGFz-88CK7tQgyzsj4Zieh6FE-VYuu4kaglZHZaYMi_dSnhTXHiH73iiFSQekzWoqvJJYeanuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی علیپور با دو پاس گل و یک گل بهترین بازیکن بازی امشب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/138633" target="_blank">📅 23:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138632">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCFcCUrrVL7Hjjkfb6dCUIk9R-6kk2l8fXkS8Dy_auRQpuj_IzycKsyLR3Lp-qNkwweeBzeUgTODC4Y1cbXvP3KwPcQJmFRhftZaKrU1EAKfnIh-zN0yEJtNyQ6J93LxoFamqrUcmHFYGb-8tTJhi0r-3wKuYM6OIAuvlztfqEufZGy_s8Ry7OCFdHfRchzb12yoXp6rcVOJpW83Yngqhe2KjFRyOGH2tRHAWnPT7Xycx1GjZEO2BMd9By6n6w5zuu36nrsWYC299PJtsUlyjMYz1ddDlBxsQrW_94OEa9qFAe0nNKIuzY_ZdYYMYPKLpEZ_1B05H2SZFC3jF7iRiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
علی علیپور، مجید عیدی و ایگور سرگیف با نمرات 8.8، 8.4 و 8.0 بهترین بازیکنان دیدار امشب دو تیم پرسپولیس
🆚
استقلال خوزستان بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138632" target="_blank">📅 23:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138631">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
✅
بهترین بیفومای دو فصل اخیر بوده .عالی بودی پسر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/138631" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138630">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
♦️
ممنوع المصاحبه ای بازیکنان؟ در این مورد من مطلع نیستم و باید بدانم ماجرا چیست. چنین چیزی با من هماهنگ نشده و این بحث مربوط به مدیر رسانه است.‌باید به هواداران تبریک بگویم و امروز سنگ تمام گذاشتند
♦️
اینکه نیمه اول در تایم زود…</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/138630" target="_blank">📅 23:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138629">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
تارتار: چون جلالی از قبل هم مصدومیت داشت، وقتی نتیجه ۲ بر صفر بود ترجیح دادیم ریسک نکنیم و او را تعویض کنیم.‌ما در پست او همایی‌فر را هم داریم که از جوانان خوب است اما نیاز داریم در این پست تقویت بشویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138629" target="_blank">📅 23:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138628">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b3360c20.mp4?token=jXQzljBJt5SZPON3-pEoPPxkxHBdjmu6kSvBHH4qFdMytTy7zbaTq0QBhHjGZJxHLC8OvpgJXpVa9JeOMqab0sRkLVyFz4vXUhsjQ4vSIJmWMsjtX9OIv9m04A-vl79khLubzPfkptflcQBgEMBy25tFio2BCpqj7A7nUkVCUFE5hKYW_0no4MHGVfqlXaxhci1gDm676-cRc2wa8JAAvF7K2HoMCRdNr3oIVRTel5R0zXAyELDU_F8EiNafKHuOIAbSLoHhLEBdQN5i8mNO-X3hNXAhDLa5bxEkTo9RipalAhEGOMLt8xuwvjPGQEUKKQ7S6968jUnZUeiwe9bK64WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b3360c20.mp4?token=jXQzljBJt5SZPON3-pEoPPxkxHBdjmu6kSvBHH4qFdMytTy7zbaTq0QBhHjGZJxHLC8OvpgJXpVa9JeOMqab0sRkLVyFz4vXUhsjQ4vSIJmWMsjtX9OIv9m04A-vl79khLubzPfkptflcQBgEMBy25tFio2BCpqj7A7nUkVCUFE5hKYW_0no4MHGVfqlXaxhci1gDm676-cRc2wa8JAAvF7K2HoMCRdNr3oIVRTel5R0zXAyELDU_F8EiNafKHuOIAbSLoHhLEBdQN5i8mNO-X3hNXAhDLa5bxEkTo9RipalAhEGOMLt8xuwvjPGQEUKKQ7S6968jUnZUeiwe9bK64WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🎙
پوریاشهرآبادی؛مهاجم پرسپولیس:
🔻
امسال تیم یکدل است.
🔻
همه بچه‌ها جان خود را برای این لباس می گذارند.
🔻
تیم ما لیاقت قهرمانی دارد.
🔻
پوشیدن پیراهن پرسپولیس آرزوی هر بازیکنی است.
🔻
مهم نیست چه کسی گل می‌زند و مهم بردن تیم است.
🔻
بوسیدن لوگو؟!این عشق بچگی است.
🔻
رقابت در خط حمله نیست و رفاقت داریم.
🔻
تارتار پرسپولیس را متحول کرده است.
🔻
در مورد وضعیت تیم امید و باشگاه نمی دانم و آنها باید حل و فصل کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/138628" target="_blank">📅 22:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138627">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb8538e6b.mp4?token=MZ-bzMWmqTMf5whyowhkmeDaU0RDUsISiE2vXq9a3T_MU8ZApTw6GWCC_zAh_TltkTSTfn5TEuq8CjfWMEm2HHMA9oSPOqR-PyWn_DyUVEx6LGzIig1rD5Rl5TSi1mPywlDrCgzIPut1EBZ8IzhvFXCjMNUnOJ1FBCqS5jiOvTd5frZFMi9ugovS2OQAe57TPkgWWh0h7U-rF1TqQGox5mhsQiqQXrRsEoAXed3v0JRnBuHJzUL49cLYOgK_XIQ_lWyZEuytC9h0oLlp8rhUSmYAq4oTDD5iMR09zxV8Q0ZNw6lPWhSswtKHG1oZRnBjNrlrEaa-_UOqz-XB2DrhMzZ_ZCzm3hPy1tx8lXlL5cwSt3KtQNQoV8txJz8ivDMGwweg9jsNImbOf3lBi8aXYTH77IhFD3idmDtpQ2JmK182SnR0AyR6gdqGGJXYNpO5o9nneWw9JuKFvZYsR2jXb5Eao92-GVyOKaCBQobf30DxVh8iesRNe0-dPYJeBNfAgzRuf55WvoIp0nVUkmYv2rIOJzlw_OORWqpAP0eDoNreI8l-Rg6La0QBYKH-kwhqYilHxutm9KVBRsCnfTAl082fMO2hgInlsIM8FPkL9t8WFPNFjfrKGGtAmBJY_7SCHUsyEPiR0sJ7p4CBvN1S-FbSaEb5GzNxE5CYYRb5Zao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb8538e6b.mp4?token=MZ-bzMWmqTMf5whyowhkmeDaU0RDUsISiE2vXq9a3T_MU8ZApTw6GWCC_zAh_TltkTSTfn5TEuq8CjfWMEm2HHMA9oSPOqR-PyWn_DyUVEx6LGzIig1rD5Rl5TSi1mPywlDrCgzIPut1EBZ8IzhvFXCjMNUnOJ1FBCqS5jiOvTd5frZFMi9ugovS2OQAe57TPkgWWh0h7U-rF1TqQGox5mhsQiqQXrRsEoAXed3v0JRnBuHJzUL49cLYOgK_XIQ_lWyZEuytC9h0oLlp8rhUSmYAq4oTDD5iMR09zxV8Q0ZNw6lPWhSswtKHG1oZRnBjNrlrEaa-_UOqz-XB2DrhMzZ_ZCzm3hPy1tx8lXlL5cwSt3KtQNQoV8txJz8ivDMGwweg9jsNImbOf3lBi8aXYTH77IhFD3idmDtpQ2JmK182SnR0AyR6gdqGGJXYNpO5o9nneWw9JuKFvZYsR2jXb5Eao92-GVyOKaCBQobf30DxVh8iesRNe0-dPYJeBNfAgzRuf55WvoIp0nVUkmYv2rIOJzlw_OORWqpAP0eDoNreI8l-Rg6La0QBYKH-kwhqYilHxutm9KVBRsCnfTAl082fMO2hgInlsIM8FPkL9t8WFPNFjfrKGGtAmBJY_7SCHUsyEPiR0sJ7p4CBvN1S-FbSaEb5GzNxE5CYYRb5Zao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
♦️
ممنوع المصاحبه ای بازیکنان؟ در این مورد من مطلع نیستم و باید بدانم ماجرا چیست. چنین چیزی با من هماهنگ نشده و این بحث مربوط به مدیر رسانه است.‌باید به هواداران تبریک بگویم و امروز سنگ تمام گذاشتند
♦️
اینکه نیمه اول در تایم زود به گل می رسند جای خوشحالی دارد. یک گلایه ای هم از داوری داریم که امروز تمرکز داور در 20 دقیقه آخر از بین رفته بود. خطای روی عیدی و توپی که به دست مدافع استقلال خوزستان خورد نیازمند دقت بیشتری بود. همه بازی های پرسپولیس سنگین است و داور باید دقت بیشتری داشته باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/138627" target="_blank">📅 22:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138626">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0042859545.mp4?token=S6LFK9rzeyRIg3ygTTBJoMo8IiBlcCrmeWuj4IgD_73FLHRzYJmwqDNwzIbGl9A_WUNRyUnkWazqu32Q7d1cbx-Qt_TuersjF4dGRS3seKe_Eze1DphrShlne2YYGAzSG4DgaIGGcdOY3nosYtd72ut63u4Y2nzw2LZNC04qZWIEKJStxIMsd4DHINEbL1eDPvgeq5pgxdFo2WdCj0GfS4TjMtrl2rcChhL0x-0OZgnj9Y5rMBaQwXgK3XeQD7jphIZjSlpLq1vEBIagZNP5mtfJty7gHDOQWXzOvwJ2PPhXGu_nKTEr1q_Ge-yvt6bINhT-Ozy7qYogEmb8wIcwQTC_KhfKl8CCkRwwEAqbCU_C4CjyYyuQhH6R040oRBoSvh4tS6BLxCD7payVqiSzgLgW2kARQq8b62csEp-x8Ks-_vDtYNWzM2dj7A37blgyuyyrGT-0ZjU2Dojhde60To4HbekiYChAPHlJvSOdJyxLowsynyuOzrfh56gYOZC3QYN2gIUbf2KRGPGpNmHttPGgVHe0adgNFvBh-qzhaBVMKGtoXhQMrW5RYXubqYXtVnEuKLwQFGBc4FwpPFll1GWz-bcPkIVAKl2XvBxvGRX9W6BvY398eqSdFj2Win3JNstN2TZbyZV3WUANUTGj40hQC6V2T3tMP28NumOh1jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0042859545.mp4?token=S6LFK9rzeyRIg3ygTTBJoMo8IiBlcCrmeWuj4IgD_73FLHRzYJmwqDNwzIbGl9A_WUNRyUnkWazqu32Q7d1cbx-Qt_TuersjF4dGRS3seKe_Eze1DphrShlne2YYGAzSG4DgaIGGcdOY3nosYtd72ut63u4Y2nzw2LZNC04qZWIEKJStxIMsd4DHINEbL1eDPvgeq5pgxdFo2WdCj0GfS4TjMtrl2rcChhL0x-0OZgnj9Y5rMBaQwXgK3XeQD7jphIZjSlpLq1vEBIagZNP5mtfJty7gHDOQWXzOvwJ2PPhXGu_nKTEr1q_Ge-yvt6bINhT-Ozy7qYogEmb8wIcwQTC_KhfKl8CCkRwwEAqbCU_C4CjyYyuQhH6R040oRBoSvh4tS6BLxCD7payVqiSzgLgW2kARQq8b62csEp-x8Ks-_vDtYNWzM2dj7A37blgyuyyrGT-0ZjU2Dojhde60To4HbekiYChAPHlJvSOdJyxLowsynyuOzrfh56gYOZC3QYN2gIUbf2KRGPGpNmHttPGgVHe0adgNFvBh-qzhaBVMKGtoXhQMrW5RYXubqYXtVnEuKLwQFGBc4FwpPFll1GWz-bcPkIVAKl2XvBxvGRX9W6BvY398eqSdFj2Win3JNstN2TZbyZV3WUANUTGj40hQC6V2T3tMP28NumOh1jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣
محمد حسین کنعانی زادگان، کاپیتان پرسپولیس:
❌
❌
من به تک تک استقلال خوزستانی ها افتخار می کنم و بعد از بازی به رختکن آنها رفتم.‌بازی تراکتور و درخواست برای حضور تماشاگر؟ فعلا بگذارید این بازی را بگذرانیم و بعد کارهای لازم را انجام می دهیم
❌
❌
ناراحتی اورونوف؟ اصلا چنین چیزی نبود، در تیمی مثل پرسپولیس بازیکنی بازی نکند طبیعی است که ناراحت شود.‌هر چه آقای تارتار تصمیم بگیرد همان می شود و تابع هستیم. گلزن تیم فرق نمی کند، من دوست دارم تا آخر فصل گل نزنم اما پرسپولیس قهرمان شود.‌خوشحالی من حرکت موزون نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138626" target="_blank">📅 22:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138625">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guVJMKFAXQjRtR8eA9RLihZn1B7sDKQqSLqq_sTjw2BNbguO4VoDAM7m8lCbWhx3wLAIr37AaLtqwlDnK99_1PWOAQaF3bxzcXEbS5d3VYeDeUsclN90_eLE9ATZgsE7ZfdYSm7D9Gsvfy1MQ9sSuXLxbUNFnTsQ6yPWx_IknqQ90NLpsGc0WMp_U27rd9RLxcDmFhLNqvvsO65C8iTeMGAT7Rro3tCGYy5iPdSXd-Eu_gIRMZXCgiFnVsL5-SxKSjgn274MNW8BPMZamKVhoC7FVvkHkopVgiXi8EmkXJla9Ej9Veirg-ojvJYrXgqDHzM1S95SdznJUJVj1sBuSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جدول لیگ برتر پس از پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138625" target="_blank">📅 22:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138624">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
مهدی تارتار، سرمربی پرسپولیس:
❌
گلی که خوردیم از شیرینی برد ما کم کرد
✔️
✔️
دوست دارم هم خط دفاع و هم گلرمان جزو بهترین ها باشند
✔️
✔️
از جلو خوب فشار به تیم ها وارد می کنیم
✔️
✔️
به جز نیازمند درون دروازه رفیعی را داریم که خوب کار می کند
✔️
✔️
دلم سوخت که…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/138624" target="_blank">📅 22:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138623">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✖️
✖️
مهدی تارتار، سرمربی پرسپولیس: بازی با تراکتور و درخواست برای تماشاگر؟ فعلا می‌خواهیم امشب از برد خود لذت ببریم
❌
از داوری امروز توقع بیشتری داشتیم! در صحنه‌ای که علیپور به سرگیف پاس می‌دهد مدافع حریف توپ را با دست می‌گیرد!
❌
داور می‌توانست برای ما پنالتی…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/138623" target="_blank">📅 22:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138622">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یکی از نکات مهم اینه که فصلهای پیش جلوی تیمهای ته جدولی امتیاز از دست میدادیم</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/138622" target="_blank">📅 22:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138621">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">یکی از نکات مهم اینه که فصلهای پیش جلوی تیمهای ته جدولی امتیاز از دست میدادیم</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/138621" target="_blank">📅 22:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138620">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
مهدی تارتار، سرمربی پرسپولیس:
✔️
✔️
هدف ما از اول این بوده همه بازی ها را ببریم. هواداران پرسپولیس این شکل بازی را دوست دارند. بر اساس فلسفه هوادار خواسته های خود را جلو می بریم.‌در یک پست باید تقویت شویم .از مدیریت باشگاه تشکر می کنم و از آنها می خواهم…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138620" target="_blank">📅 22:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138618">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
مهدی تارتار، سرمربی پرسپولیس:
❌
باید از هواداران تشکر کنم که در برد امروز سهیم هستند.از بازیکنانم کمال تشکر را دارم که از دقیقه یک فوق العاده بودند. نشان دادند امسال می توانند کارهای بزرگی کنند.استقلال خوزستان کادر و بازیکنان جوان و خوبی دارند
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138618" target="_blank">📅 22:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138617">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
مهدی تارتار، سرمربی پرسپولیس:
❌
باید از هواداران تشکر کنم که در برد امروز سهیم هستند.از بازیکنانم کمال تشکر را دارم که از دقیقه یک فوق العاده بودند. نشان دادند امسال می توانند کارهای بزرگی کنند.استقلال خوزستان کادر و بازیکنان جوان و خوبی دارند
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/138617" target="_blank">📅 22:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138616">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
تشویق بی امانه تارتار در استادیوم ..همگی دارن از این تیم هجومی و جذاب لذت میبرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/138616" target="_blank">📅 22:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138615">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📌
به عقیده من تیم با خرید یکی دو بازیکن دیگه ۱۰۰٪ تکمیل میشه
❌
یه دفاع چپ و هافبک دفاعی… بنظرم میشه به همایی فرد اعتماد کرد چون دفاع چپ ایرانی تو مارکت نیست و اگرم بخایم خارجی بگیریم باید با دو تا از خارجی ها فسخ کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/138615" target="_blank">📅 22:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138614">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔖
⚽
به باد این دوتا برد نباید بخوابیم،عیار تیم تو بازی های بزرگ مشخص میشه، با دو تیم نسبتا ضعیف بازی داشتیم اما عالی بودیم اما هنوز برخی ضعف های تاکتیکی هست که باید رفته رفته برطرف بشه ولی از همه جهات این دو بازی عالی بودیم تمام بازیکنان مون عملکرد خوبی به نمایش…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/138614" target="_blank">📅 22:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138613">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔖
⚽
به باد این دوتا برد نباید بخوابیم،عیار تیم تو بازی های بزرگ مشخص میشه، با دو تیم نسبتا ضعیف بازی داشتیم اما عالی بودیم اما هنوز برخی ضعف های تاکتیکی هست که باید رفته رفته برطرف بشه ولی از همه جهات این دو بازی عالی بودیم تمام بازیکنان مون عملکرد خوبی به نمایش گذاشتن
◀️
و به لطف باشگاه تیم خوب و سرحالی بسته شده، همه باید از تارتار و حدادی حمایت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/138613" target="_blank">📅 22:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138612">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
حساس‌ترین بازی هفته سوم لیگ برتر پشت‌ درهای بسته باید برگزار شود؛در شرایطی که براساس رای فروردین 1404 کمیته انضباطی و تائید استیناف تمام دیدارهای تراکتور و پرسپولیس مقابل هم در مسابقات لیگ برتر جام حذفی و در دو فصل 1405_1404 و 1406_1405 باید بدون حضور تماشاگر…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/138612" target="_blank">📅 22:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138611">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
رسمی؛ با اعلام سازمان لیگ دربی پایتخت برای اولین‌بار قرار است در اصفهان و ورزشگاه نقش جهان برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/138611" target="_blank">📅 22:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138610">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9bca5c905.mp4?token=maKqyPalGPreNJkvYe2jtKTZ5MuzKEBUUGIOQLu1MeSPqRNsioAAoPEDH6nVL9Br3taB7nxWmNbwMRUdXaZ6-2HrJPeo-h9SPaR-GGv2s77p9LKRPG6eU-v_k-7sZjyIrXWN0T-UYFUBKXVQOfEU1DBnKBtuxNs4nqwSCmg6pYEEytuVc4oybbhKqN8_cMBHdy-778MfGxmWnSnt9lv7S07XdOKNNncS55TQoEZQdn99lGqDHKz8xjlp0FX7fbGjNOvBf8_FromK_mc7XfWy2TXyo4GOhfftGDYb13NRPkQVpRiKHjoHw9rOtyXX3A9ulCeuuKhvyj6rVu1SpggKfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9bca5c905.mp4?token=maKqyPalGPreNJkvYe2jtKTZ5MuzKEBUUGIOQLu1MeSPqRNsioAAoPEDH6nVL9Br3taB7nxWmNbwMRUdXaZ6-2HrJPeo-h9SPaR-GGv2s77p9LKRPG6eU-v_k-7sZjyIrXWN0T-UYFUBKXVQOfEU1DBnKBtuxNs4nqwSCmg6pYEEytuVc4oybbhKqN8_cMBHdy-778MfGxmWnSnt9lv7S07XdOKNNncS55TQoEZQdn99lGqDHKz8xjlp0FX7fbGjNOvBf8_FromK_mc7XfWy2TXyo4GOhfftGDYb13NRPkQVpRiKHjoHw9rOtyXX3A9ulCeuuKhvyj6rVu1SpggKfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🎙
بهنام ابوالقاسمپور؛مدیرعامل استقلال خوزستان:‌
🔻
با حدادی در مورد بیفوما حرف زدم.
🔻
ما باید مبلغی به کمیته وضعیت می دادیم اما چون ندادیم نورشرق به نفع پرسپولیس رای داد.
🔻
الان پول رسیده و باشگاه پرسپولیس هم گفته مشکل را حل کنیم و دیگر کار به دادگاه عالی ورزش نرسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/138610" target="_blank">📅 22:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138609">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/154eade970.mp4?token=hjrY9bbkX3Evv5TVqY5Hpbl3OAvuX-bzUG-fyqn4EF2-W14UXuJxdvVFJLYAfpCEhNCqwkAqkeWFpKnHOk7bEHfpVrJ-Nism58piwxX6TjjeG7oYpPD-QP9L-t-9R5rBtJ8zRYS_bBowjFr7O7OIX259qRt2fnHrucQI5LcG82oUpQqW73mgcXqXoXnRAANtqVGEgpI8_9yQVZQ1FosOSUYJWlzpdo1p2t70OY9Vd2SULNqY9j1BxWKQnNeD0hrjp08aNo_zi1S3NP5ZLdPMxpdXVbg9tMEkDrOQoq7ncPXndFC3_fKx2ICRAcGdJC04LJTUwUWzcCaAuEIdBX3XDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/154eade970.mp4?token=hjrY9bbkX3Evv5TVqY5Hpbl3OAvuX-bzUG-fyqn4EF2-W14UXuJxdvVFJLYAfpCEhNCqwkAqkeWFpKnHOk7bEHfpVrJ-Nism58piwxX6TjjeG7oYpPD-QP9L-t-9R5rBtJ8zRYS_bBowjFr7O7OIX259qRt2fnHrucQI5LcG82oUpQqW73mgcXqXoXnRAANtqVGEgpI8_9yQVZQ1FosOSUYJWlzpdo1p2t70OY9Vd2SULNqY9j1BxWKQnNeD0hrjp08aNo_zi1S3NP5ZLdPMxpdXVbg9tMEkDrOQoq7ncPXndFC3_fKx2ICRAcGdJC04LJTUwUWzcCaAuEIdBX3XDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
شادی هواداران پرسپولیس و اعضای این تیم پس از سوت پایان بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/138609" target="_blank">📅 22:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138608">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c286dc680.mp4?token=QahQO88x35PmuYu-ibSWFzo-JrOD58xw6u1kSMwC6AuYIQMBZcW-cvNWxnZT_vTbO3_2lbbPv3mgiDgbCzy3e-KwBYBsFXrNmXMboNT_YU_z9PKv2GnQwyrAwKa5GUmGGoXdlGoKsPfGzbRykdsMNvUGqt-AFmJQGBjlC75P-OWXQKg6GShUZvNSuj7KrMPrUBdrRL4sD96O8VpBn6aks4S3r1DHunPxRkNKhJ_ZffrSovlxjEZC5gmMwU0Cd2hcO0AnCD0CREqccsBR7DL1bycG3zNRMENysJNaTiNW2kOFfUMwv-NfRHrZGRtjvP8b74aqgHza0wqy3vuJXONYmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c286dc680.mp4?token=QahQO88x35PmuYu-ibSWFzo-JrOD58xw6u1kSMwC6AuYIQMBZcW-cvNWxnZT_vTbO3_2lbbPv3mgiDgbCzy3e-KwBYBsFXrNmXMboNT_YU_z9PKv2GnQwyrAwKa5GUmGGoXdlGoKsPfGzbRykdsMNvUGqt-AFmJQGBjlC75P-OWXQKg6GShUZvNSuj7KrMPrUBdrRL4sD96O8VpBn6aks4S3r1DHunPxRkNKhJ_ZffrSovlxjEZC5gmMwU0Cd2hcO0AnCD0CREqccsBR7DL1bycG3zNRMENysJNaTiNW2kOFfUMwv-NfRHrZGRtjvP8b74aqgHza0wqy3vuJXONYmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
گل چهارم پرسپولیس به استقلال خوزستان توسط پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/138608" target="_blank">📅 22:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138607">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34f62d7868.mp4?token=Qlz3yoE32BFe428jX2kwFJi2UOx76FmaNAmV061SH4JQVOK7OCWlha2Q4bqQAKxfCCTrLoCLAQIrzKHOnkDBkAxss4uI_8k-nQyYDIwMWVnzWleY9-OiT9pYckXkJ9_SZvTxl5nrvaoUPkuHnZn8AAa4R1eMBBrIebCiVo7dBMfSLRu9yMwQoiiBH_vN0equZLzsidfaVa0qRBuGHLc6qUnP4IEpy65F9lL6-Lov41Vxc0r-5nQNo4ar-n6TNbqG0mCoQNkRmY5nAvOkevoWcBTHmpcuilFuPos-QO5owZe_N5MNOsrYcEkpHVUTa_--lXKcNpO95tIftlZizlnbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34f62d7868.mp4?token=Qlz3yoE32BFe428jX2kwFJi2UOx76FmaNAmV061SH4JQVOK7OCWlha2Q4bqQAKxfCCTrLoCLAQIrzKHOnkDBkAxss4uI_8k-nQyYDIwMWVnzWleY9-OiT9pYckXkJ9_SZvTxl5nrvaoUPkuHnZn8AAa4R1eMBBrIebCiVo7dBMfSLRu9yMwQoiiBH_vN0equZLzsidfaVa0qRBuGHLc6qUnP4IEpy65F9lL6-Lov41Vxc0r-5nQNo4ar-n6TNbqG0mCoQNkRmY5nAvOkevoWcBTHmpcuilFuPos-QO5owZe_N5MNOsrYcEkpHVUTa_--lXKcNpO95tIftlZizlnbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
❤️
گل سوم پرسپولیس به استقلال خوزستان توسط ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/138607" target="_blank">📅 22:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138606">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6f4fb205d.mp4?token=Twl1YCNvu_T0IjS2Zjmg2M1l1itGs934fR46B5PEVke57-i3_px8A-QV1tLRB-cA-pMDA6vG50WkwW1yCM8bC3BhvQbqsN6V0oeeS8CcnjmiacdPwfVEFLMV6Ddkf2UB5kRapc8ol30KCp2BsBm_t-A-92DpnpM4VOwqVvTquY7zi7-TaL-q2rqu9f6t0tS49Ch_ObJa0cuP-tIpohJzyRlC3Zg_m30n5TJhLm9XxFFdFhdQWOMnf1qRYcXtfrcFpokJEfyDJEJ2N_P-jXGQf1wr98NrOZPqXOEqtkVA2pbzBw2l4Ls2yqVmWbvAPBSdoREU5q45ti4fQu51T3otQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6f4fb205d.mp4?token=Twl1YCNvu_T0IjS2Zjmg2M1l1itGs934fR46B5PEVke57-i3_px8A-QV1tLRB-cA-pMDA6vG50WkwW1yCM8bC3BhvQbqsN6V0oeeS8CcnjmiacdPwfVEFLMV6Ddkf2UB5kRapc8ol30KCp2BsBm_t-A-92DpnpM4VOwqVvTquY7zi7-TaL-q2rqu9f6t0tS49Ch_ObJa0cuP-tIpohJzyRlC3Zg_m30n5TJhLm9XxFFdFhdQWOMnf1qRYcXtfrcFpokJEfyDJEJ2N_P-jXGQf1wr98NrOZPqXOEqtkVA2pbzBw2l4Ls2yqVmWbvAPBSdoREU5q45ti4fQu51T3otQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
گل دوم پرسپولیس به استقلال خوزستان توسط علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/138606" target="_blank">📅 21:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138605">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fbb512d19.mp4?token=IUK-RyGJ1-WFAvDZMFwqCTfvnx1z9dmCxxjrpqzSl6UYUWlajwwyex58cB7NPZ4lDS0RJrIVTSa1LttThK_HmhfcGo1_OUdOZE2xSQXSQBLFpJmGnVtdT6MrZkC9Rz2wB3E-ZOWxtaHNmxE_MRUO1kH5ogtZJS1HYgjhOUoMeWizsN9cJF0D7XB8TDnMPn8e2Xn9UC95aaj6YZAUKol-OPeFR6K-rKXQkvyQMsDj9Vf90vSL1OFWYrs6O8qB9yLnzu2cIWdoOiN1HOo0-v3aEJ3oxWCtpKsJUkTlyWAF4SVkxYglEG_-6b_fyTT5OCr5iqP8loXEQvoy_9VZTcHN5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fbb512d19.mp4?token=IUK-RyGJ1-WFAvDZMFwqCTfvnx1z9dmCxxjrpqzSl6UYUWlajwwyex58cB7NPZ4lDS0RJrIVTSa1LttThK_HmhfcGo1_OUdOZE2xSQXSQBLFpJmGnVtdT6MrZkC9Rz2wB3E-ZOWxtaHNmxE_MRUO1kH5ogtZJS1HYgjhOUoMeWizsN9cJF0D7XB8TDnMPn8e2Xn9UC95aaj6YZAUKol-OPeFR6K-rKXQkvyQMsDj9Vf90vSL1OFWYrs6O8qB9yLnzu2cIWdoOiN1HOo0-v3aEJ3oxWCtpKsJUkTlyWAF4SVkxYglEG_-6b_fyTT5OCr5iqP8loXEQvoy_9VZTcHN5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
گل اول پرسپولیس به استقلال خوزستان توسط محمد خدابنده‌لو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/138605" target="_blank">📅 21:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138604">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚫
خطا روی باکیچ و بیفوما نگرفت به هردو کارت زرد داد مادر به خطا
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/138604" target="_blank">📅 21:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138603">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❤️
👤
تعویض ها مهدی تارتار مقابل استقلال خوزستان
🔴
۱- همایی فرد: عملکرد قابل قبول
🔴
۲- بیفوما: یک پاس گل و عملکرد خوب در جریان بازی
🔴
۳- ارونوف: عملکرد خوب در جریان بازی
🔴
۴- شهرآبادی: یک گل و عملکرد در طول بازی قابل قبول
🔴
۵- باکیچ: اثر گذاری روی گل چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/138603" target="_blank">📅 21:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138602">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTyv38dwZdzRJwxl-0OqUeYgHDnRX5Y_0IP-IRhOe3uGK0mbwVkXSRW6ayvy49yhRz33lxGqJtxYz6nuIdge9A9gcbTpBs68jPfzD0973JgtzPoyi51ACZ_BDqi15cGbdH01vW1exawCM2QC4gDgULrwnSzMyClfcQKV0HB4_J5ou3cg2AJgcM6QV8oWMt453OaqE4WCHI6w-aUGunQCQL3QaSLztszmYj1Y1bck75l_nWxUOouHds42-7nCRQxV5mS9mszXW6fjHv0V6pqh0uEWzzPmwyNIcFL7QSP_nGaEAubi_ltcHcY3WtBJR8NLyhigaS1sWC8kvW1LxsNd4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
علی علیپور، مجید عیدی و ایگور سرگیف با نمرات 8.8، 8.4 و 8.0 بهترین بازیکنان دیدار امشب دو تیم پرسپولیس
🆚
استقلال خوزستان بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/138602" target="_blank">📅 21:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138601">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⚡️
⚡️
شنیده میشه تیوی بیفوما در یک ماه اخیر برای ماندن در پرسپولیس زیر نظر پزشک تغذیه باشگاه 8 کیلو کاهش وزن داشته و علاوه بر اون زندگی حرفه ای شو سالم تر از قبل کرده و تمرکز اصلی شو روی فوتبال خودش گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/138601" target="_blank">📅 21:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138600">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0ArRvwo2X7QGmQE8LXgLxNeqv_4s4W7A1OFjn9gQdF6oBaI3N-xRrAX7ol9DxdRbrhAdCWZiWiCDTGFrrOeTxaRFD4vI-fX4k29PGOvjRCy9pdIrrj3VczRbCDdscWVsKeN30N8hIENNp9LeAJk7cxlkNOLOwZvUYw2Ezjzi-tZbONfi8S85WqeRUaQ5COdT_LK0wa0I21cqlBP9_3D2_KgD85WxfIh175JjiyqQ3HoFk9ijisPw6rhRTlKb-0ZboDdR7uO5ZnQh-kBtMhWdcjfdl4rslxC8XBSZ3cPY-PrqTPTK5xCtYpx7plpeajZCkOpav1Yz2Hy_pK-g2wUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
صعود به صدر جدول با چاشنی گلزنی تمام مهاجمان/پای علیپور، سرگیف و شهرآبادی هم به گلزنی باز شد
❌
پرسپولیس 4
❌
استقلال خوزستان 1
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/138600" target="_blank">📅 21:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138599">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
✅
مبارکه با چهار گل بردیم ..دو بازی شش گل زده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138599" target="_blank">📅 21:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138598">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚫
داور حروم زاده ریدم پس کله پدر جاکشت اکرم حروم زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/138598" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138597">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
گل چهارم هم زدیم توسط شهر آبادی 19 ساله و با زدن گل بالا رفتیم صدر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/138597" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138596">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚫
داور حروم زاده ریدم پس کله پدر جاکشت اکرم حروم زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/138596" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138595">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
پای جلالی خوب نشده بود و دوباره گرفت و تعویض شد و جاش همایی فرد جوون اومد داخل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/138595" target="_blank">📅 21:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138594">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
گل چهارم هم زدیم توسط شهر آبادی 19 ساله و با زدن گل بالا رفتیم صدر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/138594" target="_blank">📅 21:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138593">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
تشویق بی امانه تارتار در استادیوم ..همگی دارن از این تیم هجومی و جذاب لذت میبرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/138593" target="_blank">📅 21:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138592">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⚡️
گل سوم هم زدیم ...بلند شید و این تیم و ایستاده تشویق کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/138592" target="_blank">📅 20:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138591">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
همگی باید کلاه از روی سر برداریم و ایستاده این تیم و تشویق کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/138591" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138590">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
✅
نیمه دوم میتونیم شاهد ورود اورونوف و شهرآبادی و تیکدری به زمین باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/138590" target="_blank">📅 20:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138589">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_lgBu7cho_U6fihpQvU6zkJwH7AX0mWb27QEAmjZ0Vqknq1qX-cWjfBe1r7knCRHVskoediJXtW4xwV9gnrvujCStcgCpqDKU4tqJYX-JqEjkNu9MkUvVQVVuusJgkOunJsy63AFEsjQTZojWyQQ6MmuX25F4ecwdm2TpYxMJPJNpEqZNLqLFvxsjKZn9IGHFJElKPzpdrknYLJK8pmvPks2H4eEv6QUNhf8nBPKMDfH8IB8qiCjkt37V4rVRFXWMUOeQFNYHfr1qNu1XoFGxhHjRsKYbGDrBUWdK7DwBnlgETttTpY6JXDGdeizCkCrSFvilA7QQeU9dBElKP5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
️ بونوس اختصاصی چرخش رایگان بازی Scarap Temple
💰
کاربران اسپورت نود می‌توانند از همین حالا، با هر بار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود ‌اسپین رایگان کازینو دریافت کنند.
💸
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/138589" target="_blank">📅 20:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138588">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
مثل نیمه اول با اختلاف زارع بهترین بازیکن زمین بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/138588" target="_blank">📅 20:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138587">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
نیمه اول و با دو گل پیروز شدیم ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/138587" target="_blank">📅 20:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138586">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
گل دوم هم علیپور زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/138586" target="_blank">📅 20:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138585">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
⚽️
بااعلام‌باشگاه پرسپولیس؛ مصدومیت ابوالفضل جلالی جدی نیست و این بازیکن مشکلی برای دیدار هفته آینده مقابل استقلال خوزستان ندارد. جلالی امروز بازی  درخشانی در ترکیب سرخ‌ها داشت.  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/138585" target="_blank">📅 20:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138584">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
باید برای این پرسپولیس تارتار ..تیم جذاب و هجومی با احترام حرف بزنیم ..چه تیمی درست کرده تارتار.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/138584" target="_blank">📅 19:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138583">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
✅
گل اول و خیلی زود توسط خدابنده لو زدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/138583" target="_blank">📅 19:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138582">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
با اختلاف سه گل ببریم میریم صدر جدول..الهی به امید تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/138582" target="_blank">📅 19:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138581">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚡️
⚡️
جمعیت خوبی هم رفته دم هوادار گرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/138581" target="_blank">📅 19:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138580">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
با اختلاف سه گل ببریم میریم صدر جدول..الهی به امید تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/138580" target="_blank">📅 19:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138579">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
🔴
📸
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/138579" target="_blank">📅 19:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138578">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
🔴
📸
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/138578" target="_blank">📅 18:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138577">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
نسبت به بازی اول فقط جای سرگیف و بیفوما تغییر کرده و همچنان اورونوف روی نیمکت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/138577" target="_blank">📅 18:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138576">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
🔴
📸
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/138576" target="_blank">📅 18:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138575">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5SkboM3RZN9xZSRAjKjx432V666TWfdLmoSPML7BCYHi0Qq_37PkyiPKe10-K6e7y6Vj2jKqpdDZtRqnk7lrxX35Y6aqNuABY2_9MjxiPkUVhtqSUhKizJ1Cb4eD6F7OVoq_1sudvbRlIbYfDW2A5P6M6Y72957wauMUgJRzzocbDtiBnJrBaacN238U87GjBeO9CpghYyfBpGNNv9s8R9oMMD3aJqjsg4MNCwBvioLB6t32puTdLmruhqAKWTJB1sFW31bxoAuht4qL3ceY9Jwfhj1NvPHzoBVKCE6YrhhjEPHq632w-_qBiIdR1QKyrmMLMw0LaBSpzbiinErCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس برابر شمس‌آذر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/138575" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138574">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d137678386.mp4?token=RZqlqT4FPAmSdEcflafwbaVql0FKZOcjrBHgcfTUIi5-70YkLxTcnUiiYpM551KWb83WQry0ynpjNRV7fhTxHVN1axWSLSPqlNYbh8Vnz8lwCEq1hCXm0wUZzYMCDSfXJ-WI3Dd0SPVbajPDPJPj1SViD1IyjvxaGDlRhQELfZej2V9QoWS8GqIvhzP6QDBeTC8i3lvwzxfp5yxKHWbU5RpW41gMSbD9UtTRR3nWOEzo7zgqOIk9bq6_XtBpc7pNEUvu5aO4U-0_4-gKRnNBJdh6h16P9BF9vwEhYjs4EGfyYU8PCQeni1BEDiOsuUac-pfyqzARDtBD5-96REQHTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d137678386.mp4?token=RZqlqT4FPAmSdEcflafwbaVql0FKZOcjrBHgcfTUIi5-70YkLxTcnUiiYpM551KWb83WQry0ynpjNRV7fhTxHVN1axWSLSPqlNYbh8Vnz8lwCEq1hCXm0wUZzYMCDSfXJ-WI3Dd0SPVbajPDPJPj1SViD1IyjvxaGDlRhQELfZej2V9QoWS8GqIvhzP6QDBeTC8i3lvwzxfp5yxKHWbU5RpW41gMSbD9UtTRR3nWOEzo7zgqOIk9bq6_XtBpc7pNEUvu5aO4U-0_4-gKRnNBJdh6h16P9BF9vwEhYjs4EGfyYU8PCQeni1BEDiOsuUac-pfyqzARDtBD5-96REQHTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
‼️
هوادار پرسپولیس: تیمی که ۷ گل خورده و دسته سه رفته، به ما نمی‌خوره! فینال آسیا واقعی رو ما دیدیم. استقلال بره آسیا ۷ تا بخوره، خوشحال میشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/138574" target="_blank">📅 18:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138573">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff8f1d1ef5.mp4?token=M0QMToN37a0nt1TxLTDV-YJgJZzolj8aWbuvf-sFmVTx3S45PFUDIw-Sncw0ol6oDkae0DtagJDswQNeVB_dOEEOnpEVq23cKmBNrTWoNz-oG-P8CprpZVbvJ4y4ZQfv9V2Q_nCIq3juRonKPnOz5XxlwBFMppxfR7f_l78kJTFfJJdVWfnPKFyZKcK__ciUHPz4NHrG6Rz3Au0hdakuN9XLjl_ssNTk-JVkd6e5h8p5w0aiCN3wValtXMQmesqN7crxCwkS56N1zfbTi4RUvkM8sBqpq5WhNecq3DGwucVVRByiKJro6239XtqAtajM67s7OC36L1aKOS6-PVH2Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff8f1d1ef5.mp4?token=M0QMToN37a0nt1TxLTDV-YJgJZzolj8aWbuvf-sFmVTx3S45PFUDIw-Sncw0ol6oDkae0DtagJDswQNeVB_dOEEOnpEVq23cKmBNrTWoNz-oG-P8CprpZVbvJ4y4ZQfv9V2Q_nCIq3juRonKPnOz5XxlwBFMppxfR7f_l78kJTFfJJdVWfnPKFyZKcK__ciUHPz4NHrG6Rz3Au0hdakuN9XLjl_ssNTk-JVkd6e5h8p5w0aiCN3wValtXMQmesqN7crxCwkS56N1zfbTi4RUvkM8sBqpq5WhNecq3DGwucVVRByiKJro6239XtqAtajM67s7OC36L1aKOS6-PVH2Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
🔴
هوادار پرسپولیس: از رنگ آبی و استقلال نفرت دارم! تارتار تیم خوبی ساخته و پرسپولیس همیشه قهرمانه. استقلال تیم نیست، عروس آسیا هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/138573" target="_blank">📅 18:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138572">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a524ae095.mp4?token=PO7r9zb__K03ULbQRWLmEozbOV5KxwQvAzJHQKaaVopZ7UOw5IdUYDxqy2ZDyJWzJrPtGw9T26eaYCz88P5DiXb1BQdUkLBddrh6yCEJ-O-ei0k9jkCX19EgDm45qu1JIwFhi2RxXhsyrgIUPFn_g1jOn3aJI0fIULJJuI2JOVQE23u4YOQEUBe4wslbrJ4c7KecyySv9cw7UUuXuvK01KfRJLkDDLC4hBykQ6JbkugRH-AUX6KTVCJ9H2Q4OeEisLNBJvSDVSiQFyYxu4SdhreHeincx3xJ2gLLXg45C34R40cZCkUgvIS9p_8OMy7oEbyePbybeYuwTRTSkVXcBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a524ae095.mp4?token=PO7r9zb__K03ULbQRWLmEozbOV5KxwQvAzJHQKaaVopZ7UOw5IdUYDxqy2ZDyJWzJrPtGw9T26eaYCz88P5DiXb1BQdUkLBddrh6yCEJ-O-ei0k9jkCX19EgDm45qu1JIwFhi2RxXhsyrgIUPFn_g1jOn3aJI0fIULJJuI2JOVQE23u4YOQEUBe4wslbrJ4c7KecyySv9cw7UUuXuvK01KfRJLkDDLC4hBykQ6JbkugRH-AUX6KTVCJ9H2Q4OeEisLNBJvSDVSiQFyYxu4SdhreHeincx3xJ2gLLXg45C34R40cZCkUgvIS9p_8OMy7oEbyePbybeYuwTRTSkVXcBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏅
وضعیت ورزشگاه شهرقدس در فاصله یک ساعت و نیم تا شروع بازی پرسپولیس.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/138572" target="_blank">📅 18:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a1e95c93.mp4?token=tOTlMSDd_HE6BzREFE0LvJ0PlxtX5mN5PpvPr8isrO8Ydin8NArE0c8V_DRzbQxRJ8uRa4qC9OsACLNBfP1hvclCKNMU4_BB68JyDJaTmmUXoTlWoow2xxblrccgnfEZpxAQ542W_WgzbhgvEQh1OYS1M5LyEccv2tqF2F0KNJ0pc6x5o11xkiXBDe3KXb4cGq01MkpOvnmzGy1X-PXu-_M5haIejCNX2LdCjNt3aKzZnHKgId75jVd5q-ew_q6vWVQH8ZW1Z2kSGTXaNA4axnUVPXHiD-V5ZmyUcCweuJFmn-mCqTbNyKj7YgVjAVWnfDNmML-qSSmGtwOi0BTSNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a1e95c93.mp4?token=tOTlMSDd_HE6BzREFE0LvJ0PlxtX5mN5PpvPr8isrO8Ydin8NArE0c8V_DRzbQxRJ8uRa4qC9OsACLNBfP1hvclCKNMU4_BB68JyDJaTmmUXoTlWoow2xxblrccgnfEZpxAQ542W_WgzbhgvEQh1OYS1M5LyEccv2tqF2F0KNJ0pc6x5o11xkiXBDe3KXb4cGq01MkpOvnmzGy1X-PXu-_M5haIejCNX2LdCjNt3aKzZnHKgId75jVd5q-ew_q6vWVQH8ZW1Z2kSGTXaNA4axnUVPXHiD-V5ZmyUcCweuJFmn-mCqTbNyKj7YgVjAVWnfDNmML-qSSmGtwOi0BTSNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ورود اتوبوس تیم به ورزشگاه برای مصاف با استقلال خوزستان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/138571" target="_blank">📅 18:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138570">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚡️
مدیر برنامه آسانی: نامه فسخ دستکاری شده است
🔹
مدیر برنامه یاسر آسانی، هافبک استقلال، انتشار نامه فسخ قرارداد این بازیکن را تکذیب کرد و مدعی شد نامه منتشرشده با هوش مصنوعی دستکاری شده است.
🔹
رسانه‌های مختلف امروز نامه‌ای منتسب به فسخ قرارداد یاسر آسانی با…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/138570" target="_blank">📅 16:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138569">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
دانیال ایری در لیست پرسپولیس برای دیدار با استقلال خوزستان قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/138569" target="_blank">📅 16:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138568">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
شوک بزرگ به طویله کیسه/ نامه مشاور حقوقی یاسر آسانی که اعلام کرده قرارداد رسما فسخ شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/138568" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138567">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gh8fRqQqG4Zx-5HAWUNF2h8N70bQ773WQvXFJzC36ttvReDQqt5qZUOB2ALDFEPr7_eE9uLKPQopltnRp9M_GHtKpGM1z3GA1rPX-kK4T7FD92QF-vG-pG5KV9qAM11PrwewuPUG9jdiSzd1gwmmEHZtpX-iX6oxCFSmmb5B0Ln_QlqlYCqdlQMhoYxCA0ecePPryamF9v-eXVO7ZSQiO8Oa1YJV3am50-kCTUrxNMaoO6ZFAGNhbD7_DGO_O78wSZLI70pV-FG_WHKBsdKik7vUJM07SXP2x8vYtoXDHFVZEtyJno1w_nTCchW6N5zHI4ASv1Sr1LDdhShEdI6Lug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسمی؛ با اعلام سازمان لیگ دربی پایتخت برای اولین‌بار قرار است در اصفهان و ورزشگاه نقش جهان برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/138567" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138566">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1Xt_d1hIS0PqqZvQP1yZmYLs0zFL9cIIMoXM2Uh81DwsPSFZ-StMhVmX1x9zLFwKieE1EZp_FgQtA5TzaJzyW9ccc0NgLVZNH18DpamRoTORCOpZ7cU2HrBFa58_3bC-DiiRUuLw17Nyjn-K3nVkTNuxqD7K7Gl0Ieh79YJBcZDO9WeqKunftB9iMt2m0LUsIlTLZ3aGCqH4nQCGVNxZGFnA1QRJxWL--YNeCS6RsUe3qRJEbTAmbRUezAlQYMnYNSuUu0ANhMBkEVD-ICN2apTTwlLklSxDHkylHmZN1Dl8qOP6SX8TSR14yvZQK2EOkkUSffH2xythc14VWz5uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
استوری وحیدقلیچ: رییس فدراسیون فوتبال روسیه دنبال منه
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/138566" target="_blank">📅 16:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138565">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
نتایج ۵ بازی رودررو اخیر پرسپولیس و استقلال خوزستان:
🇮🇷
پرسپولیس ۳-۰ استقلال.خ
🫱🏻‍🫲🏻
پرسپولیس ۰-۰ استقلال.خ
🇮🇷
استقلال.خ ۱-۰ پرسپولیس
🇮🇷
پرسپولیس ۴-۳ استقلال.خ
🫱🏻‍🫲🏻
استقلال.خ ۲-۲ پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/138565" target="_blank">📅 16:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138564">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e06320f5f.mp4?token=gl0UF5OerE0_YFxoYDebJuFr2sqXbWQ3BpgnuUr0wvLHoY45b76kPzMokWID1TfWPdGLRxZWAj84WPAnI5VWQEAXGGabsB0GEXf3rdfPQ-UkbCi8bA2cHLCvs3B0Dh8cW0CU66TUPAKm7oZlSUkKjhHVJkC-jRJSR1ea7NsW7Ejd9ioKw7KMH7JYymCyAWiHJ4p4ewOS2WFNTzwEGrtXransNVuOXHIrZkjRkjxVux4QQlulzZi_6ID2Y4B1Vzywd3phoG-yEk3HztbJxddp4H3eyDBDP83Ya5z4bTOiQxYqGQHvjJif5OEcOXirIl7poqAx1TUvEsZMi8Z048RtNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e06320f5f.mp4?token=gl0UF5OerE0_YFxoYDebJuFr2sqXbWQ3BpgnuUr0wvLHoY45b76kPzMokWID1TfWPdGLRxZWAj84WPAnI5VWQEAXGGabsB0GEXf3rdfPQ-UkbCi8bA2cHLCvs3B0Dh8cW0CU66TUPAKm7oZlSUkKjhHVJkC-jRJSR1ea7NsW7Ejd9ioKw7KMH7JYymCyAWiHJ4p4ewOS2WFNTzwEGrtXransNVuOXHIrZkjRkjxVux4QQlulzZi_6ID2Y4B1Vzywd3phoG-yEk3HztbJxddp4H3eyDBDP83Ya5z4bTOiQxYqGQHvjJif5OEcOXirIl7poqAx1TUvEsZMi8Z048RtNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏟
ثابت قدم مدیرعامل شرکت توسعه و تجهیز:
ورزشگاه آزادی اویل آذرماه آماده می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/138564" target="_blank">📅 16:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138563">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2698fac3f.mp4?token=bNUIiMQ7cIBrbemoZYJ8J2FOve7nOa5JE9VFj9PiIPIABq32BMftdsghaAzcl6mbSJWAgwZtclUr1KROjA3a38d9JXPl3VX6jSHJGB1LNoL1LxlRQ9n7jOqJ5sK1xhwSVaz2i0iTA24ag75xFyApP92IwA5UNS0a0QCHtGEJRXRhBVIeQ5KgFdITcmE_T-YKNRY9Ut3UB5Bnw69HU7dTCLXx_8-OwViu1oyWUCx6AqAUQpkRResJMLvcXlDB0BGGLAXnl2oSphZBpMbn5fKXAZN4d1tZ2QIlZxj-rLtvbgQ-R9LXpclhm5DXC8l0iOaX7Lx3mlRYkFulgrotcfnjYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2698fac3f.mp4?token=bNUIiMQ7cIBrbemoZYJ8J2FOve7nOa5JE9VFj9PiIPIABq32BMftdsghaAzcl6mbSJWAgwZtclUr1KROjA3a38d9JXPl3VX6jSHJGB1LNoL1LxlRQ9n7jOqJ5sK1xhwSVaz2i0iTA24ag75xFyApP92IwA5UNS0a0QCHtGEJRXRhBVIeQ5KgFdITcmE_T-YKNRY9Ut3UB5Bnw69HU7dTCLXx_8-OwViu1oyWUCx6AqAUQpkRResJMLvcXlDB0BGGLAXnl2oSphZBpMbn5fKXAZN4d1tZ2QIlZxj-rLtvbgQ-R9LXpclhm5DXC8l0iOaX7Lx3mlRYkFulgrotcfnjYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⛔️
آقای کمیته انضباطی اگر یکبار به صورت قاطع برخورد کرده بودید و درگیر رانت و فساد تلفن بازی نمیشدید،الان کشالش رو میکرد تو
کون
ناموسش به مردم توهین نمیکرد مسبب این بی قانونی و فساد اخلاقی رفتاری شما حضرات هستید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138563" target="_blank">📅 16:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138562">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
✅
✅
کمیته انضباطی قصد دارد به صورت ویژه شادی گل جنجالی شب گذشته شجاع خلیل زاده را مورد بررسی قرار دهد و با توجه به سابقه او در انجام شادی های جنجالی، احتمال محرومیتش وجود دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138562" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138561">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
❌
کشوری فرد دبیر سازمان لیگ برای بازدید از ورزشگاه نقش‌جهان در این ورزشگاه حضور یافت. بر این اساس، احتمال دارد دربی استقلال و پرسپولیس در هفته پنجم، روز 11 شهریور در نقش‌جهان اصفهان برگزار شود.
✔️
✔️
گزارشگر دیدار روز گذشته سپاهان و تراکتور نیز در جریان مسابقه…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138561" target="_blank">📅 14:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138560">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byAW3CJWweLTRhGawcWhaGQ2P9GB1wk4SPaDzJ2sPagsKCOlKn1nTFLaAaQY3sq71Ki8rQ_6h8r1veiJm2dpFlYGePjXqLPBm3ksY6xaDt-4KB_yl97LHU3lLTQh5JLXttSm1-VwkHGWGe9PkxyCTimojNcGBWmRfpbMe9mzlRvLHT1bf2vc-G09fe08skk9fbNboE_WQiHyFzLb7QbWx93LFwjs3I8TLX-uLdnikPBfnGeXVXF6cXvISNK38cQcJawiWABKBcfLigp0VAGfhaFYfH06X5HIE7BZc2ztM9dhovb6uT30i5cCumm0hgO7xs4nM0ctGAfEV08Jh7OOPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽
نبرد سرخ‌ها با آبی‌های خوزستان؛
پرسپولیس برای شروعی قدرتمند، استقلال خوزستان به‌دنبال غافلگیری!
⚽️
لیگ خلیج‌فارس ایران
[
پرسپولیس
⚽
🆚
🇮🇷
استقلال‌خوزستان
]
⏰
چهارشنبه ساعت ۱۹:۳۰
🏟
استادیوم شهرقدس
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/138560" target="_blank">📅 13:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138559">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
با درخواست کیسه به عنوان میزبان دربی ، دربی رفت به احتمال خیلی زیاد اصفهان و ورزشگاه نقش جهان باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/138559" target="_blank">📅 12:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138558">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
فوری؛ باشگاه نساجی مازندران از باشگاه استقلال تهران شکایت کرد
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/138558" target="_blank">📅 12:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138557">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
محمد گندمی، یعقوب براجعه، دنیل گرا، امیرحسین طاهری، علیرضا عنایت زاده و کوروش اژدهاکش از لیست پرسپولیس برای بازی فردا خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138557" target="_blank">📅 12:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138556">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
⚽
باز هم حرکت عجیب و منشوری شجاع خلیل‌زاده، بعد از خوشحالیِ گل!!!
❌
پ.ن و بازم کشاله ران بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138556" target="_blank">📅 12:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138555">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
آسانی بازم فیکسه!
❌
مدیران نساجی ام گفته بودن مستندات جدیدی دارن، چه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/138555" target="_blank">📅 12:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138554">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
قدوسی: پرسپولیس و تراکتور میدونن که الوحده قربانی رو نمیده ولی از ترس اینکه اون یکی جذبش کنه پا پس نمیکشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/138554" target="_blank">📅 10:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138553">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
فوری: بازی تراکتور و پرسپولیس در هفته سوم بدون تماشاگر برگزار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/138553" target="_blank">📅 10:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138552">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
⚽️
🧡
رامین رضاییان میان تشویق شدید هواداران فولاد با شعار « رامین، رامین، رامین ما دوست داریم » وارد خوزستان شد؛ فقط کلاه رامین رو ببینید
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138552" target="_blank">📅 10:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138551">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
مهدی تارتار قصد دارد از سیستم چرخشی در هفته های ابتدایی استفاده کند تا ضمن آمادگی تمامی بازیکنان فشار کمتری به تیم وارد شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/138551" target="_blank">📅 10:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138550">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
جنجالی‌ترین بازی هفته سوم بدون تماشاگر
‼️
✔️
✔️
تراکتور و پرسپولیس هفته آینده باید در دیداری حساس پشت درهای بسته به مصاف هم بروند. تراکتوری‌ها حالا به دنبال تعلیق محرومیت هواداران هستند تا سکوهای تیم‌شان را پس بگیرند؛ تصمیمی که می‌تواند روی بازی برگشت در…</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/138550" target="_blank">📅 10:23 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
