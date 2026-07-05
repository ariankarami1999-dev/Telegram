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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 11:56:41</div>
<hr>

<div class="tg-post" id="msg-16485">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/16485" target="_blank">📅 11:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16484">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnz0GLPHbMKB86Q2SN8KQCUjIndu5eNbZiBL98KJxHy5464fKpyJtmK9SmlgLOdi8qLWrfILpBCQsl4Gb8UPLo1bXrin4CYFqnogdlbRu--GSPoqxYn44KNchSFCO3NBARCbXJeT2GV0KZX3UY4gXPUlcBZV2fOlqZqfQCmobfzvozs2FTXalx-zsmYzo3jF4eYqRPG_Pah3osDm3kZCXc_XQX14Jd6rKv8bqddXWHF3ogL4G_zcf_wnf3kWl7Y6c2l2xm-ZhMSf7TydpR_8xIUbrvOQRBFYbIUf1B_xMSLlLKtX5om8d_xb31oHFr0P4xGbIl1392OrTWC3MHhY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون با پوشش هوایی و اسکورت سنگین، ارتش ایالات متحده یک کشتی باری (با AIS روشن) را از مسیر عمانی عبور می‌دهد!
این اولین عبور امروز خواهد بود اگر موفقیت آمیز باشد.
@withyashar</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/withyashar/16484" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16483">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">قایق‌های تندرو سپاه، مسیر عمانی را بستند
هرمزلتر: نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده.
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@withyashar</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/16483" target="_blank">📅 11:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16482">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده. @withyashar</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/withyashar/16482" target="_blank">📅 11:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16481">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فرمانده نیروی قدس، اسماعیل قاآنی، و فرمانده سپاه پاسداران انقلاب اسلامی، احمد وحیدی، هم امروز در مراسم تشییع جنازه خامنه‌ای حضور داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/withyashar/16481" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16480">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سخنگوی ارتش ایران: از فرصت آتش‌بس برای تقویت توانایی‌های نظامی خود استفاده می‌کنیم و لحظه‌ای را برای این کار از دست نمی‌دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/withyashar/16480" target="_blank">📅 11:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16479">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">قطر: فعالیت‌های کشتیرانی به‌طور کامل و فوری از سر گرفته شد.
@withyashar</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/withyashar/16479" target="_blank">📅 11:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16478">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وال استریت ژورنال: ایران، روسیه و کره شمالی، در نحوه تعامل با بازار ارز‌های دیجیتال، ایجاد رمزارز‌های اختصاصی خود و پلتفرم‌های معاملاتی برای دور زدن تحریم‌ها، بسیار پیشرفته‌تر شده‌اند
تهران و مسکو از ارز‌های دیجیتال برای خرید پهپاد و قطعات یدکی تسلیحات استفاده می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/withyashar/16478" target="_blank">📅 11:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16477">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی @withyashar</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/withyashar/16477" target="_blank">📅 10:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16476">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیویورک تایمز: مجتبی خامنه‌ای همچنان در تلاش است تا در تشییع پدرش شرکت کند اما مقامات امنیتی مانع هستند
@withyashar</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/withyashar/16476" target="_blank">📅 10:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16475">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al6sXC9B4PfREbmxLZGJ-svr9Bm-H30mGWCGGR4jCejZmbciDebC38ljYt_2rWUgffI8kSeOhjUSyM2HnMOV6NaImbf6GIpDA87Ze1Qn5nSmFc0PPHOIguBHULi04FqNFS6c4xvemM4VInNFEay_daRx4Cmz-3wGw4By3r0Ld4bK3yJ13IwmQ-JeidEwi9a5xWeZ2kFX9VIeTdP0jlNAa0Y8oP-yQV81rXTDsUlWXZ0T9P2tWZGC8jopDWQdvwRufnWFlFzrfO3Uml7fgpn3vxnidBqCULvLIHQUgImNfDwGNWb_2x88kMMvkd2vyy0G-1KsG3_64lImgGPNFw87Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شباهت امام جمعه پاوه ( ماموستا قادری ) با ( هاشمی رفسنجانی ) که دایرکت منو منفجر کرد
@withyashar</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/withyashar/16475" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16474">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV9N-bQbqishj43Z1vm96NsFvEnRCD139Wj63JfrVplB6n_TkaX3IcpBZa0FCE-CZDKAaTFcoHPNYmqheA-KqT5dMNInf1CyQKOUe5jIHcjkmb0uILOh9uUUeSNHO5kNxmPrKfZIyU-upRTfqHnwJCdLmB9ItmxBKk0Qn9crQYwwNa1JN-c36WvXJ3Z3E3AaTHwRi6gMvUkr10M5zvBfaIgwtbQL4JLxwG_nSsjqIE6tv7BxprBQ7vauCgrbHTVpH_2lWjmeHe9a8oQP_1t3tXj0YnZs1hBaebc0gVAN8ZyfQ22PBU9DymYE7KG4BeimTjBBQbJ04UMImJMho_mmBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/withyashar/16474" target="_blank">📅 10:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16473">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=KHP04yA3iH0J8QRL08iwDK57lm-6n-ScnKHql6NaV8QAKu9OCCUS-LD-4UZJ4qlNAMRiBNvPAODNq4wZ9hlp-EUy1_C_AEJO1kvYH-s3AhA2DZAjtB33mFL7jL2IWWPu-t2lD5P35jrGLOwawOoonL1vMBUbDBlTfxdg78b5dQ7YopaELU4nxHz8SG5Rlx61M_75iE9mJwAm2uzLLL4ZspzJej1KnIH52uk0a2WphjuBV8reDNR4NaWRuHfBJ_z_ouyODJmY6bfDixw2PCYROAt0rRcKSSQwvJe5hcDhtWGi_VgwoPg6op57S9WeQ8u5QUSu81sEuzHRSH8JH0MoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=KHP04yA3iH0J8QRL08iwDK57lm-6n-ScnKHql6NaV8QAKu9OCCUS-LD-4UZJ4qlNAMRiBNvPAODNq4wZ9hlp-EUy1_C_AEJO1kvYH-s3AhA2DZAjtB33mFL7jL2IWWPu-t2lD5P35jrGLOwawOoonL1vMBUbDBlTfxdg78b5dQ7YopaELU4nxHz8SG5Rlx61M_75iE9mJwAm2uzLLL4ZspzJej1KnIH52uk0a2WphjuBV8reDNR4NaWRuHfBJ_z_ouyODJmY6bfDixw2PCYROAt0rRcKSSQwvJe5hcDhtWGi_VgwoPg6op57S9WeQ8u5QUSu81sEuzHRSH8JH0MoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی
@withyashar</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/withyashar/16473" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16472">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/withyashar/16472" target="_blank">📅 10:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16471">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/withyashar/16471" target="_blank">📅 10:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16468">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uik-_fd8AiqJefXtWIA_TebJyD4D3F3Rs_yYj2wtbsfcRu1Poxg1IupLzl9u0SPQJe557otqv7OrWYS7hjBD3rCIwG0TYVLVmk8Wt5tnqvNtUkrgqwcGF9-D8saRaTUODl08DqubtgsO3haKuodKa0y3FSenGgWhQhplirzcYkX2EeJjDOsWPLHpmD0S-k8WL5ol8IlfzH9EI3sV-Wo515XfZOc1JpewHZE7Ej-hh_Xpi-gcwuvSz_ShO5mEgsy4A_NBO-a-KC3m6hxzL_4Tjusrp9AYYBH0QCOKwcRZ66IyRSwWE1J-L9OJy-QJoLXkIb7V5ZeYu6iAPxeCSpHSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtS7f0xCMhwGBiWbw1NP3dJhdGKO6TuPu5ZRYdN0dgslWFYwc7t13fVYRFbnsjjhQkXfYQlXXaDkS4al40fucKMeMPDV9ZYf9TXbNcbAvJpw48TV_WNeDF4heVb4ILuVv1pCbDeSGsH8oscOwAS8QBVhTqZ5R8oeAiimb37GC4bTI_eqLoCFt7mGwxyCPJ39LjJ0JUXh9l0veeR_EU8McFuYgJJKEyZcB5xmrLA4KgjbYJKqM849zvaGVJkB3p1MVGnR4-oyvQtDKdi20fbGTT1kgzUBQi6ks5HZ1RkZArvmD_isHA_ipu-BoxXkPB7sgZWzP4SC9TR_HRKZCCQoFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jyukUg0DzChXJwq4r6qb0_TXewARlwQQ3uT5dpxSB9Q1hTWl3LN0n5t4RrFzG2IpyZen3AsyqZnOma-c7u3xYOmDmjrtN30YgyjcA7MYL98IPtF9LOro2vyUf6HUi8BGg6u6vrBmkeX9jnZ8xJE1r681-ZfHBzgjvl3QLiv-1_GBNmKyL0oRG9mYaSiivZihtWuO0wvV6BoEtLm4KSbheuCviqytNNoPSMJsNv08uRpEQEkXHC3PL-eHV5VneqWhufgVFpYelea4mWfDbXbCp8WLHqckzZqHdJj452yFUvGBGq1QoRbVjt31TccszVZgaNyeJd6SPdmmkqCmsiws2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شهستان پهلوی (ویس قبل رو گوش کنید)
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16468" target="_blank">📅 00:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16467">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شَهِستان پهلوی، نام یک مجموعه بزرگ شهری در زمین‌های منطقه عباس‌آباد تهران بود که اجرای آن در سال ۱۳۵۴ در زمان محمدرضا پهلوی شروع شد ولی در طرح آمایش سرزمین ۱۳۵۴ ستیران آرمان‌گرایانه اما ناپایدار و مخاطره‌آمیز برای توسعه کشور و شهر تهران قلمداد شد و با وقوع انقلاب ۱۳۵۷ ایران هیچ‌گاه بطور کامل اجرایی نشد. بخشی از این طرح احداث یک برج مخابراتی مانند برج میلاد امروزی بود
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16467" target="_blank">📅 00:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16466">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارشهایی از فعالیت پدافند پرند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/16466" target="_blank">📅 00:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16465">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کانال 15 تلویزیون اسرائیل: در‌تماس‌ امروز دونالد ترامپ از بنیامین نتانیاهو خواست اوضاع لبنان را متشنج نکند.
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/16465" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16464">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ارسالی : یاشار جان درود
داداش همین الان از اطراف مصلا برگشتم ، تمام حجم ترافیک و شلوغی برای صف های ایستگاه صلواتی ها و مفت خوری ها بود
یجا مردم بخاطر یدونه تخم مرغ آبپز و یدونه لواش داشتن همدیگرو میزدن همشونم طرفدار اینا
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16464" target="_blank">📅 23:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16463">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اکونومیست: جنگ بعدی خاورمیانه بین اسرائیل و ترکیه است
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16463" target="_blank">📅 22:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16462">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ در تروث : اروپا دارد یاد می‌گیرد که وقتی مجرمان جهان سومی را در خود جای می‌دهد، خودش تبدیل به یک کشور جهان سومی می‌شود. این اتفاق خیلی سریع می‌افتد، فقط در یک چشم به هم زدن. من درست به موقع انتخاب شدم!!!
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/16462" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16461">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فردا عصر کابینه امنیتی اسرائیل یک نشست
ویژه برگزار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/16461" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16460">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رئیس‌جمهور عراق:
عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16460" target="_blank">📅 21:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16459">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو ۲۵۰ سالگی استقلال آمریکا را به ترامپ تبریک گفت و گفت:
«ممکن است ما در قاره‌های مختلف زندگی کنیم، اما به دلیل سرنوشت مشترکمان، به شدت به هم متصل هستیم. آمریکا بزرگترین نیروی آزادی‌خواهی بوده است که جهان مدرن به خود دیده است. اسرائیل مفتخر است که در کنار آن بایستد. زیرا اتحاد ما نه تنها بر اساس منافع مشترک، بلکه بر اساس ارزش‌های مشترک بنا شده است. امروز، این ارزش‌ها مورد حمله قرار گرفته‌اند. مستبدانی که با آنها روبرو هستیم، شعار مرگ بر آمریکا، مرگ بر اسرائیل سر می‌دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16459" target="_blank">📅 21:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16458">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">Bitcoin +63,100
🆙
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/16458" target="_blank">📅 21:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16457">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش انفجار شدید در سلیمانیه عراق
@withyashar
🚨</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16457" target="_blank">📅 20:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16456">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">العربیه : ارتش اسرائیل شنبه 13 تیر با انجام چهار عملیات جداگانه، اقدام به تخریب گسترده خانه‌ها و مجتمع‌های مسکونی در مناطق شرقی و شمال شرقی شهر خان‌یونس کرد.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/16456" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16455">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده  - ممکنه همین هفتهٔ آینده این دیدار انجام بشه @withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16455" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16454">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ به آکسیوس : ایرانی‌ها برای امضای توافق تقلا می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/16454" target="_blank">📅 20:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16453">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده
- ممکنه همین هفتهٔ آینده این دیدار انجام بشه
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/16453" target="_blank">📅 20:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16452">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ به اکسیوس : "از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند."
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/16452" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16451">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ به آکسیوس : هیچ یک از طرفین در طول مراسم تشییع خامنه‌ای، به سمت دیگری شلیک نخواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/16451" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16450">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ به آکسیوس:«همه آن‌ها آنجا هستند. یک گلوله می‌توانیم همه آن‌ها را از بین ببریم ، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/16450" target="_blank">📅 20:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16449">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای برگزار خواهد شد @withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/16449" target="_blank">📅 20:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16448">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECYQWsnKOg39QdR02Vcrlx-THOJQBZH_jGLpmWJtmN8fhdeFVJwZLAG0xBGpTOygYSKOKppbwUyGugMKFV6qFavyWaGxthRxmoWMhH_3jVQuszx-M-4IPv0mQAj7hv9ayik3jLXFZXPLgdBdZf1OsbytYxaVyM7DxJgTKPvwAHu_2TdyGTiMaJT0o88wvpYX_BKyu3haSiEeB5Lf4KReiS6TJ06cvQFq1xQBWEym3JPg_krQCPEyaAHaVqft11zRI-oIrugeUF47urzfXiawimWspSSEWITKLBuqQiHHYXqRkf0TF2a5-AquKCtkwMQLn6yBHJwoDW_1NMiuORkeEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای…..
@withyashar
😂</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/16448" target="_blank">📅 20:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16447">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJUeHTpvuGJGNULg5Q8q40YSSmsefQTDEmnpws8wSWisEPqRz254906km0yWPk1E54_gMrNmuHDe1EkP529yVR7lmxDHnqKMm-FT-b9OkBD2yLX7dHBE5ygq6a74t0uBJGIRjpfYqoPjsE3h9qpACrqdJJcbOsKwiJDHdb05xl778UjpoGS8hX0zxuS4E7tqe9AXas-z9zHrnPiIV68FKqIL5lkca4_IUHp_gO42O4X3xKWJxfZmxeAjTaxs6tGxLEUUBxcEhugBYz2Q2QTdHen_-zu1GLyaea1jVwSIIUXz6qPZeG__5QVFMe4fGD9tTVDk8Lf5mxD25zfeOkiYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد جهانی علی خامنه ای
بیشترین فاصله زمان مرگ تا زمان خاکسپاری رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که علی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ ثبت کرد
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16447" target="_blank">📅 19:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16446">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است. از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد…</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16446" target="_blank">📅 18:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16445">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند. @withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/16445" target="_blank">📅 18:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16444">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8xaE79NXJZGaB_rCEHcHZfz5NrCw1njOBWjFS_UWz_JvEIHelu69Y9AaBR-581V8bTUQqqpoqyH1Nvgt5g0BwAGFfP79xOHd6bEnN6tKRla7aSAVi5Ho57wuRrZeM8SaqU4loiK_Nr2Hovdxjjm5KKbGzUCaQcz-VtYRfu-srKLhWanu4wjPuHmrGjaF2gho0bUdFNA7DlUyk78PqgB_Inwrn1BbKCfGZgp5z008ZNsSH4-qfd4S-wIpUnNqu5rNQZE8Mr38aW4COmGKnQtaXJMCGVIA7IQzTmhkpKZESLk9R1bjXczCqmk5LT3gvPAumUS0DwLJgpXqRiy4mC5JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشریه نظامی «میلیتاری واچ» نوشت: کارخانه هواپیماسازی کومسومولسک-نا-آمور روسیه
تولید ۲۰ فروند جنگنده سوخو-۳۵ سفارش داده‌شده توسط نیروی هوایی ایران را به پایان رسانده است.
وزارت دفاع ایران در حال حاضر هزینه نگهداری و پشتیبانی این جنگنده‌ها را در داخل روسیه پرداخت می‌کند تا پیش از انتقال به ایران، در روسیه نگهداری شوند
احتمال دارد نخستین سوخو-۳۵ها از پایان سال ۲۰۲۶ وارد ایران شوند؛ آسیب‌دیدگی زیرساخت‌های پایگاه هوایی همدان یکی از عوامل اصلی تأخیر در انتقال است.
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16444" target="_blank">📅 18:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16443">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای برگزار خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/16443" target="_blank">📅 17:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16442">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نیویورک‌تایمز به نقل از منابعی در سپاه:
مجتبی خامنه‌ای خواهان حضور در مراسم خاکسپاری پدرش در مشهد و اقامه نماز میته، اما مقام‌های امنیتی تاکنون با این درخواست مخالفت کردن.
به گفته این منابع، نگرانی از احتمال سوءاستفاده اسرائیل برای ترور یا شناسایی محل اختفای اون، دلیل این مخالفته.
@withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/16442" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16441">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b97Y8aWNmf57yt_kJS7HpT6QuwVKz9N5DIavHrdwZoIgFRJDO7jQ8wtZHQvHhfNGtcr-WaB-4NqjkM0D4oB00DT6LpKLoH4xf0cBOHrngQQaKhQk2KNIsrQJZVs9YeX7PSdy32hgYXK4IDUM6KlrwW0OgS5YqNsfsg-vMy9GuDLEbP5IpSxqkzEBoamYswR83N39CFdJGUif9nHQdjDOmiq0gY-LODSMuYVNbwoOO7aoolz5dwXVKCcHESdV2aylchBa4laKXGbDKm2rYuE6aC3dmu5FiXCZQb-ml47nBQwRKeVsgFiTD-hxcMuqMSabxpVkShFZpM3lQ25IB_UgFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار علی عظمایی امروز به عنوان فرمانده جدید نیروی دریایی سپاه معرفی شد.
فرمانده قبلی سردار تنگسیری بود که توی جنگ کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/16441" target="_blank">📅 15:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16440">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیویورک‌تایمز:  عبدالناصر همتی به مجتبی اطلاع داد که در صورت تداوم محاصره دریایی، ذخایر مواد غذایی و دارویی تا پایان ماه اوت به اتمام خواهد رسید.
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/16440" target="_blank">📅 15:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16439">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=EHyEmEY75bUKbheAotGMaSOIkYwjjpSP8U6Sq3oFut9OycEzQ35H3Ed0UPnnNMbD5BLu5Vgg6LL7SbvgZHvfcxCAuWIivw3Gs_mfWAUoWSAnS4lAcTbpxBWK4ZiXORYV1KcZqMweTRdYW5T1PxFqWVJ37HldKYSOT4ma0sybuw3YV7Ms_sZmKn2CT_nzqvnJJRR3msjtC_gfABPOyViyEtDRgGxQRQwUBE7r3V5MEXiXwUeANIPqrUDjMjdqAb1H2ADpGBnfS1nO3zYrXc2H2OSEHPKDVR2C_I-lCm-qTRPXfuTaUIoWVmeuT9-BrZWa2fo72ImP_KavCwAEbrEzkJtTvm_iUj-UYehhK_4Jfy4wbtT2VgOfN6lTU1hm7SW0DpX52ygmzBPaN2q6DBhwFqGq15a4NEAmCr_TqX3ijRjRlKEh2EpWg4fYPYw_XyW2wfz4_ymDVrfbcw1Nlx0cV8HOUwJ4ZG8QmVzULDpXB8i0uanlIm0h8pa5eDhBNEAFXjKwCxXW-Xa1twa1KHasnsksD6-BRr3w5aPIPmxKwlHDCZxhmORrycx4YHV7lo3S0488KS0yJiYw5khp0AkHcId72scfNRY4gpWXyAXgr7luuI44npgzPRPRjkplMpTSSu1klw1td-rKDuCLVsS5HjL-pm1V0p36N29QUiq7JxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=EHyEmEY75bUKbheAotGMaSOIkYwjjpSP8U6Sq3oFut9OycEzQ35H3Ed0UPnnNMbD5BLu5Vgg6LL7SbvgZHvfcxCAuWIivw3Gs_mfWAUoWSAnS4lAcTbpxBWK4ZiXORYV1KcZqMweTRdYW5T1PxFqWVJ37HldKYSOT4ma0sybuw3YV7Ms_sZmKn2CT_nzqvnJJRR3msjtC_gfABPOyViyEtDRgGxQRQwUBE7r3V5MEXiXwUeANIPqrUDjMjdqAb1H2ADpGBnfS1nO3zYrXc2H2OSEHPKDVR2C_I-lCm-qTRPXfuTaUIoWVmeuT9-BrZWa2fo72ImP_KavCwAEbrEzkJtTvm_iUj-UYehhK_4Jfy4wbtT2VgOfN6lTU1hm7SW0DpX52ygmzBPaN2q6DBhwFqGq15a4NEAmCr_TqX3ijRjRlKEh2EpWg4fYPYw_XyW2wfz4_ymDVrfbcw1Nlx0cV8HOUwJ4ZG8QmVzULDpXB8i0uanlIm0h8pa5eDhBNEAFXjKwCxXW-Xa1twa1KHasnsksD6-BRr3w5aPIPmxKwlHDCZxhmORrycx4YHV7lo3S0488KS0yJiYw5khp0AkHcId72scfNRY4gpWXyAXgr7luuI44npgzPRPRjkplMpTSSu1klw1td-rKDuCLVsS5HjL-pm1V0p36N29QUiq7JxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت نیکسون در ‌تهران ۱۹۷۲
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/16439" target="_blank">📅 14:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16438">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDOT5xqGrx6_6aIQT9d0aHwVViAmQVVLrvHMz9Zd60XgwsD_4PSZQcqCTeVGK-PQh0JJeGM4FAVADkL3TXSDwlgd6L6kHIlX9elLJYd-t-OEI5GgNqtbhHum5-PlitPS2iRkjRRsO0Py4PU4WS9g6F5md6ybHPjVEt8mbx4BamMtHXGw8_oOcdDpNW7EWv5VCJPgZ5_4wX2e1jVnu7xmWZPV0wt5IS03bH-Ihtz7-nTLuu-SFGNBEg9lD36678kLL841jGfJ_JH8T_xb83SOt_fa9Vme8FpvMEFB1UVNZCTnB6_mn66XM5BTCzO3TJZkrKPo789K2f8KzmcKElwB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند.
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/16438" target="_blank">📅 13:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16437">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DefKqHIRss-mDqL16Az75XTg88fdQUgKusF3rySHcVNHgOlni5LAx6-3o8PrfqXiq_pehtX9Ew926ME6JcIs05RwRNt6SGWwjvrXW647b77L8k7XxnVdqgyCohoHu_tPwknZ16qAciocsVy7D_4P6spo6to7CRee9I_w0zms8PjKmooYSMxouTMFWfQ7Qc5KCBQBofuozeGQfkkFFKqi1IyI7ekUklndvpmt1J-c7hO1fLT7BrgUa1QKQhbJlvT_fm41ZjsanQTA4OIZqeWTsWqkw3vEmYO2AE7t9NU43IP7Ntn3ZdtKQbJK_nfkjQSpoEn7L1_QpE2HLU1M_lP-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان درست شد ، عباس مکار و ممباقر نره
@withyashar
😂</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/16437" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16436">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUxfF_Agfp9L5SWe2SUb4hC1K0pC9Nist1IJyMjqfnhRP6EMU9-LCoKt_0FBhF4lgvJWbU5vxmjgqVziBobKzsGWR0Ahbs5JCC1TVVpwVvv5S-bLa7fvS0HiZVO1CfO43htmHBvXM54m1Ehv8ptLOU4j102hIlQJZaYSyp5SsNsjMICo7czOiR9NiVHWDbrRpoSV5MCA6d-ZfTdE6iznYSkTPF-V8CTpYK1dLZ1G_3rvhuHD1TDHRItSOw_oAZeHhIDESFs4Enxyrfu6G-W_1fie_rfYhFnVvgssnQJy5acMBVLlb7TEvPrGhw7CIN86JkZ3EkemETNnR2UiouoUGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره حمله اسرائیل به لبنان
@withyashar</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/16436" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16435">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Psyrw6omzhD_8Z07jcoP9sXtCNHaPA1igpxiNnQT5iWb64Fenrtex9pxVjBO7TPDm9S3eltLtR2TOq4OQtBP-oFrChKMKU95odeyUMROupqflH7jkmuqK0RSXsfr7HhiJFmKEPGQRA8n3chZf6W0EQHsp5nNi4WqSYK1ngb5ZIBAhSURHZU6A1fqjgAGqI7Okn2tpA5BKAnNFdvmLaAChwgRA4iY2fvdUarLI7ZIaT4dh3Zfpf2xNFc4t5Jeqv9qwE0PlazIPXp-NN__lJ3j0oMK-NThGWDFT2gvS4LaAOwGzu_9zIm2QwapMZeU1aDPhCM9fd44EynNFOOKuLQClw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : سری جدید ۱٠٠ دلاری با امضای ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/16435" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16434">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">افزایش تولید نفت اوپک با بازگشایی تنگه هرمز
طبق یافته‌های نظرسنجی بلومبرگ، تولید نفت خام اوپک طی ماه میلادی گذشته با ازسرگیری صادرات تولیدکنندگان خلیج فارس از طریق تنگه هرمز در بحبوحه تفاهم‌نامه ایران و آمریکا، افزایش یافت.
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/16434" target="_blank">📅 11:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16433">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ان‌بی‌سی نیوز به نقل از چند منبع آگاه:
آیت الله سید مجتبی خامنه‌ای احتمالا در مراسم خاکسپاری آیت الله علی خامنه‌ای حضور نخواهد داشت، چون در حمله آغاز جنگ به‌شدت مجروح و چندین بار تحت عمل جراحی قرار گرفته!
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/16433" target="_blank">📅 11:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16432">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کانال ۱۴ اسرائیل : حسام حسن، سرمربی تیم ملی مصر که اولین پیروزی تاریخ این تیم را در مرحله حذفی کسب کرد و به مرحله یک‌هشتم نهایی جام جهانی 2026 صعود کرد (در مقابل آرژانتین)، از این فرصت برای ابراز اعتراض سیاسی استفاده کرد و پیروزی را به مردم نوار غزه تقدیم کرد: "امیدوارم خداوند پیروزی را به آنها عطا کند."
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/16432" target="_blank">📅 11:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16431">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نیکلاس لیساک فعال رسانه‌ای نوشت:
"یک منبع موثق می‌گوید مجتبی خامنه‌ای در اواخر ماه مارس، پس از آنکه بر اثر جراحات ناشی از حمله هوایی‌ای که پدرش را کشت به کما رفت، جان باخت.
او هرگز نفهمید که رهبر جمهوری اسلامی شده است.
قالیباف و سپاه اکنون در جست‌وجوی افرادی با شباهت ظاهری (بدل) هستند تا آن‌ها را در انظار عمومی به‌کار گیرند."
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16431" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16430">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">منابع اسرائیلی به «کانال 15»اسرائیل اطلاع دادند بنیامین نتانیاهو، در انتظار چراغ سبز ترامپ، برای تصرف پایگاه «حزب‌الله» در ارتفاعات منطقه «علی الطاهر» در جنوب لبنان است.ترامپ از نتانیاهو خواسته تا زمانی که مذاکرات با ایران ادامه دارد، این عملیات را به تعویق بیندازد. برآورد ارتش اسرائیل، بین 30 تا 40 نفر از نیروهای یگان «بدر» وابسته به حزب‌الله، از جمله شماری از فرماندهان این گروه، در داخل این پایگاه گرفتار شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/16430" target="_blank">📅 10:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16429">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سی‌ان‌ان‌ به نقل از مقام‌های آمریکایی:
مقامات دولت ترامپ از نزدیک شبکه جاسوسی اسرائیل که در ماه‌های اخیر، فعالیت‌های اطلاعاتی و جاسوسی خود علیه ایران و آمریکا را افزایش داده، زیر نظر داشته‌اند
مسئولان آمریکایی تلاش کردند به ایران درباره این نگرانی که اسرائیل ممکن است قالیباف و عراقچی را ترور کند، هشدار دهند
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/16429" target="_blank">📅 10:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16428">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حضور هادی خامنه ای (برادر کوچکتر سید علی) و وحیدی در‌ مراسم @withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16428" target="_blank">📅 10:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16427">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=SVSbbZVg5ymAc1Jj5HwOhVIhCeCexocI6oRW80apheH2H6I5nJwYzXnEXYh-hIp_5ILZfEKh96u4iBiBi5GgvYNIE_hwTpLkGpOhONPNhkXfm88-Y6x3opam7qOaZt_LcrlmHy2cX9SZrdjYOX2W1Zj6vvRuVZqXR_1zZRBrDsLluQK5Whi4yTapAyUed03_NFHhnSSLS7Yj996w0FA8sWuwPrLGbXopd6-J5lDllWIZCXQiE2zQ9ElUNWb2VwZMpQCFbS67n6fg0WgIMfZO7vIk8ofauvF4laXO2j8aD_NQ9TlGfFmhBwRd1_u-m272kSDPyRXAcg-HD0ZEN8QUlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=SVSbbZVg5ymAc1Jj5HwOhVIhCeCexocI6oRW80apheH2H6I5nJwYzXnEXYh-hIp_5ILZfEKh96u4iBiBi5GgvYNIE_hwTpLkGpOhONPNhkXfm88-Y6x3opam7qOaZt_LcrlmHy2cX9SZrdjYOX2W1Zj6vvRuVZqXR_1zZRBrDsLluQK5Whi4yTapAyUed03_NFHhnSSLS7Yj996w0FA8sWuwPrLGbXopd6-J5lDllWIZCXQiE2zQ9ElUNWb2VwZMpQCFbS67n6fg0WgIMfZO7vIk8ofauvF4laXO2j8aD_NQ9TlGfFmhBwRd1_u-m272kSDPyRXAcg-HD0ZEN8QUlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارزانی، رئیس اقلیم کردستان عراق، با قالیباف دیدار کرد  @withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16427" target="_blank">📅 10:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16426">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت. @withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16426" target="_blank">📅 09:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16425">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانال ۱۲ اسرائیل : مقام‌های اسرائیل ارزیابی می‌کنند که طی ۲ تا ۳ ماه آینده، احتمالاً تا سپتامبر، «هیئت صلح» ممکن است حماس را ناقض توافق غزه اعلام کند.
چنین اقدامی می‌تواند به اسرائیل آزادی عمل بیشتری برای فعالیت در مناطق تحت کنترل حماس بدهد و به‌طور بالقوه به ازسرگیری درگیری‌ها منجر شود.
@withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/16425" target="_blank">📅 09:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16424">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=ua1Dq4KnyZBUbI_ESFgj8TFd0DFdSNSbcggLa8UlxJaPiQChwjl4zyAVEyxeLVW07rKFZAQfGRCF15tj77YSpKLa4YZ71HW_6oaruFbtRP0icsyIJIPlEPZYVUg27dBYpogalO0ZZGViAtpLn5IEDNV4Kk4_RuqxUgQRbMvpGS3N-rzvL1h3e4jkp2vq8Ap1YPyPFiWHYe7Naj-eTgr1hKpCDuapjjaqc7o1NFT3Raw6hGjflL7wvHb6J41R5qfIPjR6_wwPyJ_SDmAQNVQyEO5FiEcLyaZrbtVIV1s_CzBIIrx46yxNTO7dJ80AIJxbXQA9GVO3NztRHX68KAx6Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=ua1Dq4KnyZBUbI_ESFgj8TFd0DFdSNSbcggLa8UlxJaPiQChwjl4zyAVEyxeLVW07rKFZAQfGRCF15tj77YSpKLa4YZ71HW_6oaruFbtRP0icsyIJIPlEPZYVUg27dBYpogalO0ZZGViAtpLn5IEDNV4Kk4_RuqxUgQRbMvpGS3N-rzvL1h3e4jkp2vq8Ap1YPyPFiWHYe7Naj-eTgr1hKpCDuapjjaqc7o1NFT3Raw6hGjflL7wvHb6J41R5qfIPjR6_wwPyJ_SDmAQNVQyEO5FiEcLyaZrbtVIV1s_CzBIIrx46yxNTO7dJ80AIJxbXQA9GVO3NztRHX68KAx6Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما ضربه مهلکی به ایران زدیم. آن‌ها مشتاق به حل و فصل [مشکلات] هستند. آن‌ها واقعاً می‌خواهند این موضوع را به پایان برسانند.
ما به آن‌ها یک هفته فرصت دادیم تا مراسم تدفین برگزار کنند، زیرا ما مهربان هستیم. این حقیقت دارد
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/16424" target="_blank">📅 09:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16423">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16423" target="_blank">📅 03:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16422">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16422" target="_blank">📅 03:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16419">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">@withyashar
🪓</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16419" target="_blank">📅 01:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16418">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfI43Usyhxlq3v9wP9LQor-Qcc5rstOaSuvjTFCAU1ltNbWI7lwVP32O20XIH_DAGrfX2jKCwGwS6OWtgRSDkzj4Ebx015dOhrHp7oE6Ul-pHv2bJGx2Zn6eI7B-x6UmltsZAh1PHA76w71HSgXcMMWFopIXOY5I80TuDqAQbu_e6Nwaeyu2-LkDHUreHaHg2phf9bYysCNchd4q0Exu3rsznqrNkubCnYypDDLYrJydG4XObC9Js6iZVR_6iK0w4O6Nrcs4guZFl1XLggw-RM2pW99uOKz32gzMXliB3yD6ic2id6f4JIGCOAoA5ZX39Ml2ENxwetqiwUgaqBhRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون عزاداری سنگین نیرو هوایی آمریکا کف تنگه هرمز ، قشنگ دارن سینه میزند
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16418" target="_blank">📅 01:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16417">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d07IK1vFuX78bxIf4QYdd_94obFjF2oMo1NS-HedBQr9jgjWZQh5LwHqdZW47urKUrZaq5G3fAlOq1tZ-c3zQEkZoCaKgVLoWCKP-ElmhIzh3Hzp4ozE_WkJwckCagLczqHZ06R48K_WHEPAH0ptFTgFM-ISrDvMqxYlK7T46xykDluEW2MggdfG5SCDd7GiemDbDUfNolNMNpPOxWcdBiVrDLpKuh8Slt6FDYhTpyU5jxLMO8roo6Eaiv5re5jrQ18GpUe3eyMALZORocMNzIIHNcfy2mDGgVIHOqPXPaYh1IDqNSaKAr9vS1lu_1P54REcpNfqkbSeHQoVLT5vlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16417" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16416">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تعداد کشته‌های زلزله در ونزوئلا به ۲۶۴۵ نفر افزایش یافته است، به گفته وزارت اطلاع‌رسانی این کشور. همچنین اعلام شد که بیش از ۱۲۰۰۰ نفر مجروح شده و حدود ۱۵۰۰۰ نفر خانه‌های خود را در اثر این فاجعه از دست داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16416" target="_blank">📅 00:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16415">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba3ecf0ff.mp4?token=nD4vpHjG_TG2YwA6gS_agrU8uU4dJuDiFMxIKpiwR6oAE5KZRuXvkao-ZGKj2sV2ShSyc39b3lmYlVTnxrL-UBIgTw4I1kjuszMrQuue52gLPYcILksOJX1dQzBFnjJwiM1ooJI7u4FhWPU5jNHFr_AePFKRp1YoODPeXDS4LxLZTPsESjKvGhX-A4BjSzz7TBjd0b0cFgsrAsa2ZM6JkSehH05i9PPXOArcPJ5bxVV0rvW-XGJorSo5zoqFaHKybkzYWWykDX_dPxRISOdLSoTF3XIS9lDCfuZk2O8rA7dYNB0ZCb07YadK4MI64LrXakgujEfxJgquQ__ZJw_SKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba3ecf0ff.mp4?token=nD4vpHjG_TG2YwA6gS_agrU8uU4dJuDiFMxIKpiwR6oAE5KZRuXvkao-ZGKj2sV2ShSyc39b3lmYlVTnxrL-UBIgTw4I1kjuszMrQuue52gLPYcILksOJX1dQzBFnjJwiM1ooJI7u4FhWPU5jNHFr_AePFKRp1YoODPeXDS4LxLZTPsESjKvGhX-A4BjSzz7TBjd0b0cFgsrAsa2ZM6JkSehH05i9PPXOArcPJ5bxVV0rvW-XGJorSo5zoqFaHKybkzYWWykDX_dPxRISOdLSoTF3XIS9lDCfuZk2O8rA7dYNB0ZCb07YadK4MI64LrXakgujEfxJgquQ__ZJw_SKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی و قالیباف امروز
😁
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/16415" target="_blank">📅 23:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16414">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16414" target="_blank">📅 23:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16413">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وای نت عبری : هزاران نفر در مراسم تشییع جنازه در تهران شرکت کردند، اما در اسرائیل این خبر خنده دار بود که "بسیاری نه برای عزاداری - بلکه برای اطمینان از اینکه او واقعاً مرده است، آمده بودند."
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16413" target="_blank">📅 22:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16412">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">المانیتور:
مقام‌های اسرائیلی به‌طور غیرعلنی امیدوارند ایران مذاکرات شکننده را طولانی کند و آن‌قدر آمریکا را خسته کند که ترامپ دست‌کم محاصره دریایی کامل و تحریم‌ها را بازگرداند
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16412" target="_blank">📅 21:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16411">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79266b9c5c.mp4?token=kqrBYqo6T7cVgjTAyv3bdK9TTm46p4hGogtkpBMZpmbT66WoxF3srctBtBotE4c31tmy8HmSiqUQ66VMxzGsae5d8ZQG9qUcmrRQqXmXnZEMGdT49-R3Qpiyg88CEu4Piin174_CPKVCMTwKMk_G98mFeaN1gdI2tAIoD1QMX3frn50NI61KEFdfvzPXGjxyUazYF_BFzhuaFrS1mKm7DkwVIkjZoPUROcl1kTz0idxWVD8pyn-OQuykkCuGVRdniuNi41ntJrInsMW6lFBkjN7ySZyBPsq9ZRAOE7WXmbfrICZjLn6LNhNP3_ZW29LKZDKykKSM_lLCQsrSmkLvbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79266b9c5c.mp4?token=kqrBYqo6T7cVgjTAyv3bdK9TTm46p4hGogtkpBMZpmbT66WoxF3srctBtBotE4c31tmy8HmSiqUQ66VMxzGsae5d8ZQG9qUcmrRQqXmXnZEMGdT49-R3Qpiyg88CEu4Piin174_CPKVCMTwKMk_G98mFeaN1gdI2tAIoD1QMX3frn50NI61KEFdfvzPXGjxyUazYF_BFzhuaFrS1mKm7DkwVIkjZoPUROcl1kTz0idxWVD8pyn-OQuykkCuGVRdniuNi41ntJrInsMW6lFBkjN7ySZyBPsq9ZRAOE7WXmbfrICZjLn6LNhNP3_ZW29LKZDKykKSM_lLCQsrSmkLvbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمل پیکر علی خامنه ای در کامیون یخچال دار
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/16411" target="_blank">📅 21:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16410">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یورونیوز : در پی انتشار ویدیویی از زنی که با لباس زیر در پارکی در شهر یزد قدم می‌زد، مقامات قضایی جمهوری اسلامی از بازداشت عوامل انتشار فیلم و «برخورد قانونی قاطع و متناسب با رفتار آنان» خبر داده‌اند.
خبرگزاری دولتی ایرنا با متهم کردن این زن به «هنجارشکنی» مدعی شده که وی به «اختلالات شدید روانی» مبتلا بوده و بعد از بازداشت کوتاه اکنون وی به آغوش خانواده‌اش بازگشته است.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16410" target="_blank">📅 20:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16409">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">باراک راوید خبرنگار  آکسیوس:
ترامپ امروز با نتانیاهو تلفنی صحبت کرده.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16409" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16408">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آکسیوس: نتانیاهو به زودی در سفری ناگهانی و قریب الوقوع وارد آمریکا خواهد شد و با ترامپ درباره ایران دیدار خواهد کرد.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16408" target="_blank">📅 20:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16407">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تکذیب خبر نیویورک‌تایمز درباره ترور مقامات ایرانی از سوی دفتر نتانیاهو
حساب رسمی نخست‌وزیر اسرائیل در شبکه ایکس نوشت:
«طبق معمول، آخرین گزارش نیویورک تایمز درباره اسرائیل و مذاکره‌کنندگان ایرانی، خبر جعلی است. یک جعل کامل واقعیت.»
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16407" target="_blank">📅 19:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16406">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">صفحه‌ فارسی وزارت امور خارجه اسرائیل در X:
واقعا توی اون تابوت چی‌ گذاشتن؟
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16406" target="_blank">📅 18:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16405">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حوثی‌ها ادعا می‌کنند که با هواپیماهای سعودی در آسمان یمن درگیر شده‌اند، به منظور جلوگیری از فرود یک هواپیمای غیرنظامی ایرانی در پایتخت صنعا. حوثی‌ها اعلام کرده‌اند که هرگونه حمله سعودی دیگر، "با حملاتی به فرودگاه‌ها و منافع حیاتی در عربستان سعودی پاسخ داده خواهد شد."
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16405" target="_blank">📅 18:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16404">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آغاز مذاکرات ایران با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت
به گزارش جروزالم‌پست، منابع آگاه می‌گویند ایران مذاکراتی را با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت آغاز کرده است؛ مذاکراتی که در چارچوب معافیت موقت از تحریم‌های آمریکا دنبال می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16404" target="_blank">📅 18:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16403">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecb7IKwi-mXA2zqP8g9WDp2HjS-RUSMgejRMkZLtg1yjEpKWWdYOHi6vKJoWaHN22JevaA3A-gTmTa43_49vzWAlJcEcnQbWNTV9F0jrTTdP3UvpgVPlmR8MlKyE50N4PJrO_pHRkqeg3XFUFKLMD9FapcFuF8uJAQJCSw2qfIx_n-LU98DGgm2PXwR54vMUvdgi_r2n7hPP9X40a6YTH7I6yuRyQQeo6lugmE652OGkBc8Pu_WW9kX6ArtFvwLWMVJEypFrzOlqBZP_g8VBfvhEboarDm_99zIh90brAS5JWA52ELJe7qMLD2RvY0KQjsgVK0STE-NtwTQiJtCeiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: جان اف کندی بعد از من دومین رئیس جمهور خوشگل تاریخ آمریکاست
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16403" target="_blank">📅 18:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16402">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هفت خواننده سوپر عرزشی به نام های علیرضا افتخاری، محمد معتمدی، پرواز همای، مصطفی راغب، رضا صنعتگر، رضا شیری و حسین حقیقی ی آلبوم به اسم بدرقه برای رهبر ضبط کردن.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16402" target="_blank">📅 17:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16401">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الجزیره: ۵۰۰ میلیون دلار برای ترامپ، دسترسی برای پاکستان؛ چگونه شرط‌بندیِ کریپتویی/ دیپلماتیک اسلام‌آباد جواب داد؟
وقتی این هفته جزئیات درآمدهای مالی دونالد ترامپ، رئیس‌جمهور آمریکا، در سال ۲۰۲۵ منتشر شد، یک رقم بیش از همه جلب توجه کرد: شرکت رمزارزی خانوادگی او، ورلد لیبرتی فایننشال (WLF)، فقط از محل فروش توکن‌ها در سال گذشته بیش از ۵۰۰ میلیون دلار برای او درآمد ایجاد کرده بود؛ بخشی از یک سود بادآوردۀ بسیار بزرگ‌تر از حوزهٔ رمزارز که در مجموع صدها میلیون دلار دیگر هم ارزش داشت
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16401" target="_blank">📅 17:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16400">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2a30f1a3.mp4?token=fwCYR9GRSRtazz96-ZAEaRl1cLu9Lv0AW3MlieK_EKbWRSiK2abd2lY99evh49P-a2JNFVeHtP07Lou24mOFFYtuIuKuTGAB3R2kUSgztwad2PHK_HfvYY_vjqHnkP3HOEGsi-q906W5RQmOKWMahK2n3dDmjPNSBH0HoY_-19uBTVwXeQSTfftF6bCNfJ7D2xVUth6XHBQynGZUSasgJUejA0LoQJF3pNS-9vVChweKv8xi3LEmXj1rH9rc2MfmhuJqllgeQ1waZDOZ3O0Y7ncGC5iLrxScotwcLqz7znmd8zy-SMv_vCwIxjbSDl8xBtByqcS5621WHGoZGPqDwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2a30f1a3.mp4?token=fwCYR9GRSRtazz96-ZAEaRl1cLu9Lv0AW3MlieK_EKbWRSiK2abd2lY99evh49P-a2JNFVeHtP07Lou24mOFFYtuIuKuTGAB3R2kUSgztwad2PHK_HfvYY_vjqHnkP3HOEGsi-q906W5RQmOKWMahK2n3dDmjPNSBH0HoY_-19uBTVwXeQSTfftF6bCNfJ7D2xVUth6XHBQynGZUSasgJUejA0LoQJF3pNS-9vVChweKv8xi3LEmXj1rH9rc2MfmhuJqllgeQ1waZDOZ3O0Y7ncGC5iLrxScotwcLqz7znmd8zy-SMv_vCwIxjbSDl8xBtByqcS5621WHGoZGPqDwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f09f9f705f.mp4?token=p3XXqp1xkJE_P41cS232vBnz-nkpgj9_HE48cMBeqT3RYdap-YcljnZx48So12iPfpY7P2xdjjjrs0yqChuFhgIoZvcMygFrc6m3DDK7Ef5f6A8Lu6-SRR0nYQKjpgLhsowrfo4XASLJKFo4aVz3MliarB4eXkAWsgAV3o9VeLtiji8m1dyCVzPlGUJrzkEdCMLTZVoPa0upnTKubMWbPtcqlzR_nnPu2kR5tLGxVJSoASLZeMf1_iUGXZVjJTmg-bk_ZXVctabzvRUG2NZOOhQrFHx5ztGjIKR62oLXB8L5KCS1nJCwA-87tfbFHqs7-hy-WHOxV804wKgu2GqzWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f09f9f705f.mp4?token=p3XXqp1xkJE_P41cS232vBnz-nkpgj9_HE48cMBeqT3RYdap-YcljnZx48So12iPfpY7P2xdjjjrs0yqChuFhgIoZvcMygFrc6m3DDK7Ef5f6A8Lu6-SRR0nYQKjpgLhsowrfo4XASLJKFo4aVz3MliarB4eXkAWsgAV3o9VeLtiji8m1dyCVzPlGUJrzkEdCMLTZVoPa0upnTKubMWbPtcqlzR_nnPu2kR5tLGxVJSoASLZeMf1_iUGXZVjJTmg-bk_ZXVctabzvRUG2NZOOhQrFHx5ztGjIKR62oLXB8L5KCS1nJCwA-87tfbFHqs7-hy-WHOxV804wKgu2GqzWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور هادی خامنه ای (برادر کوچکتر سید علی) و وحیدی در‌ مراسم
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16399" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16398">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">محمد نعیم جُندیه، رئیس امنیت نظامی گردان شجاعیه حماس توسط ارتش اسرائیل کشته شد
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16398" target="_blank">📅 15:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16397">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">واشنگتن پست : مقام های آمریکایی فاش کردند اختلاف اسرائیل و آمریکا با ترور لاریجانی آغاز شد
واشنگتن برخی طرح‌های اسرائیل برای ترور مقام‌های ارشد ایرانی مثل عراقچی و قالیباف را متوقف کرده است.
در این گزارش آمده اسرائیل به دنبال براندازی نظام ایران بوده، اما آمریکا به این نتیجه رسیده که چنین هدفی از طریق جنگ عملی نیست و به‌جای آن تمرکز را روی تضعیف توان نظامی و دریایی ایران گذاشته است.
همچنین ادعا شده «ترور لاریجانی» نقطه عطف این اختلافات بوده، چون آمریکا به دنبال فردی برای تعامل در داخل ایران بود و با حذف او این گزینه از بین رفت.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16397" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16396">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">هواپیماهای مهاجم ، حریم هوایی یمن را نقض کردند، پدافند یمن درگیر شد @withyashar
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16396" target="_blank">📅 14:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16395">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16395" target="_blank">📅 14:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16394">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHPCjC0XgkUVxFVUu0RrFBgbgDQdIm0gzl-3lPHtthKmUIEIYIsEjtAzcXJ1yCjz1K8CHJyxGU5onBEfB1Z1M6EzAcj2cZtvK5Gz89ZlUYxOHWiIkMNbi3QC3zqId3IM8nros--0RddGVxolu4MrCPnLLjHEQWosH-cQBEnbd72i8H1bTh7oNNF9kkV80lAClAiUoUNLudR-e4DTjoQo4mJ5MUTYsoK__FJPGNPoSIBkwRwnrsiJffOvWXpQf2jO9B0epdai5zhDgP6pN-vFHKbQvb1LktJ6Arn-J8jZh5Yk37nltnY-hbZ2cvFNIfx-70Y6XZwe_7pJGQxCaLEI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فشار فروش آلت‌کوین‌ها به پایین‌ترین سطح در چند سال اخیر رسیده؛ به‌طوری که اختلاف بین خرید و فروش در آلت‌کوین‌ها (به‌جز BTC و ETH) به ضعیف‌ترین وضعیت چندساله خود رسیده است.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16394" target="_blank">📅 14:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16393">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAd7BubpLx3Vzb5fvBMYxS4R_hl2ia1WGGggb_SHvfcPM5lfIeBVucVdQKK_ODCNRi9wgYDNoFafk2MUDBaRMX0eXNKtPtHNb6Yy9-MO55vwSmY3-1qyK4oXJTJBPplYrw16TM9ydvL7C8-WORNGeIeEz9JTFl1Feiu-1mXQYegpx-6zJzsCnA2vibhQ0JbNwOARDT3rNgS24TsQ3RCOWqFlaHiHpx7CtwISs_YezQtu1X9wktUhDnGPad3bQtiz4oBCfhUosB0HBRNDb3KREH8caUOOEDouBIMEZO-ppENzyKeHug7qUbekKZSBSkcWc2VDRCSecFTRAAcWoStcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارزانی، رئیس اقلیم کردستان عراق، با قالیباف دیدار کرد
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16393" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16392">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تکلیف امتحانات نهایی دانش‌آموزان مشخص شد
رییس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش، با تأکید بر اینکه برنامه امتحانات نهایی و کنکور با هماهنگی کامل سازمان سنجش آموزش کشور تدوین شده است، گفت: امتحانات نهایی پایه دوازدهم از ۲۱ تیرماه آغاز شده و تا ۱۲ مردادماه ادامه خواهد داشت. همچنین امتحانات پایه یازدهم از ۲۲ تیرماه آغاز می‌شود و تا ۵ مردادماه ادامه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16392" target="_blank">📅 13:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16391">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">WarRoom with YASHAR
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/withyashar/16391" target="_blank">📅 13:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16390">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">1$ Tether 176,000 Toman
Brent oil = 71$
Gold = 4173$
BTC/USDT binance = 61,685$
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16390" target="_blank">📅 13:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16389">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNYMwWQF8zwKoT71scdQX4JGxgEoWD5RsVqGcwwz46de6CsuBDNBmjoI9mGMKVpBDzAjcdqyUKLqKS4x-SHV-YltoAKIANa7DY-rGpjByzubYU68dr__knIUt442QsZ5jVDxXTC0E1-d1ZQZyZrjAK5i5olpk2fEcoGS6o0_xkXo2C4DAeqylnG7iU5beI649dOIvf-NgACddDoDzGYZX6jHZCJkAIGancjwOlZYB3txHUp2TuD97bLqhPqmG2eiRa2ElUFkeSJbZHy1oRXx2vIzSC18Cu6pTyQqHETcB5ov-kzyTELtw9UlYNLmvKz4BLCWjHwDcPsnVam2h8TZlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس از تفاوت تابوت محمدرضا شاه و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای  انگار پرچم عربستانه
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/16389" target="_blank">📅 12:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16388">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فیلم مستند «جاسوسی از تهران» هم اکنون با زیرنویس فارسی
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/16388" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16387">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">۴ تن از نیروهای نیابتی جمهوری اسلامی عضو کتائب حزب‌الله توسط سرویس ضدتروریسم عراق (ICTS) در بغداد بازداشت شدند
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16387" target="_blank">📅 12:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16386">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dq1MYwFKXMr1-CKYjLaEYa-hdO_1rmplEJzR2ZYAxJZzWRdMbJG24LHxvPiPT2oTMJxJlqu6K5PZrGFNipP8W3dShhqF8ukSg-0Zvux9DRgGO0Xjk4ixaTeNO0gmUx2mreOmJb26Uj-fT4P_fbLs8ElKRbnEU6rFiV0t52gf4lM_WmgD16TNgs8FR2dPENlHIseuD9k94_OXTIXqajOYltpMk5WgPp9hdp6Sl7EcmBwAd8k857Q2RFOuRre6KWPDKaJnExZxW-3BGseIBDRxv7yKjfx6OFFGoBje_m-yKtn4DJv8b6iwgCMT0LN4lTBxIH50KmE03n1bZZwNOhOUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رادان : یک بمب گذاری ناموفق در مصلی خمینی تهران شناسایی شد و خنثی کردیم
با برهم زنندگان امنیت تشییع جنازه بشدت برخورد خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16386" target="_blank">📅 12:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16385">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پشت گوشتون رو دیدین، بیرون رفتن ما از جنوب لبنان رو هم میبینید. @withyashar بنیامین نتانیاهو: تا وقتی تهدید برطرف نشه ما از جنوب لبنان بیرون نمیریم.</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16385" target="_blank">📅 11:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16384">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puTRPvBDprfBYNrVxgg6UAS9YtIG0wECHHzSnsn7aT2-TQRVeZad9y__eb2ziqOhqKWm-Oo4Iusg27Lzrql5_XmT3monHPMQNmZ-66xPQvvTTi1U2IZZyvUe4n0X6SMCW2GA8N4dlUoaxR6aHDzA7i-IA70uL8hgq23bkZ_C2mdhw2HJF8rCEC7iGv-jenaEdmY_4h1FCqPUq11BlFrk2q8bGO2RaOSadwaCCtcW5Taw-0u-ICd-xPILreKR6dE8jZTqwSPfUDdepTlLsrQBHQVBLBRL9aPGXHHDktUeo4bOuSBFp7-MOa-XdF745GBdn98Q4JFbUw9d0Olxg_Bxag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس تصاویر ماهواره‌ای به تاریخ 7 تیر 1405، آواربرداری و پاکسازی اغلب سازه‌های آسیب‌دیده در جنگ اخیر در حال اجرا است و برخی از آن‌ها کاملاً پاکسازی شده‌اند
هم‌چنین جزئیات موجود در تصاویر نشان می‌دهند که فعالیت‌های تولیدی در بخش‌های سالم این مرکز با شدت بالایی دنبال می‌شوند
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16384" target="_blank">📅 11:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16383">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کل تهران در زمان خاک‌سپاری رضا شاه (۱۷ اردیبهشت ۱۳۲۹) جمعیتی حدود ۵۵۰ تا ۵۸۰ هزار نفر داشت.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16383" target="_blank">📅 10:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16382">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmTuMhcGDwKn-t-pn2CjwhRfGbca4w8LJdinA1BTautz4R5S3rU4Ydepmxc1moAD-HFbuz1lDaL_zunV0qyR1YpffAl77NGoyjpb4LsGRAnz_SdoRIjifuXBNmFE-2eUs7kssQF8d-JgoKH-fb9uVIlIf-1Knegfcsf0sOK_EGsNRum-SQnIKPRR_sDqX098wAlb9XSUO-E--IJKcv_X6ivMsOMFunsh_Hb5pZzs7W_Ih9-Hn0BVjg5_kE2qMWJFGq2c8FnUYVmcwP4m7dX_-ytlcZhR_HKvdglrPDH8oGrv5wM78sIB0Dy4n5XsyX0NE14I0oNxoTuqe-daDzhMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16382" target="_blank">📅 10:28 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
