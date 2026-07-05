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
<img src="https://cdn4.telesco.pe/file/JvI_Ll3TxU1S4dgjv-yKfbhgKeQ1kW4EJzo2BpOnaXOitQ22tF2S1qugbGUdO54sjjPIQ7qhph8JSPjGR0fL7Pzhd8RIRxhL_OEk6JixUToEWC0M-t8tHMOfM45Z-6kz0wcPApewsMJ8iOA7HB_cObaAOY_qe1Kycq_c6HbZEh861dncB0PWSuHULIDMw2mSQx7xOUiGQSuSJtahCwux5G5yS0_T4zM4PJr2sXnLFzyRyz_Rh1E1pXT0RUUzShMhgIACkWyBP2TLbrTlB1rp9QvYZFfSo245Qj9sIbBcqysWs5-H3P_I5IZwsfAa4CzFMCq3YlpavAxidq7zuq63sw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 339K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 14:06:16</div>
<hr>

<div class="tg-post" id="msg-16493">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کان نیوز : در اسرائیل معتقدند وقوع یک درگیری نظامی مجدد با ایران در آینده نزدیک وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/withyashar/16493" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16492">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4z_QOqhHVx5OJ8tU3cQSPwN44pxWEXg11BxhXjb4RBPIUuHMaIqWi2HyU7V-dfjIddaik98NMwmWJdghuNkJhfqK5c-LsA5DU-oXbdAunMeZL4fh7GSmzr5Yq-FKKE2QxNsChEoacoWAjvMax5pIJnc2uS-JVuFDUWdMW6Y5YY3ctTCu1zWDgIk3KFU2srb0gRglwg38bz1dLFomjLrt2R6NwGmWLPhWjj0tBDuIhFj7EagdgW4mFjleRmsus0LRt-KlLgoWpE9aYczhDE4ojUZTiF3CEDX_zWWkKqwWzixVXCGPuta7uBUCeASInItovmv0OrepBhtU97B5TZS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشت هواپیمای تهاجمی A-10C Thunderbolt II که در خدمت وینگ ۲۳ ارتش آمریکا هستند، از پایگاه هوایی RAF Lakenheath به پایگاه هوایی موفق سلتی در اردن اعزام شده‌اند @withyashar</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/withyashar/16492" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16491">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن   ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد @withyashar</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/withyashar/16491" target="_blank">📅 12:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16490">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCJYqEiDNqYsfV1W8EG4s3fW-sVqn9RAfPNG_m0NAIkqNfIFK05a9K_Xjxr8bUxSNGgQK0-O3QsXBA1A8paOpO9gR6ooUWOZWgQr5C6jObj4Q5mNcqerqaHU_tAXwyH7Tq2aAeiIFipm7Ej1MPi6p2gd0t-Th64RE3g8-6W_KKU6jr0MGb8WB95N8-4bi3OMuVvtA_2jKrrkQKrB9LXzfI9_JZVgZCfHSMRHxnojdKOltZ4eyjXi2wymDSoFs2OhSUAnaOVvWidgsyoeUbN9wpv-o6P83lWTzWeovuu1oNpqInR2UeIjmU_bFPvtBeHLvHJ21P_3l_ThHcS2rBJf8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/16490" target="_blank">📅 12:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16489">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کانال 15 اسرائیلی: جلسه فوق‌العاده کابینه سیاسی-امنیتی به روز سه‌شنبه موکول شد. انتظار می‌رود جلسه کوچکتر کابینه امشب برگزار شود.
@withyashar</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/16489" target="_blank">📅 12:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16488">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=ahs_AAG1AretrSeelRGTz7V_S_zlsCUCSt4ABA3zvcoo0QRXW2bhqneHX0CoVAxmGO-BI8gTYImfm98xlBXlTeJjyq34qR5nKzmFi09Damx8nqYcSp9_hzAxTHE2D5Iogk705Fg6dkiwSlEvQqIs1K1L3LPI1iigRwK3SwXCQMkAxXreprimL12zqh8D8ULgkS86uyhiUvXMdL7AyVIs5YJnOkL8FA9bxqY49bGrM2KYuoeXx2et4Pn64l0T6IruJOLaNe17MJWN-eXDAu-bDjWBlSPRsc6EF2sKfwHjjpBmRgzNLwFRFdneTEbGqJy3QRP7hfOCV3KIolI9bl3LgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=ahs_AAG1AretrSeelRGTz7V_S_zlsCUCSt4ABA3zvcoo0QRXW2bhqneHX0CoVAxmGO-BI8gTYImfm98xlBXlTeJjyq34qR5nKzmFi09Damx8nqYcSp9_hzAxTHE2D5Iogk705Fg6dkiwSlEvQqIs1K1L3LPI1iigRwK3SwXCQMkAxXreprimL12zqh8D8ULgkS86uyhiUvXMdL7AyVIs5YJnOkL8FA9bxqY49bGrM2KYuoeXx2et4Pn64l0T6IruJOLaNe17MJWN-eXDAu-bDjWBlSPRsc6EF2sKfwHjjpBmRgzNLwFRFdneTEbGqJy3QRP7hfOCV3KIolI9bl3LgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم ویدیویی از حضور احمد وحیدی در تشییع جنازه نشان دادن. به نظر میرسد در صحنه ای که کات میخورد بر‌اثر هجوم و درگیری‌ بادیگارد ها  کلاهش می افتد.
@withyashar</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/withyashar/16488" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16487">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارشی درباره یک حادثه تیراندازی در آمریکا
: طبق گزارش شبکه خبری ABC، حداقل هشت نفر، از جمله چهار کودک، در کونی آیلند، ایالت نیویورک، در جریان جشن‌های روز استقلال آمریکا مورد اصابت گلوله قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/withyashar/16487" target="_blank">📅 12:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16486">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
@withyashar</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/withyashar/16486" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16485">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37255614f1.mp4?token=NfzripWQvihxivf584_tnT4uLqtjU-bAu4vDyh6liHyrjSikQm2rdJfxzgeKs-lMvK00n14XJtZ310r8ghyIf2Zl336Vepwdl7g38EGGSh02xwLf-1LhuPNs2BEzZPOMw_7CvXtRYtxHBiwlDqyzhVtHaIIA7HgpabSbGYOcRshPKsdYwOzDXhd1ac69_fg4j5euYnAMqy7Z4B0QcRusQ-RyjthBRAvqbB_RSs5-EBwDeqhX_kI46dzQzjBBJRooYZB9o3-VDjUnV7PxbLsLWp1w-niW9H98D9y3ixDB7mM9ObNBBRZi0GJkbIvdzq6faeeDfq0ZNSx-aHqU4P0mUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37255614f1.mp4?token=NfzripWQvihxivf584_tnT4uLqtjU-bAu4vDyh6liHyrjSikQm2rdJfxzgeKs-lMvK00n14XJtZ310r8ghyIf2Zl336Vepwdl7g38EGGSh02xwLf-1LhuPNs2BEzZPOMw_7CvXtRYtxHBiwlDqyzhVtHaIIA7HgpabSbGYOcRshPKsdYwOzDXhd1ac69_fg4j5euYnAMqy7Z4B0QcRusQ-RyjthBRAvqbB_RSs5-EBwDeqhX_kI46dzQzjBBJRooYZB9o3-VDjUnV7PxbLsLWp1w-niW9H98D9y3ixDB7mM9ObNBBRZi0GJkbIvdzq6faeeDfq0ZNSx-aHqU4P0mUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن
ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/withyashar/16485" target="_blank">📅 11:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16484">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnz0GLPHbMKB86Q2SN8KQCUjIndu5eNbZiBL98KJxHy5464fKpyJtmK9SmlgLOdi8qLWrfILpBCQsl4Gb8UPLo1bXrin4CYFqnogdlbRu--GSPoqxYn44KNchSFCO3NBARCbXJeT2GV0KZX3UY4gXPUlcBZV2fOlqZqfQCmobfzvozs2FTXalx-zsmYzo3jF4eYqRPG_Pah3osDm3kZCXc_XQX14Jd6rKv8bqddXWHF3ogL4G_zcf_wnf3kWl7Y6c2l2xm-ZhMSf7TydpR_8xIUbrvOQRBFYbIUf1B_xMSLlLKtX5om8d_xb31oHFr0P4xGbIl1392OrTWC3MHhY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون با پوشش هوایی و اسکورت سنگین، ارتش ایالات متحده یک کشتی باری (با AIS روشن) را از مسیر عمانی عبور می‌دهد!
این اولین عبور امروز خواهد بود اگر موفقیت آمیز باشد.
@withyashar</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/16484" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16483">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قایق‌های تندرو سپاه، مسیر عمانی را بستند
هرمزلتر: نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده.
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/16483" target="_blank">📅 11:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16482">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده. @withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/16482" target="_blank">📅 11:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16481">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فرمانده نیروی قدس، اسماعیل قاآنی، و فرمانده سپاه پاسداران انقلاب اسلامی، احمد وحیدی، هم امروز در مراسم تشییع جنازه خامنه‌ای حضور داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/16481" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16480">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سخنگوی ارتش ایران: از فرصت آتش‌بس برای تقویت توانایی‌های نظامی خود استفاده می‌کنیم و لحظه‌ای را برای این کار از دست نمی‌دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/16480" target="_blank">📅 11:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16479">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قطر: فعالیت‌های کشتیرانی به‌طور کامل و فوری از سر گرفته شد.
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/16479" target="_blank">📅 11:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16478">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وال استریت ژورنال: ایران، روسیه و کره شمالی، در نحوه تعامل با بازار ارز‌های دیجیتال، ایجاد رمزارز‌های اختصاصی خود و پلتفرم‌های معاملاتی برای دور زدن تحریم‌ها، بسیار پیشرفته‌تر شده‌اند
تهران و مسکو از ارز‌های دیجیتال برای خرید پهپاد و قطعات یدکی تسلیحات استفاده می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/16478" target="_blank">📅 11:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16477">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی @withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/16477" target="_blank">📅 10:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16476">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نیویورک تایمز: مجتبی خامنه‌ای همچنان در تلاش است تا در تشییع پدرش شرکت کند اما مقامات امنیتی مانع هستند
@withyashar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/16476" target="_blank">📅 10:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16475">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al6sXC9B4PfREbmxLZGJ-svr9Bm-H30mGWCGGR4jCejZmbciDebC38ljYt_2rWUgffI8kSeOhjUSyM2HnMOV6NaImbf6GIpDA87Ze1Qn5nSmFc0PPHOIguBHULi04FqNFS6c4xvemM4VInNFEay_daRx4Cmz-3wGw4By3r0Ld4bK3yJ13IwmQ-JeidEwi9a5xWeZ2kFX9VIeTdP0jlNAa0Y8oP-yQV81rXTDsUlWXZ0T9P2tWZGC8jopDWQdvwRufnWFlFzrfO3Uml7fgpn3vxnidBqCULvLIHQUgImNfDwGNWb_2x88kMMvkd2vyy0G-1KsG3_64lImgGPNFw87Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شباهت امام جمعه پاوه ( ماموستا قادری ) با ( هاشمی رفسنجانی ) که دایرکت منو منفجر کرد
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/16475" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16474">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV9N-bQbqishj43Z1vm96NsFvEnRCD139Wj63JfrVplB6n_TkaX3IcpBZa0FCE-CZDKAaTFcoHPNYmqheA-KqT5dMNInf1CyQKOUe5jIHcjkmb0uILOh9uUUeSNHO5kNxmPrKfZIyU-upRTfqHnwJCdLmB9ItmxBKk0Qn9crQYwwNa1JN-c36WvXJ3Z3E3AaTHwRi6gMvUkr10M5zvBfaIgwtbQL4JLxwG_nSsjqIE6tv7BxprBQ7vauCgrbHTVpH_2lWjmeHe9a8oQP_1t3tXj0YnZs1hBaebc0gVAN8ZyfQ22PBU9DymYE7KG4BeimTjBBQbJ04UMImJMho_mmBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/16474" target="_blank">📅 10:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16473">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=KHP04yA3iH0J8QRL08iwDK57lm-6n-ScnKHql6NaV8QAKu9OCCUS-LD-4UZJ4qlNAMRiBNvPAODNq4wZ9hlp-EUy1_C_AEJO1kvYH-s3AhA2DZAjtB33mFL7jL2IWWPu-t2lD5P35jrGLOwawOoonL1vMBUbDBlTfxdg78b5dQ7YopaELU4nxHz8SG5Rlx61M_75iE9mJwAm2uzLLL4ZspzJej1KnIH52uk0a2WphjuBV8reDNR4NaWRuHfBJ_z_ouyODJmY6bfDixw2PCYROAt0rRcKSSQwvJe5hcDhtWGi_VgwoPg6op57S9WeQ8u5QUSu81sEuzHRSH8JH0MoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=KHP04yA3iH0J8QRL08iwDK57lm-6n-ScnKHql6NaV8QAKu9OCCUS-LD-4UZJ4qlNAMRiBNvPAODNq4wZ9hlp-EUy1_C_AEJO1kvYH-s3AhA2DZAjtB33mFL7jL2IWWPu-t2lD5P35jrGLOwawOoonL1vMBUbDBlTfxdg78b5dQ7YopaELU4nxHz8SG5Rlx61M_75iE9mJwAm2uzLLL4ZspzJej1KnIH52uk0a2WphjuBV8reDNR4NaWRuHfBJ_z_ouyODJmY6bfDixw2PCYROAt0rRcKSSQwvJe5hcDhtWGi_VgwoPg6op57S9WeQ8u5QUSu81sEuzHRSH8JH0MoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی
@withyashar</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/16473" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16472">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/16472" target="_blank">📅 10:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16471">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c290e0d.mp4?token=Oe_Rxi593GLPprcWRpVv0Y4_3VtiKJDL4jNcYX2egMrFmkUAdy8QP7ZudNO211kB_froovaoDqQofdGmQJM-GyyrTHW08voMIfkz8bE5g5u9U18h0zC6LRAl1dTI_vwIzY0oMMzU0wsdGr2dUxxiSrXpkkkaIidNN-PE2p1QZYGhsfABwW55I2JVSkL8PnpMwG41sP3XWEIYXV1FOO8Q4XRB7u3IBdZnpCCWMZMuL2rVoNj_sVUXnA2otuBH4An6wonVGsexSSY6TzYiIdnvzevplZyw7fXkArWGyl7-2u6cCHjpVEitsbQfzu5slBt1HM_udxNm-o9ctFMMLgtIgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c290e0d.mp4?token=Oe_Rxi593GLPprcWRpVv0Y4_3VtiKJDL4jNcYX2egMrFmkUAdy8QP7ZudNO211kB_froovaoDqQofdGmQJM-GyyrTHW08voMIfkz8bE5g5u9U18h0zC6LRAl1dTI_vwIzY0oMMzU0wsdGr2dUxxiSrXpkkkaIidNN-PE2p1QZYGhsfABwW55I2JVSkL8PnpMwG41sP3XWEIYXV1FOO8Q4XRB7u3IBdZnpCCWMZMuL2rVoNj_sVUXnA2otuBH4An6wonVGsexSSY6TzYiIdnvzevplZyw7fXkArWGyl7-2u6cCHjpVEitsbQfzu5slBt1HM_udxNm-o9ctFMMLgtIgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین.
مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است!
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/16471" target="_blank">📅 10:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16468">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uik-_fd8AiqJefXtWIA_TebJyD4D3F3Rs_yYj2wtbsfcRu1Poxg1IupLzl9u0SPQJe557otqv7OrWYS7hjBD3rCIwG0TYVLVmk8Wt5tnqvNtUkrgqwcGF9-D8saRaTUODl08DqubtgsO3haKuodKa0y3FSenGgWhQhplirzcYkX2EeJjDOsWPLHpmD0S-k8WL5ol8IlfzH9EI3sV-Wo515XfZOc1JpewHZE7Ej-hh_Xpi-gcwuvSz_ShO5mEgsy4A_NBO-a-KC3m6hxzL_4Tjusrp9AYYBH0QCOKwcRZ66IyRSwWE1J-L9OJy-QJoLXkIb7V5ZeYu6iAPxeCSpHSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtS7f0xCMhwGBiWbw1NP3dJhdGKO6TuPu5ZRYdN0dgslWFYwc7t13fVYRFbnsjjhQkXfYQlXXaDkS4al40fucKMeMPDV9ZYf9TXbNcbAvJpw48TV_WNeDF4heVb4ILuVv1pCbDeSGsH8oscOwAS8QBVhTqZ5R8oeAiimb37GC4bTI_eqLoCFt7mGwxyCPJ39LjJ0JUXh9l0veeR_EU8McFuYgJJKEyZcB5xmrLA4KgjbYJKqM849zvaGVJkB3p1MVGnR4-oyvQtDKdi20fbGTT1kgzUBQi6ks5HZ1RkZArvmD_isHA_ipu-BoxXkPB7sgZWzP4SC9TR_HRKZCCQoFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jyukUg0DzChXJwq4r6qb0_TXewARlwQQ3uT5dpxSB9Q1hTWl3LN0n5t4RrFzG2IpyZen3AsyqZnOma-c7u3xYOmDmjrtN30YgyjcA7MYL98IPtF9LOro2vyUf6HUi8BGg6u6vrBmkeX9jnZ8xJE1r681-ZfHBzgjvl3QLiv-1_GBNmKyL0oRG9mYaSiivZihtWuO0wvV6BoEtLm4KSbheuCviqytNNoPSMJsNv08uRpEQEkXHC3PL-eHV5VneqWhufgVFpYelea4mWfDbXbCp8WLHqckzZqHdJj452yFUvGBGq1QoRbVjt31TccszVZgaNyeJd6SPdmmkqCmsiws2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شهستان پهلوی (ویس قبل رو گوش کنید)
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/16468" target="_blank">📅 00:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16467">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شَهِستان پهلوی، نام یک مجموعه بزرگ شهری در زمین‌های منطقه عباس‌آباد تهران بود که اجرای آن در سال ۱۳۵۴ در زمان محمدرضا پهلوی شروع شد ولی در طرح آمایش سرزمین ۱۳۵۴ ستیران آرمان‌گرایانه اما ناپایدار و مخاطره‌آمیز برای توسعه کشور و شهر تهران قلمداد شد و با وقوع انقلاب ۱۳۵۷ ایران هیچ‌گاه بطور کامل اجرایی نشد. بخشی از این طرح احداث یک برج مخابراتی مانند برج میلاد امروزی بود
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16467" target="_blank">📅 00:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16466">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارشهایی از فعالیت پدافند پرند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16466" target="_blank">📅 00:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16465">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال 15 تلویزیون اسرائیل: در‌تماس‌ امروز دونالد ترامپ از بنیامین نتانیاهو خواست اوضاع لبنان را متشنج نکند.
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/16465" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16464">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ارسالی : یاشار جان درود
داداش همین الان از اطراف مصلا برگشتم ، تمام حجم ترافیک و شلوغی برای صف های ایستگاه صلواتی ها و مفت خوری ها بود
یجا مردم بخاطر یدونه تخم مرغ آبپز و یدونه لواش داشتن همدیگرو میزدن همشونم طرفدار اینا
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16464" target="_blank">📅 23:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16463">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اکونومیست: جنگ بعدی خاورمیانه بین اسرائیل و ترکیه است
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/16463" target="_blank">📅 22:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16462">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ در تروث : اروپا دارد یاد می‌گیرد که وقتی مجرمان جهان سومی را در خود جای می‌دهد، خودش تبدیل به یک کشور جهان سومی می‌شود. این اتفاق خیلی سریع می‌افتد، فقط در یک چشم به هم زدن. من درست به موقع انتخاب شدم!!!
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/16462" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16461">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فردا عصر کابینه امنیتی اسرائیل یک نشست
ویژه برگزار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/16461" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16460">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رئیس‌جمهور عراق:
عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/16460" target="_blank">📅 21:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16459">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو ۲۵۰ سالگی استقلال آمریکا را به ترامپ تبریک گفت و گفت:
«ممکن است ما در قاره‌های مختلف زندگی کنیم، اما به دلیل سرنوشت مشترکمان، به شدت به هم متصل هستیم. آمریکا بزرگترین نیروی آزادی‌خواهی بوده است که جهان مدرن به خود دیده است. اسرائیل مفتخر است که در کنار آن بایستد. زیرا اتحاد ما نه تنها بر اساس منافع مشترک، بلکه بر اساس ارزش‌های مشترک بنا شده است. امروز، این ارزش‌ها مورد حمله قرار گرفته‌اند. مستبدانی که با آنها روبرو هستیم، شعار مرگ بر آمریکا، مرگ بر اسرائیل سر می‌دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/16459" target="_blank">📅 21:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16458">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Bitcoin +63,100
🆙
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16458" target="_blank">📅 21:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16457">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش انفجار شدید در سلیمانیه عراق
@withyashar
🚨</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16457" target="_blank">📅 20:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16456">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">العربیه : ارتش اسرائیل شنبه 13 تیر با انجام چهار عملیات جداگانه، اقدام به تخریب گسترده خانه‌ها و مجتمع‌های مسکونی در مناطق شرقی و شمال شرقی شهر خان‌یونس کرد.
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/16456" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16455">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده  - ممکنه همین هفتهٔ آینده این دیدار انجام بشه @withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16455" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16454">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ به آکسیوس : ایرانی‌ها برای امضای توافق تقلا می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16454" target="_blank">📅 20:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16453">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده
- ممکنه همین هفتهٔ آینده این دیدار انجام بشه
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/16453" target="_blank">📅 20:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16452">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ به اکسیوس : "از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند."
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16452" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16451">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ به آکسیوس : هیچ یک از طرفین در طول مراسم تشییع خامنه‌ای، به سمت دیگری شلیک نخواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16451" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16450">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ به آکسیوس:«همه آن‌ها آنجا هستند. یک گلوله می‌توانیم همه آن‌ها را از بین ببریم ، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/16450" target="_blank">📅 20:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16449">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای برگزار خواهد شد @withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16449" target="_blank">📅 20:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16448">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECYQWsnKOg39QdR02Vcrlx-THOJQBZH_jGLpmWJtmN8fhdeFVJwZLAG0xBGpTOygYSKOKppbwUyGugMKFV6qFavyWaGxthRxmoWMhH_3jVQuszx-M-4IPv0mQAj7hv9ayik3jLXFZXPLgdBdZf1OsbytYxaVyM7DxJgTKPvwAHu_2TdyGTiMaJT0o88wvpYX_BKyu3haSiEeB5Lf4KReiS6TJ06cvQFq1xQBWEym3JPg_krQCPEyaAHaVqft11zRI-oIrugeUF47urzfXiawimWspSSEWITKLBuqQiHHYXqRkf0TF2a5-AquKCtkwMQLn6yBHJwoDW_1NMiuORkeEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای…..
@withyashar
😂</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16448" target="_blank">📅 20:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16447">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpqo12KZyatO0I65kIkNvy3zxBAvkWcbQ3tGZZIYxywVy08PaX_-5ctX8a1eKf45KnkOv_EFLQIOvNrEZmVX-x0NGWJ6o3V0qgMST-4BYN9XegYUeOf3kp3kKuOfs8WRXBYh_I5anXJeOPwvGekc_CCK6D8kyIvZrwoAat2Ylc7yFajDXXlwgpUb0UDqd970l4WDDgcWen7Scy-NuCqWFyLEymsVoy2lh7GGSnbFswv5tN5_i0kl9DtWIv8wVfA2SFMnRVHr4pFQVPcmSR4RBfCRa730hGFdXsEsezuqcq3MWwy_wlyai0eV-zTGq6rBCZnQF77Wdg0LOu-xgAvdMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد جهانی علی خامنه ای
بیشترین فاصله زمان مرگ تا زمان خاکسپاری رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که علی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ ثبت کرد
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16447" target="_blank">📅 19:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16446">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است. از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد…</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/16446" target="_blank">📅 18:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16445">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند. @withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16445" target="_blank">📅 18:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16444">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BI79iH0CEeVcuINGWSq1BS0-8xttIhNwvBBl4CRLZtgDIJRZ7_eU6bBKaRsNEOdAWi-P_iYzNW5bcDbGnNbCZ21BsKgFpR7A_X0MNUa5XmVI9JDu-5FXDZRThJRY4nYTCm6iLOxWu8xcz38T7LgDVIYeFuqqGj-1BtIVgGJK9q2iof5tiPW1tlHvlF5O3EqI18t82c0SB9tdKPe7cNPLM9UPIVDQK3oc6TUbp2K9nGdhlZNrBl2Lwg0pOswfEdaw-OIhzCM3Pc9vS1p2V4dT4fgIm3RQyILZKyci4CJDHORxKZkfer-XA-F_C_ggFZmCL5gq8yisqGEzgdhZ8_BK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشریه نظامی «میلیتاری واچ» نوشت: کارخانه هواپیماسازی کومسومولسک-نا-آمور روسیه
تولید ۲۰ فروند جنگنده سوخو-۳۵ سفارش داده‌شده توسط نیروی هوایی ایران را به پایان رسانده است.
وزارت دفاع ایران در حال حاضر هزینه نگهداری و پشتیبانی این جنگنده‌ها را در داخل روسیه پرداخت می‌کند تا پیش از انتقال به ایران، در روسیه نگهداری شوند
احتمال دارد نخستین سوخو-۳۵ها از پایان سال ۲۰۲۶ وارد ایران شوند؛ آسیب‌دیدگی زیرساخت‌های پایگاه هوایی همدان یکی از عوامل اصلی تأخیر در انتقال است.
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/16444" target="_blank">📅 18:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16443">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای برگزار خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/16443" target="_blank">📅 17:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16442">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نیویورک‌تایمز به نقل از منابعی در سپاه:
مجتبی خامنه‌ای خواهان حضور در مراسم خاکسپاری پدرش در مشهد و اقامه نماز میته، اما مقام‌های امنیتی تاکنون با این درخواست مخالفت کردن.
به گفته این منابع، نگرانی از احتمال سوءاستفاده اسرائیل برای ترور یا شناسایی محل اختفای اون، دلیل این مخالفته.
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/16442" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16441">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvyzjL90RShjAPUed361_6Xdt2kUyxt-JAWQP60q0rEPRjvFB5PeTD7UVV3lfCdioCAL2ErJSuu0nYr2m9FMZRWaYXzyGS6J6FYHHgLOIEKk05egvohicny2fc8fQFbrT6UVQzc36kIEeJLZ0_Px3vJXwF9ublilXBqW3vlf_yl-Ceo2BGLqqfAKJDR-pKC6g9tta2j6rF9tGK23C9oOYz1ODdeQ80C-BHJhEs4I-Tx3jEougVl2w11j0tAKgQxvPH4CJhmlYsvsxQVQ22Oe_jiZdbeO9RWaMho4jF0pTlGr9pUDMREtbXzyGAVznlImU9CoZMh4UOMuuIEPhPfavw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار علی عظمایی امروز به عنوان فرمانده جدید نیروی دریایی سپاه معرفی شد.
فرمانده قبلی سردار تنگسیری بود که توی جنگ کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/16441" target="_blank">📅 15:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16440">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نیویورک‌تایمز:  عبدالناصر همتی به مجتبی اطلاع داد که در صورت تداوم محاصره دریایی، ذخایر مواد غذایی و دارویی تا پایان ماه اوت به اتمام خواهد رسید.
@withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/16440" target="_blank">📅 15:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16439">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=EHyEmEY75bUKbheAotGMaSOIkYwjjpSP8U6Sq3oFut9OycEzQ35H3Ed0UPnnNMbD5BLu5Vgg6LL7SbvgZHvfcxCAuWIivw3Gs_mfWAUoWSAnS4lAcTbpxBWK4ZiXORYV1KcZqMweTRdYW5T1PxFqWVJ37HldKYSOT4ma0sybuw3YV7Ms_sZmKn2CT_nzqvnJJRR3msjtC_gfABPOyViyEtDRgGxQRQwUBE7r3V5MEXiXwUeANIPqrUDjMjdqAb1H2ADpGBnfS1nO3zYrXc2H2OSEHPKDVR2C_I-lCm-qTRPXfuTaUIoWVmeuT9-BrZWa2fo72ImP_KavCwAEbrEzkIG0cWY0evpTKWb2dTfGIuyS3SH3nzlVNXfHuNRwAqFIsXg-OxdxSfOFt5XdBJKLmhrf-zi4E472syxjXnLntSCPFz3OLqs-KxqF_HRDf_eKbQrgfpnWHgvbJCxLiiiaY_82Y11z5i6epaLRGaF1yHZe6NGlVO29aEyDJeaJeYLwa1XJfWgAEuawp8qJkdz5wjKaqu4l6YcOrwg48dnIZ419svmqP4RP2NYE1vrCi3y4l9xSIJHsJMMWJJBwADOVE2PzWIDELtcmAJ4cDgyyK8qpsNNLrJfYC-VDUZtCkkGLaTH0OK0rdNUaNrNK9FC2yX3f-PdoB7qYPsTm36qzqpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=EHyEmEY75bUKbheAotGMaSOIkYwjjpSP8U6Sq3oFut9OycEzQ35H3Ed0UPnnNMbD5BLu5Vgg6LL7SbvgZHvfcxCAuWIivw3Gs_mfWAUoWSAnS4lAcTbpxBWK4ZiXORYV1KcZqMweTRdYW5T1PxFqWVJ37HldKYSOT4ma0sybuw3YV7Ms_sZmKn2CT_nzqvnJJRR3msjtC_gfABPOyViyEtDRgGxQRQwUBE7r3V5MEXiXwUeANIPqrUDjMjdqAb1H2ADpGBnfS1nO3zYrXc2H2OSEHPKDVR2C_I-lCm-qTRPXfuTaUIoWVmeuT9-BrZWa2fo72ImP_KavCwAEbrEzkIG0cWY0evpTKWb2dTfGIuyS3SH3nzlVNXfHuNRwAqFIsXg-OxdxSfOFt5XdBJKLmhrf-zi4E472syxjXnLntSCPFz3OLqs-KxqF_HRDf_eKbQrgfpnWHgvbJCxLiiiaY_82Y11z5i6epaLRGaF1yHZe6NGlVO29aEyDJeaJeYLwa1XJfWgAEuawp8qJkdz5wjKaqu4l6YcOrwg48dnIZ419svmqP4RP2NYE1vrCi3y4l9xSIJHsJMMWJJBwADOVE2PzWIDELtcmAJ4cDgyyK8qpsNNLrJfYC-VDUZtCkkGLaTH0OK0rdNUaNrNK9FC2yX3f-PdoB7qYPsTm36qzqpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت نیکسون در ‌تهران ۱۹۷۲
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/16439" target="_blank">📅 14:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16438">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ3J4MmOsYHNij8yXIUSRH1z48-zbcRhdc_3p3jY67FzPZI7i-T9VShMIGZOYtASYHwsqNZAh8k9dd7OMO_yVZ8us8gBUNq6MpOhsENASt24ylNZcFE7ZEphvwp0AkYfa6Se62BxTG7Ic91KvX6uVC7UatnaWSHT8PR_A8FefDK04mouVgIHZfJJlD_kBPzSY2teulLagCALpVjegoRQvN3_rMz6_bRPhkzXdVYQSU9t7G0nQzsrc3cVfi6w2GweRy_Woop4AKdo0pa_4imuidq-vrhtdZUJ6tOwAW0g99DDe_vH3X4CKiXWTTL7dORUKViTpRbj7Qjx6nIRp9iRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند.
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/16438" target="_blank">📅 13:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16437">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwHQSmVL_1P4J3a_TNxBvFczD4SLnV3dJoqwvIg9T6chPRDUGOT7mj5l3R6sqi0B5hWEdbqj3KFCTs4coHv0maMSwQ3f8GiNpZoICnd-CqEL8i3TEpmMiaikMQByAeRxhsvdptPET3rs7BUOP5kmGUO4zlnimhFYTnlIagU4t2mfNO0LfP6S7SRda678X0EzWiFYU6caycBcyZJnvdCkchV75pM3rNmRR4vIzkgnRzqyE63hj5W-Z9xTDq398Nz44PG6ExqNZhmdmwp-i3tlD9Zy0x-PEdSP1RMNAJ7-asjAf0R4J3jcvyclNm9mEfJJKFrzP6Xc7CrP8hYoLdvgvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان درست شد ، عباس مکار و ممباقر نره
@withyashar
😂</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16437" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16436">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjCG6GI3F2rJ8WMyUTKG5-WSAlAWet9FdXyJIGUmLRBk4IQlKxngvThN44dmgFltgg7uHiYojbZr-e4lpNB8xr97ddp1TniEZYFhzcA-2lAuWCZzsgdylUcpkqX7p7WA-YVyTx9qVpkZfAhueEnBtkZpPkrbiqXy2d-cUGpZlpYyD1PKPaCe2GmNv5JBdwDWB-Tlt4QA7AxbnBcs3RFSUSt1UriOOox-4wqnNfkBZOZytg84VC8h5QuFNpj8gmCfUPsX-UvtcbydqjPVGGXdwMDjIhtQso372wm_nxZlHpLHZkqC8GEdEiy03zgN2gyaKK_jnUD8Nw0Gy73dcN8Kgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره حمله اسرائیل به لبنان
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/16436" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16435">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gkf1iquAIZmBxQeLshSp8rk-pUv8k_EHpnwMAJTfiBKgH7GwkNUX7MyonkIRdQB7zvQ_JLc_SZ3dP3MyoZQ13rToC1d0UOKoYb5oITBfdG6ClLAh5Kx5CgTxUW1gj4IUU4VEuq1VnEQj6bKOugNYBoLir1DYglJDE3HyqEsbnJ8ofSPFPg6Aj0SX4NxRKCAV0_s4HCYHS82GlQjOjTPIW9LynWN2jPoO6FDUh8OkimeH8ijed0BqST19GXoP3806PD82bpYlzeQwVcqODU53RAH1rDasBJ9WIT1knKGC3wkk668TAqCuaCGpsDSN2wkfOgD9WJgPRI87lthKmIaX3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : سری جدید ۱٠٠ دلاری با امضای ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/16435" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16434">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">افزایش تولید نفت اوپک با بازگشایی تنگه هرمز
طبق یافته‌های نظرسنجی بلومبرگ، تولید نفت خام اوپک طی ماه میلادی گذشته با ازسرگیری صادرات تولیدکنندگان خلیج فارس از طریق تنگه هرمز در بحبوحه تفاهم‌نامه ایران و آمریکا، افزایش یافت.
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/16434" target="_blank">📅 11:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16433">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ان‌بی‌سی نیوز به نقل از چند منبع آگاه:
آیت الله سید مجتبی خامنه‌ای احتمالا در مراسم خاکسپاری آیت الله علی خامنه‌ای حضور نخواهد داشت، چون در حمله آغاز جنگ به‌شدت مجروح و چندین بار تحت عمل جراحی قرار گرفته!
@withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/16433" target="_blank">📅 11:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16432">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانال ۱۴ اسرائیل : حسام حسن، سرمربی تیم ملی مصر که اولین پیروزی تاریخ این تیم را در مرحله حذفی کسب کرد و به مرحله یک‌هشتم نهایی جام جهانی 2026 صعود کرد (در مقابل آرژانتین)، از این فرصت برای ابراز اعتراض سیاسی استفاده کرد و پیروزی را به مردم نوار غزه تقدیم کرد: "امیدوارم خداوند پیروزی را به آنها عطا کند."
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/16432" target="_blank">📅 11:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16431">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیکلاس لیساک فعال رسانه‌ای نوشت:
"یک منبع موثق می‌گوید مجتبی خامنه‌ای در اواخر ماه مارس، پس از آنکه بر اثر جراحات ناشی از حمله هوایی‌ای که پدرش را کشت به کما رفت، جان باخت.
او هرگز نفهمید که رهبر جمهوری اسلامی شده است.
قالیباف و سپاه اکنون در جست‌وجوی افرادی با شباهت ظاهری (بدل) هستند تا آن‌ها را در انظار عمومی به‌کار گیرند."
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16431" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16430">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">منابع اسرائیلی به «کانال 15»اسرائیل اطلاع دادند بنیامین نتانیاهو، در انتظار چراغ سبز ترامپ، برای تصرف پایگاه «حزب‌الله» در ارتفاعات منطقه «علی الطاهر» در جنوب لبنان است.ترامپ از نتانیاهو خواسته تا زمانی که مذاکرات با ایران ادامه دارد، این عملیات را به تعویق بیندازد. برآورد ارتش اسرائیل، بین 30 تا 40 نفر از نیروهای یگان «بدر» وابسته به حزب‌الله، از جمله شماری از فرماندهان این گروه، در داخل این پایگاه گرفتار شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/16430" target="_blank">📅 10:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16429">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سی‌ان‌ان‌ به نقل از مقام‌های آمریکایی:
مقامات دولت ترامپ از نزدیک شبکه جاسوسی اسرائیل که در ماه‌های اخیر، فعالیت‌های اطلاعاتی و جاسوسی خود علیه ایران و آمریکا را افزایش داده، زیر نظر داشته‌اند
مسئولان آمریکایی تلاش کردند به ایران درباره این نگرانی که اسرائیل ممکن است قالیباف و عراقچی را ترور کند، هشدار دهند
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/16429" target="_blank">📅 10:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16428">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حضور هادی خامنه ای (برادر کوچکتر سید علی) و وحیدی در‌ مراسم @withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16428" target="_blank">📅 10:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16427">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=CTEENUM1JrwMqKshcTfb7DmRw_gs_7GxrwGRq_5RJglzjeDHdV50O8c5a5mm0XuB_lPqbhkZrW8vPW2SVv2uJAPGWbaQB7UY4etda0Cm31jga3i4nMF3swICIIDh8WR9KPkNpi8AnxKQ0fHx9LM3ScD6SI0Lrtj12lvbiXdSfDVNGt2DXHnFnqq-n3v3Xl0eClUd-3IuPKPqTEutxq8fP3ijIz00jbV-LTT60hwZ5Wg8YxfY5Xpp6I8Knwro0abmVW0MxmliU9_cpdjM2iOmYW_ml3NdkHrKpb_B24HzGSY7QyogtVfVIWRraOLp693YUOVyKz8YAUi-xctidjk_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=CTEENUM1JrwMqKshcTfb7DmRw_gs_7GxrwGRq_5RJglzjeDHdV50O8c5a5mm0XuB_lPqbhkZrW8vPW2SVv2uJAPGWbaQB7UY4etda0Cm31jga3i4nMF3swICIIDh8WR9KPkNpi8AnxKQ0fHx9LM3ScD6SI0Lrtj12lvbiXdSfDVNGt2DXHnFnqq-n3v3Xl0eClUd-3IuPKPqTEutxq8fP3ijIz00jbV-LTT60hwZ5Wg8YxfY5Xpp6I8Knwro0abmVW0MxmliU9_cpdjM2iOmYW_ml3NdkHrKpb_B24HzGSY7QyogtVfVIWRraOLp693YUOVyKz8YAUi-xctidjk_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارزانی، رئیس اقلیم کردستان عراق، با قالیباف دیدار کرد  @withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/16427" target="_blank">📅 10:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16426">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت. @withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/16426" target="_blank">📅 09:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16425">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانال ۱۲ اسرائیل : مقام‌های اسرائیل ارزیابی می‌کنند که طی ۲ تا ۳ ماه آینده، احتمالاً تا سپتامبر، «هیئت صلح» ممکن است حماس را ناقض توافق غزه اعلام کند.
چنین اقدامی می‌تواند به اسرائیل آزادی عمل بیشتری برای فعالیت در مناطق تحت کنترل حماس بدهد و به‌طور بالقوه به ازسرگیری درگیری‌ها منجر شود.
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16425" target="_blank">📅 09:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16424">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=fFaI8AtjFM4GboXWVBXl3vK9HgRvKDc19OCUgJoBAzVdbUEl1xBf4IMCK2aEw6Z3WhM-VPLuvamyfcGIgC_HnrL5GossbKUq1oXfb807C7qntLm-eNWZXdcyJj5FZvVGwRWNPBqf918tyr_nxOIDnl_2OTCDMAat8TMp1VKdHsGdaiDS_e-53SVR6u_hUcYGdipBqdxtwuv0MpoIK6lUtFp_FO6EnfGiTLOGOp1OSyDtC-nZRxho-EnpD2dPb6YrRfOTBJD-dK8bOv9yA-bvKmYLTGlgR-yPIFzA7nd7NMI9Wk-zeO-33ILD3Rm9fxbjdLoZNrCtD6kY9Bu0XwQyCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=fFaI8AtjFM4GboXWVBXl3vK9HgRvKDc19OCUgJoBAzVdbUEl1xBf4IMCK2aEw6Z3WhM-VPLuvamyfcGIgC_HnrL5GossbKUq1oXfb807C7qntLm-eNWZXdcyJj5FZvVGwRWNPBqf918tyr_nxOIDnl_2OTCDMAat8TMp1VKdHsGdaiDS_e-53SVR6u_hUcYGdipBqdxtwuv0MpoIK6lUtFp_FO6EnfGiTLOGOp1OSyDtC-nZRxho-EnpD2dPb6YrRfOTBJD-dK8bOv9yA-bvKmYLTGlgR-yPIFzA7nd7NMI9Wk-zeO-33ILD3Rm9fxbjdLoZNrCtD6kY9Bu0XwQyCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما ضربه مهلکی به ایران زدیم. آن‌ها مشتاق به حل و فصل [مشکلات] هستند. آن‌ها واقعاً می‌خواهند این موضوع را به پایان برسانند.
ما به آن‌ها یک هفته فرصت دادیم تا مراسم تدفین برگزار کنند، زیرا ما مهربان هستیم. این حقیقت دارد
@withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/16424" target="_blank">📅 09:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16423">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16423" target="_blank">📅 03:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16422">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16422" target="_blank">📅 03:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16419">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">@withyashar
🪓</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16419" target="_blank">📅 01:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16418">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljFhwUImI5hZuronkpVeVWx_7muh1Kh8tcDXMKEb4y-slU7w7Teus8U3WUpfElNbhACZxx54i50FIiQfcVeRRb6xGroW-_MpNlCwGYGFbY79p8HahDUEgkc5m0FyRsv2Cn76Bxp4dz3hDGJq-Mqd2UtnoG3_kY6AUUagvYJGEcrKERQBKFbeo8uhDhdihUq830AbpdNv7HywnE0NEd9nSAm0DISsfTyibxXZJFwSYuJTo5CopX39dWz7RhrC9Ecrt75NTQWfXW5orsZlwo0pFMMWf8xDBCwM_zqpqP9mGTB-FJOf7BlZroFbTpZBNWN4nGhzE6zei9Hyly5cjhgQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون عزاداری سنگین نیرو هوایی آمریکا کف تنگه هرمز ، قشنگ دارن سینه میزند
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16418" target="_blank">📅 01:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16417">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHZzxJrale8ENd_5zJ9-imqLqtsJ8VZZAnBKrAGOMQ5ZCvpXeluETreFfvzwCgyAB_yX01VsTvJ3fOKl0wpe-NUxdOZrTGZrnfHnSMsJlBTxJT2d2-R7tSNtGhDZtQyqhcLPxI94Y0gp1Ok82Foek74GocfkfGtQFqmljvxtU8Ns5cy_ACj9HaX7YzcZ3q7kTPBrP_soX96cFmDbzy5g7OGdB0F1XjuC3O6_Cx2Osp2AIW6yXZgvAhy1ITp_r3MlQzpWhnql051-Ds7DTeNvi79DtDxBtrGcbt58_Xh-aIsrBDdiE4MsenCDCDnFVcBCahIMeoAAONzYNJ6f4wwTiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16417" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16416">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تعداد کشته‌های زلزله در ونزوئلا به ۲۶۴۵ نفر افزایش یافته است، به گفته وزارت اطلاع‌رسانی این کشور. همچنین اعلام شد که بیش از ۱۲۰۰۰ نفر مجروح شده و حدود ۱۵۰۰۰ نفر خانه‌های خود را در اثر این فاجعه از دست داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16416" target="_blank">📅 00:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16415">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba3ecf0ff.mp4?token=WM7YrMW7QSfCcjpR_t0UjBLcMEM8n5YSA2o3I7qXnhvykwwt4Mr0SHw6mCgaOtc-wTfqNyiuUKCzgTQDRbjoXOmyGiY32HZa4f3Z5BqvGgj-FxDavpBmvvsWZEGzxDb4zuoEz6WaSGqaQSYDwhv2UEYeypSCv6esuawEglZMHREQPU-QnYLG2HocViHI2wKFepnykjNjfBTUN5uJoZF2O7P2kIfqMsPWPepRILEYUEqO55GQGWQmRe3tyuCMqhOHHVdjpVCK6-Qf4Igyz-DPaOR-DXv6gn4O4ZUg6933GevbXbsNU3Y6MzEnq2x1myrfzW5sZNkyr0M-OlA8pP11yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba3ecf0ff.mp4?token=WM7YrMW7QSfCcjpR_t0UjBLcMEM8n5YSA2o3I7qXnhvykwwt4Mr0SHw6mCgaOtc-wTfqNyiuUKCzgTQDRbjoXOmyGiY32HZa4f3Z5BqvGgj-FxDavpBmvvsWZEGzxDb4zuoEz6WaSGqaQSYDwhv2UEYeypSCv6esuawEglZMHREQPU-QnYLG2HocViHI2wKFepnykjNjfBTUN5uJoZF2O7P2kIfqMsPWPepRILEYUEqO55GQGWQmRe3tyuCMqhOHHVdjpVCK6-Qf4Igyz-DPaOR-DXv6gn4O4ZUg6933GevbXbsNU3Y6MzEnq2x1myrfzW5sZNkyr0M-OlA8pP11yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی و قالیباف امروز
😁
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/16415" target="_blank">📅 23:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16414">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16414" target="_blank">📅 23:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16413">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وای نت عبری : هزاران نفر در مراسم تشییع جنازه در تهران شرکت کردند، اما در اسرائیل این خبر خنده دار بود که "بسیاری نه برای عزاداری - بلکه برای اطمینان از اینکه او واقعاً مرده است، آمده بودند."
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16413" target="_blank">📅 22:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16412">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">المانیتور:
مقام‌های اسرائیلی به‌طور غیرعلنی امیدوارند ایران مذاکرات شکننده را طولانی کند و آن‌قدر آمریکا را خسته کند که ترامپ دست‌کم محاصره دریایی کامل و تحریم‌ها را بازگرداند
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16412" target="_blank">📅 21:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16411">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79266b9c5c.mp4?token=Xr41STCu1Dweqh7tKa0ezJy2kDvYIAqpnQHVt6LCPBmPYQcHyhgPOD0ZCUmsS3GuAC3OlKpJ04w0KLF6BiR0TABmjEkSW84WoLJLQTdkrxjuP65A0l-A9Z99OjqJXaEB0cEkuyLQ2Z-5hTf9Szhp8_xhXlEMmAolYIfnE0_5JkFI0LHcyqt9M4dsFgSdwQOFi7MMHgv_KziaaORx8hGlE5F1-Dqi-3HE15ZCPTxyaLeppQLgBJWXh-e9UPO54PPA9MXFzvIiz0aJOP3HiTzjHqO2PJYsTDH9upb-NDWUhPF53RRB_7hygLh3ZpO4NXysAjXXdm11_jX2SMy6F0P10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79266b9c5c.mp4?token=Xr41STCu1Dweqh7tKa0ezJy2kDvYIAqpnQHVt6LCPBmPYQcHyhgPOD0ZCUmsS3GuAC3OlKpJ04w0KLF6BiR0TABmjEkSW84WoLJLQTdkrxjuP65A0l-A9Z99OjqJXaEB0cEkuyLQ2Z-5hTf9Szhp8_xhXlEMmAolYIfnE0_5JkFI0LHcyqt9M4dsFgSdwQOFi7MMHgv_KziaaORx8hGlE5F1-Dqi-3HE15ZCPTxyaLeppQLgBJWXh-e9UPO54PPA9MXFzvIiz0aJOP3HiTzjHqO2PJYsTDH9upb-NDWUhPF53RRB_7hygLh3ZpO4NXysAjXXdm11_jX2SMy6F0P10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمل پیکر علی خامنه ای در کامیون یخچال دار
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/16411" target="_blank">📅 21:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16410">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یورونیوز : در پی انتشار ویدیویی از زنی که با لباس زیر در پارکی در شهر یزد قدم می‌زد، مقامات قضایی جمهوری اسلامی از بازداشت عوامل انتشار فیلم و «برخورد قانونی قاطع و متناسب با رفتار آنان» خبر داده‌اند.
خبرگزاری دولتی ایرنا با متهم کردن این زن به «هنجارشکنی» مدعی شده که وی به «اختلالات شدید روانی» مبتلا بوده و بعد از بازداشت کوتاه اکنون وی به آغوش خانواده‌اش بازگشته است.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16410" target="_blank">📅 20:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16409">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">باراک راوید خبرنگار  آکسیوس:
ترامپ امروز با نتانیاهو تلفنی صحبت کرده.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16409" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16408">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آکسیوس: نتانیاهو به زودی در سفری ناگهانی و قریب الوقوع وارد آمریکا خواهد شد و با ترامپ درباره ایران دیدار خواهد کرد.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16408" target="_blank">📅 20:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16407">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تکذیب خبر نیویورک‌تایمز درباره ترور مقامات ایرانی از سوی دفتر نتانیاهو
حساب رسمی نخست‌وزیر اسرائیل در شبکه ایکس نوشت:
«طبق معمول، آخرین گزارش نیویورک تایمز درباره اسرائیل و مذاکره‌کنندگان ایرانی، خبر جعلی است. یک جعل کامل واقعیت.»
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16407" target="_blank">📅 19:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16406">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صفحه‌ فارسی وزارت امور خارجه اسرائیل در X:
واقعا توی اون تابوت چی‌ گذاشتن؟
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16406" target="_blank">📅 18:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16405">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حوثی‌ها ادعا می‌کنند که با هواپیماهای سعودی در آسمان یمن درگیر شده‌اند، به منظور جلوگیری از فرود یک هواپیمای غیرنظامی ایرانی در پایتخت صنعا. حوثی‌ها اعلام کرده‌اند که هرگونه حمله سعودی دیگر، "با حملاتی به فرودگاه‌ها و منافع حیاتی در عربستان سعودی پاسخ داده خواهد شد."
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16405" target="_blank">📅 18:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16404">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آغاز مذاکرات ایران با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت
به گزارش جروزالم‌پست، منابع آگاه می‌گویند ایران مذاکراتی را با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت آغاز کرده است؛ مذاکراتی که در چارچوب معافیت موقت از تحریم‌های آمریکا دنبال می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16404" target="_blank">📅 18:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16403">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSLBxbB7AomTXbxv4ClzfLk09ufohQWzSE93gjoQgRx1Tu1p8CnSnznwQ34-dEkaAD79eARpJ0dDUn6K7ZrnsbDg7nES35oRURgyGg2VfJrD4qtTnhcQslIOoVpKER4A0BWwkXPJj7zAmRg4qiMi2t5xJaMlfIyp7toJiF4ZE_ufNsV9DANEGxsl0ME426a8PeT7SjI5aXXXCi3LMKtEZ6PkgG6fR1bwfhLo9LDonEJk_eX94jY_fxM-UyzLqrJxPY0KZfBdGjimD-Gknw7vkRnaGVQOoHHIxawziiWncp0XeQp7A5yH6_kM0R5neTrPNialI7QioQ3k_wv3sqvKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: جان اف کندی بعد از من دومین رئیس جمهور خوشگل تاریخ آمریکاست
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16403" target="_blank">📅 18:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16402">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هفت خواننده سوپر عرزشی به نام های علیرضا افتخاری، محمد معتمدی، پرواز همای، مصطفی راغب، رضا صنعتگر، رضا شیری و حسین حقیقی ی آلبوم به اسم بدرقه برای رهبر ضبط کردن.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16402" target="_blank">📅 17:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16401">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الجزیره: ۵۰۰ میلیون دلار برای ترامپ، دسترسی برای پاکستان؛ چگونه شرط‌بندیِ کریپتویی/ دیپلماتیک اسلام‌آباد جواب داد؟
وقتی این هفته جزئیات درآمدهای مالی دونالد ترامپ، رئیس‌جمهور آمریکا، در سال ۲۰۲۵ منتشر شد، یک رقم بیش از همه جلب توجه کرد: شرکت رمزارزی خانوادگی او، ورلد لیبرتی فایننشال (WLF)، فقط از محل فروش توکن‌ها در سال گذشته بیش از ۵۰۰ میلیون دلار برای او درآمد ایجاد کرده بود؛ بخشی از یک سود بادآوردۀ بسیار بزرگ‌تر از حوزهٔ رمزارز که در مجموع صدها میلیون دلار دیگر هم ارزش داشت
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16401" target="_blank">📅 17:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16400">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2a30f1a3.mp4?token=jIdmZ7AEqoQjIHZ7Oajy1BC4aqee2ZBSuOA8ejfxoQ1Ye-eNLLa2m0ZI4W6YfBvzrISiVLHRJn3PPMBu7NrZhDcpKtHLhcXK0LjsBLrz2njkdoVyv8Upar6e5yTbU07OEBLLZtoHccn0FtieNfZ1tQN9YqzjXy90qRb3zr1_j2xzNoKWgodIVthL0lu0fzY_Nx2sdNEj2J4rL9RGNt0043z7dMu7MhNPJNOKva_vru9MsKDlWqrpSMAVYy8kwpj1r3Rchwlc7HpAycxYtQsWnO755G1SJhJMNCIZ6kpBOB8aB6Vt3CcjAbCyo2OnolWsi6KHq2SnqDvsCJTCMSIoLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2a30f1a3.mp4?token=jIdmZ7AEqoQjIHZ7Oajy1BC4aqee2ZBSuOA8ejfxoQ1Ye-eNLLa2m0ZI4W6YfBvzrISiVLHRJn3PPMBu7NrZhDcpKtHLhcXK0LjsBLrz2njkdoVyv8Upar6e5yTbU07OEBLLZtoHccn0FtieNfZ1tQN9YqzjXy90qRb3zr1_j2xzNoKWgodIVthL0lu0fzY_Nx2sdNEj2J4rL9RGNt0043z7dMu7MhNPJNOKva_vru9MsKDlWqrpSMAVYy8kwpj1r3Rchwlc7HpAycxYtQsWnO755G1SJhJMNCIZ6kpBOB8aB6Vt3CcjAbCyo2OnolWsi6KHq2SnqDvsCJTCMSIoLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
خطر حمله قلبی
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/16400" target="_blank">📅 16:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16399">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f09f9f705f.mp4?token=KmrG2zNssJYM4SS1E0y9GcM8DSI33GuYDKy4GIciw5PT1-5UWROws0TQsomPO8vedswc_wwkn6eIV3iS17irbhI_Np0rRRyBkn0AvLfFCYd4v84WWO2Cc7kNgtltj8Qpo0fim4DxfdyMjqnK8qZnzuiayZREMza8Tt-7Zky6xlZBdPOxVZNxWRWDPc0jYwhukHL_DiXRebwkjYnSTRfWjQ7yCV2isCDCfi-bUVndmHJqAP98qbYAlKvg-tSz4eLjsVhEd0UGP1yZCgbmFsOYccZic9dq5183m4Jt-jw68F6yPrA1QkXCDiUfKVWYlk4VY_VmbGhT_Ff9uMtnQRSixQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f09f9f705f.mp4?token=KmrG2zNssJYM4SS1E0y9GcM8DSI33GuYDKy4GIciw5PT1-5UWROws0TQsomPO8vedswc_wwkn6eIV3iS17irbhI_Np0rRRyBkn0AvLfFCYd4v84WWO2Cc7kNgtltj8Qpo0fim4DxfdyMjqnK8qZnzuiayZREMza8Tt-7Zky6xlZBdPOxVZNxWRWDPc0jYwhukHL_DiXRebwkjYnSTRfWjQ7yCV2isCDCfi-bUVndmHJqAP98qbYAlKvg-tSz4eLjsVhEd0UGP1yZCgbmFsOYccZic9dq5183m4Jt-jw68F6yPrA1QkXCDiUfKVWYlk4VY_VmbGhT_Ff9uMtnQRSixQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور هادی خامنه ای (برادر کوچکتر سید علی) و وحیدی در‌ مراسم
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16399" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16398">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">محمد نعیم جُندیه، رئیس امنیت نظامی گردان شجاعیه حماس توسط ارتش اسرائیل کشته شد
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16398" target="_blank">📅 15:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16397">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">واشنگتن پست : مقام های آمریکایی فاش کردند اختلاف اسرائیل و آمریکا با ترور لاریجانی آغاز شد
واشنگتن برخی طرح‌های اسرائیل برای ترور مقام‌های ارشد ایرانی مثل عراقچی و قالیباف را متوقف کرده است.
در این گزارش آمده اسرائیل به دنبال براندازی نظام ایران بوده، اما آمریکا به این نتیجه رسیده که چنین هدفی از طریق جنگ عملی نیست و به‌جای آن تمرکز را روی تضعیف توان نظامی و دریایی ایران گذاشته است.
همچنین ادعا شده «ترور لاریجانی» نقطه عطف این اختلافات بوده، چون آمریکا به دنبال فردی برای تعامل در داخل ایران بود و با حذف او این گزینه از بین رفت.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16397" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16396">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هواپیماهای مهاجم ، حریم هوایی یمن را نقض کردند، پدافند یمن درگیر شد @withyashar
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16396" target="_blank">📅 14:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16395">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16395" target="_blank">📅 14:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16394">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiWy1rXtBvX0ha904ihBExpLEIG9vSOmj5c0Je681D6QwZDcKzXrYJyfb_lTX97brEcv6z3_sAgc-DFBw5WsAqcnONoJDQOFEtJJA1hQ0XlJgt2w-8fzbvA6ZNFUV8XkcYqMytsJfbfOLtw5oUyTlhKbJ9vd-lhYpN9O0vyh88AIFi5ZE-GQiVCOMrS2KNwE6BNdM3K3q8oaqJsnFp438guyQuc_4ZgI-xWdazzXzEC0qsweajLl5AHebvmZgGhEgYL9GaPqWh-0Ld-YU377N1J4ARd1B-2pa5qj_D9eyspG-QBjDZn-pRlr6UgJwG-9SoZomgFcKh-3tNsbyw0VGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فشار فروش آلت‌کوین‌ها به پایین‌ترین سطح در چند سال اخیر رسیده؛ به‌طوری که اختلاف بین خرید و فروش در آلت‌کوین‌ها (به‌جز BTC و ETH) به ضعیف‌ترین وضعیت چندساله خود رسیده است.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16394" target="_blank">📅 14:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16393">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UU8SBjx94cmX6O6UsMTHjDFc-yb5vFn5zx9rH0veRqyNMYmfs9e6RsYQjjogMKjFZJebHCM4zU2BBrMKU4t2nR5PknyuwvZ-gMAi5bRKdZz-VfoVV3baR_-hK3wsG_uFsVSztONmRtUM3tjm1VuEgjyUP7g_WolXHwrQJPZ6ooxJZ2aYfSMQCVOkdQOAQO_J9wQT4NY2C3kUYH1bM6I3FJnyW-O8AMn1oDcbmpBe9TFPuW7BiencPnSne15GK1jOER79f-gOByHcKhDyrbEX3mYYGIdl8ciLphUjSM9cfn8gj1mZPZL4futOr_lBjDOkPHRSQ8fkbF3Bat8pOP6CRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارزانی، رئیس اقلیم کردستان عراق، با قالیباف دیدار کرد
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16393" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16392">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تکلیف امتحانات نهایی دانش‌آموزان مشخص شد
رییس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش، با تأکید بر اینکه برنامه امتحانات نهایی و کنکور با هماهنگی کامل سازمان سنجش آموزش کشور تدوین شده است، گفت: امتحانات نهایی پایه دوازدهم از ۲۱ تیرماه آغاز شده و تا ۱۲ مردادماه ادامه خواهد داشت. همچنین امتحانات پایه یازدهم از ۲۲ تیرماه آغاز می‌شود و تا ۵ مردادماه ادامه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16392" target="_blank">📅 13:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16391">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">WarRoom with YASHAR
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/withyashar/16391" target="_blank">📅 13:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16390">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">1$ Tether 176,000 Toman
Brent oil = 71$
Gold = 4173$
BTC/USDT binance = 61,685$
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16390" target="_blank">📅 13:00 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
