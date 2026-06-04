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
<img src="https://cdn5.telesco.pe/file/Q9ju-4Oqm_lw00WxzMmgyUZk5Jeo7lqM-ZDBghPgnkcQWI0S48yKFphb9NmxOFi88r2_UaEqKM89SrnTAi7_L5ZIqO5WAXulhtSFVz5wbngaf3myJMBLnXeYRQWGDnYk98crWjMW_aCUeUc94BkyQsqfCMZbdsm34RsaKsckLMqk7Dk8VjOWkb0k73uxK-41Z93f9YtyyfKeDvICh7BOJyawxI8GFNyuoJcneqpCK03vtovT6JbQm1GrpYjPARbPskhMv9gu_zRSL0j1Rz_tLR379R6RxKwbmqyK3tjrjr6LHyKCe0a8XriGEIaiL1VMakWOSi4HRvzJiI24b4pd9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 163K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 09:59:18</div>
<hr>

<div class="tg-post" id="msg-90869">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfbdee815.mp4?token=TRIigx2Qh5la3YOj7n9cFit_laMHtENaHtVSvR7uy7vBjme69mMIOmVvzmTJcKOJ5mUStO0JINoqecceimZeJxxXXrwCNjB4wCR_EgjqG-QEjpoBuLloyHjSgpl_Yz_z7zeklO4egOdVTUxshoLH9BoFIQN_vFbWDNBCWOdLpbBkog9uB1nT1AuQHIrj1eL3XNgOr_EBovXZIX_Ex_xfV_LbbOP-TmpucVqo7_PnqTD9-06enuBl1oUttJ58wpz-D8ZjFVDGYyFAwZBBhejYwrdUZ2oOqP0dZmbS4rxuApt8RziNsb-IsIoSUILXInGxI41QZDa-Fhhd5xGs3MzX_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfbdee815.mp4?token=TRIigx2Qh5la3YOj7n9cFit_laMHtENaHtVSvR7uy7vBjme69mMIOmVvzmTJcKOJ5mUStO0JINoqecceimZeJxxXXrwCNjB4wCR_EgjqG-QEjpoBuLloyHjSgpl_Yz_z7zeklO4egOdVTUxshoLH9BoFIQN_vFbWDNBCWOdLpbBkog9uB1nT1AuQHIrj1eL3XNgOr_EBovXZIX_Ex_xfV_LbbOP-TmpucVqo7_PnqTD9-06enuBl1oUttJ58wpz-D8ZjFVDGYyFAwZBBhejYwrdUZ2oOqP0dZmbS4rxuApt8RziNsb-IsIoSUILXInGxI41QZDa-Fhhd5xGs3MzX_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🏆
چالش بلاگر آرژانتینی با موزیک جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/Futball180TV/90869" target="_blank">📅 09:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90868">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇧🇷
مردم ریودوژانیرو این‌شکلی در آستانه جام‌جهانی؛ خداوکیلی خونه‌هارو میبینم حس خفگی میگیرم
🚬
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/Futball180TV/90868" target="_blank">📅 09:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90867">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce3254dd5.mp4?token=CtIdN5WnAbZKJXcgZUz11MzonzELmI2oo-xwOQdhw_mGmVY1obrGPIBxMGdhOTyPAzJwd1b2HGOclrv4K9w-RPIMlxzaExppGYgjvGEBBus4SChv1kZ_sEm9swC3Q2UNdXWCwnVkEXkAecMWr7jh7taoApbHxCLvWU1geWD6hRMOEiHK6Y9OWw81lD8gk0s6HjsdqzkHBwfPplQCcx43yOJf55sieb-GpQ2MYj9q3gvIF1I8SRTLSBeob4LaoaQZA1yVT7UL3XVrU9rfm0XAeR7KO8DV1WcTbef2d4KV0OW6JLlSCA7d7qAgh7DV8IMPgItJXEHX5jpTSGpx_VldXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce3254dd5.mp4?token=CtIdN5WnAbZKJXcgZUz11MzonzELmI2oo-xwOQdhw_mGmVY1obrGPIBxMGdhOTyPAzJwd1b2HGOclrv4K9w-RPIMlxzaExppGYgjvGEBBus4SChv1kZ_sEm9swC3Q2UNdXWCwnVkEXkAecMWr7jh7taoApbHxCLvWU1geWD6hRMOEiHK6Y9OWw81lD8gk0s6HjsdqzkHBwfPplQCcx43yOJf55sieb-GpQ2MYj9q3gvIF1I8SRTLSBeob4LaoaQZA1yVT7UL3XVrU9rfm0XAeR7KO8DV1WcTbef2d4KV0OW6JLlSCA7d7qAgh7DV8IMPgItJXEHX5jpTSGpx_VldXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بلاگر کانادایی تو استادیوم داشت ویدیو می‌گرفت که اینجوری مامور امنیتی کاسه کوزشو شکوند
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/Futball180TV/90867" target="_blank">📅 09:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90866">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/Futball180TV/90866" target="_blank">📅 02:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90865">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcRfkflayUPlncw-Sg9UqSzJmWbklzFsx-V5ie5CtH2v7hqusnwT0Hg91GJwWONTvcroE2trvSQG2g2Uv1lAVoeTkWmBUG3GzYrwApEXpg39ZX9pYNIW7i7GXWsaT9oFtqM9qH3tNn1H7P2EblIwiRmshlCTdUJFZtmj7jKUBytCjsTrQ5KX1_rGWjsHFylSx-ocojkDIU8iDmOXDSmOD-kKu3P-40_x-RtzaDaNfJzEl2Rxl5mUCRMu4slnvivSTCke6bekKHavAqPqA0BQUp2H5ApOIWRK_mwIT4MhnOPY2NJDvQ_mpVyW01G-IOkuj94MXkIcjw3lp_P3uh0Vhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فووووووری
؛ با اعلام رومانو، کوناته با قراردادی چهار ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90865" target="_blank">📅 01:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90864">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90864" target="_blank">📅 00:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90863">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری؛ ریکلمه: ارلینگ هالند با من قرارداد رسمی امضا کرده. اسنادش موجوده و نمیتونه بزنه زیرش. فصل بعدی شماره ۹ رئال‌مادرید در اختیارشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90863" target="_blank">📅 00:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90862">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90862" target="_blank">📅 00:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90861">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtaWKSmS9W6Ocprr4BGujmo887xm5l-7jwLswRpjQ3qBWYYe6a5tWZ_dacb7Z4jutLQAJNhoVFWb-k70Zn31q50cx3BEawjurKb0toJyfa9YgtfXfzMJdwzO-sOwpddALNHcwlTY3gKJel1czm-M0FNnGZ2i375szGwwd-9cT0moI95VeyuT2KDylfgrPxjHlgwo5OYiEy1eCdb5BZ7zUAzRvDMXFMKwoQoP7npkvX59XwPl8pLaa9era_f3tJ926X5eGEvNMqTVEAaDgGoqVFfcSa69Q7eIrkZpLtq_JUa1OzSTirCOV6g8l7jCU_aUrS90tIW2xOtD7R2cfeV3lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قرارداد بزرگ پرز: کوناته.
‼️
قرارداد بزرگ ریکلمه: هالند.
⁉️
با ریکشن بگید شما: پرز
🔥
یا ریکلمه
❤️
؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90861" target="_blank">📅 00:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90860">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZx6RgfW3cYmb_1F7IaJI26hfLxQAWoN8p48LQ6IHqBwvmyytjhZgDlGTJKURem3pEitT-HpxMifJznRrqZbQ_bnRHUULjjIp10ekFpdLCH4jyYGoEtudq6rBTz9oF3X0NaVAAIs1z5TF1AprgaUuB75C6Ke5a9ejFGQqM2GXnsCNQ9RggkstEH-o9Sr97nxIuMGm9WL9wQypt6nRgF76Qx37LuS5j-wcTA6eJ4CFMJwFjXcU9Ql9gz6_fw7SLjxvRZfozkGwQDecUOy3zl1UMpG5OCcHpo3T_eaapYpMcC-EEyU6dAlLIo-4XIubvxs5fsoDB0lZvNAKSGWbvtLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90860" target="_blank">📅 00:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90859">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">😂
خب دیگه کسشرای ریکمله ارزش پوشش دادن نداره. فقط اینکه ۴ روز دیگه انتخابات رئال برگزار میشه و احتمال ۹۹ درصد پرز با اختلاف این کودن رو شکست میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90859" target="_blank">📅 00:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90858">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw9KhKc19WkMrgnfungAjTqG-zWyoftsBmegkYYOYJg3nxG-TXq5tNvAPZi0i8p4pxQ8Tjw1lAZnGZLoxPEK0DH03Zo44AE0-7r2yUcRSMUr2emppmWVADygJhsLGpsRQCpHUDJ288X5Zs78D2ZbmlJhSfeuA91BRQAVKf4TjeXcgdChxBhxlUId0GiYurYfqSAmubHjfGUsRF1_mA9LK8nu5xdryjBDkWd-Mr9KHeF3pok2BYG64nMoP9K6VNY6mmacd3fR1_0qGFUHX4U-9OzSBTajEvu7zfzjkRJePRt0jQtGxMv7Mkmc3Yq5ii4seW6y1Y9_3LVELAFN7q_7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤲
🚨
👤
استوری سردار آزمون برای مورینیو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90858" target="_blank">📅 00:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90857">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">😂
خب دیگه کسشرای ریکمله ارزش پوشش دادن نداره. فقط اینکه ۴ روز دیگه انتخابات رئال برگزار میشه و احتمال ۹۹ درصد پرز با اختلاف این کودن رو شکست میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90857" target="_blank">📅 00:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90856">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8fa88ed9.mp4?token=XCW_feBdFN_XVzLz8yPi9Z-aK5z6ycF0_RGZyUwPwD-T2Hb4ta9ZfZkzRLBpFRQ85bp61H7_yOSqUHK5z96k-HKNYcxF_ynnMKZTMWfdf4ddbLrF0MDay5WcRotqGFQpLwBs6rbqXYMDMOqrL5KrcV4tYelt1VG-CIiOSxw_iuph8oFsd6wFR4j-IlUzz8akdzNOHZK_jPdyyIqpJBylEMGTSjN2YqqWhhyvpSfeD6-Ukuh7m8_4BENcsRFWyYIwRmQeGemw6e0yZGICm-eYsfMM97ZYJgESjzd-jiPbzgZdgiVnldhmq9S2JXbHRYXnb9N2ywtMTKuBVtx2tbQ9Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8fa88ed9.mp4?token=XCW_feBdFN_XVzLz8yPi9Z-aK5z6ycF0_RGZyUwPwD-T2Hb4ta9ZfZkzRLBpFRQ85bp61H7_yOSqUHK5z96k-HKNYcxF_ynnMKZTMWfdf4ddbLrF0MDay5WcRotqGFQpLwBs6rbqXYMDMOqrL5KrcV4tYelt1VG-CIiOSxw_iuph8oFsd6wFR4j-IlUzz8akdzNOHZK_jPdyyIqpJBylEMGTSjN2YqqWhhyvpSfeD6-Ukuh7m8_4BENcsRFWyYIwRmQeGemw6e0yZGICm-eYsfMM97ZYJgESjzd-jiPbzgZdgiVnldhmq9S2JXbHRYXnb9N2ywtMTKuBVtx2tbQ9Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خنده‌های عجیب ریکمله به انتصاب مورینیو به عنوان سرمربی جدید پروژه فلورنتینو پرز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90856" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90855">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام ریکلمه، رودری ستاره سیتی در صورت برتری در انتخابات به رئال می‌پیوندد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90855" target="_blank">📅 00:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90854">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQWiKrwOmqNGMPBm3jIUl6zW1eB5cHHOPbsmwtyGonx2h2_X4GmLdMeJ_AJQCdRToE57xh4W-5Cgy4i06AoQ8ZEu62R5r-8NQiYM9HjO8CguIVqHDw9qwd4y3DM0XwqUlOpOVMwTCxxuhF836gyd-1nt9y1yAU9Xp5F1LdfnjoCIEM8caYfZsoKpiGbU7jUxRax7zlIMM5SzdJ2aNfzkkQ1k5eFVVoM4CiyLMyfsN7UxPJmIwU_atU2Wy2wRkFDnvtkLrUtRY39VUVIlfWJ_4_GP9Li5CJxKW-uMTpg_WsyiRscS5YHzxBH5kChNyEUfjEGv6qtQBCdvCxXqrdlPfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته اجداد ریکلمه رو بگیری به خمینی برمیگرده
😂</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90854" target="_blank">📅 00:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90853">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
انریکه ریکلمه: سرمربی تیم من بزرگترین و بهترین سرمربی فعلی جهانه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90853" target="_blank">📅 00:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90852">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
‼️
تیم رویاهای ریکلمه در یک‌نگاه:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90852" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90851">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZT64mrXgN8ZCs5wChSub4rnazAt0XDEoZNziUtwgP9PUHy3TXkwdplPY8KbfKzy52jbcM52JwsO_0nQhz3PP3NUQU7V-Ymndyk1guyga5WXQIvil0KDSjcMShMucr6ZS1MsXrb0ZToraHJLJatVetIWP-qXkHzpZAuFHQo3g_0KVcO7-rgzszl8-wZurvncVM1gFwh7gnXXmtS1u8QmZQIIiFd4WMym5jiRnW0nDlMhVqQJPph0VoHaEnTdLBMtlWjzhqbINPxNYr9RW6MCtciyye2TohcojquFDyq2WcU5-VhJcP6xXTTfMns9inbEM2ytTELjUzom3VR7jLdJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
تیم رویاهای ریکلمه در یک‌نگاه
:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90851" target="_blank">📅 00:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90850">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
‼️
انریکه ریکلمه کاندید ریاست رئال: در تاريخ ‌فوتبال تیمی به شرارت و کثیفی بارسلونا ندیدم!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90850" target="_blank">📅 00:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90849">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
‼️
‼️
🚨
🇪🇸
🇪🇸
انریکه ریکلمه: بارسا تیمی با ۱۲ بازیکن است. یک یار آنها همیشه داور بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90849" target="_blank">📅 00:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
‼️
‼️
🚨
🇪🇸
🇪🇸
انریکه ریکلمه: بارسا تیمی با ۱۲ بازیکن است. یک یار آنها همیشه داور بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90848" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90847">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ با اعلام ریکلمه، رودری ستاره سیتی در صورت برتری در انتخابات به رئال می‌پیوندد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90847" target="_blank">📅 00:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90846">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووووری؛ انریکه ریکلمه کاندید ریاست رئال: سرمربی پروژه من شخصی بجز مورینیو است. ژوزه برای رئال‌مادرید کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90846" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90845">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ انریکه ریکلمه کاندید ریاست رئال: سرمربی پروژه من شخصی بجز مورینیو است. ژوزه برای رئال‌مادرید کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90845" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90844">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
حمایت مورینیو از پرز در انتخابات رئال‌مادرید با پوشیدن پیراهن کهکشانی‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90844" target="_blank">📅 23:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90843">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUC7qs-lCCuVlGLYrbazdTThzJBvJ4T5-w6NK-SeSo8sxzort-0lPqMlUr-ZfKI3boXRJ-voSdWFRQEs7SWioWdEQfdGEA455abZwI-FA01RU4I-oVTKwdhgwcPERGbS-AmEsC-efBRxcHfpycLIPlysy_GOiudigsvKxoY8cyOIDkBjFgHuHblmYQgTD2B_KVZ56-pN29mp0NQHwcCllOJLtRgpvzpAMQBkyvVS2rjnEWT5XQGXYI-MIpfxU8uqsTVQY27y9mLr-1a2H7LOVvAhLdMjUi0mk_lCgg6fInCcUSUSdul8hW6w6JrFJlfE-w7wfc5rZb2amoPrYOnD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری
؛ پرز فردا از کوناته رونمایی میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90843" target="_blank">📅 23:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90842">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaTNvaaR8Yf06bPBqLaY2UJfCDExvwofb5vXjD3V9pYPlDc7fir-41EXybzjqJ7kF8BtSNgfQxKntZjsNwaGe6tm1rc39jwvlDXR6tByNlK5tUcUzG36nOzVMg2vDcNuUCUFi6lcT63jdFW5Yp14USuzQSWfLOze2ONrs9DPLtLJUXDVNbmj8goAcZfnhb-dvt1NHamoVu_A5CAuz6tFrfNXQtmiDNjcc4P-IY9PfpPjyB99BrUr6ZSeVQzw0PVgiYfi_xNZ-biAt7ZtyAU7VAsSoda9_QtYPh5DdhiUjPoJkUVJzQCuRLiAWeHmOSyeGAqm85nWIlT5KN_HP7qeOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمایت مورینیو از پرز در انتخابات رئال‌مادرید با پوشیدن پیراهن کهکشانی‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90842" target="_blank">📅 23:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90841">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihfCaQDJkhHgHyvparS-NIjWHzYB5Hi4x7bKNp5ytOjZdD6OuJ-Ll9NyH6AzlCTxOL4gk83Mf_QFkPgvRveUeLyyrEztW7ZVdz7fkkhLygkDRpKlBa_3YpMcI7MO57HcIgLXIQkEH_3WKrBxlaRjwHN3Gd7xiAgfwjuEBOq6t2x6JWRphTWMd-6ESfTiHO6aLuPkiwIDrKBr_TiHd3JNK4Lr1mSrHoKlDtjKswADrZI1IiH2D7qyVkuep7_UPJ1djFIrKKN9mz4YTGOKV8KRKJzk43tZFJCHExjlxMG_326xch7bniCsLsyJtEjDLzy9TUIGoFkVF9jQlzM4WfWHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
14 خیابان در پاریس به افتخار بازیکنان پاریسن ژرمن تغییر نام داده شد
عثمان دمبله تبدیل به بلوار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90841" target="_blank">📅 23:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90834">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZsglWCm0RGz2-B0EpsrXeaq8Sua5W0QN81nGC5yHEprgnjAygURT8mYfsIooknTA0t6JbzCdfacvZuGhRcyZoR01FshJcaKaA1n4ECboxH_99MzXk3Lc7k6nado0yOAJ2Mh9eQabLez0nxRHMo3bProkF2oRf8k9eMlNviWli4mj95PR1tmhLb_nFM1SgWcgZ1TFa84Uqi9tHPnm_TYaafwdUI8P_CM_Oy0NdY6kh-XWDtWl8t7xNcZHHr1Wk6eoWy_05BcJ4EUsJtrFsZA0UZ84caPVAucpOH4T0VgA7M7e8GZXmhqAJW7GFcYjekHcTzgjo1p3mSCffXveCL8dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kaXovYSl6cNGiLvJNAxVaEI7D53lOU78fi0b5-7JQuFaaLy7YbLMHboJP-qIwz3fvOI1fNnUQnzOtb64qEcjFWHWSM64fT2QF7oG3pMoKx7VufcxqeJk0es-Nc2EOeLlJ91W_TqxD-EziPDJuX3HYcDy3kwEbVVEzXg24qNzHv4Xk0Yr_jE4w8DM9g8W2PQPTOe9skYR7do5Egn95xkT-1WZ3rAUTmtnUMmYMEuAtRLVF8qBElh8eko1KR_cGjGoigbl2E07UND1ZDcDz-rTLww_iN3OMBTBd4zrv_Edmw_zemgf0kI-GkN3fS29dipb_g2WFxL-U2-E83lrRXiFxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dAvfvtc2nIe___VywZg5wkQp6ZHfoSK5eGWLyS4gnHrGnn91VilTug6n1EwOOxB8KVlSg3_a2rpWITrAo9ljpBMkxLhJPjTF1CCIe09miyvx7iMhMONdPOz2GRPdrBcEPplUi8wO6TRhHIe-d0SMVrl2NhsxtWzgNNyBR8Vc4AFigNhiD8Uun5RG9jJFYDtPF4WlcFTOQV68AeAXNQrzwl4L8IDNry40qcVl9kgXgtb5eKZtDFyXecFLf1vyOd6mOsIpAnGrt2FVso4ipFCA3fR-VaLDU0tg9V9sW7gH-A4neLtn-yXAVzjlE7E9heMNEBP4DoRLLn5pXGm65G68vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtfsmFrQ-UGiklB7ikfZDwWZqb3iidm5ZA8_v6qewcS-rgE3QgWBwxDO9Kfb51dKi0IgQlcd16ePxx-YjtaTgDg2Rj6LHlrFZ53kjSKVpafnVehk2zqAD3R-miGrRLUGkAS37MUHjb-z-psEdO78R1fzaqaa1ImBGQ54xOPXi6J63jzI5S8Tcl_7YTrqla5T_RPTrm4AkAnP3lbfTruQStN1-KCGhjpElk6RGlMiu6KdIMh7Sr_nmuENmIjuNNvZWeTk_Iqo3YwM0wH1sKoWi2gwuXxEk8mV7PofDBj0jLAYFsLZ5LV_XBm_rjU9z8F5JbeC9TUlgcBxVrR8gNow8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oesGE-aNYOantEkxX-QhyF8151l96hoOjdI1RPzHJOv6L02nHuTokOINJHHxPhSo8onxY_nCYneVWujnZZYDXfhXXoSR8F1nOJ1Sd7P0HN-hD2rt0BdBgjRKQnYtRSbYuEULli0VYMUaPBgRJICpbfZwCBqWQWqaQUUxJk2l6rmrAGiATvkFgC2GhwLz5vnyEcjdjb07vD7PTpRQkZVjgn9bvfVPMzyCrbq1u_5fxu16ayWLbs_3sxuUYQnQsOJr93VruUPnvb97ID0wflCTLFXz1EQCGQm2Pgmjw2KDMP8TxZgkHjbJ27SoQq6L6prdvsC9UcU5nm6eld0ZZS--hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">8 روز مونده به شروع جام جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90834" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90833">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVZ9pCTdJ-ShqhZkFrmZzxy5MIYPekYDqC2SLS19rh8DgVGslOjSOyWlA_YVKTMz_VWiUMDjesagfp80Jc-1BmwZRnOzFR79xaDEk4HO1Hi7EvcDT47nQB6fIwL-zuRK22rNQxReGlAmjJateH4I9zLa2HHEaHGlcA9C3toVsNvPnq4tTuWzRnjtXH0T1D02GXQlAbt859SbXMrKxA6Xy4i0dgyzHEKA9gvubrMVuz17jrTDQQ2L2qsz7VAjxdBu6RgApcWiBKrBzWS2sDQuh8yAPnuUBxrl-wgp7oCclgYH7iM5Gp1hKspIt2axCRQQFvxCjcltmwhPiRPM3yfB3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
شجاع خلیل‌زاده با ارزش‌ ۱۰۰ هزار دلاری، جز کم‌ارزش‌ترین بازیکنان جام جهانی لقب گرفت.
🔥
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90833" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90832">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIOLbYYsk0pRltWeGBBc-1DuPCuapR9ID_7LKoLD40LBee-XwNRzIMnFGRiq21gRqftw-uesbErPhQP8YatG8PVSTr6oF1aDsgYTwVSrjLpYe3Lfx7cuBHlQY-Sp0FHVfaJ1HTd_HWYSmfuBU3Q3tpFxqmaaH3xlKDdYV7X0oVuv6PBrwN0I2qUvHthz5Kj7j9IOL50sq9HsdlROS_Ac28dGRLyATV7duMQd4il-nirNtV1jmODU3l6EKWmVIoTCn6KGOmslJM9wMS5278296Io-QNXvvZXXpZ6eghVR9kcu_nXRMqmzLe1lxIJxSwDG6D4kt8vqNEfSMzkvEjjr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری باشگاه استقلال برای تبریک تولد فرهاد مجیدی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90832" target="_blank">📅 22:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90831">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGub1Zpv_rzO9Pt8piEor8sazV2dqksC5LoUt4qDgVZ6oP-HbBQEN9AocnRD8Vro0E-prPsXMDwKiHsGSGPXiwKVVgIa9r4VJ2GgVAVvPXe21VnWzvI4vjfirCXa2336xjD6K_zo0fzE00XPX43KC0RvlpqRvSPSsTINxhoO1DqcZmJQlisexXv-9MHCOoKvW922QgqfNkOsi-v1rdLuMLPk2YzaAzrYODuuK4m8hwTAwCgLKl3KAkrPlsR50JBfV-hBgHI0FMJwYzd3Jpvg8zcYR2vgtfYtYqD_hypsH6bZM3xQNZ2bqLKnm7zxnUezRhJvskiFTreWQIBJ5pxRPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇮🇶
عراق
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ریازور
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپانیا در
۲۸
بازی اخیر خود در لیگ شکست نخورده است.
✅
عراق در
۷
بازی اخیر خود در لیگ مساوی نکرده است.
📈
میانگین گل در
۱۰
دیدار اخیر اسپانیا
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر عراق
۱.۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۲.۵
- ضریب :
۱.۲۹
🧠
پس از باخت، به خودتان زمان بدهید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90831" target="_blank">📅 22:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90830">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWIKzLlmHmL57PixNWDKfULklqpDNLG-M1Eorla9Tq6blYhEDoUF0C8rywUWgsvBlhrzltZQW-tBiWdB9IVppNXldlcr9H4z_Mgidg2zg6TusOwNcuIW4cdi97MOFGy_dZBk61d9JdYgv-23mD9NrR_urRcq93fqZ0XoGJqShrybT-Bkd79xdkuekcL-ckLhFZbt6xALcyutOIMfdnRqJeoBJvSM0WK3nPx-gEU5vo5o2Gh6-in0jX5eW5Km7KaQJB2_vArYMQmbPcmN5bK22Bl3sH27cl9x-ZpPmFYyM3Knaf9uD_GPQMKEPHMVu8QqZflOwcIuzophNPPdqxBmwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">TOO FUN🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/Futball180TV/90830" target="_blank">📅 21:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90829">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRFqaEvvFCEjCdy7m4PJyP1XcTd1HTYyEsFcitkao18AXYF75EbSYTCzEAwf2v0tpfkY6COoCgIzIMa7Zm5AvN7uoyhk_WryYuC38p0r1BgHMt_F7FKPN_wBT9njm45S0gCJQ9fCZQMKltxEwU03oLX0uKwZgnd6Ok_ZUKyS9FytczIqPRJgaWWV4xALV_OcZksu2hKITHzbRdgT7TJlI_Q5TT0XjXqX86-ytydeoUNflDo9QdbUZIPpWGjzKqN-wqVWjCdSet0y7zeifdwMI0UvtpznNu6g06_xajUsKws8-VI_fOILtk6VHZD-TeEIacREXzvAgTokLFPOdBkLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو: برناردو سیلوا تصمیم‌گیری درباره آینده‌اش را به بعد از جام جهانی موکول کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90829" target="_blank">📅 21:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90826">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUGjmjy6tRz6pQdTcwrekSJCDlr0vcdazPhJqroaqTHVDeAn6gsMcB4udu5A-pgUuWxvGGdkbWsEeVDIpMDBihRUwp66dKEIQe2ot7sQmO725L_SyKq23-mysh4sArc1NDa3CRFUM5Lhx3c2KFjWYGTy49AV7aDMfHwmojCXJpzAI49gnEoWqAELtTKhRmfJLEFUTjw5v-YKnWXBBt6D9Oez8lHUavRJ_aAJPCG-raADR0IXhjYfPUNaqKQ3WFhhz7Uzks5HL5KCL8AYFQwx6_ftUTe63Sge_9kth9pyP-KJ8xIvv3Nq3AKgr6b9f8RVXUUjx1yghpxLg51hURH6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSThKHQiyI0dUv8tuXqfX6IVSujRowg8nmQvVwpui1EFasbWIX5qVK1g-OHZ4tFZq7kFAqbmWF6onEPASH2WFeohsTBvS-kxaTIElrcV1YdDDf6t2aM_CAN9cyuLOSVC2UFOrENXlLZ6h4CHY1JBe3oF9dsc2M53KscU_SBiSfWTCRK9_SpwwfGimiF1Ol2T4yR28uh4Yj8wGCx1mhsHyVaVRylinhh6mhD4byKbCQ2rNpAi64nHpgdfNA1sJ8qfoqfT3zIjyZpQj9OdCo0fYvTWQ6udlpgsPYgl74onb_gNU1F6V9RRhNqRl-ViTN-9mFd7I-pKYW1DtB_6DZphmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HrHhzmt75_xAckRbMbJJab1tCRzFp9gGr487orzCjUfbVN15bu6--yXaf__-sjtEaFax3gLLwiKFWG9dP8X7kM2w8g-W4GCH1bONmaKr02i9YMWtj4BpcC6s_Ux4mplZtod39NyT6e7YHHKl-YT3VpfdW0yqoDOzM3odWylzJeSLk5V1wkYLruqbQulqbaUNF8md6m7M1EF5A-VLGIxBAto6pv6vvpGPJZFVc2xRSrEO0it4-8l-xTul1-3zKpU8HqRpZzvY2Q7AJVCBAGr2JuG3lL3tvwuQBsQcvPnOITqQhNRLlaDZDrA-gGDpWoW2UxM_333w4WZwmWRDbZ8t-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و حال امباپه و بانو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90826" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90825">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
موناکو در آستانه خرید کاسادو از بارسلونا است، به محض قطعی شدن برناردو سیلوا هم به بارسلونا میپیونده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90825" target="_blank">📅 20:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90824">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKTrDeTWnLXq_WVylAs3YrhxgVlpkr1Dh9akhjg83543HFmjewkb_0C8EF8o41T4IQWJxsLSkKwEQRW0sn8Pfc4XdOpjy1WjSsObXgvIjIzRIzz_xkGYMtjSDW2BnA_npx7AorqhWhdHFFaUbp-uYY_kXJw4nHaSZClYhrop7-MLMQQovoB0ozY7rVnw54S6XitZmMa22ltpBv1gTicyzblQ5VdDWFsQRXE6a3DMZ8liWMWfzMl-N-Y4F52ultRdQjeTyLJxk3Vx76gpgfIKviXBIjiZkGB8q8aLMtbF8QXHhJK97bkN-t0Iy4OdFxkqxnFIfLYN4ssIJu2bkernGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛ در صورت منتفی شدن جذب گواردیول، رئال‌مادرید با درخواست مورینیو بدنبال جذب کالافیوری ستاره آرسنال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90824" target="_blank">📅 20:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90823">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=MRjUhCSvwXVnqB5KE6y6AcTr8liY8o354XlsTqhWDAOGTATfhHRJUEHeeDiFAFTiu5EFakPcp2SGBgsGKZM25AT0VJmGN43uqZx5jTYz1VlhfA_S1T7VTym2HPGvB7DMeYB8gui_DEGPMDcrInTbPolDrRAfTGSQWimgxqPqZHSr_x1X4uhdKWnzno4hcNh3TCKdWFNv4_PPnz5GOM1k00wWNNsbp2cUF-MhS4Gy5FH_jDEt2nBkcz8W01TYYVs2uGp6UvNTrhl29GLUci_O2ICXIim_Fd9jgBm48WX8yCrVcRN0sZYy8m4xZPcmE4GmeBI-DpmPqX89zigHZIvmE3AffcZXmzWCJhiLApnIolz1WMJxR5ByLX1v9K3v9BDm9TLVSujT2tUKm2fAOWsfiQnsQDyPHc4yIv-N1txs_q4O8cygP8yPHEAEVnTD-Enb6YL7US6CEuC4jkgRBh-HLDyZAhE2yW4LkBRqNJCK87DeZRr89XAMu4iBfmcdH8yXxvkMcAt5Sp8ro_sUVLc6a19Kx1q1x58zd5VZSNN2jRZumPmX6OZUORsi8ARO8HyYCeAeeOY-KKatIvU8OSN4LTwZvjj5lrHbJ5P8MqBWxCysAMhVxrwE39zki2BjRv84J87d0DWrHr3sN5YXRtglOICvJGTqCEEOqQr7tfz41UE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=MRjUhCSvwXVnqB5KE6y6AcTr8liY8o354XlsTqhWDAOGTATfhHRJUEHeeDiFAFTiu5EFakPcp2SGBgsGKZM25AT0VJmGN43uqZx5jTYz1VlhfA_S1T7VTym2HPGvB7DMeYB8gui_DEGPMDcrInTbPolDrRAfTGSQWimgxqPqZHSr_x1X4uhdKWnzno4hcNh3TCKdWFNv4_PPnz5GOM1k00wWNNsbp2cUF-MhS4Gy5FH_jDEt2nBkcz8W01TYYVs2uGp6UvNTrhl29GLUci_O2ICXIim_Fd9jgBm48WX8yCrVcRN0sZYy8m4xZPcmE4GmeBI-DpmPqX89zigHZIvmE3AffcZXmzWCJhiLApnIolz1WMJxR5ByLX1v9K3v9BDm9TLVSujT2tUKm2fAOWsfiQnsQDyPHc4yIv-N1txs_q4O8cygP8yPHEAEVnTD-Enb6YL7US6CEuC4jkgRBh-HLDyZAhE2yW4LkBRqNJCK87DeZRr89XAMu4iBfmcdH8yXxvkMcAt5Sp8ro_sUVLc6a19Kx1q1x58zd5VZSNN2jRZumPmX6OZUORsi8ARO8HyYCeAeeOY-KKatIvU8OSN4LTwZvjj5lrHbJ5P8MqBWxCysAMhVxrwE39zki2BjRv84J87d0DWrHr3sN5YXRtglOICvJGTqCEEOqQr7tfz41UE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدمممم ینی؛
مصاحبه شاهکار این مرد وایرال شده؛ نزدیک خونش رو زدن و اومدن باهاش مصاحبه کنن
😂
😂
😂
+ خبرنگار: شما که خونه نبودین.
_ نه ولی کیرم دهن اسرائیل.
+ خبرنگار عع این حرفا چیه آقا
_ خب الان چی بگم؟ بگم ببخشین آقای نیتینیاهو کصکش؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90823" target="_blank">📅 20:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90822">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=clORdQEpa0vE2F01JEUc9W0M-9aYpgPU4jNPNqMQ95sVM0YDXdtp6RoIyqiY6nNAEDr5vF8c-0upGLgGOT9_oyQEBIosQgxoUwlOpp4c1eaR9JMG5_wRs4YoxeXVOpkz6KP1ZEGzMR80y7LlgWCq8HGJOf_Cg9gsC48hPEz3cUKwnVyWJMrjU9tbQib3LHXMbZ7mG2hQgR8TErCOkOzPNoFsVOKkS3u2Q4ctHAAWS5vSJ7tHg_TFQ4FDbqmKLTQntpW-DV1y7M53nvHTU2nAuJtqw_4aU43R5soPMRHHKgxrFDJaad3haKeaBvlBz4C-rOr2Bu6x_kPFtjdG_r7Hdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=clORdQEpa0vE2F01JEUc9W0M-9aYpgPU4jNPNqMQ95sVM0YDXdtp6RoIyqiY6nNAEDr5vF8c-0upGLgGOT9_oyQEBIosQgxoUwlOpp4c1eaR9JMG5_wRs4YoxeXVOpkz6KP1ZEGzMR80y7LlgWCq8HGJOf_Cg9gsC48hPEz3cUKwnVyWJMrjU9tbQib3LHXMbZ7mG2hQgR8TErCOkOzPNoFsVOKkS3u2Q4ctHAAWS5vSJ7tHg_TFQ4FDbqmKLTQntpW-DV1y7M53nvHTU2nAuJtqw_4aU43R5soPMRHHKgxrFDJaad3haKeaBvlBz4C-rOr2Bu6x_kPFtjdG_r7Hdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبلیغ گواردیولا برای پپسی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90822" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90821">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03866b7fc4.mp4?token=Q5j3UW0xyxEk8PGwF2Y_2jCdLZ-AbXu8rpr9BatkTXtXymSD8F5qu3AE9hVNm6XBh01rc6Kac8_dne_NGAUFaNpFkpnF4LaPXsRUzz1RNlrMpZWeZqpdU9duS5fVQZkVH3mwjkTeGcNiT7JJ8gKA5jefQHFEfp_It14c18EnLcZT9XFh0nQA5LJMjvDIoIozlrQox1kKhGaAu0DqD5gtSW4612zET1OPJVK0PcHRAFO68xUN6g0TmskiGquJuQKeKk5OCOpKONvuAdkkd5LQn3pTK83V4T6kMX1RJ0b6EVG82ORXGEa-6RBcVcWHck29yCFtv1S3eqqSXiri2L4bhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03866b7fc4.mp4?token=Q5j3UW0xyxEk8PGwF2Y_2jCdLZ-AbXu8rpr9BatkTXtXymSD8F5qu3AE9hVNm6XBh01rc6Kac8_dne_NGAUFaNpFkpnF4LaPXsRUzz1RNlrMpZWeZqpdU9duS5fVQZkVH3mwjkTeGcNiT7JJ8gKA5jefQHFEfp_It14c18EnLcZT9XFh0nQA5LJMjvDIoIozlrQox1kKhGaAu0DqD5gtSW4612zET1OPJVK0PcHRAFO68xUN6g0TmskiGquJuQKeKk5OCOpKONvuAdkkd5LQn3pTK83V4T6kMX1RJ0b6EVG82ORXGEa-6RBcVcWHck29yCFtv1S3eqqSXiri2L4bhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف عکاسی با رونالدو توسط بازیکنان زنان پرتغال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90821" target="_blank">📅 20:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90820">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ea114a31.mp4?token=HMarxRj8nVCBb9VuvR3ovUvoiPaTPyUqDW2V8SJUv-hOhh-E-xD-mLbNqCy4plcUWGcqOcMofgJJoy4PIqPjxoDm_8kQ0knFVsSV8G1dhApDCUxfhJlh42a_D_Mn2YdLqklDjgQoEl90Q-bhCxxtLZklEEJm1v1THbipXmhOQ7AEETJDcxivi19fNWDAcSuQWU7QUtdEIoyIQ5G7ZZowCjvORzjlQFPBzbo8QDeDNY4xELVYvmQ05PsiE-63_-RaUeefuCdr5x0Qje2-9iuvmZH3Qp-hiJvm3hm6R2Zdg-2gcDLuq9vmYUIa34tsQx6xDD1GJBDnUUmBAUuw1C3MeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ea114a31.mp4?token=HMarxRj8nVCBb9VuvR3ovUvoiPaTPyUqDW2V8SJUv-hOhh-E-xD-mLbNqCy4plcUWGcqOcMofgJJoy4PIqPjxoDm_8kQ0knFVsSV8G1dhApDCUxfhJlh42a_D_Mn2YdLqklDjgQoEl90Q-bhCxxtLZklEEJm1v1THbipXmhOQ7AEETJDcxivi19fNWDAcSuQWU7QUtdEIoyIQ5G7ZZowCjvORzjlQFPBzbo8QDeDNY4xELVYvmQ05PsiE-63_-RaUeefuCdr5x0Qje2-9iuvmZH3Qp-hiJvm3hm6R2Zdg-2gcDLuq9vmYUIa34tsQx6xDD1GJBDnUUmBAUuw1C3MeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
ویدیو منتشر شده عجیب از دولا پهنا شدن بازیکنای تیم قهرمان کره‌شمالی با حضور رهبر این کشور
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90820" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90819">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNEX VPN</strong></div>
<div class="tg-text">⭕
محدودیتی که لازم بود برداشته بشه برای پایین اومدن قیمت کانفیگ برداشته شد
❗️
گرون نخرید
⭕
طی ساعات آینده قیمت هامون به قیمت های قبل از جنگ برمیگرده
😇
منتظر باشید …
آیدی کانال :
@nexphonevpn
آیدی ربات :
@nexvpnshop_bot</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/90819" target="_blank">📅 19:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90818">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
#فوووووری
؛ باشگاه موناکو فرانسه بدنبال جذب مارک کاسادو هافبک  بارسا؛ احتمالا بارسلونا از فروش این بازیکن رقمی بیش از ۲۰ میلیون یورو درخواست کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90818" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90817">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🇪🇸
هانسی‌فلیک سرمربی فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90817" target="_blank">📅 19:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90816">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVCuhY9O6fkLMfaDwo_WI6jSFwjv2OO8KSAFFOyNl5MoPi_0NmF5vYyIGyN08YGXy5RJ9kUnJMKfSJPiOZeWM3bY5tnbxHAW2jv1KY1tySipFQunOC8Bs_xAqjkyLB2o7si_9fdKvOEv4mJEuQmSX_yLe-3C9-2tetyhewR7-syu-fHqM-1opAoga_hYx8CG3Z2pJHC5pt3xucl2RvMyEEZv4Vox5_uG_mqaAfCCNYJ94lOz0hKT_vbDRUoH3evGJR2aYo_sVqBtaF3OiAeiB4kUWVqEZdv8HL78xZASwiUBqO7kNfExSqvga0-L2iUEQRnk6Il-EHlJilVFcbYkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کونده :
«تا سال ۲۰۳۰ قرارداد دارم. در ذهن من ، موضوع تا حد زیادی روشن است. وقتی در اردوی تیم ملی فرانسه هستم ، این مسائل در حاشیه قرار می‌گیرند. فعلاً تمام تمرکزم روی مسابقات است. من در بارسلونا هستم و امیدوارم به حضورم در آنجا ادامه دهم.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/90816" target="_blank">📅 19:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90815">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تهیه کننده برنامه پاورقی: خبر تجاوز به محمدرضا شهبازی، مجری انقلابی برنامه پاورقی دروغ است و ایشان سالم است و مورد تجاوز قرار نگرفته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/90815" target="_blank">📅 19:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90814">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8B7lb9jq2MMiaePoXTz8M3JXkb3J8IdZPsYnuREdof2w8f4UWPqgLXYkIJUS1FE77X2qlgZZBVVDUiGJWVZ0NTbJ49aW7vDwP1rTt0i4up8s-R3wSeIpSunJW0MMhQL8tVCje1YlfwGcNir2sBtJgGSSRP_QkVuKRyHecD8t5Mfo_JWZlaJEZ5juM6hyVMPROTyjUDmuoNvtL2ccwg1Dc3JD2eBNOcyMIjvRV8OTHdB9h-LDyu7hIZu_Qi0YiX6jeUyvBGj1KjGOVKJRM6MBwO8Zx6Szrgdj_mvFFYQ_j_eCAqOhSzorJf1Fhd_3UJ9vB5Sn-jkxgDGkO1dhKimPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز هیچکس نفهمیده چرا زبون ویتینیا آبیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90814" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90813">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تهیه کننده برنامه پاورقی:
خبر تجاوز به محمدرضا شهبازی، مجری انقلابی برنامه پاورقی دروغ است و ایشان سالم است و مورد تجاوز قرار نگرفته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90813" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90810">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH7vz_TPnPhWkq3GJXcIc8boXkGekdDgNcZ_pO_fr_-xsTnLrKQUHkxOoUKN3N0UyzG_WNOo_HxF31bPi2k6avRNRuv79ZsGxugZK8wOA8yzo6Yfcl2uiM_-88eZB3aqCjYdE_O9ug_e5uHyfy5AFUdYxMUQJEgRVnG9TP37ZuZe_ytzB33XhP8pVMGDKHPKSJZoWQVtdRpN_8kveEu8yEqG9mtI28qduvIYKqbkJ3IhtB3ALfh0kTrv1HKfG-ceM4B4mT5HIGGPRtI0LPDVDBMmvC7S0GcG20O4nU4wl1q380A6UrO7BAr-9IAoDVkIL6TpSb8YZ_h_3N02B9VvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
هانسی‌فلیک سرمربی فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90810" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90809">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgUONS7IMXMtHJSuVERvqj1nd4pbFbiULXCwFiZBw2jv_6xkbDi5UommZ4VLG5l5JXNU4-MmztT9DysFn7DmQy9aZRR8YZs5tLQS3QDKWybhFZx_x24kYEzjw68AMSAMYQrYh_jzGbVnt_OK_t10ThUKutrNAgDVvS5j4KJD4UEj2wTCoWicv3PzZ90oWMlWxnXFcIzwRwl8NoLUETdlVx2aXOHq_iVweALYSs0j4VOyJRS_EATzW4mJnicwLrAWYYtCrRo9vbpUGwNiSArZ1gSWizehsf24g6jEzSafniw2bYoPEFfrK8WrRmmiuRnZ8L8ebWu7CI5dRbaoRmOC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محل کمپ ۴۸ تیم حاضر در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90809" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90808">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8q3av08lAIflX-OtTW3NjzOC0E6ywN7sb6gw1s08sa-vCusHzmsnJYFzmZHQvqAM5r3tL1H7NaI3s9xS-A06aa8ATTiVEjH2ERux2P_UQ8yMry3HwhyQxCjfABD7Mo-DZrSXI6rUtd6eFLxAAKp9KeDiwf4iS7OlOacP6-yJRH3sRXbuIFGts2bnSdxHAwPS93sB1JG5-glkd9HZ3fAmiF8fGTmumQKqjSYvVRTyf_72akJiCMxilpT6pUwqWVTMTY2ud85NCzhltgv2ABeVzL-bB-W9xzMv2290PDvJv5D3oyoqojBtWtR15oDF4Hx3HpbBbtG8UmSYKiE04cWMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب احتمالی و ثابت تیم اردشیر تو جام جهانی طبق گفته رسانه ها:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90808" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90807">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhjByIHmwxOBnpwB7oqF4LGcdrnuW-sHWLYogvnmsV7SIMKU7CkNtmZN8LIoJX-qfsmWpm0ycCkJa3AXlb-xZcGnqtYv37n9QapiLZ9XPl6NZ1ZXd7vtlAYGAgMGoIAqt_w3ehdWgLzAcBVpxmPQA16twLJMfZrAQkvjEuW-6jLHoUtZ6pXZGikUC14mb7bx2ML13eX5XTsYDYZRUwwm6Z8Goq0sPisya7YCEWLvE8BYPfi81RiOJaMAAsoU0mPylc12xRTuKuS8HbZ3yAmVb12k2ryztdggIKlyr04RXNcCvGsk6Wwp-r8sTUvKusQquDRMPOQoLAFsplh_aKkZTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یحیی گل‌محمدی در آستانه سرمربیگری تیم دهوک عراق قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90807" target="_blank">📅 17:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90806">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqVsd_37xQm_cJwMumhhM-Sa5FRhawvyEJWRZuHRKOYV7aWiHx16fyi2KkxnFP5ib2IfNAfDkTwTw32T5EAyISmbFRMR-QUCDDxw3xvprwepBbtDfMHcA-UrQPv8SZEgyFfZmir1n4tkWVA1TiXwQ1RL6bbgwqSEQL6WiWHbxrz3q9cHryz6l3aUfVhbjCM6Du2JMSU_R_MyhP57-BEgKWMETX6Hx-MFsYA38BQYI-9TLXsvj0zn_AWGFcFSSOe0rbunK-FOuCB_D1hoU7np4Ccx3evcnn52AcvFpLem0yPgB0CtV_bKAlhvNbjeG4Repu57Z78ASQFDeu4T1X0cFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 مربی سابق چلسی که تو این جام جهانی هدایت تیمای مختلف رو به عهده دارن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90806" target="_blank">📅 17:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90805">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
یحیی گل‌محمدی در آستانه سرمربیگری تیم دهوک عراق قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90805" target="_blank">📅 17:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90804">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-Nc3dFuOba024LTubrf7fLl9rchKpAqUH_Dwneh54iz00qB43DNGzIjyKQFi1U3gOqRQc64IbrvHujTZC86o4VVudQoGh4n4kALrVOKMFIBZPYMmhAOPo27cIpIRB0qxPnGbMuftOEkdIw2rFzbEAVZ31hWbNYXp1sM4qkpbjp4KnRAsAS5TkaA4lilitJhxFSOUZ6IqS7asEgpqMOLfjaCQDPDY3qCX0erOu9Wpjk7OW9bKcGOBJYCF6QS_xUvTN-ylh-x2IqrMIuCRZGpvaUx11IUIfwqFKOONWBAIlG1N673_cr1doWuai2PreCIgTq40gN0LuPJ0vTlMnPrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدربزرگ هالند مثل سیبیه که از وسط نصفش کردن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90804" target="_blank">📅 17:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90803">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167838926a.mp4?token=qBJBAlVjDG-US69Fm4338JhENs0n-t_JCVpvhUxcStxf4Pe9LiX7VizEnC8fsOep5uCbb1bkbKkP7tUSKoytFt1JQVQ7Qy2mTheZTrkYH-Q6RYwJQfLu5cpBPz5XdXoCtmoar5B4luBPf3TAyXICBnXHhONbcLlZqMIVUZawJ4vvRZ3gdvl_Rz11UmWCfgIcETX8mOFZHFvHQyY8JoE1NlQPC9zhVrfbwzMVrgEBiMANBXBWGe-5tzNR9aUM7mIUhppeSVVdwPNEGJx4n0ebHDQdCcJGMEbsKRhv_SY82FRYccZQ9Wx4w4SEv4QL-MGKnRVXBpYkP8mnI2aLKoA3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167838926a.mp4?token=qBJBAlVjDG-US69Fm4338JhENs0n-t_JCVpvhUxcStxf4Pe9LiX7VizEnC8fsOep5uCbb1bkbKkP7tUSKoytFt1JQVQ7Qy2mTheZTrkYH-Q6RYwJQfLu5cpBPz5XdXoCtmoar5B4luBPf3TAyXICBnXHhONbcLlZqMIVUZawJ4vvRZ3gdvl_Rz11UmWCfgIcETX8mOFZHFvHQyY8JoE1NlQPC9zhVrfbwzMVrgEBiMANBXBWGe-5tzNR9aUM7mIUhppeSVVdwPNEGJx4n0ebHDQdCcJGMEbsKRhv_SY82FRYccZQ9Wx4w4SEv4QL-MGKnRVXBpYkP8mnI2aLKoA3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش پسر مارسلو با رفقاش به یاد پدر
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90803" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90802">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e389c70190.mp4?token=SGtBRpZ2SpQ-xgRRun8elSk1V5_cnIaU3HcR-l5DMO7BFaEd3c-juuMjMrd-kjFI7G92hgabLxay4Ceu5EzxSEwjjf_r-9Ehe-JHqrvUuMeHPcGUWIufT-qFLUwAF2pKwIGOZN6BAzZYtrsxecj_bxo-7hNfd1EttcKq_Kj4BHTpSCzmqlSxST_nV37Hm0YM9hOQWty5GD_ustMGcekqASgkPRcnCzbzsBwHhdlm5LBZwS92bU4H_3KTQxZX3CyaEye_IYJuMFd-4eUsX2i14_itu1r05cWfgxwqnGT_QXSH1lZv3XyIHOfKbcFSN_wpTytcDGu0yQNznT1MYbrflA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e389c70190.mp4?token=SGtBRpZ2SpQ-xgRRun8elSk1V5_cnIaU3HcR-l5DMO7BFaEd3c-juuMjMrd-kjFI7G92hgabLxay4Ceu5EzxSEwjjf_r-9Ehe-JHqrvUuMeHPcGUWIufT-qFLUwAF2pKwIGOZN6BAzZYtrsxecj_bxo-7hNfd1EttcKq_Kj4BHTpSCzmqlSxST_nV37Hm0YM9hOQWty5GD_ustMGcekqASgkPRcnCzbzsBwHhdlm5LBZwS92bU4H_3KTQxZX3CyaEye_IYJuMFd-4eUsX2i14_itu1r05cWfgxwqnGT_QXSH1lZv3XyIHOfKbcFSN_wpTytcDGu0yQNznT1MYbrflA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
کاش برمیگشتیم به این دوران و این بازی و کلی هیجان و خیال آسوده فوتبال دیدن...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90802" target="_blank">📅 16:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90801">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6331bff84f.mp4?token=P68eEoajpplb_AnlF8RGuMeJy9Kf2zVHRs1Pl_Rbq3LI5V7N73c6B1TfYbxdSCmNkjUsQWJW5R_MSp33m1oJ7Ss06Sd-GeJ3CNJ2ohDYo7z3jeFd1FxSz_dRzmvia0VtgogR9WtX8Knc9LTOjBLYWug55lG8GraQi02Hy-4GJNrLsS-b_-eEPp38zBTFkGVT5g2PXIJqtqC6DWL9S8qSWIS4mTI32KNfZd1oVHNkjPEZLl4ECmXKe91BOgr2n55npWQ-XLwutZB5npgD8ovN1-gU4dCSHSFS9z5SVY-TrYDHem54vvwAQE9Kl5kJ0YjoKE_OAvwQuZFU10Rk6cg0ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6331bff84f.mp4?token=P68eEoajpplb_AnlF8RGuMeJy9Kf2zVHRs1Pl_Rbq3LI5V7N73c6B1TfYbxdSCmNkjUsQWJW5R_MSp33m1oJ7Ss06Sd-GeJ3CNJ2ohDYo7z3jeFd1FxSz_dRzmvia0VtgogR9WtX8Knc9LTOjBLYWug55lG8GraQi02Hy-4GJNrLsS-b_-eEPp38zBTFkGVT5g2PXIJqtqC6DWL9S8qSWIS4mTI32KNfZd1oVHNkjPEZLl4ECmXKe91BOgr2n55npWQ-XLwutZB5npgD8ovN1-gU4dCSHSFS9z5SVY-TrYDHem54vvwAQE9Kl5kJ0YjoKE_OAvwQuZFU10Rk6cg0ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم آسیا موقع دیدن جام‌جهانی:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90801" target="_blank">📅 16:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90800">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4oTR4h65ecf8Z6dTs6wwvB2cqHQI6G7EdOenqiDzYTLGhT9LkSPQbKRlWHHcIgjQxvPKKz9_gCA4aAgFZwvJjvXfLAEBqiPJa_8kn8WrR37ADoICQsgyRBysttuOKsW0Chr8fNuYEUXb_fQmqPIPt8sbttXTaX5qIZnsLhSL-6Uf8IkduKOiG2hrvTWuvXGqKB902GEEMTIFH6Mx9eUer4xXcLO67wQKBG7IVF1_b1HRqjc-4E7rblDUCXTvSAl-pL7AxfZvKUVm2_WB9IErZSOYJqoCGvIkvSw5oz4fJ-edXvdwjU7E6VmFEtXVJ4PxVq5tNoAIEdAJrCDdCIRpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ایده 48 تیمه کردن جام جهانی واقعا مسخره بود؛ فک کن سه روز اول اینقدر بازی حساسی نداریم که باید 4.30 صبح پاشی آمریکا-پاراگوئه ببینی:)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90800" target="_blank">📅 15:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90799">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e4e72992d.mp4?token=H1O0CgbHJMvOt-zVInS5WXq2U52gIhqdy9mi1Lg0sg-4gTQjtP5L4RfMVBrAbyFpBx8THJEVJXc73Dm9s1W_mbILDB_vTCKl5kkGJreFChddvXjhrWsHCO3R5c4Ftdh-vtuvPYtOV7xcEWUsIEiRou8RF_jm0cOS7DOfu7EgxbIYoKzSER9b0xKYeDKb8IJDbCXhpb_h0xesZHaL4TtFWO5YYNvRWRE8jiyqWGzvv5SpLnJ1jjc878ScuQufEX70kOXZbwskHCTCRa9S8J5b-cC-WW21wMwXX4W_R0tK2lWYZVp-x0HaZwP1-ImWXlFYTgtwL4iwMLRuX8wSl3hkDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e4e72992d.mp4?token=H1O0CgbHJMvOt-zVInS5WXq2U52gIhqdy9mi1Lg0sg-4gTQjtP5L4RfMVBrAbyFpBx8THJEVJXc73Dm9s1W_mbILDB_vTCKl5kkGJreFChddvXjhrWsHCO3R5c4Ftdh-vtuvPYtOV7xcEWUsIEiRou8RF_jm0cOS7DOfu7EgxbIYoKzSER9b0xKYeDKb8IJDbCXhpb_h0xesZHaL4TtFWO5YYNvRWRE8jiyqWGzvv5SpLnJ1jjc878ScuQufEX70kOXZbwskHCTCRa9S8J5b-cC-WW21wMwXX4W_R0tK2lWYZVp-x0HaZwP1-ImWXlFYTgtwL4iwMLRuX8wSl3hkDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروز قربانی: عاشق تتلو ام و آهنگاشو گوش میدم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90799" target="_blank">📅 15:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90798">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCq4Do2rj3bB4TOKU6i4q11Hho-sKe4ahrS6ARS9sKTybovenRQtgK6SHM1Vt_JB5Jess-ub7T_FYdjKhhX1E4UCeFzPqzY3iG8UnsFa9nuLosLc49r5Mnjc21y8A1QakkC0HzV3Fcz8XNnHtwqeWxQgqZNeZuLM42Llto3WlAXblHwAmSQiFG54Ot-L9Q0Sp4rzz2p2BCLz7U2k3vK6lL_N8P6MWALmWlEUTbbICzZTVZY-dKERuHq4Y34LEdNotkNWhVJkA3TG-6oJL1cJJdnrRCnDmyKZivScP13OkQdmLa2wzBXe8S1whGzhHaS2DXnbmtyV_dMBpKwVtnZ2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: افتخار دیدار با آیت‌الله خامنه‌ای را نداشته‌ام. به نظر می‌رسد که ما با آیت‌الله رابطه خوبی داریم و دوست دارم او را ملاقات کنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90798" target="_blank">📅 15:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90797">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfaf96dd2.mp4?token=t33Y5dCNHljpwwbwB5IEYUiBjtLILQ83twsoil2o8In02Jyb6IUaQVJN48E8qWoaKHW1reKINLAYtjz528CcawHlk7GyqHwX7Kd5Bzh615LNrZ-EvQtas5UKOhtNBCajXeJvWdI7-HVPavSwbMy-26VRw6S5b3WpD22PCkrzWcgmABMo_tGUdlGJAnk0GeUXENVKccrvmxon1ilC60NDBm6_2XzxwCyrblf7-k2bxT4KMYFMakbW4Mq6d_V7PMgQJkYTyOV5OJ979Gusa5g8eQB0BcdBK-JjoJX8p-EI_NQxCnH5kbfOnWdB-0w1ObFAQlj_IVqCrcBdecjpuzv2IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfaf96dd2.mp4?token=t33Y5dCNHljpwwbwB5IEYUiBjtLILQ83twsoil2o8In02Jyb6IUaQVJN48E8qWoaKHW1reKINLAYtjz528CcawHlk7GyqHwX7Kd5Bzh615LNrZ-EvQtas5UKOhtNBCajXeJvWdI7-HVPavSwbMy-26VRw6S5b3WpD22PCkrzWcgmABMo_tGUdlGJAnk0GeUXENVKccrvmxon1ilC60NDBm6_2XzxwCyrblf7-k2bxT4KMYFMakbW4Mq6d_V7PMgQJkYTyOV5OJ979Gusa5g8eQB0BcdBK-JjoJX8p-EI_NQxCnH5kbfOnWdB-0w1ObFAQlj_IVqCrcBdecjpuzv2IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردها اینجوری بعد باخت خنده و بعد برد گریه میکنن..
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90797" target="_blank">📅 15:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90796">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9UULohhlZxEcFOixK20ICmCVlXkarjXOh-Hf_3b3I2q1BCYNd6oBZfg1qL9WQorsRvrnTEGTKjLQJ7c-VSXzM-AOb3WEQIO3gM17DmEE5D9fkfvaAehpRaEAslOShSzCqAhEcWdKai48BnjahKu4VpVUPtrn5b_pgXzLb5IGz7QfRo0cliFjzcGm8NFtqHbxqEpC86ECKNeFpRLyP7qiHTnIRuQD6gZ6C7sQgQ9SdSH_sJ41NQCKHYaOyWAABb6QMr2LPNLONmdlxpPu1LGwt6q087gmRudF6A1KEE9zC3skMzMrpJrUOmPJgbN3EffIIDUUL8AxX6crmD59_30FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
🏆
سامورایی‌های شگفتی‌ساز که طی چند سال اخیر حداقل یکبار تیم‌های مطرح دنیا رو شکست دادن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90796" target="_blank">📅 15:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90795">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
انریکه ریکلمه کاندید ریاست رئال: امشب اعلام خواهم کرد که یک ستاره جهانی درجه یک را جذب کرده‌ایم. من به طور رسمی یک سند قانونی الزام‌آور امضا خواهم کرد که تضمین می‌کند قرارداد با او را نهایی خواهم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90795" target="_blank">📅 14:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90794">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4234f318b3.mp4?token=nR5UDT0Dr7R_l5Qfone4dmIX1KZ1wRPtdqaBhLP0WlOp5ri1EjhJmWo9VLTqcoWiuEcRgVpa_KS7cc-k6zOK-wGs8B4stM0t3j9ekpIeYbFUJAEI7NNrXgU7RFORcfmxcPADjtNGjgvao06W2wtKMLXgXH_-vAuSJoJ9azAfPJ8FIfhsvv-8c_e_ftViMpzmD_NyjkCKH8uhjzMtCZLBmtoE5_5v4JSWG4WD8QmEIM3_xpq_tqgUct-BTzHT1XceNZ8eQvaBfsnQIyho50aN0Ek4BfaRItFDyLhuFqi1t0YRsoQdieKsdd9MRyKR56CC9F0hlI98Mn1gBRuNMXk-cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4234f318b3.mp4?token=nR5UDT0Dr7R_l5Qfone4dmIX1KZ1wRPtdqaBhLP0WlOp5ri1EjhJmWo9VLTqcoWiuEcRgVpa_KS7cc-k6zOK-wGs8B4stM0t3j9ekpIeYbFUJAEI7NNrXgU7RFORcfmxcPADjtNGjgvao06W2wtKMLXgXH_-vAuSJoJ9azAfPJ8FIfhsvv-8c_e_ftViMpzmD_NyjkCKH8uhjzMtCZLBmtoE5_5v4JSWG4WD8QmEIM3_xpq_tqgUct-BTzHT1XceNZ8eQvaBfsnQIyho50aN0Ek4BfaRItFDyLhuFqi1t0YRsoQdieKsdd9MRyKR56CC9F0hlI98Mn1gBRuNMXk-cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی که از هم‌باشگاهی هم شانس نیاوردی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90794" target="_blank">📅 14:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90793">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476676c77a.mp4?token=AcDEAJsjILDKE9NtTr3nsJqZ3Npro6gCuHv_jBAs_TNdzm2HqVfBsiBEU9Y-kI5zpf_ZbED7ZZrKixZ66GXQjq8_HTBh7U84zOfHoSBii_fwbeqY7gbj7uaQSf0L8YDlafgYZ4vCUjdequM0p_Nw2K6N1fDDaMFAqYkC-UWY6OzNwBVfs_wXreaSiulRNgBVWGi5vci899HkJ5q4zzL9xIbwF0k6gZlPNhAQrgcURcw-RvcirBAOzbZGoH3X-Hln-8X3gdZQMus8VvZKlS5c-VJotN9s0Ge0HlCy1-uabNzEtebM-7KJeLXVQGzdzNN8qHuVxqCv3JLbXq9gKXlQiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476676c77a.mp4?token=AcDEAJsjILDKE9NtTr3nsJqZ3Npro6gCuHv_jBAs_TNdzm2HqVfBsiBEU9Y-kI5zpf_ZbED7ZZrKixZ66GXQjq8_HTBh7U84zOfHoSBii_fwbeqY7gbj7uaQSf0L8YDlafgYZ4vCUjdequM0p_Nw2K6N1fDDaMFAqYkC-UWY6OzNwBVfs_wXreaSiulRNgBVWGi5vci899HkJ5q4zzL9xIbwF0k6gZlPNhAQrgcURcw-RvcirBAOzbZGoH3X-Hln-8X3gdZQMus8VvZKlS5c-VJotN9s0Ge0HlCy1-uabNzEtebM-7KJeLXVQGzdzNN8qHuVxqCv3JLbXq9gKXlQiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
🔥
Colombia
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90793" target="_blank">📅 14:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90792">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: احتمال داره بزودی با آیت‌الله دیدار و ملاقات داشته باشم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90792" target="_blank">📅 14:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90791">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9285a340b.mp4?token=tLK-C8oK8oaLgE_TMpBmiLh_GA5GHYKhU9Exa6w3BXfyxu5yPc1_VvWbhh2htbUF5FgRLBENtXxET5tb37sgjsivCzwXbq-3i2ANqL-nkrpyzi4aUSwE8nU--3Sl17yQ6-lM62PhG9zLslBL_YOzgh-a2T_stWxYk64Ng4YflKmJH2fh9AzEhcMa97iF9ohG6aypGhZHL0IhrHrE6XaS9japqkNWmVKTvsaU8ZIHgAjFqNMYqHSqhnhbQ1MOg2y1HV2qf0X3PGmyzlw9ulhn8dhkxjzRhJU3yEB_QAvMrN86-L4db6u1cKv5PSeFxP3hWnZOKrH1vyrVo7RYrWr0Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9285a340b.mp4?token=tLK-C8oK8oaLgE_TMpBmiLh_GA5GHYKhU9Exa6w3BXfyxu5yPc1_VvWbhh2htbUF5FgRLBENtXxET5tb37sgjsivCzwXbq-3i2ANqL-nkrpyzi4aUSwE8nU--3Sl17yQ6-lM62PhG9zLslBL_YOzgh-a2T_stWxYk64Ng4YflKmJH2fh9AzEhcMa97iF9ohG6aypGhZHL0IhrHrE6XaS9japqkNWmVKTvsaU8ZIHgAjFqNMYqHSqhnhbQ1MOg2y1HV2qf0X3PGmyzlw9ulhn8dhkxjzRhJU3yEB_QAvMrN86-L4db6u1cKv5PSeFxP3hWnZOKrH1vyrVo7RYrWr0Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات تابستونی دوستان در بلاد کفر
🚬
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90791" target="_blank">📅 13:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90790">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: احتمال داره بزودی با آیت‌الله دیدار و ملاقات داشته باشم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90790" target="_blank">📅 13:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90789">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1YLjwC5xVSP1VKYs0GEyXhs5rKkIydNTVRu2lBuynCzX_S5NthKnnk_gm825xL-v21N11bYNdMQHiLnmePLPN-DkzJDsuuweZEletDLFc6bJrxyRxs9NI5YC52N6KIxBOvnwP901Eex_Qn1So9Z-qFNl2tpERAlk8sXRRUUDnkW7bZGMxk-AT-8DWsKegQ6PgX_AfXLahudPyIv_rgE1zHLNRIpI26wR12hE8L2gS4Ac0YuIaT15cJmrWxSKPvOP5a8XpJ4EgUJepdlhE2u4ZX_vpQpfro3s8ANmrw5Glv1tA8pnqtVPMi5SPu9AB1oTeCJo2qr0ODA5ZYktToJAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری
؛ یونایتد، psg، آرسنال و لیورپول بدنبال جذب ماتئوس فرناندز ستاره وستهام. تیم لندنی خواستار دریافت ۸۰ میلیون یورو برای فروش این بازیکن شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90789" target="_blank">📅 13:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90788">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NehsRnlrwGXE2_pocryek3YvJeo6L9pnI1UKQzKortQYJaZMkjmVC9kDh9iu4NtrVbJxMQZ4QFOI4ANaOANAe2mlOoGQu8Jg3sPM4gp1k-a1YNZpY_VwnXafk3D-VrpzgDa9CtcdhzFjkiuO_F7-VGIWDVVCdEj4R0b-XLgXGTr1wy29-DpSD5BpApmTniMp8zpfvcVxY6yjDBPD58f9QcAPx6F6eEu3bcKv4Mz2zZ3RBxYtV6EqudoRrn-QoKWMHmAStFr8GvfrNJARV_r8_ZCvOC-taTw8a-wGfuTxF7lf5-LNhDIBvNwmp4GsVTWqYJ1TGOZj3cJ8UoQciGJifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
منچستر سیتی در صدر تیم‌های با بیشترین تعداد بازیکن در جام جهانی
2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90788" target="_blank">📅 13:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90787">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2BIAeOJ8zCaxoj0qxwKtTXQHf9xk9ty0hYvTWWPqaizH7FS_5td3RD8FcpKIyrdhXsiATYev2wNMBrIQaawih58xJcY94f2qvqJFNfPeodjt0RsZljKZ2GJpareC-o98jhQi9-A5KGX2m4o95YEM5Fb6rt5eEkBEPfSS6QjoFqEfeqPwwRx6fCGq2ZsX4PGm9Qj5rO7kMiTnJDyFSxOVQEFE6ZpwWhFcZFtdVYFWpbXvB24Kld6XunO4CkWDmJ-aIedFrt9XaYgTvcNW5m4qUgxDlbE5JbALZM0of_c-lthVv9Ji21B-5DrGumRwR8xFLnBgWsFPTTVYe99FOr9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جام جهانی واقعا برامون غم انگیزه..
پایان نسلی پر از اسطوره و پر از خاطره
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90787" target="_blank">📅 13:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90786">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری؛ ژوزه مورینیو خواستار عقد قرارداد با گواردیول شده‌است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90786" target="_blank">📅 13:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90785">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCxTc2NgsQxiHipLFJSi4wC4AAXXNYpRYhLft84TnFWTUyv4D1Y5kuSelh8z94b-KGVerWAAyaSNclV02mm5AiHor4kx4MkVQLpTzFS2Tp_QC3LecSJQ8NTpYgIR7bous7ivAjAO5Wic_Xoo-D8Pg8MOjeDbRxQ5gaWLD3gEGG_oRZ3T5hufbdRaiCnuLG2WyOY9ROPpI-g7GLN5HcZcUFj7oWsI4Ym1aWKiDGG5a7RIG0220HH7gb5hFECqoexuEzI0gQyMZM1jfY9SjSl-Kqz0ohyIGN5NPG8BWARMClUNbsqdUj75RLdOkxP2SEShQMALgz9lX5atGAXzYyCVUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری
؛ ژوزه مورینیو خواستار عقد قرارداد با گواردیول شده‌است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90785" target="_blank">📅 13:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90784">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWkLsZjCj-nk9nybQb2cPu4aYteuYJ7mL8YUzv-MF9vFUyDPljIdj3hGS8geKCeKBLkCCwnvQuRvyA6lGQZsO-V0gahrPgY3-hoEqev2-aovG58IT4t2pDdkP_JudM8RJyZiqBCsB331725KSPvZ21KF5vkTPhh_Hbt8nzg6-VzSHqy-n2wTAzMUjVjAKt_PyGnXn2GYp1XHGpzR56Q-oKMROGNi3thc0_byStf563VNOubU0Z2BTFVLo4scVPAH1x2BrUkKFelRMUMVrBKJLG9LJBhuIhaGpWfLXC4Yhu6RbZmk7MtB3ckz9Y5r8zmQ4-kUsvruyO9htJ-cty4e3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستام وقتی میخوان تولدمو تبریک بگن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90784" target="_blank">📅 12:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90783">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8caed85c.mp4?token=P5nKbD6YzL7u6qYL0NUsZbwuKObFPk1UVXHy35hP1RRsNdMhlhxP0zZFwfJ3KgFCFfEGX201miUclaPKwIdAqfNxsR_4TYls9tbl4lpb7aZsTWKZYWG-mQ36mOFUm52hHokhDB4iaQ8OsyJeRZiHYdHSLZ7o_gRvKXSPDKRpUA-HguI4MdDWeqrGD_ner6K_PmNClFRKlAWWNpxzEDbsX_Udw7R97l8UkrLW4MBwx5-2uZFmtDXAkXPptcGVMKqHSd2wcwog90zzBhiJX0fLQbsB6dHetrkGT9b7LMc5Be0ec5KF199Z1moBaplPVI4SJTFuLktpReWmwHBm5KrScw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8caed85c.mp4?token=P5nKbD6YzL7u6qYL0NUsZbwuKObFPk1UVXHy35hP1RRsNdMhlhxP0zZFwfJ3KgFCFfEGX201miUclaPKwIdAqfNxsR_4TYls9tbl4lpb7aZsTWKZYWG-mQ36mOFUm52hHokhDB4iaQ8OsyJeRZiHYdHSLZ7o_gRvKXSPDKRpUA-HguI4MdDWeqrGD_ner6K_PmNClFRKlAWWNpxzEDbsX_Udw7R97l8UkrLW4MBwx5-2uZFmtDXAkXPptcGVMKqHSd2wcwog90zzBhiJX0fLQbsB6dHetrkGT9b7LMc5Be0ec5KF199Z1moBaplPVI4SJTFuLktpReWmwHBm5KrScw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇫🇷
تنها تیم‌ملی که تیم‌ملی نیست:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90783" target="_blank">📅 12:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90782">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQ4iFSUSUM20eJmBxkMSnODy-MIsiBxgq88mNm-w3fiSE8V9IbFmj1BHSM50jXlGAx8iQLRns7yTb4bq1PY3igQJCwjBflh0--7qUWPsxwYzytdn3FCEjqnBsUBAjKQhdSF6BEj-MQa_8qOV1KL--f4BnmqCZglvxeHg0oSpKHbV-SD-394ICSKj1ijz694vRhox5TtgluUD7FUh9HVFo9BAOFrgStiL7rfh3rBHwSA2EJogS2HOC23-sv49yAgaR7g2oPls2ALXP8sBAh7fenSB9PFkUuf4earcsqXSRvwk8KPzH0DX-Y1zbqruz0Y8UajUv8H2dz5H1tMWNOB9ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پیراهن اول رئال مادرید برای فصل 27_2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90782" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90781">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c9a85cfef.mp4?token=ZvrrRyMHVZ1BMIYyIdTK13-H4V3NwBhg3QxwHOsytH_mHw6oaAgtV66O5AaqCDT6I5OCTP_thxQV2RJyHWlHzY7iHMnAxUOWjOZ4TsJzUuSAt0Ku1DjWt95YZirAMwYh7Or4B5T44_jSzoaYTSMBGttcSuSK9EeBnrNNGDQYUP7PCGkFFxd1UvvN-ZWU96AIreVaDFuShq6xVPUIWXA1N78nvdgUxrwYjjfK4SMZMN7Je8WLKY5j6RY11mzjc6vLZ6I2pQAfTfTBXFnDJQQfRjvZpJRj2ngL-yU-x8sNmGiV7eS0tR-rwy1VjEo-L84C7Pvi4qhvuJjVH5AXfh1wrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c9a85cfef.mp4?token=ZvrrRyMHVZ1BMIYyIdTK13-H4V3NwBhg3QxwHOsytH_mHw6oaAgtV66O5AaqCDT6I5OCTP_thxQV2RJyHWlHzY7iHMnAxUOWjOZ4TsJzUuSAt0Ku1DjWt95YZirAMwYh7Or4B5T44_jSzoaYTSMBGttcSuSK9EeBnrNNGDQYUP7PCGkFFxd1UvvN-ZWU96AIreVaDFuShq6xVPUIWXA1N78nvdgUxrwYjjfK4SMZMN7Je8WLKY5j6RY11mzjc6vLZ6I2pQAfTfTBXFnDJQQfRjvZpJRj2ngL-yU-x8sNmGiV7eS0tR-rwy1VjEo-L84C7Pvi4qhvuJjVH5AXfh1wrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇹🇳
این دختره که می‌بینید از بیکاری زده به سرش و رو قهرمانی ترکیه با شانس یک درصد، تو جام‌جهانی بیش از ۵ هزار دلار شرط بسته
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90781" target="_blank">📅 12:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90780">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0dddef5c.mp4?token=j4l2gQphZ0SY2bT1Dl0fnlw6q8WBUFsOvndQDLmtj68ks752ngmONyXLNcPXxkA2GIDTSAkdKPmgAchq4ppRrYXHoXNszvkB_PjORLTkXdRdV_G6nnYDw5s5bfE0BGgPaTVKSWZcoWin5sPbZLEi43RV1nnTVWgvG7qUSmI49VxBMvFdq5B48rajh8KG091ynbHYoXUs4CiT6Bw02AC4AAwAktWASapT5xhTZfmNqci3yNH2X0ejb8KLHCdmnGiRXxn8J0zsnX3WuxfUZM8QKZIG1DnmYS06STGxKeTirOtC-0LDLWU3SSEu0W7Aeb6vocRs1o6g11suzgkddtLkgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0dddef5c.mp4?token=j4l2gQphZ0SY2bT1Dl0fnlw6q8WBUFsOvndQDLmtj68ks752ngmONyXLNcPXxkA2GIDTSAkdKPmgAchq4ppRrYXHoXNszvkB_PjORLTkXdRdV_G6nnYDw5s5bfE0BGgPaTVKSWZcoWin5sPbZLEi43RV1nnTVWgvG7qUSmI49VxBMvFdq5B48rajh8KG091ynbHYoXUs4CiT6Bw02AC4AAwAktWASapT5xhTZfmNqci3yNH2X0ejb8KLHCdmnGiRXxn8J0zsnX3WuxfUZM8QKZIG1DnmYS06STGxKeTirOtC-0LDLWU3SSEu0W7Aeb6vocRs1o6g11suzgkddtLkgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بسوزه پدر هوش‌مصنوعی که مردمو از راه به در کرده
😊
🎧
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90780" target="_blank">📅 11:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90779">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vcn_HozHGDpage1KIaTkPDiqZoznb3JLypd1d8XHmDbRycVLXiZuodJOen4zJTSN_5oYHP7cOyx4_qOZvGjuh_NoHB-QqHfoOBID5OCLythScY-s7xcrZy1EA5KrhpqBU2GQrqHU2wV0gjao9tUJieWx00BZw0u91cHC4SRxSOp1GHUYNXLQLN0fOrbxREPOuIIvmQ7AaX0HiIh4Z2zpl-Ng4h2Ojqdj3EQK8SP_sOwM1Qbv8MfX7ov_5XB3pIqGM4bOkMq-wqxg2Vol884JD3poXhxPZTlqn1oYKVL_TsghdgtMAJE6cD01Q3RLkQE-fqJJC49B9732BJ6BDv0Tug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
توپ‌های مختلف ادوار جام‌جهانی؛ پیشرفت تکنولوژی قشنگ حس میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90779" target="_blank">📅 11:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90778">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d071cdfe94.mp4?token=AOMIcAjtvsn4clITNEFhAr5GrhSsf--u_d3qq1MacRoDkvZ6B-7Ml6x9_ru_j5aP2a_675JvkhHTagRvdv7WWaVFpWdtFSBUeVn8xMNUM2X5OVhPYgS4Iep0bE_POV9Vj9zdzcRxBCbz83xMCB9rBRdLVkvV2dGY4oX6aQuANfZ8OqaF4ja06Mq5m53RUjG67-o6OTENv-Sh0EWEyMpPxGF1mCLaIlJO79S7YJruT5_girQHe1YGygXAe5YOYEuzKZQHw5r-WEytRISaT1qCCUPKS__wU2Pbs9TncPQrWolR0uBrX9cwgn0nfVi3J9BTz5Z6-AegzTRksQzr1ZLEaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d071cdfe94.mp4?token=AOMIcAjtvsn4clITNEFhAr5GrhSsf--u_d3qq1MacRoDkvZ6B-7Ml6x9_ru_j5aP2a_675JvkhHTagRvdv7WWaVFpWdtFSBUeVn8xMNUM2X5OVhPYgS4Iep0bE_POV9Vj9zdzcRxBCbz83xMCB9rBRdLVkvV2dGY4oX6aQuANfZ8OqaF4ja06Mq5m53RUjG67-o6OTENv-Sh0EWEyMpPxGF1mCLaIlJO79S7YJruT5_girQHe1YGygXAe5YOYEuzKZQHw5r-WEytRISaT1qCCUPKS__wU2Pbs9TncPQrWolR0uBrX9cwgn0nfVi3J9BTz5Z6-AegzTRksQzr1ZLEaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
▶️
تکنولوژی فوق‌پیشرفته توپ مسابقات WC که دیدنش خالی از لطف نیست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90778" target="_blank">📅 11:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90777">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr9v7ZMuB-RFVdzSfTeNholhcE4rICBtTkZBZy72-ZVJ9HKvOTEN4NudeY3aULBKRVdwI8FiMRnsPFe2XrExbwUUARZEaGMexrdioJy4YHDacV3mKtJxAzuApPI4oTAJ1xrx7dxPTxnUrQn7cTTxzcyC6vYmR1lfJbxScHdo_mxP0X5ygpoB8YrZs4Ppx7FhhtzBjBr3bfJj13TBO9_SeJYx1aYQTCBqf_a3pWnn3TtQdZQDRdHrveUWqWrkMJFsckQ0ckzPO3I1Nb_nPavXMDzwHPM1Oxmuum4Zt02YjnS52iw0kBUIAVarieFs0Omq4rbkn_nykadBRdXSL8Treg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
اطلاعاتی مختصر درباره ورزشگاه‌های WC
😃
نیویورک/نیوجرسی (MetLife Stadium) – بزرگ‌ترین ورزشگاه آمریکایی میزبان و محل برگزاری فینال جام جهانی ۲۰۲۶.
😀
مکزیکو سیتی (Estadio Azteca) – ورزشگاهی تاریخی که فینال‌های ۱۹۷۰ و ۱۹۸۶ را میزبانی کرده و میزبان بازی افتتاحیه خواهد بود.
😆
دالاس (AT&T Stadium) – یکی از بزرگ‌ترین ورزشگاه‌های مسابقات با سقف بازشو و صفحه نمایش عظیم.
😀
لس آنجلس (SoFi Stadium) – جدیدترین ورزشگاه جام جهانی و یکی از پیشرفته‌ترین ورزشگاه‌های جهان.
😄
سان فرانسیسکو (Levi's Stadium) – ورزشگاهی مدرن در سانتا کلارا که میزبان چندین بازی مهم است.
😃
هیوستون (NRG Stadium) – ورزشگاهی کاملاً سرپوشیده و یکی از برجسته‌ترین ورزشگاه‌های تگزاس.
😁
کانزاس سیتی (Arrowhead Stadium) – مشهور به جو پرشور هواداران و رکوردهای تشویق قوی.
😄
آتلانتا (Mercedes-Benz Stadium) – با طراحی منحصر به فرد و سقف متحرک، میزبان نیمه نهایی خواهد بود.
😃
فیلادلفیا (Lincoln Financial Field) – ورزشگاهی مدرن با جو پرشور و موقعیت برجسته
😏
😃
سیاتل (Lumen Field) – یکی از بهترین ورزشگاه‌های آمریکا از نظر حضور تماشاگران و چشم‌انداز شهر.
💥
ورزشگاه‌های شماره ۱۱ تا ۱۶ عبارتند از: میامی، بوستون، مونتری، ونکوور، گوادالاخارا و تورنتو که همه میزبان بازی‌های مرحله گروهی و حذفی در جام جهانی ۲۰۲۶ خواهند بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90777" target="_blank">📅 10:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90776">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXh2xxvdhEVrv2_DTKSK6GP4aDMuKlwm-MTQr7AXuKLJjb8X2wdPN2vy3ibsdVw9BlapA6iRDdUZe2-ME9NKaam7vUfLHMTpbEFRrUij9pgKLqW70vO7k2-EbdQlZ5zLs0AOlUNckh-9fi8hPXYqyD1op6lllBJWTj6Y0PYFiJt9_sJAuf9_8Qh15Q1hwe8ERi8r8OuYwzpC8gZ3y_O9XePYyTCNZWRnBcnXY7pPL_cYBVSp3D71B29QoQSJTC1ju1mdIxuB26LY1H8JV5dHhPPO3olKoEuX-cjWrzQbRB2CbX8NCheoWViM2AxvT1XazKOwbK4yZb4EbE-HP_GA-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرز : فردا از اولین خرید رونمایی می‌کنم و همینطور این هفته از مربی جدید رونمایی میکنم، این تابستون حداقل ۵ خرید داریم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90776" target="_blank">📅 10:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90775">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f607323bfa.mp4?token=VrCFwTRodLo-vHSyjHJIuN5EH5Ck2gMhf5LzobAlgsFWcfZOxs-dyLDbXV8S8Az3Jf_Asg9ZJk06ADLPdGNcolM8nVY0DIhzVldTc82Y42QKqKFdb2F0GuVLTuEUaz2iuUioLopAMV2rKmNV_I1q3QdrtLLTv0GNOjUP66fHwIh5vw883s_GsJ5IAjJaGE_17OhuVUR0pWOby_iw-iS07H2Wo2fACHUKHiXBLjLu0dO6FUmm3Ac9pFlxUN-3pJAxbL4GsrM55UiP14Zuw4KE6Z9eEqG1bI2RaMQc9IlPJ0q_pupxdWyavy3_vjThdW7Ahe60ye-NLmDvWlvsptgyyVShER-duxxy7p_eofzI_-MY_sJCw7_h-4VDbPdFx0A4xhqIKXNlKaJmGYMB03q4hW91MrHbWp3KMjL45yT30k6ReualYjhPCzzM4OjgDfNi4wABl7Hq-FgFg5JybYOh6d4vwlr6tCgdcqNifBtSnWa-dgAZZrH8k00fOXrr-32BHcKxc9G9GhP56XT01QlT8iavTfYyFZ_yNPBbc3kZG0u9pXewzLelZvB_h9edWHKPrMdb25Ybam6ilk5yXTG6QroCjlpGd-cdiXzDxNYKvD7NbWd8yKmnUK0HI2wK0eiPwy8Ed2kpfdnvvFt1pSScivrK_hlRqtGq58ilBRZhu2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f607323bfa.mp4?token=VrCFwTRodLo-vHSyjHJIuN5EH5Ck2gMhf5LzobAlgsFWcfZOxs-dyLDbXV8S8Az3Jf_Asg9ZJk06ADLPdGNcolM8nVY0DIhzVldTc82Y42QKqKFdb2F0GuVLTuEUaz2iuUioLopAMV2rKmNV_I1q3QdrtLLTv0GNOjUP66fHwIh5vw883s_GsJ5IAjJaGE_17OhuVUR0pWOby_iw-iS07H2Wo2fACHUKHiXBLjLu0dO6FUmm3Ac9pFlxUN-3pJAxbL4GsrM55UiP14Zuw4KE6Z9eEqG1bI2RaMQc9IlPJ0q_pupxdWyavy3_vjThdW7Ahe60ye-NLmDvWlvsptgyyVShER-duxxy7p_eofzI_-MY_sJCw7_h-4VDbPdFx0A4xhqIKXNlKaJmGYMB03q4hW91MrHbWp3KMjL45yT30k6ReualYjhPCzzM4OjgDfNi4wABl7Hq-FgFg5JybYOh6d4vwlr6tCgdcqNifBtSnWa-dgAZZrH8k00fOXrr-32BHcKxc9G9GhP56XT01QlT8iavTfYyFZ_yNPBbc3kZG0u9pXewzLelZvB_h9edWHKPrMdb25Ybam6ilk5yXTG6QroCjlpGd-cdiXzDxNYKvD7NbWd8yKmnUK0HI2wK0eiPwy8Ed2kpfdnvvFt1pSScivrK_hlRqtGq58ilBRZhu2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
مکزیک، یکی از میزبانان جام‌جهانی هم حسابی با این طرفداراش خاطرخواه داره
😂
😊
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90775" target="_blank">📅 10:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90774">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c4dc141e.mp4?token=DnWIn3x-9sejDRnMFigE4AC8VuoBnL8qvoqxNlvweDXI5AeF3BIgePwA5dpZf7tYFVumpVn_j_FYTupcLYE5rjfT-C1NTNV95DUuoEqqTbyWEz7sPEnvWjfWn30TfaGErNV-Mxx8gDvHtddftnAsgrS4DGYh2nNGUOceQafteccJJvHjRAxCaxXPFVMK9FEOxgI3CtggJ1yLfGLCiigOI2T3K2J7ttqWbPUFPPCEvqZC3Tgt6kTm4ZZCzJCzFB5tIQkhzPOmfLjZHEXm-Ee1vo8tG01V_ykYwcC15rKnFgYrLIPFZlvM0RRCgcuMfKHN07buaWKplwP_TZuPgGrgRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c4dc141e.mp4?token=DnWIn3x-9sejDRnMFigE4AC8VuoBnL8qvoqxNlvweDXI5AeF3BIgePwA5dpZf7tYFVumpVn_j_FYTupcLYE5rjfT-C1NTNV95DUuoEqqTbyWEz7sPEnvWjfWn30TfaGErNV-Mxx8gDvHtddftnAsgrS4DGYh2nNGUOceQafteccJJvHjRAxCaxXPFVMK9FEOxgI3CtggJ1yLfGLCiigOI2T3K2J7ttqWbPUFPPCEvqZC3Tgt6kTm4ZZCzJCzFB5tIQkhzPOmfLjZHEXm-Ee1vo8tG01V_ykYwcC15rKnFgYrLIPFZlvM0RRCgcuMfKHN07buaWKplwP_TZuPgGrgRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بهترین‌گل‌های جام‌جهانی قبلی رو ببینیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90774" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90773">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9ae696fa.mp4?token=szUWf7HVzeW9Vn4arAkM8nyVPqEwTgb_GukMPBtHy1KtDZswmMFphew0wyXhbaHPbdN54tSV6-HcZuI4HTJMz9Btyuxo9aW4dvvXh-TxJJp44GR-SPy7ZtmbHFKSi-xJut3nHEmY93VUObGqgsKApajtzlsNtjhA5B_2vhJzabp1XDLavaSHP0bpVoH8vo3wsD-GjuAzaDotlTqFmzyGf0Cawll7FdcABZjEcwHUKzXU04fajw_akt13pfstwVc5lh8wseb9tFwu3A-wA8W5FEyMWRyanvLm53PV00azzA6vWxgH0h4siSl1Ynm8cDc_Q_a4-gvYDiawJzUU8jGIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9ae696fa.mp4?token=szUWf7HVzeW9Vn4arAkM8nyVPqEwTgb_GukMPBtHy1KtDZswmMFphew0wyXhbaHPbdN54tSV6-HcZuI4HTJMz9Btyuxo9aW4dvvXh-TxJJp44GR-SPy7ZtmbHFKSi-xJut3nHEmY93VUObGqgsKApajtzlsNtjhA5B_2vhJzabp1XDLavaSHP0bpVoH8vo3wsD-GjuAzaDotlTqFmzyGf0Cawll7FdcABZjEcwHUKzXU04fajw_akt13pfstwVc5lh8wseb9tFwu3A-wA8W5FEyMWRyanvLm53PV00azzA6vWxgH0h4siSl1Ynm8cDc_Q_a4-gvYDiawJzUU8jGIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پنج سیو برتر فصل پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90773" target="_blank">📅 09:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90772">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxutua3NvdW08Ha-c-J1akBEBbivwwSs1ksCJjZCx7Vm5Ta9aUqx0M5WF4ubvz-dMl9Vv6ZwBnHivTMDdCjOLf0V1SlzI0oKN_P6dmrG266ZsZ8z43aur1EPwVOYJqG6c1zKrBTi-LMyuH7tRI_6YaiGsUHorR0MqOrkTTiCtec719z_rvYhn4D_A1HcwG2pHczIiTBl_HpK7f3sPclBGtvlvTlUvh-F8zQggmI0wN0oTEZkdrcDJt2RNDJPIOGIGMgcEGWjw5iE_T4UwxsZVAZiY8xb7M78VhV-nd1-70dW0NseDBKFaMpfs7LeKENHl2P3fflwXPIbGrTnhKm0yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🏆
۱۷ روز هیجان‌انگیز و متوالی که هرشب تا صبح فوتبال در پیش داریم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90772" target="_blank">📅 09:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90771">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgHHXC7D8ZHy3X9-mCclkge5n_U3I0tQ0y3jwwf6IIw8jDtAJoBEfBW6mYzAVcWfIYt0yC43qHoFsxc3T7xePoJZtZQwA8I-yNwsX0gko1HusZ1kacoJ72jLxg1naJHHjzEwIYYgjZ1DHd_KnczsUf7vgLGcgsAZ2oHa-JUxDIjF9-X2x59WsW5aJ4is5EM8bzRF1NvNdXVSf0V1xZ7P1KcWfJjhT3mjm8_Wn5QpOceyRMaWbGza7PMd3b6XMu72AdQFCgdBaqqXkkB3n0Lt_HOkX36Xrdhj7ktSPbPtOkmnqnRWAcJxtA6GWR0ccIRC-oHaDgZ4oI50mxRdO26i2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فووووووری
؛ اینتر بدنبال جذب دنی کارواخال برای جانشینی دامفریز
!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90771" target="_blank">📅 09:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90770">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ولش تهش هرچی شد، جام‌جهانی رو با اینهمه دلبرررررر از دست ندیددددددد
😍
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90770" target="_blank">📅 02:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90769">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b603dc908.mp4?token=bgEEygjEk7Oom60_A_KG2nGkBOEoZEJSgqwQ4blWnYGsKXNnTd8X3LLpqQmEc8dU46bWhgjgDjQrYdeDjV5qyL9BEcXKucYeoNbjryhiUSUEgtONVeHQlTsR08jgi5HCGGzE7oEGKkOa3aoXJFUETe5gP30JpRu2eslsKkh0JlweMPLDyRn2yT9XRSQuv-1sQTP71cvOAhK4nadWLR4-iMYX79Km6Fl_yg-Nh-nq3tV6325rXU0KuvlQEtOC9lZTiuIn8MyIk-98JI0EgBLSbAOIC7Kc_6DXwmuwoc-j_86yiM0KdYHmhvYxncgqNvnpQRdYG4nEShSFux17DXe9UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b603dc908.mp4?token=bgEEygjEk7Oom60_A_KG2nGkBOEoZEJSgqwQ4blWnYGsKXNnTd8X3LLpqQmEc8dU46bWhgjgDjQrYdeDjV5qyL9BEcXKucYeoNbjryhiUSUEgtONVeHQlTsR08jgi5HCGGzE7oEGKkOa3aoXJFUETe5gP30JpRu2eslsKkh0JlweMPLDyRn2yT9XRSQuv-1sQTP71cvOAhK4nadWLR4-iMYX79Km6Fl_yg-Nh-nq3tV6325rXU0KuvlQEtOC9lZTiuIn8MyIk-98JI0EgBLSbAOIC7Kc_6DXwmuwoc-j_86yiM0KdYHmhvYxncgqNvnpQRdYG4nEShSFux17DXe9UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولش تهش هرچی شد، جام‌جهانی رو با اینهمه دلبرررررر از دست ندیددددددد
😍
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/90769" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90768">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=I9aTDNniuudwos9-__QgmwX89oVzaFWsII8zCFs94EJPHiHIXKbMpl4RA4eoqUqaHAhzIt1zqpXRUW4iwe2gMQMv0bT5qS1yvhv8uSbctoFjacQpyMmx3_6D1a-ydIrREXa39ubAGHCsyPwilfLK1z5Khdrl0GqqPkpLhx86WAEwQqphY-tPmHXczPhv5XnCjlsvz0w-HRlnu7DGWvWawpYA6lDqjaETxF0xzmZD1PeGdnqNaBSR9gTqzp6KXisLoNl7huu56LwqNH1mC5qDKuGh6YjepcLkwe03yvb_7r7OsSeQNte8v3ZLXnlGsq0HJoRYKQJAEAfptseZEj_qWSyOtbAAdydiTfrNBx-vsoWIzuYHR1-8JnhmSyHoojWG1-KLiKNAl2o1q7TWrpsEKFUuBxKQHbSQysXPWlwOlqq3hyqkxVL-FI-uCeuiypgQYgEzy8_wMEBY2WVDjE-OxJ_zWs49LX7iI08gxJSjeN5t_vPFLeqCyjI8Qu15IOAYU7us0JerqqaKEEgh3pddzLNuTFdLYyGBBeNVa69ndv2ct8GZri4jyMks1FI98kKz8G8-rI7FQoxiGHh6YoWRM-4uGnaQk-hbqoP4icWnGqjo0KeRtZptkuMI68qroOyypgiVr8IBj3HKbYS50yTBZs_m_kKj-gUU2nky1GC7qD4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=I9aTDNniuudwos9-__QgmwX89oVzaFWsII8zCFs94EJPHiHIXKbMpl4RA4eoqUqaHAhzIt1zqpXRUW4iwe2gMQMv0bT5qS1yvhv8uSbctoFjacQpyMmx3_6D1a-ydIrREXa39ubAGHCsyPwilfLK1z5Khdrl0GqqPkpLhx86WAEwQqphY-tPmHXczPhv5XnCjlsvz0w-HRlnu7DGWvWawpYA6lDqjaETxF0xzmZD1PeGdnqNaBSR9gTqzp6KXisLoNl7huu56LwqNH1mC5qDKuGh6YjepcLkwe03yvb_7r7OsSeQNte8v3ZLXnlGsq0HJoRYKQJAEAfptseZEj_qWSyOtbAAdydiTfrNBx-vsoWIzuYHR1-8JnhmSyHoojWG1-KLiKNAl2o1q7TWrpsEKFUuBxKQHbSQysXPWlwOlqq3hyqkxVL-FI-uCeuiypgQYgEzy8_wMEBY2WVDjE-OxJ_zWs49LX7iI08gxJSjeN5t_vPFLeqCyjI8Qu15IOAYU7us0JerqqaKEEgh3pddzLNuTFdLYyGBBeNVa69ndv2ct8GZri4jyMks1FI98kKz8G8-rI7FQoxiGHh6YoWRM-4uGnaQk-hbqoP4icWnGqjo0KeRtZptkuMI68qroOyypgiVr8IBj3HKbYS50yTBZs_m_kKj-gUU2nky1GC7qD4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اساتید یه چنتا موشک سمت بحرین و کویت ول دادن. ایشالا که دم جام‌جهانی خیره
😐</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90768" target="_blank">📅 02:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90767">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این وسط که احتمالا خیلیا خوابیدن، دوباره خاورمیانه قهرمان درگیر آتیش بازی شده
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90767" target="_blank">📅 02:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90766">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این وسط که احتمالا خیلیا خوابیدن، دوباره خاورمیانه قهرمان درگیر آتیش بازی شده
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90766" target="_blank">📅 02:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90765">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">💠
سلام دوستان ! اسم من مبیناس صاحب کانال مبینابت
✅
👌
💠
اعضای کانالم روزانه 3-4 میلیون کسب درآمد میکنن
🤑
💠
میپرسی چجوری ؟ داخل کانالم عضو شید و شروع کنید
🔥
https://t.me/+vt7V5iY0jVhkNWU8
‼️
اگر سنگین شرطبندی میکنی عضو شو آمارش فوق العادس
🤑
🤑
👇
https://t.me/…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90765" target="_blank">📅 01:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90764">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxQyds6CDZs1omK2RDAL18g26gElGEuPHXIm3adV4V9bxAiDb9w7C6i7kyMWPFD8GG2ZVosHAPiBLmoHoSigwRG4XC4wcsbCKNO3j1QY5mTXE3dyrC6KmoPg_jq4dXLxRAzUTJFIZhRkOb5mKt361VyB_bRIdpoq6zkCcUClugxSXsigA6J4hNbAcFiBQij4hoO35e5k2ED6ivHqPRwqwTwCzwD5-II3NVDbyT9EQ8EgbPSSfd7O6rN04C62XxgUvGTUkO4MEYAMi4HoIG5KsEd8_Bp5fw8aNdRLpHuMYkBHCqDBmrve9Qm20hzHl3IGmdnYnG_287AQYsFPe1aStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💠
سلام دوستان ! اسم من مبیناس صاحب کانال مبینابت
✅
👌
💠
اعضای کانالم روزانه
3-4 میلیون
کسب درآمد میکنن
🤑
💠
میپرسی چجوری ؟ داخل
کانالم عضو
شید
و شروع کنید
🔥
https://t.me/+vt7V5iY0jVhkNWU8
‼️
اگر سنگین شرطبندی میکنی عضو شو آمارش فوق العادس
🤑
🤑
👇
https://t.me/+vt7V5iY0jVhkNWU8</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90764" target="_blank">📅 01:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90763">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1JsKrqn8QtbxQyoKJ_wHAg_zfe3WywjfM1eUdOD3N8fGDdmUH4ZGwj_789-ZfwHtGFn2Ac2hNvxyCyj86q1tD4KamGLzrGF_wX_xNpQ-rPUAC2hJWqIXyYAI4SymdskZ5bv3nTgJj6wQ_169Ju5h4dqXrqSH9AJ5kX8C1sOaFdr3PX0iK_R3wb6z8GLzkYjL1rfh-1Ygs8ULM3h2ahS_5IUuA_fVZZPTN_pDFYpDjV1Bo_VRmL2PhGJNyp3wz25sm2ybYtjeWqjSMZxHpEZAC5ZzlQx7HRXLE4j7YnchpJG9UYrRh8DckLIUV8ZrtRy56shi9fMBaS6mMcY6smdhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مودریچ، رونالدو، مسی و اوچوا از جام‌جهانی 2006 تا الان حضور دارن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90763" target="_blank">📅 00:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90762">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi_3aOIkfjbWG12R6qRgPgBn6QBNIOGxDYeUJJRoGcjK-OqXY98lLe87rWavalc8jghJo7qpY-CKpIx1uW7n8355PsxMZM_qEBkNisVr7KZ9C2FKt5oaauf4ifnsSpoXHoI4Qe9fiySVp08RI85kdUf15E0ObEw0cjtkQecANRDMW8r2TO4euqrhCG2RDOsFMM7Ir2SgbwrHuofd0UoOty4QNr2UoiSGSRNKEsLgLx0LpUD7BA6R82caN8x7k0twW7wKju6BB3OaAe8yje5KsHUHVRkU38n4oWfRBf-3mPyhKzQqdnBgGqpgk-6gYAO_MkQKtYLcPronw7z-SR7TVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوووریییی رومانو؛
دنزل دامفریز به رئال؛ 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90762" target="_blank">📅 00:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90761">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/orOf44s0d7C7ya_oQOd84V6bsi6LxuQ6O-wU9H4O0J5u84qJuQcx2YzXQecSDIxzOkGmFj3QuMR7riu4KlfV93FX3Ec3a9ZWh2TJdTDSWbz54oGNKRsfSDXQUHSW8nuyXSF9u40wnpkt1QoiWuW6UDng1s4axb7skIFWuX_KnL0VLoAwzh_sB4KRZtxZwPgjE-iB4bVTz03mzkWgCtOoFu30AdczIJ2PRsGy9erNCnM7_zMKUjvXEISYORBsK-wIots4H81_5Sa4oP06tMZ_crUnEbJRWoBjhu5NONw1qPKq3zDy_LTE_6kRpHAFrLSu14s5jtCT-lXIuV41Rsvq9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولدت مبارک کون عزیز
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90761" target="_blank">📅 00:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90760">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnUHOziQNtNEOtrmt3ZLTqojOiYAZ9FWPxX4_6XsiUEdHN41wFHgvq4IQDSxI-NVuPiVnP3hh2oClYftAXldGznVBtDVoeQN0ZfzlM2-wrHGWmxe-foDiAeK7GOPk99OlU1Fv2sJByb5fJsx8KDEPN5QmdXJMdFuaQb8P1f46b9msNCQ4mQgFbVixCs5yAKmBJ0xCxUcumX4_LYYfIHFMKVy2_rd_-0UVdhXbdHgUZw1P4CrwglduNn5kZW2CfCdkAV3O0lRV0c94pypal2ScENQG8S9rg8GxaW0b4ZfVi634InoIW3hot-BTOalmHdyH-jwlOMtYaKGnH4hD6ByGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎇
جشن‌تولد رضا شکاری با حضور همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90760" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
