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
<img src="https://cdn4.telesco.pe/file/tlyKg76lpw8Dwz9VZcua3ejW6ZAgoBIZWmcmyMxPLgvRAiKIIB3RPFsXSUyJD3943lL8JfUwepa3p0I7HGKOFvuypCu04HQOMbuVfcqggEU2Pa-AxbengxfO3tp9bNWF2bqVvQPgs21hldZ0NB2MOfk6-yuQT-CgTyjJK3qbkShnUGzBywrVN8N-yehekMNu3bmzaF50XesgEJDJiIfl-4kgoGpkIWzLpdXQIcME7BkRLHYNlFGJNCxI3RoZ4KNQJZj8a2Fn93LGJkFPpIoL6YnTRYn38ZsNaj7euayJSAVW6Hh4nyB7IVK9Esq1RWJyzZKASIUnFjFQLHUiXLv8jQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 134K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 13:09:42</div>
<hr>

<div class="tg-post" id="msg-90611">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B90uMvLM-yUBJHzoXmdPfmmvAtLjZwiO8PL363NlCt6imgU0mShocaLkrOLYt8qbC-osnYTfzEtA-9Pz_-fi7b6nHnnr0GN_-ad07K-xeaAsRyTMJH6ClXgfPHdXqgfiiU_VgVMijl8CSgOCxQOAIYcw9zch2YBV_oFauISuNYg5P4qL9YVPvo-jMvWH14gfWwMt0pVUdWqQ2x_A5ZkZb6LxNobf0Dh-ow3FQkmlJTj5bmhHzL-6kmILOrIA4mkanhJhyyPT77braCupJ1SrX3x_LbzsY4w5hNiawzKzaKotzN75W06yQ0Hb8TjwMdKQDuYmh46GDmjjz9dO9iWpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
داستان خولیان آلوارز تا الان:
❌
تصمیم نهایی گرفته شد: بازیکن در اتلتیکو مادرید ادامه نخواهد داد
🇪🇸
مقصد مورد علاقه: با بارسلونا بر سر تمام شرایط شخصی به توافق رسید
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خارج از داستان: آرسنال و پاریس کاملاً از رقابت خارج هستند
🇪🇸
فشارها: بازیکن و نمایندگانش با تمام قوا برای نهایی کردن قرارداد فشار می‌آورند
🇪🇸
🇪🇸
موضع مدیریت: بارسلونا پیشنهاد رسمی ارسال کرده و منتظر پاسخ اتلتیکو مادرید است
👀
🇪🇸
طرح جایگزین: بارسا پیشنهاد دومی آماده کرده در صورت رد پیشنهاد اول
✅
پایان مورد انتظار: اتلتیکو از تمایل بازیکن آگاه است و نهایتاً مجبور به نشستن پای میز مذاکره خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 608 · <a href="https://t.me/Futball180TV/90611" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90610">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmoYAWNqPjqFBk54PDY_6UpMbgolXo7q3RTaSe4vrEmiaWeRmLE9caw6L4G1dIakKx7RK-5kv6WMJ6vxwVQ6jvnxTJpkZ-JQznyqSHKSDKLUTQvpC9qP0eLGwldlIv8Qb7UNOs81cCkQ9pkPPezsww9QZmZQ11y_UrSoxhbUsq82K8KMRBv-G453_nyMiLy5R6rwzfXs1y2rOWrCgKyC0_JA9x6xVaaWIwpPmsK_FFkyLLb4ElFNSD5hx_dK3mqECLpU0TrRBUE2h6zV48W4YBUx1ZuH3p6yAOZOwg3Ox5O2VP_07YZvNDvbIUSIByERLT_j9KtZ5zQM9OG_oLxsoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سافانوف گلر پاری‌سن‌ژرمن و همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/Futball180TV/90610" target="_blank">📅 12:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90609">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/Futball180TV/90609" target="_blank">📅 12:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90608">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFRZio9V4wVRljg2LzxRnYhDsAU7lV1itGYjjFMRAkPNbn5nj1VuOUxI5RT8JmECEUC7mZa6N-6bQeVgjOV_b_1946ZPyhMq82x4TNqfywf91tajkyznEOcW_ws1H3Hy09iF4Fd716zBihZO9VNKdUpNXXUJM2i_dK493L75Xbyt40L165NwiB3nkode4hujQqYfZLJaP1sCFUDLtVug7Deb-xfH_401uD7aw5kjRfPz-EuadZ7XR3_HzF0opMGtHBwLZSgk2T-x_utHhLRZelGm3G1CK9oUJdTpt2mt7UVNljRuFxH4oRkAMVXjcyQPYtwRF6XvC8mnH-d71cJnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/Futball180TV/90608" target="_blank">📅 12:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90607">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9fc7368f.mp4?token=m414ojYnDCb0WrQx8SZjb1DB3NSuQuDsT7wQM_q35eR3-P08hughCoZCrNmZxVImRwVNTOor_OtDxGtF8Yx3_ZiHZKJzOZFUy1QbMSXWQVnhv9N3THWppxt9no5MeOEs7qAynlfmNnlhZldgyVOkNdza9R5jTrPKDMpo6AxgtFNnez0tPLf8EHOoGHh9s8BXDuY00Y6ZnpUbcVfGLYF5Fileq_uH8TGyC4XhnV_5U6QSrnK-Mw9Qnf7vYUitHnpaCeoUOuVnfhp0mt_chfl9sgy6IUHYA6isnDiNMeYzjfK_biso9Zx8_bVHpgxuicA8hFon5nKKzA3Pn4m0A3g7mqBi3EOiy2fGbey1nSgm0TtldiKPJkTQ9wHPizC29xy2jNdyQ5s9wu2MXa5F_xnxs3HmFEDgkYDN1MFQATf0bqyYfTWaZw9UoP5AFN4i0x37gfyKthilVX11r2qbP64AJLZBVyUuSgUOFy07J0WTtXfuwhmWnLv_PkOIXLLgInfJabuIOmsaxxpIYYn4GXsUnrZfa5mviWHYVwulj0-unaokM5MvDwHO5ftnQUh8XGys3dM7c2YND3itm9lKt-bIAa_9VPpYHW1nNUozVCNSdZ_bVWa0YUoIz9VfsJBR455egPWhTu55yvfMKlHQj1pk53ZoBvmUamzQa-D0mwX6rTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9fc7368f.mp4?token=m414ojYnDCb0WrQx8SZjb1DB3NSuQuDsT7wQM_q35eR3-P08hughCoZCrNmZxVImRwVNTOor_OtDxGtF8Yx3_ZiHZKJzOZFUy1QbMSXWQVnhv9N3THWppxt9no5MeOEs7qAynlfmNnlhZldgyVOkNdza9R5jTrPKDMpo6AxgtFNnez0tPLf8EHOoGHh9s8BXDuY00Y6ZnpUbcVfGLYF5Fileq_uH8TGyC4XhnV_5U6QSrnK-Mw9Qnf7vYUitHnpaCeoUOuVnfhp0mt_chfl9sgy6IUHYA6isnDiNMeYzjfK_biso9Zx8_bVHpgxuicA8hFon5nKKzA3Pn4m0A3g7mqBi3EOiy2fGbey1nSgm0TtldiKPJkTQ9wHPizC29xy2jNdyQ5s9wu2MXa5F_xnxs3HmFEDgkYDN1MFQATf0bqyYfTWaZw9UoP5AFN4i0x37gfyKthilVX11r2qbP64AJLZBVyUuSgUOFy07J0WTtXfuwhmWnLv_PkOIXLLgInfJabuIOmsaxxpIYYn4GXsUnrZfa5mviWHYVwulj0-unaokM5MvDwHO5ftnQUh8XGys3dM7c2YND3itm9lKt-bIAa_9VPpYHW1nNUozVCNSdZ_bVWa0YUoIz9VfsJBR455egPWhTu55yvfMKlHQj1pk53ZoBvmUamzQa-D0mwX6rTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
برخی از برترین گل‌های فینال لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/90607" target="_blank">📅 12:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90606">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVDaqBP_AedBDAQn2G169EtlffBu_wL3WBVnh5CdeoKk7mozNPxU2boEawj0GcNNBUL6klDA11gNr__JLR7RDx5MM0uwC3AGQeOwYm8GQxscFIaNtvYPfwZgn1jJSQYwIi_LjoQcB_thqGQJqZK-CSwO1uCtaeqP2AQjKl0tEtG3ku3jrn3yPRx9XEqP6AqBEj0Bs5D75oIFiLiDSCNsPhgIqlF5w-fUJomBMXCnNXx1IsahMA_bCQMmCt_LnIS4nsCLoUuTJ1tRIGHgqnDmIsGyvMEt0cqw_lOu1RofT8sPI78yomDn_fbV8hEERdOw55fw-I-C4DA3Ku1qCJnDtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
گزارش‌هایی غیررسمی از فیفا:
❌
فیفا قصد دارد «تمارض یا مصدومیت ساختگی» را به عنوان یک تاکتیک در جام جهانی ۲۰۲۶ ممنوع کند
❌
دیگر اجازه داده نخواهد شد که از آسیب‌ دیدگی دروازه‌بان به عنوان بهانه‌ای برای توقف بازی یا گرفتن دستور فنی از مربی استفاده شود
❌
بازیکنان همچنین نمی‌توانند در این مواقع به نیمکت ذخیره‌ها بدوند تا دستورات تاکتیکی بگیرند
✔️
تصمیمی که هدف آن افزایش سرعت بازی و کاهش تقلب است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/Futball180TV/90606" target="_blank">📅 11:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90605">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7181ecdb60.mp4?token=JK-JxAlzqgIHoNXcmP6ZZld-2NJvQcy4FFYAysDacUYDhqqJYD9WbgbUj04xV-lD0RlIs_QCcukQu_pUq7KBMaQTSv6L1G1zXBFfTdch5FPu-YUdYBNDIGPF8h6N2RNbxcKwjAkniv0EUpuxnAJRULNWt9GQI_dzz6Hv0T8vnfW2ALasBKGConluAAXmVGkmIvIV9zmTY4kZkJoGY3k__6ZpNEkZxQsT6kNL2Mj6wnRya54emUoS6MwNPrb_WhTXNrEEAqQVjfhKezf7p3jZOUb_eI8uNv_W4OUOosH_aydxeG4YJMihi3RCSeLlNwWWVb37C6avhdmF3Y8TOynTEH94CG1Nq8VRR82bPAqon2m-jpxdSZcUL7lLo68hQ4DF2R04s0o6w_wHQjtcJIIZjOM9FG_iPxyZyz1gK_7m0s0RpWNY7hxjfNJuuHh7pDHnALaWvNLJqtz56dGU8tafPMTNABDVq5TdT16G-MZFHBwTI8ytHwCyNVBso4w9WQiIDD-jJoeQaP7gW7s3d5ZbJFDC966UvnCpotG1Cx1K2U9RUAIQFA-WjKmV5KASCLvq_Lpg4bxgWQ7i7GbAsaMAGPlKwrNMNynsU4g6r7kvEPMSw-HrPqcylM8SK35-TSJ8pZd2bLbBs5oPJ9bHMKBazfV_ulRf0IMnF4BJ_z2YHlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7181ecdb60.mp4?token=JK-JxAlzqgIHoNXcmP6ZZld-2NJvQcy4FFYAysDacUYDhqqJYD9WbgbUj04xV-lD0RlIs_QCcukQu_pUq7KBMaQTSv6L1G1zXBFfTdch5FPu-YUdYBNDIGPF8h6N2RNbxcKwjAkniv0EUpuxnAJRULNWt9GQI_dzz6Hv0T8vnfW2ALasBKGConluAAXmVGkmIvIV9zmTY4kZkJoGY3k__6ZpNEkZxQsT6kNL2Mj6wnRya54emUoS6MwNPrb_WhTXNrEEAqQVjfhKezf7p3jZOUb_eI8uNv_W4OUOosH_aydxeG4YJMihi3RCSeLlNwWWVb37C6avhdmF3Y8TOynTEH94CG1Nq8VRR82bPAqon2m-jpxdSZcUL7lLo68hQ4DF2R04s0o6w_wHQjtcJIIZjOM9FG_iPxyZyz1gK_7m0s0RpWNY7hxjfNJuuHh7pDHnALaWvNLJqtz56dGU8tafPMTNABDVq5TdT16G-MZFHBwTI8ytHwCyNVBso4w9WQiIDD-jJoeQaP7gW7s3d5ZbJFDC966UvnCpotG1Cx1K2U9RUAIQFA-WjKmV5KASCLvq_Lpg4bxgWQ7i7GbAsaMAGPlKwrNMNynsU4g6r7kvEPMSw-HrPqcylM8SK35-TSJ8pZd2bLbBs5oPJ9bHMKBazfV_ulRf0IMnF4BJ_z2YHlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پشت‌صحنه فینال لیگ‌قهرمانان در استودیو گزارش‌ ورزشی که دیدنش باحال و جالبه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/90605" target="_blank">📅 11:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90604">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=dpI6fsUME-Jdmh-QiiMajwiwHyRX3g9Oo-YyphesHPiXFd4Rr4KjGMqyxEi4IJW_XrxmZuaFkMzzDOKf6JaLa8c5mRpksWbOVeQicauarIt6sEtlu5tGCFOVDJJE498cAdCRynr2NP5eAxUUFOUbOHlyXxj_aHqQBsE8-HJbOjhNSOD-IzOcB1Gm4YgPC-qjtAr5EbyenKvBgeAfmJ2GOnZ-aPaIvCIAY2LJeNlJ9I5XOwMkUdjVi6olcGAr4JcA_swAsYEMmuQpagjIVXBl3WCkvq08KHRoXHB43OX8lI_cTHcRg1kpCzALw9Ze_OYPrTQZr_xrm56MymtUWDF0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=dpI6fsUME-Jdmh-QiiMajwiwHyRX3g9Oo-YyphesHPiXFd4Rr4KjGMqyxEi4IJW_XrxmZuaFkMzzDOKf6JaLa8c5mRpksWbOVeQicauarIt6sEtlu5tGCFOVDJJE498cAdCRynr2NP5eAxUUFOUbOHlyXxj_aHqQBsE8-HJbOjhNSOD-IzOcB1Gm4YgPC-qjtAr5EbyenKvBgeAfmJ2GOnZ-aPaIvCIAY2LJeNlJ9I5XOwMkUdjVi6olcGAr4JcA_swAsYEMmuQpagjIVXBl3WCkvq08KHRoXHB43OX8lI_cTHcRg1kpCzALw9Ze_OYPrTQZr_xrm56MymtUWDF0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اکسپوزیتو زید جدید امباپه درحال قر دادن در کنسرت دیروز بدبانی!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/Futball180TV/90604" target="_blank">📅 11:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90603">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4pYKbUNr7L-IISiVhl7zbv-c-_M1wB28Yqv_dwBbJiX8TwwKNU_rPG7y84fFdgZUUZfFLQ6wYNGS09xFqXOo-gFqnJn5M_KxJFCw4XHk0jGaQmZ_1WsmvqxFi9dLuyUo-ivVhEqlmmNue1Bk3LpDNGxLdm0t6Pq1Rqs9i2Xa0hJ8bW83WBEpt7IZ9_wPH6siACZu_1Br5Jtm72nB8NtKwT3-pQQUfBKZkrEn6xf-kt25RO0dHZd698J19vMXMco3dOHDYOoMfWq0frjoZHuH5CfJXV_2eI9kMiXQhstFh5zlnDwFLEtYeJvZaE646W5tdJY5fF8Jqrj0cRuLFtNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
👋🏻
جیمز میلنر ستاره سابق تیم‌های لیورپول و منچسترسیتی از دنیای فوتبال خداحافظی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/90603" target="_blank">📅 11:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90602">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e59e2547.mp4?token=Aqzd7rtPStwn37vpnjDU_3z6k2s78aBe5X4iNdQR6uw_r2f-qjSxcqFMJCsKcTruYHx4wHcugRhMLAx5gGxX-Z4tbDflfjLrT6mlNBA19p-dhI-nv7f2QKNEGJIqbfUzfJe7bPmWmuUGOh5ZnV_xLCJEYonyOAifL0j79YE_w1xE6WmuNLJ0tSgb3EINXAnhWkSgRJbQI7VMZ3UV0DMy_dGbh_x7n7gaQ3xrcDH3S7xPAi1H0G6E5rGecBqp28vYOKB7mGa6MX6w8Ukfd7uKAtvU8XscKupaow6JWe0qTwFXgozM-UfspmvSx4E0LmLABtIfIEKwb4AnbsIWR7XzZRhoYzRkEotmnUiueSwaxeMHy5WKgDdmp0hDLL_RXYAFns46gojD4TZnMbUlH-cyef0hrt6LWjM6ze6C7T62ORJ6tM2FFS-l5RFAo80SKN9V05CXca5yp4LCN764v5U7F1cIX3mq5drN6am0-_cjuHjhDAj3fWdUDyqDRSQ5HrRsGx8QRoG_-HWrD0yLcq2DPCe6CW7k4MmP4ayVwBGJCU-hji83G4x_lAkEV0efk3DNC9ffn19LgCSHqAAMfa_6ZMycUpKI3TNc15aNAZ4j9ngA_CEGc3LD9W4gMj4mgxMHewoJSd-7UXp9bPpLpGhwxNMhU7Wq4wR0STGKACNka20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e59e2547.mp4?token=Aqzd7rtPStwn37vpnjDU_3z6k2s78aBe5X4iNdQR6uw_r2f-qjSxcqFMJCsKcTruYHx4wHcugRhMLAx5gGxX-Z4tbDflfjLrT6mlNBA19p-dhI-nv7f2QKNEGJIqbfUzfJe7bPmWmuUGOh5ZnV_xLCJEYonyOAifL0j79YE_w1xE6WmuNLJ0tSgb3EINXAnhWkSgRJbQI7VMZ3UV0DMy_dGbh_x7n7gaQ3xrcDH3S7xPAi1H0G6E5rGecBqp28vYOKB7mGa6MX6w8Ukfd7uKAtvU8XscKupaow6JWe0qTwFXgozM-UfspmvSx4E0LmLABtIfIEKwb4AnbsIWR7XzZRhoYzRkEotmnUiueSwaxeMHy5WKgDdmp0hDLL_RXYAFns46gojD4TZnMbUlH-cyef0hrt6LWjM6ze6C7T62ORJ6tM2FFS-l5RFAo80SKN9V05CXca5yp4LCN764v5U7F1cIX3mq5drN6am0-_cjuHjhDAj3fWdUDyqDRSQ5HrRsGx8QRoG_-HWrD0yLcq2DPCe6CW7k4MmP4ayVwBGJCU-hji83G4x_lAkEV0efk3DNC9ffn19LgCSHqAAMfa_6ZMycUpKI3TNc15aNAZ4j9ngA_CEGc3LD9W4gMj4mgxMHewoJSd-7UXp9bPpLpGhwxNMhU7Wq4wR0STGKACNka20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه صادق درودگر راجب مصاحبه و مناظره معروف و جنجالی شبکه خبر
🤣
🤣
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/Futball180TV/90602" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90601">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05002ce01c.mp4?token=mzZBd3AfPrkQrHABQc53KwjoIVTvGoeEJSH5dgEq4-CBrswXvCs9Gt50G3dHuwqpYuKdgg_0Ba4aikcC5hytOrIDB0C6-2shThrwdjVtu7i5iLVPEhknXITfRuWdts0PExmKw2jW9-9m4T9p07BaMUM5OB_GbEskIB3Kr6aPuBXkgaEpIOLdvRGfqsAxFnmX_uhfbOtxT5L5_Uj2uejfNImzxyNnC2v33ly96r5-I3r3XzIdAJbnZo9Pt826vn1I8TDxJVsuxGTWEEDEExX0R2fnMU72pY8RYDVxfgfVAhNYT8ifKUbPMr7ML1fulEeC1edenjgVeQWa2FFm2eroBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05002ce01c.mp4?token=mzZBd3AfPrkQrHABQc53KwjoIVTvGoeEJSH5dgEq4-CBrswXvCs9Gt50G3dHuwqpYuKdgg_0Ba4aikcC5hytOrIDB0C6-2shThrwdjVtu7i5iLVPEhknXITfRuWdts0PExmKw2jW9-9m4T9p07BaMUM5OB_GbEskIB3Kr6aPuBXkgaEpIOLdvRGfqsAxFnmX_uhfbOtxT5L5_Uj2uejfNImzxyNnC2v33ly96r5-I3r3XzIdAJbnZo9Pt826vn1I8TDxJVsuxGTWEEDEExX0R2fnMU72pY8RYDVxfgfVAhNYT8ifKUbPMr7ML1fulEeC1edenjgVeQWa2FFm2eroBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
#رسمیییییییی
؛
گل فده والورده به سیتی به عنوان بهترین گل فصل لیگ قهرمانان انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/Futball180TV/90601" target="_blank">📅 10:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90600">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aChMRVcawUFok5kRox4WmwrnsTZHP9EAay21xbEUqSZMaWyVd78upCLOlSkmEYAuXbPlUwQlHPMo8LopJOYzTew2r4WTWszwhL50GKxmAu04KUxVSBH2YFBjQbjl2XIbItFdtP-k5wTkWrEAsZotYoSv4wK9neZomNtJAaNyn8Pcz0QvNYwWvPxKEhklx-VyIHn7nEzq3DASR3qdDcaKvayOsMbs_DSxNg08VWRHtSQAiMaCsCbgRPzsMFUmT46-EoMPXtW7FvkplyJVWEA0_rYV0Um--IcbSzpJFpF4EYIUcJf5Ru5p60MAo6ezA-xvroZEa06kW4XgmVUNkSuJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
علیرضا فغانی اولین داور تاریخ فوتبال با سابقه قضاوت در چهار جام‌جهانی مختلف
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/90600" target="_blank">📅 10:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90599">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار…</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/Futball180TV/90599" target="_blank">📅 10:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90598">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb3WqCC_hD4I7LbWrzx6-McmWU4bykmIvXWTOzQTF80FcVSZOHuGu95R0EHJsoquY61meigV875Vw3Bh3-Sef3MGpeCxyGmM1bi1apvqhziMPaKzuFgRc77UfKDARlBFnYMvhTVY9kdVCG0X4O34Ihs4PpN3MFGht3kwjzEZRbVGusziZcXSMg7tXG7VjzuVCyAACoXfbsdUUCmkGF7PYMIMEZ85N8_TzCbkIlYpCmwc9oa8sVzJtKSqkzsxpMYjSk3ecPS-ztAjxJmOT65p6THVqfSXdE_rKkviwRqcLfulMUZNJyZFBl0a5_5VTbMl1YIAjcQnFXs-kFHRL-GcaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
؛ گستون ایدول خبرنگار مطرح آرژانتینی: با جرأت میتونم بگم که آلوارز در نهایت از اتلتیکومادرید جدا میشه. پیشنهاد پاری‌سن‌ژرمن بسیار بیشتر از بارسا هست اما آلوارز فقط و فقط به بارسا میره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/Futball180TV/90598" target="_blank">📅 10:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90597">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458f4f6058.mp4?token=C7NgZpEzoDWLDCs3l-K-eWWtOIRWfi7xf5LsuzQzAnuAXexYuq9bv4gUq4EfPX0XkKQTe4jyFx_dajfMLomvlwKvckUSsimD6iuxnEvoEy1POIrD_AUY9W33GC03rmsx6nGYW2RONSQFrW3_PnRsMEuUSmYQ4Hi982GAZxVMk2UMxgMRyRcBw-3Nd5pE41TNnjVdeiAfVQF4Q8XdrO5LrF7GYpryfTgk0PBXWe406DFCpB16WTU6USQr5LKQ4Pihp-6s3xDtq0gSnux7yquZXxcIJByU3bi623TGAVq2cLb6y6xdScRe4cIi6Evyds2MbWtHubaAVR1KssxPW6_Gng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458f4f6058.mp4?token=C7NgZpEzoDWLDCs3l-K-eWWtOIRWfi7xf5LsuzQzAnuAXexYuq9bv4gUq4EfPX0XkKQTe4jyFx_dajfMLomvlwKvckUSsimD6iuxnEvoEy1POIrD_AUY9W33GC03rmsx6nGYW2RONSQFrW3_PnRsMEuUSmYQ4Hi982GAZxVMk2UMxgMRyRcBw-3Nd5pE41TNnjVdeiAfVQF4Q8XdrO5LrF7GYpryfTgk0PBXWe406DFCpB16WTU6USQr5LKQ4Pihp-6s3xDtq0gSnux7yquZXxcIJByU3bi623TGAVq2cLb6y6xdScRe4cIi6Evyds2MbWtHubaAVR1KssxPW6_Gng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیکه علیرضا دبیر به پزشکیان بخاطر پوشیدن تیشرت
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/90597" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90596">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgEA6-fNoWEra3qdSIKTOXx5ysFOHrnnVkBDbUVJU_b3KliQw6gEIkTLB0QRF4sz_J2ippFxBNPsT51mx4uRgG3ax3Pwlh5b5GvdRgJZD6_rfEaJGElQbFI9vWf7v_Mzt9MAZ4ib1ZfL3PIf27PS7nRzSTjGgyRNIMdvgFuICfXQ2AcIdRBE0wFcB1zaksAurnd2O64DowKTEwBMOAhv2hLXmArsUtAIQngaiv-brUCdfC20uygK8JJf3Njjj5fW70kai64ArLp0pCyphQgblvq6EooqIA3mWpNpcBqznbKP4_wxEbgujfwv5aL4l2oD8SSAbn9oRYcGXPdIH3UjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
تمام استادیوم‌های جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/Futball180TV/90596" target="_blank">📅 09:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90595">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHW7iHfcdf3puZV_L1Z9XQjZTW87MYA1XukIXRKVXDDoO0B_ibgWw1ZPQzzo6rlKwAfs-hoE-tK7r0dIvuLhdy7QgLlhMOJa6PRXe7LjmFXvNiEoanCS1R0hD4MVRWcPNMGDU524vkb6dxNoWuoTeEQeZImTuQQM7HhwqHm-G6WkaoPvbeDNQH9RAu5U_dlRKGR2LrMfy5LjSFGcfly1n6wuBHojL8q39gawA2b7Vp3vgrkjDsNdRgH9_eBcsZiZjGbbVk7jGZtt_qWao6aiRU346czBYYVueMZDLOKjRLG4DmXbIx2e_AQaZDFEOp1iPEJvneJajK7g0QrIEUuCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابراهیم‌کوناته‌ستاره خط‌دفاعی لیورپول از سوی صندوق سرمایه‌گذاری عربستان سعودی رقم بسیار نجومی‌پیشنهاد دریافت کرده تا به فوتبال این کشور ملحق شود!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/90595" target="_blank">📅 09:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90594">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=Qgyo5zJbLOA1HVJS2qryl_f6tCMV6s4dRDlMYt0gK4HYxqLl-hbMXP8T0DGHtzrddZMf9FexVenZwdKRb0P4eCyb-29OlE2G-lwfKxxOrqstiVs71hYaV29ghndgrTV7tNAI0Bx3kfEYBoR8J4HQU5qT2rjLHDAa4VuQCC2V7W75EQG0W1W85vF3s8mQCW5U2JJflUhXCIrv8JjgDcjIpGmJ8rssndjB5et8lJdBEUpD7kFnbRHmK68Pp6H9QbjhKKgBKuBIydFz_Th9KkoolGBvWNd13RoMNF6Fbuh9gsGtD1WoiQiT8wSC32erI4XzX7OvF6X6HX9n44uWslXQlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=Qgyo5zJbLOA1HVJS2qryl_f6tCMV6s4dRDlMYt0gK4HYxqLl-hbMXP8T0DGHtzrddZMf9FexVenZwdKRb0P4eCyb-29OlE2G-lwfKxxOrqstiVs71hYaV29ghndgrTV7tNAI0Bx3kfEYBoR8J4HQU5qT2rjLHDAa4VuQCC2V7W75EQG0W1W85vF3s8mQCW5U2JJflUhXCIrv8JjgDcjIpGmJ8rssndjB5et8lJdBEUpD7kFnbRHmK68Pp6H9QbjhKKgBKuBIydFz_Th9KkoolGBvWNd13RoMNF6Fbuh9gsGtD1WoiQiT8wSC32erI4XzX7OvF6X6HX9n44uWslXQlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به کون هینکاپیه پرداختن
😂
😂
بن وایت میکروفن گرفته دستش داره اهنگ میخونه هینکااااپیه کونتو نشونمون بده
😂
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/Futball180TV/90594" target="_blank">📅 08:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90593">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d9e66e04d.mp4?token=OOO7SoXR8bQhbcvlvIGTOQnP8uxIaAtWG_z_0aSvRBujz3iaVt5TFzUVq9XEukOpHXEMHcxtbEZrZtRGayKwlqKkIOtXlfj0vxr5hQ26K6yUKmdNjQ-95k3vOAhVcUhskiEFUONd412uxS1LyJQMUlIU-9K2-g4yOm9SfnA4dunGC1tdKawA6cZy5XxIF3pLFXBhjpABh2qFx-2gQjbgw6iUD00xAW79hdjO0W9wfSu5qs1KwLMsxK182um8ZrPvIJWE2fS_uouTfXKHxCmLFCXmL3CmAmh_z6X2wIyMl-6EyRFrPeyNE9W--uhZgLiZALa1TwkWYxE_-CQ4sWWNJJ1c10_95KdJZHw62r7s9m0uGUfqDajLamSmaqvnXGek7Jmsr2yrJq6jOX-itKIQVolP4O_rffTps9WV63fTFDA3pW1pNDz5X5h-Ki1c70T3tmYQ2qE_7S_D6FasKegxKG44FCl1X3-45U8MA5TVBD-Jsjrnk87W3ITPO9AP4mhhzsgpCEx2BYZCxvZKUeplc_oOdQAQWj-7j4vqBS7_6AT_UKNtljlqAuh9E9RJogm-n3rYR0ry9s79axo5WAwUOFziEFW2C0qCLFuSUTIhFV5iTIW0puw1GqHGJruDntpbLSdzmkTDlbufEsjX39IHgZnM4B-rFWa_uW5XElpAK6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d9e66e04d.mp4?token=OOO7SoXR8bQhbcvlvIGTOQnP8uxIaAtWG_z_0aSvRBujz3iaVt5TFzUVq9XEukOpHXEMHcxtbEZrZtRGayKwlqKkIOtXlfj0vxr5hQ26K6yUKmdNjQ-95k3vOAhVcUhskiEFUONd412uxS1LyJQMUlIU-9K2-g4yOm9SfnA4dunGC1tdKawA6cZy5XxIF3pLFXBhjpABh2qFx-2gQjbgw6iUD00xAW79hdjO0W9wfSu5qs1KwLMsxK182um8ZrPvIJWE2fS_uouTfXKHxCmLFCXmL3CmAmh_z6X2wIyMl-6EyRFrPeyNE9W--uhZgLiZALa1TwkWYxE_-CQ4sWWNJJ1c10_95KdJZHw62r7s9m0uGUfqDajLamSmaqvnXGek7Jmsr2yrJq6jOX-itKIQVolP4O_rffTps9WV63fTFDA3pW1pNDz5X5h-Ki1c70T3tmYQ2qE_7S_D6FasKegxKG44FCl1X3-45U8MA5TVBD-Jsjrnk87W3ITPO9AP4mhhzsgpCEx2BYZCxvZKUeplc_oOdQAQWj-7j4vqBS7_6AT_UKNtljlqAuh9E9RJogm-n3rYR0ry9s79axo5WAwUOFziEFW2C0qCLFuSUTIhFV5iTIW0puw1GqHGJruDntpbLSdzmkTDlbufEsjX39IHgZnM4B-rFWa_uW5XElpAK6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
وینیسیوس دیشب با این گل خودشو برای جام‌جهانی کاملا سرحال نشون داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/Futball180TV/90593" target="_blank">📅 08:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90592">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXxgZ1kbUvVnTkybpbiz6F4htYUnQnTv0MxGSfaaMcmGD4G8VolBB7A3rjUzK1fM6UifGjrejj4A346tcCgzuLfHU6uZRCLQBQzoZCotney7cNaZZl2edIGZy6JUfaj4jcLX276SOFWNhzvG6sNFpxRv0G-a_hnlqWZ9jX-g7goNw8-0Eo5s3gL5Qcolt0wPPDAid8MZ7YJCF98R_tZsOJfAJRWpFTvVjzQLCiBou9BCF7HNcBgwQWSo0nU3V6L72eXf3xLZvN_r1JYzm8b765VuazFm19o6YLVK1h0lO71YCJr4y6vYP2JukOH3Wne6knwrtKblVB_vlhO9YJ29Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وقتی همه چیز متوقف شده بود
پرداخت سود دلاری اطلس ادامه داشت .
📊
ربات هوشمند
اطلس
یک سیستم سرمایه‌گذاری مبتنی بر آربیتراژ در بازار کریپتو است که با استفاده از اختلاف قیمت صرافی‌ها، معاملات را به‌صورت خودکار اجرا می‌کند.
تمامی فرآیندها شامل اجرای معامله، ثبت گزارش و پرداخت سود به‌صورت سیستمی انجام می‌شود و کاربران می‌توانند سود روزانه خود را برداشت کنند .
🔹
بدون نیاز به دانش ترید
🔹
واریز و برداشت آنی
🔹
پشتیبانی ۲۴ ساعته
🔥
ورود به ربات و مشاهده :
👉
@AtlasSmartBot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90592" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90591">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
اگر همین الان توی سایت #وینرو عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر،…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90591" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90590">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYRTcUm1XEkonXMFoOqqWDLZt2it1Ln920xHL6TARFD7YKYH1RSR6MMfN0525uOUVNsgeybYKk6NqPBJasq-ysbfB9z3YTF8InngjOhf3WMfniteW18x2zdu18VBg1AL42tLppaBnQv3ormIrjnVLih3bot2hXusLKhWPJzhfs-SvXD1gKKKDT5wAV0prNJan8JouP_GQfOXZScbFij_z1GGh2lxfWA3rbwI0ufUjACo7F7vPZGDrkaEE6pgsCkww-E2Yr0t-1wI-6Wi8lpp25sYNf8SnIMz44JrfPFbYBfqML0DgFXp4xl2uP63fe5E--qA53T8UMMlrHqWRKntEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a10
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90590" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90589">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkKi3NTFdmVBEQRTF74CEAvaV7a32fYBCFcuAxNiVmHMIejfkjoqiX1Mwwp2CKYTf3YxrERnJuyoKrGuy13STf9DS4STFQozrCCdNnD6wBKgKpGsknI5BV9zOyWSRt5QhRd4SO66S-nwzvW_63MvMPhmBwVEW7JdTpwiNDmDT9cIBKkdteyrONyD7cgIzMM87GbjUVx-2080HsmhsR2WbpSwjGflae9nUjEHLOWELfQD3pvqBHKkqjqfu2nMYm88UWUm_lU5P0euyYbCKQyt4VszpE3QFClT8bGWaLPEBPcqf62eB9KSBjPIXMC1JowWyYKc5IDj5zdJcwUbRZcfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید از اسطوره های فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90589" target="_blank">📅 23:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90588">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎙️
مهدی تاج:
بازیکنان تیم ملی دنبال پاداش و حواله نیستن، هدفشون از صعود فقط شادی مردمه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90588" target="_blank">📅 23:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90586">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCl7xKa_zUz9xtWuQP1oTvYJLOjx-19tujirPCXNE-LSApVfz2KRLmgqllhpOmUZxy31IOUcy1CR3Kir5KMY_amK13JerIgdX8TVBMVassw1iXN4uCQmxYrIDFR7fbMouNDdsfGKyEOyC_ddVLwPeVpzQJkMJTgBalef7xg9yUh_vruTFsqth_eWgbBbDeZA1yz1EJhfRyMCpYn6OpMwS3p9udKkdV7AOSUJXGkWjN9TSE5dq_axSrv3ppXS-jDsp5bIl-ylDmjxYbU7R8MdI3wZEFP49SwGftwXvOoLQPu9C9Y-6qiThaHcnk6Lwo63_M_6sysIIJ_K3UwTMX5PTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
ایندیکایلا :
آندونی ایرائولا سرمربی لیورپول شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90586" target="_blank">📅 22:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90585">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAqaCsaPENg4kFuyCpyc3kQidgJ-782tA5Ryk-eTJua-KOfwIObcPgIDESBVB0hY-PHrIl8B0q-c19adgTxQSSYsof01j8gMju5qLPbeJdl0H67Y4YSbHtjDNEfRaTK50ipASFbPuErcKQqsMh1RYv_sp29Myx92WZU2NXz9gHTTUyOoWWf5Pt5iQvdTih-njDzHQ8W5lxuurVHUuLg29qSWTCNvvNPbcwMFSkEeNWldPXUZmhQiEG0enjdhtzhr5EjHS_hYq5h00tNtH3G5z2FJjbSba03iw1aLpRv2ZlRcoI8Lzyx7emRXIDmpiZh7sWB0TIawURJvwFNCQ2GSsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوورییییی
پدر آلوارز پیج باشگاه بارسلونا رو فالو کردددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90585" target="_blank">📅 22:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90584">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0hb2sD6kzPSV0Zj9rV556FiVw_ymy0I0vg95g0HbasN2arJ6xEV0DJtbqdOK66smw8WtE3v2-8e_tRoCkREsVtuRzXtk7EwfZTKHxdv_7a_OQtpvV89q_Do5zJjKgwy3b1bgrkJ1UWhYy32ZbHyBBfAkb0d2qLre0nUg60shCGgCVtezYgsG0NKe8G9kZcEqsAkqXt_1m4rFOoA4I-cP4He053FbZRXdfo1lL26Y0hAAED4CUx9oFxfzUh0XhgGhZd5GmSKdczoVffFsIDijpiIlo6SN7tsVCXtZRNK1GbIsL3mQ0gEselH-6PfKad_WQ18KDDeLgkLUmWx5xVUCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نروژ
🇳🇴
-
🇸🇪
سوئد
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
دوشنبه ساعت ۲۰:۳۰
🏟
ورزشگاه اولوال
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
سوئد در
۱۰
دیدار اخیر خود،
چهار
برد و
دو
تساوی کسب کرده و در
چهار
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳.۷
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر سوئد
۳.۴
گل در هر بازی بوده است.
🚨
نکاتی در مورد بازی‌های رودررو:
در ده تقابل اخیر دو تیم، نروژ موفق به کسب پیروزی در
چهار
دیدار شده‌ است،
پنج
بازی نیز با نتیجه تساوی به پایان رسیده و سوئد در
یک
دیدار پیروز شده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۲۷
🧠
تغییرِ مکررِ سقف روزانه، نشانه وضعیت ناسالم است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90584" target="_blank">📅 22:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90582">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e5c0ed52.mp4?token=dvQ-J2fCOT5yqC-6XWOvJth0uBIjk99B9EosC2GvCmNoukzdfaRQ7pM93b91A_5T9aaou_nqrm181mdfINDGFBlqavvqStTGBNJtgaUMgTFNaD1Bs0hRq9JiSH04c1ndmD9hw-sFeEqWCFZRjCnokRmHwT690iPoCkb6g6_ootoS9BlaLaZ-aNlQQYeKpL_LL-i54XzUApOKBTjaU20g20yX8WaNQ_eWcHOlRseXZTpkc5JJBJ5CuZf2el829I8m6ciXUoWoyeqI3CfzkslOZPIO7lfjypgi9Qm9BABRdtJQC7CVsbMDWpz_XC7hc6AGWY8UBgprZnFJM7jMG8a98A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e5c0ed52.mp4?token=dvQ-J2fCOT5yqC-6XWOvJth0uBIjk99B9EosC2GvCmNoukzdfaRQ7pM93b91A_5T9aaou_nqrm181mdfINDGFBlqavvqStTGBNJtgaUMgTFNaD1Bs0hRq9JiSH04c1ndmD9hw-sFeEqWCFZRjCnokRmHwT690iPoCkb6g6_ootoS9BlaLaZ-aNlQQYeKpL_LL-i54XzUApOKBTjaU20g20yX8WaNQ_eWcHOlRseXZTpkc5JJBJ5CuZf2el829I8m6ciXUoWoyeqI3CfzkslOZPIO7lfjypgi9Qm9BABRdtJQC7CVsbMDWpz_XC7hc6AGWY8UBgprZnFJM7jMG8a98A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عثمون:
سال بعدم قهرمان میشیم هتریک میکنیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90582" target="_blank">📅 21:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90581">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDOy_o0dJFVpf7BWAZs225uRVbC4-MmsrIURNDbI8pTzh_RrvEcquJGBclMONw1Czer14Yzp0vp99BClp_VtBxhSFg11jAx-FbbWr7EBpR7PUIq0xqfJD5SEbQ2SrNLl236ysYmfvod0e5-yXQRngo2k68NQ10prYwan6v-AjpleSqXbiH35Nu4GF6_HExMKbod8Qj40WLEihB4-DEz_sr-LYb4jgvA9g9ttV8N1wwC6-289km_YtoUWEyfIgKf6U1ZV4B3bECc8r0L6iIIgi1ozcb4FHWRZbt0AyvImL4KA0KPO9gCOCxkX97fY64k-OUlh2sS4dEFnD1BcG49wZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و جای ژانا همچنان کنار انریکه خالیه...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90581" target="_blank">📅 21:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90580">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f41d871c.mp4?token=kQ0TaIv_ErPQf_o6YI2yai_1t6TyIHXVcn32rCi3Rg7YSDMcKHOg3uZROoLDtg99HQa72CezpeTVD9prY_osUWf9R6zj-VZKX4q_P0STUgnAkzuaCjHbPy7GWTH_QvlWUh9gJB23JieBqzquR46akUchQpZjgwCOw-BvIQAqEnkt2b6w-xE7nXIwCBBy9l6kInEZUc_EvRd6pqJt98ARRYgTwNvcucCj9zfVnuOEMwWjNXtLDtmINhmoLtEolSLRJb_D77oRxn7b3khT_e7_KOWqejlDcuIZi8px4mXhqXFETpKLQwX_gylHFnMvN74DEheeIjq1NcvCQgS5R2f6FjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f41d871c.mp4?token=kQ0TaIv_ErPQf_o6YI2yai_1t6TyIHXVcn32rCi3Rg7YSDMcKHOg3uZROoLDtg99HQa72CezpeTVD9prY_osUWf9R6zj-VZKX4q_P0STUgnAkzuaCjHbPy7GWTH_QvlWUh9gJB23JieBqzquR46akUchQpZjgwCOw-BvIQAqEnkt2b6w-xE7nXIwCBBy9l6kInEZUc_EvRd6pqJt98ARRYgTwNvcucCj9zfVnuOEMwWjNXtLDtmINhmoLtEolSLRJb_D77oRxn7b3khT_e7_KOWqejlDcuIZi8px4mXhqXFETpKLQwX_gylHFnMvN74DEheeIjq1NcvCQgS5R2f6FjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
پرایم‌گرت‌بیل واسه دوستانی که فراموش کردن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90580" target="_blank">📅 20:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90579">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/870d923735.mp4?token=LYnMZu5-fEQ3JpoCm1rbAuIHFNjgwBXAzLw4CjRr1N8IxjFJevOjTODe_4CsJaHJiDgH2LqhAxGs6GaH41RGpjafbYwYl95mG7476lsHgco-0cTDx_K9Aa8GswF3l_E0N72RGmeyPnZkjIfj-ipX7_O9yrsAexMIw0QGDnm1kf4en8sNL-RmGnTQ2VzzbKsE_YyYbnU0w4wOCP458eqqg8TDPTfyvutAPeYXf9gpzbz7utRZQIa4oMS6t2qePCoKpK7LLYcVnDj0zrSVUAVuDENIrWAAgeITAtg_JUR8Cia5e1nVC96CmSBiOBEz3yZeU7bzoYOX0eu8Yw4E1u__KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/870d923735.mp4?token=LYnMZu5-fEQ3JpoCm1rbAuIHFNjgwBXAzLw4CjRr1N8IxjFJevOjTODe_4CsJaHJiDgH2LqhAxGs6GaH41RGpjafbYwYl95mG7476lsHgco-0cTDx_K9Aa8GswF3l_E0N72RGmeyPnZkjIfj-ipX7_O9yrsAexMIw0QGDnm1kf4en8sNL-RmGnTQ2VzzbKsE_YyYbnU0w4wOCP458eqqg8TDPTfyvutAPeYXf9gpzbz7utRZQIa4oMS6t2qePCoKpK7LLYcVnDj0zrSVUAVuDENIrWAAgeITAtg_JUR8Cia5e1nVC96CmSBiOBEz3yZeU7bzoYOX0eu8Yw4E1u__KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه صفحه هواداری اومده گفته که داوید رایا با این سطح هوش تو ضربات پنالتی نشون داد که اصلا‌ گلر خوبی نیست و قهرمان نشدن آرسنال هم یکی از دلایلش همین موضوعه!
این صحنه مربوط به یکی دیگر از دیدارهای آرسنال هست که تو ضربات پنالتی جناب داوید رایا قبل حرکت بازیکن برای زدن ضربه، شیرجه میزنه
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90579" target="_blank">📅 20:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90578">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">امیر قلعه‌نویی:
چیزهایی که سه سال اخیر به دنبال آن‌ها بودیم، در بازی با گامبیا به آن‌ها رسیدیم. بازی با مالی هم محک بزرگی برای ما خواهد بود
😐
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90578" target="_blank">📅 20:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90575">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daioRumMAQ1Y9OcdYae9sFRe7D0gan9yqmce3Vbu03Os0QQqHPhTyL1amn3Sc0EMhMWVjm9FdH2mfPfqabcY8KN2rsoiQm8qwA7qxpN_J1kXYrjHu7RRXR9JH8dwn4mrsNHLyJa3CTg9s91yd3LbgQp7IwyY2AeLjjorW2q80B1CF_Fmh-C4G6QC1HGTmK-idCcGb4AsIn2Tx4ATRn7PFotP3ncxmzaqXbJcxy65Z7khQZTbeHUhrK835NM51JELpmWorgOqhnCwC3GAeyF6XhhuWlPfob_CxytYucus3Yey26IqfdL80q2N0xcw4eQSZpB3O0tHbroyPFrriP898Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
در جدیدترین آپدیت تیم‌های برتر اروپایی، بایرن‌مونیخ همچنان صدره. پاری‌سن‌ژرمن به رده سوم اومده و بارسلونا جزو تیم‌های برتر نیست. در مقابل رئال‌مادرید تیم دومه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90575" target="_blank">📅 19:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90574">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
‼️
دیشب قبل بازی فینال یه هوادار یونایتد میاد یه آرسنالی رو اذیت می‌کنه که در ادامه ببینید چه بلایی سرش میاد
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90574" target="_blank">📅 19:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90573">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3p1V74eLS2gGGy3mpIiOKbWMhnJl8RXVTws4oPmFageaRqQKvhIh7OvCYKklqVNsVjM89NuzFpOihvGMfrn3NxKILMOKT3FC5By4urKFu7e7wvvSZHv_VF7SyKvw9Zo8tnSvIa-6Fda_T6fYTY4rCPH9S4_u_PIrY0qD--gJU54bxVJDu3TAK4dCxhWB7_4WJgU3YZdzW4z-JgKDCGF_t45ED4BYXZEADn-qvzTUtmlBiD3Mwglnfmm3BggYj0lZT4eYkpMKkQ2F2zady8W5CzTnAqTkD1aZejQFjjUpQDlnlypVT4b-xJAqAn8WoAJ_M2FeO4EiwuPJZ_WhEWNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کواراتسخلیا به‌عنوان بهترین بازیکن فصل لیگ‌قهرمانان انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90573" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90572">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">💩
⚠️
دیگه #فریب بونوس های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی #وینرو و با عضویت 500 هزار تومان اعتبار بی قیدو شرط بگیر
👏
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io  کانال بونوس…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90572" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90571">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuBVZVvMi9h5E6w9onTKcVAr0gfI4-nsB3HjXtOJUESIOvTe59z-2O85i4lZzquRZmOOaIOfmVDXjwqdNOkPoJEERNC8rFa4lsNG2CxKUM6lJagx4Q5t4Qvr4dvd5hs86vepQbQOgu4bR6p1gxSUCUSutFd5CopsoGV4PqKbXAWa50DCb6nY4OT9doUb4QH0Hzs1HDNO3iBLsjTZW1UddYotxodTLL2q7ocXJ1oq7GnoqC7DByX5DT5Wd91UsjSV69ekB1H5Z1X1sFNQ3A2qOva6S6roW-58cgqsIErNT5ZT_KbQdLZflHT9MHge-FgQR1L9YawqHgBk4H6Ttpj3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💩
⚠️
دیگه
#فریب
بونوس های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی
#وینرو
و با عضویت 500 هزار تومان اعتبار بی قیدو شرط بگیر
👏
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g10
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90571" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90570">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
اتفاق عجیب در یکی از بازی‌های آمریکای جنوبی؛ یه بازیکن وسط بازی سکته ناقص میزنه که با خوش شانسی محض و اقدام سریع، جون سالم به در میبره
😕
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90570" target="_blank">📅 19:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90569">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کنفدراسیون آسیا با مجوز حرفه ای سپاهان موافقت نکرد و بدین ترتیب فدراسیون باید یک تیم دیگر رو انتخاب کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90569" target="_blank">📅 19:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90568">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_-_WZevsO6epb3l6ZaJnQlEzPvdI4G3dk5lBPvi1pms9ITfzAPx2LS2O0nroVwDH2H3liU054XNAX6f_SioBNptExNH3qfxwdhXEVRloK9kzWW-zxRasS42-JPZCu7sjjr07FHjlZ7Oi3SgAYFdjZCovE1xM_COAeSrQFvYKMIIxliC0PDFTLw1Ab5IWxKDaOipa4V7C18CGUA5nuyC-nIc2kiKM5XZYk5cWZtCCynV_6c7UTxMKwAJpSUQYWTl046snIHIggZlQqH1CmMTlf0_aBiV2NhdUWcn4uWkPmb74QQ6vOzE3dkW5BHo_xRRIxxOSZHwhlAWFa8SWw-9Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌ منتخب لیگ قهرمانان اروپا فصل 2025/26
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90568" target="_blank">📅 19:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90566">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-TEmGwXrt6Euh5EfW6MUt0VJp_uDZxmQ6bTOnpll-xbOn1vsqC0fqvxVOP76qefX3BjI9Z61MrIQTmgEcN1uU7xcCqiHRDp-M01AkQtNEowhUYO1rPm1auP9-XeI4H_baNV5jDVEaWzcK4dltpsJCe3Q0tsw_OmiF0NkOoSZPzXVKu7Yyy4H-5unYRS7PwnKeHBRL2XlTiO9YQQj_cKta7Afdx4TVrb521Msb0FnTG3P8pkwnV36isan-AExMsI_skWgfhkFu3zUJVPwvFRjNhuuRVUou0Msp-tOiLpAMAM355K6Txmn4hzRDTS4fFBPQOMxhBKsTW-_i3If8773w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حدود 1 میلیون نفر تو جشن قهرمانی آرسنال شرکت کردن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90566" target="_blank">📅 18:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90565">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c385efd6aa.mp4?token=khjvoVjcgIiw56UuYwfC6ZDr2fpm5BqduRn_4u9-BTQNpR_QjecC6I7HTuhZEn-8ySFUu81UusNwYjh-wl-zGqlJX94udAWIju6unxbjOVUVSDk1ooPbMGDZuE3BZGzBM7sJomnuU9xRHPnFchoRsyZaVN2PatPiHsjNzCck5XKt_e3sKZuZXhp2KhN9MZNOqCEC4UKzhwj_uMZnBJCX8Rgia1rVEpEPkCB_FWhXvPC49sIIsl5UYGvY4O1uNImSv1beNB-Dg-nWX9dPRnjbigIlIwmOHrGZ3KMOAD1f0hbAzl2o1pQp91b39tCYZau0ggQjJJLESsfo8hrEIBT5dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c385efd6aa.mp4?token=khjvoVjcgIiw56UuYwfC6ZDr2fpm5BqduRn_4u9-BTQNpR_QjecC6I7HTuhZEn-8ySFUu81UusNwYjh-wl-zGqlJX94udAWIju6unxbjOVUVSDk1ooPbMGDZuE3BZGzBM7sJomnuU9xRHPnFchoRsyZaVN2PatPiHsjNzCck5XKt_e3sKZuZXhp2KhN9MZNOqCEC4UKzhwj_uMZnBJCX8Rgia1rVEpEPkCB_FWhXvPC49sIIsl5UYGvY4O1uNImSv1beNB-Dg-nWX9dPRnjbigIlIwmOHrGZ3KMOAD1f0hbAzl2o1pQp91b39tCYZau0ggQjJJLESsfo8hrEIBT5dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست اکانت باشگاه الچه
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90565" target="_blank">📅 17:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90564">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAnOIdnwC4ro6TN71hBWTPLESl63OBxJtq-JVzdGfUth1qVkHr55B1EWjwa-TtjiejqjIQ1td1wP9BhS8uPylYnBNKZh1modsSk_jVPOO50DoKdmtyKjUo8YUK_VCQiMzPx57RqQz4uB9GtZ67YBb6ZEU5_XMMzJ26amrLGniCTQRL6PLBJakkat7Mjs7oENZTNOXKmAcYg4txh550Mp0HrEIVitgpV5G6InRmt1jH3yIB77-mRAl-Hb975QCeQ1Twd-d4mgOrOQhQDLyFTLfEuBP4hSgnPYRlI4sjWmxVmAsTcLJe-H6IOHFhF6ni7W3J5kxICzqhtg5PBH7_H1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بیشترین تاثیر گذاری تو لیگ قهرمانان این فصل
🇬🇪
کواراتسخلیا : 16 گل و پاس گل
🇬🇧
هری کین : 16 گل و پاس گل
🇫🇷
کیلیان امباپه 16 گل و پاس گل
🇦🇷
‌ خولیان آلوارز 14 گل و پاس گل
🇬🇧
آنتونی گوردون 12 گل و پاس گل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90564" target="_blank">📅 17:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90563">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f90b184b2c.mp4?token=IiliLULFDMN0AVcTyqSFMO4BWXgoboQbXEw6VRQYC-0JRtcusG0Z2JfdYueyTM3tnLMih0tQ9vAZnCwgJ7dcxzXC735XIDpzfbc6-ye_QIQmwb3TcQWjggxgn6Zra5gVzf1nNYsa1ao1HxnPz-EZoIsuAHWO6tC4oP03CR22fJgXwY4S9r0Jaf9JJjvJ6JWPsyJXtNZwbN4-evEwIPug1pyKmCyfs6YDVHmZdmPc0LH32tAcRdQq8Fl1JThZK4NeUFX-o3xgmVQfl6e5z6g3QGhVPhi5RPXsTd45oWYMV4TY2_q5vYPUGTyoPGI2NKsIdItxcXRCYIQUQnBCoDK_1kEla1xlECT1W_RInVpkT5jTnYhltWTXO9T69djMGpoGCA34Qml9Tvp7nSK44gucpGhLJiQffvrnM-Hr3ny64Y36yfrEWTbGOrZaflUyZ0Vhm5rlp95wlJ7mNP5nQly7Gap-nKu7Ba-qdiTcaVN5sVKsU2KF8Tp9ZKblIgZrFlp9kWBCiz75Rc97r_PxAMVe9Cu3d5a-XagandKK_w6wyarg-2uhSZsSa9YZpNdgoUK2UxvJcDg3NVZ1AmY8gU-vmDxn4l6qqg47dZJge0QMHDI2h_VClp04vtJ491Ot7bm8P_cqPVMxUA6_GG1TzD7Y9io8rtUdF8opMP8HfdQg-dE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f90b184b2c.mp4?token=IiliLULFDMN0AVcTyqSFMO4BWXgoboQbXEw6VRQYC-0JRtcusG0Z2JfdYueyTM3tnLMih0tQ9vAZnCwgJ7dcxzXC735XIDpzfbc6-ye_QIQmwb3TcQWjggxgn6Zra5gVzf1nNYsa1ao1HxnPz-EZoIsuAHWO6tC4oP03CR22fJgXwY4S9r0Jaf9JJjvJ6JWPsyJXtNZwbN4-evEwIPug1pyKmCyfs6YDVHmZdmPc0LH32tAcRdQq8Fl1JThZK4NeUFX-o3xgmVQfl6e5z6g3QGhVPhi5RPXsTd45oWYMV4TY2_q5vYPUGTyoPGI2NKsIdItxcXRCYIQUQnBCoDK_1kEla1xlECT1W_RInVpkT5jTnYhltWTXO9T69djMGpoGCA34Qml9Tvp7nSK44gucpGhLJiQffvrnM-Hr3ny64Y36yfrEWTbGOrZaflUyZ0Vhm5rlp95wlJ7mNP5nQly7Gap-nKu7Ba-qdiTcaVN5sVKsU2KF8Tp9ZKblIgZrFlp9kWBCiz75Rc97r_PxAMVe9Cu3d5a-XagandKK_w6wyarg-2uhSZsSa9YZpNdgoUK2UxvJcDg3NVZ1AmY8gU-vmDxn4l6qqg47dZJge0QMHDI2h_VClp04vtJ491Ot7bm8P_cqPVMxUA6_GG1TzD7Y9io8rtUdF8opMP8HfdQg-dE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برزیل از همین الان یکی از مدعیای اصلی جام‌جهانیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90563" target="_blank">📅 17:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90562">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_68AxaBHVKsi8yPSIPiPd2RDPr5GcFc06TvFOioD9RjTw03Y_AIgptxY_7QE3oRTqVICjxGL6SORXxn1_AA55mfkz86XM-zIRbm7ZPldpq4mBdOQl7WaKybat5PYAnL8v9PZsacH6OuK3_mzwtSSLBrc__HCKdv_O2w-t1isPIaoBdBgTBt-HHP6J6NX-B8kitf5w_fVygF5O4yDzZdhmp43Nucc7vNkjRUs1WiWnmjrFPCudVwYfKLpKhOq_y4afq0_3oKRbA07Ael4yFvEgeeMzuoOKVytgmlMq27wNFSHzpl1_BNyUuZ70K-rn6lB9zJrnWzrXezKXJoZ2thUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نونو مندس ‌23 ساله با 19 قهرمانی
🔥
1 لیگ پرتغال
5 لیگ 1 فرانسه
1 سوپرجام اروپا
1 سوپرجام پرتغال
4 سوپرجام فرانسه
1 لیگ ملت‌های اروپا
2 جام حذفی فرانسه
2 لیگ قهرمانان اروپا
1 جام اتحادیه پرتغال
1 جام بین‌المللی فیفا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90562" target="_blank">📅 16:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90561">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYBHZuA6anCtU6-PkHmriyu6LXybbFEycZphDVoq36Avb7gNqQ3Wu9McPvLuIDlZzakStLAYC491Fzn8mbca2KylOqJlfgkTBVg7xFIj7ZQJnfK0eJmO6Bzxxvyh6aDxeaZGKJX2AyaLW023wlss1Au-vYbjK-NYQNuuOPpJMtKjJ7p0vFK9EoZM7ryEWZIlV0kLsSzGfH9nyJf7APoAKfpGwZloNPBPb1Ww_nuqNU0Lts5OSpIsa3EHoRYlx-uFlA2ultx62JMPQe5QqROweRVzUiT37YUmmGqf3Me6Hkuvzj1xgyGuZfVXcSjBBqWUIKUOoAO38FcWZ5CwM37rMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🤯
🤯
فکتتتتت پشم‌ریزون اینکه ویلیام پاچو مدافع پاری‌سن‌ژرمن این‌فصل در اروپا هر ۱۷ تا مسابقه رو کامل و بدون تعویض شدن بازی کرده که یک رکورد خارق‌العاده حساب میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90561" target="_blank">📅 14:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90560">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv4nOFoCP3Uwccf1AkSsdBj535yeuyHym4KI0cNCXbQkK8XQCz5EPn3Lcved1WB--lkFwiRhlTgkPI6ZMHmbIvnkFEycx_Dmtmmu6LOSCRzsUtrkvbG_y_8nBaoQuKFej7eIGeypSWW2YXvukM5j1qTOH3u3-U5SVYHLBz_IZ2j73QZYarpu-EPjrqtvQEnl_Vo-LQtXZmgKN-XhjbHcHG5hfQCKS8mcScSaAvJzcfHSSNqValWt3EUvZU4BGrCVtv31t5ASR6_E0V9Pyc7i2TxtToiC9zL3uauk44sOLGPyPP4PFbite0t1aLTj57e81kZMg7xGWCqvcTiiaURkgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🇫🇷
وقتی صحبت از ثبات میشه؛ کافیه بدونین ترکیب اصلی تیم پاری‌سن‌ژرمن نسبت به فینال پارسال تنها یک تغییر داشت و اونم گلر بود. خلاصه که نون تو ثباته و ناصر خلاف خوب بعد چند سال فهمیده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90560" target="_blank">📅 14:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90559">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ub2ZgBxUMMNiP5yE64NfIJ7-4YUBHZUwadTZpQsX3eBlVfRbf0oxVuRx4BHY_OKVIJ5_e8iDeL3DEBcnSEQKVTPt4bElT7J68I-YshGqdazOYhCrygOpC4bNRymlhdiP3EaJfMu6Kaq1yBgMxD-9bgTuYx6SGRqfvzQ3res4y5yTitV6apDlLa_oLwafnu1dCo5qLx4NpHm9GWMC_LXsbPEqYHcQ_LblEhtuY5Uc-fU8BxO3HV2k9kKAQ_tIrBHxwala0uG5T3lEWjaD_lK72VyEgbv-DzmNIzFvvxLS14nOQ4spyk0wtSZor2s_tOjY-ZoqBxDP1NkJL4ok8_jDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید صابر ابر بازیگر سینما
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90559" target="_blank">📅 14:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90558">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7MUKGw8HrWWHf0t4UW1vK3cf20lvLM7Qt1L8T1rFjDcf5Xi-RSGtotMiVwLW69PmJigsrVs4TXlhhm6Geo00njLrP1oTh31LgP4XQtTxQDW9MSabknQnQEkKU4RLlW32bTgysH-MFPthExdIbSt0UtTg9dIfE9An_NI-kUI_SjCpc5Hy6oAE_g7yl1HksVO63ekjcFO6GvvcgXpFf_tq2zIELW03WF11PzMiT9TmCoPx_fnXsktZpWnx4B4-5lD5ybYWSun5Ghqd3VdxP8CdyO0dI1jZYLjELRndp6TmO0UrJt2rItbd3rFpjg7SELbTNtur6OqTRoxkWsGbxsAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
کوارتسخلیا: بازیکنان آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بدترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خوبی بهشون دادیم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90558" target="_blank">📅 14:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90557">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbXoPcsndDdyqdG2X1dgRJ6Mn-xHcFD5HSkQLc5PPb2HE5_0jWt3oWKTkx41gwD6OUS3YPVHbxXNpILAncOXWZWTAYPipHZPJtu-qVqIf7oevlzzo0aq6Nx8_IZjHcqEuD0JfSIuFAo7a6nak1OkFbYTT9BkC8JQGKN-myJC3TL9PfbCiwgQIWHP6R5LOh5fvvqgwJmxB9VD52DgtAkNkdEFUpEDy5X5_OVb5cix9RHNwzdoGNPZATMQJHRlbV5uJAijbPTvtfIIuH4yF7pfkmv7uUT8J-39_GvZb7-zoXZQxwZ_5bowd1If_uZfPudBUylvt_gDI8CIOhMJBQBSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
وزیر کشور فرانسه: در‌ پی آشوب دیشب خیابانی در شهر پاریس، بیش از ۷۰۰ نفر بازداشت شده‌اند و حدود ۶۰ مامور پلیس شدیدا مجروح شده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90557" target="_blank">📅 13:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90556">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGlc-jNBfUehZ5s85WL50BqzU11WejRdBo5p6p_FvlrCIyFCjnmXXUhDL_aUlAvhrUmihokkjmd-gab05tqTGNEODlTXz9ghpJ0xr5pyD1LCZpS_X7glA9CFNuBNb-NlxAQRF4qOmUFR0J-FBxrkgKTgKVuo49j5MA5JKmdqXjkbUWqjkWZonen4brlVFy2r4aFR_bH3SV1KAAWzi7xqd0XX-pivpEciraLww8OVyXHdOu_ZiqELGeO01Yg3JHBpN7KE7ttEVtbw3BFaeQFihIOEVY21ML73RABOL3syyTTctLwJwQxeELJ2LRsKqlguHF7NNOcXjpNkdNQ_sjYh4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
وضعیت وینیسیوس و دمبله با و‌ بدون امباپه:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90556" target="_blank">📅 13:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90555">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq7c9nPrU46AsSmFfP4--PNyJgPrOc9TErYmfLNFGuKIendyX0sylTVGzBSWKBwl8DwM25CHUA_98obpMqJOaoXwe9hXtiuJLboItYkJ3-ZjXaFQxu19lUiiYDFrhdRHzlqlo1_6SttQWYd7773NTUeT4DhguxKQSCcAlIF1bTjLDkqvoCr2bGh-IUWwgCY0UoNjnfwsI8ETA-OxBRK4bknRtrfoC03QtecrTDY29LpfJ31y0VmvF62-rBAolKyTpMRC1ngDCTmQmgDuqoDC-wGqQNYfXQAfO9B2oNtWgF1p7ByNa9ods1_e7J8Km1gKFWjYOxwY4djgeCtBJrX7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مونیرالحدادی بازیکن استقلال و همسرش در تعطیلات
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90555" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90554">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90554" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90553">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZV42tTLsjNERMdzW189SSp8CHp1BaO2JgBFkHNhWormhnMH7ZazZMzQuJ0WYPi1tbONahXyZDLfe3p2Fb48AJTD_ThJbO9A1DquWz3sEyQ4L8Yh3_95kbRlJO5QjOYPAHa-rtGrt12RGgfF7mFpSpjPzQocPwB_rcpQrTcs8d-eI_3Hnid2wvGZlk-W231Vv5AzwqKEBWHlWkYtY39_2f-68pkjxkXAQRuC8-paDCqVAkE-tSUPC7UQ7-roK4T0-86DEmufm5zy9vqthzuprlCDq6UYu36Wt4x8I0rmsPsyzMTY2Izi2b7N0W8SCrO7P0UW5JKZRdGs99pQY3yKx_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r10
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90553" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90551">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8df4a4da.mp4?token=L3MgbTM0GsIAXkwzrCXLWbVDsfHUEStk4fhugXhqKO8t5fT-lK_AtGLDATNsO2Vtt9b4OKvHJb3OmLupgMFMC1bcVKZStVfWaZtJGGHzTHXvvTHmry_9rZC1NntcEXDyanqLQ_SdOnwiwdFDk1YuMlTV7rqKAPgZ1QupnNv-sRUPsG-7lJZPzW9BMPSWQePROkzmWa--zPlvGz5gWg6KstY1KRum9dClbTBo9vcEiLufDvXEc_KqmGqwTV43V5mETWZ8R-HI7r38SeDs00bQrN9_DUMXMqVf8EX9oPFaxrOJa4lxEhiO9Oeql2MIvN2jPt8aGFOyyRDPMx5k0_Oz2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8df4a4da.mp4?token=L3MgbTM0GsIAXkwzrCXLWbVDsfHUEStk4fhugXhqKO8t5fT-lK_AtGLDATNsO2Vtt9b4OKvHJb3OmLupgMFMC1bcVKZStVfWaZtJGGHzTHXvvTHmry_9rZC1NntcEXDyanqLQ_SdOnwiwdFDk1YuMlTV7rqKAPgZ1QupnNv-sRUPsG-7lJZPzW9BMPSWQePROkzmWa--zPlvGz5gWg6KstY1KRum9dClbTBo9vcEiLufDvXEc_KqmGqwTV43V5mETWZ8R-HI7r38SeDs00bQrN9_DUMXMqVf8EX9oPFaxrOJa4lxEhiO9Oeql2MIvN2jPt8aGFOyyRDPMx5k0_Oz2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوس بازی‌های قبل ازدواج لامین‌یامال و دوس‌دخترش که در فضای مجازی وایرال شده. فک کنید ده روزه دیگه بازی داره زیدش هم اینجوری میذاره دهنش
🙁
😔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90551" target="_blank">📅 13:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90550">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAZ5wa8ypwmItaZ--p224G3PrdhjqFryaD57kCMOeNY7b6-ESf2Ykf_8Pij5vtVDSgFoJeIJUycCda1cgjaLdv9SffF8H4yBOBNF4fBTRj2Ey0BZuJWlSS5ItUpmF07nYSZFExIe8p0W_Rmi48CcL71eSDG2v-GAn8alL45pKuvudeEgOPOMSU_Z6kR0-k5wxP6KMtuvaTEGa6nHFt-zDBBw5bg34ylF4OfWsF7JhfJ0tMxxlu4Iok_llk_dA193XhfIwLK4AwsWjuEy3Ij0gX5EnFpnyHeaonutPdtvV3Tqrn5w-Fl6w18XuwpPEO6WTG51W83eoGACiKnnYH1GnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ روزنامه‌ اکیپ فرانسه مدعی شد که ناصرالخلیفی به مارکینیوش پیشنهاد داده که بعد از جام‌جهانی به تیم الدحیل قطر ملحق شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90550" target="_blank">📅 13:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90549">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3-PB2ZPFnks5Ik0YDDZnXW1EY7hDRgztotTwzIEUoUQ3BBeK58dqReQmDKsB0botRz4r5vLlzdNl29MS_V5tb_4pab1VlpzzS8c7oqP58OcpZ0YtrISw5q5GTxRyi2bbdUOymex_HOFBJLjieEZpNUyjuQSYMN89nkeadVGBKhXnYxr9M11KTAnSvSx2q9f01ga4ON3o5mLW86njQpr3THzBwW9DcFesg33a8YmyWyA3TxSFwhRY1V_6zrxHOOv1JT-CXfJxlyeKxDMHZ0KF7CUoijMHq0Ks7P3XCQ_GZEi5cAViQuDJ_gafikfnUdMDiXvCF3eJMZzMDs3V4A8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخت و اقبال آقای امباپه رو مشاهده می‌کنید:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90549" target="_blank">📅 12:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90547">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnuskkwMNr7FRnUi-Y8jACs0A5dSoZO-i8GOO-FiREnoieoy-vOwuslUGslphrg08ohmFebFRR12Z5daMfrepqd_YAzaSWMPoPzv50XV1PAMIvROourzF4Gh7gUPqHSxRolodfpoa078Tx6JrHU7PKeC3-dfFwNftvY2MrEZCmUfEg-FGKhFYVh8POg3W7Hk0DEjJ1dU116GCTdKWGvv720Ecz37FKohAWP_mIU4oag6-Mmvf-78RQV66QqpumVQhJS4_cay8kSIJQagdj7bN6WZm_hJ3-A3FFIrXvuwNij03sKmn0e7puYYL5pWhcT6KOxAj2obCld0bbeJA3vo0ATEkGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnuskkwMNr7FRnUi-Y8jACs0A5dSoZO-i8GOO-FiREnoieoy-vOwuslUGslphrg08ohmFebFRR12Z5daMfrepqd_YAzaSWMPoPzv50XV1PAMIvROourzF4Gh7gUPqHSxRolodfpoa078Tx6JrHU7PKeC3-dfFwNftvY2MrEZCmUfEg-FGKhFYVh8POg3W7Hk0DEjJ1dU116GCTdKWGvv720Ecz37FKohAWP_mIU4oag6-Mmvf-78RQV66QqpumVQhJS4_cay8kSIJQagdj7bN6WZm_hJ3-A3FFIrXvuwNij03sKmn0e7puYYL5pWhcT6KOxAj2obCld0bbeJA3vo0ATEkGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکا اومده یه ویدیو گذاشته از اقدامات سریع در حین فینال دیشب و جمع‌آوری صحنه کنسرت قبل شروع بازی در کمتر از ۲ دقیقه
حالا این سرعت رو مقایسه کنید با پریمیرلیگ جذاب ایران که خدا میدونه همین‌رو چقدر طولش میدن تا جمع کنن
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90547" target="_blank">📅 12:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90546">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👀
لحظه دیوانه‌وار قهرمانی پاری‌سن‌ژرمن در ورزشگاه خانگی در پاریس؛ دقیقا استارت آشوب دیشب تو پاریس از همین جا بوده!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90546" target="_blank">📅 12:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90545">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozjHBMFRwpa_gzUUxTI6bvhqYTybQFxOiHsDLgAE-RRl1UFK-kE6FKSrr1xVmkzkDZc2uG75WDNcf9UYCYaduDFLSzzykmw17uGm_0NkBYJJorOOVmyVFpEU9O-2WpgvW5_0lG6xg7DxhOrFtKuec827wl929lD4cPcJ-3nEjMMFYdqN7zQ74yJciWYgVOOzOrXBO-8K-3vEDcwjcpkyClell1NyandvNkjN4kM3DyP2zsCBRd57Eoc-Q_SIcXl0ahy7Y1yMq-a6zajaMX4YGr3wpbLa6-btHIae7_2w9vkPSK3lKEonW6tNgOGl-O1oKVxW_ANVzYLdtvQuBj5zxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرکاپ اروپا
استون ویلا Vs پاریسن ژرمن
22 مرداد
آر‌ بی آرنا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90545" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90544">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dd57d3d9.mp4?token=uqvSIaeBOXhJAjLkVDc-iAmoM2NnHThrr5sRmx0T-ZAYAWqaXGyYcGb65AOL5Q6rhVRgasRflDcSRRXhkXdQQ_n3pKycdIkDNH78JjeuZ9Ivq9D8IWi3_68m0dNm3_CeCEjtdkeJWdp5-F3ErYVpbLnI8-kx6uI6FOytxzcmmB5bNCyJ-0XKSyChnPlYuz5STwoD36106m2doWLcRwwqU1Pi8XD7SgSxpiI8CRgJHEfNfZjaT3XyIhPbfbBa5aUvUCARk0_A7wNuhXciUiC_m3hnn5BriCfGoZ3DltXUFKzECySfVdBmsAYa9QVVtl3FZU0Uiwp3kl7177atKxqI-TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dd57d3d9.mp4?token=uqvSIaeBOXhJAjLkVDc-iAmoM2NnHThrr5sRmx0T-ZAYAWqaXGyYcGb65AOL5Q6rhVRgasRflDcSRRXhkXdQQ_n3pKycdIkDNH78JjeuZ9Ivq9D8IWi3_68m0dNm3_CeCEjtdkeJWdp5-F3ErYVpbLnI8-kx6uI6FOytxzcmmB5bNCyJ-0XKSyChnPlYuz5STwoD36106m2doWLcRwwqU1Pi8XD7SgSxpiI8CRgJHEfNfZjaT3XyIhPbfbBa5aUvUCARk0_A7wNuhXciUiC_m3hnn5BriCfGoZ3DltXUFKzECySfVdBmsAYa9QVVtl3FZU0Uiwp3kl7177atKxqI-TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو هم تو فضای مجازی دست به دست میشه از این بلاگری که قبل خراب شدن پنالتی دیشب گابریل، میگه توپ گل نشده و پاریس قهرمان شده
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90544" target="_blank">📅 11:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90543">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔵
عاشقانه‌های بازیکنان psg با زن و بچه هاشون بعد فینال دیشب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90543" target="_blank">📅 11:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90542">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6ea91f0b.mp4?token=W1cU50Ao-CyeYf1WIcd47zofmgePe-PuIPqBYJESjVm53Vk92Rn0G0dDb7_0TzdAvuFxcAi-imwsHqI6gn_VYL3nFDPG47FgKsaVh5aP9eCXd2cfuVYdoJaBe_EIdha9FdNDZyyKqyGhNtJS6ERlngQMvbcPeFGOwTGmqHbVU5LwxRuqWN-vamT4WN72YXgLfD_yJ9tGGHQOcLmFJnaqXBb2NLbvzzsBxkxasA4a7Gu2e5IvDDz1lqe_f9oYvqhIt0iKBegGzW9uVwXSWT8xf57mV70UiWXyKnkbd-Giu-ywz4XyEscQVmJjS2LxCh1jqW7nGLxczzdUiXMka6AQDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6ea91f0b.mp4?token=W1cU50Ao-CyeYf1WIcd47zofmgePe-PuIPqBYJESjVm53Vk92Rn0G0dDb7_0TzdAvuFxcAi-imwsHqI6gn_VYL3nFDPG47FgKsaVh5aP9eCXd2cfuVYdoJaBe_EIdha9FdNDZyyKqyGhNtJS6ERlngQMvbcPeFGOwTGmqHbVU5LwxRuqWN-vamT4WN72YXgLfD_yJ9tGGHQOcLmFJnaqXBb2NLbvzzsBxkxasA4a7Gu2e5IvDDz1lqe_f9oYvqhIt0iKBegGzW9uVwXSWT8xf57mV70UiWXyKnkbd-Giu-ywz4XyEscQVmJjS2LxCh1jqW7nGLxczzdUiXMka6AQDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های انگلیسی از این واکنش دیشب رایا وسط پنالتی‌ها پشماشون ریخته و عملا گفتن این گلر کسخل مسخل از کجا آوردید که قبل زدن ضربه شیرجه میزنه
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90542" target="_blank">📅 11:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90541">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=hIbr6PzOQ_jGxR6dhhauJSn5QCGWmiheqIe95Xhm0wI_cLcab3LxWz00cac80nwQaESLnCz3Kw7FpABIwLbyVcVFT3gMDD48JtvQXoWqw-zOhrNIrll2XHzleycMftExeqY84t2FzGJ4IHZPCMVOoybkgT8OmY7PfWLtgFVro_2vHvKaO1juNB2sekCDZFsJCSBft_gGFav3DUzUDgV6tneXxjhgyfo7recFTU2lI_OfBkT8ihw-xbd19j1KhD0Ulapt7RAo3Q8X3JRW3FOK6oBuIPV4dQfAx86OAkO0ymy69VlD6gHJoUBZmiltmEzWPNIKxcW1XeX6WWOcP58luBrc-C-r497iSEzKEXbUnFRPw0OBu8mHU90iC4WEWBm3zB4D-gLckHpVmVi4IzOOLkKyV1hKfWd4xG582lRbU4LAgAA3uBfhQc177PMZKK3ESIqmOVsH3VclLUBvNPNn01jygBLSNCf94AlB2XAH0ZWdvTj-VvMoOZ4ZUJoN3VSMWynDKLhBIL5JCDX1HVzFsTkKvuvJVIn4ook0sjwxnIkHa5-PaGOsypHfbME364eXYh_HM8w95YTKQYal9nG5BC3lHBDARf9LH4Ihf55_nne6w6hjh9Dlcrunk8Fbu1RLCqkLiOSejEMa_qUVqrFLe7EKFcuSCqr75EFULF554rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=hIbr6PzOQ_jGxR6dhhauJSn5QCGWmiheqIe95Xhm0wI_cLcab3LxWz00cac80nwQaESLnCz3Kw7FpABIwLbyVcVFT3gMDD48JtvQXoWqw-zOhrNIrll2XHzleycMftExeqY84t2FzGJ4IHZPCMVOoybkgT8OmY7PfWLtgFVro_2vHvKaO1juNB2sekCDZFsJCSBft_gGFav3DUzUDgV6tneXxjhgyfo7recFTU2lI_OfBkT8ihw-xbd19j1KhD0Ulapt7RAo3Q8X3JRW3FOK6oBuIPV4dQfAx86OAkO0ymy69VlD6gHJoUBZmiltmEzWPNIKxcW1XeX6WWOcP58luBrc-C-r497iSEzKEXbUnFRPw0OBu8mHU90iC4WEWBm3zB4D-gLckHpVmVi4IzOOLkKyV1hKfWd4xG582lRbU4LAgAA3uBfhQc177PMZKK3ESIqmOVsH3VclLUBvNPNn01jygBLSNCf94AlB2XAH0ZWdvTj-VvMoOZ4ZUJoN3VSMWynDKLhBIL5JCDX1HVzFsTkKvuvJVIn4ook0sjwxnIkHa5-PaGOsypHfbME364eXYh_HM8w95YTKQYal9nG5BC3lHBDARf9LH4Ihf55_nne6w6hjh9Dlcrunk8Fbu1RLCqkLiOSejEMa_qUVqrFLe7EKFcuSCqr75EFULF554rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیچی‌برگردون‌های پشم‌ریزون پریمیرلیگ در سالیان اخیر؛ واقعا هرگلش یه پوشکاشه
😮‍💨
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90541" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90540">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a27edc87ad.mp4?token=puyhakEP4OZ09ZW0cKLpDXfsrbj5T_PT3mJvUr24PzLlB-gDoyo1mk8RzQXZaCi-LbPbKqxne2BxCqHo4z6UmGTfXoRc0zcebl1jjY_sUprsYUVv9yKswixpYFmEuTQWRaoNQ9U3MZxwLIU7jeqcHZNX4hFsa7JT5qfUnyiTFDWT-yhC-4cwOBzWruJkVf4GWR1zZ8CjfAx70X3VOkijOjKzmadUUodLFI3zU97nF38n7OGy6fQvcCG7clIHv_f80lYj34BmaJczg0xmNtiwaChfolviIX9cl0y-zATEKqIlqkseV0YVuLOKh-14BioOlqi__uPfNperjfdgsunFig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27edc87ad.mp4?token=puyhakEP4OZ09ZW0cKLpDXfsrbj5T_PT3mJvUr24PzLlB-gDoyo1mk8RzQXZaCi-LbPbKqxne2BxCqHo4z6UmGTfXoRc0zcebl1jjY_sUprsYUVv9yKswixpYFmEuTQWRaoNQ9U3MZxwLIU7jeqcHZNX4hFsa7JT5qfUnyiTFDWT-yhC-4cwOBzWruJkVf4GWR1zZ8CjfAx70X3VOkijOjKzmadUUodLFI3zU97nF38n7OGy6fQvcCG7clIHv_f80lYj34BmaJczg0xmNtiwaChfolviIX9cl0y-zATEKqIlqkseV0YVuLOKh-14BioOlqi__uPfNperjfdgsunFig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضدحال عجیب و غریب به تماشاگران سر صحنه پنالتی آخر دیشب گابریل
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90540" target="_blank">📅 10:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90539">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exDyEltFzzGUaBm-8dAozlFgvVwzgiImmwQvG7WGGetkKdWkph3MeR0-VaihXj5ObMXVnUajer9mMpDjAeOlbs-CxeOYn7qElWjHNwV2UZex1iT2oOlbvP9_E2Oh23WlkcTDcgzOaR_Tn8Weso2MGqOFhyl1BgpLDX4xcC67q5vvXN5OP_1p0kx11xu7dBiuGZA_eJs_ZIe2FXlQ3KQ6yRGCAJy0mz5QYsjHEt-v4xUkInAmH6ZlLGSYAnSp30p1TGqcE8jV-A8sVNQBkqYk7QWBGEsbDWKqgUcOJ_mXN6opOfuMCqZXhDakLZmUX_A1DeTA2dZPnkiUkNQlArXi7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رافائل لیائو هم این وسط اعلام کرد که دوران بازی در میلان تموم شده و تابستون جدا میشه.
مقصد احتمالی: پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90539" target="_blank">📅 10:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90538">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888a4aa5cf.mp4?token=ZjAzm6BbJXlsiUArsn-ZzRBHCmbjisx9wzdr0rak9hkHXtTy9i2ozggmvUohZ4r3D6cRcJpTzdXmpQlwaY5sz3TZLuSspwF-1kUJAAQGnuGB3Hjm9GgBDa-p1wzfZIVr4B7tAArGlhC8v2pdje9qpLMuq3eLSNrFlKk-iIyFJW7uLT5qnGwp8yxX9_q6myLbjp-1WGg53UdBocY2kNEtV5N1q8LaAewUEPekxdBhcx_OXy8qtK6li2PIF13XnkcLTsRjfCCNdVGqTaywyTd240XhuFnrtkRTFEsSMqj_dfnc958QJb-MyXzrdP5GkXj3PkgD4E5qIqp4xZa4V9RmMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888a4aa5cf.mp4?token=ZjAzm6BbJXlsiUArsn-ZzRBHCmbjisx9wzdr0rak9hkHXtTy9i2ozggmvUohZ4r3D6cRcJpTzdXmpQlwaY5sz3TZLuSspwF-1kUJAAQGnuGB3Hjm9GgBDa-p1wzfZIVr4B7tAArGlhC8v2pdje9qpLMuq3eLSNrFlKk-iIyFJW7uLT5qnGwp8yxX9_q6myLbjp-1WGg53UdBocY2kNEtV5N1q8LaAewUEPekxdBhcx_OXy8qtK6li2PIF13XnkcLTsRjfCCNdVGqTaywyTd240XhuFnrtkRTFEsSMqj_dfnc958QJb-MyXzrdP5GkXj3PkgD4E5qIqp4xZa4V9RmMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو مسابقات پایه ایران، یه گلر وقتی تیمش جلو بود اینجوری برا حریف کری میخوند که در نهایت ...
خودتون ببینید عاقبت گنده‌گوزی چی میشه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90538" target="_blank">📅 10:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90537">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔥
برندگان جایزه پوشکاش در ده سال اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90537" target="_blank">📅 09:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90536">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a192f49940.mp4?token=Gp5nQlN7eCIYKXP5DZnI7UvrjBy03lZK05GLhveJ29eZfkdLOlJpROxwktXORH2Y1E-SwmvMc0w4CGa7kP1nzsnWx-ecI7znUpbPABtJEgZo3u60sORjOgLdE_cNLZ1V1JYoAC84z3jfnQ7DMP3Xnm4DycItuuUfv1Glhah47dIGFhGBjXrPFdncUJtdPfRmROk040Axm5jUPFUrXglC8CPPWhsEV0jzGu_BuvUP4b0sEU3olCnx56xC_AzuhkgjVvj9oCOFUWslYJmY2vdfzcdcDt0-FOl9JItNZ3vFzy5W6tD9WTlcmDENPcu0_Fq1iHmavR5aWh0_9uvMZM223Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a192f49940.mp4?token=Gp5nQlN7eCIYKXP5DZnI7UvrjBy03lZK05GLhveJ29eZfkdLOlJpROxwktXORH2Y1E-SwmvMc0w4CGa7kP1nzsnWx-ecI7znUpbPABtJEgZo3u60sORjOgLdE_cNLZ1V1JYoAC84z3jfnQ7DMP3Xnm4DycItuuUfv1Glhah47dIGFhGBjXrPFdncUJtdPfRmROk040Axm5jUPFUrXglC8CPPWhsEV0jzGu_BuvUP4b0sEU3olCnx56xC_AzuhkgjVvj9oCOFUWslYJmY2vdfzcdcDt0-FOl9JItNZ3vFzy5W6tD9WTlcmDENPcu0_Fq1iHmavR5aWh0_9uvMZM223Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چیزی که اینروزا اتلتیکو بجای آلوارز به بارسا داده:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90536" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90535">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae10b6cdcd.mp4?token=fC0YAKYg1ck67hUKMZWend9MXQDdwn9NNEqel_jfhSvKEAjKwLmhihXKeoMcjLGNvMRxTLCig_xboNk6O3QZZUlSdQyQqx7xqcKJw-OQGl3ukuSAdxk9JELmXv7MAVoqmk5OF56-nhOwPAqT57-MA_eLssy6TmYntuJdUCTw2jo1Ev650EfcXMDgbqDhlqZkKdKdw5z8C6-4aC7xM6xUW4BGkMIyiY5xVmyEKNmUWYRoEc0IKM4ezF-CDzDDWugtPTAYiUNUxOgQTJWtndP-NVuEQ8esCnSMRQMjD32d71gSKZJjc54inzjgV8UZvCwjwxSL4-ePC20XfPt-bCJp9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae10b6cdcd.mp4?token=fC0YAKYg1ck67hUKMZWend9MXQDdwn9NNEqel_jfhSvKEAjKwLmhihXKeoMcjLGNvMRxTLCig_xboNk6O3QZZUlSdQyQqx7xqcKJw-OQGl3ukuSAdxk9JELmXv7MAVoqmk5OF56-nhOwPAqT57-MA_eLssy6TmYntuJdUCTw2jo1Ev650EfcXMDgbqDhlqZkKdKdw5z8C6-4aC7xM6xUW4BGkMIyiY5xVmyEKNmUWYRoEc0IKM4ezF-CDzDDWugtPTAYiUNUxOgQTJWtndP-NVuEQ8esCnSMRQMjD32d71gSKZJjc54inzjgV8UZvCwjwxSL4-ePC20XfPt-bCJp9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوتی‌بازی مارکینیوش و دلداری دادن به هموطنش گابریل بعد خراب کردن پنالتی
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90535" target="_blank">📅 08:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90534">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5c5d95ce.mp4?token=TT8ledQq05HOSSauXrm-utmU9uRNV42tufBH25EsuUw0o0g3QWXnqNfHcyNO2SntdO8fCi_QILOVF9m_Gt4gy_V43Ujhq8i3iHB44ymLQzMqb2Qe6QOi3XA4xeceCK4UAq2d8vSeqzs2Lr2blN1y7Yyk2hvU47ZBj8wU-mTxo01G9lGQsHno7j_tK5QsossupLdfe8N2UNZxI2X-uBXlpKnWQFi19dePEafCsc4eKPUm-Ihxuc7yB1-I0BLmUnrGiIEyKkabwDnKilhTM2nb43cFamQt8HbggsTZHPhOmrEbU2XfCDmKB5rIwF7XLcgbtnwdYVtSJW0E-oexrPz40A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5c5d95ce.mp4?token=TT8ledQq05HOSSauXrm-utmU9uRNV42tufBH25EsuUw0o0g3QWXnqNfHcyNO2SntdO8fCi_QILOVF9m_Gt4gy_V43Ujhq8i3iHB44ymLQzMqb2Qe6QOi3XA4xeceCK4UAq2d8vSeqzs2Lr2blN1y7Yyk2hvU47ZBj8wU-mTxo01G9lGQsHno7j_tK5QsossupLdfe8N2UNZxI2X-uBXlpKnWQFi19dePEafCsc4eKPUm-Ihxuc7yB1-I0BLmUnrGiIEyKkabwDnKilhTM2nb43cFamQt8HbggsTZHPhOmrEbU2XfCDmKB5rIwF7XLcgbtnwdYVtSJW0E-oexrPz40A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاریس دو سه تا دیگه قهرمانی چمپیونزلیگ بیاره از اون شهر فقط یه خاطره میمونه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90534" target="_blank">📅 08:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90533">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP یونی بت شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9: https:/…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90533" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90532">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzrsW71quPcrOmuAnSFV6GJy2Nw_BaSz7kBW4t2h15cVMjzbKHzaN8IefiSMzTQGMjTkvaAFfEgdmS-u_yJ0k6r-eerA_l3TRECx3_6JLCaIGZNfwiAtclF632F5tfiOHWm5b-6qHLeldkgf3gBHnx5uMKYiDFgy7g2R4GaMeKOqTe6LEhrU6_ATuf7_AsvvVzjTjP2ca1n8oRt63hMOfBy4LhpODHnaFnQ0saaZSbezptYqGmy1afxHh1fQ0BBaKfQ3RlhbG0zu4s_JQY1P0YkGS1gm-vftWLh1nWJYgsOkRb-G8KZ_tL3QNu7BOSjC6WA7-GggtluLbw8Ts09M2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP
یونی بت
شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9:
https://t.me/+YwYFluMQ5-kyNmY8
https://t.me/+YwYFluMQ5-kyNmY8</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90532" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90531">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGpmD_EhXaxNBsx-7dQv4XHDYSSoJ8bi7QIskGboIBlb8IeBoqAaKsexG6WqASGg-r32EUSc0pMB_GZv3IPXDE5DRrkFcNwxn1Lby9k9ksw4ascVkI6oMARqa_Zb0Wim7Sh2juYGMZX8YvPqrWfrGNxWBjSjup0xNsqY9l6AFDN74BocMyx10kiQRc-uyHhIAVlB79RRPXz19taD6IsZ6VDoU-DMGAO2X111GlbSU61Xgne96SAxQgyOlb9AtF5W7PnMlTBciWHPcHgknb5JQi_zsb2r_VIIyCZrf9mQvbwd3EwOd4_KBeGKSKhqPj00ynLwFya5Ot9lE99QpdtUHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
شماره 10 برزیل رسما از وینیسیوس گرفته شد و به نیمار دادن. البته قبلش توافق صورت گرفته بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90531" target="_blank">📅 00:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90530">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac643b260.mp4?token=bb16iDYbxfcyyORdn0MjNz9is8l1DFgrt_0toJRduLHO1YD-1uNX-WZ2YxlZKKQtOeBHjP8svEbSGRVFjQX1HJaNRfSzsQEop-UpCTpxCFauzm64N0uwGSd524eQKJwWoqHKjm-VpcNb4R2cz9Kn4oKpF8HR0PzUL768yCv7xK3Ol2X3C8vtYMCIOXtP1-59M83GB5NzZW3-L1OIIhFuULV8GgwPWDtSDdrJfjHXG5mMmxGx5veAxQO3LwEeS7LA34WYD706yrBSiSiH5K1rgs-t4_hXYPVEo-UfKHo-ZEV3lzC5ewRAUNzlMBtxBRwWWni0AEF2JuKFnizYsO8uxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac643b260.mp4?token=bb16iDYbxfcyyORdn0MjNz9is8l1DFgrt_0toJRduLHO1YD-1uNX-WZ2YxlZKKQtOeBHjP8svEbSGRVFjQX1HJaNRfSzsQEop-UpCTpxCFauzm64N0uwGSd524eQKJwWoqHKjm-VpcNb4R2cz9Kn4oKpF8HR0PzUL768yCv7xK3Ol2X3C8vtYMCIOXtP1-59M83GB5NzZW3-L1OIIhFuULV8GgwPWDtSDdrJfjHXG5mMmxGx5veAxQO3LwEeS7LA34WYD706yrBSiSiH5K1rgs-t4_hXYPVEo-UfKHo-ZEV3lzC5ewRAUNzlMBtxBRwWWni0AEF2JuKFnizYsO8uxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جام‌جهانی نصف شب با گزارش سرهنگ:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90530" target="_blank">📅 00:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90529">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkkOMQB7daqIhuYGV6exAiHwIk6bwyl6bs8vdpAXCf4MVCHv9RktLwNYDNEtVskMn5lgtNvTYzbymsgc0Ri_3zO8zLxvwBWfbQIBa95jiCI-XuFIGw5BD-QTa7i7Z9MndgT9fNi2hbj6_mQtWAF1ZxWS-_trxFsUNmau1LngpSLlsGybH0P85KxS48ZTXwzBVmhm5u99AJMWCjrGwEruXsE_c_yReWc57-9zcwZP1x_HDNsTS83WAgvSeSMfsXsGodF4eJgfQMpzJjeVoxiS6bDDJmCTWVbxYeRwSPZHXrPT1pHmXIDGWDr9bUNgmLKQOjgDqbWSE8hDssLwX6ijVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه با 15 گل زده آقای گل این فصل چمپیونزلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90529" target="_blank">📅 00:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90528">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=mjb3VVQBEedlWOlUJaC7eNN7tzrP1zEIKPYCVwMlA96HvY89SC9vRl17MQOdT215SjbPw9kXsv0VmTYs7RfiSd-hOb-fSW_tRsL9ZvqVrfDnDJD3lKHXjMUik8mAkpnqpN1Kh6ioBnW-xyGXfaFQI36AVN8k4L41kQHMN_YafxATYJ6LzGSg4IPX3kuxMO6E9nWnnaHsad6TbacPtmiZEP3QRLHkpDNMCLkYBx1WTbqm_cdqYDsAJLP53W97cBzDAyOEdn6tcv6NO1iusKV4qLcpfzjNmmeWztIrhI8Rrp1_W6Jh0dI9XK8FishaG_WJ-yeEPNskz6TvzKYOzRuQIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=mjb3VVQBEedlWOlUJaC7eNN7tzrP1zEIKPYCVwMlA96HvY89SC9vRl17MQOdT215SjbPw9kXsv0VmTYs7RfiSd-hOb-fSW_tRsL9ZvqVrfDnDJD3lKHXjMUik8mAkpnqpN1Kh6ioBnW-xyGXfaFQI36AVN8k4L41kQHMN_YafxATYJ6LzGSg4IPX3kuxMO6E9nWnnaHsad6TbacPtmiZEP3QRLHkpDNMCLkYBx1WTbqm_cdqYDsAJLP53W97cBzDAyOEdn6tcv6NO1iusKV4qLcpfzjNmmeWztIrhI8Rrp1_W6Jh0dI9XK8FishaG_WJ-yeEPNskz6TvzKYOzRuQIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل گزارش امشبش رو به این شکل شروع کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90528" target="_blank">📅 00:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90527">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA_a_e58RpiLJm_vI_UBe-nSYIgZGIc3FABrtOdJymv-N5mtkKG_1dTNafIHVLSv84B4RU3aFdJvALJzR-pYgy6sr-H02ZqUMNSJ6hU673ZpnLKNJ624lP2hmTzBE3vMGGpXOBMdmgRYMCn33u_RO57k7HbCyn0FSH3dg9XUQ8T8ZpLF2K15MXty--2xSJYNjB4B9A-mqIaPhyqC2qL4zBLsq8zyInlfVnPmBPVCA8bH3MnjtP8sJOJDjHKa4dJrHnBZbA5qz8U0x8AFh4jE8A5MbC7BMNVHLSdKE1ajZRRRcPKKGM06YwQQTMmkbC1yHdO-zRH-O7dji-7LRZipjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست کریستال پالاس برای ترول آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90527" target="_blank">📅 00:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90525">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S40qdFtoyEnRWC24GBdgxJzwpLfvAX0qqMuIDvt1LxElQz0Vt7Rzo0Eoi8jxp7IJc7n5l5i3pgoxVUk1MjGi0Ina0cqkcJybp5zu5jnHXjAg-jC-MvSR4k0mrBv5aGYDFEA4TAoFqV5EpqtDlnEsvFS5iOo64wxnQb42Ju9ZHKyXFHmoFnbacJT6K-q8C7lBxuwEU03CxPR-uAlsDJXLfzSOn9jE2b-ZHMlQfIfLcPBV_z00YmfCMsEf2XxylNBHmZdU8tty8W_iQMZRACSGxCRPtBKLX_2VjGQmASKO5pgodP0N7U_91qksA4Ooi_UrSvukMZLCTk_f88l-oKXMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل آرتتا:
می‌خواهم به پاریس سن ژرمن تبریک بگویم، به ویژه لوئیس انریکه. آنها بهترین تیم جهان هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90525" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90524">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ05L2ChS020nGknMh9_4aZFxXJonXCpMqVN0MEwLn0xUv9KHUhnHe-iF_iW84tC8CkmZT2miva7e3aH9dVKlJpWgkoL17F5c_B5SGMLiWDsgcxMW8BPqkCNXh5eKe_8sZ1CP0FOAJn_ZY6JH6wwVsnmKREIDUnBVsyndJh7j1KVktEu_WOySgnspicot4yu752lu-P56-3mGTRn2-HljIkdrafPWqti8EBsV8yV5fHN3kro0-bwB-k0VrAsBKUZ05-ShlhER1yb2jeK4hoj-sKmqke6ic8j2mK4rYQafcjwzPxJrtxUT0L_iC_iO7SWAoG8FimyDryOjqnTUHMDKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید چلسی بعد از باخت آرسنال : به لندن بیاید و از این جام بازدید کنید
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90524" target="_blank">📅 23:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90518">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ij27sfs690G3sxPK0DYUEdVFarbLW9lreN9a3YEdgq8KfSYuWGUEB-0OxTTI_9GSsvkXbXHOiyi52RteNhgOdSX4PsVRYZ_1-OZaH4fioBrpCBzlBsmM97RSlKhNSgyKaG-KYHs6sQUy6d3wJZ6tJHCwbawffFqYqM-bEyGhgKTm0vNEFKF7XRq3BOKjgJepwBc5uoTJIdBTTjS0VwHvpCXbL91HTBrHZNd-GyRiRZNIBN8n-UDU5Q8TR28RZ67Vx9JzUwvqw9ii1TEkbRMPJfCkqzMa5Pdvo5K1NZEpTihWomRnYZ4etXruP436AlgRI8Fyj2q6Fyz2QSpsOTZ0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ahzDJSDNKgSYulv9PoCjS3gfeiAtzAPuw8iEtp0fcXJjsu22kqmKsGU-k2tqnECsu5lgTzY2Fw6BDSMRQNf7pXjnqJGNpXr8nXEY2NuR9TeLdEJ2CxD8ZX838fxdRCfqb0F6P1WVkE9LwTYvCOjHF_REuHGcdCwBF00AKFlyAk01Sx_cc52OIMVdTaNeoOhMHLvHqsZti3HcHgjKmbHRFJPQ5WDSoiizgGMFL8BJdQQa-6vx466ejmcd35BnMpd8OFywfS4F6hzAC0RjweRkZJ0OEjqbFdrWMDnq8PwNV3JETb177nqftSt73w-TLI0t5KNEaycdPDSPMODSqbSm-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVEvSuLoxNv7xx2Gh3E6yBJhO333N4-IgIoR7rpBag_M9zEh8IULuDeLnB7PSPYiAL0kYrYVpuqwu8o7BC31oG4fYXG0F8PpkGklh6zN821eQcqbyVKd7cOKlEua6oUxYZC6BSevP3NFaKeg1l2aJw9_xYEWMVkT1cK0ujbZWhpkdzRXGcGLNSuhZm2SdGNNxXd6IaTJ2JRuUdOffELlPKDJ_9Fzu215NpblrykcQbwhydveLvS3KMc5QInWJZecP4I6REnV5200pbCfaITUM-SNGfJig5j0BibQON5NTuAljsPMBJ0bJ9g8m1Ef_VOb89pkYg-f5O8uLtBM5BzyQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHhQVqPlDHZioIAVFiO-h4p1jd9qtbM6ep6xu21p9rdl0im1VFqm4pURJ4f3WPc7AKqdJQG4_CsYasRW5bBflyaf-hiuqIsMQDy3DW4Te518ar4hTmeAdDUbk-RnUnFW4QJJG9BCfB-IlykaOnVh874GkOIcjtGH7v7yCAf0YZz0WZFfRL0sLNBpvnOfDreR_N23UJPWVUmb7Dr5gEpoDea9jxzAnq7ypdql4XX-V2sHlMYvtkRwcD8w2ue65Oa1IWIb8vfBvIEDKo7yYnMGRiiaCmFtTiCZEn-LUrUvCL3CwWFB43HezsuJ0dRTg67SQTIMcUv_e1vabrhDGWJF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l788IsWPH-rVc2bAVKxPE-rP5umwJbDJ65fPQnH0UJC6V1cXsT3W87Ul0EgdZ3opLTEuu3ToPPSEmR8N5V6KMxK4xWlvJsvl80IoMxvo6KeMDqk09w8cGJiDgLhLCPjPw0GweKB5Ev3PSBfcTGm6oaCy1g9JqhCOdvXO2l9ZKe9ZcUFyFOenNCkI3HDm9YEf5Um5HVeQAvHRjw89DZ-xw8wLrTSMz9AUGH-opDvboTsLZ9aL-yWhVCynQjg6E2AyGGqVfSfFAYwYwmwe6Wj_Xkn4ti43DbPjZpo6zvzbypOZ5KElCXViDn6BlLXOLpdkDTfYXoCMQpnPrpuRNdn5GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Crv2TpYWlJ8PdRRmFzE3Oi_FZKejFKqMQksmI0plPGULiQb7l4d8GPilmGRJtuoXy3u2tLNAF0kPJLuMKqfBBzbIex9JKhAolgOvu_lvvJCgQRQc7PCeLDUutIQGJCdlk2ZQKcAdKKxmCWYwflEKxsEQHvaqDjrCznK15EYmVXaBxybDmsQjmomGaxNBaHoE50NVZJZ1SOJc3qxjP0Smq5Ipe7u04sKHLKqeTQ1JMO8zza2SgLs9fI8I6eIiEbFqRApkjrU779hCwcGS8faEgWUQOXdU5la0-8ZWx2aFWCO8iHi2Eyb_R8eZRIE0_5kfHybgoiIvsn4SIjNkpsGnRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از جشن قهرمانی پاریسی ها پس از دبل قهرمانی در اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90518" target="_blank">📅 23:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90517">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عجیب ولی باور نکردنی!
امباپه دو سال بعد از ترک پاریس: 0 جام
پاریس بعد از ترک امباپه: ۲ چمپ(بماند باقی جام ها!!)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90517" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90516">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtLnpCmVxVWAIKYvpPTDY4NCed22ZJ_bztvYcsd095N2NW7B4KjfpY_76i2iaJL7xx06TwQYU1ANa-xr7og-Q9EuP_LD2mw8Be-CX1pFSkSJtqqYivjkvggB65oB7zthQYOk2YsjxXarrM4rF5Olncepk9-PoPbijAT31v7sIylZiTpDEZtgKq5xZPkfDgNU4jWKisOfYJrTogbWLSojNvcOQUitmE_Vt7ezRvytrU_g8shVvt5GaVI0p-f_Gm26Y-FHDThwveVTVpGtWif4cTknjhwbPrrUz1ZbLbvFGKcX_CIkT8_7c8p-5BVXoj8MtCbwUep--YOLLF5b_JnnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آلمان
🇩🇪
-
🇫🇮
فنلاند
🏆
رقابت‌های دوستانه بین المللی
🌍
⏰
یکشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه میوا آرنا
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آلمان در
۱۰
دیدار اخیر خود،
هفت
بازی را برده و در
سه
دیدار شکست خورده است.
✅
فنلاند در
۱۰
دیدار اخیر خود،
چهار
برد و
یک
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آلمان
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر فنلاند
۲.۶
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۲.۵
- ضریب :
۱.۳۰
🧠
قبل از ورود، بدترین سناریو را مرور کنید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90516" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90515">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پاریس دومین سی ال متوالی رو کسب کرد و باز آرسنال ناکام در کسب قهرمانی سی ال
🔥
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90515" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90514">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تمامممممممممم</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90514" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90513">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گابریلللل زد بیرونننننن</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90513" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90512">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">زد بیرونننن</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90512" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90511">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اگه آرسنال نزنه تمومه</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90511" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90510">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلگلگل برالدو هم زد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90510" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90509">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلگلگل مارتینلییی</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90509" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90508">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عجیبه صداسیما تاخیری نداره</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90508" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90507">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلگلگلگل حکیمی هم زد</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90507" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90506">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگلگل رایس زددد</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90506" target="_blank">📅 22:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90505">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رایا پنالتی نونو مندز رو گرفتتتت</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90505" target="_blank">📅 22:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90504">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رایا گرفتتتتت</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90504" target="_blank">📅 22:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90503">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ازه زد بیروننننن</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90503" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90502">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دوئه گلگل</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90502" target="_blank">📅 22:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90501">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گیوکرش هم گلش کرد</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90501" target="_blank">📅 22:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90500">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">راموس اولی رو گل کرد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90500" target="_blank">📅 22:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90499">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بازی آرسنال پاریس به ضربات پنالتی رفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90499" target="_blank">📅 22:15 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
