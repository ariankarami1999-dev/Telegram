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
<img src="https://cdn4.telesco.pe/file/iTP5dEGbN-JKPgO1U0Og-VqIdnEQwGx1lHjREcYd_j76Fn0z0BlKPAdTNEHVPv400Vq5kzpnwPXCPhoUrm8hmleYnm-JBRtj0OCbyQyhiLWmNBfqjfcOv1X5ZrL3C6pQWBle0TCdky2SWoFEVmh1qjwIFlb2HJsU8jwhDn80ZJ9a5Z7aeN_CSKPnw29BwiUM9W6H71td3auhpMZZb0prWgDatshhwRisBFVdYX5WN0UleM2xynIP6lZJsFEPjTpF2ZEGfY0Hst-gWOeGxqaBUuWO4F1pB7kV1KSKPiBBqn7MGiVfW7yoTTMUrR6j7dBLJ935PxL0TDrJCmRM7Gm5aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 970K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 16:26:06</div>
<hr>

<div class="tg-post" id="msg-125762">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
منابع لبنانی گزارش دادند تعداد کشته و زخمی شدگان حمله هوایی اسرائیل بالاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/125762" target="_blank">📅 16:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125761">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
در لبنان گزارش می‌شود که شهروندان اکنون در حال تخلیه بیروت هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/alonews/125761" target="_blank">📅 16:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125760">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل به نقل از یک منبع نظامی: پس از راهنمایی‌های اطلاعاتی، نیروی هوایی به یک هدف با ارزش بالا در حومه جنوبی حمله کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/alonews/125760" target="_blank">📅 16:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125759">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
کانال ۱۲ سرائیل : اسرائیل قبل از حملِه به بیروت، به آمریکا گفته بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/alonews/125759" target="_blank">📅 16:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125758">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
محل مورد هدف قرار گرفته در حومه جنوبی شهر است.
🔴
گویا ترور هدفمندی صورت گرفته
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/125758" target="_blank">📅 16:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125757">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی : یه حمله محدود تو ضاحیه انجام شده و ارتش اسرائیل هم فکر می‌کنه ایران مستقیم به اسرائیل جواب نمیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/125757" target="_blank">📅 16:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125756">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1015bb3474.mp4?token=r6UG8fgjs_3NeHFeUtldHvGEbF-7STAZG_L5om05cgAq7SFcjOjr5VH9N8-PE_dXkjFzR8XpFtNwZkTfHgB5e0MT852LuuzceA41caQF2GP-taZOi_YjgY0bdS0CoIImmahMK45duv8yf-QNQNzxhgteI6r-4jY4Nm1k-90QzryaNG5FeIH5FwH6Ya847cpsD6Y8vVinhbqJkxUorudURCyU7_Rm_ZJX20BdGmPsYCYC3SZKmU_rAwjDGAKBrDBLxy89xl4HO0_yYdiwvSysfg73ZKqC0Z5WVaYtanknGbHPtZcF2m4zRCc0k8h134xAM6eE90CHskxnUw4VO1R35Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1015bb3474.mp4?token=r6UG8fgjs_3NeHFeUtldHvGEbF-7STAZG_L5om05cgAq7SFcjOjr5VH9N8-PE_dXkjFzR8XpFtNwZkTfHgB5e0MT852LuuzceA41caQF2GP-taZOi_YjgY0bdS0CoIImmahMK45duv8yf-QNQNzxhgteI6r-4jY4Nm1k-90QzryaNG5FeIH5FwH6Ya847cpsD6Y8vVinhbqJkxUorudURCyU7_Rm_ZJX20BdGmPsYCYC3SZKmU_rAwjDGAKBrDBLxy89xl4HO0_yYdiwvSysfg73ZKqC0Z5WVaYtanknGbHPtZcF2m4zRCc0k8h134xAM6eE90CHskxnUw4VO1R35Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: ایران بعد از ۹ اسفند هیچ درخواستی برای مذاکره نداشته؛ همه اینها یک طرفه و از طرف آمریکا بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/125756" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125755">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyKzyH2pZgkHPrqNmf0jZq3OWKc43R3W2vQPedbvYgZEmmbi37thsKb5nRrH6cNABYu9fqfowMCJeMwAXFZZPKMJz8byCyZgPaWZebqzznrqdl6Mep694q5qOLhhd_3e9ePr3Q4KWq6DubXhXrsNJoqK6TCgcwiiruSArRZiUaQkc1UWvZ702e_OTTr7VDvkRM1Rxz7zl27SXdX7J1a4p7Y6ufKOx-uO2IH80FHwz4Jg5HUiE1rZ5IASH_ib3yg7aeelyh49ouutp29usKoXH7Xv47genQuIf1-nWaVrULMoW0wdcUyzKDDNFMQnxYA1IKk9nIadNuXzQmhlgcHO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محل مورد هدف قرار گرفته در حومه جنوبی شهر است.
🔴
گویا ترور هدفمندی صورت گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/125755" target="_blank">📅 15:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125754">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3XuO6QisNYtCd-j_0A45xRJ5umkHUNh75Gq9C9nLtA8pPaat3klb3bfYUxoEVC-cR0OuxB_UM36kALO9VU7DPKat1C0pyuWSXokSMg6P0qVVHSQ9mBFdwG3zJnzKHhgazRXGTxNwc_9M86iKKcq-OYaZphQEdc0t-D_CKkndpS5Dg-EFjzPE1YbBb0k4lDJ-Le-kHUuWlBJBFh5-Tjcd21fgy7abzjlDy5H5RFZl8caLCSE6U_2vprLGTYbAEoTdwpo5rxxMojP-IeALj9XtIHszKWrL5Vtepno-ilNFZw6x_SQ8XB4aBAjfk-18pnHvJdzarQCNlMBTpeJFQ56rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه: پاکستان به دنبال جداسازی پرونده لبنان از توافق ایران و آمریکا
🔴
عبدالله خلوف، خبرنگار العربیه: پیام فرمانده ارتش پاکستان به رهبری ایران، تلاشی برای رسیدن به مرکز تصمیم‌گیری ایران است. اسلام‌آباد تلاش می‌کند «پرونده لبنان» را از توافق احتمالی میان واشنگتن و تهران جدا کند و آمادگی خود را برای کمک به ارتش لبنان در اعمال کنترل بر جنوب این کشور، پس از خروج عناصر حزب‌الله، اعلام کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/125754" target="_blank">📅 15:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125753">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
عراقچی گفته بود اگه به ضاحیه حمله بشه، تهران با قدرت پاسخ می‌ده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/125753" target="_blank">📅 15:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125752">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نخست وزیر و وزیر دفاع اسرائیل در بیانیه مشترک از انجام حملات هوایی به مراکز فرماندهی و زیرساخت حزب الله در ضاحیه در پاسخ به حملات راکتی امروز صبح حزب الله خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/125752" target="_blank">📅 15:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125749">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dnp4BpexB5havb4Aqx7U1HMUs93PJvhgcVA6Smg7zEaVr6vQ8smgc5yZiVd65HWOS9-pLIWc-Vmhwn9ALUJDh1wUcugo8ISy4lp5eJrA1pLvCv7Wpl2dATS4IC5EGhgNcqAjOt1Ic56sg6DX2a8rd2XlLCp01sHxs37q6Z2lHkfQ-CBn9jjLCy6ukh-Vgkcdg0NrtydI8KgiExt7KiTilEmtYoFPlQpb_He2ei9-LCc9sKX5XfDzen0FgdFvmQMUvVPRf1m9KPL_PcTD-mbJyZgkfzDG8u6afu3Fwd8Lb9FOTrqvhku3w5Us0_LsCS5Y6-37NSt15m69buoRm936pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88104063b9.mp4?token=Z19UtgFuSmKCWTPV4wCnuUyr88CUsl6eb4jocoG2MDb0dPgq84ED8jPQC7yoWOwGsK3GUvj6R0A6gWfT90MIJJ1OBREy2lPsmmkzahjWxWMlV9s44WdAHcXZvN76pa6PkyJ9S7QQAMVhFt4IwxIVQIf7a7-hrsEmJNUFJPnwaQqSIR-mOnhvvPhuMrwdx9JiyU7MEEIs3FnEsPThX57wlxvNpaKaMhmxlmjD6MKLE3emVcp_17KjFaVGLBkGMHebdRrbEpUgySWIV5eluaKyBU4zN8tHAz2Xw16CHq-CKcKBgOgFTRlcBoq_yBWfhvljHpItuJDm49u5cJaHc_Wwkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88104063b9.mp4?token=Z19UtgFuSmKCWTPV4wCnuUyr88CUsl6eb4jocoG2MDb0dPgq84ED8jPQC7yoWOwGsK3GUvj6R0A6gWfT90MIJJ1OBREy2lPsmmkzahjWxWMlV9s44WdAHcXZvN76pa6PkyJ9S7QQAMVhFt4IwxIVQIf7a7-hrsEmJNUFJPnwaQqSIR-mOnhvvPhuMrwdx9JiyU7MEEIs3FnEsPThX57wlxvNpaKaMhmxlmjD6MKLE3emVcp_17KjFaVGLBkGMHebdRrbEpUgySWIV5eluaKyBU4zN8tHAz2Xw16CHq-CKcKBgOgFTRlcBoq_yBWfhvljHpItuJDm49u5cJaHc_Wwkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / حمله اسرائیل به ساختمانی در ضاحیه بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/125749" target="_blank">📅 15:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125748">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سه زمین‌لرزه با فاصله تنها چند دقیقه‌ای از یک‌دیگر، امروز جزیره «اویا» (Evia) در یونان را لرزاند که قوی‌ترین آنها با بزرگی ۵.۲ ریشتر ثبت شده است. این زمین‌لرزه‌ها در مناطق مختلف از جمله ناحیه «آتیکا» و پایتخت یونان، آتن، نیز احساس شد.
🔴
به گزارش روزنامه «نشنال هرالد»، مقامات یونانی اعلام کردند تاکنون گزارشی از تلفات جانی یا مصدومیت ناشی از این زمین‌لرزه‌ها دریافت نشده است. با این حال، در برخی نقاط خسارات جزئی گزارش شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/125748" target="_blank">📅 15:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125747">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فارس به نقل از یک منبع: بخشی از پرداخت‌ها برای عبور از تنگه هرمز، نقدی نیست و در قالب تتر، کالا یا تهاتر انجام می‌شود؛ یعنی برخی کشتی‌ها خدمات ارائه می‌کنند و ارزش آن از مبلغ قابل پرداخت کسر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/125747" target="_blank">📅 15:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125746">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
دبیر شورای صنفی نمایش: از نظر شورای صنفی نمایش پخش بازی‌های تیم ملی فوتبال ایران - که فعلاً در مرحله گروهی شامل سه بازی می‌شود - در سینماها با کسب مجوزهای لازم از ارگان‌های ذیرربط بلامانع است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/125746" target="_blank">📅 15:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125745">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نتانیاهو: ما اجازه نخواهیم داد حماس دوباره مسلح شود یا به ما آسیب برساند، و ما به حذف رهبران برجسته آنها ادامه خواهیم داد.
🔴
ما حلقه محاصره را به دور حماس در غزه تنگ‌تر می‌کنیم و در حال حاضر ۵۰ درصد از مساحت نوار غزه را در کنترل داریم و به زودی به ۷۰ درصد خواهیم رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125745" target="_blank">📅 15:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125744">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFmLm0wQnePUD57A364KGV2xYiA6sL13Sce5Wy7RY43nNEzmPeO9tSjenau84yVEHLLrFP4Pojq3L5gB1QZaGVP9UX0enIOssIG-tr7DgKcDtrGCgmbLY9yoFYj99c-O-QiTANpAqXmCrCZXL5gH1Mm3unu-7HJL6-uqYtJeyRE5SlDO_Ljg7rO6tcoti0zlQLaIDP6nz7Jvw9iM9jvCEB04CLrM6ZvGz0OKW5sCeXJGd1F6bz_u1i3meKLwXMTm-9aTiduDFIhu9-p2SaGA-dAyxQan7jID3kH41qbPuE_4cMllt_43nqlegKgemHybDx1fuoZAS9X0v5cqYE11Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشیدی کوچی: خطر فرقه پایداری به‌مراتب جدی‌تر از تهدیدات خارجی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125744" target="_blank">📅 15:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125743">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f40787a7c.mp4?token=efZ99UwQuR2_5bjrMQadfuP60riyzdPP4zvpGCzqH-EDVPahJlrbno_-Jzi6IUne7ixUuDt4lNxI-0SbrswQNPSJDEzPQCvWudPkq8HmcsEe-HtPbpiw_BwyjkpWE7oGdBOZK1ZfGKv30rMdl0zuqSPflvSO70yQG0QhPa9lAHk0lQMOZo7qoBmLmqazybQkOy9s_qihOXDcfCvrr7Bv1x9eWkU9NrgSqudHmlLNZQe2hcjD6RraVqsxhHs6Zk0vOW8Ar469mkz1uxH-aH6qAzXJBhAnKOvU_OgkZm0rYnAiCq_NkisdMziPUxwqKHpjIO-DtSLHJnZLLPw04t-3_ZibVGV5rQkaTxZ1_OfK-0g_8nqLjDYwGCpsWXLlndtxUNxRtNjPF0Dy6H0oxIgktERjdv6Rr1n5W6iofnmIAuOV-ri1bDtw8F6eo7hYjk-S8_NF6KzxLYd3gYfbT6obE3yAk6BXsaLhaso8eIrtxPkoPQRvH6wM8IHXRrRR2xkFMevg9u11cSpHtPZovU2N4Rs56OmeyIqea-jnEokCl0Y3GzxLiwrXM9eGxX4YuTftJR2xaHsasYeUKmkk0166RnayKrmojTnIINkasSZ9VupYrmdJ52thf3ZBTCFWMt_fY-XCwSQ-66qCHAR8fGElCbxYU1xMzglfEhxqmgkzxN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f40787a7c.mp4?token=efZ99UwQuR2_5bjrMQadfuP60riyzdPP4zvpGCzqH-EDVPahJlrbno_-Jzi6IUne7ixUuDt4lNxI-0SbrswQNPSJDEzPQCvWudPkq8HmcsEe-HtPbpiw_BwyjkpWE7oGdBOZK1ZfGKv30rMdl0zuqSPflvSO70yQG0QhPa9lAHk0lQMOZo7qoBmLmqazybQkOy9s_qihOXDcfCvrr7Bv1x9eWkU9NrgSqudHmlLNZQe2hcjD6RraVqsxhHs6Zk0vOW8Ar469mkz1uxH-aH6qAzXJBhAnKOvU_OgkZm0rYnAiCq_NkisdMziPUxwqKHpjIO-DtSLHJnZLLPw04t-3_ZibVGV5rQkaTxZ1_OfK-0g_8nqLjDYwGCpsWXLlndtxUNxRtNjPF0Dy6H0oxIgktERjdv6Rr1n5W6iofnmIAuOV-ri1bDtw8F6eo7hYjk-S8_NF6KzxLYd3gYfbT6obE3yAk6BXsaLhaso8eIrtxPkoPQRvH6wM8IHXRrRR2xkFMevg9u11cSpHtPZovU2N4Rs56OmeyIqea-jnEokCl0Y3GzxLiwrXM9eGxX4YuTftJR2xaHsasYeUKmkk0166RnayKrmojTnIINkasSZ9VupYrmdJ52thf3ZBTCFWMt_fY-XCwSQ-66qCHAR8fGElCbxYU1xMzglfEhxqmgkzxN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله پهپادهای انتحاری رو به سمت نیروها و خودروهای اسرائیلی تو جنوب لبنان شلیک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125743" target="_blank">📅 15:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125742">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرگزاری رویترز نوشت: اعضای اوپک پلاس در نشست امروز (یکشنبه) خود احتمالاً برای چهارمین بار در چند ماه، بر افزایش سهمیه تولید نفت توافق می‌کنند.
🔴
این بحران با خروج امارات از این سازمان صادرکننده نفت پس از ۶۰ سال عضویت در این ائتلاف نفتی، عمیق‌تر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125742" target="_blank">📅 15:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125741">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTa1NKDtxxBHCdZ_-5SSt4l8qWFg0DZFd-ukXf12yppKea9q-wiG-UqJs94zg62V507rkrv77cGaEmko5F8NqxLp-BfHLBnqXQLKh1XUzDo7iSDtOAkCFmKvvNtLGZKD8j3u6Zauuiq2-WQEaLBTXOWUKcIees5Y1p74CHRZy5lou9YSG1xOT0Hol4Ww6HrNq7Zz4Qu8z25hDg5_8zyKojJWftc88wCuN6xPcE6n7jda3B0U0WpWVgr9dcrnBCGAFNbGrSA4m-jAQCfiQpfJQ_A0tC51gm9b5b-XPOEjPmzpwxqSLi6BpSaId2HYQasj_KjvuGlDUWlMlt-v0k-dvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، با گذشت ۱۰۰ روز از آغاز جنگ توسط واشنگتن و اسرائیل، به نظر می‌رسد تلاش‌های ایران و آمریکا برای دستیابی به یک توافق موقت جهت پایان دادن به درگیری‌ها با پیشرفت ناچیزی همراه بوده است. همزمان، وقوع حملات جدید، فشار مضاعفی را بر آتش‌بس شکننده فعلی وارد کرده و دستیابی به صلح را دور از دسترس نشان می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125741" target="_blank">📅 15:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125740">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بقائی: وضعیت آتش‌بس فعلی بسیار شکننده و خطرناک است
🔴
موضوع اصلی اختلافات ما، نپذیرفتن حقوق قانونی ایران از جمله «حق غنی‌سازی» توسط آمریکاست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/125740" target="_blank">📅 14:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125739">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzEdP90RtRu9BV_kwObZA4VrzpSAmCBCc5n8wfVc-mxTU9HTn1FD3kKGOD-4ijseckuEtgA0Qhd-gGF46Dj9bWM2yGnUnwe6T7Injm0FAnZ7YLWvrpGNX6DyFwfc89mr773IuCkxh8vY5l4UWO_e_0xd2KXjC0tN2clBt1zicUI_gf1S1PswazJaNbEpSGJ5a7LPL8WsgYfs837RBw66buBQNdLIW43OfhSLNi9Hr-w4erZ6lIvS3VxqImucxn82tSH4iKeIFnhiXB4WL6mG_1pf40Bv1zJlr16PQvPzrxZJAqBW2HftCTfNhk8pi3zRqp9aCBRa6wxInorI0y51lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایمان صفا،بازیگر تلوزیون در صفحه اینستاگرام خود با هشتگ پخمگان نوشت:
جناب معاون گفتن در این جنگ‌های اخیر شاهد مهاجرت معکوس نخبگان بودیم. قیصر و صدف و یه سری بلاگرای دوزاری؟ اینا نخبه‌ان؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125739" target="_blank">📅 14:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125738">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3TJkRC6IebvPCxXy1iZ7D1VcJYg5j2E0qBjiVlfAJ4FiM3fYPdK04cqFQYOg3k-ywX-3SYH9U0yCcJBuSPp6jDb8mrsONCZfpeZhSO3tEIXozgMsd0IdxDbWfr6_oQYkot7jpJZCy2cXvvLJIKe_xe5Anqmbq5mtJOQKrkky78knKKWVngvwx1sn2gEVgwp3hUs3NC719ICO2UGJqov1RxSRXoB1UpsMxxlkADjJrVguNC-rb45XYV73HWXzq_t8lLjClDJCih6QIxEa2EmxC_g-rHxfzSZh4bFs8td4njCfy8M7R6Awb3yyyIfiaF5A3-b0a3RgSU_0pH9p3nLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125738" target="_blank">📅 14:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125737">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پزشکیان دستور داد که مبلغ کالابرگ افزایش پیدا کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125737" target="_blank">📅 14:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125736">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل : مردمِ شهر صور تو لبنان هرچی زودتر جمع کنن برن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125736" target="_blank">📅 14:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125734">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ULDeH6-J-fQhBnek07gRvaCDZDyeVuF-ryYT9uZ9BgL3YxUyFZ_g6PaJ0ZBZT_BPHIaNO23bcQReknE19WUKINqGSIfhilp7tUnDhZFGFI1ZaiLVMdOxZ-SLTSYU2YtY9xoNzKZ-BGIRZbgrg31Oa36XM_QJrK-cv39Mx9nV21dbO0uResxluW35gntONyW3TpChxFQseiDfr9ibGWX7byIUtJRaZiexvSRfmwp-98IzRtLkGG08Oo627QfIIQRzQfq9ysMzdpn77c5JwQ-PX9oThgxVtob1eR2mgFsznNSVQ1JDfstaNz1tzsTqRy5xbUbUgJQOOu_pAbjXGnBXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GVJeAbYagX2ZvxfZeTc-UYsjBaR3-rUz5rS533XmcFXfa63aW0NiClmCd46CnDaW1D8NNnef_ZgDVghaAQPE5OYhtSlDLDJbAylB1VB9aUQnpmA7AvpdLeT92e_AbEC56jEujBLMJ0C3WCgV2b87XdBUftFqbdvg1vqTmV5aMzNPLuj_FcJrz1PyOmRiRlX6v4d3Mv7VB9_cSFrIgxCoWMbTRSCItOyP8GVf7pz4kuOBJbFCIX1DQxbwsIb_qtTlWDy7xglUDnMcBYWQjWeFs53lMELWXA1tUUOUHpm-Vbach7kUUY8avLdjIW94oHtUkVYyRcBshnc628e4hbnxMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فلسطینی با مسلسل کارلو به شهرک نشینان اسرائیلی حمله کرد که دستگیر شد
🔴
در جریان این حمله تاکنون یک اسرائیلی کشته و 6 تن زخمی شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125734" target="_blank">📅 14:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125733">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
عضو کمیسیون آموزش: اعتراض به مصوبه کنکور فایده‌ای نداره؛ دانش‌آموزا برن درسشونو بخونن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125733" target="_blank">📅 14:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125732">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku195pOJqZ4fb9VG4HE3KHhk7IV66iThaEwUAkol1uOg8ZlYewrVVR1R7Tiz0lpX1dIPSaEIdicBBJ6KJo45087VCA58N7GQEuoWeqDbuG6B-i8Tkut_9H8ytzWh4IP0lphExQXCHrBXpAyU4zome_VUF20CMMahm_vbBZyAL39kZ_CIWVmjIzemdkmyU_0i1YPQiXlLCoFSzmVMTC09pMHLFpmLh_eyO0yhW3okk6gNmB2iXfLqca-hEsaETPtc4eeK_GgkdX5nhH6fL0XSu9_JARm2w6v7SJREOX7EZVQ2x51-mJQGFHPMLPAqiYqteFEG2Vw_lK84bBVj5Mty3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روند نزولی واردات نفت چین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125732" target="_blank">📅 14:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125731">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه در گفتگو با سی‌ان‌ان: مشکل اصلی مذاکره با این آمریکا این است که شما باید با مواضع متغیر زیادی روبه‌رو شوید؛ تغییر مداوم خط قرمزها، اظهارات متفاوت و متناقض مقامات مختلف
🔴
وقتی آنها در مورد دارایی های مسدود شده ما صحبت می‌کنند، هیچ امتیازی اعطا نمی‌کنند
🔴
تعداد قابل توجهی از مسائل اختلافی وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125731" target="_blank">📅 14:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125730">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری / ۲ زلزله پیاپی به قدرت ۲.۶ و ۲.۹ ریشتر  با عمق ۹ و ۷ کیلومتر پردیس را دقایقی پیش لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125730" target="_blank">📅 14:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125729">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpFBfpzwZJslH8tqZPcdd6L5AkK6lfQPq2-qRHEPk0WeZaCYeiD47baju1pSiSJvaMdBsecGF3QysJVYo5gGXf5a9fdMYQOH685V3NeGOjou46SZBm_EAIj9NuBXjR9FaRe6vMSVJpsFd1KPw0LZORqfdFU884_2_iWE_g2pFUocel3Lbr_mAt-tItlz-sm9F9dP0M3AVbVp1VNSYk8KynLLKfnVDZU-Iu1REbclRFOUJE2Bx13mzGbgnJ_dSSdMTkkwl-DASXq2jWCAHFqhzTA6qOT-xEGOcM1bfS59O9PiDRMUrVlbhdQSwgejZnEiFk6blPZI5vr3lldekokq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بانک مرکزی چین در ماه می بیش از ۱۰ تن طلا خریده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125729" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125728">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
عضو کمیسیون برنامه و بودجه مجلس :
از کشتی های عبوری از تنگه هرمز ۱۰۵ تا ۲ میلیون دلار عوارض می گیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125728" target="_blank">📅 14:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125727">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
عضو هیئت‌رئیسۀ مجلس: وزارت نفت صراحتاً اعلام کرده که قصد افزایش قیمت بنزین را ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125727" target="_blank">📅 13:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125726">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل: حمله در مرکز اسرائیل هشداری خونین درباره ضرورت ایجاد تغییری عمیق در میان عرب‌های اسرائیل است
🔴
اسموتریچ: گسترش جرم و افزایش افراط‌گرایی قومی در میان عرب‌ها در اسرائیل، خطری وجودی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125726" target="_blank">📅 13:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125725">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK2OvznSIqSM782t4jIopyErmKm5D_z6gKDRrL71DVrSfNaoNbxUXbo7Ibfr71MbCYq1HjjZURREhVfMOXGgHU3FhRB9mtTI4pkJYTVYzqyrnQkWo8LI2jwfRue5SiSmxa-zTmpcQO7ghN85S9yIlmR2sLWzGdX09vKQfhlQ_37zuIndhdAlDOO2Zziygjmy3TlT1LYuZYod3b1QReuaqMZuMIaxnzfqhDkbQ2Jn7zvp4UmhkeoT3ZIKnyW9FGwJG2CDhKQeqj9wctLMA8KyWAhgSQxmRscLd7bDSfZAM1ONBFis8S1fq9qE_r6bxOUDLORdTG-JuW4UhGw8ik08iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طرح«بانک زمان» توی منطقه ۴ تهران اجرایی شده و بزودی به بقیه شهرا هم میرسه. حالا چی هست؟
🔴
توی این طرح مردم به ازای پول، با زمانشون بهم دیگه خدمات میدن!
🔴
مثلا شما یه ساعت به یه نفر، زبان آموزش میدین و به جای اینکه ازش پول بگیرین، اعتبار دریافت میکنین.
🔴
با اون اعتبار مثلا میتونین ۱ ساعت ماساژ بگیرین، یا ۱ ساعت استخر برین و یا خدمات های دیگه...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125725" target="_blank">📅 13:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125724">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزارت امور خارجه ایران: عراقچی و وزیر کشور پاکستان در مورد تحولات مسیر دیپلماتیک برای پایان دادن به جنگ تبادل نظر کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125724" target="_blank">📅 13:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران به سی‌ان‌ان: مشکل اصلی ایران در مذاکراتش با واشنگتن، مواضع متناقض آن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125723" target="_blank">📅 13:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125722">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری /  یک‌ مقام‌ ایرانی تایید کرد که در صورت استفاده از دارایی‌های ایران برای تعمیرات مناطق جنگ زده کشورهای خلیج فارس دوباره به آن زیر ساخت‌ها با شدت بیشتری حمله خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125722" target="_blank">📅 13:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125721">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
دستگاه‌های اجرایی موظف به استفاده از پیام‌رسان‌های داخلی شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125721" target="_blank">📅 13:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125720">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoAcHURoOZWAGk74OaMuuz929I-I-IT6tubRd6imSLCKyjTaLNRdYv56WmFUuXUhzc-YHzhMrqWdUBzj8DyKPkowR6Y4Qeepbmgs-rXV5tk8eLtQkPKsZZudL_Zg3EHBdZQ1VwjYvj0YHMZChYRBNYkT5ID2dmAA85TDxcLMYZLzvsdP5XzLtYeyjs_RtDN4HyFwIfdboU9lFkiV9z3O-TgMT19Z_5rCCyfnH1w0aaRs7tPbY5CCaObJ9SF34kIQUQQYqwJlkXBjNEbfXgUZVop1GYN-2PP5L87OvtJr6uEdTqGbtR2j7CeFG522SPOSvX-meg5cNBXkz3H9s06YoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین 200 بوئینگ می خرد
🔴
مدیرعامل بوئینگ : این سفارش تنها «مرحله نخست» یک توافق بزرگ‌تر است و انتظار می‌رود در آینده سفارش‌های بیشتری از سوی چین ثبت شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125720" target="_blank">📅 13:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125719">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGxjASmqR0mS9rCzNFXKhtovfHD9UNuxj95cnnDfPe8qJ-6e98uIxrcKvdDnibZYsCmH0nMWvb6nNFajJcigOI4tgAB50DbvB2orvxCw80BLzSmmR-KSR6vUyFu_APd6KwenZi3tuXTL-jT1kEd2ujawMXSpAGOwCUbR6ff0eVUrSZxXuDd3pRgsLrZJy2CAoOwDmsR-Tpt_6SiYBUO4WPDU0dUtB7iXDhVvCPgVfxbLTDux11Oh-NcnOdU4v8LmEvONeR17Gf6gXYBYORUHvpKEM43OMrpF2yhagl-FIEZAwPMGDDxKy-LISpfqZyMUx2IoqmAgkLdK0DF--DFKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125719" target="_blank">📅 13:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125718">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
معاون وزیر نیرو: در دوران جنگ اخیر بیش از ۷۰۰۰مگاوات نیروگاه ما دچار آسیب جدی شدند؛ البته همه آسیب‌ها و کمبود‌ها با صرفه‌جویی مردم حل می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125718" target="_blank">📅 13:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125717">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وکیل: توبه «تتلو» از سوی دادگاه پذیرفته و برای طی مراحل نهایی پرونده به رییس قوه‌ قضائیه ارسال شد، ولی هنوز تصمیم نهایی اتخاذ نشده
🔴
اینکه موکلم برای ماه محرم درخواست مرخصی کرده تا بیرون از زندان مداحی کند، حقیقت ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125717" target="_blank">📅 13:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125716">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad0a1c177.mp4?token=emcTh-dmlW6e594gJzGFrxBsY45FkHGtjU1AvsGeJBfjF8L1f_Z2z_RAPclqIlneS9oGALt2oUY207WlJIRwwyfH3eCHPp1a7rZRjOb46THbdGZu6ljvB4VaHT0nNwfpIVuzN6ZrHUqz5W6NtI_JV6J-oPeZy4HPtYIeGcwZgOQ1aB-sdpnIek-o333paxIuMR5vjR-YD3TXTitF-g4rlhbYiwCUmW4EtXfjUBzBH5wdXSY3c1D9w47JWll4mePhiFBf7ZcVQGVy8-hJM74x90guM-UCz_3edxcUAbeECi_AGCOP6T0L3VIJlA7eZsyhSxyneZV22f6NVXj_lQj4Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad0a1c177.mp4?token=emcTh-dmlW6e594gJzGFrxBsY45FkHGtjU1AvsGeJBfjF8L1f_Z2z_RAPclqIlneS9oGALt2oUY207WlJIRwwyfH3eCHPp1a7rZRjOb46THbdGZu6ljvB4VaHT0nNwfpIVuzN6ZrHUqz5W6NtI_JV6J-oPeZy4HPtYIeGcwZgOQ1aB-sdpnIek-o333paxIuMR5vjR-YD3TXTitF-g4rlhbYiwCUmW4EtXfjUBzBH5wdXSY3c1D9w47JWll4mePhiFBf7ZcVQGVy8-hJM74x90guM-UCz_3edxcUAbeECi_AGCOP6T0L3VIJlA7eZsyhSxyneZV22f6NVXj_lQj4Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صف طولانی کشتی‌ها در هرمز از لنز دوربین یک گردشگر در عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125716" target="_blank">📅 12:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125715">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv8SArXlrWPEv7Fj7rIschOU1lUyS3jGPdCoXNe1vV9NamSI4EZe5eWIuCYpUbd4Q2fHU9iATge8k2MELsIdSG67NXlieCa2dh9EXUYYV9aFBa_h1TbYMfSSbiTXv8Cz2upP2i1F-jUVTUIbFbgPn0T-YPoZcASH4b-mBTcZjHpj0u9OGVtGhpx9gUurCiVjJWtTWmuv0y6F20-nkc8Z3JtJXEC5k3DjuxK2gdwYo_Pqt4-x4br8x4mB54yKp6jH55J8k4p7PWCeBcd3BBY7hGpnKgWD21ZzNRBPtRUy11m0-NStnMy_cjYcKK_xbSm6vC2cfRO4d5Vx2LXl_qwwWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از زمان جنگ ایران خرید غلات و دانه‌های روغنی کشورهای خاورمیانه نصف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125715" target="_blank">📅 12:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125714">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbj9yKHUG6w2atRR1o7EP4SWgMDkzdsGpZmHBrHFeW_x02MeDAceOHzo1icdou1vJ0J55YUWpne3Vydn3xQ6srdJIP2AV76ObNQ7lKNKvheVCo6pMyajCPoL2c3vEv3YXesnQQcVPtTPTT8ngJkJsE4vBXjoey-znjiN28-zx1AWPP_aKNdF2IueZD0ymjAn6KCDKEWo78LF3rzr8592b1R9xpYkVLW1PqDkzKQRwH5uPkb9fPOGoTF2cuUiFAPNqFJvhP8m4SsU2i_BrpdZH_VyZB0LpUDcOsVgi1euexAqSDhKI6Grkb125Kp35aEIUtbMZJ9_CfCQj2fmBeY7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انبارهای موشکی کره شمالی
🔴
دولت کره شمالی برنامه ای برای چند برابر کردن ظرفیت تولید موشک های بالستیک برای سال جاری میلادی در دست اجرا دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125714" target="_blank">📅 12:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125713">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزارت دفاع روسیه : تو ۲۴ ساعت گذشته ۵۰۰ پهپاد اوکراین رو منهدم کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125713" target="_blank">📅 12:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125712">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GL0FdEjh4ZUyVB_oJAt4LFQRTGOGMceHHKUxN4ThsIoxNDiW4ATBLVO1BK9SlQ-4FCp0yRmt9GZNfIPsvdyrBeGKKCTYqzBN3Civ9g2xt8N-zVeatDqxJY_PpJMKzDUGAKMkPsqx7rbIos_0Xw5-1jfGVo3re1wgDGvHDUXTYOC3NYye5x3rmXg_Z0fIpIULAXxBbUXqo4x8GUmRmkaDce4cD3v3lNqQlR1REuT79PY6fTbFZQiaYdT7aauOVl7u6qfDKt2H0yf0KBHZpOZg4PTu_01cJ53vAR4Q9SK__8jHeRlrFxoZx1mBX_bWnvZwrUH-ypCqdVFaI4xp951rTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۱۰۲ هزار واحدی به ۴ میلیون و ۴۹۴ هزار واحد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125712" target="_blank">📅 12:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125711">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نت‌بلاکس قطع گسترده اینترنت در کشمیرِ پاکستان را تایید کرد؛ این محدودیت‌ها در پی تشدید تدابیر امنیتی و اعتصابات پیش‌رو اعمال شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125711" target="_blank">📅 12:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125710">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وب سایت خبری «والا» ارتش اسرائیل عملیات زمینی را در حاشیه شهر النبطیه در جنوب لبنان آغاز کرده است.
🔴
النبطیه یکی از شهرهای مهم جنوب لبنان است که در گزارش‌ها گفته شده نیروهای ارتش اسرائیل در اطراف آن در حال انجام عملیات زمینی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125710" target="_blank">📅 12:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125709">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نامه‌ای که وزیر کشور پاکستان آورده بود برای مجتبی خامنه‌ای، تحویل عراقچی داده شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125709" target="_blank">📅 12:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125708">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری / خبرنگار الحدث:  تیراندازی در ۴ نقطه اسرائیل رخ داده
🔴
تعداد زخمی ها به ۶ نفر افزایش یافته و یک نفر کشته شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125708" target="_blank">📅 12:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125706">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hCE0YtEZVJOz_uxU4t5eAdBqJQuk1o0NK0mFD_iCnYSJdtLokJihHpDvYuGczgoKYHJg6d84fz9QcR5A2fFQpkCqRiaL3KbuMhlxkg3Y9UzhHp8E23QH_u6-85TR23sgVpElESkaa24Zu03sReyiILt6FTri_ZYbNFyCr68rqb0h08KrGlKipXUOec_TrRuQiwyIglR3SKtb1CfHj4z28zQ6kqUxFyFcynL54lHeHbjoxg6tyvBSQNy8c6mGal78vOaA3BB8vzH26Xw7ci-XKCT34Q83vqOpRWiYlWdwQIeZlbCFakVJiraJGTj0xGQSIPOdqvCBGmT6Fprw7UV7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4OhfwwkO7-Y0PNSS40Wk9R2TWM2N4GqB-7VF6KHvYdMXR59YOs_yYD1SEbsm8b0Q7hsiMo101aXa1V7W4FlDVF8dZH23SWU5vLCofjK4S3q0OzEyvhKzg4X5A366UDET0XyMMB8um6e0aN0ncnnv6w52788-RO1hEfRKJ6-NNcZK_6Ssskv8yM9UI3zfbyNGZ5NxXG6aRRNi_Cn72RFfQAQZD1cBItK2lU4o1EdfoSay2LHzxPemAIh7ZnIaNgnGULnI7KZxddkpGpCuM4ABSYsX6Jp9rOlkkj59cx8ImxRZDzNRVJmX_GfcLbEDnvJFL82i-LUOI4YF1m9xspjxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امیر قلعه نوعی دقیقا عین این ایموجی شده، حتی رنگ لباسش!
🫄
@AloSport</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125706" target="_blank">📅 12:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125705">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
مهدی خراتیان، کارشناس حکومتی، در گفتگوی اختصاصی با برنامه «ایران‌تاک» با اشاره به دی‌ماه ۱۴۰۴، پایگاه مردمی شاهزاده رضا پهلوی را رد کرده و علت اعتراضات را افزایش قیمت اقلام خوراکی دانست.
او با اذعان به اینکه در جریان اعتراضات حدود ۱۰۰ شهر در آستانه سقوط بودند یا سقوط کردند و برخی فرمانداری‌ها نیز «مانند آب خوردن» سقوط کردند
، گفت: «ما دقیق اطلاع داریم که لیدرهای اعتراضات، جمعیت را طوری هل می‌دادند که سپر انسانی مقابل ماموران جمهوری اسلامی شوند».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125705" target="_blank">📅 12:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125704">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq5yB4kPz_tWif7zfaV-ghNqROIb-nDqXlCJMQopor_7SS9-fc2vuihch1o09YAZO88rE9bOXVwNsVivVqdyVHCzXkfqPIfXh6AyJu2Oq28LksgCLRCvSfDmly9OBgTlqCPaC-R_3VCSIu6x26eABvH0v11c__ZwNvAotZHKaAFv6RUCPYl1TU2RxjVyR1Q9cnoGZlnfCYLjaHfwhf-aiYQQiB35xcnjSiCtpfHCxhpbAIzEGqZceEyiolFXo8vbpeM0oHdW4JBNl8lAfcEXyp9HjARspsSrtp3L1dE-3lBlAaNevF4VxWD4X5ODYEdrJgveaCHCrox8fitrPEocBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نامه‌ای که وزیر کشور پاکستان آورده بود برای مجتبی خامنه‌ای، تحویل عراقچی داده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125704" target="_blank">📅 12:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125703">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPIwJWO-RRNL20AY4RNgWYiqAgWoi6XctWqdg9BstJMZiWZHLgGTgsnkL3dtZELC9BiyQpOJGuuRSHiEfXuzIxsnLytOc9hzkbLKotHAglf4-wwvAejlXAMJdog9ZIv7yrGprunsI5QkjqWw95VIfd1awxLeY9Ym1E0zlogB10Qm3oNGoaiKjIPXhXffLf5qr3GYDZgdLWcLw85sS_BhPpn1CIR26ymwOjwPCpLsxT9rUNHnMixgE70ikVvrXmJud_xKBqSTQ2SBAdoEE7j1GR_UVyeyZ3r20HazhmYiI-yG60SLZ9qptkrERc1Hbs5mixVATgkFzbGBBj_hQHtzZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسرو پناه:اونایی که اعتراض میکنن دانش آموز نیستن بلکه مافیای کنکور هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125703" target="_blank">📅 12:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125702">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893be9ef42.mp4?token=VtSKKbMzF52DkOZowy9gfpXZ16zY4hwAkOzq7Gwk5sboXZhYIXResquxU_6INJ7WaE0r3F6n3TEGTOchcGDsEdVpN5r2jOrzsMkj-aMoaJI8HOVpJMoRHeHmbc0kl-TOiEeKwcQsoEON2sM5w906Orb9xYXJF_BF5bqDFD87iBXWXp_lvEmKADD3ZwJ97W4cDHCLvHLwuxQfhMUcYOouS3aHjRys5ny1K-Vwa_eX8PQPboHrDbypBI6jYSq5pSRq-kbuWyVpMredvjxhQlqTN41XwY2McM5jRchDP1DAC4YldnaRlfIZznfoJ8RR0KpOkVRSlEA7eoWCTjUuhpGacQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893be9ef42.mp4?token=VtSKKbMzF52DkOZowy9gfpXZ16zY4hwAkOzq7Gwk5sboXZhYIXResquxU_6INJ7WaE0r3F6n3TEGTOchcGDsEdVpN5r2jOrzsMkj-aMoaJI8HOVpJMoRHeHmbc0kl-TOiEeKwcQsoEON2sM5w906Orb9xYXJF_BF5bqDFD87iBXWXp_lvEmKADD3ZwJ97W4cDHCLvHLwuxQfhMUcYOouS3aHjRys5ny1K-Vwa_eX8PQPboHrDbypBI6jYSq5pSRq-kbuWyVpMredvjxhQlqTN41XwY2McM5jRchDP1DAC4YldnaRlfIZznfoJ8RR0KpOkVRSlEA7eoWCTjUuhpGacQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار تجمعات شبانه : ترام ترام حیا کن برو خونتون لالا کن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125702" target="_blank">📅 12:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125701">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
طرح رایگان‌شدن مترو برای ۵ دهک درآمدی در شورای شهر تهران رأی نیاورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125701" target="_blank">📅 11:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125700">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر کشور پاکستان با عراقچی دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125700" target="_blank">📅 11:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125699">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
الجزیره: ارتش اسرائیل در لبنان در وضعیت واقعی فرسایش و خستگی به سر می‌برد
🔴
معادله کاهش تنش و محدود کردن درگیری به منطقه جغرافیایی جنوب لبنان، همراه با محدود کردن عملیات تخریب اسرائیل، در عمل با هزینه بسیار بالایی اجرا می‌شود.
🔴
اعلام کشته شدن یک افسر و یک سرباز اسرائیلی در درگیری‌های اخیر، موجی از خشم شدید و گسترده را در محافل داخلی اسرائیل برانگیخته است و تأکید کرد که ارتش اسرائیل در جنوب لبنان در وضعیت واقعی فرسایش و خستگی به سر می‌برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125699" target="_blank">📅 11:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125698">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🌐
با ما همراه شو و در زمان قطعی   وصل بمون
😎
بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
✅
از ما با کمترین قیمت ، بهترین سرویس رو بگیر
👀
😍
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot @NetAazaadBot</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/125698" target="_blank">📅 11:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125697">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SXbhPWO3Vl1vzQoMz6seMAxt_yxtr1oZY2CFUrmkObrZy06-cViXb9LmwiBXl30pvhos1xfMn6y7H0UOjGPA51EV3-1ReJJAa6_tOmE_eVh6oKVhXGJORtI1SAzig8uXtfOKevYnJp04S8PfF-OA8gS9udyZ96uLU_YE86Tuzpvd07XzitBCpyG32tThNwLGO2ixh7a4-TJGjT4dKiy-BIGRy-mxR7bbFVUlL82i6vDjGVEhipNfVZxcuGWgCZ4mV7cazuEehNg3tDzsuKItinen6MBjuha4C844iCc_IOUuiTKkyRHa8OsQzMTNZ-0U-qkyUeyKymK7pqdnA20inw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🌐
با ما همراه شو و در زمان قطعی
وصل بمون
😎
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
✅
از ما با کمترین قیمت ، بهترین سرویس رو بگیر
👀
😍
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/alonews/125697" target="_blank">📅 11:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125696">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
تتلو واسه ماه محرم درخواست مرخصی کرد که بیاد مداحی‌ کنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125696" target="_blank">📅 11:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125695">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در ۹ اسفند ۱۴۰۴، امریکا موشکی خوشه‌ای که با انفجار به ۱۸۰ هزار ترکش مرگ‌آور تبدیل می‌شد، به لامرد فارس شلیک کرد
🔴
این، صحنه‌ی آزمایش جدیدترین سلاح مرگ‌بار ایالات متحده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125695" target="_blank">📅 11:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125694">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3FdiGnvhIpJkJiQMZUymQx-81W2YaU7KdpkHy-_mNQh77TN6QfQPeQcu5QFgb8uMuF1LaEsbcPoxjGVf4l9nfO_Yoxj5Ix0v61o1uwFavttq7TBPiasVdNBLixCn4a28T9Yi7fUZx9Tmj2x0D6mp95SnafRSqbOJOcZNCoyHOq_xmb1AYSrwCjdhcV-wwPSOqy4tJwoyS4UoBQP_USgKGDGQ4GqIF__P6g_y09Z1FPnGQN7hD3WqRwiHYgXzIcDvFJRHpRCjj71j25J7QJ_veSg43LFZhJa3Vq1DIYv-Gu-nSnAMulSH4mfqRQdWZKoQXm2wmw7qIKomUyTVmAH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص بورس تهران در یک ساعت از آغاز معاملات امروز، ۸۶هزار واحد مثبت شد و به ۴میلیون و ۴۷۸هزار واحد صعود کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125694" target="_blank">📅 11:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125693">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار کنترل شده در یزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125693" target="_blank">📅 10:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125692">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">‏از وقتی اینترنت پاکستان قطع شده  کانفیگ‌فروش‌های ایرانی خیلی جدی رفتن تو گروه‌های تلگرامی پاکستانی و دارن وی‌پی‌ان می‌فروشن.
‏توسعۀ صادرات و ارز آوری برای مملکت به معنای واقعی کلمه و آتش به‌اختیار.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125692" target="_blank">📅 10:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125691">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.
🔴
رویترز خبر داد که وزیر خزانه‌داری آمریکا به تیم خود دستور داده خسارات واردشده به کشورهای خلیج‌فارس در حملات جمهوری اسلامی را بررسی کنند
✅
@AloNews…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125691" target="_blank">📅 10:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125690">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
معاون وزیر نیرو: هیچ برنامه‌ای تا امروز برای اعمال خاموشی‌ها نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125690" target="_blank">📅 10:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125689">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.
🔴
رویترز خبر داد که وزیر خزانه‌داری آمریکا به تیم خود دستور داده خسارات واردشده به کشورهای خلیج‌فارس در حملات جمهوری اسلامی را بررسی کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125689" target="_blank">📅 10:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125688">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5faa7d2315.mp4?token=MDzqsBtWSZxi0eFKyJcgZrsoLFr72WaiOW1qZoeTdSQ2TPuBNFDh7H_MhlqaShIE5f8K-MSDCyDnBYvaTZ0FI2FzMBbYCFjoqiAsZzVVs5qXkxVI9TxWi7fS0qvr5IUt7sXHvbNYoJjoOCyFlxy_yERSrV11we9SGE1OaksuieG5hTVfMWTs8yiR5y4DOpeqgnHSWAS2XYVIoca6U2hvYP7OQGkY9yhbjwFNHhwIDUcHRw5ICWQ9ybF1cHmzFP9MByNOXgvg65VWaso1rQyoJiMjLbsxTeOkXFbLNEwgDHpiyvma86nltLeIrRGOMG5LXeYOL9sXeWoPWB2272GdzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5faa7d2315.mp4?token=MDzqsBtWSZxi0eFKyJcgZrsoLFr72WaiOW1qZoeTdSQ2TPuBNFDh7H_MhlqaShIE5f8K-MSDCyDnBYvaTZ0FI2FzMBbYCFjoqiAsZzVVs5qXkxVI9TxWi7fS0qvr5IUt7sXHvbNYoJjoOCyFlxy_yERSrV11we9SGE1OaksuieG5hTVfMWTs8yiR5y4DOpeqgnHSWAS2XYVIoca6U2hvYP7OQGkY9yhbjwFNHhwIDUcHRw5ICWQ9ybF1cHmzFP9MByNOXgvg65VWaso1rQyoJiMjLbsxTeOkXFbLNEwgDHpiyvma86nltLeIrRGOMG5LXeYOL9sXeWoPWB2272GdzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در طول شب، پهپادهای اوکراینی به انبار نفت سیمیکولودیانسک در لنینه، کریمه حمله کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/125688" target="_blank">📅 10:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125687">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkahdQEOBbWbbrAOlT9vWMRsyjyszeF-R7bf4M91UySVgw6Dj2VY_FdK36ud4Z-iHeCmPGRmnpn4zxPkGqSn91cCedHYqHC-rJKzNs2n_tmdKgprRAHgknKvKJCEw1Y_dvIkZxcuuI5pHRAlnz2UUHqW7rjHFvFHuEI_sZqRae0AjST87NNjF4YDiNQxVBJSWiR_bglIjvdw98KLcW3Mc59cKXJfxPvJToHAp5CQm37PzxcQwf_gyhhsykK3sG_0-y50Tqc7K1CpiBXKvyzc1jBImB756GtvUaNNDLLgPa6sP0A0Ad0tvspdudrWjhQwMWDcvgWHGu05WuAQCbzjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه:مذاکرات متوقف شده بین ایالات متحده و ایران... و یک "پیام بسیار مهم" از پاکستان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125687" target="_blank">📅 10:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125686">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
روزنامه اسرائیلی «یدیعوت آحارونوت» مدعی شد: خانواده بشار اسد رئیس جمهور مخلوع سوریه خواستار خروج از روسیه و سفر به امارات و بطور خاص امارت نشین ابوظبی شده بودند، اما مقامات اماراتی این درخواست را رد کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125686" target="_blank">📅 10:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125685">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f9YLplwjE6VqFzk_PeyuX8MpCEXPZD3S5M1YyC0p_CZWX4d3eUTFFJjRSPdKDWOiSgPST-OAg10d897zOL0gZHzTAA-bo3R6BHWlOla9BPUUec3jQXpanLBSEsDyUpMflsk477i5DabvvP4nI28b3uTifT2Nok45Avn8UIJmuRT82LZMDfXT9ZZHZKKX-eQ3GnN1qJDFma-cYIkAk12auvNawCXaZhWV95NJ5iCm6iQ5R7kseNJKREEeA5bVKspORt9hHyMm9xUKkQt5bDBdaWrYlYT4LGqoJJE5_uoup6iKMw03aMtVB1qkYWbEGppbduJeIl00yClrnH2lhIYe4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر سوخت تقطیری آمریکا به پایین‌ترین سطح از سال ۲۰۰۳ رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125685" target="_blank">📅 10:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125684">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
الجزیره: در پی جنگ علیه ایران، ۱۴۶ کشور قیمت بنزین را افزایش دادند
🔴
نرخ مواد غذایی نیز همگام با قیمت انرژی تغییر کرده؛ این موضوع بر هر مرحله از زنجیره تأمین، از کود‌ مزارع تا کامیون‌هایی که مواد را از مزارع به قفسه‌های سوپرمارکت‌ها حمل می‌کنند، تأثیر گذاشته
🔴
اگر قیمت‌ها همچنان بالا بمانند، خطر سقوط اقتصاد وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125684" target="_blank">📅 09:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125683">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
فرار هالیوودی با خودروی پلیس؛ متهم دستبندش را باز کرد و پشت فرمان نشست!
🔴
یک متهم بازداشت‌شده در آمریکا موفق شد دستبند خود را باز کند، از صندلی عقب به جلوی خودروی پلیس برود و کنترل خودرو را به دست بگیرد.
🔴
در نهایت واکنش سریع مأموران، این فرار جنجالی را ناکام گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125683" target="_blank">📅 09:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125682">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
یدیعوت آحارونوت: هنوز برای اعلام پایان توافق آتش‌بس در لبنان زود است
🔴
با وجود اعلام حزب‌الله مبنی بر رد توافق آتش‌بس، اما حملات به شهرهای ما متوقف شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125682" target="_blank">📅 09:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125681">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej_PiE0_CDEMqiJHn3rl_sFk0M4J9GphhWXKikoBe8vylgNu1XYtWFZuHI2YdTs1iIEsn8J2A1ngnZec2H0dkS4SD7hxx3ZuR3wbE9eX-CgO-UwLsdTurXyct2Jc_Hi6eQvU2ONlXsLLn-uDfTm5ihaJEjGccjH0zTR3ObZ_5IHcCOzROg6HldAZtEDBrfq04XsgC64_D_aGKmTQDVvxqWdLlxPyMEElmtaKCRsbKJYJpvOXV9HH7cy1YSySRtyq0tyuQfzJADc6jun-gBC78QQJIv-wCEv2VISBCeIvWMBVwBTOE3Y3GxtvIQnVFzTsW2Dh1lkwzLyOSg4hR3o9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۳.۰۹ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125681" target="_blank">📅 09:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125680">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDvutrp5ml9SGGOnRftK8lPHvDsSr1g9rJ-MMHOcELfxhJRMO1Gu2Ns0we2dZx97PKc3CFbNfa6ck-y0Meyi8jkJoRqFynJ4cBTl6ug6NVtHypbSi6VJxLI74v0sN7yimsmu67P0FuFuoWFTojluuMnR69hFePnhglBC2ZFo3KTbKfVMuc4ZwMNo8M_Msd_p0ysEEUMsc_DNVosmG6iWMDCwS1Gv3jNay0UjukuVNvZu5qfHbyr3KpniOHAClyE4-5tFlFrdywGX2J2awCvxo9ODNPsj2PZHpsS1p8662QrBpBOf7OA5RfVFGYJVP5eXUxdcf8ugqjRLz87LZMJFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ با انتشار تصویری با عنوان بندر پهپاد نوشت:این روزی واشنگتن را نجات خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125680" target="_blank">📅 09:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125679">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWKq8eVg5xpxr_hlnJ8SqYl3wlmGHos3iJq-E3RzDZvSDpLf3R9OowdIg1g7MoZ9oA2-2J-qiqPpjIIKF5mj1ZqDJB-Qya84eV3BGbIkmom4ntO2BWYJjo_0lDYToXkS-bXC0W1mhnAMOhF-P-jgno_jn3f3erzalk5Oa_5cVKCl8pPL-J3Agr1anKQnfA2NxTF7v7_rcYhpPXS7KdqKIzRaa3lSgq6fUyEs8V-bT_UnOVmSA-9ZMEILDquvoABWg-tCAXnzBm87xzBtkzkMbn55gl4BDOqTCED6fckZui7sg5crQbTtVEkb7AUpT_4Tev9iPs8T1k49Op1h_p0jsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیم یو جونگ، خواهر کیم جونگ اون، اعلام کرد که کره شمالی هرگز از جایگاه خود به‌عنوان یک قدرت هسته‌ای دست نخواهد کشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125679" target="_blank">📅 09:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125678">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
یک تیراندازی جمعی در یک جشنواره در تولدو، اوهایو رخ داده است که در آن چندین نفر مورد اصابت گلوله قرار گرفته‌اند.
🔴
قربانیان به بیمارستان منتقل شده‌اند، همراه با تیرانداز که در بازداشت نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125678" target="_blank">📅 09:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125677">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سفیر ایران در مکزیک: تیم ملی فوتبال ایران اطلاع یافته‌ که باید در همان روز مسابقه وارد خاک آمریکا شده و پس از پایان بازی، از خاک آمریکا خارج شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125677" target="_blank">📅 09:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125676">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در اربیل منابع خبری عراق از شنیده شدن صدای انفجار در استان اربیل در شمال عراق خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125676" target="_blank">📅 09:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125675">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
امتحانات دانشگاه جامع علمی کاربردی غیرحضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125675" target="_blank">📅 09:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125674">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
کره شمالی: سلاح هسته‌ای، حق حاکمیتی غیر قابل مذاکره است
🔴
«حتی به اندازه یک سر انگشت» در این موضوع عقب‌نشینی نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125674" target="_blank">📅 09:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125673">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGKTRr66lUC9wibSB7yvOuJHBNr_kyu4lSClu_Z7onvjuoS8RM7BAPUB4yGf6lqHIH9ssm9VPelyd1WV-rNEciDOHs-jqQ8-RQHCeMidKbIMTyPnjckOxeo0NLJ1SVTpiSXxL8-qXpvQUdIaPxeJ2axsOk0Locfq6_WE78jytRpV4PqBC5pLk8YTehPCSgs5ykbwokJgvDTNwI0qHUeXmi7SDhW_8iUoFBPrmvWmlpUyV8dsfJJEqFM61DsiJINuEF2jyPabJS3TZF_g11tfPfQ6Ja7j7sD8_0VvIwjSAZLf1vn94PGIaYkasMWhkHdHDIUxiVMdq0PelGCpO2TsFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام مدعی شد امروز دو پهپاد ایرانی را بر فراز تنگه هرمز رهگیری و منهدم کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125673" target="_blank">📅 08:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125672">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پولیتیکو: راه‌هایی وجود دارد که ترامپ می‌تواند توافق آینده با ایران را به نفع خودش تبلیغ و توجیه کند
🔴
اگر ایران موافقت کند که برای دسترسی به دارایی‌های مالی خود از یک خط اعتباری استفاده کند، ترامپ می‌تواند ادعا کند که بر خلاف اوباما، هیچ پول نقدی مبادله نشده است.
🔴
اگر ترامپ اجازه دهد ایران به نحوی از تردد کشتی‌ها در تنگه درآمد کسب کند بدون اینکه به طور رسمی عوارضی دریافت کند، می‌تواند آن را به عنوان یک مصالحه قابل قبول معرفی کند.
🔴
اگر ایران به عنوان بخشی از یک یادداشت تفاهم درباره چگونگی پیشبرد مذاکرات، تکرار کند که هرگز به دنبال سلاح هسته‌ای نخواهد بود، ترامپ می‌تواند آن را یک امتیاز اولیه بنامد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125672" target="_blank">📅 08:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125671">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tohEHrfBbFVef42P7I8FtnxrSTEQxj6M3qnAEx1ZNHEtUbO4AQ0llDRqpZQDVIdmP3WMSUMP4nCbkpJ6tT1aoPsfK-ulhiaG-2beO8U9KlC16phPflbmG5qOozxmaTnPwPhf1euLXdcjvrHf3KuPOpLFz9fDWNqq4IIGwJIZwV1wsMs_jH3WMTZcQSbye6oJswn20jGoB9unr4CSymgUGFVb_nHl7V6TGZFTsQYMw8punh5r2r7wok4c8VipQ7uNn8jK2F9MqZBoDIuAksaEzA1b4fQXCt-7pKUAFmVFRgv4Uj_vU8a58iduvI1lMCqKJIrTK5Hy013mv0XE-7Nypg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایجپت اینتل ابزرور: تصاویر ماهواره‌ای تأیید می‌کند که از آوریل ۲۰۲۶، عملیات توسعه قابل‌توجهی در «منطقه پشتیبانی لجستیک ارتش ایالات متحده» در ینبع عربستان سعودی، معروف به LSA Jenkins، آغاز شده است.
🔴
به نظر می‌رسد که نیروها و تجهیزات نظامی بیشتری از آمریکا به این مکان اعزام شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125671" target="_blank">📅 08:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125670">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر خارجه عراق: یک فاجعه اقتصادی ممکن است رخ دهد؛ اگر جنگ علیه ایران تا پایان سال ادامه یابد، با مشکل پرداخت حقوق مواجه می‌شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125670" target="_blank">📅 08:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125669">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTVGwXSBDGiaUCRjyV_1fP7CX0o9Gzrmm4S4uZKX5jVuEvocJKFr11OONUblO8HOILrBy0iy70V4o39WFz5uG8HxaFlG0bWObEQS3eipPpf8-WzSRWwlTyJOMvZ47umzoB5UhXMeB0uFY9u8MLe8cSQ9pho5x3O5mNElGq8G-xMh7Uki46ED9G6-Q2CNCS7qjzbZH5e0-UkRkdCEz9mZMveYsNnW-nS26caMAyww_x3yrja0qxBVzPPhkYV3iXCGPWUqml-PwBfXn4u6DIUKop53XjfnWNmn9FFsQeG30weoRGipm6ure6lyXPMCHr7uwdPRSlLPc6ApNTjDbGpndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش CNN: دولت کوبا شروع به توزیع سلاح به شهروندان عادی کرده و رسماً از آنها خواسته است برای یک تهاجم نظامی آمریکایی قریب‌الوقوع آماده شوند،
حکومت نظامی در پایتخت کوبا اعمال شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/125669" target="_blank">📅 08:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125668">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_DLYbS3EppG54ErI9OFfGe0iDV9kUORGjMfURN3bKLl0QCizCJ2m_9rG4ZlwBcOGgnsi67JFRMQA_dE1lmANdPlDC1Uw1pg_7JmRxsK64JEMUJBtKn_fZPqWSeM5gopme6MEoJR_h6qMvw3ha8lqKVvqe2EK1frYRa5thZoOkH9tzl6eJsO3TS03pvJVbowAtI6timdu-3GI9JvbzRQ4T_EmVYAUpuR1NA_X01rgP45W6FRKrywzIaexSb0bPe4bh7jBZ2cAFmJz5v832Nr0iqaNHa4ylylc1jL-8ydmFulNASyo3__flbikTOQGnYslRUWtCmXubP_DMDHl6BG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرچ گوگل یک سرباز کشته شده اوکراینی: مذاکرات اوکراین و روسیه
🔴
مذاکرات زلنسکی
🔴
جنگ در تابستان به پایان می‌رسد؟
🔴
چه زمانی جنگ به پایان می‌رسد؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/125668" target="_blank">📅 08:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125667">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
کیهان: چرا از NPT خارج نمی‌شویم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/125667" target="_blank">📅 08:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125666">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxzqtlRJkFkL6ymhR7UJsh8Kcw-b54mOLkMtChrC4v--uRGr36ZWICNdKRtMMarrqOiOsINuoIXDF25OPPO7iNKSALsTL5qwx8W7WeWPMIxq9ZhWQdR9tGVnTwtusfQsWTV1Z0HOD-64knVFaZ51ITU7TqwuBmUAqxrxaAu1kgyKifWlE9SGICEv_caEGzWUMntghaedmZ7_s0dIOqoO43ZW8TxBcOp-Asz_UEDDMTrJv-CcMqO9SHrMRReZ0Yz4yuTBwGVaw7bAd4820kDz4pEAHY03PDC_lFsWJ0jVCv0OJf5Fg8MP4YqJp_z_WMmpzQw459EsqQ8jcCzHcMFs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارزش یک میلیون تومن وجه رایج مملکت از سال 97 تا کنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/125666" target="_blank">📅 07:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125665">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0rorRzdaghndyAbecL3S0VKYkbri2SHsqIjFEFwYpO0axg6GGrmCHrgQnEVJyxyGVsROrPCaD6409l3tG4YkPzkuamlomCZ1TXXOF4gw2uMT1aQ07z5A0ucU1QB6HOWhzon1QXj6QbBPZyWskz7o-hwcBlHy0w8LiRCeNqsdXIHEbvyG6O8zAvv4KsnhS3KR_DtE6TO8Bt1w5qM7ZlfQEZQQ1pm-ajUlGuxHPZbznFv5zA-1MAg8lMccicgpoNaZwa-K-3zWIz96pLi_B726j-UBCWL-3-R4gilX4sv2vXvupIggaT4lAazmNalmFnmi8syttxjRB_n9B5W47skiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای جدید نشان می‌دهد که انبار متعلق به شرکت فناوری انرژی آمریکایی بیکر هیوز در اربیل، کردستان عراق، کاملاً تخریب شده است.
🔴
این تأسیسات در جریان حمله پهپاد کامی‌کازه در اول آوریل هدف قرار گرفت و تصاویر نشان می‌دهد که ساختار آن به طور کامل نابود شده و هیچ اثری از انبار باقی نمانده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/125665" target="_blank">📅 07:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125664">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/voOe_XjOX6w_jkg-dNGADUzSG2dwSwknBT1fObzu20v5yCH3h1iPmX8ogY5bwWAmXGk8a1HYW9wcCqEXYX-FPskQFx5B6m_F2bhvcycn6hPo5CTsqs3lNc6m6Cr4ViHByx7fpf5t-TQPW_5ElMDeOrxDvtPGrmot-Krk2O5bBpPSFPait9f7QPCptDtpWzCkybkLECUZ7r78I2a_MChvobKb4RFmT8-Zr4HimwKuL3ZA1dkQ1b08JQM92Z7XAcB3i9SC9fGNYZ69XuFE8wiQEXfzj_JT-cQnEi1faowZKtwlDikV9_c6PKiDxTSAJv2C4NcvDETRtx34K8AwrvRk8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نامحدود فقط 90 تومن
😍
فقط ۵۰ نفر اول
❤️
✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 90 تومن
🏷️
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/125664" target="_blank">📅 01:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125663">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
پیش‌نویس یادداشت تفاهم ایران و آمریکا در اختیار نهادی در تهران قرار دارد تا در آن بررسی شود.
🔴
این پیش‌نویس برای اینکه بدون مشکل به سمت اعلام توافق پیش برود، به آرای اکثریت مطلق نیاز دارد.
🔴
ممکن است در اواسط هفته شاهد تحولاتی استثنایی باشیم؛ البته به شرطی که دولت آمریکا مانند دو هفته پیش که تشریفات اعلام توافق آماده بود، در لحظه آخر نظرش را تغییر ندهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/125663" target="_blank">📅 01:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125662">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip-D8AFEPrL9zHKbH8yoW39f8DO9ZqsOBzfBqWh93__x3F5SoyVfRP7rV6vUyyCZwuQ9BGi9P722aRzugGaQsGuu4-AsGyVbq-9OfuxziO3GFxo6GmCZPoX0vqx6O_sN75PkWMSDNCrJVWxS6ExDCdvvPAtC8eTaNQ6_5LB2ZZgp6wb2P6iOMqJ1FnVTL7xMZstZzK6I2Cuun1i_LINDYQCohva0ZclQZV1xdJnn0ZE1dsNW4S-tXaAQoh44G-cw2GMsTfrhEKxsl0FJsRe4OTXLbiPatuDLLfAio-CdyIjHhCEoscNpHB7_tbvUKHliLwHVGhrcl2ZHPWrJVKT2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنعانی: حاضریم تو زمین بمیریم اما پرچم جمهوری اسلامی بالا باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/125662" target="_blank">📅 01:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125661">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2ca304ca.mp4?token=hZEOnOB8zz5iJjfeuwizFn35DOHrRcX9xaQJ7-S2fP1DKAMeHRBvxKLJJNSkuBxK_qCS93K6j0Bzu48hhD-lnyHeN5nt5lBXTp46UbWdhh-0CsmFFs2Hum1uEZUmjVDKic4S01Hg6NTP-l9jljIXZv0kIHbsM21-1AC-nJxx19o8MsIZr-w6kEgtUnPlYV30rYrbmLM3tYemgPv3pyNmfjBjk6MF_B7voZXTVCLDGF0IBNb5rmCeha-1ODxknZgMO0dt9U9rrwRyPurCIbtINRaL_GGvu2nK9-OV7qMlLusS54W4zlgFDoDOhv-ZLXMCzVpaWgp2WbFDb681DONA8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2ca304ca.mp4?token=hZEOnOB8zz5iJjfeuwizFn35DOHrRcX9xaQJ7-S2fP1DKAMeHRBvxKLJJNSkuBxK_qCS93K6j0Bzu48hhD-lnyHeN5nt5lBXTp46UbWdhh-0CsmFFs2Hum1uEZUmjVDKic4S01Hg6NTP-l9jljIXZv0kIHbsM21-1AC-nJxx19o8MsIZr-w6kEgtUnPlYV30rYrbmLM3tYemgPv3pyNmfjBjk6MF_B7voZXTVCLDGF0IBNb5rmCeha-1ODxknZgMO0dt9U9rrwRyPurCIbtINRaL_GGvu2nK9-OV7qMlLusS54W4zlgFDoDOhv-ZLXMCzVpaWgp2WbFDb681DONA8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخوند، اسماعیل رمضانی : بالاخره یه جایی باید مشخص بشه تا کِی می‌خوایم مذاکره کنیم
و باید چه اتفاقی بیفتهِ که بعد بگیم دیگه مذاکره فایده‌ای نداره و ادامه نمی‌دیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/125661" target="_blank">📅 00:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125660">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Akg-yauBMAHgUJ3z74z4OZQ8Ely-DtPYxMviUWAM08eFVLo9JA9FMU5WPBYC3Mbx827_UrtUwUHcXsAL031-pgjVXD87iZhXcFK3s4IH_Qd6emypHJd8nHCwhSrFKQtTrSj5o8MAWT1BSRwZgVE1EdDkmkiQi9_DCfQKJcNmh3-rEO-9eC8HIVuz8HX2plCvZfKtCwbnOlGxw7jr_GDNza-ZUgl_YRI8gFI0iDr1DqZzMusjIb-fj30Gs8wBVdd3tZwue7rE5tcUoVvgnLSSYdCJuIqfeKlCXe8d-9M508XMjFxU_Ir7fOtY5AJu-Vdfkm8UdnYAyfJaDnESeUj5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
درپی درگیری میان پنج دوست صمیمی در ورامین بخاطر یک دختر، چهار نفر از آنها به قتل رسیدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/125660" target="_blank">📅 00:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125659">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo1ErrpJ-WcCHoqqnCMb9_R_TJ0kyA2vgWn7Di7AOHXXlx5-kfenVf-gfvWJjZ8KTg9L2Fc3O0EPLc407Om-VCdCu-FKcSGofHc3w0JcsoLERqas3HXvXefPQfjoXwSiVmVX1bx_-ft08Qpf6d-t9WqYuzkez-SSo-txUbm98dFYsiOPpyVt3U-651ZroCVW88wLuVKgr4iX1qYjDTBXdzJvyI19uosRfiMmcnUf2sWCbNLstRRjSFJmf_cpjlui2bM1mR-sk-2EOuHJJolwMk0c5e2n6P_E-RGHKygNAbzzwdV6PIfrt-I_awk8tVIhPklkJIAULQ-hprp19Q7kXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به انتشار پست های عجیب با هوش مصنوعی ادامه میدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/125659" target="_blank">📅 00:24 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
