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
<img src="https://cdn4.telesco.pe/file/BHz2rOn3dNwbhVZO33DX8ri94Fc-n1txl5Va6dOPTB_LGCTp2BMYGuglrR9_R370npXe0YoPVhJ3h7S-Q-ILsymc42LD_o34x6f4HDh4lJkIS2QkS2PWHMvBfshOXvutBiicdb29TVJl87-QR9-11umtpov5LzcZJpfIb-Xp1c7PtXgOVSueLg8qihBlmDDGKEmQaJ0mR970RXyuAAfS9ho7p8b78vN9IJPmNSygaRTDOqH50RhuQbXRGJ8Z7YaqIVg9cyAqFKuj3r6Vc0oxVIijg0G-3_-1Yw0HRpL3UzSUHp6_lF8yzoN4Eha3CaYStRCCrG2-ZN7yVGI3b-elwA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 301K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 14:56:10</div>
<hr>

<div class="tg-post" id="msg-14009">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما در صورت تداوم حملات، از جمله در جنوب لبنان، اقدامات شدیدتر در راه خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/withyashar/14009" target="_blank">📅 14:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14008">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسرائیل هیوم: اسرائیل و ایالات متحده پیامی به ایران ارسال کردن که اگه تهران حمله دیگری انجام نده، هیچ حمله‌ای علیهش نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/withyashar/14008" target="_blank">📅 14:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14007">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e67efef8f3.mp4?token=B79DE0KuwcVWYl71-Lo9W313yrGdhcFfuxEfk02TJIh3ZW2ulxUDcNn0mECFgjWLaknSD2hLpQIRYOY1wW0G2U5DTSbyNNtxqbc2SwDqVzlGu6QLq9oaXxWCAZ_uDIUrCms7tnKxnWgLHlT1YT_gNBrTU2i-VzFuEpWW5uDa_AOg3uGJv2w8ODn0EAcPbDSGdyYtOua4Kf6dkAHEiUlX8m8aTpdEHEraeZ3WCc25bGTS1DlMow6BGaTXdWlks8uh98TyKaDaZEerHUl0GJ7PnN5GTnqWZzZVhyXaOgiAUdM01HcD4nq4ZlIfyWETj3G_qADrznwVWqcBiDIf0Ymm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e67efef8f3.mp4?token=B79DE0KuwcVWYl71-Lo9W313yrGdhcFfuxEfk02TJIh3ZW2ulxUDcNn0mECFgjWLaknSD2hLpQIRYOY1wW0G2U5DTSbyNNtxqbc2SwDqVzlGu6QLq9oaXxWCAZ_uDIUrCms7tnKxnWgLHlT1YT_gNBrTU2i-VzFuEpWW5uDa_AOg3uGJv2w8ODn0EAcPbDSGdyYtOua4Kf6dkAHEiUlX8m8aTpdEHEraeZ3WCc25bGTS1DlMow6BGaTXdWlks8uh98TyKaDaZEerHUl0GJ7PnN5GTnqWZzZVhyXaOgiAUdM01HcD4nq4ZlIfyWETj3G_qADrznwVWqcBiDIf0Ymm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش اسرائیل : ما سیستم‌های پدافند هوایی رژیم تروریستی جمهوری اسلامی در غرب و مرکز ایران را نابود کردیم
‏پس از حمله، انفجارهای ثانویه‌ای شناسایی شد که نشان می‌داد موشک‌ها در پرتابگر بوده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/withyashar/14007" target="_blank">📅 14:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14006">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d567e74a89.mp4?token=oL6N1oRqE03oNxNoFMVYbYiSn5PKzUVUd5CJdPBP5fXxoY2LNySJfzY8Mc2yQB1BwP8ON_4OgwZdi6PupHIId0GX248paG91Kb00_W_TETX-06WB92wd1bEPzLHGy0BIP-gcf6Qb0s2giz-PqiXTVAkOwWjlV41-eJsVsHbP9_hkhLmpNcKoQ6a5EgmNaCDrpZ1to2jYyp075DzNvHMCJmtdUB8e8hwDvTxGTwXjOKbheQ5paxjj1FYft2ER3ipySqRHBlWx20dKQKOJHy8CzwxEkuNQCLReWh42dGKzWLeEMD3RMkZBUZ6LFUIpvW6wF5BPiUXpTfDCgMcSwPLd1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d567e74a89.mp4?token=oL6N1oRqE03oNxNoFMVYbYiSn5PKzUVUd5CJdPBP5fXxoY2LNySJfzY8Mc2yQB1BwP8ON_4OgwZdi6PupHIId0GX248paG91Kb00_W_TETX-06WB92wd1bEPzLHGy0BIP-gcf6Qb0s2giz-PqiXTVAkOwWjlV41-eJsVsHbP9_hkhLmpNcKoQ6a5EgmNaCDrpZ1to2jYyp075DzNvHMCJmtdUB8e8hwDvTxGTwXjOKbheQ5paxjj1FYft2ER3ipySqRHBlWx20dKQKOJHy8CzwxEkuNQCLReWh42dGKzWLeEMD3RMkZBUZ6LFUIpvW6wF5BPiUXpTfDCgMcSwPLd1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان کرج سمت میدان استاندارد و فردیس
@withyashar</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/14006" target="_blank">📅 14:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14005">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رسانه های رژیم با ذکر الله اکبر ،  نوشتند تنگه هرمز کامل بسته شد @withyashar</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/withyashar/14005" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14004">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر آموزش و پرورش اسرائیل: تعطیلی مدارس فردا سه‌شنبه نیز ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/14004" target="_blank">📅 14:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14003">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرنگار I24News خطاب به پست رئیس جمهور ترامپ:
من واقعاً نمی‌دانم این مذاکره درباره چیست
این مذاکرات به مدت یک هفته و نیم به دلیل لجاجت ایرانی‌ها متوقف شده است. پیام‌های ترامپ هر روز خجالت‌آورتر می‌شوند
و تا جایی که می‌دانم، اسرائیل خواستار آتش‌بس فوری نیست
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/14003" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14001">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcEJyyrNmcse30ytnETLJR8U2LJucwAee-xMAJS8DhrU4Fw7vBG4aMfgKNkZlbcsMHcOCV5PJpH-dG1mWLQ7e1VaNRU3I2ulfgMva8VUxyt3zOnaQntrzQv0y70PXbVRLcULMnLlHA9-X4cED--1t3M43oHPXNkZOJfU0gTay0I29pemygOKeqwrVOC__I4TZqm5syCkTWFddRCSDcpbX6Vi8hnFVg6Abf0O5nSqIhtdmWWvVFzbRit0SlioPKy3XnGXu6HBsqzCfbUvgQnf__ZlTik2yO74_kXT5El3WCAKw9Ay1JuiG_SRd2AXqCph8AvwC0iPpaepIZhPMiQH6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
محاصره به قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
@withyashar</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/14001" target="_blank">📅 14:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14000">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8r3D60-kghPLzPWiOE-rlaH7V03yMJyPuAnbMYO_PHg4DXXZ1h90EeZ8eB-54j4MnYklEXN7fF7jQIbMFVyOfF0lxK6Ra_eDKlDJLFsZ9GY9tTfjzeXzDzfci7KNb8dZLSNsx_C_Le1XmH_A-7jdgGeSoOB4KTCTGs2CRF6Mx3_Q122d8dpvTJLCW0424ybDKVFGgnKC58oTn2w4ygFpHC8EYHReJp2Ocs7IeI-YFFwROcpKkI7DiYhQV2d4ZE-205q7M6UkshFPruIvSJPJ_CzOnCGlmQvqLpq7YQBhiOVpa7ZUzbOHG2INXPy5QiBbrAp-BrZMKgzBGkwVXNS_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود از انفجار در شیراز، ساعتی پیش
@withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/14000" target="_blank">📅 14:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13999">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رسانه های رژیم : پدافند یزد فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/13999" target="_blank">📅 14:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13998">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1b83882f.mp4?token=EznLXaNilvyVuUH4xXcwouRCui8QjBOZIh_dPT482PNNJkjpEHXKDJA-GeIzqySlnCeTnaiBhuixjPEfMqqXLLqQPUgOnBG6-BJTX_mkhiwTvCOmzQ9GpqFPHE_D05Tfn1kG9SbbhcERVvGR0IEd4ZASUS2G9BBEhyWNnZjp7xkCYCpHy8o__nSXuiksyMeA0_SxvFXTnELgRtF3L0oshDY35Ib5OM8ebnKkRilU2rmKFqYibHce7d7Ky3xCGQYbrKC9sP4WCm47jAm9vNfBAJlAhYupX7YRg3RMmwV93815Oiy0Kb2bZK99RGzL9Da05M1HTijwwTAbqT-RpVVzbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1b83882f.mp4?token=EznLXaNilvyVuUH4xXcwouRCui8QjBOZIh_dPT482PNNJkjpEHXKDJA-GeIzqySlnCeTnaiBhuixjPEfMqqXLLqQPUgOnBG6-BJTX_mkhiwTvCOmzQ9GpqFPHE_D05Tfn1kG9SbbhcERVvGR0IEd4ZASUS2G9BBEhyWNnZjp7xkCYCpHy8o__nSXuiksyMeA0_SxvFXTnELgRtF3L0oshDY35Ib5OM8ebnKkRilU2rmKFqYibHce7d7Ky3xCGQYbrKC9sP4WCm47jAm9vNfBAJlAhYupX7YRg3RMmwV93815Oiy0Kb2bZK99RGzL9Da05M1HTijwwTAbqT-RpVVzbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از حمله به یک کشتی باری با پرچم پالائو با ۲۴ خدمه هندی در نزدیکی تنگه هرمز ساعتی پیش , بر اساس این گزارش‌ها، در این حمله موتورخانه کشتی هدف قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/13998" target="_blank">📅 14:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13997">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سخنگوی وزارت خارجه چین : پکن به‌شدت نگران وضعیت فعلیه
@withyashar
🥴</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/13997" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13996">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کابینه جنگ اسرائیل امشب ساعت 9 به وقت اسرائیل تشکیل جلسه خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/13996" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13995">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سرپرست سرکنسولگری ایران در کربلا: هماهنگی‌های لازم با عراق جهت انتقال حجاج انجام شده است
@withyashar
حجاجی که نیومده بودن باید برن عراق زمینی‌ بیان</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/13995" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13994">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/13994" target="_blank">📅 13:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13993">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034343a08d.mp4?token=TQulKsovpCHnZG0K8JwVO6t0BcxYegk2Bi_xVQYMZRcIehv1b6V32IlMtfR_TQNkx-10cl2YVCAAr-f7EsUVf5Xnh_996B8lmt-MbijFAeLELuQpm9SVcIIBR3OzUS1LtRsNXG3C4ZZmILAabII-3_yL4sXRqMMrST5Vo-KNFAWlXROXtPSB3sNDd4W9a00iUiKJHSRZJjBEfvnSR4_jkiWxf_CxEvWxJW9bxOT2PL7Fc7vCBT_0sImMboFBxI1UcjwT634W7MAnc2PqMu-l0TboCgaO8OXXxdPorVQxlmPakfo-iJgP1WIrcmRoAP3enswrEeBv2RVeHVfts3nVTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034343a08d.mp4?token=TQulKsovpCHnZG0K8JwVO6t0BcxYegk2Bi_xVQYMZRcIehv1b6V32IlMtfR_TQNkx-10cl2YVCAAr-f7EsUVf5Xnh_996B8lmt-MbijFAeLELuQpm9SVcIIBR3OzUS1LtRsNXG3C4ZZmILAabII-3_yL4sXRqMMrST5Vo-KNFAWlXROXtPSB3sNDd4W9a00iUiKJHSRZJjBEfvnSR4_jkiWxf_CxEvWxJW9bxOT2PL7Fc7vCBT_0sImMboFBxI1UcjwT634W7MAnc2PqMu-l0TboCgaO8OXXxdPorVQxlmPakfo-iJgP1WIrcmRoAP3enswrEeBv2RVeHVfts3nVTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش السیسی محموت احمدی‌نژاد
🤣
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/13993" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13992">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYihxtfY8hIB7CCL_5btaQYLqnRclSTCqkDFCusxTLq0fQm51gYVWTjrixoY4m0eD2Z9-fxVUbQnqyKNWlXnyP8cHGZT1UVcOOacSNLAH_9tIiEM7QxojrMSZqPd9FAu5pEXx2O0g17rWQACHwk7sQxkm2vkpey0b5MwOjDC1qfloozaiPoXg19NDah5Klqgqda_H8ff14FJV7dwW2q-tG6f7ENUUtt0bWRxDeRoFeADCu37p2jwC25VUfw2wF32ExUlfVwmG7rQBNrsq3rK6XI1YgYg2zbGv6nBE80th3H2eH2aoulOgQTRIRMzGuuRTN-PP_HZkGSjmDL9yxAIlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل به سایت موشکی تنگه کنشت کرمانشاه
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/13992" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13991">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یک منبع نظامی به تسنیم: ایران برای جنگ طولانی مدت آماده شده است
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/13991" target="_blank">📅 13:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13990">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رسانه های عبری: درگیری ها تا ساعات آینده گسترده و سنگین‌تر خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/13990" target="_blank">📅 13:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13989">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
تنقلات خود را آماده کنید</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/13989" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13988">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک منبع ارشد نظامی در ایران: حزب‌الله  روزهای آینده نشان خواهد داد که محاسبات اسرائیلی‌ها و آمریکایی‌ها همیشه اشتباه است، و ایران ثابت کرده که دوستان خود را رها نمی‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/13988" target="_blank">📅 13:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13987">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فارس: تو غرب تهران پهپاد زدیم
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/13987" target="_blank">📅 13:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13986">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ با لهجه استانبلی
🤣
:
📿
الله لله</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/13986" target="_blank">📅 13:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13985">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند. پرزیدنت دونالد جی. ترامپ @withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/13985" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13984">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند. پرزیدنت دونالد جی. ترامپ @withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/13984" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13983">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مسافران محترم قاهره لطفا آرامش خود را حفظ کنید دایرکت جای  فحش‌به ترامپ نیست از مسیر لذت ببرید
🙌🏾
😁
مدیریت حمام اتاق جنگ</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/13983" target="_blank">📅 13:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13982">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">همکنون دو تا از رادار های بیدگنه رو زدند
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/13982" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13981">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orXOlj63jMfLTwUQJpjIvVTsn4cLt474fCzJFC0gC9-gIVAw9v-bkGjkc46SOqn0_lF4zMV5KSYSRG0hywgG0W9Kx69EBIFoyJp_y8cPmm7zCcZKk1pGAqFg4jNEuH9KOVAFv072ON5qZ3GQlBuc6CPGJjYPhxS6cQlhyoNdFzoo6g8NWhjCoij6MRAgwR_8xCwf98RAXIGG6Mi1AMWCWjyspgNNYXk7qGjCDiYo0qvW9_uA9GzXmJ75kknxacOTGzyqZpOfGN_5MpZXakX4A1tnnTXhIIcsM8b16qKwmOvyk2Da67Bp_TYuNB7Xk42rUPlZpmDJkBeHETc9XiuaRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند. پرزیدنت دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13981" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13980">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کابینه امنیتی اسرائیل ساعت یازده و نیم پیش‌ازظهر دوشنبه به ریاست بنیامین نتانیاهو تشکیل جلسه می‌دهد.
این مقامات همچنین گفته‌اند هر حمله موشکی ایران به اسرائیل «با حمله در ضاحیه» در لبنان نیز روبه‌رو خواهد شد.
وزیران راستگرای افراطی در دولت نتانیاهو به او گفته بودند در پاسخ به حمله موشکی ایران به اسرائیل، «تهران باید بسوزد».
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/13980" target="_blank">📅 13:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13979">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ارتش اسرائیل: برای احتمال شلیک موشک از سوی حزب‌الله به خاک اسرائیل آماده هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/13979" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13978">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یک منبع آگاه در حوزه ارتباطات به سیتنا اعلام کرد که تاکنون هیچ دستور، ابلاغ یا تصمیمی درباره قطع یا محدودسازی اینترنت بین‌الملل به دستگاه‌های مسئول اعلام نشده است، در همین حال شب گذشته پیک ترافیک اینترنت بعد از قطعی‌ها زده شد.
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/13978" target="_blank">📅 13:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13977">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سازمان ملل از شرایط موجود ابراز نگرانی کرد
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/13977" target="_blank">📅 13:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13976">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کانال 12 اسرائیل: ارتش اسرائیل در حال آماده شدن برای احتمال جنگ طولانی با ایران در حالی که عملیات "غرش شیران" ادامه دارد همچنین در حال حاضر اهداف جدیدی نیز مشخص شده است.
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/13976" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13975">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کانال ۱۲ اسرائیل: تاکنون، ایران بین ۲۲ تا ۲۴ موشک به سمت اسرائیل شلیک کرده است
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/13975" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13974">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رسانه های رژیم با ذکر الله اکبر ،  نوشتند تنگه هرمز کامل بسته شد
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/13974" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13973">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رادیو ارتش اسرائیل: در حمله به حومه جنوبی بیروت تردید نخواهیم کرد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/13973" target="_blank">📅 12:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13972">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فوری رئیس ستاد مشترک کانفیگ فروشان به ادمیرال یاشار رئیس اتاق جنگ گفت :
آماده‌ایم تا به هرگونه قطعی اینترنت پاسخ‌ کوبنده بدهیم
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/13972" target="_blank">📅 12:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13971">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اینترنشنال با استناد به ارتباطات زیرپوستیش : ارتباط مقامات و فرماندهان با مجتبی خامنه ای دچار اختلال شده.
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/13971" target="_blank">📅 12:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13970">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldS3M0YejUfWpX-u-M57TNMR3Gdzr817xT4TZVSCsNKD2xrUB1wzQ9rDhCVZ2z-vYFWPc0AO6MItFSLO_dS5kbupGFJf5RZzZslKM8uxLSOq5OzTb5p9IHtAM19aU4Y6Dhhk6-2G5xQLqhVe60skYz_YMK64FJHzWOyr9JQDtOi9qPsrnOEkIcJ7NsIM2GzimYoLcCC8ZOt81RipsCeGG_9T0aCEsxx0MDsXv5vC1lody2C5weZWFZkzsEeylVRixVr3hK1Q3qLMn_cZ-911G2q0Hca1qJjZyYv1aSkIOnUY7UVLcXlct_D4ao_blwMhdBqQuWVv29FFE6L0C-Pr-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پیش ایران موشک به سمت اسرائیل پرتاب کرد که گویا وسط دریا خورده
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/13970" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13969">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اگه تازه بیدار شدی بدون که آتش بس آمریکا و ایران همچنان پا برجا است
🥴
🤣
@withyashar
ترامپ هم کابل رو گرفته و پستهای انتخابات میزاره…</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/13969" target="_blank">📅 12:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13968">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تن و بدن عرزشیها داره تو دایرکتها میلرزه و چرتو پرته که مینویسن
😁
. اینها به هیچ وجه فکر نمیکردن که دوباره حمله شکل بگیره.
@withyashar
با عرزشی سوز ترین رسانه نسل شیک پاسارگادی با شما هستم.
✌🏾</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/13968" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13967">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ارتش اسرائیل گزارش می‌دهد که حملات به ایران تنها توسط اسرائیل انجام شده است و هیچ مشارکتی از سوی آمریکا نبوده است
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/13967" target="_blank">📅 12:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13966">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دایرکت پر شده از مسیج‌هایی که چرا نمیشه تو چنل عضو شد. من اون سمت توی گوشی شما نیستم این علت رو بدونم ولی محتمل‌ترین حالت لیمیت شدن شما به علت استفاده از فیلتر شکنه ، اگر IP تون رو یا ساده بگم فیلتر شکنتون رو عوض کنین این مشکل حتماً حل میشود.</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/13966" target="_blank">📅 12:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13965">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رسانه های رژیم: خبر ترور فرماندهان یا مسئولان کذب است؛ هیچ تروری تاکنون انجام نشده است
@withyashar
یاشار : حالا نیس اینا خیلی گردنم میگیرن !
🤣
اول همیشه اسرائیل اعلام کرده</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13965" target="_blank">📅 12:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13964">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">روسیا الیوم نوشت: ترامپ به پیاده کردن نیروهای ویژه در ایران تهدید کرد.
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/13964" target="_blank">📅 12:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13963">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خبرهایی پخش شده از حمله به ایست بازرسی ولی هیچ گزارش مردمی در این رابطه به دستم نرسیده. به نظر من این خبر فیک برای توجه یا امید واهی است، فعلاً! ولی حتماً شروع و انجام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13963" target="_blank">📅 12:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13962">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">صدای جنگنده مرکز تهران
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13962" target="_blank">📅 12:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13961">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد
بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13961" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13960">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2689f38b.mp4?token=lB-desvsLxc3hzzpJwVXc-heC0zT9SLFpPytZxd_11jdI-QZLw_rZrZHUFKI8u7udNiewrHUaIlPyMr5Y7LQM5fpWrHsnkzKVQbXB_qoltBQotD4SYu-oMc7nVuRlAbpv155Zfl7ZiSw6tHupOyDRO0z16u2mRw_CUf5BRTMbUvvRBbh91W-_7ySjKvl_jJ-mdGAWXThX66gv0V4knPp2sH4hbzb60fdVkzphEtMhvnUWpgFS3_febFvWOc4dCBm5OMu1Ecg5K8RDvf82JgQyCWhCyXtSIBqIye90ngpUx-bxngjmgBJPzdQYJ7IjIkIKP9_0l0WtbszbdJL3iORlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2689f38b.mp4?token=lB-desvsLxc3hzzpJwVXc-heC0zT9SLFpPytZxd_11jdI-QZLw_rZrZHUFKI8u7udNiewrHUaIlPyMr5Y7LQM5fpWrHsnkzKVQbXB_qoltBQotD4SYu-oMc7nVuRlAbpv155Zfl7ZiSw6tHupOyDRO0z16u2mRw_CUf5BRTMbUvvRBbh91W-_7ySjKvl_jJ-mdGAWXThX66gv0V4knPp2sH4hbzb60fdVkzphEtMhvnUWpgFS3_febFvWOc4dCBm5OMu1Ecg5K8RDvf82JgQyCWhCyXtSIBqIye90ngpUx-bxngjmgBJPzdQYJ7IjIkIKP9_0l0WtbszbdJL3iORlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از پایگاه عظیم کوه معروف یزد الان شلیک شد
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13960" target="_blank">📅 12:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13959">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه سر برم بیت رهبری الان میام
🥴
🙌🏾</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13959" target="_blank">📅 12:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13958">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شهرداری تهران جنگ بیخ داره و داریم پارکینگ‌های زیرسطحیو برای استفاده به عنوان پناهگاه آماده میکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13958" target="_blank">📅 12:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13957">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRyJagRBJZFPrROQ6Y73_MWZpBXCvLjQI5Xn-JAH94IbwFu9gGvM_SJ35X6LKBTWbUrK9A9a_TPixH42mVbgBLgmu9qx0F8t1i0Kfle6PuwmfPEF2qy-dAve-iVha3x6anfsBuVbhHBZHwnIglICf3pGI4a3xdcfdhVNcqwBSa9FHLCgRke_MrZVzrvmrl-smgzo0brLLbbwEcZIK9ZWtF1vp1rPg7sW9Oub31kml9vPPO5k01EO17wX62iA00nvmbmcjnuN9_31k7VcS58BUVB2tIeknEJ92-eqg3EMXHIAC41r65VVm6GvClWcQW1wPl-CEeKuQYBRX3n4B4vhsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰۰،۰۰۰ امین نفر کانال خانوم پی ام
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13957" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13956">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
گزارشهای از یک تررور هدفمند در تهران
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/13956" target="_blank">📅 12:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13955">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJMJ7cAu6SG6hyvDyqi0OhoBYtVNWSfaald0gqMp-kXVXCvLTNq_b5m7MWa367t63RBmeSXvoOjvuhSWJ1UTXKjYM2e1Tl03ZGrD_v4U8l0wPM_yw6Zy6P9_Kq1e6Ayq-P3QFtW8YeEqIgX22QBhGTNy354cDcI4D500Mrnk9G62Yeg0vytZy6qO2fI2CBT63599Rr1FYp9YkCPUXV68lCxb4R8GDk5kn-RPEFl0t118LV_DOp__stC999sfyHeKFcP6k20LT-EaHItmulhLu9yz9R42yVfeEcfx8mHHATSKKtMlVKeHUGEvLqkU2iNzOV3Mp2HqMGozUrt0WLvWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهده دود از شرق تهران
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13955" target="_blank">📅 12:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13954">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سفارت هند در تهران از شهروندان خود می‌خواهد فوراً ایران را ترک کنن
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13954" target="_blank">📅 12:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13953">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رادیو اسرائیل: همکنون نتانیاهو ریاست جلسه‌ای کوچک از هیئت وزیران را بر عهده دارد تا درباره مسائل امنیتی و سیاسی در تمامی جبهه‌ها بحث و بررسی کند.»
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13953" target="_blank">📅 12:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13952">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش چند انفجار در جنوب تهران
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13952" target="_blank">📅 12:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13951">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کان نیوز عبری: نیروی هوایی درحال انجام عملیات در ایران است
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/13951" target="_blank">📅 12:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13950">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فارس: موج جدید حملات موشکی در راهه.
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/13950" target="_blank">📅 12:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13949">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfhjcCCMoxcz-CpqcLgfPVRBYvgmu2-3MEKwpLv2MRThSXsk8lYIccPVhgOVimUQ4aNxAeF_6tkCrREBJZEwx7yTxoHZoOYmTqwbARlacIG4BFYrdE0Bg5P2Hp96afQxf1RPbcDj_-VtDLmT3RTQuyC8sflKuu6Wqt6I0FXebMSeSOxekWSDSZ0Rj5AjdMLMSsoe5xb84ETLQlwh7mnQ0eV6Y4SRbxefZxRwztwkTn-l1iX1SM--wOqFwQUbdztQySaPMvs9gkz4YCoiJGT3l1YVsmLxGZES-0PdPUbhcPlsWGmLuI3ESknt6pfCFzjiGU5djvPImI2Om54zp10Bzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان الان
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/13949" target="_blank">📅 12:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13948">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارشات از انفجار در فرودگاه شیراز
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/13948" target="_blank">📅 12:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13947">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui4Uvg6bn3PRaiNEEUnhouUI60hBDqBXABSIBAfveb7aI6Yl0DkyNarBplEeRpJS_zxReyMK0nK27__6rn5vvPxWYjL_He-fOPv_y-74JilYj6prp__jVoYCxnabrZO_HtdAe4fpFcPEn5U0Ztn8aCamBCs5kPKJOrD8jq7uFAyHcmeZq6VWmLJ5Edjb-Tfz96oTIrAl4SlBkYaJnHczImd3oDNHBeukY9l70_XTo9pfQrCTgCcgiWTU5GdSZ3ehmUAQP2U21l2OyAGLR0iZTLpvQlz7y1HlnmiDG550qGDC3AxyI6aSJoUYidcrdfR3Tz0_SsojwvvPL0E7wPZkAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران الان
@withyashar
این تصویر گویا مال راند قبلی جنگ بوده تکذیب شد</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/13947" target="_blank">📅 12:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13946">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b742c26d9a.mp4?token=gCDh3Q7xONFqzWwubfF8f7ZD_Y9E_tiB38_wlmL8ar3pDqOqYWcC5NjgLTgFRKsfV0eGgGskilpNoBHJvVtL_DPVdrvVIp1t982yidouYoBDKW7TBPRWbf95E3kjlbv-FNQEUSr9DDzSr8xsLRsJ6K_FsPSWSPM7KdQhG5F-UMT7EfqRoqFOlbBKsTxwYWLKTM6fQ1wbw9aDuP8uEvzBGxDZO48lCZHviP0-lukKoAGpd72bFnZoPgLTrrR6hnA5Q3UUPkYkHdWnmr03YkDpTUtIxECawnK7lHUoqMdsAI0smdSOHsiw993v5qx-ey9PLJmxbY6Z6nV919TBSRWcew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b742c26d9a.mp4?token=gCDh3Q7xONFqzWwubfF8f7ZD_Y9E_tiB38_wlmL8ar3pDqOqYWcC5NjgLTgFRKsfV0eGgGskilpNoBHJvVtL_DPVdrvVIp1t982yidouYoBDKW7TBPRWbf95E3kjlbv-FNQEUSr9DDzSr8xsLRsJ6K_FsPSWSPM7KdQhG5F-UMT7EfqRoqFOlbBKsTxwYWLKTM6fQ1wbw9aDuP8uEvzBGxDZO48lCZHviP0-lukKoAGpd72bFnZoPgLTrrR6hnA5Q3UUPkYkHdWnmr03YkDpTUtIxECawnK7lHUoqMdsAI0smdSOHsiw993v5qx-ey9PLJmxbY6Z6nV919TBSRWcew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل : ما یک حمله گسترده علیه سامانه‌های پدافندی راهبردی رژیم تروریستی ایران را تکمیل کردیم
در دوره اخیر، سامانه‌های پدافندی در چندین منطقه مختلف در ایران مستقر شده بودند، در چارچوب تلاش رژیم برای بازسازی توانایی‌های شناسایی و دفاعی خود که در عملیات «غرش شیران» آسیب دیده بودند — این حمله منجر به انهدام این سامانه‌ها شد.
در عملیات «غرش شیران»، ارتش اسرائیل به‌طور عمیق به سامانه‌های پدافندی رژیم تروریستی ایران آسیب وارد کرد. حملات تکمیل‌شده به تعمیق بیشتر آزادی عمل نیروی هوایی در آسمان ایران کمک می‌کنند.
@withyashat</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/13946" target="_blank">📅 12:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13945">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt26w7Z9g6Rb7QEg17edqN1AdFIS7rBsQ5pYcdjFq42hYMRYOeMpdAdQupNmVbGxIo4nEK6y5qTNYdVxS9tADVu0oA_3GZyhu4zLG6GvrjjFOybkdDRtELWlrfLN6zyK5XbC9dJWU4OavY1e_1y-aWi56qjGtIhBajjzmvdfleohJJjaGzljlH49IT38Qo-7VQWdZk4Ap76NHRakFgw0vr0O1tg0CBuyjqn4LMtXOfCrGgK5wJlTD8vl8eNXrYeCpW3AoWaArTwtvJ7eCHeR81g1Cn5CQKOAaEaRJjTsfKog7CYNHXldDAj3eGFMDo-y4NQUUJUHWAzeBlse2Y61qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمس آباد تهران
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/13945" target="_blank">📅 11:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13944">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دانشگاه هوا فضای عاشورا رو زدن
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/13944" target="_blank">📅 11:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13943">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNRCYdEImd8qgR7evBv6tI4HliX9XEFQHAFUZO--NC9hileBWI4hO7-JaaHYHBz2MTRjzzuE6UAyAYu9r60tQtrmxOSTPzkC9_SnW1wlulsqSiNFM-oH6w5oHMMSl-H1koQEOGqwK41xORG1V3gqP1i0-NfxdnnI-gR1Yold2fUGgfc1A9swPyf78G9KxiLe8aMv-h2xD_HoC0ktpBSXQGCiLXW4J3AYe92sd8ff0UQztQLAL_YCs91zMBb1YJYholSOIj2jU9ptwkS-EstyzLtA0oF-mc9FqUJckPFl9c37TByH5YaxW4Zzb74TkHU2AcECtamKtxrsfhU0xEdasA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار شهرری صدا انفجار اومد ۵ مین پیش فکر کنم پالایشگاه زدن ستون دود دیده میشه @withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/13943" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13942">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">غرب تهران مثل مرز  بوسنی و هرزوگبین شده یاشارررررر
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/13942" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13941">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تبریز رو بد زدن یاشار
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/13941" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13940">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یاشار اصفهان رو زدنننننن لشگر ۸ زرهی
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/13940" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13939">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🥲
انرژی‌من به انگشت شما بنده</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/13939" target="_blank">📅 11:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13938">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یاشار شهرری صدا انفجار اومد ۵ مین پیش فکر کنم پالایشگاه زدن ستون دود دیده میشه
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/13938" target="_blank">📅 11:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13937">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فارس: شنیده‌شدن صدای انفجار در غرب تهران
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/13937" target="_blank">📅 11:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13936">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پدافند فردوسی و شرق تهران فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/13936" target="_blank">📅 11:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13935">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کرج سمت بیدگنه صدای انفجار شنیده شد
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13935" target="_blank">📅 11:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13934">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجار در اصفهان شنیده شد
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13934" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13933">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آغاز موج جدیدی از حملات هوایی به تهران
حمله به دانشگاه هوا فضای عاشورا
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13933" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13932">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجار در کرمانشاه
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13932" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13931">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شنیده شدن صدای انفجار در اسلامشهر و ملارد و کهریزک و باقرشهر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13931" target="_blank">📅 11:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13930">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پدافند تهران فعال شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13930" target="_blank">📅 11:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13929">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">صدای انفجار در تهران و کرج شنیده شد
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13929" target="_blank">📅 11:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13928">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گویا دیتاسنتر آسیاتک قطع شد
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13928" target="_blank">📅 11:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13927">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سخنگوی وزارت خارجه: حمله‌ای به عربستان انجام نداده‌ایم.
نیروهای مسلح ما به هر هدفی حمله کنند، آن را صراحتاً اعلام می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13927" target="_blank">📅 11:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13926">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سپاه: حمله دشمن به صنایع پتروشیمی پاسخ داده شد.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13926" target="_blank">📅 11:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13925">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ecb277ac3.mp4?token=gLi3L9fQlptrgO-G0bLXz5c9M_aWIyjOf3pBi8TPoymP1HQQ20FbRdjO13Nrc_AWiPlS9r_BBDFYLEM-TEFOeTMScIukZIGRjOdPtzJ5aMLsfPs92pLe8esqyPuRdYKiMPa3yKLaJ46z54rLTdpLq9Ey4_Bve_jq_UAeFLFNYdCxCmFc6PVncyy0k9RiECW0RqqhUyjv_wOc9nxnDzEw0SLua9lq44yN0nb3X30Q44j7OJHQgM5mFEM-GiaK0WJ8tLkxJPwJY7iaEZXnk9b85-gt_BRDnBkngpzBF63kup0eCv8fndakfTAlQA3XrOJn2B637iTp58O6Jv4oBLCVBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ecb277ac3.mp4?token=gLi3L9fQlptrgO-G0bLXz5c9M_aWIyjOf3pBi8TPoymP1HQQ20FbRdjO13Nrc_AWiPlS9r_BBDFYLEM-TEFOeTMScIukZIGRjOdPtzJ5aMLsfPs92pLe8esqyPuRdYKiMPa3yKLaJ46z54rLTdpLq9Ey4_Bve_jq_UAeFLFNYdCxCmFc6PVncyy0k9RiECW0RqqhUyjv_wOc9nxnDzEw0SLua9lq44yN0nb3X30Q44j7OJHQgM5mFEM-GiaK0WJ8tLkxJPwJY7iaEZXnk9b85-gt_BRDnBkngpzBF63kup0eCv8fndakfTAlQA3XrOJn2B637iTp58O6Jv4oBLCVBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موقعیت دقیق لانچر پرتاب کنندهی موشک در ابهر
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13925" target="_blank">📅 11:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13924">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مسئول سیاست خارجی اتحادیه اروپا امروز از اعمال تحریم‌های بیشتر بر ایران به بهانه بسته‌بودن تنگه هرمز خبر داد.
کالاس در گفتگو با خبرنگاران پیش از ورود به نشست غیررسمی وزیران دفاع کشورهای عضو اتحادیه اروپا در قبرس، گفت: «امروز اولین باری خواهد بود که تحریم‌های مربوط به آزادی ناوبری علیه ایران اعمال می‌شود».
@withyashar</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/13924" target="_blank">📅 11:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13923">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcFEHd3OdMwI5h05LEeJmBDdHO9TUpJL9_MXkfjl2nXL6OmmbF0AqS0WlvHJk9Cbp3GZgLaVILqLy4BtTQyXIvtNjQzIiFC1Tj4gNEUd5HSmqYwcGyrhL4Z5Qu-_KqtnNo1DxDFsZvedtpoCuOiJMcJsA7mgJo7B1nN_zZYtsa4A_lVkaXImICVHOxSdsEN_SzDMYE1BKxAPaUMd4j3UMa3IQJ1CVz8MzvEigAq_nfgQt90QjDoIMzON6kqqJcfj0vm-73OvEqBZImbzHGoTRCRRW-0DI5Iqhe0TSn4resnJzhpSt9j9Ra9RN98ioHwBCeVrN09pwMXS_YLJvaOJ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاطی که امروز تا این لحظه توسط ارتش اسرائیل هدف قرار گرفته
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13923" target="_blank">📅 10:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13922">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
موج بعدی حملات اسرائیل آغاز شد
@withyashar</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/13922" target="_blank">📅 10:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13921">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIhZZ_h_igW7T8asT_dEZRL4QKfYbHpeWA-N8TLZkg8X3gGl2XdYZhS50U_WvdTci75NSfcGRLqrnQIGIkk6nHtLfJHyE2NTYnul2G-T5iAxlXxbabDFsIP9S7JhkhNgSjej_rlF9Vj4YXXaixmPw9TKufMOBBkYMX5tafcFmmYjgZoo5AaGxKfN9r7w2jg--OfS-7hKP1FMprVoIKNHmz7CpcD_cfkS4oqmr-O21INVob0XRMon7Bdyn6b5BxMdEEW3q1K97x2JN3az2SHjBgw18mfQKja3uwH82fmQ3RxuJJwLmCOpgivLeW8nSd75pSE0qQEB-l4o3yJknht6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/13921" target="_blank">📅 10:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13920">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">برخی منابع از شنیده شدن انفجارهای قوی در پایگاه هوایی ریاض پایتخت عربستان خبر دادند.
@withyashar
پیشتر ایران حمله به عربستان رو رد کرده بود ممکنه از طرف انصار یمن باشه</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/13920" target="_blank">📅 10:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13919">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b559da1eaa.mp4?token=ZcZAdYOuPhLAFHRskoE9lMlEAxWJBufzuTz3Ixee8SmKPzawSydNj-DwNpA-auKgPa1C5o586XZKnWlLY57ASQHHLaAK-zCI8qzigm93CAPXRwl5cQx1WdwemJUqyNW_86844EpYyKpRXaE7d9qr04962wmrbrGORla9RwlK8JyKybNxn-ksohR_xTVD5esSG3tlOOBEZXHKzJMBIWm_VI5KZ69eIYOVGSN0S5IQZihWted6ULvyaRi89x-oXY5XcZ8YcToAzhx6BQAIFwDgwBLQwIwGcT0jQ-2nmTGE0JMwSW9zUmM2HWoo05yi0ko25vSrFN_0HxHoqJqJ0aN76w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b559da1eaa.mp4?token=ZcZAdYOuPhLAFHRskoE9lMlEAxWJBufzuTz3Ixee8SmKPzawSydNj-DwNpA-auKgPa1C5o586XZKnWlLY57ASQHHLaAK-zCI8qzigm93CAPXRwl5cQx1WdwemJUqyNW_86844EpYyKpRXaE7d9qr04962wmrbrGORla9RwlK8JyKybNxn-ksohR_xTVD5esSG3tlOOBEZXHKzJMBIWm_VI5KZ69eIYOVGSN0S5IQZihWted6ULvyaRi89x-oXY5XcZ8YcToAzhx6BQAIFwDgwBLQwIwGcT0jQ-2nmTGE0JMwSW9zUmM2HWoo05yi0ko25vSrFN_0HxHoqJqJ0aN76w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رهگیری در شمال اسرائیل
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/13919" target="_blank">📅 10:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13918">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a47faa1692.mp4?token=M0PHjbblKKauOKXEpFxhkgXkeRpPvizTtc0gsBszNGL9hB2GKKywoQFGyPptyyx-if6diHkfOyX8AhSwOnkjgrwHWhrVhzH-ahdAEtrZ92guN6b4FqypZTK2uuUT-34nhCApyTrOkh5I1bUDHM-N8GqFZY6Ts7hRl48EWJrfAMP7uvoRvAOnPfgkpKa-JX1pPoAFPHbuf042Upz30op0lgoJkjI938n3UvqW0XO7yj8OmYh-FOvVcWCMLQQJtm1_7KLmEXap7vg7qyDBONRIonTalp2AJZK722UXP2eNm3G0Su3C2IyI97Y284paT4FqR2-uy7GnBo0Y0t4pViwvdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a47faa1692.mp4?token=M0PHjbblKKauOKXEpFxhkgXkeRpPvizTtc0gsBszNGL9hB2GKKywoQFGyPptyyx-if6diHkfOyX8AhSwOnkjgrwHWhrVhzH-ahdAEtrZ92guN6b4FqypZTK2uuUT-34nhCApyTrOkh5I1bUDHM-N8GqFZY6Ts7hRl48EWJrfAMP7uvoRvAOnPfgkpKa-JX1pPoAFPHbuf042Upz30op0lgoJkjI938n3UvqW0XO7yj8OmYh-FOvVcWCMLQQJtm1_7KLmEXap7vg7qyDBONRIonTalp2AJZK722UXP2eNm3G0Su3C2IyI97Y284paT4FqR2-uy7GnBo0Y0t4pViwvdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پتروشیمی ماهشهر
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/13918" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13917">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صداوسیما: موشک‌هایی از ایران و لبنان به سمت حیفا و شمال اسرائیل شلیک شد
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/13917" target="_blank">📅 10:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13916">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش از صدای انفجار در قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/13916" target="_blank">📅 10:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13915">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اسرائیل : ما تمام موشکهارو رهگیری و  منهدم میکنیم چیزی میفته لاشه موشکاست
@withyashar</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/13915" target="_blank">📅 10:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13914">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تمامی پروازهای فرودگاه کرمانشاه تا اطلاع ثانوی لغو شد
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/13914" target="_blank">📅 10:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13913">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">از محدوده تبریز موشک بلند شد
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/13913" target="_blank">📅 10:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13912">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">توییت ایلان ماسک درمورد ایران:
« تنگه هرمز به نام اهورا مزدا از زرتشتیان نام گذاری شده »
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13912" target="_blank">📅 10:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13911">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f3d3553b.mp4?token=DrUEAW0DqFyy0XJTeIpQnZ8EI0k_3zHetc4WwQF2zKiSEm_9TJft86C0IX-Eap82wGzVjkVQ3tOVCBFHEI0EK8LP6sZkOeRjbVkyeOfDu-ub-cxdJ8fbOYvI2NvwMSfRDyLoP0AOX4A7QOOcD0whi_HOARrXQYH_FcDa9YOzdUMp9-GixR3gHkVgksu2Z1hV4BlVR-DthJiyjQ4LQuysFMF1V_oFMAJNU9FVh1QksySBEV27YX2oYmpi_YPyCezm1To4RPu4kWXpAa-rV8JA5jqkftGAWI4zRE4xfPHOTD8zy1irg_ttt1ZmIjBOl0EuHGWAPj_2u-UZHdYPUr0lEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f3d3553b.mp4?token=DrUEAW0DqFyy0XJTeIpQnZ8EI0k_3zHetc4WwQF2zKiSEm_9TJft86C0IX-Eap82wGzVjkVQ3tOVCBFHEI0EK8LP6sZkOeRjbVkyeOfDu-ub-cxdJ8fbOYvI2NvwMSfRDyLoP0AOX4A7QOOcD0whi_HOARrXQYH_FcDa9YOzdUMp9-GixR3gHkVgksu2Z1hV4BlVR-DthJiyjQ4LQuysFMF1V_oFMAJNU9FVh1QksySBEV27YX2oYmpi_YPyCezm1To4RPu4kWXpAa-rV8JA5jqkftGAWI4zRE4xfPHOTD8zy1irg_ttt1ZmIjBOl0EuHGWAPj_2u-UZHdYPUr0lEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک جدید از ابهر زنجان
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13911" target="_blank">📅 10:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13910">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اتحادیه اروپا: طرفین فورا جنگ رو متوقف کنن
@withyashar
😁
🥴</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/13910" target="_blank">📅 10:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13909">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جروزالم پست: سپهبد ایال زامیر، رئیس ستاد کل ارتش اسرائیل، در پی حمله موشکی روز مهرشید جمهوری اسلامی به اسرائیل، چندین بار با دریاسالار برد کوپر، فرمانده،فرماندهی مرکزی ایالات متحده (سنتکام)، گفتگو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/13909" target="_blank">📅 10:18 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
