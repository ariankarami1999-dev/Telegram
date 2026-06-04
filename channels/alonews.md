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
<img src="https://cdn4.telesco.pe/file/vqNeqp1PZYaEGBUuN1T9TxAN61XYEYIy-kTtLZI6okA7qNo1JNbbUfZd_fRA_W8jnnYl3wTTNuuYRykZK3yREXeDmkg3xweIVurJJKnpi1ZfB__qSNnPhtONemk3xYDTX1RpSBNBuybiQaL3Rlw7vVg1fR8VWqbQP_CDCO_VL1A6suAzfT43VNego_MwYnyk4furXUFqsV4Sha6NorSA2PrTLqvKH1VnCl3WfL9r8esiTacDphK3F4fX_w6g9cByVShI5nO2-G-DKkuMf4qKNkwn8MBBchWdN9mHvjxQelhM6LLvbM2fjr9ysl1HVNnaRb_n1AjAIH5aaeqOq2PS2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 22:44:21</div>
<hr>

<div class="tg-post" id="msg-125146">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
عراقچی: ما اسناد و مدارک بسیار زیادی داریم که نشان می‌دهد از آسمان کویت به‌طور منظم علیه ایران استفاده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/alonews/125146" target="_blank">📅 22:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125145">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1LzUjTLVIywwbm3Rz4KRkGz5TiF6lg2m6EaHdy-TjY2pmQdOdvVUsOeaUMl2CxhHIxxns67fR9_W8oeLvf7TuPFCYzDAinbI8Fodg8E35lYGshkzMcYOadEeYTL2MflhMp71k54_3QcSzcH5TQvOD5FBdRWnip_zHRFF86Bc4ZM7a3TsEIxBtBfSV2sKaK_n05lO3HmDPcXFnX66hKo5p0rTImK7f7K7pE9r1tJkvffmdvDJhgM5dPoEaiBHH9tHll1c7iiCpiKkfggXg_DN15gWK5on297oU4Q0qslKcbtGFK25IdFIibUw9wWyunZj62tVFC-xjTNg8DAnICrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) اعلام کرد که سربازی در لبنان کشته شد: سرهنگ عیتان شمئول لمبرگ، ۲۱ ساله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/alonews/125145" target="_blank">📅 22:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125144">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ادمیرال محسن رضایی:
معنی خروج از NPT میدونید یعنی چی؟
بهتره هرچه زود تر محاصره رو باز کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/alonews/125144" target="_blank">📅 22:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125143">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJ8V4dLGiW8GT4KWsNjS3-x13qb_lJxS2Kis5-QPPHwExB6rQoEh7q3zR_eNJ-rimodBf1mVGFT6M5jHNPSVBSXHJPPJlzP9_P1-xzZh39__GQYANbplwR2FmtdzIxlVejp0WnOVSY64GJ_VRHU9EG9Tj7EWfEBxhviEZxuIdhP5yP0aTiUp4X5HG3dSjVCJ_gbXYUjjGjlQclErDBgofgyqeVAz4cnxb7fcr1TaM4v__itzn221uLQeSMfYY8pKPGfe44UYpgatJbRnKU-Bw7vjgbRqbw6vVmvMwZeWmEHk1dju60ZS6Mwrih7Nzm9a33-1ah-_s6mHxiAsccbRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز:
حزب‌الله طرح آتش‌بس پیشنهادی بین اسرائیل و لبنان رو رد کرده؛ طرحی که می‌تونست روی مذاکرات گسترده‌تر بین آمریکا، ایران و کل خاورمیانه اثر بذاره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/125143" target="_blank">📅 22:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125142">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZlCjn47dfgwRRZ4KVBIjYyJ4wkfP6zmylpjl5iAvwXUIBF9yAK_AdbBtD9R_4nysAmzqIr6vrZysDK2-HFl1B3uTtc-bzQU_7Ki1xjZLfF8YkvICQ8J5z7Yjs8q8o32UNV99V37nBFsMFRhHC8N31_dhdbYSFt64ZFDmGgtGKfe7FYWlMPcWVK--EGYt6_QVbYr_hjgELI_k7vIt6R8JxKFDJisf36ZLFKaXVwxj-NTrxDt6e_2BjJLzdvlqw0nNOBn5j5yR_p0agZ-d59MZrSkionQlliBmUuncvDZqZ6FplOE2HQh88jiqgh8_lNhAFgkCGKtowll1Ey30z7tVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یغما فشخامی، خبرنگار: قضیه تجاوز گروپ به شهبازی بو داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/125142" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125141">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
عراقچی: رابطه ما با سلطان نشین عمان بسیار دوستانه و برادرانه است و شما شاهد بوده اید که در جنگ اخیر هیچ آسیبی به آن وارد نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/125141" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125140">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0bm4x8FRWqYPaJIN_1pdNfl7wGXTO4t2BG7qiwKmn699rx2PLVEchEXqXzMTOI91veNZjp9q_CHAli4axgRnDNV8i9mg47bEN3scbTqSQyQg6v6b9SUrdZK3mc6Taw9Qb4LQtSQTBVwFphJmQXl-cfznV7oeCgx57vkcmpDIzzrhAQmFZWqhToeZ9gVhrp8KpMdTgn4KlC_oqfDVmePPU9-u_yDcRUNR6lHzbQKNISfuh1X5p3Ry38ITAhjjt3CXzKYK6FyLo7yQnhAT7NaHg5jQIIFiJ8pxc9m9Zeci4oZIlWva1L6mcnRHvv0xbmDjWOSPOXi0JvpRrS4tmkihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: ایران و عمان مدیریت تنگهٔ هرمز را براساس معیارهای حقوق بین‌الملل تنظیم خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/125140" target="_blank">📅 22:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125138">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
پوتین: ایران یک کشور دوست است و کاملاً به ما اعتماد دارد؛ از اورانیوم غنی‌شده پس از کاهش سطح غنی‌سازی، برای انرژی هسته‌ای صلح‌آمیز ایران تحت نظارت آژانس استفاده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/125138" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125136">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a5d73a4c4.mp4?token=gIC_NWpRRMXUFy-84JCG_wobSeI9H0kQuRWXF_Cl4-qe8ypuN6qePxM9AmuzXzBhrXbCT5EnyiCfNRn6Knip7Qna83aaI_LW0m-BOJwk4T4KeGOr36HNt6hwYC2FNEt317RSeOqsetMNHhUI6csqNLbj0hRryjhS5gqHoS8wV8TY1YrvX20UNdvcVnYoaFV5dWZOsMgMBTHlbuQOzr1TbHwlSp0th2cEIkj4Clv9AmxsgV-BRCSFvb2p7Hn9vSEYR744HcjjIeAa9z5hilVPoViM5pv7dNOYz-wBYqZtRhtd0Mtcc05kHjMNqn8IesZqLdhcEkX2kF7wP98rR05rIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a5d73a4c4.mp4?token=gIC_NWpRRMXUFy-84JCG_wobSeI9H0kQuRWXF_Cl4-qe8ypuN6qePxM9AmuzXzBhrXbCT5EnyiCfNRn6Knip7Qna83aaI_LW0m-BOJwk4T4KeGOr36HNt6hwYC2FNEt317RSeOqsetMNHhUI6csqNLbj0hRryjhS5gqHoS8wV8TY1YrvX20UNdvcVnYoaFV5dWZOsMgMBTHlbuQOzr1TbHwlSp0th2cEIkj4Clv9AmxsgV-BRCSFvb2p7Hn9vSEYR744HcjjIeAa9z5hilVPoViM5pv7dNOYz-wBYqZtRhtd0Mtcc05kHjMNqn8IesZqLdhcEkX2kF7wP98rR05rIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین در مورد اروپا: آن‌ها به سادگی مایل به گفتگو با روسیه به عنوان یک شریک برابر نیستند، اما مجبور خواهند شد که این کار را انجام دهند. ما عجله‌ای نداریم.
🔴
حتی اگر نه زن باردار را با هم بگذارید، نه زن نمی‌توانند در یک ماه به یک کودک زایمان کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/125136" target="_blank">📅 22:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125135">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8hb8Q-fZCd3cgGjGWz8WL67iBRD5YvrZpBkX4XqpQuS6yt3UffLXJ9e5XpXFJMYoJITXNDvenu1jOKFQ9P8pQo-Mgq_ck3-XPsrYOJBnOybUS_rrx-XvT32wTX5HzX3Ms4KZt0gBsj8ValI_KjVULZNADwFewsAnjTWspFnSF3pC8CMUq7lw-sCjOhgwaeZnhMO1Rzez5MuDTwJHnWpnlHG6J2j3KZh1ad7MmVZXFRdVsdiM0Q_mdRTlwGDu53-qjCDmiVw4l1gPbcM18kt8vk4jdPpM5dQv7-naaGNi4iAAbwlc8m0xoSXW8SnxKAw3wmm4_Vpi-DnG0n4aj_Ilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایالات متحده در اورشلیم هشدار سفر جدیدی برای اسرائیل منتشر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/125135" target="_blank">📅 22:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125132">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XqDAUNlkCsq77_S1kY3XhGiz9g0y7nOHhUchGYL9KTRp03xjpKjRrQcIMOMb1NHFcwcRgeWwYzG7oVjyeOslnXa_8tGGWaxh8OXZD_UbbEfysGh4kVELsHhg4M5vQ7L8ZQfldBaUWY4Ml6fZ0sQCM2rxUGFhmia2JyMlLAPH0kVpFfmviFilRYIdOFRawbAuMwCQij0LzuPNDngHIPQY8kOpOHA9EKhrN7ZS9o7xBuxQyGf-qbnLQk9WvlB7px_uuCt1FqU0ZBTsjwkimp7BvL0NX7BC7Ho1w_9akIuumQ2nk2p8aqpfLrgBGNeBWPv6AkTQslmGtU-bTaRdik8-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S5YQSgV2LZ-HqtATi6B_zMioOAPpSkrLxRGCEangZVRoYb09yBviM_wPri_eP4bdl_EQpTh1HEiARM-4DxAuBLzRE6w1ojcSa18e5Q7uz5VbHIUvjkgHBP55tixeHw_6Y9KQ4BNYQl0Er7CeoJdj8KflkWotX6keSuUkTEmMlqt5-NHTc3cIeQSGtB_OqAIgpU_5rWdsvqmYb09Q1qX3tMrxKMg75jQX7cpkBfRXggir4tt5t4CJpOcrreVBJgP__ynBq4Jcw2cZ0JTKdQDHSU-by2pNmdbBP1pvL4Fi396PY3AcUwsGmm7Kh0p8QRVbDK6abllavd-0Ak2fu2tqwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
طبق تصاویر جدید ماهواره ایی، ایران علاوه بر تعمیر پایگاه های فعلیش، داره به طور فعال پایگاه های موشکی جدید حفاری میکنه و قبلی هارو هم گسترش میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/125132" target="_blank">📅 22:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125131">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ_f6jRIss3XnLjfkfH8H2gLpCJHslc1BTF0xRaT36uvYPcObfo45w5VrAd4jhliZmboQ9VJoT4ShXFdTvfV7xsnMsa-fot4qq-ABw3p2YyTQJejPkmJ3svEHFJrBk4HsBPFu4T_pGkRdl8pKmLttNVR3F9qEYvfuzzwwbjeN5ecTyuLY377zKb_KPKqig7Fln2DPRW7isxGy-AizO9Eczl65PDIZKdG9rxJhzasUSO9OB5_HUGFG_2KV_sfFHMIbMKGwoPTH10siTXlVVpssFeAgZ0iB9H3pnAmrm_WLAi8hi3xQThzDafz-lZz-pjfoi4IDfoxVCY4rkIDsSpC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏هواپیمای تهاجمی عمود پرواز AV-8B Harrier II  بعد از نزدیک به 40 سال خدمت از سپاه تفنگداران دریایی آمریکا بازنشسته شد. جایگزین این هواپیما F-35 در مدل B خواهد بود
.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/125131" target="_blank">📅 22:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125130">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5371cd0bb.mp4?token=ljH2HmVcAL8OiiOC3ihplDod6Yjg1zyxG-QOG269cL0e_Iwoh7hzWde4gVVOx0ue468EWe3RXgCXf8r4vIS7ecVt5__y6mEsr6npLqcI0e73VJ8Eli3Aaz97ckd8Da2oF1IoZ43QTpXe6Qyi4b5S7VRt6Odz_5NC_zxq4IiyXM_hKeNcqtZAZ1HpaDr_KnqnE5cPPa-SLhwBMoFHaI09wvkPu2184Bp_RK9Y9_4Q4HDQ6kGz3Om8DA6PJcXTWGCm55IwtQw8mxpURcfJKlhzsfdWGTQ0fnGXaES0f59ehC1ScEImFbb4haKrozcAu4LpV5z1CvPBsYjU99pPMebRWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5371cd0bb.mp4?token=ljH2HmVcAL8OiiOC3ihplDod6Yjg1zyxG-QOG269cL0e_Iwoh7hzWde4gVVOx0ue468EWe3RXgCXf8r4vIS7ecVt5__y6mEsr6npLqcI0e73VJ8Eli3Aaz97ckd8Da2oF1IoZ43QTpXe6Qyi4b5S7VRt6Odz_5NC_zxq4IiyXM_hKeNcqtZAZ1HpaDr_KnqnE5cPPa-SLhwBMoFHaI09wvkPu2184Bp_RK9Y9_4Q4HDQ6kGz3Om8DA6PJcXTWGCm55IwtQw8mxpURcfJKlhzsfdWGTQ0fnGXaES0f59ehC1ScEImFbb4haKrozcAu4LpV5z1CvPBsYjU99pPMebRWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آب زاینده‌رود به اصفهان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/125130" target="_blank">📅 22:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125129">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">🔻
بیست سال گذشت و حالا رسیدیم به ششمین و آخرین جام جهانیِ مسی و رونالدو. این آخرین تورنمنت مشترک اوناست.
💔
🫡
🙌
@AloSport</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/125129" target="_blank">📅 22:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125128">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ef0b0142.mp4?token=mbxufohc_CmA0J6JpkbUAUgbIwKCws36U2wPvuwVCHEgaZmAZZUlGaX71WadRTMTH6h391k_PtVieaAgRTFqSveyl0wXBuVa9Dl9eSk8sQS0C92T3Q5JGbvR_cwXT_Mhr_sU0EWxRwcJmI4pBv-SdT0GHKYNpbe7i9J_fuldyHrruwdtz9izx9_sJjTzLaeLrMA6IdNM4R0TJyi1rkBdyY3OdEa7krtZW0IcSUhAn5n2c2ZN6em0mlJcIlCXuYX3L3MppWiQwKaQSo3XOZVaZXyrdBBK8bOUnCKuPCQuc_l2fkx_4duouQc6J4OkV0YQgT_P1vo4trXdO_FYBfc5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ef0b0142.mp4?token=mbxufohc_CmA0J6JpkbUAUgbIwKCws36U2wPvuwVCHEgaZmAZZUlGaX71WadRTMTH6h391k_PtVieaAgRTFqSveyl0wXBuVa9Dl9eSk8sQS0C92T3Q5JGbvR_cwXT_Mhr_sU0EWxRwcJmI4pBv-SdT0GHKYNpbe7i9J_fuldyHrruwdtz9izx9_sJjTzLaeLrMA6IdNM4R0TJyi1rkBdyY3OdEa7krtZW0IcSUhAn5n2c2ZN6em0mlJcIlCXuYX3L3MppWiQwKaQSo3XOZVaZXyrdBBK8bOUnCKuPCQuc_l2fkx_4duouQc6J4OkV0YQgT_P1vo4trXdO_FYBfc5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام علیرضا سلمانی 28ساله
🔴
شامگاه پنج‌شنبه 18 دی‌ماه حوالی ساعت 21، با شلیک مستقیم چهار گلوله توسط حرام زاده های جمهوری تروریستی اسلامی پرپر شد. چه نازنین جوانانی!
🤔
عرزشی حرام زاده، به وقتش مردم شما را پاکسازی می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/125128" target="_blank">📅 22:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125127">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai8iHohtBVIQhPkSd459rXRaPvnWxWls03F5XVEjPT5NUgSDiHZSGAcYQd2uAbCM8f73x1GVHM_uJoXJnNXZNuYrKxWxsGmsMYr_p02FgkDpmgfDgUPYFzTVomdSNKdK5AnFEo0rvC_DeaH5gSt0mwgAg6QS14bWFGC8aNftnqVUdrmMhzDjipapRNCmpU27KIg4j6_71k-A08u1KrR7Z8pge8w8DpynyD4SuEa4E4o5wuu6vKCgg18DNjvV5O8lzwb6-BVf5gWB4LhwXiRlpUQq4DnUGI6NakwHjlPF5zkZJ2zJFF0iLHsm24W5XDmBxLZsnMH7WZ4TUDJDlae8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال حاج محسن رضایی:
اگر آمریکا غلطی کنه آنچنان تو دهنش میزاریم تا درس عبرت بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/125127" target="_blank">📅 22:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125126">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVeOt0MlM042XTFwHjEJwT73gbfS6d-jnx0Hzg-YinzD8UUjsOr-fu80DOQMAEbbn-VcicOz8VkpyIog9vsQHMDVKhdZWV2AzN8srNoCQbq9ZsgPhtqwdbUGnmG5RTjBJAS36a5EQsdvkkiDFbfxn-IbZDjFpfIeXP29lthESg0lk4kIKj5EsdGBMBsbQR_joAO8uqGaPqxbcOtqoSK88z8cwWbJEYZB-V9l5Y72EaBy9I-yYzHA0qEaVupwn0f1YaHYqQ7jIEMvf36GKKSGLgCCl6xKqYld5IiHvlsf8--bwRweDaIPRRwnUrbfPbrZYas9yHf541YUj1r_ny6EmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: ایران می‌گوید در تنگه هرمز هزینه خدمات دریافت خواهد کرد، نه عوارض
🔴
ایران می‌گوید به دنبال دریافت هزینه خدمات برای کشتی‌هایی است که از تنگه هرمز عبور می‌کنند، در ازای تضمین امنیت کشتی‌ها، به جای عوارض ترانزیت.
🔴
این کشور به دنبال جبران خسارت برای خدماتی است که در کنار عمان انجام می‌دهد، از جمله کمک‌های ناوبری، جست‌وجو و نجات، خدمات امنیتی و ایمنی و خدمات پاکسازی محیط زیست در صورت آلودگی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125126" target="_blank">📅 21:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125125">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پوتین درباره فلسطین: اکنون باتوجه به رویدادهای جاری در ایران و تنگه هرمز، ما فاجعه فلسطین را فراموش کرده‌ایم، اما این مسئله هنوز وجود دارد.
🔴
روسیه معتقد است که راه‌حل اساسی این موضوع، تأسیس کشور فلسطین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125125" target="_blank">📅 21:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125124">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه قطر تماس تلفنی از وزیر خارجه مصر دریافت کرد و آن دو درباره میانجی‌گری بین واشنگتن و تهران گفت‌وگو کردند.
🔴
وزیر امور خارجه قطر بر ضرورت پاسخگویی همه طرف‌ها به تلاش‌های میانجی‌گری جاری تأکید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125124" target="_blank">📅 21:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125123">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پوتین : روسیه می‌خواد با اوکراین از راه مسالمت‌آمیز به توافق برسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125123" target="_blank">📅 21:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125122">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ادعای رویترز بر اساس داده‌های حمل و نقل: صادرات نفت ایران به پایین‌ترین سطح خود در حداقل ۶ سال گذشته رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125122" target="_blank">📅 21:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125120">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQTos46FXPHuvvEGmRpT57i6IWuhkJe18eoP5XFFQnQklr2UpVcCu129GkMM5xVyZZDcY__oikd-KrCULgoGdx3HtRGEbN9o6z0YCaJLv1oqEBaOeiXp7EabVNvSUU-17AZnEl7Sl3Ty-XsIYX01D8LbtuzF-CfotZ-0sIsySPosZgeE2l31Gkon4r14d-U3fObq7u1iCAq7mCZEvceVCAUjZ7QSgayx4496VeCS2lkZhVIIuz3LeGAgw-rxFIFf7tNtos08tGDlsfkH0Nfw2uCzw_F90Nm4zCmc9v0q6SMO0aYplgqoUd0nIojO0MV8DMdIWb2al8BofnB9_Lvzgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8938050d74.mp4?token=siMszbgTsG7eskZaL_DiSi36MpuLRdQGiVdjS8WxdikxLL9D1MtdxBL0qroc3SetEbv0WTrPlBUn3HJzbqCRHDuhJPROZQrDAx-npojASkzwYTVMdrDJJrMSqxwFnkqZhf7a4nKHikPj820FFQ1xQIFykknTWC3YhyiRW0LpYrfClWMCoagPE0NIf0NNSG4ayBtEjl_-ZwdJd_F-oW1ege3Q_OGGQe9fsnlNSBp_UbwZDWIucJUY_jH3lZoG7ynIyLwU9xTNI2ZD2yXqZ67BeIx4_ggJxDfovtEWERx0_tzo68sHRxaVBIdTBtNnyu3tOWxDepC0jb5vRqMFcZ3_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8938050d74.mp4?token=siMszbgTsG7eskZaL_DiSi36MpuLRdQGiVdjS8WxdikxLL9D1MtdxBL0qroc3SetEbv0WTrPlBUn3HJzbqCRHDuhJPROZQrDAx-npojASkzwYTVMdrDJJrMSqxwFnkqZhf7a4nKHikPj820FFQ1xQIFykknTWC3YhyiRW0LpYrfClWMCoagPE0NIf0NNSG4ayBtEjl_-ZwdJd_F-oW1ege3Q_OGGQe9fsnlNSBp_UbwZDWIucJUY_jH3lZoG7ynIyLwU9xTNI2ZD2yXqZ67BeIx4_ggJxDfovtEWERx0_tzo68sHRxaVBIdTBtNnyu3tOWxDepC0jb5vRqMFcZ3_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صبح امروز، لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125120" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125119">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqRG2Sgiwj58IRiK7b0J3OKaIm0MRglcJDY_E0uxbhsHo2g_Nxs6ySGLpSGbX93M6nnAhN4-z1l1hAvAKS8eAxSbgBgjlWU8EqDqJXUzOXCUmv7UAtUP-Z51K-a3LJMAf7UHUBP_naWRzQaba5sisLKuBdOgCtAUey-JMSg5MYq8PRft_rTfnPHYkduGoSq0w-XfPQMY__kD6cjvvAIVtUfw4Vu6GL2kpnDh4yPkc-Et6qWF4Ih-kuKsA7VqFwce8zGC_zi3_DSvOd-jZ5uvmv_3hyBbFY-2Cxpo8T_uMrQZgTIRX2cW2hP8CUSt0mFgvKxOrcN_MERqm1Pa8e2caw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ چند وقت دیگه همزمان با محرم:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125119" target="_blank">📅 21:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125118">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/125118" target="_blank">📅 21:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125117">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UJtzl8hYdxMeFc_D-UoxyEMfUS5u9NcKOaJ6y1lmlSFyk6qqBe4vBnJCZT7u3OLKABRGQaRi8q6gGzBcXL2y8KUj6r7yHznOPmDdykHgEw16hy1buVR_o6qBhyWhlxtypd2ZXJgAmbqJO2lN2sp_lh7LAKwAcb0mFB6ta5YnCEsCpl07-XuVSBBdkWv2jmh5jZvt0VVB9XpBEAC6gQ6vGGcO7PqjM5-89YkWqBwYEq9AhBJJTjn9J4Zi00c-jl3fZ_EFQ8Kyl9ZMF9KMPF9ipB53DlYv2i_fuq4jT4bruQsZDgY0PJQqBoF-nMMbZJ_XjDSpAXjCJvndqnkOxjOhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/125117" target="_blank">📅 21:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125116">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: واشنگتن به تهران گفته مراسم امضای توافق با آنها در سوئیس برگزار خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125116" target="_blank">📅 21:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125115">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پوتین : روسیه می‌خواد با اوکراین از راه مسالمت‌آمیز به توافق برسه
🔴
ارتباطات بین روسیه و اروپا از طریق سرویس‌های اطلاعاتی همچنان ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/125115" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125114">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff210baa61.mp4?token=NrmKlJDjTWVcIuudesUT0xzG8ewXMXUmwvRSh_BQmqYizbc76G9ghoZdfVjKvYnjM4MH1eAn4zwpuqNX6HJmy_DcFTDbXmsS3Fmelv2-HMvFW4JQq3xNRbidnJAzL0x9arCN8kgx-Dq2iCJ4-2wefh2eIVa3UY6MGd8EF6yoVcoVlD4kap7TAI-fq3qaNGWRFQaxzTENIsOy6ctDsleMdoIlLVkAJsxT67gupoFPT7xbXGb47-mPgI0JTtBs2THcmA8jhbeQgfCONO7KHABW97_xY4QTEslzIJ7a-npDbcBWLxGuE8QxpNcc1Mjg8HTmm9xIcCZRJOKX0gzOomqGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff210baa61.mp4?token=NrmKlJDjTWVcIuudesUT0xzG8ewXMXUmwvRSh_BQmqYizbc76G9ghoZdfVjKvYnjM4MH1eAn4zwpuqNX6HJmy_DcFTDbXmsS3Fmelv2-HMvFW4JQq3xNRbidnJAzL0x9arCN8kgx-Dq2iCJ4-2wefh2eIVa3UY6MGd8EF6yoVcoVlD4kap7TAI-fq3qaNGWRFQaxzTENIsOy6ctDsleMdoIlLVkAJsxT67gupoFPT7xbXGb47-mPgI0JTtBs2THcmA8jhbeQgfCONO7KHABW97_xY4QTEslzIJ7a-npDbcBWLxGuE8QxpNcc1Mjg8HTmm9xIcCZRJOKX0gzOomqGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر روسی کیرل دمتریف گفت که روسیه فردا برای پیشبرد کارهای طراحی مهندسی یک تونل پیشنهادی زیر تنگه برینگ که چوکوتکا و آلاسکا را به هم متصل می‌کند، توافق‌نامه‌ای را امضا خواهد کرد.
🔴
او بعداً شفاف‌سازی کرد که امضا با یک شرکت مهندسی خصوصی است، نه مقامات آمریکایی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125114" target="_blank">📅 21:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125113">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
پوتین: ما می‌توانیم منطقه دونباس را کنترل کنیم و می‌توانیم به توافق بپردازیم.
🔴
یک چیز با چیز دیگر منافات ندارد. چرا فکر می کنید که این کار را می کند؟
🔴
ما بر ۸۰ درصد زاپوریژیا، بیش از ۸۵ درصد دونتسک و تمامی لوهانسک کنترل داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125113" target="_blank">📅 21:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125112">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: پیشرفتی در مذاکرات بین ایران و ایالات متحده حاصل نشده است
🔴
واشنگتن از تهران خواسته پاسخ خود را قبل از پایان هفته تحویل دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125112" target="_blank">📅 20:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125111">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پوتین: هند یکی از اقتصادهای پیشرو در جهان است که بالاترین رشد اقتصادی را نشان می‌دهد. این نتیجه کار سخت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125111" target="_blank">📅 20:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125110">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
پوتین : تلفات ماهانه نیروهای اوکراینی حدود ۴۰ هزار نفره
🔴
روس‌ها تقریباً تو همه جبهه‌ها پیشروی داشتن؛
🔴
نیروهای اوکراین هم تو این مدت حدود ۱۰۰ هزار نفر کمتر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125110" target="_blank">📅 20:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125109">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شرکت ردیابی دریایی کپلر: چهار نفتکش ایرانی با مجموع ۷ میلیون بشکه نفت، روز دوشنبه از تنگه هرمز عبور کردند که اولین مورد از ۱۷ آوریل در جریان محاصره آمریکاست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125109" target="_blank">📅 20:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125108">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
پوتین: رابطه دوستانه ما با چین علیه کسی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125108" target="_blank">📅 20:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125107">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYe82tconC7oZnG5qXuWFT1cDCZ5hwtKvw9rTTE-hsIg1u7c2OmGQegCOg1rp4END5MrRC4G1M8yVGpnhS55asAkKzPmcQyextxs6ksaBzjM5BumXkd9VSFqGrb9dYFvlPdngdioSzjYTcleAIG3Pqu83qPTDN7ILbnCeCpkuw4SZvr0T62u1Jt-AfcAeoYGK1tAQhc7BbBqjON9QUf8PtKt8Cb0eh5C5xDZTmPl_uur_BGxHDo267lHmC-unbrttU8QU962zQgYCppUlG4LN6uIN9X7FleQ-zDyQpLtfpaxCxBgWCd-B3lqb_CZOrt_3srkMNTD5Vlgl6gnt0QYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماجرا و محتوای این پست بسیار دردناک و ناراحت کننده‌اس، اگه بیماری قلبی دارین به هیچ وجه نخونین.  توی سنندج یه زن و شوهر از هم طلاق میگیرن، بعدش مَرده حضانت بچه هارو به عهده میگیره و میره یه زن دیگه میگیره. دیشب همسایه‌ها بعد از شنیدن صدای جیغ وارد این خونه…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125107" target="_blank">📅 20:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125106">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وضعیت آب سد کرج ، امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125106" target="_blank">📅 20:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125104">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea73f38f1.mp4?token=XTbA4RoTI4PKd8xDmkP1C_VI8sY72gQOm0m-WKslme5c092YARM3eZrM049K_yzgCurRpa9VNQ6nUb1ePwzyNHUcIKLJoKYDcsLt--_II24sWd4IbsWbrSaOnOxfemqDdJwq7Z5rRZB0QR_pck22zdUosRqK3eTqeqoWo1aU-RRHbuESg9_muzMvTf3mzue_S8LpE1PxyWYc5r0fiM1zROBjR1ZFtf117jE8lasQUssYgqGEcQkHFi55742KLIcc0v8WAcJm-2C-Gp9RAN2jqZY3OXKBZWhFAvyXjTM4GVMtIp-CoOpPH3katrsHLEzgQKLtb4yIbyI73LpJRCTcEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea73f38f1.mp4?token=XTbA4RoTI4PKd8xDmkP1C_VI8sY72gQOm0m-WKslme5c092YARM3eZrM049K_yzgCurRpa9VNQ6nUb1ePwzyNHUcIKLJoKYDcsLt--_II24sWd4IbsWbrSaOnOxfemqDdJwq7Z5rRZB0QR_pck22zdUosRqK3eTqeqoWo1aU-RRHbuESg9_muzMvTf3mzue_S8LpE1PxyWYc5r0fiM1zROBjR1ZFtf117jE8lasQUssYgqGEcQkHFi55742KLIcc0v8WAcJm-2C-Gp9RAN2jqZY3OXKBZWhFAvyXjTM4GVMtIp-CoOpPH3katrsHLEzgQKLtb4yIbyI73LpJRCTcEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به گزارش خبرگزاری فرانسه، حزب الله توافق صلح میان بیروت و تل آویو را رد کرده است.
🔴
دقایقی بعد، گروه شبه‌نظامی شیعه شروع به پرتاب موشک به سمت کریات شمونا و شلومی کرد که ظاهراً این خبر را تأیید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125104" target="_blank">📅 20:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125103">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgNW-0Yx112hP_k7NvL7tYyoTjy8aj1o9YHmZXRMIYVEmw61UbmrVRY7UrPd_7ehOMS3Vk9g2_Idam9u0Bs09oI9FznWGzcdILSpdJposF2ep2xlOorqK44saJaJtDIEcokySa_ID_l8T70RWL4oPsPtp2M6MSNk39FPHDhQbCIFuQZPpParjxzaBDv1WWSR9lFhkz6GXUOrG_JLawe8fph0rM2LbZ9mQa9wfiZ81MZ-C1KOEGZasGskLhdBItvyxl-4ESINn8_Tbfv3iV_2KjPQCK-11FdJiR-OlnU5sAg2XizhPFT_WRj8_NFOyXG7kawadDMBQzAwA3KbalskLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بسته بندی رایگان هم پولی شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125103" target="_blank">📅 20:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125102">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
رویترز: روسیه برای اولین بار اذعان کرد که تولید نفت این کشور در سال جاری کاهش یافته
🔴
این اعتراف در زمانی مطرح می‌شود که اوکراین در ماه‌های اخیر حملات پهپادی و موشکی خود را به تأسیسات انرژی روسیه تشدید کرده
🔴
آژانس بین‌المللی انرژی تخمین زده که تولید نفت خام روسیه در ماه آوریل نسبت به سال گذشته حدود ۴۶۰ هزار بشکه در روز کاهش یافته و به حدود ۸.۸ میلیون بشکه در روز رسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125102" target="_blank">📅 20:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125101">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f8643a124.mp4?token=vDwSqnVBpVuolHUdhf-xXjcFrVNmWZ5xlT8UyGQDwtktYY8DkfW7o_gKkbToxneYnp5IWCfcTLv4b5txt9ggfoo9qAk1UW_f2dD4RWrk-i0iqqk1Pw9nSbuoMBgKoG03SI18AJeqoMGuU5XebiqOXxTJh8_hDhhV7Bm-CTJrjHODsVMdG2bzLR9opBQtDfMg_CFnjhMzkknZOHpUqfJRt4RxMUmG8sdY6FkrUCP8fIOKMsGK42UBLJ5RXs_NJ7roAdjgC8Am5Hlhhc45EfQwB5qwMZ3mL6m9jWBDI4anlPfdCCcnkPXwnz-7P0iThu1syVWWptJlt0fc2lOMdEdTwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f8643a124.mp4?token=vDwSqnVBpVuolHUdhf-xXjcFrVNmWZ5xlT8UyGQDwtktYY8DkfW7o_gKkbToxneYnp5IWCfcTLv4b5txt9ggfoo9qAk1UW_f2dD4RWrk-i0iqqk1Pw9nSbuoMBgKoG03SI18AJeqoMGuU5XebiqOXxTJh8_hDhhV7Bm-CTJrjHODsVMdG2bzLR9opBQtDfMg_CFnjhMzkknZOHpUqfJRt4RxMUmG8sdY6FkrUCP8fIOKMsGK42UBLJ5RXs_NJ7roAdjgC8Am5Hlhhc45EfQwB5qwMZ3mL6m9jWBDI4anlPfdCCcnkPXwnz-7P0iThu1syVWWptJlt0fc2lOMdEdTwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران شهر بزرگ صور در جنوب لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125101" target="_blank">📅 20:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125100">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fc6a353f1c.mp4?token=rbNfMphflAnHgS3IwJltj_19uPRaZ5MA87auwSyZisedrUge58bWqZvnJ2tz4EmCN6UFnoG2c0nmcYp__KK5jDBlsOvGe1R1oFIyUlLu6xHpBT7WeqmepEM33V9rX_rzIfK5uhk1NsD5Rpq3kXwUVsI0HW1Pgmhx8_rDtL8CFSFMN1M4LFcMRbRlq7ZQt0F_Q74N3WOuN6C7A9tWmDbvKLeDwqbx7a1H2T5DOkAjFAVdPaRGCrfMi0mjGQuc85bkjUB2HPlwuaSrx2I81dq7qDgMpLssOlIUBLQ4k1SfHrbtaJmnUmLLxtLLaztQgZXLwN6EhCWGYNLxx4phjlYT8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fc6a353f1c.mp4?token=rbNfMphflAnHgS3IwJltj_19uPRaZ5MA87auwSyZisedrUge58bWqZvnJ2tz4EmCN6UFnoG2c0nmcYp__KK5jDBlsOvGe1R1oFIyUlLu6xHpBT7WeqmepEM33V9rX_rzIfK5uhk1NsD5Rpq3kXwUVsI0HW1Pgmhx8_rDtL8CFSFMN1M4LFcMRbRlq7ZQt0F_Q74N3WOuN6C7A9tWmDbvKLeDwqbx7a1H2T5DOkAjFAVdPaRGCrfMi0mjGQuc85bkjUB2HPlwuaSrx2I81dq7qDgMpLssOlIUBLQ4k1SfHrbtaJmnUmLLxtLLaztQgZXLwN6EhCWGYNLxx4phjlYT8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش‌ها حاکی است سامانه‌های پدافندی اسرائیل دست‌کم ۷ بار برای رهگیری اهداف هوایی فعال شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125100" target="_blank">📅 20:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125097">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEbVPekJfNolXa_SW971YFXyyfBKNcNPkRRA3RT8WOfeHDQC71_qmAYm-0ni2vrVRi9-H0K3wLILw53h01ySyI9LDdItoDC1c3vzhHlrdGgJC3jkmhvyiubFgP9dTlHQKbjn8miE9wONFG-m128Z1apFzPSun_kZ85lP3h7qOK6NxGde_l7sJDS0U9WG1u7qSZGLTn_QkiDtrsLnQUUdVqWS7bjhA0f4G0bNtxQyPLWPEPKGdsv0Zb45jrUE2NAoWwFDjQrcFuGD6x7rtSk--Fh4vzZ9l0AXchEVSZMy0n1YqOuiSnAb9PJK6AyRDZ7Do6DfE3DhY15BzCOfDap1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9e03683c.mp4?token=FNgj0iASMYDmvX9FcW9wBxNmRMe2UlBt5GDGdHSx2OQbkcdKVYuXYHL4A9x9VCJrF2K2V8CXGbAey5tVIZTBbKQaSmSeLLH697S_gyCswMXCfJd491aOv2cC_o3n5zPoZ-K5UO55ZDClat8Q-nxsBz7CMtow1XRjuLFW7Y_oVwt7dzU_Du0iG0dQx4E31ABe_vFNX9hXa6H2MLYXizNS5AtHySb_TJkQWJAv8CLOcyHjscx8Tzj7N5Y4EAn15HftLdOwLbQ_jXE9eYiJ-H-I0jf3Eh2RizjOREk2mRx9fVLmDjm60PtNsxEh43ObvWypjJd5cXaqkFWm827EMDSwUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9e03683c.mp4?token=FNgj0iASMYDmvX9FcW9wBxNmRMe2UlBt5GDGdHSx2OQbkcdKVYuXYHL4A9x9VCJrF2K2V8CXGbAey5tVIZTBbKQaSmSeLLH697S_gyCswMXCfJd491aOv2cC_o3n5zPoZ-K5UO55ZDClat8Q-nxsBz7CMtow1XRjuLFW7Y_oVwt7dzU_Du0iG0dQx4E31ABe_vFNX9hXa6H2MLYXizNS5AtHySb_TJkQWJAv8CLOcyHjscx8Tzj7N5Y4EAn15HftLdOwLbQ_jXE9eYiJ-H-I0jf3Eh2RizjOREk2mRx9fVLmDjm60PtNsxEh43ObvWypjJd5cXaqkFWm827EMDSwUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل: تو حمله به غزه چند تا از مسئولین ارشد امنیتی حماس رو ترور کردیم
🔴
عملیات دقیق بوده و قبلش هم سعی کردیم به غیرنظامی‌ها آسیب نرسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125097" target="_blank">📅 20:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125096">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
خبرنگار الجزیره: حملات هوایی اسرائیل به کوثریات الروز، صفاد البطیخ و عین قنا در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125096" target="_blank">📅 20:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125095">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
اکونومیست: حکام خلیج فارس پس از جنگ می‌خواهند نشان دهند که در خانه همچنان قدرتمند هستند
🔴
آنها تدابیری شبیه حکومت نظامی را اعمال کرده‌اند؛ ده‌ها هزار نفر اخراج شده‌اند و بیش از هزار نفر بازداشت شده‌اند
🔴
امارات، که میزبان صدها هزار ایرانی است، بیمارستان‌ها، مدارس و باشگاه‌های ایرانی را تعطیل کرده
🔴
فشار بر شیعیان و ساکنان ایرانی، احساسات فرقه‌ای که پیش‌تر در حال کاهش بود را دوباره زنده کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125095" target="_blank">📅 20:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125094">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrKAFgp7erCPNiEBqeOaA3AP8U5uwRamGeHeJQWRW3B45UF-pdf30PirWrxRNgLdjAfgOYu4WRYCFHY_TOrHNIQsYzyQ0v52RUBDD89PUl1UM0tTV6YanH_RS116kMgRRSZiUh1fX60rOlzLxHrAFi6hR8bKm5KPPXj7Kt6swCcOF0nVI-0iEbk38BU4Ei1AGpAk0snt0bg2cbXz7onayc5SFunRGs4f569MQRtuQSHLk4xTcGalZaX5RY1-YD7ZYPcFA0YS66SiLdiKr_eC9YqsrbTPMajewnq5qQxOChH6zTvDAvQ9lE73VHp2YSoCx85zTpy7CUnXNgxHR5PXkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جان بولتون، مشاور اسبق امنیت ملی دونالد ترامپ و یکی از منتقدان سرسخت او، با وزارت دادگستری آمریکا به توافق رسیده است که به یک فقره اتهام نگهداری غیرقانونی اطلاعات طبقه‌بندی‌شده اعتراف کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125094" target="_blank">📅 19:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125093">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر خارجه روسیه : غرب تو تلاشه تا روسیه رو نابود کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125093" target="_blank">📅 19:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125092">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فارس : آمریکا برای تبعه خود در کویت هشدار امنیتی صادر کرد
🔴
سفارت ایالات متحده در کویت از شهروندان خود خواست که احتیاط کرده و دستورالعمل‌های مقامات محلی را دنبال کنند.
🔴
علاوه بر این، سفارت ایالات متحده در کویت سیتی تمام خدمات کنسولی را به حالت تعلیق درآورده است.
🔴
واشنگتن همچنین از تبعه خود خواست که از اعتراضات و تظاهرات در این کشور دوری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/125092" target="_blank">📅 19:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125091">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
واشنگتن: ارتباط با ایران از طریق میانجی‌ها ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125091" target="_blank">📅 19:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125090">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
خبرنگار بین المللی امور خاورمیانه:
من کاملاً مطمئنم که اسرائیل در مقطعی به بیروت حمله خواهد کرد، زودتر از آنچه فکر می‌کنیم، سپس ایران پاسخ خواهد داد و آتش‌بس پایان خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/125090" target="_blank">📅 19:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125089">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
مدیرعامل مایکروسافت: دیتاسنترهای هوش مصنوعی جدید ما به‌اندازه یک رستوران آب مصرف می‌کنند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125089" target="_blank">📅 19:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125088">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihcEe-c_oYix9qDofAFuv4ghnO5muWpZEBu2olsZuYIBO4PTidti_NYUjX1ViwPI5VYTzFhYXXC4MlnZASx-Q2yHImyk1sMX8e7hg2S1IwHrg8pDFGUvQo8dnYEWFaXMuXmhtgh0nIbaBvxR1y3b8TuSnQHFIQXItcuKbsHDcjv2hvEF9jy-seIC87mN4PGQxjqpV8xmiWxKKeOZWTqowOphl1Cn7GfMw_mCscT1Ix0z4mcKTkPdNmaTpWqjO6r6AUOMMbVgdPBwoGMggr_AlRqZcjTXscTuoRUIVqpTBDn_Bh3o-E0wfpa603Lk7y2DriQOUt6c_QhgIWJExT66tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۵.۰۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125088" target="_blank">📅 19:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125087">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سنتکام:۶ تا کشتی رو از کار انداختیم، ۱۲۷ تا کشتی تجاری رو مسیرشون رو، عوض کردیم
🔴
۳۶ تا کشتی هم که کمک‌های انسانی داشتن رو اجازه دادیم رد بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125087" target="_blank">📅 19:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125086">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/alonews/125086" target="_blank">📅 19:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125085">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dJ0VaugUsnCQO3VmRDaFm921NPM0DzemhrV1NZbENGoQ79DfMtXsI-Zf4SpKLFQSfrzvEaqJgZZb8thK8cegmLuL6yG8wbfClp1fXZo2mO9jSCevVzwZpd31c6b7FsICz2aW_o9GKPQPtFVdS5SvMtMWXd0M3-FeTu1SWLhbH7frZgYJ1IqyGH1DwxCf9ZtkeUQtl9kdgi44-1yRAn8VX_7KFD1sBxzmoigo8jbcGSM_4iz9ZRIjZLAkdg2lDGx3NcO_iAQ6k7YtyGaNiD3Xui-KxZPJzh_Mx7C8LdNO1V4UTmJlXwWMe_Jc_-XY5iilD-KL7BkIdIbSINe-8cjd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/125085" target="_blank">📅 19:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125084">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0bb3a1fb3.mp4?token=GpGq5QapRz3j9yGE_Pj9gmUJl0bJgWod7wSBBLz3B0miONO7LT-59b62hnHADDUczhIFmg-lKiw3VDMd4gkuI_FKLqtt51Rzu0Tnqv7BEqKRGp8mWK9Z--wUuRLQXsgbSv6rD-gi_ZHAWMG9TJEuwhcLM8eZacg9LIUmIJqx_TycDeB2XBIZ2u1hn3zF0XuDhNb8mABOTMQqXE8XRvZNwJ_PgIc5vXt1y1ZXX_RlmNcdSZVWIxlUSPw1TLCG4dhKZLXxUvvcUah344S8UQVohOF3rY6taeWeDhc5zoVmZXucIJKzLXyrhtPu2lx12YWuTY6V06ZqSLd6RUBaBHhdNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0bb3a1fb3.mp4?token=GpGq5QapRz3j9yGE_Pj9gmUJl0bJgWod7wSBBLz3B0miONO7LT-59b62hnHADDUczhIFmg-lKiw3VDMd4gkuI_FKLqtt51Rzu0Tnqv7BEqKRGp8mWK9Z--wUuRLQXsgbSv6rD-gi_ZHAWMG9TJEuwhcLM8eZacg9LIUmIJqx_TycDeB2XBIZ2u1hn3zF0XuDhNb8mABOTMQqXE8XRvZNwJ_PgIc5vXt1y1ZXX_RlmNcdSZVWIxlUSPw1TLCG4dhKZLXxUvvcUah344S8UQVohOF3rY6taeWeDhc5zoVmZXucIJKzLXyrhtPu2lx12YWuTY6V06ZqSLd6RUBaBHhdNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال ،محسن رضایی: برای ترامپ ویلچر ببرید!
🔴
از این به بعد آقای ترامپ را باید روی ویلچر ببرند که بتواند آمریکا را اداره کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125084" target="_blank">📅 19:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125083">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
حزب‌الله به دولت لبنان اعلام کرده که توافق صلح لبنان و اسرائیل که با میانجی‌گری آمریکا انجام شده رو قبول نداره- AFP
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125083" target="_blank">📅 19:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125082">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بلومبرگ، به نقل از منابع: بریتانیا و فرانسه برنامه‌هایی را برای یک مأموریت مین‌روبی چندملیتی در تنگه هرمز نهایی کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125082" target="_blank">📅 19:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125081">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
گزارش گروسی به شورای حکام: آژانس نه اطلاعاتی از ایران درباره وضعیت مواد هسته‌ای اعلام‌شده دریافت کرده و نه به هیچ‌یک از این تأسیسات و مکان‌ها برای انجام فعالیت‌های راستی‌آزمایی میدانی دسترسی داشته
🔴
حملات نظامی به تأسیسات هسته‌ای ایران وضعیتی بی‌سابقه ایجاد کرده
🔴
انجام بی‌درنگ فعالیت‌های راستی‌آزمایی آژانس در ایران مطابق با توافقنامه پادمانی ان‌پی‌تی ضروری است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125081" target="_blank">📅 19:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125080">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2dff1427f.mp4?token=CM0w1HDvt2Nc-RPaY87nvTfwlBSeQIuZZR0wLtYGeTnFfo_TNf-xt9XKwVAUmy1zDg3xUVx_1qUp5twfCVUJYRQnPxoSbmJG7hdyBp6RFIFtIQwJBWMXDtqQD5ldW-UayRlfkpFtVrSRgeby5lmvho_UQqSZkWjht-wkduYWRKeOA2Qt_wc46TlZjO65T0u_kaOdO2ODfkjvu0UOXnvoWLGOA6rc-dnFqT49yH0ycjZMi4NuiQLYWqOqB5ah4aHBvnlmqZivC1tnoUoNNI8EZZZWzY_nWWiZUSESzJpvctIlScilBWOvC4ERUIIAKencxt7yR_MtPAbZfvfu8_M8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2dff1427f.mp4?token=CM0w1HDvt2Nc-RPaY87nvTfwlBSeQIuZZR0wLtYGeTnFfo_TNf-xt9XKwVAUmy1zDg3xUVx_1qUp5twfCVUJYRQnPxoSbmJG7hdyBp6RFIFtIQwJBWMXDtqQD5ldW-UayRlfkpFtVrSRgeby5lmvho_UQqSZkWjht-wkduYWRKeOA2Qt_wc46TlZjO65T0u_kaOdO2ODfkjvu0UOXnvoWLGOA6rc-dnFqT49yH0ycjZMi4NuiQLYWqOqB5ah4aHBvnlmqZivC1tnoUoNNI8EZZZWzY_nWWiZUSESzJpvctIlScilBWOvC4ERUIIAKencxt7yR_MtPAbZfvfu8_M8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی که از لحظهٔ بمباران مقر سپاه پاسداران تو نسیم‌شهر تهران درجریان جنگ ۴۰ روزه منتشر شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125080" target="_blank">📅 19:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125079">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Knq7nOUsa23ua57slfkZYEfqvC-BNbtzkwGPCnLlobdmMMxTT_TgtpXvUrEAbc82aV4yoA05bL4j3qvZufcn26tpS0MBRqCSmjYKUq2x2IOsQxNkDVlVvulF2S-qwXLYEI1weuy-MFE8CxBjwL256g7ZNC75miItB8ZdK2xSypUUi3V_EHmlumocbv7XDhCmofi73e_G5beEJo6SB4xaGB_YJgVsAlf5LptaidyK0z7WA0SuwR2LkBA7AWrFJ_3sESqmmMuKJ5jFeTJSDQ68POdo8WT6cLqISLWPsfqet5ElyHSAMydWHFyoiZ3w_wNxjtTsrbcqvRt4VjPgWKu2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125079" target="_blank">📅 18:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125078">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خبرنگار وال‌استریت ژورنال: یک منبع نزدیک به آژانس بین‌المللی انرژی اتمی می‌گوید هیچ فعالیت قابل مشاهده‌ای (از طریق تصاویر ماهواره‌ای، یعنی در سطح زمین) در سایت‌های هسته‌ای ایران که سال گذشته بمباران شدند، در ماه‌های اخیر مشاهده نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125078" target="_blank">📅 18:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125077">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL4CWyZYjXpyenibXznmKoZMS2h02j9eQPXW0NzAgeeWOTQ3uL4rC3BH3E3jB2pN_csHe6kU8r7ki0mSIM7EGmG1uwZ8DRa55UaZnwf43w7UAtM7Py-T8AUAZYb2Ke4svHymvevf6X06VY65FssL6tbIrMQvXKChs8_Ztqm1SH3nkS4zVE8UhNBeu2sniOADztfnCnqFWVYHnUlyI7kdRYOUDiUn7GdPWxsREuwSOi4AQeeC3jfPj7PBT_ByrNVcswnZM2VQmzJLbU9oUtw0UbQtyt_lY1Us4w0GXikmueTJl_YWcxUV8Hg-qedr2f_A1Z_wu1PRXXdEMnTTVfJT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
آقای جدید از آقای قدیم سختگیر تره
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125077" target="_blank">📅 18:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125076">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvuu1x0jfNk3XjpVqXj8MsC9JIxJaKgiQGdou8Ym7_6jHUDS2nK7vjyb_szHy8tbrw6zAi92-3GxRx1ILEZlu0TTP9MttULghl-_tNJVxtBpM113swrzawXeMpe_4n_1u7uyDAZOnRLSrZxYxC2TtAYyvNS5T7jQshOWLaAM4pvEe5fParnLAARJksqXhZkoAR67awuozb9ZXWn_K_9BnArEyd_TSzr2NEyx1IXmRRRlY8sv_mNEV3mN1sJvJ4_9ZSZLgtLVkXijX7SufCSlyLGuPMZ5Y0womkKYGOz-h9gfwahNjq-QEeAkKCthZ5bcNhYG0XDPMRH-m96EWzu66A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم کارشناس صداوسیما: به نظرم جنگ تموم شده و دشمنان دیگه جرأت حمله ندارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125076" target="_blank">📅 18:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125075">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7OlSbAyWQ2PMfOyIzLyK2G36i8IeuioHBftA6Bce7NJJQ6wwNvhAvkEgrC0kuZREmFLGzntvcUcr787U5cyKGGRxd3u8nqPeORV_oMvR1aVX654KMFnTo8cIzCgegTIBefvBv0z_xBaUnJdJPDOSHBSya1N2w3rWdmPZKP7IcdC5lGkSNXZMwwljeKUVjcoA0V07xx1xu64Dv08FvHYQSe8vER3iooGI1JhB-uZgEOrg1M7Y11KB3AVSkQKvEgf4lASmc46b4FEONh_D5SVotHNKY6HcHjp7lO8PCv7AcpgUyqZVZb9JHkxrT-y-oK27uZ2JuLAMkmyvuK9gNNGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
🔴
برخی زمزمه ها از رفع فیلتر یوتیوب نیز درآینده نزدیک حکایت داره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125075" target="_blank">📅 18:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125074">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYtyuRv5FMCcRESmeQSmwsalu8zRd9KNQMTKrkihJPXDouZDUvjqGRV_GAOha8bM5xoRN_azXiwj0T1g3sc5VyhjX25-acz0YDxOdfQb4lL52GAKS_XeRUUUUXcEMb_oQVYH01L3JmxTQlUlcOEuWQ5f1XvMZePPpH7ph5S45yDsxcdejJbeZ4jp6dWItTbKHc2LP-wi9oNkkw1KAIlUC394rMgenGqy_qp7DWML91LFR5vwIlNMzw3HkUGwe_sxmGxlqs4tr13SRQdJx0JZ_sYkU7zy2bstC84yve5in1BrqU0DB47ES875MjbILwTS0oquY5br4q9s9hnsuMaLLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار قاآنی: اسرائیل باید به نقطه قبل از شروع جنگ ۴۰ روزه عقب‌نشینی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125074" target="_blank">📅 18:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125073">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه آمریکا: ارتباطات با ایران از طریق واسطه‌ها ادامه دارد و پیام‌هایی بین دو طرف رد و بدل می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125073" target="_blank">📅 17:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125072">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سپاه: اسرائیل فورا حملات خود را متوقف و از مرزهای اشغال‌شده لبنان عقب‌نشینی کند
🔴
هیچ آرامشی در منطقه بدون عقب‌نشینی از مناطق اشغالی لبنان برقرار نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125072" target="_blank">📅 17:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125071">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=v-dxUilDhSVhkYK6FMpXgspNg0gTjNIuynP0QFLhjxhl65QqEXn1C0B7m0fNob3YQjm2QXqLC9qqSr2EkF-2hGmcwKAMRCee266jQMl8pKYqlpbtyrGL-dYeV-DPvg0bhpiLWchCpVeK1zvnWif_DlGb3BlJNNHD0ap2ggOWgz2Qv19Y2kmB4Bd5fSiuenEEqOcSaYnhqJgDIpz0buRfLmu3ggWk3wld62MHMlUaoNonPxZL6ZjV2Ku_56QnSKrHBGlYcSTbXwrGgIFrDSCbtVCISDaLxZA_CapWLKPUgY2xCxbcu2GuzYTef-Y6XfcUkDIeinHUyKmNyRL6dzdHuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=v-dxUilDhSVhkYK6FMpXgspNg0gTjNIuynP0QFLhjxhl65QqEXn1C0B7m0fNob3YQjm2QXqLC9qqSr2EkF-2hGmcwKAMRCee266jQMl8pKYqlpbtyrGL-dYeV-DPvg0bhpiLWchCpVeK1zvnWif_DlGb3BlJNNHD0ap2ggOWgz2Qv19Y2kmB4Bd5fSiuenEEqOcSaYnhqJgDIpz0buRfLmu3ggWk3wld62MHMlUaoNonPxZL6ZjV2Ku_56QnSKrHBGlYcSTbXwrGgIFrDSCbtVCISDaLxZA_CapWLKPUgY2xCxbcu2GuzYTef-Y6XfcUkDIeinHUyKmNyRL6dzdHuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/125071" target="_blank">📅 17:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125070">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ab6bf7d8.mp4?token=C4mWyklxzuo_F8Xb-Biw2vzD9oeISHXLhPDILPfF2qt7wgLLrA5yzBEWuk8NdCr0NI35qIoFnsD_je8T_IW2GmYypTli5cJABHXd4llDF7Q1Sc5Q-QgnZRWriecIyG3X28sl3uTvIGgLX9qtkGKTE03SCueJxMxtmOxDwBFwdUHctCxyL9dp1mP602v_4MWd3M0sDBxf9UiWA3z2Tq84t9tTtFxSa2OkKtqDX9kDECGwxxtjiNI09QXrZIUMQkAteqvztNN_q7baE2swZe_66gp6bf9WlPGqyc2r1brVOD4DEcpL_ONDMcxY8ko9OB_e40IY7sPVSdT1dGoDWTAhdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ab6bf7d8.mp4?token=C4mWyklxzuo_F8Xb-Biw2vzD9oeISHXLhPDILPfF2qt7wgLLrA5yzBEWuk8NdCr0NI35qIoFnsD_je8T_IW2GmYypTli5cJABHXd4llDF7Q1Sc5Q-QgnZRWriecIyG3X28sl3uTvIGgLX9qtkGKTE03SCueJxMxtmOxDwBFwdUHctCxyL9dp1mP602v_4MWd3M0sDBxf9UiWA3z2Tq84t9tTtFxSa2OkKtqDX9kDECGwxxtjiNI09QXrZIUMQkAteqvztNN_q7baE2swZe_66gp6bf9WlPGqyc2r1brVOD4DEcpL_ONDMcxY8ko9OB_e40IY7sPVSdT1dGoDWTAhdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سه تا موشک حزب‌الله که به سمت شمال اسرائیل شلیک شده بود، رهگیری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125070" target="_blank">📅 17:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125069">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/45c2d0b1d6.mp4?token=e9Cr3-NWIlpo3nr0MWX5bYC0wnANVoug-Q09QSD4SpVES_DE3gPzv-HYtdlc5kR72s1YW-2ZdOIfM8EFoAWkxaFxZOdDy5hUxhEZv6E4eGCLzfAAYIQclyJwN9ByU8X9bXIA8MZCNseHFgE2xOQ7HAVwQV0bIM4GzVr3jwG7QAB-eilYI0vKukvIJqZw7ASv5RNqAoQsDQZ51ktLONbwiNkv0-3VHXB7faIM6Ip3M1uhh65bT268p_6JK9DvnWYeFS1Eb_oImPIjeDsDu2pgYzJZoxbCofwMpdEEWRMMh_hE_9fQzAYpR236XS68JqjuEKBWqo2XvFoqlaA859H3cw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/45c2d0b1d6.mp4?token=e9Cr3-NWIlpo3nr0MWX5bYC0wnANVoug-Q09QSD4SpVES_DE3gPzv-HYtdlc5kR72s1YW-2ZdOIfM8EFoAWkxaFxZOdDy5hUxhEZv6E4eGCLzfAAYIQclyJwN9ByU8X9bXIA8MZCNseHFgE2xOQ7HAVwQV0bIM4GzVr3jwG7QAB-eilYI0vKukvIJqZw7ASv5RNqAoQsDQZ51ktLONbwiNkv0-3VHXB7faIM6Ip3M1uhh65bT268p_6JK9DvnWYeFS1Eb_oImPIjeDsDu2pgYzJZoxbCofwMpdEEWRMMh_hE_9fQzAYpR236XS68JqjuEKBWqo2XvFoqlaA859H3cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ماجرا و محتوای این پست بسیار دردناک و ناراحت کننده‌اس، اگه بیماری قلبی دارین به هیچ وجه نخونین.
توی سنندج یه زن و شوهر از هم طلاق میگیرن، بعدش مَرده حضانت بچه هارو به عهده میگیره و میره یه زن دیگه میگیره.
دیشب همسایه‌ها بعد از شنیدن صدای جیغ وارد این خونه میشن، می بینن دو تا دختر 7 و 15 ساله داخل دستشویی حبس شدن.
با اومدن پلیس و اورژانس معلوم میشه توی این مدت پدر و نامادری‌شون تا سر حد مرگ شکنجه‌شون میدادن!
یکیشون فکش ۳ ماه بود شکسته بود، اون یکی دست، پا و دنده‌اش، شکسته بود. رحمِ دختر بچه رو سوزونده بودن!
به بچه کوچیکه انقد غذا ندادن مثل چوب بستنی لاغر شده بود. انقد موهاشون رو کشیدن که مو روی سرشون نمونده!
کل بدنشون جای سوختگی بود. دکترا گفتن هر لحظه ممکنه بمیرن انقد عذاب کشیدن. پدر حرومزاده‌شون بهشون تجاوز کرده و برای اینکه معلوم نشه آبجوش ریخته روی واژن دختره!
این پدر و مادر امروز دستگیر شدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/125069" target="_blank">📅 17:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125068">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">امروز عراق با اسپانیا بازی دوستانه داره و جمهوری اسلامی با مالی
😐
@AloSport</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125068" target="_blank">📅 17:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125067">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57af1916b1.mp4?token=k3TfXSyIa7kLv8L3N313tjUCpeC3eFPPiTN7ZOU1CbLHeFIXynXD_F9RXjrySixskKLI3Qg29kO2yuAY90B9efYG4ISS69ck2YSBUkz8vAoB9ubNVEsjuArAYU1tZxuVf4_Pl3_hb8xcXxFiVIkMtc0mkqq26Vx_bD9WCjb3DnRR5ivNIaYmntolHtuEhtmv11RH3ENCT5n5qBJXnahpJJR6pUWv5ipxqC0fYRFZyK27dhVuPKbZUcmeh4dXRgA9hA13zNpp_QJ1BaRIp_X5cTQ9TbRk-yRCcmkjcNELdwWINk2vHqofDCFxexH1s1HKhpASAmQCiTpgsnFOu6jF3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57af1916b1.mp4?token=k3TfXSyIa7kLv8L3N313tjUCpeC3eFPPiTN7ZOU1CbLHeFIXynXD_F9RXjrySixskKLI3Qg29kO2yuAY90B9efYG4ISS69ck2YSBUkz8vAoB9ubNVEsjuArAYU1tZxuVf4_Pl3_hb8xcXxFiVIkMtc0mkqq26Vx_bD9WCjb3DnRR5ivNIaYmntolHtuEhtmv11RH3ENCT5n5qBJXnahpJJR6pUWv5ipxqC0fYRFZyK27dhVuPKbZUcmeh4dXRgA9hA13zNpp_QJ1BaRIp_X5cTQ9TbRk-yRCcmkjcNELdwWINk2vHqofDCFxexH1s1HKhpASAmQCiTpgsnFOu6jF3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویرانی در تبنین، جنوب لبنان، پس از چندین حمله هوایی اسرائیلی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125067" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125066">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/125066" target="_blank">📅 16:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125065">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LCTg3RSJjPrdo1rlRcUJm8j7W3t5m3ujdVyHdv-aPK1hVn33_NgQ2u317YP_B7XSYbato3an0ZD85JCrLTHFkPG_dTMVZnwHySJtAZGusneq0QsEhFaizuWHc9u-dSXQ5kzRRFTQ_ewHmKeYzvZgN-_mzn7pq6XMuG1MvR73SXQeIqgqVadl3IrBqPAIjfhXZWhZu6aOQ5m2YNU4sNYFjhjPuskiqqHUrORjlTPaFoHR6aqG3FcnGfNXE5hJfZi_9YO0p0G18_IlzyUZ_gkJfNN_YCigXyGNgo3IwcJMmggDsRCoarJWB0ilvk3qvuQ8SK30eCFNeBg2NQYq1LepSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/125065" target="_blank">📅 16:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125064">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
الجزیره: قیمت نفت پس از توافق آتش‌بس لبنان و اسرائیل کاهش یافت
🔴
قیمت نفت پس از توافق آتش‌بس بین اسرائیل و لبنان کاهش یافت، زیرا امیدها برای توافقی گسترده‌تر برای پایان دادن به جنگ آمریکا و اسرائیل علیه ایران افزایش یافت که می‌تواند به بازگشایی تنگه هرمز منجر شود.
🔴
معاملات با احتیاط انجام شد و کاهش قیمت محدود بود. قیمت معاملات آتی برنت ۱.۱۴ دلار یا ۱.۲ درصد کاهش یافت و به ۹۶.۶۷ دلار در هر بشکه در ساعت ۱۰:۲۲ به وقت گرینویچ رسید، در حالی که نفت خام وست تگزاس اینترمدیت ۹۰ سنت یا ۰.۹ درصد کاهش یافت و به ۹۵.۱۲ دلار رسید.
🔴
دو قرارداد روز چهارشنبه حدود دو درصد افزایش یافته بودند، پس از آنکه خصومت‌های تازه در خاورمیانه، از جمله حملات ایران به کویت و حملات نظامیان آمریکایی در نزدیکی تنگه هرمز، روی داد.
🔴
جان ایوانز، تحلیلگر نفت پی‌وی‌ام، گفت: «ایران بر توقف تجاوز اسرائیل به لبنان، یعنی حزب‌الله، تأکید دارد و به نظر می‌رسد واقعاً پیشرفتی حاصل شده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125064" target="_blank">📅 16:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125063">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رسانه اسرائیلی i24news : یکی از پیشنهادات مصالحه «صندوق کمک‌های بشردوستانه» برای ایران به مبلغ میلیاردها دلار (من شنیدم ۶ میلیارد دلار) بود تا دارو، غذا و مسائل بشردوستانه خریداری شود - تا کنون ایران این پیشنهاد را رد کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125063" target="_blank">📅 16:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125062">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
کرایه حمل‌ونقل عمومی جاده‌ای از ۱۶ خرداد ۲۱ درصد افزایش می یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125062" target="_blank">📅 16:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125061">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPMp4oIgC66a9qLuSGJj53PLwJeS5I61i7ZfcESGPIvs_gVYya5Tly4eslSJf8c4j5CBqyQvUU3Tb4eSdZ_SNIo_NricPei0Q3TQLopMN7z_p0cxbprHNmpkmaEOvDMW7hUfL0iEPTqQDiC0MG1DPxgtXZszco-bc4NQz_pmN3LAhVwfdprREk8QHsunZZ73cqvwJoFb3P_KGgDws-EcqPgGmFQ1kqCIKLhC-XnN6El1ZQETmCQeQrznWCApSL4xlhGCzeWiI3G03KXjFfK5wUPebyUDynuQx9z04vR5qO-ihDNP0cmAYvqBAVBPnAQfPxtjsxKxdex-Gp7ANC10Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مراکش در حال ساخت بزرگترین استادیوم فوتبال جهان، با ظرفیت ۱۱۵,۰۰۰ نفره
🔴
نام این ورزشگاه «گرند استاد دو کازابلانکا» هستش، با هزینه ۵۰۰ میلیون دلار قراره ساخته بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125061" target="_blank">📅 16:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125060">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
بریتانیا و فرانسه برنامه‌های نهایی برای رهبری عملیات چندملیتی پاک‌سازی مین‌ها در تنگه هرمز را تکمیل کرده‌اند که ممکن است ظرف چند روز پس از توافق آمریکا و ایران برای بازگشایی این مسیر آبی آغاز شود، گزارش بلومبرگ.
🔴
ائتلافی متشکل از ۱۵ کشور نیرو و تجهیزات برای این ماموریت اختصاص داده‌اند، اگرچه استقرار تنها پس از بازگشت حمل‌ونقل تجاری عادی از طریق تنگه آغاز خواهد شد.
🔴
مقامات بریتانیایی و فرانسوی معتقدند که تلاش پاک‌سازی مین باید توسط ائتلاف مدیریت شود نه ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125060" target="_blank">📅 16:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125059">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
دبیرکل حزب‌الله: از ایران سپاسگزاریم که با وجود چالش‌های بزرگ خود، به ما برای بازپس‌گیری سرزمین و حق‌مان در مواجهه با تجاوزات اسرائیل و آمریکا کمک می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125059" target="_blank">📅 16:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125058">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رهبر حزب‌الله، نعیم قاسم: مذاکرات با اسرائیل بی‌شرمانه است
🔴
تا زمانی که اسرائیل در لبنان حضور دارد مقاومت ادامه خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125058" target="_blank">📅 15:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125057">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ادعای موساد به گفته کانال ۱۲ اسرائیل، سلاح‌ها و مهماتی را که از حماس و حزب‌الله گرفته بود، به کردها منتقل کرد تا بخشی از طرحی برای سرنگونی رژیم ایران باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125057" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125056">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQjjmXtntURJ1kg0sLr3cPOJ1dYYbYp4a-IIgLC_2tKYAUpVvxeJGKIclj-1WNz888poJqtKA7XguauhlwSBHFoi_UV35rDg3gv9gVODz6k00MFu5Ox8lse_hClpGGb_rqNsRuTdD0N4zYmqdSuEDIkypW1HMM64a28KRw4LJdn4x_rz8DV1iIpp_Frhu0mzaTJXX1GshwzGxePIwyrfqly9HcyPyPXDo7Yy5RpyyfDEcnQ0k1d0PEYrfuEkUOkeiXsHbPn1j49lxPCdylmcRcNCmuJg7pkd7maGsEHGrOZs7t2aR3Ol1DXWhMdGMcv1xsN3ex1NcEksDqlyZ5HHBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بررسی دقیق کمک‌های مالی آمریکا در عملیات «خشم حماسی» توسط USAID
🔴
ون نگوین، بازرس کل موقت آژانس توسعه بین‌المللی آمریکا (USAID)، اعلام کرد که این نهاد برای تضمین «شفافیت و پاسخگویی دقیق»، هرگونه کمک مالی خارجی مرتبط با عملیات «خشم حماسی» را مورد بررسی قرار خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125056" target="_blank">📅 15:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125055">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کاتز: توافق کردیم؛ اما با آزادی عمل کامل برای حمله به بیروت
👈
وزیر جنگ اسرائیل جزئیات تازه‌ای از توافق با دولت لبنان فاش کرد: ماندن ارتش اشغالگر در منطقه امنیتی تا «خط زرد»، ایجاد منطقه غیرنظامی در جنوب لیتانی و آزادی عمل برای حمله به بیروت با چراغ سبز آمریکا.
🔴
ارتش اسرائیل به هدف‌گیری زیرساخت‌های متعلق به حزب‌الله در لبنان ادامه خواهد داد.
🔴
وضعیتی که در لبنان تحمیل کرده‌ایم ممکن است در آینده به توافق صلح با این کشور منجر شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125055" target="_blank">📅 15:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125054">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzBjo0ZVVuIvCtUlbNg0gqtx9v5KMY3Hly3BynlGlenJy6eniYOV05tJxngNGdDBdBXuAnkrJc2T7UkbvV80FQJON0s_dQAkQFcGRo9ft4BCH28AbH1gA-YCgFOt-dS1MKwoYBi4cVhLvMD2fLy-1MSULvlNHqfp9DIfN_9FYJ1TuREmb09wF49tkohqiMbp4ieElEHbpFhfUFOhMZjSQQwU501UfVPLjWoTZMtr6TgFOhWzIFeqEkWbSvsPXziKy6M_YuqY459aTCijFLrQAFmBs63Ir12qfgjfdJZ4r45Lm7txWrqOrAqs_Vu2kiOCH8hdeTZmGGTiagR6DBkVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال‌استریت ژورنال: کشورهای حاشیه خلیج فارس در حال سرمایه‌گذاری در خطوط لوله، راه‌آهن و تأسیسات ذخیره‌سازی هستند تا جریان نفت را حتی در صورت بسته بودن تنگه هرمز حفظ کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/125054" target="_blank">📅 15:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125053">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ درباره قطعنامه اختیارات جنگ: دیروز، در یک رأی‌گیری بی‌معنی، مجلس با ۴ جمهوری‌خواه بد و همه دموکرات‌ها، اختیارات جنگ من را محدود کرد، درست در میانه مذاکرات نهایی من برای پایان دادن به جنگ با جمهوری اسلامی ایران. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125053" target="_blank">📅 15:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125052">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
قراردادهای آتی نفت خام برنت و نفت آمریکا با امید به پیشرفت در توافق صلح آمریکا و ایران، بیش از ۳٪ کاهش یافته و ضررهای خود را افزایش دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125052" target="_blank">📅 15:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125051">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
نیروهای اوکراینی به یه شناور گشتی کلاس «Svetlyak» در کریمه حمله کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125051" target="_blank">📅 15:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125050">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
۲ عضو شورای شهر ایلام با دستور مقام قضایی بازداشت شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125050" target="_blank">📅 15:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125049">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No9ydGBaitVvaUIB3a3Ei75flpfSTM94Uze_ToGS0Lh-xjUw1ntGEiKGGXDqmounCTOT4ii5qGiBZ-yV4PYTMd0NRplyJgZBYxGaOJkxVM8GKXLrxMlazEW8yOQcPD_PaG50Pk9lWxVRhQ_x1XdlpQ0999TnQrXgbMkH_NmJ0SYk7gAGB8o0LLQdmsnZg42ksK0oSl9plbFYH3Cs_yIAP_vzybt0OfHreqL8QiaJKKHZ9jU5lqTRI1M08xrBd6InYvt9d5y6Z4Qxw3yO5x3teBXt9UEL3dJFu-VTBVCfbmmQjRCa0_syPe-DC-v4VHYX62tNPGj6D3ibp790Kny5lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ عکسی از نشان‌های پلیس و اصلاحات با نماد جمجمه به سبک ترامپ منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/125049" target="_blank">📅 15:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125048">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6b0ffdeb.mp4?token=L79IsKQHDJe9kXrkaeTsnqA1wlCb9BVrlA7n-H03BhX4LNaIX0zMPfwg25GAotW_YmCyNqd0dgJqV0A6UN2lr3XppbE73o4CH-7SIjpCm6TYiZ7L4a6d9daWkz758si9OqN86FT4ssUaG8704oMPehvjYKe0ngjOipfcorNJLqL-meF6s-MhbAKGBKH7ZNMmTfI_jorHcZO8TDjAokvXA48hgWTngUBdb3p_B5eDAK8DRWdjayEBobat4dpvpaezuZOrfUPIn2mmO7wkHpRj3jks8OOMoGyxFhsIR_Duqw3Q0EMlXFFapxNd5R3FEZ_SQDLIdEyQAJVEeq-dBdqKOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6b0ffdeb.mp4?token=L79IsKQHDJe9kXrkaeTsnqA1wlCb9BVrlA7n-H03BhX4LNaIX0zMPfwg25GAotW_YmCyNqd0dgJqV0A6UN2lr3XppbE73o4CH-7SIjpCm6TYiZ7L4a6d9daWkz758si9OqN86FT4ssUaG8704oMPehvjYKe0ngjOipfcorNJLqL-meF6s-MhbAKGBKH7ZNMmTfI_jorHcZO8TDjAokvXA48hgWTngUBdb3p_B5eDAK8DRWdjayEBobat4dpvpaezuZOrfUPIn2mmO7wkHpRj3jks8OOMoGyxFhsIR_Duqw3Q0EMlXFFapxNd5R3FEZ_SQDLIdEyQAJVEeq-dBdqKOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در حال توضیح‌دادن این موضوع که طول استخر کاخ سفید (از پروژه‌های محبوب ترامپ) از ارتفاع آسمان‌خراش‌های معروف دنیا بیشتره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125048" target="_blank">📅 15:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125046">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JzipMMyi8w7V3MLxkRzp8MGO82P7TGsifQ9SWOX9faSJ2FrEaTzvxq-o6WyZ4xM-CIzhc0vrg1Fz4F-wr4qJiVf1ShBgNY4cp5aXbIYwFsRHue3kq4EryMcEDL4xPoBsBWDQfAF6wP5kvHTWagUoo01lxN1Lc8FINhseqPfLkEULHICsqH2keDlDVY6W6_2HFVOuqKn0cRS2mzy1IMaNlAlCtryZF3tVlOK4X760PXHT7G0ydnWPSU4w2x50YBl02ApjodJUs-n4xeOj_624CIic_N6wOvIVDXU7hiIiuPNa_cU8uNnYbBla3J8S0Mht7y-ME18pz1tZC3g_fMGHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اولین بار پارک ویژه آقایان توی قزوین راه اندازی شد!!!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125046" target="_blank">📅 15:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125045">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به ساختمان‌هایی در تبنین و حاروف در جنوب لبنان انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125045" target="_blank">📅 15:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125044">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU8n9MfmNjz4DOhAW18mSc-xIVg02Sg3-VIsQ8bOIFuiycZuhlZA3y289ieRubxoHsHKkk_0WJ43g-8EVcKrXmIGVvPdts0GBww8LWox_8cDJ5l2ts7tSiqzx2dXbHoS8W0zoaD6ImcjQ35mmnI5l6cmITXzqHF_GKeh8FHURnLH7j7C0t3QBgnG3bZ__PTGIDqAU441oxZ0TWYLuUuaQpnfPPOtMBIgAfzGUi4NoSNzuAEM6xBm5F_skDrKD1HucCORsX04JG79tgjcdBbrSJYK9uZIP55uoU9s4-PqDuqSLVLklm2L7lW5aMiIJSj8uBygS9KM62EnZPnbeTst5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش دکتر باز شد فقط با گیگی
8
فقط برای الو نیوزی ها با کد تخفیف
🔥
Alonews
همراه با لینک ساب
🔗
و مدت زمان 30 روزه
❌
بدون هیچ ضریبی
❌
⚠️
ظرفیت به شدت محدوده
⚠️
📥
جهت خرید سرویس کیلیک کنید
📥
🤖
@Xvpn021Bot
🤖
🤖
@Xvpn021Bot
🤖
🤖
@Xvpn021Bot
🤖
🤖
@Xvpn021Bot
🤖</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125044" target="_blank">📅 15:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125043">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
فیفا در آستانه آغاز جام جهانی ۲۰۲۶، ورود بطری‌های آب چند بار مصرف را به‌تمامی ورزشگاه‌های این رقابت‌ها ممنوع کرد؛ این نهاد پیش‌تر اجازه ورود بطری‌های پلاستیکی شفاف و خالی را داده بود، اما با اصلاح آیین‌نامه ورزشگاه‌ها، این مجوز لغو شد.
🔴
دلیل این تصمیم مسائل امنیتی و جلوگیری از خطر آسیب‌دیدگی ناشی از پرتاب بطری‌ها و سایر اشیا به داخل زمین یا سکوها عنوان شده است. همچنین ورود اقلامی مانند قوطی، لیوان و شیشه نیز ممنوع خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125043" target="_blank">📅 15:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125042">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
اسکای‌نیوز: حزب‌الله توافق آتش‌بس دولت لبنان و اسرائیل را رد کرد و نپذیرفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/125042" target="_blank">📅 14:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125041">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drBXpXvK6KCSP2JZ_Z1KeGa6ioi2fZATsKEgjavu5uLm_SS9oXbKVyzCq3EQYUk70vWWg4yAeDfx6LZ5nktW_pqMMhq37BX-onLenwUPioy1KA6OliUy7lXQqzzq-7Tc9jnepuRisk5YGFCLAQ4PMGPa9rn5aA_k9fZshhL3SIndZvmrbKGXqh6MV-wYafcxdQ7tilK5Rr5zaa1dt0pXlCWbJijWIp4ptuvjtTEpq4SkgdbNYU17orKN-IRQ5MtifSafLl6Zz20s1CcapkGxfjUhyyS_dpM_a80wi0E2Jya7rXR9Ydf9Z3yulMk8m9qVFV5HU5QOxGsbImxA5CoMDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره قطعنامه اختیارات جنگ:
دیروز، در یک رأی‌گیری بی‌معنی، مجلس با ۴ جمهوری‌خواه بد و همه دموکرات‌ها، اختیارات جنگ من را محدود کرد، درست در میانه مذاکرات نهایی من برای پایان دادن به جنگ با جمهوری اسلامی ایران. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام می‌دهد؟
🔴
آنها می‌دانند مذاکرات در چه مرحله‌ای است. دموکرات‌ها با سندرم اختلال ترامپ سوخت‌رسانی می‌شوند. آنها ترجیح می‌دهند کشور ما شکست بخورد تا اینکه من یکی دیگر از پیروزی‌های متعددم را کسب کنم.
🔴
چهار جمهوری‌خواه، داستانی کاملاً متفاوت است - آنها فقط نمایش‌گر هستند! آنها باید از خودشان شرمنده باشند. ماگا!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125041" target="_blank">📅 14:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125040">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRWJ6IouwGOhP3z6tDsk0gyLuzZFzZ6k0jTlDTDCJ3ka3Gu-f3VUhA6Pix99xe2bRyk1aVcZkGKMQccbueSxW1cMVV9DAomu_gPdm8LDVx86FVFvl6NMQ3BEJghwrSxfJGI0DMmtcF_xXPrmlL-aE0UNCmxGL5LhT2zHMVB9C4eI7ThuFTSfukrp-V09SIMtFHrV4p7EzNo02zcwuXGUckZd8MAgQGX_Hx6GM9B82dAiG-SJTjY1tgi7PnJ4oWuhUUKtJ8RthNEOa2gd2ho0tlXXPrIcZb5fISth81Z6x-uyjKrCxeQhtq1iujUF82NWNT6vpuX8Le6J4C0jSYF4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارین پالیسی: جایگاه متمایز آمریکا، چین، روسیه و بریتانیا در صحنه جهانی
🔴
نشریه فارین پالیسی در تحلیلی به قلم برندن سیمز استدلال می‌کند که اگرچه ایالات متحده و چین از نظر اقتصادی و نظامی بسیار جلوتر از روسیه و بریتانیا هستند، اما هر چهار کشور دارای ویژگی‌هایی هستند که آنها را از رده بعدی بازیگران اصلی در صحنه جهانی متمایز می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125040" target="_blank">📅 14:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125039">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXJZ5yORKLIvIqnrYRoxcZUzU1DjnvKlfrG-_qfVCkRIvCrxkoEzSsnp8mJ6Os8ryrzqgNbI6x_z2NTt5oebRQxx2vS6NiqD-CH6JznNGjy3jH-arFuPqlCQKS4vcH1d5byZqf5xJkgWMwhQC3cDoPGKWdWhlhUWUYUTqVX3W2CwQXWrfKn5q60XojEfsxEcjdzJ7dA3csVt6dw1ZzGVw3_59UgWH0U2g7wBBZoCjv8jUUF_Paf4e7uS8byPS0oveZWW4YRCoDbQW3oxIaFCKbR28DZoARggHe_TWx9dsmyOHLWP35y-u6zdmVx3po6pLf6yXFHwRE90u4ToQRNMYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش نشنال اینترست: استفاده ایران از موشک چینی برای سرنگونی جنگنده آمریکایی
🔴
نشریه نشنال اینترست گزارش داده است که به نظر می‌رسد چین سخت‌افزار نظامی در اختیار ایران قرار داده و ایران در جریان عملیات «خشم حماسی» از یک موشک چینی برای سرنگونی یک فروند جنگنده F-15E Strike Eagle آمریکایی استفاده کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125039" target="_blank">📅 14:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125038">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
چت جی‌پی‌تی، دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125038" target="_blank">📅 14:35 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
